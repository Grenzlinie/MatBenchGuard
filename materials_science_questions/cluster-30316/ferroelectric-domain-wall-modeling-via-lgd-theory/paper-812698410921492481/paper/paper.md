# Activation Energy of Ferroelectric Domain Wall

Yoshihiro Ishibashi¹ and Makoto Iwata²

¹Department of Applied Physics, Nagoya University, Nagoya 464-8603, Japan
²Department of Physical Science and Engineering, Nagoya Institute of Technology, Nagoya 466-8555, Japan

(Received October 26, 2018; accepted November 7, 2019; published online December 18, 2019)

Three important elements of the ferroelectric domain wall, i.e., the polarization profile in the vicinity of the domain wall, the domain wall energy, and the activation energy, are theoretically studied on the basis of continuum and discrete models. The domain wall in ferroelectrics undergoing the second-order phase transition, to which the $p^4$ potential is applicable, is revisited. For ferroelectrics undergoing the first-order phase transition, to which the $p^6$ potential is applicable, newly obtained results, such as simple closed expressions for the domain wall and activation energies, are presented in a manner convenient for comparison with the $p^4$ potential case. The detailed calculation of the activation energy in the $p^6$ potential case is shown, and it is found that, unlike in the $p^4$ potential case, it includes an oscillating factor originating from the poles located off the imaginary axis in the complex function of the local energy density.

## 1. Introduction

In ferroelectrics, domains and domain walls necessarily exist, and in the domain wall, the polarization changes gradually as a function of the distance from the center of the wall. This sort of phenomenon, i.e., the spatial change of some characteristic physical quantity, is common to various systems with transition layers, such as dislocations in metals¹⁻⁴) and melt-solid interfaces.⁵⁻¹⁰)

Regarding these transition layers, there are three sub-stantial elements: the profile of the spatial change of the characteristic physical quantity in the vicinity of the transition layer, the energy needed to form such transition layer, and the activation energy (or force) needed to displace such a transition layer (the activation energy here corresponds to the Peierls energy in the dislocation theory¹¹) or the pinning energy due to the discreteness of the lattice). Hereafter, we use the words "domain wall", and not "transition layer", which may have a more general meaning, since in this paper, we focus on ferroelectric domain walls.

The above three physical elements concerning the domain wall are investigated, usually using some continuum model expressed with an energy function, which consists of the local energy and the one originating from the spatial inhomogeneity in polarization. In the case of ferroelectrics, the energy function frequently used has a simple double minimum potential form (hereafter called the $p^4$ potential), which applies to ferroelectrics undergoing the second order phase transition, and the conclusions obtained from such a model are fairly well understood.⁵,¹²) However, many ferroelectrics undergo the first-order transition, and their domain walls have to be discussed with the $p^6$ potential. Some of the characteristic features of domain walls, which are different from the second-order transition case, may be known, but, generally speaking, it does not appear that the theory of ferroelectric domain walls in this case is well established.¹³⁻¹⁵) Given this situation, in this paper, emphasis will be partly placed on the properties of domain walls in the first-order transition case (the $p^6$ potential case), while those problems in the second-order transition case (the $p^4$ potential case) will be revisited.

On the other hand, it is considered that in ferroelectrics, the domain walls are usually thin because of strong anisotropy in ferroelectric crystals, regardless of the order of the phase transitions. It is questionable, therefore, whether the contin-uum model mentioned earlier is applicable. Given this situation, it is desirable to resort to the discrete model, but as a drawback of the discrete model, we have to rely on numerical computations, and it may not be easy to obtain an analytical prospect only from such numerical calculations. Therefore, it will make sense to discuss the ferroelectric domain walls in parallel, using both the continuum and discrete models.

