# 非可換三次 n-fold：二つの予想と研究方針

2026年11月22日 / v46。再開時は本書を最初に読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。正本は `uedakazushi/nc-cubic` の `main`、主公表原稿は [papers/nc-cubic.tex](papers/nc-cubic.tex)（日本語LuaLaTeX、著者欄空欄）。

## 最優先の二つの予想

**Main conjecture（主予想）**：任意の滑らかな非可換三次 n-fold 𝒳 に対して、同じ次元の滑らかな可換三次超曲面 X が存在し、Ku(𝒳)≃Ku(X) となる。

**Second conjecture（当初の全スキーム版・反例あり）**：その同じ可換標的 X と比較同値を、Poisson構造 π が存在して Pt(𝒳)≃Z_X(π) となるように選べる。零点は π の切断としての零スキームであり、非被約構造も含める。

**検証結果：この全スキーム版は成立しない。** `ppz:cor:complex-counterexample` は、関係式と中心元を有理数係数で明示したC上の良い一ブロック三次三様体 A★ を与える。h=1、可換標的のHesse係数は17/9に固定できる。実Sklyanin因子を `esi:prop:factor` で確認し、楕円因子と二つのA₂因子から `csc:cor:fermat` でKu比較を直接構成する。反例の証明に一般点の形式復元・C閉点へのspreadは不要である。A★は主予想を満たすが、同じKuを持つどの滑らかな可換三次とどのPoisson構造を選んでも全point schemeは零スキームと同型でない。非被約な三つの定常点の長さ八局所環を使う反例であり、自然な残余pairでは被約部分は一致する。元の命題を記録し、被約版などを自動的に新予想として採用しない。Ku比較はC上の存在であり、有理係数の表示からQ上の比較核の存在を結論しない。

この具体例の「良い」は点スキームの条件を指す。全O表示stackの全相対入力に属することをh=1で独立に確認したという意味ではなく、それらを反例の証明に用いない。

まず基礎体をC、次元をn≥3とする。主予想は通常のC線型dg Morita同値の存在を求める。第二予想は存在型であり、任意のKu標的・任意のπについての等式ではない。可換対象ではπ=0を許す。point shiftの固定点とPoisson零点を混同しない。

異なる射影表示を持つ対象間の「一致」はスキーム同型として定式化し、射影埋込みを保つ同型、点対応も保つ同型、族での自然な降下は強化問題として区別する。埋込み版には一ブロックの障害があるため、抽象スキーム版の証明で埋込み保存を無断に仮定しない。どの意味が成立・不成立かを明示して検証する。

**「任意」をgenericへ置き換えない。** 全対象の内在的な定義・認識、全O-marked moduliの代数性と表示による被覆は未完成である。少なくとも既存のAS正則周囲代数Bの中心三次商A=B/(w)は、良い開の外も研究対象とする。既知の一ブロック局所型stackの対象を全nc cubicと定義し直して主予想を解いたとはしない。point functorの表現可能性・表示独立性も必要な範囲で解く。主原稿の `conj:nc-main`, `conj:nc-second` が予想の正本である。

## 研究の進め方と達成基準

主予想の解決と、第二のpoint/Poisson対応の正確な成立範囲の決定を最優先にする。O-markedモジュライ、点対応からの復元、残余Poisson射、全O同値・中心作用の認識は、そのための手段として位置付ける。比較次数・位相・全自己同値の精密化だけを進めて、対象範囲や第二予想の検証が広がらない作業を最上位に置かない。

達成基準は、対象範囲と仮定を明記し、同じXについて実際のKu同値と全point schemeの零スキーム比較を証明すること。楕円成分のjの一致、点集合の一致、有限jet、幾何学的一般点だけの同値を全予想の解決と扱わない。一般体上の核降下や全族の大域核sectionは、C上の存在とは別の強化として扱う。

