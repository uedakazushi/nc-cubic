# Research instructions — nc-cubic

2026-11-21 / v38。再開時は `00_research_plan.md` を最初に読み、`notes/research_notes.md` と `papers/nc-cubic.tex`、必要な `AGENTS.md` を確認する。研究全体の入口は https://github.com/uedakazushi/research-hub 。

- 正本は `uedakazushi/nc-cubic` の `main`、主論文は `papers/nc-cubic.tex`（日本語LuaLaTeX、本文あり、著者欄空欄）。別論文 `cubic-quantization` は https://github.com/uedakazushi/cubic-quantization へ移行済み。量子化節・原稿・中心元計算・ノートは外部repoで管理し、本文を重複させない。
- このrepoの目標は非可換三次n-foldの可換復元・O-markedモジュライ・残余Poisson射・Ku比較。一般中心三次変形のMF/window/coherent飽和と一般点復元は広い仮定の下で成立する独立な基礎定理。良い一ブロックのモジュライへの適用は条件を明示し、全Poissonの量子化族へ不当に一般化しない。
- `poisson-cubic` は古典正規形・モジュライ、`cubic-quantization` は全Poisson構造の中心三次PBW/AS量子化・同変降下、`nc-cubic-threefold` は三次三様体の独立した相対比較の外部入力。引用する定理と仮定・版を正確に記載する。本稿はB=ambient、A=商、量子化稿は逆という記法差に注意。
- **P0：全O上の比較核・全核型・周期の全係数。** 全 `k≥2,m=0` の全慣性・表示stack同型・残余降下、全基本開の `Φ_pt` とgerbe/関係直線同期を保持する。順序付き実表示では相対非可換積の実核、任意底変更のcompact比較、Picard補正型の相対降下条件と自然な非零位相を得た。次はこれらを全O上の比較へ接続し、Picard型以外も含む核の型と周期写像qの全係数を決定する。固定核型のscalar gerbeを全比較核の分類に拡張しない。全第三根・残る境界・`k=2,m=1`も保持。
- **現在の証明を保持する。** `multiblock_serre.tex`の基底直線を含む相対双対・飽和・Serre、`multiblock_veronese.tex`の全O同値の第三Veronese認識は基礎。`multiblock_intrinsic_quotients.tex`は中心商の純成分・余法加群から`(E,L,σ)`を回復し、可換tensor表示の幾何点のgraded同型類を認識する。個々の全O関手の認識は新しい中心持上げ剛性と全自己同型分類へ接続する。相対Isomはさらに縮めた非空開上で一致するが、全境界や非被約点関手全体の分類とは区別する。
- **全慣性の現在の結論。** `multiblock_center_automorphisms.tex`では飽和冪・剰余加群からAut(D)を分類し、`multiblock_central_rigidity.tex`の負次数Ext消滅・多中心変数の一意持上げを介して全`Aut_gr(A^(3))/G_m=K_k`を証明する。全O認識の有限位数条件の下で全O群もK_k、二ブロックの全慣性は243、中心還元核は全kで自明。二ブロックでは一次中心変形類κ_Cの非消滅も系として証明した。`rO≃O(1)`の根は全分類したが、Oの像を指定しない全第三根や三乗coherenceの標識は含めない。
- **相対認識と残余降下。** `multiblock_relative_recognition.tex`は表示射を一般有限étale・階数一として非空開のstack同型を証明する。`multiblock_scalar_descent.tex`と`multiblock_central_action.tex`はcompact残余・projector・中心作用と同変化を全O開へ降ろす。全境界・全抽象圏変形の認識とは区別する。実表示上のsmooth proper性と元の正則底のcoherent一致は、下記の直接積による独立な証明を用いる。
- **相対直接積の到達範囲。** `multiblock_relative_noncommutative.tex`は滑らかな準射影C基底の順序付き実表示で `Ku_compact(A/S)^Z0≃Perf(∏_S E_i)` の実perfect Morita核と逆を構成する。相対tensor-noetherian性、有限Koszul–Shamash模型、window、perfect Hom、生成性を証明し、共通関係直線と指定周期・因子rotation・coherent中心作用を保つ。準コンパクト・分離的noetherian底への任意導来底変更（非平坦・非被約を含む）は構成済みcompact/Perf模型について成立し、非正則底の全Db(coh)へ読み替えない。元の滑らかなaffine底では全coherent飽和も証明済み。一因子の正則底windowは実際の最高次Koszul syzygy直線を保持して非零二捩れ点にも適用する。
- **同変復元の適用範囲。** `multiblock_equivariant_descent.tex`と`multiblock_point_comparison.tex`の一変数一般点・指定形式模型の結果を保持する。これと独立に `multiblock_noncommutative_product.tex` は全基本実表示の体上直接積、上記の相対節は族の実関手と底変更を与える。`multiblock_rotation_comparison.tex`と下記のPicard節は有限拡大後の通常Ku比較を与え、代数閉体上では全基本点で拡大不要。指定形式核の全jetの代数化や全O上の大域核sectionは別問題。二ブロックのHuによる独立幾何比較も保持。
- **Picard補正型の相対核と位相。** `multiblock_picard_descent.tex`では `α_Pic=Σδ_Ei(p_i)`、因子周期torsor `T_i`、`T=∏T_i`、`D=T/Δμ3` を構成し、中心作用を保つPicard型の核stackを `G_Pic×D`、rotation・指定周期付きのものを `G_Pic×T` と同定する。核Autはperiod標識後もG_mである。比較直線はHodge直線 `λ_i`、周期は `q_i:λ_i³≃O`。`j_i≠0,1728` では `h_i=c6_i/c4_i` と `u_i=q_i^⊗2(h_i³)` により位相を単元類 `γ_i=[u_i]` で表す。これはqの全係数を計算した主張ではない。核α、周期γ、表示gerbeβを区別する。
- **自然な非零位相と比較次数。** Hesse族 `(a,b,c)=(1+d,1,c)` の非零二捩れ境界で、自然な同期 `θ(Ω_H)=3dF_H` によるC((d))上の位相は `γ=[d]`、境界のKummer剰余は+1。独立k変数ではPicard gerbeが既に中立でも位相が独立で、指定Picard補正型の最小比較次数は中心作用付きで `3^(k−1)`、さらにrotation・周期付きで `3^k`。同じ最小次数は有限型函数体 `C(d_1,…,d_k)` 上でも成立する。一般の順序付き実表示の体上上界はそれぞれ `3^(2k−1)` と `3^(2k)` であり、この全上界の最小性やPicard型以外の核の不存在は未証明。
- **次の具体的着手と障害。** `θ:C≃J` は全基本開へ延長済みで、2p=0境界の零因子 `3(a−b)` が上の実際の位相分岐を与える。相対積構成を未解決課題へ戻さず、自然な同期に対するqの一般係数・他の分岐、全O射影商への核stackと核切断の降下、Picard型以外の自己同値による障害の変化を調べる。有限split torsor `Σa_i=1` は `3∤k` のときに限り置換固定点を持ち、表示gerbeを中立化しない。全O上の圏・中心作用の降下と、指定比較核の大域実現を区別する。

