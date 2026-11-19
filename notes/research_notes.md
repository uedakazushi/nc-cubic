# 非可換三次 n-fold：現行研究ノート

2026年11月20日 / v8。研究方針は `../00_research_plan.md`。証明全文は現行論文に置き、このノートは依存・適用範囲・障害・再現の入口をまとめる。

## 1. 記法と成果の確実性

n ≥ 3、N = n+2、r = n−1。次数一生成元空間は V、中心部分は U、dim U = r、active 部分は3次元。点の空間 W = V* を用いるので F ∈ Sym³V = Sym³W*。B は周囲二次代数、A = B/(w) は中心三次商。QGr は全次数付き加群の torsion による Gabriel 商であり、qgr や compact dg 残余圏と混同しない。

現行論文には主要結果の証明を記載した。次の区分を守る。

| 主張 | 状態・依存 | 証明所在 |
|---|---|---|
| 任意 d の中心 Veronese 復元 | C-flat、rank U≥2、普遍低次数中心条件の下で証明 | `thm:nfm-central-veronese` |
| 全整数の切断飽和性 | 中心正則対と C-flat から証明。noetherian 性不要 | `lem:nfm-central-saturation` |
| b_n 次元の次数付き DM stack、s_n 次元 torsor | 明示した相対 PBW・中心量子化入力と周囲代数の有限安定化子開を使用。全次数付き同型と有限性は本文で証明 | `prop:nfm-graded-presentation`, `lem:nfm-finite-stabilizer`, `thm:nfm-central-torsor` |
| 普遍相対双対、compact 性、proper Hom | 良い相対 PBW 表示チャートの明示した有限射影・分裂入力から、任意底変更と両立する構成を証明 | `thm:nfm-relative-ambient-cy`, `thm:nfm-relative-line-cohomology`, `thm:nfm-relative-serre` |
| 固定表示模型間の全 O-保存 Abel 同値との比較 | 上の相対双対入力の下で、任意係数変更・全同値の fpqc 降下を含めて証明。局所一ブロック型の対象効果化の入力 | `lem:nfm-coefficient-objects`, `prop:nfm-equivalence-descent`, `thm:nfm-fixed-model-comparison` |
| 大域の次数付き持上げの障害 | 指定した同値の線束 L_F∈Pic(R)[n−1] を同定。次数一が自由なら Pic(R)[gcd(n−1,3)]。非自明な三捩れ障害の明示例を構成 | `prop:nfm-lifting-line`, `cor:nfm-three-torsion-lift`, `prop:nfm-nontrivial-three-torsion` |
| 局所一ブロック型の O-marked stack | good 模型の fpqc forms を係数変更付き Grothendieck 圏として定義し、重み付き tails で対象を効果化。全 intrinsic 成分の被覆は未証明 | `thm:nfm-local-moduli` |
| 対象の H² 表示障害 | e=gcd(n−1,3) で消える。n≡1 mod3 では任意の非空開に非零障害の C(s,t)-点があり、位数は正確に3 | `prop:nfm-presentation-gerbe`, `thm:nfm-brauer-dense-open` |
| 相対点スキームと型 (2,2,2,3) | 任意基底変更で有限局所自由八重被覆・相対CI・点商関手・shift・中心射影を構成し、O-marked stackへ降下 | `thm:relative-point-nfold`, `thm:point-omarked-descent` |
| 点対応から中心商の復元 | 境界 Jacobi 線への中心評価が非零な非空開。Rains の公刊中心公式を使用 | `prop:point-jacobi-evaluation`, `thm:point-central-recovery` |
| Trace–Hessian による Poisson 射 | 任意基底変更に両立する三次空間の同型と torsor 同型、滑らかな三次を与える非空開。標的は Brauer–Severi ambient・偏極類を許す | `lem:point-relative-casimirs`, `thm:point-trace-hessian` |
| 滑らかな三次上の強い affine lift | 任意基底で一意な二次 lift Π=ι(dH)P と Jacobi 条件の同値を証明。非零分解可能 P から一ブロック support を復元 | `thm:poisson-strong-lift`, `cor:poisson-support-recovery` |
| 滑らかな pair の O-marked stack と Poisson 開の同型 | 周囲単独の有限安定化子を外し、良い PBW・中心・相対 Serre・点条件を保持。Msm≃Pgood⊂Pdec、自己同型と任意底変更を含む | `thm:poisson-good-open-isomorphism`, `cor:poisson-enlarged-brauer` |
| 全 Poisson moduli の唯一の支配成分 | 既存の一般三次の被約分類と本稿の非零部分のスキーム構造を使用。その一般部分への開埋込み。特殊三次上の別成分や全 intrinsic 圏成分は未分類 | `cor:poisson-generic-open-immersion` |
| Trace–Hessian 補正の非自明な幾何変形 | 固定入力の中心公式の下で、全 n の明示族 F_t の KS 類を証明し、非消滅を混合係数の非空開へ拡張。比較相手は入力の定数族 | `prop:trace-uniform-jacobi-class`, `prop:trace-nonconstant-classical-family`, `cor:trace-generic-geometric-correction` |
| Trace–Hessian と残余復元の不一致 | 固定入力の残余復元を用いる全 n の split Hesse 族。一般ファイバーの射影非同型、rotation 保存 dg Morita 同値の不存在。n≢1 mod3 では rotation 標識も不要 | `thm:nfm-th-residual-obstruction` |
| 固定周囲 Π の全三次 Casimir に対する障害 | 同じ Hesse 族で、純中心三次や非零規格化を替えても X_res と射影同型にならない。中心側がさらに分解する場合も含む | `cor:nfm-casimir-selection-obstruction` |
| 代数的 Hessian–trace 補正 | 任意基底と全 O-同値へ降下し、適切な開で有限 étale 階数9。active 切断は元の楕円点曲線。指定正規化で W≡H♯ mod h⁴ | `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet` |
| 固定 formality の全次数補正 | 正規化逆 tensor の一意性、元の中心一次空間の保存、π_h=a_hι(dW_h)P と中心逆像。被約有限型普遍模型から任意基底変更。代数化・formality 独立性は含まない | `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir` |
| 形式 jet と五次の相違 | c₂=0、π,a は奇級数、W は偶級数。純 active π₅=S(g)Π_g/80、混合制限にも成立。固定 tensor は一般に五次で有限補正と異なる | `prop:nfm-third-tensor-scalar-zero`, `prop:nfm-normalized-parity`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction` |
| split 族の補正後三次と残余比較 | 全 n、任意の滑らかな固定 λ。MF・相対 window・有限降下・coherent 飽和性の入力の下で、有限拡大上の rotation・周期保存同値 | `thm:nfm-split-corrected-residual` |
| 一般混合係数の二次比較障害 | 指定 harmonic-angle formality・厳密模型・MF/window 入力の下で、特殊ファイバー上恒等の形式比較を全 n で排除。一般ファイバーの unmarked 非同値は結論しない | `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction` |
| 3≤n≤7 の一般 Jacobi スキーム | 整数小行列の非零証明書により証明 | `thm:nfold-low-dimensional-generic` |
| n≥8 の I_F≠J_N、頂点完備化非同型 | 全滑らか F。被約分類に依存しない方程式数の証明 | `thm:nfold-high-dimensional-nilpotents` |
| n≥8 の一般 F での非被約性 | n=8 は次数三の証明書だけで証明。n≥9 は入力論文Aの √I_F=J_N を使用 | `thm:nfold-eightfold-square-zero`, `thm:nfold-high-dimensional-nilpotents` |
| 二次部分の一般階数と下界 | Koszul flattening の既知の上界を座標で証明。N≤10 の最大階数を整数小行列で再現。N=9,10 の最大性は Boij の既存 Betti 計算からも従う | `lem:nfold-universal-row-relations`, `lem:nfold-apolar-betti`, `thm:nfold-low-dimensional-generic` |
| n=8 の頂点の全構造 | 次数三の全射性の厳密な証明書から J/I=C(−2)^330。socle 長さ330、二乗零、完備局所拡大の非分裂。被約分類に非依存 | `lem:nfold-cubic-syzygy-test`, `thm:nfold-eightfold-square-zero` |
| 非零点の局所構造、頂点の有限長性 | 法接空間 Λ³K と横断切片を証明。一般全次元の有限長性・全射影化には既存の被約分類を使用 | `thm:nfold-normal-tangent`, `cor:nfold-vertex-support`, `thm:nfold-transverse-slice` |
| 特殊三次の非零点での非被約性 | 全 n≥11 で、局所環と射影スキームに330次元の二乗零部分空間を持つ滑らかな例を構成。直和の retraction を使用 | `prop:nfold-ts-retract`, `cor:nfold-special-nonzero-nilpotents` |
| 高次数の非零性・次数幅 | 標準単項式の Hilbert 関数と生成式数から証明。n=8 を除く冪零根基自身の積の指数は未決定 | `prop:nfold-higher-nilradical` |
| n≠4 の通常 Artin 残余形式認識 | 既知 HH 計算・実際の KS 単射・Lurie の tame 圏変形を用いた証明 | `thm:nf-residual-formal` |
| 全 Abel 形式近傍・大域残余射 | 未完成。Poisson 計算・次元一致からは結論しない | 研究方針の未解決課題 |

証明の記載と今回の点検を、外部査読や機械形式検証と同一視しない。新規性の網羅的確認は未完了である。

### 一般次元の四つの目標を接続する際の注意

研究方針の主目標は、各既約成分の一般 O-marked moduli、point scheme、Poisson moduli への射、同じ X の Kuznetsov 成分との比較である。固定良好模型間の全 Hom 比較は対象の局所表示を与える定理ではなく、一ブロックの商 stack を構成することと全成分の一般対象を覆うことは分ける。各型の一般点で入力を確認し、複数ブロック型を一ブロックへ無条件に還元しない。

点商関手、shift のグラフ、中心射影は、全 O-同値の局所次数付き持上げを用いて局所一ブロック型の O-marked stack 上へ降下する。圏全体の次数一 shift を大域に選んだという主張ではない。定常成分 D と楕円成分 E は一般族の研究対象であり、E をモジュライの boundary と取り違えない。

Poisson 射は、正規化 trace と尺度付き Hessian から量子中心三次 w に古典 Casimir H_w を対応させることで構成した。滑らかな X_w=V(H_w) 上の tensor は一意な強い affine lift を持つため、lift を補助標識として保持せず、非零分解可能な三次 Poisson 対と偏極類のモジュライを標的にできる。良い開では逆構成があり、Msm≃Pgood となる。実際の相対 O(1) と偏極類は区別し、Brauer–Severi ambient を許す。この同型は指定した trace–Hessian 処方についてのものであり、Ku と整合する唯一の逆量子化を意味しない。

残余圏の復元が与える X_res と、trace–Hessian 射の X_TH は一致するとは限らない。全 n の split Hesse 族では、固定入力の下で幾何学的一般ファイバーの射影非同型を証明した。同じ周囲 Π の三次 Casimir を選び直しても解消しない。これに対し、座標不変な代数的補正 Φ と、固定 formality の形式 Poisson tensor を構成した。Φ は全 O-同値へ降下し、形式 tensor は元の support を全次数で保存する。split 族では Φ の三次への残余比較を入力Bの下で得る。Φ の一般次数9、全混合係数の c₂=0・偶奇性と、active 制限での五次 tensor の相違も確定した。次に必要なのは一般混合係数の残余四次項と tensor の五次混合項、残余同値の降下である。一般混合係数で得た二次 jet 障害は marked な形式比較の結果であり、unmarked な一般ファイバーの反例へ無条件に拡張しない。必要な有限係数拡大、rotation・三次周期、同値核の降下は保持する。

general の稠密 Zariski 開、幾何学的一般点、very general の可算例外除去を区別する。very general な同値の存在だけでは、代数的な族の射や同値核の降下を得ない。まず関数体上の構成とその定義体を調べ、有限表示等の必要条件を確認して稠密開へ広げる。n=4 の幾何 locus と n≡1 mod3 の rotation 問題は、general を仮定するだけでは解決しない。

## 2. 入力研究の正確な範囲

`nc-cubic` の固定 commit は `eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59（いずれも2026年11月14日）。

