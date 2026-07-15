PHYSICAL REVIEW B 93, 165209 (2016)

# Minority carrier blocking to enhance the thermoelectric figure of merit in narrow-band-gap semiconductors

Je-Hyeong Bahk¹,² and Ali Shakouri²

¹Department of Mechanical and Materials Engineering, University of Cincinnati, Cincinnati, Ohio 45221, USA
²Birck Nanotechnology Center, Purdue University, West Lafayette, Indiana 47907, USA

(Received 1 October 2015; revised manuscript received 12 April 2016; published 27 April 2016)

We present detailed theoretical predictions on the enhancement of the thermoelectric figure of merit by minority carrier blocking with heterostructure barriers in bulk narrow-band-gap semiconductors. Bipolar carrier transport, which is often significant in a narrow-band-gap material, is detrimental to the thermoelectric energy conversion efficiency as it suppresses the Seebeck coefficient and increases the thermal conductivity. When the minority carriers are selectively prevented from participating in conduction while the transport of majority carriers is relatively unaffected by one-sided heterobarriers, the thermoelectric figure of merit can be drastically enhanced. Thermoelectric transport properties such as Seebeck coefficient, electrical conductivity, and electronic thermal conductivity including the bipolar term are calculated with and without the barriers based on the near-equilibrium Boltzmann transport equations under the relaxation time approximation to investigate the effects of minority carrier barriers on the thermoelectric figure of merit. For this, we provide details of carrier transport modeling and fitting results of experimental data for three important material systems, Bi₂Te₃-based alloys, Mg₂Si₁₋ₓSnₓ, and Si₁₋ₓGeₓ, that represent, respectively, near-room-temperature (300 K–500 K), midtemperature (600 K–900 K), and high-temperature (>1000 K) applications. Theoretical maximum enhancement of thermoelectric figure of merit that can be achieved by minority carrier blocking is quantified and discussed for each of these semiconductors.

DOI: 10.1103/PhysRevB.93.165209

## I. INTRODUCTION

Thermoelectric energy conversion has drawn great attention over the past few decades as a viable solid-state technology for waste heat recovery and on-chip cooling [1–3]. Recently, human body-heat energy harvesting for powering wearable electronics and medical sensors has emerged as a new promising application of thermoelectrics [4,5]. The energy conversion efficiency of a thermoelectric device is predominantly determined by the material’s dimensionless thermoelectric figure of merit, $zT = S^2\sigma T/(\kappa_{\text{elec}} + \kappa_{\text{lat}})$, where $S$ is Seebeck coefficient; $\sigma$ is electrical conductivity; $T$ is absolute temperature; $\kappa_{\text{elec}}$ and $\kappa_{\text{lat}}$ are electronic and lattice thermal conductivities, respectively; and $S^2\sigma$ in the numerator is called the power factor. The electronic thermal conductivity includes the bipolar thermal conductivity, which becomes significant at low carrier concentrations near the intrinsic regime. Bipolar transport also reduces the magnitude of the Seebeck coefficient, so it is crucial to minimize the bipolar transport in thermoelectrics.

In recent years, significant enhancements of the thermoelectric figure of merit have been achieved mostly by the reduction of the lattice thermal conductivity via increased phonon scatterings at structural defects, interfaces, and grain boundaries in nanostructured materials [6,7]. A very high $zT \sim 2.2$ was recently reported for bulk spark-plasma-sintered Na-doped PbTe:SrTe at 900 K, which was attributed to the significant reduction of lattice thermal conductivity to $\sim$0.5 W/mK by all-scale hierarchical structures in the material [8]. A $zT \sim 2.0$ was achieved at a lower temperature 773 K for Na-doped binary PbTe by further optimizing nanostructures to reduce the lattice thermal conductivity [9]. Recently, a $zT \sim 2.6$ was reported for undoped single-crystal SnSe at 923 K without complex alloying or nanostructuring but only with the intrinsically ultralow lattice thermal conductivity of the crystal [10]. However, more recent work reported that the highest $zT$ for doped polycrystalline SnSe was only 0.6–0.7 [11,12]. Also a theoretical study showed that the actual lattice thermal conductivity could be higher than the value reported in Ref. [10] for the crystalline direction ($b$ axis), along which the highest $zT$ value was achieved, suggesting a further study on the results [13].

Besides these approaches to reducing the lattice thermal conductivity, there have also been several independent strategies proposed for enhancing the power factor, such as the quantum confinement effect in low-dimensional materials [14] (the limitations of this effect were also studied in a recent work. [15]), resonant impurities such as Tl in p-type PbTe to enhance the Seebeck coefficient via distortion of the electronic density of states [16] (see Ref. [17] for the limitations of this effect), band convergence by alloying [18,19], and three-dimensional modulation doping [20]. The electron energy filtering scheme utilizes heterostructure barriers to filter out low-energy carriers from the transport, so the entropy transport per electric current is increased and thus the Seebeck coefficient [21,22]. Recently, solution-processed p-type Sb₂Te₃ with embedded Ag nanoparticles as nonplanar barriers showed a carrier energy filtering effect to enhance the power factor and the figure of merit over a broad temperature range from room temperature to 480 K [23].

None of the aforementioned approaches, however, deals with bipolar transport to enhance the thermoelectric figure of merit. In fact, it is the bipolar transport that limits a thermoelectric material to be useful only below a certain temperature range. Beyond this temperature range, the bipolar transport causes the power factor to suddenly decrease and the electronic thermal conductivity to shoot up rapidly at the same time, deteriorating the thermoelectric conversion efficiency.

*Corresponding author: bahkjg@uc.edu

2469-9950/2016/93(16)/165209(17)
165209-1
©2016 American Physical Society

If the bipolar transport is effectively suppressed, the thermoelectric material can be used over a much wider temperature range with even higher efficiencies. Furthermore, a much lower doping level can be utilized to further enhance the figure of merit with a lower electronic thermal conductivity and a higher Seebeck coefficient due to the suppression of the bipolar effect. Reduction of electronic thermal conductivity is particularly beneficial when the lattice thermal conductivity has already been much reduced, i.e., by increased phonon scatterings in a nanostructured material, so the electronic thermal conductivity was limiting the thermoelectric figure of merit. In addition, utilizing a low doping level will be very helpful to reduce the cost in material synthesis, particularly for the synthesis methods based on solution processes, where a high-level doping is usually very difficult [24].

As proposed in our recent paper [25], heterostructure barriers could be incorporated in a bulk material to effectively suppress the transport of minority carriers. An appropriate band alignment between the matrix and the barrier material is required, so the barriers are prominent only for the minority carriers while negligible for the majority carriers, i.e., with a sufficiently large band offset in the minority carrier band, and a negligible band offset in the majority carrier band. Recently, this proposed scheme of minority carrier blocking with heterostructure barriers has been experimentally demonstrated in the solution-processed PbTe-Ag₂Te heterostructures to enhance the figure of merit by about 40% [26]. In this material, PbTe creates a large barrier in the conduction band of the Ag₂Te matrix to suppress the minority carrier (electron) transport, whereas the relatively small barrier in the valence band ensures smoother transport for holes. Consequently, the Seebeck coefficient has been enhanced toward a larger positive (p-type) value, thereby enhancing the figure of merit. Sizes and interparticle distances of the PbTe nanoparticles were carefully controlled during the synthesis process of the dumbbell-like PbTe-Ag₂Te nanowires to meet the requirements for effective minority carrier blocking. It is noted that minority carrier blocking and electron filtering similarly utilize barriers to enhance thermoelectric properties. The difference, however, is that the filtering scheme utilizes potential barriers in the majority carrier band, while the minority carrier blocking uses barriers in the minority carrier band. Also the filtering effect requires precise energy selection of majority carriers, which is relatively difficult to achieve [22], but the minority carrier blocking only needs sufficiently high barrier heights to completely block the minority carriers.

In this paper, we further investigate the theoretical maximum of the thermoelectric figure of merit enhancement that can be achieved by minority carrier blocking for several state-of-the-art thermoelectric materials. We select one representative material system for each of the three temperature regimes for this study; Bi₂Te₃-based alloys with Sb (p-type) and Se (n-type) for the near-room-temperature range 300–500 K, Mg₂Si₁₋ₓSnₓ for the midtemperature range 600–900 K (PbTe has already been studied in Ref. [25] for this temperature range), and Si₁₋ₓGeₓ for the high-temperature range 1000 K to higher. Detailed carrier transport modeling as well as the fitting results of the experimental data obtained from literature are presented in Appendix. Thermoelectric transport properties are calculated with and without the heterostructure barriers based on the near-equilibrium Boltzmann transport equations under the relaxation time approximation for each of the materials. The thermoelectric figure of merit is then obtained with an assumed lattice thermal conductivity value to identify the theoretical maximum figure of merit by the minority carrier blocking as well as the optimal carrier concentration at a given desired temperature for each of the three material systems.

## II. CARRIER TRANSPORT EQUATIONS

### A. Multinonparabolic bands model and two-carrier transport with barriers

In a typical narrow-band-gap semiconductor, the dispersion relation in each band is highly nonparabolic and thus can be approximated by the modified Kane model [27],

$$
E(1+\alpha E)=\frac{\hbar^{2} k^{2}}{2 m^{*}},\qquad(1)
$$

where $\alpha$ is the nonparabolicity in the unit of $(\mathrm{eV})^{-1}$ and $m^{*}$ is the effective mass of the band. This nonparabolic band model works well over a broad carrier energy range up to 1–2 eV in most of the narrow-band-gap semiconductors under reasonably high fields [27]. Beyond this range, one may need to use the full band structure to calculate the transport properties. Models based on first-principles band calculations and Boltzmann transport theory are also widely employed for thermoelectric carrier transport calculations [28].

In our model, the nonparabolicity can be obtained from the fitting of the density of states as a function of energy obtained by a first-principles electronic band calculation, which is discussed in more detail in Appendix for an example case of Bi₂Te₃. The density of states (DOS) for a nonparabolic band is then given by

$$
\rho_{\mathrm{DOS}}(E)=d \frac{\sqrt{2}\left(m^{*}\right)^{3 / 2}}{\pi^{2} \hbar^{3}} \sqrt{E+\alpha E^{2}}(1+2 \alpha E),\qquad(2)
$$

where $d$ is the valley degeneracy.

One can use the linearized Boltzmann transport equations to calculate the thermoelectric transport properties in the case of two-carrier type transport. All the transport properties are an integral function of the differential conductivity defined as [29],

$$
\sigma_{d}(E)=e^{2} \tau(E) v^{2}(E) \rho_{\mathrm{DOS}}(E)\left(-\frac{\partial f}{\partial E}\right),\qquad(3)
$$

where $\tau$ is the energy-dependent scattering time of the carrier type, which will be discussed in Sec. II D, $v$ is the carrier velocity in one direction in that $v^{2}=2 E(1+$ $\alpha E) /\left(3 m^{*}(1+2 \alpha E)^{2}\right)$, and $f$ is the Fermi-Dirac distribution function. The differential conductivity should be calculated for each of the bands in the corresponding energy coordinate.

The electrical conductivity, the Seebeck coefficient, and the electronic thermal conductivity for one type of carrier are given, respectively, by

$$
\sigma=\sum_{i} \int T_{B, i}(E) \sigma_{d, i}(E) d E,\qquad(4)
$$

$$
S=\sum_{i} \frac{1}{q T} \frac{\int T_{B, i}(E) \sigma_{d, i}(E)\left(E-E_{F, i}\right) d E}{\sigma},\qquad(5)
$$

