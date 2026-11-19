# 非可換三次 n-fold：現行稿の検証範囲

2026年11月20日 / v6。対象は `papers/nc-cubic-n-fold.tex` と現行の証明書・再現コード。証明の記載、読解点検、計算の実行、組版、外部への保存を別々の確認として扱う。

本版では、任意基底上の強い affine lift、Poisson 対からの逆構成と開部分の同型、全次元の非自明な幾何補正、固定入力の残余復元との Hesse 比較障害、一般混合係数上の二次 jet 障害を統合した。執筆担当以外の読解点検と統合時の点検を行い、新しい有限式を有理係数で厳密に検算した。既存の Jacobi 証明書・検証器と中心評価コードは Git blob SHA と SHA-256 で内容不変を確認し、既存の大行列計算は再実行していない。未公表の MF 移送・中心性・一般点復元の全証明の再検証、外部査読、形式証明とは区別する。

## 1. 固定した入力と文献

- `uedakazushi/nc-cubic`：`eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59。
- `uedakazushi/nc-cubic-threefold-moduli`：`6c35d2c84671c2538e61836a6bf3a511392eacce`。比較対象の三様体稿 v22。

入力リポジトリは読取り専用。既存の一般次元正規形・中心量子化・一般点残余復元は新規成果に数えず、未公表入力の全証明を独立に再検証したとは主張しない。引用箇所は `research_notes.md` と `papers/references.tex` に記す。

一次資料で、Gesmundo–Landsberg の Proposition 6.1・式 (6.2)、Landsberg–Ottaviani の §1.2・§4.1、Boij の Remark 6（pp.163–164）、Boij–De Negri–De Stefani–Rossi の Introduction、Bricalli–Favale–Pirola の Proposition 2.1・Theorem 3.4 を確認した。Jacobi 写像と Koszul flattening・apolar Betti 数の同定も証明し、普遍階数上界と N=9,10 の二次階数の達成を既知の帰結として位置付けた。現行の次数三の決定や平方零拡大の非分裂性を、既存の Betti 数の表だけから導いたとは主張しない。全次元の一般 apolar 代数について β₄,₆=0 を示す文献は確保していない。

相対双対の入力は Berger–Taillefer の Theorems 3.1, 3.6、dg Morita 表示は Keller の Theorems 3.4, 3.8。係数降下・Kummer・曲線上の主因子は Stacks Project の Tags 023N, 03PK, 040Q, 02RU を確認し、現行の圏内の係数作用・全同値の降下には本文で証明を与えた。新規性の網羅的調査は未完了である。

既存の点検では、Behrend–Noohi の刊行版§2.3・§3.1.2を確認し、grading rigidification、twisted algebra、determinant character を既知手法として明示した。EGの刊行版§9・p.1414のRains中心公式は本文とPDF画像で確認し、Proposition 8.1.1・式(8.1.3)の形式的中心比較と今回の有限係数での処方を区別した。LBSVの刊行版Proposition 4.2.5・pp.193–194の二次関係復元も照合した。Stacks Tags058G,0781,03R6,063P,063U,062Y,056Qは新しい降下・相対幾何の使用箇所と照合した。固定入力の `prop:pg-ad-intrinsic-hessian` と `cor:pg-hesse-hessian-form` は、純中心補正の前後を区別して式を確認した。その未公表入力の非可換中心性の証明全体を今回再検証したとは主張しない。

今回の比較で Dito の arXiv:math/9905080v1、§2 式(3)と§3 Theorem2 を確認した。対象は一般 Poisson の二次積と Weyl gauge であり、Lie 代数に限定された後続公式と区別する。Shoikhet の arXiv:math/0007080v1、§1.3 の内向き wheel 消滅と§2.3.1 の逆向き wheel の区別を確認した。出版社で両文献の巻・年・頁・DOIも照合した。非線形 Poisson について中心写像の全高次消滅を主張せず、二次に寄与するグラフの数え上げを本文に与えた。

Artebani–Dolgachev の公刊版§2、Lemma2.1 と式(4)–(5)・p.240を本文とPDF画像で確認し、Hesse j式の規約を照合した。Lin–Zhang の Theorems4.1,5.1 と rotation の回復を比較し、幾何的非同型から圏の結論へ移す際の追加条件を保持した。固定入力Bの `curved_transport.tex`, `gradient_recovery.tex`, `explicit_example.tex` を固定commitから読み、完備移送、中心逆像、低 rotation 積、明示Hesse係数の該当箇所を確認した。この確認を入力Bの全証明の独立検証とは扱わない。

## 2. 証明の記載と読解点検

現行の中心復元、次数付きモジュライ、相対双対、点関手、Jacobi 方程式、残余圏の形式認識の証明を保持した。固定模型の降下、Picard 障害と明示例、Koszul/apolar 同定、八次元の全 Hilbert 関数、横断切片・retract には、執筆担当以外の担当による読解点検と統合時の点検を行った。これは外部査読や形式検証ではない。

| 対象 | 点検した論点 | 適用条件・残る限界 |
|---|---|---|
| 中心復元・次数付きモジュライ | fpqc 持上げ、μ_d、中心正則対、全次数の切断飽和性、全次数付き同型、有限安定化子、スカラー重みの相殺 | 中心平坦性・普遍低次数中心・良い PBW 表示の仮定を要する |
| 普遍相対双対 | 有限 Koszul 対角、真正な双加群自己双対、中心差分、torsion 比較、compact generator、dg orbit、相対 properness、Serre pairing・trace | 被約有限型の初期基底、有限射影・分裂 PBW・各ファイバーの Koszul/CY・中心三次の分裂正則性。その後の任意底変更には非平坦・非被約を含む。全商上の orientation の自明化は未主張 |
| 固定模型間の全同値 | 係数対象の Gabriel 局所化、faithfully flat な tails の降下、全関手と自然変換の降下、自然自己準同型のスカラー性、Isom_gr/G_m と全 O-保存同値の一致 | 比較定理に列挙した中心・次数別有限射影性・相対 Serre の仮定。一般の Abel 圏族が局所的にこの模型へ入ることや全モジュライの代数性は未証明 |
| 線束障害と三捩れ例 | μ_d と G_m の持上げ torsor の区別、L^d、行列式からの gcd(d,3)、affine 楕円曲線の非主三捩れイデアル、次数別線束 twist と PBW 入力の保持 | 三捩れへの制限は両方の次数一加群が自由な場合。明示例は指定した同値に大域の次数付き代表がないことを示し、二つの代数にどのような次数付き同型もないとは主張しない |
| 局所 O-marked 圏族の効果化 | 一般Grothendieck圏の忠実平坦係数延長、重み付き加群のgenerator・torsion商、任意係数変更、全同値のcocycleから対象を構成 | good模型の全Hom比較が入力。全intrinsic成分の局所表示や変形の閉性は未証明 |
| 表示 gerbe の H² 障害 | determinantの重み、e=1での中心拡大の分裂、cyclic division algebraのvaluation、全非空開のtwistと有理点 | n≡1 mod3で全非空開上の位数3を証明。幾何学的一般点の体に非零Brauer類が残るという主張ではない |
| 相対点関手 | 任意底変更でのKoszul完全性、八次有限局所自由性、相対Cartier、低次数イデアル、点商とshiftの降下、determinant付き相対随伴 | good点スキーム条件。ambient上のO(1)と点空間への引戻しを区別 |
| 中心三次の復元 | Rains式の境界Jacobi評価、中心評価の普遍単射、I(D)₃/I(C)₃と中心直線の逆像 | 非空開上。n=3で全切断への全射を使わない |
| Trace–Hessian 射 | 任意基底の三次Casimir、正規化trace、Hessian縮約の共変性、torsor同型と滑らかな非空開への降下 | 良い局所一ブロック型。Kuとの一致は別であり、本版では具体的な不一致を証明 |
| 強い affine lift と逆構成 | Euler列のコホモロジー、gradient Koszul、強いliftの一意性、divergenceによるJacobi同値、supportと全同型の回復 | 任意のC代数・滑らかな相対三次・n≥3。標的は偏極類とBrauer–Severi ambientを許す |
| Poisson 開の同型と支配成分 | Msm≅Pgood⊂Pdec、周囲B単独の有限性の除去、pairのDM性、Brauer位数、一般三次上の開埋込み | PBW・中心・相対Serre・全同値の入力を保持。唯一の支配成分には既存被約分類を使用。全 intrinsic 圏成分の分類ではない |
| 幾何補正 | F_tの滑らかさ因子、全nに一様なJacobi双対証明書、trace補正u³の非消滅、係数空間の非空開 | 入力の中心性を使用。入力定数族との差と残余復元との差を区別 |
| split Hesse 比較 | exact λ_THとλ_res、j差、symmetrizerの可換代数性と唯一rank3 primitive、固定Πの全smooth cubic Casimirへの障害 | 残余の同定は固定入力Bを使用。rotation保存dg Morita同値なし。n≢1 mod3でのみrotationなしの結論 |
| 一般混合係数の二次 jet | Dito二次式、Θ=−2adj、ρ₂F=Hess/8、inner二輪消滅、h⁴境界のJacobi消滅、Jacobi束切断Δ₂の非消滅開 | 指定formality模型・MF/window入力の下で複素点のmarked形式比較を妨げる。全次数relative formality・一般混合係数のunmarked一般点非同値は未主張 |
| Jacobi の二次式と既知結果 | 全係数環の式、Plücker 空間、普遍核、ρK/2 の係数と符号、Koszul strand の双対、N=5 の終端、total Betti 数から必要な graded Betti 数への帰着 | N≥11 の一般階数の最大性は未決定。一般 Koszul 性から β₄,₆=0 を推論しない |
| 八次元の頂点 | I₃=J₃ から全次数の一致、J/I=C(−2)^330、socle・飽和・根基、非分裂性、任意底変更の相対版、一次分解 | この結果は一般点被約分類に依存しない。長さ330は J/I の長さであり、明示した m-primary 成分の商 R/Q の長さ5401とは異なる |
| 非零点の局所構造 | 法接空間 Λ³K、横断方程式から混合項の消去、全 W 方向の polar 条件、Thom–Sebastiani 特徴付けと scheme retract、n≥11 の特殊非零点への330次元部分空間の注入 | 横断切片を Grassmann 方向との局所積とは主張しない。特殊例の周囲の冪零根基全体が二乗零とは主張しない。n=11 は構成が与える下限であり最小性は未証明 |
| 一般次元の頂点と高次数 | 悪い incidence の次元評価、有限長性・飽和・随伴素点・深さ、各固定次数の漸近非消滅 | 一般次元の有限長性には既存の被約分類を入力する。n=9,10 の全 Hilbert 関数と、一般次元の冪零根基自身の積は未決定 |
| 残余圏 | HH sector の次数、幾何的 KS、滑らかな変形源と形式認識、tame hull、n=4 の例外、rotation | 通常 Artin 基底・特殊ファイバー固定・一次切断。全高次群oidや導来基底、全 Abel 形式変形との同定、大域残余射は未主張 |

主張に列挙した仮定の下で、上記の点検により未解決の論理的欠落は報告されていない。原稿・要約・研究方針・研究ノートの仮定と結果の状態を整合させた。ただし外部査読や Lean 等による形式検証は行っていない。

## 3. 二次階数の整数証明書

保存済みの全6例について、指定した平方小行列の行列式を探索とは別経路で直接計算する検証が完了している。本版でも、この証明書と検証コードの SHA-256 が変更されていないことを確認した。全6例の再実行は本版の追加検証には含めない。

| N=n+2 | 小行列の次数 | 行列式 mod 32003 |
|---|---:|---:|
| 5 | 5 | 15512 |
| 6 | 35 | 14374 |
| 7 | 140 | 7973 |
| 8 | 420 | 508 |
| 9 | 1050 | 13073 |
| 10 | 1980 | 16095 |

全て非零。本文の上界と合わせ、5≤N≤10 の一般二次階数を決定する。N≤9 では I=J、N=10 では dim(J/I)₂=330 を得る。滑らかさは階数開集合と滑らかな三次の非空開集合の交わりによる。

```text
computations/verify_jacobi_rank.py
e5c1d00466265b44d6c2ea23c158a22133526231d9c2114db8ac8782d58d8ee3
computations/jacobi_rank_certificate.json
43482f8a6decff0cddc1d077abc12aeac584e5eb3b2898ad717c59793475588f
```

## 4. 八次元の次数三の厳密検証

保存した220個の対称整数テンソル成分を用い、整数 Jacobi 二次式の係数を法2へ還元した。三次多項式 T(z,z,z)/6 を標数二で解釈する計算ではない。Python 3.12.14・NumPy 2.3.5 と C++17 により、近似演算を使わず以下を再生成・検証した。

| 検証対象 | 確認値 |
|---|---:|
| Plücker 二次空間の次元 | 2310 |
| Jacobi 二次空間の階数 | 1980 |
| 二次商 D の次元 | 330 |
| 一次倍 p_s g_a の総数 | 277200 |
| 多重次数ブロック数 / 最大行数 | 23050 / 420 |
| 三次 Plücker 空間の階数 | 186340 |
| 一次 syzygy 空間の次元 | 90860 |
| E⊗D の次元 | 39600 |
| 保存した正方小行列の次数 / 行列式 mod2 | 39600 / 1 |

全 Jacobi 多項式が構成した Plücker 基底の線形結合と一致することを、非標準項だけでなく全係数について検証した。多重次数の同次性、核ベクトル数、行列の SHA-256、証明書の行番号の相異性も確認した。各ブロックで従属した入力は、source の新しい座標を持つ核ベクトルを与え、合計90860本が核の基底となる。

探索には低位 pivot のブロック消去を用いた。保存した39600行の平方小行列は、別の高位 pivot の通常 Gaussian 消去で直接検証し、全階数39600・行列式1を確認した。現在の保存対象コードによる再生成からこの検証までの実行は完了している。本版ではこの大行列計算を再実行していない。検証器と数学的な縮約の論理は、実装担当以外も読解点検した。

完全列 K→E⊗D→(J/I)₃→0 により、法2で元の Jacobi 二次式の一次倍が J₃ 全体を生成する。標数零へ移すのは、**元の整数 Jacobi 三次係数行列**の階数下界186340である。有限体で構成した個々の syzygy の持上げを仮定しない。標数零での I⊂J と次元上界を合わせて I₃=J₃ を得る。

```text
computations/verify_jacobi_vertex.py
cc899ad2dd1ca29b2a816f04a9f26664ba3d474c92a7b1c112bf7ab3ac86c7a9
computations/verify_binary_minor.cpp
7a52f8d19ce95db0548d8ae95cb77f9c6ee3bdace55d51ca6765df77c03c5f19
computations/jacobi_vertex_certificate.json
cdfa77d08a4375ce5b6d9abce70b8dc90de8cce31f561c5db7a29e0b2283dc76

