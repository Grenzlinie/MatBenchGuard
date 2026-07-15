# Solution to the Boltzmann equation for a model polyvalent metal and resistivity calculations*

E. Gorham-Bergeron $^{\dagger}$ and Lowell Dworin
Northeastern University, Boston, Massachusetts 02115
(Received 8 August 1974)

An approximate solution to the coupled electron and phonon Boltzmann equations for an idealized model of Al, In, and other metals whose Fermi surface intersects the Brillouin-zone boundary has been found. Using an expansion in Legendre polynomials for the nonequilibrium distribution function and a spherical Fermi surface, the umklapp part of the scattering term is expanded in powers of $T/\Theta_D$ (where $\Theta_D$ is the Debye temperature). The solution to this equation is found which exhibits an unusual reduction in the nonequilibrium distribution function at the region of intersection of the Fermi surface with the zone boundary, as first anticipated by Klemens and Jackson. The resistivity calculated using this distribution function shows good agreement with experimental results for Al except in the very-low-temperature low-impurity region. A subsequent modification to the solution which attempts to roughly approximate the distortion of the Fermi surface near the Brillouin-zone boundary results in good agreement with experimental results even in this region.

## I. INTRODUCTION

This paper is concerned with the calculation of the static electrical resistivity in a bulk polyvalent metal in which electrons are scattered by both impurities and phonons. "Idealized" aluminum is used as an example, although the method can be used for other materials as well. The most straightforward procedure for such a calculation, and the one which we shall employ, is to seek a solution to the coupled linearized electron and phonon Boltzmann equations in which the scattering term is just the sum of a term representing electron-impurity scattering and a term representing electron-phonon scattering.

Until now, exact solutions to the Boltzmann equation in which umklapp processes have been included in the electron-phonon scattering term have not been found, because the scattering terms are unwieldy. The most prevalent method of finding approximate solutions to the Boltzmann equation is to use the variational principle, which defines the "best" solution to the Boltzmann equation as the one which minimizes a variational integral expression for the resistivity. $^{1}$ Since the solution to the isotropic Boltzmann equation is just the first Legendre polynomial whose argument is the angle between the electronic wave vector and the electric field, the most common trial form for the deviation distribution function including umklapp is just a sum of the first few Legendre polynomials in which the coefficients are varied to minimize the resistivity. $^{2,3}$ Because the variational calculation must be done numerically for each value of temperature and impurity concentration of interest, it is a cumbersome process. This is especially so for a distribution function which is not a smooth function, as we find to be the case with our (idealized) model of Al, where very large numbers of polynomials would have to be included in the calculation before any satisfactory results can be obtained.

Other attempts which have been made to calculate the low-temperature resistivity of metals whose Fermi surface crosses the Brillouin-zone boundary assume that at low temperatures the scattering processes described by normal electron-phonon scattering processes can be represented as diffusion processes on the Fermi surface. $^{4-6}$ The electron-impurity scattering processes are included with an isotropic-relaxation-time approximation. In the calculations using this method, umklapp processes, which involve large scattering angles but occur on only a small portion of the Fermi surface, are dealt with by noting that, since for low impurity concentrations they are much stronger than normal or impurity scattering processes, their effect can be represented by imposing a boundary condition that the distribution function be zero at the Brillouin-zone boundary.

Calculations based on this diffusion model have yielded results which indicate a breakdown in Matthiessen's rule. $^{6}$ However, there are difficulties in applying the technique to the problem at hand, where the distribution function is expected to vary rapidly in a small region near the zone boundary. This rapid variation precludes the use of the diffusion equation, since the step size of the diffusion process, although small on the scale of the total Fermi surface, is comparable to the region over which the distribution function is varying most rapidly. In addition, our results will show that only for very low impurity concentrations is the distribution function actually close to zero at the Bril-

---
11

louin-zone boundary, so that the proper impurity dependence of the distribution function cannot be expected with this approach.

For this reason both the variational technique, using expansions in Legendre polynomials, and the diffusion-equation approach have been only partial- ly successful in predicting the observed deviations from Matthiessen's rule in aluminum.

We have found an approximate solution to the coupled electron and phonon Boltzmann equations for metals whose Fermi surface crosses the Bril- louin-zone boundary, which probably could not have been obtained with any method other than by seek- ing a direct solution. The approximations used in obtaining such a solution are (a) the assumption that $T \ll \Theta_{D}$, (b) the assumption of a spherical Fermi surface, (c) the inclusion of only two Bril- louin-zone boundaries cutting the Fermi surface at $\pm \frac{1}{2} \overrightarrow{\mathrm{G}}$, and (d) the assumption that $\rho_{0}$, the impurity (zero-temperature) resistance, be greater than some minimum value $\rho_{\min }$ which at low temperatures is an increasing function of temperature and which is always less than $10^{-9} \Omega \mathrm{cm}$.

The results of our calculation cause us to con- clude that the anisotropic umklapp scattering pro- cesses in such materials as aluminum represent the major contribution to the temperature-depen- dent part of the resistivity for low temperatures. Considerations of the deviations of the Fermi sur- face from sphericity are only necessary in the temperature range $0-20^{\circ} \mathrm{K}$ and only rough approxi mations to take into account nonsphericity are necessary to predict the observed $T^{3}$ temperature dependence for the range from 5 to $20^{\circ} \mathrm{K}$. Only for temperatures less than $5^{\circ} \mathrm{K}$ do we conclude that precise two-orthogonalized-plane-wave (2-OPW) calculations are necessary. In the temperature range from 10 to $300^{\circ} \mathrm{K}$ our calculated values of the resistivity agree remarkably well with observed measurements of the temperature-dependent part of the resistivity $[\rho(T)]$ and the deviations from Matthiessen's rule. Our results have not been able to reproduce the exact shape of the $\rho(T)-\mathrm{vs}-\rho_{0}$ curve (our curve varies as $\ln \rho_{0}$ over only three decades on the scale, whereas the observed range is at least five decades; this difficulty is common to all calculations to date) but we suggest further corrections which we expect to reproduce the ob- served $\rho_{0}$ dependence.

This paper is divided into six sections. In Sec. II the details of the model are introduced and the basic equations written down. Section III contains the details of the main calculation, the process of obtaining an approximate analytic solution to the Boltzmann equation, and the calculation of the electrical resistivity. In Sec. IV we introduce a modification to the solution found in Sec. III whose purpose is to include the actual Fermi surface of aluminum in the calculation. In Secs. V and VI we compare our results to those obtained using the variational principle and to experimental results, respectively, and suggest further refinements to this calculation which may lead to even better agreement with experimental results.

## II. BASIC EQUATIONS

Our model is that of a system of electrons inter- acting with both phonons and impurities in a uni- form static electric field. A pseudopotential for the electron-phonon interaction is used which in- cludes, in addition to the bare-ion potential, the potential due to core electrons, which are as- sumed to move rigidly with the ion, and the screening effects due to other conduction elec- trons. For the metals under consideration a sin- gle-plane-wave approximation can be used as a pseudo-wave-function away from the zone bounda- ries, but two plane waves must be used near the zone boundaries. $^{7}$ Initially this calculation uses a single-plane-wave approximation everywhere on the Fermi surface, and a subsequent modification discussed in Sec. IV simply eliminates the con- tribution to the resistivity from scattering proces- ses occurring in areas of the Fermi surface close to the Brillouin-zone boundaries, where it is nec- essary to use two OPW pseudo-wave-functions.
This may seem a severe modification, but an ob- jective of this paper is to show that, except in the temperature range from 0 to $5^{\circ} \mathrm{K}$, practically the total contribution to the resistivity comes from parts of the Fermi surface where there is little distortion and a single plane wave is adequate.
The fact that the phonons are displaced from their equilibrium distribution through their interactions with the electrons is included (phonon drag) and the effect is seen to be not very significant. Interac- tions between phonons and impurities are ignored, and the interaction of the electrons with impurities is expressed in terms of a simple relaxation time given by $\tau_{i}$.

