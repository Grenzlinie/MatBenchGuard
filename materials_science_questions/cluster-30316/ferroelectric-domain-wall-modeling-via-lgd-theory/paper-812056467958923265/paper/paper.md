![](./images/812056467958923265_1.jpg)

# Theory for equilibrium 180° stripe domains in Pb Ti O 3 films

G. B. Stephenson and K. R. Elder

Citation: *Journal of Applied Physics* **100**, 051601 (2006); doi: 10.1063/1.2337360
View online: http://dx.doi.org/10.1063/1.2337360
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/100/5?ver=pdfcov
Published by the AIP Publishing

## Articles you may be interested in
Engineering 180° ferroelectric domains in epitaxial PbTiO3 thin films by varying the thickness of the underlying (La,Sr)MnO3 layer
Appl. Phys. Lett. **105**, 132903 (2014); 10.1063/1.4897144

Thickness scaling of ferroelastic domains in PbTiO3 films on DyScO3
Appl. Phys. Lett. **103**, 142901 (2013); 10.1063/1.4823536

Ferroelectric domains in epitaxial PbTiO3 films on LaAlO3 substrate investigated by piezoresponse force microscopy and far-infrared reflectance
J. Appl. Phys. **110**, 084115 (2011); 10.1063/1.3651510

A modified scaling law for 180° stripe domains in ferroic thin films
J. Appl. Phys. **105**, 061601 (2009); 10.1063/1.3055355

Anelastic deformation of Pb ( Zr , Ti ) O 3 thin films by non-180° ferroelectric domain wall movements during nanoindentation
Appl. Phys. Lett. **81**, 421 (2002); 10.1063/1.1491291

![](./images/812056467958923265_2.jpg)

[This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to ] IP:
193.61.135.80 On: Mon, 15 Dec 2014 11:53:18

JOURNAL OF APPLIED PHYSICS 100, 051601 (2006)

# Theory for equilibrium $180^{\circ}$ stripe domains in $PbTiO_{3}$ films

G. B. Stephenson$^{\text{a)}}$
Materials Science Division, Argonne National Laboratory, Argonne, Illinois 60439

K. R. Elder
Department of Physics, Oakland University, Rochester, Michigan 48309-4487

(Received 25 April 2005; accepted 14 December 2005; published online 7 September 2006)

A thermodynamic theory is developed for equilibrium $180^{\circ}$ stripe domains in ferroelectric thin films on insulating substrates. Such stripe domains form to minimize the energy of the depolarizing field, and lead to a suppression of $T_{C}$ in thin films. Expressions including depolarizing field and domain wall energy are developed and applied to coherently strained $PbTiO_{3}$ films on $SrTiO_{3}$ substrates, with an upper boundary condition of either a dielectric ($SrTiO_{3}$), a conductor, or vacuum. An elastic solution appropriate for epitaxially strained stripe domains and $180^{\circ}$ domain walls is presented. We minimize the full nonlinear free energy using a numerical technique to obtain equilibrium polarization and field distributions, and determine the equilibrium stripe period as a function of temperature and film thickness for each upper boundary condition. While the stripe periods found agree reasonably well with the existing analytical solution using a linearized free energy, the suppression of $T_{C}$ as film thickness decreases is as much as a factor of 10 smaller than that given by the linear solution. © 2006 American Institute of Physics. [DOI: 10.1063/1.2337360]

## I. INTRODUCTION

When a thin film of ferroelectric material polarizes in an out-of-plane direction, e.g., due to cooling through the Curie temperature $T_{C}$, the change in the polarization across the interfaces produces an electric field that tends to oppose the polarization (the "depolarizing field"). $^{1}$ If it is not neutralized, the energy of this field is large enough in typical ferroelectrics to completely suppress polarization. $^{2}$ The depolarizing field can be reduced in two ways: either (a) through compensation by free charge arriving at the interfaces (e.g., when electrodes are present) or (b) by the formation of equal fractions of oppositely polarized ($180^{\circ}$) domains. The effects of depolarizing field on ferroelectricity in thin films have been a topic of continuing interest, and considerable attention has been paid recently to compensation by free charge. $^{3-6}$ Here we focus on the second mechanism, equilibrium $180^{\circ}$ stripe domain formation.

The domain morphology that minimizes the field energy was first worked out for the analogous case of ferromagnetic systems. $^{7,8}$ It consists of lamellas (stripes) in which the polarization direction alternates, as shown in Fig. 1. The equilibrium value of the stripe period $d$ is determined by a trade-off between residual electrostatic energy and the energy of the walls between the domains, and for thick films is proportional to the square root of the film thickness $t$. For ferroelectric films of macroscopic thickness ($t\sim 1$ mm), the equilibrium $180^{\circ}$ stripe domain period is typically much smaller than the thickness ($d\sim 10\ \mu$m). $^{9,10}$ Equilibrium $180^{\circ}$ stripe domains have recently been observed in very thin films, where the stripe period is of the same order as the thickness ($d\sim t\sim 10$ nm). $^{11,12}$ For these ultrathin films, the energy of the residual depolarizing field and the domain walls may contribute significantly to the observed suppression of $T_{C}$. The presence of such nanoscale $180^{\circ}$ stripe domains is also expected to have significant effects on the electrical properties. $^{13,14}$

Several previous theoretical treatments of equilibrium $180^{\circ}$ stripe domains have appeared. The original analytical solution for the field distributions and energies $^{8}$ was given for ferromagnetic domains with uniform magnetization. Subsequently an analytical solution for ferroelectric domains with variable polarization was developed, using an approximate free energy density for a "linearly polarizable" ferroelectric. $^{9}$ This solution was then extended to thin films where the fields from each interface overlap. $^{13-16}$ An approximate analytical solution using a higher-order free energy density has been proposed. $^{17}$ Numerical solutions using such a higher-order free energy, but considering only a single component of the polarization, have been given. $^{18}$ In all of the above, minimization of a free energy functional was used to determine the equilibrium state. Other approaches have also found $180^{\circ}$ stripe domains as the ground state, including shell-model calculations $^{19,20}$ and Monte Carlo simulations using a first-principles-based effective Hamiltonian. $^{21-24}$

Recent experimental results $^{11,12}$ motivate us to develop theoretical predictions for equilibrium $180^{\circ}$ stripe domains in

![](./images/812056467958923265_3.jpg)

FIG. 1. Schematic of stripe domain geometry showing the film thickness $t$ and stripe period $d$. Arrows indicate principal polarization direction of domains. Coordinates $r_{i}$ are aligned with the crystallographic axes.

$^{\text{a)}}$Electronic mail: stephenson@anl.gov

0021-8979/2006/100(5)/051601/17/$23.00
100, 051601-1
© 2006 American Institute of Physics

ferroelectric films that go beyond those previously reported. In particular, we desire accurate predictions for the suppression of $T_C$ as a function of film thickness. Our thermodynamic approach is to write a Landau-Ginzburg-Devonshire free energy density that takes into account polarization, stress, electric field, and domain walls, and to determine the spatial distributions of these quantities, consistent with Maxwell's equations and the constraints of linear elasticity, that minimizes the integrated free energy to determine the equilibrium state. The full nonlinear sixth-order polarization expansion is incorporated in the free energy functional, and a numerical technique is used to find the minimum. A similar approach has been used to model the complex $90^\circ/180^\circ$ domain structures that arise when the epitaxial strain is less compressive than that considered here. $^{25}$ This method avoids most of the approximations made in analytical linearized theory for $180^\circ$ stripe domains $^{9,13-16}$ and in previous nonlinear solutions. $^{17,18}$ Calculations are made for epitaxially strained $PbTiO_3$ films on (001) $SrTiO_3$, a system in which equilibrium stripe domains have recently been observed. $^{11,12}$ The $PbTiO_3$ system is ideal for developing quantitative predictions from thermodynamic theory because independent measurements of almost all of the parameters in the theory are independently available. $^{26-29}$ The $\sim 1\%$ compressive epitaxial strain from lattice matching to a (001) $SrTiO_3$ substrate forces the polarization to be normal to the film interfaces, inducing large depolarization field effects. Although the results from atomistic simulations reported to date $^{19-24}$ are closely related to this work, they are for other materials ($BaTiO_3$ and $PbZr_{0.5}Ti_{0.5}O_3$), and cover only a limited range of temperatures, film thicknesses, and strain states.

The outline of this paper is as follows. First we describe the free energy functional to be minimized. Next we summarize the existing analytical linear ferroelectric solution in the present context. Finally we use a numerical technique to solve the full nonlinear problem, for the case of coherently strained $PbTiO_3$ on $SrTiO_3$, with various top-interface boundary conditions. Examples of the polarization and field distributions are presented, as well as results for the temperature and thickness dependence of the equilibrium stripe period. The thickness dependence of the suppression of $T_C$ and the stripe period at $T_C$ are obtained and compared with the linear approximation. Several detailed derivations are given in the appendix, including the development of an elastic solution for systems with $180^\circ$ stripe domains.

## II. FREE ENERGY FUNCTIONAL

As discussed in Appendix A, the thermodynamic function that is minimized at equilibrium in the electrically isolated, coherently strained ferroelectric films considered here is the Helmholtz free energy. The total free energy is written as the integral over the system volume of a free energy density $A$. Since we consider thin film geometries with infinite in-plane dimensions, the total energy per unit area is used,

$$
\mathcal{A} \equiv \frac{1}{\text{area}} \int_V d\mathbf{r}A. \tag{1}
$$

This functional is minimized to obtain the equilibrium polarization distribution. Here we will consider three different electrical boundary conditions for the region above the ferroelectric film, as shown in Fig. 2. In all three the ferroelectric film ($PbTiO_3$) of thickness $t$ is bounded below by a semi-infinite dielectric substrate ($SrTiO_3$), to which it is coherently strained (lattice matched). Above the ferroelectric is either of the following: for case (I), a symmetrical semi-infinite $SrTiO_3$ dielectric; for case (II), a perfect conductor that fixes the potential at the top boundary; or for case (III), a region of vacuum. As illustrated in Fig. 1, the equilibrium $180^\circ$ stripe domains have their primary polarization directions normal to the film plane (the $r_3$ direction), are periodic in one of the in-plane directions ($r_1$), and are uniform in the other ($r_2$). The free energy functional can thus be written as

$$
\mathcal{A} = \mathcal{A}^{\text{in}} + \mathcal{A}_-^{\text{ex}} + \mathcal{A}_+^{\text{ex}},
$$

$$
\begin{aligned}
\mathcal{A}^{\text{in}} &= \int_0^t dr_3 \frac{1}{d} \int_0^d dr_1 A^{\text{in}}, \\
\mathcal{A}_-^{\text{ex}} &= \int_{-\infty}^0 dr_3 \frac{1}{d} \int_0^d dr_1 A_+^{\text{ex}}, \\
\mathcal{A}_+^{\text{ex}} &= \int_t^{+\infty} dr_3 \frac{1}{d} \int_0^d dr_1 A_+^{\text{ex}},
\end{aligned} \tag{2}
$$

where different free energy densities $A^{\text{in}}$, $A_-^{\text{ex}}$, and $A_+^{\text{ex}}$ are used for the ferroelectric ($0<r_3<t$), the substrate ($r_3<0$), and the upper region ($r_3>t$), respectively. We assume that the stripe geometry is aligned with the crystallographic axes, with polarization along [001]. Thus the domain walls are (100) oriented, which has been found to be the preferred crystallographic orientation in experiments. $^{11,12}$

We consider an expression for the free energy density of the ferroelectric given by

$$
\begin{aligned}
A^{\text{in}} &= A_0^\oplus + \sum_i \left( \alpha_i^\oplus P_i^2 + \alpha_{ii}^\oplus P_i^4 + \alpha_{iii}^\oplus P_i^6 \right) + \sum_{i,j>i} \alpha_{ij}^\oplus P_i^2 P_j^2 \\
& \quad + \sum_{i,j \neq i} \alpha_{iij} P_i^2 P_j^4 + \alpha_{123} P_1^2 P_2^2 P_3^2 \\
& \quad + \frac{\epsilon_0}{2} \sum_i E_i^2 + \frac{\kappa_\perp}{2} |\nabla \times \mathbf{P}|^2,
\end{aligned} \tag{3}
$$

where $P_i$ and $E_i$ are the components of the polarization and

![](./images/812056467958923265_4.jpg)

FIG. 2. Schematic of the three different upper boundary conditions considered. Case I: symmetric epitaxial $SrTiO_3$ regions above and below the $PbTiO_3$ film. Case II: the upper region is a perfect conductor that compensates the top interface. Case III: the upper region is vacuum.

electric field vectors. The origin of this expression and values of the $\alpha$ coefficients appropriate for stripe domains in coherently strained $PbTiO_{3}$ films on $SrTiO_{3}$ substrates are given in Appendixes A and B. The primary temperature dependence comes from $\alpha_{3}^{\oplus}$, which becomes negative as $T$ is lowered, favoring polarization in the out-of-plane $(r_{3})$ direction. Elastic strain energy has been included by renormalizing the coefficients denoted by a superscript $\oplus$. Note that in Appendix B we have developed a renormalization appropriate for epitaxially strained $180^{\circ}$ domain walls and stripe domains that differs from that previously developed for single domain systems. $^{30}$

The electric field term is critical for understanding equilibrium $180^{\circ}$ stripe domains, since it drives their formation when the bound charges at the interfaces of the ferroelectric are not compensated by free charge. The electric field distribution is related to the polarization distribution by Maxwell's equations. We calculate field distributions in the $PbTiO_{3}$, $SrTiO_{3}$, and vacuum assuming that these regions have no free charge. This gives the requirements $^{31} \nabla \cdot D=0$ and $\nabla$ $\times E=0$, with the normal component of $D$ and the tangential components of $E$ continuous at interfaces. The first requirement and the definition $D \equiv P+\epsilon_{0} E$ allow the divergence of $E$ to be related to that of $P$ by $\epsilon_{0} \nabla \cdot E=-\nabla \cdot P$. To ensure that the second requirement is also satisfied, one can calculate the field from the potential $\phi$ using $E \equiv-\nabla \phi$, with $\phi$ determined from the polarization distribution through
$$
\epsilon_{0} \nabla^{2} \phi=\nabla \cdot \mathbf{P}, \quad(4)
$$
and $\phi$ continuous at interfaces.

