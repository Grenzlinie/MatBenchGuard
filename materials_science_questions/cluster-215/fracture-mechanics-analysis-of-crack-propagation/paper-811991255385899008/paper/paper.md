# KLEINE MITTEILUNGEN
ZAMM 53, 409-411 (1973)

T. OHYOSHI

## Effect of Orthotropy on Singular Stresses Produced Near a Crack Tip by Incident SH-waves

As orthotropic materials are sometimes used for a kind of machine parts or members of some constructions, the analy- sis of singular stress distributions near the crack tip in or- thotropic solids (orthogonally anisotropic solids) is very im- portant. This paper concerns the interaction of elastic har- monic waves defined as horizontally polarized shear waves, SH-waves, with a finite crack located on a symmetric surface of orthotropy. The difference between the singular stresses for an orthotropic solid and for an isotropic solid is clarified by the following analysis.

Considering the problem as an antiplane shear one, the only nonvanishing displacement is the $z$ direction component, $w = w(x, y, t)$. Then, all stress components vanish identi- cally except for the longitudinal shear stresses, $\tau_{z x}$ and $\tau_{y z}$. Consequently, the stresses are connected with $w$ as
$$\tau_{y z}=C_{44} \frac{\partial w}{\partial y}, \quad \tau_{z x}=C_{55} \frac{\partial w}{\partial x},\qquad(1)$$
where $C_{44}$ and $C_{55}$ are elastic constants. The equation of motion is
$$d_{55} \frac{\partial^{2} w}{\partial x^{2}}+d_{44} \frac{\partial^{2} w}{\partial y^{2}}=\frac{\partial^{2} w}{\partial t^{2}},\qquad(2)$$
where $d_{55}$ and $d_{44}$ are $\frac{C_{55}}{\varrho}$ and $\frac{C_{44}}{\varrho}$ respectively with $\varrho$ being the mass density of homogeneous materials, they have the dimension (physe velocity)².

## Boundary Conditions and Integral Equations

Cartesian coordinates $(x, y)$ and polar coordinates $(r, \theta)$ are taken about a finite crack as shown in Fig. 1. The finite crack of width $2a$ is located on a symmetric surface of or- thotropy.

![](./images/811991255385899008_1.jpg)

Fig. 1. Coordinates on a finite crack

A periodic displacement disturbance arriving from infinite distance creates an antiplane displacement wave, SH-wave. The incident wave impinging normally on the crack surface can be expressed in the form
$$w^{(i)}=w_{0} \mathrm{e}^{-i \omega\left(y / \sqrt{d_{44}}+t\right)},\qquad(3)$$
where $w_{0}$ is the amplitude of the wave. This wave, of cause, satisfies the equations of motion, Eq. (1), and produces a stress component $\tau_{y z}$ on the $x$ axis, but on the crack surface the stress component must vanish. Consequently the diffracted waves should exist satisfying the following mixed boundary conditions:
$$\left[\tau_{y z}^{(d)}\right]_{y=0}=-P \mathrm{e}^{-i \omega t}, \quad|x|<a,\qquad(4)$$

$$\left[w^{(d)}\right]_{y=0}=0, \quad|x| \geqq a,\qquad(5)$$
where
$$P=-i \omega \varrho w_{0} \sqrt{d_{44}}\qquad(6)$$
and superscript $(d)$ stands for a diffracted component.

Hereafter, the analysis is carried out only for the half space $y \geqq 0$ as the stress fields produced by the diffracted waves are symmetric with respect to the crack plane $y=0$. Letting the displacement and the stresses as
$$w^{(d)}=w^{*} \mathrm{e}^{-i \omega t}, \tau_{y z}^{(d)}=\tau_{y z}^{*} \mathrm{e}^{-i \omega t}, \tau_{z x}^{(d)}=\tau_{z x}^{*} \mathrm{e}^{-i \omega t}, \quad(7)$$
we can supress the time factor $\mathrm{e}^{-i \omega t}$. Then, Eq. (2), (4), (5) are rewritten as
$$d_{55} \frac{\partial^{2} w^{*}}{\partial x^{2}}+d_{44} \frac{\partial^{2} w^{*}}{\partial y^{2}}+\omega^{2} w^{*}=0,\qquad(8)$$

