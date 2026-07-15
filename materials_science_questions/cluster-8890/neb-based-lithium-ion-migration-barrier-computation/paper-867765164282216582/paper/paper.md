# Influence of lattice dynamics on lithium-ion conductivity: A first-principles study

Arun K. Sagotra, $^1$ Dewei Chu, $^1$ and Claudio Cazorla$^{1, *}$

$^1$School of Materials Science and Engineering, UNSW Australia, Sydney NSW 2052, Australia

In the context of novel solid electrolytes for solid-state batteries, first-principles calculations are becoming increasingly more popular due to their ability to reproduce and predict accurately the energy, structural, and dynamical properties of fast-ion conductors. In order to accelerate the discovery of new superionic conductors is convenient to establish meaningful relations between ionic transport and simple materials descriptors. Recently, several experimental studies on lithium fast-ion conductors have suggested a correlation between lattice softness and enhanced ionic conductivity due to a concomitant decrease in the activation energy for ion migration, $E_a$. In this article, we employ extensive *ab initio* molecular dynamics simulations based on density functional theory to substantiate the links between ionic transport and lattice dynamics in a number of structurally and chemically distinct lithium superionic conductors. Our first-principles results show no evidence for a direct and general correlation between $E_a$, or the hopping attempt frequency, and lattice softness. However, we find that, in agreement with recent observations, the pre-exponential factor of lithium diffusivity, $D_0$, follows the Meyer-Neldel rule $\propto \exp(E_a/\langle\omega\rangle)$, where $\langle\omega\rangle$ represents an average phonon frequency. Hence, lattice softness can be identified with enhanced lithium diffusivity but only within families of superionic materials presenting very similar migration activation energies, due to larger $D_0$. On the technical side, we show that neglection of temperature effects in first-principles estimation of $E_a$ may lead to huge inaccuracies of $\sim 10\%$. The limitations of zero-temperature harmonic approaches in modeling of lithium-ion conductors are also illustrated.

## I. INTRODUCTION

Fast-ion, or superionic, conductors (FIC) exhibit large ionic conductivies $(\sim 1$ mS cm$^{-1})$ in the crystal phase [1]. Examples of archetypal FIC are CaF$_2$, AgI, and La$_{0.5}$Li$_{0.5}$TiO$_3$ [2-4]. In addition to their fundamental interests, FIC are of tremendous importance in technological applications such as solid-state batteries [5], solid oxide fuel cells [6], solid-state cooling [7-10], and catalysis and sensors [11, 12]. In the context of electrochemical energy storage, lithium FIC are crucial in their role as solid electrolytes, which enable the back-and-forth passage of lithium ions between electrodes. Lithium FIC, however, are complex materials in which ionic conductivity depends strongly on their chemical composition and atomic structure, and thus far only a reduced number of fast-ion conductors have been identified as suitable for applications [5]. To design novel lithium FIC with enhanced ionic conductivities then is desirable to establish meaningful relationships between lithium diffusivity and simple materials descriptors [13, 14].

Recent studies have explored the correlations between lattice dynamics and ionic transport in lithium and other families of FIC [15-20]. In particular, Kraft *et al.* have investigated the superionic argyrodites Li$_6$PS$_5$X (X = Cl, Br, I) [19] and Muy *et al.* the LISICON series originated by Li$_3$PO$_4$ [20] by using electrochemical impedance spectroscopy and neutron diffraction measurements. The authors of both studies have concluded that lattice softness is correlated with low activation energies for ion migration, $E_a$. The intuitive explanation for such an effect is that low-frequency lattice excitations involve large atomic displacements around the equilibrium positions, which may enhance the probability of lithium ions to hop towards adjacent sites [5, 20, 21].

On a general scale, it would be very interesting to ascertain whether the same interplay between $E_a$ and lattice dynamics applies also to other families of lithium FIC that present markedly different compositions and structural traits (e.g., cubic antiperovskites and hexagonal nitride compounds –we recall that Li$_6$PS$_5$X and Li$_3$PO$_4$-based compounds mostly exhibit orthorhombic crystal symmetry–). Meanwhile, the intuitive explanation that has been proposed to understand the influence of phonons on lithium-ion conductivity might be too simplistic. For instance, lithium ions are lightweight hence the low-frequency lattice excitations in FIC, which mostly are related to the mechanical stiffness of the material, generally will be dominated by heavier atomic species; intuitively then it could be argued that wide anion lattice vibrations would reduce the excursions of lithium ions (e.g., by distorting the usual low-dimensional ion conducting channels [22]) and thus obstruct, rather than enhance, their diffusivity. Moreover, large lithium displacements around the equilibrium positions involve also low vibrational frequencies, which suggests a reduction in the corresponding hopping attempt frequency; this effect would have an opposite impact on the ionic conductivity than an eventual decrease in $E_a$, and *a priori* it is not clear which of the two mechanisms would be dominant [19]. For an improved design of lithium FIC, a more general and quantitative understanding of how lattice dynamics and ionic transport are related is crucially needed.

First-principles simulations may help at improving our comprehension of FIC via accurate estimation of ion-migration energy barriers, relevant thermodynamic prop-

* Corresponding Author

erties, and preferred diffusion paths [23–25]. Neverthe- less, due to the intense computational expense associ- ated to first-principles calculations, most quantum stud- ies on FIC generally neglect temperature effects. Un- fortunately, this simplification may lead to important bias and erroneous interpretations. For instance, zero- temperature calculations of ion-migration energy barri- ers customarily are performed with the nudged-elastic band (NEB) method [26], in which the initial and fi- nal geometries of the vacancy or interstitial ions need to be guessed in the form of high-symmetry metastable states; the limitations of this method for determining preferred ion diffusion paths are well documented forsome prototype FIC like metal halogens (e.g., $CaF_{2}$ [25, 27] and $PbF_{2}$ [28, 29]), copper chalcogenides (e.g., $Cu_{2} S$ [30]) and lithium-based oxides (e.g., $LiFePO_{4}$ [31]). Likewise, phonon calculations customarily are performed at zero temperature by using the harmonic approxima- tion [32–34] and considering perfectly stoichiometric sys- tems (i.e., full Li occupancy); such simplifications may result in a misrepresentation of real lithium FIC, in which sizable ionic conductivities normally appear at high temperatures and in non-stoichiometric compounds(i.e., partial Li occupancy) [5, 20]. Actually, superi- onic phases in lithium FIC tend to be highly anharmonic and become entropically stabilized at $T \neq 0$ conditions(that is, imaginary phonon frequencies usually appear in the corresponding zero-temperature phonon spectra), as we show in Fig. 1 (see also Supplementary Fig.1 and Refs.[2, 17, 20, 35]). It thus seems apparent that consid- ering temperature effects in first-principles simulations of FIC is actually necessary for better understanding them.

Ab initio molecular dynamics (AIMD) simulations nat- urally account for temperature and anharmonic effects in materials, and thus are a powerful tool for analyzing in detail and with reliability ionic diffusion processes in FIC [2, 36–39]. Estimation of key quantities like jump rates, hopping attempt frequencies, correlation factors, and $T$ -dependent phonon frequencies, which are not ac cessible with zero-temperature methods, can be obtained directly from AIMD simulations. The superior perfor- mance of AIMD methods certainly comes with a signifi- cant increase in computational expense; however, due to the current steady growth in computational power, im- proved design of algorithms, and the fact that lithium FIC typically can be described with a relatively small number of valence electrons by using pseudopotential ap- proaches (in contrast, for instance, to oxide perovskites containing transition metals), reliable AIMD simulation of fast-ion materials is currently within reach (see works[2, 36–39] and Supplementary Methods).