Lastly, it should be pointed out that the activation energy in ferroelectrics has been less studied, compared with the two other elements, i.e., the polarization profile and the domain wall energy. In fact, even if the actual ferroelectric domain walls are strongly pinned to a certain site by crystal defects such as dislocations and imperfections, the activation energy due to the discreteness of the crystal lattice is very small, as discussed below. Therefore, it seems to be purely of some theoretical interest from a quantitative viewpoint. Although it may be so, we consider that it is worth obtaining the activation energy in a closed form to clarify its qualitative features. This problem was previously solved for the second-order transition case,⁵,¹²) but not for the first-order transition case in a systematic manner. In addition, regarding the activation energy previously presented¹³,¹⁴) for the latter case, its pre-exponential factor estimated by the saddle point method of the contour integral was found to be less accurate than that obtained by the current residue calculation. Thus, it is partly our purpose to obtain a more accurate formula for it in this paper.

Taking into account this situation regarding the present theoretical understanding of ferroelectric domain walls, we put emphasis on the activation energy, as can be understood from the title of this paper, which is organized as follows. In Sect. 2, the general view on the domain walls will be presented by using the $p^4$ and $p^6$ potentials, and in Sect. 3, the analytical method of estimating the activation energy will be presented. The final section will be devoted to discussion. Brief comments on the relationship between the activation energy and the numerical evaluation of an integral,¹⁶) which will become clear in the course of the theoretical derivation of the activation energy, will be presented in Appendix.

## 2. Domain Wall Energy in Ferroelectrics

### 2.1 Second-order transition case revisited ($p^4$ potential)
Firstly, we consider the continuous case. The local energy $f$

J. Phys. Soc. Jpn. **89**, 014705 (2020)
Y. Ishibashi and M. Iwata

of the homogeneous part in the domains far from the wall is
written in terms of the polarization $p$ at site $x$ as

$$
f = \frac{\alpha}{2} p^{2} + \frac{\beta}{4} p^{4} + \frac{\kappa}{2} \left( \frac{\mathrm{d}p}{\mathrm{d}x} \right)^{2}, \quad (\alpha < 0,\ \beta > 0,\ \kappa > 0), \quad (1)
$$

where the last term on the right-hand side (rhs) is the increase
in energy due to inhomogeneity in the polarization
distribution. The total energy $F$ is expressed as

$$
F = \int_{-\infty}^{\infty} [f(p(x)) - f_{0}] \mathrm{d}x, \tag{2}
$$

where $f_{0} = -\alpha^{2}/4\beta$ is the energy far from the wall. To
minimize $F$, we have to solve the Euler–Lagrange equation

$$
\alpha p + \beta p^{3} - \kappa \frac{\mathrm{d}^{2}p}{\mathrm{d}x^{2}} = 0 \tag{3}
$$

under the boundary conditions

$$
p = \pm p_{\mathrm{s}},\quad \frac{\mathrm{d}p}{\mathrm{d}x} = 0,\quad \text{at}\quad x = \pm\infty, \tag{4}
$$

where $p_{\mathrm{s}} = \sqrt{-\alpha/\beta}$. As a result, the integral is obtained as

$$
\frac{\kappa}{2} \left( \frac{\mathrm{d}p}{\mathrm{d}x} \right)^{2} = \frac{\beta}{4} (p^{2} - p_{\mathrm{s}}^{2})^{2}, \tag{5}
$$

from which the polarization profile is given as

$$
p = p_{\mathrm{s}} \tanh Kx, \tag{6}
$$

where $K = \sqrt{-\alpha/2\kappa}$. The energy distribution is also given as

$$
f(p(x)) - f_{0} = \kappa K^{2} p_{\mathrm{s}}^{2} \mathrm{sech}^{4} Kx, \tag{7}
$$

as shown in Fig. 1. It is needless to say that the energy is
concentrated in the wall, and the domain wall energy $W$,
which is the energy needed to create one domain wall, is
given as

$$
W = \kappa K^{2} p_{\mathrm{s}}^{2} \int_{-\infty}^{\infty} \mathrm{sech}^{4} Kx \mathrm{d}x = \frac{4}{3} \kappa K p_{\mathrm{s}}^{2} = \frac{2}{3\beta} \sqrt{-2\kappa\alpha^{3}}. \tag{8}
$$

![](./images/812698410921492481_1.jpg)

Fig. 1. (Color online) Polarization profile [Eq. (6)] and distribution of
energy [Eq. (7)] in the vicinity of the domain wall determined using the $p^{4}$
potential model. The adopted parameter values are $\alpha = -1$, $\beta = 1$, and
$\kappa = 4$, so $K = 1/\sqrt{8}$.

