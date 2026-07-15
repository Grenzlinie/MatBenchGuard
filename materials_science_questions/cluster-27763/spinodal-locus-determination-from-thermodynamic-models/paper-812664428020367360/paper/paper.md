![](./images/812664428020367360_1.jpg)

First-order coil-to-flower transition of a polymer chain pinned near a stepwise external potential: Numerical, analytical, and scaling analysis

A. M. Skvortsov, L. I. Klushin, J. van Male, and F. A. M. Leermakers

Citation: *The Journal of Chemical Physics* **115**, 1586 (2001); doi: 10.1063/1.1374210
View online: http://dx.doi.org/10.1063/1.1374210
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/115/3?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
[Coil-bridge transition in a single polymer chain as an unconventional phase transition: Theory and simulation](J. Chem. Phys. **140**, 204908 (2014); 10.1063/1.4876717)

[Adsorption of a wormlike polymer in a potential well near a hard wall: Crossover between two scaling regimes](J. Chem. Phys. **133**, 034902 (2010); 10.1063/1.3452322)

[Phase transitions of a single polymer chain: A Wang–Landau simulation study](J. Chem. Phys. **131**, 114907 (2009); 10.1063/1.3227751)

[Simulating the collapse transition of a two-dimensional semiflexible lattice polymer](J. Chem. Phys. **128**, 124905 (2008); 10.1063/1.2842064)

[A lattice model Monte Carlo study of coil-to-globule and other conformational transitions of polymer, amphiphile, and solvent](J. Chem. Phys. **112**, 7711 (2000); 10.1063/1.481363)

![](./images/812664428020367360_2.jpg)

# First-order coil-to-flower transition of a polymer chain pinned near a stepwise external potential: Numerical, analytical, and scaling analysis

A. M. Skvortsov,⁽ᵃ⁾ L. I. Klushin,⁽ᵇ⁾ J. van Male, and F. A. M. Leermakers

Laboratory of Physical Chemistry and Colloid Science, Wageningen University, Dreijenplein 6, 6703 HB Wageningen, The Netherlands

(Received 25 January 2001; accepted 3 April 2001)

A polymer chain near a penetrable interface is studied in the Gaussian model, in the lattice random walk model and by a scaling analysis. The interface is modeled as an external potential $u$ of a Heaviside step-function form. One end of the chain is fixed at a distance $z_0$ away from this interface. When the end point is fixed in the high potential region, a first-order coil-to-flower transition takes place upon variation of the distance $z_0$. Here, the flower has a strongly stretched stem from the grafting point towards the interface and, on top of it, a crown composed of the remaining segments in a (perturbed) coil conformation. The coil-to-flower transition is analyzed in terms of the Landau free energy. The order parameter is taken to be related to the fraction of segments residing in the energetically favorable region. Exact analytical expressions for the Landau function are obtained in the Gaussian model for any distances $z_0$ and potential strength $u$. A phase diagram in the $z_0$ versus $u$ coordinates is constructed. It contains a line of the first-order phase transitions (binodal line) ending at a critical point $z_0=u=0$, and two spinodal lines. Numerical results are obtained for several chain lengths in the lattice random walk model demonstrating the effects of finite extensibility on the position of the transition point. Excluded volume effects are analyzed within the scaling approach. © 2001 American Institute of Physics. [DOI: 10.1063/1.1374210]

## INTRODUCTION

One of the exciting features of polymer physics is the possibility of a phase transition at the level of a single macromolecule. In particular this occurs when a polymer chain contains a large enough number of repeat units, $N$. The number of repeat units has a similar function as the number of particles in macroscopic thermodynamic systems. The coil-to-globule transition¹ provides a well-known example. Flexible polymers have typically coil-like shapes in solution. The characteristic size of the coil increases with $N$, i.e., $R_g \propto N^\alpha$. The scaling exponent $\alpha$ depends on the solvent quality. In poor solvents the coils are collapsed and $\alpha=1/3$ (globule), whereas in good solvents the exponent is roughly $\alpha=0.6$ and the coil is highly swollen. Close to the transition point ($\theta$ conditions) the chain obeys random walk statistics and $\alpha=0.5$; the chain is nearly ideal. It is further well documented,¹ that when a force acts on a flexible chain it is possible to observe strongly stretched conformations where the characteristic size of the chain is proportional to the chain length $N$. The resulted conformations are usually referred to as trumpet states. Stretched conformations appear naturally in brushes formed by long chains end-grafted to a planar surface.¹ The stretching transition at the level of a single macromolecule can be observed under certain conditions in dilute solutions, e.g., in elongational flow.¹ There is a profound analogy between the conformation of a chain in a brush and that in the elongational flow exactly at the point of the crossover from a coil to a stretched conformation.²

Recently a third state of the polymer chain, i.e., the flower state, has received some attention. This state is uniquely linked to polymers at interfaces. The flower state is composed of a strongly stretched part which is called the stem and a coil-like part which is referred to as the crown. This state of the polymer chain is the subject of the present paper. We note that the “trumpet” states of polymers in extensional flow are also sometimes called “flowers.” We hasten to mention that our paper does not deal with these types of “flowers.”

Apart from excluded volume effects discussed in the end of this paper, most of what we will have to say is based on the Gaussian chain model. In this case ideal conditions are assumed and the behavior of the chain can be mapped on the problem of a diffusing particle. The mathematics needed for this problem is found in textbooks on probability theory.³ For a Gaussian chain fixed with one of its end segments to a solid substrate is understood in large detail because for this an exact partition function is available.⁴⁻⁶ The adsorption parameter $c$ controls the adsorption. When $c>1/R_g$, the chain is strongly adsorbed at the solid forms a layer with many surface contacts and the layer thickness is proportional to $1/c$. On the other hand, when $c<0$ the adsorption energy per segment is then too small to overcome the entropy loss and the chain avoids the surface. At $c=0$ there is an adsorption phase transition of the second-order type. It has been shown that a first-order transition can be invoked in this system when a force is applied to the free end of the chain,

⁽ᵃ⁾Chemical-Pharmaceutical Academy, Prof. Popova 14, 197022 St. Petersburg, Russia.
⁽ᵇ⁾Institute of Macromolecular Compounds of the Russian Academy of Sciences, Bolshoy prospect 31, 199004 St. Petersburg, Russia and the American University of Beirut, Department of Physics, Beirut, Lebanon.

