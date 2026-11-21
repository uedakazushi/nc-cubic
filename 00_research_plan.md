# 非可換三次 n-fold：可換 Ku 実現を中心とする研究方針

2026年11月22日 / v50。再開時は本書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。正本は `uedakazushi/nc-cubic` の `main`、主公表原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)（日本語LuaLaTeX、著者欄空欄）。

## 公表用原稿と証明の正本

| 原稿 | 役割 |
| --- | --- |
| [nc-cubic.tex](papers/nc-cubic.tex) | 本文を持つ主稿。主予想、一般点可換復元、楕円windowと分離比較、残余圏の認識・可換実現の開性、三様体の点スキーム不一致例。 |
| [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) | 構造対象付きモジュライ、表示認識、相対点・Poisson幾何、Picard/Brauer/Kummer降下、周期位相と比較次数。 |
| [mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) | 混合族の中心・局所代数・全smooth locus、不変量、明示可換候補・Eckardt模型、被約point/Poisson不一致例。 |

研究方針とノートは三稿で共有する。各証明は一つの本文を正本とし、他稿では定理番号と稿名を参照する。組版の共通設定は `papers/common/preamble.tex`、書誌は `papers/references.tex`。主比較に必要な楕円windowは主稿の `comparison_foundations.tex` に置き、精密な核の降下を主比較の前提にしない。混合稿の余有限Ku実現は主稿の比較と開性を入力とする。

## 主予想と未解決の核心

**Main conjecture（主予想）**：任意の滑らかな非可換三次 n-fold 𝒳 に対して、同じ次元の滑らかな可換三次超曲面 X が存在し、Ku(𝒳)≃Ku(X) となる。

まず基礎体をC、次元をn≥3とし、通常のC線型dg Morita同値の存在を最優先にする。指定混合族について、明示可換候補への実際の次数付き比較核は一般点でも未構成である。次の着手先はc=0の根スタック模型に対する非可換側の対合付きHochschild指標の検査と、内部次数・三次周期を保つ比較核の構成であり、その後に全smooth係数へのDVR延長を検討する。

**「任意」をgenericへ置き換えない。** 全対象の内在的な定義・認識、全O-marked moduliの代数性と表示による被覆は未完成である。少なくとも既存のAS正則周囲代数Bの中心三次商A=B/(w)は、良い開の外も研究対象とする。既知の一ブロック局所型stackの対象を全nc cubicと定義し直して主予想を解いたとはしない。point functorの表現可能性・表示独立性も必要な範囲で解く。主予想の定式化の正本は主原稿の `conj:nc-main` である。

## 研究の進め方と達成基準

主予想の解決に向けて、実際のKu比較を構成できる対象範囲を広げる。O-markedモジュライ、点対応からの復元、残余Poisson射、全O同値・中心作用の認識は、そのための手段として位置付ける。比較次数・位相・全自己同値の精密化は、可換実現の存在と対象範囲に関わる障害を解消するときに優先する。point/Poisson一致への素朴な期待が失敗する例は、主予想の意味を明確にする補助的な内容として本文に置き、Introductionから参照する。

主予想の肯定結果の達成基準は、対象範囲と仮定を明記し、実際のKu同値を構成することである。point/Poisson一致を併せて述べる場合は、同じXについてpoint schemeと零スキームの同型まで証明する。不一致の例では全候補を排除できる範囲とその入力を明記し、可換Ku比較を必要とする三様体の論法と、全可換五様体を一括排除する論法を区別する。楕円成分のjの一致、点集合の一致、有限jet、幾何学的一般点だけの同値を全主予想の解決と扱わない。一般体上の核降下や全族の大域核sectionは、C上の存在とは別の強化として扱う。

一般点可換復元・一ブロックモジュライ・満支持型比較は有効な部分結果として保持する。中心変数を加えた分離テンソル型では全固定複素点の可換Ku実現まで進み、定数型混合族にも余有限可換実現を得た。指定二因子では非smooth集合を正確にV(P64)と決定し、同じ判別集合と局所節点を持つ明示可換候補も得た。c=0と定常normの全64根では両側が滑らかであるが、この候補へのKu同値は一般点でも未証明である。主予想の核心は中心三次を保つ実際のcurved/MF比較・次数付き核の構成と、そのDVR延長にある。より一般の混合型、実楕円因子仮定の外の境界、全intrinsic成分の被覆も残る。point/Poisson一致は全対象に期待できないため、その修正版を別の最優先予想として立てず、既存の一致例・不一致例と必要な検証を保持する。

## 補助的な例：point/Poisson一致への素朴な期待の限界

