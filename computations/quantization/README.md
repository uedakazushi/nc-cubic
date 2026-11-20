# 三次超曲面の量子化：計算資産

2026-11-21 / v1。主原稿は [cubic-quantization.tex](../../papers/cubic-quantization.tex)、研究ノートは [cubic_quantization.md](../../notes/cubic_quantization.md)、仮定・既存監査は [quantization_audit.md](../../notes/quantization_audit.md)。

Python 3 と SymPy を用い、repoルートから実行する。依存はrepoの `requirements.txt` に含まれる。各コードは有限の恒等式・行列計算を検査し、一般のPBW・平坦性・AS条件・同変降下・圏同値を形式検証するものではない。大きな普遍係数行列は一つずつ実行する。

## 再現する項目

| コード（このディレクトリからの相対名） | 内容・保存入力 |
| --- | --- |
| `verify_nonelliptic_quantization.py` | 節点・尖点のmonic Diamond重なり、中心交換子、potential syzygy、分母範囲、Fermat恒等式。`nonelliptic_quantization_certificate.json` と全結果を照合 |
| `verify_nonelliptic_point_curves.py` | 節点・尖点の同次二次関係行列の行列式と尖点の座標変換。`nonelliptic_point_curves_certificate.json` と照合 |
| `verify_universal_fermat_mixed_center.py` | 全混合係数を保つ普遍Fermat中心元 |
| `verify_universal_hesse_mixed_center.py` | 全混合係数を保つ普遍Hesse中心元、339語・162関係倍数の厳密計算 |
| `verify_cubic_casimir_jet.py` | 20自由係数の三次Casimir二次jet。有限h次数の検算で、全次数中心性の証明は原稿 |
| `verify_cmr_nodal_center.py --json` | CMR既知公式とのパラメータ対応、節点の中心性・純中心補正・スカラー重み |
| `verify_zero_restriction_center.py --json` | 零制限のPBW対称化中心元、重なり、並進共変性 |
| `verify_singular_orbit_centering.py --json` | 節点・尖点の左逆と中心調整、失敗型の線形障害、滑らかな例 |
| `verify_equivariant_centering.py` | 混合係数と二つの座標変換に対する中心調整の厳密検算 |
| `verify_general_dimension_multiblock.py` | 六つの次元・ブロック構成で独立Poisson係数、Jacobi、Casimir、内在的Hessian縮約 |
| `build_general_dimension_center.py` | 共通中心を持つ二ブロックHesse中心式の合成例 |
| `verify_singular_cubic_classical_kernel.py` | 零制限の滑らかな例の古典Casimir核の厳密rank |
| `verify_universal_casimir_minor.py` | Cramer構成に関係する交換子小行列の有限計算 |
| `verify_hesse_translation.py` | Hesse混合項からEG表示への平行移動と交換関係 |
| `verify_hesse_center.py`、`verify_mixed_center.py` | 明示Hesse中心・混合中心の補助検算。有限特殊化の範囲は各コード先頭に記載 |
| `verify_nodal_cubic_centre_specialization.py` | 節点三次への中心元特殊化の厳密計算 |
| `verify_algebra.py` | Sklyanin中心・Hesse判別式、Koszul恒等式、有限体全点列挙。`verification.json` を再生成 |
| `independent/verify_fermat_nc_cubic.py`、`independent/verify_generic17_center.py`、`independent/verify_generic_center_hessian.py` | 独立実装によるFermat・一般係数中心・Hessianの補助検算 |

`fermat_center_certificate.json` はFermat中心交換子の15項の自由語証明書であり、再生成が容易なログとして削除しない。非楕円Poisson成分の整数小行列・滑らかさ・Schouten検算は [poisson-cubic/computations](https://github.com/uedakazushi/poisson-cubic/tree/main/computations) が正本である。

## 実行例と確認範囲

```sh
python3 computations/quantization/verify_nonelliptic_quantization.py
python3 computations/quantization/verify_nonelliptic_point_curves.py
python3 computations/quantization/verify_general_dimension_multiblock.py
python3 computations/quantization/verify_cmr_nodal_center.py --json --output build/verify_cmr_nodal_center.json
python3 scripts/check_sources.py
latexmk papers/cubic-quantization.tex
```

上は再現コマンドであり、一覧全件を今回実行したとの記録ではない。移管に際して全Pythonソースの構文を確認し、移動後の証明書照合・分割した行列式の検算を実行した。具体的な実行結果は [validation_quantization.json](../../validation_quantization.json) に記す。過去の成功、今回の実行、一般証明の内部点検、形式検証、組版を区別する。
