日本機械学会論文集(B編)
56卷531号(1990-11)
論文 No.90-0050 B

# 電子ビームによる物質表面加熱の数値解析*

塩田和則*1, 橋立良夫*1, 熊谷幹夫*1

## Numerical Simulation of Electron Behavior and Beam Heating on the Material Surface

Kazunori SHIODA, Yoshio HASHIDATE and Mikio KUMAGAI

The method of numerical analysis is investigated for the maunfacturing processes by means of electron beam heating such as hardening, cutting and welding. The high-energy electrons (10～50keV) impinge upon the surface of the material and diffuse through multiple elastic/nonelastic scattering with atoms. Although the electron collisions with atomic nuclei acn approximately be treated as elastic ones, the collision with the orbital electrons of atoms is a nonelastic one. The fast electrons are decelerated in the course of the atomic excitation or X-ray radiation, transferring their kinetic energy into the lattice system as heat energy. Here, the difference between the heat generating density and the electron density is clarified numerically, as are the penetration depth and reflection ratio of the electron beam, which give good agreement with the referenced data. Furthermore, the difference between the penetration depth of the electrons and that of the heat, which has never before been discussed in detail, is clarified.

**Key Words:** Computational Mechanics, High-Energy-Rate Beam Machining, Surface Treatment, Heat Treatment

---

### 1. 緒 言
レーザビームや荷電粒子ビームによる材料処理は,表面処理, 切断, 溶接などさまざまな製造技術分野で活用され, 特に電子ビーム処理はエネルギー変換効率の高さ, 工学的容易性の観点から広く応用されている. 電子ビーム処理は, ビームエネルギーやビーム電流の大小により工業的利用範囲は多岐にわたっており, 物質中の電子浸透深さが数 $\mu \mathrm{m}$ から数十 $\mu \mathrm{m}$ 程度と小さく, 物質表面を局部的に加熱することが可能である. さらに, ビームエネルギー(ビーム加速電圧)を調整することにより材料の表面処理深さを所要値に選択することが容易である(1).

本報では, 高エネルギー電子と材料物質原子との相互作用をモデル化して, 物質中の高エネルギー電子挙動の数値シミュレーションを実施した. 物質中の高エネルギー電子は, エネルギー, 物質密度, 電子阻止能に応じた飛程を有するが, その飛程内で原子との相互作用によって運動エネルギーを失って遂には熱電子になる.10~50 keV程度のエネルギー領域の電子と物質原子との相互作用としては, (1)原子核による散乱(主に弾性散乱), (2)軌道電子による散乱(原子励起を伴う非弾性散乱), (3)X線ふく射による制動損失,などが考えられるが, 本報では物質中の高エネルギー電子の挙動を相対論理的電磁気学の立場からモデル化した.

物質表面でのビーム反射率や物質中の電子浸透深さは表面処理工程では重要な量となるが, これらのパラメータ依存性を評価する.

### 記号の説明
c:真空中の光速
E:電子エネルギー
e:電荷素量
h:浸透深さ
I:電流
J:励起ポテンシャル
L:電子ビーム長さ
l:電子移動距離
M:電子角運動量
m:電子質量
$m_0$:電子静止質量
n:粒子数密度

---

*原稿受付 平成2年1月24日.
*1正員, 東芝(〒230横浜市鶴見区末広2-4).
—221—
NII-Electronic Library Service

P:エネルギースペクトル関数
Q:電子ビームパワー
q:発熱密度
$R_t:$ 一様乱数 $(=[0,1])$
r:散乱動径座標
t:時間
V:要素体積
v:電子速度
w:電子ビーム幅
x:座標
y:座標
Z:原子番号
z:座標
$\alpha:$ ビーム入射角
$\beta:$ 無次元化電子速度
$\delta:$ デルタ関数
$\Delta E:$電子エネルギー差分
$\Delta t:$時間差分
$\Delta l:$移動差分
$\Delta x:$セル要素寸法(x方向)
$\Delta y:$セル要素寸法(y方向)
$\Delta z:$セル要素寸法(z方向)
$\varepsilon:$解析精度
$\varepsilon_0:$真空中の誘電率
$\eta:$反射率
$\lambda:$平均自由行程
$\rho:$衝突径数
$\rho_m:$物質密度
$\sigma:$散乱断面積
$\tau:$衝突周期
$\Phi:$散乱ポテンシャル
$\chi:$散乱角
添 字
下付き0:初期値
e:電子
i:衝突を示す指標
j:移動距離差分を示す指標
k:電子個々を示す指標
m:カットオフ値

