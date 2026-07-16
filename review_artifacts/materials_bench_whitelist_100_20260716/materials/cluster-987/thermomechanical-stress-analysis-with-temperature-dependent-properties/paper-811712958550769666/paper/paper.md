T. R. Hsu
Professor. Assoc. Mem. ASME

S. R. Trasi
Postdoctoral Fellow.
Assoc. Mem. ASME

Department of Mechanical Engineering,
University of Manitoba,
Winnipeg, Manitoba, Canada

# On the Analysis of Residual Stresses Introduced in Sheet Metals by Thermal Shock Treatment

This paper presents a theoretical study of the residual stresses in a thin metal sheet with a circular hole subjected to an axially symmetric thermal shock over a concentric annular area. Quasi-static, uncoupled, thermoelastoplasticity theory incorporating the postulates of incremental plasticity theory is employed. The solution is sought through a numerical technique incorporating an iteration scheme and numerical integration. Several numerical examples are considered for a specific distribution and duration of the thermal shock and some optimization considerations are discussed.

## Introduction

Residual stresses arising out of manufacturing processes in components and structures usually have an adverse effect on their fatigue life. However, by proper control of their magnitude and distribution, residual stresses can be put to advantage. Means such as thermal shock by pulse lasers may be developed to achieve such a purpose in specific cases as demonstrated by Hsu [1].¹

In this paper, the authors have presented the results of a simpler but more restrictive theoretical study, prompted by the encouraging results reported in [1], on the introduction of beneficial residual stresses in the neighborhood of the periphery of a concentric hole in a thin disk by a thermal shock applied over a concentric annular area. Quasi-static, uncoupled, thermoelastoplasticity theory incorporating the postulates of incremental plasticity theory is employed. The material of the disk is assumed to be homogeneous, isotropic, and elastic-perfectly plastic throughout the entire process and to obey von Mises' yield criterion and to have temperature-independent properties, except for the yield strength in pure shear which is assumed to vary with temperature.

The theoretical analysis is further simplified by the introduction of thermal shock through axisymmetric heat sources and by accounting for the heat loss from the flat faces of the disk through the introduction of appropriate axisymmetric heat sinks, distributed uniformly over the thickness of the disk and varying in intensity only along the radial coordinate and in time. Heat loss at the inner and outer radial boundaries of the disk is accounted for by the convective heat transfer boundary conditions. The disk is assumed to be free of any mechanical loading and to be sufficiently thin to justify the assumption of plane stress conditions. One is thus left with two-dimensional axisymmetric thermal and thermoelastoplastic problems pertaining to the disk as presented in the following.

While the thermal problem is solved exactly, the solution of the thermoelastoplastic problem is sought through a numerical technique incorporating an iteration scheme and numerical integration. Numerical results in the form of graphs are presented to demonstrate the positive contribution of the residual stresses. Studies on the optimal location, width and strength of the thermal shock of a specific distribution and duration are illustrated.

## Thermal Problem

A cylindrical coordinate system is chosen as shown in Fig. 1. Assuming that the initial temperature of the disc and the temperature of the surrounding environment are zero, the temperature $T(r, t)$ of the disk, as a function of the radius $r$ and the time variable $t$, is governed by equations (1)-(3):

---
¹ Numbers in brackets designate References at end of paper.
Contributed by the Applied Mechanics Division for presentation at the National Conference of Applied Mechanics, University of Utah, Salt Lake City, Utah, June 15-17, 1976, of THE AMERICAN SOCIETY OF MECHANICAL ENGINEERS.
Discussion on this paper should be addressed to the Editorial Department, ASME, United Engineering Center, 345 East 47th Street, New York, N. Y. 10017, and will be accepted until June 1, 1976. Readers who need more time to prepare a Discussion should request an extension of the deadline from the Editorial Department. Manuscript received by ASME Applied Mechanics Division, February, 1975; final revision, August, 1975. Paper No. 76-APM-13.

---
Journal of Applied Mechanics
Copyright © 1976 by ASME
MARCH 1976 / 117

![](./images/811712958550769666_1.jpg)

Fig. 1 Dimensions of specimen and heat input function

$$
\begin{aligned}
\frac{\partial^{2} T(r, t)}{\partial r^{2}}+\frac{1}{r} \frac{\partial T(r, t)}{\partial r} &-\frac{2 h T(r, t)}{k w}+\frac{q(r, t)}{k} \\
&=\frac{1}{\kappa} \frac{\partial T(r, t)}{\partial t}, \begin{cases}a<r<b, \\
0<t<\infty\end{cases}
\end{aligned}
$$

