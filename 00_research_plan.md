# 研究方針：非可換三次超曲面の可換実現と障害

2026-11-25 / v94。正本：本リポジトリ main。まず本書と [AGENTS.md](AGENTS.md) を読み、詳細は [主題別研究ノート](notes/research_notes.md) に進む。

## 1. 研究目標・達成基準（研究固有）

旧全称予想は広い定式化でも、滑らかな proper な圏族による可換三次との変形連結性を課す定式化でも否定された。これを再び一般予想として掲げない。

- どの非可換三次超曲面の Ku が同次元の滑らかな可換三次超曲面の Ku と同値かを、圏の内在的なデータから判定する。
- 実現可能領域・非実現領域・境界を具体的な moduli で決定する。比較先と実核を構成し、必要な標識・中心作用・周期を追跡する。
- 指定クラスでの十分条件と実現構成を目指す。一般の必要十分条件が未完成である間は、適用範囲を明記する。

## 2. 現在の到達点と確実性

| 項目 | 現行原稿に記載した結果・限界 |
|---|---|
| 三次元量子 Fermat 型 | `qfo:thm:obstruction`、`qfo:cor:central-family`。残余圏の HH₁, HH₀ の次元は (1,10)、滑らかな可換三次三様体では (5,2)。固定点・文字射影の有限検算あり。ねじれ orbifold HH の適用を含む圏論証明全体の独立監査は残る。 |
| 五次元反例 | `nfc:thm:counterexample`。変形連結な smooth proper 族で可換実現点と非実現点が共存する。Serre 関手に由来する自然変換環の積を利用。 |
| 内在的必要条件・非閉性 | `nft:prop:triple`、`nft:prop:jacobian-necessary`、`nft:cor:nonclosed-cubic-locus`。七変数の三次式族で滑らかなパラメータ領域から原点を除いた実現 locus。三重積の階数が可換実現点35、原点34。必要条件を一般の十分条件とはしない。 |
| 指定 Sklyanin 表示 | 任意の固定 smooth 標準 Sklyanin 因子の組に対する、指定境界を保つ因子別 PBW・中心持上げの比較。固定 tensor 境界では `ifp:thm:factorization`、`ifp:cor:central-comparison`。全 intrinsic 表示の分類ではない。 |
| 複数中心変数 | `mcb:thm:smooth-locus` の偏極三次による smooth locus の判定と、逐次構成した三次への実 Ku 比較。X_pol と X_it の一致・実核の貼合せは別問題。 |
| Clifford 混合表示 | 一方向九変数、双方向十八変数および二十変数の形式比較。周囲 AS/CY 正則域と残余圏 smooth 域を区別する。比較の稠密開・有限 étale 降下と全係数領域の比較を混同しない。固定 Hesse 切片の十二係数の決定・大域核は未完了。 |
| モジュライと標識 | 全 O 標識、相対積、中心作用、Picard 補正・Kummer 降下等の結果は各表示・標識条件の下で成立。全標識付き核 gerbe の中立化を一般に結論しない。 |

この表は原稿の主張の整理であり、この版での全証明再検証を意味しない。正確な仮定・証明所在は各論文・ノート、独立監査と計算の範囲は [検証範囲](notes/validation.md) を参照する。

## 3. 優先順位と着手方法

以下の P0 → P1 → P2 → P3 を研究の優先順位とする。P0 の重大な未解決依存を残したまま例の追加や公表準備を優先しない。監査で誤りが見つかれば依存する主張を訂正し、必要なら方針を改める。

### P0：五次元・三次元反例の独立監査

1. 五次元：`nfc:thm:counterexample`、`nft:prop:triple`、`nft:prop:jacobian-necessary`、`nft:cor:nonclosed-cubic-locus`。Serre 自己同値の内在性、twisted MF 対角核の sector、自然変換環と乗法、生成性、相対 smooth proper 性を原典と照合する。通常 HH の一定性と三重積の非一定性を区別する。
2. 三次元：`qfo:thm:obstruction` の射影生成・twisted sector・例外対と対角三様体の肯定比較（`ndc:cor:five-diagonal`）を別々に点検する。Baranovsky–Petrov のねじれ HH は定理6。Lin–Zhang の Serre 代数と Perry の HH 底変更の適用条件を確認する。

五次元の Koszul 偶奇・全次数の次元・Serre 公式の仮定の照合は [検証範囲](notes/validation.md) に記録した。非零係数での厚生成と相対残余射影の底変更も主稿で確認した。三次元の射影生成では右加群の準逆と有限次元部分の対応を確認した。全対角三様体では既存の分類と実比較から HH₁ 次元五が可換実現の必要十分条件になる。巡回型で一対の同値を全対角群の合成則付き同値に上げる段階の独立監査を続ける。

### P1：可換実現可能性の内在的特徴付け

