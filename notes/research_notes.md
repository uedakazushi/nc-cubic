# 非可換三次 n-fold：現行研究ノート

2026年11月21日 / v24。研究方針は `../00_research_plan.md`。証明全文は現行論文に置き、このノートは依存・適用範囲・障害・再現の入口をまとめる。

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
| γ_scの形式像と未計算の算術 | W_act=b_hJ_g、b_h≡1からγ_scの完備体への像は[b_h⁻¹]=1。未知の線型lift尺度は三乗として消えるが、元のk_nでγ_scが零かは未計算。従ってこの規格化での周期標識の最小次数三／九は未決 | `prop:nfm-period-phase-formal-active-scalar` |
| 周期位相の二変数不変量体への降下 | 全n≥3の正準強化classの γ_sc,n は混合係数に依存せず、active 十係数体、さらに C(s,t)、s=c₄(g),t=−c₆(g) へ一意に降下。値と次元間の一致は未計算。全full class共通性はn=3,4に限る | `prop:nfm-adjoint-period-all-dimensions`, `cor:nfm-adjoint-period-marked-minimum` |
| 周期位相の条件付き境界判定 | torsor が A²から ΔD=0 のみを除いた開へ有限 étale に延びるという追加仮定の下で候補は1,[D],[D]²。さらにDの一般点でも非分岐なら1。他の分岐の排除は未証明 | `lem:nfm-period-two-boundary-criterion` |
| Hesse 境界の有限残余模型 | 点線束の相対行列を代数的 trait 上の有理式で構成。指定方程式・target 周期を保つ選択した integral 残余模型と、全nの点線束・右射影・有限MFを得る。特殊 fibre の滑らかさや模型の正準性は主張しない | `lem:nfm-hesse-boundary-explicit-line`, `prop:nfm-hesse-boundary-integral-residual-model`, `prop:nfm-boundary-right-projection`, `lem:nfm-boundary-line-mf` |
| 三次元境界の低 orbit Hom | 内部次数0,−1,−2,−3のHomは自由で底変更と可換。target周期t_pはprimitive。m₂/m₃、Ω_pの原始性、source格子と表示比較、位相値は未計算 | `prop:nfm-boundary-threefold-low-hom` |
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

研究方針の主目標は、各既約成分の一般 O-marked moduli、point scheme、Poisson moduli への射、同じ X の Kuznetsov 成分との比較である。固定良好模型間の全 Hom 比較は対象の局所表示を与える定理ではなく、一ブロックの商 stack を構成することと全成分の一般対象を覆うことは分ける。各型の一般点で入力を確認し、複数ブロック型を一ブロックへ無条件に還元しない。

点商関手、shift のグラフ、中心射影は、全 O-同値の局所次数付き持上げを用いて局所一ブロック型の O-marked stack 上へ降下する。圏全体の次数一 shift を大域に選んだという主張ではない。定常成分 D と楕円成分 E は一般族の研究対象であり、E をモジュライの boundary と取り違えない。

Poisson 射は、正規化 trace と尺度付き Hessian から量子中心三次 w に古典 Casimir H_w を対応させることで構成した。滑らかな X_w=V(H_w) 上の tensor は一意な強い affine lift を持つため、lift を補助標識として保持せず、非零分解可能な三次 Poisson 対と偏極類のモジュライを標的にできる。良い開では逆構成があり、Msm≃Pgood となる。実際の相対 O(1) と偏極類は区別し、Brauer–Severi ambient を許す。この同型は指定した trace–Hessian 処方についてのものであり、Ku と整合する唯一の逆量子化を意味しない。

残余圏の復元が与える X_res と、trace–Hessian 射の X_TH は一致するとは限らない。全 n の split Hesse 族では、固定入力の下で幾何学的一般ファイバーの射影非同型を証明した。同じ周囲 Π の三次 Casimir を選び直しても解消しない。座標不変な代数的補正 Φ は全 O-同値へ降下し、一般次数9と楕円点曲線との厳密な一致を持つ。split 族では Φ の三次への残余比較を入力Bの下で得る。一方、一般混合係数では残余四次項と tensor の五次項を決定した結果、Φ の三次との標識付き比較にも四次障害が残ることが分かった。この障害を打ち消す別の代数的射 Φ^[4] を構成し、固定 harmonic-angle 模型の三次を mod h⁶、tensor を mod h⁷ で再現する。Φ と Φ^[4] の厳密な性質を混同しない。

一般混合係数の残余三次は低 rotation 積の有限行列から代数的に復元でき、全 O-降下する射影 Poisson 射と同じ X の Ku への有限被覆上の比較を得た。点微分から T² の標準切断を得て、符号商残余射の一般次数は正確に18となる。全次数の混合三角性により active 逆像と反対操作以外の有限分枝を排除し、標準二重被覆の符号障害を active 不変量体上の一つの二次類 χ_act へ帰着した。有限対角による同変延長を三捩れ対称点の近傍へ構成してχ_act=0を証明した。半古典規格化したfull射は次数9、反対同変であり、共通稠密開でM≃Z×_Y P_Yとなる。

比較核については、active 制限の最高次 cohomology が次数零線束となる非空な型を構成し、full kernel class 選択後の scalar index を split 表示上で3の約数へ抑えた。点型 m_P=p_res の非空性は相対THCR/window1から得られ、一般 split 係数体では I_sc の分裂と実 Sklyanin 支配族により δ_C(p_res)=δ_E(p_pt) の period と index が正確に三となる。最高次線束の点型は、κ_nc=j_nc^!O[1]、q_Y=Li_C^*|Ku(Y) という表示を通じて、良い一ブロックの共通稠密開へ全O-降下する。

