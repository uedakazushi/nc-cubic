# 非可換三次 n-fold のモジュライ

2026年11月20日 / v8。日本語 LuaLaTeX による現行研究稿と、研究継続に必要な最小限の資料・厳密計算証明書。

**再開時は [研究方針](00_research_plan.md) を最初に読む。**

## 内容

- [公表用研究稿](papers/nc-cubic-n-fold.tex)：中心復元、局所一ブロック型の O-marked DM stack と Brauer 障害、相対点関手と中心商の復元、trace–Hessian による Poisson 対の開部分との同型、残余復元との比較障害、次数9の代数的 Poisson 補正、形式 support 保存と五次の尺度補正、split 族の残余比較、Jacobi スキーム、残余圏の通常 Artin 形式認識。
- [研究ノート](notes/research_notes.md)：主張の依存・適用範囲、反例・障害、文献の確認箇所、次の計算の入口。
- [検証範囲](notes/validation.md)：原稿点検・組版・厳密計算を区別した確認状態。
- [Jacobi 行列検証コード](computations/verify_jacobi_rank.py) と [整数小行列証明書](computations/jacobi_rank_certificate.json)。
- [八次元の頂点構造の検証コード](computations/verify_jacobi_vertex.py)、[C++ 検証器](computations/verify_binary_minor.cpp)、[次数三の全射性の証明書](computations/jacobi_vertex_certificate.json)。
- [中心評価・Hessian・trace の厳密検算](computations/verify_center_hessian.py)。
- [幾何補正・残余比較の厳密検算](computations/verify_geometric_corrections.py)：全次元の Jacobi 双対証明書、trace、普遍二次テンソル、Hesse 不変量。
- [Poisson 補正の厳密検算](computations/verify_poisson_correction.py)：一般三変数三次の点曲線、二パラメータ Hesse 公式、中心係数、尺度の変換、一般混合係数の線型復元行列、framed 被覆の分岐。
- [三次共変式の厳密検算](computations/verify_cubic_covariants.py)：Weyl 重複度、四次不変式の規格化、五次混合項の二定数への還元。
- [参考文献](papers/references.tex)。外部文献PDFは含めない。

