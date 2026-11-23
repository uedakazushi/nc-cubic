# 非可換三次 n-fold：可換 Ku 実現を中心とする研究方針

2026年11月23日 / v82。再開時は本書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。正本は `uedakazushi/nc-cubic` の `main`、主公表原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)（日本語LuaLaTeX、著者欄空欄）。

## 公表用原稿と証明の正本

| 原稿 | 役割 |
| --- | --- |
| [nc-cubic.tex](papers/nc-cubic.tex) | 本文を持つ主稿。主予想、一般点可換復元、楕円windowと分離比較、残余圏の認識・可換実現の開性、三様体の点スキーム不一致例。 |
| [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) | 構造対象付きモジュライ、表示認識、相対点・Poisson幾何、Picard/Brauer/Kummer降下、周期位相と比較次数。 |
| [mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) | 混合族の中心・局所代数・全smooth locus、任意固定楕円因子の全許容PBW・中心比較、全smooth多中心対象の比較と中央Bertini、固定tensor境界のPBW分解とClifford混合族、零係数の球面接着と有限MF模型、指定h候補の一般点核と整延長、被約point/Poisson不一致例。 |

研究方針とノートは三稿で共有する。各証明は一つの本文を正本とし、他稿では定理番号と稿名を参照する。組版の共通設定は `papers/common/preamble.tex`、書誌は `papers/references.tex`。主比較に必要な楕円windowは主稿の `comparison_foundations.tex` に置き、精密な核の降下を主比較の前提にしない。混合稿の余有限Ku実現は主稿の比較と開性を入力とする。

## 主予想と未解決の核心

**Main conjecture（主予想）**：任意の滑らかな非可換三次 n-fold 𝒳 に対して、同じ次元の滑らかな可換三次超曲面 X が存在し、Ku(𝒳)≃Ku(X) となる。

まず基礎体をC、次元をn≥3とし、通常のC線型dg Morita同値の存在を最優先にする。任意に固定した滑らかな標準Sklyanin因子の組、k≥2、固定非零重み、一つの共有中心変数について、指定境界を保つ全ての因子別PBW・中心三次補正の残余線束圏を可換三次と普遍Morita比較した（`emc:prop:coverage`, `euk:thm:universal-kernel`）。異なるj、同種・CM、二捩れ、有限位数・無限位数を許す。二捩れでない因子は平行移動後の関係式の線形三方向、二捩れ因子は中心へ加えるu倍の平方三方向を一次係数tとする。標的はX=V(G+uQ(t)+u²L(t,α)+u³C(t,α,c))、L=𝔄α+R₂(t)、C=κc+R₁,₁(t,α)+R₃(t)で、𝔄は可逆、κ≠0。可換smooth開では相対perfect核と全coherent Ku同値を得る。定数Bocksteinは3k次元の同型、一次Bocksteinは3k方向で単射だが、比較の存在は単射性を前提としない。各固定tの一般αに対して8^k個の相異なる悪いcと各可換標的の唯一の通常二重点を得て、全係数・各固定tの判別超曲面は既約被約、臨界点のaffine空間が正規化となる。固定(t,α)の一変数特殊化には重複根を許す。

任意個の共有中心変数m≥1を持つ全許容因子別表示で、残余線束圏がsmoothであることと、一中心の係数多項式を偏極した可換三次X_polが滑らかであることを同値とした（`mcb:thm:smooth-locus`）。厳密な中心作用から作る原点blow-up圏、KhanのArtin stack上の分解、各chartへの一中心普遍核、絶対対角のZariski局所性を使い、有限中心性を仮定しない。滑らかな対象には各中間商もsmoothな一般中央flagが存在する（`mcb:thm:central-flags`）。従って、固定因子k≥2・非零重み・任意mの全smooth対象について、次元n=3k+m−2の滑らかな可換三次への全coherent Ku同値を得る（`mcb:cor:all-smooth-comparison`）。ここで実比較の標的は逐次構成のX_itであり、X_polへの実核を同定したとはしない。

全係数の非smooth locusは勾配resultant 𝔇_m=Res(∂W_pol)の零集合に一致し、係数t,α,cの重みを1,2,3とするとdeg_wt 𝔇_m=3m·2^(3k+m−1)となる（`mcb:cor:global-discriminant`）。この全係数多項式の既約性・被約性は未主張である。

二中心ではsmoothnessからΔ≢0が従い、良い中央切断の仮定は不要となる。Δは次数3·8^kである。固定した滑らかな境界からの横断二項写像Bは可逆で、二次・三次係数は三角多項式同型をなす（`mtb:prop:transverse-iso`）。各固定一次係数の一般二次係数では、最後のv³係数の悪い値は相異なる2·8^k個で、各可換標的には唯一の通常二重点がある。全横断係数および各固定一次係数の判別因子は既約被約で、臨界点のaffine空間が正規化となる（`mtd:thm:normalization`）。任意mの各比較段でも同様で、最後の悪い値の数は2^(3k+m−1)。特殊二次係数では重複根を許す。

固定tensor境界と厳密な中心変数を持つ全二次PBW表示について、因子間の一次・定数補正と内部関係の他因子出力は、元の生成元のまま全て零になる（`ifp:thm:factorization`）。任意の可換係数環、非被約環、異なる因子と二捩れ因子を許す。従って指定中心三次の存在を仮定すれば、既存の正規形・全smooth locus・全coherent Ku比較を適用でき、変形後の因子間可換性は追加仮定から外れる（`ifp:cor:central-comparison`）。抽象的には各因子のDer₋₁=0とZ₁=0だけで同じ分解が従う。

二次境界自体を変える次数零変形では、Euler混合類の指定中心障害は単射である。一方、二捩れ因子の集合I₂について混合核は⊕_{i≠j,j∈I₂}HH²(S_i)₋₂⊗Z(S_j)₂、次元9|I₂|(k−1)となる（`ifh:prop:central-mixed-obstruction`）。任意の混合中心補正と全次数零gaugeを許した結論である。一つのordered pairの九方向は、定数型普遍パラメータへClifford中心平方を代入した全係数族に積分でき、中心三次とその自由商を得る（`ifc:thm:family`, `ifc:prop:tangent`）。この周囲代数は全係数で相対Koszul・untwisted相対6-CY、複素fiberではAS-regular dimension/index6である（`ifr:thm:ambient-regularity`）。

中心変数なしの四次元型と、m=1,g=cu³,c≠0の五次元型の九変数族には、分離原点を含む実相対smooth proper開とétale局所perfect比較核がある（`iff:thm:smooth-neighborhood`）。四次元ではrotationを持ち上げる通常Artin変形の全次数認識を用いる（主稿 `ifk:thm:rotation-formal`）。残余KSはJac(f₁)₁⊗Jac(f₂)₂への同型で階数9、幾何的な20次元形式変形空間への形式像は余次元11である（`ift:thm:rank-nine`, `ift:cor:first-jet`）。

両因子がCliffordの場合には双方向十八変数を積分し、全係数で中心平方上の自由階数64の二次代数を得る。二次双対は可換六二次式商のcocycle twistである。この可換商は六二次式のresultant開D(Δ)上で完全交叉となり、この開が周囲代数の有限大域次元・AS-regular領域と正確に一致する。ここで次元/index6、任意底変更に保たれる有限射影Koszul解消とuntwisted相対6-CYを持つ（`ifb:thm:regularity`, `ifb:cor:exact-regular-locus`）。別の明示的主開D(c)上で中心三次は普遍正則、商は平坦となる。τ₁=τ₂=2、Λ=M=I₃ではΔ=0・大域次元無限で、a₁=a₂=1ならc=196≠0である。この例により、平坦性・Hilbert級数・中心三次正則性だけで周囲のAS-regular性を結論しない。

rank-one slice Λ=λE₁₁、M=μE₁₁では、h=(1−τ₁³)(1−τ₂³)−τ₁²τ₂²λμ≠0が正確なAS-regular域である（`ifd:prop:ambient-locus`）。τ₁=τ₂=2、a₁=a₂=1、λ=μ=−6はh=−527、c=196で、この正則域の内部にある。しかし射影Azumaya chartの完備局所代数はMat₄(C[[t,u,v,r,s]]/(t³+uv+rs))となり、点対象の自己Extが非有界なので全coherent残余圏は非proper、残余線束圏は非smoothとなる（`ifd:thm:residual-a2`）。従ってD(Δc)全体を残余smooth域とみなすことはできない。これは主予想のsmooth仮定の外にある障害である。さらに軸上の中心normを二変数三次Pへ制限すると、判別式はα₁²α₂²(λμ−τ₁τ₂)²Qに因数分解する（`ifq:thm:axis-discriminant`）。Q=0かつλμ≠τ₁τ₂、h≠0は残余非smooth locusに含まれる。等τ・等重みではQは三尖点有理四次曲線で、一般のA₁点、3つのA₂ cusp、有理数係数のA₁例(τ=2,λ=15/2,μ=−6)を得た（`ifq:thm:tricuspidal`, `ifq:ex:rational-a1`）。Qは軸上判別の一因子である。さらに norm を二つの横Hesse三次組に分け、四つの二変数三次 F_{ε,δ}=P−εα₁²τ₁²k_x³+δα₂²τ₂²k_y³ の判別式の積が零であることと、射影中心 norm 超曲面が特異であることが同値である（`ifn:thm:four-discriminants`）。τ₁=τ₂=2、λ=0、μ³=−196、a_i=1ではh=49、c=196、前のQ≠0だが軸外のAzumaya通常二重点を持ち、残余非smoothとなる（`ifn:cor:off-axis-azumaya`）。 一方向Λ=sE₁₁、M=0では任意の許容τ₁,τ₂と固定非零重みについて、四つの明示的非零係数ρ_{εδ}の三乗根が中心normの全特異係数である（`ifod:thm:general-values`）。全sで周囲AS正則かつ中心三次正則、特異点は全てAzumayaで残余圏非smooth。τ₁³≠−2、τ₂³≠4なら全特異点は通常二重点で、通常のhypersurface判別多項式は単元倍を除き∏(s³−ρ_{εδ})^{3^{ε+δ}}、s次数48（`ifod:thm:generic-nodes`）。τ₁³=−2またはτ₂³=4では枝が合流してD₄型（Milnor数4）、両方では四変数Fermat三次のsuspension（Milnor数16）となる（`ifod:prop:collision-types`）。対称τ₁=τ₂=2、a_i=1の既存ρ=(54,56,−196,−5488/27)とノード数1/3/3/9を再現する（`ifn:thm:symmetric-probe`）。これは中心norm超曲面の判別であって、全残余smooth locusの逆判定や原点の固定Hesse切片の高次比較係数は未解決である。非Azumaya部分の圏模型と全smooth係数への核延長も残る。