同じ可換Ku標的X上でPoisson構造πを選べばPt(𝒳)≃Z_X(π)も実現できる、という素朴な期待は一般には成り立たない。これを独立した予想として掲げず、本文の注意 `ppz:rem:naive-expectation` と以下の例で扱う。Z_X(π)は切断としての零スキームであり非被約構造も含め、point shiftの固定点とは区別する。可換対象ではπ=0を許す。

**被約化しても一致しない五様体の例。** `ppz:thm:isolated-zero-dimension` は、滑らかな可換三次 n-fold のPoisson零集合に孤立点があれば n=3k、一般階数2kであり、その局所零スキームが零次元完全交叉であることを示す。入力は `poisson-cubic` の固定版の全次元正規形であり、pure blockの楕円性を仮定しない。特に全ての滑らかな可換三次五様体の全Poisson零集合には孤立点がない。一方、指定混合族の定常normの全64根ではsourceとその全coherent Kuはsmooth properで、Pt(A_c)=E₁⊔E₂⊔{p_c}は被約である。`ppz:cor:reduced-point-poisson-counterexample` はこれにより全可換五様体・全Poisson構造を排除する。c=−44828に有理係数の一例を固定できる。この例は可換Ku標的の存在を必要とせず、主予想の真偽には結論しない。

**実Ku比較を伴う三様体の全スキーム不一致の例。** `ppz:cor:complex-counterexample` は、関係式と中心元を有理数係数で明示したC上の良い一ブロック三次三様体 A★ を与える。h=1、可換標的のHesse係数は17/9に固定できる。実Sklyanin因子を `esi:prop:factor` で確認し、楕円因子と二つのA₂因子から `csc:cor:fermat` でKu比較を直接構成する。反例の証明に一般点の形式復元・C閉点へのspreadは不要である。A★は主予想を満たすが、同じKuを持つどの滑らかな可換三次とどのPoisson構造を選んでも全point schemeは零スキームと同型でない。非被約な三つの定常点の長さ八局所環を使う反例であり、自然な残余pairでは被約部分は一致する。二つの反例の機構と入力を区別し、成立範囲を検証せず修正版を新予想として採用しない。Ku比較はC上の存在であり、有理係数の表示からQ上の比較核の存在を結論しない。

この具体例の「良い」は点スキームの条件を指す。全O表示stackの全相対入力に属することをh=1で独立に確認したという意味ではなく、それらを反例の証明に用いない。

異なる射影表示を持つ対象間の「一致」はスキーム同型として定式化し、射影埋込みを保つ同型、点対応も保つ同型、族での自然な降下は強化問題として区別する。埋込み版には一ブロックの障害があるため、抽象スキーム版の証明で埋込み保存を無断に仮定しない。どの意味が成立・不成立かを明示して検証する。

## 現在の到達点と適用範囲

