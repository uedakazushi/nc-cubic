# Clifford 変形・判別・固定切片

2026-11-24 / v93。混合稿の具体構成と次の計算の正本。

[研究ノート入口](research_notes.md) · [研究方針](../00_research_plan.md) · [検証範囲](validation.md)

## 現状と計算法

両Cliffordの双方向十八変数では、周囲のAS-regular領域が正確にresultant開D(Δ)となり、その原点近傍に実残余族・局所perfect核を得る（`ifb:cor:exact-regular-locus`, `ifg:cor:local-comparison`）。二つのτも動かす二十変数族は、各分離点で幾何的20次元形式変形空間を与える（`ifv:thm:versal`）。実étale chartを有限化することで、係数空間の非空開の有限étale被覆上の比較、一般係数体の有限分離拡大上の比較、三次四様体モジュライの稠密開の実現まで得る（`ifv:cor:generic-comparison`）。混合尺度は一般の異なるClifford因子でも三乗を決定し、残る比はθ³=(τ₁³−1)/(τ₂³−1)という非自明な三次被覆で記述する（`ifm:thm:scale-cubes`, `ifm:cor:kummer-scale`）。一方向族の固定切片での二次・三次項は、反転を保つ実核を選んだ場合に未計算の4+8係数へ還元した（`ifj:thm:twelve-coefficients`）。他方、階数一の双方向スライスにはAS正則域内の残余A₂特異点があり、D(Δc)全体を残余smooth locusとすることはできない（`ifd:thm:residual-a2`）。全smooth係数への同じ核の延長と全intrinsic被覆は未解決である。

**一方向Cliffordの上位曲率模型で再利用できる計算法。** 全9係数U、V=0の相対Koszul複体でPBW実x次数を濾過すると、s正次数の変形微分δ_sはx次数を2以上下げる。分離原点の二因子細分次数を保つspecial contraction h₀から、固定内部次数N>0でh_s=h₀Σ_{r≤⌊N/2⌋}(−δ_s h₀)^rを**有限**に計算できる。既存のH,Gを保持したP₃→P₄のJはh_{3,s}^{(6)}(wI−Gd₃)とすればよく、原点線形作用のサイズ1120×315・rank280（x次数別0,18,72,100,72,18,0）、次段のrank120,21がKoszul完全性から決まる。s₂,s₃も同じ収縮で帰納的に指定でき、内部次数を忘れた源32|32曲率MFの有限算法になる（正本：混合稿`ifj:lem:filtered-koszul-contraction`, `ifj:prop:shamash-fourth-finite-formula`, `ifj:cor:finite-shamash-source-mf`）。これは基本摂動補題とShamash高次homotopyの既知理論のClifford-PBW規約での有限化であり、一般原理を新規成果と扱わない。実PBW行列の全成分、原点S₃×S₃ゲージとの一致、相対period、Ku比較Homのspecial retract(i,p,h)を得たわけではない。選択した模型の第三中間成分について280独立行・列と全20列の有理 PBW 証明書を得た記録がある（`ifj:prop:third-middle-certificate`）。次は残りの中間成分と高次 homotopies の実構成である。ただし反例の圏論的独立監査と成立可能領域の特徴付けを優先する。出典はCrainic, *On the perturbation lemma, and deformations*, arXiv:math/0403266, Theorem2.3; Eisenbud–Peeva, *Minimal Free Resolutions over Complete Intersections* (2016), §§3.4,4.1。

第三中間成分の具体的な検算は [検証範囲](validation.md) の `ifj:prop:third-middle-certificate` の記録を参照する。

## 変形・判別と比較

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

有理数係数例はτ=2、Λ=M=−6E₁₁であり、h=−527、c=196、両行列式−16、横Hessian行列式2401となる（`ifd:ex:rational-a2`）。これによりD(Δc)全体を残余smooth locusとする可能性は排除される。二次形式の退化部分まで含めた正確な残余判別式、norm三次への実Ku核は未構成である。このsource自体は非smoothなので、滑らかなnc cubicの可換実現可能性を論じる反例ではない。

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

### 階数一の中心 norm の全特異判別

正本は [interfactor_clifford_rank_one_fullnorm.tex](../papers/sections/mixed/interfactor_clifford_rank_one_fullnorm.tex) の `ifn:thm:four-discriminants` と `ifn:cor:off-axis-azumaya`。既存 rank-one の二つの Clifford 行列式から、6平方変数の norm は P(X,Y)+α₁²τ₁²(X₂³+X₃³−3k_xX₂X₃)−α₂²τ₂²(Y₂³+Y₃³−3k_yY₂Y₃) に分解する。横方程式の解は各組で零か (kζ,kζ²)（ζ³=1）なので、四つの binary cubic F_{ε,δ}=P−εα₁²τ₁²k_x³+δα₂²τ₂²k_y³ の判別式の積が零という条件が、射影中心 norm hypersurface が特異であるための必要十分条件となる。元の `ifq` の三尖点四次曲線は (ε,δ)=(0,0) の軸枝だけを検出する。

τ₁=τ₂=2、a₁=a₂=1、λ=0、μ³=−196 では h=49・c=196・Q/α₁⁴=−2000、点 [X₁:X₂:X₃;Y₁:Y₂:Y₃]=[28/(13μ):0:0;1:5/13:5/13] は軸外の特異点で、det(q_x)=det(q_y)=−(28/(13μ))³≠0。Y₁=1 での規格化 4N/196 の 5変数 Hessian determinant は12902400/2197≠0、従って通常二重点。Azumaya chart の既存非proper・非smooth移送を適用できる。再現コード [verify_clifford_fullnorm.py](../computations/verify_clifford_fullnorm.py)。**確定範囲は中心 norm の全特異係数集合であり、残余dg smooth locusの全判別ではない。** 非Azumaya層・各因子間の交叉、全smooth係数への核比較は残る。

