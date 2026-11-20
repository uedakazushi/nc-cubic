# 非可換三次 n-fold：現行稿の検証範囲

2026年11月21日 / v26。対象は旧paper Bの全証明を読み込む `papers/nc-cubic-n-fold.tex` と現行の証明書・再現コード。証明の記載、読解点検、計算の実行、組版、外部への保存を別々の確認として扱う。

本版では、全 n≥3 の境界低積、飽和した二次表示、中心商、smooth potential 三次による指定一般点同型の延長、完備局所周期位相の証明を、執筆担当以外も独立に読解点検した。主な新結論は γ_sc,n|_{k₀((z))}=[D_R]、v_D(γ̄_n)=1 mod3、正準位相体の次数三である。固定 MF・window・一般点生成性・coherent 飽和性の入力の下での結果である。外部査読、Lean 等の形式証明、固定入力全体の独立再証明、新規性の網羅的確認は行っていない。

- **実際の窓と周期。** Burke–Stevenson i=1 の窓で Ψ₁Z=N₀(−1)[1] を全 n に同定した。例外対象の section truncation が自由加群になること、M(t) の高次消滅、同じ曲率 F_R の MF 周期、共通 shift の周期符号を点検した。任意の特異圏の包括的な底変更を仮定していない。
- **全 orbit Hom。** F₀=bXYZ となる選択済み pole 消去模型に対し、active MF と零曲率 Koszul 因子の unital bigraded dg 分離を確認した。特殊 fibre の Λ(k^{n+2})⊗k[t,t⁻¹] はベクトル空間の記述であり、積の同定ではない。一般 fibre との二次数次元の一致と DVR の普遍係数列から全 Hom の自由性・底変更を得る。階数は binom(n+2,3i+2q)。既存の n=3 の表はこの公式の例として保持した。
- **積の退化と一次 jet。** active m₂=0、m₃=0 を明示 cocycle と homotopy から確認した。m₃ の零次項は tensor 自体で零である。full m₂ の特殊階数は binom(n+2,2)−3。F_R≡J_R mod z² とし、同一 dg 模型上の contraction を単位と周期を保って持ち上げることで、full と active の一次 jet を接続した。三つの Smith 指数が全て一、三次先頭項が +z acb/(3p) となる符号を、一変数 x³ の閉じた tree −(hφ+φh)=I でも校正した。
- **飽和と内在的中心。** 二次関係の飽和後の特殊代数は S(0,−2,−p)[u₁,…,u_r]。量子多項式環の Zhang twist により Hilbert 級数を直接求め、各次数の generic rank と特殊次元の一致から全次数の自由性を確認した。中心一次部分は rank r の直和因子で底変更に両立し、中心正則列の商も自由である。二次関係の飽和から全高次の平坦性へ進む論理を独立点検した。
- **potential と表示同型。** active 商の cubic syzygy line は rank一で cyclic、交代成分は単元である。その symmetric potential は g_{p,2}=pΣX³/3+2XYZ という滑らかな三次を与える。点曲線 XYZ=0 との区別、Benoist の有限 projective Isom への実際の generic section の延長、Pic(R)=0 による GL₃ lift を点検した。full 中心変数方向の同型延長は主張しない。DVR の剰余標数は零と限定した。
- **局所位相の exact class。** source の指定中心公式から Ω₀=p(p³+8)G/3 を確認した。target Ω_p は飽和 active 格子で正確に z 倍の primitive class。特殊表示同型との差の自己同型が G を cube 倍することを独立に点検した。scalar の一次係数は −1/[p³(p³+8)]、D_R/z は −(p³+8)²/27、比は (3/[p(p³+8)])³。完備性と 3 の可逆性を使って exact class [D_R] を得る。未完備商体での exact class、大域 γ̄_n=[D]、他の分岐排除、位相体上の scalar index はこの結果に含めない。

証明の所在は [境界低積と周期位相](../papers/sections/residual_boundary_products.tex) の `prop:nfm-boundary-all-orbit-flat-rank-drop`、`prop:nfm-boundary-first-jet-products`、`prop:nfm-boundary-saturated-active-potential`、`prop:nfm-boundary-period-local-kummer`。既存の相対線型行列、三次元の幾何学的低 Hom 計算、I₃ の成分群・三分点計算は [境界模型](../papers/sections/residual_boundary.tex) に保持した。三分点被覆は局所三次位相体の三コピーであり、位相 torsor 自体と同一視しない。

以下の四点は、現行稿に保持している既存の内部独立点検である。本版で全証明を一括再検証したという意味ではない。

- **全次元の強化 class の一意性。** 固定した三次双加群自己交叉、内部次数による change-of-rings 列の短完全性、通常 Ext の積、中心周期による dg 局所化を確認した。Tate Ext の j=−p−q≥0 の切出しが全 A∞ 積・写像・homotopy に保たれること、Adams Koszul 双対の Hom の全単射、局所化の homotopy epimorphism、Adams covering と hull を通した実際の kernel class の回復を点検した。表示安定化子の一般自明性と合わせ、全 n≥3 の一般一ブロック族で H_p=1、S_p=Spec(k_n)、split 体での未標識強化型最小次数三を得る。全 full class の分類ではない。証明は [Tate–Koszul 復元](../papers/sections/residual_tate_reconstruction.tex) の `thm:nfm-origin-rotation-faithful`、`cor:nfm-generic-adjoint-class-unique`。
- **五次元の半 rotation の関手同定。** spinor 完全列の射を相対随伴の unit と同定し、相対 coevaluation と通常の right mutation の coevaluation を自然変換として比較した。Ku の消滅と Beilinson 分解により差が ⟨C₁⟩ へ入り、mutation で消えることを点検した。O≃ρ⁻¹[1]、O³≃[1]、ε≃id は対象の固定からの推測ではなく perfect 核の自然同型である。既存の相対核・Fano 曲面の連結性・次数2835の零 cycle による実核降下と、E_p の二 mutation の計算も保持する。指定 square 同型と MF 周期の同時正規化は別問題。証明は [五次元の節](../papers/sections/residual_fivefold.tex) の `lem:nfm-fivefold-spinor-relative-coevaluation`、`thm:nfm-fivefold-half-rotation-identification`。
- **非分裂 rotation の算術。** 偏極 gerbe 上の例外的 projector kernel の重み零、rotation kernel の重み一、convolution による Brauer 類の和 α+rβ、次数±三 Picard 類の index 上界を点検した。指数九族の符号規約は α=(a,v)₃−(b,u)₃、β=(a,b)₃ であり、α±β の symbol 表示と K(∛au) 上の α の非零剰余も確認した。一般一ブロック開の全 n≡1 mod3 に強化型最小九を実現し、同族の rotation 軌道内では三となる。全 full 型の最小三を確定するのは幾何的 Z 分類が適用される n=4 であり、高次元の他の軌道までは分類しない。証明は [非分裂 Picard 障害の節](../papers/sections/residual_unsplit_picard.tex) の `thm:nfm-unsplit-rotation-index-three`、`thm:nfm-unsplit-lowdim-full-degree`、`cor:nfm-unsplit-nine-versus-three`。
- **全次元の正準強化 class の周期位相。** κ(m) 上の混合有理比較が、形式拡大後に同じ全 Taylor 成分と hull を持つ完備 CF 核になることを確認した。最高次線束、Picard 等式、随伴射 cone の消滅を忠実な体拡大から反映させ、特定の比較核が強化型であることを示した。従って全 n≥3 の正準 class の γ_sc,n が C(c₄,−c₆) へ一意に降下する。Hesse 拡大の Kummer 核は ⟨[Δ]⟩ だが、一般 active 係数から得る半古典条件がその曖昧さを除く。D の八直線への分解、q=2 での非分岐性と一次係数も点検した。全 full class に共通な位相という主張は n=3,4 に限る。完備局所値は本版で [D_R] と決定した。大域的な次元間の一致・ΔD 以外の非分岐性は未証明。証明は [周期位相の節](../papers/sections/residual_period_descent.tex) の `prop:nfm-adjoint-period-all-dimensions`、`prop:nfm-period-hesse-faithful-test`、`lem:nfm-period-hesse-eight-boundary-lines`。

以下の随伴復元・有限 class・cube frame に関する点検は、既存の検証として保持する。現行稿の追加証明の点検と、過去に検証した全結果の再実行・再読を同一視しない。

随伴復元では、q=Li_C^*j_Y の右随伴が q^R=j_Y^!i_* であること、Serre 半直交性と線型 Koszul 解消による q^R O_C≅j_Y^!O_Y、truncation の随伴射が閉ファイバーで同型になることを点検した。既存の形式比較で得る一般ファイバーの最高次線束と、閉ファイバーの構造層を使い、新しいDVR補題で全体の最高次線束性・平坦性・底変更を証明した。閉ファイバーだけから平坦性を推論せず、局所環での非零因子 h と一般ファイバーの階数一を併用する。その後の cone 消滅には導来 Nakayama と proper 性を使う。

有限群 H_p の証明では、固定入力Bの三対象 window と一般点の coherent 飽和性により E_p⊕ρE_p⊕ρ²E_p が compact generator となることを実文で確認した。核の underlying Hom cohomology に一様な有限 bound を与え、Toën–Vaquié Proposition3.20 の有限表示性、自己同値 locus の開性、HH¹=0 の離散性を適用する。HH¹=0だけから全自己同値群が有限とする推論はしていない。有限 H_p-torsor S_p と Picard gerbe の積表示は、最高次線束を取る関手が scalar band に恒等を誘導することで確認した。

三・四次元では既知の G_ρ=〈T〉 と H_p∩〈T〉=1 からも H_p=1 を得る。全次元の一般一ブロック族については上記の Tate–Koszul 復元が自明性を与える。class の一意性は元の体上で実際の核を取れることを意味せず、scalar gerbe はなお非自明である。固定入力の外積表示と proper Hom の Euler rank の一定性から χ(E_p,ρ^rE_p)=χ_(N,r) を得て、既存 gcd d_n>0 により [E_p]≠0 となる。奇数次元の H_p⊂G_(ρ,0)、五次元の χ(E_p,E_p)=−27、一般形式の最小次数 min_i[K_i:K]ind(α_Ki)≤3|H_p| も保持する。

周期規格化では、元の残余復元が方程式直線を与えることを明確にした。source の中心元 Ω と full Poisson 対から三重ベクトル P が一意に定まり、φ_sc の線型持上げ f に対する F_φ⊗det(f)P=t_sc が方程式生成元を三乗倍まで定める。一般係数体の線型三捩れ monodromy が SL₂(F₃) であることから $J[3](K)$=0、I_sc(K) は一元集合となる。f の scalar 変更は三乗倍、Ω の変更は source/target の同時変更なので、全次元の正準強化 class の γ_sc,n はこれらに依存しない。形式比較式 F_φ=λ_h⁻³b_h⁻¹W_h と b_h≡1 mod h を確認したが、形式体での消滅を元 K へ戻してはいない。F→hF の吸収では中心元と実際の曲率の双方を h 倍する。元 K の γ_sc は本版の境界計算により非自明である。大域式はなお未決定である。

既存の周期位相の class 不変性、生成元の source u 倍・target v 倍による γ′=[v/u]γ、適合規格化の最小次数三、target の独立尺度を加えた一般族の最小次数九は保持する。元の自然な規格化 γ_sc の具体値と、自由な相対尺度の定理は区別する。点型の全 O-降下、標準三分点体の次数九と ASL₂(F₃) の二百十六次 monodromy、三・四次元の全 full class 降下、全 class に共通な scalar index 三、七次元の既知球面対象からの全自己同値群の非巡回性も保持した。既存の全証明と未公表固定入力を本版で一括再検証したという意味ではない。