$$
\kappa_{\mathrm{elec}}=\sum_{i} \frac{1}{q^{2} T} \int T_{B, i}(E) \sigma_{d, i}(E)\left(E-E_{F, i}\right)^{2} d E-S^{2} \sigma T,
\tag{6}
$$

where $\sigma_{d, i}$ is the differential conductivity of the $i$th band of the carrier type and $T_{B, i}(E)$ is the energy-dependent transmission coefficient of the $i$th band. The $\Sigma$ in each of the equations indicates that the contributions from all the bands that belong to the carrier type must be summed to obtain the final transport property.

The transmission coefficient represents the barrier effect in the transport. When there is no barrier in the band, the transmission coefficient is unity. When there are barriers with barrier height $E_{B}$ and width $w_{B}$, the transmission coefficient can be determined by the Wentzel-Kramers-Brillouin (WKB) approximation as [30]
$$
\begin{aligned}
T_{B}= & \frac{4 E\left(E_{B}-E\right)}{E_{B}^{2} \sinh ^{2}\left(2 w_{B} \sqrt{2 m^{*}\left(E_{B}-E\right)} / \hbar\right)+4 E\left(E_{B}-E\right)}, \\
& \left(E<E_{B}\right) \\
= & \frac{4 E\left(E-E_{B}\right)}{E_{B}^{2} \sin ^{2}\left(2 w_{B} \sqrt{2 m^{*}\left(E-E_{B}\right)} / \hbar\right)+4 E\left(E-E_{B}\right)}. \\
& \left(E>E_{B}\right)
\end{aligned}
\tag{7}
$$

Note that (7) describes the transmission over a single barrier. The transmission will return to that of the bulk ($T_{B} \to 1$) if the carriers travel over a sufficiently long distance before encountering another barrier because extensive electron scatterings will cause the distorted carrier energy distribution after the first barrier to return to equilibrium. This imposes a requirement for the interbarrier spacing or the content of barrier material in the matrix. In this transport model, we assume that the average inter-barrier spacing is comparable to the minority carrier mean free path of the matrix, which ensures that the carrier transmission given by (7) is sustained with frequent blockings by barriers between electron-phonon scattering events during the travel in the matrix. Note that our model based on the transmission coefficient described above is not suitable for capturing the transition of the nonequilibrium carrier distribution after a barrier back to equilibrium with the distance of travel. Hence, this near-equilibrium bulk transport model is unable to predict the variation of transport properties with interbarrier spacing. Instead, a nonequilibrium transport theory such as the generalized Boltzmann transport theory or Monte Carlo simulation could be employed to obtain the transport properties varying with barrier spacing. Also, this model assumes that the transport inside the barrier is purely ballistic, so there is no mobility drop through the barriers for majority carriers.

Since we want to suppress the minority carrier transport as much as possible, i.e., $T_{B} \ll 1$, a sufficiently high barrier ($>4-5k_B T$) is required in the minority carrier band. Also, the barrier width must be more than a magnitude larger than the tunneling length $\hbar/\sqrt{2m^{*}(E_{B}-E)}$ to ensure all the minority carriers with energies lower than the barrier height to be effectively blocked ($T_{B} \sim 0$) without tunneling. On the other hand, a negligibly small barrier height is required in the majority carrier band to minimize the barrier effect on the majority carrier transport.

The total electrical conductivity and total Seebeck coefficient in two-carrier transport are obtained by
$$
\sigma=\sigma_{e}+\sigma_{h}, \tag{8}
$$
$$
S=\frac{\sigma_{e} S_{e}+\sigma_{h} S_{h}}{\sigma_{e}+\sigma_{h}}, \tag{9}
$$
where the subscripts $e$ and $h$ denote the partial properties of electrons and holes, respectively. Since the partial Seebeck coefficients of electrons and holes have opposite signs to each other, it is shown from (9) that the magnitude of the total Seebeck coefficient becomes smaller than that of each partial Seebeck coefficient. Consequently, the thermoelectric power factor and figure of merit are reduced due to the bipolar transport despite the slight increase in the total electrical conductivity.

The total electronic thermal conductivity is not only the sum of the partial (unipolar) electronic thermal conductivities of electrons and holes. Another term from the bipolar thermodiffusion effect must be included in the case of two-carrier transport [31]:
$$
\kappa_{\mathrm{elec}}=\kappa_{\mathrm{elect}, e}+\kappa_{\mathrm{elect}, h}+\kappa_{\mathrm{bi}}. \tag{10}
$$

The bipolar electronic thermal conductivity is given by
$$
\kappa_{\mathrm{bi}}=\frac{\sigma_{e} \sigma_{h}}{\sigma_{e}+\sigma_{h}}\left(S_{e}-S_{h}\right)^{2} T. \tag{11}
$$

We will discuss the characteristics of bipolar thermal conductivity in more detail in Sec. II B.

### B. Bipolar thermal conductivity

The total thermal conductivity is the sum of the lattice thermal conductivity and the electronic thermal conductivity such that
$$
\kappa=\kappa_{\mathrm{lat}}+\kappa_{\mathrm{elec}}. \tag{12}
$$

In this paper, the lattice thermal conductivity is not calculated, but instead extracted by subtracting the electronic thermal conductivity calculated by (10) from the measured total thermal conductivity. The obtained lattice thermal conductivity is then assumed to be constant to analyze the variation of the figure of merit with carrier concentration at a given temperature.

According to (11), the bipolar thermal conductivity can be obtained only when both the electron and hole transport are well known for the material: Both the partial electrical conductivities and Seebeck coefficients of electrons and holes must be known. These partial properties cannot be measured separately, but only the total values described in Eqs. (8) and (9) can be measured. Instead, these partial properties can be estimated based on the accurate transport modeling using (4) and (5) for each type of carrier.

At a relative low carrier concentration, i.e., near the nondegenerate limit, the partial Seebeck coefficients of electrons and holes can be approximated, respectively, as [32]
$$
S_{e}=\frac{k_{B}}{e}\left[\frac{E_{F}}{k_{B} T}-\left(r+\frac{5}{2}\right)\right], \tag{13}
$$
$$
S_{h}=-\frac{k_{B}}{e}\left[-\frac{\left(E_{F}-E_{g}\right)}{k_{B} T}-\left(r+\frac{5}{2}\right)\right], \tag{14}
$$

where $E_F$ is the Fermi level referenced to the conduction band edge in the electron energy coordinate, $E_g$ is the band gap, and $r$ is the energy exponent in the energy-dependent relaxation time as in $\tau = \tau_0 E^r$. From (13) and (14), the last factor in the right-hand side of Eq. (11) becomes

$$
(S_e - S_h)^2 T = \frac{k_B^2}{e^2} \left[ \frac{E_g}{k_B T} + (2r + 5) \right]^2 T, \tag{15}
$$

which is nearly constant, independent of the carrier concentration, at least within the concentration range discussed in this paper because $r$ typically does not change much with carrier concentration in that range. Therefore, using the relations, $\sigma_e = ne\mu_e$, $\sigma_h = pe\mu_h$, and $n_i^2 = np$, where $n_i$ is the intrinsic carrier concentration, (11) becomes, as a function of hole concentration $p$, or electron concentration $n$, respectively,

$$
\kappa_{\text{bi}} \propto \frac{p}{bn_i^2 + p^2}, \quad \text{or} \quad \kappa_{\text{bi}} \propto \frac{n}{n_i^2 / b + n^2}. \tag{16}
$$

According to (16), the bipolar thermal conductivity is a bell-shape function with each of the carrier concentrations and has a maximum when $p = bn$ or $\sigma_e = \sigma_h$ at a given temperature.

Also, near the intrinsic regime, $n \approx p \approx n_i$, and using $n_i = (N_c N_v)^{1/2} \exp(-E_g / 2k_B T)$, where $N_c$ and $N_v$ are the effective density of states in the conduction and valence bands, respectively, (11) becomes

$$
\begin{aligned}
\kappa_{\text{bi}} &= \frac{k_B^2 b \mu_p}{e(b + 1)} (N_C N_V)^{1/2} \exp\left( -\frac{E_g}{2k_B T} \right) \\
&\quad \times \left[ \frac{E_g}{k_B T} + \left( 2r + 5 \right) \right]^2 T. \tag{17}
\end{aligned}
$$

Here the last factor at the right-hand side of (17), also shown in Eq. (15), $(E_g / k_B T + 2r + 5)^2 T$, is only slowly varying with $T$ and $E_g$ for narrow-band-gap semiconductors. Therefore, (17) becomes

$$
\kappa_{\text{bi}} \propto \exp\left( -\frac{E_g}{2k_B T} \right), \tag{18}
$$

which indicates that the bipolar thermal conductivity increases exponentially with temperature. This explains the reason that the $zT$ values of most thermoelectric materials significantly drop as temperature rises beyond the material's working temperature range above room temperature, where the phonon drag [32] is typically insignificant. Equation (18) also suggests that this detrimental bipolar effect can be delayed at a later temperature if the band gap can be increased, i.e., via alloying. Furthermore, $N_c$ ($N_v$) shown in Eq. (17) is proportional to $(m_e^{*})^{3/2}$ [$({m_h^{*}})^{3/2}$]. Thus, by reducing the effective masses, i.e., through compositional changes, the bipolar thermal conductivity can be reduced [33]. However, it may not be easy to find a suitable material composition with appropriate band structures. Instead, we propose in this work to simply add heterostructure barriers to modify the carrier transport and effectively suppress the bipolar effect in an already established material composition.

### C. Carrier concentrations and Hall coefficient
When there are multiple bands participating in the conduction, which is often true for most of the narrow-band-gap thermoelectric materials at high temperatures, the electron concentration $n$ and the hole concentration $p$ are obtained by summing each band's carrier concentration as

$$
n = \sum_i \int_0^\infty \rho_{\text{DOS},i}(E) f_i(E) dE, \tag{19}
$$

$$
p = \sum_j \int_0^\infty \rho_{\text{DOS},j}(E) f_j(E) dE, \tag{20}
$$

where $\rho_{\text{DOS},i}$ is the density of states of the $i$th conduction band, and $f_i(E) = 1 / \{1 + \exp[(E - E_{F,i}) / k_B T]\}$ is the Fermi-Dirac distribution function for the $i$th conduction band with the Fermi level $E_{F,i}$ referenced to the band edge of the $i$th band. For the valence bands, an index $j$ is used. Note that the energy integrals in Eqs. (19) and (20) are performed for each band with energy referenced to the corresponding band edge. So the Fermi level of each band must be converted to its relative position from the specific band edge in the integrals, i.e., $E_{F,i} = E_F - E_{c,i}$, and $E_{F,j} = E_{v,j} - E_F$, where $E_{c,i}$, $E_{v,j}$, and $E_F$ are, respectively, the $i$th conduction band edge, the $j$th valence band edge, and the Fermi level positions in the universal electron energy coordinate.

The carrier concentrations are typically measured using the Hall effect experiment. For single carrier-type transport, the carrier concentration is easily obtained from $n$ or $p = 1/(q R_H)$, where $R_H$ is the Hall coefficient and $q$ is $-e$ for electrons and $+e$ for holes. However, in the case of two-carrier-type transport, where both electrons and holes are participating in the conduction, analysis of the Hall effect results is no longer straightforward because the Hall coefficient becomes a function of both carrier concentrations as well as their mobilities, so there are four unknowns. One may perform the Hall-effect measurements with varying magnetic field to extract all these four quantities [34]. Otherwise, it is possible to extract both electron and hole concentrations by simultaneously fitting the Seebeck coefficient and the electrical conductivity using the Boltzmann transport equations presented in Sec. II B if the band structure and the scattering characteristics of the material are readily known, because then the only adjustable parameter for the fitting is the Fermi level. Additional Hall-effect measurements may be helpful in case there are uncertainties in the band structure and scattering information for the material. The Hall coefficient in the case of two-carrier-type transport under the limit of weak magnetic field is given by