- **P1：全intrinsic成分との接続。** 1ブロックの `Z(B)_1` や中心三次torsor、点曲線、次数9/18は多ブロックで自動成立しない。中心核、同変降下、安定化子、相対双対を段階ごとに検証する。古典正規形は `poisson-cubic`、多ブロックPBW量子化は `cubic-quantization`、一般中心三次MF可換復元は本repoの `gdr:thm:generic` が入力。
- **P2：既存の1ブロック比較算術。** 残余位相 `β_n=γ̄_n/[D]` の ΔD 外での分岐、位相体上のscalar index、相対的な強化点型と非分裂比較核は有効な継続課題として保持し、成果・証明・計算を削らない。原稿に証明があること、今回の独立監査・計算・組版、形式証明を区別する。
- 研究方針・研究ノート・公表原稿は現在の成果を再開できる自己完結した現行一式とする。既知結果と新規成果、証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、主要仮定・証明箇所・依存文献・障害を記す。古い経緯や重複、旧ZIP・ログ・中間生成物を保存せず、再現に必要な証明・コード・証明書を保つ。
- `python3 scripts/check_sources.py`、`latexmk -lualatex papers/nc-cubic.tex`、必要な計算証明書を確認し、VS Code/LaTeX Workshop・SyncTeXの設定を保つ。PDFはGit追跡しない。失敗・未実行を成功と報告しない。
- ユーザーが許可した通常commitとmainへのfast-forward pushを再承諾なく行い、15–30分のまとまりで保存する。force push・GitHub Actions追加/実行は禁止し、並行変更を保持する。Libraryへの定常二重保存を行わず、push失敗時の緊急保存のみ例外。既存Libraryファイルを指示なく削除しない。
- **研究の区切りごとにresearch-hubを更新**。先に本repoの方針・ノート・原稿・READMEを保存し、そこからhubの達成点・確実性・依存・核心的障害・次の一手・正本と確認日を更新する。他研究の変更を保持し、hubも通常コミットでmainに保存する。本repoの保存とhub更新の成否を別々に報告する。
