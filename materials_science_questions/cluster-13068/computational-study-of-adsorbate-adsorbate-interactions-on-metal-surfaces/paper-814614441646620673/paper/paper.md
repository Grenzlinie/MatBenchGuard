# Contribution to the cohesive energy of simple metals: Spin-dependent effect*
O. Gunnarsson
Institute of Theoretical Physics, Chalmers University of Technology, S-402 20 Göteborg, Sweden

B. I. Lundqvist† and J. W. Wilkins
Laboratory of Atomic and Solid State Physics and Materials Science Center, Cornell University, Ithaca, New York 14850

(Received 18 March 1974)

We find that within local-density schemes for calculating the cohesive energy of simple metals greater sophistication in treating the atom is required. The outermost electron in, e.g., the sodium atom has an unpaired spin. For this and the many similar cases a generalization of the scheme to a spin-density-functional formalism is needed. Application of the local-spin-density approximation gives, e.g., the energy of the hydrogen atom within 1.6% of the exact value, while the local-density approximation is 10% off. The improvement is due to our use of a better model system, i.e., the spin-polarized electron liquid, in the local approximation. We elaborate on the factors leading to the smallness of the error, and we find that there is a systematic partial cancellation between too attractive and too repulsive contributions to the binding for valence electrons in hydrogen and similar atoms.
When we extend Tong's calculation for sodium metal along these lines, we find the cohesive energy to lie within 4% of the experimental value. A similar improvement is found for lithium. The spin-density scheme should be a very useful practical method for a large range of applications, including the calculation of chemisorption and charge transfers.

## I. INTRODUCTION

In this paper we want to point out how a calculation of the cohesive energy of sodium by Tong and similar applications of the Kohn-Sham scheme can be improved to give results of a useful accuracy.

The Kohn-Sham density-functional formalism¹ provides an efficient, useful scheme to calculate ground-state properties of electron systems. In particular, this is true in situations where the electron density has a weak and slow variation in space. Then the effects of exchange and correlation can be approximated by a local potential in the Schrödinger-like equation for the calculation of the density and by a local expression for the corresponding contribution to the total energy of the system. Parameters for these two quantities can be extracted from results for the homogeneous electron liquid.

Among real physical systems, sodium metal would seem to be an ideal system for applying this scheme. Tong² has made such an application. In a full, self-consistent computation, in which the only parameter input is the total number of electrons per atom, $Z$=11, he finds the equilibrium lattice constant and the compressibility within 1.3 and 11%, respectively, of the experimental data.² However, the calculated value for the cohesive energy is 23% larger than the experimental result.²

The former two quantities concern only the solid state, while the cohesive energy is obtained by comparing the energies of the solid and atomic states. Following a suggestion by Kohn³ we seek the source of the discrepancy between the calculated and measured cohesive energies in the atomic part of the calculation. By performing calculations for the hydrogen atom we are able to compare results from the Kohn-Sham scheme with those of the exact solution and in this way get an indication of the applicability of the local-density (LD) approximation used by Tong² and many others.

The purpose of this paper is to show by numerical examples and by *a priori* arguments that for the hydrogen and sodium atoms and for other applications with unpaired valence electrons a *spin*-density formalism should be used.⁴,⁵

We find that a local-spin-density (LSD) approximation gives a value for the energy of the hydrogen atom only 1.6% smaller in magnitude than the exact Rydberg energy, as compared to the 10% deviation in the LD approximation. Thus, inclusion of spin-polarization effects lowers the hydrogen atomic energy by 1.1 eV. We may use this number for a basis to estimate the same effects in other atoms. Basically the spin-polarization-dependent contribution to the exchange-correlation energy scales like (density)¹/³ or $r_{s}^{-1}$, where $r_{s}$ is the commonly used electron-gas parameter. Taking the density in the valence-electron orbit as characteristic for the atom, we get the characteristic values $\bar{r}_{s}$=1.8 for H and 4.7 for Na. A crude estimate of this correction to the energy of the sodium atom should then be $(\frac{1.8}{4.7})1.1$ eV =0.4 eV. We see that this lowering of the cohesive energy is of roughly the right size to account for the discrepancy (0.26 eV/atom) between Tong's theoretical result for the cohesive energy (32.0 kcal/mole=1.39 eV/atom) and the experimental number (26.0 kcal/mole

---
10

=1.13 eV/atom). In a more detailed calculation, to be described below, we find the spin-density- functional formalism in the LSD approximation to give a value for the cohesive energy of sodium within 4% of the experimental number.

In Sec. II we briefly summarize the Kohn-Sham density-functional formalism and its generalization to spin densities. In another paper⁶ we have cal- culated the exchange-correlation energy and po- tentials to be used in the scheme from a study of the homogeneous electron liquid in an approxima- tion which focuses on the dynamical effects of the correlation on the one-electron spectrum. Here we only present the resulting interpolation for- mulas, which we then use in the applications. The calculation on hydrogen is described in Sec. III. We find that the good results in the LSD approxi- mation are connected with an unexpetedly good representation of the exchange-correlation hole in the region of space where the 1s electron is most likely to be. In addition, for the hydrogenic ions we find results having small relative errors, too, and illustrating trends consistent with qualitative arguments about the exchange-correlation hole.
The calculation of the cohesive energy of sodium is described in Sec. IV. Additional evidence for the importance of using the LSD approximation for the unpaired atomic valence electron is given there by a perturbative estimate of the cohesive energy of lithium. We conclude in Sec. V with some re- marks about the broad applicability of the spin- density-functional formalism.

## II. KOHN-SHAM SCHEME