## 2. 数値解析
### 2·1 解析モデルと基礎方程式
#### 2·1·1 解析モデル
電子ビームによる物質の表面処理プロセスの数値解析モデルを図1に示す. 電子ビームは三次元の被加熱ブロックの上側表面に照射され, この上側表面近傍を熱処理する. 電子ビームの断面形状, 入射角,エネルギースペクトルなどは任意であるが, 通常はく形線状の電子ビームを用いる. 被加熱ブロックは均一の物質から成り, その厚さは電子ビームが貫通しない程度の寸法を有している.

物質中での高エネルギー電子の散乱,緩和の諸過程は主に次のとおりに分類される.
(1) 原子核による弾性散乱(衝突拡散)
(2) 軌道電子による非弾性散乱(エネルギー緩和)
(3) 電磁ふく射損失(X線損失)
以下に各項目の扱い方,基礎方程式について述べる.

#### 2·1·2 原子核による電子散乱
高エネルギー電子の散乱媒体である物質原子は,固体中では一定の密度で均一に配置されており, ここでは高エネルギー電子の挙動についての基礎方程式について述べる. まず,電子が原子により角度散乱を受ける場合は, 原子質量の圧倒的多数を占める原子核によるのがもっぱらであり, 原子核自身が散乱中心となる(図2参照). 原子核による電子散乱角は式(1)に示すとおり積分され, 式(2), (3)に示すとおりラザフォードの散乱特性により高速電子の散乱過程が記述される.

$$
\chi=\pi-2 \int_{r_{m}}^{\infty} \frac{M / r^{2} d r}{\sqrt{2 m\{E-\Phi(r)\}-(M / r)^{2}}} \cdots \cdots(1)
$$

$$
\frac{d \sigma}{d x}=2 \pi \rho\left|\frac{d \rho}{d x}\right|=\pi\left(\frac{z \cdot e^{2}}{8 \pi \varepsilon_{0} E}\right)^{2} \frac{\cos (\chi / 2)}{\sin ^{3}(\chi / 2)} \cdots(2)
$$

$$
\sigma=\int_{\chi_{m}}^{\pi} \frac{d \sigma}{d x} d x=\pi\left(\frac{z \cdot e^{2}}{8 \pi \varepsilon_{0} E}\right)^{2}\left\{\frac{1}{\sin ^{2}(\chi / 2)}-1\right\}(3)
$$

ここで
$$
E=m c^{2}-m_{0} c^{2}=m_{0} c^{2}\left(\frac{1}{\sqrt{1-\beta^{2}}}-1\right) \cdots \cdots(4)
$$

$$
M=\sqrt{2 m E} \cdot \rho \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(5)
$$

![](./images/811625289116286978_1.jpg)

図1 解析モデル

![](./images/811625289116286978_2.jpg)

図2 原子核による電子散乱

$$
\Phi(r)=\frac{z \cdot e^{2}}{4 \pi \varepsilon_{0} r} \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(6)
$$

$$
\beta=v / c \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(7)
$$

式(2)は高エネルギー電子散乱の微分断面積であり散乱角 $\varkappa$ の確率関数である. また式(3)はこれを積分して得られる全断面積であり, 高エネルギー電子にとっての散乱媒体としての等価的大きさである. ただし,式 (3)の被積分関数である微分断面積は $\varkappa=0$ において特異点を有する.そのためカットオフ角 $\varkappa_{m}$ を設け,それ以下の微少角散乱を無視することにより式(3)の積分を収束させている.ここでは $\varkappa_{m}=5 \sim 10^{\circ}$ とした.

