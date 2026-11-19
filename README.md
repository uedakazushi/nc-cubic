# 非可換三次 n-fold のモジュライ

2026年11月20日 / v4。日本語 LuaLaTeX による現行研究稿と、研究継続に必要な最小限の資料・厳密計算証明書。

**再開時は [研究方針](00_research_plan.md) を最初に読む。**

## 内容

- [公表用研究稿](papers/nc-cubic-n-fold.tex)：中心 Veronese 復元、一ブロック次数付き DM stack、普遍相対双対、全 O-保存同値の降下と線束障害、点スキーム、Jacobi スキームの平方零構造と横断切片、残余圏の通常 Artin 形式認識。
- [研究ノート](notes/research_notes.md)：主張の依存・適用範囲、反例・障害、文献の確認箇所、次の計算の入口。
- [検証範囲](notes/validation.md)：原稿点検・組版・厳密計算を区別した確認状態。
- [Jacobi 行列検証コード](computations/verify_jacobi_rank.py) と [整数小行列証明書](computations/jacobi_rank_certificate.json)。
- [八次元の頂点構造の検証コード](computations/verify_jacobi_vertex.py)、[C++ 検証器](computations/verify_binary_minor.cpp)、[次数三の全射性の証明書](computations/jacobi_vertex_certificate.json)。
- [参考文献](papers/references.tex)。外部文献PDFは含めない。

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の論文A・B。これらが既に扱う一般次元の正規形・量子化・一般点復元を、新しい成果として数えていない。

## 現在の研究目標

**一般次元の O-marked moduli、point scheme、Poisson 多様体のモジュライへの射、Kuznetsov 成分の比較**を中心に進める。各既約成分の general / very general な対象を優先し、次元に一様な定理と族の構成を目指す。general な稠密開と very general な点集合、一ブロックの表示成分と全モジュライの成分は区別する。

まず固定模型の全 O-同値比較を O-marked な族の構成に用い、点対応からの包絡・Casimir 空間の復元を、量子中心三次から Poisson 対 (X,π) を選ぶ射へ接続する。Poisson 射で得る同じ X について、非可換側の残余圏と Ku(X) の同値を期待し、その構成と降下を研究する。この同値や全成分のモジュライ射が既に完成したとは主張しない。