The last term in the free energy density (3) is a gradient energy term which accounts for the domain wall energy. The choice of the cross product form for the gradient energy is discussed in Appendix C. The relationship between the gradient energy coefficient $\kappa_{\perp}$ and the excess free energy of a $180^{\circ}$ domain wall $\gamma$ is derived in Appendix D for an epitaxially strained system. It can be expressed as
$$
\gamma \propto \kappa_{\perp}^{1 / 2} P_{0}^{* 3} f(T), \quad(5)
$$
where $P_{0}^{*}$ is the spontaneous polarization at $E=0$ of the epitaxially strained monodomain system from Eq. (A12) and $f(T)$ represents several weakly temperature dependent coefficients. Since the transition in epitaxially strained $PbTiO_{3}$ is second order, $^{30} P_{0}^{*}$ and $\gamma$ go to zero at the monodomain transition temperature $T_{C}^{*}$, while $\kappa_{\perp}$ is typically taken to be temperature independent. The gradient energy coefficient $\kappa_{\perp}$ is the only coefficient in the free energy density (3) that does not have a known value from independent measurements in the literature. The value used in the example calculations give here is $\kappa_{\perp}=7.8 \times 10^{-11} \mathrm{~V} \mathrm{~m}^{3} / \mathrm{C}$, chosen so that the predicted stripe domain periods agree with those observed. $^{11,12}$

For simplicity, we assume that the dielectric nonlinearity of $SrTiO_{3}$ is negligible for the temperatures and fields of interest, and treat the regions outside the ferroelectric as isotropic linear dielectrics. The consistency of this assumption will be discussed below. The free energy densities can be expressed as

![](./images/812056467958923265_5.jpg)

FIG. 3. Plot of $A(P_{3})-A_{0}$ at $P_{1}=E=0$ for monodomain epitaxially strained $PbTiO_{3}$ on $SrTiO_{3}$ at $T=T_{C}^{*}-100 ~K$ showing both the full sixth-order expansion and the quadratic "linear ferroelectric" approximation.

$$
A^{\mathrm{ex}}=\alpha_{\mathrm{ex}} \sum_{i} P_{i}^{2}+\frac{\epsilon_{0}}{2} \sum_{i} E_{i}^{2}, \quad(6)
$$
where we neglect the constant term. For these regions, a solution with $\nabla \cdot P=0$ and the field proportional to the polarization $E_{i}=2 \alpha_{\mathrm{ex}} P_{i}$ satisfies Maxwell's equations and minimizes the free energy density at every point. The free energy densities for these regions can thus be written as
$$
A^{\mathrm{ex}}=\frac{\epsilon_{0} \epsilon_{\mathrm{ex}}}{2} \sum_{i} E_{i}^{2}, \quad(7)
$$
where $\epsilon_{\mathrm{ex}} \equiv\left(1+2 \alpha_{\mathrm{ex}} \epsilon_{0}\right) / 2 \alpha_{\mathrm{ex}} \epsilon_{0}$ is the relative dielectric constant of the external medium. For case (III), the vacuum has no polarization, which implies $\epsilon_{\mathrm{ex}+}=1$. For case (II), the region of perfect conductor has no electric field or polarization and does not contribute to the free energy.

In the next two sections, we present a linearized analytical solution and an exact numerical solution for equilibrium $180^{\circ}$ stripe domains. Since we expect the $180^{\circ}$ domain walls to be of Ising rather than Bloch type, as shown in Appendix D, for both solutions we neglect any polarization or field components along the stripe direction, giving $P_{2}=E_{2}=0$.

### III. STRIPE DOMAINS IN A "LINEAR FERROELECTRIC"

Several previous treatments of stripe domains $^{9,13-16}$ have been based on a "linear ferroelectric" model. In this approximation, the polarization dependence of the free energy for the ferroelectric phase is simplified by expanding about one of the spontaneously polarized states $P_{3}= \pm P_{0}^{*}$ rather than about the nonpolar state $P_{3}=0$, and keeping only the quadratic terms. This leads to linear relations between the fields, which allows an exact analytical solution.

Instead of the sixth-order free energy expansion [Eq.(3)], a quadratic expansion about a reference state $P$ $=(0,0, P_{30})$ is used,
$$
A^{\mathrm{in}}=A_{0}^{\oplus^{\prime}}+\alpha_{1}^{\oplus^{\prime}} P_{1}^{2}+\alpha_{3}^{\oplus^{\prime}}\left(P_{3}-P_{30}\right)^{2}+\frac{\epsilon_{0}}{2}\left(E_{1}^{2}+E_{3}^{2}\right), \quad(8)
$$
where the domain wall energy term has been left out for now. Figure 3 illustrates this approximation. The two dashed

![](./images/812056467958923265_6.jpg)

FIG. 4. (a) Dielectric constants calculated for epitaxially strained PbTiO₃
and measured for the SrTiO₃ substrate as a function of temperature. (b)
Dielectric anisotropy $\beta\equiv(\epsilon_{1}^{\oplus}/\epsilon_{3}^{\oplus})^{1/2}$.

curves correspond to $P_{30}=\pm P_{0}^{*}$ being positive or negative.
Since the reference state is the polarized state, its free energy
$A_{0}^{\oplus\prime}$ and curvatures $\alpha_{1}^{\oplus\prime}$ and $\alpha_{3}^{\oplus\prime}$ differ below $T_{C}^{*}$ from those
of the nonpolar reference state used in Eq. (3), $A_{0}^{\oplus}$, $\alpha_{1}^{\oplus}$, and
$\alpha_{3}^{\oplus}$. They are given by

$$
\begin{aligned}
& A_{0}^{\oplus\prime}=A_{0}^{\oplus}+\alpha_{3}^{\oplus}P_{0}^{*2}+\alpha_{33}^{\oplus}P_{0}^{*4}+\alpha_{111}P_{0}^{*6}, \\
& \alpha_{1}^{\oplus\prime}=\alpha_{1}^{\oplus}+\alpha_{13}^{\oplus}P_{0}^{*2}+\alpha_{112}P_{0}^{*4}, \\
& \alpha_{3}^{\oplus\prime}=\alpha_{3}^{\oplus}+6\alpha_{13}^{\oplus}P_{0}^{*2}+15\alpha_{111}P_{0}^{*4}.
\end{aligned}
\tag{9}
$$

As shown in Fig. 3, the value of $A$ and its second derivatives
have been equated at $\mathbf{P}=(0,0,P_{30})$ to make the quadratic
expansion (8) correspond with the sixth-order expansion
(A7). The coefficients $A_{0}^{\oplus}$, $\alpha_{1}^{\oplus}$, and $\alpha_{3}^{\oplus}$ depend on the average
strain through the parameter $P^{\dagger}$, as described in Appendix B.
For the linear ferroelectric model, in which the dielectric
constants are independent of polarization, the consistent as-
sumption is to use the strain of the polar reference state $\mathbf{P}$
$=(0,0,P_{30})$ (which gives $P^{\dagger}=P_{0}^{*}$) in calculating the values of
$A_{0}^{\oplus\prime}$, $\alpha_{1}^{\oplus\prime}$, and $\alpha_{3}^{\oplus\prime}$ using Eqs. (9).

Minimizing $A$ by varying $P_{1}$ and $P_{3}$ at fixed $\mathbf{D}$ leads to
linear equations of state, given by

$$
E_{1}=2\alpha_{1}^{\oplus\prime}P_{1}, \quad E_{3}=2\alpha_{3}^{\oplus\prime}(P_{3}-P_{30}). \tag{10}
$$

In analogy with the dielectric constants for the paraelectric
phase above $T_{C}^{*}$, $\epsilon_{i}^{\oplus}\equiv(1+2\alpha_{i}^{\oplus}\epsilon_{0})/2\alpha_{i}^{\oplus}\epsilon_{0}$, one can define
relative dielectric constants in the ferroelectric phase using
$\epsilon_{i}^{\oplus}\equiv(1+2\alpha_{i}^{\oplus\prime}\epsilon_{0})/2\alpha_{i}^{\oplus\prime}\epsilon_{0}$. For the linear ferroelectric model,
the equilibrium free energy can be obtained by substituting
Eq. (10) into Eq. (8) to give

$$
A^{\text{in}}=A_{0}^{\oplus\prime}+\frac{\epsilon_{0}}{2}(\epsilon_{1}^{\oplus}E_{1}^{2}+\epsilon_{3}^{\oplus}E_{3}^{2}). \tag{11}
$$

Figure 4(a) shows $\epsilon_{1}^{\oplus}$ and $\epsilon_{3}^{\oplus}$ calculated as a function of
temperature for PbTiO₃ films on SrTiO₃ substrates. Also
shown is the experimental dielectric constant for SrTiO₃,
which can be described as $\epsilon_{\text{ex}}=8.3\times10^{4}/(T-38\ \text{K}).^{32}$ The
value of $\epsilon_{3}^{\oplus}$ diverges at $T_{C}^{*}$, but becomes smaller than the
other dielectric constants at lower $T$.

Because the reference state changes abruptly when mov-
ing from one domain into the next in this model, the domain
wall energy is introduced as an explicit term in the free en-
ergy functional, rather than as a gradient energy density. The
full functional becomes

$$
\mathcal{A}=\mathcal{A}^{\text{in}}+\mathcal{A}_{-}^{\text{ex}}+\mathcal{A}_{+}^{\text{ex}}+\frac{2\gamma t}{d}, \tag{12}
$$

where $\gamma$ is the energy per unit area of the domain wall. Its
value can be related to the gradient energy coefficient $\kappa_{\perp}$ as
described in Appendix D.

We consider case (I), in which the PbTiO₃ film is
bounded on both sides by SrTiO₃ regions. Inside the ferro-
electric film, the free energy density $A^{\text{in}}$ of Eq. (11) is used.
The reference state polarization $P_{30}$ has alternating sign in
adjacent domains, and can be written as a square plane wave
with amplitude $\pm P_{0}^{*}$ using the Fourier series

$$
P_{30}=P_{0}^{*}\frac{4}{\pi}\sum_{n\text{ odd}}\frac{\sin(nk_{0}r_{1})}{n}, \tag{13}
$$

where the fundamental wave number $k_{0}$ is defined by $k_{0}$
$\equiv2\pi/d$ and the sum runs over the positive odd integers $n$
$=1,3,5,\ldots$. For the regions above and below the ferroelec-
tric, the free energy density $A^{\text{ex}}$ of an isotropic linear dielec-
tric is used [Eq. (7)], with $P_{2}=E_{2}=0$.

The components of the electric displacement inside the
ferroelectric are $D_{3}=\epsilon_{3}^{\oplus}\epsilon_{0}E_{3}+P_{30}$, $D_{1}=\epsilon_{1}^{\oplus}\epsilon_{0}E_{1}$. The require-
ment $\boldsymbol{\nabla}\cdot\mathbf{D}=0$ then gives the condition on the internal elec-
tric potential,

$$
0=\beta^{2}\nabla_{1}^{2}\phi^{\text{in}}+\nabla_{3}^{2}\phi^{\text{in}}, \tag{14}
$$

where $\beta\equiv(\epsilon_{1}^{\oplus}/\epsilon_{3}^{\oplus})^{1/2}$ is the dielectric anisotropy. Values of $\beta$
are plotted as a function of temperature in Fig. 4(b). Outside
the ferroelectric we have $D_{i}=\epsilon_{\text{ex}}\epsilon_{0}E_{i}$, so that Laplace's equa-
tion holds,

$$
0=\nabla^{2}\phi^{\text{ex}}. \tag{15}
$$

The potential distributions inside, below, and above the
ferroelectric are given, respectively, by$^{15}$

$$
\phi^{\text{in}}=\frac{P_{0}^{*}}{\epsilon_{0}k_{0}}\frac{4}{\pi}\sum_{n\text{ odd}}\frac{W_{n}}{n^{2}}\sin(nk_{0}r_{1})\frac{\sinh[nk_{0}\beta(t/2-r_{3})]}{\sinh(nk_{0}\beta t/2)},
\tag{16}
$$

$$
\phi_{-}^{\text{ex}}=\frac{P_{0}^{*}}{\epsilon_{0}k_{0}}\frac{4}{\pi}\sum_{n\text{ odd}}\frac{W_{n}}{n^{2}}\sin(nk_{0}r_{1})\exp(nk_{0}r_{3}), \tag{17}
$$

$$
\phi_{+}^{\text{ex}}=\frac{-P_{0}^{*}}{\epsilon_{0}k_{0}}\frac{4}{\pi}\sum_{n\text{ odd}}\frac{W_{n}}{n^{2}}\sin(nk_{0}r_{1})\exp[-nk_{0}(r_{3}-t)], \quad (18)
$$

where the dimensionless coefficient in the sums is

$$
W_{n}\equiv[\epsilon_{\text{ex}}+\beta\epsilon_{3}^{\oplus}\coth(nk_{0}\beta t/2)]^{-1}. \tag{19}
$$

The polarization distributions are given by

$$
\begin{aligned}
& P_{1}^{\mathrm{in}}=-\left(\epsilon_{1}^{\oplus}-1\right) \epsilon_{0} \nabla_{1} \phi^{\mathrm{in}}, \\
& P_{3}^{\mathrm{in}}=P_{30}-\left(\epsilon_{3}^{\oplus}-1\right) \epsilon_{0} \nabla_{3} \phi^{\mathrm{in}}, \\
& P_{1}^{\mathrm{ex}}=-\left(\epsilon_{\mathrm{ex}}-1\right) \epsilon_{0} \nabla_{1} \phi^{\mathrm{ex}}, \\
& P_{3}^{\mathrm{ex}}=-\left(\epsilon_{\mathrm{ex}}-1\right) \epsilon_{0} \nabla_{3} \phi^{\mathrm{ex}}.
\end{aligned}
\tag{20}
$$

The magnitude of $\nabla_{3} \phi^{\text {in }}$ is maximum at the upper and lower interfaces, while $|\nabla_{1} \phi^{\text {in }}|$ is maximum at the domain boundaries and has weak (logarithmic) singularities at the intersections of the domain boundaries and the interfaces. The potential is constant (zero) in the central plane of the film, at $r_3$=$t$/2. This satisfies the boundary condition for a perfectly conducting electrode. Thus, the potential distributions (16) and (17) can be used for case (II), stripe domains in a film with a perfectly conducting upper electrode, by replacing $t$ with $2t$.