In this article, we present a thorough study on the lat- tice dynamics and ionic transport properties of several distinct lithium FIC based on density functional theory AIMD simulations. Specifically, we analyze the lithium diffusivity and $T$-dependent density of vibrational states in the following compounds (space groups are indicated within parentheses): hexagonal $Li_{3} N(P 6_{3} / mmc)$ [40],orthorhombic $LiGaO_{2}(Pna2_{1})$ [41], cubic $LiF(Fm \overline{3} m)$ [42], hexagonal $LiIO_{3}(P 6_{3})$ [43], and tetragonal $Li_{3} OCl$ (P4/mmm) [44]. Lattice phonons and activation en- ergies for ion migration are calculated also at zero- temperature conditions to quantify the impact of tem- perature and anharmonic effects on their evaluation. Our simulation results demonstrate the lack of a direct cor- relation between $E_{a}$ and $\langle\omega\rangle$ , where the latter term rep resents the average phonon frequency of the crystal (ei- ther associated to all the compound atoms or just Li ions). However, we show that the hopping attempt fre- quency of lithium ions, $\nu_{0}$ , follows the Meyer-Neldel rule∝ exp(Ea/(ω)), in consistent agreement with recent ex- perimental observations [45]. Thus, crystal anharmonic- ity, or equivalently lattice softness, can be identified with enhanced ionic diffusivity but only within families of FIC that present inherently similar migration activation ener- gies. On the technical side, we quantify the numerical in- accuracies in $E_{a}$ and $\langle\omega\rangle$ that result from neglecting tem perature effects, which unexpectedly turn out to be quite large (e.g., typical $\sim 10 \%$ underestimation of migration activation energies). Our theoretical work provides an improved understanding of how lattice dynamics affects lithium conductivity in FIC, hence it may be useful for improving the design of energy storage and energy con- version devices. Meanwhile, we substantiate the impor- tance of considering temperature effects in first-principles modeling of lithium FIC.

## II. SIMULATION METHODS

### A. First-principles calculations

First-principles calculations based on density func- tional theory (DFT) are performed to analyse the vibra- tional and ionic transport properties of lithium FIC. We perform these calculations with the VASP code [46] by following the generalized gradient approximation to the exchange-correlation energy due to Perdew et al. [47].(Possible dispersion interactions in $Li_{3} N$ [10] are captured with the D3 correction scheme developed by Grimme and co-workers [48].) The projector augmented-wave method is used to represent the ionic cores [49], and the follow- ing electronic states are considered as valence: Li 1s-2s, N 2s-2p, Ga 4s-4p, O 2s-2p, F 2s-2p, I 5s-5p, and Cl3s-3p. Wave functions are represented in a plane-wave basis truncated at 650 eV. By using these parameters and dense k-point grids for Brillouin zone integration, the resulting energies are converged to within 1 meV per formula unit. In the geometry relaxations, a tolerance of0.01 eV·Å⁻¹ is imposed on the atomic forces.

Ab initio molecular dynamics (AIMD) simulationsbased on DFT are performed in the canonical $(N, V, T)$  ensemble (i.e., constant number of particles, volume, and temperature) for all the considered bulk materials. The selected volumes render zero-pressure conditions at room temperature, $T_{room }=300 ~K$ . The temperature in

![](./images/867765164282216582_1.jpg)

FIG. 1. Vibrational density of states of Li₃N calculated at different compositions and temperatures. (Black) Stoichiometric system at zero temperature is vibrationally unstable since exhibits few imaginary phonon frequencies; results are obtained with the harmonic approximation. (Red) Non-stoichiometric system at zero temperature is vibrationally unstable since exhibits many imaginary phonon frequencies, most of which are associated to Li-dominated lattice eigenmodes (indicated by the red arrow); results are obtained with the harmonic approximation. (Blue) Non-stoichiometric system at $T=300$ K is vibrationally stable due to the lack of imaginary phonon frequencies; results are obtained with AIMD simulations, which fully take into consideration anharmonicity and temperature effects.

the AIMD simulations is kept fluctuating around a set-point value by using Nose-Hoover thermostats. Large simulation boxes containing $N_{ion}\sim 250$ atoms are employed in all the cases, and periodic boundary conditions are applied along the three Cartesian directions. Newton's equations of motion are integrated by using the customary Verlet's algorithm and a time-step length of $\delta t=10^{-3}$ ps. $\Gamma$-point sampling for integration within the first Brillouin zone is employed in all the AIMD simulations. The calculations comprise long simulation times of $t_{total}\sim 200$ ps. For each compound, we run a total of 8 AIMD simulations at different temperatures and considering both stoichiometric and non-stoichiometric (that is, containing vacancies) systems. We focus on the description of the superionic and vibrational properties of lithium FIC, which are estimated by monitoring the positions and velocities of the ions during the AIMD simulations. Tests performed on the numerical bias stemming from the finite size of the simulation cell and duration of the molecular dynamics runs are reported in the Supplementary Methods. In view of the results obtained in such numerical tests, the adopted $N_{ion}$ and $t_{total}$ values can be assumed to provide reasonably well converged results for the ionic diffusivity and vibrational density of states of lithium FIC (Supplementary Methods).

Zero-temperature phonon frequency calculations are performed with the small-displacement method, in which the force-constant matrix is calculated in real-space by considering the proportionality between atomic displacements and forces [32, 33, 50, 51]. The quantities with respect to which our phonon calculations are converged include the size of the supercell, the size of the atomic displacements, and the numerical accuracy in the sampling of the Brillouin zone. We find the following settings to provide quasi-harmonic free energies converged to within 5 meV per formula unit: $3\times3\times3$ supercells, typically containing 200-300 ions (the figures indicate the number of replicas of the unit cell along the corresponding lattice vectors), atomic displacements of $0.02$ Å, and $\mathbf{q}$-point grids of $14\times14\times14$. The value of the phonon frequencies are obtained with the PHON code developed by Alfè [51]. In using this code we exploit the translational invariance of the system, to impose the three acoustic branches to be exactly zero at the center of the Brillouin zone, and apply central differences in the atomic forces.

$Ab$ initio nudged-elastic band (NEB) calculations [26] are performed to estimate the energy barriers for ionic diffusion in all investigated lithium FIC at zero temperature. Our NEB calculations typically are performed in $2\times2\times2$ or $3\times3\times3$ supercells containing several tens of atoms. We use $\mathbf{q}$-point grids of $8\times8\times8$ or $6\times6\times6$ and an energy plane-wave cut-off of 650 eV. Six intermediate images are used to determine the most likely ionic diffusion paths when temperature effects are disregarded; the geometry optimizations are halted when the total forces on the atoms are smaller than $0.01$ eV·Å⁻¹.

### B. Estimation of key quantities

The mean square displacement (MSD) is estimated with the formula:

$$
\begin{aligned}
\operatorname{MSD}(\tau) &= \frac{1}{N_{ion}\left(N_{step}-n_{\tau}\right)} \times \\
& \sum_{i=1}^{N_{ion}} \sum_{j=1}^{N_{step}-n_{\tau}}\left|\mathbf{r}_{i}\left(t_{j}+\tau\right)-\mathbf{r}_{i}\left(t_{j}\right)\right|^{2},
\end{aligned} \tag{1}
$$

where $\mathbf{r}_{i}(t_{j})$ is the position of the migrating ion labelled as $i$ at time $t_{j}\ (=j\cdot\delta t)$, $\tau$ represents a lag time, $n_{\tau}=\tau/\delta t$, $N_{ion}$ is the total number of mobile ions, and $N_{step}$ the total number of time steps. The diffusion coefficient then is obtained by using the Einstein relation:

$$
D=\lim_{\tau\rightarrow\infty}\frac{\operatorname{MSD}(\tau)}{6\tau}. \tag{2}
$$