十八変数の四・五次元型には、分離原点近傍の実相対smooth proper残余模型とétale局所perfect Ku核がある。四次元のKSは階数18、二つの混合Jacobian成分への同型で、形式像は余次元2である（`ifg:thm:smooth-neighborhood`, `ifg:cor:local-comparison`, `ifg:cor:rank-eighteen`）。さらにτ₁,τ₂を動かす二十変数族は、任意の許容分離点の完備化で幾何的変形空間と同型になり、局所分類写像は滑らかな三次四様体のモジュライスタックへétaleとなる（`ifv:thm:versal`）。実相対二捩れwindowとPicard比較から純因子の二方向を計算した結論である。係数空間の非空稠密開Uの有限étale全射V→U上に実相対perfect核が存在し、Vからモジュライスタックへのétale像も稠密開である。一般係数体の有限分離拡大上にも全coherent Ku比較を得る（`ifv:cor:generic-comparison`）。Uは選んだ分離点を含むとは限らない。一般の非標識圏変形は22次元のままであり、全三次四様体・全intrinsic対象・全smooth係数の被覆は結論しない。

Heisenberg同変核を選ぶと、残余一次式の写像はL(e_a)=ℓX_a、Q(y_b²)=q[Y_{b+1}Y_{b+2}]となる（`ife:thm:projective-coefficients`）。両Cliffordの標準方程式f_τ=τΣZ³−(2+τ³)Z₁Z₂Z₃と元の関係係数を固定し、d_i=τ_i³−1と置く。各因子ℓ_iq_i=2a_id_i/(3τ_i)、κ₁₂κ₂₁=4a₁a₂d₁d₂/(9τ₁τ₂)に加え、一般因子でκ₁₂³=8a₁³d₁²d₂/(27τ₂³)、κ₂₁³=8a₂³d₂²d₁/(27τ₁³)を得る（`ifm:thm:scale-cubes`）。θ=(a₂τ₂/a₁τ₁)(κ₁₂/κ₂₁)はθ³=d₁/d₂を満たし、動く因子係数上の非自明な有限étale μ₃-torsorを定める（`ifm:cor:kummer-scale`）。三枝は指定周期付きの実比較の選択で実現され、固定核には一つの枝が対応する。同一因子・同一重みの交換同変核では両κ=2a(τ³−1)/(3τ)である。この尺度torsorを全比較核のgerbeと同定したとはしない。

両Cliffordの標準Hesse方程式・原点核・周期と明示的なJacobian線型補空間を固定すると、形式可換方程式は一意に正規化される（`ifj:lem:linear-slice`）。一方向九変数に対するH₃×H₃の二次covariantと三次不変式は各五本で、実核を周期と両立する反転まで同変化すると各四本に減る。逆向き混合二次項の四係数と純二因子三次項の八係数、計十二係数は最小四つの一変数probeで決定できるが、その数値は未計算である（`ifj:thm:twelve-coefficients`）。この四probeに対する非可換側のcurved PBW積は二方向（単位行列と行和）で係数一次、二方向（列和と対角行列）で二次止まりであり、二次の積は順序付き8基底上の四つの構造定数−L₁L₃に限る。中心三次は全probeで一次である（`ifj:prop:pbw-jet-degree`）。この源乗法のHochschild整合を実際に計算し、`ifj:prop:pbw-curved-mc` で∂m₁=0、∂m₂=m₁∘m₁、m₁∘m₂+m₂∘m₁=m₂∘m₂=0および中心体積元の曲率整合式を証明した。m₁∘m₁(e₂,e₃,e₁₂)=L₁L₃は非線形二probeで非零なので、そのPBW規約ではm₂が必須であり、四係数が厳密な二次障害の原始となる。8基底の512 triple×5次数・曲率4次数を記号検算した（`verify_clifford_curved_pbw_mc.py`、10群PASS）。これは実比較核のHPL収縮・十二係数の計算ではない。s進bar模型の三次までの移送は `ifj:lem:pbw-hpl` によりd₁,d₂と原点収縮hの有限演算へ還元される。固定線型切片への射影ΠとJacobian座標補正𝒥は全56三次単項式について明示し、任意の三次式族から三次までの正規化係数を順次求める公式を得た（`ifj:prop:explicit-jacobian-projector`, `ifj:prop:explicit-third-normalization`）。一次が既に切片にあっても、二次のJacobian補正は三次の純因子項を変えうる（`ifj:ex:third-coordinate-artifact`）。これらは一般Hesseパラメータの有限恒等式であり、比較核・周期に沿った原点収縮と高次移送の出力G₁,G₂,G₃は未構成。さらに一次を固定した四probeでは、二次G₂の必要な14単項式係数と三次G₃の32単項式係数、合計46枠から12係数を再構成できる（`ifj:prop:direct-probe-readout`）。純X三次係数に二次座標補正は作用せず、純Y三次係数にはκ/(3a₁τ₁)とG₂の平方混合係数の対合補正が残る。移送微分そのものを12係数と同一視しない。自由な標的形式座標による高次graphの消去は、固定した多項式切片でこれらの値を求めることとは異なる（`ifj:prop:formal-straightening`）。

中心体積元の平方に由来する Clifford norm の行列式 N(s)=det q_x(s) は、一般九変数のs次数3まで完全に展開した（`ifj:prop:central-norm-jets`）。固定Hesse射影ではその二次同変係数が一つの三次不変式𝒮(U,τ₁)のU-gradient、三次純Y係数が(∂𝒮/∂τ₁)/4となり、二方向C′₀,I₃だけに非零の三次normを持つ（`ifj:cor:central-norm-probes`）。ただし中心平方を可換座標と文字通り同一視すると一次像はC₂₁、実Ku比較の一次像はC₁₂で一致しない。この中心normの高次係数を未計算の12個のKu比較係数に流用しない。中心normの分離時Hesse cubicが滑らかである条件τ₁³≠1,−8も厳密に確認した。これは新しいKu核や全smoothness判定ではない。

点曲線E_τ=V(f_τ)と分離Clifford中心の判別曲線C_τ=V(D_τ)について、D_τ=(τ³/8)f_{−2/τ}という厳密なHesse係数変換を得た。標準原点o=(1:−1:0)・非零二捩れp=(1:1:τ)の下で、E_τ→E_{−2/τ}は核{ o,p }の次数2のisogenyとなり、標準三捩れ基底にはdiag(1,−1)で作用し、往復合成は[−2]になる（`ifj:thm:discriminant-two-isogeny`）。対応する偏極の引戻しはφ*O_{E_{−2/τ}}(1)≃O_{E_τ}(2)⊗M_τ、M_τ=O_{E_τ}(p−o)非自明二捩れであり、元の射影座標の普通の斉次二次式3本ではこの写像を表せない（`ifj:cor:isogeny-picard-line`）。M_τは既存の分離Picard–rotation比較の線束と同じ。二重isogeny・Cayleyanの一般理論は先行研究を引用し、今回のClifford規約での係数・標識・引戻しの具体化と分ける。これは実Ku比較核の構成、46枠の高次係数の取得、未計算の12係数の数値決定ではない。

二重isogenyのtheta群では三捩れ上の交換子がe_A=e_L²=e_L⁻¹となる（`ifj:prop:two-isogeny-theta-characters`）。引戻し偏極A=L²⊗Mに対してH⁰(E,A)はdeck対合pの±固有空間各3次元の直和で、それぞれ元の三捩れHeisenbergの双対中心文字を持つ。通常の斉次二次式も中心文字は同じ逆文字なので、中心文字だけでは二次式を排除できない。正確な障害はHom_E(L²,A)=H⁰(E,M)=0であり、二捩れPicard線束Mを落とした座標転送を阻止する。特別なτ²=−2ではτ^∨=τ、自己isogenyの平方[−2]・j=8000・CM整数環Z[√−2]となるが、M非自明のため障害は消えない（`ifj:cor:two-isogeny-cm-specialization`）。これは高次Ku比較係数12個の計算ではなく、有限比較模型で保持すべきtheta文字と線束の指定を与える。次は実相対perfect核の有限モデルにdeck対合を入れ、±の三次元固有空間・逆Heisenberg文字・相対rotationと三乗周期を同時に追跡し、46原式係数を得る。