Next, we consider the discrete case. In this case, the
differentiation is replaced with the difference and the integral
with the summation. Namely, we have to minimize the total
energy

$$
\begin{aligned}
F = a \sum_{n} &\left[ \frac{\alpha}{2} p_{n}^{2} + \frac{\beta}{4} p_{n}^{4} + \frac{\kappa}{2a^{2}} (p_{n} - p_{n-1})^{2} \right. \\
& \left. - \left( \frac{\alpha}{2} p_{\mathrm{s}}^{2} + \frac{\beta}{4} p_{\mathrm{s}}^{4} \right) \right]
\end{aligned} \tag{9}
$$

and the difference equation, corresponding to the Euler–
Lagrange equation, is written as

$$
\alpha p_{n} + \beta p_{n}^{3} - \frac{\kappa}{a^{2}} (p_{n+1} - 2p_{n} + p_{n-1}) = 0, \tag{10}
$$

where $a$ is the lattice constant, which is fixed in the present
model and should not be varied. The boundary conditions at
$x = \pm\infty$ are the same as in the continuous case, but in contrast
to the continuous case, in the discrete case, there are two types
of solution, one being the on-site solution (odd type),
(i) $p_{n} = -p_{-n}$ (therefore, $p_{0} = 0$, the center of the wall
coinciding with the lattice point), and the other, the off-site
solution (even type),
(ii) $p_{n} = -p_{-n+1}$ (therefore, $p_{0} = -p_{1}$, the center of the wall
being located at the midpoint of two lattice points).

![](./images/812698410921492481_2.jpg)

Fig. 2. (Color online) Polarization profiles of on-site and off-site walls
determined using the discrete model. The adopted parameter values are
$\alpha = -1$, $\beta = 1$, $\kappa = 1/2$, and $a = 1$, so $K = 1$.

Note that, in these two solutions, the center of the wall is
displaced by $a/2$ relative to each other.

In the discrete case, we have to resort to numerical
calculations since no exact solution is known for Eq. (10).
Without concrete calculations, the effect of discreteness will
appear most clearly in the case of thin walls. Namely, when $K$
in Eq. (6) is small, i.e., the wall is thick, the two profiles are
almost the same, and when $K$ is large, i.e., the wall is thin, the
two profiles differ noticeably. As an example of a thin wall,
two profiles are shown in Fig. 2 for the parameter values
$\alpha = -1$, $\beta = 1$, $\kappa = 0.5$ (so $K = 1$), and $a = 1$.

Reflecting the difference in the profiles, the wall energies
corresponding to the on-site and off-site solutions must differ
noticeably when a wall is thin, but the difference will be
small when a wall is thick. For the case shown in Fig. 2,
as the wall energy, $W$ (on-site) $= 0.6508$ and $W$ (off-site) $=$
$0.6284$ are obtained. Note that both $W$ (on-site) and $W$ (off-
site) are smaller than $W = 0.667$ given by Eq. (8), because
there are more adjustable parameters (all $p_{n}$) in the discrete
case than in the continuum case (only $K$). Moreover, these
energies must be the same even if each wall is displaced by
one lattice period, and this situation is schematically shown

014705-2
©2020 The Physical Society of Japan

![](./images/812698410921492481_3.jpg)

Fig. 3. (Color online) Periodic variation of wall energy.

in Fig. 3. As is easily understood, the difference between two wall energies, $\Delta W = W$ (on-site) $- W$ (off-site), is the activation energy needed to displace the wall by one lattice period and then further. In the case shown in Fig. 2, $\Delta W = 0.0224$. It is known that $\Delta W > 0$ in the $p^4$ potential case, implying that the off-site solution always corresponds to the lower wall energy (see below).$^{5,12)}$

