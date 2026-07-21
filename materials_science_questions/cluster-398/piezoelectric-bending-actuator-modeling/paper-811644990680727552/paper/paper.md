# 中央き裂を有する圧電セラミックス帯板の衝撃応答*
上 田 整*1

# Impact Response of a Piezoelectric Ceramic Strip with a Central Crack
Sei UEDA*2

*2Osaka Institute of Technology, Omiya, Asahi ku, Osaka shi, Osaka, 535-8585 Japan

The plane strain dynamic singular stress problem for a piezoelectric ceramic plate having a central crack is considered. The Laplace and Fourier transform techniques are used o formulate the problem in terms of a singular integral equation. The singular integral equation is solved by using the Gauss-Jacobi integration formula. A numerical Laplace inversion routine is used to recover the time dependence of the solution. Numerical calculations are carried out, and the main results presented are the variation of the stress intensity factor as functions of the geometric parameters and the piezoelectric material properties of the plate.

Key Words: Stress Intensity Factor, Impact Strength, Ceramics, Elasticity, Fracture Mechanics, Piezoelectric

## 1. 緒 言
一般に圧電材料は, ひずみが加えられるとその表面に電荷が現れ, 電界が与えられると内部に応力が発生するような弾性体で, 機械系と電気系が空間的に結合している材料である. このように圧電材料は, 機械系と電気系という異なる系の間でエネルギー変換を伴う材料であるため, センサー·アクチュエータ材料として利用され, PZT系などの圧電セラミックスが注目されている(1). 近年の各種工学分野では, サブミクロンのオーダーでの変位制御が求められており(2), 圧電材料を用いた知的材料システムの電気熱弾性問題に関する理論的研究成果が数多く報告されている(1),(3)~(6).

一方, 圧電セラミックスなどの圧電材料の正確な寿命予測および圧電デバイスの構造健全性評価を行うためには, これらの材料の破壊過程を理解することが重要であり(7),電気破壊力学的挙動の解明が要望されている.このため, Shindoらは, 面外せん断荷重(7)~(9)あるいは引張荷重(10)下におけるき裂を有する圧電セラミックス帯板の特異応力問題を厳密に理論解析しており, Narita and Shindoは, 圧電積層材料に関するモードIII型き裂問題についても詳細な検討を行っている(11)~(14). また, 無限領域を占めるき裂を有する圧電セラミックスを対象とした衝撃応答問題も同様に解析されているが(15),(16),実際上重要であると考えられるき裂を有する圧電セラミックス帯板の衝撃応答問題に関しては, 面外せん断負荷の場合が報告されているに過ぎない(17).

そこで本報では,き裂を有する圧電セラミックス帯板がモードI型の衝撃負荷を受ける場合を考え,動的応力拡大係数の時間的挙動を理論解析した,き裂は,帯板の中央に帯板縁に垂直に存在するものとした. 解法には, Laplace-Fourier二重積分変換法を用い,問題の解を特異積分方程式の解に導いて解く方法を採用した(18).また,特異積分方程式の数値解析にはGauss-Jacobiの数値積分公式(19)を用い, Laplace逆変換には,数値Laplace逆変換法(20)を適用した.数値計算を行い,動的応力拡大係数の時間的挙動に及ぼす幾何学的形状および圧電セラミックスの材料定数の影響を明らかにして,詳細な検討を加えた.

## 2. 問題の設定および基礎式
図1に示す直角座標系(x,y,z)において,幅2hの圧電セラミックス帯板を考え, z=0面上の帯板中央に長さ2cのき裂が帯板縁に垂直に存在するものとする.

---
*原稿受付 2000年10月13日.
*1正員,大阪工業大学工学部(〒535-8585大阪市旭区大宮5-16-1).
E-mail: ueda@med.oit.ac.jp

この場合, 分極方向はz軸方向となる.

![](./images/811644990680727552_1.jpg)

Fig.1 A piezoelectric plate with a central crack

変位ベクトルの成分を $u_{x}(x, z, t), u_{z}(x, z, t)$ , 電界の強さベクトルの成分を $E_{x}(x, z, t), E_{z}(x, z, t)$ とすると, 応力テンソルの成分 $\sigma_{x x}(x, z, t), \sigma_{z z}(x, z, t)$ , $\sigma_{z x}(x, z, t)$ および電束密度べクトルの成分 $D_{x}(x, z, t)$ , D2(x,z,t)は次のように与えられる.
$$\left.\begin{array}{l}
\sigma_{x x}=c_{11} \frac{\partial u_{x}}{\partial x}+c_{13} \frac{\partial u_{z}}{\partial z}-e_{31} E_{z} \\
\sigma_{z z}=c_{13} \frac{\partial u_{x}}{\partial x}+c_{33} \frac{\partial u_{z}}{\partial z}-e_{33} E_{z} \\
\sigma_{z x}=c_{44}\left(\frac{\partial u_{x}}{\partial z}+\frac{\partial u_{z}}{\partial x}\right)-e_{15} E_{x}
\end{array}\right\} \quad \text { (1) }$$

$$\left.\begin{array}{l}
D_{x}=e_{15}\left(\frac{\partial u_{x}}{\partial z}+\frac{\partial u_{z}}{\partial x}\right)+\varepsilon_{11} E_{x} \\
D_{z}=e_{31} \frac{\partial u_{x}}{\partial x}+e_{33} \frac{\partial u_{z}}{\partial z}+\varepsilon_{33} E_{z}
\end{array}\right\} \quad \text { (2) }$$
ここに, t は時間, $c_{11}, c_{13}, c_{33}, c_{44}$ は弾性定数, $\varepsilon_{11}$ , $\varepsilon_{33}$ は誘電定数, $e_{15}, e_{31}, e_{33}$ は圧電定数である. 静電ポテンシャル $\phi(x, z, t)$ を導入すると, 電界の強さ E(x,z,t), Ez(x,z,t)は次のように表される.
$$E_{x}=-\frac{\partial \phi}{\partial x}, \quad E_{z}=-\frac{\partial \phi}{\partial z} \quad (3)$$
変位および静電ポテンシャルに関する場の支配方程式は
$$\left.\begin{array}{c}
c_{11} \frac{\partial^{2} u_{x}}{\partial x^{2}}+c_{44} \frac{\partial^{2} u_{x}}{\partial z^{2}}+\left(c_{13}+c_{44}\right) \frac{\partial^{2} u_{z}}{\partial x \partial z} \\
+\left(e_{31}+e_{15}\right) \frac{\partial^{2} \phi}{\partial x \partial z}=\rho \frac{\partial^{2} u_{x}}{\partial t^{2}} \\
c_{44} \frac{\partial^{2} u_{z}}{\partial x^{2}}+c_{33} \frac{\partial^{2} u_{z}}{\partial z^{2}}+\left(c_{13}+c_{44}\right) \frac{\partial^{2} u_{x}}{\partial x \partial z} \\
+\left(e_{15} \frac{\partial^{2} \phi}{\partial x^{2}}+e_{33} \frac{\partial^{2} \phi}{\partial z^{2}}\right)=\rho \frac{\partial^{2} u_{z}}{\partial t^{2}}
\end{array}\right\} \quad (4)$$

