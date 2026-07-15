# Electronic Spectral Shifts and Linebroadening of Heteroclusters

ANDREAS HEIDENREICH AND JOSHUA JORTNER*
School of Chemistry, Raymond and Beverly Sackler Faculty of Exact Sciences,
Tel Aviv University, 69978 Tel Aviv, Israel

(Received 20 June 1993)

Dedicated to John A. Pople, recipient of the 1992 Wolf Prize in Chemistry

**Abstract** In this paper we report on molecular dynamics simulations of the lineshapes of the absorption spectra of perylene Arₙ heteroclusters ($n$ = 2–22), which rest on the spectral density method in conjunction with the excited-state potential modelling scheme. Inhomogeneous semiclassical absorption lineshapes were calculated by averaging of microcanonical spectra over the accessible phase space region. The size dependence and isomer specificity of the spectral shifts and spectral linewidths were elucidated, with the spectral shifts providing a powerful tool for the identification of structural isomers. Some information on isomerization dynamics was inferred from the temperature dependence of the linewidths, which mark the onset of correlated surface motion for (5|0) and (5|5) heteroclusters, as well as the onset of 2D $\rightleftarrows$ 3D isomerization and side crossing for (22|0) heteroclusters.

## I. INTRODUCTION

M·Aₙ heteroclusters, consisting of an organic aromatic molecule (M) bound to rare gas (A) atoms,¹⁴ allow for the exploration of microscopic solvation phenomena.⁵⁶ Extensive experimental³·⁷⁻²³ and theoretical¹·³·⁸·¹⁰⁻¹⁷·²⁴⁻³² studies of these heteroclusters provided a wealth of information on the energetics and dynamics of a guest molecule embedded in a local solvent configuration, thus providing basic information on solvent perturbations, as interrogated from the microscopic point of view. Of considerable interest in the context of the energetics of large finite systems are the spectral shifts of M·Aₙ heteroclusters,¹⁹·²³·³³⁻³⁶ i.e., the energy of the electronic origin of the first spin-allowed transition of M·Aₙ relative to that of M. Extensive literature is available regarding the spectral shifts of an impurity molecule in an (infinite) solvent.³⁷⁻⁴² For intravalence excitations of the impurity molecule, the red spectral shifts (towards lower energies) originate from dispersive interactions.³⁷⁻⁴² The conceptual framework for the description of dispersive spectral shifts was advanced by Longuet-Higgins and Pople (LHP),⁴² whose treatment rested on two central approximations: (i) the solute molecule was treated as a point dipole in the multipole expansion of the electrostatic solute–solvent interactions; (ii) spherical averaging over the relative solute–solvent orientations was performed. Early attempts to correlate the observed heterocluster spectral shifts with theory rested on the LHP scheme.³³⁻³⁵ However, since in large M·Aₙ heteroclusters the M–A distances are comparable with the molecular dimensions,¹⁹ the representation of the M molecule by a point transition dipole is clearly inadequate. Furthermore, the spherical averaging procedure is inapplicable. Accordingly, the theory of

Andreas Heidenreich was born in Kassel, Germany, and studied chemistry at the University of Marburg. After receiving his doctoral degree in 1990, he worked as a postdoctoral fellow at Tel Aviv University. In 1993 he joined Prof. J. Sauer's group at the Humboldt University/Max Planck Institute, Berlin. His current interests are molecular dynamics simulations of clusters and zeolites.

Joshua Jortner was born in Poland and immigrated to Israel in 1940. He received his Ph.D. from The Hebrew University of Jerusalem in 1960. He serves as the Heinemann Professor of Chemistry at Tel Aviv University and as the President of the Israel National Academy of Sciences and Humanities. His research interests pertain to the phenomena of energy acquisition, storage, and disposal in isolated molecules, clusters, condensed phases, and biophysical systems.

*Author to whom correspondence should be addressed.

Israel Journal of Chemistry Vol. 33 1993 pp. 467–474

spectral shifts requires a gross modification. Theoretical and computational treatments of spectral shifts of $M \cdot A_{n}$ heteroclusters rested on two distinct approaches:

(1) Shalev, Ben-Horin, and Jortner $^{19,43}$ advanced a semiempirical theory of spectral shifts, which rests on the evaluation of the dispersive contributions to second- order, accounting for the finite-size structural features of M by the utilization of the multicenter monopole representation of the intermolecular interactions. This scheme, which relaxes approximations (i) and (ii), constitutes the generalization of the LHP theory. This semiempirical theory, in conjunction with molecular dynamics data, was successfully applied $^{7,19}$ to account for the spectral shifts of pentacene. $Ar_{n}(n=1-8)$ , tetracene. $Ar_{n}(n=1-8)$ , tetracene. $Kr_{n}(n=1-6), 9,10$ dichloroanthracene. $Ar_{n} (n=1-34), 9,10$ dichloroanthracene. $Kr_{n}(n=1-20)$ , but not for the general pattern of the spectral shifts of anthracene. $A_{n}$  $(A=Ar, Kr ; n=1-8)$ and for perylene. $Ar_{n}(n=1-6).^{19}$ 

