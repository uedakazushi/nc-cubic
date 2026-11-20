# Research instructions

2026-11-20 / v11.

Read `00_research_plan.md` first, then `notes/research_notes.md` and the current paper. The common principles and standing authorization in the research plan apply to all work in this repository.

- Canonical destination: `uedakazushi/nc-cubic-n-fold`, branch `main`. Save authorized research work without asking again. Use ordinary fast-forward commits; never force-push. Do not create PRs or GitHub Actions workflows.
- Inputs `uedakazushi/nc-cubic` and `uedakazushi/nc-cubic-threefold-moduli` are read-only. Pin input claims to the commits recorded in the plan; do not count results already in those inputs as new.
- Write the publication manuscript in Japanese LuaLaTeX. Keep the author field empty. Main file: `papers/nc-cubic-n-fold.tex`.
- For new manuscripts or build setups, consult research-hub `papers/paper-template.tex`, `papers/README.md`, `.latexmkrc`, `.vscode/settings.json`, and `.vscode/extensions.json`. Preserve effective existing settings. Keep section root directives, source paths, PDF output and SyncTeX consistent when moving a manuscript; do not replace the main body by an index.
- Keep current proofs and useful results in the paper. Keep current ideas, counterexamples, limitations and primary-source locations in the notes. Replace stale text rather than accumulating history, old bundles or duplicate reports.
- Distinguish proof written, proof inspected, independently checked, exact computation, conditional application and unconfirmed novelty. Never infer the full Abel formal moduli or a global residual morphism from reduced Poisson classification or a dimension count.
- Track sources, exact certificates, essential inputs and reproduction instructions. Do not track PDFs, ZIPs, TeX intermediates, caches, build logs or external literature PDFs. Use `build/` for regenerable output.
- GitHub is the canonical save. Use Library only as a fallback if GitHub saving fails, and do not delete existing Library files without explicit instruction.
- Run the source-reference check and the mathematical verification relevant to changed claims; compile when TeX changes. Update `notes/validation.md` to report only checks actually performed.

## Research priorities

- Pursue results uniform in n. The central goals are O-marked moduli, point schemes, a morphism to moduli of Poisson varieties, and comparison with the Kuznetsov components of the same underlying varieties; equivalence is a research expectation, not an established result on all components.
- Prioritize general or very general objects of each irreducible component. Distinguish dense Zariski opens, geometric generic points, and complements of countably many proper closed subsets. Do not identify a one-block presentation component with all components of the intrinsic moduli.
- Treat the degree-one shift and presentation as auxiliary unless recovered from (C,O). On the one-block dense open, the pinned MF/window/generic-generation/coherent-saturation inputs give the residual cubic, the projective Poisson morphism, and a finite étale comparison to Ku of the same cubic. The point elliptic curve and residual active cubic have equal j; their plane-Isom cover has rank 18, with a rank-9 3-torsion cover of the rank-2 Jacobian-Isom torsor. The scale line is dual to the active Hodge line. The point differential defines a canonical dominant generically finite residual morphism modulo sign and a full lift on that rank-2 cover. Its generic degree and canonical sign on the original stack remain open. Do not transfer the old Hessian correction's degree 9 to this map or identify the transported point translation with Ku rotation.
- Comparison kernels still require first selecting compatible isomorphism classes under the full autoequivalence action, then descending the scalar gerbe. In the specified CF Euler type and on a split chart, the scalar generic index divides 3^floor((n+1)/2); unsplit fields require at most one extra factor 3 when n≡1 mod3. This is conditional on the first-stage class selection. Do not identify the kernel gerbe with the presentation Brauer class. Coherent graded-center linearity and categorical restriction to U=0 are still unproved; tensor restriction alone does not establish them.
- Keep the distinction between the point-normalized algebraic tensor and the fixed-generator harmonic tensor: in the chosen formal frame their ratio is h/c_h, which need not be algebraic. Retain the latter's very general transcendence, the trace–Hessian obstruction, degree-nine correction, exact point curve, mixed fifth/fourth formulas, finite correction, and all Jacobi certificates. Distinguish CF-dependent trait models from canonical extensions and kernels at h=0.
- Study boundaries and dimension-specific examples when they resolve a concrete obstruction to these general goals. Retain all valid existing proofs and exact certificates; do not make successive dimension-specific Hilbert calculations the default next task.

## Maintain research-hub

- The overall entry point is https://github.com/uedakazushi/research-hub. Local details remain in `00_research_plan.md`, `notes/research_notes.md`, `papers/nc-cubic-n-fold.tex`, and `notes/validation.md`.
- At a research checkpoint, first update and save the current materials in this repository, then read the latest research-hub README and applicable instructions and update this project's entry: goals, established scope, remaining obstacle, next action, dependencies, and restart links.
- Preserve other projects and concurrent edits. Use ordinary fast-forward commits to hub main, with no Actions or force push. Do not copy detailed proofs, task logs, or duplicate task lists into the hub.
- Verify this repository's save and the hub update separately. If the hub cannot be updated, save this research and report the unreflected item and reason. Do not infer new mathematical verification from a policy edit or a hub summary.