$$\begin{gathered}
\left(e_{31}+e_{15}\right) \frac{\partial^{2} u_{x}}{\partial x \partial z}+e_{15} \frac{\partial^{2} u_{z}}{\partial x^{2}}+e_{33} \frac{\partial^{2} u_{z}}{\partial z^{2}} \\
-\varepsilon_{11} \frac{\partial^{2} \phi}{\partial x^{2}}-\varepsilon_{33} \frac{\partial^{2} \phi}{\partial z^{2}}=0
\end{gathered}\qquad(5)$$
ここに, $\rho$ は圧電セラミックス帯板の質量密度である.
自由空間を考えると,構成方程式(2)および支配方程式(5)は
$$D_{x}=\varepsilon_{0} E_{x}, \quad D_{z}=\varepsilon_{0} E_{z} \quad (6)$$

$$\frac{\partial^{2} \phi}{\partial x^{2}}+\frac{\partial^{2} \phi}{\partial z^{2}}=0\quad (7)$$
ここに, $\varepsilon_{0}$ は自由空間の誘電率である.
問題の対称性を考慮し, $0 ≤x ≤h, 0 ≤y<\infty$ の第一象限で解析することにする. き裂面に垂直衝撃負荷が作用する場合を考えると, 境界条件式および対称条件式は(16)
$$\left.\begin{array}{ll}
\sigma_{z z}(x, 0, t)=-\frac{C_{33}}{c_{33}} \sigma_{0} H(t) & (0 \leq x<c) \\
u_{z}(x, 0, t)=0 & (c \leq x \leq h)
\end{array}\right\} \quad(8)$$

$$\left.\begin{array}{ll}
E_{x}(x, 0, t)=E_{x}^{c}(x, 0, t) & (0 \leq x<c) \\
\phi(x, 0, t)=0 & (c \leq x \leq h)
\end{array}\right\} \quad(9)$$

$$D_{z}(x, 0, t)=D_{z}^{c}(x, 0, t) \quad (0 \leq x \leq c) \quad (10)$$

$$\sigma_{z x}(x, 0, t)=0 \quad (0 \leq x \leq h) \quad (11)$$

$$\sigma_{z x}(0, z, t)=0 \quad (0 \leq z<\infty) \quad (12)$$

$$u_{x}(0, z, t)=0 \quad (0 \leq z<\infty) \quad (13)$$

$$\sigma_{x x}(h, z, t)=0 \quad (0 \leq z<\infty) \quad (14)$$

$$\sigma_{z x}(h, z, t)=0 \quad (0 \leq z<\infty) \quad (15)$$

$$D_{x}(h, z, t)=0 \quad (0 \leq z<\infty) \quad (16)$$
ここに, $C_{33}=c_{33}+e_{33}^{2} / \varepsilon_{33}, \sigma_{0}$ は応力の次元を有する定数,H()はHeavisideの単位階段関数であり, 上添字cはき裂内部の自由空間の場を示すものとする.
3. 解析
Laplace変換およびその逆変換を次式で定義する.
$$\left.\begin{array}{l}
f^{*}(p)=\int_{0}^{\infty} f(t) \exp (-p t) d t \\
f(t)=\frac{1}{2 \pi i} \int_{B r} f^{*}(p) \exp (p t) d p
\end{array}\right\} \quad(17)$$
ここに, BrはBromwichの積分路である. 式(4),(5)にLaplace-Fourier変換を適用して変位場および静電ポテンシャルの一般解を求めると(21)
$$\begin{aligned}
u_{x}^{*}(x, z, p)= & \frac{2}{\pi} \int_{0}^{\infty} \sum_{j=1}^{3}\left[a_{j}(s) A_{j}(s, p)\right. \\
& \left.× \exp \left\{-s \gamma_{j}(s) z\right\} \sin (s x)\right. \\
& \left.+a_{j}^{\prime}(s) B_{j}(s, p) \sinh \left\{s \gamma_{j}^{\prime}(s) x\right\} \cos (s z)\right] d s \quad(18)
\end{aligned}$$

$$u_{z}^{*}(x, z, p)=\frac{2}{\pi} \int_{0}^{\infty} \sum_{j=1}^{3}\left[\frac{1}{\gamma_{j}(s)} A_{j}(s, p)\right.$$


$$
\left.+\frac{1}{\gamma_{j}^{\prime}(s)} B_{j}(s, p) \cosh \left\{s \gamma_{j}^{\prime}(s) x\right\} \sin (s z)\right] d s \quad(19)
$$

$$
\begin{aligned}
\phi^{*}(x, z, p)=\frac{2}{\pi} \int_{0}^{\infty} \sum_{j=1}^{3}[ & -\frac{b_{j}(s)}{\gamma_{j}(s)} A_{j}(s, p) \\
& × \exp \left\{-s \gamma_{j}(s) z\right\} \cos (s x) \\
\left.-\frac{b_{j}^{\prime}(s)}{\gamma_{j}^{\prime}(s)} B_{j}(s, p) \cosh \left\{s \gamma_{j}^{\prime}(s) x\right\} \sin (s z)\right] & d s \quad(20)
\end{aligned}
$$

