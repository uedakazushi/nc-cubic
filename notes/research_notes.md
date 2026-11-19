# 非可換三次 n-fold：現行研究ノート

2026年11月20日 / v2。研究方針は `../00_research_plan.md`。証明全文は現行論文に置き、このノートは依存・適用範囲・障害・再現の入口をまとめる。

## 1. 記法と成果の確実性

n ≥ 3、N = n+2、r = n−1。次数一生成元空間は V、中心部分は U、dim U = r、active 部分は3次元。点の空間 W = V* を用いるので F ∈ Sym³V = Sym³W*。B は周囲二次代数、A = B/(w) は中心三次商。QGr は全次数付き加群の torsion による Gabriel 商であり、qgr や compact dg 残余圏と混同しない。

現行論文には主要結果の証明を記載した。次の区分を守る。

| 主張 | 状態・依存 | 証明所在 |
|---|---|---|
| 任意 d の中心 Veronese 復元 | C-flat、rank U≥2、普遍低次数中心条件の下で証明 | `thm:nfm-central-veronese` |
| 全整数の切断飽和性 | 中心正則対と C-flat から証明。noetherian 性不要 | `lem:nfm-central-saturation` |
| b_n 次元の次数付き DM stack、s_n 次元 torsor | 明示した相対 PBW・中心量子化入力を使用。全次数付き同型と有限安定化子は本文で証明 | `prop:nfm-graded-presentation`, `lem:nfm-finite-stabilizer`, `thm:nfm-central-torsor` |
| 普遍相対双対、compact 性、proper Hom | 良い相対 PBW 表示チャートの明示した有限射影・分裂入力から、任意底変更と両立する構成を証明 | `thm:nfm-relative-ambient-cy`, `thm:nfm-relative-line-cohomology`, `thm:nfm-relative-serre` |
| 全 O-保存 Abel 同値との比較 | 上の相対双対入力を供給。一般の圏族の係数作用・全同値の fpqc 降下を残す条件付き定理 | `thm:nfm-full-hom-conditional` |
| 点スキームと型 (2,2,2,3) | 楕円境界・固定点なし・中心三次非零因子等の明示条件下で証明 | `thm:point-nfold` 以下 |
| 3≤n≤7 の一般 Jacobi スキーム | 整数小行列の非零証明書により証明 | `thm:nfold-low-dimensional-generic` |
| n≥8 の I_F≠J_N、頂点完備化非同型 | 全滑らか F。被約分類に依存しない方程式数の証明 | `thm:nfold-high-dimensional-nilpotents` |
| n≥8 の一般 F での非被約性 | 上記に、入力論文Aの √I_F=J_N を追加 | 同定理 |
| 二次部分の一般階数と下界 | binom(N,3) 個の普遍関係を証明。N≤10 の最大階数は整数小行列で確認。N=10 の差は一般に330 | `lem:nfold-universal-row-relations`, `thm:nfold-low-dimensional-generic` |
| 非零点の局所構造、頂点の有限長性 | 法接空間 Λ³K を証明。有限長性・全射影化には既存の被約分類を使用 | `thm:nfold-normal-tangent`, `cor:nfold-vertex-support` |
| 高次数の非零性・次数幅 | 標準単項式の Hilbert 関数と生成式数から証明。冪零根基自身の積の指数は未決定 | `prop:nfold-higher-nilradical` |
| n≠4 の通常 Artin 残余形式認識 | 既知 HH 計算・実際の KS 単射・Lurie の tame 圏変形を用いた証明 | `thm:nf-residual-formal` |
| 全 Abel 形式近傍・大域残余射 | 未完成。Poisson 計算・次元一致からは結論しない | 方針の優先課題1〜3 |

証明の記載と今回の点検を、外部査読や機械形式検証と同一視しない。新規性の網羅的確認は未完了である。

## 2. 入力研究の正確な範囲