$$
R_H = \frac{1}{e} \frac{p - n b^2}{(p + n b)^2}, \tag{21}
$$

where $b = \mu_e / \mu_h$ is the mobility ratio between electron and hole.

### D. Energy-dependent scattering time
In most of the start-of-the-art thermoelectric materials including the three kinds of materials simulated in this paper, the predominant electron scattering mechanism is the acoustic phonon deformation potential scattering [22,35-37]. The energy-dependent carrier scattering time by acoustic phonon

deformation potential for a nonparabolic band is given by
$$
\tau_{A C}(E)=\frac{\pi \hbar^{4} C_{l}\left(E+\alpha E^{2}\right)^{-1 / 2}}{\sqrt{2}\left(m_{d}^{*}\right)^{3 / 2} k_{B} T D_{a}^{2}(1+2 \alpha E)}\left[(1-A)^{2}-B\right]^{-1},
\tag{22}
$$
where $C_{l}$ is the elastic constant, $m_{d}^{*}$ is the density of states effective mass for a single valley, $D_{a}$ is the acoustic phonon deformation potential, $A=\alpha E(1-K) /(1+2 \alpha E)$, and $B=$ $8 \alpha E(1+\alpha E) K /\left[3(1+2 \alpha E)^{2}\right]$. $K$ is the ratio between the deformation potentials of the valence band and conduction band.

In addition to the acoustic phonon scattering, important scattering mechanisms to consider for these materials are the polar optical phonon scattering, the ionized impurity scattering, and the short-range defect scattering. These scatterings are typically much weaker than the acoustic phonon scattering, but may be necessary to include in the calculations to fine tune the mobility. In particular, the ionized impurity and defect scatterings can be very significant in nanostructured materials where nonperfect crystalline structures are purposely created. The scattering time by polar optical phonons (POP) with screening is given by [36]
$$
\tau_{\mathrm{POP}}(E)=\frac{\hbar^{2} E^{r_{\mathrm{POP}}} F^{-1}}{\left(2 m_{d}^{*}\right)^{1 / 2} e^{2} k_{B} T\left(\varepsilon_{\infty}^{-1}-\varepsilon_{0}^{-1}\right)(1+2 \alpha E)}, \quad(23)
$$
where $\varepsilon_{\infty}$ and $\varepsilon_{0}$ are the high-frequency and static permittivity values, respectively, and
$$
\begin{aligned}
F= & 1-\delta_{\infty} \ln \left(1+\delta_{\infty}^{-1}\right)-\frac{2 \alpha E(1+\alpha E)}{(1+2 \alpha E)^{2}} \\
& \times\left[1-2 \delta_{\infty}+2 \delta_{\infty}^{2} \ln \left(1+\delta_{\infty}^{-1}\right)\right]
\end{aligned}
$$
and $\delta_{\infty}=\hbar^{2} /\left(8 m_{d}^{*} r_{\infty}^{2} E\right). r_{\infty}$ is the high-frequency screening length given by $1 / r_{\infty}^{2}=\left(e^{2} / \varepsilon_{\infty}\right) \int_{0}^{\infty}\left(-\partial f_{0} / \partial E\right) \rho_{\mathrm{DOS}}(E) d E$, and $r_{\mathrm{POP}}$ is the energy exponent of the polar optical phonon scattering, which is an adjustable parameter, typically slightly less than 0.5 [36].

The ionized (Coulomb potential) impurity scattering time is given by [37]
$$
\begin{aligned}
\tau_{\mathrm{II}}(E)= & \frac{16 \sqrt{2 m_{d}^{*}} \pi \varepsilon_{0}^{2}\left(E+\alpha E^{2}\right)^{3 / 2}}{N_{\mathrm{II}} e^{4}(1+2 \alpha E)} \\
& \times\left[\ln \left(1+\delta_{0}^{-1}\right)-\frac{\delta_{0}}{1+\delta_{0}}\right]^{-1},
\end{aligned}
$$
where $N_{\text {II }}$ is the ionized impurity density and $r_{0}$ is the static screening length given by $1 / r_{0}^{2}=$ $\left(e^{2} / \varepsilon_{0}\right) \int_{0}^{\infty}\left(-\partial f_{0} / \partial E\right) \rho_{\mathrm{DOS}}(E) d E$. Note that $N_{\text {II }}$ counts not only the impurities that are ionized but also all the charged defects and vacancies that create Coulomb potential around them. To the first-order approximation, $N_{\text {II }}$ is proportional to the carrier density, and we define the compensation ratio $r_{c}$ as the proportionality factor as in $r_{c}=N_{\text {II }} / n$ in the case of $\mathrm{n}$ type. We use the compensation ratio as a fitting parameter.

The short-range (non-Coulomb) defect scattering time is given by [37]
$$
\tau_{\mathrm{SD}}(E)=\frac{\pi \hbar^{4}\left(E+\alpha E^{2}\right)^{-1 / 2}}{\sqrt{2}\left(m_{d}^{*}\right)^{2 / 3} N_{V} U_{V}^{2}(1+2 \alpha E)}\left[(1-A)^{2}-B\right]^{-1},
\tag{25}
$$
where $N_{V}$ is the nonionized defect density and $U_{V}$ is the short-range potential of the defects.

As shown in Eqs. (24) and (25), these two defect or impurity scatterings have distinct energy dependencies, i.e., $\tau_{\mathrm{II}} \sim E^{3 / 2}$ and $\tau_{\mathrm{SD}} \sim E^{-1 / 2}$. The spatially slowly varying Coulomb potential around the ionized impurities prefers scattering low-energy or low-frequency carriers, whereas the sharp potential barrier by the short-range defects prefers scattering high-energy or high-frequency carriers [38]. Appropriate balance between the intensities of the two scattering mechanisms ensures a good fitting of the electrical conductivity and Seebeck coefficient over a wide temperature range because the transport properties are sensitive to the energy dependency of carrier scattering.

With the assumption that the different scattering events are independent of each other, the total energy-dependent scattering time can be obtained by
$$
\frac{1}{\tau(E)}=\frac{1}{\tau_{\mathrm{AC}}(E)}+\frac{1}{\tau_{\mathrm{POP}}(E)}+\frac{1}{\tau_{\mathrm{II}}(E)}+\frac{1}{\tau_{\mathrm{SD}}(E)}.
\tag{26}
$$

## III. RESULTS AND DISCUSSION

### A. $Bi_2Te_3$ alloys
Since the early boom of thermoelectrics research in the 1950s, $Bi_2Te_3$ has remained the best thermoelectric material with high $zT \sim 1$ near room temperature. Recently, nanostructured bulk $Bi_2Te_3$ alloys that were hot pressed from ball-milled nanopowder showed enhanced $zT$ via reduced thermal conductivity $(\sim 1 \mathrm{~W} \mathrm{~m}^{-1} \mathrm{~K}^{-1})$. Poudel *et al.* [39] reported $zT \sim 1.4$ for nanostructured p-type $Bi_{0.5}Sb_{1.5}Te_3$ at $\sim 400 \mathrm{~K}$. For n type, alloys with Se, i.e., $Bi_2(Te_{1-x}Se_x)_3$, showed highest $zT \sim 1$ at $350-400 \mathrm{~K}$ [40]. However, these $zT$ values decreases substantially as temperature rises beyond this temperature range due to the bipolar effect. At $500 \mathrm{~K}$ and beyond, the $zT$ value of p-type $Bi_{0.5}Sb_{1.5}Te_3$ reduces below 1.0 and that of n-type $Bi_2Te_{2.7}Se_{0.3}$ below 0.6.

Typically no particular dopant impurities are added to dope $Bi_2Te_3$ alloys. Instead, the compositional variation of stoichiometry affects the carrier concentration drastically because the vacancies and antisite defects (Te occupying the Bi site or Bi occupying the Te site) in the crystal are responsible for charge donation in $Bi_2Te_3$ alloys [41,42]. It has been reported that ball-milling conditions can also affect the antisite defect densities and thus change the carrier concentration in both p-type and n-type $Bi_2Te_3$ alloys [43,44].

We have successfully fitted the experimental data of the high $zT$ n- and p-type $Bi_2Te_3$ alloys from Refs. [39,40] using our electron transport model. Details about the modeling are presented in Appendix A. Based on the theory, we calculated the thermoelectric transport properties with and without minority carrier blocking barriers in the material as a function of carrier concentration. First results shown in Fig. 1 are for n-type $Bi_2Te_{2.7}Se_{0.3}$ at $500 \mathrm{~K}$. Here 20-nm-wide barriers with a $10k_B T$ barrier height for the minority carriers (holes) and a 0-eV barrier height for the majority carriers (electrons) were assumed for the calculations. This one-sided barrier structure showcases the ideal minority carrier blocking, in which more than 99% minority carriers are blocked by the barriers while majority carriers remain unaffected.

![](./images/814530145158168576_1.jpg)

FIG. 1. Calculated (a) electronic thermal conductivity, (b) electrical conductivity, (c) Seebeck coefficient, and (d) power factor of n-type $Bi_2Te_{2.7}Se_{0.3}$ with and without minority carrier (hole) blocking as a function of electron concentration at 500 K. Barriers with 20-nm width and $10k_BT$ barrier height in the valence bands were used for the simulation of minority carrier blocking.

As shown in Fig. 1(a), the bipolar thermal conductivity is significantly high in the electron concentration range $10^{18}-10^{19}\ \text{cm}^{-3}$, reaching the maximum $1.5\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ at $4\times 10^{18}\ \text{cm}^{-3}$ electron concentration at 500 K. Note that this electron concentration $(4\times 10^{18}\ \text{cm}^{-3})$ corresponds to hole concentration $\sim 1\times 10^{19}\ \text{cm}^{-3}$ in this material, and with 2.5 times higher mobility for electrons than holes, the partial electrical conductivity of electrons become equal to that of holes to have the maximum bipolar thermal conductivity at this concentration as discussed in Sec. II C. This is also the minimum electrical conductivity point. [Fig. 1(b)] Furthermore, the Seebeck coefficient is very small, only $-8\ \mu\text{V}\ \text{K}^{-1}$, at this concentration [Fig. 1(c)] because the partial Seebeck coefficients of electrons and holes almost cancel each other out according to (12). As a result, the power factor and $zT$ are extremely small at this concentration.

When the barriers are incorporated, however, the bipolar thermal conductivity is largely suppressed, and the total electronic thermal conductivity mostly comes from the unipolar thermal conductivity of the majority carriers (electrons in this case), which is proportional to the majority carrier concentration following the Wiedemann-Franz relation. The magnitude of Seebeck coefficient also enhances in the case with barriers because the otherwise canceling-out hole contribution is removed. The magnitude of Seebeck coefficient increases monotonically with decreasing concentration just like the case of a unipolar transport [Fig. 1(c)]. As one can see in Fig. 1(d), the resulting power factor is greatly enhanced near the intrinsic region $(10^{18}-10^{19}\ \text{cm}^{-3}$ electron concentration range) compared to the bulk case at the same concentration due to the suppression of the minority carrier contribution by barriers. Note that in this intrinsic region, the power factor is still lower than the maximum power factor occurring at $8\times 10^{19}\ \text{cm}^{-3}$ electron concentration [Fig. 1(d)], because the concentration is way much off optimal. But combined with the reduced electronic thermal conductivity, $zT$ could be enhanced beyond the maximum value of a bulk.

