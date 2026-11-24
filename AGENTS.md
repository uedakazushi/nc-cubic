# Research instructions — nc-cubic

2026-11-25 / v94。

## 再開と研究の現在地

- 研究の優先順位は **P0：反例の独立監査 → P1：可換実現の内在的特徴付け → P2：実現領域・比較核・降下 → P3：公表単位の再設計と推敲** とする。詳細・着手方法は `00_research_plan.md` を正本とする。

- [research-hub](https://github.com/uedakazushi/research-hub) の nc-cubic 項目、`00_research_plan.md`、本書、`notes/research_notes.md` を読む。中心課題は可換実現可能なクラスの内在的特徴付け。旧全称予想は三次元・五次元の反例により否定された。
- まず三次元のねじれ HH と五次元の Serre 自然変換環の圏論的同定を独立に監査する。因子別 PBW、Clifford 比較は各定理の仮定を維持する。周囲正則域、残余 smooth locus、実比較核、有限検算を区別する。
- 原稿の主張、独立読解、厳密計算、形式証明、新規性、組版を区別する。仮定・証明の所在・未完部分を明記し、一次資料を確認する。

## 構成・再現

- 正本は main。本文を持つ主原稿は `papers/nc-cubic.tex`、独立稿は `papers/cubic-moduli-descent.tex` と `papers/mixed-sklyanin-cubics.tex`。日本語 LuaLaTeX・著者欄空欄。役割を保ち、証明を重複しない。
- 方針は目標・優先順位、README は入口・再生成、`notes/research_notes.md` は主題別ノートの入口、`notes/validation.md` は実施した検証範囲、`computations/README.md` は実行手順。詳細な数学は論文と主題別ノートに保持する。旧稿、旧版 ZIP、会話、作業ログ、重複記述、バックアップ、中間生成物を現行一式に入れない。必要な証明・反例・計算入力・証明書は削らない。
- `python3 scripts/check_sources.py`、必要な検算、`python3 scripts/build_papers.py` を repo ルートで実行する。既存 latexmk / VS Code 設定を維持し PDF・SyncTeX を `build/` に出す。新規原稿・組版環境は research-hub のテンプレート・設定を参照。改名・移動時は input・root 指定・文献・相互参照・README・方針・ビルド設定を整合させる。
- 参照切れ、必要な計算・組版を確認する。実施不能な確認は理由を記す。資料整理を数学的証明の再検証とは扱わない。

## 保存と hub 更新（許可済み）

- 研究の区切りで方針・ノート・論文・README・必要な再現資産を更新し、通常 commit で main に push する。承諾不要。長時間作業では15–30分を目安に保存し、並行変更を保持する。force push・GitHub Actions の追加／起動は行わない。PDF は原則 Git に含めない。
- main が正本なので定常 Library 二重保存・ZIP は不要。push 不成功時の緊急保存、別途指示の場合のみ Library を使う。既存 Library ファイルは明示指示なしに削除しない。
- 対象 repo を保存・確認した後、research-hub 最新を読み、nc-cubic の主要到達点・確実性・核心障害・次の一手・依存・正本・実資料確認日を更新する。詳細な証明・todo を hub に複製しない。実質的変化なしの日付更新は不要。他研究・並行変更を保持し、通常 commit で hub main に反映する。
- repo 保存・hub 更新・生成・計算・組版・数学的検証を別々に確認・報告する。hub 更新が不成功でも成果は先に保存し、未反映事項と理由を報告する。