$$
T(r, 0)=0, \quad a \leq r \leq b \tag{2}
$$

$$
\left.\begin{array}{rl}
-k \frac{\partial T(r, t)}{\partial r}+h_{1} T(r, t)=0 & \text { at } r=a \text { for } t>0 \\
k \frac{\partial T(r, t)}{\partial r}+h_{2} T(r, t)=0 & \text { at } r=b \text { for } t>0
\end{array}\right\}
$$

In equation (1), the third term arises out of the heat loss from the flat faces $z=\pm w / 2$ of the disk where $h$ is the surface heat transfer coefficient for the flat faces. The radii of the hole and the disk are $a$ and $b$, respectively, and $h_{1}$ and $h_{2}$ are the surface heat transfer coefficients at the respective curved boundaries. Also, $k$ is the coefficient of thermal conductivity, $q$ is the intensity of the heat source representing the thermal shock and $\kappa$ is the diffusivity.

The solution of the thermal problem, defined by equations (1)-(3) and comprising the determination of $T(r, t)$, may be easily obtained by the integral transform technique outlined in [2]. The specific distribution of the thermal shock under consideration here may be approximated as shown in Fig. 1 and can be mathematically represented as

$$
\left.\begin{aligned}
q(r, t)=Q\left[H\left(r-a_{1}\right)-H\left(r-b_{1}\right)\right] \\
\cdot\left[H(t)-H\left(t-t_{1}\right)\right],
\end{aligned}\right\} \begin{aligned}
&a<a_{1}<b_{1}<b, \\
&0<t_{1}<\infty
\end{aligned}
$$

where $H(x)=0$ for $x<0$ and $H(x)=1$ for $x \geq 0$ and $Q$ represents the intensity of the thermal shock. Employing the Hankel transform defined in [2, p. 138], the temperature $T(r, t)$ of the disk may be obtained as the following:

For $a \leq r \leq b, 0 \leq t \leq t_{1}:$

$$
\begin{aligned}
\frac{T(r, t)}{\left(\frac{b^{2} Q}{k}\right)}= & \sum_{m=1}^{\infty} \frac{\left[P_{1}\left(\beta_{m}\right) K_{0}\left(\beta_{m}, r\right)\right]}{\gamma_{m}{ }^{2}}\left[1-e^{-\gamma_{m}{ }^{2}\left(\frac{\kappa t}{b^{2}}\right)}\right], h \neq 0 \\
= & \left\{\left(\frac{\kappa t}{b^{2}}\right)\left[P_{1}\left(\beta_{1}\right) K_{0}\left(\beta_{1}, r\right)\right]\right. \\
& \left.+\sum_{m=2}^{\infty} \frac{\left[P_{1}\left(\beta_{m}\right) K_{0}\left(\beta_{m}, r\right)\right]}{\gamma_{m}{ }^{2}}\left[1-e^{-\gamma_{m}{ }^{2}\left(\frac{\kappa t}{b^{2}}\right)}\right]\right\}, h=0
\end{aligned}
$$

For $a \leq r \leq b, t_{1} \leq t<\infty:$

$$
\begin{aligned}
\frac{T(r, t)}{\left(\frac{b^{2} Q}{k}\right)}= & \left\{\sum_{m=1}^{\infty} \frac{\left[P_{1}\left(\beta_{m}\right) K_{0}\left(\beta_{m}, r\right)\right]}{\gamma_{m}{ }^{2}}\right. \\
& \left.\times\left[1-e^{-\gamma_{m}{ }^{2}\left(\frac{\kappa t_{1}}{b}\right)}\right] e^{-\gamma_{m}{ }^{2}\left[\frac{\kappa\left(t-t_{1}\right)}{b^{2}}\right]}\right\} h \neq 0 \\
= & \left\{\left(\frac{\kappa t_{1}}{b^{2}}\right)\left[P_{1}\left(\beta_{1}\right) K_{0}\left(\beta_{1}, r\right)\right]\right. \\
& +\sum_{m=2}^{\infty} \frac{\left[P_{1}\left(\beta_{m}\right) K_{0}\left(\beta_{m}, r\right)\right]}{\gamma_{m}{ }^{2}}\left[1-e^{-\gamma_{m}{ }^{2}\left(\frac{\kappa t_{1}}{b^{2}}\right)}\right] \\
& \left.\times e^{-\gamma_{m}{ }^{2}\left[\frac{\kappa\left(t-t_{1}\right)}{b^{2}}\right]}\right\}, h=0 \quad(6)
\end{aligned}
$$