| 対象・結果 | 主予想への到達点 | 関連する幾何と比較の限界 | 正本 |
| --- | --- | --- | --- |
| 一般中心三次変形 | 明記した平坦・可換特殊化・滑らかさの仮定の下で、一般係数体の有限拡大上に全coherent Ku比較。C上の全固定点や全内在的対象の表示を与える定理ではない | point scheme全体の零点比較は含まない | `generic_recovery/` の `cft:thm:complete`, `gdr:thm:generic`、[基礎ノート](notes/recovery_foundations.md) |
| 良い一ブロックの共通稠密開 | 同じX_resへの有限被覆上のKu比較、全O降下する残余Poisson射。形式MF・window・飽和の明記した入力を使う | Pt(A)=E⊔D、Dは型(2,2,2,3)。Eと残余active曲線の比較はあるが、全Dの一致は別問題。trace–Hessian対象と残余対象も区別する | `relative_points.tex`, `poisson_morphism.tex`, `residual_algebraic.tex`, `residual_point_scale.tex` |
| 満支持k≥2,m=0の楕円tensor型 | 実際の因子積・rotation比較から可換分離和へのKu同値。明記した実因子仮定の下で同じj・特殊j・非零二捩れも許す | 同じ標的上のπについてPt(A)=Z_X(π)=⊔E_iをスキームとして証明。純成分の近傍で他block座標を単元消去するため非被約試験底にも成立 | `two_block_points.tex`, `multiblock_noncommutative_product.tex`, `multiblock_rotation_comparison.tex`, `point_poisson_split.tex` |
| 中心変数m≥1を持つ分離型、N=3k+m≥5 | 実楕円因子・全a_i≠0・中心三次gのJacobian環有限次元の下で、任意の点曲線方程式f_iに対しX=V(Σf_i+g)への実Ku同値をC上で直接構成 | m=1,g=cu³,c≠0では同じX上でPt=Z=⊔E_i。m≥2では定常完備局所環J[[t_1,…,t_{m−2}]]、length J=8^k。自然な零スキーム側のJ_clと比較 | `central_split_comparison.tex`, `central_split_points.tex` |
| 固定有理係数の一ブロック三様体 A★ | h=1,λ=17/9。指定Ω・THCR商を直接確認し、楕円因子＋二つのA₂因子で全coherent Ku比較 | 局所環J_1とJ_17/9の厳密j不一致、任意supportの局所補題、12点のHessian分類により全πを排除。BMMSで全Ku標的も排除 | `explicit_sklyanin_input.tex`, `point_poisson_obstruction.tex` の `ppz:cor:complex-counterexample`。Mayanskiy・BMMS等の既知入力を明記 |
| S(1,−1,−1)の定数型混合kブロック | 全αで有限中心・PI6・正則中心上Azumaya、任意固定係数で余有限全coherent Ku可換実現。指定二因子は全14節点のNCCR局所形・全simpleを決定し、非smooth集合を正確にV(P64)と証明 | c=0と定常normの全64係数はsmooth proper。全smooth係数での可換Ku比較は未解決。norm点の残余Extは0次1・1次10、既存100simpleのpd5も保持 | 混合稿の `mixed/local_orders.tex`, `mixed/smooth_locus.tex`, `mixed/relative_smoothness.tex`。`cmo:thm:fourteen-node-orders`, `cmo:thm:exact-sixty-four`, `cmo:cor:fixed-zero-norm-smooth`, `cmo:cor:cofinite` |
| 全Poisson構造の孤立零点制約と混合五様体 | Ku比較を入力としない。norm根での主予想は未解決 | 孤立零点にはn=3k・一般階数2kが必要で、局所零環は0次元CI。normの全64根では被約point/Poisson一致への期待も成立しない。c=−44828を明示 | 混合稿の `mixed/poisson_limits.tex`。`ppz:thm:isolated-zero-dimension`, `ppz:cor:reduced-point-poisson-counterexample`。固定版の全次元正規形を入力 |
| 指定混合族の明示可換候補 | λ²=28/27で臨界値・P64・局所五次元節点が一致。c=0にはEckardt点からの四次二重被覆とcrepant解消模型。候補へのKu同値は一般点でも未証明 | 自然なPoisson零スキームは滑らかな各cでE₁⊔E₂。norm根では全ての別標的・別πも上の定理で排除 | 混合稿の `mixed/commutative_candidate.tex`, `mixed/eckardt.tex`。`cmo:thm:commutative-discriminant-candidate`, `cmo:prop:zero-eckardt-resolution` |
| 指定族の全smooth領域の不変量 | U=A¹∖V(P64)上の実相対smooth proper模型を構成。全cでHH₀の次元2、HH±₁は各21。有理数値Euler形式も可換候補と一致 | 圏同値・積分数値格子・point比較は導かない。c=0の非可換対合のHH±₁指標は未計算 | `cmo:prop:full-relative-hh`, `cmo:cor:rational-euler-comparison` |
| c=0の可換標的の実残余模型 | T=Bl_Y P⁵の分離分岐H′⊔Z′に沿う根スタック上で、16明示例外対象の右直交K≃Ku(X₀)^μ₂とperfect射影核を構成。指標線束Nによる再同変化で通常Kuを回復 | Ku(Y)とKu(Z)のHHの直和とは一致するが、両圏の半直交分解を得たとはしない。A₀からの比較核は未構成 | `cmo:thm:eckardt-root-residual`, `cmo:cor:eckardt-equivariant-hh`, `cmo:prop:zero-involution-hh` |
| 固定曲率の非次数付きaffine MF | 一因子の全sと混合族の全cで、冪等完備後の実dg Morita比較。悪い値はCl₃・Cl₆、良い値は双方零 | 全smooth cで射影Kuは非零なので、このaffine圏を介する同値は不可能。内部次数・錐の原点・周期を保持する比較が必要 | `cmo:lem:isolated-azumaya-mf-completion`, `cmo:prop:pointwise-affine-mf-comparison` |
| n≠4の通常Artin変形・開性とtrait核判定 | 実smooth proper dg族で可換Ku実現locusがZariski開。generic同値を与える実perfect核の特殊化は二つのunit/counit coneの長さd_R=0と同値 | 開性・連結性や両側のsmooth proper性から閉性は従わない。核の存在自体とπ・point functorの延長は別問題 | `residual_categories.tex` の `thm:nf-residual-formal`、`geometric_realization_locus.tex` の `grl:thm:open-locus`, `grl:prop:trait-kernel-test` |

全原稿の証明を今回独立に再検証したという表ではない。今回の追加結果・読解点検・計算・組版・表示・保存の状態は [notes/validation.md](notes/validation.md) に記す。新規性の網羅的確認と外部査読・形式証明は未完了。