while the point $c{=}0$ at zero force is identified as a bicritical point. $^{6}$

Recently a related solvable model was proposed $^{7}$ for a Gaussian chain for which one end is positioned exactly at an interface between two penetrable media. The model features the construction that the interface is modeled by an external potential which has a finite value in one-half of the space (region) and is zero (reference side) in the other. The model has a phase transition as was discussed in Ref. 8. As soon as the dimensionless potential felt by a polymer segment obeys $|u|{>}1/N$, the chain collects its segments in the low potential region. So upon a change in sign of the external potential the chain suddenly "rolls" its segments into the other phase. For this reason the transition was named "rolling transition." We stress that we do not consider the dynamics of this transition. The order of the transition was discussed in Ref. 7. It was argued that the rolling transition is not a true first-order phase transition but that it features aspects of a critical point. In this paper we will prove this point more definitely. In particular we will analyze the phase transitions that occur in systems where the grafting point is displaced away from the phase boundary. The rolling transition is the end point of a line of first-order phase transitions where one of the control parameters is the distance of the grafting point to the interface.

For a first-order phase transition one can typically define two binodal points, which are the two phases that coexist. For a polymer system a binodal point is identified as a set of conformations that clearly can be distinguished from the set of conformations belonging to the other binodal point. In the rolling transition indeed two sets of conformations are found which are distinguished by the number of segments placed (i) in the negative half-space, or (ii) in the positive half-space. At the transition point in the two sets of conformations are equally large.

There are several standard methods to analyze phase transitions. The most common way is to study the partition function, or the free energy and its derivatives. A first-order phase transition is characterized by the fact that the first derivative of the free energy is discontinuous. This is known as the Ehrenfest route. Another route, which proved to be very useful in the theory of magnetics and liquid crystals, is based on the Landau free energy as a function of an order parameter. In polymer physics, however, this method has been used very rarely. $^{9}$ There exists as yet a more exotic approach suggested by Lee, Yang, $^{10}$ and Fisher $^{11}$ which is based on the analysis of the complex zeros of the partition function. For two exactly solved polymer models, $^{6,7}$ all these methods were followed and compared. In the present paper we apply the Landau function method to the coil-to-flower transition. We will concentrate on the scaling dependencies in the limit of strong fields. A more detailed analysis of the Gaussian chain results, where also some attention is given to logarithmic corrections and low fields is given elsewhere. $^{12}$

The Landau method for the analyses of phase transitions: In the present paper we consider an isolated polymer chain consisting of $N$ units. The equilibrium of free energy, $F$, is related to the partition function by $Q{=}\mathrm{exp}({-}F)$, where the convention that $k_{B}T{=}1$ is used. The analysis of phase transitions by Landau is based on the insight that it is possible to introduce the Landau free energy of the system, $\Phi[\varphi]$, as a function of the order parameter $\varphi$, so that $\mathrm{exp}({-}F){=}\int_{-1}^{1}\mathrm{exp}({-}\Phi[\varphi])d\varphi$. In the case of a scalar order parameter it is typically normalized that ${-}1{\leqslant}\varphi{\leqslant}1$. It is postulated that the Landau function can be written as a series expansion in powers of the order parameter. If the order parameter is a scalar the most general form of the expansion is
$$
\Phi[\varphi]{=}\Phi_{0}{+}H\varphi{+}A\varphi^{2}{+}B\varphi^{3}{+}C\varphi^{4}{+}\cdots, \tag{1}
$$
where $\Phi_{0}$ is the value of the Landau function for $\varphi{=}0$, $H$ a coupling parameter presenting the impact of an external field, $A$,$B$,$C$,..., are phenomenological coefficients that may depend on the control parameter that is used to drive the system through the phase transition. The series expansion is truncated in such a way that it represents correctly the qualitative behavior of the Landau function. A textbook example yielding a second-order transition is realized when $H{=}0$, $B{=}0$, and $C{>}0$, all the higher terms are dropped and the coefficient $A$ changes sign at the transition point. One of the simplest examples of a first-order transition follows when $A{<}0$, $B{=}0$, and $C{>}0$, and the transition is driven by the coupling parameter $H$ which changes sign at the transition. Usually, an analytical expression for the Landau function is not available.

In this paper we will be primarily interested in first-order phase transitions. In this case the Landau function should have two minima. Each minimum represents one phase the system can be in. In the thermodynamic limit $N{\rightarrow}\infty$ the only relevant points in the Landau function are these minima and the fluctuations outside these points have died out. For finite chains the shape of the whole Landau function, or at least near the minimum, is relevant. Below we will mostly ignore these fluctuations (also for short chains) and concentrate on the analysis of the minima in the Landau function as a function of a control parameter.

## A CHAIN PINNED WITH ONE END NEAR A STEP IN EXTERNAL POTENTIAL

The central idea in this paper is to investigate the thermodynamic properties of a polymer chain at or near a liquid–liquid interface. It is essential that, in contrast to a solid–liquid interface, the liquid–liquid interface is penetrable for the chain. The molecular nature of the two phases is not of primary importance. In fact, the molecular features that generate the interface will be disregarded completely. The effect of the molecules is replaced by a fixed external potential $u$ felt by the polymer segments. From this point on it is therefore not necessary anymore to specify the origin of the external potential. It may be essentially entropic in nature, i.e., when the two phases are polymer gels which differ only in polymer density, or enthalpic in nature, i.e., when two strongly segregating liquids are considered.

The external potential of a Heaviside form: $u(z){=}u$ for $z{>}0$, and $u(z){=}0$ for $z{<}0$. One end of the chain is fixed at $z{=}z_{0}$ (see Fig. 1). When $z_{0}{=}0$, we arrive at the symmetrical system for which the rolling transition was analyzed for the Gaussian chain in some depth before. $^{7}$ Here we show that the

![](./images/812664428020367360_3.jpg)