2·1·3 電子阻止能 原子核による高速電子散乱は弾性散乱のため電子エネルギー緩和はほとんどない. ただし, 原子核とはいえ高エネルギー電子の衝突による反跳がわずかでもあるので, 散乱回数が大きくなると電子のエネルギー緩和も生じてくる.

これに対して質量が同じ電子同士の散乱過程は散乱角度は小さい反面, 励起や制動ふく射によるエネルギー損失がむしろ大きい. 原子の軌道電子による非弾性散乱特性としてBetheは相対論的なエネルギー減損特性として式(8)を導出した $^{(2)}$ . 式(8)は高エネルギ一電子の移動距離当たりのエネルギー減損率を示すもので, 角度散乱は考慮していない.ただし, 高エネルギーが低エネルギー電子や熱電子になり, 電子エネルギーが原子の励起ポテンシャルに近づくと式(8)の連続特性近似は許容されず, 量子力学的不連続モデルが必要となる.

$$
\frac{d E}{d l}=\frac{2 n \cdot e^{4} Z}{m_{0} c^{2} \beta^{2}}\left\{\log _{e} \frac{m_{0} c^{2} \beta^{2} E}{2 J^{2}\left(1-\beta^{2}\right)}+f\right\} \cdots \cdots \cdots(8)
$$

$$
\begin{aligned}
f= & -\log _{e} 2\left(2 \sqrt{1-\beta^{2}}-1+\beta^{2}\right)+1-\beta^{2} \\
& +\frac{1}{8}\left(1-\sqrt{1-\beta^{2}}\right)^{2} \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots(9)
\end{aligned}
$$

2·2 境界条件 電子ビームは電子銃から発射,加速されるために, そのエネルギースペクトルはほとんど加速電圧 $E_{0}$ にそろっていると考えられる.よってエネルギー分布関数 P(E)は次のとおりである. すなわちすべての電子は初期エネルギー $E_{0}$ をもって材料表面上に到達するものとする.

$$
P(E)=\delta\left(E-E_{0}\right) \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(10)
$$

またビームの広がり分布は, く形線状ビームとして図1に示すビーム長さL, ビーム幅wの斜線範囲内の入射点の座標は統計的に一様乱数 $R_{i}=[0,1]$ により以下のように算出する.

$$
x_{i}=\frac{w}{2}\left(1-2 R_{i}\right) \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(11)
$$

$$
y_{i}=\frac{L}{2}\left(1-2 R_{i}\right) \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(12)
$$

$$
z_{i}=0 \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(13)
$$

本解析ではビーム入射角を $\alpha$ とした場合, 電子個々はすべて同じ角度 $\alpha$ で材料表面に入射するものとする.

$$
v_{x}=0 \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(14)
$$

$$
v_{y}=-v_{0} \sin \alpha \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(15)
$$

$$
v_{z}=v_{0} \cos \alpha \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(16)
$$

$$
v_{0}=c\left\{1-\left(\frac{m_{0} c^{2}}{m_{0} c^{2}+E_{0}}\right)^{2}\right\}^{1 / 2} \cdots \cdots \cdots \cdots \cdots \cdots(17)
$$

2·3 解法
2·3·1 電子の衝突拡散 電子散乱媒体である原子核の密度n, 電子エネルギーEとすると,電子の平均自由行程 $\lambda$ , および衝突周期 $\tau$ は次のとおりである.

$$
\begin{array}{r}
\lambda_{e}=\frac{1}{n \cdot \sigma}=\frac{1}{n \cdot \pi}\left(\frac{z \cdot e^{2}}{8 \pi \varepsilon_{0} E}\right)^{-2}\left\{\frac{1}{\sin ^{2}\left(\varkappa_{m} / 2\right)}-1\right\}^{-1} \\
\cdots \cdots \cdots \cdots(18)
\end{array}
$$

$$
\tau_{e}=\frac{\lambda_{e}}{v_{e}}=\frac{\lambda_{e}}{c}\left\{1-\left(\frac{m_{0} c^{2}}{m_{0} c^{2}+E}\right)^{2}\right\}^{-1 / 2} \quad \cdots \cdots \cdots(19)
$$