In practice, we consider $0<\tau\leq100$ ps and estimate $D$ by performing linear fits over the last $\Delta\tau=50$ ps.

The $T$-dependence of the diffusion coefficient is assumed to follow the Arrhenius formula:

$$
D(T)=D_{0}\cdot\exp\left[-\frac{E_{a}}{k_{B}T}\right], \tag{3}
$$

where $D_{0}$ is known as the pre-exponential factor, $E_{a}$ is the activation energy for ionic migration, and $k_{B}$ the

Boltzmann constant. From a physical point of view, $D_0$ can be interpreted as a hopping attempt frequency, $\nu_0$, the value of which is obtained via the relationship:

$$
\nu_{0}=\frac{D_{0}}{a_{0}^{2}}, \tag{4}
$$

where $a_0$ represents the equilibrium lattice parameter of the crystal (that is, a characteristic length for the ionic hops). Likewise, the exponential factor in Eq.(3) can be interpreted as an acceptance probability for the proposed ionic jumps. Hence, large (small) $D_0$ and small (large) $E_a$ lead to high (low) ionic conductivities.

To estimate the density of vibrational states in lithium FIC, VDOS, we calculate the Fourier transform of the velocity-velocity autocorrelation function, directly obtained from the AIMD simulations, as:

$$
\operatorname{VDOS}(\omega)=\frac{1}{N_{i o n}} \sum_{i}^{N_{i o n}} \int_{0}^{\infty}\left\langle\mathbf{v}_{i}(\tau) \cdot \mathbf{v}_{i}(0)\right\rangle e^{i \omega \tau} d \tau, \quad(5)
$$

where $\mathbf{v}_i(t)$ represents the velocity of the atom labelled as $i$ at time $t$, and $\langle\cdots\rangle$ denotes statistical average in the $(N,V,T)$ ensemble. We note that VDOS depends on temperature. Once the density of vibrational states is known, it is straightforward to calculate the corresponding phonon band center or average lattice frequency, $\langle\omega\rangle$, defined as:

$$
\langle\omega\rangle=\frac{\int_{0}^{\infty} \operatorname{VDOS} \omega d \omega}{\int_{0}^{\infty} \operatorname{VDOS} d \omega}, \tag{6}
$$

which also depends on $T$. Likewise, the contribution of a particular group of ions to the full VDOS can be estimated by considering them alone in the summation appearing in Eq.(5). In order to determine a characteristic low-energy phonon frequency for lithium FIC, we (somewhat arbitrarily) define the quantity:

$$
\langle\omega\rangle_{\text {room }}=\frac{\int_{0}^{\omega_{\text {room }}} \operatorname{VDOS} \omega d \omega}{\int_{0}^{\omega_{\text {room }}} \operatorname{VDOS} d \omega}, \tag{7}
$$

where $\omega_{\text{room}}$ is $k_B T_{\text{room}}/\hbar=6.25$ THz.

## III. RESULTS

### A. $Li_3N$

This compound presents two common polymorphs known as $\alpha$ and $\beta$ phases. The $\alpha$ phase (hexagonal, space group $P6/mmm$) has a layered structure composed of alternating planes of hexagonal $\text{Li}_2\text{N}$ and pure $\text{Li}^+$ ions (see, for instance, Fig.1 in Ref.[10]). The $\beta$ phase (hexagonal, space group $P6_3/mmc$) exhibits an additional layer of lithium ions intercalated between consecutive $\text{Li}_2\text{N}$ planes that is accompanied by a doubling of the unit cell (Fig.2a). Exceptionally high ionic conductivities of the order of $10^{-4}$-$10^{-3}$ S cm$^{-1}$ have been measured experimentally in $\text{Li}_3\text{N}$ at room temperature [40, 52, 53]. Here, we restrict our analysis to $\beta$-$\text{Li}_3\text{N}$.

Figure 2a shows the minimum ion migration activation energy calculated for $\text{Li}_3\text{N}$ at zero temperature with the NEB method, $E_a^0$. The local minimum-energy points correspond to lithium vacancy positions, since we were not able to generate any metastable interstitial configuration for the stoichiometric system. This outcome suggests that superionicity in $\text{Li}_3\text{N}$ is vacancy mediated, hence mostly it occurs in non-stoichiometric systems. In good agreement with previous zero-temperature DFT results reported by Li *et al.* [40], we find that the minimum $E_a^0$ amounts to 0.03 eV and corresponds to lithium diffusion in the region contained between consecutive $\text{Li}_2\text{N}$ planes lying along the $z$ direction (Fig.2a). Thus, ionic diffusion seems to be mostly confined to two dimensions, which we denote here as $x$-$y$. We note that the migration activation energy determined in experiments, $E_a^{\text{expt}}$, is 0.45 eV [40], which is significantly larger than $E_a^0$.

Figures 2b and c show the results of our AIMD simulations performed for $\text{Li}_3\text{N}$ at finite temperatures. In accordance with the zero-temperature results just explained, lithium conductivity appears to be vacancy mediated since the diffusion coefficients calculated in the stoichiometric system at high temperatures are too small (namely, $D<10^{-6}$ cm$^2$s$^{-1}$ at $T>1000$ K, Fig. 2b). However, the lithium diffusion mechanisms and activation energy that are deduced from the $T\neq0$ simulations differ appreciably from those obtained with zero-temperature methods. In particular, the lithium ions are found to diffuse almost equally along all three Cartesian directions (Fig. 2c), and the estimated activation energy is much larger, $E_a=0.15$ eV (Fig. 2b). Although the agreement between the estimated and experimentally measured activation energies has been improved, there is still a considerable difference between $E_a$ and $E_a^{\text{expt}}$. A likely explanation for such a discrepancy may be the neglection of defects other than vacancies in the AIMD simulations (e.g., cracks, dislocations, and interfaces), which in some cases are known to deplete ionic diffusivity significantly [54, 55]. Another possibility is that the concentration of extrinsic vacancies in our AIMD simulations probably is too large (that is, $\sim2\%$), which may lead to an overestimation of lithium conductivity. Meanwhile, we estimate a pre-exponential factor of $D_0=2.5\cdot10^{-5}$ cm$^2$s$^{-1}$ and a hopping attempt frequency, $\nu_0$, of $\sim0.01$ THz.

Figure 3a shows the density of vibrational states, VDOS, estimated for non-stoichiometric $\text{Li}_3\text{N}$ at several temperatures with AIMD methods. The system is vibrationally stable in all the cases since no imaginary phonon frequencies appear in the corresponding phonon spectra. This outcome is contrary to the results obtained with the harmonic approximation at zero temperature, which indicate that non-stoichiometric $\text{Li}_3\text{N}$ is vibrationally unstable (see Fig. 1); we note that the imaginary eigenfrequency phonon modes appearing in that zero-

![](./images/867765164282216582_2.jpg)

![](./images/867765164282216582_3.jpg)

FIG. 2. Activation energy for ion migration calculated for ${\rm Li_3N}$ at (a) $T=0$ K and (b) finite temperatures considering lithium vacancies. (c) Ionic diffusivity estimated along the three Cartesian axis in non-stoichiometric ${\rm Li_3N}$ at $T=900$ K. Lithium and nitrogen ions are represented with large green and small blue spheres, respectively. Lithium vacancy positions are indicated with black squares and mobile ions with purple spheres.

