# EFFECTS OF SIMPLE VACANCIES AND DIVACANCIES ON THE PHYSICAL PROPERTIES OF METALS

V. E. Zinov'ev and S. I. Masharov

UDC 537.312

The effects of simple vacancies and divacancies on the electrical and thermal conductivities of metals are calculated. It is shown that, although the concentration of divacancies is usually less than that of simple vacancies, the changes caused in the kinetic coefficients by the two types of vacancies can be comparable.

The effects of point defects on various properties of crystals have recently been the object of intense study, both theoretically and experimentally, because such defects generally cause important changes in physical properties such as the heat capacity, the electrical and thermal conductivities, the thermal emf, etc.

Vacancies are of particular interest among point defects; they exist in any crystal in a state of thermodynamic equilibrium, in a concentration which increases rapidly with increasing temperature, reaching a value of the order of 0.01-1 at.% at sufficiently high temperatures in certain metals. In addition to single or simple vacancies, complexes of two vacancies ("divacancies") or more arise.

Many experimental studies have shown that changes in many of the physical properties of solids, particularly deviations from simple temperature dependences predicted theoretically for the kinetic coefficients, e.g., the resistivity, are due to vacancies and vacancy complexes [1-4]. Theoretical study of the effects of vacancies and vacancy complexes is thus quite pertinent in connection with the high-temperature behavior of solids. Quenching to low temperatures can fix a large number of vacancies in a sample, much larger than the equilibrium number at the given temperature. Low-temperature studies are particularly fruitful for determining the role played by vacancies, since at these temperatures their effects are not masked by other effects, e.g., the anharmonicity of lattice vibrations which is important at high temperatures.

In this paper we will analyze the effects of vacancies and the least complicated vacancy complexes -- divacancies -- on the kinetic properties of metals. Since we are interested in only qualitative results, we can make several simplifying assumptions: we assume the lattice distortion near the vacancies and divacancies to be negligible; we assume that these defects are distributed independently throughout the lattice; and we consider only the interaction between the nearest neighbors in the crystal.

To determine the positions of the simple vacancies and divacancies in the crystal, we specify a set of coefficients h(n) and b(n) in the following manner:

$$
\mathrm{h}(\mathbf{n})=
\begin{cases}
1 & \text{if there is a simple vacancy at the position with radius vector } \mathbf{n}; \\
0 & \text{if this position is filled by an atom or by a vacancy which is part of a divacancy};
\end{cases}
$$

$$
\mathrm{b}(\mathbf{n})=
\begin{cases}
1 & \text{if a vacancy which is part of a divacancy is at the position with radius vector } \mathbf{n}; \\
0 & \text{if this position is filled by an atom or a simple vacancy}.
\end{cases}
$$

We obviously have

$$
h(\boldsymbol{n}) h(\boldsymbol{n}+\boldsymbol{\rho})=0, \quad h(\boldsymbol{n}) b(\boldsymbol{n}+\boldsymbol{\rho})=0, \tag{1}
$$

where $\boldsymbol{\rho}$ is the radius vector corresponding to the nearest-neighbor positions in the lattice.

---

A. M. Gor'kii Urals State University. Translated from Izvestiya VUZ. Fizika, No. 10, pp. 88-93, October, 1969. Original article submitted December 2, 1968.

© 1972 Consultants Bureau, a division of Plenum Publishing Corporation, 227 West 17th Street, New York, N. Y. 10011. All rights reserved. This article cannot be reproduced for any purpose whatsoever without permission of the publisher. A copy of this article is available from the publisher for $15.00.

The Hamiltonian describing the system of conduction electrons which interact with ions undergoing small vibrations about their equilibrium positions in a crystal containing simple vacancies and divacancies is