The potential gradients are significant only in regions within approximately one stripe period of the ferroelectric/dielectric interfaces. When the film thickness becomes as small as $d$, the fields from the two surfaces overlap and the solution given here differs from the original Mitsui and Furuichi result. $^{9}$ Note that the anisotropy coefficient $\beta$ modifies the thickness of these regions; as $\beta$ becomes smaller (e.g., near $T_{C}^{*}$), the region of field becomes thicker. When the thickness of the film is much larger than that of the surface layers ($\beta k_0 t \gg 1$), the polarization in the central zero-field region of the film is $P_3$=$P_{30}$, $P_1$=0, which is the reference state for the linear ferroelectric model. For this model to be an accurate approximation of the full nonlinear model, the polarization should not deviate too much from this reference state. A self-consistency check can be made by calculating the value of $P_3$ at the interface, $r_3$=0. For $\beta k_0 t \gg 1$ and $\beta \epsilon_{3}^{\oplus} \gg \epsilon_{\mathrm{ex}}$, one obtains $P_3(r_3$=0)=$P_{30}/\epsilon_{3}^{\oplus}$, so that $P_3$ is reduced almost to zero at the interface. Thus the linear ferroelectric solution is not expected to give accurate field distributions. It underestimates the thickness of the region of field near the interface, and overestimates the free energy. The use of a uniform value for $\gamma$ is a consistent, if not necessarily realistic, approximation in the linear ferroelectric model because the discontinuity in $P_3$ at the domain walls is $2P_{0}^{*}$, independent of $r_3$, in this solution.

The internal and external fields can be integrated to give a total free energy of $^{13,15,16}$
$$
\mathcal{A}=t A_{0}^{\oplus^{\prime}}+\frac{\gamma k_{0} t}{\pi}+\frac{8 P_{0}^{* 2}}{\pi^{2} \epsilon_{0} k_{0}} \sum_{n \text { odd }} \frac{W_{n}}{n^{3}}. \tag{21}
$$

The equilibrium value of $k_0$ can be obtained by setting $\partial \mathcal{A}/\partial k_0$ to zero, noting that $W_n$ depends on $k_0$. The equilibrium $k_0$ satisfies the relation
$$
k_{0}^{2}=\frac{8 P_{0}^{* 2}}{\pi \epsilon_{0} \gamma} \sum_{n \text { odd }} \frac{W_{n}}{n^{3}}\left[1-\frac{n W_{n} k_{0} \epsilon_{1}^{\oplus} t}{2 \sinh ^{2}\left(n k_{0} \beta t / 2\right)}\right]. \tag{22}
$$

Kopal et al., $^{16}$ obtained an equivalent expression for the case in which $\epsilon_{\mathrm{ex}}$=1 (apart from a missing factor of $n$ in the last term). In the limit $\beta k_0 t \gg 1$, one obtains

![](./images/812056467958923265_7.jpg)

FIG. 5. Equilibrium stripe period as a function of temperature for various film thicknesses calculated from the linear ferroelectric model for case (I).

$$
k_{0}^{2}=\frac{8 P_{0}^{* 2}}{\pi \epsilon_{0}\left(\epsilon_{\mathrm{ex}}+\beta \epsilon_{3}^{\oplus}\right) \gamma} \sum_{n \text { odd }} n^{-3}, \tag{23}
$$

where the sum has a value of about 1.05. For $\epsilon_{\mathrm{ex}}$=1 this is the Mitsui and Furuichi result, $^{9}$ which predicts that $d$ is proportional to $t^{1/2}$. The temperature dependence of $d$ can be estimated from those of $P_{0}^{*}$, $\beta$, $\epsilon_{3}^{\oplus}$, and $\gamma$. These vary as $(T_{C}^{*}-T)^n$ with exponents $n$ of 1/2, 1/2, $-1$, and 3/2, respectively, which indicates that $d$ should be approximately independent of temperature. The temperature dependence of the equilibrium stripe period $d \equiv 2\pi/k_0$ is shown in Fig. 5 for various film thicknesses, using $\gamma(T)$ from Appendix D.

The equilibrium free energy of the stripe domain phase can be obtained by using $k_0$ from Eq. (22) in Eq. (21). This can be compared with the free energy of the paraelectric phase, $tA_{0}^{*}$, to predict the suppression of $T_C$ below $T_{C}^{*}$ in thin films with stripe domains. Since the paraelectric and striped ferroelectric free energies have different dependences on thickness, the suppression of $T_C$ depends on film thickness. As discussed below, the linear ferroelectric theory significantly overestimates the suppression of $T_C$.

## IV. STRIPE DOMAINS IN A NONLINEAR FERROELECTRIC

To move beyond the linear ferroelectric approximation illustrated in Fig. 3, a different approach must be used. Expressions (16)–(20) for the potential and polarization distributions were derived from the requirement $\nabla \cdot \mathbf{D}$=0 by first using the linear equations of state (10) between $\mathbf{E}$ and $\mathbf{P}$. These were obtained by minimizing the free energy density $A$ for a linear ferroelectric with respect to the $P_i$. The more general expression for the free energy density given by Eq. (3) leads to nonlinear equations of state between $\mathbf{E}$ and $\mathbf{P}$ if it is minimized directly. However, it turns out that there are no solutions that simultaneously satisfy the requirement $\nabla \cdot \mathbf{D}$=0 and these nonlinear equations of state at every point. We must therefore find the polarization and potential distributions that minimize the integrated free energy $\mathcal{A}$ while satisfying Maxwell's equations.

We are interested in solutions for the potential and polarization with the boundary conditions $\phi \to 0$ and $\mathbf{P} \to 0$ at $r_3 \to \pm \infty$, or, in case (II), $\phi$=0 and $\mathbf{P}$=0 in the conductor. The polarization $\mathbf{P}$ is continuous across the bottom and top

interfaces, or, in case (II), the normal gradients $\nabla_3 P_i$ are zero at the interface with the conductor. By symmetry these boundary conditions imply that a film of thickness $t$ with a perfectly conductive cap [case (II)] is identical to the lower half of a film of thickness $2t$ with a $SrTiO_3$ cap [case (I)].

For the periodic stripe geometry, the polarization and electric potential in each region can be written as the Fourier series

$$
P_1 = \sum_{n=-\infty}^{\infty} a_n(r_3)\exp(ink_0r_1),
$$

$$
P_3 = i \sum_{n=-\infty}^{\infty} b_n(r_3)\exp(ink_0r_1), \tag{24}
$$

$$
\phi = i \sum_{n=-\infty}^{\infty} v_n(r_3)\exp(ink_0r_1),
$$

with $a_n=a_{-n}$, $b_n=-b_{-n}$, and $v_n=-v_{-n}$. In this notation all Fourier coefficients are real and $P_1$ is 90 deg out of phase with $P_3$ and $\phi$. When there is no free charge, and the polarization dependence is independent of sign, the minimum energy occurs with equal volume fractions of oppositely polarized domains. In this case $\mathcal{A}$ is a functional of only even powers of $P_i$ which implies that Fourier coefficients with even $n$ are zero. Consequently in what follows only odd values of $n$ are considered.

The coefficients and stripe wavelength are determined by minimizing the integrated free energy $\mathcal{A}$. Technically this is achieved by solving the variational expressions

$$
\frac{\delta \mathcal{A}}{\delta P_1} = \frac{\delta \mathcal{A}}{\delta P_3} = 0 \tag{25}
$$

for the Fourier components $(a_n,b_n,v_n)$ at fixed $k_0$, with $\mathcal{A}$ and $\phi$ determined by Eqs. (2)-(4) and (7) using coefficients given in Eqs. (B7), (B8), (B10), and (A8). In particular, the value of $P^{\dagger}$ is allowed to vary with polarization according to Eq. (B10). In the regions above and below the ferroelectric film, the minimum free energy solution can be obtained analytically as described in Eq. (7). The Fourier components in the substrate $(r_3<0)$ are given by $v_n=v_n^o\exp(-|nk_0r_3|)$, $a_n$ $=nk_0v_n/a_{\text{ex}}$, and $b_n=-a_n$, where $v_n^o$ is the Fourier component of the electric potential at the film/substrate interface [i.e., $v_n^o\equiv v_n(r_3=0)$]. Substituting these solutions into Eqs. (24), (7), and (2) gives

$$
\mathcal{A}_{-}^{\text{ex}} = k_0\epsilon_0\epsilon_{\text{ex}} \sum_{n=1}^{\infty} n(v_n^o)^2. \tag{26}
$$

For case (I), the same expression can be used for the energy of the upper region $\mathcal{A}_{+}^{\text{ex}}$, with $v_n^o$ replaced by the values at the top of the film, $v_n^t\equiv v_n(r_3=t)$. For case (III), this expression for $\mathcal{A}_{+}^{\text{ex}}$ can be used with $\epsilon_{\text{ex}}=1$. For case (II), there is no contribution to the energy from the upper region. Thus the minimum free energy solutions for the regions above and below the film can be determined from the Fourier components of the electric potential at the upper and lower interfaces. Unfortunately, the lowest energy solutions for the ferroelectric film region cannot be obtained analytically because of the higher-order terms in the energy density. To obtain these solutions numerically, a relaxation method was first used to determine the polarization distribution giving the minimum free energy $\mathcal{A}$ at various fixed stripe periods. The equilibrium stripe period was then obtained by interpolating to find the value that minimizes $\mathcal{A}$. Equilibrium solutions were first determined using only one Fourier component $(|n|=1)$, then using three components $(|n|=1,3)$, then five $(|n|=1,3,5)$, etc., until convergence was achieved.

![](./images/812056467958923265_8.jpg)

FIG. 6. Equilibrium polarization distribution for a sample of thickness $t$ =24.2 nm and stripe period $d$=13.2 nm at $T$=700 K for case (I) boundary conditions.

The polarization and electric field distributions for a typical minimum free energy state are depicted for case (I) in Figs. 6 and 7. Only half of the film is shown since it is symmetric about $r_3=t/2$. The field distributions also describe case (II) for a film of half the thickness (i.e., if $t/2$ is replaced by $t$ in both figures). The field distributions for case

![](./images/812056467958923265_9.jpg)

FIG. 7. Equilibrium electric field distribution for a sample of thickness $t$ =24.2 nm and stripe period of $d$=13.2 nm at $T$=700 K for case (I) boundary conditions.

![](./images/812056467958923265_10.jpg)

FIG. 8. Normalized polarization components (a) $P_{1}(r_{3}=0)$ and (b) $P_{3}(r_{3}$ $=t / 2)$ as a function of $r_{1} / d$ for sample of thickness $t=24.2$ nm in case (I). The five curves, from minimum amplitude to maximum amplitude, correspond to temperatures of 957, 951, 900, 800, and 700 K, respectively.

(III) with vacuum above the ferroelectric are very similar to those for case (I), except that the magnitude of the polarization is larger near the $SrTiO_{3}$ interface than the vacuum interface. It is notable that significant polarization of the $SrTiO_{3}$ occurs in the vicinity of the interfaces.

For the parameters used in Figs. 6 and 7, roughly 11 Fourier modes (i.e., $|n|=1,3,5,7,9$, and 11) are needed to achieve convergence in all quantities calculated. In general the number of harmonics needed increases as the ratio of the stripe wavelength to the domain wall width increases at lower temperatures. To illustrate this point the polarizations $P_{1}$ at $r_{3}=0$ and $P_{3}$ at $r_{3}=t / 2$ are plotted as a function of $r_{1}$ at various temperatures in Fig. 8. One can see that the profiles contain more harmonics at lower temperatures, and conversely that a one-mode solution is adequate at temperatures near $T_{C}$. In Figs. 9(a)-9(c), the free energy of the stripe solution relative to the nonpolar phase, the maximum of the electric field, and the equilibrium stripe period are shown as a function of temperature for a film of thickness $t=24.2$ nm in case (I), calculated using different numbers of Fourier modes. While 9 modes are sufficient to reach convergence for the energy and electric field, 11 modes are needed for the stripe period.

The maximum electric field predicted by the model can be used to check the consistency of the assumption that the $SrTiO_{3}$ regions can be treated as a linear dielectric. The dielectric nonlinearity of $SrTiO_{3}$ at high temperature can be estimated using Landau theory, $^{33}$ using an equation for $E(P)$ analogous to Eq. (A11). At 700 K, the nonlinear terms in $E(P)$ become comparable to the linear term at an electric field of $\sim 700$ MV/m. This is significantly larger than the maximum field shown in Fig. 9(b) for a film of thickness $t$ =24.2 nm, consistent with the neglect of nonlinearity in the $SrTiO_{3}$. This simplification should always be adequate near $T_{C}$, where the electric fields are small. Since for a given polarization the maximum field increases at smaller stripe periods and the nonlinearity of $SrTiO_{3}$ becomes significant at smaller fields at lower temperatures (e.g., $\sim 170$ MV/m at 300 K), it should be taken into account for very thin films well below $T_{C}$. This could be done by treating the medium using the same type of numerical solution employed here for the ferroelectric film.

![](./images/812056467958923265_11.jpg)

FIG. 9. (a) Total free energy per unit area of the stripe solution relative to the nonpolar phase, $\Delta A \equiv A-t A_{0}^{*}$, (b) magnitude of the maximum electric field, and (c) stripe period as a function of $T$ for a thickness $t=24.2$ nm in case (I). Nonlinear solutions using 1, 3, 5, 7, 9, and 11 Fourier modes are shown, from top to bottom in (a) and from bottom to top in (b) and (c). In (a) and (b) the 7, 9, and 11 mode results are difficult to distinguish. The dotted line in (a) and (c) is the linear approximation. (d) Average polarization $P^{\dagger}$ as a function of $T$ for $t=15.2,24.2$, and 60.0 nm (bottom to top).

The free energy for the linear approximation [Eq. (21)] is also shown in Fig. 9(a). One can see that the linear theory predicts a first-order transition at a temperature significantly lower than that predicted by the full nonlinear theory. In contrast the nonlinear solution gives a second-order transition. The linear approximation gives fairly accurate values for the stripe period, as shown in Fig. 9(c), unlike its inaccurate $T_{C}$ prediction. The equilibrium stripe period is calculated to be only weakly dependent on temperature.

