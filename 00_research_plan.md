# 非可換三次 n-fold：研究方針

2026年11月20日 / v10。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 基本目標と優先順位

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

主公表原稿は `papers/nc-cubic-n-fold.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

**一般混合係数について、残余三次と射影 Poisson 対の代数的な射を稠密開上に構成した。** 固定入力Bの完備 MF・正則底の window・一般点生成性・coherent 飽和性の下で、低 rotation 積の核 Q とその積分核 L から三次方程式の直線を復元する。中心一次作用 U→V_ρ の annihilator K と合わせた Ψ_res は全 O-同値へ降下し、Brauer–Severi ambient を許す、尺度を忘れた Poisson moduli への支配射となる。適切な開で滑らか、相対次元は全 n≥3 で1である。さらに有限 étale 被覆上で、この射が選んだ **同じ X_res の Ku** と非可換残余圏の同値を得る。方程式の直線の復元、族への拡張、被覆上の核、元の stack への核の降下を分ける。

生成元固定模型からの **相対 graph flow は中心一次作用を厳密に保つ**。従って上の射の一般形式像は (V(W_h),[π_h]) に全次数で一致する。次数一空間の比較には形式行列を許す。一変数 trait では、この形式比較から格子を降ろすことで h=0 まで滑らかな三次模型も得るが、その選択の正準性、核の h=0 への延長、大域 boundary 射は主張しない。

**固定生成元・固定 h の実際の tensor π_h は、各 n≥3 の very general な滑らかな係数で代数的でない。** 普遍再帰の各係数の多項式性と、xyz での厳密な log((2+h)/(2−h)) を用い、有界次数の代数関係 locus がそれぞれ真の閉集合であることを証明した。有限 jet の不一致を全次数へ外挿した結果ではない。この障害は固定 frame、または代数的に関係する frame に対するものであり、任意の形式 Nat frame を介した intrinsic な尺度切断との一致や、あらゆる尺度付きモジュライ射の不存在は結論しない。

次の最優先は **比較核の同型類と scalar 二 cocycle の大域降下、および尺度線束 T=L⊗det K の標準的な切断**である。同値全体は全自己同値 stack の torsor であり、同型類を選んだ後で初めて scalar gerbe の問題になる。表示 gerbe の Brauer 類 β とこの kernel gerbe を同一視しない。元の目標のうち、良い一ブロック成分の一般部分における方程式・射影 Poisson 射・同じ三次への被覆上の Ku 比較は得たが、尺度、核の大域降下、全 intrinsic 成分の被覆は残っている。

既存のモジュライ同型、相対点復元、Brauer 障害、Jacobi スキームの証明と計算資産は保持する。trace–Hessian 三次への比較には全次元の Hesse 反例があり、その障害も保持する。有限 Hessian 補正 Φ は全 O-降下・一般次数9・楕円点曲線との厳密な一致を持つ。混合五次定数 β=1/60, γ=1/240、残余四次項 W₄=Ψ+I/24−J/80 と marked な四次障害は決定済みであり、追加補正 Φ^[4] は三次に mod h⁶、tensor に mod h⁷ で一致する。これらの有限処方と、新しい内在的な Ψ_res は別の射である。Φ の次数9・点曲線公式を他の射へ移さない。

## 一般性と成分の扱い

- 各既約成分について対象、仮定、非空開、表示による被覆範囲を明記する。一ブロック表示空間の既約性から全 intrinsic O-marked moduli の全成分を扱ったとは結論しない。Poisson 側の唯一の支配成分の結果と、未構成の圏 moduli の成分分類を分ける。
- general は稠密 Zariski 開、very general は可算個の真の閉集合を除いた範囲と区別する。有限個の小位数除外と無限位数条件は異なる。点集合だけから代数的な開 stack や族の射を結論しない。
- 関数体上、有限拡大上、形式完備化上、有限 Artin jet 上の結果を区別する。有限 jet の marked 非同型から一般ファイバーの unmarked 非同型を結論しない。Hesse 例の一般ファイバーの非同型は、別の j 不変量と symmetrizer の証明による。
- 射はまず一般点で構成し、有限表示と必要な降下を確認して稠密開へ広げる。実際の相対 O(1) と偏極類、split ambient と Brauer–Severi ambient を区別する。
- boundary・非被約形式近傍・個別次元の計算は一般構成の具体的な障害を解消するときに優先する。独立成分の一般点や point scheme の楕円成分 E を、この方針を理由に除外しない。

## 固定した入力と現在の到達点

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の固定 commit `eabe601c1341777742964584dde5314c0bcf64a9`（論文A A-v61、論文B B-v59）。三様体の比較対象は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli/tree/6c35d2c84671c2538e61836a6bf3a511392eacce) の固定 commit `6c35d2c84671c2538e61836a6bf3a511392eacce`（v22）。両 repo は読取り専用とする。

入力の全次元 Poisson 正規形・中心量子化・完備 MF 移送・一般点残余復元・Hesse の exact residual potential、および公刊の PBW/CY・星積・wheel 消滅・Kontsevich の二次形式対応・Mori–Smith の点曲線 Hessian 公式、Banks–Panzer–Pym の harmonic graph weights と Buring の公開データ、Wang・Hwang の勾配復元、Toën–Vaquié の perfect 核の有限表示・同値 locus の開性を新規成果に数えない。未公表入力の全証明を独立に再検証したとは主張しない。書誌・参照箇所は `notes/research_notes.md`、確認状態は `notes/validation.md` に置く。

| 基本目標 | 現行稿に証明のある到達点 | 未解決の核心 |
|---|---|---|
| O-marked moduli | 全 O-同値比較と重み付き tails による効果化。滑らかな出力を持つ良い pair では周囲単独の有限安定化子を外せ、滑らかな既約 DM stack Msm を構成。表示 gerbe は n≢1 mod3 で中立、n≡1 mod3 では全非空開上で位数3 | 各 intrinsic 成分の一般対象の局所表示、複数ブロック型、成分性 |
| point scheme | 相対 Pt(A)=E⊔D、中心への八重有限平坦被覆、型 (2,2,2,3) の定常成分。点関手・shift・中心射影を降下し、非空開で埋込み点対応から A 全体を復元。補正 Φ の active 平面切断は元の楕円点曲線に一致 | 各成分の一般点の幾何、点データだけによる像の認識、分岐と自己同型 |
| Poisson moduli | Msm≅Pgood⊂Pdec と唯一の支配成分の一般開。固定入力Bの下で低 rotation 積・中心作用による代数的 Ψ_res を構成し、全 O-降下・支配性・一般相対次元1・選んだ形式 Poisson 直線との全次数一致を証明。尺度の lift は T=L⊗det K の非零切断。固定 frame の tensor は very general に超越的 | 標準的な尺度切断とその形式比較、各 intrinsic 成分、特殊三次上の別成分。有限補正 Φ^[4] の一般次数 |
| Kuznetsov 比較 | 固定 MF・window・一般点生成性・coherent 飽和性の下で、一般混合係数の稠密開の有限 étale 被覆上に、同じ X_res への比較核を構成。局所 rotation・指定周期を保存。形式比較を選んだ trait の滑らかな三次模型も存在。旧 trace–Hessian と有限補正の比較障害・split 族の正の比較は保持 | 比較核の同型類の整合と scalar 二 cocycle、表示 gerbe との関係、正準的な trait 延長、全 intrinsic 成分 |

一般残余射の主証明は `papers/sections/residual_algebraic.tex`。`lem:nfm-dominant-central-family`、`thm:nfm-relative-residual-cubic`、`lem:nfm-relative-center-transport`、`thm:nfm-projective-residual-morphism`、`prop:nfm-projective-residual-dominance`、`thm:nfm-residual-comparison-cover`、`prop:nfm-residual-kernel-descent`、`cor:nfm-residual-good-reduction`、`thm:nfm-normalized-tensor-transcendence` を参照する。

補正の主証明は `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction`, `prop:nfm-mixed-fifth-reduction`, `prop:nfm-correction-point-cubic`, `cor:nfm-corrected-residual-jet`, `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir`, `thm:nfm-split-corrected-residual`。四次補正の証明は `papers/sections/fourth_correction.tex` の `prop:nfm-mixed-fifth-explicit`、`lem:nfm-fourth-center-locality`、`thm:nfm-mixed-fourth-potential`、`cor:nfm-fourth-jacobi-class`、`prop:nfm-fourth-uniform-witness`、`cor:nfm-corrected-fourth-obstruction`、`thm:nfm-fourth-algebraic-correction`。既存の主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. 同じ X の比較核と Poisson 尺度を大域化する

最優先。Ψ_res は既存一ブロック成分の非空稠密開に構成済みである。再開時は `residual_algebraic.tex` の低積、中心作用、重み、有限被覆の定理から読む。一般点の存在だけを再び目標にしたり、既に決定した有限 jet の計算を反復したりしない。

- **比較核の同型類。** rotation・指定周期・中心作用を保つ自己同値 stack の作用を調べ、被覆上の核の同型類を全 O-同値に沿って整合させる条件を得る。P[2m] は同じ低積を保つため、低積だけで核の一意性を主張できない。Toën–Vaquié の Corollaries 3.22, 3.24 と実際の核の Morita endomorphism を出発点とする。追加の標識を採用するなら、その必要性と元の O-marked 目標への影響を明記する。
- **scalar 二 cocycle。** 同型類が整合した後に、重なり同型の三重積 c_ijk を構成し、kernel gerbe の類を調べる。既存の表示 gerbe β と同じとは仮定せず、determinant、周期、trace の具体的な比較写像から関係を検討する。HH¹=0 はこの消滅を意味しない。
- **Poisson の尺度。** T=L⊗det K の quotient chart 上の遷移を求め、量子中心直線・Serre pairing・周期に由来する標準切断があるかを判定する。T^× が full tensor の lift を分類することは証明済み。固定 frame の π_h の超越性から intrinsic な切断の不存在を推論せず、CF の形式 frame も含めて比較する。
- **trait 模型。** 選んだ CF から格子を降ろすと滑らかな模型はある。次にその選択依存性、全 O-同値への整合、比較核の良い還元を調べる。相対 Hochschild 模型の h=0 での perfect 性を暗黙に仮定しない。

有限補正の公式・純中心項・証明書は `fourth_correction.tex`、研究ノートと README にまとめてある。Φ、Φ^[4]、Ψ_res は標的・厳密性・次数の異なる構成である。必要な高次計算は尺度または核の降下の具体的な判定のために行う。

### 2. 各 intrinsic 成分の一般対象を覆う表示を調べる

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には入力論文Aの各ブロック型で、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. 一般の点対応からモジュライ内の像を認識する

相対点関手、shift、中心射影、中心三次の復元は構成した。次はその像の有限条件、定常完全交叉の一般の滑らかさ・連結性、八重被覆の分岐、自己同型を調べる。

まず、相対 graph flow の中心線型性を U=0 への基底変更へ適用し、量子側の楕円点曲線 E と残余三次の active 切断 X_res∩P(K_res) の関係を調べる。三次曲線の同型、次数三偏極、shift の対応は別々に確認し、Φ の既知の点曲線公式を Ψ_res へ無条件に移さない。並行して、埋込み点対応から復元した二次関係・中心直線について、good PBW 条件を判定する条件を整理する。抽象的な D だけで同じ復元ができるとは仮定しない。D の滑らかさは全定理の仮定ではなく、相対完全交叉と正則切断から区別する。相対随伴の determinant 因子と Brauer 障害も保持する。

### 4. 公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・代数的な残余射・同じ三次への比較とその降下へ置く。Wang の Theorem 3.3、Hwang の symmetrizer 群、Toën–Vaquié の Lemmas 2.10, 3.25・Corollaries 3.22, 3.24、Bergh–Schnürer の gerbe と Brauer–Severi の分解を一次資料に即して比較する。Kontsevich 2001 §2.3 Proposition 6、Mori–Smith Theorems 1.2, 7.2、Lindberg–Pym 2024 Theorem 6.9、Dito・Shoikhet、Banks–Panzer–Pym と Buring の一次資料・公開 graph データとの比較を含め、形式対応・点曲線公式そのものと、本稿の混合 trace 補正・全 O-降下・残余比較を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
