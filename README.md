# 非可換三次超曲面の可換復元とモジュライ

2026年11月21日 / v31。日本語LuaLaTeXによる主論文と再現資料。再開時は [研究方針](00_research_plan.md) を最初に読む。

**本repoの公表用主原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex) のみ。** 完備MF移送、一般中心三次変形の可換復元、良い一ブロックのO-markedモジュライ、満支持複数ブロック型の次数付き表示、残余Poisson射、Kuznetsov成分の比較と降下障害を扱う。量子化の全次元・全ブロック存在証明と独立した原稿・計算・ノートは [cubic-quantization](https://github.com/uedakazushi/cubic-quantization) に移した。古典的Poisson正規形・退化・モジュライは [poisson-cubic](https://github.com/uedakazushi/poisson-cubic) を参照する。

## 可換復元・モジュライの内容

完備MF移送と一般点の全coherent残余圏のKu比較（旧 `poisson-cubic` 論文B）の全証明をこの主原稿へ統合した。一般の中心三次変形の基礎定理は、一ブロック型のモジュライ構成とは独立した仮定の下で述べる。外部の未公表入力は `poisson-cubic` の古典Poisson論文と、`nc-cubic-threefold` の三様体固有の指定版である。三様体固有の全Abel圏形式近傍と相対射はそのrepoに保持し、全次元の復元・Poisson射・点型算術は本repoを正本とする。量子化の全証明は別repo `cubic-quantization` に置く。

- [可換復元の基礎節](papers/sections/generic_recovery/main_result.tex)：完備MF比較 `cft:thm:complete`、一般点の可換復元 `gdr:thm:generic`、局所模型・window・飽和・低積の積分・明示Hesse模型を含む全9節。主原稿から読み込む。
- [可換復元の研究上の障害と再現入口](notes/recovery_foundations.md)：定義体、有限降下、symmetrizer、具体例の規約、残るkernel有効化。
- [可換復元の検証スクリプト](computations/verify_generic_cubic_descent.py)：既知の勾配空間の積分と非分裂symmetrizer。`verify_complete_curved_transport.py`、`verify_three_object_window.py`、`verify_recovery_example.py` も同じ `computations/` に置く。


- [公表用研究稿](papers/nc-cubic.tex)：中心復元、局所一ブロック型の O-marked DM stack と Brauer 障害、相対点関手と中心商の復元、trace–Hessian による Poisson 対の開部分との同型、残余復元との比較障害、次数9の代数的 Poisson 補正、形式 support 保存、全混合五次 tensor と残余四次 potential、四次の比較障害と新しい代数的補正、split 族の残余比較、一般混合係数の代数的残余三次・点曲線の j の一致・点微分による一般有限な符号商 Poisson 射、有限被覆上の Ku 比較、点型の全 O-降下と scalar 障害、n=3,4 の全 full class 降下と最小比較次数三、三分点体の次数九と ASL₂(F₃) モノドロミー、固定 tensor の very general な超越性、Jacobi スキーム、残余圏の通常 Artin 形式認識。
- [研究ノート](notes/research_notes.md)：主張の依存・適用範囲、反例・障害、文献の確認箇所、次の計算の入口。
- [検証範囲](notes/validation.md)：原稿点検・組版・厳密計算を区別した確認状態。
- [量子化の検証状態](https://github.com/uedakazushi/cubic-quantization/blob/main/validation_quantization.json) と [再現入口](https://github.com/uedakazushi/cubic-quantization/blob/main/computations/quantization/README.md)：中心元・多ブロック計算と独立量子化稿の確認範囲。
- [相対構成の補助ノート](notes/relative_construction_obstacles.tex)、[中心二チャートの補助ノート](notes/central_cubic_generic_smoothness.tex)、[未照合の外部資料](notes/unresolved_external_sources.md)：本文へ無条件に取り込まない技術的障害・残る照合範囲。
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
- [四次補正の本文](papers/sections/fourth_correction.tex)：上の有限計算を一般次元の証明と Poisson moduli の射へ統合する主原稿の分割ファイル。
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

外部の古典入力は [poisson-cubicの論文](https://github.com/uedakazushi/poisson-cubic/blob/main/papers/poisson-cubic.tex) のPoisson正規形であり、代数的量子化の入力は別repoの [cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) である。旧論文Bの一般点復元は現行主原稿内に証明を統合した。統合は結果を新たに今回証明したという意味ではない。

## 満支持複数ブロック型の到達点と次の目標

**満支持`k≥2,m=0`の次数付き表示について、次元`2k`の滑らかな既約DM stackを構成した。** `B=⊗S_i`, `A=B/(Σa_iΩ_i)`、全係数非零、滑らかな楕円因子で`p_i,2p_i,3p_i≠0`、相異なる一般`j_i`という非空開の結果。共通grading scalarを除いた幾何的慣性は`(H_27^k)/Δμ_3`、位数`3^(3k−1)`であり、**二ブロック三次四様体では次元4・慣性243**となる。これは射影的なgraded表示のstackで、全O-marked圏のstackとの同定は未証明。

- [点対応とZhang twist](papers/sections/two_block_points.tex)：点スキームは`⊔E_i`。点対応から二次関係を復元すると`9 binom(k,2)`次元の余分な関係が入り、二ブロックでは24対15となる。非自明なblock `μ_3` twistは同じSerre指数のVeroneseとO-marked圏を持ちながらgraded非同型。
- [中心・中心直線・自己同型](papers/sections/two_block_algebra.tex)：三次中心の次元`k,k−1`、二次包絡と商直線の復元、中心係数の尺度商`B(μ_3^(k−1))`、全graded慣性を証明。中心係数比を新たな粗modulusとして数えない。
- [表示スタック](papers/sections/multiblock_presentations.tex)：普遍平面三次の相対Jacobianから非空開を構成し、局所自由性・任意底変更・全graded同型を検証。scalarを除く商では実際の大域代数の存在に持上げ障害が残る。
- [二ブロック完備復元](papers/sections/two_block_recovery.tex)：既存MF定理の下で`μ_3`同変比較を選び、復元potentialが`W_1(x)+W_2(y)`に分裂する。一変数一般点の有限拡大上のKu比較も仮定確認後に得る。同変代数化・全O降下・点曲線との同定は未証明。
- [厳密有限検算](computations/verify_two_block_structure.py)：有理Sklyanin因子の次数4までの関係と中心、Heisenberg中央積の位数243を再現。一般証明と圏同値は計算の結論に含めない。

**P0の次の一手**は、二ブロックで全O保存同値と次数一の根のgroupoidを認識し、相対Serre・飽和を確保して表示stackから内在的モジュライへ進むこと。同時に`μ_3`同変比較核を代数化し、可換側の既知の同変Ku／楕円積比較に接続する。その後`k=2,m=1,n=5`を扱う。量子化の`m>0,k≥2`同変中心選択は外部repoでも未完成であり、既知入力としない。

既存1ブロック型の大域周期位相`β_n=γ̄_n/[D]`と位相体上scalar indexはP2として保持する。具体的な仮定・証明箇所・残る課題は[研究方針](00_research_plan.md)、実際の検証範囲は[検証記録](notes/validation.md)を参照する。新規性の網羅的確認・外部査読・形式証明は未実施。

**一般次元の O-marked moduli、point scheme、Poisson 多様体のモジュライへの射、Kuznetsov 成分の比較**を中心に進める。各既約成分の general / very general な対象を優先し、次元に一様な定理と族の構成を目指す。general な稠密開と very general な点集合、一ブロックの表示成分と全モジュライの成分は区別する。

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

点型の比較と算術的障害については、次の適用範囲を区別する。平面同型の分裂は [点曲線・尺度の本文](papers/sections/residual_point_scale.tex)、点型・full class の証明は [点の平行移動と核の Picard 類の本文](papers/sections/residual_kernel_point.tex)、周期位相の不変量降下は [周期位相の節](papers/sections/residual_period_descent.tex) にある。

| 対象 | 現行稿に証明のある結果 | 証明の入口と限界 |
|---|---|---|
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

必要な環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）、Python 3・NumPy・SymPy、および C++17 対応コンパイラ（GCC または Clang）。PDFと検証用の中間ファイルは `build/` に生成し、Gitでは追跡しない。

リポジトリのルートで実行する：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 computations/verify_two_block_structure.py
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
latexmk papers/nc-cubic.tex
```

引数なしの `latexmk` は上の二論文を組版する。`python3 scripts/check_sources.py` は各論文の入力・引用・ラベルを独立に検査する。量子化の再現コマンドは `notes/cubic_quantization.md` と量子化の検証資料を参照する。

点障害、Jacobi・Hessian 補正、境界 MF と低積の計算資産を保持する。各検証器の実行・厳密証明書・原稿点検・組版・表示確認の状態は [検証範囲](notes/validation.md) を参照する。有限計算による恒等式確認と、全次数の平坦性、同型延長、Brauer 類、圏同値、Kummer 降下の証明は区別する。

active 不変量の検算は rψ=ar、判別式・Jacobian の公式を有理係数で確認する。active符号の検算はQQ(ζ)上のHesse群の24要素・閉性・不変量・二次指標と、体次数の消去式を確認する。有限対角によるPoisson対の近傍延長・同変降下とχ_actの消滅は、この計算ではなく本文の証明による。幾何学的一般ファイバー、全次数混合三角性、正確な一般次数18は本文の証明に依る。中心・Hessian と幾何補正の検算は有理係数の記号恒等式、八次自由代数の trace、Jacobi 商の双対証明書、普遍 cofactor 恒等式と Hesse の j 差を再現する。補正検算では十個の独立係数を持つ三変数三次、任意の対称行列、二パラメータ Hesse 中心の係数変換、混合項の復元行列、九重被覆の分岐、Weyl の整数重複度と四次不変式も確認する。混合五次の検算は保存した73項の graph データから β,γ を評価し、四次 potential の検算は中心 symbol の全係数恒等式・純中心項・尺度・全次元の非消滅証明書を確認する。入力論文の混合中心公式の非可換中心性、graph 積分そのもの、圏同値はこれらの記号計算で再検証しない。組版設定は既存の repo ルート基準のパスを維持し、PDF と SyncTeX を `build/` に揃えている。研究hubの現行テンプレートと設定も参照し、LaTeX Workshop の推奨拡張を指定した。

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