二重isogenyの引戻し偏極を、元のHesse平面上の三次式からなる六次元の完全線型系で明示した（`ifj:prop:two-isogeny-cubic-sextet`）。接線一次式Wと二つの一次式T,Sにより、元の点曲線は厳密にWS²=T³+aWT²+bW²Tとなる。共通基点因子D=2o+pを持つ六三次式W²T,W²S,WT²,WTS,T³,T²Sの制限が、Dを除いてφ*O(1)=O(2)⊗Mの全切断を生成する。deck対合の作用はU=T/W,V=S/Wを用いてD(g)=U⁴g(b/U,−bV/U²)/b²という6×6行列で明示でき、±各3次元の固有基底を具体化した。二重被覆の負固有線束は標的側M_{τ∨}=O(p∨−o∨)と同定した。正固有三次式G0=WT²,G1=T³+aWT²+bW²T,G2=S(T²−bW²)は標的Weierstrass曲線を与え、元の曲線三次×明示六次式に分解する次数9の恒等式を持つ。逆線型変換で標的Hesse座標にも戻せ、反転と両立する。一般のCayleyan/isogeny理論は既知で、本Clifford座標における有限模型とPicard補正の具体化である。これでも実Ku核・rotationと三乗周期の高次移送は未構成であり、46原式係数・12 scalarは未計算。

相対二重被覆の符号固有加群を有限代数として明示した（`ifj:prop:double-cover-algebra`）。許容τの係数環K上でa=Aτ、b=Bτ、δ=a²−4b=(τ³+8)³/(81τ)、g(X)=X²−2aX+δとすると、標的R=K[X,Y]/(Y²−Xg(X))、源被覆B=K[ξ,η]/(η²−g(ξ²))（X=ξ²、Y=ξη、deckは同時符号反転）である。B=R⊕I、I=(X,Y)、I²=(X)、符号成分積ij/Xが成り立ち、任意の許容底変更と両立する。単純な√Xの追加には二捩れ点上に偽の通常二重点があり、η=Y/ξを加えた整閉包が必要。源Mτと標的Mτ∨の両方のPicard線束を斉次2×2行列分解で有限表示した（`ifj:prop:two-torsion-matrix-factorization`）。その余核はO(−p)なのでM=O(p−o)には一点捩れO(o)が必要であり、通常の次数shiftは代用にならない。標的符号線束は被覆へ引き戻すと自明だがdeck符号が残る（`ifj:cor:double-cover-sign-descent`）。11群の厳密計算で多項式恒等式を確認した。これでPicard線束の相対MF入力は得たが、非可換曲率・rotationと三乗周期を保つ実比較核、46原式係数、12数値はまだ未完成。

二重被覆のtrace/Casimirと有限射影冪等元まで明示した（`ifj:prop:cover-trace-casimir`）。R=K[X,Y]/(Y²−Xg)、I=(X,Y)、δ=a²−4b、g=X(X−2a)+δに対し、P_I=δ⁻¹[[-X(X−2a),−Y(X−2a)],[Y,g]]はP_I²=P_IでI≃Im P_I、B≃Im diag(1,P_I)⊂R³となる。さらに被覆のΘ=(η⊗η−(X−2a)ξ⊗ξ)/δはΘ²=1、e±=(1±Θ)/2がB⊗_R B≃B×Bの対角・反対角を分離する。e+はtrace pairingの双対Casimirであり、有限被覆の乗法に双加群sectionを与える。そこから相対Hochschild cochainの明示収縮を得て、任意のB-双加群MについてHH_R^n(B,M)=0 (n>0)を証明した（`ifj:cor:cover-hochschild-contraction`）。非可換Ku比較核全体の収縮ではない。a(s),b(s)を動かしてもδ(s)⁻¹の明示的三次展開によりP_s、e_sの3-jetが未定定数なしで得られ、各Artin切断の有限étale被覆は指定した原点被覆から一意に持ち上がる（Stacks Tag 0BQB）。この有限étale部分には独立の高次障害がないが、Picard一点捩れ・非可換曲率・rotation・三乗周期・Ku kernelの比較cochainを与えておらず、46原式係数・12比較係数は未計算。

二捩れPicard線束M=O(p−o)を直接余核として与える、対称3×3線形行列分解を構成した（`ifj:prop:picard-symmetric-linear-mf`）。Weierstrass三次F=Y²Z−X(X²+aXZ+bZ²)に対しL=[[X,Y,0],[Y,aX+bZ,X],[0,X,−Z]]、det L=F、L adjL=F I3、coker(O(-2)^3→O(-1)^3)=i_*M。以前の2×2 MF余核O(−p)に必要だった一点捩れO(o)を、この3×3模型では別操作なしに線束として内蔵する。M(1)=O(p+2o)の基底s=(−Y/X,1,X/Z)でM²≅Oの乗法をu=X/Zで規格化すると、積の対称行列は正確に−adjLであり、D=diag(−1,1,1)がY反転を二つのMF微分と二乗評価に厳密に持ち上げる。一般の対称線形表示はBeauville (2000) Propositions3.1,4.2とBuchweitz–Pavlov (2024) Theorem Aの既知機構で、本研究の有効な入力はCliffordの固定係数・二捩れ点・二乗scalar・反転の明示式。元のHesse一次式W,T,Sを代入するとdetLτ=4cτ² fτで、(4cτ²)⁻¹ adjLτを第二微分にすれば余分な三乗根なしで指定fτのMFとなる（`ifj:cor:picard-symmetric-hesse-family`）。動くa(s),b(s)の三次jetも行列の代入・微分で処理できる。一方、最小四混合probeはτ_i固定だから、このPicard行列はs-定数であり、それだけから未計算β,γの値は出ない。有限被覆・Picardの単独精密化をこれ以上P0の代わりにせず、混合PBW曲率・原点Koszul–Shamash比較核・unit/counit・指定rotation/periodの本体へ進む。

対称三階Picard行列分解のアフィン縮約を明示した（`ifj:prop:picard-affine-bridge`）。Weierstrass三次のZ=1で可逆な三角行列Tを取り、TLTᵗ=S⊕(−1)、対応する随伴を(−adj S)⊕(−f)に分割する。coker SはI=(x,y)、βが単元ならI²=xAで、M²のx規格化はI⊗I→A、r⊗s↦rs/xと符号まで一致する。これは有限二重被覆B=R⊕Iの符号成分の積そのものであり、xを逆にする必要はない。可縮一階因子の除去はZ≠0に限るため、斉次線束の一点捩れ・rotation/三乗周期・非可換Koszul--Shamash核を得たとはしない。有限恒等式は`verify_clifford_picard_affine_bridge.py`の8群で厳密検算した。四probeの46原式・12高次係数は依然として未計算。

同一S(1,−1,−1)の既存結果では、指定規約でκ_k²=27/28、κ_k=3√21/14を保持する（`mcs:cor:universal-scale`）。Heisenberg同変な一次像は純ブロックJac₂の直和で、比較の七定数形のうち六定数χ_k,A_k,…,E_kは未数値化（`lec:thm:seven-scalar-form`）。一般の異なる因子へこの数値κを流用しない。指定二ブロックのP64・norm全64根・有限中心と局所型も保持する。残る核心は、全intrinsic対象の認識と表示被覆、最高次の二次境界を変える混合族の比較の具体化・全smooth係数への延長、偏極標的への実比較核、因子moduli上の核選択・降下である。一般の比較係数、一般PBW族のPI性・有限中心性、選択済みh一般点核のdefect零特殊化も未解決。

**「任意」をgenericへ置き換えない。** 全対象の内在的な定義・認識、全O-marked moduliの代数性と表示による被覆は未完成である。少なくとも既存のAS正則周囲代数Bの中心三次商A=B/(w)は、良い開の外も研究対象とする。既知の一ブロック局所型stackの対象を全nc cubicと定義し直して主予想を解いたとはしない。point functorの表現可能性・表示独立性も必要な範囲で解く。主予想の定式化の正本は主原稿の `conj:nc-main` である。

## 研究の進め方と達成基準

主予想の解決に向けて、実際のKu比較を構成できる対象範囲を広げる。O-markedモジュライ、点対応からの復元、残余Poisson射、全O同値・中心作用の認識は、そのための手段として位置付ける。比較次数・位相・全自己同値の精密化は、可換実現の存在と対象範囲に関わる障害を解消するときに優先する。point/Poisson一致への素朴な期待が失敗する例は、主予想の意味を明確にする補助的な内容として本文に置き、Introductionから参照する。

主予想の肯定結果の達成基準は、対象範囲と仮定を明記し、実際のKu同値を構成することである。point/Poisson一致を併せて述べる場合は、同じXについてpoint schemeと零スキームの同型まで証明する。不一致の例では全候補を排除できる範囲とその入力を明記し、可換Ku比較を必要とする三様体の論法と、全可換五様体を一括排除する論法を区別する。楕円成分のjの一致、点集合の一致、有限jet、幾何学的一般点だけの同値を全主予想の解決と扱わない。一般体上の核降下や全族の大域核sectionは、C上の存在とは別の強化として扱う。

