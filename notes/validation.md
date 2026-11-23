# 非可換三次超曲面：現行稿の検証範囲

2026年11月23日 / v89。正本はGitHub main。証明記載、独立読解、厳密計算、組版、表示確認、保存を区別する。

## 混合尺度・階数一の残余特異点・固定切片の高次係数

- **一方向九変数のShamash一次中間成分・厳密二次多項式（v89）：** [現行二命題・証明](../papers/sections/mixed/interfactor_clifford_mixed_shamash_first_middle.tex)（`ifj:prop:mixed-shamash-first-middle`, `ifj:prop:mixed-shamash-nine-parameter-certificate`）に、全許容Cliffordτ_i・非零中心重みと全九係数Λ=sUについて、既知primitive uとd₁,d₂による**d₂H+u d₁=w_s I₆**が内部次数二のHをもち、細分次数degΛ=(2,−2)により厳密にH₀+sH₁(U)+s²H₂(U)とできることを証明記載。w_y部分はs定数。原点のS₃×S₃ Shamash規格化をKoszul d₃の像で合わせ、36元Reynolds平均により同変に選べる。具体的なH係数はτ₁=τ₂=2,a_i=1の九変数全体で計算。**厳密実行** `python3 /mnt/data/nc-cubic-current/verify_clifford_mixed_shamash_first_middle.py` はPython3/SymPy1.14で**7群PASS・終了コード0**、全九単位方向のPBW係数写像336×315のexact rank210、その210×210小行列の厳密有理数逆、H₀の6列、H₁の9×6列、H₂の45×6列（各336式）の成立、九変数三次165単項式の全6列×336係数の消滅を確認。四指定probe E₀₀,R₀,C′₀,D₀と一般整数Uを追加厳密照合。浮動小数点のピボット選択・係数補間は使用しない。実行ソースSHA-256=`356f197971893ef6ec4950d56d9e23ee36b1d6a2ef12fc09689c82d54061c374`、Git blob=`33e79970aae59f08b7d92933337515eae15eb15d`でGitHub保存ソースと一致。**日本語LuaLaTeX独立組版**：保存済みTeXの全文をltjsarticle wrapperで二巡組版、**3頁**、終了コード0、overfull/underfullなし、全3頁をPNG表示点検。TeX SHA-256=`3309db86c1fb8656633ae8fd6f347b6261782933f8bbc4d6c080860bec9aa930`、Git blob=`fd7dd23f64401cf568a70aa157095e488a6d2782`が組版ソースと一致。独立wrapperでは他稿の参照未解決；全稿LuaLaTeX組版・全参照収束、一般τでのH係数全展開、Shamash s₁のP₂–P₅成分とs₂以降、混合32|32MF・実Ku比較Hom(i,p,h)・unit/counit・rotation/三乗period・四probe46原式/12高次値、形式証明器・外部査読・新規性網羅調査は**未実施**。

- **双方向18係数Cliffordの正則resultant開の全六段Koszul自由解消（v88）：** 公表用混合稿の`ifj:prop:mixed-koszul-endpoints`（d₁,d₂・曲率端点）、`ifj:thm:mixed-koszul-full-third`（全係数上d₃の全20列・大域自由基底）に加え、[現行定理・証明](../papers/sections/mixed/interfactor_clifford_mixed_koszul_frobenius.tex) `ifj:thm:mixed-koszul-frobenius-upper` で二次双対E=D^χの次数2平方なし15基底・次数3平方なし20基底が旧d₃の係数座標と一致することを証明。Δ_res≠0で既存`ifb:lem:relative-ci`のγ=2^-6det(∂g_i/∂z_j)・Frobenius完全対合によりK₄=E₂,K₅=E₁,K₆=E₀を自由化し、d₄の全20×15成分をΣ_j z_j t(mνζ_jq_r)、d₅をE₂のζ_jζ_i係数、d₆を六生成元列として有限係数抽出する。全六段の解消完全性は**既存**`ifb:thm:regularity`に依存。**新計算:** `python3 computations/verify_clifford_mixed_koszul_frobenius.py` は、ローカルPython3/SymPy1.14で**新12群PASS＋依存のd₃検算器9群PASS・終了コード0**。対象は**一つの非零双方向点**τ_i=2,s=1,U₁₁=V₁₁=1（他零）：グレブナー正規形によるE₂(15)・E₃(20)基底、γ=33u₁u₂u₃v₁v₂v₃、Frobenius積のE₂–E₄/E₁–E₅完全対合、旧d₃全20列との成分一致、d₄の非零104構造係数とy₁/33例、B₂の21PBW基底すべてでd₃d₄=d₄d₅=d₅d₆=0。保存済みの新計算器Git blob=`23c078b0a4b3c7d22838e29e1a04dbc51a86dd56`とローカル実行版の`git hash-object`一致、ローカルSHA-256=`819a34e1dedbb02d0e2bbf97e6d2b6625b37df5337e19c08cb81777861bcfc3d`。依存d₃スクリプトの最新Git blob=`0552454657cd7e08df8b0606cf6fd9ee3f3ca101`とも一致。**新TeX組版:** 定理・証明全文を日本語ltjsarticle/LuaLaTeXで二巡・**3頁**、終了コード0、全頁PNG表示点検。保存TeX Git blob=`4f8935d1f2ce8aa50bfd089cb31a212ca8052372`と実組版原文一致、原文SHA-256=`be7c23fee7fb3654b46b01b987ab74e97288bcb4ad4dccb96d59ef5cf03c9cf5`。独立wrapperの他節参照未解決と原稿全体の組版は区別する。**未実施:** 18係数一般の300成分の全多項式展開、resultant零の基底延長・全複体完全性、一方向P₁中間以外のShamash中間/高次homotopies、混合32|32MF、実Ku核・Hom特殊収縮(i,p,h)・unit/counit・rotation/三乗period・46原式/12比較値、三稿全文組版、形式証明・外部査読・網羅的新規性監査。

- **S₃×S₃厳密同変の原点Shamashと混合九変数族（v85）：** [現行命題と補題](../papers/sections/mixed/interfactor_clifford_explicit_shamash.tex)（`ifj:prop:clifford-explicit-shamash`, `ifj:lem:mixed-clifford-s3-family`）ではκ=(4−τ³)/6を用いる明示的なKoszul–Shamash higher homotopiesからD₊D₋=D₋D₊=ΩτI₄を構成し、反転σ(x)=−PxのKoszul各段作用(1,−P,P,−1)、最上syzygy線−1、F⁰/F⁻¹の反転行列diag(1,P)/diag(−P,−1)と巡回の厳密S₃関係を証明した。s₁²のx₁⁴係数τ(τ³−1)(τ³+8)/18は非零。二因子原点の32|32外積・中心scalar aの重みも保つ。さらに全九係数ΛにはS₃×S₃が行・列の置換として作用し、混合二次関係・Clifford両体積元・中心三次wを固定する。既に選択した同変(n−1)次のMF jetがn次へ可解なら、線型補正を36元平均して同変解にできるが、可解性は未証明。**ローカル厳密検算：** `computations/verify_clifford_explicit_shamash.py`はSymPy1.14で15群PASS・終了コード0、実行SHA-256=`25cc452fda95e3b23605e700c2ff9203cb950b2be3ac4a26de5a051ccadc028d`、保存/実行Git blob=`d60e0229c86123e37d0dd8debb248a2c8519a552`。`computations/verify_clifford_family_s3.py`は8群PASS・終了コード0、実行SHA-256=`920e05163827548f532bf4ac444d0af24a334c8fe2e0ac56ffc3d8b1ef288e87`、保存/実行Git blob=`9d938709e65ca08059f69ba6da85908c97ed96da`。**組版：** 現行TeX全文を独立ltjsarticle/LuaLaTeX二巡で3頁組版、終了コード0、全頁をPNG表示点検。保存TeXのGit blob=`f4837f38525cec213a86b9a37e1e7f3f5790aa32`は組版ソースと一致。**未実施：** 保存済み混合稿全体と三稿全体の組版、混合Ku比較核・Hom特殊収縮(i,p,h)、unit/counit・rotation/三乗period整合、46原式・12高次係数、形式証明・網羅的新規性監査・外部査読。有限群平均や源MFの同変性からこれらは結論できない。

- **Clifford曲率付きPBWのHochschild二次障害と高次整合（v82）：** `ifj:prop:pbw-curved-mc` に∂m₂=m₁∘m₁、三・四次のMC恒等式、中心曲率ω₀+sω₁の4次数交換子恒等式、非線形二probeの非零証人(m₁∘m₁)(e₂,e₃,e₁₂)=L₁L₃を証明記載。二次primitive m₂は全8×8積で4枠のみ、他の二probeでは消滅。ローカルPython 3/SymPy1.14で `computations/verify_clifford_curved_pbw_mc.py`とバイト同一のコードを実行し**厳密10群PASS、終了コード0**（512組×5結合律次数、中心32検査、障害80非零係数枠と非零証人、四probe）。保存済みGitHub blob SHA=`0a473624b4805e3375225126ab7ec45aaf510131`はローカル`git hash-object`と一致、ローカルSHA-256=`ddc8af01539ef73b11d18ddf9cb6535981144ffa0ce14b4e69d44630c3ad1ba8`。追加命題の日本語LuaLaTeX簡約独立抜粋は**1頁の組版・終了コード0**、他節参照はwrapper中で未定義（保存済み混合稿全文や三稿全体の組版ではない）。通常のClifford結合律が既知であることと本固定PBW規約の具体計算を区別する。曲率付きKS比較核・special retract・unit/counit・rotation/period・12高次係数、形式証明器・外部査読・一般的新規性監査は未完了。

- **対称Picard MFのアフィン縮約と被覆符号積の同一視（v81）：** 混合稿`ifj:prop:picard-affine-bridge`に、Z=1で三角TによりTLTᵗ=S⊕(−1)、随伴の対応、cokerS≃I=(x,y)、β単元でI²=xAとM²規格化積rs/xを明示する命題・証明を統合。標的二重被覆B=R⊕Iの符号成分の積と同じ係数・符号で一致し、反転にも両立。`computations/verify_clifford_picard_affine_bridge.py`と同内容のローカルPython3/SymPy厳密検算は**8群PASS・終了コード0**。GitHubで読み戻した保存コードのblob SHA=`4fe5d27de316e5a72c0a1bf2ee2092b09b630b5e`と、8群を実行したローカルファイルの`git hash-object`が一致。実行ファイルのSHA-256=`5c8213728b7d6024111e6c0330ee333488874049ab44c78d64f18171948c71a7`。独立した日本語補題・証明の簡約抜粋はltjsarticle/LuaLaTeXで**1頁の組版・終了コード0**（全稿や保存済み節全文の組版、PDF表示点検ではない）。非可換Koszul--Shamash比較核・unit/counit・指定周期・四probeの46原式係数と12値・全原稿組版は未実施。新命題の一般的新規性・一次文献比較は未確認。

- **二捩れPicardの対称3×3線形MFと正規化された二乗評価（v80）：** `ifj:prop:picard-symmetric-linear-mf` でF=Y²Z−X(X²+aXZ+bZ²)の対称線形行列L、detL=F、L adjL=F·I₃、cokerL=O_E(p−o)を証明。M(1)の基底(-Y/X,1,X/Z)とu=X/ZによるM²≃Oの規格化で、対称積行列が−adjLと一致する。反転Y→−Yの厳密D共変も証明。`ifj:cor:picard-symmetric-hesse-family` はHesse座標のdetLτ=4cτ²fτから三乗根なしで指定fτそのもののMFを与える。Beauville (2000) Props3.1,4.2、Buchweitz–Pavlov (2024) ThmAの一般既知結果を一次PDFで確認し、Clifford固定係数・二乗scalarの具体化と区別した。ローカル`python3 /mnt/data/nc_cubic_v80/verify_clifford_picard_linear_mf.py`はSymPyで**10群PASS・終了コード0**。SHA-256=`b65c0d09164303083486670af40c095e39c64a298e11ddf3ff0b78a6460680aa`、Git blob SHA=`d110b426c2625cf72b39618a6f1f6b14ea3d60eb`で保存済みGitHubコードと一致。独立の簡約した原式・Hesse正規化抜粋をltjsarticle/LuaLaTeXで二巡組版し1頁PDFをレンダリング表示確認したが、**保存された混合稿の新節全文または三稿全体の組版ではない**。今回の一次PDFはBeauville Prop3.1/4.2とBuchweitz–Pavlov ThmAの該当頁を確認した。可換因子のPicard二乗評価のみであり、nc比較核・period・46原式係数・12 scalarの数値化は未実施。

- **相対有限被覆のtrace/CasimirとHochschild収縮（v79）：** `ifj:prop:cover-trace-casimir` にI=(X,Y)の2×2冪等行列P_I²=P_I、B≃im diag(1,P_I)⊂R³、Θ=(η⊗η−(X−2a)ξ⊗ξ)/δ、Θ²=1、e±=(1±Θ)/2によるB⊗_R Bの対角・反対角の分離とtrace双対枠を証明。`ifj:cor:cover-hochschild-contraction` に任意のB-bimoduleの相対Hochschild正次数の明示cochain収縮・HH消滅、形式a(s),b(s)の三次δ逆数展開、有限étale Artin持上げの一意性（Stacks Tag0BQB）を証明・引用。ローカルPython3/SymPy1.14の厳密スクリプトは9群PASS・終了コード0（P、dual frame、Θ、trace、左右対称および非対称双加群のHochschild n=1..4、三次δ逆数、非定数三次路）。GitHub保存済みの再現器`computations/verify_clifford_cover_trace_casimir.py`を独立にローカルで復元して実行し、9群すべてPASS・終了コード0を確認。保存Git blob SHA=`88028e6b66ef2fefb29d60d7b1462f16a0bd422f`、実行ファイルのGit blob SHAも同一。実行ファイルSHA-256=`d97be70dfb3539cf06078c9c200048753318f7f2b980ec960569adb33301eb38`。有限被覆のHH収縮をcurved Koszul–Shamash HPLのhと混同しない。実比較核・rotation/period・46原式係数・12値は未完成。改訂3稿の統合LuaLaTeX組版・PDF表示、形式証明・外部査読は未実施。

- **相対二重被覆の正規化とPicard斉次2×2行列分解（v78）：** 混合稿`ifj:prop:double-cover-algebra`に、K上のB=R⊕I、I=(X,Y)、I²=(X)、deck同時符号、積ij/X、任意底変更への互換と粗い平方根被覆の偽の通常二重点を証明。`ifj:prop:two-torsion-matrix-factorization`に源と標的の2×2行列積AB=BA=F1、余核=(X,Y)、層O(−p)、一点捩れO(o)の必要性を証明。`ifj:cor:double-cover-sign-descent`に標的符号線束の源への引戻し自明化と残るdeck符号を記載。Python3/SymPy1.14で11群PASS・終了コード0（許容τの非零式、四次式被覆、deck、イデアル積、アフィン/斉次MF、粗い節点、τ=2/−1の滑らかさ、両側MF、Bezout）。ローカル実行ソースSHA-256 `6143d5813f4bb4ca580faa6f060fda855074c998b0961d5060111abd29180091`、GitHub保存blob SHA `e5be2c4fa7d07cd0b1f2b503b462a049445a3b40` は一致検証済み。保存後の独立した再実行ではなく同一ソースのGit blob照合である。相対的線束・正規性・cokerの数学的証明は本文にある。Ku比較核・指定周期・46原式係数・12 scalar未計算。最新3稿LuaLaTeX組版、形式証明、外部査読は今回未実施。

- **基点付き三次式によるisogeny有限座標模型（v77）：** `ifj:prop:two-isogeny-cubic-sextet`でW,T,Sの厳密なWeierstrass変換、共通基点因子D=2o+pを持つ6三次式、実際のdeck作用行列と±3+3固有基底、負固有線束N=M_{τ∨}、標的Hesseを構成する正固有三次式と次数9の多項式恒等式、反転同変性を証明として記載。`computations/verify_clifford_isogeny_cubics.py` をPython 3/SymPy 1.14でローカル8群PASS・終了コード0と確認し、保存済みGitHub blob SHA `8801f997328505750b95ce0a81d46bd6bfaa8251` とローカル実行ファイルの `git hash-object` が一致した（SHA-256 `73f94d20792a49cb04f5b4e8d246926062f7c2252c5788cf5e8edad225f53f2b`）。記号的な全係数のdegree-9恒等式と具体的τ=2,−1のHesse多項式除算を検算したが、曲線上の基点因子・線束同型・双対isogenyの数学的証明は本文による。実Ku核の比較や46原式係数・βγ12値には何も計算していない。保存済み節/三稿全体のLuaLaTeX組版・Lean・外部査読も今回未実施。

- **二重isogenyのtheta文字・±3次元空間・CM点（v76）：** `ifj:prop:two-isogeny-theta-characters` に引戻し偏極A=L²⊗Mのtheta交換子e_A=e_L²=e_L⁻¹、二重被覆の直像O⊕N、H⁰(E,A)のdeck±固有空間3+3と逆Heisenberg文字、Hom(L²,A)=H⁰(M)=0を証明として記載。中心文字の反転`だけ`では普通二次式を排除しないことを明示。CM特殊化τ²=−2でφ²=[−2]、j=8000、End(E)=Z[√−2]（`ifj:cor:two-isogeny-cm-specialization`）。SymPy 1.14のローカル`python3 /mnt/data/nc_cubic_v76/verify_clifford_hesse_theta.py`で修正版6群PASS・終了コード0を確認（SHA-256 `c998ae132435f375e94dfc3a572672effc32421e1afa28c6623fd27ac47882e5`）。初版検算では`factor`で整形されたSymPy式の構造的等値比較が失敗したため、`cancel`で差を零判定するよう修正してから6 PASS。有限行列・j恒等式の検算でありtheta群・Picard・Kuの圏論証や12係数を形式検証したものではない。GitHub保存後の同一ファイルの再読・再実行は別に報告する。全三稿LuaLaTeX組版・外部査読も今回未実施。

