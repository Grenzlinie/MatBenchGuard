# Parameter Studies of Modal Vibrations Associated with Impurity Pinned Dislocations in a Metal Single Crystal

Charlie H. Cooke, John Kroll
Old Dominion University Norfolk, VA 23529-0077

Received 31 October 2000; accepted 30 December 2000

Koehler's model [1-2] of motion for edge-type dislocations in a metal single crystal that are pinned down by impurity atoms is studied. An exact solution can be found, which is composed of a rapidly decaying transient and a steady time-oscillating, steady state vibration. This solution is used to improve Koehler's [1] approximation to the steady time-oscillating steady state vibration. General parameter studies of the modes of oscillation are then performed. The present result is of some significance, because it allows insight into the behavior of crystalline solids over a wide parameter range, whereas Koehler's asymptotic approach is valid only for materials that exhibit order-of-magnitude variation in system parameters. © 2001 John Wiley & Sons, Inc. Numer Methods Partial Differential Eq 17: 427-439, 2001

Keywords: crystal dislocations; modal vibrations

## I. INTRODUCTION

Suppose that a rapidly oscillating shearing stress is applied to a crystal. When the frequency of the applied stress is in the kilocycle range, the impurity atoms are completely unable to follow the alternating stress because at room temperature diffusion is a slow process. The dislocations are, therefore, anchored by the Cottrell force to the impurity atoms, and the portion of the line dislocation between two impurity atoms oscillates back and forth on its slip plane like a stretched string. References [1-3] give mathematical models of the process, which are of varying degrees of sophistication. Although published for some years, Koehler's formulation [1-2] is still important as a means to obtain computationally efficient initial estimates of material behavior.

Koehler [1-2] derives the following differential equation modeling the motion of a pinned down, edge-type dislocation in a metal single crystal:

$$
A \frac{\partial^{2} y}{\partial t^{2}}+B \frac{\partial y}{\partial t}-C \frac{\partial^{2} y}{\partial x^{2}}=\sigma_{0} a \cos (\omega t). \tag{1}
$$

Correspondence to: Dr. C. H. Cooke, Dept. of Mathematics and Statistics, Old Dominion University, Norfolk, VA 23529
(e-mail: ccooke@odu.edu)
© 2001 John Wiley & Sons, Inc.

![](./images/812456741542297603_1.jpg)

FIG. 1. The amplitudes of $U(z)$ and $V(z)$ from (17) versus $z$ for $\delta=.2$ and $\epsilon=10^{-6}$, (nominal values), solid $=U$, dotted $=V$.

Here, $a$ is the interatomic distance, $y$ is the displacement of an element of the dislocation locus from its equilibrium position, and $x$ is a displacement along the dislocation (often the distance from the center of the dislocation locus).

The applied shearing stress tending to move the dislocation along its slip plane is $\sigma_0 \cos(\omega t)$, and the term on the right gives the force per unit length produced on the dislocation by the external shearing stress. The term on the left involving the constant $A$ represents the inertial force acting on the dislocation, while the term involving $B$ represents the damping force per unit length acting on the dislocation. For a pinned down impurity, the ends of the dislocation are assumed fixed: $y(0,t)=y(l,t)=0$, where $l$ is the distance between two pinned down impurities. It is assumed that the dislocation initially satisfies $y(x,0)=y_t(x,0)=0, 0<x<l$.

Using a power series technique whose justification is not clearly communicated, Koehler [1] obtains several terms of a perturbation approximation of the steady oscillations, assuming that $A$ is small compared to $B$ and $C$. Initial conditions are avoided by the assumption that, for fixed $t$, $y$ is an even function of $x$.

Although Koehler's solution may be adequate for his purposes, it is hampered by a certain degree of inflexibility, because it cannot be used to address either a wide range of parameter variation or general initial conditions. The purpose of this research is to provide an exact solution that can be used for parameter studies over a wide parameter range. For the nominal parameter values associated with annealed copper, it is seen that low-order terms of the presently obtained solution agree with Koehler's first-order solution. The improved solution is used to generate parameter studies that make clear the diverse behaviors that can emerge for the oscillating steady vibrations of a dislocation loop, as the material constants vary.

![](./images/812456741542297603_2.jpg)