![](./images/814530145158168576_2.jpg)

FIG. 2. Calculated figure of merit $zT$ of n-type $Bi_2Te_{2.7}Se_{0.3}$ with and without minority carrier blocking as a function of electron concentration at 400 K and 500 K. The same barrier size and heights used in Fig. 1 were used for the calculations. A constant lattice thermal conductivity of $0.5\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ was assumed.

Figure 2 shows $zT$ with and without the minority carrier blocking as a function of electron concentration for the n-type $Bi_2Te_{2.7}Se_{0.3}$ at two temperatures, 400 K and 500 K. The lattice thermal conductivity was assumed to be $0.5\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$, which was the value extracted from the experimental thermal conductivity data reported in Ref. [39]. (See Appendix A

for details.) Without the barriers, bulk $Bi_2Te_{2.7}Se_{0.3}$ has a maximum $zT \sim 1.0$ at electron concentration $3 \times 10^{19}\ \text{cm}^{-3}$ (hole concentration $1.2 \times 10^{18}\ \text{cm}^{-3}$) at 500 K. This maximum $zT$ value is drastically enhanced to 1.7 by the minority carrier blocking at a lower electron concentration $1 \times 10^{19}\ \text{cm}^{-3}$. At 400 K, the enhancement is a bit lower; about 27% enhancement from $zT = 1.1$ for bulk to 1.4 with minority carrier blocking. Smaller enhancement at a lower temperature is anticipated because the bipolar thermal conductivity decreases overall as temperature lowers according to (21), so the enhancement through bipolar thermal conductivity reduction becomes weaker.

In the case of p-type $Bi_{0.5}Sb_{1.5}Te_3$, the story is similar, and the effect differs only quantitatively. As shown in Fig. 3(a), the bipolar thermal conductivity becomes as high as $1.6\ \text{W m}^{-1}\text{K}^{-1}$ at hole concentration $6 \times 10^{18}\ \text{cm}^{-3}$ (electron concentration $2.1 \times 10^{18}\ \text{cm}^{-3}$) at 500 K. As the hole concentration increases after this point, the bipolar thermal conductivity gradually decreases, but the unipolar electronic thermal conductivity rises up instead. Due to the opposite behaviors of these two quantities, total electronic thermal conductivity becomes to have a minimum value of $0.9\ \text{W m}^{-1}\text{K}^{-1}$ at hole concentration $4 \times 10^{19}\ \text{cm}^{-3}$ (electron concentration $2.8 \times 10^{17}\ \text{cm}^{-3}$). However, if the minority carriers are blocked by the barriers, the electronic thermal conductivity comes mostly from the unipolar conduction of majority carriers and thus monotonically decreases with decreasing hole concentration. Near intrinsic, the total electronic thermal conductivity becomes less than $0.1\ \text{W m}^{-1}\text{K}^{-1}$ as shown in Fig. 3(a). Due to the same reason, the Seebeck coefficient monotonically increases with decreasing hole concentration in the case when the barriers block the electron (minority carrier) transport [Fig. 3(c)]. But the electrical conductivity keeps decreasing at the same time [Fig. 3(b)], so because of that the power factor decreases with decreasing hole concentration but still in a much slower pace than the bulk case [Fig. 3(d)].

Figure 4 shows the calculated figure of merit $zT$ of p-type $Bi_{0.5}Sb_{1.5}Te_3$ as a function of hole concentration at 400 K and 500 K with and without the minority carrier blocking barriers. The same lattice thermal conductivity $(0.5\ \text{W m}^{-1}\text{K}^{-1})$ used previously for n-type $Bi_2Te_{2.7}Se_{0.3}$ was used for the p-type. Overall, p-type bulk $Bi_{0.5}Sb_{1.5}Te_3$ shows higher $zT$ than that of n-type bulk $Bi_2Te_{2.7}Se_{0.3}$ at the same majority carrier concentration. This is because of the lower electronic thermal conductivity of the p-type than that of the n-type with relatively similar power factors for the two materials at the same majority carrier concentration. The higher electronic thermal conductivity for the n-type mainly comes from its higher carrier (electron) mobility than the hole mobility of the p-type material. So the highest $zT$ value achievable for p-type bulk $Bi_{0.5}Sb_{1.5}Te_3$ is found to be $\sim$1.2 at hole concentration of $6 \times 10^{19}\ \text{cm}^{-3}$ at 500 K. (Recall that the maximum $zT$ for n-type was $\sim$1.0.). This $zT$ value can be enhanced to 2.0 when the minority carrier blocking takes place with the 20-nm barriers as shown in Fig. 4 for the p-type $Bi_{0.5}Sb_{1.5}Te_3$, which is about $\sim$68% enhancement, a similar enhancement as the n-type $Bi_2Te_{2.7}Se_{0.3}$ had at the same temperature 500 K. At 400 K, the bulk material without the barriers has maximum $zT \sim 1.4$, which is higher than that of 500 K mainly because of the lower bipolar thermal conductivity at the lower temperature. (Recall that the bipolar thermal conductivity increases exponentially with temperature.) However, $zT$ enhancement by minority carrier blocking is smaller at 400 K; the maximum $zT$ is enhanced from 1.4 to 1.74 at 400 K, which is about 24% enhancement.

![](./images/814530145158168576_3.jpg)

FIG. 3. Calculated (a) electronic thermal conductivity, (b) electrical conductivity, (c) Seebeck coefficient, and (d) power factor of p-type $Bi_{0.5}Sb_{1.5}Te_3$ with and without minority carrier (electron) blocking as a function of hole concentration at 500 K. Barriers with 20-nm width and $10k_BT$ barrier height in the conduction bands were used for the simulation of minority carrier blocking.

![](./images/814530145158168576_4.jpg)

FIG. 4. Calculated figure of merit $zT$ of p-type ${\text{Bi}}_{0.5}{\text{Sb}}_{1.5}{\text{Te}}_{3}$ with and without minority carrier blocking as a function of hole concentration at 400 K and 500 K. The same barrier size and height used in Fig. 3 were used for the calculations. A constant lattice thermal conductivity of $0.5\ \text{W}\ {\text{m}}^{-1}\ {\text{K}}^{-1}$ was assumed.

In addition, we conducted a later study to investigate the effects of barrier height and thickness on the figure of merit of the p-type ${\text{Bi}}_{0.5}{\text{Sb}}_{1.5}{\text{Te}}_{3}$. Figure 5 shows the bipolar thermal conductivity and the figure of merit of this material with varying barrier height and thickness at $T=500\ \text{K}$. It is shown that as the barrier height decreases from $10k_{B}T$ to $5k_{B}T$ and to $2k_{B}T$, the reduction of bipolar thermal conductivity by barriers is steadily lessened, confirming that the minority carrier blocking is less effective with lower barrier height. Although the percentage of minority carriers (electron) that have energy above $5k_{B}T$ is very small, i.e., less than 4% among the total electron concentration of $1.3\times 10^{18}\ {\text{cm}}^{-3}$ at hole concentration of $1\times 10^{19}\ {\text{cm}}^{-3}$, for example, the magnitude of the Seebeck coefficient of electrons is relatively large ($\sim -800\ \mu\text{V/K}$) due to the barriers, so the bipolar thermal conductivity becomes as large as 0.2 W/mK at this doping level, compared to the almost completely suppressed bipolar thermal conductivity with $105k_{B}T$ barrier height as shown in Fig. 5(a). Consequently, the figure of merit is reduced by more than 20% at this hole concentration as the barrier height is lowered from $10k_{B}T$ to $5k_{B}T$ [Fig. 5(b)]. Similarly, a significant reduction of $zT$ is found when the barrier height is lowered from $5k_{B}T$ to $2k_{B}T$, due to the much reduced effectiveness of the minority carrier blocking on the suppression of bipolar thermal conductivity.

![](./images/814530145158168576_5.jpg)

FIG. 5. Variation of (a) bipolar thermal conductivity and (b) figure of merit with barrier height ($E_{B}$) and barrier width in nm in the minority carrier band for p-type ${\text{Bi}}_{0.5}{\text{Sb}}_{1.5}{\text{Te}}_{3}$ at 500 K. In the figure of merit calculations, lattice thermal conductivity is assumed to be $0.5\ \text{W}\ {\text{m}}^{-1}\ {\text{K}}^{-1}$.

However, the impact of the minority carrier blocking on $zT$ is much less sensitive to the width of barriers. As shown in Fig. 5(b), a 1 nm barrier width is found as effective as a 20 nm width in reducing the bipolar thermal conductivity when the barrier height is higher than $5k_{B}T$. This is because the tunneling depth for such a high barrier height is very shallow, $\sim 0.6$ nm, much shorter than the barrier width, so most of minority carriers cannot tunnel through the barriers. This suggests that a broad range of barrier sizes from a few nm to tens of nm can be incorporated for the minority carrier blocking without a loss in $zT$ enhancement. We find that this statement also applies to the other two material systems discussed below, ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$ and ${\text{Si}}_{1-x}{\text{Ge}}_{x}$.

### B. ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$

${\text{Mg}}_{2}\text{Si}$ and other silicides have been recently attracting great attention as a viable thermoelectrics for midtemperature applications due to their various advantages such as material stability, nontoxicity, and low cost with abundant elements [45]. In particular, its alloys with Sn, ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$ solid solutions, have been one of the main research foci in the field because of their tunable band structure with Sn content to achieve high $zT$. ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$ has its two conduction bands converging with each other for Sn content $x=0.6-0.7$, which is known as one of the important ingredients for a large Seebeck coefficient [35]. It has been reported that n-type ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$ with $x=0.6-0.7$ exhibited $zT=1.0-1.5$ at 700 K–900 K [19,46,47]. However, the high bipolar thermal conductivity prevented further improvement of $zT$ for this material.

For analysis of the experimental results, we have recently developed an electron transport model for both n-type and p-type ${\text{Mg}}_{2}{\text{Si}}_{1-x}{\text{Sn}}_{x}$ solid solutions ($0\leqslant x\leqslant 1$) and successfully fitted most of the key experimental data from literature using the theory [35]. Herein we reuse the band structure and scattering parameter information obtained for the material system in Ref. [35] and add the barrier effect in the model to assess the impact of minority carrier blocking on the thermoelectric properties of ${\text{Mg}}_{2}{\text{Si}}_{0.4}{\text{Sn}}_{0.6}$ ($x=0.6$) as discussed below.

![](./images/814530145158168576_6.jpg)

FIG. 6. Calculated (a) electronic thermal conductivity, (b) electrical conductivity, (c) Seebeck coefficient, and (d) power factor of Mg₂Si₀.₄Sn₀.₆ with and without minority carrier blocking as a function of electron concentration (bottom x axis) and hole concentration (top x axis) at 900 K. Barriers with 20-nm width and $10k_BT$ barrier height in the conduction bands ($e$-barrier) for p-type or valence bands ($h$-barrier) for n-type were used for the simulation of minority carrier blocking for each type of carriers.