電子個々の自由行程 l の確率関数 P(l)および逆関数法による自由行程 lの確率的算出式を式(20), (21)に示す. さらに散乱時の散乱角 $\varkappa$ は, 式(2)で与えられる微分断面積に対して棄却法により算出される.

$$
P(l)=\lambda_{e}^{-1} \cdot \exp \left(-\frac{l}{\lambda_{e}}\right) \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(20)
$$

$$
l_{i}=-\lambda_{e} \log _{e} R_{i} \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(21)
$$

2·3·2 エネルギー緩和 次に電子のエネルギー緩和の数値シミュレーションにおいては, 時間差分 $\Delta t$ ごとの電子阻止能 $(d E / d l)_{i j}$ を積分することによって電子エネルギーを求めることができる(図4参照).

$$
E_{i j}=E_{0}-\int \frac{d E}{d l} d l=E_{0}-\sum_{i} \sum_{j}\left(\frac{d E}{d l}\right)_{i j} \cdot \Delta l_{i j}(22)
$$

$$
l_{i}=\sum_{j} \Delta l_{i j} \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(23)
$$

2·3·3 解析の終了判定 図1に示した三次元の被加熱ブロックを解析領域として, これに基づく解析上の電子を次の4ケースに分類する.

(1) 解析領域中の運動電子
(2) 解析領域中の停止電子
(3) 解析領域を貫通した運動電子
(4) 表面で反射された運動電子
(5) (4)の電子のうち表面に再突入した運動電子

![](./images/811625289116286978_3.jpg)

図3 ビーム入射角

3428
電子ビームによる物質表面加熱の数値解析

これらの電子のフロー図を示すと図5のようになる. 電子の運動状態と停止状態の判定においては, カットオフエネルギー $E_{m}$ を設けて, 電子エネルギー Eとの大小関係により $E>E_{m}$ なら運動状態, $E<E_{m}$ なら停止状態とみなす. これは便宜的な処置であるが,エネルギードライバとしての高エネルギー電子の挙動を解析する立場からは, (i)初期エネルギーの大半を失った低エネルギー電子や熱電子を解析対象から外す, (ii)エネルギーの低い電子の挙動は基本的に量子論的モデルにより記述される, という二つの理由に基づくものである. 例えばカットオフエネルギー $E_{m}$ は通常, 初期エネルギー $E_{0}$ の $2 \%$ 程度で十分である.Emをこれ以下に設定すると解析時間を著しく増加させることになる.

解析過程ですべての解析電子のうち(2)~(4)の電子総数が増加し, (1)の電子数は漸減する. 解析終了の判定は $\varepsilon$ を微少値として, (1)の電子数 $n_{e 1}$ が次の条件を満足したかにより判定する.
$$\frac{n_{e 1}}{\sum_{j} n_{e j}}<\varepsilon \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(24)$$

2·3·4 発熱密度 物質原子との非弾性衝突により失われる電子エネルギーは, 物質の格子系へと伝達されて遂には熱エネルギーとなる. わずかに光エネルギー, 電磁エネルギー(X線)に変換されるが, 電子エネルギーE=10~50 keVの領域では熱エネルギーに比べれば十分小さく無視できる. よって本解析ではX線損失は無視することになる.

物質中に発生する発熱密度gは, あるセル要素内の通過電子群のエネルギー損失を積分して得られる.kはセル要素内を通過する電子に対する添字である.
$$\begin{aligned}
q & =\lim _{V \to 0} \frac{1}{V} \frac{\partial}{\partial t} \iiint n_{e} \Delta E d x d y d z \\
& =\frac{1}{V \Delta t} \sum_{i} \sum_{j} \sum_{k}\left(\frac{d E}{d l}\right)_{i j} \Delta l_{i j} \quad \cdots \cdots \cdots \cdots \cdots(25)
\end{aligned}$$

$$\Delta E=\int \frac{d E}{d l} d l=\sum_{i j} \sum\left(\frac{d E}{d l}\right)_{i j} \Delta l_{i j} \quad \cdots \cdots \cdots \cdots(26)$$

$$V=\Delta x \Delta y \Delta z \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(27)$$

![](./images/811625289116286978_4.jpg)

