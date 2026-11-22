# 非可換三次 n-fold：可換 Ku 実現を中心とする研究方針

2026年11月22日 / v59。再開時は本書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。正本は `uedakazushi/nc-cubic` の `main`、主公表原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)（日本語LuaLaTeX、著者欄空欄）。

## 公表用原稿と証明の正本

| 原稿 | 役割 |
| --- | --- |
| [nc-cubic.tex](papers/nc-cubic.tex) | 本文を持つ主稿。主予想、一般点可換復元、楕円windowと分離比較、残余圏の認識・可換実現の開性、三様体の点スキーム不一致例。 |
| [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) | 構造対象付きモジュライ、表示認識、相対点・Poisson幾何、Picard/Brauer/Kummer降下、周期位相と比較次数。 |
| [mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) | 混合族の中心・局所代数・全smooth locus、任意固定楕円因子の全許容PBW・中心比較、滑らかな中央flagによる多中心比較、零係数の球面接着と有限MF模型、指定h候補の一般点核と整延長、被約point/Poisson不一致例。 |

研究方針とノートは三稿で共有する。各証明は一つの本文を正本とし、他稿では定理番号と稿名を参照する。組版の共通設定は `papers/common/preamble.tex`、書誌は `papers/references.tex`。主比較に必要な楕円windowは主稿の `comparison_foundations.tex` に置き、精密な核の降下を主比較の前提にしない。混合稿の余有限Ku実現は主稿の比較と開性を入力とする。

## 主予想と未解決の核心

**Main conjecture（主予想）**：任意の滑らかな非可換三次 n-fold 𝒳 に対して、同じ次元の滑らかな可換三次超曲面 X が存在し、Ku(𝒳)≃Ku(X) となる。

まず基礎体をC、次元をn≥3とし、通常のC線型dg Morita同値の存在を最優先にする。任意に固定した滑らかな標準Sklyanin因子の組、k≥2、固定非零重み、一つの共有中心変数について、指定境界を保つ全ての因子別PBW・中心三次補正の残余線束圏を可換三次と普遍Morita比較した（`emc:prop:coverage`, `euk:thm:universal-kernel`）。異なるj、同種・CM、二捩れ、有限位数・無限位数を許す。二捩れでない因子は平行移動後の関係式の線形三方向、二捩れ因子は中心へ加えるu倍の平方三方向を一次係数tとする。標的はX=V(G+uQ(t)+u²L(t,α)+u³C(t,α,c))、L=𝔄α+R₂(t)、C=κc+R₁,₁(t,α)+R₃(t)で、𝔄は可逆、κ≠0。可換smooth開では相対perfect核と全coherent Ku同値を得る。定数Bocksteinは3k次元の同型、一次Bocksteinは3k方向で単射だが、比較の存在は単射性を前提としない。各固定tの一般αに対して8^k個の相異なる悪いcと各可換標的の唯一の通常二重点を得て、全係数・各固定tの判別超曲面は既約被約、臨界点のaffine空間が正規化となる。固定(t,α)の一変数特殊化には重複根を許す。

二中心の全許容因子別表示では、中央切断の判別形式 Δ(u,v) の次数は3·8^kであり、Δが恒等零でない開集合 U_cut は「残余線束圏がsmoothな中央切断が一本存在する」条件を正確に表す（`mcpn:prop:ray-discriminant`）。その切断を固定すれば、残る全横断係数上で実Morita核を構成でき、最上段がsmoothなとき同次元の滑らかな可換三次との全coherent Ku同値を得る（`mci:thm:iterated-kernel`）。最後のv³係数の悪い値は重複度込みで2·8^k個。任意個の中心でも、途中の残余線束圏がsmoothな中央flagを仮定すれば反復できる。全smooth対象で良い切断・flagが存在することは未解決である。

同一S(1,−1,−1)の既存結果では、指定規約でκ_k²=27/28、κ_k=3√21/14を保持する（`mcs:cor:universal-scale`）。Heisenberg同変な一次像は純ブロックJac₂の直和で、比較の七定数形のうち六定数χ_k,A_k,…,E_kは未数値化（`lec:thm:seven-scalar-form`）。一般の異なる因子へこの数値κを流用しない。指定二ブロックのP64・norm全64根・有限中心と局所型も保持する。残る核心は、全中央切断が特異となる部分、全smooth対象での良い中央flagの存在、因子moduli上の核選択・降下、全intrinsic対象の表示被覆である。一般の比較係数、一般PBW族のPI性・有限中心性、選択済みh一般点核のdefect零特殊化も未解決。