- 論文A `poisson_geometry.tex`：`prop:pg-represent` の bivector 表示、`prop:pg-jacobi-extension` の affine Jacobi 延長、`thm:pg-normal` の複数 Jacobian ブロック正規形、`cor:pg-generic` の一般三次における被約 Grassmann 錐。全次元の一般 Jacobi スキームの有限長冪零根基を論じる際には最後の被約分類を使う。二次方程式の不足、n=8 の長さ330の定理、およびその直和から作る特殊三次の非零冪零例は、この被約分類に依存しない。
- 論文A `general_dimension_universal_quantization.tex`：`thm:pg-all-dimensions`, `prop:pg-ad-relative-chart` が中心量子化の入力。一ブロック相対 PBW 開と中心三次束の存在は、この研究稿と Etingof–Ginzburg の既知の構成から取る。今回その全証明を独立に再検証したわけではない。
- 論文B `generic_recovery/main_result.tex` 等：既に全 n≥3 が対象。C[h]_(h) 上の次数別有限自由な中心三次対が、多項式環と滑らかな三次式へ特殊化する場合を扱う。一般点の coherent 残余模型は rotation と指定三次周期を保つ。方程式は C(h)、同値核は有限拡大上という区別を守る。全パラメータ・任意の nc cubic・核の基底体への降下を自動的に含まない。
- 同論文Bの `cft:thm:complete`, `cft:lem:model`, `cft:lem:center`：選んだ formality と厳密同型 φ に対し、残余 potential は W=C_π^(-1)φ(w) である。W mod h=F は W=F を意味しない。`gcd:thm:field-model` は幾何的な可換模型の存在を得た後の方程式の関数体への降下であり、h=0 での正則性や同値核の同じ体への降下を自動的に与えない。`gre:prop:input`, `gre:prop:hesse-normalform`, `gre:thm:exact-potential`, `gre:prop:jet` の split Hesse 公式を全 n の比較例に用いる。固定標的への一般点比較には `rog:lem:localization`, `rog:lem:descent` を使い、線束生成部分から全 coherent 残余圏へ移るには `crs:prop:residual-smooth`, `crs:thm:coherent` をさらに使う。これらの未公表入力の全証明を今回独立に再検証したとは主張しない。
- 三様体稿 v22 の固定 commit は `6c35d2c84671c2538e61836a6bf3a511392eacce`。任意係数の全 Hom 比較と点スキームの出発点を参照するが、n=3 の形式環を高次元にそのまま転用しない。

古い一般次元ノート中の別リポジトリ名を現行の依存先として使わない。上記の固定 commit と現行稿の参考文献が参照の正本である。

## 3. 中心復元・モジュライで失わない条件

Z(A^(d)) = Z(A)^(d) は、中心元 u に対して u^(d−1)[z,a]=0 と C-flatness を使う。非被約係数でも u は非零因子である。Z(A)_d = Sym^d U だけを書いて、中心 Veronese の同定を飛ばさない。

次数一を復元する最後の段階は A[u⁻¹] ∩ A[v⁻¹] = A である。rank U≥2 を使う箇所はこの二変数 Čech 交叉であり、rank1 に無条件に広げていない。Veronese 同型の持上げ μ_d は次数スカラー内にあり、全 O-保存問題の新しい慣性ではない。個々の同型の大域持上げの H¹(μ_d) と、対象の降下の H² 障害を区別する。

同じ交叉は切断の飽和性も与える。tails 上の射 f の f(u^m)/u^m = f(v^m)/v^m を比較すると、元 a∈A_j が回復し、f は左乗法 a に等しい。これにより負次数の Hom も零となる。一般の Hom と局所化の可換性を仮定せず、既にある射から得た一意な係数を貼る。

一ブロックでは楕円 σ の小位数を 1≤j≤max(3,n−1) で除く。3次元で必要な位数除外だけでは高 n の低次数中心を保証しない。相対中心を任意底変更後にも使うには、有限型被約の普遍底で交換子行列を分裂単射にし、その後に係数変更する。閉点の中心等式だけを非被約底へ外挿しない。

表示空間は Sym³V/Sym³U、群は U を保つ parabolic P、作用は det(g|V/U)^(-1)g(F)。grading scalar を除いた P̄ を用いる。全次数付き同型がこの作用で捉えられることは、関係空間が Λ²V→Sym²V の graph であることと Z(B)_1=U に依存する。

中心束 E の中の W=Sym³U、L=E/W は、それぞれ scalar weight3 を持つ。商へ普通のベクトル束として降りるのは Hom(L,W) である。P(E)\P(W) は分裂の torsor であり、一般の拡大だけから原点は選べない。一方、trace が定義される良い開では trace 零の中心直線が標準分裂を与える。ambient とその同定を固定した2-fiberと、ambient の同型類だけを固定して残る自己同型作用は異なる。この自己同型群の有限性は周囲の有限安定化子開に限り、拡大した pair stack の定義には課さない。

複数ブロックでは rank(E/W)=k。正しい形は P(E)\P(W)→P(E/W) 上の Hom(O(-1),W)-torsor。k≥2 では固定 ambient 上にも射影的な k−1 次元の方向が残る。一ブロックのアフィン空間だけの記述を流用しない。

### 相対双対で使う入力と降下の境界

`papers/sections/relative_duality.tex` は、最初に被約有限型 C-基底 R、純 active 代数 S の次数別有限射影性・各幾何学的ファイバーの二次 Koszul 3-CY 性、分裂した active PBW 同型を仮定する。その上で中心差 u_{α,L}−u_{α,R} の r 本の Koszul 解消を使い、Θ_{B/R}=B(N)[−N] を真正な双加群として構成する。各ファイバーの CY 性だけを相対同型へ外挿していない。

中心三次商の各次数の完全列は係数線型に分裂する必要がある。良い一ブロックの G+g は最高 active 記号の正則性と一定階数からこの条件を満たす。これらの入力を得た後は、任意の非平坦・非被約 R→T を許す。

全 twist RHom は a=j−i≥0 で A_a、−r<a<0 で0、a≤−r で A_{−a−r}^∨[−n]。compact generator は O(0),…,O(N−1) の直和で、compact 間の Hom は係数 perfect となる。Γ_A(A)^∨=A(−r)[N−1] を真正な双加群として求め、dg orbit 代数 A→Q への両側局所化から Q^∨=Q(−r)[N−2]、Serre 関手 S=(−r)[n] と trace を構成する。

相対 CY の規格化は表示チャート上のもの。全商 stack 上で orientation を自明化したという主張ではない。compact Hom の底変更、固定表示模型間の全 Abel 同値の fpqc 降下、一般の圏族の効果化は別問題である。前二者は固定模型で構成し、最後も良い一ブロック模型を局所的に持つ圏族に限定して効果化した。任意の intrinsic 成分の局所表示は未解決である。dg smoothness もこの計算からは結論していない。

### 固定模型の係数作用と全同値の降下

`papers/sections/abel_comparison.tex` では、任意の可換 R-代数 T に対し QGr(A⊗_R T) を QGr(A) 内の T-作用付き対象の圏として同定する。Gabriel の商関手と切断関手に係数作用を移し、torsion の核を確認する構成である。一般の Hom と tensor 積の可換性を仮定しない。

忠実平坦な T/R の降下対象は、係数作用の余作用と単位の差の核として回復する。完全・忠実な係数拡大と、対象・射の降下を使い、全同値とその逆同値を対象ごとに降下させる。任意の T-作用付き対象は自由 T-作用付き対象の反射的余等化子で表せる。自由対象間の任意の T-線型射も、R-線型射への自由係数拡大と T の乗法の合成に分解できるため、降下した関手の係数拡大が元の関手を回復する。

