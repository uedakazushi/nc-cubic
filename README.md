# 非可換三次超曲面の可換復元とモジュライ

2026年11月23日 / v90。日本語LuaLaTeXによる公表用三稿と再現資料。再開時は [研究方針](00_research_plan.md) を最初に読む。

**本文を持つ主原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)。** 研究方針とノートを共有し、公表用本文は中心問題ごとの三稿に分ける。

| 公表用原稿 | 役割と証明の範囲 |
| --- | --- |
| [nc-cubic.tex](papers/nc-cubic.tex) | 主予想、完備MF移送と一般点可換復元、楕円因子の基礎・分離型の直接Ku比較、残余圏の認識と可換実現の開性、三様体の点スキーム不一致例。 |
| [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) | 構造対象付きモジュライと表示認識、相対点関手・Poissonモジュライ、精密なPicard/Brauer/Kummer降下、周期位相と最小比較次数。 |
| [mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) | 混合Sklyanin族の有限中心・局所代数・全smooth locus、任意固定楕円因子の全許容PBW・中心比較、全smooth多中心対象の比較と中央Bertini、固定tensor境界のPBW分解とClifford混合族、零係数の球面接着と有限MF模型、指定h候補の一般点核・整延長、被約point/Poisson不一致例。 |

各数学的な節の本文は一つの稿を正本とし、他稿では稿名と定理番号を付けて参照する。組版設定は `papers/common/preamble.tex`、書誌は `papers/references.tex` を共有する。混合稿の本文は `papers/sections/mixed/` に置く。三稿の整理は、既存の数学全体を新たに証明・検証したという意味ではない。