Figure 6 presents the calculation results for the thermoelectric properties of Mg₂Si₀.₄Sn₀.₆ with the minority carrier blocking over a wide carrier concentration range encompassing both n-type and p-type regimes at 900 K. As one may expect at such an elevated temperature, the electronic thermal conductivity of Mg₂Si₀.₄Sn₀.₆ at 900 K is found to be much higher than that of Bi₂Te₃ alloys at 500 K that we showed previously in Figs. 1 and 3. Due to the very small band gap of the material $\sim$0.25 eV at this temperature, the bipolar thermal conductivity remains very high above $1\ \text{W m}^{-1}\text{K}^{-1}$ near the intrinsic region ($10^{19}-10^{20}\ \text{cm}^{-3}$ electron concentration range) and peaked as high as $2.8\ \text{W m}^{-1}\text{K}^{-1}$ at $3\times10^{19}\ \text{cm}^{-3}$ electron concentration at this temperature, which is about twice larger than those of the Bi₂Te₃ alloys at 500 K. This large bipolar thermal conductivity is the major limiting factor for the material's $zT$ in this low doping range, because the lattice thermal conductivity for this material has been reduced quite much to be $\sim1\ \text{W m}^{-1}\text{K}^{-1}$ or lower by nanostructuring and alloying [19,35]. The unipolar thermal conductivities of electrons and holes [red curve and blue curve, respectively, in Fig. 6(a)] do not different much from those of Bi₂Te₃ alloys at 500 K at the same carrier concentration; their lower electrical conductivities are compensated by the higher temperature (900 K) because the unipolar thermal conductivity are proportional to both electrical conductivity and temperature according to the Wiedemann-Franz relation. This unipolar thermal conductivity becomes larger than $1\ \text{W m}^{-1}\text{K}^{-1}$ when the majority carrier concentration is sufficiently high for both types of carriers, when the electron concentration is higher than $2\times10^{20}\ \text{cm}^{-3}$, or the hole concentration is higher than $3\times10^{20}\ \text{cm}^{-3}$.

Hence, as seen in Fig. 6(a), the total electronic thermal conductivity cannot be lower than $2\ \text{W m}^{-1}\text{K}^{-1}$ over the entire carrier concentration range because of the conflicting behaviors of the unipolar thermal conductivity and the bipolar thermal conductivity with varying carrier concentration. However, this high minimum of electronic thermal conductivity could be lowered drastically by minority carrier blocking. Due to the suppression of the bipolar transport, the total electronic thermal conductivity can be kept very low, below $0.5\ \text{W m}^{-1}\text{K}^{-1}$ in the carrier concentration range near intrinsic region ($10^{19}-10^{20}\ \text{cm}^{-3}$ electron and hole concentrations). The power factor is also enhanced in this concentration region due to the Seebeck enhancement despite the slight reduction in the electrical conductivity by the barriers [Fig. 6(d)].

As a result, the figure of merit $zT$ of Mg₂Si₀.₄Sn₀.₆ is enhanced quite substantially in this low-carrier-concentration region. Figure 7 displays the $zT$ enhancement by minority carrier blocking for both types of carriers of Mg₂Si₀.₄Sn₀.₆ at 900 K. Here, we inspected the two cases of lattice thermal conductivity: 0.8 and $0.3\ \text{W m}^{-1}\text{K}^{-1}$. Experimentally, the lowest up-to-date lattice thermal conductivity achieved for Mg₂Si₀.₄Sn₀.₆ at $\sim$800 K or higher temperatures is $\sim0.8\ \text{W m}^{-1}\text{K}^{-1}$. Assuming this lattice thermal conductivity value, the bulk maximum $zT$ that can be achieved for n-type Mg₂Si₀.₄Sn₀.₆ is 1.1 at 900 K. This $zT$ value can be enhanced to $\sim$2 at $\sim1\times10^{19}\ \text{cm}^{-3}$ electron concentration by the minority carrier blocking as shown as a blue dotted curve with triangles ($h$-barrier) in Fig. 7. This accounts for about an 80% enhancement. For the p-type material, the enhancement is similar, about 85%, from the bulk maximum $zT=0.7$ to 1.3 by the minority carrier blocking ($e$-barriers) as shown in Fig. 7.

![](./images/814530145158168576_7.jpg)

FIG. 7. Calculated figure of merit $zT$ of ${\rm Mg_2Si_{0.4}Sn_{0.6}}$ with and without minority carrier blocking as a function of electron concentration (bottom $x$ axis) and hole concentration (top $x$ axis) at 900 K. The same barrier size and height used in Fig. 6 were used for the calculations. Electron barriers ($e$-barrier) were used for the minority carrier blocking in the p-type material and hole barriers ($h$-barrier) for the minority carrier blocking in the n-type. Two constant lattice thermal conductivities, 0.8 and $0.3\ {\rm Wm^{-1}K^{-1}}$, were considered for each type.

If the lattice thermal conductivity is further reduced, i.e., to $0.3\ {\rm Wm^{-1}K^{-1}}$ at this temperature, the $zT$ enhancement by minority carrier blocking can be much larger. As shown by the solid curves in Fig. 7, $zT$ for the n-type material can be enhanced above 3 from the bulk maximum 1.3 in the case of $0.3\ {\rm Wm^{-1}K^{-1}}$ lattice thermal conductivity, which is a more than 130% enhancement. For p type, $zT$ can be enhanced above 2.5 from the bulk maximum 0.9, thus a more than 170% enhancement. This exemplifies the fact that the minority carrier blocking can be more effective in enhancing the figure of merit when the lattice thermal conductivity is lower. Note that the lattice thermal conductivity reduction may be achieved simultaneously by the incorporation of heterostructure barriers for minority carrier blocking, because these nanoscale barriers could also effectively scatter phonons if there was a large acoustic mismatch between the two dissimilar materials at the heterointerfaces [8].

At a lower temperature, 700 K, the $zT$ enhancement is expected to be smaller because the bipolar thermal conductivity to be suppressed is already smaller in the bulk due to a larger band gap (0.31 eV) and a lower temperature (700 K) than those at 900 K. The peak value of bipolar thermal conductivity $(1.2\ {\rm Wm^{-1}K^{-1}})$ at 700 K is found to be only $\sim$46% of the 900 K value $(2.6\ {\rm Wm^{-1}K^{-1}})$. Figure 8 presents the calculated $zT$ of ${\rm Mg_2Si_{0.4}Sn_{0.6}}$ with and without minority carrier blocking as a function of carrier concentrations at 700 K. Here we assumed the lattice thermal conductivity to be $0.5\ {\rm Wm^{-1}K^{-1}}$, a slightly higher value than the value $(0.3\ {\rm Wm^{-1}K^{-1}})$ previously used for the calculations at 900 K, because the predominant phonon scattering at these temperatures is the Umklapp scattering, which becomes weaker as temperature decreases, causing the lattice thermal conductivity to increase. Note that this value of lattice thermal conductivity $(0.5\ {\rm Wm^{-1}K^{-1}})$ still remains to be experimentally achieved for this material.

![](./images/814530145158168576_8.jpg)

FIG. 8. Calculated figure of merit $zT$ of ${\rm Mg_2Si_{0.4}Sn_{0.6}}$ with and without minority carrier blocking as a function of electron concentration (bottom $x$ axis) and hole concentration (top $x$ axis) at 700 K. The same barrier size and height used in Fig. 6 were used for the calculations. Electron barriers ($e$-barrier) were used for the minority carrier blocking in the p-type material and hole barriers ($h$-barrier) for the minority carrier blocking in the n-type material. A constant lattice thermal conductivity of $0.5\ {\rm Wm^{-1}K^{-1}}$ was assumed.

As shown in Fig. 8, bulk n-type ${\rm Mg_2Si_{0.4}Sn_{0.6}}$ can achieve maximum $zT\sim1.6$ with electron concentration $\sim1\times10^{20}\ {\rm cm^{-3}}$ at 700 K. This figure of merit can be enhanced to $\sim$2.1 by the minority carrier blocking (blue curve with triangles in Fig. 8), which is an enhancement of about 30%. Similarly for p type, $zT$ is enhanced from the bulk maximum 1.1 to 1.5 by the minority carrier blocking, which is an enhancement of 36%.

### C. ${\rm Si_{1-x}Ge_x}$

Silicon germanium alloys have been actively studied for thermoelectric applications since 1960s and used in many radioisotope thermoelectric generators (RTGs) by NASA for deep space missions since the early 1970s [48–50]. They are particularly suited for space applications due to their unique advantages such as excellent material reliability and thermoelectric properties at high temperatures up to $\sim$1300 K. Until recently, the maximum $zT$ values for SiGe alloys had been $\sim$0.65 for p type and $\sim$1.0 for n type at 1200 K [49,51]. In 2008, Joshi *et al.* [52] reported a large enhancement of $zT$ for p-type B-doped ${\rm Si_{0.8}Ge_{0.2}}$ to achieve $zT\sim1.0$ via reduced lattice thermal conductivity by nanostructuring achieved by the advanced material synthesis method. In the same year, Wang *et al.* [53] from the same group reported an enhanced $zT\sim1.3$ for n-type P-doped ${\rm Si_{0.8}Ge_{0.2}}$ as well as at $\sim$1200 K.

We have modeled the electron transport for both of these p-type and n-type ${\rm Si_{0.8}Ge_{0.2}}$ alloys and successfully fitted the data reported in these recent papers. Details are discussed in Appendix B. Based on the developed electron transport model, we investigated the minority carrier blocking effects in the SiGe alloys. Figure 9 displays the calculation results for

![](./images/814530145158168576_9.jpg)

FIG. 9. Calculated (a) electronic thermal conductivity, (b) electrical conductivity, (c) Seebeck coefficient, and (d) power factor of Si₀.₈Ge₀.₂ with and without minority carrier blocking as a function of electron concentration (bottom x axis) and hole concentration (top x axis) at 1200 K. Barriers with 20-nm width and $10k_BT$ barrier height in the conduction bands ($e$-barrier) for p-type or valence bands ($h$-barrier) for n type were used for the simulation of minority carrier blocking for each type of carriers.

Si₀.₈Ge₀.₂ with and without minority carrier blocking at 1200 K over a wide carrier concentration range encompassing both n-type and p-type regions. Without the minority carrier blocking, the bipolar thermal conductivity has a peak of $1.3\ \text{W m}^{-1}\text{K}^{-1}$ at $6 \times 10^{18}\ \text{cm}^{-3}$ electron concentration or, equivalently, at $6 \times 10^{18}\ \text{cm}^{-3}$ hole concentration. Mobilities for both types of carriers are very close to each other in Si₀.₈Ge₀.₂, so, at very similar carrier densities of electrons and holes, the bipolar thermal conductivity and the electrical conductivity have their minima. The bipolar thermal conductivity is relatively small compared to that of Mg₂Sn₀.₄Si₀.₆ shown in Fig. 6, even though the temperature is higher. This is because the band gap of Si₀.₈Ge₀.₂ at 1200 K is much larger (0.67 eV) than that of Mg₂Sn₀.₄Si₀.₆ (0.25 eV) at 900 K. Therefore, it can be expected that the $zT$ enhancement in this material by the minority carrier blocking might not be as large as in Mg₂Sn₀.₄Si₀.₆. The bipolar effect on Seebeck coefficient is significant only when the electron concentration is below $\sim 5 \times 10^{19}\ \text{cm}^{-3}$ in the n-type material or when the hole concentration is below $\sim 5 \times 10^{19}\ \text{cm}^{-3}$ in the p-type as shown in the middle of Fig. 9(c). Thus, the minority carrier blocking effect is large within these carrier concentration ranges. However, in these carrier concentration ranges, the bulk $zT$ is relatively small because the bulk optimal carrier concentrations for maximum $zT$ are much higher beyond the range. As a result, one can see from Fig. 9(d) that the power factor enhancement by minority carrier blocking is relatively small near the optimal concentrations ($\sim 1 \times 10^{20}\ \text{cm}^{-3}$) for both n- and p-types. Also noted is that at very high carrier concentrations for both p- and n-types [far left and right part, respectively, of Fig. 8(c)], the magnitude of the Seebeck coefficient obtained with the barriers rolls over and starts to decrease when the carrier concentration increases. At such high carrier concentrations and at such a high temperature, a significant portion of the carriers can have energies high enough to go over the barrier height, so the effect of carrier blocking is diminished, resulting in the recurring bipolar effect affecting the transport properties unfavorably.