where

$$
\gamma_{m}{ }^{2}=\left(b \beta_{m}\right)^{2}+\frac{2 h b^{2}}{k w}, \quad m=1,2, \ldots, \infty \tag{7}
$$

$$
\left.\begin{array}{rl}
P_{1}\left(\beta_{1}\right) & =\sqrt{2 /\left(b^{2}-a^{2}\right)}\left[\left(b_{1}{ }^{2}-a_{1}{ }^{2}\right) / 2\right] \\
P_{1}\left(\beta_{m}\right) & =\frac{1}{\beta_{m} \sqrt{N\left(\beta_{m}\right)}}\left\{\frac{b_{1} J_{1}\left(\beta_{m} b_{1}\right)-a_{1} J_{1}\left(\beta_{m} a_{1}\right)}{h_{2} J_{0}\left(\beta_{m} b\right)-k \beta_{m} J_{1}\left(\beta_{m} b\right)}\right. \\
& \left.-\frac{b_{1} Y_{1}\left(\beta_{m} b_{1}\right)-a_{1} Y_{1}\left(\beta_{m} a_{1}\right)}{h_{2} Y_{0}\left(\beta_{m} b\right)-k \beta_{m} Y_{1}\left(\beta_{m} b\right)}\right\}, \\
m & =2,3, \ldots, \infty
\end{array}\right\}
$$

$$
K_{0}\left(\beta_{m}, r\right)=R_{0}\left(\beta_{m}, r\right) / \sqrt{N\left(\beta_{m}\right)}, \quad m=1,2,3, \ldots, \infty \quad(9)
$$

$$
\begin{aligned}
R_{0}\left(\beta_{m}, r\right)=1, & \beta_{m}=0 \\
= & \frac{J_{0}\left(\beta_{m} r\right)}{h_{2} J_{0}\left(\beta_{m} b\right)-k \beta_{m} J_{1}\left(\beta_{m} b\right)} \\
& \quad-\frac{Y_{0}\left(\beta_{m} r\right)}{h_{2} Y_{0}\left(\beta_{m} b\right)-k \beta_{m} Y_{1}\left(\beta_{m} b\right)}, \beta_{m} \neq 0 \quad(10)
\end{aligned}
$$

$$
\begin{aligned}
N\left(\beta_{m}\right)=\left(b^{2}-a^{2}\right) / 2, & \beta_{m}=0 \\
=\frac{b^{2}}{2}\left[\frac{h_{2}{ }^{2}}{k^{2} \beta_{m}{ }^{2}}+1\right] & R_{0}{ }^{2}\left(\beta_{m}, b\right) \\
-\frac{a^{2}}{2}\left[\frac{h_{1}{ }^{2}}{k^{2} \beta_{m}{ }^{2}}+1\right] & R_{0}{ }^{2}\left(\beta_{m}, a\right), \beta_{m} \neq 0 \quad(11)
\end{aligned}
$$

The eigenvalues $\beta_{m}\left(\beta_{1}=0\right), m=2,3, \ldots \infty$ are the positive roots of the following transcendental equation:

$$
\begin{aligned}
{\left[\left(\frac{h_{1} b}{k}\right) J_{0}(\beta a)\right.} & \left.+\beta b J_{1}(\beta a)\right]\left[\left(\frac{h_{2} b}{k}\right) Y_{0}(\beta b)-\beta b Y_{1}(\beta b)\right] \\
& -\left[\left(\frac{h_{2} b}{k}\right) J_{0}(\beta b)-\beta b J_{1}(\beta b)\right] \\
& \times\left[\left(\frac{h_{1} b}{k}\right) Y_{0}(\beta a)+\beta b Y_{1}(\beta a)\right]=0 \quad(12)
\end{aligned}
$$

---

118 / MARCH 1976

Transactions of the ASME

# Thermoelastoplastic Problem

The radial displacement $u(r, t)$, the principal strains $\epsilon_j(r, t), j = r, \theta, z$ and the principal stresses $\sigma_j(r, t), j = r, \theta$ ($\sigma_z = 0$) are governed by

**Equilibrium Equation:**
$$
\left. rac{\partial \sigma_r}{\partial r} + rac{\sigma_r - \sigma_\theta}{r} = 0, ight\}
egin{aligned}
&a < r < b \
&0 < t < \infty
\end{aligned} \tag{13}
$$