The Kohn-Sham density-functional scheme for the ground state of an interacting electron system in an external potential $v(\vec{r})$ is based on a varia tional principle,⁷ which states that there exists a universal functional of the density $F[n(\vec{r})]$ that has as its minimum value the correct ground-state en- ergy associated with $v(\vec{r})$. This minimum princi- ple does not apply strictly to approximate function- als, as we then do not know whether the minimum value is above or below the correct ground-state energy, only that the scheme gives the appropriate density for the chosen functional. By an unphysical approximation, as in the so-called $X\alpha$ method⁸ with a large $\alpha$, we could easily obtain minimum values far below the correct ground-state energy. Hence, some physical insight is required in the construction of an approximate functional, as we will discuss later. In many situations this re- quires a generalization of the original scheme.

The Kohn-Sham self-consistent scheme in the local-density (LD) approximation is summarized in Eqs. (1)-(9) of Tong's paper.² The scheme can be generalized to apply for spin-polarized sys- tems.¹,⁹ The case where the spin density is local- ly restricted either along or opposite some fixed direction, the same throughout the system, has a large range of applications. For this case the generalization amounts to (i) replacing the density $n(\vec{r})$ in Eqs. (1)-(9) of Tong's paper by a two- component spin density $n_{s}(\vec{r})$, with one component $[n_{+}(\vec{r})]$ for spin-up and one $[n_{-}(\vec{r})]$ for spin-down electrons, (ii) adding a spin index $s$ to the set $i$ of Schrödinger-equation solutions on Tong's Eq. (3), and (iii) performing the appropriate summa- tions over the spin index $s$.