全次元・全ブロックの代数的量子化は [cubic-quantization](https://github.com/uedakazushi/cubic-quantization)、古典的Poisson正規形・退化・モジュライは [poisson-cubic](https://github.com/uedakazushi/poisson-cubic) を参照する。

## 最優先目標と現在の到達点

**二十変数のClifford族は、幾何的形式変形の全体とモジュライの稠密開を実現する。** 両Clifford因子の十八の混合係数に、二つの因子係数τ₁,τ₂を加えた族を構成した。[二十変数族の局所完全性](papers/sections/mixed/interfactor_clifford_versal.tex)は、任意の許容分離点で残余KSが三次四様体の幾何的20次元接空間への同型となり、原点を標識した形式変形空間そのものが同型になることを証明する（`ifv:thm:versal`）。さらに係数空間の非空稠密開Uの有限étale全射V→U上に、滑らかな可換三次族と実相対perfect比較核を得る。分類写像V→𝔐₄^cubはétaleで、像はモジュライスタックの稠密開となる（`ifv:cor:generic-comparison`）。一般係数体でも有限分離拡大上に全coherent Ku比較がある。有限化したUが指定分離点を含むとは限らず、全22次元の非標識圏変形、粗モジュライへのétale性、全三次四様体・全smooth係数・全intrinsic対象の被覆は結論しない。

**十八変数の周囲代数の正則領域を正確に決定した。** [双方向積分と相対正則性](papers/sections/mixed/interfactor_clifford_bidirectional.tex)では、全係数で中心平方上のClifford tensor表示と自由階数64を得る。二次双対は可換六二次式商のcocycle twistである。この可換商は六二次式のresultant開D(Δ)上で完全交叉となり、Δ≠0が有限大域次元・AS-regular性の正確な領域である。ここでは次元/index6、任意底変更に保たれる有限射影Koszul双加群解消とuntwisted相対6-CYを持つ（`ifb:thm:regularity`, `ifb:cor:exact-regular-locus`）。別の明示的な主開D(c)では指定中心三次が普遍正則で、その商は平坦である。τ₁=τ₂=2、Λ=M=I₃はΔ=0で大域次元が無限となる例で、a₁=a₂=1ならc=196≠0となる。平坦性とHilbert級数だけではAS-regular性を判定できない。

**周囲がAS-regularでも、残余圏が非smoothとなる具体点がある。** [rank-one sliceの境界](papers/sections/mixed/interfactor_clifford_rank_one.tex)では、Λ=λE₁₁、M=μE₁₁の正確なAS-regular域をh=(1−τ₁³)(1−τ₂³)−τ₁²τ₂²λμ≠0と決定した（`ifd:prop:ambient-locus`）。τ₁=τ₂=2、a₁=a₂=1、λ=μ=−6ではh=−527、c=196で、周囲代数はAS-regular・6-CY、中心三次も正則である。しかし射影Azumaya chartの完備局所代数はMat₄(C[[t,u,v,r,s]]/(t³+uv+rs))となり、点対象の自己Extは高次数まで非零である。全coherent残余圏は非proper、残余線束圏は非smoothとなる（`ifd:thm:residual-a2`）。従って周囲の正則開D(Δc)を残余smooth locusと同一視できない。この対象は主予想のsmooth仮定を満たさない。さらに[階数一残余判別曲線](papers/sections/mixed/interfactor_clifford_rank_one_caustic.tex)では、軸上の中心normの三次判別が(λμ−τ₁τ₂)²Qへ分解することを計算し、Q=0のAzumaya部分を残余非smooth locusへ含めた。等τ・等重みの場合Qは有理三尖点四次曲線となり、一般A₁点と3つのA₂ cuspを持つ。τ=2、λ=15/2、μ=−6は周囲AS正則域にある有理A₁例。さらに[中心normの全特異判別](papers/sections/mixed/interfactor_clifford_rank_one_fullnorm.tex)では、四つの二変数三次の判別式の積が零であることと射影norm超曲面の特異性が同値になる。τ=2、λ=0、μ³=−196、a_i=1ではh=49、c=196、軸上Q≠0のAzumaya通常二重点を得て残余非smoothを示した。これはnorm超曲面の全特異判別であり、残余圏の全smooth locusや比較核の延長の決定ではない。

**九・十八変数の局所Ku比較を、実相対核で構成した。** [十八変数の残余模型](papers/sections/mixed/interfactor_clifford_bidirectional_geometry.tex)により、四次元型と中心変数一つを加えた五次元型の双方に、分離点を含むsmooth proper開とétale局所perfect比較核がある。四次元型の十八方向の像はJac(f₁)₁⊗Jac(f₂)₂⊕Jac(f₁)₂⊗Jac(f₂)₁であり、幾何的形式空間への形式像は余次元2となる。各一方向の九変数族については、[全係数の周囲AS/CY定理](papers/sections/mixed/interfactor_clifford_regularity.tex)、[原点近傍のsmoothness](papers/sections/mixed/interfactor_clifford_smoothness.tex)、[階数9・余次元11の接写像](papers/sections/mixed/interfactor_clifford_tangent_product.tex)も保持する。四次元の比較には、[rotationを持ち上げる変形の形式認識](papers/sections/rotation_preserving_deformations.tex)を用いる。

**一般の混合一次尺度は、指定周期に対応する三枝まで決定した。** [Heisenberg同変比較](papers/sections/mixed/interfactor_clifford_equivariant_ks.tex)を選ぶと、L(e_a)=ℓX_a、Q(y_b²)=q[Y_{b+1}Y_{b+2}]となり、一方向の一次式はF+κ₁₂ΣΛ_ab X_aY_{b+1}Y_{b+2}である。標準方程式f_τ=τΣZ³−(2+τ³)Z₁Z₂Z₃と元の関係係数を固定し、d_i=τ_i³−1と置く。[Morse比較による尺度決定](papers/sections/mixed/interfactor_clifford_scale.tex)は

\[
\kappa_{12}^{3}=\frac{8a_1^3d_1^2d_2}{27\tau_2^3},\qquad
\kappa_{21}^{3}=\frac{8a_2^3d_2^2d_1}{27\tau_1^3}
\]

を与える（`ifm:thm:scale-cubes`）。既存の較正ℓ_iq_i=2a_id_i/(3τ_i)、κ₁₂κ₂₁=4a₁a₂d₁d₂/(9τ₁τ₂)と合わせると、θ=(a₂τ₂/a₁τ₁)(κ₁₂/κ₂₁)はθ³=d₁/d₂を満たす。この非自明なμ₃-torsorは因子係数空間上の有限étale三重被覆で、有理的な大域sectionを持たず、三枝は周期付き比較の選択で実現する（`ifm:cor:kummer-scale`）。固定した実核と周期には一つの枝が対応し、尺度を任意に正規化し直せるわけではない。同一因子・同一重みの交換同変核では両κ=2a(τ³−1)/(3τ)を保持する。尺度torsorを全比較核のgerbeと同定したとはしない。

**任意のClifford二因子の一方向probeで中心norm判別を完全決定した。** [一般一方向の四臨界値](papers/sections/mixed/interfactor_clifford_oneway_discriminant.tex) の`ifod:thm:general-values`は、Λ=sE₁₁、M=0、任意の許容τ_iと非零重みについて、四つの明示非零ρ_{εδ}の三乗根が全特異係数であることを示す。全sで周囲AS正則・中心三次正則、中心norm特異点は全てAzumayaで残余非smooth。τ₁³≠−2、τ₂³≠4ならノード数1/3/3/9、schematicな判別は∏(s³−ρ_{εδ})^{3^{ε+δ}}でs次数48。特殊値ではD₄（Milnor数4）または四変数Fermat三次のsuspension（Milnor数16）へ合流する。対称τ₁=τ₂=2の既存12値は特殊化として保持する（`ifn:thm:symmetric-probe`）。全残余smooth locusと固定Hesse切片の12高次係数の実計算を決定したものではない。[再現コード](computations/verify_clifford_general_oneway.py)。

**固定した可換方程式の高次項は、まず十二係数の実計算へ帰着する。** [固定切片と同変jet](papers/sections/mixed/interfactor_clifford_jets.tex)は、両Cliffordの標準Hesse方程式、Jacobian補空間による線型切片、原点の実核・指定周期を固定すると、形式可換方程式が一意になることを示す（`ifj:lem:linear-slice`）。Heisenberg群の二因子作用に対する二次covariantと三次不変式は各五本であり、周期と両立する反転同変実核を選ぶと各四本に減る。一方向九変数族の逆向き混合二次項は四係数、二つの純因子三次項は八係数で尽くされ、最小四つの一変数probeで回収できる（`ifj:thm:twelve-coefficients`）。**この4+8=12個の数値は未計算**である。ただし[PBW摂動と三次移送](papers/sections/mixed/interfactor_clifford_jets.tex)で、四つのprobeの源curved代数演算が単位行列・行和の二方向は厳密に一次、残る列和・対角の二方向は二次に止まると証明した。非零な二次演算は四つのPBW構造定数だけで、中心三次は全方向で一次。原点に選んだ収縮(i,p,h)のもと、HPLによる二・三次の移送を有限式へ還元した（`ifj:prop:pbw-jet-degree`, `ifj:lem:pbw-hpl`）。必要な原点核・周期に沿った収縮と高次三次式G₁,G₂,G₃の算出は未完成。一方、得られた三次式を固定Hesse切片に移す**後段の正規化は構成済み**である。全56単項式のJacobian射影Πと逆補正𝒥、三次Taylor係数の再帰公式を [明示的正規化命題](papers/sections/mixed/interfactor_clifford_jets.tex) に証明し、[有限計算器](computations/verify_hesse_slice_transfer.py)を追加した。一次項が切片内でも、二次のJacobian座標補正が三次の純因子項を非零にできるため、三次式の直接射影だけでは一般に誤る（`ifj:ex:third-coordinate-artifact`）。 さらに[46係数の直接読出し命題](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:direct-probe-readout`）により、四probeについて二次14枠と三次32枠の原式単項式係数だけで固定Hesseの4+8係数を回収できる。純Xの三次係数には二次gauge補正がなく、純Y側にはκ/(3a₁τ₁)とG₂の平方混合係数の対合補正が必要である。[厳密検算器](computations/verify_hesse_probe_readout.py)を保存した。[厳密PBW検算](computations/verify_clifford_jet_transfer.py)も保持する。自由な標的形式座標で高次項を消せることと、固定した多項式切片で数値を求めることは別である。

**非可換PBW源の二次障害と中心曲率をHochschild複体で明示した。** [混合稿の命題](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:pbw-curved-mc`）で、m_s=m₀+sm₁+s²m₂の厳密な結合律から∂m₂=m₁∘m₁、三・四次整合式を導き、中心体積元ω₀+sω₁の交換子を各次数で零と証明した。非線形二probeでは`(m₁∘m₁)(e₂,e₃,e₁₂)=L₁L₃≠0`であり、既知の四つのm₂成分が必須の二次補正である。源Cliffordの8基底について512 triple×5次数と曲率4次数を[厳密記号検算](computations/verify_clifford_curved_pbw_mc.py)で10群PASS。これは実Ku比較核の原点収縮(i,p,h)・比較のunit/counit・rotation/period・12高次係数を求める前の入力である。

**分離原点のS₃厳密同変Shamash模型と九変数混合族のS₃×S₃対称性。** [現行命題・補題](papers/sections/mixed/interfactor_clifford_explicit_shamash.tex)（`ifj:prop:clifford-explicit-shamash`, `ifj:lem:mixed-clifford-s3-family`）では、Clifford augmentationの4×4 MFを巡回・反転同変に規格化し、反転−Pに対するKoszul四項の作用(1,−P,P,−1)、最上線の符号−1を決定した。二因子32|32外積を保ち、九混合係数Λの行・列を同時に置換するS₃×S₃作用が二次関係と中心wを固定することを証明した。選択済み同変(n−1)次MF jetのn次持上げ方程式が可解なら、解を36元平均して同変化できるが、**可解性は未証明**。一因子の[15群厳密検算](computations/verify_clifford_explicit_shamash.py)、九変数族の[8群検算](computations/verify_clifford_family_s3.py)はいずれもPASS。現行TeXの独立LuaLaTeX二巡・3頁組版、表示点検済み。実Ku核・比較Hom special retract(i,p,h)・unit/counit・rotation/三乗period・46原式/12高次係数は未構成。

**双方向Clifford混合族の全六段Koszul微分を正則resultant開で構成した。** [初段・中心primitive](papers/sections/mixed/interfactor_clifford_mixed_koszul_endpoints.tex)（`ifj:prop:mixed-koszul-endpoints`）でd₁,d₂、[三次全20列](papers/sections/mixed/interfactor_clifford_mixed_koszul_full_d3.tex)（`ifj:thm:mixed-koszul-full-third`）で全係数上の大域自由基底K₃(20)を構成した。**[Frobenius上位微分の定理](papers/sections/mixed/interfactor_clifford_mixed_koszul_frobenius.tex)**（`ifj:thm:mixed-koszul-frobenius-upper`）は、二次双対E=D^χのE₂(15),E₃(20)の平方なし積を全係数上で基底化し、resultant開Δ_res≠0では正規化socle γと完全積対合からK₄=E₂,K₅=E₁,K₆=E₀を自由基底にする。d₄の全300成分を `Σ_j z_j t(mν ζ_j q_r)`、d₅をE₂の二次積、d₆を六生成元列として**有限計算式**で指定し、d₃d₄=d₄d₅=d₅d₆=0を証明。全六段の完全性は既存`ifb:thm:regularity`を入力とする。新しい[厳密計算器](computations/verify_clifford_mixed_koszul_frobenius.py)はτ_i=2,U₁₁=V₁₁=1,s=1の非自明な双方向例でγ=33u₁u₂u₃v₁v₂v₃、d₄のy₁/33成分、既存d₃の20列一致と三合成零を検証（新12群＋依存d₃の9群PASS）。**Δ_res=0への基底延長や、Shamash中間・高次homotopies、混合32|32MF、Ku比較Hom・unit/counit・rotation/period・12高次値は未完成。**

**一方向Clifford九変数族の一次Shamash homotopyを二つの中間成分まで構成した。** [最初の成分](papers/sections/mixed/interfactor_clifford_mixed_shamash_first_middle.tex)（`ifj:prop:mixed-shamash-first-middle`）はd₂H+u d₁=wI₆、[第二中間成分](papers/sections/mixed/interfactor_clifford_mixed_shamash_second_middle.tex)（`ifj:prop:mixed-shamash-second-middle`）はd₃G+Hd₂=wI₁₅を全許容τ_i、全九係数V=0についてs二次以下に選べると証明。さらに`ifj:cor:mixed-shamash-entire-first-degree-bound`は一次s₁全体のs次数を**抽象的に高々2**とする。τ_i=2,a_i=1の九変数全体では前段336×315階数210、第二段840×420階数336の正確な有理数小行列を使い、HとGを二次多項式として実係数構成。新しい[第二段の厳密検算](computations/verify_clifford_mixed_shamash_second_middle.py)は9群PASS（依存するHの7群もPASS）、一次9・二次45・三次165の全U単項式の840行×15列を係数ごとに検査し、四最小probeと一般整数係数例でも実Clifford積を直接検査。新証明節は日本語LuaLaTeXで3頁独立組版・全頁表示点検済み。**P₃–P₅のs₁行列、s₂以降・混合32|32MF・実Ku比較Homの収縮/period・四probe46原式/固定Hesse12数値は未完成。**

**Clifford 中心normは明示できるが、可換Ku標的そのものではない。** [全九変数の中心norm三次展開](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:central-norm-jets`）では、体積元の平方`ω_x(s)²=−det q_x(s)`を三次まで厳密に計算した。Hesse射影の二次同変係数は一つの三次Heisenberg不変式𝒮のgradient、三次純Y係数は(∂𝒮/∂τ₁)/4で、最小四probeのうち列和と対角の二つにだけ非零の三次normがある。一方、平方中心変数を可換Hesse座標と文字どおり同定すると一次像はC₂₁であり、実Ku比較の一次像C₁₂と一致しない（`ifj:cor:central-norm-probes`）。従ってこの計算は未決定のβ・γの値ではなく、実核・周期付き移送を省略できないことの具体的な証拠である。[厳密記号検算](computations/verify_clifford_central_norm_jets.py)は7群PASS。GitHub保存済み本文を読み戻して復元・再実行し、同じ7群PASS・終了コード0を確認した（再取得ファイルのSHA-256は[検証記録](notes/validation.md)）。

**中心判別楕円は点楕円の二重 isogeny 商である。** [Clifford中心と点楕円の二重 isogeny](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:thm:discriminant-two-isogeny`）では、分離判別のD_τ=(τ³/8)f_{−2/τ}と、点曲線E_τからE_{−2/τ}への次数2 isogenyを元のClifford規約で明示した。核は標準原点oと非零二捩れ点p=(1:1:τ)。往復[−2]、三捩れ標識への作用diag(1,−1)を得る。偏極の引戻しφ*O(1)=O(2)⊗M_τ（M_τ=O(p−o)）なので、元のHesse射影座標の通常二次式三本による表示ではない（`ifj:cor:isogeny-picard-line`）。M_τは分離原点の実Picard–rotation比較で使う線束と同じ。一般のCayleyan二重isogenyは既知理論として引用し、本研究の具体的な係数照合と分ける。[厳密検算](computations/verify_clifford_hesse_two_isogeny.py)は8群PASS（GitHub保存ソースの再取得・実行確認）。ただし二重isogenyから実Ku比較核・12高次係数を求めたわけではない。

**二重isogenyのtheta表現を有限次元で分離した。** [theta文字・Picard障害の命題](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:two-isogeny-theta-characters`）により、引戻し偏極A=φ*O(1)=L²⊗Mに対して三捩れtheta交換子はe_A=e_L²=e_L⁻¹と反転する。H⁰(E,A)はdeck対合の±固有空間に各3次元（6=3+3）で分解し、双方は標準3次元Heisenberg表現の双対型となる。一方、普通の二次式も中心文字は反転するので、表現論だけでは二次座標表示を否定できない。**本当の障害はHom_E(L²,A)=H⁰(E,M)=0** という非自明二捩れ線束の消滅である。τ²=−2では自己二重isogenyの平方は[−2]、j=8000、End(E)=Z[√−2]となるが線束障害は残る（`ifj:cor:two-isogeny-cm-specialization`）。[有限厳密検算](computations/verify_clifford_hesse_theta.py)6群PASS、ただしKu核移送や12係数の実値ではない。

**二重 isogeny の6次元線型系を元の平面上の三次式で表示した。** [三次式とdeck行列の命題](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:two-isogeny-cubic-sextet`）では、適切な線型座標W,T,Sにより点曲線をWS²=T³+aWT²+bW²Tと書き、六つの三次式W²T,W²S,WT²,WTS,T³,T²Sが共通基点因子2o+pを持ち、これを除くとφ*O(1)=O(2)⊗Mの切断空間を与えることを証明した。deck変換はU=T/W,V=S/W上で`D(g)=U⁴g(b/U,−bV/U²)/b²`となり、正負3次元の明示固有基底を得る。正の三次式から標的のHesse座標を再構成し、次数9の多項式恒等式と反転同変性を確認した。二重被覆の負固有線束は標的のM_{τ∨}に一致する。[8群厳密検算コード](computations/verify_clifford_isogeny_cubics.py)をGitHub保存後にblob同一性を確認済み。これは**実Ku比較核や46個の原式係数を求めたことではない**。

**Picard二捩れの有限相対模型。** [相対二重被覆とPicard MF](papers/sections/mixed/interfactor_clifford_jets.tex) において、B=K[ξ,η]/(η²−g(ξ²))、R=K[X,Y]/(Y²−Xg(X))、X=ξ²、Y=ξη、deck同時符号反転という相対有限étale二重被覆を得た。符号成分はI=(X,Y)でI²=(X)、B=R⊕I、積はij/Xと厳密に書ける（`ifj:prop:double-cover-algebra`）。素朴な√X被覆には偽の節点があり、η=Y/ξによる正規化が必須。源Mτと標的Mτ∨の二捩れPicardを同形の斉次2×2行列分解から得るが、その余核層O(−p)をO(p−o)へ変える一点捩れO(o)は整数次数shiftではない（`ifj:prop:two-torsion-matrix-factorization`）。標的符号線束は被覆に引き戻すと自明だがdeck符号が残る。保存された[11群の厳密検算](computations/verify_clifford_double_cover_mf.py)は実行したコードとGit blob SHAが一致する。非可換Ku比較核と46原式係数・12係数の数値は未完成。

**二重被覆のtrace・対角分離元と相対HH収縮を完全表示した。** [新命題と証明](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:cover-trace-casimir`, `ifj:cor:cover-hochschild-contraction`）は、符号固有線束I=(X,Y)を冪等行列P_I=δ⁻¹[[-X(X−2a),−Y(X−2a)],[Y,g]]の像として扱い、BをR³の階数2直和因子にする。被覆のΘ=(η⊗η−(X−2a)ξ⊗ξ)/δはΘ²=1で、e+=(1+Θ)/2がB⊗_R Bの対角を切り出すtrace-Casimir/分離冪等元となる。これにより有限被覆のunit/counitに必要な分裂と、任意のB-双加群係数でHH_R^{>0}(B,M)=0を示す明示Hochschild収縮が得られる。形式的a(s),b(s)の三次jetではδ(s)⁻¹を直接展開すればよく、有限étale被覆のArtin持上げの一意性は[Stacks Tag 0BQB](https://stacks.math.columbia.edu/tag/0BQB)の既知結果。[厳密計算](computations/verify_clifford_cover_trace_casimir.py)はGitHub保存済みソースを独立に復元・実行し、SymPy 9群PASS・終了コード0、Git blob SHA一致まで確認した。ただしこれは**Ku側の曲率付きKoszul–Shamash HPL収縮ではなく**、rotation・三乗周期と46原式係数、12数値は未完成。

**二捩れPicardの一点捩れを直接的な対称線形MFで内蔵した。** [新命題と系](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:picard-symmetric-linear-mf`, `ifj:cor:picard-symmetric-hesse-family`）では、Weierstrass三次F=Y²Z−X(X²+aXZ+bZ²)に対してL=[[X,Y,0],[Y,aX+bZ,X],[0,X,−Z]]の行列式をFとし、余核がM=O_E(p−o)となる対称3×3線形MFを構成した。従来の2×2 MFが余核O(−p)だったのに対し、今回は一点捩れO(o)を別操作なしで次数零線束として保持する。−adjLはu=X/Zで規格化したM²≃Oの対称積行列であり、反転D=diag(−1,1,1)と厳密両立する。元のClifford Hesse fτへの座標変換ではdetLτ=4cτ² fτ、第二微分(4cτ²)⁻¹ adjLτで指定方程式を分解し、別途μ₃枝を追加しない。一般的な線形対称表示はBeauville・Buchweitz–Pavlovの既知結果として一次資料を引用。[厳密検算コード](computations/verify_clifford_picard_linear_mf.py)は10群PASS、ローカル独立LuaLaTeX簡約抜粋1頁を2巡組版・表示確認。**ただし四混合probeではPicard MFはsに依存しないため、実Ku核・12係数の数値はまだ未構成**。

**対称Picard行列分解から有限被覆の符号積へのアフィン接続を明示した。** [命題と証明](papers/sections/mixed/interfactor_clifford_jets.tex)（`ifj:prop:picard-affine-bridge`）では、3×3対称行列分解LをZ=1で三角共役し、2×2行列S=[[x,y],[y,x²+αx+β]]と可縮な一階因子に分解する。coker S≃I=(x,y)、β可逆ならI²=xAなので規格化したM²積はrs/xとなり、二重被覆B=R⊕Iの符号成分の積と一致する。反転も厳密に保たれ、xの逆元は使わない。[有限恒等式の検算コード](computations/verify_clifford_picard_affine_bridge.py)は8群PASS。これはアフィン上の縮約で、斉次Picard線束の一点捩れ・非可換Ku比較核・rotation・三乗周期および12高次係数を決めたものではない。

**固定tensor境界の全PBW表示まで、因子別比較の適用範囲が広がった。** [因子間変形の節](papers/sections/mixed/interfactor_deformations.tex)では、任意の可換係数環と厳密な中心変数の下で、因子間の一次・定数補正と内部関係の他因子出力が全て零になることを証明した（`ifp:thm:factorization`）。因子別分解は元の生成元で成立し、形式的gaugeや被約性を要しない。指定中心三次があれば全許容正規形へ入り、smoothness判定・一般中央flag・全coherent Ku比較を適用できる（`ifp:cor:central-comparison`）。固定した最高次境界とPBW性は仮定として残る。

**主予想**は、任意の滑らかな非可換三次n-fold 𝒳に対し、同じ次元の滑らかな可換cubic XとKu(𝒳)≃Ku(X)が存在すること。任意に固定した滑らかな標準Sklyanin因子の組、k≥2、固定非零重み、一つの共有中心変数について、指定境界を保つ全ての因子別PBW・中心三次補正の残余線束圏を可換三次と普遍Morita比較した（`emc:prop:coverage`, `euk:thm:universal-kernel`）。異なるj、同種・CM、二捩れ、有限位数・無限位数を許す。二捩れでない因子は平行移動後の関係式の線形三方向、二捩れ因子は中心へ加えるu倍の平方三方向を一次係数tとする。標的はX=V(G+uQ(t)+u²L(t,α)+u³C(t,α,c))、L=𝔄α+R₂(t)、C=κc+R₁,₁(t,α)+R₃(t)で、𝔄は可逆、κ≠0。可換smooth開では相対perfect核と全coherent Ku同値を得る。定数Bocksteinは3k次元の同型、一次Bocksteinは3k方向で単射だが、比較の存在は単射性を前提としない。各固定tの一般αに対して8^k個の相異なる悪いcと各可換標的の唯一の通常二重点を得て、全係数・各固定tの判別超曲面は既約被約、臨界点のaffine空間が正規化となる。固定(t,α)の一変数特殊化には重複根を許す。

任意個の共有中心変数m≥1を持つ全許容因子別表示で、残余線束圏がsmoothであることと、一中心の係数多項式を偏極した可換三次X_polが滑らかであることを同値とした（`mcb:thm:smooth-locus`）。厳密な中心作用から作る原点blow-up圏、KhanのArtin stack上の分解、各chartへの一中心普遍核、絶対対角のZariski局所性を使い、有限中心性を仮定しない。滑らかな対象には各中間商もsmoothな一般中央flagが存在する（`mcb:thm:central-flags`）。従って、固定因子k≥2・非零重み・任意mの全smooth対象について、次元n=3k+m−2の滑らかな可換三次への全coherent Ku同値を得る（`mcb:cor:all-smooth-comparison`）。ここで実比較の標的は逐次構成のX_itであり、X_polへの実核を同定したとはしない。

全係数の非smooth locusは勾配resultant 𝔇_m=Res(∂W_pol)の零集合に一致し、係数t,α,cの重みを1,2,3とするとdeg_wt 𝔇_m=3m·2^(3k+m−1)となる（`mcb:cor:global-discriminant`）。この全係数多項式の既約性・被約性は未主張である。

二中心ではsmoothnessからΔ≢0が従い、良い中央切断の仮定は不要となる。Δは次数3·8^kである。固定した滑らかな境界からの横断二項写像Bは可逆で、二次・三次係数は三角多項式同型をなす（`mtb:prop:transverse-iso`）。各固定一次係数の一般二次係数では、最後のv³係数の悪い値は相異なる2·8^k個で、各可換標的には唯一の通常二重点がある。全横断係数および各固定一次係数の判別因子は既約被約で、臨界点のaffine空間が正規化となる（`mtd:thm:normalization`）。任意mの各比較段でも同様で、最後の悪い値の数は2^(3k+m−1)。特殊二次係数では重複根を許す。

同一S(1,−1,−1)の既存結果では、指定規約でκ_k²=27/28、κ_k=3√21/14を保持する（`mcs:cor:universal-scale`）。Heisenberg同変な一次像は純ブロックJac₂の直和で、比較の七定数形のうち六定数χ_k,A_k,…,E_kは未数値化（`lec:thm:seven-scalar-form`）。一般の異なる因子へこの数値κを流用しない。指定二ブロックのP64・norm全64根・有限中心と局所型も保持する。残る核心は、全intrinsic対象の認識と表示被覆、最高次の二次境界を変える混合族の固定切片での具体化と全smooth係数への比較拡張、偏極標的への実比較核、因子moduli上の核選択・降下である。一般の比較係数、一般PBW族のPI性・有限中心性、選択済みh一般点核のdefect零特殊化も未解決。

周囲のresultant開D(Δ)、中心三次の正則性を保証するD(c)、残余圏のsmooth proper開は別の領域である。上記A₂例はD(Δc)内部にも残余非smooth点があることを示すが、残余smooth locusの全境界はまだ明示していない。一般係数の有限étale比較を全smooth係数への比較へ拡張したとはしない。十八・二十変数族と尺度・jet・境界の証明の正本は上記の混合稿の各節に置き、研究ノートには再開に必要な要点と残る障害を保持する。

まずC上、n≥3の主予想を最優先にする。genericな表示のみへ「任意」を弱めず、全intrinsic対象の認識と被覆を課題として残す。両Cliffordの二十変数族の形式完全性・モジュライの稠密開・一般係数の有限étale比較、および一般混合尺度の三乗は証明済みの入力とする。次は固定切片の十二係数の最初の非零値を実計算し、比較核のKummer三枝の選択と降下、残余smooth locusの境界と核延長を調べる。偏極標的への実核、全比較核のgerbe、全smooth係数への比較、選択済みh核のdefect零特殊化も継続する。原稿・独立読解・計算・組版・保存の確認状態は [検証範囲](notes/validation.md) を参照する。

- **多中心の全smooth対象と中央Bertini。** [多中心比較](papers/sections/mixed/multicentral_comparison.tex)が入口。[正規形](papers/sections/mixed/multicentral_pbw.tex)が全中心列の正則性を与え、[実blow-up](papers/sections/mixed/multicentral_blowup.tex)が射影方向の圏とOrlov分解を構成する。[smooth locusと中央flag](papers/sections/mixed/multicentral_bertini.tex)でK_A smooth ⇔ X_pol smoothを示し、一般flagから[逐次核](papers/sections/mixed/multicentral_iterated_comparison.tex)を全smooth因子別対象へ適用する。有限中心性を必要としない。
- **横断二項の全階数と最後の中心値。** [Bockstein](papers/sections/mixed/multicentral_transverse_bockstein.tex)は定数関係の曲率と中心一次式のunary微分を分離し、Bの可逆性を証明する。[横断判別](papers/sections/mixed/multicentral_transverse_discriminant.tex)は各固定一次係数の一般二次係数に対する2^(3k+m−1)個の単純悪値、各唯一ODP、判別因子の既約被約性とaffine正規化を与える。

- **中央pencilと二重制限の混合情報。** [切断の判別](papers/sections/mixed/multicentral_pencil.tex)はΔの次数3·8^kと一般係数のLefschetz性を証明する。これはW_polの幾何であり、実標的W_itとの一致は未証明。[二重制限](papers/sections/mixed/two_center_restrictions.tex)は実BC射とjoint comonadを構成し、G+u³+v³とG+(u+v)(u−v)²が同じ滑らかな二軸を持ちながら全体のsmoothnessを異にする例を与える。裸の二軸comonadだけでは全比較は決まらない。
- **異なる楕円因子・二捩れを含む全係数核。** [全許容表示と相対線束模型](papers/sections/mixed/elliptic_mixed_comparison.tex)、[境界の実核](papers/sections/mixed/elliptic_boundary_kernel.tex)、[二つのBockstein](papers/sections/mixed/elliptic_bockstein.tex)、[普遍比較](papers/sections/mixed/elliptic_universal_kernel.tex)が正本。非二捩れの線形P三方向と二捩れの中心β三方向を共通のtとして扱い、𝔄∈GL_(3k)(C)、κ≠0の三角多項式同型で可換族を構成する。全tの一次単射はunaryとbinaryの異なる検出による。次数別自由性・untwisted相対双対を確認し、全comonadからgraph双加群を得る。判別代数の階数8^k、各固定tの一般αでの一節点性とaffine正規化も成立する。
- **S(1,−1,−1)の任意ブロック数の比較と尺度・判別行列。** [多ブロックの中心比較](papers/sections/mixed/multiblock_central_kernel.tex)の `cmm:thm:universal-kernel` は次元3k−1=5,8,11,…を扱う。[尺度決定](papers/sections/mixed/multiblock_scale.tex)の `mcs:cor:universal-scale` は一因子の八つのAzumaya Morse点の外積、全係数の実比較、非零二次momentからκ_k²=27/28を全kで証明する。`cmm:cor:determinantal-discriminant` は普遍rank8臨界代数のtensor積とH=−(2/3)Σa_iα^(i)·x_iからdet(κcI+m_H)を与える。一般αでは8^k個の相異なる悪い中心係数と各標的の唯一ODPを得る。特殊係数の重複臨界値・非被約臨界点を含み、動く重み上の核降下と因子追加に対する標識の互換性は別課題である。
- **線形PBW補正と残余Bockstein。** [線形PBW補正](papers/sections/mixed/linear_pbw_boundary.tex)はM=Mᵗ条件、対角成分を消す唯一の平行移動、三つの線形係数p,q,rと任意αの普遍中心三次を与える。HH²₋₁(S)=Sym₃(C)/Diag₃(C)≅C³に加え、[残余Bockstein](papers/sections/mixed/linear_bockstein.tex)の `mix:thm:linear-bockstein-injection` は3k方向の残余圏への単射性を証明する。自己交叉の双加群類をfull cochainとしてKoszul–Tate模型へ移し、unary成分の対称行列と、独立な左右homotopyが作る対角＋交代行列を比較する。各κ(a)上の値が零でも全自然変換は零とは限らない。具体的なJacobian座標は未算出である。
- **楕円因子の中心三次持上げと二捩れの障害。** [中心持上げの判定](papers/sections/mixed/elliptic_center_obstruction.tex)は、非二捩れの滑らかな標準Sklyanin因子で全PBW係数に普遍多項式liftを与える。二捩れS(1,1,τ)では正規化p=0が必要十分で、許容線形項は平行移動方向に正確に一致する。τ=2,p=(1,0,0)のPBW・CY変形では指定中心三次を持ち上げられず、二次中心7x²+4xが残る。EGの非スカラー中心存在との矛盾はなく、Ku実現予想への反例でもない。二捩れで残る中心平方三方向を含む実Ku比較は、上の全係数定理で構成した。

- **S(1,−1,−1)の七定数表示と判別幾何。** [Heisenberg係数形](papers/sections/mixed/linear_equivariant_coefficients.tex)はQ=χ_kΣa_i(p_ix_iy_i+q_iy_iz_i+r_iz_ix_i)とR₂,R₁,₁,R₃の全候補を与え、異ブロック項を排除する。κ_k以外の六定数は未算出。[判別超曲面](papers/sections/mixed/linear_discriminant_geometry.tex)は任意固定pの一般αで8^k個の唯一ODPファイバーを与え、全係数・各固定pの判別式の既約性、affine正規化、臨界値衝突またはHessian退化という特異点条件を証明する。

- **非分裂comonadによる全線形族の実比較。** [普遍線形比較](papers/sections/mixed/linear_comonad_comparison.tex)は、任意η∈Jac(G)₂のK_η=fib(Id→ρ²)でも正規化比較群が二項Jac(G)₁、三項Cだけになることを示す。実可換族G+uQを参照し、下位構造を一致させた後に次の差を測り、重み1,2,3から多項式L,Cを構成する。四項以降の全coherenceを延長して実coKleisli代数を比較する。PI性を用いず相対potential解消から周囲代数のAS正則性とuntwisted双対性を確認し、可換smooth開では全coherent Kuへ飽和する。この存在比較は上のBockstein単射性に依存しない。

- **中心変数を持つ分離型の可換実現。** [直接Ku比較](papers/sections/central_split_comparison.tex)の `csc:thm:comparison` は、k,m≥1、N=3k+m≥5、全a_i≠0、実楕円因子S_i/(Ω_i)=B(E_i,L_i,t_{p_i})、原点だけにcritical pointを持つ中心三次gについて、A=((⊗S_i)⊗C[U])/(Σa_iΩ_i+g)とX=V(Σf_i+g)の全coherent Ku同値を構成する。f_iは同じ偏極曲線E_iの任意の非零方程式でよい。有限MF外積、周期付きPicard補正、二重同変化から比較し、そのsmoothnessを用いて全coherent圏へ飽和する。中心Fermat和は一変数A2因子だけでも証明できる。
- **中心変数の数による全スキームの違い。** [分離型の点関手と零スキーム](papers/sections/central_split_points.tex)は、固定点なしの楕円点グラフを仮定して原代数の点関手を任意試験環で計算する。m=1、g=cu³、c≠0では、上の同じX上でPt(A)=Z_X(π)=⊔E_iとなる。m≥2でV(g)が滑らかなら、定常成分の完備局所環はJ[[t_1,…,t_{m−2}]]で、J=⊗(S_i)_abの長さは8^kである。可換側ではJ^cl=⊗Jac(f_i)となり、両者の差が全スキーム同型の障害を与える。被約部分は一致するが、全スキームの一致は一般には成立しない。

- **満支持型の同時実現。** [点と零スキームの比較](papers/sections/point_poisson_split.tex)の `pps:thm:elliptic-existence` は、m=0、k≥2、実際の楕円Sklyanin因子・正則中心三次・固定点なしの点グラフという仮定の下で、同じX=V(Σf_i)についてKu同値とPt(A)=Z_X(π)=⊔E_iを証明する。jの相異性・j≠0,1728・2p_i≠0を課さない。自然θが二捩れで零になることは、別の方程式選択による存在を妨げない。基本開では従来の自然なX_ptを選べる。
- **固定された複素三様体での障害。** [点スキームと零点比較の障害](papers/sections/point_poisson_obstruction.tex)は、後述のA★に三つの定常点Spec J_1があることを示す。孤立零点の局所環とHessian階数2の12点の分類により、X★上の全Poisson構造を排除し、categorical Torelliで同じKuを持つ全可換標的も排除する。指定中心元の非零socle値は−4xyz/3であり、j(1)≠j(17/9),0が局所環の差を検出する。実際の因子・正則中心元は [具体的Sklyanin入力](papers/sections/explicit_sklyanin_input.tex) で確認する。一ブロック零スキームのE_H⊔D_H分解と、良いrank2標的への射影埋込み一致障害も保持する。
- **定数型混合族の余有限可換実現。** [混合族の相対滑らかさと余有限可換実現](papers/sections/mixed/relative_smoothness.tex)では、S(1,−1,−1)の定数型PBW変形について、三つの普遍六次中心元を構成し、任意の混合係数で有限中心性を証明した。射影的な中央模型上の対角加群を使い、分離型への収縮族が0の近傍で相対smooth properとなることを示した。従って任意のk≥2、α^(i)∈C³、全a_i≠0について、有限集合Fを除くcでA_c=(⊗_{C[u]}B_{α^(i)})/(Σa_iΩ_i+cu³)の全coherent Kuを滑らかな可換三次(3k−1)-foldとして実現する（`cmo:cor:cofinite`）。この余有限性の議論だけではFを同定しない。現在は `cmm:cor:determinantal-discriminant` がdet(κ_k c I+m_H)による判別集合を与え、κ_k=3√21/14と選べる。判別集合を定常点のnormの根集合とは同一視しない。
- **指定混合族のsmooth locusを完全決定。** α=(1,4,9),(16,25,49)、中心和係数1,100を固定すると、全coherent圏がsmooth properであることは64次終結式P64(c)≠0と同値である（`cmo:thm:exact-sixty-four`）。各中心の14節点のNCCR局所形、全節点での非等方なΩ切断、相対対角の合成、射影境界u=0の検査を用いる。従って **c=0と定常normの全64根はsmooth proper**。P64の64根では36次元simpleの局所模型がMat36上の5次元通常二重点となり、全coherent Kuは非proper、線束圏と残余線束圏は非smoothである。P64と定常normは互いに素であり、pointの出現とsmoothnessを区別する。この全smooth locusでの実Ku比較核も `cmo:thm:all-central-commutative-kernel` により構成済みである。
- **同じ判別式を持つ明示的な可換候補。** G_α=(x³+y³+z³+xyz)/3−u²(α₁x+α₂y+α₃z)、λ²=28/27として、X_c=V(λ(G_{(1,4,9)}+100G_{(16,25,49)})+cu³)⊂P⁶を得た。各Jacobi環の正則表現を厳密計算し、X_cもP64(c)≠0と同値に滑らかで、各悪い係数では唯一の通常五次元二重点を持つと示した。c=0にはEckardt点があり、そのblow-upは超平面と滑らかな三次四様体に分岐する二重被覆のクレパント解消となる（cmo:thm:commutative-discriminant-candidate、cmo:prop:zero-eckardt-resolution）。この指定標的への実比較は全cの残余線束圏上で構成され、全smooth cでは相対perfect核による全coherent Ku同値となる。尺度は実線束比較を構成した後にP64の非零二次momentから決定する。
- **全smooth係数のHochschild群と有理Euler形式。** 指定c族をU=A¹∖V(P64)全体で相対smooth properとする有限中心・平坦対角の模型を構成した（`cmo:prop:full-relative-hh`）。Mathewの相対退化定理から全cでHH₀=C²、HH±₁=C²¹、他次数零となる。pr(O(4)),pr(O(5))は両側の有理数値Grothendieck群の基底であり、共通Euler行列は[[-27,−189],[−162,−1161]]、行列式729（`cmo:cor:rational-euler-comparison`）。この不変量計算は実核の構成とは独立である。実Morita同値は積分数値格子の同型も与えるが、表示した二対象の積分基底性とその同型の基底表示は未計算。
- **零係数の可換標的の実際の残余模型。** 根スタックℛの16例外対象の右直交K≃Ku(X₀)^μ₂とperfect射影核、指標線束NとN²≃Oを保持する。これに加え、中心二重根orderの8例外mutationとKnörrer核により、Ku(Z),Ku(Y)による実SODを構成した。HHの直和一致からSODを相殺したものではない。非可換A₀側のK_Rと球面接着も境界comonadから比較し、下記の通常Ku同値へ接着する。
- **全固定値のaffine MF比較と次数情報の必要性。** 内部次数を忘れた有限射影Z/2-MFを冪等完備すると、一因子の全sと混合族の全cで可換候補と実Morita比較できる。Morse値ではCl₃・Cl₆の局所模型、smooth値では双方零となる（`cmo:prop:pointwise-affine-mf-comparison`）。全smooth cで射影Kuは非零なので、このaffine圏を介するKu同値は得られない。錐の原点・内部shift・三次周期を保つ比較が必要である。
- **低次元単純加群と残余射影。** 二次元単純加群は半跡(a,b,c)∈(C×)³と(a²−bc,b²−ca,c²−ab)=αで完全分類し、退化係数も扱う。abcF≠0上で高次作用の普遍式κ₂=−2N₆/(9F)を得て、三次数体の例では全characterの有限射影次元検査を通りながら、characterを持たない中心値に無限射影次元の二次元simpleが存在する。指定二因子の各8 charactersと各2二次元simpleから得る100tensor simplesは全て射影次元5で、coherent延長は線束perfect。従来の64定常点の残余射影Kには Ext⁰(K,K)=C、Ext¹(K,K)=C¹⁰、他次数0を得た。これら対象のperfect性から全体のsmoothnessは結論しない。別の有理係数α=α′=(9,9,1),c=−1616/3での無限自己Ext例も保持する。 指定二因子ではさらに全simpleを分類し、非Azumaya中心上には各28類、次元1〜5の個数は8,2,8,2,8、正則中心の各点には6次元simpleが一つある（`cmo:thm:fourteen-node-orders`）。
- **主予想の局所開性。** [可換実現locus](papers/sections/geometric_realization_locus.tex)の `grl:thm:open-locus` はn≠4の実smooth proper dg族で可換Ku実現領域がZariski開であり、étale局所に実際のcubic族と比較核があると示す。既存のArtin形式認識と核モジュライの代数性を用いる。全点での存在には境界延長と未被覆成分が残る。

**全中心係数での残余線束圏比較。** [中心超平面の球面制限](papers/sections/mixed/central_spherical_reconstruction.tex)は、特異係数を含むproperな残余線束圏から固定境界Sへ制限し、右随伴像が生成することを周期から証明する。underlying comonadはId⊕J、J=ρ_S²[−1]であるが、二項・三項の余乗法が残る。[低項パラメータの比較](papers/sections/mixed/central_formal_comparison.tex)は、二項Jac(G)₁=C⁶をBocksteinによるα、三項Jac(G)₀=Cを非零scalar·cへ同定する。係数の多項式性と重み(2,3)、法線符号対合、一変数MFを使う。四項以降の非空fiberは可縮なので、[全中心族の実核](papers/sections/mixed/central_kernel.tex)は全comonadを比較し、coKleisli生成代数のgraphから一つのC[c]線型Morita族を構成する。実比較の後で尺度λ²=28/27を決め、U上で相対perfect核と全coherent比較を得る。全構造の存在は実随伴から得ており、任意の低項データの存在障害が自動消滅するとは仮定しない。任意αの同じ二因子にも普遍比較がある（`cmo:cor:all-alpha-central-kernel`）。特異係数では線束圏を扱い、全coherent圏やperfect対角と同一視しない。

**固定零係数の球面接着による構成。** [中心二重根の比較](papers/sections/mixed/root_order.tex)は、全coherent圏上のtensor/inflationと随伴を構成し、Ku(A₀)^μ₂=⟨ΦKu(Z),ΨK_R⟩ を実perfect核で与える。Zは分離型可換三次四様体であり、接着は球面関手 −⊗_R^L S である。[球面境界類による核の構成](papers/sections/mixed/spherical_boundary_class.tex)の `cmo:thm:fixed-zero-commutative-kernel` は、Bocksteinによる六つの変形パラメータの検出とHeisenberg対称性から球面関手の単位を比較し、全coherenceを持つcomonadのcoKleisli模型からK_R≃Ku(Y)と制限関手のdg自然同型を同時に構成する。YはEckardt接切断の底である滑らかな三次三様体。二成分の核を接着し、Serre関手から内在化した指標χの二乗coherenceを平方根で補正し、二重同変化によって通常のKu(A₀)≃Ku(X₀)を得る。通常の二側商R/(L)は有限次元であり、この商への切断を比較に使ってはいない。

**指定h候補への形式・一般点比較と整核。** [交換子族の実核](papers/sections/mixed/equivariant_deformation.tex)ではh⁶+27≠0上の全次数平坦性、実際の形式MF関手と逆関手を構成する。普遍係数のHeisenberg対称性、二ブロックの積、楕円中心商を用いて、復元potentialを W_h^cand=Σ_i q_i[(x_i³+y_i³+z_i³+h²x_iy_iz_i)/3−u²α^(i)·x^(i)] へ全形式次数で同定し、C(h)の有限拡大上で指定候補への実perfectKu核を得た。[相対模型と核の整延長](papers/sections/mixed/kernel_specialization.tex)は、一般点非PIのまま通常coherent射影積を使い、0,1を含む底上の相対perfect対角とh=1でのperfect整核を構成する（`mix:thm:h-semilocal-smooth`, `mix:thm:h-integral-kernel`）。残るのは、選択した一般点核の整延長をdefect零にし、上の固定点核との互換性を持つ同値族にすること。固定点での同値の存在と、この特定の一般点核の良い特殊化は区別する。

[三対象window](papers/sections/mixed/equivariant_window.tex)の384次元stable Homと対合指標に加え、h族の実相対smooth proper模型から、非可換A₀のHH±₁の正負固有次元も無条件に(5,16)と決定した。これらは補助不変量であり、同値の証明は実核と自然変換の構成による。通常affine twisted HHの中心変数消去は曲率付き比較と区別する。

指定二ブロックの中心族定理は、固定された二つのS(1,−1,−1)因子、中心和の重み1,100、任意の定数補正αと中心係数cを扱う。普遍係数上では残余線束圏の比較であり、可換標的が滑らかな開では相対perfect核・全coherent Ku比較となる。指定α¹=(1,4,9)、α²=(16,25,49)ではsmooth条件をP64(c)≠0と完全に明示できる。Q上への降下、全rotation・指定周期・中心作用の標識を同時に保つ比較、全係数を列挙した最小核は別問題である。原稿の証明・今回の独立読解・計算の確認は [検証範囲](notes/validation.md) に区別して記す。新規性の網羅的調査、外部査読、形式証明器による検証は未完了である。

### 補助的な例：point/Poisson一致への素朴な期待の限界

同じ可換Ku標的X上でPoisson構造πを選び、Pt(𝒳)≃Z_X(π)まで実現できるという期待は一般には成り立たない。これを独立した予想として掲げず、[本文の注意と例](papers/sections/point_poisson_obstruction.tex)（`ppz:rem:naive-expectation`）で説明する。射影埋込みも保つ一致はさらに強い要求であり、一ブロック型にはその障害もある。以下の三様体例と五様体例は、Ku実現と点スキームの幾何を同一視できないことを示す補助例として保持する。

**全スキームとして一致しない三様体の例。** h=1、Sklyanin parameters (1:−3:−2)、点曲線のHesse係数λ=17/9を用いる。実因子の確認 `esi:prop:factor` と中心A2因子の直接比較 `csc:cor:fermat` により、A★=S★[u,v]/(Ω★+(u³+v³)/3)と滑らかな可換三次X★のKu同値をC上で構成した。A★は点スキームの良い条件を満たす滑らかな楕円一ブロック型であり、そのsmoothnessと全coherent Kuは直接比較から得る。同じKuを持つどの滑らかな可換三次上のどのPoisson構造でも全point schemeを実現できない（`ppz:cor:complex-counterexample`）。この反例の構成に形式復元や一般点からのspread、全O stackのchartへの所属は必要ない。この三様体例の自然な対応で被約部分は一致する。

**被約化しても一致しない五様体の例。** 証明の正本は混合稿の [孤立零点と不一致の節](papers/sections/mixed/poisson_limits.tex)。全Poisson正規形から、滑らかな三次n-foldのPoisson零集合に孤立点があるならn=3k、一般階数2kであり、各孤立零点は零次元局所完全交叉であることを証明した（ppz:thm:isolated-zero-dimension）。従って五次元では孤立零点はない。一方、指定混合族の定常ノルムの全64根ではPt(A_c)=E₁⊔E₂⊔{p_c}が被約で、A_cはsmooth properである（ppz:cor:reduced-point-poisson-counterexample）。例えばc=−44828を取れる。これはどの滑らかな可換三次五様体上のどのPoisson構造でも、被約零集合と同型にはならない。不一致の証明には可換Ku比較やTorelliを仮定しない。一方、`cmo:cor:norm-commutative-kernel` は全64根に実Ku標的X_cを与えるので、これらは主予想の存在結論を満たしながら被約point/Poisson一致が失敗する具体例である。正規形はpoisson-cubicの固定された未公表入力であり、一般性やブロックの楕円性は仮定しない。この次元制約の文献上の新規性は未確認である。

### 主要計算の再現

[一般Clifford尺度の検算](computations/verify_clifford_morse_scale.py)は `python3 computations/verify_clifford_morse_scale.py`（**8 PASS、終了コード0**）。adjugate恒等式、臨界値の不変二次moment、非退化な具体例と二つの混合尺度の三乗を厳密に確認する。

[rank-one境界の検算](computations/verify_clifford_rank_one.py)は `python3 computations/verify_clifford_rank_one.py`（**4 PASS、終了コード0**）。正則域のh、中心normのA₂展開、横断Hessianと明示的有理点を検算する。

[固定切片・同変jetの検算](computations/verify_clifford_jets.py)は `python3 computations/verify_clifford_jets.py`（**7 PASS、終了コード0**）。Heisenbergの五つの二次covariant・五つの三次不変式、反転後の四次元部分、gradient関係、最小四probe、全smooth Hesse fiberの補空間、反転と体積線の符号を検算する。旧版の7 PASSは実行確認済みだが、この四probe改訂版全体の再実行は未実施。四probeの評価行列と最小性は別途SymPyで厳密確認した。実核・周期coherence・Azumaya降下・形式切片の存在と一意性は本文の証明に依り、十二係数の数値や組版・保存の成否をこれらの有限計算から結論しない。

[双方向Clifford族の検算](computations/verify_bidirectional_clifford.py)は `python3 computations/verify_bidirectional_clifford.py`（**9 PASS、終了コード0**）。全係数の二次双対の直交・単元小行列式、cocycleとtraceの符号、原点の完全交叉恒等式、中心normの最高係数、非正則な具体点、Heisenberg作用、純因子微分と中心規格化の一次比を厳密に確認する。相対Koszul解消・CY双対性、実核、二十変数の形式完全性は本文の証明による。Python 3とSymPyを使う。

[残余KSのJacobian証明書](computations/verify_interfactor_residual_ks.py)は `python3 computations/verify_interfactor_residual_ks.py`（**7 PASS、終了コード0**）。全Hesse smooth fiberに対する次数三の56単項式・全36関係・20基底、九次元の(1,2)成分、ブロック指標、tensor行列式、τ³=−2のFermat特殊化を厳密確認する。Fermatでは文字通りの可換平方が全て零になることも検出する。実比較核とfull Bocksteinの積の同定は本文の証明であり、この有限計算の結論とは区別する。依存する一般因子Bockstein検算の8 PASSとともに、保持する有限証明書である。今回の再実行範囲は検証資料を参照する。

[因子間PBW検算](computations/verify_interfactor_pbw.py)は `python3 computations/verify_interfactor_pbw.py` と `python3 computations/verify_interfactor_pbw.py --clifford`（それぞれ **6 PASS、終了コード0**）。S(1,−1,−1)二因子とS(1,1,2)二因子について全90一次係数・全15定数係数から条件を組み立て、一次行列の階数78、定数行列の階数9、全12+6残存パラメータのBG恒等式を有理数上で確認する。一般因子の分解定理、中心持上げ、Ku同値の形式証明ではない。

[多中心PBW検算](computations/verify_multicentral_pbw.py)は `python3 computations/verify_multicentral_pbw.py`（**4 PASS**）、[中央pencil検算](computations/verify_multicentral_pencil.py)は `python3 computations/verify_multicentral_pencil.py`（**6 PASS**）で再現する。任意中心形式の平行移動とuv偏極、六変数の次数192判別式の平方因子なし・Hessian・一次jetを厳密計算する。圏の実核と一般性の証明は本文による。

[二重制限の法線検算](computations/verify_two_center_restrictions.py)は `python3 computations/verify_two_center_restrictions.py`（**6 PASS**）。独立な4×4外積・縮約行列から曲率、閉元、混合二項と三項、同軸反例を再現する。実BC・生成性・smoothnessの圏論的証明は本文を参照する。

[一般因子Bocksteinの証明書](computations/verify_elliptic_bockstein.py)は `python3 computations/verify_elliptic_bockstein.py`（**8 PASS**）で再現する。一般左右gauge、Clifford二項検出、全Tate逆冪の双次数を検算し、実cochain移送は本文の証明による。

[楕円中心障害の証明書](computations/verify_elliptic_center_obstruction.py)は `python3 computations/verify_elliptic_center_obstruction.py` で再現する（**7 PASS**）。普遍Clifford体積元の平方・中心行列式、Hesse条件、PBW正規形、Q(τ)上の一次障害と全二次補正の消去、有理τ=2での全低次補正の不整合と二次中心を厳密確認する。非二捩れの一般持上げとKu比較は本文の証明による。

[Heisenberg係数の証明書](computations/verify_mixed_equivariant_coefficients.py)は `python3 computations/verify_mixed_equivariant_coefficients.py` で再現する（**10 PASS**）。関係式・中心元の群作用、同変写像空間の次元1,2,1,2、独立中心文字による全kの異ブロック項排除、重みの復帰を確認する。非可換中心の可換化53/54をχ_kとは同定しない。

[線形Bocksteinと非分裂towerの証明書](computations/verify_mixed_linear_bockstein.py)は `python3 computations/verify_mixed_linear_bockstein.py` で再現する（**6 PASS**）。二次関係から双対積を作り、独立な左右primitiveのgauge行列のrank6、対称対角外3方向との補行列式−64、Tate逆冪を許す双次数条件を確認する。全k≥2・全arity・全higher homotopyについて、隣接群も含めたsector消滅を非負変数の多項式不等式で検算する。実Bocksteinのfull cochainへの同定と比較核の全coherenceは本文の証明に依存する。

[多ブロックの有限証明書](computations/verify_mixed_multiblock.py)は普遍8×8乗法行列、平方自由基底、Euler恒等式、臨界値の二次moment、tensor spectrum、非被約な零係数、全kのsector不等式、および一般節点性の種となる八臨界点・八臨界値を確認する（**9 PASS**）。中心Morse多項式と可換臨界多項式のλ²=28/27での一致も検算する。[線形PBWの普遍証明書](computations/verify_mixed_linear_pbw.py)はPBW重なり、普遍中心の三交換子、低次数中心の消滅、平行移動則、三方向の独立性、既存中心元への特殊化を確認する（**6 PASS**）。それぞれ `python3 computations/verify_mixed_multiblock.py`、`python3 computations/verify_mixed_linear_pbw.py` で再現する。全次数PBWはBraverman–Gaitsgoryの定理と本文の条件確認によるもので、有限Hilbert関数からの外挿ではない。比較核の全coherenceは本文で証明し、これらの有限検算を形式証明器での確認とは扱わない。

[中心係数方向の有限証明書](computations/verify_mixed_central_direction.py)はPython 3とSymPyで、Knörrer座標と法線二次式のhomotopy、Jacobian類の非零小行列式、P64根の非零二次moment、中央三次MFのMassey係数、重み三の単項式を厳密検算する（**7 PASS**）。`python3 computations/verify_mixed_central_direction.py` で再現できる。全comonadのcoherenceと実比較核の同値性は本文の証明によるもので、この有限計算を形式証明とは扱わない。

[形式比較の有限恒等式](computations/verify_mixed_formal_kernel.py)はPython 3とSymPyで、普遍PBW重なり、一次bar homotopy、二次eye補正、Jacobian classの非消滅、普遍不変空間とHesse jの局所逆を再現する（**9 PASS**）。`python3 computations/verify_mixed_formal_kernel.py` で実行する。全形式次数の同値と一般点核の降下は本文の証明による。固定h=1の同値は球面境界類から別に構成しており、この形式核の特殊化との互換性は未証明。

[不変環の非斉次Koszul双対](computations/verify_mixed_invariant_pbw_dual.py)は元の関係式から双対積を作り、128次元dg代数、微分のrank24、cohomology次元80と双次数を検算する（**5 PASS**）。`python3 computations/verify_mixed_invariant_pbw_dual.py` で実行する。この計算は曲率を加える前の有限dg双対を扱い、以下の実MF構成の入力となる。

[実曲率と有限MFの縮約](computations/verify_mixed_curved_dual.py)は実際の w=Ω₁+100Ω₂ を保つrank64+64のMFを構成し、有限摂動でrank40+40へ縮約する。二乗w、両向きの写像、合成のhomotopyまで有理係数で検査する（**12 PASS**）。`python3 computations/verify_mixed_curved_dual.py` で再現でき、`--export <出力先.json>` で全係数を再生成できる。生成性とK_Rのdg End模型は [有限曲率模型](papers/sections/mixed/curved_invariant_model.tex) の `cmo:thm:finite-curved-invariant-model`, `cmo:cor:curved-invariant-end-model` に証明を置く。rank80は自由MFの大きさであり、End A∞代数やHHの次元ではない。

[三対象windowの同変指標検算](computations/verify_mixed_window_involution.py)はPython標準ライブラリの整数演算だけで、Koszul指標、全13行のstable Hom表、384次元の集約表、通常・対合付き・不変部分のEuler行列を再現する。七線束のHilbert多項式と四例外対象の射影から通常Euler形式を別に計算し、windowの基底変換とも照合する。`python3 computations/verify_mixed_window_involution.py` で実行し、HHの値はこの検算対象に含めない。

[普遍六次中心元の厳密検算](computations/verify_mixed_pi_center.py)は、独立な三パラメータを保ったQQ上で、全交換子の関係イデアルへの所属と中心最高部の独立性（小行列式−4/9）を確認する。全次数の中心生成にはSmith–Tateの定理を別に用いる。

[中心の関係式と特異ファイバー](computations/verify_mixed_center_geometry.py)は、次数18までの正確な商計算、二つの21項中心関係、Gröbner消去、全28節点の横断Hessianの非退化、64次終結式の平方因子・normとの最大公約数を再現する。[二次元表現の恒等式](computations/verify_mixed_two_dimensional.py)と[高次作用の検算](computations/verify_mixed_two_dimensional_ext.py)も厳密演算で実行できる。後者の `--universal` は二変数有理関数体で普遍式を検証するため、既定の二つの数体例より時間を要する。`--zero-example` は三次数体上のκ₂=0と、全characterのκ₁≠0・指定中心値にcharacterがないことを検査する。 中心検証器の全14 PASSを確認した。

[可換候補と共通判別式の厳密検算](computations/verify_mixed_commutative_candidate.py)は、QQ上のJacobi環の次元8、Hessianの可逆性、λ²=28/27での特性多項式の一致、独立な終結式と既存P64の全係数一致、normとの互いに素性、c=−44828の唯一のcharacterを確認する。**9 PASS**を二名が独立に実行した。孤立Poisson零点定理やKu同値の機械検証ではない。

[比較不変量の厳密検算](computations/verify_mixed_comparison_invariants.py)は、指定有理係数のJacobian関係行列をQQ上で作り、次数二・三の対合固有次元、residueの符号、同変HHの算術、有理Euler行列を確認する（**9 PASS**）。必要環境はPython 3とSymPy。全領域の相対smoothness、Mathewの適用、根スタック圏模型、非可換MFの完備化比較は本文の証明であり、この有限計算による形式証明ではない。

[characterの自己Extの厳密検算](computations/verify_mixed_character_ext.py)は、普遍higher homotopy、κ公式、既存64点、有理係数のκ=0例を確認する。射影次元は本文のRees・周期性の証明と合わせて結論し、有限次数のrank計算から外挿しない。

[点・零スキームの厳密検算](computations/verify_point_poisson_obstruction.py) は12 PASSを確認した。有限語関係による中心性、Hessian・j不変量、64個の例外値の検算と、全次数PBW・圏同値の証明は区別する。独立読解・組版・表示確認・保存の状態は [検証範囲](notes/validation.md)を参照する。

## 可換復元・モジュライの内容

完備MF移送と一般点の全coherent残余圏のKu比較の証明は主稿 `papers/nc-cubic.tex`、構造対象付きモジュライと精密降下は `papers/cubic-moduli-descent.tex`、混合族の具体的な代数と幾何は `papers/mixed-sklyanin-cubics.tex` に置く。一般の中心三次変形の基礎定理は、一ブロック型のモジュライ構成とは独立した仮定の下で述べる。外部の未公表入力は `poisson-cubic` の古典Poisson論文と、`nc-cubic-threefold` の三様体固有の指定版である。三様体固有の全Abel圏形式近傍と相対射はそのrepoに保持し、全次元の復元・Poisson射・点型算術は本repoを正本とする。量子化の全証明は別repo `cubic-quantization` に置く。

- [可換復元の基礎節](papers/sections/generic_recovery/main_result.tex)：完備MF比較 `cft:thm:complete`、一般点の可換復元 `gdr:thm:generic`、局所模型・window・飽和・低積の積分・明示Hesse模型を含む全9節。主原稿から読み込む。
- [可換復元の研究上の障害と再現入口](notes/recovery_foundations.md)：定義体、有限降下、symmetrizer、具体例の規約、残るkernel有効化。
- [可換復元の検証スクリプト](computations/verify_generic_cubic_descent.py)：既知の勾配空間の積分と非分裂symmetrizer。`verify_complete_curved_transport.py`、`verify_three_object_window.py`、`verify_recovery_example.py` も同じ `computations/` に置く。
- [中心変数を持つ分離和の直接Ku比較](papers/sections/central_split_comparison.tex)：孤立中心三次のMF因子、明示A2模型、有限外積と周期付き補正、全coherent Kuの可換実現。`csc:thm:comparison`、`csc:cor:fermat`。
- [分離型の点関手と零スキーム](papers/sections/central_split_points.tex)：任意試験環の点グラフ、中心定常成分、スキーム論的像とFittingイデアル、長さ8^kの局所Artin環、同じ標的でのm=1の一致。`csp:thm:point-functor`、`csp:thm:poisson-zero`。
- [具体的な複素Sklyanin因子](papers/sections/explicit_sklyanin_input.tex)：parameters (1:−3:−2)、点曲線E_{17/9}、指定中心元Ω★の規格化、中心商、AS正則な周囲環を一次資料と直接計算で確認する。`esi:prop:factor`。
- [混合Sklyanin三次稿](papers/mixed-sklyanin-cubics.tex)：有限norm、中心一関係・PI6・Azumaya性、全14節点のNCCR局所形と全simple分類、全Ω節点切断、非smooth集合V(P64)の完全決定とc=0・norm全根のsmoothness、2次元普遍高次作用、100simpleのpd5、64点の残余Ext、余有限可換Ku実現。`cmo:thm:fourteen-node-orders`、`cmo:thm:exact-sixty-four`、`cmo:cor:fixed-zero-norm-smooth`、`cmo:cor:cofinite`。
- [点・Poisson比較の有限証明書](computations/verify_point_poisson_obstruction.py)：Hessian小行列・制限三次・j不変量、固定中心元と混合中心元の語関係、有限定常環の正則表現と64根の厳密検算。全幾何学的議論や圏同値の代用ではない。


- [モジュライ・降下稿](papers/cubic-moduli-descent.tex)：中心復元、局所一ブロック型の O-marked DM stack と Brauer 障害、相対点関手と中心商の復元、trace–Hessian による Poisson 対の開部分との同型、残余復元との比較障害、次数9の代数的 Poisson 補正、形式 support 保存、全混合五次 tensor と残余四次 potential、四次の比較障害と新しい代数的補正、split 族の残余比較、一般混合係数の代数的残余三次・点曲線の j の一致・点微分による一般有限な符号商 Poisson 射、有限被覆上の Ku 比較、点型の全 O-降下と scalar 障害、n=3,4 の全 full class 降下と最小比較次数三、三分点体の次数九と ASL₂(F₃) モノドロミー、固定 tensor の very general な超越性、Jacobi スキーム。
- [残余圏の通常Artin形式認識](papers/sections/residual_categories.tex)と[可換実現locusの開性・DVR核判定](papers/sections/geometric_realization_locus.tex)は主稿に置く。
- [研究ノート](notes/research_notes.md)：主張の依存・適用範囲、反例・障害、文献の確認箇所、次の計算の入口。
- [検証範囲](notes/validation.md)：原稿点検・組版・厳密計算を区別した確認状態。
- [量子化の検証状態](https://github.com/uedakazushi/cubic-quantization/blob/main/validation_quantization.json) と [再現入口](https://github.com/uedakazushi/cubic-quantization/blob/main/computations/quantization/README.md)：中心元・多ブロック計算と独立量子化稿の確認範囲。
- [相対構成の補助ノート](notes/relative_construction_obstacles.tex)、[中心二チャートの補助ノート](notes/central_cubic_generic_smoothness.tex)、[未照合の外部資料](notes/unresolved_external_sources.md)：本文へ無条件に取り込まない技術的障害・残る照合範囲。中心二チャートの非可換Bertiniでは、chart代数が有限生成可換中心上有限という追加仮定を明示する。
- [Jacobi 行列検証コード](computations/verify_jacobi_rank.py) と [整数小行列証明書](computations/jacobi_rank_certificate.json)。
- [八次元の頂点構造の検証コード](computations/verify_jacobi_vertex.py)、[C++ 検証器](computations/verify_binary_minor.cpp)、[次数三の全射性の証明書](computations/jacobi_vertex_certificate.json)。
- [中心評価・Hessian・trace の厳密検算](computations/verify_center_hessian.py)。
- [幾何補正・残余比較の厳密検算](computations/verify_geometric_corrections.py)：全次元の Jacobi 双対証明書、trace、普遍二次テンソル、Hesse 不変量。
- [active 不変量の厳密検算](computations/verify_active_invariants.py)：二つの不変量上の補正式、Hesse 可換式、判別式と Jacobian の恒等式。
- [active 符号判定の有限恒等式](computations/verify_active_sign.py)：Hesse群の24要素、二次指標と不変量、体次数の消去式。有限対角による延長と降下は本文の証明による。
- [Poisson 補正の厳密検算](computations/verify_poisson_correction.py)：一般三変数三次の点曲線、二パラメータ Hesse 公式、中心係数、尺度の変換、一般混合係数の線型復元行列、framed 被覆の分岐。
- [三次共変式の厳密検算](computations/verify_cubic_covariants.py)：Weyl 重複度、四次不変式の規格化、五次混合項の二定数への還元。
- [混合五次 tensor の厳密検算](computations/verify_mixed_fifth.py) と [必要な73項の harmonic graph データ・出典・hash](computations/data/harmonic_linear_products.json)：二つの普遍定数の評価と原 weight の規約照合。
- [残余四次項の厳密検算](computations/verify_fourth_potential.py)：古典的 Hessian・Aronhold 微分との恒等式、中心 symbol、純中心項、尺度、全次元の Jacobi 双対証明書。
- [残余射・尺度・比較核の本文](papers/sections/residual_algebraic.tex)：一般次元の相対復元、全 O-降下、有限被覆上の Ku 比較、完備中心商、最高次 cohomology と階数三束によるscalar index、従来のEuler格子、固定tensorの超越性。
- [点曲線と自然な残余尺度の本文](papers/sections/residual_point_scale.tex)：active 部分の全次数比較、Hodge 線束、点曲線の同型被覆、符号商射、反対代数、正確な一般次数18、混合三角性・符号消滅・半古典full射の次数9、一般係数体上の平面同型torsorの分裂、指定半古典平面同型の全O降下。
- [四次補正の本文](papers/sections/fourth_correction.tex)：上の有限計算を一般次元の証明と Poisson moduli の射へ統合する、モジュライ・降下稿の本文。
- [点の平行移動と核のPicard類](papers/sections/residual_kernel_point.tex)：右加群の rotation 共役、相対 THCR/window1、非空で内在的な点型、active 同値の全分類、点側・残余側の exact index 三、非分裂 period、三分点体の ASL₂(F₃) モノドロミー、n=3,4 の全 full class 降下・周期位相の class 不変性・相対尺度による最小次数三／九、三乗倍までの方程式規格化と γ_sc の形式像、高次元の T-軌道降下・奇数次元の数値中央化群、随伴復元点型の有限 class torsor・全次元の正準強化 class・全奇数次元の有限な数値自明安定化群、七次元の球面 twist による障害。
- [周期位相の混合定数降下](papers/sections/residual_period_descent.tex)：κ(m) 上の周期付き full Morita 比較、γ_sc,n の C(c₄,−c₆) への一意な降下、他の分岐を排除できた場合の大域式 [D]。
- [Hesse 境界の残余模型](papers/sections/residual_boundary.tex)：三分点被覆、点線束の有理相対行列、指定周期を保つ積分模型、右射影と有限 MF。
- [境界の低積と周期位相](papers/sections/residual_boundary_products.tex)：全 n の窓・orbit Hom の自由性、低積の一次項と二次関係の飽和、smooth potential 三次による格子比較、完備局所 γ_sc,n=[D_R]。
- [境界の低積の厳密検算](computations/verify_boundary_low_products.py)：QQ(p) 上の有限 Hom 行列、cocycle の一次持上げ、二次積の homotopy、三次 class の非零証人を再生成する。
- [非分裂点 Picard 障害](papers/sections/residual_unsplit_picard.tex)：period 三・index 九の曲線、n≡1 mod3 の全非空開での実現、普遍重み一束の最小階数九、非分裂 rotation の gerbe、低次元の全型の最小次数一／三と四次元の強化点型九・全型三。
- [Tate–Koszul 復元](papers/sections/residual_tate_reconstruction.tex)：原点・内部 shift を保つ核の忠実性、全 n の一般族の強化点型 class 唯一性と最小実現次数三。
- [五次元 Clifford 半 rotation](papers/sections/residual_fivefold.tex)：平面上の相対核と平面非依存性、奇数次数零 cycle による実核降下、原点像の二 mutation への還元。
- [Fano 曲面の次数の厳密検算](computations/verify_fivefold_plane_degree.py)：Grassmann 積分の整数係数計算による次数2835の再現。
- [点障害の厳密検算](computations/verify_picard_obstruction.py)：Hesse 接線・巡回 norm、Sklyanin 点三次・係数の逆、rotation の六つの数値 centralizer、巡回平面 twist・norm 係数・symbol 補正、普遍 Jacobian の三捩れ点・八点軌道・安定化群 core、右点対応。
- [参考文献](papers/references.tex)。外部文献PDFは含めない。

外部の古典入力は [poisson-cubicの論文](https://github.com/uedakazushi/poisson-cubic/blob/main/papers/poisson-cubic.tex) のPoisson正規形であり、代数的量子化の入力は別repoの [cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) である。一般点復元の証明は現行主稿の `papers/sections/generic_recovery/` に保持する。本文の配置変更と数学的な検証範囲は区別する。

## 満支持複数ブロック型の到達点と次の目標

**全 `k≥2,m=0` の満支持楕円型で、全O自己同値群を `K_k=(H_27^k)/Δμ_3` と決定した。位数は `3^(3k−1)`、二ブロックでは正確に243である。** `B=⊗S_i`, `A=B/(Σa_iΩ_i)`、全中心係数非零、`p_i,2p_i,3p_i≠0`、相異なる`j_i≠0,1728`を基本とする。全O同値の認識にはさらに`jp_i≠0 (1≤j≤3k−3)`を課す。無限位数や全自己同値群の有限性を事前には仮定しない。

- [中心商・余法加群](papers/sections/multiblock_intrinsic_quotients.tex)から各`(E_i,L_i,σ_i)`を回復し、[飽和冪による全自己同型の認識](papers/sections/multiblock_center_automorphisms.tex)で中心商の全多重次数を復元する。`Aut_gr(D)=(∏Aut_gr(T_i))/Δμ_3`を得る。
- [中心方向の持上げ剛性](papers/sections/multiblock_central_rigidity.tex)は負次数Hom・Ext消滅と正次数の安定性を使う。中心還元核は全`k≥2`で自明。次数一軌道の復元を[SSS認識](papers/sections/multiblock_veronese_automorphisms.tex)へ接続して全群K_kを得る。
- [相対認識](papers/sections/multiblock_relative_recognition.tex)により、適切な非空開で表示stackと全O局所型stackが同型になる。この開では、任意の非被約底を含む族に対して`Eq_O=Isom_gr(A,A')/G_m`。全慣性の中心は順序付き被覆上で`(μ_3^k)/Δμ_3`、順序を忘れる際は因子置換で降下する。
- [一般の全O局所型モジュライ](papers/sections/multiblock_generic_moduli.tex)は滑らか・既約・DM・次元`2k`。[相対双対](papers/sections/multiblock_serre.tex)と[第三Veronese認識](papers/sections/multiblock_veronese.tex)を基礎に、支配的可換特殊化と関係Grassmann像の独立な構成を保持する。二ブロックの第三Veroneseは55生成元・2619二次関係。
- `s=(1)`に対し`rO≃O(1)`を満たす根は一意に`r=sΦ_h`と書け、二ブロックでは243個の自然同型類・83共役類となる。一般の共役類数は`(11^k+2·8^k)/3`。この分類に`6p_i≠0`は不要だが、[代数的Zhang twist表示の直接分類](papers/sections/multiblock_roots.tex)ではこの追加条件を使う。三乗同型・coherenceの標識や、Oの像を指定しない全根の分類は含めない。
- [同変一般点復元](papers/sections/multiblock_equivariant_descent.tex)と[点曲線による模型](papers/sections/multiblock_point_comparison.tex)では、明示的Jacobian tensor/PBW族と既存cft/gdrの下で `J_i=g_i+ε_i² det Hess(g_i)/24` の分離和を復元する。[全kの積表示](papers/sections/multiblock_residual_descent.tex)により、有限拡大後に `(K_A^coh)^(Z_0)≃Db(∏E_i)`。可換側のBFK・Orlov公式とElaginの双対作用は既知の入力として扱う。
- [表示gerbeと残余構造](papers/sections/multiblock_scalar_descent.tex)：表示類βは各非空開で正確に位数3。compact残余圏・mutation projectorは全O開へ降下し、例外成分は `Perf(P_k,−jβ)`。rotationは重み1で、MF/window比較の範囲では `ρ³⊗ℓ^∨≃[2]` が降下する指定周期となる。
- [中心群のcoherent作用](papers/sections/multiblock_central_action.tex)：作用と同変化は基準に依存しない。線型的持上げの選択は `Σa_i=1` というF3上のtorsorで、rotation比較にはcharacter twistが生じる。置換不変な選択は `3∤k` のときに限り存在する。この障害と表示gerbeを区別する。
- [比較核のstackと双対作用](papers/sections/multiblock_residual_descent.tex)：両側のsmooth proper族を固定すると同変核stackはfpqc降下する。一般点の実dg模型が有限拡大上にあり、幾何学的一般点で非空なら縮小後有限étale被覆上に実核が存在する。可換Kuは曲線積の導来圏の双対群同変化となり、その作用は因子rotationの比で記述される。`3∤k` の対称rotationも明示し、二因子では `(R_1R_2)^−1[2]` となる。全基本固定点の比較と実表示上の相対核は下記の直接構成で扱い、全O上の大域核sectionは別課題として残す。
- [因子モジュライと点曲線積](papers/sections/multiblock_factor_moduli.tex)：`P_k//Z_0≃B_k` と、平面三次の組への滑らかな相対次元kの射を構成する。点曲線積のsmooth projective族は全O開へ降下する。
- [中心線から点三次線への自然な比較](papers/sections/multiblock_point_line.tex)：最大可換商の比較を相対Hesse被覆で全基本楕円開へ延長する。自然な可換三次族 `Φ_pt` と表示gerbe・関係直線の同期は任意底変更に対応する。2p=0境界の零点による延長障害も記載した。
- [相対曲線積の実核](papers/sections/multiblock_relative_product.tex)：滑らかな準射影C基底、共通係数直線 `L` に値を取る滑らかな三次の分離和について、相対Orlovと実dg外積から `Perf(∏E_i)≃Ku_Perf(X/S)^(Z_0)` を構成する。実perfect核・逆核の導来引戻しによって準コンパクト・分離的noetherian底（非平坦・非被約も許す）にも両立し、因子置換もcoherent。有限生成C体上の可換積比較には追加拡大が不要で、med/mpcの既存有限比較体のまま曲線積へ進める。非正則底ではPerfの主張であり、全Db(coh)との一致は主張しない。
- [比較核と周期の同期](papers/sections/multiblock_kernel_synchronization.tex)：局所rotation比較とscalar-simple/負Ext/底変更の仮定の下で、固定核型のgerbe類αと固定同期の周期torsor類γの両消滅が大域実現条件となる。period標識後も核のAutはG_m。自然な非可換族のPicard補正型は下記の相対Picard節で具体化し、全核型の分類とは区別する。
- [非可換側の直接積表示](papers/sections/multiblock_noncommutative_product.tex)：体上の全基本実表示に対し `Ku_coh(A)^(Z_0)≃Perf(∏E_i)`。全kのtensor-noetherian性、有限Koszul–Shamash外積、window、smoothnessと全coherent飽和を証明する。一変数変形を仮定しない。
- [相対非可換積の実核](papers/sections/multiblock_relative_noncommutative.tex)：滑らかな準射影C基底の順序付き実表示で、`Ku_compact(A/S)^(Z_0)≃Perf(∏_S E_i)` を実perfect Morita核と逆核として構成する。相対tensor-noetherian性、有限Koszul–Shamash外積、window、perfect Homと生成性を証明し、共通関係直線・指定周期・因子rotation・coherent中心作用を保つ。compact圏はsmooth properであり、任意の準コンパクト・分離的noetherian底変更（非平坦・非被約を含む）に両立する。元の滑らかなaffine底では全coherent飽和も証明した。非正則底の全Db(coh)への同定は含めない。一因子の正則底windowは最高次Koszul syzygy直線を保持し、非零二捩れ点の境界模型にも適用する。
- [Picard補正と固定点の有限比較](papers/sections/multiblock_rotation_comparison.tex)：因子rotationを点の実線束で共役し周期差を三乗根で補正する。順序付き実表示は次数高々 `3^(2k)` の有限拡大後に自然標的の通常Kuと中心作用・rotation・指定周期付きで比較できる。代数閉体上は全基本点で拡大不要。rotationを標識せず中心作用を保つ比較では、下記の相対Picard分類により上界を `3^(2k−1)` に改良した。これらの全上界の最小性は未証明。
- [Picard補正型の相対降下](papers/sections/multiblock_picard_descent.tex)：積のPicard gerbe `G_Pic` の類は `α_Pic=Σδ_Ei(p_i)`。各因子の指定周期torsorを `T_i` とし、`T=∏T_i`、`D=T/Δμ_3` と置くと、中心作用を保つPicard型の核stackは `G_Pic×D`、さらにrotation・指定周期を保つものは `G_Pic×T` となる。個々のPicard障害が非零でも和は消え得る。核のAutはperiod標識後もG_mであり、このscalar gerbeは全ての比較核を分類するものではない。
- [自然な周期の全係数](papers/sections/multiblock_hesse_phase.tex)：比較直線はHodge線λであり、自然な同期では `q(ω³)=−1/v_ω(p)`、`γ=[v_ω(p)]`。`v_ω=2y+a₁x+a₃` はJacobianの奇Weierstrass座標で、`v_ω(p)ω³∈λ³` は内在的である。Hesseの全九flexで中心を正則化し、原点で周期の定数を校正する。全基本開と許された任意底変更に成立し、一ブロック残余位相の未解決大域式とは区別する。
- [全中心同変核・同種因子・正規化群](papers/sections/multiblock_full_comparison.tex)：`k≥3` では同種性・CMによらず全H作用が因子を分離し、`k=2` で幾何学的非同種の場合と共通に全型を分類する。scalar障害は `α=Σδ_i`、通常比較の位相は `γ_i+ν_i(φ_i)` の一致、rotation・周期付きは全ての消滅で判定。固定Hesse独立族では最小 `3^(k−1)`／`3^k`。三因子以上のH-normalizerの像は偏極因子置換だけで、共通反転は三次周期に反する。二つの同種因子にはPell方程式から外積でない無限位数のcoherent中央化核を作り、次数二isogenyではH反転も実現する。混合型の一般K上の実現gerbe・位相は未分類。
- [通常Kuにおける中心μ3の非正規性](papers/sections/multiblock_unmarked.tex)：滑らかな二ブロック分離和三次四様体のflex接線から三平面を作り、そのイデアル層がKu内で球面対象となることを証明する。数値格子のGram行列（対角−2・非対角2、行列式32）から、球面捻りが中心を逆元まで含めても保たず、二つの捻りの積が無限個の相異なる共役部分群を与える。全基本二ブロック非可換幾何点にも移る。これは同じ共役軌道内の無限性であり、無標識比較の最小次数の低下を結論しない。
- [比較核の全O降下](papers/sections/multiblock_intrinsic_comparison.tex)：次数ごとのscalarと中心慣性の比較から、相対積核が射影表示Pと中心rigidification Bへ降下し、B上で非捩れ `Perf(∏E_i)` を得る。Picard型核stackと相対rotation・周期比較もBから来て、既存の全O認識開と因子置換に両立する。個々のrotationの非捩れ降下、表示gerbeの中立化、通常比較核の大域切断とは区別する。
- [周期公式の厳密検算](computations/verify_multiblock_hesse_phase.py)：中心の除算certificate、Hesseの原点jet、微分付きWeierstrass式、Hesse自己同型の方程式保存、非零multiplier例をSymPyの有理式で確認する。圏同値・降下・最小次数の証明は本文による。
- [同種因子と三平面格子の厳密検算](computations/verify_multiblock_isogenous.py)：Orlov行列、整数annihilator、Pell混合isometry、二次同種のH反転、Gram行列・反射・無限共役軌道の冪公式を七組の厳密計算で確認する。球面性、核の存在、coherenceは本文の証明に依存する。
- [中心・点線比較の厳密計算](computations/verify_multiblock_point_line.py)：QQ(t)上のFermat次数四関係行列に加え、Hesse点行列式と `ab(Ω_H)−3(a−b)F_H=(a−b)³Σx_i r_i^ab` を多項式恒等式として検算する。一般Hesse中心性・PBW・圏同値の機械証明ではない。
- [有限群の指標・表現検算](computations/verify_veronese_representation.py)と[共役類検算](computations/verify_multiblock_twists.py)を保持する。55次元表現の中心固有空間19・18・18、ambient線型normalizerの計算と、今回の紙上の全代数自己同型群の証明を区別する。

基礎となる[点対応](papers/sections/two_block_points.tex)、[中心と自己同型](papers/sections/two_block_algebra.tex)、[表示stack](papers/sections/multiblock_presentations.tex)、[完備比較](papers/sections/two_block_recovery.tex)も保持する。任意の抽象圏変形や全境界を覆う主張ではない。表示gerbeとSerreの基底直線も保持する。

**現在のP0**は、固定Hesse切片に残る十二係数の最初の非零値の実計算、比較核のKummer三枝の選択・降下、AS-regular域内部も含む残余smooth locusの境界と核延長である。九・十八方向のKS、二十変数の形式完全性・モジュライの稠密開と一般係数の有限étale比較、一般尺度の三乗は証明済みの入力として用いる。全比較核のgerbeと尺度torsorの同定、全smooth係数の比較、全intrinsic対象の認識・表示被覆は未完成である。固定tensor境界の全PBW表示は因子別に分解し、その全smooth中心三次商には中央flagと可換Ku実現がある。偏極標的X_polへの実核については、chart核の重なりでの自己同値・周期位相とČech coherenceを調べる。二軸の同定だけでは混合情報が消えるため、実BC・joint comonadを入力とする。因子moduli上のPicard補正、横断係数の具体化、選択済みh一般点核のdefect零特殊化も保持する。具体的な着手は[研究方針](00_research_plan.md)を参照する。

一般次元のO-marked moduli、point scheme、Poisson対への射、比較核は、可換Ku実現の構成と対象範囲の認識に役立つ限りで優先する。各成分の一般点での結果、全固定点での結果、全族の構成を区別し、一般点の結果だけで最終目標を達成したとはしない。

良い一ブロック型で、O-marked 圏 stack と分解可能な Poisson 対の非空開の同型を構成した。一方、固定入力の残余復元の下で **trace–Hessian 射の X_TH と X_res が異なる全次元の Hesse 族**があり、固定した周囲 tensor の純中心補正では修復できない。二次 jet の障害を除く代数的 Hessian–trace 補正 Φ は、全 O-降下・適切な開上での有限 étale 階数9・楕円点曲線との厳密な一致を持つ。split 族では、この補正後三次と残余圏の全次数比較を固定入力の下で得ている。

一般混合係数についても五次 tensor と残余四次 potential を決定した。その結果、従来の Φ と残余三次の marked な比較は、各 n≥3 の非空 Zariski 開で四次に妨げられる。新たな座標不変の代数的射 Φ^[4] は全 O-同値へ降下し、残余三次に mod h⁶、tensor に mod h⁷ で一致する。Φ の次数9・点曲線との厳密な一致・split 族の全次数同値を、Φ^[4] の性質とはしていない。一般混合係数の代数的な残余三次と射影 Poisson 射については、次の結果を得た。

**固定入力Bの下で、残余射 Ψ_res を良い一ブロック成分の稠密開上に構成した。** 低 rotation 積の核 Q と、その積分核 L=ker(Sym³V_ρ→V_ρ⊗(Sym²V_ρ/Q)) から三次の方程式直線を取り出す。中心一次作用 c:U→V_ρ の annihilator K_res と合わせると、Brauer–Severi ambient を許す射影 Poisson moduli への射となり、全 O-同値と任意底変更に両立する。射は支配的で、適切な開では相対次元1の滑らかな射である。有限 étale 被覆上で、この **同じ X_res の Ku** への比較核を得る。完備 MF・正則底の window・一般点生成性・coherent 飽和性の未公表入力を明示した条件付き結果であり、全 intrinsic 成分を覆う主張ではない。

選んだ相対 graph flow は中心一次作用を厳密に保ち、Ψ_res の一般形式像は (V(W_h),[π_h]) に全次数で一致する。一変数族では、完成上の格子を降ろすことにより h=0 に滑らかな三次模型も得るが、形式比較の選択に依存し得る。

**固定 h・固定生成元の実際の tensor π_h は、全 n≥3 の very general な滑らかな係数で代数的でない。** xyz での厳密な対数級数と普遍再帰の多項式性から、各有界次数の代数関係 locus が真の閉集合となることを証明した。単一の Zariski 開の全点での主張ではなく、有限 jet の外挿でもない。任意の形式 frame を許した intrinsic な尺度付き射の不存在は結論しない。

**全 n≥3 で、残余 active 曲線と楕円点曲線の j が一致することを証明した。** 正規化再帰の active 制限と Hesse 族からの普遍化により、形式 frame では W_h|_K=b_h(g+h²Hess(g)/24) が全次数で成り立つ。j≠0,1728 の開で、平面同型の層 I は有限 étale 階数18、Jacobian の群同型の層 D は階数2であり、I→D は3捩れの階数9の torsor となる。

**点曲線の標準微分が自然な残余 Poisson 射を与える。** 相対随伴から T=L⊗det K_res≃λ_res* を同定する。点曲線の尺度 τ_pt=(H♯|K)⊗P と modular forms から T² の非零切断 η_res を得て、Ψ_res^±:M→[Pdec/μ₂] を構成した。これは全 O-同値・任意底変更に両立し、支配的・一般有限、縮小後には有限 étale 全射である。標準二重被覆 D 上に full tensor があり、点 shift も残余 active 曲線の平行移動へ移せる。同じ X_res への Ku 比較はさらに有限被覆上で保たれる。半古典先頭項で元のM上の符号を規格化できる。移送shiftをfull Ku rotation自体と同一視することや、比較核の降下は別に残る。

**この残余射の一般次数は、全 n≥3 で正確に18である。** 反対代数の自由な involution ιと active 不変量の九次中間被覆 Z により、適切な開で M→M/⟨ι⟩≃Z→Y と有限 étale に因子化し、階数は2,1,9となる。全次数残余 potential は混合係数について三角形の多項式写像となり、その対角が可逆である。これと共通の Hesse 安定化群の指数二を用いて追加分枝を排除した。形式近傍の逆だけから次数を結論していない。一般の A と A^op は O-marked 圏として異なるが、同じ X_res と共通被覆上で同値な残余圏を持つ。

**符号類χ_actの消滅を証明し、一般次数九のfull残余Poisson射を得た。** 符号二重被覆Dの一般点の類はactive不変量体L₀=C(c₄,−c₆)から来る。全次数で混合重みが有界なため、形式残余potentialはκ=C(p,q)((h))上の混合係数の実際の多項式となる。この表示はC₃対称点でも滑らかである。Poisson符号商標的の有限対角を用い、一般点で指定した同型をsmoothな有限係数模型とその二重・三重積上へ延長して、対称点を通る残余射の近傍延長を降下した。延長された曲線の有理三捩れ点がJacobianの二次twistを排除し、Hesse体への二次類の単射性からχ_act=0を得る。半古典先頭項で二つの符号の一方を選ぶと、全O-同値に自然なΨ_res^scが定まり、適切な開で有限étale階数9、Ψ_res^sc∘ι=−Ψ_res^scとなる。χ_op=χ_sgnであり、符号商射の次数18も保持する。

点規格化した tensor は形式 frame で (h/c_h)π_h であり、固定 harmonic tensor と同じ尺度ではない。自然な射の代数性は上の very general な固定 tensor の超越性と両立する。二重被覆は Jacobian 同型を持つが、genus-one torsor 自体や次数三偏極の同型には I→D を用いる。

この符号消滅は既存の固定入力の下での結果であり、別の近傍延長仮定を要しない。構成したものは一般点のPoisson対の代数的延長である。その特殊ファイバーを圏の低rotation積から底変更と両立して再構成できることや、比較核がそこへ延びることは未証明だが、符号消滅の証明には不要である。Dの分裂だけではgenus-one torsor自体の同型やfull比較核の降下は従わない。一般 split 係数体上の平面同型は、下記の H_g による別の証明で得る。点規格化tensorは形式frameで(h/c_h)π_hであり、固定harmonic tensorの超越性と両立する。

**比較核の scalar index には、次元によらない三捩れ評価を得た。** split表示でκ_ncとactive係数商・window1のq_Yを固定し、R_P=q_YΦ_P(κ_nc)がH^{>−1}=0、H^{−1}が次数零線束となる型を構成する。この型の核は一般点の有限分離拡大上に存在する。同型類を整合的に選んだ後のgerbe上では、最高次cohomologyから重み一階数三束を作れ、そのendomorphismは次数三Azumayaへ降下する。従って3α=0、ind(α)|3。表示分裂後にこの型となる仮定の下で、非分裂表示を含む体上ではn≢1 mod3でind(α)|3、n≡1 mod3でind(α)|9となる。

上のsplit表示と固定したq_Yの下で、最高次線束の相対Picard類m_Pを使うと、scalar gerbeはPicard gerbeの引戻しと正確に同定できる。m_P=0なら障害は消える。またactive曲線C上に実際のfull比較核があり、一般直線の三点切断は具体的な有限étale scalar分裂被覆になる。これも核の同型類を選択した後の結果である。


**選択済み核には、Picard 三分点による標準的な相対分裂を構成した。** C/S と実際の次数三線束 L を固定し、J=Pic⁰(C/S)、Picard stack 上の普遍線束を M とすると、$M^{\otimes3}\otimes\pi^*(\det(\pi_*(M\otimes L))^{-1}\otimes\det(\pi_*L))$ は重み零で C×J へ降下し、三倍写像を表す。ここで$\pi$は曲線方向の射影で、$\pi_*$と$\pi^*$はそれぞれ押し下げと引戻しを表す。従って T_P^(3)=S×_(m_P,J,[3])J は階数9の有限 étale J[3]-torsorで、その上に最高次線束との同型まで規格化したfull比較核が一意な同型を除いて一意に存在する。scalar障害はJ(S)/3J(S)を通り、m_P=3qなら元のS上で消える。これは同型類選択後・固定表示とwindowの下の構成で、既存のindex|3を改善したものではない。

**点の平行移動との関係を、固定入力の下で具体化した。** 右加群ではs=σ_*∘tensor Lである。ρ=T_O∘tensor Lに対し、U_(a,b)=t_a^*∘tensor P_bへの共役は(a,b)↦(−2a−b,3a+b)であり、σ=t_pのrotationを可換側へ移す条件は3a=0,b=pとなる。支配的なR=k[[h]]族で、点関係行列から相対THCRを構成し、指定中心三次がその核に入ることを証明した。次数別Nakayama・相対ample pair・AS-Gorenstein条件を確認し、window1と閉／一般ファイバーへの導来底変更も構成した。従って相対THCR/window1を別に仮定せず、固定入力Bの下で、半古典Jacobian同型θ_scに対してJac(φ)=θ_sc、m_P=θ_sc(p_pt)となるfull核の追加型は非空である。φはθ_sc上の階数九J[3]-torsor I_scから選べる。この型の同型類選択後にはα=δ_C(p_res)を得る。全ての既存最高次線束型の核に m_P=p_res を主張しない。full 同型類の選択は一般には別段階であり、n=3,4 の一般点での解決は下記の別の定理による。

**点型は、構造対象と active 曲線への幾何的制限だけで定義できる。** source と残余側の包含を j_nc、j_Y、active 曲線の閉埋込みを i_C とすると、κ_nc≃j_nc^!O[1]、q_Y≃Li_C^*∘j_Y である。従って Q_P=Li_C^*j_YΦ_Pj_nc^!O と置けば R_P≃Q_P[1] となり、点型は H^{>0}(Q_P)=0、H⁰(Q_P) が次数零の線束、[H⁰(Q_P)]=p_res という条件で表せる。右随伴での Serre 基底線の相殺と、係数商・window1 の比較写像を unit・随伴から構成する証明により、表示選択に由来する余分な基底線や shift は残らない。

この幾何的記述は、良い一ブロックの共通稠密開上で全 O-保存同値と任意底変更に両立し、Brauer–Severi 表示も許す。full class を自動選択する結果でも、全ての refined 核を点型と同定する結果でもない。非分裂表示上でも、この内在的記述によって最高次線束型の類 m_P が降下し、選択済み full class の scalar 障害は α=δ_C(m_P) となる。次数三の偏極類が Pic_C³(K) に入るので3[C]=0であり、Tate pairing により period は三を割る。これは点型だけでなく最高次線束型の選択済み class 全体に成立する。index は n≢1 mod3 で三、n≡1 mod3 で九を割る。Euler 数だけを指定した全核へは広げない。下記の非分裂族では period 三・index 九を実現するが、全ての非分裂体で index 九となるという主張ではない。

**n≡1 mod3 の非分裂表示では、点 Picard 障害の period 三・index 九を実現できる。** 全 n≥4、n≡1 mod3 について、良い一ブロック stack の任意の非空開に、この障害を持つ体値点を構成する。一般 Hesse 曲線とその一般点を三捩れ theta torsor で twist し、active 表現と中心表現に同じ中心重みを与えた mixed 表示へ降下する。表示の Brauer 類 β は index 三だが、点線束の障害 α=δ_C(p_res) は period 三・index 九であり、両者を同一視しない。混合係数と中心 torsor の一般化は純超越拡大だけで行うので index 九を保つ。この構成は full class の事前選択を要しない。

これらの体値点で実際の点型 full 核が有限拡大 L/K 上に存在すれば 9∣[L:K] である。随伴復元点型の有限 class torsor と実現 gerbe の記述も全 O-降下し、表示安定化子が自明な共通稠密開内では全 n≡1 mod3 で強化点型の class が一つなので、周期標識を加えない最小実現次数は正確に九となる。強化点型の九と、下記の全型での三を区別する。全非分裂体への一律の九という結論ではない。証明の入口は `prop:nfm-unsplit-point-index-nine-family`、`lem:nfm-adjoint-point-unsplit-descent`、`cor:nfm-unsplit-point-minimum-nine`。

同じ n≡1 mod3 の共通な良い開上の普遍点 Picard gerbe には、Brauer–Severi 平面の相対反標準束を用いて重み一・階数九の束を構成できる。任意の非空開で正の重み一階数は九の倍数なので、開を縮めても階数三には改善できない（`cor:nfm-universal-unsplit-picard-rank-nine`）。個々の体値点の index を一律に九とする主張ではない。

**非分裂 rotation の実現 gerbe は偏極障害 β であり、class 変更で核の障害は α+rβ となる。** 最高次線束型の class を選択した後、α±β は次数±三の Picard 類に由来するため index は三を割る。従って型を指定しない比較は、その rotation 軌道内で三次以下の拡大により実現できる。n=3,4 の幾何学的自己同値群が Z となる範囲では全 class を尽くし、未標識 full 比較の最小次数は α∈⟨β⟩ なら一、それ以外は三である。四次元の指数九族では、同じ対象に対して強化点型の最小次数九・全型の最小次数三を得る。実際、α+β=(au,bv)₃ を消す三次体 K(∛au) 上でも α は非零のままであり、点型は実現されない。一般の有限 class torsor には全型上界 3 min_i[K_i:K]≤3|H_p| があり、表示安定化子が自明な一般一ブロック開では H_p=1 により全次元で上界三となる。周期標識を加えた次数とは別の結果である。証明は `lem:nfm-unsplit-rotation-gerbe`、`thm:nfm-unsplit-rotation-index-three`、`thm:nfm-unsplit-lowdim-full-degree`、`cor:nfm-unsplit-nine-versus-three`。

**点 shift の Picard 障害は、一般 split 表示で正確に index 三となる。** K=C(a,b,λ) 上の Hesse 型三次 X³−aY³−bZ³+λXYZ と三捩れ移動点 p₀ の障害は巡回代数 (a,b+λ³/(27a))₃ であり、period=index=3である。Jacobian の関数体上で p=p₀+3q とすると、一般の j・無限位数の p でも同じ障害を保つ。この曲線・偏極・平行移動から幾何的 Sklyanin 代数を元の体上に作り、一次元の cyclic potential を降下して、滑らかな commutator–gradient 形式へ規格化した。Hesse 係数の支配性を確認した後、一般の基底変更、混合係数・中心三次係数の付加は、非零障害を保つ純超越拡大だけで行える。Hesse 座標用の根の有限拡大は支配性の検査だけに使い、非零例の基礎体には加えない。従って全 n≥3 の標準 split 一ブロック係数表示の一般点で δ_Ept(p_pt) の period と index は三である。これは係数体上の族の障害であり、複素数体上の個々の曲線に非零 Brauer 類を主張するものではない。

**楕円 active 比較は全 Fourier–Mukai 同値まで分類できる。** 標数零の体 K 上で実際の次数三線束を持つ任意の二曲線 (E,L_E),(C,L_C) に対し、ρ_E,p と ρ_C を intertwine する実際の K-線型 Fourier–Mukai 同値の存在は、偏極曲線同型 φ:E→C の存在と δ_E(p)=0 の二条件に同値である。三次 rotation の数値 centralizer {±I,±R,±R²} により全数値型を規格化し、同値を φ と Jac(φ)(p) を表す実線束へ還元する。従って一般 split 係数体 k_n 上では、三に素な有限拡大後も、任意のそのような標的曲線への active intertwiner は存在しない。θ_sc を指定した規格化 active 核の同型類の fppf 層は I_sc、その実現 gerbe は Picard gerbe の引戻しである。rotation 同型そのものと指定周期を標識する場合の μ₃-torsor は別に追う。この active 分類だけから full 同型類の選択は得られない。以下の点型 full 核の不存在は、別に最高次線束と残余側 Picard 障害を用いて証明する。

**一般 split 係数体では、半古典平面同型 torsor が分裂し、その有理点は一意である。** 残余復元・全次数混合三角性の固定入力の下で、全 n≥3 の標準 split 一ブロック係数体 k_n 上で I_sc(k_n)≠∅ を証明した。混合係数についての定数降下により問題を active 体上の有限 étale torsor へ戻し、一般三次 g の Heisenberg 群 H_g の作用を full ambient の標準三次元表現 X⊕自明表現 1^r 上で追う。自明中心 summand が projective character twist を排除するため、中央化群は GL_r となり、Hilbert 90 によって対称点での form を解く。この点で得た分裂を混合定数 torsor へ戻し、F′=hF による k_n(h) からの純超越降下を行う。さらに三捩れの線型 Galois 像が SL₂(F₃) なので Jac(E_pt)[3] の k_n-有理点は零、従って I_sc(k_n)={φ_sc} となる。torsor の階数は依然として九であり、九点全てが有理になるという意味ではない。指定した formality 規約の下で、形式的な active 恒等分枝と一致する φ_sc は、中心空間を保つ全 parabolic 表示変更への共変性を持ち、良い一ブロック O-marked stack Msm の共通な滑らかな稠密開上へ、全 O-保存同値と任意底変更に両立して降下する。Brauer–Severi 平面を許すが、偏極線束の scalar 同型は追加選択しない。全 intrinsic 成分・稠密開の外・任意 formality 間の独立性へ広げる主張ではない。

**点型の scalar 障害は、一般 split 係数体で正確に period=index 三となる。** 一般の二曲線については α=δ_Ept(p_pt)+e₃,*([I_sc]∪κ₃(p_pt)) だが、上の分裂によって補正項は零であり、full class を選ぶ前から δ_Cres(p_res)=δ_Ept(p_pt) の period と index が三である。点型 full class を k_n 上で整合的に選べば、その scalar gerbe α も正確に index 三となり、残余平面三次の横断直線切片から三次分裂体を得る。全 n≥3 でこの scalar 段階を決定し、n=3,4 では下記の full class 降下により、実際の full 比較の最小次数も三と決定した。全 n≥3 の一般一ブロック族では下記の Tate–Koszul 忠実性により強化点型 class が一意となり、この型の実際の比較の最小次数も三となる。既知の Tate–Weil pairing による cup 表示、flex・平面同型・三分点の三つの階数九 torsor の区別は保持する。

**標準三分点 torsor の連結性と全モノドロミーを決定した。** 全 n≥3 の標準 split 一ブロック係数体 k_n 上で [3]⁻¹(p_pt) は連結な次数九の有限 étale 体であり、θ_sc による p_res の三分点体も同じである。一点を定義する最小拡大次数は九で、任意の有限定義体の次数は九の倍数となる。Galois 閉包の群は ASL₂(F₃)=F₃²⋊SL₂(F₃)、位数216であり、九次体は非 Galois で真の中間体を持たない。Galois な点定義体の最小次数は216である。証明は真の一般 Hesse 点による連結な [3] 被覆、Sklyanin 係数の有理逆、一般三次の Heisenberg 群による三捩れモノドロミーの移送を用いる。p=p₀+3q という特殊族だけからモノドロミーを推論しない。この九整除性は三分点をデータに持つ体への制約であり、全ての full 比較体への制約ではない。

点関係行列の余核が表すのは3pであり、pの障害を消さない。一般の p_pt と p_res は三で割れず、標準三分点 torsor は k_n-有理点を持たない。その連結性・最小次数・Galois 群は上記の通り決定した。一方、完備半古典族 R=k[[h]] では p≡0 から 3q=p、q≡0 を満たす切断が一意に存在して δ_E(p)=0 となる。この形式的分裂を完備化前の係数体上の分裂と混同しない。形式平面比較だけで cup 補正を決められない巡回 twist 例があるため、上の H_g 作用と混合定数降下は省略できない。

**全 n≥3 で、実際の点型 full 核は k_n と三に素な有限拡大上には存在しない。** その核 P があれば H⁻¹(q_YΦ_P(κ_nc)) は p_res を表す実際の線束となり、非零の δ_Cres(p_res) を消すためである。従って有限拡大 L/k_n 上に実際の点型 P が存在すれば3∣[L:k_n]であり、点型比較被覆の各一般成分の次数も三の倍数となる。I_sc は既に k_n 上で分裂するので、φ∈I_sc(L) をデータに追加する必要はない。この点型での不存在に full class の事前選択や代数的 active 核 assignment は不要である。n=3,4 では別の全自己同値分類によって任意の full 核へ強化するが、n≥5 では任意型への拡張は未証明である。

**n=3,4 では、一般 split 係数体上で full 比較核の同型類の降下を解いた。** 三次三様体・very general な三次四様体の既知の自己同値分類を幾何学的一般点に適用し、projector 核の一意性を用いると、full dg 核の自己同値類は元の体上の実核 T=ρ_Y⁻¹[1] が生成する定数群 Z となる。連続な Galois cocycle は Z に非零有限像を持てないため、全ての幾何的 full 比較 class が k_n 上へ降下する。T の合成で各 class の scalar gerbe を同定でき、点型で計算した α=δ_Cres(p_res)=δ_Ept(p_pt) の period=index 三が全 class に共通する。従って型を指定しない実際の full 核も k_n と三に素な有限拡大上には存在せず、三次拡大上には存在する。underlying 比較と rotation を intertwine する性質を要求した比較の最小次数は三である。この全 class 降下だけでは一つの class を選ばないが、下記の随伴復元条件を満たす点型は唯一の class を与える。全核が点型になるという主張ではなく、この自己同値分類を Zariski 開の全点へ拡張しない。n≥5 でも下記の強化点型の第一段階は解決するが、全 class の分類は主張しない。

**n=3,4 の指定周期の位相は、全 underlying full class に共通である。** scalar 重み零の Hom 直線 V₀ 上の三次形式 c に対し、周期 torsor の Kummer 類を γ=[c(e)⁻¹]∈k_n×/k_n×³ と定める。T=ρ_Y⁻¹[1] の全整数冪は指定 MF 周期に適合するため、class を変えても γ は変わらない。source の中心元を u 倍、target の方程式生成元を v 倍すると、指定周期はそれぞれ u⁻¹ 倍、v⁻¹ 倍となり、γ′=[v/u]γ となる。両側を同時に同じ単元で変えた場合は不変である。

**周期位相を問う規格化は、点尺度と唯一の平面同型から三乗倍まで定める。** 低 rotation 積から回復するのは残余方程式の直線であり、独立な target 生成元を最初から標識しているわけではない。source 中心元 Ω と trace–Hessian 像 H を選ぶと、Π=ι(dH)P_src による強い持上げが volume P_src を一意に定める。φ_sc の任意の k_n-線型持上げ f に対し、F_φ⊗det(f)(P_src)=t_sc と置く。f の scalar 倍は F_φ を三乗倍しか変えない。また Ω を u 倍すると P_src は u⁻¹ 倍、F_φ は u 倍となるので、両側の同時変更に対する周期位相は不変である。これにより全 n≥3 の正準強化 class に γ_sc,n∈k_n×/k_n×³ が定まり、n=3,4 では全 full class に共通となる。target の実際の基底や marked kernel 自体を正準的に選んだという主張ではない。

生成元固定の形式 CF 模型では、W_h|_K=b_hJ_g、b_h∈1+h k[[h]] と、ある線型持上げの scalar λ_h に対して F_φ=λ_h⁻³b_h⁻¹W_h を得る。従って γ_sc の完備半古典体への像は [b_h⁻¹]=1 である。F′=hF による係数の吸収では source 中心元と実際の曲率の双方を h 倍するため、余分な h の Kummer 類は残らない。さらに、有限 MF の内部次数と混合重みによって無限 arity の CF 挿入後も混合単項式数を一様に抑え、h だけを完備化した κ(m) 上に実際の周期付き full Morita 比較を構成できる。局所化するのは integral な有限対象の Hom であり、負の h 冪を持つ新しい Maurer–Cartan 元へ無限 flow を再評価しない。

**全 n≥3 の正準強化 class の γ_sc,n は、二変数不変量体 C(s,t)、s=c₄(g)、t=−c₆(g)、へ一意に降下する。** 混合有理 CF 比較が形式拡大後に同じ完備核となることを確認し、随伴復元条件を忠実平坦降下する。線型持上げと周期解の商 (f,η)↦(λf,λ⁻¹η) による μ₃-torsor の SL₃ 同変構造と、Heisenberg 安定化群の character 消滅を用いる。Δ=s³−t²、D=1−s/24−t/216−s²/6912 と置くと、下記の境界計算により全 n で γ̄_n は非自明、位相体 M の次数は三である。正準強化 class の標識付き最小次数は 3 ind(α_M)∈{3,9} であり、α_M の index は未決定。全 full class への共通性は n=3,4 に限る。ΔD 外の非分岐性を仮定すれば、半古典条件による三候補 1,[D],[D]² のうち境界付値が [D] を選ぶ。大域式 γ̄_n=[D] と大域的な次元間の一致には、この追加仮定をまだ要する。

**半古典条件を保つ周期位相は Hesse 係数体で忠実に検査できる。** C(s,t)→C(p,q) の三次 Kummer 核は ⟨[Δ]⟩ だが、一般 active 十係数体で得た半古典像1の条件が非自明な核の二元を除く。D の逆像は八本の直線であり、q=2 の一般点では Hesse 写像は非分岐、D=−(p³+8)²(q−2)/27+O((q−2)²) となる。この trait 上の実際の低積計算から、以下の完備局所 Kummer 類と D での付値を得る。Hesse 完備体では Δ が既に三乗なので、完備体だけから大域的な忠実性を主張しない。証明は `prop:nfm-period-hesse-faithful-test`、`lem:nfm-period-hesse-eight-boundary-lines`。

**指定周期の位相は、随伴復元対象の有限な二次・三次積で評価できる。** Picard gerbe 上の普遍線束 M から Z_p=q_Y^R M[1] を作ると、その Adams graded orbit は重み零なので元の体へ降りる。通常 Ext の切出しの m₂ が B_p、指定周期 t_p と m₃ が Ω_p∈(B_p)₃ を定め、一般係数体上の実際の同型 f により γ_sc,n=[f(Ω_p)/Ω] となる。三次積の gauge 差は二次関係 ideal で消える。良い integral 表示と primitive な三次関係を持つ場合の非分岐判定も保持するが、q=2 で得た三次関係は飽和格子内で正確に z の一倍を含み、その十分条件を満たさない。証明は `prop:nfm-period-phase-low-products`、`lem:nfm-period-integral-presentation-unramified`。

**q=2 境界の三分点被覆は、完全分岐三次体の三つのコピーへ分かれる。** z=q−2、K=C(p,m)((z)) とすると点曲線は split I₃ 模型で、P−O の線束の multidegree は (1,0,−1)。接線比の規格化から三分点被覆は3 Spec L、L=K(∛(2z/(p³+8)))=K(∛D) と明示でき、慣性型は3³となる。一方、実線束 O(P−O) とその三行三列線型表示は R=C(p,m)[[z]] 上へ延びる。従って三分点の分岐を full 周期位相の分岐と同一視しない。この三次体では候補1,[D],[D]²が全て消えるため、三分点上の計算だけでは D の指数を判別できない。証明は `prop:nfm-hesse-boundary-third-division`、`lem:nfm-hesse-boundary-determinantal-line`。

**q=2 の完備局所周期位相を、全 n≥3 で [D_R] と決定した。** 明示的な点線束の行列と十分強い中心座標の極消去により、実際の指定方程式を保ったまま F≡J_g mod z² とする。右射影の窓を通して、全 orbit Hom は R-自由で底変更と可換となり、N=n+2 に対して rank HⁱRHom(Z,ρʲZ)=binom(N,3i+2j)（範囲外は零）である。特殊 fibre では m₂* の階数が binom(N,2)−3 に落ち、m₃ の三次 class も零となるが、失われる三つの二次関係の Smith 指数は全て一である。関係を飽和すると全次数で平坦な代数を得、その active 特殊 fibre は S(0,−2,−p)。三次関係の初出は z 倍の非零中央元である。cyclic potential の alternating 成分を用いて滑らかな potential 三次を回復し、指定された一般 active 射影同型を延長して係数を比較すると γ_sc,n=[D_R] を得る。従って v_D(γ̄_n)=1 mod3、位相被覆の分岐指数は三である。滑らかな特殊残余三次や full 比較核の延長を主張する結果ではない。主証明は [境界の低積と周期位相](papers/sections/residual_boundary_products.tex) の `prop:nfm-boundary-saturated-active-potential`、`prop:nfm-boundary-period-local-kummer`。

周期 torsor の成分体 M は次数一または三で、指定周期付き比較の最小次数は全 class に共通に [M:k_n]ind(α|_M)∈{3,9} となる。target の生成元を適切な k_n-単元倍に選び直した適合規格化では最小次数は三である。target だけに独立変数 t による尺度を付けた k_n(t) 上の一般族では、周期成分体が k_n 上の純超越体となり scalar index 三を保つため、任意の有限実現体の次数は九の倍数であり、最小次数は正確に九となる。この独立尺度を元の一ブロック係数や formality のパラメータと同一視しない。scalar G_m-gerbe、標準三分点 torsor、相対周期の μ₃-torsor は別の構成であり、裸の O-marked 対は任意の相対周期規格化を標識しない。

**一般高次元の class と T-軌道には同じ Galois 安定化群がある。** rotation を保つ幾何的 full 自己同値類の群を G_ρ、対応する比較 class の torsor を C_ρ とする。元の体上の実核 T=ρ_Y⁻¹[1] は G_ρ の中心にあり、⟨T⟩≅Z である。各 class とその T-軌道の Galois 安定化群は一致するので、class 選択は C_ρ/⟨T⟩ の有理点、すなわち G_ρ/⟨T⟩ に値を持つ非可換 H¹ 障害の中立性へ正確に帰着する。点型を含む固定軌道が一つあれば、その点型 class 自体が降下する。T が点型を保つことはこの議論の前提ではない。

split な滑らかな三次の奇数次元では数値 Ku 格子は階数二、Galois 作用は自明であり、rotation の数値中央化群は C₆ となる。G_{ρ,0} を数値作用の核とすると G_ρ/⟨T⟩≅G_{ρ,0}/⟨[2]⟩ である。n≢1 mod3 では Serre 関手から rotation を回復できるため、G_ρ は全自己同値類群に等しい。数値作用だけでは full class を決定できないが、随伴復元条件ではこの群の有限部分に絞れ、さらに Tate–Koszul 忠実性でその自明性を示せる。

**随伴復元条件を満たす点型の first stage は、有限 étale torsor である。** Z=j_nc^!O、q=Li_C^*j_Y、q^R=j_Y^!i_* と置く。点型 P に対し E_P=Φ_PZ、M_P=H⁰(qE_P) とし、truncation と随伴から来る正準射 E_P→q^R M_P が同型になる条件を加える。この強化点型は固定入力の形式恒等分枝と finite-perfect 降下により非空である。幾何学的に p_res を表す線束 M を選んだ E_p=q^R M の同型類は Galois 不変であり、H_p={g∈G_ρ:g(E_p)≃E_p} は有限群となる。三つの rotation 像による generator、Toën–Vaquié の boundedness と HH¹=0 を合わせて有限性を示すのであり、全自己同値群の有限性を主張しない。強化点型の class は有限 étale H_p-torsor S_p をなし、その実現 stack は S_p×Picard_{p_res} である。M や E_p の実現を元の体上で選べるとは仮定せず、class の有限 torsor と scalar index 三を区別する。

有限 H_p と class torsor の記述は一般の形式で保持する。全 n≥3 で rotation Euler 数の最大公約数 d_n は正なので [E_p]≠0、全奇数 n では H_p⊂G_{ρ,0} であり、n=5 では χ(E_p,E_p)=−27 である。S_p=⊔Spec(K_i) による強化点型の最小次数公式 min_i[K_i:k_n]ind(α_{K_i})≤3|H_p| も有効である。一般一ブロック族では下記の Tate–Koszul 忠実性により H_p=1 と分かるため、class を選択する第一段階は全次元で解消する。随伴復元条件のない全点型や任意の full class の分類は含まない。

**全 n≥3 の一般一ブロック族で、随伴復元点型の class は正準的に一つとなる。** A=B/(Ω)、deg Ω=3 に対し、固定入力の双加群自己交叉三角から通常 Ext= B!⊗k[t] と Tate Ext= B!⊗k[t,t⁻¹] を得る。deg ξ=(1,−1)、deg t=(2,−3) とすると j=−p−q≥0 の部分が通常 Ext であり、全 A∞ 積・写像・homotopy に保たれる。Adams Koszul 双対と derived localization の mapping space の忠実性により、原点と rotation を保つ核 class は Aut_gr(B,kΩ)/G_m へ単射を持つ。一般表示の射影安定化子は自明なので H_p=1、S_p=Spec(k_n)。scalar gerbe はなお α=δ_C(p_res)、period=index=3 であり、周期標識を加えない強化点型の最小実現次数は正確に三である。全自己同値群を分類した結果ではない。証明は `thm:nfm-origin-rotation-faithful`、`cor:nfm-generic-adjoint-class-unique`。

**一般三次五次元の Clifford 半 rotation は、平面の選択に依存せず実核として元の体へ降下する。** Peize Liu の O_Cl²≃ρ を、平面の Fano 曲面 F₂(Y) 全体の実際の相対 perfect 核として構成する。F₂(Y) の幾何学的連結性と HH¹=0 による離散性から、その幾何的核 class は一定となる。降下 gerbe の類 β_O は convolution により 2β_O=0 であり、F₂(Y) の Plücker 次数2835の零 cycle 上で分裂するので 2835β_O=0、従って β_O=0 となる。ここでは β_O を表示 gerbe や点 Picard 障害と区別する。

Clifford 半 rotation はさらに、関手として O_Cl A≃Aρ⁻¹[1] と同定できる。spinor 列を相対随伴の unit と同定し、相対 coevaluation と通常の right mutation の coevaluation を比較する。Ku の二つの消滅から差が例外的 block ⟨C₁⟩ に入り、mutation で消える。従って元の体上でも O≃T、O³≃[1]、ε=OT⁻¹≃id であり、E_p も固定される。これは対象の固定や数値的自明性からの推論ではなく、perfect 核の自然同型である。既存の相対核・奇数零 cycle による降下の証明も保持する。指定された square 同型と MF period の同時正規化は別問題である。証明は `lem:nfm-fivefold-spinor-relative-coevaluation`、`thm:nfm-fivefold-half-rotation-identification`、`cor:nfm-fivefold-half-rotation-candidate-trivial`。

全自己同値群が常に Z になるという延長は、一般三次七次元では実際に偽である。Iliev–Manivel の既知の rank 九球面束に由来する twist と shift は Z² を生成し、この twist の異なる冪は G_ρ の異なる剰余類を与えるので G_ρ は全群内で無限指数となる。これは rotation 中央化群自身が巡回でないという結論ではない。Torelli による多様体の復元も、自己同値の作用の忠実性を自動的に与えない。このため全自己同値群の分類を先に解くことを必要条件にせず、点型を含む一つの固定軌道を狙う。全 n の強化点型 class は下記の忠実性により選択でき、任意の full class の分類は残る。

この型は従来の CF Euler 数値型より強い。Euler 条件だけの型に対する d_n=3^floor((n+1)/2) の bound と、rotation Euler 格子 d_n Z は保持する。n≥5 では、この評価だけから任意型の scalar index 三や full class の降下を結論しない。n=3,4 の全 class に対する exact index 三は、自己同値分類による別の降下定理で得るものであり、全ての核が点型になるという主張ではない。表示類βと核の類αは同一視しない。既に選んだ三-primary な類の index は三に素な体拡大では不変である。

**完備中心商について MF 比較を構成した。** 厳密相対 bar flow とその逆を中心係数の斉次商へ降ろせるので、U=0 の active MF にも比較が得られる。任意の quotient MF を扱い、元の MF からの持上げを仮定しない。ただし、一般点の有限代数的核への coherent な中心線型性の降下は未完成である。係数商と圏の導来 tensor の同一視、absolute perfect から relative perfect への推論には一般的な反例があり、研究ノートに整理した。

既存の1ブロック型に残る重要な精密課題は、二変数体上の残余 Kummer 類 β_n=γ̄_n/[D] と、三次位相体 M 上の scalar index ind(α_M) である。全 n の q=2 完備局所値 [D_R] と D での三次分岐は決定済み。次は ΔD 外の divisor、特に現行の保証開が除外する小位数の active 移動点の divisor で β_n の非分岐性を検査する。それが示せれば半古典条件と既存の UFD 判定により大域式 γ̄_n=[D] が従う。位相体の次数三だけでは標識付き最小次数三／九は決まらず、α_M の計算が必要である。coherent な中心線型性、高次元の任意 full class、非分裂の別 rotation 軌道、各 intrinsic 成分も別に残る。主証明は [低積評価](papers/sections/residual_tate_reconstruction.tex)、[周期位相](papers/sections/residual_period_descent.tex)、[境界計算](papers/sections/residual_boundary_products.tex)。

個別次元の Jacobi 計算と boundary の精査は、この一般目標の具体的な障害を解消する場合に行う。八次元の頂点構造等の既存成果と証明書は保持する。次の具体的な着手方法と各目標の到達基準は [研究方針](00_research_plan.md) にまとめ、全体の要約は [research-hub](https://github.com/uedakazushi/research-hub) に反映する。

## 主要結果と未完成部分

複数ブロックの相対比較・自然な周期・因子分離下の全中心同変核・二ブロックの中心非正規性と、一ブロックの点型・算術的障害について、次の適用範囲を区別する。複数ブロックは上記mbhp・mbic・mbfc・mbun節を参照する。一ブロックの平面同型の分裂は [点曲線・尺度の本文](papers/sections/residual_point_scale.tex)、点型・full class は [点の平行移動と核のPicard類の本文](papers/sections/residual_kernel_point.tex)、周期位相の未解決大域式は [周期位相の節](papers/sections/residual_period_descent.tex) にある。

| 対象 | 現行稿に証明のある結果 | 証明の入口と限界 |
|---|---|---|
| 複数ブロックの相対直接積 | 実perfect核と任意noetherian底へのcompact底変更。射影表示・中心rigidification上へ降下し、後者で非捩れ `Perf(∏E_i)` | `mbrn:thm:relative-product`、`mbic:thm:projective-product`、`mbic:prop:rigidified-product`。非正則底の全Db(coh)や通常残余圏自体のB降下は含めない |
| 複数ブロックのPicard補正型 | 核gerbeは `Σδ_i`、位相は `Cube(v_i(p_i))`。通常／rotation・周期付きの核stackは `G_Pic×D`／`G_Pic×T` として因子stack・全O認識開へ降下 | `mbhp:thm:period-formula`、`mbic:thm:kernel-stack`。stackの降下と大域切断は別 |
| 自然な二捩れ境界の独立位相 | 剰余+1の独立なk位相を実現。Picard型の最小比較次数は中心作用付きで `3^(k−1)`、さらにrotation・周期付きで `3^k`。有限型函数体 `C(d_1,…,d_k)` でも同じ | `mbpd:prop:boundary-phase`、`mbpd:cor:phase-independence`。Picard gerbeは既に中立。位相段階の最小性であり、任意の核型への下界ではない |
| 全基本実表示の体上比較 | 通常Kuの中心作用付き比較は次数高々 `3^(2k−1)`、さらにrotation・指定周期付きなら高々 `3^(2k)` の有限拡大で存在 | `mbpd:cor:field-degree`、`mbrc:thm:finite-point-comparison`。順序付き実表示が入力。全上界の最小性は未証明 |
| 全 active Fourier–Mukai 同値 | 実次数三偏極を持つ任意の標的曲線 C への intertwiner の存在は、偏極同型 E→C と δ_E(p)=0 に同値 | `cor:nfm-elliptic-any-intertwiner-criterion`、`prop:nfm-elliptic-intertwiner-gerbe`。追加の周期標識は別の μ₃-torsor。full 核の分類ではない |
| 一般 split 係数体の点障害 | 全 n≥3 で δ_Ept(p_pt) の period=index=3。三に素な有限拡大後も active intertwiner はなく、p_pt と p_res は三で割れない | `prop:nfm-active-point-obstruction-dominant`、`cor:nfm-generic-point-picard-index-three`、`cor:nfm-generic-active-intertwiner-obstruction`。係数体上の族の結果であり、複素閉点の Brauer 類ではない |
| 半古典平面同型の存在と自然性 | I_sc(k_n)={φ_sc}。三捩れの全 SL₂(F₃) 像により有理点は一意だが scheme の階数は九。φ_sc は良い一ブロックの共通滑らかな稠密開上で全 O-同値・任意底変更へ降下 | `thm:nfm-generic-plane-isom-splitting`、`prop:nfm-semiclassical-plane-isom-descent`、`cor:nfm-generic-plane-isom-unique`。Brauer–Severi 平面可。全 intrinsic 成分や任意 formality 間の独立性は未主張 |
| 一般 split 係数体の残余障害 | δ_Cres(p_res)=δ_Ept(p_pt) の period=index=3 | `cor:nfm-generic-residual-picard-index-three`。非分裂表示の全ての体へ exact index 三を拡張しない |
| 選択済み点型 full class の scalar 類 | α=δ_Cres(p_res) は正確に index 三、三次分裂体を持つ | 全 n≥3 の scalar 定理。強化点型 class は全次元で一意。n=3,4 の全 class 降下は下記の別定理 |
| 点型の幾何的認識と非分裂障害 | Q_P=Li_C^*j_YΦ_Pj_nc^!O の最高次線束で点型を記述し、共通な良い稠密開上で全 O-同値・任意底変更に両立。非分裂の最高次線束型の選択済み class も period∣3、index は n≢1 mod3 で三、n≡1 mod3 で九を割る | `prop:nfm-active-restriction-geometric`、`cor:nfm-point-type-O-descent`、`cor:nfm-unsplit-point-scalar-period-three`。full class 選択は別段階。全非分裂体で一律の exact index は主張しない |
| 非分裂点型の指数九 | 全 n≥4、n≡1 mod3 の任意の非空開に period 三・index 九の点 Picard 障害を実現。表示障害の index は三。実際の点型核の体次数は九の倍数で、表示安定化子が自明な共通稠密開内の全 n≡1 mod3 の強化点型は最小次数九を達成。普遍点 Picard gerbe の正の最小重み一階数も任意の非空開で九 | `prop:nfm-unsplit-point-index-nine-family`、`lem:nfm-adjoint-point-unsplit-descent`、`cor:nfm-unsplit-point-minimum-nine`。周期標識を加えず、任意型や全非分裂体へ一律の九を主張しない |
| 非分裂 full 比較の rotation 軌道 | ρ の実現 gerbe は β、ρʳP の障害は α+rβ。α±β の index は三を割り、n=3,4 の全型の最小次数は α∈⟨β⟩ に応じて一／三。指数九の四次元族では強化点型九・全型三 | `thm:nfm-unsplit-rotation-index-three`、`thm:nfm-unsplit-lowdim-full-degree`、`cor:nfm-unsplit-nine-versus-three`。高次元では共通慣性自明開の強化 class 選択を用いて上界三。周期標識なし |
| 点型 full 比較被覆 | 全 n≥3 で実際の点型核は k_n と三に素な有限拡大上に不存在。各一般成分の次数は三の倍数 | `cor:nfm-point-comparison-cover-three-divisibility`。φ の付加や active assignment は不要。n≥5 の任意型への拡張は未証明 |
| n=3,4 の全 full 比較 | 全 full class が k_n 上へ降下し、scalar gerbe は全型共通で period=index=3。underlying 比較と rotation intertwining の性質を要求する比較の最小次数三 | `thm:nfm-low-dimensional-full-class-index-three`。幾何学的一般点の結果。全核が点型とは主張せず、高次元の全 class 分類は未完成 |
| 正準強化 class の指定周期付き比較 | 全 n≥3 で γ_sc,n は C(c₄,−c₆) へ降下し、q=2 完備局所で [D_R]。従って非自明で位相体 M は三次、標識付き最小次数は 3 ind(α_M)∈{3,9} | `prop:nfm-boundary-period-local-kummer`。全 class 共通性は n=3,4。大域式 [D] は ΔD 外の非分岐仮定付き。相対 frame 変更・適合 frame の三・独立 target 尺度族の九も保持 |
| 周期位相の有限評価 | Z_p=q_Y^R M[1] の m₂,m₃ と指定周期から B_p,Ω_p を回復し、γ_sc,n=[f(Ω_p)/Ω]。q=2 では二次関係を飽和した格子で Ω_p は正確に z の一倍 | `prop:nfm-period-phase-low-products`、`prop:nfm-boundary-period-local-kummer`。primitive target 周期と primitive 三次関係を区別する |
| Hesse 境界の三分点と線束 | q=2+z で split I₃、点線束の multidegree (1,0,−1)、三分点被覆は3 Spec K(∛D)、慣性型3³。点線束の三行三列表示 L は完備化前の代数的 trait 上の有理式で与えられる | `prop:nfm-hesse-boundary-third-division`、`lem:nfm-hesse-boundary-explicit-line`。三分点上では三候補1,[D],[D]²を区別できない |
| 境界の full 残余対象と低積 | 指定周期を保つ選択した模型に全 n の右射影を構成。全 orbit Hom は自由で rank binom(n+2,3i+2j)。raw 二次関係の三つの Smith 指数は一、飽和代数は全次数平坦 | `prop:nfm-boundary-saturated-active-potential`、`prop:nfm-boundary-period-local-kummer`。特殊残余三次の滑らかさや full 核の延長は不要 |
| 高次元の full class 選択 | class と T-軌道の Galois 安定化群が一致。奇数 n で G_ρ/⟨T⟩≅G_{ρ,0}/⟨[2]⟩、数値中央化群 C₆ | `prop:nfm-highdim-central-shift-obstruction`、`cor:nfm-highdim-point-class-orbit`、`prop:nfm-odd-numerical-rotation-centralizer`。全点型・任意型の class 選択は未解決 |
| 随伴復元点型の class 選択 | 全 n≥3 の一般一ブロック族で H_p=1、S_p=Spec(k_n)。一意な class の scalar gerbe は Picard_{p_res}、一般 split 体で未標識最小次数三 | `thm:nfm-origin-rotation-faithful`、`cor:nfm-generic-adjoint-class-unique`。全群や全型の分類は含まない |
| 五次元の Clifford 半 rotation | 相対核として降下し、さらに O≃ρ⁻¹[1]、O³≃[1]、ε≃id を perfect 核として同定 | `thm:nfm-fivefold-half-rotation-identification`。相対・絶対 coevaluation の自然な比較による。指定 square/period の正規化は別 |
| 七次元の自己同値の障害 | 一般三次七次元の全自己同値群は球面 twist と shift による Z² を含み、rotation 中央化群は全群内で無限指数 | `prop:nfm-sevenfold-noncyclic-aut`。球面束・twist 自体は Iliev–Manivel の既知結果。中央化群自身の巡回性を否定する結果ではない |
| 標準三分点 torsor | 全 n≥3 の k_n 上で連結な九次体、真の中間体なし。Galois 閉包は ASL₂(F₃)、位数216。最小点定義次数九、最小 Galois 点定義次数216 | `thm:nfm-generic-point-third-division-monodromy`。全 full 比較体に九整除性を要求する結果ではない |
| 行列余核・形式分裂 | 点行列の余核から得る次数零線束は3pを表す。R=k[[h]] 上の p≡0 には一意な q≡0、3q=p があり、点障害は分裂 | `prop:nfm-point-matrix-tripling-line`、`lem:nfm-formal-point-third-division`。完備化前の係数体での分裂は従わない |

Sklyanin の幾何学的分類、楕円 Fourier–Mukai 核の graph 認識、Picard 障害の Tate–Weil pairing、Fisher の Heisenberg 中央拡大、Liu と Huybrechts の低次元自己同値分類、Peize Liu の五次元 Clifford 表示と半 rotation、Kuznetsov の相対二次曲面束、Collino の平面 Fano 曲面、Ciliberto–Zaidenberg の次数公式、Iliev–Manivel の七次元の球面束と twist、Toën–Vaquié の perfect 対象の boundedness、Murfet の MF residue trace は既知の入力である。本稿では算術的実現・一般点の index 三、full ambient と混合定数降下による平面同型、点型の全 O-共変性、三分点の全モノドロミー、低次元 full class 降下、周期位相の class 不変性・三乗規格化・形式像・混合有理比較と二変数不変量体への降下、高次元の T-軌道簡約と随伴復元点型の有限 torsor を記述し、内部で独立点検した。有限安定化群の証明は全自己同値群の有限性を意味せず、形式位相の消滅も元の係数体での消滅を意味しない。Tate–Koszul 忠実性、五次元半 rotation の関手同定、非分裂 rotation の算術、周期位相の忠実な Hesse 判定を本文で証明し、内部独立点検を行った。外部査読や新規性の網羅的確認は未完了である。具体的な文献と確認範囲は [研究ノート](notes/research_notes.md) と [検証範囲](notes/validation.md) を参照する。

一ブロックの周囲代数の次数付きモジュライの次元は `(n²+7n−4)/2`、中心三次 torsor の相対次元は `binom(n+1,3)`。良い相対 PBW 表示チャートでは、有限 Koszul 対角、真正な双加群双対、compact 性、相対 properness、Serre 関手 `S=(1−n)[n]` と trace を任意底変更に両立して構成した。

固定した良い表示模型間では、任意係数変更を圏内の係数作用として構成し、全 O-保存同値と自然同型の fpqc 降下を証明した。全同値の層は `Isom_gr/G_m` に一致する。同値を大域の次数付き同型で表す障害は `Pic(R)[n−1]` の線束であり、次数一部分がともに自由なら `Pic(R)[gcd(n−1,3)]` に入る。従って `n≠1 mod3` では全同値に大域の次数付き代表がある。`n≡1 mod3` では、滑らかな affine 曲線上の非自明な三捩れ線束による良い PBW 模型の明示例で、指定した同値の大域持上げが存在しないことを示す。

良い一ブロック模型に fpqc 局所的に同値な O-marked Grothendieck 圏族は、重み付き次数加群の tails によって効果化され、滑らかな既約 DM stack `[Jgood/P̄]` として分類される。次数一 shift は標識に含めない。大域次数付き表示の障害 β∈H²(G_m) は `gcd(n−1,3)` で消える。`n≡1 mod3` では、**任意の非空開**に β≠0 の C(s,t)-点が存在し、普遍障害の位数は正確に3である。これは上の指定同値の Picard 障害とは別の結果である。

楕円境界・固定点なし・中心三次非零因子の条件下で、相対点スキームは `E⊔D`。臨界スキーム C=V(F_x,F_y,F_z) は中心への有限局所自由八重被覆であり、その三次切断 D は型 `(2,2,2,3)`、各 fibre の次元 `n−3`、次数24である。これらの構成は任意基底変更に両立する。点商関手・shift・中心射影は O-marked stack 上に降下し、非空開では埋込み点対応から中心直線 [w] まで回復する。従って A=B/(w) 全体を復元できる。

正規化 trace `Tr/8` と尺度付き Hessian によって量子中心三次と古典三次 Casimir を同定する。さらに任意基底上で、滑らかな三次の相対双ベクトルには `ι(dH)Π=0` を満たす一意な強い affine lift `Π=ι(dH)P` がある。この結果から Poisson 対だけで support・二次関係・中心直線を回復し、**Msm≅Pgood⊂Pdec** を得る。周囲 B 単独の有限安定化子は要求せず、良い PBW・中心・相対双対・全同値比較を満たす pair を扱う。次元は `binom(n+2,3)+3n−2`、Brauer 障害の位数も同じである。標的は Brauer–Severi ambient と偏極類を許し、実際の相対 O(1) の存在は別条件である。

既存の一般三次の被約 Poisson 分類を使うと、一般三次の非空開上では全非零 Poisson moduli への開埋込みとなる。滑らかな三次 moduli を支配する Poisson 成分は一つだけで、本構成はその一般部分の開を同定する。特殊三次上の別成分や、全 intrinsic 圏成分の分類を含む主張ではない。

**Kuznetsov 比較には具体的な障害がある。** 固定入力論文Bの完備移送・一般点復元の下で、全 n≥3 の split Hesse 族に対し `λ_TH=h`、`λ_res=(h+h²/3+h⁵/12)/(1−h⁴/4)` を得る。三重線形形式の symmetrizer が active な平面三次を回復し、その j 不変量の差は `13824h⁴+O(h⁵)`。従って一般ファイバーは代数閉拡大後も同型でなく、非可換残余圏と Ku(X_TH) との rotation 保存 dg Morita 同値はない。`n≢1 mod3` では rotation なしでも同値はない。同じ ambient Π のどの smooth cubic Casimir を選んでも、この例の X_res は得られない。

一般混合 Hesse 表示では、短い中心式から h²ABC/6 を引いた Hessian jet の規格化を固定する。Dito の二次星積と Shoikhet の内向き wheel 消滅を用いる指定 formality 模型で、残余 potential と trace–Hessian 像の最初の差は `h²(Hess_active(F)/24+tr(Hess_active(F))/12)` となる。その全 Jacobi 類は非空 Zariski 開で非零であり、marked な形式比較を妨げる。この有限 jet の結果から、標識を外した全ての一般ファイバーの圏非同値までは結論しない。入力定数族に対する純中心補正の非自明性も別に全次元で証明した。

代数的補正は、`D_P(H)=〈det(D_K²H),P⊗P〉` と正規化 trace τ による `H♯=H+D_P(H)/24+τ(D_P(H))/12` である。`Φ:(H,P)↦(H♯,P)` は任意基底変更・方程式の生成元・全射影同型に両立し、O-marked moduli の非空開へ降下する。適切な稠密開上で表現可能な有限 étale 射となり、階数は全 n≥3 で9である。support を残した零切断の形式近傍では可逆だが、この補正射自体は有理同型ではない。次数9は同一座標群の商 stack の射の次数であり、慣性群を調べず粗モジュライの次数とは同一視しない。`H♯|K` は元の量子代数の楕円点曲線に厳密に一致する。この点曲線公式自体は Mori–Smith の既知結果である。

固定した harmonic-angle formality の下では、生成元を固定する逆 Poisson tensor π_h は二次関係から一意に決まり、元の中心一次空間を全次数で保存する。滑らかな三次と滑らかな active 制限の下で `π_h=a_hι(dW_h)P`、`a_h=h+O(h²)` となる。中心逆像は純中心三次を固定する。既知の Kontsevich の形式対応を使う結果であり、有限 h の収束・代数化は含まない。

係数が h に依存しない二次関係と Hessian 正規化中心元では、`c₂=0`、π_h と a_h は奇級数、W_h は偶級数となる。従って `a_h=h+O(h⁵)`、`W_h≡H♯ mod h⁴`、`π_h≡Π♯ mod h⁵` が全混合係数で成立する。さらに純 active 三次 g では `π₅(g)=S(g)Π_g/80`。四次不変式の規格化は `S(xyz)=1`、`S((x³+y³+z³)/3+λxyz)=λ(λ³−8)` である。一般混合係数も U=0 へ制限すると同じ式となるため、S(g)≠0 の稠密開で実際の tensor と有限 Hessian 補正は五次から異なる。証明は Lindberg–Pym の既知の量子トーラス交換比と、共変式の一次元性を用いる。この相違だけから残余三次や Ku の非同値を結論しない。

五次の全混合 tensor は、明示三次共変式 I,J により `π₅=Π_Q₅`、`Q₅=(4I+J−2S(g)F)/240` となる。二定数表示の値は **β=1/60、γ=1/240**。証明は普遍共変式空間への還元と、Banks–Panzer–Pym の既知の harmonic weights を Buring の公開データから抽出した73項の有理数計算を使う。graph 積分を新たに評価したという主張ではない。

指定した Hessian 正規化中心元では **W₄=Ψ_λ(F)+I/24−J/80**、`a_h=h(1+S(g)h⁴/240)+O(h⁷)` を得る。`W₄=Q₅−a₄F+G₄(U)` の純中心項も `G₄=C₄` と決まる。Hesse 表示 `F=g_λ+Axy+Byz+Czx+Dx+Ey+Hz+G` では、

```text
C₄ = λ(A³+B³+C³)/60 + λ²ABC/40
     + (2−λ³)(AH+BD+CE)/180 + S(g_λ)G/80.
```

全 Jacobi 環では `[J]=[F]=0` であり、従来の補正との四次差は `[I]/60+[τ_F(I)]/40+S(g)[τ_F(F)]/80` となる。全次元の滑らかな例 `F_*=(x³+y³+z³+u³+v³+Σw_j³)/3+uxy+vyz` で、この類を −1/9 に送る双対証明書がある。従って各 n≥3 の一般混合係数の非空開で、同じ h と特殊ファイバーの同定を保つ四次の三次超曲面の比較は存在しない。固定入力の MF・window 同値を適用した標識付き Ku 比較にも障害を与えるが、一般ファイバー上の無標識の非同値までは結論しない。

この四次差は、`E_P(H)=I_P(H)/60+J_P(H)/240−S_P(H)(H−τ(H))/80+τ(I_P(H))/40` により打ち消せる。四つの volume を P で縮約して S_P,I_P,J_P を定義し、`H^[4]=H♯+E_P(H)`、`P^[4]=(1+S_P(H)/240)P` と置く。出力が滑らかで後者の係数が可逆な非空開上の **Φ^[4]:(H,P)↦(H^[4],P^[4])** は任意基底変更と全 O-同値に両立する。指定中心元の trace–Hessian 像に沿って `H^[4]≡W_h mod h⁶`、`ι(dH^[4])P^[4]≡π_h mod h⁷`。新しい射の一般次数、楕円点曲線との全次数の関係、同じ X の Ku との全次数同値は未決定である。証明は [四次補正の本文](papers/sections/fourth_correction.tex) の `prop:nfm-mixed-fifth-explicit`、`thm:nfm-mixed-fourth-potential`、`cor:nfm-corrected-fourth-obstruction`、`thm:nfm-fourth-algebraic-correction`。

**全 n≥3 の split 族では正の Kuznetsov 比較が得られる。** 任意の固定 λ∈C、`1+λ³≠0` と滑らかな純中心三次 G に対し、`Hcorr=g_λ+G+s²Hess(g_λ)/24` は、固定入力Bの MF 移送・相対 window・固定標的への有限降下・coherent 飽和性の下で、元の残余圏と rotation・指定三次周期を保つ同値をある有限拡大上に与える。正規化した Hesse 係数は `ν=[λ+s²(4+λ³)/12]/[1−s²λ²/4]`、tensor の尺度は `s(1−s²λ²/4)` となる。この split 族の全次数同値は従来の補正 Φ に対する結果である。一般混合係数では Φ に対する四次の marked 障害があり、Φ^[4] への修正で残余三次の一致を mod h⁶ まで得た。一般混合係数の有限式 Φ^[4] そのものへの全次数同値は未証明である。一方、内在的に復元した X_res への比較は、上述の固定入力の下で稠密開の有限 étale 被覆上に構成した。

一般の滑らかな三次に対して、`3 ≤ n ≤ 7` では Jacobi スキームが Grassmann 錐に等しい。`n=8`、すなわち `N=n+2=10` では、整数行列の証明書から全次数の差
`J₁₀/I_F ≃ C(−2)^330` を決定した。冪零根基は頂点に支持される長さ330の二乗零イデアルで、頂点の極大イデアルで消え、socle 全体に等しい。Hilbert 級数は Grassmann 環のものに `330t²` を加えたものであり、この平方零拡大は次数付き代数としても頂点の完備局所代数としても分裂しない。この八次元の結果は、既存の一般三次の被約分類に依存しない。

非零分解可能点では Hessian の共通核 `K` により横断切片を記述した。Thom–Sebastiani 直和の Jacobi スキームの retraction を用いると、全ての `n≥11` について、非零 Poisson 点の局所環と射影 Jacobi スキームに、任意の二元の積が零となる330次元の冪零部分空間を持つ滑らかな特殊三次を構成できる。周囲の冪零根基全体が二乗零であるとは主張しない。

全次元の一般三次では、既存の被約分類を用いると、非零部分と射影化は Grassmann のものに一致し、`n≥8` の冪零根基は頂点に支持される有限長加群となる。`n≥11` では次数三にも非零部分があり、最高次数と頂点の極大イデアルによる消滅指数は次元によらず一様に有界ではない。`n=9,10` の全 Hilbert 関数や、一般次元での冪零根基自身の積は引き続き未決定である。

Jacobi 行列の普遍的な階数上界は Gesmundo–Landsberg の Koszul flattening の既知の結果に対応する。`N=9,10` の二次行列の最大階数の達成も Boij（1999, Remark 6）の apolar Betti 計算に対応し、独立した新規成果として数えない。現行稿はこの対応を明示し、計算証明書を再現可能な独立検証として保持する。正確な参照箇所は [参考文献](papers/references.tex) と [研究ノート](notes/research_notes.md) に記す。

通常 Artin 基底上の残余圏の一次切断変形は `n ≠ 4` で幾何的変形として認識できる。四次元の categorical hull は22次元、幾何的変形は20次元。全 intrinsic 成分の一般対象の局所表示、比較核の元の stack への降下、全 Abel 形式近傍の完成は主張していない。新規性の網羅的確認・外部査読は未完了。

## 再生成

必要な環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、xr-hyper、etoolbox、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）、Python 3・NumPy・SymPy、および C++17 対応コンパイラ（GCC または Clang）。PDFと検証用の中間ファイルは `build/` に生成し、Gitでは追跡しない。

リポジトリのルートで実行する：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 computations/verify_point_poisson_obstruction.py
python3 computations/verify_mixed_pi_center.py
python3 computations/verify_mixed_character_ext.py
python3 computations/verify_mixed_center_geometry.py
python3 computations/verify_mixed_commutative_candidate.py
python3 computations/verify_mixed_central_direction.py
python3 computations/verify_mixed_two_dimensional.py
python3 computations/verify_mixed_two_dimensional_ext.py --zero-example
# 普遍式を有理関数体上でも再生成する場合（数分程度）
python3 computations/verify_mixed_two_dimensional_ext.py --universal
python3 computations/verify_two_block_structure.py
python3 computations/verify_multiblock_twists.py
python3 computations/verify_multiblock_point_line.py
python3 computations/verify_multiblock_hesse_phase.py
python3 computations/verify_multiblock_isogenous.py
python3 computations/verify_center_hessian.py
python3 computations/verify_geometric_corrections.py
python3 computations/verify_active_invariants.py
python3 computations/verify_active_sign.py
python3 computations/verify_picard_obstruction.py
python3 computations/verify_fivefold_plane_degree.py
python3 computations/verify_poisson_correction.py
python3 computations/verify_cubic_covariants.py
python3 computations/verify_mixed_fifth.py
python3 computations/verify_fourth_potential.py
python3 computations/verify_jacobi_rank.py --verify computations/jacobi_rank_certificate.json
python3 computations/verify_jacobi_vertex.py --verify computations/jacobi_vertex_certificate.json
python3 scripts/build_papers.py
```

`python3 scripts/build_papers.py` はLuaLaTeXとlatexmkで三稿を組版し、他稿の定理番号付き参照を整える。出力は `build/nc-cubic.pdf`、`build/cubic-moduli-descent.pdf`、`build/mixed-sklyanin-cubics.pdf`。SyncTeXも同じ `build/` に置く。`python3 scripts/check_sources.py` は三稿の入力・引用・ラベルと他稿参照を検査する。VS CodeのLaTeX Workshopも三稿組版のレシピを使う。量子化の再現手順は別repoの [再現入口](https://github.com/uedakazushi/cubic-quantization/blob/main/computations/quantization/README.md) と検証資料を参照する。

補助ノートを単独で組版する場合は、repoルートで次を実行する。PDFは `build/notes/` に出力される。

```sh
latexmk -lualatex -outdir=build/notes notes/relative_construction_obstacles.tex
latexmk -lualatex -outdir=build/notes notes/central_cubic_generic_smoothness.tex
```


点障害、Jacobi・Hessian 補正、境界 MF と低積の計算資産を保持する。各検証器の実行・厳密証明書・原稿点検・組版・表示確認の状態は [検証範囲](notes/validation.md) を参照する。有限計算による恒等式確認と、全次数の平坦性、同型延長、Brauer 類、圏同値、Kummer 降下の証明は区別する。

active 不変量の検算は rψ=ar、判別式・Jacobian の公式を有理係数で確認する。active符号の検算はQQ(ζ)上のHesse群の24要素・閉性・不変量・二次指標と、体次数の消去式を確認する。有限対角によるPoisson対の近傍延長・同変降下とχ_actの消滅は、この計算ではなく本文の証明による。幾何学的一般ファイバー、全次数混合三角性、正確な一般次数18は本文の証明に依る。中心・Hessian と幾何補正の検算は有理係数の記号恒等式、八次自由代数の trace、Jacobi 商の双対証明書、普遍 cofactor 恒等式と Hesse の j 差を再現する。補正検算では十個の独立係数を持つ三変数三次、任意の対称行列、二パラメータ Hesse 中心の係数変換、混合項の復元行列、九重被覆の分岐、Weyl の整数重複度と四次不変式も確認する。混合五次の検算は保存した73項の graph データから β,γ を評価し、四次 potential の検算は中心 symbol の全係数恒等式・純中心項・尺度・全次元の非消滅証明書を確認する。入力論文の混合中心公式の非可換中心性、graph 積分そのもの、圏同値はこれらの記号計算で再検証しない。組版設定は既存の repo ルート基準のパスを維持し、PDF と SyncTeX を `build/` に揃える。研究hubの現行テンプレートと設定を参照した共通preambleを使い、LaTeX Workshopの三稿レシピと出力先を合わせる。

原 graph データから抽出・規約も再検証する場合は、[出典と SHA-256 を記した JSON](computations/data/harmonic_linear_products.json) の `star5.txt` と `kontsevich_2_k.txt`・`weights_kontsevich_2_k.txt`（k=1,…,5）を同じディレクトリに置き、次を実行する。通常の検算は保存済みの必要項だけで完結し、外部データ取得は不要である。

```bash
python3 computations/verify_mixed_fifth.py --source-directory build/harmonic-source
```

この追加検証は元ファイルの hash、頂点置換の符号、自己同型群の位数を調べ、全73項について `star5 の係数/2^k=raw weight/|Aut|` を照合する。取得元の全データや外部文献PDFを現行一式に複製しない。

証明書の再生成も可能である：

```bash
python3 computations/verify_jacobi_rank.py --generate build/jacobi_rank_certificate.json
python3 computations/verify_jacobi_rank.py --verify build/jacobi_rank_certificate.json
```

`--generate` の前に `build/` を作成する。二次行列の生成と保存済み小行列の検証は別のコード経路で行い、法32003で非零の整数行列式を用いる。

八次元の頂点構造の検証は、整数係数の Jacobi 式を法2で計算し、次数三の縮約写像の全射性を保存済み小行列で確認する。標数二の三次多項式を解釈する主張ではなく、整数行列の階数下界を特性零へ移す証明である。検証時には約450 MBの行列を `build/jacobi-vertex/` に再生成し、直接消去のメモリ使用量は約220 MB、所要時間は約1〜2分（環境依存）。大きな行列は追跡対象に含めない。いずれの検証にも浮動小数点による近似判定を用いない。

作業規約は [AGENTS.md](AGENTS.md) を参照。正本はこのリポジトリの main とし、現在のソースと証明に必要な計算資産だけを保存する。
