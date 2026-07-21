![](./images/812449694637621249_1.jpg)

Nuclear Physics B 625 [FS] (2002) 409-459

![](./images/812449694637621249_2.jpg)
www.elsevier.com/locate/npe

# Statistical mechanics of the self-gravitating gas: I. Thermodynamic limit and phase diagrams

## H.J. de Vega a,b, N. Sánchez c,d

a Laboratoire de Physique Théorique et Hautes Energies, Université Paris VI, Tour 16, 1er étage, 4, Place Jussieu 75252 Paris cedex 05, France
b Laboratoire Associé au CNRS UMR 7589, France
c Observatoire de Paris, Demirm, 61, avenue de l'Observatoire, 75014 Paris, France
d Laboratoire Associé au CNRS UA 336, Observatoire de Paris et École Normale Supérieure, France

Received 1 November 2001; accepted 14 January 2002

## Abstract
We provide a complete picture to the self-gravitating non-relativistic gas at thermal equilibrium using Monte Carlo simulations, analytic mean field methods (MF) and low density expansions. The system is shown to possess an infinite volume limit in the grand canonical (GCE), canonical (CE) and microcanonical (MCE) ensembles when $(N,V)\to\infty$, keeping $N/V^{1/3}$ fixed. We compute the equation of state (we do not assume it as is customary), as well as the energy, free energy, entropy, chemical potential, specific heats, compressibilities and speed of sound; we analyze their properties, signs and singularities. All physical quantities turn out to depend on a single variable $\eta\equiv\frac{Gm^{2}N}{V^{1/3}T}$ that is kept fixed in the $N\to\infty$ and $V\to\infty$ limit. The system is in a gaseous phase for $\eta<\eta_{T}$ and collapses into a dense object for $\eta>\eta_{T}$ in the CE with the pressure becoming large and negative. At $\eta\simeq\eta_{T}$ the isothermal compressibility diverges. This gravitational phase transition is associated to the Jeans' instability. Our Monte Carlo simulations yield $\eta_{T}\simeq1.515$. $PV/[NT]=f(\eta)$ and all physical magnitudes exhibit a square root branch point at $\eta=\eta_{C}>\eta_{T}$. The values of $\eta_{T}$ and $\eta_{C}$ change by a few percent with the geometry for large $N$: for spherical symmetry and $N=\infty$ (MF), we find $\eta_{C}=1.561764\dots$ while the Monte Carlo simulations for cubic geometry yields $\eta_{C}\simeq1.540$. In mean field and spherical symmetry $c_{V}$ diverges as $(\eta_{C}-\eta)^{-1/2}$ for $\eta\uparrow\eta_{C}$ while $c_{P}$ and $\kappa_{T}$ diverge as $(\eta_{0}-\eta)^{-1}$ for $\eta\uparrow\eta_{0}=1.51024\dots$ . The function $f(\eta)$ has a second Riemann sheet which is only physically realized in the MCE. In the MCE, the collapse phase transition takes place in this second sheet near $\eta_{MC}=1.26$ and the pressure and temperature are larger in the collapsed phase than in the gaseous phase. Both collapse phase transitions (in the CE and in the MCE) are of zeroth order since the Gibbs free energy has a jump at the transitions. The MF equation of state in a sphere, $f(\eta)$, obeys a first order non-linear differential equation of first kind Abel's type. The MF gives an

E-mail address: devega@lpthe.jussieu.fr (H.J. de Vega).

0550-3213/02/$ - see front matter © 2002 Elsevier Science B.V. All rights reserved.
PII: S0550-3213(02)00025-1

extremely accurate picture in agreement with the MC simulations both in the CE and MCE. Since we perform the MC simulations on a cubic geometry they describe an isothermal cube while the MF calculations describe an isothermal sphere. The local properties of the gas, scaling behaviour of the particle distribution and its fractal (Haussdorf) dimension are investigated in the companion paper quoted as paper II in the text: H.J. de Vega, N. Sánchez, astro-ph/0101567, next paper in this issue.
© 2002 Elsevier Science B.V. All rights reserved.

PACS: 64.10.+h; 04.40.-b; 05.45.Df; 05.70.Fh

## 1. Statistical mechanics of the self-gravitating gas

Physical systems at thermal equilibrium are usually homogeneous. This is the case for gases with short range intermolecular forces (and in absence of external fields). In such cases the entropy is maximum when the system homogenizes.

When long range interactions as the gravitational force are present, even the ground state is inhomogeneous. In this case, each element of the substance is acted on by very strong forces due to distant particles of the gas. Hence, regions near to and far from the boundary of the volume occupied by the gas will be in very different conditions, and, as a result, the homogeneity of the gas is destroyed [2]. The state of maximal entropy for gravitational systems is inhomogeneous. This basic inhomogeneity suggested us that fractal structures can arise in a self-interacting gravitational gas [3–7].

The inhomogeneous character of the ground state for gravitational systems explains why the universe is not going towards a 'thermal death'. A 'thermal death' would mean that the universe evolves towards more and more homogeneity. This can only happen if the entropy is maximal for an homogeneous state. Instead, it is the opposite what happens, structures are formed in the universe through the action of the gravitational forces as time evolves.

Usual theorems in statistical mechanics break down for inhomogeneous ground states. For example, the specific heat may be negative in the microcanonical ensemble (not in the canonical ensemble where it is always positive) [2].

As is known, the thermodynamic limit for self-gravitating systems does not exist in its usual form ($N \to \infty$, $V \to \infty$, $N/V =$ fixed). The system collapses into a very dense phase which is determined by the short distance (non-gravitational) forces between the particles.

We instead find that the thermodynamic functions exist in the dilute limit

$$
N \to \infty, \quad V \to \infty, \quad \frac{N}{V^{1 / 3}}=\text { fixed, } \tag{1}
$$

where $V$ stands for the volume of the box containing the gas. In such a limit, the energy $E$, the free energy and the entropy turns to be extensive. That is, we find that they take the form of $N$ times a function of

$$
\eta=\frac{G m^{2} N}{L T} \quad \text { or } \quad \xi=\frac{E L}{G m^{2} N^{2}},
$$

where $\eta$ and $\xi$ are intensive variables. Namely, $\eta$ and $\xi$ stay finite when $N$ and $V \equiv L^{3}$ tend to infinite. $\eta$ is appropriate for the canonical ensemble and $\xi$ for the microcanonical ensemble. Physical magnitudes as the specific heat, speed of sound, chemical potential and compressibility only depend on $\eta$ or $\xi$. $\eta$ and $\xi$ as well as the ratio $N/L$ are therefore intensive magnitudes. The energy, the free energy, the Gibbs free energy and the entropy are of the form $N$ times a function of $\eta$. These functions of $\eta$ have a finite $N=\infty$ limit for fixed $\eta$ (once the ideal gas contributions are subtracted). Moreover, the dependence on $\eta$ in all these magnitudes express through a single universal function $f(\eta)$.

We study here and in the companion paper [1] (called paper II in what follows) the statistical mechanics of the self-gravitating gas. That is, our starting point is the partition function for non-relativistic particles interacting through their gravitational attraction in thermal equilibrium. We study the self-gravitating gas in the three ensembles: microcanonical (MCE), canonical (CE) and grand canonical (GCE). We performed calculations by three methods:

- By expanding the partition function through direct calculation in powers of $1/\xi$ and $\eta$ for the MCE and CE, respectively. These expressions apply in the dilute regime $(\xi \gg 1, \eta \ll 1)$ and become identical for both ensembles for $N \to \infty$. At $\eta=0=1/\xi$ we recover the ideal gas behaviour.
- By performing Monte Carlo simulations both in the MCE and in the CE. We found in this way that the self-gravitating gas collapses at a critical point which depends on the ensemble considered. As shown in Fig. 1 the collapse occurs first in the canonical ensemble (point T). The microcanonical ensemble exhibits a larger region of stability that ends at the point MC (Fig. 1). Notice that the physical magnitudes are identical in the common region of validity of both ensembles within the statistical error. Beyond the critical point T the system becomes suddenly extremely compact with a large negative pressure in the CE. Beyond the point MC in the MCE the pressure and the temperature increase suddenly and the gas collapses. The phase transitions at T and at MC are of zeroth order since the Gibbs free energy has discontinuities in both cases.
- By using the mean field approach we evaluate the partition function for large $N$. We do this computation in the grand canonical, canonical and microcanonical ensembles. In the three cases the partition function is expressed as a functional integral over a statistical weight which depends on the (continuous) particle density. These statistical weights are of the form of the exponential of an 'effective action' proportional to $N$. Therefore, the $N \to \infty$ limit follows by the saddle point method. The saddle point is a space dependent mean field showing the inhomogeneous character of the ground state. Corrections to the mean field are of the order $1/N$ and can be safely ignored for $N \gg 1$ except near the critical points. These mean field results turned out to be in excellent agreement with the Monte Carlo results and with the low density expansion.

We calculate the saddle point (mean field) for spherical symmetry and we obtain from it the various physical magnitudes (pressure, energy, entropy, free energy, specific heats, compressibilities, speed of sound and particle density). Furthermore, we compute the determinants of small fluctuations around the saddle point solution for spherical symmetry for the three statistical ensembles in paper II.

When any small fluctuation around the saddle point decreases the statistical weight in the functional integral, the saddle point is dominating the integral and the mean field approach is fully valid. In that case the determinant of small fluctuations is positive. A negative determinant of small fluctuations indicates that some fluctuations around the saddle point are increasing the statistical weight in the functional integral and hence the saddle point does not dominate the partition function. The mean field approach cannot be used when the determinant of small fluctuations is negative.

The zeroes of the small fluctuations determinant determine the position of the critical points for the three statistical ensembles. The Monte Carlo simulations for the CE and the MCE show that the self-gravitating gas collapses near the critical points obtained from mean field.

The saddle point solution is identical for the three statistical ensembles. This is not the case for the fluctuations around it. The presence of constraints in the CE (on the number of particles) and in the MCE (on the energy and the number of particles) changes the functional integral over the quadratic fluctuations with respect to the GCE.

The saddle point of the partition function turns out to coincide with the hydrostatic treatment of the self-gravitating gas [8–16]. (Usually known as the ‘isothermal sphere’ in the spherically symmetric case.)

Our Monte Carlo simulations are performed in a cubic geometry. The equilibrium configurations obtained in this manner can thus be called the ‘isothermal cube’.

We find for spherical symmetry: $\eta_{\mathrm{GC}}^{R}=0.797375 \ldots$, $\eta_{C}^{R}=2.517551 \ldots$ and $\eta_{\mathrm{MC}}^{R}=2.03085 \ldots$ The variable $\eta^{R}$ appropriate for a spherical symmetry is defined as $\eta^{R} \equiv \frac{G m^{2} N}{R T}=\eta(4 \pi / 3)^{1 / 3}=1.61199 \ldots \cdot \eta$.

The values of $\eta_{T}$ and $\eta_{C}$ change by a few percent with the geometry and with the number of particles (for large $N>500$ ). For spherical symmetry and $N=\infty$ (mean field) we obtain $\eta_{C}=(3 / 4 \pi)^{1 / 3} \eta_{C}^{R}=1.56176 \ldots$ Our Monte Carlo simulations yield $\eta_{T} \simeq 1.515$. We find from the mean field approach that the isothermal compressibility diverges at $\eta=\eta_{0}=1.51024 \ldots \simeq \eta_{T}$ for spherical symmetry. 2 The conclusion being that the MF correctly describes the thermodynamic limit except near the critical points (where the small fluctuations determinant vanishes); the MF is valid for $N\left|\eta-\eta_{\text {crit }}\right| \gg 1$. The vicinity of the critical point should be studied in a double scaling limit $N \rightarrow \infty, \eta \rightarrow \eta_{\text {crit }}$.

In summary, the picture we get from our calculations using these three methods show that the self-gravitating gas behaves as a perfect gas for $\eta \rightarrow 0,1 / \xi \rightarrow 0$. When $\eta$ and $1 / \xi$ grow, the gas becomes denser till it suddenly condenses into a high density object at a critical point GC, C or MC depending upon the statistical ensemble chosen. In the Monte Carlo simulations for the CE the collapse takes place at the point T slightly before $\eta_{C} . \eta$ is related with the Jeans' length $d_{\mathrm{J}}$ of the gas through $\eta=3\left(L / d_{\mathrm{J}}\right)^{2}$. Hence, when $\eta$ goes beyond $\eta_{T}$, the length of the system becomes larger than $d_{\mathrm{J}} / \sqrt{\eta_{T} / 3}$. The collapse at $\mathrm{T}$ in the CE is therefore a manifestation of the Jeans' instability. The saddle point ceases to describe the physics at $\mathrm{C}$ since the determinant of fluctuations for the $\mathrm{CE}$ vanishes there.

In the MCE, the determinant of fluctuations vanishes at the point MC. The physical states beyond MC are collapsed configurations shown by the Monte Carlo simulations (see Fig. 4). Actually, the gas collapses in the Monte Carlo simulations slightly before the mean field prediction for the point MC. The phase transition at the critical point MC is the so-called gravothermal catastrophe [12].

The gravitational interaction being attractive without lower bound, a short distance cut-off $(A)$ must be introduced in order to give a meaning to the partition function. We take the gravitational force between particles as $-Gm^2/r^2$ for $r > A$ and zero for $r < A$ where $r$ is the distance between the two particles. We show that the cut-off effects are negligible in the $N = \infty$ limit. That is, *once* we set $N = \infty$ with fixed $\eta$, *all* physical quantities are finite in the zero cut-off limit $(A = 0)$. The cut-off effects are of the order $A^2/L^2$ and can be safely ignored.

All physical quantities are expressed in terms of $f(\eta)$. Besides computing $f(\eta)$ numerically in the mean field approach, we obtain analytic results about it from the Abel's equation. There is a square root branch point in $f(\eta)$ at $\eta_C$. The specific heat is positive in the first sheet and negative in the second sheet. This second sheet is only physically realized in the microcanonical ensemble (MCE). (The specific heat is positive definite in the CE.) $f(\eta)$ has infinitely many branches in the $\eta$ plane but only the first two are physically realized. Beyond MC the states described by the mean field saddle point are unstable. We plot and analyze the equation of state, the energy, the entropy, the free energy, $c_V$, $c_P$, the isothermal compressibility and the speed of sound (Figs. 10-15). Most of these physical magnitudes were not previously computed in the literature as functions of $\eta$.

We find analytically the behaviour of $f(\eta)$ near $\eta_C$ in mean field,

$$
\begin{aligned}
f_{\mathrm{MF}}\left(\eta^{R}\right) \stackrel{\eta^{R} \uparrow \eta_{C}^{R}}{=} & \frac{1}{3}+0.213738 \ldots \cdot \sqrt{\eta_{C}^{R}-\eta^{R}} \\
& +0.172225 \ldots \cdot\left(\eta_{C}^{R}-\eta^{R}\right)+\mathcal{O}\left[\left(\eta_{C}^{R}-\eta^{R}\right)^{3 / 2}\right].
\end{aligned}
$$

This shows that the specific heat at constant volume diverges as $(\eta_C - \eta)^{-1/2}$ for $\eta^R \uparrow \eta_C^R$. The specific heat at constant pressure and the isothermal compressibility diverge at $\eta_0$ as $(\eta_0 - \eta)^{-1}$. These mean field results apply for $|\eta - \eta_C| \ll 1 \ll N|\eta - \eta_C|$. Fluctuations around mean field can be neglected in such a regime.

The Monte Carlo calculations permit us to obtain $f(\eta)$ in the collapsed phase. Such result (which is cut-off dependent) cannot be obtained in the mean field approach. The mean field only provides information (as $f(\eta)$) in the gas phase.

For the self-gravitating gas, we find that the Gibbs free energy $\Phi$ *is not* equal to $N$ times the chemical potential and that the thermodynamic potential $\Omega$ *is not* equal to $-PV$ as usual [2]. This is a consequence of the dilute thermodynamic limit $N \to \infty$, $L \to \infty$, $N/L =$ fixed.

We compute *local* properties of the gas in paper II. That is, the local energy density $\epsilon(r)$, local particle density and local pressure. Furthermore, we analyze the scaling behaviour of the particle distribution and its fractal (Haussdorf) dimension.

This paper is organized as follows. In Section 2 we present the statistical mechanics of the self-gravitating gas in the microcanonical ensemble, in Section 3 we do the analogous presentation for the canonical ensemble and in Section 4 we contrast the results for the CE and the MCE. Section 5 contains the results from Monte Carlo simulations and we develop in Section 6 the mean field approach. In Section 7 we present the results for intensive magnitudes. Discussion and remarks are presented in Section 8 whereas Appendices A-C contain relevant mathematical developments.

## 2. Statistical mechanics of the self-gravitating gas: the microcanonical ensemble

We investigate in this section an isolated set of $N$ non-relativistic particles with mass $m$ interacting through Newtonian gravity with total energy $E$. That is, a self-gravitating gas in the microcanonical ensemble. We assume the system being on a cubic box of side $L$ just for simplicity. We consider spherical symmetry in Section 6. Please notice that we never use periodic boundary conditions.

At short distances, the particle interaction for the self-gravitating gas in physical situations is not gravitational. Its exact nature depends on the problem under consideration (opacity limit, Van der Waals forces for molecules etc.). We shall just assume a repulsive short distance potential, that is,