### 一方向rank-oneの一般二因子判別と特別なMilnor型

正本は[一般一方向判別の定理](../papers/sections/mixed/interfactor_clifford_oneway_discriminant.tex)（`ifod:thm:general-values`, `ifod:thm:generic-nodes`, `ifod:prop:collision-types`）。Λ=sE₁₁、M=0、t=τ₁、u=τ₂、a=α₁²、b=α₂²、g=(u³−1)(u³+8)²/(27u⁶)とおくと、ρ₀δ=27btu²g^δ/(4a)、ρ₁δ=−bu²(t³−1)²(t³+8)g^δ/(4at²)。中心norm超曲面の特異係数は正確に ∏(s³−ρ_{εδ})=0。周囲AS正則性h=(1−t³)(1−u³)≠0、中心三次普遍正則性c=at²/4≠0は全sで成立し、特異点ではdet q_y=−u²g^δ/4≠0・det q_x=(b/a)det q_y≠0ゆえ射影Azumaya。既存ifqの点対象・coherent飽和の論法から残余非smoothが従う。逆向きの全残余smooth判定ではない。

t³≠−2,u³≠4なら特異点は全て通常二重点、各枝の節点数は3^{ε+δ}。通常の六変数cubic判別多項式をsへ制限すると、非零定数倍を除き∏(s³−ρ_{εδ})^{3^{ε+δ}}（次数48）。ρの交差一致時は異なる節点が同じfiberに入るが点は合流しない。t³=−2（標準HesseのFermat）またはu³=4（中心normの横Hesseの三次特殊化）ではD₄（Milnor数4）へ合流。両特殊値では四変数Fermat三次のsuspension（Milnor数16）であり、通常節点1+3+3+9の保存を説明する。いずれも指定比較核の高次Hesse係数とは別。有限計算の正本は[verify_clifford_general_oneway.py](../computations/verify_clifford_general_oneway.py)。

#### τ₁=τ₂=2 の正確な12値と全局所証人

正本は[階数一normの判別定理](../papers/sections/mixed/interfactor_clifford_rank_one_fullnorm.tex)の`ifn:thm:symmetric-probe`。τ₁=τ₂=2、a_i=1で、四つのbinary cubicの判別はそれぞれ(λμ−4)²Q₀₀、−(λμ−8)²Q₀₁/27、−(λμ−8)²Q₁₀/27、−(λμ−16)²Q₁₁/19683に分解する。二乗因子は非Azumayaの臨界点、四つの残余Q因子にはそれぞれAzumaya通常二重点の証人がある。Λ=sE₁₁、M=0では全sでh=49,c=196。中心normが特異となるのは(s³−54)(s³−56)(s³+196)(27s³+5488)=0の12係数で、その各fiberのノード数は1・3・3・9。全てAzumaya。原点から離れたこの判別式だけでは、原点の固定Hesse多項式切片での12個の高次比較係数は決定できない。必要なのは実Bockstein・比較核の高次移送。検算入口は[verify_clifford_symmetric_discriminants.py](../computations/verify_clifford_symmetric_discriminants.py)。

### 最小四probeのcurved PBW摂動と三次HPLへの有限還元

正本は [interfactor_clifford_jets.tex](../papers/sections/mixed/interfactor_clifford_jets.tex) の `ifj:prop:pbw-jet-degree`、`ifj:lem:pbw-hpl`。1〜3添字のCliffordで q23=−τ₁X₁/2+sL₁/2, q13=−τ₁X₂/2+sL₂/2, q12=−τ₁X₃/2+sL₃/2（L_a=Σ_b U_abY_b）。8つの順序PBW基底の全64組の積の非線形項は q12 q23 に由来する4つだけで、源m_s=m0+s m1+s² m2のm2はこの4出力に−L₁L₃を掛けたもの。ω_x=e123−q12e3+q13e2−q23e1なので中心w_s=w0+s w1は全probeで厳密に一次。最小四方向 E00,R0,C0,I3 のうち E00,R0 の2つはm2=0、C0,I3の2つはm2≠0（固定した順序PBWでの性質）。

**曲率付きPBWのHochschild障害が四つの積成分で消える（証明済み、`ifj:prop:pbw-curved-mc`）：** 変形q_ij(s)=q_ij(0)+sd_ij（d12=L3/2,d13=L2/2,d23=L1/2）の8基底積m=m0+s m1+s²m2に対し、∂m1=0、∂m2=m1∘m1、m1∘m2+m2∘m1=m2∘m2=0。m2は四つのPBW出力枠に−L1L3を持つ。二次障害の具体証人は(m1∘m1)(e2,e3,e12)=L1L3·1で、E00,R0では零、C0,I3では非零。中心ω_x(s)=ω0+sω1について[ω0,−]m0=0、[ω1,−]m0+[ω0,−]m1=0、[ω1,−]m1+[ω0,−]m2=0、[ω1,−]m2=0。`../computations/verify_clifford_curved_pbw_mc.py`はm0,m1,m2を全8×8基底で構成し、全512 triple×5次数、中心4次数、80非零障害枠、四probeを厳密10群PASSで確認した。一般Cliffordの結合律・中心性は既知だが、この規約での4-slot原始と非零証人を具体化した。原点Koszul--Shamash比較のspecial retract(i,p,h)はこの普通のHochschild積複体とは異なり未構成；46原式・12比較値も未計算。