直接の入力は [nc-cubic](https://github.com/uedakazushi/nc-cubic/tree/eabe601c1341777742964584dde5314c0bcf64a9) の論文A・B。これらが既に扱う一般次元の正規形・量子化・一般点復元を、新しい成果として数えていない。

## 現在の研究目標

**一般次元の O-marked moduli、point scheme、Poisson 多様体のモジュライへの射、Kuznetsov 成分の比較**を中心に進める。各既約成分の general / very general な対象を優先し、次元に一様な定理と族の構成を目指す。general な稠密開と very general な点集合、一ブロックの表示成分と全モジュライの成分は区別する。

良い一ブロック型で、O-marked 圏 stack と分解可能な Poisson 対の非空開の同型を構成した。一方、固定入力の残余復元の下で **trace–Hessian 射の X_TH と X_res が異なる全次元の Hesse 族**があり、固定した周囲 tensor の純中心補正では修復できない。一般混合係数でも、指定 formality 模型の下で marked な形式比較に二次 jet の障害がある。この障害を打ち消す代数的 Hessian–trace 補正 Φ を構成し、全 O-降下と適切な開上での有限 étale 階数9を証明した。固定 formality の全次数では support が保存され、残余三次が tensor を scalar 倍まで決める。split 族では補正後三次と残余圏の全次数比較を固定入力の下で得た。c₂の消滅と偶奇性により W≡H♯ mod h⁴を得る一方、固定 tensor は五次で異なる稠密開を決定した。次は一般混合係数の W₄・π₅と残余同値の降下を進め、各 intrinsic 成分の一般対象を覆う表示を研究する。

個別次元の Jacobi 計算と boundary の精査は、この一般目標の具体的な障害を解消する場合に行う。八次元の頂点構造等の既存成果と証明書は保持する。次の具体的な着手方法と各目標の到達基準は [研究方針](00_research_plan.md) にまとめ、全体の要約は [research-hub](https://github.com/uedakazushi/research-hub) に反映する。

## 主要結果と未完成部分

一ブロックの周囲代数の次数付きモジュライの次元は `(n²+7n−4)/2`、中心三次 torsor の相対次元は `binom(n+1,3)`。良い相対 PBW 表示チャートでは、有限 Koszul 対角、真正な双加群双対、compact 性、相対 properness、Serre 関手 `S=(1−n)[n]` と trace を任意底変更に両立して構成した。

固定した良い表示模型間では、任意係数変更を圏内の係数作用として構成し、全 O-保存同値と自然同型の fpqc 降下を証明した。全同値の層は `Isom_gr/G_m` に一致する。同値を大域の次数付き同型で表す障害は `Pic(R)[n−1]` の線束であり、次数一部分がともに自由なら `Pic(R)[gcd(n−1,3)]` に入る。従って `n≠1 mod3` では全同値に大域の次数付き代表がある。`n≡1 mod3` では、滑らかな affine 曲線上の非自明な三捩れ線束による良い PBW 模型の明示例で、指定した同値の大域持上げが存在しないことを示す。

良い一ブロック模型に fpqc 局所的に同値な O-marked Grothendieck 圏族は、重み付き次数加群の tails によって効果化され、滑らかな既約 DM stack `[Jgood/P̄]` として分類される。次数一 shift は標識に含めない。大域次数付き表示の障害 β∈H²(G_m) は `gcd(n−1,3)` で消える。`n≡1 mod3` では、**任意の非空開**に β≠0 の C(s,t)-点が存在し、普遍障害の位数は正確に3である。これは上の指定同値の Picard 障害とは別の結果である。

楕円境界・固定点なし・中心三次非零因子の条件下で、相対点スキームは `E⊔D`。臨界スキーム C=V(F_x,F_y,F_z) は中心への有限局所自由八重被覆であり、その三次切断 D は型 `(2,2,2,3)`、各 fibre の次元 `n−3`、次数24である。これらの構成は任意基底変更に両立する。点商関手・shift・中心射影は O-marked stack 上に降下し、非空開では埋込み点対応から中心直線 [w] まで回復する。従って A=B/(w) 全体を復元できる。

正規化 trace `Tr/8` と尺度付き Hessian によって量子中心三次と古典三次 Casimir を同定する。さらに任意基底上で、滑らかな三次の相対双ベクトルには `ι(dH)Π=0` を満たす一意な強い affine lift `Π=ι(dH)P` がある。この結果から Poisson 対だけで support・二次関係・中心直線を回復し、**Msm≅Pgood⊂Pdec** を得る。周囲 B 単独の有限安定化子は要求せず、良い PBW・中心・相対双対・全同値比較を満たす pair を扱う。次元は `binom(n+2,3)+3n−2`、Brauer 障害の位数も同じである。標的は Brauer–Severi ambient と偏極類を許し、実際の相対 O(1) の存在は別条件である。

既存の一般三次の被約 Poisson 分類を使うと、一般三次の非空開上では全非零 Poisson moduli への開埋込みとなる。滑らかな三次 moduli を支配する Poisson 成分は一つだけで、本構成はその一般部分の開を同定する。特殊三次上の別成分や、全 intrinsic 圏成分の分類を含む主張ではない。

**Kuznetsov 比較には具体的な障害がある。** 固定入力論文Bの完備移送・一般点復元の下で、全 n≥3 の split Hesse 族に対し `λ_TH=h`、`λ_res=(h+h²/3+h⁵/12)/(1−h⁴/4)` を得る。三重線形形式の symmetrizer が active な平面三次を回復し、その j 不変量の差は `13824h⁴+O(h⁵)`。従って一般ファイバーは代数閉拡大後も同型でなく、非可換残余圏と Ku(X_TH) との rotation 保存 dg Morita 同値はない。`n≢1 mod3` では rotation なしでも同値はない。同じ ambient Π のどの smooth cubic Casimir を選んでも、この例の X_res は得られない。

一般混合 Hesse 表示では、短い中心式から h²ABC/6 を引いた Hessian jet の規格化を固定する。Dito の二次星積と Shoikhet の内向き wheel 消滅を用いる指定 formality 模型で、残余 potential と trace–Hessian 像の最初の差は `h²(Hess_active(F)/24+tr(Hess_active(F))/12)` となる。その全 Jacobi 類は非空 Zariski 開で非零であり、marked な形式比較を妨げる。この有限 jet の結果から、標識を外した全ての一般ファイバーの圏非同値までは結論しない。入力定数族に対する純中心補正の非自明性も別に全次元で証明した。

代数的補正は、`D_P(H)=〈det(D_K²H),P⊗P〉` と正規化 trace τ による `H♯=H+D_P(H)/24+τ(D_P(H))/12` である。`Φ:(H,P)↦(H♯,P)` は任意基底変更・方程式の生成元・全射影同型に両立し、O-marked moduli の非空開へ降下する。適切な稠密開上で表現可能な有限 étale 射となり、階数は全 n≥3 で9である。support を残した零切断の形式近傍では可逆だが、この補正射自体は有理同型ではない。次数9は同一座標群の商 stack の射の次数であり、慣性群を調べず粗モジュライの次数とは同一視しない。`H♯|K` は元の量子代数の楕円点曲線に厳密に一致する。この点曲線公式自体は Mori–Smith の既知結果である。

固定した harmonic-angle formality の下では、生成元を固定する逆 Poisson tensor π_h は二次関係から一意に決まり、元の中心一次空間を全次数で保存する。滑らかな三次と滑らかな active 制限の下で `π_h=a_hι(dW_h)P`、`a_h=h+O(h²)` となる。中心逆像は純中心三次を固定する。既知の Kontsevich の形式対応を使う結果であり、有限 h の収束・代数化は含まない。

係数が h に依存しない二次関係と Hessian 正規化中心元では、`c₂=0`、π_h と a_h は奇級数、W_h は偶級数となる。従って `a_h=h+O(h⁵)`、`W_h≡H♯ mod h⁴`、`π_h≡Π♯ mod h⁵` が全混合係数で成立する。さらに純 active 三次 g では `π₅(g)=S(g)Π_g/80`。四次不変式の規格化は `S(xyz)=1`、`S((x³+y³+z³)/3+λxyz)=λ(λ³−8)` である。一般混合係数も U=0 へ制限すると同じ式となるため、S(g)≠0 の稠密開で実際の tensor と有限 Hessian 補正は五次から異なる。証明は Lindberg–Pym の既知の量子トーラス交換比と、共変式の一次元性を用いる。この相違だけから残余三次や Ku の非同値を結論しない。

五次の全混合 tensor も、明示的な三次共変式 I,J を用いて `π₅=Π_Q₅`、`Q₅=S(g)F/80+β(I−S(g)F)+γ(J−S(g)F)` と書けることを証明した。β,γ は次元によらない二つの普遍定数で、値は未計算である。分離型とその中心平行移動では追加二方向が消えるため、混合係数の評価が必要になる。残余四次項は `W₄=Q₅−a₄F+G₄(U)`。全Jacobi環では[F]=0なので、幾何的な四次障害はβ,γと純中心項G₄の計算へ絞られる。

**全 n≥3 の split 族では正の Kuznetsov 比較が得られる。** 任意の固定 λ∈C、`1+λ³≠0` と滑らかな純中心三次 G に対し、`Hcorr=g_λ+G+s²Hess(g_λ)/24` は、固定入力Bの MF 移送・相対 window・固定標的への有限降下・coherent 飽和性の下で、元の残余圏と rotation・指定三次周期を保つ同値をある有限拡大上に与える。正規化した Hesse 係数は `ν=[λ+s²(4+λ³)/12]/[1−s²λ²/4]`、tensor の尺度は `s(1−s²λ²/4)` となる。一般混合係数では H♯と W_res の一致は現時点で mod h⁴ であり、全次数の同値を結論していない。

一般の滑らかな三次に対して、`3 ≤ n ≤ 7` では Jacobi スキームが Grassmann 錐に等しい。`n=8`、すなわち `N=n+2=10` では、整数行列の証明書から全次数の差
`J₁₀/I_F ≃ C(−2)^330` を決定した。冪零根基は頂点に支持される長さ330の二乗零イデアルで、頂点の極大イデアルで消え、socle 全体に等しい。Hilbert 級数は Grassmann 環のものに `330t²` を加えたものであり、この平方零拡大は次数付き代数としても頂点の完備局所代数としても分裂しない。この八次元の結果は、既存の一般三次の被約分類に依存しない。

非零分解可能点では Hessian の共通核 `K` により横断切片を記述した。Thom–Sebastiani 直和の Jacobi スキームの retraction を用いると、全ての `n≥11` について、非零 Poisson 点の局所環と射影 Jacobi スキームに、任意の二元の積が零となる330次元の冪零部分空間を持つ滑らかな特殊三次を構成できる。周囲の冪零根基全体が二乗零であるとは主張しない。

全次元の一般三次では、既存の被約分類を用いると、非零部分と射影化は Grassmann のものに一致し、`n≥8` の冪零根基は頂点に支持される有限長加群となる。`n≥11` では次数三にも非零部分があり、最高次数と頂点の極大イデアルによる消滅指数は次元によらず一様に有界ではない。`n=9,10` の全 Hilbert 関数や、一般次元での冪零根基自身の積は引き続き未決定である。

Jacobi 行列の普遍的な階数上界は Gesmundo–Landsberg の Koszul flattening の既知の結果に対応する。`N=9,10` の二次行列の最大階数の達成も Boij（1999, Remark 6）の apolar Betti 計算に対応し、独立した新規成果として数えない。現行稿はこの対応を明示し、計算証明書を再現可能な独立検証として保持する。正確な参照箇所は [参考文献](papers/references.tex) と [研究ノート](notes/research_notes.md) に記す。

通常 Artin 基底上の残余圏の一次切断変形は `n ≠ 4` で幾何的変形として認識できる。四次元の categorical hull は22次元、幾何的変形は20次元。全 intrinsic 成分の一般対象の局所表示、一般混合係数の全次数残余比較、残余同値の全 O-降下、全 Abel 形式近傍の完成は主張していない。新規性の網羅的確認・外部査読は未完了。

## 再生成

必要な環境は LuaLaTeX、latexmk、LuaTeX-ja、AMS、hyperref、enumitem、booktabs、needspace、和文フォント（Noto Serif CJK または Harano Aji）、Python 3・NumPy・SymPy、および C++17 対応コンパイラ（GCC または Clang）。PDFと検証用の中間ファイルは `build/` に生成し、Gitでは追跡しない。

リポジトリのルートで実行する：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/check_sources.py
python3 computations/verify_center_hessian.py
python3 computations/verify_geometric_corrections.py
python3 computations/verify_poisson_correction.py
python3 computations/verify_cubic_covariants.py
python3 computations/verify_jacobi_rank.py --verify computations/jacobi_rank_certificate.json
python3 computations/verify_jacobi_vertex.py --verify computations/jacobi_vertex_certificate.json
latexmk papers/nc-cubic-n-fold.tex
```

中心・Hessian と幾何補正の検算は有理係数の記号恒等式、八次自由代数の trace、Jacobi 商の双対証明書、普遍 cofactor 恒等式と Hesse の j 差を再現する。新しい補正検算では十個の独立係数を持つ三変数三次、任意の対称行列、二パラメータ Hesse 中心の係数変換、混合項の復元行列、九重被覆の分岐、Weyl の整数重複度と四次不変式も確認する。入力論文の混合中心公式の非可換中心性や圏同値そのものは記号計算で再検証しない。組版設定は既存の repo ルート基準のパスを維持し、PDF と SyncTeX を `build/` に揃えている。研究hubの現行テンプレートと設定も参照し、LaTeX Workshop の推奨拡張を指定した。

証明書の再生成も可能である：

```bash
python3 computations/verify_jacobi_rank.py --generate build/jacobi_rank_certificate.json
python3 computations/verify_jacobi_rank.py --verify build/jacobi_rank_certificate.json
```

`--generate` の前に `build/` を作成する。二次行列の生成と保存済み小行列の検証は別のコード経路で行い、法32003で非零の整数行列式を用いる。

八次元の頂点構造の検証は、整数係数の Jacobi 式を法2で計算し、次数三の縮約写像の全射性を保存済み小行列で確認する。標数二の三次多項式を解釈する主張ではなく、整数行列の階数下界を特性零へ移す証明である。検証時には約450 MBの行列を `build/jacobi-vertex/` に再生成し、直接消去のメモリ使用量は約220 MB、所要時間は約1〜2分（環境依存）。大きな行列は追跡対象に含めない。いずれの検証にも浮動小数点による近似判定を用いない。

作業規約は [AGENTS.md](AGENTS.md) を参照。正本はこのリポジトリの main とし、現在のソースと証明に必要な計算資産だけを保存する。