(2) Several workers $^{8,17,25-31}$ have adopted a potential mod elling scheme. Excited-state Lennard-Jones atom- atom potentials were chosen for the A-C and A-H interactions, which, together with ground-state mo- lecular dynamics data, were used to account for the spectral shifts over a broad size domain. This proce- dure was applied for the size dependence and isomer specificity of perylene. $Ar_{n}(n=1-45),^{31}$ tetracene. $Ar_{n}$  $(n=1-26),^{8}$ and benzene. $Ar_{n}(n=1-26)^{26,27}$  heteroclusters.

Linear optical electronic spectroscopy provides important information on excited state energetics, allowing for the spectroscopic assignment of structural isomers for small and medium-sized (n =2-6) heteroclusters and for the distinction between interior and surface states of M inor on an $Ar_{n}$ cluster for large heteroclusters. $^{7,8,13,14,17,24-}$ 26,30,31 The experimental and theoretical exploration of thetotal absorption lineshapes provides rich information. $^{44-55}$  While the first moment of the absorption lineshape, which approximates well the spectral shift, originates from the cumulative contributions of the M-A interactions, the second moment of the absorption lineshape is due to(static or dynamic) density fluctuations. $^{55}$ The second spectral moment, the spectral linewidth, and the total lineshape provide important information on homogeneous and inhomogeneous broadening, structural effects, and nuclear dynamics. $^{26,27,30,55}$ In this paper we apply the semiclassical spectral density method $^{26-30}$ in conjunction with the potential modelling scheme $e^{8,17,25-31}$ for the calculation of the total lineshapes of perylene. $Ar_{n}(n=2-22)$ heteroclusters. The perylene. $Ar_{n}$ heteroclusters, $^{31,56-59}$  which were recently experimentally studied over a broad size domain by Bahatt et al., $^{31}$ are of considerable interest in view of an abnormal size dependence of their spectral shifts, which decrease with increasing n for n = 6-10, reaching a local minimum at $n=8 .^{31}$ This abnormal trend was attributed $^{31}$ to the dominance of one-sided structures for n=6-10, and the abundance of two-layered one-sided structures for large n (S22) heteroclusters. In this paper we shall report on the size dependence, isomer specificity, and temperature dependence of the spectroscopic observables, which provide new information on theisomerization dynamics of these interesting perylene. $Ar_{n}$  heteroclusters.

## II. SIMULATIONS
### (II.1) Molecular Dynamics
We have performed classical constant energy MDsimulations using the Quaternion formalism $^{60,61}$ with a 5 value Gear predictor-corrector method for quaternions and for angular velocities and a 4-value Gear predictor- corrector method for translational motions. The thermalequilibration procedure was carried out by iterativerescaling of the velocities as previously described. $^{24}$  Constant energy trajectories were generated in the ground electronic state for 0.3-10 ns. The potential surfaces of perylene. $Ar_{n}$ clusters in the ground electronic state werespecified with Lennard-Jones atom-atom potentials. $^{24}$ 

$$\varepsilon_{\mathrm{Ar}-\mathrm{C}}=43.036 \mathrm{~cm}^{-1} \quad \sigma_{\mathrm{Ar}-\mathrm{C}}=3.3854 \mathring{A}$$

$$\varepsilon_{\mathrm{Ar}-\mathrm{H}}=29.724 \mathrm{~cm}^{-1} \quad \sigma_{\mathrm{Ar}-\mathrm{H}}=3.2072 \mathring{A}$$

$$\varepsilon_{\mathrm{Ar}-\mathrm{Ar}}=98.760 \mathrm{~cm}^{-1} \quad \sigma_{\mathrm{Ar}-\mathrm{Ar}}=3.360 \mathring{A}$$

The perylene molecule was taken to be frozen in its planar equilibrium nuclear configuration (from MNDO geometry optimization $^{62}$ or from X-ray solid-state struc tural data $^{63}$ ). The molecule-fixed cartesian coordinate system was specified by the origin at the center of mass of perylene with the x (in plane parallel to the short axis), the y (in plane parallel to the long axis), and the z axis(perpendicular to the perylene plane).
We have calculated the ground-state potential energy $V_{g}({\vec{r}}_{A}(t)})$ and the excited-state potential energy $V_{c}({\vec{r}}_{A}(t)})$ , where $\vec{r}_{A}(t)(A=1,..., n)$ are the time-depen dent coordinates of the rare-gas atoms. Ensemble average microcanonical observables (denoted by <>) were calcu- lated by averaging over trajectories in the ground elec- tronic state of perylene. $Ar_{n}$ .
### (II.2) Excited-state potential energy parameters
We have used the modelling scheme for the potential parameters for the potential surfaces in the electronically- exited $S_{1}$ state. We introduced a set of excited-state Lennard-Jones atom-atom potential parameters, whereboth the Ar-C and Ar-H pair interactions are modified. $^{31}$ 

$$\varepsilon_{\mathrm{Ar}-\mathrm{C}}^{(\mathrm{e})}=1.1238 \varepsilon_{\mathrm{Ar}-\mathrm{C}}$$

Israel Journal of Chemistry 33 1993