$$\left[\tau_{y z}^{*}\right]_{y=0}=-P, \quad|x|<a,\qquad(9)$$

$$\left[w^{*}\right]_{y=0}=0, \quad|x| \geqq a.\qquad(10)$$

By the theory of partial differential equations and the rela- tions (1), the solutions of (8), (9), (10) may be expressed in the forms
$$w^{*}=\frac{2}{\pi} \int_{0}^{\infty} A(\xi) \mathrm{e}^{-\lambda y} \cos (\xi x) d \xi,\qquad(11)$$

$$\tau_{y z}^{*}=-\frac{2}{\pi} C_{44} \int_{0}^{\infty} \lambda A(\xi) \mathrm{e}^{-\lambda y} \cos (\xi x) d \xi,\qquad(12)$$

$$\tau_{z x}^{*}=-\frac{2}{\pi} C_{55} \int_{0}^{\infty} \xi A(\xi) \mathrm{e}^{-\lambda y} \sin (\xi x) d \xi,\qquad(13)$$
where $A(\xi)$ is the function to be determined from the bound ary conditions, and where
$$\lambda=\sqrt{\left(\xi^{2} d_{55}-\omega^{2}\right) / d_{44}}.\qquad(14)$$

The function $\lambda$ should be restricted as
$$\operatorname{Re} \lambda>0, \quad \operatorname{Im} \lambda<0,\qquad(15)$$
in the upper half space $y \geqq 0$, because the conditions that $w^{*}$ must vanish at an infinite distance from the crack and also that there is nothing but out going waves are required in the field of diffracted waves. Making use of the boundary conditions (9), (10), we have the dual integral equations
$$\frac{2}{\pi} \int_{0}^{\infty} A(\xi) \cos (\xi x) d \xi=0, \quad|x| \geqq a,\qquad(16)$$

$$\frac{2}{\pi} C_{44} \int_{0}^{\infty} \lambda A(\xi) \cos (\xi x) d \xi=P, \quad|x|<a.\qquad(17)$$

To solve the above, $\lambda$ is divided into two terms as
$$\lambda=\sqrt{d_{55} / d_{44}} \xi+G(\xi),\qquad(18)$$
in which a function $G(\xi)$ has the order $\xi^{-1}$ for large $\xi$. Then(17) becomes
$$\frac{2}{\pi} \int_{0}^{\infty} \xi A(\xi) \cos (\xi x) d \xi=h(x), \quad|x|<a,\qquad(19)$$
where
$$h(x)=\sqrt{\frac{d_{44}}{d_{55}}}\left(\frac{P}{C_{44}}-\frac{2}{\pi} \int_{0}^{\infty} G(\xi) A(\xi) \cos (\xi x) d \xi\right), \quad|x|<a.$$

Assuming $h(x)$ to be known for a moment, the solution of (16), (19) may be obtained by the analysis in $[1]^{1})$:

$$
\begin{aligned}
A(\tau)= & a^{2} \int_{0}^{1} \eta J_{0}(a \eta \tau) d \eta \int_{0}^{1} \frac{h(a \eta \zeta)}{\sqrt{1-\zeta^{2}}} d \zeta, \quad(0 \leqq \tau \leqq 1) \quad(21) \\
= & a^{2} \int_{0}^{1} \eta J_{0}(a \eta \tau) d \eta\left[\frac{\pi}{2} \frac{P}{\varrho \sqrt{d_{44} d_{55}}}-\right. \\
& \left.-\sqrt{\frac{d_{44}}{d_{55}}} \int_{0}^{\infty} J_{0}(a \xi \eta) G(\xi) A(\xi) d \xi\right].
\end{aligned}
$$

