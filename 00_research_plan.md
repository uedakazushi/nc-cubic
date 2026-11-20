# 非可換三次 n-fold：研究方針

2026年11月20日 / v11。再開時はこの文書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 基本目標と優先順位

任意の n≥3 に対して、非可換三次 n-fold の **O-marked moduli の構成、point scheme の研究、Poisson 多様体のモジュライへの射、同じ X の Kuznetsov 成分との比較**を一つの研究として進める。各既約成分の一般点・very general な対象で成り立つ、次元に一様な構造定理を優先する。

O-marked の基本対象は Abel 圏と構造対象の対 (C,O) であり、射は O を保つ同値とする。次数一 shift、次数付き表示、量子化パラメータ、rotation 等は補助データと、本質的に保持する標識とを区別する。表示依存の写像を、その降下を示さず O-marked moduli の射とは呼ばない。

主公表原稿は `papers/nc-cubic-n-fold.tex`。日本語 LuaLaTeX、著者欄は空欄。達成基準は、各対象成分について、一般の族を扱うモジュライと point scheme、Poisson 射の定義域・降下、対応する Kuznetsov 成分の同値を、正確な仮定と十分な証明で結び付けることである。

**良い一ブロック成分の一般部分で、点曲線と残余三次を結び付け、符号を除いた標準的な Poisson 射を構成した。** 固定入力Bの完備 MF・正則底の window・一般点生成性・coherent 飽和性の下で、低 rotation 積の積分直線 L と中心一次作用の annihilator K_res から残余三次 X_res と射影 Poisson 射 Ψ_res を復元する。全 O-同値・任意底変更へ降下し、Brauer–Severi ambient を許す。Ψ_res は支配的・一般相対次元1であり、さらに有限 étale 被覆上で **同じ X_res の Ku** への比較核を得る。

生成元固定再帰を U=0 に制限し、既存の split Hesse 同定を係数空間上の多項式恒等式へ広げると、全 n≥3・一般混合係数で **W_h|_K=b_h J_g、J_g=g+h²Hess(g)/24** を得る。従って量子側の楕円点曲線 E_pt と残余 active 曲線 C_res は同じ j を持つ。これは MF 圏の U=0 への基底変更を仮定する証明ではない。

相対随伴により尺度線束 **T=L⊗det K_res≃λ_res∗** を同定する。有限 Hessian 補正 Φ が与える点曲線の尺度 τ_pt=(H♯|K)⊗P、すなわち標準微分 ω_pt を用い、j≠0,1728 の稠密開で T² の標準非零切断を構成する。これが **Ψ_res^±:M→[Pdec/μ₂]** を定め、全 O-降下・任意底変更・支配性・一般有限性を持つ。適切な非空開では有限 étale 全射である。標準二重被覆 D=Isom_gp(Jac E_pt,Jac C_res) 上では full tensor を得る。平面同型の十八重被覆 I→M と I→D の Jac(E_pt)[3]-torsor、点 shift の平行移動としての移送も構成した。

この進展により、尺度を未構成のまま扱う方針を改め、**自然な符号商射の一般次数・二重被覆の自明性・移送 shift の圏論的意味**を追う。一般次数を Φ の9や二重被覆の2と同一視しない。D は Jacobian 同型を持つが、両 genus-one torsor の同型や比較核そのものを持つとは限らない。点曲線で規格化した tensor は形式 frame で (h/c_h)π_h であり、固定 harmonic 尺度との一致は主張しない。

**比較核の scalar 障害も全次元で制御した。** split 表示 chart で、混合 Euler 数を三次 stabilization の数値型に合わせる比較核が、一般点の有限拡大上に存在する。同型類を整合的に選んだ後の gerbe α は d_nα=0、一般点で ind(α)|d_n、d_n=3^floor((n+1)/2) を満たす。表示 gerbe の分裂も必要な体上では n≡1 mod3 の場合だけ上界に因子3を加える。この bound は自己同値 torsor の同型類を選ぶ第一段階を解決しない。αと表示 Brauer 類βを同一視しない。

固定生成元・固定 h の **実際の harmonic tensor π_h は very general に超越的**であり、この結果も保持する。自然な点規格化はこれと矛盾しない。形式 Nat frame を許した比較と固定 frame の代数性を区別する。選んだ相対 graph flow は中心乗法を厳密に保ち、Ψ_res の形式値は (V(W_h),[π_h])。CF を選んだ trait の滑らかな模型はあるが、正準延長や h=0 での核は未構成である。

