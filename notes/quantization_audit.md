# 量子化論文：主張・依存・一次資料の確認範囲

2026-11-21 / v1（3論文構成）。最初に `00_research_plan.md` を読む。
この文書は現行原稿の仮定・証明所在・一次資料の確認範囲を整理する。
以下の「点検」は移管前の有効な内部監査の範囲であり、今回の分割時に全証明を再読・形式検証したことを意味しない。
新規性・外部査読の確定と、証明記載・内部点検・有限計算・組版は別の状態である。

本文は `papers/cubic-quantization.tex`、文献は `papers/quantization-references.tex`、節は `papers/sections/quantization/`。
詳細な着想・障害は [cubic_quantization.md](cubic_quantization.md)。
古典的な正規形・退化幾何・Poisson成分は [poisson-cubic](https://github.com/uedakazushi/poisson-cubic/blob/main/papers/poisson-cubic.tex) を入力とする。

## 公表範囲

中心元は固定した変数分解の全滑らかな係数空間上で同時選択できる。
さらにN>=5、全三次式Fが滑らか、Pが非零分解可能である全supportの係数空間について、
H_N=GL_N×Gmに共変な代数的中心元を、普遍Hessian二次jet
Ω=sym(F−h²H(P,F)/12+O(h⁴))まで指定して、全零h切断を含む一つの開上に同時に選べる。
証明は古典核のBWB消滅、K/h³Kの指定切断からのh冪厚化への持上げ、
Stiefel開の正則関数の延長、有限核のNoetherian完備化mod h³、還元的平均化を結ぶ。
gcd(N,3)=1なら、全階数二の被約Poisson層とh直線の積の零切断近傍へ
実際の次数付き代数・中心イデアル・中心商が降りる。N=5では全非零Poisson対を扱う。
gerbeの位数は正確にgcd(N,3)であり、3|Nなら非中立で、重み一の線束による元の次数一の補正は不可能である。
一方、全N>=5でA_(3d)⊗λ^d、B_(3d)⊗λ^dは第三Veroneseの代数族として降り、
Ω⊗1は新しい次数一の大域中心元となる。商と次数別局所自由性は保たれ、古典Projの偏極はO(3)である。
qgrのVeronese同値は左右noetherianである各幾何学的ファイバーに限って述べる。
零Poisson構造、全hへの延長、一意性、別ambientやMorita模型による比較はこの結果の範囲外である。

複数ブロックでもN=3k、k>=2の満supportでは、還元的安定化群による軌道と
smooth Fの係数空間がアフィンなので、有限射影核の指定jetから直接持ち上げる。
形式的持上げ・完備化を使わず、ブロック順序・基底・相対規格化を底へ追加しない
H_N共変な中心元と正則中心商を全零h切断近傍に得る。
第三Veroneseは実際の被約Poisson層へ降り、底の次元は2k、三次四様体のrank4層では四である。
これは固定h≠0での非可換同型類の像の次元ではない。
また全非零被約rank2k層のgerbe位数はgcd(N,3)=gcd(m,3)であり、満supportでは三である。
位数の主張は階数層全体または全零h切断近傍についてで、任意の稠密開や一般点の主張ではない。
中心変数の残るm>0、k>=2での一般の同時中心元は未解決である。

層別の明示的構成も保持する。
単一ブロックではreductive群に関して全係数空間上で同変に選べ、
三変数制限が滑らかな開と、節点・尖点の各軌道では、中心平行移動を含む群にも型ごとに拡張できる。
零制限ではPBW対称化したΩ=sym(f)が全パラメータの全G共変な正則中心元となり、
一般のG_0同変選択もこの零層の元に一致させられる。
線形群の商上の中心Gm-gerbeを同定し、gcd(m,3)=1では指標で次数線形化を補正して、
階数二のPoisson対の被約層内の開へ代数族を降ろす。
support平面がXに含まれる零制限層では、同じ指標による降下を全h直線上で行える。
節点・尖点層では唯一の特異点の直線束で次数重みを補正するため、gcd(m,3)=1を仮定せず、
本稿の範囲m>=2の全てでgerbeが中立となり、実際の次数付き代数と中心商が零h近傍へ降りる。
三次三様体での底の次元は節点型16、尖点型15である。
N>=6では零制限の標準中心直線O sym(F)と全supportの中心直線を全層で一致させることは、
群同変性を課さなくても二次jetの相対H¹障害により不可能である。
零制限の全h公式sym(f)と、その式に一致する固定supportのG_0選択は別の有効な族として保持する。
所定ambientでの中心イデアルの非一致は、抽象的な商の非同型やqgr非同値を意味しない。
全f・η・hを用いても補空間を正則同変に選ぶことはできず、
中心平行移動Uの自由商は非アフィンである。中心核を直接扱う方法はこの障害と両立する。
ambientの二次包絡、偏極付き圏からの復元、三次三様体の条件付き導来復元は付録に収める。本文・付録を通じてambientはA、中心商はBとする。
要約・序論はこの依存順に整理し、Fermatのspace・固定stack・相対stackの三種類の成分数を区別する。
表示式には数値の式番号を付ける。

記号はこの論文ではambientをA、中心商をBとする。`nc-cubic.tex` の記号と照合するときは役割を優先する。

## 主張と証明の所在

| 主張・所在 | 有効な仮定と結論 | 既存の内部点検の範囲 |
| --- | --- | --- |
| `prop:pg-PBW`、`lem:pg-center-parity`、`prop:pg-universal-casimir-jet`、`quantization_foundations.tex` | 一ブロックの相対PBW・偶性・有限jet | 既知PBW入力と係数環への拡張。全次数PBWを有限次数の中心性検算とは区別 |
| `thm:pg-universal-determinant`、`universal_casimir_determinant.tex` | 全体三次fが滑らかなら、active制限が特異・零でも、原点近傍に代数的中心三次元 | gcd、古典核、普遍行列、局所自由性、稠密Hesse開、Cramer規格化、偶性 |
| `lem:pg-det-divided-kernel`、`prop:pg-det-normalization-transition`、`thm:pg-det-global-coefficient-lift` | 固定変数分解の全係数空間×h内で、全零切断を含む開上の偶な中心元。遷移はΩ'=aΩ+c | 任意底変更、通常の中心との差、偶principal開、忠実平坦下降、UFD/Pic=0、単元補正、Hesseのイデアル不一致、covarianceを独立に再点検 |
| `thm:pg-equivariant-levi-center`、`equivariant_central_lifts.tex` | 全滑らかなfでG_0同変な偶中心元。定義開は零切断とg=0の全t層を含み、零制限ではsym(f)に一致 | stable idealへのReynolds平均、指標twist、Z₀=(t=0)∪(g=0)上の指定値の持上げ、商線束の零点除去 |
| `lem:pg-equivariant-singular-retractions` | 節点・尖点の各軌道上にδ_gの正則なL同変左逆。軌道の次元は9、8 | 方程式scale込みの全安定化群Gm×S₃、Gm²、明示σ、L/Hへの正則な移送。各型の標準形を係数比較で確認 |
| `thm:pg-equivariant-parabolic-center` | gが滑らかな開、節点軌道、尖点軌道のそれぞれで、零t切断全体を含む開上の全G同変中心元 | smooth gではaffine底の分裂、節点・尖点では軌道上のσを使用。B_fの変換則、fの滑らかさ、Q(f⁰,0)=1を保つ定義開の引戻し。これら層別の式と全supportの別の選択との一致は未主張 |
| `rem:pg-equivariant-stratumwise-centering` | 不可約ternary cubicの全開には、gだけに依存する単一の正則なδ_g左逆は存在しない | 可約式の錐の余次元2、正規性による行列成分の延長、g=0での矛盾。同変性なしでも成立し、中心元自体の貼合せ不存在は意味しない |
| `thm:pg-equivariant-zero-center` | g=0なら全t・全係数でPBW、Ω=sym(f)は全G共変。f smoothなら三次の割った交換子核はOΩ⊕C_m | 中心e₀を足したLie代数、monic PBW、対称化と交換子の厳密一致、全tの定階数核。中心性にはf smooth不要。一般のG_0族を(t=0)∪(g=0)上の指定値へ持ち上げる補強も点検 |
| `cor:pg-equivariant-central-quotient` | 線形群の商上の次数別平坦なAS-Gorenstein中心商族 | t=ηhでhを固定、domainと正則性、各次数の局所自由性、スカラーの重み |
| `prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent`、`rem:pg-equivariant-classical-family` | gcd(m,3)=1なら次数線形化を補正して階数二の被約Poisson層内の開へ降下。n=3で底は17次元 | GLの付随束表示、二つのスカラーの群完全列、fppf安定化群完全列、mr−3s=1の分裂、古典極限Sym(E_θ)と三次直線、相対Projを点検。大域中心生成元と固定h≠0での像の次元は未主張 |
| `prop:pg-equivariant-zero-stratum` | P(W_P)⊂Xのrank2層はm>=3でのみ非空、滑らか既約・余次元10。全hのgerbe族、gcd(m,3)=1なら層自体へ降下 | m個の法方向二次式、滑らかな例、共通incidence上のrank10制限束、Gbar商と次元D−m²−3m−18。m=3で指標法の適用は主張しない |
| `prop:pg-equivariant-singular-strata` | m>=2、節点・尖点の被約rank2層は非空・滑らか・既約、余次元c=1、2、次元D−m²−3m−8−c。全mでgerbe中立、零h近傍の次数付き代数が層自体へ降下 | 滑らかな全fの例、共通incidenceの局所閉制限、Gbar商。特異点直線ℓのpullback M⁻¹と重み−1、A_d⊗ℓ^d、frameによる中立化、重み零の積・中心イデアルの下降、古典Proj。n=3では16・15次元 |
| `lem:pg-rank-two-bott-vanishing`、`intrinsic_rank_two_center.tex` | N>=5、Gr(3,N)上のO(j)とSym³Q*⊗O(j)のH¹が全整数jで零 | BWB重みの重複・置換長、非零Plücker錐のGm-torsor、全twistの直和、アフィンな全F係数空間との積を独立に確認 |
| `thm:pg-intrinsic-rank-two-center` | 全smooth F・非零分解可能P・任意の制限型を扱い、全零h切断近傍でH_N共変な偶中心元、普遍Hessian二次jet、K=C⊕OΩ、次数別局所自由な正則中心商 | jet命題からΘ mod h³∈K/h³Kを初期値に取る。H¹消滅、Stiefel/SL3不変環、有限Weyl開、Khat/h³Khat≅K/h³K、平均化による指定jet保持、全次数PBW開への制限。形式級数全体の代数性やP=0での定階数性は仮定しない |
| `cor:pg-intrinsic-rank-two-descent` | gcd(N,3)=1なら全被約rank2層×A¹_hの零切断近傍へ元の次数を保つ代数と中心商が降下。N=5では全非零Poisson対 | H_N/K_scによる商同定、Nr−3s=1、θ=(det L)^rλ^s、次数θ⁻ᵈによる重み除去。この降下での中心直線の大域生成元、零Poisson、全hは未主張 |
| `prop:pg-intrinsic-gerbe-period` | Pic(S)=0、中心重み像gcd(N,3)Z、gerbe位数gcd(N,3)。3\|Nでは全零h切断近傍にも重み±1線束なし | Stiefel開のfactorial性と余次元、SL3線形化の単元計算、H_N同変線束の指標表示、重みr線束とrα=0のcocycle証明。別ambient・Morita模型・圏の降下は排除しない |
| `cor:pg-intrinsic-third-veronese-descent`、`rem:pg-intrinsic-veronese-qgr` | 全NでA_(3d)⊗λ^d、B_(3d)⊗λ^dと次数一の大域中心元ωが降下。B^[3]=A^[3]/(ω)、次数別局所自由、古典ProjとO(3)偏極 | 中心重み3d−3d、λΦ(Ω′)=Ω、正則中心商の完全列、χ=λθ³による比較。qgr同値は左右noetherian閉ファイバーに限定し、訂正文のTor条件を直接確認。VeroneseのAS-regular性は未主張 |
| `lem:pg-intrinsic-block-cover`、`full_support_quantization.tex` | Pのunordered支持ブロック、全安定化群Hom(U,W)⋊((SL₃^k⋊S_k)×GL_m)、次数kの有限étaleブロック被覆と次数k!の順序付けtorsor | 点ごとの復元は既存ne:blocks。縮約軌跡の被約イデアル、射影化のk個のP²、相対Stein分解と任意底変更。k=1,2にも追加の連続対称性なし。補空間・純中心配分は内在的に選ばれない |
| `prop:pg-intrinsic-all-rank-gerbe` | 全非零被約rank2k層のH_N/K_sc商表示、中心重み像gcd(N,3)Z、gerbe位数gcd(N,3)=gcd(m,3) | 全層での既約性、Fermat点の安定化群にあるS,Tと交換子ζ⁻¹I_N、線束ファイバーの一次元表現、λ⁻¹の重み三とBezout。全零h切断近傍にも同位数。任意稠密開・一般点の位数は未主張 |
| `thm:pg-intrinsic-full-support-center` | N=3k、k>=2、全満support係数空間で偶かつH_N共変な代数的中心元と指定Hessian二次jet、階数kの割った交換子核、正則中心商 | 還元的安定化群とMatsushima、判別式主開のアフィン性、ブロック多重次数とminorによる定階数、有限射影核からΘ mod h³を直接持上げてReynolds平均。形式持上げ・完備化は不要。各成分非零開と一ブロックfiltrationによる正則性 |
| `cor:pg-full-support-veronese-descent`、`cor:pg-full-support-moduli-dimension` | 満supportで第三Veroneseと次数一の大域中心元・平坦中心商が被約Poisson層へ降下。古典Projの偏極O(3)、底の次元2k、四様体rank4では四 | 重み零の降下、正則商の完全列、相対Projの局所同定。全層gerbeは位数三。固定h≠0での像の次元、VeroneseのAS-regular性、相対qgr同値や全fiberの滑らかさは未主張 |
| `prop:pg-intrinsic-zero-matching-obstruction` | N>=6、全supportの任意の偶中心元は零制限の標準直線O sym(F)へ全層で一致できない。同変性不要 | ω₂=−H/12+aF+cの大域分解、Zの閉性、P重み二のH⁰消滅、H_Z=8u₁u₂u₃の滑らかな例、非零接続類∂(H_Z/12)∈H¹(I_Z C)。ambient同一視下のideal非一致であり、抽象商やqgrの非同値は未主張 |
| `prop:pg-equivariant-global-centering-obstruction` | m>=1、全f・η・hに依存しても全零h切断近傍のG共変な補空間選択Bは存在しない。U商は非自明torsorかつ非アフィン代数空間 | Stiefel開の左逆R(A)A=I₃、余次元m+1の境界とA=0での矛盾。gradient正則列による自由性、U変換則を保つLevi平均、アフィン底の加法群torsor消滅。中心元そのものの不存在とは区別 |
| `rem:pg-cmr-nodal-comparison` | CMR既知のγ=0中心公式を節点Jacobian関係へ移し、t=0で正則かつ古典剰余fの中心元を得る | accepted v2の式(4.38)–(4.39)、別の同変左逆、q=p/s等の係数対応、Q=s⁵Ω_CMR/(6t)+κ、交換差−6A₃ℓ₃t³と純中心補正。既知の存在・公式と本稿の相対適用を区別 |
| `thm:pg-quantization`（`algebraic_quantization.tex`）、`thm:pg-ad-all-poisson` | 全Poisson構造について原点を含むZariski開上のAS-regular ambientと中心正則三次商 | 中心三次配分、PBW、Koszul tensor、中心元の正則性、AS-Gorenstein change of rings |
| `thm:pg-all-dimensions`、`cor:pg-ad-whole-pencil`、`prop:pg-ad-intrinsic-hessian` | 各純active三次が滑らかな場合は独立多変数底と短い多項式中心公式 | 係数環上の自由性、全パラメータでの多項式中心性、交差補正がないこと |
| `thm:pg-ambient-recovery-general`、`thm:pg-ambient-recovery-polarized`、`ambient_recovery_general.tex` | 二次包絡と三次核。圏からの復元には本文のnoetherian・AS-Gorenstein条件 | 低次数積、section algebra、飽和のExt消滅 |
| `prop:pg-ambient-even`、`cor:pg-ambient-derived-threefold` | C上、二変数中心、中心上自由性、左右noetherian性、所定のSerre関手を仮定 | conicからの中心復元、局所化と交叉、次数の再設定、必要仮定の明示 |

中心変数が残るm>0、k>=2での一般の同変中心元、全hへの延長、全閉パラメータのqgr滑らかさは未解決である。
同一ambient内の中心イデアルの不一致は、抽象商の非同型やMorita/qgr非同値を意味しない。
可換復元の一般点定理の仮定と、任意の特殊ファイバーを含む相対同値を区別する。

## 構造上の要点

### 階数二の全supportの中心核と代数的持上げ

S=T_smooth×C₃^×上でK₀=OF⊕Sym³(V/W_P)*である。
普遍jet命題のΘ=sym(F−h²H(P,F)/12)はDΘ∈h⁴を満たし、
局所核の底変更との両立によりΘ mod h³はK/h³Kの大域切断となる。
Gr(3,N)上の全整数twistのH¹消滅から、この初期値は全h冪厚化へ整合的に持ち上がる。
ここで得る形式中心元の各Weyl係数は、Stiefel開の補集合の余次元N−2>=2と
SL3-torsorの関数降下により、有限生成環A_N=Γ(T_smooth,O)⊗C[Mat_(N,3)]^(SL3)に属する。
錐の射影正規性や全supportにわたる補空間選択は仮定しない。

有限次数三・四のWeyl同型が成立する不変principal開D(q)、q mod h=1上で、
R=A_N[h,q⁻¹]、K=ker MとするとKは有限R加群である。
完備化の完全性からKhat=ker Mhat、Khat/h³Khat≅K/h³Kであり、
形式中心元の剰余類をKの元で代表してΩ≡Θ mod h³を得る。
K/h³K→(自由加群)/h³の単射性を使う議論ではなく、包含と剰余写像の可換性を用いる。
ΘのH_N共変性と偶性により平均化でも指定jetは保たれ、偶性から剰余はO(h⁴)となる。
指定した形式級数全体との一致は必要ない。P=0での核の階数跳躍もこの有限加群の操作を妨げない。
全次数PBWと正則中心商は、別に既存の局所PBW/AS開へ制限して得る。

全fに依存する中心調整Bを仮定すると、固定smooth FをStiefel開へ引き戻して
R(A)A=I₃を満たす正則左逆が得られる。その全行列空間への延長はA=0で矛盾する。
U作用が自由でも商がアフィンとは限らず、本件では非自明U-torsorの商Yは非アフィンである。
したがって自由商上のアフィン平均化に置き換える方法も使えない。
この障害は中心核を直接扱う上の存在証明とは両立する。

中心スカラーK_sc={(cI,c⁻³)}を除いた商は全rank2被約Poisson層である。
gcd(N,3)=1の指標θ=(det L)^rλ^s、Nr−3s=1により次数重みを除く。
この元の次数の降下では、中心三次直線の一つの大域生成元までを結論しない。
N=5の底の次元17は固定h≠0の非可換同型類像の次元ではない。

全係数底SのPicard群が零であることと、同変線束の線形化の単元計算から、
gerbeの中心重み像はgcd(N,3)Z、位数はgcd(N,3)となる。
3|Nでは重み一線束を用いる元の次数の補正が不可能だが、
A_(3d)⊗λ^d、B_(3d)⊗λ^dは全Nで重み零なので降下する。
Ωの共変性により第三Veroneseではω=Ω⊗1が次数一の大域中心元となる。
この代数族の降下と、左右noetherianである各閉ファイバーのqgr Veronese同値は別々に証明する。
Smith訂正文の追加条件は、V(Tor_1^T(N,R))=0からπIの完全性を確認して満たす。

零制限Z={F|W_P=0}はN>=6で非空の閉部分である。
任意の大域中心元の二次係数はω₂=−H/12+aF+cと大域分解される。
標準直線O sym(F)との全層での一致にはc|Z=H_Z/12が必要だが、
BottによりΓ(S,C)のP重み二成分は零、H_Zは非零となり得る。
これが非零の接続類∂(H_Z/12)∈H¹(S,I_Z C)を与える。
詳細例とaffine torsor・dilatationとの関係は `notes/cubic_quantization.md` §2(IX)、§3に保持する。
この一致障害を中心商の抽象非同型やqgr非同値へ読み替えない。

### 満supportの有限jetの直接持上げ

N=3k、k>=2では、Pが定めるブロック上でF=Σg_sと内在的に分かれ、
F smoothと各g_s smoothは同値である。J=SL₃^k⋊S_kは還元的なのでGL_N/Jはアフィン。
その上の階数10kの係数束の判別式主開S_(N,k)もアフィンである。
各一ブロック核K_sは階数一で、直和はブロック多重次数によって三次束の局所直和因子になる。
古典核⊕Cg_sと全交換子行列のminorから、全零h切断近傍でK=⊕K_s、rank K=kとし、
核・像・余核の形成を任意底変更と両立させる。

不変なアフィン主開D(q)、q mod h=1上でΘ mod h³∈K/h³Kを取る。
有限射影加群Kからの剰余写像の全射により代数的に持ち上げ、λΦのtwistと偶平均で
共変性と指定二次jetを保つ。階数二のBWB・形式持上げ・完備化はここでは使わない。
有限étale順序付け被覆上で全ブロック成分の零点を除くと、全零切断を保った開が元の底へ降りる。
一ブロックだけの次数filtrationで左右正則性を示し、各次数の正則商の完全列から局所自由性を得る。
テンソル積代数全体のdomain性を仮定しない。

満supportの第三Veroneseは全被約rank2k層へ降下し、gerbe位数は三である。
底の次元2kは相対Poissonモジュライの次元であって固定h≠0の非可換同型類像の次元ではない。
m>0では軌道が非アフィンなので同じアフィン性の証明は使えないが、
判別式開の非アフィン性や同時中心元の不存在までは結論しない。

### 特異制限の軌道と中心スカラーの除去

節点・尖点では、方程式scaleを含む安定化群に同変な明示左逆を標準形で作る。
σ_{(M,λ)g_*}=Mσ_*ρ₂(M,λ)⁻¹は右安定化群作用に不変なので、
軌道L/H上の正則な写像へ降りる。各gの標準形への座標変換を大域的に選ぶ必要はない。
このσを中心調整に使うと、各係数層の全零切断を含む不変principal開が得られる。
各軌道での分裂と、不可約三次式全域での単一の分裂は区別する。
後者は可約式の錐の余次元2による正則関数の延長とδ_0=0に反する。

各gの唯一の特異点は、軌道上の正則な同変射O_γ→P(W)を与える。
そのtautological直線ℓの点の順方向の写像はMだが、代数のΦと同じ向きの引戻しデータはM⁻¹である。
従ってℓの中心スカラー重みは−1であり、A_d⊗ℓ^d、J⊗ℓ³、B_d⊗ℓ^dの重みが零になる。
重み+1の双対線束をLと書くなら同じ補正はA_d⊗L⁻ᵈである。
積と中心イデアルも整合して降りるため、代数そのものの降下である。
重み一の線束にframeを付けたスタックが底とfppf局所的に同型となる直接証明から、gerbeも中立となる。
この方法は群の指標による分裂と異なり、mに合同条件を課さない。

support平面とXの交わりが節点・尖点曲線である条件は、support平面そのものがXに含まれる零制限条件とは異なる。
節点・尖点層の余次元1・2および底の次元16・15は、固定したh≠0での非可換同型類の像の次元ではない。
これら層別の式の全hへの延長、全supportの別の選択との一致、
降下後の大域中心生成元の存在は主張しない。
接線とconicの軌道でのδの同変非分裂は `notes/cubic_quantization.md` §2(VIII) に独立な障害として記録する。
これらの障害は中心調整の方法に関するものであり、
中心核を直接扱う全supportのH_N共変中心元定理とは両立する。

### 中心二変数とambient復元

$S=\mathbf C[u,v]$、$D=S^{(2)}=\mathbf C[a,b,c]/(ac-b^2)$ とする。
$D_1$ のconicのgraded自己同型は $GL_2/\{\pm1\}$ から来る。
偶数Veroneseを元の次数の2倍に戻してからSとtensorし、uとvの局所化を取る。
$S[u^{-1}]=D[(u^2)^{-1}]\oplus uD[(u^2)^{-1}]$ と奇数部分の記述、
S自由基底に関する交叉から元の代数を回復する。
このため商代数自身のS自由性が必要である。

**ambientのPBW性だけでは商のS自由性は従わない。** 例えば $A/(u^3)$ はS-torsionを持つ。
active filtrationに関して中心三次元Gの最高記号 $g_3$ が正則で、
$\operatorname{gr}A=S_{f_3}\otimes S$ なら
$\operatorname{gr}(A/(G))=(S_{f_3}/(g_3))\otimes S$ となり、斉次基底の持上げでS自由性を得る。
これは `eq:pg-ambient-quotient-symbol` の十分条件である。
導来復元の系にはAの左右noetherian性を明示し、BのAS-Gorenstein injective dimension 4からsection algebraを回復する。

## 代数的中心元の証明の依存

1. `lem:pg-det-gradient-coprime`：全体fの滑らかさから $\gcd(f_x,f_y,f_z)=1$。
   共通因子と中心偏微分を同時に消す非零点がKrullの高さ定理から生じれば、全勾配の零点となって矛盾する。
2. `lem:pg-det-classical-kernel`：三次古典Casimirは $\mathbf C f+\mathbf C[u]_3$。
   分数体上の比例係数はgcd=1により多項式で、斉次次数から定数となる。
3. `lem:pg-det-universal-rank`：有限表示の次数別行列は被約な係数底上で一定階数を持ち、局所自由な商を与える。
   各固定fのh曲線上で、滑らかなactive制限に対するHesse中心公式から小行列式の消滅を得る。
   その後fを動かして普遍恒等式とする。Hesse座標の代数的な同時選択は仮定しない。
4. `thm:pg-universal-determinant`：古典rankの非零小行列を局所化し、Cramer法で $\Omega_0=f$ を規格化する。
   語の反転と $h\mapsto-h$ により係数は $h^2$ の有理関数となり、分母は原点で消えない。
5. `thm:pg-det-global-coefficient-lift`：固定した全係数空間の零切断全体を含む偶principal開へ縮める。
   割った交換子行列をτ=h²へ降ろし、factorial係数環のPic=0と特殊化の単元補正で全係数に正則な中心元を得る。
   規格化変更のaffine遷移は同じ中心イデアルを保証しない。実例と同変降下の条件は `notes/cubic_quantization.md`。
6. `thm:pg-equivariant-levi-center`、`thm:pg-equivariant-parabolic-center`：
   affine底上でReynolds平均を定義開・中心元・方向微分の左逆へ適用する。
   滑らかなgではこの左逆を、節点・尖点では`lem:pg-equivariant-singular-retractions`の軌道上の左逆を用いる。
   混合二次項からB_fを作り、B_f'=(MB_f−C)N^-1を用いて全G同変に戻す。
   純中心係数の固定は全平行移動との同変性に一般には両立しないため、この規格化を外す。
   g=0は`thm:pg-equivariant-zero-center`のPBW対称化で全tの全G共変性を別途証明する。
   G_0選択では指定閉部分を(t=0)∪(g=0)として、この標準元への一致も保てる。
   節点・尖点層のモジュライ降下は、特異点直線による重み補正を別途用いる。
   同変な中心元の選択、gerbe上の族、底のPoisson層への代数の降下はそれぞれ区別する。
7. `lem:pg-central-splitting-smooth`：純中心三次を各ブロックへ配分する。
   $u=0$ は全体Xの滑らかさ、$u\ne0$ は基点自由な線形系のBertiniを用いる。
   射影線形系のうち元のブロックの係数が非零のchartで係数を1に規格化し、必要なアフィン配分空間に戻る。
8. `thm:pg-quantization`、`thm:pg-ad-all-poisson`：各中心元の和、共有中心上のPBW/Koszul性、
   一つのactive blockのfiltrationによる正則性から、全Poisson構造と固定正規形のpencilを量子化する。
   非可換domainのtensor積が常にdomainである、という一般には誤る命題は使わない。
9. `thm:pg-intrinsic-rank-two-center`：全supportの古典核のH¹消滅から形式持上げを行う。
   Stiefel開・Hilbert有限生成・有限Weyl行列を介し、Noetherian完備化の完全性で
   普遍Hessian二次jetを保つ代数的中心元を得てH_Nで平均する。
   初期値はΘ mod h³∈K/h³K、有限核への移行もmod h³で行う。外部formalityを存在入力には用いない。
   形式中心元存在自体と相対・還元群への対応はEG Proposition 8.1.1(i)に既にある。
10. `cor:pg-intrinsic-rank-two-descent`：全rank2被約Poisson層の商表示と、
    gcd(N,3)=1の重み一指標による次数補正を用いる。
    中心線の選択・gerbe上の族・rigidification後の代数の降下を区別する。
    `prop:pg-intrinsic-gerbe-period` はPicard群と中心重みから残る位数三の障害を確定し、
    `cor:pg-intrinsic-third-veronese-descent` は重み−3dのλ^dで全Nの降下を与える。
11. `prop:pg-intrinsic-zero-matching-obstruction`：普遍二次jetとBottの重み二H⁰消滅を組み合わせる。
    Z上のHessianが非零の純中心切断であるため、標準直線への全域一致は相対H¹で妨げられる。
    これは同変性を課さない任意の大域偶中心元にも適用する。
12. `thm:pg-intrinsic-full-support-center`：N=3kでは還元的安定化群による軌道と係数底がアフィン。
    一ブロック核の直和と古典階数から全量子核の階数kを得て、Θ mod h³を有限射影核から直接持ち上げる。
    平均化、各ブロック成分の非零条件、一ブロックfiltrationにより、共変な指定jetと正則平坦商を得る。
    形式的持上げや完備化はこの証明に用いない。
13. `prop:pg-intrinsic-all-rank-gerbe` は全被約rank2k層の位数をFermat点の交換子から決定する。
    `cor:pg-full-support-veronese-descent` は満supportで構成した族を重み零にして降ろす。
    m>0、k>=2の中心元存在は、全階数でのgerbeの計算からは従わない。

任意の滑らかなactive制限に対する短い多項式公式はHesse標準形への帰着で得る。零制限はPBW対称化が全tで適用でき、非零の特異な一般制限はCramer構成で扱う。個別の非零特異例には別途明示式がある。
普遍Hesse証明書は独立混合係数を保持した有理関数体上の恒等式であり、数値特殊化による推測ではない。
内在的な二次補正は $H(P,F)=\frac16\sum P^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}$、
正規形では $\sum_s\lambda_s^2\det\operatorname{Hess}_{x_s}(f_s)$。
四次補正を一つの座標不変式と断定しない。
詳しい公式、例、Dolgushevによる代替形式ルートの制約は `notes/cubic_quantization.md` を参照する。


