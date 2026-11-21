# 非可換三次 n-fold：可換復元とモジュライの研究方針

2026年11月21日 / v40。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 独立論文と外部入力

本repoの唯一の主原稿は `papers/nc-cubic.tex`。一般中心三次変形に対するMF移送・可換復元、良い一ブロック型のO-markedモジュライ、満支持複数ブロック型の次数付き表示、残余Poisson射・Kuznetsov比較を研究する。**全次元・全ブロックの量子化の存在・中心元・同変降下の証明は別repo [cubic-quantization](https://github.com/uedakazushi/cubic-quantization) の [公表原稿](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) が正本**。古典Poisson正規形・退化とモジュライは [poisson-cubic](https://github.com/uedakazushi/poisson-cubic) が正本。一般中心三次変形の比較定理は量子化の存在定理を仮定せずに条件付きで成立する一方、良い一ブロック・残余Poissonの応用では量子化稿の具体的定理を外部入力として使う。量子化稿はAをambient・Bを中心商とし、本稿はBをambient・Aを商とする。

## 可換復元・モジュライの基本目標と優先順位

**現行の最優先研究目標（P0）：中心作用の共役軌道と二つの同種因子の算術的比較を調べる。** 主な対象は `n=4,N=6=3+3,k=2,m=0`、相対積とPicard補正は全 `k≥2,m=0` を扱う。自然な可換三次族 `Φ_pt`、相対積核、全O認識開へのPicard比較stack降下、周期の大域式 `q(ω³)=−1/v_ω(p)` を得た。全中心同変核型のscalar・位相判定は、三ブロック以上では同種因子を許し、二ブロックでは幾何学的非同種を仮定する。二つの同種因子には実際の混合coherent核があり、次数二の同種では双対群の反転も生じる。さらに二ブロックの通常Kuでは、平面イデアル層の球面捻りから指定中心μ3の非正規性と無限共役軌道を証明した。従って、全通常同値が指定中心を保つという方針は採れない。次はこの共役軌道上のGalois降下、混合核型の実現gerbeと位相、scalarを含む最小比較次数である。

**優先順位を変更する数学的理由：** 良い1ブロック型では既に広い範囲の一般次数・比較核の算術・周期の局所値が決まった。未解決の大域周期位相と scalar index は重要だが、そこだけを完成しても対象成分が増えない。複数ブロック型への拡張は全Poisson階数層を覆う構造理論へ直結し得るため、研究全体の価値の観点からこれをP0、既存の精密算術をP2にする。既存の証明・例・計算・未解決の詳細は削らず公表用主稿とノートに保持する。

**既存入力と境界：** `poisson-cubic` の正規形は `N=n+2=3k+m`, `V=⊕W_s⊕U` を与え、`cubic-quantization` の `thm:pg-all-dimensions` と `thm:pg-intrinsic-full-support-center` は、記載された原点近傍・滑らかさの範囲でPBW/AS正則ambient、中心三次商と満supportの同変選択を与える。一般中心三次変形の可換復元 `gdr:thm:generic` は一ブロックに限定されない。満支持型の全慣性・相対認識、非捩れ中心同変積表示、Picard比較stackの全O降下、自然な周期式を保持する。全中心同変核の算術判定は `k≥3`、または `k=2` で幾何学的非同種の範囲に成立する。同種二因子の全算術分類、完全無標識の最小次数、全境界・構造対象の像を指定しない全第三根・中心一次変数を持つ型は残る。量子化の存在は外部repoを正本とし、一ブロックの中心・点曲線・次数9/18を多ブロックへ無検証に流用しない。

**満支持型の表示モジュライ：** `B=⊗_{i=1}^k S_i`, `A=B/(Σa_iΩ_i)`、`k≥2,m=0`、全 `a_i≠0` とする。各因子は滑らかな楕円Sklyanin型で、`p_i,2p_i,3p_i≠0`、`j_i≠0,1728`、`j_i`相異なるという非空開を扱う。中心は `Z(B)_1=Z(A)_1=0`, `dim Z(B)_3=k`, `dim Z(A)_3=k−1`。次数二・三の乗法から周囲二次代数と商の中心直線を復元し、全次数付き同型を認識した。共通grading scalarを除いた**射影的な次数付き表示**の滑らかな既約DM stack `P_k` は次元`2k`、幾何点の慣性は `(H_27^k)/Δμ_3`、位数`3^(3k−1)`。二ブロックでは次元4・慣性243である。一般底上の大域的な実代数の存在には、別の表示gerbeの持上げが必要となる。

**相対双対と全O同値の認識：** 中心一次変数を使わず、因子の有限potential/Koszul解消と中心関係直線`ℓ`から普遍AS-Gorenstein恒等式、全整数の切断飽和、compact部分の相対Serreを得た。`D=det(⊕W_i)⊗ℓ^∨`, `r=3k−3`, `n=3k−2` とするとSerreは`(-r)[n]⊗D`、内在的反標準環は`⊕A_(rq)⊗D^(−q)`で、共通scalarの重み零により表示stackへ降下する。これだけからtailsのsmoothnessやcompact＝全coherentは結論しない。

`jp_i≠0`（`1≤j≤3k−3`）という有限個の捩れ条件を除いた非空開で、`C=A^(3)`の中心次数`k−1`と中心多項式環上の平坦性を確認した。`k≥3`では`A^(3k−3)`から`A^(3)`への同型持上げが`μ_(k−1)`-torsor、`k=2`では恒等である。従って全O同値はfpqc層として `Eq_O(QGr A,QGr A')=Isom_gr(A^(3),A'^(3))/G_m` と認識できる。第三Veroneseは二次表示を持ち、二ブロックでは生成元55・独立二次関係2619、固定模型間の全同値層は有限表示schemeである。さらに、滑らかな可換三次への支配的特殊化で全O自己同値の一般有限性を証明し、関係Grassmann多様体の像の非空開でfppf局所表示を効果化した。得られた全O局所型stackは滑らか・既約・DM・次元2kである。全境界や任意の抽象Abel圏変形を覆うことは未証明。

**中心商・全自己同値群・根：** `D=C/(Z(C)_1)=(⊗T_i)^(3)`の純成分と余法加群は元の`(E_i,L_i,σ_i)`を復元する。純商イデアルの飽和冪から全多重次数を回復し、`Aut_gr(D)=(∏Aut_gr(T_i))/Δμ_3`を得た。中心完全交叉の局所コホモロジーと負次数Ext消滅から`M_j=(A(j))^(3)`の全中心thickeningへの持上げを一意化し、次数別安定性により実際のgraded同型へ戻した。その結果、基本楕円開の全`k≥2`で`Aut_gr(C)/G_m=K_k=(H_27^k)/Δμ_3`、中心還元核は自明となる。上の全O認識条件を加えると全`Aut_O=K_k`であり、二ブロックの全慣性は正確に243である。有限性や中心一次変形類の非消滅を仮定しない。二ブロックでは逆に還元核自明性から`κ_C≠0`も従う。一次で自明なら二次関係を保つ`g↦−g`が生じるためである（`mbcr:cor:nonzero-class`）。具体的なcocycleの値は未計算。

**相対認識と中心慣性：** 表示を忘れる射`P_k°→M_k°`は射影枠を使って表現可能・fppf・準有限と分かる。標数零の一般滑らかさと有限表示降下により、さらに非空開上で有限étaleとなり、全幾何慣性の一致から階数一、従って同型となる。この開に属する族では、任意の非被約試験底上で`Eq_O=Isom_gr(A,A')/G_m`である。全慣性の中心はブロック順序付き被覆上で`(μ_3^k)/Δμ_3`、順序を忘れた底では因子置換で降下する。全境界と全抽象Abel圏変形は含めない。compact残余enhancementと中心作用は以下の構成で降下するが、rotationや比較核には別の障害を保持する。

**表示障害と残余圏：** 実表示の `G_m`-gerbe の類 `β` は、表示stackの各非空開で正確に位数3である。関係直線 `ℓ` の重み3が上界、実表示慣性のcommutator内の共通 `μ3` が下界を与える。これはstack上の類の主張であり、各体値点の引戻しが常に非零とはしない。順序付き被覆でweight1束の最小正階数は3。`O(j)` とshift(j)は重みj、RHomと対象のtensorで重みが相殺するためcompact残余圏・評価・mutation projectorは全O開へ降下する。例外成分は `Perf(P_k,−jβ)` となる。有限mutationと相対Serreからrotationの自己同値性と `S_K=ρ^(−r)⊗D[n]` を得る。MF/window比較がある範囲では `ρ³⊗ℓ^∨≃[2]` が降下する周期であり、`ρ³≃[2]` は関係方程式のframeを選んだ後の式である。実際のrotation核の非降下はscalar-simple・負Ext消滅・底変更の条件を明記して述べる。

**中心作用と順序：** `Z_0=(μ3^k)/Δμ3` の作用および同変化は、共通scalarの自然同型を用いてcoherenceごと全O開へ降下する。線型的持上げの選択は `S_k={a∈F3^k:Σa_i=1}`、階数 `3^(k−1)` の `Z_0` の双対群torsorである。基準bからcへの変更で `χ_bc=z_b/z_c` とすると `J_bc ρ_b≃Tw_(χ_bc^−1) ρ_c J_bc`。置換不変な選択は `3∤k` の場合に限り一意に存在し、`3|k` では非空開に縮めても分裂選択被覆は切断を持たない。これは作用本体の降下を妨げず、共通 `G_m`-gerbeの障害とも異なる。

**積表示と比較核の境界：** 可換分離和 `X=V(Σf_i)` では `Ku(X)^(Z_0)≃Db(∏V(f_i))`。双対群のcharacterを移送すると、積側の因子rotation `R_i=T_O∘(−⊗O(1))` の比 `R_i^−1 R_b` によるcoherent作用を得て、通常のKuは積圏の双対同変化として記述される。`3∤k` では `c=k^−1∈{1,2}`, `m=(ck−1)/3` として対称rotationは `(R_1⋯R_k)^c[−2m]`、特に二因子では `(R_1R_2)^−1[2]` となる。この可換公式と二因子のrotation比はBFK・Elaginの既知結果の適用であり、新しい一般定理とは数えない。両側のsmooth proper族と作用を固定すれば同変Morita核の∞stackはfpqc降下する。一般点の実dg模型が有限拡大上にあり、幾何学的一般点で非空なら縮小後の有限étale被覆上に核が存在するが、大域切断は別問題。source/targetのrotation比較はscalar重み `(−1,1)`、比のbandは `β_t−β_s` を持ち、関係直線の同期も保持する。

**因子モジュライと自然な可換標的：** `P_k//Z_0≃B_k`、`B_k→E_k` は表現可能・滑らか・全射・相対次元kで、点曲線積のsmooth projective族が全O開へ降下する。最大可換商 `Q=S_ab` の三次部がrank1でC,Jの像が可逆な非空開の比較 `θ=(J→Q_3)^−1(C→Q_3)` は、相対Hesse被覆上の `θ(Ω_H)=3(a−b)F_H` により全基本楕円開へ一意に延長する。中心公式は既知結果、非零性・分母なし比較式・普遍被約重なりでの降下を本文で証明し、任意非平坦・非被約底変更に対応する。従って `Φ_pt:P_k→C_(3k)^sm`、表示gerbeのband同値 `β=Φ_pt*β_cub`、関係直線 `ℓ≃ℓ_pt` を全基本開で得た。2p=0の一般Hesse境界では比較係数が零となり、同じ線同型を延長できない。全O認識の既存開は拡大していない。証明は `mbfm`節と `mbpl:thm:global-line-comparison`, `mbpl:thm:commutative-family`。

**体上の直接非可換比較：** 全基本楕円領域の実表示 `A=(⊗S_i)/(Σa_iΩ_i)` に対し、有限Koszul–Shamash stabilizationの外積とBurke–Stevenson windowから `Ku_line(A)^(Z_0)≃Perf(∏E_i)` を直接構成する。多重THCRのnoetherian性はNC-ampleness・ideal sheafの安定・有限幅の端の帰納で全kを証明した。二因子のKeeler系を単純に反復していない。双対同変化でKu_lineのsmooth proper性を得て、既存crs飽和定理により `Ku_line=Ku_coh`。因子rotationは `R_i,p=T_O (t_pi)_*(−⊗L_i)`、dual characterは `R_i,p^−1 R_b,p`。各piを実線束化する高々三次拡大と指定周期の三乗根補正を各k回行い、次数 `3^e,e≤2k` の拡大後に `Ku_coh(A)≃Ku(X_pt)` を中心作用・rotation・周期付きで得る。代数閉体では拡大不要。これは全モジュライの表示チャートの一般点にも適用できるが、非分裂表示やブロック順序の持上げ次数は上界に含めない。さらに同じ偏極点曲線組の幾何fiber上でunmarked Kuの同値類は一定となる（関手の一意性・相対自明化・逆の回復は含めない）。証明は `mbnp:thm:product`, `mbnp:cor:coherent`, `mbnp:prop:rotations`, `mbrc:thm:finite-point-comparison`, `mbrc:cor:point-fiber-constancy`。

**相対非可換積と具体的な降下型：** `mbrn:thm:relative-product` はsmooth準射影C基底の順序付き実表示上で `Ku_comp(A/S)^Z0≃Perf(∏E_i/S)` の実Morita核を与える。訂正済みKeelerの相対Fujita消滅から任意noetherian基底のtensor-noetherian性を示し、正則基底上でBS/window・有限Shamash・Γ-Homを構成する。構成済みcompact/Perf模型は任意導来底変更に両立し、元のsmooth affine底ではcoherentと一致する。非正則底で全coherentとの一致は主張しない。`mbpd` のPicard型は `α=Σδ_i`、中心作用付き核stack `G_Pic×D`、rotation・周期付き `G_Pic×T` で記述する。標準有限étale比較被覆の階数は `3^(3k−1)`／`3^(3k)`、横断直線を選んだ非空開では `3^(2k−1)`／`3^(2k)`、体上の存在上界も後者である。

**自然な周期の全係数：** `mbhp:thm:period-formula` は conormal 規約 `pr₂f−pr₁f↦df` の下で `q(ω³)=−1/v_ω(p)` を与える。`v_ω=2y+a₁x+a₃`、`ω=dx/v_ω`、`v_ω(p)ω³` はJacobianとHodge線だけから定まる。Hesseの全九flexで中心を `Ω_H/(abc)` と正則化し、比較線 `λ⊗O(o)`、同期前の三乗写像、原点の係数−1/2と一次項−tから定数を校正した。全基本開と許された任意底変更に成立する。一ブロック残余位相 `γ̄_n/[D]` の大域式とは別であり、後者の未解決部分は残る。

**全O降下と因子を分離する全核型：** `mbic` では実積核のscalar/中心慣性をΓ次数ごとに比較し、射影表示Pと中心rigidification Bへ降下する。B上の中心同変残余は非捩れ `Perf(∏E_i)`、Picard型核stackは `G_Pic×D`／`G_Pic×T` であり、既存の全O認識開と因子置換へ降下する。個々のrotation・dual作用の非捩れB降下やgerbeの中立化は主張しない。`mbfc` ではOrlov像のblock対角性から核を外積へ分解し、`k≥3` なら全H作用を使う `(r−I)g_ij=0⇒3g_ij=0⇒g_ij=0` により同種性・CMを許す。`k=2` は幾何学的非同種なら同じ結論となる。全型で通常の中心同変核は `α=Σδ_i=0` かつ、ある `φ_i∈Aut_K(E_i,L_i)` に対し `γ_i+ν_i(φ_i)` が全て等しいことと同値、rotation・指定周期付きは全て零と同値。`g(f)=c_g f` に対し `ν(φ_*)=[c_g]`。固定Hesse levelの独立族では全νが零なので、全中心同変核の最小次数は `3^(k−1)`／`3^k`。

**二因子で実在する混合と中心標識の限界：** 二つの同種因子ではisogeny uとdualから `N²=DI`, `N^♯=−N` を作り、Pell方程式 `a²−Db²=1` により無限位数の混合Orlov isometryを構成する。代数閉体では可換子のshiftを三次周期で除き、`1−q` のisogeny補正と三乗根規格化で実際のcoherent核へ持ち上げる。幾何的中央化群はOrlov中央化群を商とし、核は `Z×E₁[3]×E₂[3]`。次数二isogenyではH反転も実現する。対照的に三因子以上のH-normalizerの像は偏極因子の置換だけで、共通符号反転は `3n=4` により不可能。不同jのk≥3、または非同種k2では、中心bandの抽象自己同型を許しても判定は変わらない。証明は `mbfc:prop:normalizer`, `mbfc:prop:two-isogenous-mixing`, `mbfc:lem:cyclic-centralizer-lift`, `mbfc:ex:two-isogenous-inversion`。

**通常Kuでは指定中心が正規でない：** 全ての滑らかな二ブロック分離和三次四様体で、二つのflex接線が中心生成元に巡回される三平面P_iを与える。`I_{P_i}` はKu内の二次元球面対象、数値Mukai行列は対角−2・非対角2・行列式32。球面捻りは中心μ3を逆元まで含めても正規化せず、二つの捻りの積の冪は無限個の相異なる共役部分群を与える。既存のG同変比較で全基本二ブロック非可換幾何点のKuにも移る。これは同じ共役軌道内の無限性であり、非共役作用が無限という主張ではない。中心同変化が点曲線積であるという性質だけでも指定部分群は選べない。元のK上の無標識比較の存在・最小次数は別問題である。証明は `multiblock_unmarked.tex` の `mbun:thm:non-normal`, `mbun:cor:infinite-orbit`, `mbun:cor:nc-non-normal`。

**相対可換比較と実現の二障害：** 滑らかな準射影C基底上で `f_i∈Sym³W_i⊗L`、各平面三次がsmoothなら、相対Orlovと共通Lを含む実dg外積から `Perf(∏E_i)≃Ku_Perf(V(Σf_i)/S)^(Z_0)` の実perfect核を構成した。noetherian qc separated底への任意の導来引戻しもこの同値を保つ。非正則底でDb(coh)=Perfや絶対coherent MFとの一致を主張しない。因子置換はKoszul braidingによりcoherent。これは既知のOrlov–Thom–Sebastiani法の相対実施であり、最小A∞模型の予想は使わない（`mbrp:thm:relative-product`, `mbrp:cor:base-change`, `mbrp:prop:permutations`）。両側のsmooth proper族と指定周期（残余ではMF/window比較）、非可換側の局所rotation比較、scalar-simple性、負Ext消滅・底変更を仮定し、核の局所型と自然な同期を固定すると、比較直線 `L_P` と `q:L_P³≃ℓ_tℓ_s^−1` が付随する。実際の周期付き大域核が存在する条件は核のgerbe類 `α_P=0` とtorsor類 `γ(P,θ)=0`。period標識後も核のAutはG_mである。連結ordered cover上のphase sectionは、全データの置換coherenceが既にある場合にS_kへ降りるが、G_m核gerbeの障害には適用できない（`mbks:thm:kernel-criterion`, `mbks:prop:permutation-phase`）。自然な非可換族の積Picard型のαと因子位相の構造・二捩れ境界剰余は `mbpd` で計算した。自然な位相の全係数はmbhpで決定済みであり、全型の算術判定は上記の因子分離条件の下で得られた。二つの同種因子の算術と完全無標識比較の次数は残る。

**根の正確な範囲：** `s=(1)`とし`rO≃O(1)`を満たす自己同値は一意に`r=sΦ_h (h∈K_k)`と書け、自動的に`r³≃s³`となる。自然同型類は`3^(3k−1)`個、全O群による共役類数は`(11^k+2·8^k)/3`、二・三ブロックでは83・785。三乗同型やcoherenceは標識しない。この関手分類に`6p_i≠0`は不要である。一つの自己同型の冪による全代数的Zhang twist表示の直接分類は`6p_i≠0`の下で保持する。点関係の過剰`9 binom(k,2)`と、可換tensor端点間の一般twisting system剛性も保持する。`r³≃s³`だけを仮定した全根は未分類である。

**多ブロックの同変一般点比較：** `R=C[h]_(h)` 上の次数別自由な三変数多項式環の変形 `D_i` と、滑らかな平面三次へ特殊化する中心三次 `Ω_i` の和を入力とする。既存 `cft:thm:complete`, `gdr:thm:generic` の下で、分裂式 `F_1+⋯+F_k` を `K=C(h)` 上に取れ、有限拡大上で中心群同変・rotation・指定周期保存のKu比較を得る。BFKの同変Thom–Sebastiani公式・Orlov比較を反復し、全 `k≥2` で既存の有限比較体上に `(K_A^coh)^(Z_0)≃Db(∏C_i)` を得た。可換積側の追加拡大は `mbrp:cor:comparison-field` により不要である。明示的Jacobian tensor/PBW族なら `J_i=g_i+ε_i² det Hess(g_i)/24` の分離和が復元模型であり、右辺は入力の実際の点曲線の積 `Db(∏E_i)` となる。この一般点法だけでは任意の固定非零パラメータや特殊点を含む相対比較を結論しない。その別構成は上記mbnp・mbrn・mbpdが与える。有限拡大上に別の比較核が存在することと、指定形式核の全jetの代数化を区別する。

**残余降下と積表示の証明：** `multiblock_scalar_descent.tex` の `mbsd2:thm:gerbe-period`, `mbsd2:thm:projector-descent`, `mbsd2:prop:rotation-serre`, `mbsd2:prop:line-period`、`multiblock_central_action.tex` の `mbza:thm:central-action`, `mbza:prop:shift-character`, `mbza:cor:permutation-obstruction`、`multiblock_residual_descent.tex` の `mbrd:prop:kernel-stack`, `mbrd:thm:split-product`, `mbrd:prop:factor-rotations`, `mbrd:cor:symmetric-rotation`, `mbrd:cor:dual-action`, `mbrd:cor:nc-product`。三節の証明を執筆担当以外も内部読解した。形式証明・外部査読・新規性の網羅的確認は未実施。

**中心認識の証明：** `multiblock_central_rigidity.tex`の`mbcr:prop:negative-ext`, `mbcr:lem:graded-lifting`, `mbcr:thm:reduction-rigidity`、`multiblock_center_automorphisms.tex`の`mbca:thm:center-automorphisms`, `mbca:thm:full-inertia`, `mbca:cor:marked-roots`、`multiblock_relative_recognition.tex`の`mbrr:thm:finite-etale`, `mbrr:cor:stack-isomorphism`, `mbrr:cor:central-band`。基礎となる余法加群認識・SSS・Grassmann像・点三次比較の証明も現行稿に保持する。文献比較では自由Poisson／多項式環のVeronese持上げ（Aitzhanova–Makar-Limanov–Umirbaev）とskew polynomial環の判別式による自己同型分類（Chan–Young–Zhang）の仮定差をIntroductionに明記した。初出の網羅的確認は未完了。

**基礎の証明の入口：** 主稿の`multiblock_serre.tex`（`mbsd:thm:serre`）、`multiblock_veronese.tex`（`mbv:thm:all-o-third`）、`multiblock_roots.tex`（`mbr:thm:algebraic-twist-groupoid`）、`multiblock_equivariant_descent.tex`（`med:thm:multiblock-generic`）。前提となる点対応・中心・表示stack・完備比較は`two_block_points.tex`, `two_block_algebra.tex`, `multiblock_presentations.tex`, `two_block_recovery.tex`に保持する。証明の内部点検、有限群の全要素検算、既存MF基礎定理の再証明、形式証明、新規性の網羅的確認を区別する。


旧論文Bの全coherent残余圏比較を一般次元の基礎部分として主論文に統合した。完備noetherian局所底での実際の有限rank MF関手と逆、三対象window、一般点の全coherent飽和、低rotation積からの関数体上の方程式復元、Hesse–Sklyanin有理例を省略せず保持する。モジュライの一ブロック仮定より広い基礎定理の一般性を縮小しない。一般復元は主稿内の基礎定理群、代数的中心量子化は外部repo `cubic-quantization`、古典的正規形は外部のPoisson論文を正本とする。

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

可換復元・モジュライの主公表原稿は `papers/nc-cubic.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

**良い一ブロック成分の一般部分で、点曲線が規格化する残余 Poisson 射を構成し、その符号商の一般次数が全 n≥3 で正確に18、半古典規格化したfull射の一般次数が9であることを示した。** 固定入力Bの完備 MF・正則底の window・一般点生成性・coherent 飽和性の下で、低 rotation 積の積分直線 L と中心一次作用の annihilator K_res から残余三次 X_res と射影 Poisson 射 Ψ_res を復元する。全 O-同値・任意底変更へ降下し、Brauer–Severi ambient を許す。Ψ_res は支配的・一般相対次元1であり、さらに有限 étale 被覆上で **同じ X_res の Ku** への比較核を得る。

生成元固定再帰を U=0 に制限し、既存の split Hesse 同定を係数空間上の多項式恒等式へ広げると、全 n≥3・一般混合係数で **W_h|_K=b_h J_g、J_g=g+h²Hess(g)/24** を得る。従って量子側の楕円点曲線 E_pt と残余 active 曲線 C_res は同じ j を持つ。これは MF 圏の U=0 への基底変更を仮定する証明ではない。

相対随伴により尺度線束 **T=L⊗det K_res≃λ_res∗** を同定する。有限 Hessian 補正 Φ が与える点曲線の尺度 τ_pt=(H♯|K)⊗P、すなわち標準微分 ω_pt を用い、j≠0,1728 の稠密開で T² の標準非零切断を構成する。これが **Ψ_res^±:M→[Pdec/μ₂]** を定め、全 O-降下・任意底変更・支配性・一般有限性を持つ。適切な非空開では有限 étale 全射である。標準二重被覆 D=Isom_gp(Jac E_pt,Jac C_res) 上では full tensor を得る。平面同型の十八重被覆 I→M と I→D の Jac(E_pt)[3]-torsor、点 shift の平行移動としての移送も構成した。

**残余射は、適切な稠密開で M→M/⟨ι⟩≃Z→Y と有限 étale に因子化し、階数は2,1,9、従って一般次数は正確に18である。** ιは反対代数の自由な操作、Zは補正前の active 不変量 (c₄,−c₆) による九次中間被覆である。active 不変量への一般ファイバーの幾何学的整性により、active 係数だけの体拡大で次数を検査できる。全次数残余 potential の混合重みが三以下に有界なことと trace の混合多項式性から、混合係数の三角形の多項式逆を構成する。共通の Hesse 三捩れ安定化群と符号付き安定化群の指数二を比較し、残っていた因子 e_n=1 を得る。形式逆だけから一般次数を推測する議論ではない。

**符号類χ_actの消滅を証明し、一般次数九のfull残余Poisson射を得た。** 符号二重被覆Dの一般点の類はactive不変量体L₀=C(c₄,−c₆)から来る。全次数で混合重みが有界なため、形式残余potentialはκ=C(p,q)((h))上の混合係数の実際の多項式となる。この表示はC₃対称点でも滑らかである。Poisson符号商標的の有限対角を用い、一般点で指定した同型をsmoothな有限係数模型とその二重・三重積上へ延長して、対称点を通る残余射の近傍延長を降下した。延長された曲線の有理三捩れ点がJacobianの二次twistを排除し、Hesse体への二次類の単射性からχ_act=0を得る。半古典先頭項で二つの符号の一方を選ぶと、全O-同値に自然なΨ_res^scが定まり、適切な開で有限étale階数9、Ψ_res^sc∘ι=−Ψ_res^scとなる。χ_op=χ_sgnであり、符号商射の次数18も保持する。

この符号消滅は既存の固定入力の下での結果であり、別の近傍延長仮定を要しない。構成したものは一般点のPoisson対の代数的延長である。その特殊ファイバーを圏の低rotation積から底変更と両立して再構成できることや、比較核がそこへ延びることは未証明だが、符号消滅の証明には不要である。Dの分裂だけではgenus-one torsor自体の同型やfull比較核の降下は従わない。一般 split 係数体上の平面同型は、下記の H_g による別の証明で得る。点規格化tensorは形式frameで(h/c_h)π_hであり、固定harmonic tensorの超越性と両立する。


**比較核には、最高次 cohomology を用いる次元非依存の三捩れ評価を得た。** split 表示上で source stabilization κ_nc と可換側の active 係数商・window1の関手 q_Y を固定し、R_P=q_YΦ_P(κ_nc) の H^{>−1}=0、H^{−1} が次数零の線束となる型を考える。この型は一般点の有限分離拡大上で非空であり、従来の CF Euler 条件も同時に保てる。証明は線型中心列に対する graded purity、MF係数商の Tor-independent な同定、Galinat の window規約における負 rotation の計算、有限模型からの閉点特殊化を用いる。

この型で **full kernel の同型類を整合的に選んだ後**、その scalar gerbe 上の H^{−1}(R_P) は正準的な重み一線束となる。実際の O_C(1) と tensor して押し下げると階数三束ができ、その endomorphism は次数三の Azumaya 代数へ降下する。従って split 一般点で 3α=0、ind(α)|3。表示分裂後にこの型となるという仮定の下で、非分裂表示を含む体上では n≢1 mod3 で ind(α)|3、n≡1 mod3 で ind(α)|9。表示類βと核の類αは同一視しない。一般の refined 型については核の同型類の選択と残る Picard 類の計算が別に必要である。下記の点型では、一般 split 係数体上の scalar 障害が非零で index 三であることまで決定した。

上のsplit表示と固定したq_Yの下で、最高次線束の相対Picard類 m_P:S→Jac(C/S) が定まり、核のgerbeは m_P によるPicard gerbeの引戻し、すなわち α=m_P^*(β_Pic,C) と同定できる。m_Pを実際の線束で表せれば中立であり、とくにm_P=0ならCの有理点を仮定せず障害が消える。またαはC上で零となり、C上には実際のfull比較核がある。一般K直線との横断切片は次数三のfinite étale scalar分裂被覆を与える。いずれもfull classを選択した後の結果である。


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

**点型の scalar 障害は、一般 split 係数体で正確に period=index 三となる。** 一般の二曲線については α=δ_Ept(p_pt)+e₃,*([I_sc]∪κ₃(p_pt)) だが、上の分裂によって補正項は零であり、full class を選ぶ前から δ_Cres(p_res)=δ_Ept(p_pt) の period と index が三である。点型 full class を k_n 上で整合的に選べば、その scalar gerbe α も正確に index 三となり、残余平面三次の横断直線切片から三次分裂体を得る。全 n≥3 でこの scalar 段階を決定し、n=3,4 では下記の full class 降下により、実際の full 比較の最小次数も三と決定した。全 n の強化点型 class は Tate–Koszul 忠実性で一意に選択できる。既知の Tate–Weil pairing による cup 表示、flex・平面同型・三分点の三つの階数九 torsor の区別は保持する。

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

正準 frame の周期 torsor は上の非自明性により次数三の体 M となり、強化点型の指定周期付き最小次数は 3 ind(α_M)∈{3,9} である。n=3,4 では全 full class に共通する。任意の別 frame では位相成分体の次数は一または三であり、target の生成元を適切な k_n-単元倍にした適合 frame の最小次数三、target だけに独立変数 t を掛けた k_n(t) 上の一般族の正確な最小次数九も保持する。この独立尺度を元の一ブロック係数や formality パラメータと同一視しない。scalar G_m-gerbe、標準三分点 torsor、相対周期の μ₃-torsor は別の構成である。

**一般高次元の class と T-軌道には同じ Galois 安定化群がある。** rotation を保つ幾何的 full 自己同値類の群を G_ρ、対応する比較 class の torsor を C_ρ とする。元の体上の実核 T=ρ_Y⁻¹[1] は G_ρ の中心にあり、⟨T⟩≅Z である。各 class とその T-軌道の Galois 安定化群は一致するので、class 選択は C_ρ/⟨T⟩ の有理点、すなわち G_ρ/⟨T⟩ に値を持つ非可換 H¹ 障害の中立性へ正確に帰着する。点型を含む固定軌道が一つあれば、その点型 class 自体が降下する。T が点型を保つことはこの議論の前提ではない。

split な滑らかな三次の奇数次元では数値 Ku 格子は階数二、Galois 作用は自明であり、rotation の数値中央化群は C₆ となる。G_{ρ,0} を数値作用の核とすると G_ρ/⟨T⟩≅G_{ρ,0}/⟨[2]⟩ である。n≢1 mod3 では Serre 関手から rotation を回復できるため、G_ρ は全自己同値類群に等しい。数値作用だけでは full class を決定できないが、随伴復元条件ではこの群の有限部分に絞れ、さらに Tate–Koszul 忠実性でその自明性を示せる。

**随伴復元条件を満たす点型の first stage は、有限 étale torsor である。** Z=j_nc^!O、q=Li_C^*j_Y、q^R=j_Y^!i_* と置く。点型 P に対し E_P=Φ_PZ、M_P=H⁰(qE_P) とし、truncation と随伴から来る正準射 E_P→q^R M_P が同型になる条件を加える。この強化点型は固定入力の形式恒等分枝と finite-perfect 降下により非空である。幾何学的に p_res を表す線束 M を選んだ E_p=q^R M の同型類は Galois 不変であり、H_p={g∈G_ρ:g(E_p)≃E_p} は有限群となる。三つの rotation 像による generator、Toën–Vaquié の boundedness と HH¹=0 を合わせて有限性を示すのであり、全自己同値群の有限性を主張しない。強化点型の class は有限 étale H_p-torsor S_p をなし、その実現 stack は S_p×Picard_{p_res} である。M や E_p の実現を元の体上で選べるとは仮定せず、class の有限 torsor と scalar index 三を区別する。

有限 H_p と class torsor の記述は一般の形式で保持する。全 n≥3 で rotation Euler 数の最大公約数 d_n は正なので [E_p]≠0、全奇数 n では H_p⊂G_{ρ,0} であり、n=5 では χ(E_p,E_p)=−27 である。S_p=⊔Spec(K_i) による強化点型の最小次数公式 min_i[K_i:k_n]ind(α_{K_i})≤3|H_p| も有効である。一般一ブロック族では下記の Tate–Koszul 忠実性により H_p=1 と分かるため、class を選択する第一段階は全次元で解消する。随伴復元条件のない全点型や任意の full class の分類は含まない。

**全 n≥3 の一般一ブロック族で、随伴復元点型の class は正準的に一つとなる。** A=B/(Ω)、deg Ω=3 に対し、固定入力の双加群自己交叉三角から通常 Ext= B!⊗k[t] と Tate Ext= B!⊗k[t,t⁻¹] を得る。deg ξ=(1,−1)、deg t=(2,−3) とすると j=−p−q≥0 の部分が通常 Ext であり、全 A∞ 積・写像・homotopy に保たれる。Adams Koszul 双対と derived localization の mapping space の忠実性により、原点と rotation を保つ核 class は Aut_gr(B,kΩ)/G_m へ単射を持つ。一般表示の射影安定化子は自明なので H_p=1、S_p=Spec(k_n)。scalar gerbe はなお α=δ_C(p_res)、period=index=3 であり、周期標識を加えない強化点型の最小実現次数は正確に三である。全自己同値群を分類した結果ではない。証明は `thm:nfm-origin-rotation-faithful`、`cor:nfm-generic-adjoint-class-unique`。

**一般三次五次元の Clifford 半 rotation は、平面の選択に依存せず実核として元の体へ降下する。** Peize Liu の O_Cl²≃ρ を、平面の Fano 曲面 F₂(Y) 全体の実際の相対 perfect 核として構成する。F₂(Y) の幾何学的連結性と HH¹=0 による離散性から、その幾何的核 class は一定となる。降下 gerbe の類 β_O は convolution により 2β_O=0 であり、F₂(Y) の Plücker 次数2835の零 cycle 上で分裂するので 2835β_O=0、従って β_O=0 となる。ここでは β_O を表示 gerbe や点 Picard 障害と区別する。

Clifford 半 rotation はさらに、関手として O_Cl A≃Aρ⁻¹[1] と同定できる。spinor 列を相対随伴の unit と同定し、相対 coevaluation と通常の right mutation の coevaluation を比較する。Ku の二つの消滅から差が例外的 block ⟨C₁⟩ に入り、mutation で消える。従って元の体上でも O≃T、O³≃[1]、ε=OT⁻¹≃id であり、E_p も固定される。これは対象の固定や数値的自明性からの推論ではなく、perfect 核の自然同型である。既存の相対核・奇数零 cycle による降下の証明も保持する。指定された square 同型と MF period の同時正規化は別問題である。証明は `lem:nfm-fivefold-spinor-relative-coevaluation`、`thm:nfm-fivefold-half-rotation-identification`、`cor:nfm-fivefold-half-rotation-candidate-trivial`。

全自己同値群が常に Z になるという延長は、一般三次七次元では実際に偽である。Iliev–Manivel の既知の rank 九球面束に由来する twist と shift は Z² を生成し、この twist の異なる冪は G_ρ の異なる剰余類を与えるので G_ρ は全群内で無限指数となる。これは rotation 中央化群自身が巡回でないという結論ではない。Torelli による多様体の復元も、自己同値の作用の忠実性を自動的に与えない。このため全自己同値群の分類を先に解くことを必要条件にせず、点型を含む一つの固定軌道を狙う。全 n の強化点型 class は下記の忠実性により選択でき、任意の full class の分類は残る。

従来の **Euler 数だけを指定した型**には d_n=3^floor((n+1)/2) の bound を保持する。n≥5 では全ての核へ上の3を拡張しない。n=3,4 の全 class に共通な三という結論は Euler 評価ではなく、別の自己同値分類と class 降下による。既存の rotation 軌道・shift・有限 cone の整数 Euler pairing は d_n Z であり、その反復では bound を改善できない。新しい評価は full kernel から作る正準的な最高次 cohomology を用い、active 同値核の選択や代数的な coherent 中心線型性の降下を前提としない。いずれの三-primary な既選択類も、三に素な体拡大では index が変わらない。

固定生成元・固定 h の **実際の harmonic tensor π_h は very general に超越的**であり、この結果も保持する。自然な点規格化はこれと矛盾しない。形式 Nat frame を許した比較と固定 frame の代数性を区別する。選んだ相対 graph flow は中心乗法を厳密に保ち、Ψ_res の形式値は (V(W_h),[π_h])。さらに bar flow と逆を中心係数環上で商へ降ろすことで、完備・次数別の中心商について MF 比較を構成した。U=0 の active MF 比較も得るが、一般点の有限な代数的核への coherent な中心線型性の降下は未完成である。圏の導来 tensor と係数商を同一視する方法、および absolute perfect から relative perfect を推論する方法には一般的な反例がある。CF を選んだ trait の滑らかな模型はあるが、正準延長や h=0 での核は未構成である。

既存のモジュライ同型、相対点復元、Brauer 障害、Jacobi スキームと証明書は保持する。trace–Hessian と残余三次の全次元反例、一般次数9の有限補正 Φ、全混合五次 tensor と残余四次項、四次障害と追加補正 Φ^[4] も有効である。Φ、Φ^[4]、Ψ_res、Ψ_res^± は標的と厳密性の異なる構成である。元の目標では、一ブロック一般部分の moduli・点曲線・自然な Poisson 射・被覆上の同じ X への Ku 比較が接続した。**複数ブロック型の内在的表示・モジュライ・Poisson射・Ku比較への拡張**を優先し、1ブロック型の正準強化classの周期位相・coherent中心線型性・一般高次元の任意full classと非分裂軌道を並行する重要課題として保持する。

## 一般性と成分の扱い

- 各既約成分について対象、仮定、非空開、表示による被覆範囲を明記する。一ブロック表示空間の既約性から全 intrinsic O-marked moduli の全成分を扱ったとは結論しない。Poisson 側の唯一の支配成分の結果と、未構成の圏 moduli の成分分類を分ける。
- general は稠密 Zariski 開、very general は可算個の真の閉集合を除いた範囲と区別する。有限個の小位数除外と無限位数条件は異なる。点集合だけから代数的な開 stack や族の射を結論しない。
- 関数体上、有限拡大上、形式完備化上、有限 Artin jet 上の結果を区別する。有限 jet の marked 非同型から一般ファイバーの unmarked 非同型を結論しない。Hesse 例の一般ファイバーの非同型は、別の j 不変量と symmetrizer の証明による。
- 射はまず一般点で構成し、有限表示と必要な降下を確認して稠密開へ広げる。実際の相対 O(1) と偏極類、split ambient と Brauer–Severi ambient を区別する。
- boundary・非被約形式近傍・個別次元の計算は一般構成の具体的な障害を解消するときに優先する。独立成分の一般点や point scheme の楕円成分 E を、この方針を理由に除外しない。

## 固定した入力と現在の到達点

外部の古典入力は [poisson-cubicのPoisson幾何論文](https://github.com/uedakazushi/poisson-cubic/blob/main/papers/poisson-cubic.tex) の `poisson_geometry.tex`（`prop:pg-represent`, `prop:pg-jacobi-extension`, `thm:pg-normal`, `cor:pg-generic`）。固定入力はcommit `9f91efa3465f18219c36c31750f1e66220faeaa7` のA-v62（2026-11-21）。代数的中心量子化の入力は[cubic-quantization](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) v1であり、具体的ラベルを主論文の参考文献に記す。従来の論文B B-v59の完備MF移送・一般点可換復元とその証明は、このリポジトリの `papers/sections/generic_recovery/` に移して主原稿へ統合したため、外部入力とは数えない。三様体の比較対象は [nc-cubic-threefold](https://github.com/uedakazushi/nc-cubic-threefold/tree/6c35d2c84671c2538e61836a6bf3a511392eacce) の固定 commit `6c35d2c84671c2538e61836a6bf3a511392eacce`（v22）。通常の非可換研究では外部repoを読取り専用とする。今回の三論文への分割ではユーザーの明示依頼に基づきpoisson-cubicも整合させる。

古典Poisson論文を入力とする全次元正規形、別論文 `cubic-quantization.tex` の代数的中心量子化と、公刊の PBW/CY・星積・wheel 消滅・Kontsevich の二次形式対応・Mori–Smith の点曲線 Hessian 公式、Banks–Panzer–Pym の harmonic graph weights と Buring の公開データ、Wang・Hwang の勾配復元、Toën–Vaquié の perfect 核の有限表示・boundedness・同値 locus の開性を外部からの既知入力として扱う。完備MF移送・一般点可換復元・Hesseの有理模型は本稿中の独立した基礎定理・証明として保持する。Matsuno の Sklyanin 分類、Hille–Van den Bergh の楕円 Fourier–Mukai の graph 認識、Ciperiani–Krashen の Tate–Weil pairing、Liu と Huybrechts の低次元自己同値分類、Peize Liu の五次元 Clifford 表示と半 rotation、Kuznetsov の相対二次曲面束、Collino の平面 Fano 曲面、Ciliberto–Zaidenberg の次数公式、Iliev–Manivel の一般三次七次元の球面束と twist、Murfet の MF residue trace も既知の入力として用いる。三分点の全モノドロミー、低次元 full class 降下、点型の全 O-共変性、周期位相の class 不変性と相対尺度の算術、高次元の中心的整数軌道と数値中央化群による簡約に加え、三乗倍までの方程式規格化と形式位相の計算、混合係数を有理的に保つ周期付き CF 比較と二変数不変量体への位相の降下、随伴復元点型の有限 class torsor を本文に証明し、内部で独立点検した。外部査読と新規性の網羅的確認は未完了であり、未公表入力の全証明を独立に再検証したとは主張しない。書誌・参照箇所は `notes/research_notes.md`、確認状態は `notes/validation.md` に置く。

| 基本目標 | 現行稿に証明のある到達点 | 未解決の核心 |
|---|---|---|
| 満支持多ブロックの相対積 | 順序付き実表示上の実Morita核、全kの相対noetherian性、任意noetherian底変更でのcompact/Perf比較。元の正則affine基底でcoherent飽和 | 非正則底の全coherentへの拡張、Picard型を超える相対全核分類 |
| 多ブロックのPicard型比較 | scalar類Σδ_i、因子位相の対角商D、Hodge比較線と単元表示。中心作用付きG_Pic×D、rotation/period付きG_Pic×∏Ti | 同種二因子の全算術型、非被約底上の全型stack、完全無標識比較 |
| 自然な多ブロック周期の算術 | 二捩れ境界の剰余+1。有限型函数体の独立k方向例でscalar類0、指定型の最小位相次数3^(k−1)/3^k。一般体上の比較上界3^(2k−1)/3^(2k) | 位相と非零scalar障害の同時最小次数、中心標識を完全に忘れた下界 |
| O-marked moduli | 全 O-同値比較と重み付き tails による効果化。滑らかな出力を持つ良い pair では周囲単独の有限安定化子を外せ、滑らかな既約 DM stack Msm を構成。表示 gerbe は n≢1 mod3 で中立、n≡1 mod3 では全非空開上で位数3 | 各 intrinsic 成分の一般対象の局所表示、複数ブロック型、成分性 |
| point scheme | 相対 Pt(A)=E⊔D、中心への八重被覆、定常成分の型(2,2,2,3)、埋込み点対応からの A 復元。I_sc は一般 split 係数体で分裂し、Jac(E_pt)[3] の非零 k_n-有理点がないため有理点 φ_sc は一意。φ_sc と点型の最高次線束条件は、良い一ブロックの共通稠密開上で全 O-同値・任意底変更へ降下 | full rotation からの点データ認識、各 intrinsic 成分への拡張、像・分岐・自己同型 |
| Poisson moduli | Msm≅Pgood。入力Bの下で射影残余射 Ψ_res と T≃λ_res*、点微分による Ψ_res^±。正確な一般次数18、M/⟨ι⟩≃Z、χ_op=χ_sgn+χ_act。Hesse体への二次類単射とC₃対称族自身のJacobian同型被覆の分裂。有限対角による近傍延長からχ_act=0、半古典規格化full射の次数9と反対同変性。固定 harmonic tensor は very general に超越的 | 特殊族での圏的再構成との整合、各 intrinsic 成分 |
| active 比較と点障害 | 任意の実次数三偏極標的 C への全 Fourier–Mukai intertwiner の存在は、偏極曲線同型と δ_E(p)=0 に同値。Sklyanin による算術的実現と支配族から、一般 split 係数体で点障害の period=index=3。三に素な有限拡大後も active intertwiner はなく、p_pt と p_res は非三可除。行列余核は3pを表す実線束。完備半古典族では一意な形式三分点により点障害が分裂 | active の同型類・実現 gerbe を full 核へ持ち上げる条件、追加周期標識の μ₃-torsor、非分裂表示への適用範囲 |
| 三分点の算術 | 全 n≥3 の k_n 上で標準三分点 torsor は連結な九次体。最小点定義次数九、Galois 閉包群 ASL₂(F₃)・位数216、真の中間体なし。残余側へ θ_sc で移送 | full 比較の最小次数とは別。標準 split 係数体以外へのモノドロミー拡張 |
| Kuznetsov 比較 | 全 n≥3 の一般一ブロック族で強化点型 class が一意、一般 split 体で最小実現次数三。五次元半 rotation は ρ⁻¹[1]。非分裂 n≡1 mod3 の指数九族では強化点型最小九、別型の full 核は三次拡大で存在し、n=4 では全型の最小も三 | 高次元の任意 full class と他の非分裂軌道、coherent 中心線型性、共通開の外と全 intrinsic 成分 |
| 周期標識の算術 | 全 n≥3 の正準強化 class に γ̄_n∈C(c₄,−c₆)×/cubes。q=2 の完備局所値は [D_R]、v_D=1 mod3、位相被覆は三次分岐。位相体 M は次数三。frame 変更は γ′=[v/u]γ | 大域的な β_n=γ̄_n/[D]、ΔD 外の非分岐性、ind(α_M) と標識付き最小次数三／九。大域式 [D] は追加非分岐仮定付き |
| 高次元の full class 障害 | class と T-軌道の Galois 安定化群が一致。奇数 n で G_ρ/⟨T⟩≅G_{ρ,0}/⟨[2]⟩、数値像 C₆。一般三次七次元では full Aut は非巡回、G_ρ は全群内で無限指数 | 随伴復元条件のない全点型・任意型の class 選択。G_ρ 自身の巡回性は七次元の反例では否定されない |
| 随伴復元点型の class の一意性 | Tate–Koszul 忠実性により全 n≥3 の一般一ブロック族で H_p=1、S_p=Spec(k_n)。実現 gerbe は Picard_{p_res}、一般 split 体で未標識最小次数三。一般形式の有限 torsor と最小次数公式も保持 | 随伴復元条件のない全点型・任意 full class、共通稠密開の外への延長 |
| 五次元の Clifford 半 rotation | 相対・絶対 coevaluation の比較から O≃ρ⁻¹[1]、O³≃[1]、ε≃id を実際の perfect 核として同定。平面非依存性と奇数零 cycle による降下の別証明も保持 | 指定 square 同型と MF 周期の同時正規化。全自己同値群の分類は含まない |

一般残余射の主証明は `papers/sections/residual_algebraic.tex`。`lem:nfm-dominant-central-family`、`thm:nfm-relative-residual-cubic`、`lem:nfm-relative-center-transport`、`thm:nfm-projective-residual-morphism`、`prop:nfm-projective-residual-dominance`、`thm:nfm-residual-comparison-cover`、`prop:nfm-residual-kernel-descent`、`cor:nfm-residual-good-reduction`、`thm:nfm-normalized-tensor-transcendence` を参照する。

点曲線と自然な尺度の主証明は `papers/sections/residual_point_scale.tex`。`lem:nfm-active-restriction-all-orders`、`prop:nfm-residual-active-point-cubic`、`thm:nfm-residual-point-j`、`prop:nfm-point-residual-isom-cover`、`prop:nfm-scale-hodge-line`、`thm:nfm-canonical-signed-residual-map`、`prop:nfm-point-normalized-jacobian-cover`、`prop:nfm-point-scale-formal-comparison` を参照する。一般次数の主証明は `thm:nfm-residual-exact-degree-eighteen`、`prop:nfm-residual-mixed-triangular`、`lem:nfm-active-invariant-regular-fiber`、符号は `thm:nfm-residual-sign-active-class`、`cor:nfm-opposite-cover-active-twist`。 Hesse体の二次類単射・対称族自身の分裂・符号消滅は `lem:nfm-hesse-kummer-injective`、`prop:nfm-cyclic-test-sign-split`、`lem:nfm-finite-diagonal-rational-extension`、`lem:nfm-poisson-target-finite-diagonal`、`thm:nfm-active-sign-vanishing`、`cor:nfm-semiclassical-full-residual`。反対作用は `prop:nfm-opposite-involution`、`thm:nfm-residual-opposite-even-degree`。核の数値型・index は `residual_algebraic.tex` の `lem:nfm-kernel-determinant-annihilator`、`lem:nfm-cubic-euler-gcd`、`prop:nfm-kernel-three-primary`、`cor:nfm-generic-kernel-bound`、`prop:nfm-kernel-euler-orbit-lattice`、`cor:nfm-kernel-prime-to-three-invariance`。新しい三捩れ評価は `lem:nfm-linear-center-purity`、`prop:nfm-mf-linear-restriction`、`lem:nfm-active-line-rotation`、`prop:nfm-kernel-active-line-nonempty`、`thm:nfm-kernel-active-line-bound`、`cor:nfm-kernel-picard-obstruction`、`cor:nfm-kernel-active-curve-splitting`、`cor:nfm-kernel-active-line-unsplit`。一般Picard障害の鋭さは `prop:nfm-picard-cubic-index-sharp`、`cor:nfm-picard-infinite-translation`。標準三分点被覆は `lem:nfm-picard-tripling-line`、`thm:nfm-kernel-tripling-cover`、`cor:nfm-kernel-picard-mod-three`。指定中心商の相対THCR/window1と点の平行移動への同定は `papers/sections/residual_kernel_point.tex` の `prop:nfm-relative-active-thcr`、`lem:nfm-active-dvr-gorenstein`、`prop:nfm-relative-active-window-basechange`、`lem:nfm-elliptic-rotation-conjugacy`、`prop:nfm-kernel-point-line-nonempty`、`cor:nfm-kernel-point-picard-obstruction`。完備中心商は `prop:nfm-completed-central-restriction`、`cor:nfm-completed-active-mf`。

全 active Fourier–Mukai 比較は `papers/sections/residual_kernel_point.tex` の `lem:nfm-elliptic-numerical-graph`、`thm:nfm-elliptic-normalized-intertwiners`、`cor:nfm-elliptic-any-intertwiner-criterion`、`cor:nfm-elliptic-full-centralizer`、`prop:nfm-elliptic-intertwiner-gerbe`。追加周期標識は `rem:nfm-elliptic-period-phase` で分ける。行列余核と完備化上の分裂は `prop:nfm-point-matrix-tripling-line`、`lem:nfm-formal-point-third-division`、flex と平面同型による障害移送は `prop:nfm-kernel-flex-cup`、`prop:nfm-picard-plane-transfer`。

点障害の算術的実現と一般点の正確な index は同節の `prop:nfm-active-point-sklyanin-realization`、`prop:nfm-active-point-obstruction-dominant`、`cor:nfm-generic-point-picard-index-three`。active intertwiner の一般点での不存在は `cor:nfm-generic-active-intertwiner-obstruction`、点型 full 比較被覆の次数制約は `cor:nfm-point-comparison-cover-three-divisibility`。有限恒等式の再現は `python3 computations/verify_picard_obstruction.py` を用いる。接線・norm・点三次・Hesse 係数の逆・六つの数値 centralizer・巡回 twist と symbol 補正を厳密検算するコードであり、Brauer 類の非零性、支配性、降下や Fourier–Mukai 分類の証明そのものは本文にある。

一般 split 係数体上の平面同型は `papers/sections/residual_point_scale.tex` の `thm:nfm-generic-plane-isom-splitting`、同じ節の `prop:nfm-semiclassical-plane-isom-descent` は指定形式分枝の全 O-降下・任意底変更を与える。残余側の正確な Picard index は `papers/sections/residual_kernel_point.tex` の `cor:nfm-generic-residual-picard-index-three`。点型 full 核の不存在と比較被覆の三整除性は強化した `cor:nfm-point-comparison-cover-three-divisibility` を参照する。補正が genus-one torsor の差だけを見ることは `lem:nfm-picard-torsor-quotient`、形式比較だけでは補正を決められない例は `prop:nfm-cyclic-plane-twist`。

三分点の連結性と Galois 群は `papers/sections/residual_kernel_point.tex` の `lem:nfm-generic-hesse-third-division`、`lem:nfm-generic-active-three-torsion-monodromy`、`thm:nfm-generic-point-third-division-monodromy`。n=3,4 の全 class 降下と最小比較次数は `lem:nfm-projector-kernel-uniqueness`、`lem:nfm-cyclic-kernel-class-descent`、`prop:nfm-generic-low-dimensional-kernel-aut`、`thm:nfm-low-dimensional-full-class-index-three`、指定周期付き最小次数の三・九という二択は `rem:nfm-full-kernel-period-nine`。最高次線束型と点型の表示共変性・全 O-降下・非分裂 period は `lem:nfm-origin-object-weight-zero`、`prop:nfm-active-restriction-geometric`、`eq:nfm-point-type-intrinsic-complex`、`cor:nfm-point-type-O-descent`、`cor:nfm-unsplit-point-scalar-period-three` を参照する。

周期位相の class 不変性・規格化変換・独立尺度付き最小次数九は同節の `lem:nfm-mf-period-central-coherence`、`prop:nfm-period-phase-class-invariance`、`prop:nfm-period-equation-frame-change`、`thm:nfm-free-period-frame-degree-nine`、`rem:nfm-period-frame-scope`。三乗倍までの方程式規格化、一般係数体での平面同型の一意性、形式位相の計算は `prop:nfm-period-equation-cube-frame`、`cor:nfm-generic-plane-isom-unique`、`prop:nfm-period-phase-formal-active-scalar`。三次元の位相を fractional Serre 自明化の比較へ戻す補題は `lem:nfm-period-phase-fractional-serre`。

周期位相の混合定数降下と二変数不変量体への帰着は `papers/sections/residual_period_descent.tex` の `thm:nfm-period-phase-active-descent`、`prop:nfm-period-phase-invariant-descent`。全 n の q=2 完備局所値と三次分岐は `papers/sections/residual_boundary_products.tex` の `prop:nfm-boundary-saturated-active-potential`、`prop:nfm-boundary-period-local-kummer`。追加の ΔD 外非分岐性から大域式 [D] を得るには `lem:nfm-period-two-boundary-criterion` とこの局所値を組み合わせる。

高次元の Serre 合同類、中心的整数軌道、奇数次元の数値中央化群、七次元の障害は同節の `prop:nfm-highdim-rotation-serre`、`prop:nfm-highdim-central-shift-obstruction`、`cor:nfm-highdim-point-class-orbit`、`prop:nfm-odd-numerical-rotation-centralizer`、`prop:nfm-sevenfold-noncyclic-aut`。球面束と twist の存在・無限位数は Iliev–Manivel の既知結果であり、その数値作用と rotation 中央化群との比較を区別する。

随伴復元点型の定義と非空性は `lem:nfm-origin-active-right-adjoint`、`lem:nfm-dvr-top-line-lifting`、`prop:nfm-adjoint-point-type-nonempty`、有限安定化群と class torsor は `lem:nfm-generator-stabilizer-finite`、`thm:nfm-adjoint-point-finite-class-torsor`。n=3,4 の唯一 class、全奇数次元の数値自明性、全 n≥3 の最小実現次数は `cor:nfm-low-dimensional-canonical-adjoint-class`、`cor:nfm-odd-finite-stabilizer-numerical`、`cor:nfm-adjoint-point-realization-degree`。

全次元の Tate–Koszul 忠実性、五次元半 rotation の関手同定、非分裂 rotation の算術と Hesse 位相判定は本文に証明を記し、内部独立点検を済ませた。新規性の網羅的確認は未完了である。

計算資産の実行範囲・厳密証明書・原稿点検・組版・表示確認は `notes/validation.md` を正本とする。有限行列による積と一次項の検算、全次数の平坦性・同型延長・Kummer 降下の紙上証明、実際の組版を別の確認状態として扱う。以前の有効な計算資産と証明書は保持する。

補正の主証明は `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction`, `prop:nfm-mixed-fifth-reduction`, `prop:nfm-correction-point-cubic`, `cor:nfm-corrected-residual-jet`, `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir`, `thm:nfm-split-corrected-residual`。四次補正の証明は `papers/sections/fourth_correction.tex` の `prop:nfm-mixed-fifth-explicit`、`lem:nfm-fourth-center-locality`、`thm:nfm-mixed-fourth-potential`、`cor:nfm-fourth-jacobi-class`、`prop:nfm-fourth-uniform-witness`、`cor:nfm-corrected-fourth-obstruction`、`thm:nfm-fourth-algebraic-correction`。既存の主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. P0：中心の共役軌道・同種二因子・比較次数

**最初の対象は引き続き `n=4,k=2,m=0`。** 全O認識開上のPicard比較stack、自然な周期式、因子分離下の全中心同変核判定を入力とする。独立Hesse族の全中心同変核は一般点上に存在しない。指定中心μ3の非正規性・無限共役軌道を踏まえ、通常Kuの全同値へ中心標識を自動付与することを目標にしない。中心作用の共役軌道を保つ算術的分類と、同種二因子の新しい型を調べる。

1. **中心作用の共役軌道とGalois降下。** 二ブロックで球面捻りが作る無限共役軌道を入口とし、指定中心を保つ部分群Nと全Aut(Ku)の間で核の降下cocycleがどう変わるかを調べる。まず有限比較体上の既存G同変核を固定し、共役作用のGalois安定性とその実現gerbeを計算する。無限軌道を有限torsorへ根拠なく縮約せず、中心の共役類を内在的に特徴付けられるかは別の問いとして残す。
2. **同種二因子の混合Fourier–Mukai型の算術。** 幾何的には全Orlov中央化元がcoherent核へ持ち上がる。次はHom格子・CM・isogenyの定義体を固定し、Pell型と次数二反転型のGalois不変性、実現gerbe、period multiplierを計算する。`k≥3` の全H作用では混合が排除されるため、未解決は二因子に集中できる。
3. **scalarと位相の同時最小次数。** `α=Σδ_i` と内在的 `Cube(v_i(p_i))` を入力に、位相分裂体上の `ind(α)` と追加自己同型νの像を計算する。Hesseの位相のみの鋭い次数と、一般上界 `3^(2k−1)`／`3^(2k)` の鋭さは分ける。
4. **自然な射と認識開の境界。** 二捩れ点でθが零となる障害は残る。raw top syzygyを保持し、標的の退化、全O認識のfinite étale locus、等しいj、全intrinsic成分性を別々に調べる。自然な周期の全基本開での式を未解決へ戻さない。
5. **全第三根と中心一次変数。** `rO≃O(1)` の条件を外した `r³≃s³` の根を中心商と軌道対象から絞る。`k=2,m=1,n=5` は混合中心三次・全自己同型を再計算し、量子化側の `m>0,k≥2` の同変中心選択の適用範囲を確認する。

### 2. P1：複数ブロックを含む各intrinsic成分の表示を探す

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には古典Poisson論文の各ブロック型と量子化論文の族について、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. P2：1ブロックの残余位相と位相体上のscalar index

継続課題。全 n≥3 の q=2 完備局所値 γ_sc,n=[D_R]、D での付値1 mod3、位相体の次数三は決定した。全 orbit Hom、二次関係の三つの Smith 指数一、飽和した active 格子と三次関係の一次項、smooth potential 三次による指定 generic Isom の延長が証明の要点である。D で非分岐性を示して位相を消す方針は、この計算結果と両立しない。

次は β_n=γ̄_n/[D] の ΔD 外の divisor を調べる。現在の保証開は σ^j≠1 (j≤max(3,n−1)) を課しており、n≥5 の位数四 divisor などが ΔD 外にも除外される。一般混合係数だけでこの入力不足は解消しない。有限な低積の関係加群を飽和し、三次関係の付値と active potential の滑らかさを調べ、射影同型の延長を各 divisor で確かめる。既存の良い integral 表示の非分岐判定も、仮定を満たす場所で用いる。他の分岐を排除できれば、UFD と半古典条件により大域式 γ̄_n=[D] と次元間の一致を得る。

正準 frame の位相体 M/k_n は三次と確定したので、標識付き最小次数は 3 ind(α_M) に絞られる。位相体上で既知の点 Picard 障害 α が消えるかを、Tate–Weil pairing と具体的な三次体で検査する。q=2 での位相体が局所三分点体 K(∛D_R) と一致することだけから、一般体上で α_M=0 と結論しない。n=3,4 の全 full class 共通性と、n≥5 の正準強化 class に限った範囲を保つ。

n=3 の fractional Serre trace は他の divisor や大域式を検査する別経路として保持する。抽象的な Serre 自然性・反対操作だけでは指定周期の比較値は決まらない。full class の高次元全分類や coherent 中心線型性は、今回の有限な局所計算の前提ではない。

### 4. P3：強化点型classの相対構造と全型

全 n≥3 の一般一ブロック族で H_p=1、S_p=Spec(k_n)、強化点型の未標識最小次数三を得た。原点・rotation を保つ kernel の作用を、通常 Ext の回復、Adams Koszul 双対、Tate 再局所化、次数付き covering category の順で忠実に検出する。五次元の Clifford 候補も O≃ρ⁻¹[1]、ε=id と決定済みであり、これらを未解決の次課題に戻さない。

次はこの一意 class の相対的な構造と、代数的核の coherent な中心線型性を接続する。係数商と圏の導来 tensor、absolute perfect と relative perfect は区別する。随伴復元条件を外した全点型・任意 full class の分類や、その Galois 作用は未解決であり、既存の T-軌道と奇数次元の数値中央化群の簡約をそのために保持する。全自己同値群の分類を先に要求せず、七次元の球面 twist による非巡回性とも整合させる。

### 5. P4：非分裂点型と全型の実現次数

表示安定化子が自明な共通稠密開内では、非分裂形式でも強化点型 class は全 n で一つとなる。n≡1 mod3 の任意の非空開で実現した指数九族は、強化点型の最小次数九を全該当次元で達成する。普遍点 Picard gerbe の最小重み一階数九も保持する。

一方、rotation 自身の gerbe は偏極障害 β であり、α±β は index∣3 となるので、同じ族には三次拡大上の別型の full 比較がある。n=4 では全群分類により全型の最小次数が正確に三と決まり、高次元では他の rotation 軌道の元の体上の核を排除していない。次はこれらの他軌道と、点型を固定した一般の非分裂体の index 三／九を調べる。周期標識の μ₃ 位相は別段階である。

### 6. P5：点対応の幾何による残余射の認識

楕円点曲線 E_pt と残余 active 曲線 C_res の j の一致、θ_sc 上の階数九 torsor I_sc、点 shift の移送を得た。実次数三偏極と 2p,3p≠0 を満たす平行移動から、元の体上で滑らかな勾配型 active 代数を実現できる。次は、この active データから full な混合表示を回復する際の自由度と、残余圏の rotation から平行移動を内在的に認識する条件を明確にする。二曲線の平面同型は共通な良い稠密開へ全 O-降下した。点型自体の全 O-共変性は確定したので、この自然性を基準に、優先課題2の相対核構造と全型への拡張と、rotation からの内在的認識を接続する。

並行して、埋込み点対応から復元した二次関係・中心直線について good PBW 条件を有限条件で認識する。定常成分の一般の滑らかさ・連結性、八重被覆の分岐と自己同型も、成分や一般次数の判定に役立つ範囲で調べる。抽象的な定常成分だけから同じ復元ができるとは仮定せず、相対随伴の determinant 因子と Brauer 障害を保持する。

### 7. P6：公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・点微分による自然な残余射・同じ三次への比較とその降下へ置く。Fisher の ternary cubic 不変式環・微分付き軌道・§9.5 の Heisenberg 中央拡大、Fulton–Olsson の Hodge・modular forms・μ₂-gerbe、Knudsen–Mumford と Lieblich の determinant・twisted sheaf を既知の入力として比較し、Benoistの分離性・有限対角と有限表示降下を既知の入力として加え、曲線比較・混合三角性・正確な次数18・符号消滅とfull次数9・最高次 cohomology による index bound、full ambient の H_g 中央化群と混合定数降下による平面同型、残余 Picard 障害の exact index、parabolic 共変性からの平面同型の全 O-降下への適用を区別する。Galinat の window1・stabilization・rotation の同一規約、Orlov と Burke–Stevenson の a=0 比較を一次資料から確認し、graded purity と核 gerbe 上の階数三束への応用を分ける。Wang の Theorem 3.3、Hwang の symmetrizer 群、Toën–Vaquié の Lemmas 2.10, 3.25・Corollaries 3.22, 3.24、Bergh–Schnürer の gerbe と Brauer–Severi の分解を一次資料に即して比較する。Kontsevich 2001 §2.3 Proposition 6、Mori–Smith Theorems 1.2, 7.2、Lindberg–Pym 2024 Theorem 6.9、Dito・Shoikhet、Banks–Panzer–Pym と Buring の一次資料・公開 graph データとの比較を含め、形式対応・点曲線公式そのものと、本稿の混合 trace 補正・全 O-降下・残余比較を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。Liu の三次三様体、Huybrechts の very general な三次四様体の自己同値分類については、幾何学的一般点への適用と dg 核の一意性を区別し、本稿の class 降下・最小次数への応用と比較する。Iliev–Manivel の rank 九球面束と twist の既知結果を、高次元での全自己同値群と rotation 中央化群の区別に用いる。categorical Torelli や Fourier–Mukai partner の有限性を、固定標的への核の分類・作用の忠実性へ無条件に読み替えない。Murfet の Theorem 6.2 と式 (6.6) の residue trace は既知の入力であり、具体的な source/target trace の比較は別に必要である。Toën–Vaquié の Proposition 3.20 の boundedness と Hochschild 消滅を用いる有限安定化群の証明を、自己同値群全体の有限性と区別する。三分点の ASL₂(F₃) モノドロミー、点型の全 O-共変性、周期の三乗規格化、随伴復元点型の有限 torsor と高次元簡約を含め、外部査読・新規性の確認は未完了である。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