As shown in Fig. 10, the $zT$ enhancement by minority carrier blocking is relatively small in both n-type and p-type Si₀.₈Ge₀.₂ at 1200 K. If the lattice thermal conductivity is assumed to be $0.8\ \text{W m}^{-1}\text{K}^{-1}$ or higher at this temperature, then the enhancement is less than 5%. If the lattice thermal conductivity is even lower to be $0.3\ \text{W m}^{-1}\text{K}^{-1}$, then the enhancement can be larger than 20% for both carrier types, achieving $zT \sim 3.0$ for n-type Si₀.₈Ge₀.₂ at $8 \times 10^{19}\ \text{cm}^{-3}$ electron concentration and $zT \sim 2.0$ for p-type Si₀.₈Ge₀.₂ at $5 \times 10^{19}\ \text{cm}^{-3}$ hole concentration. Apparently, this relative small $zT$ enhancement is due to the relatively large band gap (0.67 eV) of Si₀.₈Ge₀.₂ at 1200 K. Beyond 1200 K, SiGe alloys can be unstable and undergo material degradation [50]. Nonetheless, if we can assume that the material can survive at a higher temperature, i.e., 1500 K, the band gap of Si₀.₈Ge₀.₂ decreases to $\sim 0.54\ \text{eV}$. Therefore, the minority carrier blocking effect can be larger than the case at 1200 K. We find that the $zT$ can be enhanced above 3.6 for n-type with $6 \times 10^{19}\ \text{cm}^{-3}$ electron concentration, and above 2.3 for p-type with $6 \times 10^{19}\ \text{cm}^{-3}$ hole concentration at 1500 K if the lattice

![](./images/814530145158168576_10.jpg)

FIG. 10. Calculated figure of merit $zT$ of $Si_{0.8}Ge_{0.2}$ with and without minority carrier blocking as a function of electron concentration (bottom $x$ axis) and hole concentration (top $x$ axis) at 1200 K. The same barrier size and height used in Fig. 8 were used for the calculations. Electron barriers ($e$-barrier) were used for the minority carrier blocking in the p-type material, and hole barriers ($h$-barrier) for the minority carrier blocking in the n type. Two constant lattice thermal conductivities of 0.8 and $0.3\ \text{W}\ \text{m}^{-1}\text{K}^{-1}$ were considered.

thermal conductivity is as small as $0.5\ \text{W}\ \text{m}^{-1}\text{K}^{-1}$. This is an enhancement of about $80\%$ over the bulk value obtained with the same lattice thermal conductivity for both carrier types.

## IV. CONCLUSIONS

In this paper, we have theoretically investigated the $zT$ enhancement by minority carrier blocking with heterostructure barriers in several state-of-the-art thermoelectric materials such as $Bi_{2}Te_{3}$, $Mg_{2}Sn_{1-x}Si_{x}$, and $Si_{1-x}Ge_{x}$ alloys over a wide temperature range. It is shown through the these example materials that the minority carrier blocking can enhance the thermoelectric figure of merit significantly at low carrier concentrations by suppressing the bipolar thermal conductivity and keeping the power factor high that is otherwise critically diminished by the bipolar effect. Typically, the enhancement is larger when the band gap of the material is smaller and temperature is higher. Also, the smaller the lattice thermal conductivity, the larger the enhancement that can be achieved. In $Bi_{2}Te_{3}$ alloys, about $70\%$ enhancements are predicted for both n-type and p-type materials to achieve maximum $zT\sim1.7$ for the n-type $Bi_{2}Te_{2.7}Se_{0.3}$ and maximum $zT\sim2.0$ for the p-type $Bi_{0.5}Sb_{1.5}Te_{3}$ at 500 K when the lattice thermal conductivity is $0.5\ \text{W}\ \text{m}^{-1}\text{K}^{-1}$. Despite the relatively low temperature 500 K, the enhancement was large due to the small band gaps ($\sim0.2\ \text{eV}$) of the $Bi_{2}Te_{3}$ alloys. It is expected that the enhancement is even larger at higher temperatures than 500 K. This effect, if realized, will be particularly useful for the $Bi_{2}Te_{3}$ alloys to be used over a much wider temperature range than the bulks without the need to search for another material working at elevated temperatures. In $Mg_{2}Si_{0.4}Sn_{0.6}$, $zT_{s}$ larger than 3.0 and 2.5 are possible for the n-type and p-type materials, respectively, at 900 K by the optimal minority carrier blocking, when the lattice thermal conductivity is as low as $0.3\ \text{W}\ \text{m}^{-1}\text{K}^{-1}$. In $Si_{0.8}Ge_{0.2}$ alloy, the enhancement can be small due to its relatively large band gap ($\sim0.67\ \text{eV}$ at 1200 K), but at higher temperatures, for example, at 1500 K, the material could achieve $zT$ larger than 3.0 for n-type $Si_{0.8}Ge_{0.2}$ by the minority carrier blocking.

## APPENDIX A: ELECTRON TRANSPORT MODELING AND EXPERIMENTAL DATA FITTING FOR $Bi_{2}Te_{3}$ ALLOYS

The crystal structures of $Bi_{2}Te_{3}$ and its alloys with Se are rhombohedral with the space group $R\bar{3}m$ [54]. They can be easily cleaved in planes perpendicular to the $c$ axis (trigonal axis) because the five individual atomic layers following the sequence Te(1)-Bi-Te(2)-Bi-Te(1) in the direction of the $c$ axis constitute a quintuple layer, and two adjacent quintuple layers are bound by the weak van der Waals force [32]. According to the band structure calculations based on density functional theory, $Bi_{2}Te_{3}$ has the conduction band minima with six valleys along the $\Lambda$ line ($\Gamma-Z$) in the Brillouin zone and the valence band maxima with six valleys on the mirror planes of the Brillouin zone [32].

In order to calculate transport properties, we are particularly interested in the density of states for both conduction and valence bands with the band gap. We use the density of state results based on the first-principles calculations from Ref. [55] and model the band structure within the effective mass approximation (EMA) with nonparabolic bands: We use two parameters, effective mass and nonparabolicity, both defined in Eq. (1), for each band. Figure 11 shows the curve-fitting results of the density of states with two conduction bands and two valence bands information. The extracted band structure parameters are summarized in Table I ($x=0$ in $Bi_{2}Te_{3-x}Se_{x}$ for $Bi_{2}Te_{3}$). The obtained effective masses of the first conduction band and the first valence band are in a good agreement with the values from the literature [32,56].

The energy gap of $Bi_{2}Te_{3-x}Se_{x}$ depends on the composition. It has been found experimentally that the band gap linearly increases from Se content $x=0$ to $x\sim0.9$ and then decreases with further Se content increase [57]. We are particularly

![](./images/814530145158168576_11.jpg)

FIG. 11. Curve fitting of the density of states of $Bi_{2}Te_{3}$ (Jeong *et al.* [55]) as a function of energy using the multiband effective mass approximation (EMA) with the nonparabolic band model. The extracted band structure parameters are summarized in Table I.

<table>
<caption>TABLE I. Band structure and material parameters used for transport calculations of n-type $\text{Bi}_2\text{Te}_{3-x}\text{Se}_x$ ($0 \leqslant x \leqslant 1$) and p-type $\text{Bi}_{0.5}\text{Sb}_{1.5}\text{Te}_3$.ª</caption>
<thead>
  <tr>
    <th>Parameter</th>
    <th>n-type $\text{Bi}_2\text{Te}_{3-x}\text{Se}_x$</th>
    <th>p-type $\text{Bi}_{0.5}\text{Sb}_{1.5}\text{Te}_3$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Band gap (eV)</td>
    <td>$0.16 \times (1-x) + 0.3 \times x - 9.5 \times 10^{-5}$ $\times (T-300)$</td>
    <td>$0.23-9.5 \times 10^{-5}$ $\times (T-300)$</td>
  </tr>
  <tr>
    <td>Band offset between the 1st and 2nd conduction bands (eV)</td>
    <td>0.23</td>
    <td>0.23</td>
  </tr>
  <tr>
    <td>Band offset between the 1st and 2nd valence bands (eV)</td>
    <td>0.27</td>
    <td>0.27</td>
  </tr>
  <tr>
    <td>Electron effective mass of the 1st conduction band ($m_0$)</td>
    <td>$0.20 + 0.07 \times x \times (1-x)$</td>
    <td>0.17</td>
  </tr>
  <tr>
    <td>Electron effective mass of the 2nd conduction band ($m_0$)</td>
    <td>$0.21 + 0.07 \times x \times (1-x)$</td>
    <td>0.18</td>
  </tr>
  <tr>
    <td>Hole effective mass of the 1st valence band ($m_0$)</td>
    <td>$0.36 + 0.16 \times x \times (1-x)$</td>
    <td>0.36</td>
  </tr>
  <tr>
    <td>Hole effective mass of the 2nd valence band ($m_0$)</td>
    <td>$0.36 + 0.16 \times x \times (1-x)$</td>
    <td>0.36</td>
  </tr>
  <tr>
    <td>Nonparabolicity $\alpha$ of the 1st conduction band ($\text{eV}^{-1}$)</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Nonparabolicity $\alpha$ of the 2nd conduction band ($\text{eV}^{-1}$)</td>
    <td>1.0</td>
    <td>1.0</td>
  </tr>
  <tr>
    <td>Nonparabolicity $\alpha$ of the 1st valence band ($\text{eV}^{-1}$)</td>
    <td>0.6</td>
    <td>0.6</td>
  </tr>
  <tr>
    <td>Nonparabolicity $\alpha$ of the 2nd valence band ($\text{eV}^{-1}$)</td>
    <td>2.0</td>
    <td>2.0</td>
  </tr>
  <tr>
    <td>Acoustic phonon deformation potential $D_a$ for electrons (eV)</td>
    <td>$[16 \times (1-x) + 26 \times x]$</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Acoustic phonon deformation potential $D_a$ for holes (eV)</td>
    <td>$[21 \times (1-x) + 30 \times x]$</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Elastic constant $C_l$ ($\text{N/m}^2$)</td>
    <td>$7.1 \times 10^{10}$</td>
    <td>$7.1 \times 10^{10}$</td>
  </tr>
  <tr>
    <td>Compensation ratio $r_c$</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Nonionized defect density $N_v$ ($\text{cm}^{-3}$)</td>
    <td>$1 \times 10^{19}$</td>
    <td>$3 \times 10^{19}$</td>
  </tr>
  <tr>
    <td>Short-range potential of defects $U_v$ ($\text{J m}^{-3}$)</td>
    <td>$1 \times 10^{-46}$</td>
    <td>$1 \times 10^{-46}$</td>
  </tr>
</tbody>
</table>

