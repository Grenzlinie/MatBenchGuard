# 完全脆性材料の遅れ破壊に及ぼす初期亀裂の大きさと試験片寸法の影響
野島武敏
京都大学大学院工学研究科航空宇宙工学教室,606-01京都市左京区吉田本町

# Effect of Initial Crack Length and Specimen Size on Delayed Failure Time in Perfectly Brittle Materials
Taketoshi NOJIMA
Department of Aeronautics and Astronautics, Kyoto University, Yoshida Hon-machi, Sakyo-ku, Kyoto-shi 606-01

In order to clarify the effect of the initial crack length $a_{0}$ and specimen size on the time to failure $(T_{f})$ as well as to find the most suitable condition for evaluating the minimum value of the stress intensity factor $K_{0}$ (the threshold, the slow crack growth limit), the characteristics of static fatigue tests of brittle materials were analytically discussed and the analyzed results were verified by the tests on a soda lime glass. Both by analytical and experimental works, it was clarified that the $T_{f}$ for a given value of $K_{II}$ becomes shorter as $a_{0}$ decreases ( $K_{II}$ : the initial stress intensity). This fact indicates that to use the specimens with a smaller crack is very advantageous to characterize $K_{II}-T_{f}$ relations as well as the $K_{0}$ value in a shorter time.

[Received May 6, 1997; Accepted September 19, 1997]

Key-words : Delayed failure, Static fatigue, Initial crack size, Threshold, Stress intensity, Glass

## 1. 緒 言
ガラスやセラミックス等の脆性材料の遅れ破壊 (静疲労) における負荷応力 $\sigma$ と破断時間 $T_{f}$ の関係についての解析はEvans らによって報告されている1)~3). この解析においては,線形破壊力学に基づく $K_{I}=\sigma \sqrt{\pi a} \cdot F(x)$ , 亀裂速度 $\dot{a}$ と $K_{I}$ 間の構成式 $\dot{a} \propto(K_{I})^{n}$ ( $n$ : 定数) を用い, 微小亀裂を想定し, 試験片の形状係数 $F(x)$ を定数と仮定し( $a$ : 亀裂長さ, $x=a / W$ (W: 試験片幅)), 簡便な $\sigma$ と $T_{f}$ の関係式, $(\sigma)^{n} \cdot T_{f}=C$ が得られておりこの $C$ 值は初期亀裂長さ $a_{0}$ の関数である $(C \propto$  $\sigma_{i}^{(n-2)} \propto a_{0}^{(2-n) / 2}, \sigma_{i}:$ 不活性強度 $)^{4), 5)}$ . しかしながら, その後なされた研究報告では, $C$ 值を定数としてデータの解析がなされることが多い6),7). 一方, 亀裂を有する試験片の静疲労試験結果の解析において $\sigma$ にかえて初期応力拡大係数 $K_{II}$ を用いると, 式は $(K_{II})^{n} \cdot T_{f}=C^{\prime}$ のように同様の形になりこの $C^{\prime}$ 值は試験片寸法 $W$ や初期亀裂長さ $a_{0}$ の関係になる8)にもかかわらず, これまでに報告された数多くの静疲労や繰り返し疲労の試験結果の解析では, これらの依存性を十分斟酌して議論されてきたとは言い難い. 本報告は前報8)の議論をもとに, 最初に破壊力学的な見地から興味が大きいと思われる $K_{II}-T_{f}$ や $\sigma-T_{f}$ 関係並びにこれらの相互の関連性について述べ, これらの関係に及ぼす試験片寸法 $W$ や初期亀裂長さ $a_{0}$ の影響を“初期亀裂が微小な場合"と"有限長の大きな亀裂の場合"に分類して明らかにする. また静疲労試験において最も重要であると思われる下限界の $K_{I}$ 值( $K_{0}$ 又は $K_{ISCC}$ : threshold) をできるかぎり短時間で同定するための条件について述べる. 次にこれらの解析結果を検証するために行った, ソーダ石灰ガラスの遅れ破壊についての実験結果とその考察について報告する.