ここに, $A_{j}(s, p), B_{j}(s, p)(j=1,2,3)$ は境界条件より決定される未知関数であり, $\gamma_{j}(s), \gamma_{j}'(s), a_{j}(s), a_{j}'(s)$ ,bj(s), bj(s)' (j=1,2,3)は付録1に示す既知関数である. Laplace 像空間における電界の強さ $E_{x}^{*}(x, z, p)$ , $E_{z}^{*}(x, z, p)$ は式 (20) を式 (3) に代入して得られ, 応力成分 $\sigma_{x x}^{*}(x, z, p), \sigma_{z z}^{*}(x, z, p), \sigma_{z x}^{*}(x, z, p)$ および電束密度成分 $D_{x}^{*}(x, z, p), D_{z}^{*}(x, z, p)$ は, 式 (18),(19) および得られた電界の強さを式(1),(2)に代入することにより求まる. また, これらのLaplace像空間における変位場および応力場は, Laplace変換された境界条件式(12),(13)を自動的に満足している.

式(7)にFourier変換を適用して, き裂内部の自由空間における静電ポテンシャルを求めると
$$
\begin{aligned}
\phi^{c *}(x, z, p)=\frac{2}{\pi} \int_{0}^{\infty} D(s, p) & \sinh (s z) \cos (s x) d s \\
& (0 \leq x \leq c) \quad(21)
\end{aligned}
$$
ここに, $D(s, p)$ は未知関数である. また, 自由空間における電界の強さおよび電束密度成分は, 式(3),(6),(21)より求まる.

式(21)を考慮すると, Laplace変換した境界条件式(9),(11) より未知関数 $A_{j}(s, p)(j=1,2,3)$ は一つの新しい未知関数 $B_{0}(s, p)$ を用いて次のように表せる.
$$
\begin{array}{r}
A_{j}(s, p)=\frac{\gamma_{j}(s) k_{j}(s)}{k_{1}(s)+k_{2}(s)+k_{3}(s)} B_{0}(s, p) \\
(j=1,2,3) \quad(22)
\end{array}
$$

ここに
$$
\left.\begin{array}{l}
k_{1}(s)=b_{2}(s) f_{3}(s)-b_{3}(s) f_{2}(s) \\
k_{2}(s)=b_{3}(s) f_{1}(s)-b_{1}(s) f_{3}(s) \\
k_{3}(s)=b_{1}(s) f_{2}(s)-b_{2}(s) f_{1}(s)
\end{array}\right\} \quad(23)
$$

$$
\begin{array}{r}
f_{j}(s)=c_{44}\left\{a_{j}(s) \gamma_{j}(s)^{2}+1\right\}-e_{15} b_{j}(s) \\
(j=1,2,3) \quad(24)
\end{array}
$$

新しい未知関数 G(x, p) を次のように導入する $^{(18)}$ .
$$
G(x, p)=\left\{\begin{array}{ll}
\frac{\partial}{\partial x} u_{z}^{*}(x, 0, p) & (0 \leq x<c) \\
0 & (c \leq x \leq h)
\end{array}\right\} \quad(25)
$$

式(22)を考慮して式(19)を式(25)に代入し, Fourier逆変換することにより, $B_{0}(s, p)$ が次のように求まる.
$$
B_{0}(s, p)=-\frac{1}{s} \int_{0}^{c} G(\xi, p) \sin (s \xi) d \xi \quad(26)
$$
また, $G(\xi, p)$ が奇関数であることを考慮すると,Laplace変換された混合境界条件式(8)の第2式より次の補足の条件式が得られる.
$$
\int_{-c}^{c} G(\xi, p) d \xi=0\quad (27)
$$

Laplace変換された境界条件式(14)~(16)および式(26)を用いると, 混合境界条件式(8)の第1式より,未知関数 $G(\xi, p)$ に関する次の特異積分方程式が得られる.
$$
\begin{aligned}
& \frac{1}{\pi} \int_{-c}^{c} \frac{G(\xi, p)}{\xi-x} d t+\frac{1}{\pi} \int_{-c}^{c} G(\xi, p)\left\{M_{1}(\xi, x, p)\right. \\
& \left.+M_{2}(\xi, x, p)\right\} d t=\left(\frac{C_{33}}{c_{33} Q_{0}^{\infty}}\right) \frac{\sigma_{0}}{p}
\end{aligned}\quad (28)
$$
式 (28) 中の $M_{1}(\xi, x, p), M_{2}(\xi, x, p)$ は積分核であり,次式で与えられる.
$$
\left.\begin{array}{l}
M_{1}(\xi, x, p)=\int_{0}^{\infty} m_{1}(\xi, x, s, p) d s \\
M_{2}(\xi, x, p)=\int_{0}^{\infty} m_{2}(\xi, x, s, p) d s
\end{array}\right\} \quad(29)
$$

ここに
$$
\left.\begin{array}{c}
m_{1}(\xi, x, s, p)=\left\{\frac{Q_{0}(s)}{Q_{0}^{\infty}}-1\right\} \sin (s \xi) \cos (s x) d s \\
Q_{0}(s)=\frac{\sum_{j=1}^{3} \gamma_{j}(s) k_{j}(s) p_{0 j}(s)}{k_{1}(s)+k_{2}(s)+k_{3}(s)} \\
Q_{0}^{\infty}=\lim _{s \to \infty} Q_{0}(s)
\end{array}\right\}
$$
であり, $m_{2}(\xi, x, s, p)$ および $p_{0 j}(s)(j=1,2,3)$ は付録2に示す.

## 4. 特異積分方程式の数値解析
特異積分方程式(28)を数値解析するため, 次の無次元量を導入する.
$$
u=\frac{\xi}{c}, v=\frac{x}{c}, \kappa=\frac{p c}{c_{2}}, G(\xi, p)=\psi(u, \kappa) \quad(31)
$$
ここに, $c_{2}=(c_{44} / \rho)^{1 / 2}$ はせん断波の伝播速度である.また, 解 $\psi(u, \kappa)$ の特異性を考慮して, なめらかな関数 $\Psi(u, \kappa)$ を用いて $\psi(u, \kappa)$ を次のように置く $^{(19)}$ .
$$
\psi(u, \kappa)=\frac{\Psi(u, \kappa)}{\left(1-u^{2}\right)^{1 / 2}}\quad (32)
$$


中央き裂を有する圧電セラミックス帯板の衝撃応答