In Fig. 9(d) the $T$ dependence of the average polarization $P^{\dagger}$ of Eq. (B10) is shown for three films of thicknesses $t$ $=15.2$ nm, $t=24.2$ nm, and $t=60.0$ nm. $P^{\dagger}$ approaches $P_{0}^{*}$ at low $T$ when the stripe period (and film thickness) is much larger than the domain wall width while it approaches zero at $T_{C}$.

The calculations can be used to predict the temperature $T_{C}(t)$ at which a film of thickness $t$ will undergo a transition from a nonpolar to a striped polar state for each of cases (I), (II), and (III). The suppression of $T_{C}$ below the $t \to \infty$ limit $T_{C}^{*}=1025$ K is plotted as a function of film thickness in Fig. 10. Also shown is the prediction from the linear approximation for case (I). In general, the suppression scales approximately as $T_{C}^{*}-T_{C}(t) \sim t^{-1}$ for thick films, where the constant of proportionality varies. Fits of power law exponents give $-0.92,-0.92$, and $-0.98$ for cases (I), (II), and (III), respectively. The deviations from the simple value of $-1$ reflect the

![](./images/812056467958923265_12.jpg)

FIG. 10. Suppression of the transition temperature as a function of film thickness. Nonlinear solutions for case (II), (I), and (III) upper boundary conditions and the linear solution for case (I) are shown.

contributions from the relatively weak temperature dependences of parameters such as $x_{m}$, $\epsilon_{\mathrm{ex}}$, and $\epsilon_{1}^{\oplus}$.

While the equilibrium stripe period is only weakly dependent on temperature (see Fig. 9), it is a stronger function of film thickness. To illustrate this point the equilibrium stripe period at $T_{C}$ is plotted as a function of film thickness in Fig. 11 for all three cases. For thick films one obtains the classical parabolic dependence on film thickness $d(T_{C},t)$ $\sim t^{-1/2},^{7}$ which arises from the trade-off between depolarization field and domain wall energies. Some deviation from this dependence is predicted for ultrathin films where the fields from the two interfaces overlap. This figure also includes the linear prediction for the thickness dependence of the stripe period in case (I). Since the stripe period for a given thickness is smallest at $T_{C}$ in the nonlinear theory, the minimum period as a function of $T$ predicted by the linear approximation is used for comparison in Fig. 11. The linear prediction is reasonably close to the full nonlinear one, indicating that the analytical formula (22) can be a useful guide to expected stripe periods.

![](./images/812056467958923265_13.jpg)

FIG. 11. Equilibrium stripe period as a function of film thickness. Nonlinear solutions for case (I), (II), and (III) upper boundary conditions, at $T=T_{C}$, and the linear solution for case (I), at temperature of minimum $d$, are shown.

## V. DISCUSSION AND CONCLUSIONS

In this paper we have calculated the equilibrium stripe period and $T_{C}$ as a function of film thickness for epitaxial $PbTiO_{3}$ on $SrTiO_{3}$ with various electrical boundary conditions, by minimizing a free energy functional containing the full sixth-order polarization dependence. All of the parameters in the theory have been previously determined from experimental data, $^{26-29}$ apart from the gradient energy coefficient $\kappa_{\perp}$. Since the domain wall energy varies as the square root of $\kappa_{\perp}$, the equilibrium stripe period varies approximately as the $1/4$ power of $\kappa_{\perp}$. Here we have chosen a value $\kappa_{\perp}=7.8\times 10^{-11}\ \mathrm{V\ m^{3}/C}$ so that the stripe domain periods calculated here agree with those recently observed. $^{11,12}$ To make this correspondence, we associate the measured $F_{\alpha}$ and $F_{\beta}$ stripe periods $^{11,12}$ with those of cases (III) and (II), respectively. This value of $\kappa_{\perp}$ for $PbTiO_{3}$ may therefore be more accurate than the gradient coefficient values adopted in previous theoretical work, $^{25}$ which correspond to $\kappa_{\perp}=(1.0$ or $3.3)\times 10^{-10}\ \mathrm{V\ m^{3}/C}$ (see Appendix C).

The equilibrium stripe period is predicted to be only weakly dependent on temperature, and to scale with the square root of film thickness for thicknesses larger than about $10\ \mathrm{nm}$, in agreement with the observations. $^{11,12}$ For smaller thicknesses, where the equilibrium stripe period is comparable to the film thickness, the stripe period is predicted to deviate positively from this scaling law. The calculated suppression of $T_{C}$ from the thick-film value is approximately inversely proportional to film thickness. The results for upper interfaces bounded by either $SrTiO_{3}$ dielectric or vacuum [cases (I) or (III)] are very similar, while the results for an upper interface bounded by a perfect conductor [case (II)] are equivalent to those for a case (I) film of twice the thickness. Thus the stripe period increases by a factor of $\sqrt{2}$, and the suppression of $T_{C}$ is halved when the upper interface changes from insulating to conducting.

The case (I) results have been compared with those from the existing analytical solution using the approximate free energy for a linear ferroelectric. While qualitatively similar thickness dependences are obtained, the analytical solution gives a significantly more accurate result for the equilibrium stripe period ($20\%$ underestimate) than for the $T_{C}$ suppression (up to a factor of 10 overestimate).

The nonlinear result for the suppression of $T_{C}$ in case (I) can be expressed as $T_{C}^{*}-T_{C}\approx 2C\lambda/t$, where $C=1.5\times 10^{5}\ \mathrm{K}$ is the Curie constant for $PbTiO_{3}$ and $\lambda=5\times 10^{-12}\ \mathrm{m}$ is a

characteristic length. This functional form is identical to that given by classical theories for the suppression of $T_{C}$ in monodomain ferroelectric thin films due to either a finite electronic screening length in conducting electrodes $^{2}$ or an "intrinsic" surface effect. $^{34,35}$ In the former case, the value of $\lambda$ corresponds to the screening length in the electrode. In the latter case, the intrinsic surface effect gives $\lambda=\xi_{0}^{2} /(\xi_{0}+\delta)$ , where $\xi_{0}=(\epsilon_{0} \kappa_{11})^{1 / 2}$ is the longitudinal correlation length andδ is a parameter called the "extrapolation length." Both of these effects have been purposely left out of the analysisabove, to understand the effects arising solely form $180^{\circ}$  stripe domains. It would be straightforward to add them to the thermodynamic analysis developed here; however, the values of the parameters involved are not known. The very small value of $\lambda$ found in our study indicates that stripe domains alone are very effective at neutralizing the depolar- izing field in thin ferroelectric films.

The characteristics of the stripe domains found here are remarkably consistent with those of recent atomistic calcula- tions, considering that different material systems, tempera- tures, and boundary conditions have been modeled. Ab initio based Monte Carlo simulation $^{21-24}$ of epitaxially strained $PbZr_{0.5} Ti_{0.5} O_{3}$ surrounded by vacuum have found $180^{\circ}$ stripe periods of 2.8-4 nm for films with thicknesses in the range of 1.6-4 nm at temperatures near 0 K. A stripe period of2.4 nm has been reported for a shell-model simulation $^{19}$ of a3 nm thick $BaTiO_{3}$ film surrounded by vacuum near 0 K. These are about $20 \%$ smaller than the stripe periods we would predict for epitaxially strained $PbTiO_{3}$ films of these thicknesses at $T_{C}$ with case (III) boundary conditions.

The calculations presented here provide quantitative val- ues for the electric fields present near the interfaces in stripe domain systems. As the temperature decreases and the polar- ization within the film increases, the magnitude of these elec- tric fields increases. If these increase sufficiently, it may be possible to promote carriers across the band gap of the film or substrate, or to attract sufficient ions from the vapor phase above the film in case (III), to compensate the depolarizing field by free charge. To illustrate the energy available per unit charge to drive such interfacial compensation, Fig. 12 compares the total free energy per unit area relative to the nonpolar phase, $A-t A_{0}^{*}$ , divided by the average polarization $P^{\dagger}$ , as a function of temperature for a film of thickness t=12.1 nm under three conditions: a film with stripe domains and case (III) boundary conditions (no free charge at either interface), a film with stripe domains and case (II) boundary conditions (top interface compensated by free charge), and a monodomain film with both interfaces fully compensated by free charge (e.g., short-circuited, perfect-conductor top and bottom electrodes). For the monodomain case the free energy is obtained from Eq. (A7) with $P=(0,0, P_{0}^{*}), E=0$ . The rela tive values of these curves give the energy per unit charge(i.e., voltage) available to drive interfacial compensation and achieve the lower-energy condition. In this case differ- ences of about 100-200 mV are available to attract charge to compensate a single (top) interface, while voltages several times larger are available if both interfaces are compensated. These voltages increase approximately proportionally to film thickness. They can become comparable to the band gap of $PbTiO_{3}( 4 V)$ for thicker films at low temperatures, sug gesting that field-effect creation of free carriers must be con- sidered.

![](./images/812056467958923265_14.jpg)

FIG. 12. Total energy per unit polarization as a function of T for a film of thickness t=12.1 nm with zero, one, and two interfaces compensated. From top to bottom, the curves correspond to case (III), case (II), and a mon- odomain film with uniform polarization $P=(0,0, P_{0}^{*})$ and zero electric field.

Although we have included effects of epitaxial strain on ferroelectric stripe domains, approximations remain in the analysis. The elastic solution used neglects some potentially important effects in ultrathin films with stripe domains, suchas polarization-dependent displacements (offsets) in the $r_{3}$  direction across the domain wall and at the film interfaces. In general the zero-stress offsets across the domain wall and the interfaces of the positive and negative domains cannot all be satisfied without elastic strain. The balance between the wall and interface offsets will change as a function of film thick- ness, producing additional thickness effects. These are not captured in the free energy (A1) or the constitutive relations(A3), but could be included, e.g., by adding terms coupling polarization gradients to strain. Even within the framework of the free energy expression (A1), the approach taken here of incorporating elastic energy by renormalizing the polar- ization coefficients involves an approximation in the case of stripe domains, as discussed in Appendix B. To avoid the approximations inherent in this approach and to satisfy the need for strain compatibility, in future work an indepen- dently varied displacement field could be included in the free energy minimization procedure.

ACKNOWLEDGMENTS

The authors thank S. K. Streiffer for contributing hisinsight in extensive discussions. One of the authors (K.R.E.) would like to acknowledge support from the Materials Theory Institute at Argonne National Laboratory and from

the NSF under Grant No. DMR-0413062. This work was supported by the U.S. Department of Energy, Office of Sci- ence, Basic Energy Sciences under Contract No. W-31-109- ENG-38.

## APPENDIX A: THERMODYNAMICS OF SINGLE DOMAIN FERROELECTRIC FILMS

Here we consider the free energy of homogeneous, spa- tially uniform, single domain systems, in order to develop the free energy density to be used for nonuniform systems with stripe domains. The proper choice of thermodynamic state function to be minimized at equilibrium depends on the boundary conditions. Different state functions account for the thermal, mechanical, and electrical energies transferred across the boundaries under different conditions. We con- sider systems at constant temperature, so in all cases the appropriate function is a free energy. In general we will con- sider systems which are isolated with respect to mechanical and electrical energies, so that the environment does no work on the system. In this case the state function minimized at equilibrium is the Helmholtz free energy $A$. It is useful to consider the Gibbs free energy $G$ as well.

Each of the state functions has a different set of principal variables. The two pairs of conjugate variables relevant to our problem are strain $\mathbf{x}$ and stress $\mathbf{X}$, and electric displace- ment (flux density) $\mathbf{D}$ and field $\mathbf{E}$. It is assumed that the equilibrium state of a system is determined by specifying one variable from each pair, either $\mathbf{x}$ or $\mathbf{X}$ and either $\mathbf{D}$ or $\mathbf{E}$. For example, the Helmholtz free energy $A$ has principal variables $\mathbf{x}$ and $\mathbf{D}$, and the Gibbs free energy $G$ has principal variables $\mathbf{X}$ and $\mathbf{E}$. They are related by $G \equiv A-\sum_{i} X_{i} x_{i}-\sum_{i} E_{i} D_{i}$. Subscripts on $D_{i}$ and $E_{i}$ refer to the Cartesian components of the vectors $\mathbf{D}$ and $\mathbf{E}$, while $x_{i}$ or $X_{i}$ are the single-index-notation components of the tensors $\mathbf{x}$ and $\mathbf{X}^{36}$

The first law can be written in terms of these quantities using differential relations such as $d A=\sum_{i} X_{i} d x_{i}+\sum_{i} E_{i} d D_{i}$ or $d G=-\sum_{i} x_{i} d X_{i}-\sum_{i} D_{i} d E_{i}$. Expressions for the equilibrium free energies in terms of their principal variables can therefore be used to give constitutive equations for the remaining depen- dent variables, using relations such as $E_{i}=d A /\left.d D_{i}\right|_{D_{j \neq x}}$ and $x_{i}=-d G /\left.d X_{i}\right|_{X_{i}, E}$. Another use of the free energies stems from the second law, which implies that, for fixed values of a set of principal variables, the corresponding state function is minimized at equilibrium. Since the principal variables are fixed, this minimization is with respect to other "internal" variables, such as order parameters describing the internal structure of the system. For ferroelectrics, the primary inter- nal variable of interest is the polarization $\mathbf{P}$. In systems with domains, other internal variables might describe the domain size, arrangement, etc. The general expression for the free energy density of a system not necessarily at equilibrium (the "incomplete thermodynamic potential" $^{1}$ ) is thus a function of both the principal variables and the internal variables.

### 1. Free energy density

Several different forms of the polarization, stress, and electric field terms in the free energy densities have been used in the literature. The expression we adopt for the Gibbs free energy density is