$$
\begin{align*}
\sigma_{\text{Ar-C}}^{(\text{e})}&=1.0088\sigma_{\text{Ar-C}}\\
\varepsilon_{\text{H-Ar}}^{(\text{e})}&=0.8556\varepsilon_{\text{H-Ar}}\\
\sigma_{\text{H-Ar}}^{(\text{e})}&=\sigma_{\text{H-Ar}}
\end{align*}
$$

These potential parameters accounted well for the isomer-specific spectral shifts for $n=1-5.^{31}$

### (II.3) Absorption lineshapes
The electronic absorption lineshape L(E) at the photon energy E is expressed as the Fourier transform of the transition dipole autocorrelation function, I(τ), in the form⁴⁴⁻⁴⁶
$$
\mathrm{L}(\mathrm{E})=(1 / \pi) \operatorname{Re} \int_{0}^{\infty} \mathrm{d} \tau \exp \left[-\mathrm{i}\left(\mathrm{E}-\omega_{\mathrm{eg}}\right) \tau\right] \mathrm{I}(\tau) \quad(2.1)
$$
where
$$
\mathrm{I}(\tau)=\left\langle\exp \left(\mathrm{i} H_{\mathrm{e}} \mathrm{t}\right) \exp \left(-\mathrm{i} H_{\mathrm{g}} \mathrm{t}\right)\right.\tag{2.2}
$$
where $H_{\mathrm{g}}$ and $H_{\mathrm{e}}$ are the ground-state and excited-state Hamiltonians, respectively, and $\omega_{\text{eg}}$ is the 0-0 electronic energy gap of the bare M molecule. The function I(τ) is approximated by the spectral density method, which requires the calculation of the energy gap.⁸⁻²⁴²⁶⁻³⁰ The time-dependent energy gap
$$
\mathrm{U}(\mathrm{t})=\mathrm{V}_{\mathrm{e}}\left(\left\{\overrightarrow{\mathrm{r}}_{\mathrm{A}}(\mathrm{t})\right\}\right)-\mathrm{V}_{\mathrm{g}}\left(\left\{\overrightarrow{\mathrm{r}}_{\mathrm{A}}(\mathrm{t})\right\}\right)\tag{2.3}
$$
is evaluated at regular time intervals along a ground-electronic state MD trajectory. The first and second moments of the energy gap are⁸²⁴
$$
\mathrm{M}_{1}=\langle\mathrm{U}(\mathrm{t})\rangle\tag{2.4}
$$
and
$$
\mathrm{M}_{2}=\langle\mathrm{U}(\mathrm{t})^{2}\rangle\tag{2.5}
$$

The central second moment of the energy gap is
$$
\Delta^{2}=\mathrm{M}_{2}-\mathrm{M}_{1}^{2}\tag{2.6}
$$

$\Delta^{2}$ is referred to as the total dispersion of the absorption band. The classical expressions for the first and the second moment of the absorption lineshape are identical to the corresponding quantum results. The classical energy gap autocorrelation function is⁴⁶⁴⁸⁵⁰⁻⁵⁴
$$
\mathrm{J}(\tau)=\langle\mathrm{U}^{\prime}(0) \mathrm{U}^{\prime}(\tau)\rangle\tag{2.7}
$$
where
$$
\mathrm{U}^{\prime}(\tau)=\mathrm{U}(\tau)-\langle\mathrm{U}\rangle\tag{2.8}
$$

The Fourier transform J(ω) of J(t) is obtained by the Wiener-Khintchine theorem by $\mathrm{J}(\omega)=|\mathrm{U}(\omega)|^{2}$. As a consequence of the fluctuation-dissipation theorem, the semiclassical energy correlation function $\mathrm{J}_{\mathrm{SC}}(\omega)$ in the frequency space is⁵³⁵⁴
$$
\mathrm{J}_{\mathrm{SC}}(\mathrm{w})=\left[1+\tanh \left(\hbar \omega / 2 \mathrm{k}_{\mathrm{B}} \mathrm{T}\right)\right] \mathrm{J}(\omega)\tag{2.9}
$$

The semiclassical homogeneous absorption lineshape, eq
2.1, is approximated by⁵³⁵⁴
$$
\mathrm{L}(\mathrm{E})=(1 / \pi) \operatorname{Re} \int_{0}^{\infty} \mathrm{d} \tau \exp \left[\mathrm{i}\left(\mathrm{E}-\omega_{\mathrm{eg}}+<\mathrm{U}>\right) \tau\right] \exp [-\mathrm{g}(\tau)]
\tag{2.10}
$$
where the correlation function I(τ), eq 2.2, is expressed in terms of $\exp [-\mathrm{g}(\tau)], \mathrm{g}(\tau)$ is the two-time integral of the semiclassical energy gap autocorrelation function (eq 2.9) in the time domain, i.e.,
$$
\mathrm{g}(\tau)=\int_{0}^{\tau} \mathrm{d} \tau_{1} \int_{0}^{\tau_{1}} \mathrm{~d} \tau_{2} \mathrm{~J}_{\mathrm{SC}}\left(\tau_{2}\right)\tag{2.11}
$$

The lineshape, eq 2.10, corresponds to a microcanonical subspectrum. The microcanonical subspectrum was calculated from a single trajectory of 340 ps, which corresponds to a spectral resolution of $0.1 \mathrm{~cm}^{-1}$. The Nyquist frequency was $200 \mathrm{~cm}^{-1}$. A time step of 4 fs was chosen for the integration of the classical equations of motion.