既存のモジュライ同型、相対点復元、Brauer 障害、Jacobi スキームと証明書は保持する。trace–Hessian と残余三次の全次元反例、一般次数9の有限補正 Φ、全混合五次 tensor と残余四次項、四次障害と追加補正 Φ^[4] も有効である。Φ、Φ^[4]、Ψ_res、Ψ_res^± は標的と厳密性の異なる構成である。元の目標では、一ブロック一般部分の moduli・点曲線・自然な Poisson 射・被覆上の同じ X への Ku 比較が接続した。**比較核の大域降下、全 intrinsic 成分の一般対象の被覆**は引き続き核心である。

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
| point scheme | 相対 Pt(A)=E⊔D、中心への八重被覆、定常成分の型(2,2,2,3)、埋込み点対応からの A 復元。残余 active 曲線と j が一致。平面同型の十八重被覆、Jacobian 同型の二重被覆と点 shift の移送 | 移送 shift と Ku rotation の関係、二重被覆上の genus-one torsor の差、各成分の像・分岐・自己同型 |
| Poisson moduli | Msm≅Pgood。入力Bの下で射影残余射 Ψ_res と T≃λ_res* を構成。点微分から Ψ_res^± を自然に定義し支配的・一般有限、縮小後有限 étale。標準二重被覆上の full lift。固定 harmonic tensor は very general に超越的 | Ψ_res^± の一般次数・分岐・符号 torsor、同じ微分からの逆構成、各 intrinsic 成分 |
| Kuznetsov 比較 | 固定 MF・window・生成性・飽和性の下で、有限 étale 被覆上の同じ X_res への核。数値型内で同型類を整合させた後、split 一般点の scalar index は 3^floor((n+1)/2) を割る。trait 模型と既存比較障害も保持 | 核の同型類の整合、scalar gerbe の中立性・正確な index、graded center 上の coherent な核、全 intrinsic 成分 |

一般残余射の主証明は `papers/sections/residual_algebraic.tex`。`lem:nfm-dominant-central-family`、`thm:nfm-relative-residual-cubic`、`lem:nfm-relative-center-transport`、`thm:nfm-projective-residual-morphism`、`prop:nfm-projective-residual-dominance`、`thm:nfm-residual-comparison-cover`、`prop:nfm-residual-kernel-descent`、`cor:nfm-residual-good-reduction`、`thm:nfm-normalized-tensor-transcendence` を参照する。

点曲線と自然な尺度の主証明は `papers/sections/residual_point_scale.tex`。`lem:nfm-active-restriction-all-orders`、`prop:nfm-residual-active-point-cubic`、`thm:nfm-residual-point-j`、`prop:nfm-point-residual-isom-cover`、`prop:nfm-scale-hodge-line`、`thm:nfm-canonical-signed-residual-map`、`prop:nfm-point-normalized-jacobian-cover`、`prop:nfm-point-scale-formal-comparison` を参照する。核の数値型・index は `residual_algebraic.tex` の `lem:nfm-kernel-determinant-annihilator`、`lem:nfm-cubic-euler-gcd`、`prop:nfm-kernel-three-primary`、`cor:nfm-generic-kernel-bound`。

補正の主証明は `thm:nfm-algebraic-hessian-correction`, `thm:nfm-correction-degree-nine`, `cor:nfm-mixed-even-jet`, `prop:nfm-active-fifth-covariant`, `cor:nfm-fifth-restriction-obstruction`, `prop:nfm-mixed-fifth-reduction`, `prop:nfm-correction-point-cubic`, `cor:nfm-corrected-residual-jet`, `thm:nfm-residual-formal-poisson`, `cor:nfm-formal-center-casimir`, `thm:nfm-split-corrected-residual`。四次補正の証明は `papers/sections/fourth_correction.tex` の `prop:nfm-mixed-fifth-explicit`、`lem:nfm-fourth-center-locality`、`thm:nfm-mixed-fourth-potential`、`cor:nfm-fourth-jacobi-class`、`prop:nfm-fourth-uniform-witness`、`cor:nfm-corrected-fourth-obstruction`、`thm:nfm-fourth-algebraic-correction`。既存の主証明は `thm:nfm-local-moduli`, `thm:point-trace-hessian`, `thm:poisson-strong-lift`, `thm:poisson-good-open-isomorphism`, `cor:poisson-generic-open-immersion`, `thm:nfm-th-residual-obstruction`, `cor:nfm-casimir-selection-obstruction`, `prop:nfm-relative-residual-second-jet`, `cor:nfm-generic-marked-comparison-obstruction`。相対点復元は `thm:relative-point-nfold`, `thm:point-omarked-descent`, `thm:point-central-recovery`、残余形式認識は `thm:nf-residual-formal`。

保持する補助成果：指定同値の持上げ線束と三捩れ障害・その明示例、八次元の J/I=C(−2)^330 と非分裂平方零構造、横断切片・直和 retract・高次数下界。Koszul 階数上界と N=9,10 の二次階数は既知結果に対応し、新規性を主張しない。証明・厳密計算資産は現行稿に保持する。

## 優先する次の課題と具体的な着手

### 1. 自然な残余射の有限性と同じ X への比較核を詰める