FIG. 1. A liquid-liquid interface is modeled as a Heaviside step function of the external potential $u(z)$: it assumes a value $u$ for positive $z$ and 0 otherwise. An isolated Gaussian chain is fixed with one of its ends at a position $z_0$ as indicated by the black dot. When the grafting point is at any negative $z$ or at a very positive $z$ the chain is (approximately) in a Gaussian conformation (indicated by the big spheres). When the grafting end is at $z_0>0$ and near the interface, a flower may form which consists of a stem (string of stretching blobs) and a crown (perturbed coil); the dashed spheres are drawn to help understand the flower structure.

more general case for $z_0 \neq 0$ can be solved as well. We obtain exact analytical expressions for the Landau function in the Gaussian model, and numerical evaluations for the lattice random walk model. The lattice model differs from the Gaussian chain primarily due to the fact that the lattice chain cannot extend further than its contour length, whereas the Gaussian chain can be deformed indefinitely. At relatively weak external potentials this difference is totally unimportant since the stem deformation always remains within the Hookean range. In the strong field, effects of finite extensibility may be very pronounced.

## The freely jointed chain approach

Numerical calculations can be very effectively performed for lattice models. The chain consists of $N$ lattice steps each of size $l$, numbered $s=1,..., N$. Lattice sites are arranged in layers with coordination number $Z=6$ (cubic lattice) and the layers are numbered arbitrarily $\zeta=-M,-M+1$, ...,$-1,0,1,..., M-1,M$, where $M$ is a layer sufficiently far from $\zeta=0$ such that the chain cannot reach this point. The distance $z$ and the layer number $\xi$ are closely linked: $z=(\xi-\frac{1}{2}) l$. The statistical weight $P(\zeta, s)$ of the $s$-step walk with the last unit residing in layer $\zeta$ is defined by the recurrence relation:

$$
\begin{aligned}
P(\zeta, s)= & e^{-u(\zeta)}\left[\frac{1}{6} P(\zeta-1, s-1)+\frac{4}{6} P(\zeta, s-1)\right. \\
& \left.+\frac{1}{6} P(\zeta+1, s-1)\right] \\
= & e^{-u(\zeta)}\langle P(\zeta, s-1)\rangle,
\end{aligned}
$$

where $u(\zeta)=u$ when $\zeta \geqslant 0, u(\zeta)=0$ when $\zeta<0$. Equation (2) also defines the use of the angular bracket notation. The starting condition

$$
P(\zeta, 1)=\exp (-u(\zeta)) \delta_{\zeta, \zeta_{0}},
$$

where $\delta_{\zeta, \zeta_{0}}=1$ when $\zeta=\zeta_{0}$ and zero otherwise is such that the first segment of the chain sits at a lattice site, and therefore there is always a small distance (i.e., at least half a lattice layer) between the position of the grafting segment and the position of the step in the potential. The end-point distribution $P(\zeta, N)$ is found after $N-1$ successive applications of Eq. (2) for each layer $\zeta$. The end-point distribution, which may be normalized to unity for convenience, is thus obtained after order $N^{*} M$ operations.

Apart from the end-point distribution, we compute the number of states with a given fraction $t$ of segments residing in the negative coordinate half space $\Omega(t)$. It is sufficient to obtain $\Omega(t)$ in the absence of an external potential. The change of this distribution with the external field is simply obtained after Boltzmann weighting. This function is found at the cost of a rather expensive procedure which takes a number of operations of order $N^{2} M$. First, a set of end-point distribution functions $P_{m}(\zeta, s)$ where $m=0,..., N$ is introduced. The variable $m$ indicates the number of segments of the chain that reside in the negative half-space. Next there are propagators of the type of Eq. (2) for the negative half-space, and for the positive half-space:

$$
\begin{aligned}
& P_{m}(\zeta, s)=\left\langle P_{m-1}(\zeta, s-1)\right\rangle, \quad \zeta \leqslant 0, \quad m>0, \quad s>1, \\
& P_{m}(\zeta, s)=\left\langle P_{m}(\zeta, s-1)\right\rangle, \quad \zeta>0, \quad m \geqslant 0, \quad s>1
\end{aligned}
$$

if the first segment (starting condition) is in the negative half-space, then $P_{1}(\zeta, 1)=\delta_{\zeta, \zeta_{0}}$ else $P_{0}(\zeta, 1)=e^{-u} \delta_{\zeta, \zeta_{0}}$. If the $(m, \zeta, s)$ cube is too large to be stored in the computer, it suffices to store just a matrix $(m, \zeta)$ and the $s$ dependence is overwritten (effectively we are only interested in the values of $s=N$ ). The order by which the $m$ propagators are executed in this case is to work from large $m$ to smaller ones. Summation over the $\zeta$ coordinates gives at the end of the propagator procedure, i.e., when $s=N$,

$$
P_{m}(N)=\sum_{\zeta=-M}^{M} P_{m}(\zeta, N).
$$

The $m$ distribution $p_{m}=P_{m}(N) / \sum_{m=0}^{N} P_{m}(N)$, is straightforwardly transformed into the $t$ distribution $\Omega(t)$ as $t=m / N$.

## Gaussian model

We consider the case where a Gaussian chain is grafted to a point $z_{0}$. There are two types of conformations: coils and flowers. Coils reside predominantly within one-half space, while flowers have comparable fractions of segments in each region. This is the rationale for choosing the order parameter to be related to the fraction of segments residing within the negative (zero-potential) half-space. Each segment that sits in this region will be called a contact. It turns out that the partition function for the chain starting at coordinate $z_{0}$ and making $m$ contact with the negative half-space, $Q(z_{0} \mid m)$, can be calculated exactly. Thus, we will obtain a closed analytical expression for the Landau function.

We start with the partition function for a chain which does not cross the interface. If the chain starts at positive coordinates this automatically means that all segments feel the external potential, and the number of contacts is zero. The solution is obtained by the mirror reflection method:

$$
\begin{aligned}
Q\left(z_{0} | 0\right) & =\frac{1}{\sqrt{2 \pi} R_{g}} \int_{0}^{\infty} e^{-\left[\left(z-z_{0}\right) / 2 R_{g}\right]^{2}}-e^{-\left[\left(z+z_{0}\right) / 2 R_{g}\right]^{2}} d z \ e^{-U} \\
& =\operatorname{erf}(a) \cdot e^{-U}, \quad z_{0}>0,
\end{aligned}
$$