さらにn=3,4では幾何的full自己同値群が、元の体上のT=ρ⁻¹[1]で生成される定数無限巡回群となる。これによりfull classの第一段階が解け、全classのscalar gerbeが同じexact index三を持つ。従ってこの二つの次元では任意の実際のfull核が元の体と三に素な有限拡大上に存在せず、周期同型を標識しない比較の最小体次数は三である。全n≥3では随伴復元条件を満たす非空な強化点型を取り出し、そのclass層を有限H_p-torsor S_pへ縮約した。全n≥3の一般一ブロック族ではTate–Koszul忠実性によりH_p=1、S_p=Spec(k_n)となり、強化型classは唯一で未標識最小実現次数三となる。全full classの分類は含まない。

指定MF周期のcoherenceから、n=3,4の追加のμ₃位相も全classで共通となる。位相に適合する方程式の相対規格化を選べば標識付き最小次数三、標的に独立尺度を付した一般族では正確に九である。source の Ω と唯一の φ_sc は target 方程式の cube frame を与える。全n≥3の正準強化classの位相 γ_sc,n は混合係数に依存せず二変数不変量体 C(c₄,−c₆) へ一意に降下するが、その値と次元間の一致は未計算である。形式像は一である。裸のO-marked対の障害と独立尺度の障害を混同しない。全nの標準三分点torsorの最小点定義次数九も、これとは別の構成である。非分裂の n≡1 mod3 では点障害の index 九を実現し、表示安定化子が自明な共通開では全該当次元の強化点型で未標識最小次数九を達成した。同じ例のrotation軌道の最小は三、n=4では全型の最小も三である。n=5 の半 rotation は平面に依存せず実核へ降下し、O≃ρ⁻¹[1]、ε≃id と同定した。γ_sc の算術的計算と coherent 中心線型性、任意 full 核への高次元の拡張は別に残る。

完備中心係数商の比較は構成できたが、その coherent な相対構造の代数的降下は別に必要である。最高次線束による指数評価はこの降下を前提とせず、active 比較自体や点 shift と Ku rotation の比較では引き続き有用な課題として残る。有限 jet を順に増やすこと自体は主経路にしない。二次・四次の混合比較障害は marked な形式比較の結果であり、unmarked な一般ファイバーの反例へ無条件に拡張しない。必要な有限係数拡大、rotation・三次周期、同値核の降下は保持する。一ブロックの良い開と Poisson 側の支配成分に関する成果を、全 intrinsic 圏成分の一般対象の被覆へ外挿しない。

general の稠密 Zariski 開、幾何学的一般点、very general の可算例外除去を区別する。very general な同値の存在だけでは、代数的な族の射や同値核の降下を得ない。まず関数体上の構成とその定義体を調べ、有限表示等の必要条件を確認して稠密開へ広げる。n=4 の幾何 locus と n≡1 mod3 の rotation 問題は、general を仮定するだけでは解決しない。

## 2. 入力研究の正確な範囲

