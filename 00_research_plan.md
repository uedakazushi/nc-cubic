# 非可換三次 n-fold：研究方針

2026年11月20日 / v9。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 基本目標と優先順位

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

主公表原稿は `papers/nc-cubic-n-fold.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

良い一ブロック型の O-marked 圏 stack は、強い affine lift の一意性と逆構成により、分解可能な Poisson 対の非空開と同型になった。しかし **trace–Hessian 射が選ぶ三次に対する rotation を保つ Ku 比較は一般には成立しない**（n≢1 mod3 では rotation を指定しない dg Morita 同値もない）。固定入力の残余復元の下で、全次元の明示 Hesse 族に幾何学的一般点の反例があり、周囲 tensor を固定したまま純中心三次だけを補正しても修復できない。さらに混合 Hesse 係数の一般点では、指定 formality 模型の下で marked な形式比較が二次 jet で妨げられる。

この障害に対して、**座標不変な代数的補正 Φ と、固定 formality の全次数の形式 Poisson 対**を構成した。Φ は全 O-同値に降下し、適切な稠密開上で次数9の表現可能な有限 étale 射となり、補正後の active 平面三次は量子側の楕円点曲線に厳密に一致する。分離型 g_λ+G(U) では任意の滑らかな固定 λ に対し、入力Bの下で、この補正後三次と残余圏の比較を有限拡大上で全次数にわたり得る。形式構成では元の support を全次数で保存し、残余三次 W が tensor を形式スカラー倍まで決める。c₂は零、π と a は奇級数、W は偶級数である。

**一般混合係数の五次 tensor と残余四次 potential は決定した。** S(xyz)=1 の規格化で、β=1/60、γ=1/240、π₅=Π_(4I+J−2SF)/240、W₄=Ψ_λ(F)+I/24−J/80 となる。指定中心元の尺度は a₄=S/240、純中心項 G₄=C₄も Hesse 係数の明示式で与えた。従来の Φ は W≡H♯ mod h⁴ を満たすが、各 n≥3 の一般混合係数の非空開に、同じ h と特殊ファイバーの同定を保つ四次の比較障害がある。固定入力の MF・window 比較を適用した marked な Ku 比較にも同じ障害が移る。一般ファイバー上で標識を忘れた非同値を、この有限 jet だけから結論しない。

この四次差を消す **代数的射 Φ^[4]** も構成した。全 O-同値と任意基底変更に両立し、指定中心元に沿って残余三次に mod h⁶、tensor に mod h⁷ で一致する。従来の Φ の次数9・楕円点曲線との厳密な一致・split 族の全次数 MF 比較は、それぞれの適用範囲を保つ。新しい Φ^[4] に同じ一般次数や全次数同値を移してはいない。

次の中心課題は、**一般混合係数の残余射の代数化と、同じ X の Ku 比較同値の核・cocycle の降下**である。有限補正だけでは全次数の同じ三次を得たとはいえないため、内在的な残余復元と代数的な族の構成を結び付ける。必要な高次計算はこの判定を進めるために行い、決定済みの β,γ,W₄,a₄,G₄を再計算課題にしない。開部分のモジュライ同型、相対点復元、Brauer 障害、八次元 Jacobi 頂点の証明・証明書は引き続き保持する。

## 一般性と成分の扱い

- 各既約成分について対象、仮定、非空開、表示による被覆範囲を明記する。一ブロック表示空間の既約性から全 intrinsic O-marked moduli の全成分を扱ったとは結論しない。Poisson 側の唯一の支配成分の結果と、未構成の圏 moduli の成分分類を分ける。
- general は稠密 Zariski 開、very general は可算個の真の閉集合を除いた範囲と区別する。有限個の小位数除外と無限位数条件は異なる。点集合だけから代数的な開 stack や族の射を結論しない。
- 関数体上、有限拡大上、形式完備化上、有限 Artin jet 上の結果を区別する。有限 jet の marked 非同型から一般ファイバーの unmarked 非同型を結論しない。Hesse 例の一般ファイバーの非同型は、別の j 不変量と symmetrizer の証明による。
- 射はまず一般点で構成し、有限表示と必要な降下を確認して稠密開へ広げる。実際の相対 O(1) と偏極類、split ambient と Brauer–Severi ambient を区別する。
- boundary・非被約形式近傍・個別次元の計算は一般構成の具体的な障害を解消するときに優先する。独立成分の一般点や point scheme の楕円成分 E を、この方針を理由に除外しない。

## 固定した入力と現在の到達点

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の固定 commit `eabe601c1341777742964584dde5314c0bcf64a9`（論文A A-v61、論文B B-v59）。三様体の比較対象は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli/tree/6c35d2c84671c2538e61836a6bf3a511392eacce) の固定 commit `6c35d2c84671c2538e61836a6bf3a511392eacce`（v22）。両 repo は読取り専用とする。

入力の全次元 Poisson 正規形・中心量子化・完備 MF 移送・一般点残余復元・Hesse の exact residual potential、および公刊の PBW/CY・星積・wheel 消滅・Kontsevich の二次形式対応・Mori–Smith の点曲線 Hessian 公式、および Banks–Panzer–Pym の harmonic graph weights と Buring の公開データを新規成果に数えない。未公表入力の全証明を独立に再検証したとは主張しない。書誌・参照箇所は `notes/research_notes.md`、確認状態は `notes/validation.md` に置く。

| 基本目標 | 現行稿に証明のある到達点 | 未解決の核心 |
|---|---|---|
| O-marked moduli | 全 O-同値比較と重み付き tails による効果化。滑らかな出力を持つ良い pair では周囲単独の有限安定化子を外せ、滑らかな既約 DM stack Msm を構成。表示 gerbe は n≢1 mod3 で中立、n≡1 mod3 では全非空開上で位数3 | 各 intrinsic 成分の一般対象の局所表示、複数ブロック型、成分性 |
| point scheme | 相対 Pt(A)=E⊔D、中心への八重有限平坦被覆、型 (2,2,2,3) の定常成分。点関手・shift・中心射影を降下し、非空開で埋込み点対応から A 全体を復元。補正 Φ の active 平面切断は元の楕円点曲線に一致 | 各成分の一般点の幾何、点データだけによる像の認識、分岐と自己同型 |
| Poisson moduli | 任意基底で一意な強い lift Π=ι(dH)P。Msm≅Pgood⊂Pdec、次元 binom(n+2,3)+3n−2。既存被約分類の下で一般三次上の全非零 Poisson moduli への開埋込みと唯一の支配成分。Φ は全同値へ降下し、適切な開上で有限 étale 階数9。新しい Φ^[4] も全同値へ降下し、残余三次に mod h⁶、tensor に mod h⁷ で適合 | 一般混合係数の全次数の代数的残余射、各 intrinsic 圏成分との関係、特殊三次上の別成分。Φ^[4] の一般次数は未決定 |
| Kuznetsov 比較 | 固定入力を使う全次元 Hesse 族で X_TH と X_res の一般ファイバー非同型。rotation 保存 dg Morita 同値なし、n≢1 mod3 では rotation なしでも同値なし。同じ Π の全 smooth cubic Casimir に障害。一般混合 π₅,W₄,a₄,G₄を決定し、Φ に対する全次元の四次 marked 障害を証明。Φ^[4] はその障害を除去する有限 jet を与える。split 族の Φ に対する全次数同値は有限拡大上・固定 MF・有限降下・coherent 飽和性の入力付き | 一般混合係数の同じ X への全次数同値、比較核と cocycle の降下、formality 依存性と代数化。n≡1 mod3 の rotation、n=4 の幾何 locus |

補正の主証明は `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction`, `prop:nfm-mixed-fifth-reduction`, `prop:nfm-correction-point-cubic`, `cor:nfm-corrected-residual-jet`, `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir`, `thm:nfm-split-corrected-residual`。四次補正の証明は `papers/sections/fourth_correction.tex` の `prop:nfm-mixed-fifth-explicit`、`lem:nfm-fourth-center-locality`、`thm:nfm-mixed-fourth-potential`、`cor:nfm-fourth-jacobi-class`、`prop:nfm-fourth-uniform-witness`、`cor:nfm-corrected-fourth-obstruction`、`thm:nfm-fourth-algebraic-correction`。既存の主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. 一般混合係数の残余射を代数化し、同じ X への比較核を降下する

最優先。従来の補正は D_P(H)=〈det(D_K²H),P⊗P〉、H♯=H+D_P(H)/24+τ(D_P(H))/12、Φ=(H,P)↦(H♯,P) である。この射の全 O-降下・一般次数9・楕円点曲線との厳密な一致は確立しているが、一般混合係数の残余三次とは四次で marked な差が生じる。従って Φ と残余復元の全次数一致をそのまま証明する方針は採らず、有限補正と全次数の内在的残余射を区別して構成する。

現在の有限係数は、固定 harmonic 模型で

```text
π_h = hΠ_F + h³Π_Hess(F)/24 + h⁵Π_(4I+J−2SF)/240 + O(h⁷),
W_h = F + h²Hess(F)/24 + h⁴(Ψ_λ(F)+I/24−J/80) + O(h⁶),
a_h = h(1+S h⁴/240) + O(h⁷).
```

純中心項も G₄=C₄ と明示され、F=g_λ+Axy+Byz+Czx+Dx+Ey+Hz+G に対して C₄=λ(A³+B³+C³)/60+λ²ABC/40+(2−λ³)(AH+BD+CE)/180+SG/80 である。全 Jacobi 環での四次差は [I]/60+[τ_F(I)]/40+S[τ_F(F)]/80。Fermat active 切断の滑らかな全次元例で値 −1/9 の双対証明書を持つ。証明は `fourth_correction.tex`、有限 graph 計算は `computations/verify_mixed_fifth.py`、中心・Jacobi 恒等式は `computations/verify_fourth_potential.py`。必要な73項・出典・原ファイルの SHA-256 は `computations/data/harmonic_linear_products.json` に保持する。通常の再現は外部データを不要とし、原 weight の照合は `--source-directory` で別に実行できる。手順は README の「再生成」を参照する。

新しい補正は E_P(H)=I_P(H)/60+J_P(H)/240−S_P(H)(H−τ(H))/80+τ(I_P(H))/40、H^[4]=H♯+E_P(H)、P^[4]=(1+S_P(H)/240)P である。出力の滑らかさと係数の可逆性を課した非空開上で、Φ^[4] は代数的かつ全 O-同値に両立し、指定中心元に沿って H^[4]≡W_h mod h⁶、ι(dH^[4])P^[4]≡π_h mod h⁷ を満たす。Φ^[4] の一般次数や全次数の同値はまだ決めていない。

具体的な次の着手は、固定入力Bの `papers/generic_recovery/field_model.tex` の `gcd:thm:field-model` と `generic_descent.tex` の `rog:lem:descent` を読み、三次の定義体、有限拡大上の核、h=0での正則性、全 O-同値に沿うcocycleを分けて点検することである。一般係数の関数体上で、低 rotation 積・量子中心・点対応から残余三次を有限個の代数的データとして回復する方法を比較し、固定 formality の W_h をその完成と同定できるか調べることである。必要なら六次 potential と七次 tensor を共変式空間へ還元し、代数的候補の成立または本質的な高次障害を判定する。高次係数の列挙自体や次元別実験を主目的にせず、有限型の残余射の存在・定義域・内在性を達成基準とする。

形式 tensor は二次 ambient B_h から一意に決まり、中心三次の選択に依存しない。中心逆像は純中心三次を固定し、W_h が tensor を scalar 倍まで全次数で決める。この形式表示 groupoid 上の結果と、有限 h の代数化・全 intrinsic O-moduli の射を区別する。普遍 PBW 模型からの任意の非被約基底への移行は構成済みだが、完備 MF 同値自体の任意基底版は新たに証明していない。

比較核については、同じ X の Ku への同値をまず一般係数の関数体上で構成し、有限表示・有限降下・coherent 飽和性の仮定を個別に確認する。その後に非空開へ広げ、全 O-同値に沿う核の比較と cocycle の整合を示す。split 族の ν(λ,s)=[λ+s²(4+λ³)/12]/[1−s²λ²/4] と Hcorr=g_λ+s²Hess(g_λ)/24+G は、従来の Φ に関する正の全次数比較例として用いる。同値核の有限降下と形式座標変換の代数化は別々に扱い、rotation・指定三次周期・特殊ファイバーの標識の有無を明記する。

### 2. 各 intrinsic 成分の一般対象を覆う表示を調べる

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には入力論文Aの各ブロック型で、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. 一般の点対応からモジュライ内の像を認識する

相対点関手、shift、中心射影、中心三次の復元は構成した。次はその像の有限条件、定常完全交叉の一般の滑らかさ・連結性、八重被覆の分岐、自己同型を調べる。

具体的には埋込み点対応から復元した二次関係・中心直線について、good PBW 条件を判定する条件を整理する。抽象的な D だけで同じ復元ができるとは仮定しない。D の滑らかさは全定理の仮定ではなく、相対完全交叉と正則切断から区別する。相対随伴の determinant 因子と Brauer 障害も保持する。

### 4. 公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・残余比較の障害と修正へ置く。Kontsevich 2001 §2.3 Proposition 6、Mori–Smith Theorems 1.2, 7.2、Lindberg–Pym 2024 Theorem 6.9、Dito・Shoikhet、Banks–Panzer–Pym と Buring の一次資料・公開 graph データとの比較を含め、形式対応・点曲線公式そのものと、本稿の混合 trace 補正・全 O-降下・残余比較を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