$$
\begin{aligned}
G= & A_{0}+\alpha_{1}\left(P_{1}^{2}+P_{2}^{2}+P_{3}^{2}\right)+\alpha_{11}\left(P_{1}^{4}+P_{2}^{4}+P_{3}^{4}\right)+\alpha_{12}\left(P_{1}^{2} P_{2}^{2}+P_{2}^{2} P_{3}^{2}+P_{3}^{2} P_{1}^{2}\right)+\alpha_{111}\left(P_{1}^{6}+P_{2}^{6}+P_{3}^{6}\right)+\alpha_{112}\left[P_{1}^{4}\left(P_{2}^{2}+P_{3}^{2}\right)\right. \\
& \left.+P_{2}^{4}\left(P_{3}^{2}+P_{1}^{2}\right)+P_{3}^{4}\left(P_{1}^{2}+P_{2}^{2}\right)\right]+\alpha_{123}\left(P_{1}^{2} P_{2}^{2} P_{3}^{2}\right)-s_{11}\left(X_{1}^{2}+X_{2}^{2}+X_{3}^{2}\right) / 2-s_{12}\left(X_{1} X_{2}+X_{2} X_{3}+X_{3} X_{1}\right)-s_{44}\left(X_{4}^{2}+X_{5}^{2}+X_{6}^{2}\right) / 2 \\
& -Q_{11}\left(X_{1} P_{1}^{2}+X_{2} P_{2}^{2}+X_{3} P_{3}^{2}\right)-Q_{12}\left[X_{1}\left(P_{2}^{2}+P_{3}^{2}\right)+X_{2}\left(P_{3}^{2}+P_{1}^{2}\right)+X_{3}\left(P_{1}^{2}+P_{2}^{2}\right)\right]-Q_{44}\left(X_{4} P_{2} P_{3}+X_{5} P_{3} P_{1}+X_{6} P_{1} P_{2}\right) \\
& -\sum_{i}\left(\frac{\epsilon_{0}}{2} E_{i}^{2}+E_{i} P_{i}\right), \quad \text { (A1) }
\end{aligned}
$$

where $A_{0}$ is the free energy density of the stress-free, zero- field, nonpolar state $(\mathbf{X}=\mathbf{E}=\mathbf{P}=0)$ and $\epsilon_{0}=8.85$ $\times 10^{-12} \mathrm{C} / \mathrm{V} \mathrm{m}$ is the permittivity of free space. Equation (A1) is obtained by taking the expression used by Haun $e t$ $a l .{ }^{26}$ for $G$ at $\mathbf{E}=0$ as a function of the $P_{i}$ and $X_{i}$, and adding the electric field terms (as given, e.g., in Ref. 37).

The self-consistent constitutive relations are

$$
D_{i}=\epsilon_{0} E_{i}+P_{i}, \quad \text { (A2) }
$$

$$
x_{1}=s_{11} X_{1}+s_{12}\left(X_{2}+X_{3}\right)+Q_{11} P_{1}^{2}+Q_{12}\left(P_{2}^{2}+P_{3}^{2}\right),
$$

$$
x_{2}=s_{11} X_{2}+s_{12}\left(X_{3}+X_{1}\right)+Q_{11} P_{2}^{2}+Q_{12}\left(P_{3}^{2}+P_{1}^{2}\right),
$$

$$
\begin{aligned}
& x_{3}=s_{11} X_{3}+s_{12}\left(X_{1}+X_{2}\right)+Q_{11} P_{3}^{2}+Q_{12}\left(P_{1}^{2}+P_{2}^{2}\right), \\
& x_{4}=s_{44} X_{4}+Q_{44} P_{2} P_{3},
\end{aligned}
$$

$$
x_{5}=s_{44} X_{5}+Q_{44} P_{3} P_{1},
$$

$$
x_{6}=s_{44} X_{6}+Q_{44} P_{1} P_{2},
$$

where the reference state of zero strain is the unstressed non- polar phase. These expressions for the $D_{i}$ and $x_{i}$ can be used to eliminate them from the relation between $G$ and $A$, allow- ing $A$ to be expressed in terms of the $P_{i}, X_{i}$, and $E_{i}$,

$$
\begin{aligned}
A= & A_{0}+\alpha_{1}\left(P_{1}^{2}+P_{2}^{2}+P_{3}^{2}\right)+\alpha_{11}\left(P_{1}^{4}+P_{4}^{2}+P_{3}^{4}\right)+\alpha_{12}\left(P_{1}^{2} P_{2}^{2}-P_{2}^{2} P_{3}^{2}+P_{3}^{2} P_{1}^{2}\right)+\alpha_{111}\left(P_{1}^{6}+P_{2}^{6}+P_{3}^{6}\right)+\alpha_{112}\left[P_{1}^{4}\left(P_{2}^{2}+P_{3}^{2}\right)+P_{2}^{4}\left(P_{3}^{2}\right.\right. \\
& \left.\left.+P_{1}^{2}\right)+P_{3}^{4}\left(P_{1}^{2}+P_{2}^{2}\right)\right]+\alpha_{123}\left(P_{1}^{2} P_{2}^{2} P_{3}^{2}\right)+s_{11}\left(X_{1}^{2}+X_{2}^{2}+X_{3}^{2}\right) / 2+s_{12}\left(X_{1} X_{2}+X_{2} X_{3}+X_{3} X_{1}\right)+s_{14}\left(X_{4}^{2}+X_{5}^{2}+X_{6}^{2}\right) / 2+\epsilon_{2}\left(E_{1}^{2}\right. \\
& \left.+E_{2}^{2}+E_{3}^{2}\right) / 2.
\end{aligned}
\tag{A4}
$$

It is interesting to note that this expression for the Helmholtz free energy density $A$ contains no cross terms between polarization, stress, and electric field.

The values for all of the coefficients in the expressions for the free energies have been determined for $PbTiO_{3}$ by comparison with experiment. $^{26-29}$ Experimental data at a variety of temperatures both above and below $T_{C}$ can be fit using only a single temperature-dependent coefficient,

$$\alpha_{1}=(T-\theta) / 2 \epsilon_{0} C, \tag{A5}$$

where $\theta$ and $C$ are constants. Values of all the coefficients are listed in Table I. These are identical to those used in several previous theoretical studies. $^{25,30}$ (Note the difference of a factor of 2 in the definition of $Q_{44}$ in Ref. 25 arising from the tensor strain notation used there.)

### 2. Coherently strained epitaxial film

We next wish to consider the equations for the case of uniform, coherent epitaxial films having in-plane strain equal to the epitaxial misfit $(x_{1}=x_{2}=x_{m}, x_{6}=0)$, and zero stress normal to the surface $(X_{3}=X_{4}=X_{5}=0)$. For fully strained $PbTiO_{3}$ on $SrTiO_{3}$, the epitaxial misfit is a function of temperature given by $x_{m}=(a_{S}-a_{P}^{\text{cub}})/a_{P}^{\text{cub}}$, where $a_{S}$ and $a_{P}^{\text{cub}}$ are the zero-stress lattice parameters of cubic, nonpolar $SrTiO_{3}$ and $PbTiO_{3}$, respectively. Here $a_{P}^{\text{cub}}$ can be measured above $T_{C}$, but must be extrapolated to temperatures below $T_{C}$ based on analysis of the $a$ and $c$ lattice parameters of the tetragonal phase. $^{26}$ The values of $a_{S}(T)$ (Ref. 38) and $a_{P}^{\text{cub}}(T)$ are given in Table II. Since the cubic and tetragonal lattice parameters of $PbTiO_{3}$ are part of the experimental data used to determine the coefficients in the free energy expansion, $^{26,29}$ we have used the expressions for $a_{P}^{\text{cub}}(T)$ above and below $T_{C}$ which are consistent with the coefficients in Table I.

Equations (A3) can be solved to give the other stress and strain components as a function of misfit, $^{30}$

$$
\begin{aligned}
x_{3}= & \frac{2 s_{12}}{s_{11}+s_{12}} x_{m}-\frac{s_{12} Q_{11}-s_{11} Q_{12}}{s_{11}+s_{12}}\left(P_{1}^{2}+P_{2}^{2}\right) \\
& +\frac{\left(s_{11}+s_{12}\right) Q_{11}-2 s_{12} Q_{12}}{s_{11}+s_{12}} P_{3}^{2}, \\
x_{4}= & Q_{44} P_{2} P_{3}, \\
x_{5}= & Q_{44} P_{3} P_{1}, \\
X_{1}= & x_{m} /\left(s_{11}+s_{12}\right)-\left[\left(Q_{11}+Q_{12}\right)\left(P_{1}^{2}+P_{2}^{2}\right) / 2+Q_{12} P_{3}^{2}\right] / \\
& \left(s_{11}+s_{12}\right)-\left(Q_{11}-Q_{12}\right)\left(P_{1}^{2}-P_{2}^{2}\right) / 2\left(s_{11}-s_{12}\right), \\
X_{2}= & x_{m} /\left(s_{11}+s_{12}\right)-\left[\left(Q_{11}+Q_{12}\right)\left(P_{1}^{2}+P_{2}^{2}\right) / 2+Q_{12} P_{3}^{2}\right] / \\
& \left(s_{11}+s_{12}\right)+\left(Q_{11}-Q_{12}\right)\left(P_{1}^{2}-P_{2}^{2}\right) / 2\left(s_{11}-s_{12}\right), \\
X_{6}= & -Q_{44} P_{1} P_{2} / s_{44}.
\end{aligned}
\tag{A6}
$$

Even though the boundary conditions are mixed between fixed stress and fixed strain, $^{30}$ the boundary stress is zero when the strain is nonzero, so no work is done on the system. Thus the free energy minimized at equilibrium is the Helmholtz free energy. The expressions for stress [Eqs. (A6)] can be substituted into Eq. (A4) to give

$$
\begin{aligned}
A= & A_{0}^{*}+\alpha_{1}^{*}\left(P_{1}^{2}+P_{2}^{2}\right)+\alpha_{3}^{*} P_{3}^{2}+\alpha_{11}^{*}\left(P_{1}^{4}+P_{4}^{2}\right)+\alpha_{33}^{*} P_{3}^{4} \\
& +\alpha_{13}^{*}\left(P_{2}^{2} P_{3}^{2}+P_{3}^{2} P_{1}^{2}\right)+\alpha_{12}^{*}\left(P_{1}^{2} P_{2}^{2}\right)+\alpha_{111}\left(P_{1}^{6}+P_{2}^{6}+P_{3}^{6}\right) \\
& +\alpha_{112}\left[P_{1}^{4}\left(P_{2}^{2}+P_{3}^{2}\right)+P_{4}^{2}\left(P_{3}^{2}+P_{1}^{2}\right)+P_{3}^{4}\left(P_{1}^{2}+P_{2}^{2}\right)\right] \\
& +\alpha_{123}\left(P_{1}^{2} P_{2}^{2} P_{3}^{2}\right)+\epsilon_{0}\left(E_{1}^{2}+E_{2}^{2}+E_{3}^{2}\right) / 2,
\end{aligned}
\tag{A7}
$$

where the free energy of the $\mathbf{P}=\mathbf{E}=\mathbf{0}$ reference state, $A_{0}^{*}$, and six of the coefficients, marked with an asterisk, have different values than in Eq. (A4). The renormalized coefficients are given by $^{30}$

$$
\begin{aligned}
& A_{0}^{*}=A_{0}+x_{m}^{2} /\left(s_{11}+s_{12}\right), \\
& \alpha_{1}^{*}=\alpha_{1}-x_{m}\left(Q_{11}+Q_{12}\right) /\left(s_{11}+s_{12}\right),
\end{aligned}
$$

<table>
<caption>TABLE I. Values of coefficients in the free energy expressions for unstressed bulk $PbTiO_{3}$.</caption>
<tbody>
<tr>
<td>$T_{C}$</td>
<td>765.4</td>
<td>K</td>
<td>$C$</td>
<td>$1.5×10^{5}$</td>
<td>
</td>
</tr>
<tr>
<td>$\theta$</td>
<td>752.0</td>
<td>K</td>
<td>$Q_{11}$</td>
<td>$8.9×10^{-2}$</td>
<td>$\text{m}^{4}/\text{C}^{2}$</td>
</tr>
<tr>
<td>$\alpha_{11}$</td>
<td>$-7.25×10^{7}$</td>
<td>$\text{V m}^{5}/\text{C}^{3}$</td>
<td>$Q_{12}$</td>
<td>$-2.6×10^{-2}$</td>
<td>$\text{m}^{4}/\text{C}^{2}$</td>
</tr>
<tr>
<td>$\alpha_{12}$</td>
<td>$7.5×10^{8}$</td>
<td>$\text{V m}^{5}/\text{C}^{3}$</td>
<td>$Q_{44}$</td>
<td>$6.75×10^{-2}$</td>
<td>$\text{m}^{4}/\text{C}^{2}$</td>
</tr>
<tr>
<td>$\alpha_{111}$</td>
<td>$2.61×10^{8}$</td>
<td>$\text{V m}^{9}/\text{C}^{5}$</td>
<td>$s_{11}$</td>
<td>$8.0×10^{-12}$</td>
<td>$\text{m}^{2}/\text{N}$</td>
</tr>
<tr>
<td>$\alpha_{112}$</td>
<td>$6.1×10^{8}$</td>
<td>$\text{V m}^{9}/\text{C}^{5}$</td>
<td>$s_{12}$</td>
<td>$-2.5×10^{-12}$</td>
<td>$\text{m}^{2}/\text{N}$</td>
</tr>
<tr>
<td>$\alpha_{123}$</td>
<td>$-3.7×10^{9}$</td>
<td>$\text{V m}^{9}/\text{C}^{5}$</td>
<td>$s_{44}$</td>
<td>$9.0×10^{-12}$</td>
<td>$\text{m}^{2}/\text{N}$</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE II. Coefficients for cubic lattice constants of $PbTiO_{3}$ and $SrTiO_{3}$ using the functional form $a=a_{0}[1+\sum_{n}b_{n}(T-T_{\text{ref}})^{n}]$.</caption>
<tbody>
<tr>
<th>Coefficient</th>
<td>Value for $SrTiO_{3}$</td>
<td>Value for $PbTiO_{3}$ ($T>T_{C}$)</td>
<td>Value for $PbTiO_{3}$ ($T<T_{C}$)</td>
</tr>
<tr>
<th>$a_{0}$ (nm)</th>
<td>0.392 47</td>
<td>0.396 63</td>
<td>0.396 63</td>
</tr>
<tr>
<th>$T_{\text{ref}}$ (K)</th>
<td>765</td>
<td>765</td>
<td>765</td>
</tr>
<tr>
<th>$b_{1}(×10^{-5})$</th>
<td>1.133</td>
<td>1.29</td>
<td>0.472</td>
</tr>
<tr>
<th>$b_{2}(×10^{-9})$</th>
<td>1.367</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>$b_{3}(×10^{-13})$</th>
<td>1.923</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