$$
\begin{aligned}
\hat{H}= & -\frac{\hbar^{2}}{2 m_{e}} \sum_{i} \Delta_{i}+\sum_{i} \sum_{\boldsymbol{n}}[1-h(\boldsymbol{n})-b(\boldsymbol{n})] v\left(\boldsymbol{n}-\boldsymbol{r}_{i}\right) \\
- & \frac{\hbar^{2}}{2 m} \sum_{\boldsymbol{n}}[1-h(\boldsymbol{n})-b(\boldsymbol{n})] \Delta_{n}+\frac{1}{2} \sum_{m, \boldsymbol{n}} \sum_{\kappa, l=1}^{3} V^{\kappa l}(\boldsymbol{m}-\boldsymbol{n})[1-h(\boldsymbol{m}) \\
& -b(\boldsymbol{m})][1-h(\boldsymbol{n})-b(\boldsymbol{n})]\left(u_{m}^{\kappa} u_{m}^{l}-u_{m}^{\kappa} u_{n}^{l}-u_{m}^{l} u_{n}^{\kappa}+u_{n}^{\kappa} u_{n}^{l}\right) \\
& -\sum_{i} \sum_{\boldsymbol{n}}[1-h(\boldsymbol{n})-b(\boldsymbol{n})]\left(\boldsymbol{u}_{i} \cdot \nabla_{i} v\left(\boldsymbol{n}-\boldsymbol{r}_{i}\right).\right.
\end{aligned}
$$

Here the first term gives the kinetic energy of the conduction electrons, the second gives the energy of the interaction between electrons and the field produced by the ions at rest, the third gives the kinetic energy of the vibrating ions, the fourth gives the potential energy of the elastic vibrations of the ions, and the last term gives the energy of the interaction between electrons and the field of elastic vibrations. Here also $m_e$ and m are the electron and ion masses; $v(\mathbf{n}-\mathbf{r}_i)$ is the potential energy of the interaction between the i-th electron and the ion at lattice position having radius vector n; $V^{\kappa l}(\mathbf{m}-\mathbf{n})$ is the elastic-interaction coefficient for atoms at positions m and n; $\mathfrak{u}_{\mathbf{n}}^{\kappa}$ is the $\kappa$-th displacement component of the ion at position n, and $\mathfrak{u}_i$ is the vector showing the displacement of the potential of lattice point $\mathbf{r}_i$ caused by elastic vibrations.

Hamiltonian (2) is written under the assumption that the interaction between atoms is central and that the potential fields of the individual ions are distorted by the vibrations (the Bloch model of deformable ions [5]).

We write $\hat{\mathrm{H}}$ as the sum
$$
\hat{H}=\hat{H}_{0}+\hat{H}^{\prime},
$$
where
$$
\hat{H}_{0}=-\frac{\hbar^{2}}{2 m} \sum_{i} \Delta_{i}+\sum_{i} \sum_{\boldsymbol{n}} \tilde{v}\left(\boldsymbol{n}-\boldsymbol{r}_{i}\right)-\frac{\hbar^{2}}{2 \tilde{m}} \sum_{\boldsymbol{n}} \Delta_{n}+\frac{1}{2} \sum_{m, \boldsymbol{n}} \sum_{\kappa, l} \tilde{V}_{m n}^{\kappa l} u_{m}^{\kappa} u_{n}^{l} ;
$$

$$
\hat{H}^{\prime}=\hat{H}-\hat{H}_{0}.
$$

In Eq. (4),
$$
\tilde{v}\left(\boldsymbol{n}-\boldsymbol{r}_{i}\right)=\left(1-x_{h}-2 x_{b}\right) v\left(\boldsymbol{n}-\boldsymbol{r}_{i}\right) ;
$$

$$
\tilde{m}=\frac{m}{1-x_{h}-2 x_{b}} ;
$$

$$
\tilde{V}_{m n}^{\kappa l}=\left[2\left(x_{h}+2 x_{b}\right)-1\right] V^{\kappa l}(\boldsymbol{m}-\boldsymbol{n}) ;
$$

$$
\tilde{V}_{m m}^{\kappa l}=-\sum_{\boldsymbol{n}} \tilde{V}_{m n}^{\kappa l} ;
$$
and $x_h$ and $x_b$ are the concentrations of simple vacancies and divacancies in the crystal.

We see that $\hat{\mathrm{H}}_0$ is the energy operator describing a system of electrons and a vibrating lattice in a crystal formed by atoms of mass $\tilde{\mathrm{m}}$ producing potential fields $\tilde{\mathrm{v}}$ and related by elastic constants $\tilde{\mathrm{V}}_{\mathrm{mn}}^{\kappa l}$.

Transforming to the second-quantization representation, we find
$$
\hat{H}_{0}=\sum_{\kappa, \sigma} E_{\kappa} a_{\kappa \sigma}^{+} a_{\kappa \sigma}+\sum_{\boldsymbol{q}, j} \hbar \omega_{\boldsymbol{q} j}\left(b_{\boldsymbol{q} j}^{+} b_{\boldsymbol{q} j}+\frac{1}{2}\right),
$$
where $a_{\kappa \sigma}^{+}$and $a_{\kappa \sigma}$ are the creation and annihilation operators for an electron having quasimomentum $\kappa$, energy $\mathrm{E}_{\kappa}$, and spin $\sigma$; $\mathrm{b}_{\mathbf{q} \mathrm{j}}^{+}$and $\mathrm{b}_{\mathbf{q} \mathrm{j}}$ are the creation and annihilation operators for a phonon of the j-th branch having a quasimomentum $\mathbf{q}$; and $\omega_{\mathbf{q} j}$ is the eigenfrequency of this "average" crystal. For $\hat{\mathrm{H}}^{\prime}$ we have
$$
\hat{H}^{\prime}=\hat{H}_{1}^{\prime}+\hat{H}_{2}^{\prime} ;
$$

$$
\hat{H}_{1}^{\prime}=\sum_{\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime}, \sigma} \sum_{\boldsymbol{q}, j}\left\{\frac{2 i}{3} \frac{C}{\sqrt{N}} \sqrt{\frac{\hbar}{2 \tilde{m} \omega_{\boldsymbol{q} j}}}\left(e_{\boldsymbol{q} j} \cdot\left(\boldsymbol{\kappa}^{\prime}-\boldsymbol{\kappa}\right)\right) \delta_{\boldsymbol{\kappa}^{\prime}-\boldsymbol{\kappa}, \boldsymbol{q}} a_{\boldsymbol{\kappa}^{\prime} \sigma}^{+} a_{\boldsymbol{\kappa} \sigma} b_{\boldsymbol{q} j}+\text { Herm. adj. }\right\} ;
\tag{12}
$$

