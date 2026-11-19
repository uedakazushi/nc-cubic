# 非可換三次 n-fold：研究方針

2026年11月20日 / v8。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 基本目標と優先順位

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

主公表原稿は `papers/nc-cubic-n-fold.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

良い一ブロック型の O-marked 圏 stack は、強い affine lift の一意性と逆構成により、分解可能な Poisson 対の非空開と同型になった。しかし **trace–Hessian 射が選ぶ三次に対する rotation を保つ Ku 比較は一般には成立しない**（n≢1 mod3 では rotation を指定しない dg Morita 同値もない）。固定入力の残余復元の下で、全次元の明示 Hesse 族に幾何学的一般点の反例があり、周囲 tensor を固定したまま純中心三次だけを補正しても修復できない。さらに混合 Hesse 係数の一般点では、指定 formality 模型の下で marked な形式比較が二次 jet で妨げられる。

この障害に対して、**座標不変な代数的補正 Φ と、固定 formality の全次数の形式 Poisson 対**を構成した。Φ は全 O-同値に降下し、適切な稠密開上で次数9の表現可能な有限 étale 射となり、補正後の active 平面三次は量子側の楕円点曲線に一致する。形式構成では元の support を全次数で保存し、残余三次 W が tensor を形式スカラー倍まで決める。三次のスカラー c₂は零で、π と a は奇級数、W は偶級数である。全混合係数で W≡H♯ mod h⁴、π≡Π♯ mod h⁵ を得る。一方、active 制限 g に対する四次不変式 S を S(xyz)=1 と規格化すると π₅|K=S(g)Π_g/80 であり、固定 h・生成元に関しては代数的 tensor 補正と五次で異なる稠密開がある。さらに全混合 π₅は明示三次共変式 I,J と二つの未評価普遍定数 β,γ へ還元した。分離型 g_λ+G(U) では任意の滑らかな固定 λ に対し、入力Bの下で補正後三次と残余圏の比較を有限拡大上で全次数にわたり得る。

次の中心課題は、**一般混合係数の残余三次の四次項と tensor の五次項を求め、同じ X の Ku 比較と残余同値の降下へ進むこと**である。Φ 自身の非双有理性と、固定規格化での形式 tensor との差が分かったため、残余三次の同定・tensor の尺度・必要な高次補正を分けて調べる。五次の tensor の相違自体は Ku の非同値を意味しない。収束・代数化・選択独立性を済んだことにしない。開部分のモジュライ同型、相対点復元、Brauer 障害、八次元 Jacobi 頂点の証明・証明書は引き続き保持する。

## 一般性と成分の扱い

- 各既約成分について対象、仮定、非空開、表示による被覆範囲を明記する。一ブロック表示空間の既約性から全 intrinsic O-marked moduli の全成分を扱ったとは結論しない。Poisson 側の唯一の支配成分の結果と、未構成の圏 moduli の成分分類を分ける。
- general は稠密 Zariski 開、very general は可算個の真の閉集合を除いた範囲と区別する。有限個の小位数除外と無限位数条件は異なる。点集合だけから代数的な開 stack や族の射を結論しない。
- 関数体上、有限拡大上、形式完備化上、有限 Artin jet 上の結果を区別する。有限 jet の marked 非同型から一般ファイバーの unmarked 非同型を結論しない。Hesse 例の一般ファイバーの非同型は、別の j 不変量と symmetrizer の証明による。
- 射はまず一般点で構成し、有限表示と必要な降下を確認して稠密開へ広げる。実際の相対 O(1) と偏極類、split ambient と Brauer–Severi ambient を区別する。
- boundary・非被約形式近傍・個別次元の計算は一般構成の具体的な障害を解消するときに優先する。独立成分の一般点や point scheme の楕円成分 E を、この方針を理由に除外しない。

## 固定した入力と現在の到達点

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の固定 commit `eabe601c1341777742964584dde5314c0bcf64a9`（論文A A-v61、論文B B-v59）。三様体の比較対象は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli/tree/6c35d2c84671c2538e61836a6bf3a511392eacce) の固定 commit `6c35d2c84671c2538e61836a6bf3a511392eacce`（v22）。両 repo は読取り専用とする。

入力の全次元 Poisson 正規形・中心量子化・完備 MF 移送・一般点残余復元・Hesse の exact residual potential、および公刊の PBW/CY・星積・wheel 消滅・Kontsevich の二次形式対応・Mori–Smith の点曲線 Hessian 公式を新規成果に数えない。未公表入力の全証明を独立に再検証したとは主張しない。書誌・参照箇所は `notes/research_notes.md`、確認状態は `notes/validation.md` に置く。

| 基本目標 | 現行稿に証明のある到達点 | 未解決の核心 |
|---|---|---|
| O-marked moduli | 全 O-同値比較と重み付き tails による効果化。滑らかな出力を持つ良い pair では周囲単独の有限安定化子を外せ、滑らかな既約 DM stack Msm を構成。表示 gerbe は n≢1 mod3 で中立、n≡1 mod3 では全非空開上で位数3 | 各 intrinsic 成分の一般対象の局所表示、複数ブロック型、成分性 |
| point scheme | 相対 Pt(A)=E⊔D、中心への八重有限平坦被覆、型 (2,2,2,3) の定常成分。点関手・shift・中心射影を降下し、非空開で埋込み点対応から A 全体を復元。補正 Φ の active 平面切断は元の楕円点曲線に一致 | 各成分の一般点の幾何、点データだけによる像の認識、分岐と自己同型 |
| Poisson moduli | 任意基底で一意な強い lift Π=ι(dH)P。Msm≅Pgood⊂Pdec、次元 binom(n+2,3)+3n−2。既存被約分類の下で一般三次上の全非零 Poisson moduli への開埋込みと唯一の支配成分。Hessian–trace 補正 Φ は全同値へ降下し、適切な開上で有限 étale 階数9（商 stack の次数） | 特殊三次上の別成分、全 intrinsic 圏成分との関係、残余三次の高次比較、tensor の尺度と高次補正 |
| Kuznetsov 比較 | 固定入力を使う全次元 Hesse 族で X_TH と X_res の一般ファイバー非同型。rotation 保存 dg Morita 同値なし、n≢1 mod3 では rotation なしでも同値なし。同じ Π の全 smooth cubic Casimir に障害。一般混合係数の二次障害は Φ で除去。固定 formality では π_h=a_hι(dW_h)P、c₂=0 と偶奇性により W≡H♯ mod h⁴。π₅の active 制限は S(g)Π_g/80。split 族は任意の滑らかな固定 λ に対し補正後三次との全次数同値を有限拡大上で得る（MF・有限降下・coherent 飽和性の入力付き） | 一般混合係数の W₄・π₅、形式 scalar と formality 依存性、代数化と残余同値の全 O-降下。n≡1 mod3 の rotation、n=4 の幾何 locus |

補正の主証明は `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction`, `prop:nfm-mixed-fifth-reduction`, `prop:nfm-correction-point-cubic`, `cor:nfm-corrected-residual-jet`, `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir`, `thm:nfm-split-corrected-residual`。既存の主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. 一般混合係数で補正と残余復元を全次数比較する

最優先。代数的補正は D_P(H)=〈det(D_K²H),P⊗P〉、C_P(H)=D_P(H)/24+τ(D_P(H))/12、H♯=H+C_P(H) である。Φ=(H,P)↦(H♯,P) の射と全 O-降下は構成済み。量子側の楕円点曲線が H♯|K に等しいことも厳密である。ただしこの一致は全三次の残余復元を決めない。

まず一般混合係数で W_res=F+h²Hess_active(F)/24+h⁴W₄+O(h⁶) の W₄を求める。生成元固定再帰 `eq:nfm-normalized-tensor-recursion`、π_h=a_hι(dW_h)P、active 制限 π₅|K=S(g)Π_g/80 を併用し、正の中心次数を持つ五次 tensor を Q₅=S(g)F/80+β(I−S(g)F)+γ(J−S(g)F) に還元した結果を使い、まず β,γ を決める。I,J は `prop:nfm-mixed-fifth-reduction` の ε縮約で明示してある。独立な二つの混合 Taylor jet で正規化再帰を評価すれば足り、中央変数の個数は増やす必要がない。Hessian 正規化中心元に対して H♯=F+h²Hess_active(F)/24+h⁴τ_F(Ψ_λ(F)) は厳密なので、W₄=Q₅−a₄F+G₄(U) の純中心項 G₄を中心逆像から求める。全 Jacobi 環では [F]=0 なので、差の類は β[I]+γ[J]+[G₄−τ_F(Ψ_λ(F))] となり、尺度 a₄の評価はこの障害判定には不要である。c₂と奇数次 potential は既に消滅が証明され、再計算課題ではない。低次の一般係数恒等式を優先し、各次元の個別実験を主経路にしない。

形式 tensor は二次 ambient B_h だけから一意に定まり、中心三次の選択に依存しない。中心逆像は純中心三次を固定し、W_h が tensor を scalar 倍まで全次数で決める。これは固定 formality・固定 h の形式表示 groupoid に対する構成であり、有限 h の代数化や全 intrinsic O-moduli の射ではない。被約有限型の普遍 PBW 模型から任意の非被約基底へ移せるが、完備 MF 同値そのものの任意基底版まで新たに証明したとはしない。

split 族での ν(λ,s)=[λ+s²(4+λ³)/12]/[1−s²λ²/4] と Hcorr=g_λ+s²Hess(g_λ)/24+G は正の比較例となる。ここで得た同値核の有限降下と、形式座標変換の代数化を区別する。一般混合係数への拡張では、同じ X の Ku 比較、rotation・指定三次周期、同値核の cocycle を達成基準とする。低 rotation 積による勾配回復は、形式構成の内在性と降下を検証する別経路として保持する。

### 2. 各 intrinsic 成分の一般対象を覆う表示を調べる

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には入力論文Aの各ブロック型で、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. 一般の点対応からモジュライ内の像を認識する

相対点関手、shift、中心射影、中心三次の復元は構成した。次はその像の有限条件、定常完全交叉の一般の滑らかさ・連結性、八重被覆の分岐、自己同型を調べる。

具体的には埋込み点対応から復元した二次関係・中心直線について、good PBW 条件を判定する条件を整理する。抽象的な D だけで同じ復元ができるとは仮定しない。D の滑らかさは全定理の仮定ではなく、相対完全交叉と正則切断から区別する。相対随伴の determinant 因子と Brauer 障害も保持する。

### 4. 公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・残余比較の障害と修正へ置く。Kontsevich 2001 §2.3 Proposition 6、Mori–Smith Theorems 1.2, 7.2、Lindberg–Pym 2024 Theorem 6.9、Dito・Shoikhet の一次資料との比較を含め、形式対応・点曲線公式そのものと、本稿の混合 trace 補正・全 O-降下・残余比較を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