一般点可換復元・一ブロックモジュライ・満支持型比較は有効な部分結果として保持する。一つの中心変数を共有する任意の固定楕円因子の全許容PBW表示では全係数核を得ており、多中心ではsmoothness判定と一般中央flagから全smooth因子別対象を比較できる。固定tensor境界のPBW分解に続き、二次境界を動かす両Cliffordの十八変数族にも局所比較を得た。二十変数族の幾何的形式完全性、モジュライの稠密開と一般係数の有限étale比較、一般混合尺度の三乗を既知の入力として使う。次は固定切片の十二係数の最初の非零値を実計算し、比較核のKummer三枝の選択・降下と残余smooth locusの境界を調べる。全smooth係数への核延長、全比較核のgerbe、未被覆の内在的対象は残る。元の全intrinsic対象という目標は変えず、全中心作用を保つ比較と因子moduli上の降下も継続する。

[中心持上げ条件](papers/sections/mixed/elliptic_center_obstruction.tex)と[一般因子の全係数比較](papers/sections/mixed/elliptic_mixed_comparison.tex)を一体として使う。二捩れでは残余線形PBW補正に障害がある一方、中心平方の三方向が残るため、関係式だけで一次変形を数えない。全許容表示をこの二種類の一次係数で尽くすことを確認してから、境界核・Bockstein・実comonadを比較した。主予想の全対象という目標は変更していない。

## 補助的な例：point/Poisson一致への素朴な期待の限界

同じ可換Ku標的X上でPoisson構造πを選べばPt(𝒳)≃Z_X(π)も実現できる、という素朴な期待は一般には成り立たない。これを独立した予想として掲げず、本文の注意 `ppz:rem:naive-expectation` と以下の例で扱う。Z_X(π)は切断としての零スキームであり非被約構造も含め、point shiftの固定点とは区別する。可換対象ではπ=0を許す。

**被約化しても一致しない五様体の例。** `ppz:thm:isolated-zero-dimension` は、滑らかな可換三次 n-fold のPoisson零集合に孤立点があれば n=3k、一般階数2kであり、その局所零スキームが零次元完全交叉であることを示す。入力は `poisson-cubic` の固定版の全次元正規形であり、pure blockの楕円性を仮定しない。特に全ての滑らかな可換三次五様体の全Poisson零集合には孤立点がない。一方、指定混合族の定常normの全64根ではsourceとその全coherent Kuはsmooth properで、Pt(A_c)=E₁⊔E₂⊔{p_c}は被約である。`ppz:cor:reduced-point-poisson-counterexample` はこれにより全可換五様体・全Poisson構造を排除する。c=−44828に有理係数の一例を固定できる。不一致の証明自体は可換Ku標的の存在を必要としないが、`cmo:cor:norm-commutative-kernel` が全64根に実Ku標的X_cを与える。従ってこれらは主予想の存在結論を満たしながら、被約point/Poisson一致への期待が失敗する例である。

**実Ku比較を伴う三様体の全スキーム不一致の例。** `ppz:cor:complex-counterexample` は、関係式と中心元を有理数係数で明示したC上の良い一ブロック三次三様体 A★ を与える。h=1、可換標的のHesse係数は17/9に固定できる。実Sklyanin因子を `esi:prop:factor` で確認し、楕円因子と二つのA₂因子から `csc:cor:fermat` でKu比較を直接構成する。反例の証明に一般点の形式復元・C閉点へのspreadは不要である。A★は主予想を満たすが、同じKuを持つどの滑らかな可換三次とどのPoisson構造を選んでも全point schemeは零スキームと同型でない。非被約な三つの定常点の長さ八局所環を使う反例であり、自然な残余pairでは被約部分は一致する。二つの反例の機構と入力を区別し、成立範囲を検証せず修正版を新予想として採用しない。Ku比較はC上の存在であり、有理係数の表示からQ上の比較核の存在を結論しない。

この具体例の「良い」は点スキームの条件を指す。全O表示stackの全相対入力に属することをh=1で独立に確認したという意味ではなく、それらを反例の証明に用いない。

異なる射影表示を持つ対象間の「一致」はスキーム同型として定式化し、射影埋込みを保つ同型、点対応も保つ同型、族での自然な降下は強化問題として区別する。埋込み版には一ブロックの障害があるため、抽象スキーム版の証明で埋込み保存を無断に仮定しない。どの意味が成立・不成立かを明示して検証する。

## 現在の到達点と適用範囲