**Clifford augmentationのS₃厳密同変Shamash源模型（証明済み）：** 正本は[混合稿節](../papers/sections/mixed/interfactor_clifford_explicit_shamash.tex)の`ifj:prop:clifford-explicit-shamash`。τ(τ³−1)(τ³+8)≠0のSklyanin S(1,1,τ)でd₁=(x₁,x₂,x₃)、d₂の対角τx_i・非対角x_k、d₃=d₁ᵗを固定。Ωτ=2(1−τ³)ωのs₁=(u,A,uᵗ)、s₂=vはΔ=τ³−1、κ=(4−τ³)/6に対しu_i=−Δ(2x_{i+1}x_{i+2}+τx_i²)/3、A_{ii}=−τ³x_i²/2−τ²x_{i+1}x_{i+2}、A_{i,i+1}=τx_{i+2}²+κx_ix_{i+1}、A_{i+1,i}=−τx_{i+2}²−κx_{i+1}x_i、v=−τΔ(τ³+8)Σx_i³/18。これで4×4 MF(D₊,D₋)は両積Ωτ I₄。巡回ρ:x_i→x_{i+1}と反転σ:x→−Px（P=(12)交換）を厳密に保つ。Koszul各段へのσの行列は(T₀,T₁,T₂,T₃)=(1,−P,P,−1)、F⁰,F⁻¹への行列はdiag(1,P)、diag(−P,−1)で、σ(D₊)=E₀D₊E₁⁻¹、σ(D₋)=E₁D₋E₀⁻¹。S₃のρ³=σ²=1・σρσ=ρ⁻¹を厳密に満たす。最上線−1は可換側反転Pのdet=-1と同じ符号だが比較kernelsのcoherenceは別。s₁²のx₁⁴成分はτΔ(τ³+8)/18≠0。中心scalar aではs₁→as₁、s₂→a²s₂。二因子原点は32|32外積。新計算15群PASSの現行コードは`../computations/verify_clifford_explicit_shamash.py`、3頁の独立組版抜粋を点検済み。**これは非可換源側の有限模型であり、混合D(s)、比較Hom特殊収縮(i,p,h)、unit/counit、rotation三乗整合、46原式/12比較値は未構成。** さらに九変数一方向混合族にはS₃×S₃作用（`ifj:lem:mixed-clifford-s3-family`）があり、係数Λ_{ab}は行列のπ₁(a),π₂(b)へ写り、二次関係・中心曲率w_Λを厳密に保つ。原点32|32の同変sourceを用い、同変なn−1次MF jetの延長方程式が可解なら、そのn次解を36元のReynolds平均で同変に選択できる。しかし解の存在・比較kernelの同値性は導かない。現行`../computations/verify_clifford_family_s3.py`で全九係数のGram・volume・中心不変性、群関係を8群厳密検算。次はこの同変構造を保つHom成分・混合微分の可解性と有限係数計算を優先する。

**双方向CliffordのKoszul全微分・Frobenius基底（証明済み、`ifj:thm:mixed-koszul-frobenius-upper`）：** 6生成元・15二次関係のd₁,d₂、18係数上の三次syzygy全20列の大域自由基底d₃（xxy9,xyy9,最上2）は`ifj:prop:mixed-koszul-endpoints`と`ifj:thm:mixed-koszul-full-third`。K₃自由性は全係数PBW B₃階数56と20×20単位小行列に依存し、resultant零でもsyzygy自体は大域自由。二次双対E=D^χの次数二はq^x_a=u_{a+1}u_{a+2},q^y_b=v_{b+1}v_{b+2},q^c_{ab}=u_av_bの15基底、次数三はm^{xxx}=u₁u₂u₃,m^{yyy}=v₁v₂v₃,m^{xxy}=q^x_av_b,m^{xyy}=q^y_bu_aの20基底（旧d₃双対と厳密一致）。Δ_res≠0でγ=2^-6det(∂g_i/∂z_j)を用いたt(γ)=1のFrobenius積対合によりK₄≅E₂、K₅≅E₁、K₆≅E₀を自由基底化。右Koszul規約でd₄の全成分はΣ_j z_j t(mν ζ_j q_r)、d₅はΣ_j z_j[q_r](ζ_jζ_i)、d₆は六生成元列となる。**これは全300成分を全十八変数で展開したのではなく、正則開の有限係数抽出算法。** 新しい`../computations/verify_clifford_mixed_koszul_frobenius.py`ではτ₁=τ₂=2、s=1、U₁₁=V₁₁=1、残り零の正則双方向点でγ=33u₁u₂u₃v₁v₂v₃、d₄の一成分y₁/33、旧d₃全20列一致、d₃d₄=d₄d₅=d₅d₆=0をB₂の21独立PBW成分で厳密確認（新12群＋依存d₃の9群PASS）。全係数の定理は既知のFrobenius完全対合とKoszul構成から証明。**次の一手は、構成済みの一方向s₁:P₁→P₂(3)を使い、d₃s_{1,2}+s_{1,1}d₂=wI₁₅を解くこと。さらにP₃–P₅とs₂以降を構成する。** それを折り畳む混合32|32MF、比較Hom特殊収縮(i,p,h)・unit/counit・rotation/三乗period・46原式/12高次係数は未構成。resultant零での基底延長と全解消完全性も未主張。