最優先。`residual_point_scale.tex` の平方尺度と二重被覆から再開する。射の存在や active 曲線の j の一致を再び未解決課題に戻さない。

- **一般次数と符号 torsor。** Ψ_res^± の関数体拡大を、低 rotation 積と点微分の二つの Weierstrass 不変量から調べる。D の Kummer 類は b_pt/b_res の平方根であり、modular 正規化 b_res(t²)=1 の被覆と異なる。既存の Φ の次数9を移さず、full lift の標準的な符号選択と有限射の次数を別々に判定する。
- **比較核の同型類。** rotation・指定周期・中心作用を保つ自己同値 stack の作用と、CF 数値型の開閉部分を調べる。P[2m] が低積を変えないため低積だけでは選択できない。点微分・移送 shift が追加の認識を与えるか検討するが、現在は Ku rotation の制限との同定を仮定しない。
- **scalar index の改善。** 現在の bound は同型類を選んだ後の split 一般点で d_n=3^floor((n+1)/2)。試験対象の Euler pairing を増やし、実際の障害の位数・index を絞る。全 O-marked stack への試験対象の降下、表示βとの関係を明示する。HH¹=0、特殊 Hom⁰=k、μ_d band だけから中立性や次数 d の全域有限被覆を推論しない。
- **graded center に沿う比較。** 選んだ graph flow の厳密な中心保存を、比較核の graded center 上の coherent な Morita 線型性・z=0 での導来基底変更へ強められるかを調べる。これが成立して active elliptic MF の試験対象を使えれば、Euler ベクトル(0,3,−3)から次元に依存しない index≤3 を目指せる。現段階は着想であり、低 Nat の中心保存や tensor の U=0 制限だけでは圏の基底変更を証明していない。

尺度は underlying cubic を変えず、既存の有限比較被覆は D に引き戻せる。D 自身に核が降りることは別問題である。trait の選択依存性・核の良い還元は、上の一般的な核の問題に具体的に役立つ場合に扱う。有限補正の公式・純中心項・証明書は保持し、高次 jet 計算の反復自体を主経路にしない。

### 2. 各 intrinsic 成分の一般対象を覆う表示を調べる

現在の Msm は良い一ブロック局所模型を持つ圏族である。Poisson 側の唯一の支配成分を同定したことは、全 intrinsic 圏モジュライの成分分類を意味しない。

具体的には入力論文Aの各ブロック型で、中心一次階数、普遍低次数中心、PBW 平坦性、Serre 軌道と Veronese 復元の仮定を点検する。rank U≥2 が失われる型には中心正則対の議論をそのまま使わない。中心三次の商束が階数一でない場合は P(E)\P(W)→P(E/W) の torsor を用い、一ブロック直線の同型を無条件に流用しない。

### 3. 点対応の幾何を残余射の認識へ使う

楕円点曲線 E_pt と残余 active 曲線 C_res の j の一致、I→D の3捩れ torsor、点 shift の移送を得た。次は、D 上の genus-one torsor の差と次数三偏極を保持した同型の障害を調べる。移送された平行移動から量子表示を回復する条件、残余圏の rotation からその平行移動を認識する条件を明確にする。

並行して、埋込み点対応から復元した二次関係・中心直線について good PBW 条件を有限条件で認識する。定常成分の一般の滑らかさ・連結性、八重被覆の分岐と自己同型も、成分や一般次数の判定に役立つ範囲で調べる。抽象的な定常成分だけから同じ復元ができるとは仮定せず、相対随伴の determinant 因子と Brauer 障害を保持する。

### 4. 公表価値と新規性の確認

中心を一般次元のモジュライ同型・点復元・点微分による自然な残余射・同じ三次への比較とその降下へ置く。Fulton–Olsson の Hodge・modular forms・μ₂-gerbe、Knudsen–Mumford と Lieblich の determinant・twisted sheaf を既知の入力として比較し、曲線比較・支配性・数値型による index bound への適用を区別する。Wang の Theorem 3.3、Hwang の symmetrizer 群、Toën–Vaquié の Lemmas 2.10, 3.25・Corollaries 3.22, 3.24、Bergh–Schnürer の gerbe と Brauer–Severi の分解を一次資料に即して比較する。Kontsevich 2001 §2.3 Proposition 6、Mori–Smith Theorems 1.2, 7.2、Lindberg–Pym 2024 Theorem 6.9、Dito・Shoikhet、Banks–Panzer–Pym と Buring の一次資料・公開 graph データとの比較を含め、形式対応・点曲線公式そのものと、本稿の混合 trace 補正・全 O-降下・残余比較を区別する。未公表入力の主要な依存は、必要な範囲から独立検証を進める。公表に向けて全引用・被引用文献の確認を継続し、既存の個別次元結果は削除せず論理的な配置を維持する。

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