| 対象・結果 | 主予想への到達点 | 関連する幾何と比較の限界 | 正本 |
| --- | --- | --- | --- |
| 任意固定楕円因子の全許容PBW・中心三次 | 全係数の残余線束Morita比較、可換smooth開の相対perfect核・全coherent Ku。二捩れβも含む | 固定因子のC上の存在。因子moduli上の核選択・全intrinsic被覆は残る | `emc:prop:coverage`, `ebk:lem:boundary`, `ebc:prop:constant-iso`, `ebc:thm:first-injection`, `euk:thm:universal-kernel` |
| 固定tensor境界の全二次PBW表示 | 任意可換係数環上で元の生成元のまま厳密な因子別分解。中心三次があれば従来の全許容正規形へ入る | 厳密な中心変数と固定した最高次境界を仮定。全intrinsic被覆は含まない | `ifp:thm:factorization`, `ifp:cor:central-comparison` |
| 多中心の全許容正規形 | 非被約係数環でも一次・二次・三次の中心形式で全表示を分類。係数数3km+3k binom(m+1,2)+binom(m+2,3)、二中心15k+4。中心列は任意順序で正則 | 最高次の二次境界を動かす変形は別問題 | `mcp:thm:normal-form`, `mcp:prop:free-quotient` |
| 全smooth固定tensor境界対象 | K_A smooth ⇔ X_pol smooth。一般中央flagの各商もsmoothであり、任意mで次元3k+m−2の滑らかな可換三次への全coherent Ku比較 | X_itへの実核を構成。X_polへの核、全中心作用の同時保存は未証明 | `ifp:cor:central-comparison`, `mcb:thm:smooth-locus`, `mcb:thm:central-flags` |
| 二次境界の混合変形と指定中心 | Euler混合類の障害は単射、Clifford混合核の次元は9·#I₂·(k−1)。一ordered pairの九変数と、両Cliffordの双方向十八変数を実積分 | 一方向は全係数の自由商、双方向は明示的D(c)上の平坦商。一般の複数ordered pairの全核積分と全intrinsic被覆は未解決 | `ifh:prop:central-mixed-obstruction`, `ifc:thm:family`, `ifb:prop:family` |
| Clifford九変数族の周囲代数 | 全Λ・任意可換C-係数環で相対Koszul、有限自由双加群解消、untwisted相対6-CY。複素fiberはAS-regular dimension/index6 | 相対smoothnessと基礎環上の絶対smoothnessを区別。中心商の滑らかさは別証明 | `ifr:thm:ambient-regularity`, `ifr:cor:central-extension` |
| Clifford族の四・五次元型 | 九・十八変数の分離原点を含む実smooth proper開、複素fiberのcoherent飽和、étale局所の可換三次族とperfect Ku核 | 残余smooth locusの補集合、高次方程式、全smooth係数への比較は未確定 | `iff:thm:smooth-neighborhood`, `ifk:cor:clifford-fourfold-neighborhood`, `ifg:thm:smooth-neighborhood`, `ifg:cor:local-comparison` |
| Clifford四次元族の残余接写像 | 九方向はJac(f₁)₁⊗Jac(f₂)₂、双方向十八は二つの混合成分の直和。形式像はそれぞれ余次元11、2の正則閉埋込み | 同変比較でL(e_a)=ℓX_a、Q(y_b²)=q[Y_{b+1}Y_{b+2}]。非可換中心平方を同名の可換平方へ写さない | `ift:thm:rank-nine`, `ifg:cor:rank-eighteen`, `ife:thm:projective-coefficients` |
| 双方向十八変数の周囲代数 | 二次双対の可換六二次resultant Δ≠0が正確な有限大域次元・AS-regular領域。相対Koszul・untwisted6-CY、有限射影双加群解消、任意底変更互換 | Δ=0ではaugmentationの射影次元が無限。τ₁=τ₂=2、Λ=M=I₃が具体例 | `ifb:thm:regularity`, `ifb:cor:exact-regular-locus`, `ifb:ex:nonregular` |
| 二つの因子係数を含む二十変数族 | 任意の許容分離点でKSは幾何的20次元への同型、標識付き形式変形空間も同型。係数稠密開の有限étale被覆上に実perfect核があり、分類写像のétale像は三次四様体モジュライの稠密開 | 一般係数体の有限分離拡大上にも全coherent Ku比較。粗モジュライへのétale性、全22次元圏変形、全smooth係数・全intrinsic被覆は含まない | `ifv:thm:versal`, `ifv:cor:generic-comparison`, `ifv:rem:generic-scope` |
| Clifford混合一次尺度と枝 | κ₁₂³=8a₁³d₁²d₂/(27τ₂³)、κ₂₁³=8a₂³d₂²d₁/(27τ₁³)、d_i=τ_i³−1。尺度比はθ³=d₁/d₂の非自明なμ₃-torsor。同一τ・同一aの交換同変核では両κ=2ad/(3τ) | 標準方程式・元の関係係数・指定周期に対する値。固定核の枝は一つに定まり、全比較核のgerbeを分類するものではない | `ifv:prop:scale-calibration`, `ifm:thm:scale-cubes`, `ifm:cor:kummer-scale` |
| 固定Hesse切片の高次jet | 一方向九変数の形式可換方程式は固定核の下で一意。H₃×H₃の五covariants・五invariantsは反転同変実核で各四本となり、二次四係数と純三次八係数へ帰着 | 十二係数の数値は未計算。四probeが必要十分で、二つの二次PBW方向も最小。全56単項式に対するJacobian射影・三次正規化と、四方向合計46個の単項式係数を読む直接公式を明示済み。原点実核からその入力となるG₂,G₃の必要係数を得ることは未完成。自由な標的形式座標での直線化とは区別する | `ifj:lem:linear-slice`, `ifj:lem:reflection-kernel`, `ifj:thm:twelve-coefficients`, `ifj:prop:pbw-curved-mc` |
| Clifford中心normの全九変数jet | `ifj:prop:central-norm-jets` で N(s)=det q_x(s) の三次までの厳密係数・Hesse射影・三次不変式𝒮のgradientを計算。二つの非線形PBW probeのみに三次normが現れる | 文字通りの平方中心座標では一次像C₂₁≠実KuのC₁₂。これは比較標的の計算ではなく、12係数の数値も未計算 | `ifj:prop:central-norm-jets`, `ifj:cor:central-norm-probes`, `verify_clifford_central_norm_jets.py` |
| 点楕円とClifford中心判別の二重isogeny | D_τ=(τ³/8)f_{−2/τ}。核{ o,p }の次数2 isogeny E_τ→E_{−2/τ}、往復[−2]、三捩れの反対称作用、偏極の引戻しO(2)⊗M_τ | 二重isogenyの一般理論は既知。M_τは分離比較のPicard線束と同じだが、それだけから実Ku核の高次比較や12係数は導けない | `ifj:thm:discriminant-two-isogeny`, `ifj:cor:isogeny-picard-line`, `verify_clifford_hesse_two_isogeny.py` |
| isogenyのtheta文字とPicard障害 | 引戻し線束A=L²⊗MのE[3]交換子はe_L²=e_L⁻¹。H⁰(E,A)はdeck±固有空間の3+3。τ²=−2はCM・j=8000で自己isogeny | 普通の二次式も逆中心文字を持つがHom(L²,A)=0。高次Ku核や12係数は未計算 | `ifj:prop:two-isogeny-theta-characters`, `ifj:cor:two-isogeny-cm-specialization`, `verify_clifford_hesse_theta.py` |
| 基点付き三次式によるisogenyの有限座標模型 | 6次元のW²T,W²S,WT²,WTS,T³,T²Sを基底とし、基点因子2o+pを除いてφ*O(1)を得る。deck±3次元の明示行列、標的Hesse三次式、全次数9因数分解と反転を与える | Picard線束を保持した楕円線型系であり、実Koszul–Shamash核・rotation・46比較係数は未算出 | `ifj:prop:two-isogeny-cubic-sextet`, `ifj:eq:cubic-sextet-nine-identity`, `verify_clifford_isogeny_cubics.py` |
| 相対二重被覆・Picardの2×2MF | B=R⊕I、I²=(X)、deck符号、有限étale・整閉包、源と標的の2×2斉次MFを明示 | 余核O(−p)には一点捩れO(o)が必要。Ku実比較核・46原式係数は未構成 | `ifj:prop:double-cover-algebra`, `ifj:prop:two-torsion-matrix-factorization`, `ifj:cor:double-cover-sign-descent` |
| 二重被覆のtrace/Casimirと相対HH収縮 | IをR²の明示射影P_Iとして実現、B=im diag(1,P_I)。Θの平方1と対角分離冪等元e±、trace双対枠、HH_R^{>0}(B,M)=0。a(s),b(s)の三次変形に同じ公式が適用可能 | 収縮は有限étale被覆側の相対HHであり、curved Koszul–Shamash比較のspecial retractではない。Ku 12係数は未取得 | `ifj:prop:cover-trace-casimir`, `ifj:cor:cover-hochschild-contraction`, `verify_clifford_cover_trace_casimir.py` |
| Picard二捩れの対称3×3線形MF | L=[[X,Y,0],[Y,aX+bZ,X],[0,X,−Z]]、detL=F、cokerL=M=O(p−o)を直接実現。−adjLはu=X/Zで規格化したM²の積行列、反転D=diag(−1,1,1)と両立。Hesse fτへ単元4cτ²のみで移送 | Beauville/Buchweitz–Pavlovの一般原理は既知。四混合probeではPicard MFはs-定数、実nc比較核・46原式係数・βγ12値は未計算 | `ifj:prop:picard-symmetric-linear-mf`, `ifj:cor:picard-symmetric-hesse-family`, `verify_clifford_picard_linear_mf.py` |
| 対称Picard MFと二重被覆の符号積のアフィン接続 | Z=1で三角congruenceにより3×3 MFが2×2理想I=(x,y)のMFと可縮一階因子へ分解。規格化M²積=rs/xがB=R⊕Iの符号積に一致 | β単元。大域斉次MFの同一視、nc Ku核の移送、12高次係数は未完成 | `ifj:prop:picard-affine-bridge`, `verify_clifford_picard_affine_bridge.py` |
| 周囲AS-regular域内部の残余特異点 | rank-one sliceの正則域はh≠0。τ₁=τ₂=2、λ=μ=−6、a₁=a₂=1ではh=−527、c=196だが射影Azumaya局所型はA₂で残余非smooth | D(Δc)と残余smooth域は一致しない。全境界の分類ではなく、主予想のsmooth仮定を満たす反例でもない | `ifd:prop:ambient-locus`, `ifd:thm:residual-a2` |
| 三次四様体のrotationを持ち上げる変形 | HH²固定部分20次元＝幾何的接空間。C3固定形式空間を使い通常Artin全次数で幾何的変形と認識、標識付き原点からétale局所核へ | 持上げ自体や周期coherenceを追加標識する高次群oid、一般の22次元変形全部の幾何化ではない | 主稿 `ifk:prop:geometric-fixed-part`, `ifk:thm:rotation-formal`, `ifk:thm:rotation-neighborhood` |
| 固定smooth境界の全横断係数 | Bは同型、二次・三次係数は三角多項式同型。各固定一次係数の一般二次係数で2^(3k+m−1)個の単純悪値と各唯一ODP。判別は既約被約、affine正規化 | 特殊二次係数の多重根を許す。可換標的の局所型から非可換中心の局所型は結論しない | `mtb:prop:transverse-iso`, `mtb:cor:many-centers`, `mtd:thm:normalization`, `mtd:cor:many-centers` |
| 中央pencilと二重制限 | Δは次数3·8^k、一般α(U),c(U)で単純な一節点切断。実BCとjoint comonadを構成 | このLefschetz幾何は偏極した可換候補のもの。同一軸でも全体のsmoothnessが異なるため全分配データが必要 | `mcpn:thm:lefschetz-pencil`, `tcr:prop:beck-chevalley`, `tcr:ex:same-axes` |
| 一般中心三次変形 | 明記した平坦・可換特殊化・滑らかさの仮定の下で、一般係数体の有限拡大上に全coherent Ku比較。C上の全固定点や全内在的対象の表示を与える定理ではない | point scheme全体の零点比較は含まない | `generic_recovery/` の `cft:thm:complete`, `gdr:thm:generic`、[基礎ノート](notes/recovery_foundations.md) |
| 良い一ブロックの共通稠密開 | 同じX_resへの有限被覆上のKu比較、全O降下する残余Poisson射。形式MF・window・飽和の明記した入力を使う | Pt(A)=E⊔D、Dは型(2,2,2,3)。Eと残余active曲線の比較はあるが、全Dの一致は別問題。trace–Hessian対象と残余対象も区別する | `relative_points.tex`, `poisson_morphism.tex`, `residual_algebraic.tex`, `residual_point_scale.tex` |
| 満支持k≥2,m=0の楕円tensor型 | 実際の因子積・rotation比較から可換分離和へのKu同値。明記した実因子仮定の下で同じj・特殊j・非零二捩れも許す | 同じ標的上のπについてPt(A)=Z_X(π)=⊔E_iをスキームとして証明。純成分の近傍で他block座標を単元消去するため非被約試験底にも成立 | `two_block_points.tex`, `multiblock_noncommutative_product.tex`, `multiblock_rotation_comparison.tex`, `point_poisson_split.tex` |
| 中心変数m≥1を持つ分離型、N=3k+m≥5 | 実楕円因子・全a_i≠0・中心三次gのJacobian環有限次元の下で、任意の点曲線方程式f_iに対しX=V(Σf_i+g)への実Ku同値をC上で直接構成 | m=1,g=cu³,c≠0では同じX上でPt=Z=⊔E_i。m≥2では定常完備局所環J[[t_1,…,t_{m−2}]]、length J=8^k。自然な零スキーム側のJ_clと比較 | `central_split_comparison.tex`, `central_split_points.tex` |
| 固定有理係数の一ブロック三様体 A★ | h=1,λ=17/9。指定Ω・THCR商を直接確認し、楕円因子＋二つのA₂因子で全coherent Ku比較 | 局所環J_1とJ_17/9の厳密j不一致、任意supportの局所補題、12点のHessian分類により全πを排除。BMMSで全Ku標的も排除 | `explicit_sklyanin_input.tex`, `point_poisson_obstruction.tex` の `ppz:cor:complex-counterexample`。Mayanskiy・BMMS等の既知入力を明記 |
| S(1,−1,−1)の定数型混合kブロック、k≥2 | 固定非零重み・任意α,cの残余線束圏をG−u²L+κcu³と普遍Morita比較。可換smooth開では相対perfect核と全coherent Ku同値。rank8^k判別行列 | 全kでκ²=27/28をAzumaya Morse点と二次momentから証明。因子追加に対する核の標識の互換性は別問題。指定二因子の14節点・全simple・P64・norm全64根を保持 | `mixed/multiblock_central_kernel.tex` の `cmm:thm:universal-kernel` と `mixed/multiblock_scale.tex` の `mcs:cor:universal-scale` |
| S(1,−1,−1)の全線形PBW族の残余Bocksteinと可換比較 | M対称・対角零正規形・普遍中心、3k方向の残余Bockstein単射性、普遍線束Morita比較と可換smooth開の全coherent Ku同値。一次像は純ブロック直和、全比較係数は七定数表示 | 既知κと残る六定数χ_k,A_k,…,E_k。任意固定pの一般αで8^k個の単純な悪いc。全係数・各固定pの判別超曲面は既約被約でaffine正規化。一般PI・有限中心性は未解決 | `mixed/linear_bockstein.tex`, `mixed/linear_comonad_comparison.tex`, `mixed/linear_equivariant_coefficients.tex`, `mixed/linear_discriminant_geometry.tex` |
| 他の滑らかなSklyanin因子の指定中心三次 | 非二捩れでは全PBW係数に普遍多項式lift。二捩れS(1,1,τ)では正規化p=0が必要十分で、許容線形項は平行移動方向に一致 | PBW・CYだけでは指定三次は持ち上がらない。τ=2,p=(1,0,0)は有理反例で、非スカラー二次中心7x²+4xは残る。これ自体はKu主予想への反例ではない。許容部分の実比較は上段euk定理で構成済みで、二捩れの中心β三方向も含む | `mixed/elliptic_center_obstruction.tex` の `eco:thm:clifford-obstruction`, `eco:prop:universal-lift`, `eco:cor:non-clifford-lift` |
| 全Poisson構造の孤立零点制約と混合五様体 | 不一致の証明はKu比較を入力としない。norm全64根には現在実Ku標的X_cもある | 孤立零点にはn=3k・一般階数2kが必要で、局所零環は0次元CI。norm全64根では被約point/Poisson一致への期待が成立しない。c=−44828を明示 | `mixed/poisson_limits.tex`, `cmo:cor:norm-commutative-kernel`。固定版の全次元正規形を入力 |
| 元の中心係数c族の実比較と任意αへの普遍化 | 全cの残余線束圏のMorita同値族、U上の相対perfect核・全coherent Ku比較を構成。任意αでも可換側smooth開に実比較 | 三項までの全comonad比較で核を先に作り、P64の二次momentでλ²=28/27を決定。Q降下・全rotation/周期標識の保存は別問題 | `cmo:thm:all-central-commutative-kernel`, `cmo:cor:all-alpha-central-kernel`。証明は `mixed/central_spherical_reconstruction.tex`, `mixed/central_formal_comparison.tex`, `mixed/central_kernel.tex` |
| 指定族の全smooth領域の不変量 | U=A¹∖V(P64)上の実相対smooth proper模型を構成。全cでHH₀の次元2、HH±₁は各21。有理数値Euler形式も可換候補と一致 | c=0の対合のHH±₁固有次元は無条件に(+5,−16)。不変量の一致自体は核の証明ではない。実核が誘導する積分数値同型の基底表示と二対象の積分基底性は未計算 | `cmo:prop:full-relative-hh`, `cmo:cor:rational-euler-comparison`, `mix:thm:h-semilocal-smooth` |
| c=0の実二成分分解と球面接着 | Ku(A₀)^μ₂=⟨ΦKu(Z),ΨK_R⟩ を全coherent圏上の実perfect核で構成。球面comonadの比較からK_R≃Ku(Y)と制限intertwinerも構成し、通常Kuへ接着 | Serre数値やHHからの認識・相殺ではない。通常のL二側商は有限次元で使えず、実比較は境界類とcoKleisli復元による | `cmo:thm:root-order-residual`, `cmo:prop:invariant-restriction-spherical`, `cmo:thm:fixed-zero-commutative-kernel` |
| 交換子h族の指定候補への実核 | h⁶+27≠0上の全次数平坦性、指定W_h^candへの全次数形式MF同値、C(h)の有限拡大上のperfectKu核。0,1を含む相対perfect対角とh=1でのperfect整核も構成 | 選択済み一般点核をdefect零で延長し固定点の核へ接続する問題は未解決。全行列・拡大次数・Q降下を算出したわけではない。構成済みの元c族の同値族と、この選択済みh核の互換性は別 | `mix:thm:h-exact-candidate`, `mix:thm:h-semilocal-smooth`, `mix:thm:h-integral-kernel` |
| 固定曲率の非次数付きaffine MF | 一因子の全sと混合族の全cで、冪等完備後の実dg Morita比較。悪い値はCl₃・Cl₆、良い値は双方零 | 全smooth cで射影Kuは非零なので、このaffine圏を介する同値は不可能。内部次数・錐の原点・周期を保持する比較が必要 | `cmo:lem:isolated-azumaya-mf-completion`, `cmo:prop:pointwise-affine-mf-comparison` |
| n≠4の通常Artin変形・開性とtrait核判定 | 実smooth proper dg族で可換Ku実現locusがZariski開。generic同値を与える実perfect核の特殊化は二つのunit/counit coneの長さd_R=0と同値 | 開性・連結性や両側のsmooth proper性から閉性は従わない。核の存在自体とπ・point functorの延長は別問題 | `residual_categories.tex` の `thm:nf-residual-formal`、`geometric_realization_locus.tex` の `grl:thm:open-locus`, `grl:prop:trait-kernel-test` |

