# 非可換三次 n-fold：現行研究ノート

2026年11月23日 / v66。研究方針は `../00_research_plan.md`。公表結果の証明は三本の現行論文に置き、このノートは可換復元・モジュライの依存・適用範囲・障害・再現の入口をまとめる。代数的量子化の現行知識は [量子化ノート](https://github.com/uedakazushi/cubic-quantization/blob/main/notes/cubic_quantization.md)、その独立論文は [量子化原稿](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) を参照する。

## 可換 Ku 実現を中心とする研究の入口

主予想は任意の滑らかなnc cubicのKuを同次元の滑らかな可換cubicで実現することである。一つの共有中心変数・任意の固定smooth標準Sklyanin因子の組（k≥2）について、指定境界を保つ全因子別PBW・中心持上げを可換三次と全係数でMorita比較した（`emc:prop:coverage`, `euk:thm:universal-kernel`）。非二捩れの正規化線形Pと二捩れの中心平方βを一次係数tとする。標的はG+uQ(t)+u²(𝔄α+R₂(t))+u³(κc+R₁,₁(t,α)+R₃(t))、𝔄可逆、κ≠0であり、可換smooth開では相対perfect核・全coherent Ku同値を得る。定数3k方向のBocksteinは同型、一次3k方向は単射だが、存在比較は後者を仮定しない。

rank8^kの臨界代数で全係数のsmoothnessを判定する。任意固定tの一般αでは8^k個の相異なる悪いcと、各可換標的の唯一の通常二重点がある。全係数・固定tの判別超曲面は既約被約で、臨界点のaffine空間が正規化を与える。一変数特殊化の重複根は許す。同一S(1,−1,−1)では純ブロックJac₂像・七定数形・κ_k²=27/28を保持し、残る六定数は未数値化。一般因子へこのκ値を流用しない。任意中心数の全因子別表示でK_A smooth ⇔ X_pol smoothを示し、一般中央flagの存在から全smooth対象を比較した。横断二項Bは可逆で、各固定一次係数の一般二次係数では2^(3k+m−1)個の単純悪値を得る。X_polへの実核、因子moduli上の核選択・降下、全intrinsic被覆、h一般点核のdefect零特殊化は残る。指定二ブロックのP64・norm全64根・局所型も保持する。

最高active二次関係が固定したtensor Sklyanin境界で、中心一次変数を厳密に可換に保つ全quadratic PBW表示は、因子間可換を事前に課さなくても元の生成元で因子別に分解する（`ifp:thm:factorization`）。従って、指定中心三次の最高項が非零重みのΣa_iΩ_iである範囲では既存の全許容表示・全smooth比較へ戻る。残る混合問題は境界二次関係自体を動かす変形にある。その次数零一次中心障害を計算し、Clifford因子の中心平方に由来する一組の九方向を、自由な二次代数族と中心正則三次商へ実積分した（`ifh:prop:central-mixed-obstruction`, `ifc:thm:family`）。この周囲代数は全係数で相対Koszul・untwisted相対6-CYであり、複素fiberはAS-regular dimension/index6となる。四・五次元型の原点近傍には実相対smooth proper模型とétale局所perfect Ku核を得た（`ifr:thm:ambient-regularity`, `iff:thm:smooth-neighborhood`, `ifk:cor:clifford-fourfold-neighborhood`, `iff:cor:cubic-fivefold-open`）。四次元には主稿のrotation付きArtin形式認識を用いる。

両Cliffordの双方向十八変数では、周囲のAS-regular領域が正確にresultant開D(Δ)となり、その原点近傍に実残余族・局所perfect核を得る（`ifb:cor:exact-regular-locus`, `ifg:cor:local-comparison`）。二つのτも動かす二十変数族は、各分離点で幾何的20次元形式変形空間を与える（`ifv:thm:versal`）。実étale chartを有限化することで、係数空間の非空開の有限étale被覆上の比較、一般係数体の有限分離拡大上の比較、三次四様体モジュライの稠密開の実現まで得る（`ifv:cor:generic-comparison`）。混合尺度は一般の異なるClifford因子でも三乗を決定し、残る比はθ³=(τ₁³−1)/(τ₂³−1)という非自明な三次被覆で記述する（`ifm:thm:scale-cubes`, `ifm:cor:kummer-scale`）。一方向族の固定切片での二次・三次項は、反転を保つ実核を選んだ場合に未計算の4+8係数へ還元した（`ifj:thm:twelve-coefficients`）。他方、階数一の双方向スライスにはAS正則域内の残余A₂特異点があり、D(Δc)全体を残余smooth locusとすることはできない（`ifd:thm:residual-a2`）。全smooth係数への同じ核の延長と全intrinsic被覆は未解決である。

C上n≥3を基本とし、generic・全固定点・全族・一般体上の降下を区別する。全intrinsic対象の認識やpoint functorの表現可能性は未完成であり、既知の局所表示だけを全対象と定義して済ませない。可換候補の方程式・判別集合・局所特異点の一致と、その候補への実際の比較核の存在も区別する。

point schemeとPoisson零スキームまで同一視できるという素朴な期待は、本文の注意 `ppz:rem:naive-expectation` と不一致の例で扱う。指定混合五様体の定常ノルムの全64根では、smooth properなsourceの点スキームに一つの被約孤立点がある。一方、滑らかな可換三次五様体上の全Poisson零集合には孤立点がないため、Ku比較を仮定せず全可換標的を排除できる。この五様体にも全64根で実際の可換Ku核を構成済みである。三様体の非被約局所環を用いる別の例も、実際の可換Ku同値を持つsourceについての結果である。これらは可換Ku実現から点スキームについて結論できる範囲を示す補助的な例として保持し、独立の予想や修正版を最優先課題として掲げない。

### 三稿の役割と再開する本文

| 正本となる原稿 | 内容と入口 |
| --- | --- |
| [可換復元の主稿](../papers/nc-cubic.tex) | 一般点可換復元、楕円windowとrotationの基礎、分離型の実Ku比較、残余圏の認識・可換実現の開性、三様体の非被約不一致例。 |
| [モジュライ・降下稿](../papers/cubic-moduli-descent.tex) | O-marked認識・全慣性・点とPoissonのモジュライ射、Picard/Brauer/Kummer障害、周期位相、点型と全型の比較次数。主要結果の詳細は `moduli_overview.tex`、証明は各主題の節。 |
| [混合Sklyanin稿](../papers/mixed-sklyanin-cubics.tex) | 中心・局所order・単純加群、固定tensor境界のPBW因子分解と全smooth多中心比較、Clifford双方向族の正則域・二十変数局所完全性と稠密開比較、混合尺度の三次被覆・固定切片の高次係数・周囲正則域内の残余特異点、普遍中心三次、残余Bocksteinの純ブロック像と七定数形、全kの中心尺度、普遍判別超曲面の正規化、零係数の球面接着・有限MF模型、指定h候補の一般点核と整延長、実Ku標的を持つ被約point/Poisson不一致例。本文は `papers/sections/mixed/`。 |

主比較に必要な楕円windowと体上のrotation共役の正本は、主稿の `comparison_foundations.tex` である。`eq:nfm-right-thcr-shift`、`lem:nfm-twisted-elliptic-window` をここから引用し、`csc:thm:comparison` が用いる `mbrc:lem:factor-correction` と分離比較も主稿に置く。相対Picard gerbe、比較核の分類と算術的降下は、これらの実比較を入力とするモジュライ稿に置く。混合族の `cmo:cor:cofinite` は主稿の `grl:thm:open-locus` を使う。稿をまたぐ参照は、定理番号と稿名から証明の所在をたどれるようにする。

point/Poisson不一致は本文の補助例として扱う。三様体の例の証明は主稿の `point_poisson_obstruction.tex`、混合五様体の例と孤立零点制約は混合稿の `mixed/poisson_limits.tex` を正本とする。Introductionはそれぞれの本文を参照し、例のために独立の予想を立てない。各稿の序論は中心問題・主要結果・既存理論との差・適用範囲を述べ、詳細な主張と証明を本文へ置く。

研究方針・研究ノート・共通preamble・書誌は三稿で共有し、数学的な本文は複製しない。三稿への整理は編集と参照の再構成であり、既存の数学全体の再証明ではない。以下の点検・計算に関する記述は各結果の既存の確認範囲であり、今回のソース保持・組版・表示確認とは区別する。実際の確認状態は [検証範囲](validation.md) を参照する。

研究を進める作業単位は、使用する定理・仮定・証明所在・未解決箇所・達成基準を一度に追える範囲とする。固定tensor境界・厳密中心作用の全PBW表示は因子別に分解するので、この範囲の混合関係の分類を未解決へ戻さない。P0は全intrinsic被覆と境界二次関係を動かす表示の認識に置く。Clifford族の階数9・18の残余KS、二十変数の幾何的形式完全性、一般係数の有限比較、一般二因子の尺度の三乗は既知である。次の具体計算は、元の係数を保った七つの一変数族を固定三次切片へ正規化し、二次4・純三次8係数を求めることにある。階数一スライスの厳密な周囲正則域とA₂例を基準に残余smooth locusを調べ、全smooth係数への核の延長を検討する。Δ≡0は既存のsmooth二中心対象では起こらない。偏極標的への実核と全中心作用、因子moduli上のPicard/周期降下も残る。尺度の三次被覆を実核全体の最小定義体と同一視せず、h核の良い特殊化も固定点の同値の存在と分ける。

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

### 中心変数一つの混合型：有限ノルムと自己 Ext

混合稿の `mixed/points.tex` にある `cmo:thm:point-norm` は、R=C[u]上のk因子をtensorし、二次関係にuが実際に現れる型を扱う。u=0で滑らかな固定点なしの楕円グラフを持ち、可換化の三つの二次式の最高active部分が正則列という仮定の下で、全可換化TはR上階数L=8^kの有限自由加群となる。C=Proj Tはu≠0に入り、Q=T/(u−1)と置けばC=Spec Q。中心三次wの像bに対し

\[
\operatorname{Pt}(B/(w+cu^3))=\coprod_iE_i\amalg\operatorname{Spec}(Q/(b+c)),
\qquad N(c)=\det(cI+m_b)
\]

であり、定常成分が現れる係数はmonic次数LのNの根に等しい。普遍加群のFittingイデアルも(N)。これは各例外値でsourceがcoherently smoothだという主張ではない。

具体例 `cmo:ex:sixty-four` は、[y,z]=x²−α_1u²と巡回置換、α=(1,4,9),(16,25,49)を用いる。中心元は Ω_α=(x³+y³+z³)/3−(2/3)sym(xyz)−u²(α_1x+α_2y+α_3z)、w_c=Ω_α+100Ω_α′+cu³。中心性は三つの独立パラメータを保った普遍関係行列で確認する。全次数PBW性はBraverman–Gaitsgory Main Theorem0.5 / Lemma3.3により別に証明し、次数3,4のHilbert関数だけから推測しない。u=0ではΩ_0=−c_3/3（De Laet–Le Bruyn §2の規格化）であり、中心和の正則性はuによる次数下降で持ち上がる。

Q=C^{64}であり、R={±28,±16,±56/3,±28/3}、S={±448,±196,±176,±284/3}と置くとN(c)=∏_{r∈R,s∈S}(c+r+100s)。全64根は相異なる有理数で、各根では一つの被約定常点が加わる。根以外、特にc=0では点スキームは二つの楕円曲線だけ。このnorm根集合とc=0のsourceは、下記の正確なP64判定によって全てsmooth properと確定した。P64で得る非smoothな64係数とは交わらない。滑らかな中心変数一つのブロックJacobian可換標的の零スキームが純楕円曲線だけとなること（`cmo:prop:poisson-zero`）に加え、全Poisson構造を扱う `ppz:thm:isolated-zero-dimension` により、norm根では任意の滑らかな可換三次五様体上の被約零スキームとの同型が不可能である（`ppz:cor:reduced-point-poisson-counterexample`）。この排除は可換Ku比較核を必要としない。`cmo:cor:norm-commutative-kernel`によりnorm全64根でも明示X_cへの実perfect Ku核を得た。従ってこの被約不一致例は、実際の可換Ku標的を持つ。

`cmo:prop:character-ext` は、u=1の一因子D_pとcharacter p=(a,b,c)∈(C×)^3について、中心元からその値を引いた f_p=Ω_p−λ_p の高次作用を

\[
\lambda_p=-\frac23(a^3+b^3+c^3+abc),\qquad
\kappa(p)=\frac{2((ab)^3+(bc)^3+(ca)^3+9a^2b^2c^2)}{9abc}
\]

で決定する。D_p/(f_p)上の自己Extを計算するcochain複体は、|t|=2、|η|=3、dη=κ(p)t²を持つ C[t]⊕C[t]η。これはYoneda積の同定ではない。κ≠0ならExtは次数0,2のみ、κ=0なら非有界である。中心元の係数sはこの高次作用にs²として入る。証明は長さ三のPBW/Koszul分解、普遍的な二段のhigher homotopy、C[t]上の有限消去を使い、完備化・有限次数からの外挿は使わない。全多項式証明書は `computations/verify_mixed_character_ext.py` に収める。

二因子の中心和では dη_1=κ(p)t²、dη_2=10000κ(p′)t²。全16因子characterについてκ≠0は324>251と176400>72827で示せるので、全64例外点の自己Extは次数0,2,3,5に各一次元で、それ以外は零（`cmo:cor:sixty-four-ext`）。さらに `cmo:prop:character-pd` は有限ambient分解・Rees同型・Shamash二周期性を使って、そのaffine射影次元が正確に5であると証明する。一般のk因子では、一つでもκ≠0ならpd=3k−1、全κ=0ならpd=∞。有限自己Extだけから射影次元を推論する一般論ではなく、全加群・対角のsmoothness判定とも異なる。

κ=0は有理点p=(3,−3,1)、α=(9,9,1)で実現し、λ_p=16/3となる。同じ係数の二因子を係数1,100で合わせ、c=−1616/3とすると、対応するcoherent点の自己ExtのHilbert級数は (1+s³)²/(1−s²) である（`cmo:prop:rational-singular`）。中心chartのfd加群をπ(M[u])へ延ばすと、exactなj_*と大きいQGrでの単射分解から全次数Extを比較でき、Positselski–Schnürer Proposition2.1でcoherent部分へ戻せる。従ってqgrのhomological dimensionは無限、Db(qgr)は非proper、線束生成圏とその残余部分は非smoothである。全Db(qgr)のdg smoothness単独の否定とは区別する。このsourceは滑らかなnc cubicの仮定を満たさず、主予想の反例ではない。

同じαの八characterにはκ=0が四個あり、λ=±16/3が各二個。二因子の両κ=0となる16組は c=±1616/3,±528 に各四点ずつ分かれる。残り48組はpd5である。検証器はこの全組合せも厳密確認する。以前の別候補 a=b=1, 2ρ³+9ρ²+1=0, c=ρ でもκ=0となるが、混合稿の障害例には上の有理例を使えば十分である。

### 二次元単純加群と中心方程式の高次作用

`cmo:prop:two-dimensional-classification` では、X=aI+U等と跡零分解し、既約性からU,V,Wがsl₂の基底になることを示す。半跡はq(a,b,c)=α、abc≠0を満たし、この条件は十分でもある。q(q(p))=F(p)p、F(q(p))=F(p)²、F(p)=a³+b³+c³−3abc。F(α)≠0ではq(α)の全座標が非零ならちょうど2類、半跡はq(α)/√F(α)。F(α)=0でq(α)≠0なら存在せず、q(α)=0の非零係数ではC*から6点を除いた曲線、α=0では3本のC*となる。Waltonの公刊稿Proposition4.1は斉次α=0の存在、§5.2は一般変形の分類を課題としており、ここで扱う具体的分類の新規性は未確定。

指定中心の値はλ₂=−2(a³+b³+c³+abc)/3。一次変形の正規形を双対数環上で取るとExt¹=ker Dq、det Dq=−2Fとなり、3CY双対から全ambient自己Extを得る。F(α)≠0では0,3次のみ各1。中心商のpd判定には高次作用κ₂が別に必要で、rank(2,6,6,2)の自由分解から全Shamash恒等式を解き、identity/trace規格化で二段消去する（`cmo:lem:two-dimensional-shamash`）。普遍式は `cmo:prop:two-dimensional-universal-kappa` の

\[
\kappa_2(a,b,c)=-\frac{2N_6(a,b,c)}{9F(a,b,c)},\qquad abcF(a,b,c)\ne0,
\]
\[
N_6=a^6+b^6+c^6+66((ab)^3+(bc)^3+(ca)^3)
 +26abc(a^3+b^3+c^3)+153a^2b^2c^2
\]

である。`--universal` はc=−1/b,r=1の表現をQQ(a,b)上で計算する。これは補間ではなく、全homotopy恒等式と二段消去の有理関数恒等式である。相対複体のconstant rank、identity/traceによる両端の自明化、最初のchange-of-rings微分の選択独立性からκ₂はabcF≠0上正則であり、補助的な分母の零点にも延長する。N₆≠0なら単因子中心商上pd2、N₆=0ならpd∞。F=0でのκ₂判定はこの式の適用範囲外である。

`cmo:ex:two-dimensional-zero-action` は、a³−2a²−11a+8=0、半跡(a,1,−1)、α=(a²+1,a+1,1−a)、λ₂=−2(a³−a)/3の例を与える。N₆(a,1,−1)=0であり、剛的な二次元simpleが自身の中心商上pd∞となる。同時に全8 characterは自身の中心商上pd2で、λ₂にはcharacterが一つもない。`--zero-example` は三次数体で全高次homotopyを再計算し、8次有限エタール可換化上の二つの乗法行列の行列式と互除法から後二条件を検査する。従ってcharacterだけの検査を二次元判定が実質的に強める。

指定二因子ではκ₂≠0を数体で厳密検証した。各因子の8 charactersと2二次元simpleの全100tensor simpleは、互いに異なる100中心値に現れ、pd5、自己Extは0,2,3,5次各1、coherent延長は線束perfectである。この百加群の検査自体は全体のsmoothnessを含意しない。指定因子の全simple分類と全体判定は、下記のNCCR局所形と対角の証明で別に得る。

### 定数型混合族の有限中心と余有限Ku実現

`cmo:thm:finite-center` は、斉次入力をS(1,−1,−1)に固定した定数型変形の全α∈C³を扱う。中心生成元はΩ_αと三つの六次元C_0,C_+,C_-であり、斉次化ではさらにuを加える。C_0=z(z²−α_3)(xzy+α_1x+α_2y)+α_1α_2z²、C_+の全式とC_-の反自己同型による定義は混合稿の `mixed/centers.tex` に置く。検証器 `verify_mixed_pi_center.py` は三パラメータを独立な重み二変数に保ち、QQ上の全二側関係倍で中心性を検証する。重み6,7の商の次元は119,189、最高部Ω_0²,C_0,0,C_+,0,C_-,0の独立性は小行列式−4/9で確認する。

全次数の生成性はSmith–Tate Theorem3.7（3|nも含む）によりZ(S)が次数3と三つの次数6で生成されることを入力とする。したがってZ(S)_6の次元は高々4で、上の四元が全基底となる。全生成元が持ち上がった後にfiltered次数帰納、斉次化では同論文Lemma3.6を使い、全中心の生成とmodule-finitenessを得る。同じ有限生成語を係数族でも用いるため、点ごとのPI性の外挿ではない。

一次比較は [Walton学位論文](https://math.rice.edu/~notlaw/thesis.pdf) DefinitionV.1・RemarkV.16（印刷pp.113–114,123–124）。そこで提案された位数六の中心持上げのうち、斉次パラメータ(1,−1,−1)、線形補正d_i=0、定数補正e_i任意の部分族を具体化した。全位数六パラメータや一般の線形補正はこの有限中心定理では対象外。Smith–Tateの中心定理やPBW理論自体の新規性は主張せず、具体式の初出・後続研究との網羅的照合も未完了である。

`cmo:prop:contraction` のR=C[t]族はα_i↦t²α_i、中心式Σa_iΩ_(t²α_i)+u³で、t=0は分離型、t≠0はv=tuにより元のc=t^(−3)族と同型。次数別自由性・有限線束生成・proper残余模型Γ_Rは `cmo:prop:proper-contraction`。`cmo:thm:relative-smoothness` は次の入力で対角を証明する。

1. 普遍中心元の像が生成するC_R⊂A_RはR上torsionfreeでflat。重み1,3,6の六次VeroneseでZ=Proj C_R^(6)を作り、coherentな有限代数𝔄へsheaf化する。
2. 次数一生成により、中央斉次元を反転した環は強Z次数付き。従って全O(j)は𝔄上局所射影であり、有限線束和Eが全非有界qc導来圏をcompactに生成する。
3. Z×_R Z上のΛ=𝔄^op⊠𝔄とM=Δ_*𝔄はcoherentかつRflat。E^∨⊠EによるMorita同値で、Mが線束模型Σ_Rの対角に対応する。Künnethと評価は両側作用まで保持する。
4. 特殊ファイバーのM_0は分離型比較からperfect。中心局所環のt進完備化、idempotentの持上げ、忠実平坦降下により、その近傍でMの有限射影次元を持ち上げる。非perfect locusは閉で、そのproperな射影像は0を含まない。従って0の近傍の相対対角はperfectで、残余Γもsmooth properとなる。

`cmo:cor:cofinite` はn=3k−1≠4の可換実現locusの開性を適用し、任意の固定α_iと非零a_iについて、有限集合Fを除くcで全coherent Kuを可換実現する。この一般kの結果を保持する。固定した二つのS(1,−1,−1)因子・重み1,100では、`cmo:cor:all-alpha-central-kernel`がさらに明示標的X_(α,c)のsmooth開全体で実比較を与える。指定αの全coherent比較から除く必要がある係数は正確にV(P64)であり、normの64係数とc=0は除かれない。一般kの例外集合の全体や、その各点での明示標的比較をこの二因子結果から結論しない。

別経路として、D=⊗D_{α_i}は有限大域次元の有限中心代数なので、c↦−Σa_iΩ_iという中心作用でRennemo–Segal–Van den Berghの非可換Bertini（[arXiv:1705.01366v2](https://arxiv.org/abs/1705.01366)、Proposition2.1）を適用すると、一般cのaffine中心chartの有限大域次元を得る。R=C[c]の作用は最高active部分の正則性により忠実である。このaffine結論だけから全qgrや可換Ku比較を推論しない。混合稿の余有限Ku比較は上の射影的対角と収縮を使う。二中心変数の [補助ノート](central_cubic_generic_smoothness.tex) は別の仮定を持ち、一般のPBW変形へ有限中心性を無断で流用しない。

### 有効な中心幾何、Azumaya性、norm外の64非smooth係数

`cmo:prop:center-hypersurface-degree` はSmith–Tate Theorem4.8とfiltered次数帰納により、全αで Z(Dα)=C[s,U,V,T]/(Pα(s²,U,V,T)) を与える。Pαの全次数は3、最高部は81W²U+468WU²+784U³−36WVT−176UVT+16V³+16T³、W=s²。全体符号反転によってsは偶数冪だけにできる。中心とDのHilbert多重度の比は36で、PI次数6を得る。指定二係数の21項の全関係は本文の表と再現コードに一度ずつ収録する。

`verify_mixed_center_geometry.py` は次数n−1の基底語×一文字から一段ずつ正確な商を作る。実際の関係倍で割った次元が既知PBW次元に一致するので、その乗法表は正しい。次数18でも仮の最高部分513列、全語代表1330個で足りる。中心の35単項式の核は1次元。さらにI=(P,P_U,P_V,P_T)の商は長さ18、Wへの消去はWH(W)²Q(W)。Hは五つの一次因子、Qは四次既約で、全係数は本文に置く。各中心の特異点は14通常二重点（H上10点、s=0上4点）、sの特異ファイバー値は19個、Q(s²)=0上の8点は正則中心上のMorse臨界点である。長さ・消去・被約性・Hessian単元性は全てQQ上の厳密計算による。

`cmo:thm:azumaya-regular` は全αでAzumaya locus＝正則中心を証明する。Dαは3CY・全simple有限次元なので全simpleのpd3、従ってhomologically homogeneousで、中心normalと中心上CMを得る。斉次化Bαの全中心TについてT/(u)=Z(S)。u=0上のAzumaya性を自由加群の基底とNakayamaで持ち上げる。Bad(Bα)の余次元1成分があれば斉次閉錐のu=0切断は次元2以上となり、Walton–Wang–Yakimov Theorem1.3(1),Lemma5.4の3曲線に矛盾。余次元1AzumayaとBrown–Yakimov Corollary5.2から結論する。有限中心性だけでregular=Azumayaとする一般論は用いない。

`cmo:thm:morse-singular-sixty-four` は P64(c)=pp₊Res_z(Q1((-c−100z)²),Q2(z²)) を定める。64次、偶、平方因子なし、P64(0)≠0、gcd(P64,N)=1。根の全てで36次元simpleを持ち、その完備局所中心商はMat36(C[[v1,…,v6]]/(Σv_i²))となる。自己Ext級数は(1+s)⁶/(1−s²)、coherent延長も同じ。有限中央台から逆方向Extもchartで計算でき、RHom(𝒫,O(i))=C³⁶[−5]。例外射影Kの自己Extは十分高い全次数でC³²となり、全coherent Ku自体が非properである。線束圏と残余線束圏は非smooth。全Db(qgr)のdg smoothness単独の否定は主張しない。

巨大なP64の係数全文は保存せず、resultantから再生成する。最高次から定数項まで65整数をASCIIコンマで結び改行なしの6910 bytesのSHA-256は `20923491b92e21c3fceb0b30b0f331e500d83f898f756d0cb853ace75de42dbb`。この64根はnormの64根からすべて異なる。次の局所・射影対角の証明により、指定族の非smooth係数はこの64根だけと確定した。

### 全節点の局所代数、全simple、正確なsmooth locus

`cmo:lem:formal-node-brauer` は R=C[[x,y,z,w]]/(xy−zw) の穿孔スペクトラムUのBr′(U)=0を示す。小解消Yの例外曲線P¹、Česnavičius Theorem1.1の純性、strictly Henselian底上のproper base change、Kummer列を使う。解析的なlinkだけから代数的Brauer群の消滅を推論しない。Azumaya分裂束を反射的に延長し、Hartogsから局所orderをEnd_R(M)と表す。完備化後の有限global dimensionを単純加群の解消とminimal resolution/Torで確認した上で、Iyama–Wemyss Lemma2.23・Proposition4.5・非generatorも含むTheorem5.20を適用する。

`cmo:thm:fourteen-node-orders` の結論は実際のR-代数同型 End_R(R^{⊕a}⊕I^{⊕b})、I=(x,z)、a+b=6である。共通のrank1 reflexive twistはEndそのものを保つ。8個のcharacter中心では(1,5)、2個の2次元中心では(2,4)、Ω=0上の4点では(3,3)。従って各因子の非Azumaya simpleは28類、次元1,2,3,4,5の個数は8,2,8,2,8。正則中心の各点には6次元simpleが一つある。具体的な3〜5次元行列を列挙せず、中心点と局所orderの二つのsimpleで同型類を完全に記述できる。

`cmo:prop:conifold-nonisotropic-slice` は中心関数fの一次項がdual quadratic formで非等方なら、Λ/(f)がC[[p,q]]⋊μ₂と同型、global dimension2になることを示す。高次項は任意に許す。R/(f)はA1、I/fIは非自由rank1 CM、両辺の反射性からEndの底変更を確認する。形式的対角は完成包絡環上の差Koszul分解と平均化で扱う。形式冪級数環の通常のC上tensorをsmoothとしない。`cmo:lem:all-nodes-nonisotropic` の追加入力は J=(P,P_W,P_U,P_V,P_T) 上の3変数Hessianの単元性であり、既存中心検証器に統合した。全28節点で非等方性を厳密確認した。

`cmo:lem:relative-diagonal-from-slice` は有限中央模型の対角点で完備化し、中央パラメータの正則性、syzygyの射影持上げ、忠実平坦降下から代数的な相対対角を得る。混合和には `cmo:lem:mixed-relative-diagonal` を使う。一方AがC=C[s]上相対smooth、他方Bが絶対smoothなら、R=A⊗_C B、T=A^op⊗_C Aに対し N=R^e⊗_{B^e}B≅T⊗_C B はR^e-perfectであり、Aの相対分解をN⊗_T−で移す。相対projective項を無条件にR^e-freeと扱わない。

`cmo:prop:projective-boundary-smooth` は任意の定数型α、非零a_i、k≥2、全cでu=0の境界対角がperfectと示す。六次中央chart L=A[f⁻¹]にQ=L/(f−1)を取り、強Z/6次数付けとQ⋊μ₆≅End_{L₀}(Q)を使う。uはQでは中心元だがL₀の次数零元ではないため、L₀/(u)とは書かない。Q/(u)は既存の分離境界の有限巡回模型でsmooth。u正則性は直接の消去で確認し、通常の中央対角持上げ・有限群平均化・Moritaで境界へ降ろす。

以上とMorse点の局所計算から、`cmo:thm:exact-sixty-four` は指定族について P64(c)≠0 ⇔ affine対角perfect ⇔ 線束圏smooth ⇔ 全coherent圏smooth proper ⇔ coherent Ku smooth proper を与える。qgrのhomological dimensionはこの場合5、P64の根では∞。`cmo:cor:fixed-zero-norm-smooth` によりc=0とnorm全64根はsmooth properである。

同じ二因子と重み1,100の任意のαについて、残余線束圏のsmoothnessは明示可換三次X_(α,c)の滑らかさと同値になった（`cmo:cor:all-alpha-central-kernel`）。可換側がsmoothなら全coherent圏への飽和とKu同値も得る。これは一般αの中心の節点数、全simple、局所orderの分類を完成したという主張ではなく、それらの局所解析は残る。指定αでは元c族の全smooth係数とnorm全64根の比較を実相対核で構成済みであり、DVR特殊化や開性・連結性だけによる全体性の推論を用いない。一般的なBrauer純性・NCCR分類は既知結果であり、本例の具体的結論の新規性の網羅的確認は未了。一次文献・定理番号・識別子は混合稿Introductionと共有書誌 `papers/references.tex` に置く。

### 同じ判別集合を持つ明示可換三次族

α^(1)=(1,4,9)、α^(2)=(16,25,49)、λ=2√21/9、λ²=28/27とし、

\[
G_\alpha(x,y,z,u)=\frac{x^3+y^3+z^3+xyz}{3}
 -u^2(\alpha_1x+\alpha_2y+\alpha_3z),\qquad
X_c=V\!\left(\lambda(G_{\alpha^{(1)}}+100G_{\alpha^{(2)}})+cu^3\right)
\subset\mathbb P^6
\]

と置く。`cmo:prop:commutative-critical-spectrum` は、f_α=G_α|_(u=1)の八次元Jacobi環J_αが被約で、八臨界点が全てMorse型、臨界値も相異なることと、

\[
\det(t-\lambda m_{f_{\alpha^{(i)}}})=Q_i(t^2)/3^{17}
\]

を証明する。Q_iは非可換中心の正則点上のMorse臨界値を与える同じ四次多項式であり、近似した臨界値の比較ではなく有理係数の全恒等式である。八次元Jacobi環の乗法行列から終結式を作ると、既存P64の65係数と正準hashが一致する。再現の入口は `computations/verify_mixed_commutative_candidate.py`。

`cmo:thm:commutative-discriminant-candidate` により、X_cが滑らかであることとP64(c)≠0は同値。P64の各根では特異点は一つで五次元通常二重点となり、非可換側の該当完備局所中心商はその局所環上のMat₃₆である。u=0の射影境界は全cで滑らか。従ってc=0とnormの64根にも滑らかな候補を得る。自然なブロックJacobian Poisson tensorの零スキームは、smooth locus全体で二つのHesse曲線E₁⊔E₂である。

**元c族の全smooth係数で、この指定X_cへの実比較が成立する。** `cmo:thm:all-central-commutative-kernel`は全C[c]上の残余線束圏のMorita双加群を構成し、U=A¹∖V(P64)上で相対perfect核とする。全c∈UでKu_coh(A_c)≃Ku(X_c)となり、一般点、c=0、norm全64根を含む。特異係数でも比較するのはproperな残余線束圏であり、全coherent圏や相対積上perfectな核をそこへ無条件に延長する主張ではない。判別集合は核を構成した後で尺度λを決定するために用い、同値存在の代用にはしない。

### 中心超平面の三項復元と全α,cの実比較

正本は混合稿の `central_spherical_reconstruction.tex`、`central_formal_comparison.tex`、`central_kernel.tex`。二つのS(1,−1,−1)因子と重み1,100を固定し、T=C[α¹,α²,c]全体のproperな残余線束模型を作る。active filtrationの随伴代数はS⊗T[u]であり、固定内部次数で有限な濾過から次数別自由性を得る。特異係数でも使うのは線束生成部分であり、全coherent圏のproper性を仮定しない（`cmo:lem:central-universal-line-model`）。

中心超平面u=0への制限Fのtwistはρ_S²、unshifted cotwistはρ_A⁻¹[1]で、三乗はそれぞれ[4],[1]である。proper性とこの周期からFと右随伴の像のsplit-generationを証明する。A/(u²)=S[u]/(u²)なので一次Bocksteinは零、余単位付きunderlying comonadはK=Id⊕J、J=ρ_S²[−1]に一意的に分裂する。分裂だけから全余乗法は決まらない。BFKのsector式と固定counitのA_n障害塔により、非空な各段の選択空間はarity二でJac(G)₁=C⁶、三でJac(G)₀=C、四以上で可縮となる（`cmo:prop:central-comonad-three-arity`）。任意の低次データの存在障害を一律に消したという主張ではなく、双方に実在する全comonadの比較を延ばす。

二項はv=u²変形のBockstein b(α)である。二列法線Koszul解消における閉じた奇数作用素ξの平方がBocksteinを表す。境界比較をHeisenberg作用とブロック交換に両立させると、二項の像は共通の非零定数βを用いてβLとなる。三項torsorには法線符号反転の唯一の固定点を原点として取り、全T上の正則性とwt(α)=2,wt(c)=3から三項はγcに限られる。中央rank一MF(u,cu²)の法線Massey積が±c·Idとなること、および原点のnon-smooth射影錐と既知のsmoothファイバーを比べる独立な検出により、γも非零である（`cmo:lem:central-universal-parameters`、`cmo:lem:central-ternary-nonzero`、`cmo:rem:central-nonzero-smooth-test`）。普遍正則性を欠く局所Artin変形だけでは、α⁴/c²のような有理補正を除けない。

Jのr倍によって二項・三項はr²,r³倍される。r²β=1とし、κ=r³γ≠0とすれば、まず全α,cでG−u²L+κcu³の残余線束圏への実Morita比較が得られる。全coherenceを持つcomonadの比較から生成代数RHom(KG_S,G_S)のcoKleisli積・高次構造を比較し、graph双加群と逆双加群を構成する。次に指定αの全cでMorita不変なsmoothnessを比較する。P64の根の二次モーメントは10260312863360/243≠0なので、その根集合を保つscalarは±1に限られる。これによりκλ=±1、λ²=28/27と決まり、符号を正規化して指定X_cへの核を得る。判別式から同値を推測する順序ではない（`cmo:lem:critical-spectrum-scaling`、`cmo:thm:all-central-commutative-kernel`）。

全C[c]上、さらに全T上の構成は実Morita双加群・逆・unit/counitを含む。可換族が滑らかな開では相対積上perfectで、任意の導来底変更が同値を保つ。各複素ファイバーではcoherent飽和によりKu_coh(A_(α,c))≃Ku(X_(α,c))となる（`cmo:cor:all-alpha-central-kernel`）。一般の非正則基底上の全Db(coh)まで同定したわけではない。特異係数の線束圏間のMorita双加群については、両側の対角や積上perfect性を主張しない。

幾何的な一次変形の再開データは `central_geometry.tex` に置く。X₀の対合負固有のHH²は十次元であり、対合だけではcu³の像を一つの直線へ絞れない。L=ℓ、G=g+ℓQ、t=v−Qとすると、Knörrer核の明示homotopyによりcotwistの単位fiber射の乗法vはQ|_(ℓ=0)へ移る。この同じ二次式は(Jac(G−u²L)₃)⁻≃Jac(g)₂の下で[u³]に対応し、指定係数で非零である。これらの接空間計算は全核の証明を代用せず、その具体的な作用と今後の変形比較に使う。

`python3 computations/verify_mixed_central_direction.py` は、Knörrer座標式とhomotopy、非零Jacobian類の6×6小行列式、P64根の二次モーメントとmonic係数、中央MFの三項Massey恒等式、重み三の単項式を厳密に再現する（7 PASS）。計算成功は全圏同値・生成性・全障害塔の形式証明ではない。新しい核の証明は本文と独立読解によるもので、組版・表示・保存の確認状態は `validation.md` を正本とする。

### 任意ブロック数の中心比較と判別行列

正本は `mixed/multiblock_central_kernel.tex`。境界の変数数N=3kに対し、中心超平面制限のtwistはρ²、cotwistはρ_A⁻¹[1]のままである。非恒等μ₃ sectorの条件はa≡N mod2, 2b+3a=N。正規化A_r塔へ代入すると6−2r−3i=Nまたは5−2r−3i=Nが必要になり、r≥2,i≥0,N≥6で不可能となる。従って二項Jac(G)₁=C^(3k)、三項C以外の比較の自由度は消える。既存の実全構造の比較を延長するのであり、任意の低項データの存在障害を消してはいない（`cmm:lem:all-block-sectors`）。

同一のPicard補正・Heisenberg線型化・周期補正を全因子に用い、全Λ_k次数とsplitting変更の文字twistを保つ。特に3|kで因子置換不変なrotation分裂を仮定しない。各ブロックのBocksteinの独立性と因子置換から二項はβ_k L、重みと法線符号対合から三項はγ_k cとなる。双方非零なのでJの尺度を正規化して(L,κ_k c)を得る。全α,cでcoKleisli代数を比較し、可換smooth開では相対perfect対角とcoherent飽和へ移る。固定重みはt_i³=a_i, x'_i=t_i x_i, α'^(i)=t_i²α^(i)で処理する。動く重み上の核降下は別問題である。

中心尺度は `mixed/multiblock_scale.tex` の `mcs:cor:universal-scale` により、全k≥2でκ_k²=27/28となる。符号を選べばκ_k=κ=3√21/14、λ=κ⁻¹=2√21/9と揃う。一因子α₀=(1,4,9)の正則中心にある八個のAzumaya Morse点を尺度変更してk個組み合わせると、8^k個の相異なる中心係数でMat_(6^k)(通常二重点)を得る（`mcs:lem:azumaya-morse-detection`）。剰余simpleの全自己Extとcoherent飽和判定が残余線束圏の非smoothnessを検出する。既に構成した実Morita比較と可換側の判別次数により、これらの悪い係数の包含が集合等号となり、非零な二次momentがκ_kを較正する。

この較正は、比較核を構成してからsmoothnessを用いる順序であり、判別集合の一致から同値存在を推測していない。また、二ブロックの通常同値を追加因子へ無条件にtensorすることも用いない。異なるブロック数の間で核・rotation・指定周期を同時に保存する比較は別の強化問題であり、中心尺度の数値決定とは分ける。

各因子の臨界代数Q_i=C[α][x,y,z]/(x²+yz/3−α₁,…)は平方自由基底のrank8自由加群である。Q=⊗Q_i, H=−(2/3)Σa_iα^(i)·x_iとすれば、det(κc I+m_H)の非消滅が可換smoothnessと残余線束圏のsmoothnessの必要十分条件となる。κを上記の値に固定すれば、定数型族の元c座標での判別行列は全て指定される。零点の重複度は局所臨界代数の長さを含み、α=0では(κc)^(8^k)となるので悪い係数は一つしかない。一般αでは正確に8^k個の相異なる悪い係数があり、各可換標的は唯一の通常二重点を持つ（`cmm:cor:generic-nodal-discriminant`）。各α^(i)=t_i²(1,4,9)の臨界値がt_i³倍されることと有限個の衝突の回避を使う。三ブロックの八様体では512個となる。`verify_mixed_multiblock.py` の9 PASSは普遍乗法・有限恒等式、八臨界値の相異性・Hessianの非退化性、一因子中心多項式とのλ²=28/27の一致を厳密確認する。全kでの包含・較正の証明は本文を正本とする。

### 線形補正の正規形、中心元と残余Bockstein

正本は `mixed/linear_pbw_boundary.tex`。関係式[y,z]=x²+Σm₁ⱼxⱼ−α₁と巡回式に対して、唯一のKoszul重なりとR∩Λ²V=0からPBW性はM=Mᵗと同値である。X_i=x_i+t_iへの変更はM'=M−2diag(t), α'=α+Mt−t²となり、t_i=m_ii/2が唯一の対角零正規形を与える。この一意性は指定された斉次Sを保つ平行移動に関するもので、全自己同型による分類ではない。

正規形の三つの線形係数p,q,rと三つの定数αに対し、Ω=Ω₀+uQ_nc+u²L_ncを明示した（`mix:thm:linear-pbw-central-cubic`）。Q_nc=p(sym₂(xy)+z²/18)+q(sym₂(yz)+x²/18)+r(sym₂(zx)+y²/18)、L_ncのx係数はq²/6−pr/18−α₁で、y,z係数は巡回する。添字ncは可換比較標的のQ,Lと区別するためである。中心性は普遍係数を保持する162×339の有理関係行列、階数144で三交換子の厳密な零剰余として証明する。Z(S)₁=Z(S)₂=0により、最高部Ω₀を持つ中心三次の自由度はscalar·u³だけである。任意kの中心和は正則で、商は全係数で次数別自由、Hilbert級数(1−t³)/(1−t)^(3k+1)となる。

Koszul複体の内部次数−1成分はC³→Mat₃(C)→S₂であり、二番目の微分の核は対称行列、最初の像は対角行列となる。従ってHH²₋₁(S)=Sym₃(C)/Diag₃(C)≅C³である。これらの方向は多ブロックの中心商でも消えない。ただし、この代数の結果だけでは残余圏への単射性は従わない。定数補正に用いたaugmentationでは、今回の一次関係係数と中心の二次係数Q_ncはactive原点で消える。中心元の一般存在とPBW理論はEG/BGの既知入力であり、本表示の明示式の網羅的新規性は未確認である。

`mixed/linear_bockstein.tex` の `mix:thm:linear-bockstein-injection` は、この障害をfull Hochschild cochainで処理する。二項自己交叉の双加群classをA/(u²)の乗法cocycleとbar上で同定し、Lowenのbrace写像を用いて持上げ自由複体のdg変形へ移す。相対Koszul–Shamash模型を、双加群自己交叉から来る中央周期作用素tで導来局所化すると、実際のunary微分はδ₁(ξ_j)=−Σ_l m_lj ξ_l²となる。中心のuQ_ncはこのunary成分には寄与しない。通常Extの数値だけでTate模型へ外挿した主張ではない。

最小模型のarity oneでは、任意のnullhomotopyの寄与は[m₂,h₀]だけである。双次数(1,−1)の零項primitiveは、tの負冪を許してもF₁t⁰しかない。隣接する二対象の独立なh_L,h_Rを許したgauge行列は対角＋交代行列をなす。一方δ₁は対称対角零なので一致は零の場合に限られる。これによりb₁:C^(3k)→Jac(G)₂は単射、ν=0 iff p=0となる。rotation不変homotopyだけに制限した結果ではなく、通常残余圏の全coherent自然変換の単射性である。各κ(a)上の値が零であることと、全自然変換が零であることを区別する。証明全文は上記節を参照する。

### 非分裂comonadの普遍比較と具体化の入口

正本は `mixed/linear_comonad_comparison.tex`。J=ρ²[−1]、K_η=fib(Id→ηρ²)とし、U_r=RHom(Id,J^r), W_r=RHom(J,J^r), N_r=RHom(K_η,J^r)を使う。d=2−r−iでは長完全列のH^(d−1)W_rとH^dW_rがともに消えるので、H^dN_r≃H^dU_rは全ηの普遍係数上でも自然に成立する。二項Jac(G)₁、三項C以外は零で、全higher homotopyも消える。N_r複体全体がηと無関係とは主張しない。各非空fiberを比較しており、任意の低項データの存在障害の自動消滅も主張しない。

可換族G+uQ+u²L+u³dのtwist射は−[Q]である。固定線型切断で実際の非可換η(p)を実現し、可換族G+uQ(p)を二項構造の参照点に取る。二項を合わせた可換族を次に三項の参照点とし、原点を持たないtorsorの差を順番に測る。普遍proper模型と固定境界複体のC線型縮約から差は多項式であり、法線の重み(p,α,c)=(1,2,3)により

\[
L(p,α)=-\sum_i a_iα^{(i)}\cdot x_i+R_2(p),\qquad
C(p,α,c)=κ_kc+R_{1,1}(p,α)+R_3(p)
\]

となる。p=0の既知比較がα,cの係数の非零性を保証するため、(p,α,c)→(p,L,C)は三角な多項式同型である。四項以降の比較を延長して全comonadを同定し、右随伴像の生成性から実coKleisli代数・Morita双加群を得る。周囲代数のuntwisted双対性はcyclic potentialの相対自己双対解消を用い、共有u差を一度だけ加えて証明する。AS正則性という語だけからuntwisted性を推論せず、一般PI・有限中心性も仮定しない。

この存在比較はb₁の単射性に依存しない。単射定理は線形方向が圏で消えないことを保証する別の結果であり、下記の像と係数形の決定に用いる。数値係数が未決定でも、各段で実可換族を参照する普遍比較の存在は保たれる。ℚ上への核降下・全標識保存・一般線形族のPI性と有限中心性は別の未解決課題である。

`verify_mixed_linear_bockstein.py` の6 PASSは、二次関係からの双対積、独立左右primitiveのrank6、対称対角外三列との補行列式−64、Tate双次数、および全k・全arityに対する非分裂towerの両隣接群の消滅を検算する。実クラス同定・全coherence・Morita核自体の形式証明ではない。

近接する既知結果として、Etingof–Ginzburg, JEMS12(2010), §3.5・Theorem3.6.2(i), p1389は一因子の斉次中心商のgraded MFと楕円曲線の導来圏を比較する。Anno–Arkhipov–Logvinenko, arXiv:2303.11826v2, Theorems6.1,8.4はenhanced adjunctionの全comonadとcoKleisli復元を扱う。後者の復元にはperfect対象から作るfree comoduleのperfect性という仮定がある。本稿では随伴像の生成性を直接証明し、指定境界の比較群の消滅と実可換族の参照によって全線形PBW族へ適用する。一般の復元理論を新規成果とせず、個々の具体化の網羅的新規性は未確認とする。一次PDFを確認した箇所とURLは混合稿Introductionおよび共有書誌に置く。

### 一次Bocksteinの像と七定数の比較形

正本は `mixed/linear_equivariant_coefficients.tex`。`lec:thm:seven-scalar-form` は、`cmm:lem:boundary-parameters` のHeisenberg同変な境界比較と、Jac(G)₂の純ブロック代表xy,yz,zxおよび全異ブロック単項式からなる切断を固定する。生成元への作用c(x,y,z)=(y,z,x), d(x,y,z)=(x,ωy,ω²z)に対し、B_(p,α)→B_(gp,gα)の規約ではc_P(p,q,r)=(r,p,q), d_P(p,q,r)=(ωp,q,ω²r)である。中心ζはPにζ²、αとactive一次式にζとして作用する。従って各ブロックの中心文字を比較すると、b₁の像から異ブロック項が排除され、像は正確に⊕ᵢJac(J_i)₂となる。

Schurの補題と因子置換の同変性により、比較係数は次の形に限られる。

\[
\begin{aligned}
Q(\mathbf p)&=\chi_k\sum_i a_i(p_ix_iy_i+q_iy_iz_i+r_iz_ix_i),\\
R_2(\mathbf p)&=A_k\sum_i a_i(q_i^2x_i+r_i^2y_i+p_i^2z_i)
 +B_k\sum_i a_i(p_ir_ix_i+p_iq_iy_i+q_ir_iz_i),\\
R_{1,1}(\mathbf p,\alpha)&=C_k\sum_i a_i
 (q_i\alpha^{(i)}_1+r_i\alpha^{(i)}_2+p_i\alpha^{(i)}_3),\\
R_3(\mathbf p)&=D_k\sum_i a_i(p_i^3+q_i^3+r_i^3)
 +E_k\sum_i a_ip_iq_ir_i.
\end{aligned}
\]

χ_k≠0は残余Bocksteinの単射性から従う。A_k,…,E_kには非消滅を課さず、定数は一般にkへ依存してよい。κ_k=κを合わせた七定数のうち、未決定なのはχ_k,A_k,B_k,C_k,D_k,E_kの六つである。重み一からx'_i=t_ix_i,p'_i=t_ip_i,α'^(i)=t_i²α^(i),t_i³=a_iで戻すと、全てのブロック項にちょうどa_iが掛かる。

高次係数の同変性は、非線型なA∞積の平均によるものではない。同変な切断でQを選び、実可換族G+uQ、次いでG+uQ+u²Lを参照する。下位構造を同定するpathの空間が可縮なので、その後の二項・三項の差classは一意に定まり、群作用と両立する（`lec:lem:equivariant-differences`）。一ブロックの同変写像空間の次元は順に1,2,1,2であり、独立中心文字が全ての異ブロック補正を排除する。3|kでも全次数格子を保持し、対称rotation分裂は仮定しない。

Q_ncを可換化してJac(J)₂へ写すと(53/54)(p xy+q yz+r zx)になるが、これは同じSchur直線に属することを示すにとどまる。χ_k=53/54やA_k=1/6,B_k=−1/18の同定はしていない（`lec:rem:numerical-scope`）。次の数値化には、実境界核によるfull Bocksteinの像と、実可換参照族に対する二項・三項差の計算を用いる。`verify_mixed_equivariant_coefficients.py` の10 PASSはsource→target規約の関係式・中心式、四つの写像空間、全kの台、重み復帰と上の53/54だけを厳密検算する。比較核や全coherenceの形式証明ではない。

### 任意の固定線形係数での判別超曲面

正本は `mixed/linear_discriminant_geometry.tex`。f=G+Q+Lの臨界代数は、最高次数部分∂Gが正則列であることから、全(p,α)上階数8^kの有限自由加群となる。Euler恒等式により[f]=[(Q+2L)/3]であり、det(CI+m_f)はc次数8^k、最高係数κ^(8^k)となる。u=0の境界が滑らかなので、その非消滅が可換標的と残余線束圏のsmoothnessの必要十分条件である（`lcc:cor:linear-discriminant`）。

`ldg:lem:fixed-quadratic-morsification` は、任意に固定した二次式Qについて、H=G+Qへの一般線形摂動f_ℓ=H+ℓ·xが8^k個の非退化臨界点と相異なる臨界値を持つことを示す。臨界スキームはℓ=−∇HによりA^N_xであり、A^N_ℓ上有限平坦となる。相異なる臨界点対ではd(f_ℓ(x)−f_ℓ(y))=Σ(x_j−y_j)dℓ_jとなるため、臨界値の一致は各成分の恒等式になり得ない。これにより、各固定pに対する一般αで8^k個の相異なる悪い中心係数と、各可換標的の唯一の通常二重点を得る（`ldg:cor:fixed-linear-parameters`）。

独立係数ℓ,γを用いた普遍判別式Δ(p,ℓ,γ)=det(γI+m_f)はC[p,ℓ,γ]上既約・被約であり、pを任意に固定してもC[ℓ,γ]上既約である。整な普遍臨界代数と臨界値分離から、−fがその関数体拡大を生成することを示している。一般のnorm多項式の既約性を仮定した結果ではない。`ldg:thm:normalization` の正規化射は

\[
(\mathbf p,\mathbf x)\longmapsto
\bigl(\mathbf p,-\nabla H_{\mathbf p}(\mathbf x),
\mathbf x\cdot\nabla H_{\mathbf p}(\mathbf x)-H_{\mathbf p}(\mathbf x)\bigr)
\]

であり、源はA^(3k)_p×A^N_x、固定pではA^N_xである。臨界スキームから(p,ℓ)への射は次数8^kだが、判別超曲面への正規化射は双有理である。判別超曲面が複素点で特異となるのは、同じ値−γを持つ相異なる臨界点が二つ以上あるか、その値を持つ臨界点でHessianが退化するとき、かつそのときに限る。これは有限正規化のファイバーと微分からの集合論的な特異点判定である。

三角多項式同型Θ:(p,α,c)→(p,ℓ=coeff L,γ=C)により、これらは元の非可換係数上の判別式𝒟_kへ移る。普遍Δ・𝒟_kおよび固定pの多変数判別式の被約性と、固定(p,α)の一変数多項式の被約性は異なる。後者には臨界値の衝突や非被約な臨界代数による重複根があり、各根の重複度は対応する局所臨界代数の長さの和である。特異係数での比較は残余線束圏に限り、非可換中心の局所型や全coherent圏の比較をこの判別幾何から結論しない。全coherent Ku比較は引き続き𝒟_k≠0上である。

固定二次項のmorsificationとLegendre判別式は既知の枠組みであり、その一般機構を本研究の新規成果とはしない。関連する一次資料と本表示への適用の範囲は同節のIntroductionおよび共有書誌を参照する。上記の証明執筆・独立読解、有限記号計算、組版・表示・保存は別の状態であり、実施範囲の正本は `validation.md` とする。

### 他の楕円因子へ進む際の中心持上げ条件

正本は `mixed/elliptic_center_obstruction.tex`。PBW性・untwisted CY性と、指定した最高次中心三次Ω₀の持上げは別の条件である。τ≠0, τ³≠1,−8のS_τ=S(1,1,τ)は滑らかな楕円曲線の非零二捩れ平行移動を持ち、関係は{y,z}+τx²=0とその巡回式、指定中心元はΩ_τ=(τ³−1)(C_−−C_+)/3である。ここでC_+=xyz+yzx+zxy、C_−=yxz+xzy+zyx（`eco:lem:clifford-input`）。

一般の線形補正r_i+uΣm_ijx_j−u²α_iがPBWであることはM=Mᵗと同値である。平行移動によって非対角部分を唯一に消すと、残る三方向はp_x=m₁₁−τm₂₃、p_y=m₂₂−τm₁₃、p_z=m₃₃−τm₁₂となる（`eco:prop:clifford-pbw`）。`eco:thm:clifford-obstruction` は、任意のαと全ての二次・一次・定数補正を許しても、Ω mod u=Ω_τとなる中心三次が存在することとp_x=p_y=p_z=0が同値であることを証明する。一次中心性の障害を三つの係数汎関数で測ると−3τ(p_z,p_x,p_y)となり、二次補正の交換子では消せない。逆にp=0では平方と反交換子が中心で、Clifford体積元Ω_τ自体が持ち上がる。

τ=2,p=(1,0,0),α=0,u=1の有理係数例では、指定三次中心元の持上げは存在しないが、7x²+4xは非スカラー中心元である（`eco:ex:rational-obstruction`）。従って、Etingof–Ginzburgが保証する濾過次数三以下の非スカラー中心元の存在と矛盾しない。そのRees斉次化u(7x²+4ux)はu=0で零であり、元の楕円中心商を与えない。この障害は同じ境界を保つ中心三次商の表示に関するもので、滑らかなnc cubicの可換Ku実現への反例ではない。

一方、Z(S)₁=Z(S)₂=0、Z(S)₃=CΩ₀を持つ三生成元のquadratic Koszul untwisted 3CY因子では、全ての低次cyclic potential Φ₃+uP+u²Lに対し、普遍多項式中心持上げΩ_T=Ω₀+uC₂(P)+u²C₁(P,L)がある（`eco:prop:universal-lift`）。u³のscalar項を零にするPBW規約で一意であり、C₂はPに一次、C₁はPに二次・Lに一次となる。各点での中心存在と低次数中心消滅だけで普遍性を宣言せず、固定交換子写像S₂→Hom(V,S₃)、S₁→Hom(V,S₂)の左逆で多項式係数を構成する。

滑らかな標準Sklyanin S(a,b,c)で平行移動点が二捩れでなければ、これらの中心条件が成立し、全quadratic–linear–constant PBW補正を覆う（`eco:cor:non-clifford-lift`）。有限位数・無限位数を含み、滑らかなHesse表示ではabc≠0により平行移動点は変曲点でなく、三捩れも除かれる。中心商のsection比から、次数dの非零中心元があればdp=0となることを使う。二捩れ条件は座標交換が逆元写像であることからa=bと同値で、S(1,1,τ)へ規格化できる。従って上の二場合は、滑らかな点曲線を持つ全標準Sklyanin因子を覆う（`eco:rem:exhaustion`）。二捩れでない範囲では中心元の存在自体を未知の追加入力にする必要はない。

`verify_elliptic_center_obstruction.py` の7 PASSは、Hesse条件、PBW重なり・平行移動、次数三基底、ℚ(τ)上の一次中心障害と三つの消去汎関数、Clifford体積元の中心性・平方・行列式、有理係数例の全低次補正を許した線型系と二次中心元を厳密確認する。非二捩れの一般持上げと楕円曲線の論証は本文に依拠し、この計算を全比較核の証明と同一視しない。

中心持上げの成立範囲を入力として、次の全係数比較を構成した。PBW・中心存在、残余Bockstein検出、実comonadと核は異なる証明段階であり、全intrinsic対象の表示被覆はなお別の問題である。

### 任意固定楕円因子の全許容比較と二種類の一次方向

正本は `mixed/elliptic_mixed_comparison.tex` と、その入力である `elliptic_boundary_kernel.tex`, `elliptic_bockstein.tex`, `elliptic_universal_kernel.tex`。滑らかな標準S(A_i,B_i,C_i)を固定し、k≥2、全a_i≠0、一つの共有中心u、因子間は可換とする。固定tensor境界と厳密中心作用を持つ全二次PBW表示では、この因子間可換性も `ifp:thm:factorization` から従う。異なるj、同種・CM、二捩れ、有限位数・無限位数を許す。因子を動かすmoduli上で一つの核を選んだという主張ではない。

二捩れの定数型ambientはR=C[α,u,X,Y,Z]上階数8のClifford代数となり、X=x²,Y=y²,Z=z²が中心である。対称行列qの対角はX,Y,Z、非対角は(u²α_z−τZ)/2等。体積元v=xyz−q_xy z+q_xz y−q_yz xに対し、中心はR⊕Rv、v²=−det q、Ωτ=−2(τ³−1)vである（`eco:prop:clifford-center-freedom`）。u=0のdet qは−τ²(X³+Y³+Z³)/4+(1−τ³/4)XYZで、全α特殊化で非零最高項が残る。分数体上の中心からPBW基底の1・xyz係数を比較して分母を除く。同じ境界Ωτを持つ全中心三次はΩτ+uβ·(x²,y²,z²)+du³に限られる。多因子の低中心も各二捩れ因子の平方の直和なので、混合ブロック補正に追加自由度はない（`emc:prop:coverage`）。

固定境界は、実MF外積・windowで中心群同変圏をPerf(∏E_i)へ比較し、因子別Picard線束とscalar三乗根でrotationと指定周期を合わせる（`ebk:lem:boundary`）。全次数格子と基準因子を使うため3|kでもよい。双対character作用は元の同変MF模型では厳密dg作用であり、perfect双加群圏上でElagin Lemma8.6を適用して実同変核へ戻す。任意の三角作用からのdg liftを仮定していない。

二つの法線Bocksteinを区別する。定数方向はt=0でv=u²と置き、剰余体評価にΣα_ij r_ij*が残る。二次双対ではξ_ij²=C_i r_ij*であり、Shamash周期にtorsionがないのでTate局所化後も独立である。可換境界のJac(G)₁の次元は3kなので、定数方向の写像は同型となる（`ebc:prop:constant-iso`）。一次方向では自己交叉のfull cochainを使う。非二捩れのPはunaryで検出され、独立な左右gauge行列Dの対称部分が平行移動T((L+R)/2)となることから対角零Pは消せない。二捩れのβはunaryでは見えず、relative barのYoneda積にδ₂=±a_i diagβ·ϑが現れる。baseline m₃はClifford体積元の交代三tensorである。全対象依存h₀の挿入は交代、h₁m₂はClifford三関係の対称spanとなり、純対角βと交わらない。全整数周期冪を許した双次数計算を併用し、全3k一次方向の単射を得る（`ebc:thm:first-injection`）。普通のExtの低積だけからTate移送を推測せず、中央局所化と非負周期部分の同定を本文で確認する。

全係数T=C[t,α,c]上の相対potential解消と共有中心差一回のchange of ringsにより、untwisted双対・proper線束模型・実球面随伴を構成する（`emc:prop:line-model`）。固定counitの正規化塔は二項Jac₁・三項Cだけを残し、非分裂の両隣接群も消える。各段に実可換族を参照し、全Tの差を重み(1,2,3)で整理することでL=𝔄α+R₂、C=κc+R₁,₁+R₃を得る。𝔄は上の同型、κ≠0は中央一変数MFの三項による。全comonadとcoKleisli生成代数から実graph双加群を作る（`euk:thm:universal-kernel`）。比較の存在は一次Bockstein単射にも𝔄の可逆性にも依存せず、後者は係数変更と判別幾何で使う。

Θ:(t,α,c)→(t,ℓ=coeff L,γ=C)は三角多項式同型。各固定tでは任意の線形ℓを動かせるため、rank8^kの有限平坦gradient写像の一般fiberは単純で臨界値も相異なる。判別はdet(CI+m_(G+Q+L))、その正規化は(t,x)↦(t,−∇(G+Q),x·∇(G+Q)−G−Q)である（`euk:cor:discriminant`, `euk:cor:normalization`）。特異判別点は値−Cを共有する異なる臨界点、またはその値を持つ退化Hessian点に正確に対応する。特異係数の比較は残余線束圏であり、全coherent比較や非可換中心の局所分類へ広げない。

有限証明書 `verify_elliptic_bockstein.py` は8 PASS。一般左右gaugeの恒等式、det=−8c³(a−b)³、Clifford binary補行列det=8、Tate双次数と三つの独立挿入を検算する。文献の一次入力は Reich–Walton, Involve11(2018),585–608, DOI10.2140/involve.2018.11.585, Theorem7.1(a)（斉次二捩れ中心）、Lu–Palmieri–Wu–Zhang, JPAA213(2009),2017–2037, DOI10.1016/j.jpaa.2009.02.006, TheoremA/CorollaryB/§5（体上の関係とExt高次積）、Elagin arXiv:1403.7027v2 Lemma8.6/Theorems4.2,8.7,8.9である。これら既知理論と本表示への適用を区別し、後者の網羅的な新規性調査は未完了とする。

多中心の比較は次項の良い切断／flag付き結果へ進む。因子moduli上のPicard線束と周期三乗根の降下、一般因子の数値Q・𝔄・κ、全intrinsic表示被覆も残る。一般因子の一次像の具体的Jac₂座標は未決定で、同一S0のHeisenberg純ブロック像を無断に流用しない。

### 多中心の全表示、良い中央切断と反復比較

正本は `mixed/multicentral_comparison.tex`。`mcp:thm:normal-form` は固定因子・因子間可換の表示について、非被約を許す任意可換C-代数R上で、一次中心形式t(U)、二次中心形式α(U)、三次中心形式c(U)を全パラメータとする。`ifp:thm:factorization` により、指定中心三次を持つ固定tensor境界・厳密中心作用の全二次PBW表示をこの正規形へ戻せる。非二捩れの中心式は既に証明した普遍多項式をh=1とした後に係数代入する。二捩れでは正規化関係線形項が零、中心平方の一次係数βは残る。分類はI=(U)の随伴代数と低中心を使い、Σu_jq_jの中心性から各q_jの中心性を推論しない。自由係数数は3km+3k binom(m+1,2)+binom(m+2,3)、m=2で15k+4。`mcp:prop:free-quotient` によりAはR[U]上自由、wと中心列は任意順序で正則である。

二中心では一中心のQ,L,Cへ形式を代入したW_polと、切断判別Δ=D(t(U),α(U),c(U))を定める。Δは重みから次数3·8^kの二変数形式。U_cut={Δ≢0}はsmoothな中央ray商が一本ある条件と正確に一致する。固定t(U)で一般α(U),c(U)はΔの単純根3·8^k個を持ち、W_polはsmooth、境界Zをblow-upするとLefschetz pencilになる（`mcpn:thm:lefschetz-pencil`）。証明の入力は固定tの被約判別、各点の値評価の全射性、三次形式の一次jetの自由度である。次数自体はTevelev, arXiv:math/0112028v1, §7.1 Example7.4の既知の双対次数公式と一致する。

実核は一本のsmooth切断A₁=A₂/(v)を固定し、一中心の核E₁と実制限随伴から作る。W_polのsmoothnessとsourceのsmoothnessは下記のblow-upで同値となるが、X_polそのものへの核はまだ同定していない。cotwistはρ_A₁⁻¹[1]なので、E₁はrotation比較を与える。smooth cubic境界のHH⁰=C、HH<0=0により、C上でscalar三乗根を選べば指定三次periodを同期できる。元のu作用の標識を同時に保つとはしていない。固定境界のM=N+1変数に対し、BFKの隣接sectorの必要等式は左辺≤2<Mとなり、二項Jac(F₁)₁・三項Cだけが残る。

横断係数は重み一 γ₁=(t_v,α_uv,c_uuv) が2N+1個、重み二 γ₂=(α_vv,c_uvv) がN+1個、重み三 z=c_vvv が1個。固定E₁をこの多項式環へ移し、実可換参照族との差を二項・三項で消すと、W_it=F₁+vQ̃+v²L̃+v³C̃と実全comonad比較を得る。L̃=Bγ₂+R̃₂(γ₁)、C̃=κ′z+R̃₁,₁+R̃₃、κ′≠0。`mtb:prop:transverse-iso`でBの可逆性を証明したが、核の存在の証明はそれを入力としない。coKleisli生成代数から全横断係数の実Morita核・逆・制限intertwinerを構成する（`mci:thm:iterated-kernel`）。smoothnessはsource line圏と標的で同値、そこで全coherentへ飽和する。

F₁のgradientが原点だけを零点に持つため、Q̃,L̃を固定した臨界代数は階数2^(N+1)=2·8^k。det(C̃I+m_(F₁+Q̃+L̃))のz最高係数は(κ′)^(2·8^k)であり、任意固定γ₁,γ₂で有限個のzを除いてsmoothとなる。さらにB可逆性により各固定γ₁の一般γ₂では2·8^k個の単根を持ち、各可換標的に唯一の通常二重点がある（`mtd:cor:simple-values`）。全横断係数・各固定γ₁の判別は既約被約、正規化はそれぞれA^(2N+1)×A^(N+1)、A^(N+1)である。正規化射はΘ⁻¹(γ₁,−∇H,y·∇H−H)。複数の同値臨界点またはHessian退化が判別超曲面の特異点を正確に与える。特殊γ₂の多重根は許す。

横断Bocksteinの検出ではε=v²とし、E=B₁!のTate模型E[ϑ,ϑ⁻¹]を用いる。α_vvはδ₀(κ)=±Σαq∈E₂で検出される。これを消した後、中心式w₁+εd uの変形はaugmentationを保つが、相対Shamashの微分がδ₁(ξ_u)=±dϑを与える。primitive零項の双次数(1,−2)はj+2r=1,j+3r=2からj=−1となって存在しない。したがって全対象依存のprimitive・全高arityを許してもdは消せない。Lowen Theorems3.21/4.15のfull brace移送と実二列法線自己交叉を使い、対象上の値だけから自然変換を推測しない。任意q中心の固定smooth境界でも、d_j u_jの各方向をδ₁(ξ_{u_j})で分離できる（`mtb:cor:many-centers`）。period同期済みの実境界核を入力とする。

任意mの逐次核は、固定した境界核とsmooth中央flagに沿って構成する。このflagの存在は下記の中央Bertiniにより全smooth因子別対象で保証される。各段の二次係数はN+m−1方向を持ち、一般二次係数の最後の悪い値は2^(N+m−1)個で各唯一ODP、固定一次係数の判別はA^(N+m−1)を正規化に持つ。因子・flagを動かす大域核ではなく、固定した境界の横断係数上の相対核である。

### 実中央blow-up、全smooth locusと一般中央flag

`mbl:lem:strict-action`は、中央u_iの厳密な可換作用と内部shiftから全線束圏L_AのPerf([A^m/G_m])作用を作る。残余Kuそのものが全内部shiftで閉じるとは仮定しない。実圏

\[
\mathcal P_A=\mathcal L_A\otimes_{\operatorname{Perf}([\mathbb A^m/\mathbb G_m])}
\operatorname{Perf}([\operatorname{Bl}_0\mathbb A^m/\mathbb G_m])
\]

はP^(m−1)線型であり、chart U_iではA[z_j]/(u_j−z_j u_i)の全線束圏になる。実free–forgetful随伴と中央Koszul解消のHomをqgr制限随伴のHomと比較する証明であり、Koszul加群解消をassociative cofibrant代替と取り違えない。全ray fiberは通常の一中心商で、相対proper性も全係数線束模型から従う。

Khan, *Algebraic K-theory of quasi-smooth blow-ups and cdh descent*, Ann.Henri Lebesgue3(2020),1091–1116, DOI[10.5802/ahl.55](https://doi.org/10.5802/ahl.55), Theorem C・Proposition4.2・§4.4はderived Artin stackにも適用できる。これをstrict作用へ実随伴・projection三角とともにtensorし、P_A=〈m−1個のL_D,L_A〉を得る（`mbl:prop:orlov`）。L_Dは既存境界比較でsmooth proper、gluingはcompact随伴を通じてC-perfect。従ってL_A smoothならP_A smooth properとなる。m2のcross HomはRHom_D(N,i*M)[−1]である。Jiang–Leung §1.5の幾何的admissible部分圏という仮定を、このsourceへ無条件に適用しているのではない。

`mcb:lem:smooth-local`は絶対対角のperfect性を底のZariski局所で判定する。P_A^op⊗C P_AにはP^(m−1)×P^(m−1)の作用があり、恒等核は底の対角上に支持される。U_i×U_i上ではchart圏の絶対対角となる。有限affine被覆の有界ČechとMapの有限極限がfiltered colimitと交換することからcompact性を大域へ戻す。Antieau–Gepner, Geom.Topol.18(2014),1149–1244, DOI[10.2140/gt.2014.18.1149](https://doi.org/10.2140/gt.2014.18.1149), Lemma6.4・Theorem6.11の証明にも同じmapping pullbackの原理がある。これは相対smoothnessや比較核の貼合せを主張する補題ではない。

各chartの残余圏には、一中心の普遍実核を多項式係数変更で適用でき、W_pol(x,sℓ(z))の残余線束圏となる（`mbl:cor:chart-kernel`）。R=C[z]上properな例外成分のgluingは、残余の絶対対角の有限解消をtensorすることで絶対perfectになる。この補題により残余の絶対smoothnessと全line/Perf圏の絶対smoothnessを行き来できる。Lunts, *Categorical resolution of singularities*, J.Algebra323(2010),2977–3003, DOI[10.1016/j.jalgebra.2009.12.023](https://doi.org/10.1016/j.jalgebra.2009.12.023), Proposition3.13はproper仮定なしに有限型schemeのPerf smoothnessとregularityを同値とする。

これらの可換chartはBl_Z X_pol、Z=V(G)⊂P^(N−1)のchartである。Z上では∂_xGが消えないのでX_polは元々滑らかで、blow-upはZ外で同型になる。従ってsource smooth⇒P_A smooth⇒各可換chart smooth⇒X_pol smooth。逆にX_pol smoothならZもsmoothなのでblow-upの各chartはsmoothであり、一中心核・相対例外gluing・絶対対角の局所性からP_A smooth、さらにadmissible L_Aと残余K_Aもsmoothとなる。これが `mcb:thm:smooth-locus` のK_A smooth ⇔ X_pol smoothである。有限中心性・PI性・全chart核の降下を入力としない。

全係数の非smooth locusは一つの非零・非定数多項式で定まる。普遍正規形の係数環をP_m、N=3kとして、

\[
\mathfrak D_m=\operatorname{Res}_{x,U}
 (\partial_{x_1}W_{\mathrm{pol}},\ldots,\partial_{U_m}W_{\mathrm{pol}})
\]

と置く。`mcb:cor:global-discriminant`は係数の重みwt(t,α,c)=(1,2,3)に関してdeg_wt 𝔇_m=3m·2^(N+m−1)を与える。中心座標Uだけをλ倍することと係数を重みで拡大することが等しく、Busé–Jouanolou, *On the discriminant scheme of homogeneous polynomials*, Math.Comput.Sci.8(2014),175–234, DOI[10.1007/s11786-014-0188-7](https://doi.org/10.1007/s11786-014-0188-7), [arXiv:1210.4697v1](https://arxiv.org/abs/1210.4697v1) Proposition4.13の勾配resultant座標変換則を適用する。零集合の判定は同Proposition2.4とEuler公式による。分離slice t=α=0では非零定数倍のRes(∂c)^(2^N)となる。全𝔇_mの既約性・被約性はここからは結論しない。Q,L,Cの未算出定数があるので、全係数の展開を計算したという意味でもない。

二因子・二中心（N=6,m=2）の三つの次数は、対象と変数を分けて使う。

| 判別式 | 次数を測る変数 | 次数 |
| --- | --- | ---: |
| 切断方向Δ(a,b) | rayの同次座標a,b | 192 |
| 固定smooth境界の横断判別D_it | 最後のv³係数z | 128 |
| 全係数判別𝔇_2 | t,α,cの重み1,2,3 | 768 |

可換側の中央線型系はZ外で基点を持たず、Z上では中心du_iが独立である。普遍hyperplane incidenceのsmoothnessと標数零のgeneric smoothnessから一般中央切断がsmoothとなる。制限係数の偏極は元のW_polの制限に一致するため、同じsmoothness同値を中間商へ反復して一般中央flagを得る（`mcb:thm:central-flags`）。二中心では特にsmoothness⇒Δ≢0であり、全cutが特異な対象はsmooth対象には入らない。`mcb:cor:all-smooth-comparison`はこのflagと既存逐次核から、任意mの全smooth因子別表示の全coherent Ku実現を結論する。実標的X_itと偏極候補X_polの同値核、全中心作用の同時保存、全intrinsic被覆は未証明である。

近接する既知結果としてLBSV Theorem3.2.6、Cassidy–Shelton Theorems1.3/1.5、Gaddis Propositions2.7/5.1は正規形・PBW・正則homogenization・tensor積の入力であり、本Ku比較を直接与えない。Perry, arXiv:1804.00132v2 Lemma7.18/Proposition7.19のHPDは実P(V)-linear Lefschetz圏を入力とする。本稿の基点付きsourceは上のstrict中心作用とKhanの定理で構成した。Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2 Proposition2.1は可換有限型環上有限な代数を仮定する。一般PBW族へその仮定を流用しない。二捩れClifford部分では中心平方から有限中心性を確かめる別経路があるが、全固定因子の結論はこの有限中心法に依存しない。網羅的な新規性確認は未了である。

中央pencilの具体的な先行例として、S. P. Smith–M. Van den Bergh, *Noncommutative quadric surfaces*, [著者公開本文](https://sites.math.washington.edu/~smith/Research/pencil-nc-quadrics.pdf), DOI [10.4171/JNCG/136](https://doi.org/10.4171/JNCG/136), Theorems5.6,10.2を確認した。前者は対象とする非可換二次曲面のsmoothnessを有限次元代数C(A)の半単純性で判定し、後者は四次元Sklyanin代数の中央二次式pencilの特異memberが四つであることを示す。本三次族への一般Bertiniではないが、圏のsmoothnessを実有限模型で検出する比較例として有用である。

### 二重制限で保持する混合情報と失われる軸データ

`tcr:prop:beck-chevalley` はA,A/(u),A/(v),Sの実残余制限正方形のcanonical右mateが同型であることを証明する。inflationの右projectionのcorrectionはO_A(−1)だけに入り、他方の制限後のprojectionがこれを消すことが要点。単なるambientのTor-independenceだけで残余BCを済ませない。`tcr:prop:joint-comonad` のjoint HH^Rはunderlying kernelとして軸comonadの積に同型となり、実HH^Rの全構造を移したcoherent分配データを持つ。これはBeck, Distributive Laws, LNM80(1969),119–140, DOI10.1007/BFb0083084, §3 Propositionの形式論と両立する。裸の交換射による高次一意性は未主張。

指定Koszul法線MFでq=u²A₂+uvB₂+v²C₂+du³+eu²v+fuv²+hv³を扱うと、二つのodd classの二項積はClifford形−t(A₂,B₂,C₂)、同一odd線に沿う三項積は±t(dr³+er²s+frs²+hs³)となる（`tcr:lem:mixed-normal-products`）。これは選んだ模型での混合係数検出であり、全active gaugeを割ったmoduliの単射性ではない。非分裂一次項uQ_u+vQ_vを消したという意味でもない。

`tcr:ex:same-axes` のW₀=G+u³+v³とW₁=G+(u+v)(u−v)²は、二つの滑らかな軸切断、交叉Z、軸からZへの実随伴と全軸comonadを共有する。しかし前者の残余線束圏はsmooth、後者はp=[0:…:0:1:1]の非正則局所環によりsmoothでない。この反例は、二つの一中心比較を個別に固定しても全体の比較にならないことを示す。一方、逐次核は一本のsmooth境界から元の全横断変形を使うので、この反例と矛盾しない。

相対balancingの未完成点は本ノート後半の「graded-center balancing の有限性」と `tcr:rem:balancing-scope` に保持する。有限Koszul加群模型とassociative cofibrant相対対角の無限q_m列を区別する。逐次比較ではこの未同定towerの有限性を仮定せず、一中心の固定境界塔を用いる。

有限再現資産は `verify_multicentral_pbw.py`（4 PASS）、`verify_multicentral_pencil.py`（6 PASS）、`verify_two_center_restrictions.py`（6 PASS）。pencilのFermat六変数例はb_j=2^jとして、64個の非零相異なる符号和2Σ ε_j8^jから192個の単純方向を厳密に確認する。二重制限の検算器は独立な4×4行列で混合二項・三項を確認する。これらを一般の比較定数や全Ku核の機械検証として扱わない。

### 固定tensor境界の全PBW関係は因子別に分解する

正本は [interfactor_pbw.tex](../papers/sections/mixed/interfactor_pbw.tex) の `ifp:thm:factorization`。固定smooth標準Sklyanin因子S_i、k≥2、任意可換C-代数R、厳密中心一次変数U=(u_1,…,u_m)を取る。最高active次数の随伴代数を(⊗S_i)⊗R[U]に固定し、全二次関係にU×全active生成元とSym²Uの補正を許す。内部関係が別因子の生成元を出力することも、因子間交換子が線形・定数補正を持つことも、初めから禁止しない。

このPBW仮定だけで混合交換子の全補正と内部関係の他因子出力が零となり、元の生成元を保つR[U]-代数同型B≅⊗_{R[U]}B_iを得る。各B_iもPBWである。形式同型やgaugeを選んだ後の分解に留まらない。二つの入力はDer₋₁(S_i)=0とZ(S_i)₁=0であり、関係の平方係数C_i≠0から有限線型写像の単射性として直接示す。I=(U)のI/I²で混合線形項、次いで内部の他因子出力を消し、I²/I³で混合定数項を消す。単射はC上で分裂するため、非被約・非平坦な係数変更も許される。

`ifp:cor:abstract-factorization` は同じ二条件を持つ任意のconnected二次C-代数へこの証明を拡張する。生成空間は有限次元とし、Koszul性・AS正則性・smoothnessはこの分解自体には不要である。次数−1導分を持つ多項式因子ではxy−yx=u²というPBW例があるので、低次数条件を省略できない。固定tensor境界を持たない対象や中心作用自体を動かす変形は範囲外である。

指定中心三次の最高項がΣa_iΩ_i、全a_i≠0であるときは、この分解と `mcp:thm:normal-form` を続けて使い、既存の中心持上げ分類へ戻る。C上のsmoothな商には `mcb:cor:all-smooth-comparison` を適用できる。全intrinsic対象がこの表示を持つことは未証明のままである。有限検算の入口は `computations/verify_interfactor_pbw.py`（標準例と `--clifford`）であり、全因子・任意Rの定理は本文の有限線型証明に依拠する。実行状態は `validation.md` を参照する。

### 境界二次関係を動かす一次混合類と中心障害

正本は [interfactor_hochschild.tex](../papers/sections/mixed/interfactor_hochschild.tex)。固定境界S=⊗S_iの負内部次数ではHH²(S)₋₁とHH²(S)₋₂は純因子の直和で、ともに次元3kとなる（`ifh:lem:negative`）。有限Koszul双加群解消のtensor積でgraded Künnethを計算し、境界を保つidentity gaugeは各生成元への中心一次形式の加算だけであることも確かめる。これは上の厳密分解のcohomologicalな説明であり、有限関係式の結論は直接証明を正本とする。

境界そのものを動かす次数零変形では別の混合類が現れる。二捩れ因子の集合をI₂、各因子のEuler導分をE_iとすると、`ifh:prop:central-mixed-obstruction` は

\[
\operatorname{HH}^2(S)_0=\mathcal P\oplus\mathcal E\oplus\mathcal C,
\quad
\mathcal P=\bigoplus_i\operatorname{HH}^2(S_i)_0,
\quad
\mathcal E=\bigoplus_{i<j}\mathbb C(E_i\smile E_j),
\]

\[
\mathcal C=\bigoplus_{i\ne j,\ j\in I_2}
 \operatorname{HH}^2(S_i)_{-2}\otimes Z(S_j)_2,
\qquad \dim\mathcal C=9|I_2|(k-1)
\]

を与える。w₀=Σa_iΩ_iを中心へ持ち上げる障害はHH¹(S)₃に値を取り、Euler混合類には3(a_iΩ_iE_j−a_jΩ_jE_i)を与える。異なるordered成分が独立なので、この部分では単射で、純因子の障害とも相殺しない。一方、定数PBW変形の指定中心liftΩ_i+δq_iを使えば、中心平方z_jを掛けた混合類の障害はa_iq_i z_jによるinner導分となる。従って障害核は純因子の各障害核と𝒞の直和である。全因子が非二捩れなら一次中心lift可能な類は純因子に限られるが、この一次計算から形式・大域の因子分解や核の降下を結論しない。

### Clifford中心平方から得る九変数混合族

正本は [interfactor_clifford_family.tex](../papers/sections/mixed/interfactor_clifford_family.tex)。第一因子S₁を任意の固定smooth標準Sklyanin、第二因子を固定Clifford S₂=S(1,1,τ)、τ≠0、τ³≠1,−8とする。R=C[Λ_ab]、1≤a,b≤3に対し、

\[
\mathcal B_\Lambda
 =R\langle x_1,x_2,x_3,y_1,y_2,y_3\rangle/
 \bigl(r_{1,a}-\textstyle\sum_b\Lambda_{ab}y_b^2,
       r_{2,b},[x_a,y_b]\bigr)
\]

を作る。S₂の三つの平方が中心なので、第一因子の普遍定数PBW族𝒰₁にα_a↦Σ_bΛ_ab y_b²を代入したcentral base changeとして定義できる。𝒰₁はC[α]上自由であるから、代入先のC[α]-平坦性を追加せず、二因子の語基底の積がR-基底となる（`ifc:thm:family`）。同じ代入でΩ₁,Λ=Ω₁,₀+Σ_abΛ_ab y_b²ℓ_a(x)を得て、Ω₂,₀も中心に残る。全a_i≠0のw_Λ=a₁Ω₁,Λ+a₂Ω₂,₀は両側正則で、商𝒜_ΛもR上自由である。Hilbert級数はそれぞれ(1−t)⁻⁶、(1−t³)(1−t)⁻⁶。中心変数Uと任意中心三次g(U)の追加後も商はR[U]上自由となる（`ifc:cor:central-variables`）。

原点の接写像はMat₃(C)≅HH²(S₁⊗S₂)_{(−2,2)}=HH²(S₁)₋₂⊗Z(S₂)₂である（`ifc:prop:tangent`）。全代数S₁⊗S₂のHochschild cohomologyを計算するKoszul双加群複体の双次数(−2,2)では、一次cochainが零、二cocycleはHom(R₁,Z(S₂)₂)となる。従って九方向の独立性は純因子gaugeだけを割った計算ではない。この一つのordered pairの障害核を全次数へ同時積分した。両因子がCliffordの場合には、下記の双方向十八変数族が原点近傍の実残余族・局所可換比較まで積分し、二つのτ方向を加えると二十変数の幾何的形式変形空間を得る。一般の複数ordered pair・純因子次数零変形との任意の同時積分は未解決である。ここでのPBW濾過はxだけの次数であり、全active最高二次関係を固定する `ifp` の濾過とは異なる。従ってこの族は固定境界分解の反例ではない。

### 九変数族の全係数でのKoszul・Calabi–Yau性

証明の正本は [interfactor_clifford_regularity.tex](../papers/sections/mixed/interfactor_clifford_regularity.tex) の `ifr:thm:ambient-regularity`。任意の可換C-係数環と任意Λについて、長さ6、項の階数binom(6,i)の相対Koszul双加群解消を持つ。内部次数付き逆双対化は B(6)[−6] で、Nakayama twistはない。複素fiberでは大域次元6、AS index6、GK次元6となる。中心変数m個の追加後は次元/index6+m、中心正則三次商のaugmentation双対はR(3+m)[−(5+m)]である。特異な係数環上の相対双対性を、その環を含む絶対C代数の有限大域次元とは同一視しない。

証明の要点は、xのみの次数濾過を内部次数ごとに有限化し、固定C-bar複体の分裂に有限摂動を施すことである。これによりKoszul空間K_iの自由性と任意底変更を同時に得る。双対Eの反転濾過ではξ_xの重み0、η_yの重み1、E₆は重み3のrank1である。最高成分のtraceの完全対合を濾過から持ち上げると、Frobenius Nakayamaはμ(ξ)=−ξ、μ(η)=−η+Cξまで制限される。実自己同型x↦−x,y↦yはtop traceを−1倍しμと可換するため、C=0となる。このgraded symmetric traceでKoszul双加群複体を明示的に自己双対化する。単にPBWやAS正則性からuntwisted性を結論していない。

有限型係数環の局所化ではBとB^eも左右noetherianである（`ifr:cor:noetherian-envelope`）。主稿 `mbnp:lem:noetherian` の多重THCRの証明をS₁,S₂とそのoppositeの四因子へ適用し、濾過から戻す。個々の因子のstrong noetherian性だけを根拠にしない。Koszul双対のFrobenius形式による双対性判定はBerger–Marconnet Theorem6.3/Proposition6.4、He–Van Oystaeyen–Zhang Lemmas1.1–1.2の既知機構であり、本族について任意底の有限解消と符号対称性を確認したことを区別する。

### 通常のcoherent対角から得るsmooth proper近傍

正本は [interfactor_clifford_smoothness.tex](../papers/sections/mixed/interfactor_clifford_smoothness.tex)。m=0の四次元型と、m=1,g=cu³,c≠0の五次元型を扱う。全九変数環上にN=6+m本の線束からなるproper模型Σと、有限mutationで得る残余模型Γを構成する。非被約Artin底でもHomの計算複体・mutation・内部shiftが底変更を保つ。

`iff:thm:smooth-neighborhood` はΛ=0を含む実Zariski開でΣ,Γの相対対角をperfectにする。通常の二重次数対角Δ⁺_{i,j}=A_{i+j}はcyclic coherentかつ係数環上次数別自由である。原点局所環の次元9に関する帰納法で、flat対象間の高次Extを正則パラメータとNakayamaによって消す。一般の対象には9段のgraded free解消を使い、最後のsyzygyのflatnessから戻す。最初の核がflatだとは仮定しない。全係数環で既に存在する対角の線束解消を十分長く切ったYoneda境界が局所的に零となり、有限Extの局所化互換性で分母を払えば、その開上で有限複体のretractを得る。特殊fiberの微分やidempotentを無条件に持ち上げる議論ではない。

得られた相対smooth proper模型では、各複素fiberの全coherent圏と線束模型が一致する。rotation=L_O∘(1)は先に実関手として定義し、smooth開上でgraph双加群のperfect性・相対双対から随伴を作り、原点で零のunit/counit coneを消す開へ縮めて自己同値とする。全族の三乗周期coherenceはこの段階で仮定・主張していない。開集合の補集合の方程式と全smooth locusは未算出である。

### 四次元のrotationを持ち上げる変形と局所可換比較

一般論の正本は主稿 [rotation_preserving_deformations.tex](../papers/sections/rotation_preserving_deformations.tex)。BFK Corollary5.41とTheorem6.5はhomologyのsectorとcharacter作用を与える。三次四様体ではHH₀=Jac(F)₃⊕C_ζ⊕C_ζ²、HH±₂は恒等sectorの各一次元である。rotation固定の2-CY volumeによるcap同型を通して、HH²の固有値は1,ζ,ζ²、重複度は20,1,1となる。幾何的KSの単射性と次元比較から、固定接空間は正確に幾何的なJac(F)₃である。Huybrechts–Rennemoの内部shiftから作る次数付きHochschild代数と、この固定部分は定義を混同しない。

`ifk:thm:rotation-formal` はこれを通常Artinの全次数へ進める。既存 `prop:nf-fourfold-obstruction` の22次元形式hullには標識変更によるρ作用がある。ρ³≃[2]と偶数shiftによるHochschild複体の恒等共役から、同型類関手上ではC₃作用になる。cotangentの切断を有限群について平均すると同変な形式座標を取れ、固定点部分は非固定の二座標を零とした20次元形式円板になる。これは不変環による商空間ではない。幾何的変形の全次数自然変換はそこへ入り、接同型と形式逆写像から同型となる。tameな実catdefからhullへの写像の(−1)-truncated性を使い、rotationの持上げが存在する実変形は幾何的Kuへ戻る。分類するのは持上げの存在を条件とする充満部分群oidであり、持上げ自体や三乗周期を追加標識した高次群oidではない。

`ifk:thm:rotation-neighborhood` は実相対smooth proper族、実相対自己同値ρ、一点のrotation付きperfect核を入力として、その核をétale近傍へ延ばす。比較核スタックの小拡大問題に上の充満部分群oidの認識を使うので、既に指定されたP_Aへ新たにrotation同変性を要求せず持ち上げられる。有限表示・smooth atlas・étale局所切断から、実際の滑らかな三次族と核を得る。全基底上で核が全rotation・周期・中心標識を同時保存することは結論しない。

近接文献はLin–Zhang, *Categorical Torelli and Fourier–Mukai partners of hypersurfaces*, [arXiv:2611.05915v1](https://arxiv.org/abs/2611.05915v1)のTheorem2.2・Proposition2.4・Remark3.9である。幾何的KSの通常HH²全体への全射を使い、小拡大での核持上げから実際のsmoothな核族を得る。同文献は三次四様体を20対22のため明示的に除外する。ここでは全HH²への全射を仮定せず、rotationが持ち上がる変形を固定形式円板へ制限する。核スタックの代数化機構自体は既知であり、この仮定・結論の組合せの初出は未確認である。

Clifford族への適用は [interfactor_clifford_kodaira_spencer.tex](../papers/sections/mixed/interfactor_clifford_kodaira_spencer.tex)。原点の `ebk:lem:boundary` は任意固定因子、二捩れを含めてrotation付き実核を与える。従ってm=0にも原点を含む可換Ku実現開とétale局所perfect核がある（`ifk:cor:clifford-fourfold-neighborhood`）。m=1はn≠4の既存開性を使う `iff:cor:cubic-fivefold-open` による。いずれも原点開の存在であり、全smooth係数への比較ではない。

九方向の残余KSは幾何的20次元部分へ入り、二つの非恒等sectorへの射影は零である。さらに次項のfull Bocksteinの積により階数9と像を決定する。双方向十八変数族にも原点近傍の残余smoothnessと実比較が成立する（`ifg:thm:smooth-neighborhood`, `ifg:cor:local-comparison`）。全smooth係数への核延長、一般の複数ordered pairの同時積分、全intrinsic被覆は未完成である。既知の形式変形・有限群・核スタックの機構と、この族への適用の新規性を区別し、文献上の初出は未確認とする。

### 中心作用の積と残余KSの全階数

証明の正本は [interfactor_clifford_tangent_product.tex](../papers/sections/mixed/interfactor_clifford_tangent_product.tex)。`ift:lem:central-substitution` は、C[v]/(v²)上の平坦代数の積をm+vφと書き、厳密中心元zを用いてv=tzへ代入した族のfull Hochschild classがzφとなることを示す。d=deg vとe=deg zが同じ場合のdeg t=0も含む。双加群characteristic作用、dg quotient、windowが合成を保つため、対象ごとの評価だけでなく全自然変換で積を同定する。

これをB₀/(w₀²)、v=w₀、z∈Z(S₂)₂へ適用すると、w₀のBocksteinは実Shamash周期であり、w₀−tzのBocksteinは中心乗法q_zそのものになる。既存 `ebc:thm:first-injection` のClifford β三方向の単射性から、中心作用Z(S₂)₂→Hom(id,ρ²)は単射である。一方、`ebc:prop:constant-iso` の第一因子定数BocksteinはHom(id,ρ)に独立な三方向を与える。同じ中心代入v=εy_b²が関係式と中心三次補正をともに正しく移すため、九変数族のKSはこの二つの自然変換の積となる。

原点の比較核Eはブロック作用g:(x,y)↦(ζx,y)とrotation・指定周期を保つ。定数Bocksteinのg指標はζ、第二因子中心作用の指標は1なので、可換側ではそれぞれJac(f₁)₁とJac(f₂)₂に同型として入る。Huybrechts–Rennemo, Algebraic Geometry6(2019),76–99, DOI10.14231/AG-2019-005のPropositions3.3/3.5/3.9（一次本文確認2026-11-23）は、Jacobian環から内部shift自然変換環への環準同型・単射性と核による積の保存を与える。従って `ift:thm:rank-nine` は

\[ E_*\operatorname{KS}(M)=\sum_{a,b}M_{ab}L_aQ_b,\qquad \operatorname{im}\operatorname{KS}=(J_{f_1})_1\otimes(J_{f_2})_2,\qquad \operatorname{rank}=9 \]

を得る。L,Qは比較核に依存する可逆写像である。任意のブロック同変核だけでその数値行列が定まるとはしないが、下記のHeisenberg同変核の選択では射影的形を決定できる。`ift:cor:first-jet` は原点を標識した三次の20次元形式変形空間への余次元11の正則閉埋込みを与える。大域的な係数の識別や閉像は主張しない。両因子がCliffordなら同じ比較Eに因子を交換した計算を適用でき、逆向きの像はJac(f₁)₂⊗Jac(f₂)₁となる。二つの接写像の直和の階数は18であり（`ift:cor:two-clifford-tangents`）、下記の双方向族ではこれが実際のsmooth proper残余族のKSとなる。

**可換化の障害。** 許容値τ³=−2ではf₂はFermat三次で、文字通りの可換平方Y_b²はJac(f₂)₂で全て零となる。しかしQ(y_b²)は三つの独立な非零類である。したがって非可換中心の係数を同名座標で可換化してKSを計算できない。Picard補正と指定周期を含む実核を通す必要がある（`ift:rem:fermat-warning`）。

**高次係数に残る制約。** 一方向九変数族について、ブロックμ₃に同変な形式座標を選ぶと、20次元接空間の指標は(1,ζ,ζ²)に対して(2,9,9)であり、Λはζで変換する。像の(1,2)成分は総次数1 mod3、逆向き(2,1)成分は2 mod3、二つの純三次成分は0 mod3のTaylor項だけを持つ。最初の未計算項は逆向き成分を値に取る二次形式と、純成分を値に取る三次形式である。下記 `ifj:thm:twelve-coefficients` は具体的な多項式切片と反転同変原点核を固定し、この部分を4+8係数へ還元する。任意の標的形式座標に関する不変量ではないが、固定切片では一次部分が恒等の同変な源座標変更に不変である。rotationのC₃固定部分を取る操作とは異なるブロック作用であり、係数の数値・非消滅・収束は未決定である。

`verify_interfactor_residual_ks.py` の7 PASSは全Hesse smooth fiberのJacobian次数三の全56単項式・36関係・20基底、九次元(1,2)部分、指標分解、tensor行列式と上のFermat例を厳密確認する。既存 `verify_elliptic_bockstein.py` の8 PASSとともに保持する有限証明書である。今回の再実行範囲、full class移送と実核の証明、独立読解、組版は別々に `validation.md` へ記す。

近接する先行研究と今回の適用範囲は次の通りである。

- Braverman–GaitsgoryのPBW条件、Etingof–Ginzburgの低次potential変形、Clifford因子の中心平方は既知入力である。中心環へ定数パラメータを代入する構成原理自体の新規性は主張しない。今回の証明は、この九方向の実族・指定中心lift・全係数自由商・全接写像を一つの表示で確かめる。
- Walton–Witherspoon, *PBW deformations of braided products*, J.Algebra504(2018),536–567, DOI[10.1016/j.jalgebra.2018.02.028](https://doi.org/10.1016/j.jalgebra.2018.02.028), [著者PDF](https://people.tamu.edu/~sjw/pub/Walton-Witherspoon2.pdf), Hypothesis2.6・§6.2 Proposition6.2は、(S⊗Sᵒᵖ)#C C₂の定数型補正を分類する。scalar値の因子間補正は零であり、Cliffordの場合の追加九方向は非自明な群元gを値とする混合交換子である。gはactive生成元を符号反転するため厳密中心でなく、中心平方を内部関係へ代入する上の九方向とは異なる。Problem7.2の一般braided smash productの線形補正を解いたとはしない。
- Witherspoon, *Hochschild Cohomology for Algebras*, GSM204(2019), [著者PDF](https://people.tamu.edu/~sjw/pub/gsm204.pdf), Theorem3.1.2の有限生成自由双加群解消によるKünnethを使う。Sklyaninでは有限Koszul解消のtensorにより内部多重次数も保持して適用できる。
- Shepler–Witherspoon, *Deformation theory and Hopf actions on Koszul algebras*, Adv.Math.496(2026),110975,57pp., DOI[10.1016/j.aim.2026.110975](https://doi.org/10.1016/j.aim.2026.110975), [arXiv:2504.14397v3](https://arxiv.org/abs/2504.14397v3)のprimary abstract・Introductionは非可換係数環上のPBW/graded変形とHopf smash productを扱う。一般理論は§§2–4、Hopf–Koszulの具体条件はTheorem11.2・Corollary11.3に置かれる。本九変数族の分類や指定中心商を直接述べる箇所としては引用しない。

これらの限定した一次資料確認により、構成の一般原理と本表示への適用を分けた。固定境界の厳密因子分解およびこの特定九変数族の初出・網羅的な新規性確認は未了である。本文の証明、内部の独立読解、有限計算、組版・表示確認、外部査読・形式証明器の確認はそれぞれ別の状態として `validation.md` に記す。

### Heisenberg同変核による一次式

正本は [interfactor_clifford_equivariant_ks.tex](../papers/sections/mixed/interfactor_clifford_equivariant_ks.tex)。第一因子は任意の滑らかな標準Hesse表示S(a,b,c)、第二因子はClifford S(1,1,τ)とする。標準Hesse座標と点曲線方程式の非零scalar倍を固定し、原点の実比較核をH₃×H₃・rotation・指定周期に両立させて選べる（`ife:lem:equivariant-kernel`）。これは任意に選んだ核の自動的な性質でも、因子moduli全体における標準的な切断でもない。

構成の要点は、一因子のPicard補正Mに[3]*N≃Mという選択からE[3]-線形化を与えること、rotation比較射の一次元Hom線の指標をWeil対合による三捩れ平行移動で消すこと、最後に三乗根で指定周期を合わせることである。厳密dg character作用・全次数格子を保持した外積・二重同変化から実核へ戻す。関係式の指標と係数点の指標は反変なので、生成元の巡回・対角作用に対する定数係数点の作用はc(α₁,α₂,α₃)=(α₃,α₁,α₂)、d(α₁,α₂,α₃)=(α₁,ωα₂,ω²α₃)となる。この規約とSchurの補題により

\[
 L(e_a)=\ell X_a,\qquad Q(y_b^2)=q[Y_{b+1}Y_{b+2}],\qquad
 E_*\operatorname{KS}(M)=\kappa\sum_{a,b}M_{ab}[X_aY_{b+1}Y_{b+2}],
 \qquad \kappa=\ell q\ne0
\]

を得る（`ife:thm:projective-coefficients`）。交差二次式は、3τY_b²=(2+τ³)Y_{b+1}Y_{b+2}から全ての許容τでJac(f₂)₂の基底になる。この証明は2+τ³で割らないため、Fermat点τ³=−2も含む。第一因子をCliffordと仮定しない一般の場合には、元の係数表示でのκは未計算である。両Cliffordの場合は下記の三乗尺度と三次被覆を用いる。パラメータをκ倍して係数を1にすることを数値較正と呼ばない。

### 双方向十八変数族の正則域と実残余族

代数の証明の正本は [interfactor_clifford_bidirectional.tex](../papers/sections/mixed/interfactor_clifford_bidirectional.tex)、残余族は [interfactor_clifford_bidirectional_geometry.tex](../papers/sections/mixed/interfactor_clifford_bidirectional_geometry.tex)。両因子S(1,1,τ_i)、τ_i≠0、τ_i³≠1,−8、重みa_i≠0を固定し、独立行列Λ=(Λ_ab), M=(M_ba)を用いて

\[
 \{x_{a+1},x_{a+2}\}+\tau_1x_a^2=\sum_b\Lambda_{ab}y_b^2,\qquad
 \{y_{b+1},y_{b+2}\}+\tau_2y_b^2=\sum_aM_{ba}x_a^2,\qquad[x_a,y_b]=0
\]

とする。六つの平方は全係数で中心に残る。X_a=x_a²,Y_b=y_b²、p_a=Σ_bΛ_abY_b−τ₁X_a、s_b=Σ_aM_baX_a−τ₂Y_bとすると、対角X_a,Y_b・対応する非対角p_a/2,s_b/2を持つ二つの三次元Clifford代数の通常のtensor積であり、中央多項式環上自由階数64、H_B=(1−t)⁻⁶となる。体積元ω_x,ω_yに対しΩ_τ=2(1−τ³)ω、α_i=2a_i(1−τ_i³)、w=α₁ω_x+α₂ω_yと取る（`ifb:prop:family`）。wのnormのX₁³係数

\[
 c=\frac{\alpha_1^2\tau_1^2+\alpha_2^2M_{11}M_{21}M_{31}}4
\]

が非零の主開では、wは任意の係数変更後も左右正則で、商は底上平坦・次数別有限射影、H_{B/(w)}=(1−t³)(1−t)⁻⁶である。これはmonicなnormの乗法による普遍単射性から得る。二つの一方向軸は、指定中心元を含めて既存の九変数族に一致し、それぞれの軸全体での正則性は一方向定理による。大域的な自由基底を商へ無条件に主張しない。

**周囲代数の正確なAS-regular領域。** 二次双対は可換六変数の次の六二次式による商の、(Z/2)² cocycle twistとなる：

\[
 g_{x,a}=u_a^2-\tau_1u_{a+1}u_{a+2}+\sum_bM_{ba}v_{b+1}v_{b+2},\qquad
 g_{y,b}=v_b^2-\tau_2v_{b+1}v_{b+2}+\sum_a\Lambda_{ab}u_{a+1}u_{a+2}.
\]

Δ=Res(g_x,g_y)とするとΔ(0)≠0であり、複素fiberの有限大域次元・AS-regular性は正確にΔ≠0と同値である（`ifb:prop:dual`, `ifb:cor:exact-regular-locus`）。この開では六二次式が相対完全交叉をなし、双対の各次数は階数binom(6,i)の有限射影となる。Jacobian socleの向きとcocycle符号からgraded symmetric traceを得て、任意可換底変更に保たれる長さ六のKoszul双加群解消とuntwisted相対6-CY双対性を構成する（`ifb:lem:relative-ci`, `ifb:thm:regularity`）。複素fiberの大域次元・AS indexは六である。Δ=0では双対が無限次元となり、Koszul性を仮定せずTor_i(C,C)_i=(B^!_i)*からaugmentationの射影次元無限が従う。相対CY性を、特異な係数環を含む絶対C代数の有限大域次元と混同しない。

**保持する悪い点。** τ₁=τ₂=2、Λ=M=I₃ではu=v=(1,1,1)が双対六二次式の射影共通零点となり、Δ=0・大域次元無限である。一方H_B=(1−t)⁻⁶は保たれ、a₁=a₂=1ならc=196≠0なので中心三次はなお正則である（`ifb:ex:nonregular`）。従ってHilbert級数、周囲代数のAS-regular性、中心三次の正則性を同一条件としてはならない。

**実残余族と十八次元の形式像。** D(cΔ)の分離原点近傍で、B/(w)の四次元型およびB[u]/(w+γu³)、γ≠0の五次元型は、実相対smooth proper残余模型・底変更に両立するrotationを持つ。各複素fiberでは全coherent Kuに一致し、さらにétale局所perfect核で滑らかな可換三次へ比較できる（`ifg:thm:smooth-neighborhood`, `ifg:cor:local-comparison`）。通常のcoherent対角を正則底上で有限線束複体のretractへ移す証明であり、Δ≠0だけから残余smoothnessを推論しない。四次元型のKS像はJac(f₁)₁⊗Jac(f₂)₂⊕Jac(f₁)₂⊗Jac(f₂)₁、階数18で、標識付き幾何的20次元変形空間への形式像は余次元2の正則閉部分である（`ifg:cor:rank-eighteen`）。残余smooth locus全体と二本の形式方程式の高次係数は未決定だが、次項のA₂例はD(cΔ)の内部にも非smooth係数があることを示す。

### 階数一の周囲判別式と残余A₂特異点

正本は [interfactor_clifford_rank_one.tex](../papers/sections/mixed/interfactor_clifford_rank_one.tex)。Λ=λE₁₁、M=μE₁₁と制限すると、六二次式の射影共通零点を分類できる。零点では両ブロックの全座標が非零となり、各ブロックの後二式を解くと三乗根を含む有限個の枝に帰着する。残る二式の行列式から

\[
 V(\Delta)=V(h),\qquad
 h=(1-\tau_1^3)(1-\tau_2^3)-\tau_1^2\tau_2^2\lambda\mu
\]

を得る（`ifd:prop:ambient-locus`）。これは終結式の零集合についての厳密な等式であり、因子の重複度は決めていない。従って周囲AS正則域は正確にD(h)である。他方c=α₁²τ₁²/4は全スライス上の非零定数なので、中心三次の正則性・商の平坦性はh=0でも保たれる。

τ₁=τ₂=τ、a₁=a₂=1、λ=μ=−3τでは

\[
 h=-(4\tau^3-1)(2\tau^3+1),\qquad c=\tau^2(1-\tau^3)^2.
\]

τ≠0、τ³∉{1,−8,1/4,−1/2}なら、周囲代数は六次元Koszul AS正則・非捩れCYで中心三次も正則であるが、平方座標[1,0,0;1,0,0]に残余特異点を持つ（`ifd:thm:residual-a2`）。ここではdet q_x=det q_y=−4τ²≠0で、norm D=det q_y−det q_xのY₁=1, X₁=1+tの局所式は、横Hessian行列式(τ³−1)⁴、臨界切断上の値τ²t³/4を持つ。

射影圏への移行には内部次数一の中心単元ζ=ω_x/Y₁を使う。d_x=det q_x/Y₁³とするとY₁=−ζ²/d_x、ω_x=−ζ³/d_xとなり、中心の次数零chartをnorm超曲面へ正確に同定できる。次数零のClifford代数はその上次数四のAzumaya代数で、完備化は

\[
 \operatorname{Mat}_4\!\left(\mathbb C[[t,u,v,r,s]]/(t^3+uv+rs)\right)
\]

となる。有限中心の射影模型に単純加群を延長した一点対象の自己Ext級数は(1+z)⁵/(1−z²)。有限例外mutation後も高次自己Extの次元16が残るため、全coherent残余圏は非proper、properな残余線束圏は非smoothである。次数を忘れたaffine MFの比較から射影Kuへ外挿した結論ではない。

有理数係数例はτ=2、Λ=M=−6E₁₁であり、h=−527、c=196、両行列式−16、横Hessian行列式2401となる（`ifd:ex:rational-a2`）。これによりD(Δc)全体を残余smooth locusとする可能性は排除される。二次形式の退化部分まで含めた正確な残余判別式、norm三次への実Ku核は未構成である。このsource自体は非smoothなので、滑らかなnc cubicに関する主予想の反例ではない。

### 二つの因子係数を動かす二十変数と尺度較正

正本は [interfactor_clifford_versal.tex](../papers/sections/mixed/interfactor_clifford_versal.tex)。τ_i(τ_i³−1)(τ_i³+8)を逆にした二次元底Tの上で十八混合係数も動かし、重みa_iは固定する。α_i=2a_i(1−τ_i³)として、Clifford表示・resultant開・相対6-CY性・実残余近傍はいずれもこの底上で成立する（`ifb:cor:moving-factors`, `ifg:thm:smooth-neighborhood`）。尺度については方程式を厳密に

\[
 f_t(\mathbf Z)=t\sum_b Z_b^3-(2+t^3)Z_1Z_2Z_3,\qquad
 F_{\boldsymbol\tau}=a_1f_{\tau_1}(\mathbf X)+a_2f_{\tau_2}(\mathbf Y)
\]

と固定する。

**純因子を動かす実核。** 点曲線の零点o=(1:−1:0)、非零二捩れ点p=(1:1:τ)に対するM=O(p−o)を相対線束として使う。主稿 `mbrn:cor:factor-boundary` の二捩れを許す相対一因子windowと、相対Poincaré核の実同型からPicard比較を構成する。Hom線の局所自明化と有限étale三乗根で周期を合わせ、相対Thom–Sebastiani・全次数格子・二重同変化へ移す（`ifv:lem:moving-split-kernel`）。これは各閉点の同値だけから相対同値を推定する議論ではなく、2p≠0を仮定する別の相対積定理をそのまま適用するものでもない。Heisenberg補正の三捩れ選択も有限étale局所で延ばせるので、同じ原点核の下で純・混合方向を比較できる。

この実相対比較から、純因子のKSは

\[
 E_*\operatorname{KS}(\partial_{\tau_i})
   =\frac{2a_i(1-\tau_i^3)}{\tau_i}[Z_{i1}Z_{i2}Z_{i3}]
\]

となり、全ての許容分離点で非零である（`ifv:prop:pure-tangents`）。二つの純Jac₃方向と十八混合方向は直和でJac(F)_3全体をなす。したがって二十変数のKSは同型であり、原点を標識した通常Artin変形の形式写像は、滑らかな二十次元形式円板同士の同型となる。実際の局所三次族の分類写像は三次四様体のモジュライスタック[U_sm/PGL₆]へétaleである（`ifv:thm:versal`）。有限自己同型を無視した粗モジュライへのétale性、一般の22次元圏変形全体、全三次の大域一意表示は主張しない。

**一般係数とモジュライの稠密開。** `ifv:cor:generic-comparison` は、既存の実比較核を持つ一つの整な有限型étale chartを制限し、二十変数係数空間Pの非空開Uと有限étale全射V→U、V上の滑らかな可換三次族・相対perfect核を得る。PGL₆-torsorを先にétale局所自明化するので、一般係数体K=C(P)のある有限分離拡大L上で実際のX_L⊂P⁵_Lと全coherent Ku比較を持つ。分類写像V→[U_sm/PGL₆]もétaleで、その非空な開像はモジュライの既約性から稠密である。従ってこの開像の各複素三次四様体は本Clifford族のあるfiberで実現される。接空間の次元から大域核を推測する議論ではない。有限化後のUが最初の分離点を含むこと、核や可換族のPへの降下、全smooth係数または全可換三次の被覆、被覆の最小次数は結論しない。

**元の関係係数での較正。** 一つのClifford因子の三定数方向へそれぞれεz_b²を中心代入して加えると、τはτ−εに動く。固定交代語と標準Ω_{τ−ε}の比(1−τ³)/(1−(τ−ε)³)=1−3τ²ε/(1−τ³)は重みの変化だけであり、ブロック生成元の三乗根scalar倍で消える。このfull classと上の純KSを比較して

\[
 \ell_iq_i=\frac{2a_i(\tau_i^3-1)}{3\tau_i},\qquad
 \kappa_{12}\kappa_{21}
   =\frac{4a_1a_2(\tau_1^3-1)(\tau_2^3-1)}{9\tau_1\tau_2}
\]

を得る（`ifv:prop:scale-calibration`）。同一τ・同一aでは同じ一因子選択の外積をブロック交換に両立させ、κ₁₂=κ₂₁=2a(τ³−1)/(3τ)を得る。平方の値から未指定の符号を選んだのではない。Fermat点ではκ=−2a/τとなる。一般の異なるClifford因子の尺度は次項の三乗式と三次被覆で決まる。各ℓ_iとq_iの個別値、一般の非Clifford第一因子のκは未計算である。方程式を別のscalar倍に変えた場合やS(1,−1,−1)のκ²=27/28へこの値を流用しない。

### 一般Clifford二因子の尺度と非自明な三次被覆

正本は [interfactor_clifford_scale.tex](../papers/sections/mixed/interfactor_clifford_scale.tex)。定数PBW一因子のClifford行列qと、det H_τ=−f_τを満たすHesse行列H_τを用いる。ω≠0上では、Ω_τの中心臨界スキームと∇f_τ(z)=α, f_τ(z)≠0の臨界スキームが

\[
 q=-\operatorname{adj}H_\tau(z),\quad \omega=-f_\tau(z),\quad
 z_a=\operatorname{adj}(q)_{a+1,a+2}/\omega
\]

で互いに逆に対応する（`ifm:lem:adjugate-critical`）。臨界値はΩ_τ=(1−τ³)(f_τ−α·z)なので、各許容τの一般αで八個の相異なる非零Azumaya Morse値を得る。det q=0の非Azumaya点を、この同型に含めてはいない。

二因子の八値から64個の相異なる非smooth中心係数を検出し、既存 `euk:thm:universal-kernel` の実全係数比較と可換臨界代数の階数64を併用して値集合の等号を得る。非Azumaya部分を先に全分類したことにはしない。二次moment m_τ(α)=Tr((f_τ−α·z)²)は全ての許容τで非零多項式である（`ifm:lem:moment`）。同じ原点核・指定周期での定数Bocksteinがeukとiftの両方に現れるため、可換u²係数b_iの比はℓ₁/ℓ₂に等しい（`ifm:lem:same-bockstein`）。重みを含むmomentは可換側b_i³m_i/a_i、非可換側a_i²d_i²m_i、d_i=τ_i³−1となる。共通中心尺度κ_cを二式の比で消して

\[
 \frac{\ell_1^3}{\ell_2^3}=\frac{a_1^3d_1^2}{a_2^3d_2^2},\qquad
 \kappa_{12}^3=\frac{8a_1^3d_1^2d_2}{27\tau_2^3},\qquad
 \kappa_{21}^3=\frac{8a_2^3d_2^2d_1}{27\tau_1^3}
\]

を得る（`ifm:thm:scale-cubes`）。従って一般の尺度比を未確定の自由な複素定数として扱う必要はない。ただし原点核・比較射を固定すると、その三乗根の一つは既に選ばれており、任意に取り直せる数値とは区別する。

正規化比θ=(a₂τ₂/a₁τ₁)(κ₁₂/κ₂₁)について

\[
 \theta^3=\frac{d_1}{d_2},\qquad
 \kappa_{12}=\frac{2a_1d_1}{3\tau_2\theta},\qquad
 \kappa_{21}=\frac{2a_2d_2\theta}{3\tau_1}
\]

となる（`ifm:cor:kummer-scale`）。可換標的の実ブロックスカラーのgraph核を原点比較へ後合成することにより、指定周期を保ったまま三つの値を実現できる。τ_iの許容開T上のこの有限étale三次被覆は非自明であり、τ₁=1に沿う付値が一なので関数体上の有理切断は存在しない。これは混合尺度の被覆であって、実核全体の最小定義体、Picard・Heisenberg・周期の全標識の同時降下次数ではない。

### 階数一の Azumaya 残余判別曲線

正本は [interfactor_clifford_rank_one_caustic.tex](../papers/sections/mixed/interfactor_clifford_rank_one_caustic.tex) の ifq 定理群。rank-one の周囲AS正則域は h=(1−τ₁³)(1−τ₂³)−τ₁²τ₂²λμ≠0、中心三次は全切片で正則という既存結果を使う。中心 norm の平方座標軸への制限は P=α₁² X(λY−τ₁X)²−α₂²Y(μX−τ₂Y)² で、Disc(P(X,1))=α₁²α₂²(λμ−τ₁τ₂)²Q。Q=4α₁⁴τ₁λ³+α₁²α₂²(λ²μ²+18τ₁τ₂λμ−27τ₁²τ₂²)+4α₂⁴τ₂μ³。Q=0、λμ≠τ₁τ₂、h≠0ではAzumaya軸上に特異中心局所環があり、点対象の無限自己Ext、全coherent残余非proper、線束残余非smoothが従う。これは全判別の必要十分条件ではない。

等τ・等重みでは l=λ/τ,m=μ/τ として Qの正規化は l=−z²−2/z, m=−2z−1/z²。三つの通常 cusp は (l,m)=(-3ξ,-3ξ²), ξ³=1。z³≠±1の一般点ではA₁、z³=1では横Hessian非退化のA₂（τ³≠1,-8,1/4,-1/2を仮定）。z³=-1は非Azumaya境界との交点なので本結論から除外する。有理A₁証人 τ=2, λ=15/2, μ=−6, a_i=1 では h=769,c=196、軸点 [X₁:Y₁]=[1:4]、両行列式−49/16、五変数の規格化Hessian行列式−10596600。計算証明書は [verify_rank_one_caustic.py](../computations/verify_rank_one_caustic.py)。この中心normを可換Ku標的の三次方程式と無条件に同一視しない。

### 固定した三次切片と高次項の十二係数

正本は [interfactor_clifford_jets.tex](../papers/sections/mixed/interfactor_clifford_jets.tex)。添字をZ/3={0,1,2}とし、三次形式の補空間を

\[
 C=\langle X_aY_{b+1}Y_{b+2}\rangle_{a,b}
   \oplus\langle X_{a+1}X_{a+2}Y_b\rangle_{a,b}
   \oplus\langle P_X,P_Y\rangle,
 \qquad P_X=X_0X_1X_2,\quad P_Y=Y_0Y_1Y_2
\]

と固定する。これは全許容因子でJac(F)₃へ同型に写り、三次形式全体はGL₆の軌道接空間36次元とCの20次元に分かれる。形式逆写像定理により、恒等に還元される射影座標変更と切片F+Cへの正規化は一意である（`ifj:lem:linear-slice`）。従って元の非可換係数Λと原点比較を固定すれば、切片の係数(u_ab,v_ab,z₁,z₂)には意味がある。

Heisenberg対称性だけでは二次写像Sym²V→V*が五次元、三次不変式が五次元で、純二方向を値に取る三次写像は十次元である（`ifj:prop:heisenberg-bases`）。非可換側−P・可換側Pによる因子反転に両立する実原点核を追加で構成すると、それぞれ4・8次元へ減る（`ifj:lem:reflection-kernel`, `ifj:cor:reflection-bases`）。この4+8を、任意に固定したHeisenberg同変核へ無条件に適用しない。二捩れPicard線束の[3]降下と反転、top syzygyの符号、rotation比較射の文字ε²=ε³=1を保持して追加構造を構成している。

四つの三次不変式は、全成分の立方和I₀、行積和I_r、列積和I_c、六置換積の和I_d=I_++I_-でよい。二次写像の基底は、成分平方Q₀、同じ列の他二行の積Q_r、同じ行の他二列の積Q_c、二つの対角積の和Q_d=Q_++Q_-である。det Λ=I_+−I_-は反転で排除される。選んだ追加同変核では

\[
 u(\Lambda)=\kappa\Lambda+O(\mathfrak m^4),\qquad
 v(\Lambda)=\sum_{e=0,r,c,d}\beta_eQ_e+O(\mathfrak m^5),\qquad
 z_i(\Lambda)=\sum_{e=0,r,c,d}\gamma_{ie}I_e+O(\mathfrak m^6)
\]

となる（`ifj:thm:twelve-coefficients`）。βの四個とγの八個は固定した因子・重み・原点比較の係数であり、新しい十二変形パラメータではない。**その数値、消滅・非消滅は未計算である。**

計算の最短の入口は、E₀₀、E₁₀+E₂₀、E₀₁+E₀₂、E₁₁+E₂₂、第一行和、第一列和、I₃という七つの一変数族Λ=tAである。固定切片への正規化後の[t²]v₀₀と[t³]z_iから、`ifj:eq:probe-table`に従って十二係数を回収できる。各制限では中心持上げ・実核・Jacobian補空間への射影を三次まで追う必要があり、normや点曲線の形式だけを可換方程式と見なすことはできない。

任意の標的形式座標変更なら全高次項を消して(κΛ,0,0)へ移せるが、これは固定した多項式切片の係数を計算したことにはならない（`ifj:prop:formal-straightening`）。一方、一次部分が恒等の同変な源座標変更の最初の補正は四次なので、上の二次・三次係数は変わらない。形式座標に関するこの区別を計算時にも維持する。

**残る具体課題と到達基準。** 第一に七制限の実比較を三次まで計算し、固定切片の十二係数を求める。第二に階数一のD(h)内で、Azumaya norm特異点と二次形式退化部分を分けて残余smooth locusの方程式を調べる。A₂例は除外すべき係数を既に与えるが、全判別式ではない。第三に、構成済みの有限étale比較被覆がどの残余smooth係数まで延長できるかを実核のperfect性と同値性で判定する。尺度θの三次被覆だけから全核の降下を結論しない。一般の非Clifford第一因子の尺度、任意の複数ordered pairの同時積分、全intrinsic表示被覆も残る。

有限計算の入口は `verify_clifford_morse_scale.py`（随伴行列・moment・三乗尺度）、`verify_clifford_rank_one.py`（h・norm局所式・Hessian・有理係数例）、`verify_clifford_jets.py`（全低次同変空間・反転・七制限・Hesse補空間）である。いずれも厳密な有限代数計算であり、実核・coherent飽和・指定周期・高次十二係数の数値を機械検証したとはしない。実行と組版・保存の状態は `validation.md` を正本とする。

### Clifford族・尺度・局所比較に使う一次文献

- Cassidy–Vancliff, *Generalizations of graded Clifford algebras and of complete intersections*, J. Lond. Math. Soc.81(2010),91–112, [DOI](https://doi.org/10.1112/jlms/jdp057), [著者版](https://bpb-us-e1.wpmucdn.com/websites.uta.edu/dist/0/5123/files/2022/10/scliff.pdf), Definition1.12・Theorem4.2とその証明。base-point-free条件には必ず [2014年訂正](https://doi.org/10.1112/jlms/jdu030), J. Lond. Math. Soc.90(2014),631–636, [著者版](https://bpb-us-e1.wpmucdn.com/websites.uta.edu/dist/0/5123/files/2022/10/scliff-cor.pdf), Definition2・Proposition10・Corollary11を含める。通常のpoint moduleだけでなくfat point moduleを含む条件である。本表示のΔによる正確な領域と任意底の有限解消は、本文の具体的cocycle twist・相対完全交叉で証明する。
- Hu–Mori, *Clifford quadratic complete intersections*, [arXiv:2302.04446v3](https://arxiv.org/abs/2302.04446v3) (2023), Theorem3.21・Corollary3.22（通常のClifford型と可換二次完全交叉の双対）、Theorem3.28（中心二次正則列の商への双対）、Corollary3.13（通常のClifford quantum polynomial algebraがCYであるのは次元が奇数のときに限る）。本六生成元族はブロック間が可換なgraded skew Clifford型で、双対の非自明cocycleとsocle parityが6-CYの符号を相殺する。可換完全交叉との一般双対性を新規成果とはしない。既知の中心二次商と本稿の中心三次商を区別する。
- Berger–Marconnet, *Koszul and Gorenstein properties for homogeneous algebras*, Algebr. Represent. Theory9(2006),67–97, [arXiv:math/0310070v2](https://arxiv.org/abs/math/0310070v2), [DOI](https://doi.org/10.1007/s10468-005-9002-1), Theorem6.3・Proposition6.4（preprint pp.28–29）。He–Van Oystaeyen–Zhang, *Deformations of Koszul Artin–Schelter Gorenstein algebras*, Manuscripta Math.141(2013),463–483, [arXiv:1302.0390](https://arxiv.org/abs/1302.0390), [DOI](https://doi.org/10.1007/s00229-012-0580-z), Lemmas1.1–1.2。Koszul双対のFrobenius性からAS-Gorenstein性・Nakayamaを読む既知機構と、本族の任意底・untwisted符号の具体確認を区別する。
- Cremona–Fisher–O’Neil–Simon–Stoll, *Explicit n-descent on elliptic curves. I. Algebra*, J. reine angew. Math.615(2008),121–155, [arXiv:math/0606580v1](https://arxiv.org/abs/math/0606580v1), [DOI](https://doi.org/10.1515/CRELLE.2008.012), §1.6 Definition1.29（theta群の交換子とWeil対合）、Lemma1.27（E[n]の指標）、Lemma4.8（対合の非退化性）。これがH₃同変Picard比較でHom線の指標を三捩れ平行移動により消す入力である。
- Buchweitz–Pavlov, *Moore matrices and Ulrich bundles on an elliptic curve*, Enseign. Math. (2)70(2024), no.1/2, 1–24, [DOI](https://doi.org/10.4171/LEM/1018), [arXiv:1511.05502](https://arxiv.org/abs/1511.05502), [出版PDF](https://ems.press/content/serial-article-files/47659?nt=1), §§2.1,2.6。H_τは既知Moore行列M_(τ,1,1),zの第二・第三行を交換した表示である。既知のHesse行列式・随伴行列の幾何と、本稿の非零体積上のaffine臨界スキーム同型および尺度較正を区別する。書誌キー `IFMBuchweitzPavlov`。
- Beauville, *The Coble hypersurfaces*, C. R. Math. Acad. Sci. Paris337(2003),189–194, [DOI](https://doi.org/10.1016/S1631-073X(03)00302-9), [arXiv:math/0306097v1](https://arxiv.org/abs/math/0306097v1), §1 Proposition1と証明（著者稿pp.2–3）。level三の九次元Heisenberg表現では三次不変式が五次元で、微分が二次同変写像を与えることは既知である。本稿の五つの単項式軌道の具体表示、反転を保つClifford/Picard核、固定切片の4+8係数への適用と分ける。書誌キー `IFJBeauvilleCoble`。
- Eisenbud–Peeva, *Minimal Free Resolutions over Complete Intersections*, LNM2152, Springer, 2016, [著者PDF](https://pi.math.cornell.edu/~irena/papers/ci.pdf), Construction4.1.3・Proposition4.1.4・Remark4.1.5（著者稿pp.36–37）。Koszul分解と高次homotopyから得るShamash/Tate分解が既知入力である。A₂例では本文でdθ=t²e_t+v e_u+s e_rと極小性を具体的に確認し、(1+z)⁵/(1−z²)を計算する。次数付き中心局所化から射影圏へ移す論証は別に必要である。書誌キー `CMOEisenbudPeeva`。
- Stacks Project, [Tag02NW](https://stacks.math.columbia.edu/tag/02NW), Lemma29.52.1：準コンパクト・準分離・局所有限型で有限一般ファイバーを持つ射は標的の適当な非空開上で有限となる。[Tag03FQ](https://stacks.math.columbia.edu/tag/03FQ), Lemma66.16.7と[Tag04XB](https://stacks.math.columbia.edu/tag/04XB)：代数空間のétale射の開性とrepresentableな性質のスタックへの移行。これらを既存の実比較chartへ適用するのが `ifv:cor:generic-comparison` であり、標準的な一般点有限化そのものの新規性は主張しない。Azumaya代数の局所行列表示の規約は[Tag0A2J](https://stacks.math.columbia.edu/tag/0A2J)による。以上の本文を2026-11-23に確認した。

- Kuznetsov, *Derived categories of cubic fourfolds*, [arXiv:0808.3351v1](https://arxiv.org/abs/0808.3351v1), §4 Lemma4.2・Theorem4.3。平面を含む三次四様体をquadric surface fibrationへ移し、同節で課す各fiberのrank≥3の下で、偶Clifford代数の圏とtwisted K3の圏・残余圏を比較する。本稿の六生成元の相互補正・中心三次変形族とは構成と仮定が異なる。既存書誌キー `NFKuznetsovCubicFourfolds` を使う。
- Baumann–Belmans–van Garderen, *Central curves on noncommutative surfaces*, [arXiv:2410.07620v1](https://arxiv.org/abs/2410.07620v1) (2024), TheoremA（大域次元2のtame orderを中央曲線へ制限する比較）、§6 Proposition50・§6.1（三変数skew cubicと可換曲線の比較）。中心商の幾何比較の近接例として参照するが、四様体の二十変数の局所完全性を述べる入力として用いない。

これらの一般機構は既知結果として使う。今回の文献確認は、列挙した一次資料と近接するHeisenberg・Picard・Clifford理論の限定調査であり、引用・被引用文献全体やMathSciNet/zbMATHの網羅的調査ではない。随伴行列の一般恒等式、五つのHeisenberg不変式、Shamash分解、étale射の開性を新規成果とはしない。本表示における混合尺度の三乗とKummer障害、正則域内の射影A₂例、固定切片の十二係数還元、実二十変数核からの稠密開比較について、証明の所在は本文に明記したが、厳密な初出・網羅的な新規性は未確認である。外部査読・形式証明器による確認も未了である。外部文献PDFは現行一式へ複製せず、書誌と参照箇所を保持する。

### 全smooth領域の相対模型と比較不変量

`cmo:prop:full-relative-hh` は、U=Spec C[c,P64(c)⁻¹]上で指定c族の有限線束模型・残余模型を相対smooth properにする。固定ambientのKoszul解消、全cでの中心三次の正則性から次数別自由商を作り、有限中心C_R、Z=Proj C_R^(6)、通常のcoherent代数Λ=𝒜^op⊠𝒜と対角加群M=Δ_*𝒜を使う。Λ,Mの底上の平坦性とZ×Zのproper性を確認し、各smooth閉点での対角perfect性を `cmo:prop:proper-perfect-spread` で近傍へ延ばす。これは一般のproper dg族のfiberwise smoothnessからの推論ではなく、下記のEnd(R→^tR)の障害を避ける具体的な構成である。

Mathew, *Kaledin’s degeneration theorem and topological Hochschild homology*, [arXiv:1710.09045v3](https://arxiv.org/abs/1710.09045), Theorem1.3（Geom.Topol.24(2020),2675–2708）をこの実相対族に適用すると、各HH_iはU上の有限射影加群となる。既存の余有限可換実現で階数を求め、Uの連結性から全cでHH₀=C²、HH±₁=C²¹、他次数零を得る。特定候補X_cへの同値を入力にしない。とくに全smooth cで射影Kuは非零である。

`cmo:cor:rational-euler-comparison` は両側のe₄=[pr O(4)], e₅=[pr O(5)]を有理数値Grothendieck群の基底とし、共通Gram行列を[[-27,−189],[−162,−1161]]、det729と決定する。基底(e₄,e₅−7e₄)では27[[-1,0],[1,−1]]である。線束Euler数の多項式と例外射影から行列を直接計算し、HH₀の次元2とShklyarovの[dg HRR](https://arxiv.org/abs/0710.1937v3)、Theorem3.5・§3.2を使って基底性を証明する。全smooth係数の実Morita同値は、Euler形式を保つ積分数値Grothendieck群の同型も与える。ただし、この二つの線束射影類が積分基底であることや、構成した核がそれらをどの類へ送るかは未計算。c=0の対合はe₄,e₅を保つので、非可換側でもHH₀と有理Knum上は恒等である。

### c=0のEckardt点、根スタックと実残余模型

`cmo:prop:zero-eckardt-resolution` では、J=(x³+y³+z³+xyz)/3、G=J(x^(1))+100J(x^(2))、L=α^(1)·x^(1)+100α^(2)·x^(2)と置く。X₀=V(G−u²L)はλに依存せずQ上で定義される滑らかな五様体で、p=[0:⋯:0:1]の接超平面はL=0。その接切断は滑らかな三次三様体Y=V(G,L)⊂P⁵を底とするconeである。Z=V(G)は滑らかな分離型三次四様体であり、H=V(L)とYに沿って横断的に交わる。

四次分岐二重被覆S→P⁵をw²=LGで定めると、pからの射影はBl_p(X₀)→S→P⁵と因子化する。第一の射はcrepant resolutionで、SのYに沿う局所型はA₁ surface singularityと滑らかな三次元因子の積、解消の幾何ファイバーはY上でP¹、それ以外で一点となる。局所模型はw²=ab、解消上のcanonical classとSからの引戻しはともに−4q*O_(P⁵)(1)である。この可換側の幾何は、Z・Yおよび二重被覆のClifford/解消模型を非可換側の中心u²と比較する入口である。実際のKu比較には下記の球面境界類とcomonadの復元を使う。

`cmo:prop:eckardt-smooth-quotient` は、対合ι:u↦−uの商Bl_p(X₀)/μ₂をT=Bl_Y(P⁵)と同定する。狭義変換H′≅P⁴、Z′≅Zは互いに交わらず、分岐線束M=O_T(2h−e)を得る。商スタックℛ=[Bl_p(X₀)/μ₂]はH′⊔Z′の二乗根スタックである。根因子を𝓗,𝓩とすると、指標線束N=O_ℛ(𝓗+𝓩)⊗π*M⁻¹、B=π*O_T(h)⊗O_ℛ(𝓗)が明示され、ω_ℛ=π*O_T(−4h)⊗Nとなる。N²≃Oには被覆由来のcoherenceを指定する。

`cmo:thm:eckardt-root-residual` の16対象はB^r⊗N^εとj_*π_H*O_(P⁴)(s)⊗N^ε（r,s=0,…,3、ε=0,1）である。この順序の例外列の右直交KはKu(X₀)^μ₂に同値で、通常Ku(X₀)はKを−⊗Nで再同変化して回復できる。左mutation核Cone(F_i^∨⊠F_i→O_Δ)を最後の例外対象から順に適用すれば、Kへのperfect射影核になる。非可換側のKu(A₀)^μ₂からKへの核は、下記の二成分比較と接着によって構成する。使用する既知入力はOrlov1993 Theorem4.3、Ishii–Ueda2015 Theorem1.6・Proposition6.1、Elagin arXiv:1403.7027v2 Theorem4.2・§8であり、同変Serreの指標と実際の16対象を本候補で具体化した。新規性の網羅的確認は未完了である。

`cmo:prop:zero-involution-hh` は可換候補のHH±₁固有次元を(+5,−16)と決定する。Jacobian次数二の(+16,−5)からresidueへ移る際にdet(ι)=−1が掛かる。固定集合Z⊔{p}のEuler数28からもtrace−11を照合する。Ku(X₀)^μ₂のHHは次数−2,…,2で(1,5,24,5,1)。これとは独立に、`root_order.tex` の実mutationと可換Knörrer核により、Ku(Z)とKu(Y)の二成分SODそのものを構成した。HHの加法的一致によってSODを相殺したのではない。

非可換側のHH±₁のι指標も、h=0,1を含む実相対smooth proper模型から正負固有次元(5,16)と決まる。通常affine twisted HHから直接導く経路の注意点は別に保持する。u=1のchartでιは各active変数の符号反転、中心Ω_iは奇、六次中心元は偶である。中心の固定点集合だけのEuler数を非可換Lefschetz数へ置き換えず、Azumayaの内的実装・非Azumaya点の寄与を区別する。c≠0ではιはA_cとA_−cを交換するため、元c族の通常HHの階数一定性だけからc=0指標を導くことはできない。

### 零係数の同変三対象windowから再開する

証明の正本は混合稿 `equivariant_window.tex` の `cmo:prop:equivariant-window-hom`。G=K⊕K(1)⊕K(2)をaugmentationの自明な同変構造から取り、内部shiftに追加の指標を掛けない。uの反射をσとすると、Koszul空間W_iの指標は(1+z)^6(1−z)の係数である。σ不変なhigher homotopiesを段階的に選び、三次周期の指標が+であることを確認したminimal Shamash分解から、全stable Homを計算する。

| cohomological degree | 総次元 | σ=+1 | σ=−1 |
| ---: | ---: | ---: | ---: |
| −1 | 7 | 6 | 1 |
| 0 | 80 | 48 | 32 |
| 1 | 162 | 84 | 78 |
| 2 | 112 | 48 | 64 |
| 3 | 23 | 6 | 17 |

総次元は384。全13行のHom表と通常・対合付きEuler行列は本文に置く。通常の隣接二対象のEuler形式は27[[-1,0],[1,−1]]で、七本の線束からの独立な射影計算と一致する。`python3 computations/verify_mixed_window_involution.py` はこの有限計算を整数演算で再現する。

**この有限windowからHHを直接計算する際の残る入力。** H*End(G)のベクトル空間と対合の作用は確定したが、minimal A∞構造の高次積は未計算である。H¹Hom(K,K)の35次元からsuspension後に次数零のbar文字が生じるため、同じ総次数のbar語の長さは任意に大きくなれる。内部shiftも零であり、総次数や三次周期だけによる有限長打切りは正当化できない。同変Shamash模型から高次積と対角の有限解消を構成するか、twisted sectorの比較を曲率・内部次数付きで証明する必要がある。この直接計算は、既に得られた相対模型によるHH指標や実Ku同値の前提ではない。384次元の表やHomのsupertraceをHHの表・supertraceと置き換えない。

### 対合を保つh族と、有限中心法が使えない理由

証明の正本は混合稿 `equivariant_deformation.tex`。関係式[y,z]=h(x²−α₁u²)と巡回二式に対する中心三次元は

$$
\Omega_{h,\alpha}=\frac{x^3+y^3+z^3}{3}-\frac{2h^2}{3}\operatorname{sym}(xyz)-u^2(\alpha_1x+\alpha_2y+\alpha_3z).
$$

`mix:prop:h-central` の証明はhで除さない普遍恒等式である。指定二ブロックの中心和を商したQ_hではu↦−uが底を固定し、Q_1=A₀となる。Q_0のProjであるFermat型Eckardt五様体Y_Fは、既存候補X₀とは異なる方程式を持つ。Y_Fの滑らかさとHH±₁固有次元(+5,−16)は `mix:prop:fermat-eckardt-endpoint` に証明を置く。

一般点K=C(h)でQ_ηは非PIである（`mix:prop:h-generic-nonpi`）。u=0のSklyanin曲線E_h: x³+y³+z³+h²xyz=0上の平行移動点p_h=(1:−1:−h)は、形式群でt(p_h)=−h/2となるため非捩れである。標準中心元はg_h=−3h Ω̄_hで、Q_ηはTHCR B(E_h,O(1),t_p)を商に持つ。無限の平行移動軌道上のm点に次数3d>mの切断を補間すれば、任意の非零多重線型恒等式を排除できる。このため既存の有限中心・properな中央台による相対対角の証明は適用できない。

`mix:thm:h-semilocal-smooth` は、0,1を含む半局所底上の全coherent残余模型に相対perfect対角を構成する。左右noetherian性、Torのpro-zero性による有限cohomological dimension、通常二重次数射影積でのcoherent Ext有限性、閉ファイバーでcompactな通常coherent加群のNakayama持上げを使う。七線束の模型と四例外の残余射影を保ち、対合作用も底上で定義される。この実相対模型にMathewの退化と底変更を適用すると、非可換h=1でもHH±₁の正負固有次元は(5,16)、traceは−11、全HHの交代traceは24となる。追加の相対smoothness仮定は残らない。一般点非PIは有限中心法の適用を妨げるが、この通常coherent射影積の方法は妨げない。


### 指定h候補への実形式関手と一般点核

`mix:thm:h-formal-kernel` はbar flowのTaylor成分とその逆を有限rank graded MFへ挿入して実関手を構成する。三対象G_hとその像のendomorphism模型Γ,Λ上にはgraph双加群P,Qがあり、P⊗_Γ^L Q≃Λ、Q⊗_Λ^L P≃Γ。`mix:prop:h-kernel-jet` は一次F₃=(h/t)HKR(Ξ₀)、逆は符号反転と明示し、二次potential F+h²(P₁+100P₂)/3を得る。この二次classはJac(F)₃で非零なので、固定Y_Fへのmarked定数比較はh³切断まで延ばせない。

`mix:thm:h-exact-candidate` はさらに全形式次数で指定候補へ比較する。普遍αの段階ではC[α,u]に相対的な通常formalityと中心逆像のみを用いる。Heisenberg群H₂₇と補助weight(u)=1,weight(α)=−2により、一ブロックの逆像はa(h)Σx³/3+b(h)xyz−c(h)u²α·xの三係数に限られる。block間の微分辺と余分な閉clusterの消滅が積・中心写像の両立を与え、両ブロックで同じa,cを使える。u=0の通常模型に三変数curved flowを改めて適用し、THCR・楕円derived比較・jからb/a=h²/3を決める。七変数MFのu=0非平坦底変更は使わない。xをa^(−1/3)、共有uを(ca^(−1/3))^(−1/2)倍すれば、potentialは厳密にW_h^candへ移る。

指定αに戻した後の形式MF同値はσと三次周期を保つ。固定三対象の局所化・有限定義体降下により、C(h)の有限拡大上で指定X_h^candへの実perfectKu核が存在する。これは核の存在を与える構成であり、全行列・係数・拡大次数を算出したわけではない。`mix:thm:h-integral-kernel` はこの選択済み核をh=1の局所環の有限整閉包上、さらに各DVR上のperfect整核へ延長する。通常coherentな二重次数複体の格子を取り、相対smoothnessからperfect性を得る。次は整延長の中でunit/counit defectが零となる核を作り、固定c=0で構成した核との互換性を与える。元の中心係数c族は全smooth開上で比較済みであり、このh方向の選択済み核の互換性とは別問題である。

検算は `python3 computations/verify_mixed_formal_kernel.py`。Jacobi/Casimir、Ξ₀、Θとeye補正、非零Jacobian class、Hesse jの局所逆と共通座標正規化を厳密に確認する。一般formality・全次数核・代数化の証明を有限計算の成功だけで置き換えない。

### 中心変数の反射と通常の twisted Hochschild homology

以下は通常の代数の導来テンソル積についての補題であり、曲率付き Hochschild 複体や次数付き行列因子化圏への適用を主張しない。

**補題（中心変数の消去）。** 体 $k$ 上の代数 $A$ と中心元 $u$ を取り、指定した準同型 $k[u]\to A$ に関して $A$ が平坦であると仮定する。$\gamma\in\operatorname{Aut}_k(A)$ が $\gamma(u)=\lambda u$、$\lambda\in k^\times\setminus\{1\}$ を満たすとする。$\bar A=A/(u)$ とし、誘導される自己同型を $\bar\gamma$ と書く。右作用を $\gamma$ で捻った双加群を $A_\gamma$ とすれば、導来圏 $D(k)$ に自然な同型

$$
A\otimes_{A^e}^{\mathbf L}A_\gamma
\simeq
\bar A\otimes_{\bar A^e}^{\mathbf L}\bar A_{\bar\gamma}
$$

がある。特に全ての整数 $i$ について

$$
HH_i(A,A_\gamma)\cong HH_i(\bar A,\bar A_{\bar\gamma})
$$

となる。$A$ が内部次数付きで、$u$ が正の次数の斉次元、$\gamma$ が次数を保存する場合、同型は内部次数も保存し、ホモロジー次数・内部次数のいずれにも追加の shift は生じない。

**証明。** $E=A\otimes_k A^{\mathrm{op}}$、$u_L=u\otimes1$、$u_R=1\otimes u$、$t=u_L-u_R$ と置く。対角双加群 $A$ を右 $E$-加群として $a\cdot(b\otimes c^{\mathrm{op}})=cab$ で実現し、$A_\gamma$ を左 $E$-加群として $(b\otimes c^{\mathrm{op}})m=bm\gamma(c)$ で実現する。この規約では $t$ は対角 $A$ 上では零、$A_\gamma$ 上では $(1-\lambda)u$ として作用する。

$k[u]$-平坦性により $E$ は $k[u_L,u_R]$-平坦である。したがって $t$ は $E$ 上の中心的非零因子であり、

$$
D=E/(t)=A\otimes_{k[u]}A^{\mathrm{op}}
$$

は $k[u]$-平坦である。$D$ の $E$ 上の二項自由分解を $A_\gamma$ とテンソルすると、微分は $(1-\lambda)u$ となる。これは $A_\gamma$ 上で単射なので

$$
D\otimes_E^{\mathbf L}A_\gamma\simeq\bar A_{\bar\gamma}
$$

を得る。右辺は自然に

$$
D_0=D/(u)\cong\bar A\otimes_k\bar A^{\mathrm{op}}
$$

の加群である。同様に、$D_0$ の $D$ 上の二項自由分解と $u$ の $A$ 上の単射性から

$$
A\otimes_D^{\mathbf L}D_0\simeq\bar A
$$

となる。導来テンソル積の結合法則を二度用いれば

$$
\begin{aligned}
A\otimes_E^{\mathbf L}A_\gamma
&\simeq A\otimes_D^{\mathbf L}
       (D\otimes_E^{\mathbf L}A_\gamma)\\
&\simeq(A\otimes_D^{\mathbf L}D_0)
       \otimes_{D_0}^{\mathbf L}\bar A_{\bar\gamma}\\
&\simeq\bar A\otimes_{\bar A^e}^{\mathbf L}\bar A_{\bar\gamma}.
\end{aligned}
$$

内部次数付きの場合、二項分解には通常の $(-\deg u)$ が入るが、どちらも零次の cokernel のみを残すため、最終同型に追加の shift はない。以上で証明を終える。

**今回の適用。** $A=A_0$、$\gamma=\sigma$、$\sigma(u)=-u$ とする。既存の中心変数の正則性から $u$ は $A_0$ 上の非零因子である。$A_0$ は非負内部次数付きなので、任意の非零多項式 $p(u)$ も最高次数成分を比較することで非零因子となる。従って $A_0$ は PID $\mathbf C[u]$ 上で torsion-free、したがって平坦である。$\sigma$ は残りの六生成元を固定し、

$$
B_0=A_0/(u)=(S\otimes S)/(\Omega_1+100\Omega_2)
$$

上で恒等作用を誘導する。よって

$$
HH_i(A_0,(A_0)_\sigma)\cong HH_i(B_0)
$$

が内部次数付きで成立する。これは affine cone の通常の twisted HH の計算であって、$HH_i(\operatorname{Ku}_{\mathrm{coh}}(A_0),\sigma)$ の計算ではない。局所化 $A_0[u^{-1}]$ に同じ変数反射を作用させた通常の twisted HH は、$2u$ が単元なので零になる。一方、射影 chart $u=1$ 上の作用は六生成元全ての符号反転であり、この消滅をその chart に移してはいけない。

**次数付き MF へ進む際の未解決箇所。** ポテンシャルの内部次数は三であり、次数付き MF では $[2]\cong(3)$ を保つ必要がある。仮に固定 sector による表示を用いるなら、$\zeta^3=1$ に対する $\sigma\zeta$ の全 sector と grading の不変条件を扱う必要がある。これらは全て $u$ を $-\zeta u$ に送るので通常の代数に関する上の補題は適用できるが、そこから曲率付き複体の準同型や通常の MF 圏の HH との同一視は従わない。具体的には、曲率を含む対角模型、そこでの変数消去、第一種と第二種の HH の比較、および全内部次数を保持した sector 分解を別々に証明する必要がある。

Polishchuk--Positselski, *Hochschild (co)homology of the second kind I*, [arXiv:1010.0982v2](https://arxiv.org/abs/1010.0982v2), Theorems 3.5.C--D と Section 4.8 は、第一種と第二種の比較を導く十分条件として対角生成条件を課す。Section 4.8 の行列因子化の直接的な適用例は可換正則環／滑らかな affine variety の場合であり、この非可換環への適用を既知とはしない。

**指標計算への位置付け。** $\mathcal K=\operatorname{Ku}_{\mathrm{coh}}(A_0)$ とする。既知の通常 HH の次元と $HH_0$ 上の恒等作用、同変 Mukai 双対から、$a=\dim HH_1(\mathcal K)^+$ と置けば

$$
\operatorname{str}(\sigma\mid HH_*(\mathcal K))=44-4a.
$$

相対h族の模型から既に $a=5$、固有次元 $(5,16)$、supertrace $24$ を得ている。smooth proper dg 圏の Lefschetz 公式はこの supertrace を $HH(\mathcal K,\sigma)$ の Euler 数と同定するが、上の affine cone 補題だけでその Euler 数を計算したわけではない。参照：Polishchuk, *Lefschetz type formulas for dg-categories*, [arXiv:1111.0728v7](https://arxiv.org/abs/1111.0728v7), Introduction (0.3)。なお $HH(\mathcal K)^\Gamma$ と $HH(\mathcal K^\Gamma)$ は異なる。一般の有限群作用に対する後者の分解は Nordström, *Finite group actions on dg categories and Hochschild homology*, [arXiv:2406.13866v2](https://arxiv.org/abs/2406.13866v2), Theorem 16 により twisted sector の中心化群不変部分を含む。

### 中心二重根の全coherent分解と実残余核

証明の正本は混合稿 `mixed/root_order.tex` とその二つの部分ソース `invariant_algebra.tex`, `invariant_comparison.tex`。通常Perfだけでなく、有限生成・有限次元torsionの保存と有界導来Serre商を確認し、全Db(qgr)の分解を構成した（`cmo:prop:graded-root-order`）。本小節は本文の証明を重複せず、実核の再開入口を記す。

R=A₀^σ、v=u²、S=R/(v)=A₀/(u)、C=A₀⋊μ₂、e_±=(1±σ)/2とする。右加群規約でiはC→Sによるinflation、j(M)=M⊗_R e_+C。長さ一の射影解消 e_+C(−1)→e_-C→S と双加群三角 Ce_+⊗_R e_+C→C→S が全coherent分解、随伴、unit/counitを与える。D=B^σはCY7・parameter8、R=D/(w)はparameter5である。

**実残余分解。** K_S=⟨O_S,O_S(1),O_S(2)⟩^⊥、K_R=⟨O_R,…,O_R(4)⟩^⊥ と置く。`cmo:thm:root-order-residual` は

$$
\operatorname{Ku}(A_0)^{\mu_2}=\langle\Phi\mathcal K_S,\Psi\mathcal K_R\rangle,
\quad \Phi(F)=L_{E_0^-}i(F(1)),\quad\Psi(M)=M\otimes_R e_+C
$$

を実perfect核で構成する。既存分離比較によりK_S≃Ku(Z)。貼合せは RHom_S(F,M⊗_R^L S)[−1] であり、L=−⊗_R^L Sは球面関手、unshifted cotwistはρ_R^(−2)[1]=Serre_(K_R)[−2]である。K_RのSerre³=[5]という関係だけから可換三様体と同定しない。指標χはSerre_(Ku(A₀)^μ₂)³[−7]で内在化され、二乗coherenceの差は核の有限次元可換自己準同型環内の平方根で補正する。通常Kuへは指標作用を保つ二重同変化を使い、忘却後の完全忠実性を仮定しない。

**第二成分と制限関手の実比較。** 可換R_cl=C[x₁,…,x₆,v]/(G−vL)では、ℓ=L、G=g+ℓQ、t=v−Qによりpotentialはg−ℓtとなる。rank一の次数付き核 (ℓ,−t) との外積でK_Rcl≃Ku(Y)を得る。非可換K_RからK_Rclへの核P_Rと、既存境界比較Eに対するdg自然同型 E∘L≃L_cl∘P_R は下記の球面境界類・coKleisli復元から構成する。`cmo:prop:root-order-comparison-criterion` はこの入力を五様体の核へ接着する。

**通常の切断が使えない理由。** 指定Lの二側商D/(L),R/(L)はv³³で消える有限次元環であり、qgr(R/(L))=0（`cmo:prop:invariant-linear-quotient-finite`）。可換Knörrer核の置換としてこの商を使わない。この障害は実Ku同値を否定しない。有限PBW双対からの曲率付きMF・有限縮約は下記の別の計算模型を与え、可換側との比較そのものは球面境界類から構成する。

### 固定零係数の境界類、comonadと実比較核

証明の正本は `mixed/spherical_comparison.tex` と `mixed/spherical_boundary_class.tex`。指定α¹=(1,4,9)、α²=(16,25,49)、重み1,100、h=1,c=0で、`cmo:thm:fixed-zero-commutative-kernel` はC線型dg Morita同値 Ku_coh(A₀)≃Ku(X₀)を実perfect核で構成する。固定した一つの対象の存在に留まらず、第二成分の核P_R:K_R≃Ku(Y)と球面制限を保つ自然同型を同時に得る。

`cmo:lem:spherical-bockstein` は球面制限の余単位三角から得るtwist射ν:Id→ρ_Sを、中心vによる一階変形R/(v²)のBocksteinと同定する。`cmo:lem:boundary-parameter-injection` はα↦νが単射であることを、境界代数Sのminimal Shamash Extで検出する。そこではExtがF[t]としてt-torsionfreeで、変形の像はq_α=−Σα_jξ_j²となり、periodを反転しても消えない。可換側の境界類は線型式Lの乗算である。境界の分離比較をHeisenberg作用とrotationに両立させ、ブロック交換で二ブロックの共通scalarを揃えると、適切なrotation同型の規格化によりνが一致する。

twist射の一致だけで全高次構造の一致を宣言しない。`cmo:prop:cubic-boundary-comonad-vanishing` は三次四様体境界のsector計算によって、正規化された全arityの障害群と比較群を消し、counit付きのcomonad比較を復元する。高次随伴・comonadの既知入力はWillumsgaardの一次資料に置く。球面twist/cotwistの周期から右随伴の像が生成することを示し、coKleisli模型をpretriangulated・冪等完備化してP_Rと制限intertwinerを構成する。最後に二成分を接着し、χ≃Serre³[−7]、有限次元HH⁰内の平方根による二乗coherenceの補正、perfect核上の二重同変化を用いて通常Ku同値を得る。χ-coherenceは独立の未解決仮定ではない。

この固定点定理はC上の通常dg Morita同値を主張する。元c族のc≠0・norm全64根・全smooth係数への拡張は、上記の中心超平面comonadによって得られた。一方、全行列の列挙、Qへの降下、全rotation・指定周期・元の中心作用の標識を同時に保つ比較、選択済みh一般点核と互換な同値族、他の表示と全intrinsic対象への拡張は残る。主張の新規性の網羅的確認、外部査読、形式証明器による検証は未完了であり、本文の証明と読解・有限検算の範囲は `validation.md` に分ける。

### 不変周囲代数の有限PBW双対と実曲率模型

対象は D=B^σ、v=u²、α¹=(1,4,9)、α²=(16,25,49)。本来の内部重みは六変数が一、v が二である。これとは別に、全七生成元の補助的な語長を一とする filtration を取ると、D は (S⊗S)⊗C[v] の quadratic-linear PBW 変形となる。中心 v の次数別自由性で S⊗S の斉次基底を持ち上げ、関係の αv 項が語長を下げることから associated graded を確認できる。以下の微分には potential のブロック重み 1,100 は入らず、それは w=Ω₁+100Ω₂ の追加データである。

一因子の二次双対 E₀=S! は basis (1,a,b,c,A=a²,B=b²,C=c²,T=abc) を持つ。積は ab=−C,bc=−A,ca=−B、逆順は符号反転、aA=Aa=bB=Bb=cC=Cc=−T、その他の degree-one と degree-two の積は零であり、四次以上は零である。これは S の三つの関係 yz−zy−x², zx−xz−y², xy−yx−z² の直交補空間から得られる。

F=E₀⊗E₀（graded tensor、dim64）とし、ε の cohomological degree を一、内部重みを二として

\[
 E=F\otimes\Lambda(\epsilon),\qquad
 d|_F=0,\qquad d\epsilon=q_1+q_2,
 \quad q_i=-\sum_{j=1}^3\alpha_j^{(i)}\xi_{ij}^{2}
\]

を取る。E は128次元で、q は F の偶中心元なので d は well-defined な導分、d²=0 である。符号は Positselski, *Nonhomogeneous quadratic duality and curvature*, arXiv:1411.1982v2, §§2.1–2.5 の規約 r+φ(r)=0、d=φ* による。元の r₁* は bc=−a² に対応する。§3.3 の PBW 定理、または associated graded が通常の Koszul 分解となる filtered Koszul 複体により、この有限 dg 代数は D の augmentation の非斉次 Koszul 双対を与える。filtered Koszul 複体の完全性は、下に有界な語長 filtration の associated graded が完全であることから従う。従ってその cohomology は Ext_D(C,C) を計算する。これを potential w を含む MF の模型と同一視しない。

F 上の m_q の degree 0,…,4 の階数は (1,6,10,6,1)、総階数24である。degree-two の10は、F₂=(E₀)₂⊕((E₀)₁⊗(E₀)₁)⊕(E₀)₂について両外側からの像の階数5と中央からの像の階数5の和である。後者は二つの非零線型汎関数による二方向の縮約で、両方の縮約の共通一次元条件により階数3+3−1=5となる。Frobenius 対によって後半の階数は前半と対称になる。

結果として H(E,d) の cohomological Betti 数は (1,6,14,19,19,14,6,1)、総次元80。非零な二次数 (cohomological degree,内部重み): 次元は (0,0):1, (1,1):6, (2,2):14, (3,3):14, (3,4):5, (4,4):5, (4,5):14, (5,6):14, (6,7):6, (7,8):1 である。交代 Hilbert 多項式は (1−t)⁶(1−t²)=H_D(t)⁻¹ と一致する。

`computations/verify_mixed_invariant_pbw_dual.py` は一因子の関係行列の直交補空間と次数≤4の有理行簡約から積を構成し、一因子結合則、q の中心性、d の二次数・d²=0、階数、二次数 cohomology と Hilbert Euler を確認する。Python 3 と SymPy が必要。既存の実行記録は5 PASS。形式証明器による検証、curved MF の構成、HH 計算、Ku 比較を実行したものではない。

wを保持した有限模型は `mixed/curved_invariant_model.tex` の `cmo:thm:finite-curved-invariant-model` で構成する。Eの双対からD自由Koszul複体を取り、実際の中心元wの乗算のShamash higher homotopyを有理係数の線型方程式で逐次解く。三次周期で畳み込むとrank64+64のgraded MF Q₁₂₈となり、そのcokernelは剰余体のstabilizationに一致する。選択した正の添字のhigher homotopyはσ₁,σ₂だけが非零であり、Σ_(a+b=n)σ_aσ_bの全必要恒等式を有限計算で確認する。−vLだけをClifford反交換関係として追加しFの積を固定する案は成立しない。仮に{ε,ξ_j}=tℓ_jならt⁻¹ad(ε)がF上でdξ_j=ℓ_jを満たす奇導分となるが、bc+a²等の関係に適用すると全ℓ_j=0を強制する。従って二次pairingだけによる比較は使わない。

曲率を含む縮約では、定数微分∂のrank24の部分を消すcontraction (i,p,h₀)を選び、Δ=δ₁₂₈−∂と置く。εの有無とhomological degreeに関する有限filtrationから(Δh₀)⁴=0を証明するため、B=(1+Δh₀)⁻¹は有限和でありh=1でも定義される。A=BΔ、d₈₀=pAi、I=i−h₀Ai、P=p−pAh₀、H=h₀−h₀Ah₀に対し d₈₀²=w、δ₁₂₈ I=I d₈₀、P δ₁₂₈=d₈₀ P、PI=1、IP=1−δ₁₂₈H−Hδ₁₂₈を得る。rank40+40のMF Q₈₀と両向きの写像・homotopyが実係数で得られ、形式級数のh=1への代入は使わない。80は自由MFの総rankであり、H(E,d)上の全A∞積を列挙した、または80次元のEnd代数を作ったという意味ではない。


右加群規約のMFをκ_Rとし、G_R=κ_R⊕κ_R(1)⊕κ_R(2)と置く。`cmo:cor:curved-invariant-end-model` はG_RがK_Rを生成し、Γ_R=End_dg(G_R)によりK_R≃Perf(Γ_R)となることを示す。C=A₀⋊μ₂のsingularity圏の生成対象を、perfectを保つj_sg^*=(-)e_+でRへ移すと、符号+の三つの剰余体shiftがκ_R,κ_R(1),κ_R(2)へ、符号−は零へ移る。j_sg^*j_sg=Idなので生成性が従う。球面制限の像はMFの係数にv=0を代入して表せる。これは対象・射・自然変換を有限行列で具体化する入口であり、可換比較核の全行列を列挙した結果ではない。

最小模型からのstable Homの再開データも保持する。上のH(E,d)の非零二次数(i,w)と周期変数tについて、κ_R(a)からκ_R(b)へのHomは w+3p=a−b、cohomological degree=i+2p を満たす項から得る。a,b=0,1,2の全和は次数−1,0,1,2,3で(11,70,108,50,1)、総次元240、Euler行列は[[-27,27,0],[0,−27,27],[27,0,−27]]となる。この表はH*End(G_R)のベクトル空間を記述し、Yoneda積・高次積やHHの計算ではない。

`python3 computations/verify_mixed_curved_dual.py` はKoszul微分、曲率homotopy、rank128 MF、有限摂動とrank80 MF、両向き写像・homotopyを厳密に再現する（12 PASS）。`--export <出力先.json>` で全係数を再生成できる。大きなJSONは現行一式に追跡せず、必要な時にコードから作る。PBW双対の一次資料はPositselski, *Nonhomogeneous quadratic duality and curvature*, [arXiv:1411.1982v2](https://arxiv.org/abs/1411.1982), §§2.1–2.5,3.3、higher homotopyとShamash構成はEisenbud–Peeva, *Minimal Free Resolutions over Complete Intersections*, LNM2152 (2016), Definition3.4.1, Proposition3.4.2, Construction4.3.1, Proposition4.3.2を参照する。外部PDF自体は収録しない。

### 固定affine MFの比較と次数を忘れる障害

`cmo:lem:isolated-azumaya-mf-completion` は、有限中心・有限大域次元のambient T、正則中心曲率w、唯一の圏的特異点がAzumaya Morse点という仮定の下で、有限射影Z/2-MFの完備化関手が冪等完備後の実Morita同値を与えることを証明する。中心の特異点が唯一であるという仮定ではない。MFのHom cohomologyの有限長性で完備化の完全忠実性を示し、大域simpleの高次syzygyを実際のMFへ持ち上げて、完備化先の剰余体stabilizationを像に入れる。可換局所圏のsplit-generationとClifford模型はDyckerhoff, [arXiv:0904.4713v5](https://arxiv.org/abs/0904.4713v5), Theorems4.1,5.2・§5.5による。非可換orderへの完備化定理の無条件な拡張を引用していない。

`cmo:prop:pointwise-affine-mf-comparison` で、指定された二つのα⁽ⁱ⁾の各一因子(D_α,Ω−s)と(C[x,y,z],λf_α−s)は全固定sで比較される。8個のMorse値ではCl₃、その他は零となり、14中心節点の切断は有限大域次元なので追加のMF成分を生まない。混合族も全固定cで可換候補のaffine MFと同値で、P64根ではCl₆、その他は零。いずれもZ/2圏としての比較であり、通常Z次数のproperな射影Kuとの同一視ではない。

全smooth cでこのaffine圏は零だが射影KuのHH₀は二次元である。特にc=−44828では既存の残余点対象KにExt⁰=C, Ext¹=C¹⁰がある。このためaffine MFを介する関手だけではKu比較を実現できず、内部shift・錐の原点・三次周期、または射影境界との貼合せが必要となる。さらに全空間(D_α[s],Ω−s)の商は有限大域次元のD_αなので全空間の通常MFは零であるが、Morse特殊ファイバーは非零である。各固定値の同値を通常MF族の底変更として無条件に貼り合わせることもできない。

`python3 computations/verify_mixed_comparison_invariants.py`（9 PASS）はJacobian次数二・三、residue符号、同変HHの算術、有理Euler行列をQQ上で再現する。相対圏・核・生成性の証明とは区別する。

### ambient比較と形式的な混合三角性の限界

ambient D_αを通常のdg Morita同値でC[x,y,z]に置き換える経路は使えない。HH⁰は中心環を保つ一方、指定D_αの中心は14通常二重点を持ち、三変数多項式環の中心は正則だからである。これはcurved/MF圏や射影残余圏の比較を排除しない。使用する既知入力はKeller, *Derived invariance of higher structures on the Hochschild complex*, §3.2（2018年5月16日改訂の[著者稿](https://webusers.imj-prg.fr/~bernhard.keller/publ/dih.pdf)）。

形式的混合三角性 `prop:nfm-residual-mixed-triangular` をFermat入力g=(x³+y³+z³)/3、b=0へ直接適用すると、Ŵ_h=J_g+B_h(g)ℓ+γ_h(g)d、J_g=(x³+y³+z³+h²xyz)/3、ℓ=−u²Σα_jx_jとなる。積一の三乗根対角変換への共変性でB_hは対角、巡回対称性でB_h=β_h idとなる。この形式単元β_h,γ_hのh=1での正則性・収束と、この形式経路から得る核の特殊化は未証明であり、一般係数の有理式に現れる未検証の分母を特殊化しない。固定h=1の全中心係数族は、形式h級数への代入を用いず、普遍係数上の実球面制限から比較できる。

固定係数のW=γ⁻¹(J−βu²Σα_jx_j)+cu³にactive変数の√β倍を施すと、候補とのscalar条件β³/γ²=28/27を得る。この必要な規格化は、中心族の実核を先に構成してから特異係数集合の二次モーメントで尺度を決める方法で実現した。split点の抽象Artin変形と重みwt(α)=2,wt(c)=3だけではα⁴/c²型の補正を排除できない、という障害は引き続き有効である。今回は全普遍多項式環上のproper線束模型と境界の自由mapping群を用い、低arity係数が大域正則な多項式であることを先に証明したため、この分母の問題を避けられる。

### 通常の完備底で生成性を失う障害

properなdg代数のsmoothnessを特殊ファイバーと全Artin切断だけから導く推論には、次の具体的反例がある。R=k[[t]]、P=[R→^t R]（次数−1,0）、Γ=End_R^•(P)と置く。Γは底上有限自由な有界strict dg代数である。R_n=R/(t^n)ではCone(t^n)=R_n⊕R_n[1]がP_n=Cone(t)から有限回のconeで作れるので、P_nはPerf(R_n)の生成対象である。したがってPerf(Γ_n)≃Perf(R_n)はP_nとその双対による、nについて互換なMorita同値となる。

ところがΓは通常の完備底R上smoothでない。もしsmoothならR-perfectなΓ加群N=RHom_R(P,R)はΓ-perfectとなる。評価N⊗^L_ΓP→Rのcone CはR-perfectで、RHom_R(P,C)=0。P≃R/(t)なので導来NakayamaからC=0となり、R∈thick(P)を得るが、tを反転すればP[1/t]=0かつR[1/t]≠0なので矛盾する。P_n自身はPへ代数化されるが、生成性が保たれない。tはP_n上null-homotopicであり、ℓ個のextension因子で作る対象はt^ℓで消えるため、R_nの生成に必要な因子数は少なくともn。段数の一様上界が失われることが本質である。

この反例ではH⁰(Γ)=H¹(Γ)=kで、cohomologyはRflatではない。したがってcohomologyの平坦性まで持つ命題の反例ではなく、混合族の非smooth性も意味しない。元c族の相対対角証明は通常のcoherent加群とproperな中央台を使い、h族では通常coherent射影積のExt有限性とcompact持上げを使って、この障害を回避する。

### 有限台加群の線束perfect性と64点の残余射影

`cmo:lem:finite-support-perfect` は、有限中心模型でM[u]の中心像がC[u]上有限になることから、有限次元chart加群のcoherent延長𝒫(M)の中央台がu≠0内で閉じた有限集合であることを示す。従って𝒫(M)が線束perfectであることとpd_D M<∞は同値。任意のj_*がperfect性を保存するとは主張しない。左右のcharacter規約はy,z交換と反対代数で合わせる。これによりκの非零条件がそのまま定常点の線束perfect判定となり、全64点、および下記の100個の低次元simpleの延長はperfectである。

`cmo:prop:projected-point-ext` は、二ブロックの𝒫の例外射影を F=[O²⁰→O(1)¹⁵⊕O→O(2)⁶→O(3)]（次数−3..0）で構成する。全4例外とのRHomを斉次Shamashの内部次数成分で照合し、properな線束圏上のSerre(−4)[5]を使う。残余射影Kの自己Extは次数0が1、次数1が10、他0、Euler値−9。𝒫自体のExt(0,2,3,5)と混同しない。数値類は [K]=[𝒫]+19[O]−15[O(1)]+6[O(2)]−[O(3)]。Yoneda積の同定は使わない。

有限中心性を持たない別の表示では、graded Shamashの周期syzygyと線束への一様Ext消滅からperfect性へ進む代案が残る。その場合は両向きの一様消滅とtwist付きYoneda類の分裂を別に証明する必要があり、本稿の上記判定には用いない。

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

## 0. 満支持複数ブロック型：全慣性・相対積比較・核の降下障害

**設定。** `N=n+2=3k+m`。満支持`m=0,k≥2`では`B=⊗S_i`, `A=B/(Σa_iΩ_i)`、全`a_i≠0`。`p_i,2p_i,3p_i≠0`、相異なる`j_i≠0,1728`を基本とする。全O認識にはさらに`jp_i≠0 (1≤j≤3k−3)`を課す。無限位数は要求しない。全O群は自然同型類の群であり、根の分類は三乗同型やcoherenceを標識しない。

| 内容 | 状態・仮定・証明所在 |
| --- | --- |
| 表示stack・相対双対 | 表示DM stackは次元2k、慣性`K_k=(H_27^k)/Δμ_3`。Serreは基底直線`det(⊕W_i)⊗ℓ^∨`を保持。`mbs:thm:presentation-stack`, `mbsd:thm:serre` |
| 全O同値の第三Veronese認識 | `Eq_O=Isom_gr(C,C')/G_m`, `C=A^(3)`。二ブロック55生成元・2619二次関係。`mbv:thm:all-o-third` |
| 中心商と余法加群 | `D=(⊗T_i)^(3)`の純商・余法加群から`(E_i,L_i,σ_i)`を回復。幾何点の可換tensor表示が認識される。`mbiq:thm:triple-recovery`, `mbiq:cor:commuting-o-rigidity` |
| 中心商の全自己同型 | 飽和冪が全多重次数を認識し、`Aut_gr(D)=(∏Aut_gr(T_i))/Δμ_3`。各元が`E=⊗T_i`へ持ち上がる。`mbca:lem:saturated-powers`, `mbca:thm:center-automorphisms` |
| 中心方向の剛性 | 負次数Hom・Ext¹消滅、多中心thickeningへの唯一lift、次数別安定によるgraded同型。中心還元核は全kで自明。`mbcr:prop:negative-ext`, `mbcr:lem:graded-lifting`, `mbcr:thm:reduction-rigidity` |
| 全自己同値群 | 基本開で`Aut_gr(C)/G_m=K_k`。全O認識条件の下で`Aut_O=K_k`、位数`3^(3k−1)`。二ブロックは正確に243。`mbca:thm:full-inertia` |
| 根の分類 | `rO≃O(1)`なら唯一に`r=sΦ_h`、自動的に`r³≃s³`。共役類数`(11^k+2·8^k)/3`。Oの像を指定しない全根は未解決。`mbca:cor:marked-roots` |
| 一般相対認識 | `P_k°→M_k°`はさらに非空開で有限étale・階数一。任意非被約底の全同値層もgraded Isom/G_mに等しい。`mbrr:thm:finite-etale`, `mbrr:cor:stack-isomorphism` |
| 内在的中心慣性 | 順序付きブロック被覆上`Z(K_k)=(μ_3^k)/Δμ_3`、階数`3^(k−1)`。順序を忘れる降下は因子置換。`mbrr:cor:central-band` |
| 表示gerbe | 各非空開でorder3、順序付き被覆のweight1束の最小正階数3。各体値点のpullbackは零になり得る。`mbsd2:thm:gerbe-period` |
| compact残余とprojector | weight0として全O開へ降下。例外成分は `Perf(P_k,−jβ)`。rotationの自己同値性・Serreは有限mutationで証明。`mbsd2:thm:projector-descent`, `mbsd2:prop:rotation-serre` |
| 関係直線と周期 | MFでは `[2]=(3)⊗ℓ^∨`。残余にはwindow比較の範囲で `ρ³⊗ℓ^∨≃[2]`。scalar-simple核の実現gerbe=βは追加条件付き。`mbsd2:prop:line-period`, `mbsd2:cor:rotation-obstruction` |
| 中心作用・有限指標 | 作用と同変化はcoherenceごと基準非依存。split torsorは `Σa_i=1`、置換固定点は `3∤k` と同値。`mbza:thm:central-action`, `mbza:prop:shift-character`, `mbza:cor:permutation-obstruction` |
| 全kの可換積表示 | `Ku(V(Σf_i))^(Z_0)≃Db(∏V(f_i))`。通常Kuは積圏の双対同変化で、characterは因子rotation比に対応。`3∤k` なら対称rotationは `(∏R_i)^c[−2m]`（`ck−3m=1`）。BFK・Orlov・Elaginの既知定理の適用。`mbrd:thm:split-product`, `mbrd:prop:factor-rotations`, `mbrd:cor:symmetric-rotation`, `mbrd:cor:dual-action` |
| 核stackと実核 | 両側smooth proper族・作用を固定すればfpqc降下。一般点の実dg模型が有限拡大上にあり幾何学的一般点で非空なら、縮小後有限étale被覆上の核。大域sectionは別。`mbrd:prop:kernel-stack` |
| 点三次と同変復元 | 明示的Jacobian tensor/PBW族、既存cft/gdrの下で `J_i=g_i+ε_i² det Hess(g_i)/24` の分離和を復元。全kで有限拡大後 `(K_A^coh)^(Z_0)≃Db(∏E_i)`。`mpc:thm:point-model`, `mbrd:cor:nc-product` |
| 中心rigidificationと点族 | `P_k//Z_0≃B_k`、`B_k→E_k`はsmooth representable surjective・相対次元k。点曲線積のsmooth projective族は全O開にある。`mbfm:prop:rigidification`, `mbfm:prop:point-map`, `mbfm:prop:product-family` |
| 中心線と点三次線の自然な同期 | 最大可換商による比較を相対Hesse被覆で全基本楕円開へ一意延長。全graded同型・任意底変更に自然。`Φ_pt`と表示gerbe・関係直線の同期を同時に得る。2p=0の一般境界では延長係数が零。`mbpl:thm:global-line-comparison`, `mbpl:thm:commutative-family` |
| 可換分離和の相対核 | smooth準射影C基底・共通L・smooth各三次。実dg外積と相対Orlovにより実perfect核。構成済み核の引戻しは準コンパクト・分離的noetherian底（非平坦・非被約も許す）のPerf比較を保ち、置換coherent。`mbrp:thm:relative-product`, `mbrp:cor:base-change`, `mbrp:prop:permutations` |
| 体上の直接非可換積 | 全基本領域の実表示で `Ku_line(A)^Z0≃Perf(∏E_i)`。全kのtensor-noetherian性・有限Koszul–Shamash・Γ-Hom・windowを本文証明。smooth proper性とcrsから `Ku_line=Ku_coh`。`mbnp:thm:product`, `mbnp:cor:coherent` |
| 実表示上の相対非可換積 | smooth準射影C基底で `Ku_compact(A/S)^Z0≃Perf(∏E_i/S)`。相対noetherian性・有限MF Hom・実Morita核を構成。任意のqc separated noetherian底変更はcompact/perfect比較。`mbrn:lem:noetherian`, `mbrn:thm:relative-product`, `mbrn:cor:base-change` |
| 固定点の通常Ku比較 | 順序付き実表示で中心作用を保つ比較は高々 `3^(2k−1)` 次、rotation・指定周期も保つ比較は高々 `3^(2k)` 次の拡大上に存在。代数閉体では全基本点・拡大不要。全上界の最小性は主張しない。`mbpd:cor:field-degree`, `mbrc:thm:finite-point-comparison` |
| 固定局所型の一般降下判定 | 局所rotation比較・scalar-simple・負Ext消滅・底変更の下で `L_P³≃ℓ_tℓ_s^−1`。marked核stackはG_m-gerbeとμ₃-torsorの積で、存在iffα=γ=0。`mbks:prop:comparison-line`, `mbks:thm:kernel-criterion` |
| Picard補正型の相対分類 | `α_Pic=Σδ_Ei(p_i)`、因子period torsor `T_i`、`D=(∏T_i)/Δμ3`。中心作用を保つ核stackは `G_Pic×D`、rotation・period付きは `G_Pic×∏T_i`。全比較型の分類ではない。`mbpd:prop:product-gerbe`, `mbpd:thm:coherent-corrections` |
| 自然な周期の全係数 | Hodge比較線λに `q(ω³)=−1/v_ω(p)`、`γ=[v_ω(p)]`。Jacobianの `v_ω(p)ω³` は内在的。全九flexの中心正則化と原点校正を用いる。`mbhp:thm:period-formula`, `mbhp:cor:global-kummer` |
| 全中心同変核の位相と最小次数 | k≥3は同種・CMを許し、k2は幾何学的非同種ならα=Σδ_iとγ_i+ν_iで判定。H-normalizerの像はk≥3で因子置換のみ。固定Hesse独立族の最小 `3^(k−1)`／`3^k` は中心bandの抽象自己同型を許しても不変。`mbfc:thm:full-criterion`, `mbfc:prop:normalizer`, `mbfc:cor:normalizer-bound` |
| 有限étale被覆の実構成 | 三分点の標準被覆rank `9^k` と位相商／全位相を合わせrank `3^(3k−1)`／`3^(3k)`。非空開の横断次数三切片ならrank `3^(2k−1)`／`3^(2k)`。`mbpd:prop:finite-covers` |


**点の支持と余法加群。** `F=⊗T_i^(3)⊂D`に対しDは左右有限加群。点加群の十分なtailをFへ制限すると、複数active因子は`σ_i³`の固定点を要求して不可能。混合次数一作用が残れば、その三乗はinactive因子を持つFの元として零になる一方、点列では非零となり矛盾する。純成分核I_iは次数一で生成される。I_i²は次数二以上で「外部次数≥2」の部分なので、余法加群は外部次数一、すなわち`(T_i)_(3n−1)`のコピーを残す。次数一だけの有限長例外はtailsで消える。skyscraperの支持からσ、構造層の像からLを回復する。全文は`mbiq`節。

**モジュライの一般開。** `End(C_1)/kI→Hom(R_2,C_2)`の核が全射影自己同型のLie代数。滑らかな可換三次ではEuler以外の次数零導分がなく、Hesse関係`(1+hα)yz+(−1+hα)zy+hβx²`の支配的変形で一般の核も零となる。中心のprimitive剰余はPoisson Casimirとして滑らかなHesse三次の定数倍。関係Grassmann像ZへChevalleyとgeneric flatnessを適用し、一つのfppf被覆から全次数の自由性を降ろす。GLのframe束にPGLが直接作用するとはしない。対象はこの局所表示と全O同値のstack化であり、大域graded代数は不要。幾何fiberは9k次元なので商の次元2kを得る。相対Isomの有限性・平坦性を有限幾何fiberだけから結論していない。

**飽和冪と多重次数。** 純商核`I_i`に対し、`(I_i^m)_n`は`n≥m`で外部次数`Σ_(j≠i)a_j≥m`の全成分に等しい。飽和は下の次数制約だけを除く。外部次数の不足は、純i成分による任意に大きい右積でも消えない。従って`|a|=3n`の成分は`D_n∩⋂_i (I_i^(3n−a_i))^sat`として内在的に回復される。純部分代数の作用を除いた自己同型は、`Λ={e∈(Z/3)^k:Σe=0}`ごとの加群にスカラーとして作用する。各剰余加群のEnd=Kと非零な純tensor積により、このスカラーはΛのcharacterであり、ブロックμ3スカラーで実現する。全文は`mbca`節。

**中心の持上げと全群。** `R=Sym Z(C)_1`、`M_j=(A(j))^(3)`はR上自由。`E=⊗T_i`は中心完全交叉で、有限次元加群の双対は`RHom_E(F,E)=F^∨[-2k]`。局所化三角とVeronese同値を使い`Hom_GrD(M̄_j,M̄_j(-n))=Ext¹_GrD(M̄_j,M̄_j(-n))=0`を得る。Veroneseが一般にExtを保つとは仮定せず、Rωの同定とconeの下界から次数0,1を比較する。中心n次層は`M̄_j(-n)⊗Sym^n Z_1`なので、R-flatnessを使うderived base changeとHom完全列で同型が唯一に持ち上がる。各固定次数は有限段階で安定するため、完備化だけで止まらず実際のgraded同型となる。AutDの全factor liftを接続してO(1),O(2)を認識し、SSSから全G=Kを得る。一次変形類κ_Cの非消滅はこの証明の入力に不要。逆に二ブロックでは`κ_C≠0`が従う（`mbcr:cor:nonzero-class`）。一次で自明なら補空間Uのliftを変えて全二次関係を`[g,U]`と`r−c_rg²`にでき、gの符号反転が射影的にも非自明な還元核を与えて矛盾する。具体的なHH² cocycleの値は計算していない。

**相対化の独立な段階。** 幾何点の群の一致だけでは非被約底のIsom一致は従わない。射影枠`P=Fr(A_3)/G_m`を用い、表示射のbase changeを代数空間`Q=[P/G_k]→Z°`とする。任意底上の飽和と隣接Homは表示射の忠実性を与える。Qはfppf・準有限、Pは標数零体上滑らかなのでQの一般fiberは有限étale。有限表示降下で非空開へ広げ、その後`[G_A:K_k]=1`を使う。全点の一致から直ちにstack同型を主張しない。縮小前の全パラメータや抽象圏の全変形への拡張は未解決。

**共通scalarの重みと三次障害。** 右加群の移送を `Φ_h(M)=M^(h^−1)`、shiftを `M(j)_n=M_(n+j)` とする。scalarの自然自明化は `τ_(λ,M)(m_n)=λ^n m_n` で、`τ_(λ,M(j))=λ^(−j)τ_(λ,M)(j)`。この比較の下で `O(j)` とshift(j)の標準同変構造は重みjとなる。表示gerbeにweight3線束ℓがあるので `3β=0`。実表示慣性 `(G_m×H_27^k)/Δμ3` のcommutatorには共通scalarのμ3が含まれるため、任意のline characterのscalar weightは3の倍数である。従ってstackの各非空開でβ≠0。これは代数閉体値点での実表示の不存在を意味せず、coarse generic fieldのindex計算とも異なる。

**残余構造が降下する理由。** `RHom(O(j),−)⊗O(j)` は重み−jとjが相殺し、evaluation・dg cofiber・mutation合成もweight0となる。`r=3k−3`、残余への左射影Pについて `ρ^r=P(1)^r|K`、逆Serreについて `S_K^−1=P S_D^−1|K`。従ってρは全compact表示族で自己同値となる。MFのline-valued定義から `[2]=(3)⊗ℓ^∨` であり、内部shiftをρへ移すwindow比較があれば `ρ³⊗ℓ^∨≃[2]`。その範囲では `S_K=[k]⊗(det V⊗ℓ^(−k))`、後ろの線束はweight0。係数線束でrotationを補正できる最小正冪は3。実際のrotation核の非降下は、実現stackのfpqc降下・負自己Ext消滅・End=O・底変更を仮定して、そのgerbeをβと同定する。標準同変構造のweightだけから無条件に全核の実現を否定しない。

**有限中心作用の基準変更。** `Z̃=μ3^k→Z_0` の全splitは `Spl_k={a∈F3^k:Σa_i=1}` で、`s_a([z])_i=z_i/∏z_j^(a_j)`。`s_a'=χ_aa' s_a`、`χ_aa'=∏z_i^(a_i−a_i')` とすると、τから作用のcoherent比較εと同変圏の比較Jを得る。積・三重cocycleはscalarの積の恒等式そのもの。shift/rotationでは `Jρ_a≃Tw_(χ^−1)ρ_a'J` が残るが、三乗ではχ³=1で消える。置換固定点は全a_i=k^−1で `3∤k` の場合に一意。`3|k` では `δ(1)∈H¹(𝔖_k,Ẑ_0)` が非零・order3で、ordered coverの既約性から各非空開にも切断がない。この有限split選択被覆上でも共通G_m-gerbeは残るため、rotationの線型化は実表示gerbeへ引き戻して述べる。

**Thom–Sebastianiの適用とdual action。** `Γ_k={λ_i³が共通}`、共通character χは非torsion、作用群はreductive。可換各f_iのcritical locusは原点なのでBFK Cor5.18のsupport条件を外せる。Orlovで `MF_gr(f_i)=Db(E_i)`、`MF_gr(Σf_i)=Ku(X)`、Γのsplitで `MF_Γ(Σf_i)=Ku(X)^(Z_0)`。module weight=degreeの規約では `Tw(e_i^−1)` が内部(1)、`Tw(e_i/e_b)` が積上の `R_i^−1 R_b` に対応する。群法則はcharacter作用のcoherenceを移送する。非可換の場合は下の直接外積から同じΓ構造を得るが、因子rotationは `R_i,p=T_O(t_pi)_*(−⊗L_i)` となる。Elaginの二重同変化により通常Kuはこのdual equivariantizationである。K⊃CではFourier冪等元が全て定義され、代数閉仮定なしに同じ構成が働く。

**比較核の降下と同期の障害。** 両側とG作用が降下済みなら、同変perfect双加群は局所的に `(C^op⊗D)⋊G` の加群として表され、群coherenceを含む∞stackが降下する。全比較核を一つのgerbeとは呼ばない。simpleな局所同型型を固定して初めてG_m-gerbeとなり、そのsectionは別の中立化問題である。実dg一般模型が有限拡大上に存在することも仮定すれば、一般点の核は縮小後の有限étale被覆へ広げられる。二つの表示gerbe上の `η:Pρ_s→ρ_tP` は重み `(−1,1)`、三乗周期の比較には `ℓ_s→ℓ_t` が伴う。比のband `β_t−β_s` の同期と、P自身のscalar障害の消滅は区別する。

**因子stackのrigidification。** `T=(G_m^k)/G_m`は全supportの中心係数torusへ三乗で作用し、fppf推移的で核は `T[3]=Z_0`。従って係数を忘れるP→BはZ₀-gerbeであり、中立性を主張せずにrigidificationを明示できる。順序を忘れたbandは因子置換を含む。B→Eの幾何fiberは `∏(Jac(E_i)∖(E_i[2]∪E_i[3]))`。点曲線積の射影性は各因子の `O(3)⊗det(W_i)^−1` の外積（次数九、weight0）で確認する。中心作用付き圏のgerbe上のsection圏を使えば、その同変化はBへ降りるが、本表示族の捩れのない積圏との同値はmbic節でτ_z=θ_zを確認して得る。一般のgerbeについて自動とはしない。詳細はmbfm・mbic節。

**最大可換商による尺度の決定。** `Q=S_ab`は交換子の線型包ではなく両側イデアルで割った最大可換商。`R₂⊗W→Sym³W→Q₃` の左はrank9以下なのでQ₃は少なくとも一次元である。rank1 locusとC,Jの像の非零locus上で `θ=(J→Q₃)^−1(C→Q₃)` を定める。Fermat族 `[y,z]=t x²` と巡回式では、`C=x³+y³+z³`, `U=xyz+yzx+zxy`, `Ω=(3+t³)C−2t²U`, `F=C+t²xyz` に対し `Ω→−6t²xyz`, `F→t²xyz`、従って `θ(Ω)=−6F`。Q₃内の比を用いるため、中心元と点方程式の任意のframeを無断で同一視しない。一般のframeでは `F_pt=Σa_i u_iJ_i`、`u_i=[Ω_i]/[J_i]` である。Fermat族の形式群でtorsionを排除し、独立parameterの非定数jから全kの非空性を得る。全O認識開との交わりは既約性で得るので、特定の一変数traitが任意に指定した認識開に入るとはしない。詳細はmbpl節。

**相対外積の要点。** `f_i∈Sym³W_i⊗L`、関係直線 `ℓ=L^∨` として周期は `[2]=(3)⊗L`。有限MFのodd⊗odd項には共通Lが一つ必要である。Γ指標群 `Z^k/〈3e_i−3e_j〉` によるHom分解を複体段階で比較し、smooth基底の正則環の有限大域次元を使って導来tensorを計算する。零切断のKoszul stabilizationと全character shift・Perf(S)が生成する。relative Orlov、外積、scheme上のToën核対応を合成した核を固定し、逆核・projectorの恒等式を導来引戻しすることで非平坦底変更を得る。quotient stack上のprojectorはdiagonal-Z₀ kernelのZ₀×Z₀へのinductionとして扱い、全Rep(Z₀)成分を保持する。特異底でのabsolute coherent MF比較は主張しない。積側の相対標準直線 `det(⊕W_i)⊗L^k` は既存残余Serreの `detV⊗ℓ^−k` と一致する。有限生成C体へのspreadと一般点への引戻しにより、可換積比較には追加体拡大が不要となる。従ってmed/mpcの有限比較体をそのまま使える（mbrp:cor:comparison-field）。詳細はmbrp節。

**同期を固定した周期障害。** 局所的なrotation比較の直線束 `L_P=H⁰RHom(Pρ_s,ρ_tP)` には三重合成 `q_P:L_P³≃ℓ_tℓ_s^−1` がある。同期θに対する `q_P(η³)=θ` がμ₃-torsorであり、Pic(S)[3]成分は[L_P]、直線自明化後は単数の三乗障害となる。核のscalarはηの両側で相殺するので、核の実現gerbeG_Pとphase torsorTは独立に降下し、marked stackは `G_P×T`。このためAut(P,η)=G_mは残る。gerbe同期をNで変えると `L_P→L_P⊗N`、`ℓ_t→ℓ_t⊗N³` となり、自由な同期変更で吸収できる場合とmbplの自然な同期を固定した問題を区別する。非自明なPic[3]直線とC(t)上の `η³=t` は一般論の反例として保持する。自然なSklyanin族における実際の非零位相は、下記の二捩れ境界で証明した。全データのcoherent置換作用が既にあれば、連結ordered cover上のTの切断はHom(S_k,μ₃)=0により降りる。他方、S₂の弱作用のscalar cocycle tはG_m核gerbeの非降下例を与え、このphase消滅を核へ拡大できない。詳細はmbks節。

**全基本楕円開での中心線比較。** Hesse関係 `ayz+bzy+cx²` と巡回式、点式 `F=abc C−(a³+b³+c³)xyz`、既知中心式 `Ω_H=c(a³−b³)C+a(b³−c³)U+b(c³−a³)V` を用いる。H₂₇不変三次tensorは〈C,U,V〉、三次関係の不変部分は〈cC+aU+bV〉なので、Ω_Hが零ならa³=b³=c³となり点三次が特異になる。分母なし恒等式 `ab(Ω_H)−3(a−b)F=(a−b)³Σx_i r_i^ab` により `θ(Ω_H)=3(a−b)F` が既存比較を延長する。flex原点・level3・三乗が1のtheta持上げを選ぶ有限étale被覆と、W・Rの二固有直線のframe torsorで滑らかなHesse被覆を構成した。普遍被約重なりの稠密開で一致を示して降下し、その後に任意非被約底へ引き戻す。これで最大可換商Q₃のrank退化を越えられる。2p=0のHesse境界ではΩ_HとFは非零のままa−b=0となるので、同じ比較を線同型として延長できない。証明は `mbpl:lem:hesse-cover`, `mbpl:lem:hesse-center`, `mbpl:thm:global-line-comparison`, `mbpl:rem:two-torsion-boundary`。

**直接非可換外積の環論と生成。** `T_i=S_i/(Ω_i)=B(E_i,L_i,t_pi)`。Keelerの二因子tensor定理はそのまま反復できないため、X=∏E_i上の多重THCRで証明する。多重斉次ideal Jの評価ideal I_nは大域生成性から単調で、Noetherian X上で安定する。translationのNS作用は恒等、各方向が正なら外積線束はampleなのでNC-amplenessを適用できる。評価核のH¹消滅で十分深い多重次数を有限生成し、有限幅の端はk−1因子の有限加群で帰納する。反対環にも適用し、中心正則列Ω_iの正次数filtrationから⊗S_iの両側noetherian性を戻す。任意Kは代数閉包上の証明から忠実平坦降下する。詳細は `mbnp:lem:noetherian`。

**有限模型とcoherent飽和の論理順序。** 各ambientの有限Koszul解消にcentral w_i=a_iΩ_iのhigher homotopiesを入れ、有限曲率付きfoldを作る。h₁²=0とは仮定しない。外積の異なる因子のodd演算は反可換し、総曲率はΣw_i。Shamash系は総augmentation stabilizationを与える。Γ指標ごとのHom分解で実dg外積の完全忠実性を示し、windowの三つのaugmentation shiftと全中心characterから残余部分を生成する。product圏はsmooth proper、有限群の双対同変化でKu_lineもsmooth proper、次いで既存crsの全coherent飽和定理を適用する。この順で全coherent生成を外積の入力にしない。体上の証明はmbnp節、相対noetherian性と有限MF Homの底変更を加えた証明はmbrn節に置く。

**相対非可換積の入力と到達範囲。** smooth準射影C基底の順序付き実表示では、共通関係直線ℓを保持した有限Koszul–Shamash模型から `Ku_compact(A/S)^Z0≃Perf(∏E_i/S)` を構成した。環論は任意noetherian係数環を許し、相対外積線束を固定ampleの大冪と相対nef線束に分け、訂正を含むKeelerの相対Fujita消滅を使う。評価idealの安定・深い多重次数・有限幅の端の帰納を相対化し、全kのtensor-noetherian性を得る。regular基底上のparameter-zero／positive-parameter window、有限MF Homのperfect模型、augmentation生成により実Morita核を構成する。任意のqc separated noetherian底への導来引戻しは作用・rotation・`[2]=(3)⊗ℓ^∨`・単位余単位を保持するが、非正則底で全coherent＝compactとはしない。`mbrn:lem:noetherian`, `mbrn:lem:window`, `mbrn:lem:finite-models`, `mbrn:thm:relative-product`, `mbrn:cor:base-change`。

**Picard補正型のscalar gerbe。** `G_i=Pic^{p_i}(E_i/S)` の外積はbandの積写像 `G_m^k→G_m` を持ち、その核でrigidifyすると、積曲線上の対角線束核 `F=−⊗M` のgerbe `G_Pic` となる。従って `α_Pic=Σδ_Ei(p_i)`。これは各δ_iを別々に消すことより弱い条件であり、因子線束が個別には存在しなくても和の相殺は許される。三倍点の実線束から `3α_Pic=0` を得る。分類対象はidentity graphのPicard補正型であり、全ての残余比較核がこの型になるとはしていない。`mbpd:prop:product-gerbe`。

**因子位相と対角商。** 各 `η_i:F_iR_i,p→R_i,0F_i` の指定周期torsorをT_i、類をγ_iとする。核scalarはHomの両側で相殺するためT_iは因子gerbeから基底へ降りる。双対作用 `Q_i=R_i^−1R_b` の比較射はη_i^−1η_bに依存し、全coherent構造の差は `Hom(Ẑ_0,G_m)=Z_0`。従って `D=(∏T_i)/Δμ3`、`[D]_b=(γ_b−γ_i)` であり、中心作用を保持したPicard型核stackは `G_Pic×D`。d∈D(S)を選んだ型のscalar類はΣδ_i、rotation・指定周期に残る類はγ_bで、全部を標識したstackは `G_Pic×∏T_i` となる。共通非零phaseはDでは消えるがrotationのperiodには残る。核Autは依然G_m。中心作用の標識を忘れた全核への忠実な分類は別問題である。`mbpd:thm:coherent-corrections`, `mbpd:cor:descent-criterion`。

**Hodge比較線と周期の全係数。** 一因子のrotation核の比を対角へ制限すると、graphとMの因子が相殺し、比較線はHodge線λとなる。自然な同期で `q(ω³)=−1/v_ω(p)`、`v_ω=2y+a₁x+a₃`、`ω=dx/v_ω` である。内在的な `𝔳(p)=v_ω(p)ω³` により `T=Cube(𝔳(p))`。基本j開では `h=c6/c4`、`u=h³/𝔳²`、`e=−h²/𝔳` なので、既存の単元表示も `[u]=[v_ω(p)]` に一致する。因子 `div(v)=Σ_{0≠t∈E[2]}[t]−3[o]` は固定滑らかな楕円曲線上のもの。特異曲線境界や一ブロック残余位相をこの式で解決したとはしない。証明は `mbhp:thm:period-formula`、`mbhp:cor:unit-and-residue`。

**中心の正則化と定数の校正。** 固定Hesse曲線 `E_μ` の全点pを動かす。`Ω_H/(abc)` はS₃の中で正則化され、中心直線C=O(−3o)となる。a≠0とb≠0の二chartは全九flexを覆い、p∈E[3]では線型liftによる多項式環のZhang twistを用いる。次数三の中心全体が一意とは主張せず、THCRへの核直線を保持する。比較線は原点を含めてV=λ⊗O(o)、同期前のcubeはV³≃J⊗C^∨。θの零点が非零二捩れ三点なのでqの因子が決まる。原点のsourceは−3F、自然targetは6F、従ってq_V(id³)=−1/2。conormal規約 `pr₂f−pr₁f↦df` でλ→Vの一次項は−t、vの主部は−2t⁻³だから `qv=−1`。滑らかな被約の普遍表示上で射を一致させてから任意底へ引き戻す。証明全文はmbhp節。

**Hesseでの有理式。** `a³+b³+c³−3μabc=0`、`ω_H=dc/(3b²−3μc)`（a=1 chart）なら `v_ωH(p)=9(1−μ³)(a−b)/(a+b+μc)`、`q(ω_H³)=(a+b+μc)/(9(μ³−1)(a−b))`。接線a+b+μc=0は3o、a=bは非零二捩れ三点である。この式は正規化されたqの全係数を与え、三乗類だけを計算したものではない。

**実積核と比較stackの内在化。** THCR切断の次数nのscalar λⁿは既存τ_λと一致する。Γ次数αでは `τ_z=∏ζ_i^{α_i}` が同変対象のθ_zと一致し、核・逆・単位余単位がPとB=P//Z0へ降下する。B上の中心同変残余は非捩れPerf(Y)。偏極Li自体はB上で捩れていても `σ_*Li⊗Li⁻¹` は実線束で3piを表し、3δ_i=0を保持する。sourceとtargetのLi→Li⊗Niを同時に変更するとHom・period・dual作用の比較で全twistが相殺し、Picard型核stackもBから来る。全O認識開は拡大せず、順序なしでは群を置換局所系として扱う。個々のrotationの選択と3|kの障害は残る。証明はmbic節。

**全型と自己同型の追加位相。** Orlov像がblock対角のFM核は、非同種性によらず因子外積となり、外積写像の核は総和零のshift分配のみ。k≥3では全H作用の中央化条件から非対角成分が `(r−I)g_ij=0` を満たし、`(r−I)(r+2I)=−3I` とHomのtorsion-free性により消える。k2非同種も同じ外積分類となる。Q_i=R_i⁻¹R_bの条件で出る因子shiftはR_i³=[2]から零なので、全型は `∏Aut(E_i,L_i)×Λ_k`、`Λ_k=Z^k/{3n:Σn_i=0}`。K上では幾何型の一意性から偏極φ_iが降り、実K自己同値を除いた総核がΔ_*Mとして降りるので、個々のδ_iではなく和αだけがscalar障害となる。位相はγ_i+ν_i(φ_i)、νはg(f)=c_gfの[c_g]。全H構造の差がHom(H,Gm)=Gなのでcoherent構造も尽くす。証明はmbfc節。

**一般のνを零と置けない反例。** K=C(a)、一般μ∈Cに対し `f=x³+a y³+a²z³−3μa xyz`、`g(x,y,z)=(az,x,y)` とする。g³=aI、g(f)=afなのでν=[a]≠0。代数閉包上では通常Hesse曲線となりj≠0,1728を保てる。従ってPicard型の位相が非零であることだけで一般Kの全中心同変核を排除できない。一方、固定Hesse levelの独立族は全自己同型liftが方程式を厳密保存するためν=0であり、別の状況である。

**自然な二捩れ境界の剰余。** Hesse `(a,b,c)=(1+d,1,c)` でcを一般定数とすると、d=0で点曲線は滑らか、pは非零二捩れとなる。`Ω_H=(1−c³)(U−V)` は非零正則のままで、source Ω_Hとauxiliary target F_Hの指定周期は正則trait上に延びる。flexから実線束 `M=O(p−o)` を持つのでδ_E(p)=0。しかし自然targetは `θΩ_H=3dF_H` であり、生成元変更則 `τ_(vF)=v^−1τ_F` により `q_nat=(3d)^−1q_reg`。したがってKummer剰余は+1。C[[d]]では単元が三乗なので正確にγ=[d]となる。これは任意にperiodを変更した例ではなく、自然な関係直線同期に対する障害である。`mbpd:prop:boundary-phase`, `prop:nfm-period-equation-frame-change`。

**境界のtop syzygy線を保持する理由。** a=bでも三段Koszul分解と中心商THCRは有効だが、raw top syzygy `P=(W⊗R_2)∩(R_2⊗W)` からdetWへの交代化は零になり得る。DVRの次数別自由性と有限Koszul複体を使い、Pそのものを保持して一因子window・指定periodを構成する。detWによる基本開の表示をそのまま境界へ延ばしてはならない。これは `mbrn:cor:factor-boundary` の補足であり、全O認識開の拡張を意味しない。

**H-normalizerと同種二因子。** k≥3の指標配置±χ_iは唯一の関係Σχ_i=0を持つので、その線型対称性は±S_kである。Tate加群の忠実性で実際のblock permutationへ戻し、各isometryをFM同値へ持ち上げる。common−は `F_iR_iF_i⁻¹=R_j⁻¹[n]` の三乗から `3n=4` となり不可能。像は偏極因子置換Π、代数閉体ではjを保つ置換に一致する。不同jのk≥3、非同種k2ではNormal=Centとなる。これは指定中心部分群を保つ比較の範囲であり、Kuの全無標識自己同値の主張ではない。

二つの同種因子では任意isogeny uとdualに対し、`B₁=[[-1,-1],[0,1]]`, `B₃=[[-3,-1],[6,3]]` を用いて `N=[[0,uB_s],[u†B_s,0]]` を作る。`D=deg(u)s` が非平方となるs=1または3を選ぶと `N²=DI`, `N^♯=−N` であり、Pell解から `aI+bN` が混合中央化元となる。Orlov liftの可換子のshiftはQ³=1で消え、`1−q` のisogenyと三乗scalar規格化で実coherent核を得る。幾何的中央化群のOrlov核は `Z×E₁[3]×E₂[3]`。次数二isogenyではさらに `[[s,φ∨I],[φI,s]]`, `s=[[1,0],[-3,-1]]` がH反転を実現する。不同jだけでは二因子の反転を排除できない。証明はmbfcの混合中央化群小節。一般Kでの実現gerbe・位相は残る。

**通常Kuにおける中心の無限共役軌道。** 分離和四様体では、各因子のflex接線上の三次式が線型式の三乗となることから、中心生成元gに巡回される三平面P₀,P₁,P₂を得る。任意の平面のI_PはKuに属し、normal bundleのc₁=0,c₂=3とχ=2、Serre=[2]から2-sphericalである。異なる三平面は直線でcleanに交わり、excess line O(−1)により交点数−1。δ_i=[I_Pi]のMukai Gram行列は対角−2・非対角2、det32となる。r₀gr₀δ₀=−2δ₀−δ₁はgδ₀, g⁻¹δ₀のいずれとも異なる。二twistの積の数値行列hは `(h−I)³=0`、s=δ₀+δ₁+δ₂に `h^m s=(1+4m²+2m,1+4m²−2m,1)` と作用し、m≠0でg固定直線を保たない。従って中心の共役軌道は無限。各共役作用の同変化は同じPerf(E₁×E₂)であり、この積表示の性質でも指定部分群を一意化できない。全基本二ブロック非可換幾何点へ既存G同変比較で移る。全文はmbun節。無限個の非共役作用、一般K上の無標識核の存在、最小次数の低下は結論しない。

**独立なk位相と最小次数。** 独立なHesseパラメータd_iに対し `K0=C(d₁,…,d_k)` 上でα=0、位相の付値剰余行列は単位行列となる。従って全γ_iと差γ_b−γ_iのKummer次元はkとk−1である。独立な非定数j_iから因子は幾何学的に非同種。固定Hesse levelの全偏極自己同型はC上の行列で三次式を厳密に保つので、全νが零となる。よって最小次数 `3^(k−1)`／`3^k` は全中心同変核型に対して鋭い。任意の非空開にもその大域核はない。一方、中心標識を忘れた核や一般scalar上界の最小性は結論しない。

**有限被覆と体上の上界。** 全基底上の標準被覆 `P=∏[3]^{-1}(p_i)` はrank9^kであり、三倍写像を表すdeterminant線束から各M_iを構成できる。P×Dはrank `3^(3k−1)`、P×∏T_iはrank `3^(3k)`。既約基底を非空開へ縮め、各平面三次に相対横断直線を選べばrank3の点被覆を使え、同じ二つのrankは `3^(2k−1)` と `3^(2k)` になる。体上では次数1又は3の閉点を順次選び、同じ上界を3の冪の体拡大で実現できる。前者も中心作用は保持し、選んだrotation・period比較を要求しない。実表示やブロック順序を得る拡大は上界に含めない。`mbpd:prop:finite-covers`, `mbpd:cor:field-degree`。

**幾何ファイバーの残余圏。** 代数閉体上では実線束と三乗根を選べる。同じ偏極点曲線組の表示をそれぞれ自然標的へ比較し、block cube rescalingで標的を同型にできるので、unmarked Kuの同値類はB_k→E_kの幾何fiber上で一定。これは圏から曲線組を回復する逆向き、関手の一意性、全O開上の大域比較核を意味しない。`mbrc:cor:point-fiber-constancy`。

**保持する表現と障害。** 二ブロックC_1のK_2作用は射影的に忠実。55次元表現は自明表現3コピー、商の16個の非自明一次指標、二つの9次元既約表現各2コピーで、中心固有空間は19・18・18。ambient PGLのcentralizer次元32、normalizer/centralizer位数186624は関係を保つ群とは限らない。実際の全G=Kは上の別の証明で決定した。一般的な二次中心拡張では`xy−yx=g²`の`g↦−g`が還元上恒等となり、還元核を無条件にunipotentとする議論は失敗する。この例は保持するが、本対象の核自明性を妨げない。

**保持する補助課題。** 全O上のPicard比較stack、自然な周期式、因子分離下の全中心同変核判定、二ブロックの中心非正規性を入力に、以下の算術課題を保持する。主予想の比較核・表示範囲、または本文で述べる全point構造の検証に必要な場合に着手する。

1. **中心作用の共役軌道の降下。** 全通常同値による指定μ3保存は偽である。有限比較体上のG同変核を基準に、中心normalizerから全Aut(Ku)へ移すときの降下cocycleとgerbeを調べる。共役類自体の認識は残る。
2. 同種二因子では、証明済みの幾何的Orlov中央化群とPell・反転核から、Galois不変な混合型の実現gerbe・period multiplierを計算する。k≥3の全H作用では混合は排除済み。
3. 位相分裂体上のind(α)と自己同型νの像を調べ、scalarと位相を同時に消す次数を決める。Hesse位相族の鋭さを一般上界の鋭さと混同しない。

`r³≃s³`だけを課した全根、全O認識開の境界、m=1の中心核、良い一ブロックの大域位相とscalar indexは独立な未解決課題として保持する。二捩れ境界では因子windowを構成したが、自然なθを同じ線同型として境界へ延ばす障害自体は消えていない。

**形式的点三次比較の独立な意味。** Jacobian tensor族のKontsevichグラフでは異色微分が零で、残る異色成分も配置空間次元と角形式の次数から消える。既存の一ブロック恒等式により `W_i=b_iJ_i`、block cube rescalingはG・内部次数・指定周期を保ち、可換方程式を元K上の `Σc_iλ_iJ_i` に固定できる。この形式入力に関する結果は直接積定理とは別に保持する。形式単元b_iや指定核全jetの代数性は主張しない。点三次の自然な全O射はmbplの全基本開上の射を既存全O認識開へ制限して得る。体上の固定点比較はmbrc、相対積核とPicard型の全O降下はmbrn・mbicで得た。任意型の相対核分類と大域核のsectionは別問題である。

**指定形式核の障害。** G-coherenceはcrossed product上のperfect加群として有限データとともに降ろす。有限型底の閉点は別の核を与えるため、指定形式核の全jetは保たない。`P¹`の`[X:Y]↦[X+(exp(h)−1)Y:Y]`のgraph核は指定核として有限代数拡大へ降りないが、恒等核は元の体上に存在する（`med:ex:formal-kernel`）。

**一次資料と寄与の区別。** THCRとshift規約はStafford–Van den Bergh §3の式(3.1),(3.3), Theorem3.2。Burke–Stevenson [arXiv:1507.00830v1](https://arxiv.org/pdf/1507.00830v1) §4 Proposition4.5・式(4.15)は局所化三角の参照であり、本件の必要な消滅は有限Koszulと中心商Torのpro-zeroを本文で証明した。相対認識はStacks Project [04Y5](https://stacks.math.columbia.edu/tag/04Y5)、[038U](https://stacks.math.columbia.edu/tag/038U)、[038X](https://stacks.math.columbia.edu/tag/038X)、[084Z](https://stacks.math.columbia.edu/tag/084Z)、[07SL](https://stacks.math.columbia.edu/tag/07SL)、05W5、0DUDを使用する。関係像の既存構成は047N,02G3,054K,052A,0DSL。点三次式はMori–Smith arXiv:1502.07403v2 Theorem7.2、配置空間と角形式はKontsevich §§5.1,6.1–6.3。

残余降下の一次資料は Bergh–Schnürer, Doc.Math.26(2021),1465–1500, [公刊PDF](https://ems.press/content/serial-article-files/26626), Propositions4.10,5.7・Corollaries4.12,5.8,5.9。line-valued MFの周期は Polishchuk–Vaintrob, Ann.Inst.Fourier61(2011),2609–2642, [公刊PDF](https://www.numdam.org/item/10.5802/aif.2788.pdf), Definitions1.1,1.3。群作用の随伴・strictification・SODは Shinder, Eur.J.Math.4(2018),413–422, [arXiv:1706.01714](https://arxiv.org/abs/1706.01714), Proposition3.13・Theorems5.4,6.2。Elagin [arXiv:1403.7027v2](https://arxiv.org/abs/1403.7027v2) Definitions3.1,3.5・§4・Theorem4.2・§8は作用・dual twist・二重同変化・dg enhancementの参照。

BFK I, Publ.Math.IHÉS120(2014),1–111, [公刊PDF](https://numdam.org/item/10.1007/s10240-013-0059-9.pdf), Definition3.50（群fiber product）・Corollary5.18（Morita外積）・Theorem6.13（Orlovとrotation）を確認。刊行pp.38,68–69,89–94とarXiv版のページを混同しない。BFK II, J.Math.Pures Appl.102(2014),702–757, [arXiv:1310.2656v2](https://arxiv.org/html/1310.2656v2), Theorem1.1・Corollary2.40・Theorem3.5・Corollaries3.6,4.6・Examples4.7,4.12には二楕円曲線の積によるcubic fourfold圏のcoverとrotation比が既にある。全k積公式はこれらの反復適用であり、本件の中心作用の内在化・表示障害・非可換一般点との接続から区別する。

因子rigidificationには Romagny, Michigan Math.J.53(2005),209–236, [著者PDF](https://imag.umontpellier.fr/~romagny/articles/group_actions.pdf), Theorem5.1・Remarks5.2 と Stacks [06PD](https://stacks.math.columbia.edu/tag/06PD) を使用する。相対比較には Ballard–Deliu–Favero–Isik–Katzarkov, [arXiv:1409.5568v1](https://arxiv.org/pdf/1409.5568v1), Corollary3.4・Propositions4.1,4.2,4.7,4.8とその後のKoszul対象を確認した。使用するのは実dg模型で、§5の最小A∞模型に関するConjecture5.1.2は入力にしない。Toën, Invent.Math.167(2007),615–667, DOI10.1007/s00222-006-0025-y, [2006年著者稿](https://www.math.univ-toulouse.fr/~btoen/mapdgcat.pdf)のTheorem8.15・Lemma8.11を一般可換環上のsmooth proper schemesに適用し、群線型化を核対応で移す。無条件の一般stack版として引用しない。相対phaseにはStacks [03PK](https://stacks.math.columbia.edu/tag/03PK), [040Q](https://stacks.math.columbia.edu/tag/040Q), [03RQ](https://stacks.math.columbia.edu/tag/03RQ)を参照する。rigidification、Kummer理論、可換Orlov–Thom–Sebastiani法自体の新規性は主張しない。

相対Hesse被覆には Mumford, Invent.Math.1(1966),287–354, DOI10.1007/BF01389737, §1 Theorems1–2 pp293–298 と Shin, Algebra Number Theory6(2012),1719–1772, DOI10.2140/ant.2012.6.1719, §2B(2-1), Lemma2.8, §2C を使用する。既知theta理論を普遍関係束へ適用し、冪等射影で非被約底の固有直線を構成した。DLL arXiv:1405.1158v1 §2 p3の3c3式を確認し、Introductionの表示と取り違えない。Keeler, J.Algebra265(2003),299–311, DOI10.1016/S0021-8693(03)00126-1 は [arXiv本文](https://arxiv.org/abs/math/0210417) のTheorem2.7, Lemmas2.4/4.4, Corollary3.5を確認した。Cor3.5は二因子であり全kのideal-sheaf/edge証明を補った。定理番号はarXiv版に従い、刊行PDFとの番号対応は未照合。Burke–Stevenson公刊版Definition5.1, Lemmas6.1–6.2, Theorem6.4の仮定を確認し、一般非可換TS定理を未確認の文献から引用せず本件の有限模型を本文で証明する。これらを組み合わせた結果の初出・新規性の網羅的確認は未完了。

相対noetherian性の追加入力は Keeler, *Ample filters of invertible sheaves*, J.Algebra259(2003),243–283、corrigendum J.Algebra507(2018),592–598、[訂正を含むarXiv:math/0108068v5](https://arxiv.org/abs/math/0108068v5)、Theorem1.5・Definition2.9・erratum TheoremE2.5。ここでnefは相対nefであり、coherent層の基底flatnessを要求しない。有限Koszul–Shamash Hom、Γ生成、windowからの実核と任意底変更への接続はmbrn節で証明する。

Picard型分類の基礎は Stacks [0DME](https://stacks.math.columbia.edu/tag/0DME) のPicard gerbeと [03PK](https://stacks.math.columbia.edu/tag/03PK) のKummer理論であり、外積bandの積とscalar-simpleなcoherent構造のcharacter差を本文で計算する。Hodge単元化には Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., III§1 Table3.1,p45 のc4,c6,ωの変換則を用いる。二捩れ境界の因子入力は Smith–Tate, K-Theory8(1994),19–63、[著者PDF](https://sites.math.washington.edu/~smith/Research/tate.pdf)、§1 pp19–21 のSklyanin正則中心商であり、order2は除外されていない。MF生成元のu⁻¹則は既存 `prop:nfm-period-equation-frame-change` の規約を用いる。既知Picard/Kummer理論と、自然な境界剰余・独立位相・指定型の最小次数という本件の適用を区別する。

全型分類の一次資料は Orlov, *Derived categories of coherent sheaves on Abelian varieties and equivalences between them*, Izv.Math.66(2002),569–594、[著者PDF](https://homepage.mi-ras.ru/~orlov/papers/abelnew.pdf)、[DOI](https://doi.org/10.1070/IM2002v066n03ABEH000389)。著者版Proposition2.15（p13）、Propositions3.2–3.3（pp16–17）、Theorem4.14（p22）を確認した。外積分解は代数閉体・標数零の完全列にblock対角性を加えた適用であり、k≥3では全H作用からその条件を証明する。一般Kで因子ごとの実核を仮定しない。Hesseの定数行列はArtebani–Dolgachev, Enseign.Math.55(2009),235–273、[刊行PDF](https://ems.press/content/serial-article-files/44190)、[DOI](https://doi.org/10.4171/LEM/55-3-3)、§4 pp246–247のpencil作用の核の生成元と照合した。これらの既知分類と、指定period multiplier・scalar和・全中心同変核の最小次数という本稿の帰結を分ける。新規性の網羅的確認は未了。

中心非正規性の入力は Seidel–Thomas, *Braid group actions on derived categories of coherent sheaves*, Duke Math.J.108(2001),37–108、[DOI](https://doi.org/10.1215/S0012-7094-01-10812-0)、[著者稿](https://arxiv.org/pdf/math/0001043) §2b Definition2.9・Proposition2.10（p15）、式(1.1)–(1.2)（pp3–4）。球面性をKu内で証明してこのdg評価構成を適用し、ambient Db(X)内での球面性は主張しない。Kuznetsovの[刊行版](https://math.nyu.edu/~tschinke/books/rationality/final/kuznetsov/kuznetsov.pdf) p220 (2)–(3)とSerre=[2]も確認した。球面捻り自体は既知であり、三平面による指定中心の非正規性・無限共役軌道の新規性は網羅的に未確認。

Veroneseの関連研究としてAitzhanova–Makar-Limanov–Umirbaev、J.Algebra Appl.24(2025),2550095、[DOI](https://doi.org/10.1142/S0219498825500951)の[MPIM著者稿](https://archive.mpim-bonn.mpg.de/id/eprint/4913/1/mpim-preprint_2023-14.pdf) Theorem1・Corollaries4,5を確認した。自由Poisson代数／多項式環のd剰余次数付き持上げであり、自由結合代数には§5の障害がある。本件への無条件の非可換持上げとして引用しない。Chan–Young–Zhang [arXiv:1606.01296v1](https://arxiv.org/pdf/1606.01296) Theorems0.1,0.2は1の冪根をパラメータとするskew polynomial環と判別式を扱う。Cooney–Grabowskiのgeometric仮定も点関係の過剰により直接適用しない。これらとの差と本件の飽和・中心剛性の組合せをIntroductionで明記したが、初出の網羅的確認は未完了。

**再現と確認状態。** `python3 computations/verify_multiblock_isogenous.py` はOrlov行列・整数annihilator、Rosati/Pell混合元、次数二反転、三平面Gramと無限軌道の有限恒等式を検算する。Orlovの全射・coherent lift・球面性・幾何的平面の実現は本文証明である。`python3 computations/verify_multiblock_hesse_phase.py` は二つの中心正則化chart、原点の三次jet、`dX/ω_H=V` とWeierstrass式、`qV=−1`、固定Hesse自己同型とν非零例を厳密な有理式で検算する。`verify_multiblock_point_line.py` の既存検算は、Fermat次数四関係行列と中心・交換子恒等式、Hesse点行列式と自然線比較certificateを保持する。これらはPBW全次数、window、圏同値、降下、最小次数の機械証明ではない。mbhp・mbic・mbfcの証明を執筆担当以外も独立読解した。実際の計算実行・source確認・組版・表示確認の範囲は `validation.md` に記す。

## 1. 記法と成果の確実性

以下の従来の1ブロック型の節では n ≥ 3、N = n+2、r = n−1、中心部分 U の次元はr、active 部分は3次元とする。多ブロックについては上記の k,m を使用する。点の空間 W = V* を用いるので F ∈ Sym³V = Sym³W*。B は周囲二次代数、A = B/(w) は中心三次商。QGr は全次数付き加群の torsion による Gabriel 商であり、qgr や compact dg 残余圏と混同しない。

現行論文には主要結果の証明を記載した。次の区分を守る。

| 主張 | 状態・依存 | 証明所在 |
|---|---|---|
| 全Poisson零集合の孤立点制約 | C上、任意のsmooth cubic、n≥3。未公表の全Poisson正規形を入力に、孤立零点ならn=3k、一般階数2k、局所完全交叉と証明。各active三次の楕円性は不要。新規性未確認 | `ppz:thm:isolated-zero-dimension` |
| 被約point/Poisson対応の反例 | 指定混合五様体のnorm全64根はsmooth properで、明示X_cへの実perfect Ku核を持つ。点スキームの被約孤立点により全smooth可換三次五様体・全πを排除。排除の証明自体はKu比較を入力にしない | `ppz:cor:reduced-point-poisson-counterexample`, `cmo:cor:norm-commutative-kernel` |
| 三様体の全スキーム版反例 | h=1の実Sklyanin因子と分離型直接Ku比較によりsourceを固定。長さ八局所環、全Poisson分類、BMMS Torelliで全Ku標的を排除。自然対の被約部分は一致 | `ppz:cor:complex-counterexample`, `esi:prop:factor`, `csc:cor:fermat` |
| 定数型二ブロックの全中心係数の実比較 | 全α,cで明示X_(α,c)への残余線束圏のMorita双加群を普遍環上に構成。smooth可換開では相対perfect核と各複素ファイバーの全coherent Ku同値。指定αのsmooth開は正確にP64≠0 | `cmo:thm:all-central-commutative-kernel`, `cmo:cor:all-alpha-central-kernel` |
| c=0候補の射影模型 | Eckardt点からの射影を四次二重被覆w²=LGで表し、Bl_p X₀がcrepant resolutionとなる。この幾何命題とは別に、全中心係数の実Ku比較を構成済み | `cmo:prop:zero-eckardt-resolution` |
| DVR上の実perfect比較核の有限判定 | smooth properな両側・既存perfect核・一般点同値を仮定。単位と余単位のconeの有限長和の零性が特殊同値と同値。元c族は相対実核で比較済み。h族の選択済み一般点核のdefect零と固定点核への接続は残る | `grl:prop:trait-kernel-test`, `mix:thm:h-integral-kernel` |
| 一般中心三次変形の完備MF移送と可換復元 | 統合済みの基礎定理。\(n\ge3\)、中心三次対の次数別自由性・滑らかな剰余の仮定。関数体上の方程式と有限拡大上のfull coherent Ku比較を区別 | `cft:thm:complete`, `gdr:thm:generic`, `rog:lem:descent` |
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
| 一般残余三次と射影 Poisson 射 | 固定 MF・window・一般点生成性・coherent 飽和性の下で、低積の積分直線・中心作用から稠密開上の支配射を構成。全 O-降下・任意底変更・一般相対次元1 | `thm:nfm-projective-residual-morphism`, `prop:nfm-projective-residual-dominance` |
| 同じ三次への被覆上の Ku 比較 | 表示 gerbe を分裂させた有限 étale 被覆上で比較核を構成。全 moduli 上の核・cocycle は未完成。全 n の標準 split 一般係数体では強化点型の class が一意で最小次数三、n=3,4 では全型でも三 | `thm:nfm-residual-comparison-cover`, `prop:nfm-residual-kernel-descent`, `thm:nfm-low-dimensional-full-class-index-three` |
| 相対中心作用と完備係数切断 | 選んだ生成元固定 graph flow は中心乗法を厳密保存。全 Taylor 成分を任意の斉次中心係数商へ降ろし、U=0 で完備 active MF 同値を構成。代数的 kernel の coherent 中心線型降下は未証明 | `lem:nfm-relative-center-transport`, `prop:nfm-completed-central-restriction`, `cor:nfm-completed-active-mf` |
| 残余射の全次数の形式像 | 相対 flow の低 Nat 同定の下で Ψ_res の形式像は (V(W_h),[π_h])。固定 harmonic 尺度と点微分の尺度は区別 | `cor:nfm-projective-formal-compatibility`, `prop:nfm-point-scale-formal-comparison` |
| 残余 active 曲線と点曲線 | 再帰の active 制限、同座標 Hesse 比較、係数空間への普遍化により W_act=b_hJ_g。全 O-stack 上で j が一致 | `lem:nfm-active-restriction-all-orders`, `prop:nfm-residual-active-point-cubic`, `thm:nfm-residual-point-j` |
| 十八重／二重同型被覆 | j≠0,1728。平面同型 I→M は rank18、Jacobian 同型 D→M は rank2、I→D は J_E[3]-torsor | `prop:nfm-point-residual-isom-cover` |
| 点微分による自然な残余射 | T≃λ_res*、T² の標準非零切断、Ψ_res^± の全 O-降下・任意底変更・支配性・一般有限性。D 上の full lift と shift の移送 | `prop:nfm-scale-hodge-line`, `thm:nfm-canonical-signed-residual-map`, `prop:nfm-point-normalized-jacobian-cover` |
| 残余射の正確な一般次数18 | 固定入力の下で全 n≥3。active 九次被覆・反対二重性に加え、全次数の有限混合三角性と proper/sign 安定化群の指数二から e_n=1。適切な開で M/⟨ι⟩≃Z | `prop:nfm-residual-mixed-triangular`, `lem:nfm-hesse-stabilizer-index-two`, `thm:nfm-residual-exact-degree-eighteen` |
| 全次数 potential の混合三角性 | TH逆像で規格化した W/b は active 体 C(g)((h)) 上で混合係数の多項式自己同型。TH scalar γ_h・純中心係数の倍率は active のみ。active 係数についての代数性は未主張 | `lem:nfm-trace-mixed-polynomial`, `prop:nfm-residual-mixed-triangular` |
| 符号類と反対被覆 | D→MのKummer類はactive不変量体から来るが、有限対角による延長でχ_act=0。χ_op=χ_sgnであり、半古典full射は一般次数9 | `thm:nfm-residual-sign-active-class`, `thm:nfm-active-sign-vanishing`, `cor:nfm-opposite-cover-active-twist` |
| 三捩れ対称族と有限対角延長 | 全n≥3の滑らかなC₃対称例で混合多項式模型が定義される。有限Isomを正規な二重・三重積へ延長し、同変なPoisson対を降下。有理三捩れからχ_actを消し、M≃Z×_Y P_Yを得る | `lem:nfm-hesse-kummer-injective`, `lem:nfm-finite-diagonal-rational-extension`, `lem:nfm-poisson-target-finite-diagonal`, `thm:nfm-active-sign-vanishing`, `cor:nfm-semiclassical-full-residual` |
| 反対な O-marked 対と同じ残余圏 | 一般の A と A^op は O-marked 圏として非同値。残余三次は同じで、共通の有限 étale 被覆上で両残余 dg 圏を同じ Ku に比較 | `prop:nfm-opposite-involution`, `thm:nfm-residual-opposite-even-degree`, `cor:nfm-opposite-same-residual-category` |
| 最高次 cohomology が線束となる比較核の型 | split 表示・source stabilization・Galinat window1 を固定。R_P=q_YΦ_P(κ_nc) の H^{>−1}=0、H^{−1} が次数零線束となる型は一般点の有限分離拡大上で非空。従来の Euler 条件も同時に保持 | `lem:nfm-linear-center-purity`, `prop:nfm-mf-linear-restriction`, `lem:nfm-active-line-rotation`, `prop:nfm-kernel-active-line-nonempty` |
| 点型の全O-降下 | κ_nc=j_nc^!O[1]、q_Y=Li_C^*j_Yを実際のwindow・Koszul比較で同定。最高次線束条件とm_P=p_resは良い一ブロックの共通稠密開へ全O-同値・任意底変更に両立して降下。Brauer–Severi ambientを許す | `lem:nfm-origin-object-weight-zero`, `prop:nfm-active-restriction-geometric`, `cor:nfm-point-type-O-descent` |
| 上の型の次元非依存 scalar 評価 | full kernel class 選択後、gerbe 上の正準的な最高次線束から重み1・階数3の束と次数3 Azumaya を構成し、split 体上で ind(α) は3を割る。αは次数零 Picard 類 m_P の表現障害であり、active 曲線上で消える。その次数3の横断切片は finite étale 分裂被覆。表示分裂後に上の型となる unsplit 体では3または9 | `thm:nfm-kernel-active-line-bound`, `cor:nfm-kernel-picard-obstruction`, `cor:nfm-kernel-active-curve-splitting`, `cor:nfm-kernel-active-line-unsplit` |
| 非分裂表示の最高次線束型のscalar period | class選択後、α=δ_C(m_P)。Brauer–Severi平面の偏極類がPic³(C)(K)の点を与えるため3[C]=0、Tate pairingにより3α=0。点型は特例。indexの既存上界3/9は保持し、Euler型だけの全核や非分裂体上のexact index三へは拡張しない | `cor:nfm-unsplit-point-scalar-period-three` |
| 非分裂曲線の点 Picard index 九 | 一般 Hesse 曲線の一般点 p と独立な theta twist により、α=δ_C(p) は period 三・index 九、偏極障害 β は index 三。α,β は線型独立で、曲線 C 自身も period 三・index 九 | `lem:nfm-bisymbol-index-nine`, `prop:nfm-unsplit-genus-one-picard-nine` |
| 非分裂一ブロック族と普遍の階数九 | 全 n≥4、n≡1 mod3 の任意の非空開に点障害 index 九の体値点を実現。普遍点 Picard gerbe は重み一・階数九束を持ち、どの非空開でも正の重み一階数は九の倍数。全非分裂体で一律の index 九とはしない | `prop:nfm-unsplit-point-index-nine-family`, `cor:nfm-universal-unsplit-picard-rank-nine` |
| 非分裂強化点型と最小次数九 | 随伴復元条件も全 O-降下し、S_p×Pic_C^p の記述を保持。指数九例の全実点型核は九で割れる次数を要する。表示安定化子が自明な共通稠密開内では全 n≡1 mod3 の強化点型が未標識最小次数九を達成 | `lem:nfm-adjoint-point-unsplit-descent`, `cor:nfm-unsplit-point-minimum-nine` |
| Picard 三分点被覆上の規格化核 | 実際の次数3線束 L から、[3]:J→J を表す線束 N_L を determinant で構成。full class 選択後、T_P^(3)=[3]⁻¹(m_P) は標準的な階数9有限 étale scalar 分裂被覆で、最高次線束を規格化した full 核を持つ。δ_C は J(S)/3J(S) を通り、m_P∈3J(S) なら元の底で中立 | `lem:nfm-picard-tripling-line`, `thm:nfm-kernel-tripling-cover`, `cor:nfm-kernel-picard-mod-three` |
| 一般点の三分点被覆の正確な次数 | 全n≥3の標準split一般係数体で[3]⁻¹(p_pt)≃[3]⁻¹(p_res)は連結九次体。Galois閉包はASL₂(F₃)で位数216、九次体は非Galoisで真の中間体を持たない。三分点の最小定義次数は九、Galois定義次数は216 | `lem:nfm-generic-hesse-third-division`, `lem:nfm-generic-active-three-torsion-monodromy`, `thm:nfm-generic-point-third-division-monodromy` |
| 相対THCR/windowと点型 | 指定中心商の相対THCR、Gorenstein条件、window1の閉／一般底変更を証明。φ∈I_sc、m_P=θ_sc(p_pt)のfull核の型が少なくとも一つの支配被覆上で非空。class選択後α=δ_C(p_res)。全refined核がこの型となることは未証明。強化点型のfull class選択は全nの一般点で解決 | `prop:nfm-relative-active-thcr`, `lem:nfm-active-dvr-gorenstein`, `prop:nfm-relative-active-window-basechange`, `prop:nfm-kernel-point-line-nonempty`, `cor:nfm-kernel-point-picard-obstruction` |
| 全 active Fourier–Mukai intertwiner の分類 | 実際の次数三線束を持つ二曲線間で、存在は偏極同型の存在と δ_E(p)=0 に同値。数値 centralizer の六元を全て含み、規格化核は graph と実線束に還元 | `lem:nfm-elliptic-numerical-graph`, `thm:nfm-elliptic-normalized-intertwiners`, `cor:nfm-elliptic-any-intertwiner-criterion`, `cor:nfm-elliptic-full-centralizer` |
| 相対 active 核の二段階障害 | 非被約底も含め、θを固定した規格化核の同型類層は I_θ、実現 gerbe は I_θ×Pic_C^(θp)。rotation 同型と三次周期の標識には別の μ₃-torsor が現れ、scalar G_m inertia は残る | `prop:nfm-elliptic-intertwiner-gerbe`, `rem:nfm-elliptic-period-phase` |
| 点行列と形式三分点 | 点関係行列の余核を次数零化した線束は3pを表す。完備半古典族では p≡0 により一意な q≡0、3q=p を得るが、完備化前の係数体の分裂は従わない | `prop:nfm-point-matrix-tripling-line`, `lem:nfm-formal-point-third-division` |
| full scalar 障害の cup 表示と二曲線の移送 | 選択済み点型で α=δ_C(p_res)。既知の Tate–Weil pairing により α=δ_E(p_pt)+e₃,*([I_sc]∪κ₃(p_pt))。Jacobian 同型だけでは二つの Picard 障害を同一視しない | `prop:nfm-kernel-flex-cup`, `prop:nfm-picard-plane-transfer` |
| 一般 j の Picard 障害と実 Sklyanin 実現 | Hesse 型三次と無限位数点に period=index=3 の明示巡回類を構成。幾何的 Sklyanin 代数と cyclic potential を元の体へ降下し、滑らかな commutator–gradient 形式で実現 | `prop:nfm-picard-cubic-index-sharp`, `cor:nfm-picard-infinite-translation`, `prop:nfm-active-point-sklyanin-realization` |
| 一般 split 表示の点障害 | 全 n≥3、純超越拡大上の支配族により一般係数体で per δ_E(p_pt)=ind δ_E(p_pt)=3。任意標的への全 active intertwiner は三に素な有限拡大後も存在しない。p_pt と p_res は三で割れない | `prop:nfm-active-point-obstruction-dominant`, `cor:nfm-generic-point-picard-index-three`, `cor:nfm-generic-active-intertwiner-obstruction` |
| 半古典平面同型の分裂と全 O-降下 | 混合定数降下と H_g の full ambient 作用により I_sc(k_n)≠∅。指定形式恒等分枝 φ_sc は良い一ブロックの共通滑らかな稠密開へ、全 O-同値・任意底変更に両立して降下。偏極線束の scalar 同型は未選択 | `thm:nfm-generic-plane-isom-splitting`, `prop:nfm-semiclassical-plane-isom-descent` |
| 残余 Picard 障害と選択後の scalar stage | full class 選択前から δ_Cres(p_res)=δ_Ept(p_pt) は exact period=index=3。点型 full class を選べた場合の scalar gerbe も index 三で、三次分裂体を持つ | `cor:nfm-generic-residual-picard-index-three` |
| 点型 full 核の不存在と比較被覆の次数 | 全n≥3で実際の点型 full P は k_n と三に素な有限拡大上に不存在。P を持つ有限 L/k_n は3∣[L:k_n]で、φの付加は不要。n=3,4では全full核へ下記の別証明で拡張 | `cor:nfm-point-comparison-cover-three-divisibility` |
| projector 核の一意性 | 全n≥3の滑らかな三次で、同じ標準projection exact functorを与えるperfect核は同型。従って可逆dg核の同型類からFM自己同値関手の同型類への写像は単射 | `lem:nfm-projector-kernel-uniqueness` |
| n=3,4のfull class選択と全型のscalar障害 | 既知の幾何的FM群分類を実核へ移し、K定義のT=ρ⁻¹[1]による定数Zを得る。有限像のGalois cocycleは零。全class gerbeが同じexact index三を持ち、周期標識を忘れた全full比較の最小体次数は三 | `lem:nfm-cyclic-kernel-class-descent`, `prop:nfm-generic-low-dimensional-kernel-aut`, `thm:nfm-low-dimensional-full-class-index-three` |
| 最高次線束からの原点像の復元 | q=Li_C* j_Yの右随伴q^R=j_Y!i_*はq^R(O_C)≃j_Y!O_Yを満たす。E_P=Φ_Pj_nc!O→q^RH⁰(qE_P)が同型となる強化点型は、形式恒等分枝と有限降下により全n≥3の一般点で非空 | `lem:nfm-origin-active-right-adjoint`, `prop:nfm-adjoint-point-type-nonempty` |
| 強化点型の有限class torsor | 全n≥3の標準split一般係数体でE_p=q^RMのclassはGalois不変。H_p=Stab_Gρ(E_p)は三対象生成・TV boundedness・HH¹=0により有限、強化点型class層は有限étale H_p-torsor S_p、実現stackはS_p×Pic_C^p。一般一ブロック族では下記のTate–Koszul忠実性により全nでH_p=1 | `lem:nfm-generator-stabilizer-finite`, `thm:nfm-adjoint-point-finite-class-torsor` |
| 低次元の正準classと奇数次元の残る有限群 | n=3,4ではH_p∩〈T〉=1とGρ=〈T〉から強化点型classは幾何的に一つ、K上で正準的に選ばれる。実核にはscalar分裂が必要。奇数nではEuler格子の非消滅とC₆からH_p⊂Gρ,0。全n≥3で最小強化点型実現次数はmin_i[K_i:K]ind(α_Ki)≤3|H_p|、S_p(K)≠∅なら三 | `cor:nfm-low-dimensional-canonical-adjoint-class`, `cor:nfm-odd-finite-stabilizer-numerical`, `cor:nfm-adjoint-point-realization-degree` |
| 全次元の原点・rotation 忠実性 | 通常 Ext を Tate の j≥0 切断から回復し、Adams Koszul 双対と再局所化により kernel class を Aut_gr(B,kΩ)/G_m へ単射。一般一ブロックで H_p=1、S_p=Spec(k_n)、強化型最小次数三 | `thm:nfm-origin-rotation-faithful`, `lem:nfm-generic-presentation-stabilizer-trivial`, `cor:nfm-generic-adjoint-class-unique` |
| 五次元 Clifford 半 rotation の降下 | 滑らかな幾何学的連結 F₂(Y) 上の相対 perfect 核と HH¹=0 から平面非依存 class を得る。square が実核 ρ、Fano 曲面の次数2835が奇数なので scalar 障害が消え、元の体上の実核 O を得る | `lem:nfm-fivefold-clifford-relative-kernel`, `prop:nfm-fivefold-half-rotation-plane-independent`, `thm:nfm-fivefold-half-rotation-kernel-descent` |
| 五次元半 rotation の同定と原点像 | O≃ρ⁻¹[1]、O³≃[1]、ε≃id を perfect 核として同定。E_p の二 mutation 表示も保持 | `lem:nfm-fivefold-spinor-relative-coevaluation`, `thm:nfm-fivefold-half-rotation-identification`, `prop:nfm-fivefold-origin-clifford-complex` |
| 高次元のfull class障害の縮約 | rotationを保つ群G_ρの中心にK上のT=ρ⁻¹[1]が定数Zを与える。各classとそのT軌道のGalois安定化群は一致。点型を含むGalois固定T軌道の存在と点型class選択が同値。強化点型の固定classは全nで存在するが、全群の分類は未証明 | `prop:nfm-highdim-rotation-serre`, `prop:nfm-highdim-central-shift-obstruction`, `cor:nfm-highdim-point-class-orbit` |
| 奇数次元の数値像と七次元の障害 | 奇数nの数値格子は階数二、rotation中央化群の像はC₆で、G_ρ/〈T〉≃G_ρ,0/〈[2]〉。一般三次七様体の既知球面対象からfull自己同値群にZ²、G_ρの無限指数を得る。高次元全群の巡回性へは拡張しない | `prop:nfm-odd-numerical-rotation-centralizer`, `prop:nfm-sevenfold-noncyclic-aut` |
| full比較の周期位相とclass不変性 | n=3,4では指定MF周期の中心的coherenceにより全T^mが周期を保ち、全full classに共通なμ₃位相γを得る。標識付き最小次数は成分体Mについて[M:k_n]ind(α_M)∈{3,9} | `lem:nfm-mf-period-central-coherence`, `prop:nfm-period-phase-class-invariance`, `eq:nfm-marked-minimum-index` |
| 相対的な周期規格化と正確な次数九 | Ω_nc↦uΩ_nc、F_Y↦vF_Yでτ↦u⁻¹τ、γ↦[v/u]γ。適合するtarget規格化を選べば標識付き最小次数三。targetだけに独立尺度tを加えたk_n(t)上では任意実現次数が九の倍数で、最小九。裸のO-pairの不変量とはしない | `prop:nfm-period-equation-frame-change`, `thm:nfm-free-period-frame-degree-nine`, `rem:nfm-period-frame-scope` |
| 半古典比較からの周期方程式のcube frame | 指定ΩからTHとΠを通じてPを復元し、t_scとφ_scの線型liftから残余方程式を三乗倍を除いて選ぶ。一般係数体では$J[3](k_n)$=0なのでφ_scは唯一。n=3,4の共通位相γ_scはlift・full class・同時尺度変更によらない | `prop:nfm-period-equation-cube-frame`, `cor:nfm-generic-plane-isom-unique` |
| γ_sc の形式像と非自明な位相体 | 完備半古典体では [b_h⁻¹]=1。一方 q=2 の完備局所値は全 n で [D_R] なので元の k_n の正準位相は非自明、位相体 M は三次。標識付き最小次数 3 ind(α_M) は三／九が未決 | `prop:nfm-period-phase-formal-active-scalar`, `prop:nfm-boundary-period-local-kummer` |
| 周期位相の二変数不変量体への降下 | 全 n≥3 の正準強化 class の γ_sc,n は C(s,t) へ一意に降下。D での付値は1 mod3で全次元共通。大域的な γ̄_n/[D] と次元間の一致は未決定。全 full class 共通性は n=3,4 に限る | `prop:nfm-adjoint-period-all-dimensions`, `prop:nfm-boundary-period-local-kummer` |
| 周期位相の条件付き大域式 | ΔD 外へ torsor が有限 étale に延びるという追加仮定の下で、半古典条件による三候補と既知の D 付値1が γ̄_n=[D] を与える。他の分岐の排除は未証明 | `lem:nfm-period-two-boundary-criterion`, `prop:nfm-boundary-period-local-kummer` |
| Hesse 境界の有限残余模型 | 点線束の相対行列を代数的 trait 上の有理式で構成。指定方程式・target 周期を保つ選択した integral 残余模型と、全nの点線束・右射影・有限MFを得る。特殊 fibre の滑らかさや模型の正準性は主張しない | `lem:nfm-hesse-boundary-explicit-line`, `prop:nfm-hesse-boundary-integral-residual-model`, `prop:nfm-boundary-right-projection`, `lem:nfm-boundary-line-mf` |
| 全次元境界の orbit Hom と積 | 十分強い極消去模型で全 Hom は自由かつ底変更可、rank HⁱRHom(Z,ρʲZ)=binom(n+2,3i+2j)。raw m₂* は階数を三失い、m₃ の三次 class は零。三つの Smith 指数は一、関係の飽和で全次数平坦な代数を得る | `prop:nfm-boundary-saturated-active-potential` |
| Hesse 境界の正準周期位相 | 飽和 active 格子で Ω_p は z 倍の primitive 中央元。smooth potential 三次を用いて指定 generic Isom を延長し、完備局所 γ_sc,n=[D_R]、Dでの付値1 mod3・tame三次分岐を証明 | `prop:nfm-boundary-period-local-kummer` |
| cup 補正と形式比較の限界 | 補正は H¹(J)[3] の genus-one torsor の差だけを見る。形式的に恒等へ近づく巡回平面 twist が非零補正・完全相殺を持つ例を構成。actual residual の同定には H_g など追加の降下構造が必要 | `lem:nfm-picard-torsor-quotient`, `prop:nfm-cyclic-plane-twist` |
| Euler 数値型の scalar index | split chart の指定 CF Euler 数値型で、核の同型類が整合した後に d_nα=0、一般点の ind(α) は d_n を割る。unsplit 体上の追加因子は高々3。この型の全ての核へ上の強い評価を拡張しない | `lem:nfm-cubic-euler-gcd`, `prop:nfm-kernel-three-primary`, `cor:nfm-generic-kernel-bound` |
| Euler 試験と符号被覆の限界 | stabilization の全 rotation 軌道の整数 K₀ 格子の pairing ideal は d_n Z。同型類が元の体上で選ばれていれば、三に素な体拡大・標準二重被覆では scalar index 不変 | `prop:nfm-kernel-euler-orbit-lattice`, `cor:nfm-kernel-prime-to-three-invariance` |
| active 核による別の十分条件と Hom 剛性化 | 元の核 gerbe 上の重み1 active 核と perfect mixed Hom の Euler 型 (0,3,−3) があれば index は3を割る。この追加構造は未構成だが、最高次線束による主経路には不要。最低 Hom の非零ベクトルによる Brauer–Severi 空間上の普遍核は標準手法 | 本ノート「active 比較による index 改善の十分条件」「最低 Hom による核の剛性化」 |
| 固定 tensor の超越性 | 普遍係数の関数体および各 n≥3 の very general な滑らかな係数で、固定 h/frame の π_h は非代数的。任意形式 frame を介した intrinsic 尺度の不存在は未主張 | `thm:nfm-normalized-tensor-transcendence` |
| 一変数の良い還元 | 選んだ CF から完成格子を降ろし、滑らかな三次 trait 模型を構成。正準性・kernel の延長は未証明 | `cor:nfm-residual-good-reduction` |
| 固定 formality の全次数補正 | 正規化逆 tensor の一意性、元の中心一次空間の保存、π_h=a_hι(dW_h)P と中心逆像。被約有限型普遍模型から任意基底変更。代数化・formality 独立性は含まない | `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir` |
| 形式 jet と五次の相違 | c₂=0、π,a は奇級数、W は偶級数。純 active π₅=S(g)Π_g/80、混合制限にも成立。固定 tensor は一般に五次で有限補正と異なる | `prop:nfm-third-tensor-scalar-zero`, `prop:nfm-normalized-parity`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction` |
| 全混合五次 tensor と残余四次項 | 既知 harmonic graph weights の厳密評価から β=1/60、γ=1/240。局所共変式と固定入力の中心公式により W₄=Ψ+I/24−J/80、a₄=S/240、純中心項も明示。固定 formality・指定中心規格化の下で全 n に一様 | `prop:nfm-mixed-fifth-explicit`, `lem:nfm-classical-mixed-covariants`, `thm:nfm-mixed-fourth-potential` |
| Hessian 補正後の四次障害 | 全 Jacobi 環の比較類を決定し、全 n の滑らかな一様例で非消滅。特殊ファイバー上恒等・同じ h を保つ形式同型を排除。Ku の同じ標識付き非同値は MF/window 入力付き | `cor:nfm-fourth-jacobi-class`, `prop:nfm-fourth-uniform-witness`, `cor:nfm-corrected-fourth-obstruction` |
| 全 O-同値へ降下する四次補正 | Φ^[4] は良い一ブロック開上の代数的 Poisson 射。指定族で三次は mod h⁶、tensor は mod h⁷ で実際の形式復元と一致。全次数の比較・一般次数・点曲線の厳密な一致は未証明 | `thm:nfm-fourth-algebraic-correction` |
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
| 全 intrinsic 成分・核の大域降下 | 未完成。一ブロック一般部分の自然な半古典full射（次数9）、さらに有限被覆上のKu比較と区別 | 研究方針の未解決課題 |

証明の記載と今回の点検を、外部査読や機械形式検証と同一視しない。新規性の網羅的確認は未完了である。

### 一般次元の四つの目標を接続する際の注意

研究方針の主目標は任意のnc cubicの可換Ku実現と、同じ可換標的でのpoint/Poisson零点対応の検証である。一般O-marked moduli、点復元、Poisson射、核降下はそのための構成として扱う。固定良好模型間の全 Hom 比較は対象の局所表示を与える定理ではなく、一ブロックの商 stack を構成することと全成分の一般対象を覆うことは分ける。各型の一般点で入力を確認し、複数ブロック型を一ブロックへ無条件に還元しない。

点商関手、shift のグラフ、中心射影は、全 O-同値の局所次数付き持上げを用いて局所一ブロック型の O-marked stack 上へ降下する。圏全体の次数一 shift を大域に選んだという主張ではない。定常成分 D と楕円成分 E は一般族の研究対象であり、E をモジュライの boundary と取り違えない。

Poisson 射は、正規化 trace と尺度付き Hessian から量子中心三次 w に古典 Casimir H_w を対応させることで構成した。滑らかな X_w=V(H_w) 上の tensor は一意な強い affine lift を持つため、lift を補助標識として保持せず、非零分解可能な三次 Poisson 対と偏極類のモジュライを標的にできる。良い開では逆構成があり、Msm≃Pgood となる。実際の相対 O(1) と偏極類は区別し、Brauer–Severi ambient を許す。この同型は指定した trace–Hessian 処方についてのものであり、Ku と整合する唯一の逆量子化を意味しない。

残余圏の復元が与える X_res と、trace–Hessian 射の X_TH は一致するとは限らない。全 n の split Hesse 族では、固定入力の下で幾何学的一般ファイバーの射影非同型を証明した。同じ周囲 Π の三次 Casimir を選び直しても解消しない。座標不変な代数的補正 Φ は全 O-同値へ降下し、一般次数9と楕円点曲線との厳密な一致を持つ。split 族では Φ の三次への残余比較を入力Bの下で得る。一方、一般混合係数では残余四次項と tensor の五次項を決定した結果、Φ の三次との標識付き比較にも四次障害が残ることが分かった。この障害を打ち消す別の代数的射 Φ^[4] を構成し、固定 harmonic-angle 模型の三次を mod h⁶、tensor を mod h⁷ で再現する。Φ と Φ^[4] の厳密な性質を混同しない。

一般混合係数の残余三次は低 rotation 積の有限行列から代数的に復元でき、全 O-降下する射影 Poisson 射と同じ X の Ku への有限被覆上の比較を得た。点微分から T² の標準切断を得て、符号商残余射の一般次数は正確に18となる。全次数の混合三角性により active 逆像と反対操作以外の有限分枝を排除し、標準二重被覆の符号障害を active 不変量体上の一つの二次類 χ_act へ帰着した。有限対角による同変延長を三捩れ対称点の近傍へ構成してχ_act=0を証明した。半古典規格化したfull射は次数9、反対同変であり、共通稠密開でM≃Z×_Y P_Yとなる。

比較核については、active 制限の最高次 cohomology が次数零線束となる非空な型を構成し、full kernel class 選択後の scalar index を split 表示上で3の約数へ抑えた。点型 m_P=p_res の非空性は相対THCR/window1から得られ、一般 split 係数体では I_sc の分裂と実 Sklyanin 支配族により δ_C(p_res)=δ_E(p_pt) の period と index が正確に三となる。最高次線束の点型は、κ_nc=j_nc^!O[1]、q_Y=Li_C^*|Ku(Y) という表示を通じて、良い一ブロックの共通稠密開へ全O-降下する。

さらにn=3,4では幾何的full自己同値群が、元の体上のT=ρ⁻¹[1]で生成される定数無限巡回群となる。これによりfull classの第一段階が解け、全classのscalar gerbeが同じexact index三を持つ。従ってこの二つの次元では任意の実際のfull核が元の体と三に素な有限拡大上に存在せず、周期同型を標識しない比較の最小体次数は三である。全n≥3では随伴復元条件を満たす非空な強化点型を取り出し、そのclass層を有限H_p-torsor S_pへ縮約した。全n≥3の一般一ブロック族ではTate–Koszul忠実性によりH_p=1、S_p=Spec(k_n)となり、強化型classは唯一で未標識最小実現次数三となる。全full classの分類は含まない。

指定MF周期のcoherenceから、n=3,4の追加のμ₃位相も全classで共通となる。位相に適合する方程式の相対規格化を選べば標識付き最小次数三、標的に独立尺度を付した一般族では正確に九である。source の Ω と唯一の φ_sc は target 方程式の cube frame を与える。全n≥3の正準強化classの位相 γ_sc,n は混合係数に依存せず C(c₄,−c₆) へ一意に降下する。半古典形式像は一だが、q=2 完備局所では [D_R] となり全次元で非自明である。大域的な γ̄_n/[D]、次元間の一致、三次位相体上の scalar index は未決定である。裸のO-marked対の障害と独立尺度の障害を混同しない。全nの標準三分点torsorの最小点定義次数九も、これとは別の構成である。非分裂の n≡1 mod3 では点障害の index 九を実現し、表示安定化子が自明な共通開では全該当次元の強化点型で未標識最小次数九を達成した。同じ例のrotation軌道の最小は三、n=4では全型の最小も三である。n=5 の半 rotation は平面に依存せず実核へ降下し、O≃ρ⁻¹[1]、ε≃id と同定した。残余位相 γ̄_n/[D] と位相体上の scalar index、coherent 中心線型性、任意 full 核への高次元の拡張は別に残る。

完備中心係数商の比較は構成できたが、その coherent な相対構造の代数的降下は別に必要である。最高次線束による指数評価はこの降下を前提とせず、active 比較自体や点 shift と Ku rotation の比較では引き続き有用な課題として残る。有限 jet を順に増やすこと自体は主経路にしない。二次・四次の混合比較障害は marked な形式比較の結果であり、unmarked な一般ファイバーの反例へ無条件に拡張しない。必要な有限係数拡大、rotation・三次周期、同値核の降下は保持する。一ブロックの良い開と Poisson 側の支配成分に関する成果を、全 intrinsic 圏成分の一般対象の被覆へ外挿しない。

general の稠密 Zariski 開、幾何学的一般点、very general の可算例外除去を区別する。very general な同値の存在だけでは、代数的な族の射や同値核の降下を得ない。まず関数体上の構成とその定義体を調べ、有限表示等の必要条件を確認して稠密開へ広げる。n=4 の幾何 locus と n≡1 mod3 の rotation 問題は、general を仮定するだけでは解決しない。

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

F=(x³+y³+z³)/3+Axy+Byz+Czx+Dx+Ey+Hz+G とし、A,B,Cは任意個の中心変数の一次式、D,E,Hは二次式、Gは三次式とする。量子化論文の `papers/sections/quantization/hesse_mixed_universal_center.tex`, `cor:pg-hesse-hessian-form` の短い中心元をΩ、純中心補正h²ABC/6を引いたものをΩtildeとすると、同入力の中心性を仮定した上で、現行のtrace計算は

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

### 一般係数の残余三次を代数的な族へ広げる

証明は `residual_algebraic.tex`。本稿の一般点可換復元・方程式の定義体降下を基礎として用い、ここでは相対的な方程式直線と全 O-同値への降下を構成する。

相対 proper 模型は、B の Koszul 複体を A に tensor した tails での完全性から、連続する N 個の O(i) を有限生成子とし、例外 block への有限 mutation で残余生成子を作って得る。generic smoothness を使う前に対角の compact 性を仮定しない。一般点の perfect 模型 E と射 E→Δ を広げ、底上 perfect な cone の台を除くことで smoothness を得る。低 Nat 複体の cohomology を局所自由にした後に、任意底変更を使う。

元の表示空間を支配する h-family は有限中心行列で作る。B_{hF} の次数3,4で δ_h(b)=(h⁻¹[x_i,b])_i を取り、δ_0 の核が kF⊕Sym³U、一般中心も同次元であることから単元 minor で消去する。Ω_h mod h=F が代数的に存在し、純中心 G を独立に動かすと (F,G,h)↦(B_{hF},[Ω_h+G]) は有理的に J×G_m を与える。一般係数体上の入力Bの適用は、有限 Koszul 行列・普遍 formality 恒等式・固定三対象の Laurent 局所化により行う。一本の固定特殊曲線の一般点から Msm の一般点を推論しない。

V_ρ=Nat⁰(Id,ρ)、Q=ker(Sym²V_ρ→Nat⁰(Id,ρ²)) の階数は N,N。scalar symmetrizer の開では D_Q の核 L が一意な方程式直線であり、任意底変更に両立する。全 N≥5 の巡回三次 Σx_i²x_{i+1} は scalar symmetrizer を持つ。x_4=⋯=x_N=x_1 の切断は x²y+y²z+z²x+(N−3)x³、特異条件は c³=−27/64 なので滑らかであり、必要な開の非空性を全次元で証明する。勾配復元そのものは Wang・Hwang の既知結果と区別する。

### 中心作用、全 O-降下と形式像

中心乗法は c:U→V_ρ を与える。特殊化の単射性だけでは h-torsion を排除できないため、可換完備側の perfect Nat 複体を使う。一般・特殊の H⁰ 次元が N で等しいことと DVR の universal coefficient 完全列から、H⁰ の自由性と必要な基底変更を得る。そこで rank n−1 の minor が単元となる。

次数一持上げの線束を M とすると V_ρ,U は重み1、Q は重み2、L は重み3、K_res=ann(cU) は重み−1。射影三次と support は全 O-同値に降下し、T=L⊗det K_res は重み零の通常の線束になる。full Poisson tensor の lift を分類するのは T^×。T≃λ_res* と点微分から T² の標準切断を得たが、元の stack 上の無条件の標準的な符号選択は未構成。n≡1 mod3 の非中立な表示 gerbe と両立するよう、標的は Brauer–Severi ambient を許す。

選んだ正規化模型では π_h=a_hι(dW_h)P_0。入力Bの明示 flow の primitive は Xi=a_hP_0 であり、すべてのグラフの出る辺は active 方向になる。曲率 W_h の頂点には出る辺がない。したがって flow と逆は Sym(U)[t^{±1}] に関して多重線型、単位正規化を保ち、MF 挿入で u·Id は厳密に同じ u·Id へ移る。これは任意の CF 同値についての主張ではない。

この相対 flow の低 Nat 同定の下で Ψ_res の一般形式像は (V(W_h),[π_h])。h=0 に延長する Poisson 直線は [π_h/h] であり、中心族 Ω_h+G の特殊三次は F+G である。純中心 G は tensor を変えないが underlying cubic を変える。一般の (F+G,U) を特殊点とする支配族から像の支配性が従い、次元差1と標数零の generic smoothness を使う。Φ の有限次数9をこの射へ移さない。

### 完備中心係数商と active MF

R を noetherian、R̂=R[[h]]、C=R̂[u₁,…,u_r] とし、完備化は内部次数ごとに h について取る。選んだ相対 flow の全 Taylor 成分 F_j と逆の H_j は C[t,t⁻¹]-多重線型であり、任意の斉次イデアル I⊂C による分離完備な係数商へ降りる。bar 恒等式・逆性・単位は各有限 h-切断で有限和の等式なので、非平坦な商でも保たれる。F_(2a)=H_(2a)=0、F_(2a+1),H_(2a+1)∈h^a、F₀=H₀=0 という評価が、有限自由 MF 行列の挿入公式を商上でも収束させる。したがって商上の全有限自由 MF 圏の実際の A∞ 同値を得る（`prop:nfm-completed-central-restriction`）。商上の対象が元の環へ持ち上がるという仮定は要らず、まず bar 写像自体を還元してから任意の MF 行列を挿入する。

I=(U) とすれば

\[
 \operatorname{MF}^{\mathbf Z}(B_h/(U),\Omega_h\bmod U)
 \simeq
 \operatorname{MF}^{\mathbf Z}(\widehat R[x,y,z],W_h|_{U=0})
\]

を得る（`cor:nfm-completed-active-mf`）。有限自由 rank、内部 shift、周期変数 t と (3)≃[2] は保たれる。W_h|_(U=0)=b_hJ_g の単元 b_h を除くときには指定周期の尺度も追う必要があるので、ここでは実際の potential を保持する。

この係数切断と、元の圏を Perf^gr(C) 上で導来 tensor した圏を商の全 MF 圏と同定する一般定理とは異なる。また、完備底上の全 Taylor 写像が C-線型であることと、代数的な一般点へ降ろした比較核が全 coherent な中心線型構造を持つことも異なる。有限個の中心 Nat 類の一致だけで全 coherence を指定したとはしない（`rem:nfm-central-restriction-scope`）。

**係数切断と categorical base change を区別する反例。** 非次数付きの C=k[u]、A=C[x]、W=x²+u を取る。任意の有限自由 MF 行列 Q は Q²=W·Id を満たすから

\[
 Q\,\partial_uQ+(\partial_uQ)Q=\operatorname{Id}
\]

となり、全対象が可縮で MF(A,W)=0。一方 u=0 では MF(k[x],x²) に二つの矢印が x である非零の rank 一 factorization がある。もしその恒等射が境界なら法 x で恒等射が零になり矛盾する。したがって MF(A,W)⊗_C^L k=0 であっても商代数の MF 圏は非零である。ambient が C 上自由、total ambient と特殊 ambient が正則という条件だけでは、両操作を同一視できない。本稿の滑らかな射影三次族そのものへの反例ではない。

**absolute perfect から relative perfect は従わない。** C=k[u]、A=B=k=C/(u) とする。Perf(k) の恒等関手は C-線型で、核 k は absolute 包絡代数 k 上 perfect である。しかし

\[
 A^{\mathrm{op}}\otimes_C^{\mathbf L}B
 \simeq E=k[\epsilon]/(\epsilon^2),\qquad |\epsilon|=-1
\]

上では perfect でない。実際、k の semifree E-分解を基底 e_j（j≥0）、|e_j|=−2j、de₀=0、de_j=εe_(j−1) で与えると、k⊗_E^L k の cohomology は各次数 −2j に k を持つ。k が E-perfect なら、この tensor は有限個の k の shift から作られて有界になるはずなので矛盾する。従って absolute な smooth proper 核の有限表示降下を、相対導来包絡代数上の perfect 核の降下へ置き換える際には、相対 perfect 性を別途証明する必要がある。この例は中心線型構造の降下自体が不可能であるとは述べていない。

**各ファイバーの perfect 性だけでは相対 perfect 性は従わない。** R=k[[t]]、K=k((t))、A=R[ε]/(ε²)、|ε|=1、d_A=0とする。次数零の生成元mを持つM=A·mにdm=tεmを入れると、MはR-perfectであり、M⊗_R k=A_k、M⊗_R K≃0なので両ファイバーはその代数上perfectである。しかしMはA-perfectでない。augmentation Rのsemifree分解P=⊕_(j≥0)Ae_j、|e_j|=0、de₀=0、de_j=εe_(j−1)を用いると、M⊗_A^L Rは⊕Rから⊕Rへの微分tI+shiftを持つ。そのH¹はK/Rであり、R-perfectでない。A-perfectならRへの導来tensorもperfectとなることに反する。一般の非connectiveなdg代数上のpseudo-perfect moduleに対し、ファイバーのcompact性をそのまま持ち上げる議論は使えない。A_k自体はsmoothでないので、smoothな特殊ファイバーを持つ代数の相対smoothnessへの反例ではない。

### 比較被覆と二種類の降下

同じ X_res への generic な kernel は入力Bの有限降下で得る。正規化・分岐 locus の除去と perfect kernel・逆・単位・余単位の spreading により、さらに小さい開の有限 étale 被覆上へ広げられる。裸の O-marked stack は global rotation や指定周期の自明化を持たず、それらは分裂被覆上で指定する。Brauer–Severi 族では O(i) を大域線束とせず、局所的に生成する admissible block とその直交を降ろす。

kernel 全体は自己同値 stack の torsor であり、P[2m] が同じ低積・rotation・周期を保つ無限個の非同型核を与える。まず kernel の同型類を整合させ、その後に scalar 二 cocycle c_ijk を調べる。HH¹=0 はこの二段階の解決を意味しない。たとえば K=k(h) 上の非分裂有限 étale cover z²=1+h は k((h)) 上で z≡1 の切断を持つ。形式的に指定した分枝と infinitesimal rigidity だけでは、完備化前の class 降下は従わない。n=3,4の一般点では、下記の全自己同値群の定数Zという別の入力により第一段階を解く。kernel gerbe と表示 gerbe β の同一視は用いない。

R=k[h]_(h) の一変数 trait については、完成格子が有限 jet から降下する。実際の Laurent 体上の CF で標準次数一格子を引き戻し、Λ=V_K∩Λ_hat と saturated な Q_R を取り、積分直線を降ろせば滑らかな三次模型を得る。これは CF の選択に依存し得る良い還元の存在であり、自然な相対 Hochschild 格子や kernel の h=0 への延長を証明したものではない。

### 固定 tensor の very general な超越性

普遍全三次係数 c に対する再帰は和・積・active 微分・固定 graph weights だけを使うため、各係数は C[c] に属する。PBW や MC を境界で主張せずとも、係数列自体は全 affine 空間上に定義される。π_h(dx,dy) の xy 係数 f(c,h) は xyz で ℓ(h)=log((2+h)/(2−h)) になる。ℓ が代数的なら、有限曲線上の dℓ=4dh/(4−h²) が h=2 の上で非零留数を持ち、完全微分の留数零に反する。

固定 d,e について M=(d+1)(e+1) 個の級数 h^i f^j を列とする係数行列を取る。すべての M 次 minor の零 locus Z_{d,e} は閉であり、xyz の超越性から真である。代数的な特殊化の全体は可算和 ∪Z_{d,e} に等しい。これにより一般関数体と任意の非空滑らかな係数開の very general な点での非代数性を得る。単一の Zariski 開での全点の主張ではない。

有限代数拡大と代数的に可逆な frame 変更では障害は消えない。一方、CF が供給する Nat frame 自体は形式的である。従って intrinsic な代数的尺度切断がその形式 frame を介して π_h に一致する可能性は、この定理からは排除されない。W_h の特定係数の超越性、任意の full Poisson 射の不存在も未主張である。

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

### 全混合五次 tensor と古典的共変式

`prop:nfm-mixed-fifth-reduction` に全証明とI,Jのε縮約を置く。T=F'''_active、M=F''_active、q=F'_active とすると、再帰の五次項はqT⁴またはM²T³の型だけを持つ。Weyl対称化の局所性も二次式の恒等式で確認しており、裸の座標やF自身を追加のjetとして使わない。この二型の一次形式共変式の次元はそれぞれ1と2。S(g)dF,dI,dJの独立性を行列式−35/3で示し、全nで

```
π₅(F)=Π_Q₅,
Q₅=S(g)F/80+β(I(F)−S(g)F)+γ(J(F)−S(g)F)
```

へ還元する。二つの独立な混合 Taylor jet における正規化再帰を厳密評価すると、β=1/60、γ=1/240 であり、従って

\[
 \pi_5(F)=\frac1{240}\Pi_{4I(F)+J(F)-2S(g)F}
\]

となる（`prop:nfm-mixed-fifth-explicit`）。普遍還元の証明があるため、二標本から一般係数の公式を補間したものではない。三次共変式の一次元性から I(g)=J(g)=S(g)g も恒等的に得る。F=g(x+a(U))+G(U) では両追加項の active 勾配が零となり、分離型だけでは二定数を決められないという障害は保持する。

入力は Banks–Panzer–Pym の harmonic graph weights と、Buring の著者公開データ `star5.txt`, `kontsevich_2_k.txt`, `weights_kontsevich_2_k.txt`（1≤k≤5）。線型二入力・二次 tensor に寄与する73項を `computations/data/harmonic_linear_products.json` に保持し、出典、元入力の SHA-256、規約、グラフの自己同型数を付す。元の `fg+t{f,g}+…` を本稿の `fg+h{f,g}/2+…` へ直す係数 2^(−k) と、正規化後の weight/automorphisms を照合した。`verify_mixed_fifth.py` は有理数による評価器であり、既知の積分重みそのものを再計算したわけではない。二つの独立な評価実装、第三の混合 jet、純 log-canonical 模型の既知交換比との比較を行った範囲は `validation.md` に記す。

I,J は古典的な写像の微分でも計算できる（`lem:nfm-classical-mixed-covariants`）。ℋ(F)=det Hess_K(F) とすると

\[
 I(F)=\frac1{12}\operatorname{tr}
       \bigl(\operatorname{adj}(M)\operatorname{Hess}_K(\mathscr H(F))\bigr)
     =\frac1{12}D\mathscr H_F[\mathscr H(F)],
 \qquad
 J(F)=\frac14(dS)_T[M\odot q],
\]

ただし (M⊙q)_ijk=(M_ij q_k+M_ik q_j+M_jk q_i)/3 とする。第二式の微分は対称三階 tensor T の空間上で取る。三次多項式 g(ξ)=T(ξ,ξ,ξ)/6 の規約なら、J=(dS)_g[q(ξ)M(ξ,ξ)]/24 である。十個の T、六個の M、三個の q を独立記号とした多項式恒等式でも確認した。Hessian 写像・Aronhold 不変式自体の新規性は主張しない。

### 中心逆像の四次項と標識付き障害

`lem:nfm-fourth-center-locality` の局所性を使うと、W₄−Ψ_λ(F) に現れ得るスカラー共変式は qMT³ と M³T² の二型で、それぞれ一次元である。Weyl 対称化と中心写像は単位を固定し active affine 変換に共変なので、微分されない F は追加の局所 jet として現れない。固定入力の Ψ の式と五次 tensor の係数を合わせると

\[
 W_4=\Psi_\lambda(F)+I(F)/24-J(F)/80,
 \qquad a_h=h\bigl(1+S(g)h^4/240\bigr)+O(h^7)
\]

となる（`thm:nfm-mixed-fourth-potential`）。四次の中心写像のグラフ積分を別途評価する必要はない。指定 Hesse 中心規格化の下で、純中心項も

\[
 \begin{aligned}
 W_4&=-SF/80+I/60+J/240+\mathcal C_4(U),\\
 \mathcal C_4(U)&=\lambda(A^3+B^3+C^3)/60+\lambda^2ABC/40\\
 &\hspace{8mm}+(2-\lambda^3)(AH+BD+CE)/180+SG/80
 \end{aligned}
\]

と明示される（`lem:nfm-fourth-center-symbol`）。ここで S=λ(λ³−8)。中心元を任意の形式単元倍に替えると a_h は変わり、純中心三次を加えると W_h も同じだけ変わる。この規格化依存性は残る。

J の縮約には q_l=F_l が因子として現れるので J=Σ_l B_lF_l、B_l は全座標の一次式であり、[J]=0 と τ_F(J)=0 が成立する。全 Jacobi 環ではさらに [F]=0 となる。そのため四次比較類は

\[
 \Delta_4(F)=[W_4-\tau_F(\Psi_\lambda(F))]
 =\frac{[I(F)]}{60}+\frac{[\tau_F(I(F))]}{40}
                  +\frac{S[\tau_F(F)]}{80}
\]

である（`cor:nfm-fourth-jacobi-class`）。γ、a₄、純中心項の独立した評価は、この幾何的比較には不要となる。

λ=0 の全混合族では、R₁₁=ACx+ABy+BCz、K=AH+BD+CE と置くと、active 勾配の明示的な倍数を引いて I≡20R₁₁/3+8K/3、τ_F(I)=8K/3 を得る。従って Δ₄=[R₁₁+K]/9。各 n≥3 の共通の例

\[
 F_*=(x^3+y^3+z^3+u^3+v^3+\sum_{j=1}^{n-3}w_j^3)/3+uxy+vyz
\]

は滑らかで、Δ₄(F_*)=[uvy]/9≠0 となる。ℓ(vx²)=ℓ(uz²)=1、ℓ(uvy)=−1、その他の三次単項式では零という汎関数が Jacobi ideal の次数三部分と全純中心三次を消し、ℓ(Δ₄)=−1/9 を与える。非消滅は各次元の滑らかな係数開上の Jacobi 束の正則切断として非空 Zariski 開を定める（`prop:nfm-fourth-uniform-witness`）。純中心三次の像でさらに商を取った空間の一定階数性は使わない。

この非消滅開では、W_h と H♯ の三次族を同じ h と特殊ファイバー上の同定を保って C[h]/(h⁵) 上で同型にすることはできない。固定入力の剰余で恒等な MF/window 比較を適用する場合は、HH¹=0 と実際の幾何的 KS 単射により、同じ標識を持つ C[[h]]-線型 dg Morita 同値も存在しない（`cor:nfm-corrected-fourth-obstruction`）。この入力付きの主張は n=4 でも成り立つ。一般ファイバー上の unmarked な三次または Ku の非同値は、この有限 jet だけからは結論しない。

### 全 O-同値へ降下する四次補正

四つの ε を P で置き換えた縮約を S_P(H),I_P(H),J_P(H) とし、τ=τ_{H,K} とする。有限式

\[
 \begin{aligned}
 \mathcal E_P(H)&=I_P(H)/60+J_P(H)/240
       -S_P(H)\bigl(H-\tau(H)\bigr)/80+\tau(I_P(H))/40,\\
 H^{[4]}&=H^\sharp+\mathcal E_P(H),\qquad
 P^{[4]}=\bigl(1+S_P(H)/240\bigr)P
 \end{aligned}
\]

により、出力の滑らかさと係数の単元条件を満たす非空開上の代数的射 Φ^[4] を得る（`thm:nfm-fourth-algebraic-correction`）。(H,P)→(cH,c⁻¹P) では S_P は不変、I_P,J_P,E_P は c 倍であり、純中心三次の加算で E_P は変わらない。trace と縮約の任意底変更・全線型変換への共変性から、既存の良い一ブロック O-marked 開へ降下する。

指定中心元の H_TH と P=hP₀ に沿っては、H^[4]≡W_h mod h⁶、ι(dH^[4])P^[4]≡π_h mod h⁷ が全混合係数で成立する。有限式の代数性と、全次数の残余比較・形式復元の代数化は区別する。従来の Φ が持つ一般次数9と楕円点曲線との厳密な一致を Φ^[4] に移してはいない。実際、純 active では E_{hP₀}(g)=h⁴S(g)g/120 であり、新しい射の一般次数も未決定である。

### 点曲線と残余 active 切断の全次数比較

主証明は `residual_point_scale.tex`。生成元固定再帰の各段階は active 微分・有限の積と和であるため、π_h(F)|_(U=0)=π_h^act(g) は普遍係数環上の恒等式である。既存 split Hesse 証明が与える **同じ座標での** potential の比例を、SL₃×A²→Sym³(C³)* の支配性で全係数へ広げると、J_g=g+h²Hess(g)/24 は全次数で Casimir となる。Koszul 正則性と斉次三次の Euler 恒等式から W_h|_K=b_hJ_g を得る。AKW の j の一致だけをこの比例の代わりに用いてはいない。

相対 flow の中心保存と支配的 h-family による関数体の単射から、元の O-stack 上で j(E_pt)=j(C_res)。形式同定の行列の代数化、MF 圏の U=0 基底変更、n=1 への field-model 定理の適用は使わない。h=0 で延長する点曲線は一般ファイバーの楕円成分の閉包であり、可換代数の点スキーム全体ではない。

j≠0,1728 では D=Isom_gp(J_E,J_C) は μ₂-torsor。曲線自体を同定するには Jacobian の torsor の差があり、次数三偏極を合わせるには [3]q=a を解く。従って平面対の同型 I→D は J_E[3]-torsor、I→M は階数18となる。偏極**類**を保持し、O(1) の線束同型の scalar をデータに加えない。Brauer–Severi 平面は étale 局所的に split して降下する。

### 点微分・Hodge 線束と自然な符号商射

相対随伴は λ_res≃(L⊗det K_res)* を与える。表示変更 L→L⊗M³、K→K⊗M⁻¹ の重みが相殺するため、T=λ_res* は元の O-stack 上の線束である。方程式 G と volume P に対し、双対微分は Res(ι_Eν_P/G) であり、G→aG、P→bP で (ab)⁻¹ 倍になる。

Φ の点曲線公式から τ_pt=(H♯|K)⊗P∈λ_pt* が標準的に定まる。c₄,c₆,Δ の規約を両側でそろえ、


\[
 b_{\rm res}=c_{6,\rm res}/c_{4,\rm res}\in T^{-2},\quad
 b_{\rm pt}=(c_{6,\rm pt}/c_{4,\rm pt})(\tau_{\rm pt}^2),\quad
 \eta_{\rm res}=b_{\rm pt}b_{\rm res}^{-1}\in(T^2)^\times
\]

と置く。η_res が自然な Ψ_res^±:M→[Pdec/μ₂] を定め、平方根の被覆が上の D に一致する。D 上の θ は ω_res=(θ*)⁻¹ω_pt を与える。c₄,res(η²)=c₄,pt(τ_pt⁴)、c₆,res(η³)=c₆,pt(τ_pt⁶) も元の開へ降りる。

支配性には j の一致を使わず、零切断への特殊化を使う。一般の中心 lift Ω_h+G に対応する active primitive が c(h)g なら volume は (h/c(h))P₀、補正 active は c(h)J_g であり、τ_pt=hJ_g⊗P₀ と厳密に相殺する。従って η_res=h²・unit。残余側の特殊対は一般の (F+G,K) なので、全尺度平方線束内の像の既約閉包は零切断全体と非零点を含み、全空間となる。同次元性から一般有限、自己同型なしの開で有限化と分岐除去により有限 étale 全射を得る。形式 Nat frame の代数性は要求しない。

この D は modular 正規化 {t:b_res(t²)=1} と異なり、その差は b_pt の平方根の Kummer torsor である。Δ∈λ_res¹² は T¹² を自明化し、modular な12重・2重尺度被覆も与えるが、標的の曲線だけからの正規化では相対次元1の方向の支配性は出ない。点微分がその方向を保つ。

形式的な恒等分枝では τ_res^pt=(h/b_h)W_h⊗P₀、Π_res^pt=(h/c_h)π_h。c_h=h+S(g)h⁵/80+O(h⁷) なので一般には同じ harmonic 尺度ではない。比の代数性も仮定しない。一般次数は正確に18であり、D の一般点の類は補正前の active 不変量体から来る。有限対角による近傍延長からこの二次類を消し、元の稠密開上で半古典規格化を得る。証明は下記を参照する。T の一般点で非標準的な切断を選べば元の開上の full 一般有限射も作れるが、その一般次数は選択で変わり、点微分を保つとは限らない。

点 shift は固定点なしなので Jac(E_pt) の一意な切断 p による平行移動である。D 上で θ(p) を C_res の torsor 作用へ入れれば σ_res を得る。I 上の平面同型はこれを共役で移し、反転は (Π_res^pt,σ_res)→(−Π_res^pt,σ_res⁻¹) を与える。Ku rotation 自体をこの平行移動と同一視する証明はない。固定入力から得た相対active window比較では、rotationの共役からm_P=θ_sc(p_pt)の非空な型を得るが、full Ku rotation自体の同定とは別の内容である。定常成分まで残余側で同定したわけでもない。

### 反対操作・active 九次被覆と正確な一般次数

語順反転は B(V,U,Π)^op≃B(V,U,−Π) を与え、表示変更と可換なので O-marked stack の involution ι に降下する。最大可換商、中心元の可換像、Π に関して偶数の Hessian は変わらないため、trace–Hessian 同型の下では (X_TH,Π)↦(X_TH,−Π)。一般の滑らかな三次 n-fold は射影自己同型を持たないので、全 n≥3 の稠密開で ι は自由である。点対応のグラフは転置され、E_pt は同じ、σ_pt は逆、τ_pt は負になる（`prop:nfm-opposite-involution`）。

支配的中心族の持上げを (Ω_h+rev(Ω_−h))/2 に置き換えると、剰余 F と中心三次 torsor の支配性を保持しつつ、反転に不変な代数的中心元を得る。Weyl symbol と W_h は h の偶数級数となる。支配的形式族の関数体の k(G)((h)) への単射を使い、慣性自明な scheme 標的への射として Ψ_resι=Ψ_res、Ψ_res^±ι=Ψ_res^± を忠実に検査する（`lem:nfm-even-dominant-central-family`, `thm:nfm-residual-opposite-even-degree`）。反対圏や導来双対を rotation 保存の共変同値として扱う議論ではない。

active 三次 f の不変量 S=c₄(f)、T=−c₆(f) に対し、φ₃(f)=f+det Hess(f)/24 は a:A²→A² を誘導する。Hesse 族では

\[
 g_{p,q}=p(x^3+y^3+z^3)/3+qxyz,\qquad
 r(p,q)=\bigl(q(q^3-8p^3),\,q^6+20p^3q^3-8p^6\bigr),
\]

\[
 \psi(p,q)=\bigl(p(1-q^2/4),\,q+p^3/3+q^3/12\bigr),\qquad
 r\psi=ar,\qquad \det Dr=-384p^2(p^3+q^3)^2.
\]

r の一般有限性と ψ の次数9から deg a=9を得る（`lem:nfm-active-invariant-degree-nine`）。c₄,c₆ の規約は Weierstrass 式と随伴留数 dx/(2y) によって Hodge 線束の modular forms と合わせる。点規格化が両不変量を保つため、補正前の active 写像 w₀ と符号商標的の w_Y は w_YΨ_res^±=aw₀ を満たす。

**一般ファイバーの整性。** 固定 support・volume で全三次を active 三次へ制限すると、混合係数と純中心係数の affine 空間をファイバーに持つ。Fisher の同じ不変量を持つ smooth form の proper-equivalence 分類により、幾何学的一般 active ファイバーは一つの SL₃ 軌道で既約。被約性は別に、正則な係数環の一般ファイバーが標数零で幾何学的に正則であることから得る。非空開と滑らかな商 atlas による降下を用いると、full Poisson 側と符号商側の両方で一般ファイバーは幾何学的に整である（`lem:nfm-active-invariant-regular-fiber`）。一般点上の rational frame や Brauer–Severi ambient の分裂は仮定しない。

K=C(Y)、L=C(M)、標的不変量体 K₀、補正前の不変量体 L₀ に対し [L₀:K₀]=9。K/K₀ の正則性から K⊗_(K₀)L₀ は体であり、Z=Y×_(A²,a)A² は整な九次中間被覆となる。反対操作は残余値と w₀ を保つ。全次数の混合三角性によって残る因子 e_n=1 を示すと、適切な非空開で

\[
 M\longrightarrow M/\langle\iota\rangle\simeq Z\longrightarrow Y
\]

は階数2,9の有限 étale 全射となり、**deg Ψ_res^±=18** を得る（因子分解は `thm:nfm-residual-degree-eighteen`、正確な次数は `thm:nfm-residual-exact-degree-eighteen`）。平面同型被覆 I の階数18とは別の構成であり、Φ の次数9を残余射へ直接移していない。

a の二成分は `computations/verify_active_invariants.py` にある。D(S,T)=1−S/24−T/216−S²/6912 とすると、a=(a₄,a₆^−) に対して a₄³−(a₆^−)²=(S³−T²)D³、det Da=(1−S/16)D² を有理数係数で検算した。これは不変量の規約と有限式の検証であり、boundary の分類を優先する理由とはしない。

### 全次数の有限混合三角性と体の比較

本文 `prop:nfm-residual-mixed-triangular` の分解を F=g+b+ℓ+d とする。b,ℓ,d の中心次数は1,2,3。中心元を Ω_TH=d_(hΠF)^−1(F) と一意に規格化し、active 部 J_g=g+h²Hess(g)/24 に合わせた residual potential は

\[
 \widehat W_h
 =J_g+A_h(g)b+B_h(g)\ell+Q_h(g)(b,b)
   +\gamma_h(g)d+R_h(g)(b,\ell)+S_h(g)(b,b,b).
\]

A_h,B_h は可逆線型作用素、γ_hは非零scalarであり、係数は k((h))、k=C(g) に属する。三つの対角が可逆なので、混合係数の写像は **k((h))上の多項式自己同型**。作用素はactive微分と中心因子の積だけを使い、中心変数の個数に依存しない。active係数についての有理性や、harmonic tensor の代数性を結論していない。

再開時に失わない証明上の点は次のとおり。

- graph再帰は各h係数で普遍多項式。b,ℓの重み1,2と出力のU次数が一致し、tensorで高々2、三次potentialで高々3となるため、**混合単項式の個数は全h次数を通じて有限**である。
- R_h=φ∘sym と CπはU次数を下げず、次数三空間の有限filtrationの対角blockはgだけに依存する。逆R_hもmixedに多項式。Jacobi trace の同じ性質は、active最高次勾配の正則列とfiltered自由基底から得る（`lem:nfm-trace-mixed-polynomial`）。
- raw primitive V_hを中心へ移したTH像は γ_h(g)(g+b+ℓ)+D_hで、D_hは重み三のbℓ,b³だけを含む。商直線の係数γ_hはU=0で決まる。TH式はh²で割るため、γ_h≡1は先頭項だけでなく、既存Hessian二次jetを持つ中心元と完備中心商rank1を使って証明する。W_THのactive scalarはb_h=γ_h^−1であり、純中心係数の倍率もactive-onlyである。
- H同変性は、一意なTH規格化W_THの線型共変性とactive scalarの不変性から得る。純中心項を零にしたraw primitiveのせん断共変性を無断で仮定しない。

次数計算では k=C(p,q)、κ=k((h)) とし、補正前のactive不変量体L₀を s↦h⁴c₄(g), t↦−h⁶c₆(g) でκへ入れる。sourceとZのL₀上の一般ファイバーは幾何学的に整なので、このactive基底だけの拡大は一般次数を保つ。候補射は有限混合多項式性によりκ(m)で定義され、実際のintrinsic残余射も同じ体上にある。より大きい体 k(m)((h)) で形式CF比較により両射を同定し、scheme標的への射の等式を忠実降下する。Nat frame自身がκ(m)へ降りる必要はない。**単なるk(m)((h))上の形式逆から次数一を結論する方法とは区別する。**

gとJ_gは同じHesse pencilにあり、proper projective stabilizerは共通のT₉。固定supportのparabolic G_K→PGL(K)で、その逆像Hを取る。sign targetの安定化群H^±はHを指数二で含み、奇置換と符号−1が非自明cosetを与える。三角同型は[A_g/H]≃[A_J/H]を与え、sign商への写像だけが次数二となる（`lem:nfm-hesse-stabilizer-index-two`）。SL₃の中心μ₃を別に数えず、gと−gが同じproper orbitにあることもこの固定切片と安定化群で扱う。

### 符号二次類と反対被覆の twist

L=C(M)はL₀=C(s,t)上正則であり、尺度二重被覆D→Mの一般点の類は、一意な

\[
 \chi_{\mathrm{act}}\in L_0^\times/(L_0^\times)^2
\]

の引戻しである（`thm:nfm-residual-sign-active-class`）。κへの基底変更後、三角写像はproper subgroup Hの商上でfull Poisson targetへのliftを与えるので、Dは**商の一般点でも**splitする。mixed affine atlas上だけのsectionから結論したのではない。

用いる体論は `lem:nfm-quadratic-class-constant-descent`。正則な有限生成拡大L/k上の二次類が定数体拡大で消えるなら、その類はk由来である。非自明な二次拡大E/Lがk上正則なら、任意の定数体拡大後も整でありsplitできない。従ってEはkの二次拡大を含み、それとの合成体に等しくなる。正則性によるKummer類の単射性が一意性も与える。

F_Z=C(Z)上で、反対被覆M→Zの類をχ_op、full Poisson符号被覆をZへ引いた類をχ_sgnとすると

\[
 \chi_{\mathrm{op}}=\chi_{\mathrm{sgn}}+\chi_{\mathrm{act}}
       \quad\text{in }H^1(F_Z,\mu_2).
\]

両者のMへの制限を比較し、二次拡大のKummer制限の核と、full Poisson側のactive一般ファイバーの幾何学的整性を使う（`cor:nfm-opposite-cover-active-twist`）。したがってM→Zはfull Poisson符号被覆のactive二次twistである。これらのμ₂類は表示gerbeやkernel scalar gerbeのBrauer類とは異なる。

点微分に整合する full lift の**有理的な存在**は χ_act=0 と同値である。下の有限対角による延長でこの消滅を証明し、半古典先頭項で規格化された一般次数9のfull射を得た。κへの体拡大だけではL₀上の二次類の消滅を戻せない。例えば1+sはC(s,t)で平方でないが、s=h⁴c₄(g)を代入するとκで形式平方根を持つ。証明に使うのは、K=C(p,q,h)上での近傍延長と有理三捩れ点である。

D={t²=η_res}上のι_+(a,t)=(ιa,t)、ι_−(a,t)=(ιa,−t)は可換で、積はdeck変換。ι_+はfull tensorと移送shiftを保ち、θを−θへ送る。ι_−はθを保ち、tensorの符号とshiftを反転する（`cor:nfm-opposite-scale-cover-actions`）。一般のAとA^opはO-marked圏として非同値だが同じX_resを持ち、共通有限étale被覆上で両残余dg圏をKu(X_res)に比較できる（`cor:nfm-opposite-same-residual-category`）。標準核や元の開への核の降下はこれからは得られない。

### 三捩れ対称族と有限対角による active 符号の消滅

全 r=n−1≥2 に対し、三次

\[
 F_{p,q}=\frac p3(x^3+y^3+z^3)+qxyz
             +x\sum_i u_i^2+\frac13\sum_i u_i^3
\]

を用いる。p=q=1 の場合は滑らかで scalar symmetrizer を持ち、従って一般の p,q でも同じ性質を持つ。σ=diag(1,ζ,ζ²;1,…,1) はこの族を保つ（`lem:nfm-cyclic-scalar-witness`）。[量子化論文](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex)の普遍 Hesse 中心式と固定入力Bをこの族自身へ適用すると、K=C(p,q)(h) 上に残余 active 曲線 C_σ と点曲線 E_σ が構成できる。残余側では σ が Hodge 微分を固定し、非零の K-有理三捩れ平行移動を与える。点側の全三捩れは K-有理であるため、j≠0,1728 上の Jacobian-Isom の二次 twist は自明となる（`prop:nfm-cyclic-test-sign-split`）。

Hesse 不変量 s=q(q³−8p³)、t=q⁶+20p³q³−8p⁶ に対し、C(s,t) から C(p,q) への二次類の制限は単射である（`lem:nfm-hesse-kummer-injective`）。本文は次数24の Hesse 体拡大と、その群 Q₈⋊C₃ が非自明な μ₂ 指標を持たないことを直接確認する。この体論と上の対称族自身の分裂だけではχ_actを閉じた族へ特殊化できないため、次の代数的延長を構成する。

**有限対角による有理射の延長。** 滑らかで幾何学的に整なK-scheme X、点x∈X(K)、有限対角を持つ有限表示stack Y、稠密開U上の射fを考える。ある体拡大κ/K後に、x_κを含む近傍でf_κと一般点で同型な射gが存在すれば、fはxの開近傍へ延長する（`lem:nfm-finite-diagonal-rational-extension`）。証明ではgと指定同型をsmoothな有限型K代数Bへ降ろす。得たV⊂X_Bからその開像Wへのsmooth coverの二重・三重積はsmoothである。有限Isomの指定された有理切断は、係数が正規環上整であることから一意に延長し、cocycleも稠密開から延びる。これをfppf降下する。特殊点の慣性が自明である必要はない。

本研究への適用で重要な点は以下である。

- Y=[Pdec/μ₂]は有限対角を持つ。Benoistの偏極付き滑らかな三次の分離性・DM性を用い、tensorまたはその負を保つ条件を有限Isomの閉条件として課す（`lem:nfm-poisson-target-finite-diagonal`）。偏極線束を自明化したG_m-gerbeとは区別する。
- XはK=C(p,q,h)上の混合係数のaffine空間とする。κ=C(p,q)((h))上の三角式T_hは実際の有限多項式なので、有限表示のPoisson対の射を与える。対称点x_σではW_hat=F_σ+O(h)、F_σは滑らかであり、この点を定義開に含む。
- genericな射との同型は既存の次数18の証明で得られる。慣性自明なgeneric開で一意なためC₃同変であり、有限Isomによる延長後にも同変性が保たれる。従ってK上の延長されたactive曲線C'_σに非零の有理三捩れ平行移動が作用する。
- 点曲線E_σはHesse曲線で全三捩れがK有理である。jの一致とC'_σの非零有理三捩れ点により、Jacobianの非自明な二次twistを排除する。正規近傍上のJacobian-Isomと定数torsorχ_act|Kのgeneric同型を延長し、x_σで制限するとχ_act|K=0となる。
- P=hp、Q=hqと置くとK=C(P,Q,h)。純超越拡大とHesse体への二次類の単射性から、χ_act=0を得る（`thm:nfm-active-sign-vanishing`）。形式体κでの平方根だけから戻す議論ではない。

二つのfull liftのうち、支配的h族でτ_res=h(F+G)⊗P₀+O(h²)を持つものは一意である。これが全O-同値に自然な半古典規格化Ψ_res^scで、反対作用に対して符号を変え、適切な開でfinite étale階数9となる（`cor:nfm-semiclassical-full-residual`）。符号商射の階数18は保持され、χ_op=χ_sgnとなる。

**証明が与える延長の範囲。** 延長されたPoisson対のC'_σと、独立に低rotation積から作ったC_σが同じgenus-one torsorであることは使わない。圏の対角のperfect性・低Natの底変更をこの閉族の近傍へ延ばす問題や、そこでのfull比較核の延長は残るが、符号消滅の前提ではない。一般点のfinite-cell模型を開へ広げることだけでは、この閉族を通る開は得られない。この障害は有限対角を使う今回の方法と区別して保持する。

### active 制限の最高次線束型と三捩れ評価

良い一ブロック表示と固定した full section-window・Galinat window1 を用いる。source の包含を j_nc:K_nc→Perf(C_nc)、可換側の active 曲線の包含を i_C:C_res→Y=X_res とすると、原点 stabilization と active 制限は

\[
 \kappa_{\rm nc}\simeq j_{\rm nc}^{!}\mathcal O[1],\qquad
 q_Y\simeq Li_C^*|_{\operatorname{Ku}(Y)}
\]

と表示できる。したがって full equivalence kernel P に対して

\[
 R_P=q_Y\Phi_P(\kappa_{\rm nc}),\qquad
 H^i(R_P)=0\ (i>-1),\qquad
 H^{-1}(R_P)\text{ は次数零の線束}
\]

となる型を考える。この型は一般点の有限分離拡大上で非空であり、従来の CF mixed Euler 条件も同時に課せる（`prop:nfm-kernel-active-line-nonempty`）。Euler 数だけを指定する型より強い条件であり、その全ての核が最高次線束条件を満たすとは主張しない。型の非空性と、元の底で full kernel の同型類を整合的に選ぶことも区別する。

非空性の第一の入力は、次数一の中心正則列 U に対する graded purity である。connected 非負次数代数 A と A′=A/(U) に対して

\[
 K\otimes_A^{\mathbf L}A'
 \simeq\bigoplus_{j=0}^{r}K(-j)[j]^{\binom rj}
\]

が graded A′-module として非正準に分裂する。Koszul Tor の純粋内部次数だけでなく、minimal resolution の次数から Ext^{q+1}_gr(K,K(−q))=0 を示し、Postnikov の attaching class を消す（`lem:nfm-linear-center-purity`）。MF 側では PBW による Sym(U)-flatness と active 中心三次の regularity によって ambient square が Tor-independent となり、実際の係数商がこの導来制限に対応する（`prop:nfm-mf-linear-restriction`）。圏全体の categorical derived tensor との同定を仮定していない。

**中心列の次数一という仮定は必要である。** A=K[x]、u=x²、A′=K[x]/(x²) の場合、K⊗_A^L A′ は二項自由複体 [A′(−1)→A′]、写像は x であり perfect である。その cohomology の直和 K⊕K(−2)[1] は D_sg(A′) で非零なので、両者は導来圏で同型でない。Koszul differential が K と tensor して零になることだけから、商代数上の formality を推論してはいけない。

第二の入力は window と負 rotation の計算である。L=O_C(1)、deg L=3 とし、Galinat の Φ₁ の規約で

\[
 \kappa_{\rm act}\leftrightarrow O_C[1],\qquad
 \rho=T_{O_C}\circ(-\otimes L),\qquad \rho^3\simeq[2]
\]

を同時に用いる。次数零線束 M に対して ρ⁻¹M=M⊗L⁻¹、ρ⁻²M=B_M[−1] であり、B_M は階数2・次数−3の束である。従って ⊕_j ρ^(−j)M[j+1]^{⊕binom(r,j)} の j=3a,3a+1,3a+2 の項は順に M[a+1]、(M⊗L⁻¹)[a+2]、B_M[a+2] となり、j=0 だけが H⁻¹ に寄与する（`lem:nfm-active-line-rotation`）。この sheaf 計算は体上で用いる。M が O_C を通過する Picard 族に、非正準な分解を一律に貼り合わせたとはしない。BFK と Galinat の異なる window の剰余体 shift を混用しない。

完備 CF 比較の active 部分は h=0 で剰余体を O_C[1] へ送る。その像は滑らかな proper 曲線族上の perfect 複体なので、閉ファイバーから線束の shift M_R[1] となる。体上へ移った後、完備中心切断・graded purity・上の rotation 計算を合成すると R_P の最高次線束条件を得る。核・逆核・単位・余単位・rotation・周期を有限生成係数環へ降ろし、R_P の cohomology を平坦化して線束性を広げ、閉点へ特殊化することで有限分離拡大上に同じ型を実現する。元の特定の形式核そのものが有限体拡大へ降りたという主張ではない。証明の詳細は `prop:nfm-kernel-active-line-nonempty` に置く。

この型で **full kernel の同型類が整合的に選ばれた後**、その実現を G_m-gerbe G→S、普遍核を P とする。底変更に両立する cohomology stratum 上で M=H⁻¹(R_P) は C_G 上の正準的な重み1線束である。π:C_G→G とすると

\[
 V=\pi_*(M\otimes L)
\]

は重み1・階数3の束となる。実際、各幾何ファイバーで次数3の線束の H¹ は零、H⁰ の次元は3である。det V の重みから 3α=0、End(V) の降下から次数3の Azumaya 代数を得るので、体上では ind(α)|3 まで従う（`thm:nfm-kernel-active-line-bound`）。period と index は別の根拠で評価している。対応する Brauer–Severi 平面の tautological twist は full 比較核を与える。

さらに M 自体が C_G 上の重み1線束なので **α|_C=0** である。C_G へ引き戻した普遍核 P に M⁻¹ を tensor すれば重み零となり、C 上の比較核へ降下する。従って C(K)≠∅ なら既に α_K=0。split 平面内の一般の K-直線との横断切片は次数3の有限 étale K-代数であり、その上でも比較核が存在する（`cor:nfm-kernel-active-curve-splitting`）。この具体的な分裂被覆と次数3 Azumaya は同じ最高次線束から得る。どちらも full class の第一段階の選択を前提とする。

最高次線束の相対 Picard 類は m_P:S→Jac(C/S) へ降下する。M が定める G→Pic⁰_stack(C/S) は scalar band 上で恒等なので、G≃m_P^*Pic⁰_stack(C/S)、従って **α=m_P^*β_(Pic,C)** となる（`cor:nfm-kernel-picard-obstruction`）。これは選択済み full class の scalar 障害を、次数零 Picard 類の実際の線束による表現障害へ具体化する。m_P が C 上の線束で表せれば核 gerbe は中立、とくに m_P=0 なら C(K)≠∅ を仮定せず中立である。下では三分点被覆による相対的な中立化と、固定入力から証明した相対windowを用いてm_Pを点の平行移動と同定する型を記す。表示変更則は下記の全O-降下で決まるが、一般の refined 核の m_P の値は未決定であり、β_(Pic,C) と表示 gerbe の β を同一視しない。

非分裂表示では、表示 gerbe β の次数1または3の分裂拡大後にこの型が成立すると仮定する。このとき

\[
 \operatorname{ind}(\alpha_K)\mid3^{1+\epsilon_n},
 \qquad \epsilon_n=\mathbf1_{n\equiv1\ (3)}
\]

となり、n≢1 mod3 では3、n≡1 mod3 では9を得る（`cor:nfm-kernel-active-line-unsplit`）。表示の分裂条件・実際の O_C(1) と、核 gerbe の中立性は異なる。αとβの同一視や元の Euler 型の全核への適用は行わない。型自体は下記の共通稠密開へ降下するが、非分裂表示の任意の体で exact index 三となるとは主張しない。n≥5のfull class選択と任意核への適用は別に残る。この評価には代数的な active 同値核の assignment や coherent な中心線型性は不要である。

### 原点対象・active 制限の内在的表示と点型の全 O-降下

a=n−1、full section-window の整数 i=1−a、active window1を固定する。入力Bの `tw:eq:triangular` から κ_nc≃ρ_nc^(−a)p_nc(O(a))[1] を得る。相対Serre式に同じ基底線束Dを保持して S_K=ρ_nc^(−a)[n]⊗D、S_D=(−a)[n]⊗D と書くと、j_nc^!=S_Kp_ncS_D^(−1) でDが相殺し、κ_nc≃j_nc^!O[1]となる。全O-同値の持上げ線束を A′_j=A_j⊗M^j の向きに取ると、F O(a)=O′(a)⊗M^(−a)、Fρ_nc=ρ′_ncF⊗M⁻¹なので、κの線束重みも相殺する。次数スカラーはaugmentationの次数零に恒等として作用する。

可換側のq_Yは、単にMFの式を形式的に商する記号ではなく、実際の導来制限 Li_C^*|Ku(Y) と一致する。F∈Ku(Y)ならRΓ(F(t))=0が1−a≤t≤0で成立するので、fullのRΓ_(≥1−a)FはRΓ_(≥1)Fと等しい。a本の中心一次式によるKoszul複体で、RΓ_(≥1)F⊗^L_(A_Y)A_C→RΓ_(≥1)(Li_C^*F)を比較する。j項の次数m≥1で切断により欠ける可能性があるのは1−a≤m−j≤0だけで、全て上の消滅に含まれる。正準のA_C-linear比較が準同型となり、active window1の逆を通じて結論する。この証明は標的の可換側に限定され、非可換sourceからactual active同値核を取り出すassignmentを構成しない。

従って最高次線束は

\[
 M_P=H^0\!\left(Li_C^*\Phi_P(j_{\rm nc}^{!}\mathcal O)\right)
\]

と書ける。表示変更が誘導する曲線同型f_Cに対しR_{P′}≃f_{C,*}R_P、m_{P′}=Jac(f_C)(m_P)となる。Pを底線束NでtensorしてもM_PがNだけ捩じれるだけで、相対Picard類は変わらない。これにp_resの自然性を合わせ、最高次線束条件とm_P=p_resは、良い一ブロックO-marked stackの共通な稠密開において全O-保存同値・任意底変更へ降下する。Brauer–Severi ambientを許し、大域O_C(1)の選択は不要である。

証明は `lem:nfm-origin-object-weight-zero`, `prop:nfm-active-restriction-geometric`, `cor:nfm-point-type-O-descent`。内在的複体は `eq:nfm-point-type-intrinsic-complex` のQ_P=Li_C^*j_YΦ_Pj_nc^!Oであり、R_P=Q_P[1]。非正則試験底では一般の特異圏の底変更定理を新たに仮定せず、正則atlas上で得たperfect対象・bimoduleを導来pullbackする。R_P∈D^(≤−1)とH⁻¹(R_P)の線束性から、この最高次cohomologyは任意底変更に両立する。表示の次数スカラーが重み零であることと、核自身のscalarが最高次線束に重み一で作用することは区別する。二つのwindowは既存の行列定義との同定に使い、右随伴と閉埋込みによる表示には追加標識として残さない。別windowの計算式への無調整の置換、全intrinsic成分、任意formality間の独立性、coherent中心線型性は結論しない。

さらに非分裂Brauer–Severi平面内のC/Kでも、幾何的O_C(1)のGalois不変類がPic³(C)(K)の点を与え、3[C]=0∈H¹(K,J_C)となる。この偏極類を実際の線束とは仮定しない。最高次線束型の選択済みfull classのα=δ_C(m_P)=⟨[C],m_P⟩にTate pairingの双線型性を適用すれば3α=0となる（`cor:nfm-unsplit-point-scalar-period-three`）。点型はm_P=p_resという特例である。従って非分裂体でもperiodは三を割り、既存index上界はn≢1 mod3で三、n≡1 mod3で九のままである。後述の theta twist により index 九は実際に達成されるが、個々の非分裂体での exact index を一律に三または九とはしない。

### Picard 三分点被覆と scalar 障害の三を法とする記述

滑らかな proper genus-one 族 π:C→S と実際の次数3線束 L を固定し、J=Pic⁰(C/S) とする。Picard gerbe 上の普遍線束 M に対して

\[
 M^{\otimes3}\otimes\pi^*\left(
    \det\pi_*(M\otimes L)^{-1}\otimes\det\pi_*L\right)
\]

の scalar 重みは 3−3=0 であり、C×_S J 上の線束 N_L へ降下する。これは相対類 [3]:J→J を表し、零切断で O_C に規格化され、底変更・対 (C,L) の同型・底からの線束による L の twist に両立する（`lem:nfm-picard-tripling-line`）。正準性はこの determinant 構成に関するものであり、三倍の相対類と零切断の規格化だけで任意の線束を一意に特徴付けるという意味ではない。

**full class を選んだ後**、T_P^(3)=S×_(m_P,J,[3])J は階数9の有限 étale J[3]-torsor である。普遍三分点 q に対し N_q=(1_C×q)^*N_L は m_P の実際の代表となる。gerbe の同値 G≃m_P^*Pic⁰_stack(C/S) により、最高次線束を N_q と同定した full 比較核は T_P^(3) 上に一意な同型を除いて一意に存在する（`thm:nfm-kernel-tripling-cover`）。これは任意の直線切片を選ばずに相対的に定まる scalar 分裂被覆である。体上の index|3 を改善する結果でも、第一段階の class 選択でもない。平面同型の九重被覆 I→D、および Poisson 射の次数とも区別する。

Picard の tensor 積と上の三倍線束から、表現障害は群準同型

\[
 \delta_C:J(S)/3J(S)\longrightarrow H^2(S,\mathbf G_m)[3],
 \qquad \alpha=\delta_C([m_P])
\]

を誘導する（`cor:nfm-kernel-picard-mod-three`）。m_P=3q となる q∈J(S) があれば、q 自身を線束で表す必要も C の切断を持つ必要もなく、規格化された full 核を S 上に得る。一般の refined 型の m_P の三可除性はここからは決まらない。ただし点型の一般 split 係数体では m_P=p_res は三で割れない（`cor:nfm-generic-point-picard-index-three`）。この型を三可除性だけで元の係数体上に中立化する経路は使えない。一般 split 係数体ではさらに I_sc の分裂から δ_C(p_res) の非零性も決まり、選択済み scalar 段階の最小分裂次数は三である。

### 一般三分点被覆の九次性と ASL₂(F₃) monodromy

全n≥3の標準split一般係数体k_nでは、T_pt^(3)=[3]⁻¹(p_pt)は連結な有限étale被覆、従って九次体L₉のspectrumである。任意の三分点定義体L/k_nは9∣[L:k_n]を満たし、最小値は九である。九点上のGalois置換群は

\[
 \operatorname{ASL}_2(\mathbf F_3)
 =\mathbf F_3^2\rtimes\operatorname{SL}_2(\mathbf F_3),
 \qquad |\operatorname{ASL}_2(\mathbf F_3)|=9\cdot24=216.
\]

したがってL₉のGalois閉包は216次である。作用が二重推移的なので一点安定化群は極大となり、L₉には真の中間体がない。またL₉/k_n自体は非Galoisで、一つの三分点を含む最小Galois拡大の次数も216となる。θ_scは三倍写像と可換するため、残余側の[3]⁻¹(p_res)にも同じ結論が成立する（`thm:nfm-generic-point-third-division-monodromy`）。

証明には二つの独立した入力を用いる。まず、普遍Hesse曲線E_μの**真の一般点**p=(A:B:C)を取ると、F=C(μ)(E_μ)=C(P,Q)、P=−2C/(A−B)、Q=−2(A+B)/(A−B)となる。[3]⁻¹(p)は[3]:E_μ→E_μの一般ファイバーそのもので、定数E_μ[3]によるGalois九重被覆である。一般GL₃基底変換と混合・中心係数を純超越的に加えた族は表示係数空間を支配するので、元の一般三分点被覆も連結であり、そのGalois像は全translation部分群F₃²を含む（`lem:nfm-generic-hesse-third-division`）。非零Picard障害を保つ別の族p₀+3qを、この連結性の証明には流用しない。

線型部分は、Hesse不変量体上の二十四次Galois拡大から求める。E₀:y²=x³−27sx+54t上の明示三捩れ点T=(−9q²,12(1+2ζ)(p³+q³))の軌道は非零三捩れ八点全体で、安定化群C₃のnormal coreは自明である。これにより完全三捩れ体の群がSL₂(F₃)と決まる。一般三次の不変量体拡大の正則性を使ってこの群を保ち、さらにH_g=H_(J_g)という同じ有限群schemeをμ₃で割ることで、点曲線V(J_g)のJacobianの三捩れへ移す（`lem:nfm-generic-active-three-torsion-monodromy`）。次数九のHessian写像に沿ってGalois群が不変と仮定する議論ではない。

ここで九は**点を三で割る**最小次数であり、δ_C(p_res)を消す最小scalar次数三とは異なる。三次scalar分裂体上ではp_resは依然として三で割れず、L₉も三次の中間体を持たない。選択済み点型full classにはL₉上の標準規格化核があるが、任意のfull核が三分点を選ぶわけではない。全比較体の九整除性や、n≥5のfirst-stage class選択が九次で済むことは結論しない。

### 指定中心商の相対 THCR/window1 と点 shift による線束類

右 THCR 規約の符号が重要である。楕円曲線 E、次数3線束 L、点 shift σ=t_p に対し、qgr の内部 shift は s=σ_*∘(−⊗L) である。U_(a,b)=t_a^*∘(−⊗P_b)、P_b=O_E(b−0)、ρ=T_O∘(−⊗L) とすると

\[
 \operatorname{Ad}_\rho(a,b)=(-2a-b,3a+b),\qquad
 \rho_{\rm nc}=t_{-p}^*\rho,
\]

\[
 U_{a,b}\rho_{\rm nc}U_{a,b}^{-1}\simeq\rho
 \quad\Longleftrightarrow\quad 3a=0,\ b=p.
\]

この部分群内で ρ を保つ自己同値は U_(a,0)、a∈E[3] であり、次数零 Picard 類を変えない（`lem:nfm-elliptic-rotation-conjugacy`）。右 THCR の s を σ^* と取り違えると平行移動の符号が逆になる。適用可能な Gorenstein parameter a=0 の window1 では κ↔O_E[1]、内部 shift↔T_O∘s である。Γ_(≥1) と Γ_(≥0) の切断三角形による証明は可換性を使わない（`lem:nfm-twisted-elliptic-window`）。

同じ相対曲線・偏極上で、恒等核から変形する perfect Fourier–Mukai 比較が二つの rotation を intertwine すると仮定する。graph-support の議論で比較は原点を局所に選んだ U_(a,b) の形となり、3a=0 と閉ファイバー a=0 から a=0、最高次線束の相対類は p となる（`lem:nfm-formal-elliptic-point-line`）。閉ファイバーで線束が O_E になることだけから、変形全体で O_E とは結論しない。

full 比較に必要な **source active 商の相対 THCR/window1 比較**は、支配的な完備族 R=k[[h]] 上で固定入力から導ける。比較は閉／一般ファイバーへの導来底変更に両立し、κ・内部 shift は上の式に対応し、閉ファイバーでは可換側と同じ window1 となる。証明は `prop:nfm-relative-active-thcr`、`lem:nfm-active-dvr-gorenstein`、`prop:nfm-relative-active-window-basechange`。この比較は任意の非正則底への特異圏の一般的な底変更定理ではない。

半古典規格化のJacobian同型θ_scを固定し、I_sc=I×_(D,θ_sc)Sと置く。これは階数九のfinite étale J_E[3]-torsorである。固定入力Bと良い一ブロックの仮定の下で、平面同型φ∈I_scと

\[
 m_P=\theta_{\rm sc}(p_{\rm pt})=:p_{\rm res},\qquad\operatorname{Jac}(\phi)=\theta_{\rm sc}
\]

を同時に備える full 核の追加型は、少なくとも一つの支配的な有限 étale 被覆上で非空である。元の最高次線束条件と三つの Euler 条件も満たす（`prop:nfm-kernel-point-line-nonempty`）。形式比較のφは正確な尺度(h/b_h)W_h⊗P₀を与え、その先頭項がθ_scの符号を選ぶ。有限生成係数環Dへ降ろす対象はfull核・逆核・単位／余単位・rotation／周期・I_scへの点φとPicard等式であり、符号の一致も保つ。形式比較での等式を体の忠実平坦拡大から Frac(D) へ戻し、分離な相対 Jacobian の等式として開へ広げてから閉点を取る。代数的 active 同値核の assignment を仮定せずに非空性を得るが、全ての refined 核や全ての φ にこの等式を主張しない。

この型の full class と Jacobian 同定を選んだ後には、α=δ_C(p_res) となる（`cor:nfm-kernel-point-picard-obstruction`）。実際の線束による p_res の代表、または p_res∈3J(S) は scalar 中立性の十分条件であり、常にその三分点被覆上で上記の規格化核を得る。ただし一般 split 係数体では三可除性だけでなく実線束の存在も、I_sc の分裂と残余側の exact index 三によって否定される。点 shift が非自明なら p_res≠0 なので、この型で m_P=0 を無条件の目標にするのは適切でない。これは active window の共役式から得た線束類の記述であって、full Ku rotation 自体を点の平行移動と同一視する主張ではない。定常点成分の圏的特徴付けも別に残る。

**相対比較の証明で保持する要点。** 詳細は上記の三結果を参照する。

1. 点関係行列 M_h(u)=[u]_×−h Hess(g)(u)/2 の determinant は −3hJ_g。滑らかな E_R=V(J_g) 上で rank 二であり、kernel が point graph σ を与える。σ₀=id、一般ファイバーに固定点がなく、三捩れの有限 étale 性から σ_K³≠id となる。
2. 指定中心三次 ω の THCR 像が非零なら、次数一切断との可換性から σ_K³ が全切断比を固定し、恒等になる。従って像は零。この論点により、任意の中心三次を説明なしに既知の標準中心生成元と同一視せずに済む。両辺の次数 m≥1 は自由階数3mであり、閉ファイバーの同型から次数別Nakayamaを適用する。
3. coherent 層の二つの h-完全列と曲線の cohomological dimension 一を用い、H¹消滅と大域生成を閉ファイバーから持ち上げる。Keelerのample-pair条件を満たし、右加群の qgr≃coh を得る。
4. pinned B の次数別Koszul持上げにより、左右noetherian、gldim D_R≤4、A_R=D_R/(ω)の有限injective dimensionとRHom_A(R,A)=R[−2]を確認する。Burke–StevensonのDefinition5.1ではinjective dimensionとこのshiftが一致する必要はなく、parameter零の定理を適用できる。
5. RΓ_(≥1)は有界有限生成で、各内部次数にproper perfect base changeを適用する。無限個の内部次数を切り捨てず、R→k,KのTor幅≤1を使って実際の導来係数変更をdg商へ降ろす。MF余核の次数別自由性と有限totalizationを確認し、曲線側のO(m)の厚生成・Hom底変更からMorita底変更を得る。

### 全 active Fourier–Mukai intertwiner と相対 gerbe

標数零の体 K 上の genus-one 曲線 E,C と実際の次数三線束 L_E,L_C を取る。K-有理原点は仮定しない。p∈Jac(E)(K) と右 shift に対し、ρ_(E,p)=T_O∘(t_p)_*∘(−⊗L_E)、ρ_C=T_O∘(−⊗L_C) とする。ここで扱うのは実際の perfect kernel で与えられる K-線型 Fourier–Mukai 同値である。

rank・degree 格子上の rotation は R=((−2,−1),(3,1))、SL₂(Z) 内の centralizer は正確に {±I,±R,±R²}。可換行列の形と determinant を解くと c=−3b、d=a−3b、a²−3ab+3b²=1 となり、平方完成で |b|≤1 が従う。数値恒等の同値は (−⊗M)φ_*[2a] で、φ:E→C は実際の曲線同型、M は実際の次数零線束である。幾何ファイバーの長さ一の point object と flat な kernel の support から graph を回復し、support と線束を降下する（`lem:nfm-elliptic-numerical-graph`）。

F(O_E) が shift のない次数零線束となる規格化では、q=Jac(φ)(p)、d=[φ_*L_E⊗L_C⁻¹]、m=[M] と置くと

\[
 F\rho_{E,p}F^{-1}=U_{m-q-d,d}\rho_C.
\]

従って intertwining は **φ が偏極を保つことと m=q** に同値である（`thm:nfm-elliptic-normalized-intertwiners`）。偏極を保たない φ の誤差を M で補うことはできない。任意の数値型も ρ_C と shift の合成でこの形へ規格化できるため、全 Fourier–Mukai 同値について

\[
 \exists F:\ F\rho_{E,p}\simeq\rho_CF
 \quad\Longleftrightarrow\quad
 \operatorname{Isom}_K((E,L_E),(C,L_C))\ne\varnothing
 \ \text{かつ}\ \delta_E(p)=0
\]

を得る（`cor:nfm-elliptic-any-intertwiner-criterion`）。同じ偏極曲線上の全 centralizer は同型類の群として Aut_K(E,L)×Z で、Z の生成元は ε=ρ⁻¹[1]、ε²=ρ、ε³=[1]。O_E を shift なしで保ち Jacobian 作用が恒等となる部分は J[3] である（`cor:nfm-elliptic-full-centralizer`）。これは active 導来圏の分類であり、full Ku の全自己同値や full 核の同型類選択にはそのまま適用しない。

noetherian Q-scheme S 上で Jacobian 同型 θ を固定すると、規格化した active 核で intertwining が局所的に存在するものの stack は

\[
 \mathfrak A_\theta\simeq I_\theta\times_S\mathcal{Pic}^{\,\theta p}_{C/S}.
\]

従って同型類の fppf 層は階数九の I_θ、各 class の実現障害は δ_C(θp) の gerbe である（`prop:nfm-elliptic-intertwiner-gerbe`）。非被約 S も含む。graph 化には第一射影に関する derived fibre が長さ一の層であることからの平坦性判定を用い、d=0、m=θp は相対 Poincaré 線束と共役式から**切断の等式**として得る。幾何点での等式だけで非被約底上の等式を結論しない。

この stack では rotation 同型 η 自身は標識していない。η と指定三次周期を標識すると、その Hom 線束 V の三重合成が V³≃O を与え、周期に適合する η は μ₃-torsor をなす。核の scalar 自己同型は η に自明に作用するので G_m inertia は残り、V は weight zero として I_θ へ降下する。構造付き class 層は階数三の被覆 \(\widetilde I_\theta\to I_\theta\)、その gerbe は上の Picard gerbe の引戻しである（`rem:nfm-elliptic-period-phase`）。現行構成でこの位相被覆が自明・非自明のいずれかはまだ決めていない。

### 点関係行列が与える三倍線束と形式三分点

点関係行列 M:O_E(−1)³→O_E³ は scheme-theoretic に det M=0 を満たし、その二次小行列式が単位イデアルを生成するとする。この一定 rank 二の条件は、非被約底での点ごとの rank 条件より強い。右 kernel が σ=t_p の graph を与えるとき、L=O_E(1)、Q=coker M と置くと

\[
 \ker M=L^{-1}\otimes\sigma^*L^{-1},\qquad
 Q=L^2\otimes(\sigma^*L)^{-1},\qquad
 [Q\otimes L^{-1}]=3p.
\]

余核 Q は次数三であり、次数零化した線束の類は p ではなく **3p** となる（`prop:nfm-point-matrix-tripling-line`）。座標の determinant に由来する底線束は相対 Picard 類を変えない。この行列から p の線束代表や δ_E(p)=0 を結論する近道は使えない。

一方、完備半古典族 R=k[[h]] では p₀=0 である。[3]⁻¹(p) は有限 étale、閉ファイバーの零点は Hensel 性により一意に q∈J(R) へ持ち上がり、3q=p、q₀=0 を満たす。三倍線束の構成から δ_(E_R)(p)=0、従って Laurent 体でも零となる（`lem:nfm-formal-point-third-division`）。これは完備化前の係数体の障害が零であることを意味しない。一般係数体の非零類と形式 CF 比較の存在が両立する理由である。

### flex・平面同型・三分点の cup product

C/K と実際の次数三線束 L に対し、flex torsor F_L={x:[O_C(3x)]=[L]} の類を ξ_L∈H¹(K,J[3]) とする。これは曲線 torsor [C]∈H¹(K,J) の lift である。p∈J(K) の三分点 torsor の Kummer 類を κ₃(p) とすると、Ciperiani–Krashen Theorem3.7 の順序・符号規約で

\[
 \delta_C(p)=e_{3,*}\bigl(\xi_L\smile\kappa_3(p)\bigr)\in\operatorname{Br}(K)[3]
\]

となる（`prop:nfm-kernel-flex-cup`）。第一因子が曲線、第二因子が点である。有限 Galois 拡大で flex x₀、3q=p、J[3] を分裂させ、c_γ=γx₀−x₀、d_γ=γq−q と置けば、cocycle は e₃(c_γ,γd_η)。有限 crossed product として計算できるが、その表示次数 |G| を Brauer index と同一視しない。選択済み点型 full class には p=p_res を代入する。

偏極曲線 (E,L_E),(C,L_C) と θ:Jac(E)≃Jac(C) を固定する。I_θ の右作用を φ⋅a=φ∘t_a とし ι_θ=[I_θ] と書くと

\[
 \xi_{L_C}=\theta_*(\xi_{L_E}+\iota_\theta),\qquad
 \delta_C(\theta p)=\delta_E(p)+e_{3,*}\bigl(\iota_\theta\smile\kappa_3(p)\bigr)
\]

である（`prop:nfm-picard-plane-transfer`）。実際の φ があれば cup 項は零になるが、δ_E(p) 自体が消えるとは限らない。flex・平面同型・三分点は全て階数九の torsor だが、その class と役割は異なる。特に θ_sc の存在だけで二曲線の Picard gerbe を同一視しない。

### 補正が見る商と、形式比較だけでは決まらない降下

任意の b,p∈J(K) に対して e₃,*(κ₃(b)∪κ₃(p))=0 である。J 自身に L₀=O_J(3O)、L_b=L₀⊗O_J(b−O) を置くと、恒等 Jacobian 同型を誘導する平面同型 torsor は [3]⁻¹(b) となる。二つの曲線自体は同じ J なので transfer 式の左辺は零であり、等式が従う。従って補正は H¹(K,J[3])/κ₃J(K)=H¹(K,J)[3] を通り、θ⁻¹_*[C]−[E] のみを見る（`lem:nfm-picard-torsor-quotient`）。偏極を指定しない曲線同型で既に補正は零となり、単なる偏極のずれでは非零点障害を相殺できない。これは既知の Tate pairing の性質の必要な形である。

形式同型だけでこの差を決めることはできない。E:X³−aY³−bZ³+λXYZ に対し C_d:X³−adY³−bd²Z³+λdXYZ を取ると、s³=d 上の φ_s=[X:s⁻¹Y:s⁻²Z] は τφ_s=φ_sσ⁻¹ を満たし、その Jacobian 同型 θ_d は元の体へ降下する。σの三捩れ移動点 p₀ に対する補正は

\[
 \delta_{C_d}(\theta_dp_0)-\delta_E(p_0)
       =(d,ab+\lambda^3/27)_3.
\]

d=1+h なら φ_s≡id の形式同型があるが、d を独立変数とした元の体ではこの symbol は非零である。d=a⁻¹ では C_d に有理 flex [1:1:0] があり、補正は点障害を完全に相殺する。一般 Jacobian 点 q を使えば無限位数・点障害の exact index 三を保ち、相対 Jacobian の原点近傍で a−1=zh、局所パラメータ u(q)=h として q≡0 と φ≡id も同時に実現できる（`prop:nfm-cyclic-plane-twist`と直後の注意）。この C_d を actual residual 曲線と同定した例ではなく、H_g 作用を含む追加の降下データを使う必要性を示す。

**有理な三捩れ全作用だけでも不十分。** K=C(t)、E:X³+Y³+Z³−6XYZ=0、C:X³+tY³+t²Z³−6tXYZ=0 とする。P(X,Y,Z)=(tZ,X,Y)、Q=diag(1,ζ,ζ²) は PGL₃(K) 内で可換な位数三の作用を与え、F(P)=tF、det P=t、F(Q)=F、det Q=1 なので proper な全 T₉ 作用を持つ。しかし C(C((t)))=∅。三つの立方項の付値は異なる mod3 を持つため最小値が一意で、XYZ項の付値はその平均となり最小値より大きいからである。従って C と有理点を持つ E の平面同型 torsor は非自明である。P³=tI という lift の差は、full ambient X⊕1^r 上の標準 H_g 作用とは両立しない。三次元の projective 作用と、中心 summand を含む labelled H_g 作用を分けることが次の分裂証明の要点となる。

有限次数 d の被覆上で得た top line の norm は dp の代表を与えるだけである。既に三捩れの障害に対して、次数九や三の倍数の被覆から norm・determinant を取るだけでは weight one の線束を作れない。指定した generic section の有限 étale rigidity と、形式的な section から元の体の section を作ることも別である。

### 一般 j の巡回障害と実 Sklyanin 代数への降下

K=C(a,b,λ)、C:X³−aY³−bZ³+λXYZ=0 とし、σ=[X:ζY:ζ²Z] の非零三捩れ移動点を p₀ とする。b_λ=b+λ³/(27a)、K'=K(t)、t³=a、τ(t)=ζt と置くと

\[
 \delta_C(p_0)=[(K'/K,\tau,b_\lambda)],\qquad
 \operatorname{per}\delta_C(p_0)=\operatorname{ind}\delta_C(p_0)=3.
\]

j=27r(r+8)³/(r−1)³、r=−λ³/(27ab) は非定数で、この族は j=0,1728 に限定されない。接線の比 f=(X−tY+λZ/(3t))/Z の norm が b_λ となる cocycle を本文で計算し、b_λ-進付値により非 norm 性を示す（`prop:nfm-picard-cubic-index-sharp`）。λ=0 では対角三次と norm b の例を回復する。

F=K(J_C)、一般点 q に対し p=p₀+3q は無限位数で、δ_C(p)=δ_C(p₀)_F は非零のままである（`cor:nfm-picard-infinite-translation`）。定数 Brauer 類が消えたとすると、Brauer–Severi 曲面への有理写像を滑らかな曲線 J_C の K-有理原点で延長して矛盾する。この p の平行移動は L を保たない。

この例は実際の active 代数に実現できる。一般に、実際の次数三線束 L と 2p≠0、3p≠0 を持つ E/F に対し、V=H⁰(E,L)、R=ker(V⊗V→H⁰(E,L⊗σ*L)) から幾何的 Sklyanin 代数 T(V)/(R) を元の F 上で作る。p 自体の線束代表や E(F) は不要である。三次 syzygy 線 (V⊗R)∩(R⊗V) と cyclic 条件を降下すると、交代成分が非零の cyclic potential が F 上に存在し、commutator–gradient 形式 D_g に規格化できる（`prop:nfm-active-point-sklyanin-realization`）。

幾何的 Hesse 座標で E:X³+Y³+Z³−3μXYZ=0、p=(A:B:C) とすると、滑らかな potential は

\[
 g=-\frac{2C}{3(A-B)}(X^3+Y^3+Z^3)-\frac{2(A+B)}{A-B}XYZ.
\]

その点三次は J_g=g+det(Hess(g))/24 で、

\[
 J_g=\frac{8}{3(A-B)^3}\{ABC(X^3+Y^3+Z^3)-(A^3+B^3+C^3)XYZ\}
\]

となり、元の E と shift p を回復する。potential の滑らかさは μ³≠1 と Hesse 上の点条件から従う。既知の Sklyanin 正則性・cyclic potential 理論を用い、Koszul resolution と双対性を降下して AS-regular・3-Calabi–Yau 性を得る。一般論を新しく証明したとは扱わず、ここでの算術的降下・規格化・障害を保持した実現を分ける。

### 一般 split 係数点の exact index と full 比較への限界

上の無限位数点を用いる実現族は、全 n≥3 の良い split 一ブロック表示空間へ支配的に広げられる（`prop:nfm-active-point-obstruction-dominant`）。Hesse potential の係数 P=−2C/(A−B)、Q=−2(A+B)/(A−B) は有理逆 (A:B:C)=(2−Q:−2−Q:−2P) を持つ。根号を加えた Hesse 座標は支配性の検査だけに使い、非零 Brauer 類の保持をその有限拡大へ依存させない。実際の族には一般の GL₃ 基底変換、混合係数、中心三次 torsor の自由係数を**純超越拡大**で加える。非純中心商の一次元空間の lift は線型代数で選び、追加の代数拡大を要しない。division algebra の純超越拡大は index を保つ。

従って一般 split 係数体 k_n 上で

\[
 \operatorname{per}\delta_{E_{\rm pt}}(p_{\rm pt})
 =\operatorname{ind}\delta_{E_{\rm pt}}(p_{\rm pt})=3,\qquad
 p_{\rm res}\notin3J_{C_{\rm res}}(k_n)
\]

となる（`cor:nfm-generic-point-picard-index-three`）。p_pt も三で割れない。標準三分点torsorの連結性と最小定義次数九は、上記の真の一般Hesse点による別の支配族から証明する。全 FM 判定により、実際の次数三線束を持つ任意の標的曲線への active rotation intertwiner は k_n 上でも三に素な有限拡大後でも存在しない（`cor:nfm-generic-active-intertwiner-obstruction`）。これは係数体上の主張であり、個々の複素曲線に非零 Brauer 類を主張するものではない。

### 一般係数体での平面同型 torsor の分裂

標準 split 一ブロック係数体 k_n について I_sc(k_n)≠∅ を得た（`thm:nfm-generic-plane-isom-splitting`）。さらに生成元固定形式模型の active 恒等分枝に一致するものを選ぶと、下記の共変性により良い一ブロックの共通滑らかな稠密開へ全 O-降下する。証明全文は本文を参照し、再開時には次の四点を保持する。

1. 全次数の混合三角多項式と有限 étale 性を使う**混合定数降下**により、平面同型 torsor を active 係数体上の定数 torsor として扱う。単に形式体上で I_sc が分裂することだけを根拠にしない。
2. 一般三次 g の群 scheme H_g は幾何的に位数27の Heisenberg 群である。F=g+Σu_i³ の対称点を含む近傍へ Poisson 対と labelled H_g 作用を有限対角により延長し、full ambient の表現型 X⊕1^r を形式比較から確認する。定数 Hesse 群の作用へ不適切に置き換えず、一般 g 上の群 scheme として追う。
3. 各 H_g 元を保つ full projective centralizer は (G_m×GL_r)/G_m≃GL_r である。非零の自明中心 summand が character twist を排除し、中心元の固有値が二つの block の混合を妨げる。Hilbert 90 で form を解き、この centralizer が active 平面に恒等に作用することから active 同定を得る。active P² だけの centralizer には三捩れが残るので、full ambient を使うことは不可欠である。
4. 対称点での分裂を定数 torsor へ戻して一般の混合係数へ広げ、F′=hF により得る k_n(h) からの純超越降下で元の k_n 上の点を得る。特定の有限 Hesse 根号拡大や完備体上の分裂だけで結論しない。

Fisher の §9.5 の中央拡大・既知の Heisenberg 表現と、本稿での full ambient 中央化群・混合定数降下への適用を区別する。平面同型の存在は full kernel class の選択ではない。

### 指定半古典平面同型の parabolic 共変性と全 O-降下

生成元固定形式模型の active 恒等分枝に一致する φ_sc は、良い一ブロック O-marked stack Msm の共通な滑らかな稠密開 U 上で I_sc の切断へ降下する（`prop:nfm-semiclassical-plane-isom-descent`）。全 O-保存同値と任意底変更に両立し、Brauer–Severi 平面も許す。これは平面と埋込み曲線の同型であり、偏極線束の scalar 同型を選ぶものではない。

証明の要点は、中心空間を保つ parabolic の一般元 x↦Mx+Cu、u↦Du を全て扱うことである。Δ=det M とすると作用は a⋅F=Δ⁻¹a(F)。TH 正規化の中心元と、**純中心項を含む full potential** は

\[
 \Omega_h(a\cdot F)=\Delta^{-1}a(\Omega_h(F)),\qquad
 W_h^{\mathrm{TH}}(a\cdot F)=\Delta^{-1}a(W_h^{\mathrm{TH}}(F))
\]

を満たす。純中心項を零にした primitive だけのせん断共変性は仮定しない。u=0 では C,D が消え、gとJ_gが同じ Δ⁻¹ 重みで移るため、形式 active 恒等同型と半古典 Jacobian 分枝を保つ。一般の a,F の体上で、形式比較から得る二つの有理平面同型の一致を忠実な Laurent 体拡大から戻し、F′=hF の変数変換によって一般点の P-同変性を得る。

次に正規な表示 atlas J° 上で有限 étale torsor の指定有理切断を一意に延長する。P×J° 上の同変性も一般点から分離性で延び、次数スカラーは両平面に恒等なので P/G_m の quotient へ降下する。既存の全 O-同値の局所次数付き持上げを使い、全 O-同値に対する自然性と任意底変更を得る。特定の中心基底や active 補空間は追加標識として残らない。

この自然性は固定した formality 規約と指定形式分枝に関するもの。全 intrinsic 成分・共通稠密開の外・任意 formality 間の独立性は含まない。full kernel class の選択とscalar gerbeの中立性も、この平面同型だけからは導かない。点型の表示独立性には上記のκとq_Yの自然性を別に証明し、n=3,4の一般点のfull class選択には下記の全自己同値群を使う。exact index 三は標準 split 一般係数体の結果であり、非分裂表示の全ての体に同じ index を主張しない。

### 残余側の exact index と点型 full 核の不存在

一般の二曲線についての移送式は保持するが、標準 split 係数体 k_n 上では [I_sc]=0 なので

\[
 \delta_{C_{\rm res}}(p_{\rm res})
 =\delta_{E_{\rm pt}}(p_{\rm pt}),\qquad
 \operatorname{per}\delta_{C_{\rm res}}(p_{\rm res})
 =\operatorname{ind}\delta_{C_{\rm res}}(p_{\rm res})=3.
\]

この等式は full class 選択前の幾何的な Picard 障害の判定である（`cor:nfm-generic-residual-picard-index-three`）。点型 full class を k_n 上で整合的に選べた場合、その scalar gerbe α はこの非零類に等しく、scalar 段階の最小分裂次数は三となる。残余平面三次の一般横断直線切片は次数三の finite étale 分裂被覆であり、index 三のため体上では三次分裂体を得る。一般次元ではこの段階だけからfull classを選択しない。n=3,4については次の自己同値群による独立の議論が第一段階を補う。

実際の点型 full P があれば H⁻¹(q_YΦ_P(κ_nc)) は p_res を表す実線束であり、上の障害が零となる。従って k_n と三に素な有限拡大上にはそのような P は存在しない。実際の点型 P を持つ任意の有限 L/k_n は3∣[L:k_n]を満たし、点型比較被覆の各一般成分にも同じ整除性が成り立つ（`cor:nfm-point-comparison-cover-three-divisibility`）。I_sc は元の体で分裂するため、φ∈I_sc(L) をデータに加える必要はない。この議論には full class の事前選択や代数的 active 核 assignment は不要である。

全nでのこの証明は点型m_P=p_resを仮定する。その型は良い共通稠密開上で全O-降下するが、全refined核が点型となるとは主張しない。n=3,4では全full核のscalar gerbeが同じことを別に示すため、点型の同一性を仮定せず任意full核の不存在へ拡張できる。n≥5ではfull class選択と任意full核への障害の拡張が残る。

### 非分裂偏極類の Picard index 九と一ブロック族への実現

実際の次数三線束がある場合の index 三上界と、次数三の偏極**類**だけがある場合を分ける。主証明は [非分裂 Picard 障害の節](../papers/sections/residual_unsplit_picard.tex) に置く。symbol は \(YX=\zeta XY\)、\(X^3=c,Y^3=d\) の規約で \((c,d)_3\) と書く。

\(\ell=\mathbf C(\lambda)\) 上の一般 Hesse 曲線 E とその三捩れ基底を取り、F=ℓ(E)、p∈E(F) を一般点とする。\([3]:E\to E\) の一般ファイバーが連結な次数九の体なので、\(\kappa_3(p)=([u],[v])\) の二座標は F×/F×³ で独立である。K=F(a,b) 上で \(\xi=([a],[b])\) による translation twist C を作ると

\[
 \beta=\delta_C(\lambda_C)=(a,b)_3,\qquad
 \alpha=\delta_C(p)=(a,v)_3-(b,u)_3,\qquad
 \operatorname{per}(\alpha)=3,\quad\operatorname{ind}(\alpha)=9.
\]

λ_C∈Pic³_C(K) は偏極類で、実線束ではない。β の period と index は三であり、α,β は Br(K)[3] で線型独立となる（`prop:nfm-unsplit-genus-one-picard-nine`）。符号は逆巡回の theta lift AB=ζ⁻¹BA を用い、Picard cocycle が点座標の matrix factor set の逆であることを直接計算して固定する。同じ規約で Tate–Weil 公式と整合する。α の division 性は F((a))((b)) 上の辞書式付値で示す。九つの単項式の値が Z² を法として異なるため、各積の最低項が一意で消えない（`lem:nfm-bisymbol-index-nine`）。この議論は二つの Kummer 座標の独立性を使う。C 自身も period 三・index 九であり、点を持つ拡大の最小次数は九。α の index は純超越拡大で保たれる。曲線の period–index 現象、theta obstruction と Tate pairing の一般論そのものの新規性は主張しない。

一ブロック族への実現には別の mixed theta twist を使う。n−1=3m とし、active theta 表現 V に対して中心表現を U=V⊗K^m と取る。V⊕U 上の中心重みが揃うので projective 表示へ降下し、mixed 三次の重みは三で通常の G=E[3] 表現となる。twisted mixed 係数と中心三次の加法 torsor を一般化する際の拡大は純超越的であり、点障害の index 九を保つ。Hesse 係数の有理逆と全 mixed 係数を使う支配性から、全 n≥4、n≡1 mod3 について良い一ブロック stack の任意の非空開にこの種の体値点がある。表示障害は β、点障害は α であり、構成中に表示の分裂体を加えていない（`prop:nfm-unsplit-point-index-nine-family`）。自然な半古典平面同型により残余側の障害も α となる。

共通な良い開上の普遍点 Picard gerbe では、Brauer–Severi 平面の相対反標準束を C に制限した次数九の実線束 A を使い、\(\pi_*(M\otimes A)\) が重み一・階数九の束を与える。どの非空開にも index 九の体値点があるので、正の重み一階数は必ず九の倍数であり、開を縮めて普遍階数を三にはできない（`cor:nfm-universal-unsplit-picard-rank-nine`）。全ての体値点の index が九となるという意味ではない。

随伴復元条件の矢 \(E_P\to q^RH^0(qE_P)\) も全 O-同値・任意底変更に自然なので、有限 H_p と class torsor S_p、実現 gerbe \(S_p\times\mathscr P_p\) は非分裂形式へ降下する（`lem:nfm-adjoint-point-unsplit-descent`）。指数九例で実際の点型核が L/K 上にあれば 9∣[L:K]。表示安定化子が自明な共通稠密開内では全該当次元で唯一の強化点型 class があり、指数九 division 代数の極大部分体で実現できるため、**周期標識を加えない強化点型の最小実現次数は九**である（`cor:nfm-unsplit-point-minimum-nine`）。全型の最小次数は下記の rotation 計算により三となる。全非分裂体への一律の九、または高次元の S_p の中立性へは拡張しない。

### 非分裂 rotation による gerbe の変更と全型の最小次数

偏極類 λ_C の障害を β=δ_C(λ_C)、選択済み最高次線束型 class の障害を α=δ_C(m_P) とする。非分裂表示では ρ の幾何的 class は降下するが、実際の核の gerbe は β である。局所的な O(i) の双対⊠自身と evaluation は重み零なので Ku 射影核は降下し、tensor O(1) を一度用いる rotation 核は重み一となる。従って ρʳP の障害は α+rβ。この点が、実際の T=ρ⁻¹[1] がある split 体で全 class の gerbe が同じになる証明との相違である。

次数三 Picard 類の gerbe 上の普遍線束の H⁰ は重み一・階数三である。α±β は次数±三の Picard 類の障害なので index∣3。n=3,4 で幾何学的自己同値群が Z の場合、唯一の随伴復元 class P₀ と ρ、shift が全 class を与え、全型の最小次数は min_r ind(α+rβ)、すなわち α∈⟨β⟩ なら一、それ以外は三となる。一般の finite class torsor の成分を用いる全型上界は 3 min_i[K_i:K]≤3|H_p| である。一般一ブロックの表示安定化子が自明な共通稠密開内では全 n で H_p=1 なので全型の上界三を得るが、他の rotation 軌道の K 核は高次元で未排除である。

指数九の四次元族では **強化点型の最小次数九・型を指定しない full 比較の最小次数三** を同時に得る。symbol の等式は α+β=(au,bv)₃、α−β=−(a/u,b/v)₃。三次体 L=K(w)、w³=au 上では α_L=(u,b)₃、β_L=−(u,b)₃ であり、非零性は b-進剰余と u の非三乗性で分かる。従って L 上の full 比較は存在するが、点型の実現も ambient の分裂も起きない。普遍点 Picard gerbe の最小階数九と矛盾しない。主証明は `lem:nfm-unsplit-rotation-gerbe`、`thm:nfm-unsplit-rotation-index-three`、`thm:nfm-unsplit-lowdim-full-degree`、`cor:nfm-unsplit-nine-versus-three` に置き、ここに重複しない。新規性は未確認である。

### projector 核の一意性と三・四次元の full class 選択

既知のFM自己同値分類はexact functorの同型類についての定理であり、perfect dg核の同型類への移行には根拠が要る。滑らかな三次n-fold、n≥3では標準projector jpの核Uは一意である（`lem:nfm-projector-kernel-uniqueness`）。例外的blockのdirected algebraの射影分解長≤n−2から、全点xでp(k_x)がsimpleかつ負の自己Extを持たないことを示す。同じprojectorを与える核Kについて相対Homの次数零は線束Nとなり、evaluationからK≃U⊗p₁*Nを得る。Canonaco–Stellariのcohomology一意性と正のrankを持つpushforwardのdeterminantによりNはtorsion、Pic(Y)=ZによりN=Oとなる。これを包含・projectionと合成して、可逆dg核の同型類からFM自己同値関手の同型類への単射を得る。一般のFM核の一意性を仮定したものではない。

n=3ではLiuの全FM群Z×Aut(Y)と一般三次のAut(Y)=1、n=4ではHuybrechtsのvery general cubicにおける全FM群Zを使う。いずれもT=ρ_Y⁻¹[1]が生成元で、T³=[1]、T²=ρ_Yである。Tは元の係数体に定義されるので、幾何的な核自己同値群はGalois作用自明の定数Zとなる（`prop:nfm-generic-low-dimensional-kernel-aut`）。n=3のSerre式S=ρ_Y[1]、S³=[5]とも整合し、T=S⁻¹[2]である。

四次元の既知定理のvery general条件をZariski開の全点へ拡張しない。除外される可算個の真閉集合の全定義係数を可算体k₀⊂Cへ入れ、残余射の支配性から幾何学的一般残余三次が全てを避けることを使う。任意の核・逆核・合成同型の有限データを加えた体の代数閉包Ω₀をCへ埋めると、この非消滅は保たれる。複素数体上の分類とprojector一意性を適用し、Homの底変更とHH⁰=1によってQ≃T^mをΩ₀へ戻す。この有限データの議論で幾何学的一般点に必要な核群を得る。

一つの幾何的full比較核Pに対し[γP]=[T^(c_γ)P]と置くと、Tが元の体にあるためc_γは連続なGalois群からZへの準同型である。核の有限表示によりその像は有限、したがって零となる。**全ての幾何的full classが元の体上で選択できる**（`lem:nfm-cyclic-kernel-class-descent`）。この全classの降下定理だけでは一つのclassを正準的に指定せず、同型類の層は非標準的にZと同型である。後述する随伴復元条件を加えると、n=3,4では幾何的に唯一のclassを取り出せる。HH¹=0だけの議論やactive class I_scの分裂から、これらの結論を推論していない。

T^mとの合成は元の体上の実際の核で、scalar bandを恒等に写す。従って全class gerbeは互いに同値であり、点型classのα=δ_C(p_res)と同じexact period=index三を持つ。任意のL上のfull核Qから、ある整数mについてT^(−m)Qを作れば点型classを実現するので、3∣[L:k_n]である。逆に三次scalar分裂体上で点型Pを実現できる。従って **n=3,4の標準split一般係数体では、周期標識を忘れた任意full比較の最小体次数は正確に三**となる（`thm:nfm-low-dimensional-full-class-index-three`）。この段階の不存在は点型以外のfull核にも及ぶが、全refined核についてm_P=p_resを示したという意味ではない。

### rotation 同型・周期標識の追加位相

前段はunderlying full核の同型類を扱う。K=k_n、n=3,4とし、選択済みclassの実現gerbeをGとする。V=Hom(Pρ_nc,ρ_YP)は始域・終域のscalarが相殺する重み零の直線であり、K上のV₀へ降下する。指定周期τ_nc、τ_Yに対し、三重合成の規約を

\[
 (\tau_Y P)\eta^{(3)}=c(\eta)\,P\tau_{\rm nc},\qquad
 \gamma=[c(e)^{-1}]\in K^\times/K^{\times3}
\]

と固定する。ここでeはV₀の任意の非零K基底で、変更してもγは不変である。周期標識付きstackはG×T_η、T_η={z³=c(e)⁻¹}であり、scalar G_m inertiaは残る。T_ηの成分体Mの次数は一または三なので、標識付き核の最小体次数は

\[
 [M:K]\operatorname{ind}(\alpha_M)\in\{3,9\}.
\]

下界は任意の実現体がMを含んでα_Mを分裂させること、達成はdivision代数の極大部分体による。最小六などはない（`eq:nfm-period-phase-convention`, `eq:nfm-period-phase-kummer`, `eq:nfm-marked-minimum-index`）。

**位相はfull classを変更しても不変。** 固定入力Bの指定MF周期は、内部shiftと可換で、cohomological次数二のため[1]との交換符号も正である。双加群の境界B→B(−3)[2]とwindowの実際の比較図式から、このcoherenceをKuへ運べる。従ってT=ρ⁻¹[1]の全整数冪はK上で指定周期を保つ。P↦T^mPがV₀の三次形式cを保つため、上のγとT_ηは全full classで共通となる（`lem:nfm-mf-period-central-coherence`, `prop:nfm-period-phase-class-invariance`）。同型類を選び直すことでは非自明位相を消せず、最小次数公式も全classに共通する。

**方程式の生成元による変換。** 中心ideal I=(Ω)のconormal同定B(−3)→I/I²はΩ↦uΩでu倍になる。intrinsicな境界射をこの基底で表示すると

\[
 \tau_{u\Omega}=u^{-1}\tau_\Omega.
\]

従ってsourceの中心元をuΩ_nc、targetの方程式をvF_Yへ変更すると、underlying圏とrotationは同じまま

\[
 c'=(u/v)c,\qquad \gamma'=[v/u]\gamma
\]

となる（`prop:nfm-period-equation-frame-change`）。両側の同時変更u=vでは不変であり、片側だけの独立変更とは異なる。この符号は固定入力Bの`lp:prop:sing-period`、`tw:eq:period-extension`、`tw:eq:rotation-period-square`のconormal・二拡張・window規約に従う。

**適合規格化の次数三と独立尺度の次数九。** γ=[d]と書けば、targetの生成元をd⁻¹倍する選択でγ=1となり、標識付き最小次数は三になる。これは相対規格化の存在であり、正準的な生成元を選んだという主張ではない。他方、独立変数tを取りtargetだけをt倍したK(t)上では、位相の成分体はM=K(t)[s]/(s³−dt)。t=s³/dよりK上の体としてM≃K(s)であり、元の次数三division代数は純超越拡大後もdivisionのままである。よって任意の標識付き実現体の次数は九の倍数、最小次数は正確に九となる（`thm:nfm-free-period-frame-degree-nine`）。独立尺度を元の一ブロック係数やformalityパラメータと無条件に同一視せず、裸のO-marked対だけから次数九を不可避な障害とは呼ばない（`rem:nfm-period-frame-scope`）。この定理は、次の半古典cube frameにおける位相を計算するものではない。

**三次元のSerre比較と残る計算。** ρ≃S[−1]に沿って指定周期をζ:S³≃[5]へ移し、同値の標準Serre比較σ_Pに対する差を

\[
 (\zeta_Y P)\sigma_P^{(3)}=d(P)\,P\zeta_{\rm nc}
\]

と書けばγ=[d(P)⁻¹]である。補助的なρ≃S[−1]の変更は三乗倍だけを変える（`lem:nfm-period-phase-fractional-serre`）。指定したfractional Serre自明化を保つことを示せれば位相は消えるが、S³≃[5]の存在やSerre関手との標準的可換性だけではd(P)=1を得ない。実際、K=C(s)上の同じ可換三次YをsourceではF、targetではsFから来る周期で標識すると、恒等核でc=s⁻¹、γ=[s]≠1となる。これは固定した非可換一般族の位相を計算する反例ではなく、Serre関手だけによる消滅論法の障害である。

**半古典cube frameによる問題の固定。** 低Nat復元が与えるのは残余方程式の直線L_resであり、その基底ではない。そこで、sourceの指定中心元ΩからH=TH(Ω)とΠ=ι(dH)Pにより決まるPを使い、半古典full scalar t_sc∈L_res⊗det K_resと平面同型φ_scを組み合わせる。Pは独立に追加するvolume datumではない。φ_scの線型lift f:K_pt→K_resについて

\[
 F_{\varphi_{\rm sc}}\otimes\det(f)(P)=t_{\rm sc}
\]

と定義すれば、f↦λfでF_φ↦λ⁻³F_φとなり、方程式の非零生成元の三乗倍を除いた類が定まる（`prop:nfm-period-equation-cube-frame`, `eq:nfm-period-cube-frame`）。Ω↦uΩならH↦uH、P↦u⁻¹P、F_φ↦uF_φであり、両周期の相対位相は変わらない。実際の方程式基底や周期標識を選んだこととは区別する。

標準split一般係数体では三捩れの線型Galois像がSL₂(F₃)なので$J[3](K)$=0となる。I_sc(K)の非空性と合わせてφ_scは唯一である（`cor:nfm-generic-plane-isom-unique`）。従ってn=3,4では

\[
 \gamma_{\rm sc}=\gamma(\Omega,F_{\varphi_{\rm sc}})
 \in K^\times/K^{\times3}
\]

がfull class、線型lift、およびsourceとtargetの同時尺度変更によらず定まる。一般の別の体でφを変更する自由まで消したのではない。φ'=φaの線型liftの差をAとすれば、方程式と位相はともに[det A⁻¹]倍となり得る。φ_scの全O-降下と、この標準split一般係数体上の唯一性・cube frameの主張を区別する。

**形式像が消えることと元の体の未解決性。** 実際のCF potentialをW_h、そのactive制限をW_act=b_hJ_g、b_h∈1+hk[[h]]と書く。指定形式比較aの下で、正確な尺度式はa(t_sc)=(h/b_h)W_h⊗P₀である。a f=λ_h idとおけば

\[
 F_{\varphi_{\rm sc}}=\lambda_h^{-3}b_h^{-1}W_h,
 \qquad \gamma_{\rm sc}\longmapsto[b_h^{-1}]=1.
\]

未知の線型lift尺度λ_hは三乗として消え、b_hは1を特殊化値に持つ一意な形式三乗根を持つ（`prop:nfm-period-phase-formal-active-scalar`）。F'=hFで一般係数体へ戻す際にも、source中心元とW_hの両方にhが掛かるため、この比へ余分なhは残らない。しかしKのKummer類から完備体への写像は単射とは限らない。例えば1+hはk((h))では三乗だがk(h)では三乗でない。b_hの代数性もここでは主張していない。元の K での γ_sc の非自明性は、以下の独立な q=2 計算により確定した。その位相体は三次だが、そこでの α の index はなお未計算であり、この規格化の標識付き最小次数三／九は未決である。

この形式像だけでは元の体の値を決められないが、次の混合定数降下によって計算を二変数不変量平面へ移せる。別経路として実際の移送済み MF の微分・射と source の AS-Gorenstein trace 規格化を比較する。Murfet の residue trace は potential の係数だけから比較 scalar を得る公式ではなく、Serre 基底線 D_Y≃det U⊗λ_res の同定も指定 fractional Calabi–Yau 自明化との一致を代替しない。

このμ₃-torsorはscalar G_m-gerbeとも標準三分点torsorとも別である。標準九次体L₉には三次中間体がないので、T_ηが非自明ならL₉でも周期標識を選べない。三分点正規化がperiod図式を保持するのは、既に標識を含めたclassを選択済みの場合だけであり、underlying classの規格化から未選択の周期標識は得ない。三分点の最小次数九・Galois閉包216から周期標識の最小次数を推論せず、scalar gerbeの最小次数三からμ₃位相の消滅も推論しない。全intrinsic moduli上の標準class、任意の非分裂体でのexact index、coherent中心線型性を得たとは主張しない。

### 周期位相の混合定数降下と二変数不変量への帰着

全n≥3の正準な随伴復元点型classを固定する。n=3,4では全full classにも共通する半古典 cube frame の周期位相は、active 十係数体 \(k=\mathbf C(g_\alpha)\) を通り、さらに一意な

\[
 \overline\gamma_n\in\mathbf C(s,t)^\times/\mathbf C(s,t)^{\times3},
 \qquad s=c_4(g),\quad t=-c_6(g)
\]

から来る（`thm:nfm-period-phase-active-descent`、`prop:nfm-period-phase-invariant-descent`）。主証明は [周期位相の降下の節](../papers/sections/residual_period_descent.tex)。全 n の q=2 完備局所値は [D_R] と計算したが、大域的な β_n=γ̄_n/[D] と次元間の一致は未決定である。形式像1は元の体での消滅を意味しない。

核心は \(k(m)((h))\) より小さい体 \(\kappa(m)=k((h))(m)\) 上の実際の周期付き CF 比較である。mixed/pure-center 係数 m=(b,ℓ,d) の重みを1,2,3、active 座標の重みを零、中心座標の重みを−1と取る。内部次数・有限基底の重みを固定した MF 行列では、各 monomial の混合重みは \(D+w_j-w_i\) 以下となり、h の次数や微分の挿入回数に依存しない。逆 flow の各係数は有限個の m 単項式上で h 進収束するため、単なる k[m][[h]] ではなく k[[h]][m] に属する（`lem:nfm-period-flow-mixed-bound`）。

可換側の三つの Koszul stabilization を逆 CF で移し、固定された integral 有限対象の Hom 比較を局所化する。有限 cone と直和因子は pretriangulated hull・冪等完備化の普遍性で扱い、h の負冪を持つ新しい Maurer–Cartan 元へ無限挿入公式を再評価しない。proper Hom と window の実際の局所化、および固定入力の三対象生成を使って \(\kappa(m)\) 上の full Morita 比較を得る（`prop:nfm-period-comparison-mixed-rational`）。この比較は形式拡大後に随伴復元の非空性証明で使った同じ完備CF核となる。全Taylor成分・hullの一致を確認した上で、最高次線束、Picard等式、正準随伴射のconeの消滅を忠実な体拡大から反映できるため、全nで唯一の強化classを実現する（`lem:nfm-period-mixed-comparison-adjoint-type`）。従ってそこで \(\gamma_{\rm sc,n}=1\) となるので、有限 étale 定数降下を二回用い、F′=hF による同時尺度変更も追って混合係数を除く。単に大きい完備体で三乗根が存在することだけでは、この降下は得られない。

不変量体への次の降下では、Kummer 類が SL₃ 不変というだけでは足りない。線型 lift f と周期解 η の組に

\[
 (f,\eta)\longmapsto(\lambda f,\lambda^{-1}\eta),\qquad
 F_{\lambda f}=\lambda^{-3}F_f,\quad c_{\lambda f}=\lambda^3c_f
\]

という実際の作用を入れ、商として coherent な μ₃-torsor を作る。核の scalar は Hom 直線上で相殺するので、表示変更の合成もこの torsor へ降下する。一般 SL₃ 安定化群 H_g の可換化は元の三次 V(g) の Jacobian の三捩れ J_g[3] であり、全 SL₂(F₃) モノドロミーから K 有理な character H_g→μ₃ は零となる。従って安定化群の作用が自明で、Fisher の一軌道の一般ファイバーを用いて商 gerbe から C(s,t) へ降下する。active 係数体が不変量体上正則であることが一意性を与える。

**境界を絞れた場合の大域式。** Δ=s³−t²、D=1−s/24−t/216−s²/6912 とする。torsor が U=Spec C[s,t,1/(ΔD)] へ有限 étale に延びるという追加仮定の下では、U の UFD 性と Kummer 列により類は [Δ]^a[D]^b と書ける。半古典代入で Δ↦h¹²Δ、D≡1 mod h となるため既知の形式像1は a=0 を強制する。下記の D 付値1により b=1、従って γ̄_n=[D] となる。追加仮定なしで得たのは D での局所値と非自明性までである（`lem:nfm-period-two-boundary-criterion`、`prop:nfm-boundary-period-local-kummer`）。
\(D=1-s/24-t/216-s^2/6912\) とする。torsor が
\(U=\operatorname{Spec}\mathbf C[s,t,1/(\Delta D)]\)
へ有限 étale に延びるという**追加仮定**の下では、U の UFD 性と Kummer 列により類は [Δ]^a[D]^b と書ける。半古典代入 (s,t)↦(h⁴s,h⁶t) で Δ↦h¹²Δ、D≡1 mod h となるため、既知の形式的消滅は a=0 を強制する。従って候補は1,[D],[D]²。さらにD=0の一般点でも非分岐ならb=0となる（`lem:nfm-period-two-boundary-criterion`）。

既存の判別式公式 Δ(c₄(J_g),−c₆(J_g))=Δ(s,t)D(s,t)³ により D は点三次の追加判別境界である。D の付値は計算済みだが、現在の定義開だけから他の branch divisor がないとは言えない。次は β_n=γ̄_n/[D] の他の divisor を調べる。他の分岐を排除せず局所値 [D_R] だけから大域式 [D] や次元間の大域的一致を推論しない。

### 忠実な Hesse 制限と追加境界の具体模型

K=C(s,t) と Hesse 体 L=C(p,q) の三次 Kummer 核は正確に ⟨[Δ]⟩≃Z/3 である。Galois 群 Q₈⋊C₃ の character の位数三と、Δ(r(p,q))=(−4p(p³+q³))³ から従う。一般 active 十係数体 E/K は正則であり、E((h)) での半古典像1を K((h)) へ戻せるため、この核の非自明な二元は排除される。したがって現在の規格化位相は Hesse 体への制限で忠実に検査できる。Hesse 完備化を先に取ると Δ 自体が三乗なので、この議論は成立しない。主証明は `lem:nfm-period-laurent-constant-injective`、`lem:nfm-hesse-cubic-kummer-kernel`、`prop:nfm-period-hesse-faithful-test`。

D の Hesse 引戻しは八直線の積である。q=2 の一般点で det Dr=−384p²(p³+8)²、Δ=−64p³(p³+8)³ は非零で、分岐指数は一。D=−(p³+8)²(q−2)/27+O((q−2)²)。剰余体 C(p)/C(p³) の次数三を分岐指数と混同しない。この trait での実際の周期付値1 mod3は、元の不変量平面でも同じ D 付値を与える（`lem:nfm-period-hesse-eight-boundary-lines`、`prop:nfm-boundary-period-local-kummer`）。

**active 境界代数。** g=p(x³+y³+z³)/3+qxyz とすると q=2 では zy=−px²/2、xz=−py²/2、yx=−pz²/2。u=−p/2 と置き、S_u=K⟨x,y,z⟩/(zx−uxz,xy−uyx,yz−uzy) の巡回自己同型 τ(x)=z、τ(y)=x、τ(z)=y で a*b=aτ^{deg a}(b) とすれば、この境界代数を得る。例えば z*y=zx=u xz=u(x*x) で、他二式は巡回する。固定入力 A `hesse_mixed_universal_center.tex`, `thm:pg-universal-hesse-mixed` の中心式を h′=p、t=q/p として p 倍すると、Ω=pU(x³+y³+z³)/3+V sym(xyz)、U=1+q²/2+p³q/6−q⁴/48、V=(4−q²)(12q+q³−8p³)/48。q=2 では Ω=p(p³+8)x³/3、J=(p³+8)xyz/3 であり、x^{*3}=u⁻¹xyz より Ω は −2J に移る。

この −2 は C の三乗だが、full 周期位相の非分岐性を意味しない。一般の S_u は可換でなく、active twist を中心変数へ自明に延ばすと次数一中心変数が新積で中心でなくなる。実際の局所位相は、下記の full 低積・二次関係の飽和・generic active Isom の延長によって [D_R] と決定する。source 境界の AS-regular 性と primitive 中央元は、回復した raw 関係の flatness を保証しない。

**反対代数の障害。** 反変双対は intertwiner の矢印と rotation の両方を反転するため、正の rotation へ戻す際に scalar weight が元へ戻り得る。したがって反対操作と c₄,c₆ の偶数次数だけから γ=γ⁻¹ は導けない。同じ可換 cubic を source 方程式 F、target 方程式 aF で標識すると、underlying opposite は同じでも周期位相は任意の [a] を持つ。conormal 周期を含む図式を比較する必要がある。

### q=2 境界の三分点と点線束の有限模型

z=q−2、k₀=C(p,m)、R=k₀[[z]] とする。点三次は AΣX³/3+BXYZ、A=p(1−q²/4)、B=q+p³/3+q³/12。P=(1−q/2:−1−q/2:−p) と O=(1:−1:0) はそれぞれ C_X、C_Z の滑らかな点へ落ちる。全空間は三節点で横断微分 −p/3 を持つ正則 split I₃ 模型である。M=O(P−O) の multidegree は (1,0,−1) で、交点行列から垂直 twist で零にできない。一方 M³(C_X−C_Z) は全成分次数零となる。紙上証明は `prop:nfm-hesse-boundary-third-division`。

T=(0:1:−1)、U=(1:−ζ:0) による Kummer 二座標は ([(p³+8)/(2z)],1)。接線比を原点の局所座標で先頭係数一に規格化し、F∘[3] が三乗になることを確認して Silverman XI.9.2 を適用する。従って [3]⁻¹(P) は同じ完全分岐巡回三次体 L=K(∛(2z/(p³+8))) の三つのコピーであり、幾何的慣性型は3³。一般 active 係数へは非分岐な Hesse chart でこの慣性型を移す。一般係数の剰余体上でも三つのコピーに分かれる、とまでは主張しない。

M₀(j) の cohomology は j≥1 で (h⁰,h¹)=(3j,0)、j=0 で零、j≤−1 で (0,−3j)。M₀(1) は `eq:nfm-hesse-boundary-determinantal-line` の行列 L₀による 0→O(−1)³→O³→i_*M₀(1)→0 を持つ。行列式 −XYZ、三節点での階数二、三切断の貼合せを厳密検算した。相対持上げは存在だけでなく、完備化前の DVR R₀=k₀[q]_(q−2) 上の有理式 L=U⁻¹NV で明示できる。b=(p³+8)/3 とすると det L=−F_E/b、L mod(q−2)=L₀、Q=−b adj(L) は LQ=QL=F_E I₃ を満たす。三分点の選択は不要であり、この行列は点関係行列から得た三倍線束とは別で、実際の M(1) を表示する。式と cokernel の同定は [境界の節](../papers/sections/residual_boundary.tex) の `lem:nfm-hesse-boundary-explicit-line` を参照する。

D_R=D(r(p,2+z)) に対し [D_R]=[(p³+8)/(2z)]⁻¹、従って L=K(∛D_R)。Kummer 制限の核は正確に ⟨[D_R]⟩ であり、条件付き候補1,[D_R],[D_R]²はこの被覆上では区別できない（`cor:nfm-hesse-boundary-period-candidates-blind`）。三分点上で周期分裂を仮に示しても、元の D-付値を決定しない。

**指定周期を保つ残余模型。** 一般 fibre の唯一の φ_sc を用いて active 平面を点三次 J_g に合わせ、残余方程式の active 制限を J_g に規格化する。混合係数の極を中心座標の u↦zᴺu で消せば、同じ target 方程式とその MF 周期を保つ integral 平坦模型を、分岐した体拡大なしに選べる。C_res は点曲線の I₃ 模型となり、φ_sc と点線束もこの選択した模型へ延びる。正準性や特殊 fibre の滑らかさは主張しない。全空間は C に沿って正則で、C は中心一次式による regular immersion である。証明は `prop:nfm-hesse-boundary-integral-residual-model` と `lem:nfm-hesse-boundary-transverse-smoothness`。

**全次元の full 残余対象。** r=n−1 とすると、負の line bundle block の右変異 R_O(−1)⋯R_O(−r) により q_Y^RM[1] の相対 perfect 模型を作る。右端から適用し、最後の [1] を保持する。相対 Gorenstein 双対と有限 mutation は特異な特殊 fibre でも使える。F−J_g=Σu_iG_i と相対線型行列から、各 parity の階数3·2^rの明示 MF を得る。raw MF は i_*M(1) の stabilization を表し、右射影対象との同定は別途実際の window1で行う。指定された内部 shift と F の自己交叉周期もこの窓で合わせる。証明は `prop:nfm-boundary-right-projection`、`lem:nfm-boundary-line-mf` と同じ境界節の窓比較。

**三次元の低 Hom。** n=3 では最初の O(−2) に関する right mutation が零となり、残る一つの coevaluation cone で対象を表示できる。adj(L₀) の成分が平面上の六つの二次単項式を張るので H⁰M(1)⊗H⁰M⁻¹(1)→H⁰O_C(2) は全射である。これと lci Ext、逆 rotation、相対 Serre、指定方程式の MF 周期から次を得る。表にない Ext は零であり、全項が R-自由で閉・一般 fibre への底変更と可換となる（`prop:nfm-boundary-threefold-low-hom`）。

| 内部次数 q | HⁱRHom(Z,ρ^qZ) の非零階数 |
| --- | --- |
| 0 | i=0で1、i=1で10 |
| −1 | i=1で5、i=2で5 |
| −2 | i=2で10、i=3で1 |
| −3 | i=2で1、i=3で10 |

指定 target 周期 t_p は q=−3、i=2 の自由階数一加群の生成元である。Burke–Stevenson の正の Gorenstein parameter に対する Theorem6.4(1), i=1 を用い、相対窓と実際の F-自己交叉周期を合わせた結果であり、一般点の周期同型を無条件に特殊化したものではない。

### 全次元の低積・飽和と完備局所周期位相

主証明は [境界の低積と周期位相](../papers/sections/residual_boundary_products.tex)。有限行列の再生成は `python3 computations/verify_boundary_low_products.py` による。実行状態は `validation.md` を参照する。

中心項を z²以上へ消すように模型を選ぶと、指定方程式を変えず F≡J_g mod z² とできる。実際の窓を通した MF は、この一次近傍で active 3×3 MF と中心 Koszul 因子の tensor に分かれる。全 n≥3 で orbit Hom は R-自由かつ底変更と可換であり、N=n+2 とすると

\[
 \operatorname{rank}_R H^iR\operatorname{Hom}(Z,\rho^jZ)
      =\binom{N}{3i+2j}
\]

となる。下添字が0未満またはN超なら零とする。上の n=3 の表はこの一般式の例である。period class t_p は自由階数一加群の生成元だが、特殊 fibre の active 二次積は全て零、三次積の relation class も零である。full の m₂* の階数は binom(N,2)−3。この例は「自由な低 Hom と primitive な周期から primitive な関係が従う」という推論を具体的に否定する。

**二次関係の飽和。** zで割った最初の active 二次積は階数三で、三つの Smith 指数は全て一である。特殊 fibre の飽和関係は

\[
 ac+p^2b^2,\qquad a^2+pcb,\qquad ba+\frac{p^2}{8}c^2.
\]

X=a、Y=pb、Z=pc/2 により、これは source の S(0,−2,−p) に一致する。full の飽和二次代数は全次数で R-flat となり、特殊 fibre はこの Sklyanin 代数に r 個の中心変数を付けたものになる。次数一中心は内在的な commutator map の核として自由部分束となり、その中央商も flat である。raw 二次関係加群をそのまま source 格子と同一視しない。

**同型を延ばす三次は potential の方である。** active 商の cubic syzygy line (R₂⊗V)∩(V⊗R₂) は自由階数一で、底変更と可換となる。generic CY potential の巡回性は R 上に延び、alternating 成分が特殊 fibre で非零なので volume で規格化できる。対称成分から得た potential 三次は特殊 fibre で g=pΣX³/3+2XYZ となり、p(p³+8)≠0により滑らかである。指定 generic graded Isom はこの滑らかな偏極三次間の射影 Isom を与えるので、Benoist の proper な対角によって R 上へ延び、Pic(R)=0で線型持上げを取れる。特異な点三次 J_g=0 の同型空間に有限性を仮定する議論ではない。full 特殊代数には GL_r の中心自己同型が残るため、full Isom の有限性や full kernel の積分延長も主張しない。主証明は `prop:nfm-boundary-saturated-active-potential`。

**三次関係の初出と周期値。** 同じ homotopy 系で三次テンソルの零次項自体が零となるため、zで割った初出 class は二次関係や中心格子の未使用の高次項に影響されない。指定 t_p に対する三次積の一次項は、共通の符号規約を除いて −z acb/(3p)。飽和商では acb=−X³/p なので、Ω_p/z の像は X³/(3p²) となり非零である。source の指定中央元は Ω₀=p(p³+8)X³/3 だから、実際の比較 scalar の先頭比は z/[p³(p³+8)]。特殊 active Sklyanin の射影自己同型群 μ₃²の標準持上げは X³=Y³=Z³ を固定し、残る grading scalar は三乗を掛けるだけである。

\[
 D_R=-\frac{(p^3+8)^2}{27}z+O(z^2),\qquad
 \frac{1/[p^3(p^3+8)]}{-(p^3+8)^2/27}
       =\left(-\frac3{p(p^3+8)}\right)^3.
\]

完備 DVR では1+zRの単元が三乗根を持つ。従って全 n≥3 で γ_sc,n|_{k₀((z))}=[D_R]、v_D(γ̄_n)=1 mod3となる。位相被覆は tame な完全分岐三次拡大であり、元の一般係数体上でも正準位相は非自明、位相体の次数は三である（`prop:nfm-boundary-period-local-kummer`）。局所三分点体と一致することだけから、一般位相体上の scalar Picard 障害の消滅を導かない。大域式 γ̄_n=[D] には ΔD 外の非分岐性が残る。

**smooth な曲線の共役公式を直接延長する障害。** M₀の multidegree は (1,0,−1)。x∈C_Xの滑らかな点で M₀(x) は (2,0,−1) となり、唯一の切断は C_Y∪C_Z 上で零、C_X の二節点で単純零を持つ。評価 O_C→M₀(x) の核は I_{C_X}、余核は M₀(x)|_{C_Y∪C_Z} で、ともに非零である。従って T_O(−⊗M₀)T_O⁻¹(k(x)) は点層ではなく、smooth elliptic の graph 認識をこの fibre へ無条件に延ばせない。M₀(1),M₀⁻¹(1) の大域生成性は保持される。失われるのは次数一の切断の零因子が零次元 Cartier 因子となる性質である。

### 高次元の class 障害を rotation 中央化群へ絞る

幾何的な可逆dg核の同型類の群で、rotationを保つ部分をG_ρ、その比較class torsorをC_ρと書く。ここではrotationを保つ**性質**だけを使い、比較同型ηや周期の標識は加えない。S=ρ^(1−n)[n]、ρ³=[2]から、n=3mではρ=S[−m]、n=3m+2ではρ=S⁻¹[m+2]なので、n≢1 mod3ではG_ρは全自己同値群である。n≡1 mod3ではこの同一視を行わない（`prop:nfm-highdim-rotation-serre`）。

T=ρ⁻¹[1]は元の体K上の実核で、G_ρの中心に属し、T³=[1]である。proper性により非零shiftは恒等にならず、〈T〉は定数Zとなる。各class cとそのT軌道c̄に対して

\[
 \operatorname{Stab}_{\Gamma_K}(c)
 =\operatorname{Stab}_{\Gamma_K}(\bar c).
\]

実際、軌道を固定するprofinite部分群上ではγc=T^(a_γ)cと書け、a_γはZへの連続準同型なので零となる。従ってclassの定義体とT軌道の定義体は一致し、class選択はC_ρ/〈T〉というG_ρ/〈T〉-torsorのK点、すなわちH¹(K,G_ρ/〈T〉)の対応する類の中立性へ帰着する（`prop:nfm-highdim-central-shift-obstruction`）。同じT軌道のclass gerbeはbandを保って同値になる。

点型は全O-降下によりGalois不変なので、**点型classを含む一つのT軌道がGalois固定か**を判定すれば十分である（`cor:nfm-highdim-point-class-orbit`）。Tが全ての点型を保つことや、全full群を先に分類することは不要。一方、商torsorが有限とはまだ分からない。各点のGalois軌道が有限であることと、全軌道の数や大きさの一様有限性は異なる。また符号作用を持つZではH¹(Z/2,Z₋)=Z/2なので、Galois作用が捩れたtorsion-free群の消滅を仮定しない。

**奇数次元では数値的自明部分が残る。** 実際のO_Y(1)を持つ奇数次元三次では、偶数コホモロジーがambient由来であるため、Kuの数値格子Nは階数二でGalois作用は自明となる。R=ρ_*の最小多項式はt²+t+1であり、Eisenstein整数の単元の計算から

\[
 \operatorname{Cent}_{\operatorname{GL}(N)}(R)
   =\{\pm I,\pm R,\pm R^2\},\qquad
 G_\rho/\langle T\rangle
   \simeq G_{\rho,0}/\langle[2]\rangle,
\]

を得る。G_ρ,0は数値作用の核である。T_*=-R⁻¹が六元群全体を生成し、G_ρ,0∩〈T〉=〈T⁶〉=〈[2]〉となることによる（`prop:nfm-odd-numerical-rotation-centralizer`）。この商群全体の自明性や、Hochschild/Jacobianへの作用の忠実性は未証明である。n=5の具体的なclass選択では、下記の随伴復元条件により、この群全体ではなく有限安定化群H_pへさらに絞れる。

**七次元での既知球面対象の意味。** Iliev–Manivelの一般三次七様体のCartan表示は、Ku内の階数九の三次元球面対象Sを与える。v=[S]、w=[p(k_x)]とするとχ(w,v)=−9、球面twistはw↦w−9vとなるので無限位数である。[1]との間に関係はなく、全自己同値群はZ²を含む（`prop:nfm-sevenfold-noncyclic-aut`）。さらにRに有理不変直線がないことから、球面twistの非零冪はG_ρへ入らず、G_ρはfull群で無限指数となる。これは高次元の全群を一律Zとする経路も、full群を有限個のrotation型へ分ける経路も妨げる。ただしG_ρ自身の非巡回性や、n≥5のclass降下の不成立を示すものではない。球面対象・twistの理論そのものは既知入力であり、現在の障害問題との接続を区別する。

Pirozhkovのenhanced pairからの三次復元、Huybrechts–Rennemoのrotation保存核からのHochschild/Jacobian同型は、自己同値の作用の忠実性を与える結果ではない。最近のcategorical Torelli・Fourier–Mukai partnerの有限性も、固定標的への核classの有限性や上のH¹の中立性へ置き換えない。

### 原点像を右随伴で復元する強化点型と有限 H_p

標準split一般係数体K=k_n上でZ=j_nc!O、q=Li_C* j_Yと置く。qの右随伴はq^R=j_Y!i_*である。ここにi!やdeterminant twistを入れない。a=n−1個の線型切断のKoszul解消と、Serre半直交性によるj_Y!O_Y(−j)=0（1≤j≤a）から

\[
 j_Y^!\mathcal O_Y\simeq q^R\mathcal O_C
\]

を得る（`lem:nfm-origin-active-right-adjoint`）。点型Pに対しE_P=Φ_PZ、M_P=H⁰(qE_P)を置くと、truncation qE_P→M_Pの随伴として正準な射E_P→q^RM_Pがある。この射が同型となることを**随伴復元条件**とし、条件を加えた点型をここでは強化点型と呼ぶ。全ての既存点型がこの条件を満たすとは主張しない。

この強化型は全n≥3で非空である（`prop:nfm-adjoint-point-type-nonempty`）。既存の形式CF比較は一般ファイバーでqE≤0と次数零の最高次線束を与え、閉ファイバーではE_0=j_Y!O、H⁰(qE_0)=O_Cとなる。この両ファイバーの条件から、独立のDVR補題 `lem:nfm-dvr-top-line-lifting` によりQ=q_RE_R≤0、M_R=H⁰(Q)がflat線束で、閉・一般底変更と両立することを得る。局所環AでH⁰(Q)/h≃A/hからNakayamaでA→H⁰(Q)を全射に持ち上げ、一般ファイバーのrank一から核がh-torsion、AのR-flat性から核零となる。正のcohomologyの消滅と局所同定の全体化にはperfect性とproper性を使う。**閉ファイバーだけの線束性から平坦性を推論しない**。例えば微分hの二項複体はその誤推論を妨げる。

qE_0∈D≤0、H⁰(qE_0)=O_CからHom(qE_0,O_C)=Kで、右随伴counitはid_E0に対応する非零射なので、truncationの随伴は閉ファイバーで同型である。coneのperfect性、Y_Rのproper性と導来Nakayamaから形式族全体で同型となり、この射と逆・合成等式も有限降下へ加えられる。相対族で負rotationの層分解を主張する必要はない。

p=p_resを表す線束Mを代数閉包上で一つ取り、E_p=q^RMとする。pがK有理でq^RがK上にあるので、E_pの幾何的同型類はGalois不変である。Mの実線束としてのK降下は不要で、非零のPicard障害αは消えていない。強化点型class集合に

\[
 H_p=\{g\in G_\rho:g(E_p)\simeq E_p\}
\]

が単純推移する。**この群は有限である**。源のκと三連続rotationが生成する固定windowの入力を比較核で移すと、G_p=E_p⊕ρE_p⊕ρ²E_pが全Kuのcompact generatorとなり、H_pはG_pを保つ。標数零の代数閉体上のsmooth properかつ冪等完備なdg圏でHH^{<0}=0、HH⁰=k、HH¹=0なら、指定generatorを保つ自己同値類は有限である（`lem:nfm-generator-stabilizer-finite`）。Morita代数A=REnd(G_p)を使うと、核圏のgeneratorはfree A^eで、核QへのHomはRHom(G_p,QG_p)。QG_p≃G_pならそのcohomology次元は一様に固定される。Toën–Vaquié Proposition3.20によるbounded stackは有限型、可逆核locusは開、HH¹=0のclass空間は離散なので、準compactな像は有限となる。stackのproper性や自己同値群全体の有限性は用いない。

従って強化点型のclass層は有限étale H_p-torsor S_p/Kとなり、実現stackは

\[
 \mathscr G_p\simeq S_p\times_K\operatorname{Pic}_C^p
\]

である（`thm:nfm-adjoint-point-finite-class-torsor`）。最高次線束を取る写像がscalar bandに恒等を誘導することが、積表示の根拠となる。T^mE_p≃E_pならT³=[1]よりE_p[m]≃E_pとなり、proper性からm=0。よってH_p∩〈T〉=1で、強化点型は各T軌道に高々一つのclassを持つ。この有限torsorがfirst stageを表し、一般一ブロック族では下記の忠実性で中立化される。任意点型・任意full核のclass層全体が有限となるという主張ではない。

n=3,4ではGρ=〈T〉なのでH_p=1、S_p=SpecKとなる。従って強化点型は**幾何的に唯一のfull classを正準的に選び、そのclassはKへ降下する**（`cor:nfm-low-dimensional-canonical-adjoint-class`）。実際の核を選ぶことは別であり、そのgerbeは依然としてexact index三のPicard gerbeである。ここでの正準性はこの条件と一般係数体のscopeに関するもので、全moduli上の普遍核の存在を意味しない。

既存のrotation Euler格子の三値χ(Z,ρ^rZ)、r=0,1,2のgcdはd_n>0である（`lem:nfm-cubic-euler-gcd`）。支配的なDVR族のproper perfect HomのEuler rankを比較し、強化点型の同値で移すと、少なくとも一つのχ(E_p,ρ^rE_p)が非零なので[E_p]≠0となる。n=5では自己Euler数だけでχ(E_p,E_p)=1−C(7,3)+C(7,6)=−27と分かる。奇数次元の数値中央化群C₆の非恒等元は非零ベクトルを固定しないため、全奇数n≥3で

\[
 H_p\subset G_{\rho,0},\qquad H_p\cap\langle[2]\rangle=1
\]

を得る（`cor:nfm-odd-finite-stabilizer-numerical`）。この**有限**安定化群を消すか、当該torsorを中立化すればよく、全Gρ,0/〈[2]〉の分類は不要である。

全n≥3に戻りS_p=∐SpecK_iと書けば、強化点型の周期標識を含めない最小実現次数は

\[
 \min_i[K_i:K]\operatorname{ind}(\alpha_{K_i})\le3|H_p|.
\]

Tate–Koszul忠実性により全nでH_p=1、S_p(K)≠∅となり、一般split体で最小三を得る（`cor:nfm-adjoint-point-realization-degree`）。体成分の次数が|H_p|を割ることは一般には仮定しない。

### 五次元 Clifford 半 rotation の平面非依存性と実核降下

主証明は [五次元 Clifford 半 rotation の節](../papers/sections/residual_fivefold.tex) にある。一般の残余三次五様体 Y/K では F=F₂(Y) が滑らかで幾何学的に連結であり、Ku(Y) は HH^{<0}=0、HH⁰=K、HH¹=0 を満たす。平面 Π⊂Y を選んだ Liu の同値 \(A_\Pi=\Psi_\Pi\sigma_\Pi^*\) により Clifford rotation を Ku へ移すと、既知式は \(O_\Pi^2\simeq\rho\)、\((O_\Pi)_*=S_*\) を与える。ここで T=ρ⁻¹[1]=S[−2]、T²=ρ、T³=[1] である。

普遍平面の blowup と相対 quadric surface fibration により、これは実際の相対 perfect 核として F 全体に構成できる。Clifford algebra・奇 bimodule・Ψ,Φ・相対 mutation は実在する束と評価写像から作り、局所選択を貼り合わせる gerbe の中立性を先に仮定しない。随伴の向きは \(\Psi\dashv\Phi\)、\(A^R=j_Y^!R\sigma_*\Phi\)。相対例外性は \(R\mathcal Hom(C_i,C_i)\simeq C_0\) と proper な P³-bundle の cohomology base change から確認する（`lem:nfm-fivefold-clifford-relative-kernel`）。

実族 F→Autkernel の class 写像は、HH¹=0 による離散 class 空間への射となる。F の幾何学的連結性により一定で、共通 class [O] は Galois 不変となる（`prop:nfm-fivefold-half-rotation-plane-independent`）。その実現 gerbe β_O は convolution の band (λ,μ)↦λμ と O²=ρ の実核から 2β_O=0 を満たす。F の次数2835の零 cycle の各点上に実核があるため corestriction により 2835β_O=0。両整数は互いに素なので β_O=0 となり、元の体上の実核 O を得る（`thm:nfm-fivefold-half-rotation-kernel-descent`）。β_O は表示 gerbe β や点 Picard 障害 α と別の類である。

従って \(\epsilon=OT^{-1}=O^3[-1]\) は元の体上の実核で、ε²≃id、数値作用は恒等となる。Liu の構成した安定性の GL̃₂⁺ 軌道を O と T がともに保つ。中心電荷が実二次元格子上の同型なので、有限位数かつ数値的に恒等な元の軌道内の変位は deck shift だけとなり、有限位数から零である。ε はこの軌道を点ごとに固定する（`prop:nfm-fivefold-finite-stability-fixed`）。

spinor 列を相対随伴の unit と同定し、相対 coevaluation と絶対 coevaluation を比較する別の証明から、O≃T=ρ⁻¹[1]、O³≃[1]、ε≃id を perfect 核として得る（`lem:nfm-fivefold-spinor-relative-coevaluation`、`thm:nfm-fivefold-half-rotation-identification`）。M=Rπ_*(σ*E)∨ は Ku の二つの消滅から ⟨O(-1),O⟩ に入り、二つの coevaluation の差は ⟨C₁⟩ に入り mutation で消える。対象ごとの固定や安定性作用の忠実性を仮定していない。この同定は定義された中心平面を持つ任意の滑らかな三次五様体に成立する。元の体上へ降下した O と実核 T の幾何的同型は一次元の perfect Hom により元の体へ戻る。指定 square 同型と MF 周期の同時正規化は含まない。

Liu の stable moduli における Fano 曲面は一つの連結成分であり、全 moduli の既約性はこの同定から従わない。ε は恒等なので当該成分を保つが、一般の自己同値について安定性への作用の忠実性を結論しない。

### 平面対象の PBW と一次元拡張による直接検算

中心平面と交わらない Π は基底 P³ の hyperplane j:D=P²→P³ に写る。S=E(2H)|_Π とすると、isotropic line O_D(-1) と complement O_D³ の Clifford PBW quotient は underlying 束として S=O_D⊕3O_D(-1)、S⊗C₁=3O_D⊕O_D(-1) を与える。module としての直和分解ではない。spinor 列から 0→S(-1)→C₁|_D→S⊗C₁→0、唯一の評価全射 C₁→j_*(S⊗C₁) の核から 0→C_{−1}→K→j_*S(-1)→0 を得る。

最高外積成分への Clifford pairing は C₀∨≃C₀(3) という Frobenius 双加群同型を与える。j!C_{−1}=C₁|_D[-1] と合わせると RHom_{C₀}(j_*S(-1),C_{−1})=k[-1]。実際、D 上の内部 Hom は (S⊗C₁)∨(-1)=O_D⊕3O_D(-1) であり、quadric の非退化性や S の Clifford-projectivity は要しない。underlying 局所自由性と coinduction の随伴を使う。Liu の P_Π の三角も同じ非split拡張の [1] となり、O(F_Π)=P_Π=T(F_Π) を直接検算できる。一般 E_p の評価空間は三・十五次元なので、この拡張一意性だけで全関手同定はできず、本文の相対 coevaluation 比較が必要である。

### E_p の Clifford 像を調べるための二つの mutation

幾何学的に p を表す M∈Pic⁰(C) を取り、active 平面三次 C と交わらない平面 Π を選ぶ。blowup 上の C の持上げを \(i':C\to\widetilde Y_\Pi\)、H を Y の hyperplane の引戻しとする。E_p=j_Y!i_*M の Clifford 像は

\[
 A_\Pi(E_p)\simeq O_{\rm Cl}^{-8}\Psi_\Pi
 L_{\mathcal O(2H)}L_{\mathcal O(3H)}i'_*(M(4))
\]

となる（`prop:nfm-fivefold-origin-clifford-complex`、`eq:nfm-fivefold-origin-clifford-complex`）。Serre の [5] と [−5] が相殺して E_p=ρ⁻⁴p_Yi_*M(4) を与え、Ψ が O と O(H) の mutation を消すことが簡約の根拠である。Π∩C=∅ は導来 pullback をこの形で書く条件として保持する。

最初の評価空間は H⁰(C,M(1))、次元三。二番目は乗法写像 \(H^0(C,M(1))\otimes H^0(Y,\mathcal O_Y(1))\to H^0(C,M(2))\) の核を [1] だけ shift した複体で、次元は 3·7−6=15 である。全射性は M≠O なら base point free pencil、M=O なら平面三次の projective normality から従う。Ψ 自身は Liu の式 (2-4) の rank 四局所自由 Clifford module による pushforward なので、**評価写像を含む有限複体**として OE_p と TE_p を比較できる。数値 class や cohomology 次元の一致だけで ε∈H_p を結論しない。

### Tate–Koszul 復元による全次元の忠実性

主証明は [Tate–Koszul 復元](../papers/sections/residual_tate_reconstruction.tex) に置く。A=B/(Ω)、B が二次 Koszul AS-regular、Ω が正則中心三次という固定入力の下で、双加群自己交叉の自然変換 t:k→k(-3)[2] を使う。Ext_B は対角に集中するため change-of-rings 長完全列の connecting は次数だけで零となり、積込みで Ext_A=B!⊗k[t] を得る。t の cone は perfect、perfect 対象は t の冪で消えるので、stabilization の実 dg 射は中央 t の derived localization を表示する。

Tate 模型では ξ=(1,−1)、t=(2,−3) とし、j=−p−q が t 指数である。j≥0 の切断は全 A∞ 積・射・homotopy で保たれ、通常 Ext を A∞ 代数として回復する。LPWZ の Adams Koszul 双対が A をその全写像とともに回復し、BCL の localization が homotopy epimorphism であることにより通常 Ext への制限は忠実となる。従って homotopy 恒等部分群の pro-unipotence や閉性を別途仮定する必要はない。

核から orbit への比較では、実際の enhanced 同型 Qρ≃ρQ を選び、Keller の関手性を使う。この選択の変更は内部次数 q 上の character c^q だけであり、A の次数スカラーに対応する。Adams 次数を忘れず対象集合 Z、Hom(i,j)=S_{j−i} の covering category へ戻すと、homotopy は κ(i) の全生成部分圏へ戻る。これが核の class に対する忠実性を与える。単に generator の対象像を固定したという議論ではない。

二次関係 R から B=T(V)/(R) を回復し、A の三次関係は RV+VR+kΩ なので、作用は Aut_gr(B,kΩ)/G_m に移る。m₃ のテンソル自体は gauge 不変でなく、f₂(m₂(ξ,ξ),ξ) が t 成分を持ち得るため、Ω はこの quotient 内で扱う。この注意は有用な障害として保持する。良い Poisson 対の stack 同型と一般三次の射影自己同型自明性により、一般一ブロック開で表示安定化子は自明。従って全 n≥3 で H_p=1、S_p=Spec(k_n)、強化点型 class は一意、一般 split 体でその最小実現次数は三である。

幾何学的証明なので、既存の全 O-降下と合わせて非分裂形式にも強化 class の唯一性を適用できる。scalar gerbe の中立性は別であり、非分裂の指数九例では強化型の最小次数九を全該当次元で得る。任意 full 核の分類、全 intrinsic 成分、coherent な中心線型性、指定周期の μ₃ 位相はこの定理で消えない。

**別の gluing 経路の障害。** 原点を保つ自己同値を全導来圏へ延長するには、例外的 block と原点の間の全作用を保つ gluing module が必要である。対象の固定だけではその同型を与えない。現行の忠実性証明はこの延長を使わない。安定性条件・Torelli による多様体復元も、自己同値作用の忠実性を代用しない。

### 指定周期の位相を二次・三次積で評価する

標準 split 一般係数体 K=k_n 上で、Picard gerbe の普遍線束 M から Z_p=q_Y^R M[1] を作る。S_p=⊕_q RHom(Z_p,ρ_Y^qZ_p) は scalar inertia の重み零なので、Adams 次数、合成、全 A∞ 構造を含めて K 上へ降下する。Z_p 自体は K 上の対象でなくてもよい。標的の cube frame を一つ代表して指定周期 t_p∈S_p^{2,−3} を固定する。

X_p=(S_p^{1,−1})* と m₂* の像から B_p=T(X_p)/(R₂) を回復する。t_p*(t_p)=1 とし、Ω_p=[m₃*(t_p*)]∈(B_p)₃ と置く。三次 tensor は gauge 不変ではないが、変化は R₂X_p+X_pR₂ に入り、B_p 内の元は同じとなる。source の中央自己交叉の二拡張と同じ右加群 bar 規約で、t_Ω の双対が +Ω となることを確認する（`lem:nfm-tate-cubic-relation-normalization`）。

一般表示の射影安定化子の自明性と Hilbert 90 により K 上の f:(B_p,KΩ_p)≃(B,KΩ) が存在し、

\[
 \gamma_{\mathrm{sc},n}=\left[\frac{f(\Omega_p)}{\Omega}\right].
\]

証明は `prop:nfm-period-phase-low-products`。orbit 比較は t_Ω↦c(η)⁻¹t_p、反変 Koszul 双対は Ω_p↦c(η)⁻¹Ω となり、既存の γ=[c(η)⁻¹] と一致する。f の変更は次数 scalar なので比は三乗倍だけ変わる。標的方程式の v 倍は t_p を v⁻¹ 倍、Ω_p を v 倍し、γ′=[v]γ と整合する。q=2 の局所計算により、この正準位相が一でないことを証明した。大域的な式 [D] は他の divisor の非分岐性を追加仮定する。

計算では有限分裂体上で実際の M と q_Y^R M[1] を表示し、内部次数 −1,−2,−3 の有限 Hom 模型、合成と contraction を求めればよい。重み零性により関係と最終比は元の体へ戻せる。単に可換側の通常の原点 stabilization に置き換えると二次包絡を誤り、m₃ を零と置くこともできない。coherent な中心線型性の全降下はこの評価式の前提でも結論でもない。

**非分岐性の有限データ判定。** source と回復した対が閉 fibre を含む良い integral 表示を持ち、Ω と Ω_p が直線部分束の生成元なら、指定された K-射影 Isom は有限対角により R 上へ延びる。有限自由生成元加群の射影同型を GL/G_m 完全列と Pic(R)=0 で持ち上げれば fΩ_p=uΩ、u∈R× となる（`lem:nfm-period-integral-presentation-unramified`）。幾何的 Isom の存在だけで K 上の切断を得たとしない。

この十分条件を各 divisor へ適用するには、低 Ext の自由性と底変更、積の integral transfer、関係束の階数、三次 relation の原始性と閉 fibre の良い条件を確認する。q=2 では全 n の低 Hom は自由だが、raw m₂* の階数は三だけ落ち、飽和後の Ω_p は z の一倍を含むため、この非分岐性の十分条件を満たさない。一般点の finite perfect spread だけでは指定した divisor の良い還元は保証されない。別の divisor では関係加群の飽和、有限行列の minor・Fitting ideal と三次関係の付値を調べる。

現行の T は σ^j≠1 (1≤j≤max(3,n−1)) を課す。n≥5 では ΔD≠0 にも位数四点の divisor があり、現在の入力保証はそこを除く。これは真の分岐や実中心の跳躍を示した結果ではなく、既存証明の適用範囲の不足である。将来の弱化では、全 O-復元の高次中心条件を要求する代わりに、相対低次数中心・境界評価 ε・滑らかな trace–Hessian 三次から graded Isom を有限な polarized cubic Isom の閉部分へ入れる方法を検討できる。q=2 自体は滑らかな点曲線を要求する既存 good open の外なので、そこへこの補題を直接適用してはいない。

### 次の着手方法：周期境界・coherent 中心作用・全型への拡張

第一に、β_n=γ̄_n/[D] の他の divisor を調べる。q=2 の全次元の orbit Hom、二次積・三次積の一次項、二次関係の飽和と source active 格子の比較、完備局所値 [D_R] は決定済みである。現行の小位数除外を含む ΔD 外の divisor で、同じ有限評価法の積分模型・飽和・primitive 関係・smooth potential による同型延長を検査する。非分岐性を示せれば、半古典条件と UFD 判定から大域式 γ̄_n=[D] が従う。並行して三次位相体 M 上の α の index を求め、標識付き最小次数三／九を決める。n=3 の fractional Serre trace は大域比較の別経路として保持する。

第二に、一意な強化点型 class を有限代数的核の coherent な中心線型性へ接続する。可換側の q_Y=Li_C^* は source の中心作用を代用しない。全群分類を前提とせず、他の full class については既存の T-軌道と数値中央化群を使う。全次元の H_p=1 と五次元の ε=id は既に確定した範囲である。

第三に、非分裂の全 n≡1 mod3 における強化点型最小九と、rotation による全型の上界三を基準に、他の軌道の K 核と点型を固定した一般体の index を調べる。四次元の指数九族の全型最小三は決定済みだが、高次元には同じ下界をまだ得ていない。共通な良い開の外と全 intrinsic 成分の問題も保持する。

### 比較核の Euler 数値型と scalar index

核の同型類が選ばれた後の G_m-gerbe 上では、試験対象 A_i,B_j に対する混合 Hom は重み1の perfect 複体となり、determinant の重みは Euler 数 χ_ij である。その gcd=d>0 によって dα=0、μ_d による band の縮小を得る。体上では各 cohomology の rank 自体が ind(α) の倍数なので ind(α)|d まで分かる。period と index を同一視していない。

固定入力B `papers/sections/generic_recovery/generic_descent.tex`, `rog:prop:euler` の三次 stabilization の Euler 数は

\[
 \chi_{N,r}=\sum_{s\equiv-r\ (3)}(-1)^s\binom Ns,\qquad
 \gcd_r\chi_{N,r}=3^{\lfloor(N-1)/2\rfloor}=d_n.
\]

gcd の証明は Z[t]/(t³−1) で p_(N+2)=−3t p_N、p₁=1−t、p₂=1−2t+t² から従う。m=floor((N−1)/2)、r_N≡−m mod3 とすれば χ_(N,r_N)=(−3)^m で、一つの determinant または双対が重み d_n を持つ。元の Euler 公式自体は既知入力である。

split 正則表示 chart で augmentation の stabilization κ_nc と可換 Koszul stabilization κ_Y を取る。混合 Euler 条件 χ(κ_Y,Φ_P(κ_nc(r)))=χ_(N,r) は開閉条件であり、CF の剰余恒等と **任意の二つの有限 rank MF** の proper Hom (`window.tex`, `tw:lem:proper-hom`) から支配 trait 上で成り立つ。Φ(κ_nc)=κ_Y という対象の同定は不要。形式 Laurent 体上の frame の後で、核・図式・試験対象・混合 Hom を有限表示に降ろし、閉点へ特殊化すると同じ数値型の有限比較核を得る。

この数値型で同型類を整合的に選んだ後、split 一般点では ind(α)|d_n。表示 gerbe β は階数3・重み1の束 V/U の End によって次数3の Azumaya 代数を持つので、その分裂体を取る追加次数は1または3。n≢1 mod3 ではβ=0。従って既に同型類が体K上にある場合、ind(α_K)|3^(floor((n+1)/2)+ε_n)、ε_n=1_{n≡1 mod3}。これは比較核全体の被覆次数を第一段階の選択前から抑える主張ではない。

特殊 Hom⁰(κ_F,κ_F)=k から重み1の線束を得る近道は使えない。入力の外積代数表示から Ext¹(κ_F,κ_F)=Λ³k^N≠0 であり、特殊で一致する二変形対象の Hom⁰ は一般に跳び得る。確実に保たれるのは全 perfect Hom の Euler rank である。

**既存の Euler 格子だけでは改善できない。** ρ³≃[2] と比較核の rotation 適合性から、全 rotation 軌道の混合 Euler 行列は χ_(N,i−j) の circulant 行列となる。両側の三つの stabilization の整数 K₀ span の pairing ideal は正確に d_n Z（`prop:nfm-kernel-euler-orbit-lattice`）。全 twist、cohomological shift、有限直和、有限回の cone を加えてもこの gcd は減らない。これは実際の Brauer index が d_n に等しいという下界ではない。thick 生成には新たな idempotent summand が含まれ、その類は元の整数 span に入るとは限らない。例えば Perf(k×k) の regular module G は thick generator だが Z[G] は K₀≃Z² の対角部分群であり、χ(G,G)=2 に対して一つの summand G₁ は χ(G₁,G₁)=1。新しい最高次線束の構成は、active 制限と正準的な cohomology によって、既存の整数 span の Euler pairing とは異なる試験束を得る。新たな summand、点・線型切片の residual projection、実際の active 比較も候補だが、それぞれ降下と Euler 数の別の証明が要る。

**符号被覆は既に選んだ核の scalar index を減らさない。** 同型類が体 K 上に既に整合的に選ばれ、scalar gerbe α_K が定まっているとする。現在の bound により d=ind(α_K) は三の冪。有限拡大 L/K の次数 e と d′=ind(α_L) に対し、d′|d、d|ed′ が成立するので、3∤e なら d′=d（`cor:nfm-kernel-prime-to-three-invariance`）。j≠0,1728 上の標準二重被覆 D の各体成分は次数1または2であり、この scalar 障害を改善しない。選んだ同型類の核が D_K 上で存在することと K 上で存在することは同値である。平面同型の十八重被覆 I_K の**全体**で核が存在するなら、各体成分の次数が d の倍数なので d|18、従って d|9。I の一つの未指定成分上の存在だけでこの結論を使わず、同型類自体を D 上で初めて選べる場合とも区別する。

### 最低 Hom による核の剛性化

これは twisted sheaf の標準的な Brauer–Severi 構成を比較核へ適用するもので、大きな新規定理として数えない。整合した核の同型類を実現する G_m-gerbe q:G→S と普遍核 P、大域試験対象 A,B を固定する。E=RHom(B,Φ_P(A)) は重み1の perfect 複体である。ある a について H^i(E)=0（i<a）、V=H^a(E) が階数 r>0 の局所自由層であり、消滅と V の形成が任意底変更に両立すると仮定する。

局所核 P_T と H^a(E_(P_T)) の至る所非零な切断 v の対 (P_T,v) は、S 上相対次元 r−1 の Brauer–Severi 空間 Z_(A,B,a) で表され、その上には普遍同値核がある。証明は次のとおり。gerbe を中立化した chart S_i で核 P_i を選ぶと、核の変化は底線束による twist であり、対の局所 moduli は [(V_i∖0)/G_m]=P(V_i) となる。ここでは部分直線の規約を用いる。scalar cocycle は射影化後に消えるので、射影束は Brauer–Severi 空間 Z に貼り合わさる。

G 上の P_G(V) の tautological line L⊂V は重み1を持つ。従って P⊗L⁻¹ は重み零で Z へ降下し、実際の普遍核 P_Z を与える。L→V を twist した切断は scalar 自己同型を消す。L^(−r)⊗det V も重み零の相対 ample 線束であり、Z→S の射影性を与える。H^a が最低次なので、hypercohomology の spectral sequence により Γ(T,H^a(E_(P_T)))=H^a(RΓ(T,E_(P_T)))。単に cohomology sheaf の任意の切断が同次数の derived Hom へ持ち上がると仮定していない。全構成は上の仮定を保つ底変更に両立する。

S=Spec K なら Z(K)≠∅ と α_K=0 は同値。K-点から普遍核を制限すれば中立化し、逆に核が K 上にあれば V の非零ベクトルを選べる。従ってこの構成は元の K 上の核の存在や、有限比較被覆の次数改善を主張しない。また単に Hom の**直線**をデータに加えるだけでは scalar inertia は残る。実際に非零ベクトルを付けることと、上記の tautological twist による核の降下が必要である。有限型の整な底では、非零の perfect Hom の cohomology を平坦にする縮小で仮定を満たせるが、核の同型類の第一段階をその縮小だけで選んだとはしない。

体上で a(P)=min{i:H^i(E(P))≠0} と置けば a(P[2m])=a(P)−2m。従って a∈{0,1} という規格化は各偶 shift 軌道でただ一つの代表同型類を選ぶ。これは低 Nat 積が検出しない偶 shift の曖昧さを除くが、全 rotation-compatible 自己同値 torsor の切断や、Hom 階数が跳ぶ族全体の代数的な選択は与えない。

### active 比較による index 改善の十分条件

同型類を既に選んだ比較核 gerbe G→S 上で、active な三変数比較を functorial に定め、元の scalar λ が active 核にも同じ λ として作用すると仮定する。さらに S 上の active 試験対象 A₀,B₀ に対する三つの mixed Hom

\[
 E_i=R\operatorname{Hom}(B_0,\Phi_{P,0}(A_0(i))),\qquad i=0,1,2
\]

が G 上 perfect で、Euler rank が (0,3,−3) であると仮定する。このとき E_i は重み1、det E_i の重みは0,3,−3なので、既存 determinant lemma から 3α=0。体上では各 cohomology の rank が index の倍数だから ind(α)|3 まで従う。これは全 n に一様な**追加仮定付きの判定**であり、これらの active 核と perfect Hom を元の代数的 gerbe 上へ構成することは未解決である。

完備 flow の中心係数商はこの追加構造の形式的な候補を与える。ただし一般 split 係数体上では全 active intertwiner が存在しないので、同体上の実際の full 核を常に actual active 同値へ送る構成を、何の追加条件もなく仮定できない。完備化では点障害が消えることと区別する。一方、最高次線束による本文の評価は、full kernel と可換側の実際の q_Y だけを使うので、この active 核の assignment を必要としない。次の二つの補助経路は、active 比較自体や coherent な中心作用を研究する際に有効であり、主評価の証明の欠落部分ではない。

### genus-one 比較核の一般的な index 補助

E,C を体 K 上の滑らかな幾何学的連結 genus-one 曲線とし、類 α の G_m-gerbe 上に重み1の perfect equivalence kernel Q があるとする。このとき

\[
 \operatorname{ind}(\alpha)\mid
 \gcd\bigl(\operatorname{ind}(E),\operatorname{ind}(C)\bigr),
\]

ただし曲線の index は閉点の次数の gcd である。証明は Euler pairing の標準手法である。M=Φ_Q(O_E) の幾何的な rank・degree を (a,d) とする。代数閉体上の数値 K₀≃Z² で同値は primitive vector (1,0) を primitive vector へ送るので gcd(a,d)=1。次数 e の閉点 z∈C に対し、重み1の perfect 複体 RHom(O_C,M)、RHom(O_z,M) の Euler 数は d、−ea。従って ind(α) は gcd(d,ea)=gcd(d,e) を割り、全閉点について gcd を取れば ind(α)|ind(C) を得る。逆核は重み−1で同じ index を持つので E についても成立する。

C に実際の正次数 ℓ の線束があれば Riemann–Roch によりその次数の有効因子があり、ind(C)|ℓ。split 平面三次の O_C(1) なら3を得る。Brauer–Severi 平面内の三次に偏極**類**しかなければ、この議論で使える反標準線束 O_C(3) の次数は9であり、無条件に3へ戻せない。これは一般的な補助判定で、新規性を主張しない。本文の full 核の最高次線束の存在とは仮定が異なる。

### 有限比較四角の降下と同型類の障害

四つの smooth proper dg 圏 A,B,A₀,B₀ と、absolute perfect な実際の関手 q_A:A→A₀、q_B:B→B₀ を固定する。full 同値核 P、active 同値核 Q と可逆な2-cell q_BΦ_P≃Φ_Qq_A は有限な perfect 図式である。核・逆・単位・余単位・2-cell を有限生成係数環へ降ろし、cone の消滅を縮小してから閉点へ特殊化すれば、同じ有限図式を有限分離拡大上に実現できる。q_A,q_B の absolute perfect 性は smooth な源と compact な像から確認し、相対包絡代数上の perfect 性を仮定する必要はない。

ただし、この有限実現は元の底での compatible **diagram class の選択**ではない。R=q_BΦ_P≃Φ_Qq_A とすると、図式の自己準同型は

\[
 \operatorname{fib}\bigl(R\operatorname{End}(P)\oplus
 R\operatorname{End}(Q)\longrightarrow R\operatorname{End}(R)\bigr)
\]

で制御され、H⁻¹End(R) が H⁰ の自己同型に寄与し得る。P,Q の通常の自己同型がそれぞれ scalar G_m であるというだけでは、図式の stabilizer が対角 G_m とは言えない。Ext⁻¹(R,R) の消滅などを確認するか、元の scalar gerbe 上の重み1 active 核の存在を別途仮定する必要がある。

**class 選択が自動でない例。** 次数 d>1 の非分裂 central division algebra D を取り、A=Perf(K)、B=Perf(D)、A₀=B₀=Perf(K) とする。q_A は K^d との tensor、q_B は underlying K-complex を取る関手である。全圏は smooth proper、全関手は perfect kernel を持ち、その像は active 圏を thick 生成する。幾何的 full Morita class は K 上不変で、実現 gerbe は符号を除き [D] である。代数閉体上の単純 D-module S と active な線 Q の間の square は、underlying S≃K^d⊗Q の同型である。その diagram class の選択は D^op≃M_d(K) の分裂同型を与え、これらは K-point を持たない PGL_d-torsor をなす。active 側に Euler 数1の対象があっても、full gerbe の index d は消えない。full class の選択・有限図式・生成性の三つだけから、同じ gerbe 上への active 核の assignment は得られない。

### graded-center balancing の有限性：有効な評価と未完成の適用

多項式中心 C=k[u₁,…,u_r] 自体には exterior coalgebra の reduced cobar による有限 quasi-free associative dg 解消がある。非空集合 I ごとの生成元 x_I は cohomological/internal 次数 (1−|I|,|I|) を持ち、dx_ij=x_ix_j−x_jx_i。生成元数は2^r−1である。これは Shoikhet の既知の Koszul 解消であり、二つの中心作用を coherent に balance する相対問題とは異なる。

R′=R[u_L,u_R]、z_i=u_(i,L)−u_(i,R) とすると対角の Koszul dg algebra は K=R′⊗Λ(ε_i)、|ε_i|=(−1,1)、dε_i=z_i である。R′-complex として有限自由でも associative algebra として cofibrant ではない。r=1 の相対解消は

\[
 Q=R'\langle q_1,q_2,\ldots\rangle,\quad
 |q_m|=(1-2m,m),\quad dq_1=z,\quad
 dq_m=\sum_{i+j=m}q_iq_j\ (m\ge2)
\]

と無限に続く。d²=0 は全 q_i が奇次数であることと z の centrality から従い、ε への写像は内部次数ごとの filtration で quasi-isomorphism と分かる。相対代数 C が homotopically finitely presented なら derived 対角基底変更後の exterior algebra も smooth となるが、前述の augmentation module の無限 Tor がこれを妨げる。従って C 自体の有限解消や absolute perfect 性から、相対 balancing の有限表示を推論できない。

一方、**実際の balancing の模型を別途同定するという仮定の下で**、内部次数は有限化に有効である。E_t=RHom(P,P(t))、E₀,E₁,E₂ が ordinary base change 後も共通の cohomology 下限 b を持つ perfect 複体で、E_(3q+s)≃E_s[2q] とする。strict C^e-linear、strictly unital な curved-bar 模型において

\[
 V_m=\operatorname{Hom}_{R'}((K/R')^{\otimes m},E)_{\mathrm{int}=0}
\]

の associated graded は、total exterior degree t≥m に対応する E_t[−t] の有限直和である。t=3q+s より H^ℓ(E_t[−t])=H^(ℓ−t+2q)(E_s)、従って

\[
 H^\ell(V_m)=0\quad\text{if}\quad
 \ell<b+\lceil m/3\rceil.
\]

arity m の obstruction は H^(2−m)、高次の選択は H^(1−m−j)（j≥0）に入るので、m>max{1,2−b} では全て消える。この obstruction tower が kernel balancing の空間を表し、period・derived End・composition が filtered 底変更と両立すると示せれば、有限 arity 部分の通常の係数降下と組み合わせられる。高次 Taylor 成分を零に置くという意味ではなく、延長の選択空間が可縮になるという意味である。dε_i=z_i は unit 成分を持つため、普通の augmented bar ではなく curved bar が必要となる。

振幅評価自体には上の紙上証明があるが、実際の rotation 付き Morita 核の moduli と strict C^e-linear curved-bar 模型の同定は未完成である。任意の非有界 derived base にわたる一様切断、relative envelope の HFP、全代数的比較核の coherent 中心線型性を結論していない。次の着手はこの模型同定と filtered End の底変更であり、本文の最高次線束による指数評価から独立した課題である。

**内部次数を忘れると有限化が失敗する例。** z=0 の上の Q に対し、2-periodic algebra E=k[v,v⁻¹]⊗Λ(θ)、|v|=2、|θ|=−1、d=0 を取る。任意の列 (a_m) が q_m↦a_mθv^(1−m) という dg algebra map を与える。polynomial de Rham homotopy の一般形は a_m(s)θv^(1−m)+ds b_m(s)v^(−m) であり、積の交差項は i,j の交換で相殺するので a′_m(s)=0 を得る。従って全 a_m が homotopy invariant であり、k(t₁,t₂,…) 上で a_m=t_m とすればどの有限生成部分体にも降りない。これは graded cubic への反例ではなく、内部次数を捨てた periodic properness だけでは有限表示が得られないことを示す。双次数として (3)≃[2] を保持すると、上の任意列は内部次数を保てない。

## 7. 一次資料の確認箇所と引用上の注意

本文の引用文献の書誌とURLは `papers/references.tex`。以下は議論に直結する確認箇所と、ノートだけの補助経路の一次資料であり、全論文を監査したという一覧ではない。

- Dyckerhoff, *Compact generators in categories of matrix factorizations*, Duke Math.J.159(2011),223–274、[arXiv:0904.4713v5](https://arxiv.org/pdf/0904.4713)、§5.6、Theorem5.8（著者版p.31）。2026-11-22に一次PDFで、一変数W=Σr_i x^iのunital minimal A∞模型のm_i(θ,…,θ)=±r_iを確認した。中央因子cu³の三項係数に用い、本文では2×2行列により直接再検算する。非可換ambient全体のformalityをこの定理から導いていない。既存keyは `ROGDyckerhoff`。
- Willumsgaard, *Obstructions for Associativity in Stable Homotopy Theory*, [arXiv:2605.11390v1](https://arxiv.org/abs/2605.11390v1)（2026）、Theorem3.3、Lemma3.11。確認済みの固定unitのA_n障害塔を、安定な境界核圏のoppositeを通じて固定counitへ適用する。非空fiberのhomotopy群がH^(2−n−i)RHom(K,J^n)となるshiftを保持する。一般理論と、本族でarity二・三だけが残るsector計算を区別する。keyは `CMOWillumsgaardAssociativity`。
- Christ, *Spherical monadic adjunctions of stable infinity categories*, [arXiv:2010.05294v3](https://arxiv.org/abs/2010.05294v3)（2022）、Proposition1.11、Theorem4.1、§4.1、Example4.10。確認済みのstable Kleisli模型と、underlying monadおよびunitだけでは乗法が決まらない例を参照する。本族では実随伴とsplit-generationからcoKleisli代数を作り、全coherenceの比較を別に証明する。keyは `CMOChristSphericalMonadic`。

- Druel–Pereira–Pym–Touzet, *Bondal's conjecture in dimension five*, [arXiv:2606.03424v1](https://arxiv.org/html/2606.03424v1)（2026-06-02）。公式本文のTheorem1.2、Corollary1.3（PDF p.2）、§4.4 Theorem4.3の記述を確認した。次元2r+1のFanoではD_(2r−4)(π)に次元2r−3以上の既約成分が存在する。本文Theorem4.3は一般階数2rを仮定し、導入で低階数を既知結果へ帰着する。五次元での正次元零成分の存在と、本稿の全孤立成分の排除を区別する。外部証明全体の監査を行ったという確認ではない。
- Gualtieri–Pym, *Poisson modules and degeneracy loci*, Proc. London Math. Soc. (3)107(2013),627–654、[DOI](https://doi.org/10.1112/plms/pds090)、[arXiv:1203.4293v1](https://arxiv.org/abs/1203.4293v1)。Conjecture1.1（PDF p.2）、導入に掲げられたTheorem7.13（PDF p.3）の記述を確認。上の定理番号はarXiv v1に従う。偶数次元の上位退化軌跡と四次元のBondal予想を扱い、ここでも十分大きい成分の存在が結論である。smooth cubicの孤立零点の3整除制約をこの既知結果の帰結とはしない。
- Okawa–Uehara, *Exceptional sheaves on the Hirzebruch surface F2*, Int. Math. Res. Not. IMRN2015(23),12781–12803、[DOI](https://doi.org/10.1093/imrn/rnv079)、[arXiv:1409.7813v2](https://arxiv.org/abs/1409.7813v2)。Lemma4.2（p.18）のsmooth projectiveなHirzebruch曲面の変形、Remark1.2（p.3）の(−2)-curve上のspherical objectを一次本文で確認。これらの既知幾何と、smooth properな両側だけでは特殊同値が従わないという本ノートでの使用を区別する。
- Keller, *Derived invariance of higher structures on the Hochschild complex*, August 2003, last modified 2018-05-16、[著者PDF](https://webusers.imj-prg.fr/~bernhard.keller/publ/dih.pdf)。Introductionと§3.2の主定理でHochschild cochainの導来不変性を確認。通常の代数ではHH⁰(A)=Z(A)であり、指定混合因子のambient Morita可換化を排除する際に使う。curved/MF圏・射影残余圏の比較を否定する入力ではない。

上の一次文献とcubic hypersurface / cubic fivefold / isolated Poisson zerosについての限定検索では、孤立零点の一般次元の3整除制約と同一の主張をする先行一次資料は特定できなかった。検索の不発を先行結果の不存在の証明とせず、本定理および被約反例の文献上の新規性は未確認とする。

- Etingof–Ginzburg, JEMS12(2010), Theorem3.3.2 / §9（印刷p.1414）：三変数 potential の PBW・中心元・Rains の有限中心公式。今回のεの非消滅は公刊式の斉次部分を直接使い、係数恒等式を独立に記号検算した。Proposition8.1.1と式(8.1.3)には形式量子化の中心とPoisson中心の同型が既にある。§8.1の証明（印刷pp.1407–1408）はunimodularityによる相対形式Jacobian potentialの認識も含み、これらの存在そのものを新規とは数えない。現行のtrace–Hessian処方は有限パラメータと相対降下について位置付ける。https://ems.press/content/serial-article-files/31746
- Dito, *Kontsevich star-product on the dual of a Lie algebra*, arXiv:math/9905080, §2 equation (3), §3 Theorem2：§2 の式は一般 Poisson tensor の二次星積であり、eye 項を含む。§3 Theorem2 も一般 Poisson 構造の星積に対する Weyl 化である。Lie 代数に限定される後続の Gutt 星積との比較とは区別する。本稿の ρ₂F は §2 の式の線型形式の冪への適用と polarization から直接求める。[一次資料](https://arxiv.org/abs/math/9905080)。
- Shoikhet, *Vanishing of the Kontsevich integrals of the wheels*, arXiv:math/0007080, §1.3 Theorem、§2.3.1：harmonic-angle の内向き wheel の重みの消滅と中心写像を確認。Weyl 模型への変換で現れる二次項と、同じ formality の中心写像の項を区別する。固定 gauge を指定せず係数 1/24 を普遍的な未標識量と呼ばない。[一次資料](https://arxiv.org/abs/math/0007080)。
- Shoikhet, *Kontsevich formality and PBW algebras*, [arXiv:0708.1634v2](https://arxiv.org/pdf/0708.1634) (2007), §1.3 pp.6–7：symmetric algebra を exterior coalgebra の cobar で解消する既知の構成と二変数の式を確認。多項式中心自体の有限解消に用い、相対 balancing の有限表示をこの結果からは結論しない。
- Burke, *Strictly unital A∞-algebras*, [arXiv:1801.06943v1](https://arxiv.org/pdf/1801.06943) (2018)：普通の可換基礎環上で、unit splitting と curvature により augmentation の欠如を扱う枠組みを確認。ノートの curved-bar 模型の出典であり、内部次数による有限 arity 評価や実際の kernel moduli への適用を同論文の定理として引用しない。
- Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*, Enseign.Math.55(2009),235–273、DOI 10.4171/LEM/55-3-3、§2 Lemma2.1と式(4)–(5)・p.240：Hesse正規形とWeierstrass係数を公刊PDFで確認。パラメータ(t₀,t₁)=(1,3λ)から本文のj式を得る。係数式からjの規格化も厳密検算した。[公刊一次資料](https://ems.press/journals/lem/articles/12146)。
- Fisher, *Testing equivalence of ternary cubics*, Algorithmic Number Theory, LNCS4076(2006),333–345、[著者PDF](https://www.dpmms.cam.ac.uk/~taf1000/papers/testeqtc.pdf)、[DOI](https://doi.org/10.1007/11792086_24)。Theorem1.1 の Weierstrass 規約・不変式環 C[c₄,c₆]、Lemma2.2 の代数閉体上の proper equivalence、Lemma2.3 の証明の微分付き楕円正規曲線の自己同型E[3]、Theorem2.5・Lemma2.6 の微分の変換、§4 の Hesse 不変量を確認。本文の g_(p,q) へは a=p/3,b=−q/3 と置換する。proper projective stabilizerの位数9と、sign stabilizerの指数二に使用し、SL₃内の中心μ₃を重複して数えない。さらに著者稿§9.5「Reduction of Ternary Cubics」（PDF pp.12–13）の中央拡大 μ₃→H₃→E[3] と非可換な位数27の群を原文確認し、一般三次の H_g の記述に用いる。full ambient の中央化群 GL_r と混合定数降下は本文で別に証明する。古典的不変量・軌道分類・三捩れ自己同型は既知であり、混合三角性と正確な残余次数18への応用と区別する。
- Stacks Project, Lemma10.49.3, [Tag0FWF](https://stacks.math.columbia.edu/tag/0FWF)：代数閉包への底変更で整であることと幾何学的整性の同値を一次本文で確認。有限 torsor の定数降下で、代数閉体上の有限体因子をさらに定数拡大しても整性と体拡大次数が保たれることに用いる。torsor の降下自体は本文で証明する。
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
- Banks–Panzer–Pym, *Multiple zeta values in deformation quantization*, Invent.Math.222(2020),79–159、Corollary1.3・§§6.1–6.2：harmonic-angle graph weights の既知の厳密計算。五次 tensor の評価はこの入力を利用し、積分の再計算を本研究の成果に数えない。[刊行版](https://doi.org/10.1007/s00222-020-00970-x)、[著者稿](https://arxiv.org/abs/1812.11649v1)、[2022年訂正](https://doi.org/10.1007/s00222-022-01122-z)。
- Buring, *The action of Kontsevich's graph complex on Poisson structures and star products: an implementation*, Mainz 博士論文(2022)、§§3.4.1–3.4.2（pp.74–76）、§3.5（p.89）、§3.6.4（pp.103–105）：グラフの標識・自己同型・星積の規約と著者公開データ。本稿は `star5.txt` と `kontsevich_2_k.txt` / `weights_kontsevich_2_k.txt` を照合し、線型二入力に必要な73項だけを出典・入力ハッシュ付きで保持する。[学位論文](https://www.rburing.nl/gcaops/gcaops-dissertation-rburing.pdf)、[著者データ](https://www.rburing.nl/gcaops/)。第三者の評価器の実装自体は収録せず、保存した数値重みと辺データを独立の有理数評価器で再現する。
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
- BFK, *A category of kernels for equivariant factorizations and its implications for Hodge theory*, Theorem5.39 **一般式**とその証明、印刷pp.82–84：sector の Koszul コホモロジーと parity。Lin–Zhang Theorem3.5 の parity にある内部 twist は cohomological degree と読む。同所の引用番号5.9は原著では5.39。BFK p.83 の簡約表示にも奇数側 Jac を残す誤植があるため、一般式の H^(2l+1) と孤立臨界点なら H^0 のみという p.84 の証明を根拠にする。さらに [arXiv:1105.3177v5](https://arxiv.org/pdf/1105.3177) の Definition6.11・Theorem6.13（PDF pp.69–74）で rotation の dg bimodule レベルの同定を確認。Remark6.14 の剰余体の shift は Galinat の window1 と混用しない。
- Pirozhkov, arXiv:2208.13604v1, Lemmas5.1,5.2：非対角 Hodge diamond と実際の幾何的 KS 単射。Lemma5.2 は n=3 でも使えるが、同稿の大域 Torelli Theorem5.3 の三次条件は n>3。
- Huybrechts–Rennemo, Algebraic Geometry6(2019), Proposition3.5 / Remark3.8：四次元の HH²=22 と幾何方向20。
- Lurie DAG X, Theorems5.1.9,5.3.16 / Proposition5.3.21、Blanc–Katzarkov–Pandit §3.3,§4.3：tame の1-proximate性、hull の Hochschild 制御、actual→hull の (−1)-truncated性。BKP の一変数形式生成結果を任意基底の定理へ読み替えない。
- Kuznetsov の fractional CY 論文と Lin–Zhang Proposition3.7：Serre/rotation の算術。Lin–Zhang Theorems4.1,5.1 の categorical Torelli は既知入力。
- Orlov, *Derived Categories of Coherent Sheaves and Triangulated Categories of Singularities*, [arXiv:math/0503632v3](https://arxiv.org/pdf/math/0503632) (2009), Theorems2.5(iii),3.11(iii)：Theorem2.5(iii) は非可換 connected graded Gorenstein algebra の parameter a=0 も扱う。可換な d=N、特に N=d=3 で graded MF と滑らかな plane cubic の D^b(coh) を比較する場合と併せて、三変数の proper Hom に用いる。N≥5 の window 定理の適用範囲を広げたとも、体上の同値だけで相対底変更が従うとも扱わない。
- Galinat, *Orlov's Equivalence and Maximal Cohen-Macaulay Modules over the Cone of an Elliptic Curve*, [arXiv:1302.1383v1](https://arxiv.org/pdf/1302.1383) (2013), §1.1・Lemma1.2・§1.4・Lemma2.7の証明：Φ=Φ₁、O_C と irrelevant ideal A_(≥1) の対応、Φ∘T_O∘tensor O(1)≃(1)∘Φ を同じ規約で確認。0→A_(≥1)→A→K→0 と合わせて κ_act↔O_C[1] を用いる。最高次線束型の負 rotation 計算は本文で別に証明する。
- Stafford–Van den Bergh, *Noncommutative curves and noncommutative surfaces*, Bull.Amer.Math.Soc.(N.S.)38(2001),171–216、[arXiv:math/9910082v2](https://arxiv.org/pdf/math/9910082)、§3・PDF p.10・式(3.1)：右 THCR の shift s=σ_*∘(−⊗L) を原著の添字まで確認。σ_* と σ^* の区別を点の平行移動と rotation の共役式に用いる。引用 key は `NFMStaffordVdB`。
- Burke–Stevenson, *The derived category of a graded Gorenstein ring*, [arXiv:1507.00830v1](https://arxiv.org/pdf/1507.00830) (2015), Definition5.1、Lemma6.2、Theorem6.4(3)：Gorenstein 条件・χ と、parameter a=0 の任意の window i における相互逆同値を確認。指定 source active 商の noetherian 性・有限 injective dimension・次数零環の有限大域次元は `lem:nfm-active-dvr-gorenstein`、相対 dg window の底変更は `prop:nfm-relative-active-window-basechange` で検証した。境界の full 可換三次には別に Theorem6.4(1), i=1（原著pp.18–19）を用いる。これは A₀が regular DVR、a=n−1>0 の場合を含み、Proj の滑らかさを要求しない。隣接する窓の mutation と F の自己交叉周期を組み合わせた低 Hom 計算への適用を、既知の Orlov 比較そのものと区別する。
- Preygel, *Thom-Sebastiani & Duality for Matrix Factorizations*, [arXiv:1101.5834v1](https://arxiv.org/pdf/1101.5834) (2011), §2.2（pp.5–6）、Theorems4.1.3,4.2.2,4.2.3：literal な R-線型性と Perf(R)-module category の区別、および support・periodic coefficient を伴う相対構成を確認。本稿の非可換 graded-center 切断や代数的核の降下へ無条件には適用していない。
- BFK, *Orlov spectra: bounds and gaps*, arXiv:1012.0864v3, Theorem5.15：孤立次数三特異点の三連続内部 shift による生成。前項の BFK 論文と区別する。
- Kuznetsov, *Derived categories of cubic fourfolds*, Theorem3.1：Pfaffian cubic と K3 の導来同値。

- Fraenkel, arXiv:1310.6083v2, Proposition4.1 / Theorem4.3：孤立特異点を持つ affine 超曲面の Poisson 延長を gradient の Koszul 複体で記述する。三次 n-fold のパラメータスキームの境界を主張するものではない。
- Carles, Ann.Math.Blaise Pascal3(1996), §8 Lemma8.35（p.60）、DOI 10.5802/ambp.67：Lie law の変形の非零二乗零パラメータ。
- Carles–Márquez, Ann.Inst.Fourier61(2011), §3 Theorem3.2、Propositions3.9,3.10、DOI 10.5802/aif.2620：Lie law の Jacobi スキームの局所・大域冪零元と明示例。本稿の次数2という意味と冪零指数を区別する。

関連する近刊には Bricalli, *Linear Spaces in Hessian Loci of Cubic Hypersurfaces*, Mediterr.J.Math.23(2026),173、[DOI 10.1007/s00009-026-03169-1](https://doi.org/10.1007/s00009-026-03169-1)、[arXiv:2603.23207v1](https://arxiv.org/abs/2603.23207v1) がある。Definition1.3、Lemma1.8、Theorem1.5 の Thom–Sebastiani/Hessian/apolar の関連を確認した。同 Theorem1.5 が前論文を Theorem2.3 と呼ぶ箇所は、前論文の公刊版では Theorem3.4 に対応する。これらの Hessian 幾何の既存結果と、本稿の Jacobi 方程式全体の局所構造を区別する。

Lie algebra law の Jacobi スキーム一般に非被約性があることは既知である。また本稿の二次階数の上界、N=9,10 の最大性、および差330という数値も上記の既存研究に由来する。「Jacobi スキームに初めて冪零元を見つけた」あるいは「330という二次の不足次元を初めて計算した」という主張をしない。

現在証明を持つ寄与候補の中心は、全 O-同値の係数降下と局所模型 stack、全非空開に残る表示障害、相対点対応からの中心商復元、trace–Hessian と強い lift による Poisson 開の逆構成、残余復元との比較障害、混合 trace を含む代数的補正の降下・一般次数9、全混合五次 tensor と残余四次 potential、全次元に一様な四次比較障害、さらにそれを除く全 O-同値共変な有限補正である。c₂の消滅・偶奇性・形式 support 保存と split 族での補正後残余比較も保持する。一般混合係数の代数的残余三次・射影 Poisson 射と被覆上の Ku 比較、点微分による自然な符号商射と標準二重被覆上の full lift、さらに反対不変性・九次中間被覆・全次数の有限混合三角性による正確な一般次数18と、符号二次類の active 基底への降下・反対被覆の twist 構造は、明記した固定入力の下で本文に証明した。比較核には最高次 cohomology が線束となる非空な型を構成し、full class 選択後に split 一般点で index が3を割ること、Picard 障害としての同定と active 曲線・次数3切片による分裂を証明した。さらに determinant の三倍線束により、選択済み類の三分点被覆上の規格化核と J(S)/3J(S) による障害の記述を得た。従来 Euler 型の d_n 評価、全 rotation Euler 格子だけでは改善しないこと、三に素な被覆で選択済み核の scalar index が変わらないことも有効である。

符号については有限対角と有限混合多項式を使う近傍延長により、固定入力の下でχ_act=0と半古典規格化full射の次数9を証明した。追加の圏的延長仮定は使わない。独立に、指定中心商の相対THCR/window1と閉／一般底変更からm_P=p_resの非空型を得た。κとq_Yの内在的表示を通じ、この型は良い共通稠密開へ全O-降下する。一般jのHesse巡回例を実Sklyanin代数へ降下し、全n≥3の一般split係数点でδ_E(p_pt)のexact period=index三を得た。全active FM分類と合わせて全active intertwinerを排除し、さらにH_gのfull ambient作用によるI_scの分裂とparabolic共変性から、残余側も同じexact indexとなる。真の一般Hesse点を使う別の支配族は三分点torsorの連結九次性とASL₂(F₃)の216次Galois閉包を与える。

n=3,4では既知の全自己同値分類を核へ移し、定数Zのclass降下によって全full classの共通scalar障害を決定し、周期標識を忘れた全full比較の最小体次数三を得る。さらにE_P→q^RH⁰(qE_P)が同型となる随伴復元条件を加えると、全n≥3で非空な有限class torsor S_pと有限安定化群H_pを得る。この強化点型の実現stackはS_p×Pic_C^pで、最小実現次数はmin_i[K_i:K]ind(α_Ki)≤3|H_p|である。一般一ブロック族ではTate–Koszul忠実性により全n≥3でH_p=1、S_p=Spec(k_n)となり、強化型の同型類は正準的に一つとなる。奇数次元の数値的自明性も別の帰結として保持する。任意full classへは拡張しない。

非分裂の n≡1 mod3 では、二つの独立な Kummer 座標による曲線例を mixed theta 表示へ降下し、良い一ブロックの任意の非空開で点 Picard index 九を実現した。普遍点 gerbe の最小重み一階数も九で、表示安定化子が自明な共通開内では全該当次元の強化点型が未標識最小次数九を達成する。五次元では Clifford 半 rotation の平面非依存性と、二捩れの scalar 障害を次数2835の零 cycle で消す実核降下を得た。さらに相対・絶対 coevaluation の比較から O≃ρ⁻¹[1]、ε≃id を得た。全 n の H_p=1 は別の Tate–Koszul 忠実性による。二 mutation の具体的複体は他の対象作用を調べる資産として保持する。

指定周期の μ₃ 位相は n=3,4 の全 full class に共通である。相対規格化を適合させた最小次数三と、独立 target 尺度族の正確な九を保持する。唯一の φ_sc・t_sc・source Ω による正準 cube frame では、全 n の γ_sc,n は C(c₄,−c₆) へ降下し、半古典形式像は1だが q=2 の完備局所値は [D_R]。従って位相は全次元で非自明であり、位相体は三次と決まる。大域的な γ̄_n/[D] と次元間の一致、位相体上の scalar index は未決定。ΔD 外の非分岐性を追加仮定すれば大域式 [D] が得られる。n≥5 の任意 full class への位相共通性や全型の標識付き最小次数は未解決である。

高次元のclass問題では、元の体上の実核T=ρ⁻¹[1]を除いたG_ρ/〈T〉-torsorへの縮約と、classとT軌道のGalois安定化群の一致を証明した。奇数次元の数値像は六元群であり、残る群はG_ρ,0/〈[2]〉である。一般三次七様体の既知の球面対象からfull群のZ²とG_ρの無限指数が分かるため、低次元の全群の巡回性を全nへ拡張する方針は取らない。強化点型の正準classにより、点型を含むGalois固定軌道の存在も全次元で従う。他のfull軌道の分類は未決定である。

強いliftのKoszul手法、formalityと中心対応、既知の星積重み・wheel消滅、古典的Hessian写像・Aronhold不変式、残余MF模型そのものは既存入力と区別する。完備中心係数商の比較は選んだ相対flowの直接の補強であり、一般のcategorical base-change定理やその代数化ではない。重み1束からのAzumaya・Brauer–Severi剛性化、Picard gerbe、THCR・Orlov window、三・四次元のFM自己同値群分類、Iliev–Manivelの七次元球面対象、Toën–Vaquiéのboundednessと自己同値moduliは既知の入力である。本稿での最高次線束型、点の平行移動、projector核の一意性を通じたclass降下、指定MF周期のcoherenceとcube frameによる算術、随伴復元条件と有限H_p-torsorへの縮約と分ける。新規性の網羅的確認は未了。全intrinsic成分のモジュライ、特殊族でのPoisson対の延長と低Natの底変更の一致、良い稠密開の外での点型、n≥5の強化条件外の任意full核への適用、大域的な残余位相 γ̄_n/[D]、位相体上の scalar index、coherent graded-center比較の代数的降下は未完成である。全refined核でm_P=p_resを示したとはせず、一般次元での有限torsorへの縮約や選択後の規格化を未選択の全同値stackへ外挿しない。

保持する補助成果には、n=8 の**次数三以降を含む** Jacobi イデアルの決定、頂点の長さ330の平方零拡大と完備局所非分裂性、全 polar 方向を残した横断切片、直和の retraction による特殊三次の非零冪零例、実現する大域持上げ障害がある。二次階数だけでは得られない主張として証明を置く。全引用・被引用文献や MathSciNet/zbMATH の網羅的調査は未実施であり、以上の寄与候補、比較障害、残余形式認識の厳密な初出は継続して確認する。

勾配復元では Wang, *Deformation of Milnor algebras*, Pacific J. Math.305(2020),329–338、[DOI](https://doi.org/10.2140/pjm.2020.305.329)、[arXiv:1906.04891v3](https://arxiv.org/abs/1906.04891v3) の §3、Corollary3.2・Theorem3.3を確認した。Hwang, *Symmetrizer group of a projective hypersurface*, JMSJ78(2026),55–62、[DOI](https://doi.org/10.2969/jmsj/93469346)、[arXiv:2501.08633v1](https://arxiv.org/abs/2501.08633v1) の Theorems1.5,1.6、Propositions2.2,2.6、Corollary2.7を確認した。scalar symmetrizer による体上の一意性は既知であり、本稿の相対核・O-降下とは区別する。

Toën–Vaquié, *Moduli of objects in dg-categories*, Ann.Sci.ENS(4)40(2007),387–444、[DOI](https://doi.org/10.1016/j.ansens.2007.05.001)、[arXiv:math/0503269v5](https://arxiv.org/abs/math/0503269v5) の Lemmas2.8,2.10,3.25、Proposition3.20、Corollaries2.13,3.17,3.22,3.24を一次資料で確認した。Proposition3.20（公刊pp.433–434）は一つの指定generatorに対するHomのcohomology次元上界によるboundedness、Corollary3.17は接空間、Corollary3.22はsimple-object gerbe、Lemma3.25とCorollary3.24の証明（pp.437–438）は可逆核の開性を与える。これらを全Kuの三対象生成とHH¹=0へ適用して有限安定化群を得るのであり、TVの定理自体を新規成果としない。核側にはcategorical dualを使い、幾何学的dualがKuに属することを仮定しない。引用keyは `NFMToenVaquieModuli`。

smoothnessによるpseudo-perfectからperfectへの移行とfiltered descent、simple-object gerbeと全自己同値sheafを区別し、smoothnessのspreadingではperfectな源から対角への射を先に降ろす。Toën, *Anneaux de définition des dg-algèbres propres et lisses*, [arXiv:math/0611546v3](https://arxiv.org/abs/math/0611546v3) の Théorème1、F2–F6、Sous-lemme7（pp.8–9）も参照した。perfect moduleの係数降下とEndへのalgebra mapによる作用の記述を利用し、source HFPの仮定を無限な相対解消へ流用しない。一般のproper族のsmoothnessの開性を無条件に引用する使い方もしない。

Bergh–Schnürer, *Decompositions of derived categories of gerbes and of families of Brauer–Severi varieties*, Doc.Math.26(2021),1465–1500、[公刊PDF](https://ems.press/content/serial-article-files/26626)、Proposition4.10、Remark6.1、Theorem6.2・Remark6.3を確認した。さらに [arXiv:1901.08945v2](https://arxiv.org/pdf/1901.08945) の Proposition5.7（p.23）の weight-zero derived 降下と、§6 の式(6.1)・tautological trivialization を確認した。Hom 剛性化で用いる P⊗L⁻¹ の降下はこの既知の一般原理であり、本文・ノートでは必要な重みと cocycle を直接計算する。Lindberg–Pym の原生成元 q 比、Theorem6.9・Remark6.10も全次数の対数境界値に適用する範囲を再点検した。

点規格化と kernel index の一次資料：

- Fulton–Olsson, *The Picard group of M₁,₁*, Algebra Number Theory4(2010),87–104、[公刊PDF](https://msp.org/ant/2010/4-1/ant-v4-n1-p04-p.pdf)、[DOI](https://doi.org/10.2140/ant.2010.4.87)。§1・式(1-1)–(1-5)、pp.87–88で Weierstrass 微分・判別式の変換、Corollary2.4の証明p.91で j≠0,1728 上の μ₂-gerbe を確認。Hodge 線・modular forms は既知であり、残余尺度への応用と区別する。
- Poonen, *Varieties without extra automorphisms III: Hypersurfaces*, Finite Fields Appl.11(2005),no.2,230–268、[著者稿](https://math.mit.edu/~poonen/papers/projaut.pdf)。Theorem1.1（著者稿p.1）のAut=Lin、Theorem1.5と直前の開性（p.2）を確認。三次n≥3は例外に属さない。sourceと残余標的の一般慣性を除く箇所、およびLiuの群Z×Aut(Y)を一般点のZへ帰着する箇所で使用する。
- Stacks [Tag07S5](https://stacks.math.columbia.edu/tag/07S5), Lemma66.14.2：自由な有限局所自由群作用の scheme 商と torsor。本文では有限 étale 残余射を affine な標的へ縮め、その affine source 上の定数群 Z/2 の反対作用に適用する。
- Stacks [Tag037P](https://stacks.math.columbia.edu/tag/037P), Lemma10.47.8、[Tag0322](https://stacks.math.columbia.edu/tag/0322), Proposition10.158.9、[Tag05DW](https://stacks.math.columbia.edu/tag/05DW), §10.49：相対的な代数閉性からの幾何学的既約性、標数零の体拡大の幾何学的被約性、幾何学的整性と任意の体拡大後の整域性を確認。引用keyは `NFMStacksRegularFields`。active基底変更での一般次数保持と二次類の定数体への降下に使い、Kummer類の判定自体は本文で証明する。
- Knudsen–Mumford, *The projectivity of the moduli space of stable curves. I: Preliminaries on “det” and “Div”*, Math.Scand.39(1976),19–55、[DOI](https://doi.org/10.7146/math.scand.a-11642)。刊行情報を出版社で確認。twisted perfect 複体への適用は次項の本文で確認し、determinant の重み計算は原稿内で記す。
- Lieblich, *Moduli of twisted sheaves*, [arXiv:math/0411337v2](https://arxiv.org/abs/math/0411337v2)、§2.2.4・Definition2.2.4.1、§2.2.5。perfect twisted 複体の determinant、rank・period・index の関係を確認。書誌は確認した arXiv 版で固定する。
- Stacks [Tag074S](https://stacks.math.columbia.edu/tag/074S), Lemma11.7.4、[Tag074X](https://stacks.math.columbia.edu/tag/074X), Lemmas11.8.3–11.8.4：極大部分体の次数と分裂、有限分裂体の次数による index の整除。
- Stacks [Tag0DME](https://stacks.math.columbia.edu/tag/0DME), Lemma108.9.1：Picard stack から Picard functor への射が gerbe となることと、fppf 局所での線束の実現・同型を確認。滑らかな幾何学的連結曲線では scalar band は G_m。最高次線束からの band を保つ射により、選択済み kernel gerbe を m_P に沿う pullback と同定する。
- Stacks [Tag0BFG](https://stacks.math.columbia.edu/tag/0BFG), [Tag0BFH](https://stacks.math.columbia.edu/tag/0BFH)：abelian variety の整数倍写像の次数と、標数に素な倍写像の étale 性。相対 Jacobian の [3] の階数9・有限 étale 性に用いる。引用 key は `NFMStacksMultiplication`。
- Stacks [Tag0BQI](https://stacks.math.columbia.edu/tag/0BQI), Lemma58.10.7：正規な整 scheme 上の有限 étale 被覆の generic fibre への完全忠実性。対称点を含む正規近傍へ延長した二つのtorsor の同型を延ばすために用いる。近傍への延長そのものをこの補題で得るわけではない。引用 key は `NFMStacksEtaleNormal`。

有限対角による符号消滅の一次資料：

- Benoist, *Séparation et propriété de Deligne–Mumford des champs de modules d’intersections complètes lisses*, J. London Math. Soc. 87(2013),138–156、[公刊PDF](https://www.math.ens.psl.eu/~benoist/articles/separticle.pdf)、[arXiv:1111.1582v2](https://arxiv.org/abs/1111.1582v2)、[DOI](https://doi.org/10.1112/jlms/jds045)。Theorems1.6(ii),1.7（公刊p.140）は3を可逆にした底での平面三次のDM性と分離性を与え、対角はproperかつquasi-finiteなのでfinite。Lemma2.2(iii)（p.141）はDVR上の二つのsmooth polarized complete intersection間の指定generic ambient PGL Isomが延びることを明記する。境界計算では、特異な点三次ではなく、飽和active代数のcyclic potentialから回復した滑らかな三次へ適用する。
- Stacks [Tag0CMX](https://stacks.math.columbia.edu/tag/0CMX), Lemma102.3.7：局所有限表示stackのlimit-preserving性。射・同型・有限descent datumを有限係数環へ降ろすために使う。指定有理Isomの一意延長は本文で正規環への整性から直接証明する。

相対 THCR/window1 と Picard 反例の一次資料：

- Keeler, *Ample filters of invertible sheaves*, J.Algebra259(2003),243–283、Corrigendum507(2018),592–598、[arXiv:math/0108068v5](https://arxiv.org/abs/math/0108068v5)：Proposition7.2、Lemma7.6。訂正を含む版を確認。本文ではamplenessをDVR上で直接確認しており、訂正対象の旧Lemma3.3に依存するgeneric alterationは使わない。
- Burke–Stevenson の DVR 上の Gorenstein/window 入力は上記の同文献を参照。active a=0 には Theorem6.4(3)、full 三次の境界 a=n−1>0 には Theorem6.4(1)を用い、適用範囲を混同しない。
- Stacks [Tag0B91](https://stacks.math.columbia.edu/tag/0B91), Lemma36.30.4：proper flat有限表示射上のperfect複体の押下げと任意底変更。相対windowにはこの各次数の主張とMF余核の実際の比較図式を併用する。
- Milne, *Class Field Theory*, version4.03 (2020-08-06), [著者PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf)：III§4 Steps1–2（印刷pp.111–112）の巡回norm判定、IV§3 Theorem3.14（印刷p.137）のcrossed productとBrauer群。反例のfactor setをこれと照合した。
- Fisher, *On some algebras associated to genus one curves*, [arXiv:1707.08330v1](https://arxiv.org/abs/1707.08330v1)：Theorems1.1–1.2、Corollary1.4、§§6–7。genus-one曲線に付随するJacobian上のAzumayaとTate評価は既知の背景であり、今回の明示計算やfull比較核への応用と区別する。

全 active FM 分類・cup 表示・実 Sklyanin 実現の一次資料：

- Hille–Van den Bergh, *Fourier–Mukai transforms*, Handbook of Tilting Theory, LMS Lecture Note Ser.332 (2007), Chapter7、[著者稿](https://cantate.be/site/hille.pdf)、[DOI](https://doi.org/10.1017/CBO9780511735134.007)。Proposition4.2、Corollary4.3、Theorem5.3と証明。数値作用・点対象からの graph 認識と elliptic 自己同値の一般論を照合し、本稿では指定 rotation の centralizer、非閉体への実核の降下、相対 gerbe と周期標識を分けて証明する。引用 key は `NFMHilleVdBFM`。
- Ciperiani–Krashen, *Relative Brauer groups of genus 1 curves*, Israel J.Math.192(2012),921–949、[著者稿](https://web.ma.utexas.edu/users/mirela/BrauerGroups.pdf)、[DOI](https://doi.org/10.1007/s11856-012-0057-5)。Theorems3.1、3.7（pp.929–933）。Picard 障害の Tate 評価と有限 Weil cup の順序を確認。本稿の flex lift・I_sc 移送・選択済み full 核への適用と、既知の pairing 一般論を区別する。引用 key は `NFMCiperianiKrashen`。
- Cremona–Fisher–O'Neil–Simon–Stoll, *Explicit n-descent on elliptic curves. I. Algebra*, J. reine angew. Math.615(2008),121–155、[arXiv:math/0606580v1](https://arxiv.org/abs/math/0606580v1)、[DOI](https://doi.org/10.1515/CRELLE.2008.012)。§§1.1・1.3・1.6、Proposition2.2、Lemma2.4で theta group と degree-three divisor-class pair の descent、obstruction の対応を確認。非分裂曲線の偏極類と β の規約に用いる。二つの独立な Kummer 座標による α の index 九の付値証明と、一ブロック mixed 族への実現は本稿で記す。引用 key は `NFMCremonaFisherDescentAlgebra`。
- David J. Saltman, *Genus 1 Curves in Severi--Brauer Surfaces*, [arXiv:2105.09986v1](https://arxiv.org/abs/2105.09986v1)（2021-05-20）。§§3–4、Theorem5の Heisenberg 表現と Brauer–Severi surface 内の滑らかな genus-one 三次の関係を比較対象として原著確認した。こうした曲線の存在や period–index 現象そのものの新規性は主張しない。本稿では点 p の Picard 障害 α と偏極障害 β を明示的に分け、mixed 一ブロック族への実現と普遍重み一階数へ用いる。引用 key は `NFMSaltmanSeveri`。
- Matsuno, *A Complete Classification of 3-dimensional Quadratic AS-regular Algebras of Type EC*, Canad.Math.Bull.64(2021),123–141、[arXiv:1912.05167](https://arxiv.org/abs/1912.05167)、[DOI](https://doi.org/10.4153/S0008439520000302)。§2.4、Lemma2.16、Theorem3.3、§4、Corollary4.3。Hesse 型の幾何的 Sklyanin 代数、正則性と cyclic potential の一次資料。本稿では曲線の原点や p の線束を仮定しない体上への降下と、障害を保つ支配族への拡張を補う。引用 key は `NFMMatsunoElliptic`。
- Mori–Smith の既存書誌 `MoriSmith`、Proposition2.11、Theorem4.2(1)：potential と commutator–gradient 形式、滑らかな三次の3-Calabi–Yau条件との関係。本稿の有限恒等式・算術的降下・純超越的支配性は別に本文で検証する。

projector核・低次元full自己同値分類の一次資料：

- Canonaco–Stellari, *Non-uniqueness of Fourier–Mukai kernels*, Math.Z.272(2012),577–588、[著者PDF](https://sites.unimi.it/stellari/Research/Papers/NonUniq.pdf)、[arXiv:1009.5577](https://arxiv.org/abs/1009.5577)、[DOI](https://doi.org/10.1007/s00209-011-0950-3)。Theorem1.2、Proposition4.3、Corollary4.4（著者稿pp.10–11）で、同型なFM関手の核の各cohomology層が同型となることを確認。核自身の一般的一意性は主張されておらず、本稿ではprojectorのsimpleな点像とPic(Y)のtorsion-free性を追加して一意性を証明する。引用keyは `NFMCanonacoStellariKernels`。
- Ziqi Liu, *On Fourier–Mukai type autoequivalences of Kuznetsov components of cubic threefolds*, Math.Nachr.297(2024),1866–1878、[arXiv:2304.12669v2](https://arxiv.org/abs/2304.12669v2)、[DOI](https://doi.org/10.1002/mana.202300237)。Theorems1.1・4.13、§§2.2–2.3、Proposition3.5・Example3.7を確認。全ての滑らかな複素三次三次元多様体についてAut^FM(KuY)=Z×Aut(Y)、S=ρ[1]、S³=[5]を用いる。一般点ではAut(Y)=1、T=S⁻¹[2]=ρ⁻¹[1]が生成元となる。引用keyは `NFMLiuCubicThreefoldAut`。
- Huybrechts, *The K3 category of a cubic fourfold*, Compos.Math.153(2017),586–620、[公刊PDF](https://compositio.nl/Content/prize2021_huybrechts.pdf)、[arXiv:1505.01775](https://arxiv.org/abs/1505.01775)、[DOI](https://doi.org/10.1112/S0010437X16008137)。Theorem1.2(i)（公刊p.587）のvery generalな三次四次元多様体の全FM自己同値群Zと、[1]の生成する部分群の指数三を確認。Proposition3.12、Corollary3.13、§§3.4–3.5・6.1が関連箇所である。本稿では可算bad lociと核の有限データを用いて幾何学的一般点へ適用し、Zariski開上の全対象の定理とは扱わない。引用keyは `NFMHuybrechtsK3Cubic`。
- Iliev–Manivel, *On cubic hypersurfaces of dimensions 7 and 8*, Proc.London Math.Soc.(3)108(2014),no.2,517–540、[arXiv:1102.3618v2](https://arxiv.org/abs/1102.3618v2)、[DOI](https://doi.org/10.1112/plms/pdt042)。Proposition3.1の一般七様体のCartan表示、Theorem3.4、Proposition5.2、Corollary5.3の階数九の束とKu内の三次元球面対象を確認。本稿の数値作用の計算は、その既知対象のtwistからZ²とrotation中央化群の無限指数を取り出す。球面対象の存在を本稿の新規結果とせず、全ての特殊七様体にも拡張しない。引用keyは `NFMIlievManivelSevenfold`。

高次元の文献比較では、Lin–Rennemo–Zhang, *Categorical Torelli theorems for weighted hypersurfaces*, Adv.Math.503(2026),PartC,111271、[DOI](https://doi.org/10.1016/j.aim.2026.111271)、Theorem1.3（Theorem3.12・Corollary3.13）、Lin–Zeng–Zhang [arXiv:2610.00130v1](https://arxiv.org/abs/2610.00130v1)、Proposition2.1・Remark2.2、Lin–Zhang [arXiv:2611.05915v1](https://arxiv.org/abs/2611.05915v1)、Theorem1.3のstatementを原著で確認した。順にweighted hypersurfaceの復元、Serre関手からの内部shiftの回復、三次四様体を除くCalabi–Yau型のFourier–Mukai partner数の有限性に関する結果である。最後の対象は標的多様体の数であり、固定標的への核の数ではない。これらの全証明の独立点検はしておらず、高次元class選択の証明入力にも用いない。

五次元の安定性条件と有限安定化群の比較に必要な一次資料：

- Peize Liu, *Stability conditions and moduli spaces on the Kuznetsov component of cubic fivefolds*, [arXiv:2509.21454v5](https://arxiv.org/abs/2509.21454v5)（2026-08-03）。Theorem2.8、§2.2の式(2-4)・Remark2.11の Ψ⊣Φ と rank 四局所自由 module、Lemmas2.12–2.14 の mutation 比較、Lemma3.4、Corollary3.10(ii)、Proposition3.11 の rotation と数値作用を確認。Theorem5.5の証明は Clifford rotation が構成した安定性軌道を保つこと、Corollary5.10は Serre 不変性を与える。Proposition6.10の Fano 曲面は最小 stable moduli の一つの連結成分であり、全体の既約性は Remark6.11 の予想、Serre 不変軌道の一意性は Remark5.6 の未解決問題である。本稿では相対核・平面非依存性・奇数零 cycle による元の体への降下と E_p の二 mutation 表示を補う。さらに spinor 列の随伴 unit と相対・絶対 coevaluation を比較し、O≃ρ⁻¹[1]、ε≃id を perfect 核として同定する。引用 key は `NFMPeizeLiuFivefold`。
- Alexander Kuznetsov, *Derived categories of quadric fibrations and intersections of quadrics*, Adv.Math.218(2008),1340–1369、[公刊著者PDF](https://homepage.mi-ras.ru/~akuznet/publications/DerivedCategoriesOfQuadricFibrationsAndIntersectionsOfQuadrics.pdf)、[DOI](https://doi.org/10.1016/j.aim.2008.03.007)。Theorem4.2、Lemmas3.8・4.5・4.6・4.7・4.10、Remark4.8（公刊 pp.1353,1357,1359–1361）を確認。Clifford module の局所射影性、実際の局所自由 kernel、有限振幅、随伴が相対半 rotation の構成に必要である。absolute perfect から相対 perfect を無条件に推論せず、相対 Clifford 模型と滑らかな幾何学的 kernel で確認する。引用 key は `NFMKuznetsovQuadric`。
- Alberto Collino, *The Abel–Jacobi isomorphism for the cubic fivefold*, Pacific J.Math.122(1986),43–55、[公刊PDF](https://msp.org/pjm/1986/122-1/pjm-v122-n1-p04-s.pdf)。Propositions1.8・1.10（公刊 p.46）の Fano 曲面の連結性・一般の滑らかさと既約性を確認。本稿では一般の残余五様体に適用し、相対核の離散 class 写像が一定になることへ使う。引用 key は `NFMCollinoFivefold`。
- Ciro Ciliberto–Mikhail Zaidenberg, *On Fano schemes of complete intersections*, in *Polynomial Rings and Affine Algebraic Geometry*, Springer Proc.Math.Stat.319(2020),1–39、[DOI](https://doi.org/10.1007/978-3-030-42136-6_1)、[著者稿 arXiv:1903.11294v2](https://arxiv.org/abs/1903.11294v2)。著者稿 Example4.4（p.20）の cubic fivefold の Fano 曲面の Plücker 次数2835と係数公式を確認した。数値自体は既知で、本稿では整数多項式で再現し、二捩れ kernel gerbe の corestriction に用いる。引用 key は `NFMCilibertoZaidenbergFano`。
- D. Wu, *Construction of stability conditions on some Kuznetsov components*, [arXiv:2611.02388v1](https://arxiv.org/abs/2611.02388v1)（2026）。Theorem1.3、Proposition7.2の各numerical stability連結成分が自由なGL̃₂⁺軌道となるstatementを原著で確認した。自己同値群の作用の忠実性やH_p=1を与える定理としては使わず、全証明の独立検証もしていない。引用keyは `NFMWuStability`。
- A. Aravena, P. Liu, J. Tevelev, *Gepner stability conditions on hypersurface categories*, [arXiv:2611.05350v1](https://arxiv.org/abs/2611.05350v1)（2026）。Theorem1.2、Corollary1.3のGepner安定性条件の存在のstatementと適用範囲を確認した。H_pやS_pの自明性の証明入力には用いず、全証明の独立検証とも区別する。引用keyは `NFMAravenaLiuTevelevGepner`。

指定MF周期の規約は、固定入力B `papers/sections/generic_recovery/local_model.tex` の `lp:prop:sing-period`、`window.tex` の `tw:eq:period-extension` と `tw:eq:rotation-period-square` に置かれている。前者の双加群truncation境界とconormal基底、後二者のYoneda二拡張と実際のrotation比較を照合した。周期の中心的coherenceと生成元変更のu⁻¹則はこの指定規約に関する主張であり、任意に選び直したfractional Calabi–Yau自明化の自然性を仮定しない。

周期位相の混合定数降下では、同じ固定 B の `cft:lem:arity`、`cft:lem:flow`、`cft:eq:bound`、`cft:eq:object`、`cft:eq:insertions`、`cft:eq:two-block-matrix` を使用する。三対象生成と actual Hom の局所化には `gcd:prop:bound`、`tw:lem:proper-hom`、`rog:lem:localization` を用いる。局所化前の integral な有限 MF の Hom を先に比較する範囲を保持し、任意の Laurent 係数 MC 元への収束を新たに主張しない。Fisher の Theorem1.1・Lemma2.2・§9.5 の不変式・一般軌道・Heisenberg 群と、既存の全三捩れモノドロミーを合わせた μ₃-character の消滅が、二変数不変量体への降下に必要である。

Murfet, *Residues and duality for singularity categories of isolated Gorenstein singularities*, Compos.Math.149(2013),no.12,2071–2100、[arXiv:0912.1629v3](https://arxiv.org/abs/0912.1629v3)、[DOI](https://doi.org/10.1112/S0010437X13007082) のTheorem6.2・式(6.6)、Proposition4.2・式(5.7)を確認した。MFの微分と射を含むresidue trace、およびdeterminantの変換則を、γ_scの計算候補として保持する。sourceから移した実際の微分・射とAS-Gorenstein traceの規格化をまだ同定していないため、指定した位相の大域値の証明としては用いていない。引用keyは `NFMMurfetResidue`。

自然な残余射・active曲線比較・正確な一般次数18・符号消滅とfull射の次数9・最高次線束型・点型の全O-降下・三分点被覆の九次性と216次monodromy・低次元のfull class降下・随伴復元条件による有限class torsor・周期位相とcube frameの算術への適用について、初出と新規性の網羅的確認は未完了である。既知の曲線同型理論、Hessian点曲線、Hesse群・古典的不変式環、determinantによるBrauer消去、Picard gerbe、楕円導来圏の自己同値一般論、Tate–Weil pairing、Sklyanin理論、LiuとHuybrechtsの自己同値群分類、Toën–Vaquiéのmoduli、Murfetのresidue公式自体を新規成果としない。非被約相対分類、実active族への算術的降下、H_gのfull ambient作用による平面同型torsorの分裂、残余側のexact index、projector核の一意性と定数ZによるGalois降下、有限 H_p への縮約、五次元半 rotation の平面非依存性・奇数零 cycle による降下、非分裂点 Picard index 九の一ブロック実現と普遍最小階数、指定周期の cube frame と scalar gerbe の算術との接続を、これらの既知入力から区別して記載する。

### 境界の Kummer 計算の一次資料

Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer (2009), DOI 10.1007/978-0-387-09494-6。[一次資料PDF](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf) の Chapter XI, Proposition 9.2 と直前の定義（印刷pp.398–400、PDF pp.409–411）を確認した。pairing は e₃(σQ−Q,T) であり、div(f)=3(T)−3(O) に加えて f∘[3] が K(E) 内の三乗である規格化を要求する。原点で先頭係数一の接線比はこの仮定を満たすことを本文で証明した。Appendix C, Theorems 15.1–15.2、Corollary 15.2.1 の正則模型・成分群も確認。Kummer 理論や I₃ 成分群は既知結果であり、本稿の点 shift の局所体と有限行列表示の計算と区別する。

- Eisenbud, *Homological algebra on a complete intersection, with an application to group representations*, Trans.AMS260(1980),35–64、[DOI](https://doi.org/10.1090/S0002-9947-1980-0570778-7)、[原著PDF](https://ssather.people.clemson.edu/fa11/790-3/eisenbud.pdf)：Theorem7.2（公刊pp.56–57）を原著確認。有限自由分解と高次 homotopy から超曲面商上の自由分解を作る既知の Shamash 構成である。本稿では線型行列 L と中心 Koszul 分解に対し dh+hd=F、h²=0 の明示 homotopy を与え、各 parity の階数3·2^(n−1)と内部 shift を記述した。この一般構成や MF の周期性自体の新規性は主張しない。引用キー `NFMEisenbudCI`。

### Tate–Koszul と Clifford 同定の一次資料

- Lu–Palmieri–Wu–Zhang, *Koszul equivalences in A∞-algebras*, New York J. Math.14(2008),325–378、[一次PDF](https://nyjm.albany.edu/j/2008/14-16.pdf)。Definition2.1 の Adams connected 条件、Theorem2.4 と Corollary2.5(b)、pp.338–340 の二重双対と homotopy Hom の反変全単射を確認。局所有限性を内部次数ごとに確認して適用する。引用キー `NFMLPWZKoszul`。
- 同著者, *A∞ structure on Ext-algebras*, J. Pure Appl. Algebra213(2009),2017–2037、[著者PDF](https://sites.math.washington.edu/~palmieri/Papers/ext-a-infty.pdf)、Theorem A と Corollary B。関係式を高次積から回復する既知入力であり、三次テンソルの gauge 不変性を主張する文献ではない。`NFMLPWZExt`。
- Braun–Chuang–Lazarev, *Derived localisation of algebras and modules*, Adv.Math.328(2018),555–622、[arXiv:1505.01146v3](https://arxiv.org/abs/1505.01146v3)、[DOI](https://doi.org/10.1016/j.aim.2018.02.004)。Proposition3.17、Theorem3.18 の homotopy epimorphism と mapping-space fibre、Theorem5.3 の中央 class の cohomology 局所化を確認。書誌は著者機関 City の公開記録とも照合。`NFMBCLLocalization`。
- Keller, *On triangulated orbit categories*, Doc.Math.10(2005),551–581、[著者PDF](https://webusers.imj-prg.fr/~bernhard.keller/publ/triaorbit.pdf)、§§9.3–9.4。実際の quasi-functor の比較同型を cofibrant bimodule へ持ち上げ、orbit 関手と合成整合性を作る箇所を確認。[2009訂正](https://webusers.imj-prg.fr/~bernhard.keller/publ/corrTriaOrbit.pdf)も確認し、旧§7の hull 表示と周期・Serre に関する修正前の主張は使わない。`NFMKellerOrbit`。
- 五次元全関手同定には既存 Kuznetsov 文献の Lemma4.5（spinor 列）・Lemma4.7（局所自由性）、Liu v5 の式(2-4)、Lemma2.12、Corollary3.10(ii)を使用。新しい部分は spinor 射の adjunction unit としての同定、相対・絶対 coevaluation と Beilinson defect の比較である。指定 square/period の同時正規化は扱わない。

これらの既知の一般定理と、現行稿の Tate cutoff・核への忠実性・全次元の強化 class 選択への適用を分ける。全引用・被引用文献を尽くした新規性調査、外部査読、形式証明器の検証は未完了である。

## 8. 再現の入口

README の再生成手順で、ソース参照、二次・三次の保存済み証明書、LuaLaTeX 組版を確認できる。`python3 scripts/check_sources.py` で三稿の入力・引用・ラベル・他稿参照を検査し、ルートで `python3 scripts/build_papers.py` を実行して組版する。PDFは `build/nc-cubic.pdf`、`build/cubic-moduli-descent.pdf`、`build/mixed-sklyanin-cubics.pdf`、SyncTeXも同じ `build/` に出す。次数三の検証は Python・NumPy と C++17 コンパイラを用い、大きな行列を `build/jacobi-vertex/` に再生成する。証明に必要なテンソル・選択行・検証コードを保存し、再生成できる大行列自体は収録しない。

trace–Hessian の中心係数・八次代数 trace、全次元の KS 例、split Hesse の有理式と j 差、混合係数の二次恒等式についても、README と `notes/validation.md` にある該当手順と確認範囲を参照する。厳密な記号計算による係数検証を、未公表入力の非可換中心性・完備 MF 移送・一般点復元の全証明の独立検証と同一視しない。任意次元・任意基底の主張は、有限個の計算例だけでなく本文の相対証明に依拠する。

混合五次 tensor の再現は `computations/verify_mixed_fifth.py` と必要最小限の重み証明書 `computations/data/harmonic_linear_products.json`、中心逆像の四次恒等式・Jacobi 非消滅・古典的共変式の恒等式は `computations/verify_fourth_potential.py` に収める。両者とも Python と SymPy を用い、グラフ縮約は整数・Fraction、係数恒等式は有理数係数の多項式として厳密に計算する。既知重みの使用、係数恒等式の検算、一般次元の証明、形式証明器による検証は異なる状態として記録する。新たな四次の中心グラフ積分は行っていない。

active 不変量の有限式は、ルートから `python computations/verify_active_invariants.py` を実行して再現する。SymPy の QQ 上で不変量・判別式・Jacobian・点線束行列と MF 曲率の有限恒等式を扱う。境界の二次・三次積と一次項は別の有限行列証明書で扱い、実行範囲と出力の状態は `notes/validation.md` を参照する。一般 fibre の幾何学的整性、全次数の有限混合三角性、飽和代数の平坦性、Isom 延長と Kummer 降下の証明を、有限恒等式の検算そのものと同一視しない。

Hesse 体の二次類単射に用いる有限恒等式は、`python computations/verify_active_sign.py` で再現する。QQ(ζ)、ζ²+ζ+1=0 上で不変量の保存、四元数群と C₃ の関係、群の位数24、次数の上界を与える四次・三次恒等式、非自明な μ₂ 指標の不存在を検算する。全次元の滑らかさの証明に現れる二つの整数の非消滅も確認するが、scalar symmetrizerの全次元の証明、有限対角による延長と同変降下、χ_actの消滅の全論証を計算で代用するものではない。実際の実行結果は `notes/validation.md` を参照する。

最高次線束型の graded purity、PBW の中心平坦性、Tor-independent な MF 係数商、Galinat の同じ window における shift・rotation、cohomology の平坦化と gerbe 上の貼合せは内部で独立に読解した。Picard 障害・active 曲線上の分裂・階数3 Azumaya も紙上の証明による。完備中心切断の bar 恒等式、係数商と relative perfect 性の反例、次数二中心の formality 反例、有限四角の PGL_d 障害、内部次数を忘れた無限 coherence の例、Hom 剛性化はノートの証明で確認できる。実際の Morita 核と curved-bar 模型の同定は未完成であり、条件付き振幅評価と区別する。外部査読・全固定入力の独立検証・形式証明器による機械検証を行ったという意味ではない。

三倍線束の重み・零切断での相殺・底変更と、三分点被覆上の規格化の一意性は紙上で独立に点検した。右 THCR の符号と楕円 rotation の二つの shear、形式恒等核からの graph-support、Picard 等式を保つ有限降下も内部で独立に読解した。これらには別の検算コードを設けず本文の証明を正本とする。指定中心商の相対THCR/window1と閉／一般底変更は本文の証明を執筆担当以外の二担当も読解点検した。一般の特異圏の底変更とは区別する。符号消滅には別に有限対角による延長補題を証明し、特殊点の非自明な慣性を含むC₃同変降下を独立に点検した。

Picard 障害と三捩れ monodromy の有限恒等式は `python computations/verify_picard_obstruction.py` で再現する。Hesse 接線・norm・点三次・係数逆、数値 rotation centralizer、巡回 twist、symbol と三捩れ点の恒等式を扱う。既存の計算資産と証明書を保持し、各版で実際に実行した範囲は `notes/validation.md` を正本とする。付値による非norm性、一般係数体への降下、gerbe・導来圏の一般証明は有限検算と区別する。

五次元 Fano 曲面の次数は、`python3 computations/verify_fivefold_plane_degree.py` で再現する。Sym³S* の Chern 根の積と Grassmann 積分から

\[
 [x^6y^5z^4]\!
 \left(\prod_{a+b+c=3}(ax+by+cz)\right)
 (x+y+z)^2(x-y)(x-z)(y-z)=2835
\]

を整数演算だけで検算し、PASS を確認した。Chern 根は tautological bundle の双対 S* の規約である。この既知の次数の再現と、実相対核・class の連続性・2β_O=2835β_O=0による降下の紙上の証明を区別する。半 rotation の構成、随伴の向き、relative C_i の例外性、ε の安定性軌道固定、E_p の二 mutation と十五次元評価核は、一次資料との照合を含め内部独立点検を済ませた。

非分裂点障害の period 三・index 九は、二変数の付値を用いる division 証明、theta factor set の符号、Tate pairing、mixed 表示への twist と純超越的な支配性を紙上で点検した。普遍重み一階数九の上界と全非空開での下界、非分裂強化点型の降下と共通慣性自明開の全 n≡1 mod3 における未標識最小次数九は別の一般証明であり、2835の有限計算では検証していない。外部査読・新規性の網羅的確認は未完了である。

全 FM 判定の数値規格化・graph 認識・偏極条件と、非被約底の相対分類・μ₃位相と G_m inertia の区別は、本文の証明を別担当が独立に読解した。CK の符号規約、一般 j の巡回例、Sklyanin の既知仮定と本稿の降下の区別も一次資料と照合している。これは外部査読や形式証明器での検証とは異なる。検証の実行範囲と原稿の論理的な証明を分ける。

κのSerre基底線束の相殺、q_YのA_C-linearなKoszul/window比較、projector核の一意性、n=3,4の既知自己同値群からのclass降下は紙上で独立に読解した。三分点被覆の九次性と216次群の一般証明は、上の四つの有限恒等式とは別に本文を正本とする。新規補題の執筆・内部点検、文献の一次確認、計算の実行、組版、保存を一括して同じ検証とは呼ばない。

指定 MF 周期の中心的 coherence、T^m による class 不変性、相対 frame の変換則、混合有理比較と C(s,t) への降下を、指定した入力と照合して内部で独立点検した。境界の局所値 [D_R] には、実際の低積とその一次項、二次関係の飽和、全次数平坦性、smooth potential 三次による Isom 延長を組み合わせる。有限行列の実行確認、紙上証明の点検、組版、外部査読、形式証明器での検証を別々に扱い、実施状態は `notes/validation.md` に記載する。ΔD 外の分岐排除と大域式 [D] は未証明である。

随伴復元による強化点型では、q^RO_C≃j_Y!OのKoszul証明、両ファイバーを用いるDVR上の最高次線束の持上げ、coneのproper性による非空型の有限降下を紙上で点検した。有限H_pには固定入力Bの三対象生成、Morita核のfree A^e、TV Proposition3.20と可逆核の開性、HH¹=0を実際に照合した。S_p×Pic_C^p、低次元の唯一のclass、Euler格子による奇数次元の数値的自明性、最小実現次数公式は一般証明であり、新たな計算コードや有限例だけによる確認ではない。全moduli上の実核の存在は主張しない。一方、全次元の一般一ブロック族でH_p=1、S_p=Spec(k_n)となる別のTate–Koszul証明は、既存の独立読解点検の対象である。

高次元の中央shift部分の除去、classと軌道の安定化群の一致、奇数次元の数値格子・六元中央化群、七次元のZ²とrotation中央化群の無限指数は、本文の証明を別担当が独立に読解した。Iliev–Manivelの球面対象は既知入力と分け、数値的自明な自己同値の分類や対応torsorの中立性まで検証したとはしない。

外部文献 PDF、旧版原稿、旧 ZIP、担当者別の重複レポート、コンパイル中間生成物は現行一式に含めない。主張の証明・証明書の生成・実際の検証・保存は別の状態として扱い、検証事実の正本は `notes/validation.md` とする。
