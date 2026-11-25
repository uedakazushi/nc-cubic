# 非可換三次超曲面の可換実現とモジュライ

2026-11-25 / v95。正本は本リポジトリの main。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 現在の問題と到達点

任意の滑らかな非可換三次超曲面が同次元の可換三次超曲面の Ku と同値になるという旧全称予想は、三次元の量子 Fermat 型反例と、smooth proper な圏族で変形連結な五次元の反例によって否定された。現在の目標は **可換実現可能なクラスの内在的特徴付けと実現領域の決定** である。

複素数体上、次元 $n\ge2$ の滑らかな可換三次の Ku を、抽象的な smooth proper dg 圏の中で認識する条件を得た。一つの対象とその二つの回転が厚生成し、整合的な三乗周期の下で軌道自己射の積が外積代数となり、自己三重 Massey 積が滑らかな三次式を与えることが必要十分である。この式が比較先を定め、生成対象の双加群が実同値を与える。五次元では回転も Serre 関手で指定できる。[認識定理と比較核](papers/sections/cubic_orbit_generator.tex)

任意の滑らかな次数一 del Pezzo 三様体からの三次五様体の退化に対し、比較核を一つの線束で左 mutation すると、元の行列式障害が消え、半安定特殊ファイバーの二成分の和への完全忠実な関手を得る。指定した埋込みを保つと、残る成分では階数零の対象の行列式に次数の不一致が生じる。[二成分上の実核と延長障害](papers/sections/veronese_boundary_mutation.tex)

可換三次五様体、次数一 del Pezzo 三様体、偶符号五様体の滑らかな残余圏を合わせると、Serre 自然変換の三重積の核から同値類と比較先の方程式を復元できる。三重積の階数が 35 なら三次五様体、34 なら次数一三様体である。偶符号族でこの階数が落ちる因子は重複度一で、次数一三様体の被覆対合を持ち上げる形式変形に横断する。[判定・復元・形式変形](papers/sections/fivefold_triple_kernel.tex)

三次元・五次元反例と対角三様体の肯定比較について、主要な圏論的依存を原典と照合し、独立な固定点・乗法計算と生成対象の証明を記録した。指定された Sklyanin / Clifford 族での環による判定に加え、抽象圏では上記の周期付き生成対象を使える。任意の圏で Serre 自然変換環の条件からその対象が存在するか、一般の混合族で核を大域的に降下できるかは未解決である。[監査の項目と根拠](notes/validation.md)

偶符号五様体族では全自然変換環が完全交叉であることが可換実現の必要十分条件となる。非実現点でも環は Gorenstein で、環から重み付き六次式を復元できる。すべての滑らかな零係数点で、復元した六次式から次数一 del Pezzo 三様体とその残余圏への実比較核が得られ、環の次数付き同型は、偶符号族と滑らかな可換三次五様体の Ku の合併で圏同値の必要十分条件になる。Hesse 切片では $\kappa^3=-27$ を除く各値が非実現圏の同値類一つに対応する。[最小関係・復元・実核](papers/sections/even_sign_sextic.tex)

三次元の量子 Fermat 型では、全滑らかな中心三次商の残余圏で $(\dim HH_1,\dim HH_0)=(1,10)$ を、位数 27 の中心拡大に対する通常の固定点公式からも得た。[二つの固定点計算](papers/sections/quantum_fermat_obstruction.tex)

五次元の例では全次数の自然変換空間の Hilbert 級数も可換側と一致し、三重積の階数が原点を区別する。偶符号族の全滑らかな零係数被覆で、一次生成部分から漏れるのは次数三と四に各一元であり、一つの三次生成元を加えれば全環を得る。非零係数での比較の生成対象と、五次元族の相対残余射影が各ファイバーの全残余圏を与えることも主稿で確認した。[原典との照合範囲](notes/validation.md)