Within the LD approximation [Tong's Eq. (2)] the exchange-correlation energy and potential can be obtained from results for the homogeneous, paramagnetic electron liquid. When accounting for exchange and correlation, the theory in this form thus views the electrons as a spin-compen- sated electron liquid. Though there are good reasons to have confidence in this for such systems as simple, paramagnetic metals, e.g., sodium metal, it is obviously not appropriate for systems with unpaired electrons, like the hydrogen atom, the outermost electron in the sodium atom,³ and ferromagnetic systems.¹,⁶,⁹

Our improvement in the applications described in the subsequent sections is to use the spin- density-functional formalism instead of the density- functional formalism. We assume the local-spin- density (LSD) approximation to hold, i.e., Tong's Eq. (2) generalized to spin densities,
$$
\begin{aligned}
E^{\mathrm{xc}}\left[n_{+}, n_{-}\right] & \simeq \int \epsilon^{\mathrm{xc}}\left(n_{+}(\vec{r}), n_{-}(\vec{r})\right) n(\vec{r}) d \vec{r} \\
& \equiv \int \epsilon^{\mathrm{xc}}\left(\gamma_{s}(\vec{r}), \zeta(\vec{r})\right) n(\vec{r}) d \vec{r}.
\end{aligned}\tag{1}
$$

For the description of the calculation of the ex- change-correlation energy and potentials for the homogeneous, spin-polarized electron liquid, we refer the reader to Ref. 6. In our computations here we use as inputs the following interpolation formulas for the exchange-correlation energy $\epsilon^{\mathrm{xc}}$ and potentials $\mu_{s}^{\mathrm{xc}}$, expressed in terms of the electron-liquid parameters $\gamma_{s}$, defined by $4\pi\gamma_{s}^{3}a_{0}^{3}/3$ $=1/n$, and the fractional spin polarization $\zeta=(n_{+}$ $-n_{-})/n$:
$$
\epsilon^{\mathrm{xc}}\left(\gamma_{s}, \zeta\right)=\epsilon_{P}^{\mathrm{xc}}+\left(\epsilon_{F}^{\mathrm{xc}}-\epsilon_{P}^{\mathrm{xc}}\right) f(\zeta) \mathrm{Ry}, \tag{2}
$$
where
$$
f(\zeta)=\left[(1+\zeta)^{4 / 3}+(1-\zeta)^{4 / 3}-2\right] /\left(2^{4 / 3}-2\right)
$$
and
$$
\epsilon_{i}^{\mathrm{xc}}=\epsilon_{i}^{x}-c_{i}\left[\left(1+x_{i}^{3}\right) \ln \left(1+1 / x_{i}\right)+\frac{1}{2} x_{i}-x_{i}^{2}-\frac{1}{3}\right],
$$
$$
i=P, F
$$
with $x_{i}=\gamma_{s}/r_{i}$, $\epsilon_{P}^{x}=-3/(2\pi\alpha r_{s})$, $\alpha=(4/9\pi)^{1/3}$, and $\epsilon_{F}^{x}=2^{1/3}\epsilon_{P}^{x}$ ($c_{P}=0.0666$, $c_{F}=0.0406$, $r_{P}=11.4$, and $r_{F}=15.9$), and

![](./images/814614441646620673_1.jpg)

FIG. 1. Exchange-correlation energy density of the hydrogen atom $\epsilon^{\mathrm{xc}}(r)$ (in Ry), as defined in Eq. (4), in the local-spin-density (LSD) and local-density (LD) approximations compared with the exact result. The LSD result is calculated from Eq. (2) with $\zeta=1$ and the LD result from the same equation with $\zeta=0$. The distance from the nucleus is denoted by $r$.

$$
\mu_{\pm}^{\mathrm{xc}}\left(r_{s}, \zeta\right)=-\frac{2}{\pi \alpha r_{s}}\left(\beta \pm \frac{1}{3} \frac{\delta \zeta}{1 \pm \gamma \zeta}\right) \mathrm{Ry}, \tag{3}
$$

where
$$\beta=1+0.0545 r_{s} \ln \left(1+11.4 / r_{s}\right),$$
$$\delta=1-0.036 r_{s}-1.36 r_{s} /\left(1+10 r_{s}\right),$$
and
$$\gamma=0.297.$$

These interpolation formulas reproduce the calculated values within about 1 and $2 \%$ respectively. $^{6}$ Not knowing the exact solution of the electron-gas problem, we cannot give a firm estimate of the error, but these results are likely to be within $0.1-0.2 \mathrm{eV}$ of the exact exchange-correlation energy and potentials for $r_{s}$ above about $1 .^{6}$ For smaller $r_{s}$ values the absolute error of the interpolation formula is expected to be slightly larger. $^{6}$

### III. HYDROGEN ATOM AND HYDROGENIC IONS

Approximations are introduced into the Kohn-Sham spin-density-functional scheme through approximations for the exchange-correlation energy functional $E^{\mathrm{xc}}\left[n_{+}, n_{-}\right]$. The exchange and correlation forces are fundamentally nonlocal in nature. In practical applications, however, we have had to resort to local approximations, like the LSD [Eq. (1)] and LD approximations [Eq. (2) in Ref. 2]. The fundamental theory says that such an approximation should be good only in the limit of weak and slow spatial variations of the spin density but has not yet provided any useful criteria for how strong and rapid variations we can use a local approximation.

#### A. Hydrogen atom

The hydrogen atom can provide an informative test case for the LD and LSD approximations, because (i) there is an exact solution to the problem available, and (ii) the electron density of the hydrogen atom is in a region $[r_{s}=(3 / 4)^{1 / 3} e^{2 r / 3}$ going from 0.9 and up] where the approximations and available electron-liquid data are commonly used. We will in this section present results for the hydrogen atom and then from a discussion of the exchange-correlation hole draw conclusions about the applicability of these approximations for other electron systems.

The electron of the hydrogen atom obviously has its spin unpaired. In the Kohn-Sham scheme, the appropriate local functional should then be for a spin-polarized, homogeneous electron liquid.

A straightforward, numerical application of the Kohn-Sham scheme with the LSD approximation gives the value $-13.38 \mathrm{eV}$ for the atomic energy of hydrogen in good agreement (within $1.6 \%$ ) with the exact result, $-13.60 \mathrm{eV}$.

The total energy is composed of a kinetic part and an electron-nucleus-interaction part. In the Kohn-Sham scheme there are in addition electrostatic and exchange-correlation terms, describing the intrinsic interaction of the electron-charge distribution [see Tong's Eq. (1)]. In an exact version of the scheme these latter two terms would cancel for the hydrogen atom, as the single electron does not interact with itself. In an approximate treatment the electrostatic integrals are handled exactly, while a model functional is used to simulate the role of the exchange-correlation forces in reducing (ideally, in eliminating) the repulsive electrostatic forces. Being approximate, such a model is bound to fail in some regions, and the best we can hope for is that we have a good representation in the important regions and some cancellation between the misrepresentations in other regions. Figure 1 is meant to illustrate that such is the case for the hydrogen atom in the LSD approximation. It shows the approximate and exact exchange-correlation-energy densities $\epsilon^{\mathrm{xc}}(r)$, defined by

$$
E^{\mathrm{xc}}=\int \epsilon^{\mathrm{xc}}(r) n(r) d^{3} r. \tag{4}
$$

We see that the difference between the LSD approximation $\epsilon^{\mathrm{xc}}(r) \simeq \epsilon^{\mathrm{xc}}\left(r_{s}(r), \zeta(r)\right)$ and the exact result is positive for large $r$ values, negative for small $r$, and zero at a distance about 1 Bohr radius from the nucleus, i.e., where the electron is most likely to be.

It should be noted from the figure that the result in the LD approximation deviates from the exact

![](./images/814614441646620673_2.jpg)

FIG. 2. Hartree $(V_{H})$ and exchange-correlation $(\mu_{+}^{xc})$ potentials of the electron in the hydrogen atom. The curve $\mu_{+}^{xc}+V_{H}$ is drawn to illustrate the relative constancy of the difference between the approximate (LSD) and exact $(=-V_{H})$ exchange-correlation potentials. Equation(3) has been used to get the LSD $(\zeta=1)$ and LD $(\zeta=0)$  results for $\mu_{+}^{xc}$ .
result for the whole r range of importance. Ac- cordingly, the energy value, - 12.25 eV, deviates significantly more $(10 \%)$ from the exact result. This is not surprising, because in describing the exchange and correlation effects by the LD approx- imation we are simulating the fully spin-polar- ized electron distribution of the hydrogen atom locally by a spin-compensated homogeneous elec- tron liquid. A priori, the spin-polarized electron liquid, used in the LSD approximation, should be a more appropriate model system. The same is true in all applications on systems with unpaired electrons. Stated in the Hartree-Fock practitioner jargon: The "unrestricted" rather than the "re- stricted" scheme should be used.
The "wave function" in the Kohn-Sham scheme has to be calculated from a Schrodinger equation[Eq. (3) of Ref. 2], which in the approximate ver- sion has a potential differing from the true Keplerpotential. In Fig. 2 we show the electrostatic $V_{H}$  and the exchange-correlation potentials $\mu_{+}^{xc}$ for majority spin (s = +) electrons. The exact ex-change-correlation potential should equal $-V_{H}$  within a constant. $^{10}$ We see that the additional potential $V_{H}+\mu_{+}^{xc}$ is almost constant as a function of r in the LSD approximation. A constant shift in the potential does not affect the wave function. As a matter of fact, our calculated density de- viates everywhere less than $4 \%$ from the true hy drogenic density. The dashed curve illustrates the stronger r dependence of $V_{H}+\mu^{xc}$ in the LD ap proximation.
B. Exchange-correlation hole
Figure 1 raises questions about why the LSD ap- proximation gives such a good representation of the exchange-correlation-energy density $\epsilon^{xc}(r)$ and why the errors involved tend to cancel in the in- tegration giving $E^{xc}$ . Another question concerns the implications for other electron systems. We attempt to answer by both general, qualitative arguments and explicit calculations for the hydro- gen atom. The discussion will focus on the ex- change-correlation hole and the way the LSD ap- proximation closely models this quantity and elec- trostatic integrals over it that contribute to $E^{xc}$ . We will show the following.
(i) Near the nucleus the approximation overem- phasizes the higher-density regions. This leads to an LSD hole smaller than the exact one and thus $\epsilon_{LSD}^{xc}<\epsilon_{exact}^{xc} .$
(ii) In the tail the LSD hole is at the wrong place, being centered around the electron while the ex- act hole is around the nucleus, and has the wrong size, the low density in the tail making it too ex- tended. This makes $\epsilon_{LSD}^{xc}>\epsilon_{exact}^{xc}$ in this region.
(ii) The crossover region, where $\epsilon_{LSD}^{xc}=\epsilon_{exact}^{xc}$ , happens to occur around 1 a.u. for the hydrogen atom. Its location is affected by the magnitude of the electron-gas screening. The greater the screening, the smaller the LSD hole, and the smaller the misrepresentation in point (ii) above. In the hydrogen atom a large part of the tail is in a low-density regime with strong screening. In the hydrogenic ions, on the other hand, increasing nuclear charge increases the density and reduces the effect of screening. This reduces the ratio(crossover radius)/(orbital radius) with an in- creasing misrepresentation of $E^{xc}$ as a conse quence. Finally, for valence electrons in atomic systems with lower average valence-electron den- sity than the hydrogen atom, i.e., in the alkali atoms, the higher screening should contribute to an improved representation of $E^{xc}$ .
A central quantity in a discussion like this is theinteraction energy $^{11}$ 
$$E_{\text {int }}=\frac{1}{2} \int d^{3} r n(\overrightarrow{\mathrm{r}}) \int d^{3} r^{\prime} \frac{e^{2}}{\left|\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{r}}^{\prime}\right|} \rho_{\mathrm{xc}}\left(\overrightarrow{\mathrm{r}}, \overrightarrow{\mathrm{r}}^{\prime}\right). \quad(5)$$

The quantity
$$\rho_{\mathrm{xc}}\left(\overrightarrow{\mathrm{r}}, \overrightarrow{\mathrm{r}}^{\prime}\right)=\left[g\left(\overrightarrow{\mathrm{r}}, \overrightarrow{\mathrm{r}}^{\prime}\right)-1\right] n\left(\overrightarrow{\mathrm{r}}^{\prime}\right),\qquad(6)$$
 where $g(\overrightarrow{r}, \overrightarrow{r}')$ is the pair-correlation functions, expresses how the electronic charge density around a particular electron (at $\overrightarrow{r}$ ) is suppressed owing to the exchange and Coulomb interaction with that electron. In the electrostatic energy, omitted

![](./images/814614441646620673_3.jpg)

FIG. 3. Illustration of the similarities and differences between the exact and approximate (LSD approximation, using the random-phase approximation for the spin-polarized electron liquid) exchange-correlation holes. We have plotted the contribution $\epsilon(\vec{r}, r_{0})$ [Eq. (7)] to the interaction energy density at different points $r$ due to the suppressed charge at a distance $r_{0}$ from the point $\vec{r}$. The area under the curve gives the interaction energy density at $\vec{r}$.

from Eq. (5), the Coulomb interaction between the charge distributions $-e n(\vec{r})$ and $-e n(\vec{r}^{\prime})$ is included, and Eq. (5) corrects for the fact that the charge is suppressed. The quantity $\rho_{\mathrm{xc}}(\vec{r}, \vec{r}^{\prime})$ then describes this decreased density, called the exchange-correlation hole. It is this quantity which is described approximately in the LSD approximation.

In the hydrogen atom the exact pair-correlation function $g(\vec{r}, \vec{r}^{\prime})$ is zero. Accordingly, the exchange-correlation hole is $\rho_{\mathrm{xc}}(\vec{r}, \vec{r}^{\prime})=-n(\vec{r}^{\prime})$; i. e., it is centered around the nucleus and independent of the electron position $\vec{r}$. In the LSD (and LD) approximation, the hole is assumed to be spherical around $\vec{r}$. The hole is thus misrepresented in some regions. The interaction energy, however, can still come out reasonable owing to cancellation of errors in the integration.

The simplest form of the arguments uses the fact that the size of the exchange-correlation hole in the homogeneous electron liquid decreases as the density increases. As the density is highest at the nucleus $(r=0)$, the LSD approximation overestimates the density surrounding an electron there, and the LSD hole will be too small there. The contribution to the integral in Eq. (5) from this region will thus be too negative. For large $r$, owing to the low local density, the hole will be too extended. Besides, it has the wrong shape. This will give a contribution to $E_{\text {int }}$ which is not negative enough.

By considering an explicit calculation for the hydrogen atom we can see how these arguments work and what increased sophistications are needed to understand more complicated systems. Consider the calculation of the quantity
$$
\epsilon\left(\vec{r}, r_{0}\right)=\frac{e^{2}}{r_{0}} \int d^{3} r^{\prime} \rho_{\mathrm{xc}}\left(\vec{r}, \vec{r}^{\prime}\right) \delta\left(\left|\vec{r}-\vec{r}^{\prime}\right|-r_{0}\right). \quad(7)
$$

This quantity is suitable for comparing exact and LSD-approximation results (Fig. 3), since (i) after integration over $r_{0}$ it gives the interaction-energy density in Eq. (5) for different $r$ values, and (ii) it is a spherical average of the exact hole, which can then be readily compared with the spherical hole of the LSD approximation. For the calculation of the pair-correlation function $g$ of the homogeneous, spin-polarized electron liquid we have here used the random-phase approximation. We see from Fig. 3 that the LSD approximation agrees well with the averaged exchange-correlation hole [Eq. (7)] for $r$ around 1 a.u., but less well, when the electron is either closer to the nucleus (hole is too contracted) or further away (hole is too extended). Figure 3 thus substantiates the qualitative arguments given above. It is due to the heavy weight on the region around $r=1$ a.u. and due to the cancellation between the small positive errors from the outer region and the small negative errors from the inner region that the exchange-correlation energy agrees so well for the hydrogen atom.

To understand the differing behavior of the hole it is important to keep three length scales in mind $^{12}$:

(i) The inhomogeneity length scale, which characterizes the density variations: In hydrogen and hydrogenic ions the orbital radius $a_{1 s}$ is a convenient measure. In the uniform electron gas the length is of course infinite, while for alkali atoms it lies in between. The next two lengths, while defined initially for the homogeneous electron gas, apply to the inhomogeneous one, as well, where their values are accordingly modified by the changing local density.

(ii) The Fermi length $\lambda_{F}=0.52 r_{s}(1+\zeta)^{-1 / 3}$ a.u., where $\zeta=0$ in the paramagnetic limit and 1 in the ferromagnetic limit: Crudely speaking, this length sets the size of the hole in the high-density region, where one often says exchange effects dominate.

(iii) The Thomas-Fermi screening length

$$
\begin{aligned}
\lambda_{\mathrm{TF}}= & 1.23 r_{s}^{-1 / 2} \lambda_{\mathrm{F}}\left\{2(1+\zeta)^{2 / 3} /\right. \\
& {\left.\left[(1+\zeta)^{1 / 3}+(1-\zeta)^{1 / 3}\right]\right\}^{1 / 2} ; }
\end{aligned}
$$

This length scales the size of the hole in the lowerdensity region, where, again, one says that correlation effects dominate. It would be tempting to choose the density, where the latter two lengths are equal $(r_{s}=1.5$, when $\zeta=0)$ as the dividing line between exchange and correlation domination. In fact, of course, there is no line and only a diffuse boundary between the high- and low-density limits.

### C. Hydrogenic ions
An illustration of increasing exchange domination and hence a resulting deterioration in the balance between exchange and correlation seen in the hydrogen atom is provided by the one-electron or hydrogenic ions. Increasing nuclear charge $Z$ in the hydrogenic problem gives a higher and spatially more varying electron density, $r_{s}$ going from $0.9 / Z$ and up, $\bar{r}_{s}=1.8 / Z$, and the orbital radius $a_{1 s}$ decreasing like $1 / Z$ a. u. The latter characteristic length should be compared with $\lambda_{\mathrm{F}}$ and $\lambda_{\mathrm{TF}}$. Just as for the hydrogen atom, the LSD approximation gives too contracted a hole close to the nucleus and too extended a hole in the outer parts of the electron distribution. However, as $Z$ increases, there is a growing fraction of the electron-density distribution in the exchange-dominated regime. Relatively speaking, i. e., relating $\lambda_{\mathrm{F}}$ and $\lambda_{\mathrm{TF}}$ to $a_{1 s}$, the exchange-correlation hole is more extended in this regime. The approximate hole is thus too extended in a relatively larger region of space. The balance found for the hydrogen atom is thus slightly upset, and as a result the approximate $E^{\mathrm{xc}}$ will not be negative enough, the relative error growing with $Z$. As both $\lambda_{\mathrm{F}}$ and $a_{1 s}$ scale like $Z^{-1}$, the relative error in accounting for $E^{\mathrm{xc}}$ should approach a constant in the limit of large $Z$.

As the kinetic and electron-nucleus-interaction energies go like $Z^{2}$, while the interelectronicinteraction energy increases proportional to $Z$, the relative importance of the latter contribution decreases as $Z$ increases. The relative error in the total energy should thus decrease with increasing $Z$.

Table I shows how all these features are present in the results from explicit calculations. In addition, the table shows that the relative errors are rather small throughout the series.

We see that the limiting value of the relative error in accounting for $E^{\mathrm{xc}}$ for large $Z$ is about $14 \%$. The same relative error is obtained for the hydrogen atom $(Z=1, E=-11.4 \mathrm{eV})$ when the Hartree-Fock results
$$
\epsilon^{x}=-3\left[(1+\zeta)^{4 / 3}+(1-\zeta)^{4 / 3}\right] / 4 \pi \alpha r_{s} \mathrm{Ry}
$$
and
$$
\mu_{ \pm}^{x}=-2(1 \pm \zeta)^{1 / 3} / \pi \alpha r_{s} \mathrm{Ry}
$$
are used instead of Eqs. (2) and (3), respectively. This is one way of illustrating that the hydrogenic ions for very large $Z$ are entirely in the exchangedominated regime. The last column of Table I shows how gradually this regime is reached even at small $\bar{r}_{s}$.

It should be stressed here that we are not advocating the use of the LSD approximation for detailed descriptions of tightly bound electrons. Table I also shows that the absolute error grows with $Z$.

### D. Implications
Our point has been to show that the applications to the exactly solvable cases support the qualitative arguments. We argued earlier that the approximate hole is too extended in the outer parts of the atom (large $r$ ). Now we see that this misrepresentation is reduced for densities in the correlation-dominated regime. A smaller hole gives a more negative interaction-energy density. Accordingly, we expect that for valence electrons in atomic systems with lower average valence-electron density than the hydrogen atom, such as the alkali atoms, the LSD curve for the exchange-correlation-energy density should come closer to the exact result at large $r$ than the hydrogen-atom curve shown in Fig. 1. This would imply that the

<table>
<caption>TABLE I. Total energy $E$ and exchange-correlation energy $E^{\text{xc}}$ of the hydrogenic ions.</caption>
<thead>
<tr>
<th rowspan="2">$Z$</th>
<th rowspan="2">Ion</th>
<th rowspan="2">$\overline{r}_{s}$</th>
<th colspan="2">Total energy $E$ (eV)</th>
<th colspan="2">Error $\Delta E^{\text{xc}}$</th>
<th>Exact $E^{\text{xc}}$</th>
<th>$\Delta E^{\text{xc}}/E^{\text{xc}}$</th>
</tr>
<tr>
<td>exact: $-13.6Z^{2}$</td>
<td>LSD appr.</td>
<td>(eV)</td>
<td>$\Delta E^{\text{xc}}/E(\%)$</td>
<td>$8.5Z$ (eV)</td>
<td>(%)</td>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>H</td>
<td>1.8</td>
<td>$-13.6$</td>
<td>$-13.38$</td>
<td>0.22</td>
<td>1.6</td>
<td>8.5</td>
<td>2.6</td>
</tr>
<tr>
<td>2</td>
<td>He*</td>
<td>0.9</td>
<td>$-54.4$</td>
<td>$-53.3$</td>
<td>1.1</td>
<td>2.0</td>
<td>17.0</td>
<td>6.5</td>
</tr>
<tr>
<td>3</td>
<td>Li²⁺</td>
<td>0.6</td>
<td>$-122.4$</td>
<td>$-120.3$</td>
<td>2.1</td>
<td>1.7</td>
<td>25.5</td>
<td>8.2</td>
</tr>
<tr>
<td>5</td>
<td>B⁴⁺</td>
<td>0.4</td>
<td>$-340.0$</td>
<td>$-335.7$</td>
<td>4.3</td>
<td>1.3</td>
<td>42.5</td>
<td>10.1</td>
</tr>
<tr>
<td>10</td>
<td>Ne⁹⁺</td>
<td>0.2</td>
<td>$-1360$</td>
<td>$-1350$</td>
<td>10</td>
<td>0.7</td>
<td>85.0</td>
<td>11.8</td>
</tr>
<tr>
<td>50</td>
<td>In⁴⁹⁺</td>
<td>0.04</td>
<td>$-34013$</td>
<td>$-33956$</td>
<td>57</td>
<td>0.2</td>
<td>425</td>
<td>13.4</td>
</tr>
</tbody>
</table>

crossover between the LSD and the exact curves should lie further out, relative to the orbital radius, and that hence the exchange-correlation energy of the valence electron should be better accounted for by the LSD approximation here than in the hydrogen atom.

The core electrons have not been considered in the preceding. However, the essence of the argu- ment still holds with them included, and we esti- mate that at least for the alkali atoms the error introduced by them is smaller than the built-in un- certainty in Eqs. (2) and (3) (0.1-0.2 eV). In, for instance, Na (Li) the core-valence exchange and correlation effects contribute about $-0.3(-0.2)^{13}$ and $-0.1(-0.1)^{14} eV$ each to the total energy. The essential contributions to these effects come from the exchange-dominated region, where the local approximation might have an error up to about $15 \%$ , judging from our results for the hy drogenic ions. Similar numbers for this error have been obtained by Tong and Sham. $^{15}$ However, even a maximum error in this region will intro- duce a small error in the core-valence contribu- tion to $E^{xc}$ , well below 0.1 eV in sodium and lithium, for instance. In conclusion, the argu- ments presented above should cause the reader, we believe, to attach significance to the numbers presented in Sec. IV.

## IV. COHESIVE ENERGY
Finally we turn to the objective of the preceding arguments: How well does the LSD approximation do in improving the cohesive energy of the alkalis? Of course, it is a little foolish to bury so much physics-or at least what we perceive as physics- in one single number. But fortunately we see other possible applications of the approach, which will be discussed in Sec. V.

For the moment, however, let us see if Tong's result for sodium can be improved by LSD. Of course, there may be more conventional explana- tions for the discrepancy between the experimental number (1.13 eV/atom) and Tong's. One possibili- ty, as Tong $^{2}$ has suggested, might be computation al difficulties. The cohesive energy is obtained by subtracting the total energy per atom of metallic sodium from the total energy of the isolated atom. These two very large numbers have been calculated from different computer programs, and thus the small difference might be inaccurate. However, the independent calculation of the cohesive energy by Averill supports the view that the computationalerror in Tong's calculation is small. $^{16}$

Another possible explanation for the deviation could be a limited ability of the local-density ap- proximation to describe the effects of exchange and correlation. These effects are fundamentally nonlocal. Lacking quantitative criteria for the applicability of the local approximation, we can- not definitely reject this reason for the deviation. The qualitative arguments expressed in Sec. III, however, point at sodium as an ideal system for applying the approximation.

A third reason, suggested by $Kohn^{3}$ and which we favor, is that the discrepancy should be due to an insufficient description of the sodium atom in the LD approximation. In the atom, the outermost 3s electron is unpaired, giving a nonzero net spin density. In the LD approximation used by Tong, the exchange-correlation potential and energy have been obtained from results for the spin-compen- sated electron liquid. This should give a bad rep- resentation of these quantities for the unpaired3s electron. In the following we will provide re- sults in the LSD approximation, which support Kohn's suggestion.

Tong solved his Eqs. (1)-(9) numerically both for the sodium atom and the metal. $^{2}$ We see no reason to repeat the calculation for the metal, Tong's result having been essentially checked by Averill. $^{16}$ To obtain the effect of the improved theory we calculate the difference in total energy of the sodium atom between the "unrestricted"(LSD approximation) and "restricted "(LD ap- proximation) cases. This difference is then added to Tong's value for the cohesive energy.

Equations (1)-(9) of Ref. 2, generalized as de- scribed in Sec. II, have been solved self-consis- tently for the sodium atom by a numerical pro- cedure. We have made one computation, in which we let the relative spin polarization $\zeta$ take the self-consistent value from the local spin density, and another one, in which we lock the parameterζ to the value zero, the value for a completely spin-compensated system, and we calculated the total energies in the two cases.

We obtain the value -0.29 eV/atom for the dif- ference between these two energies. When this number is added to Tong's result (1.39 eV/atom), the cohesive energy becomes 1.10 eV/atom.

Our values for the correlation energy of the pa- ramagnetic electron liquid deviates slightly from the values used by Tong. We estimate the effect of this deviation on the exchange-correlation en-ergy [Eq. (1)] to give a contribution of 0.07 eV/ atom to the cohesive energy. $^{17}$ When this contri bution is included, the cohesive energy becomes1.17 eV/atom, i.e., within 4% of the experimen- tal value.

We thus see that an a priori calculation starting from no other information than the nuclear charge Z=11 gives a result in ridiculously close agree- ment with the experimental value 1.13 eV/atom.

In Sec. III we argued that the Kohn-Sham scheme in the LSD approximation should be applicable for the valence electrons of a range of elements. An-

<table><caption>TABLE II. Total energies of the lithium and sodium atoms, in Ry.</caption>
<tbody><tr><th>Method</th><th>Lithium</th><th>Sodium</th></tr>
<tr><td>Expt., Ref. 15</td><td>−14.956</td><td>−324.521</td></tr>
<tr><td>LSD appr.</td><td>−14.766</td><td>−323.268</td></tr>
<tr><td>Hartree-Fock, Ref. 15</td><td>−14.865</td><td>−323.717</td></tr>
<tr><td>LD appr., Ref. 15</td><td>−14.656</td><td>−322.768</td></tr>
<tr><td>LD appr., Eq. (2)</td><td>−14.741</td><td>−323.247</td></tr>
</tbody></table>

other possible comparison is offered by Liber- man's calculation on Lithium. $^{18}$ Liberman has used the LD approximation, however with only ex- change included. His result for the cohesive en- ergy is 1.8 eV/atom, $^{18}$ already in good agreement with the experimental number of 1.65 eV/atom. $^{19}$ Using Liberman's data we estimate the effects of correlation with and without spin polarization in a perturbative way. Amusingly, we find that in- clusion of correlation in the LD approximation in- creases the cohesive energy to 2.2 eV/atom, while when the LSD approximation is applied, the energy of the atom is lowered 0.4 eV from the val- ue given by the LD approximation, giving back Liberman's value of 1.8 eV/atom. The important point is that correlation effects must be included in calculating the cohesive energy, and if we had not taken into account the outer, unpaired spin in determining the correlation energy, we would necessarily have overestimated the cohesive energy.

As discussed in Sec. III, we do not attach any great significance to detailed results for tightly bound core electrons in the LSD approximation. However, it might be of some interest to compare our results for the total energies of atomic lithium and sodium with experiment and with the results obtained when using more traditional methods. Such a comparison is made in Table II. The dif- ference between our results in the LD approxi- mation and those of Tong and Sham is due to the use of different interpolation formulas for the elec- tron-gas input, their correlation energy likely being above the exact result and ours below. The reason that the spin polarization affects the total energy so little is of course that it is primarily only the lightly bound valence electron which is affected by the spin polarization and the major contribution to the total energy comes from the core electrons.

## V. DISCUSSION AND CONCLUSIONS

We have discussed and applied the Kohn-Sham spin-density-functional formalism in the local- spin-density approximation. We have argued that the spin-density formalism includes additional relevant physics compared to the commonly used density formalism, as it takes proper account of the exchange-correlation effects of systems with unpaired electrons. In Sec. III we have shown that the LSD approximation gives a good repre- sentation of the exchange-correlation energy of the hydrogen atom. The qualitative arguments about the exchange-correlation hole are supported by trends through the hydrogenic-ion series. These arguments also imply that the approximation should give a good representation of the exchange-cor- relation energy of valence electrons of systems with a lower density than the hydrogen atom. Sup- port for these arguments is obtained in Sec. IV, where values for the cohesive energies of sodium and lithium in close agreement with the experi- mental numbers are calculated.

The usefulness of the spin-density-functional formalism in its approximate form is of interest not only for atoms but still more so for molecules, for atoms interacting with solids, and for other situations where the complicated geometry causes a need for simple schemes of calculation. We are presently developing such a scheme for chemisorp- tion problems. First we observe that the scheme works well for separated entities of surface and adsorbate. For example, the work-function values calculated with the Kohn-Sham scheme are close to the experimental numbers. $^{20}$ For the isolated atom, the LSD approximation gives good results for the relevant parameters of the hydrogen ad- sorption, the ionization energy $I=-E(H)$ , the af finity $A=E(H)-E(H^{-})$ , and the Coulomb repulsion energy $U=I-A$ . The ionization energy $I$ of the hydrogen atom has been calculated in Sec. III. Further, we have calculated values for $A$ (1.0 eV) and $U$ (12.4 eV) close to the exact results 0.8 and12.9 eV, 21 respectively. We see no a priori rea- son why the scheme cannot be used to describe the interaction between adsorbate and surface. How- ever, obviously there are difficulties in describ- ing the transition between the paramagnetic limit of the surface and the spin-polarized limit of the adsorbate. In particular, as the adsorbate ap- proaches the surface, there is a tendency to form a local moment, so that it may be necessary to build spin-fluctuation effects into the exchange-correlation-energy functional. $^{22}$

In conclusion, we have shown that the use of the spin-density-functional rather than the density- functional formalism gives an improved descrip- tion of the exchange and correlation effects on atomic valence electrons with unpaired spins. An application on the cohesive energy of sodium brings Tong's result in close agreement with the experimental value.

## ACKNOWLEDGMENT

The authors are very grateful to A. Rosén for making available the computer program used in these calculations.

*Supported by the Swedish Natural Science Research
Council and in part by the National Science Foundation,
Grant No. GH-36457, through the Cornell Materials
Science Center, Grant No. GH-33637, Report No. 2163.
†On leave from the Institute of Theoretical Physics,
Chalmers University of Technology, S-402 20, Göte-
borg, Sweden.
$^{1}$W. Kohn and L. J. Sham, Phys. Rev. $\underline{140}$, A1133
(1965).
$^{2}$B. Y. Tong, Phys. Rev. B $\underline{6}$, 1189 (1972).
$^{3}$W. Kohn, in *Energy Bands in Metals and Alloys*, edited
by L. H. Bennett and J. T. Waber (Gordon and Breach,
New York, 1968), p. 65.
$^{4}$A brief account of these results has been given in Ref.
5, p. 159.
$^{5}$*Collective Properties of Physical Systems*, Proceedings
of the Twenty-Fourth Nobel Symposium, edited by B. I.
Lundqvist and S. Lundqvist (Academic, New York,
1974).
$^{6}$O. Gunnarsson, B. I. Lundqvist, and S. Lundqvist,
Solid State Commun. $\underline{11}$, 149 (1972); O. Gunnarsson and
B. I. Lundqvist (unpublished).
$^{7}$P. Hohenberg and W. Kohn, Phys. Rev. $\underline{136}$, B864
(1964).
$^{8}$J. C. Slater and K. H. Johnson, Phys. Rev. B $\underline{5}$, 844
(1972).
$^{9}$J. C. Stoddart and N. H. March, Ann. Phys. (N. Y.)
$\underline{64}$, 174 (1971); U. von Barth and L. Hedin, J. Phys. C
$\underline{5}$, 1629 (1972); A. K. Rajagopal and J. Callaway, Phys.
Rev. B $\underline{7}$, 1912 (1973).
$^{10}$This constant does not need to be zero. One can add
terms to the variational expression for the energy func-
tional [Tong's Eq. (1)], which for physical densities
gives zero contribution to the energy functional but a
constant contribution $C$ to the potential obtained by tak-
ing the functional derivative of this functional with re-
spect to the (spin) density. Such a density-functional
term is $C\{\int d^{3}r\ n(\overrightarrow {r})-[\int d^{3}r\ n(\overrightarrow {r})+\frac {1}{2}]\}$, where $[\bullet \bullet \bullet]$
means the integer part of the number within brackets.
Physical densities satisfy the condition $\int d^{3}r\ n(\overrightarrow {r})=N$, the
number of electrons of the system.
$^{11}$The interaction energy will give the exchange-correla-
tion energy of Fig. 1 after an integration over the cou-
pling constant. See e.g., D. Pines and P. Nozières,
*The Theory of Quantum Liquids* (Benjamin, New York,
1966); p. 297.
$^{12}$See, e.g., C. Herring, Int. J. Quantum Chem. $\underline{1S}$, 788
(1967).
$^{13}$J. B. Mann, Los Alamos Scientific Laboratory Report
No. LA-3690, 1967 (unpublished).
$^{14}$J. Callaway, Phys. Rev. $\underline{106}$, 868 (1957); V. Samathi-
yakanit, thesis, report No. 69-30 (Institute of Theo-
retical Physics, Göteborg, Sweden, 1969) (unpublished).
$^{15}$B. Y. Tong and L. J. Sham, Phys. Rev. $\underline{144}$, 1 (1966).
$^{16}$F. W. Averill, Phys. Rev. B $\underline{6}$, 3637 (1972). Averill's
calculation is performed in the so-called $X\alpha$ approxi-
mation. Considering only exchange effects in the LD
approximation (corresponding to $\alpha=\frac{2}{3}$ in his scheme)
he obtains 1.18 eV/atom for the cohesive energy of
sodium. To compare this result with Tong's value, one
has to consider the effects of correlation in the same
way as he. By perturbation theory we estimate
Averill's value to increase to 1.36 eV/atom, when these
effects are included, a value close to Tong's number.
$^{17}$Tong obtains the correlation energy $\epsilon^{c}(r_{s})$ from an inter-
polation between the low-density Wigner correlation
formula and the high-density expression of Gell-Mann
and Brueckner. We estimate the deviation by evaluating
Eq. (1) with his $\epsilon^{c}(r_{s})$ and our $\epsilon^{c}(r_{s},\zeta=0)$ from Eq. (2),
using our calculated density result for the atom and
density data from E. Wigner and F. Seitz, Phys. Rev.
$\underline{34}$, 804 (1933), for the metal.
$^{18}$D. A. Liberman, Phys. Rev. B $\underline{3}$, 2081 (1971), and
private communication.
$^{19}$D. R. Stull and H. Prophet, Natl. Stand. Ref. Data Ser.
$\underline{37}$ (1971).
$^{20}$N. D. Lang and W. Kohn, Phys. Rev. B $\underline{3}$, 1215 (1971).
$^{21}$C. L. Pekeris, Phys. Rev. $\underline{126}$, 1470 (1962).
$^{22}$See, e.g., J. R. Schrieffer, in Ref. 5, p. 160.