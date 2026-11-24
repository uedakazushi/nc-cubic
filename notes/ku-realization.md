# 可換実現・反例・内在的判定

2026-11-24 / v93。主稿の比較、反例および回復に必要な補足。

[研究ノート入口](research_notes.md) · [研究方針](../00_research_plan.md) · [検証範囲](validation.md)

## 現在の可換実現問題

**現在有効な問題**は全称可換Ku実現予想（広い定式化と変形連結条件付きの両方が否定済み）の修正ではなく、可換実現可能な対象の特徴付けである。五次元には内在的 $R_j=\operatorname{Hom}(\Delta,S^{-j}[3j])$ とその三重積の必要条件があり、$T=\mathbb A^1\setminus V(27b^6+64)$ の実smooth proper族で可換実現可能な係数はちょうど $b\ne0$。$b=0$ の余核は不変Jacobian環の $[x_1x_2x_3]$ で、通常HHの次元は族全体で不変。重要なのは成立領域の分類と乗法・自然変換環の独立監査であり、HH一致や変形連結性だけを十分条件として使わない。原稿の証明の所在は `nft:prop:jacobian-necessary`, `nft:cor:nonclosed-cubic-locus`、新規性は未網羅確認。


狭い全称命題は五次元で否定される。$F_b=\sum_i(u_ix_i^2+u_i^3)+w^3+bx_1x_2x_3$ の偶符号作用を非自明な乗数で同変化すると、$b=2$ は可換 Ku に同値で $b=0$ はどの可換 Ku にも同値でない。家族の両点は同じ smooth proper 開にある。$b=0$ で三つの閉 Clifford 演算子に Pauli 行列を掛けた偶積は一次の rotation 変換であり、対称行列の階数一関係を作る。五様体では rotation は無標識でも保存される。[反例の証明](../papers/sections/narrow_fivefold_counterexample.tex)。

全次数の $R_j$ の Hilbert 級数も族全体で $(1+z)^7$ となる。偏微分の正則列の指標を固定部分ごとに平均する計算は [三重積の証明](../papers/sections/narrow_fivefold_cubic_product.tex) に置いた。非零係数の比較では二重原点加群の軸上の cone が剰余体を直和因子に持ち、三つの内部シフトの直和が厚生成する。五次元族の相対射影は例外四項を 3,2,1,0 の順で左変異する合成であり、perfect 複体の底変更と可換する。

同じ反例には三重積による独立な検証がある。一次・三次の自然変換空間の次元は族の全点で 7・35 だが、一次変換の三重積の階数は可換ファイバーで 35、反例で 34 となる。余核は同時符号反転で符号の変わる $x_1x_2x_3$ の一方向である。[固定点ごとの計算](../papers/sections/narrow_fivefold_cubic_product.tex)。

五変数の全対角型で全 coherent 圏が smooth proper なら、残余圏の HH₁ 次元五、可換 Ku 実現、可換 Ku への変形連結性は同値である（主稿 ndc:cor:hh-characterization）。十分性の入力は三乗根の三軌道での実比較と、符号型 I の除外・型 II の Clifford 双対である。

五変数の全対角交換型では二捩れ成分も解決した。三座標の偶符号作用の非自明な乗数を、Pauli 行列を tensor した Clifford 固有空間の積で扱う。比較先は $l\mapsto-l$、$g\mapsto g+4pql/\lambda^2$ で与えられる。三様体では円錐曲線束の偶代数と正則右加群を比較する。任意個の中心変数では、中心係数 $d=r^2=pq-s^2$ を共有する Koszul 因子化の積を用いる。二重原点加群の内部シフトが生成することを軸上の分裂から確認した。[三様体の同値](../papers/sections/narrow_diagonal_clifford.tex)・[全次元での指定二捩れ型](../papers/sections/narrow_sign_factorization.tex)。

五変数三乗根交換型では、連結な smooth proper 族の条件から残る三つの型すべてで可換実現を得た。巡回五頂点型では二変数因子の星型 quiver の変異で同値を作り、一つの座標対について群作用の合成障害が零であることを調べる。四つの座標対で順次同変化すると必要な乗数になる。任意次元でも互いに交わらない二変数対が分離した三次式は、指定した対ごとの位数三の作用で同変化しても同じ残余圏を与える。[同値の構成と適用条件](../papers/sections/narrow_fermat_root_equivalence.tex)。

一般の対角量子多項式環で中心三次が座標点に一次項を欠けば、その点の自己 Ext はいくらでも高い次数で非零となる。座標 chart を可換多項式商の多重次数付き twist として比較すると、交換係数の有限位数を仮定せずにこれを示せる。五変数では各座標の単項式の選び方を 47 軌道にまとめ、唯一の指数四の型を射影直線上の特異点によって除き、全係数を六乗根に絞った。[対角交換係数の有限位数制約](../papers/sections/narrow_diagonal_support.tex)。