## 2. 初期応力拡大係数 $K_{II}$ あるいは負荷応力 $\sigma$ と破断時間T:の関係
### 2.1 初期応力拡大係数 $K_{II}$ と破壊時間 $T_{f}$ の基本関係式
準静的な力の釣り合いを仮定すると, エネルギー解放率 $G$ は $K_{I}$ を応力拡大係数として
$$G=\frac{K_{\mathrm{I}}^{2}}{E^{\prime}}=\frac{P^{2}}{2 B} \cdot \frac{\mathrm{d} \lambda}{\mathrm{d} a}\qquad(1)$$
で与えられる.ここで, $E^{\prime}=E /(1-v^{2})(E, v:$ 試験片の縦弾性率とポアソン比), $P:$ 負荷荷重, $\lambda(a)$ : 試験片のコンプライアンス, $B$ : 試験片の厚さである. 亀裂速度 $\dot{a}$ と $K_{I}$ 值の構成関係式を $\dot{a}^{*}$ 及び $K_{I}^{*}$ を定数として次式で表す.
$$\frac{\dot{a}}{\dot{a}^{*}}=\left(\frac{K_{\mathrm{I}}}{K^{*}}\right)^{n}\qquad(2)$$
本論文では, $K_{I}-\dot{a}$ 関係における下限界の $K_{I}$ 值( $K_{0}$ と定義)をあたえる最大の亀裂速度を $\dot{a}_{0}$ と定義する.すなわち $K^{*}=$  $K_{0}, \dot{a}^{*}=\dot{a}_{0}$ である (図 $2(C)$ 参照). 試験片の幅 (又は高さ) を $W$ とし, 無次元き裂長さを $x \equiv a / W$ で表し, 試験片のコンプライアンスを無次元コンプライアンス入を用いて $\tilde{\lambda} \equiv \lambda /$  $(2 / E^{\prime} B)$ で表す.この $\tilde{\lambda}$ と(1)式を(2)式に代入すると次式を得る.
$$\frac{\dot{a}}{\dot{a}^{*}}=\left\{\frac{P(t)}{B \sqrt{W K^{*}}}\right\}^{n}-\left\{\frac{\mathrm{d} \tilde{\lambda}}{\mathrm{d} x}\right\}^{n / 2}\qquad(3)$$
無次元荷重 $\tilde{P} \equiv P /(B \sqrt{W K^{*}})$ , 無次元時間 $\tilde{T} \equiv t /(W / \dot{a}^{*})$ を導入し, (3)式を $\dot{a}=W \dot{x}$ として, $t=0$ で $x=x_{0}$ として積分し,“ $x=a / W=1$ で破断する”とすると, 無次元破断時間を $\tilde{T}_{f}$ と置いて
$$\int_{0}^{\tilde{T}_{\mathrm{f}}} \tilde{P}^{n} \mathrm{~d} \tilde{T}=\int_{x_{0}}^{1}\left(\frac{\mathrm{d} \tilde{\lambda}}{\mathrm{d} x}\right)^{-n / 2} \mathrm{~d} x\qquad(4)$$
を得る.ここで $x_{0}$ は無次元初期亀裂長さである. 破壊力学の基本関係式, $K_{I}=\sigma \sqrt{\pi a} \cdot F(x)$ を用い, $P=\alpha \sigma B W$ と表す.ここで $\alpha$ の值は $S$ をスパン長さとすると 3 点曲げ試験片では1.5(S/W),引張型の試験片では1である. これらの関係を(1)式に代入すると
$$\frac{\mathrm{d} \lambda}{\mathrm{d} x}=\frac{2 B W K_{\mathrm{I}}{ }^{2}}{P^{2} E^{\prime}}=\frac{2 \pi}{\alpha^{2} E^{\prime} B} x F^{2}(x)\qquad(5-A)$$
すなわち
$$\frac{\mathrm{d} \tilde{\lambda}}{\mathrm{d} x}=\frac{\pi}{\alpha^{2}} x F^{2}(x)\qquad(5-B)$$
を得る.

定荷重の遅れ破壊試験を考えて負荷荷重 $P$ を定数 $(P_{0})$ とし, (5-B) 式の $d \tilde{\lambda} / d x$ 及び $\tilde{P}_{0}=P_{0} /(B / \sqrt{W} K^{*})$ を用いると(4)式は次式となる.

野島武敏
Journal of the Ceramic Society of Japan 106 [1] 1998