相対 Serre 関手から d=n−1 刻みの全 twist の orbit とその切断 Z-代数を復元し、中心 Veronese 復元を適用する。恒等関手の自然自己準同型環は R であり、O 上で恒等な自己同型は自明である。このため O の同定を付けた全同値の groupoid は離散で、fpqc 層 Isom_gr(A,A')/G_m に等しい。これは固定された良い表示模型間の全 Hom 比較を完成するが、任意の Abel 圏族がその模型から生じることや、全 Abel モジュライの代数性を与えるものではない。

### 大域持上げ線束と実現する三捩れ障害

指定した O-保存同値 F の次数付き持上げは G_m-torsor をなし、その線束 L_F は L_F^d≃R を満たす。対応する模型は A'_j≃A_j⊗L_F^j であり、F が大域の次数付き同型から来ることと L_F が自明であることは同値である。両方の次数一部分が階数 N の自由加群なら determinant から L_F^N≃R も従い、障害は Pic(R)[gcd(d,3)] に入る。従って、この自由性の仮定の下で n≠1 mod3 なら指定した全同値に大域の次数付き代表がある。

一つの Serre 比較を固定して得る Veronese 同型の持上げは μ_d-torsor であり、その Kummer 類と L_F の Picard 類は異なる。R=C[t,t⁻¹] 上で新次数 j に t^j を掛ける Veronese 同型は d 乗根を持たなくても、tails 上では恒等同値を与え、L_F は自明である。指定した Veronese 同型の持上げ不能を、元の同値の持上げ不能に置き換えない。

三捩れ障害は実際に生じる。R=C[s,t]/(t²−s³−1) と L=(s,t−1) に対し、L³=(t−1) であり、L は非主イデアルである。後者は、唯一の無限遠点で s,t の極位数が2,3なので、極位数1を持つ正則関数がないことから従う。Dedekind 環の Steinitz 分解を互いに素なイデアルと分裂完全列から証明すると、3|m のとき L の m 個の直和は自由となる。

全 n≥4、n≡1 mod3 に対し、定数の良い PBW 模型を次数 j ごとに L^j で捩じると、active 部分・中心部分・次数一全体がともに自由な新しい模型を得る。L³ の自明化が大域の三次 potential と中心三次商を与える。次数別 tensor による O-保存同値は L_F=L を持つので大域の次数付き同型に持ち上がらない。結論はこの**指定した同値**についてであり、二つの代数間のあらゆる次数付き同型が存在しないとは主張していない。

### 局所一ブロック型の対象効果化と Brauer 障害

族は R-linear Grothendieck Abel 圏と O の対で、係数変更を C_T=Mod_T(C) として持つものに限る。good 模型への局所同値は条件であって、全 intrinsic 圏族に対する局所表示定理ではない。全 O-Hom 比較により [Jgood/P̄] と同じ射の層を得る。対象は持上げ gerbe 上で degree j / weight j の加群を作り、その torsion Gabriel 商を取って効果化する。任意係数変更は係数作用として行い、右随伴と tensor の可換性を仮定しない。

表示 gerbe [Jgood/P]→Mloc の β∈H²(G_m) は、重み一の中心束（rank r）と active 商束（rank3）の determinant により rβ=3β=0。e=gcd(r,3)=1 では ar+3b=1 の character det(U)^a det(V/U)^b が中立化を与える。β=0 が意味するのは有限局所自由な次数一を持つ大域表示の存在であり、自由基底や中心直線の自明化ではない。

r=3m では、K=C(s,t) の cyclic division algebra (s,t)₃ の PGL₃-torsor を g↦diag(g^{⊕m},g) によって P̄ へ移す。twist した potential 空間は通常の affine vector space、中心三次族はその上の加法 torsor となる。任意の非空開の滑らかな像にK点を取り、さらにその fibre の非空 affine 開にK点を取ることで、全ての非空開上に β≠0 の対象を得る。個別の幾何点では β が零になることと矛盾しない。指定同値の Picard 障害とこの H² 障害を混同しない。

滑らかな出力を持つ pair の Msm=[Jsm/P̄] では、周囲単独の有限安定化子条件 Tfin を外す。Talg に残すのは相対 PBW・普遍低次数中心・Serre・全 O-Hom 比較の入力であり、Jsm では ε の同型性、相対点条件、H_w の滑らかさを要求する。全 Hom 比較と重み付き tails の効果化は周囲単独の有限性を使わない。pair の自己同型は滑らかな三次の射影自己同型群に入るので有限となる。以前の Poisson 射の定義域 MPois は Msm の非空開だが、H_w の滑らかさ等を課さない Mloc 全体をその開と同一視しない。

determinant による rβ=3β=0 はこの拡大後も有効である。n≢1 mod3 では中立化し、n≡1 mod3 では Msm の任意の非空開と稠密な MPois との交わりに前述の障害点があるため、位数は正確に3のまま残る（`cor:poisson-enlarged-brauer`）。

## 4. 相対点対応、中心復元、Poisson 射

### 点関手と正確な相対式

点は fpqc 局所的に正規化点加群 A→M の tails となる全射 O→P として定義する。全 O-同値の局所持上げから表示に依存せず、点対応が自己同型なので tails は初期点を復元する。普遍点商と shift は降下するが、圏全体の次数一 shift を大域に固定したわけではない。

C=V(F_x,F_y,F_z) は P(U*) への次数八の有限局所自由被覆である。可換代数 T=Sym(V)/(F_x,F_y,F_z) は Sym(U) 上階数八で有限局所自由、これが trace と norm の任意底変更を支える。D は中心三次直線 ℓ の相対 Cartier 切断であり、点スキームは E⊔D。完全交叉型は (2,2,2,3)、各 fibre の次元はn−3、次数は24である。

相対随伴では基底因子を保持する：

\[
\omega_{D/S}=O_D(7-n)\otimes p_D^*(\det V\otimes(\det Q)^{-1}\otimes\ell^{-1}).
\]

norm は O(24)⊗ℓ^(−8) の切断であり、f_*O_D の Fitting₀ を定める。被約像の方程式や射影先への双有理性を意味しない。n=4 の滑らかなDは種数37、n=7の各 fibre は双対化層自明だが、この数値だけから残余圏の模型とは同定しない。

ambient と中心射影の標的は Brauer–Severi 束となる。e=gcd(r,3)、ar+3b=e と選べば O(e)⊗(det U)^(-a)⊗(det(V/U))^(-b) が相対 ample 線束として降下する。ambient 上の O(1) 型線束の存在は β=0 と同値だが、これを D への制限について無条件に言い換えない。点空間 Y への引戻しでは普遍点の M₁ が重み一を持ち、gerbe は中立化される。A_j,M_j の双方を M₁^(−j) で捩じることができる。

### 点対応から中心三次商へ

Q=I(D)₂、U=I(E)₁、shift のグラフ Γ から H⁰(I_Γ(1,1))=R_B を得る。相対 Koszul 計算は I(D)₃/I(C)₃≃ℓ も任意底変更で与える。n=3では D が零次元でもこのイデアルの式は正しいが、全切断への制限写像の全射は不要である。

α:Z(B)₃→T₃ と ε:Z(B)₃/Sym³U→(J_g)₃ を使う。J_g=T/(U) は次数付き環の Artin 商であり、空である C∩V(U) への幾何的制限ではない。公刊EG §9のRains中心Ψに対して、Hesse形 g=(x³+y³+z³)/3+λxyz、δ=1−hλ/2 では

\[
[\Psi_{ab}]=-4h^4(1+\lambda^3)\delta^{-6}[xyz]
\ne0.
\]

従って ε が同型となる不変な非空開があり、αは普遍分裂単射となる。直線 I(D)₃/I(C)₃ の α による逆像が [w] を一意に与える。埋込み点対応は B だけでなく A=B/(w) を復元する。 r=1では、Cが八つの被約点なら一般の中心三次商のDは空となり、点対応は同じ楕円グラフのみになる。従ってr≥2という範囲は中心直線の復元にも本質的であり、LBSVの一点中心拡大の周囲二次関係の復元と区別する。

Q だけからの Casimir 空間の復元には M Hess(g) が対称ならMがscalarという追加条件を用いる。一方、尺度込み Π を既に回復した場合には追加条件は不要である。三つの偏微分の普遍Koszul cochainの完全性から、三次Casimirは任意の係数環で RF⊕Sym³U に一致する。

### Trace–Hessian 射とその限界

W=Sym³U、E=Z(B)₃、R_Π=RF⊕W とする。tr=Tr_{T/Sym(U)}/8 は純中心上で恒等なので、EとR_Πを W とtrace零の直線へ標準分裂する。尺度込み Π=ι_{dF}P は、Hessian縮約による ν_Π:R_Π/W≃(J_g)₃ を与える。局所的には ν_{hΠ_F}([F])=h²[det Hess(g)]。F→cF+G、P→c^(−1)P により縮約はc倍となるため、表示から独立である。

trace零の古典持上げを s_cl とすると、中心三次の同型は

\[
 d_\Pi(w)=-12s_{cl}\bigl(\nu_\Pi^{-1}\epsilon(\bar w)\bigr)+\operatorname{tr}(\alpha w).
\]

これは W 上で恒等であり、中心直線の torsor を同定する。滑らかな X_w=V(d_Π(w)) を与える非空開上で Poisson 対への射を得る。強い affine lift の一意性により、以下の PGL 商は三次 Poisson 対と偏極類そのものを表す。全 O-同値と任意底変更に両立するが、全 intrinsic 成分を覆うという主張は含まない。

単純な可換化による対応は成立しない。古典 R_Π の T₃ への像は (J_g)₃ で零なのに、非純中心の w の像は非零だからである。したがって D=C∩V(d_Π(w)) とはならない。この相違を消すのでなく、境界の非零類から古典方向の係数を読み取るのが上の構成である。

係数−12は指定Hessian jetに合う規約であり、同型の存在には任意の固定非零定数を使える。唯一の自然な逆量子化を証明したわけではない。固定入力の `papers/support/papers/sections/general_dimension_universal_quantization.tex`, `prop:pg-ad-intrinsic-hessian` は、短い中心元から純中心補正を引いた後のjetを扱う。この範囲では d_{hΠ_F}(Ωtilde)=F+O(h²) だが、有限hでの等式は一般に成立せず、指定の trace–Hessian 像に対する Ku 比較にも後述の障害がある。

### 強い affine lift と Poisson モジュライの逆構成

滑らかな相対三次 X=V(H)⊂P(V*)、n≥3 に対し、任意の bivector π∈H⁰(X,Λ²T_X) は、恒等式 ι(dH)Π=0 を多項式環で満たす一意な斉次二次 affine lift Π を持つ。この強い Casimir 条件は X 上だけの接条件より強い。相対 Euler 列の核 E∧L と勾配 Koszul 複体を用い、さらに一意な定数三重ベクトル P で Π=ι(dH)P と書けること、π の Jacobi 条件と Π の Jacobi 条件の同値を得る（`thm:poisson-strong-lift`）。証明は任意の非平坦・非被約係数変更と両立する。

三次方程式の直線を L_H とすれば、全 bivector の相対束は L_H⊗Λ³V* である。H→cH には P→c⁻¹P が対応する。非零分解可能条件は Plücker 方程式を満たす非零錐の条件として課し、幾何ファイバーでの分解可能性だけで代用しない。このとき support K⊂V* は階数3の部分束、U=ann(K) は一次 Poisson 中心として回復する。

Pdec は、滑らかな三次式の空間と Gr(3,V*) の積上の L_H⊗det K の零切断を除き、PGL(V) で割った stack である。その good 開上で

\[
 B_\Pi=T(V)/\bigl(a\otimes b-b\otimes a-\operatorname{sym}\Pi(a,b)\bigr),
 \qquad [w]=d_\Pi^{-1}([H])
\]

を構成すると、量子側との相互逆を得る。必要な条件は Talg の入力、ε の同型性、[w] の良い相対点条件である。active 切断 H|P(K) の滑らかさは Talg の仮定から取り、H 全体の滑らかさだけから推論しない。Msm≃Pgood⊂Pdec は全自己同型を含む fpqc stack の同型で、滑らか・既約・DM、次元は binom(n+2,3)+3n−2 となる（`thm:poisson-good-open-isomorphism`）。

一般三次の非零 Jacobi スキームが非零 Grassmann 錐に等しいという既存分類を用いる開上では、全非零 Poisson moduli への開埋込みとなる（`cor:poisson-generic-open-immersion`）。一般ファイバーの既約性から、三次 moduli を支配する Poisson 成分は一つである。特殊三次上にのみある成分は除外しない。全滑らかな三次の上で分解可能 locus が自動的に開になるわけではなく、この結果を全 intrinsic O-marked 圏成分の分類とも同一視しない。

### 有限パラメータでの比較に使える厳密例

F=(x³+y³+z³)/3+Axy+Byz+Czx+Dx+Ey+Hz+G とし、A,B,Cは任意個の中心変数の一次式、D,E,Hは二次式、Gは三次式とする。入力論文Aの `hesse_mixed_universal_center.tex`, `cor:pg-hesse-hessian-form` の短い中心元をΩ、純中心補正h²ABC/6を引いたものをΩtildeとすると、同入力の中心性を仮定した上で、現行のtrace計算は

\[
 d_{h\Pi_F}(\Omega)=F+\frac76h^2ABC-\frac{h^4}{18}(AH+BD+CE),
\qquad
 d_{h\Pi_F}(\widetilde\Omega)=F+h^2ABC-\frac{h^4}{18}(AH+BD+CE)
\]

を与える。これは新しい特定次元の実験ではなく、六つの混合係数を独立記号に保つ恒等式である。証明の要点は、x²=−Ay−Cz−D 等で定まる八次自由代数の平方自由単項式基底について tr(x)=tr(y)=tr(z)=0、tr(det Hess(F))=−12ABC を計算すること。`computations/verify_center_hessian.py` はEGの係数証明書とこのtraceを厳密に再現する。入力中心元の非可換中心性そのものの再検証ではない。

この補正は一般に座標変換で消えない。全 n≥3 に対し m=n−2 と置くと、

\[
 F_t=\frac{x^3+y^3+z^3+u^3+\sum_{a=1}^{m}v_a^3}{3}
       +tu(xy+yz+zx)
\]

は (1+12t³)(1+2t³+5t⁶)≠0 のとき滑らかで、t≠0 なら [u³]≠0∈(J_{F_t})₃ である。後者は Jacobi イデアルを消す明示汎関数により全 n で証明した。t=1 は共通の滑らかな例であり、

\[
 d_{h\Pi_{F_t}}(\widetilde\Omega_{t,h})=F_t+h^2t^3u^3
\]

は入力の中心公式の下での厳密等式となる。従ってこの出力は h³ を法として既に入力 X_t の定数族と同型でない。H⁰(T_{X_t})=0 と非零 KS 類を使い、特殊ファイバー上の同型を定数自己同型で調整することで、標識を外した形式同型も排除する（`prop:trace-uniform-jacobi-class`, `prop:trace-nonconstant-classical-family`）。

一般混合 Hesse 係数でも K₂(F)=−tr(det Hess_active F)/12 の Jacobi 類は正則切断であり、上の例から非零となる非空開を得る（`cor:trace-generic-geometric-correction`）。これは**入力の定数三次と trace–Hessian 出力**の比較である。残余復元との相違と Ku 非同値は第6節の別の議論を要する。また出力の式が h=0 まで延長することは、中心次元が跳ぶ可換特殊点全体への moduli 射の延長を意味しない。

## 5. Jacobi スキームの構造と計算証明書

R_N=C[p_ijk]、P∈Λ³W、H_r=(F_ijr)。I_F は次の N binom(N,4) 本の二次式で生成する：

`Σ_ij T_ijr (p_abi p_cdj + p_bci p_adj + p_cai p_bdj)`、`a<b<c<d`。

p の添字は交代符号で増加順に直し、重複添字は零とする。証明書の対称整数テンソル T は F_T=(1/6)Σ_ordered T_ijr z_i z_j z_r を定める。行番号は (r,a,b,c,d) の辞書順、列番号は辞書順の Plücker 変数の非順序二次単項式、全て0始まり。

| N | n | 方程式数 | Plücker 二次空間 | 証明した一般階数 | 非零小行列式 mod 32003 |
|---:|---:|---:|---:|---:|---:|
| 5 | 3 | 25 | 5 | 5 | 15512 |
| 6 | 4 | 90 | 35 | 35 | 14374 |
| 7 | 5 | 245 | 140 | 140 | 7973 |
| 8 | 6 | 560 | 420 | 420 | 508 |
| 9 | 7 | 1134 | 1050 | 1050 | 13073 |
| 10 | 8 | 2100 | 2310 | 1980 | 16095 |

入力 T、行・列番号、行列式が `computations/jacobi_rank_certificate.json` にある。生成コードは rank 探索、検証コードは記録された平方小行列だけの直接行列式を別関数で計算する。N=10 の探索では非標準 Plücker 単項式の列へ制限して高速化するが、証明書は元の全行列の列番号を記録し、検証もその全行列から小行列を作る。NumPy int64 の各積はこの法では約10^9以下であり、浮動小数点を用いない。

この非零整数小行列により特性零の非空開を得る。選んだ有限体テンソル自体の滑らかさを証明する必要はない。全三次係数空間が既約なので、この開は滑らかな三次の開と交わる。

### 普遍関係・Koszul flattening・apolar Betti 数

対称性から Σ_r B_{H_r}(P)_{rabc}=0 が恒等的に成り立つ。Λ³W*→W⊗Λ⁴W*、β↦Σe_r⊗(dz_r∧β) は縮約を N−3 で割ることで分裂するので、binom(N,3) 個の独立な従属関係を与える。全三次テンソルに共通する核もこの像に等しいことを、T=ℓ³ によって証明した（`lem:nfold-universal-row-relations`）。

従って a_N=N binom(N,4)−binom(N,3) が階数上界であり、次数二の差は ε_N=5binom(N+1,6)−a_N 以上となる。この上界は既知の Koszul flattening の階数上界に対応する。V=W* とすると、係数写像は K_T:W⊗Λ⁴V→V⊗Λ⁵V と、ρ(λ⊗η)(P)=η((ι_λP)∧P) によって Φ_T=(1/2)ρK_T と書ける。ρ は外積写像の核を Plücker 二次関係空間へ同型に写す。係数1/2は標数零の規約であり、法2の証明書ではこの式を還元せず、元の整数係数 Jacobi 式を使う。

一次偏微分が独立なら、別の多項式環 S=Sym W 上の apolar 代数 G_F=S/Ann(F) の Hilbert 関数は (1,N,N,1) である。β_{i,j}=dim Tor_i^S(G_F,C)_j とすると、内部次数 N−3 の Koszul 複体に det(W*) を掛けて外積双対を取ることにより、

- dim(ker Φ_T/im ι)=β_{4,6}、
- dim((J_N)_2/(I_F)_2)=β_{5,6}=ε_N+β_{4,6}

を得る（`lem:nfold-apolar-betti`）。前者に対応する Tor の位置は (N−4,N−3)、後者は (N−5,N−3) であり、socle 次数三の Gorenstein 双対性で上の添字となる。

Boij（1999, Remark 6, pp.163–164）の N=9,10 の **total** Betti 数から β_{4,6}=0 が従う。実際、`c_N = [t⁵]((1+Nt+Nt²+t³)(1−t)^N)`、b₄=Σ_jβ_{4,j} とすると b₄−c_N=β_{3,5}+β_{4,6} であり、同論文の例では (c_N,b₄)=(288,288),(693,693) となる。従って N=9,10 の最大階数、N=10 の二次の差330は、既存の apolar Betti 計算から既に従う数値である。保存した整数小行列証明書は、これらを Jacobi 方程式から直接再現する独立した証明として保持する。

N≥11 の一般核の一様な記述は未決定である。必要な問題は一般三次について β_{4,6}=0 を示すことであり、剰余体の G_F 上の分解に関する Koszul 性だけでは解決しない。「全テンソルに共通する核」と「一般の一つのテンソルの核」、G_F 上と S 上の二つの分解を混同しない。

### n=8 の全 Hilbert 関数、socle、非分裂性

N=10、E=(R_N)_1、D_F=(J_N)_2/(I_F)_2 と置く。Plücker イデアルの線形 syzygy 空間 K_N=ker(E⊗(J_N)_2→(J_N)_3) から完全列 K_N→E⊗D_F→(J_N/I_F)_3→0 を得る。二次階数が1980なら dim E=120、dim D_F=330、dim(E⊗D_F)=39600 である。標準単項式から dim(R_N/J_N)_3=108900、dim(J_N)_3=186340、dim K_N=90860 を得る。

`computations/jacobi_vertex_certificate.json` は対称整数テンソル T と、法2で得た 90860×39600 の縮約行列の39600行を記録する。この正方小行列は行列式1を持ち、K_N→E⊗D_F の全射性を証明する。`computations/verify_jacobi_vertex.py` は Plücker 二次関係・元の Jacobi 多項式・三次積の像と核を再生成し、`computations/verify_binary_minor.cpp` は探索と逆向きの pivot による通常の Gaussian 消去で保存済み小行列を独立に検証する。具体的な実行結果と検証範囲は `notes/validation.md` を参照する。

標数零への移行では、有限体上の syzygy ベクトル自体を持ち上げない。法2の全射性を、**元の整数係数 Jacobi 二次式の一次倍を並べた行列**の階数186340という下界へ戻す。二次行列にも階数1980の下界があり、標数零の普遍的な上界と合わせることで両方の等号が従う。非零整数小行列により複素三次係数空間の非空開を得る。T(z,z,z)/6 を標数二の三次式とみなす必要はない。

J_N/I_F は次数二で生成されるため、次数三の消滅は全ての次数三以上の消滅を意味する。この開集合上では

`J₁₀/I_F ≃ C(−2)^330`、`m₀(J₁₀/I_F)=0`、`(J₁₀/I_F)²=0`、`H_(R/I)(t)=H_(R/J)(t)+330t²`

となり、√I_F=I_F^sat=J₁₀ も従う。R/J₁₀ が正次元整域なので、この長さ330の核が頂点の局所環の socle 全体に等しい。この結果は入力論文Aの被約分類にも F の滑らかさにも依存せず、必要なら得た非空開を滑らかな三次の開と交わらせられる。相対版では次数二の差が階数330の局所自由加群となり、任意底変更後にも同じ消滅式が成り立つ。

平方零拡大 0→C(−2)^330→R/I_F→R/J₁₀→0 は次数付き代数としても、頂点の完備局所 C-代数としても分裂しない。局所切断があれば一次座標の持上げは p_s+u_s（u_s は核）となるが、極大イデアルが核を消すので、二次 Plücker 関係の値を変えられない。従って J₂\I₂ の非零像を消すことはできない。この拡大を自明な平方零拡大と同一視しない。

明示的な一次分解は I_F=J₁₀∩Q、Q=I_F+m₀³ で与えられる（`cor:nfold-vertex-primary`）。Q は m₀-primary で、R/Q の Hilbert 関数は (1,120,5280)、長さは5401である。**330は冪零根基 J₁₀/I_F の長さであり、この埋込み primary 成分の長さではない。**

### 非零点と頂点の構造

滑らかな F、P∈Λ³A に対して K_{F,A}={w:T_F(A,w,W)=0} と置く。A∩K=0 は滑らかさから従い、法接空間は Λ³K となる。dimK≤2 と、非零点 P の近傍で I_F=J_N となることが同値（`thm:nfold-normal-tangent`）。独立に、三次元部分空間対の incidence によって、横断性を失う滑らかな三次は係数空間の余次元少なくとも3Nの閉集合に入ることも示した（N≥6）。

既存入力 √I_F=J_N の下で dimK≥3 なら、K 内の分解可能な Q を取り P+tQ という非分解可能解ができるため矛盾する。従って一般の全非零 Poisson スキームは Grassmann 錐非零部に等しく、Proj(R/I)=Gr(3,N)、I_F^sat=J_N となる。この等式は係数開上で相対的にも成立し、任意底変更と両立する。n=8 では前項の証明書が、被約分類を使わずにこれらの結論を与える。

冪零根基 N_F=J_N/I_F は有限長で、H⁰_{m0}(R/I)=N_F。n≥8 では Ass(R/I)={J_N,m0}、頂点の深さは零である。したがって一般 F の非被約性は零構造に集中する埋込み成分である。n=8 の二乗零性は前項で確定しているが、一般次元の次数二の元が冪零であることだけから二乗零性は従わない。

### 横断切片、直和の retraction、特殊三次の非零冪零元

滑らかな F と P=e₁₂₃∈Λ³A に対し、K=K_{F,A} を含む補空間 B を選ぶ。横断アフィン空間 S_P=P+(A⊗Λ²B)⊕Λ³B と Jacobi スキームとの交叉は、P の開近傍で γ↦P+γ により Z_F∩Λ³K と同型になる（`thm:nfold-transverse-slice`）。これは接空間だけの同定ではない。(2A,2B) 成分の方程式は D(q)+E(β)=0 で E は β の二次式に限られるため、D の左逆を用いて β+M(β)β=0 を得る。det(1+M) を可逆にすると β=0 が従い、残りの線型式が γ∈Λ³K、残りの二次式が上記の交叉を与える。

この polar Jacobi スキームは T_F(−,−,v)|_(K×K) の **全ての v∈W** に対する式を課す。一般には F|K の Jacobi スキームではない。また横断切片の同定から局所環全体と Grassmann 方向との直積表示は結論しない。Fermat 三次の座標部分空間と近くの一般部分空間では dim K が跳ぶため、そのような一様な積表示を仮定できない。

dim K=N−3 という最大法接空間の条件は、W=A⊕K に沿う Thom–Sebastiani 分解 F=G(A)+H(K) と同値である。この場合には横断切片が H の Jacobi スキームになる（`prop:nfold-maximal-normal-ts`）。Thom–Sebastiani 分解と Hessian/apolar 積の既存の幾何については Bricalli–Favale–Pirola を参照する。

任意の直和 F=G(A)+H(B) に対し、純三重ベクトル成分への射影 ρ:Z_F→Z_G×Z_H と和による切断 σ を構成でき、ρσ=id となる（`prop:nfold-ts-retract`）。一ブロックに属する polar 方向と四重添字の方程式が射影を正当化し、直和の mixed Hessian が零であることが切断を正当化する。任意の非被約係数について成立するスキームの retraction であり、Z_F 全体の直積表示ではない。

全 n≥11 に対し W=A₃⊕B₁₀⊕C_(n−11)、F=G(A)+H(B)+Σc_i³ と取る。G は滑らかな ternary cubic、H は上の N=10 証明書の開集合に属する滑らかな三次とする。勾配の直和から F も滑らかである。非零 P_A∈Λ³A を固定すると、Z_H の頂点局所環は Z_F の P_A における局所環の retract となる。従って330次元の平方零イデアルが、任意の二元の積が零である冪零部分空間として後者へ分裂単射し、m²/m³ にも330個の独立な類を与える。

射影座標 t=p₁₂₃≠0 の chart では [P]↦pr_B(P)/t と Q↦[P_A+Q] が同じ retraction を与えるので、射影 Jacobi スキームも非被約である。この構成は既存の一般三次の被約分類に依存しない。横断切片だけの非被約性から周囲の非被約性を推論せず、retraction の単射を使うことが重要である。周囲の冪零根基全体の二乗零性や有限長性、n=11 が最小の可能次元であることは主張していない。

### 高次数と必要時の計算の入口

`prop:nfold-higher-nilradical` は、Grassmann 環の Hilbert 関数と R_{d−2}⊗I_2→I_d の全射から、各次数の差に明示的な下界 L_{N,d} を与える。N≥13 では L_{N,3}>0、N=13 では179179。固定した任意の d≥2 に対しても、N が十分大きければ L_{N,d}>0 となる。

従って有限長冪零根基の最高次数・最高 socle 次数は次元によらず有界でない。N_F が次数二で生成されるので、次数 d に非零部分があれば m₀^(d−2)N_F≠0 となり、m₀ による最小消滅指数も非有界である。一方 N_F 自身の積による冪零指数は、n=8 の二乗零という確定結果を除き未決定である。

一般次元の補助課題として、一般 apolar 代数の β_{4,6} と、K_N→E⊗D_F の余核がどのように変わるかが残る。個別の N=11,12 の計算や N≥13 の高次数 Hilbert 関数は、一般 O-marked moduli・Poisson 射の構成に対する具体的な障害を判定する必要が生じたときに着手する。現行の多重次数別 syzygy 計算を再利用できるが、次元を順番に増やすことを既定の研究方針にしない。二次階数の最大性と Jacobi イデアルの高次数構造・冪零根基の積は別問題である。

特殊 cubic では n≥4 から非分解可能解がある。F=Σz_i³、P=e_123+e_456 は独立な二つの Jacobian 括弧の和で一般階数4。従って「全滑らかな三次で Grassmann 錐」という主張は、n=4 から既に複素点の集合として偽である。

## 6. 残余圏の認識と Poisson 射の比較

### 三つの異なる次元区分

既知の sector 公式は HH^q(Ku X) = (J_F)_(3q/2)（q偶数のみ）に、3|N かつ q=N/3 のとき C² を加える。HH^1=0、HH^2 は n=4 だけ二方向多い。HH^3 は n=7 だけ C² となる。

| n | dim H¹(T_X) | dim HH²(Ku X) | HH³(Ku X) | Serre |
|---:|---:|---:|---|---|
| 3 | 10 | 10 | 0 | R[1] |
| 4 | 20 | 22 | 0 | [2] |
| 5 | 35 | 35 | 0 | R⁻¹[3] |
| 6 | 56 | 56 | 0 | R[2] |
| 7 | 84 | 84 | C² | [3] |
| 8 | 120 | 120 | 0 | R⁻¹[4] |

形式認識は「滑らかな幾何的源＋実際の自然変換＋接同型」の補題を使う。極小 L∞ 模型の MC 方程式 Q(x) に対し、x=f(t) の可逆な線型項と Q(f(t))=0 が全次数で成立すれば Q=0。HH³=0 を前提にしない。この補題は全 L∞ 演算の消滅を意味しない。

actual compact category deformation→formal hull は tame 条件で (−1)-truncated。幾何的模型が hull の全 π0 を既に覆うことと組み合わせる。全高次 groupoid の同値は主張せず、HH^0=C に由来する scalar π2 は残る。

四次元は幾何的20方向と hull22方向の区別。指定された中心三次族が幾何 locus に入らないことは、この次元比較だけでは証明できない。

rotation は n=3q で R=S[-q]、n=3q+2 で R=S⁻¹[q+2]、n=3q+1 では S=[q+1]。中段の Calabi–Yau 型で R を Serre と shift の積にすることは、R³=[2] と proper 性に反する。ほかの不変量からの復元を否定していない。

BFK の任意非零 M による M⊕RM⊕R²M の生成を使えば、rotation±1 に安定な非零 thick 部分圏は全体。n≠1 mod3 では Serre 安定でもよい。四次元で Pfaffian cubic の Ku≃Db(K3) を取ると、一点支持複体は非零で真の thick 部分圏かつ Serre=[2] 安定であり、仮定の必要性が分かる。

### 残余復元が保持するデータと低積による比較

固定入力の完備 MF 移送が選ぶ potential は W=C_π^(-1)φ(w) である（`eq:nfm-formality-central-inverse`）。π は formality の formal Poisson tensor であり、量子代数の二次交換関係から直接得る affine Π と同一とは限らない。指定三次周期は双次数 (2,−3) の周期変数を固定して保持する。potential の単元倍を行う場合には、内部 shift だけでなく周期の規格化も追跡する。

既に滑らかな可換模型の幾何学的存在が分かっている rotation 付き dg pair (K,ρ) では、低積の核 Q_ρ=ker(Sym²V_ρ→U_ρ) を計算し、指定三次 H の勾配空間と線型同型で一致するかを判定すればよい（`prop:nfm-residual-low-product-test`）。これは既存模型の三次を同定する判定であり、低積の次元や可積分性だけから模型の存在や圏同値を構成する定理ではない。方程式の定義体、同値核の有限拡大、必要な三乗根による周期調整を分ける。

### 全次元の split Hesse 族における厳密な不一致

R=C[h]_(h)、K=C(h) とし、active 代数 D_R を

\[
 [y,z]=hx^2+\frac{h^2}{2}(yz+zy)
\]

とその巡回式で定め、B_R=D_R[u₁,…,u_r]、r=n−1 とする。G=Σu_i³/3、F₀=(x³+y³+z³)/3+G と置く。固定入力の中心三次 w_h と PBW 性の検証は active な三変数内で完結し、中心変数の付加により全 n≥3 の量子族を与える。その上で固定入力の全次元の残余復元と明示 Hesse 公式を適用する。w_h の係数と厳密な式は `papers/sections/residual_comparison.tex` の split Hesse 族に収めた。

この族では尺度付き周囲 tensor は Π=hΠ_{g_h}、g_h=(x³+y³+z³)/3+hxyz であり、

\[
 H_h^{\mathrm{TH}}=F_0+hxyz,\qquad
 H_h^{\mathrm{res}}=F_0+\lambda_{\mathrm{res}}(h)xyz,\qquad
 \lambda_{\mathrm{res}}(h)
   =\frac{h+h^2/3+h^5/12}{1-h^4/4}.
\]

第一式は trace と境界 Jacobi 線から得る厳密計算（`prop:nfm-th-hesse-exact`）、第二式は固定入力の残余 potential の結果（`prop:nfm-residual-hesse-input`）である。差の二次係数は [xyz]/3∈(J_{F₀})₃ で非零なので、特殊ファイバー上恒等の形式同型は h³ を法として既に存在しない。

一般ファイバーの非同型は、別に有理不変量を使って証明する。Hesse 平面三次の

\[
 j(\lambda)=\frac{27\lambda^3(8-\lambda^3)^3}{(1+\lambda^3)^3},
 \qquad
 j(\lambda_{\mathrm{res}}(h))-j(h)
 =13824h^4+4608h^5+512h^6+O(h^7)
\]

は一致しない。対称三重形式の symmetrizer はこの族で K·Id₃×K^r となり、唯一の階数3の原始冪等元が active 部分を復元する。従って全三次の射影同型も active 平面三次の同型を強制し、代数閉包上でも X_TH と X_res は射影同型でない（`thm:nfm-th-residual-obstruction`）。

固定入力による K_A≃Ku(X_res) と rotation を保つ復元を用いると、K_A と Ku(X_TH) の間に rotation 保存 dg Morita 同値は存在しない。n≢1 mod3 では rotation が Serre と shift から回復されるため、rotation の標識を外した dg Morita 同値も存在しない。n≡1 mod3 の unmarked 同値の不存在をこの議論から結論しない。

さらに、同じ Π の滑らかな三次 Casimir は H=cg_h+G'(u)、c≠0 と書ける。滑らかさは対応する三重形式の第一引数についての非退化性を与え、centroid E(H)=K×E(G') の active 射影は階数3の原始冪等元となる。三つの slot 間で作用を移すと centroid は可換代数となるため、この原始性は G' がさらに分解する場合にも保持される。X_res の唯一の階数3の原始冪等元と比較すれば同じ j 不一致が生じる。従って**純中心三次の選択や trace–Hessian の非零数値規格化だけでは、固定 Π に対する比較を修復できない**（`cor:nfm-casimir-selection-obstruction`）。