従って, 特異積分方程式(28)は, Gauss-Jacobiの数値積分公式(19)を用いて次式で近似される.
$$
\begin{gathered}
\sum_{m=1}^{N} \Psi\left(u_{m}, \kappa\right)\left\{\frac{1}{u_{m}-v_{n}}+c M_{1}\left(c u_{m}, c v_{n}, \frac{\kappa c_{2}}{c}\right)\right. \\
\left.+c M_{2}\left(c u_{m}, c v_{n}, \frac{\kappa c_{2}}{c}\right)\right\} W_{m}=\left(\frac{C_{33}}{c_{33} Q_{0}^{\infty}}\right) \frac{\sigma_{0}}{p} \\
(n=1,2,..., N-1) \quad(33)
\end{gathered}
$$
ここに, $W_{m}(m=1,2,..., N)$ は重みであり, $u_{m}, v_{n}$ はJacobiの多項式の根である. 式(33)より, N個の未知関数 $\Psi(u_{m}, \kappa) (m=1,2,..., N)$ に関する N-1個の代数方程式が得られ,さらに, 補足の条件式(27)より次の代数方程式が得られる.
$$\sum_{m=1}^{N} \Psi\left(u_{m}, \kappa\right) W_{m}=0\quad (34)$$
 $\Psi(u_{m}, \kappa)(m=1,2, ..., N)$ は, 式 (33) および式 (34)を数値解析することにより得られ, 後に定義される応力拡大係数に必要な $\Psi(1, \kappa)$ の值は, $\Psi(u_{N-3}, \kappa)$ ,Ψ(uN-2, k), Ψ(uN-1,k) の値から二次曲線を用いた外挿により求まる.
Laplace 像空間における動的応力拡大係数 $K_{I}^{*}(p)$ は次式で定義される.
$$\begin{aligned}
K_{\mathrm{I}}^{*}(p) & =\lim _{x \to c^{+}}\{2 \pi(x-c)\}^{1 / 2} \sigma_{z z}^{*}(x, 0, p) \\
& =\sigma_{0}(\pi c)^{1 / 2} Q_{0}^{\infty} \frac{\Psi\left(1, p c / c_{2}\right)}{p}
\end{aligned}\qquad(35)$$
従って, 動的応力拡大係数 $K_{I}(t)$ は
$$K_{\mathrm{I}}(t)=\sigma_{0}(\pi c)^{1 / 2} \frac{Q_{0}^{\infty}}{2 \pi i} \int_{B r} \frac{\Psi\left(1, p c / c_{2}\right)}{p} \exp (p t) d p$$

### 5. 数値結果および考察
式(36)にPapoulisの数値Laplace逆変換法(20)を適用し, 動的応力拡大係数 $K_{I}(t)$ の時間的挙動を解明する. 数値例として用いた圧電セラミックスPZT-4,PZT-5H, P-7およびPZT-6Bの材料定数を表1に示す(10),(16)

<table><caption>Table.1 Properties of piezoelectric ceramics</caption>
<thead>
  <tr>
    <th></th>
    <th>PZT-4</th>
    <th>PZT-5H</th>
    <th>P-7</th>
    <th>PZT-6B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$c_{11}$(GPa)</td>
    <td>139.0</td>
    <td>126.0</td>
    <td>130.0</td>
    <td>168.0</td>
  </tr>
  <tr>
    <td>$c_{13}$(GPa)</td>
    <td>74.3</td>
    <td>84.1</td>
    <td>83.1</td>
    <td>60.0</td>
  </tr>
  <tr>
    <td>$c_{33}$(GPa)</td>
    <td>113.0</td>
    <td>117.0</td>
    <td>119.0</td>
    <td>163.0</td>
  </tr>
  <tr>
    <td>$c_{44}$(GPa)</td>
    <td>25.6</td>
    <td>23.0</td>
    <td>25.0</td>
    <td>27.1</td>
  </tr>
  <tr>
    <td>$e_{13}$(C/m²)</td>
    <td>-6.98</td>
    <td>-6.50</td>
    <td>-10.3</td>
    <td>-0.9</td>
  </tr>
  <tr>
    <td>$e_{33}$(C/m²)</td>
    <td>13.8</td>
    <td>23.3</td>
    <td>14.7</td>
    <td>7.1</td>
  </tr>
  <tr>
    <td>$e_{15}$(C/m²)</td>
    <td>12.7</td>
    <td>17.0</td>
    <td>13.5</td>
    <td>4.6</td>
  </tr>
  <tr>
    <td>$\varepsilon_{11}$(nC/Vm)</td>
    <td>6.00</td>
    <td>15.04</td>
    <td>17.10</td>
    <td>3.6</td>
  </tr>
  <tr>
    <td>$\varepsilon_{33}$(nC/Vm)</td>
    <td>5.47</td>
    <td>13.00</td>
    <td>18.60</td>
    <td>3.4</td>
  </tr>
</tbody>
</table>

![](./images/811644990680727552_2.jpg)

Fig. 2 Dynamic stress intensity factor versus timefor $h / c \to \infty$