$$\tilde{P}_{0}{ }^{n} \cdot \tilde{T}_{\mathrm{f}}=\int_{x_{0}}^{1}\left\{\frac{\sqrt{\pi}}{\alpha} \sqrt{x} F(x)\right\}^{n} \mathrm{~d} x\qquad(6)$$

一方 $x=x_{0}$ の時の初期応力拡大係数 $K_{Ii}$ は(1)式より
$$K_{\mathrm{Ii}}=\frac{P_{0}}{B \sqrt{W}} \cdot \frac{\sqrt{\pi}}{\alpha} \sqrt{x_{0}} F\left(x_{0}\right)\qquad(7)$$
となる. $\tilde{P}_{0}=P_{0} /(B / \sqrt{W} K^{*})$ と(7)式より $\tilde{P}_{0}=(K_{Ii} / K^{*}) /$  ${\sqrt{(\pi / \alpha^{2})} \sqrt{x_{0}} F(x_{0})}$ を得る. この $\tilde{P}_{0}$ を(6)式に代入すると $K_{Ii^{-}}$  T:関係の一般式, (8)式を得る.
$$\begin{aligned}
& \left(\frac{K_{\mathrm{Ii}}}{K^{*}}\right)^{n} \cdot \tilde{T}_{\mathrm{f}}=\frac{W I}{a^{*}}, \\
& I \equiv \int_{x_{0}}^{1}\left\{\frac{\sqrt{x_{0}} F\left(x_{0}\right)}{\sqrt{x} F(x)}\right\}^{n} \mathrm{~d} x
\end{aligned}\qquad(8)$$
(8)式において $K^{*}, a^{*}$ 及び n を材料定数とすると, 破断時間 $\tilde{T}_{f}$ は試験片寸法 W 及び初期き裂長さによって与えられる I 值に比例することが分かる.n=5~100として3点曲げ試験片(スパン長さS=4W)についてI値を算出した結果を図1に示す. I 值は $x_{0}<0.05 0.06$ の小さな $x_{0}$ の領域においては, 近似的に $x_{0}$ に比例して増大し, その後最大值を示して漸減することが分かる.