- **点楕円と中心判別の二重isogeny（v75）：** `ifj:thm:discriminant-two-isogeny` と `ifj:cor:isogeny-picard-line` に、D_τ=(τ³/8)f_{−2/τ}、核{o,p}の次数2 isogeny、Weierstrass座標式、往復[−2]、三捩れのdiag(1,−1)作用、φ*O(1)=O(2)⊗M_τ（非自明二捩れ）の証明を統合。普遍的なHesse/Cayleyan二重isogenyは既知理論と明記し、本Cliffordの係数・標識とPicard線束を照合した。`computations/verify_clifford_hesse_two_isogeny.py` の8群をPython/SymPyで検算し、GitHub mainに保存後にそのファイルを読み戻して復元した同一ソースでも **8 PASS・終了コード0** を確認した（保存ファイルGitHub blob SHA `131d67e8124c793300123fe7bbf35e9d032729ac`、再取得実行ソースSHA-256 `c5567ab615810ded9ca796ed6406358b0cbd7c841c89028b320066aa6a9a9ece`）。同内容の拡張下書きに対する単独ltjsarticle/LuaLaTeX組版は二巡実行・3頁を確認したが、**保存済みの節そのもの・混合稿全体を組版したことではない**。Picard引戻しの数学的証明は本文、8群は有限式の検算であり、形式証明器・外部査読・本三稿統合組版は未実施。Ku核の高次移送と12 scalarの数値・非消滅も未完成。

- **全九変数Clifford中心normの三次jetと比較非同一性（v74）：** `ifj:prop:central-norm-jets` の全係数D=det q_x(s) のs⁰〜s³展開、固定Hesse射影の二次covariantと三次invariant、単一三次不変式𝒮によるU-gradient・τ₁微分、四probeの三次norm（C′₀,I₃だけ非零）、N₀のHesse滑らかさ条件を本文に証明記載。平方中心変数を可換Hesse座標へ文字通り同一視すると一次KSのbidegreeがC₂₁（norm）とC₁₂（実比較）で異なることを明記。ローカルの`python3 /mnt/data/verify_clifford_central_norm_jets.py`はSymPy 1.14で全7群PASS・終了コード0（一般9記号の行列式、二次射影、三次不変式、gradient、一次成分、四probe、Hesse判別因子）。`computations/verify_clifford_central_norm_jets.py`をGitHub mainに保存後、同パスをGitHub connectorで読み戻した本文をbase64に変換し、ローカルで復元・再実行してもSymPy 1.14で7群PASS・終了コード0を確認した（再取得ファイルSHA-256: `d708383bc360fe6e8633a6cda4ffb0af09ab8ca62901f96fe274ca9cf501f982`、GitHub blob SHA: `eac924ee3bea1021d1c2c7594850dd9e31848059`）。したがって今回の中心norm有限計算は保存後の同一コードでも実行確認済み。中心normのidentityは実Ku比較核・周期・46枠・12 scalarの計算ではない。全三稿の統合LuaLaTeX組版・PDF表示、Lean・外部査読・網羅的先行研究調査も今回未実施。
- **固定Hesse四probeの46枠直接読出し：** `ifj:prop:direct-probe-readout` を混合稿へ証明として記載。G₁=κΣA_ab X_aY_{b+1}Y_{b+2}の一次標準化後に、二次逆混合・三次純X/Y係数を原式G₂,G₃の特定の14+32=46単項式係数枠から得る。純X三次には二次座標補正がなく、純Y三次にはκ/t₁と`[X_a²Y_b]G₂`の対合補正がある。四probeの逆評価行列も明示。Python 3 / SymPy 1.14で独立のローカル読出し検算を実行し、四probe×二次数×全56単項式、12係数の逆変換、対合係数と46枠算術、非零補正例の4群PASS・終了コード0。GitHubに `computations/verify_hesse_probe_readout.py` を保存。同内容の保存用ソースも互換名を付けたローカル基礎射影実装に対して実行し4群PASSしたが、GitHubからの保存後バイト列を取り直した再実行や全三稿のLuaLaTeX組版は未実施。これは比較核の出力の計算ではなく、12個の数値は未決定。
- **固定 Hesse 切片の明示 Jacobian 分解と三次正規化（v72）：** `ifj:prop:explicit-jacobian-projector` と `ifj:prop:explicit-third-normalization` の証明を混合稿へ統合。一般パラメータ h_i,t_i の下で Π+𝒟_F𝒥=1、𝒥𝒟_F=1 を全56単項式の三種類の簡約公式から導く。三次Taylorの順序を固定し、G₁∈Cでも二次座標補正が純三次項を非零にできる例 `ifj:ex:third-coordinate-artifact` を構成。SymPy 1.14を使ったローカルの厳密スクリプトで4群PASS・終了コード0（一般記号56単項式、20次元切片と36次元Jacobian方向、τ₁=2/τ₂=3・重み1/2の三次座標代入、非零三次補正）。同じ公式の再現用コード `computations/verify_hesse_slice_transfer.py` をGitHubへ保存したが、**保存後のコードそのものの独立再実行は未実施**。原点比較核・周期収縮の構成とその出力G₁,G₂,G₃、12係数の実数値は未完成。今回、全三稿の統合LuaLaTeX組版・PDF表示、外部査読、形式証明器は未実施。
- **四つの最小probeによる高次係数回収：** `ifj:prop:minimal-probes` に四方向 `E00,R0,C0,I3` の二次・三次評価行列と行列式 −1,1 を証明として記載。独立した三次不変式が四つあるため最低四方向を要し、二次PBW摂動が零なら第一または第三行が零で `I_c,I_d` も消えるため最低二方向の非線形PBW摂動を要する。四方向は双方の下限を達成する。この評価行列と零行の多項式恒等式をSymPyで厳密確認した。全12 scalarの数値・非消滅は未計算。
- **PBW・高次移送の有効範囲：** `ifj:prop:pbw-jet-degree` の全8×8 PBW積の四つの二次構造定数と `ifj:lem:pbw-hpl` の既知三次HPL式を維持。選んだ最小四probeでは積の二つは厳密一次、二つは二次、中心三次は全方向で一次。旧七probe版の `verify_clifford_jet_transfer.py` は全64積、中心性、512 triple、曲率、非可換順序の移送を6群PASSした実行記録がある。今回変更した両検算スクリプトの全体再実行、三稿のLuaLaTeX組版・PDF表示確認、実核の収縮 `(i,p,h)`・高次比較の数値化は未実施。

- **一方向rank-oneの一般因子の判別とMilnor型：** 新節 `interfactor_clifford_oneway_discriminant.tex`（ifod）の三定理・命題に、任意の許容τ_iと非零重みの四つの正確な三乗特異値、全特異点のAzumaya性、一般条件τ₁³≠−2・τ₂³≠4でのノード数1/3/3/9と通常discriminantのs次数48、特殊t³=−2/u³=4でのD₄とMilnor数16の合流を証明記載。証明は既存 `ifd:prop:ambient-locus`、`ifn:thm:four-discriminants` と射影Azumaya内のcoherent飽和を入力とする。今ターンのSymbolic検算 `python3 computations/verify_clifford_general_oneway.py` はSymPy 1.14で6群PASS（一般四binary cubic判別恒等式、二因子の臨界根と値、∂s横断性、Clifford行列式、t=3/u=2の四枝の厳密非零Hessian、特殊分岐の三次jet）。新節単体をltjsarticleの独立LuaLaTeX wrapperで4頁として組版し、未定義の外部参照を除きTeXエラー・overfull/underfullなし、全4頁のPNG montageを確認した。**三稿の統合LuaLaTeX組版や全参照の収束は今回未実施**。有限計算は圏同値・coherent飽和・全残余smooth判別・固定Hesse切片の高次12係数を検証するものではない。特殊D₄の形式同値は書いた形式Morseと有限決定性の数学的論証による。外部査読・Lean・新規性網羅確認は未実施。
- **階数一の全二方向判別・対称特別値の保持:** `ifn:thm:four-discriminants` には任意λ,μの中心norm全特異条件を四binary cubic判別式で記述する証明、`ifn:thm:symmetric-probe` にはτ₁=τ₂=2の四判別因数分解、非Azumaya二乗因子、12特異係数とAzumayaノード数を記載。これらの厳密計算6群（v67）、6群（v68）は以前の実行記録で、今回再実行ではない。今回の新一般式はv68に正確に特殊化することをSymbolic検算でも確認した。

証明の正本は混合稿の `interfactor_clifford_scale.tex`（ifm）、`interfactor_clifford_rank_one.tex`（ifd）、`interfactor_clifford_jets.tex`（ifj）と、`interfactor_clifford_versal.tex` の一般係数の系である。主担当は各証明を読み、ifm・ifd・ifjとifvの一般係数の系は執筆者以外の担当者も全文読解した。これは内部の独立読解であり、外部査読・形式証明器による確認ではない。

- **一般尺度の三乗：** `q=−adj(Hτ(z))`、`ω=−fτ(z)` と逆写像 `zₐ=adj(q)ᵦ𝚌/ω` を用いる、非零体積上の臨界スキーム同型を確認した。全許容τの有限平坦階数8のgradient写像、一般Morse臨界値の分離、第二momentの非零性を本文で証明する。AZ Morse値の検出と既存eukの全係数核から64値の集合の等号を得て、同じ `v=u²` のfull Bocksteinに属する `b₁/b₂=ℓ₁/ℓ₂` と純因子 `ℓᵢqᵢ` により両κの三乗を決定した。共通中心三次尺度は比で消しており、個々のℓの絶対値は主張しない。三枝は可換側の実ブロックスカラーのgraph核を後合成して実現する。`θ³=(τ₁³−1)/(τ₂³−1)` の非自明性は境界τ₁=1の付値1による。これを全比較核のgerbeや全降下障害の同定へ広げていない。
- **周囲正則域内のA₂：** 階数一の双方向係数における六二次式の全射影共通零点を分類し、`V(Δ)=V(h)` の必要十分性を確認した。中心正則性の係数cは全スライスで非零である。`Λ=M=−3τ E₁₁` のnorm局所式、非退化横Hessian、横臨界切断上の三次関数を用い、一般許容τのA₂型を示す。`ζ=ωₓ/Y₁` の次数一中心単元を用いて次数零の射影chartを作り、その中心と次数4 Azumaya代数を直接同定する。完備局所Mat₄表示、Tate–Shamashの極小解消、有限台の局所大域比較、有限例外mutation後に残る高次Ext、coherent飽和の反対命題まで読解した。非次数付きaffine MFの特異性だけを射影Kuへ移す推論は使わない。この例は非smoothなので、滑らかな非可換三次に関する主予想の反例ではない。
- **固定切片と十二係数：** `gl₆→(∂F)₃` の単射性と20単項式の補空間、恒等枝の形式逆写像、sourceの−PとtargetのPの区別、二捩れPicard束の[3]降下と反転の両立、比較射の文字 `ε²=ε³=1`、指定周期との整合を確認した。Heisenbergだけの5二次・10純三次から、反転も保つ核では4二次・8純三次へ減る。四つの最小一変数probeが十二値を回収し、二つの非線形PBW方向も最小であることを有限計算で確認した。十二値の数値・非消滅は未計算。自由な標的形式座標で高次項を消せることと、固定した多項式切片での値を区別する。
- **一般係数とモジュライ稠密開：** 実比較核を持つ有限型étale chartを出発点とし、射影空間束をさらにétale局所自明化してから一般有限射を縮小する。係数の非空開への有限étale全射、実三次族・実核、モジュライへのétale分類写像とその稠密開像を得る。有限化後の開が最初の分離点を含むこと、元の係数体への核の降下、全smooth係数の比較は主張しない。

一次資料では、Buchweitz–Pavlovの刊行版§§2.1,2.6、Beauvilleの *The Coble hypersurfaces* §1 Proposition1、Eisenbud–Peevaの著者版Construction4.1.3・Proposition4.1.4・Remark4.1.5、Stacks Tags02NW,03FQ,04XBの該当本文を確認した。Moore行列のHesse表示、Heisenbergのgradient機構、Tate–Shamash解消、一般有限射の縮小は既知結果として引用する。今回の具体的臨界スキーム同型・尺度較正・残余特異例・核の反転構造の網羅的な初出確認は未完了である。

### 今回実行した有限代数検算

| コマンド | 実行結果 | 確認範囲 |
| --- | --- | --- |
| `python3 computations/verify_clifford_morse_scale.py` | 8 PASS、終了コード0。主担当と別担当が実行 | Q(τ)上のadjugate恒等式、二つの完全gradient商による第二moment、τ=2の臨界多項式と8非零単根、尺度三乗・Kummer式 |
| `python3 computations/verify_clifford_rank_one.py` | 4 PASS、終了コード0。主担当と別担当二名が実行 | 全分枝の2×2行列式h、一般τのnorm特異点・局所式・横Hessian、τ=2の有理数係数例 |
| `python3 computations/verify_clifford_jets.py` | 旧七probe版は7 PASS・終了コード0。四probe改訂版の全体再実行は未実施 | 全単項式重み・巡回軌道、反転固定部分、gradient、四probe、Hesse補空間、中心三次と最上線の符号 |

旧版の有限検算器のSHA-256は資料確認時の値として保持されるが、変更した `verify_clifford_jets.py` に旧ハッシュを流用しない。今回確認したのは四probeの評価行列・零行恒等式のSymPy厳密計算であり、全スクリプトの再実行やdg核の形式証明ではない。

## Clifford族の正則性・実smooth近傍・四様体のrotation形式認識

主稿 `papers/sections/rotation_preserving_deformations.tex` と、混合稿の `interfactor_clifford_regularity.tex`, `interfactor_clifford_smoothness.tex`, `interfactor_clifford_kodaira_spencer.tex` に証明を記載した。主担当は各証明を読み、正則性・実smooth近傍・rotation形式認識は執筆者以外の独立読解でも確認した。以下は本文にある証明と内部点検の状態であり、形式証明器、外部査読、網羅的な新規性調査の完了を意味しない。

- **任意係数環の相対Koszul・CY性：** 内部次数ごとに有限なbar濾過と固定C線型縮約の有限摂動から、canonical Koszul空間の自由性・直和因子性・任意底変更を得る段階を確認した。反転双対濾過、最高成分のtrace、完全対合のannihilator公式、Nakayamaの濾過保存を区別した。実符号対合により残るshearが消えることと、双加群Koszul複体の自己双対の微分符号を確認した。非被約係数環を複素閉点検査で代用していない。有限型係数環でのenveloping algebraのnoetherian性は、主稿の多重THCR補題を四因子へ適用する証明に依存する。
- **実smooth proper近傍：** 全九変数環上の有限line模型、実際の通常coherent対角、原点の正則局所環上の高次Ext消滅、Yoneda境界の局所化による有限複体retract、両側Gorenstein双対とtorsion保存による実評価写像の構成、dg対角への輸送を独立読解した。一般のcoherent対象は局所環の次元と同じ段数のfree解消でflat syzygyへ帰着する。特殊fiberのcone・idempotentの無条件の持上げを使わない。四・五次元型の原点開を扱い、全smooth locusや開集合の補集合の方程式を計算したとはしない。
- **四様体の固定接空間：** BFKのCorollary5.41・Theorem6.5はHochschild homologyの公式として読み、rotation固定の2-CY volumeとのcap同型によってcohomologyへ移した。固有値1,ζ,ζ²の重複度20,1,1、幾何的KSの単射性、固定部分との一致を確認した。
- **通常Artinの全次数認識：** 既存22次元hull、偶数shiftの恒等共役、有限C₃作用の同変形式座標、固定部分の20次元形式円板、全Artin自然変換への形式逆写像定理という順序を確認した。固定部分スキームと不変環による商は区別する。Lurieのtame比較の(−1)-truncated性を用い、実変形からhullへのπ₀単射とπ₁比較を介して実際の圏へ戻る。持上げが存在する対象の充満な一次切断群oidを分類し、選択したrotation・周期を追加標識した高次群oidや導来Artin基底は結論に含めない。
- **実際の局所比較核：** 比較核スタックの小拡大問題で、既存のP_Aにも新しいintertwinerを要求せず、充満部分群oidの完全忠実性からその核自体を持ち上げる段階を独立読解した。有限表示とsmooth atlasから指定点を通るétale近傍を得る。Clifford原点の入力は、二捩れ因子も含む既存のrotation付き実核 `ebk:lem:boundary` である。延長核による全基底上のrotation・周期・中心標識の同時保存は主張しない。

