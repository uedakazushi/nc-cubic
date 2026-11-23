# 非可換三次超曲面の可換実現とモジュライ

2026-11-24 / v93。正本は本リポジトリの main。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 現在の問題と到達点

任意の滑らかな非可換三次超曲面が同次元の可換三次超曲面の Ku と同値になるという旧全称予想は、三次元の量子 Fermat 型反例と、smooth proper な圏族で変形連結な五次元の反例によって否定された。現在の目標は **可換実現可能なクラスの内在的特徴付けと実現領域の決定** である。

五次元では Serre 関手から復元する自己同値への自然変換環の積が実現の障害を与える。同じ smooth proper 族の非零パラメータで可換実現があり、原点ではない。Sklyanin 因子別 PBW 表示、混合 Clifford 表示等の肯定的比較は各定理の仮定の下で保持する。一般の必要十分条件、核の大域降下、両反例の圏論的入力の独立監査は未完了。

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
