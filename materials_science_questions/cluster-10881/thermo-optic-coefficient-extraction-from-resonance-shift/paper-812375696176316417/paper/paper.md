# Thermal effect of high power laser and output laser beam quality
Lu, Peihua
Wang, Runwen

Shanghai Institute of Optics & Fine Mechanics, Shanghai 201800,PRC

## ABSTRACT
In this paper, thermal equation of high power laser output coupler is established, and analysis solution of the equation with its boundary value of the actual model is given. The temperature distribution of output coupler is obtained. Then the thermal lens of output coupler is calculated also. Otherwise, the beam quality of output laser is discussed. All of these problems are significant for high power laser design.

Keywords thermal effect, high power laser, beam quality

## 1. INTRODUCTION
In high power CO₂ laser, the output coupler absorbs lots of laser power as the high power laser beam propagating through it, and a temperature distribution in the volume of coupler appears. Ordinarily, many kinds of cooling method are adopted to keep the coupler in lower temperature. Forcing the edge of coupler to be cold with cooling water is applied extensively because it can bring sufficient heat energy out of the device. Due to the limited value of the thermal conductivity of the coupler material, even though the laser device is running stably, it still forms a certain temperature distribution. Then it will lead to thermal distortion of the coupler and the thermal convex lens effect will appear. [1][2][3]

Existence of thermal effect of output coupler leads to the change of size and far field angle of output laser beam, and it is also the reason that the actual output laser beam is different with the ideal output beam. And then the quality of laser beam becomes poor. In this paper, the above process is discussed quantitatively.

## 2. RESONATOR OF HIGH POWER LASER
In high power CO₂ laser, the resonator is designed to be one plan mirror as coupler, and another concave mirror R as back reflective mirror, as fig.1(a) shows. When the high power CO₂ laser is running, the coupler absorbs lots of heat quantity, and forms a convex lens. So the running resonator consists of a convex mirror Rₜₕ and a concave mirror R. At the same time, before the laser outputted, it transmits through a convex lens f₀, as fig.1(b) shows.

The ABCD matrix of high power CO₂ laser is:
$$
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
=
\begin{bmatrix}
1 & L \\
0 & 1
\end{bmatrix}
$$

where, L is the length of the resonator.

So,
$$
\begin{split}
g_1 &= 1+\frac{L}{R_{th}} \\
g_2 &= 1-\frac{L}{R}
\end{split} \tag{1}
$$

The beam waist of the laser in resonator is,
$$
w_0 = \sqrt{\frac{\lambda L}{\pi}} \left[ \frac{g_1g_2(1-g_1g_2)}{(g_1+g_2-2g_1g_2)^2} \right]^{\frac{1}{4}} \tag{2}
$$

The position of beam waist in resonator is,
$$
z = \frac{g_2(1-g_1)L}{g_1+g_2-2g_1g_2} \tag{3}
$$

So the parameters of output laser is,

$$
W_{0}{ }^{\prime 2}=\frac{W_{0}{ }^{2}}{\left(1-\frac{z}{f}\right)^{2}+\frac{\pi^{2} w_{0}{ }^{4}}{\lambda^{2} f_{t h}{ }^{2}}} \tag{4}
$$

$$
z^{\prime}=\left[1-\frac{\left(1-\frac{z}{f}\right)}{\left(1-\frac{z}{f}\right)^{2}+\frac{\pi^{2} w_{0}{ }^{4}}{\lambda^{2} f_{t h}{ }^{2}}}\right] f_{t h} \tag{5}
$$

The far field angle is

$$
\theta=\frac{\lambda}{\pi w_{0}{ }^{\prime}} \tag{6}
$$

## 3. HEAT ENERGY BALANCE ANALYSIS OF COUPLER AND ITS THERMAL LENS EFFECT

### 3.1 Temperature distribution calculation of the laser coupler