Since we have assumed a uniform static electric field it is reasonable to require that both phonon and electron distributions be independent of time. While it is somewhat artificial to neglect phonon- impurity interactions, it is nevertheless a worth- while endeavor to investigate a system without these interactions to clarify the importance of phonon-drag effects on the resistivity. Phonon- impurity interactions would tend to bring the pho- non distribution toward equilibrium, so our model can be expected to exhibit larger phonon-drag ef- fects than would be seen in a real system and thus to set an "upper bound" on these effects.

For calculational simplicity only two Brillouin-
zone boundaries are considered to intersect the
Fermi surface; the corresponding reciprocal-lat-
tice vectors are $\pm \vec{G}$.

The electron and phonon distribution functions
are given by
$$
f_{\vec{k}}=f_{\vec{k}}^{0}+\frac{\partial f_{\vec{k}}^{0}}{\partial E_{\vec{k}}} \varphi_{\vec{k}}
$$
and
$$
N_{\vec{q}, s}=N_{\vec{q}, s}^{0}+\frac{\partial N_{\vec{q}, s}^{0}}{\partial E_{\vec{q}}} \eta_{\vec{q}, s},
$$
respectively, where $f_{\vec{k}}^{0}$ is the Fermi distribution
function for an electron of wave vector $\vec{k}$ and $N_{\vec{q}, s}^{0}$
the Bose distribution function for a phonon of wave
vector $\vec{q}$, and $\varphi_{\vec{k}}$ and $\eta_{\vec{q}, s}^{0}$ are considered to be
small. If $T \ll E_{F} / K_{B} \sim 10^{3}{ }^{\circ} \mathrm{K}$, where $T$ is the tem-
perature, $E_{F}$ is the Fermi energy, and $K_{B}$ the
Boltzmann constant, then to a good approximation
we may set
$$
\frac{\partial f_{\vec{k}}^{0}}{\partial E_{\vec{k}}}=-\delta\left(E_{F}-E_{\vec{k}}\right),
$$
where $E_{\vec{k}}$ is the energy of an electron of wave vec-
tor $\vec{k}$. In this case scattering processes take place
entirely on the Fermi surface. The linearized
Boltzmann equation for an electron in a constant
electric field is given, under the condition noted
above, by $^{8}$

$$
\begin{aligned}
-e \overrightarrow{\mathrm{E}} \cdot v_{\vec{k}} \delta\left(E_{\vec{k}}-E_{F}\right)= & -\frac{1}{\tau_{i}} \varphi_{\vec{k}} \delta\left(E_{\vec{k}}-E_{F}\right)+\sum_{\vec{q}} \sum_{s} \sum_{\vec{G}}\left|v_{s}(\vec{q}-\vec{G})\right|^{2} \delta\left(E_{\vec{k}}-E_{F}\right) \beta \hbar \omega_{\vec{q}, s} N_{\vec{q}, s}^{0}\left(N_{\vec{q}, s}^{0}+1\right) \\
& \left.\times\left[\delta\left(E_{\vec{k}-\vec{q}+\vec{G}}-E_{\vec{k}}+\omega_{\vec{q}, s} \hbar\right)\left(\varphi_{\vec{k}-\vec{q}+\vec{G}}-\varphi_{\vec{k}}+\eta_{\vec{q}, s}\right)+\delta\left(E_{\vec{k}}-E_{\vec{k}+\vec{q}-\vec{G}}+\omega_{\vec{q}, s} \hbar\right)\left(\varphi_{\vec{k}+\vec{q}-\vec{G}}-\varphi_{\vec{k}}-\eta_{\vec{q}, s}\right)\right]\right]
\end{aligned}
$$
(1)

where $\tau_{i}$ is the relaxation time for the electron-
impurity interactions and $\beta=1 / T K_{B}$. The right-
hand side of Eq. (1), which represents the change
in the electron distribution due to scattering from
both phonons and impurities, is, in the first Born
approximation, the sum of two independent terms,
the first describing the scattering of electrons due
to impurities and the second describing the scat-
tering due to the electron-phonon interaction. A
corresponding equation for the rate of change of the
phonon distribution is, for the assumed steady
state and in the Born approximation,
$$
\begin{aligned}
0=\dot{N}_{\vec{q}, s}= & \sum_{\vec{k}} \sum_{\vec{G}}\left|v_{s}(\vec{q}-\vec{G})\right|^{2} N_{\vec{q}, s}^{0}\left(N_{\vec{q}, s}^{0}+1\right) \beta \hbar \omega_{\vec{q}, s} \\
& \times \delta\left(E_{\vec{k}}-E_{\vec{k}-\vec{q}+\vec{G}}-\hbar \omega_{\vec{q}, s}\right) \\
& \times\left(\varphi_{\vec{k}}-\varphi_{\vec{k}-\vec{q}+\vec{G}}-\eta_{\vec{q}, s}\right) \delta\left(E_{\vec{k}}-E_{F}\right).
\end{aligned}
$$

We have expressed the electron wave vector in the
extended zone scheme, and $\left|v_{s}(\vec{q}-\vec{G})\right|^{2}$, the scat-
tering matrix between two electrons in states $\vec{k}$ and
$\vec{k}^{\prime}$, is given by
$$
\frac{\pi}{d \hbar \omega_{\vec{q}, s}}\left|\left\langle\vec{k}^{\prime}\left|\frac{d \vec{V}}{d \vec{u}_{0}}\right| \vec{k}\right\rangle \cdot \vec{e}_{s}(\vec{q})\right|^{2} \delta_{\vec{k}-\vec{k}^{\prime}, \vec{q}-\vec{G}},
$$
where $\vec{e}_{s}(\vec{q})$ is the polarization of the phonon mode
$s$ with wave vector $\vec{q}, \vec{d}$ the density of the crystal,
$\omega_{\vec{q}, s}$ the energy of the phonon of wave vector $\vec{q}$ and
polarization $s$, and $V$ the pseudopotential. If $\vec{u}_{0}$ is
the displacment of the 0th ion from equilibrium,
and only 1-OPW pseudo-wave-functions are used
to describe the electrons, then $^{7}$
$$
\begin{aligned}
& \left|\left\langle\vec{k}^{\prime}\left|\frac{d \vec{V}}{d \vec{u}_{0}} \cdot \vec{e}_{s}(\vec{q})\right| k\right\rangle\right|^{2} \\
& =\left|\left(\vec{k}-\vec{k}^{\prime}\right) \cdot \vec{e}_{s}(\vec{q})\right|^{2} V^{2}\left(\vec{k}-\vec{k}^{\prime}\right).
\end{aligned}
$$

Here $V(\vec{k}-\vec{k}^{\prime})$ is the pseudopotential of Ashcroft $^{9}$
or Harrison. $^{10}$