where $a=z_{0} /\left(2 R_{g}\right)$ and $R_{g}=\sqrt{N / 6}$ is the gyration radius of an ideal Gaussian coil, and $U=u N$. When the grafting distance is small compared to the coil size, $a \ll 1$, we can approximate the $\operatorname{erf}(a)$ with $\operatorname{erf}(a) \approx 2 a / \sqrt{\pi}$ and when $a>1 \operatorname{erf}(a) \approx 1$.

It is trivial to extract from Eq. (6) the result for the chain that is at negative coordinates. Then of course no segments feel the external potential:

$$
Q\left(z_{0} | N\right)=\operatorname{erf}(a), \quad z_{0}<0.
$$

When the chain is far from the interface we find the reference state for the free energy of the coils and $Q\left(z_{0} | N\right)=1$.

The partition function for the conformations that cross the interface is more complicated. In this case the problem is split into two tasks. The first task is to calculate the partition function for the chain segment that starts at the grafting point $z_{0}$ and ends just before the first contact with the interface. The second one starts at the interface and includes all the rest of the chain no matter where these segments are. As for the first part, we are interested in the partition function of a chain of length $n$ with one end at $z=z_{0}$ and another at the interface $(z=0)$ without making any other contact with the interface. This partition function follows from Eq. (6) if the Gaussian chain end is taken at a very small distance $z=\delta$ from the interface, and is given by

$$
P_{n}\left(z_{0}, \delta | 0\right)=\frac{3 \sqrt{6}}{\sqrt{\pi}} \frac{z_{0} \delta}{n^{3 / 2}} \exp \left(\frac{3 z_{0}^{2}}{2 n}\right).
$$

The zero in $P_{n}\left(z_{0}, \delta | 0\right)$ indicates that the number of contacts with the negative half-space is zero. An internally consistent choice $\delta=1 / 6$ which we will employ henceforward follows from a simple identity for a Gaussian chain in a free space:

$$
P_{N}\left(z_{0}, 0\right)=\int_{0}^{N} P_{n}\left(z_{0}, \delta | 0\right) P_{N-n}(0,0) d n,
$$

where

$$
P_{N-n}(0,0)=\sqrt{\frac{3}{2 \pi(N-n)}}
$$

is the partition function of a Gaussian loop.

The partition function for the second part of the chain consisting of $q=N-n$ segments follows from the classical works on random walks, and was applied to the problem of a Gaussian chain grafted at the liquid–liquid interface in Ref. 8. For a given number of contacts with the negative half-space, $m$, the partition function is

$$
Q_{q}(0 | m)=\frac{1}{\pi \sqrt{m(q-m)}} e^{-u(q-m)}.
$$

Combining Eqs. (8) and (11) we obtain the desired partition function for the whole chain:

$$
\begin{aligned}
Q\left(z_{0} | m\right)= & \int_{n=0}^{N-m} P_{n}\left(z_{0}, \delta | 0\right) Q_{N-n}(0 | m) d n \\
& =\frac{1}{\pi \sqrt{m(N-m)}} e^{-\left[3 z_{0}^{2} / 2(N-m)\right]-u(N-m)}, \quad z_{0}>0,
\end{aligned}
$$

where of course $m>0$. When the chain starts at negative coordinates a similar reasoning leads to

$$
\begin{aligned}
& Q\left(z_{0} | m\right) \\
& \quad=\frac{1}{\pi \sqrt{m(N-m)}} e^{-\left(3 z_{0}^{2} / 2 m\right)-u(N-m)}, \quad z_{0}<0, \quad m<N.
\end{aligned}
$$

This is an exact result which can also be found by alternative routes as is shown elsewhere. $^{12}$

Let us at this point introduce the order parameter as the difference between the fraction of segments that a chain has on the negative side of the space and that of the positive side of the space: $\varphi=2(m / N)-1$. From this is it easily seen that when all the $m=N$ segments are on the negative half-space $\varphi=1$ and when all the segments are on the positive half-space $\varphi=-1$.

In the system under consideration, the truly isotropic phase with $\varphi=0$ is realized only in one special case: $z_{0}=u$ $=0$. Otherwise, the absence of symmetry results in the fact that the state with $\varphi=0$ corresponds to an inhomogeneous flower conformation, and the term "isotropic" does not make much sense. Introducing the Landau function $N \Phi(\varphi)$ $=-\operatorname{In} Q\left(z_{0}, \varphi\right)$, we find