As fig. 2(a), d is the thickness of laser coupler, a is the radius, and the coupler is cooled by water around its edge. We choose cylindrical coordinates system and the origin is on the center point of inside surface, and output laser propagates along z axis. As fig 2(b), we divide the coupler into a series of thin pieces and define $\Delta d$ the thickness of every piece. Compared with the diameter of the coupler, obviously there is $\Delta d<<2a$. In this piece, we can believe that laser power is almost absorbed uniformly by the whole coupler, and then the analysis solution of every piece is got easily. Let $n \to \infty$, the continuous analysis solution of thermal conducting equation is obtained. For simplicity, we suppose the laser beam that propagates in the coupler occupies the whole volume and uniformly distributed in each section of the coupler with constant thermal conductivity and thermal absorption index. Furthermore, temperature distribution is symmetrical around z axis.

We have the thermal conduction equation of the coupler,

$$
\frac{\partial^{2} T(r, z)}{\partial r^{2}}+\frac{1}{r} \frac{\partial T(r, z)}{\partial r}+\frac{\partial^{2} T(r, z)}{\partial z^{2}}=-\frac{\beta I}{k} \tag{7}
$$

where k is the thermal conductivity of coupler, $\beta$ is the absorption index of coupler, I is the laser power density which input the coupler and its distribution is uniform as expressed above, so $I=P/\pi a^{2}$, P is the laser power which input the coupler, a is the radius of the coupler.

Cooling water flows along the z axis, which cools the coupler edge from inside surface to outside. We suppose the origin temperature is $T_{c}$ and the edge temperature of inside surface is $T_{0}$ , edge temperature of outside is $T_{n}$ . Because of thermal absorption effects of the cooling water flowing along z axis, we can suppose edge temperature of the coupler increase linearly along the z axis, and then the boundary conditions of equation (7) is

$$
T(0,0)=T_{c}
$$

$$
T(a, z)=T_{0}+g z \tag{8}
$$

where, g is constant, $g=(T_{n}-T_{0})/d$ , d is the thickness of the coupler, a is the radius of the coupler.

Let $T(r, z)=F(r, z)-\frac{\beta I}{2 k} z^{2}$ , then equation (7) is transformed to

$$
\frac{\partial^{2} F(r, z)}{\partial r^{2}}+\frac{1}{r} \frac{\partial F(r, z)}{\partial r}+\frac{\partial^{2} F(r, z)}{\partial z^{2}}=0
\tag{9}
$$

An alternative method ("separation of variables") gives the solution of equation (9) and then gets the solution of equation (7)

$$
T(r, z)=\left(c_{1} \exp (\lambda z)+c_{2} \exp (-\lambda z)\right) J_{0}(\lambda r)-\frac{\beta I}{2 k} z^{2}
\tag{10}
$$

where $c_{1}, c_{2}$ are integral constants, their values are determined from boundary conditions. In equation (10), $\lambda$ may be any constant in principle, but it is related to the temperature distribution of inside surface of the coupler. When the other conditions are decided, the value of $\lambda$ is related to the initial heat distribution of the coupler.

From equation (10), when $z=0$, the temperature distribution of inside surface of the coupler is

$$
T(r, 0)=\left(c_{1}+c_{2}\right) J_{0}(\lambda r)
\tag{11}
$$

For $r=0$, gives center temperature $T_{c}$ from the boundary condition (8)

$$
T_{c}=T(0,0)=c_{1}+c_{2}
\tag{12}
$$

For $r=a$, formula (11) gives edge temperature $T_{0}$ of the inside surface

$$
T_{0}=T(a, 0)=\left(c_{1}+c_{2}\right) J_{0}(\lambda r)
\tag{13}
$$

Considering equation (12), (13) gives

$$
T_{0}=T_{c} J_{0}(\lambda a)
\tag{14}
$$