**広い定式化への三次元の反例。** [量子 Fermat 中心三次商の定理](../papers/sections/quantum_fermat_obstruction.tex) は、次元・指数 5 の AS 正則な量子多項式環の中心正則三次商で、全 coherent 圏が smooth proper かつ残余圏の `(dim HH₁, dim HH₀)=(1,10)` となる例を与える。滑らかな可換三次三様体ではこの組は常に `(5,2)` である。主予想はこの滑らかな中心三次商を含む広い定式化で扱い、上の例で否定される。同じ周囲代数の全中心三次は七項で尽くされ、係数射影空間の滑らかな開集合全体で同じ障害が成り立つ（同節の系 `qfo:cor:central-family`）。Perry の相対 Hochschild 底変更定理から、そこに属する残余圏と可換三次三様体の残余圏は連結な smooth proper 圏族で結べない（`qfo:cor:deformation-separation`）。

C上n≥3を基本とし、generic・全固定点・全族・一般体上の降下を区別する。全intrinsic対象の認識やpoint functorの表現可能性は未完成であり、既知の局所表示だけを全対象と定義して済ませない。可換候補の方程式・判別集合・局所特異点の一致と、その候補への実際の比較核の存在も区別する。

point schemeとPoisson零スキームまで同一視できるという素朴な期待は、本文の注意 `ppz:rem:naive-expectation` と不一致の例で扱う。指定混合五様体の定常ノルムの全64根では、smooth properなsourceの点スキームに一つの被約孤立点がある。一方、滑らかな可換三次五様体上の全Poisson零集合には孤立点がないため、Ku比較を仮定せず全可換標的を排除できる。この五様体にも全64根で実際の可換Ku核を構成済みである。三様体の非被約局所環を用いる別の例も、実際の可換Ku同値を持つsourceについての結果である。これらは可換Ku実現から点スキームについて結論できる範囲を示す補助的な例として保持し、独立の予想や修正版を最優先課題として掲げない。

主比較に必要な楕円windowと体上のrotation共役の正本は、主稿の `comparison_foundations.tex` である。`eq:nfm-right-thcr-shift`、`lem:nfm-twisted-elliptic-window` をここから引用し、`csc:thm:comparison` が用いる `mbrc:lem:factor-correction` と分離比較も主稿に置く。相対Picard gerbe、比較核の分類と算術的降下は、これらの実比較を入力とするモジュライ稿に置く。混合族の `cmo:cor:cofinite` は主稿の `grl:thm:open-locus` を使う。稿をまたぐ参照は、定理番号と稿名から証明の所在をたどれるようにする。

point/Poisson不一致は本文の補助例として扱う。三様体の例の証明は主稿の `point_poisson_obstruction.tex`、混合五様体の例と孤立零点制約は混合稿の `mixed/poisson_limits.tex` を正本とする。Introductionはそれぞれの本文を参照し、例のために独立の予想を立てない。各稿の序論は中心問題・主要結果・既存理論との差・適用範囲を述べ、詳細な主張と証明を本文へ置く。

## 分離型と回復の比較

### 満支持型における同時存在

`point_poisson_split.tex` の `pps:thm:elliptic-existence` は、A=(⊗S_i)/(Σa_iΩ_i)、m=0,k≥2、全a_i≠0、実際のquadratic Koszul AS3楕円Sklyanin因子、正則中心Ω_i、滑らかな平面三次のTHCR商、固定点なしの点グラフを仮定する。各E_iの任意の非零方程式f_iに対し、X=V(Σf_i)とπ=Σc_iι_df_i P_i（全c_i≠0）を取り、Ku(A)≃Ku(X)とPt(A)=Z_X(π)=⊔E_iを同じXで実現する。

零イデアルはEuler場ξとの外積ξ∧πで計算する。E_i近傍である∂f_iが単元になり、mixed係数x_j∂f_iから全他block座標が消え、純block係数は3f_iとなる。従って台だけでなく任意非被約底でのスキーム等式となる。原Aの点関手自体も既存 `tbp:cor:all-blocks` で証明済みであり、第三Veronese中心商Dの幾何点の結果だけを用いているわけではない。

Ku比較は非可換・可換両側の中心同変積表示をPicard線束で共役し、actual Ωとfの三乗周期をスカラーの三乗根で同期して二重同変化する。jの相異性・特殊j除外・2p≠0はこの存在証明には不要。自然なθが二捩れで零でも、explicit因子仮定を満たせば別のfを選べる。基本開の自然X_ptは `pps:cor:simultaneous-comparison` と分ける。p=0や三捩れ等で点グラフ仮定が失われる場合は含めない。全O stackの単一の自然tensorや大域核sectionは別課題。

代数閉体ではblock scalingがΩ_iへ三乗で作用するので、全非零の中心係数直線は一つの軌道をなす。係数がpoint schemeに見えないことだけから非同型な満支持商を得たとは結論できない。

### 中心変数を持つ分離型の直接Ku比較と全点スキーム

`central_split_comparison.tex` の `csc:thm:comparison` は、C上、k,m≥1、N=3k+m≥5、B=(⊗S_i)⊗C[U]、w=Σa_iΩ_i+g(U)、全a_i≠0、gのJacobian環が有限次元の分離型を扱う。S_iは実際のquadratic Koszul AS正則三次元楕円因子であり、正則中心Ω_iとTHCR商S_i/(Ω_i)=B(E_i,L_i,t_pi)を仮定する。各E_iの任意の非零三次方程式f_iに対し、X=V(Σf_i+g)は滑らかで、Ku_coh(B/(w))≃Ku(X)を直接構成する。gに一次・二次のactive–central混合を許したという定理ではない。