図4 エネルギー緩和のシミュレーション

![](./images/811625289116286978_5.jpg)

図5 電子フロー図

3.解析結果

3·1 電子ビームの表面反射率と物質浸透深さ
表1は被加熱体としての銀の表面に垂直に電子ビームを照射したときの解析条件を示すものであり, そのときの電子ビームの表面反射率および物質浸透深さを表2, 3に示す.

図6は材料断面内の高エネルギー電子密度および発熱密度の分布を示し, 材料深さ方向(z方向)を拡大して図示している. 図7は図6の解析結果をグラフ化したものである. なお, 表3に示す物質浸透深さは図7に基づき電子密度が最高値の1/eに減衰する深さとして定義した.

図7において破線は電子密度分布を与える近似式式(28)を示し, 式(29)は電子浸透深さ $h_{e}$ を与えるものである(3).
$$n_{e} \propto 1-\frac{9}{4}\left(\frac{z}{h_{e}}-\frac{1}{3}\right)^{2} \cdots \cdots \cdots \cdots \cdots \cdots \cdots(28)$$

$$h_{e}(m)=2.1 × 10^{-11} \frac{E_{0}^{2}[\mathrm{eV}]}{\rho_{m}\left[\mathrm{~kg} / \mathrm{m}^{3}\right]} \cdots \cdots \cdots \cdots(29)$$

3·2 電子エネルギー依存性 図8は被加熱物質がタングステンのとき初期エネルギー $E_{0}$ をパラメー

表1 解析条件
<table><tbody><tr><td>Beam current</td><td>I</td><td>2.0 A</td></tr><tr><td>Beam energy</td><td>E0</td><td>30 keV</td></tr><tr><td>Beam length</td><td>L</td><td>50 mm</td></tr><tr><td>Beam width</td><td>w</td><td>6 mm</td></tr><tr><td>Incident angle</td><td>α</td><td>0°</td></tr><tr><td>Excited potential of substantial atom</td><td>J</td><td>422 eV (Silver)</td></tr><tr><td rowspan="3">Dimensions of substance</td><td>x</td><td>100 mm</td></tr><tr><td>y</td><td>10 mm</td></tr><tr><td>z</td><td>5 μm</td></tr><tr><td>Cut-off energy</td><td>Em</td><td>0.3 keV</td></tr><tr><td>Cut-off angle</td><td>χm</td><td>5°</td></tr></tbody></table>

-224-
NII-Electronic Library Service

タとしたときの電子および発熱密度分布を示すもので, 図9および図10は反射率, 浸透深さを示す. 図10中の破線は電子浸透深さ $h_{e}$ を与える近似式式(29),および最大電子密度の深さ $h_{e m}=h_{e} / 3$ を示すものである.

表2反射率

<table>
  <tr>
    <td>Input power</td>
    <td>$Q_{0}$</td>
    <td>6 0 . 0 k W</td>
  </tr>
  <tr>
    <td>Reflected power</td>
    <td>$Q_{r}$</td>
    <td>9 . 7 k W</td>
  </tr>
  <tr>
    <td>Heat power</td>
    <td>$Q_{0}$</td>
    <td>5 0 . 3 k W</td>
  </tr>
  <tr>
    <td>Power reflection</td>
    <td>$\eta_{0}$</td>
    <td>1 6 . 1 %</td>
  </tr>
  <tr>
    <td>Beam reflection</td>
    <td>$\eta_{b}$</td>
    <td>2 9 . 0 %</td>
  </tr>
</table>

表3 物質浸透深さ

<table>
  <tr>
    <td>Beam penetration</td>
    <td>$h_{e}$</td>
    <td>2 . 1 $\mu$ m</td>
  </tr>
  <tr>
    <td>Max-density depth h</td>
    <td>$e_{m}$</td>
    <td>0 . 6 2 $\mu$ m</td>
  </tr>
  <tr>
    <td>Power penetration h</td>
    <td>0</td>
    <td>1 . 4 $\mu$ m</td>
  </tr>
  <tr>
    <td>Max-power depth</td>
    <td>$h_{0}$</td>
    <td>0 . 4 8 $\mu$ m</td>
  </tr>