$$
v_{A}\left(\left|\vec{q}_{l}-\vec{q}_{j}\right|\right)=-\frac{1}{\left|\vec{q}_{l}-\vec{q}_{j}\right|_{A}}= \begin{cases}-\frac{1}{\left|\vec{q}_{l}-\vec{q}_{j}\right|}, & \text { for }\left|\vec{q}_{l}-\vec{q}_{j}\right| \geqslant A, \\ +\frac{1}{A}, & \text { for }\left|\vec{q}_{l}-\vec{q}_{j}\right| \leqslant A,\end{cases}
\label{eq:2}
$$

where $A \ll L$ is the short distance cut-off.

The presence of the repulsive short-distance interaction prevents the collapse (here unphysical) of the self-gravitating gas. In the situations we are interested to describe (interstellar medium, galaxy distributions) the collapse situation is unphysical.

The entropy of the system can be written as

$$
S(E, N)=\log \left\{\frac{1}{N !} \int \cdots \int \prod_{l=1}^{N} \frac{d^{3} p_{l} d^{3} q_{l}}{(2 \pi)^{3}} \delta\left[E-\sum_{l=1}^{N} \frac{p_{l}^{2}}{2 m}-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right]\right\}, \quad (3)
$$

where

$$
U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)=-G m^{2} \sum_{1 \leqslant l<j \leqslant N} \frac{1}{\left|\vec{q}_{l}-\vec{q}_{j}\right|_{A}},
\label{eq:4}
$$

and $G$ is Newton's gravitational constant.

In order to compute the integrals over the momenta $p_{l}$ ($1 \leqslant l \leqslant N$), we introduce the variables,

$$
\vec{\rho}_{i}=\frac{1}{\sqrt{2 m}} \vec{p}_{i}.
$$

We can now integrate over the angles in $3N$ dimensions,

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} \cdots \int_{-\infty}^{+\infty} \prod_{l=1}^{N} \frac{d^{3} p_{l}}{(2 \pi)^{3}} \delta\left[E-\sum_{l=1}^{N} \vec{\rho}_{l}^{2}-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right] \\
& \quad=\left(\frac{\sqrt{2 m}}{2 \pi}\right)^{3 N} \frac{2 \pi^{3 N / 2}}{\Gamma(3 N / 2)} \int_{0}^{\infty} \rho^{3 N-1} d \rho \delta\left[E-\rho^{2}-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right] \\
& \quad=\left(\frac{m}{2 \pi}\right)^{3 N / 2} \frac{1}{\Gamma(3 N / 2)}\left[E-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right]^{3 N / 2-1} \theta\left[E-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right]. \quad (5)
\end{aligned}
$$
```

The delta function in the energy thus becomes the constraint of a positive kinetic energy $E - U(\vec{q}_1, \dots, \vec{q}_N) > 0$. We then get for the entropy,

$$
\begin{aligned}
S(E, N)=\log \Bigg\{ \frac{(m / 2 \pi)^{3 N / 2}}{N! \Gamma(3 N / 2)} & \int_{0}^{L} \cdots \int_{0}^{L} \prod_{l=1}^{N} d^{3} q_{l}\left[E-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right]^{3 N / 2-1} \\
& \left.\times \theta\left[E-U\left(\vec{q}_{1}, \ldots, \vec{q}_{N}\right)\right]\right\}.
\end{aligned} \tag{6}
$$

It is convenient to introduce the dimensionless variables $\vec{r}_l$, $1 \leqslant l \leqslant N$, making explicit the volume dependence as

$$
\vec{q}_{l}=L \vec{r}_{l}, \quad \vec{r}_{l}=\left(x_{l}, y_{l}, z_{l}\right), \quad 0 \leqslant x_{l}, y_{l}, z_{l} \leqslant 1. \tag{7}
$$

That is, in the new coordinates the gas is inside a cube of unit volume.

The entropy then becomes

$$
\begin{aligned}
S(E, N)=\log \Bigg\{ & \frac{N^{3 N-2} m^{9 N / 2-2} L^{3 N / 2+1} G^{3 N / 2-1}}{N! \Gamma(3 N / 2)(2 \pi)^{3 N / 2}} \\
& \times \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-1} \\
& \left.\times \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]\right\},
\end{aligned} \tag{8}
$$

where we introduced the dimensionless variable $\xi$,

$$
\xi \equiv \frac{E L}{G m^{2} N^{2}}, \tag{9}
$$

and

$$
u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right) \equiv \frac{1}{N} \sum_{1 \leqslant l<j \leqslant N} \frac{1}{\left|\vec{r}_{l}-\vec{r}_{j}\right|_{a}}, \tag{10}
$$

where $a \equiv A / L \ll 1$.

Let us define the coordinate partition function in the microcanonical ensemble as

$$
\begin{aligned}
w(\xi, N) \equiv \int_{0}^{1} \cdots \int_{0}^{1} & \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-1} \\
& \times \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right].
\end{aligned} \tag{11}
$$

Therefore,

$$
S(E, N)=\log \left[\frac{N^{3 N-2} m^{9 N / 2-2} L^{3 N / 2+1} G^{3 N / 2-1}}{N! \Gamma(3 N / 2)(2 \pi)^{3 N / 2}}\right]+\log w(\xi, N).
$$
```

We can now compute the thermodynamic quantities, temperature and pressure through the standard thermodynamic relations

$$
\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_{V} \quad \text { and } \quad p=T\left(\frac{\partial S}{\partial V}\right)_{E},
\tag{12}
$$

where $V \equiv L^{3}$ stands for the volume of the system and $p$ is the external pressure on the system.

We obtain the temperature as a function of $E$ and $\xi$ from Eqs. (8) and (12)

$$
\frac{1}{T}=\frac{\xi}{E} \frac{\partial}{\partial \xi} \log w(\xi, N)=\frac{3 N \xi}{2 E}\left[1-\frac{2}{3 N}\right]\left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle,
\tag{13}
$$

where

$$
\begin{aligned}
& \left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle \\
& \equiv \frac{\int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-2} \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]}{\int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-1} \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]} .
\end{aligned}
\tag{14}
$$

The equation of state follows from Eqs. (8) and (12)

$$
\begin{aligned}
\frac{p V}{N T} & =\frac{1}{2}+\frac{1}{3 N}+\frac{\xi}{3 N} \frac{\partial}{\partial \xi} \log w(\xi, N) \\
& =\frac{1}{2}\left(1+\frac{2}{3 N}\right)+\frac{\xi}{2}\left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle\left[1-\frac{2}{3 N}\right].
\end{aligned}
\tag{15}
$$

We are interested in the large size limit where $N \rightarrow \infty, L \rightarrow \infty$ and $E \rightarrow \infty$. We consider that $\xi=\frac{E L}{G m^{2} N^{2}}$ stays fixed in such limit. That is, we assume $E / N$ and $L / N$ bounded and non-zero when $E, L$ and $N \rightarrow \infty$. We shall see below that such limit is meaningful.

It is possible to write the energy and the equation of state in terms of a single function

$$
g(\xi) \equiv \frac{\xi}{N} \frac{\partial}{\partial \xi} \log w(\xi, N)=\frac{3 \xi}{2}\left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle\left[1-\frac{2}{3 N}\right].
\tag{16}
$$

We find from Eqs. (13), (15) and (16),

$$
\frac{p V}{N T}=\frac{1}{2}+\frac{1}{3} g(\xi)+\frac{1}{3 N}, \quad \frac{E}{N T}=g(\xi).
\tag{17}
$$

We obtain the virial theorem by eliminating $g(\xi)$ in Eq. (17)

$$
p V=\frac{N T}{2}+\frac{E+T}{3},
\tag{18}
$$

where the term $T / 3$ can be neglected for large $N$.

In the case of a perfect gas (no gravity) we have $u(\cdot) \equiv 0, g(\xi)=\frac{3}{2}, p V=N T$ and $E=\frac{3}{2} N T$ as it must be.

The function $g(\xi)$ is computed by Monte Carlo simulations, mean field methods and, in the weak field limit $\xi \ll 1$, is calculated analytically in powers of $1 / \xi$ in Section 2.1.

The specific heat per particle is given by

$$
c_{V}=\frac{T}{N}\left(\frac{\partial S}{\partial T}\right)_{V}=\frac{1}{N(\partial T / \partial E)_{V}}.
$$

Hence, using Eq. (17) yields

$$
c_{V}=\frac{g(\xi)}{1-\left(\xi g^{\prime}(\xi) / g(\xi)\right)} \quad \text { or } \quad \frac{1}{c_{V}}=\frac{d}{d \xi}\left[\frac{\xi}{g(\xi)}\right].
$$

We can relate the specific heat $c_{V}$ with the fluctuations as follows. We can express $g(\xi)$ as an average value using Eqs. (14) and (16)

$$
\begin{aligned}
\frac{\xi}{g(\xi)}= & \frac{2}{3-\frac{2}{N}} \\
& \times \frac{\int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-1} \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]}{\int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l}\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-2} \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]}.
\end{aligned}
$$

Computing the derivative with respect to $\xi$ yields,

$$
\frac{1}{c_{V}}=\frac{2}{3}-\frac{\left(\Delta \frac{1}{\xi+\frac{1}{N} u(\cdot)}\right)^{2}}{\left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle^{2}}+\mathcal{O}\left(\frac{1}{N}\right),
$$

where

$$
\left(\Delta \frac{1}{\xi+\frac{1}{N} u(\cdot)}\right)^{2} \equiv N\left\{\left\langle\frac{1}{\left[\xi+\frac{1}{N} u(\cdot)\right]^{2}}\right\rangle-\left\langle\frac{1}{\xi+\frac{1}{N} u(\cdot)}\right\rangle^{2}\right\},
$$

is of order $N^{0}$ for $N \rightarrow \infty$. (Notice that in the calculation of the fluctuations we must keep the $1 / N$ corrections till the end.)

We can express $c_{V}$ in terms of the fluctuations of the inverse temperature $\beta \equiv 1 / T$ using Eq. (13):

$$
\frac{1}{c_{V}}=\frac{2}{3}-\left(\frac{\Delta \beta}{\beta}\right)^{2}.
$$

It must be noticed that in the microcanonical ensemble, $c_{V}$ may be positive as well as negative. In fact, it becomes negative when the fluctuations are large enough (see Sections 5 and 6).

We see that extensivity holds here in an specific way. $T, S / N$ and $p V / N$ are of order one for $N \rightarrow \infty$ provided $\xi$ stays fixed in such limit. That is, we must keep $E / N$ and $L / N$ fixed in the $N \rightarrow \infty$ limit.

### 2.1. The diluted regime: $\xi \gg 1$

We can obtain the thermodynamic quantities as a series in powers of $1 / \xi$ just expanding the integrand in Eq. (11).

We find

$$
\begin{aligned}
w(\xi, N) & \stackrel{\xi \rightarrow \infty}{=} \xi^{3 N / 2-1}\left\{1+\frac{9 b_{0} N}{2 \xi}\left(1-\frac{2}{3 N}\right)\left(1-\frac{1}{N}\right)\right. \\
&+\frac{9}{8 \xi^{2}}\left(1-\frac{2}{3 N}\right)\left(1-\frac{4}{3 N}\right) \\
& \quad \times\left[9 N^{2} b_{0}^{2}\left(1-\frac{1}{N}\right)\left(1-\frac{2}{N}\right)\left(1-\frac{3}{N}\right)\right. \\
&\left.\left.\quad+N b_{1}\left(1-\frac{1}{N}\right)\left(1-\frac{2}{N}\right)+\frac{1}{2} b_{2}\left(1-\frac{1}{N}\right)\right]+\mathcal{O}\left(\xi^{-3}\right)\right\}
\end{aligned}
\label{eq21}
\tag{21}
$$

where $b_0$, $b_1$ and $b_2$ are pure numbers,

$$
\begin{aligned}
b_{0} &=\frac{1}{6} \int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|}, \\
b_{1} &=\int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2} d^{3} r_{3}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|\left|\vec{r}_{1}-\vec{r}_{3}\right|}, \\
b_{2} &=\int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|^{2}}.
\end{aligned}
\tag{22}
$$

For the cubic geometry chosen, it takes the value

$$
b_{0}^{\text {cube }}=\frac{4}{3} \int_{0}^{1}(1-x) d x \int_{0}^{1}(1-y) d y \int_{0}^{1} \frac{(1-z) d z}{\sqrt{x^{2}+y^{2}+z^{2}}}=0.31372 \ldots
$$

For a sphere of unit volume we find

$$
\begin{aligned}
b_{0}^{\text {sphere }} &=\frac{1}{5}\left(\frac{4 \pi}{3}\right)^{1 / 3}=0.32239839 \ldots, \\
b_{1}^{\text {sphere }} &=\frac{51}{35}\left(\frac{4 \pi}{3}\right)^{2 / 3}=3.786412026 \ldots, \\
b_{2}^{\text {sphere }} &=\frac{9}{4}\left(\frac{4 \pi}{3}\right)^{2 / 3}=5.846665629 \ldots.
\end{aligned}
\tag{23}
$$

We see that the coefficient $b_0$ for cubic and spherical geometries only differ by about $3\%$.

We thus find from Eq. (21) in the $N \to \infty$ limit

$$
\lim _{N \rightarrow \infty} \frac{1}{N} \log w(\xi, N)=\frac{3}{2} \log \xi+\frac{9 b_{0}}{2 \xi}+\frac{9}{8 \xi^{2}}\left(b_{1}-42 b_{0}^{2}\right)+\mathcal{O}\left(\xi^{-3}\right).
\tag{24}
$$

We considered here these integrals in the zero cut-off limit since $b_0$, $b_1$ and $b_2$ have finite zero cut-off limits. It is easy to see that their finite cut-off values behave as

$$
b_{0}(a)-b_{0}=\mathcal{O}\left(a^{2}\right), \quad b_{1}(a)-b_{1}=\mathcal{O}\left(a^{4}\right), \quad b_{2}(a)-b_{2}=\mathcal{O}(a).\qquad(25)
$$

Inserting Eq. (24) into Eq. (16) yields,

$$
g(\xi)=\frac{3}{2}-\frac{9 b_{0}}{2 \xi}-\frac{9}{4 \xi^{2}}\left(b_{1}-42 b_{0}^{2}\right)+\mathcal{O}\left(\xi^{-3}\right),\qquad(26)
$$

and

$$
\frac{p V}{N T}=1-\frac{3 b_{0}}{2 \xi}-\frac{3}{4 \xi^{2}}\left(b_{1}-42 b_{0}^{2}\right)+\mathcal{O}\left(\xi^{-3}\right).\qquad(27)
$$

We see that after letting $N \to \infty$ the zero cut-off limit is finite. We further discuss this important issue in the next section.

### 3. Statistical mechanics of the self-gravitating gas: the canonical ensemble

We investigate in this section the self-gravitating gas considered in the previous section but in thermal equilibrium at temperature $T \equiv \beta^{-1}$. That is, we work in the canonical ensemble where the system of $N$ particles is not isolated but in contact with a thermal bath at temperature $T$. We keep assuming the gas being on a cubic box of side $L$.

The partition function of the system can be written as

$$
\mathcal{Z}_{C}(N, T)=\frac{1}{N !} \int \cdots \int \prod_{l=1}^{N} \frac{d^{3} p_{l} d^{3} q_{l}}{(2 \pi)^{3}} e^{-\beta H_{N}},\qquad(28)
$$

where

$$
H_{N}=\sum_{l=1}^{N} \frac{p_{l}^{2}}{2 m}-G m^{2} \sum_{1 \leqslant l<j \leqslant N} \frac{1}{\left|\vec{q}_{l}-\vec{q}_{j}\right|_{A}},\qquad(29)
$$

$G$ is Newton's gravitational constant.

Computing the integrals over the momenta $p_{l}$ ($1 \leqslant l \leqslant N$)

$$
\int_{-\infty}^{+\infty} \frac{d^{3} p}{(2 \pi)^{3}} e^{-\frac{\beta p^{2}}{2 m}}=\left(\frac{m}{2 \pi \beta}\right)^{3 / 2},
$$

yields

$$
\mathcal{Z}_{C}(N, T)=\frac{1}{N !}\left(\frac{m}{2 \pi \beta}\right)^{3 N / 2} \int_{0}^{L} \cdots \int_{0}^{L} \prod_{l=1}^{N} d^{3} q_{l} e^{\beta G m^{2} \sum_{1 \leqslant l<j \leqslant N} \frac{1}{\left|\vec{q}_{l}-\vec{q}_{j}\right|_{A}}}.\qquad(30)
$$

We make now explicit the volume dependence introducing the variables $\vec{r}_{l}$, $1 \leqslant l \leqslant N$, defined in Eq. (7). The partition function takes then the form,

$$
\mathcal{Z}_{C}(N, T)=\frac{1}{N!}\left(\frac{m T L^{2}}{2 \pi}\right)^{3 N / 2} \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)},\qquad(31)
$$

where we introduced the dimensionless variable $\eta$

$$
\eta \equiv \frac{G m^{2} N}{L T},\qquad(32)
$$

and $u(\vec{r}_{1}, \ldots, \vec{r}_{N})$ is defined by Eq. (10). Recall that

$$
U \equiv-\frac{G m^{2} N}{L} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right),\qquad(33)
$$

is the potential energy of the gas.

The free energy takes then the form,

$$
F=-T \log \mathcal{Z}_{C}(N, T)=-N T \log \left[\frac{e V}{N}\left(\frac{m T}{2 \pi}\right)^{3 / 2}\right]-T \Phi_{N}(\eta),\qquad(34)
$$

where

$$
\Phi_{N}(\eta)=\log \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)}.\qquad(35)
$$

The derivative of the function $\Phi_{N}(\eta)$ will be computed by Monte Carlo simulations, mean field methods and, in the weak field limit $\eta \ll 1$, it will be calculated analytically.

We get for the pressure of the gas,