本版で新たに作成・実行した検証器は `computations/verify_boundary_low_products.py` であり、十群の PASS と終了コード0を確認した。執筆担当と統合担当がそれぞれ実行した。Python 3.12.14、SymPy 1.14.0 を用い、有理関数体 Q(p) 上の厳密演算である。他の十六件の計算資産は基準 main `abdc32ee39cedc0b78f73b607521794157f6f219` と全内容を照合して不変と確認し、本版では再実行していない。以下に保持する既存の PASS・対象ハッシュは、その検証範囲の記録であり、今回の新たな実行を意味しない。

## 1. 固定した入力と文献

- `uedakazushi/nc-cubic`：`eabe601c1341777742964584dde5314c0bcf64a9`。論文A A-v61、論文B B-v59。
- `uedakazushi/nc-cubic-threefold-moduli`：`6c35d2c84671c2538e61836a6bf3a511392eacce`。比較対象の三様体稿 v22。

入力リポジトリは読取り専用。既存の一般次元正規形・中心量子化・一般点残余復元は新規成果に数えず、未公表入力の全証明を独立に再検証したとは主張しない。引用箇所は [研究ノート](research_notes.md) と [文献一覧](../papers/references.tex) に記す。

本版の境界計算では、Burke–Stevenson の公刊版 Theorem 6.4(1)、window i=1 と相対 Gorenstein 条件を再確認した。Benoist の公刊版著者 PDF の Theorems 1.6(ii),1.7 と Lemma 2.2(iii)、pp.140–141 を担当者が一次資料で確認し、剰余標数零の滑らかな potential 平面三次への適用を独立点検した。統合担当は固定入力Aの `papers/support/papers/sections/hesse_mixed_universal_center.tex` を固定 commit から読み、`thm:pg-universal-hesse-mixed`、`eq:pg-hm-coefficients`、`eq:pg-hm-center` の式を h′=p, t=q/p で変換し q=2 に特殊化した。中心性全体の独立再証明ではない。

既存の周期降下の点検では、統合担当が固定 commit の `papers/generic_recovery/curved_transport.tex` を実際に開き、`cft:eq:bound`、`cft:lem:primitive`、`cft:lem:arity`、`cft:lem:flow`、`cft:eq:object`、`cft:eq:insertions`、`cft:eq:two-block-matrix` の bound・原始元・arity・有限対象・挿入・二ブロック模型を新証明と照合した。三対象生成、proper Hom、局所化は `gcd:prop:bound`、`tw:lem:proper-hom`、`rog:lem:localization` と比較した。これは必要な一次模型への適用確認であり、入力B全体の全証明の再検証ではない。Fisher の不変式・一般軌道・Heisenberg 群の既知記述と、保存済みの全三捩れ monodromy を用いる character の消滅も内部点検した。

非分裂曲線には Cremona–Fisher–O'Neil–Simon–Stoll, J. reine angew. Math.615(2008),121–155、DOI10.1515/CRELLE.2008.012、arXiv:math/0606580v1 の §§1.1,1.3,1.6、Proposition2.2、Lemma2.4 と Ciperiani–Krashen Theorem3.7 を照合した。Saltman, *Genus 1 Curves in Severi--Brauer Surfaces*, arXiv:2105.09986v1 の §§3–4、Theorem5を既知の関連結果として確認し、曲線の period–index 現象そのものの新規性は主張しない。

Tate–Koszul 復元には Lu–Palmieri–Wu–Zhang, New York J.Math.14(2008),325–378 の Definition2.1・Theorem2.4・Corollary2.5(b) と、同著者 JPAA213(2009),2017–2037 の Theorem A・Corollary B を一次PDFで確認した。Braun–Chuang–Lazarev, Adv.Math.328(2018),555–622、arXiv:1505.01146v3 の Proposition3.17・Theorems3.18,5.3 を照合した。Keller の orbit 圏論文 §§9.3–9.4 と2009年訂正も確認し、訂正対象の旧§7の hull 表示は使わない。固定入力Bの `field_model.tex` の `gcd:prop:automatic-as`、`local_model.tex` の `lp:lem:noetherian`・`lp:prop:koszul`・`lp:prop:gorenstein`・`lp:prop:sing-period`、window・coherent 飽和の該当命題を本稿の仮定に照合した。詳しい識別子とリンクは研究ノートの「Tate–Koszul と Clifford 同定の一次資料」に置く。

有限 class の入力として Toën–Vaquié の Proposition3.20、Corollaries3.17,3.22,3.24 と Lemma3.25 直後の可逆核 locus の開性を原著で確認した。固定入力Bの window.tex の tw:thm:window・tw:eq:main、main_result.tex の一般点 coherent 飽和、generic_descent.tex の rog:eq:exterior と proper Hom を、今回の生成性と Euler 数の比較に照合した。Murfet の arXiv:0912.1629v3 Theorem6.2・式(6.6)、Proposition4.2・式(5.7)を確認し、公刊書誌 Compos.Math.149(2013),2071–2100、DOI10.1112/S0010437X13007082 を出版社と照合した。

五次元では Peize Liu arXiv:2509.21454v5（2026-08-03改訂）の Theorem2.8、§2.2の式(2-4)・Remark2.11、Lemmas2.12–2.14・3.4、Corollary3.10(ii)、Proposition3.11、Theorem5.5の証明、Corollary5.10を一次資料で確認した。Proposition6.10は Fano 曲面を一つの stable moduli 成分と同定し、全 moduli の既約性は Remark6.11 の予想、安定性軌道の一意性は Remark5.6 の未解決問題として区別した。Kuznetsov の公刊版 Adv.Math.218(2008),1340–1369 の Theorem4.2、Lemmas3.8・4.5・4.6・4.7・4.10、Remark4.8で実際の Clifford kernel、局所自由性、有限振幅、随伴を確認し、Collino Propositions1.8・1.10、Ciliberto–Zaidenberg arXiv:1903.11294v2 Example4.4の幾何学的連結性と次数2835を照合した。平面非依存性と元の体上への実核降下を内部点検した。さらに Proposition3.3 の相対表示と spinor 列の Lemma4.5 を用い、O≃ρ⁻¹[1] の自然な関手同定を独立点検した。Wu arXiv:2611.02388v1 Theorems1.1,1.3・Proposition7.2 と Aravena–Liu–Tevelev arXiv:2611.05350v1 Theorem1.2 の主張も確認したが、これら最近の安定性条件の全証明を独立再検証したとはしていない。有限 H_p の証明はこれらに依存しない。

一次資料で、Gesmundo–Landsberg の Proposition 6.1・式 (6.2)、Landsberg–Ottaviani の §1.2・§4.1、Boij の Remark 6（pp.163–164）、Boij–De Negri–De Stefani–Rossi の Introduction、Bricalli–Favale–Pirola の Proposition 2.1・Theorem 3.4 を確認した。Jacobi 写像と Koszul flattening・apolar Betti 数の同定も証明し、普遍階数上界と N=9,10 の二次階数の達成を既知の帰結として位置付けた。現行の次数三の決定や平方零拡大の非分裂性を、既存の Betti 数の表だけから導いたとは主張しない。全次元の一般 apolar 代数について β₄,₆=0 を示す文献は確保していない。

相対双対の入力は Berger–Taillefer の Theorems 3.1, 3.6、dg Morita 表示は Keller の Theorems 3.4, 3.8。係数降下・Kummer・曲線上の主因子は Stacks Project の Tags 023N, 03PK, 040Q, 02RU を確認し、現行の圏内の係数作用・全同値の降下には本文で証明を与えた。新規性の網羅的調査は未完了である。

既存の点検では、Behrend–Noohi の刊行版§2.3・§3.1.2を確認し、grading rigidification、twisted algebra、determinant character を既知手法として明示した。EGの刊行版§9・p.1414のRains中心公式は本文とPDF画像で確認し、Proposition 8.1.1・式(8.1.3)の形式的中心比較と今回の有限係数での処方を区別した。LBSVの刊行版Proposition 4.2.5・pp.193–194の二次関係復元も照合した。Stacks Tags058G,0781,03R6,063P,063U,062Y,056Qは新しい降下・相対幾何の使用箇所と照合した。固定入力の `prop:pg-ad-intrinsic-hessian` と `cor:pg-hesse-hessian-form` は、純中心補正の前後を区別して式を確認した。その未公表入力の非可換中心性の証明全体を今回再検証したとは主張しない。

二次 jet 比較に用いた Dito の arXiv:math/9905080v1、§2 式(3)と§3 Theorem2 を確認した。対象は一般 Poisson の二次積と Weyl gauge であり、Lie 代数に限定された後続公式と区別する。Shoikhet の arXiv:math/0007080v1、§1.3 の内向き wheel 消滅と§2.3.1 の逆向き wheel の区別を確認した。出版社で両文献の巻・年・頁・DOIも照合した。非線形 Poisson について中心写像の全高次消滅を主張せず、二次に寄与するグラフの数え上げを本文に与えた。

Artebani–Dolgachev の公刊版§2、Lemma2.1 と式(4)–(5)・p.240を本文とPDF画像で確認し、Hesse j式の規約を照合した。Lin–Zhang の Theorems4.1,5.1 と rotation の回復を比較し、幾何的非同型から圏の結論へ移す際の追加条件を保持した。固定入力Bの `curved_transport.tex`, `gradient_recovery.tex`, `explicit_example.tex` を固定commitから読み、完備移送、中心逆像、低 rotation 積、明示Hesse係数の該当箇所を確認した。この確認を入力Bの全証明の独立検証とは扱わない。

新しい補正について、Kontsevich の著者最終稿 *Deformation quantization of Poisson manifolds* の Theorem4.6、§§4.6.2,6.3、および *Deformation quantization of algebraic varieties* の §2.3 Proposition6 と後続の Conjecture1・Questions1 を一次資料で確認した。二次代数と二次 Poisson 構造の形式対応は既知結果であり、本稿の新規成果に数えない。Mori–Smith arXiv:1502.07403v2 の Theorems1.2,7.2 と Lemma7.1 を確認し、点曲線の Hessian 表示の既知性を Introduction と本文へ明記した。

Antieau–Krashen–Ward arXiv:1409.2580 の Theorem2.2 と証明を確認し、原点を持つ楕円曲線の導来同値から同型への帰結を使用した。De Laet–Le Bruyn arXiv:1405.1158v1 の §2 p.3 にある巡回和の中心元も直接確認した。この式は Rains の非巡回式とは引用箇所を分けた。追加した四文献の刊行年・巻・頁・DOIを出版社の情報と照合した。固定入力Bの `field_model.tex`, `generic_descent.tex`, `coherent_saturation.tex` の該当定理文と仮定を固定commitから読み、`gcd:prop:automatic-as`、`rog:lem:localization`, `rog:lem:descent`、`crs:prop:residual-smooth`, `crs:thm:coherent` の役割を区別した。線束生成残余部分から全 coherent 残余圏へ移る入力を、有限降下だけで代用しない。

既存の点検では、Kontsevich の harmonic-angle 配置空間と向き（著者最終稿§§2.2,6.2）を反射による偶奇性と照合した。Lindberg–Pym arXiv:2408.16685v1 §1.6と§6.7 Theorem6.9、Remark6.10を一次資料で確認し、qが原生成元の星積係数比であること、元のKontsevich formalityが適用範囲に含まれること、任意stable formalityへの拡張に残る条件を点検した。Ciliberto–Ottaviani arXiv:2006.07213v1 Theorem5.7とp.17の二回合成、Ottavianiの2024年刊行版§3のAronhold不変式の25項・古典的縮約も確認し、本稿の射や応用と既知の構成要素を区別した。