全原稿の証明を今回独立に再検証したという表ではない。今回の追加結果・読解点検・計算・組版・表示・保存の状態は [notes/validation.md](notes/validation.md) に記す。新規性の網羅的確認と外部査読・形式証明は未完了。

## 優先する次の課題と具体的な着手

**再開の中心となる実核。** `mixed/central_spherical_reconstruction.tex` は全係数でproperな残余線束圏から境界Sへの球面制限を作り、周期によって右随伴像が生成することを示す。underlying comonadはId⊕ρ_S²[−1]である。正規化した余乗法の選択は二項Jac(G)₁=C⁶と三項Jac(G)₀=Cに限られ、四項以降の非空fiberは可縮になる。`mixed/central_formal_comparison.tex` は普遍係数環上の正則性・重み(2,3)・法線符号対合・一変数MFから、これらをαと非零scalar·cへ対応させる。`mixed/central_kernel.tex` は全coherenceとcoKleisli生成代数から相対核を作り、既に構成した全cの線束比較のsmoothnessを使ってλ²=28/27を決める。特異係数では線束圏を扱い、全coherent圏や相対perfect対角を仮定しない。

**零係数の比較に使える新たな入力と限界。** 混合稿 `mixed/equivariant_window.tex` の `cmo:prop:equivariant-window-hom` は、同変minimal Shamash分解からG=K⊕K(1)⊕K(2)の全stable Homを計算する。次数−1,0,1,2,3の総次元は7,80,162,112,23、対合の正固有次元は6,48,84,48,6、負固有次元は1,32,78,64,17である。これはHHではない。H¹Hom(K,K)から次数零のbar文字が生じるので、有限bar長の打切りには別の縮約の証明が必要である。

混合稿 `mixed/equivariant_deformation.tex` は、h=0の滑らかなFermat型端点とh=1のA₀を結ぶ中心三次族について、全次数自由性、実形式MF関手・逆関手とgraph核、指定可換h候補への全形式次数の同定を与える。普遍αのHeisenberg対称性はpotentialを三係数a,b,cへ制限し、u=0の楕円中心商と二次jetがb/a=h²/3を決める。共通の形式単元a,cの座標補正で両ブロックを同時に正規化できる。`mixed/kernel_specialization.tex` は一般点非PIのまま通常coherent射影積を使い、0,1を含む相対perfect対角と、選択した一般点perfect核のh=1での整延長を構成する。残る特殊化条件は適切な整核のunit/counit defectを零にすることであり、固定点で別に構成した同値核との互換性を自動的には得ない。

**固定零係数の実核と計算模型。** `mixed/spherical_boundary_class.tex` の `cmo:thm:fixed-zero-commutative-kernel` は、境界変形のBocksteinとHeisenberg対称性から球面関手のtwist射を比較し、全coherenceの復元を経てK_Rの比較核と制限intertwinerを構成する。二成分の接着、内在的指標χと平方根補正、二重同変化によって通常のKu同値を得る。補助資産 `mixed/curved_invariant_model.tex` は実曲率wを持つrank128のMFを有限摂動でrank80へ縮約し、三つの内部shiftからK_Rの生成対象を作る。12 PASSの再現コードはMF恒等式と両向き写像・homotopyを検査する。80は自由MFの総rankであり、End代数やHHの次元ではない。

### P0：主予想の存在領域を全対象へ広げる

