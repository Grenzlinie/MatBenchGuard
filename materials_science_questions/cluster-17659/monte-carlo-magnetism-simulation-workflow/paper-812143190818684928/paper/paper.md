PHYSICAL REVIEW B 72, 064518 (2005)

# Molecular dynamics of pancake vortices with realistic interactions: Observing the vortex lattice melting transition

Yadin Y. Goldschmidt

Department of Physics and Astronomy, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, USA

(Received 6 April 2005; revised manuscript received 15 June 2005; published 18 August 2005)

In this paper we describe a version of London Langevin molecular dynamics simulations that allows for investigations of the vortex lattice melting transition in the highly anisotropic high-temperature superconductor material $\mathrm{Bi}_{2}\mathrm{Sr}_{2}\mathrm{CaCu}_{2}\mathrm{O}_{8+\delta}$. We include the full electromagnetic interaction as well as the Josephson interaction among pancake vortices. We also implement periodic boundary conditions in all directions, including the $z$ axis along which the magnetic field is applied. We show how to implement flux cutting and reconnection as an analog to permutations in the multilevel Monte Carlo scheme and demonstrate that this process leads to flux entanglement that proliferates in the vortex liquid phase. The first-order melting transition of the vortex lattice is observed to be in excellent agreement with previous multilevel Monte Carlo simulations.

DOI: 10.1103/PhysRevB.72.064518

PACS number(s): 74.25.Dw, 74.25.Qt, 74.25.Ha, 74.25.Bt

## I. INTRODUCTION