四中心変数の偶符号五様体では、滑らかな被覆の全係数で、Serre 自然変換の二次関係の射影共通零点が空であることが可換実現の必要十分条件になる。特定の非実現ファイバーではこのスキームは Veronese 曲面の平方零拡大である。[二次関係の決定](papers/sections/narrow_fivefold_cubic_product.tex)

五変数の対角量子多項式環の中心三次商で全 coherent 圏が smooth proper なら、残余圏の HH₁ 次元が五であることは滑らかな可換三次三様体による実現の必要十分条件である。[各型の実同値への帰着](papers/sections/narrow_diagonal_clifford.tex)

三角形型では三変数部分の係数と二変数三次の判別式から全 smooth proper 領域が決まり、楕円因子の比較線束は二つの変曲点の差で書ける。[係数判別と比較線束](papers/sections/narrow_quantum_threefolds.tex)

巡回五頂点型で使う一対輸送の指標恒等式は、固定点の原始留数を積に書き、動く二座標の有限 Fourier 変換を取ることで証明できる。[輸送と周期の証明](papers/sections/narrow_fermat_root_equivalence.tex)

二楕円因子と一中心の分離五様体は非順序の j 対で無標識分類される。線型結合切片の二次関係から分離型を判定でき、境界が Fermat 二因子でも全ての非零 j を持つ対 {0,j} が現れる。[証明と条件](papers/sections/two_elliptic_fivefold_relations.tex)

任意の二つの固定 Sklyanin 因子からの一中心族を、既に可換実現を持つ五様体の二次関係から復元した三次式の二平面条件で認識できる。この軌跡の余次元は方程式空間で曲線型固定なら 23、両型可変なら 21。同一二因子の二パラメータ切片では、分離型と同値な係数は三点を除いた放物線になる。[純二次結合の判定](papers/sections/two_elliptic_fivefold_relations.tex)

研究の優先順位は **P0：反例の独立監査 → P1：可換実現の内在的特徴付け → P2：実現領域・比較核・降下 → P3：公表単位の再設計と推敲** とする。詳細・着手方法は `00_research_plan.md` を正本とする。

## 読む順序

| 資料 | 役割 |
|---|---|
| [研究方針](00_research_plan.md) | 目標・主要到達点・優先課題 |
| [研究ノート](notes/research_notes.md) | 主題別の補足、着想、障害、証明所在 |
| [検証範囲](notes/validation.md) | 計算・独立読解・組版等の実施範囲と未確認事項 |
| [計算の再現](computations/README.md) | 実行手順・証明書・外部入力 |
| [AGENTS.md](AGENTS.md) | 作業・保存規約 |

## 公表用原稿

| 原稿 | 内容 |
|---|---|
| [nc-cubic.tex](papers/nc-cubic.tex) | 主原稿。可換実現、三次元・五次元反例、内在的判定、実現 locus |
| [cubic-moduli-descent.tex](papers/cubic-moduli-descent.tex) | 標識、中心作用、相対積、比較核の降下・モジュライ |
| [mixed-sklyanin-cubics.tex](papers/mixed-sklyanin-cubics.tex) | 因子別 PBW、混合 Sklyanin / Clifford 族、判別、比較核 |

本文は各主原稿と `papers/sections/` に置く。管理文書に証明を再録しない。外部の未公表入力は [一次資料・外部入力](notes/literature.md) と [未解決外部入力](notes/unresolved_external_sources.md) を参照する。

## 再生成

リポジトリのルートで実行する。必要環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、xr-hyper、etoolbox、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）、Python 3・NumPy・SymPy、必要に応じ C++17 コンパイラ（GCC または Clang）。

```sh
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 scripts/build_papers.py
```

三稿の PDF・SyncTeX は `build/` に生成する。相互参照の収束を含む三稿組版には `build_papers.py` を用い、VS Code の LaTeX Workshop でも同じビルド設定を用いる。PDF・中間生成物は Git に含めない。個別検算・証明書再生成は [計算の再現](computations/README.md) に従う。証明記載と計算確認・独立監査・組版確認は区別し、実施範囲は [検証範囲](notes/validation.md) に記す。
