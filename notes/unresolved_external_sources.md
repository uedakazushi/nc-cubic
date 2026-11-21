# 外部原資料の未照合箇所

2026-11-22 / v50。ここは公表済み・検証済みの成果の一覧ではなく、独立した相対構成と原資料に残る重要な内容の再取得先である。原資料の書誌・原本識別・未照合箇所を保持し、三稿への編集整理を外部PDFの所在・本文の再照合とは扱わない。

現在の証明の正本は、[可換復元主稿](../papers/nc-cubic.tex)、[モジュライ・降下稿](../papers/cubic-moduli-descent.tex)、[混合Sklyanin稿](../papers/mixed-sklyanin-cubics.tex) である。代数的量子化は別repoの [cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) を正本とする。外部原資料の内容を使う場合は、対応する現行稿の具体的定理・仮定・証明との一致を個別に確認する。

## 原資料と残る照合

| 外部参照先（nc-cubic2） | 原本識別・既存の確認範囲 | 保持すべき内容・未照合点 |
| --- | --- | --- |
| [central_cubic_technical.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_cubic_technical.pdf) | `nc_cubic_p4_paper_ja_20261101_v5.pdf`、61頁。第28節43–44頁の一部をTeX化 | 有限中心式、AS正則性、一般軌道、正則locus。部分ノートは [central_cubic_generic_smoothness.tex](central_cubic_generic_smoothness.tex) |
| [central_pair_formal_moduli.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_pair_formal_moduli.pdf) | `nc_cubic_unified_paper_V_ja_20261101_v16.pdf`、60頁。全証明一致未了 | 41次元incidence、17次元商、全Artin比較、偏極付き復元、低次数中心、局所化 |
| [central_quotient_singularities.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/central_quotient_singularities.pdf) | `nc_cubic_unified_paper_VI_ja_20261101_v1.pdf`、61頁。第15節25–27頁に中心曲面判別式 | 中心判別式H(H+1)(27H+28)、混合因子(α³+9)(28α³+243)、21中心特異点と3 homological singularities、Azumaya locus、Brauer指数6、spherical twist。中心曲面の証明だけでtails判別へ昇格しない |
| [pfaffian_contact.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/pfaffian_contact.pdf) | `nc_cubic_unified_paper_III_ja_20261101_v2.pdf`、89頁。部分重複・全証明一致未了 | 普遍非線形接触分類、Hessian局所不変量、Pfaffian graph解消、高次正規形と計算証明書。独立研究の現行所在はnc-cubic2の研究方針から確認する |
| [sklyanin_mixed_quantization.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf) | `nc_cubic_unified_paper_II_ja_20261101_v16.pdf`、195頁。全体TeX未確認 | 全21混合方向、標識付き全Artin比較、点加群スキーム、臨界層・局所特異点・例外値・同型判定 |

ページ数と同サイズ原本との対応は移管前に目次を調べた記録であり、全内容の一致や現在の保存状態を保証するものではない。

## 具体的な再開先と適用境界

- [relative_construction_obstacles.tex](relative_construction_obstacles.tex) は相対Beilinson模型、PI中心幾何、生成性、有限パラメータの障害を保持する。現在の一般点復元定理と条件付きの個別構成を分けて読む。
- [中心曲面判別式TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/central_fiber_discriminant.tex) と [検算](https://github.com/uedakazushi/nc-cubic2/blob/main/computations/verify_central_fiber_discriminant.py) が中心判別式・Hessian・H=9のGroebner計算の再開候補である。Azumaya性・local order・Brauer指数6・非可換tailsへの昇格は別に照合する。
- [有限正則性ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/ambient_finite_smoothness_and_recovery.tex) と [dg perfectness反例](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_reconstruction/dg_perfectness_counterexamples.tex) は、特殊・Artin perfect性から相対perfectnessが従わないこと、非開性、Hom有限性の参照先である。
- [有限barノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/sm_bar_and_spreading.tex) は有限bar-skeleton、Artin底の検出、generic spreadingを扱う。これだけで相対smoothness全体が証明されたとはしない。
- 一次Poisson変形のJacobian接空間への写像と五変数のPlücker障害については、nc-cubic2の `papers/relative_reconstruction/first_order_poisson_kernel.tex` が元資料に指定された参照先である。JLLZのη同型、三様体の接空間20→10と核10、17次元族の7方向の対応を区別し、最後の対応を確認済みと扱わない。

独自の定理・必要な証明・反例・厳密入力を現行TeXへ統合し、原本と照合する前に原資料を削除しない。見出しや主題の一致は証明単位の照合ではない。`sources/candidates/` 等として識別されていた包括稿も未照合の原資料であり、現在の三稿や量子化論文の証明入力にはしていない。
