# Research instructions

Read `00_research_plan.md` first, then `notes/research_notes.md` and the current paper. The common principles and standing authorization in the research plan apply to all work in this repository.

- Canonical destination: `uedakazushi/nc-cubic-n-fold`, branch `main`. Save authorized research work without asking again. Use ordinary fast-forward commits; never force-push. Do not create PRs or GitHub Actions workflows.
- Inputs `uedakazushi/nc-cubic` and `uedakazushi/nc-cubic-threefold-moduli` are read-only. Pin input claims to the commits recorded in the plan; do not count results already in those inputs as new.
- Write the publication manuscript in Japanese LuaLaTeX. Keep the author field empty. Main file: `papers/nc-cubic-n-fold.tex`.
- Keep current proofs and useful results in the paper. Keep current ideas, counterexamples, limitations and primary-source locations in the notes. Replace stale text rather than accumulating history, old bundles or duplicate reports.
- Distinguish proof written, proof inspected, independently checked, exact computation, conditional application and unconfirmed novelty. Never infer the full Abel formal moduli or a global residual morphism from reduced Poisson classification or a dimension count.
- Track sources, exact certificates, essential inputs and reproduction instructions. Do not track PDFs, ZIPs, TeX intermediates, caches, build logs or external literature PDFs. Use `build/` for regenerable output.
- GitHub is the canonical save. Use Library only as a fallback if GitHub saving fails, and do not delete existing Library files without explicit instruction.
- Run the source-reference check and the mathematical verification relevant to changed claims; compile when TeX changes. Update `notes/validation.md` to report only checks actually performed.