Equation (2) can be used as an expression for
$\eta_{\vec{q}, s}$ and that variable eliminated from Eq. (1), so
that there is a single integral equation to be
solved. Hereafter, $\omega_{\vec{q}, s}$ in the energy $\delta$ functions
is neglected, since $\omega_{\vec{q}, s} \hbar \ll E_{\vec{k}}, E_{\vec{k}-\vec{q}+\vec{G}}$. In addi-
tion, $\varphi_{\vec{k}}$ is expanded in terms of Legendre poly-
nomials,
$$
\varphi_{\vec{k}}=\varphi(\hat{k} \cdot \hat{E})=\sum_{M} a_{M} P_{M}(\hat{k} \cdot \hat{E}),
$$
and we seek solutions of Eq. (1) for the $a_{M}$, thus
converting the integral equation to a matrix equa-
tion. The vector $\hat{k}$ is a unit vector in the direction
of $\vec{k}$, and $\hat{E}$ is a unit vector in the direction of $\overrightarrow{\mathrm{E}}$.
Only odd powers of $M$ need to be included in the
sum, since conservation of electrons requires that
$\varphi_{\vec{k}}$ be an odd function of $\hat{k} \cdot \hat{E}$.

If $\vec{k}, \vec{k}'$, and $\vec{q}$ are restricted to the first Brillouin zone, then a scattering process for which $\vec{k} - \vec{k}' \pm \vec{q}$ $=\pm \vec{G} \neq 0$ is normally considered an umklapp process. Here an in what is to follow it is considered more convenient to express $\vec{k}$ and $\vec{k}'$ in the extended-zone scheme, but still to classify as umklapp those processes for which $\vec{k} - \vec{k}' \pm \vec{q} = \pm \vec{G} \neq 0$. Only in a few cases does this classification of a process as either normal or umklapp differ from the normal method, and since all scattering processes must be summed irrespective of the terminology used to describe them, the physics is not altered.

$$
\eta_{\vec{\mathrm{q}}, s}^{+}=\sum_{n} a_{n} \int_{0}^{\infty} k^{2} d k \delta\left(k^{2}-k_{F}^{2}\right) \int_{-1}^{1} d(\hat{k} \cdot \hat{E}) \int_{0}^{2 \pi} d \varphi_{k E}
$$

$$
\times \frac{\delta\left(\vec{k}^{2}-(\vec{k}-\vec{q}+\vec{G})^{2}\right)\left\{P_{n}(\hat{k} \cdot \hat{E})-P_{n}(\hat{x} \cdot \hat{k}) P_{n}(\hat{k} \cdot \hat{E})-\sum_{m=1}^{n}[2(n-m)! /(n+m)!] P_{n}^{m}(\hat{x} \cdot \hat{k}) P_{n}^{m}(\hat{k} \cdot \hat{E}) \cos m\left(\varphi_{k E}-\varphi_{k-q+G, E}\right)\right\}}{\int_{0}^{\infty} k^{2} d k \delta\left(k^{2}-k_{F}^{2}\right) \int_{-1}^{1} d(\hat{k} \cdot \hat{E}) \delta\left(\vec{k}^{2}-(\vec{k}-\vec{q}+\vec{G})^{2}\right) \int_{0}^{2 \pi} d \varphi_{k E}}
$$

where $\hat{x}$ is the unit vector in the direction of $\vec{k} - \vec{q} + \vec{G}$, use has been made of the form $E_{\vec{k}}=\hbar^{2} k^{2} / 2 m^{*}, m^{*}$ is the effective mass, and it has been assumed that $\hbar \omega_{\vec{q}, s} \ll E_{\vec{k}}, E_{\vec{k}-\vec{q}+\vec{G}}$.

The final expression for $\eta_{\vec{q}, s}^{+}$is

$$
\begin{aligned}
\eta_{\vec{\mathrm{q}}, s}^{+}= & {\left[\sum_{G} \sum_{M} 2 a_{M} P_{M}\left(\frac{|\vec{q}-\vec{G}|}{2 k_{F}}\right) P_{M}(\hat{H} \cdot \hat{E}) \frac{\left|v_{s}(\vec{q}-\vec{G})\right|^{2}}{|\vec{q}-\vec{G}|} \Theta\left(1-\frac{|\vec{q}-\vec{G}|}{2 k_{F}}\right)\right] } \\
& \times\left[\sum_{G} \frac{\left|v_{s}(\vec{q}-\vec{G})\right|^{2}}{|\vec{q}-\vec{G}|} \Theta\left(1-\frac{|\vec{q}-\vec{G}|}{2 k_{F}}\right)\right]^{-1},
\end{aligned}
$$

where $H$ is the unit vector in the direction of $\vec{q} - \vec{G}$ and $\Theta(x)$ is the step function. In this exact form it is a complicated expression and we make our main approximation-keeping only lowest-order terms in the magnitude of $\vec{q}$, the phonon wave vector. Thus our equation becomes an expansion in temperature, since in the final integration over phonon states the powers of $\vec{q}$ determine the temperature dependence.

It is important to notice that in the following expansions in powers of $q / G$ or $q / 2 k_{F}$ we will avoid expansions of the Legendre polynomials in terms of their arguments whenever the argument is different from unity by an amount greater than $q^{2} / G^{2}$. This care is taken because we wish to include very large values of $M$ in our expression for $\varphi(\hat{k} \cdot \hat{E})$ in terms of the $P_{M}(\hat{k} \cdot \hat{E})$, for which such an expansion would not be valid. In the derivation of the diffusion equation from Eq. (1), expansions of the Legendre polynomials themselves are necessary, thus precluding the validity of the approach for nonsmooth distribution functions, such as those we consider here. In this respect our approach provides a substantial theoretical improvement over the diffusion-equation approach.

### III. CASE OF THE FERMI SURFACE OUTSIDE THE ZONE BOUNDARY

Without loss of generality Eq. (2) can be solved for $\eta_{\vec{q}, s}^{+}$. The expression for $\eta_{\vec{q}, s}^{+}$is further simplified using the expansion of $\varphi_{\vec{k}}$ in terms of a sum of Legendre polynomials. The sum over $\vec{k}$ can be changed to an integral, since we are interested in a bulk material, and with the use of the addition theorem for Legendre polynomials, the integrand can be reduced to a form for which the integrations over $\vec{k}$ can be accomplished:

In order to make the expansion in powers of $\vec{q}$ one must make assumptions about the $\vec{q}$ dependence of the scattering matrix elements. We consider here only 1-OPW pseudo-wave-functions so that for normal processes $^{7}$

$$
\left|v_{l}(\overrightarrow{\mathrm{q}})\right|^{2} \propto q^{2} V^{2}(0),
$$

and for umklapp processes

$$
\left|v_{l}(\vec{q}-\vec{G})\right|^{2} \propto|\vec{q}-\vec{G}|^{2} V(G)^{2}
$$

and

$$
\left|v_{t}(\vec{q}-\vec{G})\right|^{2} \propto|\vec{G}|^{2} V(G)^{2},
$$

where $l$ refers to longitudinal phonon modes and $t$ refers to transverse phonon modes. In addition, the exact position of the Brillouin-zone boundary is important in approximating $\eta_{\vec{q}, s}^{+}$. We take $G / 2 k_{F}$ $<1$ since we are considering such metals as aluminum or indium, where the Fermi surface crosses the zone boundary.

To put Eq. (1) into the form of a matrix equation,