temperature harmonic VDOS are mostly dominated by Li ions (see Supplementary Fig.2). As the temperature is increased, the peaks of the VDOS become smoothed and the resulting phonon band center, $\langle\omega\rangle$, increases steadily (due to the fact that higher-frequency vibrational modes become thermally activated). The accompanying increase in $\langle\omega\rangle$, however, is very mild. For instance, the phonon band center amounts to 11.66 THz at room temperature and to 11.74 THz at $T=700$ K. The average phonon frequency that is estimated by applying a cut-off of $k_BT_{room}/\hbar$ to the VDOS, $\langle\omega\rangle_{room}$ (Eq.(7) in Sec. II B), provides a characteristic frequency for the low-energy phonons of the material, which are mostly related to the mechanical stiffness of the material. We find that the $T$-induced variation of such a frequency is also very moderate; for example, at $T=700$ K $\langle\omega\rangle_{room}$ is $\sim 1\%$ larger than the value estimated at ambient conditions, which is 4.7 THz.

We note that at $T=700$ K non-stoichiometric ${\rm Li_3N}$ is superionic and presents a large diffusion coefficient of $2.2\cdot 10^{-6}\ {\rm cm^2 s^{-1}}$ whereas at room temperature remains in the normal state $(D\sim 0)$. Hence, for a same lithium FIC it seems not possible to correlate the large $T$-induced variations in ionic conductivity with the accompanying changes in VDOS, which are minute (i.e., of the order of $\sim 0.1$ THz). Figures 3b and c show the partial VDOS corresponding to lithium and nitrogen ions, respectively. The partial phonon band center of the nitrogen ions is lower than $\langle\omega\rangle_{Li}$ by $\sim 3\%$, as it could have been foreseen due to their larger atomic mass (recall the $m_{\alpha}^{-1/2}$ factors entering the expression of the dynamical force constant matrix [32-34]). Interestingly, low anion vibration phonon excitations have been linked to a reduction in FIC stability against electrochemical oxidation by Muy et al. [20].

### B. ${\rm LiGaO_2}$

At ambient conditions this compound stabilizes in a orthorhombic structure with space group $Pna2_1$. The lithium and gallium ions are located at the center of oxygen tetrahedrons, forming a two-dimensional stacking of alternating ${\rm LiO_4}$ and ${\rm GaO_4}$ arrays. Recently, a combined experimental and theoretical study has proved the superionic nature of ${\rm LiGaO_2}$ at temperatures $T\geq 800$ K [41].

Figures 4a and b show the activation energy for Li interstitial and vacancy migration calculated at zero temperature with the NEB method. In this case, we were able to generate a metastable interstitial configuration for the stoichiometric system, as shown in Fig.4a; however, the accompanying zero-temperature interstitial formation energy and activation migration energy appear to be too large, namely, 2.4 and 2.6 eV respectively. Meanwhile, the estimated zero-temperature activation energy for vacancy migration is considerably lower, $E_a^0=0.78$ eV (Fig.4b). These results suggest that fast-ion conductivity in ${\rm LiGaO_2}$ is vacancy mediated, which is in agreement with previous NEB DFT calculations reported by Islam et al. for the same system [41]. We note, however, that the experimentally measured acti-

![](./images/867765164282216582_4.jpg)

FIG. 3. Density of vibrational states calculated for $Li_3N$ at different temperatures considering (a) all the atoms, (b) only Li ions, and (c) only N ions. Results are obtained from the Fourier transform of the velocity-velocity autocorrelation function calculated during long AIMD simulations.

vation energy for Li migration is $E_a^{\text{expt}} = 1.25$ eV [41], which is significantly larger than the predicted $E_a^0$. A possible explanation for the significant discrepancy between the measured and calculated zero-temperature activation energies could be, among other causes, the neglection of temperature effects in NEB simulations, as it has been suggested by the authors of Ref.[41].

Our AIMD results shown in Fig.4c confirm that after considering temperature effects the agreement between the estimated and measured activation energies improves drastically. In particular, we calculate a large $E_a$ of 1.22 eV, which practically coincides with the corresponding experimental value. Likewise, the computed pre-exponential factor is $5.0{\cdot}10^{-2}$ cm²s⁻¹, which leads to a very large $\nu_0$ of $\sim$ 10 THz. In agreement with the zero-temperature results explained above, lithium conductivity in $LiGaO_2$ appears to be vacancy mediated since even at high temperatures of $T > 1000$ K the stoichiometric system remains in the normal state (Fig.4d).

