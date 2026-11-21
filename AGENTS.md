# Research instructions — nc-cubic

2026-11-21 / v43。研究全体の入口は https://github.com/uedakazushi/research-hub 。再開時はhubの該当項目、本repoの `00_research_plan.md`、このAGENTS、研究ノートと必要な証明を読む。

## 最優先目標

- **Main conjecture:** 任意の滑らかなnc cubic 𝒳について、同じ次元の滑らかな可換cubic XとKu(𝒳)≃Ku(X)が存在する。
- **Second conjecture:** その同じXを、Poisson構造πとスキーム同型Pt(𝒳)≃Z_X(π)が存在するように選べる。非被約構造を含み、point shiftの固定点とは区別する。
- まずC上、n≥3の存在を最優先とする。「任意」をgenericや既知の良い表示へ弱めない。全intrinsic対象の定義・認識と表示被覆は未完成として明記する。point functorの表現可能性・表示独立性も必要な範囲で検証する。
- 主原稿の `conj:nc-main`, `conj:nc-second` が元の定式化の正本。第二の全スキーム版は `ppz:cor:complex-counterexample` の固定された複素代数A★（h=1、点曲線のHesse係数λ=17/9）で否定された。実因子の確認 `esi:prop:factor` と中心A2因子の直接比較 `csc:cor:fermat` により可換Ku標的をC上で構成し、形式復元・一般点のspreadをこの反例の入力にしない。被約版などの修正候補は別に検証し、自動採用しない。同じ射影埋込みを保つ版、point correspondence、全族の自然な降下、一般体上の核降下、中心作用・rotation・周期の標識は別の強化問題である。予想に反する可能性のある例も検証し、都合のよい定式化へ黙って変更しない。
- 次のP0は、可換Ku実現locusの境界と未被覆成分、中心変数が二次関係にも現れる真の混合型のsmoothnessとKu比較、定常成分の局所環によるpoint/Poisson対応の成立範囲である。中心変数を持つ分離型の直接比較と、真の混合型で得た点関手・有限normを区別する。比較次数・周期・全自己同値の精密化は補助課題へ移す。既存の有効な証明・例・計算は保持する。

## 現行結果の範囲と研究上の注意

- 一般中心三次変形のMF/window/coherent飽和・一般点復元は、一ブロックより広い明記した仮定で成立する基礎定理。全固定点・全抽象圏の表示定理ではない。
- `point_poisson_split.tex` はm=0の楕円tensor表示について、同じ可換分離和へのKu比較とPt=Poisson零スキームを結合する。存在版は実因子・固定点なしの点グラフを仮定し、j相異性・特殊j除外・2p≠0を必要としない。自然なθによる標的は基本開に限定する。θの二捩れ境界退化を、何らかの可換標的の不存在と混同しない。
- `central_split_comparison.tex` の `csc:thm:comparison` は、C上、k,m≥1、N=3k+m≥5、全a_i≠0、実楕円因子S_i/(Ω_i)=B(E_i,L_i,t_{p_i})、原点だけにcritical pointを持つ中心三次gについて、A=((⊗S_i)⊗C[U])/(Σa_iΩ_i+g)とX=V(Σf_i+g)の全coherent Ku同値を直接構成する。f_iは同じ偏極曲線E_iの任意の非零方程式でよい。点グラフの固定点なしはKu比較自体の仮定ではない。中心因子の有限MF、周期付きPicard補正、二重同変化、smoothness後のcoherent飽和の順序を保つ。Fermat中心和は `csc:cor:fermat` のA2模型だけで比較できる。
- `central_split_points.tex` は、固定点なしの楕円点グラフを持つ分離表示の原代数の点関手を任意試験環で計算する。m=1,g=cu³,c≠0では、上の同じX上でPt(A)=Z_X(π)=⊔E_iとなる。m≥2でV(g)が滑らかなら、定常成分の完備局所環はJ[[t_1,…,t_{m−2}]]、J=⊗(S_i)_abの長さは8^kである。可換側のJ^cl=⊗Jac(f_i)との差を全スキーム比較で検査し、被約部分の一致や長さの一致を全スキーム同型としない。自然な中心射影のスキーム論的像と第零Fittingイデアルも区別する。
- `explicit_sklyanin_input.tex` はS★のparameters (1:−3:−2)、指定中心元Ω★、点曲線E_{17/9}、中心商、AS正則な周囲環を具体的に確認する。`point_poisson_obstruction.tex` はこれと上の直接Ku比較を用い、A★=S★[u,v]/(Ω★+(u³+v³)/3)の全スキーム版反例を証明する。A★は点スキームの良い条件を満たす滑らかな楕円一ブロック型であり、そのsmoothnessと全coherent Kuは直接比較から得る。全O stackの全chart入力をh=1で独立確認したという主張にはしない。三つの定常点の局所環J_1、任意supportの局所補題、12点のHessian分類、Mayanskiyの全Poisson分類、BMMSのcategorical Torelliにより、別π/別Xも排除する。自然な対の被約部分は一致する。一ブロック零スキームのE_H⊔D_H分解と良いrank2標的への埋込み一致障害も保持する。境界中心評価εはZ(B)_3/Sym³UからJacobi次数三線への写像である。
- `central_mixed_one_variable.tex` は、中心変数uが二次関係に現れる表示を扱う。明記した楕円グラフと可換化正則列の仮定の下で、定常環Qは長さ8^k、例外係数はmonic norm det(c+m_b)の零点となる。有理係数の二ブロック例では64個の相異なる例外値を明示し、各値で一つの被約定常点を得る。`cmo:prop:character-ext` と `cmo:cor:sixty-four-ext` は普遍higher homotopyのκ公式から、全64点のaffine characterの自己Extが次数0,2,3,5のみ各一次元と証明する。有限自己Extを有限射影次元・smoothness・Yoneda積の同定と混同しない。`cmo:prop:contraction` の収縮はc=t^(-3)で元の族と同型になり、`cmo:cor:conditional-cofinite` は相対対角のperfect性を追加仮定とする余有限Ku実現である。この追加仮定と個々の混合商のsmoothnessは未解決。normの根をsmoothness判別式や新しい反例と扱わない。
- `geometric_realization_locus.tex` の局所開性はn≠4の実smooth proper dg族と既存Artin形式認識を用いる。全Abel族の飽和性、境界での閉性、全intrinsic成分を自動的に与えない。
- 全O認識・全慣性・第三Veronese・全根、相対積、Picard比較、自然周期q(ω³)=−1/v_ω(p)の既存証明を保持する。全中心同変核の判定はk≥3では同種・CMを許し、k=2では幾何学的非同種を仮定する。二因子の混合核や指定中心の非正規性を無視しない。中心の無限共役軌道は同じ共役類内の無限性であり、非共役作用の無限性とは異なる。
- compact/Perfの任意導来底変更と非正則底の全Db(coh)を区別する。smooth regular元底のcoherent飽和の証明、raw最高次syzygy線、共通関係直線と指定periodを保持する。点集合だけから全非被約point functorや族の射を結論しない。
- 一ブロックの中心三次商線、点曲線、残余射次数9/18、点型Picard指数三・非分裂指数九、γ̄_n/[D]の問題を多ブロックへ無条件に流用しない。full class選択、gerbe中立化、period位相は別段階。
- `notes/central_cubic_generic_smoothness.tex` の非可換Bertiniの適用には、中心chartが有限生成可換中心上有限という仮定が必要。PBW性やassociated gradedのPI性だけで代用しない。
- `verify_mixed_character_ext.py` の4 PASSと `verify_point_poisson_obstruction.py` の12 PASSの厳密計算を確認済み。有限語関係による中心性の証明、全次数PBWの文献による判定、smoothness・Ku比較の証明は別である。独立読解、組版、表示確認、保存の状態は `notes/validation.md` を正本とし、計算成功だけで組版や保存の完了を報告しない。