`nc-cubic` の固定 commit は `eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59（いずれも2026年11月14日）。

- 論文A `poisson_geometry.tex`：`prop:pg-represent` の bivector 表示、`prop:pg-jacobi-extension` の affine Jacobi 延長、`thm:pg-normal` の複数 Jacobian ブロック正規形、`cor:pg-generic` の一般三次における被約 Grassmann 錐。今回の Jacobi スキームの非被約性は最後の被約分類に依存するが、二次方程式の不足自体は依存しない。
- 論文A `general_dimension_universal_quantization.tex`：`thm:pg-all-dimensions`, `prop:pg-ad-relative-chart` が中心量子化の入力。一ブロック相対 PBW 開と中心三次束の存在は、この研究稿と Etingof–Ginzburg の既知の構成から取る。今回その全証明を独立に再検証したわけではない。
- 論文B `generic_recovery/main_result.tex` 等：既に全 n≥3 が対象。C[h]_(h) 上の次数別有限自由な中心三次対が、多項式環と滑らかな三次式へ特殊化する場合を扱う。一般点の coherent 残余模型は rotation と指定三次周期を保つ。方程式は C(h)、同値核は有限拡大上という区別を守る。全パラメータ・任意の nc cubic・核の基底体への降下を自動的に含まない。
- 三様体稿 v22 の固定 commit は `6c35d2c84671c2538e61836a6bf3a511392eacce`。任意係数の全 Hom 比較と点スキームの出発点を参照するが、n=3 の形式環を高次元にそのまま転用しない。

古い一般次元ノート中の別リポジトリ名を現行の依存先として使わない。上記の固定 commit と現行稿の参考文献が参照の正本である。

## 3. 中心復元・モジュライで失わない条件

Z(A^(d)) = Z(A)^(d) は、中心元 u に対して u^(d−1)[z,a]=0 と C-flatness を使う。非被約係数でも u は非零因子である。Z(A)_d = Sym^d U だけを書いて、中心 Veronese の同定を飛ばさない。

次数一を復元する最後の段階は A[u⁻¹] ∩ A[v⁻¹] = A である。rank U≥2 を使う箇所はこの二変数 Čech 交叉であり、rank1 に無条件に広げていない。Veronese 同型の持上げ μ_d は次数スカラー内にあり、全 O-保存問題の新しい慣性ではない。個々の同型の大域持上げの H¹(μ_d) と、対象の降下の H² 障害を区別する。

同じ交叉は切断の飽和性も与える。tails 上の射 f の f(u^m)/u^m = f(v^m)/v^m を比較すると、元 a∈A_j が回復し、f は左乗法 a に等しい。これにより負次数の Hom も零となる。一般の Hom と局所化の可換性を仮定せず、既にある射から得た一意な係数を貼る。

一ブロックでは楕円 σ の小位数を 1≤j≤max(3,n−1) で除く。3次元で必要な位数除外だけでは高 n の低次数中心を保証しない。相対中心を任意底変更後にも使うには、有限型被約の普遍底で交換子行列を分裂単射にし、その後に係数変更する。閉点の中心等式だけを非被約底へ外挿しない。

表示空間は Sym³V/Sym³U、群は U を保つ parabolic P、作用は det(g|V/U)^(-1)g(F)。grading scalar を除いた P̄ を用いる。全次数付き同型がこの作用で捉えられることは、関係空間が Λ²V→Sym²V の graph であることと Z(B)_1=U に依存する。

中心束 E の中の W=Sym³U、L=E/W は、それぞれ scalar weight3 を持つ。商へ普通のベクトル束として降りるのは Hom(L,W) である。P(E)\P(W) は分裂の torsor であり、標準原点はない。ambient とその同定を固定した2-fiberと、ambient の同型類だけを固定して残る有限自己同型作用は異なる。

複数ブロックでは rank(E/W)=k。正しい形は P(E)\P(W)→P(E/W) 上の Hom(O(-1),W)-torsor。k≥2 では固定 ambient 上にも射影的な k−1 次元の方向が残る。一ブロックのアフィン空間だけの記述を流用しない。

### 相対双対で使う入力と降下の境界

`papers/sections/relative_duality.tex` は、最初に被約有限型 C-基底 R、純 active 代数 S の次数別有限射影性・各幾何学的ファイバーの二次 Koszul 3-CY 性、分裂した active PBW 同型を仮定する。その上で中心差 u_{α,L}−u_{α,R} の r 本の Koszul 解消を使い、Θ_{B/R}=B(N)[−N] を真正な双加群として構成する。各ファイバーの CY 性だけを相対同型へ外挿していない。

中心三次商の各次数の完全列は係数線型に分裂する必要がある。良い一ブロックの G+g は最高 active 記号の正則性と一定階数からこの条件を満たす。これらの入力を得た後は、任意の非平坦・非被約 R→T を許す。

全 twist RHom は a=j−i≥0 で A_a、−r<a<0 で0、a≤−r で A_{−a−r}^∨[−n]。compact generator は O(0),…,O(N−1) の直和で、compact 間の Hom は係数 perfect となる。Γ_A(A)^∨=A(−r)[N−1] を真正な双加群として求め、dg orbit 代数 A→Q への両側局所化から Q^∨=Q(−r)[N−2]、Serre 関手 S=(−r)[n] と trace を構成する。

相対 CY の規格化は表示チャート上のもの。全商 stack 上で orientation を自明化したという主張ではない。compact Hom の底変更、全 Abel 同値の fpqc 降下、対象となる圏族の効果化は別問題であり、後二者は現在のモジュライ上の課題である。dg smoothness もこの計算からは結論していない。

## 4. 点関手の幾何と復元の限界

点加群には M_0≃O_S の同定を付け、同型はそれを保つ。これを省くと基底の Pic(S) による tensor が余分に残り、点スキームが単純に関手を表すとは言えない。

C=V(F_x,F_y,F_z) は中心射影 P^(r−1) への有限平坦8重被覆であり、pushforward は O⊕O(-1)^3⊕O(-2)^3⊕O(-3) と非標準的に分解する。中心三次による乗法の行列式は O(24) の非零切断で、f_*O_D の Fitting0を与える。これを射影先への双有理写像や被約像の方程式と読み替えない。

D の双対化層は O_D(7−n)。n=3 は長さ24、n=4 は滑らかなら次数24・種数37、n=7 は双対化層自明となる。この最後の数値から D と残余圏の幾何的模型を同一視する証明はない。

埋込み点スキームだけからは Q=I(D)_2、U=I(E)_1 を得る。Hessian 条件 M Hess(g) symmetric ⇒ M scalar を加えると R_Q = C F⊕Sym³U が回復する。Hesse 型 g=(x³+y³+z³)/3+λxyz の λ(λ³−8)≠0、λ³≠−1 が明示的非空条件。shift のグラフを加えると二次関係そのものと hΠ_F の尺度が回復する。

R_Q/Sym³U の直線は、特定の古典三次代表を選ばない。量子中心 w と残余圏からの可換三次式の対応、有限係数での補正、Poisson 零スキームとの関係は別問題である。

## 5. Jacobi 行列の証明書と今後の計算

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

### 普遍関係・一般階数・共通核

対称性から Σ_r B_{H_r}(P)_{rabc}=0 が恒等的に成り立つ。Λ³W*→W⊗Λ⁴W*、β↦Σe_r⊗(dz_r∧β) は縮約を N−3 で割ることで分裂するので、binom(N,3) 個の独立な従属関係を与える。全三次テンソルに共通する核もこの像に等しいことを、T=ℓ³ によって証明した（`lem:nfold-universal-row-relations`）。

従って a_N=N binom(N,4)−binom(N,3) が階数上界であり、次数二の差は ε_N=5binom(N+1,6)−a_N 以上となる。N=9,10 の証明書は一般の核が普遍核と等しいことを示す。N≥11 の一般核は未決定であり、「全テンソルに共通する核」と「一般の一つのテンソルの核」を混同しない。

### 非零点と頂点の構造

滑らかな F、P∈Λ³A に対して K_{F,A}={w:T_F(A,w,W)=0} と置く。A∩K=0 は滑らかさから従い、法接空間は Λ³K となる。dimK≤2 と、非零点 P の近傍で I_F=J_N となることが同値（`thm:nfold-normal-tangent`）。独立に、三次元部分空間対の incidence によって、横断性を失う滑らかな三次は係数空間の余次元少なくとも3Nの閉集合に入ることも示した（N≥6）。

既存入力 √I_F=J_N の下で dimK≥3 なら、K 内の分解可能な Q を取り P+tQ という非分解可能解ができるため矛盾する。従って一般の全非零 Poisson スキームは Grassmann 錐非零部に等しく、Proj(R/I)=Gr(3,N)、I_F^sat=J_N となる。この等式は係数開上で相対的にも成立し、任意底変更と両立する。

冪零根基 N_F=J_N/I_F は有限長で、H⁰_{m0}(R/I)=N_F。n≥8 では Ass(R/I)={J_N,m0}、頂点の深さは零である。したがって非被約性は一般の非零 Poisson 構造の余分な変形方向を意味せず、零構造に集中する埋込み成分である。次数二の元が冪零であることと二乗零であることを区別する。

### 高次数と計算の次の入口

`prop:nfold-higher-nilradical` は、Grassmann 環の Hilbert 関数と R_{d−2}⊗I_2→I_d の全射から、各次数の差に明示的な下界 L_{N,d} を与える。N≥13 では L_{N,3}>0、N=13 では179179。固定した任意の d≥2 に対しても、N が十分大きければ L_{N,d}>0 となる。

従って有限長冪零根基の最高次数・最高 socle 次数は次元によらず有界でない。N_F が次数二で生成されるので、m0 による最小消滅指数も非有界である。一方 N_F 自身の積による冪零指数は未決定。N=10 の全 Hilbert 関数、長さ、次数三の消滅、二乗零性もまだ決定していない。次は保存済みテンソルで R_1⊗I_2→J_3 を疎行列として計算する。

特殊 cubic では n≥4 から非分解可能解がある。F=Σz_i³、P=e_123+e_456 は独立な二つの Jacobian 括弧の和で一般階数4。従って「全滑らかな三次で Grassmann 錐」という主張は、n=4 から既に複素点の集合として偽である。

## 6. 残余圏：三つの異なる次元区分

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

## 7. 一次資料の確認箇所と引用上の注意

正確な書誌とURLは `papers/references.tex`。以下は議論に直結する確認箇所であり、全論文を監査したという一覧ではない。

- Etingof–Ginzburg, JEMS12(2010), Theorem3.3.2 / §9：三変数 potential の PBW・中心元・Rains の有限中心公式。中心変数を係数として使う相対構成は入力研究と合わせて扱う。
- Berger–Taillefer, J.Noncommut.Geom.1(2007), Theorems3.1,3.6 と Theorem3.6 の証明：potential による PBW 変形と自己双対解消。体上の定理を任意係数環へ直接適用せず、cyclic Hessian と分裂濾過から相対複体を構成する。
- Keller, *On differential graded categories*, arXiv:math/0601185v5, Theorems3.4,3.8(c)：compact 部分の thick 生成と compact generators による dg Morita 表示。基底は一般の可換環。本文では dg orbit 模型 A→Q とその両側作用を明示して用いる。
- Mori–Smith, arXiv:1502.07403v2, Theorem4.2：滑らかな三変数三次に付随する二次 Calabi–Yau 代数。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996), Theorem4.2.2, Proposition4.2.5, §4.3：一点中心拡大の点対応と二次関係。
- Mayanskiy, arXiv:1303.5916v1, Theorem1, §2.2：三様体の Plücker 方程式。被約分類と scheme structure を区別する注意があり、後者には実際の Schouten 計算を使う。
- Bonala–Clarke–Mohammadi, arXiv:2103.16208v1, §2.4 Theorem2.3：標準単項式基底。本稿はその次数二の比較不能対を列挙して 5 binom(N+1,6) を導く。
- Stacks Tags 01OA,0245：射影束と fpqc アフィン降下。01OA の商直線規約と本文の部分直線規約は双対であり、混同しない。
- Gabriel, *Des catégories abéliennes*, III §1, p.365：商圏の Hom の filtered-colimit 表示。中心正則対による飽和性の証明に使う。
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

新規性の追加調査では、Lie algebra law の Jacobi スキーム一般に非被約性があることは既知である。本稿の寄与候補は、滑らかな cubic に付随する特定の Hessian-Jacobi イデアル、Grassmann 錐との n=7/8 境界、および冪零根基の次数二部分の次元の下界にある。「Jacobi スキームに初めて冪零元を見つけた」という主張をしない。検索、Loray–Pereira–Touzet/Mayanskiy の原文、Fraenkel、Carles らの一次資料では同じ境界を見いだしていないが、全引用・被引用文献や MathSciNet/zbMATH の網羅的調査は未実施である。高次元 cubic の該当境界と形式認識の初出確認は、なお継続課題である。

## 8. 再現の入口

READMEの4コマンドで、ソース参照、保存済み証明書、LuaLaTeX組版を確認できる。TeXはルートから実行し、`.latexmkrc` が `build/` を出力先とする。外部文献PDF、旧版原稿、旧ZIP、担当者別の重複レポート、コンパイル中間生成物は現行一式に含めない。検証事実の正本は `notes/validation.md`。