$$
p=-\left(\frac{\partial F}{\partial V}\right)_{T}=\frac{N T}{V}-\frac{\eta T}{3 V} \Phi_{N}^{\prime}(\eta).\qquad(36)
$$

(Here, $V \equiv L^{3}$ stands for the volume of the box and $p$ is the external pressure on the system.) We see from Eq. (35) that $\Phi_{N}(\eta)$ increases with $\eta$ since $u(\cdot)$ is positive. Therefore, the second term in Eq. (36) is a *negative* correction to the perfect gas pressure $\frac{N T}{V}$.

The mean value of the potential energy $U$ can be written from Eq. (33) as

$$
\langle U\rangle=-T \eta \Phi_{N}^{\prime}(\eta).\qquad(37)
$$

Combining Eqs. (36) and (37) yields the virial theorem,

$$
\frac{p V}{N T}=1+\frac{\langle U\rangle}{3 N T} \quad \text { or } \quad \frac{p V}{N T}=\frac{1}{2}+\frac{E}{3 N T},\qquad(38)
$$

where we use that the average value of the kinetic energy of the gas is $\frac{3}{2} N T$.

A more explicit form of the equation of state is

$$
\frac{p V}{N T}=1-\frac{\eta}{3 N} \Phi_{N}^{\prime}(\eta),\qquad(39)
$$

where

$$
\begin{aligned}
\Phi_{N}^{\prime}(\eta) & =e^{-\Phi_{N}(\eta)} \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right) e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)} \\
& =\frac{1}{2}(N-1) e^{-\Phi_{N}(\eta)} \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} \frac{1}{\left|\vec{r}_{1}-\vec{r}_{2}\right|_{a}} e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)}.
\end{aligned}
\tag{40}
$$

This formula indicates that $\Phi_{N}^{\prime}(\eta)$ is of order $N$ for large $N$. Monte Carlo simulations as well as analytic calculations for small $\eta$ show that this is indeed the case. In conclusion, we can write the equation of state of the self-gravitating gas as

$$
\frac{p V}{N T}=f(\eta),
\tag{41}
$$

where the function

$$
f(\eta) \equiv 1-\frac{\eta}{3 N} \Phi_{N}^{\prime}(\eta),
$$

is *independent* of $N$ for large $N$ and fixed $\eta$. (In practice, Monte Carlo simulations show that $f(\eta)$ is independent of $N$ for $N>100$.)

We get in addition,

$$
\langle U\rangle=-3 N T[1-f(\eta)].
\tag{42}
$$

In the dilute limit, $\eta \rightarrow 0$ and we find the perfect gas value

$$
f(0)=1.
$$

Equating Eqs. (39) and (41) yields,

$$
\Phi_{N}(\eta)=3 N \int_{0}^{\eta} d x \frac{1-f(x)}{x}.
$$

Relevant thermodynamic quantities can be expressed in terms of the function $f(\eta)$. We find for the free energy from Eq. (34),

$$
F=F_{0}-3 N T \int_{0}^{\eta} d x \frac{1-f(x)}{x},
\tag{43}
$$

where

$$
F_{0}=-N T \log \left[\frac{e V}{N}\left(\frac{m T}{2 \pi}\right)^{3 / 2}\right],
\tag{44}
$$

is the free energy for an ideal gas.

We find for the total energy $E$, chemical potential $\mu$ and entropy $S$ the following expressions,

$$
E=3 N T\left[f(\eta)-\frac{1}{2}\right],\tag{45}
$$

$$
\begin{aligned}
\mu & =\left(\frac{\partial F}{\partial N}\right)_{T, V} \\
& =-T \log \left[\frac{V}{N}\left(\frac{m T}{2 \pi}\right)^{3 / 2}\right]-3 T[1-f(\eta)]-3 T \int_{0}^{\eta} d x \frac{1-f(x)}{x},
\end{aligned}
$$

$$
S=-\left(\frac{\partial F}{\partial T}\right)_{V}=S_{0}+3 N\left[\int_{0}^{\eta} d x \frac{1-f(x)}{x}+f(\eta)-1\right],\tag{46}
$$

where
$$
S_{0}=-\frac{F_{0}}{T}+\frac{3}{2} N,
$$
is the entropy of the ideal gas.

Notice that here the Gibbs free energy

$$
\Phi=F+p V=F_{0}+N T\left[f(\eta)-3 \int_{0}^{\eta} d x \frac{1-f(x)}{x}\right],\tag{47}
$$

is not proportional to the chemical potential. That is, here $\Phi \neq \mu N$ and we have instead,

$$
\Phi-\mu N=2 N T[1-f(\eta)].\tag{48}
$$

This relationship differs from the customary one (see [2]) due to the fact that the dilute scaling relation $N \sim L$ holds here instead of the usual one $N \sim L^{3}$. The usual relationship is only recovered in the ideal gas limit $\eta=0$.

The specific heat at constant volume takes the form [2],

$$
c_{V}=\frac{T}{N}\left(\frac{\partial S}{\partial T}\right)_{V}=3\left[f(\eta)-\eta f^{\prime}(\eta)-\frac{1}{2}\right],\tag{49}
$$

where we used Eq. (46). This quantity is also related to the fluctuations of the potential energy $(\Delta U)^{2}$ and it is positive defined in the canonical ensemble,

$$
c_{V}=\frac{3}{2}+(\Delta U)^{2}.\tag{50}
$$

Here,
$$
(\Delta U)^{2} \equiv \frac{\left\langle U^{2}\right\rangle-\langle U\rangle^{2}}{N T^{2}}=3\left[f(\eta)-\eta f^{\prime}(\eta)-1\right].\tag{51}
$$

The specific heat at constant pressure is given by [2]

$$
c_{P}=c_{V}-\frac{T}{N} \frac{(\partial p / \partial T)_{V}^{2}}{(\partial p / \partial V)_{T}},\tag{52}
$$

and then,

$$
c_{P}=c_{V}+\frac{\left[f(\eta)-\eta f^{\prime}(\eta)\right]^{2}}{f(\eta)+\frac{1}{3} \eta f^{\prime}(\eta)}=-\frac{3}{2}+\frac{4 f(\eta)\left[f(\eta)-\eta f^{\prime}(\eta)\right]}{f(\eta)+\frac{1}{3} \eta f^{\prime}(\eta)}.\tag{53}
$$

The isothermal $(K_{T})$ and adiabatic $(K_{S})$ compressibilities take the form

$$
\begin{aligned}
& K_{T}=-\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{T}=\frac{V}{N T} \frac{1}{f(\eta)+\frac{1}{3} \eta f^{\prime}(\eta)}, \\
& K_{S}=-\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{S}=\frac{c_{V}}{c_{P}} K_{T}.
\end{aligned}\tag{54}
$$

It is then convenient to introduce the compressibilities

$$
\kappa_{T} \equiv \frac{N T}{V} K_{T}=\frac{1}{f(\eta)+\frac{1}{3} \eta f^{\prime}(\eta)} \quad \text { and } \quad \kappa_{S} \equiv \frac{N T}{V} K_{S}=\frac{c_{V}}{c_{P}} \kappa_{T},\tag{55}
$$

which are both of order one (intensive) in the $N, L \rightarrow \infty$ limit with $N / L$ fixed.

The speed of sound $v_{s}$ can be written as [18]

$$
v_{s}^{2}=-\frac{c_{P} V^{2}}{c_{V} N}\left(\frac{\partial p}{\partial V}\right)_{T}=\frac{V^{2}}{N}\left[\frac{T}{N c_{V}}\left(\frac{\partial p}{\partial T}\right)_{V}^{2}-\left(\frac{\partial p}{\partial V}\right)_{T}\right],\tag{56}
$$

where we used Eq. (52) in the last step. Therefore,

$$
\frac{v_{s}^{2}}{T}=\frac{\left[f(\eta)-\eta f^{\prime}(\eta)\right]^{2}}{3\left[f(\eta)-\eta f^{\prime}(\eta)-\frac{1}{2}\right]}+f(\eta)+\frac{1}{3} \eta f^{\prime}(\eta).\tag{57}
$$

The pressure $p$ used in this calculation corresponds to the pressure on the surface of the system. Hence, this is the speed of sound on the surface of the system, this is different from the speed of sound inside the volume since the ground state is inhomogeneous. We compute the speed of sound as a function of the point in paper II.

We see that the large $N$ limit of the self-gravitating gas is special. Energy, free energy and entropy are extensive magnitudes in the sense that they are proportional to the number of particles $N$ (for fixed $\eta$). They all depend on the variable $\eta=\frac{G m^{2} N}{L T}$ which is to be kept fixed for the thermodynamic limit $(N \rightarrow \infty$ and $V \rightarrow \infty)$ to exist. Notice that $\eta$ contains the ratio $N / L=N V^{-1 / 3}$ which must be considered here an intensive variable. Here, the presence of long-range gravitational situations calls for this new intensive variable in the thermodynamic limit.

In addition, all physical magnitudes can be expressed in terms of a single function of one variable: $f(\eta)$.

### 3.1. The diluted regime: $\eta \ll 1$

We can obtain the thermodynamic quantities as a series in powers of $\eta$ just expanding the exponent in the integrand of $\Phi_N(\eta)$ (Eq. (35)).

To first order in $\eta$ we get,
$$
\begin{aligned}
\Phi_{N}(\eta) &=\eta \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)+\mathcal{O}\left(\eta^{2}\right) \\
&=\frac{1}{2} \eta(N-1) \int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|_{a}}+\mathcal{O}\left(a^{2}\right)+\mathcal{O}\left(\eta^{2}\right) \\
&=3(N-1) b_{0} \eta+\mathcal{O}\left(\eta a^{2}\right)+\mathcal{O}\left(\eta^{2}\right),
\end{aligned}
\tag{58}
$$
where the coefficient $b_0$ is defined by Eq. (22).

To first order in $\eta$ we see that the cut-off effect is negligible $\sim \mathcal{O}(a^2)$ (see Eq. (25)).

To second order in $\eta$ we find from Eq. (35),
$$
\begin{aligned}
e^{\Phi_{N}(\eta)}= & \int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)} \\
= & 1+3(N-1) b_{0} \eta \\
& +\frac{\eta^{2}}{2 N^{2}}\left[\frac{N(N-1)(N-2)(N-3)}{4} \int \frac{d^{3} r_{1} d^{3} r_{2} d^{3} r_{3} d^{3} r_{4}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|\left|\vec{r}_{3}-\vec{r}_{4}\right|}\right. \\
& \quad+N(N-1)(N-2) \int \frac{d^{3} r_{1} d^{3} r_{2} d^{3} r_{3}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|\left|\vec{r}_{1}-\vec{r}_{3}\right|} \\
& \left.\quad+\frac{N(N-1)}{2} \int \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|^{2}}\right]+\mathcal{O}\left(\eta^{3}, \eta a^{2}, \eta^{2} a\right),
\end{aligned}
\tag{59}
$$
where the coefficients in front of the integrals count the number of combinations of particles yielding the same contribution. Using the notation defined by Eq. (22) we get
$$
\begin{aligned}
e^{\Phi_{N}(\eta)}=1 &+3(N-1) b_{0} \eta \\
+ & \eta^{2}\left[\frac{9(N-1)(N-2)(N-3)}{2 N} b_{0}^{2}\right. \\
& \left.\quad+\frac{(N-1)(N-2)}{2 N} b_{1}+\frac{(N-1)}{4 N} b_{2}\right]+\mathcal{O}\left(\eta^{3}, \eta a^{2}, \eta^{2} a\right).
\end{aligned}
\tag{60}
$$

Taking the log we get in the infinite $N$ limit
$$
\lim _{N \rightarrow \infty} \frac{1}{N} \Phi_{N}(\eta)=3 b_{0} \eta+\eta^{2}\left[\frac{1}{2} b_{1}-18 b_{0}^{2}\right]+\mathcal{O}\left(\eta^{3}\right),
$$
where we have now set $a=0$.

The cut-off effect is here again of order $\sim \mathcal{O}(a^2)$. It must be noticed that the coefficient $b_2$ which has the stronger dependence on the cut-off (see Eq. (25)) cancels out in the $N = \infty$ limit.

We therefore find in the low density and the large $N$ limit using Eqs. (39), (41) and (58):
$$
\frac{p V}{N T}=f(\eta)=1-b_{0} \eta-\eta^{2}\left[\frac{1}{3} b_{1}-12 b_{0}^{2}\right]+\mathcal{O}\left(\eta^{3}\right).
\tag{61}
$$

Furthermore, the speed of sound approaches for $\eta \to 0$ its perfect gas value,
$$
\frac{v_{s}^{2}}{T} \stackrel{\eta \downarrow 0}{=} \frac{5}{3}-\frac{4}{3} b_{0} \eta-\frac{5}{9} \eta^{2}\left[b_{1}-36 b_{0}^{2}\right]+\mathcal{O}\left(\eta^{3}\right),
$$
where we used Eqs. (57) and (61).

As we see, there are no divergent contributions in $\Phi_{N}(\eta)$ in the zero cut-off limit to the second order in $\eta$.

At order three a logarithmically divergent integral appears in $e^{\Phi_{N}(\eta)}$. Namely,
$$
\frac{\eta^{3}}{3! N^{3}} \frac{1}{2} N(N-1) \int \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|_{a}^{3}} \sim \frac{\eta^{3}}{N} \log a.
$$

This integral gives to $f(\eta)$ and the other physical magnitudes a contribution of the order
$$
\frac{\eta^{3}}{N^{2}} \log a.
$$

Therefore, such quantities can be safely neglected for $N \to \infty$ and fixed (small) $a$ since $f(\eta)$ is of order $N^{0}$ for $N \to \infty$.

More generally, to the $n$th order in $\eta$ and $n > 3$ the leading divergent contribution to $e^{\Phi_{N}(\eta)}$ for $a \to 0$ is of the form
$$
\frac{\eta^{n}}{n! N^{n}} \frac{1}{2} N(N-1) \int \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|_{a}^{n}} \sim \frac{\eta^{n}}{n! N^{n-2}} a^{3-n}.
$$

This gives to $f(\eta)$ and the other physical magnitudes a contribution of the order
$$
\frac{\eta^{n}}{n! N^{n-1}} a^{3-n}.
$$

As in the $n=3$ case, such contributions are negligible in the $N \to \infty$ limit since we take it at fixed (small) $a$.

## 4. Microcanonical vs. canonical ensembles

Let us compare the thermodynamical quantities computed in the microcanonical and canonical ensembles in the $N \to \infty$ limit keeping $\xi$ and $\eta$ fixed, respectively.

We consider here the dilute limit where we dispose of analytic expressions. The Monte Carlo and mean field results for the two ensembles will be compared in the next sections and in paper II.

In the dilute limit, we have the expressions (27) and (61) for the equation of state in the microcanonical and canonical ensembles, respectively. We want to know whether they are or not equivalent.

Let us start from the microcanonical equation of state (27). We have to express $\eta$ in terms of $\xi$ in order to compare with the canonical equation of state (61).

It follows from Eqs. (9), (17) and (32) that
$$
\eta=\frac{g(\xi)}{\xi}.
$$

Hence, for large $\xi$ and small $\eta$,
$$
\eta=\frac{3}{2 \xi}-\frac{9 b_{0}}{2 \xi^{2}}-\frac{9}{4 \xi^{3}}\left(b_{1}-42 b_{0}^{2}\right)+\mathcal{O}\left(\xi^{-4}\right),\qquad(62)
$$
and then
$$
\frac{1}{\xi}=\frac{2}{3} \eta\left[1+2 b_{0} \eta-2\left(10 b_{0}^{2}-\frac{1}{3} b_{1}\right) \eta^{2}+\mathcal{O}\left(\eta^{3}\right)\right].\qquad(63)
$$

One easily sees that inserting Eq. (63) in the microcanonical equation of state (27) yields the canonical equation of state (61) (up to $\mathcal{O}\left(\eta^{3}\right)=\mathcal{O}\left(\xi^{-3}\right)$).

Conversely, starting from the canonical ensemble, it follows from Eqs. (17), (45) and (61) that
$$
\frac{E}{N T}=g(\xi)=3\left[f(\eta)-\frac{1}{2}\right]=\frac{3}{2}-3 b_{0} \eta-\eta^{2}\left[b_{1}-36 b_{0}^{2}\right]+\mathcal{O}\left(\eta^{3}\right),\qquad(64)
$$
and
$$
\xi=\frac{3}{\eta}\left[f(\eta)-\frac{1}{2}\right]=\frac{3}{2 \eta}\left[1-2 b_{0} \eta-\frac{2}{3} \eta^{2}\left(b_{1}-36 b_{0}^{2}\right)+\mathcal{O}\left(\eta^{3}\right)\right].
$$

We see that this relation is identical to Eqs. (62) and (63) obtained in the microcanonical ensemble (up to $\mathcal{O}\left(\eta^{3}\right)=\mathcal{O}\left(\xi^{-3}\right)$).

Inserting now Eq. (62) into the canonical equation of state (61) yields the microcanonical equation of state (27) (up to $\mathcal{O}\left(\eta^{3}\right)=\mathcal{O}\left(\xi^{-3}\right)$).

One verifies in the same way that all thermodynamical quantities coincide to the same order in both ensembles.

In summary, the microcanonical and canonical ensembles yield the same results for $N \rightarrow \infty$ to the orders $\eta^{0}$, $\eta$ and $\eta^{2}$ (or equivalently $\xi^{0}$, $\xi^{-1}$ and $\xi^{-3}$).

## 5. Monte Carlo calculations