An alternative approach for the simulation of the microcanonical spectrum rests on the calculation of an average of $\mathrm{J}(\omega)$ over (10-100) trajectories and utilizing this average for the calculation of $\mathrm{J}_{\mathrm{SC}}(\omega)$, eq 2.9, and the lineshape from eqs 2.10 and 2.11.

The microcanonical subspectra, eq 2.10, have to be averaged over the accessible region of the phase space. The averaged semiclassical absorption lineshape $\mathrm{L}(\mathrm{E})$ is given by
$$
\overline{\mathrm{L}}(\mathrm{E})=(1 / \pi) \operatorname{Re} \int_{\Omega} \mathrm{dpdq} \rho(\mathrm{p}, \mathrm{q}) \int_{0}^{\infty} \mathrm{d} \tau \exp [\mathrm{i}(\mathrm{E}-
\omega_{\mathrm{eg}}+<\mathrm{U}>) \tau] \exp (-\overline{\mathrm{g}}(\tau ; \mathrm{p}, \mathrm{q}))\tag{2.12}
$$
where $\mathrm{q} \equiv\left\{\overrightarrow{\mathrm{r}}_{\mathrm{A}}(0)\right\}, \mathrm{p} \equiv\left\{\overrightarrow{\mathrm{p}}_{\mathrm{A}}(0)\right\}$, and $\rho(\mathrm{p}, \mathrm{q})$ is the distribution function of the ground electronic state in the accessible region $(\bar{\Omega})$ of the phase space. The averaging over the accessible region of the phase space essentially leads to the inhomogeneous broadening of the absorption spectrum. In practice, we have carried out the averaging over 100 microcanonical subspectra obtained for different initial momenta p and nuclear configurations q.

The generation of the initial conditions for the simulation of the spectra of a structural isomer (i.e., a cluster with a fixed number of atoms on each side of M) was accomplished by the following MD simulation procedure:
(1)Initial thermal equilibration at temperature $\mathrm{T}_{0}$ was achieved by iterated rescaling of the velocities. The temperature $\mathrm{T}_{0}$ was chosen to be lower than the onset of side crossing,³¹ i.e., $\mathrm{T}_{0}=40 \mathrm{~K}$ for small $(n=2-10)$ clusters and $\mathrm{T}_{0}=25 \mathrm{~K}$ for large $(n=16-22)$ clusters.
(2)Prolongation run. A trajectory was run during $10 n$ at $\mathrm{T}_{0}$. The phase space points along the trajectory were sampled in intervals of 100 ps. The identity of the initial structural isomer was preserved, while different nuclear configurations or adcluster isomers could be sampled.

Heidenreich and Jortner/ Spectral Shifts and Linebroadening of Heteroclusters

(3)Thermal equilibration at the desired temperature T = (5-40K). Equilibration runs by iterative rescaling were performed for the 100 sampled phase space points obtained from (2).
(4)Simulations of microcanonical subspectra L(E). These were generated for $t_a$ = 340 ps trajectories by starting from the thermally-equilibrated systems prepared ac- cording to (3). External rotational energy of $k_B$ T/2 per rotational degree of freedom was inserted. The cluster rotation was found to exert a minor effect on the lineshape. $^{28}$ 100 microcanonical spectra were gener ated at each final temperature T = 5-40K.
The averaged spectrum L (E) of a structural isomer was obtained from the averaging over the 100 microcanonical subspectra. This averaged spectrum may contain inhomogeneous broadening contributions due to the existence of different configurations, i.e., a single adcluster or/and adcluster isomers for n = 2-10 (for T = 5-40K) and different structural isomers for n = 22 (at T > 25 K). The simulated structural isomer-specific averaged lineshapes L (E) are specified by the following parameters:
(1) The energy $E_{MAX}$ of the maximum of the prominent0-0 absorption band, with the spectral shift being $\delta v=E_{MAX} .$
(2) The inhomogeneous linewidth $\Gamma$ , i.e., the FWHM of the prominent 0-0 band. One can also consider otherrelated physical parameters:
(3) The distribution $W(\delta v_{a})$ of the spectral shifts (the peak energies) $\delta v_{a}$ of the individual subspectra.
(4) The mean spectral shift $\delta v$ , which is obtained by averaging the peak energies ${\delta v_{a}}$ of the individual microcanonical subspectra. The deviation between $\delta v$ and $\delta v$ is very small, the difference originating from the different averaging over $W(\delta v_{a})$ and over L(E). Within a good approximation for each subspectrum $\delta v_{a}=M_{1}$ , the small deviation $(<0.5 cm^{-1})$ between the spectral shift and the first spectral moment is due to the contributions of the intermolecular nuclear vibrational excitation to L(E).
(5) The mean linewidth (FWHM), $\tilde{\Gamma}$ , which is obtained by averaging the linewidths ${\Gamma_{a}}$ of the individual microcanonical subspectra. As this averaging process does not incorporate the effects of the distribution of the spectral shifts, $\tilde{\Gamma}$ can be considered as a mean homogeneous linewidth. In general, we expect that $\tilde{\Gamma}<\Gamma$ is due to the contribution of $W(\delta v_{a})$ to the linebroadening.