We have estimated the VDOS of non-stoichiometric $LiGaO_2$ at several temperatures with AIMD methods (Supplementary Fig.3). The system is vibrationally stable in all the cases since no imaginary phonon frequencies appear in the corresponding phonon spectra. The effect of temperature on the calculated VDOS is very small and similar to that described previously for $Li_3N$. For instance, the average phonon frequency $\langle\omega\rangle$ amounts to 11.74 THz at $T = 900$ K and to 11.83 THz at 1300 K. Thus, again the large diffusion coefficient changes induced by temperature ($\Delta D/D \sim 10^2$ for $\Delta T = 400$ K) do not appear to be reflected on the corresponding VDOS ($(\Delta\langle\omega\rangle/\langle\omega\rangle \sim 10^{-2}$ for the same $\Delta T$). An analagous increase of about 1% is found for $\langle\omega\rangle_{\text{room}}$, which at $T =$ 900 K amounts to 4.4 THz. Regarding the partial VDOS, we find that $\langle\omega\rangle_{\text{Ga}} = 0.6\langle\omega\rangle_{\text{Li}}$ and $\langle\omega\rangle_{\text{O}} = 1.2\langle\omega\rangle_{\text{Li}}$, thus in average the Ga ions vibrate at lower frequencies than the lithium ions while the oxygen atoms at higher. Despite the larger mass of the oxygen atoms as compared to lithium, $\langle\omega\rangle_{\text{O}}$ is the highest because the oxygen atoms participate in all covalent bonds of the crystal and therefore appear represented along the whole VDOS (Supplementary Fig.3). Consequently, the presence of oxygens in Li FIC will tend to increase the phonon band center of the anion sublattice; this effect, however, is likely to be reduced significantly in the presence of other electronegative species with larger atomic masses (e.g., sulfur) [20].

### C. LiF

The crystal structure of bulk LiF at ambient conditions is rocksalt (cubic, space group $Fm\overline{3}m$). The presence of LiF has been revealed in the interface formed between the solid electrolyte and electrodes in Li-ion batteries [56], and the accompanying effects on energy storage performance have been investigated recently by several authors with theory [42, 57, 58].

By performing NEB calculations, we estimate a zero-temperature energy barrier for lithium vacancy diffusion of $E_a^0 = 0.68$ eV (Fig.5a), which is in very good agreement with previous DFT calculations [42, 57, 58]. We note that in this case we could neither find a metastable interstitial configuration, hence ionic conductivity in LiF in principle appears to be vacancy mediated. The $E_a^0$ calculated for LiF is comparable to that determined previously for $LiGaO_2$, suggesting that lithium diffusivity in both materials should be similar. However, our AIMD simulations show this not to be the case. In particular, at temperatures above 700 K non-stoichiometric LiF becomes vibrationally unstable, as shown by the fact that both the lithium and fluorine ions become mobile (Fig.5b). Consequently, we have not been able to determine any $E_a$ or $D_0$ for bulk LiF. This outcome highlights the importance of atomic structure on lithium conductivity: two materials with similar $E_a^0$ but different geometries may be not comparable in terms of ionic diffusiv-

![](./images/867765164282216582_5.jpg)

FIG. 4. Activation energy for ion migration calculated for LiGaO₂ at zero-temperature considering (a) interstial and (b) vacancy positions. (c) Lithium diffusivity of non-stoichiometric LiGaO₂ calculated at finite temperatures. (d) Mean square displacement of stoichiometric LiGaO₂ calculated at very high temperatures. Lithium, gallium, and oxygen ions are represented with large green, small blue, and small red spheres, respectively. Lithium vacancy positions are indicated with black squares and mobile ions with purple spheres.

ity. Meanwhile, our AIMD simulations show that lithium conduction in stoichiometric LiF is negligible even at high temperatures (that is, $D \sim 0$ at $T > 1000$ K, Fig.5c), in agreement with the zero-temperature NEB calculations.

The $T$-dependent VDOS of non-stoichiometric LiF calculated with AIMD simulations are reported in Supplementary Fig.4. The corresponding average phonon frequency amounts to 9.19 THz at $T = 400$ K and to 9.45 THz at 600 K. Hence, despite the fact that LiF is a much worse lithium conductor than, for instance, Li₃N, its phonon band center is significantly lower (e.g., $\langle\omega\rangle = 11.70$ THz at $T = 500$ K for non-stoichiometric Li₃N). Such a comparison suggests the lack of a direct correlation between lattice dynamics and lithium diffusivity in the investigated systems; we will comment on this point with more detail later on. Regarding the partial VDOS, we find that $\langle\omega\rangle_{\text{F}} = 0.7\langle\omega\rangle_{\text{Li}}$ owing to the larger mass of the fluorine ions and the ionic nature of the material. Thus, the low-frequency lattice excitations in LiF ($\omega < 5$ THz) are dominated by the fluorine ions, rather than by Li.

### D. LiIO₃

At ambient conditions this compound stabilizes in a hexagonal phase (space group $P6_{3}$) in which each iodine atom is surrounded by three oxygen atoms, forming a three-dimensional net of tightly bound pyramidal $\text{IO}_{3}^{-}$ groups (Fig.6a). $\text{LiIO}_{3}$ has a very complex polymorphism and undergoes reconstructive phase transitions by effect of pressure and temperature [59, 60]. More than four decades ago, Aliev *et al.* experimentally investigated the mobility of lithium ions in this compound [43]. They concluded that ionic diffusion occurred within quasi one-dimensional channels oriented along the hexagonal $c$-axis, with a corresponding activation energy of $E_{a}^{\text{expt}} = 0.26$ eV [43]. To the best of our knowledge,

![](./images/867765164282216582_6.jpg)

FIG. 5. (a) Activation energy for ion migration calculated for LiF at zero-temperature considering vacancy positions. (b) Mean square displacement of non-stoichiometric LiF calculated at high temperatures. (c) Mean square displacement of stoichiometric LiF calculated at very high temperatures. Lithium and fluorine ions are represented with large green and small blue spheres, respectively. Lithium vacancy positions are indicated with black squares and mobile ions with purple spheres.

![](./images/867765164282216582_7.jpg)

FIG. 6. (a) Activation energy for ion migration calculated for LiIO₃ at zero-temperature considering vacancy positions. (b) Lithium diffusivity of non-stoichiometric and stoichiometric LiIO₃ calculated at finite temperatures. Lithium, iodine, and oxygen ions are represented with large green, small blue, and small red spheres, respectively. Lithium vacancy positions are indicated with black squares and mobile ions with purple spheres.

the lithium diffusion mechanisms in LiIO₃ have not been studied previously with first-principles methods.

By using NEB calculations, we estimate a zero-temperature activation energy of $E_a^0 = 0.09$ eV for lithium vacancies diffusing along the hexagonal $c$ direction (Fig.6a). This result is significantly smaller than the corresponding experimental value. Nevertheless, our AIMD simulations render $E_a = 0.36$ eV (Fig.6b), which is larger than $E_a^0$ and provides a better agreement with the experiments. Likewise, the calculated pre-exponential factor is $3.5 \cdot 10^{-4}$ cm²s⁻¹ and the resulting hopping attempt frequency $\sim 0.1$ THz. Large diffusion coefficients are estimated also for stoichiometric LiIO₃, although at temperatures well above ambient conditions (Fig.6b).

The VDOS calculated for non-stoichiometric LiIO₃ at

$T \neq 0$ conditions are reported in Supplementary Fig.5.
The total phonon band center amounts to 9.82 THz at room temperature and increases to 9.92 THz at $T =$ 700 K. Once again, the huge changes induced by temperature on the diffusion coefficient $(\Delta D/D \sim 10^3$ for $\Delta T = 400$ K) are not reflected on the corresponding VDOS $(\Delta\langle\omega\rangle/\langle\omega\rangle \sim 10^{-2}$ for the same $\Delta T)$. We also note that although the $E_a$ estimated for $LiIO_3$ is about two times larger than estimated for $Li_3N$, the average phonon frequency in the former compound is noticeably smaller (namely, 9.82 and 11.66 THz, respectively, at $T_{\rm room}$). In analogy to $LiGaO_2$, we find that the oxygen ions render the largest $\langle\omega\rangle$ whereas the heaviest cations the smallest ($\langle\omega\rangle_{\rm I} = 0.4\langle\omega\rangle_{\rm Li}$); in this case, the low-frequency lattice excitations ($\omega < 5$ THz) are clearly dominated by oxygen and iodine ions (Supplementary Fig.5).

### E. $Li_3OCl$

Similar to that of archetypal $ABO_3$ perovskite oxides [44, 61, 62]. Specifically, the Li, O, and Cl ions are placed at octahedral vertices, octahedral centers, and cube vertices, respectively. (We note that in our zero-temperature geometry relaxations the $Li_3OCl$ unit cell presents a $c/a$ ratio of 0.97; hence, our symmetry labelling as tetragonal $P4/mmm$ rather than as cubic $Pm\overline{3}m$.) The main mechanism for ion migration in $Li_3OCl$ has been proposed to be vacancy diffusion accompanied by anion disorder [24, 44, 63].

Our zero-temperature NEB calculations render $E_a^0 =$ 0.37 eV for lithium vacancy diffusion (Fig.7a), which is in good agreement with previous first-principles results [24, 63] and the experimental value $E_a^{\rm exp t} = 0.26$ eV [44]. Our AIMD simulations, however, provide a much larger value of the lithium migration enery barrier, namely, $E_a = 0.90$ eV (Fig.7b). The corresponding pre-exponential factor is very large as well, $D_0 = 1.4 \cdot 10^{-2}$ cm$^2$s$^{-1}$, which leads to a high hopping attempt frequency of $\sim 10$ THz (very similar to the one estimated previously for $LiGaO_2$). A possible cause for the large discrepancy between $E_a^{\rm exp t}$ and $E_a$ may be the presence of a higher concentration of anion disorder and lithium vacancies in the experimental samples (in our AIMD simulations we have considered only vacancies at a small concentration of $\sim 1\%$). Meanwhile, our AIMD simulations confirm that lithium diffusivity in stoichiometric $Li_3OCl$ is negligible [24, 63], even at high temperatures of $T > 1000$ K (Fig.7c).

The VDOS calculated for non-stoichiometric $Li_3OCl$ considering anharmonic and temperature effects are reported in Supplementary Fig.6. The total phonon band center amounts to 8.90 THz at $T = 1000$ K and increases to 9.08 THz at $T = 1250$ K. Like in the previous cases, the huge changes induced by temperature on the diffusion coefficient $(\Delta D/D \sim 10^1$ for $\Delta T = 250$ K) do not translate into significant VDOS variations $(\Delta\langle\omega\rangle/\langle\omega\rangle \sim 10^{-2}$ for the same $\Delta T)$. We also note that although the $E_a$ calculated for $Li_3ClO$ is about three times larger than estimated for $LiIO_3$, the total average phonon frequency of both compounds are quite similar (8.9 and 9.9 THz, respectively, at $T \sim 1000$ K). In analogy to previous cases, we find that the oxygen ions render the largest $\langle\omega\rangle$ whereas the heaviest cations the smallest ($\langle\omega\rangle_{\rm Cl} = 0.5\langle\omega\rangle_{\rm Li}$). On the other hand, the low-frequency lattice excitations ($\omega < 5$ THz) are dominated by lithium and chlorine ions (Supplementary Fig.6).

### IV. DISCUSSION

Table 1 encloses a summary of the main results obtained for the five lithium FIC analysed in this study. Next, we comment on (i) the importance of considering temperature effects on the estimation of migration activation energies and phonon frequencies in lithium FIC, and (ii) the correlations between superionic descriptors and lattice dynamics that can be deduced from our AIMD simulations.

### A. Temperature effects on $E_a$ and $\langle\omega\rangle$

The differences between columns $E_a^0$ and $E_a$ in Table 1, provide a quantitative estimate of how much temperature effects may influence the calculation of migration energy barriers in lithium FIC. In the present study, temperature effects account for as much as 35-80% of the final migration activation energies (straightforwardly estimated as $|E_a - E_a^0|/E_a$). Meanwhile, we have shown that, except for the $Li_3OCl$ case, inclusion of temperature effects always brings into better agreement the calculated and measured migration energy barriers (Table 1). Therefore, we argue that AIMD simulations are strongly recommended when pursuing accurate estimation of migration energy barriers (and of lithium diffusion mechanisms as well), in spite of the much larger computational load associated to them as compared to zero-temperature techniques. LiF, for example, illustrates very well the convenience of performing finite-temperature simulations. This material appears to be a very poor lithium-ion conductor [42, 57, 58], however, a relatively moderate migration energy barrier of $E_a^0 = 0.68$ eV is calculated for it with $T = 0$ K methods. Such a value turns out to be quite similar to the $E_a^0$ obtained for other promising ionic conductors (e.g., 0.78 eV for $LiGaO_2$ [41]), hence one could easily arrive at the wrong conclusion that LiF is a good superionic material.

Interestingly, we appreciate that the calculated $E_a$'s are systematically higher than the corresponding values estimated at zero temperature. This observation could be interpreted such that thermally activated anion lattice vibrations tend to deplete lithium transport (since in zero-temperature $E_a^0$ calculations the anion sublattice

![](./images/867765164282216582_8.jpg)

FIG. 7. (a) Activation energy for ion migration calculated for Li₃OCl at zero-temperature considering vacancy positions. (b) Lithium diffusivity of non-stoichiometric Li₃OCl calculated at finite temperatures. (c) Mean square displacement of stoichiometric Li₃OCl calculated at very high temperatures. Lithium, chlorine, and oxygen ions are represented with large green, small blue, and small red spheres, respectively. Lithium vacancy positions are indicated with black squares and mobile ions with purple spheres.

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>$E_a^0$ (eV)</th>
      <th>$E_a$ (eV)</th>
      <th>$E_a^{\text{expt}}$ (eV)</th>
      <th>$D_0$ (cm²/s)</th>
      <th>$\nu_0$ (s⁻¹)</th>
      <th>$\langle\omega\rangle_{\text{room}}$ (s⁻¹)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Li₃N</td>
      <td>0.03</td>
      <td>$0.15\pm0.01$</td>
      <td>0.45 [40]</td>
      <td>$2.5\pm1.0\cdot10^{-5}$</td>
      <td>$\sim10^{10}$</td>
      <td>$4.7\cdot10^{12}$</td>
    </tr>
    <tr>
      <td>LiGaO₂</td>
      <td>0.78</td>
      <td>$1.2\pm0.1$</td>
      <td>1.25 [41]</td>
      <td>$5.0\pm1.5\cdot10^{-2}$</td>
      <td>$\sim10^{13}$</td>
      <td>$4.4\cdot10^{12}$</td>
    </tr>
    <tr>
      <td>LiF</td>
      <td>0.68</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>$5.0\cdot10^{12}$</td>
    </tr>
    <tr>
      <td>LiIO₃</td>
      <td>0.09</td>
      <td>$0.36\pm0.07$</td>
      <td>0.26 [43]</td>
      <td>$3.5\pm1.5\cdot10^{-4}$</td>
      <td>$\sim10^{11}$</td>
      <td>$4.2\cdot10^{12}$</td>
    </tr>
    <tr>
      <td>Li₃OCl</td>
      <td>0.37</td>
      <td>$0.90\pm0.05$</td>
      <td>0.26 [44]</td>
      <td>$1.4\pm0.5\cdot10^{-2}$</td>
      <td>$\sim10^{13}$</td>
      <td>$4.4\cdot10^{12}$</td>
    </tr>
  </tbody>
</table>

TABLE I. Summary of the activation energies for ion migration calculated at zero and finite temperatures for the different lithium FIC considered in this study. Experimental values for $E_a$ are reported for comparison purposes. The accompanying pre-exponential factors of lithium diffusivity, $D_0$, and corresponding hopping attempt frequencies, $\nu_0$, are enclosed along with the energy scale of the lattice phonon excitations calculated at room temperature, $\langle\omega\rangle_{\text{room}}$ (estimated by using a frequency cut-off of $k_BT_{\text{room}}/\hbar$ on the total density of vibrational states).

vibrations are mostly neglected). However, other possible temperature effects associated to the diffusion of mobile ions (e.g., entropic stabilization of diverse transition paths) and the complex interactions between cations and anions, cannot be disregarded. In the next subsection, we will comment in detail on the correlations between lithium conductivity ($E_a$ and $D_0$) and $\langle\omega\rangle$ that can be drawn from our AIMD results.