**九変数一方向Cliffordの一次Shamash s₁の二つの中間成分（証明済み・厳密計算）：** 正本は`ifj:prop:mixed-shamash-first-middle`（H:P₁→P₂）と`ifj:prop:mixed-shamash-second-middle`（G:P₂→P₃）。V=0, Λ=sUで中心w=w_x(s)+w_yを分け、全係数相対Koszul完全性とdeg x=(1,0),deg y=(0,1),degΛ=(2,−2)を用いると、d₂H+u d₁=wI₆、d₃G+Hd₂=wI₁₅をともに**s二次以下で解ける**。P₂の基底x第一次数0,1,2、P₃の基底は0,1,2,3なので、G^x係数の第一次数≤5、G^y≤2が二次上限を強制。さらに`ifj:cor:mixed-shamash-entire-first-degree-bound`でP_i→P_{i+1}(3),0≤i≤5のs₁全成分も二次以下に選べることを抽象的に証明（上段の実係数は未計算）。τ_i=2,a_i=1では旧Hの336×315階数210の右逆を保持し、d₃のPBW係数作用D₃:(B₂)^20→(B₃)^15を**840×420、階数336**として六細分ブロック[6,54,108,108,54,6]の小行列で正確に分裂。R=wI₁₅−Hd₂のPBW係数は0次・9一次・45二次のみ（3・4次は厳密零）。D₃=D₃,₀+s∑U_aD₃,₁,aを用い、G₀=T₃R₀、G₁,a=T₃(R₁,a−D₃,₁,aG₀)、G₂,ab=T₃(R₂,ab−D₃,₁,aG₁,b−[a≠b]D₃,₁,bG₁,a)を全15列で厳密構成。**165三次単項式×15列×840成分の和が全て零**、四最小probeと任意の追加整数Uを使った15×15の非可換積直接検査もPASS。`../computations/verify_clifford_mixed_shamash_second_middle.py`は新9群＋依存H7群PASS、保存コードblobと実行blob一致。構成したGの疎成分数G₀=118/G₁=482/G₂=334は固定ピボットのゲージ依存で不変量ではない。**次の具体計算はd₄s₁,₃+s₁,₂d₃=wI₂₀を同じ有理数PBW分裂で解くこと。** その後P₄–P₅とs₂以降。混合32|32MF、実Ku比較kernel・Hom(i,p,h)・unit/counit・rotation/period・46原式/12高次値は未完成。

原点s進curved bar模型 d_s=d0+s d1+s²d2 と原点収縮 (i,p,h), d0h+hd0=1−ip を選ぶと、三次移送の増分は s p d1 i+s²p(d2−d1hd1)i+s³p(−d1hd2−d2hd1+d1hd1hd1)i+O(s⁴)。従って必要な源摂動演算はd1,d2のみで、二つの線形probeではd2=0かつd1²=0。これは移送「微分」の演算式であり、Hesse切片のβ・γを直接与えるものではない。現行の次の実計算は、既存の原点perfect核・Shamash縮約・Picard/rotation周期から(i,p,h)を実際に取り、同じJacobian切片へ高次積まで移すこと。自由な標的再座標化でβ・γを消す操作は採用しない。再現は [verify_clifford_jet_transfer.py](../computations/verify_clifford_jet_transfer.py)。既知のHPLはGugenheim--Lambe--Stasheff (1991)と区別する。

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

最小の計算入口は、E₀₀、第一行和R₀、第一列和C₀、I₃という四つの一変数族Λ=tAである。[t²]v₀₀の評価行列式は−1、[t³]z_iの不変式評価行列式は1で、`ifj:prop:minimal-probes`と`ifj:eq:probe-table`から十二係数を回収できる。四つの三次不変式の係数回収には最低四方向、さらにPBWの二次摂動を持つ方向が最低二つ必要なので、選択は両下限を達成する。各制限では中心持上げ・実核から三次までの可換側原式を取り出す必要があり、normや点曲線の形式だけを比較方程式と見なすことはできない。固定切片への射影と座標正規化自体は次の明示公式で処理する。

**Jacobian 切片の構成的正規化（証明済みの有限代数）：** `ifj:prop:explicit-jacobian-projector` は h_i=(2+τ_i³)/(3τ_i), t_i=3a_iτ_i, r_{i,a}=Z_{i,a}²−h_i Z_{i,a+1}Z_{i,a+2} により、全56三次単項式を固定20単項式の射影Πと36次元のJacobian方向への明示的な右逆𝒥に分解する。純三乗の射影は h_iP_i、純重複二変数 Z_{i,a}²Z_{i,b} (a≠b) は0、混合重複 Z_{i,a}²Z_{j,b} (i≠j) は h_i Z_{i,a+1}Z_{i,a+2}Z_{j,b}。その他の切片単項式はそのままである。Jacobian 方向は係数 t_i と (1−h_i³) の有理式で解け、Π+𝒟_F𝒥=1、𝒥𝒟_F=1 が成立する。これは原点比較核の存在・形式的変形の幾何化とは独立な多項式線型代数である。

`ifj:prop:explicit-third-normalization` は原式 F+sG₁+s²G₂+s³G₃ について座標補正 T=I+sA₁+s²A₂+s³A₃ を三次まで再帰的に構成する。各段階のJacobian 成分を A_j=−𝒥(R_j) で消し、切片係数を H_j=Π(R_j) とする。一次項が既に C にある場合でも H₃=Π(G₃−D_{𝒥(G₂)}G₁) であり、G₃ を単独で射影してはいけない。実際、純代数的な例 G₁=X₀Y₁Y₂,G₂=X₀²Y₀,G₃=0 は、正規化後 H₃=−P_Y/t₁ を与える（`ifj:ex:third-coordinate-artifact`）。これは未計算の γ の実値ではない。局所計算では全56単項式の一般記号分解、20単項式基底、τ₁=2,τ₂=3での三次座標代入、非零三次補正の4群を厳密確認した。`computations/verify_hesse_slice_transfer.py` はその再現器である。実際の比較核と周期から原式 G₁,G₂,G₃ を計算する部分が残る。