1. **固定切片の十二係数から、最初の非零値を実計算する。** `ifj:thm:twelve-coefficients` の標準Hesse方程式・Jacobian線型切片・反転同変原点核・指定周期を固定する。`ifj:eq:probe-table` の四つの一変数probeに沿って、逆向き混合成分の二次四係数と純因子成分の三次八係数を求める。まず `ifj:prop:pbw-curved-mc` の曲率付きMC恒等式を固定して `ifj:prop:pbw-jet-degree` の2つの厳密線形源変形と2つの二次源変形に対して、分離原点の有限Koszul--Shamash比較核から実際の収縮(i,p,h)を固定し、`ifj:eq:pbw-hpl` の二次・三次の演算と必要な高次積・unit/counitを評価する。得られた可換側の原式G₁をまず固定切片に正規化し、その後は `ifj:prop:direct-probe-readout` の二次14・三次32（四probe通算46）の単項式係数だけを原式G₂,G₃から抽出して十二係数を取得する。全三次式を展開する必要はないが、純Y三次のκ/(3a₁τ₁)対合補正 `ifj:eq:direct-jet-observables` を必ず入れる。`ifj:prop:central-norm-jets` の明示中心normは、一次KSでC₂₁とC₁₂を取り違えるため、原点核の高次出力を得る代用品としない。判別楕円との二重isogenyにはM_τ=O(p−o)が不可避で、theta中心文字も反転する。±三次元固有空間・逆中心文字と原点比較のPicard線束・rotation・指定周期を保持して高次移送を構成する。最初の有限座標入力には`ifj:eq:cubic-sextet-basis`の六つの基点付き三次式・6×6 deck作用に加え、`ifj:prop:double-cover-algebra`のR⊕Iと`ifj:prop:two-torsion-matrix-factorization`の両側2×2 MFを使う。実比較核のwindowへ移す際、O(−p)のO(o)一点捩れ・deck符号・最上Koszul線・rotationと三乗周期を同時に追跡し、通常の整数次数shiftで一点捩れを代用しない。 有限被覆側には`ifj:eq:cover-picard-idempotent`と分離Casimirを保持する。Picard線束を実核へ入れる一次的な入口として`ifj:prop:picard-symmetric-linear-mf`の直接の対称3×3 MFと、随伴行列で規格化したM²の評価を優先する。これにより2×2 MFへ別途O(o)を作用させる処理を減らせるが、これは可換一因子に限る。四混合probeではこのMFはs-定数なので、有限被覆/因子Picardの単独微分では46原式係数は得られない。今後は実Koszul–Shamash模型で混合PBW曲率のm1,m2と原点特殊収縮(i,p,h)、comparison unit/counit、rotation・三乗periodを具体構成する。相対HH収縮とKu比較のHPL用hを同一視しない。通常の二次多項式による中心平方座標化を代用としない。一般一次尺度には `ifm:thm:scale-cubes` と選択したKummer枝を使い、同一因子・同一重みでは交換同変尺度を固定できる。自由な標的形式座標で高次を消して数値計算の代用とせず、非零値を得たら核・周期・座標依存を明記する。十八・二十変数の方程式の具体化はこの固定切片で進める。
2. **比較核のKummer三枝を選び、因子moduli上の降下を調べる。** θ³=(τ₁³−1)/(τ₂³−1)の有限étale三重被覆は非自明であり、有理的な大域sectionはない。`ifv:lem:moving-split-kernel` の実相対核におけるPicard線束、三捩れ補正、周期の三乗根と、`ifm:cor:kummer-scale` の各枝を対応させる。尺度torsorだけから全標識付き核のgerbeや、その中立化・最小比較次数は結論しない。一般係数の有限étale比較は構成済みだが、比較三次族と核の元の係数空間への大域降下は残る。
3. **残余smooth locusの境界と核延長を調べ、全intrinsic対象へ進む。** 九変数の全係数AS/CY、十八変数の正確な周囲正則域D(Δ)、二十変数の形式完全性・モジュライの稠密開・一般係数の有限étale比較は既知の入力とする。rank-oneの一般一方向判別はD(Δc)内部にも残余非smooth点があることと、その特異値・節点重複度・D₄合流を明示した。まず `ifd:thm:residual-a2` の中心chartとunit/counit defectを使い、実際のsmooth域・境界での核延長を調べる。一般の複数ordered pairの高次障害、既存O-marked認識と表示被覆を調べ、全smooth係数の比較や主予想の「任意」を現在の稠密開・表示族へ限定しない。
4. **偏極標的への実核と中心作用の比較を調べる。** `mcb:thm:smooth-locus` はX_polによる全smooth locusの判定を与えるが、実Ku核の標的は逐次構成のX_itである。次は `mbl:cor:chart-kernel` の局所核を重なりへ制限し、差となる自己同値・周期位相とČech coherenceを計算する。対角の局所完全性は比較核の貼合せではない。`tcr:prop:joint-comonad` の混合情報と `tcr:ex:same-axes` を保ち、単純な軸データから全比較を決定しない。

### P1：主予想に必要な認識・降下

全O認識、相対双対・coherent飽和、点関手の表示独立性、Ku比較の実perfect核を必要な範囲で整える。一般点・形式完備化・有限Artin jet・固定幾何点を区別する。全作用付き比較を通常Ku比較の必要条件と誤認しない。二ブロックの指定中心μ3は通常Kuの全自己同値群で非正規である。

### P2-A：point/Poisson一致・不一致の例の検証

以下は本文の例と補助的な幾何比較を支える課題であり、主予想と並ぶ存在予想や最優先の研究目標には置かない。既知の証明と計算を保持し、公表に必要な依存関係・適用範囲・文献比較を点検する。

1. **孤立零点定理と被約反例の外部検証・新規性調査。** 全Poisson構造への適用は `poisson-cubic` commit `9f91efa3465f18219c36c31750f1e66220faeaa7` の `thm:pg-normal` に依存する。表示・Jacobi延長・Hessianの基点自由性・Lie代数の根基排除を含む入力と、そこからの孤立零点排除・0次元CIの証明を分けて検証する。五様体では全標的を一括して排除でき、実比較核を持つnorm全64根でも不一致が成立する。不一致の証明と実Ku核の証明の依存を分けて点検する。正式な新規性の確認と外部査読・形式証明は未完了である。
2. **三様体の全スキーム反例と実Ku比較を保持・点検する。** h=1の因子、指定Ω、THCR、分離MF積・Picard補正・周期同期、coherent飽和を入口とする。局所長さ8/埋込み次元3からHessian階数2への帰着、12点の制限三次、Mayanskiyの全Poisson分類、BMMSのcategorical Torelliが全標的排除の依存である。形式復元とspreadは必要入力ではない。この例の自然pairの被約一致は有効だが、全対象での被約point/Poisson一致へ一般化しない。
3. **対象を制限した肯定結果の成立範囲を定める。** 五様体の反例は被約な定常点でも不一致が起こることを示す。したがって「定常成分が滑らか」という条件だけでは全対象の一致は得られない。既知の分離型・定常成分を持たない場合を出発点に、一般混合係数でのDとD_Hの抽象同型、偏極・canonical ring、全Poisson標的の可能性を調べる。n6ではK_D=O_D(1)を使えるが、二次netからsupportを一意に回復する方法には交代行列の偶奇障害がある。詳細はノート。
4. **分離型の局所障害から相対・大域比較へ。** m≥2ではJとJ_clのgraded同型が全スキーム同型の必要条件であり、m=2では十分条件でもある。m>2の局所自明性から大域積を推論せず、中心socle θによる厚みを調べる。自然射のscheme imageは(g^{s+1})、Fitting supportは(g^{8^k})で異なる。j多重集合による自然pairの障害を、全π・全Ku標的の排除へ拡張できる範囲を検証する。

### P2-B：保持する精密算術・分類・公表作業

既存の成果・証明・計算資産は削らない。次の補助課題は、主予想の比較核や表示範囲に関わる障害を解消する場合に優先度を上げる。詳細は研究ノートと各節が正本である。

- 中心作用の無限共役軌道のGalois降下、同種二因子のPell混合核・反転核の定義体、gerbeとperiod multiplier。全中心同変核判定はk≥3なら同種・CMも含み、k=2では幾何学的非同種の場合に適用する。
- scalar和α=Σδ_iと自然位相Cube(v_i(p_i))の同時最小次数。自然周期q(ω³)=−1/v_ω(p)は決定済み。中心標識を忘れた最小次数の低下は未証明。
- 一ブロック残余位相β_n=γ̄_n/[D]のΔD外の分岐、三次位相体上のind(α)、高次元の任意full classと非分裂の別rotation軌道。q=2で付値1 mod3、強化点型のclass一意性、一般split体の最小三、指定非分裂族の点型九・全型三は保持する。
- Oの像を指定しない全第三根、coherent graded-centerの代数的降下、full rotationから点shiftの認識。有限scalar条件と無限位数条件は区別する。
- 公表上の新規性・一次文献比較。既存MF/THCR/Orlov/Thom–Sebastiani/Picard理論自体と本研究の適用を分ける。必要な証明を担当する公表用原稿に保持し、予想を完成した定理と混同しない。
- 三稿の中心結果と文献上の新規性を確認し、Introductionには目的・主要結果・依存・適用範囲を簡潔に置く。詳細な主張と証明は各稿の本文を正本とする。三稿への編集整理、ソース保持、組版、数学的証明の再検証は別の状態として扱う。

## 外部入力・再開と再現

