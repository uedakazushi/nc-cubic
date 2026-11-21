"""Check the three manuscripts, their explicit cross-references and source ownership.

This validates source integrity, not mathematical proofs or typeset output.
Run from any directory; TeX inputs remain relative to the repository root.
"""
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import os
import re

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    "main": "nc-cubic",
    "moduli": "cubic-moduli-descent",
    "mixed": "mixed-sklyanin-cubics",
}
SHARED = {ROOT / "papers/common/preamble.tex", ROOT / "papers/references.tex"}


def without_comments(text):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())


def source_graph(name):
    seen, contents = set(), {}

    def visit(path):
        path = path.resolve()
        assert path not in seen, f"{name}: repeated or circular input: {path}"
        assert path.is_file(), f"{name}: missing source: {path}"
        assert path.is_relative_to(ROOT), f"{name}: external source: {path}"
        seen.add(path)
        text = without_comments(path.read_text(encoding="utf-8"))
        contents[path] = text
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            child = ROOT / target
            visit(child if child.suffix else child.with_suffix(".tex"))

    visit(ROOT / "papers" / (name + ".tex"))
    return contents


def audit(only=None):
    graphs = {tag: source_graph(name) for tag, name in PAPERS.items()}
    owners, labels, label_owner = defaultdict(set), {}, {}
    for tag, graph in graphs.items():
        for path in graph:
            owners[path].add(tag)
        text = "\n".join(graph.values())
        labels[tag] = Counter(re.findall(r"\\label\{([^}]+)\}", text))
        assert all(v == 1 for v in labels[tag].values()), f"{tag}: duplicate label"
        for key in labels[tag]:
            assert key not in label_owner, f"label has multiple owners: {key}"
            label_owner[key] = tag

    for path, tags in owners.items():
        assert len(tags) == 1 or path in SHARED, f"duplicated body source: {path}"
        if path in SHARED:
            assert not re.search(r"\\begin\{proof\}", path.read_text()), \
                f"proof in shared source: {path}"
        else:
            tag = next(iter(tags))
            main = ROOT / "papers" / (PAPERS[tag] + ".tex")
            expected = os.path.relpath(main, path.parent)
            magic = re.search(r"^% !TEX root = (.+)$", path.read_text(), re.M)
            assert magic and magic[1] == expected, f"wrong editor root: {path}"

    for tag, name in PAPERS.items():
        text = "\n".join(graphs[tag].values())
        refs = {k for k in re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text)
                if "#" not in k}
        assert refs <= labels[tag].keys(), \
            f"{name}: use explicit paperref for external/missing labels: {sorted(refs-labels[tag].keys())}"
        external = re.findall(r"\\paper(?:ref|eqref|pageref)\{([^}]+)\}\{([^}]+)\}", text)
        for target, key in external:
            if "#" in target + key:
                continue
            assert target in PAPERS and target != tag, f"{name}: invalid paper tag: {target}"
            assert label_owner.get(key) == target, f"{name}: wrong external target: {target}/{key}"
        items = Counter(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
        assert all(v == 1 for v in items.values()), f"{name}: duplicate bibliography key"
        citations = set()
        for value in re.findall(r"\\cite\w*(?:\[[^]]*\]){0,2}\{([^}]+)\}", text):
            citations.update(k.strip() for k in value.split(","))
        assert citations <= items.keys(), f"{name}: missing citations: {sorted(citations-items.keys())}"
        main_text = (ROOT / "papers" / (name + ".tex")).read_text()
        assert "\\author{}" in main_text, f"{name}: keep author blank"
        assert f"\\SetPaper{{{tag}}}" in main_text, f"{name}: wrong reference configuration"
        if only is None or name in only:
            print(f"OK {name}: {len(graphs[tag])} TeX sources; {len(labels[tag])} labels; "
                  f"{len(refs)} local referenced labels; {len(external)} external references; "
                  f"{len(citations)} cited keys.")
    present = set((ROOT / "papers").rglob("*.tex"))
    assert present == owners.keys(), f"unused TeX sources: {sorted(present-owners.keys())}"
    print(f"OK: {len(present)} TeX files covered; {len(label_owner)} labels with unique paper ownership.")
    print("LIMIT: source integrity only; not a proof audit or typesetting check.")
    return graphs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=PAPERS.values(), action="append")
    args = parser.parse_args()
    audit(args.only)


if __name__ == "__main__":
    main()
