# 非可換三次 n-fold：現行稿の検証範囲

2026年11月20日 / v12。対象は `papers/nc-cubic-n-fold.tex` と現行の証明書・再現コード。証明の記載、読解点検、計算の実行、組版、外部への保存を別々の確認として扱う。

本版では、反対代数による残余射の不変性と自由な二重商、active 不変量の九次中間被覆、全 n≥3 に対する一般次数 δ_n=18e_n（e_n≥1）を統合した。固定 support の係数 atlas、Fisher の軌道分類、幾何学的一般ファイバーの整性、関数体の線型無関連性、微分の正規化を点検した。証明は執筆・統合時の読解点検に加え、執筆担当以外による独立の読解点検を受けた。e_n=1や標準符号被覆の分裂は証明していない。

選んだ相対 bar flow と逆の中心係数商への降下を証明し、完備 active MF 比較を統合した。係数商と圏の導来 tensor を区別し、absolute perfect と relative perfect の差を示す反例も研究ノートへ整理した。比較核の rotation Euler 格子と、既に選んだ同型類の scalar index の三に素な体拡大に対する不変性を別途証明・点検した。有限代数的核への coherent な中心作用の降下は未完成であり、次元非依存の index≤3 は追加データを要する条件付き判定としてのみノートに記す。

新しい計算は `computations/verify_active_invariants.py` の有理係数多項式恒等式であり、Hesse の不変量、rψ=ar、判別式・Jacobian の公式と符号不変性を実行確認した。全次数・全次元の結論は本文の一般証明による。既存の12計算資産を保存済み v11 の Git blob SHA と照合し、変更していないことを確認した。既存の graph・四次 potential・大行列 Jacobi 計算は本版で再実行せず、内容不変の照合と再実行を区別する。未公表の完備 MF・一般点復元・coherent 飽和性の全証明の独立検証、外部査読、Lean 等による形式証明は行っていない。

## 1. 固定した入力と文献