Now, putting

$$
A(\tau)=\frac{\pi P a^{2}}{2 \varrho \sqrt{d_{44} d_{55}}} \int_{0}^{1} \eta \Lambda(\eta) J_{0}(a \eta \tau) d \eta \quad(0 \leqq \tau \leqq 1). \quad(23)
$$

Eq. (22) is reformed into

$$
\Lambda(\mu)=1+\int_{0}^{1} \eta \Lambda(\eta) F(\mu, \eta) d \eta \quad(0 \leqq \mu \leqq 1),
$$

where

$$
F(\mu, \eta)=a^{2} \int_{0}^{\infty}\left(\xi-\sqrt{\frac{d_{44}}{d_{55}}} \lambda\right) J_{0}(a \xi \eta) J_{0}(a \xi \mu) d \xi .
$$

Eq. (24) is a FREDHOLM's integral equation of the second kind and the function $F(\mu, \eta)$ is symmetric in $\mu$ and $\eta$.

### Evaluation of $F(\mu, \eta)$

In Eq. (25), the integral can be reduced to an integral with finite limit. That is

$$
F(\mu, \eta)=\Omega^{2} i \int_{0}^{1} \sqrt{1-\zeta^{2}} H_{0}^{(1)}(\Omega \zeta \eta) J_{0}(\Omega \zeta \mu) d \zeta(\eta>\mu)(26)
$$

where

$$
\Omega=a \omega / \sqrt{d_{55}} .
$$

It is driven by the following method which is analogous to [2]. Consider the new integrals

$$
I_{1}=\oint_{C_{1}} L(\gamma, \xi) J_{0}(a \xi \mu) H_{0}^{(1)}(a \xi \eta) d \xi \quad(\eta>\mu),
$$

$$
I_{2}=\oint_{C_{2}} L(\gamma, \xi) J_{0}(a \xi \mu) H_{0}^{(2)}(a \xi \eta) d \xi \quad(\eta>\mu),
$$

where

$$
L(\gamma, \xi)=\xi-\gamma
$$

and $C_{1}, C_{2}$ are the contours defined on the complex $\xi$-plane (see, Fig. 2). Letting

$$
\nu=\sqrt{\xi^{2}-\left(\omega^{2} / d_{55}\right)},
$$

$$
\nu^{\prime}=\sqrt{\left(\omega^{2} / d_{55}\right)-\xi^{2}},
$$

the value of $\gamma$ on real axis is defined as illustrated in Fig. 2. Finally, we get the relation

$$
\begin{aligned}
& \int_{0}^{\infty}\left(\xi-\sqrt{\xi^{2}-\frac{\omega^{2}}{d_{55}}}\right) J_{0}(a \xi \mu) J_{0}(a \xi \eta) d \xi \\
& \frac{\omega}{\sqrt{d_{0 s}}} \\
& \quad=-\int_{0}^{\frac{\omega}{\sqrt{d_{s s}}}}\left\{\xi J_{0}(a \xi \eta)+\sqrt{\frac{\omega^{2}}{d_{55}}-\xi^{2}} N_{0}(a \xi \eta)\right\} J_{0}(a \xi \mu) d \xi \\
& \quad(\eta>\mu)
\end{aligned}
$$

![](./images/811991255385899008_2.jpg)

Fig. 2. The contours of integration for the integrals in Eqs. (28), (29)

since $I_{1}+I_{2}=0$. Consequently, making use of the above, we can transform the representation (25), under the condition (15), into the expression

$$
\begin{array}{r}
F(\mu, \eta)=a^{2} i\left\{\int_{0}^{\frac{\omega}{\sqrt{d_{55}}}} \sqrt{\frac{\omega^{2}}{d_{55}}-\xi^{2}} H_{0}^{(1)}(a \xi \eta) J_{0}(a \xi \mu) d \xi\right\} \\
(\eta>\mu). \quad(34)
\end{array}
$$