$$
\begin{gathered}
\hat{H}_{2}^{\prime}=\sum_{\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime}, \sigma} w_{\boldsymbol{\kappa} \boldsymbol{\kappa}^{\prime}} a_{\boldsymbol{\kappa} \sigma}^{+} a_{\boldsymbol{\kappa}^{\prime} \sigma}+\sum_{\boldsymbol{q}, \boldsymbol{q}^{\prime}} \sum_{j, j^{\prime}}\left\{C_{j j^{\prime}}\left(\boldsymbol{q}, \boldsymbol{q}^{\prime}\right) b_{\boldsymbol{q} j} b_{\boldsymbol{q}^{\prime} j^{\prime}}+C_{j j^{\prime}}\left(-\boldsymbol{q}, \boldsymbol{q}^{\prime}\right) b_{\boldsymbol{q} j}^{+} b_{\boldsymbol{q}^{\prime} j^{\prime}}\right. \\
+ \text { Herm. adj. }\}+\sum_{\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime} \sigma} \sum_{\boldsymbol{q}, j}\left\{\frac{2 i}{3} \frac{C}{\sqrt{N}} \frac{1}{N} \sqrt{\frac{\hbar}{2 \tilde{m} \omega_{\boldsymbol{q} j}}}\left(e_{\boldsymbol{q} j}\left(\boldsymbol{\kappa}^{\prime}-\boldsymbol{\kappa}\right)\right) F\left(\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime} ; \boldsymbol{q}\right) a_{\boldsymbol{\kappa}^{\prime} \sigma}^{+} a_{\boldsymbol{\kappa} \sigma} b_{\boldsymbol{q} j}+\text { Herm. adj. }\right\}.
\end{gathered}
\tag{13}
$$

Here $\hat{\mathrm{H}}_{1}^{\prime}$ describes the ordinary electron-phonon interaction, during which quasimomentum is conserved, and $\hat{\mathrm{H}}_{2}^{\prime}$ describes the additional interactions in a metal having defects: elastic scattering of conduction electrons [the first term in (13)], the phonon-defect interaction (second term), and electron-phonon scattering in which quasimomentum is not conserved [the last term in (13)]. In Eqs. (12) and (13), $\mathrm{w}_{\kappa \kappa^{\prime}}$ is the matrix element for the elastic scattering of electrons; $\mathrm{e}_{\mathrm{qj}}$ is the polarization vector of the (q, j) normal vibration; $\mathrm{N}$ is the number of atoms per unit volume; $\mathrm{C}$ is a constant characterizing the electron -lattice interaction; and

