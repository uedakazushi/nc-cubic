# 混合 Sklyanin 族と中心・相対比較

2026-11-24 / v93。混合稿の構成・判別・核の補足。

[研究ノート入口](research_notes.md) · [研究方針](../00_research_plan.md) · [検証範囲](validation.md)

## 現在の範囲

否定された旧主予想は任意の滑らかなnc cubicのKuを同次元の滑らかな可換cubicで実現することだった。一つの共有中心変数・任意の固定smooth標準Sklyanin因子の組（k≥2）について、指定境界を保つ全因子別PBW・中心持上げを可換三次と全係数でMorita比較した（`emc:prop:coverage`, `euk:thm:universal-kernel`）。非二捩れの正規化線形Pと二捩れの中心平方βを一次係数tとする。標的はG+uQ(t)+u²(𝔄α+R₂(t))+u³(κc+R₁,₁(t,α)+R₃(t))、𝔄可逆、κ≠0であり、可換smooth開では相対perfect核・全coherent Ku同値を得る。定数3k方向のBocksteinは同型、一次3k方向は単射だが、存在比較は後者を仮定しない。

rank8^kの臨界代数で全係数のsmoothnessを判定する。任意固定tの一般αでは8^k個の相異なる悪いcと、各可換標的の唯一の通常二重点がある。全係数・固定tの判別超曲面は既約被約で、臨界点のaffine空間が正規化を与える。一変数特殊化の重複根は許す。同一S(1,−1,−1)では純ブロックJac₂像・七定数形・κ_k²=27/28を保持し、残る六定数は未数値化。一般因子へこのκ値を流用しない。任意中心数の全因子別表示でK_A smooth ⇔ X_pol smoothを示し、一般中央flagの存在から全smooth対象を比較した。横断二項Bは可逆で、各固定一次係数の一般二次係数では2^(3k+m−1)個の単純悪値を得る。X_polへの実核、因子moduli上の核選択・降下、全intrinsic被覆、h一般点核のdefect零特殊化は残る。指定二ブロックのP64・norm全64根・局所型も保持する。

最高active二次関係が固定したtensor Sklyanin境界で、中心一次変数を厳密に可換に保つ全quadratic PBW表示は、因子間可換を事前に課さなくても元の生成元で因子別に分解する（`ifp:thm:factorization`）。従って、指定中心三次の最高項が非零重みのΣa_iΩ_iである範囲では既存の全許容表示・全smooth比較へ戻る。残る混合問題は境界二次関係自体を動かす変形にある。その次数零一次中心障害を計算し、Clifford因子の中心平方に由来する一組の九方向を、自由な二次代数族と中心正則三次商へ実積分した（`ifh:prop:central-mixed-obstruction`, `ifc:thm:family`）。この周囲代数は全係数で相対Koszul・untwisted相対6-CYであり、複素fiberはAS-regular dimension/index6となる。四・五次元型の原点近傍には実相対smooth proper模型とétale局所perfect Ku核を得た（`ifr:thm:ambient-regularity`, `iff:thm:smooth-neighborhood`, `ifk:cor:clifford-fourfold-neighborhood`, `iff:cor:cubic-fivefold-open`）。四次元には主稿のrotation付きArtin形式認識を用いる。

## 因子別 PBW・中心変数

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

## 相対圏・root・境界

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

## 次の比較課題

**偏極標的への実核と中心作用の比較を調べる。** `mcb:thm:smooth-locus` はX_polによる全smooth locusの判定を与えるが、実Ku核の標的は逐次構成のX_itである。次は `mbl:cor:chart-kernel` の局所核を重なりへ制限し、差となる自己同値・周期位相とČech coherenceを計算する。対角の局所完全性は比較核の貼合せではない。`tcr:prop:joint-comonad` の混合情報と `tcr:ex:same-axes` を保ち、単純な軸データから全比較を決定しない。

証明所在：`cmm:thm:universal-kernel`、`cmm:cor:determinantal-discriminant`、`mtd:thm:normalization`、`mtd:cor:many-centers`、`ifp:cor:central-comparison`、`cmo:prop:invariant-restriction-spherical`、`mix:prop:h-flat`。