Eq. (26) may be found easily from (34).

### Stresses Near the Crack Tip

Integrating Eq. (23) by parts, we have

$$
A(\xi)=\frac{\pi P a}{2 \varrho \sqrt{d_{44} d_{55}} \xi}\left[J_{1}(a \xi) \Lambda(1)-\int_{0}^{1} \eta J_{1}(a \xi \eta) \frac{\partial \Lambda(\eta)}{\partial \eta} d \eta\right] .
$$

If $\partial \Lambda(\eta) / \partial \eta$ is bounded in the closed interval $[0,1]$, the divergences of the stress representations at the crack tip, which are obtained by substituting (35) into (12), (13), depend upon the behavior of the corresponding integrands as $\xi \rightarrow \infty$ [3]. Hence the singular parts of the stress representations can be written:

$$
\tau_{y z}^{*} \sim-P a \Lambda(1) \int_{0}^{\infty} J_{1}(a \xi) \mathrm{e}^{-\varkappa \xi y} \cos (\xi x) d \xi
$$

$$
\tau_{z x}^{*} \sim-\varkappa P a \Lambda(1) \int_{0}^{\infty} J_{1}(a \xi) \mathrm{e}^{-\varkappa \xi y} \sin (\xi x) d \xi
$$

where

$$
\varkappa=\sqrt{d_{55} / d_{44}} .
$$

Now, making use of the identity [4]

$$
\int_{0}^{\infty} \mathrm{e}^{-(\varkappa y-i x) \xi} J_{1}(a \xi) d \xi=\frac{1}{a}-\frac{\varkappa y-i x}{a \sqrt{(\varkappa y-i x)^{2}+a^{2}}},
$$

the foregoing integrals in (36), (37) can be evaluated. Representing respectively the real part and the imaginary part of the identity in terms of the polar coordinates $(r, \theta)$ illustrated

1) Here and in the following formulas are:
$J_{0}, J_{1}$ the BESSEL functions of the first kind of order 0 resp. 1 ,
$N_{0}$ the BESSEL function of the second kind,
$H_{0}^{(1)}, H_{0}^{(2)}$ the HANKEL functions of the first resp. second kind.

in Fig. 1 for a very small $r$, we have

$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-\varkappa y \xi} J_{1}(a \xi) \cos (\xi x) d \xi & =-\frac{1}{\sqrt{2 a r}} R_{\mathrm{c}}(\varkappa, \theta)+O\left(r^{0}\right), \\
\int_{0}^{\infty} \mathrm{e}^{-\varkappa y \xi} J_{1}(a \xi) \sin (\xi x) d \xi & =\frac{1}{\sqrt{2 a r}} R_{\mathrm{s}}(\varkappa, \theta)+O\left(r^{0}\right) \quad(41)
\end{aligned}
$$

where

$$
R_{\mathrm{c}}(\varkappa, \theta)=\sqrt{\frac{\sqrt{\cos ^{2} \theta+\varkappa^{2} \sin ^{2} \theta}+\cos \theta}{2\left(\cos ^{2} \theta+\varkappa^{2} \sin ^{2} \theta\right)}}
$$

$$
R_{\mathrm{s}}(\varkappa, \theta)=\sqrt{\frac{\sqrt{\cos ^{2} \theta+\varkappa^{2} \sin ^{2} \theta}-\cos \theta}{2\left(\cos ^{2} \theta+\varkappa^{2} \sin ^{2} \theta\right)}} .
$$

Hence the singular stresses near the crack tip are finally written as

$$
\tau_{y z}^{*} \sim \frac{K}{\sqrt{2 r}} R_{\mathrm{c}}(\varkappa, \theta),
$$

$$
\tau_{z x}^{*} \sim-\frac{K}{\sqrt{2 r}} \varkappa R_{\mathrm{s}}(\varkappa, \theta)
$$