There has been a major research effort in recent years to understand the properties of high-temperature superconductors which have been discovered during the 1980s. High-temperature superconductors belong to the class of superconducting materials known as type II that allow for partial magnetic flux penetration whenever the external field satisfies $H_{c1}<H<H_{c2}.^{1-3}$ The flux penetrates the sample in the form of flux-lines (FL's), each containing a quantum unit $\phi_{0}=hc/2e$ of flux. At low temperature the FL's form an ordered hexagonal lattice (Abrikosov lattice) due to their mutual repulsion. At high temperature and/or magnetic field this lattice melts due to thermal fluctuations. $^{4-8}$

High-temperature superconductors are anisotropic materials which are made from stacks of superconducting layers associated with copper-oxide planes. The layers are weekly coupled to each other. The parameter measuring the anisotropy is $\gamma$, defined as $\gamma^{2}=m_{z}/m_{\perp}$, where $m_{z}$ and $m_{\perp}$ denote the effective masses of electrons moving along the $c$ axis (perpendicular to the superconducting planes) and the $ab$ plane, respectively. While for the material $\mathrm{YBa}_{2}\mathrm{Cu}_{3}\mathrm{O}_{7-\delta}$ known as YBCO the anisotropy is somewhere between 5 and 7, for the material $\mathrm{Bi}_{2}\mathrm{Sr}_{2}\mathrm{CaCu}_{2}\mathrm{O}_{8+\delta}$ known as BSCCO, the anisotropy is estimated to be 10 to 100 times larger.

For BSCCO and highly anisotropic materials similar to it, each FL is represented more faithfully by a collection of objects referred to as pancake vortices or just "pancakes". $^{9,10}$ Pancakes are centered at the superconducting planes. Each pancake interacts with every other pancake, both in the same plane and in different planes. The interaction can be shown to consist of two parts. The first part is called the electromagnetic interaction (or simply magnetic) and it exists even in the case where layers of the material are completely decoupled, so no current can flow along the $c$ axis of the sample. The electromagnetic interaction originates from screening currents that arise in the same plane where a pancake resides as well as in more distant planes. This leads to a repulsive interaction among pancakes in the same plane and an attractive interaction among pancakes in different planes. $^{9,11}$

The second part of the interaction is called the Josephson interaction. $^{2,11,12}$ It results from the fact that there is a Josephson current flowing between two superconductors separated by an insulator and this current is proportional to the sine of the phase difference of the superconducting wave functions. The two superconductors in the present case are the adjacent $\mathrm{CuO}_{2}$ planes. When two pancakes belonging to the same stack and residing in adjacent planes move away from each other, the phase difference that originates causes a Josephson current to begin flowing between the planes. This results in an attractive interaction between pancakes that for distances smaller than $r_{g}\equiv\gamma d$ is approximately quadratic $^{2,11}$ in the distance. Here we denoted by $d$ the interplane separation and $\gamma$ is the anisotropy. When the two adjacent pancakes are separated by a distance larger than $r_{g}$, a "Josephson string" is formed, whose energy is proportional to its length. $^{12,13}$

In three recent papers $^{14-16}$ we presented results of multilevel Monte Carlo simulations performed on high temperature superconductors. In the first publication $^{14}$ both YBCO and BSCCO were treated with and without columnar defects. In that paper we included the effect of the electromagnetic interaction only as an in-plane interaction which is valid in the approximation that the FL's do not deviate too much from a straight line and the anisotropy is not too large. This is usually the case for YBCO (Ref. 17) and is justified for highly anisotropic materials if the anisotropy is not higher than about 250, which is often not the case for BSCCO where for optimally doped samples one expects anisotropies in the range of $400-500.^{18}$

In the second paper we conducted multilevel Monte Carlo simulations including both the in- and out-of-plane electromagnetic interactions plus the Josephson interaction among nearest neighbor pancakes in adjacent planes. The Josephson interaction is often neglected in simulations of the highly anisotropic BSCCO, but we showed that it is crucial to obtain the proper scaling behavior of the results and should not be entirely neglected. We also implemented periodic boundary conditions in all directions including the $z$ direction. In the third paper an approximation to the Josephson coupling

1098-0121/2005/72(6)/064518(10)/$23.00

064518-1

©2005 The American Physical Society

has been derived from a numerical solution of the two- dimensional sine Gordon equation, which is meant to im- prove on the previous approximation introduced by Ryu et al. $^{19}$

Molecular dynamics (MD) is a powerful tool for simula- tions of physical systems and it often serves as an alternative to Monte Carlo (MC) simulations. Its advantage is that it can be used to investigate the real dynamics of the system as opposed to MC simulations that are used for obtaining equi- librium properties. However MD simulations could be plagued by the absence of ergodicity when applied to sys- tems represented by path integrals $^{20}$ and there is also the problem of implementing permutations for the case of iden- tical particles like Bosons. The problem of ergodicity is re- ally not much of an issue for Langevin simulations since the thermal noise helps the system explore the configuration space and it can be shown by using the corresponding Fokker-Planck equation that equilibrium is reached in the long time limit. For flux-lines (FL's) we have found a way to implement "permutations" in the MD simulations by flux cutting and recombining as will be explained further below. We were also able to implement periodic boundary condi- tions in all directions (including the $z$ direction) and to in clude the in- and out-of-plane electromagnetic interaction as well as the Josephson interaction using the approximation wehave recently obtained. $^{16}$

Results that clearly show the first-order melting transi- tions in BSCCO for fields of 100-200 gauss are presented below. There is an excellent agreement with the results of our multilevel Monte Carlo simulations $^{15}$ including the pro liferation of nonsimple loops corresponding to flux entangle- ment above the melting transition.

At this point we should briefly discuss some previous ap- plications of MD Langevin simulations for investigations of vortex-lattice phenomena. Wilkin and Jensen $^{21}$ used Lange vin dynamics to investigate the melting transition in the pres- ence of point disorder in layered superconductors. However they used the nonrealistic Gaussian potential among pancake vortices instead of the actual long-ranged logarithmic inter-actions derived by Clem $^{9}$ and Artemenko and Kruglov. $^{11}$  They observed a signature of a first-order transition that dis- appear completely when the disorder is strong.

van Otterlo et al. $^{22}$ used Langevin dynamics for the case of YBCO where flux lines rather than individual pancakes are the relevant dynamical variables. The electromagnetic interaction is taken only in plane and then there is the bend- ing forces due to the line tension. The authors introduce point disorder and investigate the Bragg glass to vortex glass transition.

Olson et al. $^{23,24}$ use Langevin dynamics for pancake vor tices in BSCCO. However they take into account only the electromagnetic interaction and neglect the Josephson inter- action entirely, thus effectively using $\gamma=\infty$ . They also do not implement periodic boundary conditions in the $z$ direction, nor do they implement flux cutting and recombination. In- stead of varying the magnetic field they use an artificial pa- rameter $S_{m}$ that changes the relative strength of the in- and out-of-plane interactions. However varying this parameter away from unity makes the interaction of a single pancake with a straight stack of pancakes a distance $R$ away different from $K_{0}(R / \lambda).^{15}$ These authors are able to observe the de coupling transition of the superconducting planes that occurs at high magnetic fields. They also include the effects of point disorder and in addition they investigate the effect of a driv- ing force, like an electric current going through the sample.

Kolton et al. $^{25}$ use MD simulations at $T=0$ which are therefore not of the Langevin type. They implement periodic boundary conditions in all directions and include the full long-ranged electromagnetic interaction but neglect the Jo- sephson coupling. They study current driven pancakes in highly anisotropic superconductors.

Fangohr et al. $^{26}$ use both MD Langevin simulations and Monte Carlo to study the melting transition in highly aniso- tropic superconductors. As an alternative to including the full long-range electromagnetic interactions they use a mean- field approach in which the instantaneous density of pan- cakes in layers other than the currently simulated layer is replaced by an average density, thus leading to an effective "substrate potential,"27 that is adjusted self-consistently. These authors do not include the Josephson interaction. Note that our results for the case of infinite anisotropy as dis- cussed in the Sec. V and in Ref. 15 agree with the results of this paper.

## II. MODEL

The equation of motion for the $m$ th pancake vortex is
$$d \eta \frac{d \mathbf{R}_{m}}{d t}=-\nabla_{m} V\left(\left\{\mathbf{r}_{n}\right\}\right)+\mathbf{f}_{L}+\boldsymbol{\zeta}_{m}(t).\qquad(2.1)$$

The pancake label $m$ stands actually for two indices $(i, p)$  where $p$ is the plane label and $i$ is the pancake label in that plane. The position $R_{m}$ is a two component vector in the plane. Here we have used the over-damped model for vortex motion in which the velocity of the vortex is proportional to the applied force and $\eta$ is the viscous drag coefficient per unit length given by the Bardeen-Stephen $^{28}$ expression
$$\eta=\frac{\phi_{0} H_{c 2}}{\rho_{n} c^{2}},\qquad(2.2)$$
with $\rho_{n}$ the normal-state resistivity, $d$ is the interlayer spacing between $CuO_{2}$ planes that is taken to be equal to the width of the pancake vortex, and $V$ is the potential energy depending on the position of all pancakes and includes both the mag- netic energy and Josephson energy. The force is minus the gradient of the potential energy with respect to the position of the $m$ th pancake. $f_{L}$ is a driving force (if present), for example, the Lorentz force induced by a current. $\zeta_{m}$ is a white thermal noise term which satisfies
$$\left\langle\zeta_{m}^{\alpha}(t) \zeta_{n}^{\beta}\left(t^{\prime}\right)\right\rangle=2 k T \eta d \delta_{\alpha \beta} \delta_{m n} \delta\left(t-t^{\prime}\right).\qquad(2.3)$$

In Eq. (2.3) $\alpha$ and $\beta$ refer to the $x$ and $y$ components of the vector $\zeta$ and $m$ and $n$ are pancake labels. $k$ is Boltzmann's constant. In our simulations we measure distances in units of $a_{0}=\sqrt{2 \phi_{0} / B \sqrt{3}}$ where $B$ is the magnetic field. We measure energy in units of $\epsilon_{0} d$ where $\epsilon_{0}(T)=(\phi_{0} / 4 \pi \lambda)^{2}$ is the basic energy scale per unit length and $\lambda$ is the penetration depth. We measure time in units of $\eta a_{0}^{2} / \epsilon_{0}$ . Putting

$$
\begin{gathered}
\mathbf{R}_{m}=a_{0} \tilde{\mathbf{R}}_{m}, \quad t=\left(\frac{\eta a_{0}^{2}}{\epsilon_{0}}\right) \tilde{t}, \quad \nabla=a_{0}^{-1} \tilde{\nabla}, \quad V=\left(\epsilon_{0} d\right) \tilde{V}, \\
\mathbf{f}_{L}=\left(\epsilon_{0} d / a_{0}\right) \tilde{\mathbf{f}}_{L}, \quad \boldsymbol{\zeta}_{m}=\left(\epsilon_{0} d / a_{0}\right) \tilde{\boldsymbol{\zeta}}_{m}, \quad k T=\left(\epsilon_{0} d\right) \tilde{T},
\end{gathered}
$$
(2.4)

we obtain

$$
\frac{d \tilde{\mathbf{R}}_{m}}{d \tilde{t}}=-\tilde{\nabla}_{m} \tilde{V}\left(\left\{\tilde{\mathbf{r}}_{n}\right\}\right)+\tilde{\mathbf{f}}_{L}+\tilde{\boldsymbol{\zeta}}_{m}(\tilde{t})
\tag{2.5}
$$

with

$$
\left\langle\tilde{\zeta}_{m}^{\alpha}(\tilde{t}) \tilde{\zeta}_{n}^{\beta}\left(\tilde{t}^{\prime}\right)\right\rangle=2 \tilde{T} \delta_{\alpha \beta} \delta_{m n} \delta\left(\tilde{t}-\tilde{t}^{\prime}\right).
\tag{2.6}
$$

In the simulation we take $\tilde{t}$ to be discreet with an increment $\Delta \tilde{t}$. Thus instead of the Dirac delta function $\delta(\tilde{t})$ we take a function which is zero everywhere except when $\tilde{t}=0$, in which case it is $1 / \Delta \tilde{t}$. Thus we take

$$
\tilde{\zeta}_{m}^{\alpha}(\tilde{t})=\sqrt{2 \tilde{T} / \Delta \tilde{t}} \chi_{m}^{\alpha}(\tilde{t}),
\tag{2.7}
$$

where $\chi$ is a normally distributed random number with zero mean and unit variance.

To give an example of the magnitude of the various units used we quote their values for $T=60 \mathrm{~K}$ and $B=100 \mathrm{G}$. In that case we have $a_{0} \approx 4887 \AA, \epsilon_{0} d \approx 4.685 \times 10^{-14} \mathrm{erg}$ $\approx 339.5 \mathrm{~K} / \mathrm{k}$. Reference 29 quotes a value for $\eta$ for a single crystal BSCCO of around $1 \times 10^{-7} \mathrm{~g} /(\mathrm{cm} \mathrm{s})$. Based on this value the time unit is about $0.765 \mathrm{~ns}$. The value of the time unit is unimportant for the results of the present paper since we report on equilibrium properties.

We now discuss the expressions used for the various interactions and the methods used to implement periodic boundary conditions.

### A. Electromagnetic coupling

For the in-plane interaction between two pancakes one has, $^{2,3,9}$

$$
\frac{\mathbf{U}\left(R_{i j}, 0\right)}{\epsilon_{0} d}=2 \ln \frac{C}{R_{i j}}-\frac{d}{\lambda}\left(\ln \frac{C}{R_{i j}}-E_{1}\left(R_{i j}\right)\right),
\tag{2.8}
$$

where $R_{i j}=\left|\mathbf{R}_{i, p}-\mathbf{R}_{j, p}\right|$ is the radial distance in cylindrical coordinates. Here $\mathbf{R}$ is a two-dimensional vector with components $x$ and $y$.

The interaction between two pancakes $\left(\mathbf{R}_{i, p_{1}}, p_{1} d\right)$ and $\left(\mathbf{R}_{j, p_{2}}, p_{2} d\right)$ is given in the case when the pancakes are situated at different planes by

$$
\frac{\mathbf{U}\left(R_{i j}, z\right)}{\epsilon_{0} d}=-\frac{d}{\lambda}\left(\exp (-|z| / \lambda) \ln \frac{C}{R_{i j}}-E_{2}\left(R_{i j}, z\right)\right), \quad(2.9)
$$

where $R_{i j}=\left|\mathbf{R}_{i, p_{1}}-\mathbf{R}_{j, p_{2}}\right|$, and $z=\left(p_{1}-p_{2}\right) d$.

In the above equations we defined the residual interactions

$$
\begin{aligned}
& E_{1}\left(R_{i j}\right)=\int_{R_{i j}}^{\infty} d \rho \exp (-\rho / \lambda) / \rho, \\
& E_{2}\left(R_{i j}, z\right)=\int_{R_{i j}}^{\infty} d \rho \exp \left(-\sqrt{z^{2}+\rho^{2}} / \lambda\right) / \rho,
\end{aligned} \quad(2.10)
$$

$C$ is some unimportant constant that cancels out upon taking energy differences. We see that $E_{1}\left(R_{i j}\right)=E_{2}\left(R_{i j}, 0\right)$. This form of energy can be derived either by starting from the Lawrence-Doniach model $^{2,30}$ or by following Clem. $^{9}$

We choose our simulation cell to have a rectangular cross section of size $a_{0} \sqrt{N_{f l}} \times a_{0} \sqrt{3 N_{f l}} / 2$ where $N_{f l}$ is the number of flux lines (number of pancake vortices in each plane). We usually worked with 36 flux lines. The aspect ratio of the cell was chosen to accommodate a triangular lattice without distortion, such that each triangle is equilateral. In the $z$ direction we take $N_{p}$ layers of width $d$ each, where in practice we have chosen $N_{p}=36$.

We now discuss how to implement periodic boundary conditions (PBC) in all directions. Let us consider first the implementation of PBC in the $z$ direction and later we will implement PBC in the $x$ and $y$ directions. Periodic boundary conditions mean that every pancake interacts not only with the actual pancakes in the simulation cell but will all their images in other cells which are part of an infinite periodic array. Each image of a pancake is located at the same position in the corresponding cell as the original pancake in the simulation cell. Thus it is not a reflection through a boundary.

Let us start with the interaction of a pancake in a certain plane $p$ with another pancake in plane $p^{\prime}$. Because of the PBC in the $z$ direction it also interacts with all images of $p^{\prime}$ in positions $\left(p^{\prime}+N_{p} l\right) d$ where $l$ is an integer. Thus concerning the first term in Eq. (2.9) we have to evaluate the sum

$$
\begin{aligned}
f_{m}(\Delta p) & =\sum_{l=-\infty}^{\infty} \exp \left(-\left|\Delta p+N_{p} l\right| \mu\right) \\
& =\frac{\exp (-|\Delta p| \mu)+\exp (|\Delta p| \mu) \exp \left(-N_{p} \mu\right)}{1-\exp \left(-N_{p} \mu\right)},
\end{aligned}
$$

where we put $\Delta p=p-p^{\prime}$ and $\mu=d / \lambda$. The dependence of $f_{m}$ on $\Delta p$ is rather weak.

For the second term we have to evaluate the sum

$$
\begin{aligned}
& \sum_{l=-\infty}^{\infty} E_{2}\left(R,\left(\Delta p+N_{p} l\right) d\right) \\
& \quad=\int_{R / d}^{\infty} d y / y \sum_{l=-\infty}^{\infty} \exp \left(-\mu \sqrt{y^{2}+\left(\Delta p+N_{p} l\right)^{2}}\right).
\end{aligned}
$$

(2.12)

We now make the approximation, valid for the case when $d N_{p} \ll \lambda$ that the sum over $l$ can be replaced by an integral $\int_{-\infty}^{\infty} d l$. The estimated error is small for the range of parameters under consideration. Recall that for BSCCO, $\lambda(T)$ $=\lambda_{0} / \sqrt{\left(1-T / T_{c}\right)}$ and it is equal to $3000-5000 \AA$ for the


range of temperatures we work with, whereas $N_p d \approx 500$ Å for the value $N_p$=36 that has been used in the simulations. Changing variables from $l$ to $x=\Delta p + N_p l$ we find

$$
\begin{aligned}
\sum_{l=-\infty}^{\infty} & E_{2}\left(R,\left(\Delta p+N_{p} l\right) d\right) \\
& \approx \frac{1}{N_{p}} \int_{R / l d}^{\infty} \frac{d y}{y} \int_{-\infty}^{\infty} d x \exp \left(-\mu \sqrt{x^{2}+y^{2}}\right). \quad(2.13)
\end{aligned}
$$

We can now change variables from rectangular $(x,y)$ to polar $(\rho,\theta)$ to get

$$
\frac{1}{N_{p}} \int_{0}^{\pi} \frac{d \theta}{\sin \theta} \int_{R /(d \sin \theta)}^{\infty} d \rho \exp (-\mu \rho)=\quad (2.14)
$$

$$
\frac{2 \lambda}{d N_{p}} \int_{0}^{\pi / 2} \frac{d \theta}{\sin \theta} \exp \left(-\frac{R}{\lambda \sin \theta}\right)=\frac{2 \lambda}{d N_{p}} K_{0}\left(\frac{R}{\lambda}\right), \quad(2.15)
$$

with $K_0$ being the modified Bessel function of the second kind of zeroth order. The last integral was calculated by using the change of variable $z=1/\sin\theta$ and then referring to formula 3.384/3 in Ref. 38. Thus the total contribution to the out-of-plane pair interaction becomes

$$
\frac{U(R, \Delta p \neq 0)}{\epsilon_{0} d} \approx \frac{d}{\lambda}\left[\frac{2 \lambda}{d N_{p}} K_{0}\left(\frac{R}{\lambda}\right)-f_{m}(\Delta p) \ln \left(\frac{C}{R}\right)\right].
$$

It can be checked that to leading order

$$
f_{m}(\Delta p)=\frac{2 \lambda}{N_{p} d}\left[1+O\left(\frac{N_{p}^{2} d^{2}}{\lambda^{2}}\right)\right],\quad (2.17)
$$

since $|\Delta p|<N_p$. As $R\rightarrow0$, $K_0(R/\lambda)\approx\ln(\lambda/R)+$const. Thus requiring that the energy to be finite in the limit $R\rightarrow0$ we replace the prefactor of $K_0$ by $f_m(\Delta p)$, where the difference involves only higher order terms, and the correct limits are obtained both when $R$ is small and in the limit when $R$ is large and $K_0(R/\lambda)$ tends to zero. Thus Eq. (2.16) is replaced by.

$$
\frac{U(R, \Delta p \neq 0)}{\epsilon_{0} d} \approx \frac{d}{\lambda} f_{m}(\Delta p)\left[K_{0}\left(\frac{R}{\lambda}\right)-\ln \left(\frac{C}{R}\right)\right].
$$

We now turn to the interaction of pancakes in the same plane, again concentrating on one pancake, and its interaction with another in the same plane and all its images in other cells above or below a distance $dN_p l$ in the $z$ direction. For the images we must use the out-of-plane interaction. Thus apart from the $2\ln(C/R)$ term we have the same calculation as above with only difference is that now $\Delta p$=0. Thus we get

$$
\frac{U(R, 0)}{\epsilon_{0} d} \approx 2 \ln \left(\frac{C}{R}\right)+\frac{d}{\lambda} f_{m}(0)\left[K_{0}\left(\frac{R}{\lambda}\right)-\ln \left(\frac{C}{R}\right)\right].
$$

Let us check if we get the right answer for the case of one pancake interacting with a straight stack of pancakes a distance $R$ away. Summing all the pair interactions one obtains

$$
\frac{U(R)}{\epsilon_{0} d} \approx 2 \ln \left(\frac{C}{R}\right)+\frac{d}{\lambda} \sum_{\Delta p=0}^{N_{p}-1} f_{m}(\Delta p)\left[K_{0}\left(\frac{R}{\lambda}\right)-\ln \left(\frac{C}{R}\right)\right].
$$

Using the fact that

$$
\sum_{\Delta p=0}^{N_{p}-1} f_{m}(\Delta p) \approx \frac{2 \lambda}{d},\quad (2.21)
$$

one obtains

$$
\frac{U(R)}{\epsilon_{0} d} \approx 2 K_{0}\left(\frac{R}{\lambda}\right),\quad (2.22)
$$

which is the correct result for the interaction of a pancake with a straight infinite stack, see Appendix A in Ref. 15.

Consider also a straight stack of pancakes with one pancake from the stack displaced a distance $R$ away. The interaction of that pancake with the rest will be in this case

$$
\frac{U(R)}{\epsilon_{0} d} \approx 2\left[K_{0}\left(\frac{R}{\lambda}\right)-\ln \left(\frac{C}{R}\right)\right],\quad (2.23)
$$

to leading order (with correction of order $1/N_p$), which coincides with the result obtained by Clem⁹ provided $C$ is chosen appropriately so the energy vanishes as $R\rightarrow0$.

Thus far we only summed over images in the $z$ direction. We now have to implement the PBC in the transverse direction. In that case

$$
K_{0}(R / \lambda) \rightarrow G_{0}\left(\mathbf{R} / \lambda, L_{1} / \lambda\right),\quad (2.24)
$$

where the Green's function $G_0(\mathbf{R}/\lambda,L_1/\lambda)$ satisfies London's equation

$$
\left(1-\lambda^{2} \nabla^{2}\right) G_{0}\left(\mathbf{R} / \lambda, L_{1} / \lambda\right)=2 \pi \lambda^{2} \delta(\mathbf{R}) \quad(2.25)
$$

with PBC in the rectangular cell of dimensions $L_1\times L_2$ with $L_2=\sqrt{3}L_1/2$. Note that $G_0$ is not spherically symmetric. Also, in the case of $\lambda\rightarrow\infty$ one has to replace the logarithm by

$$
\ln (R / C) \rightarrow G_{0 C}\left(x / L_{1}, y / L_{2}\right),\quad (2.26)
$$

which satisfies PBC. Again the expression is derived in the Appendix. In this case an infinite constant independent of $\mathbf{R}$ has to be subtracted to make the expression finite. Our final expression for the pair energy with fully implemented PBC is

$$
\frac{U_{\text {mag }}(\mathbf{R}, \Delta p \neq 0)}{\epsilon_{0} d} \approx \frac{d}{\lambda} f_{m}(\Delta p)\left[G_{0}\left(\frac{\mathbf{R}}{\lambda}, \frac{L_{1}}{\lambda}\right)-G_{0 C}\left(\frac{x}{L_{1}}, \frac{y}{L_{2}}\right)\right],
$$

and similarly

$$
\begin{aligned}
\frac{U_{m a g}(\mathbf{R}, 0)}{\epsilon_{0} d} \approx & 2 G_{0 C}\left(\frac{x}{L_{1}}, \frac{y}{L_{2}}\right) \\
& +\frac{d}{\lambda} f_{m}(0)\left[G_{0}\left(\frac{\mathbf{R}}{\lambda}, \frac{L_{1}}{\lambda}\right)-G_{0 C}\left(\frac{x}{L_{1}}, \frac{y}{L_{2}}\right)\right].
\end{aligned}
$$
(2.28)

### B. Josephson interaction

In a recent paper $^{16}$ we derived an approximation to the Josephson interaction among pancakes in nearest neighbor planes. The approximation is based on a numerical solution of the nonlinear sine Gordon equation in two dimensions. A stringlike solution corresponding to a Josephson string that connects two singularities has been investigated and its energy calculated. It is believed that the derived formula constitutes a better approximation to the Josephson interaction than the one previously used. $^{19}$ The formula obtained for the Josephson interaction is
$$
\begin{aligned}
U_{\text {Josephson }}(R)= & \epsilon_{0} d[1.55+\ln (\lambda / d)] 0.25\left(R / r_{g}\right)^{2} \\
& \times \ln \left(9 r_{g} / R\right), \quad R \leqslant 2 r_{g} \\
= & \epsilon_{0} d[1.55+\ln (\lambda / d)]\left(\left(R / r_{g}\right)-0.5\right), \quad 2 r_{g}<R,
\end{aligned}
$$
(2.29)
where $R$ is the lateral separation of the pancakes and $r_{g}$ $=\gamma d$ where $\gamma$ is the anisotropy and $d$ is the interplane separation.

Since the Josephson interaction is between nearest neighbor pancakes in adjacent planes it is quite straight forward to implement PBC. A pancake at the top plane $\left(N_{p}\right)$ interacts with the closest pancake in the bottom plane 1 as well as with a pancake in plane $N_{p}-1$. When calculating the lateral distance between pancakes we always measure the "shortest distance" defined as follows: If the actual $|\Delta x|$ separation is larger than $L_{1} / 2$ we subtract or add $L_{1}$ depending on the sign of $\Delta x$, and similarly for $\Delta y$ with $L_{2}$ replacing $L_{1}$. This way the correct distance is obtained even when the adjacent pancake in the plane above has exited the simulation cell and emerged close to the other side of the simulation cell. This is because when a pancake exits the cell from one side it (or what was its image) enters the cell from the other side, so for the Josephson interaction, pancakes close to two distance boundaries can actually be neighbors.

In the case of $R \gg r_{g}$, string-string interactions that involve three- and four-body interactions become important. $^{29}$ However near the melting transition for the range of magnetic fields investigated in this paper $R \approx 0.25 a_{0} \approx 1000 \AA$ whereas $r_{g} \approx 5625 \AA$. Thus large transverse fluctuations for which the string-string interactions become important are statistically rare and can be neglected.

## III. DETAILS OF THE SIMULATIONS

The simulation cell is divided into a $800 \times 692$ mesh of small cells of area $\tilde{h} \times \tilde{h}$ each where $\tilde{h}=\sqrt{N_{f l}} / 800$ (in units of $a_{0}$ ), and we tabulate the functions $G_{0}$ and $G_{0 C}$ in each small cell thus creating two large $800 \times 692$ matrices. During the simulations we use the tables as a lookup to calculate the pair interaction. For each table we also calculate the negative of the gradient and save the two components of the gradient in their own tables. We also tabulate the Josephson interaction and its gradient. When simulating we allow pancakes to move to arbitrary real locations but in order to calculate the forces we divide the actual position by $\tilde{h}$ and round to the nearest integer to use for the lookup tables.

In each simulation step we move all the pancakes at the same time, using the instantaneous forces. This is done using a time step $\Delta \tilde{t}$. It is very important to chose the time step correctly. Consider the magnitude of the white thermal noise given in Eq. (2.7). On the average, the distance a pancake moves during a time $\Delta \tilde{t}$ is given by $\sqrt{2 \tilde{T} \Delta \tilde{t}}$. We choose this distance to be either $5 \tilde{h}$ or $8 \tilde{h}$ as explained below. We have used two methods: First we have employed a simple Euler method. For a given configuration of pancakes we calculate the force on each pancake due to the pair potential due all other pancakes, both magnetic and Josephson. To this force we add the constant driving force (if any) and the thermal noise. Based on these forces we move each and every pancake simultaneously (in parallel) by a distance given by the total force acting on it just before the move times $\Delta \tilde{t}$ $=(5 \tilde{h})^{2} /(2 \tilde{T})$. Then we calculate the new forces and repeat. At each step we generate the thermal noise by calling a Gaussian vector random number generator to obtain a vector of length $2 \times N_{f l} \times N_{p}$ filled with random numbers (total number of pancakes times two force components). The Euler method works adequately but is relatively slow since in order to get good results we needed to simulate up to a time span of 72 time units or more.

We found that we can improve performance by using a second-order Runge-Kutta method. We have tried to use a fourth-order method but there has been no further improvement over the second-order method for reasons that will be explained below. In the second-order method we use a larger time step of length $\Delta \tilde{t}=(8 \tilde{h})^{2} /(2 \tilde{T})$, which is about 2.6 larger than in the Euler method. In this method we first consider a virtual move of duration $\Delta \tilde{t} / 2$ with the initial instantaneous forces, we then calculate the new forces at the end of the virtual move, and we use these forces to move a full time step starting at the original initial position. The random noise is only generated once at the original point. Exactly the same random noise is used both for the virtual move and for the actual move. Thus the vector of random numbers is saved and used in the same order for the virtual and actual moves. Of course each move now takes about twice the cpu time than before, but we gain both because the results are more accurate and because we use a larger time step that reduces cpu time for the same total time span. In this method we could get reliable results in about half to two thirds the cpu time needed for Euler's method.

We believe that the reason we did not get an improvement with the fourth-order method is that in order to get a reduction in cpu time we need to increase the time step by at least a factor of two since each update move requires four evaluations of the forces instead of two. But for the same total time span this reduces the number of steps by at least a factor

of two. This interferes with the statistics of averaging over the thermal noise since the number of steps is not large enough to get good statistics so the results are actually not as good as the results from the second order method (for the same total time span).

It is a nice feature of multilevel Monte Carlo that one can implement flux cutting and permutations, $^{14,15,17,20}$ so that flux lines with PBC in the $z$ direction do not end on themselves but form loops that wind more than once across the system. We term such loops non-simple or "composite loops." For Bosons, the abundance of such loops characterizes the super- fluid phase. $^{20}$ They represent permutations of the particles that differ from the identity permutation. There is an approxi- mate mapping from the world lines of bosons propagating along the Euclidean time direction to FL's stretching along the $z$ direction. $^{17,31}$ For flux lines these composite loops rep resent the entangled state of the vortex liquid above the melt- ing transition. In order for this concept to exist one must not neglect the Josephson interactions even for a highly aniso- tropic material like BSCCO since it is the Josephson inter- actions that really tie up a stack of independent pancakes into a flux line even if loosely so, since this interaction is weak.

It is sometimes argued that one cannot implement permu- tations in a molecular dynamic simulation as the motion through permutation space is discrete and molecular dynam- ics involves continuous evolution. However in our situation it is quite possible to introduce "permutations" in our system and see that they proliferate above the melting transitions. In fact the results obtained for the number of loops not ending on themselves agree amazingly well with the corresponding results from our Monte Carlo simulations of the same sys- tem.

The way we implement "permutations" is through flux cutting and recombination. We assume that within the coupled-planes model, vortices may switch connections tolower their elastic energy (in this case Josephson energy) when they cross each other. $^{19}$ In the simulation we construct two matrices of size $N_{f l} \times N_{p}$ which we call the "up" matrix and the "down" matrix. For a given pancake $i$ in plane $p$ the "up" matrix points to the pancake in the plane $p+1$ (or 1 if $p=N_{p}$ ) that is connected to the given pancake $(i, p)$ via a Josephson interaction. Generally this is the pancake closest to the given pancake in the next plane. The "down" matrixsimilarly points to the closest pancake below (or in plane $N_{p}$  for $p=1$ ). When we start from an initial configuration in which the FL are a straight stack of pancake the matrices simply point to the pancake just above or below a given pancake. When constructing the force matrix after each time step we check if indeed the "up" matrix points to the closest pancake above. If there is a closer pancake than the one given by the pointer then we find out its parent in the plane p by using the down matrix, and we check if switching the two connections will decrease the sum of the squares of the two distances. If it does we cut and switch connections and update the "up" and "down" matrices. We term this precess an "exchange." The reason we use the square of the distances is that in most instances the Josephson interaction is propor-tional to the square of the transverse distance [see Eq. (2.29) above]. This procedure mimics the actual dynamics in which we expect the magnetic flux to choose a path that minimizes the Josephson energy. We implement the flux cutting proce- dure after every update move of the system, but not during the virtual half-step in the Runge-Kutta procedure.

Note that the extent that flux cutting and reconnecting occurs in real experimental samples and the existence of the entangled state is still a debatable issue. $^{32}$ Flux cutting can allow an entangled state to disentangle and vice versa. Our simulations show that just below the melting transition, even though some exchanges occur, they soon reverse themselves in space or in time, and thus they do not lead to what we refer to as an entangled state where composite loops or per- mutations are abundant. On the other hand when exchanges proliferate through the system, a phenomenon that occurs in our simulations just above the melting transition, the ex- changes do not undo each other, and the system of FL's changes from being composed of simple loops each made up of a single FL, to a system composed mainly of composite loops that wind up several times around the simulation cell in the $z$ direction before returning to the original point. The reason that the exchanges proliferate above the melting tran- sition is that the transverse fluctuations become strong enough to overcome the potential barriers due the repulsion among pancakes residing in the same plane and thus the crossing of FL's occur.

Crabtree and Nelson $^{33}$ give a rough back of the envelope estimate of the magnetic fields $B_{x 1}$ and $B_{x 2}$ such that when Bx1<B<Bx2 entanglement should occur in the flux liquid phase. For the system size and the values of parameters and field range that we use (100 G-300 G), we verified that in- deed the FL liquid should indeed be entangled. It should be noted that Wilkin and Jensen $^{21}$ measured flux cutting by sim ply observing the rate that the nearest neighbors of a given pancake in adjacent planes change during the course of a given time interval. In the liquid state many of those events occurred. However they did not implement "exchanges," nor did they keep track of composite loops and their relative abundance compared to simple loops as we do in our simu- lations.

## IV. MEASURED QUANTITIES

We measured the following physical quantities. For de-tails the reader is referred to our earlier work. $^{14,15}$

### A. Energy

The average energy was obtained by adding the electro- magnetic energy of all pairs of pancakes combined with the Josephson energy of nearest neighbor pancakes in adjacent planes.

### B. Translational structure factor

The translational structure factors $S(Q_{i})$ is defined as,
$$S\left(\mathbf{Q}_{i}\right)=\frac{1}{N_{p} N_{f l}^{2}}\left\langle\sum_{j k, p} e^{\left[i \mathbf{Q}_{i} \cdot\left(\mathbf{R}_{j, p}-\mathbf{R}_{k, p}\right)\right]}\right\rangle,\qquad(4.1)$$
where $\langle\cdots\rangle$ stands for the time average, and $Q_{i}, i=1,2$ stand for the basic reciprocal lattices vectors which are given by

$$
\mathbf{Q}_{i}=\frac{2 \pi}{a_{0} \sin ^{2} \theta}\left(\mathbf{e}_{i}-\mathbf{e}_{j} \cos \theta\right),
\tag{4.2}
$$

where $i,j=(1,2)$ or $(2,1)$, $\theta=\pi/3$, $a_0$ is the size of the unit cell of the triangular lattice and $\mathbf{e}_{1,2}$ are the unit vectors along the rhombic unit cell such that
$$
\mathbf{e}_{1} \cdot \mathbf{e}_{2}=\cos \theta.
\tag{4.3}
$$

Notice that we normalized the structure factor to unity instead of $N_{fl}$. We actually try different orientations of $\mathbf{e}_{1}$ to allow for situations that the lattice unit cell does not align with the simulation cell and numerically find the angle for which the average $[S(\mathbf{Q}_{1})+S(\mathbf{Q}_{2})]/2$ is maximal. We then record this value as the measure of translational order.

### C. Mean square deviations

For each individual flux-line we define the position of the lateral center of mass as $\mathbf{R}_{\mathrm{CN}}=\Sigma \mathbf{R}_{(i,p)}/N_p$ where the sum goes over all the pancake belonging to it. We then define the mean square deviations as
$$
R_{f}^{2}=\left\langle\sum\left[\mathbf{R}_{(i,p)}-\mathbf{R}_{\mathrm{CM}}\right]^{2}\right\rangle,
\tag{4.4}
$$
where the sum is over all pancakes belonging to an individual flux line and the average is over all flux lines of the system and then taking a time average. The melting transition is expected to occur when this quantity satisfies
$$
R_{f}/a_{0} \geqslant c_{L},
\tag{4.5}
$$
where $c_L$ is the Lindemann coefficient.

### D. Line entanglement

As we allow for flux cutting and recombination, we can define the number $N_e/N_{fl}$ as that fraction of the total number of FL's which belong to loops that are bigger than the size of a "simple" loop. A simple loop is defined as a set of $N_p$ beads connected end to end (due to the periodic boundary conditions in the $z$ direction), $N_p$ being the total number of planes. Loops of size $2N_p, 3N_p,\dots$, start proliferating at and above the melting temperature.

### E. Parameters

Parameters for BSCCO were taken as follows: $\lambda_0$ $=1700$ Å, $d=15$ Å, and $T_c=90$ K. The temperature dependence of $\lambda$ in this work was taken to follow the Ginzburg-Landau convention $\lambda^{2}(T)=\lambda_{0}^{2}/(1-T/T_{c})$. See discussion in Ref. 15 on the agreement of this choice with experiments. For the anisotropy we have used values of 250-400.

## V. RESULTS

In this section we display some of the results for the melting transition obtained with the molecular dynamics method. The case of $B=100$ gauss and $\gamma=400$ is depicted in Fig. 1. In Fig. 1(a) we see the decay of the normalized structure factor. The melting temperature is about 69 K (corresponding to a reduced temperature of 300 K). In Fig. 1(b) we observe the quantity $R_{f}^{2}$ defined above that measures the square of the transverse deviations from a straight line. We see that at the transition the Lindemann parameter $c_L$ is about 0.25 (its square is about 0.06). In Fig. 1(c) we observe that composite loops corresponding to line entanglement start to proliferate above the melting transitions. In Fig. 1(d) we show the jump in the Josephson energy corresponding to a first-order transition. There is a corresponding jump in the total energy that is more difficult to observe since it is fractionally smaller. The jumps are of course smoothened by fine size effects, i.e., the fact that we have 36 FL's and 36 planes for a total of 1296 pancake vortices.

![](./images/812143190818684928_1.jpg)

FIG. 1. Results for $\gamma=400$ and $B=100$ G. The following quantities are shown: (a) the translational structure factor normalized to unity; (b) the mean square transverse deviations about the FL's center of mass in units of $a_{0}^{2}$; (c) the fraction of composite loops as a measure of FL entanglement; and (d) Josephson energy per pancake in units of $\epsilon_{0}d$. The temperature is measured in kelvin and so is the reduced temperature $T/(1-T/T_{c})$.

The results agree with multilevel MC simulations carried by us and the fact that the fraction of nonsimple loops agrees with the MC shows that "permutations" were implemented faithfully in the MD simulations. Some of our previous MC results are given in Ref. 15. Note that in Ref. 15 we used a different approximation for the Josephson interaction as given by Ryu *et al.*¹⁹ and hence one has to adjust the values of the anisotropies in Ref. 15 by about 1.5 to correspond to the current simulation which treats the Josephson interaction according to the approximation given in Ref. 16. More recent MC are presented in Ref. 34 which uses the current scheme.

In the MC simulations we investigated the finite size effects in more detail. We tried to increase the number of FL's to 64 instead of 36. We also simulated with the number of planes equal 25, 36, and 50. As the number of FL's and planes increase the transition becomes sharper but its position does not move by more than 1 K from its value for 36 FL's and 36 planes which we use in the current simulations. Our aim here is not to pinpoint the melting transition to a high accuracy but to have a simulation method that gives reasonable results, and can be the basis for simulations on

![](./images/812143190818684928_2.jpg)

FIG. 2. (Color online) Hysteresis loop displaying the structure factor for $\gamma$=400 and $B$=100 G. The direction of the heating and cooling cycle is indicated by arrows. The temperature is changed by 0.5 K increments.

larger systems if one needs to obtain better precision. The equilibration times in the MD simulation were chosen to give a good agreement with the MC simulations. We also ob- served that if the equilibration time is not long enough the melting appears gradual. By increasing the simulation time the transition becomes sharper up to a point when increasing the equilibration time further has no noticeable affect on the results. That is how we fixed the equilibration time. Usually it corresponds to at least 10 000 MD moves (in each move all the pancakes are moved at once) out of which 5000 moves are discarded before the measurement process begins.

Since the melting transition is a first-order transition we expect hysteresis effects if we perform a heating and cooling cycle. The hysteresis should be enhanced by the fact that the FL's in the liquid phase are entangled and it takes consider- able time for them to disentangle. Most of our simulations were done on a parallel machine where at each temperature we start from an ordered vortex configuration. However, in order to observe the hysteresis we carried out a heating and cooling cycle at 0.5 K increments where at each temperature we started from the last configuration obtained in the previ- ous temperature. We simulated for 72 time units at each tem- perature. The results for $B$=100 G and $\gamma$=400 are depicted in Fig. 2.

In Fig. 3 we see the melting transition for $B$=200 G and as expected it occurs at lower temperature. From the figure one can read an approximate transition temperature of 63 K (corresponding to a reduced temperature of 210 K). To simu- late each point in the above figures took between 12-24 pro- cessor hours on a 1 GHZ processor. Time spans were be- tween 72-108 time units (in the units discussed in Sec. II above), and about half of this time was discarded for equili- bration and half used for measurements. The cpu times are larger by a of factors of 2-3 compared with the correspond- ing times in our multilevel MC simulations because of the need to calculate all of the forces, not just the energies. how- ever since this method can be used to implement real dynam- ics in addition to the measurement of equilibrium properties only as done in MC simulations, the extra time can certainly be tolerated.

![](./images/812143190818684928_3.jpg)

FIG. 3. Results for $\gamma$=400 and $B$=200 G. The same quantities are shown as in Fig. 1.

In Fig. 4 we display the simulation results for $\gamma$=400 and $\gamma$=$\infty$ (no Josephson coupling) as compared to the experi- mental results of Majer et al. $^{35}$ For a more complete phase diagram obtained using the MC method for different values of the anisotropy parameter and more values of the $B$ field see Ref. 15. Notice that although we have chosen $\gamma$=400 in order that the melting temperature for $B$=150 G will roughly agree with experimental results, $^{35,36}$ the simulated melting curve is steeper than the observed experimental melting curve in pristine systems. This has been observed and dis- cussed before. $^{15}$ We should remember that experimental pris tine systems always include a certain amount of point defects that tend to reduce the melting temperature. The effective-

![](./images/812143190818684928_4.jpg)

FIG. 4. (Color online) Phase diagram showing the MD simula- tion results for $\gamma$=400 (circles), the MD simulation results for $\gamma$=$\infty$ with no Josephson coupling (triangles), and the experimental results (squares) of Ref. 35.

ness of these defects increases when the temperature is decreased and this causes the melting curve to flatten down in the experimental curves of the phase boundary in the $B$-$T$ plane as compared with the theoretical results for a defect free system. The experimental “irreversibility line” which lies just below the melting line is steeper and agrees better with the simulations. In Ref. 15 we also showed that when the Josephson interaction is present the data for the melting line for different anisotropies collapses onto a single straight line when $\ln(B\gamma^{2})$ is plotted versus $\ln(kT/\epsilon_{0}d)$. This confirms a prediction of Koshelev$^{37}$ that when the Josephson interaction is important the phase boundary is given by a single dimensionless function of the dimensionless parameters $(kT/\epsilon_{0}d)$ and $r_{g}/a_{0}^{2}\propto B\gamma^{2}$. For $\gamma=\infty$ our results are in agreement with Dodgson *et al.*$^{27}$ and scaling is obtained when plotting $B\lambda^{2}/\phi_{0}$ versus $kT/\epsilon_{0}d$.

## VI. CONCLUSIONS

In this paper we have shown that molecular dynamics is a powerful tool that can be used to obtain the properties of the melting transition in a similar way to multilevel MC simulations. We showed how to implement flux cutting and recombination and obtained results showing flux-line entanglement similar to those obtained by implementing permutations in the MC simulations. We have included both the electromagnetic interaction among all pancakes and the Josephson interaction among nearest neighbor pancakes in adjacent planes. We have implemented periodic boundary conditions in all directions.

Our next goal is to include defects, either in the form of columnar defects and/or point defects and to investigate steady-state, nonequilibrium properties of the system when a current is flowing.

## ACKNOWLEDGMENTS

This work is supported by the U.S. Department of Energy (DOE), Grant No. DE-FG02-98ER45686. Some of the simulations were done at the Pittsburgh Super Computer center under Grant No. DMR950009P. I thank Eduardo Cuansing for some useful discussions.

## APPENDIX: ENERGY SUM OVER THE IMAGES

Here unlike our previous papers we work with a rectangular simulation cell with edges of size $L_{1}$ and $L_{2}=L_{1}\sqrt{3}/2$.
The function $G_{0}$ is a solution to the London equation
$$(1-\lambda^{2}\nabla^{2})G_{0}(\mathbf{R},\lambda)=2\pi\lambda^{2}\delta(\mathbf{R}),\tag{A1}$$
with the parameter $\lambda$ (penetration depth) setting the scale for the range of the interaction. Periodic boundary conditions are to be satisfied in the $x$ and $y$ directions. The solution is given by
$$G_{0}(\mathbf{R},\lambda)=\frac{2\pi\lambda^{2}}{L_{1}L_{2}}\sum_{\mathbf{Q}}\frac{\exp(i\mathbf{Q}\cdot\mathbf{R})}{1+\lambda^{2}\mathbf{Q}^{2}},\tag{A2}$$
where $\mathbf{Q}=n_{1}(2\pi/L_{1})\hat{\mathbf{i}}+n_{2}(2\pi/L_{2})\hat{\mathbf{j}}$ is a reciprocal lattice vector and $n_{1}$ and $n_{2}$ are integers. The summation over $n_{1}$ can be done analytically using a well-known formula [see Gradshteyn and Ryzhik,$^{38}$ Eq. (1.445/2)]. We are left with one summation
$$
\begin{aligned}
G_{0}(\mathbf{R},\lambda)=&\frac{L_{1}}{L_{2}}\sum_{n=1}^{\infty}\frac{\cosh[\alpha_{n}(\pi-t_{1})]\cos(nt_{2})}{\alpha_{n}\sinh(\alpha_{n}\pi)}\\
&+\frac{L_{1}}{2L_{2}}\frac{\cosh[\alpha_{0}(\pi-t_{1})]}{\alpha_{0}\sinh(\alpha_{0}\pi)},
\end{aligned}\tag{A3}
$$
where we defined
$$\alpha_{n}=\frac{L_{1}}{L_{2}}\sqrt{n^{2}+\frac{L_{2}^{2}}{4\pi^{2}\lambda^{2}}},\quad t_{1}=\frac{2\pi x}{L_{1}},\quad t_{2}=\frac{2\pi y}{L_{2}},\tag{A4}$$
and $0\leqslant x\leqslant L_{1}$, $0\leqslant y\leqslant L_{2}$. We used this formula, and a similar one obtained by first summing over $n_{2}$, to calculate $G_{0}$ numerically for finite $\lambda$. In the limit $\lambda\rightarrow\infty$ we can obtain an equation for the “periodic logarithm.” In that limit we have $\alpha_{n}=nL_{1}/L_{2}$ but we see that the last term in Eq. (A3) diverges. The diverging term $L_{1}/(L_{2}2\pi\alpha_{0}^{2})$, is independent of the position $\mathbf{R}$ and can be subtracted out. The final expression for $G_{0C}$ is
$$
\begin{aligned}
G_{0C}\left(\frac{x}{L_{1}},\frac{y}{L_{2}}\right)=&\frac{L_{1}}{L_{2}}\sum_{n=1}^{\infty}\frac{\cosh[\alpha_{n}(\pi-t_{1})]\cos(nt_{2})}{\alpha_{n}\sinh(\alpha_{n}\pi)}\\
&+\frac{\pi L_{1}}{6L_{2}}\left(1-\frac{3t_{1}}{\pi}+\frac{3t_{1}^{2}}{2\pi^{2}}\right),
\end{aligned}\tag{A5}
$$
with $\alpha_{n}=nL_{1}/L_{2}$.

$^{1}$M. Tinkham in *Introduction to Superconductivity* (McGraw-Hill, New York, 1975).

$^{2}$G. Blatter, M. V. Feigel’man, V. B. Geshkenbein, A. I. Larkin, and V. M. Vinokur, Rev. Mod. Phys. **66**, 1125 (1994) and references therein.

$^{3}$E. H. Brandt, Rep. Prog. Phys. **58**, 1465 (1995).

$^{4}$H. Safar, P. L. Gammel, D. A. Huse, D. J. Bishop, J. P. Rice, and D. M. Ginsberg, Phys. Rev. Lett. **69**, 824 (1992).

$^{5}$W. K. Kwok, S. Fleshler, U. Welp, V. M. Vinokur, J. Downey, G. W. Crabtree, and M. M. Miller, Phys. Rev. Lett. **69**, 3370 (1992).

$^{6}$R. Cubitt, E. M. Forgan, G. Yang, S. L. Lee, D. M. Paul, H. M. Mook, M. Yethiraj, P. H. Kes, T. W. Li, A. A. Menovsky, Z. Tarnavski and K. Mortensen, Nature (London) **365**, 407 (1993).

$^{7}$E. Zeldov, D. Majer, M. Konczykowski, V. B. Geshkenbein, V. M. Vinokur, and H. Shtrikman, Nature (London) **375**, 373 (1995).

$^{8}$A. Schilling, R. A. Fisher, N. E. Phillips, U. Welp, D. Dasgupta, W. K. Kwok, and G. W. Crabtree, Nature (London) **382**, 791 (1996).

$^{9}$J. R. Clem, Phys. Rev. B 43, 7837 (1991).

$^{10}$J. R. Clem, J. Supercond. 17, 613 (2004).

$^{11}$S. N. Artemenko and A. N. Kruglov, Phys. Lett. A 143, 485 (1990).

$^{12}$J. R. Clem, M. W. Coffey, and Z. Hao, Phys. Rev. B 44, 2732 (1991).

$^{13}$A. E. Koshelev, Phys. Rev. B 48, 1180 (1993).

$^{14}$S. Tyagi and Y. Y. Goldschmidt, Phys. Rev. B 67, 214501 (2003).

$^{15}$S. Tyagi and Y. Y. Goldschmidt, Phys. Rev. B 70, 024501 (2004).

$^{16}$Y. Y. Goldschmidt and S. Tyagi, Phys. Rev. B 71, 014503 (2005)

$^{17}$H. Nordborg and G. Blatter, Phys. Rev. B 58, 14556 (1998).

$^{18}$M. B. Gaifullin, Y. Matsuda, N. Chikumoto, J. Shimoyama, and K. Kishio, Phys. Rev. Lett. 84, 2945 (2000).

$^{19}$S. Ryu, S. Doniach, G. Deutscher, and A. Kapitulnik, Phys. Rev. Lett. 68, 710 (1992); S. Ryu, Ph.D. thesis, Stanford University, 1995.

$^{20}$D. M. Ceperley, Rev. Mod. Phys. 67, 279 (1995).

$^{21}$N. K. Wilkin and H. J. Jensen, Phys. Rev. Lett. 79, 4254 (1997).

$^{22}$A. van Otterlo, R. T. Scalettar, and G. T. Zimanyi, Phys. Rev. Lett. 81, 1497 (1998).

$^{23}$C. J. Olson, G. T. Zimanyi, A. B. Kolton, and N. Gronbech-Jensen, Phys. Rev. Lett. 85, 5416 (2000).

$^{24}$C. J. Olson, C. Reichhardt, R. T. Scalettar, G. T. Zimanyi, and N. Gronbech-Jensen, Phys. Rev. B 67, 184523 (2003).

$^{25}$A. B. Kolton, D. Dominguez, C. J. Olson, and N. Gronbech-Jensen, Phys. Rev. B 62, R14657 (2000).

$^{26}$H. Fangohr, A. E. Koshelev, and M. J. W. Dodgson, Phys. Rev. B 67, 174508 (2003).

$^{27}$M. J. W. Dodgson, A. E. Koshelev, V. B. Geshkenbein, and G. Blatter, Phys. Rev. Lett. 84, 2698 (2000).

$^{28}$J. Bardeen and M. J. Stephen, Phys. Rev. 140, 1197A (1965).

$^{29}$L. N. Bulaevskii, J. H. Cho, M. P. Maley, P. Kes, Q. Li, M. Suenaga, and M. Ledvij, Phys. Rev. B 50, 3507 (1994).

$^{30}$W. E. Lawrence and S. Doniach, in *Proceedings of LT 12, Kyoto, 1970*, edited by E. Kanda (Keigaku, Tokyo, 1971), p. 361; S. Doniach, in *High Temperature Superconductivity, Proceedings*, edited by K. S. Bedell, D. Coffey, D. E. Meltzer, D. Pines, and J. R. Schrieffer (Addison-Wesley, Redwood City, 1989), p. 406.

$^{31}$D. R. Nelson, Phys. Rev. Lett. 60, 1973 (1988).

$^{32}$C. J. Olson Reichhardt and M. B. Hastings, Phys. Rev. Lett. 92, 157002 (2004).

$^{33}$G. W. Crabtree and D. R. Nelson, Phys. Today 50 (4), 38 (1997).

$^{34}$Y. Y. Goldschmidt and E. Cuansing, cond-mat/0506054 (unpublished).

$^{35}$D. Majer, E. Zeldov, and M. Konczykowski, Phys. Rev. Lett. 75, 1166 (1995).

$^{36}$S. S. Banerjee, A. Soibel, Y. Myasoedov, M. Rappaport, E. Zeldov, M. Menghini, Y. Fasano, F. de la Cruz, C. J. van der Beek, M. Konczykowski, and T. Tamegai, Phys. Rev. Lett. 90, 087004 (2003).

$^{37}$A. E. Koshelev, Phys. Rev. B B56, 11201 (1997).

$^{38}$I. S. Gradshteyn and I. M. Ryzhik, in *Table of Integrals, Series, and Products*, edited by Alan Jeffrey, 5th ed. (Academic Press, San Diego, 1994).