Fig. 1. $I-x_{0}$ relations for various values of n.
Evans と同様に, 微小亀裂を考え, $F(x)=F(x_{0})=$ 定数と仮定し,積分の上限を1に代えて不安定に破壊する臨界亀裂長さ $x_{f}$ を用いて (8) 式を積分すると $I \equiv I'$ は $x_{f} \gg x_{0}$ のとき(xt/xo)(2-n)/2=0 となるから
$$\begin{aligned}
I^{\prime} & =\int_{x_{0}}^{x_{\mathrm{f}}}\left\{\sqrt{\frac{x_{0}}{x}}\right\}^{n} \mathrm{~d} x=\frac{2}{n-2} x_{0}\left\{1-\left(\frac{x_{\mathrm{f}}}{x_{0}}\right)^{(2-n) / 2}\right\} \\
& \simeq \frac{2}{n-2} x_{0}
\end{aligned}\qquad(9)$$
となる. この取り扱いは積分の上限を1としても結果は同様であるから, 微小な亀裂についてはIの近似値として(9)式が成り立つ. (9)式のI'を(8)式のIに代えて用い, a=Wxを用いて有次元の形で表示すると, 微小な亀裂に対して
$$\left(\frac{K_{\mathrm{Ii}}}{K^{*}}\right)^{n} \cdot T_{\mathrm{f}}=\frac{2}{n-2} \frac{a_{0}}{a^{*}}\qquad(10)$$
を得る. 先と同様に $K^{*}, a^{*}$ 及び n を定数と考えると, 破断時間 $T_{f}$ は同一の $K_{Ii}$ 值について, 初期亀裂長さ $a_{0}$ にのみ比例しWに依存することはない. (9)式から, 微小亀裂については $I'-x_{0}$ 関係の傾きは 2 /(n-2) であることが分かる.この值を傾きと取って, n=5,10,20について図1に原点を通る3本の破線で示す. $x_{0}$ が小さな領域では(9)式の I' 值は I 值より少し小さいがほぼI値の近似値になっていることが分かる(この相違は F(x)= const. の仮定による). Evans は $K_{Ii}=\sigma \cdot \sqrt{\pi a_{0}} \cdot F$ を用い $T_{f}={2 /(n-2)} \cdot(K_{Ii})^{(2-n)}{(K^{*})^{n} / a^{*}} /(\pi \sigma \cdot F)^{2}$ を得た (F: 定数). この式に $\sigma \cdot F=K_{Ii} / \sqrt{\pi a_{0}}$ を代入すると $(K_{Ii} /$ K*)"·T;={2/(n-2)}ao/a*となり(10)式と一致する. すなわち(10)式は Evans が得た $\sigma-T_{f}$ 関係を $K_{Ii}-T_{f}$ 関係に書き替えたものに対応し, この式は微小な亀裂を有する脆性材料についての破断時間 $T_{f}$ , 初期応力拡大係数 $K_{Ii}$ , 初期亀裂長さ $a_{0}$ 間の関係を与える.
破断時間 $T_{f}$ と初期応力拡大係数 $K_{Ii}$ の関係を示す一般式,(8)式, 微小亀裂についての簡便関係式, (10)式, 及び図1に示された結果は以下のようにまとめられる(図2).図1でI值が $x_{0}$ にほぼ比例する領域の小さな $x_{0}$ 值 $(x_{0}<0.05 0.06)$ を微小亀裂とし: $x_{0}$ が大略 0.1 より大きい亀裂と区別する. $x_{0}$  $=a_{0} / W$ が大きな試験片では: (1) $x_{0}=$ 一定にして静疲労試験を行うと(図2(A)),試験片寸法Wが大きな試験片ほど,"同一の $K_{Ii}$ 值については", 破断時間が大きくなる. 試験片寸法を一定にすると(図 2(B)): $x_{0}$ が大きくなるほど: I 值に比例して $T_{f}$ が大きくなるが: $x_{0}$ のある值( n 值に依存する,でピークを示し: $x_{0}$ の増大によってその後徐々に小さくなる.一方: (2) 無次元初期亀裂長さ $x_{0}$ が微小な試験片では: $T_{f}$ 值は $a_{0}$ のみによって決まり, 試験片寸法 W に依存しない(図2 (C)). しかしながら W が一定のときには $a_{0}$ が大きくなるほど,破断時間はその寸法に比例して長くなる(図2(D)).いずれの亀裂長さの場合においても: $K_{Ii}-T_{f}$ 関係は $a_{0}$ に依存し:同じ $K_{Ii}$ を与えると, 初期亀裂長さ $a_{0}$ が大きくなるほど破断時間は長くなる.
2.2 微小亀裂を有する材料の $\sigma-T_{f}$ 関係
上述の破壊力学的取り扱いが微小な表面亀裂を有する試験片にも適用し得ると考えて $\sigma-T_{f}$ 関係を導く.これは微小な先在表面亀裂を有する平滑材などの遅れ破壊などの試験結果の解析にも適用し得ると考えられる. ここでは, 特にこれまで議論されてこなかった下限界の $K_{I}$ を与える $\sigma^{*}$ , 及びこの $\sigma^{*}$ を与える最短の破断時間 $(T_{f})_{0}$ (図 2 (C) 参照) について考える.(10)式に $K_{Ii}=\sigma \cdot \sqrt{\pi a_{0}} \cdot F(x_{0})$ を代入すると次式を得る.
$$\sigma^{n} \cdot T_{\mathrm{f}}=\frac{2}{n-2} \cdot \frac{1}{a^{*}}\left\{\frac{K^{*}}{\sqrt{\pi} F}\right\}^{n}\left(a_{0}\right)^{(2-n) / 2}\qquad(11)$$

![](./images/811647860176060417_1.jpg)
Fig. 2. Schematic of $log (K_{Ii})-log (T_{f})$ relations for large and small cracks in static fatigue tests.

72
完全脆性材料の遅れ破壊に及ぼす初期亀裂の大きさと試験片寸法の影響

![](./images/811647860176060417_2.jpg)

Fig. 3. Shift of $(T_{f})_{0}$ with the decrease of crack size (for small cracks).

すなわち: $\sigma-T_{f}$ 関係は $K^{*}$ を一定とすると $(\sigma)^{n} \cdot T_{f} \propto$  $(a_{0})^{(2-n) / 2}$ となる. 一方下限界の $\sigma^{*}$ は $K_{Ii}=K_{0}=\sigma^{*} \sqrt{\pi a_{0}} \cdot F(x_{0})$ より得られ: そのときの破断時間 $(T_{f})_{0}$ はこの関係式と(11)式より(あるいは(10)式で $K_{Ii}=K^{*}=K_{0}$ とおいて,得られ:次式で与えられる.
$$\left(T_{\mathrm{f}}\right)_{0}=\frac{2}{n-2} \cdot \frac{a_{0}}{\dot{a}_{0}{ }^{*}}\qquad(12)$$
上述のことを模式的に図3に示す. 図は3種の初期き裂長さ $a_{0}=a_{01}, a_{02}$ 及び $a_{03}(a_{01}<a_{02}<a_{03})$ について, $(\sigma)^{n} \cdot T_{f} \propto$  $(a_{0})^{(2-n) / 2}$ 関係を 3 本の斜線 (1), (2), (3) で, 下限界の $K_{I}$ についての関係, $K_{Ii}=K_{0}=\sigma^{*} \sqrt{\pi a_{0}} \cdot F(x_{0})$ , を 3 本の水平線(I, II, III ; $\sigma^{*}=\sigma_{1}, \sigma_{2}, \sigma_{3})$ で示したものである.これらの交点の時間は $(T_{f})_{0}$ を与え, これらの $(T_{f})_{0}$ はおのおの $a_{0}=a_{01}$ , $a_{02}, a_{03}$ として(12)式により算出される(図中 A, B, 及び C点).この図は $a_{0}$ が小さくなるほど $\sigma^{*}$ は大きくなるが: 逆に $(T_{f})_{0}$ は $a_{0}$ に比例して小さくなることを示す. (12)式あるいは図3に示された関係は, 初期亀裂長さの計測やその評価が困難な,先在微小表面亀裂を有する平滑材や微小なビッカース圧痕等を有する試験片の遅れ破壊試験において, 下限界の $K_{I}$ を与える臨界破断時間 $(T_{f})_{0}$ は破壊を支配する亀裂の大きさに依存することを示す.また(12)式は $K_{Ii}=K^{*}=K_{0}$ とおいて得られたものであるから構成式(2)式中の $\dot{a}^{*}$ は下限界の $K_{0}$ を与える最大のき裂速度 $(\dot{a}_{0})$ である. それゆえ(12)式を用いると, 下限界の $K_{0}$ を与える最小の破断時間 $(T_{f})_{0}$ などを, 別の実験から得られる $\dot{a}-K_{I}$ 関係より推定することもできる.なお図 3 の $\sigma-T_{f}$ 関係は初期亀裂長さ $a_{0}$ を与えれば $K_{Ii}-T_{f}$ 関係で表示でき,図2(D)のような関係となる.

## 3. 実験方法と実験結果
### 3.1 試験材料と試験法
試験には完全脆性体と考えられる市販のソーダ石灰ガラスの予亀裂を有する3点曲げ試験片(スパン長S=4W)を用いた.1 mm 以上の長いき裂の導入は熱応力亀裂導入法によった $^{9)}$ .微小な亀裂はビッカース圧痕(荷重 $P_{V}=4.9$ 及び 9.8 N ,で代用した. 板厚Bはおよそ1.8及び2.7 mm,またW=3~40mmである. なお試験は大気中 (相対湿度40~60%) で行った. 荷重はいわゆる第1領域で破壊が進展するよう選択した.遅れ破壊試験の方法は前報によった $^{9)}$ .
### 3.2 実験結果
 $x_{0}=0.5$ の大きな亀裂を有する試験片の遅れ破壊試験 (W=5,10,20 及び 40 mm) に打ける $K_{Ii}$ と $T_{f}$ の関係を図 4 に示す.図より同一の $K_{Ii}$ については寸法 W が大きくなる程, 破断時間 $T_{f}$ が長くなることが分かる.これは図 2 (A)に示された解析的予測と合致し: このような大きな亀裂の $T_{f}$ の寸法依存性は微小亀裂を仮定したEvansの式では予測し得ない結果である. 図 5 に図 4 から求めた $\ln (K_{Ii})=-0.5$ 及び $-0.3(K_{Ii}$ : $MPa \sqrt{m}$ ) のときの $T_{f}$ と寸法 W の関係を示す. 結果は理論的予測 ((8)式) から得られる $T_{f} \propto W$ がほぼ成立しているこ

![](./images/811647860176060417_3.jpg)

Fig. 4. Specimen size (W) effect on $K_{Ii}-T_{f}$ relation for large cracks.

![](./images/811647860176060417_4.jpg)

Fig. 5. $log (T_{f})-log (W)$ relations showing $T_{f} \propto W$ (from Fig. 4).

とを示す. 図 6 は既報の W= 一定の場合の $x_{0}$ の相違による $K_{Ii}$ と $T_{f}$ の関係を示す.この図は図 2 (B)に対応している. 前報の研究によって下限界の $K_{0}$ 值の存在が確認され: $K_{0}$ 值としておよそ0.27 0.3 MPa $\sqrt{m}$ が得られており $^{9)}$ , 以下の議論においては0.28 MPa $\sqrt{m}$ を用いる.
図7はW=8,5及び3mmの"異なる寸法の試験片"に荷重 $P_{V}=9.8 N$ でビッカース圧痕を導入した試験片の負荷応力 $\sigma(=1.5 PS / B W^{2})$ と $T_{f}$ の関係を示す.この図は小さな亀裂については, 初期亀裂の大きさが同一であれば破断時間が寸法Wに依存しないことを示す. この関係は図2(C)の微小亀裂に関する $K_{Ii}-T_{f}$ 関係に対応する. ビッカース荷重 $P_{V}=4.9$ 及び9.8 N として得た $\sigma-T_{f}$ 関係 $(W \fallingdotseq 5 mm)$ を図 8 に示す. あまり明瞭ではないが: 亀裂が小さくなる程 $(T_{f})_{0}$ が小さくなる傾向を示す $\sigma-T_{f}$ 関係 (図 3 参照) が見られる. 図 7 と図 8 で得られた試験での下限界の応力 $\sigma^{*}$ は $P_{V}=4.9$ 及び 9.8 N について, おのおのおおよそ34と25Nである.