### 2.2 First-order transition case ($p^6$ potential)
Firstly, we consider the continuous case. The local energy function $f$ at site $x$ is given as
$$
\begin{aligned}
f &= \frac{\alpha}{2} p^{2}+\frac{\beta}{4} p^{4}+\frac{\gamma}{6} p^{6}+\frac{\kappa}{2}\left(\frac{\mathrm{d} p}{\mathrm{~d} x}\right)^{2}, \\
& \left(\alpha<\frac{3 \beta^{2}}{16 \gamma}, \beta<0, \gamma>0, \kappa>0\right).
\end{aligned}
\tag{11}
$$

Following a similar process to that described above and using the equilibrium condition for $p_{\mathrm{s}}$, i.e.,
$$
\alpha+\beta p_{\mathrm{s}}^{2}+\gamma p_{\mathrm{s}}^{4}=0,
\tag{12}
$$
we obtain an equation that
$$
\begin{aligned}
\frac{\kappa}{2}\left(\frac{\mathrm{d} p}{\mathrm{~d} x}\right)^{2} &=\frac{\alpha}{2}\left(p^{2}-p_{\mathrm{s}}^{2}\right)+\frac{\beta}{4}\left(p^{4}-p_{\mathrm{s}}^{4}\right)+\frac{\gamma}{6}\left(p^{6}-p_{\mathrm{s}}^{6}\right) \\
&=\left(p^{2}-p_{\mathrm{s}}^{2}\right)^{2}\left[\frac{\beta}{4}+\frac{\gamma}{6}\left(p^{2}+2 p_{\mathrm{s}}^{2}\right)\right],
\end{aligned}
\tag{13}
$$
where $p_{\mathrm{s}}=\left[\left(-\beta+\sqrt{\beta^{2}-4 \alpha \gamma}\right) / 2 \gamma\right]^{1 / 2}$ is the polarization at $x=\infty$. As the result, the polarization profile is given as
$$
p=p_{\mathrm{s}} \cdot \frac{\sinh K x}{\sqrt{b+\cosh ^{2} K x}},
\tag{14}
$$
where
$$
\begin{aligned}
& K=\sqrt{\frac{\beta+2 \gamma p_{\mathrm{s}}^{2}}{2 \kappa}} p_{\mathrm{s}} \leq \sqrt{\frac{\gamma}{\kappa}} p_{\mathrm{s}}^{2}, \\
& b=\frac{2 \gamma p_{\mathrm{s}}^{2}}{3 \beta+4 \gamma p_{\mathrm{s}}^{2}}=\frac{1}{2} \cdot \frac{p_{\mathrm{s}}^{2}}{p_{\mathrm{s}}^{2}-p_{\mathrm{c}}^{2}} \geq \frac{1}{2}
\end{aligned}
\tag{15}
$$
with $p_{\mathrm{c}}^{2}=-3 \beta / 4 \gamma$ being the squared polarization at the first-order transition temperature $\alpha_{\mathrm{c}}=3 \beta^{2} / 16 \gamma$. Using the profile of the polarization distribution, Eq. (14), we can obtain the energy distribution around the domain wall as
$$
f(p(x))-f_{0}=\kappa K^{2} p_{\mathrm{s}}^{2}(1+b)^{2} \frac{\cosh ^{2} K x}{\left(b+\cosh ^{2} K x\right)^{3}}.
\tag{16}
$$

![](./images/812698410921492481_4.jpg)

Fig. 4. (Color online) Polarization profiles [Eq. (14)] and distribution of energy [Eq. (16)] in the vicinity of the domain wall determined using the $p^6$ potential model. The adopted parameter values are $\beta=-1, \gamma=1$, and $\kappa=1$. (a) High temperature: $\alpha=0.18>0$, and (b) low temperature: $\alpha=-1<0$.

Note that when $b=0$, Eq. (16) is reduced to Eq. (7). In the first-order transition case ($p^6$ potential), there are two places, symmetrically displaced from the center, where the energy is high when $\alpha>0$, and they merge into one with decreasing temperature in $\alpha<0$ [Figs. 4(a) and 4(b)]. The wall energy is given by the integration of Eq. (16) as
$$
W=\frac{\kappa K p_{\mathrm{s}}^{2}}{4 b}\left[2 b-1-\frac{4 b+1}{\sqrt{b(b+1)}} \ln (\sqrt{1+b}-\sqrt{b})\right], \quad(17)
$$
which is shown as a function of $b$ in Fig. 5. Note that $W$ in Eq. (17) approaches the value given by Eq. (8) for the case of the second-order transition with $b$ approaching zero, although the value of $b$ here is limited to $b>1 / 2$ as shown in Eq. (15).