**Initial Conditions:**
$$
\sigma_r(r,0) = \sigma_\theta(r,0) = 0, \quad a \leq r \leq b \tag{14}
$$

**Boundary Conditions:**
$$
\sigma_r(a,t) = \sigma_r(b,t) = 0, \quad 0 < t < \infty \tag{15}
$$

**Strain-Displacement Relations:**
$$
\epsilon_r = rac{\partial u}{\partial r}; \epsilon_\theta = rac{u}{r} \tag{16}
$$

**Constitutive or Stress-Strain Relations [3, pp. 474, 480]:**
$$
\begin{gathered}
\epsilon = \alpha T + rac{\sigma}{3K}; e_j^E = rac{1}{2G} s_j,\ j = r,\theta,z \
\dot{e}_j^P = [1 - g(r,t)]\ \mu(r,t)\ s_j,\ j = r,\theta,z \
g = egin{cases}
1 & 	ext{if } f < 0 	ext{ or if } f = 0 	ext{ and } \mu < 0 \
0 & 	ext{if } f = 0 	ext{ and } \mu \geq 0
\end{cases} \
\mu = (GS_j \dot{e}_j - \sigma_{ys} \dot{\sigma}_{ys})/(2G\sigma_{ys}^2),\ j = r,\theta,z \
f = J_2 - \sigma_{ys}^2;\ J_2 = (s_r^2 + s_\theta^2 + s_z^2)/2
\end{gathered} \tag{17}
$$

The material properties appearing in equation (17) are the coefficient of linear thermal expansion $\alpha$, the Poisson's ratio $\nu$, the bulk modulus $K = E/[3(1 - 2\nu)]$ where $E$ is the Young's modulus, the shear modulus $G = E/2(1 + \nu)$, and the temperature-dependent yield strength in pure shear $\sigma_{ys}(T)$. The new variables in equation (17) are the mean stress $\sigma(r, t) = (\sigma_r + \sigma_\theta)/3$, the mean strain $\epsilon(r, t) = (\epsilon_r + \epsilon_\theta + \epsilon_z)/3$, the deviatoric stresses $s_j = \sigma_j - \sigma,\ j = r, \theta, z$ and the deviatoric strains $e_j = e_j^E + e_j^P = \epsilon_j - \epsilon,\ j = r, \theta, z$ where the superscripts $E$ and $P$ stand for the elastic and plastic component, respectively. The dot above the characters represents differentiation with respect to time, e.g., $\dot{\sigma}_{ys} \equiv \dot{T} (d\sigma_{ys}(T)/dT)$.

The second stress invariant $J_2$ and the variable $\mu$ may be rewritten for convenience as
$$
J_2 = rac{1}{4}(3\sigma^2 + s^2) \tag{18}
$$

$$
\begin{aligned}
\mu(r,t) = rac{1}{4\sigma_{ys}^2} \Bigg\{ &s \Bigg[ rac{\dot{s}}{2G} + (1 - g)\ \mu s \Bigg] \
&+ 3\sigma \Bigg[ rac{\dot{\sigma}}{2G} + (1 - g)\mu\sigma \Bigg] - 2\sigma_{ys}\dot{\sigma}_{ys} \Bigg\} \tag{19}
\end{aligned}
$$

where the new variable $s(r, t)$ and another new variable $e(r, t)$, introduced now for later convenience, are defined as
$$
s = s_r - s_\theta = \sigma_r - \sigma_\theta;\ e = e_r - e_\theta = \epsilon_r - \epsilon_\theta \tag{20}
$$

The process of solution of the thermoelastoplastic problem, defined by equations (13)-(20) and comprising the determination of the stress distribution, is similar to that of [4]. One has
$$
rac{\partial (ru)}{\partial r} = r(\epsilon_r + \epsilon_\theta) = r\left[3\alpha T + rac{\sigma}{K} - \epsilon_z\right]
$$

From the foregoing, one obtains,
$$
\begin{aligned}
u(r,t) = rac{a}{r}u(a,t) + rac{1}{r} \int_a^r \Bigg[ &3\alpha T(r,t) \
&+ rac{\sigma(r,t)}{K} - \epsilon_z(r,t) \Bigg] r\ dr \quad (21)
\end{aligned}
$$