FIG. 2. The amplitudes of $U(z)$ and $V(z)$ from (17) versus $z$ for $\delta = 1$ and $\epsilon = 10^{-6}$, solid $= U$, dotted $= V$.

![](./images/812456741542297603_3.jpg)

FIG. 3. The amplitudes of $U(z)$ and $V(z)$ from (17) versus $z$ for $\delta = 10$ and $\epsilon = 10^{-6}$, solid $= U$, dotted $= V$.

## II. FIRST SOLUTION BY EIGEN-FUNCTION EXPANSIONS

The purpose of the present section is motivation of what follows. Some information is gathered concerning the solution of the problem expressed by Eq. (1). In the next section, we obtain and analyze the steady oscillation, which essentially characterizes the modal oscillations of problem (1).

It is well known that series solution of (1) can be achieved by forcing the eigen-function expansion

$$
Y(x, t)=\sum_{k=1}^{\infty} A_{k}(t) \sin (k \pi x / l)
$$

to formally satisfy Eq. (1). Consider the Fourier sine expansion of the right member of Eq. (1):

$$
F=\sigma_{0} a \cos (\omega t)=\sum_{k=1}^{\infty} F_{k} \sin \left(\frac{k \pi x}{l}\right),
$$

where, for $k$ even, $F_{k}=0$, and, for $k$ odd,

$$
F_{k}=4 \sigma_{0} a \cos (\omega t) /(k \pi) .
$$

![](./images/812456741542297603_4.jpg)

FIG. 4. The maximum amplitude versus $\delta$ for $\epsilon=0$.

![](./images/812456741542297603_5.jpg)

FIG. 5. The maximum amplitude, normalized by the maximum amplitude at the nominal values (where $l_{o}=10^{-4}$ cm), versus the nondimensionalized length.

Problem (1) formally can be satisfied by $Y(x,t)$ iff the time-varying amplitudes satisfy the differential equations

$$
A \frac{d^{2} A_{k}}{d t^{2}}+B \frac{d A_{k}}{d t}+C \omega_{k}^{2} A_{k}=F_{k}, \quad \text { where } \quad \omega_{k}=k \pi / l,
\tag{5}
$$

subject to the initial conditions

$$
A_{k}(0)=\frac{d A_{k}}{d t}(0)=0.
\tag{6}
$$

For even $k$, $A_{k}=0$; thus, the formal solution reduces to

$$
Y(x, t)=\sum_{k=1}^{\infty} A_{2 k+1}(t) \sin [(2 k+1) \pi x / l].
\tag{7}
$$

Solution for the $A_{n}(t)$, $n=2k+1$ can be obtained by employing the Laplace transform, and methods of Churchill [4] can be used to show that the resulting solution is rigorous. Unfortunately, the series does not afford a very feasible computational solution, so this is not pursued.

### A. Information Gathering
Vanishing of the $A_{2 k}(t)$ implies that the formal solution is symmetric with respect to the center of the dislocation loop, which is the key assumption Koehler [1] uses to avoid specifying *a priori* an initial distribution of displacement, in determining an approximate steady solution by the perturbation method and a power series technique.

![](./images/812456741542297603_6.jpg)

FIG. 6. The total amplitude versus $z$ for $\alpha=100$ and $\epsilon=0$.

It is clear from a study of the differential equation governing the time-varying amplitudes $A_n(t)$ that resonance cannot occur, because $B$ does not vanish. It also makes clear that the solution of (1) is composed of a transient term and a time-oscillatory steady state. Due to inequalities that are similar to $\sqrt{B^2 - 4AC} < B$, the transient solution of (1) decays with time, more or less quickly, depending upon the parameters of the system. The decay is very rapid, if the Koehler's [1] nominal values for annealed copper are used.

### III. BETTER APPROACH TO SOLUTION BY EIGEN-FUNCTION EXPANSION

In general, when solving a linear partial differential equation using an eigen-function expansion, one seeks a form of the solution that exhibits homogeneous boundary conditions (true here), and, if possible, this solution should also satisfy a homogeneous differential equation. Sometimes this is accomplished by subtracting out the steady solution, which follows.

The solution of Problem (1) can be separated into a rapidly decaying transient plus a time-oscillating steady solution. An outline is given of how the transient could be obtained, whereas the major focus of interest is the oscillating steady solution.