a step which also facilitates handling of some of the angular integrations, both sides of Eq. (1) are multiplied by $P_{1}(\hat{k} \cdot \hat{E})$ and summed over all values of $\hat{k}$. In a manner similar to the handling of $\eta_{\overrightarrow{\mathrm{q}}, s}$ the terms in Eq. (1) are further simplified. The addition theorem for Legendre polynomials is used to express angular quantities appearing in the ex- pressions for $\varphi_{\overrightarrow{k}}$ and $\varphi_{\overrightarrow{k}}$, in terms of angular variables in the energy $\delta$ functions. Free angular in tegrations are carried out and only lowest order terms in $q / G$ or $q / 2 k_{F}$ are kept. The resulting matrix equation is

$$
\begin{aligned}
A \delta_{L, 1}= & -\frac{a_{L} X_{L}^{\prime}}{2 L+1}-\sum_{M} \sum_{s} a_{M} \frac{m^{* 2} V}{\hbar^{2} \pi} \\
& \times \iint \frac{1}{|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|} q^{2} d q d(\hat{q} \cdot \hat{G})\left|W_{s}(\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}})\right|^{2} \\
& \times P_{M}\left(\frac{|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|}{2 k_{F}}\right) P_{L}\left(\frac{|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|}{2 k_{F}}\right) \Theta\left(1-\frac{|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|}{2 k_{F}}\right),
\end{aligned}
$$

where
$$
A=\frac{-2 \pi k_{F}^{2} \hbar e E}{3 m^{*}},
$$
$$
\left|W_{s}(\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}})\right|^{2}=\beta \omega_{\overrightarrow{\mathrm{q}}, s} \hbar N_{\overrightarrow{\mathrm{q}}, s}^{0}\left(N_{\overrightarrow{\mathrm{q}}, s}^{0}+1\right)\left|v_{s}(\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}})\right|^{2},
$$
and

$$
\begin{aligned}
& X_{L}^{\prime}=\frac{2 \pi k_{F}}{\tau_{i}}+\frac{m^{*} V}{\hbar^{2} \pi} \sum_{s} \int q d q\left|W_{s}(q)\right|^{2} \\
& \times\left[1-P_{L}\left(1-\frac{q^{2}}{2 k_{F}^{2}}\right)\right. \\
&\left.\quad-2 P_{L}\left(\frac{q}{2 k_{F}}\right)^{2}\left(\frac{V^{2}(q) q}{V^{2}(q) q+2 V^{2}(G) G}\right)\right]. \quad \text { (4) }
\end{aligned}
$$

The second term on the right-hand side of Eq. (3) is due to umklapp processes only, the first, the diagonal term, is due mainly to normal processes but includes effects of phonon drag.

It is immediately evident that if all the $a_{M}$ except $a_{1}$ are taken to be zero, one would get the standard result of the variational principle for the case as- sumed (where only two Brillouin-zone boundaries intersect the Fermi surface). $^{1}$ In fact, this is a poor approximation. The contribution to the right- hand side of Eq. (3) from terms for which $a_{M} \neq a_{1}$ is large and cannot be ignored compared to the single term containing $a_{1}$.

To find a solution which includes all of the $a_{n}$ it is important to understand the dependence of $X_{L}^{\prime}$ on $L$. The $X_{L}^{\prime}$ have been calculated numerically for various temperatures. $X_{L}^{\prime}$ is a rapidly converging sequence, that is, equal to a constant, $X_{\infty}^{\prime}$, for all but the first few values of $L$. Thus as a first ap- proximation we let $X_{L}^{\prime}=X_{\infty}^{\prime}$ and as second and third approximations allow $X_{1}^{\prime}$ and $X_{3}^{\prime}$ successively to be different from $X_{\infty}^{\prime}$. Any number of additional terms, $X_{L}^{\prime} \neq X_{\infty}^{\prime}$, can be included although, as it turns out, only the first changes the result signifi- cantly. Equation (3) can be solved to give $\varphi_{\vec{k}}$ and $1 / a_{1}$, which for the case of a spherical Fermi surface is just proportional to the resistivity.

For $\hat{k} \cdot \hat{E}=y>0$, and in the second approximation,

$$
\varphi_{\overrightarrow{\mathrm{k}}}=\varphi(\hat{k} \cdot \hat{E})=\varphi(y)=\varphi_{0}(y)\left[1-\frac{X_{1}^{\prime}}{A}\left(\frac{1}{X_{1}^{\prime}}-\frac{1}{X_{\infty}^{\prime}}\right) \frac{4 k_{F} V m^{*}}{G \hbar^{2} \pi} \sum_{s} \int q^{2} d q \int_{(G-q) / 2 k_{F}}^{(G+q) / 2 k_{F}}\left|W_{s}(\bar{z}=|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|)\right|^{2} P_{1}(z) \varphi_{0}(z) d z\right]^{-1}
$$

and

$$
\begin{aligned}
\left(\frac{1}{a_{1}}\right)_{1} & =\frac{X_{1}^{\prime}}{(-3 A)}\left[1-\frac{X_{1}^{\prime}}{A}\left(\frac{1}{X_{L}^{\prime}}-\frac{1}{X_{\infty}^{\prime}}\right) \frac{4 k_{F} V m^{*}}{G \hbar^{2} \pi} \sum_{s} \int q^{2} d q \int_{(G-q) / 2 k_{F}}^{(G+q) / 2 k_{F}} d z\left|W_{s}(\bar{z}=|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|)\right|^{2} P_{1}(z) \varphi_{0}(z)\right] \\
& \times\left[1+\frac{4 m^{*} k_{F} V X_{1}^{\prime}}{\hbar^{2} G A X_{\infty}^{\prime} \pi} \sum_{s} \int q^{2} d q \int_{(G-q) / 2 k_{F}}^{(G+q) / 2 k_{F}} d z\left|W_{s}(\bar{z}=|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|)\right|^{2} P_{1}(z) \varphi_{0}(z)\right]^{-1},
\end{aligned}
$$

where

$$
\varphi_{0}(y)=-3 \frac{A}{X_{1}^{\prime}} P_{1}(y)\left[1+\frac{4 k_{F} V m^{*}}{G \pi \hbar^{2} X_{\infty}^{\prime}} \sum_{s} \int q^{2} d q\left|W_{s}(|\overrightarrow{\mathrm{q}}-\overrightarrow{\mathrm{G}}|=\bar{y})\right|^{2} \Theta\left(\frac{q+G}{2 k_{F}}-y\right) \Theta\left(y-\frac{G-q}{2 k_{F}}\right)\right]^{-1}
$$

and $\bar{z}=z 2 k_{F}$ and $\bar{y}=y 2 k_{F}$.

In order to compare the analytic results with experimental data, numerical calculations for aluminum of the electronic distribution function and the resistivity were carried out using equations similar to (6) for $1 / a_{1}$ and to (5) for $\varphi_{\vec{k}}$ which include even the next-order correction $X_{3}' \neq X_{\infty}'$ (Figs. 1-10). In all cases except one (which will be discussed subsequently) the numerical calculation of the integrals was straightforward. We have used a value of $G=2 \pi \sqrt{3} / c$, where $c=4.04 \AA$, to approximate the geometry of $\mathrm{Al}$, where this value of $G$ represents the smallest reciprocal-lattice vector, which is in the [111] direction.

The greatest difficulty in the numerical calculations has been in the treatment of the phonon spectra. A correct treatment would involve the process of allowing $\omega_{\vec{q}, s}$ to vary with the direction of $\vec{q}$ as well as the magnitude. The integrals involved in this calculation are too difficult to allow for such an exact treatment. We have already assumed $\omega_{\vec{q}, s}$ to be a function of $|\vec{q}|$ alone in deriving Eqs. (5) and (6) and have attempted to determine the change in the results obtained by using the spectra appropriate to phonons moving in different directions. A typical difference is shown in Figs. 6 and 7; in few cases are the essential results changed and they are discussed subsequently.