原目標の一般点可換復元・一ブロックモジュライ・満支持型比較は有効な部分結果として保持する。中心変数を加えた分離テンソル型では全固定複素点の可換Ku実現まで進み、定数型混合族にも余有限可換実現を得た。指定二因子では非smooth集合を正確に64係数と決定し、c=0と定常normの全64根のsmooth proper性も証明した。主予想について残る具体的な課題は、既知のsmooth locus全体での可換Ku比較、より一般の混合型、実楕円因子仮定の外の境界、全intrinsic成分の被覆である。全スキーム版の第二予想は上の反例で否定されたため、その局所機構と被約・滑らかな定常成分での成立範囲を調べる。これが現在の優先順位の理由である。方針変更の履歴は蓄積しない。

## 現在の到達点と二つの予想への位置付け

| 対象・結果 | 主予想への到達点 | 第二予想への到達点・限界 | 正本 |
| --- | --- | --- | --- |
| 一般中心三次変形 | 明記した平坦・可換特殊化・滑らかさの仮定の下で、一般係数体の有限拡大上に全coherent Ku比較。C上の全固定点や全内在的対象の表示を与える定理ではない | point scheme全体の零点比較は含まない | `generic_recovery/` の `cft:thm:complete`, `gdr:thm:generic`、[基礎ノート](notes/recovery_foundations.md) |
| 良い一ブロックの共通稠密開 | 同じX_resへの有限被覆上のKu比較、全O降下する残余Poisson射。形式MF・window・飽和の明記した入力を使う | Pt(A)=E⊔D、Dは型(2,2,2,3)。Eと残余active曲線の比較はあるが、全Dの一致は別問題。trace–Hessian対象と残余対象も区別する | `relative_points.tex`, `poisson_morphism.tex`, `residual_algebraic.tex`, `residual_point_scale.tex` |
| 満支持k≥2,m=0の楕円tensor型 | 実際の因子積・rotation比較から可換分離和へのKu同値。明記した実因子仮定の下で同じj・特殊j・非零二捩れも許す | 同じ標的上のπについてPt(A)=Z_X(π)=⊔E_iをスキームとして証明。純成分の近傍で他block座標を単元消去するため非被約試験底にも成立 | `two_block_points.tex`, `multiblock_noncommutative_product.tex`, `multiblock_rotation_comparison.tex`, `point_poisson_split.tex` |
| 中心変数m≥1を持つ分離型、N=3k+m≥5 | 実楕円因子・全a_i≠0・中心三次gのJacobian環有限次元の下で、任意の点曲線方程式f_iに対しX=V(Σf_i+g)への実Ku同値をC上で直接構成 | m=1,g=cu³,c≠0では同じX上でPt=Z=⊔E_i。m≥2では定常完備局所環J[[t_1,…,t_{m−2}]]、length J=8^k。自然な零スキーム側のJ_clと比較 | `central_split_comparison.tex`, `central_split_points.tex` |
| 固定有理係数の一ブロック三様体 A★ | h=1,λ=17/9。指定Ω・THCR商を直接確認し、楕円因子＋二つのA₂因子で全coherent Ku比較 | 局所環J_1とJ_17/9の厳密j不一致、任意supportの局所補題、12点のHessian分類により全πを排除。BMMSで全Ku標的も排除 | `explicit_sklyanin_input.tex`, `point_poisson_obstruction.tex` の `ppz:cor:complex-counterexample`。Mayanskiy・BMMS等の既知入力を明記 |
| S(1,−1,−1)の定数型混合kブロック | 全αで有限中心・PI6・正則中心上Azumaya、任意固定係数で余有限全coherent Ku可換実現。指定二因子は全14節点のNCCR局所形・全simpleを決定し、非smooth集合を正確にV(P64)と証明 | c=0と定常normの全64係数はsmooth proper。全smooth係数での可換Ku比較は未解決。norm点の残余Extは0次1・1次10、既存100simpleのpd5も保持 | `central_mixed_one_variable.tex` の `cmo:thm:fourteen-node-orders`, `cmo:thm:exact-sixty-four`, `cmo:cor:fixed-zero-norm-smooth`, `cmo:cor:cofinite` |
| n≠4の通常Artin変形と開性 | 実smooth proper dg族で可換Ku実現locusがZariski開。étale局所に指定実核を延長 | πとpoint functorを同時に延ばすことは別に必要 | `residual_categories.tex` の `thm:nf-residual-formal` と `geometric_realization_locus.tex` の `grl:thm:open-locus` |