It is helpful to nondimensionalize Problem (1). Let $\tau=\omega t, x=l z$, and $y=l^2(\sigma_0 a/C)\phi$, so that (1) becomes

$$
\epsilon \frac{\partial^2 \phi}{\partial \tau^2}+\delta \frac{\partial \phi}{\partial \tau}-\frac{\partial^2 \phi}{\partial z^2}=\cos(\tau) \tag{8}
$$

![](./images/812456741542297603_7.jpg)

FIG. 7. The total amplitude versus $z$ for $\alpha=100$ and $\epsilon=100$.

with boundary and initial conditions

$$
\phi(0, \tau)=\phi(1, \tau)=0, \tag{9}
$$

$$
\phi(z, 0)=\phi_{\tau}(z, 0)=0, \tag{10}
$$

where $\epsilon C=A \omega^{2} l^{2}$ and $\delta C=B \omega l^{2}$.

Nominal values for the constants are

$$
A=2.5\left(10^{-14}\right) g \cdot c m^{-1}, \tag{11}
$$

$$
B=5\left[10^{-3}\right] g \cdot s^{-1} \cdot c m^{-1}, \tag{12}
$$

$$
C=4\left[10^{-4}\right] g \cdot c m \cdot s^{-1}. \tag{13}
$$

Values of $\omega$ and $l$ generally vary. The nominal values used in this paper are, for forcing frequency, $\omega_{0}=4.6 \pi\left[10^{5}\right] s^{-1}$, and, for impurity separation, $l_{0}=10^{-4} \mathrm{~cm}$. This leads to nominal values for the dimensionless parameters: $\epsilon=10^{-6}$ and $\delta=0.2$.

Solution Splitting. Assume that the general solution is the sum of a homogeneous part and a particular part:

$$
\phi=\phi_{h}(z, \tau)+\bar{\phi}(z, \tau). \tag{14}
$$

![](./images/812456741542297603_8.jpg)

FIG. 8. The total amplitude versus $z$ for $\alpha = .2$ and $\epsilon = 50$.

Here the homogeneous solution satisfies

$$
\epsilon \frac{\partial^{2} \phi_{h}}{\partial \tau^{2}}+\delta \frac{\partial \phi_{h}}{\partial \tau}-\frac{\partial^{2} \phi_{h}}{\partial z^{2}}=0, \tag{15}
$$

and the particular solution satisfies

$$
\epsilon \frac{\partial^{2} \bar{\phi}}{\partial \tau^{2}}+\delta \frac{\partial \bar{\phi}}{\partial \tau}-\frac{\partial^{2} \bar{\phi}}{\partial z^{2}}=\cos (\tau). \tag{16}
$$

Both $\phi_{h}$ and $\bar{\phi}$ must satisfy the homogeneous boundary conditions, because the steady solution and the full solution do.

### A. Particular Solution

Assume a particular solution of the form

$$
\bar{\phi}(z, \tau)=U(z) \cos (\tau)+V(z) \sin (\tau). \tag{17}
$$

This yields the set of second-order, ordinary differential equations

$$
U^{\prime \prime}-\delta V+\epsilon U=-1, \tag{18}
$$

$$
V^{\prime \prime}+\delta U+\epsilon V=0. \tag{19}
$$

This system can be reduced to a single equation by defining $W=U(z)+i V(z)$, which yields

$$
W^{\prime \prime}+(i \delta+\epsilon) W=-1, \tag{20}
$$

![](./images/812456741542297603_9.jpg)

FIG. 9. The total amplitude versus $z$ for $\alpha = .2$ and $\epsilon = 100$.

whose solution is

$$W(z)=C_{1} \exp (\alpha z)+C_{2} \exp (-\alpha z)-1 /[i \delta+\epsilon]. \tag{21}$$

Here $i^{2}=-1$ and

$$\alpha=1 / 2\left[\sqrt{\sqrt{\epsilon^{2}+\delta^{2}}+\delta}(1+i)-\sqrt{\sqrt{\epsilon^{2}+\delta^{2}}-\delta}(1-i)\right]. \tag{22}$$

Since $W(0)=W(1)=0$, there results

$$C_{1}=(1-\exp (-\alpha)) /[2 \sinh (\alpha)(i \delta+\epsilon)], \tag{23}$$