Next, we move on to the discrete case. In this case, the differentiation is replaced with the difference and the integral with summation. Namely, we have to minimize the total energy
$$
\begin{aligned}
F= & a \sum_{n}\left[\frac{\alpha}{2} p_{n}^{2}+\frac{\beta}{4} p_{n}^{4}+\frac{\gamma}{6} p_{n}^{6}+\frac{\kappa}{2 a^{2}}\left(p_{n}-p_{n-1}\right)^{2}\right. \\
& \left.-\left(\frac{\alpha}{2} p_{\mathrm{s}}^{2}+\frac{\beta}{4} p_{\mathrm{s}}^{4}+\frac{\gamma}{6} p_{\mathrm{s}}^{6}\right)\right],
\end{aligned}
\tag{18}
$$
and the difference equation, corresponding to the Euler-Lagrange equation, is written as

![](./images/812698410921492481_5.jpg)

Fig. 5. Wall energy as a function of $b$ [Eq. (17)]. $\kappa K p_{s}^{2}=1$.

$$
\alpha p_{n}+\beta p_{n}^{3}+\gamma p_{n}^{5}-\frac{\kappa}{a^{2}}\left(p_{n+1}-2 p_{n}+p_{n-1}\right)=0. \tag{19}
$$

The situation regarding the solution of these difference equations is the same as the second order transition case, i.e., there are two types of solution, one being the on-site solution (odd type) and the other the off-site solution (even type), where in the former, the center of the domain wall coincides with a lattice point, and in the latter, it is located at the midpoint between two lattice points.

Now, the difference between the continuum and discrete models appears more clearly when the wall is thin. We present, as an example, the polarization profiles of the on-site and off-site walls numerically obtained for two cases, i.e., a thick wall and a thin wall. The parameter values commonly adopted are $\alpha=-1, \beta=-1$, and $\gamma=1$, and so the thickness of the wall depends only on the parameter $\kappa$. For the thick wall, we put $\kappa=4$, so $K=0.9256$, and $b=0.7741$ [Fig. 6(a)], and for the thin wall, we put $\kappa=0.5$, so $K=2.6180$, and $b=0.7741$ [Fig. 6(b)]. When the wall is thick, the profiles of the on-site and off-site walls appear to be almost the same at a glance; nevertheless, the wall energies are slightly different, i.e., $W$ (on-site) $=4.4951$ and $W$ (off-site) $=4.4945$, and they are both found to be smaller than $W=4.5329$ given by the continuum model [see Eq. (18)]. The activation energy $\Delta W=W$ (on-site) $-$ $W$ (off-site) in this case is given as $\Delta W=0.0006>0$. On the other hand, when the wall is thin, the profiles of the on-site and off-site walls are considerably different, and so are the wall energies, i.e., $W$ (on-site) $=1.5107$ and $W$ (off-site) $=1.3770$, and they are both found to be smaller than $W=1.6026$ given by the continuum model [see Eq. (18)]. The activation energy $\Delta W=W$ (on-site) $-$ $W$ (off-site) in this case is given as $\Delta W=0.1337$. Under the adopted model parameters here, $\Delta W$ happens to be positive, but in general, in the case of the $p^{6}$ potential, the sign of $\Delta W$ depends on the parameter values $\alpha, \beta, \gamma$, and $\kappa$ (see below).

### 3. Activation Energy of Thick Ferroelectric Domain Walls

Thus far, the activation energy has been obtained only in the discrete case and not in the continuous case. Note that the activation energy is strongly dependent on the difference in the polarization profiles of the on-site and off-site walls.

![](./images/812698410921492481_6.jpg)