![](./images/811647860176060417_5.jpg)

Fig. 6. Experimental $log (K_{Ii})-log (T_{f})$ relations ( W= constant, data from Ref.(9)).

![](./images/811647860176060417_6.jpg)

Fig. 7. Experimental $log (\sigma)-log (T_{f})$ relations for small cracks showing Windependency.

![](./images/811647860176060417_7.jpg)

Fig. 8. Experimental $log (\sigma)-log (T_{f})$ relations for small cracks(initial cack size effect).

![](./images/811647860176060417_8.jpg)

Fig. 9. Experimental $log (K_{Ii})-log (T_{f})$ relations for small crack $(x_{0}<0.06)$ showing initial crack length effect on $T_{f}$ .

図 9 に W=40 mm の試験片に $a_{0}=1.6 1.9 mm$ の予亀裂を導入した試験片の $K_{Ii}-T_{f}$ 関係を黒丸点で示す. 図 5 の $x_{0}$  $\fallingdotseq 0.054(a_{0} \fallingdotseq 1 mm)$ の小さな亀裂についての $K_{Ii}-T_{f}$ 関係の結果を破線で示す. またビッカース圧痕を導入した試験片(図8)の $K_{Ii}-T_{f}$ 関係を白丸と黒三角印で示す.ここでこれらの試験片についての $K_{Ii}$ 值は, 上述の $\sigma^{*}(P_{V}=4.9$ 及び 9.8 N について $\sigma^{*}=34$ 及び 25 N) 及び $K_{0}=0.28 MPa \sqrt{m}$ を $K_{0}=\sigma^{*} \pi(a_{e})$ . $F(a_{e} / W)$ に代入して得られた亀裂長さ $a_{e}$ (これを等価初期亀裂長さと仮定する,を用いて算出されている.この $K_{Ii}$ の算出に用いられた $a_{e}$ 值はおのおの35及び19 $\mu m$ である. 図 9 は図2 (D)で解析的に示された “同一の $K_{Ii}$ 值については初期亀裂長さが小さくなる (すなわち初期強度が大きくなる) 程, 短時間で破断する"一見奇妙に思える関係が微小亀裂についても成立つことを示している. 図10に図 9 に打ける $K_{Ii}-T_{f}$ 関係と $K_{0}$  $=0.28 MPa \sqrt{m}$ との交点から得られる $(T_{f})_{0}$ と初期亀裂長さ

74
完全脆性材料の遅れ破壊に及ぼす初期亀裂の大きさと試験片寸法の影響

![](./images/811647860176060417_9.jpg)

Fig. 10. $(T_{f})_{0}$-initial crack length relation (from Fig. 9, $\dot{a}_{0}$-valueafter Wiederhorn). $^{10)}$

 $a_{0}$ (あるいは $a_{e}$ ) の関係を示す. 図中の破線は Wiederhorn によって報告されたガラスの $\dot{a}-K_{I}$ 関係より求めた下限界の $K_{I}$ 值を与える最大の亀裂速度 $(\dot{a}_{0}=3 ×10^{-11} m / s)^{10)}$ , 及び図 4と図 8 から得られる n 值 $(\fallingdotseq 16)$ を(10)式に代入して算出した $(T_{f})_{0}$ と $a_{0}$ の関係を示したものである. 実験点を結んだ傾き(実線)は破線で示される理論的予測より少し小さめであるが $(T_{f})_{0}$ 值としてはほぼ一致していると思われる. 上述の結果は通常の遅れ破壊試験, あるいはこのような下限界の $K_{I}$ 值を求める遅れ破壊試験においては試験片寸法Wにかかわりなく,できるかぎり小さな亀裂を有する試験片を用いることが有利であることを示す(ただし: $x_{0}=a_{0} / W<0.05$ ).すなわち良好に導入された50〜100 $\mu m$ 程度の微小亀裂を用いた試験は,破断時間の極めて短い試験を可能にし, 面倒な静疲労試験の遂行を飛躍的に簡素化するとともに, 下限界の $K_{I}$ 值の決定を容易にするものと考えられる. 上述の結果はまた,破断時間が亀裂の大きさに依存することを示すことから, このような試験の遂行とその結果のデータ整理の際には, 亀裂の大きさを考慮に入れた考察が必要不可欠であることを示し, このような観点に立ってなされた報告の蓄積は, セラミックス材の遅れ破壊挙動, 特に下限界の $K_{I}$ 值を明確にし得るものと考えられる.