**四probeの直接読出しと必要な原式係数の縮小（有限代数の証明済み）：** `ifj:prop:direct-probe-readout` は、一次項を `G_{1,A}=κΣA_{ab}X_aY_{b+1}Y_{b+2}` に固定した任意の三次式族から、二次・三次の固定Hesse係数を特定の単項式係数だけで回収する。二次`v00`は`[X1X2Y0]G₂+h₁[X0²Y0]G₂`、純X三次は`[P_X]G₃+h₁Σ[X_a³]G₃`、純Y三次は`[P_Y]G₃+h₂Σ[Y_b³]G₃−κ/t₁ΣA_ab[X_a²Y_b]G₂`（`t₁=3a₁τ₁`）である。四方向に要する原式の単項式係数枠は、二次14、三次32、計46。純X三次の二次座標補正はbidegreeで消え、純Y三次には明示的な対合補正がある。従来の四probe評価行列を逆に解けば12係数となる。全56単項式×4方向について一次項が指定の状態でこの読出しを厳密に確認した（4群PASS、検算器`verify_hesse_probe_readout.py`）。原点核から必要な46枠の実値を求めたわけではなく、未知の12係数の消滅・非消滅も未解決である。

**中心 norm からの数値代入が失敗する具体的理由：** Clifford の中心体積元は `ω_x(s)²=−N(s)`、`N(s)=det q_x(s)` を満たす。混合行列Uに対し `L_a=Σ_bU_abY_b` とすると、`N₂=−(1/4)Σ_a X_a(L_a²+τ₁L_{a+1}L_{a+2})`、`N₃=L₀L₁L₂/4` が全係数で正確に成り立つ。固定Hesse射影では `Π(N₂)=−(1/4)Σ_ab(∂𝒮/∂U_ab) X_aY_{b+1}Y_{b+2}`、`Π(N₃)=(1/4)(∂𝒮/∂τ₁)P_Y` で、`𝒮=(h₂/3)I₀+2I_r+τ₁(h₂I_c+I_d)`、`I_d=I_++I_-`。これらは中心normの**同じ三次不変式に由来するgradientの整合条件**であり、`β,γ`への等式ではない。四probeでは三次normが E₀₀,R₀で零、C′₀でY₀³/4、I₃でP_Y/4。Fermatの場合h₂=0ならC′₀のHesse射影が零でも中心normの三次恒等式は非零。さらに平方中心変数を文字どおり可換座標とすると `Π(N₁)` はC₂₁、実比較のKSはC₁₂で二重次数が異なるため、この素朴な座標同定は一次で失敗する。N₀の滑らかさも `(τ₁³−1)(τ₁³+8)²` によって確認できる。証明は `ifj:prop:central-norm-jets`, `ifj:cor:central-norm-probes`。有限検算器は `../computations/verify_clifford_central_norm_jets.py`（SymPy 7群PASS）。原点perfect核・Picard/rotation周期の実高次移送と46枠の数値化が引き続き必要。

**Clifford中心判別と点曲線の二重isogeny（証明・検算済み、一般機構は既知）：** 点曲線E_τ=V(f_τ)、o=(1:−1:0)、p=(1:1:τ)∈E_τ[2]に対し、分離中心判別D_τ=(1−τ³/4)P_X−(τ²/4)ΣX_a³=(τ³/8)f_{−2/τ}となる。E_τ→E_{−2/τ}への次数2 isogeny φ_τ をWeierstrass座標で構成し、ker φ_τ={o,p}、双方向合成[−2]、三捩れ基底(P,Q)上のdiag(1,−1)を示した（`ifj:thm:discriminant-two-isogeny`）。一般にはj(E_τ)≠j(E_{−2/τ})で、τ=2が有理数の具体例。φ_τ*O(1)=O(2)⊗M_τ、M_τ=O(p−o)非自明二捩れ（`ifj:cor:isogeny-picard-line`）。これは既存の分離 Picard–rotation 比較核に現れるMと同じ。通常の二次斉次座標式だけでは不足する理由を偏極の引戻しで説明するが、この幾何的isogenyは実Ku比較核・指定周期の高次移送ではなく、46原式係数・12個のβγは未計算。一般のHesse/Cayleyan二重isogenyはOudompheng Proposition2.5とMoodyらの既知理論として扱い、本稿はClifford中心係数と固定三捩れ標識への特殊化・明示計算を保持する。再現は `../computations/verify_clifford_hesse_two_isogeny.py`、GitHubで保存した同一ソースを独立に再取得して8群PASSを確認。