全原稿の証明を今回独立に再検証したという表ではない。今回の追加結果・読解点検・計算・組版・表示・保存の状態は [notes/validation.md](notes/validation.md) に記す。新規性の網羅的確認と外部査読・形式証明は未完了。

## 優先する次の課題と具体的な着手

### P0-M：主予想の存在領域を全対象へ広げる

1. **滑らかな混合族の全係数で可換Ku実現を構成する。** 検査例は `cmo:ex:sixty-four` のk=2,m=1,n=5、α=(1,4,9),(16,25,49)。全14節点の完備局所代数は End_R(R^{⊕a}⊕I^{⊕b})、a+b=6、重複度(1,5),(2,4),(3,3)と決まり、各因子の全simpleを分類した。非等方なΩ切断はA1 skew group模型となり、相対対角の合成とu=0の射影境界の検査から、全coherent圏のsmooth proper性はP64(c)≠0と同値になった。c=0と定常normの64根のsmoothnessは解決済みであり、次の核心はそれらを含む全smooth locusでの実際の可換Ku比較である。まずc=0とnorm根の有限残余模型を取り、既存の比較核をDVRに沿って延長するためのperfect性・生成性と可換三次標的の滑らかさを検査する。開性と基底の連結性だけで全係数へ比較を延ばさない。一般αの例外判定は、中心の節点性とΩ切断の非等方性が失われるlocusから着手する。指定族でのsmoothness判定の完了に合わせた重点移動であり、主予想の全intrinsic対象への拡張は引き続き未解決。二次元の普遍高次作用、character非検出のpd∞例、100simpleのpd5、64定常点の残余Extも有効な入力として保持する。

### P0-S：第二の対応の成立範囲と修正候補

1. **明示反例と直接比較の外部検証・文献比較。** h=1の因子、指定Ω、THCR、分離MF積・Picard補正・周期同期、coherent飽和を入口とする。局所長さ8/埋込み次元3からHessian階数2への帰着、12点の制限三次、全Poisson分類、categorical Torelliが全標的排除の残りの依存である。形式復元とspreadは反例の必要入力ではない。本文の証明・内部読解・厳密計算を、外部査読・形式証明・新規性の確定と区別する。
2. **被約版と滑らかな定常点付き混合型を検証する。** 明示反例の自然pairではPt(A)_red=Z_X(π)_redである。m=1の滑らかなブロックJacobian標的には定常零点がない一方、指定混合族のnormの64根では被約定常点が加わり、そのsourceは全てsmooth properと判定できた。点の残余射影は自己Extが0次1・1次10である。次はこれらの係数で同じKuを持つ可換三次標的を構成し、その全Poisson構造を検査する。自然なブロックJacobian標的との差だけでは、別π・別Xを排除できない。現時点で被約版の反例とも肯定定理とも扱わない。
3. **定常成分が滑らかな場合。** 反例は非被約な定常点を用いる。一般混合係数でのDとD_Hの抽象同型を調べ、偏極・canonical ring等から不一致が被約な例にも残るか検査する。n6ではK_D=O_D(1)を使えるが、二次netからsupportを一意に回復する方法には交代行列の偶奇障害がある。詳細はノート。
4. **分離型の局所障害から相対・大域比較へ。** m≥2ではJとJ_clのgraded同型が全スキーム同型の必要条件であり、m=2では十分条件でもある。m>2の局所自明性から大域積を推論せず、中心socle θによる厚みを調べる。自然射のscheme imageは(g^{s+1})、Fitting supportは(g^{8^k})で異なる。j多重集合による自然pairの障害を、全π・全Ku標的の排除へ拡張できる範囲を検証する。

### P1：二つの予想に必要な認識・降下

全O認識、相対双対・coherent飽和、点関手の表示独立性、Ku比較の実perfect核を必要な範囲で整える。一般点・形式完備化・有限Artin jet・固定幾何点を区別する。全作用付き比較を通常Ku比較の必要条件と誤認しない。二ブロックの指定中心μ3は通常Kuの全自己同値群で非正規である。