一次資料として、Berger–Marconnet Theorem6.3・Proposition6.4、He–Van Oystaeyen–Zhang Lemmas1.1–1.2、BFK Corollary5.41・Theorem6.5、Huybrechts–Rennemo Proposition3.5・Remark3.8を照合した。Lurie DAG X Remarks5.3.9/5.1.11、Theorem5.1.9、Definition5.3.20、Proposition5.3.21とBKP §§3.3,4.3は別担当も一次本文で確認した。射影積の入力はBallard–FarmanのProposition3.41・3.42、Lemma4.9、Corollary4.12、Proposition4.14・Theorem4.15・Remark4.17に照合した。近接するLin–Zhang arXiv:2611.05915v1のTheorem2.2・Proposition2.4・Remark3.9も一次本文で確認し、通常HH²への幾何的KS全射を用いる同論文が四様体を除外することと、本稿のrotation固定形式部分との違いをIntroduction・本文・ノートへ記した。これらの一般機構自体の新規性は主張しない。

九変数のambient HH²接類の独立性と、残余KuのKS写像の単射性は別である。後者は次節の中心代入とfull Bocksteinの積によって別に証明した。ここまでの正則性・smoothness・形式認識の証明自体には新規有限計算を用いていない。一次比較のH₃同変形と二方向の尺度積は下記ife/ifvで確定した。一般二因子の尺度は上記ifmで三乗と有限三枝まで決定した。固定切片の十二高次係数の値と全smooth係数への延長は未解決である。

## Clifford四次元族の残余KSと形式的な像

正本は `papers/sections/mixed/interfactor_clifford_tangent_product.tex`。平方零中心代入の平坦性とfull class、実三次のShamash周期による中心作用の同定、定数・Clifford β Bocksteinの既存単射性、ブロックμ₃の指標、Jacobian積を用いる。主担当と執筆者以外の読解で、対象依存の全gaugeを許した等式と、関係式に加えて指定中心補正も代入することを確認した。ambient独立性を残余の単射性へ外挿していない。階数9・像Jac(f₁)₁⊗Jac(f₂)₂と、可換三次の一次変形式を得た。

原点を標識した三次の形式変形空間への閉埋込みは、余接全射から完備局所環の全射を得る。source/targetが正則なので余次元11の正則閉埋込みとなる。ブロック作用による形式Taylor次数の制限はrotation作用による22次元から20次元への認識とは別の作用である。L,QのH₃同変な射影形と尺度の較正は下記ife/ifvの結果による。高次係数の非消滅、全smooth係数の比較や大域単射性は結論していない。

Huybrechts–Rennemoの刊行版Propositions3.3/3.5/3.9、Corollary3.7、Remark3.8を一次本文で確認した。内部shiftの自然変換環の積を普通のHH²全体と混同せず、次数三の20対22を保持する。BFKの恒等sector公式と既存のperiod付き境界核を入力とする。この具体的KS計算の網羅的な新規性確認、外部査読、形式証明器は未実施である。

### 保持する残余KSの有限検算

| コマンド | 結果 | 範囲 |
| --- | --- | --- |
| `python3 computations/verify_interfactor_residual_ks.py` | 保持するv63の確認：7 PASS、終了コード0。作成担当と主担当が実行 | Hesse Jacobianの全次数三関係・20基底、(1,2)九基底、指標、Kronecker行列式、τ³=−2のFermat例 |
| `python3 computations/verify_elliptic_bockstein.py` | 保持するv63の確認：8 PASS、終了コード0。主担当が再実行 | 既存の定数BocksteinとClifford β検出を支える有限gauge・双次数恒等式 |

これら二本をv64で再実行したとはしない。残余KS検算器はQ[h,k]上で全56単項式と全36Jacobian関係倍を使い、20補基底との行列式±(1−h³)²(1−k³)²を確認する。k=0を除外せず、Fermat特殊化で文字通りの平方が零となることも厳密検出する。実比較核やfull characteristic classの恒等式を有限計算で証明したとはしない。

## 双方向十八変数族・同変一次係数・二十変数形式完全性

正本は混合稿の `interfactor_clifford_bidirectional.tex`（ifb）、`interfactor_clifford_bidirectional_geometry.tex`（ifg）、`interfactor_clifford_equivariant_ks.tex`（ife）、`interfactor_clifford_versal.tex`（ifv）。本文に完全な証明を記載し、主担当と執筆者以外の独立読解を行った。以下の証明の点検、有限恒等式の計算、組版・表示、外部保存を区別する。外部査読・形式証明器・新規性の網羅的確認は未完了である。

- **全十八係数の代数と中心商：** cross可換性だけを用いた循環交換子の消滅から平方中心性を導き、相互逆写像で二つの三次元Clifford代数の通常tensor積と同定した。六平方の多項式環上の自由階数64と全係数でのHilbert級数 `(1−t)⁻⁶` を確認した。指定中心元は `αᵢ=2aᵢ(1−τᵢ³)` を用いて正規化し、中心normの `X₁³` 係数 `c=(α₁²τ₁²+α₂²M₁₁M₂₁M₃₁)/4` を指定した。D(c)上で任意の係数加群に対するmonic多項式の単射性からwの普遍正則性を得て、Torにより商の平坦性を証明した。商の各次数は有限射影であり、大域自由性を仮定しない。
- **正確なambient正則 locus：** 二次双対を可換六二次式商の `(Z/2)²` cocycle twistとして記述した。六二次式のresultant Δは分離点で非零である。D(Δ)上でこの商は完全交叉となる。各内部次数の有限自由Koszul複体をfiberで調べ、unit minorによる局所消去から双対の次数別有限射影性・階数 `binom(6,i)`・次数6での終端を得る。次数ごとに異なる開を無限に交差する議論を使わない。逆向きはKoszul性を仮定せずbar複体の対角部分 `Torᵢ(k,k)ᵢ=(B!ᵢ)*` を用いる。Δ=0なら双対が無限次元なので大域次元は無限となり、複素fiberのAS正則性はΔ≠0と同値である。
- **相対Koszul・untwisted 6-CY：** 可換二次完全交叉のTate線型解消、cocycle twist、二次Koszul双対性を確認した。Jacobian行列式の `2⁻⁶` 倍はsocleの大域生成元で、Koszul比較の最高成分とExt⁶単射が各fiberでの非消滅を与える。完全対合とparity `(1,1)` から双対のNakayamaは六生成元上で−Idとなり、次元6の双加群自己双対の符号と相殺する。有限射影Koszul空間とtraceを用いる解消は局所基底によらず貼り合い、各内部次数でsplit exactである。従って非平坦・非被約な任意底変更後にも正確性とuntwisted相対6-CY性を保持する。複素fiberのAS次元・indexはともに6である。
- **実残余圏と十八方向：** D(c)∩D(Δ)の分離点近傍で、有限射影入力、noetherian包絡代数、通常coherent対角、正則局所環上の有限解消とExt局所化を用いて、四・五次元型の実残余圏のsmooth proper近傍を構成した。実rotation graph・随伴・unit/counitを用い、指定原点核を延長するétale局所perfect核を得る。四様体のKS像は二つの混合部分 `(1,2)⊕(2,1)` の18次元で、標識した幾何的20次元形式変形空間への余次元2の正則閉埋込みとなる。ambientのD(Δ)を残余の全smooth locusと同一視せず、全係数での比較核や全標識の保存を主張しない。
- **H₃同変な一次係数：** Picard補正の三分根による線型化、実rotation intertwinerの指標を三捩れ平行移動で消す操作、周期の三乗根同期を確認した。こうして選んだ実核に対しSchurの補題から `Lᵢ(eₐ)=ℓᵢXₐ`、`Qᵢ(xₐ²)=qᵢ[Xₐ₊₁Xₐ₊₂]`、`ℓᵢqᵢ≠0` を得る。τ³=−2のFermatの場合もcross二次式は基底であり、中心作用を文字通りの可換平方と同一視していない。
- **動く二因子と尺度：** τ₁,τ₂を滑らかなClifford開上で動かす。二捩れ点を許す既存の相対因子境界定理に、明示Clifford表示からの一因子商の普遍平坦性を入力した。相対Poincaré束の比、有限MF外積と全次数格子、実二重同変化により、同じ原点核・H₃構造・周期を延長する。二捩れを除外する別の定理を流用していない。標準方程式 `fτ=τΣZᵢ³−(2+τ³)Z₁Z₂Z₃` に対する純τ接類は `2aᵢ(1−τᵢ³)/τᵢ [Z₁Z₂Z₃]` で非零である。同因子への平方零中心代入がτ→τ−εを与えること、固定Ωと正規化したΩの一次比がblock重みの自明な変化であることを確認し、`ℓᵢqᵢ=2aᵢ(τᵢ³−1)/(3τᵢ)` を得た。二方向の混合尺度の積はこの二値の積であり、同じτ・同じ重み・交換同変な核では元の関係式の尺度 `κ=2a(τ³−1)/(3τ)` まで決まる。一般二因子の比は上記ifmの三次Kummer被覆で記述した。
- **二十変数の形式完全性：** 18混合類と二つの純τ類がJac(F)₃の全20次元を張る。同じ実比較からの通常Artin自然変換に形式逆写像定理を適用し、各分離点の完備化を標識した可換三次四様体の形式変形空間と同型にした。実代数族のsmooth cubic四様体DMモジュライスタックへの写像は原点近傍でétaleである。これは全22次元の非標識圏変形、導来Artin基底、全intrinsic対象、全smooth係数、大域粗モジュライ空間の同型を意味しない。

Cassidy–VancliffのTheorem4.2と証明、および2014年corrigendumのProposition10・Corollary11を一次資料で確認した。normalizingな二次系の有限商条件を用い、点だけでなくfat pointも必要とする訂正を保持する。相対・任意底変更の議論は本文の有限射影解消で証明し、複素閉点上の既知定理だけから非被約底へ外挿していない。CY符号は既存のBerger–Marconnet、He–Van Oystaeyen–Zhangの一次入力とも照合した。

追加の一次比較として、Hu–Mori arXiv:2302.04446v3のTheorem3.21・Corollary3.22・Theorem3.28と、通常Clifford型のCY偶奇を述べるCorollary3.13を確認した。本稿の双対cocycleによる符号相殺を通常の六次元Cliffordへ流用しない。Kuznetsovの既存書誌§4 Lemma4.2・Theorem4.3とquadric fiberのrank≥3の仮定、Baumann–Belmans–van Garderen arXiv:2410.07620v1のTheoremA・§6 Proposition50・§6.1の対象範囲も一次本文と照合した。この限定した調査では本二十変数族と直接同じ定理は見つからなかったが、網羅的新規性を確認したとはしない。

反例 `τ₁=τ₂=2, Λ=M=I` では六二次式が `(1,…,1)` に共通零点を持つためΔ=0であり、ambientの大域次元は無限となる。一方 `a₁=a₂=1` ならc=196で、中心商は平坦である。全係数でのHilbert級数・中心正則性とAS正則性を区別する具体例として保持する。

### 双方向Clifford族の有限検算

`computations/verify_bidirectional_clifford.py` は元の15関係と双対21関係の直交・unit minor、cocycleと中心parity、trace・Nakayama符号、原点の完全交叉に用いる有限恒等式とJacobian、monic係数c、上記反例、H₃作用を扱う。純τ接類・Euler恒等式と中心規格化の一次比を含む最終検算器について、作成担当と主担当がそれぞれ **9 PASS・終了コード0** を確認した。全て有理式・多項式および三乗根の円分環上の厳密計算であり、浮動小数点やランダム標本は用いていない。検算器のSHA-256は `d8d330311ff91ace1f6b9f739a1facb6d79d5cbb8d5f5959496103c4bf2e552d`。有限検算は全係数の相対解消、実比較核、全coherence、形式完全性の形式証明を代替しない。

## 因子間PBW分解・中心障害・Clifford混合族の確認範囲

正本は `interfactor_deformations.tex` と三つの入力節 `interfactor_pbw.tex`, `interfactor_hochschild.tex`, `interfactor_clifford_family.tex`。本文に完全な証明を記載し、主担当と執筆者以外の独立読解で確認した。外部査読、形式証明器、新規性の網羅的確認は未実施である。

- **有限PBW分解：** Der₋₁=0とZ₁=0の有限C線型単射、PBW自由基底によるI-adic係数抽出、I/I²の異なる因子別次数によるcross一次消滅、内部他因子出力の消滅、I²/I³によるcross定数消滅、各因子自身のPBW性を全文読解した。任意可換係数環と非被約底変更、Koszul性を要しない一般二次代数への系も確認した。
- **比較の適用：** 指定中心三次の存在を別途仮定し、因子分解→emc/mcp全中心正規形→複素係数でmcb smooth判定→一般中央flag→全coherent/perfect核という適用鎖を独立読解した。m=1への任意係数環版はmcpの証明を一変数へ適用することを明記した。X_polと逐次実標的を同一視していない。
- **一次中心障害：** 有限Koszul双加群解消のKünneth、負次数cocycle自体の純因子性と全gauge、勾配正則列によるHH¹₀=C Euler、全HH²₀=P⊕E⊕C、任意混合三次補正を許した中心障害を読解した。Euler像のordered(3,0)成分と追加(1,2)成分を区別し、dim C=9|I₂|(k−1)とker ob=(pure kernel)⊕Cを確認した。両Cliffordの二因子の十八方向は上記ifb/ifgで積分した。一般の複数ordered pairを含む全混合核の同時積分は主張していない。
- **九変数族：** 普遍定数PBW係数のClifford中心平方への代入、非可換因子との中心balanced tensor積、第一因子だけの次数濾過、中心初項の左右正則性、主idealのstrict性、商の斉次自由基底と任意底変更を全文読解した。全Koszul cochainのbidegree(−2,2)でC¹=0、cocycle=Hom(R₁,Z(S₂)₂)を確認し、全次数零gaugeに対する九接類の独立性を得た。AS正則性・CY性と原点近傍のsmoothness・Ku比較は上節の証明による。
- **一次文献：** Walton–Witherspoon, J. Algebra504(2018),536–567 の著者稿Hypothesis2.6、Proposition6.2、Problem7.2を確認した。定数scalar混合補正の消滅は近接既知結果、Clifford追加方向は非中心群元値であり本稿と異なる。Witherspoonの書籍Theorem3.1.2の有限生成自由双加群解消という仮定、BGのLemma3.3と§§3.6,4.3も一次資料で確認した。中心への係数代入は通常の構成原理であり、その原理自体を新規成果とはしない。

### 保持する因子間関係の厳密検算

Python3.12.14、SymPy1.14.0で、執筆担当と主担当が次の二実行をそれぞれ確認した。

| コマンド | 結果 | 固定因子 |
| --- | --- | --- |
| `python3 computations/verify_interfactor_pbw.py` | 6 PASS、終了コード0 | S(1,−1,−1)の二因子 |
| `python3 computations/verify_interfactor_pbw.py --clifford` | 6 PASS、終了コード0 | S(1,1,2)の二因子 |

二次関係36×15行列のrank15、三次overlapの216×180行列のrank160から20 syzygyを再構成した。全90一次補正の420×90 BG行列はrank78で、核は二つのSym₃（12次元）、禁止される72係数は全て零。平行移動gaugeのrankは6。全15定数補正の120×15行列はrank9で、核は純因子の6定数だけである。残余BG恒等式は全12一次・6定数パラメータの係数積として厳密に確認した。浮動小数点・補間・ランダム標本は使っていない。

検算器のSHA-256は `e7efd5b042ec9965362c66587d0db80623502a638c32aa80c7c3cb7ef253aef9`。これは二つの固定入力についての有限行列証明書である。一般因子の因子分解、中心三次持上げ、Clifford九変数族の全次数自由性、Ku同値の形式証明ではない。全次数PBWの解釈には既知のKoszul性とBG定理を別途用いる。

## 多中心の全smooth locus・中央flag・横断判別の確認範囲

正本は `multicentral_comparison.tex` と八つの入力節。従来の正規形・pencil・逐次比較・二重制限に、`multicentral_transverse_bockstein.tex`, `multicentral_transverse_discriminant.tex`, `multicentral_blowup.tex`, `multicentral_bertini.tex` を統合した。本文に証明を記載し、主担当と執筆担当以外の読解を分けて確認した。外部査読、形式証明器、新規性の網羅的確認は未実施である。

- 多中心PBW正規形は、普遍環でh=1としてからの係数代入、非被約Rへの底変更、I-adic低中心分類、active初項による自由基底、wを含む全順序正則性を主担当と別担当が全文読解した。
- 中央pencilは固定tの判別超曲面の特異点判定まで照合し、値評価・cの一次jetによる余次元二incidence、P¹のproper射影、ノルム局所因子によるtotal spaceのsmoothnessを独立読解した。
- 逐次核は、実cotwistからのrotation移送、固定C点での三乗根同期、一般M≥6の両隣接sector、固定境界を全横断係数へ移した実参照族差・三項κ′≠0・coKleisli・smooth飽和を主担当と二人の別担当が全文読解した。未完成の二中心balancing towerは入力に使わない。中央座標を選ぶ一次式はC係数非零と明記した。
- 二重制限は、負例外列によるO(−1)だけの補正、canonical右mate、共同comonadへの全構造移送、指定MFの混合積、同一smooth二軸と異なるtotal smoothnessの反例を主担当と別担当が全文読解した。bare交換射から高次構造が一意とは主張しない。