ªAll the effective masses in this table are one-valley values. To obtain the DOS effective mass, it must be multiplied by $N_{\text{val}}^{2/3}$, where $N_{\text{val}}$ is the number of valley of each band (i.e., $N_{\text{val}} = 6$ for the $\text{Bi}_2\text{Te}_3$ alloys).

interested in the low Se content alloys with ($0 \leqslant x \leqslant 1$) in this paper. As shown in Table I, we assumed the band gap and all other band parameters for $\text{Bi}_2\text{Te}_{3-x}\text{Se}_x$ to be a linear interpolation between those of $\text{Bi}_2\text{Te}_3$ ($x=0$, extracted from the DOS fitting in Fig. 11) and those of $\text{Bi}_2\text{Te}_2\text{Se}_1$ ($x=1$, from literature [32,56]), except for the effective masses, which are known to approximately follow a parabolic relation with Sn content between $x=0$ and 1 [56]. Note that the effective masses shown in Table I are single-valley values. To obtain the DOS effective mass, it must be multiplied by $N_{\text{val}}^{2/3}$, where $N_{\text{val}}$ is the number of the valley of each band. The temperature coefficient of the band gap ($\text{d}E_g/\text{d}T$) was set to be $-9.5 \times 10^{-5}$ eV/K [32]. It turns out that the second conduction band and the first and second valence bands are highly nonparabolic, while the first conduction band can be modeled as a parabolic band. In the transport properties calculations for the $\text{Bi}_2\text{Te}_3$ alloys in Table I, the acoustic phonon deformation potential scattering and the ionized impurity scattering described by (22) and (24) are included for the calculation of the energy-dependent scattering time. These parameters were used to successfully fit the experimental Seebeck coefficient as a function of electrical conductivity for $\text{Bi}_2\text{Te}_3$ [55] and $\text{Bi}_2\text{Te}_{2.4}\text{Se}_{0.6}$ [56,58] at room temperature as shown in Fig. 12.

We also fitted the experimental data of the high $zT$ $\text{Bi}_2\text{Te}_3$ alloys: nanostructured p-type $\text{Bi}_{0.5}\text{Sb}_{1.5}\text{Te}_3$ [39] and n-type $\text{Bi}_2\text{Te}_{2.7}\text{Se}_{0.3}$ [40] using the band structure information and scattering parameters shown in Table I. Figure 13 presents the fitting results for the experimental data. We used a constant hole concentration of $3.5 \times 10^{19}\text{cm}^{-3}$ to fit the experimental data of the p-type $\text{Bi}_{0.5}\text{Sb}_{1.5}\text{Te}_3$ and a constant electron concentration of $1.7 \times 10^{19}\text{cm}^{-3}$ to fit the data of n-type $\text{Bi}_2\text{Te}_{2.7}\text{Se}_{0.3}$ over the temperature range 300 K–530 K. (Carrier concentrations were not measured in these papers.) As shown in Fig. 13, the simulation results agree very well with the experimental data. There is a slight discrepancy between theory and experiment at high temperatures around 500 K for the n-type material. The experimental electrical conductivity

![](./images/814530145158168576_12.jpg)

FIG. 12. Fitting results of the experimental data, Seebeck coefficient as a function of electrical conductivity, for $\text{Bi}_2\text{Te}_3$ [55] and $\text{Bi}_2\text{Te}_{2.4}\text{Se}_{0.6}$ [56,58] at 300 K.

![](./images/814530145158168576_13.jpg)

FIG. 13. Fitting results of (a) electrical conductivity, (b) Seebeck coefficient, (c) thermal conductivity, and (d) figure of merit $zT$; experimental data of p-type $Bi_{0.5}Sb_{1.5}Te_3$ from Poudel *et al.* [39] and n-type $Bi_2Te_{2.7}Se_{0.3}$ from Yan *et al.* [40]. Symbols are experimental data, and curves are theoretical fitting. In (c), the lattice thermal conductivity ($\kappa_{\text{lat}}$) and electronic thermal conductivity ($\kappa_{\text{elec}}$) including the bipolar term are separated by the theory.

was slightly higher, and the magnitude of the Seebeck coefficient was lower than the calculated values, which may indicate that the bipolar effect is even more significant than the theory predicted. There is room for adjustment of the band structure and scattering parameters, e.g., a higher temperature coefficient of the band gap, and thus a further reduced band gap at the higher temperatures could better fit the data with an increased bipolar effect. However, an increased bipolar effect should result in a higher bipolar thermal conductivity at the same time, but the thermal conductivity shown in Fig. 12(c) is already overestimated by the theory. It is also possible that there is some degree of uncertainty in the experimental data, particularly in the thermal conductivity at above 450 K. With this uncertainty taken into account, the lattice thermal conductivity for these $Bi_2Te_3$ alloy materials is extracted from the experimental data and found to be as low as $0.4\ \text{W m}^{-1}\text{K}^{-1}$ at around 500 K, indicating strong phonon scattering by the nanostructures in these materials.

### APPENDIX B: ELECTRON TRANSPORT MODELING AND EXPERIMENTAL DATA FITTING FOR $\text{Si}_{1-x}\text{Ge}_x$

$\text{Si}_{1-x}\text{Ge}_x$ alloys have an indirect band gap that decreases steadily with increasing Ge content from the Si band gap of 1.12 eV [59]. At $x>0.85$, the band structure has a Ge-like band symmetry, and below $x<0.85$, it becomes Si like. We are interested in the low-Ge-content compositions with $x\sim0.2$. We have listed the band structure information that we used for the calculations of the transport properties of the low Ge content alloys in Table II. The band gap also has a strong temperature dependency, steadily decreasing with increasing temperature, e.g., from 0.99 eV at 300 K to 0.67 eV at 1200 K for 20% Ge content [60]. The second conduction band is located at the X point in the Brillouin zone, with its minimum only 160 meV above the first conduction band minimum for $\text{Si}_{0.8}\text{Ge}_{0.2}$. Therefore, it is important to include the transport through the second conduction band. For the valence band, we model both the heavy hole and light hole bands as one band (first valence band), and the split-off band as another (second) valence band, of which the band maximum is about 90 meV below that of the first valence band. For SiGe alloys, we included the acoustic phonon deformation potential scattering, the ionized impurity scattering, and the short-range defect scattering (for n-type only) given by (22), (24), and (25), respectively, for the transport calculations.

Figure 14 presents the fitting results of the experimental thermoelectric properties of both p-type [52] and n-type [53] $\text{Si}_{0.8}\text{Ge}_{0.2}$ over a wide temperature range. We used a constant

TABLE II. Band structure and material parameters used for transport calculations of ${\rm Si_{1-x}Ge_x}$ ($x<0.85$).

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>${\rm Si_{1-x}Ge_x}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Band gap (eV)</td>
      <td>$1.12-0.41\times x+0.008\times x^2-4.73\times10^{-4}\times T^2/(T+636)$</td>
    </tr>
    <tr>
      <td>Band offset between the 1st and 2nd conduction bands (eV)</td>
      <td>$1.2-(1.12-0.41\times x+0.008\times x^2)$</td>
    </tr>
    <tr>
      <td>Band offset between the 1st and 2nd valence bands (eV)</td>
      <td>$0.044+0.246\times x$</td>
    </tr>
    <tr>
      <td>Electron effective mass of the 1st conduction band ($m_0$)</td>
      <td>$0.32$</td>
    </tr>
    <tr>
      <td>Electron effective mass of the 2nd conduction band ($m_0$)</td>
      <td>$0.32$</td>
    </tr>
    <tr>
      <td>Hole effective mass of the 1st valence band ($m_0$)</td>
      <td>$0.59$</td>
    </tr>
    <tr>
      <td>Hole effective mass of the 2nd valence band ($m_0$)</td>
      <td>$0.23-0.135\times x$</td>
    </tr>
    <tr>
      <td>Acoustic phonon deformation potential $D_a$ for electrons (eV)</td>
      <td>$20$</td>
    </tr>
    <tr>
      <td>Acoustic phonon deformation potential $D_a$ for holes (eV)</td>
      <td>$15$</td>
    </tr>
    <tr>
      <td>Elastic constant $C_l$ (N/m²)</td>
      <td>$9.8\times10^{10}$</td>
    </tr>
    <tr>
      <td>Compensation ratio $r_c$ for electrons</td>
      <td>$4$</td>
    </tr>
    <tr>
      <td>Compensation ratio $r_c$ for holes</td>
      <td>$1.4$</td>
    </tr>
    <tr>
      <td>Non-ionized defect density $N_v$ (cm⁻³)ᵃ</td>
      <td>$5\times10^{18}$</td>
    </tr>
    <tr>
      <td>Short-range potential of defects $U_v$ (J m⁻³)ᵃ</td>
      <td>$1\times10^{-46}$</td>
    </tr>
  </tbody>
</table>

ᵃFor n-type ${\rm Si_{1-x}Ge_x}$ only. All the bands are modeled as parabolic (i.e., nonparabolicity $\alpha=0$).

hole concentration of $1.2\times10^{20}\ {\rm cm^{-3}}$ for the p-type material fitting and the same electron concentration of $1.2\times10^{20}\ {\rm cm^{-3}}$ for the n-type material fitting. Both types of materials have similar electrical conductivities as shown in Fig. 14(a), both of which steadily decrease with increasing temperature due to the decreasing mobility by stronger acoustic phonon scattering at higher temperatures. The Seebeck coefficient keeps increasing in magnitude for both types of materials

![](./images/814530145158168576_14.jpg)

FIG. 14. Fitting results of (a) electrical conductivity, (b) Seebeck coefficient, (c) thermal conductivity, and (d) figure of merit $zT$; experimental data of p-type ${\rm Si_{0.8}Ge_{0.2}}$ from Joshi et al. [52] and n-type ${\rm Si_{0.8}Ge_{0.2}}$ from Wang et al. [53]. Symbols are experimental data, and curves are theoretical fitting. In addition, the calculated properties with the minority carrier blocking (MCB) by 10-nm-wide and $10k_BT$-high barriers in the minority carrier band are also plotted to show the $zT$ enhancement. In (c), the lattice thermal conductivity ($\kappa_{\rm lat}$) and electronic thermal conductivity ($\kappa_{\rm elec}$) including the bipolar term have been separated by the theory.

[Fig. 14(b)]. Above 900 K, the experimental data deviate from the theoretical prediction in both the electrical conductivity and Seebeck coefficient. The trend is the opposite for the electrical conductivity and Seebeck coefficient of each carrier type, which may indicate that there is a carrier concentration variation with temperature at these high temperatures. It is not unsual to observe redistribution of carrier-donating impurities in a material at such a high temperature to change the carrier concentration; in Na-doped PbTe, Na atoms, which were confined at the grain boundaries, redistributes themselves into the matrix at high temperatures $\sim$650 K and above to increase the hole concentration in the material [8]. Similarly, it is possible that the phosphorus dopant atoms were redistributed into the matrix in the n-type $Si_{0.8}Ge_{0.2}$ to increase the electron concentration at high temperatures above 900 K, which resulted in a sudden increase in the electrical conductivity and a sudden drop in the magnitude of Seebeck coefficient. On the other hand, the hole concentration might have been reduced in the p-type $Si_{0.8}Ge_{0.2}$ to cause a sudden decrease in the electrical conductivity, while increasing the Seebeck coefficient. This process could be related to the compensation of holes by defects or impurities in the material.