### P2：保持する精密算術・分類・公表作業

既存の成果・証明・計算資産は削らない。次の補助課題は、主予想・第二予想への障害を解消する場合に優先度を上げる。詳細は研究ノートと各節が正本である。

- 中心作用の無限共役軌道のGalois降下、同種二因子のPell混合核・反転核の定義体、gerbeとperiod multiplier。全中心同変核判定はk≥3なら同種・CMも含み、k=2では幾何学的非同種の場合に適用する。
- scalar和α=Σδ_iと自然位相Cube(v_i(p_i))の同時最小次数。自然周期q(ω³)=−1/v_ω(p)は決定済み。中心標識を忘れた最小次数の低下は未証明。
- 一ブロック残余位相β_n=γ̄_n/[D]のΔD外の分岐、三次位相体上のind(α)、高次元の任意full classと非分裂の別rotation軌道。q=2で付値1 mod3、強化点型のclass一意性、一般split体の最小三、指定非分裂族の点型九・全型三は保持する。
- Oの像を指定しない全第三根、coherent graded-centerの代数的降下、full rotationから点shiftの認識。有限scalar条件と無限位数条件は区別する。
- 公表上の新規性・一次文献比較。既存MF/THCR/Orlov/Thom–Sebastiani/Picard理論自体と本研究の適用を分ける。必要な証明を公表用主稿に保持し、予想を完成した定理と混同しない。

## 外部入力・再開と再現

古典Poisson正規形・退化とmoduliの正本は [poisson-cubic](https://github.com/uedakazushi/poisson-cubic)、全次元・全Poissonの代数的中心量子化・中心元・同変降下の正本は [cubic-quantization](https://github.com/uedakazushi/cubic-quantization)。三様体固有の全Abel変形・相対比較と独立した点スキーム論文は [nc-cubic-threefold](https://github.com/uedakazushi/nc-cubic-threefold)。具体的な版・commit・定理・適用条件は [notes/research_notes.md](notes/research_notes.md) と参考文献を参照する。外部repoは通常読取り専用。本稿はB=ambient、A=中心商であり、量子化稿では逆の記法を使う。

再開順序は本書 → 適用AGENTS.md → 研究ノートの二予想と該当節 → 主原稿の証明 → 検証範囲。本文に証明がある既存内容は、planへ全文を重複しない。一般性はgeneralな稠密Zariski開、very general、全固定幾何点を区別し、Brauer–Severi ambientとsplit ambient、実O(1)と偏極類も区別する。

基本確認は `python3 scripts/check_sources.py`、`latexmk -lualatex papers/nc-cubic.tex`。必要な計算の入口はREADMEと検証範囲。PDF/SyncTeXはbuild/、VS Code/LaTeX Workshopの既存設定を使う。GitHub反映は通常commitとmainへのfast-forward、認証できない経路を迂回して権限を広げない。保存の成否と数学的確認を分ける。

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
- 研究の区切りごとの生成・検証・保存は、ユーザーの再承諾を求めず実行する許可がある。**正本は指定された `uedakazushi/nc-cubic` の main**。通常の fast-forward 保存を用い、force push、PR、GitHub Actions、PDF/ZIP/中間生成物の追跡は行わない。既存の外部Git管理項目をLibraryへ重複保存せず、GitHub保存が失敗した場合だけLibraryを代替保存先とする。既存Libraryファイルの削除は別の操作であり、明示指示なしに行わない。
- 一式と主要文書に日付・版番号を付け、現行版だけを収録する。配布前に欠落、参照、必要な組版と計算を確認する。生成・検証・保存を別の状態として扱い、実際に確認したことだけを報告する。

研究の区切りでは、先に本repoを保存し、その内容に基づいて research-hub の該当項目を更新する。最新のhubを読み、他研究と並行変更を保持する。対象repoの保存・hub更新・数学的検証は別々に確認し、hubに未反映の項目があれば理由を報告する。詳細な証明・todoは本repoを正本とする。