For the normal scattering term in $X_{L}^{\prime}$ only longitudinal phonon modes enter, but for terms involving umklapp processes all phonon modes will enter. $^{12}$ For temperatures less than $10^{\circ} \mathrm{K}$ a Debye approximation to the phonon spectrum was used, and there is little uncertainty in determining the appropriate value of the speed of sound (less than $20 \%$ variation). Also for temperatures less than $10^{\circ} \mathrm{K}$ we have used in the normal matrix element $V^{2}(q) \approx V^{2}(0)$ and in the umklapp matrix element $[\vec{q}-\vec{G} \cdot \vec{e}_{t}(\vec{q})]^{2} V^{2}(\vec{q}-\vec{G}) \approx[\vec{G} \cdot \vec{e}_{t}(\vec{q})]^{2} V^{2}(G)$. Although the form factor at $\vec{q}=0, V(0)$, is well defined there is some uncertainty in $V$ at $\vec{G}$, since in this area

![](./images/812728010904961027_1.jpg)

FIG. 1. Normalized expression for the distribution function $(X_{1}^{\prime} /-3 A) \varphi_{\vec{k}}=F(\hat{k} \cdot \hat{E})$ . Note that use of only the first Legendre polynomial in the expansion would produce a straight line, $F(\hat{k} \cdot \hat{E})=\hat{k} \cdot \hat{E}$ . The dip is centered at the Brillouin-zone boundary. The function $F(\hat{k} \cdot \hat{E})$ is given for $\rho_{0}=0.418 ×10^{-9} \Omega cm$ and $T=10^{\circ} K$ . Where two curves are distinguishable, the lower curve was calculated for $X_{1}' \neq X_{\infty}'$ and $X_{3}' \neq X_{\infty}'$ and the upper curve for only $X_{1}' \neq X_{\infty}'$ .

![](./images/812728010904961027_2.jpg)

FIG. 2. Same as Fig. 1 except $\rho_{0}=0.218 ×10^{-7} \Omega cm$  and $T=100^{\circ} K$ .

![](./images/812728010904961027_3.jpg)

FIG. 3. Same as Fig. 1 except $\rho_{0}=0.218 ×10^{-7} \Omega cm$  and $T=10^{\circ} K$ .

![](./images/812728010904961027_4.jpg)

FIG. 4. Temperature-dependent part of the resistivity
as a function of temperature for (a) $q_{\mathrm{min}}=0$, (b) $q_{\mathrm{min}}$
$=0.005 \times 2 k_{F}$, and (c) $q_{\mathrm{min}}=0.01 \times 2 k_{F}$, and $\rho_{0}=0.418 \times 10^{-9}$
$\Omega \mathrm{cm} ; V(G)=0.02$ Ry.

$V$ is close to zero. We have used the value 0.018
Ry. $^{13}$

For temperatures greater than $10^{\circ} \mathrm{K}$ the full
phonon spectra and a complete functional form of
$V$ (Ref. 14) were used in the integrals over wave
vector. Unlike the case with low temperatures,
the quantitative results often vary greatly depend-
ing on which phonon mode is used.

It can be seen from Eqs. (5) and (6) that the de-
viation of the distribution function $\varphi_{\vec{k}}$ from a form
proportional to $\hat{k} \cdot \hat{E}$ occurs in a region about $\hat{k} \cdot \hat{E}$
$=G / 2 k_{F}$, the size of the region increasing with
temperature. In addition, the size of the dip in
the distribution function increases with size of the
matrix element for umklapp scattering. It de-
creases with increasing magnitude of the impurity
resistance and the size of the normal scattering
term, although the last factor has a very small ef-
fect.

The reduction of the number of electrons away
from equilibrium at the zone boundary is due to
the fact that umklapp scattering, which drives the
electrons back to equilibrium, is strong near the
zone boundary. If the size of the umklapp matrix
element is decreased or the impurity concentration
is increased, the number of electrons at the zone
boundaries will be increased, because the impurity
scattering, which is symmetric over the Fermi
surface, will have been made more important. The
normal processes also scatter evenly over the
Fermi surface, so that even when the impurity
concentration is zero, there is a balance between
the asymmetric umklapp scattering and the normal
scattering which will determine just how large the
reduction in $\varphi_{\vec{k}}$ at the zone boundary is. In addi-
tion, as the temperature is increased the region
around the zone boundary in which umklapp pro-
cesses may take place increases and so, corres-
pondingly, the area around the zone boundary in
which $\varphi_{\vec{k}}$ is reduced increases.

An additional property of the distribution func-
tion, that it is exactly zero at the Brillouin-zone
boundary, is not shown distinctly on the graphs.
This property is the result of assuming, as we
have initially, that the Fermi surface is spherical
at the Brillouin-zone boundary. An approximate
technique for including effects of Fermi surface
curvature near the Brillouin-zone boundary, which
is introduced later, results in an elimination of
this unphysical property.

The distribution function has been calculated
numerically and is given in Figs. 1-3 for differing
values of $T$ and $\rho_{0}$, the resistance due to impuri-
ties. For this particular case both $X_{1}^{\prime}$ and $X_{3}^{\prime}$ were
allowed to be different from $X_{\infty}^{\prime}$.

Graphs of $\rho(T)$, the temperature-dependent part
of the resistivity, show a $T^{2}$ dependence. Except
in the high-temperature $(T>300^{\circ} \mathrm{K})$ and very-low-
$\rho_{0}\left[\rho_{0} \ll \rho(T)\right]$ regions, the results presented are an
accurate solution to the model. The calculation of
the resistivity with $X_{3}^{\prime} \neq X_{\infty}^{\prime}$ shows virtually no
change compared with the case in which just $X_{1}^{\prime}$
$\neq X_{\infty}^{\prime}$. The applicability of this model to aluminum
will be discussed later, especially with respect to

![](./images/812728010904961027_5.jpg)

FIG. 5. Temperature-dependent part of the resistivity
as a function of temperature for $\rho_{0}=0.218 \times 10^{-7} \Omega \mathrm{cm}$.
Also plotted are the data of Krsnik et al. for the same
value of $\rho_{0}$. The phonon spectrum used was $T_{2}$ in the
[110] direction (see Ref. 11).

![](./images/812728010904961027_6.jpg)

FIG. 6. Temperature- dependent part of the re- sistivity as a function of impurity resistance for $q_{min}=0$. The phonon spec- trum used was the degener- ate transverse mode in the [100] direction.

the curvature of the Fermi surface of aluminum near the Brillouin-zone boundary.

Graphs of $\rho(T)$ vs $\rho_{0}$, the impurity resistance, show a characteristic S-shaped curve. The height of the curve varies with temperature, size of the umklapp matrix element, and shape of the phonon spectrum. In fact, a different choice of transverse phonon mode for integrals involving umklapp scat- tering can cause the height of the curve in Fig. 7 to be reduced by as much as 50%, as shown in Fig.6. The position of the curve along the $\rho_{0}$ axis and the height of the curve are sensitive to the size of
G. Increasing the value of $G$ increases the height of the curve and moves the curve to the left.

The position of the curve along the axis is also influenced by the size of the temperature-depen- dent part of $X_{\infty}^{\prime}$. At $20^{\circ} K$, the temperature for which this graph was calculated, the value of $X_{\infty}'(T)$ varies between $6 \times 10^{-10}$ and $2 \times 10^{-9} \Omega cm$, depending on the direction of the longitudinal pho- non mode chosen for the calculation. In addition, an increase in temperature will cause the tem-