$$
N \Phi[\varphi]=\left\{\begin{array}{ll}
-\ln \operatorname{erf}(-a), & \varphi=1, \\
\ln (N \pi / 2)+\frac{1}{2} \ln \left(1-\varphi^{2}\right)+\frac{2 a^{2}}{1+\varphi}+U \frac{1-\varphi}{2}, & \varphi<1, \quad a<0
\end{array}\right.
$$

for the case when the grafting point is outside the region of the external potential.

Alternatively, when the grafting point is in the region of the (unfavorable) external potential

$$
N \Phi[\varphi]=\left\{\begin{array}{ll}
-\ln \operatorname{erf}(a)+U, & \varphi=-1 \\
\ln (N \pi / 2)+\frac{1}{2} \ln \left(1-\varphi^{2}\right)+\frac{2 a^{2}}{1-\varphi}+U \frac{1-\varphi}{2}, & \varphi>-1 \quad a>0 .
\end{array}\right.
$$

![](./images/812664428020367360_4.jpg)

FIG. 2. $N$ times the Landau functions for various values of the reduced grafting distance $a=z_{0}/(2R_{g})$ as indicated. $N=100$, $u=0.2$. (a) The grafting point is inside the region where the external potential is zero, i.e., $a<0$; (b) The grafting point is inside the region of positive external potential, i.e., $a>0$. The value of the Landau free energy of the coil state is indicated by the diamond marker.

It is of interest to point out that the Landau functions (14) and (15) reduce to the one for the rolling transition. $^{7}$ In this case, $a=0$ and $N\Phi_{a=0}[\varphi]=\ln(N\pi/2)+\frac{1}{2}\ln(1-\varphi^{2})+U(1-\varphi)/2$. As compared to the rolling transition the current Landau functions (14) and (15) are nonanalytical at the extremes $\varphi=1$ when $a<0$, and $\varphi=-1$. The term $\frac{1}{2}\ln(1-\varphi^{2})$ may be expanded leading to even powers of the order parameter only (and thus the rolling transition is symmetric). Series expansion of the new terms $2a^{2}/(1+\varphi)$ and $2a^{2}/(1-\varphi)$ gives both odd and even terms in the expanded Landau function. The reason for the appearance of the odd powers in the order parameter is the symmetry breaking due to the asymmetric position of the grafting point. The new term is proportional to $a^{2}$. In the absence of an external field Eqs. (14) and (15) are invariant to the change $\varphi\rightarrow-\varphi$, $z_{0}\rightarrow z_{0}$, obeying the natural symmetry with respect to interchanging left and right.

Although the above shows that Eqs. (14) and (15) are consistent with Eq. (1), it is noted that Eqs. (14) and (15) are exact and that no series expansions are required or desired.

The two families of the Landau function curves, i.e.; for $a<0$ Eq. (14) and $a>0$ Eq. (15) differ qualitatively, as displayed in Fig. 2. Here two examples are given for the case of $N=100$, $u=0.2$. If the chain is anchored in the low potential region [cf. Fig. 2(a)], the Landau functions are always monotonous and have just one minimum at $\varphi=1$. This minimum corresponds to the coil confined in the negative half-space. In this case there can be no transition whatsoever.

If the grafting point is situated in the region with positive potentials, the situation is fundamentally different. The minimum at $\varphi=-1$ corresponds to the coil in the unfavorable region [indicated in Fig. 2(b) by the diamond marker]. However, for small enough grafting distances there appears to be a new minimum at $\varphi^{*}>0$ which means that the majority of chain segments reside in the favorable half-space. This suggests a flower conformation with the property that the chain has a stem composed of a stretched subchain crossing the unfavorable region from the grafting point to the interface, and a coil-like crown in the favorable half-space. This shape of the Landau function, with two minima separated by a barrier, is a signature of a first-order phase transition.

The coexistence line (binodal) is determined by the condition that the two minima are equally deep. In the vicinity of the binodal line the thermodynamically unfavorable phase described by the higher minimum may be still metastable. In a standard approach, spinodal points are identified by the condition that the metastable minimum disappears together with the separating barrier. At this point the flower state becomes unstable. This case requires a more delicate analysis which will be given later. Analysis of the Landau function allows one to construct the complete phase diagram.

# PHASE DIAGRAM

## Coexistence line: analytical description

The concept of phases and of a phase diagram has a strict meaning only in the thermodynamic limit $N\rightarrow\infty$, $U=uN\rightarrow\infty$. Although we can analyze the Landau function at arbitrary values of $u$ and $N$, the two phases are not well defined for $U\approx1$, and the positions of the minima by themselves are not enough to determine the average properties of the system. The region of relatively small $U$ means that, even if both minima exist, we are in the limit of a ‘‘small system’’ where one cannot properly speak of phases.

In the ‘‘large system’’ limit $U\gg1$ the binodal and spinodal lines are well defined. From differentiation of Eq. (15) the minimum in the Landau function corresponding to the flower state is located at
$$
\varphi_{\min}\approx1-2\frac{a}{\sqrt{U}}+\frac{1}{2U}, \tag{16}
$$
where the Landau function takes the value
$$
\begin{aligned}
N\Phi_{\text{flower}}&\approx\ln(N\pi/2)+\frac{1}{2}\ln\left(\frac{4a}{\sqrt{U}}\right)+\frac{1}{2}\ln\left(1-\frac{a}{\sqrt{U}}\right)\\
&+2a\sqrt{U}. \tag{17}
\end{aligned}
$$

The minimum describing the coil state remains at $\varphi=-1$ and has a depth of
$$
N\Phi_{\text{coil}}=U-\ln\operatorname{erf}(a)\approx U. \tag{18}
$$

At the binodal condition the two minima of the Landau function have the same depth which means that the two type of populations are equally large. An expression for the binodal in reduced variables is given by
$$
\frac{2a^{*}}{\sqrt{U}}\approx1-\frac{1}{U}\ln(N\pi/2) \tag{19a}
$$
and the corresponding formula in natural coordinates is

![](./images/812664428020367360_5.jpg)

FIG. 3. The average fraction of contacts numerically evaluated for the lattice model with N=200 plotted against the reduced grafting distance $z_0/N$ for several values for the external potential felt by each segment of the polymer chain, $u$, as indicated.

$$
\frac{z_{0}^{*}}{N} \approx \sqrt{\frac{u}{6}}-\frac{1}{N \sqrt{6 u}} \ln (N \pi / 2). \tag{19b}
$$

The asterisk indicates that the values are taken on the coexistence line. Inserting this result in Eq. (16) we obtain that at the equilibrium transition point, the flower conformation is characterized by
$$
\frac{m^{*}}{N} \approx \frac{1}{2}\left(1+\frac{N}{6 z_{0}^{2}} \ln (N \pi / 2)\right). \tag{20}
$$

In the limit of very long chains, half of the segments in the flower state make contacts with the favorable region $m^{*}=N/2$. We have shown earlier $^{7}$ that the crown penetrates the positive potential region only to a completely negligible extent. This means that the number of segments in the crown equals $N/2$. Therefore at the transition point half of the total number of segments form the stem and the other half makes the crown, independently of the position along the binodal. The jump in the order parameter $\varphi_{\text {flower}}-\varphi_{\text {coil}} \approx 1$ turns out to be universal, independent of the long chain length and the other control parameters.

### Numerical results: finite extensibility effects

As the grafting distance $z_0$ is increased, the number of contacts in the flower conformation goes down. For the Gaussian model this should happen linearly with $z_0$ [see Eq. (16)]:
$$
\frac{m_{\mathrm{fl}}}{N} \cong 1-\frac{z_{0}}{N} \sqrt{\frac{3}{2 u}}. \tag{21}
$$

Below the transition distance $z_{0}^{*}/N=\sqrt{u/6}$ the value $m_{\text {fl}}$ coincides with the equilibrium average value $\langle m \rangle$. The average fraction of contacts $\langle m \rangle/N$ reaches the value of $1/2$ at the transition distance and then drops abruptly to zero since above the transition distance the coil state becomes thermodynamically stable.

Figure 3 displays the average fraction of contacts as a function of the grating distance $z_0/N$ calculated numerically for a lattice model with $N=200$ for several values of $u$. In this figure it is seen that for each value of the external potential the number of contacts decreases linearly with $z_0$ up to the transition distance. This linear dependence is closely related to the fact that the force acting on the grafting point is independent of $z_0$, as will be discussed in the last section of this paper.

As is seen in Fig. 3, when the potential is not very strong, $u<1$, both the position of the transition point, as well as the magnitude of the jump are in good accordance with the analytical results for the Gaussian chain. For very strong potentials however, the stem of the flower is stretched to such an extent that finite extensibility effects become quite pronounced. For a lattice chain, the transition distance $z_{0}^{*}/N$ cannot be larger than unity and only tends towards unity in the limit of $u \gg 1$. The magnitude of the jump in strong potentials becomes smaller than $1/2$ and eventually vanishes in the same limit. Calculations show that in the coordinates used, the curves are universal in the sense that they do not depend on the chain length, $N$ (at least not for $N>50$). The transition points $z_{0}^{*}/N$ extracted from the set of numerical data give us the coexistence line which, therefore, turns out to be universal for all chains provided they are sufficiently long.

![](./images/812664428020367360_6.jpg)

FIG. 4. Coexistence curves for the Gaussian model (straight dotted line) and for the lattice model with finite extensibility (solid line) in the $z_{0}^{*}/N$ vs $\sqrt{u}$ coordinates.

The coexistence line is shown both for the Gaussian chain as well as for the lattice chains in the $z_{0}^{*}/N$ versus $\sqrt{u}$ coordinates in Fig. 4. For the Gaussian model, the binodal is given by a straight line (shown as a dotted line) as follows from Eq. (19). For the lattice chain model, the curve deviates more and more from this straight line at large values of $u$ approaching the limiting value of unity. Again, the shape of the binodal line of the lattice chain model in the $z_{0}^{*}/N$ versus $\sqrt{u}$ coordinates is universal, i.e., does not depend on $N$.

### Metastable states and spinodal lines

The flower state and the coil state are separated by a free energy barrier. The position of the barrier is found from expression (15) for the Landau function:
$$
\varphi_{b} \approx-1+\frac{2}{U-a^{2}}. \tag{22}
$$

The barrier height calculated from the Landau free energy of the coil state is given by

$$
N(\Phi_{b}-\Phi_{c})=\ln\left(\frac{N\pi}{e\sqrt{U-a^{2}}}\right)+a^{2}. \tag{23}
$$

It is clear that when the grafting distance is large enough,

$$
a^{2}=\frac{3 z_{0}^{2}}{2 N} \gg 1, \tag{24}
$$

the barrier height will be much larger than $k_{B}T$, and even if the coil state does not correspond to the true equilibrium it will be metastable, with a long lifetime. The spinodal is determined by the condition that the lifetime of the metastable state becomes small (microscopic). Neglecting the logarithmic term (which is usually done unless one is specifically interested in details of the barrier crossing kinetics) we can write the spinodal condition as $a^{**}\approx 1$, or

$$
\frac{z_{0}^{**}}{N} \approx \frac{R_{g}}{N} \sim N^{1 / 2}. \tag{25}
$$

Physically, $a^{2}$ has the meaning of the work required to deform the coil in order for it to make some contacts with the interface. At the spinodal [cf. Eq. (25)], the grafting distance is comparable to a typical fluctuation in the coil size, $R_{g}$.

The barrier height counted from the flower state minimum is given by

$$
N(\Phi_{b}-\Phi_{\mathrm{fl}})=\ln\left(\frac{4\sqrt{a}}{e(\sqrt{U}-a)(\sqrt{U}+a)^{1/2}}\right)+(\sqrt{U}-a). \tag{26}
$$

The equation for the other spinodal line can be simply written as

$$
a^{**} \approx \sqrt{U} \tag{27}
$$

or

$$
\frac{z_{0}^{**}}{N} \approx \sqrt{\frac{2 u}{3}}. \tag{28}
$$

Comparing this to the equation of the binodal line, we see that the flower state becomes absolutely unstable when the grafting distance becomes twice as large as the stem length at the equilibrium transition point,

$$
\frac{z_{0}^{**}}{z_{0}^{*}}=2. \tag{29}
$$

The complete phase diagram for the Gaussian chain model is shown schematically in Fig. 5. It consists of the coexistence line (shown as a solid line) and two spinodal lines (shown as dotted lines). Regions of stability of the coil and the flower states are indicated. Metastable states can exist in the region between the two spinodals and are also indicated. Near the origin, there is a region of the size $1\sqrt{N}$ which corresponds to the "small system" limit. Phases cannot be properly defined there.

Finite extensibility effects are illustrated in Fig. 6. Both the coexistence line and the upper spinodal line obtained numerically for the lattice chain model are deformed in a similar way at very large values of $u$. Therefore, the region where metastable flowers exist become narrower for very strong potentials. In the thermodynamic limit $N\rightarrow\infty$, the "small system" region is contracted to a point in the $(z_{0}^{*}/N-\sqrt{u})$ coordinates. The region where the coil state is absolutely unstable also vanishes. Therefore, these two regions are not shown in Fig. 6.

![](./images/812664428020367360_7.jpg)

FIG. 5. Qualitative phase diagram for a Gaussian chain grafted with one end near a step in the external potential. The normalized distance of the grafting point to the step in the potential $z_{0}/N$ is plotted against the square root of the potential field. The binodal line is a solid and the spinodal line (#1) and (#2) are dotted. Regions of stability and metastability of the coil as well as the flower conformations are indicated.

The binodal and spinodal points of our system are illustrated in Fig. 7 for the potential value of $u$=0.1 and $N$=1000. The equilibrium average fraction of contacts as a function of the grafting distance, $z_{0}$, is shown together with the average number of contacts that would be measured if the distance is changed with finite speed. The hysteresis effect is demonstrated by curves describing the number of contacts in metastable states. Arrows indicate the direction of the process of changing the grafting distance. The flower state is metastable at distances between $z_{0}^{*}$ and $z_{0}^{**}$, where its

![](./images/812664428020367360_8.jpg)

FIG. 6. Phase diagram for lattice chains with finite extensibility in the $N\rightarrow\infty$ limit. The binodal line is shown as solid and the spinodal is displayed as a dotted line. The normalized distance of the grafting point to the step in the potential $z_{0}/N$ is plotted against the square root of the potential field. Regions of stability and metastability of the coil as well as the flower conformations are indicated. In the $N\rightarrow\infty$ limit the second spinodal line coincides with the abscissa and the "small system" region vanishes. Therefore these are not indicated.

![](./images/812664428020367360_9.jpg)

FIG. 7. Equilibrium average fraction of contacts as a fraction of the grafting distance, $z_0$, for the potential value of $u$=0.2 and $N$=1000 (solid line). The hysteresis effect is demonstrated by curves describing the number of contacts in the metastable states (dotted lines). Arrows indicate the direction in which the grafting distance is changed.

Landau function minimum is higher than that of the coil state. The fraction of contacts for a metastable flower state is still given by the position of the corresponding minimum of the Landau function [Eq. (21)]: It decreases linearly with the grafting distance until it vanishes at $z_0^{**}=2z_0^{*}$.

On the other hand, if the grafting point is moved closer to the interface starting from a distance $z_0>z_0^{**}$, the coil state with no contacts remains metastable until the grafting distance becomes of the order of $R_g$, and then the fraction of contacts jumps to a value close to unity.

## DISCUSSION

### Force acting on the grafting point

Let us consider the case when external potential is fixed ($U\gg 1$) and the pinned end point is moved across the interface. When the end point is in the zero potential region (negative coordinates), the chain forms a coil. When the end point is moved to the interface, the coil is deformed and still resides in the negative half-space. To move the grafting point further into the unfavorable region one has to do work. In other words, the end point fixed at positive $z_0$ experiences a force

$$
f=-\frac{\partial F}{\partial z}=-\frac{\partial \Phi\left(\varphi_{\mathrm{fl}}\right)}{\partial z}.\qquad(30)
$$

It follows from Eq. (17) that the force is given by

$$
f=\sqrt{6 u}+\frac{1}{2}\left(\frac{1}{z_{0}}-\frac{1}{N \sqrt{2 u / 3-z_{0}}}\right).\qquad(31)
$$

When the grafting distance $z_0$ is not too small, the force becomes independent of the end-point position:

$$
f=\sqrt{6 u}.\qquad(32)
$$

In the equilibrium situation, the force remains constant until we reach the grafting distance $z_0^{*}$, corresponding to the binodal line. The force then drops abruptly to zero since the coil retracts completely into the unfavorable region. However, when the system has no time to equilibrate Eq. (27) is still applicable until we approach the spinodal condition $z_0=z_0^{**}=N\sqrt{2u/3}$. Here the correction term in Eq. (31) diverges. This divergence is unphysical and signals the disappearance of the flower state. Beyond the spinodal distance the force is zero.

### Scaling picture and excluded volume effects

One can easily construct a scaling picture of the coil-to-flower transition. The flower consists of a stem of $n$ segments crossing the unfavorable region from the grafting point to the interface and the crown of $(N-n)$ segments residing in the favorable region. The free energy of this state has the stretching term $3z_0^2/2n$, and the interaction term $nu$. Minimization with respect to $n$ gives $n=z_0\sqrt{3/(2u)}$, while the free energy of the flower state is $F_{\mathrm{fl}}=z_0\sqrt{6u}$. It follows immediately that the elastic force, as well as the degree of stretching of the stem, $z_0/n=\sqrt{2u/3}$ are independent on the position of the grafting point. Both parameters are related to the size of the stretching blob $\xi\sim 1/f=(6u)^{-1/2}$. As the end point is moved further into the region with positive external potential, the number of blobs in the stem grows linearly with $z_0$, while the blob size remains the same. Going back to Eq. (31) derived from a rigorous theory, we see that corrections to the simple blob picture become important in two extreme cases. When the stem is comparable or smaller than one blob $z_0\leqslant\xi$ the first correction term is dominant. When the crown is comparable or smaller than one blob, the second correction term becomes important (since $N\sqrt{2u/3}$ is the length of the stem composed of all the segments, $N\sqrt{2u/3}-z_0$ gives some measure of the size of the crown). The scaling picture gives the correct value for the equilibrium transition point. Equating the free energy of the flower state to that of the coil, $F_c=uN$, one obtains again

$$
\frac{z_{0}^{*}}{N}=\sqrt{\frac{u}{6}}.\qquad(33)
$$

The scaling picture is quite useful for estimating the effect of excluded volume interactions on the coil-to-flower transition. The flower free energy is modified to

$$
F_{\mathrm{fl}}=n u+A\left(\frac{z_{0}}{n^{v}}\right)^{1 /(1-v)},\qquad(34)
$$

where $A$ is a numerical coefficient which is 3/2 for an ideal three-dimensional coil, and $v$ is the Flory exponent equal to 3/5 in the three-dimensional case and 3/4 in a two-dimensional situation. Minimization with respect to $n$ yields

$$
n=z_{0} u^{v-1}\left(\frac{1-v}{A v}\right)^{v-1}\qquad(35)
$$

and the free energy is given by

$$
F_{\mathrm{fl}}=B z_{0} u^{v},\qquad(36)
$$

where $B$ again is purely a number given by $B=[1-v/Av]^{v-1}+A[1-v/Av]^v$. It follows that the crown still exerts a constant stretching force, which now scales as $f\sim u^v$. Since the free energy of the coil is $F_c=uN$, the equilibrium transition point (the equation of the coexistence line) is

$$
\frac{z_{0}^{*}}{N}=B u^{1-v}. \tag{37}
$$

Comparing a Gaussian chain with a self-avoiding walk in the same potential $u$, one can see that in the presence of excluded volume the flower at the coexistence line has a longer stem: $Nu^{2/5}>Nu^{1/2}$. This is natural since the elastic modules is related to $R_{g}^{-2}$ so that the Gaussian chain is more difficult to stretch. The fraction of segments in the stem at the binodal line is found to be $n^{*}/N=v$, still independent of $z_0$ and $u$. The value of $1/2$ is of course recovered in the Gaussian case. As a result, the jump in the fraction of contacts in the presence of excluded volume effects is smaller ($2/5$ instead of $1/2$). The spinodal conditions are modified correspondingly. One spinodal line is obviously given by
$$
z^{* *} \sim R_{g} \sim N^{v}. \tag{38}
$$

The other spinodal line is found from the condition that the number of segments in the stem is equal to $N$. Since the number of segments in the stem is linear in $z_0$, one can immediately obtain
$$
\frac{z^{* *}}{z^{*}}=\frac{1}{v}. \tag{39}
$$

The binodal and spinodal lines came closer to each other than in the Gaussian chain case. The region where metastable flowers exist is relatively smaller since the crown at the coexistence line is composed of only $2N/5$ segments.

## Phase diagram and the critical point
The phase diagram in the coordinates $(z_0/N,\sqrt{u})$ shown in Fig. 6 contains a line of first order coil-to-flower transitions. As usual the phase diagram is strictly speaking only applicable in the thermodynamic limit, i.e., $N\rightarrow\infty$. In terms of the Landau free energy, the minima have to be separated by a very high barrier in order for the two phases to be properly determined. The coexistence line terminates at the origin which means that $(z_0/N\sqrt{u})=(0,0)$ must be a critical point.

In a canonical picture, the jump in the order parameter should decrease as one comes closer to the critical point, and eventually vanish there. The "rolling transition" corresponding to crossing the critical point $(0,0)$ was examined earlier. It was found that the order parameter $\varphi=(2m/N)-1$ which we are using here still changes jumpwise. Moreover, the magnitude of the jump $\Delta\varphi=2$ at the rolling transition is twice as large as when the coil-flower coexistence line is crossed. This of course goes contrary to the standard picture. One must note however that the choice of the order parameter in single-macromolecule phase transitions is quite a delicate matter, and the general picture of these phase transitions differs sometimes from more conventional examples for low-molecular weight systems. For example, an exactly solvable model of an adsorbing chain with an external force acting on its end exhibits a first-order transition while the Landau function does not develop two minima. In our present model an obvious difference between the two phases (coil and flower) is due to the stretched stem. The stretching parameter of the stem $S=z_0/n$ actually determines the position of the barrier and its height at the transition point. As one approaches the critical point along the binodal, the stretching parameter decreases and eventually vanishes. This gives an indication that $S$ may serve as a reasonable order parameter. In the case of $uN\gg1$ which we mostly analyze here; there is a simple relationship between the two order parameters:
$$
S=\frac{2 z_{0}}{N(1-\varphi)}. \tag{40}
$$

## CONCLUSIONS
A polymer chain pinned with one of its ends at the unfavorable side of a penetrable interface show a conformational phase transition upon variation of the grafting distance. The two types of conformations that can coexist are the coil and the flower state. The last one is a conformation with a strongly stretched stem from the grafting point to the interface and a crown which is a perturbed coil living on the favorable side. We have shown that it is possible to analyze the coil-to-flower transition by means of a Landau function. It was proven that the prediction for the Gaussian chain copied accurately the numerically exact results in a freely-jointed chain lattice model provided that the stem is not stretched too much. In the phase diagram one binodal and two spinodal lines are identified. Effects of finite extensibility on the phase diagram occur only at very high fields. Excluded volume correlations also effect the phase diagram and these changes are analyzed by a scaling analysis. From all of this information is available in which region of parameter space one can expect metastable states, i.e., (i) the coil state that is present in the unfavorable part of the interface, while thermodynamically a flower state is more favorable or (ii) the flower state is present even though the coil has a lower free energy. The line of first-order phase transitions, i.e., the binodal line, in the phase diagram stops at $(z_0,U)=(0,0)$. For this reason the rolling transition, which is the name of the transition exactly at this point, is not a first-order phase transition but necessarily a critical point. For this critical point the exact partition function is known for all values of the chain length.

## ACKNOWLEDGMENTS
This work was partially supported by NWO Dutch-Russian program for polyelectrolytes in complex systems. The work of one of the authors (J.v.M.) is part of the research programs sponsored by Netherlands Organization for Scientific Research/Chemical Sciences (NWO/CW). A.M.S. acknowledges support from Russian Fund of Fundamental Investigations (RFFI) Grant 9903-33385a. L.K. is grateful to the Center for Advanced Mathematical Sciences at the American University of Beirut.

$^{1}$G. J. Fleer, J. M. H. M. Scheutjens, M. A. Cohen Stuart, T. Cosgrove, and B. Vincent, *Polymers at Interfaces* (Chapman & Hall, London, 1993).
$^{2}$A. M. Skvortsov, A. A. Gorbunov, and L. I. Klushin, Polym. Sci., Ser. A Ser. B **A36**, 1696 (1994).
$^{3}$W. Feller, *An Introduction to Probability Theory and its Applications* (Wiley, New York, 1950).
$^{4}$Y. Lepine and A. Caillé, Can. J. Phys. **56**, 403 (1978).

$^{5}$E. K. Eisenriegler and K. Binder, J. Chem. Phys. **77**, 6296 (1982).

$^{6}$A. A. Gorbunov and A. M. Skvortsov, J. Chem. Phys. **98**, 5961 (1992).

$^{7}$A. M. Skvortsov, J. van Male, and F. A. M. Leermakers, Physica A **290**, 445 (2001).

$^{8}$A. M. Skvortsov, L. I. Klushin, J. van Male, and F. A. M. Leermakers, J. Chem. Phys. **112**, 7238 (2000).

$^{9}$L. D. Landau and E. M. Lifshitz, *Statistical Physics* (Nauka, Moscow, 1976).

$^{10}$T. D. Lee and C. N. Yang, Phys. Rev. **87**, 410 (1952).

$^{11}$M. E. Fisher and D. R. Nelson, Phys. Rev. Lett. **32**, 1350 (1974).

$^{12}$A. M. Skvortsov, L. I. Klushin, J. van Male, and F. A. M. Leermakers (unpublished).