- `uedakazushi/nc-cubic`：`eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59。
- `uedakazushi/nc-cubic-threefold-moduli`：`6c35d2c84671c2538e61836a6bf3a511392eacce`。比較対象の三様体稿 v22。

入力リポジトリは読取り専用。既存の一般次元正規形・中心量子化・一般点残余復元は新規成果に数えず、未公表入力の全証明を独立に再検証したとは主張しない。引用箇所は `research_notes.md` と `papers/references.tex` に記す。

一次資料で、Gesmundo–Landsberg の Proposition 6.1・式 (6.2)、Landsberg–Ottaviani の §1.2・§4.1、Boij の Remark 6（pp.163–164）、Boij–De Negri–De Stefani–Rossi の Introduction、Bricalli–Favale–Pirola の Proposition 2.1・Theorem 3.4 を確認した。Jacobi 写像と Koszul flattening・apolar Betti 数の同定も証明し、普遍階数上界と N=9,10 の二次階数の達成を既知の帰結として位置付けた。現行の次数三の決定や平方零拡大の非分裂性を、既存の Betti 数の表だけから導いたとは主張しない。全次元の一般 apolar 代数について β₄,₆=0 を示す文献は確保していない。

相対双対の入力は Berger–Taillefer の Theorems 3.1, 3.6、dg Morita 表示は Keller の Theorems 3.4, 3.8。係数降下・Kummer・曲線上の主因子は Stacks Project の Tags 023N, 03PK, 040Q, 02RU を確認し、現行の圏内の係数作用・全同値の降下には本文で証明を与えた。新規性の網羅的調査は未完了である。

既存の点検では、Behrend–Noohi の刊行版§2.3・§3.1.2を確認し、grading rigidification、twisted algebra、determinant character を既知手法として明示した。EGの刊行版§9・p.1414のRains中心公式は本文とPDF画像で確認し、Proposition 8.1.1・式(8.1.3)の形式的中心比較と今回の有限係数での処方を区別した。LBSVの刊行版Proposition 4.2.5・pp.193–194の二次関係復元も照合した。Stacks Tags058G,0781,03R6,063P,063U,062Y,056Qは新しい降下・相対幾何の使用箇所と照合した。固定入力の `prop:pg-ad-intrinsic-hessian` と `cor:pg-hesse-hessian-form` は、純中心補正の前後を区別して式を確認した。その未公表入力の非可換中心性の証明全体を今回再検証したとは主張しない。

二次 jet 比較に用いた Dito の arXiv:math/9905080v1、§2 式(3)と§3 Theorem2 を確認した。対象は一般 Poisson の二次積と Weyl gauge であり、Lie 代数に限定された後続公式と区別する。Shoikhet の arXiv:math/0007080v1、§1.3 の内向き wheel 消滅と§2.3.1 の逆向き wheel の区別を確認した。出版社で両文献の巻・年・頁・DOIも照合した。非線形 Poisson について中心写像の全高次消滅を主張せず、二次に寄与するグラフの数え上げを本文に与えた。

Artebani–Dolgachev の公刊版§2、Lemma2.1 と式(4)–(5)・p.240を本文とPDF画像で確認し、Hesse j式の規約を照合した。Lin–Zhang の Theorems4.1,5.1 と rotation の回復を比較し、幾何的非同型から圏の結論へ移す際の追加条件を保持した。固定入力Bの `curved_transport.tex`, `gradient_recovery.tex`, `explicit_example.tex` を固定commitから読み、完備移送、中心逆像、低 rotation 積、明示Hesse係数の該当箇所を確認した。この確認を入力Bの全証明の独立検証とは扱わない。

新しい補正について、Kontsevich の著者最終稿 *Deformation quantization of Poisson manifolds* の Theorem4.6、§§4.6.2,6.3、および *Deformation quantization of algebraic varieties* の §2.3 Proposition6 と後続の Conjecture1・Questions1 を一次資料で確認した。二次代数と二次 Poisson 構造の形式対応は既知結果であり、本稿の新規成果に数えない。Mori–Smith arXiv:1502.07403v2 の Theorems1.2,7.2 と Lemma7.1 を確認し、点曲線の Hessian 表示の既知性を Introduction と本文へ明記した。

Antieau–Krashen–Ward arXiv:1409.2580 の Theorem2.2 と証明を確認し、原点を持つ楕円曲線の導来同値から同型への帰結を使用した。De Laet–Le Bruyn arXiv:1405.1158v1 の §2 p.3 にある巡回和の中心元も直接確認した。この式は Rains の非巡回式とは引用箇所を分けた。追加した四文献の刊行年・巻・頁・DOIを出版社の情報と照合した。固定入力Bの `field_model.tex`, `generic_descent.tex`, `coherent_saturation.tex` の該当定理文と仮定を固定commitから読み、`gcd:prop:automatic-as`、`rog:lem:localization`, `rog:lem:descent`、`crs:prop:residual-smooth`, `crs:thm:coherent` の役割を区別した。線束生成残余部分から全 coherent 残余圏へ移る入力を、有限降下だけで代用しない。

既存の点検では、Kontsevich の harmonic-angle 配置空間と向き（著者最終稿§§2.2,6.2）を反射による偶奇性と照合した。Lindberg–Pym arXiv:2408.16685v1 §1.6と§6.7 Theorem6.9、Remark6.10を一次資料で確認し、qが原生成元の星積係数比であること、元のKontsevich formalityが適用範囲に含まれること、任意stable formalityへの拡張に残る条件を点検した。Ciliberto–Ottaviani arXiv:2006.07213v1 Theorem5.7とp.17の二回合成、Ottavianiの2024年刊行版§3のAronhold不変式の25項・古典的縮約も確認し、本稿の射や応用と既知の構成要素を区別した。

保存済みの graph 検算に用いた一次資料として、Banks–Panzer–Pym, *Multiple zeta values in deformation quantization*, Invent. Math.222(2020),79–159、DOI [10.1007/s00222-020-00970-x](https://doi.org/10.1007/s00222-020-00970-x) の Corollary1.3と続く段落（著者稿印刷p.6）、二変数 log-canonical 星積の展開（同p.3）、§6を確認した。harmonic weights の五次までの有理性は既知入力である。Buring の2022年学位論文 *The action of Kontsevich’s graph complex on Poisson structures and star products: an implementation* の§§3.4.1–3.4.2、印刷pp.74–76で重複度と係数規約を、§3.5、p.89で `star5.txt` の使用を確認した。[著者公開資料](https://www.rburing.nl/gcaops/)から組立済みの星積と独立した graph–weight 対を取得し、双方を照合した。一次資料の積分の証明を独立に再証明したわけではない。

Banks–Panzer–Pym の2022年訂正、Invent. Math.229(2022),449、DOI [10.1007/s00222-022-01122-z](https://doi.org/10.1007/s00222-022-01122-z) は[出版社PDF](https://link.springer.com/content/pdf/10.1007/s00222-022-01122-z.pdf)を確認した。原論文p.150、§6.2の係数は b=−1/2⁸ に訂正される。原論文の同節が対象を型(7,2)の graph と明記していることも照合したため、現行稿で使う五次以下のデータには影響しない。

Etingof–Ginzburg の刊行版§8.1、印刷pp.1407–1408、Proposition8.1.1・式(8.1.3)を現行稿の形式 potential と比較した。unimodular な形式 Poisson tensor の相対 Jacobian potential による認識は既知の先行結果であり、存在そのものを新規成果に数えない。限定的な追加文献検索では本稿の混合五次公式と四次 potential の既出箇所を確保できていないが、新規性の確認が完了したという意味ではない。全ての数値係数は指定 harmonic-angle・生成元固定・中心規格化に関するもので、任意 stable formality や任意 gauge から独立とは主張しない。

残余射の既存点検では、Wang arXiv:1906.04891v3 §3、Corollary3.2・Theorem3.3、Hwang arXiv:2501.08633v1 Theorems1.5,1.6・Propositions2.2,2.6・Corollary2.7を一次資料で確認した。Toën–Vaquié arXiv:math/0503269v5 の Lemmas2.8,2.10,3.25、Corollaries3.22,3.24、および Bergh–Schnürer の公刊PDF Proposition4.10、Remark6.1、Theorem6.2・Remark6.3を照合した。勾配復元、perfect 核の有限表示と同値性の開性、重み零降下そのものは既知の原理として記載した。

固定入力Bの `field_model.tex`, `generic_descent.tex`, `curved_transport.tex` の定理文と使用する構成を読み、(L),(CF)、三対象への制限後の Laurent 局所化、coherent 飽和性、一般係数体への係数変更の役割を分けた。相対 flow の新しい中心保存補題については、固定入力の `cft:lem:primitive`, `cft:lem:arity`, `cft:lem:flow` と MF 挿入公式を直接照合した。Lindberg–Pym の §1.6、Theorem6.9・Remark6.10を再確認し、対数境界値が原生成元の交換比から全次数で従うことを点検した。

点曲線・尺度の追加では、Fulton–Olsson の公刊版§1、式(1-1)–(1-5)、pp.87–88および Corollary2.4の証明p.91を読み、微分と判別式の変換、j≠0,1728 上のμ₂-gerbeを照合した。Poonen の Theorem1.5と直前の開性の記述を確認し、n≥3の三次に例外がないことを確認した。

scalar 障害について、Knudsen–Mumford の刊行情報を出版社で確認し、twisted perfect複体のdeterminantは Lieblich arXiv:math/0411337v2 §2.2.4、Definition2.2.4.1、period/index は§2.2.5の本文と照合した。Stacks Tags074S,074X の Lemma11.7.4、Lemmas11.8.3–11.8.4により、極大部分体の次数・分裂と index の整除を確認した。固定入力Bの `generic_descent.tex`, `rog:prop:euler` の二重次数とEuler式、`window.tex`, `tw:lem:proper-hom` の任意二有限rank MFのHom、`rog:lem:localization` の有限rankを保つCFを固定commitで確認した。window定理をMF全体の相対同値へ強めて引用してはいない。

Fisher, *Testing equivalence of ternary cubics* の著者稿 Theorem1.1、Definition2.1、Lemmas2.2,2.6、§4を一次資料で確認し、出版社で LNCS4076(2006),333–345、DOI10.1007/11792086_24を照合した。古典的不変量 c₄,c₆ の Weierstrass 規約と微分の変換を、現行稿の Hodge 尺度と合わせた。Fisher が表示する Jacobian の6倍座標変更を、微分を追わずに本稿の規約へ流用していない。Stacks Tag07S5 Lemma66.14.2を自由な有限商に、Tags074S,074Xを index の整除に照合した。Bergh–Schnürer arXiv:1901.08945v2 Proposition5.7、§6式(6.1)、Remark6.1を Hom anchor の補助構成と比較した。これらの一般原理自体を新規とは数えない。

完備中心商については固定入力 `curved_transport.tex` の相対 bar 構成、arity 評価、flow と逆、二ブロック行列と t の重みを確認した。既存の厳密相対中心保存を入力とし、任意の商上の有限自由 MF へ公式を適用する。入力の一般点生成・window の次元条件を n=1へ広げる主張はしていない。

## 2. 証明の記載と読解点検

現行の中心復元、次数付きモジュライ、相対双対、点関手、Jacobi 方程式、残余圏の形式認識の証明を保持した。固定模型の降下、Picard 障害と明示例、Koszul/apolar 同定、八次元の全 Hilbert 関数、横断切片・retract には、執筆担当以外の担当による読解点検と統合時の点検を行った。これは外部査読や形式検証ではない。

| 対象 | 点検した論点 | 適用条件・残る限界 |
|---|---|---|
| 反対代数と残余不変性 | 語順反転・中心直線・trace–Hessian、反転不変な代数的中心族、偶 Weyl symbol に対する W の偶性、支配形式族による射の等式、自由有限商 | 固定残余入力の下。Abel圏の反対や導来双対をrotation保存の共変同値として扱わない |
| 九次中間被覆と18整除 | c₄,c₆の規約、Hesse可換式と次数乗法、SL₃軌道・混合係数・商atlas、幾何学的一般整性、正則体拡大と合成体、有限étale因子2,e_n,9 | 良い一ブロック成分・全n≥3。e_n=1、符号被覆の分裂、他のintrinsic成分は未証明 |
| 完備中心商のMF | 全Taylor成分の中心多重線型性、商の分離完備性、arityによる収束、逆・単位・rank・shift・指定周期、任意のquotient MFへの挿入 | 係数商の明示公式。categorical derived tensorや有限代数的核のcoherent中心線型性の降下は別 |
| scalar indexとEuler格子 | circulant Euler行列と整数格子、thick閉包との区別、d′|dとd|[L:K]d′、標準二重被覆・十八重被覆の各体成分 | 既に選んだ核同型類のscalar段階のみ。実際のindexの下界や非零例は得ていない |
| active 部分の全次数比較 | active 出辺と U=0 制限、同座標 Hesse 分枝の識別、SL₃×A² の支配性、普遍係数恒等式、Koszul と Euler による W_act=b_hJ_g | 固定 split 比較を入力。単なる j の一致を同座標比例へ読み替えず、MF の中心基底変更や n=1 の field-model は未使用 |
| 点曲線と同型被覆 | 支配族からの j の降下、短い Weierstrass 式、[3]q=a、偏極類と Brauer–Severi 平面の étale 降下 | Iの階数18、Dの階数2、I→Dの階数9。Dだけに genus-one 曲線・平面同型があるとは主張しない |
| Hodge と自然な尺度 | 相対随伴のdeterminant因子、重み零、modular formsのweight、τ_pt、η_res、Jacobian-Isomとの同一視 | j≠0,1728 の共通稠密開。modular正規化被覆と点微分の被覆を区別 |
| 符号商射の支配性 | 一般中心liftのc(h)相殺、η=h²・unit、一般特殊点の零切断、既約閉包、同次元性、自己同型なしの開の有限化 | 形式frameの代数化を未使用。一般次数は18e_n、e_nは未決定。比較核の二重被覆への降下は未主張 |
| 点shiftとharmonic尺度 | 固定点なしから平行移動、Jacobianのtorsor作用、deck反転、t=(h/b_h)W_h⊗P₀、tensor比h/c_h、c_hの五次係数 | Ku rotationの制限との同定は未証明。比の代数性や固定harmonic尺度との一致は未主張 |
| kernelのEuler/index | 重み1 perfect Homとdeterminant、p_(N+2)=−3tp_N、数値型の開閉性・非空性、有限表示降下、indexによるrank整除 | 整合する核の同型類を選んだ後のscalar段階。体上indexと一般底上bandを区別。未証明のΦκ_nc=κ_Yを不使用 |
| unsplit体上のindex | rank3重み1の束でβを次数≤3でsplitし、その上のαを次数がd_nを割る体でsplit | α=βを仮定しない。同型類選択前の比較被覆全体の次数は抑えていない |
| 相対積分直線 | D_Q の scheme 的 rank 条件、単元 minor による核・余核の分裂、非被約を含む底変更 | 体上の勾配一意性は Wang・Hwang の既知結果。scalar symmetrizer と射影自己同型群の自明性を区別 |
| 全次元の非空性 | 巡回三次の滑らかさ、Hessian 係数行列の台の交差、N=5 の最小例、active 切断の特異条件 c³=−27/64 | 全 N≥5 の手計算による証明。有限個の次元の計算からの外挿ではない |
| 支配的中心 h-family | δ_h=h⁻¹[x_i,−] の有限自由行列、特殊 Casimir 核、一般中心との同次元性、Ω_h の代数的持上げ、純中心 G による全 torsor fibre の被覆 | 固定 PBW・中心入力。Ω_h+G の特殊三次は F+G、tensor は Π_F のまま |
| 相対残余模型と低 Nat | 有限個の線束・mutation による proper 模型、perfect な源 E→Δ を先に広げる非循環な smoothness 証明、全 cohomology の局所自由化 | rotation の可逆性・底上 perfect 性を明示。compact 相対圏と各 fibre の coherent 飽和性を区別 |
| 中心作用の一般階数 | 可換側の perfect Nat、一般・特殊 H⁰ の等次元性、DVR 完全列による torsion の排除、Laurent 体上への生成性の降下 | 特殊化の単射性だけで結論しない。完備底で三対象が生成するという強化は未使用 |
| 相対 graph flow | Xi=a_hP_0、active な全出辺、中心係数に関する多重線型性、単位正規化、flow・逆・MF 挿入での uId の厳密保存 | 選んだ正規化 flow についての証明。任意の CF 同値への一般化や形式 frame の代数性は未主張 |
| 射影 Poisson 射と尺度 | 全 O-持上げの線束重み、projective cocycle、L⊗det K の重み零、full scale の引戻し torsor、像の支配性 | 固定入力Bの下で既存一ブロック稠密開。Brauer–Severi を許し、全 intrinsic 成分を主張しない。一般相対次元1、連結 fibre・表現可能性は未決定 |
| 有限比較被覆と kernel | 同じ X の generic 核、正規化・分岐除去・perfect cone の台除去、DM chart の有限化、P[2m] による非一意性 | 有限 étale 被覆上で比較。元の stack への kernel 降下は自己同値 torsor と選んだ同型類の scalar gerbe の二段階 |
| trait の良い還元 | 完成格子の有限 jet 降下、saturated Q、積分直線の忠実平坦降下 | CF 依存の滑らかな模型の存在。正準性・相対 Hochschild 格子・kernel の h=0 延長は未証明 |
| very general な超越性 | 再帰の普遍多項式性、厳密 log 境界値、留数の矛盾、有界次数の関係 locus を全 maximal minor で定義 | 任意非空良い開の very general と普遍関数体の主張。単一 Zariski 開の全点や arbitrary formal frame を許す intrinsic な尺度の不存在は未主張 |
| 中心復元・次数付きモジュライ | fpqc 持上げ、μ_d、中心正則対、全次数の切断飽和性、全次数付き同型、有限安定化子、スカラー重みの相殺 | 中心平坦性・普遍低次数中心・良い PBW 表示の仮定を要する |
| 普遍相対双対 | 有限 Koszul 対角、真正な双加群自己双対、中心差分、torsion 比較、compact generator、dg orbit、相対 properness、Serre pairing・trace | 被約有限型の初期基底、有限射影・分裂 PBW・各ファイバーの Koszul/CY・中心三次の分裂正則性。その後の任意底変更には非平坦・非被約を含む。全商上の orientation の自明化は未主張 |
| 固定模型間の全同値 | 係数対象の Gabriel 局所化、faithfully flat な tails の降下、全関手と自然変換の降下、自然自己準同型のスカラー性、Isom_gr/G_m と全 O-保存同値の一致 | 比較定理に列挙した中心・次数別有限射影性・相対 Serre の仮定。一般の Abel 圏族が局所的にこの模型へ入ることや全モジュライの代数性は未証明 |
| 線束障害と三捩れ例 | μ_d と G_m の持上げ torsor の区別、L^d、行列式からの gcd(d,3)、affine 楕円曲線の非主三捩れイデアル、次数別線束 twist と PBW 入力の保持 | 三捩れへの制限は両方の次数一加群が自由な場合。明示例は指定した同値に大域の次数付き代表がないことを示し、二つの代数にどのような次数付き同型もないとは主張しない |
| 局所 O-marked 圏族の効果化 | 一般Grothendieck圏の忠実平坦係数延長、重み付き加群のgenerator・torsion商、任意係数変更、全同値のcocycleから対象を構成 | good模型の全Hom比較が入力。全intrinsic成分の局所表示や変形の閉性は未証明 |
| 表示 gerbe の H² 障害 | determinantの重み、e=1での中心拡大の分裂、cyclic division algebraのvaluation、全非空開のtwistと有理点 | n≡1 mod3で全非空開上の位数3を証明。幾何学的一般点の体に非零Brauer類が残るという主張ではない |
| 相対点関手 | 任意底変更でのKoszul完全性、八次有限局所自由性、相対Cartier、低次数イデアル、点商とshiftの降下、determinant付き相対随伴 | good点スキーム条件。ambient上のO(1)と点空間への引戻しを区別 |
| 中心三次の復元 | Rains式の境界Jacobi評価、中心評価の普遍単射、I(D)₃/I(C)₃と中心直線の逆像 | 非空開上。n=3で全切断への全射を使わない |
| Trace–Hessian 射 | 任意基底の三次Casimir、正規化trace、Hessian縮約の共変性、torsor同型と滑らかな非空開への降下 | 良い局所一ブロック型。Kuとの一致は別であり、別の比較節で具体的な不一致を証明 |
| 強い affine lift と逆構成 | Euler列のコホモロジー、gradient Koszul、強いliftの一意性、divergenceによるJacobi同値、supportと全同型の回復 | 任意のC代数・滑らかな相対三次・n≥3。標的は偏極類とBrauer–Severi ambientを許す |
| Poisson 開の同型と支配成分 | Msm≅Pgood⊂Pdec、周囲B単独の有限性の除去、pairのDM性、Brauer位数、一般三次上の開埋込み | PBW・中心・相対Serre・全同値の入力を保持。唯一の支配成分には既存被約分類を使用。全 intrinsic 圏成分の分類ではない |
| 幾何補正 | F_tの滑らかさ因子、全nに一様なJacobi双対証明書、trace補正u³の非消滅、係数空間の非空開 | 入力の中心性を使用。入力定数族との差と残余復元との差を区別 |
| split Hesse 比較 | exact λ_THとλ_res、j差、symmetrizerの可換代数性と唯一rank3 primitive、固定Πの全smooth cubic Casimirへの障害 | 残余の同定は固定入力Bを使用。rotation保存dg Morita同値なし。n≢1 mod3でのみrotationなしの結論 |
| 一般混合係数の二次 jet | Dito二次式、Θ=−2adj、ρ₂F=Hess/8、inner二輪消滅、h⁴境界のJacobi消滅、Jacobi束切断Δ₂の非消滅開 | 指定formality模型・MF/window入力の下で複素点のmarked形式比較を妨げる。完備MF同値自体の任意基底版・一般混合係数のunmarked一般点非同値は未主張 |
| 代数的 Poisson 補正 | Hessian 縮約と trace の座標共変性、方程式直線の尺度、任意基底変更、flag 付き零切断での微分、étale・支配性、全 O-降下 | 出力と active 制限が滑らかな非空開。次数9により非双有理。固定 tensor は五次で形式逆と異なる稠密開あり |
| 補正射の一般次数 | ψの基点なしP²拡張・次数9、SL₃×A²被覆の微分と次数乗法性、混合の三角復元、traceのf₀独立性、全分枝を残す開、同一群の商への降下 | 全n≥3、商stack上の表現可能有限étale階数9。粗モジュライ次数は別。未公表MF入力に依存しない |
| 点曲線との一致 | 普遍 determinant 恒等式、adjugate による incidence の scheme 的因子化、相対 rank2 の核直線、左右射影 | Mori–Smith の既知公式。shift 付き対応全体と定常成分の同一視は含めない。零パラメータの実際の点スキームは別 |
| 全次数の形式 tensor | 最初の差による正規化一意性、有限 graph 再帰、被約普遍係数上の恒等式と任意底変更、単位正規化、線型中心保存、Koszul と次数による scalar factorization、中心逆像 | 固定 formality・固定 h・PBW/存在入力。滑らかな Poisson 対には全 F も滑らかと仮定。c₂=0を別途証明。有限 Artin 中心とは区別 |
| c₂と偶奇性 | 普遍係数の多項式性と原始係数ベクトルによる分母除去、二次SL₃不変式の消滅、混合制限、配置空間と商群の反射符号、中心写像と反対積 | h独立の二次関係、指定harmonic-angle模型、偶数Weyl中心元。W≡H♯ mod h⁴、π≡Π♯ mod h⁵ |
| 五次tensor の active 制限 | smooth split拡張からのclosedness、Euler積分、最高ウェイト(7,4,4)の重複度、原生成元q比とPBW同型、Sの規格化、混合制限と非空稠密開 | 純active公式とmixed制限は全混合公式の入力。tensor の相違だけから三次やKuの非同値を推論しない |
| 全混合五次項の還元 | Weyl再帰の局所jet性、型qT⁴/M²T³、次元1+2、ε縮約I,J、det−35/3、独立Taylor jetの斉次実現、純active普遍恒等式、中心平行移動 | 二つの jet への評価が普遍係数を決める根拠。特異な試験式から一般対象の結論を直接推測する方法ではない |
| 全混合五次項の係数 | 公刊 weights の73項への縮約、raw weights/Aut と star5/2^k の照合、二つの独立混合 jet、π₃の挿入とWeyl補正、β=1/60・γ=1/240 | 指定 harmonic-angle・生成元固定の普遍多項式。configuration-space 積分自体の再計算や任意 formality への係数不変性は含まない |
| 中心逆像の四次項 | 単位保存と active affine 共変性による局所jet性、型qMT³/M³T²の次元1+1、Ψの入力公式、I・J・SdFの独立性、W₄=Ψ+I/24−J/80とa₄=S/240 | Hessian 正規化した指定中心元と固定 formality。中心元の任意単元倍に対して同じa₄を主張しない。非可換中心性は固定入力 |
| 四次 Jacobi 類の非消滅 | Jがactive勾配イデアルに属すること、τ(J)=0、Eulerの[F]=0、Fermat active式、全nの滑らかなF_*とℓ(Δ₄)=−1/9、Jacobi束の非消滅開 | 全混合の滑らかな係数空間の非空開。全 intrinsic O-moduli の各成分を覆う結果ではなく、純中心像による商束の一定階数性も仮定しない |
| 四次の標識付き比較障害 | H⁰(T)=0、HH¹=0と実際の幾何的KS写像の単射性、小拡大上の二つの持上げの差、Artin切断と両立するMF/window移送 | 全n≥3、n=4を含む。圏への適用は固定MF/window入力付き、同じhと特殊ファイバーの標識を保持する。HH³消滅や幾何変形の全射性を使わず、unmarked一般ファイバーの非同値は未主張 |
| 全 O-降下する四次補正 | S_P,I_P,J_Pの縮約、traceの底変更、方程式の尺度と純中心加法、単元倍のP、滑らかな非空開、H^[4]≡W mod h⁶とtensorのmod h⁷一致 | 有限の代数的射。全次数の収束・代数化・残余同値の降下は未証明。旧Hessian補正の次数9や厳密な点曲線一致を新射へ転用しない |
| I,Jの古典的微分表示 | 独立なT,M,qでのadjugate–Hessian縮約とAronhold不変式の方向微分の恒等式 | 係数環上の厳密多項式検算。既知不変式Sや古典的演算自体の新規性を主張しない |
| split 族の正の残余比較 | 独立 λ,s の中心係数と TH 出力、点曲線 ν、Heisenberg 同変性、j 分岐点を含む形式枝、active scale、固定標的への有限降下と coherent 飽和性 | 全 n≥3・各固定 λ、1+λ³≠0。MF・window・生成性・有限降下・coherent 飽和性は固定入力。一般混合係数や全 O-同値への残余同値の降下は含まない |
| Jacobi の二次式と既知結果 | 全係数環の式、Plücker 空間、普遍核、ρK/2 の係数と符号、Koszul strand の双対、N=5 の終端、total Betti 数から必要な graded Betti 数への帰着 | N≥11 の一般階数の最大性は未決定。一般 Koszul 性から β₄,₆=0 を推論しない |
| 八次元の頂点 | I₃=J₃ から全次数の一致、J/I=C(−2)^330、socle・飽和・根基、非分裂性、任意底変更の相対版、一次分解 | この結果は一般点被約分類に依存しない。長さ330は J/I の長さであり、明示した m-primary 成分の商 R/Q の長さ5401とは異なる |
| 非零点の局所構造 | 法接空間 Λ³K、横断方程式から混合項の消去、全 W 方向の polar 条件、Thom–Sebastiani 特徴付けと scheme retract、n≥11 の特殊非零点への330次元部分空間の注入 | 横断切片を Grassmann 方向との局所積とは主張しない。特殊例の周囲の冪零根基全体が二乗零とは主張しない。n=11 は構成が与える下限であり最小性は未証明 |
| 一般次元の頂点と高次数 | 悪い incidence の次元評価、有限長性・飽和・随伴素点・深さ、各固定次数の漸近非消滅 | 一般次元の有限長性には既存の被約分類を入力する。n=9,10 の全 Hilbert 関数と、一般次元の冪零根基自身の積は未決定 |
| 残余圏 | HH sector の次数、幾何的 KS、滑らかな変形源と形式認識、tame hull、n=4 の例外、rotation | 通常 Artin 基底・特殊ファイバー固定・一次切断。全高次群oidや導来基底、全 Abel 形式変形との同定、全 intrinsic 成分を覆う大域残余射は未主張 |

本版の新しい主張では、列挙した入力と仮定の下で内部読解点検による未解決の論理的欠落は報告されていない。これは証明の記載と内部点検の状態であり、外部査読や Lean 等による形式検証ではない。既存の主張の全証明を本版で一括再検証したという意味でもない。

## 3. 二次階数の整数証明書

保存済みの全6例について、指定した平方小行列の行列式を探索とは別経路で直接計算する検証が完了している。以下はその保持した結果と対象資産のハッシュである。全6例の再実行は本版の追加検証には含めない。

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

`computations/verify_center_hessian.py` は保存済み検算で SymPy 1.14.0 により全assertionと二つのPASSを確認したコードである。本版ではこの既存計算を再実行していない。検算対象のSHA-256は `20bb71ce1b8c56f0e81a3776dce38c1f1f786ec54a44c409a0ecf2c71d4721bc`。浮動小数点、係数の補間、ランダムな有限標本は使わない。

- 公刊Rains式の可換化と、κ=−4h⁴(1+λ³)/(1−hλ/2)⁶ の差が三偏微分のイデアルに入ることを、明示的な係数恒等式で確認した。統合担当は別の短い式の簡約でも係数を確認した。
- HessianのJacobi類が8(1+λ³)xyzとなる恒等式と、固定入力のHesse中心のW−λUを確認した。
- 六つの混合係数を独立記号とするFermat型の八次自由代数を、平方自由単項式の基底で扱い、正規化traceと有限hの純中心補正を計算した。これは任意個の中心変数への特殊化を許す係数恒等式である。
- 最後の比較に用いるΩの非可換中心性は、固定入力の `cor:pg-hesse-hessian-form` を使用する。このスクリプト自体がその中心性やPBW性を再証明するわけではない。

### 幾何補正と残余比較の保持した厳密検算

`python computations/verify_geometric_corrections.py` は保存済み検証で全assertionと13個のPASSを確認したコードである。本版では再実行していない。検算対象のSHA-256 は `78f592342b91531a6382576cc6025c8684e7f56d5efa84019b02d91b9923b85c`。その確認対象は次の通り。

- 四変数の二十個の三次単項式上で全十六個の gradient 一次倍を消す多項式汎関数、u³での値3t、t=1での階数16→17。
- 滑らかさの二因子 `(1+12t³)(1+2t³+5t⁶)` と、八次自由臨界代数のtraceによる `F_t+h²t³u³`。
- 一般Hesse中心元のh⁴境界項がg_λの倍数であり、境界Jacobi環で零となる恒等式。
- 独立六記号の対称3×3行列について、Θ=−2adjの全九成分とρ₂F=det(Hess)/8、線型形式の星積冪の帰納係数。
- Fermatの二次差 `xyz/3` のJacobi非消滅。追加の中心変数への一様性は本文のテンソル積による証明であり、有限個の次元の標本確認によるものではない。
- split Hesse の `b_h−h a_h=−2h²(1+h³)/3`、λ_res−hの有理式、j差の初項13824h⁴とh⁶までの係数。
- active symmetrizerの九元一次方程式で、明示八次小行列式 `λ²(λ³−8)²` と核がscalarであること。

traceについては、別担当がGroebner基底と八次乗法行列を別実装し、本文の値を独立に再確認した。上のスクリプトは非可換中心性、formalityの存在、MF同値、Torelliを機械的に証明するものではない。

### Poisson 補正について保持している厳密検算

保存済み検証では `python3 computations/verify_poisson_correction.py` を実行し、SymPy 1.14.0 で全assertionと11個のPASSを確認した。本版ではこの既存計算を再実行していない。独立した十個の三次係数、六個の対称行列係数、独立な λ,s を用い、浮動小数点・補間・有限標本への特殊化を使わない。

- `adj(C(p))=ppᵀ` と `det(C(p)+tM)=t pᵀMp+t³det M`。
- 全三変数三次での Euler–Hessian 恒等式と点曲線 `g+s²det(Hess(g))/24`。
- 二パラメータ Hesse 係数 A,B,ν、変位 ν−λ、中心元の係数を既知の cyclic 式から変換した恒等式、Hessian 正規化と h⁴ 項。
- Sklyanin 点曲線の係数と移動切断、λ=s=h での固定入力の式、二次・四次係数。
- 方程式直線の rescaling と active 座標だけによる規格化。
- 研究ノートの framed 二パラメータ chart における一般次数9。分子次数9・分母次数6・多項式 gcd が1であることを有理関数体で確認した。全混合係数と商 stack の次数9には別途本文の証明を使う。
- 混合二次項の線型写像Lの6×6行列式、active全十係数での微分行列式。
- framed p′=1 被覆の判別式の全係数とresultant、次数10・平方因子なし。S₉という群の帰結は研究ノートの位相的議論を併用する。

Hesse 係数と cyclic 中心式の変換は、別担当の短い独立実装でも確認した。共有 repo には重複実装を残さず、上の検証器へ必要な assertion を統合した。この検算自体は非可換中心性、formality の存在、MF 同値、有限降下を機械的に証明するものではない。

### 五次共変式・四次 scalar jet の厳密検算

`python3 computations/verify_cubic_covariants.py` を実行した。Python標準ライブラリの整数とFractionのみを使い、次数1〜8の三次共変式の重複度 `1,0,1,0,1,0,2,0`、不変式の次数2,4,6の重複度 `0,1,1` を有限の重み計数で確認した。四つのε縮約の6⁴項を有理数として展開し、Sが25個の整数係数単項式を持つこと、S(xyz)=1、S(g_λ)=λ(λ³−8) を確認した。五次tensorの係数1/80はこの計算だけから得たものではなく、Lindberg–Pymの既知定理と本文のPBW・一意性の証明を用いる。Kontsevichグラフ重みを直接積分した検証や形式証明器による確認ではない。

同じ検証器で混合jet型の重複度1,2、三つの勾配共変式の独立性の行列式−35/3、I(g)=J(g)=S(g)gの比例係数を確認した。重み計数は別担当が別の多重集合列挙でも照合した。保存済み検証では qMT³ と M³T² の scalar jet も加えて現行検証器を実行し、最高重み(4,4,4)のWeyl公式の六項がそれぞれ `(156,−136,−136,100,109,−92)` と `(122,−105,−105,78,84,−73)`、和がいずれも1であることを確認した。保存コードは共通の有限重み計数を共有し、重複実装を残していない。この重み計数だけで graph の数値係数や中心逆像を決めたわけではなく、以下の別計算と本文の局所共変性の証明を併用する。

### 混合五次 tensor と73項 graph certificate

`python3 computations/verify_mixed_fifth.py` と、その `--source-directory` を指定する元資料照合を実行し、全assertionと全PASSを確認した。Pythonの整数・FractionとSymPyを使い、浮動小数点や数値積分を使わない。入力 `computations/data/harmonic_linear_products.json` は必要な73項だけを収め、元ファイルのSHA-256、取得元、係数規約、graphの辺・weight・自己同型群位数を記録する。二つの新規資産のハッシュは次の通り。

```text
computations/verify_mixed_fifth.py
8388956c8cf6bee1e4e28f20a36edbe6d01ac1586779dd4ced86d0b3fc2db0d8
computations/data/harmonic_linear_products.json
fc960343d5f4f1536881bf678b8bc4fda9a438e0dc0f029fe6d7840364b6d7d6
```

Buring の元資料 `star5.txt` のSHA-256は `05e0689ddb32a3d3a3ee4475086606bbeb9b5d71f8e24da2c216e43564a31129`。線型二入力と二次tensorに寄与する条件で残る非零項数は、頂点数1〜5の順に `1,1,1,19,51` である。原資料の `fg+h{f,g}` 規約を本稿の `fg+h{f,g}/2` 規約へ変換し、k次の組立係数を2^kで割る。aerial頂点の置換、outgoing edgeの交換符号、自己同型群の位数を含む有限列挙により、全73項で組立係数/2^kとraw weight/Autが一致することを確認した。元資料11ファイルのハッシュも照合した。

五次再帰には π₃=Π_det(Hess F)/24 の一頂点への挿入の和と、二次式のWeyl対称化の四次係数を含めた。表はxy成分の厳密値であり、W列はこのWeyl寄与を表す。

| 試験式・評価点 | B₅ | B₃のπ₃挿入 | W | π₅=−2(B₅+B₃)+W |
|---|---:|---:|---:|---:|
| xyz、(1,1,1) | 1/720 | 0 | 11/720 | 1/80 |
| xyz+z²/2、(0,0,1) | 1/480 | 0 | −1/144 | −1/90 |
| xyz+z、(0,0,1) | 1/720 | 0 | −1/240 | −1/144 |

後二式は一つの中心変数uで斉次化してからu=1とする。二定数への普遍還元と合わせて β=1/60、γ=1/240、α=−1/120 を得る。各試験jetで三次再帰も既知のHessian項と一致した。独立した非log型混合jet `(x³+y³+z³)/3+xyz+x²/2+xy+x` の原点では、volume-dual五次成分 `(1/30,−11/720,1/36)` が三共変式の公式と一致した。また二変数Poisson tensor `xy ∂x∧∂y` の原生成元積の五次までの係数 `1/2,1/24,−1/48,−1/1440,1/480` がBPPの公刊展開と一致した。

別担当の独立したFractionによるgraph縮約も、二つの混合試験式と定数β,γについて同じ値を与えた。さらに元graph–weight対の別実装で符号・自己同型群・正規化を独立に照合した。保存対象には再現に必要な一つの検証器と証明書だけを残し、独立実装の重複や大量の元資料は収録しない。73項の入力は公刊weightsに依存し、この検算はconfiguration-space積分の再証明、全次数のformality、MF同値、形式証明器による検証を含まない。

### 四次中心 potential と一般次元の障害

`python3 computations/verify_fourth_potential.py` を実行し、SymPyの厳密多項式演算で全assertionと6個のPASSを確認した。次の四項目に、下記の古典的表示の二恒等式を統合した現行コードによる実行である。

- Hesse係数 λ,A,B,C,D,E,H,G を独立記号として、入力中心元の四次symbol Ψ と `−SF/80−I/40+J/60+C₄(U)` の全係数が一致すること。
- 別途graph計算で得たβ,γから、`W₄=Ψ+I/24−J/80`、`a₄=S/240`、五次tensorの式が恒等的に両立すること。
- Fermat active切断で Jが勾配イデアルに属する明示恒等式と、`[Δ₄]=[ACx+ABy+BCz+AH+BD+CE]/9` を与える係数恒等式。
- 全次元に共通するF_*の三次単項式上の線型汎関数ℓが、全gradientの一次倍と純中心三次を消し、`ℓ(Δ₄)=−1/9` となること。

全nへの拡張は追加変数が独立な三乗で現れる本文の証明を使い、有限個の次元の実験から推測したものではない。F_*の滑らかさ、Jacobi束の非消滅開、scalar jetによるW₄の普遍性、標識付き幾何・Ku比較の小拡大の議論は本文の証明と内部読解点検に依存する。これらの全てをこのスクリプトが機械的に証明したとはしない。

Ψは固定入力Aの `cor:pg-hesse-hessian-form`・`eq:pg-hesse-hessian-closed` にある指定中心元から採った。純中心補正と中心元の単元倍を区別し、Ψの可換Weyl symbolの展開を検算した。その非可換中心性やPBW性自体を再証明したとは主張しない。別担当も全Hesse係数のΨ恒等式を独立に記号検算した。Kuへの四次障害は指定MF・window入力付きであり、固定h・特殊ファイバーの標識を外した一般ファイバーの非同値へ拡張しない。

### I,Jの古典的表示の独立検算

独立したSymPy検算で2個のPASSを得た。対称三次tensor Tの10係数、対称行列Mの6係数、ベクトルqの3係数を全て独立記号とし、次の二恒等式の差が有理数係数多項式として零であることを確認した。補間や数値標本を使わない。

\[
 I=\frac1{12}\operatorname{tr}\!\left(\operatorname{adj}(M)
  \left.\operatorname{Hess}_x\det\left(M+\sum_kT_{::k}x_k\right)\right|_{x=0}\right),
\qquad
 J=\frac14\,dS_T[N],\quad
 N_{ijk}=\frac{M_{ij}q_k+M_{ik}q_j+M_{jk}q_i}{3}.
\]

後者の方向微分は、SをTの10個の独立係数の多項式として微分している。この独立検算の後、二つのassertionを現行の四次検証器へ統合し、全6項目の実行成功を確認した。現行検証器のSHA-256は `a58f1f8f1979a3d289ff55bb2665a2c008bab3e7e9fe2a49b6343c27c661f2d4`。独立実装の重複は保存しない。

### active 不変量の厳密恒等式

`python3 computations/verify_active_invariants.py` を実行し、終了コード0を確認した。S=c₄、T=−c₆の規約で、Hesse不変量のJacobian、rψ=arの両成分、D=1−S/24−T/216−S²/6912に対する判別式恒等式 `(a₄³−a₆²)=(S³−T²)D³`、`det Da=(1−S/16)D²`、反対符号に対する不変性を有理数上の多項式係数として照合した。浮動小数点、ランダムな代入、有限次元の外挿を使わない。degree9およびdegree18e_nの幾何学的部分は別途本文の証明に依る。

## 6. ソース・組版の確認

### 最終ソース検査

`python3 scripts/check_sources.py` を実行し、17個のTeXソース、重複のない287ラベル、176個の参照先、62個の引用キーを確認した。input・本文参照・文献キーに欠落はない。README・方針・ノートの内部ラベルを照合し、Markdown の相対ファイルリンク29件の参照先が存在することを確認した。正本は41ファイルで、既存40ファイルを保持し、active 不変量の検算コード1本を加えた。既存12計算資産の Git blob SHA は保存済み v11 と全て一致する。

主原稿、空の著者欄、分割 root、repo ルート基準の input、build/ の PDF/SyncTeX は維持している。入力稿の外部ラベルは固定commitの参照として、内部ラベルと区別して照合した。

### 最終組版と表示

LuaLaTeX・latexmk で最終ソースを組版し、終了コード0を確認した。最終 PDF は166頁・1,534,376 bytes、SHA-256 は `63bf273af60813bf938c7f20689cd36e8fcf790825943535917ebd2781b58c7b`。未定義参照・未定義引用・overfull/underfull box はない。数式の小さい添字について4.5ptを5ptへ置き換えるフォント警告は残る。著者欄は空欄で、表題・subject・和文フォントを含む全フォントの埋込み・文字抽出を確認した。

全頁を画像化し、14枚の一覧画像で全166頁を目視点検した。概要、中心係数商、Euler 格子と index、反対代数、九次中間被覆と18の整除、参考文献は拡大画像でも確認した。命題の一行だけの頁末への残留と参考文献末尾の疎な頁を調整し、変更頁を再点検した。最後の参考文献調整後、本文161頁の画像 hash は直前の点検済み画像と一致し、変化した参考文献5頁を再確認した。全頁の抽出テキストの外接矩形も紙面端から18pt以上の範囲に収まり、点検した範囲に欠け・重なり・意図しない空頁は見られない。

これらは組版・表示の点検であり、数学的な証明の検証とは別である。PDFと画像はGitの追跡対象に含めない。

## 7. 再現と保存の区別

再現手順はルートの `README.md`。原稿は `latexmk papers/nc-cubic-n-fold.tex` で `build/` に出力する。主要依存は LuaLaTeX・LuaTeX-ja・和文フォント・標準 TeX パッケージ、Python 3・NumPy・SymPy、C++17 コンパイラ。次数三の検証は約450 MBの行列を再生成し、直接消去には約220 MBのメモリを用いる。大行列は保存せず、220個の入力・行番号の圧縮表・検証コードから再生成する。

保存対象は現在の原稿、研究方針、研究ノート、本検証範囲、書誌、再現コード、証明書、必要な設定だけ。入力稿の全コピー、旧稿、旧bundle、担当者別レポート、外部文献PDF、ビルド中間生成物を含めない。PDFは再生成物として提供し、Gitの追跡対象に含めない。

外部への保存は生成・検証とは別に、GitHub の tree にある全ファイルの blob SHA を手元のソースと照合し、通常の fast-forward による main の更新後に、先端 commit と tree を読み直して確認する。保存された版の識別子は Git の履歴と配布時の報告に記す。この文書だけをもって、未実行の外部保存が完了したとは扱わない。