4.'結 論
完全脆性体の遅れ破壊 (静疲労)試験における負荷応力-破断時間の関係を, 微小亀裂から有限の大きな亀裂を含めて検討し,解析結果の妥当性をガラスの3点曲げ試験片を用いて得た実験結果と併せて議論した. 得られた結果は以下のようにまとめられる.
(1,無次元初期亀裂長さ $x_{0}$ で0.05〜0.06より大きな亀裂においては $x_{0}=$ 一定にして静疲労試験を行うと, 試験片寸法 Wが大きな試験片ほど, 同一の $K_{II}$ 值については, 破断時間が長くなる. また試験片寸法を一定にすると: $x_{0}$ が大きくなるほど: 一般に $T_{f}$ が大きくなる(I值(図 1,に比例する).
(2,初期亀裂長さの小さな試験片 $(x_{0}<0.05)$ では, 破断時間 $T_{f}$ は初期亀裂長さ $a_{0}$ のみによって決まり, 試験片寸法W に依存しない. また W が一定の場合には $a_{0}$ が大きくなるほど, 破断時間はその大きさに比例して長くなる.
(3,下限界の $K_{I}$ 值を効率よく決定するためには破断時間を短縮することが不可欠であり, これを達成するためには小さな亀裂を有する試験片を用いて一連の実験を行うことが有利である.
文献
1) A. G. Evans and S. M. Wiederhorn, Int. J. Fracture, 10, 379-92(1974).
2) A. G. Evans and E. R. Fuller, Met. Trans., 5, 27-33 (1974).
3) A. G. Evans. Int. J. Fracture, 16, 485-98 (1972).
4) R. W. Davidge, "Mechanical Behavior Ceramics," Cam- bridge Univ. Press (1979) p.144.
5) 西田俊彦, 安田榮一,"セラミックスの力学的特性評価",日刊工業新聞社(1986)p.85.
6) C. J. Lim and D. F. Socie, J. Am. Ceram. Soc., 74, 1511-18(1991).
7)町田隆志,太田裕之,中門公明,富田 寬,日本機械学会論文集A,57,1021-26(1991).
8)野島武敏,加藤秀輝,材料,42,1331-37(1993).
9)野島武敏,杉山文子,阪口健一,材料,43,1457-62(1993).
10) S. M. Wiederhorn, J. Am. Ceram. Soc., 50, 407-14 (1967).