- 横断二項の全階数は、ε=v²の平坦族、実自己交叉・Lowen full cochain、αのarity0評価、中心一次式のunary Bockstein、全対象primitiveの双次数消滅、実二列法線解消を主担当と別担当が全文読解した。任意q中心の境界への追加も主担当が読解し、既に存在するperiod同期済み実核を入力とすることを確認した。
- 横断判別は、最高次gradientによる有限平坦性、標数零の一般étale性、臨界値差の微分、最小多項式の冪指数一、有限双有理正規化と局所Nakayama、各悪値の一節点性を主担当と別担当が全文読解した。一般mの差分も確認した。特殊二次係数の多重根を排除していない。
- 実blow-upは、strict graded中心作用、qgr商との適合、free–forgetful随伴とKoszul Homによるchart同定、Khanの実随伴・projection三角のtensor、SOD順序、gluing、各chartへの普遍核の底変更を主担当と別担当が全文読解した。
- 全smooth locusと中央旗は、絶対対角の底対角支持と有限Čechのmappingによるcompactness局所性、R-proper gluingの絶対perfect化、可換blow-up chart、基点での∂Gとdu_i、普遍incidenceとgeneric smoothnessを主担当と別担当が全文読解した。j_*がperfectを保つという仮定、比較核の全chartへの貼合せ、一般dg Bertiniは用いていない。

一次資料はTevelev arXiv:math/0112028v1 §7.1 Example7.4、Rennemo–Segal–Van den Bergh arXiv:1705.01366v2 Proposition2.1とIntroduction、Beck Distributive Laws §3 Proposition・証明（TAC再版104–106頁）を確認した。双対次数と随伴形式論を新規結果として扱わず、Bertiniの有限中心仮定を一般PBWへ流用しない。

追加の近接文献として、LBSV Theorem3.2.6のType A、Cassidy–Shelton Theorems1.3,1.5と証明、Gaddis Propositions2.7,5.1、Perry Remark4.23/Lemma7.18/Proposition7.19、Jiang–Leung arXiv:1811.05132v2 §1.5/Definition3.2/Theorems3.3,4.5を一次本文で確認し、既知の正則拡大・tensor積・HPD・幾何的圏のblow-upと本結果の違いをIntroductionと研究ノートへ統合した。sourceの実blow-up、全smooth locus、一般中央flagを本文の証明へ進めた。新たな一次入力はKhan Theorem C/Proposition4.2/Theorem4.3/§4.4、Lunts Propositions3.11/3.13とLemma3.15、Antieau–Gepner Lemma6.4とTheorem6.11の証明（1222–1223頁）。主担当も一次本文を確認した。Lowen Theorems3.21/4.15と証明も再照合した。既知の一般機構の新規性は主張せず、適用対象は固定因子・因子間可換のPBW・中心三次族に限定する。

全係数の勾配resultantは、零集合の判定・非零性・中心座標の拡大による重み付き次数・独立変数ブロックの分離公式を主担当と別担当が確認した。Busé–Jouanolou arXiv:1210.4697v1 Propositions2.4/4.13を主担当も一次本文で読み、公刊書誌を著者の公開リストと所属機関の書誌で照合した。全係数判別の既約性・被約性や係数展開は主張しない。

### 厳密計算

| 検算器 | 実行結果 | 確認範囲 |
| --- | --- | --- |
| `verify_multicentral_pbw.py` | 4 PASS、終了コード0 | 中心形式による平行移動、Clifford一次障害、既存普遍中心証明書の代入、uv偏極。執筆担当と主担当が実行。 |
| `verify_multicentral_pencil.py` | 6 PASS、終了コード0 | 六変数Fermat例の64臨界値と192方向、Hessian、平方因子なし、一次jet、斉次次数。主担当と別担当が実行。 |
| `verify_two_center_restrictions.py` | 6 PASS、終了コード0 | 独立な4×4行列の曲率・閉元・混合二項・homotopy・三項偏極、同軸反例。執筆担当・別担当・主担当が実行。 |

有限恒等式の検算と、全係数核・高次coherence・一般係数の証明を区別する。

### 現行ソース・組版・表示

主稿・混合稿はv65、モジュライ稿の本文はv50を保持する。上記の新結果を本文・要約・研究方針へ統合した。`python3 scripts/check_sources.py` は137 TeXファイル・2144一意ラベルで成功した（主稿34/491、モジュライ稿45/874、混合稿62/779）。入力・他稿参照・引用・author欄・rootを検査した。

三稿をLuaLaTeX・latexmkで組版し、相互参照は二巡で安定した。表示確認に基づく文章の微調整後、混合稿・主稿をこの順に再組版し、いずれも終了コード0を確認した。最終PDFは主稿191頁、モジュライ稿457頁、混合稿346頁である。最終ログで未解決参照・未解決引用・再実行要求・重複ラベル・欠字・overfull/underfull boxはいずれも0件、全PDFの抽出本文に`??`は0件である。書体代替・旧書体命令等の既存警告は主稿9件、モジュライ稿1件、混合稿10件を保持する。

最終調整で変わったラベルの頁番号は混合稿の命題`cmo:prop:equivariant-window-hom`の一箇所のみである。この命題を外部参照する主稿は混合稿の後に再組版し、モジュライ稿にその参照はない。主稿・モジュライ稿の自前ラベルは調整前後で一致した。主要Markdown五文書のローカル参照先228件も確認し、欠落は0件であった。

PNGによる表示確認は計39頁に対して行った。混合稿273–296頁の新結果部分を執筆担当以外でも確認し、表紙・目次・参考文献、主稿の要約・結果一覧・該当参照箇所、モジュライ稿の参考文献も標本確認した。短い文末だけが送られる箇所を修正後、混合稿293–296頁と主稿1–2頁を再度画像で確認した。確認した頁には数式・本文の重なり、裁ち落とし、欠字、未解決参照の表示は見つからなかった。全994頁を一頁ずつ画像で確認したとはしない。

PDF・キャッシュ・中間生成物はGitで追跡しない。既存の保持する検算器を全て再実行したとはしない。今回の独立読解は本作業内での確認であり、外部査読や形式証明器による検証ではない。

## 任意固定楕円因子の全係数比較の確認範囲

対象は `elliptic_mixed_comparison.tex`, `elliptic_boundary_kernel.tex`, `elliptic_bockstein.tex`, `elliptic_universal_kernel.tex` と、中心障害節に統合した普遍Clifford中心である。執筆と独立読解、有限検算、組版・表示、保存を別々に扱う。新規性の網羅的確認、外部査読、形式証明器による検証は未完了である。

### 証明と一次資料

- 普遍Clifford中心R⊕Rv、v²=−det q、全α特殊化、全中心三次liftのβ三方向＋cu³を執筆担当以外も独立読解した。PBW基底の1/xyz係数による分母消去と、全αで非零のdet最高項を確認した。
- 任意固定因子の境界核ではPicard補正・指定三乗周期・全次数格子・双対群法則を確認した。元の同変MF上の厳密dg character作用を持つ双加群圏へElagin Lemma8.6を適用する。導来作用一般のdg liftを同補題だけから得る議論ではない。
- 全許容表示の被覆は、純ブロックu一次障害と低次数中心による。相対potential双加群解消、共有中心差一回、untwisted双対、有限line-modelと生成性を独立読解した。一般PI性・有限中心性や特異fiber全coherentのproper性を仮定していない。
- 定数Bocksteinの剰余体評価は独立なrelation dualに入り、Shamash周期torsionがないことからTate後も非零となる。一次Pは独立左右gaugeの対称部分、Clifford βはrelative Yoneda m₂と交代m₃により検出する。任意対象依存primitive・全Tate逆冪を許し、通常Extからの移送とfull cochainの橋を本文に記す。
- 任意smooth cubic Gの両隣接sector消滅、実可換参照族、全Tの差・重み・可縮path、全comonadからcoKleisli/graph核、smooth開のperfect性とcoherent飽和を独立読解した。既存判別定理の導入を、その証明が使う任意smooth G・多項式的Qという一般性へ揃えた。

Reich–Walton Theorem7.1(a)と公刊書誌、Lu–Palmieri–Wu–Zhang TheoremA/CorollaryB/§5と公刊書誌、Elagin Lemma8.6/Theorems8.7,8.9、Berger–Taillefer Theorem3.6/Lemma3.7の自己双対解消、Mori–Smith Corollary2.9を一次資料で確認した。LPWZは体上のbaseline m₃に用い、非被約係数環のYoneda m₂は相対barから別に証明した。

### 保持する厳密計算

| 検算器 | 実行結果 | 確認範囲 |
| --- | --- | --- |
| `verify_elliptic_center_obstruction.py` | 7 PASS、終了コード0 | 従来の中心障害に加え、普遍Clifford体積元の平方、Ωとの尺度、det qの非零最高項を記号的に確認。 |
| `verify_elliptic_bockstein.py` | 8 PASS、終了コード0 | 一般dual積・独立左右gaugeと平行移動、非二捩れdet、Clifford binary det=8、全Tate双次数、対象依存m₃挿入の交代性。 |

両検算器は主担当でも再実行した。有限記号恒等式の証明書であり、実境界核・full cochain移送・全coherence・Morita同値の形式証明ではない。

## 保持する尺度・七定数形・中心障害の確認範囲

対象は混合稿の `multiblock_scale.tex`, `linear_equivariant_coefficients.tex`, `linear_discriminant_geometry.tex`, `elliptic_center_obstruction.tex`。各節は既に執筆担当以外でも全文読解し、下記の仮定・依存と論理を確認した。外部査読、全既存本文の再監査、形式証明器による確認、網羅的な新規性調査とは異なる。

### 証明と一次資料の読解

- **全kの尺度。** 一因子の正則中心上の八Morse点を外積して、任意kでMat_(6^k)(通常二重点)と自己Ext級数(1+s)^(3k)/(1−s²)を得る。有限中心台上のchart Ext比較と既存のcoherent飽和判定から残余線束圏の非smoothnessを導く。一因子の中心Morse多項式と可換Jacobi多項式の一致はkブロック比較に依存しない。全係数の実Morita比較を先に用い、λΣ⊂κ_k⁻¹Σ、両辺8^k点、非零二次momentからκ_k²=27/28を得る。全非Azumaya局所型の分類や、比較核の因子追加互換性を仮定しない。
- **七定数形。** 同変境界比較と標準Jac₂切断を固定し、実参照族との差と可縮pathの自然性からQ,L,Cの同変性を得る。非線型A∞構造を平均しない。独立なHeisenberg中心文字が異ブロック項を全て排除し、四つのHom空間の次元は1,2,1,2となる。単射Bocksteinの像は純ブロックJac₂の直和であり、χ_k≠0。κ以外の六定数は未算出。53/54は非可換中心係数の可換化に過ぎず、χ_kとの同定には使わない。
- **固定pの判別幾何。** 任意固定Qで有限平坦gradient写像の次数はμ=8^k。有限étale開の相異臨界点対上でdh=Σ(x−y)dℓを使い、臨界値を分離する。臨界代数が整で、norm多項式が一般点で分離的であることから最小多項式の指数が1となり、全係数・各固定pの判別式は既約被約となる。有限双有理な臨界graphが正規化である。唯一のMorse前像から局所同型を得る逆向きは、余接全射と二段のNakayamaで確認した。全体の被約性から固定(p,α)の一変数特殊化の被約性を推論しない。
- **全滑らか標準Sklyaninの中心持上げ。** Clifford S(1,1,τ)ではτ≠0,τ³≠1,−8の下で実楕円・非零二捩れ・指定中心正則元を確認した。BG条件はM対称、平行移動の正規形はp_x=m11−τm23等である。全二次補正を消す三汎関数が−3τ(p_z,p_x,p_y)を検出し、liftはp=0に限る。p=0では中心平方とodd Clifford volumeが全定数補正で十分性を与える。非二捩れではTHCRの中心sectionからσ^d=idが必要となり、Hesseのflexの位置からZ₁=Z₂=0,Z₃=CΩを得る。EGの各固定係数での中心存在を適用し、固定した単射adの左逆で普遍多項式liftを作る。PBWやCYだけを指定三次の持上げへ置き換えない。

一次資料は Etingof–Ginzburg 公刊版Theorem3.3.2と§8.3（全固定CY leadingに対する非スカラー中心≤3、generic限定のTheorem3.4.5とは区別）、§9のRains公式のq+1退化、De Laet–Le Bruyn arXiv:1405.1158v1 §§1–2（中心商とp.3の3c₃公式）、Mori–Smith Corollary2.9を照合した。Maxim–Tibăr arXiv:2307.04032v3 Theorem2.5とそのgraph埋込みによる証明、Tevelev arXiv:math/0112028v1 §1.2 Theorem1.7・§1.3.Bを確認し、書誌を追加した。線形morsification、双対性、Heisenberg表現論、PBW・CY性自体を本研究の新規成果とは扱わない。新しい適用・明示障害の初出確認は未完了である。

### 保持する有限証明書

| 検算器 | 実行結果 | 確認範囲 |
| --- | --- | --- |
| `verify_mixed_multiblock.py` | 9 PASS、終了コード0 | 普遍8×8臨界代数、二次moment、tensor和、Morse seed、全kのsector不等式。新たに中心Q₁と可換h₁のλ²=28/27での一致を検算。中心消去全体の再実行ではない。 |
| `verify_mixed_equivariant_coefficients.py` | 10 PASS、終了コード0 | 関係式からのsource→target群作用、中心元の厳密同変性、標準Jac₂切断、Hom次元1,2,1,2、全kの台、重みa_i、53/54留保。 |
| `verify_elliptic_center_obstruction.py` | 7 PASS、終了コード0 | Hesse条件・BG重なり・平行移動、Q(τ)上の自由語による一次障害と全二次補正の消去、Clifford体積元、有理τ=2の全低次補正系rank8/拡大rank9、二次中心7x²+4x。 |

上記は各検算器の確認済み範囲である。中心障害の7 PASSを含め、これらは保持する既存の確認結果であり、v60の変更で再実行したとはしない。無限個のkや係数への外挿を有限標本で代用せず、記号的な恒等式・中心文字の台と本文の証明を併用する。全coherence、一般中心持上げ、Morita同値そのものを形式証明したという意味ではない。


## 保持する全線形PBW比較とBocksteinの入力

以下は既存の証明・有限証明書の点検範囲であり、今回新たに全文再監査・再実行したとの主張ではない。判別幾何は上記の任意固定pに対する結果へ強化されている。

### 保持する full Bockstein と非分裂比較の読解

自己交叉の二拡張を正規化barの乗法cocycleと同定する橋渡し、Lowenのfull brace mapと対象ごとのobstructionの区別、相対Koszul–Shamash模型のunary微分、中央自然変換tによるderived localization、対象ごとに独立なhomotopyのarity one検出を読解した。Tate逆冪を許す双次数と、他ブロックの成分を除く射影も確認した。通常Extのcohomology algebraだけからの移送や、objectwise vanishingから自然変換の零性を結論する議論ではない。

非分裂K_ηの比較では、長完全列の両隣接群を含めたBFK sector計算、全ηの係数上の自然な自由加群同定、固定counitのWillumsgaard towerの適用を確認した。実可換族を各段の参照点とする順序、二項を同定した後のpath空間の可縮性、重み1,2,3から得る三角多項式変換を独立読解した。Bockstein単射性は存在比較の前提ではない。

周囲代数の相対potential解消、共有u差を一度だけ加えるchange of rings、untwisted双対、proper線束模型と周期による生成、coKleisli積、可換smooth開でのperfect核とcoherent飽和を確認した。主稿のcrsの入力に有限中心・PIがないことも確認した。普遍臨界代数のfiltered Koszulによる自由性、Euler恒等式、determinantの重複度、定数型Morse seedから一般(p,α)の非空開へ進む議論を確認した。

既存の二節は執筆担当以外でも全文を読解した。一次資料としてLowen Theorems3.21,4.8,4.15と4.15の証明、Berger–Taillefer Theorem3.6/Lemma3.7と自己双対解消の証明、BCL Theorem5.3/Corollary5.16を確認し、引用・書誌へ反映した。BCLの普遍性とcentral localizationのcohomology計算は区別して使用する。Etingof–Ginzburg §3.5/Theorem3.6.2(i)の一因子斉次比較と、Anno–Arkhipov–Logvinenko arXiv:2303.11826v2 Theorems6.1,8.4の全comonad・条件付きcoKleisli復元を原著で確認し、当該具体的適用との関係をIntroductionへ記した。BFK Theorem5.39、Willumsgaard Theorem3.3/Lemma3.11、BG条件、既存中心恒等式と定数型比較は、前提となる既存確認範囲を保持する。全既存本文の再監査、網羅的新規性確認、外部査読、形式証明器での確認ではない。

### 保持する Bockstein の厳密計算

`python3 computations/verify_mixed_linear_bockstein.py`：**6 PASS**。元の三つの二次関係からdual積を導出。独立な左右primitiveの9×6 gauge行列の階数6、対称対角外の3列を加えた9×9行列の行列式−64、対称gaugeとの交わりが対角3次元であることを有理数上で確認した。双次数(1,−1)のprimitiveはtの負冪を許してもF₁t⁰のみとなる。非負変数k=2+K,r=2+R,i=Iを使い、非分裂towerの三群の非恒等sectorが全k・全arityで消えることと、恒等sectorが二項Jac₁・三項Jac₀だけになることを記号的に確認した。

`verify_mixed_linear_pbw.py` の6 PASSと普遍中心関係行列162×339/rank144は保持する入力で、今回再実行した結果とは数えない。多ブロック検算器の9 PASSは保持する確認済み入力である。全次数PBWはBG条件と定理、full Bockstein・全coherence・実Morita比較は本文の証明に依存する。


## 保持する全中心係数の実核と普遍定数補正