- Serre 自然変換環の積・生成次数・Jacobian 完全交叉性・勾配の積分可能性を精密化する。まず具体的 Sklyanin / Clifford 族で必要条件の十分性を検討し、反例があれば追加の内在的不変量を探す。
- 十分性は再構成と実比較核を伴う場合にのみ主張する。通常 HH の一致や smooth proper 変形連結性だけを十分条件としない。入口は [ku-realization.md](notes/ku-realization.md) と [優先検算](computations/README.md)。

### P2：実現可能領域の幾何・実比較核・認識と降下

- Sklyanin / Clifford の肯定的結果を、全 O 標識の認識・表示の被覆に結び付ける。`ifd:thm:residual-a2` の中心チャートと unit/counit defect から残余 smooth locus の境界と核延長を調べる。
- Clifford：固定 Hesse 切片の十二係数を求める。選択した模型の一方向 Shamash の前三中間成分は構成・検算の記録がある（`ifj:prop:third-middle-certificate`）。残る成分と高次 homotopies、実比較核の special retract、四 probe の読出しを進める。計算設計・規格化は [clifford-deformations.md](notes/clifford-deformations.md) に集約する。
- 多中心：`mbl:cor:chart-kernel` の局所核を重なりへ制限し、自己同値・周期位相・Čech coherence を計算する。軸データから全比較を決めない。[mixed-sklyanin.md](notes/mixed-sklyanin.md)。
- 比較核の Kummer 三枝、因子 moduli 上の降下、標識付き核 gerbe・最小次数を調べる。尺度 torsor と核 gerbe を区別する。全 O 認識、相対双対・coherent 飽和、点関手の表示独立性も必要な範囲で検討する。[moduli-descent.md](notes/moduli-descent.md)。
- Clifford 二十変数族の全 smooth 係数への比較と、実現 locus の境界を重点課題とする。

### P3：公表単位の再設計と推敲

- 五次元反例・実現 locus の非閉性・Serre–Jacobian 必要条件を中心とする独立論文を第一候補として検討する。三次元反例は論理的まとまりに応じて同稿または独立稿とする。P0 の監査結果を踏まえて決定し、既存の有効な証明を失わず、重複を避ける。
- point / Poisson スキームの一致・不一致は可換実現から得られる幾何学的情報の限界を示す補助例。成立範囲の検証は [ku-realization.md](notes/ku-realization.md) に置き、独立の最優先予想にしない。
- 精密算術・中心作用・Picard 障害・周期の課題は [moduli-descent.md](notes/moduli-descent.md) を参照し、実現可能性の特徴付けに必要なら優先度を上げる。
- 三稿を各々公表可能な形に推敲する。先行研究と一次資料・適用範囲・論理依存を確認し、反例と構成結果を適切に関連付ける。新規性の網羅的確認・外部査読・形式証明は未完了。

## 4. 正本・依存関係・再現

- 主原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)。別論文 [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) は標識・降下・モジュライ、[mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) は具体的 PBW・混合族・判別・比較核。役割を維持し、証明本文を複製しない。
- 外部研究： [poisson-cubic](https://github.com/uedakazushi/poisson-cubic)、[cubic-quantization](https://github.com/uedakazushi/cubic-quantization)、[nc-cubic-threefold](https://github.com/uedakazushi/nc-cubic-threefold)、[nc-cubic2](https://github.com/uedakazushi/nc-cubic2)。特に `poisson-cubic` の `thm:pg-normal` は commit `9f91efa3465f18219c36c31750f1e66220faeaa7` の `papers/support/papers/sections/poisson_geometry.tex` に固定した未公表入力。適用条件を確認し、公開済み定理と混同しない。本稿では B=ambient、A=中心商、量子化稿では逆。外部 repo は通常読取り専用。詳細は [文献・外部入力](notes/literature.md) と [未解決外部入力](notes/unresolved_external_sources.md)。
- general な稠密開、very general、全固定幾何点、一般点・形式完備化・有限 Artin jet、Brauer–Severi ambient と split ambient、実 O(1) と偏極類を区別する。
- [計算再現](computations/README.md)、[検証範囲](notes/validation.md)。`python3 scripts/check_sources.py`、`python3 scripts/build_papers.py`。LuaLaTeX / latexmk、VS Code の LaTeX Workshop、PDF と SyncTeX の build 出力を保つ。実施不能な検証・認証・環境制約は明記する。

## 5. 共通原則と保存許可（研究固有の計画とは別）

研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。hub は概要・主要到達点・次の一手・優先順位・依存関係・再開先を置き、詳細は対象 repo を正本とする。GitHub 移行前は現行 bundle（組版済み PDF を含む）を承諾なく Library に保存する。移行後は main が正本であり定常二重保存は不要。push 不成功時の緊急保存・別途指示の場合のみ Library を使い、既存 Library ファイルを明示指示なしに削除しない。
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

長時間作業では15–30分を目安に区切り保存する。必要な計算・組版・参照の確認と、対象 repo、Library、hub の保存・反映の成否は別々に報告する。hub では他研究・並行変更を保持し、実質的変化なしの日付更新はしない。主原稿の具体的な正本は `papers/nc-cubic.tex`。独立した別稿は役割を明記し、軽量化を理由に重要な成果や証明を削除しない。