## 優先する次の課題と具体的な着手

### P0：主予想の存在領域を全対象へ広げる

1. **明示可換候補への実際の比較核を構成する。** 検査例は `cmo:ex:sixty-four` のk=2,m=1,n=5、α¹=(1,4,9)、α²=(16,25,49)、重み1,100。G_α=(x³+y³+z³+xyz)/3−u²(α₁x+α₂y+α₃z)、λ=2√21/9として、候補はX_c=V(λ(G_α¹+100G_α²)+cu³)である。λ²=28/27によって臨界値が一致し、両側のsmooth locusは正確にP64(c)≠0、特異点の完備局所型も一致する。しかし既存の余有限可換実現はこの指定候補への一般点同定を含まない。まず中心三次を保持するcurved/MF比較、または全次数付き残余圏の実perfect核を作り、随伴・unit・counitを具体化する。通常のambient derived Morita同値でD_αを多項式環へ置き換える方法は、HH⁰である中心の特異性が異なるため使えない。C[[h]]では1−hが単元なのでh↦1の評価準同型は存在せず、h進形式比較から進むには代数化と当該係数での定義を別に証明する。
2. **c=0の根スタック模型へ非可換比較核を構成する。** X₀=V(G−u²L)、Y=V(G,L)、Z=V(G)に対して、T=Bl_Y P⁵と根スタックℛ=√[2]{(T,H′⊔Z′)}、16例外対象、Kへの射影核、指標線束NとN²≃Oのcoherenceは `cmo:thm:eckardt-root-residual` に明示した。A₀のu↦−u作用と中心u²を使ってKu(A₀)^μ₂からKへの核を作り、16直交条件と単位・余単位を検査する経路を優先する。得られた核がN作用に同変なら再同変化で通常Kuを比較できる。ただし対合保存は主予想の追加条件であり、その経路の障害を主予想の反例とはしない。全Uで通常HHと有理Euler形式は一致する。可換側のHH±₁の対合固有次元は(5,16)、同変KuのHHは次数−2,…,2で(1,5,24,5,1)であり、非可換側の同変指標を次の検査とする。Ku(Y),Ku(Z)のHH一致から圏を相殺しない。
3. **実kernelを得た後、全smooth係数へDVRで延長する。** 一般点での同値、perfect整核の存在、特殊点での同値性を三つの段階として扱う。`grl:prop:trait-kernel-test` により、最後の条件は生成対象上のunit/counit coneの有限長総和d_R=0で判定できる。正のd_Rは分岐指数eの底変更でe倍となり、固定核の不良特殊化は有限分岐だけでは消えない。c=0とnormの全64根は両側smoothであることが既知なので、そこで具体的な行列と必要な核の整格子を構成する。開性と連結性だけで全係数へ延ばさず、両側smooth proper・generic同値でもspecial同値が失われるF₂/F₀の障害例を踏まえる。
4. **指定族の外へ広げる。** 一般αの例外判定は中心の節点性とΩ切断の非等方性が失われるlocusから着手する。指定族で得た全14節点のEnd_R(R^{⊕a}⊕I^{⊕b})模型、全simple分類、二次元の普遍高次作用、character非検出のpd∞例、100simpleのpd5、64定常点の残余Extを保持する。より一般の混合表示と全intrinsic対象の被覆は引き続き未解決である。

### P1：主予想に必要な認識・降下

全O認識、相対双対・coherent飽和、点関手の表示独立性、Ku比較の実perfect核を必要な範囲で整える。一般点・形式完備化・有限Artin jet・固定幾何点を区別する。全作用付き比較を通常Ku比較の必要条件と誤認しない。二ブロックの指定中心μ3は通常Kuの全自己同値群で非正規である。

### P2-A：point/Poisson一致・不一致の例の検証

以下は本文の例と補助的な幾何比較を支える課題であり、主予想と並ぶ存在予想や最優先の研究目標には置かない。既知の証明と計算を保持し、公表に必要な依存関係・適用範囲・文献比較を点検する。

1. **孤立零点定理と被約反例の外部検証・新規性調査。** 全Poisson構造への適用は `poisson-cubic` commit `9f91efa3465f18219c36c31750f1e66220faeaa7` の `thm:pg-normal` に依存する。表示・Jacobi延長・Hessianの基点自由性・Lie代数の根基排除を含む入力と、そこからの孤立零点排除・0次元CIの証明を分けて検証する。五様体では全標的を一括して排除でき、norm根で可換Ku核を構成することは反例の未完了条件ではない。正式な新規性の確認と外部査読・形式証明は未完了である。
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