個別次元の Jacobi 計算と boundary の精査は、この一般目標の具体的な障害を解消する場合に行う。八次元の頂点構造等の既存成果と証明書は保持する。次の具体的な着手方法と各目標の到達基準は [研究方針](00_research_plan.md) にまとめ、全体の要約は [research-hub](https://github.com/uedakazushi/research-hub) に反映する。

## 主要結果と未完成部分

一ブロックの周囲代数の次数付きモジュライの次元は `(n²+7n−4)/2`、中心三次 torsor の相対次元は `binom(n+1,3)`。良い相対 PBW 表示チャートでは、有限 Koszul 対角、真正な双加群双対、compact 性、相対 properness、Serre 関手 `S=(1−n)[n]` と trace を任意底変更に両立して構成した。

固定した良い表示模型間では、任意係数変更を圏内の係数作用として構成し、全 O-保存同値と自然同型の fpqc 降下を証明した。全同値の層は `Isom_gr/G_m` に一致する。同値を大域の次数付き同型で表す障害は `Pic(R)[n−1]` の線束であり、次数一部分がともに自由なら `Pic(R)[gcd(n−1,3)]` に入る。従って `n≠1 mod3` では全同値に大域の次数付き代表がある。`n≡1 mod3` では、滑らかな affine 曲線上の非自明な三捩れ線束による良い PBW 模型の明示例で、指定した同値の大域持上げが存在しないことを示す。

本文の楕円境界・固定点なしの条件と中心三次の非零因子条件の下で、点スキームの定常成分は型 `(2,2,2,3)`、次元 `n−3`、次数24で、四次元の滑らかな場合には種数37の曲線となる。

一般の滑らかな三次に対して、`3 ≤ n ≤ 7` では Jacobi スキームが Grassmann 錐に等しい。`n=8`、すなわち `N=n+2=10` では、整数行列の証明書から全次数の差
`J₁₀/I_F ≃ C(−2)^330` を決定した。冪零根基は頂点に支持される長さ330の二乗零イデアルで、頂点の極大イデアルで消え、socle 全体に等しい。Hilbert 級数は Grassmann 環のものに `330t²` を加えたものであり、この平方零拡大は次数付き代数としても頂点の完備局所代数としても分裂しない。この八次元の結果は、既存の一般三次の被約分類に依存しない。

非零分解可能点では Hessian の共通核 `K` により横断切片を記述した。Thom–Sebastiani 直和の Jacobi スキームの retraction を用いると、全ての `n≥11` について、非零 Poisson 点の局所環と射影 Jacobi スキームに、任意の二元の積が零となる330次元の冪零部分空間を持つ滑らかな特殊三次を構成できる。周囲の冪零根基全体が二乗零であるとは主張しない。

全次元の一般三次では、既存の被約分類を用いると、非零部分と射影化は Grassmann のものに一致し、`n≥8` の冪零根基は頂点に支持される有限長加群となる。`n≥11` では次数三にも非零部分があり、最高次数と頂点の極大イデアルによる消滅指数は次元によらず一様に有界ではない。`n=9,10` の全 Hilbert 関数や、一般次元での冪零根基自身の積は引き続き未決定である。

Jacobi 行列の普遍的な階数上界は Gesmundo–Landsberg の Koszul flattening の既知の結果に対応する。`N=9,10` の二次行列の最大階数の達成も Boij（1999, Remark 6）の apolar Betti 計算に対応し、独立した新規成果として数えない。現行稿はこの対応を明示し、計算証明書を再現可能な独立検証として保持する。正確な参照箇所は [参考文献](papers/references.tex) と [研究ノート](notes/research_notes.md) に記す。

通常 Artin 基底上の残余圏の一次切断変形は `n ≠ 4` で幾何的変形として認識できる。四次元の categorical hull は22次元、幾何的変形は20次元。一般の Abel 圏族の効果化、全 Abel モジュライの代数性、大域残余射、全 Abel 形式近傍の完成は主張していない。新規性の網羅的確認・外部査読は未完了。

## 再生成

必要な環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）、Python 3・NumPy、および C++17 対応コンパイラ（GCC または Clang）。PDFと検証用の中間ファイルは `build/` に生成し、Gitでは追跡しない。

リポジトリのルートで実行する：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 computations/verify_jacobi_rank.py --verify computations/jacobi_rank_certificate.json
python3 computations/verify_jacobi_vertex.py --verify computations/jacobi_vertex_certificate.json
latexmk papers/nc-cubic-n-fold.tex
```

証明書の再生成も可能である：

```bash
python3 computations/verify_jacobi_rank.py --generate build/jacobi_rank_certificate.json
python3 computations/verify_jacobi_rank.py --verify build/jacobi_rank_certificate.json
```

`--generate` の前に `build/` を作成する。二次行列の生成と保存済み小行列の検証は別のコード経路で行い、法32003で非零の整数行列式を用いる。

八次元の頂点構造の検証は、整数係数の Jacobi 式を法2で計算し、次数三の縮約写像の全射性を保存済み小行列で確認する。標数二の三次多項式を解釈する主張ではなく、整数行列の階数下界を特性零へ移す証明である。検証時には約450 MBの行列を `build/jacobi-vertex/` に再生成し、直接消去のメモリ使用量は約220 MB、所要時間は約1〜2分（環境依存）。大きな行列は追跡対象に含めない。いずれの検証にも浮動小数点による近似判定を用いない。

作業規約は [AGENTS.md](AGENTS.md) を参照。正本はこのリポジトリの main とし、現在のソースと証明に必要な計算資産だけを保存する。