$$
\begin{aligned}
\epsilon_r(r,t) = -rac{a}{r^2}u(a,t) - rac{1}{r^2} \int_a^r \Bigg[ &3\alpha T(r,t) \
&+ rac{\sigma(r,t)}{K} - \epsilon_z(r,t) \Bigg] r\ dr \
&+ 3\alpha T(r,t) + rac{\sigma(r,t)}{K} - \epsilon_z(r,t)
\end{aligned}
$$

$$
\begin{aligned}
\epsilon_\theta(r,t) = rac{a}{r^2}u(a,t) + rac{1}{r^2} \int_a^r \Bigg[ &3\alpha T(r,t) \
&+ rac{\sigma(r,t)}{K} - \epsilon_z(r,t) \Bigg] r\ dr \quad (21)
\end{aligned}
$$
(Cont.)

From equations (13), (17), and (20), one can show that
$$
\dot{\epsilon}_z(r,t) = \alpha \dot{T} - [1 - g]\mu\sigma - rac{3\nu}{E}\dot{\sigma} \tag{22}
$$

$$
\dot{s} = 2G[\dot{e} - (1 - g)\mu s] \tag{23}
$$

$$
\sigma_r(r,t) = -\int_a^r rac{s(r,t)}{r}\ dr \tag{24}
$$

Equation (24) clearly satisfies the boundary condition at $r = a$. In view of equation (14), the boundary condition at $r = b$ of equation (15) may be replaced by
$$
\dot{\sigma}_r(b,t) = -\int_a^b rac{\dot{s}(r,t)}{r} dr = 0,\ t \geq 0_* \tag{25}
$$

From $\dot{\sigma} = (2\dot{\sigma}_r - \dot{s})/3$ and equations (24) and (25), it can be shown that
$$
\int_a^b \dot{\sigma}(r,t)\ r\ dr = 0,\ t \geq 0_* \tag{26}
$$

Also
$$
\int_a^r rac{\dot{e}}{r} dr = \int_a^r rac{(\dot{\epsilon}_r - \dot{\epsilon}_\theta)}{r} dr = \left[ rac{\dot{u}(r,t)}{r} - rac{\dot{u}(a,t)}{a} \right] \ (27)
$$

Using equations (21), (22), (26), and (27), one may solve for $\dot{u}(a, t)$ to obtain
$$
\begin{aligned}
\dot{u}(a,t) = rac{ab^2}{(b^2 - a^2)} \Bigg\{ rac{1}{b^2}&\int_a^b \left[2\alpha \dot{T} + (1 - g)\ \mu\sigma\right] r\ dr \
&- \int_a^b (1 - g)\ \mu rac{s}{r} dr \Bigg\} \ (28)
\end{aligned}
$$

From $\dot{\sigma} = (2\dot{\sigma}_r - \dot{s})/3$ and equation (23) and the use of the foregoing equations, after some manipulation and simplification, one can finally arrive at the following:
$$
\begin{aligned}
\dot{\sigma}(r,t) = rac{E}{3} \Bigg[ &rac{2\alpha}{(b^2 - a^2)}\int_a^b \dot{T}\ rdr \
&- \alpha \dot{T} + rac{1}{(b^2 - a^2)}\int_a^b (1 - g)\mu\sigma\ r\ dr \
&- rac{b^2}{(b^2 - a^2)}\int_a^b (1 - g)\mu rac{s}{r} dr \
&+ \int_a^r (1 - g)\mu rac{s}{r} dr - rac{(1 - g)}{2} \mu(\sigma - s) \Bigg],
\end{aligned}
$$

$$
\begin{aligned}
\dot{s}(r,t) = E\Bigg[ &- rac{2\alpha\ a^2}{(b^2 - a^2)r^2} \int_a^b \dot{T}\ r\ dr \
&- rac{2\alpha}{r^2} \int_a^r \dot{T}\ r\ dr + \alpha \dot{T} - rac{a^2}{(b^2 - a^2)r^2} \
&	imes \int_a^b (1 - g)\mu\sigma\ r\ dr + rac{a^2b^2}{(b^2 - a^2)r^2} \int_a^b (1 - g)\mu rac{s}{r}dr
\end{aligned}
$$
(29)

---

Journal of Applied Mechanics
MARCH 1976 / 119

![](./images/811712958550769666_2.jpg)

$$
\left. -\frac{1}{r^{2}} \int_{a}^{r}(1-g) \mu \sigma r\ d r+\frac{(1-g)}{2} \mu(\sigma-s)\right],
$$