## 一次文献と位置づけ

| 文献 | 確認した所在・適用範囲 | 本稿との関係 |
| --- | --- | --- |
| Etingof, MIT 2024 lecture notes | Cor.13.7–13.8 p.75、Prop.16.9 p.88、Def.21.13/Lem.21.14 p.114、Thm.25.17 p.137、§32.2 p.173 | PBW対称化の随伴同変性、可解根基、最高ウェイト、最高根の既知入力 |
| Mori--Smith, Math. Z. 287 (2017), 215--241, DOI 10.1007/s00209-016-1824-5 | 本文確認はarXiv:1502.07403v2。Thm.1.4 p.5、Cor.2.7 p.11/2.9 p.12、Thm.4.2 pp.16–17、Lemma 7.1/Thm.7.2 pp.23--24 | standard性、AS-regular/3-CY、滑らかな平面三次で全パラメータの判定、point curve |
| Berger--Taillefer, JNCG 1 (2007), 241--270, DOI 10.4171/JNCG/6 | 刊行PDFのThm.1.1(i) p.242、Thm.3.1 p.246、Thm.3.6 p.251 | 低次数potentialからのPBW変形。(ii)の逆向き分類の追加条件は使わない |
| Le Bruyn--Smith--Van den Bergh, Math. Z. 222 (1996), 171--212 | 著者PDF、Thm.2.6/Cor.2.7、Thm.3.1.3 | 中心正則拡大。Fermatブロックのパラメータ代入を本文で明示 |
| Smith--Tate; De Laet--Le Bruyn | 後者arXiv:1405.1158v1 §2 p.3 | 純Sklyanin中心公式は既知。本稿は固定係数環の無極な規格化、普遍恒等式、Cramer構成を扱う。表示の誤植注意は中心ノートに記載 |
| Etingof--Ginzburg, JEMS 12 (2010), 1371–1416, DOI 10.4171/JEMS/235 | 刊行Thm.3.3.2(ii) p.1385、Prop.8.1.1(i) p.1407・証明pp.1407–1408、§8.3 pp.1410–1411、§9 p.1414 | 一ブロックの中心元存在・特殊化・Rains公式に加え、指定古典剰余を持つ形式中心と相対・還元群に対応した形式性も既知。本稿の追加は動く全support上の同時代数的選択と被約層への降下 |
| Chekhov–Mazzocco–Rubtsov, Adv. Math. 376 (2021), 107442, DOI 10.1016/j.aim.2020.107442 | 本文確認はaccepted arXiv:1905.02772v2。式(4.38) p.21、Lemma 4.6・式(4.39) p.22、Table 5 p.41 | γ=0の場合の節点型中心元は既知。本稿は一般混合二次項からの移送、対称Jacobian関係への係数対応、t=0の規格化と安定化群共変な純中心補正を明示 |
| Guo–Lu–Sharpe, arXiv:1605.01410v2 | [本文](https://arxiv.org/pdf/1605.01410v2)、§2.2 Thm.2.3 pp.5–6、Thm.2.4の証明 | Grassmann多様体上のBWBの重み規約と負の最高重みを確認。全整数twistのH¹消滅への適用は本稿で計算 |
| Lurie, *A proof of the Borel–Weil–Bott theorem* | [著者公開ノート](https://www.math.harvard.edu/~lurie/papers/bwb.pdf)、Thm.5と証明 p.3。PDF内に刊行年の記載なし | BWB一般定理の確認に使用。Bott原論文・Weyman原書を直接読了したとはしない |
| Derksen, Advances in Mathematics 141 (1999), 366–384 | [著者公開刊行PDF](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.4.pdf)、Thm.2.1 pp.368–369、Reynoldsの性質p.369 | Hilbert有限生成とstable部分加群を保つReynolds射影は既知。SL3不変環のNoetherian性、不変開・有限中心核の平均に適用 |
| Arzhantsev, *Invariant Ideals and Matsushima's Criterion*, Commun. Algebra 36 (2008), 4368–4374, DOI 10.1080/00927870802179347 | 実読は[arXiv:math/0506430v1](https://arxiv.org/abs/math/0506430v1)、§2 Thm.2.1・Prop.2.2 p.2、標数零の仮定p.1 | 還元的部分群Hに対するG/Hのアフィン性は既知。満supportのSL₃^k⋊S_kと係数束の判別式主開へ適用。刊行レイアウトを照合したとはしない |
| Stacks Project [00MA](https://stacks.math.columbia.edu/tag/00MA)・[00MB](https://stacks.math.columbia.edu/tag/00MB) | Lemmas 10.97.1–10.97.2 | Noetherian有限加群の完備化の完全性・テンソル積との一致。形式中心の指定二次jetを有限核から代数的に持ち上げる |
| Stacks Project [06PH](https://stacks.math.columbia.edu/tag/06PH)・[03OY](https://stacks.math.columbia.edu/tag/03OY) | Lemma 80.11.7、§59.22のThm.59.22.4 | flat・局所有限表示群の自由作用の代数空間商とfppf torsor、準連接層のfppf/Zariskiコホモロジー比較。U商の非アフィン性へ適用 |
| Milne, *Algebraic Groups*, CUP 2022 | [著者PDF](https://www.jmilne.org/math/Books/iAG2022.pdf)、Props.7.12, 7.17 pp.142–143 | 軌道L/Hと忠実平坦な軌道写像は既知。標準形での同変左逆を軌道上へ正則に移送するために用い、軌道のaffine性を追加仮定しない |
| Bergh–Schnürer, Doc. Math. 26 (2021), 1465–1500, DOI 10.4171/DM/846 | [刊行PDF](https://ems.press/content/serial-article-files/26626?nt=1)、Prop.4.10 p.1487 | gerbe上の重み零の準連接層の降下は既知。次数付き代数・積・中心イデアルへ適用。重み一の直線によるgerbe中立化は本文のframeを用いる直接証明であり、同命題へ誤帰属しない |
| Lieblich, Compos. Math. 144 (2008), 1–31、[DOI](https://doi.org/10.1112/S0010437X07003144) | Lemma 3.1.1.8 p.7 | 重みnの可逆層とn倍gerbe類の消滅は既知。同節の底は代数空間なのでスタック底のcocycle証明も本文に記す。階数二のPic(S)=0と、全階数のFermat交換子による位数gcd(N,3)は本稿の個別計算 |
| Smith, *Maps between non-commutative spaces*, Trans. AMS 356 (2004), 2927–2944 | [著者PDF](https://sites.math.washington.edu/~smith/Research/Maps.pdf)、Thm.4.1 p.2934、Prop.4.8 pp.2940–2941。訂正文[arXiv:1507.02497v2](https://arxiv.org/abs/1507.02497v2)、Lemma 1.1 pp.1–4も確認 | 次数一生成の場合のVeronese同値は既知。訂正文のTor条件を直接確認し、qgrへの適用は左右noetherian閉ファイバーに限定。訂正文刊行DOI 10.1090/tran/6908 |
| Van den Bergh, *Non-commutative P¹-bundles over commutative schemes*, Trans. AMS 364 (2012), 6279–6313 | 実読は[arXiv:math/0102005v3](https://arxiv.org/abs/math/0102005v3)、§4.2 p.9、Lemma 4.2.3直後。刊行DOI 10.1090/S0002-9947-2012-05469-9 | sheaf Z-algebraの可逆bimoduleによるtwistと次数付き加群の同値は既知。底の線束の次数冪による補正へ適用 |
| Dolgushev, Selecta Math. 14 (2009), 199--228, DOI 10.1007/s00029-008-0062-z | 本文確認はarXiv:math/0612288v3 Prop.1 p.9、Thm.3 pp.15--16 | 条件は全形式Poisson classのunimodularity。本稿の代数化の証明には用いない |
| SGA 2 XII Cor.3.7、Stacks Tags 06FI/0BCH/06PD/06WT、Artin--Zhang | Picard群、商stack、UFDのPic=0、gerbe判定、同変準連接層の降下、section algebra | モジュライ・係数空間上の中心元・偏極付き復元の既知の一般原理 |

Hesse表示の混合二次項Axy+Byz+Czxは、t可逆なら
x=X−B/t、y=Y−C/t、z=Z−A/tで消える。残る低次項は各一変数の多項式で、
q=(1+ht/2)/(1−ht/2)、μ=h/(1−ht/2)によりEG§9の交換関係へ移る。
全残余係数と自由語の関係は `rem:pg-hesse-eg-translation` と
`computations/quantization/verify_hesse_translation.py` に明示した。
この座標変換がt=0で使えないことから、全ての座標変換による既知公式への帰着不能を結論しない。
混合係数を含むことだけを初出の根拠にせず、指定した係数環・古典極限・正則性を比較する。
EG刊行本文: https://ems.press/content/serial-article-files/31746

EG Proposition 8.1.1(i), p.1407は、正の重みa,b,c、d=a+b+cについて
Φ=xyz−yxz+Σ_(j≥1)h^jΦ_j、deg Φ_j≤dという三生成元potentialに、
古典剰余(Φ₁)^abを持つ次数d以下の形式中心元を与える。
孤立特異点は同命題(ii),(iii)の追加仮定であり、(i)には不要である。
証明pp.1407–1408はR=C[u]を基底とする相対構成を用い、
還元群作用に対応するKontsevichの形式性とその相対版も明記している。
従って指定古典剰余の形式中心元存在、相対・同変な形式構成、
形式解から有限条件を取り出す一般原理だけを本稿の新規性とはしない。
現行稿では、階数二の全smooth F・全非零support、および満supportの全適合smooth Fの係数底で、
一つの代数的中心元を同時に選び、全H_N共変性と被約Poisson層への代数族の降下まで制御する主張を区別する。

CMRとの具体対応は、f°=x³+y³+xyz+ΣA_i x_i²+Σℓ_i x_i+κに対し、
p=1+t/2、s=1−t/2、q_CMR=p/s、α=β=3t/s、γ=0、
(a₁,b₁,c₁)=−2t(A₁,A₂,A₃)/s、(a₂,b₂,c₂)=−t(ℓ₁,ℓ₂,ℓ₃)/sである。
Q=s⁵Ω_CMR/(6t)+κの係数はt=0で正則、古典極限はf°となり、
x,y交換とt↦−tの差−6A₃ℓ₃t³をQhat=Q−3A₃ℓ₃t³で補正する。
任意の二次混合項への移送を含む詳細は `rem:pg-cmr-nodal-comparison` と
`notes/cubic_quantization.md` §2(VIII)にある。
CMRの刊行書誌とaccepted versionの本文確認を区別し、刊行レイアウトを照合したとはしない。


節点・尖点層についても、軌道への移送と重み零降下の原理自体は既知として扱う。
本稿の明示的な左逆、係数族の中心調整、特異点直線を用いた中心商族の下降という包括的な適用の初出は未確定である。
全supportのBWB計算・有限核の完備化・還元的平均を結んだ同時代数的選択についても、
一般原理と本稿の適用を区別し、包括的な初出は未確定とする。
満supportのアフィン性・有限jetからの直接持上げ・第三Veronese降下も、
既知のアフィン商・還元的平均・重み零降下の適用として記述し、包括的な初出は未確定とする。
刊行書誌を確認したことと、その刊行版の定理番号・証明全文を再照合したことも区別する。


## 有限計算の範囲

以下は移管前の実行証拠を保持する検算一覧である。今回の実行は [validation_quantization.json](../validation_quantization.json) と計算資産READMEで明示し、全件を新たに再実行したとは扱わない。

| スクリプト（computations/quantization/） | 保持する検算の範囲 |
| --- | --- |
| `verify_general_dimension_multiblock.py` | A-v61で実行、六例PASS。独立Poisson係数による古典Jacobi・F-Casimir・異ブロックHessian消滅・内在的Hessian縮約を検算。量子中心元の存在・厳密中心性、核の定階数と底変更、コホモロジー・gerbe位数・降下の検証ではない |
| `verify_cmr_nodal_center.py --json` | A-v59のPASSを保持、移管前の監査時には未再実行。独立QQ係数でCMR γ=0関係の唯一のzyx重なり、三中心交換子、Jacobian関係への係数対応、Qのt=0正則性・古典極限、交換差とQhatの純中心補正、スカラー・μ₃重みを検算。sp≠0での計算でありt=±2のPBW・平坦性、Weyl偶性、安定化群の完全分類・軌道移送・モジュライ降下は対象外 |
| `verify_singular_orbit_centering.py --json` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。独立10係数と3並進係数、nodeの全生成子・cuspの対角torusでσδ=id、B_fと中心調整式の共変性を検算。接線とconicでは左逆・Lie同変性の線形系のrank18/拡大rank19、torus制限後rank4/拡大rank5。二つの拡張例の勾配イデアルへの純冪の所属をQQ Groebnerで確認。安定化群の完全分類、一般GLの軌道移送、quantum中心性・モジュライ降下の計算機証明ではない |
| `verify_zero_restriction_center.py --json` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。QQ上の独立10係数とt、独立3並進係数でzyxの重なり、全3中心交換子、関係式と中心元の並進共変性が恒等的に零。数値特殊化・t打切り・分母なし。一般線形変換・AS条件・幾何・降下の検算ではない |
| `verify_hesse_translation.py` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。独立全係数で平行移動後の三次式を定数項まで照合し、三つの交換関係を自由語の有理係数で照合。中心性・PBW性の検証ではない |
| `verify_equivariant_centering.py` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。25混合係数を記号のまま保持。二組の座標変換で左逆、B_fの変換、中心調整した三次式、三つのJacobian括弧がPASS。Reynolds存在や全群定理の計算機証明ではない |
| `verify_universal_hesse_mixed_center.py` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。339基底語、162関係倍数、rank 144。Q(h,t)上で独立な6混合係数を保持し、3交換子が恒等的に零 |
| `verify_cubic_casimir_jet.py` | A-v60のPASSを保持、移管前の監査時には未再実行。20自由係数、x,y,z各交換子の125個の語・次数係数が零。計算はh⁴を法とする恒等式、偶性によるh⁵への補強と全次数持上げは本文の証明。有限jet検算だけで厳密中心性を結論しない |
| `verify_singular_cubic_classical_kernel.py` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。active制限0の滑らかな例で378×56行列のrank 45、核次元11 |
| `verify_nonelliptic_quantization.py` | 実施済み結果を引継ぎ、移管前の監査時には未再実行。二つのmonic Diamond系と重なり、六普遍中心交換子、h=0極限、potential syzygy、分母範囲、二つのnegative control、17項Fermat恒等式がPASS。実行時の再計算は保存JSON全体と厳密一致 |

量子化後の非楕円ブロックの行列式曲線は `verify_nonelliptic_point_curves.py` と `nonelliptic_point_curves_certificate.json` に分離した。
BWB消滅、満supportのアフィン性、指定jetを保つ有限核の持上げ、gerbe位数、Veronese降下、零制限一致の相対H¹障害、U商の非アフィン性は本文の一般証明であり、有限計算や形式証明器で確認したとはしない。

再現手順は [computations/quantization/README.md](../computations/quantization/README.md)、当面の数学的課題は [cubic_quantization.md](cubic_quantization.md) §3 に置く。