With regard to the estimation of average phonon frequencies, we note that the harmonic approximation may be not adequate for describing lithium FIC due to the high degree of anharmonicity that superionic phases normally present [17, 35]. We have explicitly demonstrated this in Fig.1, where the zero-temperature vibrational spectrum of non-stoichiometric Li₃N is shown to contain a considerable number of imaginary phonon frequen-

![](./images/867765164282216582_9.jpg)

FIG. 8. Phonon band center versus the activation energy barrier for ion migration calculated in lithium FIC considering (a) all the atoms in the crystal, (b) only the Li ions, and (c) all the atoms in the crystal and a frequency cut-off of $k_B T_{room}/\hbar$. Solid lines are guides to the eye.

![](./images/867765164282216582_10.jpg)

cies, in contrast to the VDOS obtained under realistic $T \neq 0$ K conditions; we have checked that $LiIO_3$ and $Li_3OCl$ behave in a very similar manner (Supplementary Fig.7). In fact, the inherent limitations of the harmonic approximation may lead to misinterpretations of the vibrational stability of lithium FIC and to biased estimation of average phonon frequencies. For instance, we find that $\langle \omega \rangle$ is about $2\%$ larger for $Li_3N$ at zero temperature than at $T_{room}$, and that such discrepancies propagate to the partial VDOS. It goes without saying that the presence of negative phonon frequencies in zero-temperature VDOS automatically invalidates any estimation of $\langle \omega \rangle$, due to violation of the fundamental assumptions from which harmonic approaches are deduced [32, 33]. Correction of the explained computational artifacts (e.g., by using finite-temperature simulation methods as done here) is very important for an improved interpretation of experiments, since partial VDOS normally cannot be resolved directly from measurements and consequently first-principles calculations are employed for that end [20, 64].

### B. Lattice dynamics versus migration activation energy and pre-exponential factor