$$
\begin{gathered}
C_{j j^{\prime}}\left(\boldsymbol{q}, \boldsymbol{q}^{\prime}\right)=\frac{\hbar \tilde{m}}{4 N} \sum_{n} \sum_{\kappa=1}^{3} e_{\boldsymbol{q} j}^{\kappa} e_{\boldsymbol{q}^{\prime} j^{\prime}}^{\kappa} \sqrt{\omega_{\boldsymbol{q} j} \omega_{\boldsymbol{q}^{\prime} j^{\prime}}}\left(\frac{1}{\tilde{m}}-\frac{1-h(\boldsymbol{n})-b(\boldsymbol{n})}{m}\right) \\
× \exp \left[i\left(\boldsymbol{q}+\boldsymbol{q}^{\prime}\right) \boldsymbol{n}\right]+\frac{\hbar}{4 \tilde{m} N} \sum_{\boldsymbol{m}, \boldsymbol{n}} \sum_{\boldsymbol{\kappa}, l} e_{\boldsymbol{q} j}^{\kappa} e_{\boldsymbol{q}^{\prime} j^{\prime}}^{l} \frac{\Delta^{\kappa l}(\boldsymbol{m}, \boldsymbol{n})}{\sqrt{\omega_{\boldsymbol{q} j} \omega_{\boldsymbol{q}^{\prime} j^{\prime}}}}\left[\exp (i \boldsymbol{q} \boldsymbol{m})-\exp (i \boldsymbol{q} \boldsymbol{n})\right]\left[\exp \left(i \boldsymbol{q}^{\prime} \boldsymbol{m}\right)-\exp \left(i \boldsymbol{q}^{\prime} \boldsymbol{n}\right)\right] ; \quad(14)
\end{gathered}
$$

$$
\Delta^{\kappa l}(\boldsymbol{m}, \boldsymbol{n})=V^{\kappa l}(\boldsymbol{m}-\boldsymbol{n})\left|[1-h(\boldsymbol{m})-b(\boldsymbol{m})][1-h(\boldsymbol{n})-b(\boldsymbol{n})]-\left[1-2\left(x_{h}+2 x_{b}\right)\right]\right| ;
\tag{15}
$$

$$
F\left(\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime} ; \boldsymbol{q}\right)=\sum_{\boldsymbol{n}}\left[h(\boldsymbol{n})+b(\boldsymbol{n})-x_{h}-2 x_{b}\right] \exp \left[i\left(\boldsymbol{\kappa}-\boldsymbol{\kappa}^{\prime}+\boldsymbol{q}\right) \boldsymbol{n}\right].
\tag{16}
$$

It is not difficult to see that the diagonal matrix elements of the operator $\hat{H}_{2}'$ averaged over all the defect configurations in the crystal vanish; we can therefore treat this operator as the cause of quantum transitions among the various states defined by the Hamiltonian $\hat{\mathrm{H}}_{0}$. Since the probabilities for these tran-sitions are expressed in terms of various products of the matrix element of the operator $\hat{H}_{2}'$, averaged over the defect configurations (a procedure which always results in coefficients of these matrix elements which contain various powers of the defect concentration, beginning with the first power), we can treat $\hat{H}_{2}'$ as a small perturbation in calculating the kinetic coefficients if we have $\mathrm{x}_{\mathrm{h}}, \mathrm{x}_{\mathrm{b}} \ll 1$, as is always the case in real crystals.

The additional scattering of conduction electrons in a metal having defects gives rise to an additional resistivity; the maximum effect turns out to be due to elastic scattering, which gives rise to a residual resistivity which is independent of the temperature. The defects also cause important changes in the tem-perature-dependent part of the resistivity, especially at low temperatures, at which essentially the entire thermal part of the resistivity turns out to be caused by defects [6].

The resistivity of a metal having simple vacancies and divacancies was calculated by the Ziman vari-ational method [7]. Omitting the details of these calculations, we merely note that an average of the quantity $|F(\kappa, \kappa' ; q)|^{2}$ over all positions of defects in the crystal is required in order to find the probabilities for electron-phonon transitions in which quasimomentum is not conserved; restricting the discussion to the case of metals having few conduction electrons, in which case we have $\kappa, \kappa'<1 / a$ (where $a$ is the lattice con stant), we find

$$
\left|F\left(\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime} ; \boldsymbol{q}\right)\right|^{2}=N\left(x_{h}+2 x_{b}\right)+2 N x_{b} \frac{1}{z} \sum_{\varrho} \cos (\boldsymbol{q} \boldsymbol{\rho}),
\tag{17}
$$