### III. SIZE DEPENDENCE AND ISOMER SPECIFICITY OF SPECTRAL SHIFTS AND LINEWIDTHS
Simulations of the microcanonical homogeneous and the inhomogeneous lineshapes were performed for perylene-Ar $_{n}(n=1-22)$ heteroclusters at 30 K. Typical results for the inhomogeneous lineshapes of several isomer-specific perylene-Ar $_{n}(n=3,5$ , and 8) clusters are portrayed in Fig. 1. The simulated isomer-specific inhomogeneous lineshapes are specified by the overall lineshape, the spectral shifts $\delta v$ (and $\delta v$ ), and the linewidths $\Gamma$ (and $\tilde{\Gamma}$ ), as well as the characteristic intermolecular frequency.

![](./images/813180220948348928_1.jpg)

Fig. 1. Averaged lineshapes of n(n'lm') structural isomers (marked on the figure) of n = 3, 5, and 8 heteroclusters at T = 30 K.

Fig. 2 shows the size- and isomer-dependence of the spectral shifts for perylene-Ar $_{n}(n=4-10)$ clusters. Thegeneral trends of the isomer specificity are:
(1) For a given n the largest red shift corresponds to the nearly equal distribution of ligands, i.e., (n/2|n/2) for even n and ((n-1)/2|(n+1)/2) for odd n.
(2) The smallest red shifts (for a fixed n) correspond toone-sided structures, i.e., one-sided one layer (nl0)and one-sided multilayer $(n_{2}+[n-n_{2}] | 0)$ structures $(n_{2}$  is the number of rare gas atoms in the second layer).
(3) The red spectral shift for the one-sided multilayered structure is smaller than $\delta v$ for the one-layered struc ture.
In Fig. 2 we also included the simulated total inhomogeneous linewidths of the lineshapes. In Fig. 3 we display the size dependence and the isomer specificity of the mean homogeneous linewidths $\tilde{\Gamma}$ at a constant temperature (T=30 K). The $\tilde{\Gamma}$ data reveal the followingfeatures:
(1) For one-sided (nl0) heteroclusters $\tilde{\Gamma}$ shows an overall increase with increasing n. Marked jumps in $\tilde{\Gamma}$ ("magic

Israel Journal of Chemistry 33 1993

![](./images/813180220948348928_2.jpg)

Fig. 2. Simulated isomer-specific spectral shifts of perylene·Ar$_n$ ($n$=4-10) at T=30 K. The isomer structures, which are labelled by (n$_2$+n'lm') (refs 7 and 8), are marked in the order of decreasing |δν| for each $n$. Error bars represent the linewidths $\boldsymbol{\Gamma}$.

![](./images/813180220948348928_3.jpg)

Fig. 3. Isomer specific mean homogeneous linewidths $\boldsymbol{\tilde{\Gamma}}$ of perylene·Ar$_n$ clusters ($n$ = 1-16) at T = 30 K. The isomer structures are marked by (n$_2$+n'lm').

numbers") are exhibited for (4|0) and for (n|0) ($n = 8$ or 9).
(2) For a nearly equal distribution of ligands a weak $n$ dependence of $\tilde{\Gamma}$ is exhibited for the (2|1), (2|2), (3|2), and (3|3) structures, followed by a marked jump of $\tilde{\Gamma}$ for the (4|3) and (4|4) structures.
(3) The sum of the $\tilde{\Gamma}$ values for the one-sided structures (n'|0) and (0|m') constitutes an upper limit for the spectral width of the (n'|m') structure, i.e., $\tilde{\Gamma}$ (n'|m') $\leq$ $\tilde{\Gamma}$ (n'|0) + $\tilde{\Gamma}$ (0|m').
(4) For a fixed composition $n$, the isomer specificity of $\tilde{\Gamma}$ is irregular.

## IV. THE TEMPERATURE DEPENDENCE OF THE LINESHAPES

The temperature dependence of the absorption lineshapes is of interest for the following reasons: (i) establishing relations between nuclear dynamics and spectral properties; (ii) the possible elucidation of the onsets of isomerization processes from absorption lineshapes and linewidths; (iii) the utilization of absorption linewidths as an internal thermometer for the heterocluster temperature. In Fig. 4 we present typical examples for the temperature dependence (over the range $\boldsymbol{T=5-40\ K}$) of the averaged inhomogeneous absorption spectra of perylene·Ar$_n$ for $n=2(2|0)$, $n=5(5|0)$, $n=10(3_2$+7|0), $n=10(5|5)$, and $n=22(22|0))$. These spectral data span the temperature region below the onset of side crossing for the $n=2-10$ clusters, while for the (22|0) cluster side crossing occurs for T > 25 K.³¹ The (2|0), (5|0), and (5|5) clusters maintain the 2D architecture of the adclusters on the M surface(s). 2D $\rightleftarrows$ 3D isomerization sets in for the (3₂+7|0) cluster at 30 K < T < 40 K, while the (22|0) cluster is characterized by a 3D adcluster architecture at all temperatures. The temperature dependence of the spectral shifts $\delta$ν (Fig. 5), the inhomogeneous shifts $\delta$v, the mean homogeneous linewidths $\tilde{\Gamma}$ (Fig. 6), and the inhomogeneous linewidths $\Gamma$ reveal the following features:
(1) The spectral shifts $\delta$v for the averaged inhomogeneous lineshapes are practically identical (mostly within 1-2 cm⁻¹) with the mean value $\overline{\delta v}$ (of the spectral shifts of the homogeneous microcanonical lineshapes.
(2) The temperature dependence of the spectral shifts is weak and nearly linear for all cluster sizes and structures. The temperature dependence of $\delta$v (and $\overline{\delta v}$) does not provide any specific information on the nature of nuclear motion and isomerization.
(3) The nearly linear weak temperature dependence of $\overline{\delta v}$ (Fig. 5) is in accord with the results of previous simulations of the first moment of the absorption lineshapes.
(4) The inhomogeneous linewidths $\Gamma$ are mostly larger than the average homogeneous linewidths, i.e., $\Gamma\geq\tilde{\Gamma}$.

Heidenreich and Jortner/ Spectral Shifts and Linebroadening of Heteroclusters

![](./images/813180220948348928_4.jpg)

Fig. 4. The temperature depen-
dence of the simulated
inhomogeneous absorption
lineshapes of several one-sided
and two-sided perylene-Ar,
heteroclusters at T = 30 K. (a): n
= 2(2|0); (b):n = 5(5|0) and n =
10(5|5);(c):n=10(3,+7|0).(d):n
=22(22|0) with the initial struc-
ture $(3_{3}+7_{2}+12|0)$.

The largest deviations between $\Gamma$ and $\tilde{\Gamma}$ were obtained
for $n=2(2 \mid 0)$ where $\Gamma \simeq 2 \tilde{\Gamma}$ over the temperature
range 10-40 K. For larger one-sided and two-sided
clusters the deviation between $\Gamma$ and $\tilde{\Gamma}$ is smaller, e.g.,
$(\Gamma-\tilde{\Gamma}) / \Gamma$ being $0.05-0.2$ for the $n=5$ and 10 clusters
over the entire temperature range. The difference
between $\Gamma$ and $\tilde{\Gamma}$ originates from the energetic spread
of spectral shifts. The overall temperature dependence
of $\Gamma$ and $\tilde{\Gamma}$ is similar.

(5) The temperature dependence of $\Gamma$ and $\tilde{\Gamma}$ for small
$2(2 \mid 0)$ and medium-sized $10(3_{2}+7 \mid 0)$ one-sided clus-
ters reveals a strong, superlinear temperature depen-
dence. This pattern is distinct from the temperature
dependence of the second central moments, eq 2.6
(i.e., the dispersion of the lineshape), which are given
by $^{24,55} \Delta^{2} \propto T$. A heuristic argument based on Kubo's
theory $^{44-46}$ will imply that the mean linewidths are given
in the fast modulation limit by $\tilde{\Gamma} \propto \Delta^{2}$, i.e., $\tilde{\Gamma} \propto T$ and
in the slow modulation limit by $\tilde{\Gamma} \propto \Delta$, i.e., $\tilde{\Gamma} \propto T^{1 / 2}$.
The difference between the superlinear temperature
dependence of $\tilde{\Gamma}$ for some one-sided clusters and the
predictions of Kubo's theory indicates that the
contribution of nuclear dynamics to $\tilde{\Gamma}$ in $M \cdot A_{n}$
heteroclusters is more complex.

(6) The structures $(5 \mid 0)$ and $(5 \mid 5)$ consist of one-sided and
two-sided trapezoidal five-atom adclusters. At low
$(T<10 ~K)$ temperatures the adclusters are clamped in
two distinct configurations, with the trapeze's long
axis being parallel to the perylene long $y$ axis, and
being located between the perylene long $y$ and short $x$
axes, respectively. These two distinct nuclear
configurations give rise to an inhomogeneously
broadened split spectrum at $5 ~K$ with the distinct
lineshapes originating from different trajectories
(Fig. 4). At $T \simeq 10-15 ~K$ the distinct spectral features
merge into a single broader feature, marking the onset

![](./images/813180220948348928_5.jpg)

Fig. 5. The temperature dependence of the mean spectral shifts for several structural isomers (marked on the figure).

![](./images/813180220948348928_6.jpg)

Fig. 6. The temperature dependence of the mean linewidths $\tilde{\Gamma}$ for several structural isomers (marked on the figure).

of interconversion between these configurations. The linewidth increases with increasing temperature in this region. This pattern manifests the onset of correlated in-plane motion of the (5|0) trapezoidal structure at T = 10-15 K, which is consistent with the analysis of the thermal fluctuations parameters for the (3|0) and (7|0) structures.³¹ At $T \geq 20$ K a practical temperature independence of $\tilde{\Gamma}$ (and $\Gamma$) is exhibited. This surprising feature may be due to fast free correlated motion of the trapezoidal adcluster on the perylene surface.

(7) For a large, one-sided (22|0) cluster (which was prepared at 25 K in the $(3_3+7_2+12|0)$ initial structure and then equilibrated at the appropriate temperature), the temperature dependence of $\tilde{\Gamma}$ (and $\Gamma$) in the range T = 10-30K is rather weak, being of the approximate form $\tilde{\Gamma} \propto T^{1/2}$, as expected from nuclear dynamics in the slow modulation limit. In the temperature domain 30-40K an abrupt superlinear increase of $\tilde{\Gamma}$ (and $\Gamma$) with increasing T sets in. In this temperature range $3D \rightleftarrows 2D$ and side-crossing isomerization processes are manifested. The rapid rise of the linewidth is due to the coexistence of a multitude of one-sided multilayered 3D isomers and two-sided 3D isomers, giving rise to additional contributions to inhomogeneous linebroadening.

## V. CONCLUDING REMARKS
The analysis of the temperature dependence of the spectral shifts does not provide information on the nature of nuclear dynamics and isomerization, in agreement with the results of previous simulations of the first spectral moment of $M\cdot A_n$ clusters.⁷·⁸ Previous studies⁷·⁸ have shown that the temperature dependence of the second central moment $\Delta^2$ provides limited information on nuclear and isomerization dynamics. However, the present simulations of the lineshapes and their linewidths clearly reveal that the relation between $\Gamma$ and $\Delta$ is not straightforward for the cluster size domain explored herein. The present simulations indicate that the temperature onset of some isomerization processes may be reflected in the change of linebroadening of the inhomogeneous spectra corresponding to a certain (rigid or nonrigid) structural isomer. The two examples emerging from the present simulations are the onset of correlated surface motion for the (5|0) and (5|5) adclusters at $T \geq 10$ K, which is manifested by the blurring of the inhomogeneous spectrum and setting in of a weakly temperature-dependent linewidth, and the onset of $3D \rightleftarrows 2D$ and side-crossing transitions for (22|0) at T ≃ 30 K, which is revealed by the onset of a strong temperature dependence of the linewidth.

**Acknowledgments.** A.H. is indebted to the Minerva Foundation for granting a postdoctoral fellowship. This research was supported in part by the German-Israeli James Franck Research Program for Laser-Matter Interaction.

Heidenreich and Jortner/ Spectral Shifts and Linebroadening of Heteroclusters

## REFERENCES

(1) Even, U.; Amirav, A.; Leutwyler, S.; Ondrechen, M.J.; Berkovitch-Yellin, Z.; Jortner, J. *Faraday Discuss. Chem. Soc.* 1982, **73**: 153, and references therein.

(2) Leutwyler, S.; Jortner, J. *J. Phys. Chem.* 1987, **91**: 5558, and references therein.

(3) Leutwyler, S.; Bösiger, J. *Chem. Rev.* 1990, **90**: 489, and references therein.

(4) Jortner, J. *Z. Phys. D* 1992, **24**: 247.

(5) Amirav, A.; Even, U.; Jortner, J. *Chem. Phys. Lett.* 1979, **67**: 9.

(6) Amirav, A.; Even, U.; Jortner, J. *J. Chem. Phys.* 1981, **75**: 2489.

(7) Ben-Horin, N.; Bahatt, D.; Even, U.; Jortner, J. *J. Chem. Phys.* 1992, **97**: 6011.

(8) Ben-Horin, N.; Even, U.; Jortner, J.; Leutwyler, S. *J. Chem. Phys.* 1992, **97**: 5296.

(9) Jortner, J. *Ber. Bunsenges. Phys. Chem.* 1984, **88**: 188.

(10) Leutwyler, S.; Bösiger, J. *Z. Phys. Chem. NF* 1987, **154**: 31.

(11) Bösiger, J.; Leutwyler, S. *Phys. Rev. Lett.* 1987, **59**: 1895.

(12) Bösiger, J.; Leutwyler, S. In *Large Finite Systems*; Jortner, J.; Pullman, B., Eds.; Reidel: Dordrecht, 1987, pp. 153-164.

(13) Leutwyler, S.; Bösiger, J. *Faraday Discuss. Chem. Soc.* 1988, **86**: 225.

(14) Bösiger, J.; Knochenmuss, R.; Leutwyler, S. *Phys. Rev. Lett.* 1989, **62**: 3058.

(15) Knochenmuss, R.; Leutwyler, S. *J. Chem. Phys.* 1990, **92**: 4686.

(16) Ben-Horin, N.; Even, U.; Jortner, J. *Chem. Phys. Lett.* 1992, **188**: 73.

(17) Schmidt, M.; Mons, M.; Le Calvé, J. *J. Phys. Chem.* 1992, **96**: 2404.

(18) Hahn, M.Y.; Whetten, R.L. *Phys. Rev. Lett.* 1988, **61**: 1190.

(19) Shalev, E.; Ben-Horin, N.; Even, U.; Jortner, J. *J. Chem. Phys.* 1991, **95**: 3147.

(20) Bösiger, J.; Bombach, R.; Leutwyler, S. *J. Chem. Phys.* 1991, **94**: 5098.

(21) Ben-Horin, N.; Sanderovitch, H.; Kaldor, U.; Even, U.; Jortner, J. *J. Phys. Chem.* 1992, **96**: 1569.

(22) Shalev, E.; Ben-Horin, N.; Jortner, J. *J. Chem. Phys.* 1991, **94**: 7757.

(23) Amirav, A.; Jortner, J. *Chem. Phys.* 1984, **85**: 19.

(24) Ben-Horin, N.; Even, U.; Jortner, J. *J. Chem. Phys.* 1992, **97**: 5988.

(25) Hermine, P.; Parneix, P.; Coutant, B.; Amar, F.G.; Bréchignac, Ph. *Z. Phys. D* 1992, **22**: 529.

(26) Fried, L.E.; Mukamel, S. *Phys. Rev. Lett.* 1991, **66**: 2340.

(27) Fried, L.E.; Mukamel, S. *J. Chem. Phys.* 1992, **96**: 116.

(28) Heidenreich, A.; Jortner, J. *Z. Phys. D*, in press.

(29) Parneix, P.; Amar, F.G.; Bréchignac, Ph. *Z. Phys. D*, in press.

(30) Troxler, T.; Leutwyler, S. *Ber. Bunsenges. Phys. Chem.* 1992, **96**: 1246.

(31) Bahatt, D.; Heidenreich, A.; Ben-Horin, N.; Even, U.; Jortner, J., submitted for publication.

(32) Hobza, P.; Selzle, H.L.; Schlag, E.W. *J. Chem. Phys.* 1991, **95**: 391.

(33) Leutwyler, S. *Chem. Phys. Lett.* 1984, **107**: 284.

(34) Henke, W.E.; Yu, W.; Selzle, H.L.; Schlag, E.W.; Wutz, D.; Lin, S.H. *Chem. Phys.* 1985, **97**: 205.

(35) Kettley, J.C.; Palmer, T.F.; Simons, J.P.; Amos, A.T. *Chem. Phys. Lett.* 1986, **126**: 107.

(36) Amos, A.T.; Palmer, T.F.; Walters, A.; Burrows, B.L. *Chem. Phys. Lett.* 1990, **172**: 503.

(37) Bayliss, N.S. *J. Chem. Phys.* 1950, **18**: 292.

(38) Ooshika, Y. *J. Phys. Soc. Japan* 1954, **9**: 594.

(39) McRae, E.G. *J. Phys. Chem.* 1957, **61**: 562.

(40) Basu, S. *Adv. Quantum Chem.* 1964, **1**: 145.

(41) Amos, A.T.; Burrows, B.L. *Adv. Quantum Chem.* 1973, **7**: 289.

(42) Longuet-Higgins, H.C.; Pople, J.A. *J. Chem. Phys.* 1957, **27**: 192.

(43) Shalev, A.; Ben-Horin, N.; Jortner, J. *Chem. Phys. Lett.* 1991, **177**: 161.

(44) Lax, M. *J. Chem. Phys.* 1952, **20**: 1752.

(45) Kubo, R.; Toyozawa, Y. *Prog. Theor. Phys.* 1955, **13**: 160.

(46) Kubo, R. *Adv. Chem. Phys.* 1969, **15**: 101.

(47) Robertson, G.N.; Yarwood, J. *Chem. Phys.* 1978, **32**: 267.

(48) Rothschild, W.G.; Soussen-Jacob, J.; Bessière, J.; Vincent-Geisse, J. *J. Chem. Phys.* 1983, **79**: 3002.

(49) Thirumalai, D.; Bruskin, E.J.; Berne, B.J. *J. Chem. Phys.* 1985, **83**: 230.

(50) Mukamel, S. *J. Chem. Phys.* 1982, **77**: 173.

(51) Mukamel, S. *Phys. Rep.* 1982, **93**: 1.

(52) Sue, J.; Yan, Y.J.; Mukamel, S. *J. Chem. Phys.* 1986, **85**: 462.

(53) Islampour, R.; Mukamel, S. *Chem. Phys. Lett.* 1984, **107**: 239.

(54) Islampour, R.; Mukamel, S. *J. Chem. Phys.* 1984, **80**: 5487.

(55) Jortner, J.; Ben-Horin, N. *J. Chem. Phys.*, in press.

(56) Leutwyler, S. *J. Chem. Phys.* 1984, **81**: 5480.

(57) Doxtader, M.M.; Mangle, E.A.; Bhattacharya, A.K.; Cohen, S.M.; Topp, M.R. *Chem. Phys.* 1986, **101**: 413.

(58) Schwartz, S.A.; Topp, M.R. *J. Phys. Chem.* 1984, **88**: 5673.

(59) Amos, A.T.; Cohen, S.M.; Ketteley, J.C.; Palmer, T.F.; Simons, J.P. In *Structure and Dynamics of Weak Molecular Complexes*; Weber, A. Ed.; Reidel: Dordecht, 1987, p. 263.

(60) Allen, M.P.; Tildesley, D.J. *Computer Simulations of Liquids*; Clarendon Press: Oxford, 1990.

(61) Evans, D.J.; Murad, S. *Mol. Phys.* 1977, **34**: 327.

(62) Dewar, M.J.S.; Thiel, W. *J. Am. Chem. Soc.* 1977, **99**: 4899.

(63) Dallinga, C.; Toneman, L.H.; Tretteberg, M.M. *Rec. Trav. Chim.* 1967, **795**: 86.

Israel Journal of Chemistry 33 1993