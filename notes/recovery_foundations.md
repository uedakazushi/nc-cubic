# 一般点可換復元：有効な技術的注意と再現

2026年11月22日 / v50。研究全体の入口は [研究方針](../00_research_plan.md)。証明の正本は [主原稿](../papers/nc-cubic.tex) の `papers/sections/generic_recovery/`、主張の確実性は [研究ノート](research_notes.md) を参照する。

可換復元の基礎は主稿に集約し、楕円因子のwindowとrotation共役は [comparison_foundations.tex](../papers/sections/comparison_foundations.tex) を正本とする。構造対象付きモジュライと精密なPicard・周期降下は [モジュライ・降下稿](../papers/cubic-moduli-descent.tex)、混合族の中心とsmooth locus、具体的な比較候補は [混合Sklyanin稿](../papers/mixed-sklyanin-cubics.tex) を参照する。各証明の本文を三稿へ重複して置かない。

## 核心の定理と依存

`gdr:thm:generic` は \(n\ge3\) の次数別有限自由な代数的中心三次変形を扱う。通常の一変数基底 \(R=\mathbb C[h]_{(h)}\) の剰余は多項式環と滑らかな三次式である。関数体上の三次方程式、有限拡大上のrotation・指定三次周期付き全coherent Ku比較を区別する。特に全体の導来圏の同値、元の \(K\) 上での同値核、特殊点を含む相対比較は無条件に得られない。

証明の入口は `lp:thm:main`（相対noetherian・Koszul・中心正則性）、`tw:thm:window`（実際の三対象window・stabilization・回転周期正方形）、`cft:thm:complete`（完備曲率付きMF functorと逆）、`rog:lem:localization`・`rog:lem:descent`（固定対象局所化・有限降下）、`crs:thm:coherent`（全coherent飽和）、`gcd:thm:field-model`（勾配空間の積分と方程式の体降下）である。完全な証明は本文にあり、このノートに重複しない。

## 誤用してはならない推論と有効な障害

- \(\ker(V\otimes V\to U)\) には交代部分が含まれ、勾配空間は \(\ker(\operatorname{Sym}^2 V\to U)\)。可積分行列の全体は有限étaleなsymmetrizer代数 \(E_F\) と対応するが、その単元による曖昧さは全PGLのformや同値核の降下とは違う。幾何学的に分解不能なら基礎体上の方程式はスカラー倍を除き一意でも、元の体上の比較核は従わない（`gcd:ex:forms`）。
- 残余部分の左右admissibilityを例外列の存在だけで済ませない。smooth properの比較とPerryの条件が必要。有限降下では核と逆核・単位余単位のconeのperfect性を底上で確保する（`rog:lem:descent`）。
- 完備MF移送のbar Taylor評価は一般に挿入後のMF functorの偶arity消滅を意味しない。周期変数の冪と固定内部次数を同時に追う。任意のLaurent係数のMC元へ無限級数を再評価せず、integralな有限対象の通常Homを局所化する。
- 完備体 \(\mathbb C((h))\) に元を持つtorsorは \(\mathbb C(h)\) に有理点を持つとは限らない。例として \(z^3=1+h\)。有限核を定義する体の次数やGalois障害には別の計算が必要である。
- \(F=x_0^3+3t x_0x_1^2+x_2^3+x_3^3+x_4^3\) は \(\mathbb Q(t)\) 上の非分裂symmetrizer \(\mathbb Q(t)[u]/(u^2-t)\times\mathbb Q(t)^3\) を持つ。勾配空間の積分における有限étale性と分裂を区別する検査例である。

## Hesse–Sklyaninの厳密な模型

非可換関係 \([y,z]=h x^2+(h^2/2)(yz+zy)\) と巡回置換に中心変数 \(u,v\) を加える。指定されたharmonic-angleの生成元固定比較で \(W_{\mathrm{rec}}=F+hxyz+(h^2/3)xyz+O(h^3)\)。既知のDito二次星積とShoikhetのinner二輪消滅の規約を区別し、二次係数 \(-2/3+1=1/3\) を得る。これは任意formalityで同じ固定frameの係数を主張するものではない。

全次数のHesse規格化係数は
\[
 \lambda(h)=\frac{h+h^2/3+h^5/12}{1-h^4/4},
\]
可換五変数三次は
\[
 (4-h^4)(x^3+y^3+z^3+u^3+v^3)+(12h+4h^2+h^5)xyz=0.
\]
この同定は相対THCR、三変数 \(a=0\) dg Orlov、楕円曲線の導来同値と \(j\) の形式分枝比較による。有限jetや楕円曲線だけから五変数の指定周期同値を結論していない。固定模型上のKu比較核は有限体拡大後の存在に留まり、その具体行列は未計算。

## 計算資産と継続の入口

`python3 computations/verify_complete_curved_transport.py`：Schouten恒等式と有限arityのflow。
`python3 computations/verify_three_object_window.py`：windowの有限縮約。
`python3 computations/verify_generic_cubic_descent.py`：可積分行列と非分裂symmetrizer。
`python3 computations/verify_recovery_example.py`：中心恒等式、二次jetとHesse係数・五変数式の有限検算。

これらのコードは有限恒等式の検算であり、全coherentの同値、曲線の全次数比較、Brauer障害や指定周期の証明そのものを確認するものではない。三稿への編集整理だけで、これらのPython計算を再実行したとは扱わない。

新たな計算では、原点stabilizationの有限Homとrotation核から \(V=H^0R\operatorname{Hom}(\Delta,P)\)、\(U=H^0R\operatorname{Hom}(\Delta,P^2)\) と積を直接構成し、既知の楕円比較で得た方程式との一致を調べる。独立のArtin・étale・point-schemeの広範な成果は `nc-cubic2` を正本とする。

三稿のソース参照は `python3 scripts/check_sources.py`、他稿の定理番号付き参照を含む組版は `python3 scripts/build_papers.py` で確認する。出力は `build/<各稿名>.pdf` と対応するSyncTeXであり、実行済みの範囲は [検証範囲](validation.md) に記す。