![](./images/812728010904961027_7.jpg)

FIG. 7. Temperature-dependent part of the resistivity as a function of impurity resistance for $q_{min}=0$. The phonon spectrum used was $T_{2}$ in the [110] direction (see Ref. 11).

![](./images/812728010904961027_8.jpg)

FIG. 8. Deviation from Matthiessen's rule as a func- tion of temperature for (a) $\rho_{0}=0.487 \times 10^{-7} \Omega cm$ and (b) $\rho_{0}=6.81 \times 10^{-7} \Omega$ cm shown with data obtained by Seth and Woods. The points denoted by $\times$ are for $\rho_{0}=0.487$ $\times 10^{-7} \Omega cm$ and by + are for $\rho_{0}=6.81 \times 10^{-7} \Omega cm$.

![](./images/812728010904961027_9.jpg)

FIG. 9. Temperature-dependent part of the resistivity vs temperature for $q_{\min }=0.03 \times 2 k_{F}, V(G)=0.018$ Ry, and $\rho_{0}=0.418 \times 10^{-9} \Omega \mathrm{cm}$. Data for $\rho_{0}=0.418 \times 10^{-9} \Omega \mathrm{cm}$ taken by Ekin and Maxfield are also shown.

perature dependent part of $X_{\infty}^{\prime}$ to increase, which, in turn, causes the graph of $\rho(T)$ vs $\rho_{0}$ to shift to the right. The low- $\rho_{0}$ limit is reached when the temperature-dependent part of $X_{\infty}^{\prime}$ is greater than $\rho_{0}$ and occurs when the dip in the distribution function about the zone boundary is largest. The high- $\rho_{0}$ limit corresponds physically to the limit in which the number of electrons scattered symmetrically by the impurities is much larger than the number scattered by the anisotropic umklapp processes, and the solution to the Boltzmann equation is just the isotropic solution $\varphi_{\vec{k}} \propto \hat{k} \cdot \hat{E}$. In this limit the influence of umklapp scattering on the distribution function at the zone boundaries is overshadowed by the impurity scattering.

We are also interested in looking at the deviation from Matthiessen's rule (DMR) as measured experimentally. This is generally calculated as $^{14}$ $\left[\rho_{2}(T)-\rho_{02}\right]-\left[\rho_{1}(T)-\rho_{01}\right]$, where $\rho_{2}(T)$ is the resistivity measured at some impurity concentration (2) and temperature $T$ and $\rho_{02}$ is the resistivity measured at the same impurity concentration and $0{ }^{\circ} \mathrm{K}$ temperature. $\rho_{1}(T)$ is the resistivity measured at temperature $T$ and some impurity concentration such that $\rho_{01}$ is in the low impurity limit and $\rho_{01}$ is the resistivity measured at the same impurity concentration and $0{ }^{\circ} \mathrm{K}$ temperature. The low impurity limit is reached when the temperature-dependent part of the resistivity no longer depends on impurity concentration. The deviation from Matthiessen's rule was calculated from 0 to $300{ }^{\circ} \mathrm{K}$ and plotted in Fig. 8.

![](./images/812728010904961027_10.jpg)

FIG. 10. Umklapp scattering processes on a Fermi surface similar to that of aluminum.

## IV. MODIFICATIONS DUE TO FERMI-SURFACE CURVATURE

This model is not expected to be an accurate representation of aluminum for very low temperatures and, indeed, in this region $\rho(T)$ is observed to vary as $T^{3}$ not $T^{2}$ as the model predicts. A more accurate treatment for aluminum would involve use of a 2-OPW plane-wave approximation in the energy-wave-number relationships for the electrons, the electron-phonon scattering matrix elements, as well as the driving term $\left[\vec{v}_{\vec{k}}\left(E_{F}\right) \cdot \vec{E}\right]$ in the Boltzmann equation. This is a complicated process. The easiest modification to treat is that of the driving term, but a detailed analysis shows that any small term added to the driving term will also add only a small term to the resistivity, certainly not large enough to change its basic temperature dependence.

One might try to make a simple modification to this model by roughly approximating the changes a 2-OPW model would make to the basic equations. The change that has been made was to allow the umklapp matrix element to be zero for the phonon wave vector smaller than a certain $q_{\min }$. Since distortion of the Fermi surface does produce a gap between two bands in $k$ space this seems to be a perfectly normal and simple approach. In fact one must look carefully at the Fermi surface and the definition of umklapp processes to understand the feasibility of such an approach. Figure 10 shows a cross section of a Fermi surface similar to that of aluminum. All the scattering processes represented are umklapp processes. In process 1 there is indeed a value of $|\vec{q}|$ below which no scattering processes can take place. For processes

2 and 3 there is a value of $|\vec{q}|$ below which the scattering process is modified by the distortion of the Fermi surface; the distortion of the Fermi surface is such that these processes do not con- tribute as much to the resistivity as other umklapp processes, because the change in the velocities be- tween initial and final states is almost zero. Therefore as a first approximation we ignore these processes.

The size of $q_{min}$ was chosen to best fit the ex perimental data of Ekin and Maxfield $^{15}$ in the 0 to $10^{\circ} K$ temperature range, and was slightly larger(by a factor of 2) than the value one might approxi- mate from the shape of the Fermi surface of alu- minum. $^{13}$ This may be because the actual umklapp matrix elements are distorted in a larger region around the zone boundaries than the region of dis- tortion of the actual geometry of the surface. The effect of this modification would reduce the amount of umklapp scattering for low temperatures and very small values of $\vec{q}$ so that the temperature de pendence of $\rho(T)$ would be $T^{5}$ (umklapp totally eliminated) or a combination of $T^{2}$ and $T^{5}$ (umklapp term reduced) in the low-temperature region, and a $T^{2}$ term slightly reduced in the high-temperature region.

Figure 4 shows a graph of $\rho(T)$ vs $T$ with $q_{min}$  $=0.01 ×2 k_{F}, q_{min }=0.005 ×2 k_{F}$ , and with $q_{min }=0$ . As expected, the $T^{2}$ dependence of $\rho(T)$ changes to some dependence between $T^{2}$ and $T^{5}$ for temperatures below some cutoff temperature which in- creases with the size of $q_{min}$ . Figure 9 shows a graph of $\rho(T)$ vs $T$ with $q_{min}=0.03 ×2 k_{F}$ , the value of $q_{min }$ which gives the best fit with the data ofEkin and Maxfield. Graphs of $\rho(T)$ vs $\rho_{0}$ with $q_{min}$  $=0.03 ×2 k_{F}$ show little change from the curves shown in Figs. 6 and 7 for which $q_{min}=0$ and con sequently are not shown.

## V. DISCUSSION-COMPARISON WITH OTHER THEORIES
The results of this analysis are unique with re- spect to any current variational-technique ap- proach, with the possible exception of the recent work of Bergman, Kaveh, and Wiser, $^{16}$ because an infinite number of Legendre polynomials have been included in the electronic distribution func- tion. In previous variational-technique calcula- tions of the resistivity, inclusion of only a few polynomials have made small contributions to the resistivity. This is to be expected, since the true shape of the distribution function, sharply indented about $\hat{k} \cdot \hat{E}=G / 2 k_{F}$ , could only be reproduced with a large number of Legendre polynomials.