<table><caption>Table.2 $K_{I}^{M a x}, t^{M a x}, K_{I}^{\infty}$ および $K_{I}^{M a x} / K_{I}^{\infty}$</caption>
<thead>
  <tr>
    <th>$\frac{h}{c}$</th>
    <th>$\frac{K_{I}^{Max}}{\sigma_{0}(\pi c)^{1 / 2}}$</th>
    <th>$\frac{c_{2}t^{Max}}{c}$</th>
    <th>$\frac{K_{I}^{\infty}}{\sigma_{0}(\pi c)^{1 / 2}}$</th>
    <th>$\frac{K_{I}^{Max}}{K_{I}^{\infty}}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>PZT-4</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\infty$</td>
    <td>1.692</td>
    <td>2.340</td>
    <td>1.310</td>
    <td>1.292</td>
  </tr>
  <tr>
    <td>3.00</td>
    <td>1.612</td>
    <td>2.620</td>
    <td>1.518</td>
    <td>1.062</td>
  </tr>
  <tr>
    <td>2.00</td>
    <td>1.917</td>
    <td>$\infty$</td>
    <td>1.917</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.70</td>
    <td>2.368</td>
    <td>$\infty$</td>
    <td>2.368</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.50</td>
    <td>3.158</td>
    <td>$\infty$</td>
    <td>3.158</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>PZT-5H</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\infty$</td>
    <td>1.777</td>
    <td>2.520</td>
    <td>1.357</td>
    <td>1.310</td>
  </tr>
  <tr>
    <td>3.00</td>
    <td>1.728</td>
    <td>2.860</td>
    <td>1.582</td>
    <td>1.093</td>
  </tr>
  <tr>
    <td>2.00</td>
    <td>2.016</td>
    <td>$\infty$</td>
    <td>2.016</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.70</td>
    <td>2.509</td>
    <td>$\infty$</td>
    <td>2.509</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.50</td>
    <td>2.731</td>
    <td>$\infty$</td>
    <td>2.731</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>P-7</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\infty$</td>
    <td>1.418</td>
    <td>2.600</td>
    <td>1.098</td>
    <td>1.292</td>
  </tr>
  <tr>
    <td>3.00</td>
    <td>1.451</td>
    <td>2.880</td>
    <td>1.279</td>
    <td>1.135</td>
  </tr>
  <tr>
    <td>2.00</td>
    <td>1.629</td>
    <td>$\infty$</td>
    <td>1.629</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.70</td>
    <td>2.026</td>
    <td>$\infty$</td>
    <td>2.026</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.50</td>
    <td>2.731</td>
    <td>$\infty$</td>
    <td>2.731</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>PZT-6B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\infty$</td>
    <td>1.310</td>
    <td>2.400</td>
    <td>1.048</td>
    <td>1.249</td>
  </tr>
  <tr>
    <td>3.00</td>
    <td>1.320</td>
    <td>2.500</td>
    <td>1.191</td>
    <td>1.109</td>
  </tr>
  <tr>
    <td>2.00</td>
    <td>1.459</td>
    <td>$\infty$</td>
    <td>1.459</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.70</td>
    <td>1.753</td>
    <td>$\infty$</td>
    <td>1.753</td>
    <td>1.000</td>
  </tr>
  <tr>
    <td>1.50</td>
    <td>2.245</td>
    <td>$\infty$</td>
    <td>2.245</td>
    <td>1.000</td>
  </tr>
</tbody>
</table>

まず,動的応力拡大係数の時間的挙動に及ぼす材料の影響について検討する. 図2は, 帯板幅とき裂長さの比 $h / c \to \infty$ , すなわち, き裂を有する無限圧電体の場合について,無次元化された動的応力拡大係数 $K_{I}(t) / \sigma_{0}(\pi c)^{1 / 2}$ と無次元時間 $c_{2} t / c$ の関係を示したグラフである. 時間の経過に伴い,動的応力拡大係数は急激に増大して, 時刻 $t^{M a x}$ で最大值 $K_{I}^{M a x}$ に達した後, $p \to 0$ として得られる対応した静的值 $K_{I}^{\infty}$ に振動しながら漸近している. また, PZT-5HおよびPZT-6Bの場合の結果はShindoらの解(16)と良く一致している. それぞれの材料に対する $K_{I}^{M a x} / \sigma_{0}(\pi c)^{1 / 2}$ ,c2tMax/c, K /σo(πc)1/2および最大値と静的値の比 $K_{I}^{M a x} / K_{I}^{\infty}$ を表 2 に示す. $K_{I}^{M a x} / \sigma_{0}(\pi c)^{1 / 2}$ および $K_{I}^{\infty} / \sigma_{0}(\pi c)^{1 / 2}$ は PZT-6B, P-7, PZT-4, PZT-5Hの

--101--
NII-Electronic Library Service

順に増大し, $c_{2} t^{M a x} / c$ は PZT-4, PZT-6B, PZT-5H,P-7の順に遅くなる傾向を示す. また, 慣性効果を表す $K_{I}^{M a x} / K_{I}^{\infty}$ は, PZT-5H が最も大きな值であり, PZT4とP-7が同程度の値, PZT-6Bが最も小さい値となっている.

![](./images/811644990680727552_3.jpg)

Fig. 3 Dynamic stress intensity factor versus time for PZT-4

![](./images/811644990680727552_4.jpg)

Fig. 4 Dynamic stress intensity factor versus time for PZT-5H

次に, 動的応力拡大係数 $K_{I}(t)$ の時間的挙動に及ぼす幾何学的形状の影響を明らかにする. 図3~6は,それぞれPZT-4, PZT-5H, P-7およびPZT-6Bの場合の無次元化された動的応力拡大係数 $K_{I}(t) / \sigma_{0}(\pi c)^{1 / 2}$ と無次元時間 $c_{2} t / c$ の関係を帯板幅とき裂長さの比h/cをパラメータとして示したグラフであり, 破線は図 2 で検討した $h / c \to \infty$ の結果である. h / c の減少に伴い, 動的応力拡大係数 $K_{I}(t)$ は増大する傾向を示す. また, h/c=3.0の場合の動的応力拡大係数 $K_{I}(t)$ は, 各材料とも最初の極大值が最大值 $K_{I}^{M a x}$ となっており, $h / c \to \infty$ の場合と同様な傾向を示すのに対し, h / c ≤2.0 の $K_{I}(t)$ は $K_{I}^{M a x} / K_{I}^{\infty}=1.0$ であり, $t \to \infty$ で最大值となる. すなわち, h / c=2.0 の $K_{I}(t)$ は, $c_{2} t / c=0.25,10.0$ 付近で極大值となるが, その後時間の経過に伴い, 僅かに増大して $c_{2} t / c \to \infty$ で $K_{I}^{M a x}=K_{I}^{\infty}$ となる. また, h / c=1.7,1.5 の $K_{I}(t)$ には極大値は存在せず, 時間の経過に従って静的値に徐々に漸近する.

![](./images/811644990680727552_5.jpg)

Fig. 5 Dynamic stress intensity factor versus timefor P-7

![](./images/811644990680727552_6.jpg)

Fig. 6 Dynamic stress intensity factor versus time for PZT-6B