For $T_{0}, T_{c}$ can be obtained by experiment, then the value of $\lambda$ can be given from equation (14).Equation (11) expresses absolute temperature distribution of inside surface of the coupler which will lead to the determination of temperature distribution of the volume of the first thin piece, then the second -- -- and then the whole coupler, From equation (14), the bigger the value of $\lambda$ is the bigger the difference between the center and edge temperature of the coupler is, vice versa. Hence, the value of $\lambda$ is depended on the state of coupler heated by actual laser power and cooled by the water. The temperature of the origin in the coupler can be measured directly in experiment. So it is believed reasonably that the temperature of origin should be in proportion to the laser power which input into it when the material of coupler and cooling state are chosen, or it is measured from experiment. In this paper, we obtain $T_{c}=T_{0}+2 \times 10^{-4} P$ according to our actual device, where P's unit is W, $T_{c}$ is $^{\circ} K, T_{0}$ is the temperature when the input laser power is zero and that is also the temperature of circumstances. Figure 3 gives the curve of $\lambda$ and input laser power P according to equation (14).

As discussed above, the coupler is divided into n pieces along z axis, as figure 2 (b). The solution of every piece's thermal equation can be expressed as equation (10) with different constants $c_{1}$ and $c_{2}$ . The main reason is the temperature of cooling water is different in every piece. The thickness of every piece is d / n and the water absorbs more and more heat when it flows continually from edge of surface along z axis, so its temperature rises from $T_{0}$ to $T_{n}$ , which can be expressed as boundary (8).

Edge temperatures of the i-th piece's two surfaces are

$$
\begin{aligned}
& T\left(a, \frac{i-1}{n} d\right)=T_{i-1}=T_{0}+g \frac{(i-1) d}{n} \\
& T\left(a, \frac{i}{n} d\right)=T_{i}=T_{0}+g \frac{i d}{n}
\end{aligned}
\tag{15}
$$

From formula (10), two algebra equations with $c_{1}^{i}$ and $c_{2}^{i}$ are

$$
\begin{aligned}
& T\left(a, \frac{i-1}{n} d\right)=J_{0}(\lambda a)\left(c_{1}{ }^{i} \exp \left(\lambda \frac{i-1}{n} d\right)+c_{2}{ }^{i} \exp \left(-\lambda \frac{i-1}{n} d\right)\right)-\frac{\beta I}{2 k}\left(\frac{i-1}{n} d\right)^{2} \\
& T\left(a, \frac{i}{n} d\right)=J_{0}(\lambda a)\left(c_{1}{ }^{i} \exp \left(\lambda \frac{i}{n} d\right)+c_{2}{ }^{i} \exp \left(-\lambda \frac{i}{n} d\right)\right)-\frac{\beta I}{2 k}\left(\frac{i}{n} d\right)^{2}
\end{aligned}
\tag{16}
$$

Solving equation (15) and (16), then substituting $c_{1}{ }^{i}$ and $c_{2}{ }^{i}$ into (10) and arranging it, the temperature of the i-th piece is
$$
T\left(r, \frac{i}{n} d\right)=\left(T_{0}+g \frac{i}{n} d+\frac{\beta I}{2 k}\left(\frac{i}{n} d\right)^{2}\right) \frac{J_{0}(\lambda r)}{J_{0}(\lambda a)}-\frac{\beta I}{2 k}\left(\frac{i}{n} d\right)^{2}
$$

Let $n \rightarrow \infty$, that is to say, the coupler is divided into infinite pieces, then $\frac{i}{n} d \rightarrow z$.

Hence the analysis solution of the coupler temperature is
$$
T(r, z)=\left(T_{0}+g z+\frac{\beta I}{2 k} z^{2}\right) \frac{J_{0}(\lambda r)}{J_{0}(\lambda a)}-\frac{\beta I}{2 k} z^{2}
\tag{17}
$$

### 3.2 Analysis of convex lens effects of the coupler

Thermal expansion coefficient of coupler is $\alpha$, its refractive index in normal temperature is $n_{0}$, the derivative of refractive index to temperature is $\gamma=\frac{d n}{d T}$, The optical path in the coupler which propagated by the laser beam is
$$
L(r)=\int_{0}^{d} n_{0}\left(1+\gamma\left(T(r, z)-T_{0}\right)\right)\left(1+\alpha\left(T(r, z)-T_{0}\right)\right) d z
\tag{18}
$$