主結果は混合稿の `cmo:thm:all-central-commutative-kernel` である。指定係数 α¹=(1,4,9), α²=(16,25,49)、重み1,100、固定 h=1 に対し、全 c の残余線束圏を V(λ(G−u²L)+cu³)、λ²=28/27、の残余線束圏と実際にMorita比較する。U=A¹∖V(P64)上で同じ双加群は相対perfectであり、各ファイバーで全coherent Ku同値を与える。定常normの全64根も含む。普遍係数環上の構成から、同じ固定二ブロックの任意の定数補正αについても、可換方程式が滑らかな開上の相対perfect核を得る。全標識の同時保存、Q降下、交換子h族の選択済み一般点核との相対整合性、他の混合表示や全intrinsic対象は結論しない。

### 全中心係数の証明の読解

- **普遍模型と中心一次元制限：** 全係数環T=C[α₁,…,α₆,c]上でactive PBW濾過と中心元の正則初項から次数別有限自由性を確認した。七線束と四つのmutationのproper模型、制限と左右随伴を全T上で構成する。特異ファイバーでも境界線束の二項解消がinflationを線束圏に送る。cotwist C=ρ_A⁻¹[1]、twist T_F=ρ_S²、C³=[1]、T_F³=[4]、H=C[−1]のH³=[−2]を実随伴射とmutationで確認した。properなHomの有界性で生成性を証明し、特異係数の全coherent圏のproper性を仮定しない。
- **二項・三項と全coherence：** A/(u²)=S[u]/u²から一次Bocksteinは零、指定counitはK=1⊕J、J=ρ_S²[−1]に一意に分裂する。正規化towerの非空fiberのπ_iはH^(2−n−i)RHom(K,Jⁿ)。BFKの恒等・非恒等sectorを計算し、二項の選択がJac(G)₁≅C⁶、三項がC、四項以降と全高次homotopyが零であることを独立に照合した。三項・四項の存在障害群自体は残る。実際に存在する全構造のA₃比較を延長する論理と、任意のA₃が延長するという主張を区別した。
- **実パラメータと多項式性：** 固定境界のmapping complexをTへ底変更し、低arityのクラスを大域的な有限自由T加群の切断として取る。点ごとに選ぶminimal modelや分母を使わない。厳密な二列法線解消D²=0、閉作用素ξのξ²=Θにより二項をv-Bocksteinへ同定した。法線符号反転の三項torsor上の唯一の固定点を原点にし、wt α=2, wt c=3によって三項は定数倍のcに限られる。中央一変数のrank一MFの三項積±cと、smooth/non-smoothファイバーによる独立な倍率の非零性を確認した。
- **全係数の実核と尺度：** Heisenberg作用・block交換から二項は共通scalar倍のL、三項は非零scalar倍のcとなる。Jの再尺度で二項を合わせ、まず未知κのG−u²L+κcu³への全T上のcomonad比較・coKleisli代数・graph双加群を構成する。全cの残余線束圏のsmoothness集合が一致することを使ってから、P64根集合の非零二次冪和でκλ=±1を決める。両smooth開だけで判別集合が一致すると推論していない。
- **相対perfect性と全α：** T上のproper性と周期により相対生成性も成立する。coKleisli比較と単位・余単位は全T上で構成し、可換smooth locus上で相対smoothnessとgraphのperfect性を得る。全coherentとの一致には各複素ファイバーで主稿 `crs:thm:coherent` のnoetherian Koszul AS正則ambient・正則中心三次・有限sectionの仮定を確認した。任意導来底変更で保たれるPerf比較を、非正則基底の全Db(coh)へ広げてはいない。
- **中心方向と反例：** (Jac F)₃⁻≅(Jac g)₂、[u³]↦[∂_eG|ker L]を証明し、cotwist射vの像をrank一Knörrer核の実homotopyで確認した。指定中心方向の非零性には6×6有理行列式の証明書もある。norm全64根に実核が得られたため、被約point/Poisson不一致は実際の可換Ku標的を持つ例として成立する。不一致定理の全Poisson正規形への依存は変わらない。

既存の四つの数学節とその依存を執筆担当以外の複数担当が独立に読解した。全cのline圏とsmoothファイバーの全coherent圏、存在障害と比較の一意性、尺度の論理順序、相対底変更、全αへの仮定を重点確認した。これは外部査読、形式証明器による確認、既存全本文の包括的再監査ではない。

### 保持する固定零係数とh族の読解

- **実二成分分解と球面周期：** 中心二重根のorderによる全coherent分解、実inflation/tensor/mutation核、gluing=RHom(F,L M)[−1]を保持する。実余単位三角と二本のright mutationからT_L=ρ_S、T_L³=[2]、C_L³=[−1]を確認した。proper性と有限回の三角からLのconservativity、L像とLᴿ像のsplit生成を証明した。Verdier商のproper性やInd上のconservativityは仮定しない。
- **高次comonadの一意性：** K=Cone(id→ρ)[−1]、J=ρ[−1]について、全n≥2,q≤0でH^q RHom(K,Jⁿ)=0をdiagonal MFの恒等・二つの非恒等sectorから確認した。opposite monoidal stable圏のInd完備化に、unitを固定したA_n構造のtowerを適用する。各非空fiberはΩ∞RHom(K,Jⁿ)[2−n]で可縮、既存の構造によりtowerは非空であり、全高次構造が一意となる。単純なchain-level splittingや一般的な「twistだけから復元」を仮定しない。このtowerとshiftは執筆以外の担当でも一次資料を照合した。
- **BocksteinとHeisenberg比較：** 自由解消の持上げの二乗をvで割ったoperatorを実twist射と同定した。最小Shamash解消のExtは周期tについてF⊗C[t]として自由であり、六つの二次双対の平方の独立性からパラメータ写像は単射。可換境界のJac(G)₁が六次元なので同型となる。Picard補正をE[3]で線型化し、rotation intertwinerのcharacterをWeil pairingで消去する。両因子を同じ選択にすることでSchurの二scalarが一致し、重み100へ戻してνをLに共通scalarまで同定する。最後にtwist比較をrescaleするので全周期標識の保存は要求しない。
- **実核の構成：** 境界生成子Gの右随伴像が源を生成し、End(LᴿG)はRHom(KG,G)のcoKleisli積で記述される。全coherenceを保つcomonad比較からgraph双加群を作り、smooth proper性からperfect核P_Rと実制限intertwinerを得る。既存の可換rank一Knörrer核、二成分の貼合せ、χ=Serre³[−7]と二乗coherenceの平方根補正、平均冪等元と二重crossed productを合成し、通常五様体の同値を構成する。単一の全係数行列を列挙したという意味ではない。
- **固定値での有限行列分解：** 非斉次Koszul双対E=F⊗Λε、dε=−Σαξ²から長さ七の解消を作り、中心wに対する高次homotopyを有限境界持上げで構成する。rank64+64のMFを定数微分の縮約でrank40+40へ移し、d₈₀²=w、二つのchain map、PI=1、IP=1−dH−Hdを確認した。三つの内部shiftがK_Rを生成し、v=0で実制限が得られる。これは総階数80のMFであって80次元A∞自己準同型代数の完成や直接Knörrer消去ではない。Fの積を固定したstrict Clifford ansatzは二次関係と両立しない。
- **非PI族の相対perfect対角：** R₀₁=C[h]を0,1で半局所化した環上で、次数別自由性、noetherian性、相対Koszul解消、七線束のproper模型と底変更を確認した。bigraded射影積上の通常coherent対角を用いる。torsionのTor遷移の消滅、有限cohomological dimension、coherent Extの有限性と底変更を証明し、特殊ファイバーのcompact性からExt有限性・Nakayama・有限line解消によるretractを通じて相対compact性を持ち上げる。一般のfiberwise smoothからの形式的推論や有限中心性の一般点への流用はしない。
- **整核と対合指標：** 選択済みgeneric核をcoherentなbigraded複体へ戻し、R-flat格子と上のcompact持上げからperfect整核を得る。有限拡大の整数閉包の有限flat性と、その局所DVRの有限性は区別した。特殊化のunit/counit defect零は未証明で、固定値の別構成の存在だけでは保証しない。相対smooth proper模型にMathew Theorem1.3を適用し、連結性と対合冪等元からHH±₁の正負固有次元(5,16)、HH₀の(2,0)を無条件に得た。
- **保持する形式・一般点比較：** 普遍PBWの平坦性、曲率付きbar flowと逆flow、Heisenberg不変空間・blocktensor性・楕円中心商による指定potentialの全形式次数同定を入力とする。七変数MFをu=0へ非平坦に底変更する論法は使わない。固定三対象と一般点への降下は保持し、形式h級数をh=1に代入しない。

新規証明は執筆以外の担当による読解も行った。相対compact持上げと射影積、球面復元のsector・tower・graph、Bockstein・Heisenberg選択を別担当で照合した。これは外部査読、形式証明器による確認、文献上の新規性の網羅的確認ではない。

### 一次資料の確認箇所

| 一次資料 | 確認箇所と使用範囲 |
| --- | --- |
| Willumsgaard, arXiv:2605.11390v1 | Theorem3.3・Lemma3.11。固定unitのA_n構造のtowerとcofiberによる正規化。公刊定理と同一視せず一次preprintに依存する。 |
| Segal, IMRN2018,3137–3154 | Section3.2、Remarks3.8–3.9とProposition3.10。twist/sectionによる復元案とcoherence上の留保。 |
| Christ, arXiv:2010.05294v3 | Proposition1.11、Theorem4.1、Section4.1・Example4.10。stable Kleisli、一般的な復元への反例。 |
| Dyckerhoff, arXiv:0904.4713v5 | Section5.6・Theorem5.8。一次PDFを確認し、一変数potentialの係数がminimal高次積になる公式を中央三次MFの直接計算と照合。 |
| Ballard–Favero–Katzarkov, Publ.IHÉS120(2014),1–111 | Theorem5.39。六変数三次のdiagonal sector公式からHom(id,ρ^b[a])を計算。 |
| Cremona–Fisher–O’Neil–Simon–Stoll, J.reine angew.Math.615(2008),121–155 | Sections1.3,1.6・Definition1.29。theta群と非退化なWeil交換子。 |
| Ballard–Farman, JNCG15(2021),1129–1180 | 公刊版Definitions3.16,3.18、Propositions3.41–3.42,4.14、Theorem4.15・Remark4.17・Corollary4.18。bigraded射影積と核。半局所底への有限性は本文で別証明。 |
| Positselski, arXiv:1411.1982v2 | Sections2.1–2.5,3.3。非斉次二次双対と曲率。 |
| Eisenbud–Peeva, LNM2152(2016) | Definition3.4.1、Proposition3.4.2、Constructions4.1.1,4.3.1、Proposition4.3.2。Shamashの高次homotopy。非可換中心元での恒等式と完全性は本文で確認。 |
| Burke, JPAA222(2018),4099–4125 | Definition4.1・Lemma4.4。split unitの正規化されたA∞操作。非分裂unitでのtowerの代用にはしない。 |
| Negron–Volkov–Witherspoon, JNCG14(2020),531–565 | Sections2.1,2.3,3.1。双加群の高次cooperationと完成tensor。shift規約は本文で明記。 |
| Mathew, Geom.Topol.24(2020),2675–2708 | Theorem1.3。可換Q代数上の実smooth proper dg圏のHH有限射影性。相対smoothnessを先に証明して適用する。 |

既知のPBW・Knörrer・球面関手・operadic obstruction・非可換射影積・相対退化自体を新規成果とは扱わない。書誌・参照箇所・識別子は論文と研究ノートに保持する。

### 保持する厳密計算

この節の計算は変更していない入力の既存確認であり、冒頭に記す現行変更の確認範囲とは区別する。

`python3 computations/verify_mixed_central_direction.py` は **7 PASS・終了コード0**。Knörrer座標、cotwistの二行二列homotopy、6×6行列式、P64根集合の二次momentとc62係数、中央MFの閉元・二項零homotopy・三項Massey scalar、重み三の単項式を有理数と多項式の厳密計算で確認した。SHA-256は `fe9b7c2bacacde762b5dc3bede3692c882ddc22808931b31ad59b1b2c509dfd3`。全coherence、生成性、Morita同値の形式証明ではない。

`python3 computations/verify_mixed_curved_dual.py` は **12 PASS・終了コード0**。実際の非可換関係を有理数上で簡約し、rank64+64の曲率、rank40+40への有限縮約、二つのchain map、retraction・homotopyとstrict Clifford ansatzの障害を検算した。この既存検証器のSHA-256は `68efa8db3e8c3d56e1b38ed458557e6d4a4c321ae14117ef4476c75c970f4c1b`。`--export` で全有理行列を再生成できる。これらの有限恒等式の計算は、解消の完全性・生成性・球面復元・Ku同値の形式証明ではない。

変更していない `verify_mixed_formal_kernel.py` の **9 PASS**、`verify_mixed_invariant_pbw_dual.py` の **5 PASS** は保持する入力であり、中心方向検証器とともに保持する。前者のSHA-256は `b4c7a92f9ae4f5847fffd010accfdb409a6427e56f4232cfdf441dbbe9a5cf72`、後者は `f950608a1aec0a9e4bed4a73204f89e0b51babff925eebea37043f172dd4c979`。既存の重い中心計算や全検証suiteを今回再実行したとはしない。

## 保持する数学的検証

以下は変更していない数学的本文・計算資産に対応する既存の点検範囲である。今回の編集で、全証明の再読解、厳密計算suiteの再実行、外部文献の再照合、形式証明器による検証を行ったとはしない。全中心係数の指定候補への比較は上記の中心係数比較の証明鎖で得る。以下の各不変量・局所計算自体から同値を導いたという意味ではない。

### 相対模型・根スタック・MF比較

- **全領域の相対模型：** cmo:prop:full-relative-hhを執筆担当以外の二名が点検した。固定ambientの有限解消、全閉ファイバーでの中心三次の正則性、次数別自由性、有限中心像の平坦性、射影中央模型、全twistの局所射影性、有限生成対象と底変更を確認。通常のcoherent代数Λと対角Mの底上flatnessと中央台のpropernessを確認してからproper-perfect-spreadを各c₀へ適用し、U全体へ拡張する。一般のproper dg族のfiberwise smoothからの推論は使わない。
- **通常HHと有理Euler形式：** 実相対smooth proper模型へMathew Theorem1.3を適用し、HHの底変更と連結性、余有限可換実現から全UのHHを求める論理を点検した。pr O(4),pr O(5)の射影係数、Euler行列、det729、基底変換を有理計算でも確認。ShklyarovのHRRとdim HH₀=2から有理Knum基底を得る証明を点検した。この不変量の計算自体は同値を与えない。実Morita核から積分Knum同型も得るが、表示した二類の積分基底性と核の行列表現は未計算である。c=0の非可換HH₀上の対合は恒等であり、HH±₁指標は上記の相対h模型から各(5,16)と決定した。
- **根スタックの幾何と実圏模型：** cmo:prop:eckardt-smooth-quotientとcmo:thm:eckardt-root-residualの二乗商、Bl_Y P⁵のRees表示、分岐の分離、線束M、根スタック同型を執筆担当とは別に点検した。N²≃Oの指定coherence、Bの線形化、ω_ℛの指標N、同変point blow-upの8対象をSerre逆で末尾へ回す操作、残る8線束、右直交の向き、再同変化、左mutation核の適用順序を確認した。これは可換標的内の実射影核であり、A₀からの比較核ではない。
- **対合付きHochschild群：** 通常HH±₁の固有次元(+5,−16)は、Jacobian次数二(+16,−5)とresidueのdeterminant符号−1から得る。固定集合Z⊔{p}のLefschetz数28でも照合した。同変HHの(1,5,24,5,1)は根スタック・blow-up SODとorbifold HKRの二通りで確認した。後者にはage shiftを入れず、4例外線束の2指標で8対象を除く。加法的不変量の相殺を圏のSODの相殺と混同しない。
- **非可換MFの完備化：** cmo:lem:isolated-azumaya-mf-completionを執筆担当以外の二名が点検した。有限射影MFのstable Hom、唯一の圏的特異点に台を持つ有限長Hom、平坦完備化、global simpleの高次syzygyのambient射影次元≤1、実MFへの持上げ、完成先の剰余体stabilizationの生成性を確認した。中心自体に他の特異点がないとは仮定していない。
- **固定曲率比較の範囲：** 各因子の有限中心・有限3CY解消、tensor ambientの有限大域次元、PBW濾過による曲率の正則性、全14節点の切断が有限大域次元であること、8/64のMorse値の相異性を既存入力と照合した。各固定値でのZ/2-MFの冪等完備後の比較は非標準的で、全パラメータの核・内部shift・三次周期は含まない。全smooth cでaffine MFは零、射影Kuは非零であり、c=−44828の具体的残余Extとも整合する。

### 一次資料と確実性

| 一次資料 | 既存の点検箇所・用途 |
| --- | --- |
| Mathew, arXiv:1710.09045v3（Geom.Topol.24(2020),2675–2708） | Theorem1.3、PDF p.3。可換Q代数上の実smooth proper dg圏に対するHHの有限射影性。 |
| Shklyarov, arXiv:0710.1937v3 | Theorem3.5・§3.2。HHのChern characterを介したEuler pairing。 |
| Orlov, Russian Acad.Sci.Izv.Math.41(1993),133–141 | Theorem4.3。点blow-upと余次元二blow-upの分解。 |
| Ishii–Ueda, Tohoku Math.J.67(2015),585–609 | Theorem1.6・Proposition6.1。滑らかな因子に沿う根スタックのSOD。 |
| Elagin, arXiv:1403.7027v2 | Theorem4.2・§8。指定coherent指標作用による二重同変化とdg enhancement。 |
| Arinkin–Căldăraru–Hablicsek, arXiv:1412.5233v1 | Corollary1.17(2)。商スタックのHochschild homology。著者PDFの本文を確認。 |
| Huybrechts, The Geometry of Cubic Hypersurfaces, 著者版 | Chapter1, Theorem4.21。Jacobian環とprimitive Hodge群のresidue比較。体積形式のdeterminantは本文で直接計算した。 |
| Dyckerhoff, arXiv:0904.4713v5 | Theorems4.1,5.2・§5.5。可換孤立超曲面の剰余体stabilization、2周期dg Morita、二次形式のClifford模型。非可換orderの完備化自体は本稿で直接証明。 |

