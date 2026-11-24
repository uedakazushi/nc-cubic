# 一次資料・外部入力・再現上の注意

2026-11-24 / v93。論文の参考文献に対応する一次資料確認箇所、外部入力の適用範囲。実行手順は計算再現を参照する。

[研究ノート入口](research_notes.md) · [研究方針](../00_research_plan.md) · [検証範囲](validation.md)

## 7. 一次資料の確認箇所と引用上の注意

本文の引用文献の書誌とURLは `papers/references.tex`。以下は議論に直結する確認箇所と、ノートだけの補助経路の一次資料であり、全論文を監査したという一覧ではない。

Lin–Rennemo–Zhang は滑らかな Veronese double cone について Ku からの偶数 Jacobian 部分の復元、勾配イデアルの復元と Fourier–Mukai 型 categorical Torelli を証明している。主稿では、偶符号五様体から次数一 del Pezzo 三様体への実核を先に構成し、その像を判定する際にこの Torelli を用いる。[arXiv:2408.08266v1, Theorem 4.3, Proposition 4.11, Theorem 4.12](https://arxiv.org/abs/2408.08266v1)

- Dyckerhoff, *Compact generators in categories of matrix factorizations*, Duke Math.J.159(2011),223–274、[arXiv:0904.4713v5](https://arxiv.org/pdf/0904.4713)、§5.6、Theorem5.8（著者版p.31）。2026-11-22に一次PDFで、一変数W=Σr_i x^iのunital minimal A∞模型のm_i(θ,…,θ)=±r_iを確認した。中央因子cu³の三項係数に用い、本文では2×2行列により直接再検算する。非可換ambient全体のformalityをこの定理から導いていない。既存keyは `ROGDyckerhoff`。
- Willumsgaard, *Obstructions for Associativity in Stable Homotopy Theory*, [arXiv:2605.11390v1](https://arxiv.org/abs/2605.11390v1)（2026）、Theorem3.3、Lemma3.11。確認済みの固定unitのA_n障害塔を、安定な境界核圏のoppositeを通じて固定counitへ適用する。非空fiberのhomotopy群がH^(2−n−i)RHom(K,J^n)となるshiftを保持する。一般理論と、本族でarity二・三だけが残るsector計算を区別する。keyは `CMOWillumsgaardAssociativity`。
- Christ, *Spherical monadic adjunctions of stable infinity categories*, [arXiv:2010.05294v3](https://arxiv.org/abs/2010.05294v3)（2022）、Proposition1.11、Theorem4.1、§4.1、Example4.10。確認済みのstable Kleisli模型と、underlying monadおよびunitだけでは乗法が決まらない例を参照する。本族では実随伴とsplit-generationからcoKleisli代数を作り、全coherenceの比較を別に証明する。keyは `CMOChristSphericalMonadic`。

- Druel–Pereira–Pym–Touzet, *Bondal's conjecture in dimension five*, [arXiv:2606.03424v1](https://arxiv.org/html/2606.03424v1)（2026-06-02）。公式本文のTheorem1.2、Corollary1.3（PDF p.2）、§4.4 Theorem4.3の記述を確認した。次元2r+1のFanoではD_(2r−4)(π)に次元2r−3以上の既約成分が存在する。本文Theorem4.3は一般階数2rを仮定し、導入で低階数を既知結果へ帰着する。五次元での正次元零成分の存在と、本稿の全孤立成分の排除を区別する。外部証明全体の監査を行ったという確認ではない。
- Gualtieri–Pym, *Poisson modules and degeneracy loci*, Proc. London Math. Soc. (3)107(2013),627–654、[DOI](https://doi.org/10.1112/plms/pds090)、[arXiv:1203.4293v1](https://arxiv.org/abs/1203.4293v1)。Conjecture1.1（PDF p.2）、導入に掲げられたTheorem7.13（PDF p.3）の記述を確認。上の定理番号はarXiv v1に従う。偶数次元の上位退化軌跡と四次元のBondal予想を扱い、ここでも十分大きい成分の存在が結論である。smooth cubicの孤立零点の3整除制約をこの既知結果の帰結とはしない。
- Okawa–Uehara, *Exceptional sheaves on the Hirzebruch surface F2*, Int. Math. Res. Not. IMRN2015(23),12781–12803、[DOI](https://doi.org/10.1093/imrn/rnv079)、[arXiv:1409.7813v2](https://arxiv.org/abs/1409.7813v2)。Lemma4.2（p.18）のsmooth projectiveなHirzebruch曲面の変形、Remark1.2（p.3）の(−2)-curve上のspherical objectを一次本文で確認。これらの既知幾何と、smooth properな両側だけでは特殊同値が従わないという本ノートでの使用を区別する。
- Keller, *Derived invariance of higher structures on the Hochschild complex*, August 2003, last modified 2018-05-16、[著者PDF](https://webusers.imj-prg.fr/~bernhard.keller/publ/dih.pdf)。Introductionと§3.2の主定理でHochschild cochainの導来不変性を確認。通常の代数ではHH⁰(A)=Z(A)であり、指定混合因子のambient Morita可換化を排除する際に使う。curved/MF圏・射影残余圏の比較を否定する入力ではない。

上の一次文献とcubic hypersurface / cubic fivefold / isolated Poisson zerosについての限定検索では、孤立零点の一般次元の3整除制約と同一の主張をする先行一次資料は特定できなかった。検索の不発を先行結果の不存在の証明とせず、本定理および被約反例の文献上の新規性は未確認とする。

- Etingof–Ginzburg, JEMS12(2010), Theorem3.3.2 / §9（印刷p.1414）：三変数 potential の PBW・中心元・Rains の有限中心公式。今回のεの非消滅は公刊式の斉次部分を直接使い、係数恒等式を独立に記号検算した。Proposition8.1.1と式(8.1.3)には形式量子化の中心とPoisson中心の同型が既にある。§8.1の証明（印刷pp.1407–1408）はunimodularityによる相対形式Jacobian potentialの認識も含み、これらの存在そのものを新規とは数えない。現行のtrace–Hessian処方は有限パラメータと相対降下について位置付ける。https://ems.press/content/serial-article-files/31746
- Dito, *Kontsevich star-product on the dual of a Lie algebra*, arXiv:math/9905080, §2 equation (3), §3 Theorem2：§2 の式は一般 Poisson tensor の二次星積であり、eye 項を含む。§3 Theorem2 も一般 Poisson 構造の星積に対する Weyl 化である。Lie 代数に限定される後続の Gutt 星積との比較とは区別する。本稿の ρ₂F は §2 の式の線型形式の冪への適用と polarization から直接求める。[一次資料](https://arxiv.org/abs/math/9905080)。
- Shoikhet, *Vanishing of the Kontsevich integrals of the wheels*, arXiv:math/0007080, §1.3 Theorem、§2.3.1：harmonic-angle の内向き wheel の重みの消滅と中心写像を確認。Weyl 模型への変換で現れる二次項と、同じ formality の中心写像の項を区別する。固定 gauge を指定せず係数 1/24 を普遍的な未標識量と呼ばない。[一次資料](https://arxiv.org/abs/math/0007080)。
- Shoikhet, *Kontsevich formality and PBW algebras*, [arXiv:0708.1634v2](https://arxiv.org/pdf/0708.1634) (2007), §1.3 pp.6–7：symmetric algebra を exterior coalgebra の cobar で解消する既知の構成と二変数の式を確認。多項式中心自体の有限解消に用い、相対 balancing の有限表示をこの結果からは結論しない。
- Burke, *Strictly unital A∞-algebras*, [arXiv:1801.06943v1](https://arxiv.org/pdf/1801.06943) (2018)：普通の可換基礎環上で、unit splitting と curvature により augmentation の欠如を扱う枠組みを確認。ノートの curved-bar 模型の出典であり、内部次数による有限 arity 評価や実際の kernel moduli への適用を同論文の定理として引用しない。
- Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*, Enseign.Math.55(2009),235–273、DOI 10.4171/LEM/55-3-3、§2 Lemma2.1と式(4)–(5)・p.240：Hesse正規形とWeierstrass係数を公刊PDFで確認。パラメータ(t₀,t₁)=(1,3λ)から本文のj式を得る。係数式からjの規格化も厳密検算した。[公刊一次資料](https://ems.press/journals/lem/articles/12146)。
- Fisher, *Testing equivalence of ternary cubics*, Algorithmic Number Theory, LNCS4076(2006),333–345、[著者PDF](https://www.dpmms.cam.ac.uk/~taf1000/papers/testeqtc.pdf)、[DOI](https://doi.org/10.1007/11792086_24)。Theorem1.1 の Weierstrass 規約・不変式環 C[c₄,c₆]、Lemma2.2 の代数閉体上の proper equivalence、Lemma2.3 の証明の微分付き楕円正規曲線の自己同型E[3]、Theorem2.5・Lemma2.6 の微分の変換、§4 の Hesse 不変量を確認。本文の g_(p,q) へは a=p/3,b=−q/3 と置換する。proper projective stabilizerの位数9と、sign stabilizerの指数二に使用し、SL₃内の中心μ₃を重複して数えない。さらに著者稿§9.5「Reduction of Ternary Cubics」（PDF pp.12–13）の中央拡大 μ₃→H₃→E[3] と非可換な位数27の群を原文確認し、一般三次の H_g の記述に用いる。full ambient の中央化群 GL_r と混合定数降下は本文で別に証明する。古典的不変量・軌道分類・三捩れ自己同型は既知であり、混合三角性と正確な残余次数18への応用と区別する。
- Stacks Project, Lemma10.49.3, [Tag0FWF](https://stacks.math.columbia.edu/tag/0FWF)：代数閉包への底変更で整であることと幾何学的整性の同値を一次本文で確認。有限 torsor の定数降下で、代数閉体上の有限体因子をさらに定数拡大しても整性と体拡大次数が保たれることに用いる。torsor の降下自体は本文で証明する。
- Behrend–Noohi, Math. Ann.371(2018),1375–1408, DOI10.1007/s00208-017-1624-1：刊行版§2.3のgrading rigidification・twisted algebra・determinant中立化、§3.1.2の(C,O,s)を直接確認。これらの一般手法自体は既知であり、本稿は全O同値によるsを外した局所stack比較とrank(r,3)の非中立性を区別する。https://link.springer.com/article/10.1007/s00208-017-1624-1
- Stacks Tags058G,0781,03R6：Lazard、代数的stack上のQCohがGrothendieck圏、PGL torsorと中心単純代数。Tags063P,063U,062Y,056Q：相対正則埋込み・相対Cartier因子の任意底変更。本文の相対構成に使う範囲を一次資料で確認。
- Berger–Taillefer, J.Noncommut.Geom.1(2007), Theorems3.1,3.6 と Theorem3.6 の証明：potential による PBW 変形と自己双対解消。体上の定理を任意係数環へ直接適用せず、cyclic Hessian と分裂濾過から相対複体を構成する。
- Keller, *On differential graded categories*, arXiv:math/0601185v5, Theorems3.4,3.8(c)：compact 部分の thick 生成と compact generators による dg Morita 表示。基底は一般の可換環。本文では dg orbit 模型 A→Q とその両側作用を明示して用いる。
- Mori–Smith, arXiv:1502.07403v2, Theorem4.2：滑らかな三変数三次に付随する二次 Calabi–Yau 代数。Theorems1.2,7.2 と Lemma7.1：点曲線の Hessian 公式と対称行列＋交代行列の行列式。点曲線公式を新規とは数えない。[一次資料](https://arxiv.org/abs/1502.07403v2)。
- De Laet–Le Bruyn, *The geometry of representations of 3-dimensional Sklyanin algebras*, Algebr.Represent.Theory18(2015),761–776、arXiv:1405.1158v1 §2 p.3：巡回和で書いた中心元 a(b³−c³)C+b(c³−a³)D+c(a³−b³)S。非巡回の Rains 式とは出典箇所を区別する。[一次資料](https://arxiv.org/abs/1405.1158v1)、[刊行版](https://doi.org/10.1007/s10468-014-9515-6)。
- Kontsevich, *Deformation quantization of algebraic varieties*, LMP56(2001),271–294、§2.3 Proposition6：二次 Poisson tensor と二次代数の形式的 GL 同変対応。Conjecture1・Questions1 の収束・周期の問題と、本稿の有限 jet・形式構成を区別する。[一次資料](https://arxiv.org/abs/math/0106006)、[刊行版](https://doi.org/10.1023/A:1017957408559)。
- Kontsevich, *Deformation quantization of Poisson manifolds*, LMP66(2003),157–216、Theorem4.6、§§4.6.2,6.3：formality とグラフ構成・線型共変性。選択した formality 自体の独立性を主張しない。[著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf)、[刊行版](https://doi.org/10.1023/B:MATH.0000027508.00421.bf)。
- Ciliberto–Ottaviani, *The Hessian map*, arXiv:2006.07213v1 (2020), §5 Theorem5.7：射影的な純Hessian写像の一般次数3をSL₃同変性とHesse族への還元で求める。p.17の二回合成は次数9。本稿のaffine補正f↦f+Hess(f)/24とは異なり、Hesse還元手法そのものの新規性を主張しない。[一次資料](https://arxiv.org/abs/2006.07213v1)。
- Ottaviani, *Effective methods for plane quartics, their theta characteristics and the Scorza map*, Ann.Univ.Ferrara70(2024),1115–1153, §3 Remark3.3直後：古典的四次Aronhold不変式の25単項式表示と四つのdeterminantによる縮約を明記。本稿のSはS(xyz)=1という規格化と再現検算であり、新しい不変式ではない。[一次資料](https://doi.org/10.1007/s11565-024-00528-2)。
- Lindberg–Pym, *Semiclassical Hodge theory for log Poisson manifolds*, arXiv:2408.16685v1 (2024), §1.6・§6.7 Theorem6.9、Remark6.10（印刷pp.59–60）：Kontsevichの元のharmonic-angle星積で、原生成元の交換比 q_ij=exp(hλ_ij) を証明。§1.6でqをw_ij/w_jiとして定義しているため、任意の生成元変更を経た抽象同型だけの結論ではない。任意stable formalityへの一般化に残るGauss–Manin適合条件と区別する。この量子トーラスの公式自体は既知入力。[一次資料](https://arxiv.org/abs/2408.16685v1)。
- Banks–Panzer–Pym, *Multiple zeta values in deformation quantization*, Invent.Math.222(2020),79–159、Corollary1.3・§§6.1–6.2：harmonic-angle graph weights の既知の厳密計算。五次 tensor の評価はこの入力を利用し、積分の再計算を本研究の成果に数えない。[刊行版](https://doi.org/10.1007/s00222-020-00970-x)、[著者稿](https://arxiv.org/abs/1812.11649v1)、[2022年訂正](https://doi.org/10.1007/s00222-022-01122-z)。
- Buring, *The action of Kontsevich's graph complex on Poisson structures and star products: an implementation*, Mainz 博士論文(2022)、§§3.4.1–3.4.2（pp.74–76）、§3.5（p.89）、§3.6.4（pp.103–105）：グラフの標識・自己同型・星積の規約と著者公開データ。本稿は `star5.txt` と `kontsevich_2_k.txt` / `weights_kontsevich_2_k.txt` を照合し、線型二入力に必要な73項だけを出典・入力ハッシュ付きで保持する。[学位論文](https://www.rburing.nl/gcaops/gcaops-dissertation-rburing.pdf)、[著者データ](https://www.rburing.nl/gcaops/)。第三者の評価器の実装自体は収録せず、保存した数値重みと辺データを独立の有理数評価器で再現する。
- Antieau–Krashen–Ward, *Derived categories of torsors for abelian schemes*, Adv.Math.306(2017),1–23、Theorem2.2：体上の原点を持つ楕円曲線の k-linear 導来同値は k-同型を導く。点のない genus-one torsor に同じ結論を流用しない。[一次資料](https://arxiv.org/abs/1409.2580)、[刊行版](https://doi.org/10.1016/j.aim.2016.09.037)。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996), Theorem4.2.2, Proposition4.2.5, §4.3：一点中心拡大の点対応と二次関係。
- Mayanskiy, arXiv:1303.5916v1, Theorem1, §2.2：三様体の Plücker 方程式。被約分類と scheme structure を区別する注意があり、後者には実際の Schouten 計算を使う。
- Bonala–Clarke–Mohammadi, arXiv:2103.16208v1, §2.4 Theorem2.3：標準単項式基底。本稿はその次数二の比較不能対を列挙して 5 binom(N+1,6) を導く。
- Landsberg–Ottaviani の Young flattening と Gesmundo–Landsberg, *Explicit polynomial sequences with maximal spaces of partial derivatives and a question of K. Mulmuley*, Theory of Computing15(2019), Article3, Proposition6.1, 式(6.2)、Remark6.6：三次式の Koszul flattening の既知の階数上界。本稿の Jacobi 係数写像との同定と座標的な普遍関係を介して利用する。上界そのものを新しい結果として数えない。
- Boij, *Gorenstein algebras with nonunimodal Betti numbers*, Math.Scand.84(1999), 161–164, Remark6（pp.163–164）、DOI 10.7146/math.scand.a-13871：N=9,10、socle 次数三の apolar Gorenstein 代数の total Betti 表とその達成例。本文の Koszul 複体の比較を通じて二次 Jacobi 階数の最大性と差330が既に従う。表を graded Betti 表と誤読せず、b₄−c_N=β_{3,5}+β_{4,6} から必要な消滅を取り出す。
- Boij–De Negri–De Stefani–Rossi, *On the rate of generic Gorenstein K-algebras*, Math.Z.311(2025), Article10, arXiv:2304.14842v2, Introduction pp.2–3：生成次数についての既知結果と最小分解全体の問題を区別し、中間位置の予想には反例があることを記す。一般 apolar 代数の Koszul 性を β_{4,6}=0 の代用にしない。
- Bricalli–Favale–Pirola, *On the irreducibility of Hessian loci of cubic hypersurfaces*, Forum Math.Sigma13(2025), e80, DOI 10.1017/fms.2025.36：Proposition2.1 の Hessian/apolar 積と滑らかさ、Definition3.1・Remark3.3 の Thom–Sebastiani 分解、Theorem3.4 の Hessian rank locus による判定。本稿の最大法接空間の幾何と関連する既存結果であり、Jacobi 横断切片やスキームの retraction は本文で別に証明する。
- Stacks Tags 01OA,0245：射影束と fpqc アフィン降下。01OA の商直線規約と本文の部分直線規約は双対であり、混同しない。
- Gabriel, *Des catégories abéliennes*, III §1, p.365：商圏の Hom の filtered-colimit 表示。中心正則対による飽和性の証明に使う。
- Stacks Tag023N（Proposition35.3.9）：忠実平坦な加群降下の核による構成。Tag03PK・040Q（§59.28）：Kummer 列と μ_d-torsor。Tag02RU：曲線の主因子の次数。固定模型の tails・全同値の降下は本文で構成する。局所一ブロック型の効果化には、別に重み付き加群のGabriel商と全O-Hom比較を用いる。
- BFK, *A category of kernels for equivariant factorizations and its implications for Hodge theory*, Theorem5.39 **一般式**とその証明、印刷pp.82–84：sector の Koszul コホモロジーと parity。Lin–Zhang Theorem3.5 の parity にある内部 twist は cohomological degree と読む。同所の引用番号5.9は原著では5.39。BFK p.83 の簡約表示にも奇数側 Jac を残す誤植があるため、一般式の H^(2l+1) と孤立臨界点なら H^0 のみという p.84 の証明を根拠にする。さらに [arXiv:1105.3177v5](https://arxiv.org/pdf/1105.3177) の Definition6.11・Theorem6.13（PDF pp.69–74）で rotation の dg bimodule レベルの同定を確認。Remark6.14 の剰余体の shift は Galinat の window1 と混用しない。
- Pirozhkov, arXiv:2208.13604v1, Lemmas5.1,5.2：非対角 Hodge diamond と実際の幾何的 KS 単射。Lemma5.2 は n=3 でも使えるが、同稿の大域 Torelli Theorem5.3 の三次条件は n>3。
- Huybrechts–Rennemo, Algebraic Geometry6(2019), Proposition3.5 / Remark3.8：四次元の HH²=22 と幾何方向20。
- Lurie DAG X, Theorems5.1.9,5.3.16 / Proposition5.3.21、Blanc–Katzarkov–Pandit §3.3,§4.3：tame の1-proximate性、hull の Hochschild 制御、actual→hull の (−1)-truncated性。BKP の一変数形式生成結果を任意基底の定理へ読み替えない。
- Kuznetsov の fractional CY 論文と Lin–Zhang Proposition3.7：Serre/rotation の算術。Lin–Zhang Theorems4.1,5.1 の categorical Torelli は既知入力。
- Orlov, *Derived Categories of Coherent Sheaves and Triangulated Categories of Singularities*, [arXiv:math/0503632v3](https://arxiv.org/pdf/math/0503632) (2009), Theorems2.5(iii),3.11(iii)：Theorem2.5(iii) は非可換 connected graded Gorenstein algebra の parameter a=0 も扱う。可換な d=N、特に N=d=3 で graded MF と滑らかな plane cubic の D^b(coh) を比較する場合と併せて、三変数の proper Hom に用いる。N≥5 の window 定理の適用範囲を広げたとも、体上の同値だけで相対底変更が従うとも扱わない。
- Galinat, *Orlov's Equivalence and Maximal Cohen-Macaulay Modules over the Cone of an Elliptic Curve*, [arXiv:1302.1383v1](https://arxiv.org/pdf/1302.1383) (2013), §1.1・Lemma1.2・§1.4・Lemma2.7の証明：Φ=Φ₁、O_C と irrelevant ideal A_(≥1) の対応、Φ∘T_O∘tensor O(1)≃(1)∘Φ を同じ規約で確認。0→A_(≥1)→A→K→0 と合わせて κ_act↔O_C[1] を用いる。最高次線束型の負 rotation 計算は本文で別に証明する。
- Stafford–Van den Bergh, *Noncommutative curves and noncommutative surfaces*, Bull.Amer.Math.Soc.(N.S.)38(2001),171–216、[arXiv:math/9910082v2](https://arxiv.org/pdf/math/9910082)、§3・PDF p.10・式(3.1)：右 THCR の shift s=σ_*∘(−⊗L) を原著の添字まで確認。σ_* と σ^* の区別を点の平行移動と rotation の共役式に用いる。引用 key は `NFMStaffordVdB`。
- Burke–Stevenson, *The derived category of a graded Gorenstein ring*, [arXiv:1507.00830v1](https://arxiv.org/pdf/1507.00830) (2015), Definition5.1、Lemma6.2、Theorem6.4(3)：Gorenstein 条件・χ と、parameter a=0 の任意の window i における相互逆同値を確認。指定 source active 商の noetherian 性・有限 injective dimension・次数零環の有限大域次元は `lem:nfm-active-dvr-gorenstein`、相対 dg window の底変更は `prop:nfm-relative-active-window-basechange` で検証した。境界の full 可換三次には別に Theorem6.4(1), i=1（原著pp.18–19）を用いる。これは A₀が regular DVR、a=n−1>0 の場合を含み、Proj の滑らかさを要求しない。隣接する窓の mutation と F の自己交叉周期を組み合わせた低 Hom 計算への適用を、既知の Orlov 比較そのものと区別する。
- Preygel, *Thom-Sebastiani & Duality for Matrix Factorizations*, [arXiv:1101.5834v1](https://arxiv.org/pdf/1101.5834) (2011), §2.2（pp.5–6）、Theorems4.1.3,4.2.2,4.2.3：literal な R-線型性と Perf(R)-module category の区別、および support・periodic coefficient を伴う相対構成を確認。本稿の非可換 graded-center 切断や代数的核の降下へ無条件には適用していない。
- BFK, *Orlov spectra: bounds and gaps*, arXiv:1012.0864v3, Theorem5.15：孤立次数三特異点の三連続内部 shift による生成。前項の BFK 論文と区別する。
- Kuznetsov, *Derived categories of cubic fourfolds*, Theorem3.1：Pfaffian cubic と K3 の導来同値。

- Fraenkel, arXiv:1310.6083v2, Proposition4.1 / Theorem4.3：孤立特異点を持つ affine 超曲面の Poisson 延長を gradient の Koszul 複体で記述する。三次 n-fold のパラメータスキームの境界を主張するものではない。
- Carles, Ann.Math.Blaise Pascal3(1996), §8 Lemma8.35（p.60）、DOI 10.5802/ambp.67：Lie law の変形の非零二乗零パラメータ。
- Carles–Márquez, Ann.Inst.Fourier61(2011), §3 Theorem3.2、Propositions3.9,3.10、DOI 10.5802/aif.2620：Lie law の Jacobi スキームの局所・大域冪零元と明示例。本稿の次数2という意味と冪零指数を区別する。

関連する近刊には Bricalli, *Linear Spaces in Hessian Loci of Cubic Hypersurfaces*, Mediterr.J.Math.23(2026),173、[DOI 10.1007/s00009-026-03169-1](https://doi.org/10.1007/s00009-026-03169-1)、[arXiv:2603.23207v1](https://arxiv.org/abs/2603.23207v1) がある。Definition1.3、Lemma1.8、Theorem1.5 の Thom–Sebastiani/Hessian/apolar の関連を確認した。同 Theorem1.5 が前論文を Theorem2.3 と呼ぶ箇所は、前論文の公刊版では Theorem3.4 に対応する。これらの Hessian 幾何の既存結果と、本稿の Jacobi 方程式全体の局所構造を区別する。

Lie algebra law の Jacobi スキーム一般に非被約性があることは既知である。また本稿の二次階数の上界、N=9,10 の最大性、および差330という数値も上記の既存研究に由来する。「Jacobi スキームに初めて冪零元を見つけた」あるいは「330という二次の不足次元を初めて計算した」という主張をしない。

現在証明を持つ寄与候補の中心は、全 O-同値の係数降下と局所模型 stack、全非空開に残る表示障害、相対点対応からの中心商復元、trace–Hessian と強い lift による Poisson 開の逆構成、残余復元との比較障害、混合 trace を含む代数的補正の降下・一般次数9、全混合五次 tensor と残余四次 potential、全次元に一様な四次比較障害、さらにそれを除く全 O-同値共変な有限補正である。c₂の消滅・偶奇性・形式 support 保存と split 族での補正後残余比較も保持する。一般混合係数の代数的残余三次・射影 Poisson 射と被覆上の Ku 比較、点微分による自然な符号商射と標準二重被覆上の full lift、さらに反対不変性・九次中間被覆・全次数の有限混合三角性による正確な一般次数18と、符号二次類の active 基底への降下・反対被覆の twist 構造は、明記した固定入力の下で本文に証明した。比較核には最高次 cohomology が線束となる非空な型を構成し、full class 選択後に split 一般点で index が3を割ること、Picard 障害としての同定と active 曲線・次数3切片による分裂を証明した。さらに determinant の三倍線束により、選択済み類の三分点被覆上の規格化核と J(S)/3J(S) による障害の記述を得た。従来 Euler 型の d_n 評価、全 rotation Euler 格子だけでは改善しないこと、三に素な被覆で選択済み核の scalar index が変わらないことも有効である。

符号については有限対角と有限混合多項式を使う近傍延長により、固定入力の下でχ_act=0と半古典規格化full射の次数9を証明した。追加の圏的延長仮定は使わない。独立に、指定中心商の相対THCR/window1と閉／一般底変更からm_P=p_resの非空型を得た。κとq_Yの内在的表示を通じ、この型は良い共通稠密開へ全O-降下する。一般jのHesse巡回例を実Sklyanin代数へ降下し、全n≥3の一般split係数点でδ_E(p_pt)のexact period=index三を得た。全active FM分類と合わせて全active intertwinerを排除し、さらにH_gのfull ambient作用によるI_scの分裂とparabolic共変性から、残余側も同じexact indexとなる。真の一般Hesse点を使う別の支配族は三分点torsorの連結九次性とASL₂(F₃)の216次Galois閉包を与える。

n=3,4では既知の全自己同値分類を核へ移し、定数Zのclass降下によって全full classの共通scalar障害を決定し、周期標識を忘れた全full比較の最小体次数三を得る。さらにE_P→q^RH⁰(qE_P)が同型となる随伴復元条件を加えると、全n≥3で非空な有限class torsor S_pと有限安定化群H_pを得る。この強化点型の実現stackはS_p×Pic_C^pで、最小実現次数はmin_i[K_i:K]ind(α_Ki)≤3|H_p|である。一般一ブロック族ではTate–Koszul忠実性により全n≥3でH_p=1、S_p=Spec(k_n)となり、強化型の同型類は正準的に一つとなる。奇数次元の数値的自明性も別の帰結として保持する。任意full classへは拡張しない。

非分裂の n≡1 mod3 では、二つの独立な Kummer 座標による曲線例を mixed theta 表示へ降下し、良い一ブロックの任意の非空開で点 Picard index 九を実現した。普遍点 gerbe の最小重み一階数も九で、表示安定化子が自明な共通開内では全該当次元の強化点型が未標識最小次数九を達成する。五次元では Clifford 半 rotation の平面非依存性と、二捩れの scalar 障害を次数2835の零 cycle で消す実核降下を得た。さらに相対・絶対 coevaluation の比較から O≃ρ⁻¹[1]、ε≃id を得た。全 n の H_p=1 は別の Tate–Koszul 忠実性による。二 mutation の具体的複体は他の対象作用を調べる資産として保持する。

指定周期の μ₃ 位相は n=3,4 の全 full class に共通である。相対規格化を適合させた最小次数三と、独立 target 尺度族の正確な九を保持する。唯一の φ_sc・t_sc・source Ω による正準 cube frame では、全 n の γ_sc,n は C(c₄,−c₆) へ降下し、半古典形式像は1だが q=2 の完備局所値は [D_R]。従って位相は全次元で非自明であり、位相体は三次と決まる。大域的な γ̄_n/[D] と次元間の一致、位相体上の scalar index は未決定。ΔD 外の非分岐性を追加仮定すれば大域式 [D] が得られる。n≥5 の任意 full class への位相共通性や全型の標識付き最小次数は未解決である。

高次元のclass問題では、元の体上の実核T=ρ⁻¹[1]を除いたG_ρ/〈T〉-torsorへの縮約と、classとT軌道のGalois安定化群の一致を証明した。奇数次元の数値像は六元群であり、残る群はG_ρ,0/〈[2]〉である。一般三次七様体の既知の球面対象からfull群のZ²とG_ρの無限指数が分かるため、低次元の全群の巡回性を全nへ拡張する方針は取らない。強化点型の正準classにより、点型を含むGalois固定軌道の存在も全次元で従う。他のfull軌道の分類は未決定である。

強いliftのKoszul手法、formalityと中心対応、既知の星積重み・wheel消滅、古典的Hessian写像・Aronhold不変式、残余MF模型そのものは既存入力と区別する。完備中心係数商の比較は選んだ相対flowの直接の補強であり、一般のcategorical base-change定理やその代数化ではない。重み1束からのAzumaya・Brauer–Severi剛性化、Picard gerbe、THCR・Orlov window、三・四次元のFM自己同値群分類、Iliev–Manivelの七次元球面対象、Toën–Vaquiéのboundednessと自己同値moduliは既知の入力である。本稿での最高次線束型、点の平行移動、projector核の一意性を通じたclass降下、指定MF周期のcoherenceとcube frameによる算術、随伴復元条件と有限H_p-torsorへの縮約と分ける。新規性の網羅的確認は未了。全intrinsic成分のモジュライ、特殊族でのPoisson対の延長と低Natの底変更の一致、良い稠密開の外での点型、n≥5の強化条件外の任意full核への適用、大域的な残余位相 γ̄_n/[D]、位相体上の scalar index、coherent graded-center比較の代数的降下は未完成である。全refined核でm_P=p_resを示したとはせず、一般次元での有限torsorへの縮約や選択後の規格化を未選択の全同値stackへ外挿しない。

保持する補助成果には、n=8 の**次数三以降を含む** Jacobi イデアルの決定、頂点の長さ330の平方零拡大と完備局所非分裂性、全 polar 方向を残した横断切片、直和の retraction による特殊三次の非零冪零例、実現する大域持上げ障害がある。二次階数だけでは得られない主張として証明を置く。全引用・被引用文献や MathSciNet/zbMATH の網羅的調査は未実施であり、以上の寄与候補、比較障害、残余形式認識の厳密な初出は継続して確認する。

勾配復元では Wang, *Deformation of Milnor algebras*, Pacific J. Math.305(2020),329–338、[DOI](https://doi.org/10.2140/pjm.2020.305.329)、[arXiv:1906.04891v3](https://arxiv.org/abs/1906.04891v3) の §3、Corollary3.2・Theorem3.3を確認した。Hwang, *Symmetrizer group of a projective hypersurface*, JMSJ78(2026),55–62、[DOI](https://doi.org/10.2969/jmsj/93469346)、[arXiv:2501.08633v1](https://arxiv.org/abs/2501.08633v1) の Theorems1.5,1.6、Propositions2.2,2.6、Corollary2.7を確認した。scalar symmetrizer による体上の一意性は既知であり、本稿の相対核・O-降下とは区別する。

Toën–Vaquié, *Moduli of objects in dg-categories*, Ann.Sci.ENS(4)40(2007),387–444、[DOI](https://doi.org/10.1016/j.ansens.2007.05.001)、[arXiv:math/0503269v5](https://arxiv.org/abs/math/0503269v5) の Lemmas2.8,2.10,3.25、Proposition3.20、Corollaries2.13,3.17,3.22,3.24を一次資料で確認した。Proposition3.20（公刊pp.433–434）は一つの指定generatorに対するHomのcohomology次元上界によるboundedness、Corollary3.17は接空間、Corollary3.22はsimple-object gerbe、Lemma3.25とCorollary3.24の証明（pp.437–438）は可逆核の開性を与える。これらを全Kuの三対象生成とHH¹=0へ適用して有限安定化群を得るのであり、TVの定理自体を新規成果としない。核側にはcategorical dualを使い、幾何学的dualがKuに属することを仮定しない。引用keyは `NFMToenVaquieModuli`。

smoothnessによるpseudo-perfectからperfectへの移行とfiltered descent、simple-object gerbeと全自己同値sheafを区別し、smoothnessのspreadingではperfectな源から対角への射を先に降ろす。Toën, *Anneaux de définition des dg-algèbres propres et lisses*, [arXiv:math/0611546v3](https://arxiv.org/abs/math/0611546v3) の Théorème1、F2–F6、Sous-lemme7（pp.8–9）も参照した。perfect moduleの係数降下とEndへのalgebra mapによる作用の記述を利用し、source HFPの仮定を無限な相対解消へ流用しない。一般のproper族のsmoothnessの開性を無条件に引用する使い方もしない。

Bergh–Schnürer, *Decompositions of derived categories of gerbes and of families of Brauer–Severi varieties*, Doc.Math.26(2021),1465–1500、[公刊PDF](https://ems.press/content/serial-article-files/26626)、Proposition4.10、Remark6.1、Theorem6.2・Remark6.3を確認した。さらに [arXiv:1901.08945v2](https://arxiv.org/pdf/1901.08945) の Proposition5.7（p.23）の weight-zero derived 降下と、§6 の式(6.1)・tautological trivialization を確認した。Hom 剛性化で用いる P⊗L⁻¹ の降下はこの既知の一般原理であり、本文・ノートでは必要な重みと cocycle を直接計算する。Lindberg–Pym の原生成元 q 比、Theorem6.9・Remark6.10も全次数の対数境界値に適用する範囲を再点検した。

点規格化と kernel index の一次資料：

- Fulton–Olsson, *The Picard group of M₁,₁*, Algebra Number Theory4(2010),87–104、[公刊PDF](https://msp.org/ant/2010/4-1/ant-v4-n1-p04-p.pdf)、[DOI](https://doi.org/10.2140/ant.2010.4.87)。§1・式(1-1)–(1-5)、pp.87–88で Weierstrass 微分・判別式の変換、Corollary2.4の証明p.91で j≠0,1728 上の μ₂-gerbe を確認。Hodge 線・modular forms は既知であり、残余尺度への応用と区別する。
- Poonen, *Varieties without extra automorphisms III: Hypersurfaces*, Finite Fields Appl.11(2005),no.2,230–268、[著者稿](https://math.mit.edu/~poonen/papers/projaut.pdf)。Theorem1.1（著者稿p.1）のAut=Lin、Theorem1.5と直前の開性（p.2）を確認。三次n≥3は例外に属さない。sourceと残余標的の一般慣性を除く箇所、およびLiuの群Z×Aut(Y)を一般点のZへ帰着する箇所で使用する。
- Stacks [Tag07S5](https://stacks.math.columbia.edu/tag/07S5), Lemma66.14.2：自由な有限局所自由群作用の scheme 商と torsor。本文では有限 étale 残余射を affine な標的へ縮め、その affine source 上の定数群 Z/2 の反対作用に適用する。
- Stacks [Tag037P](https://stacks.math.columbia.edu/tag/037P), Lemma10.47.8、[Tag0322](https://stacks.math.columbia.edu/tag/0322), Proposition10.158.9、[Tag05DW](https://stacks.math.columbia.edu/tag/05DW), §10.49：相対的な代数閉性からの幾何学的既約性、標数零の体拡大の幾何学的被約性、幾何学的整性と任意の体拡大後の整域性を確認。引用keyは `NFMStacksRegularFields`。active基底変更での一般次数保持と二次類の定数体への降下に使い、Kummer類の判定自体は本文で証明する。
- Knudsen–Mumford, *The projectivity of the moduli space of stable curves. I: Preliminaries on “det” and “Div”*, Math.Scand.39(1976),19–55、[DOI](https://doi.org/10.7146/math.scand.a-11642)。刊行情報を出版社で確認。twisted perfect 複体への適用は次項の本文で確認し、determinant の重み計算は原稿内で記す。
- Lieblich, *Moduli of twisted sheaves*, [arXiv:math/0411337v2](https://arxiv.org/abs/math/0411337v2)、§2.2.4・Definition2.2.4.1、§2.2.5。perfect twisted 複体の determinant、rank・period・index の関係を確認。書誌は確認した arXiv 版で固定する。
- Stacks [Tag074S](https://stacks.math.columbia.edu/tag/074S), Lemma11.7.4、[Tag074X](https://stacks.math.columbia.edu/tag/074X), Lemmas11.8.3–11.8.4：極大部分体の次数と分裂、有限分裂体の次数による index の整除。
- Stacks [Tag0DME](https://stacks.math.columbia.edu/tag/0DME), Lemma108.9.1：Picard stack から Picard functor への射が gerbe となることと、fppf 局所での線束の実現・同型を確認。滑らかな幾何学的連結曲線では scalar band は G_m。最高次線束からの band を保つ射により、選択済み kernel gerbe を m_P に沿う pullback と同定する。
- Stacks [Tag0BFG](https://stacks.math.columbia.edu/tag/0BFG), [Tag0BFH](https://stacks.math.columbia.edu/tag/0BFH)：abelian variety の整数倍写像の次数と、標数に素な倍写像の étale 性。相対 Jacobian の [3] の階数9・有限 étale 性に用いる。引用 key は `NFMStacksMultiplication`。
- Stacks [Tag0BQI](https://stacks.math.columbia.edu/tag/0BQI), Lemma58.10.7：正規な整 scheme 上の有限 étale 被覆の generic fibre への完全忠実性。対称点を含む正規近傍へ延長した二つのtorsor の同型を延ばすために用いる。近傍への延長そのものをこの補題で得るわけではない。引用 key は `NFMStacksEtaleNormal`。

有限対角による符号消滅の一次資料：

- Benoist, *Séparation et propriété de Deligne–Mumford des champs de modules d’intersections complètes lisses*, J. London Math. Soc. 87(2013),138–156、[公刊PDF](https://www.math.ens.psl.eu/~benoist/articles/separticle.pdf)、[arXiv:1111.1582v2](https://arxiv.org/abs/1111.1582v2)、[DOI](https://doi.org/10.1112/jlms/jds045)。Theorems1.6(ii),1.7（公刊p.140）は3を可逆にした底での平面三次のDM性と分離性を与え、対角はproperかつquasi-finiteなのでfinite。Lemma2.2(iii)（p.141）はDVR上の二つのsmooth polarized complete intersection間の指定generic ambient PGL Isomが延びることを明記する。境界計算では、特異な点三次ではなく、飽和active代数のcyclic potentialから回復した滑らかな三次へ適用する。
- Stacks [Tag0CMX](https://stacks.math.columbia.edu/tag/0CMX), Lemma102.3.7：局所有限表示stackのlimit-preserving性。射・同型・有限descent datumを有限係数環へ降ろすために使う。指定有理Isomの一意延長は本文で正規環への整性から直接証明する。

相対 THCR/window1 と Picard 反例の一次資料：

- Keeler, *Ample filters of invertible sheaves*, J.Algebra259(2003),243–283、Corrigendum507(2018),592–598、[arXiv:math/0108068v5](https://arxiv.org/abs/math/0108068v5)：Proposition7.2、Lemma7.6。訂正を含む版を確認。本文ではamplenessをDVR上で直接確認しており、訂正対象の旧Lemma3.3に依存するgeneric alterationは使わない。
- Burke–Stevenson の DVR 上の Gorenstein/window 入力は上記の同文献を参照。active a=0 には Theorem6.4(3)、full 三次の境界 a=n−1>0 には Theorem6.4(1)を用い、適用範囲を混同しない。
- Stacks [Tag0B91](https://stacks.math.columbia.edu/tag/0B91), Lemma36.30.4：proper flat有限表示射上のperfect複体の押下げと任意底変更。相対windowにはこの各次数の主張とMF余核の実際の比較図式を併用する。
- Milne, *Class Field Theory*, version4.03 (2020-08-06), [著者PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf)：III§4 Steps1–2（印刷pp.111–112）の巡回norm判定、IV§3 Theorem3.14（印刷p.137）のcrossed productとBrauer群。反例のfactor setをこれと照合した。
- Fisher, *On some algebras associated to genus one curves*, [arXiv:1707.08330v1](https://arxiv.org/abs/1707.08330v1)：Theorems1.1–1.2、Corollary1.4、§§6–7。genus-one曲線に付随するJacobian上のAzumayaとTate評価は既知の背景であり、今回の明示計算やfull比較核への応用と区別する。

全 active FM 分類・cup 表示・実 Sklyanin 実現の一次資料：

- Hille–Van den Bergh, *Fourier–Mukai transforms*, Handbook of Tilting Theory, LMS Lecture Note Ser.332 (2007), Chapter7、[著者稿](https://cantate.be/site/hille.pdf)、[DOI](https://doi.org/10.1017/CBO9780511735134.007)。Proposition4.2、Corollary4.3、Theorem5.3と証明。数値作用・点対象からの graph 認識と elliptic 自己同値の一般論を照合し、本稿では指定 rotation の centralizer、非閉体への実核の降下、相対 gerbe と周期標識を分けて証明する。引用 key は `NFMHilleVdBFM`。
- Ciperiani–Krashen, *Relative Brauer groups of genus 1 curves*, Israel J.Math.192(2012),921–949、[著者稿](https://web.ma.utexas.edu/users/mirela/BrauerGroups.pdf)、[DOI](https://doi.org/10.1007/s11856-012-0057-5)。Theorems3.1、3.7（pp.929–933）。Picard 障害の Tate 評価と有限 Weil cup の順序を確認。本稿の flex lift・I_sc 移送・選択済み full 核への適用と、既知の pairing 一般論を区別する。引用 key は `NFMCiperianiKrashen`。
- Cremona–Fisher–O'Neil–Simon–Stoll, *Explicit n-descent on elliptic curves. I. Algebra*, J. reine angew. Math.615(2008),121–155、[arXiv:math/0606580v1](https://arxiv.org/abs/math/0606580v1)、[DOI](https://doi.org/10.1515/CRELLE.2008.012)。§§1.1・1.3・1.6、Proposition2.2、Lemma2.4で theta group と degree-three divisor-class pair の descent、obstruction の対応を確認。非分裂曲線の偏極類と β の規約に用いる。二つの独立な Kummer 座標による α の index 九の付値証明と、一ブロック mixed 族への実現は本稿で記す。引用 key は `NFMCremonaFisherDescentAlgebra`。
- David J. Saltman, *Genus 1 Curves in Severi--Brauer Surfaces*, [arXiv:2105.09986v1](https://arxiv.org/abs/2105.09986v1)（2021-05-20）。§§3–4、Theorem5の Heisenberg 表現と Brauer–Severi surface 内の滑らかな genus-one 三次の関係を比較対象として原著確認した。こうした曲線の存在や period–index 現象そのものの新規性は主張しない。本稿では点 p の Picard 障害 α と偏極障害 β を明示的に分け、mixed 一ブロック族への実現と普遍重み一階数へ用いる。引用 key は `NFMSaltmanSeveri`。
- Matsuno, *A Complete Classification of 3-dimensional Quadratic AS-regular Algebras of Type EC*, Canad.Math.Bull.64(2021),123–141、[arXiv:1912.05167](https://arxiv.org/abs/1912.05167)、[DOI](https://doi.org/10.4153/S0008439520000302)。§2.4、Lemma2.16、Theorem3.3、§4、Corollary4.3。Hesse 型の幾何的 Sklyanin 代数、正則性と cyclic potential の一次資料。本稿では曲線の原点や p の線束を仮定しない体上への降下と、障害を保つ支配族への拡張を補う。引用 key は `NFMMatsunoElliptic`。
- Mori–Smith の既存書誌 `MoriSmith`、Proposition2.11、Theorem4.2(1)：potential と commutator–gradient 形式、滑らかな三次の3-Calabi–Yau条件との関係。本稿の有限恒等式・算術的降下・純超越的支配性は別に本文で検証する。

projector核・低次元full自己同値分類の一次資料：

- Canonaco–Stellari, *Non-uniqueness of Fourier–Mukai kernels*, Math.Z.272(2012),577–588、[著者PDF](https://sites.unimi.it/stellari/Research/Papers/NonUniq.pdf)、[arXiv:1009.5577](https://arxiv.org/abs/1009.5577)、[DOI](https://doi.org/10.1007/s00209-011-0950-3)。Theorem1.2、Proposition4.3、Corollary4.4（著者稿pp.10–11）で、同型なFM関手の核の各cohomology層が同型となることを確認。核自身の一般的一意性は主張されておらず、本稿ではprojectorのsimpleな点像とPic(Y)のtorsion-free性を追加して一意性を証明する。引用keyは `NFMCanonacoStellariKernels`。
- Ziqi Liu, *On Fourier–Mukai type autoequivalences of Kuznetsov components of cubic threefolds*, Math.Nachr.297(2024),1866–1878、[arXiv:2304.12669v2](https://arxiv.org/abs/2304.12669v2)、[DOI](https://doi.org/10.1002/mana.202300237)。Theorems1.1・4.13、§§2.2–2.3、Proposition3.5・Example3.7を確認。全ての滑らかな複素三次三次元多様体についてAut^FM(KuY)=Z×Aut(Y)、S=ρ[1]、S³=[5]を用いる。一般点ではAut(Y)=1、T=S⁻¹[2]=ρ⁻¹[1]が生成元となる。引用keyは `NFMLiuCubicThreefoldAut`。
- Huybrechts, *The K3 category of a cubic fourfold*, Compos.Math.153(2017),586–620、[公刊PDF](https://compositio.nl/Content/prize2021_huybrechts.pdf)、[arXiv:1505.01775](https://arxiv.org/abs/1505.01775)、[DOI](https://doi.org/10.1112/S0010437X16008137)。Theorem1.2(i)（公刊p.587）のvery generalな三次四次元多様体の全FM自己同値群Zと、[1]の生成する部分群の指数三を確認。Proposition3.12、Corollary3.13、§§3.4–3.5・6.1が関連箇所である。本稿では可算bad lociと核の有限データを用いて幾何学的一般点へ適用し、Zariski開上の全対象の定理とは扱わない。引用keyは `NFMHuybrechtsK3Cubic`。
- Iliev–Manivel, *On cubic hypersurfaces of dimensions 7 and 8*, Proc.London Math.Soc.(3)108(2014),no.2,517–540、[arXiv:1102.3618v2](https://arxiv.org/abs/1102.3618v2)、[DOI](https://doi.org/10.1112/plms/pdt042)。Proposition3.1の一般七様体のCartan表示、Theorem3.4、Proposition5.2、Corollary5.3の階数九の束とKu内の三次元球面対象を確認。本稿の数値作用の計算は、その既知対象のtwistからZ²とrotation中央化群の無限指数を取り出す。球面対象の存在を本稿の新規結果とせず、全ての特殊七様体にも拡張しない。引用keyは `NFMIlievManivelSevenfold`。

高次元の文献比較では、Lin–Rennemo–Zhang, *Categorical Torelli theorems for weighted hypersurfaces*, Adv.Math.503(2026),PartC,111271、[DOI](https://doi.org/10.1016/j.aim.2026.111271)、Theorem1.3（Theorem3.12・Corollary3.13）、Lin–Zeng–Zhang [arXiv:2610.00130v1](https://arxiv.org/abs/2610.00130v1)、Proposition2.1・Remark2.2、Lin–Zhang [arXiv:2611.05915v1](https://arxiv.org/abs/2611.05915v1)、Theorem1.3のstatementを原著で確認した。順にweighted hypersurfaceの復元、Serre関手からの内部shiftの回復、三次四様体を除くCalabi–Yau型のFourier–Mukai partner数の有限性に関する結果である。最後の対象は標的多様体の数であり、固定標的への核の数ではない。これらの全証明の独立点検はしておらず、高次元class選択の証明入力にも用いない。

五次元の安定性条件と有限安定化群の比較に必要な一次資料：

- Peize Liu, *Stability conditions and moduli spaces on the Kuznetsov component of cubic fivefolds*, [arXiv:2509.21454v5](https://arxiv.org/abs/2509.21454v5)（2026-08-03）。Theorem2.8、§2.2の式(2-4)・Remark2.11の Ψ⊣Φ と rank 四局所自由 module、Lemmas2.12–2.14 の mutation 比較、Lemma3.4、Corollary3.10(ii)、Proposition3.11 の rotation と数値作用を確認。Theorem5.5の証明は Clifford rotation が構成した安定性軌道を保つこと、Corollary5.10は Serre 不変性を与える。Proposition6.10の Fano 曲面は最小 stable moduli の一つの連結成分であり、全体の既約性は Remark6.11 の予想、Serre 不変軌道の一意性は Remark5.6 の未解決問題である。本稿では相対核・平面非依存性・奇数零 cycle による元の体への降下と E_p の二 mutation 表示を補う。さらに spinor 列の随伴 unit と相対・絶対 coevaluation を比較し、O≃ρ⁻¹[1]、ε≃id を perfect 核として同定する。引用 key は `NFMPeizeLiuFivefold`。
- Alexander Kuznetsov, *Derived categories of quadric fibrations and intersections of quadrics*, Adv.Math.218(2008),1340–1369、[公刊著者PDF](https://homepage.mi-ras.ru/~akuznet/publications/DerivedCategoriesOfQuadricFibrationsAndIntersectionsOfQuadrics.pdf)、[DOI](https://doi.org/10.1016/j.aim.2008.03.007)。Theorem4.2、Lemmas3.8・4.5・4.6・4.7・4.10、Remark4.8（公刊 pp.1353,1357,1359–1361）を確認。Clifford module の局所射影性、実際の局所自由 kernel、有限振幅、随伴が相対半 rotation の構成に必要である。absolute perfect から相対 perfect を無条件に推論せず、相対 Clifford 模型と滑らかな幾何学的 kernel で確認する。引用 key は `NFMKuznetsovQuadric`。
- Alberto Collino, *The Abel–Jacobi isomorphism for the cubic fivefold*, Pacific J.Math.122(1986),43–55、[公刊PDF](https://msp.org/pjm/1986/122-1/pjm-v122-n1-p04-s.pdf)。Propositions1.8・1.10（公刊 p.46）の Fano 曲面の連結性・一般の滑らかさと既約性を確認。本稿では一般の残余五様体に適用し、相対核の離散 class 写像が一定になることへ使う。引用 key は `NFMCollinoFivefold`。
- Ciro Ciliberto–Mikhail Zaidenberg, *On Fano schemes of complete intersections*, in *Polynomial Rings and Affine Algebraic Geometry*, Springer Proc.Math.Stat.319(2020),1–39、[DOI](https://doi.org/10.1007/978-3-030-42136-6_1)、[著者稿 arXiv:1903.11294v2](https://arxiv.org/abs/1903.11294v2)。著者稿 Example4.4（p.20）の cubic fivefold の Fano 曲面の Plücker 次数2835と係数公式を確認した。数値自体は既知で、本稿では整数多項式で再現し、二捩れ kernel gerbe の corestriction に用いる。引用 key は `NFMCilibertoZaidenbergFano`。
- D. Wu, *Construction of stability conditions on some Kuznetsov components*, [arXiv:2611.02388v1](https://arxiv.org/abs/2611.02388v1)（2026）。Theorem1.3、Proposition7.2の各numerical stability連結成分が自由なGL̃₂⁺軌道となるstatementを原著で確認した。自己同値群の作用の忠実性やH_p=1を与える定理としては使わず、全証明の独立検証もしていない。引用keyは `NFMWuStability`。
- A. Aravena, P. Liu, J. Tevelev, *Gepner stability conditions on hypersurface categories*, [arXiv:2611.05350v1](https://arxiv.org/abs/2611.05350v1)（2026）。Theorem1.2、Corollary1.3のGepner安定性条件の存在のstatementと適用範囲を確認した。H_pやS_pの自明性の証明入力には用いず、全証明の独立検証とも区別する。引用keyは `NFMAravenaLiuTevelevGepner`。

指定MF周期の規約は、固定入力B `papers/sections/generic_recovery/local_model.tex` の `lp:prop:sing-period`、`window.tex` の `tw:eq:period-extension` と `tw:eq:rotation-period-square` に置かれている。前者の双加群truncation境界とconormal基底、後二者のYoneda二拡張と実際のrotation比較を照合した。周期の中心的coherenceと生成元変更のu⁻¹則はこの指定規約に関する主張であり、任意に選び直したfractional Calabi–Yau自明化の自然性を仮定しない。

周期位相の混合定数降下では、同じ固定 B の `cft:lem:arity`、`cft:lem:flow`、`cft:eq:bound`、`cft:eq:object`、`cft:eq:insertions`、`cft:eq:two-block-matrix` を使用する。三対象生成と actual Hom の局所化には `gcd:prop:bound`、`tw:lem:proper-hom`、`rog:lem:localization` を用いる。局所化前の integral な有限 MF の Hom を先に比較する範囲を保持し、任意の Laurent 係数 MC 元への収束を新たに主張しない。Fisher の Theorem1.1・Lemma2.2・§9.5 の不変式・一般軌道・Heisenberg 群と、既存の全三捩れモノドロミーを合わせた μ₃-character の消滅が、二変数不変量体への降下に必要である。

Murfet, *Residues and duality for singularity categories of isolated Gorenstein singularities*, Compos.Math.149(2013),no.12,2071–2100、[arXiv:0912.1629v3](https://arxiv.org/abs/0912.1629v3)、[DOI](https://doi.org/10.1112/S0010437X13007082) のTheorem6.2・式(6.6)、Proposition4.2・式(5.7)を確認した。MFの微分と射を含むresidue trace、およびdeterminantの変換則を、γ_scの計算候補として保持する。sourceから移した実際の微分・射とAS-Gorenstein traceの規格化をまだ同定していないため、指定した位相の大域値の証明としては用いていない。引用keyは `NFMMurfetResidue`。

自然な残余射・active曲線比較・正確な一般次数18・符号消滅とfull射の次数9・最高次線束型・点型の全O-降下・三分点被覆の九次性と216次monodromy・低次元のfull class降下・随伴復元条件による有限class torsor・周期位相とcube frameの算術への適用について、初出と新規性の網羅的確認は未完了である。既知の曲線同型理論、Hessian点曲線、Hesse群・古典的不変式環、determinantによるBrauer消去、Picard gerbe、楕円導来圏の自己同値一般論、Tate–Weil pairing、Sklyanin理論、LiuとHuybrechtsの自己同値群分類、Toën–Vaquiéのmoduli、Murfetのresidue公式自体を新規成果としない。非被約相対分類、実active族への算術的降下、H_gのfull ambient作用による平面同型torsorの分裂、残余側のexact index、projector核の一意性と定数ZによるGalois降下、有限 H_p への縮約、五次元半 rotation の平面非依存性・奇数零 cycle による降下、非分裂点 Picard index 九の一ブロック実現と普遍最小階数、指定周期の cube frame と scalar gerbe の算術との接続を、これらの既知入力から区別して記載する。

### 境界の Kummer 計算の一次資料

Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer (2009), DOI 10.1007/978-0-387-09494-6。[一次資料PDF](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf) の Chapter XI, Proposition 9.2 と直前の定義（印刷pp.398–400、PDF pp.409–411）を確認した。pairing は e₃(σQ−Q,T) であり、div(f)=3(T)−3(O) に加えて f∘[3] が K(E) 内の三乗である規格化を要求する。原点で先頭係数一の接線比はこの仮定を満たすことを本文で証明した。Appendix C, Theorems 15.1–15.2、Corollary 15.2.1 の正則模型・成分群も確認。Kummer 理論や I₃ 成分群は既知結果であり、本稿の点 shift の局所体と有限行列表示の計算と区別する。

- Eisenbud, *Homological algebra on a complete intersection, with an application to group representations*, Trans.AMS260(1980),35–64、[DOI](https://doi.org/10.1090/S0002-9947-1980-0570778-7)、[原著PDF](https://ssather.people.clemson.edu/fa11/790-3/eisenbud.pdf)：Theorem7.2（公刊pp.56–57）を原著確認。有限自由分解と高次 homotopy から超曲面商上の自由分解を作る既知の Shamash 構成である。本稿では線型行列 L と中心 Koszul 分解に対し dh+hd=F、h²=0 の明示 homotopy を与え、各 parity の階数3·2^(n−1)と内部 shift を記述した。この一般構成や MF の周期性自体の新規性は主張しない。引用キー `NFMEisenbudCI`。

### Tate–Koszul と Clifford 同定の一次資料

- Lu–Palmieri–Wu–Zhang, *Koszul equivalences in A∞-algebras*, New York J. Math.14(2008),325–378、[一次PDF](https://nyjm.albany.edu/j/2008/14-16.pdf)。Definition2.1 の Adams connected 条件、Theorem2.4 と Corollary2.5(b)、pp.338–340 の二重双対と homotopy Hom の反変全単射を確認。局所有限性を内部次数ごとに確認して適用する。引用キー `NFMLPWZKoszul`。
- 同著者, *A∞ structure on Ext-algebras*, J. Pure Appl. Algebra213(2009),2017–2037、[著者PDF](https://sites.math.washington.edu/~palmieri/Papers/ext-a-infty.pdf)、Theorem A と Corollary B。関係式を高次積から回復する既知入力であり、三次テンソルの gauge 不変性を主張する文献ではない。`NFMLPWZExt`。
- Braun–Chuang–Lazarev, *Derived localisation of algebras and modules*, Adv.Math.328(2018),555–622、[arXiv:1505.01146v3](https://arxiv.org/abs/1505.01146v3)、[DOI](https://doi.org/10.1016/j.aim.2018.02.004)。Proposition3.17、Theorem3.18 の homotopy epimorphism と mapping-space fibre、Theorem5.3 の中央 class の cohomology 局所化を確認。書誌は著者機関 City の公開記録とも照合。`NFMBCLLocalization`。
- Keller, *On triangulated orbit categories*, Doc.Math.10(2005),551–581、[著者PDF](https://webusers.imj-prg.fr/~bernhard.keller/publ/triaorbit.pdf)、§§9.3–9.4。実際の quasi-functor の比較同型を cofibrant bimodule へ持ち上げ、orbit 関手と合成整合性を作る箇所を確認。[2009訂正](https://webusers.imj-prg.fr/~bernhard.keller/publ/corrTriaOrbit.pdf)も確認し、旧§7の hull 表示と周期・Serre に関する修正前の主張は使わない。`NFMKellerOrbit`。
- 五次元全関手同定には既存 Kuznetsov 文献の Lemma4.5（spinor 列）・Lemma4.7（局所自由性）、Liu v5 の式(2-4)、Lemma2.12、Corollary3.10(ii)を使用。新しい部分は spinor 射の adjunction unit としての同定、相対・絶対 coevaluation と Beilinson defect の比較である。指定 square/period の同時正規化は扱わない。

これらの既知の一般定理と、現行稿の Tate cutoff・核への忠実性・全次元の強化 class 選択への適用を分ける。全引用・被引用文献を尽くした新規性調査、外部査読、形式証明器の検証は未完了である。

## 8. 再現の入口

README の再生成手順で、ソース参照、二次・三次の保存済み証明書、LuaLaTeX 組版を確認できる。`python3 scripts/check_sources.py` で三稿の入力・引用・ラベル・他稿参照を検査し、ルートで `python3 scripts/build_papers.py` を実行して組版する。PDFは `build/nc-cubic.pdf`、`build/cubic-moduli-descent.pdf`、`build/mixed-sklyanin-cubics.pdf`、SyncTeXも同じ `build/` に出す。次数三の検証は Python・NumPy と C++17 コンパイラを用い、大きな行列を `build/jacobi-vertex/` に再生成する。証明に必要なテンソル・選択行・検証コードを保存し、再生成できる大行列自体は収録しない。

trace–Hessian の中心係数・八次代数 trace、全次元の KS 例、split Hesse の有理式と j 差、混合係数の二次恒等式についても、README と `notes/validation.md` にある該当手順と確認範囲を参照する。厳密な記号計算による係数検証を、未公表入力の非可換中心性・完備 MF 移送・一般点復元の全証明の独立検証と同一視しない。任意次元・任意基底の主張は、有限個の計算例だけでなく本文の相対証明に依拠する。

混合五次 tensor の再現は `computations/verify_mixed_fifth.py` と必要最小限の重み証明書 `computations/data/harmonic_linear_products.json`、中心逆像の四次恒等式・Jacobi 非消滅・古典的共変式の恒等式は `computations/verify_fourth_potential.py` に収める。両者とも Python と SymPy を用い、グラフ縮約は整数・Fraction、係数恒等式は有理数係数の多項式として厳密に計算する。既知重みの使用、係数恒等式の検算、一般次元の証明、形式証明器による検証は異なる状態として記録する。新たな四次の中心グラフ積分は行っていない。

active 不変量の有限式は、ルートから `python computations/verify_active_invariants.py` を実行して再現する。SymPy の QQ 上で不変量・判別式・Jacobian・点線束行列と MF 曲率の有限恒等式を扱う。境界の二次・三次積と一次項は別の有限行列証明書で扱い、実行範囲と出力の状態は `notes/validation.md` を参照する。一般 fibre の幾何学的整性、全次数の有限混合三角性、飽和代数の平坦性、Isom 延長と Kummer 降下の証明を、有限恒等式の検算そのものと同一視しない。

Hesse 体の二次類単射に用いる有限恒等式は、`python computations/verify_active_sign.py` で再現する。QQ(ζ)、ζ²+ζ+1=0 上で不変量の保存、四元数群と C₃ の関係、群の位数24、次数の上界を与える四次・三次恒等式、非自明な μ₂ 指標の不存在を検算する。全次元の滑らかさの証明に現れる二つの整数の非消滅も確認するが、scalar symmetrizerの全次元の証明、有限対角による延長と同変降下、χ_actの消滅の全論証を計算で代用するものではない。実際の実行結果は `notes/validation.md` を参照する。

最高次線束型の graded purity、PBW の中心平坦性、Tor-independent な MF 係数商、Galinat の同じ window における shift・rotation、cohomology の平坦化と gerbe 上の貼合せは内部で独立に読解した。Picard 障害・active 曲線上の分裂・階数3 Azumaya も紙上の証明による。完備中心切断の bar 恒等式、係数商と relative perfect 性の反例、次数二中心の formality 反例、有限四角の PGL_d 障害、内部次数を忘れた無限 coherence の例、Hom 剛性化はノートの証明で確認できる。実際の Morita 核と curved-bar 模型の同定は未完成であり、条件付き振幅評価と区別する。外部査読・全固定入力の独立検証・形式証明器による機械検証を行ったという意味ではない。

三倍線束の重み・零切断での相殺・底変更と、三分点被覆上の規格化の一意性は紙上で独立に点検した。右 THCR の符号と楕円 rotation の二つの shear、形式恒等核からの graph-support、Picard 等式を保つ有限降下も内部で独立に読解した。これらには別の検算コードを設けず本文の証明を正本とする。指定中心商の相対THCR/window1と閉／一般底変更は本文の証明を執筆担当以外の二担当も読解点検した。一般の特異圏の底変更とは区別する。符号消滅には別に有限対角による延長補題を証明し、特殊点の非自明な慣性を含むC₃同変降下を独立に点検した。

Picard 障害と三捩れ monodromy の有限恒等式は `python computations/verify_picard_obstruction.py` で再現する。Hesse 接線・norm・点三次・係数逆、数値 rotation centralizer、巡回 twist、symbol と三捩れ点の恒等式を扱う。既存の計算資産と証明書を保持し、各版で実際に実行した範囲は `notes/validation.md` を正本とする。付値による非norm性、一般係数体への降下、gerbe・導来圏の一般証明は有限検算と区別する。

五次元 Fano 曲面の次数は、`python3 computations/verify_fivefold_plane_degree.py` で再現する。Sym³S* の Chern 根の積と Grassmann 積分から

\[
 [x^6y^5z^4]\!
 \left(\prod_{a+b+c=3}(ax+by+cz)\right)
 (x+y+z)^2(x-y)(x-z)(y-z)=2835
\]

を整数演算だけで検算し、PASS を確認した。Chern 根は tautological bundle の双対 S* の規約である。この既知の次数の再現と、実相対核・class の連続性・2β_O=2835β_O=0による降下の紙上の証明を区別する。半 rotation の構成、随伴の向き、relative C_i の例外性、ε の安定性軌道固定、E_p の二 mutation と十五次元評価核は、一次資料との照合を含め内部独立点検を済ませた。

非分裂点障害の period 三・index 九は、二変数の付値を用いる division 証明、theta factor set の符号、Tate pairing、mixed 表示への twist と純超越的な支配性を紙上で点検した。普遍重み一階数九の上界と全非空開での下界、非分裂強化点型の降下と共通慣性自明開の全 n≡1 mod3 における未標識最小次数九は別の一般証明であり、2835の有限計算では検証していない。外部査読・新規性の網羅的確認は未完了である。

全 FM 判定の数値規格化・graph 認識・偏極条件と、非被約底の相対分類・μ₃位相と G_m inertia の区別は、本文の証明を別担当が独立に読解した。CK の符号規約、一般 j の巡回例、Sklyanin の既知仮定と本稿の降下の区別も一次資料と照合している。これは外部査読や形式証明器での検証とは異なる。検証の実行範囲と原稿の論理的な証明を分ける。

κのSerre基底線束の相殺、q_YのA_C-linearなKoszul/window比較、projector核の一意性、n=3,4の既知自己同値群からのclass降下は紙上で独立に読解した。三分点被覆の九次性と216次群の一般証明は、上の四つの有限恒等式とは別に本文を正本とする。新規補題の執筆・内部点検、文献の一次確認、計算の実行、組版、保存を一括して同じ検証とは呼ばない。

指定 MF 周期の中心的 coherence、T^m による class 不変性、相対 frame の変換則、混合有理比較と C(s,t) への降下を、指定した入力と照合して内部で独立点検した。境界の局所値 [D_R] には、実際の低積とその一次項、二次関係の飽和、全次数平坦性、smooth potential 三次による Isom 延長を組み合わせる。有限行列の実行確認、紙上証明の点検、組版、外部査読、形式証明器での検証を別々に扱い、実施状態は `notes/validation.md` に記載する。ΔD 外の分岐排除と大域式 [D] は未証明である。

随伴復元による強化点型では、q^RO_C≃j_Y!OのKoszul証明、両ファイバーを用いるDVR上の最高次線束の持上げ、coneのproper性による非空型の有限降下を紙上で点検した。有限H_pには固定入力Bの三対象生成、Morita核のfree A^e、TV Proposition3.20と可逆核の開性、HH¹=0を実際に照合した。S_p×Pic_C^p、低次元の唯一のclass、Euler格子による奇数次元の数値的自明性、最小実現次数公式は一般証明であり、新たな計算コードや有限例だけによる確認ではない。全moduli上の実核の存在は主張しない。一方、全次元の一般一ブロック族でH_p=1、S_p=Spec(k_n)となる別のTate–Koszul証明は、既存の独立読解点検の対象である。

高次元の中央shift部分の除去、classと軌道の安定化群の一致、奇数次元の数値格子・六元中央化群、七次元のZ²とrotation中央化群の無限指数は、本文の証明を別担当が独立に読解した。Iliev–Manivelの球面対象は既知入力と分け、数値的自明な自己同値の分類や対応torsorの中立性まで検証したとはしない。

外部文献 PDF、旧版原稿、旧 ZIP、担当者別の重複レポート、コンパイル中間生成物は現行一式に含めない。主張の証明・証明書の生成・実際の検証・保存は別の状態として扱い、検証事実の正本は `notes/validation.md` とする。