The work of Bergman, Kaveh, and Wiser is anextension of the work of Lawrence and Wilkins, $^{17}$  who attempted to take into account the distortion of the Fermi surface by using 2-OPW wave func- tions. Lawrence and Wilkins did an exact varia- tional calculation of the resistivity with $\varphi_{k} \propto \hat{k} \cdot \hat{E}$ . Without such a 2-OPW modification the tempera- ture dependence would be a $T^{2}$ dependence due to umklapp terms. Their work resulted in power laws of $T^{5}$ below $3^{\circ} K$ , a $T^{4}$ law from 4 to $10^{\circ} K$ , and a $T^{3}$ law in the $20-40^{\circ} K$ range. This modifi cation of the power laws in the low-temperature region agrees well with the results of our modifi- cation due to Fermi-surface curvature, where umklapp scattering processes were simply not allowed for a $\vec{q}$ less than some $q_{min }$ . In our calcu lation the temperature dependence was changed as a result of this modification to a dependence proportional to $T^{5}$ at the lowest temperatures, while gradually changing to $T^{2}$ at higher tempera tures, with the boundaries of the various regions depending on the value of $q_{min}$ chosen.

Bergman, Kaveh, and Wiser claim to have ex- tended the work of Lawrence and Wilkins consid- erably by using a trial function which has a dip in the region of distortion of the spherical Fermi surface. The depth of the dip was allowed to vary with temperature and impurity concentration. The results of their calculation seem to agree with ex- perimental results for aluminum quite well for temperatures less than about $10^{\circ} K$ . We don't ex pect this technique to produce meaningful results beyond about $10^{\circ} K$ because this tempera ture the actual dip in the distribution function oc- curs over a much larger area of the Fermi sur- face than just the region of distortion of the spher- ical surface.

In addition, the use of this particular trial func- tion for the alkali metals, which have spherical Fermi surfaces, would produce no deviation from Matthiessen's rule at all, since the distribution function would just be proportional to $\hat{k} \cdot \hat{E}$ . In fact, a small deviation from Matthiessen's rule is observed and we think it is a result of a small decrease in the distribution function which does occur on the parts of the Fermi surface closest to zone boundaries. Umklapp processes can oc- cur, although reduced in strength on these parts of the Fermi surface and are responsible for a small decrease in the distribution function there.

The calculations of Bergman, Kaveh, and Wiser and Lawrence and Wilkins are complementary to our work. They have used an approximate elec- tronic distribution function, although in the case of Bergman et al. this may be a fairly good ap- proximation for low temperatures, but a correct treatment of curvature of the Fermi surface. We have chosen to assume the Fermi surface to be spherical, completely excluding those umklapp scattering processes where use of a 2-OPW pseudo-wave-function is necessary, but have used

a more correct form of the electronic distribution function based on an asymptotic solution to the Boltzmann equation. The work of Bergman *et al.* gives reasonably good agreement with experiment for aluminum in the low-temperature range, but appears to yield poorer agreement with experiment for aluminum in the higher-temperature range. Our method gives good agreement with experiment in the 5 to $300^\circ$K temperature range and promises to be applicable to the alkali metals, but gives poor agreement in the 0 to $5^\circ$K temperature range.

We disagree with the finding of Bergman *et al.* that the normal scattering processes contribute to a large percentage of the DMR in aluminum. From the analytic form of our expression for the electronic distribution function and the resulting conductivity we can easily separate the contributions due to umklapp and normal scattering processes. These were calculated separately and it was found that the total temperature-dependent part of the resistivity contributed by normal processes alone is two orders of magnitude smaller than the resistivity due to umklapp processes for the temperature range in which Bergman *et al.* have made calculations. This is due to the fact that in normal processes only small-angle scattering contributes, while for umklapp processes large-angle scattering is present. While the use of a strongly indented distribution function, rather than the trial function proportional to $\hat{k} \cdot \hat{E}$, will reduce the contribution to the resistivity due to the umklapp processes relative to that due to the normal processes, the umklapp processes still dominate. In addition, at higher impurity concentrations the distribution function should approach the form proportional to $\hat{k} \cdot \hat{E}$. In that case the finding of Lawrence and Wilkins, using 2-OPW pseudo-wave-functions and $\varphi_{\boldsymbol{k}} \propto \hat{k} \cdot \hat{E}$, that the normal processes still contribute only a small part to the resistivity, should apply.

Thus although we suppose their calculations may be correct in the low-temperature range their interpretation of their numerical results appears somewhat confused.

The $\rho(T)$-vs-$\rho_0$ curve produced by Bergman *et al.* seems to fit the experimental data quite well. However, the more recent data of Krsnik *et al.* has not been included in their graph.¹⁸ The curve of $\rho(T)$ vs $\rho_0$ produced by Bergman *et al.* flattens off into an impure region after about three decades on the $\rho_0$ scale (as does our work), long before the complete set of experimental data shows any sign of flattening off. One possible explanation for this discrepancy might be that not all of the zone boundaries present in aluminum have been included in Bergman's work.

The results of the analyses of Klemens and Jackson,⁴ Ehrlich,⁵ and Schotte and Schotte⁶ have not been discussed in detail here because the diffusion-equation approach is, as we have stated earlier, essentially a very-low-temperature approximation. Such an approach cannot be compared readily to our work, which clearly is not valid for temperatures less than $5^\circ$K.

In conclusion, while the methods discussed in this section, including our own, give similar behavior at low temperatures, only our method can be used for temperatures above about $10^\circ$K (and up to about $300^\circ$K). This is a significant improvement. We feel that this improvement was possible because, with the approximate solution to the Boltzmann equation we have obtained, we were able to accurately represent the significant processes, the highly anisotropic umklapp scattering processes, which are responsible for the main features of the observed deviations from Matthiessen's rule.

## VI. DISCUSSION-COMPARISON WITH EXPERIMENTS

In a recent review article¹⁹ Bass has stated that the various measurements of the temperature-dependent part of the resistivity of aluminum-based alloys do not completely agree in the low-temperature region ($4$-$20^\circ$K). The more recent experiments seem to indicate a $T^3$ temperature dependence,²⁰ although some researchers report a $T^2$ dependence.

Krsnik, Babic, and Rizzuto¹⁸ (1973) indicate that as temperature increases above $15^\circ$K the temperature-dependent part of the resistivity gradually changes to $T^2$ up to about $100^\circ$K.

In the case of experimental measurements of the DMR over a much wider range of temperatures there is considerable disagreement between researchers. Measurements of the deviations from Matthiessen's rule made by Toth¹⁹ showed that the DMR increased with increasing temperature and contained "humps" at about $50^\circ$K. The data of Panova *et al.* and Seth and Woods is in rough agreement but differs in detail from that of Toth. The DMR also contain humps around $50^\circ$K but the DMR is found to decrease or stay approximately constant, depending on impurity concentration, with temperature after about $100^\circ$K.

The data of Ekin and Maxfield have been included in Fig. 9, which shows our calculation of $\rho(T)$ vs $T$ from 0 to $10^\circ$K. Agreement in the $0$-$4^\circ$K range is not very good. This is because in that temperature range all of the umklapp scattering processes involving a scattering wave vector less than $q_{\text{min}}$ have been removed, leaving only normal scattering processes, which contribute only a

small $T^{5}$ term. A more accurate modification to take into account distortion of the Fermi surface would have reduced, rather than eliminated, the contribution due to umklapp processes for values of the scattering wave vector less than $q_{\text {min }}$, since the distortion of the Fermi surface, while elimi- nating some umklapp processes, only changes others into more-normal-type processes. These additional terms would have produced an increase in the resistivity in the $0-4^{\circ} \mathrm{K}$ range over that which is indicated, resulting in better qualitative agreement between our calculation and experiment in this region.