Fig. 6. (Color online) Polarization profiles of on-site and off-site walls in low temperature, where the domain wall is thin, as determined using the continuum model. The adopted parameter values are $\alpha=-1, \beta=-1, \gamma=1$, and $a=1$. (a) Thick wall: $\kappa=4$, and (b) thin wall: $\kappa=1/2$.

However, in the continuous case, unlike in the discrete case, the polarization profiles of both walls are the same as given in Eqs. (6) and (16) for the second- and first-order transition cases, respectively. Therefore, at a glance, it may seem that there is no activation energy. Nevertheless, it is possible to obtain the finite activation energy on the basis of Eq. (7) or (14).

In this section, we first show the mathematical method and attempt to obtain the activation energy for both cases of the second- and first-order transitions. For this purpose, the use of the Poisson sum formula appears to be simple and clear as mentioned by Cahn. $^{5)}$ The Poisson sum formula enables us to sum the values at periodic intervals of a function of a continuous variable as

$$
a \sum_{n=-\infty}^{\infty} f(n a)=\sum_{s=-\infty}^{\infty} \int_{-\infty}^{\infty} f(z) \cos \frac{2 \pi s z}{a} \mathrm{~d} z. \tag{20}
$$

Since the sum on the rhs converges rapidly as can be seen from the discussion below, we take only two leading terms ($s=0,1$) on the rhs, i.e.,

$$
a \sum_{n=-\infty}^{\infty} f(n a) \cong \int_{-\infty}^{\infty} f(z) \mathrm{d} z+2 \int_{-\infty}^{\infty} f(z) \cos \frac{2 \pi z}{a} \mathrm{~d} z. \tag{21}
$$

Then, the meaning of the Poisson sum formula becomes clear, namely, the cosine transform of $f$ indicates the error in the numerical evaluation based on the trapezoidal sum rule of

an integral of the function $f$ with a continuous variable. In the Poisson sum formula, we can displace the position of the evaluation of $f$ by $\delta$, i.e.,

$$
\begin{aligned}
a \sum_{n=-\infty}^{\infty} & f(n a-\delta) \\
& \cong \int_{-\infty}^{\infty} f(z-\delta) \mathrm{d} z+2 \int_{-\infty}^{\infty} f(z-\delta) \cos \frac{2 \pi z}{a} \mathrm{~d} z \\
& =\int_{-\infty}^{\infty} f(z) \mathrm{d} z \\
& \quad+2 \int_{-\infty}^{\infty} f(z)\left[\cos \frac{2 \pi z}{a} \cos \frac{2 \pi \delta}{a}-\sin \frac{2 \pi z}{a} \sin \frac{2 \pi \delta}{a}\right] \mathrm{d} z.
\end{aligned}
$$

In the off-site solution, $\delta$ is $a / 2$, so the sine transform of $f$ is not needed, and it becomes clear that the activation energy of the domain walls can be obtained by the cosine transform of the local energy density $f[p(x)]-f_{0}$ in Eqs. (7) and (16) for the second- and first-order transition cases, respectively.

### 3.1 Second-order transition case revisited ($p^4$ potential)
Here, using the energy distribution in the continuum case, i.e., the rhs of Eq. (7), we calculate

$$
\Delta W=4 \kappa K^{2} p_{\mathrm{s}}^{2} \int_{-\infty}^{\infty} \operatorname{sech}^{4} K x \cos \frac{2 \pi x}{a} \mathrm{~d} x,
$$

where the prefactor 4 comes from $2[1-\cos (\pi)]$ [see Eqs. (21) and (22)]. On putting $z=K x$ and $\lambda=2 \pi / K a$, Eq. (23) is reduced to a contour integral on the complex plane $z$ using the integration path shown in Fig. 7, where the pole in the integrand is located at $z=\pi \mathrm{i} / 2$ on the imaginary axis. By the residue calculation, the activation energy $\Delta W$ is finally obtained as

$$
\Delta W=4 \kappa K p_{\mathrm{s}}^{2} \cdot \frac{\pi}{3} \frac{\lambda^{3}+4 \lambda}{1-\mathrm{e}^{-\lambda \pi}} \mathrm{e}^{\frac{-\lambda \pi}{2}} \cong 4 \kappa K p_{\mathrm{s}}^{2} \cdot \frac{\pi}{3}\left(\frac{2 \pi}{K a}\right)^{3} \mathrm{e}^{\frac{-\pi^{2}}{K a}} .
$$