## 6. 結言
本報は, 帯板縁に垂直に存在するき裂を有する圧電セラミックス帯板の動的特異応力を厳密に理論解析したものである. 解法は, 積分変換法を用い, 問題の解を特異積分方程式の解に導いて解く方法によった. 特異積分方程式を数値解析し,動的応力拡大係数の時間的挙動に及ぼす幾何学的形状および圧電セラミックスの材料定数の影響を定量的に明らかにした.
本研究の一部は, 平成12年度文部省「バイオベンチャー研究開発拠点整備事業」の援助を得た. 記して謝意を表す.
## 文献
(1) Rao, S.S. and Sunar, M., Appl.Mech.Rev., 47(1994), 113-123.
(2) Noda, N. and Kimura, S., JSME Int.J., Ser.A, 43(2000), 117-123.
(3) Tauchert, T.R., J.Thermal Stresses, 15 (1992), 25-37.
(4) Noda, N. and Kimura, S., J.Thermal Stresses, 21(1998), 359-379.
-102-

(5) Ootao, Y. and Tanigawa, Y., Int.J.Solids Struct., 37(2000),4377-4401.
(6) Cheng, Z.-Q. and Batra, R.C., J.Thermal Stresses,23(2000),95-110.
(7)進藤裕英,田中宏治,機論,58-553(1992),1655-1661.
(8) Shindo, Y., Narita, F. and Tanaka, K., The- ore.Appl.Frac.Mech., 25 (1996), 65-71.
(9) Shindo, Y., Tanaka, K. and Narita, F., Acta Mech.,120(1997),31-45.
(10) Shindo, Y., Watanabe, K. and Narita, F., Int.J.Eng.Sci., 38 (2000), 1-19.
(11) Narita, F. and Shindo, Y., Theore.Appl. Frac.Mech.,30(1998),119-126.
(12) Narita, F. and Shindo, Y., JSME Int.J., Ser.A, 41(1998),40-48.
(13) Narita, F. and Shindo, Y., Int.J.Frac., 98 (1999),87-101.
(14) Narita, F. and Shindo, Y., Acta Mech., 134 (1999),27-43.
(15) Narita, F. and Shindo, Y., Theore.Appl.Frac. Mech.,29(1998),169-180.
(16) Shindo, Y., Narita, F. and Ozawa, E., Acta Mech.,137,(1999)99-107.
(17) Chen, Z.T. and Meguid, S.A., Int.J.Solids Struct.,37(2000),6051-6062.
(18) Gupta, G.D., Int.J.Solids Struct., 9 (1973), 1141-1154.
(19) Erdogan, F., Gupta, G.D. and Cook, T.S., Methods of Analysis and Solution of Crack Problems, (Edited by G.C. Sih), (1972), Noordhoff, Leyden.
(20) Papoulis, A., J.Appl.Mathe., 14 (1957), 405-414.
(21) Sneddon, I.N. and Lowengrub, M., (1969). Crack Problems in the Classical Theory of Elasticity,(1969), John Wiley & Sons, Inc., New York.

付 録 1
$\gamma_{j}(s)^{2}, \gamma_{j}'(s)^{2}(j=1,2,3)$ は次の $\gamma^{2}$ に関する特性方程式の3根である.

$$
\begin{aligned}
& \left\{F_{1}(s) G_{4}(s)+G_{1}(s) F_{4}(s)\right\}\left(\gamma^{2}\right)^{3}+\left\{F_{1}(s) G_{5}(s)\right. \\
& \left.+G_{1}(s) F_{5}(s)+F_{2}(s) G_{4}(s)+G_{2}(s) F_{4}(s)\right\}\left(\gamma^{2}\right)^{2} \\
& +\left\{F_{2}(s) G_{5}(s)+G_{2}(s) F_{5}(s)+F_{3}(s) G_{4}(s)\right. \\
& \left.+G_{3}(s) F_{4}(s)\right\}\left(\gamma^{2}\right) \\
& +F_{3}(s) G_{5}(s)+G_{3}(s) F_{5}(s)=0
\end{aligned}
$$

$$
\begin{aligned}
& \left\{F_{1}^{\prime}(s) G_{4}^{\prime}(s)+G_{1}^{\prime}(s) F_{4}^{\prime}(s)\right\}\left(\gamma^{\prime 2}\right)^{3}+\left\{F_{1}^{\prime}(s) G_{5}^{\prime}(s)\right. \\
& \left.+G_{1}^{\prime}(s) F_{5}^{\prime}(s)+F_{2}^{\prime}(s) G_{4}^{\prime}(s)+G_{2}^{\prime}(s) F_{4}^{\prime}(s)\right\}\left(\gamma^{\prime 2}\right)^{2} \\
& +\left\{F_{2}^{\prime}(s) G_{5}^{\prime}(s)+G_{2}^{\prime}(s) F_{5}^{\prime}(s)+F_{3}^{\prime}(s) G_{4}^{\prime}(s)\right. \\
& \left.+G_{3}^{\prime}(s) F_{4}^{\prime}(s)\right\}\left(\gamma^{\prime 2}\right) \\
& +F_{3}^{\prime}(s) G_{5}^{\prime}(s)+G_{3}^{\prime}(s) F_{5}^{\prime}(s)=0
\end{aligned}
$$

ここに

$$
\left.\begin{array}{rl}
F_{1}(s)= & \varepsilon_{33} c_{44} \\
F_{2}(s)= & -\varepsilon_{33} c_{11}-\varepsilon_{11} c_{44}-\left(e_{31}+e_{15}\right)^{2} \\
& -\varepsilon_{33} \rho(p / s)^{2} \\
F_{3}(s)= & \varepsilon_{11}\left\{c_{11}+\rho(p / s)^{2}\right\} \\
F_{4}(s)= & \left(c_{13}+c_{44}\right) \varepsilon_{33}+\left(e_{31}+e_{15}\right) e_{33} \\
F_{5}(s)= & -\left(c_{13}+c_{44}\right) \varepsilon_{11}-\left(e_{31}+e_{15}\right) e_{15} \\
F_{1}^{\prime}(s)= & \varepsilon_{11} c_{11} \\
F_{2}^{\prime}(s)= & -\varepsilon_{33} c_{11}-\varepsilon_{11} c_{44}-\left(e_{31}+e_{15}\right)^{2} \\
& -\varepsilon_{11} \rho(p / s)^{2} \\
F_{3}^{\prime}(s)= & \varepsilon_{33}\left\{c_{44}+\rho(p / s)^{2}\right\} \\
F_{4}^{\prime}(s)= & \left(c_{13}+c_{44}\right) \varepsilon_{11}+\left(e_{31}+e_{15}\right) e_{15} \\
F_{5}^{\prime}(s)= & \left(c_{13}+c_{44}\right) \varepsilon_{33}+\left(e_{31}+e_{15}\right) e_{33}
\end{array}\right\} \quad (39)
$$