再生成した 90860×39600 行列（449757008 bytes、非追跡）
314f31ba61792baff9c4adff367ed15c5a83ab004fdbcd52900dbc25e9b583d9
```

N≥11 の二次最大階数と、n=9,10 の全 Hilbert 関数を確定する計算は未実行。全 n≥11 の特殊非零点の330次元部分空間は、八次元の検証済み結果と本文の retract の証明から導き、各次元での個別実験に基づく主張ではない。

## 5. 中心評価・Hessian・trace の厳密記号検算

`computations/verify_center_hessian.py` は SymPy 1.14.0 で全assertionと二つのPASSが確認済みの現行コードである。本版では内容不変を照合し、この既存計算の再実行はしていない。SHA-256は `20bb71ce1b8c56f0e81a3776dce38c1f1f786ec54a44c409a0ecf2c71d4721bc`。浮動小数点、係数の補間、ランダムな有限標本は使わない。

- 公刊Rains式の可換化と、κ=−4h⁴(1+λ³)/(1−hλ/2)⁶ の差が三偏微分のイデアルに入ることを、明示的な係数恒等式で確認した。統合担当は別の短い式の簡約でも係数を確認した。
- HessianのJacobi類が8(1+λ³)xyzとなる恒等式と、固定入力のHesse中心のW−λUを確認した。
- 六つの混合係数を独立記号とするFermat型の八次自由代数を、平方自由単項式の基底で扱い、正規化traceと有限hの純中心補正を計算した。これは任意個の中心変数への特殊化を許す係数恒等式である。
- 最後の比較に用いるΩの非可換中心性は、固定入力の `cor:pg-hesse-hessian-form` を使用する。このスクリプト自体がその中心性やPBW性を再証明するわけではない。

### 幾何補正と残余比較の新しい厳密検算

`python computations/verify_geometric_corrections.py` を実行し、全assertionと13個のPASSを確認した。確認対象は次の通り。

- 四変数の二十個の三次単項式上で全十六個の gradient 一次倍を消す多項式汎関数、u³での値3t、t=1での階数16→17。
- 滑らかさの二因子 `(1+12t³)(1+2t³+5t⁶)` と、八次自由臨界代数のtraceによる `F_t+h²t³u³`。
- 一般Hesse中心元のh⁴境界項がg_λの倍数であり、境界Jacobi環で零となる恒等式。
- 独立六記号の対称3×3行列について、Θ=−2adjの全九成分とρ₂F=det(Hess)/8、線型形式の星積冪の帰納係数。
- Fermatの二次差 `xyz/3` のJacobi非消滅。追加の中心変数への一様性は本文のテンソル積による証明であり、有限個の次元の標本確認によるものではない。
- split Hesse の `b_h−h a_h=−2h²(1+h³)/3`、λ_res−hの有理式、j差の初項13824h⁴とh⁶までの係数。
- active symmetrizerの九元一次方程式で、明示八次小行列式 `λ²(λ³−8)²` と核がscalarであること。

traceについては、別担当がGroebner基底と八次乗法行列を別実装し、本文の値を独立に再確認した。上のスクリプトは非可換中心性、formalityの存在、MF同値、Torelliを機械的に証明するものではない。

## 6. ソース・組版の確認

`python scripts/check_sources.py` は13個のTeXソース、178個の相異なるラベル、105個の参照ラベル、42個の引用キーについて成功した。方針・README・研究ノート・本書から参照する本文ラベルも照合した。本文の著者欄とPDFのauthorメタデータは空である。分割原稿のroot指定、LuaLaTeXとlatexmk、PDF・SyncTeXの `build/` 出力を確認した。research-hubの現行テンプレートと設定を参照し、既存の有効な組版設定を保持してLaTeX Workshopの推奨拡張を追加した。VS Code UIによる実行はしていない。

最終ソースからLuaLaTeX 1.24.0・latexmkで組版を完了した。生成PDFは95ページ、1050286 bytes、SHA-256は次の通り。

```text
7b06c1eb55aa1828fe6fb5ea93f7be843d97067b07208c45bf7eebdc4e397c6f
```

全95ページを画像化して一覧を目視し、新しい定理・証明・冒頭のページを拡大確認した。目次を第2ページにまとめた最終版についても全ページの一覧と主要箇所を再点検した。ページ端への文字の突出、重なり、欠けは見つからず、機械的な文字領域の端点検査も全ページで通過した。最終ログに未定義参照・未定義引用・missing character・overfull・underfullはない。

環境由来の `lltjp-array` の `@tabular 2` patch診断と、4.5ptの数式フォントを5ptへ置換する警告は残る。表と数式の表示は画像で確認し、組版エラーや本文の欠落は認めなかった。警告が一切ない組版、または異なる環境で同じPDFハッシュが得られることは主張しない。

## 7. 再現と保存の区別

再現手順はルートの `README.md`。原稿は `latexmk papers/nc-cubic-n-fold.tex` で `build/` に出力する。主要依存は LuaLaTeX・LuaTeX-ja・和文フォント・標準 TeX パッケージ、Python 3・NumPy・SymPy、C++17 コンパイラ。次数三の検証は約450 MBの行列を再生成し、直接消去には約220 MBのメモリを用いる。大行列は保存せず、220個の入力・行番号の圧縮表・検証コードから再生成する。

保存対象は現在の原稿、研究方針、研究ノート、本検証範囲、書誌、再現コード、証明書、必要な設定だけ。入力稿の全コピー、旧稿、旧bundle、担当者別レポート、外部文献PDF、ビルド中間生成物を含めない。PDFは再生成物として提供し、Gitの追跡対象に含めない。

外部への保存は生成・検証とは別に、GitHub の tree にある全ファイルの blob SHA を手元のソースと照合し、通常の fast-forward による main の更新後に、先端 commit と tree を読み直して確認する。保存された版の識別子は Git の履歴と配布時の報告に記す。この文書だけをもって、未実行の外部保存が完了したとは扱わない。