where $z$ is the number of the nearest neighbors. Replacing the sum over nearest positions in (17) by the average value of $\cos (\boldsymbol{q} \boldsymbol{\rho})$ in a sphere of radius $\rho_{0}$, where $\rho_{0}$ is the distance between nearest neighbors, we find

$$
\left|F\left(\boldsymbol{\kappa}, \boldsymbol{\kappa}^{\prime} ; \boldsymbol{q}\right)\right|^{2}=N\left(x_{h}+2 x_{b}\right)+2 N x_{b} \frac{\sin q \rho_{0}}{q \rho_{0}}.
\tag{18}
$$

For the temperature-dependent part of the resistivity of a metal having simple vacancies and divacan-cies, the calculations yield the following results:

a) The resistivity due to electron scattering by phonons in which quasimomentum is conserved is
$$
\begin{align}
\rho_{1}(T) &=\rho_{0}(T), & & T>\Theta; \\
\rho_{1}(T) &=\left[1+6\left(x_{h}+4 x_{b}\right)\right] \rho_{0}(T), & & T<\Theta,
\end{align}
\tag{19}
$$
where $\rho_{0}$ is the resistivity of a defect-free sample, and $\Theta$ is the Debye temperature.

b) The resistivity due to electron scattering by phonons during which quasimomentum is not con- served is
$$
\begin{align}
\rho_{2}(T) &=\left[100\left(x_{h}+2 x_{b}\right)+60 x_{b}\right] \rho_{0}(T), & & T>\Theta; \\
\rho_{2}(T) &=5\left(x_{h}+4 x_{b}\right)\left(\frac{\Theta}{T}\right)^{3} \rho_{0}(T), & & T<\Theta.
\end{align}
\tag{20}
$$

According to Eqs. (19) and (20), electron-phonon scattering not involving quasimomentum conserva- tion is primarily responsible for changes in the resistivity. It also follows from these equations that di- vacancies make an important contribution to the temperature-dependent part of the resistivity if their con- centration is less than that of simple vacancies. For example, with $x_{b} \sim 0.1 x_{h}$, the divacancy contribution is about $25 \%$ of the total increase in the resistivity at high temperatures and about $40 \%$ at low temperatures.

Point defects in the metal cause additional scattering of thermal carriers and thus cause changes in both the lattice and electronic components of the thermal resistivity. The lattice resistivity in ideal crys- tals vanishes very rapidly at low temperatures because the collisions between phonons which result in the thermal resistivity become very rare events. Accordingly, the only mechanism limiting the phonon range at low temperatures in defective crystals is the elastic scattering of these phonons by the static field of the defects, described by the operator $\hat{H}_{2}^{\prime}$ in (13), and here the only defects in the sample are simple vacancies and divacancies. Using the standard approximations of the theory of the thermal conductivity of solids [8], we find from (13) and (15) the probability for elastic scattering of phonons by the static fields of simple vacancies and divacancies:
$$
w\left(q \rightarrow q^{\prime}\right)=\frac{2 \pi}{\hbar} \cdot \frac{342 \hbar^{2} u^{2} q q^{\prime} z^{2}\left(x_{h}+3 x_{b}\right)}{N} N_{q}^{0}\left(N_{q^{\prime}}^{0}+1\right) \delta\left(\hbar \omega_{q}-\hbar \omega_{q^{\prime}}\right).
\tag{21}
$$

Here $u$ is the sound velocity in the ideal crystal, and $N_{\mathrm{q}}^{0}$ is the equilibrium phonon distribution function.

Standard calculations based on probability (21) yield the thermal resistivity
$$
W_{\text {ela }}^{(\Phi)}=\frac{27 \hbar\left(x_{h}+3 x_{b}\right)(k \Theta)^{6} T}{\pi^{4}(\hbar u)^{8} N^{3}} \cdot \frac{I_{8}(\Theta / T)}{I_{4}^{2}(\Theta / T)},
\tag{22}
$$
where $k$ is the Boltzmann constant, and
$$
I_{n}\left(\frac{\Theta}{T}\right)=\int_{0}^{\Theta / T} \frac{x^{n} d x}{\left(e^{x}-1\right)\left(1-e^{-x}\right)}.
\tag{23}
$$