where

$$
K=P \sqrt{a} \Lambda(1) .
$$

Though the value of $\Lambda(1)$ should be calculated for a wave number, it will be shown that it takes the same value as for isotropic solids [2] when it is plotted on a graph versus normalized wave number $\Omega$ (see Eq. (27)). So a detailed discussion of the results are omitted here. By making use of GAUssian Method [5], we calculated $\Lambda(1)$ on electronic computer and show the result in Fig. 3. The main purpose

![](./images/811991255385899008_3.jpg)

Fig. 3. The value of $|\Lambda(1)|$ plotted against the normalized wave number $\Omega$

of this analysis is in representing the singular stresses as functions of angle $\theta$ and orthotropic parameter $\varkappa$. Hence the function $R_{\mathrm{c}}(\varkappa, \theta)$ in (44) is evaluated for $\theta$ from $0^{\circ}$ to $180^{\circ}$ because of an even function with respect to $\theta$. While $R_{\mathrm{s}}(\varkappa, \theta)$ in (45) may be found easily according to the relation

$$
R_{\mathrm{c}}(\varkappa, \theta)=R_{\mathrm{s}}\left(\varkappa, 180^{\circ}-\theta\right) .
$$

$R_{\mathrm{c}}(z, \theta)$ is graphed as shown in Fig. 4, 5. From these figures, it is clear that the orthotropic effect is considerably large on the stresses near the crack tip. Decreasing the parame- ter $\varkappa$ from unit, we find that the angle to yield a maximum value of $R_{\mathrm{c}}(\varkappa, \theta)$ is shifted toward $90^{\circ}$, cf. Fig. 4. Hence, it is recognized that the maximum stresses don't always arise at the angle $\theta=0^{\circ}$ in orthotropic solids.

Putting $\varkappa=1$, i. e., for isotropic case, (44), (45) are reduced to the forms

$$
\tau_{y z}^{*} \sim \frac{K}{\sqrt{2 r}} \cos \frac{\theta}{2},
$$

$$
\tau_{z x}^{*} \sim-\frac{K}{\sqrt{2 r}} \sin \frac{\theta}{2}
$$

![](./images/811991255385899008_4.jpg)

Fig. 4. The behavior of $R_{\mathrm{c}}(\varkappa, \theta)$ for $\varkappa \leqq 1$

![](./images/811991255385899008_5.jpg)

Fig. 5. The behavior of $R_{\mathrm{c}}(\varkappa, \theta)$ for $\varkappa \geqq 1$

which are coincident with the well-known expression for isotropic solids [6].

### Acknowledgment

The author is especially indebted to Prof. A. ATSUMI of Tohoku University for suggesting this problem and for directions throughout the present work.

### References

1 SNEDDON, I. N., Fourier Transforms N. Y. 1951, McGraw-Hill, pp. $65-70$.
2 MAL, A. K., Interaction of Elastic Waves with a Griffith Crack, Int. J. Engng. Sci. 8 pp. $763-776$ (1970).
3 SHI, G. C., and LOEBER, J. F., Wave Propagation in an Elastic Solid witha Line of Discontinuity of Finite Crack, J. Math. Phys. 27 (2), pp. 193 to 213 (1969).
4 ERDELYI, A., Tables of Integral Transforms, Vol. 1, N. Y. 1954, McGraw Hill, p. 182.
5 KRONROD, A. S., Nodes and Weights of Quadrature Formulas, Con- sultants Bureau, N. Y. (1965).
6 LOEBER, J. F., and SHI, G. C., Diffraction of Antiplane Shear Waves by a Finite Crack, J. Acoust. Soc. Am. 44(1), pp. $90-98$ (1968).

Eingereicht am 24. 2. 1972

Anschrift: TADASHI OHYOSHI, Graduate Student, Me- chanical Engineering II, Faculty of Engineering, Tohoku University, Sendai Japan

29*