It can be seen that the activation energy is very small, i.e., on the order of $\exp \left(-\pi^{2} / K a\right)$, and decreases rapidly with increasing wall thickness. Numerically, $\Delta W / W$ is estimated to be about $4.5 \times 10^{-5}$ when $K a=1$.

### 3.2 First-order transition case ($p^6$ potential)
Here, using the energy distribution in the continuum case, i.e., the rhs of Eq. (16), we calculate

$$
\Delta W=4 \kappa K^{2} p_{\mathrm{s}}^{2}(1+b)^{2} \int_{-\infty}^{\infty} \frac{\cosh ^{2} K x}{\left(b+\cosh ^{2} K x\right)^{3}} \cos \frac{2 \pi x}{a} \mathrm{~d} x,
$$

which can be reduced to a contour integral using the integration path shown in Fig. 7. Note that, unlike in the second-order transition case [Eq. (23)], here, the poles $z_{\mathrm{A}}$ and $z_{\mathrm{B}}$ are located at

$$
z_{\mathrm{A}}=\frac{\pi}{2} \mathrm{i}+x_{\mathrm{p}},
$$

$$
z_{\mathrm{B}}=\frac{\pi}{2} \mathrm{i}-x_{\mathrm{p}},
$$

both being off the imaginary axis, where $x_{\mathrm{p}}=\operatorname{arcsinh} \sqrt{b}=$ $\ln (\sqrt{b}+\sqrt{1+b})$. After tedious residue calculation, we obtain the activation energy as

![](./images/812698410921492481_7.jpg)

Fig. 7. Contour of integration. The solid and open circles show the pole of Eq. (7) and that of Eq. (16), respectively.

$$
\begin{aligned}
\Delta W \cong & 4 \kappa K p_{\mathrm{s}}^{2} \mathrm{e}^{\frac{-\pi^{2}}{K a}} \\
& \times\left(-\frac{\pi}{4 b}\right)\left[(1-2 b) \lambda \cos \left(x_{\mathrm{p}} \lambda\right)\right. \\
& \left.-\frac{1+4 b+\lambda^{2} b(1+b)}{\sqrt{b(b+1)}} \sin \left(x_{\mathrm{p}} \lambda\right)\right] .
\end{aligned}
$$

Note that, unlike in the second order transition case ($p^4$ potential case), oscillating factors consisting of both the sine and cosine functions appear, as given in the brackets in Eq. (28), which clearly originate from the poles located off the imaginary axis. The activation energy thus obtained, therefore, may happen to be zero owing to the accidental cancellation of the cosine and sine terms. Note, however, that, even in such case, it does not mean that there is no potential barrier to displace the wall, because, in such a case, the next higher order cosine and sine transforms in Eq. (22) may give rise to a finite potential barrier on the order of $\exp \left(-2 \pi^{2} / K a\right)$, no matter how small it is.

## 4. Discussion
In this work, we have studied the ferroelectric domain wall problems theoretically based on the continuum and discrete models. Three important elements of the domain wall, i.e., the polarization profile in the vicinity of the domain wall, the domain wall energy, and the activation energy, are clarified. The domain wall in ferroelectrics undergoing the second- order phase transition, to which the $p^{4}$ potential is applicable,is revisited and the previous results are confirmed. $^{5,12)}$  Regarding ferroelectrics undergoing the first-order phase transition, to which the $p^{6}$ potential is applicable, some newly obtained results, such as closed expressions for the domain wall and activation energies, are presented. The analytical expression for the domain wall energy unfortunately appears too complicated to be of much help for quick understanding, but such an analytical expression is expected to be useful for further development of the related theory.

On the other hand, the activation energy obtained by using the $p^{6}$ potential is presented in a concrete closed form and will shed new light on several related problems. It includes an oscillating factor as a function of the wall site in the lattice, which originates from the poles in the local energy density function located off the imaginary axis. The relationship between the two topics, i.e., the activation energy and the error in the numerical integration, is mentioned in Appendix, although they may seem, at a glance, to have nothing to do with each other.