`nc-cubic` の固定 commit は `eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59（いずれも2026年11月14日）。

- 論文A `poisson_geometry.tex`：`prop:pg-represent` の bivector 表示、`prop:pg-jacobi-extension` の affine Jacobi 延長、`thm:pg-normal` の複数 Jacobian ブロック正規形、`cor:pg-generic` の一般三次における被約 Grassmann 錐。全次元の一般 Jacobi スキームの有限長冪零根基を論じる際には最後の被約分類を使う。二次方程式の不足、n=8 の長さ330の定理、およびその直和から作る特殊三次の非零冪零例は、この被約分類に依存しない。
- 論文A `general_dimension_universal_quantization.tex`：`thm:pg-all-dimensions`, `prop:pg-ad-relative-chart` が中心量子化の入力。一ブロック相対 PBW 開と中心三次束の存在は、この研究稿と Etingof–Ginzburg の既知の構成から取る。今回その全証明を独立に再検証したわけではない。
- 論文A `papers/support/papers/sections/hesse_mixed_universal_center.tex`：`thm:pg-universal-hesse-mixed`、`eq:pg-hm-coefficients`、`cor:pg-hesse-hessian-form`、`eq:pg-hesse-hessian-closed` が全混合中心元と Ψ_λ(F) の有限公式。固定 commit の本文を直接確認し、四次係数を I,J と純中心項へ書き直した恒等式を厳密検算した。中心公式そのものは入力であり、今回の可換記号計算を非可換中心性の再証明と呼ばない。
- 論文B `generic_recovery/main_result.tex` 等：既に全 n≥3 が対象。C[h]_(h) 上の次数別有限自由な中心三次対が、多項式環と滑らかな三次式へ特殊化する場合を扱う。一般点の coherent 残余模型は rotation と指定三次周期を保つ。方程式は C(h)、同値核は有限拡大上という区別を守る。全パラメータ・任意の nc cubic・核の基底体への降下を自動的に含まない。
- 同論文Bの `cft:thm:complete`, `cft:lem:model`, `cft:lem:center`：選んだ formality と厳密同型 φ に対し、残余 potential は W=C_π^(-1)φ(w) である。W mod h=F は W=F を意味しない。`gcd:thm:field-model` は幾何的な可換模型の存在を得た後の方程式の関数体への降下であり、h=0 での正則性や同値核の同じ体への降下を自動的に与えない。`gre:prop:input`, `gre:prop:hesse-normalform`, `gre:thm:exact-potential`, `gre:prop:jet` の split Hesse 公式を全 n の比較例に用いる。固定標的への一般点比較には `rog:lem:localization`, `rog:lem:descent` を使い、線束生成部分から全 coherent 残余圏へ移るには `crs:prop:residual-smooth`, `crs:thm:coherent` をさらに使う。これらの未公表入力の全証明を今回独立に再検証したとは主張しない。
- 同論文B `papers/generic_recovery/curved_transport.tex` の完備比較は N≥3 を対象とし、`cft:lem:arity`, `cft:lem:flow`, `cft:eq:bound`, `cft:eq:t-weight`, `cft:eq:insertions`, `cft:eq:two-block-matrix` を直接確認した。これに対し `window.tex` の節全体は N≥5 を仮定する。三変数の active 比較は相対 bar 写像の中心係数還元で構成し、一般点生成・window 定理を n=1 へ流用しない。三変数の相対 a=0 比較・proper Hom・Laurent 底変更には `papers/generic_recovery/explicit_example.tex` の `gre:prop:elliptic-quotient`, `gre:lem:elliptic-mf` を用い、正則 DVR と滑らかな active 曲線という仮定を確認した。剰余体と rotation の具体式は Galinat の同じ window1 に統一する。
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

### 一般係数の残余三次を代数的な族へ広げる

証明は `residual_algebraic.tex`。入力Bの体上の可換模型存在・方程式の定義体降下は既知入力であり、ここでは相対的な方程式直線と全 O-同値への降下を構成する。

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

を用いる。p=q=1 の場合は滑らかで scalar symmetrizer を持ち、従って一般の p,q でも同じ性質を持つ。σ=diag(1,ζ,ζ²;1,…,1) はこの族を保つ（`lem:nfm-cyclic-scalar-witness`）。入力Aの普遍 Hesse 中心式と固定入力Bをこの族自身へ適用すると、K=C(p,q)(h) 上に残余 active 曲線 C_σ と点曲線 E_σ が構成できる。残余側では σ が Hodge 微分を固定し、非零の K-有理三捩れ平行移動を与える。点側の全三捩れは K-有理であるため、j≠0,1728 上の Jacobian-Isom の二次 twist は自明となる（`prop:nfm-cyclic-test-sign-split`）。

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

未知の線型lift尺度λ_hは三乗として消え、b_hは1を特殊化値に持つ一意な形式三乗根を持つ（`prop:nfm-period-phase-formal-active-scalar`）。F'=hFで一般係数体へ戻す際にも、source中心元とW_hの両方にhが掛かるため、この比へ余分なhは残らない。しかしKのKummer類から完備体への写像は単射とは限らない。例えば1+hはk((h))では三乗だがk(h)では三乗でない。b_hの代数性もここでは主張していない。したがって**元のKでのγ_scと、その成分体上のαのindexはなお未計算**であり、この規格化の標識付き最小次数三／九は未決である。

この形式像だけでは元の体の値を決められないが、次の混合定数降下によって計算を二変数不変量平面へ移せる。別経路として実際の移送済み MF の微分・射と source の AS-Gorenstein trace 規格化を比較する。Murfet の residue trace は potential の係数だけから比較 scalar を得る公式ではなく、Serre 基底線 D_Y≃det U⊗λ_res の同定も指定 fractional Calabi–Yau 自明化との一致を代替しない。

このμ₃-torsorはscalar G_m-gerbeとも標準三分点torsorとも別である。標準九次体L₉には三次中間体がないので、T_ηが非自明ならL₉でも周期標識を選べない。三分点正規化がperiod図式を保持するのは、既に標識を含めたclassを選択済みの場合だけであり、underlying classの規格化から未選択の周期標識は得ない。三分点の最小次数九・Galois閉包216から周期標識の最小次数を推論せず、scalar gerbeの最小次数三からμ₃位相の消滅も推論しない。全intrinsic moduli上の標準class、任意の非分裂体でのexact index、coherent中心線型性を得たとは主張しない。

### 周期位相の混合定数降下と二変数不変量への帰着

全n≥3の正準な随伴復元点型classを固定する。n=3,4では全full classにも共通する半古典 cube frame の周期位相は、active 十係数体 \(k=\mathbf C(g_\alpha)\) を通り、さらに一意な

\[
 \overline\gamma_n\in\mathbf C(s,t)^\times/\mathbf C(s,t)^{\times3},
 \qquad s=c_4(g),\quad t=-c_6(g)
\]

から来る（`thm:nfm-period-phase-active-descent`、`prop:nfm-period-phase-invariant-descent`）。主証明は [周期位相の降下の節](../papers/sections/residual_period_descent.tex)。**類の具体値と次元間の一致は未計算である。** 二変数への帰着を周期標識の消滅と読み替えない。

核心は \(k(m)((h))\) より小さい体 \(\kappa(m)=k((h))(m)\) 上の実際の周期付き CF 比較である。mixed/pure-center 係数 m=(b,ℓ,d) の重みを1,2,3、active 座標の重みを零、中心座標の重みを−1と取る。内部次数・有限基底の重みを固定した MF 行列では、各 monomial の混合重みは \(D+w_j-w_i\) 以下となり、h の次数や微分の挿入回数に依存しない。逆 flow の各係数は有限個の m 単項式上で h 進収束するため、単なる k[m][[h]] ではなく k[[h]][m] に属する（`lem:nfm-period-flow-mixed-bound`）。

可換側の三つの Koszul stabilization を逆 CF で移し、固定された integral 有限対象の Hom 比較を局所化する。有限 cone と直和因子は pretriangulated hull・冪等完備化の普遍性で扱い、h の負冪を持つ新しい Maurer–Cartan 元へ無限挿入公式を再評価しない。proper Hom と window の実際の局所化、および固定入力の三対象生成を使って \(\kappa(m)\) 上の full Morita 比較を得る（`prop:nfm-period-comparison-mixed-rational`）。この比較は形式拡大後に随伴復元の非空性証明で使った同じ完備CF核となる。全Taylor成分・hullの一致を確認した上で、最高次線束、Picard等式、正準随伴射のconeの消滅を忠実な体拡大から反映できるため、全nで唯一の強化classを実現する（`lem:nfm-period-mixed-comparison-adjoint-type`）。従ってそこで \(\gamma_{\rm sc,n}=1\) となるので、有限 étale 定数降下を二回用い、F′=hF による同時尺度変更も追って混合係数を除く。単に大きい完備体で三乗根が存在することだけでは、この降下は得られない。

不変量体への次の降下では、Kummer 類が SL₃ 不変というだけでは足りない。線型 lift f と周期解 η の組に

\[
 (f,\eta)\longmapsto(\lambda f,\lambda^{-1}\eta),\qquad
 F_{\lambda f}=\lambda^{-3}F_f,\quad c_{\lambda f}=\lambda^3c_f
\]

という実際の作用を入れ、商として coherent な μ₃-torsor を作る。核の scalar は Hom 直線上で相殺するので、表示変更の合成もこの torsor へ降下する。一般 SL₃ 安定化群 H_g の可換化は元の三次 V(g) の Jacobian の三捩れ J_g[3] であり、全 SL₂(F₃) モノドロミーから K 有理な character H_g→μ₃ は零となる。従って安定化群の作用が自明で、Fisher の一軌道の一般ファイバーを用いて商 gerbe から C(s,t) へ降下する。active 係数体が不変量体上正則であることが一意性を与える。

**境界を絞れた場合の候補は三つ。** \(\Delta=s^3-t^2\)、
\(D=1-s/24-t/216-s^2/6912\) とする。torsor が
\(U=\operatorname{Spec}\mathbf C[s,t,1/(\Delta D)]\)
へ有限 étale に延びるという**追加仮定**の下では、U の UFD 性と Kummer 列により類は [Δ]^a[D]^b と書ける。半古典代入 (s,t)↦(h⁴s,h⁶t) で Δ↦h¹²Δ、D≡1 mod h となるため、既知の形式的消滅は a=0 を強制する。従って候補は1,[D],[D]²。さらにD=0の一般点でも非分岐ならb=0となる（`lem:nfm-period-two-boundary-criterion`）。

既存の判別式公式 \(\Delta(c_4(J_g),-c_6(J_g))=\Delta(s,t)D(s,t)^3\) により D は点三次の追加判別境界である。しかし、現在の定義開だけから他の branch divisor がないとは言えない。次は二変数平面での分岐範囲と境界付値を計算するか、上の actual trace 比較で類の値を決める。他の分岐を排除せず D の付値だけを調べても結論は足りず、原点の形式 jet を増やして境界の計算を代用することもできない。

### 忠実な Hesse 制限と追加境界の具体模型

K=C(s,t) と Hesse 体 L=C(p,q) の三次 Kummer 核は正確に ⟨[Δ]⟩≃Z/3 である。Galois 群 Q₈⋊C₃ の character の位数三と、Δ(r(p,q))=(−4p(p³+q³))³ から従う。一般 active 十係数体 E/K は正則であり、E((h)) での半古典像1を K((h)) へ戻せるため、この核の非自明な二元は排除される。したがって現在の規格化位相は Hesse 体への制限で忠実に検査できる。Hesse 完備化を先に取ると Δ 自体が三乗なので、この議論は成立しない。主証明は `lem:nfm-period-laurent-constant-injective`、`lem:nfm-hesse-cubic-kummer-kernel`、`prop:nfm-period-hesse-faithful-test`。

D の Hesse 引戻しは八直線の積である。q=2 の一般点で det Dr=−384p²(p³+8)²、Δ=−64p³(p³+8)³ は非零で、分岐指数は一。D=−(p³+8)²(q−2)/27+O((q−2)²)。剰余体 C(p)/C(p³) の次数三を分岐指数と混同しない。追加の二境界非分岐仮定の下ではこの trait の付値が残る D 指数を決める（`lem:nfm-period-hesse-eight-boundary-lines`）。

**active 境界代数。** g=p(x³+y³+z³)/3+qxyz とすると q=2 では zy=−px²/2、xz=−py²/2、yx=−pz²/2。u=−p/2 と置き、S_u=K⟨x,y,z⟩/(zx−uxz,xy−uyx,yz−uzy) の巡回自己同型 τ(x)=z、τ(y)=x、τ(z)=y で a*b=aτ^{deg a}(b) とすれば、この境界代数を得る。例えば z*y=zx=u xz=u(x*x) で、他二式は巡回する。固定入力 A `hesse_mixed_universal_center.tex`, `thm:pg-universal-hesse-mixed` の中心式を h′=p、t=q/p として p 倍すると、Ω=pU(x³+y³+z³)/3+V sym(xyz)、U=1+q²/2+p³q/6−q⁴/48、V=(4−q²)(12q+q³−8p³)/48。q=2 では Ω=p(p³+8)x³/3、J=(p³+8)xyz/3 であり、x^{*3}=u⁻¹xyz より Ω は −2J に移る。

この −2 は C の三乗だが、full 周期位相の非分岐性を意味しない。一般の S_u は可換でなく、active twist を中心変数へ自明に延ばすと次数一中心変数が新積で中心でなくなる。必要なのは一般混合係数を伴う full comparison の実際の周期図式である。

**反対代数の障害。** 反変双対は intertwiner の矢印と rotation の両方を反転するため、正の rotation へ戻す際に scalar weight が元へ戻り得る。したがって反対操作と c₄,c₆ の偶数次数だけから γ=γ⁻¹ は導けない。同じ可換 cubic を source 方程式 F、target 方程式 aF で標識すると、underlying opposite は同じでも周期位相は任意の [a] を持つ。conormal 周期を含む図式を比較する必要がある。

### q=2 境界の三分点と点線束の有限模型

z=q−2、k₀=C(p,m)、R=k₀[[z]] とする。点三次は AΣX³/3+BXYZ、A=p(1−q²/4)、B=q+p³/3+q³/12。P=(1−q/2:−1−q/2:−p) と O=(1:−1:0) はそれぞれ C_X、C_Z の滑らかな点へ落ちる。全空間は三節点で横断微分 −p/3 を持つ正則 split I₃ 模型である。M=O(P−O) の multidegree は (1,0,−1) で、交点行列から垂直 twist で零にできない。一方 M³(C_X−C_Z) は全成分次数零となる。紙上証明は `prop:nfm-hesse-boundary-third-division`。

T=(0:1:−1)、U=(1:−ζ:0) による Kummer 二座標は ([(p³+8)/(2z)],1)。接線比を原点の局所座標で先頭係数一に規格化し、F∘[3] が三乗になることを確認して Silverman XI.9.2 を適用する。従って [3]⁻¹(P) は同じ完全分岐巡回三次体 L=K(∛(2z/(p³+8))) の三つのコピーであり、幾何的慣性型は3³。一般 active 係数へは非分岐な Hesse chart でこの慣性型を移す。一般係数の剰余体上でも三つのコピーに分かれる、とまでは主張しない。

M₀(j) の cohomology は j≥1 で (h⁰,h¹)=(3j,0)、j=0 で零、j≤−1 で (0,−3j)。M₀(1) は `eq:nfm-hesse-boundary-determinantal-line` の行列 L₀による 0→O(−1)³→O³→i_*M₀(1)→0 を持つ。行列式 −XYZ、三節点での階数二、三切断の貼合せを厳密検算した。相対持上げは存在だけでなく、完備化前の DVR R₀=k₀[q]_(q−2) 上の有理式 L=U⁻¹NV で明示できる。b=(p³+8)/3 とすると det L=−F_E/b、L mod(q−2)=L₀、Q=−b adj(L) は LQ=QL=F_E I₃ を満たす。三分点の選択は不要であり、この行列は点関係行列から得た三倍線束とは別で、実際の M(1) を表示する。式と cokernel の同定は [境界の節](../papers/sections/residual_boundary.tex) の `lem:nfm-hesse-boundary-explicit-line` を参照する。

D_R=D(r(p,2+z)) に対し [D_R]=[(p³+8)/(2z)]⁻¹、従って L=K(∛D_R)。Kummer 制限の核は正確に ⟨[D_R]⟩ であり、条件付き候補1,[D_R],[D_R]²はこの被覆上では区別できない（`cor:nfm-hesse-boundary-period-candidates-blind`）。三分点上で周期分裂を仮に示しても、元の D-付値を決定しない。

**指定周期を保つ残余模型。** 一般 fibre の唯一の φ_sc を用いて active 平面を点三次 J_g に合わせ、残余方程式の active 制限を J_g に規格化する。混合係数の極を中心座標の u↦zᴺu で消せば、同じ target 方程式とその MF 周期を保つ integral 平坦模型を、分岐した体拡大なしに選べる。C_res は点曲線の I₃ 模型となり、φ_sc と点線束もこの選択した模型へ延びる。正準性や特殊 fibre の滑らかさは主張しない。全空間は C に沿って正則で、C は中心一次式による regular immersion である。証明は `prop:nfm-hesse-boundary-integral-residual-model` と `lem:nfm-hesse-boundary-transverse-smoothness`。

**全次元の full 残余対象。** r=n−1 とすると、負の line bundle block の右変異 R_O(−1)⋯R_O(−r) により q_Y^RM[1] の相対 perfect 模型を作れる。右端から適用し、最後の [1] を保持する。特殊 fibre が特異でも相対 Gorenstein 双対と有限 mutation は使え、全 Hom 複体は R-perfect となる。これは各 cohomology の平坦性とは別である。さらに F−J_g=Σu_iG_i と相対線型行列から、各 parity の階数3·2^(n−1)の明示 MF を得る。この raw MF が表すのは i_*M(1) の stabilization であり、未指定の window で右射影対象と同一視しない。証明は `prop:nfm-boundary-right-projection`、`lem:nfm-boundary-line-mf`。

**三次元の低 Hom。** n=3 では最初の O(−2) に関する right mutation が零となり、残る一つの coevaluation cone で対象を表示できる。adj(L₀) の成分が平面上の六つの二次単項式を張るので H⁰M(1)⊗H⁰M⁻¹(1)→H⁰O_C(2) は全射である。これと lci Ext、逆 rotation、相対 Serre、指定方程式の MF 周期から次を得る。表にない Ext は零であり、全項が R-自由で閉・一般 fibre への底変更と可換となる（`prop:nfm-boundary-threefold-low-hom`）。

| 内部次数 q | HⁱRHom(Z,ρ^qZ) の非零階数 |
| --- | --- |
| 0 | i=0で1、i=1で10 |
| −1 | i=1で5、i=2で5 |
| −2 | i=2で10、i=3で1 |
| −3 | i=2で1、i=3で10 |

指定 target 周期 t_p は q=−3、i=2 の自由階数一加群の生成元である。Burke–Stevenson の正の Gorenstein parameter に対する Theorem6.4(1), i=1 を用い、相対窓と実際の F-自己交叉周期を合わせた結果であり、一般点の周期同型を無条件に特殊化したものではない。

**残る計算。** target の t_p が primitive でも、m₃ から回復する Ω_p が primitive とは限らない。次は自由な低 Hom の実際の m₂・m₃、二次関係束の階数、Ω_p の原始性、source 側の integral 格子と表示同型を計算する。高次元の同様の Hom 平坦性と、他の divisor の非分岐性も未解決である。極消去を十分強くすると F₀∝XYZ とでき、MF の特殊 fibre は active 行列と (u_i,0) の tensor になるが、この分離を right window を通した積の評価へ使う方法は未証明。三分点の分岐を full 位相の分岐と同一視せず、上記有限模型も full 比較核・Morita 同値・source/target 周期の一致を与えたとは扱わない。

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

証明は `prop:nfm-period-phase-low-products`。orbit 比較は t_Ω↦c(η)⁻¹t_p、反変 Koszul 双対は Ω_p↦c(η)⁻¹Ω となり、既存の γ=[c(η)⁻¹] と一致する。f の変更は次数 scalar なので比は三乗倍だけ変わる。標的方程式の v 倍は t_p を v⁻¹ 倍、Ω_p を v 倍し、γ′=[v]γ と整合する。値が一であることは未証明。

計算では有限分裂体上で実際の M と q_Y^R M[1] を表示し、内部次数 −1,−2,−3 の有限 Hom 模型、合成と contraction を求めればよい。重み零性により関係と最終比は元の体へ戻せる。単に可換側の通常の原点 stabilization に置き換えると二次包絡を誤り、m₃ を零と置くこともできない。coherent な中心線型性の全降下はこの評価式の前提でも結論でもない。

**非分岐性の有限データ判定。** source と回復した対が閉 fibre を含む良い integral 表示を持ち、Ω と Ω_p が直線部分束の生成元なら、指定された K-射影 Isom は有限対角により R 上へ延びる。有限自由生成元加群の射影同型を GL/G_m 完全列と Pic(R)=0 で持ち上げれば fΩ_p=uΩ、u∈R× となる（`lem:nfm-period-integral-presentation-unramified`）。幾何的 Isom の存在だけで K 上の切断を得たとしない。

この十分条件を各 divisor へ適用するには、低 Ext の自由性と底変更、m₃ の integral transfer、関係束の階数、三次 relation の原始性と、回復表示の閉 fibre 条件を確認する。q=2 の選択した模型では n=3 の必要な低 Hom と target 周期の原始性を証明したが、実際の m₂/m₃・回復関係・source 格子の比較は未完了である。一般点の finite perfect spread だけでは、指定した divisor を良い開が横切ることは保証されない。有限行列の minor・Fitting ideal を混合変数の多項式として扱い、共通因子による垂直成分を点検する。

現行の T は σ^j≠1 (1≤j≤max(3,n−1)) を課す。n≥5 では ΔD≠0 にも位数四点の divisor があり、現在の入力保証はそこを除く。これは真の分岐や実中心の跳躍を示した結果ではなく、既存証明の適用範囲の不足である。将来の弱化では、全 O-復元の高次中心条件を要求する代わりに、相対低次数中心・境界評価 ε・滑らかな trace–Hessian 三次から graded Isom を有限な polarized cubic Isom の閉部分へ入れる方法を検討できる。q=2 自体は滑らかな点曲線を要求する既存 good open の外なので、そこへこの補題を直接適用してはいない。

### 次の着手方法：周期境界・coherent 中心作用・全型への拡張

第一に、有限評価式 γ_sc,n=[f(Ω_p)/Ω] の実際の積を計算する。q=2 の明示有理行列・残余 integral 模型・右射影と n=3 の低 Hom の自由性は証明済みなので、m₂/m₃、二次関係束、Ω_p の原始性、source 格子と射影 Isom を調べる。F₀∝XYZ の tensor 分離が right window を経た積へ使えるかを検査する。三分点の完全分岐体上では D の三候補が全て消えるため、元の trait または三に素な分岐指数の模型で計算する。ΔD 外の非分岐性は現在の小位数除外も含めて個別に点検する。n=3 の fractional Serre trace は別経路として保持する。

第二に、一意な強化点型 class を有限代数的核の coherent な中心線型性へ接続する。可換側の q_Y=Li_C^* は source の中心作用を代用しない。全群分類を前提とせず、他の full class については既存の T-軌道と数値中央化群を使う。全次元の H_p=1 と五次元の ε=id は既に確定した範囲である。

第三に、非分裂の全 n≡1 mod3 における強化点型最小九と、rotation による全型の上界三を基準に、他の軌道の K 核と点型を固定した一般体の index を調べる。四次元の指数九族の全型最小三は決定済みだが、高次元には同じ下界をまだ得ていない。共通な良い開の外と全 intrinsic 成分の問題も保持する。

### 比較核の Euler 数値型と scalar index

核の同型類が選ばれた後の G_m-gerbe 上では、試験対象 A_i,B_j に対する混合 Hom は重み1の perfect 複体となり、determinant の重みは Euler 数 χ_ij である。その gcd=d>0 によって dα=0、μ_d による band の縮小を得る。体上では各 cohomology の rank 自体が ind(α) の倍数なので ind(α)|d まで分かる。period と index を同一視していない。

固定入力B `generic_recovery/generic_descent.tex`, `rog:prop:euler` の三次 stabilization の Euler 数は

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

指定周期のμ₃位相はn=3,4の全full classに共通であり、方程式の相対規格化を適合させた最小次数三と、独立なtarget尺度の一般族での正確な九を証明した。元の一般係数体には、唯一の φ_sc・t_sc・source の Ω から target 方程式の cube frame が定まる。各 γ_sc,n の形式像は [b_h⁻¹]=1であり、さらに混合重みを制御した逆 CF 比較と coherent な μ₃-torsor の安定化群作用から、各類は C(c₄,−c₆) へ一意に降下する。類の値、n=3 と n=4 の一致、その成分体上の scalar index は未計算である。二境界に分岐を絞れた場合の候補1,[D],[D]²は、明示した追加仮定付きの結果である。全nの正準強化classにも同じ混合有理CFを適用でき、周期位相と標識付き最小次数三／九が定まる。n≥5で任意full classに位相が共通か、全型の標識付き最小も同じかは未解決である。

高次元のclass問題では、元の体上の実核T=ρ⁻¹[1]を除いたG_ρ/〈T〉-torsorへの縮約と、classとT軌道のGalois安定化群の一致を証明した。奇数次元の数値像は六元群であり、残る群はG_ρ,0/〈[2]〉である。一般三次七様体の既知の球面対象からfull群のZ²とG_ρの無限指数が分かるため、低次元の全群の巡回性を全nへ拡張する方針は取らない。強化点型の正準classにより、点型を含むGalois固定軌道の存在も全次元で従う。他のfull軌道の分類は未決定である。

強いliftのKoszul手法、formalityと中心対応、既知の星積重み・wheel消滅、古典的Hessian写像・Aronhold不変式、残余MF模型そのものは既存入力と区別する。完備中心係数商の比較は選んだ相対flowの直接の補強であり、一般のcategorical base-change定理やその代数化ではない。重み1束からのAzumaya・Brauer–Severi剛性化、Picard gerbe、THCR・Orlov window、三・四次元のFM自己同値群分類、Iliev–Manivelの七次元球面対象、Toën–Vaquiéのboundednessと自己同値moduliは既知の入力である。本稿での最高次線束型、点の平行移動、projector核の一意性を通じたclass降下、指定MF周期のcoherenceとcube frameによる算術、随伴復元条件と有限H_p-torsorへの縮約と分ける。新規性の網羅的確認は未了。全intrinsic成分のモジュライ、特殊族でのPoisson対の延長と低Natの底変更の一致、良い稠密開の外での点型、n≥5の強化条件外の任意full核への適用、元の体でのγ_sc、coherent graded-center比較の代数的降下は未完成である。全refined核でm_P=p_resを示したとはせず、一般次元での有限torsorへの縮約や選択後の規格化を未選択の全同値stackへ外挿しない。

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

- Benoist, *Séparation et propriété de Deligne–Mumford des champs de modules d’intersections complètes lisses*, J.London Math.Soc.87(2013),138–156、[arXiv:1111.1582v2](https://arxiv.org/abs/1111.1582v2)、[DOI](https://doi.org/10.1112/jlms/jds045)：Theorems1.6–1.7（著者稿p.3）。標数零の滑らかな三次では分離・DMであり、有限対角を得る。Poissonの符号商にはtensorを保つ閉条件を加える。
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

指定MF周期の規約は、固定入力B `papers/generic_recovery/local_model.tex` の `lp:prop:sing-period`、`window.tex` の `tw:eq:period-extension` と `tw:eq:rotation-period-square` に置かれている。前者の双加群truncation境界とconormal基底、後二者のYoneda二拡張と実際のrotation比較を照合した。周期の中心的coherenceと生成元変更のu⁻¹則はこの指定規約に関する主張であり、任意に選び直したfractional Calabi–Yau自明化の自然性を仮定しない。

周期位相の混合定数降下では、同じ固定 B の `cft:lem:arity`、`cft:lem:flow`、`cft:eq:bound`、`cft:eq:object`、`cft:eq:insertions`、`cft:eq:two-block-matrix` を使用する。三対象生成と actual Hom の局所化には `gcd:prop:bound`、`tw:lem:proper-hom`、`rog:lem:localization` を用いる。局所化前の integral な有限 MF の Hom を先に比較する範囲を保持し、任意の Laurent 係数 MC 元への収束を新たに主張しない。Fisher の Theorem1.1・Lemma2.2・§9.5 の不変式・一般軌道・Heisenberg 群と、既存の全三捩れモノドロミーを合わせた μ₃-character の消滅が、二変数不変量体への降下に必要である。

Murfet, *Residues and duality for singularity categories of isolated Gorenstein singularities*, Compos.Math.149(2013),no.12,2071–2100、[arXiv:0912.1629v3](https://arxiv.org/abs/0912.1629v3)、[DOI](https://doi.org/10.1112/S0010437X13007082) のTheorem6.2・式(6.6)、Proposition4.2・式(5.7)を確認した。MFの微分と射を含むresidue trace、およびdeterminantの変換則を、γ_scの計算候補として保持する。sourceから移した実際の微分・射とAS-Gorenstein traceの規格化をまだ同定していないため、位相消滅の証明としては用いない。引用keyは `NFMMurfetResidue`。

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

README の再生成手順で、ソース参照、二次・三次の保存済み証明書、LuaLaTeX 組版を確認できる。TeX はルートから実行し、`.latexmkrc` が `build/` を出力先とする。次数三の検証は Python・NumPy と C++17 コンパイラを用い、大きな行列を `build/jacobi-vertex/` に再生成する。証明に必要なテンソル・選択行・検証コードを保存し、再生成できる大行列自体は収録しない。

trace–Hessian の中心係数・八次代数 trace、全次元の KS 例、split Hesse の有理式と j 差、混合係数の二次恒等式についても、README と `notes/validation.md` にある該当手順と確認範囲を参照する。厳密な記号計算による係数検証を、未公表入力の非可換中心性・完備 MF 移送・一般点復元の全証明の独立検証と同一視しない。任意次元・任意基底の主張は、有限個の計算例だけでなく本文の相対証明に依拠する。

混合五次 tensor の再現は `computations/verify_mixed_fifth.py` と必要最小限の重み証明書 `computations/data/harmonic_linear_products.json`、中心逆像の四次恒等式・Jacobi 非消滅・古典的共変式の恒等式は `computations/verify_fourth_potential.py` に収める。両者とも Python と SymPy を用い、グラフ縮約は整数・Fraction、係数恒等式は有理数係数の多項式として厳密に計算する。既知重みの使用、係数恒等式の検算、一般次元の証明、形式証明器による検証は異なる状態として記録する。新たな四次の中心グラフ積分は行っていない。

active 不変量の有限式は、ルートから `python computations/verify_active_invariants.py` を実行して再現する。SymPy の QQ 上で rψ=ar、det Dr、判別式の変換、a と ψ の Jacobian、符号不変性を係数ごとに検算し、数値サンプルには依存しない。本版では同検証器を更新・実行し、境界の明示相対行列、余因子 pairing、tensor MF の曲率恒等式を加えた十五群すべての PASS を確認した。一般ファイバーの幾何学的整性、反対不変性、全次数の有限混合三角性と正確な次数18、符号二次類と twist の構造は本文の一般証明に依存し、有限式の記号計算による証明と同一視しない。三角性・小さい体への射の降下・安定化群の指数二は紙上で独立に点検した。新たな graph 積分や高次 jet の数値計算を行ったという意味ではない。

Hesse 体の二次類単射に用いる有限恒等式は、`python computations/verify_active_sign.py` で再現する。QQ(ζ)、ζ²+ζ+1=0 上で不変量の保存、四元数群と C₃ の関係、群の位数24、次数の上界を与える四次・三次恒等式、非自明な μ₂ 指標の不存在を検算する。全次元の滑らかさの証明に現れる二つの整数の非消滅も確認するが、scalar symmetrizerの全次元の証明、有限対角による延長と同変降下、χ_actの消滅の全論証を計算で代用するものではない。実際の実行結果は `notes/validation.md` を参照する。

最高次線束型の graded purity、PBW の中心平坦性、Tor-independent な MF 係数商、Galinat の同じ window における shift・rotation、cohomology の平坦化と gerbe 上の貼合せは内部で独立に読解した。Picard 障害・active 曲線上の分裂・階数3 Azumaya も紙上の証明による。完備中心切断の bar 恒等式、係数商と relative perfect 性の反例、次数二中心の formality 反例、有限四角の PGL_d 障害、内部次数を忘れた無限 coherence の例、Hom 剛性化はノートの証明で確認できる。実際の Morita 核と curved-bar 模型の同定は未完成であり、条件付き振幅評価と区別する。外部査読・全固定入力の独立検証・形式証明器による機械検証を行ったという意味ではない。

三倍線束の重み・零切断での相殺・底変更と、三分点被覆上の規格化の一意性は紙上で独立に点検した。右 THCR の符号と楕円 rotation の二つの shear、形式恒等核からの graph-support、Picard 等式を保つ有限降下も内部で独立に読解した。これらには別の検算コードを設けず本文の証明を正本とする。指定中心商の相対THCR/window1と閉／一般底変更は本文の証明を執筆担当以外の二担当も読解点検した。一般の特異圏の底変更とは区別する。符号消滅には別に有限対角による延長補題を証明し、特殊点の非自明な慣性を含むC₃同変降下を独立に点検した。

Picard障害と三捩れmonodromyの有限恒等式は `python computations/verify_picard_obstruction.py` で再現する。Python3・SymPyにより、Hesse接線の三重接触、三つの接線比のnorm、規格化potentialの点三次、Hesse係数の有理逆、滑らかさの恒等式、数値rotation centralizerの六元、巡回平面twistの同型、norm係数の変換、symbolの外積恒等式を厳密に検算する。さらに普遍Jacobian上の明示三捩れ点、非零八点のHesse軌道とC₃安定化群、そのnormal coreの自明性、右点対応がHesse原点を(A:B:C)へ送ることを確認する。**保存済みの確認結果は13項目 PASS。本版で更新・実行したのは active 不変量検証器の十五群であり、この Picard 検証器を含む他の十五計算資産は基準版 `586eb26` との同一性を照合し、再実行せず保持した。実施範囲は `notes/validation.md` を正本とする。** 付値による非norm性、一般係数体への降下・支配性、gerbe・導来圏の一般証明をこの有限検算で置き換えない。

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

指定MF周期の中心的coherence、T^mによるclass不変性、方程式生成元のu⁻¹則とγの[v/u]変換、fractional Serre比較への帰着は、固定入力の該当式を照合して別担当が紙上で独立に点検した。独立尺度の一般族での最小次数九は、Kummer成分体が元の体の純超越拡大となりindex三を保つという体論の証明による。半古典 cube frame と γ_sc の形式像は、既存の全 scalar 式・一般三捩れ monodromy と照合した。さらに逆 CF の混合重み上界、integral Hom の局所化、κ(m) 上の比較、(f,η) の実際の同変商、一般安定化群の character 消滅と C(s,t) への一意な降下を内部で独立点検した。二境界候補の証明も点検したが、その前提である他の分岐の排除や D での非分岐性を検証したわけではない。元の K 上の位相の値を計算したという意味ではなく、新たな有限 jet 計算や形式証明器による検証とも区別する。

随伴復元による強化点型では、q^RO_C≃j_Y!OのKoszul証明、両ファイバーを用いるDVR上の最高次線束の持上げ、coneのproper性による非空型の有限降下を紙上で点検した。有限H_pには固定入力Bの三対象生成、Morita核のfree A^e、TV Proposition3.20と可逆核の開性、HH¹=0を実際に照合した。S_p×Pic_C^p、低次元の唯一のclass、Euler格子による奇数次元の数値的自明性、最小実現次数公式は一般証明であり、新たな計算コードや有限例だけによる確認ではない。全moduli上の実核の存在は主張しない。一方、全次元の一般一ブロック族でH_p=1、S_p=Spec(k_n)となる別のTate–Koszul証明は、本版で独立読解点検した。

高次元の中央shift部分の除去、classと軌道の安定化群の一致、奇数次元の数値格子・六元中央化群、七次元のZ²とrotation中央化群の無限指数は、本文の証明を別担当が独立に読解した。Iliev–Manivelの球面対象は既知入力と分け、数値的自明な自己同値の分類や対応torsorの中立性まで検証したとはしない。

外部文献 PDF、旧版原稿、旧 ZIP、担当者別の重複レポート、コンパイル中間生成物は現行一式に含めない。主張の証明・証明書の生成・実際の検証・保存は別の状態として扱い、検証事実の正本は `notes/validation.md` とする。