Generally, the amount of $\alpha$ and $\gamma$ are about $10^{-6}$. Omitting their quadratic item, L(r) can be expressed as
$$
L(r)=n_{0} \int_{0}^{d}\left(1+(\alpha+\gamma)\left(T(r, z)-T_{0}\right)\right) d z
$$

Substituting equation (18) into above equation, L(r) can be simplified as
$$
L(r)=n_{0} d+(\alpha+\gamma) n_{0}\left(\left(T_{0} d+\frac{1}{2} g d^{2}+\frac{\beta I}{6 k} d^{3}\right) \frac{J_{0}(\lambda r)}{J_{0}(\lambda a)}-\frac{\beta I}{6 k} d^{3}-T_{0} d\right)
\tag{19}
$$

So the optical path difference between center axle and edge of coupler can be expressed as
$$
\Delta L=L(0)-L(a)=(\alpha+\gamma) n_{0}\left(T_{0} d+\frac{1}{2} g d^{2}+\frac{\beta I}{6 k} d^{3}\right)\left(\frac{1}{J_{0}(\lambda a)}-1\right)
\tag{20}
$$

Suppose the radii of both surfaces of the thin lens are the same, and equal to $R_{th}$.

Then,
$$
R_{t h}=\frac{a^{2}}{\Delta L}
\tag{21}
$$

is got. The focal length of thin lens is
$$
f_{t h}=\frac{R_{t h}}{2\left(n_{0}-1\right)}=\frac{a^{2}}{2 \Delta L\left(n_{0}-1\right)}
\tag{22}
$$

## 4. RESULT AND DISSCUSSION

Figure 4 gives 3D temperature distribution of the coupler, where GaAs material is chosen. The parameters are, $k=0.037 \mathrm{~W} / \mathrm{cm}$ ${ }^{\circ} \mathrm{K}, \beta=0.012 \mathrm{~cm}^{-1}, \mathrm{a}=1 \mathrm{~cm}, \mathrm{~d}=0.5 \mathrm{~cm}, \mathrm{n}_{0}=3.30, \quad \gamma=18.7^{*} 10^{-5} /{ }^{\circ} \mathrm{K}, \alpha=5.7 * 10^{-6} /{ }^{\circ} \mathrm{K}, \mathrm{P}=1000 \mathrm{~W}, \lambda=0.053, \mathrm{~T}_{1}=298{ }^{\circ} \mathrm{K}, \mathrm{T}_{\mathrm{n}}=$ $298.1^{\circ} \mathrm{K}$. The result of figure 4 shows that the temperature variation at the edge of coupler along $\mathrm{z}$ axis is almost linear, and radial temperature variation in each section is slowly decreasing near the central area, the fast decreasing nearly linearly. Figure 5 gives the

curve of focal length for equivalent thermal convex lens v.s. different input laser power. It shows that, the bigger the input laser power is, the bigger the temperature difference between center and edge is, which leads to the change of optical path more serious and the thermal focal length is shorter. Figure 6 gives the curve of beam waist of output laser v.s. different laser power. It shows that, the bigger the laser power is, the smaller the beam waist is, and the bigger the far field angle is as showed in figure 8. Figure 7 shows the position of beam waist v.s. laser power. It shows that the beam waist is farther from output coupler when the laser power is bigger.

## 5. REFERENCES
1.M.Sparks, Optical Distortion by Heated Windows in High-power Laser Systems, J,Appl.Phys.NOV.1971,42:5027

2.B.S.Patael, Optical Suitability of Windows Materials for CO₂ Laser. Appl.Opt.May 1977, 16(5):1232

3.Jim Evans, Thermal Lens: a practical approach, SPIE 1992 (1625) :44

![](./images/812375696176316417_1.jpg)

![](./images/812375696176316417_2.jpg)

Figure 2 Schematic diagram of laser coupler

![](./images/812375696176316417_3.jpg)

![](./images/812375696176316417_4.jpg)

![](./images/812375696176316417_5.jpg)

![](./images/812375696176316417_6.jpg)

![](./images/812375696176316417_7.jpg)

![](./images/812375696176316417_8.jpg)