In Fig.8a, we plot the $E_a$ and $\langle\omega\rangle$ results obtained for the superionic compounds considered in this study. A direct correlation between migration activation energies and average phonon frequencies cannot be established. For instance, $\text{Li}_3\text{N}$ and $\text{LiGaO}_2$ present the smallest and largest $E_a$, respectively, with a large difference of $\sim 1$ eV, however the corresponding $\langle\omega\rangle$ turn out to be very similar. Likewise, one concludes the lack of any robust connection between either $\langle\omega\rangle_{\text{Li}}$ or $\langle\omega\rangle_{\text{room}}$ and $E_a$ (Figs.8b,c and Table 1). Hence, the recently suggested correspondence between lattice softness and low activation energies in superionic argyrodites and $\text{Li}_3\text{PO}_4$-based LISICON [19, 20] is not reproduced by our AIMD simulations and thereby should not be generalised to other families of lithium FIC. Actually, if $\text{LiGaO}_2$ was excluded from our analysis, we would arrive at the opposite conclusion that vibrationally rigid lattices, that is, larger $\langle\omega\rangle$, render smaller $E_a$ (see Fig.8a).

In previous sections we have shown that when lithium FIC are analysed individually, the large enhancements in ionic conductivity as induced by temperature are not accompanied by noticeable changes in VDOS. In particular, we have obtained large diffusivity variations of $\Delta D/D \sim 10^1 - 10^3$ and only minute vibrational changes of $\Delta\langle\omega\rangle/\langle\omega\rangle \sim 10^{-2}$. Hence, the generalised insensitivity of $\langle\omega\rangle$ for large $D$ fluctuations observed in all individual materials, already suggests the lack of a direct correlation between $E_a$ and $\langle\omega\rangle$ across different families of lithium FIC.

Supplementary Fig.8 encloses the $D_0$ and $\langle\omega\rangle$ results obtained for the superionic compounds investigated in this study. Once again, we cannot determine any rigorous correspondence between the two represented quantities. We note that the calculated hopping attempt frequencies fluctuate between 0.01 and 10 THz whereas all the estimated $\langle\omega\rangle$ consistently amount to $\sim 10$ THz (Table 1). Therefore, lithium hoppings and lattice vibrations may operate at very different time scales, which could relate to the cause of their disconnection.

### C. Hopping attempt frequency versus $E_a$

The similarity of the $E_a$-$\langle\omega\rangle$ and $D_0$-$\langle\omega\rangle$ trends shown in Fig.8a and Supplementary Fig.8 respectively, appears to suggest some sort of correlation between $E_a$ and $D_0$. In fact, the conventional hopping theory developed by Rice and Roth provides the well known, and usually reported, relationship $D_0 \propto \sqrt{E_a}$ [65]. However, we should note that conventional hopping theory was originally developed to understand ionic transport in AgI and other analogous type-I FIC [1, 8], in which the superionic transition is accompanied by a first-order structural transformation affecting the static sublattice (in contrast to lithium FIC, typically referred to as type-II, in which the superionic transition normally is of second-order type and mostly affects the mobile ions [1, 8]). Moreover, a recent experimental study by Muy *et al.* has provided solid evidence showing that the actual interplay between $D_0$ on $E_a$ may be more complex than previously thought [45].

Figure 9a reports the $D_0$ and $E_a$ results that we have obtained in this study. In this case, the two represented quantities appear to be correlated since larger migration activation energies systematically are accompanied by larger pre-exponential factors. However, we note that the usually reported relationship $D_0 \propto \sqrt{E_a}$ [65] clearly does not pertain here (we recall that the $y$-axes in Fig.9 are in logarithmic scale). Rather, the dependence of $D_0$ on $E_a$ appears to be exponential like. Recently, Muy *et al.* have shown that the diffusion pre-exponential factors of a large number of LISICON compounds seem to follow the Meyer-Neldel rule $D_0 \propto \exp(E_a/\langle\omega\rangle)$ [45]. In fact, when we represent the computed diffusion pre-exponential factors as a function of the quantity $E_a/\langle\omega\rangle$ we find a perfect agreement with the Meyer-Neldel rule within our numerical uncertainties (see linear fit in Fig.9b). Our theoretical findings confirm Muy *et al.*'s conclusions reported in work [45] and demonstrate that Rice and Roth's hopping theory in general is not adequate for describing lithium FIC (as it could have been foreseen, see explanations in previous paragraph).

The results and discussions presented thus far let us to conclude the following: lattice softness can be identified with enhanced lithium diffusivity but only within families of superionic materials presenting very similar migration activation energies, due to superior $D_0$ (as given by the Meyer-Neldel rule). We should note that according to our zero-temperature and AIMD simulations lithium partial occupancy in FIC can be identified with larger anharmonicity, or equivalently, smaller $\langle\omega\rangle$. For instance, the average phonon frequency calculated for non-stoichiometric $\text{Li}_3\text{N}$ at finite temperatures is about 1% lower than the estimated for the analogous stoichiometric system. Hence, lattice softness may indeed be a key factor for better understanding the ionic transport differences between chemically similar stoichiometric and non-stoichiometric lithium FIC [45].

---

### V. CONCLUSIONS

We have performed a comprehensive first-principles study of several lithium FIC at finite temperatures. Based on our AIMD results, it has not been possible to establish any direct correlation between either $E_a$ or $D_0$ and $\langle\omega\rangle$, in disagreement with recent experimental findings reported for superionic argyrodites and $\text{Li}_3\text{PO}_4$-based LISICON. Nevertheless, the three quantities of interest appear to be related by the Meyer-Neldel rule, in accordance with recent measurements; hence, on a general scale it is possible to identify lattice softness with enhanced ionic conductivity but only within families of FIC

presenting very similar migration activation energies, ow- ing to an increase in the hopping attempt frequency. In- terestingly, we have shown that the spectra of lattice vi- brations in lithium FIC generally are very insensitive to temperature changes, in contrast to what is observed for ionic transport. On the technical side, we have demon- strated that zero-temperature methods present some in- herent limitations for describing Li-based FIC. In partic- ular, migration activation energies can be seriously un- derestimated due to the neglection of temperature effects, and harmonic approaches may be ill-defined due to the prominent role of anharmonicity in FIC. We hope that our theoretical findings will help at establishing phys- ically meaningful relationships between ionic transport and simple materials descriptors in lithium FIC. Also, we expect to promote a wider use of finite-temperature approaches in first-principles modeling of fast-ion con- ductors.

[1] S. Hull, Rep. Prog. Phys. **67**, 1233 (2004).

[2] C. Cazorla and D. Errandonea, Phys. Rev. Lett. **113**, 235902 (2014).

[3] D. A. Keen, S. Hull, W. Hayes, and N. J. G. Gardner, Phys. Rev. Lett. **77**, 4914 (1996).

[4] Y. Inaguma, C. Liquan, M. Itoh, T. Nakamura, T. Uchida, H. Ikuta, and M. Wakihara, Solid State Com- mun. **86**, 689 (1993).

[5] J. C. Bachman, S. Muy, A. Grimaud, H.-H. Chang, N. Pour, S. F. Lux, O. Paschos, F. Maglia, S. Lupart, P. Lamp, L. Giordano, and Y. Saho-Horn, Chem. Rev. **116**, 140 (2016).

[6] R. M. Ormerod, Chem. Soc. Rev. **32**, 17 (2003).

[7] C. Cazorla and D. Errandonea, Nano Letters **16**, 3124 (2016).

[8] A. K. Sagotra, D. Errandonea, and C. Cazorla, Nat. Commun. **8**, 963 (2017).

[9] A. Aznar, P. Lloveras, M. Romanini, M. Barrio, J. Ll. Tamarit, C. Cazorla, D. Errandonea, N. D. Mathur, A. Planes, X. Moya, and Ll. Manosa, Nat. Commun. **8**, 1851 (2017).

[10] A. K. Sagotra, D. Chu, and C. Cazorla, Nat. Commun. **9**, 3337 (2018).

[11] T. Montini, M. Melchionna, M. Monai, and P. Fornasiero, Chem. Rev. **116**, 5987 (2016).

[12] J. B. Goodenough, Solid State Ion. **17**, 94 (1997).

