# 非可換三次 n-fold のモジュライ

2026年11月20日 / v2。日本語 LuaLaTeX による現行研究稿と、研究継続に必要な最小限の資料・厳密計算証明書。

**再開時は [研究方針](00_research_plan.md) を最初に読む。**

## 内容

- [公表用研究稿](papers/nc-cubic-n-fold.tex)：中心 Veronese 復元、一ブロック次数付き DM stack、普遍相対双対、点スキーム、Jacobi スキームの次元境界と頂点構造、残余圏の通常 Artin 形式認識。
- [研究ノート](notes/research_notes.md)：主張の依存・適用範囲、反例・障害、文献の確認箇所、次の計算の入口。
- [検証範囲](notes/validation.md)：原稿点検・組版・厳密計算を区別した確認状態。
- [Jacobi 行列検証コード](computations/verify_jacobi_rank.py) と [整数小行列証明書](computations/jacobi_rank_certificate.json)。
- [参考文献](papers/references.tex)。外部文献PDFは含めない。

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の論文A・B。これらが既に扱う一般次元の正規形・量子化・一般点復元を、新しい成果として数えていない。

## 主要結果と未完成部分

一ブロックの周囲代数の次数付きモジュライの次元は `(n²+7n−4)/2`、中心三次 torsor の相対次元は `binom(n+1,3)`。良い相対 PBW 表示チャートでは、有限 Koszul 対角、真正な双加群双対、compact 性、相対 properness、Serre 関手 `S=(1−n)[n]` と trace を任意底変更に両立して構成した。全 O-保存 Abel 比較には一般の圏族の係数作用・全同値の fpqc 降下の条件が残る。

本文の楕円境界・固定点なしの条件と中心三次の非零因子条件の下で、点スキームの定常成分は型 `(2,2,2,3)`、次元 `n−3`、次数24で、四次元の滑らかな場合には種数37の曲線となる。

一般の滑らかな三次に対して、`3 ≤ n ≤ 7` では Jacobi スキームが Grassmann 錐に等しい。`n ≥ 8` では、既存の被約分類を入力すると、頂点に支持される非零の有限長冪零根基を持つ。非零部分と射影化は全次元で Grassmann のものにスキームとして一致する。普遍的な `binom(n+2,3)` 個の従属関係を用い、`n=8` の次数二部分は一般にちょうど330次元と求めた。`n≥11` では次数三にも非零部分があり、最高次数と頂点の極大イデアルによる消滅指数は次元によらず一様に有界ではない。冪零根基自身の積による冪零指数は未決定。

通常 Artin 基底上の残余圏の一次切断変形は `n ≠ 4` で幾何的変形として認識できる。四次元の categorical hull は22次元、幾何的変形は20次元。全 Abel モジュライの代数性、大域残余射、全 Abel 形式近傍の完成は主張していない。新規性の網羅的確認・外部査読は未完了。

## 再生成

必要な環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）と、Python 3・NumPy。PDFは `build/` に生成し、Gitでは追跡しない。

リポジトリのルートで実行する：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 computations/verify_jacobi_rank.py --verify computations/jacobi_rank_certificate.json
latexmk papers/nc-cubic-n-fold.tex
```

証明書の再生成も可能である：

```bash
python3 computations/verify_jacobi_rank.py --generate build/jacobi_rank_certificate.json
python3 computations/verify_jacobi_rank.py --verify build/jacobi_rank_certificate.json
```

`--generate` の前に `build/` を作成する。生成と保存済み小行列の検証は別のコード経路で行う。法32003で非零の整数行列式を用いるため、特性零の一般点階数の証明になる。浮動小数点による近似判定は用いない。

作業規約は [AGENTS.md](AGENTS.md) を参照。正本はこのリポジトリの main とし、現在のソースと証明に必要な計算資産だけを保存する。