We have applied first the standard METROPOLIS algorithm [19] to the self-gravitating gas in a cube of size $L$ in the canonical ensemble at temperature $T$. We computed in this way the pressure, the energy, the average density, the potential energy fluctuations, the average particle distance and the average squared particle distance as functions of $\eta$. We implement the METROPOLIS algorithm changing at random the position of one particle chosen at random. The energy of the configurations is calculated performing the exact

sums as in Eq. (10). We used as statistical weight for the METROPOLIS algorithm in the canonical ensemble,

$$e^{\eta u\left(\vec{r}_{1},..., \vec{r}_{N}\right)},$$

which appears in the coordinate partition function (35).

The number of particles $N$ went up to 2000. We introduced a small short distance cut-off $A=10^{-4} L-10^{-8} L$ in the attractive Newton's potential according to Eq. (2). All results in the gaseous phase were insensitive to the cut-off value. The partition function calculation turns to be much less sensible to the short distance singularities of the gravitational force than Newton's equations of motion for $N$ particles. That is, solving the classical dynamics for $N$ particles interacting through gravitational forces as well as solving the Boltzman equation including the $N$-body gravitational interaction requires sophisticated algorithms to avoid excessively long computer times [17]. As is clear, solving the $N$-body classical evolution or the kinetic equations provides the time- dependent dynamics and out of thermal equilibrium effects which are out of the scope of our approach.

In the CE, two different phases show up: for $\eta<\eta_{T}$ we have a non-perfect gas and for $\eta>\eta_{T}$ it is a condensed system with negative pressure. The transition between the two phases is very sharp. This phase transition is associated with the Jeans instability.

A negative pressure indicates that the free energy grows for increasing volume at constant temperature (see Eq. (36)). Therefore, the system wants to contract sucking on the walls.

We plot in Figs. 1 and 2, $f(\eta)=p V /[N T]$ and $(\Delta U)^{2}$ as functions of $\eta$, respectively.

We find that for small $\eta$, the Monte Carlo results for $p V /[N T]$ well reproduce the analytical formula (61). $p V /[N T]$ monotonically decreases with $\eta$.

In the Monte Carlo simulations the phase transition to the condensed phase happens for $\eta=\eta_{T}$ slightly below $\eta_{C}$. For $N=2000$ we find $\eta_{T} \sim 1.515$. For $\eta_{T}<\eta<\eta_{C}$, the gaseous phase can only exist as a metastable state.

The average distance between particles $\langle r\rangle$ and the average squared distance between particles $\langle r^{2}\rangle$ monotonically decrease with $\eta$. When the gas collapses at $\eta_{T},\langle r\rangle$ and $\langle r^{2}\rangle$ exhibit a sharp decrease.

The values of $p V /[N T],\langle r\rangle$ and $\langle r^{2}\rangle$ in the condensed phase are independent of the cut-off for $a<10^{-5}$. The Monte Carlo results in this condensed phase can be approximated for $\eta>2$ as

$$
\frac{p V}{N T}=f(\eta) \simeq 1-K \eta, \quad\langle r\rangle \simeq 0.016,
\tag{65}
$$

where $K \simeq 14$.

Since $f(\eta)$ has a jump at the transition, the Gibbs free energy $\Phi$ is discontinuous and we have a phase transition of the zeroth order. We find from Eq. (47)

$$
\frac{\Phi(\text { collapse })-\Phi\left(\eta_{T}\right)}{N T}=f(\text { collapse })-f\left(\eta_{T}\right) \simeq-21<0.
\tag{66}
$$

![](./images/812449694637621249_3.jpg)

Fig. 1. $f(\eta^R) \equiv PV/[NT]$ as a function of $\eta^R$ by Monte Carlo simulations for the microcanonical and canonical ensembles ($N=2000$). Both curves coincide within the statistical error till the point T.

![](./images/812449694637621249_4.jpg)

Fig. 2. $(\Delta U)^2 \equiv \frac{\langle U^2 \rangle - \langle U \rangle^2}{NT^2} = 3[f(\eta) - \eta f'(\eta) - 1]$ as a function of $\eta$ in the gaseous phase from Monte Carlo simulations with 2000 particles in the canonical ensemble. Recall that $c_V = 3/2 + (\Delta U)^2$.

We can easily compute the latent heat of the transition per particle $(q)$ using the fact that the volume $V$ stays constant. Hence, $q=\Delta E/N$ and we obtain from Eq. (45)

$$
\begin{aligned}
\frac{q}{T} & =\frac{E(\text { collapse })-E\left(\eta_{T}\right)}{N T}=3\left[f(\text { collapse })-f\left(\eta_{T}\right)\right] \\
& \simeq 2-3 K \eta_{T} \simeq-62<0 .
\end{aligned}
$$

This phase transition is different from the usual phase transitions since the two phases cannot coexist in equilibrium as their pressures are different.

Eq. (65) can be understood from the general treatment in Section 3 as follows. We have from Eqs. (39) and (40)

$$
f(\eta)=1-\frac{\eta}{3}\left\langle\frac{1}{r}\right\rangle .
$$

The Monte Carlo results indicate that $\langle 1 / r\rangle \simeq 42$ is approximately constant in the collapsed region as well as $\langle r\rangle$ and $\left\langle r^{2}\right\rangle$. Eq. (65) thus follows from Eq. (68) using such value of $\langle 1 / r\rangle$.

The behaviour of $p V /[N T]$ near $\eta_{C}$ in the gaseous phase can be well reproduced by

$$
\frac{p V}{N T}=f(\eta) \stackrel{\eta \uparrow \eta_{C}}{=} f_{C}+A \sqrt{\eta_{C}-\eta},
$$

where $f_{C} \simeq 0.316, A \simeq 0.414$ and $\eta_{C} \simeq 1.540$.

In addition, the behaviour of $(\Delta U)^{2}$ in the same region is well reproduced by

$$
(\Delta U)^{2} \stackrel{\eta \uparrow \eta_{C}}{=} C+\frac{D}{\sqrt{\eta_{C}-\eta}},
$$

with $C \simeq-1.64$ and $D \simeq 0.901$. (Notice that for finite $N,(\Delta U)^{2}$ will be finite albeit very large at the phase transition.) Eq. (51) relating $f(\eta)$ and $(\Delta U)^{2}$ is satisfied with reasonable approximation.

We thus find a critical region just below $\eta_{C}$ where the energy fluctuations tend to infinity as $\eta \uparrow \eta_{C}$.

The point $\eta_{T}$ where the phase transition actually takes place in the Monte Carlo simulations is at $\eta_{T} \simeq 1.51<\eta_{C}$. This value for $\eta_{T}$ is close to the point $\eta_{0}$ where the isothermal compressibility $\kappa_{T}$ diverges (see Section 7). They are probably the same point.

Since Monte Carlo simulations are like real experiments, we conclude that the gaseous phase extends from $\eta=0$ till $\eta=\eta_{T}$ in the CE and not till $\eta=\eta_{C}$. Notice that in the literature based on the hydrostatic description of the self-gravitating gas [9,14-16], only the instability at $\eta=\eta_{C}$ is discussed whereas the singularities at $\eta=\eta_{0}$ are not considered.

We then performed Monte Carlo calculations in the microcanonical ensemble where the coordinate partition function is given by Eq. (11). We thus used

$$
\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right]^{3 N / 2-1} \theta\left[\xi+\frac{1}{N} u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)\right],
$$

as the statistical weight for the METROPOLIS algorithm.

The MCE and CE Monte Carlo results coincide up to the statistical error for $0<\eta<\eta_{T}$, that is for $\infty>\xi>\xi_{T} \simeq-0.19$. In the MCE the gas does not clump at $\eta=\eta_{C}$ (point C

in Fig. 1) and the specific heat becomes negative between the points C and MC. In the MCE the gas does clump at $\xi \simeq -0.52$, $\eta_{\text{MC}}^{T} \simeq 1.33$ (point MC in Fig. 1) increasing both its temperature and pressure discontinuously. We find from the Monte Carlo data that the temperature increases by a factor 2.4 whereas the pressure increases by a factor 3.6 when the gas clumps. The transition point $\eta_{\text{MC}}^{T}$ in the Monte Carlo simulations is slightly to the right of the critical point $\eta_{\text{MC}}$ predicted by mean field theory. The mean field yields for the sphere $\eta_{\text{MC}} = 1.2598\ldots$

In Ref. [24] finite $N$ corrections to the critical point $\eta_{\text{MC}}$ are computed in mean field for the sphere. This finite $N$ corrections shift $\eta_{\text{MC}}$ by $+3.3\%$ for $N=2000$. Since, $\eta_{\text{MC}}^{T}$ differs from $\eta_{\text{MC}}$ by $+5.6\%$, $\eta_{\text{MC}}^{T}$ and $\eta_{\text{MC}}$ are probably different critical points.

As is clear, the domain between C and MC cannot be reached in the CE since $c_{V}>0$ in the CE as shown by Eq. (50).

We find an excellent agreement between the Monte Carlo and mean field (MF) results (both in the MCE and CE). (This happens although the geometry for the MC calculation is cubic while it is spherical for the MF.) The points where the collapse phase transition occurs ($\eta_{T}$ and $\eta_{\text{MC}}^{T}$) slowly increase with the number of particles $N$.

We verified that the Monte Carlo results in the gaseous phase ($\eta < \eta_{T}$) are cut-off independent for $10^{-3} \geqslant a \geqslant 10^{-7}$.

As for the CE, the Gibbs free energy is discontinuous at the transition in the MCE. The transition is then of the zeroth order. We find from Eq. (47)
$$
\frac{\Phi(\text{collapse})-\Phi(\eta_{T})}{NT_{\text{gas}}}=\frac{T_{\text{coll}}}{T_{\text{gas}}}f(\text{collapse})-f(\eta_{T})\simeq 0.7>0,
$$
where we used the numerical values from the Monte Carlo simulations. Notice that the Gibbs free energy increases at the MC transition whereas it decreases at the C transition (see Eq. (66)).

Here again the two phases cannot coexist in equilibrium since their pressures and temperatures are different.

We display in Figs. 3 and 4 the average particle distribution from Monte Carlo simulations with 2000 particles in the microcanonical ensemble at both sides of the gravothermal catastrophe, i.e., $\eta = \eta_{\text{MC}}$. Fig. 3 corresponds to the gaseous phase and Fig. 4 to the collapsed phase. The inhomogeneous particle distribution is clear in Fig. 3 whereas Fig. 4 shows a dense collapsed core surrounded by a halo of particles.

The different nature of the collapse in the CE and in the MCE can be explained using the virial theorem (see Eq. (38))
$$
\frac{pV}{NT}=1+\frac{U}{NT}.
$$
When the gas collapses in the CE the particles get very close and $U$ becomes large and negative while $T$ is fixed. Therefore, $\frac{pV}{NT}$ may become large and negative as it does.

We can write the virial theorem also as,
$$
pV-\frac{1}{2}NT=\frac{1}{3}E.
$$
When the gas is near the point MC, $E<0$ is fixed and we have $T>0$. Therefore, $\frac{pV}{NT}$ as well as $U=E-3NT/2$ cannot become large and negative as in the CE collapse.

![](./images/812449694637621249_5.jpg)

Fig. 3. Average particle distribution in the gaseous phase from Monte Carlo simulations with 2000 particles in the microcanonical ensemble for $\xi=-0.5$, $\eta=1.38$, $pV/[NT]=0.277$. One particle denoted as $+$.

![](./images/812449694637621249_6.jpg)

Fig. 4. Average particle distribution in the collapsed phase from Monte Carlo simulations with 2000 particles in the microcanonical ensemble for $\xi=-0.6$, $\eta=0.43$, $pV/[NT]=0.414$. One particle denoted as $+$.

![](./images/812449694637621249_7.jpg)

Fig. 5. Average particle distribution in the gaseous phase from Monte Carlo simulations in the canonical ensemble for $\eta=1.5$ and $N=2000$. One particle denoted as +.

![](./images/812449694637621249_8.jpg)

Fig. 6. Average particle distribution in the collapsed phase from Monte Carlo simulations with 2000 particles in the canonical ensemble for $\eta=1.53$, $pV/[NT]=-14.44$. One particle denoted as +.

This prevents the distance between the particles to decrease. Actually, the Monte Carlo simulations show that $\langle r \rangle$ increases by 18% when the gas collapses in the MCE.

Figs. 5 and 6 depict the average particle distribution from Monte Carlo simulations with 2000 particles in the canonical ensemble at both sides of the collapse critical point, i.e., $\eta = \eta_C$. Fig. 5 corresponds to the gaseous phase and Fig. 6 to the collapsed phase. The inhomogeneous particle distribution is clear in Fig. 5 whereas Fig. 6 shows a dense collapsed core surrounded by a very little halo of particles.

Notice that the collapsed phases are of different nature in the CE and MCE. The core is much tighter and the halo much smaller in the CE than in the MCE.

Figs. 3 and 5 depict the average particle distribution for the gaseous phase in the MCE and the CE, respectively. In this phase, the MC simulations give identical descriptions for large $N$ in both ensembles. (This important point will be further demonstrated in Section 6 by functional integral methods.) The average configurations in Figs. 3 and 5 describe a self-gravitating gas in thermal equilibrium within a *cube*. We may call it the *isothermal cube* by analogy with the well-known isothermal sphere [10–16].

## 6. Mean field approach

Both in the microcanonical and the canonical ensembles the coordinate partition functions are given by $3N$-uple integrals (Eqs. (11) and (35), respectively). In the $N \to \infty$ limit both $3N$-uple integrals can be recasted as functional integrals over the continuous particle density as we see below.

### 6.1. The canonical ensemble

We now recast the coordinate partition function $e^{\Phi_N(\eta)}$ in the canonical ensemble given by Eq. (35) as a functional integral in the thermodynamic limit:

$$
e^{\Phi_N(\eta)} \stackrel{N \gg 1}{=} \iint D\rho \, d\hat{a} \, e^{-N s_C[\rho(\cdot),\hat{a},\eta]},
$$

$$
\begin{aligned}
s_C[\rho(\cdot), \hat{a}, \eta]= & -\frac{\eta}{2} \int \frac{d^3 x \, d^3 y}{|\vec{x}-\vec{y}|} \rho(\vec{x}) \rho(\vec{y})+\int d^3 x \, \rho(\vec{x}) \log \rho(\vec{x}) \\
& -i \hat{a}\left(\int d^3 x \, \rho(\vec{x})-1\right),
\end{aligned}
$$

where we used the coordinates $\vec{x}$ in the unit volume. The first term is the potential energy, the second term is the functional integration measure for this case (see Appendix A). Here $N\rho(\vec{x})$ stands for the density of particles.

The integration over $\hat{a}$ enforces the number of particles to be exactly $N$:

$$
\int d^3 x \, \rho(\vec{x})=1.
$$

That is, in the coordinates $\vec{q}$ (running from 0 to $L$), the density of particles is

$$
\frac{N}{L^3} \rho(\vec{q}) \quad \text{with} \quad \int d^3 q \, \frac{N}{L^3} \rho(\vec{q})=N.
$$

### 6.2. The microcanonical ensemble

Let us express the coordinate partition function in the microcanonical ensemble $w(\xi, N)$ defined by Eq. (11) in terms of the coordinate partition function in the canonical ensemble $e^{\Phi_{N}(\eta)}$ defined by Eq. (35). In order to do that we use the Fourier expansion [22]

$$
x^{\lambda} \theta(x)=\frac{\Gamma(\lambda+1)}{2 \pi} \int_{-\infty}^{+\infty} e^{i \omega x} \frac{d \omega}{(i \omega)^{\lambda+1}}.
\tag{73}
$$

We thus find from Eqs. (11), (35) and (73) that

$$
\begin{aligned}
w(\xi, N) & =\Gamma\left(\frac{3 N}{2}\right) \int_{-\infty}^{+\infty} \frac{d \omega}{2 \pi} e^{i \omega \xi+\Phi_{N}(i \omega / N)-\frac{3 N}{2} \log (i \omega)} \\
& =N \Gamma\left(\frac{3 N}{2}\right) \int_{\gamma} \frac{d \eta}{2 \pi i} e^{N \eta \xi+\Phi_{N}(\eta)-\frac{3 N}{2} \log (N \eta)},
\end{aligned}
\tag{74}
$$

where we introduced the integration variable $\eta \equiv i \omega / N$ and where $\gamma$ is an upward integration contour parallel to the imaginary $\eta$ axis. Using Stirling's approximation for the $\Gamma$ function we find for $N \gg 1$ up to irrelevant constants

$$
w(\xi, N) \stackrel{N \gg 1}{=} \int_{\gamma} \frac{d \eta}{2 \pi i} e^{N \eta \xi+\Phi_{N}(\eta)-\frac{3 N}{2} \log \eta}.
$$

Now, inserting the functional integral representation (71) for the coordinate canonical partition function yields,

$$
w(\xi, N) \stackrel{N \gg 1}{=} \iint D \rho d \hat{a} \frac{d \eta}{2 \pi i} e^{N\left[\eta \xi-\frac{3}{2} \log \eta-s_{C}[\rho(\cdot), \hat{a}, \eta]\right]}.
\tag{75}
$$

We thus find a functional integral representation in the microcanonical ensemble analogous to the canonical representation Eq. (71) but with an extra integration (over $\eta$ ) that constrains the value of the energy.

The 'effective action' in the microcanonical ensemble takes thus the form,

$$
\begin{aligned}
s_{\mathrm{MC}}[\rho(\cdot), \hat{a}, \eta]= & \frac{3}{2} \log \eta-\eta \xi-\frac{\eta}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho(\vec{x}) \rho(\vec{y}) \\
& +\int d^{3} x \rho(\vec{x}) \log \rho(\vec{x})-i \hat{a}\left(\int d^{3} x \rho(\vec{x})-1\right).
\end{aligned}
\tag{76}
$$