証明は、線束windowの三つのaugmentation shift、有限Koszul–Shamash Hom、Γによる共通次数化から、中心群同変化をPerf(∏E_i)⊗MF^Z(C[U],g)へ比較する。楕円因子ではPicard補正とスカラー三乗根でrotation・actual Ωの指定周期を合わせ、中心因子は同一模型で比較する。有限二重同変化後にsmooth proper性とcoherent飽和を用いる。g=Σc_j u_j³の場合は各MF(C[u_j],c_j u_j³)≃Db(mod A₂)を直接用いる系 `csc:cor:fermat` があり、一般gのsmoothness補題への依存も不要。反例で使うのはk=1,m=2のこの経路である。

点グラフが固定点なしという仮定を加え、J_i=(S_i)_ab、J=⊗J_i、θ=Σa_i[Ω_i]とすると、`central_split_points.tex` の `csp:thm:point-functor` は任意の試験環で

\[
\operatorname{Pt}(A)=\coprod_i E_i\amalg D,\qquad
D=\operatorname{Proj}\bigl(J\otimes\operatorname{Sym}U/(g+\theta)\bigr)
\]

を与える。各J_iは三つの二次式の局所完全交叉、Hilbert級数(1+t)³、長さ8である。m=1,g=cu³,c≠0ではc+θが単元なのでDは空。`csp:cor:simultaneous-one-center` は同じXとブロックJacobian Poisson tensorについてKu同値とPt=Z=⊔E_iを同時に与える。

m≥2,g≠0ではDは型(2^{3k},3)、次元m−2、次数3·8^kの完全交叉。H=V(g)が滑らかなら、各点の完備局所環はJ[[t_1,…,t_{m−2}]]となる。中心射影は一般にHを経由しない。非零socle項a_i[Ω_i]の個数をsとするとscheme imageはV(g^{s+1})、第零Fittingイデアルは(g^{8^k})であり、この二つを混同しない。m=2ならDは三つのSpec Jだが、m>2では局所模型から大域的な積を主張しない。

自然な可換零スキーム側は同じ式のJをJ_cl=⊗Jac(f_i)、θを0に置いたもの。抽象スキーム同型でもgraded J≃graded J_clが必要である。完備局所環のassociated gradedはJ[t]で、次数一の冪零元が生成する部分環がJそのものだから、未証明の形式変数消去を使わずに回復できる。m=2ではこの条件は十分でもある。各Jacobian三次が滑らかでST非分解ならjの多重集合が必要不変量となる。この自然pairの障害だけでは、全Poisson構造・全Ku標的を排除していない。

## 実現 locus、回復と境界の障害

### 可換Ku実現locusの開性

`geometric_realization_locus.tex` の `grl:thm:open-locus` は、有限型C基底Sの実smooth proper dg族（étale局所Perf(Γ)、Γは底上perfect、対角perfect）について、n≠4なら可換cubicのKuとして実現する幾何点の集合がZariski開であり、étale局所に実際のcubic族・核を持つことを示す。

比較核stackはTVのperfect対象moduliと同値性の開性で局所有限表示Artin。既存 `thm:nf-residual-formal` の群oidとしての完全忠実性が、Artin持上げで既に指定された核とのactual自然同型を回復する。scalar Gmを消したとはしない。smooth atlasで局所smoothness criterionを使い、étale局所sectionを取る。n4、境界での閉性、全Abel族の相対smooth proper性、全intrinsic成分、point構造の同時延長は別問題。

### DVR上の比較核を判定する有限長複体

`geometric_realization_locus.tex` の `grl:prop:trait-kernel-test` では、DVR Rの商体をK、剰余体をkとする。R上smooth properなdg代数A,Bとperfect A–B双加群Pが既に与えられ、一般ファイバーの関手F_(P_K)=−⊗^L_(A_K) P_Kが同値である場合を扱う。Q=RHom_B(P,B)とし、

\[
C_A=\operatorname{Cone}\bigl(A\longrightarrow\operatorname{RHom}_B(P,P)\bigr),\qquad
C_B=\operatorname{Cone}\bigl(Q\otimes_A^{\mathbf L}P\longrightarrow B\bigr)
\]

と置く。二つのconeはR-perfectで、全cohomologyは有限長である。F_Pが同値であること、特殊ファイバーF_(P_k)が同値であること、(C_A⊕C_B)⊗^L_R k=0は同値。生成対象で単位・余単位を検査し、一般点での消滅と導来Nakayamaを組み合わせる。既知入力はToën–Vaquié, *Moduli of objects in dg-categories*, Lemma3.25とその証明である。

\[
d_R(P;A,B)=\sum_j\bigl(\operatorname{length}_R H^j(C_A)
 +\operatorname{length}_R H^j(C_B)\bigr)
\]

は有限な非負整数で、同値性はd_R=0と同値。分岐指数eの有限平坦局所DVR拡大R→R′ではd_(R′)=e d_Rとなるので、固定した延長核の不良特殊化は有限分岐だけでは消えない。有界有限自由複体のSmith標準形で、一般点でacyclicな各二項因子[R→^(t^m) R]のmを加えればこの長さを計算できる（`grl:rem:trait-smith`）。この数値は選んだ生成模型・延長核に依存し、圏だけの内在的不変量とはしない。