書誌・識別子・URLは参考文献と研究ノートに記載する。一般のblow-up・根スタック・二重同変化・相対退化・HRR・MF生成理論を新規結果とは扱わない。具体的模型と適用の文献上の新規性の網羅的確認、外部査読・形式証明器による確認は未了。固定A₀の通常の実比較核と非可換HH±₁の対合指標は上記で構成・決定した。全標識付きの核、Q降下、積分数値格子の具体的な基底表示、一般αにおける局所orderと単純加群の全分類は未解決である。全αの残余線束圏のsmoothnessには上記の可換方程式による判定がある。

### 比較不変量の厳密計算

`python3 computations/verify_mixed_comparison_invariants.py` を最終ソースで実行し、**9 PASS、終了コード0**を確認した。執筆担当も同じ計算を独立実行した。QQ上で指定七変数三次のJacobian関係行列を構成し、次数二の固有部分のambient/rank/商の次元(22,6,16),(6,1,5)、次数三(62,37,25),(22,12,10)を確認した。同変Jacobian指標(1,5,11,15,15,11,5,1)、residue符号、Lefschetz数、同変HHの算術、共通Euler行列とdet729・基底変換も確認した。

検証器SHA-256は `d18567121b0be88e8253cd88db334958df3e39c12ca4f015f1d217a4a3cafa2f`。Python 3・SymPy 1.14.0による有限の厳密計算であり、相対smoothness・圏同値・根スタックSOD・全Poisson分類の形式証明ではない。既存の可換候補検証器の9 PASS、P64全係数とhashの一致は保持する入力であり、今回その重い中心計算を再実行したとはしない。

### 保持する孤立零点・可換候補・DVRの点検

- **全Poisson正規形の入力：** poisson-cubicの固定コミット9f91efa3465f18219c36c31750f1e66220faeaa7（A-v62）の支持節poisson_geometry.texについて、全bivectorの表示、錐上Jacobiへの持上げ、Hessianの基点自由性、根基排除、三重ベクトルのsl₂ブロック分解、thm:pg-normalまでの証明を通読した。確認時の同repo main 288246bca7b703543d24cf6276894dc5467bf1d2の同支持節は固定入力と全文一致した。未公表入力であること、全一般性を含む入力であることを本文・書誌に明記する。
- **孤立Poisson零点：** ppz:thm:isolated-zero-dimensionの証明を執筆担当と別の二名が点検した。Euler線の外積による零理想の同定、u≠0での3k偏微分、m=1の排除、m=2の零次元局所完全交叉、u=0での純ブロック曲線または複数臨界ベクトルの射影線型空間を確認した。純三次g_sの滑らかさ・非零性は使わず、中心方向の微分まで消えるとは主張しない。
- **被約反例：** ppz:cor:reduced-point-poisson-counterexampleは、既存の全64ノルム根のsmooth proper性と被約点スキームE₁⊔E₂⊔{p}に上記定理を適用する。Ku同値やTorelliを仮定せず全可換三次五様体のPoisson零集合を排除する。全64根への実Ku核は別に上記の構成で得る。c=−44828の中心値28,448と唯一のcharacterは厳密計算でも確認した。旧三様体の実Ku比較付き全スキーム反例は別の有効な結果として保持した。
- **可換候補と共通判別式：** cmo:prop:commutative-critical-spectrum、cmo:thm:commutative-discriminant-candidateを二名が独立に点検した。QQ上のJacobi環、尺度λ²=28/27での特性多項式、境界u=0の滑らかさ、64個の相異なる臨界値、各悪いファイバーの唯一の通常五次元二重点を確認した。非可換側の完備Mat36模型との局所比較は非正準であり、大域Ku同値の証明ではない。この具体的候補への相対核は、冒頭の全中心係数の構成で得られる。
- **零係数の模型：** cmo:prop:zero-eckardt-resolutionのG−u²L表示、pと接超平面、Y=V(G,L)の滑らかさ、incidence方程式、二つのchartでのwの貼合せ、Y上のP¹ファイバー、canonical divisorを二名が点検した。これは可換候補の幾何の証明であり、非可換圏との比較を含まない。
- **DVR判定：** grl:prop:trait-kernel-testの右加群規約、Q=RHom_B(P,B)の向き、単位と余単位の二cone、底上perfect性、導来底変更、Nakayama、有限長、有限平坦DVR拡大での分岐指数eによる長さの倍率を執筆担当とは別に点検した。既知の随伴判定を有限長として整理したもので、一般的手法の新規性は主張しない。grl:ex:perfect-kernel-not-equivalenceと研究ノートのF₂/F₀例により、perfectな核の延長やsmooth proper性だけでは同値の特殊化を保証しないことを明示する。


### 保持する節点・対角の点検

- **穿孔完備節点のBrauer群：** `cmo:lem:formal-node-brauer` の小解消Y、例外曲線P¹、Yの正則性と余次元2、Česnavičiusの純性、strictly Henselian底のproper base change、O_Y(1)のKummer classによるBr′=0を独立読解した。解析的linkと代数的穿孔Specを混同していない。
- **NCCRと全simple：** `cmo:lem:completion-global-dimension` の左右simpleの解消・minimal resolution/Tor、中心が完備化と可換すること、分裂束のreflexive延長とEnd同定、IW Lemma2.23→Proposition4.5→Theorem5.20を統合担当と別担当が点検した。自由直和因子は仮定せず、共通rank1 reflexive twistがEndそのものを保つことを確認。`cmo:thm:fourteen-node-orders` の重複度(1,5),(2,4),(3,3)、各因子28simple、次元分布8/2/8/2/8を確認した。3〜5次元の具体的行列の列挙ではなく、中心点と局所orderのsimpleによる全同型類の記述である。
- **非等方切断：** `cmo:prop:conifold-nonisotropic-slice` は任意の高次項を許す。切断のA1性、I/fIの非自由rank1 CM性、両辺reflexiveによるEndの底変更、μ₂ skew groupとglobal dimension2を確認した。形式的対角には完成包絡環と差Koszul分解を使い、通常のC上tensorに関する形式冪級数環のsmoothnessを主張していない。全28節点の横断Hessianは後記の厳密計算で確認。
- **相対・混合対角：** `cmo:lem:relative-diagonal-from-slice` の中央完備化、正則パラメータ、syzygyの射影持上げと忠実平坦降下を確認した。`cmo:lem:mixed-relative-diagonal` ではN=R^e⊗_{B^e}B≅(A^op⊗_C A)⊗_C Bを介する二段の有限解消を使う。B^e→Bを環写像とせず、相対projective項を直接R^e-freeとしない。中央基底をZ(A)⊗_C Z(A)に取り、局所化する元をZ(A)⊗_ℂ Z(A)から絶対包絡環へ持ち上げる。
- **射影境界：** `cmo:prop:projective-boundary-smooth` の強Z/6模型Q=L/(f−1)、Q⋊μ₆とL₀のMorita、有限群平均化、直接消去によるQ上のu正則性、中央持上げを点検した。次数一のuをL₀の元とせず、Q/(u)で切断する。既存の分離境界比較はk=2の次元4も許す。これは全α、非零a_i、k≥2、全cに対する境界の結果である。
- **正確な判別集合：** `cmo:thm:exact-sixty-four` は全中央点で少なくとも一方の相対対角がperfectとなることを使う。射影境界とcoherent飽和からP64(c)≠0の場合の全coherent smooth proper性を得て、既存Morse節点の無限自己Extで逆向きを得る。Serre(−4)[5]からqgrのhomological dimension5、根上で∞を確認。P64(0)≠0とgcd(P64,N)=1によりc=0とnorm全64根がsmooth properである。このsmoothness定理自体は比較核を構成しない。全smooth係数の実核は冒頭の別の構成による。

### 保持する局所理論の一次資料

| 一次資料 | 確認済みの箇所・用途 |
| --- | --- |
| Česnavičius, arXiv:1711.06456v4 | Theorem1.1=6.1。小解消から余次元2の例外曲線を除く際のH²(G_m)の純性。 |
| Iyama–Wemyss, Invent. Math.197 (2014), 521–586 | 著者版Definition1.7、Lemma2.23、Proposition4.5。End型CM有限大域次元代数からNCCR/MMへ。 |
| Iyama–Wemyss, J. Reine Angew. Math.738 (2018), 149–202 | accepted manuscript/arXiv:1304.5259v2 Theorems5.1(2),5.20、Lemma5.22、Corollary5.21。非generatorを含むcA_nのMM分類とrank1 twist。 |
| Stacks Project | Tags03QN,095T,03RQ,03PK,0A2J,0EBJ,0AV3。strictly Henselian cohomology、proper base change、Kummer、Azumaya、reflexive延長。 |
| Năstăsescu–Rodinò, Rend. Sem. Mat. Univ. Padova74 (1985),129–137 | 公刊一次PDF Theorems1.3,2.1。有限群次数付けのsmash productとEnd表示。強次数付けでの零成分との同型は本文で具体的に確認。 |

### 保持する厳密計算

`python3 computations/verify_mixed_center_geometry.py` の最終計算ソースについて、**14 PASS、終了コード0**を確認した。次数18までのPBW商、二つの21項中心関係、長さ18のcritical scheme、消去WH²Q、中心14節点、8Morse点、全節点の横断Hessian、64次終結式の偶性・平方因子なし・非零定数・定常normとのgcdを含む。全節点の切断に必要な確認はJ=(P,P_W,P_U,P_V,P_T)上の3変数Hessianの単元性である。二つの別担当も既存関係式から可換部分を独立再実行した。重複する検証器は現行一式に追加していない。

最終検証器のSHA-256は `1dafb9c120177e1ad1cb2b13222bfdf1951a0657cef58942097de86cdb464a27`。P64の全65整数係数を最高次からASCIIコンマで区切った改行なし6910 bytesのSHA-256は `20923491b92e21c3fceb0b30b0f331e500d83f898f756d0cb853ace75de42dbb`。大量係数列は保存せず再生成する。

未変更の既存計算として、`verify_mixed_two_dimensional.py` 5 PASS（SHA-256 `0edd52f5ffca48d1b859baac285f66badb06cda3a908e6aa97af8460848887a1`）、`verify_mixed_two_dimensional_ext.py --universal` 9 PASS・`--zero-example` 10 PASS（SHA-256 `2c6b23b735efb630822c5fe3130c9c51897a6f6663c0b9a7e7a96d1f85c6e226`）を保持する。普遍計算後の変更は独立した零例helper/flagのみで、最終版の零例は確認済み。`verify_mixed_pi_center.py` 3 PASS、`verify_mixed_character_ext.py` 8 PASS、`verify_point_poisson_obstruction.py` 12 PASS等も保持済みであり、これらの未変更の全suiteは今回再実行していない。有限計算を全次数中心生成・NCCR分類・対角・圏同値の証明の代用にしない。

### 保持する中心・表現・残余射影の点検

以下は現行本文に依存する既存の検証範囲であり、冒頭に記す今回の点検とは区別する。

- **全中心の一関係表示とPI次数：** `cmo:prop:center-hypersurface-degree` は、保持済みの普遍中心元とgr中心一致にSmith–Tate Theorem4.8を適用する。次数18の関係の持上げとstrict filtered inductionで核全体を得ること、符号反転でΩの奇数冪を除くこと、Hilbert多重度比36からPI次数6を得ることを確認した。次数18までの有限計算だけを全核の証明にしていない。
- **Azumaya locus＝正則中心：** `cmo:thm:azumaya-regular` を二名が独立読解した。3CYと全simple有限次元からhomologically homogeneous、Brown–Yakimov §3.8(b)(i)・Proposition3.10の入力から中心normal・中心上CMを得る。斉次化のu=0上の自由性とenveloping同型をNakayamaで持ち上げ、非Azumaya閉錐の次元を斉次Sklyaninの三曲線から抑える。余次元一Azumaya、有限大域次元、CM、normalityとreduced traceの条件を揃えて同論文Corollary5.2を適用する。有限中心性だけで結論していない。
- **中心幾何と新しい64係数：** `cmo:prop:center-critical-polynomials` の二つの21項関係、長さ18のcritical scheme、消去WH²Q、14個の通常二重点、正則中心上の8個のMorse点を厳密計算した。中心関係の非可換再生成は統合担当・執筆担当が実行し、その後の可換消去・Hessian・resultantを別担当も独立再実行した。19個の特異ファイバー値をそのまま非可換の例外値とはしない。
- **64個の真の非smooth係数：** `cmo:thm:morse-singular-sixty-four` は二つのMorse値の和の64次resultant P64を用いる。Azumaya性、形式的Morse補題、Mat36上のMorita同値から5次元通常二重点の局所模型を得る。自己Ext級数は(1+s)⁶/(1−s²)であり、36倍・36²倍しない。有限中央台による逆向きExtとGorenstein双対からRHom(𝒫,O(i))=C³⁶[−5]を計算し、有限例外射影Kの高次数自己Extが全てC³²となることを二名が独立点検した。従って全coherent Ku自体が非properであり、線束圏と残余線束圏は非smooth。全Db(qgr)のdg smoothness単独の否定は主張しない。P64と既存定常normは互いに素なので、余有限比較の除外集合をnormの根だけに取れない。
- **二次元simpleの全分類と剛性：** `cmo:prop:two-dimensional-classification` の跡零sl₂基底、半跡q(p)=α、abc≠0、逆変換q(q(p))=F(p)p、退化境界の分類を確認した。双対数環での正規形からExt¹=ker Dq、3CY双対からExt²を得る `cmo:prop:two-dimensional-center-rigidity` も読解した。F(α)≠0ではambient自己Extは0,3次のみ各1である。
- **二次元の普遍高次作用：** `cmo:lem:two-dimensional-shamash` と `cmo:prop:two-dimensional-universal-kappa` はrank(2,6,6,2)の自由分解、全higher homotopy、identity/traceで規格化した二段消去からκ₂=−2N₆/(9F)を得る。QQ(a,b)上の有理関数恒等式を実行確認した。相対Hom複体のconstant rankと局所収縮、最初のchange-of-rings微分の選択独立性による正則性、稠密開から全abcF≠0への延長を別担当も独立点検した。補助分母の零点を黙って除いていない。F=0には適用しない。N₆非零/零でpd2/∞となる結論は、有限自己Extの一般論ではなく、既存の中心商周期性・Reesの証明による。外積型のcochain模型をYoneda積と同一視しない。
- **characterが検出しない二次元の障害：** `cmo:ex:two-dimensional-zero-action` の三次体a³−2a²−11a+8=0、半跡(a,1,−1)について、普遍式とは独立な数体homotopy計算でもκ₂=0を確認した。全8characterのκ₁≠0と当該中心値にcharacterがないことを、有限エタール代数の二つの8×8乗法行列のdeterminantと互除法で確認した。二次元判定がcharacter判定を実質的に強める例である。
- **有限台perfect性と100加群：** `cmo:lem:finite-support-perfect` の中心像S⊂End(M)[u]、C[u]上有限性、u≠0内の閉有限台、中央Proj上の有限代数と線束compact生成を点検した。任意のj_*がperfect性を保つとはしていない。`cmo:prop:point-perfect` と `cmo:cor:hundred-perfect` において左右規約を確認した。高次元simpleの体双対については、自己Extの比較後に右側の有限ambient分解・周期性を別に適用し、有限pdを双対だけから推論していない。指定二因子の全100tensor simpleはpd5、延長は線束perfect。
- **64点の残余自己Ext：** `cmo:lem:mixed-line-serre` のproperな線束圏上のSerre(−4)[5]を真のCY双対から得る。`cmo:prop:projected-point-ext` の実例外射影F=[O²⁰→O(1)¹⁵⊕O→O(2)⁶→O(3)]、Shamashの内部次数成分による射影条件、ambient cochain微分、自己Extからの制限写像、Serre双対を独立読解した。KのExtは0次C、1次C¹⁰、他0。Euler値−9の数値検算だけを証明にはしていない。高次元simpleの残余射影へこの次元表を流用しない。

## 保持する数学的点検の範囲

### 満支持型の点・零スキームと幾何実現locus