</table>

![](./images/811625289116286978_6.jpg)

図6 電子および発熱密度(銀)

![](./images/811625289116286978_7.jpg)

図7 電子ビームの浸透特性(銀)

 $3 \cdot 3$ 材料物性への依存性 ビーム反射率 $\eta_{b}$ および電子浸透深さ $h_{e}$ の被加熱物質の材料属性に対する依存性を図11, 12に示す. 図11中の破線はAr-chardらによる実験結果であり, 図12中の破線は図10 に準する(4)
 $3 \cdot 4$ 入射角依存性 図13は $3 \cdot 1$ 節に示した解析結果においてビーム入射角 $\alpha$ をパラメータとしたときの反射率を示す.

![](./images/811625289116286978_8.jpg)

図 8 電子密度(タングステン, $\alpha=0^{\circ}$ )

![](./images/811625289116286978_9.jpg)

図 9 反射率(タングステン, $\alpha=0^{\circ}$ )

![](./images/811625289116286978_10.jpg)

図 10 電子浸透深さ(タングステン, $\alpha=0^{\circ}$ )

( $E_{0}=30 keV, \alpha=0^{\circ}$ )
![](./images/811625289116286978_11.jpg)

図11 ビーム反射率の材料依存性

![](./images/811625289116286978_12.jpg)

図12 電子浸透深さの材料依存性

## 4. 検 討
### 4·1 電子ビームによる表面処理深さ β線など
の高エネルギー電子の物質中の飛程は, そのエネルギーを失うまでの移動距離の積分値として定義され, 電子飛程の実験式が文献値として式(28), (29)が与えられている. これによると最大電子密度は電子飛程の1/3の距離だけ表面より侵入した所にできることになる. 本解析による数値シミュレーションに基づき式(28), (29)を検証することができ, 電子エネルギーEおよび物質密度 $\rho$ への依存性をも併せて確認した.

また従来より電子の浸透深さと発熱密度の浸透深さとの差別化は成されていないが, 本解析によれば後者が前者の約 $70 \%$ 程度である.すなわち, 電子密度分布と発熱密度分布とはほぼ相似であるが, 浸透深さおよびその最大位置は共に発熱密度のほうが表面に近い場所にできる.

![](./images/811625289116286978_13.jpg)

図13 反射率の入射角依存性
(銀, $E_{0}=30 keV$ )

### 4·2 電子ビームの反射率について 電子ビーム
の反射率についてもビーム反射率とパワー反射率を差別化して考える必要がある. パワー反射率はビーム反射率に比べ10~15%低下するのが一般的である.これらの反射率は一般には, 電子ビームの性状にもよるが主に物質原子の属性(密度, 原子番号, 励起ポテンシャル)により決まる.

## 5.結 論
本研究に類する従来の研究例 $^{(5)}$ では, 高エネルギー電子の拡散挙動をモンテカルロ計算している. 本解析では電子ビームによる材料表面処理工程の数値解析を電子と物質(格子系)とのエネルギー授受も併せてモデル化しており, 材料中の電子密度と共に発熱密度をも並行して解析評価した.
(1) 電子ビームの浸透深さとして, 電子浸透深さと発熱浸透深さの定量的差異については従来言及されていなかった. 材料物質やビーム入射角により若干の差異はあるが, 発熱浸透深さは電子浸透深さの約70%程度であることを解析的に検証した.
(2) 以前より実験的に指摘されていた電子ビームにおけるパワー反射率とビーム反射率との差異については, 本解析により前者が後者より10~15%小さめであることを明らかにした.

## 文 献
(1) Schiller. S.. ほか2名, Electron Beam Technology.(1982),38ページ.John Wiley & Sons.
(2) Bethe. H. A.. Ann. Physik., 5. (1940), 325ページ.
(3) Chistenhusz. R., ほか1名, Z. Angew. Phys., 23(1967),397-404.
(4) Archard. G. D.. J. Appl. Phys., 32(1961), 1505-1509.
(5) Shimizu. R.. Jpn. J. Appl. Phys., 22-11(1983), 1631-1642.
-226-