$$
\left.\begin{array}{rl}
G_{1}(s)= & e_{33} c_{44} \\
G_{2}(s)= & -e_{33} c_{11}-e_{15} c_{44}+\left(e_{31}+e_{15}\right) \\
& \times\left(c_{13}+c_{44}\right)-e_{33} \rho(p / s)^{2} \\
G_{3}(s)= & e_{15}\left\{c_{11}+\rho(p / s)^{2}\right\} \\
G_{4}(s)= & \left(e_{31}+e_{15}\right) c_{33}-\left(c_{13}+c_{44}\right) e_{33} \\
G_{5}(s)= & \left(c_{13}+c_{44}\right) e_{15}-\left(e_{31}+e_{15}\right) \\
& \times\left\{c_{44}+\rho(p / s)^{2}\right\} \\
G_{1}^{\prime}(s)= & e_{15} c_{11} \\
G_{2}^{\prime}(s)= & -e_{33} c_{11}-e_{15} c_{44}+\left(e_{31}+e_{15}\right) \\
& \times\left(c_{13}+c_{44}\right)-e_{15} \rho(p / s)^{2} \\
G_{3}^{\prime}(s)= & e_{33}\left\{c_{44}+\rho(p / s)^{2}\right\} \\
G_{4}^{\prime}(s)= & \left(e_{31}+e_{15}\right) c_{44}-\left(c_{13}+c_{44}\right) e_{15} \\
G_{5}^{\prime}(s)= & \left(c_{13}+c_{44}\right) e_{33}-\left(e_{31}+e_{15}\right) \\
& \times\left\{c_{33}+\rho(p / s)^{2}\right\}
\end{array}\right\} \quad (42)
$$

また, $a_{j}(s), a_{j}'(s), b_{j}(s), b_{j}'(s)(j=1,2,3)$ は, 次式で与えられる.

$$
\left.\begin{array}{rl}
a_{j}(s) & =\frac{G_{4}(s) \gamma_{j}(s)^{2}+G_{5}(s)}{G_{1}(s) \gamma_{j}(s)^{4}+G_{2}(s) \gamma_{j}(s)^{2}+G_{3}(s)} \\
a_{j}^{\prime}(s) & =\frac{G_{4}^{\prime}(s) \gamma_{j}^{\prime}(s)^{2}+G_{5}^{\prime}(s)}{G_{1}^{\prime}(s) \gamma_{j}^{\prime}(s)^{4}+G_{2}^{\prime}(s) \gamma_{j}^{\prime}(s)^{2}+G_{3}^{\prime}(s)}
\end{array}\right\}
$$

$$
\left.\begin{array}{rl}
b_{j}(s)=\frac{1}{e_{31}+e_{15}} & {\left[\left\{c_{44} \gamma_{j}(s)^{2}-c_{11}\right.\right.} \\
& \left.\left.-\rho(p / s)^{2}\right\} a_{j}(s)+c_{13}+c_{44}\right] \\
b_{j}^{\prime}(s)=\frac{1}{e_{31}+e_{15}} & {\left[\left\{c_{11} \gamma_{j}^{\prime}(s)^{2}-c_{44}\right.\right.} \\
& \left.\left.-\rho(p / s)^{2}\right\} a_{j}^{\prime}(s)+c_{13}+c_{44}\right]
\end{array}\right\}
$$


884
中央き裂を有する圧電セラミックス帯板の衝撃応答

付 録 2

$m_{2}(\xi, x, s, p)$ は, 次式で与えられる.

$$
\begin{aligned}
m_{2}(\xi, x, s, p)=- & \frac{1}{Q_{0}^{\infty}} \sum_{i=1}^{3} \sum_{j=1}^{3} \theta_{j}(x, s) r_{j i}(s) \\
& × Q_{i}(s, \xi, p) q_{0 j}(s) \quad(45)
\end{aligned}
$$

ここに, $\theta_{j}(x, s), r_{j i}(s), Q_{i}(s, \xi, p)(i, j=1,2,3)$ およ
び $p_{i j}(s), q_{i j}(s)(i=0,1,2,3, j=1,2,3)$ は

$$
\left.\begin{array}{l}
\theta_{1}(x, s)=\frac{\cosh \left\{s \gamma_{1}^{\prime}(s) x\right\}}{\cosh \left\{s \gamma_{1}^{\prime}(s) h\right\}} \\
\theta_{l}(x, s)=\frac{\cosh \left\{s \gamma_{l}^{\prime}(s) x\right\}}{\sinh \left\{s \gamma_{l}^{\prime}(s) h\right\}} \quad(l=1,2)
\end{array}\right\} \quad(46)
$$

$$
\left.\begin{array}{rl}
r_{10}(s)=q_{11}(s) & +\left\{\frac{q_{12}(s) \delta_{11}(s)}{\delta_{10}(s)}\right\} \frac{T_{2}(s)}{T_{1}(s)} \\
& +\left\{\frac{q_{13}(s) \delta_{21}(s)}{\delta_{20}(s)}\right\} \frac{T_{3}(s)}{T_{1}(s)} \\
r_{11}(s)=- & \frac{1}{r_{10}(s)} \\
r_{12}(s)=- & \frac{1}{r_{10}(s)}\left\{\frac{q_{12}(s) \delta_{12}(s)}{\delta_{10}(s)} T_{2}(s)\right. \\
& \left.+\frac{q_{13}(s) \delta_{22}(s)}{\delta_{20}(s)} T_{3}(s)\right\} \\
r_{13}(s)=- & \frac{1}{r_{10}(s)}\left\{\frac{q_{12}(s) \delta_{13}(s)}{\delta_{10}(s)} T_{2}(s)\right. \\
& \left.+\frac{q_{13}(s) \delta_{23}(s)}{\delta_{20}(s)} T_{3}(s)\right\} \\
r_{21}(s)= & \frac{\delta_{11}(s) r_{11}(s)}{\delta_{10}(s) T_{1}(s)} \\
r_{22}(s)= & \frac{1}{\delta_{10}(s)}\left\{\frac{\delta_{11}(s) r_{12}(s)}{T_{1}(s)}+\delta_{12}(s)\right\} \\
r_{23}(s)= & \frac{1}{\delta_{10}(s)}\left\{\frac{\delta_{11}(s) r_{13}(s)}{T_{1}(s)}+\delta_{13}(s)\right\} \\
r_{31}(s)= & \frac{\delta_{21}(s) r_{11}(s)}{\delta_{20}(s) T_{1}(s)} \\
r_{32}(s)= & \frac{1}{\delta_{20}(s)}\left\{\frac{\delta_{21}(s) r_{12}(s)}{T_{1}(s)}+\delta_{22}(s)\right\} \\
r_{33}(s)= & \frac{1}{\delta_{20}(s)}\left\{\frac{\delta_{21}(s) r_{13}(s)}{T_{1}(s)}+\delta_{23}(s)\right\}
\end{array}\right\}
$$

