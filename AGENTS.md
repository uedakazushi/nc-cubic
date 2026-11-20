# Research instructions — nc-cubic

2026-11-21 / v30。再開時は `00_research_plan.md` を最初に読み、`notes/research_notes.md` と `papers/nc-cubic.tex`、必要な `AGENTS.md` を確認する。研究全体の入口は https://github.com/uedakazushi/research-hub 。

- 正本は `uedakazushi/nc-cubic` の `main`、主論文は `papers/nc-cubic.tex`（日本語LuaLaTeX、本文あり、著者欄空欄）。別論文 `cubic-quantization` は https://github.com/uedakazushi/cubic-quantization へ移行済み。量子化節・原稿・中心元計算・ノートは外部repoで管理し、本文を重複させない。
- このrepoの目標は非可換三次n-foldの可換復元・O-markedモジュライ・残余Poisson射・Ku比較。一般中心三次変形のMF/window/coherent飽和と一般点復元は広い仮定の下で成立する独立な基礎定理。良い一ブロックのモジュライへの適用は条件を明示し、全Poissonの量子化族へ不当に一般化しない。
- `poisson-cubic` は古典正規形・モジュライ、`cubic-quantization` は全Poisson構造の中心三次PBW/AS量子化・同変降下、`nc-cubic-threefold` は三次三様体の独立した相対比較の外部入力。引用する定理と仮定・版を正確に記載する。本稿はB=ambient、A=商、量子化稿は逆という記法差に注意。
- **P0：複数ブロック型への拡張。** 最初は `n=4=3k+m-2`, `k=2,m=0` の二ブロック満support三次四様体。二ブロックの中心三次直線、内在的なブロック分解、全O-marked Abel同値とfpqcモジュライ、一般MF定理の仮定確認後の残余可換三次・Ku比較を研究する。次に `k=2,m=1`（`n=5`）を扱い、一般 `k≥2` を目指す。研究計画の達成基準は `00_research_plan.md` P0にある。新定理として証明済みとは扱わない。
- **P1：全intrinsic成分との接続。** 1ブロックの `Z(B)_1` や中心三次torsor、点曲線、次数9/18は多ブロックで自動成立しない。中心核、同変降下、安定化子、相対双対を段階ごとに検証する。古典正規形は `poisson-cubic`、多ブロックPBW量子化は `cubic-quantization`、一般中心三次MF可換復元は本repoの `gdr:thm:generic` が入力。
- **P2：既存の1ブロック比較算術。** 残余位相 `β_n=γ̄_n/[D]` の ΔD 外での分岐、位相体上のscalar index、相対的な強化点型と非分裂比較核は有効な継続課題として保持し、成果・証明・計算を削らない。原稿に証明があること、今回の独立監査・計算・組版、形式証明を区別する。
- 研究方針・研究ノート・公表原稿は現在の成果を再開できる自己完結した現行一式とする。既知結果と新規成果、証明済み・追加仮定付き・未完成・予想・計算的観察を区別し、主要仮定・証明箇所・依存文献・障害を記す。古い経緯や重複、旧ZIP・ログ・中間生成物を保存せず、再現に必要な証明・コード・証明書を保つ。
- `python3 scripts/check_sources.py`、`latexmk -lualatex papers/nc-cubic.tex`、必要な計算証明書を確認し、VS Code/LaTeX Workshop・SyncTeXの設定を保つ。PDFはGit追跡しない。失敗・未実行を成功と報告しない。
- ユーザーが許可した通常commitとmainへのfast-forward pushを再承諾なく行い、15–30分のまとまりで保存する。force push・GitHub Actions追加/実行は禁止し、並行変更を保持する。Libraryへの定常二重保存を行わず、push失敗時の緊急保存のみ例外。既存Libraryファイルを指示なく削除しない。
- **研究の区切りごとにresearch-hubを更新**。先に本repoの方針・ノート・原稿・READMEを保存し、そこからhubの達成点・確実性・依存・核心的障害・次の一手・正本と確認日を更新する。他研究の変更を保持し、hubも通常コミットでmainに保存する。本repoの保存とhub更新の成否を別々に報告する。