$$C_{2}=(\exp (\alpha)-1) /[2 \sinh (\alpha)(i \delta+\epsilon)], \tag{24}$$

so that an exact steady oscillating solution is

$$\bar{\phi}(z, \tau)=\operatorname{Re}(W(z)) \cos (\tau)+\operatorname{Im}(W(z)) \sin (\tau). \tag{25}$$

Low-Order Approximation. For the nominal values of the parameters of Koehler, when $\epsilon \ll \delta$, then $\alpha=\bar{\alpha}(1+i)$, where $\bar{\alpha}=\sqrt{(\delta / 2)}$. After some labor, there results the solution approximation now given, which approaches Koehler's lowest-order approximation as $\epsilon$ and $\delta$ approach zero:

$$U(z)=A_{1} \sinh (\bar{\alpha} z) \cos (\bar{\alpha} z)+B_{1} \cosh (\bar{\alpha} z) \sin (\bar{\alpha} z)+\exp (-\bar{\alpha} z) \sin (\bar{\alpha} z) / \delta, \tag{26}$$

$$V(z)=B_{1} \sinh (\bar{\alpha} z) \cos (\bar{\alpha} z)-A_{1} \cosh (\bar{\alpha} z) \sin (\bar{\alpha} z)+(1-\exp (-\bar{\alpha} z) \cos (\bar{\alpha} z)) / \delta. \tag{27}$$

![](./images/812456741542297603_10.jpg)

FIG. 10. The total amplitude versus $\epsilon$ for $\delta = .2$.

Here

$$A_1=[-\exp(-\bar{\alpha})\sinh(\bar{\alpha})\sin(\bar{\alpha})\cos(\bar{\alpha})+\cosh(\bar{\alpha})\sin(\bar{\alpha})(1-\exp(-\bar{\alpha})\cos(\bar{\alpha}))]/(\delta D), \ (28)$$

$$B_1=[-(1-\exp(-\bar{\alpha})\cos(\bar{\alpha}))\sinh(\bar{\alpha})\cos(\bar{\alpha})-\cosh(\bar{\alpha})\sin^2(\bar{\alpha})]/(\delta D), \qquad(29)$$

$$D=\sinh^2(\bar{\alpha})\cos^2(\bar{\alpha})+\cosh^2(\bar{\alpha})\sin^2(\bar{\alpha}). \qquad(30)$$

Equations (20)–(24) give the solution that Koehler [1] approximates using power series and a perturbational approach. It is a steady time-oscillating steady state. The advantage of the present approach is that it can be more useful in making studies of the effects of parameter variations; whereas, for small $\epsilon$ and $\delta$, good agreement between the two is expected.

Homogeneous Solution. Seek now a normal mode type solution for the homogeneous equation:

$$\phi_h(z,\tau)=\sum_{n=1}^{\infty}P_n(\tau)\sin(n\pi z), \qquad(31)$$

which yields an ordinary differential equation for determining the $P_n(\tau)$:

$$\epsilon P_n''+\delta P_n'+(n\pi)^2P_n=0. \qquad(32)$$

This equation is easily solved, and because $\sqrt{\delta^2-4\epsilon n^2A^2}<\delta$, the solution decays as $\tau$ increases. For $\delta\gg\epsilon$, which is true in the nominal case, the decay is extremely fast. Hence, the homogeneous solution represents a rapidly decaying transient, which is not of great practical interest.

![](./images/812456741542297603_11.jpg)

FIG. 11. The total amplitude versus $\epsilon$ for $\delta=5$.

## IV. NUMERICAL RESULTS

The steady oscillating solution is of some practical interest. For the nominal case, Koehler's approximate solution may be adequate. However, it is interesting to see what happens for more extreme values, especially as the frequency, $\omega$, and length, $l$, of the dislocation loop are varied.

The parameter $\delta$ increases with both $\omega$ and $l$. Figure 1 depicts the shape of the dislocation loop corresponding to Koehler's [1] lowest-order perturbational solution, for the case $\delta=0.2$. Here, $V(z)$ is negligible, and approximately,

$$
U(z)=1 / 8-1 / 2(z-1 / 2)^{2}. \tag{33}
$$

For $\delta=0, V(z)$ is exactly zero, and $U(z)$ above is exact. For $\delta=1.0$, as seen by Fig. 2, not much has changed. Only as $\delta$ nears 10 do $U(z), V(z)$ become comparable, as seen in Fig. 3.

