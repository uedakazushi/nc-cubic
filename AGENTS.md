# Research instructions — nc-cubic

2026-11-21 / v36。再開時は `00_research_plan.md` を最初に読み、`notes/research_notes.md` と `papers/nc-cubic.tex`、必要な `AGENTS.md` を確認する。研究全体の入口は https://github.com/uedakazushi/research-hub 。

- 正本は `uedakazushi/nc-cubic` の `main`、主論文は `papers/nc-cubic.tex`（日本語LuaLaTeX、本文あり、著者欄空欄）。別論文 `cubic-quantization` は https://github.com/uedakazushi/cubic-quantization へ移行済み。量子化節・原稿・中心元計算・ノートは外部repoで管理し、本文を重複させない。
- このrepoの目標は非可換三次n-foldの可換復元・O-markedモジュライ・残余Poisson射・Ku比較。一般中心三次変形のMF/window/coherent飽和と一般点復元は広い仮定の下で成立する独立な基礎定理。良い一ブロックのモジュライへの適用は条件を明示し、全Poissonの量子化族へ不当に一般化しない。
- `poisson-cubic` は古典正規形・モジュライ、`cubic-quantization` は全Poisson構造の中心三次PBW/AS量子化・同変降下、`nc-cubic-threefold` は三次三様体の独立した相対比較の外部入力。引用する定理と仮定・版を正確に記載する。本稿はB=ambient、A=商、量子化稿は逆という記法差に注意。
- **P0：自然な可換標的への相対核。** 全 `k≥2,m=0` の非空開で全慣性・表示stack同型・中心作用付きcompact残余の降下、点曲線積、自然な可換三次への射 `Φ_pt` と表示gerbe/関係直線の同期を得た。可換分離和の実表示族上では相対積核も構成済み。次は非可換側の相対核、固定局所型のgerbe類αと固定同期の周期torsor類γの計算。全O一般点・任意固定parameterへの比較は明示的一変数一般点の定理から推論しない。全第三根・境界・`k=2,m=1`も保持。
- **現在の証明を保持する。** `multiblock_serre.tex`の基底直線を含む相対双対・飽和・Serre、`multiblock_veronese.tex`の全O同値の第三Veronese認識は基礎。`multiblock_intrinsic_quotients.tex`は中心商の純成分・余法加群から`(E,L,σ)`を回復し、可換tensor表示の幾何点のgraded同型類を認識する。個々の全O関手の認識は新しい中心持上げ剛性と全自己同型分類へ接続する。相対Isomはさらに縮めた非空開上で一致するが、全境界や非被約点関手全体の分類とは区別する。
- **全慣性の現在の結論。** `multiblock_center_automorphisms.tex`では飽和冪・剰余加群からAut(D)を分類し、`multiblock_central_rigidity.tex`の負次数Ext消滅・多中心変数の一意持上げを介して全`Aut_gr(A^(3))/G_m=K_k`を証明する。全O認識の有限位数条件の下で全O群もK_k、二ブロックの全慣性は243、中心還元核は全kで自明。二ブロックでは一次中心変形類κ_Cの非消滅も系として証明した。`rO≃O(1)`の根は全分類したが、Oの像を指定しない全第三根や三乗coherenceの標識は含めない。
- **相対認識と残余降下。** `multiblock_relative_recognition.tex`は表示射を一般有限étale・階数一として非空開のstack同型を証明する。`multiblock_scalar_descent.tex`と`multiblock_central_action.tex`はcompact残余・projector・中心作用と同変化を全O開へ降ろす。全境界、全抽象圏変形、全coherentとの一致やsmoothnessをこの構成だけから結論しない。
- **同変復元の適用範囲。** `multiblock_equivariant_descent.tex`の分裂方程式・同変核の有限降下、`multiblock_point_comparison.tex`のJacobian tensor/PBW点三次模型を保持。`multiblock_residual_descent.tex`はBFK・Orlov・Elaginの既知定理を全kに適用し、cft/gdrの下で有限拡大後に同変残余圏を曲線積のDbへ比較する。通常Kuは積圏の双対同変化。任意固定parameter、相対特殊点、指定形式核の全jet、大域核sectionへの拡大はしない。二ブロックのHuによる独立な幾何比較も保持。
- **次の具体的着手と障害。** 最大可換商の三次部を介する `θ:C≃J` は明示非空開でのみ確定。`Φ_pt`の自然な同期を保ち、実際の非可換核の局所同型型と `L_P³≃ℓ_tℓ_s^−1` を計算する。核のαと周期のγは別で、period標識後も核のAutはG_m。有限split torsor `Σa_i=1` は `3∤k` のときに限り置換固定点を持ち、共通G_m-gerbeを中立化しない。可換相対核の非平坦底変更は構成済みperfect核の導来引戻しとして述べ、非正則底のcoherent MFへ拡大しない。

- **P1：全intrinsic成分との接続。** 1ブロックの `Z(B)_1` や中心三次torsor、点曲線、次数9/18は多ブロックで自動成立しない。中心核、同変降下、安定化子、相対双対を段階ごとに検証する。古典正規形は `poisson-cubic`、多ブロックPBW量子化は `cubic-quantization`、一般中心三次MF可換復元は本repoの `gdr:thm:generic` が入力。
- **P2：既存の1ブロック比較算術。** 残余位相 `β_n=γ̄_n/[D]` の ΔD 外での分岐、位相体上のscalar index、相対的な強化点型と非分裂比較核は有効な継続課題として保持し、成果・証明・計算を削らない。原稿に証明があること、今回の独立監査・計算・組版、形式証明を区別する。
- 研究方針・研究ノート・公表原稿は現在の成果を再開できる自己完結した現行一式とする。既知結果と新規成果、証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、主要仮定・証明箇所・依存文献・障害を記す。古い経緯や重複、旧ZIP・ログ・中間生成物を保存せず、再現に必要な証明・コード・証明書を保つ。
- `python3 scripts/check_sources.py`、`latexmk -lualatex papers/nc-cubic.tex`、必要な計算証明書を確認し、VS Code/LaTeX Workshop・SyncTeXの設定を保つ。PDFはGit追跡しない。失敗・未実行を成功と報告しない。
- ユーザーが許可した通常commitとmainへのfast-forward pushを再承諾なく行い、15–30分のまとまりで保存する。force push・GitHub Actions追加/実行は禁止し、並行変更を保持する。Libraryへの定常二重保存を行わず、push失敗時の緊急保存のみ例外。既存Libraryファイルを指示なく削除しない。
- **研究の区切りごとにresearch-hubを更新**。先に本repoの方針・ノート・原稿・READMEを保存し、そこからhubの達成点・確実性・依存・核心的障害・次の一手・正本と確認日を更新する。他研究の変更を保持し、hubも通常コミットでmainに保存する。本repoの保存とhub更新の成否を別々に報告する。