Equation (23) yields $\mathrm{W}_{\text {ela }}^{(\Phi)} \sim \mathrm{T}$ for low temperatures and $\mathrm{W}_{\text {ela }}^{(\Phi)}=$ const for high temperatures; accord- ing to (22), the relative contribution of divacancies to the lattice thermal resistivity is the same at all tem- peratures.

In metals, phonons are also scattered in collisions with conduction electrons; in ideal crystals this leads to a thermal resistivity proportional to $T^{-2}$ for $T<\Theta$ and independent of the temperature for $T>\Theta$. In alloys, the corresponding thermal-resistivity component increases due to the appearance of electron -phonon scattering without quasimomentum conservation [9]. This mechanism leads to a contribution
$$
W_{\text {ph-e }}^{\prime}=\frac{(\pi \hbar)^{3} C^{2} K_{\zeta}^{4} \mathfrak{S} k^{2} \Theta^{6}\left(x_{h}+4 x_{b}\right)}{25(2 \pi)^{9} m N^{4}(\hbar u)^{5}\left(\hbar v_{\zeta}\right)^{2} T^{3}}
\tag{24}
$$
to the lattice thermal resistivity for $T<\Theta$ ( $K_{\zeta}$ and $v_{\zeta}$ are the quasimomentum and velocity of a conduction electron at the Fermi surface, and $\mathfrak{S}$ is the area of the Fermi surface) and a contribution
$$
W_{\text {ph-e }}^{\prime}=\frac{3.5(\pi \hbar)^{3} C^{2} K_{\zeta}^{4} \mathfrak{S} k^{2} \Theta^{3}\left(x_{h}+3 x_{b}\right)}{(2 \pi)^{9} m N^{4}(\hbar u)^{5}\left(\hbar v_{\zeta}\right)^{2}}
\tag{25}
$$
for $T>\Theta$. We see that the role of divacancies in this component of the thermal resistivity turns out to be most important at low temperatures.

The electronic component $W_e$ of the thermal resistivity, due to electron-phonon scattering, can be found from the Wiedemann-Franz law

$$
W_{e}=\frac{\rho}{L T}
$$

for high temperatures (L is the Lorentz number); it is not difficult to see that this law remains valid for metals having simple vacancies and divacancies. At low temperature this component consists of two terms, one of which is proportional to $T^2$ and the other to T. The second term, due to electron-phonon scattering without quasimomentum conservation is

$$
W_{e}^{\prime}=\frac{50 C^{2} K_{c}^{2}\left(x_{i}+4 x_{b}\right) T}{\pi^{4} N^{2} m u^{3}\left(\hbar v_{c}\right)^{2} \mathfrak{S}}.
$$

We thus see that the relative effect of divacancies on the physical properties of metals is displayed to the greatest extent at low temperatures. Low-temperature experiments with quenched samples will appar- ently yield the most information about their role.

## LITERATURE CITED
1. A. C. Damask and G. J. Dienes, Point Defects in Metals, Gordon and Breach, New York (1964).
2. V. A. Pervakov and V. I. Khotkevich, Ukrainsk. Fiz. Zh., 12, 1777 (1967); Studies of Structural De- fects in Crystals [in Russian], Kiev (1965), p. 53.
3. B. F. Ormont, Permanent Intercollegiate Colloquium on Phases of Variable Composition [in Russian], No. 39 (9), Leningrad (1963).
4. Ya. A. Kraftmakher, Dissertation [in Russian], Novosibirsk (1967).
5. H. Bethe and A. Sommerfeld, Electronic Theory of Metals [Russian translation], Moscow (1938).
6. S. I. Masharov, Fiz. Met. i Metallov., 13, 166 (1962).
7. J. M. Ziman, Electrons and Phonons, Oxford University Press, London (1960).
8. G. Leibfried, Microscopic Theory of Mechanical and Thermal Properties of Crystals [Russian trans- lation], FM, Moscow-Leningrad (1963).
9. S. I. Masharov, Fiz. Met. i Metallov., 20, 489 (1966).