"""Build all three LuaLaTeX papers until their cross-paper references stabilize.

Requires latexmk, LuaLaTeX, LuaTeX-ja and the packages used by the shared preamble.
Generated PDFs, aux files and console logs stay under build/ and are not tracked.
"""
from pathlib import Path
import argparse
import hashlib
import re
import shutil
import subprocess
import sys

from check_sources import PAPERS, ROOT, audit


def label_state():
    state = []
    for name in PAPERS.values():
        aux = ROOT / "build" / (name + ".aux")
        text = aux.read_text(errors="replace") if aux.exists() else ""
        # Bibliography numbers and page numbers also affect the imported output.
        state.extend(line for line in text.splitlines()
                     if line.startswith(("\\newlabel", "\\bibcite")))
    return hashlib.sha256("\n".join(state).encode()).hexdigest()


def unresolved(name):
    text = (ROOT / "build" / (name + ".log")).read_text(errors="replace")
    patterns = (r"(?:Reference|Citation) .+ undefined", r"There were undefined references",
                r"LABELS NOT IMPORTED", r"multiply defined", r"Missing character:")
    return [line for line in text.splitlines() if any(re.search(p, line) for p in patterns)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-rounds", type=int, default=4)
    args = parser.parse_args()
    if args.max_rounds < 2:
        parser.error("at least two rounds are needed to verify external references")
    if not shutil.which("latexmk"):
        parser.error("latexmk is not on PATH")
    audit()
    (ROOT / "build").mkdir(exist_ok=True)
    previous = label_state()
    for round_number in range(1, args.max_rounds + 1):
        for name in PAPERS.values():
            log = ROOT / "build" / (name + ".compile-output.txt")
            print(f"Build round {round_number}: {name}", flush=True)
            with log.open("w") as output:
                proc = subprocess.run(
                    ["latexmk", "-lualatex", "-g", f"papers/{name}.tex"],
                    cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
            if proc.returncode:
                print("\n".join(log.read_text(errors="replace").splitlines()[-55:]), file=sys.stderr)
                raise SystemExit(f"Build failed: {name}; see {log}")
        current = label_state()
        problems = {name: unresolved(name) for name in PAPERS.values()}
        if round_number >= 2 and current == previous and not any(problems.values()):
            print(f"OK: all three PDFs and cross-paper references stabilized after {round_number} rounds.")
            print("LIMIT: successful typesetting does not verify mathematical proofs.")
            return
        previous = current
    for name, messages in problems.items():
        for message in messages[:15]:
            print(f"{name}: {message}", file=sys.stderr)
    raise SystemExit("External references did not stabilize; inspect build/*.log.")


if __name__ == "__main__":
    main()