**theta交換子と線束の二重障害（証明済み）：** 二重isogeny φ:E_τ→E_{−2/τ}、L=O_E(3o)、M=O_E(p−o)、A=φ*O(1)=L²⊗Mに対して、E[3]上のtheta交換子はe_A=e_L²=e_L⁻¹。標識付き三捩れを恒等とみなし中心μ₃も恒等に保つ三次元intertwinerは零となる。二重被覆の直像はφ_*O_E=O_{E'}⊕N（Nは標的の非自明二捩れ線束）で、H⁰(E,A)=H⁰(E',O(1))⊕H⁰(E',O(1)⊗N)の3+3。deck±固有空間はいずれも逆中心文字のSchrödinger型。注意すべきは、通常二次式Sym²H⁰(E,L)≅H⁰(E,L²)も中心文字はe_L²なので、反転`だけ`は二次表示を排除しないこと。決定的なのはHom(L²,A)=H⁰(M)=0という線束の障害（`ifj:prop:two-isogeny-theta-characters`）。τ²=−2のCM点ではφ²=[−2]、j=8000、End(E)=Z[√−2]。これは自己isogenyとして使える厳密な試験点だが、Mは非自明のままで、高次比較係数の数値は出ない。保存済み`verify_clifford_hesse_theta.py`は三捩れ行列・intertwinerのrank9・6=3+3・二次文字・CM条件・j=8000を6群で検算。実核のdeck作用と比較周期を併せて計算するのが次の課題。

**isogenyの基点付き三次模型（証明・検算済み、正本 `ifj:prop:two-isogeny-cubic-sextet`）：** 点曲線E_τを線型座標W=3τ(Z0+Z1)+(2+τ³)Z2、T=cτ(Z2−rτW)、S=cτ(Z0−Z1)で厳密にWS²=T³+aWT²+bW²Tへ移す（a,bは既存Weierstrass係数、b≠0）。接線Wの零因子は3o、T/Wの零因子は2pで極は2o。三次式W²T,W²S,WT²,WTS,T³,T²Sの共通基点因子はD=2o+pで、これを除いた六切断はφ*O(1)のH⁰(E,A)。deck対合は(u,v)=(T/W,S/W)について(u,v)↦(b/u,−bv/u²)、線束の正規化作用D(g)=u⁴g(b/u,−bv/u²)/b²である。±の三次元固有基底は本文`ifj:eq:cubic-sextet-eigenspaces`、正側のG0=WT²,G1=T³+aWT²+bW²T,G2=S(T²−bW²)から標的Weierstrass・Hesse座標を得る。次数9の全多項式恒等式`ifj:eq:cubic-sextet-nine-identity`により三次式が標的を定めることを検証し、反転Z0↔Z1とも両立する。負固有線束Nはdual isogenyの核p∨からO(p∨−o∨)=M_{τ∨}と特定できる。これらは前段の楕円線型系の有限入力であり、まだ実MF/window比較核・period/homotopyの高次転送も46原式係数も得ていない。再現コード`../computations/verify_clifford_isogeny_cubics.py`は一般記号での座標式・6×6行列・次数9恒等式と、τ=2,−1での標的Hesseへの厳密割算など8群PASS。

**相対被覆代数と二捩れPicardの有限MF（正本：混合稿`ifj:prop:double-cover-algebra`, `ifj:prop:two-torsion-matrix-factorization`）：** K上でR=K[X,Y]/(Y²−Xg(X))、B=K[ξ,η]/(η²−g(ξ²))、X=ξ²、Y=ξη、g=X²−2aX+δ、δ=a²−4b=(τ³+8)³/(81τ)と固定する。B=R⊕I、I=(X,Y)、I²=(X)、積ij/X。源Weierstrassの(u,v)からξ=v/u,η=u−b/u、逆u=(ξ²−a+η)/2を明示。粗いR[√X]の二捩れ点は通常二重点で、整閉包の第二生成元ηが不可欠。源・標的の各三次F=Y²Z−X(X²+αXZ+βZ²)で行列A=[[Y,−G],[-X,YZ]]、B=[[YZ,G],[X,Y]]、AB=BA=F·1、余核ideal(X,Y)の層O(−p)。次数零Picard MはO(o)の一点捩れが必要で、O(1)=O(3o)の整数shiftでは代用不可。標的符号線束を源に引き戻すとBezout恒等式η²−ξ²(ξ²−2a)=δで自明化するがdeck符号が残る。保存コードは11群PASS、SHA-256 `6143d5813f4bb4ca580faa6f060fda855074c998b0961d5060111abd29180091`、Git blob `e5be2c4fa7d07cd0b1f2b503b462a049445a3b40`。これは既知の二捩れ被覆・行列分解の機構の具体化であり、実nc Ku核・rotationと三乗周期・高次12数値を計算したものではない。

**相対二重被覆のtrace/Casimirと有限Hochschild収縮（証明済み）：** K上のδ=a²−4b、g=X(X−2a)+δ、R=K[X,Y]/(Y²−Xg)、I=(X,Y)、B=R⊕I。R²→Iの分裂からP_I=δ⁻¹[[-X(X−2a),−Y(X−2a)],[Y,g]]、P_I²=P_Iが得られ、B≃Im diag(1,P_I)⊂R³は階数2有限射影。B⊗_R BのΘ=(η_1η_2−(X−2a)ξ_1ξ_2)/δはΘ²=1、対角/反対角に±1で、e+=(1+Θ)/2は乗法μのB-bimodule sectionとtrace pairingの双対Casimirを与える。任意のB-bimodule Mの相対Hochschild cochainsにh f=(1/2)f(1,-)+(1/(2δ))[η f(η,-)−(X−2a)ξ f(ξ,-)]を用い、dh+hd=1（正次数）、HH_R^{>0}(B,M)=0。一般の有限étaleとHH消滅は既知機構であり、本研究の貢献はClifford相対表示の局所化を用いない射影行列・Casimir・hの具体式（`ifj:prop:cover-trace-casimir`, `ifj:cor:cover-hochschild-contraction`）。形式a(s),b(s)ではδ(s)逆数を三次まで一意に展開してP_s,e_sを得る。Artin切断の有限étale持上げの同型一意性はStacks 58.8.3 Tag 0BQBを直接確認。有限計算器`../computations/verify_clifford_cover_trace_casimir.py`はSymPyの射影恒等式・trace・相対HH n=1..4（対称および非対称双加群）・形式三次摂動を9群検査。GitHub保存済み検算器そのものをローカルへ復元して独立実行し、SymPy1.14で9群PASS・終了コード0、保存済みGit blobと実行ファイルのGit blob SHA `88028e6b66ef2fefb29d60d7b1462f16a0bd422f` の一致、SHA-256 `d97be70dfb3539cf06078c9c200048753318f7f2b980ec960569adb33301eb38`を確認した。相対被覆のhをcurved Koszul–Shamash比較のHPL hと混同しない。Picard O(o)一点捩れ・非可換曲率・rotation/periodと実比較核・46原式係数・12scalarは未完成。

**Picard二捩れの直接対称3×3 MF・二乗評価（証明済み、一般理論は既知）：** Weierstrass F=Y²Z−X³−aX²Z−bXZ², o=(0:1:0), p=(0:0:1)に対しL=[[X,Y,0],[Y,aX+bZ,X],[0,X,−Z]]は対称、detL=F、adjLも対称でL adjL=F I₃。coker(O_P²(-2)^3→O_P²(-1)^3)はM=O_E(p−o)であり、前の2×2 MF余核O(-p)から必要だった一点捩れO(o)が直接MFに組み込まれる。M(1)=O(p+2o)の相対3切断はs=(-v,1,u), u=X/Z,v=Y/X、関係uv²=u²+au+b。その3関係が行列Lの列。M²の同型をdiv(u)=2p−2oに従ってuの乗法で固定すると積の行列はQ=-adjL=[[X²+aXZ+bZ²,−YZ,−XY],[-YZ,XZ,X²],[-XY,X²,Y²−aX²−bXZ]]という厳密な2次式行列。反転Y↦−YにD=diag(−1,1,1)でL(-Y)=D L(Y)D、adjでも同じ。元HesseのW,T,SでdetL(T,S,W)=4cτ² fτ、第二MF微分=(4cτ²)⁻¹adjLで追加三乗根なし。源(α,β)=(a,b)・標的(-2a,δ)両方で相対。形式a(s),b(s)のMF係数も直ちに定まるが四混合probeではτ_i一定なのでこの一因子Picard MFはs-定数。従って非可換混合PBWと比較核を通さずには12係数を得られない。正本は`ifj:prop:picard-symmetric-linear-mf`, `ifj:cor:picard-symmetric-hesse-family`。既知の一般理論の一次資料はBeauville (2000) Props3.1,4.2、Buchweitz–Pavlov (2024) Theorem Aと§2.21を確認。検算器`../computations/verify_clifford_picard_linear_mf.py`はローカルSymPyで10群PASS。前述の被覆相対HH収縮と、このMFの自己双対、実Ku核のHPL収縮はすべて異なるデータである。

**対称3×3 Picard MFから二重被覆の符号積へのアフィン接続（証明済み、正本 `ifj:prop:picard-affine-bridge`）：** Z=1でx=X/Z, y=Y/Z, g=x²+αx+β, f=y²−xgとし、T=[[1,0,0],[0,1,x],[0,0,1]]を用いるとTLTᵗ=S⊕(−1)、S=[[x,y],[y,g]]、T^{-t}adj(L)T^{-1}=−adj(S)⊕(−f)。coker S→I=(x,y)は(r,s)↦yr−xsの同型で、以前の2×2理想MFとアフィン上で一定基底変換で等価。β単元のときI²=xA、xは非零因子、I⊗²→A、rs/xは規格化M²評価を−x倍のセクション同定により再現する。標的二重被覆B=R⊕Iの符号積がこの評価と同じであり、反転y↦−yにも両立。x^{-1}不要。TはZ=1限定なので大域斉次MFの同値でもO(o)一点捩れの消去でもない。curved KS kernel、比較unit/counit、rotation/指定周期、46原式・12高次係数は未構成。`../computations/verify_clifford_picard_affine_bridge.py`の厳密8群PASSは行列・積の恒等式検算であり、高次圏同値の証明ではない。

任意の標的形式座標変更なら全高次項を消して(κΛ,0,0)へ移せるが、これは固定した多項式切片の係数を計算したことにはならない（`ifj:prop:formal-straightening`）。一方、一次部分が恒等の同変な源座標変更の最初の補正は四次なので、上の二次・三次係数は変わらない。形式座標に関するこの区別を計算時にも維持する。

**残る具体課題と到達基準。** 第一に四制限について原点のreal perfect kernelから周期付き収縮と可換側の原式 G₁,G₂,G₃ を求め、明示された四probe通算46枠（G₂の14枠・G₃の32枠）を抽出し、`ifj:eq:direct-twelve-readout` の逆評価で十二係数を決定する。第二に階数一のD(h)内で、Azumaya norm特異点と二次形式退化部分を分けて残余smooth locusの方程式を調べる。A₂例は除外すべき係数を既に与えるが、全判別式ではない。第三に、構成済みの有限étale比較被覆がどの残余smooth係数まで延長できるかを実核のperfect性と同値性で判定する。尺度θの三次被覆だけから全核の降下を結論しない。一般の非Clifford第一因子の尺度、任意の複数ordered pairの同時積分、全intrinsic表示被覆も残る。

有限計算の入口は `verify_clifford_morse_scale.py`（随伴行列・moment・三乗尺度）、`verify_clifford_rank_one.py`（h・norm局所式・Hessian・有理係数例）、`verify_clifford_jets.py`（全低次同変空間・反転・最小四制限・Hesse補空間）である。いずれも厳密な有限代数計算であり、実核・coherent飽和・指定周期・高次十二係数の数値を機械検証したとはしない。実行と組版・保存の状態は `validation.md` を正本とする。

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

## 固定切片の十二係数：具体的な着手手順

**固定切片の十二係数から、最初の非零値を実計算する。** `ifj:thm:twelve-coefficients` の標準Hesse方程式・Jacobian線型切片・反転同変原点核・指定周期を固定する。`ifj:eq:probe-table` の四つの一変数probeに沿って、逆向き混合成分の二次四係数と純因子成分の三次八係数を求める。まず構成済みの原点4×4 Shamash模型（`ifj:prop:clifford-explicit-shamash`）の二因子32|32外積を基準とし、九変数係数へのS₃×S₃作用（`ifj:lem:mixed-clifford-s3-family`）と最上syzygy線の符号を固定したまま、既に構成したd₁–d₃の全係数基底とresultant正則開のd₄–d₆ Frobenius自由行列（`ifj:thm:mixed-koszul-frobenius-upper`）、曲率端点uを使用し、**選択した一方向九変数模型では s₁ の前三中間成分（P₁→P₂、P₂→P₃、P₃→P₄）を構成した記録がある。第三成分 J の20列は `ifj:prop:third-middle-certificate` の証明書（280独立行・列、係数次数0/1/2の非零項122/516/450）を用いる。次は残る中間成分・s₂以降の higher homotopies を実係数で解いて**混合32|32微分とHomの有限special retractを**解の存在から**構成する。九変数では係数軌道1/4/10を利用する。可解な各次数の補正は群平均で同変化できるが、非可解な障害を除去できるわけではない。その上で `ifj:prop:pbw-curved-mc` の曲率付きMC恒等式を固定して `ifj:prop:pbw-jet-degree` の2つの厳密線形源変形と2つの二次源変形に対して、分離原点の有限Koszul--Shamash比較核から実際の収縮(i,p,h)を固定し、`ifj:eq:pbw-hpl` の二次・三次の演算と必要な高次積・unit/counitを評価する。得られた可換側の原式G₁をまず固定切片に正規化し、その後は `ifj:prop:direct-probe-readout` の二次14・三次32（四probe通算46）の単項式係数だけを原式G₂,G₃から抽出して十二係数を取得する。全三次式を展開する必要はないが、純Y三次のκ/(3a₁τ₁)対合補正 `ifj:eq:direct-jet-observables` を必ず入れる。`ifj:prop:central-norm-jets` の明示中心normは、一次KSでC₂₁とC₁₂を取り違えるため、原点核の高次出力を得る代用品としない。判別楕円との二重isogenyにはM_τ=O(p−o)が不可避で、theta中心文字も反転する。±三次元固有空間・逆中心文字と原点比較のPicard線束・rotation・指定周期を保持して高次移送を構成する。最初の有限座標入力には`ifj:eq:cubic-sextet-basis`の六つの基点付き三次式・6×6 deck作用に加え、`ifj:prop:double-cover-algebra`のR⊕Iと`ifj:prop:two-torsion-matrix-factorization`の両側2×2 MFを使う。実比較核のwindowへ移す際、O(−p)のO(o)一点捩れ・deck符号・最上Koszul線・rotationと三乗周期を同時に追跡し、通常の整数次数shiftで一点捩れを代用しない。 有限被覆側には`ifj:eq:cover-picard-idempotent`と分離Casimirを保持する。Picard線束を実核へ入れる一次的な入口として`ifj:prop:picard-symmetric-linear-mf`の直接の対称3×3 MFと、随伴行列で規格化したM²の評価を優先する。これにより2×2 MFへ別途O(o)を作用させる処理を減らせるが、これは可換一因子に限る。四混合probeではこのMFはs-定数なので、有限被覆/因子Picardの単独微分では46原式係数は得られない。今後は実Koszul–Shamash模型で混合PBW曲率のm1,m2と原点特殊収縮(i,p,h)、comparison unit/counit、rotation・三乗periodを具体構成する。相対HH収縮とKu比較のHPL用hを同一視しない。通常の二次多項式による中心平方座標化を代用としない。一般一次尺度には `ifm:thm:scale-cubes` と選択したKummer枝を使い、同一因子・同一重みでは交換同変尺度を固定できる。自由な標的形式座標で高次を消して数値計算の代用とせず、非零値を得たら核・周期・座標依存を明記する。十八・二十変数の方程式の具体化はこの固定切片で進める。

**比較核のKummer三枝を選び、因子moduli上の降下を調べる。** θ³=(τ₁³−1)/(τ₂³−1)の有限étale三重被覆は非自明であり、有理的な大域sectionはない。`ifv:lem:moving-split-kernel` の実相対核におけるPicard線束、三捩れ補正、周期の三乗根と、`ifm:cor:kummer-scale` の各枝を対応させる。尺度torsorだけから全標識付き核のgerbeや、その中立化・最小比較次数は結論しない。一般係数の有限étale比較は構成済みだが、比較三次族と核の元の係数空間への大域降下は残る。

**残余smooth locusの境界と核延長を調べ、全intrinsic対象へ進む。** 九変数の全係数AS/CY、十八変数の正確な周囲正則域D(Δ)、二十変数の形式完全性・モジュライの稠密開・一般係数の有限étale比較は既知の入力とする。rank-oneの一般一方向判別はD(Δc)内部にも残余非smooth点があることと、その特異値・節点重複度・D₄合流を明示した。まず `ifd:thm:residual-a2` の中心chartとunit/counit defectを使い、実際のsmooth域・境界での核延長を調べる。一般の複数ordered pairの高次障害、既存O-marked認識と表示被覆を調べ、全smooth係数の比較とintrinsic対象の認識は、成立可能クラスを特徴付ける課題として継続する。

関連する正本：`ifq:thm:axis-discriminant`、`ifq:thm:tricuspidal`、`ifq:ex:rational-a1`、`ifr:cor:central-extension`、`ifv:rem:generic-scope`、`ifk:prop:geometric-fixed-part`。