この split 族の B 単独は正次元の安定化子を持ち、周囲の有限安定化子開 Tfin に入らない。一方、相対点条件は w_ab の乗法の determinant が G⁸≠0 であることから満たされる。一般点の楕円平行移動は、原点へ特殊化する非定数形式切断と標数零形式群の性質から無限位数である。固定入力の PBW・中心・相対双対を適用する範囲で、拡大した Msm の良い pair として扱える。定常成分 D 自体の滑らかさは必要としない。この例だけを根拠に、Tfin の一般対象で unmarked 非同値を主張しない。

### 一般混合 Hesse 係数での二次 jet

F=g_λ+Axy+Byz+Czx+Dx+Ey+Hz+G とし、A,B,C∈U、D,E,H∈Sym²U、G∈Sym³U、F と g_λ は滑らかとする。Δ_F=det Hess_{x,y,z}(F)、τ_F=Tr_{T_F/Sym U}/8 と書く。量子交換関係を hΠ_F、中心元を固定入力の規格化

\[
 \widetilde\Omega_{F,h}
 =\operatorname{sym}\bigl(F-h^2\Delta_F/12+h^4\Psi_\lambda(F)\bigr)
\]

とする。harmonic-angle formality と、内部次数を保ち次数一生成元を固定する厳密同型 φ を選ぶ条件の下で、