**「任意」をgenericへ置き換えない。** 全対象の内在的な定義・認識、全O-marked moduliの代数性と表示による被覆は未完成である。少なくとも既存のAS正則周囲代数Bの中心三次商A=B/(w)は、良い開の外も研究対象とする。既知の一ブロック局所型stackの対象を全nc cubicと定義し直して主予想を解いたとはしない。point functorの表現可能性・表示独立性も必要な範囲で解く。主予想の定式化の正本は主原稿の `conj:nc-main` である。

## 研究の進め方と達成基準

主予想の解決に向けて、実際のKu比較を構成できる対象範囲を広げる。O-markedモジュライ、点対応からの復元、残余Poisson射、全O同値・中心作用の認識は、そのための手段として位置付ける。比較次数・位相・全自己同値の精密化は、可換実現の存在と対象範囲に関わる障害を解消するときに優先する。point/Poisson一致への素朴な期待が失敗する例は、主予想の意味を明確にする補助的な内容として本文に置き、Introductionから参照する。

主予想の肯定結果の達成基準は、対象範囲と仮定を明記し、実際のKu同値を構成することである。point/Poisson一致を併せて述べる場合は、同じXについてpoint schemeと零スキームの同型まで証明する。不一致の例では全候補を排除できる範囲とその入力を明記し、可換Ku比較を必要とする三様体の論法と、全可換五様体を一括排除する論法を区別する。楕円成分のjの一致、点集合の一致、有限jet、幾何学的一般点だけの同値を全主予想の解決と扱わない。一般体上の核降下や全族の大域核sectionは、C上の存在とは別の強化として扱う。

一般点可換復元・一ブロックモジュライ・満支持型比較は有効な部分結果として保持する。一つの中心変数を共有する任意の固定楕円因子の全許容PBW表示では、非分裂counitの比較が三項までで決まり、実際の全係数核を得た。多中心では滑らかな切断から比較を反復し、現在の核心は全smooth対象での良いflag、全交換構造、因子を動かすときの降下、および全intrinsic成分の被覆である。数値係数の具体化は存在定理を具体化する課題として並行し、全対象への拡張を置き換えない。

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
| 任意固定楕円因子の全許容PBW・中心三次 | 全係数の残余線束Morita比較、可換smooth開の相対perfect核・全coherent Ku。二捩れβも含む | 固定因子のC上の存在。因子moduli上の核選択・良いflagの存在・全intrinsic被覆は残る | `emc:prop:coverage`, `ebk:lem:boundary`, `ebc:prop:constant-iso`, `ebc:thm:first-injection`, `euk:thm:universal-kernel` |
| 多中心の全許容因子別表示 | 非被約係数環でも一次・二次・三次の中心形式で全表示を分類。係数数3km+3k binom(m+1,2)+binom(m+2,3)、二中心15k+4。中心列は任意順序で正則 | 因子を混ぜる一般PBW関係や全intrinsic被覆を含まない | `mcp:thm:normal-form`, `mcp:prop:free-quotient` |
| 二中心のU_cutと滑らかな中央flag | 一本のsmooth中央切断を固定した全横断係数で実線束Morita比較。smooth最上段では全coherent Ku。良いflagがあれば任意mへ反復 | v³判別は次数2·8^k。全smooth対象でのflag存在、W_it=W_pol、横断二項写像Bの可逆性は未証明 | `mci:thm:iterated-kernel`, `mci:cor:finite-discriminant`, `mci:cor:smooth-flag` |
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

1. **滑らかな多中心対象で良い中央切断・flagが存在するかを決める。** 二中心では `mcpn:prop:ray-discriminant` の全係数消滅 Δ≡0 と、元の残余線束圏のsmoothnessとの関係を調べる。良い切断が一本あれば `mci:thm:iterated-kernel` が全横断係数を比較するので、切断を持たない部分が次の核心となる。まず分離端点と既知の有限中心部分でBertiniの仮定を確認し、一般PBW族では実proper線束模型のどの追加条件が必要かを切り分ける。Rennemo–Segal–Van den Bergh Proposition2.1の有限中心仮定やsmooth dg圏への未証明の拡張を暗黙に使わない。
2. **必要な混合情報を実模型で同定する。** `tcr:prop:beck-chevalley` と `tcr:prop:joint-comonad` は実二重制限・joint comonadを与えるが、全coherent分配データの有限な比較塔はまだ同定していない。同一の二軸から全体のsmoothnessが異なる `tcr:ex:same-axes` を基本検査例とし、uv・u²v・uv²項の指定MF上の計算から、全残余gaugeを許す比較へ進む。単純な偏極候補 W_pol と逐次標的 W_it の一致、横断二項写像Bの可逆性も未解決である。
3. **全intrinsic対象の認識と表示被覆を進める。** 任意個の中心の因子別PBW正規形は `mcp:thm:normal-form` で得たが、因子を混ぜる関係や全内在的成分の被覆を与えない。全対象という主予想をこの表示族やU_cutへ限定しない。

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
