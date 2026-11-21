# Keep repository-root-relative inputs. For convergent cross-paper references,
# use python3 scripts/build_papers.py (also the default VS Code recipe).
@default_files = ('papers/nc-cubic.tex', 'papers/cubic-moduli-descent.tex', 'papers/mixed-sklyanin-cubics.tex');
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;