![](./images/812056467958923265_15.jpg)

FIG. 13. Temperature-dependent coefficients in the free energy density for coherently strained $PbTiO_{3}$ on $SrTiO_{3}$. The $\oplus$ coefficients plotted here correspond to the thick-film limit $P^{\dagger}=P_{0}^{*}$, as discussed in Appendix B; for finite $t$, as $T \to T_{C}$ and $P^{\dagger} \to 0$, the $\oplus$ coefficients approach the $*$ values.

$$
\begin{aligned}
\alpha_{3}^{*}= & \alpha_{1}-2 x_{m} Q_{12} /\left(s_{11}+s_{12}\right), \\
\alpha_{11}^{*}= & \alpha_{11}+\left[\left(Q_{11}^{2}+Q_{12}^{2}\right) s_{11} / 2-Q_{11} Q_{12} s_{12}\right] /\left(s_{11}^{2}-s_{12}^{2}\right), \\
\alpha_{33}^{*}= & \alpha_{11}+Q_{12}^{2} /\left(s_{11}+s_{12}\right), \\
\alpha_{13}^{*}= & \alpha_{12}+Q_{12}\left(Q_{11}+Q_{12}\right) /\left(s_{11}+s_{12}\right), \\
\alpha_{12}^{*}= & \alpha_{12}-\left[\left(Q_{11}^{2}+Q_{12}^{2}\right) s_{12}-2 Q_{11} Q_{12} s_{11}\right] /\left(s_{11}^{2}-s_{12}^{2}\right) \\
& +Q_{44}^{2} /\left(2 s_{44}\right).
\end{aligned}
$$

(A8)

Values of $A_{0}^{*}$, $\alpha_{1}^{*}$, and $\alpha_{3}^{*}$ depend on temperature, and are shown in Fig. 13. Values of the temperature-independent coefficients are listed in Table III.

### 3. Coherently strained epitaxial film with uniaxial polarization

Because compressive epitaxial strain favors uniaxial polarization normal to the surface in $PbTiO_{3},{ }^{30}$ it is useful to consider the simple case in which $P_{3}$ and $E_{3}$ are the only nonzero components. The nonzero components of stress and strain and the free energy are given by $x_{1}=x_{2}=x_{m}$, ,

$$
\begin{gathered}
x_{3}=Q_{11} P_{3}^{2}+2 s_{12}\left(x_{m}-Q_{12} P_{3}^{2}\right) /\left(s_{11}+s_{12}\right) \\
X_{1}=X_{2}=\left(x_{m}-Q_{12} P_{3}^{2}\right) /\left(s_{11}+s_{12}\right),
\end{gathered}
$$

(A9)

$$
A=A_{0}^{*}+\alpha_{3}^{*} P_{3}^{2}+\alpha_{33}^{*} P_{3}^{4}+\alpha_{111}^{*} P_{3}^{6}+\left(\epsilon_{0} / 2\right) E_{3}^{2}. \quad \text { (A10) }
$$

The equilibrium polarization of the epitaxial film is obtained by minimizing $A$ with respect to $P_{3}$ at fixed $D_{3}$, which gives

$$
\begin{gathered}
E_{3}=\left(1 / \epsilon_{0}\right)\left(D_{3}-P_{3}\right)=2 \alpha_{3}^{*} P_{3}+4 \alpha_{33}^{*} P_{3}^{3}+6 \alpha_{111}^{*} P_{3}^{5} . \\
\text { (A11) }
\end{gathered}
$$

This can be solved for the spontaneous polarization at $E_{3}$ $=0$,

$$
P_{0}^{* 2}=\left[-\alpha_{33}^{*}+\left(\alpha_{3}^{* 2}-3 \alpha_{3}^{*} \alpha_{111}\right)^{1 / 2}\right] / 3 \alpha_{111} . \quad \text { (A12) }
$$

The renormalization of the free energy coefficients due to epitaxial misfit strain modifies the paraelectric-toferroelectric phase transition. $^{30}$ Since $\alpha_{33}^{*}$ is positive, the transition for $E_{3}=0$ is second order, rather than first order. The transition temperature for $E_{3}=0$ is determined by the change in sign of $\alpha_{3}^{*}$, which gives

$$
T_{C}^{*}=\theta+4 \epsilon_{0} C Q_{12} x_{m} /\left(s_{11}+s_{12}\right) . \quad \text { (A13) }
$$

For the $x_{m}(T)$ appropriate for epitaxially strained $PbTiO_{3}$ on $\mathrm{SrTiO}_{3}$, the transition is predicted to occur at $T_{C}^{*}=1025 \mathrm{~K}$, about $260 \mathrm{~K}$ higher than in the unconstrained case.

### APPENDIX B: ELASTIC SOLUTION FOR EPITAXIAL FILMS WITH STRIPE DOMAINS

Here we consider the nonuniform stress and strain in epitaxial films with $180^{\circ}$ stripe domains. We would like to express the stress in terms of the polarization, in order to eliminate the stress terms in the free energy (A4) and obtain renormalized polarization coefficients, as we did in Appendix A for a uniformly strained single domain film. We initially consider the "zero $X_{3}$ " solution developed above for uniform systems, and determine that it is a poor approximation for the case of stripe domains. A "fixed $x_{3}$ " solution appropriate for stripe domains is then developed.

In both cases we consider stripe domains running in the $r_{2}$ direction, which are periodic in the $r_{1}$ direction, as shown in Fig. 1. We assume the domain walls are of Ising (rather than Bloch) type, as discussed in Appendix D. In this geometry, the mirror symmetry perpendicular to $r_{2}$ leads us to assume that the components of polarization $P_{2}$ and strain $x_{4}$ are zero. The constraint of coherent epitaxial strain is the same as in a uniform system, and determines three components of strain $\left(x_{1}=x_{2}=x_{m}, x_{6}=0\right)$ at the epitaxial interface(s). For simplicity, we will assume that these strains are uniform in the film. We will also assume that the free energy density (A1) and the derived constitutive equations (A3) for a uniform system hold, so that we neglect any effects associated with a polarization-dependent displacement (offset) across the domain walls or film interfaces. The stress components $X_{4}$ and $X_{6}$ are thus also zero.

<table>
<caption>TABLE III. Values of the renormalized temperature-independent coefficients in the free energy expressions for epitaxially strained $PbTiO_{3}$.</caption>
<tbody>
<tr>
<td>$\alpha_{11}^{*}$</td>
<td>$4.2×10^{8}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\alpha_{33}^{*}$</td>
<td>$5.0×10^{7}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
<td>$\alpha_{33}^{\oplus}$</td>
<td>$4.2×10^{8}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
</tr>
<tr>
<td>$\alpha_{13}^{*}$</td>
<td>$4.5×10^{8}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
<td>$\alpha_{13}^{\oplus}$</td>
<td>$7.3×10^{8}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
</tr>
<tr>
<td>$\alpha_{12}^{*}$</td>
<td>$7.3×10^{8}$</td>
<td>$\mathrm{V\ m^{5}/C^{3}}$</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### 1. Zero $X_3$ elastic solution

If we assume that $X_3$=0 throughout the film, the stress solution is similar to that obtained above for a single domain epitaxial film. The values of $x_3$, $X_1$, and $X_2$ can be obtained from Eq. (A6) with $P_2$=0,

$$
\begin{aligned}
x_{3}= & \frac{2 s_{12}}{s_{11}+s_{12}} x_{m}-\frac{s_{12} Q_{11}-s_{11} Q_{12}}{s_{11}+s_{12}} P_{1}^{2} \\
& +\frac{\left(s_{11}+s_{12}\right) Q_{11}-2 s_{12} Q_{12}}{s_{11}+s_{12}} P_{3}^{2}, \\
X_{1}= & \frac{x_{m}-Q_{12} P_{3}^{2}}{s_{11}+s_{12}}-\frac{s_{11} Q_{11}-s_{12} Q_{12}}{s_{11}^{2}-s_{12}^{2}} P_{1}^{2}, \\
X_{2}= & \frac{x_{m}-Q_{12} P_{3}^{2}}{s_{11}+s_{12}}-\frac{s_{11} Q_{12}-s_{12} Q_{11}}{s_{11}^{2}-s_{12}^{2}} P_{1}^{2},
\end{aligned}
\tag{B1}
$$

where these now all vary with position. The contributions of these terms to the free energy are the same as for the monodomain system and give the same renormalized coefficients (A7) and (A8). However, since $x_3$ varies in the $r_1$ direction, strain compatibility requires $x_5$ to be nonzero. $^{39}$ The variation of $x_5$ can be determined from the relationship $\nabla_1\nabla_3x_5$ $=2\nabla_1^2x_3$. The stress component $X_5$ is nonzero, and can be obtained from

$$
X_{5}=\frac{x_{5}-Q_{44} P_{1} P_{3}}{s_{44}}. \tag{B2}
$$

This gives an additional contribution to the free energy through the term $(1/2)s_{44}X_{5}^{2}$, which is not present in the expression obtained above for the single domain film. The new term is generally not negligible. For stripe domains in $PbTiO_3$ lattice matched to $SrTiO_3$ at typical temperatures (e.g., $T=T_C^*-100$ K), $x_3$ varies periodically in the $r_1$ direction with an amplitude of several percent. Differentiating in $r_1$ and integrating in $r_3$ multiplies this by approximately the film thickness divided by the domain wall width, giving peaks in $x_5$ approaching unity at the domain walls. The resulting strain energy $(1/2)s_{44}X_{5}^{2}$ integrates to a large value, giving a positive contribution typically 10–100 times the magnitude of the free energy calculated neglecting this term. Thus the zero $X_3$ elastic solution developed for uniform, monodomain films does not predict a stable stripe domain state.

### 2. Fixed $x_3$ elastic solution

An elastic solution appropriate for stripe domains can be obtained by assuming that the strain component $x_3$ is constant. In this case the strain $x_5$ will be zero. Using Eqs. (A3), the strains can be written as

$$
\begin{aligned}
x_{1}=x_{m} & =s_{11} X_{1}+s_{12}\left(X_{2}+X_{3}\right)+Q_{12}\left(P_{1}^{2}+P_{3}^{2}\right), \\
x_{2}=x_{m} & =s_{11} X_{2}+s_{12}\left(X_{1}+X_{3}\right)+Q_{11} P_{1}^{2}+Q_{12} P_{3}^{2}, \\
x_{3}=x^{\dagger} & \equiv Q_{11} P^{2}+2 s_{12}\left(x_{m}-Q_{12} P^{\dagger 2}\right) /\left(s_{11}+s_{12}\right) \\
& =s_{11} X_{3}+s_{12}\left(X_{1}+X_{2}\right)+Q_{11} P_{3}^{2}+Q_{12} P_{1}^{2}, \\
x_{5}=0 & =s_{44} X_{5}+Q_{44} P_{1} P_{3},
\end{aligned}
\tag{B3}
$$

where the fixed $x_3$ value, $x^{\dagger}$, has been expressed in terms of an equivalent polarization $P^{\dagger}$ in analogy with Eq. (A9). One can solve these equations to obtain the nonzero stress components in terms of the polarization,

$$
\begin{aligned}
& X_{1}=C_{11} P_{1}^{2}+C_{12}\left(P_{3}^{2}-P^{\dagger 2}\right)+X_{m}, \\
& X_{2}=C_{12} P_{1}^{2}+C_{12}\left(P_{3}^{2}-P^{\dagger 3}\right)+X_{m}, \\
& X_{3}=C_{12} P_{1}^{2}+C_{11}\left(P_{3}^{2}-P^{\dagger 2}\right), \\
& X_{5}=-\left(Q_{44} / s_{44}\right) P_{1} P_{3},
\end{aligned}
\tag{B4}
$$

where the coefficients are defined by

$$
\begin{aligned}
C_{11} & \equiv \frac{2 s_{12} Q_{12}-\left(s_{11}+s_{12}\right) Q_{11}}{\left(s_{11}-s_{12}\right)\left(s_{11}+2 s_{12}\right)}, \\
C_{12} & \equiv \frac{s_{12} Q_{11}-s_{11} Q_{12}}{\left(s_{11}-s_{12}\right)\left(s_{11}+2 s_{12}\right)}, \\
X_{m} & \equiv \frac{x_{m}-Q_{12} P^{\dagger 2}}{s_{11}+s_{12}}.
\end{aligned}
\tag{B5}
$$

Substituting Eqs. (B4) and (B5) into Eq. (A4) gives

$$
\begin{aligned}
A= & A_{0}^{\oplus}+\alpha_{1}^{\oplus} P_{1}^{2}+\alpha_{3}^{\oplus} P_{3}^{2}+\alpha_{33}^{\oplus}\left(P_{1}^{4}+P_{3}^{4}\right)+\alpha_{13}^{\oplus} P_{1}^{2} P_{3}^{2} \\
& +\alpha_{111}\left(P_{1}^{6}+P_{3}^{6}\right)+\alpha_{112}\left(P_{1}^{4} P_{3}^{2}+P_{3}^{4} P_{1}^{2}\right)+\epsilon_{0}\left(E_{1}^{2}+E_{3}^{2}\right) / 2,
\end{aligned}
\tag{B6}
$$

where the renormalized coefficients include terms in addition to those in Eqs. (A8),

$$
\begin{aligned}
A_{0}^{\oplus} & =A_{0}^{*}+C_{33}^{\oplus} P^{\dagger 4}, \\
\alpha_{1}^{\oplus} & =\alpha_{1}^{*}-C_{13}^{\oplus} P^{\dagger 2}, \\
\alpha_{3}^{\oplus} & =\alpha_{3}^{*}-2 C_{33}^{\oplus} P^{\dagger 2}, \\
\alpha_{33}^{\oplus} & =\alpha_{33}^{*}+C_{33}^{\oplus}, \\
\alpha_{13}^{\oplus} & =\alpha_{13}^{*}+C_{13}^{\oplus}+Q_{44}^{2} / 2 s_{44},
\end{aligned}
\tag{B7}
$$

with new coefficients defined by

![](./images/812056467958923265_16.jpg)