\[
 \begin{aligned}
 W^{\mathrm{res}}&=F+\frac{h^2}{24}\Delta_F+O(h^3),\\
 H^{\mathrm{TH}}&=F-\frac{h^2}{12}\tau_F(\Delta_F)
                       +h^4\tau_F(\Psi_\lambda(F)),\\
 D_2(F)&=\left[\frac{\Delta_F}{24}
                    +\frac{\tau_F(\Delta_F)}{12}\right]\in(J_F)_3
 \end{aligned}
\]

を得る（`prop:nfm-relative-residual-second-jet`）。三変数縮約の普遍恒等式 Θ=−2 adj(Hess_active F) と Dito の二次星積から ρ₂F=Δ_F/8、同じ harmonic-angle formality の Shoikhet の wheel 消滅から中心写像 C_π=1+O(h³) を得ることが、係数 1/24 の根拠である。trace 側では固定入力の h⁴ 境界項が λ(8−λ³)g_λ/48 であり、境界 Jacobi 環で零になるため、ν が h² を含んでも非純中心方向の倍率は厳密に一となる。一般の O(h⁴) という jet のみからこの倍率を推論していない。

Fermat 点 F_*=(x³+y³+z³+Σu_i³)/3 では Δ_{F_*}=8xyz、τ_{F_*}(Δ_{F_*})=0、D₂(F_*)=[xyz]/3≠0 である。D₂ は全混合係数の Jacobi 束の正則切断なので、各 n≥3 の既約係数空間に非空な非消滅開を与え、良い一ブロック入力の開とも交わる。任意係数変更と両立するのは、この有限式と Jacobi 類の形成である。この二次 jet 計算だけから全次数の formality/MF 移送を得たという主張ではない。後述の正規化再帰により普遍 PBW 模型からの形式 Poisson 構成は任意基底変更へ移せるが、完備 MF 同値自体の任意基底版は別の入力である。

