# 非可換三次 n-fold：研究方針

2026年11月20日 / v6。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 基本目標と優先順位

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

主公表原稿は `papers/nc-cubic-n-fold.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

良い一ブロック型の O-marked 圏 stack は、強い affine lift の一意性と逆構成により、分解可能な Poisson 対の非空開と同型になった。しかし **trace–Hessian 射が選ぶ三次に対する rotation を保つ Ku 比較は一般には成立しない**（n≢1 mod3 では rotation を指定しない dg Morita 同値もない）。固定入力の残余復元の下で、全次元の明示 Hesse 族に幾何学的一般点の反例があり、周囲 tensor を固定したまま純中心三次だけを補正しても修復できない。さらに混合 Hesse 係数の一般点では、指定 formality 模型の下で marked な形式比較が二次 jet で妨げられる。

従って次の中心課題は、**残余圏と整合する Poisson tensor 自体の構成・選択独立性・降下**である。これは同じ X の Ku 比較という目標を維持し、成立しない特定の処方を期待から外す変更である。開部分のモジュライ同型、相対点復元、Brauer 障害は独立に有効である。八次元 Jacobi 頂点の成果・証明書も保持し、次元別の追加計算や boundary の精密化は一般目標の具体的な障害を解消する場合に扱う。

## 一般性と成分の扱い

- 各既約成分について対象、仮定、非空開、表示による被覆範囲を明記する。一ブロック表示空間の既約性から全 intrinsic O-marked moduli の全成分を扱ったとは結論しない。Poisson 側の唯一の支配成分の結果と、未構成の圏 moduli の成分分類を分ける。
- general は稠密 Zariski 開、very general は可算個の真の閉集合を除いた範囲と区別する。有限個の小位数除外と無限位数条件は異なる。点集合だけから代数的な開 stack や族の射を結論しない。
- 関数体上、有限拡大上、形式完備化上、有限 Artin jet 上の結果を区別する。有限 jet の marked 非同型から一般ファイバーの unmarked 非同型を結論しない。Hesse 例の一般ファイバーの非同型は、別の j 不変量と symmetrizer の証明による。
- 射はまず一般点で構成し、有限表示と必要な降下を確認して稠密開へ広げる。実際の相対 O(1) と偏極類、split ambient と Brauer–Severi ambient を区別する。
- boundary・非被約形式近傍・個別次元の計算は一般構成の具体的な障害を解消するときに優先する。独立成分の一般点や point scheme の楕円成分 E を、この方針を理由に除外しない。

## 固定した入力と現在の到達点

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の固定 commit `eabe601c1341777742964584dde5314c0bcf64a9`（論文A A-v61、論文B B-v59）。三様体の比較対象は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli/tree/6c35d2c84671c2538e61836a6bf3a511392eacce) の固定 commit `6c35d2c84671c2538e61836a6bf3a511392eacce`（v22）。両 repo は読取り専用とする。

入力の全次元 Poisson 正規形・中心量子化・完備 MF 移送・一般点残余復元・Hesse の exact residual potential、および公刊の PBW/CY・星積・wheel 消滅を新規成果に数えない。未公表入力の全証明を独立に再検証したとは主張しない。書誌・参照箇所は `notes/research_notes.md`、確認状態は `notes/validation.md` に置く。

| 基本目標 | 現行稿に証明のある到達点 | 未解決の核心 |
|---|---|---|
| O-marked moduli | 全 O-同値比較と重み付き tails による効果化。滑らかな出力を持つ良い pair では周囲単独の有限安定化子を外せ、滑らかな既約 DM stack Msm を構成。表示 gerbe は n≢1 mod3 で中立、n≡1 mod3 では全非空開上で位数3 | 各 intrinsic 成分の一般対象の局所表示、複数ブロック型、成分性 |
| point scheme | 相対 Pt(A)=E⊔D、中心への八重有限平坦被覆、型 (2,2,2,3) の定常成分。点関手・shift・中心射影を降下し、非空開で埋込み点対応から A 全体を復元 | 各成分の一般点の幾何、点データだけによる像の認識、分岐と自己同型 |
| Poisson moduli | 任意基底で一意な強い lift Π=ι(dH)P。Msm≅Pgood⊂Pdec、次元 binom(n+2,3)+3n−2。既存被約分類の下で一般三次上の全非零 Poisson moduli への開埋込みと唯一の支配成分 | 特殊三次上の別成分、全 intrinsic 圏成分との関係、Ku と整合する別の tensor の構成 |
| Kuznetsov 比較 | 固定入力を使う全次元 Hesse 族で X_TH と X_res の一般ファイバー非同型。rotation 保存 dg Morita 同値なし、n≢1 mod3 では rotation なしでも同値なし。同じ Π の全 smooth cubic Casimir に障害。一般混合係数では marked 形式比較の二次障害 | formality 補正 Π または残余低積による Poisson データの構成・代数化・全同値への降下。一般混合係数の unmarked 一般点比較、n≡1 mod3 の rotation、n=4 の幾何 locus |

主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. 残余復元と両立する Poisson tensor を作る

最優先。固定 ambient Π の Casimir 選択だけによる修復は Hesse 族で不可能である。したがって中心補正だけを探索する方針を採らない。

具体的な着手は、指定 formality 模型の formal tensor と residual potential W の組を、h³ の tensor 係数から比較すること。Hesse 族では active potential を g_h から g_λres へ替える候補があるが、一般混合係数では全中心方向と尺度・座標 gauge を追跡する。Hessian jet に規格化した中心元 Ω̃（短い式から h²ABC/6 を引く）について、普遍恒等式 Θ=−2 adj(Hess_active F)、ρ₂F=Hess_active(F)/8 と、残余 potential の W=F+h²Hess_active(F)/24+O(h³) を出発点にする。

別経路として、残余圏の低 rotation 積の核 Q_ρ を計算し、既に存在する可換模型の勾配空間を回復する。そこから rank3 support または Poisson bivector を選ぶ構造が何かを特定する。低積の次元や可積分性だけから圏同値や canonical な tensor を結論しない。

次の達成基準は、一般点または明示した有限拡大上の (X_res,π_res) と K_A≃Ku(X_res) の整合、および選択の変換則。形式級数しか得られない段階では代数的モジュライ射と呼ばず、代数化・有限表示・cocycle と全 O-同値への降下を別に示す。

### 2. 各 intrinsic 成分の一般対象を覆う表示を調べる

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には入力論文Aの各ブロック型で、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. 一般の点対応からモジュライ内の像を認識する

相対点関手、shift、中心射影、中心三次の復元は構成した。次はその像の有限条件、定常完全交叉の一般の滑らかさ・連結性、八重被覆の分岐、自己同型を調べる。

具体的には埋込み点対応から復元した二次関係・中心直線について、good PBW 条件を判定する条件を整理する。抽象的な D だけで同じ復元ができるとは仮定しない。D の滑らかさは全定理の仮定ではなく、相対完全交叉と正則切断から区別する。相対随伴の determinant 因子と Brauer 障害も保持する。

### 4. 公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・残余比較の障害と修正へ置く。Dito・Shoikhet の一次資料との比較を含め、既知の formality そのものと本稿の具体的な補正差を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
- 研究の区切りごとの生成・検証・保存は、ユーザーの再承諾を求めず実行する許可がある。**正本は指定された `uedakazushi/nc-cubic-n-fold` の main**。通常の fast-forward 保存を用い、force push、PR、GitHub Actions、PDF/ZIP/中間生成物の追跡は行わない。既存の外部Git管理項目をLibraryへ重複保存せず、GitHub保存が失敗した場合だけLibraryを代替保存先とする。既存Libraryファイルの削除は別の操作であり、明示指示なしに行わない。
- 一式と主要文書に日付・版番号を付け、現行版だけを収録する。配布前に欠落、参照、必要な組版と計算を確認する。生成・検証・保存を別の状態として扱い、実際に確認したことだけを報告する。

研究の区切りでは、先に本repoを保存し、その内容に基づいて research-hub の該当項目を更新する。最新のhubを読み、他研究と並行変更を保持する。対象repoの保存・hub更新・数学的検証は別々に確認し、hubに未反映の項目があれば理由を報告する。詳細な証明・todoは本repoを正本とする。