保存済みの graph 検算に用いた一次資料として、Banks–Panzer–Pym, *Multiple zeta values in deformation quantization*, Invent. Math.222(2020),79–159、DOI [10.1007/s00222-020-00970-x](https://doi.org/10.1007/s00222-020-00970-x) の Corollary1.3と続く段落（著者稿印刷p.6）、二変数 log-canonical 星積の展開（同p.3）、§6を確認した。harmonic weights の五次までの有理性は既知入力である。Buring の2022年学位論文 *The action of Kontsevich’s graph complex on Poisson structures and star products: an implementation* の§§3.4.1–3.4.2、印刷pp.74–76で重複度と係数規約を、§3.5、p.89で `star5.txt` の使用を確認した。[著者公開資料](https://www.rburing.nl/gcaops/)から組立済みの星積と独立した graph–weight 対を取得し、双方を照合した。一次資料の積分の証明を独立に再証明したわけではない。

Banks–Panzer–Pym の2022年訂正、Invent. Math.229(2022),449、DOI [10.1007/s00222-022-01122-z](https://doi.org/10.1007/s00222-022-01122-z) は[出版社PDF](https://link.springer.com/content/pdf/10.1007/s00222-022-01122-z.pdf)を確認した。原論文p.150、§6.2の係数は b=−1/2⁸ に訂正される。原論文の同節が対象を型(7,2)の graph と明記していることも照合したため、現行稿で使う五次以下のデータには影響しない。

Etingof–Ginzburg の刊行版§8.1、印刷pp.1407–1408、Proposition8.1.1・式(8.1.3)を現行稿の形式 potential と比較した。unimodular な形式 Poisson tensor の相対 Jacobian potential による認識は既知の先行結果であり、存在そのものを新規成果に数えない。限定的な追加文献検索では本稿の混合五次公式と四次 potential の既出箇所を確保できていないが、新規性の確認が完了したという意味ではない。全ての数値係数は指定 harmonic-angle・生成元固定・中心規格化に関するもので、任意 stable formality や任意 gauge から独立とは主張しない。

残余射の既存点検では、Wang arXiv:1906.04891v3 §3、Corollary3.2・Theorem3.3、Hwang arXiv:2501.08633v1 Theorems1.5,1.6・Propositions2.2,2.6・Corollary2.7を一次資料で確認した。Toën–Vaquié arXiv:math/0503269v5 の Lemmas2.8,2.10,3.25、Corollaries3.22,3.24、および Bergh–Schnürer の公刊PDF Proposition4.10、Remark6.1、Theorem6.2・Remark6.3を照合した。勾配復元、perfect 核の有限表示と同値性の開性、重み零降下そのものは既知の原理として記載した。

固定入力Bの `field_model.tex`, `generic_descent.tex`, `curved_transport.tex` の定理文と使用する構成を読み、(L),(CF)、三対象への制限後の Laurent 局所化、coherent 飽和性、一般係数体への係数変更の役割を分けた。相対 flow の新しい中心保存補題については、固定入力の `cft:lem:primitive`, `cft:lem:arity`, `cft:lem:flow` と MF 挿入公式を直接照合した。Lindberg–Pym の §1.6、Theorem6.9・Remark6.10を再確認し、対数境界値が原生成元の交換比から全次数で従うことを点検した。

点曲線・尺度の追加では、Fulton–Olsson の公刊版§1、式(1-1)–(1-5)、pp.87–88および Corollary2.4の証明p.91を読み、微分と判別式の変換、j≠0,1728 上のμ₂-gerbeを照合した。Poonen の Theorem1.5と直前の開性の記述を確認し、n≥3の三次に例外がないことを確認した。

scalar 障害について、Knudsen–Mumford の刊行情報を出版社で確認し、twisted perfect複体のdeterminantは Lieblich arXiv:math/0411337v2 §2.2.4、Definition2.2.4.1、period/index は§2.2.5の本文と照合した。Stacks Tags074S,074X の Lemma11.7.4、Lemmas11.8.3–11.8.4により、極大部分体の次数・分裂と index の整除を確認した。固定入力Bの `generic_descent.tex`, `rog:prop:euler` の二重次数とEuler式、`window.tex`, `tw:lem:proper-hom` の任意二有限rank MFのHom、`rog:lem:localization` の有限rankを保つCFを固定commitで確認した。window定理をMF全体の相対同値へ強めて引用してはいない。

Fisher, *Testing equivalence of ternary cubics* の著者稿 Theorem1.1、Definition2.1、Lemmas2.2,2.6、Lemma2.3の証明、Theorem2.5、§4、§9.5（著者稿12–13頁）を一次資料で確認し、出版社で LNCS4076(2006),333–345、DOI10.1007/11792086_24を照合した。古典的不変量 c₄,c₆ の Weierstrass 規約と微分の変換を、現行稿の Hodge 尺度と合わせた。Fisher が表示する Jacobian の6倍座標変更を、微分を追わずに本稿の規約へ流用していない。Stacks Tag07S5 Lemma66.14.2を自由な有限商に、Tags074S,074Xを index の整除に照合した。Bergh–Schnürer arXiv:1901.08945v2 Proposition5.7、§6式(6.1)、Remark6.1を Hom anchor の補助構成と比較した。これらの一般原理自体を新規とは数えない。

完備中心商については固定入力 `curved_transport.tex` の相対 bar 構成、arity 評価、flow と逆、二ブロック行列と t の重みを確認した。既存の厳密相対中心保存を入力とし、任意の商上の有限自由 MF へ公式を適用する。入力の一般点生成・window の次元条件を n=1へ広げる主張はしていない。

正則な体拡大と二次Kummer類の降下にはStacks Tags037P、0322、05DWを一次資料で確認した。active曲線のwindowにはGalinat arXiv:1302.1383v1 §1.1、Lemma1.2、§1.4、Lemma2.7の証明を読み、Φ=Φ₁、κ↔O[1]、ρ=T_O∘tensor O(1)の規約を一貫させた。異なるwindowの剰余体shiftを混用していない。Orlov arXiv:math/0503632v3 Theorem2.5(iii)、Burke–Stevenson arXiv:1507.00830v1 Theorem6.4(3)、Toën–Vaquié Lemmas2.8,2.10を確認し、固定入力Bの `gre:prop:elliptic-quotient` と `gre:lem:elliptic-mf` の正則DVR上のdg比較・底変更を読んだ。N≥5のfull windowの定理をそのまま三変数へ適用していない。Picard stackが相対Picard functor上のgerbeであることはStacks Tag0DME Lemma108.9.1を直接確認し、重み一線束からのband identityとgerbe同値は本文に証明を与えた。

既存の依存箇所について、Benoist arXiv:1111.1582v2 Theorems1.6–1.7とStacks Tag0CMXを原著で確認し、有限対角を持つPoisson符号商と係数下降への適用を点検した。Keeler arXiv:math/0108068v5（訂正を含む）のProposition7.2・Lemma7.6、Burke–Stevenson Definition5.1・Proposition4.18・Lemma6.2・Theorem6.4(3)、Stacks Tag0B91も該当箇所を確認した。固定Bの `local_model.tex` のnoetherian・Koszul resolution・Gorensteinの証明と `explicit_example.tex` の三変数MF比較を照合した。Keelerの訂正対象の旧Lemma3.3を使わず、amplenessはDVR上で直接示す。

Picard反例にはMilne *Class Field Theory*, version4.03のIII§4 Steps1–2とIV§3 Theorem3.14を確認した。Fisher arXiv:1707.08330v1 Theorems1.1–1.2・Corollary1.4と比較し、Jacobian上のAzumaya・Tate評価自体を新規と扱わない。

点障害の一次資料として、Ciperiani–Krashen *Relative Brauer groups of genus 1 curves* の Theorem 3.1、Theorem 3.5、Theorem 3.7 と証明（公刊版 pp.929–932）を読み、Picard 境界・Tate pairing・Weil cup 積の順序と符号を確認した。Matsuno *A Complete Classification of 3-dimensional Quadratic AS-regular Algebras of Type EC* の §2.4、Lemma 2.16、Theorem 3.3、§4、Corollary 4.3 を出版社 PDF で確認し、j 公式、2/3-torsion の座標、Sklyanin 関係式と cyclic potential を照合した。Mori–Smith arXiv:1502.07403 の Proposition 2.11、Corollary 2.9、Theorem 4.2(1) により、determinant 付きの生成元変更と滑らかな勾配族の正則性を確認した。

Hille–Van den Bergh *Fourier–Mukai transforms* の Proposition 4.2、Corollary 4.3、Theorem 5.3 と証明を原著 PDF で確認した。数値作用の核と graph 認識は既知結果であり、原点なしの体上の実際の核への降下、三次 rotation の centralizer と存在判定への適用を本文で証明する。新規性の網羅的確認を完了したとは扱わない。書誌・識別子・直接リンクは `research_notes.md` と `papers/references.tex` に統一する。

有限 torsor の定数降下には Stacks Lemma10.49.3、Tag0FWF の一次本文を確認した。代数閉体上の整代数の幾何学的整性を、有限体因子の定数体拡大とその非零局所化に適用する。Heisenberg 群の既知の部分は Fisher の §9.5 による。群 scheme の中央化群が GL_r の未知の form ではなく split GL_r 自身であることは、B↦[I_X⊕B] が幾何学的同型であるという本文の降下証明で確認した。有限 étale 群作用の延長には、既存の有限対角補題を群の二重・三重積へ適用し、一般点で指定した同変同型を保つ。

低次元の class 降下について、Liu *On Fourier–Mukai type autoequivalences of Kuznetsov components of cubic threefolds* の arXiv:2304.12669v2 Theorem4.13（同Theorem1.1）、§§2.2–2.3、Proposition3.5・Example3.7を確認した。出版社で Math.Nachr.297(2024),1866–1878、DOI10.1002/mana.202300237を照合した。Huybrechts *The K3 category of a cubic fourfold* は公刊PDFのTheorem1.2(i)、Proposition3.12、Corollary3.13、§§3.4–3.5・6.1を確認し、全FM群とsymplectic部分群、[1]と[2]の指数を区別した。書誌はCompos.Math.153(2017),586–620、DOI10.1112/S0010437X16008137である。

Canonaco–Stellari *Non-uniqueness of Fourier–Mukai kernels* の著者PDF Theorem1.2・Corollary4.4で、同じFM関手の核のcohomology層が同型になることを確認した。Math.Z.272(2012),577–588、DOI10.1007/s00209-011-0950-3を出版社で照合した。一般の核そのものの一意性を引用せず、本稿のprojectorに必要な追加証明を与える。Poonen のTheorems1.1,1.5と直前の開性の記述、Ciperiani–Krashen のTheorem3.1も今回の適用箇所に合わせて再確認した。三分点monodromyの古典入力はFisherのTheorem1.1(iv)、Lemmas2.2–2.3、§4と、Matsunoの§2.4・§4である。

指定周期の変換について、固定入力Bの `generic_recovery/local_model.tex` の `lp:prop:sing-period`・`lp:eq:period`、`generic_recovery/window.tex` の `tw:eq:period-extension`・`tw:eq:rotation-period-square` を実ソースで確認した。conormal の生成元変更と二拡大の境界、window で移送される周期を照合した。入力B全体の再検証とは扱わない。

高次元の既知入力として Iliev–Manivel の arXiv:1102.3618v2、Proposition3.1、Theorem3.4、Proposition5.2、Corollary5.3 を原著PDFで確認した。公刊書誌は Proc.London Math.Soc.108(2014), no.2,517–540、DOI10.1112/plms/pdt042 を出版社情報で照合した。Serre 式は既存 Lin–Zhang の Proposition3.7 の証明と、Lin–Zeng–Zhang arXiv:2610.00130v1 Proposition2.1・Remark2.2 を比較した。Lin–Rennemo–Zhang, Adv.Math.503(2026), PartC,111271 の Theorem1.3 と、Lin–Zhang arXiv:2611.05915v1 Theorem1.3 の主張の範囲を確認した。新しい2026年原著の全証明を独立再検証したわけではなく、対象復元や partner 有限性を自己同値群の忠実性・class 降下の入力として使わない。

Silverman, *The Arithmetic of Elliptic Curves*, 第2版 (2009), Chapter XI §9 の定義・Proposition 9.2（印刷pp.398–400）を一次 PDF で確認した。先頭係数の規格化が f∘[3] の三乗性を保証する点を本文で補い、Weil pairing の引数と cocycle の向きを照合した。Appendix C の正則模型・成分群の記述も確認した。URL と識別子は研究ノートと書誌に保持する。

境界の追加について、Eisenbud *Homological algebra on a complete intersection, with an application to group representations*, Trans. AMS260(1980),35–64 の Theorem7.2、印刷pp.56–57 を原著PDFで確認し、有限自由分解に dh+hd=F,h²=0 を与える Shamash 構成へ適用した。Burke–Stevenson arXiv:1507.00830v1 Theorem6.4(1)、印刷pp.18–19 と Definition5.1 を確認し、A₀ が regular DVR、Gorenstein parameter が n−1 の場合を用いた。既存の楕円 active 比較が用いる同定理(3)とは分ける。Stacks Tags0BQP,0A1G の local-to-global Ext と proper flat な基底上の perfect 押下げ・底変更も直接本文と照合した。これら一般手法そのものの新規性は主張しない。

## 2. 証明の記載と読解点検

三分点被覆の使用箇所について、Stacks Tags0BFG・0BFH の三倍写像の有限局所自由性・étale 性、Tag0DME の Picard gerbe、および Bergh--Schnürer Proposition4.10 の重み零降下を一次資料で確認した。Tag0BQI Lemma58.10.7の完全忠実性は、有限対角によって得た正規近傍上で、二つの有限étale被覆のgeneric同型を延長するために用いる。被覆の存在を一般点だけから推論する方法ではない。

Stafford--Van den Bergh, *Noncommutative curves and noncommutative surfaces*, arXiv:math/9910082v2 §3、式(3.1)を原著 PDF の画像でも確認し、右加群の規約 s=σ_*(−⊗L) の下付き * を照合した。Orlov Theorem2.5(iii)、Burke--Stevenson Definition5.1・Lemma6.2・Theorem6.4(3)も原著の該当箇所を確認し、指定active商に必要な環論的仮定と閉／一般底変更までの適用を本文で検証した。固定入力Aの `prop:pg-PBW` と `thm:pg-universal-hesse-mixed`、入力Bの `rog:thm:geometric-generic` を三捩れ対称族に代入して点検し、後者が (L),(CF) を満たす一変数族を扱い、全係数の一般性を追加要求していないことを確認した。

現行の中心復元、次数付きモジュライ、相対双対、点関手、Jacobi 方程式、残余圏の形式認識の証明を保持した。固定模型の降下、Picard 障害と明示例、Koszul/apolar 同定、八次元の全 Hilbert 関数、横断切片・retract には、執筆担当以外の担当による読解点検と統合時の点検を行った。これは外部査読や形式検証ではない。

| 対象 | 点検した論点 | 適用条件・残る限界 |
|---|---|---|
| 全次元の強化 class の一意性 | Tate の非負内部切断、A∞ 写像と homotopy、Adams Koszul 双対の全単射、中央局所化の mapping space、Adams covering と hull、一般表示安定化子 | 固定入力と一般一ブロック開で H_p=1、S_p=Spec(k_n)。全 full class・全 intrinsic 成分の分類ではない |
| 全次元の正準 class の周期 | 同じ mixed-rational CF の完備核 class、faithful な随伴復元条件、重み零 Hom と三次形式、二段定数降下 | 強化 class の標識付き最小3/9。全 full class 共通性と全型の最小は n=3,4 に限る |
| 五次元半 rotation の相対核と class | 普遍平面の blowup・flat quadric、実在する Clifford kernel と正しい随伴、相対 C_i の例外性、HH¹=0と連結 F₂ の class 写像 | 滑らかな幾何学的連結 F₂ を持つ一般五様体。absolute perfect からの無条件な相対化や局所核の貼合せを仮定しない |
| 五次元半 rotation の実現と関手同定 | 相対 spinor 列の随伴 unit、相対・絶対 coevaluation、二つの Ku 消滅と Beilinson 分解、C₁-mutation による差の消滅 | O≃ρ⁻¹[1]、ε≃id を実際の perfect 核で同定。指定 square と周期の同時規格化は別 |
| 非分裂曲線と index 九 | 独立 Kummer 二座標、二段付値、最小項の一意性、逆巡回 theta lift と divisor cocycle、αとβの区別 | αはperiod3/index9、βはindex3、両者は線型独立。曲線例だけで非可換族を実現したとはしない |
| 非分裂一ブロック実現と最小階数 | 共通中心重み、mixed theta twist、加法torsor、純超越的支配性、反標準束の次数九、非分裂随伴条件 | n≡1 mod3の任意の非空開にindex9例、普遍最小重み一階数9。共通慣性自明開の全n≡1 mod3の強化点型で未標識最小9。全体・任意型への一律の九ではない |
| 周期位相の混合定数降下 | MF行列の混合重み上界、inverse CF、integral Homの局所化、三対象生成、二回の有限étale定数降下 | 全nの正準強化classの位相をactive十係数体へ戻す。k(m)((h))だけの消滅や新しいLaurent MC元への無限flow評価を使わない |
| 周期 torsor の不変量降下 | (f,η)へのcoherent G_m作用、scalar bandの相殺、SL₃同変性、H_g^ab=J_g[3]とfull monodromy、正則性 | 各類はC(s,t)へ一意降下。局所[D_R]とv_D=1を決定。大域[D]と次元間の一致は他のbranch排除という追加仮定付き |
| 反対代数と残余不変性 | 語順反転・中心直線・trace–Hessian、反転不変な代数的中心族、偶 Weyl symbol に対する W の偶性、支配形式族による射の等式、自由有限商 | 固定残余入力の下。Abel圏の反対や導来双対をrotation保存の共変同値として扱わない |
| 正確な一般次数18 | c₄,c₆、一般ファイバーの整性、traceの混合多項式性、全次数混合三角形、TH scalarの規格化、PGLの共通T₉と指数二、小さい体上の候補射と忠実拡大 | 固定残余入力・良い一ブロック・全n≥3。形式逆だけから次数を推測せず、Nat frameの代数化を未使用 |
| activeな符号類 | 正則体拡大による定数降下、Hesse二次類単射、C₃同変な有限対角延長 | 固定入力の下でχ_act=0、χ_op=χ_sgn。半古典full射は一般次数9 |
| Hesse 二次類と対称族 | Q8⋊C3 の位数24・固定体・二次指標の自明性、全次元の smooth scalar 例、対称族上の有理三捩れ点と二次 twist の排除 | 独立対称族のJacobian被覆は分裂。一般χ_actとの比較は有限対角による別の延長を用いる |
| 符号消滅とfull射 | smooth有限係数模型・有限Isomの指定有理切断・二重三重積・C₃同変性・有理三捩れ・半古典分枝 | finite étale階数9とCartesian図式。特殊fiberの低Nat再構成や核の延長は別 |
| 点型の全 O-降下 | 原点対象の重み相殺、固定section-windowとactive window1、graded Koszulの切断比較、最高次線束の実際の同型 | 良い一ブロックの共通稠密開、任意底変更、Brauer–Severi ambient可。型の降下とclass選択は別 |
| 非分裂最高次線束型のperiod | Pic_C^3の有理点から3[C]=0、CK Tate pairingの双線型性、Picard gerbeのband identity | 選択済み最高次線束型類でper|3、index|3/9。index9は下記の別の非分裂族で実現し、全非分裂体の一律の値は主張しない |
| 三分点被覆の連結性 | 普遍Hesse曲線の真の一般点、P,Qの有理逆、全係数への純超越支配族 | 全n≥3のk_nで最小三分点次数9。scalar分裂や全比較核の最小次数と区別 |
| 完全三捩れ・affine monodromy | Hesse24群のorbit8/stabilizerC3/core1、正則不変量体拡大、H_g=H_Jg、全translation群 | ASL₂(F₃)全体、Galois閉包216、九次体に中間体なし。有限Hessian拡大で像不変を仮定しない |
| projector核の一意性 | directed解像長、projected点のsimple/負Ext、相対Hom線束、CS cohomology一意性、detとPic(Y)のtorsion-free性 | 全n≥3のsmooth cubic、代数閉体。一般のFM核一意性は主張しない |
| 低次元の全full class | Liu/Huybrechts分類、可算体からCへの埋込み、dg核の単射性、K定義T、連続Γ→Zの零性 | n=3,4の幾何generic。very generalを全Zariski開と同一視せず、n≥5未解決 |
| 低次元の最小比較次数 | T^mによる全gerbeのband同値、非空点型、既存exact3、三次分裂体 | 全full型で最小3、三に素な拡大上不存在。指定周期標識は追加μ₃。正準frameの位相体は三次、最小3 ind(α_M)の二択は残る。適合frameの最小3・独立target尺度族の最小9を別途証明 |
| 周期位相の class 不変性と frame 則 | 指定 MF 周期の中心的整合性、実 K-核 T の全冪、conormal の生成元と二拡大 | n=3,4 の全 full class で γ 共通、γ′=[v/u]γ。同時尺度では不変、正準frameは局所[D_R]により非自明 |
| 周期標識の最小次数 | 相対尺度による γ 消去、M=K(s) の純超越性、division algebra の多項式環、最大部分体 | 適合規格化で最小3、独立 target 尺度の K(t) 上では全実現次数を9が割り最小9 |
| fractional Serre 差 | canonical Serre 比較、θ による周期の移送、三重合成図式 | n=3 で γ=[d(P)⁻¹]。S³≅[5] の存在だけから d(P)=1 は従わない |
| 高次元 class の中央部分除去 | 実 K-核 T の中心性、profinite 安定化群から Z への連続準同型 | class と T-軌道の安定化群が一致。点型軌道を選べば十分だが存在は未証明 |
| 奇数次元の数値的自明部分 | Lefschetz/RR、実 projector、R≠I、Eisenstein 単元、T_* の位数六 | 全奇数 n≥3 の split 偏極で G_ρ/〈T〉≅G_(ρ,0)/〈[2]〉。群の消滅や H¹ 中立性は未証明 |
| 七次元の全群の障害 | 既知 IM 球面束、projected point の Euler pairing ±9、twist の無限 unipotent 作用 | 一般七様体の full 群は Z² を含み G_ρ は無限指数。G_ρ 自体の非巡回性は未主張 |
| 一般平面同型 torsor の分裂 | κ(m) 上の指定比較、有限 étale torsor の定数降下、一般 H_g の全 ambient 中央化群、特殊点、正規延長、F'=hF | 固定入力・一般 split 係数体。full 核の特殊点延長を仮定せず、有限 Hesse 拡大から類を戻さない |
| 半古典平面同型の全 O-降下 | 全 parabolic・純中心項を含む TH 共変性・形式分枝の一致・normal atlas・次数 scalar・固定模型の全同値比較 | 良い一ブロックの共通滑らかな稠密開、Brauer–Severi 平面可、任意底変更。full class・点型の内在性は別の結果で扱う。任意 formality 独立性は未証明 |
| 残余障害の exact index 三 | 実際の平面同型による Picard gerbe 同定、点側の非零類、三次横断切片の体成分 | δ_C は full class 選択前から exact3。この系のscalar主張は選択済み類。n=3,4の全class選択は別の定理で証明 |
| cup 補正の限界例 | Kummer 同士の pairing、C_d の係数変換、cyclic symbol、一般 Jacobian 点と形式弧の単射 | actual residual と同定しない。形式比較と半古典零点だけからの不正な降下を排除する |
| Picard 三分点被覆 | 三乗と determinant の重み相殺、零切断での規格化、任意底変更、gerbe 同値の規格化された逆像、δ_C の加法性 | 実際の次数三線束、固定表示・window・選択済み full class。階数9の被覆で scalar 障害を消すが class selection は解かない |
| 点平行移動と Picard 類 | 右 THCR の pushforward、Adρ の二つの shear、window1 の切断、恒等からの graph-line 変形、finite model での Picard 等式 | 指定中心商の相対THCR/window1を証明し、存在する追加型でm_P=θ_sc(p_pt)。全 refined 核や coherent active 核 assignment へ拡張しない |
| 指定中心商の相対window | 点行列・σ³≠1・中心像の零・Nakayama・ample pair・Gorenstein・実際の底変更図式 | 支配的k[[h]]族と閉／一般底変更。任意非正則底の一般論ではない |
| 一般点の Picard 障害 | Hesse 接線 norm、付値、Jacobian 関数体、syzygy potential の忠実降下、Hesse chart の有理逆、純超越的な全係数支配族 | 標準 split 一ブロック係数体で period=index=3。有限 Hesse 拡大は支配性の検査だけに使用。I_sc 分裂と合わせ、点型の残余障害も exact index 三 |
| 全 active FM 判定 | 数値 centralizer 六元、hereditary 圏と点層、graph の fpqc 降下、偏極差 d と Picard 類 m の共役式 | 実次数三偏極・標数零。全数値型を含め polarized φ の存在と δ_E(p)=0 が必要十分 |
| 相対 active gerbe と周期 | Tor amplitude、長さ一平坦層、graph と線束、相対 Poincaré 計算、Hom 線束の重み零と三乗条件 | noetherian Q-scheme、非被約底も可。I_θ 上の Picard gerbe と、η の μ₃-torsor を区別。full class lifting は別 |
| 点行列と形式三分 | scheme-theoretic det=0 と二次小行列の単位生成、核と余核の determinant、Hensel 有限 étale 切断 | 余核は3pを表す。k[[h]]上 p≡0 の三分可能性を元の一般係数体へ外挿しない |
| flex cup と平面同型移送 | CK Tate–Weil 公式、c_γ=γx₀−x₀、d_γ=γq−q、I_θ の右作用、ξ_C=θ(ξ_E+ι_θ) | 三つの階数九 torsor を区別。一般補正は H¹(J)[3] を通り、actual residual の一般 split 係数体では I_sc 分裂により零 |
| 点型比較被覆の次数下界 | I_sc の元体上の分裂、actual top line、period 三、restriction–corestriction | 点型 actual full P だけで有限拡大の次数は三の倍数。元体での full class 選択や active assignment は不要。全nの系は点型。n=3,4は別の自己同値分類で全full核へ拡張 |
| 核のPicard障害と曲線上の分裂 | top lineの相対Picard類m_P、band identityによるgerbe同値、重みの相殺、一般直線の次数三étale切片 | 選択済みfull classのscalar段階。m_P=0やC上の実際の線束による表示を一般に証明したわけではない |
| 線型中心列とMF制限 | Torの内部次数purity、minimal resolutionとExt消滅、非正準Postnikov分裂、Ω₀正則によるTor-independent square | 次数一の正則中心列。次数二の反例を保持。圏全体のcategorical tensorと同一視しない |
| 最高次cohomology型 | Galinat window1、体上の負rotation、唯一のH^{-1}、perfect族の線束性、generic flatnessと閉点特殊化 | 非空な強い型を構成。最初の形式核そのものの有限拡大への定義を主張しない |
| 階数三束とscalar index | universal full kernelからcanonical weight1 line、O_C(1)とのtensor、H¹=0・h⁰=3、Endの重み零降下 | 型を満たす選択済みfull classのgerbe。splitでindexは3を割り、表示分裂後の型を仮定すると3/9。強化点型のclass選択は全nのTate–Koszul定理、n=3,4の全class選択は別の分類定理による |
| 完備中心商のMF | 全Taylor成分の中心多重線型性、商の分離完備性、arityによる収束、逆・単位・rank・shift・指定周期、任意のquotient MFへの挿入 | 係数商の明示公式。categorical derived tensorや有限代数的核のcoherent中心線型性の降下は別 |
| scalar indexとEuler格子 | circulant Euler行列と整数格子、thick閉包との区別、d′|dとd|[L:K]d′、標準二重被覆・十八重被覆の各体成分 | Euler 格子自体は既選択類の上界の議論。点型 full scalar 類の exact index 三は、別の平面同型分裂と Picard 障害から得る |
| active 部分の全次数比較 | active 出辺と U=0 制限、同座標 Hesse 分枝の識別、SL₃×A² の支配性、普遍係数恒等式、Koszul と Euler による W_act=b_hJ_g | 固定 split 比較を入力。単なる j の一致を同座標比例へ読み替えず、MF の中心基底変更や n=1 の field-model は未使用 |
| 点曲線と同型被覆 | 支配族からの j の降下、短い Weierstrass 式、[3]q=a、偏極類と Brauer–Severi 平面の étale 降下 | Iの階数18、Dの階数2、I→Dの階数9。Dだけに genus-one 曲線・平面同型があるとは主張しない |
| Hodge と自然な尺度 | 相対随伴のdeterminant因子、重み零、modular formsのweight、τ_pt、η_res、Jacobian-Isomとの同一視 | j≠0,1728 の共通稠密開。modular正規化被覆と点微分の被覆を区別 |
| 符号商射の支配性 | 一般中心liftのc(h)相殺、η=h²・unit、一般特殊点の零切断、既約閉包、同次元性、自己同型なしの開の有限化 | 形式frameの代数化を未使用。一般次数18の証明は混合三角性と安定化群比較を併用。比較核の二重被覆への降下は未主張 |
| 点shiftとharmonic尺度 | 固定点なしから平行移動、Jacobianのtorsor作用、deck反転、t=(h/b_h)W_h⊗P₀、tensor比h/c_h、c_hの五次係数 | Ku rotationの制限との同定は未証明。比の代数性や固定harmonic尺度との一致は未主張 |
| kernelのEuler/index | 重み1 perfect Homとdeterminant、p_(N+2)=−3tp_N、数値型の開閉性・非空性、有限表示降下、indexによるrank整除 | 整合する核の同型類を選んだ後のscalar段階。体上indexと一般底上bandを区別。未証明のΦκ_nc=κ_Yを不使用 |
| unsplit体上のindex | rank3重み1の束でβを次数≤3でsplitし、その上のαを次数がd_nを割る体でsplit | α=βを仮定しない。同型類選択前の比較被覆全体の次数は抑えていない |
| 相対積分直線 | D_Q の scheme 的 rank 条件、単元 minor による核・余核の分裂、非被約を含む底変更 | 体上の勾配一意性は Wang・Hwang の既知結果。scalar symmetrizer と射影自己同型群の自明性を区別 |
| 全次元の非空性 | 巡回三次の滑らかさ、Hessian 係数行列の台の交差、N=5 の最小例、active 切断の特異条件 c³=−27/64 | 全 N≥5 の手計算による証明。有限個の次元の計算からの外挿ではない |
| 支配的中心 h-family | δ_h=h⁻¹[x_i,−] の有限自由行列、特殊 Casimir 核、一般中心との同次元性、Ω_h の代数的持上げ、純中心 G による全 torsor fibre の被覆 | 固定 PBW・中心入力。Ω_h+G の特殊三次は F+G、tensor は Π_F のまま |
| 相対残余模型と低 Nat | 有限個の線束・mutation による proper 模型、perfect な源 E→Δ を先に広げる非循環な smoothness 証明、全 cohomology の局所自由化 | rotation の可逆性・底上 perfect 性を明示。compact 相対圏と各 fibre の coherent 飽和性を区別 |
| 中心作用の一般階数 | 可換側の perfect Nat、一般・特殊 H⁰ の等次元性、DVR 完全列による torsion の排除、Laurent 体上への生成性の降下 | 特殊化の単射性だけで結論しない。完備底で三対象が生成するという強化は未使用 |
| 相対 graph flow | Xi=a_hP_0、active な全出辺、中心係数に関する多重線型性、単位正規化、flow・逆・MF 挿入での uId の厳密保存 | 選んだ正規化 flow についての証明。任意の CF 同値への一般化や形式 frame の代数性は未主張 |
| 射影 Poisson 射と尺度 | 全 O-持上げの線束重み、projective cocycle、L⊗det K の重み零、full scale の引戻し torsor、像の支配性 | 固定入力Bの下で既存一ブロック稠密開。Brauer–Severi を許し、全 intrinsic 成分を主張しない。一般相対次元1、連結 fibre・表現可能性は未決定 |
| 有限比較被覆と kernel | 同じ X の generic 核、正規化・分岐除去・perfect cone の台除去、DM chart の有限化、P[2m] による非一意性 | 有限 étale 被覆上で比較。元の stack への kernel 降下は自己同値 torsor と選んだ同型類の scalar gerbe の二段階 |
| trait の良い還元 | 完成格子の有限 jet 降下、saturated Q、積分直線の忠実平坦降下 | CF 依存の滑らかな模型の存在。正準性・相対 Hochschild 格子・kernel の h=0 延長は未証明 |
| very general な超越性 | 再帰の普遍多項式性、厳密 log 境界値、留数の矛盾、有界次数の関係 locus を全 maximal minor で定義 | 任意非空良い開の very general と普遍関数体の主張。単一 Zariski 開の全点や arbitrary formal frame を許す intrinsic な尺度の不存在は未主張 |
| 中心復元・次数付きモジュライ | fpqc 持上げ、μ_d、中心正則対、全次数の切断飽和性、全次数付き同型、有限安定化子、スカラー重みの相殺 | 中心平坦性・普遍低次数中心・良い PBW 表示の仮定を要する |
| 普遍相対双対 | 有限 Koszul 対角、真正な双加群自己双対、中心差分、torsion 比較、compact generator、dg orbit、相対 properness、Serre pairing・trace | 被約有限型の初期基底、有限射影・分裂 PBW・各ファイバーの Koszul/CY・中心三次の分裂正則性。その後の任意底変更には非平坦・非被約を含む。全商上の orientation の自明化は未主張 |
| 固定模型間の全同値 | 係数対象の Gabriel 局所化、faithfully flat な tails の降下、全関手と自然変換の降下、自然自己準同型のスカラー性、Isom_gr/G_m と全 O-保存同値の一致 | 比較定理に列挙した中心・次数別有限射影性・相対 Serre の仮定。一般の Abel 圏族が局所的にこの模型へ入ることや全モジュライの代数性は未証明 |
| 線束障害と三捩れ例 | μ_d と G_m の持上げ torsor の区別、L^d、行列式からの gcd(d,3)、affine 楕円曲線の非主三捩れイデアル、次数別線束 twist と PBW 入力の保持 | 三捩れへの制限は両方の次数一加群が自由な場合。明示例は指定した同値に大域の次数付き代表がないことを示し、二つの代数にどのような次数付き同型もないとは主張しない |
| 局所 O-marked 圏族の効果化 | 一般Grothendieck圏の忠実平坦係数延長、重み付き加群のgenerator・torsion商、任意係数変更、全同値のcocycleから対象を構成 | good模型の全Hom比較が入力。全intrinsic成分の局所表示や変形の閉性は未証明 |
| 表示 gerbe の H² 障害 | determinantの重み、e=1での中心拡大の分裂、cyclic division algebraのvaluation、全非空開のtwistと有理点 | n≡1 mod3で全非空開上の位数3を証明。幾何学的一般点の体に非零Brauer類が残るという主張ではない |
| 相対点関手 | 任意底変更でのKoszul完全性、八次有限局所自由性、相対Cartier、低次数イデアル、点商とshiftの降下、determinant付き相対随伴 | good点スキーム条件。ambient上のO(1)と点空間への引戻しを区別 |
| 中心三次の復元 | Rains式の境界Jacobi評価、中心評価の普遍単射、I(D)₃/I(C)₃と中心直線の逆像 | 非空開上。n=3で全切断への全射を使わない |
| Trace–Hessian 射 | 任意基底の三次Casimir、正規化trace、Hessian縮約の共変性、torsor同型と滑らかな非空開への降下 | 良い局所一ブロック型。Kuとの一致は別であり、別の比較節で具体的な不一致を証明 |
| 強い affine lift と逆構成 | Euler列のコホモロジー、gradient Koszul、強いliftの一意性、divergenceによるJacobi同値、supportと全同型の回復 | 任意のC代数・滑らかな相対三次・n≥3。標的は偏極類とBrauer–Severi ambientを許す |
| Poisson 開の同型と支配成分 | Msm≅Pgood⊂Pdec、周囲B単独の有限性の除去、pairのDM性、Brauer位数、一般三次上の開埋込み | PBW・中心・相対Serre・全同値の入力を保持。唯一の支配成分には既存被約分類を使用。全 intrinsic 圏成分の分類ではない |
| 幾何補正 | F_tの滑らかさ因子、全nに一様なJacobi双対証明書、trace補正u³の非消滅、係数空間の非空開 | 入力の中心性を使用。入力定数族との差と残余復元との差を区別 |
| split Hesse 比較 | exact λ_THとλ_res、j差、symmetrizerの可換代数性と唯一rank3 primitive、固定Πの全smooth cubic Casimirへの障害 | 残余の同定は固定入力Bを使用。rotation保存dg Morita同値なし。n≢1 mod3でのみrotationなしの結論 |
| 一般混合係数の二次 jet | Dito二次式、Θ=−2adj、ρ₂F=Hess/8、inner二輪消滅、h⁴境界のJacobi消滅、Jacobi束切断Δ₂の非消滅開 | 指定formality模型・MF/window入力の下で複素点のmarked形式比較を妨げる。完備MF同値自体の任意基底版・一般混合係数のunmarked一般点非同値は未主張 |
| 代数的 Poisson 補正 | Hessian 縮約と trace の座標共変性、方程式直線の尺度、任意基底変更、flag 付き零切断での微分、étale・支配性、全 O-降下 | 出力と active 制限が滑らかな非空開。次数9により非双有理。固定 tensor は五次で形式逆と異なる稠密開あり |
| 補正射の一般次数 | ψの基点なしP²拡張・次数9、SL₃×A²被覆の微分と次数乗法性、混合の三角復元、traceのf₀独立性、全分枝を残す開、同一群の商への降下 | 全n≥3、商stack上の表現可能有限étale階数9。粗モジュライ次数は別。未公表MF入力に依存しない |
| 点曲線との一致 | 普遍 determinant 恒等式、adjugate による incidence の scheme 的因子化、相対 rank2 の核直線、左右射影 | Mori–Smith の既知公式。shift 付き対応全体と定常成分の同一視は含めない。零パラメータの実際の点スキームは別 |
| 全次数の形式 tensor | 最初の差による正規化一意性、有限 graph 再帰、被約普遍係数上の恒等式と任意底変更、単位正規化、線型中心保存、Koszul と次数による scalar factorization、中心逆像 | 固定 formality・固定 h・PBW/存在入力。滑らかな Poisson 対には全 F も滑らかと仮定。c₂=0を別途証明。有限 Artin 中心とは区別 |
| c₂と偶奇性 | 普遍係数の多項式性と原始係数ベクトルによる分母除去、二次SL₃不変式の消滅、混合制限、配置空間と商群の反射符号、中心写像と反対積 | h独立の二次関係、指定harmonic-angle模型、偶数Weyl中心元。W≡H♯ mod h⁴、π≡Π♯ mod h⁵ |
| 五次tensor の active 制限 | smooth split拡張からのclosedness、Euler積分、最高ウェイト(7,4,4)の重複度、原生成元q比とPBW同型、Sの規格化、混合制限と非空稠密開 | 純active公式とmixed制限は全混合公式の入力。tensor の相違だけから三次やKuの非同値を推論しない |
| 全混合五次項の還元 | Weyl再帰の局所jet性、型qT⁴/M²T³、次元1+2、ε縮約I,J、det−35/3、独立Taylor jetの斉次実現、純active普遍恒等式、中心平行移動 | 二つの jet への評価が普遍係数を決める根拠。特異な試験式から一般対象の結論を直接推測する方法ではない |
| 全混合五次項の係数 | 公刊 weights の73項への縮約、raw weights/Aut と star5/2^k の照合、二つの独立混合 jet、π₃の挿入とWeyl補正、β=1/60・γ=1/240 | 指定 harmonic-angle・生成元固定の普遍多項式。configuration-space 積分自体の再計算や任意 formality への係数不変性は含まない |
| 中心逆像の四次項 | 単位保存と active affine 共変性による局所jet性、型qMT³/M³T²の次元1+1、Ψの入力公式、I・J・SdFの独立性、W₄=Ψ+I/24−J/80とa₄=S/240 | Hessian 正規化した指定中心元と固定 formality。中心元の任意単元倍に対して同じa₄を主張しない。非可換中心性は固定入力 |
| 四次 Jacobi 類の非消滅 | Jがactive勾配イデアルに属すること、τ(J)=0、Eulerの[F]=0、Fermat active式、全nの滑らかなF_*とℓ(Δ₄)=−1/9、Jacobi束の非消滅開 | 全混合の滑らかな係数空間の非空開。全 intrinsic O-moduli の各成分を覆う結果ではなく、純中心像による商束の一定階数性も仮定しない |
| 四次の標識付き比較障害 | H⁰(T)=0、HH¹=0と実際の幾何的KS写像の単射性、小拡大上の二つの持上げの差、Artin切断と両立するMF/window移送 | 全n≥3、n=4を含む。圏への適用は固定MF/window入力付き、同じhと特殊ファイバーの標識を保持する。HH³消滅や幾何変形の全射性を使わず、unmarked一般ファイバーの非同値は未主張 |
| 全 O-降下する四次補正 | S_P,I_P,J_Pの縮約、traceの底変更、方程式の尺度と純中心加法、単元倍のP、滑らかな非空開、H^[4]≡W mod h⁶とtensorのmod h⁷一致 | 有限の代数的射。全次数の収束・代数化・残余同値の降下は未証明。旧Hessian補正の次数9や厳密な点曲線一致を新射へ転用しない |
| I,Jの古典的微分表示 | 独立なT,M,qでのadjugate–Hessian縮約とAronhold不変式の方向微分の恒等式 | 係数環上の厳密多項式検算。既知不変式Sや古典的演算自体の新規性を主張しない |
| split 族の正の残余比較 | 独立 λ,s の中心係数と TH 出力、点曲線 ν、Heisenberg 同変性、j 分岐点を含む形式枝、active scale、固定標的への有限降下と coherent 飽和性 | 全 n≥3・各固定 λ、1+λ³≠0。MF・window・生成性・有限降下・coherent 飽和性は固定入力。一般混合係数や全 O-同値への残余同値の降下は含まない |
| Jacobi の二次式と既知結果 | 全係数環の式、Plücker 空間、普遍核、ρK/2 の係数と符号、Koszul strand の双対、N=5 の終端、total Betti 数から必要な graded Betti 数への帰着 | N≥11 の一般階数の最大性は未決定。一般 Koszul 性から β₄,₆=0 を推論しない |
| 八次元の頂点 | I₃=J₃ から全次数の一致、J/I=C(−2)^330、socle・飽和・根基、非分裂性、任意底変更の相対版、一次分解 | この結果は一般点被約分類に依存しない。長さ330は J/I の長さであり、明示した m-primary 成分の商 R/Q の長さ5401とは異なる |
| 非零点の局所構造 | 法接空間 Λ³K、横断方程式から混合項の消去、全 W 方向の polar 条件、Thom–Sebastiani 特徴付けと scheme retract、n≥11 の特殊非零点への330次元部分空間の注入 | 横断切片を Grassmann 方向との局所積とは主張しない。特殊例の周囲の冪零根基全体が二乗零とは主張しない。n=11 は構成が与える下限であり最小性は未証明 |
| 一般次元の頂点と高次数 | 悪い incidence の次元評価、有限長性・飽和・随伴素点・深さ、各固定次数の漸近非消滅 | 一般次元の有限長性には既存の被約分類を入力する。n=9,10 の全 Hilbert 関数と、一般次元の冪零根基自身の積は未決定 |
| 残余圏 | HH sector の次数、幾何的 KS、滑らかな変形源と形式認識、tame hull、n=4 の例外、rotation | 通常 Artin 基底・特殊ファイバー固定・一次切断。全高次群oidや導来基底、全 Abel 形式変形との同定、全 intrinsic 成分を覆う大域残余射は未主張 |

五次元半 rotation の降下、非分裂 index 九の実現、周期位相の二変数帰着の証明を執筆担当以外も独立して読解点検した。従来の周期規格化・最小次数、高次元 class の簡約、七次元の既知球面対象からの帰結に関する有効な点検も保持した。上表には保持した既存結果も含む。適用範囲と未解決条件は冒頭に記す。外部査読、Lean 等による形式検証、既存の全証明の一括再検証を行ったという意味ではない。

## 3. 二次階数の整数証明書

保存済みの全6例について、指定した平方小行列の行列式を探索とは別経路で直接計算する検証が完了している。以下はその保持した結果と対象資産のハッシュである。全6例の再実行は本版の追加検証には含めない。

| N=n+2 | 小行列の次数 | 行列式 mod 32003 |
|---|---:|---:|
| 5 | 5 | 15512 |
| 6 | 35 | 14374 |
| 7 | 140 | 7973 |
| 8 | 420 | 508 |
| 9 | 1050 | 13073 |
| 10 | 1980 | 16095 |

全て非零。本文の上界と合わせ、5≤N≤10 の一般二次階数を決定する。N≤9 では I=J、N=10 では dim(J/I)₂=330 を得る。滑らかさは階数開集合と滑らかな三次の非空開集合の交わりによる。

```text
computations/verify_jacobi_rank.py
e5c1d00466265b44d6c2ea23c158a22133526231d9c2114db8ac8782d58d8ee3
computations/jacobi_rank_certificate.json
43482f8a6decff0cddc1d077abc12aeac584e5eb3b2898ad717c59793475588f
```

## 4. 八次元の次数三の厳密検証

保存した220個の対称整数テンソル成分を用い、整数 Jacobi 二次式の係数を法2へ還元した。三次多項式 T(z,z,z)/6 を標数二で解釈する計算ではない。Python 3.12.14・NumPy 2.3.5 と C++17 により、近似演算を使わず以下を再生成・検証した。

| 検証対象 | 確認値 |
|---|---:|
| Plücker 二次空間の次元 | 2310 |
| Jacobi 二次空間の階数 | 1980 |
| 二次商 D の次元 | 330 |
| 一次倍 p_s g_a の総数 | 277200 |
| 多重次数ブロック数 / 最大行数 | 23050 / 420 |
| 三次 Plücker 空間の階数 | 186340 |
| 一次 syzygy 空間の次元 | 90860 |
| E⊗D の次元 | 39600 |
| 保存した正方小行列の次数 / 行列式 mod2 | 39600 / 1 |

全 Jacobi 多項式が構成した Plücker 基底の線形結合と一致することを、非標準項だけでなく全係数について検証した。多重次数の同次性、核ベクトル数、行列の SHA-256、証明書の行番号の相異性も確認した。各ブロックで従属した入力は、source の新しい座標を持つ核ベクトルを与え、合計90860本が核の基底となる。

探索には低位 pivot のブロック消去を用いた。保存した39600行の平方小行列は、別の高位 pivot の通常 Gaussian 消去で直接検証し、全階数39600・行列式1を確認した。現在の保存対象コードによる再生成からこの検証までの実行は完了している。本版ではこの大行列計算を再実行していない。検証器と数学的な縮約の論理は、実装担当以外も読解点検した。

完全列 K→E⊗D→(J/I)₃→0 により、法2で元の Jacobi 二次式の一次倍が J₃ 全体を生成する。標数零へ移すのは、**元の整数 Jacobi 三次係数行列**の階数下界186340である。有限体で構成した個々の syzygy の持上げを仮定しない。標数零での I⊂J と次元上界を合わせて I₃=J₃ を得る。

```text
computations/verify_jacobi_vertex.py
cc899ad2dd1ca29b2a816f04a9f26664ba3d474c92a7b1c112bf7ab3ac86c7a9
computations/verify_binary_minor.cpp
7a52f8d19ce95db0548d8ae95cb77f9c6ee3bdace55d51ca6765df77c03c5f19
computations/jacobi_vertex_certificate.json
cdfa77d08a4375ce5b6d9abce70b8dc90de8cce31f561c5db7a29e0b2283dc76

再生成した 90860×39600 行列（449757008 bytes、非追跡）
314f31ba61792baff9c4adff367ed15c5a83ab004fdbcd52900dbc25e9b583d9
```

N≥11 の二次最大階数と、n=9,10 の全 Hilbert 関数を確定する計算は未実行。全 n≥11 の特殊非零点の330次元部分空間は、八次元の検証済み結果と本文の retract の証明から導き、各次元での個別実験に基づく主張ではない。

## 5. 中心評価・Hessian・trace の厳密記号検算

`computations/verify_center_hessian.py` は保存済み検算で SymPy 1.14.0 により全assertionと二つのPASSを確認したコードである。本版ではこの既存計算を再実行していない。検算対象のSHA-256は `20bb71ce1b8c56f0e81a3776dce38c1f1f786ec54a44c409a0ecf2c71d4721bc`。浮動小数点、係数の補間、ランダムな有限標本は使わない。

- 公刊Rains式の可換化と、κ=−4h⁴(1+λ³)/(1−hλ/2)⁶ の差が三偏微分のイデアルに入ることを、明示的な係数恒等式で確認した。統合担当は別の短い式の簡約でも係数を確認した。
- HessianのJacobi類が8(1+λ³)xyzとなる恒等式と、固定入力のHesse中心のW−λUを確認した。
- 六つの混合係数を独立記号とするFermat型の八次自由代数を、平方自由単項式の基底で扱い、正規化traceと有限hの純中心補正を計算した。これは任意個の中心変数への特殊化を許す係数恒等式である。
- 最後の比較に用いるΩの非可換中心性は、固定入力の `cor:pg-hesse-hessian-form` を使用する。このスクリプト自体がその中心性やPBW性を再証明するわけではない。

### 幾何補正と残余比較の保持した厳密検算

`python computations/verify_geometric_corrections.py` は保存済み検証で全assertionと13個のPASSを確認したコードである。本版では再実行していない。検算対象のSHA-256 は `78f592342b91531a6382576cc6025c8684e7f56d5efa84019b02d91b9923b85c`。その確認対象は次の通り。

- 四変数の二十個の三次単項式上で全十六個の gradient 一次倍を消す多項式汎関数、u³での値3t、t=1での階数16→17。
- 滑らかさの二因子 `(1+12t³)(1+2t³+5t⁶)` と、八次自由臨界代数のtraceによる `F_t+h²t³u³`。
- 一般Hesse中心元のh⁴境界項がg_λの倍数であり、境界Jacobi環で零となる恒等式。
- 独立六記号の対称3×3行列について、Θ=−2adjの全九成分とρ₂F=det(Hess)/8、線型形式の星積冪の帰納係数。
- Fermatの二次差 `xyz/3` のJacobi非消滅。追加の中心変数への一様性は本文のテンソル積による証明であり、有限個の次元の標本確認によるものではない。
- split Hesse の `b_h−h a_h=−2h²(1+h³)/3`、λ_res−hの有理式、j差の初項13824h⁴とh⁶までの係数。
- active symmetrizerの九元一次方程式で、明示八次小行列式 `λ²(λ³−8)²` と核がscalarであること。

traceについては、別担当がGroebner基底と八次乗法行列を別実装し、本文の値を独立に再確認した。上のスクリプトは非可換中心性、formalityの存在、MF同値、Torelliを機械的に証明するものではない。

### Poisson 補正について保持している厳密検算

保持した検証では `python3 computations/verify_poisson_correction.py` を実行し、SymPy 1.14.0で全assertionと11個のPASS・終了コード0を確認した。独立した十個の三次係数、六個の対称行列係数、独立な λ,s を用い、浮動小数点・補間・有限標本への特殊化を使わない。

- `adj(C(p))=ppᵀ` と `det(C(p)+tM)=t pᵀMp+t³det M`。
- 全三変数三次での Euler–Hessian 恒等式と点曲線 `g+s²det(Hess(g))/24`。
- 二パラメータ Hesse 係数 A,B,ν、変位 ν−λ、中心元の係数を既知の cyclic 式から変換した恒等式、Hessian 正規化と h⁴ 項。
- Sklyanin 点曲線の係数と移動切断、λ=s=h での固定入力の式、二次・四次係数。
- 方程式直線の rescaling と active 座標だけによる規格化。
- 研究ノートの framed 二パラメータ chart における一般次数9。分子次数9・分母次数6・多項式 gcd が1であることを有理関数体で確認した。全混合係数と商 stack の次数9には別途本文の証明を使う。
- 混合二次項の線型写像Lの6×6行列式、active全十係数での微分行列式。
- framed p′=1 被覆の判別式の全係数とresultant、次数10・平方因子なし。S₉という群の帰結は研究ノートの位相的議論を併用する。

Hesse 係数と cyclic 中心式の変換は、別担当の短い独立実装でも確認した。共有 repo には重複実装を残さず、上の検証器へ必要な assertion を統合した。この検算自体は非可換中心性、formality の存在、MF 同値、有限降下を機械的に証明するものではない。

### 五次共変式・四次 scalar jet の厳密検算

`python3 computations/verify_cubic_covariants.py` を実行した。Python標準ライブラリの整数とFractionのみを使い、次数1〜8の三次共変式の重複度 `1,0,1,0,1,0,2,0`、不変式の次数2,4,6の重複度 `0,1,1` を有限の重み計数で確認した。四つのε縮約の6⁴項を有理数として展開し、Sが25個の整数係数単項式を持つこと、S(xyz)=1、S(g_λ)=λ(λ³−8) を確認した。五次tensorの係数1/80はこの計算だけから得たものではなく、Lindberg–Pymの既知定理と本文のPBW・一意性の証明を用いる。Kontsevichグラフ重みを直接積分した検証や形式証明器による確認ではない。

同じ検証器で混合jet型の重複度1,2、三つの勾配共変式の独立性の行列式−35/3、I(g)=J(g)=S(g)gの比例係数を確認した。重み計数は別担当が別の多重集合列挙でも照合した。保存済み検証では qMT³ と M³T² の scalar jet も加えて現行検証器を実行し、最高重み(4,4,4)のWeyl公式の六項がそれぞれ `(156,−136,−136,100,109,−92)` と `(122,−105,−105,78,84,−73)`、和がいずれも1であることを確認した。保存コードは共通の有限重み計数を共有し、重複実装を残していない。この重み計数だけで graph の数値係数や中心逆像を決めたわけではなく、以下の別計算と本文の局所共変性の証明を併用する。

### 混合五次 tensor と73項 graph certificate

`python3 computations/verify_mixed_fifth.py` と、その `--source-directory` を指定する元資料照合を実行し、全assertionと全PASSを確認した。Pythonの整数・FractionとSymPyを使い、浮動小数点や数値積分を使わない。入力 `computations/data/harmonic_linear_products.json` は必要な73項だけを収め、元ファイルのSHA-256、取得元、係数規約、graphの辺・weight・自己同型群位数を記録する。二つの新規資産のハッシュは次の通り。

```text
computations/verify_mixed_fifth.py
8388956c8cf6bee1e4e28f20a36edbe6d01ac1586779dd4ced86d0b3fc2db0d8
computations/data/harmonic_linear_products.json
fc960343d5f4f1536881bf678b8bc4fda9a438e0dc0f029fe6d7840364b6d7d6
```

Buring の元資料 `star5.txt` のSHA-256は `05e0689ddb32a3d3a3ee4475086606bbeb9b5d71f8e24da2c216e43564a31129`。線型二入力と二次tensorに寄与する条件で残る非零項数は、頂点数1〜5の順に `1,1,1,19,51` である。原資料の `fg+h{f,g}` 規約を本稿の `fg+h{f,g}/2` 規約へ変換し、k次の組立係数を2^kで割る。aerial頂点の置換、outgoing edgeの交換符号、自己同型群の位数を含む有限列挙により、全73項で組立係数/2^kとraw weight/Autが一致することを確認した。元資料11ファイルのハッシュも照合した。

五次再帰には π₃=Π_det(Hess F)/24 の一頂点への挿入の和と、二次式のWeyl対称化の四次係数を含めた。表はxy成分の厳密値であり、W列はこのWeyl寄与を表す。

| 試験式・評価点 | B₅ | B₃のπ₃挿入 | W | π₅=−2(B₅+B₃)+W |
|---|---:|---:|---:|---:|
| xyz、(1,1,1) | 1/720 | 0 | 11/720 | 1/80 |
| xyz+z²/2、(0,0,1) | 1/480 | 0 | −1/144 | −1/90 |
| xyz+z、(0,0,1) | 1/720 | 0 | −1/240 | −1/144 |

後二式は一つの中心変数uで斉次化してからu=1とする。二定数への普遍還元と合わせて β=1/60、γ=1/240、α=−1/120 を得る。各試験jetで三次再帰も既知のHessian項と一致した。独立した非log型混合jet `(x³+y³+z³)/3+xyz+x²/2+xy+x` の原点では、volume-dual五次成分 `(1/30,−11/720,1/36)` が三共変式の公式と一致した。また二変数Poisson tensor `xy ∂x∧∂y` の原生成元積の五次までの係数 `1/2,1/24,−1/48,−1/1440,1/480` がBPPの公刊展開と一致した。

別担当の独立したFractionによるgraph縮約も、二つの混合試験式と定数β,γについて同じ値を与えた。さらに元graph–weight対の別実装で符号・自己同型群・正規化を独立に照合した。保存対象には再現に必要な一つの検証器と証明書だけを残し、独立実装の重複や大量の元資料は収録しない。73項の入力は公刊weightsに依存し、この検算はconfiguration-space積分の再証明、全次数のformality、MF同値、形式証明器による検証を含まない。

### 四次中心 potential と一般次元の障害

`python3 computations/verify_fourth_potential.py` を実行し、SymPyの厳密多項式演算で全assertionと6個のPASSを確認した。次の四項目に、下記の古典的表示の二恒等式を統合した現行コードによる実行である。

- Hesse係数 λ,A,B,C,D,E,H,G を独立記号として、入力中心元の四次symbol Ψ と `−SF/80−I/40+J/60+C₄(U)` の全係数が一致すること。
- 別途graph計算で得たβ,γから、`W₄=Ψ+I/24−J/80`、`a₄=S/240`、五次tensorの式が恒等的に両立すること。
- Fermat active切断で Jが勾配イデアルに属する明示恒等式と、`[Δ₄]=[ACx+ABy+BCz+AH+BD+CE]/9` を与える係数恒等式。
- 全次元に共通するF_*の三次単項式上の線型汎関数ℓが、全gradientの一次倍と純中心三次を消し、`ℓ(Δ₄)=−1/9` となること。

全nへの拡張は追加変数が独立な三乗で現れる本文の証明を使い、有限個の次元の実験から推測したものではない。F_*の滑らかさ、Jacobi束の非消滅開、scalar jetによるW₄の普遍性、標識付き幾何・Ku比較の小拡大の議論は本文の証明と内部読解点検に依存する。これらの全てをこのスクリプトが機械的に証明したとはしない。

Ψは固定入力Aの `cor:pg-hesse-hessian-form`・`eq:pg-hesse-hessian-closed` にある指定中心元から採った。純中心補正と中心元の単元倍を区別し、Ψの可換Weyl symbolの展開を検算した。その非可換中心性やPBW性自体を再証明したとは主張しない。別担当も全Hesse係数のΨ恒等式を独立に記号検算した。Kuへの四次障害は指定MF・window入力付きであり、固定h・特殊ファイバーの標識を外した一般ファイバーの非同値へ拡張しない。

### I,Jの古典的表示の独立検算

独立したSymPy検算で2個のPASSを得た。対称三次tensor Tの10係数、対称行列Mの6係数、ベクトルqの3係数を全て独立記号とし、次の二恒等式の差が有理数係数多項式として零であることを確認した。補間や数値標本を使わない。

\[
 I=\frac1{12}\operatorname{tr}\!\left(\operatorname{adj}(M)
  \left.\operatorname{Hess}_x\det\left(M+\sum_kT_{::k}x_k\right)\right|_{x=0}\right),
\qquad
 J=\frac14\,dS_T[N],\quad
 N_{ijk}=\frac{M_{ij}q_k+M_{ik}q_j+M_{jk}q_i}{3}.
\]

後者の方向微分は、SをTの10個の独立係数の多項式として微分している。この独立検算の後、二つのassertionを現行の四次検証器へ統合し、全6項目の実行成功を確認した。現行検証器のSHA-256は `a58f1f8f1979a3d289ff55bb2665a2c008bab3e7e9fe2a49b6343c27c661f2d4`。独立実装の重複は保存しない。

### active 不変量の厳密恒等式

保持した検証では `python3 computations/verify_active_invariants.py` を実行し、十五群の PASS と終了コード0を確認した。従来の不変量・判別境界・I₃・Kummer・特殊線型行列の十三群を保持し、明示相対行列の有理式、slope による点の符号、厳密な L₀ への特殊化を第十四群に加えた。第十五群は余因子による六次元二次式空間の係数行列式 +2p と、任意の可換記号 G₁,G₂ による24×24 tensor MF の平方が (bXYZ+u₁G₁+u₂G₂)I となる恒等式を検証する。各 parity の階数は12である。すべて Q、Q(p,q) または Q(ζ₃) 上の厳密演算で、浮動小数点・標本抽出・補間はない。相対線束の同定、右射影、低 Ext、m₂/m₃ の integral な存在の一般証明は本文に依る。full 周期位相の値を計算した検証ではない。SHA-256 は `05cb75af610c90e9f4098a27fac3803cddcaba97958b6ab2549ec151d3623ffa`。

### 境界低積と最初の非零項の厳密検算

`python3 computations/verify_boundary_low_products.py` の十群全てで PASS、終了コード0を確認した。三つの cocycle、九つの pair products と唯一の homotopy、四つの exact minor と kernel 次元、n=3 full m₂ の階数七の unit minor、actual 相対 L の一次曲率、正規化した全 cocycle lift の閉性、m₂ 一次係数と −2/(27p³) の minor、正符号の x³ transfer、m₃ 一次係数 acb/(3p)、十八個の二次関係倍数を消す三次双対汎関数、source 関係と指定中心の特殊化、D の一次係数との cube 比を確認する。

検証器は有限行列と必要な minor の添字を内部に持つ自己完結した一ファイルで、外部 JSON や大きな計算出力を要しない。SHA-256 は `ead99c04dde10e3101dd1ebb25a91c264788e52e2a619512bbeaca3ad0076cb5`。三つの Smith 指数一を実際の一次係数から確認しており、有限体標本や数値補間は用いない。全 n の窓同定・自由性・飽和後の全次数平坦性・Benoist による指定 Isom の延長・Kummer 降下は本文の証明を併用し、このスクリプト単独の形式検証とはしない。

### Hesse の二次類と三捩れ対称族

保持した検証では `python3 computations/verify_active_sign.py` を実行し、6個の PASS・終了コード0を確認した。Q(ζ)、ζ²+ζ+1=0 上で、Hesse 群の二生成元による c₄,−c₆ の不変性、quaternion 関係と C3 の共役作用、24元の群の閉性、固定体の次数上界を与える四次式と三次式、μ₂ 指標の自明性、および滑らかさに現れる 1+4k・2+4k の非消滅を照合した。群の有限列挙と多項式係数の演算は厳密である。

この計算は、全nのscalar symmetrizerの紙上証明、有限対角による近傍延長・同変降下、χ_act消滅の全論証、MF比較の存在を機械的に検証するものではない。点平行移動と rotation の共役は本文の関手計算による。以下の新計算は、別途必要となる整数行列の centralizer を含む。

### Picard 障害と Sklyanin 表示の厳密検算

保存済みの検証で `python3 computations/verify_picard_obstruction.py` を実行し、SymPy による有理関数・多項式の厳密演算で全 assertion と13個の PASS、終了コード0を確認した。本版ではこの検算を再実行していない。

- Hesse 型曲線の接線を代入した三重点の恒等式。
- ζ²+ζ+1=0 での三つの接線比の積と b+λ³/(27a) の一致。
- normalized potential の J_g=g+det(Hess g)/24 と元の点三次の比例式。
- Hesse potential の二係数 P,Q と (A:B:C) の有理逆。
- symmetric cubic の特異性が Hesse 曲線の特異性を強制する係数恒等式。
- 数値 rotation R の整数 centralizer の六元計算。全列挙の範囲の十分性は、本文の正定値 determinant 形式による |b|≤1、|a|≤2 の証明を用いる。
- 巡回 twist C_d の cube root 後の平面同型、接線 norm 係数の d² 倍、三次 symbol 補正 (d,aB) の外積係数を法三で照合した三つの恒等式。

- 普遍 Jacobian 上の表示した点の曲線方程式と三捩れ方程式。
- Hesse 群による八点の軌道と位数三の安定化群。
- その安定化群の normal core が自明であること。
- 右点対応が原点を (A:B:C) へ送る三関係式。

有限標本の外挿、浮動小数点、係数補間は使わない。この検算は Brauer 類の非零性・potential の降下・支配性・導来同値の形式証明ではなく、それらの紙上証明に用いる係数恒等式の確認である。既存の同一再現コードには三分点の四つの確認が統合されており、基準版の15計算資産に含まれる。重複実装・大量出力は保存しない。検証コードのSHA-256は `12237ed3f92874f18fbfb8dd7cecaf63d8fef01d52e737f00671bf05838929be`。

### 五次元 Fano 曲面の次数の厳密検算

保存済みの実行では `python3 computations/verify_fivefold_plane_degree.py` により、

`PASS: degree(F_2(Y)) = 2835; gcd(degree, 2) = 1`

と終了コード0を確認した。tautological bundle の双対 S* の Chern 根を x,y,z とする規約で、

\[
 [x^6y^5z^4]\!
 \left(\prod_{a+b+c=3}(ax+by+cz)\right)
 (x+y+z)^2(x-y)(x-z)(y-z)=2835
\]

を Python 3 の整数多項式演算だけで求める。浮動小数点・補間・有限標本を用いない。Ciliberto–Zaidenberg の既知の係数公式と値を独立に再現したものであり、相対 Clifford 核・gerbe・Galois 降下の証明を計算で置き換えない。検証器の SHA-256 は次の通り。

```text
computations/verify_fivefold_plane_degree.py
b7a9f66af04e2b4506aff22e87ebc53d3bc1eaa3466af0059d13025a424c019d
```

## 6. ソース・組版の確認

### ソースと参照

`python3 scripts/check_sources.py` は終了コード0で、24 TeX sources、553 unique labels、363 referenced labels、103 cited bibliography keys を確認した。`git diff --check` も通過した。五つの主要 Markdown 文書のローカルファイル参照63件を確認し、欠落はなかった。現在の追加証明は `papers/sections/residual_boundary_products.tex` に統合し、既存の境界模型から読み込む。主原稿の要旨・序論・主定理・到達範囲、関連節の未解決課題、研究方針・ノート・README の記述を現在の局所結果へ合わせた。

### PDF の組版状態

現行 v25 を `latexmk papers/nc-cubic-n-fold.tex` により LuaLaTeX で組版し、終了コード0、333頁の PDF と同じ出力先の SyncTeX を確認した。最終ログに未定義参照・未定義引用・欠字・overfull/underfull box はない。既存の小さい数式フォントのサイズ置換7件と、その集約警告は残る。

生成した PDF の1、8–9、21–22、25–26、253–267、326、331頁、計24頁を PNG として実際に目視した。統合担当は表題・概要、先行研究、主定理、到達範囲、追加書誌の9頁、独立担当は境界低積から局所位相までの追加節15頁を確認した。二つの横長行列は折り返して再組版し、最終版では数式のはみ出し・重なり・欠字・切断を認めなかった。全333頁の再読・全頁拡大点検ではない。PDF は2,528,652 bytes、SHA-256 は `80a5f3f9beccfb2bb59670eb4972dd81052339443e2b4628e3c80701f0170470`。

## 7. 再現と保存の区別

再現手順はルートの `README.md`。原稿は `latexmk papers/nc-cubic-n-fold.tex` で `build/` に出力する。主要依存は LuaLaTeX・LuaTeX-ja・和文フォント・標準 TeX パッケージ、Python 3・NumPy・SymPy、C++17 コンパイラ。次数三の検証は約450 MBの行列を再生成し、直接消去には約220 MBのメモリを用いる。大行列は保存せず、220個の入力・行番号の圧縮表・検証コードから再生成する。

保存対象は現在の原稿、研究方針、研究ノート、本検証範囲、書誌、再現コード、証明書、必要な設定だけ。入力稿の全コピー、旧稿、旧bundle、担当者別レポート、外部文献PDF、ビルド中間生成物を含めない。PDFは再生成物として提供し、Gitの追跡対象に含めない。

外部への保存は生成・検証とは別に、GitHub の tree にある全ファイルの blob SHA を手元のソースと照合し、通常の fast-forward による main の更新後に、先端 commit と tree を読み直して確認する。保存された版の識別子は Git の履歴と配布時の報告に記す。この文書だけをもって、未実行の外部保存が完了したとは扱わない。