非消滅開と中心量子化・次数別 PBW・指定 formality の入力が成立する開との交差の複素点では、W_res と H_TH の族は同じ底 h と特殊ファイバーの同定を保つ形式同型を持たない。さらに固定入力の完備 MF 移送・相対 window 同定を適用すれば、実際の幾何的 KS 写像 η_F:(J_F)₃→HH²(Ku X_F) の単射性と HH¹=0 により、同じ h を固定し特殊ファイバー上恒等となる C[[h]]-線型 dg Morita 同値も存在しない（`cor:nfm-generic-marked-comparison-obstruction`）。この部分は n=4 でも成立し、全 Artin 形式認識の全射性を必要としない。ただし、一般混合係数の一般ファイバーにおける **unmarked** な Ku 非同値は、この二次 jet だけからは結論しない。

### 代数的 Hessian–trace 補正と点曲線

Poisson 対 (H,P)、K=supp(P)、U=ann(K) に対して、T=Sym(V)/(∂_kH:k∈K) は Sym(U) 上の八次有限局所自由代数である。正規化 trace τ=Tr/8 と D_P(H)=〈det(D_K²H),P⊗P〉から、H♯=H+D_P(H)/24+τ(D_P(H))/12 を定める。この定義は補空間を選ばず、(H,P)→(cH,c⁻¹P) と全線型座標変更に共変で、任意底変更に両立する（`thm:nfm-algebraic-hessian-correction`）。滑らかな出力の非空開で Φ を得て、Msm≃Pgood を介し全 O-同値に降下する。

support K を保持して P=0 を許すと、補正は線束方向の二次以上で、零切断上の微分は恒等。従って Φ は支配的で非空開上 étale、flag 付き零切断の形式完備化では自己同型である。これは零 tensor のとき K を忘れたモジュライの形式自己同型や、大域的な有理同型ではない。

trace は純中心なので H♯|K=g+D_P(g)/24、Π♯=Π+ι(dD_P(H))P/24 となる。三変数の双線型化行列 C(p)−t Hess(g)/2 の行列式が −3t(g+t²Hess(g)/24) であることから、H♯|K は元の楕円点曲線と一致する。これは Mori–Smith の既知の点曲線公式を本稿の規約で使ったもの。左右の kernel line による相対証明を本文に置く（`prop:nfm-correction-point-cubic`）。曲線の一致だけで shift 付き対応全体や定常成分 D の同定を結論しない。

Hessian 正規化中心元では、H_TH−F は純中心だから active gradient・Hessian・trace は変わらない。厳密に H♯=F+h²Hess_active(F)/24+h⁴τ_F(Ψ_λ(F))、Π♯=hΠ_F+h³Π_Hess/24 となる。偶奇性により W_res との一致は mod h⁴ である。ここから全次数の Ku 比較はまだ従わない。

### 固定 formality の全次数の補正

Kontsevich の affine-equivariant harmonic-angle formality を固定する。生成元固定模型で、二つの formal tensor の最初の差 h^mD は交換子の h^m 係数に現れるが、二次関係右辺の差にはさらに h が掛かる。この一意性により係数を有限 graph の再帰で得る（`lem:nfm-normalized-star-model`）。形式二次対応そのものは Kontsevich 2001 Proposition 6 の既知結果である。

被約有限型の普遍 PBW 係数模型では各係数が正則となり、全閉点での存在から MC 恒等式を証明した後、非被約・非平坦を含む任意基底へ移せる。中心一次関数を入力するグラフと単位正規化を調べると、π_h は U を全次数で消し、星積は Sym(U)-線型、C_π は純中心関数を固定する。active gradient の Koszul 完全性と内部次数から π_h=a_hι(dW_h)P、a_h∈hR[[h]]、a_h/h は単元となる。滑らかな Poisson 対の主張には全 F の滑らかさも要る。active 平面三次だけ滑らかでも、中心変数に依存しない F は cone となる。

π_h は B_h だけから決まり、中心逆像は Z(B_h)₃≃R[[h]]W_h⊕Sym³U[[h]] を与える。従って中心元の単元倍・純中心加算に自然である（`cor:nfm-formal-center-casimir`）。これは h 進形式中心であり、有限 Artin 切断の余分な h-torsion 中心と区別する。

指定した中心正規化では c₂=0 を証明した（`prop:nfm-third-tensor-scalar-zero`）。普遍係数環で π₃−Π_Hess/24 は多項式共変式、Π_g の係数ベクトルは primitive なので比例スカラーの分母を除ける。そのスカラーは次数二の SL₃不変式であり、対角重みと二つのせん断で零となる。混合係数への移行は U=0 制限と active 微分の可換性、相対 gradient Koszul の単射性を使い、非被約基底にも普遍恒等式から適用する。

上半平面の反射で harmonic-angle 形式の符号を追うと、星積は反対積へ移り、関数上の中心写像 Cπ は π→−π で不変となる。生成元固定模型の一意性から π_-h=−π_h、Weyl 対称化の像は偶数、偶数の Weyl symbol を持つ指定中心元の W_h も偶数である。従って a_h=h+O(h⁵)、W_h=F+h²Hess/24+h⁴W₄+O(h⁶)、π_h=hΠ_F+h³Π_Hess/24+O(h⁵)（`cor:nfm-mixed-even-jet`）。任意の formality や h依存の二次関係へ同じ偶奇性を無条件に移さない。

純 active 三次 g では、π_m の volume 双対一次形式が閉じているので Euler 積分により次数m・order3の三次共変式になる。m=5の重複度は Weyl 交代和 41−35−30+23+21−19=1。四次不変式 S を S(xyz)=1 と規格化し、Lindberg–Pym の原生成元の量子トーラス交換比を用いると π_h(xyz)=log((1+h/2)/(1−h/2))Π_xyz であり、π₅(g)=S(g)Π_g/80 を得る（`prop:nfm-active-fifth-covariant`）。S(g_λ)=λ(λ³−8)。混合係数も U=0 に制限すると同じ式になるため、S(g)≠0 の稠密開で有限 Hessian tensor 補正との五次係数は異なる（`cor:nfm-fifth-restriction-obstruction`）。これは tensor の尺度を固定した相違であり、W₄や Ku の非同値の判定ではない。

固定 formality の形式表示 groupoid 上の降下と、有限 h の代数的 moduli 射・formality 独立性・全 intrinsic O-降下は別である。完備 MF/window 比較そのものは固定入力を適用する条件付きの結論である。