Finally, one more comment on the activation energy is worth mentioning here. The activation energy obtained in this

paper is that due to the discreteness of the crystal lattice, so it is expected to be much smaller than the energy actually needed to displace the ferroelectric domain wall, which is pinned by a very strong force due to various lattice defects. Moreover, the mathematical method adopted in this paper for deriving the activation energy is valid only for thick walls, where the continuum model works, although real ferroelectric domain walls are usually thin. Therefore, one may find the activation energy discussed above to be only of theoretical interest quantitatively when applied to real ferroelectric domains. Nevertheless, we consider that it is important to understand that there is always a set of three substantial elements characteristic to ferroelectric domain walls, and the activation energy is one of them, with the two others being the polarization profile and domain wall energy. The theoretical results presented are expected to be useful for studying not only the ferroelectric domain walls but also the transition layers in some other similar systems in gener-al.1–4,6–11,17,18

Acknowledgement The authors express their sincere gratitude to Professor Yukio Kaneda, Aichi Institute of Technology, for his support in mathematical problems.

### Appendix: Application to Numerical Evaluation of an Integral¹⁶⁾

As mentioned below Eq. (21), the activation energy corresponds to the error in the numerical evaluation of an integral of the function $f$ with a continuous variable. In the domain wall problems, the parameter $a$ is the given lattice constant, and is therefore fixed. However, in numerical integration, $a$ corresponds to the interval over which the function $f$ is evaluated, so it can be chosen so that the error in the numerical integration should be as small as possible.

For this, the interval $a$ usually must be sufficiently small. However, the smaller the $a$ the longer the computation time needed, so in general, the precision of the numerical integration and the computation time have a trade-off relationship.

Here, it should be especially noted that, in the error estimation, an oscillating factor appears, as seen in the curly brackets in Eq. (28), when the function $f$ has the poles located off the imaginary axis, and therefore, this oscillating pre-exponential factor can be made zero by choosing the interval $a$ properly. In such a case, the interval may not necessarily be small, but rather can be large to some extent. Therefore, one may be able to reduce the computation time by choosing properly a certain large interval for the evaluation of the function $f$ when the poles of $f$ are located off the imaginary axis.

1) J. Frenkel and T. Kontorova, J. Phys. USSR **1**, 139 (1939).
2) V. L. Indenbom, Sov. Phys. Crystallogr. **3**, 193 (1958).
3) R. Hobart, J. Appl. Phys. **36**, 1944 (1965); R. Hobart, J. Appl. Phys. **36**, 1948 (1965).
4) R. Hobart, J. Appl. Phys. **37**, 3573 (1966).
5) J. W. Cahn, Acta Metall. **8**, 554 (1960).
6) Y. Ishibashi, J. Phys. Soc. Jpn. **55**, 2099 (1986).
7) M. Remoissenet and M. Peyrard, J. Phys. C **14**, L481 (1981).
8) M. Peyrard and M. Remoissenet, Phys. Rev. B **26**, 2886 (1982).
9) M. Remoissenet and M. Peyrard, Phys. Rev. B **29**, 3153 (1984).
10) Y. Ishibashi and I. Suzuki, J. Phys. Soc. Jpn. **53**, 4250 (1984).
11) P. E. Peierls, Proc. Phys. Soc. **52**, 34 (1940).
12) Y. Ishibashi, J. Phys. Soc. Jpn. **46**, 1254 (1979).
13) Y. Ishibashi and I. Suzuki, J. Phys. Soc. Jpn. **53**, 1093 (1984).
14) I. Suzuki and Y. Ishibashi, Ferroelectrics **64**, 181 (1985).
15) Y. Ishibashi, Ferroelectrics **98**, 193 (1989).
16) H. Takahasi and M. Mori, Appl. Anal. **1**, 201 (1971).
17) Y. Ishibashi and I. Suzuki, J. Phys. Soc. Jpn. **53**, 1366 (1984).
18) Y. Ishibashi, J. Phys. Soc. Jpn. **54**, 2017 (1985).