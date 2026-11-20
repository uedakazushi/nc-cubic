# Keep existing repository-root-relative input paths for the standalone reconstruction/moduli paper.
@default_files = ('papers/nc-cubic.tex');
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;