### split 族での全次数比較と尺度

任意の固定 λ∈C、1+λ³≠0 と量子化尺度 s を分け、g_λ=(x³+y³+z³)/3+λxyz、H_TH=g_λ+G(U) とする。Φ が与える Hcorr=J+G は、J=g_λ+s²Hess(g_λ)/24=A g_ν、A=1−s²λ²/4、ν=[λ+s²(4+λ³)/12]/A である。

固定入力Bの完備 MF・相対 window・固定標的への有限降下・coherent 飽和性の下で、全 n≥3 に対し K_A≃Ku(V(Hcorr)) をある有限拡大 C(s)⊂K′上で得る（`thm:nfm-split-corrected-residual`）。Heisenberg 同変性は生成元固定模型の一意性から従う。active quotient の楕円曲線比較には、原点のある楕円曲線の導来同値から同型を得る AKW Theorem 2.2 を使う。復元係数 μ と点曲線係数 ν はともに λ+(1+λ³)s²/3+… で始まるため、j の分岐点でも同じ形式分枝を選び μ=ν となる。単なる一パラメータ式への代入ではない。

形式 active 係数 a(s) を代数的 A へ移す座標変換 (A/a)^(1/3) と、既に代数的な標的への同値核の有限降下を分ける。形式座標変換自体の代数化は使わない。Hcorr を g_ν+G へ規格化すると tensor は sAΠ_gν となり、sΠ_gν ではない。指定三次周期は potential を厳密に移す座標変換で保持する。

### 一般次数9と framed 被覆の分岐

support と体積を局所的に固定すると、補正は F↦F+Hess_active(F)/24+τ_F(Hess_active(F))/12 である。active 三次の写像を φ₃ とし、g_(p,q)=pΣx_i³/3+qxyz を使うと ψ(p,q)=(p(1−q²/4),q+p³/3+q³/12)。これは基点のない三次式による P²自己射へ延長し、有限平坦階数9となる。SL₃×A²→Sym³(C³)* の微分が Fermat 点で同型になることと同変性から、一般次数の乗法性で φ₃の次数も9と分かる。Hesse frame の有限同定の個数は不要である。

Fをactive次数でf₃+f₂+f₁+f₀に分けると、f₂の像はL_f₃ f₂、f₁とf₀の像はそれぞれ既知項を加える平行移動である。Hesse表示では det L=(1+(8p³q−q⁴)/144)³、最後のtraceはf₀に依存しない。従ってactive逆像ごとに全混合係数を一意に復元でき、全nで一般次数9。同一群の商へのcartesian atlasにより、適切な非空開上で **表現可能な有限 étale 階数9** に降下する（`thm:nfm-correction-degree-nine`）。これでΦ自体は非双有理と確定する。粗モジュライの関数体次数と同一視するには慣性群の比較が別途必要である。

補助的な厳密計算として、framedなψの幾何学的モノドロミーはS₉となる。p′=1に制限すると

```
b=q+q³/12+1/[3(1−q²/4)³]
P(q,b)=−q⁹+12bq⁶+96q⁵−144bq⁴−512q³+576bq²+768q−768b+256.
```

有理写像P¹_q→P¹_bの次数は9、q=2,−2,∞にそれぞれ位数3の極を持つ。`computations/verify_poisson_correction.py` に判別式の全係数とresultantを保持し、判別式が非零定数倍の次数10の平方因子を持たない多項式となることを有理数上で確認する。従って有限分岐点は10個ですべて単純。連結被覆なので作用は推移的であり、無限遠の局所モノドロミーも有限分岐点のものの積で書けるため、互換で生成される推移的群はS₉となる。この制限の群は二次元のψの群に含まれ、ψ自体もS₉。intrinsicな粗モジュライのGalois群はこの計算から自動的に決めない。

### 五次混合項の二定数への還元