perfect延長の存在だけでは不十分である。A=B=R、P=R⊕R/(t)は一般点で恒等核だが、特殊化はk²⊕k[1]となり同値を与えない（`grl:ex:perfect-kernel-not-equivalence`）。この例には良い別の格子Rがあるため、必要なのは適切な核の整格子の選択である。指定二ブロックの元c族では、全smooth開上の実perfect Morita核と逆核・unit/counitを直接構成したので、そのDVRへの底変更も同値を保つ。norm全64根で個別にdefect行列を列挙したという意味ではない。一方h族では `mix:thm:h-integral-kernel` により指定一般点核のperfect整延長まで成立し、その中からdefect零の核を選んでh=1の核へ接続する問題が残る。固定点同値の存在は、既に選択した一般点核の任意の整延長の可逆性を意味しない。

### smooth properな両側からは特殊同値を導けない

一般のDVR延長原理への障害として、R=C[[t]]上のextension

\[
0\longrightarrow\mathcal O\longrightarrow\mathcal E
\longrightarrow\mathcal O(2)\longrightarrow0,
\qquad[\mathcal E]=t\in H^1(\mathbb P^1_R,\mathcal O(-2))\simeq R
\]

を取る。X=P(𝔈)はsmooth projectiveで、特殊ファイバーはF₂、一般ファイバーはF₀。後者は非零extensionの代表であるEuler列から従う。定数族Y=F_(0,R)と比べれば、両側がtrait全体でsmooth properで、一般点では同型である。これは既知のHirzebruch曲面の変形であり、Okawa–Uehara, *Exceptional sheaves on the Hirzebruch surface F2*, [arXiv:1409.7813v2](https://arxiv.org/abs/1409.7813v2), Lemma4.2（p.18）にも記されている。

特殊ファイバーの導来圏は同値でない。F₂の(−2)-section C上のO_C(−1)は2-sphericalで、自己Extは0,2次が各C、1次が零である（同文献Remark1.2、p.3）。F₀上でE⊗K≃Eなら、−Kのample性とcohomology sheafのHilbert多項式から各台は零次元となり、Riemann–Rochによりχ(E,E)=0である。従ってχ=2を持つ2-spherical objectは存在しない。一般点の同型graphの閉包は正則な積X×_R Y上のcoherent、従ってperfectな核になるが、その特殊化は同値にならない。smooth proper性とperfect延長だけから比較核の同値性を結論する方法は使えない。この例は三次五様体の残余圏の追加構造を持たず、nc cubicの主予想への反例ではない。

### 全Poisson零集合の孤立点制約と被約版の反例

混合稿の `mixed/poisson_limits.tex` にある `ppz:thm:isolated-zero-dimension` は、C上の任意の滑らかな三次超曲面X⊂P^(n+1)、n≥3と任意のPoisson構造πについて、

\[
|Z_X(\pi)|\text{ に孤立点がある}
\quad\Longrightarrow\quad
n=3k,\qquad\operatorname{rank}_{\mathrm{gen}}\pi=2k
\]

を示す。各孤立零点の局所スキームは零次元局所完全交叉である。π=0の場合は零集合がX全体なので孤立点を持たない。全非零πへの適用は未公表入力 `NCCubicA`、`poisson-cubic` の `thm:pg-normal` に依存する。正規形に一般性や各ブロックの楕円性を加えない。固定版と使用する補題は第2節「入力研究の正確な範囲」に記す。

証明の要点は、n+2=3k+mの正規形でEuler場Eとlift qの外積E∧qを計算することにある。中心座標u_α≠0のchartでは零理想が3k個のactive偏微分で生成され、局所次元は少なくともm−2。m=1ではEuler式がXの特異点を強制するため孤立点はm=2に限られ、正則局所環内の同数の生成元から局所完全交叉も従う。u=0では、非零ブロックbivectorを持つ点は純ブロックの平面三次曲線上にある。全active勾配が零で二つ以上のブロックが非零なら、それぞれを独立に拡大縮小して得る射影線型空間が零集合に入る。従ってu=0にも孤立点はない。この議論は各制限三次が特異あるいは零式の場合も含み、中央偏微分の消滅を仮定しない。

五次元では3∤5なので、**どの滑らかな可換三次五様体上のどのPoisson零集合にも孤立成分がない**。`ppz:cor:reduced-point-poisson-counterexample` は、指定二因子のnormの全64根で

\[
\operatorname{Pt}(A_c)=E_1\sqcup E_2\sqcup\{p_c\}
\]

が被約であり、全coherent導来圏・全coherent Kuがsmooth properであることを組み合わせる。孤立連結成分の有無は抽象被約スキームの同型で保たれるため、任意の滑らかな可換三次五様体Yと任意のπについてPt(A_c)_red≄Z_Y(π)_redとなる。この排除はKu(Y)≃Ku(A_c)を仮定する前に全Yに適用できる。さらに `cmo:cor:norm-commutative-kernel` により実際にKu(A_c)≃Ku(X_c)となるため、主予想の可換実現を持つ例でも被約point/Poisson一致は成り立たない。

一つの完全に明示した係数は **c=−44828**（`ppz:ex:reduced-counterexample-rational`）。u=1で二つのcharacterを(−1,−2,−3)、(−4,−5,−7)と取ると、中心値は28、448であり、28+100·448−44828=0となる。normの根の相異性により定常点は一つで、gcd(P64,N)=1によりsourceはsmooth properである。定常成分自体も一つの滑らかな被約点なので、全対象について単に「定常成分が滑らか」と仮定してもpoint/Poisson一致は得られない。個別の成立族・別の点関手・付加構造を課す修正は、それぞれ別に検証する。

Bondal予想の退化軌跡に関する結果とは量化が異なる。Druel–Pereira–Pym–Touzet, *Bondal's conjecture in dimension five*, [arXiv:2606.03424v1](https://arxiv.org/html/2606.03424v1), Theorem1.2、Corollary1.3、§4.4 Theorem4.3は、五次元Fano上のZ_X(π)に正次元成分が存在することを与える。これは別の孤立成分の併存を排除しない。本稿の全孤立成分排除は三次超曲面の正規形から得る別の結論である。一般次元の3整除制約と被約反例について、文献上の新規性の網羅的確認は未完了。一次資料の確認範囲は第7節を参照する。

### 一ブロックの定常成分が持つ情報

`point_poisson_obstruction.tex` の `ppz:prop:zero-scheme` は、HとH|Kが滑らかなrank2 Jacobian対について Z_X(π_H)=E_H⊔D_H、D_H=V(H_x,H_y,H_z,H) を証明する。量子側は D=V(F_x,F_y,F_z,w_ab) であり、楕円曲線の一致だけでは定常成分の一致は従わない。

境界中心評価は ε:Z(B)_3/Sym³U→Jac(g)_3 という**商直線間**の写像。全Z(B)_3と一次元空間の同型ではない。ε同型の開では元のDを同じΠの古典Casimir切断として実現できない（`prop:point-casimir-restriction-obstruction`）。Hessian scalar条件を加えると、全Ptの射影埋込み一致は良いrank2標的全体で不可能（`ppz:prop:embedded-obstruction`）。抽象同型や別supportを、これだけで排除しない。

三次三様体のsplitHesse族では、g_t=(x³+y³+z³)/3+txyz、λ(h)=(h+h²/3+h⁵/12)/(1−h⁴/4) と置くと、量子点楕円曲線と残余active曲線はE_λで一致する。自然残余pairの被約point schemeも同じである。一方、三つの定常点の局所環は量子側でJ_h、残余側でJ_λ、J_t=C[x,y,z]/(x²+tyz,y²+tzx,z²+txy)。全長さは各8である。中心socle項η=−(2/3)h²(1+h³)xyzは零とせず、u=1でv=a−η/a²（a³=−1,η²=0）へ吸収して厳密に局所環を計算する。一般hの有理恒等式は `residual_comparison.tex` に保持する。

局所環同型ならm-adic associated gradedも同型であり、次数一・二の乗法から勾配空間を回復する。既存gradient復元により平面三次が同型になるはずだが、j(λ(h))−j(h)=13824h⁴+O(h⁵)≠0に反する。固定h=1ではλ=17/9、j(1)=9261/8、j(17/9)=3813232609367/4849120870776と厳密に異なる。`ppz:prop:split-artin-obstruction` はこの固定例を直接証明し、有限j計算だけをscheme非同型の証明としているわけではない。

### 三様体の非被約局所環による全スキーム版の反例

**可換Ku実現を持ちながら、point/Poisson一致への期待が全スキームとして成り立たない例。** 正本は `point_poisson_obstruction.tex` の注意 `ppz:rem:naive-expectation` と系 `ppz:cor:complex-counterexample`。具体的な複素代数は

\[
S_\star=\mathbb C\langle x,y,z\rangle/(yz-3zy-2x^2,\ zx-3xz-2y^2,\ xy-3yx-2z^2),
\quad A_\star=S_\star[u,v]/\bigl(\Omega_\star+(u^3+v^3)/3\bigr),
\]
\[
\Omega_\star=\frac{79}{144}(x^3+y^3+z^3)+\frac5{96}
(xyz+yzx+zxy+yxz+xzy+zyx).
\]

指定因子は `explicit_sklyanin_input.tex` で、点曲線E_17/9、平行移動点p=(1:−3:−2)、THCR商、Koszul AS正則性、Ω★=−c_3/48を確認する。系 `csc:cor:fermat` は楕円因子と二つのA₂因子からX★=V(g_17/9+(u³+v³)/3)への実Ku同値と全coherent smoothnessを与える。この経路は一般点の形式復元とspreadを使わない。『良い一ブロック』は点関手の条件を指し、全O表示stackの全入力をこの固定係数で独立に確認したという意味ではない。係数は有理数だが、Ku比較の存在はC上の主張である。

前の自然pairでの非同型から全標的・全πの排除へ進むための追加証明は次のとおりであり、本文に全て記載した。

- Mayanskiy Theorem1と§2.2の既知のSchouten/Plücker計算により、任意の滑らかなcubic threefoldの全非零Poisson構造は分解可能なP∈Λ³C⁵から来る。active切断の滑らかさやgood条件を全πへ仮定しない。
- 任意の孤立Poisson零点pで局所長さ8・埋込み次元3なら、pはsupport平面外にあり、零イデアルの一次項が全て消える。Euler式と合わせるとHessian B_pは階数2。R_p=ker B_pは三次元で、G_p=H|R_pは滑らかな平面三次である。gr_m O_Z,p≃Jac(G_p)となる（`ppz:lem:isolated-artin-eckardt`）。G_pの滑らかさは、特異方向aがあればa+tp上で唯一の残りの法微分の二次式に根を持ちXが特異になることから示す。
- H_λ=g_λ+(u³+v³)/3でλ≠0、λ³≠8,−1なら、Hessian階数≤2の点は中心三点とactive九flexの計12点だけ。中心ではG_p=g_λ、flexではG_pがFermat型でj=0（`ppz:lem:hesse-eckardt`）。したがってj(h)≠j(λ),0により、どのπの零スキームもJ_h型の孤立点を持てない。
- 複素数体上のBMMS categorical Torelli Theorem1.1により、Kuが同値な二つの滑らかな三次三様体は同型。別の可換Ku標的も排除できる。ここで使うKu同値は固定h=1で直接構成済みである。

この三様体例では主予想の可換Ku比較が実際に構成されている。自然残余対の被約部分は一致するが、三つの非被約な長さ八局所環が全スキーム同型を妨げる。このため、上の五次元の被約反例とは独立した機構を示す結果として有効である。全対象についての被約版および滑らかな定常点を許す版は、既に上の混合五様体で否定されており、未解決の修正予想としては掲げない。

有限計算は `computations/verify_point_poisson_obstruction.py` にある。T_Qの行列、Hesseの小行列式・Hessian determinant・九flexと中心三点の核と制限三次・一般j差に加え、h=1の正確なj値と中心性、混合二表示の中心性と64根のnormを有理数上で確認する。現行suiteは12 PASS。全locusを尽くすcase分け・任意supportの局所補題・全次数PBW・Ku比較・Torelliは本文の証明であり、有限計算だけで証明したものではない。

### 一般点の実核を複素閉点へ移す手法の適用範囲

固定反例の必要入力ではないが、他の族で一般点上の実核から複素閉点へ進む場合には、正則な非空開U上で相対線束と有限mutationの模型Γ_Uを先に作り、各ファイバーがKu^linを表すことを `thm:nfm-relative-ambient-cy` / `thm:nfm-relative-line-cohomology` で確認する。有限拡大K′/C(h)上の実perfect核があれば、UのK′内の正規化T上へ核・逆・単位・余単位をfinite-cell/retract表示で広げる。`rog:lem:descent` と同様、可換側のsmooth proper性とΓ_Tのproper性により比較coneはO_T-perfectであり、一般点で零なら非空開へ縮めて零になる。その後、各ファイバーのKu^linのsmoothnessを使って `crs:prop:residual-smooth` / `crs:thm:coherent` を適用し、全coherent残余圏と同定する。有限個の開条件を保つ複素閉点を選べるが、指定したh値や元の形式分枝の全jetを再現する主張ではない。

### 二次方程式空間だけからsupportを復元する方法の限界

n=6の滑らかなDはK_D=O_D(1)なのでcanonical embeddingから二次イデアルQを回復できる。ただしQからactive supportを唯一化する単純な可積分方向の議論には障害がある。

q_i(v)=vᵗA_i v、A_iは対称、A_1可逆とし、T_QをA_jv_i=A_iv_j（i<j）を満たす三組の方向の空間とする。v_2=A_1⁻¹A_2v_1、v_3=A_1⁻¹A_3v_1を消去すると、T_Q≃ker K_Q、K_Q=A_3A_1⁻¹A_2−A_2A_1⁻¹A_3となる。K_Qは交代行列なのでdim T_Q≡N mod2。N=8では元のactive方向が非零解を与える以上dim T_Q≥2であり、dim1による唯一復元は不可能である。

明示的なrank6証人はg=(x³+y³+z³)/3+xyz、F=g+xQ_1+yQ_2+zQ_3+G(u)、Q_1=Σu_a²、Q_2=Σa u_a²、Q_3=2u_1u_2+2u_3u_4（a=1,…,5）。K_Qのactive blockは[[0,0,0],[0,0,−7/4],[0,7/4,0]]、中心blockは二つの標準2×2交代blockと零であり、rank6、全24変数の可積分行列rank22を厳密計算した。再現は `computations/verify_point_poisson_obstruction.py`。二つの解が実際に異なる許容supportや滑らかなPoisson標的を与えるかは別問題であり、そこまでは結論しない。

## 2. 入力研究の正確な範囲

## 一般点可換復元の基礎と証明の依存

- **一般性:** \(n\ge3\)、\(R=\mathbb C[h]_{(h)}\)、各次数有限自由な中心三次対を入力とする。剰余は多項式環と滑らかな三次式。任意の良い一ブロック表示に限らない。主定理 `gdr:thm:generic` は \(K=\mathbb C(h)\) 上に可換方程式を構成し、ある有限 \(K'/K\) 上で全coherent残余圏とKuのrotation・指定三次周期付き同値を得る。特殊ファイバーを含む代数的相対同値や \(K'=K\) は主張しない。
- **完備移送:** `cft:thm:complete` は任意の完備noetherian局所 \(\mathbb C\)-底上で有限rank graded MF関手と逆を構成し、内部shift・二つのrank・周期を保つ。これと正則底のwindow（`tw:thm:window`）および一般点でのcoherent飽和（`crs:thm:coherent`）は別の定理。
- **降下:** `rog:lem:descent` では実際のperfect核、逆核、単位・余単位・rotation・周期図式を有限表示で降下する。\(K\) 上に方程式があることはその \(K\)-線型同値核の存在を意味しない。非分裂symmetrizerと可積分行列空間の区別は `gcd:thm:field-model` 及び `gcd:ex:forms`。
- **明示Hesse例:** `gre:thm:exact-potential` の \(\lambda(h)=(h+h^2/3+h^5/12)/(1-h^4/4)\) と固定 \(K\)-三次 \((4-h^4)(x^3+y^3+z^3+u^3+v^3)+(12h+4h^2+h^5)xyz=0\) は全次数の幾何・圏比較を用いる。有限jetの外挿ではない。
- **境界:** 比較核の具体行列と一般的な最小拡大次数、元の固定非可換入力からの低rotation積 \(V,U,\mu\) の全行列、特殊点を含む代数的相対同値は別課題である。追加の高次元の同型類選択・period・Brauer障害はモジュライ・降下稿の残余節を参照。
- **計算:** `computations/verify_complete_curved_transport.py`、`verify_three_object_window.py`、`verify_generic_cubic_descent.py`、`verify_recovery_example.py`。記録済み結果と今回の再実行を区別する。

一次資料の適用差分：Etingof–Ginzburgの有限rank MF、Carqueville–Kayの第二種変形複体、BFKの生成上界、Lin–Zhangの低積、Hwangのsymmetrizer、Pirozhkovの三次 \(n>3\) Torelliは既知。新たな基礎結果の核心は全有限rankの実際の相対MF functor・逆・指定周期、正則windowとの接続、全coherent比較と有限降下であり、初出の網羅確認は未了。

詳細の有効な技術的障害は [可換復元の補助ノート](recovery_foundations.md) に保持する。


古典Poisson論文は `poisson-cubic/papers/poisson-cubic.tex`（A-v62、2026-11-21）を外部入力とする。現在の固定入力はcommit `9f91efa3465f18219c36c31750f1e66220faeaa7`。[正規形の支持節](https://github.com/uedakazushi/poisson-cubic/blob/9f91efa3465f18219c36c31750f1e66220faeaa7/papers/support/papers/sections/poisson_geometry.tex)は、main `288246bca7b703543d24cf6276894dc5467bf1d2` の同ファイルとも全文が同一であることを照合した。量子化の全証明は[cubic-quantizationの主論文](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex)（v1）を正本とする。一般点可換復元の必要証明は主稿の `papers/sections/generic_recovery/` を正本とする。

- 論文A `poisson_geometry.tex`：`prop:pg-represent` の bivector 表示、`prop:pg-jacobi-extension` の affine Jacobi 延長、`thm:pg-normal` の複数 Jacobian ブロック正規形、`cor:pg-generic` の一般三次における被約 Grassmann 錐。全次元の一般 Jacobi スキームの有限長冪零根基を論じる際には最後の被約分類を使う。二次方程式の不足、n=8 の長さ330の定理、およびその直和から作る特殊三次の非零冪零例は、この被約分類に依存しない。
- 孤立Poisson零点の次元制約には、同支持節のHessianの基点自由性、`lem:pg-linearize`、`lem:pg-basepoint-free-lie` の根基排除、`lem:pg-quadratic-lie` のsl₂直和への帰着から `thm:pg-normal` に至る全Poisson正規形を用いる。主張だけでなくこの証明鎖を内部で読解点検した。正規形以降のEuler外積・局所次元・critical方向の線型空間の議論は混合稿の `ppz:thm:isolated-zero-dimension` にあり、未公表入力の内容とその帰結を分ける。外部査読や形式証明器による確認を意味しない。
- 量子化論文 `papers/sections/quantization/general_dimension_universal_quantization.tex`：`thm:pg-all-dimensions`, `prop:pg-ad-relative-chart` が中心量子化の入力。一ブロック相対 PBW 開と中心三次束の存在は、この研究稿と Etingof–Ginzburg の既知の構成から取る。今回その全証明を独立に再検証したわけではない。
- 量子化論文 `papers/sections/quantization/hesse_mixed_universal_center.tex`：`thm:pg-universal-hesse-mixed`、`eq:pg-hm-coefficients`、`cor:pg-hesse-hessian-form`、`eq:pg-hesse-hessian-closed` が全混合中心元と Ψ_λ(F) の有限公式。固定 commit の本文を直接確認し、四次係数を I,J と純中心項へ書き直した恒等式を厳密検算した。中心公式そのものは入力であり、今回の可換記号計算を非可換中心性の再証明と呼ばない。
- 主稿の一般復元節 `papers/sections/generic_recovery/main_result.tex` 等：全 n≥3 が対象。C[h]_(h) 上の次数別有限自由な中心三次対が、多項式環と滑らかな三次式へ特殊化する場合を扱う。一般点の coherent 残余模型は rotation と指定三次周期を保つ。方程式は C(h)、同値核は有限拡大上という区別を守る。全パラメータ・任意の nc cubic・核の基底体への降下を自動的に含まない。
- 主稿の一般復元節の `cft:thm:complete`, `cft:lem:model`, `cft:lem:center`：選んだ formality と厳密同型 φ に対し、残余 potential は W=C_π^(-1)φ(w) である。W mod h=F は W=F を意味しない。`gcd:thm:field-model` は幾何的な可換模型の存在を得た後の方程式の関数体への降下であり、h=0 での正則性や同値核の同じ体への降下を自動的に与えない。`gre:prop:input`, `gre:prop:hesse-normalform`, `gre:thm:exact-potential`, `gre:prop:jet` の split Hesse 公式を全 n の比較例に用いる。固定標的への一般点比較には `rog:lem:localization`, `rog:lem:descent` を使い、線束生成部分から全 coherent 残余圏へ移るには `crs:prop:residual-smooth`, `crs:thm:coherent` をさらに使う。証明全文は現行主稿に保持し、三稿への整理によってそれらの全証明を独立に再検証したとは主張しない。
- 主稿の一般復元節 `papers/sections/generic_recovery/curved_transport.tex` の完備比較は N≥3 を対象とし、`cft:lem:arity`, `cft:lem:flow`, `cft:eq:bound`, `cft:eq:t-weight`, `cft:eq:insertions`, `cft:eq:two-block-matrix` を直接確認した。これに対し `window.tex` の節全体は N≥5 を仮定する。三変数の active 比較は相対 bar 写像の中心係数還元で構成し、一般点生成・window 定理を n=1 へ流用しない。三変数の相対 a=0 比較・proper Hom・Laurent 底変更には `papers/sections/generic_recovery/explicit_example.tex` の `gre:prop:elliptic-quotient`, `gre:lem:elliptic-mf` を用い、正則 DVR と滑らかな active 曲線という仮定を確認した。剰余体と rotation の具体式は Galinat の同じ window1 に統一する。
- 三様体稿 v22 の固定 commit は `6c35d2c84671c2538e61836a6bf3a511392eacce`。任意係数の全 Hom 比較と点スキームの出発点を参照するが、n=3 の形式環を高次元にそのまま転用しない。

古い一般次元ノート中の別リポジトリ名を現行の依存先として使わない。上記の固定 commit と現行稿の参考文献が参照の正本である。

## point/Poisson の補助課題

以下は本文の例と補助的な幾何比較を支える課題であり、可換Ku実現の判定と並ぶ最優先の研究目標には置かない。既知の証明と計算を保持し、公表に必要な依存関係・適用範囲・文献比較を点検する。

1. **孤立零点定理と被約反例の外部検証・新規性調査。** 全Poisson構造への適用は `poisson-cubic` commit `9f91efa3465f18219c36c31750f1e66220faeaa7` の `thm:pg-normal` に依存する。表示・Jacobi延長・Hessianの基点自由性・Lie代数の根基排除を含む入力と、そこからの孤立零点排除・0次元CIの証明を分けて検証する。五様体では全標的を一括して排除でき、実比較核を持つnorm全64根でも不一致が成立する。不一致の証明と実Ku核の証明の依存を分けて点検する。正式な新規性の確認と外部査読・形式証明は未完了である。
2. **三様体の全スキーム反例と実Ku比較を保持・点検する。** h=1の因子、指定Ω、THCR、分離MF積・Picard補正・周期同期、coherent飽和を入口とする。局所長さ8/埋込み次元3からHessian階数2への帰着、12点の制限三次、Mayanskiyの全Poisson分類、BMMSのcategorical Torelliが全標的排除の依存である。形式復元とspreadは必要入力ではない。この例の自然pairの被約一致は有効だが、全対象での被約point/Poisson一致へ一般化しない。
3. **対象を制限した肯定結果の成立範囲を定める。** 五様体の反例は被約な定常点でも不一致が起こることを示す。したがって「定常成分が滑らか」という条件だけでは全対象の一致は得られない。既知の分離型・定常成分を持たない場合を出発点に、一般混合係数でのDとD_Hの抽象同型、偏極・canonical ring、全Poisson標的の可能性を調べる。n6ではK_D=O_D(1)を使えるが、二次netからsupportを一意に回復する方法には交代行列の偶奇障害がある。詳細はノート。
4. **分離型の局所障害から相対・大域比較へ。** m≥2ではJとJ_clのgraded同型が全スキーム同型の必要条件であり、m=2では十分条件でもある。m>2の局所自明性から大域積を推論せず、中心socle θによる厚みを調べる。自然射のscheme imageは(g^{s+1})、Fitting supportは(g^{8^k})で異なる。j多重集合による自然pairの障害を、全π・全Ku標的の排除へ拡張できる範囲を検証する。

関連する正本：`ndc:cor:five-diagonal`、`csp:thm:poisson-zero`、`nft:prop:jacobian-necessary`、`nft:cor:nonclosed-cubic-locus`。回復、Poisson 一致、可換実現の十分性は別問題である。