古典Poisson正規形・退化とmoduliの正本は [poisson-cubic](https://github.com/uedakazushi/poisson-cubic)、全次元・全Poissonの代数的中心量子化・中心元・同変降下の正本は [cubic-quantization](https://github.com/uedakazushi/cubic-quantization)。三様体固有の全Abel変形・相対比較と独立した点スキーム論文は [nc-cubic-threefold](https://github.com/uedakazushi/nc-cubic-threefold)。具体的な版・commit・定理・適用条件は [notes/research_notes.md](notes/research_notes.md) と参考文献を参照する。外部repoは通常読取り専用。本稿はB=ambient、A=中心商であり、量子化稿では逆の記法を使う。

孤立零点定理が使う正規形は `poisson-cubic` commit `9f91efa3465f18219c36c31750f1e66220faeaa7` の `papers/support/papers/sections/poisson_geometry.tex`、`thm:pg-normal` に固定する。これは本研究群の未公表入力であり、公表済み分類定理として扱わない。

再開順序は本書 → 適用AGENTS.md → 研究ノートの主予想と該当節 → 該当する稿の証明 → 検証範囲。本文に証明がある既存内容は、planへ全文を重複しない。一般性はgeneralな稠密Zariski開、very general、全固定幾何点を区別し、Brauer–Severi ambientとsplit ambient、実O(1)と偏極類も区別する。

基本確認は `python3 scripts/check_sources.py`、`python3 scripts/build_papers.py`。三稿の他稿参照も含めて組版する。必要な計算の入口はREADMEと検証範囲。PDFは `build/nc-cubic.pdf`、`build/cubic-moduli-descent.pdf`、`build/mixed-sklyanin-cubics.pdf`、SyncTeXも同じ出力先に置く。VS Code/LaTeX Workshopの三稿レシピを使う。GitHub反映は通常commitとmainへのfast-forward、認証できない経路を迂回して権限を広げない。保存の成否と数学的確認を分ける。

双方向Clifford族は `python3 computations/verify_bidirectional_clifford.py`（9 PASS）で有限恒等式を検算する。全二次双対の直交、cocycle・traceの符号、原点完全交叉、中心norm、非正則例、Heisenberg作用、純因子微分と中心規格化を確認する。任意底の相対解消・実核・二十変数形式完全性は本文の証明と独立読解による。

一般尺度は `python3 computations/verify_clifford_morse_scale.py`（8 PASS）、rank-oneのA₂境界は `python3 computations/verify_clifford_rank_one.py`（4 PASS）、固定切片・同変jetは `python3 computations/verify_clifford_jets.py`（7 PASS）を実行確認済み、いずれも終了コード0である。順にadjugateと臨界二次moment・尺度三乗、正則域hとA₂展開、五/四次元の同変空間・最小四probe・Hesse補空間・反転符号を有限検算する（7 PASSの記録は旧スクリプトで、四probe版の全体再実行とは区別）。実核、coherence、Azumaya降下、形式切片の一意性とモジュライの稠密開は本文の証明による。十二係数の数値はこの検算に含まれず、組版・保存の確認状態も別に記録する。

残余KSに用いる有限Jacobian証明書は `python3 computations/verify_interfactor_residual_ks.py`（7 PASS）。全Hesse smooth fiberのJac₃の20次元補空間、(1,2)成分の九基底、指標分解、tensor行列式とFermat特殊化を厳密確認する。実比較核・full cochain移送は本文の証明による。依存する `verify_elliptic_bockstein.py` の8 PASSとともに保持し、今回の再実行範囲は検証資料で区別する。

因子間PBWの有限証明書は `python3 computations/verify_interfactor_pbw.py` と同コマンドの `--clifford`（各6 PASS）。全90一次係数の核12・平行移動rank6、全15定数係数の核6、残余BG恒等式を二つの固定入力で厳密確認する。一般分解と中心障害・積分族の証明は `interfactor_deformations.tex` の三入力節に置く。

多中心の正規形は `python3 computations/verify_multicentral_pbw.py`（4 PASS）、中央pencilの六変数例は `python3 computations/verify_multicentral_pencil.py`（6 PASS）で再現する。前者は普遍式の中心形式代入とuv偏極、後者は192個の単純臨界方向・Hessian・一次jetを厳密確認する。全族核と全一般係数の証明は本文にあり、有限検算だけから結論していない。

二重制限の法線計算は `python3 computations/verify_two_center_restrictions.py`（6 PASS）。独立な4×4行列から二項・三項の混合係数と同軸反例を確認する。

楕円因子の中心障害は `python3 computations/verify_elliptic_center_obstruction.py`（7 PASS）で再現する。普遍Clifford体積元の平方・中心行列式、Q(τ)上の一次障害・全二次補正を消す三汎関数、有理τ=2の全低次補正系の不整合と残る二次中心を確認する。非二捩れでの一般存在と普遍多項式性は本文の証明に依存する。

一般因子のBocksteinは `python3 computations/verify_elliptic_bockstein.py`（8 PASS）。独立左右gaugeと平行移動の一致、Clifford中心平方の二項検出、全Tate逆冪の双次数を厳密検算する。実自己交叉からfull cochain、境界核と全comonadへの移送は本文の証明に依存する。

Heisenberg係数の有限証明書は `python3 computations/verify_mixed_equivariant_coefficients.py`（10 PASS）。群作用と四つの同変写像空間、全kの異ブロック項排除、重み復帰を検算する。比較の自然性・全coherenceは本文の証明に依存し、53/54をχ_kと同定しない。

任意ブロック数の有限証明書は `python3 computations/verify_mixed_multiblock.py`（9 PASS）、線形PBW・普遍中心の証明書は `python3 computations/verify_mixed_linear_pbw.py`（6 PASS）で再現する。前者は普遍臨界代数・sector不等式・一般節点性のseed・中心と可換のMorse尺度一致、後者はQQ上の全係数中心恒等式・PBW重なり・正規形を扱う。全核のcoherenceと全次数PBWの理論入力は本文に置く。

中心方向の有限証明書は `python3 computations/verify_mixed_central_direction.py`（7 PASS）で再現する。Knörrerの法線二次式・非零Jacobian小行列式・P64の二次moment・中央三次MFのMassey係数・重み三単項式を厳密検算する。全comonad比較と実核の同値性は本文の証明による。

明示可換候補の再現入口は `python3 computations/verify_mixed_commutative_candidate.py`（9 PASS）。有理係数Jacobi環から臨界値・Hessian・P64の一致を厳密に検算する。これはKu比較核や全Poisson分類の計算検証ではない。

比較不変量の再現入口は `python3 computations/verify_mixed_comparison_invariants.py`（9 PASS）。c=0候補のJacobian次数二・三の固有部分の有理階数、residueのdeterminant符号、同変HHの算術、pr(O(4)),pr(O(5))のEuler行列を確認する。全Uの相対smoothness・HHの階数一定性・根スタックの圏模型・affine MF比較は本文の証明による。特にaffine MFは全smooth領域で零であり、主予想には内部次数を保持した核が必要である。

## 研究全体に共通する一般原則と保存許可

以下は上の研究固有の計画とは別の継続原則である。

- 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化するよう目標を柔軟に変更する。重要な変更は現方針として理由・解決済み範囲・未解決点を整理し、変更履歴を蓄積しない。
- 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別し、仮定・依存・証明所在を記す。既知結果と本研究の成果を区別し、新規性の未確認を明記する。誤りが判明したら依存する本文・要約・方針も更新し、有用な反例や本質的障害はノートに残す。
- 公表稿では重要な文献の一次資料を確認し、Introductionで仮定・範囲・貢献を比較する。未確認内容や書誌を推測しない。必要な識別子・参照箇所を残し、外部PDFの大量収録を避ける。
- GitHub 管理の主原稿は本文を持つ `papers/<リポジトリ名>.tex` とする。新規原稿・組版環境では research-hub の `papers/paper-template.tex`, `papers/README.md`, `.latexmkrc`, `.vscode/settings.json`, `.vscode/extensions.json` を参照し、有効な既存設定を保つ。改名時は input・文献・分割原稿の root・README・方針・PDF と SyncTeX の参照を整合させる。
- 原稿は現在の成果を理解しやすい順に構成する。版ごとの追記・補遺を積み重ねず、新しい内容は適切な場所へ統合する。未完成箇所を完成した定理として扱わない。標準は日本語LuaLaTeX、簡潔で内容を示すファイル名。
- 研究ノートは現在有効な知識に絞り、着想、計算、例・反例、失敗の本質、文献比較を保持する。論文の証明全文を重複しない。会話、実況、作業ログ、解決済み課題の経緯は残さない。
- 最新の一式だけから再開できるよう、方針・ノート・原稿・再現コード・入力を整合させる。過去のZIPや旧稿を取得することを再開の前提にしない。
- 履歴・重複・不要物を除去して軽量化し、数学的内容や検証可能性を削らない。現行の証明書・不可欠な入力・依存は保持する。固定のページ数・容量上限を目標にしない。
- 研究の区切りごとの生成・検証・保存は、ユーザーの再承諾を求めず実行する許可がある。**正本は指定された `uedakazushi/nc-cubic` の main**。通常の fast-forward 保存を用い、force push、PR、GitHub Actions、PDF/ZIP/中間生成物の追跡は行わない。既存の外部Git管理項目をLibraryへ重複保存せず、GitHub保存が失敗した場合だけLibraryを代替保存先とする。既存Libraryファイルの削除は別の操作であり、明示指示なしに行わない。
- 一式と主要文書に日付・版番号を付け、現行版だけを収録する。配布前に欠落、参照、必要な組版と計算を確認する。生成・検証・保存を別の状態として扱い、実際に確認したことだけを報告する。

研究の区切りでは、先に本repoを保存し、その内容に基づいて research-hub の該当項目を更新する。最新のhubを読み、他研究と並行変更を保持する。対象repoの保存・hub更新・数学的検証は別々に確認し、hubに未反映の項目があれば理由を報告する。詳細な証明・todoは本repoを正本とする。
