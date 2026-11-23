# 計算の再現

2026-11-24 / v93。実行はリポジトリのルートから。有限代数の計算は原稿の圏論的証明全体を自動的に検証するものではない。検算の仮定・結果・実行済み範囲は [検証範囲](../notes/validation.md)、主張の正本は [論文一覧](../README.md)。

## 環境と優先する検算

Python 3、requirements.txt（NumPy、SymPy）、必要に応じ C++17 コンパイラ。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_quantum_fermat_obstruction.py
python3 computations/verify_narrow_fivefold_counterexample.py
python3 computations/verify_narrow_quantum_threefolds.py
python3 computations/verify_cyclic_fermat_sector_comparison.py
python3 computations/verify_diagonal_quantum_support.py
python3 computations/verify_diagonal_sign_sectors.py
python3 computations/verify_diagonal_clifford_dual.py
```

## 証明書・追加モード

```sh
mkdir -p build
python3 computations/verify_clifford_mixed_shamash_third_middle.py --certificate build/clifford_third_middle.json
python3 computations/verify_mixed_two_dimensional_ext.py --zero-example
python3 computations/verify_mixed_two_dimensional_ext.py --universal
python3 computations/verify_interfactor_pbw.py --clifford
python3 computations/verify_jacobi_rank.py --verify computations/jacobi_rank_certificate.json
python3 computations/verify_jacobi_vertex.py --verify computations/jacobi_vertex_certificate.json
python3 computations/verify_jacobi_rank.py --generate build/jacobi_rank_certificate.json
python3 computations/verify_jacobi_rank.py --verify build/jacobi_rank_certificate.json
```

二次行列の生成と保存済み小行列の検証は別のコード経路を使い、法32003で非零の整数行列式を用いる。八次元頂点の次数三縮約写像の検証は法2での整数行列の階数下界を標数零へ移すもので、標数二の三次多項式の幾何を主張しない。過去の記録では約450 MBの出力・約220 MBのメモリを要した（環境依存）。生成物は `build/` に置き追跡しない。その他の追加モード（`--export` 等）は各スクリプトの引数を確認する。

通常の混合第五の検算は保存した [harmonic_linear_products.json](data/harmonic_linear_products.json) の必要な73項を使う。原データからの抽出・規約の再検証は同 JSON の出典・SHA-256 を参照し、`star5.txt`、`kontsevich_2_k.txt`、`weights_kontsevich_2_k.txt`（k=1,…,5）を用意して、`python3 computations/verify_mixed_fifth.py --source-directory build/harmonic-source` を実行する。全73項について star5 の係数/2^k=raw weight/|Aut| を照合する。外部の全データを Git に追加しない。

補助ノートの組版：`latexmk -lualatex -outdir=build/notes notes/relative_construction_obstacles.tex`、`latexmk -lualatex -outdir=build/notes notes/central_cubic_generic_smoothness.tex`。三稿の相互参照込み組版は `python3 scripts/build_papers.py`。量子化の再現は [別 repo の再現入口](https://github.com/uedakazushi/cubic-quantization/blob/main/computations/quantization/README.md) を参照する。

## 計算資産索引

以下は現行ソース一覧であり、一括再実行済みのリストではない。通常は `python3 computations/ファイル名.py`、追加モードは各コード・検証範囲を参照する。

### 反例・対角量子三様体

- [verify_cyclic_fermat_sector_comparison.py](verify_cyclic_fermat_sector_comparison.py)
- [verify_diagonal_clifford_dual.py](verify_diagonal_clifford_dual.py)
- [verify_diagonal_quantum_support.py](verify_diagonal_quantum_support.py)
- [verify_diagonal_sign_sectors.py](verify_diagonal_sign_sectors.py)
- [verify_narrow_fivefold_counterexample.py](verify_narrow_fivefold_counterexample.py)
- [verify_narrow_quantum_threefolds.py](verify_narrow_quantum_threefolds.py)
- [verify_quantum_fermat_obstruction.py](verify_quantum_fermat_obstruction.py)

### Clifford・Shamash・混合変形

- [verify_bidirectional_clifford.py](verify_bidirectional_clifford.py)
- [verify_clifford_central_norm_jets.py](verify_clifford_central_norm_jets.py)
- [verify_clifford_cover_trace_casimir.py](verify_clifford_cover_trace_casimir.py)
- [verify_clifford_curved_pbw_mc.py](verify_clifford_curved_pbw_mc.py)
- [verify_clifford_double_cover_mf.py](verify_clifford_double_cover_mf.py)
- [verify_clifford_explicit_shamash.py](verify_clifford_explicit_shamash.py)
- [verify_clifford_family_s3.py](verify_clifford_family_s3.py)
- [verify_clifford_fullnorm.py](verify_clifford_fullnorm.py)
- [verify_clifford_general_oneway.py](verify_clifford_general_oneway.py)
- [verify_clifford_hesse_theta.py](verify_clifford_hesse_theta.py)
- [verify_clifford_hesse_two_isogeny.py](verify_clifford_hesse_two_isogeny.py)
- [verify_clifford_isogeny_cubics.py](verify_clifford_isogeny_cubics.py)
- [verify_clifford_jet_transfer.py](verify_clifford_jet_transfer.py)
- [verify_clifford_jets.py](verify_clifford_jets.py)
- [verify_clifford_mixed_koszul_endpoints.py](verify_clifford_mixed_koszul_endpoints.py)
- [verify_clifford_mixed_koszul_frobenius.py](verify_clifford_mixed_koszul_frobenius.py)
- [verify_clifford_mixed_koszul_full_d3.py](verify_clifford_mixed_koszul_full_d3.py)
- [verify_clifford_mixed_shamash_first_middle.py](verify_clifford_mixed_shamash_first_middle.py)
- [verify_clifford_mixed_shamash_second_middle.py](verify_clifford_mixed_shamash_second_middle.py)
- [verify_clifford_mixed_shamash_third_middle.py](verify_clifford_mixed_shamash_third_middle.py)
- [verify_clifford_morse_scale.py](verify_clifford_morse_scale.py)
- [verify_clifford_picard_affine_bridge.py](verify_clifford_picard_affine_bridge.py)
- [verify_clifford_picard_linear_mf.py](verify_clifford_picard_linear_mf.py)
- [verify_clifford_rank_one.py](verify_clifford_rank_one.py)
- [verify_clifford_symmetric_discriminants.py](verify_clifford_symmetric_discriminants.py)
- [verify_hesse_probe_readout.py](verify_hesse_probe_readout.py)
- [verify_hesse_slice_transfer.py](verify_hesse_slice_transfer.py)
- [verify_interfactor_pbw.py](verify_interfactor_pbw.py)
- [verify_interfactor_residual_ks.py](verify_interfactor_residual_ks.py)
- [verify_multiblock_hesse_phase.py](verify_multiblock_hesse_phase.py)
- [verify_shamash_dimension_table.py](verify_shamash_dimension_table.py)

### Sklyanin・中心・PBW・比較

- [verify_center_hessian.py](verify_center_hessian.py)
- [verify_elliptic_center_obstruction.py](verify_elliptic_center_obstruction.py)
- [verify_generic_cubic_descent.py](verify_generic_cubic_descent.py)
- [verify_mixed_center_geometry.py](verify_mixed_center_geometry.py)
- [verify_mixed_central_direction.py](verify_mixed_central_direction.py)
- [verify_mixed_character_ext.py](verify_mixed_character_ext.py)
- [verify_mixed_commutative_candidate.py](verify_mixed_commutative_candidate.py)
- [verify_mixed_comparison_invariants.py](verify_mixed_comparison_invariants.py)
- [verify_mixed_curved_dual.py](verify_mixed_curved_dual.py)
- [verify_mixed_equivariant_coefficients.py](verify_mixed_equivariant_coefficients.py)
- [verify_mixed_fifth.py](verify_mixed_fifth.py)
- [verify_mixed_formal_kernel.py](verify_mixed_formal_kernel.py)
- [verify_mixed_invariant_pbw_dual.py](verify_mixed_invariant_pbw_dual.py)
- [verify_mixed_linear_bockstein.py](verify_mixed_linear_bockstein.py)
- [verify_mixed_linear_pbw.py](verify_mixed_linear_pbw.py)
- [verify_mixed_multiblock.py](verify_mixed_multiblock.py)
- [verify_mixed_pi_center.py](verify_mixed_pi_center.py)
- [verify_mixed_two_dimensional.py](verify_mixed_two_dimensional.py)
- [verify_mixed_two_dimensional_ext.py](verify_mixed_two_dimensional_ext.py)
- [verify_mixed_window_involution.py](verify_mixed_window_involution.py)
- [verify_multicentral_pbw.py](verify_multicentral_pbw.py)
- [verify_picard_obstruction.py](verify_picard_obstruction.py)
- [verify_two_center_restrictions.py](verify_two_center_restrictions.py)

### Jacobi・Hessian・回復・その他

- [verify_active_invariants.py](verify_active_invariants.py)
- [verify_active_sign.py](verify_active_sign.py)
- [verify_boundary_low_products.py](verify_boundary_low_products.py)
- [verify_complete_curved_transport.py](verify_complete_curved_transport.py)
- [verify_cubic_covariants.py](verify_cubic_covariants.py)
- [verify_elliptic_bockstein.py](verify_elliptic_bockstein.py)
- [verify_fivefold_plane_degree.py](verify_fivefold_plane_degree.py)
- [verify_fourth_potential.py](verify_fourth_potential.py)
- [verify_geometric_corrections.py](verify_geometric_corrections.py)
- [verify_jacobi_rank.py](verify_jacobi_rank.py)
- [verify_jacobi_vertex.py](verify_jacobi_vertex.py)
- [verify_multiblock_isogenous.py](verify_multiblock_isogenous.py)
- [verify_multiblock_point_line.py](verify_multiblock_point_line.py)
- [verify_multiblock_twists.py](verify_multiblock_twists.py)
- [verify_multicentral_pencil.py](verify_multicentral_pencil.py)
- [verify_point_poisson_obstruction.py](verify_point_poisson_obstruction.py)
- [verify_poisson_correction.py](verify_poisson_correction.py)
- [verify_rank_one_caustic.py](verify_rank_one_caustic.py)
- [verify_recovery_example.py](verify_recovery_example.py)
- [verify_three_object_window.py](verify_three_object_window.py)
- [verify_two_block_structure.py](verify_two_block_structure.py)
- [verify_veronese_representation.py](verify_veronese_representation.py)

## 証明に必要な入力・補助コード

- [data/harmonic_linear_products.json](data/harmonic_linear_products.json)
- [jacobi_rank_certificate.json](jacobi_rank_certificate.json)
- [jacobi_vertex_certificate.json](jacobi_vertex_certificate.json)
- [verify_binary_minor.cpp](verify_binary_minor.cpp)