### 6.3. The grand canonical ensemble

The partition function in the grand canonical ensemble can be written as

$$
\mathcal{Z}_{\mathrm{GC}}(z, T)=\sum_{N=0}^{\infty} z^{N} \mathcal{Z}(N, T),
\tag{77}
$$

where $z=e^{\mu / T}$ stands for the fugacity and $\mathcal{Z}(N, T)$ is the partition function in the canonical ensemble given by Eqs. (28) and (31).

As shown in Ref. [4], this grand canonical partition function can be expressed as a functional integral
$$
\mathcal{Z}_{\mathrm{GC}}(z, T)=\iint \mathcal{D} \Phi e^{\frac{1}{T_{\text {eff }}} \int_{V} d^{3} q\left[\frac{1}{2} \Phi \nabla^{2} \Phi+M^{2} e^{\Phi(\vec{q})}\right]},\qquad(78)
$$
where
$$
M^{2}=\sqrt{\frac{2 T}{\pi}} z G m^{7 / 2}, \quad T_{\mathrm{eff}}=4 \pi \frac{G m^{2}}{T}.\qquad(79)
$$

Notice that the representation (78) is exact while the functional integral representations in the microcanonical and canonical ensembles only apply for large number of particles.

Rewriting Eq. (78) in terms of the dimensionless variables (7) yields for the exponent
$$
\begin{aligned}
& \frac{1}{T_{\text {eff }}} \int_{V} d^{3} q\left[\frac{1}{2} \Phi \nabla_{q}^{2} \Phi+\mu^{2} e^{\Phi(\vec{q})}\right] \\
& \quad=\frac{L}{T_{\text {eff }}} \int_{0}^{1} d^{3} x\left[\frac{1}{2} \Phi \nabla_{r}^{2} \Phi+\zeta^{2} e^{\Phi(\vec{x})}\right],
\end{aligned}
$$
where $\zeta \equiv M L$ is of the order one $(L^{0})$, since $M^{2} \sim z=e^{\mu / T} \sim L^{-2}$ (see Eq. (46)).

Since the exponent in the functional integral (78) is proportional to $L$, the large volume limit is dominated by the stationary points (mean field approximation)
$$
\nabla_{r}^{2} \Phi_{s}(\vec{x})+\zeta^{2} e^{\Phi_{s}(\vec{x})}=0.\qquad(80)
$$

We expand around the saddle point $\Phi_{s}(\vec{x})$ changing to a new functional integration $Y(\vec{x})$ variable as follows,
$$
\Phi(\vec{x})=\Phi_{s}(\vec{x})+Y(\vec{x}).\qquad(81)
$$

Keeping in Eq. (78) quadratic terms in $Y(\cdot)$ yields,
$$
\begin{aligned}
\mathcal{Z}_{\mathrm{GC}}(z, T)= & e^{\frac{L}{T_{\text {eff }}} \int_{0}^{1} d^{3} x\left[\frac{1}{2} \Phi_{s} \nabla_{r}^{2} \Phi_{s}+\zeta^{2} e^{\Phi_{s}(\vec{x})}\right]} \\
& \times \iint \mathcal{D} Y e^{\frac{L}{2 T_{\text {eff }}} \int_{0}^{1} d^{3} x\left[Y \nabla^{2} Y+\zeta^{2} Y^{2} e^{\Phi_{s}(\vec{x})}\right]}\left[1+\mathcal{O}\left(\frac{1}{L}\right)\right],
\end{aligned}\qquad(82)
$$
where the Gaussian integral over $Y(\cdot)$ gives a factor of order $L^{0}$ (see paper II).

We recall that the saddle point method applies while all eigenvalues of the quadratic form in the exponent of Eq. (82) are positive. Therefore, the determinant of the quadratic fluctuations is positive. The determinant vanishing or changing sign indicates the presence of zero or negative eigenvalues. In such a case the system is no more on a stable phase but on a metastable or unstable phase. The free energy gets an imaginary part in such metastable or unstable situations.

The average number of particles in the grand canonical ensemble is given by

$$
\overline{N} = \frac{1}{\mathcal{Z}_{\mathrm{GC}}} \sum_{N=0}^{\infty} N z^{N} \mathcal{Z}(N, T) = \left. \frac{\partial \log \mathcal{Z}_{\mathrm{GC}}}{\partial \log z} \right|_{V,T}.
$$

We thus find in the mean field approximation,

$$
\overline{N} = \frac{L \zeta^{2}}{T_{\text{eff}}} \int_{0}^{1} d^{3} x e^{\Phi_{s}(\vec{x})}.
$$

Therefore, using this and Eq. (79) we can express $\zeta^{2}$ in terms of $\eta$ where we denote $\overline{N}$ as $N$ to avoid cluttering of notation,

$$
\zeta^{2} = \frac{4 \pi \eta}{\int_{0}^{1} d^{3} x e^{\Phi_{s}(\vec{x})}}, \tag{83}
$$

and the fugacity results

$$
z = \frac{N}{L^{3}} \left( \frac{2 \pi}{m T} \right)^{3/2} \frac{1}{\int_{0}^{1} d^{3} x e^{\Phi_{s}(\vec{x})}}. \tag{84}
$$

We again see that $z \sim L^{-2}$ in the GCE.

Integrating Eq. (80) over the unit volume yields

$$
\int \vec{\nabla} \Phi_{s}(\vec{x}) \cdot d \vec{s} = -4 \pi \eta, \tag{85}
$$

where we used Eq. (83).

We find for the free energy [2],

$$
\begin{aligned}
F & = -T \log \mathcal{Z}_{\mathrm{GC}} + N T \log z \\
& = F_{0} + \frac{N T}{2} K(\eta) - N T \log C(\eta) + \mathcal{O}(N^{0}),
\end{aligned} \tag{86}
$$

where we used the grand canonical partition function (82) evaluated at the stationary point,

$$
\log \mathcal{Z}_{\mathrm{GC}} = N \left[ 1 - \frac{1}{2} K(\eta) \right], \tag{87}
$$

and $z$ is given by Eq. (84) with

$$
K(\eta) \equiv \frac{\int_{0}^{1} d^{3} x \Phi_{s}(\vec{x}) e^{\Phi_{s}(\vec{x})}}{C(\eta)} \quad \text{and} \quad C(\eta) \equiv \int_{0}^{1} d^{3} x e^{\Phi_{s}(\vec{x})}. \tag{88}
$$

$F_{0}$ is given by Eq. (44).

We easily calculate the mean value of the potential energy in the mean field approximation

$$
\langle U \rangle = -T \frac{\partial \log \mathcal{Z}_{\mathrm{GC}}}{\partial \log G} = -\frac{N T}{2} K(\eta). \tag{89}
$$

Combining the two expressions for the entropy
$$
S=\frac{E-F}{T} \quad \text { and } \quad S=-\left(\frac{\partial F}{\partial T}\right)_{V},
\tag{90}
$$
yields
$$
S=S_{0}-N[K(\eta)-\log C(\eta)],
\tag{91}
$$
and the first order differential equation
$$
\eta K^{\prime}(\eta)+K(\eta)=2 \eta \frac{d}{d \eta} \log C(\eta).
\tag{92}
$$

The boundary conditions $K(0)=0, C(0)=1$ ensure the ideal gas limit $\eta=0$.

The pressure takes the form,
$$
\begin{aligned}
P & =-\left(\frac{\partial F}{\partial V}\right)_{T} \\
& =\frac{N T}{V}\left[1+\frac{\eta}{3}\left(\frac{1}{2} K^{\prime}(\eta)-\frac{d}{d \eta} \log C(\eta)\right)\right]+\mathcal{O}\left(N^{0}\right).
\end{aligned}
\tag{93}
$$

These equations guarantee in addition that the virial theorem (38) holds.

### 6.4. Saddle point evaluation in the canonical ensemble

The functional integral in Eq. (71) is dominated for large $N$ by the extrema of the 'effective action' $s_{C}[\rho(\cdot), \hat{a}, \eta]$, that is, the solutions of the stationary point equation
$$
\log \rho_{s}(\vec{x})-\eta \int \frac{d^{3} y \rho_{s}(\vec{y})}{|\vec{x}-\vec{y}|}=a_{s},
\tag{94}
$$
$a=i \hat{a}$ is a Lagrange multiplier enforcing the constraint (72).

Applying the Laplacian and setting $\phi(\vec{x}) \equiv \log \rho_{s}(\vec{x})$ yields,
$$
\nabla^{2} \phi(\vec{x})+4 \pi \eta e^{\phi(\vec{x})}=0.
\tag{95}
$$

This equation is scale covariant [4]. That is, if $\phi(\vec{x})$ is a solution of Eq. (95), then
$$
\phi_{\lambda}(\vec{x}) \equiv \phi(\lambda \vec{x})+\log \lambda^{2},
\tag{96}
$$
where $\lambda$ is an arbitrary constant is also a solution of Eq. (95). For spherically symmetric solutions this property can be found in Ref. [8].

Integrating Eq. (95) over the unit volume and using the constraint (72) yields
$$
\int \vec{\nabla} \phi(\vec{x}) \cdot d \vec{s}=-4 \pi \eta,
\tag{97}
$$
where the surface integral is over the boundary of the unit volume.

Comparing Eqs. (80)-(85) with (95) and (97) shows that the grand canonical and canonical stationary points are related by
$$
\Phi_{s}(\vec{x})=\phi(\vec{x})+\log C(\eta).
\tag{98}
$$

Eq. (82) can then be written as

$$
\begin{aligned}
\mathcal{Z}_{\mathrm{GC}}(z, T) & \\
= & e^{\frac{N}{4 \pi \eta}\left\{\int_{0}^{1} d^{3} x\left[\frac{1}{2} \phi \nabla_{r}^{2} \phi+4 \pi \eta e^{\phi(\vec{x})}\right]-2 \pi \eta \log C(\eta)\right\}} \\
& \times \iint \mathcal{D} Y e^{\frac{N}{8 \pi \eta} \int_{0}^{1} d^{3} x\left[Y \nabla^{2} Y+4 \pi \eta Y^{2} e^{\phi(\vec{x})}\right]}\left[1+\mathcal{O}\left(\frac{1}{N}\right)\right],
\end{aligned}\tag{99}
$$

where we used Eqs. (32), (79), (83), (97) and (98).

We have taken the zero cut-off limit in Eqs. (94) and (95). The mean field equations turn to be finite with regular solutions in such limit. This can be understood from our perturbative calculation in Section 3.1. All potentially divergent contributions at zero cut-off are suppressed by factors $1/N^2$ and therefore disappear in the $N=\infty$ limit. Hence one can set the cut-off to zero in the mean field approximation.

In order to evaluate the functional integral in Eq. (71) by the saddle point method we change the functional integration variable as follows,

$$
\rho(\vec{x})=\rho_{s}(\vec{x})+Y(\vec{x}), \quad a=a_{s}+y_{0},\tag{100}
$$

where $\rho_{s}(\vec{x})$ and $a_{s}$ obey Eq. (94). We can expand the exponent to second order as

$$
s_{C}[\rho(\cdot), a, \eta]-s_{C}\left[\rho_{s}(\cdot), a_{s}, \eta\right]=s_{C}^{(2)}\left[Y(\cdot), y_{0}\right]+\mathcal{O}\left(Y^{3}, Y^{2} y_{0}\right),\tag{101}
$$

where we use that

$$
\left.\frac{\delta s_{C}}{\delta \rho(\vec{x})}\right|_{\rho=\rho_{s}, a=a_{s}}=0,\left.\quad \frac{\partial s_{C}}{\partial a}\right|_{\rho=\rho_{s}, a=a_{s}}=0,
$$

and

$$
\begin{aligned}
s_{C}^{(2)}\left[Y(\cdot), y_{0}\right] \equiv & \left.\frac{1}{2} \int d^{3} x d^{3} y Y(\vec{x}) Y(\vec{y}) \frac{\delta^{2} s_{C}}{\delta \rho(\vec{x}) \delta \rho(\vec{y})}\right|_{\rho=\rho_{s}, a=a_{s}} \\
& +\left.y_{0} \int d^{3} x Y(\vec{x}) \frac{\delta^{2} s_{C}}{\delta \rho(\vec{x}) \partial a}\right|_{\rho=\rho_{s}, a=a_{s}} .
\end{aligned}
$$

Notice that

$$
\frac{\partial^{2} s_{C}}{\partial a^{2}}=0.
$$

We evaluate explicitly the second derivatives from Eq. (71) with the result,

$$
\frac{\delta^{2} s_{C}}{\delta \rho(\vec{x}) \delta \rho(\vec{y})}=\frac{\delta(\vec{x}-\vec{y})}{\rho(\vec{x})}-\frac{\eta}{|\vec{x}-\vec{y}|}, \quad \frac{\delta^{2} s_{C}}{\delta \rho(\vec{x}) \partial a}=1.
$$

Therefore,