FIG. 14. Free energy density vs $P_3$ for coherently strained PbTiO$_3$ on SrTiO$_3$ calculated using the stripe domain and monodomain elastic solutions with $P_1$=$P_2$=$E$=0 and $P^\dagger$=$P_0^*$ at $T$=$T_C^*$-100 K.

$$
\begin{aligned}
C_{33}^{\oplus} & \equiv \frac{\left[\left(s_{11}+s_{12}\right) Q_{11}-2 s_{12} Q_{12}\right]^{2}}{2\left(s_{11}^{2}-s_{12}^{2}\right)\left(s_{11}+2 s_{12}\right)}, \\
C_{13}^{\oplus} & \equiv \frac{-s_{12} Q_{11}^{2}+2 s_{11} Q_{11} Q_{12}+\left(s_{11}-2 s_{12}\right) Q_{12}^{2}}{\left(s_{11}-s_{12}\right)\left(s_{11}+2 s_{12}\right)} \\
& \quad-\frac{\left(Q_{11}+Q_{12}\right) Q_{12}}{s_{11}+s_{12}}.
\end{aligned} \qquad (B8)
$$

The values of the coefficients $C_{33}^{\oplus}$ and $C_{13}^{\oplus}$ are $3.73 \times 10^{8}$ and $3.01 \times 10^{7} \mathrm{~m}^{5} \mathrm{~V} / \mathrm{C}^{3}$, respectively for PbTiO$_3$. The difference between the free energy densities for stripe domain and monodomain films, i.e., Eqs. (B6) and (A7) with $P_2$=0, is given by
$$
\begin{aligned}
\Delta A= & C_{33}^{\oplus}\left(P_{3}^{2}-P^{\dagger 2}\right)^{2}+C_{13}^{\oplus} P_{1}^{2}\left(P_{3}^{2}-P^{\dagger 2}\right) \\
& +\left(Q_{44}^{2} / 2 s_{44}\right) P_{1}^{2} P_{3}^{2}.
\end{aligned} \qquad (B9)
$$

The value of $P^\dagger$ is a parameter (like the stripe period) to be varied to minimize the total free energy. Since it enters the free energy density only through the first two terms in Eq. (B9), the value which minimizes the integrated free energy can be obtained analytically for any polarization distribution by setting the derivative with respect to $P^\dagger$ to zero. This gives
$$
P^{\dagger 2}=\left\langle P_{3}^{2}+\frac{C_{13}^{\oplus}}{2 C_{33}^{\oplus}} P_{1}^{2}\right\rangle, \qquad (B10)
$$
where the angle brackets represent the average over the film volume. The factor in front of $P_1^2$ has a value of only 0.04 for PbTiO$_3$, so the optimum value of $P^\dagger$ is approximately equal to the root-mean-square average of $P_3$. For thick films well below $T_C$, it should approach $P_0^*$ of Eq. (A12) to give zero stress $X_3$ in the interior of the film where $\mathbf{P}=(0,0,P_0^*)$. Near $T_C$ it should approach zero, and be zero above $T_C$. When $P^\dagger$ is zero, the values of $A_0^{\oplus}$, $\alpha_1^{\oplus}$, and $\alpha_3^{\oplus}$ reduce to $A_0^*$, $\alpha_1^*$, and $\alpha_3^*$. Calculated values of $A_0^{\oplus}$, $\alpha_1^{\oplus}$, and $\alpha_3^{\oplus}$ as a function of temperature, using the extreme value $P^\dagger$=$P_0^*$, are shown in Fig. 13. Values of the temperature- and $P^\dagger$-independent coefficients $\alpha_{33}^{\oplus}$ and $\alpha_{13}^{\oplus}$ are listed in Table III.

The primary effect of the elastic solution for stripe domains is illustrated in Fig. 14, which compares the $P_3$ dependence of the free energy density functions of Eqs. (B6) and (A7) at $P_1$=$P_2$=$E$=0. In this case the difference between the free energies for stripe domain and monodomain films is given by the first term in Eq. (B9), which is a double-well quartic function with minima at $P_3=\pm P^\dagger$. For thick films well below $T_C$, where $P^\dagger$=$P_0^*$, both functions have the same positions of the minima at $P_3$=$P_0^*$, and values of the equilibrium free energy density $A(P_0^*)$. However, the elastic solution for stripe domains gives a narrower energy well width, significantly decreasing the dielectric constant $\epsilon_3$ in the polar phase.

The assumption of fixed $x_3$ allows the elastic energy to be included by simply renormalizing polarization coefficients in the free energy density expansion. It leads to non-zero stresses $X_3$ and $X_5$ at the interfaces of the thin film, which would match the stress boundary conditions only for an infinitely stiff external medium. To properly account for the reduction in stress near, e.g., a vacuum interface will require treating the displacement as an independently variable field in the free energy minimization, which is beyond the scope of this work. In principle the fixed $x_3$ solution overestimates the free energy of the stripe domain phase, which gives an overestimate of the suppression of $T_C$.

## APPENDIX C: POLARIZATION GRADIENT TERMS

Polarization gradient terms can be included in the free energy density expansions to model the effects of domain walls and interfaces. For stripe domains in thin films, complex polarization gradients can occur near the domain walls and interfaces. Thus it is relevant to understand all of the gradient terms that could contribute.

For terms in the free energy density, we are interested in the lowest order scalar quantities that are invariant under cubic symmetry operations. These are sums of second-order terms of the form $\nabla_i P_j \nabla_k P_l$. In general there are four such invariants. These have been previously expressed as$^{25}$
$$
\begin{aligned}
\Delta A_{\mathrm{grad}}- & \frac{G_{11}}{2} \sum_{i}\left(\nabla_{i} P_{i}\right)^{2}+\sum_{i, j>i}\left[G_{12} \nabla_{i} P_{i} \nabla_{j} P_{j}+\frac{G_{44}}{2}\left(\nabla_{i} P_{i}\right.\right. \\
& \left.\left.+\nabla_{j} P_{i}\right)^{2}+\frac{G_{44}^{\prime}}{2}\left(\nabla_{i} P_{j}-\nabla_{j} P_{i}\right)^{2}\right].
\end{aligned} \qquad (C1)
$$

Here we will write the four gradient contributions to the free energy density in a manner that reflects the possible material symmetries,
$$
\begin{aligned}
\Delta A_{\mathrm{grad}}= & \frac{1}{2} \kappa_{11}(\boldsymbol{\nabla} \cdot \mathbf{P})^{2}+\frac{1}{2} \kappa_{\perp}|\boldsymbol{\nabla} × \mathbf{P}|^{2} \\
& +\left(\kappa_{12}-\kappa_{11}\right) \operatorname{tr}[\operatorname{cof}(\boldsymbol{\nabla} \mathbf{P})] \\
& +\left(2 \kappa_{44}+\kappa_{12}-\kappa_{11}\right) \sum_{i, j>i} \nabla_{i} P_{j} \nabla_{j} P_{i},
\end{aligned} \qquad (C2)
$$
where the coefficients of the third and fourth terms are given in a form analogous to the stress coefficients in Eq. (A1). The correspondences between the coefficients in Eqs. (C2) and (C1) are $\kappa_{11}$=$G_{11}$, $\kappa_{12}$=$G_{12}$, $\kappa_{44}$=$G_{44}$, and $\kappa_{\perp}$=$G_{44}$

$+G_{44}'$. The first three terms in Eq. (C2) are isotropically invariant, and can be written out as

$$
(\boldsymbol{\nabla} \cdot \mathbf{P})^{2}=\left(\operatorname{tr}[\boldsymbol{\nabla} \mathbf{P}]\right)^{2}=\left(\sum_{i} \nabla_{i} P_{i}\right)^{2},
$$

$$
\begin{aligned}
& |\boldsymbol{\nabla} × \mathbf{P}|^{2}=\operatorname{tr}\left[\operatorname{cof}\left(\boldsymbol{\nabla} \mathbf{P}-(\boldsymbol{\nabla} \mathbf{P})^{T}\right)\right]=\sum_{i, j>i}\left(\nabla_{i} P_{j}-\nabla_{j} P_{i}\right)^{2}, \\
& \operatorname{tr}[\operatorname{cof}(\boldsymbol{\nabla} \mathbf{P})]=\sum_{i, j>i}\left(\nabla_{i} P_{i} \nabla_{j} P_{j}-\nabla_{i} P_{j} \nabla_{j} P_{i}\right),
\end{aligned}
$$

where $\operatorname{tr}[\boldsymbol{\nabla} \mathbf{P}],(\boldsymbol{\nabla} \mathbf{P})^{T}$, and $\operatorname{cof}(\boldsymbol{\nabla} \mathbf{P})$ represent the trace, transpose, and cofactor $^{40}$ operators, respectively. The second term is zero if $\boldsymbol{\nabla} \mathbf{P}$ is symmetric, so that this type of term does not occur in expansions of symmetric tensors (such as stress). This term was not included in a previous treatment of polarization gradient terms. $^{41}$ The coefficient of the fourth term would be zero in an isotropic system, but can be nonzero in a cubic system.

Since the values of the coefficients are not known, we have chosen to keep only a single gradient term in the free energy density. The only gradient term which is nonzero for an isolated, infinite (100)-oriented $180^{\circ}$ domain wall is $|\boldsymbol{\nabla} × \mathbf{P}|^{2}$. Thus we keep only this term in the free energy used to model $180^{\circ}$ stripe domains.

## APPENDIX D: FREE ENERGY OF A $180^{\circ}$ DOMAIN WALL IN AN EPITAXIAL FILM

Here we solve for the equilibrium polarization distribution and excess free energy of a $180^{\circ}$ domain wall in an epitaxial film. We consider a (100) oriented domain wall at $r_{1}=0$. The film is polarized normal to its interfaces (the $r_{3}$ direction), with boundary conditions $\mathbf{P}=\left(0,0, \pm P_{0}^{*}\right)$ at $r_{1}$ $\rightarrow \pm \infty$. We wish to consider situations with $\mathbf{E}=0$, e.g., with depolarizing field compensated by free charge at film interfaces. To satisfy $\boldsymbol{\nabla} \cdot \mathbf{D}=0$, this requires the polarization component normal to the boundary to be zero throughout the system $\left(P_{1}=0\right)$. The problem consists in determining the variation of $P_{2}, P_{3}$, and $\mathbf{X}$ in the vicinity of the domain wall at equilibrium. Consistent with the treatment of stripe domains in Appendix B we consider an elastic solution with fixed $x_{3}$.

For a thick epitaxial film $(t \rightarrow \infty)$ with gradients only in the $r_{1}$ direction, strain compatibility requires $x_{2}, x_{3}$, and $x_{4}$ to be constant. The values of $x_{1}, x_{2}$, and $x_{6}$ are fixed by the substrate, and we assume them to be uniform in the film. We use the constitutive relations (A3) for a uniform system, neglecting any polarization-dependent displacement across the domain wall. The components $x_{5}$ and $X_{5}$ are free to be zero since they are not coupled to the polarization when $P_{1}=0$. The strains can then be written as

$$
\begin{aligned}
x_{1}= & x_{m}=s_{11} X_{1}+s_{12}\left(X_{2}+X_{3}\right)+Q_{12}\left(P_{2}^{2}+P_{3}^{2}\right), \\
x_{2}= & x_{m}=s_{11} X_{2}+s_{12}\left(X_{1}+X_{3}\right)+Q_{11} P_{2}^{2}+Q_{12} P_{3}^{2}, \\
x_{3}= & Q_{11} P_{0}^{* 2}+2 s_{12}\left(x_{m}-Q_{12} P_{0}^{* 2}\right) /\left(s_{11}+s_{12}\right) \\
= & s_{11} X_{3}+s_{12}\left(X_{1}+X_{2}\right)+Q_{11} P_{3}^{2}+Q_{12} P_{2}^{2}, \\
x_{4}=0 & =s_{44} X_{4}+Q_{44} P_{2} P_{3}, \\
x_{5}= & x_{6}=0,
\end{aligned}
$$

where $P_{0}^{*}$ is given by Eq. (A12). One can solve these equations to obtain the nonzero stress components in terms of the polarization, giving

$$
\begin{aligned}
& X_{1}=C_{12} P_{2}^{2}+C_{12}\left(P_{3}^{2}-P_{0}^{* 2}\right)+X_{m}, \\
& X_{2}=C_{11} P_{2}^{2}+C_{12}\left(P_{3}^{2}-P_{0}^{* 2}\right)+X_{m}, \\
& X_{3}=C_{12} P_{2}^{2}+C_{11}\left(P_{3}^{2}-P_{0}^{* 2}\right), \\
& X_{4}=-\left(Q_{44} / s_{44}\right) P_{2} P_{3},
\end{aligned}
$$

where the coefficients are the same as those in Eqs. (B4) and (B5), with $P^{\dagger}$ set to $P_{0}^{*}$ in $X_{m}$.

For gradients only in the $r_{1}$ direction and $P_{1}=0$, the only nonzero gradient energy terms in Eqs. (C2) and (C3)-(C4) are from $|\boldsymbol{\nabla} × \mathbf{P}|^{2}$. The appropriate free energy to minimize is $\mathcal{A}$. By substituting Eqs. (D2) into Eq. (A4), and adding the gradient term, one obtains

$$
\begin{aligned}
A= & A_{0}^{\oplus}+\alpha_{1}^{\oplus} P_{2}^{2}+\alpha_{3}^{\oplus} P_{3}^{2}+\alpha_{33}^{\oplus}\left(P_{2}^{4}+P_{3}^{4}\right)+\alpha_{13}^{\oplus} P_{2}^{2} P_{3}^{2} \\
& +\alpha_{111}\left(P_{2}^{6}+P_{3}^{6}\right)+\alpha_{112}\left(P_{2}^{4} P_{3}^{2}+P_{3}^{4} P_{2}^{2}\right) \\
& +\frac{1}{2} \kappa_{\perp}\left[\left(\nabla_{1} P_{2}\right)^{2}+\left(\nabla_{1} P_{3}\right)^{2}\right],
\end{aligned}
$$

where the renormalized coefficients are the same as in Eqs. (B6) and (B7), with $P^{\dagger}$ set to $P_{0}^{*}$.

The free energy functional $\mathcal{A}$ can be minimized using standard variational calculus techniques. $^{42}$ Setting the variational derivatives of $\mathcal{A}$ with respect to $P_{2}$ and $P_{3}$ to zero gives two Euler equations,