Of special interest is the maximum amplitude. If the first derivatives of $U$ and $V$ with respect to $z$ both vanish only at the center, then maximum amplitude occurs there. The condition that this happens is

$$
\sqrt{\sqrt{\epsilon^{2}+\delta^{2}}+\delta}+\sqrt{\sqrt{\epsilon^{2}+\delta^{2}}-\delta}<2 \pi. \tag{34}
$$

For the nominal values, this is easily satisfied; this is assumed in the coming discussion.

When the maximum amplitude of the dislocation occurs at the center, $z=0.5$; then the maximum value of $\phi$ is

$$
\phi_{M}=\sqrt{U^{2}(0.5)+V^{2}(0.5)}. \tag{35}
$$

![](./images/812456741542297603_12.jpg)

FIG. 12. The total amplitude versus $\epsilon$ for $\delta = 10$.

The variation of the maximum amplitude, $\phi_M$, with $\delta$ is shown in Fig. 4. Since $\delta$ varies directly with $\omega$, this is the variation of maximum displacement, $\phi_M$, with $\omega$. The figure clearly shows that the maximum amplitude decreases with increasing $\omega$. For $\delta = 0$, the result of Koehler [1] is recovered that maximum displacement is $Y = l^2 \sigma_0 a/(8C)$, in dimensional quantities.

For variations of the length $l$, normalize the maximum amplitude with that maximum obtained by using the nominal value of the other parameters. Thus, define (dimensionless) $dl = l/l_0$, and define a modified maximum dimensionless amplitude as $dl^2 \phi_M$. Figure 5 depicts amplitude variations with $dl$. For $dl = 1$, the maximal value is 0.125. It is also of interest that, for $dl \simeq 13$, there is a maximum of the maximum amplitude, approximately 5.7, which is some 50 times greater than the maximal value 0.125, and which converges to 5 as length increases.

We have assumed in these calculations that $\epsilon$ is small. However, $\epsilon$ could be O(1) for sufficiently large values of $\omega$ and $l$.

Now consideration is given to the solution behavior for parameter values that differ widely from the nominal values. The presence of side lobes with off-center maximum displacement can be seen by plotting total amplitude, or $\sqrt{U^2 + V^2}$, across the length. Figure 6 shows barely formed single side-lobes, for the case $\delta = 100$ and $\epsilon = 0$. Figures 7–9 show more robust side lobes obtained for other conditions.

As damping parameter $\delta$ approaches zero, the steady solution is characterized by the presence of amplitude spikes. Note that for $\delta = 0$, Eq. (18) becomes

$$
U'' + \epsilon U = -1, \tag{36}
$$

$$
U(0) = U(1) = 0. \tag{37}
$$

By the Fredholm Alternative, there is a unique solution only if $\epsilon \neq n^2\pi^2$, where $n$ is a positive integer. There is no solution if this condition is violated. These solutions are not physically realizable, since $\delta = 0$ is impossible. However, for the case $\epsilon = \pi^2$ and $\delta \ll 1$, large amplitudes can occur in the steady solution.

Figures 10-12 show how the amplitude at loop-center achieves a maximum near $\epsilon = \pi^2$. As expected, the maximum decreases as damping increases.

This problem was suggested to the authors by Dr. Stephen Cupschalk, a faculty member of the Department of Mechanical Engineering, Old Dominion University, Norfolk, Virginia. Dr. Cupschalk also provided helpful discussions and orientation concerning dislocations in a metal single crystal.

## References

1.  J. S. Koehler, The influence of dislocations and impurities on the damping and the elastic constants of metal single crystals, ONR and NAS Joint Conf Lattice Imperfections, Pocono Manor, PA October 12-14, 1950.

2.  J. S. Koehler, "The influence of dislocations and impurities on the damping and the elastic constants of metal single crystals," W. Shockley, J. H. Holloman, R. Maurer, F. Seitz (Editors), Imperfections in nearly perfect crystals, Wiley, New York, 1952, p. 197.

3.  A. Granato and K. Lucke, Theory of mechanical damping due to dislocations, J Appl Phys 27 (1956), 583-593.

4.  R. V. Churchill, Fourier series and boundary value problems, McGraw-Hill, New York, 1970, pp. 30-60.