$$
\begin{aligned}
s_{C}^{(2)}\left[Y(\cdot), y_{0}\right]= & \frac{1}{2} \int d^{3} x \frac{Y^{2}(\vec{x})}{\rho(\vec{x})}-\frac{\eta}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} Y(\vec{x}) Y(\vec{y}) \\
& -y_{0} \int d^{3} x Y(\vec{x}).
\end{aligned}\tag{102}
$$
```

Inserting Eqs. (100) and (101) into Eq. (71) yields

$$
e^{\Phi_{N}(\eta)} \stackrel{N \gg 1}{=} e^{-N s(\eta)} \iint D Y d y_{0} e^{-N s_{C}^{(2)}\left[Y(\cdot), y_{0}\right]}\left[1+\mathcal{O}\left(\frac{1}{N}\right)\right], \tag{103}
$$

where $s(\eta) \equiv s_{C}[\rho_{s}(\cdot), a_{s}, \eta]$ stands for the value of the exponent at the saddle point. Terms of order higher than quadratic in $s_{C}[\rho(\cdot), a, \eta]$ contribute to the $1/N$ corrections.

The Gaussian functional integral (103) can be exactly computed in terms of the functional determinant of the quadratic form (102) (see paper II). It gives a result of order one $(N^{0})$.

In the mean field approximation we only keep the dominant order for large $N$. Therefore, only the exponent at the saddle point accounts and according to Eq. (34) we find for the free energy

$$
F=F_{0}+N T s(\eta)+\mathcal{O}\left(N^{0}\right), \quad \frac{p V}{N T}=1+\frac{\eta}{3} \frac{d s}{d \eta}+\mathcal{O}\left(N^{-1}\right). \tag{104}
$$

Hence, in the mean field approximation, the function $f(\eta)$ is given by

$$
f_{\mathrm{MF}}(\eta) \equiv 1+\frac{\eta}{3} \frac{d s}{d \eta}. \tag{105}
$$

From Eq. (71) we can compute $s(\eta)$ in terms of the saddle point solution as follows

$$
\begin{aligned}
s(\eta) & \equiv s_{C}\left[\rho_{s}(\cdot), a_{s}, \eta\right] \\
& =-\frac{\eta}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho_{s}(\vec{x}) \rho_{s}(\vec{y})+\int d^{3} x \rho_{s}(\vec{x}) \log \rho_{s}(\vec{x}).
\end{aligned} \tag{106}
$$

Using Eq. (94) we find an equivalent expression that will be useful in paper II,

$$
s(\eta)=\frac{a_{s}}{2}+\frac{1}{2} \int \phi(\vec{x}) e^{\phi(\vec{x})} d^{3} x. \tag{107}
$$

### 6.5. Saddle point evaluation in the microcanonical ensemble

The extrema of the 'effective action' (76) dominate the microcanonical partition function (75) in the large $N$ limit. Extremizing Eq. (76) with respect to $\rho(\cdot)$ and $\hat{a}$ gives again Eqs. (94) and (72), respectively.

An extra equation follows by extremizing the 'effective action' (76) with respect to $\eta$:

$$
\xi=\frac{3}{2 \eta_{s}}-\frac{1}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho_{s}(\vec{x}) \rho_{s}(\vec{y}). \tag{108}
$$

Going back to dimensionful variables this equation takes the familiar form

$$
E=\frac{3}{2} N T-\frac{G m^{2}}{2} \int \frac{d^{3} q d^{3} q^{\prime}}{\left|\vec{q}-\vec{q}^{\prime}\right|} N \rho(\vec{q}) N \rho\left(\vec{q}^{\prime}\right).
$$

That is, Eq. (108) enforces the fixed value of the energy in the microcanonical ensemble.

Therefore, the stationary point equations in the microcanonical and canonical ensembles are identical. Both ensembles yield the same results in the $N \to \infty$ limit in their common

region of validity. We derive the domain of validity of the mean field approach for each of the three statistical ensembles in paper II. That is, the regions where all fluctuations around it decrease its statistical weight within their common region of validity.

In order to evaluate the functional integral for the microcanonical partition function (75)
$$
w(\xi, N) \stackrel{N \gg 1}{=} \iint D \rho d \hat{a} \frac{d \eta}{2 \pi i} e^{-N s_{\mathrm{MC}}[\rho(\cdot), \hat{a}, \eta]},\qquad(109)
$$
we expand the 'effective action' $s_{\mathrm{MC}}[\rho(\cdot), \hat{a}, \eta]$ around the stationary point $\rho_{s}(\cdot), \hat{a}_{s}, \eta_{s}$ to second order. This gives
$$
w(\xi, N) \stackrel{N \gg 1}{=} e^{-N s(\eta)} \iint D Y d y_{0} \frac{d \tilde{\eta}}{2 \pi i} e^{-N s_{\mathrm{MC}}^{(2)}\left[Y(\cdot), y_{0}, \tilde{\eta}\right]}\left[1+\mathcal{O}\left(\frac{1}{N}\right)\right],\qquad(110)
$$
where $Y(\cdot)$ and $y_{0}$ are defined by Eq. (100) and we set $\eta=\eta_{s}+\tilde{\eta}$. The second order piece of the 'effective action' takes now the form
$$
s_{\mathrm{MC}}^{(2)}\left[Y(\cdot), y_{0}, \tilde{\eta}\right]=s_{C}^{(2)}\left[Y(\cdot), y_{0}\right]-\tilde{\eta} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho_{s}(\vec{x}) Y(\vec{y})-\frac{3}{4 \eta_{s}^{2}} \tilde{\eta}^{2}.\qquad(111)
$$

The Gaussian functional integral in Eq. (110) yields a contribution of order one $(N^{0})$ (see paper II). The dominant (mean field) contribution, $e^{-N s(\eta)}$, exactly coincides with the mean field result in the canonical ensemble (Eq. (103)). Therefore, the canonical and microcanonical ensembles yields identical physical magnitudes and the same equation of state in the mean field limit.

### 6.6. Spherically symmetric case
We shall consider here the spherically symmetric case where Eq. (95) takes the form
$$
\frac{d^{2} \phi}{d R^{2}}+\frac{2}{R} \frac{d \phi}{d R}+4 \pi \eta e^{\phi(R)}=0,\qquad(112)
$$
where we work on an unit volume sphere instead of an unit volume cube as in Eq. (7). Therefore, the radial variable runs in the interval
$$
0 \leqslant R \leqslant\left(\frac{3}{4 \pi}\right)^{1 / 3}.
$$

It is more convenient to introduce a new radial variable
$$
r \equiv R\left(\frac{4 \pi}{3}\right)^{1 / 3},
$$
such that $0 \leqslant r \leqslant 1$.

The saddle point equation (112) takes then the form
$$
\frac{d^{2} \phi}{d r^{2}}+\frac{2}{r} \frac{d \phi}{d r}+4 \pi \eta^{R} e^{\phi(r)}=0,\qquad(113)
$$
where
$$
\eta^{R} \equiv \eta\left(\frac{4 \pi}{3}\right)^{1 / 3}=1.61199 \ldots \cdot \eta \quad \text { and } \quad e^{\phi(r)}=e^{\phi(R)} \frac{3}{4 \pi}.\qquad(114)
$$

In order to have a regular solution at $r=0$ one has to impose

$$
\phi^{\prime}(0)=0. \tag{115}
$$

Otherwise, the second term in Eq. (112) diverges for $r \to 0$.

In the spherically symmetric case, the constraint (97) becomes

$$
\phi^{\prime}(1)=-\eta^{R}. \tag{116}
$$

Using the scale covariance (96) we can express $\phi(r)$ as

$$
\phi(r)=\log \left(\frac{\lambda^{2}}{4 \pi \eta^{R}}\right)+\chi(\lambda r), \tag{117}
$$

where

$$
\chi^{\prime \prime}(\lambda)+\frac{2}{\lambda} \chi^{\prime}(\lambda)+e^{\chi(\lambda)}=0, \quad \chi^{\prime}(0)=0. \tag{118}
$$

This equation is invariant under the transformation:

$$
\lambda \Rightarrow \lambda e^{\alpha}, \quad \chi(\lambda) \Rightarrow \chi(\lambda)-2 \alpha, \tag{119}
$$

where $\alpha$ is a real number. Hence, we can set $\chi(0) \equiv 0$ without loosing generality.

$\chi(x)$ is independent of $\eta^{R}$ and $\lambda$ is related to $\eta^{R}$ through Eq. (116)

$$
\lambda \chi^{\prime}(\lambda)=-\eta^{R}. \tag{120}
$$

Since $\lambda$ and $\eta^{R}$ are always positive, $\chi(\lambda)$ is a monotonically decreasing function of $\lambda$.

Eq. (118) can be easily solved for small arguments as

$$
\chi(x)=-\frac{x^{2}}{6}+\frac{x^{4}}{120}+\mathcal{O}\left(x^{6}\right).
$$

Hence, in the dilute limit Eq. (120) relating $\eta^{R}$ with $\lambda$ gives

$$
\eta^{R}=\frac{\lambda^{2}}{3}-\frac{\lambda^{4}}{30}+\mathcal{O}\left(\lambda^{6}\right). \tag{121}
$$

For large argument, the solution of Eq. (118) takes the asymptotic form [8]

$$
\chi(x)=\log \frac{2}{x^{2}}+\frac{A}{\sqrt{x}} \cos \left(\frac{\sqrt{7}}{2} \log x+B\right)\left[1+\mathcal{O}\left(\frac{1}{x}\right)\right], \tag{122}
$$

where $A$ and $B$ are numerical constants. Using Eq. (120) this gives for $\eta^{R}$

$$
\eta^{R}=2+\frac{C}{\sqrt{\lambda}} \cos \left(\frac{\sqrt{7}}{2} \log \lambda+D\right)\left[1+\mathcal{O}\left(\frac{1}{\lambda}\right)\right], \tag{123}
$$

where $C$ and $D$ are constants related to $A$ and $B$. By numerically solving Eq. (118) we find

$$
C=1.667 \ldots .
$$

It must be noticed, however, that the mean field solution is unphysical for $\lambda>\lambda_{\mathrm{MC}}=$ $34.36361 \ldots$ as we shall see in paper II. Anyway, we see from Fig. 7 that $\eta^{R}$ approaches very fast its asymptotic behaviour (123) for $\log \lambda>2$.

![](./images/812449694637621249_9.jpg)

Fig. 7. $\eta^R$ as a function of the uniformizing scale variable $\log\lambda$ according to Eq. (120). Notice the maximum of $\eta^R$ as $\eta_C^R=2.517551\ldots$. The region beyond the point MC ($\ln\lambda_{\text{MC}}=3.53698\ldots$), is unphysical as we discuss in paper II.

We plot in Fig. $8\ \chi(\lambda(\eta^R))$ as a function of $\eta^R$.

In the spherically symmetric case the integral over the angles in Eq. (94) is immediate with the result,
$$
\phi(r)=a_s+4\pi\eta^R\left[\frac{1}{r}\int_0^r r'^2 dr' e^{\phi(r')}+\int_r^1 r' dr' e^{\phi(r')}\right]. \tag{124}
$$

Deriving with respect to $r$ yields,
$$
\frac{d\phi(r)}{dr}=-\frac{4\pi\eta^R}{r^2}\int_0^r r'^2 dr' e^{\phi(r')}.
$$

This again shows that $\phi(r)$ is a monotonically decreasing function of $r$ (see above, Eq. (120))).

Setting $r=1$ in Eq. (124) leads to the relation
$$
\phi(1)=a_s+4\pi\eta^R\int_0^1 r^2 dr e^{\phi(r)}.
$$

![](./images/812449694637621249_10.jpg)

Fig. 8. $\chi(\lambda(\eta^R))=\log\frac{p(0)}{p(1)}=\log\frac{\rho(0)}{\rho(1)}$ as a function of $\eta^R$.

Using now the constraint (72) allows us to compute the Lagrange multiplier $a$ at the saddle point
$$
a_{s}=\phi(1)-\eta^{R}.\tag{125}
$$

The particle density in MF is given by
$$
\rho(r)=e^{\phi(r)}=\frac{\lambda^{2}}{4 \pi \eta^{R}} e^{\chi(\lambda r)}, \quad 0 \leqslant r \leqslant 1.
$$

Since $\chi(\lambda)$ monotonically decreases with $\lambda$, the particle density monotonically decreases with $r$ for fixed $\eta^{R}$.

Let us now compute $s(\eta^R)$ (the exponent in Eq. (71) at the saddle point) for the spherically symmetric case. We find from Eq. (107)
$$
\begin{aligned}
s\left(\eta^{R}\right) & =\frac{1}{2}\left[\phi(1)-\eta^{R}\right]+2 \pi \int_{0}^{1} r^{2} d r \phi(r) e^{\phi(r)} \\
& =\log \left(\frac{\lambda^{2}}{4 \pi \eta^{R}}\right)+\chi(\lambda)-\frac{\eta^{R}}{2}+\frac{1}{2 \lambda \eta^{R}} \int_{0}^{\lambda} x^{2} d x\left[\chi^{\prime}(x)\right]^{2},
\end{aligned}\tag{126}
$$
where we integrated by parts and used Eqs. (117)-(120).

The integral in the r.h.s. of Eq. (126) can be computed in closed form (see Appendix B)
with the result,

$$
s\left(\eta^{R}\right)=\log \left(\frac{\lambda^{2}}{4 \pi \eta^{R}}\right)+\chi(\lambda)+3-\eta^{R}-\frac{\lambda^{2}}{\eta^{R}} e^{\chi(\lambda)}.
$$

Inserting now $s(\eta^{R})$ into Eq. (105) and using Eqs. (118)-(120) yields after calculation

$$
f_{\mathrm{MF}}\left(\eta^{R}\right)=\frac{\lambda^{2}}{3 \eta^{R}} e^{\chi(\lambda)},
$$

$$
s\left(\eta^{R}\right)=3\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right]-\eta^{R}+\log \left[\frac{3 f_{\mathrm{MF}}\left(\eta^{R}\right)}{4 \pi}\right]. \tag{127}
$$

Notice that $f_{\mathrm{MF}}(\eta^{R})$ as well as the other physical quantities are invariant under the
transformation (119) as it must be.

It follows from Eqs. (118), (120) and (127) that $f_{\mathrm{MF}}(\eta^{R})$ obeys the first order non-linear
differential equation

$$
\eta^{R}\left(3 f_{\mathrm{MF}}-1\right) f_{\mathrm{MF}}^{\prime}\left(\eta^{R}\right)+\left(3 f_{\mathrm{MF}}-3+\eta^{R}\right) f_{\mathrm{MF}}=0, \tag{128}
$$

which reduces to an Abel equation of first kind [21].

We thus find that in the mean field approximation all thermodynamic quantities follow
from the resolution of the single first order non-linear differential Eq. (128) with the initial
condition $f_{\mathrm{MF}}(0)=1$.

Integrating Eq. (128) with respect to $\eta^{R}$ yields,

$$
3 \int_{0}^{\eta^{R}} \frac{d x}{x}\left[1-f_{\mathrm{MF}}(x)\right]=3\left[f_{\mathrm{MF}}\left(\eta^{R}\right)-1\right]+\eta^{R}-\log f_{\mathrm{MF}}\left(\eta^{R}\right).
$$

Further useful relations follow from Eqs. (117) and (127)

$$
\phi(1)=\log \left[\frac{3 f_{\mathrm{MF}}\left(\eta^{R}\right)}{4 \pi}\right], \quad \rho(1)=\frac{3}{4 \pi} f_{\mathrm{MF}}\left(\eta^{R}\right). \tag{129}
$$

That is, the particle density at the surface $(r=1)$ is proportional to $f_{\mathrm{MF}}(\eta^{R})$.

We can then write the different physical magnitudes in the MF approximation as

$$
\begin{aligned}
\frac{p V}{N T} &=f_{\mathrm{MF}}\left(\eta^{R}\right), \\
\frac{F-F_{0}}{N T} &=3\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right]-\eta^{R}+\log f_{\mathrm{MF}}\left(\eta^{R}\right), \\
\frac{S-S_{0}}{N} &=6\left[f_{\mathrm{MF}}\left(\eta^{R}\right)-1\right]+\eta^{R}-\log f_{\mathrm{MF}}\left(\eta^{R}\right), \\
\frac{E}{N T} &=3\left[f_{\mathrm{MF}}\left(\eta^{R}\right)-\frac{1}{2}\right],
\end{aligned} \tag{130}
$$

where we used Eqs. (41), (43), (45) and (46).

![](./images/812449694637621249_11.jpg)

Fig. 9. $f_{\mathrm{MF}}(\eta^{R})=PV/[NT]$ as a function of $\eta^{R}$ in the MF approximation (Eq. (128)). $f_{\mathrm{MF}}(\eta^{R})$ has a square root branch point at $\eta_{C}^{R}$. The points GC, C and MC indicate the transition to the collapsed phase for each ensemble (grand canonical, canonical and microcanonical, respectively): $\eta_{\mathrm{GC}}^{R}=0.797375\ldots$, $\eta_{C}^{R}=2.517551\ldots$, $\eta_{\mathrm{MC}}^{R}=2.03085\ldots$ (notice that $\eta_{\mathrm{MC}}^{R}$ is in the second Riemann sheet). Since $E/[3NT]=f_{\mathrm{MF}}(\eta^{R})-\frac{1}{2}$, this plot also shows the energy per particle as a function of $\eta^{R}$. Furthermore, the particle density at the surface is proportional to $f_{\mathrm{MF}}(\eta^{R})$ (Eq. (129)).

We derive in Appendix C the properties of the function $f_{\mathrm{MF}}(\eta^{R})$ from the differential equation (128). One easily obtains for small $\eta^{R}$ (dilute regime),

$$
f_{\mathrm{MF}}(\eta^{R})=1-\frac{\eta^{R}}{5}-\frac{(\eta^{R})^{2}}{175}+\mathcal{O}\left(\left[\eta^{R}\right]^{3}\right).
$$

These terms exactly coincide with the perturbative calculation in the dilute regime for spherical symmetry (see Eqs. (23), (61) and (114)).

We plot in Fig. 9 $f_{\mathrm{MF}}(\eta^{R})$ as a function of $\eta^{R}$ obtained by solving Eq. (128) by the Runge–Kutta method. We see that $f_{\mathrm{MF}}(\eta^{R})$ is a *monotonically decreasing* function of $\eta^{R}$ for $0<\eta^{R}<\eta_{C}^{R}$. At the point $\eta^{R}=\eta_{C}^{R}$, the derivative $f_{\mathrm{MF}}'(\eta^{R})$ takes the value $-\infty$. It then follows from Eq. (128) that

$$
f_{\mathrm{MF}}(\eta_{C}^{R})=\frac{1}{3}.
$$

At the point $\eta_C^R$ the series expansion for $f_{\rm MF}(\eta^R)$ in powers of $\eta^R$ diverges. Both, from the ratio test on its coefficients and from the Runge–Kutta solution, we find that

$$
\eta_{C}^{R}=2.517551 \ldots.\qquad(131)
$$

From Eq. (128) we find that $f_{\rm MF}(\eta^R)-\frac{1}{3}$ has a square root behaviour around $\eta^R=\eta_C^R$:

$$
\begin{aligned}
f_{\mathrm{MF}}\left(\eta^{R}\right) \stackrel{\eta^{R} \uparrow \eta_{C}^{R}}{=} & \frac{1}{3}+\sqrt{\frac{2\left(\eta_{C}^{R}-2\right)}{9 \eta_{C}^{R}}} \sqrt{\eta_{C}^{R}-\eta^{R}} \\
& +\frac{2\left(\eta_{C}^{R}-1\right)}{7 \eta_{C}^{R}}\left(\eta_{C}^{R}-\eta^{R}\right)+\mathcal{O}\left[\left(\eta_{C}^{R}-\eta^{R}\right)^{3 / 2}\right].
\end{aligned}
$$

Inserting the numerical value (131) for $\eta_C^R$ yields,

$$
\begin{aligned}
f_{\mathrm{MF}}\left(\eta^{R}\right) \stackrel{\eta^{R} \uparrow \eta_{C}^{R}}{=} & \frac{1}{3}+0.213738 \ldots \cdot \sqrt{\eta_{C}^{R}-\eta^{R}}+0.172225 \ldots \cdot\left(\eta_{C}^{R}-\eta^{R}\right) \\
& +\mathcal{O}\left[\left(\eta_{C}^{R}-\eta^{R}\right)^{3 / 2}\right].\qquad(132)
\end{aligned}
$$

We see that $f_{\rm MF}(\eta^R)$ becomes complex for $\eta^R > \eta_C^R$. Recall that in the Monte Carlo simulations the gas phase collapses at the point $\eta_T^R < \eta_C^R$.

From Eq. (130), we plot $pV/[NT]$, $S/N$ and $\frac{F-F_0}{NT}$ as a function of $\eta^R$ in Figs. 9, 10 and 11, respectively.

The points GC, C and MC correspond to the collapse phase transition in the grand canonical, canonical and microcanonical ensembles, respectively. Their positions are determined by the breakdown of the mean field approximation through the analysis of the small fluctuations (see paper II).

$f_{\rm MF}(\eta^R)$ is a multivalued function of $\eta^R$ as well as all physical magnitudes (see Eq. (130)).

As noticed before, the CE only describes the region between the ideal gas point, $\eta^R=0$ and C in Fig. 1. The MCE goes beyond the point C (till the point MC) with the physical magnitudes described by the second sheet of the square root in Eq. (132) (minus sign). We have near C between C and MC,

$$
\begin{aligned}
f_{\mathrm{MF}}\left(\eta^{R}\right) \stackrel{\eta^{R} \uparrow \eta_{C}^{R}}{=} & \frac{1}{3}-0.213738 \ldots \cdot \sqrt{\eta_{C}^{R}-\eta^{R}}+0.172225 \ldots \cdot\left(\eta_{C}^{R}-\eta^{R}\right) \\
& +\mathcal{O}\left[\left(\eta_{C}^{R}-\eta^{R}\right)^{3 / 2}\right].
\end{aligned}
$$

The function $f_{\rm MF}(\eta^R)$ takes its absolute minimum at $\eta^R=\eta_{\rm min}^R=2.20731\ldots$ in the second sheet where $f_{\rm MF}(\eta_{\rm min}^R)=0.264230\ldots$.

Since $f_{\rm MF}(\eta^R) < \frac{1}{2}$ implies that the total energy is negative (see Eq. (130)), the gas is in a *bounded state* for $\eta^R$ beyond $\eta_2^R=2.18348\ldots$ in the first sheet.

Since $\chi(\lambda)$ and $\eta(\lambda)$ are single-valued functions of $\lambda$, $f_{\rm MF}(\eta^R(\lambda))$ defined by Eq. (127) is also a single-valued function of $\lambda$. That is, $\lambda$ is the *uniformization* variable. All physical magnitudes are single-valued functions of $\lambda$. On the other hand, $\lambda$ is an infinite-valued

![](./images/812449694637621249_12.jpg)

Fig. 10. The entropy per particle minus the ideal gas value as a function of $\eta^R$ in the MF approximation (Eq. (130)).

function of $\eta^R$ as one sees from Fig. 7 and Eq. (123). That is, $f_{\mathrm{MF}}(\eta^R)$ has an infinite number of Riemann sheets. However, only the first two sheets are physically realized. The rest are unphysical. A plot of $f_{\mathrm{MF}}(\eta^R)$ including all sheets produces a nice spiral [8] converging towards $\eta^R=2$, $f_{\mathrm{MF}}(\eta^R)=1/3$ for $\lambda=\infty$ as follows from Eqs. (122), (123) and (127).

$\lambda$ induces a scale transformation in coordinate space as we see in Eq. (117) whereas $\eta^R$ plays the coupling constant (recall that $\eta^R$ is proportional to Newton's gravitational constant).

The variation of $\eta^R$ with respect to $\lambda$ yields the renormalization group equation

$$
\lambda \frac{d \eta^R}{d \lambda}=\eta^R\left[3 f_{\mathrm{MF}}\left(\eta^R\right)-1\right],
$$

where we used Eqs. (118), (120) and (127). Here $\eta^R[3 f_{\mathrm{MF}}(\eta^R)-1]$ plays the role of the renormalization group beta function. We see that it has two fixed points at $\eta^R=0$ and at $\eta^R=\eta_C^R$. (See Fig. 7 where the running of $\eta^R$ with $\lambda$ is exhibited.)

We find from Eqs. (121) and (132) near these fixed points

$$
\eta^R \stackrel{\lambda \rightarrow 0}{=} \frac{\lambda^2}{3}, \quad \eta^R \stackrel{\lambda \rightarrow \lambda_C}{=} \eta_C^R-\frac{\eta_C^R\left(\eta_C^R-2\right)}{2 \lambda_C^2}\left(\lambda-\lambda_C\right)^2,
$$

where the coefficient has the numerical value $\frac{\eta_C^R(\eta_C^R-2)}{2 \lambda_C^2}=0.0085515 \ldots$

![](./images/812449694637621249_13.jpg)

Fig. 11. $\frac{F-F_0}{NT}$ as a function of $\eta$ in the MF approximation (Eq. (130)).

### 6.7. Canonical vs. grand canonical ensembles in the mean field approximation

We have seen that the stationary point equations and their respective solutions are closely related in the canonical and grand canonical ensembles (Eqs. (80)-(85) and (97), (98)).

Let us now show that physical quantities obtained from both ensembles do coincide in the mean field approximation.

From Eqs. (88) and (98) we find that
$$
K(\eta)=\int \phi(\vec{x}) e^{\phi(\vec{x})} d^{3} x+\log C(\eta). \tag{133}
$$
(Recall that $\int e^{\phi(\vec{x})} d^{3} x=1$.)

In the spherically symmetric case this integral takes the form
$$
4 \pi \int_{0}^{1} r^{2} d r \phi(r) e^{\phi(r)}=\phi(1)+\frac{1}{\eta^{R}} \int_{0}^{1} r^{2} d r\left(\frac{d \phi}{d r}\right)^{2}
$$

$$
=6\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right]-\eta^{R}+\log \left[\frac{3 f_{\mathrm{MF}}\left(\eta^{R}\right)}{4 \pi}\right],\qquad(134)
$$

where we integrated by parts and used Eqs. (117), (120) and Appendix B.

From Eqs. (133) and (134) we find
$$
K\left(\eta^{R}\right)-\log C\left(\eta^{R}\right)=6\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right]-\eta^{R}+\log \left[\frac{3 f_{\mathrm{MF}}\left(\eta^{R}\right)}{4 \pi}\right].
$$

Inserting this result into the linear differential equations (92) leads to the solution,
$$
C\left(\eta^{R}\right)=\frac{4 \pi}{3} \frac{\exp \left[\eta^{R}\right]}{f_{\mathrm{MF}}\left(\eta^{R}\right)} \quad \text { and } \quad K\left(\eta^{R}\right)=6\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right].\qquad(135)
$$

We then find from Eqs. (98), (125) and (129) that
$$
\log C(\eta)=-a_{s}.\qquad(136)
$$

Combining Eq. (135) with Eqs. (89), (86)–(91) and (93) shows that the canonical and the grand canonical ensembles yields identical physical magnitudes (pressure, energy, entropy, free energy, specific heats, compressibilities, speed of sound) and the same equation of state in the mean field approximation.

The thermodynamical potential [2],
$$
\Omega \equiv-T \log \mathcal{Z}_{\mathrm{GC}}=N\left[3 f_{\mathrm{MF}}\left(\eta^{R}\right)-2\right],
$$
is not equal to $-P V$. That is, here $\Omega \neq-P V$ and we have instead
$$
\Omega+P V=2 N T\left[1-f_{\mathrm{MF}}\left(\eta^{R}\right)\right].
$$

This relation is analogous to Eq. (48). $\Omega$ differs here from $-P V$ since for the self-gravitating gas we have $N \sim L$ instead of the usual relation $N \sim L^{3}$.

## 7. Specific heats, speed of sound and compressibility

The specific heat at constant volume in the mean field approximation takes the form
$$
\left(c_{V}\right)_{\mathrm{MF}}=6 f_{\mathrm{MF}}\left(\eta^{R}\right)-\frac{7}{2}+\eta^{R}+\frac{\eta^{R}-2}{3 f_{\mathrm{MF}}\left(\eta^{R}\right)-1},\qquad(137)
$$
where we used Eqs. (49) and (128).

We plot in Fig. 12 Eq. (137) for $(c_{V})_{MF}$ as a function of $\eta$ . We see that $(c_{V})_{MF}$ increases with $\eta$ till it tends to $+\infty$ for $\eta^{R} \uparrow \eta_{C}^{R}$ . It has a square-root branch point at the point C. In the stretch C-MC (only physically realized in the microcanonical ensemble), $(c_{V})_{MF}$ becomes negative. We shall not discuss here the peculiar properties of systems with negative $c_{V}$ as they can be find in Refs. [11,12,16]

From Eqs. (132) and (137) we obtain the following behaviour near the point C in the positive (first) branch
$$
\begin{aligned}
\left(c_{V}\right)_{\mathrm{MF}} \stackrel{\eta^{R} \uparrow \eta_{C}^{R}}{=} & 0.80714 \cdots\left(\eta_{C}^{R}-\eta^{R}\right)^{-1 / 2} \\
& -0.19924 \cdots+\mathcal{O}\left(\sqrt{\eta_{C}^{R}-\eta^{R}}\right),
\end{aligned}\qquad(138)
$$

![](./images/812449694637621249_14.jpg)

Fig. 12. $(c_V)_{MF}$ as a function of $\eta^R$ from mean field Eq. (137). Notice that $(c_V)_{MF}$ diverges at the point C, that is for $\eta_C^R = 2.517551\ldots$.

and between C and MC in the negative (second) branch
$$
(c_V)_{MF} \stackrel{\eta^R \uparrow \eta_C^R}{=} -0.80714\ldots \cdot (\eta_C^R - \eta^R)^{-1/2} - 0.19924\ldots + \mathcal{O}\left(\sqrt{\eta_C^R - \eta^R}\right).
$$

Finally, $(c_V)_{MF}$ vanishes at the point MC $\eta_{\text{MC}}^R = 2.03085\ldots$.

The isothermal compressibility in mean field follows from Eqs. (54) and (128)
$$
(\kappa_T)_{MF} = \frac{3}{2 f_{\text{MF}}(\eta^R)} \left[ 1 + \frac{\eta^R - 2}{6 f_{\text{MF}}(\eta^R) - \eta^R} \right]. \tag{139}
$$

We plot $(\kappa_T)_{MF}$ in Fig. 13. We see that $(\kappa_T)_{MF}$ is positive for $0 \leqslant \eta^R < \eta_0^R = 2.43450\ldots$ where $(\kappa_T)_{MF}$ diverges. The point $\eta_0^R$ is defined by the equation
$$
6 f_{\text{MF}}(\eta_0^R) - \eta_0^R = 0. \tag{140}
$$

We find from Eqs. (128) and (140) that
$$
f_{\text{MF}}'(\eta_0^R) = -\frac{1}{2}. \tag{141}
$$

$(\kappa_T)_{MF}$ diverges for $\eta^R \simeq \eta_0^R$ as
$$
(\kappa_T)_{MF} \stackrel{\eta^R \simeq \eta_0^R}{=} \frac{9 (\eta_0^R - 2)}{4 \eta_0^R (\eta_0^R - \eta^R)} + \mathcal{O}(1) = \frac{0.40157\ldots}{\eta_0^R - \eta^R} + \mathcal{O}(1).
$$

![](./images/812449694637621249_15.jpg)

Fig. 13. $(\kappa_{T})_{\text{MF}}$ as a function of $\eta$ from mean field Eq. (139). Notice that $(\kappa_{T})_{\text{MF}}$ diverges at $\eta^{R}=\eta_{0}^{R}=2.43450\ldots$

$(\kappa_{T})_{\text{MF}}$ is negative for $\eta_{0}^{R}<\eta^{R}<\eta_{C}^{R}$ and exactly vanishes at the point C. $(\kappa_{T})_{\text{MF}}$ then becomes positive in the stretch between C and MC only physically realized in the microcanonical ensemble.

Notice that the singularity of $(\kappa_{T})_{\text{MF}}$ at $\eta^{R}=\eta_{0}^{R}=2.43450\ldots$ is before but near the point C. It appears as a preliminary signal of the phase transition at C. $\eta_{0}^{R}$ is probably the transition point $\eta_{T}$ seen with the Monte Carlo simulations (see Fig. 1). (Recall that $\eta_{T}\sim1.515$ corresponds to $\eta_{T}^{R}\sim2.44$.)

It is easy to understand the meaning of a large compressibility. From the definition (54)
$$
\frac{\delta V}{V}=-K_{T} \delta p=-\kappa_{T} \frac{V \delta p}{N T}.\tag{142}
$$

A large compressibility implies that a small increase in the pressure $(\delta p \ll N T / V)$ produces a large change in the density of the gas. That means a very soft fluid.

For negative compressibility, Eq. (142) tells us that the gas increases its volume when the external pressure on it increases. This is clearly an unusual behaviour that leads to instabilities as we shall see below.

The specific heat at constant pressure in the mean field approximation takes the form
$$
\left(c_{P}\right)_{\mathrm{MF}}=12 f_{\mathrm{MF}}\left(\eta^{R}\right)-\frac{3}{2}+\frac{24\left(\eta^{R}-2\right) f_{\mathrm{MF}}\left(\eta^{R}\right)}{6 f_{\mathrm{MF}}\left(\eta^{R}\right)-\eta^{R}},\tag{143}
$$

![](./images/812449694637621249_16.jpg)

Fig. 14. $c_P$ as a function of $\eta$ from mean field Eq. (143). Notice that $c_P$ diverges at $\eta^R=\eta_0^R=2.43450\ldots$

where we used Eqs. (53) and (128). We plot $(c_P)_{\rm MF}$ in Fig. 14. We see that $(c_P)_{\rm MF}$ is positive and grows with $\eta^R$ till it diverges at the same point where $(\kappa_T)_{\rm MF}$ diverges $\eta^R=\eta_0^R=2.43450\ldots$. That is,

$$
(c_P)_{\rm MF} \stackrel{\eta^R\cong\eta_0^R}{=} \frac{\eta_0^R(\eta_0^R-2)}{\eta_0^R-\eta^R}+\mathcal{O}(1)=\frac{1.05779\ldots}{\eta_0^R-\eta^R}+\mathcal{O}(1).
$$

$(c_P)_{\rm MF}$ becomes negative for $\eta_0^R<\eta^R<\eta_C^R$. It keeps negative in the C–MC section till the point $\eta^R=\eta_1^R=2.14675\ldots$ where it becomes positive. The point $\eta_1^R$ is defined by the equation

$$
24f_{\rm MF}^2(\eta_1^R)+(4\eta_1^R-19)f_{\rm MF}(\eta_1^R)+\frac{\eta_1^R}{2}=0. \tag{144}
$$

The speed of sound squared at the surface in the mean field approximation takes the form

$$
\frac{v_s^2}{T}=\frac{f_{\rm MF}(\eta^R)}{3}\left[4+\frac{3f_{\rm MF}(\eta^R)+\frac{\eta^R}{2}-2}{6f_{\rm MF}^2(\eta^R)+\left(\eta^R-\frac{11}{2}\right)f_{\rm MF}(\eta^R)+\frac{1}{2}}\right], \tag{145}
$$

where we used Eqs. (57) and (128). We plot $\frac{v_s^2}{T}$ as a function of $\eta^R$ in Fig. 15. We see that $\frac{v_s^2}{T}(\eta^R)$ is positive and decreasing with $\eta^R$ in the whole interval between $\eta^R=0$ and C. At the point C it takes the value $\frac{v_s^2}{T}(\eta_C^R)=11/18$. Then, $\frac{v_s^2}{T}(\eta^R)$ decreases between C and MC

![](./images/812449694637621249_17.jpg)

Fig. 15. The speed of sound squared at the surface divided by the temperature, $v_s^2/T$, as a function of $\eta$ from mean field (Eq. (143)). Notice that $v_s^2/T$ takes the value $11/18$ at the critical point $\eta=\eta_C$ and becomes negative beyond $\eta_1^R=2.14675\ldots$ in the second sheet.

becoming negative at $\eta_1^R=2.14675\ldots$ in the second sheet where it vanishes. Notice that $\frac{v_s^2}{T}(\eta^R)$ and $(c_P)_{\text{MF}}$ vanish at the same point $\eta_1^R$ defined by Eq. (144).

$v_s^2<0$ indicates an instability. That is, small density fluctuations grow exponentially in time instead of propagating harmonically. It is remarkable that $v_s^2$ becomes negative at $\eta_1^R=2.14675\ldots$ in the second sheet before but near the MC critical point $\eta_{\text{MC}}^R=2.03085\ldots$ in the second sheet. Somehow, the change of sign in $v_s^2$ announces the MC critical point.

$\frac{v_s^2}{T}(\eta^R)$ tends to $-\infty$ for $\eta^R\downarrow\eta_{\text{MC}}^R$. Notice that the denominator in Eq. (145) exactly vanishes at $\eta^R=\eta_{\text{MC}}^R$ (see Table 1).

The adiabatic compressibility $\kappa_S$ is not here an independent quantity. We find from Eqs. (55), (137), (139) and (143),

$$
\kappa_S=\frac{c_V}{c_P}\kappa_T=\frac{3}{f_{\text{MF}}(\eta^R)}\frac{12f_{\text{MF}}^2(\eta^R)+(2\eta^R-11)f_{\text{MF}}(\eta^R)+1}{48f_{\text{MF}}^2(\eta^R)+(8\eta^R-38)f_{\text{MF}}(\eta^R)+\eta^R}.
$$

That is,

$$
\kappa_S=\frac{T}{v_s^2}.
$$

<table>
<caption>Table 1<br>Values of the critical points in the three ensembles GC, C and MC (using mean field) and further characteristic points for spherical symmetry. $pV/[NT]$, $E$ and $S\rightarrow-\infty$ for $\eta^{R}\uparrow\eta_{\text{GC}}^{R}$ and $\eta^{R}\uparrow\eta_{C}^{R}$. Notice that $\eta_{\text{min}}$, $\eta_{1}$ and $\eta_{\text{MC}}$ are in the second Riemann sheet</caption>
<thead>
<tr>
<th>Point</th>
<th>$\lambda$</th>
<th>$\eta^{R}$</th>
<th>Defining equation</th>
<th>$f_{\text{MF}}(\eta^{R})$</th>
<th>Physical meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>GC</td>
<td>1.7772…</td>
<td>0.797375…</td>
<td>$2 - 3\eta_{\text{GC}}^{R}f_{\text{MF}}(\eta_{\text{GC}}^{R}) = 0$</td>
<td>0.836076…</td>
<td>Collapse in the GCE</td>
</tr>
<tr>
<td>3</td>
<td>3.38626…</td>
<td>1.73745…</td>
<td>$3 - \eta^{R} + \chi(\lambda) = 0$</td>
<td>0.622424…</td>
<td>Energy density<br>vanishes at $r = 0$</td>
</tr>
<tr>
<td>2</td>
<td>4.73739…</td>
<td>2.18348…</td>
<td>$2f_{\text{MF}}(\eta_{2}^{R}) - 1 = 0$</td>
<td>0.5</td>
<td>Total energy vanishes</td>
</tr>
<tr>
<td>0</td>
<td>6.45077…</td>
<td>2.43450…</td>
<td>$6f_{\text{MF}}(\eta_{0}^{R}) - \eta_{0}^{R} = 0$</td>
<td>0.40575…</td>
<td>$\kappa_{T}$ and $c_{P}$ diverge</td>
</tr>
<tr>
<td>C</td>
<td>8.993195…</td>
<td>2.517551…</td>
<td>$1 - 3f_{\text{MF}}(\eta_{C}^{R}) = 0$</td>
<td>$1/3$</td>
<td>Collapse in the CE,<br>$c_{V}$ diverges</td>
</tr>
<tr>
<td>Min</td>
<td>22.5442…</td>
<td>2.20731…</td>
<td>$f_{\text{MF}}'(\eta_{\text{min}}^{R}) = 0$</td>
<td>0.264230…</td>
<td>Minimum of<br>$pV/[NT]$<br>in the gas phase</td>
</tr>
<tr>
<td>1</td>
<td>25.7991…</td>
<td>2.14675…</td>
<td>$\begin{aligned} 48f_{\text{MF}}^{2}(\eta_{1}^{R})&\\ -(38 - 8\eta_{1}^{R})f_{\text{MF}}(\eta_{1}^{R})&\\ + \eta_{1}^{R} = 0& \end{aligned}$</td>
<td>0.265290…</td>
<td>$v_{s}^{2}$ and $c_{P}$ vanish</td>
</tr>
<tr>
<td>MC</td>
<td>34.36361…</td>
<td>2.03085…</td>
<td>$\begin{aligned} 12f_{\text{MF}}^{2}(\eta_{\text{MC}}^{R})&\\ -(11 - 2\eta_{\text{MC}}^{R})f_{\text{MF}}(\eta_{\text{MC}}^{R})&\\ + 1 = 0& \end{aligned}$</td>
<td>0.273512…</td>
<td>Collapse in the MCE,<br>$c_{V}$ vanishes</td>
</tr>
</tbody>
</table>

## 8. Discussion

We have presented here a set of new results for the self-gravitating thermal gas obtained by Monte Carlo and analytic methods. They provide a complete picture for the thermal self-gravitating gas.

Contrary to the usual hydrostatic treatments [8,9], we do not assume here an equation of state but we obtain the equation of state from the partition function (see Eq. (41)). We find at the same time that the relevant variable is here $\eta^{R} = Gm^{2}N/[V^{1/3}T]$. The relevance of the ratio $Gm^{2}/[V^{1/3}T]$ has been noticed on dimensionality grounds [9]. However, dimensionality arguments alone cannot single out the crucial factor $N$ in the variable $\eta^{R}$.

The crucial point is that the thermodynamic limit exist if we let $N\rightarrow\infty$ and $V\rightarrow\infty$ keeping $\eta^{R}$ fixed. Notice that $\eta$ contains the ratio $NV^{-1/3}$ and not $N/V$. This means that in this thermodynamic limit $V$ grows as $N^{3}$ and thus the volume density $\rho = N/V$ decreases as $\sim N^{-2}$. $\eta$ is to be kept fixed for a thermodynamic limit to exist in the same way as the temperature. $pV$, the energy $E$, the free energy, the entropy are functions of $\eta$ and $T$ times $N$. The chemical potential, specific heat, etc. are just functions of $\eta$ and $T$.

We find collapse phase transitions both in the canonical and in the microcanonical ensembles. They take place at different values of the thermodynamic variables and are of different nature. In the CE the pressure becomes large and negative in the collapsed phase. The phase transition in the MCE is sometimes called ‘gravothermal catastrophe’. We find that the temperature and pressure increase discontinuously at the MCE transition. Both are zeroth order phase transitions (the Gibbs free energy is discontinuous). The two phases cannot coexist in equilibrium since the pressure has different values at each phase.

The parameter $\eta^R$ (introduced in Eq. (32)) can be related to the Jeans length of the system

$$
d_{\mathrm{J}}=\sqrt{\frac{3 T}{m}} \frac{1}{\sqrt{G m \rho}},
\tag{146}
$$

where $\rho \equiv N / V$ stands for the number volume density. Combining Eqs. (32) and (146) yields

$$
\eta^{R}=3\left(\frac{L}{d_{\mathrm{J}}}\right)^{2}.
$$

We see that the phase transition in the canonical ensemble takes place for $d_{\mathrm{J}} \sim L$. (The precise numerical value of the proportionality coefficient depends on the geometry.) For $d_{\mathrm{J}}>L$ we find the gaseous phase and for $d_{\mathrm{J}}<L$ the system condenses as expected. Hence, the collapse phase transition in the canonical ensemble is related to the Jeans instability.

The latent heat of the transition $(q)$ is negative in the CE transition indicating that the gas releases heat when it collapses (see Eq. (67)). The MCE transition exhibits an opposite behaviour. The Gibbs free energy increases at the MCE collapse phase transition (point MC in Fig. 1) whereas it decreases at the CE transition (point T in Fig. 1, see Eq. (66)). Also, the average distance between particles increases at the MCE phase transition whereas it decreases dramatically in the CE phase transition. These differences are related to the MCE constraint keeping the energy fixed whereas in the CE the system exchanges energy with an external heat bath keeping fixed its temperature. The constant energy constraint in the MCE keeps the gas stable in a wider domain and makes the collapse transition softer than in the CE. Notice that the core is much tighter and the halo much smaller in the CE than in the MCE (see Figs. 4 and 6).

## Acknowledgements

One of us (H.J. de V.) thanks M. Picco for useful discussions on Monte Carlo methods. We thank S. Bouquet for useful discussions and J. Katz for calling our attention on Ref. [24].

## Appendix A. Functional integration measure in the mean field approach

We follow the derivation of Ref. [20] for the functional integral measure. We want to recast

$$
e^{\Phi_{N}(\eta)}=\int_{0}^{1} \cdots \int_{0}^{1} \prod_{l=1}^{N} d^{3} r_{l} e^{\eta u\left(\vec{r}_{1}, \ldots, \vec{r}_{N}\right)},
\tag{A.1}
$$

as a functional integral in the large $N$ limit.

We start by dividing the domain of integration (of unit volume) into $M$ cells. Each cell is of volume $\omega_r$ and contains $k_r$ particles with $1 \leqslant r \leqslant M$. Therefore,

$$
\sum_{r=1}^{M} k_{r}=N, \quad \sum_{r=1}^{M} \omega_{r}=1.
$$

We can thus rewrite the multiple integral (A.1) as follows:

$$
e^{\Phi_{N}(\eta)}=\sum_{k_{1}, \ldots, k_{M}} \delta\left(N-\sum_{r=1}^{M} k_{r}\right) \frac{N!}{\prod_{r=1}^{M} k_{r}!} \prod_{r=1}^{M}\left(\omega_{r}\right)^{k_{r}} e^{-J},
$$

where [20]
$$
\begin{aligned}
J= & -\frac{1}{2} \sum_{r, r^{\prime}} k_{r} k_{r^{\prime}} V_{r, r^{\prime}}+\frac{1}{2} \sum_{r} k_{r} V_{r, r} \\
& +\frac{1}{2} \sum_{r, r^{\prime}, r^{\prime \prime}} k_{r} k_{r^{\prime}} k_{r^{\prime \prime}}\left[\left\langle V_{r, r^{\prime}} V_{r, r^{\prime \prime}}\right\rangle-\left\langle V_{r, r^{\prime}}\right\rangle\left\langle V_{r, r^{\prime \prime}}\right\rangle\right]+\cdots,
\end{aligned}
$$

and
$$
V_{r, r^{\prime}}=\left.\frac{1}{\omega_{r} \omega_{r^{\prime}}} \frac{\eta}{N} \int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|}\right|_{\vec{r}_{1} \in \omega_{r}, \vec{r}_{2} \in \omega_{r^{\prime}}}.
$$

Assuming $1 / N \ll \omega_{r}<N^{-2 / 3}$ one can neglect in $J$ terms quadratic and higher in $V_{r, r^{\prime}}$ [20].

The particle density is defined as
$$
N \rho(\vec{r}) \equiv \sum_{r=1}^{M} \frac{k_{r}}{\omega_{r}} \theta\left(\vec{r} \in \omega_{r}\right).
$$

Therefore, we can write the sums over $r$ as integrals in the following way
$$
\frac{1}{2} \sum_{r, r^{\prime}} k_{r} k_{r^{\prime}} V_{r, r^{\prime}}=\frac{\eta}{2 N} \int_{0}^{1} \int_{0}^{1} \frac{d^{3} r_{1} d^{3} r_{2}}{\left|\vec{r}_{1}-\vec{r}_{2}\right|} \rho\left(\vec{r}_{1}\right) \rho\left(\vec{r}_{2}\right).
$$

Using Stirlings' formula one finds that
$$
\prod_{r=1}^{M} \frac{\left(\omega_{r}\right)^{k_{r}}}{k_{r}!} \stackrel{N \rightarrow \infty}{=} \frac{1}{N^{N}} \prod_{r=1}^{M} \frac{1}{\sqrt{2 \pi k_{r}}} e^{-N \int d^{3} x \rho(\vec{x}) \log [\rho(\vec{x}) / e]}.
$$

Collecting all terms yields,
$$
N! \prod_{r=1}^{M} \frac{\left(\omega_{r}\right)^{k_{r}}}{k_{r}!} e^{-J} \stackrel{N \rightarrow \infty}{=} e^{\frac{N \eta}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho(\vec{x}) \rho(\vec{y})-N \int d^{3} x \rho(\vec{x}) \log [\rho(\vec{x}) / e]},
$$


whereas the constraint in the number of particles takes the form
$$
\delta\left(N-\sum_{r=1}^{M} k_{r}\right)=\frac{1}{N} \delta\left(\int d^{3} x \rho(\vec{x})-1\right),
$$
and finally,
$$
\begin{aligned}
e^{\Phi_{N}(\eta)} \stackrel{N \gg 1}{=} \frac{1}{N} \iint & D \rho e^{\frac{N \eta}{2} \int \frac{d^{3} x d^{3} y}{|\vec{x}-\vec{y}|} \rho(\vec{x}) \rho(\vec{y})-N \int d^{3} x \rho(\vec{x}) \log [\rho(\vec{x}) / e]} \\
& \times \delta\left(\int d^{3} x \rho(\vec{x})-1\right).
\end{aligned}
$$

Replacing the Dirac delta by its Fourier representation
$$
\frac{1}{N} \delta\left(\int d^{3} x \rho(\vec{x})-1\right)=\int \frac{d \hat{a}}{2 \pi} e^{i N \hat{a}\left(\int d^{3} x \rho(\vec{x})-1\right)},
$$
yields Eq. (71).

## Appendix B. Calculation of the saddle point

We prove in this appendix that the integral
$$
I(\lambda) \equiv \int_{0}^{\lambda} x^{2} d x\left[\chi^{\prime}(x)\right]^{2},\qquad(\mathrm{B}.1)
$$
takes the value
$$
I(\lambda)=\lambda \eta^{R}\left(6-\eta^{R}\right)-2 \lambda^{3} e^{\chi(\lambda)}.\qquad(\mathrm{B}.2)
$$

Here $\chi(x)$ is a regular solution of Eq. (118) in the interval $0 \leqslant x \leqslant \lambda$ fulfilling the relation (120).

We start by computing the derivative of $I(\lambda)$ in two ways. According to the definition (B.1)
$$
\frac{d I(\lambda)}{d \lambda}=\lambda^{2}\left[\chi^{\prime}(\lambda)\right]^{2}.
$$

Then, we compute the derivative of Eq. (B.2) with respect to $\lambda$ and use Eqs. (118) and (120). We find after calculation that both results coincide.

Finally, we observe that both Eqs. (B.1) and (B.2) vanish at $\lambda=0$. Therefore, Eq. (B.2) is valid.

## Appendix C. Abel's equation of first kind for the equation of state

In the mean field approximation the equation of state for spherical symmetry satisfies the first order differential equation (128)
$$
\eta^{R}\left(3 f_{\mathrm{MF}}-1\right) f_{\mathrm{MF}}^{\prime}\left(\eta^{R}\right)+\left(3 f_{\mathrm{MF}}-3+\eta^{R}\right) f_{\mathrm{MF}}=0,\qquad(\mathrm{C}.1)
$$

with the boundary condition $f_{\mathrm{MF}}(0)=1$.

We can solve Eq. (C.1) in power series in $\eta^R$ around the origin,

$$
f_{\mathrm{MF}}(\eta)=1+\sum_{n=1}^{\infty} f_{n} \eta^{n}. \tag{C.2}
$$

Inserting Eq. (C.2) into Eq. (C.1) yields the quadratic recurrence relation

$$
f_{n}=-\frac{1}{2 n+3}\left[f_{n-1}+3 \sum_{k=2}^{n} k f_{k-1} f_{n-k+1}\right], \quad \text { for } n \geqslant 2,
$$

where $f_{1}=-\frac{1}{5}$.

We find from this recurrence relation,

$$
f_{2}=-\frac{1}{175}, \quad f_{3}=-\frac{2}{1575}, \quad f_{4}=-\frac{991}{3031875}.
$$

All coefficients $f_{n}$ are negative rational numbers for $n \geqslant 1$. They decrease very fast with $n$ as

$$
f_{n} \stackrel{n \gg 1}{=}-\frac{0.0956678 \ldots}{\left[\eta_{C}^{R}\right]^{n} n^{3 / 2}}\left[1+\mathcal{O}\left(\frac{1}{n}\right)\right].
$$

This formula reproduces the large orders of the expansion of $\sqrt{\eta_{C}^{R}-\eta^{R}}$ describing the behaviour of $f_{\mathrm{MF}}(\eta)$ near $\eta_{C}^{R}$ (see Eq. (132) and Ref. [23])

$$
\sqrt{\eta_{C}^{R}-\eta^{R}}=-\frac{1}{2} \sqrt{\frac{\eta_{C}^{R}}{\pi}} \sum_{n=0}^{\infty} \frac{\Gamma\left(n-\frac{1}{2}\right)}{n!}\left(\frac{\eta^{R}}{\eta_{C}^{R}}\right)^{n}.
$$

Notice that

$$
-\frac{1}{2} \sqrt{\frac{\eta_{C}^{R}}{\pi}} \frac{\Gamma\left(n-\frac{1}{2}\right)}{n!} \stackrel{n \gg 1}{=}-\frac{0.447594 \ldots}{n^{3 / 2}}\left[1+\mathcal{O}\left(\frac{1}{n}\right)\right],
$$

and that $0.213738 \ldots \times 0.447594 \ldots=0.0956678 \ldots$

The power series (C.2) thus has a radius of convergence $\eta_{C}^{R}=2.517551 \ldots$ The singularity of $f_{\mathrm{MF}}(\eta)$ nearest to the origin is thus the critical point.

## References

[1] H.J. de Vega, N. Sánchez, Statistical mechanics of the self-gravitating gas: II. Local physical magnitudes and fractal structures, Nucl. Phys. B 625 (2002) 460, next article in this issue.
[2] L.D. Landau, E.M. Lifchitz, Physique Statistique, 4ème édition, Mir-Ellipses, 1996.
[3] H.J. de Vega, N. Sánchez, F. Combes, Nature 383 (1996) 56.
[4] H.J. de Vega, N. Sánchez, F. Combes, Phys. Rev. D 54 (1996) 6008.
[5] H.J. de Vega, N. Sánchez, F. Combes, Astrophys. J. 500 (1998) 8.
[6] H.J. de Vega, N. Sánchez, F. Combes, in: N. Sánchez, A. Zichichi (Eds.), Current Topics in Astrofundamental Physics: Primordial Cosmology, NATO ASI at Erice, Vol. 511, Kluwer, 1998.

[7] D. Pfenniger, F. Combes, L. Martinet, Astron. Astrophys. 285 (1994) 79;
D. Pfenniger, F. Combes, Astron. Astrophys. 285 (1994) 94.

[8] S. Chandrasekhar, An Introduction to the Study of Stellar Structure, Chicago Univ. Press, 1939.

[9] See, for example, W.C. Saslaw, Gravitational Physics of Stellar and Galactic Systems, Cambridge Univ.
Press, 1987.

[10] R. Emden, Gaskugeln, Teubner, Leipzig und Berlin, 1907.

[11] D. Lynden-Bell, R.M. Lynden-Bell, Mon. Not. R. Astron. Soc. 181 (1977) 405;
D. Lynden-Bell, cond-mat/9812172.

[12] D. Lynden-Bell, R. Wood, Mon. Not. R. Astron. Soc. 138 (1968) 495.

[13] V.A. Antonov, Vestnik Leningrad Univ. 7 (1962) 135.

[14] T. Padmanabhan, Phys. Rep. 188 (1990) 285.

[15] G. Horwitz, J. Katz, Astrophys. J. 211 (1977) 226;
G. Horwitz, J. Katz, Astrophys. J. 222 (1978) 941.

[16] J. Binney, S. Tremaine, Galactic Dynamics, Princeton Univ. Press.

[17] See, for example, W. Dehnen, astro-ph/0011568.

[18] L. Landau, E. Lifchitz, Mécanique des Fluides, Mir, Moscou, 1971.

[19] See, for example, K. Binder, D.W. Heermann, Monte Carlo Simulations in Statistical Physicks, Springer
Series in Solid-State, Vol. 80, Springer, Berlin, 1988.

[20] L.N. Lipatov, JETP 45 (1978) 216.

[21] E. Kamke, Differentialgleichungen, Chelsea, New York, 1971.

[22] I.M. Gelfand, G.E. Shilov, Distribution Theory, Vol. 1, Academic Press, New York, 1968.

[23] I.S. Gradshteyn, I.M. Ryshik, Table of Integrals, Series and Products, Academic Press, New York, 1980.

[24] J. Katz, I. Okamoto, astro-ph/0004179.