$$
\begin{aligned}
& Q_{i}(s, \xi, p)=\sum_{j=1}^{3} P_{i j}^{\infty} \exp \left\{\frac{-(h-\xi) s}{\gamma_{j}^{\infty}}\right\} \\
& +\frac{1}{\pi} \sum_{j=1}^{3} \int_{0}^{\infty} R_{i j}(s, \xi, p, \eta) d \eta \quad(i=1,2,3) \quad(48)
\end{aligned}
$$

$$
\left.\begin{array}{l}
p_{0 j}(s)=c_{13} a_{j}(s)-c_{33}+e_{33} b_{j}(s) \\
p_{1 j}(s)=c_{11} a_{j}(s)-c_{13}+e_{31} b_{j}(s) \\
p_{2 j}(s)=c_{44}\left\{\gamma_{j}(s) a_{j}(s)+\frac{1}{\gamma_{j}(s)}\right\}-e_{15} \frac{b_{j}(s)}{\gamma_{j}(s)} \\
p_{3 j}(s)=e_{15}\left\{\gamma_{j}(s) a_{j}(s)+\frac{1}{\gamma_{j}(s)}\right\}+\varepsilon_{11} \frac{b_{j}(s)}{\gamma_{j}(s)} \\
q_{0 j}(s)=c_{13} \gamma_{j}^{\prime}(s) a_{j}^{\prime}(s)+c_{33} \frac{1}{\gamma_{j}^{\prime}(s)}-e_{33} \frac{b_{j}^{\prime}(s)}{\gamma_{j}^{\prime}(s)} \\
q_{1 j}(s)=c_{11} \gamma_{j}^{\prime}(s) a_{j}^{\prime}(s)+c_{13} \frac{1}{\gamma_{j}^{\prime}(s)}-e_{31} \frac{b_{j}^{\prime}(s)}{\gamma_{j}^{\prime}(s)} \\
q_{2 j}(s)=-c_{44}\left\{a_{j}^{\prime}(s)-1\right\}+e_{15} b_{j}^{\prime}(s) \\
q_{3 j}(s)=-e_{15}\left\{a_{j}^{\prime}(s)-1\right\}+\varepsilon_{11} b_{j}^{\prime}(s) \\
\quad(j=1,2,3) \quad(49)
\end{array}\right\}
$$

上式中, $T_{j}(s)(j=1,2,3), \delta_{i j}(s)(i=1,2, j=$
$0,1,2,3)$ および $R_{i j}(s, \xi, p, \eta)(i, j=1,2,3)$ は

$$
T_{j}(s)=\frac{1+\exp \left\{-2 s \gamma_{j}^{\prime}(s) h\right\}}{1-\exp \left\{-2 s \gamma_{j}^{\prime}(s) h\right\}} \quad(j=1,2,3) \quad(50)
$$

$$
\left.\begin{array}{l}
\delta_{10}(s)=q_{32}(s) q_{23}(s)-q_{22}(s) q_{33}(s) \\
\delta_{11}(s)=q_{21}(s) q_{33}(s)-q_{31}(s) q_{23}(s) \\
\delta_{12}(s)=q_{33}(s) \\
\delta_{13}(s)=-q_{23}(s) \\
\delta_{20}(s)=q_{33}(s) q_{22}(s)-q_{23}(s) q_{32}(s) \\
\delta_{21}(s)=q_{21}(s) q_{32}(s)-q_{31}(s) q_{22}(s) \\
\delta_{22}(s)=q_{32}(s) \\
\delta_{23}(s)=-q_{22}(s)
\end{array}\right\}
$$

$$
\left.\begin{array}{rl}
R_{1 j}(s, \xi, p, \eta) & =\eta\left[\frac{P_{1 j}(\eta)}{\eta^{2}+\left\{s / \gamma_{j}(\eta)\right\}^{2}}\right. \\
& \left.-\frac{P_{1 j}^{\infty}}{\eta^{2}+\left\{s / \gamma_{j}^{\infty}\right\}^{2}}\right] \sin \{(h-\xi) \eta\} \\
R_{l j}(s, \xi, p, \eta) & =s\left[\frac{P_{l j}(\eta)}{\eta^{2}+\left\{s / \gamma_{j}(\eta)\right\}^{2}}\right. \\
& \left.-\frac{P_{l j}^{\infty}}{\eta^{2}+\left\{s / \gamma_{j}^{\infty}\right\}^{2}}\right] \cos \{(h-\xi) \eta\}(l=2,3) \\
& (i=1,2,3) \quad(52)
\end{array}\right\}
$$

ここに

$$
\left.\begin{array}{l}
P_{i j}(\eta)=\frac{k_{j}(\eta) p_{i j}(\eta)}{k_{1}(\eta)+k_{2}(\eta)+k_{3}(\eta)} \\
P_{i j}^{\infty}=\lim _{\eta \rightarrow \infty} P_{i j}(\eta) \\
\gamma_{j}^{\infty}=\lim _{\eta \rightarrow \infty} \gamma_{j}(\eta)
\end{array}\right\}
$$

$(i, j=1,2,3)(53)$

--104--
NII-Electronic Library Service