$$
\begin{aligned}
\kappa_{\perp} \nabla_{1}^{2} P_{2}= & 2 \alpha_{1}^{\oplus} P_{2}+4 \alpha_{33}^{\oplus} P_{2}^{3}+2 \alpha_{13}^{\oplus} P_{2} P_{3}^{2}+6 \alpha_{111} P_{2}^{5} \\
& +2 \alpha_{112}\left(P_{2} P_{3}^{4}+2 P_{2}^{3} P_{3}^{2}\right), \\
\kappa_{\perp} \nabla_{1}^{2} P_{3}= & 2 \alpha_{3}^{\oplus} P_{3}+4 \alpha_{33}^{\oplus} P_{3}^{3}+2 \alpha_{13}^{\oplus} P_{2}^{2} P_{3}^{2}+6 \alpha_{111} P_{3}^{5} \\
& +2 \alpha_{112}\left(P_{2}^{4} P_{3}+2 P_{2}^{2} P_{3}^{3}\right) .
\end{aligned}
$$

Bulaevskii $^{43}$ and Huang $e t a l .{ }^{44}$ have considered the solutions to these equations. In general, there are two types of solutions: (1) an "Ising" domain wall, in which $P_{2}=0$ and the magnitude of $\mathbf{P}$ goes to zero in the center of the wall, and (2) a "Bloch" domain wall, in which $\left|P_{2}\right|$ is maximum at the wall center and the direction of $\mathbf{P}$ rotates from positive to negative $r_{3}$ in the wall. Bulaevskii gives criteria for the existence of these solutions, and for which has the lowest free energy, in terms of several dimensionless parameters. In our notation, these parameters are given by

![](./images/812056467958923265_17.jpg)

FIG. 15. Parameters describing the Ising vs Bloch nature of (100) $180^{\circ}$ domain walls in coherently strained $PbTiO_{3}$ on $SrTiO_{3}$.

$$
\begin{aligned}
& a=-\alpha_{1}^{\oplus} / \alpha_{3}^{\oplus}, \\
& b_{2}=-2 \alpha_{33}^{\oplus} P_{0}^{* 2} / \alpha_{3}^{\oplus}, \\
& c_{2}=-3 \alpha_{111} P_{0}^{* 4} / \alpha_{3}^{\oplus}, \\
& \delta^{2}=\frac{2\left(\alpha_{1}^{\oplus}+\alpha_{13}^{\oplus} P_{0}^{* 2}+\alpha_{112} P_{0}^{* 4}\right)}{3 \alpha_{111} P_{0}^{* 4}-\alpha_{3}^{\oplus}}.
\end{aligned} \quad \text { (D5) }
$$

The Ising solution exists for all values of the parameters. If $a$ and $b_{2}$ are both positive, or $a$ is positive and $b_{2}^{2}-4 a c_{2}$ is negative, then only the Ising solution exists; otherwise, a Bloch solution also exists. If it exists, the Bloch solution has the lowest free energy only if $\delta^{2}$ is smaller than unity. Values of $\delta^{2}, a$, and $b_{2}$ are shown as a function of temperature for epitaxially strained $PbTiO_{3}$ on $SrTiO_{3}$ in Fig. 15. Although $a$ becomes negative at lower $T$, so that a Bloch solution exists, $\delta^{2}$ remains larger than unity, indicating that the Ising solution is the equilibrium domain wall structure at all temperatures.

For the Ising solution, $P_{2}$ is zero, and the remaining Euler equation reads
$$
\kappa_{\perp} \nabla_{\perp}^{2} P_{3}=2 \alpha_{3}^{\oplus} P_{3}+4 \alpha_{33}^{\oplus} P_{3}^{3}+6 \alpha_{111} P_{3}^{5}. \quad \text { (D6) }
$$

The solution to this equation is given by several authors $^{41,43,45}$ as
$$
P_{3}=P_{0}^{*} \frac{\sinh \left(r_{\perp} / \xi_{\perp}\right)}{\left[\Delta+\cosh ^{2}\left(r_{\perp} / \xi_{\perp}\right)\right]^{1 / 2}}, \quad \text { (D7) }
$$
where the domain wall shape parameter $\Delta$ and width $\xi_{\perp}$ are given by
$$
\Delta=\left[2+\alpha_{33}^{\oplus} /\left(\alpha_{111} P_{0}^{* 2}\right)\right]^{-1}, \quad \text { (D8) }
$$

$$
\xi_{\perp}=\left[\frac{\kappa_{\perp}(1-2 \Delta)}{2 \alpha_{33}^{\oplus} P_{0}^{* 2}(1+\Delta)}\right]^{1 / 2}. \quad \text { (D9) }
$$

(There are errors in the expressions for $P_{3}$ and $\xi$ given in Ref. 44.) The excess free energy of the domain wall is given by $^{43}$
$$
\gamma=(4 / 3)\left(2 \kappa_{\perp} \alpha_{33}^{\oplus}\right)^{1 / 2} P_{0}^{* 3}\left(\frac{1+\Delta}{1-2 \Delta}\right)^{1 / 2}(1+\Delta)^{2} \mathcal{I}(\Delta),
$$

where the function $\mathcal{I}(\Delta)$ is the hypergeometric integral

![](./images/812056467958923265_18.jpg)

FIG. 16. Width, shape parameter, and free energy of (100) $180^{\circ}$ domain walls in coherently strained $PbTiO_{3}$ on $SrTiO_{3}$.

$$
\mathcal{I}(\Delta) \equiv \frac{3}{4} \int_{-\infty}^{+\infty} \frac{\cosh ^{2}(t) d t}{\left[\Delta+\cosh ^{2}(t)\right]^{3}}, \quad \text { (D11) }
$$
which is equal to unity for $\Delta=0$. For second-order phase transitions, the sixth-order terms $\alpha_{111}$ and $\alpha_{112}$ are often neglected in free energy expansions such as Eq. (D3); this corresponds to $\Delta=0$. The equations above then reduce to oftencited results, $^{46}$ e.g., $P_{3}=P_{0}^{*} \tanh \left(r_{\perp} / \xi_{\perp}\right)$. (Other authors $^{41,45}$ give expressions for $\gamma$ which do not appear to be correct, e.g., they diverge at $\Delta=0$.) Values of the $180^{\circ}$ domain wall width, shape parameter, and energy for coherently strained $PbTiO_{3}$ on $SrTiO_{3}$ are given as a function of temperature in Fig. 16. As in the main text, the value of the gradient energy coefficient used was $\kappa_{\perp}=7.8 \times 10^{-11} \mathrm{~V} \mathrm{~m}^{3} / \mathrm{C}$.

The resulting $180^{\circ}$ domain wall energies can be compared with the value of $0.13 \mathrm{~J} / \mathrm{m}^{2}$ calculated for unstressed $PbTiO_{3}$ at $0 \mathrm{~K}$ using $a b$ initio techniques. $^{47}$ It would be interesting to have $a b$ initio calculations of the domain wall energies in epitaxially strained films of $PbTiO_{3}$ on $SrTiO_{3}$ for direct comparison with these results.

The result that Ising rather than Bloch walls are the equilibrium structure for planar (100) $180^{\circ}$ domain walls in $PbTiO_{3}$ supports the assumption $P_{2}=0$ in the stripe domain solutions obtained above. More complex solutions to the Euler equation (D6) also exist, $^{48}$ including periodic solutions with multiple walls that may be relevant for stripe domains.

$^{1}$ B. A. Strukov and A. P. Levanyuk, *Ferroelectric Phenomena in Crystals* (Springer, Berlin, 1998).
$^{2}$ P. Wurfel and I. P. Batra, *Ferroelectrics* **12**, 55 (1976); I. P. Batra, P. Wurfel, and B. D. Silverman, J. Vac. Sci. Technol. **10**, 687 (1973).
$^{3}$ N. Sai, A. M. Kolpak, and A. M. Rappe, Phys. Rev. B **72**, 020101(R) (2005).
$^{4}$ J. Junquera and P. Ghosez, *Nature* (London) **422**, 506 (2003).

$^{5}$M. Dawber, P. Chandra, P. B. Littlewood, and J. F. Scott, J. Phys.: Con- dens. Matter **15**, L393 (2003).

$^{6}$Y. Watanabe, M. Okano, and A. Masuda, Phys. Rev. Lett. **86**, 332 (2001).

$^{7}$L. Landau and E. Lifshitz, Phys. Z. Sowjetunion **8**, 153 (1935); *Collected Works of L.D. Landau*, edited by D. ter Haar (Gordon and Breach, New York, 1965), p. 101.

$^{8}$C. Kittel, Phys. Rev. **70**, 965 (1946).

$^{9}$T. Mitsui and J. Furuichi, Phys. Rev. **90**, 193 (1953).

$^{10}$Y. Cho, S. Kazuta, and K. Matsuura, Jpn. J. Appl. Phys., Part 1 **38**, 5689 (1999).

$^{11}$S. K. Streiffer *et al.*, Phys. Rev. Lett. **89**, 067601 (2002).

$^{12}$D. D. Fong, G. B. Stephenson, S. K. Streiffer, J. A. Eastman, O. Auciello, P. H. Fuoss, and C. Thompson, Science **304**, 1650 (2004).

$^{13}$A. Kopal, P. Mokry, J. Fousek, and T. Bahnik, Ferroelectrics **223**, 127 (1999).

$^{14}$A. M. Bratkovsky and A. P. Levanyuk, Phys. Rev. Lett. **84**, 3177 (2000); Phys. Rev. B **63**, 132103 (2001).

$^{15}$J. L. Bjorkstam and R. E. Oettel, Phys. Rev. **159**, 427 (1967).

$^{16}$A. Kopal, T. Bahnik, and J. Fousek, Ferroelectrics **202**, 267 (1997).

$^{17}$E. V. Chenskii, Sov. Phys. Solid State **14**, 1940 (1973).

$^{18}$Y. G. Wang, W. L. Zhong, and P. L. Zhang, Phys. Rev. B **51**, 5311 (1995).

$^{19}$S. Tinte and M. G. Stachiotti, Phys. Rev. B **64**, 235403 (2001).

$^{20}$M. G. Stachiotti, Appl. Phys. Lett. **84**, 251 (2004).

$^{21}$Z. Wu, N. Huang, Z. Liu, J. Wu, W. Duan, B.-L. Gu, and X.-W. Zhang, Phys. Rev. B **70**, 104108 (2004).

$^{22}$I. I. Naumov, L. Bellaiche, and H. Fu, Nature (London) **432**, 737 (2004).

$^{23}$I. Kornev, H. Fu, and L. Bellaiche, Phys. Rev. Lett. **93**, 196104 (2004).

$^{24}$Z. Wu, N. Huang, J. Wu, W. Duan, and B.-L. Gu, Appl. Phys. Lett. **86**, 202903 (2005).

$^{25}$Y. L. Li, S. Y. Hu, Z. K. Liu, and L. Q. Chen, Appl. Phys. Lett. **81**, 427 (2002); Acta Mater. **50**, 395 (2002).

$^{26}$M. J. Haun, E. Furman, S. J. Jang, H. A. McKinstry, and L. E. Cross, J. Appl. Phys. **62**, 3331 (1987).

$^{27}$M. J. Haun, Z. Q. Zhuang, E. Furman, S. J. Jang, and L. E. Cross, Ferro- electrics **99**, 45 (1989).

$^{28}$G. A. Rossetti, Jr., K. R. Udayakumar, M. J. Huan, and L. E. Cross, J. Am. Ceram. Soc. **73**, 3334 (1990).

$^{29}$G. A. Rossetti, Jr., J. P. Cline, and A. Navrotsky, J. Mater. Res. **13**, 3197 (1998).

$^{30}$N. A. Pertsev, A. G. Zembilgotov, and A. K. Tagantsev, Phys. Rev. Lett. **80**, 1988 (1998).

$^{31}$J. R. Reitz and F. J. Milford, *Foundations of Electromagnetic Theory* (Addison-Wesley, Reading, MA, 1960).

$^{32}$F. Jona and G. Shirane, *Ferroelectric Crystals* (Macmillan, New York, 1962).

$^{33}$N. A. Pertsev, A. K. Tagantsev, and N. Setter, Phys. Rev. B **61**, R825 (2000).

$^{34}$R. Kretschmer and K. Binder, Phys. Rev. B **20**, 1065 (1979).

$^{35}$M. D. Glinchuk, E. A. Eliseev, and V. A. Stephanovich, Physica B **322**, 356 (2002).

$^{36}$J. F. Nye, *Physical Properties of Crystals* (Oxford, London, 1957).

$^{37}$L. D. Landau, E. M. Lifshitz, and L. P. Pitaevskii, *Electrodynamics of Continuous Media*, 2nd ed. (Butterworth-Heinemann, Oxford, 1995), Sec. 19. Note that the first edition of this text gave different results.

$^{38}$*Thermophysical Properties of Matter*, edited by Y. S. Touloukian (Plenum, New York, 1977), Vol. 13. p. 670.

$^{39}$A. E. H. Love, *A Treatise on the Mathematical Theory of Elasticity*, 4th ed. (Dover, New York, 1944), p. 49.

$^{40}$T. M. Apostol, *Calculus*, 2nd ed. (Xerox College Publishing, Waltham, MA, 1969), Vol. II, p. 92.

$^{41}$W. Cao and L. E. Cross, Phys. Rev. B **44**, 5 (1991).

$^{42}$G. Arfken, *Mathematical Methods for Physicists* (Academic, New York, 1970).

$^{43}$L. N. Bulaevskii, Sov. Phys. Solid State **5**, 2329 (1964).

$^{44}$X. R. Huang, X. B. Hu, S. S. Jiang, and D. Feng, Phys. Rev. B **55**, 5534 (1997).

$^{45}$I. I. Ivanchik, Sov. Phys. Solid State **3**, 2705 (1962).

$^{46}$M. E. Lines and A. M. Glass, *Principles and Applications of Ferroelec- trics and Related Materials* (Clarendon, Oxford, 1977).

$^{47}$B. Neyer and D. Vanderbilt, Phys. Rev. B **65**, 104111 (2002).

$^{48}$F. Falk, Z. Phys. B: Condens. Matter **51**, 177 (1983).