## 正本・外部入力・保存

- 正本は `uedakazushi/nc-cubic` の `main`。本文のある主原稿は必ず `papers/nc-cubic.tex`、日本語LuaLaTeX、著者欄空欄。現在の成果を理解できる順に統合し、版ごとの補遺・履歴・旧ZIPを蓄積しない。
- `poisson-cubic` は古典正規形とPoisson moduli、`cubic-quantization` は全Poissonの代数的中心三次量子化と同変降下、`nc-cubic-threefold` は三様体固有の全Abel変形・相対比較と独立点スキーム論文の正本。通常は読取り専用で、具体的定理・仮定・版を引用する。本稿はB=ambient、A=商、量子化稿は逆。
- 方針・研究ノート・公表稿を中心とする自己完結した現行一式を維持する。証明済み・追加仮定付き・未完成・予想・計算的観察、原稿の証明と今回の独立読解、形式証明・新規性を区別する。誤りは依存する本文・要約・方針・hubへ反映し、有用な障害はノートに保持する。
- 公表稿では一次文献を確認し、既存結果の適用範囲と本研究の寄与をIntroductionで比較する。外部PDFや大量の検索結果は保存しない。論文に十分な証明がある内容をノートへ全文重複しない。
- `python3 scripts/check_sources.py`、`latexmk -lualatex papers/nc-cubic.tex`、変更内容に必要な厳密計算を確認する。PDF/SyncTeXはbuild/。research-hubのLuaLaTeX/latexmk/VS Code設定を参考に既存の有効設定を保つ。主原稿の移動時はinput・文献・root指定・README・設定も更新する。
- 通常commitとmainへのfast-forward pushを再承諾なく行い、15–30分の切りのよい区切りで保存する。他の作業者の変更を保持する。force push・PR・GitHub Actionsの追加/実行、PDF/ZIP/中間生成物のGit追跡は行わない。Library定常二重保存は不要で、push失敗時の緊急保存または別の明示指示時に使う。既存Libraryファイルを指示なく削除しない。
- **各区切りにresearch-hubを更新する。** 先に本repoの方針・ノート・原稿・READMEを保存し、その結果に基づきhubの到達点・確実性・未解決核心・次の一手・依存・正本・実確認日を更新する。保存前にhub最新を読み、他研究と並行変更を保持して通常commitでmainへ反映する。対象repo保存とhub更新の成否を別々に確認し、hub未反映なら理由と未反映項目を報告する。