[13] Y. Wang, W. D. Richards, S. P. Ong, L. J. Miara, J. C. Kim, Y. Mo, and G. Ceder, Nat. Mater. **14**, 1026 (2015).

[14] R. Xiao, H. Li, and L. Chen, J. Materiomics **1**, 325 (2015).

[15] P. Goel, M. K. Gupta, R. Mittal, S. Rols, S. J. Patwe, S. N. Achary, A. K. Tyagi, and S. L. Chaplot, J. Mater. Chem. A **2**, 14729 (2014).

[16] T. Krauskopf, C. Pompe, M. A. Kraft, and W. G. Zeier, Chem. Mater. **29**, 8859 (2017).

[17] C. Cazorla and D. Errandonea, Phys. Rev. B **98**, 186101 (2018).

[18] H. Fang and P. Jena, Proc. Natl. Acad. Sci. **114**, 11046 (2017).

[19] M. A. Kraft, S. P. Culver, M. Calderon, F. Bocher, T. Krauskopf, A. Senyshyn, C. Dietrich, A. Zevalkink, J. Janek, and W. G. Zeier, J. Am. Chem. Soc. **139**, 10909 (2017).

[20] S. Muy, J. C. Bachman, L. Giordano, H.-H. Chang, D. L. Abernahy, D. Bansal, O. Delaire, S. Hori, R. Kanno, F. Maglia, S. Lupart, P. Lamp, and Y. Shao-Horn, Energy Environ. Sci. **11**, 850 (2018).

[21] K. Wakamura, Phys. Rev. B **56**, 11593 (1997).

[22] X. He, Y. Zhu, and Y. Mo, Nat. Commun. **8**, 15893 (2017).

[23] Y. Mo, S. P. Ong, and G. Ceder, Chem. Mater. **24**, 15 (2012).

[24] Y. Zhang, Y. Zhao, and C. Chen, Phys. Rev. B **87**, 134303 (2013).

[25] C. Cazorla, A. K. Sagotra, M. King, and D. Errandonea, J. Phys. Chem. C **122**, 1267 (2018).

[26] G. Henkelman, B. P. Uberuaga, and H. Jonsson, J. Chem. Phys. **113**, 9901 (2000).

[27] A. K. Sagotra and C. Cazorla, ACS Appl. Mater. Interf. **9**, 38773 (2017).

[28] J. P. Goff, W. Hayes, S. Hull, and M. T. Hutchings, J. Phys.: Condens. Matt. **3**, 3677 (1991).

[29] M. J. Castiglione and P. A. Madden, J. Phys.: Condens. Matt. **13**, 9963 (2001).

[30] L.-W. Wang, Phys. Rev. Lett. **108**, 085703 (2012).

[31] J. Yang and J. S. Tse, J. Phys. Chem. A **115**, 13045 (2011).

[32] C. Cazorla and J. Boronat, Rev. Mod. Phys. **89**, 035003 (2017).

[33] C. Cazorla and J. & Íñiguez, Phys. Rev. B **88**, 214430 (2013).

[34] C. Cazorla, O. Dieguez, and J. Íñiguez, Sci. Adv. **3**, e1700288 (2017).

[35] M.-H. Chen, A. Emly, and A. Van der Ven, Phys. Rev. B **91**, 214306 (2015).

[36] N. J. J. Klerk, E. van der Maas, and M. Wagemaker, ACS Appl. Energy Mater. **1**, 3230 (2018).

[37] B. Singh, M. K. Gupta, R. Mittal, and S. L. Chaplot, J. Mater. Chem. A **6**, 5052 (2018).

[38] W. D. Richards, T. Tsujimura, L. J. Miara, Y. Wang, J. C. Kim, S. P. Ong, I. Uechi, N. Suzuki, and G. Ceder, Nat. Commun. **7**, 11009 (2016).

[39] L. Kahle, A. Marcolongo, and N. Marzari, Phys. Rev. Mater. **2**, 065405 (2018).

[40] W. Li, G. Wu, C. M. Araujo, R. H. Scheicher, A. Blomqvist, R. Ahuja, Z. Xiong, Y. Feng, and P. Chen, Energy Environ. Sci. **3**, 1524 (2010).

[41] M. M. Islam, J. Uhlendorf, E. Witt, H. Schmidt, P. Heitjans, and T. Bredow, J. Phys. Chem. C **121**, 27788 (2017).

[42] H. Yildirum, A. Kinaci, M. K. Y. Chan, and J. P. Greeley, ACS Appl. Mater. Interfaces **7**, 18985 (2015).

[43] A. E. Aliev, A. Sh. Akramov, L. N. Fershtat, and P. K. Khabibullaev, Phys. Stat. Sol. (a) **108**, 189 (1988).

[44] Y. Zhao and L. L. Daemen, J. Am. Chem. Soc. **134**, 15042 (2012).

[45] S. Muy, J. C. Bachman, H.-H. Chang, L. Giordano, F. Maglia, S. Lupart, P. Lamp, W. G. Zeier, and Y. Shao- Horn, Chem. Mater. 30, 5573 (2018).

[46] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[47] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[48] S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem. Phys. 132, 154104 (2010).

[49] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

[50] G. Kresse, J. Furthmüller, and J. Hafner, Europhys. Lett. 32, 729 (1995).

[51] D. Alfè, Comp. Phys. Commun. 180, 2622 (2009).

[52] U. V. Alpen, A. Rabenau, and G. H. Talat, Appl. Phys. Lett. 30, 621 (1977).

[53] G. A. Nazri, C. Julien, and H. S. Mavi, Sol. Stat. Ionics 70, 137 (1994).

[54] L. Sun, D. Marrocchelli, and B. Yildiz, Nat. Commun. 6, 6294 (2015).

[55] K. K. Adepalli, J. Yang, J. Maier, H. L. Tuller, and B. Yildiz, Adv. Funct. Mater. 27, 1700243 (2017).

[56] M. Y. Nie, D. Chalasani, D. P. Abraham, Y. J. Chen, A. Bose, and B. L. Lucht, J. Phys. Chem. C 117, 1257 (2013).

[57] J. Pan and Y.-T. Cheng, Phys. Rev. B 91, 134116 (2015).

[58] F. A. Soto, A. Marzouk, F. El-Mellouhi, and P. B. Bal- buena, Chem. Mater. 30, 3315 (2018).

[59] J. K. Liang, G. H. Rao, and Y. M. Zhang, Phys. Rev. B 39, 459 (1989).

[60] W. W. Zhang, Q. L. Cui, Y. W. Pan, S. S. Dong, J. Liu, and G. T. Zou, J. Phys.: Condens. Matter 14, 10579 (2002).

[61] C. Cazorla and M. Stengel, Phys. Rev. B 92, 214108 (2015).

[62] C. Cazorla and M. Stengel, Phys. Rev. B 90, 020101(R) (2014).

[63] Z. Lu, C. Chen, Z. M. Baiyee, X. Chen, C. Niu, and F. Ciucci, Phys. Chem. Chem. Phys. 17, 32547 (2015).

[64] T. Krauskopf, S. Muy, S. P. Culver, S. Ohno, O. De- laire, Y. Shao-Horn, and W. G. Zeier, J. Am. Chem. Soc. doi:10.1021/jacs.8b09340 (2018).

[65] M. J. Rice and W. L. Roth, J. Sol. Stat. Chem. 4, 294 (1972).

## ACKNOWLEDGMENTS

This research was supported under the Australian Re- search Council's Future Fellowship funding scheme (No. FT140100135). Computational resources and technical assistance were provided by the Australian Government and the Government of Western Australia through the National Computational Infrastructure (NCI) and Mag- nus under the National Computational Merit Allocation Scheme and The Pawsey Supercomputing Centre.