$$
\text{for } 0_{+} \leqq t<\infty,\ a \leqq r \leqq b \tag{29}
$$
(Cont.)

Equation (14) may be written in the form of initial conditions on $\sigma$ and $s$ as

$$
\sigma(r, 0)=0=s(r, 0), \quad a \leqq r \leqq b \tag{30}
$$

From $\dot{\sigma}_{r}=(3 \dot{\sigma}+\dot{s}) / 2$ it is clear that equation (29) satisfies

$$
\left.\dot{\sigma}_{r}(r, t)\right|_{r=a}=0=\left.\dot{\sigma}_{r}(r, t)\right|_{r=b}, \quad t \geqq 0_{+}
$$

which, in view of equation (14), insure that equation (15) is satisfied.

It thus remains to determine $\sigma(r, t)$ and $s(r, t)$, for $a \leqq r \leqq b$, $0<t<\infty$, from equations (29), (17)-(19), and (5)-(12) subject to the initial conditions of equation (30). Analytical integration of the foregoing equations is not possible and a scheme involving iteration and numerical integration is clearly necessary.

### Numerical Computations
For any interval of time $(t', t'')$ during which the thermoelastic equations govern the state of stress in the disk, one has, from equation (29) (since $g=1$),

$$
\left. \begin{aligned}
\sigma(r, t)-\sigma(r, t') & \\
& =\frac{E}{3}\left\{\frac{2 \alpha}{\left(b^{2}-a^{2}\right)} \int_{a}^{b} \Delta T r\ d r-\alpha\ \Delta T\right\}, \\
s(r, t)-s(r, t') & \\
& =E\left\{-\frac{2 \alpha}{\left(b^{2}-a^{2}\right)} \frac{a^{2}}{r^{2}} \int_{a}^{b} \Delta T r\ d r\right. \\
& \left.\quad \quad -\frac{2 \alpha}{r^{2}} \int_{a}^{b} \Delta T r\ d r+\alpha\ \Delta T\right\}, \\
& \quad \quad \quad a \leqq r \leqq b,\ t' \leqq t \leqq t''
\end{aligned} \right\} \tag{31}
$$

where $\Delta T=T(r, t)-T(r, t')$. There are two such intervals, $(0, t_{2})$ and $(t_{3}, \infty)$, where $t_{2}$ is the instant at which plastic yielding in the disk commences during thermal shock and $t_{3}$ is the instant at which plastic yielding in the disk ceases following the thermal shock, assuming, of course, that no further plastic yielding occurs under the developing residual stresses. The stress distribution during the interval $(0, t_{2})$ is readily given by equations (31) and (5)-(12) in view of equation (30). For the interval $(t_{3}, \infty)$, however, one needs, in addition, the stress distributions $\sigma(r, t_{3})$ and $s(r, t_{3})$ for $a \leqq r \leqq b$. These may be obtained from equations (29), (17)-(19), and (5)-(12) on using a numerical technique incorporating an iteration procedure and numerical integration; a listing of a computer code for carrying out the same has been provided in [5] along with a flow chart and detailed description.

![](./images/811712958550769666_3.jpg)

![](./images/811712958550769666_4.jpg)

In carrying out the numerical technique, the first step is to select a sufficiently large number of equidistant stations on the radius of the disk and also a sufficiently small time step $\Delta t$. Starting from the instant $t=t_{2}$, progress is made in steps of $\Delta t$ in time till the instant $t=t_{3}$ is reached and identified. At each step in the interval $[t_{2}, t_{3}]$, the correct values for $g, \mu, \dot{\sigma}$, and $\dot{s}$ for all the stations on the radius are determined by iteration from equations (29), (17)-(19), and (5)-(12) where the integrals involving $\dot{T}$ in the integrands are evaluated analytically [5] and those involving $\mu$ in the integrands are evaluated by the trapezoidal rule. Using the values of the final iteration for $g, \mu, \dot{\sigma}$ and $\dot{s}$ for each of the stations on the radius, for the current instant $t$, the values of $\sigma$ and $s$ for all the stations for the subsequent instant $t+\Delta t$ are then evaluated as

---

120 / MARCH 1976
Transactions of the ASME

![](./images/811712958550769666_5.jpg)

Fig. 5 Residual tangential stress distributions, having $\sigma_{\theta \theta}^{res}/\sigma_{ys}|_{r=a} = -0.41$ resulting from thermal shocks of suitable strengths and varying width

![](./images/811712958550769666_6.jpg)

Fig. 6 Thermal shock strength and maximum tangential residual tensile stress versus width of heating zone, from Fig. 4

![](./images/811712958550769666_7.jpg)

Fig. 7 Thermal shock strength and maximum tangential residual tensile stress versus width of heating zone, from Fig. 5

![](./images/811712958550769666_8.jpg)

Fig. 8 Tangential stress distribution in a strip with a hole, under combined (longitudinal tensile and residual) loading at impending plastic yielding at the rim of the hole, along the diametrical line perpendicular to the longitudinal tensile load

$\sigma(r, t + \Delta t) = \sigma(r, t) + \dot{\sigma}(r, t)\Delta t$ and $s(r, t + \Delta t) = s(r, t) + \dot{s}(r, t)\Delta t$ except for those stations having $J_2(r, t + \Delta t) > \sigma_{ys}^2$ when $J_2$ is evaluated from the foregoing through equation (18), in which case, a multiplicative correction factor of $\sigma_{ys}/\sqrt{J_2(r, t + \Delta t)}$ on the values of $\sigma(r, t + \Delta t)$ and $s(r, t + \Delta t)$ evaluated as in the foregoing is used for such stations. The residual stress distribution may be obtained from equations (31) and (5)-(12), once $t_3$, $\sigma(r, t_3)$, and $s(r, t_3)$ have been determined as just outlined briefly, on taking the time variable $t$ to infinity, i.e., by using the steady-state temperature value for evaluating $\Delta T$.

## Numerical Illustration and Discussion
An aluminum disk of dimensions $a = 1.6$ mm, $b = 12.7$ mm, and $w = 1$ mm, having the following material properties, is considered

$$
\begin{align*}
k &= 6230.3 \text{ joules/hr cm } ^\circ\text{C}; \\
\alpha &= 0.1692 \times 10^{-4} \text{ cm/cm } ^\circ\text{C}; \\
E &= 8.964 \times 10^6 \text{ Newtons/cm}^2; \\
\kappa &= 0.64516 \text{ cm}^2/\text{sec}; \\
\nu &= 0.3 \\
h_1 &= h_2 = h = 10.22 \text{ joules/hr cm}^2 \, ^\circ\text{C} \text{ (arbitrarily assigned small value)} \\
\sigma_{ys} &= 13790.6 \text{ Newtons/cm}^2
\end{align*}
$$

It should be noted that the yield strength is taken as temperature independent for the purpose of numerical illustration.

The duration $t_1$ of the thermal shock is taken as $1.5 \times 10^{-3}$ sec and varying strengths and widths (zonal) of thermal shock are considered at two locations of the disk separately. Fig. 2 shows the stress distributions in the disk at three instants of time under thermal shock in one such case. Fig. 3 shows the residual stress distributions following thermal shock at the same location and of the same width but differing in strength in three independent cases. In Figs. 4 and 5 are presented the residual tangential stress distributions, having the same magnitude at the rim of the hole, resulting from thermal shock applied at the respective two locations and differing in strength and width in independent cases at each location. Replotting of Figs. 4 and 5 as shown in Figs. 6 and 7 reveals that of the two locations considered, the one nearer the hole having $a_1/b =$

---
Journal of Applied Mechanics
MARCH 1976 / 121

![](./images/811712958550769666_9.jpg)

Fig. 9 Tangential stress distribution in a strip with a hole, under combined (longitudinal tensile and residual) loading at impending plastic yielding at the rim of the hole, along the diametrical line perpendicular to the longitudi- nal tensile load

![](./images/811712958550769666_10.jpg)

Fig. 10 Some results for $a_{1} / b=0.25$ for varying shock zone widths for simultaneous impending plastic yielding at $r=a$ and at the interior point of peak tensile stress in a strip with a hole under combined (longitudinal ten- sile and residual) loading

0.25 leads to the minimum peak residual tangential tensile stress for a thermal shock width of $(b_{1}-a_{1}) / b=0.2375$

For an illustration of the advantage of this type of treatment to metals, consider a long sheet metal strip, as shown in Fig. 1, of width $2 b$ and thickness $w$ and with a hole of radius $a$, subjected to an uniform longitudinal plane tensile stress $S$. The stress distribu- tion in the neighborhood of the hole may be assessed by that in an infinite plate with a hole of radius $a$, subjected to an uniform uni- axial plane tensile stress $S$ and may be obtained from the formula given in reference [6]. The stress distribution in the strip on the di- ametrical line perpendicular to $S$ is then given by

$$
\begin{aligned}
\frac{\sigma_{\theta}}{S}=\frac{1}{2}\left(2+\frac{a^{2}}{r^{2}}+\frac{3 a^{4}}{r^{4}}\right) ; \\
\frac{\sigma_{r}}{S}=\frac{3}{2} \frac{a^{2}}{r^{2}}\left(1-\frac{a^{2}}{r^{2}}\right) ; \tau_{r \theta}=0 \quad(32)
\end{aligned}
$$

![](./images/811712958550769666_11.jpg)

Fig. 11 Some results for $a_{1} / b=0.25$ for varying shock zone widths for simultaneous impending plastic yielding at $r=a$ and at the interior point of peak tensile stress in a strip with a hole under combined (longitudinal ten- sile and residual) loading

For impending plastic yielding at $r=a$, the stress-concentration factor of 3 at the rim of the hole limits $S$ to $S / \sigma_{y s}=0.577$. How ever, superimposition of the residual stresses corresponding to the case with $a_{1} / b=0.25$ and $(b_{1}-a_{1}) / b=0.2375$ and having $\left.\sigma_{\theta}^{\text {res }} / \sigma_{y s}\right|_{r=a}=-0.41$ on the stress distribution of equation (32) permits $S$ to be raised to $S / \sigma_{y s}=0.714$ for impending subsequent plastic yielding at $r=a$. The combined tangential stress distribu- tion and $\sqrt{J_{2}}$ distribution under such superimposed conditions is presented in Fig. 8 from which it is clear that there is still scope for raising $S$ further. The maximum value of $S$ thus attainable is $S / \sigma_{y s}$= 0.77 as shown in Fig. 9 where there is simultaneous impending plastic yielding at both the rim of the hole and the interior point of the disk where the combined tangential tensile stress has a peak, thus permitting a maximum improvement of 33.44 percent over an untreated sheet metal strip with a hole. Figs. 10 and 11 present some results for thermal shocks of $a_{1} / b=0.25$ and of varying widths and suitable strengths such that the maximum applicable longitudinal tensile stress $S$ causes, in each case, impending plastic yielding at both $r=a$ and the interior point of peak tangential ten sile stress under superimposed loading. From Fig. 11, it is seen that while there is some improvement in the maximum applicable ten-sile stress for $(b_{1}-a_{1}) / b=0.2375$ over that for $(b_{1}-a_{1}) / b=$


0.125, the energy of the thermal shock required is more than dou- bled.

It is plausible that a further increase of the maximum applicable tensile stress $S$ for impending plastic yielding in the sheet metal strip can be obtained by using more than one thermal shock on the same specimen at separate locations in order to reduce the peak tangential tensile residual stress for a given tangential compressive residual stress at the rim of the hole. A more thorough experimen- tal investigation than that of [1] is continuing at the authors' labo- ratory.

## Acknowledgment
The authors wish to acknowledge the financial support of this work by the National Research Council of Canada under Grant No. A8276, and by the Defence Research Board under Grant No.9761-05.

## References
1 Hsu, T. R., "Application of the Laser Beam Technique to the Im- provement of Metal Strength," *Journal of Testing and Evaluation*, ASTM, Vol. 1, No. 6, 1973, pp. 457-458.
2 Özisik, M. N., *Boundary-Value Problems of Heat Conduction*, Inter- national Textbook Co., Scranton, Pa., 1968.
3 Boley, B. A., and Weiner, J. H., *Theory of Thermal Stresses*, Wiley, New York, 1967.
4 Landau, H. G., and Zwicky, E. E., Jr., "Transient and Residual Ther- mal Stresses in an Elastic-Plastic Cylinder," JOURNAL OF APPLIED ME- CHANICS, Vol. 27, No. 3, TRANS. ASME, Vol. 82, Series E, Sept. 1960, pp.481-488.
5 Trasi, S. R., and Hsu, T. R., "Nonstationary Quasistatic Thermoelas- toplastic Stress Analysis of a Disk Subjected to Thermal Shock," Report No.75-3, May 1975, Thermomechanics and Composite Structures Laboratory, Department of Mechanical Engineering, University of Manitoba, Winnipeg, Manitoba, Canada.
6 Timoshenko, S. P., and Goodier, J. N., *Theory of Elasticity*, McGraw- Hill, New York, 3rd ed., 1970, p. 91.

---

Journal of Applied Mechanics
MARCH 1976 / 123