`prop:nfm-mixed-fifth-reduction` に全証明とI,Jのε縮約を置く。T=F'''_active、M=F''_active、q=F'_active とすると、再帰の五次項はqT⁴またはM²T³の型だけを持つ。Weyl対称化の局所性も二次式の恒等式で確認しており、裸の座標やF自身を追加のjetとして使わない。この二型の一次形式共変式の次元はそれぞれ1と2。S(g)dF,dI,dJの独立性を行列式−35/3で示し、全nで

```
π₅(F)=Π_Q₅,
Q₅=S(g)F/80+β(I(F)−S(g)F)+γ(J(F)−S(g)F)
```

へ還元する。β,γの値は未計算だが、還元自体には本文の証明と独立読解点検がある。三次共変式の一次元性からI(g)=J(g)=S(g)gを得るため、有限標本からの推測ではない。F=g(x+a(U))+G(U)では両追加項のactive勾配が零となり、分離型だけでは二定数を決められない。

指定中心元についてW₄=Q₅−a₄F+G₄(U)。全Jacobi環では[F]=0なので、[W₄−τ_F(Ψ_λ(F))]=β[I]+γ[J]+[G₄−τ_F(Ψ_λ(F))]。従って幾何的な四次障害を求める際にはa₄を先に計算する必要がない。β,γと純中心三次G₄を求め、得た類の消滅・非消滅を検証するのが次の具体的な課題である。

### 次の比較計算

二つの独立な混合Taylor jetで生成元固定再帰を評価してβ,γを決め、中心逆像からG₄(U)を求め、差 W₄−τ_F(Ψ_λ(F)) を全 Jacobi 環で評価する。c₂と奇数次potentialの消滅は確定済みである。split 族の点曲線一致は強い検査例だが、一般混合係数の全三次の復元を保証しない。残余低 rotation 積による勾配回復は、形式写像の選択依存性と全 O-降下を調べる別経路として保持する。

## 7. 一次資料の確認箇所と引用上の注意

正確な書誌とURLは `papers/references.tex`。以下は議論に直結する確認箇所であり、全論文を監査したという一覧ではない。

- Etingof–Ginzburg, JEMS12(2010), Theorem3.3.2 / §9（印刷p.1414）：三変数 potential の PBW・中心元・Rains の有限中心公式。今回のεの非消滅は公刊式の斉次部分を直接使い、係数恒等式を独立に記号検算した。Proposition8.1.1と式(8.1.3)には形式量子化の中心とPoisson中心の同型が既にあり、対応の存在そのものを新規とは数えない。現行のtrace–Hessian処方は有限パラメータと相対降下について位置付ける。https://ems.press/content/serial-article-files/31746
- Dito, *Kontsevich star-product on the dual of a Lie algebra*, arXiv:math/9905080, §2 equation (3), §3 Theorem2：§2 の式は一般 Poisson tensor の二次星積であり、eye 項を含む。§3 Theorem2 も一般 Poisson 構造の星積に対する Weyl 化である。Lie 代数に限定される後続の Gutt 星積との比較とは区別する。本稿の ρ₂F は §2 の式の線型形式の冪への適用と polarization から直接求める。[一次資料](https://arxiv.org/abs/math/9905080)。
- Shoikhet, *Vanishing of the Kontsevich integrals of the wheels*, arXiv:math/0007080, §1.3 Theorem、§2.3.1：harmonic-angle の内向き wheel の重みの消滅と中心写像を確認。Weyl 模型への変換で現れる二次項と、同じ formality の中心写像の項を区別する。固定 gauge を指定せず係数 1/24 を普遍的な未標識量と呼ばない。[一次資料](https://arxiv.org/abs/math/0007080)。
- Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*, Enseign.Math.55(2009),235–273、DOI 10.4171/LEM/55-3-3、§2 Lemma2.1と式(4)–(5)・p.240：Hesse正規形とWeierstrass係数を公刊PDFで確認。パラメータ(t₀,t₁)=(1,3λ)から本文のj式を得る。係数式からjの規格化も厳密検算した。[公刊一次資料](https://ems.press/journals/lem/articles/12146)。
- Behrend–Noohi, Math. Ann.371(2018),1375–1408, DOI10.1007/s00208-017-1624-1：刊行版§2.3のgrading rigidification・twisted algebra・determinant中立化、§3.1.2の(C,O,s)を直接確認。これらの一般手法自体は既知であり、本稿は全O同値によるsを外した局所stack比較とrank(r,3)の非中立性を区別する。https://link.springer.com/article/10.1007/s00208-017-1624-1
- Stacks Tags058G,0781,03R6：Lazard、代数的stack上のQCohがGrothendieck圏、PGL torsorと中心単純代数。Tags063P,063U,062Y,056Q：相対正則埋込み・相対Cartier因子の任意底変更。本文の相対構成に使う範囲を一次資料で確認。
- Berger–Taillefer, J.Noncommut.Geom.1(2007), Theorems3.1,3.6 と Theorem3.6 の証明：potential による PBW 変形と自己双対解消。体上の定理を任意係数環へ直接適用せず、cyclic Hessian と分裂濾過から相対複体を構成する。
- Keller, *On differential graded categories*, arXiv:math/0601185v5, Theorems3.4,3.8(c)：compact 部分の thick 生成と compact generators による dg Morita 表示。基底は一般の可換環。本文では dg orbit 模型 A→Q とその両側作用を明示して用いる。
- Mori–Smith, arXiv:1502.07403v2, Theorem4.2：滑らかな三変数三次に付随する二次 Calabi–Yau 代数。Theorems1.2,7.2 と Lemma7.1：点曲線の Hessian 公式と対称行列＋交代行列の行列式。点曲線公式を新規とは数えない。[一次資料](https://arxiv.org/abs/1502.07403v2)。
- De Laet–Le Bruyn, *The geometry of representations of 3-dimensional Sklyanin algebras*, Algebr.Represent.Theory18(2015),761–776、arXiv:1405.1158v1 §2 p.3：巡回和で書いた中心元 a(b³−c³)C+b(c³−a³)D+c(a³−b³)S。非巡回の Rains 式とは出典箇所を区別する。[一次資料](https://arxiv.org/abs/1405.1158v1)、[刊行版](https://doi.org/10.1007/s10468-014-9515-6)。
- Kontsevich, *Deformation quantization of algebraic varieties*, LMP56(2001),271–294、§2.3 Proposition6：二次 Poisson tensor と二次代数の形式的 GL 同変対応。Conjecture1・Questions1 の収束・周期の問題と、本稿の有限 jet・形式構成を区別する。[一次資料](https://arxiv.org/abs/math/0106006)、[刊行版](https://doi.org/10.1023/A:1017957408559)。
- Kontsevich, *Deformation quantization of Poisson manifolds*, LMP66(2003),157–216、Theorem4.6、§§4.6.2,6.3：formality とグラフ構成・線型共変性。選択した formality 自体の独立性を主張しない。[著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf)、[刊行版](https://doi.org/10.1023/B:MATH.0000027508.00421.bf)。
- Ciliberto–Ottaviani, *The Hessian map*, arXiv:2006.07213v1 (2020), §5 Theorem5.7：射影的な純Hessian写像の一般次数3をSL₃同変性とHesse族への還元で求める。p.17の二回合成は次数9。本稿のaffine補正f↦f+Hess(f)/24とは異なり、Hesse還元手法そのものの新規性を主張しない。[一次資料](https://arxiv.org/abs/2006.07213v1)。
- Ottaviani, *Effective methods for plane quartics, their theta characteristics and the Scorza map*, Ann.Univ.Ferrara70(2024),1115–1153, §3 Remark3.3直後：古典的四次Aronhold不変式の25単項式表示と四つのdeterminantによる縮約を明記。本稿のSはS(xyz)=1という規格化と再現検算であり、新しい不変式ではない。[一次資料](https://doi.org/10.1007/s11565-024-00528-2)。
- Lindberg–Pym, *Semiclassical Hodge theory for log Poisson manifolds*, arXiv:2408.16685v1 (2024), §1.6・§6.7 Theorem6.9、Remark6.10（印刷pp.59–60）：Kontsevichの元のharmonic-angle星積で、原生成元の交換比 q_ij=exp(hλ_ij) を証明。§1.6でqをw_ij/w_jiとして定義しているため、任意の生成元変更を経た抽象同型だけの結論ではない。任意stable formalityへの一般化に残るGauss–Manin適合条件と区別する。この量子トーラスの公式自体は既知入力。[一次資料](https://arxiv.org/abs/2408.16685v1)。
- Antieau–Krashen–Ward, *Derived categories of torsors for abelian schemes*, Adv.Math.306(2017),1–23、Theorem2.2：体上の原点を持つ楕円曲線の k-linear 導来同値は k-同型を導く。点のない genus-one torsor に同じ結論を流用しない。[一次資料](https://arxiv.org/abs/1409.2580)、[刊行版](https://doi.org/10.1016/j.aim.2016.09.037)。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996), Theorem4.2.2, Proposition4.2.5, §4.3：一点中心拡大の点対応と二次関係。
- Mayanskiy, arXiv:1303.5916v1, Theorem1, §2.2：三様体の Plücker 方程式。被約分類と scheme structure を区別する注意があり、後者には実際の Schouten 計算を使う。
- Bonala–Clarke–Mohammadi, arXiv:2103.16208v1, §2.4 Theorem2.3：標準単項式基底。本稿はその次数二の比較不能対を列挙して 5 binom(N+1,6) を導く。
- Landsberg–Ottaviani の Young flattening と Gesmundo–Landsberg, *Explicit polynomial sequences with maximal spaces of partial derivatives and a question of K. Mulmuley*, Theory of Computing15(2019), Article3, Proposition6.1, 式(6.2)、Remark6.6：三次式の Koszul flattening の既知の階数上界。本稿の Jacobi 係数写像との同定と座標的な普遍関係を介して利用する。上界そのものを新しい結果として数えない。
- Boij, *Gorenstein algebras with nonunimodal Betti numbers*, Math.Scand.84(1999), 161–164, Remark6（pp.163–164）、DOI 10.7146/math.scand.a-13871：N=9,10、socle 次数三の apolar Gorenstein 代数の total Betti 表とその達成例。本文の Koszul 複体の比較を通じて二次 Jacobi 階数の最大性と差330が既に従う。表を graded Betti 表と誤読せず、b₄−c_N=β_{3,5}+β_{4,6} から必要な消滅を取り出す。
- Boij–De Negri–De Stefani–Rossi, *On the rate of generic Gorenstein K-algebras*, Math.Z.311(2025), Article10, arXiv:2304.14842v2, Introduction pp.2–3：生成次数についての既知結果と最小分解全体の問題を区別し、中間位置の予想には反例があることを記す。一般 apolar 代数の Koszul 性を β_{4,6}=0 の代用にしない。
- Bricalli–Favale–Pirola, *On the irreducibility of Hessian loci of cubic hypersurfaces*, Forum Math.Sigma13(2025), e80, DOI 10.1017/fms.2025.36：Proposition2.1 の Hessian/apolar 積と滑らかさ、Definition3.1・Remark3.3 の Thom–Sebastiani 分解、Theorem3.4 の Hessian rank locus による判定。本稿の最大法接空間の幾何と関連する既存結果であり、Jacobi 横断切片やスキームの retraction は本文で別に証明する。
- Stacks Tags 01OA,0245：射影束と fpqc アフィン降下。01OA の商直線規約と本文の部分直線規約は双対であり、混同しない。
- Gabriel, *Des catégories abéliennes*, III §1, p.365：商圏の Hom の filtered-colimit 表示。中心正則対による飽和性の証明に使う。
- Stacks Tag023N（Proposition35.3.9）：忠実平坦な加群降下の核による構成。Tag03PK・040Q（§59.28）：Kummer 列と μ_d-torsor。Tag02RU：曲線の主因子の次数。固定模型の tails・全同値の降下は本文で構成する。局所一ブロック型の効果化には、別に重み付き加群のGabriel商と全O-Hom比較を用いる。
- BFK, *A category of kernels for equivariant factorizations and its implications for Hodge theory*, Theorem5.39 **一般式**とその証明、印刷pp.82–84：sector の Koszul コホモロジーと parity。Lin–Zhang Theorem3.5 の parity にある内部 twist は cohomological degree と読む。同所の引用番号5.9は原著では5.39。BFK p.83 の簡約表示にも奇数側 Jac を残す誤植があるため、一般式の H^(2l+1) と孤立臨界点なら H^0 のみという p.84 の証明を根拠にする。
- Pirozhkov, arXiv:2208.13604v1, Lemmas5.1,5.2：非対角 Hodge diamond と実際の幾何的 KS 単射。Lemma5.2 は n=3 でも使えるが、同稿の大域 Torelli Theorem5.3 の三次条件は n>3。
- Huybrechts–Rennemo, Algebraic Geometry6(2019), Proposition3.5 / Remark3.8：四次元の HH²=22 と幾何方向20。
- Lurie DAG X, Theorems5.1.9,5.3.16 / Proposition5.3.21、Blanc–Katzarkov–Pandit §3.3,§4.3：tame の1-proximate性、hull の Hochschild 制御、actual→hull の (−1)-truncated性。BKP の一変数形式生成結果を任意基底の定理へ読み替えない。
- Kuznetsov の fractional CY 論文と Lin–Zhang Proposition3.7：Serre/rotation の算術。Lin–Zhang Theorems4.1,5.1 の categorical Torelli は既知入力。
- BFK, *Orlov spectra: bounds and gaps*, arXiv:1012.0864v3, Theorem5.15：孤立次数三特異点の三連続内部 shift による生成。前項の BFK 論文と区別する。
- Kuznetsov, *Derived categories of cubic fourfolds*, Theorem3.1：Pfaffian cubic と K3 の導来同値。

- Fraenkel, arXiv:1310.6083v2, Proposition4.1 / Theorem4.3：孤立特異点を持つ affine 超曲面の Poisson 延長を gradient の Koszul 複体で記述する。三次 n-fold のパラメータスキームの境界を主張するものではない。
- Carles, Ann.Math.Blaise Pascal3(1996), §8 Lemma8.35（p.60）、DOI 10.5802/ambp.67：Lie law の変形の非零二乗零パラメータ。
- Carles–Márquez, Ann.Inst.Fourier61(2011), §3 Theorem3.2、Propositions3.9,3.10、DOI 10.5802/aif.2620：Lie law の Jacobi スキームの局所・大域冪零元と明示例。本稿の次数2という意味と冪零指数を区別する。

関連する近刊には Bricalli, *Linear Spaces in Hessian Loci of Cubic Hypersurfaces*, Mediterr.J.Math.23(2026),173、[DOI 10.1007/s00009-026-03169-1](https://doi.org/10.1007/s00009-026-03169-1)、[arXiv:2603.23207v1](https://arxiv.org/abs/2603.23207v1) がある。Definition1.3、Lemma1.8、Theorem1.5 の Thom–Sebastiani/Hessian/apolar の関連を確認した。同 Theorem1.5 が前論文を Theorem2.3 と呼ぶ箇所は、前論文の公刊版では Theorem3.4 に対応する。これらの Hessian 幾何の既存結果と、本稿の Jacobi 方程式全体の局所構造を区別する。

Lie algebra law の Jacobi スキーム一般に非被約性があることは既知である。また本稿の二次階数の上界、N=9,10 の最大性、および差330という数値も上記の既存研究に由来する。「Jacobi スキームに初めて冪零元を見つけた」あるいは「330という二次の不足次元を初めて計算した」という主張をしない。

現在証明を持つ寄与候補の中心は、全 O-同値の係数降下と局所模型 stack、全非空開に残る表示障害、相対点対応からの中心商復元、trace–Hessian と強い lift による Poisson 開の逆構成、ならびに残余復元との比較障害、混合 trace を含む代数的補正の降下・一般次数9、c₂の消滅・偶奇性・五次共変式の適用、形式 support 保存と split 族での補正後残余比較である。強い lift の Koszul 手法、formality と中心対応、二次星積、wheel 消滅、残余 MF 模型そのものは既存入力と区別する。全成分のモジュライ、一般混合係数の全次数 Ku 比較、残余同値の全 O-降下は未完成である。

保持する補助成果には、n=8 の**次数三以降を含む** Jacobi イデアルの決定、頂点の長さ330の平方零拡大と完備局所非分裂性、全 polar 方向を残した横断切片、直和の retraction による特殊三次の非零冪零例、実現する大域持上げ障害がある。二次階数だけでは得られない主張として証明を置く。全引用・被引用文献や MathSciNet/zbMATH の網羅的調査は未実施であり、以上の寄与候補、比較障害、残余形式認識の厳密な初出は継続して確認する。

## 8. 再現の入口

README の再生成手順で、ソース参照、二次・三次の保存済み証明書、LuaLaTeX 組版を確認できる。TeX はルートから実行し、`.latexmkrc` が `build/` を出力先とする。次数三の検証は Python・NumPy と C++17 コンパイラを用い、大きな行列を `build/jacobi-vertex/` に再生成する。証明に必要なテンソル・選択行・検証コードを保存し、再生成できる大行列自体は収録しない。

trace–Hessian の中心係数・八次代数 trace、全次元の KS 例、split Hesse の有理式と j 差、混合係数の二次恒等式についても、README と `notes/validation.md` にある該当手順と確認範囲を参照する。厳密な記号計算による係数検証を、未公表入力の非可換中心性・完備 MF 移送・一般点復元の全証明の独立検証と同一視しない。任意次元・任意基底の主張は、有限個の計算例だけでなく本文の相対証明に依拠する。

外部文献 PDF、旧版原稿、旧 ZIP、担当者別の重複レポート、コンパイル中間生成物は現行一式に含めない。主張の証明・証明書の生成・実際の検証・保存は別の状態として扱い、検証事実の正本は `notes/validation.md` とする。
