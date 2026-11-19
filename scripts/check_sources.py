"""Check the current TeX input graph, labels, references and bibliography keys.

Run from the repository root. This is a source-integrity check, not a proof check
or a replacement for LuaLaTeX compilation.
"""
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "papers/nc-cubic-n-fold.tex"


def without_comments(text):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())


seen = set()
contents = []


def read_source(path):
    path = path.resolve()
    if path in seen:
        raise AssertionError(f"Repeated or circular TeX input: {path}")
    assert path.is_file(), f"Missing source: {path}"
    assert path.is_relative_to(ROOT), f"External source dependency: {path}"
    seen.add(path)
    text = without_comments(path.read_text(encoding="utf-8"))
    contents.append(text)
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
        child = ROOT / name
        if not child.suffix:
            child = child.with_suffix(".tex")
        read_source(child)


read_source(MAIN)
text = "\n".join(contents)
labels = Counter(re.findall(r"\\label\{([^}]+)\}", text))
duplicates = sorted(k for k, v in labels.items() if v > 1)
assert not duplicates, f"Duplicate labels: {duplicates}"
refs = set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text))
assert refs <= labels.keys(), f"Missing labels: {sorted(refs - labels.keys())}"
items = Counter(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
assert all(v == 1 for v in items.values()), "Duplicate bibliography keys"
citations = set()
for value in re.findall(r"\\cite\w*(?:\[[^]]*\]){0,2}\{([^}]+)\}", text):
    citations.update(k.strip() for k in value.split(","))
assert citations <= items.keys(), f"Missing citations: {sorted(citations-items.keys())}"
tracked_tex = set((ROOT / "papers").rglob("*.tex"))
assert tracked_tex == seen, f"Unused TeX sources: {sorted(tracked_tex-seen)}"
assert "\\author{}" in MAIN.read_text(encoding="utf-8"), "Keep author blank"
print(f"OK: {len(seen)} TeX sources; {len(labels)} unique labels; "
      f"{len(refs)} referenced labels; {len(citations)} cited bibliography keys.")