- **満支持型の同時存在：** `point_poisson_split.tex` の零イデアル計算を統合担当と執筆担当以外が読解した。Euler外積の係数イデアル、mixed supportの階数、gradient単元による他block座標消去から、非被約底を含むスキーム等式を確認した。実因子を仮定する存在版は、既存の積比較・actual Ωの周期・Picard補正・三乗根同期を使い、j相異性・特殊j・2p≠0の除外を必要としないことを依存箇所まで再読した。自然θの境界延長や全O stackの自然tensorの存在とは区別する。
- **一ブロックの埋込み：** `point_poisson_obstruction.tex` のE_H⊔D_H分解、Hessian scalar条件による積分一意性、既存Casimir切断障害との接続を独立読解した。埋込みの一致を要求する障害と、全Poisson・全可換Ku標的を排除する現在の抽象スキームの反例とは論理の段階が異なる。
- **可換実現locusの開性：** `geometric_realization_locus.tex` のfinite-type C-baseと実相対smooth proper dg模型、比較核stackのlfp/Artin性、通常Artin形式認識の完全忠実性による指定核の持上げ、scalar Gmを保持したsmooth atlasとétale局所sectionを点検した。n4、DVR境界での閉性、全Abel族の飽和性、pointデータの保持は結論に含めない。連結性だけで全対象の可換実現を得ることもない。
- **局所開性の一次資料：** Toën–Vaquié arXiv:math/0503269v5 Corollaries3.15,3.21,3.22・Lemma3.25と、Stacks Tags02HX,055Uの局所smoothness・étale局所sectionについて、保存済みの原文確認を保持する。Sklyanin代数に用いるTate–Van den Berghとは別の文献である。

### 全中心同変核・無標識作用の既存点検

- **三因子以上の全中心同変核と正規化群：** 拡張したmbfc節を執筆担当以外も全文読解した。Orlov像がblock対角の場合の外積分解、実際のE×Ê上でのrotation行列r、第三因子による `(r−I)g_ij=0⇒3g_ij=0⇒g_ij=0`、同種・CMを許すk≥3への拡張を点検した。normalizerでは指標配置の自己同型が±S_kに限られること、Tate加群から整数Homのblock分解への移行、指定isometryの実関手への持上げ、三次周期の `3n=4` による共通反転の排除を確認した。正規化群自体と、それがAut(H)へ誘導する像は区別する。
- **全型の算術判定との接続：** k≥3、またはk=2で幾何学的非同種という仮定の下で、既存の全型判定が適用されることを再点検した。個々のδ_iの消滅を仮定せずα=Σδ_iを保持し、全coherent H構造の差をHom(H,Gm)=Gで分類する。通常の中心同変比較はγ_i+ν_i(φ_i)の一致、rotation・指定周期付きは全ての消滅を要する。固定Hesse levelの最小3^(k−1)／3^kはこの範囲で保持する。任意非被約底の全型stackや完全無標識比較へは一般化していない。
- **同種二因子の実際の混合核：** Pell元の整数Hom表示、Rosati条件、非対角成分と無限位数を点検した。Orlov liftの可換子shiftは三次周期で零となり、1−qのisogeny補正と三乗根規格化でcoherent中央化核を得る。核Z×E₁[3]×E₂[3]を持つ正確列と、次数二isogenyによるH反転核も内部で独立点検した。これらは代数閉体上の主張であり、一般K上の実現gerbe・周期位相は未分類である。
- **指定中心の非正規性と無限共役軌道：** mbun節を統合担当と執筆担当以外の担当が読解した。平面イデアル層のKuへの所属、χ(I_P,I_P)=2とSerre[2]からの球面性、実perfect kernel、flex接線による三平面、共通直線の過剰交差束O_L(−1)、Mukai行列2J₃−4I₃を確認した。球面反射による非正規性、二つの捻りの積の全整数冪による無限共役軌道、既存のG同変比較を介する非可換幾何点への移送を点検した。中心の共役類の内在的認識や元のK上での比較次数の低下までは示していない。
- **一次資料：** Orlov著者版のDefinition2.17・Proposition2.18とTheorems4.13・4.14を、実アーベル多様体上のisometryと代数閉体上の持上げに照合した。Seidel–Thomas著者版§2b Definition2.9・Proposition2.10の球面捻りとdg評価写像、Kuznetsov刊行版p220の(2)–(3)とSerre関手の記述を直接確認した。書誌・識別子・参照箇所は `papers/references.tex` に記載する。既知の球面捻り・Orlov理論を新規結果とは扱わない。
- **厳密計算：** `python3 computations/verify_multiblock_isogenous.py` を実行し、rotation行列、Rosati/Pell式、複数次数のPell元、同一因子の混合unipotent、次数二反転、三平面のGram行列と球面反射、無限共役軌道の全整数冪の式の全七組が成功した。SymPy 1.14.0の厳密な行列・多項式計算であり、幾何的対象の存在、Orlov liftやcoherenceの形式証明ではない。この計算器の既存確認を保持し、今回の追加計算とは区別する。

### 自然周期・内在的積核の既存点検

- **自然な周期の全係数：** mbhp節を執筆担当以外も全文読解した。二つのchartによる全九flexの中心正則化、三捩れ点でのpolynomial Zhang twist、THCRの核直線、raw top syzygyを保つwindow、比較線V=λ⊗O(o)と同期前の三乗写像を点検した。原点の−3F対6Fからq_V(id³)=−1/2、conormalの一次項−tとWeierstrassの主部−2t⁻³からq(ω³)=−1/v_ω(p)を校正する。普遍被約Hesse表示上で射を一致させ、降下後に非被約底を含めて引き戻す。
- **内在的な積核と比較stack：** mbic節を統合担当と別担当が全文読解し、第三担当もscalar・Γ慣性・非捩れ積表示を監査した。τ_z=θ_zの向き、対角liftの消去、積cocycle、PからBへの実核の降下、独立な偏極twistの両側相殺、全O認識開の適用範囲、順序なし相対rotation比較を確認した。核stackの降下と大域切断、個々のrotationの降下は区別する。
- **因子自己同型の位相：** pushforward規約のν=[c_g]、非零ν例、固定Hesse levelでのν消滅を読解点検した。Orlov著者版Propositions2.15・3.2–3.3とTheorem4.14、Artebani–Dolgachev刊行版§4 pp246–247を直接確認した。内在的降下の担当はBergh–Schnürer刊行版Propositions4.10・5.7、Corollaries4.12・5.9、Romagny Theorem5.1、Stacks0DMEも直接照合した。SilvermanのWeierstrass変換則は既存参照を用い、本文で変換を直接計算した。書籍PDFの再取得はtimeoutであり、書籍全該当本文を再読したとは扱わない。
- **厳密計算：** `computations/verify_multiblock_hesse_phase.py` の二つの中心正則化chart、原点の三次jet、dX/ω=V、Weierstrass式とqV=−1、原点係数、Hesse生成元の方程式保存、g(f)=af・g³=aIの全五組の成功を保持する。SymPy 1.14.0の有理式・多項式計算であり、圏比較・降下・最小次数の形式証明ではない。この計算器は今回再実行していない。

### 相対積・Picard型の既存点検

- **相対noetherian性と実window：** mbrn節の全証明を執筆担当以外も読解した。訂正済みKeeler Theorem1.5の相対nef版消滅を用い、全kの多重評価イデアルの安定、非平坦な評価加群の射影公式、有限幅の端の帰納、中心正則列のfiltrationを確認した。任意noetherian基底のnoetherian性と、正則基底での有限大域次元・BSの適用は別段階である。BS Definition5.1とRemark5.2がcohomological shiftとinjective dimensionの一致を要求しないことを一次資料で照合した。
- **相対非可換積核・任意底変更：** 関係直線を保持した有限Koszul–Shamash解消、Tor二段の連結射、Γ-Hom、有限生成対象、K-flatなHom模型、実windowと外積、有限群双対化を内部で独立点検した。構成済みMorita核とcompact/Perf模型の非平坦・非被約底変更まで確認する。元のsmooth affine基底でのcoherent飽和は別に証明し、非正則底での全Dbcohや全coherent MFへの同値は主張しない。
- **Picard型のscalar・位相・kernel stack：** mbpd節を統合担当と別担当が全文読解した。外積bandの積によるα_Pic=Σδ_i、Hom比較直線とHodge線の同定、c4/c6の重みによる単元表示、対角μ3商Dと積torsor T、G-marked Picard型kernel stack G_Pic×DとG_Pic×Tを点検した。共通位相は比作用から消えるが、rotationの指定周期に残る。中心作用を忘れた全核の分類とはしない。
- **自然な二捩れ境界と最小位相次数：** mbrnの一因子補足とmbpdの境界証明を執筆担当以外も独立読解した。最上syzygy線Pのままの相対双対・window、a=bでのΩ_H非零、自然targetの3dF_H、周期の逆尺度変換から剰余+1を確認した。交代化P→detWは境界で使わない。有限型函数体C(d_1,…,d_k)とその完備局所例で、付値剰余行列が単位行列となり、指定Picard型・中心作用付きの最小位相次数3^(k−1)、rotation/period付き3^kを証明した。全核型や全上界3^(2k−1),3^(2k)の最小性は主張しない。
- **一次資料：** Keelerの訂正済みarXiv:math/0108068v5のTheorem1.5（p3）、Definition2.9（p5）、Proposition7.2・Lemma7.6（pp30–31）、erratum TheoremE2.5（p40）を本文で確認した。Burke–Stevenson公刊版Definition5.1・Remark5.2（p110）とTheorem6.4（p115）、Smith–Tate §1（pp19–21）の位数二を除外しないSklyanin・中心商の記述を照合した。Silverman III§1 Table3.1（p45）のc4,c6,微分の変換則は原著PDFを対象とする検索抽出で確認した（PDF全体の直接取得はタイムアウト）。本文の使用はこの変換則に限る。既知の相対Fujita・Orlov・Picard/Kummer・同変化理論と本稿の適用を区別し、新規性の網羅的確認は未完了。


以下は分割前から保存されている有効な証明点検・文献比較・厳密検算であり、上の今回実行した内容とは区別する。仮定と結論は現行本文に保持する。

既存の点検では、全 n≥3 の境界低積、飽和した二次表示、中心商、smooth potential 三次による指定一般点同型の延長、完備局所周期位相の証明を、執筆担当以外も独立に読解点検した。主な新結論は γ_sc,n|_{k₀((z))}=[D_R]、v_D(γ̄_n)=1 mod3、正準位相体の次数三である。固定 MF・window・一般点生成性・coherent 飽和性の入力の下での結果である。外部査読、Lean 等の形式証明、固定入力全体の独立再証明、新規性の網羅的確認は行っていない。

- **実際の窓と周期。** Burke–Stevenson i=1 の窓で Ψ₁Z=N₀(−1)[1] を全 n に同定した。例外対象の section truncation が自由加群になること、M(t) の高次消滅、同じ曲率 F_R の MF 周期、共通 shift の周期符号を点検した。任意の特異圏の包括的な底変更を仮定していない。
- **全 orbit Hom。** F₀=bXYZ となる選択済み pole 消去模型に対し、active MF と零曲率 Koszul 因子の unital bigraded dg 分離を確認した。特殊 fibre の Λ(k^{n+2})⊗k[t,t⁻¹] はベクトル空間の記述であり、積の同定ではない。一般 fibre との二次数次元の一致と DVR の普遍係数列から全 Hom の自由性・底変更を得る。階数は binom(n+2,3i+2q)。既存の n=3 の表はこの公式の例として保持した。
- **積の退化と一次 jet。** active m₂=0、m₃=0 を明示 cocycle と homotopy から確認した。m₃ の零次項は tensor 自体で零である。full m₂ の特殊階数は binom(n+2,2)−3。F_R≡J_R mod z² とし、同一 dg 模型上の contraction を単位と周期を保って持ち上げることで、full と active の一次 jet を接続した。三つの Smith 指数が全て一、三次先頭項が +z acb/(3p) となる符号を、一変数 x³ の閉じた tree −(hφ+φh)=I でも校正した。
- **飽和と内在的中心。** 二次関係の飽和後の特殊代数は S(0,−2,−p)[u₁,…,u_r]。量子多項式環の Zhang twist により Hilbert 級数を直接求め、各次数の generic rank と特殊次元の一致から全次数の自由性を確認した。中心一次部分は rank r の直和因子で底変更に両立し、中心正則列の商も自由である。二次関係の飽和から全高次の平坦性へ進む論理を独立点検した。
- **potential と表示同型。** active 商の cubic syzygy line は rank一で cyclic、交代成分は単元である。その symmetric potential は g_{p,2}=pΣX³/3+2XYZ という滑らかな三次を与える。点曲線 XYZ=0 との区別、Benoist の有限 projective Isom への実際の generic section の延長、Pic(R)=0 による GL₃ lift を点検した。full 中心変数方向の同型延長は主張しない。DVR の剰余標数は零と限定した。
- **局所位相の exact class。** source の指定中心公式から Ω₀=p(p³+8)G/3 を確認した。target Ω_p は飽和 active 格子で正確に z 倍の primitive class。特殊表示同型との差の自己同型が G を cube 倍することを独立に点検した。scalar の一次係数は −1/[p³(p³+8)]、D_R/z は −(p³+8)²/27、比は (3/[p(p³+8)])³。完備性と 3 の可逆性を使って exact class [D_R] を得る。未完備商体での exact class、大域 γ̄_n=[D]、他の分岐排除、位相体上の scalar index はこの結果に含めない。

証明の所在は [境界低積と周期位相](../papers/sections/residual_boundary_products.tex) の `prop:nfm-boundary-all-orbit-flat-rank-drop`、`prop:nfm-boundary-first-jet-products`、`prop:nfm-boundary-saturated-active-potential`、`prop:nfm-boundary-period-local-kummer`。既存の相対線型行列、三次元の幾何学的低 Hom 計算、I₃ の成分群・三分点計算は [境界模型](../papers/sections/residual_boundary.tex) に保持した。三分点被覆は局所三次位相体の三コピーであり、位相 torsor 自体と同一視しない。

以下の四点は、現行稿に保持している既存の内部独立点検である。既存の点検で全証明を一括再検証したという意味ではない。

- **全次元の強化 class の一意性。** 固定した三次双加群自己交叉、内部次数による change-of-rings 列の短完全性、通常 Ext の積、中心周期による dg 局所化を確認した。Tate Ext の j=−p−q≥0 の切出しが全 A∞ 積・写像・homotopy に保たれること、Adams Koszul 双対の Hom の全単射、局所化の homotopy epimorphism、Adams covering と hull を通した実際の kernel class の回復を点検した。表示安定化子の一般自明性と合わせ、全 n≥3 の一般一ブロック族で H_p=1、S_p=Spec(k_n)、split 体での未標識強化型最小次数三を得る。全 full class の分類ではない。証明は [Tate–Koszul 復元](../papers/sections/residual_tate_reconstruction.tex) の `thm:nfm-origin-rotation-faithful`、`cor:nfm-generic-adjoint-class-unique`。
- **五次元の半 rotation の関手同定。** spinor 完全列の射を相対随伴の unit と同定し、相対 coevaluation と通常の right mutation の coevaluation を自然変換として比較した。Ku の消滅と Beilinson 分解により差が ⟨C₁⟩ へ入り、mutation で消えることを点検した。O≃ρ⁻¹[1]、O³≃[1]、ε≃id は対象の固定からの推測ではなく perfect 核の自然同型である。既存の相対核・Fano 曲面の連結性・次数2835の零 cycle による実核降下と、E_p の二 mutation の計算も保持する。指定 square 同型と MF 周期の同時正規化は別問題。証明は [五次元の節](../papers/sections/residual_fivefold.tex) の `lem:nfm-fivefold-spinor-relative-coevaluation`、`thm:nfm-fivefold-half-rotation-identification`。
- **非分裂 rotation の算術。** 偏極 gerbe 上の例外的 projector kernel の重み零、rotation kernel の重み一、convolution による Brauer 類の和 α+rβ、次数±三 Picard 類の index 上界を点検した。指数九族の符号規約は α=(a,v)₃−(b,u)₃、β=(a,b)₃ であり、α±β の symbol 表示と K(∛au) 上の α の非零剰余も確認した。一般一ブロック開の全 n≡1 mod3 に強化型最小九を実現し、同族の rotation 軌道内では三となる。全 full 型の最小三を確定するのは幾何的 Z 分類が適用される n=4 であり、高次元の他の軌道までは分類しない。証明は [非分裂 Picard 障害の節](../papers/sections/residual_unsplit_picard.tex) の `thm:nfm-unsplit-rotation-index-three`、`thm:nfm-unsplit-lowdim-full-degree`、`cor:nfm-unsplit-nine-versus-three`。
- **全次元の正準強化 class の周期位相。** κ(m) 上の混合有理比較が、形式拡大後に同じ全 Taylor 成分と hull を持つ完備 CF 核になることを確認した。最高次線束、Picard 等式、随伴射 cone の消滅を忠実な体拡大から反映させ、特定の比較核が強化型であることを示した。従って全 n≥3 の正準 class の γ_sc,n が C(c₄,−c₆) へ一意に降下する。Hesse 拡大の Kummer 核は ⟨[Δ]⟩ だが、一般 active 係数から得る半古典条件がその曖昧さを除く。D の八直線への分解、q=2 での非分岐性と一次係数も点検した。全 full class に共通な位相という主張は n=3,4 に限る。完備局所値は既存の点検で [D_R] と決定した。大域的な次元間の一致・ΔD 以外の非分岐性は未証明。証明は [周期位相の節](../papers/sections/residual_period_descent.tex) の `prop:nfm-adjoint-period-all-dimensions`、`prop:nfm-period-hesse-faithful-test`、`lem:nfm-period-hesse-eight-boundary-lines`。

以下の随伴復元・有限 class・cube frame に関する点検は、既存の検証として保持する。現行稿の追加証明の点検と、過去に検証した全結果の再実行・再読を同一視しない。