The experimental data were measured up to 1200 K only, but the theory predicts that the $zT$ would drop down as temperature further increases above 1200 K for both types of materials as shown in Fig. 14(d). However, this reduction of $zT$ could be overturn by the minority carrier blocking, causing it to keep increasing with temperature beyond 1200 K mainly because the bipolar thermal conductivity could be effectively suppressed by the heterostructure barriers [Fig. 14(c)]. Although this carrier concentration $1.2\times10^{20}\ \mathrm{cm}^{-3}$ used in the material is not the optimal carrier concentration to maximize the $zT$ enhancement by minority carrier blocking, $zT$ could reach $\sim$2.0 for the n-type material at 1800 K with the minority carrier blocking assuming that the material can be stable at this temperature. The lattice thermal conductivity was extracted for the materials and found to be $1.6-1.8\ \mathrm{Wm}^{-1}\mathrm{K}^{-1}$, being flat over the measured temperature range.

[1] L. E. Bell, *Science* **321**, 1457 (2008).

[2] I. Chowdhury, R. Prasher, K. Lofgreen, G. Chrysler, S. Narasimhan, R. Mahajan, D. Koester, R. Alley, and R. Venkatasubramanian, *Natu. Nanotechnol.* **4**, 235 (2009).

[3] L. Shi, C. Dames, J. R. Lukes, P. S. Reddy, J. Duda, D. G. Cahill, J. Lee, A. Marconnet, K. E. Goodson, J.-H. Bahk *et al.*, *Nanosc. Microsc. Therm.* **19**, 127 (2015).

[4] Z. Wang, V. Leonov, P. Fiorini, and C. V. Hoof, *Sensor Actuat. A Phys.* **156**, 95 (2009).

[5] J.-H. Bahk, H. Fang, K. Yazawa, and A. Shakouri, *J. Mater. Chem. C* **3**, 10362 (2015).

[6] Y. C. Lan, A. J. Minnich, G. Chen, and Z. F. Ren, *Adv. Funct. Mater.* **20**, 357 (2010).

[7] C. J. Vineis, A. Shakouri, A. Majumdar, and M. G. Kanatzidis, *Adv. Mater.* **22**, 3970 (2010).

[8] K. Biswas, J. He, I. D. Blum, C.-I. Wu, T. P. Hogan, D. N. Seidman, V. P. Dravid, and M. G. Kanatzidis, *Nature* **489**, 414 (2012).

[9] H. Wang, J.-H. Bahk, C. Kang, J. Hwang, K. Kim, J. Kim, P. Burke, J. E. Bowers, A. Shakouri, and W. Kim, *Proc. Natl. Acad. Sci. USA* **111**, 10949 (2014).

[10] L.-D. Zhao, S.-H. Lo, Y. Zhang, H. Sun, G. Tan, C. Uher, C. Wolverton, V. P. Dravid, and M. G. Kanatzidis, *Nature* **508**, 373 (2014).

[11] S. Sassi, C. Candolfi, J.-B. Vaney, V. Ohorodniichuk, P. Masschelein, A. Dauscher, and B. Lenoir, *Appl. Phys. Lett.* **104**, 212105 (2014).

[12] C.-L. Chen, H. Wang, Y.-Y. Chen, T. Day, and G. J. Snyder, *J. Mater. Chem. A* **2**, 11171 (2014).

[13] J. Carrete, N. Mingo, and S. Curtaloro, *Appl. Phys. Lett.* **105**, 101907 (2014).

[14] L. D. Hicks and M. S. Dresselhaus, *Phys. Rev. B* **47**, 12727 (1993); **47**, 16631 (1993).

[15] R. Kim, S. Datta, and M. S. Lundstrom, *J. Appl. Phys.* **105**, 6 (2009).

[16] J. P. Heremans, V. Jovovic, E. S. Toberer, A. Saramat, K. Kurosaki, A. Charoenphakdee, S. Yamanaka, and G. J. Snyder, *Science* **321**, 554 (2008).

[17] Y. Pei, A. LaLonde, S. Iwanaga, and G. J. Snyder, *Energy Environ. Sci.* **4**, 2085 (2011).

[18] Y. Pei, X. Shi, A. LaLonde, H. Wang, L. Chen, and G. J. Snyder, *Nature* **473**, 66 (2011).

[19] W. Liu, X. J. Tan, K. Yin, H. J. Liu, X. F. Tang, J. Shi, Q. J. Zhang, and C. Uher, *Phys. Rev. Lett.* **108**, 166601 (2012).

[20] M. Zebarjadi, G. Joshi, G. Zhu, B. Yu, A. Minnich, Y. Lan, X. Wang, M. Dresselhaus, Z. Ren, and G. Chen, *Nano Lett.* **11**, 2225 (2011).

[21] D. Vashaee and A. Shakouri, *Phys. Rev. Lett.* **92**, 106103 (2004).

[22] J.-H. Bahk, Z. Bian, and A. Shakouri, *Phys. Rev. B* **87**, 075204 (2013).

[23] Y. Zhang, J.-H. Bahk, J. Lee, C. Birkel, M. Snedaker, D. Liu, H. Zeng, M. Moskovits, A. Shakouri, and G. Stucky, *Adv. Mater.* **26**, 2755 (2014).

[24] H. Yang, J.-H. Bahk, T. Day, A. M. S. Mohammed, B. Min, G. J. Snyder, A. Shakouri, and Y. Wu, *Nano Lett.* **14**, 5398 (2014).

[25] J.-H. Bahk and A. Shakouri, *Appl. Phys. Lett.* **105**, 052106 (2014).

[26] H. Yang, J.-H. Bahk, T. Day, A. M. S. Mohammed, G. J. Snyder, A. Shakouri, and Y. Wu, *Nano Lett.* **15**, 1349 (2015).

[27] M. Lundstrom, *Fundamentals of Carrier Transport*, 2nd ed. (Cambridge University Press, Cambridge, 2000).

[28] J. Zhou, B. Liao, and G. Chen, *Semicond. Sci. Technol.* **31**, 043001 (2016).

[29] J.-H. Bahk and A. Shakouri, in *Nanoscale Thermoelectrics*, Lecture Notes in Nanoscale Science and Technology, edited by X. Wang and Z. Wang (Springer, Switzerland, 2014), Vol. 16, Chap. 2, pp. 41–92.

[30] D. Narducci, E. Selezneva, G. Cerofolini, S. Frabboni, and G. Ottaviani, *J. Solid State Chem.* **193**, 19 (2012).

[31] G. S. Nolas and H. J. Goldsmid, in *Thermal Conductivity: Theory, Properties, and Applications*, edited by T. M. Tritt (Kluwer Academic, New York, 2004), Chap. 1.4, pp. 105–120.

[32] G. S. Nolas, J. Sharp, and H. J. Goldsmid, *Thermoelectrics: Basic Principles and New Materials Developments* (Springer-Verlag, Berlin, 2001).

[33] S. Wang, J. Yang, T. Toll, J. Yang, W. Zhang, and X. Tang, Sci. Rep. **5**, 10136 (2015).

[34] I. M. Tsidilkovskii, W. Giriat, G. I. Kharus, and E. A. Neifeld, Phys. Status Solidi B **64**, 717 (1974).

[35] J.-H. Bahk, Z. Bian, and A. Shakouri, Phys. Rev. B **89**, 075204 (2014).

[36] C. J. Vineis, T. C. Harman, S. D. Calawa, M. P. Walsh, R. E. Reeder, R. Singh, and A. Shakouri, Phys. Rev. B **77**, 235202 (2008).

[37] D. M. Zayachuk, *Semiconductors* **31**, 173 (1997).

[38] J.-H. Bahk, Z. Bian, M. Zebarjadi, P. Santhanam, R. Ram, and A. Shakouri, Appl. Phys. Lett. **99**, 072118 (2011).

[39] B. Poudel, Q. Hao, Y. Ma, Y. Lan, A. Minnich, B. Yu, X. Yan, D. Wang, A. Muto, D. Vashaee, X. Chen, J. Liu, M. S. Dresselhaus, G. Chen, and Z. Ren, *Science* **320**, 634 (2008).

[40] X. Yan, B. Poudel, Y. Ma, W. S. Liu, G. Joshi, H. Wang, Y. Lan, D. Wang, G. Chen, and Z. Ren, *Nano Lett.* **10**, 3373 (2010).

[41] S. Cho, Y. Kim, A. DiVenere, G. K. Wong, and J. B. Ketterson, Appl. Phys. Lett. **75**, 1401 (1999).

[42] S. S. Lin and C. N. Liao, J. Appl. Phys. **110**, 093707 (2011).

[43] J. H. Son, M. W. Oh, B. S. Kim, S. D. Park, B. K. Min, M. H. Kim, and H. W. Lee, J. Alloys Compd. **566**, 168 (2013).

[44] M. W. Oh, J. H. Son, B. S. Kim, S. D. Park, B. K. Min, and H. W. Lee, J. Appl. Phys. **115**, 133706 (2014).

[45] M. I. Fedorov and V. K. Zaitsev, in *Thermoelectrics Handbook: Macro to Nano*, edited by D. M. Rowe (CRC Press, Boca Raton, 2006), Chap. 31.

[46] V. K. Zaitsev, M. I. Fedorov, E. A. Gurieva, I. S. Eremin, P. P. Konstantinov, A. Y. Samunin, and M. V. Vedernikov, *Phys. Rev. B* **74**, 045207 (2006).

[47] P. Gao, X. Lu, I. Berkun, R. D. Schmidt, E. D. Case, and T. P. Hogan, Appl. Phys. Lett. **105**, 202104 (2014).

[48] C. B. Vining, J. Appl. Phys. **69**, 331 (1991).

[49] C. B. Vining, W. Laskow, J. O. Hanson, R. R. Van der Beck, and P. D. Gorsuch, J. Appl. Phys. **69**, 4333 (1991).

[50] C. B. Vining, in *CRC Handbook of Thermoelectrics*, edited by D. M. Rowe (CRC Press, Boca Raton, 1995), Chap. 28.

[51] J. P. Dismukes, L. Ekstrom, E. F. Steigmeier, I. Kudman, and D. S. Beers, J. Appl. Phys. **35**, 2899 (1964).

[52] G. Joshi, H. Lee, Y. Lan, X. Wang, G. Zhu, D. Wang, R. W. Gould, D. C. Cuff, M. Y. Tang, M. S. Dresselhaus, G. Chen, and Z. Ren, *Nano Lett.* **8**, 4670 (2008).

[53] X. W. Wang, H. Lee, Y. C. Lan, G. H. Zhu, G. Joshi, D. Z. Wang, J. Yang, A. J. Muto, M. Y. Tang, J. Klatsky, S. Song, M. S. Dresselhaus, G. Chen, and Z. Ren, *Appl. Phys. Lett.* **93**, 193121 (2008).

[54] S. K. Mishra, S. Satpathy, and O. Jepsen, *J. Phys.: Condens. Matter* **9**, 461 (1997).

[55] C. Jeong, R. Kim, M. Luisier, S. Datta, and M. Lundstrom, J. Appl. Phys. **107**, 023707 (2010).

[56] M. Neuberger, *The BiTe-BiSe system data sheet*, Airforce Mater. Res. Lab (1966), http://www.dtic.mil/cgi-bin/GetTRDoc?AD=AD0477558.

[57] I. G. Austin, and A. R. Sheard, J. Electron. Control **3**, 236 (1957).

[58] D. J. Ryden, *Energy Convers.* **11**, 161 (1971).

[59] R. Braunstein, A. R. Moore, and F. Herman, *Phys. Rev.* **109**, 695 (1958).

[60] P. Lautenschlager, P. B. Allen, and M. Cardona, *Phys. Rev. B* **31**, 2163 (1985).