Figure 6 shows $\rho(T)$ vs $T$ for temperatures from 10 to $100^{\circ} \mathrm{K}$ and includes data of measurements of Krsnik *et al.* Agreement here is good, especially since there is no adjustment of parameters. The value of $q_{\text {min }}$ affects the results only for temperatures less than about $40^{\circ} \mathrm{K}$ and results in better agreement with the data than for $q_{\text {min }}=0$. One characteristic of the experimental curves, noted by Krsnik *et al.*, is that the point at which the temperature dependence changes from $T^{3}$ to $T^{2}$ increases with increasing impurity resistance; this feature is also present in our results.

Figure 8 shows our calculations for the DMR as a function of temperature from 0 to $300^{\circ} \mathrm{K}$. Some of the data of Seth and Woods has been plotted on the same graph.

Caplin and Rizzuto, and Carter, and Krsnik *et al.* have found that the temperature-dependent part of the resistivity varies with impurity concentration roughly as $\ln \rho_{0}$ over at least 5 decades. We present the data of Krsnik *et al.* in Figs. 6 and 7 along with the results of our calculation. Although the general features are reproduced, our calculation definitely predicts a high-$\rho_{0}$ limit after three decades, which is not present in the experimental data. The low-$\rho_{0}$ limit is definitely observed and the resistivity at which it is reached decreases with temperature as predicted by our calculation. As mentioned earlier, certain characteristics of the graph such as height and position along the $\rho_{0}$ scale are parameter dependent and can be made to fit the curves in these respects quite perfectly with plausible values for all parameters.

In order to understand the results of our analysis in comparison to experimental measurements on aluminum one must have some idea of how closely our model approximates aluminum and how the discrepancies will affect our calculations. The problem of curvature of the Fermi surface near the Brillouin-zone boundaries has already been discussed. We expect that in regions of low temperature and low impurity concentration where the regions of Fermi surface near the Brillouin-zone boundaries are important our model may not predict results similar to those observed in aluminum, and indeed this is the case. Our attempts to take into account the curvature of the Fermi surface are only approximately successful. Better approximations could have been made and, as has been indicated, they would give better agreement with experiment.

Because we have included only two Brillouin- zone boundaries, our model essentially depicts a crystal whose lattice spacing along two directions is very much shorter than along the third. It is difficult to predict how important an accurate treatment of all the Brillouin-zone boundaries is to reproducing the experimental data on aluminum, especially since the position of the Brillouin-zone boundary varies with crystallographic direction.
The correct distribution function for aluminum would have to be a function of an azimuthal angle in addition to $\hat{k} \cdot \hat{E}$. This approximate treatment of the Brillouin-zone boundaries in our model is a possible explanation for the fact that our $\rho(T)$-vs-$\rho_{0}$ curve seems to flatten off in the high-$\rho_{0}$ region, whereas experimental data show that no such flattening occurs, or at least not as quickly as our results show. Our results indicate that the curve will shift to the right, although the width of variation remains constant, if the value of $G / 2 k_{F}$ is decreased or if $X_{a}^{\prime}(T)$ is increased. The experimental results may actually be a superposition or average of a number of curves centered about different points on the axis, each curve appropriate for the electric field pointed along a particular crystallographic direction and thus to a slightly different value of $G$. It is the particular functional form of the distribution function on $\rho_{0}$ that appears in our results which determines the width of the $\rho(T)$-vs-$\rho_{0}$ curve. In addition, we are convinced that any theory for aluminum which assumes the Boltzmann equation to be correct will result in a $\rho(T)$-vs-$\rho_{0}$ curve with a "dirty" limit. This would also be true of results obtained by use of variational calculations. The $\rho(T)$-vs-$\rho_{0}$ curves of Schotte and Schotte also have the characteristic of flattening off sooner than experiment indicates. Nevertheless, their model did not attempt to include any known data on the Fermi surface of aluminum, and they may not have allowed the position of the zone boundary to vary with direction.

To summarize, our calculation has used a very simple model, which is capable of reproducing much of the observable results for a number of materials, temperatures, and impurity concentrations and promises to be applicable to an even wider range. All the results are in terms of known parameters and require no new concepts, just a more detailed calculation. Of the two curves which fit the data for aluminum the least well the

$\rho(T)$-vs-$T$ curve in the $0$-$10^\circ$K range is the most easily explained in terms of an inadequate treat- ment of the Fermi surface of aluminum. Although at present there is no way of knowing if a more detailed analysis using the Boltzmann equation will also result in better agreement with the $\rho(T)$-vs-$\rho_0$ curve, we feel that a 2-OPW approximation would improve the low-temperature behavior of our calculation but not change the essential results over the whole temperature range significantly.

The main importance of this analysis is the clari- fication of the role of anisotropic umklapp pro- cesses in producing the observed DMR in simple metals and the understanding of the very non- classical shape of the distribution function. This method may easily be extended to provide detailed results for materials other than aluminum, and to obtain the thermal conductivity for these same materials.

*Work supported by the National Science Foundation under Contract No. GP-23518.
†Now at Sandia Laboratories, Alburquerque, New Mexi- co.
¹J. M. Ziman, *Electrons and Phonons* (Oxford U.P., London, 1960).
²J. W. Ekin and A. Bringer, Phys. Rev. B (to be pub- lished).
³J. Black and D. L. Mills, Phys. Rev. B 9, 1458 (1974).
⁴P. G. Klemens and J. L. Jackson, *Physica* (Utr.) 30, 2031 (1964).
⁵A. C. Ehrlich, Phys. Rev. B 1, 4537 (1970).
⁶D. Schotte and U. Schotte, Solid State Commun. 10, 131 (1972).
⁷L. J. Sham and J. M. Ziman, in *Solid State Physics*, edited by F. Seitz and D. Turnbull (Academic, New York, 1963), Vol. 15.
⁸R. E. Peierls, *Quantum Theory of Solids* (Oxford U.] London, 1956).
⁹N. W. Ashcroft, Phys. Lett. 23, 48 (1966).
¹⁰W. A. Harrison, Phys. Rev. 131, 2433 (1964).
¹¹J. L. Yarnell, J. L. Warren, and S. Koenig, in *Lattice Dynamics, Proceedings of an International Conference*, edited by R. F. Wallis (Pergamon, New York, 1965), p. 57.
¹²E. Bergeron, Ph.D. thesis (Northeastern University, Boston, Mass., 1974) (unpublished), available from University Microfilms, Ann Arbor, Mich.
¹³W. A. Harrison, *Pseudopotentials in the Theory of Metals* (Benjamin, New York, 1966).
¹⁴R. S. Seth and S. B. Woods, Phys. Rev. B 2, 2961 (1971).
¹⁵J. W. Ekin and B. W. Maxfield, Phys. Rev. B 2, 4805 (1970).
¹⁶Y. Bergman, M. Kaveh, and N. Wiser, Phys. Rev. Lett. 32, 606 (1974).
¹⁷W. E. Lawrence and J. W. Wilkins, Phys. Rev. B 6, 4466 (1972).
¹⁸R. Krsnik, E. Babic, and C. Rizzuto, Solid State Com- mun. 12, 891 (1973).
¹⁹J. Bass, Adv. Phys. 21, 431 (1972).
²⁰S. Senoussi and I. A. Campbell, J. Phys. F 3, L19 (1973).