"""Check each current paper's TeX graph, labels, citations and source coverage.

Run from the repository root. This checks source integrity, not mathematical
proofs or the output of LuaLaTeX. Independent papers are checked separately:
a label in one paper must not silently satisfy a reference in the other.
"""
from collections import Counter
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("nc-cubic", "cubic-quantization")


def without_comments(text):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())


def audit(name):
    main = ROOT / "papers" / (name + ".tex")
    seen, contents = set(), []

    def read_source(path):
        path = path.resolve()
        if path in seen:
            raise AssertionError(f"{name}: repeated or circular TeX input: {path}")
        assert path.is_file(), f"{name}: missing source: {path}"
        assert path.is_relative_to(ROOT), f"{name}: external source dependency: {path}"
        seen.add(path)
        text = without_comments(path.read_text(encoding="utf-8"))
        contents.append(text)
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            child = ROOT / target
            if not child.suffix:
                child = child.with_suffix(".tex")
            read_source(child)

    read_source(main)
    text = "\n".join(contents)
    labels = Counter(re.findall(r"\\label\{([^}]+)\}", text))
    duplicates = sorted(k for k, v in labels.items() if v > 1)
    assert not duplicates, f"{name}: duplicate labels: {duplicates}"
    refs = set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text))
    assert refs <= labels.keys(), f"{name}: missing labels: {sorted(refs - labels.keys())}"
    items = Counter(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
    assert all(v == 1 for v in items.values()), f"{name}: duplicate bibliography keys"
    citations = set()
    for value in re.findall(r"\\cite\w*(?:\[[^]]*\]){0,2}\{([^}]+)\}", text):
        citations.update(k.strip() for k in value.split(","))
    assert citations <= items.keys(), f"{name}: missing citations: {sorted(citations-items.keys())}"
    assert "\\author{}" in main.read_text(encoding="utf-8"), f"{name}: keep author blank"
    print(f"OK {name}: {len(seen)} TeX sources; {len(labels)} unique labels; "
          f"{len(refs)} referenced labels; {len(citations)} cited bibliography keys.")
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=PAPERS, action="append")
    args = parser.parse_args()
    seen = set()
    for name in args.only or PAPERS:
        seen.update(audit(name))
    if not args.only:
        present_tex = set((ROOT / "papers").rglob("*.tex"))
        assert present_tex == seen, f"Unused TeX sources: {sorted(present_tex-seen)}"
        print(f"OK: both independent source graphs cover all {len(seen)} paper TeX files.")
    print("LIMIT: source integrity only; not a proof audit or typesetting check.")


if __name__ == "__main__":
    main()