随伴復元では、q=Li_C^*j_Y の右随伴が q^R=j_Y^!i_* であること、Serre 半直交性と線型 Koszul 解消による q^R O_C≅j_Y^!O_Y、truncation の随伴射が閉ファイバーで同型になることを点検した。既存の形式比較で得る一般ファイバーの最高次線束と、閉ファイバーの構造層を使い、新しいDVR補題で全体の最高次線束性・平坦性・底変更を証明した。閉ファイバーだけから平坦性を推論せず、局所環での非零因子 h と一般ファイバーの階数一を併用する。その後の cone 消滅には導来 Nakayama と proper 性を使う。

有限群 H_p の証明では、固定入力Bの三対象 window と一般点の coherent 飽和性により E_p⊕ρE_p⊕ρ²E_p が compact generator となることを実文で確認した。核の underlying Hom cohomology に一様な有限 bound を与え、Toën–Vaquié Proposition3.20 の有限表示性、自己同値 locus の開性、HH¹=0 の離散性を適用する。HH¹=0だけから全自己同値群が有限とする推論はしていない。有限 H_p-torsor S_p と Picard gerbe の積表示は、最高次線束を取る関手が scalar band に恒等を誘導することで確認した。

三・四次元では既知の G_ρ=〈T〉 と H_p∩〈T〉=1 からも H_p=1 を得る。全次元の一般一ブロック族については上記の Tate–Koszul 復元が自明性を与える。class の一意性は元の体上で実際の核を取れることを意味せず、scalar gerbe はなお非自明である。固定入力の外積表示と proper Hom の Euler rank の一定性から χ(E_p,ρ^rE_p)=χ_(N,r) を得て、既存 gcd d_n>0 により [E_p]≠0 となる。奇数次元の H_p⊂G_(ρ,0)、五次元の χ(E_p,E_p)=−27、一般形式の最小次数 min_i[K_i:K]ind(α_Ki)≤3|H_p| も保持する。

周期規格化では、元の残余復元が方程式直線を与えることを明確にした。source の中心元 Ω と full Poisson 対から三重ベクトル P が一意に定まり、φ_sc の線型持上げ f に対する F_φ⊗det(f)P=t_sc が方程式生成元を三乗倍まで定める。一般係数体の線型三捩れ monodromy が SL₂(F₃) であることから $J[3](K)$=0、I_sc(K) は一元集合となる。f の scalar 変更は三乗倍、Ω の変更は source/target の同時変更なので、全次元の正準強化 class の γ_sc,n はこれらに依存しない。形式比較式 F_φ=λ_h⁻³b_h⁻¹W_h と b_h≡1 mod h を確認したが、形式体での消滅を元 K へ戻してはいない。F→hF の吸収では中心元と実際の曲率の双方を h 倍する。元 K の γ_sc は既存の点検の境界計算により非自明である。大域式はなお未決定である。

既存の周期位相の class 不変性、生成元の source u 倍・target v 倍による γ′=[v/u]γ、適合規格化の最小次数三、target の独立尺度を加えた一般族の最小次数九は保持する。元の自然な規格化 γ_sc の具体値と、自由な相対尺度の定理は区別する。点型の全 O-降下、標準三分点体の次数九と ASL₂(F₃) の二百十六次 monodromy、三・四次元の全 full class 降下、全 class に共通な scalar index 三、七次元の既知球面対象からの全自己同値群の非巡回性も保持した。既存の全証明と未公表固定入力を既存の点検で一括再検証したという意味ではない。

既存の点検で新たに作成・実行した検証器は `computations/verify_boundary_low_products.py` であり、十群の PASS と終了コード0を確認した。執筆担当と統合担当がそれぞれ実行した。Python 3.12.14、SymPy 1.14.0 を用い、有理関数体 Q(p) 上の厳密演算である。他の十六件の計算資産は基準 main `abdc32ee39cedc0b78f73b607521794157f6f219` と全内容を照合して不変と確認し、既存の点検では再実行していない。以下に保持する既存の PASS・対象ハッシュは、その検証範囲の記録であり、当該点検の新たな実行を意味しない。

## 1. 固定した入力と文献

- `uedakazushi/poisson-cubic`：現行の古典Poisson論文 `papers/poisson-cubic.tex` A-v62、固定commit `9f91efa3465f18219c36c31750f1e66220faeaa7`。保持している以前の点検では分割前の固定commit `eabe601c1341777742964584dde5314c0bcf64a9` を使用した。量子化の現在の正本は別repoの `papers/cubic-quantization.tex` Q-v1であり、その証明・一次資料監査は `notes/quantization_audit.md`、実行状態は `validation_quantization.json` に置く。旧論文B B-v59の完備MF移送・可換復元の全証明は本リポジトリの `papers/sections/generic_recovery/` に統合。旧原稿を外部入力とは扱わない。
- `uedakazushi/nc-cubic-threefold`：`6c35d2c84671c2538e61836a6bf3a511392eacce`。比較対象の三様体稿 v22。

通常の非可換研究では外部入力リポジトリは読取り専用。ユーザーが指示した三論文構成への移管ではpoisson-cubicとの整合も行った。既存の一般次元正規形・中心量子化・一般点残余復元は新規成果に数えず、未公表入力の全証明を独立に再検証したとは主張しない。引用箇所は [研究ノート](research_notes.md) と [文献一覧](../papers/references.tex) に記す。

既存の点検の境界計算では、Burke–Stevenson の公刊版 Theorem 6.4(1)、window i=1 と相対 Gorenstein 条件を再確認した。Benoist の公刊版著者 PDF の Theorems 1.6(ii),1.7 と Lemma 2.2(iii)、pp.140–141 を担当者が一次資料で確認し、剰余標数零の滑らかな potential 平面三次への適用を独立点検した。統合担当は固定入力Aの `papers/support/papers/sections/hesse_mixed_universal_center.tex` を固定 commit から読み、`thm:pg-universal-hesse-mixed`、`eq:pg-hm-coefficients`、`eq:pg-hm-center` の式を h′=p, t=q/p で変換し q=2 に特殊化した。中心性全体の独立再証明ではない。

既存の周期降下の点検では、統合担当が固定 commit の `papers/sections/generic_recovery/curved_transport.tex` を実際に開き、`cft:eq:bound`、`cft:lem:primitive`、`cft:lem:arity`、`cft:lem:flow`、`cft:eq:object`、`cft:eq:insertions`、`cft:eq:two-block-matrix` の bound・原始元・arity・有限対象・挿入・二ブロック模型を新証明と照合した。三対象生成、proper Hom、局所化は `gcd:prop:bound`、`tw:lem:proper-hom`、`rog:lem:localization` と比較した。これは必要な一次模型への適用確認であり、入力B全体の全証明の再検証ではない。Fisher の不変式・一般軌道・Heisenberg 群の既知記述と、保存済みの全三捩れ monodromy を用いる character の消滅も内部点検した。

非分裂曲線には Cremona–Fisher–O'Neil–Simon–Stoll, J. reine angew. Math.615(2008),121–155、DOI10.1515/CRELLE.2008.012、arXiv:math/0606580v1 の §§1.1,1.3,1.6、Proposition2.2、Lemma2.4 と Ciperiani–Krashen Theorem3.7 を照合した。Saltman, *Genus 1 Curves in Severi--Brauer Surfaces*, arXiv:2105.09986v1 の §§3–4、Theorem5を既知の関連結果として確認し、曲線の period–index 現象そのものの新規性は主張しない。

Tate–Koszul 復元には Lu–Palmieri–Wu–Zhang, New York J.Math.14(2008),325–378 の Definition2.1・Theorem2.4・Corollary2.5(b) と、同著者 JPAA213(2009),2017–2037 の Theorem A・Corollary B を一次PDFで確認した。Braun–Chuang–Lazarev, Adv.Math.328(2018),555–622、arXiv:1505.01146v3 の Proposition3.17・Theorems3.18,5.3 を照合した。Keller の orbit 圏論文 §§9.3–9.4 と2009年訂正も確認し、訂正対象の旧§7の hull 表示は使わない。統合した基礎節の `field_model.tex` の `gcd:prop:automatic-as`、`local_model.tex` の `lp:lem:noetherian`・`lp:prop:koszul`・`lp:prop:gorenstein`・`lp:prop:sing-period`、window・coherent 飽和の該当命題を本稿の仮定に照合した。詳しい識別子とリンクは研究ノートの「Tate–Koszul と Clifford 同定の一次資料」に置く。

有限 class の入力として Toën–Vaquié の Proposition3.20、Corollaries3.17,3.22,3.24 と Lemma3.25 直後の可逆核 locus の開性を原著で確認した。統合した基礎節の window.tex の tw:thm:window・tw:eq:main、main_result.tex の一般点 coherent 飽和、generic_descent.tex の rog:eq:exterior と proper Hom を、当該点検の生成性と Euler 数の比較に照合した。Murfet の arXiv:0912.1629v3 Theorem6.2・式(6.6)、Proposition4.2・式(5.7)を確認し、公刊書誌 Compos.Math.149(2013),2071–2100、DOI10.1112/S0010437X13007082 を出版社と照合した。

五次元では Peize Liu arXiv:2509.21454v5（2026-08-03改訂）の Theorem2.8、§2.2の式(2-4)・Remark2.11、Lemmas2.12–2.14・3.4、Corollary3.10(ii)、Proposition3.11、Theorem5.5の証明、Corollary5.10を一次資料で確認した。Proposition6.10は Fano 曲面を一つの stable moduli 成分と同定し、全 moduli の既約性は Remark6.11 の予想、安定性軌道の一意性は Remark5.6 の未解決問題として区別した。Kuznetsov の公刊版 Adv.Math.218(2008),1340–1369 の Theorem4.2、Lemmas3.8・4.5・4.6・4.7・4.10、Remark4.8で実際の Clifford kernel、局所自由性、有限振幅、随伴を確認し、Collino Propositions1.8・1.10、Ciliberto–Zaidenberg arXiv:1903.11294v2 Example4.4の幾何学的連結性と次数2835を照合した。平面非依存性と元の体上への実核降下を内部点検した。さらに Proposition3.3 の相対表示と spinor 列の Lemma4.5 を用い、O≃ρ⁻¹[1] の自然な関手同定を独立点検した。Wu arXiv:2611.02388v1 Theorems1.1,1.3・Proposition7.2 と Aravena–Liu–Tevelev arXiv:2611.05350v1 Theorem1.2 の主張も確認したが、これら最近の安定性条件の全証明を独立再検証したとはしていない。有限 H_p の証明はこれらに依存しない。

一次資料で、Gesmundo–Landsberg の Proposition 6.1・式 (6.2)、Landsberg–Ottaviani の §1.2・§4.1、Boij の Remark 6（pp.163–164）、Boij–De Negri–De Stefani–Rossi の Introduction、Bricalli–Favale–Pirola の Proposition 2.1・Theorem 3.4 を確認した。Jacobi 写像と Koszul flattening・apolar Betti 数の同定も証明し、普遍階数上界と N=9,10 の二次階数の達成を既知の帰結として位置付けた。現行の次数三の決定や平方零拡大の非分裂性を、既存の Betti 数の表だけから導いたとは主張しない。全次元の一般 apolar 代数について β₄,₆=0 を示す文献は確保していない。

相対双対の入力は Berger–Taillefer の Theorems 3.1, 3.6、dg Morita 表示は Keller の Theorems 3.4, 3.8。係数降下・Kummer・曲線上の主因子は Stacks Project の Tags 023N, 03PK, 040Q, 02RU を確認し、現行の圏内の係数作用・全同値の降下には本文で証明を与えた。新規性の網羅的調査は未完了である。

既存の点検では、Behrend–Noohi の刊行版§2.3・§3.1.2を確認し、grading rigidification、twisted algebra、determinant character を既知手法として明示した。EGの刊行版§9・p.1414のRains中心公式は本文とPDF画像で確認し、Proposition 8.1.1・式(8.1.3)の形式的中心比較と当該点検の有限係数での処方を区別した。LBSVの刊行版Proposition 4.2.5・pp.193–194の二次関係復元も照合した。Stacks Tags058G,0781,03R6,063P,063U,062Y,056Qは新しい降下・相対幾何の使用箇所と照合した。固定入力の `prop:pg-ad-intrinsic-hessian` と `cor:pg-hesse-hessian-form` は、純中心補正の前後を区別して式を確認した。その未公表入力の非可換中心性の証明全体を当該点検再検証したとは主張しない。

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

Canonaco–Stellari *Non-uniqueness of Fourier–Mukai kernels* の著者PDF Theorem1.2・Corollary4.4で、同じFM関手の核のcohomology層が同型になることを確認した。Math.Z.272(2012),577–588、DOI10.1007/s00209-011-0950-3を出版社で照合した。一般の核そのものの一意性を引用せず、本稿のprojectorに必要な追加証明を与える。Poonen のTheorems1.1,1.5と直前の開性の記述、Ciperiani–Krashen のTheorem3.1も当該点検の適用箇所に合わせて再確認した。三分点monodromyの古典入力はFisherのTheorem1.1(iv)、Lemmas2.2–2.3、§4と、Matsunoの§2.4・§4である。

指定周期の変換について、固定入力Bの `papers/sections/generic_recovery/local_model.tex` の `lp:prop:sing-period`・`lp:eq:period`、`papers/sections/generic_recovery/window.tex` の `tw:eq:period-extension`・`tw:eq:rotation-period-square` を実ソースで確認した。conormal の生成元変更と二拡大の境界、window で移送される周期を照合した。入力B全体の再検証とは扱わない。

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

保存済みの全6例について、指定した平方小行列の行列式を探索とは別経路で直接計算する検証が完了している。以下はその保持した結果と対象資産のハッシュである。全6例の再実行は既存の点検の追加検証には含めない。

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

探索には低位 pivot のブロック消去を用いた。保存した39600行の平方小行列は、別の高位 pivot の通常 Gaussian 消去で直接検証し、全階数39600・行列式1を確認した。現在の保存対象コードによる再生成からこの検証までの実行は完了している。既存の点検ではこの大行列計算を再実行していない。検証器と数学的な縮約の論理は、実装担当以外も読解点検した。

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

`computations/verify_center_hessian.py` は保存済み検算で SymPy 1.14.0 により全assertionと二つのPASSを確認したコードである。既存の点検ではこの既存計算を再実行していない。検算対象のSHA-256は `20bb71ce1b8c56f0e81a3776dce38c1f1f786ec54a44c409a0ecf2c71d4721bc`。浮動小数点、係数の補間、ランダムな有限標本は使わない。

- 公刊Rains式の可換化と、κ=−4h⁴(1+λ³)/(1−hλ/2)⁶ の差が三偏微分のイデアルに入ることを、明示的な係数恒等式で確認した。統合担当は別の短い式の簡約でも係数を確認した。
- HessianのJacobi類が8(1+λ³)xyzとなる恒等式と、固定入力のHesse中心のW−λUを確認した。
- 六つの混合係数を独立記号とするFermat型の八次自由代数を、平方自由単項式の基底で扱い、正規化traceと有限hの純中心補正を計算した。これは任意個の中心変数への特殊化を許す係数恒等式である。
- 最後の比較に用いるΩの非可換中心性は、固定入力の `cor:pg-hesse-hessian-form` を使用する。このスクリプト自体がその中心性やPBW性を再証明するわけではない。

### 幾何補正と残余比較の保持した厳密検算

`python computations/verify_geometric_corrections.py` は保存済み検証で全assertionと13個のPASSを確認したコードである。今回の点検では再実行していない。検算対象のSHA-256 は `78f592342b91531a6382576cc6025c8684e7f56d5efa84019b02d91b9923b85c`。その確認対象は次の通り。

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

保存済みの検証で `python3 computations/verify_picard_obstruction.py` を実行し、SymPy による有理関数・多項式の厳密演算で全 assertion と13個の PASS、終了コード0を確認した。既存の点検ではこの検算を再実行していない。

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

## 6. 現行ソースと組版

本repoの唯一の主原稿は `papers/nc-cubic.tex` である。現行入力グラフの参照・引用とLuaLaTeX組版の実行範囲は先頭の現行確認に記す。量子化稿は外部repoへ移行済みであり、ここでの主稿組版を外部稿の組版確認としない。旧名の原稿や過去のPDFを現行稿の組版証拠に使わない。PDFとSyncTeXは `build/` に置きGitで追跡しない。VS Code設定とレシピ相当のルート基準コマンドは整合しているが、VS Code UIの操作は当該点検行っていない。

## 7. 再現と保存の区別

再現手順はルートの `README.md`。相互参照を含む三稿は `python3 scripts/build_papers.py` で `build/` に出力する。主要依存は LuaLaTeX・LuaTeX-ja・和文フォント・標準 TeX パッケージ、Python 3・NumPy・SymPy、C++17 コンパイラ。次数三の検証は約450 MBの行列を再生成し、直接消去には約220 MBのメモリを用いる。大行列は保存せず、220個の入力・行番号の圧縮表・検証コードから再生成する。

保存対象は現在の原稿、研究方針、研究ノート、本検証範囲、書誌、再現コード、証明書、必要な設定だけ。入力稿の全コピー、旧稿、旧bundle、担当者別レポート、外部文献PDF、ビルド中間生成物を含めない。PDFは再生成物として提供し、Gitの追跡対象に含めない。

外部への保存は生成・検証とは別に、GitHub の tree にある全ファイルの blob SHA を手元のソースと照合し、通常の fast-forward による main の更新後に、先端 commit と tree を読み直して確認する。保存された版の識別子は Git の履歴と配布時の報告に記す。この文書だけをもって、未実行の外部保存が完了したとは扱わない。
