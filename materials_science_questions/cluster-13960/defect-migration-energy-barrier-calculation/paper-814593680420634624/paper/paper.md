# Influence of dislocation strain fields on the diffusion of interstitial iron impurities in silicon

Benedikt Ziebarth, $^{1,2,*}$ Matous Mrovec, $^{1,\dagger}$ Christian Elsässer, $^{1}$ and Peter Gumbsch $^{1,2}$

$^{1}$ Fraunhofer-Institut für Werkstoffmechanik IWM, Wöhlerstraße 11, 79108 Freiburg, Germany
$^{2}$ Institut für Angewandte Materialien (IAM), Karlsruher Institut für Technologie, Engelbert-Arnold-Straße 4, 76131 Karlsruhe, Germany

(Received 31 July 2015; published 22 September 2015)

The efficiency of silicon (Si)-based solar cells is strongly affected by crystal defects and impurities. Metallic impurities, in particular interstitial iron (Fe) atoms, cause large electric losses because they act as recombination centers for photogenerated charge carriers. Here, we present a systematic first-principles density functional theory (DFT) study focusing on the influence of hydrostatic, uniaxial, and shear strains on the thermodynamic stability and the diffusivity of Fe impurities in crystalline Si. Our calculations show that the formation energy of neutral Fe interstitials in tetrahedral interstitial sites is almost unaffected by uniform deformations of the Si crystal up to strains of 5%. In contrast, the migration barrier varies significantly with strain, especially for hydrostatic deformation. In order to determine effective diffusion coefficients for different strain states, a kinetic Monte Carlo (kMC) model was set up based on the activation energy barriers and frequency factors obtained from the DFT simulations. By using the strain dependence of the migration barrier, we examined the migration of Fe interstitials in the vicinity of perfect $1/2\langle 110\rangle$ screw and $60^{\circ}$ mixed dislocations, and $1/6\langle 112\rangle90^{\circ}$ and $30^{\circ}$ partial dislocations. While the strain field of the perfect screw dislocation always enhances the local Fe diffusion, the existence of tensile and compressive regions around the $60^{\circ}$ mixed dislocation results in a strong anisotropic diffusion profile with significantly faster and slower diffusivities on its tensile and compressive sides. The influences of the partial dislocations are qualitatively similar to that of the $60^{\circ}$ mixed dislocation.

DOI: 10.1103/PhysRevB.92.115309
PACS number(s): 88.40.jj, 62.20.-x, 71.55.Ak, 71.15.Mb

## I. INTRODUCTION

The economically most important feed-stock material for silicon-based solar cells is metallurgical multicrystalline sili- con (mc-Si). Unfortunately, this relatively cheap material con- tains large concentrations of metallic impurities, which cause electrical efficiency losses either by acting as recombination centers [1–5] or by forming second-phase precipitates [6,7].

One of the most detrimental impurities is interstitial Fe. Even though many of its negative influences are well under- stood [1,2], some fundamental mechanisms associated with thermodynamic and kinetic aspects of the Fe-Si interaction are still a matter of debate [8–10]. For instance, little effort has been made to study the effect of mechanical stress on the segregation and diffusion of Fe in Si even though experiments show a preferential agglomeration of metallic impurities in regions of high local strains [11] associated with dislocations [12], grain boundaries [13,14], and other extended defects such as precipitates [15].

In particular the interactions between metallic impurities and dislocations, which are characterized by narrow cores as well as long-range elastic strain fields, present a challenging problem. Metallic impurities tend to preferentially segregate at dislocation cores but are also attracted by strain fields around dislocations [9,16–18]. The segregated impurity atoms may either enhance or inhibit elementary dislocation processes such as glide, climb, or cross slip, and hence affect the dislocation density during processing of mc-Si [19,20]. In addition, the lattice distortions around dislocations are suspected to influ- ence the migration barriers for diffusing interstitial impuri- ties [9,16]. The presence of dislocations can therefore strongly affect the thermodynamic and kinetic aspects of the impurity distribution in the material. For instance, dislocation clusters are known to act as favorable seeds for precipitation of iron silicide particles in mc-Si [18,21]. However, the understanding of the underlying atomic-scale mechanisms associated with the dislocation-impurity interactions is still incomplete.

In this work, we investigate the effect of mechanical strain on the behavior of interstitial Fe impurities in bulk Si by means of first-principles calculations based on density functional theory (DFT). Two main aspects are considered: (i) the thermodynamic stability of Fe impurities at finite temperatures and various strain states, and (ii) the effect of strain on Fe diffusion. In order to determine effective diffusion coefficients for different strain states, a kinetic Monte Carlo (kMC) model was set up based on the activation energy barriers and frequency factors obtained from the DFT simulations. By using the strain dependence of the migration barriers, we examine Fe migration in the long-range strain fields of perfect as well as dissociated $\frac{1}{2}\langle 110\rangle$ screw and $60^{\circ}$ mixed dislocations outside of their core regions.

The paper is organized as follows: in Sec. II, the com- putational methods and the structural model are described. Thermodynamic properties of Fe impurities at finite tempera- tures and various strain states are reported in Sec. III. Results for the diffusion of interstitial Fe in a strained perfect crystal are presented in Sec. IV. Section V addresses the diffusion of Fe atoms in strain fields of dislocations in Si. The results are discussed in Sec. VI, and the work is summarized in Sec. VII.

## II. COMPUTATIONAL METHODS AND STRUCTURAL MODEL

### A. Computational methodology

All DFT calculations were carried out using the Quantum Espresso PWscf code [22], which uses a plane-wave basis to

*Benedikt.Ziebarth@iwm.fraunhofer.de
†matous.mrovec@iwm.fraunhofer.de

1098-0121/2015/92(11)/115309(11)
115309-1
©2015 American Physical Society

<table><caption>Table I. Cubic elastic constants and bulk modulus of bulk Si (in GPa).</caption>
<tbody><tr><th>[GPa]</th><td>Calc.</td><td>Exp. [29]</td></tr>
<tr><th>$C_{11}$</th><td>149</td><td>165.6</td></tr>
<tr><th>$C_{12}$</th><td>59</td><td>63.9</td></tr>
<tr><th>$C_{44}$</th><td>99</td><td>79.5</td></tr>
<tr><th>$B$</th><td>89</td><td>97.8</td></tr>
</tbody></table>

represent the wave functions of the valence electrons. Interactions of ionic cores and valence electrons were described by ultrasoft pseudopotentials. The PBE generalized gradient approximation was used for exchange-correlation [23,24]. All calculations for supercell models containing Fe atoms were carried out as spin-polarized. Energy cutoffs of 35 Ry and 350 Ry for the plane-wave basis and electron-density Fourier expansion, respectively, were found to yield converged total energies within an accuracy of 0.005 eV. The Brillouin-zone integrals were calculated on a $4×4×4$ Monkhorst-Pack grid [25] with a Gaussian broadening of 0.25 eV. Atom positions were relaxed until the residual forces acting on the atoms were less than $10^{-3}$ eV/Å and the total energy was converged to $10^{-5}$ eV. The minimum energy paths (MEPs) for jumps of Fe atoms between neighboring sites were calculated using the nudged elastic band (NEB) method [26]. In addition, the climbing image NEB (CI-NEB) method was applied to ensure an accurate determination of the migration barriers [26]. The threshold for the total forces, which are acting on the NEB images of an interpolated reaction path, was set to 0.05 eV/Å.

### B. Structural models
In all DFT calculations, a cubic diamond supercell with 64 Si atoms was used. Validation calculations for several structures with a larger supercell containing 96 Si atoms yielded identical results. The calculated equilibrium value of the cubic lattice constant is 5.467 Å, which is in agreement with experimental (5.431 Å [27]) and other calculated data (5.469 Å [28]). Calculated values of the cubic elastic constants also agree reasonably well with experimental data (cf. Table I; the deviations are typical for DFT results within the generalized gradient approximation).

### C. Diffusion at the atomic scale
Diffusion at the atomic scale happens by thermally activated jumps of atoms. The rate $\Gamma$ of such an atomic jump can be described by the transition state theory (TST) [30] as
$$
\Gamma=v e^{-\Delta E / k_{B} T}, \quad(1)
$$
in which $v$ is the frequency factor, $\Delta E$ is the migration energy barrier along the path, $k_{B}$ is the Boltzmann constant, and $T$ is the absolute temperature.

In this work, the energy barriers for atomic jumps between interstitial sites were obtained from minimum-energy-path calculations using the CI-NEB method [26]. The frequency factors were obtained for given $q$ points in the phonon Brillouin zone (BZ) from products of phonon frequencies at the stable initial-state configuration $v^{0}$ and at the transition-state configuration $v^{\dagger}$ as [30]
$$
v_{q}=\frac{\prod_{i=0}^{3 N_{\text {atoms }}} v_{i}^{0}(q)}{\prod_{j=0}^{3 N_{\text {atoms }}-1} v_{j}^{\dagger}(q)}. \quad(2)
$$

In a system of $N_{\text {atoms }}$ atoms, there are $3 N_{\text {atoms }}$ vibration frequencies for each $q$ point in the BZ. In the transition configuration, the imaginary frequency associated with the unstable mode is excluded from the product in Eq. (2). The frequency factor $v$ in Eq. (1) is obtained by averaging a sample set of $v_{q}$'s evaluated on a Monkhorst-Pack mesh of $N_{q} q$ points in the BZ [25]:
$$
v=\frac{1}{N_{q}} \sum_{i=0}^{N_{q}} v_{q}. \quad(3)
$$

### D. Kinetic Monte Carlo
Diffusion coefficients can be calculated analytically for perfect crystals with only one relevant migration process for the diffusing species. However, alloying elements, the presence of structural defects, and the application of external stresses give rise to nonuniform deformations that make the migration pathways in a crystal nonequivalent. In these cases, more sophisticated approaches, such as kinetic Monte Carlo simulations [31–35], are needed to extract the diffusion behavior.

Within the kMC approach, the actual crystal system is mapped on a lattice and the trajectory of the diffusing particle is evolved by stochastic events with known jump rates. For the case of interstitial diffusion, the interstitial sites form the kMC lattice on which the migrating atoms can jump according to the TST. To evolve such a system for a given configuration, the sum of the rates of all accessible jump events, $\Gamma_{\text {total }}$, is calculated. Subsequently, a uniformly distributed random number $r$ between 0 and 1 is generated and the $p$th jump event is chosen according to
$$
\sum_{i=0}^{p-1} \Gamma_{i}<r \Gamma_{\text {total }} \leqslant \sum_{i=0}^{p} \Gamma_{i}. \quad(4)
$$

Since the reaction rates are constant and independent of the system's history, the process is a Poisson process [36] and, hence, the evolution for the $n$th kMC step in real time is given by
$$
t_{n}=t_{n-1}-\Gamma_{\text {total }} \ln r^{\prime}, \quad(5)
$$
where $r'$ is another uniformly distributed random number between 0 and 1. From the final trajectory, one can obtain observables such as the diffusivity or the probability to find a particle at a given site. The observables are acquired from averages of an ensemble of trajectories to ensure their convergence.

Diffusion constants are obtained from mean-square displacements, $\Delta r_{i}^{2}$, of all the diffusing particles by
$$
D=\sum_{i=0}^{N_{\text {particles }}} \frac{\Delta r_{i}^{2}}{2 N t_{\text {total }}}, \quad(6)
$$
where $N_{\text {particles }}$ is the number of diffusing particles in the system and $t_{\text {total }}$ is the total time of the trajectory.

![](./images/814593680420634624_1.jpg)

FIG. 1. (Color online) Four different configurations of Fe impurities (red spheres) in the diamond structure of Si (blue spheres) are shown. The local coordination shell is depicted as a red polyhedron. The pictures show a projection along the [110] direction.

## III. THERMODYNAMICS OF IRON IMPURITIES IN SILICON

### A. Temperature dependence of defect formation energies for iron impurities

Previous studies [1,37,38] have shown that Fe impurities in bulk Si can be located in three different configurations. The Fe atom can occupy either interstitial sites with tetrahedral $T_d$ or trigonal $D_{3d}$ symmetries [39] (the trigonal site is commonly called "hexagonal" due to its six Si neighbors) or Fe can substitute Si on regular sites. These three configurations are displayed in Fig. 1 together with a configuration of the transition state (marked as TRA in the following) between the tetrahedral and hexagonal sites (see discussion bellow).

In a perfect Si single crystal, the tetrahedral (TET) site is known to be energetically more favorable for the interstitial Fe than the hexagonal (HEX) site [37]. Our calculated energy difference between the TET and HEX configurations of 0.60 eV agrees well with the value of 0.57 eV obtained in previous DFT calculations [37]. It has also been reported that interstitial Fe atoms will preferentially occupy Si vacancies [forming substitutional (SUB) Fe defects] rather than forming a defect complex with the Si vacancy [38].

The formation energy $E_f$ of a defect configuration can be calculated as
$$
E_f = E^{\text{total}} - N_{\text{Si}}\mu_{\text{Si}} - N_{\text{Fe}}\mu_{\text{Fe}}, \tag{7}
$$
where $E^{\text{total}}$ is the total (internal) energy of the supercell with the Fe impurity, $N_{\text{Si}}$ and $N_{\text{Fe}}$ are the numbers of Si and Fe atoms in the supercell, respectively, and $\mu_{\text{Si}}$ and $\mu_{\text{Fe}}$ are the chemical potentials for Si and Fe, respectively. In our calculations, $\mu_{\text{Si}}$ has been chosen to be equal to the chemical potential of Si in the crystalline equilibrium diamond structure, and $\mu_{\text{Fe}}$ such that the formation energy of an interstitial Fe atom at a tetrahedral site in a Si single crystal is zero. This corresponds to the Si-rich limit of the binary Si-Fe system. In unstrained Si, we obtained formation energies of 0.0, 0.70, 0.56, and 0.76 eV for all the TET, TRA, HEX, and SUB defects, respectively. The calculated values for excess volumes for these defects turned out to be negligibly small. The formation energy of a SUB defect includes the formation energy of the Si vacancy.

In order to take into account finite-temperature effects, we also investigated the phonon contributions to the defect formation energies [40]. The phonon densities of states for the different defect configurations and for the perfect Si crystal were calculated, using the Phonopy software package [41], from the dynamical matrix obtained from finite atomic displacements in the harmonic approximation [40,42]. Atomic displacements from equilibrium positions were set to $0.05\ \mathring{\text{A}}$. From the phonon density of states, it is straightforward to calculate the free energy of defect formation for a given temperature [43]. The calculated temperature dependencies of the free energies for the four defect configurations are shown in Fig. 2. Since all four curves look very similar, the relative energy differences between the defect configurations are almost independent of temperature. Hence, it is reasonable to assume that temperature does not affect significantly the hierarchy of defect formation energies for Fe impurities in bulk Si, and therefore the temperature dependence is not further taken into account.

### B. The effect of strain on the defect-formation energy of Fe impurities

In order to investigate the effect of elastic strain $\varepsilon$ on the defect formation energies, different uniform strain states with strain magnitudes ranging between $-5\%$ and $+5\%$ were applied. The considered strain modes were: hydrostatic strain $\varepsilon_{\text{Hyd}}$, uniaxial strains $\varepsilon_{[100]}$, $\varepsilon_{[110]}$, $\varepsilon_{[111]}$, $\varepsilon_{[112]}$, and shear strains $\tau_{[010],[001]}$, $\tau_{[112],[111]}$, $\tau_{[\overline{1}10],[112]}$, $\tau_{[111],[\overline{1}10]}$. Strain is applied by

![](./images/814593680420634624_2.jpg)

FIG. 2. (Color online) Temperature dependencies of the free energies of defect formation for the four different Fe defect configurations.

the deformation of the conventional cubic fcc unit cell with a lattice constant of $a_0$ and cell vectors [44],
$$
\mathbf{a}=\begin{pmatrix}
\mathbf{a}_1 \\
\mathbf{a}_2 \\
\mathbf{a}_3
\end{pmatrix}=\begin{pmatrix}
a_0 & 0 & 0 \\
0 & a_0 & 0 \\
0 & 0 & a_0
\end{pmatrix}, \tag{8}
$$
by applying a deformation matrix $\mathbf{D}$ such that new cell vectors $\mathbf{a}'$ are
$$
\mathbf{a}'=(\mathbf{I}+\mathbf{D}) \cdot \mathbf{a}, \tag{9}
$$
where $\mathbf{I}$ is the identity matrix. The deformation matrices are given in the Appendix. In addition to the formation energies of interstitial Fe defects, the formation energies of substitutional Fe defects and Si vacancies were also calculated. As mentioned above, the Si-vacancy + Fe-interstitial complex is not as stable as a Fe-substitutional unstrained Si, but this relative stability may be altered by applied strains. For the calculations of the formation energies under external strain, we always set the chemical potential of Si [$\mu_{\text{Si}}$ in Eq. (7)] at the same strain state as for the perfect Si crystal containing the Fe impurity. The defect formation energies for all applied strain modes are displayed in Fig. 3. Note that the energy scales for the Fe impurities are different from that for the Si vacancy.

Due to the lattice symmetry, the tetrahedral interstitial sites in bulk Si remain equivalent for arbitrary homogeneous strain. In contrast, the hexagonal interstitial sites become nonequivalent depending on the strain state of the system.

![](./images/814593680420634624_3.jpg)

FIG. 3. (Color online) Formation energies of the different Fe defects and the Si vacancy in Si for different strain states. The energy scale for the Fe impurities is on the left side and the energy scale for the Si vacancy is on the right side. Negative strain corresponds to compression and positive strain corresponds to expansion.

![](./images/814593680420634624_4.jpg)

FIG. 4. (Color online) The interstitial tetrahedral site (red sphere) in Si is connected via hexagonal sites (small black spheres) in $\langle 111 \rangle$ directions with four neighboring tetrahedral sites.

The four differently oriented hexagonal sites in the rectangular supercell system differ by the orientation of their large facet, which is orthogonal to one of the following four directions: $[111]$, $[\overline{1}11]$, $[1\overline{1}1]$, and $[11\overline{1}]$ (see Fig. 4). These four hexagonal sites are therefore labeled in the following by their directions from the tetrahedral site.

As displayed in Fig. 3, the formation energy for the TET configurations remains almost constant for all investigated strain states. The strain dependencies for the HEX configurations follow linear relations in the cases of hydrostatic and uniaxial strains. The largest change in the interstitial formation energies is for the hydrostatic strain, for Fe at the HEX site it changes by almost 1.2 eV over the range of $\pm 5\%$ strain. In the case of uniaxial strains, the changes are only by about 0.5 eV for the same strain range. For shear strains, the HEX formation energies depend nonlinearly on the strain with maximum variations reaching also about 0.5 eV (e.g., for the $\tau_{[010],[001]}$). In all cases, there is at least one hexagonal site that shows a reduction in the formation energy during shear.

The formation energies for the Fe substitutional and the Si vacancy follow similar parabolic trends, but the variations are more pronounced for the latter. In all investigated cases, the transformation of a Fe-substitutional into an Si-vacancy + Fe-interstitial defect complex is unlikely because the formation energy for substitutional (SUB) Fe remains smaller than the sum of the formation energies of the interstitial TET Fe and the Si vacancy.

The formation energies for charged $\text{Fe}^+$ defects in Si have not been calculated because $\text{Fe}^+$ is mainly present in p-doped Si and forms defect clusters with shallow acceptors such as boron [1,37]. In order to accurately describe the energetics and kinetics of charged $\text{Fe}^+$, it would therefore be necessary to consider such defect clusters of Fe with B. This is not in the scope of the present work.

### IV. DIFFUSION OF IRON IN STRAINED SILICON

To analyze the migration of Fe impurities in Si, we first determined the frequency factors for the $\text{TET} \rightarrow \text{HEX}$ and $\text{HEX} \rightarrow \text{TET}$ jumps from phonons according to Eqs. (2) and (3). For the unstrained Si crystal, we obtained frequency factors of $\nu_{\text{TET} \rightarrow \text{HEX}} = 30$ THz and $\nu_{\text{HEX} \rightarrow \text{TET}} = 18$ THz. For simplicity, the frequency factors for Fe are taken to be the same as well for the strained cases in the following.

The MEPs and associated migration barriers for Fe jumps between the interstitial TET and HEX sites were calculated using the CI-NEB method for all investigated strain states but

![](./images/814593680420634624_5.jpg)

FIG. 5. (Color online) Minimum energy paths for interstitial Fe migration between two tetrahedral sites for different uniaxial [100] strains.

only for the three strain magnitudes of $-5\%$, 0, and $+5\%$. For illustration, the MEPs for different uniaxial [100] strains are shown in Fig. 5. The migration barrier decreases for tension and increases for compression. The HEX site corresponds to a local energy minimum and its relative stability with respect to the TET site depends strongly on the applied strain.

All computed energy barriers are compiled in Fig. 6. The reference energy barrier for Fe diffusion from a TET to a HEX site in unstrained bulk Si amounts to 0.74 eV while the barrier height for the reverse jump (HEX to TET) is only 0.19 eV. The largest changes in the energy barriers are observed for the hydrostatic strain. The energy barrier between the TET and HEX sites decreases to about 0.3 eV for $+5\%$ strain while the energy barrier for the reverse direction increases to about 0.25 eV. For negative strain of $-5\%$, the energy barrier between the TET and HEX sites increases to about 1.20 eV, for the reverse direction the energy barrier almost vanishes. A similar but less pronounced change is found for uniaxial strain. Some of the deformations, e.g., uniaxial strain along the [111] direction, do not conserve the equivalence of the hexagonal sites, and thus different energy barriers for different directions are obtained. For all shear strains, the migration barriers are reduced for both directions. Again, the magnitude of the reduction depends specifically on both the elastic shear direction and the geometric jump direction. This is of particular interest because it is not reflected in the formation energies shown in Fig. 3, i.e., the formation energy for the HEX site increases with strain whereas the energy barrier decreases for both jump directions.

To investigate the influence of the migration barrier changes on the diffusion of Fe, lattice-based numerical kMC simulations were employed. A rate table for the different migration directions was set up using Eq. (1) with the calculated energy barriers from Fig. 6 and the frequency factors given above for the unstrained supercell. The diffusion constants (with a standard deviation lower than $1\%$) for different strain states were obtained by averaging one hundred kMC runs (each having one million kMC steps) according to Eqs. (4)–(6).

Figure 7 displays the temperature dependencies of the diffusion coefficient (with respect to the diffusion coefficients of interstitial Fe in unstrained bulk Si) for all investigated strain types. Despite the consideration of different migration directions and the strain-induced change of the crystal structure (symmetry), the Fe diffusion always follows an Arrhenius

![](./images/814593680420634624_6.jpg)

FIG. 6. (Color online) Energy barriers for forward and backward jumps between the TET and HEX sites obtained using CI-NEB calculations. The dashed line corresponds to the energy barrier for migration of Fe interstitials in unstrained bulk Si. The solid blue and green lines indicate to the effective energy barriers obtained from the kMC simulations.

![](./images/814593680420634624_7.jpg)

FIG. 7. (Color online) Temperature dependencies of relative diffusion coefficients (with respect to Fe diffusion in unstrained bulk Si) for all investigated strain states obtained from kMC simulations. The shaded areas emphasize data with quantitatively similar behaviors.

behavior. The effective energy barriers are included in Fig. 6 as green and blue solid lines. They only deviate slightly from the lowest energy barriers found for the TET $\rightarrow$ HEX migration. The reverse migration direction has no significant influence on the effective energy barriers. Beware that due to our simplification of setting the frequency factors to those of the unstrained crystal, the intercepts may be inaccurate and, hence, they are not considered here. The results for $D/D_{\text{bulk}}$ can be sorted into four quantitatively similar groups. The two extreme cases, i.e., strongly reduced and strongly enhanced diffusion, occur for $+5\%$ and $-5\%$ hydrostatic strain, respectively. The third group, consisting of compressive uniaxial strains, leads to a slightly lower diffusivity. The majority of the strain states, including all types of shear strain, form a fourth group that causes a moderately higher diffusivity.

## V. FE IN THE STRAIN FIELD OF PERFECT AND PARTIAL DISLOCATIONS

Dislocations are line defects accompanied by long-ranged stress and strain fields that, according to the linear elasticity theory, diverge at the dislocation centers [45]. In the region around the dislocation center, usually referred to as the dislocation core, linear elasticity ceases to be valid and nonlinear elasticity [46] or the discrete atomic structure need to be taken into account. In this work, we focus on the interactions between the interstitial Fe impurities and the long-ranged strain fields of dislocations in Si.

The most frequent types of dislocations in Si are the $\frac{1}{2}\langle 110\rangle$ screw and $60^{\circ}$ mixed dislocations [47]. The cores of both dislocations are known to be dissociated into two Shockley partial dislocations with Burgers vectors $a/6\langle 211\rangle$, according to Refs. [45,47]:
$$
\frac{a}{2}[1\overline{1}0] \rightarrow \frac{a}{6}[2\overline{1}\overline{1}]+\frac{a}{6}[1\overline{2}1]. \tag{10}
$$

These partials are connected by a stacking fault. The perfect screw dislocation dissociates into two $30^{\circ}$ partial dislocations while the $60^{\circ}$ mixed dislocation dissociates into one $30^{\circ}$ and one $90^{\circ}$ partial dislocation [47]. The dissociation of the dislocation core is of particular interest in Si because the dissociation length can reach up to 5 nm due to the very low stacking fault energy of about $0.05\ \text{J/m}^2$ [48–51]. For simplicity, we treat in the following the partial dislocations as individual objects since the strain field of the stacking fault is negligibly small relative to the strain fields of the cores. The crystallographic orientations for the dislocations are sketched in Fig. 8. The strain field of the screw dislocation has an axial symmetry and can be decomposed into shear strains $\tau_{xz},\tau_{yz}$ along the dislocation line only [45]. The strain fields of the $60^{\circ}$ mixed and the $30^{\circ}$ partial dislocations have more complex symmetries as they consist of strain components with both screw and edge characters. The latter includes dilatational strains $\varepsilon_x$ and $\varepsilon_y$ and shear strain $\tau_{xy}$ perpendicular to the dislocation line [45]. The $90^{\circ}$ partial dislocation is a pure edge dislocation with a corresponding strain field. Note that decompositions of dislocation strain fields into individual strain components are not unique but depend on the choice of the geometrical reference frame (for the orientations used here see Fig. 8).

![](./images/814593680420634624_8.jpg)

FIG. 8. (Color online) Orientation for the screw and $60^{\circ}$ mixed dislocations and the $90^{\circ}$ and $30^{\circ}$ partial dislocations. The stacking fault associated with the partial dislocation is not shown here.

![](./images/814593680420634624_9.jpg)

FIG. 9. (Color online) Parameterizations of the change of the migration barrier $e_s(\varepsilon)$ for strain component $s$ and strain value $\epsilon$ by a polynomial function. Only strain components necessary for the dislocation strain fields are shown. The different colors represent the different $\langle 111\rangle$ migration directions (of Fig. 8).

In order to analyze the diffusion of Fe in the strain fields of the four dislocations, we first parametrized the changes of the migration barriers as functions of the relevant strain components. This was done by interpolating the barrier changes calculated for strains ranging between $-5\%$ and $+5\%$ (cf. Fig. 6) with a polynomial function. Results of these interpolations, showing the barrier change $e_s(\varepsilon)=\Delta E(\varepsilon)/\Delta E_{\text{bulk}}$ for the two dilatational and four shear strains needed for the dislocation strain fields, are presented in Fig. 9. The different colors in each graph correspond to migration pathways in the different $\langle 111\rangle$ directions.

In linear elasticity, the total strain field at an arbitrary location in the field of the dislocation (outside of the dislocation core) is given by superposition of all strain components. The corresponding migration barrier at this location can be then written as
$$
\Delta E(\varepsilon)=\Delta E_{\text{bulk}} \cdot \prod_{i=1}^{N_{\text{strain}}} e(\varepsilon_i), \tag{11}
$$
where $N_{\text{strain}}$ is the number of strain components.

Figure 10 shows the variations of migration barriers for Fe jumps along different $\langle 111\rangle$ directions in the strain fields of all four considered dislocations. As expected, the most pronounced barrier changes are close to the dislocation cores, where the amplitude of the strain field is largest. In case of the screw dislocation, the influence of the elastic field is rather short-ranged and the migration barrier differs less than $0.01\ \text{eV}$ from the bulk value at a distance of $40\ \text{\AA}$ away from the dislocation core. For the $60^{\circ}$ mixed dislocation, the

![](./images/814593680420634624_10.jpg)

FIG. 10. (Color online) Migration barrier for interstitial Fe impurities in the strain field of a $60^\circ$ mixed dislocation, screw dislocation, $90^\circ$ partial dislocation, and $30^\circ$ partial dislocation for different migration directions. The yellow circles indicate the core region of the dislocation (radius chosen to be $5$ Å) where our model is not applicable due to core effects. The panels on the right show cross sections along the dashed green lines marked in the contour plots. The dotted horizontal black line indicate the migration barrier for Fe in bulk Si.

influence of the strain field on the migration barrier is much more pronounced and its difference from the bulk value falls below 0.01 eV at a distance of about $150$ Å away from the dislocation core (not shown here). The shear strain field of the screw dislocation leads only to a decrease of the migration barrier, whereas for the $60^\circ$ mixed dislocation the migration barrier is increased in the compressive region (positive $y$ values) and decreased in the tensile region (negative $y$ values). The strain fields of both partial dislocations influence the migration barrier similarly as that of the $60^\circ$ mixed dislocation, predominantly due to the edge components of their strain fields. The influence is more pronounced for the $90^\circ$ partial dislocation than for the $30^\circ$ partial dislocation due to the larger edge character.

For all dislocations, the migration barrier depends also on the migration direction, which leads to direction-dependent shapes of the contour plots. Cross sections along the green dashed lines are shown in the right-most panels. For the $60^\circ$ mixed dislocation and the two partial dislocations, different $\langle 111 \rangle$ migration directions have almost the same migration barriers in the tensile region, while in the compressive region the [111] migration direction has a slightly larger migration barrier then the other three directions. However, in both cases the deviations between the different directions are hardly significant.

In order to estimate the influence of the strain field on the diffusion of interstitial Fe, we compare the ratio $\lambda$ between the migration rate $\Gamma_{\text{local,direction}}(\mathbf{r})$, in different migration directions

![](./images/814593680420634624_11.jpg)

FIG. 11. (Color online) Angle-averaged distance-dependent ratios between migration rates of interstitial Fe around dislocations and in the perfect crystal of Si in the two halfspace above (a) and below (b) the glide plane of the dislocation for the two temperatures $T = 100$ K and $T = 300$ K.

at a position $\mathbf{r}$ and the migration rate in bulk $\Gamma_{\text{bulk}}$. This ratio is given by

$$
\begin{aligned}
\lambda(\mathbf{r}) &=\frac{1}{4} \sum_{\text {direction }} \frac{\Gamma_{\text {local,direction }}(\mathbf{r})}{\Gamma_{\text {bulk }}} \\
&=\frac{1}{4} \sum_{\text {direction }} \frac{\mathrm{e}^{-\Delta E_{\text {local,direction }}(\mathbf{r}) / k_{B} T}}{\mathrm{e}^{-\Delta E_{\text {bulk }} / k_{B} T}},
\end{aligned}
\tag{12}
$$

where $\lambda = 1$ corresponds to a bulk-like migration while Fe migration is enhanced or decreased for $\lambda > 1$ or $\lambda < 1$, respectively. From $\lambda$ angle-averaged rates are calculated. Since for all cases but the screw dislocation the migration behaviors are different in the two halfspaces above (a) and below (b) the glide plane of the dislocation [i.e., (a) $y > 0$ and (b) $y < 0$ in Fig. 10], separate $\overline{\lambda_{\mathrm{a}}}(r)$ and $\overline{\lambda_{\mathrm{b}}}(r)$ are calculated for these two regions. The angle-averaged $\overline{\lambda_{\mathrm{a}}}(r)$ and $\overline{\lambda_{\mathrm{b}}}(r)$ around the dislocation center are calculated from the ratio $\lambda(\mathbf{r})$ in Eq. (12) according to

$$
\overline{\lambda_{a}}(r)=\int_{0}^{\pi} \lambda(r, \theta) d \theta
\tag{13}
$$

and

$$
\overline{\lambda_{b}}(r)=\int_{-\pi}^{0} \lambda(r, \theta) d \theta,
\tag{14}
$$

where $r$ and $\theta$ are the polar coordinates of $\mathbf{r}$ in a plane perpendicular to the dislocation line, and the half spaces above and below the glide plane are denoted by the subscripts $a$ and $b$.

In Fig. 11, we show the results of $\overline{\lambda_{\mathrm{a}}}(r)$ and $\overline{\lambda_{\mathrm{b}}}(r)$ for the different dislocations at $T = 100$ and $300$ K. In the lower half space (left panels) the migration of Fe is enhanced in all cases. The $60^{\circ}$ dislocation has the largest influence on the migration. In the upper half space (right panels) only the screw dislocation leads to an increase of the diffusion, which is the same for the upper halfspace. The compressive strain fields of the other tree dislocations lead to a decrease of the diffusion.

The influence of the screw dislocation has the shortest range. This is reflected in the decay of $\overline{\lambda_{\mathrm{a}}}(r)$ and $\overline{\lambda_{\mathrm{b}}}(r)$ as a function of $r$. For the screw dislocation it approaches the bulk value faster than for the $90^{\circ}$ and $30^{\circ}$ dislocation. The influence of the $60^{\circ}$ dislocation has the longest range.

With increasing temperature, the influence of the strain field on the diffusion is less pronounced. While $\overline{\lambda_{\mathrm{a}}}$ is about 2.5 at a radius $r = 15$ Å for the $60^{\circ}$ dislocation at $T = 100$ K, it is only 1.35 for $T = 300$ K.

## VI. DISCUSSION

The results of our DFT calculations show that the behavior of Fe atoms in a bulk Si crystal is not significantly affected by temperature. The temperature neither changes the stability hierarchy of the Fe defect configurations nor does it influence the predominant migration mechanism, i.e., the MEP and its energy barrier for migration of a Fe interstitial between the neighboring tetrahedral sites. This finding is consistent with experimental observations of only one operating mechanism for diffusion of Fe in Si over a wide range of temperatures [52].

It is still a matter of debate why Fe impurities are attracted by regions of large elastic strains [8,11,12,15]. The stability of the most favorable configuration for Fe atoms occupying the interstitial tetrahedral sites in Si remains almost unaltered in the presence of realistic strain fields ranging within $\pm 5\%$ (cf. Fig. 3). Therefore, there is no thermodynamic driving force for the accumulation of Fe impurities in regions of large strain associated with high concentrations of dislocations or other extended crystal defects. This result is consistent with the experimental observation of *Lu et al.* that the gettering of interstitial Fe by the strain field of dislocations is very inefficient [53].

Nonetheless, the formation energies of other interstitial and substitutional Fe defects are affected by strain. Even though these configurations are not thermodynamically stable, they play a role in the diffusion of Fe impurities. We carried out extensive MEP calculations to study the effect of various homogeneous strains on the migration of Fe atoms in Si. The results for the energy barriers were then used for the parametrization of a mesoscopic kMC simulation model to obtain effective diffusion coefficients under various strain states and temperatures. The effects of different strain states could be classified into four groups (cf. Fig. 7). For all considered cases, the diffusion of Fe follows an Arrhenius behavior with effective energy barriers close to that of the lowest energy barrier for the TET $\to$ HEX migration direction. Hydrostatic strains lead to the largest changes of Fe diffusion. For 5% hydrostatic expansion of the lattice the diffusion at room temperature becomes seven orders of magnitude faster than the diffusion in unstrained Si. An analogous reduction of the Fe diffusivity by eight orders of magnitude occurs for hydrostatic compression of the same magnitude (cf. Fig. 7). Similarly, all the uniaxial compressive and tensile strains also lead to a decrease and an increase of the Fe diffusion, respectively, albeit not to such dramatic ones. Rather surprising is our finding that a shearing of the crystal structure results always in an enhancement of the Fe diffusion, which is similar to that found for uniaxial tension. In summary, we observe an increase of Fe diffusion for all types of strain except for compressive strain.

The obtained dependencies for the migration barriers on the applied strain were utilized to analyze the diffusional behavior of Fe interstitial in the strain fields of the perfect screw and $60^\circ$ mixed dislocations as well as of the partial $90^\circ$ and $30^\circ$ dislocations in Si. Due to the shear character of its strain field, the perfect screw dislocation always enhances the Fe diffusion in its vicinity. However, the effect is rather short-ranged, within a radius of less than 4 nm. In contrast, the perfect $60^\circ$ mixed dislocation enhances Fe diffusion on one side and impedes it on the other side, since the migration barriers are increased in the compressive and reduced in the tensile regions of the dislocation (cf. Fig. 10). The barriers are systematically influenced by strain even beyond 15 nm from the dislocation center, i.e., within a significantly larger region than around the screw dislocation.

Both partial dislocations behave qualitatively similarly as the $60^\circ$ mixed dislocation although the barriers are affected within a smaller range (smaller for the $30^\circ$ than for the $90^\circ$ partial dislocation). A superposition of the effects of the two partials can be used to determine whether dissociated dislocations alter the migration barrier differently than the perfect dislocations. Since the dissociated $60^\circ$ mixed dislocation is composed of the $30^\circ$ and the $90^\circ$ partials separated by less than 5 nm, its overall effect on the migration barrier is qualitatively same as that of the perfect dislocation. In contrast, the dissociated screw dislocation will influence the migration barrier of Fe markedly differently than the perfect dislocation, since two $30^\circ$ partials have both screw and edge characters. The dissociation in this case therefore gives rise to regions of inhibited and enhanced Fe diffusivity around the screw dislocation.

For all dislocations the most pronounced changes of the migration barriers occur close to the dislocation cores where the stresses and strains are largest. As mentioned above, we did not consider the core effects in this study, since the atomic structure of the core is very different from that of perfect Si crystal and linear elasticity does not apply there [46].

Without taking the core effects into account, the understanding of the role of dislocations on the distribution and diffusion of Fe in Si remains incomplete. Nevertheless, we attempt to relate our current findings to some experimental observations. There exists experimental evidence [9,54,55] that dislocations cause a strong recombination activity after metallic impurities have been incorporated into the Si material. Moreover, a direct correlation between the interstitial Fe concentration and the dislocation density was reported by *Lauer et al.* [17]. This is further supported by transmission electron microscopy of a Fe-decorated interfacial screw dislocation in a SiGe/Si heterostructure by *Lu et al.* [53]. These observations are consistent with our findings as enhanced diffusion around dislocations is observed by which Fe atoms can be transported easily to regions of higher dislocation densities. However, the preferential segregation of Fe has to occur within the core region. In addition, the dislocation core may also act as a strong diffusion channel along the dislocation line for Fe in Si (pipe diffusion), as observed for instance for Si in Al [56].

The diffusion of Fe in n-doped Si under external uniaxial stress along [110] has been studied by *Suzuki et al.* [8,57] using Mössbauer spectroscopy. The activation energy barrier for interstitial Fe diffusion was found to decrease from 0.68 to 0.33 eV for a stress of about 19 MPa at room temperature. Since the lattice strain corresponding to this stress is much lower than 1%, the expected change for the migration barrier is very small. According to our calculations, the reduction of the migration barrier to 0.35 eV requires an application of external hydrostatic stress of about 4.4 GPa (cf. Table I), which is much higher that the reported stress value. A possible explanation of the experimental observations of *Suzuki et al.* may be related to large local stress associated with dislocation entanglements and their changes under external loading; unfortunately, no information about the dislocation distribution and arrangement was given.

### VII. SUMMARY

Defect formation energies (including the vibrational entropy contribution) for different interstitial and substitutional defect configurations of atomic Fe impurities in crystalline Si were computed using DFT-based first-principles calculations. The relative energies of the investigated defect configurations are almost independent of temperature in a range between 0

and 600 K. Therefore, temperature is not expected to affect significantly the behavior of Fe impurities in Si.

The effects of various elastic strain modes, namely hydrostatic, uniaxial, and shear strains, on the formation energies of Fe impurities were investigated in detail. Surprisingly, the stability of the most favorable configuration, an interstitial Fe atom at a tetrahedral site, is not significantly affected by any of the strain modes. However, the strain affects the formation energies of other defect configurations as well as the diffusion behavior of Fe in Si.

Combined DFT calculations of minimum energy paths combined with kMC simulations were used to obtain the effective diffusion coefficients as function of strain and temperature. It was found that tensile and shear strains can significantly enhance the Fe diffusion at room temperature, whereas compressive strains result in diffusion impediment. These results were used to analyze the influences of the strain fields of perfect screw and $60^\circ$ mixed dislocations on the migration of the Fe interstitial. For both dislocations the most pronounced changes of the migration barriers occur close to the dislocation cores where the stresses and strains are largest. The strain field of the perfect screw dislocation enhances the Fe diffusion within 4 nm from the geometric center of the dislocation. The perfect $60^\circ$ mixed dislocation can both enhance and impede the Fe diffusion since the migration barriers are increased in the compressive and reduced in the tensile regions of the dislocation. When the dislocations are split into partial $90^\circ$ and $30^\circ$ dislocations, qualitatively similar behavior to the $60^\circ$ mixed dislocation is found. Consequently, the edge character of the two $30^\circ$ partial dislocations changes the qualitative behavior of the screw dislocation to be longer ranged and more efficient.

## ACKNOWLEDGMENTS
This work was performed on the computational resource ForHLR Phase I funded by the Ministry of Science, Research and the Arts, Baden-Württemberg, and DFG ("Deutsche Forschungsgemeinschaft"). All calculations were managed using the *atomic simulation environment ASE* [58]; atomistic structure models are visualized using VESTA [59]. This work was funded by the Hans L. Merkle foundation of the Robert Bosch GmbH.

## APPENDIX
In the following, we list the transformation matrices $D$, which are used to introduce an elastic strain to the cubic 64-atom supercell of the diamond structure of Si. For hydrostatic strain $\varepsilon_{Hyd}(\varepsilon)$, the deformation matrix is
$$
\begin{pmatrix}
\varepsilon & 0 & 0 \\
0 & \varepsilon & 0 \\
0 & 0 & \varepsilon
\end{pmatrix}. \tag{A1}
$$

For uniaxial strains $\varepsilon_{[100]}$, $\varepsilon_{[110]}$, $\varepsilon_{[111]}$, $\varepsilon_{[112]}$, the deformation matrices are
$$
\begin{pmatrix}
\varepsilon & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}, \quad
\begin{pmatrix}
\frac{\varepsilon}{2} & -\frac{\varepsilon}{2} & 0 \\
-\frac{\varepsilon}{2} & \frac{\varepsilon}{2} & 0 \\
0 & 0 & 0
\end{pmatrix},
$$
$$
\begin{pmatrix}
\frac{\varepsilon}{3} & \frac{\varepsilon}{3} & \frac{\varepsilon}{3} \\
\frac{\varepsilon}{3} & \frac{\varepsilon}{3} & \frac{\varepsilon}{3} \\
\frac{\varepsilon}{3} & \frac{\varepsilon}{3} & \frac{\varepsilon}{3}
\end{pmatrix}, \quad
\begin{pmatrix}
\frac{\varepsilon}{6} & \frac{\varepsilon}{6} & -\frac{\varepsilon}{3} \\
\frac{\varepsilon}{6} & \frac{\varepsilon}{6} & -\frac{\varepsilon}{3} \\
-\frac{\varepsilon}{3} & -\frac{\varepsilon}{3} & \frac{\varepsilon}{6}
\end{pmatrix},
$$
respectively. For the shear strains, $\tau_{[010],[001]}$, $\tau_{[112],[111]}$, $\tau_{[\overline{1}10],[112]}$, $\tau_{[111],[\overline{1}10]}$, the deformation matrices are
$$
\begin{pmatrix}
0 & \varepsilon & 0 \\
\varepsilon & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}, \quad
\begin{pmatrix}
\sqrt{2}\frac{\varepsilon}{3} & \sqrt{2}\frac{\varepsilon}{3} & -\sqrt{2}\frac{\varepsilon}{6} \\
\sqrt{2}\frac{\varepsilon}{3} & \sqrt{2}\frac{\varepsilon}{3} & -\sqrt{2}\frac{\varepsilon}{6} \\
-\sqrt{2}\frac{\varepsilon}{6} & -\sqrt{2}\frac{\varepsilon}{6} & -2\sqrt{2}\frac{\varepsilon}{3}
\end{pmatrix},
$$
$$
\begin{pmatrix}
-\sqrt{3}\frac{\varepsilon}{3} & 0 & \sqrt{3}\frac{\varepsilon}{3} \\
0 & \sqrt{3}\frac{\varepsilon}{3} & -\sqrt{3}\frac{\varepsilon}{3} \\
\sqrt{3}\frac{\varepsilon}{3} & -\sqrt{3}\frac{\varepsilon}{3} & 0
\end{pmatrix}, \quad
\begin{pmatrix}
-\sqrt{6}\frac{\varepsilon}{3} & 0 & -\sqrt{6}\frac{\varepsilon}{6} \\
0 & \sqrt{6}\frac{\varepsilon}{3} & \sqrt{6}\frac{\varepsilon}{6} \\
-\sqrt{6}\frac{\varepsilon}{6} & \sqrt{6}\frac{\varepsilon}{6} & 0
\end{pmatrix},
$$
respectively.

[1] A. Istratov, H. Hieslmair, and E. Weber, *Appl. Phys. A* **69**, 13 (1999).
[2] A. Istratov, H. Hieslmair, and E. Weber, *Appl. Phys. A* **70**, 489 (2000).
[3] G. Coletti, P. C. Bronsveld, G. Hahn, W. Warta, D. Macdonald, B. Ceccaroli, K. Wambach, N. Le Quang, and J. M. Fernandez, *Adv. Funct. Mater.* **21**, 879 (2011).
[4] T. Buonassisi, A. A. Istratov, M. D. Pickett, M. Heuer, J. P. Kalejs, G. Hahn, M. A. Marcus, B. Lai, Z. Cai, S. M. Heald, T. F. Ciszek, R. F. Clark, D. W. Cunningham, A. M. Gabor, R. Jonczyk, S. Narayanan, E. Sauar, and E. R. Weber, *Prog. Photovolt. Res. Appl.* **14**, 513 (2006).
[5] T. Buonassisi, A. A. Istratov, M. A. Marcus, B. Lai, Z. Cai, S. M. Heald, and E. R. Weber, *Nat. Mater.* **4**, 676 (2005).
[6] M. D. Pickett and T. Buonassisi, *Appl. Phys. Lett.* **92**, 122103 (2008).
[7] A. Hähnel, J. Bauer, H. Blumtritt, O. Breitenstein, D. Lausch, and W. Kwapil, *J. Appl. Phys.* **113**, 044505 (2013).
[8] K. Suzuki, Y. Yoshida, T. Kamimura, M. Ichino, and K. Asahi, *Physica B* **404**, 4678 (2009).
[9] M. Seibt, R. Khalil, V. Kveder, and W. Schröter, *Appl. Phys. A* **96**, 235 (2009).
[10] J. Hofstetter, D. P. Fenning, D. M. Powell, A. E. Morishige, and T. Buonassisi, *Solid State Phenom.* **205-206**, 15 (2013).
[11] G. Sarau, S. Christiansen, M. Holla, and W. Seifert, *Sol. Energy Mater. Sol. Cells* **95**, 2264 (2011).
[12] A. Augusto, D. Pera, H. J. Choi, P. Bellanger, M. C. Brito, J. M. Alves, A. M. Vallra, T. Buonassisi, and J. M. Serra, *J. Appl. Phys.* **113**, 083510 (2013).
[13] M. Nacke, M. Allardt, P. Chekhonin, E. Hieckmann, W. Skrotzki, and J. Weber, *J. Appl. Phys.* **115**, 163511 (2014).
[14] B. Ziebarth, M. Mrovec, C. Elsässer, and P. Gumbsch, *Phys. Rev. B* **91**, 035309 (2015).


[15] V. Gianapati, S. Schoenfelder, S. Castellanos, S. Oener, R. Koepge, A. Sampson, M. A. Marcus, B. Lai, H. Morhenn, G. Hahn, J. Bagdahn, and T. Buonassisi, J. Appl. Phys. 108, 063528 (2010).

[16] M. Seibt, D. Abdelbarey, V. Kveder, C. Rudolf, P. Saring, L. Stolze, and O. Voß, Mater. Sci. Eng. B 159-160, 264 (2009).

[17] K. Lauer, M. Herms, A. Grochocki, and J. Bollmann, Solid State Phenom. 178-179, 211 (2011).

[18] M. Kivambe, G. Stokkan, T. Ervik, S. Castellanos, J. Hofstetter, and T. Buonassisi, Solid State Phenom. 205-206, 71 (2013).

[19] K. Hartman, M. Bertoni, J. Serdy, and T. Buonassisi, Appl. Phys. Lett. 93, 122108 (2008).

[20] H. Choi, M. Bertoni, J. Hofstetter, D. Fenning, D. Powell, S. Castellanos, and T. Buonassisi, IEEE J. Photovoltaics 3, 189 (2013).

[21] S. Castellanos, M. Kivambe, J. Hofstetter, M. Rinio, B. Lai, and T. Buonassisi, J. Appl. Phys. 115, 183511 (2014).

[22] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, J. Phys.: Condens. Matter 21, 395502 (2009).

[23] D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).

[24] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[25] H. Monkhorst and J. Pack, Phys. Rev. B 13, 5188 (1976).

[26] G. Henkelman, B. Uberuaga, and H. Jónsson, J. Chem. Phys. 113, 9901 (2000).

[27] W. O'Mara, R. B. Herring, and L. P. Hunt, Handbook of Semiconductor Silicon Technology (Noyes Publications, Park Ridge, NJ, 1990).

[28] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. A. Persson, APL Mater. 1, 011002 (2013).

[29] M. A. Hopcroft, W. D. Nix, and T. W. Kenny, J. Microelec- tromech. Syst. 19, 229 (2010).

[30] G. H. Vineyard, J. Phys. Chem. Solids. 3, 121 (1957).

[31] A. Bortz, M. Kalos, and J. Lebowitz, J. Comput. Phys. 17, 10 (1975).

[32] D. T. Gillespie, J. Comput. Phys. 22, 403 (1976).

[33] A. F. Voter, in Radiation Effects in Solids (Springer, Berlin, 2007), pp. 1-23.

[34] Y. A. Du, J. Rogal, and R. Drautz, Phys. Rev. B 86, 174110 (2012).

[35] J. P. Dekker, C. A. Volkert, E. Arzt, and P. Gumbsch, Phys. Rev. Lett. 87, 035901 (2001).

[36] K. A. Fichthorn and W. H. Weinberg, J. Chem. Phys. 95, 1090 (1991).

[37] M. Sanati, N. G. Szwacki, and S. K. Estreicher, Phys. Rev. B 76, 125204 (2007).

[38] S. K. Estreicher, M. Sanati, and N. Gonzalez Szwacki, Phys. Rev. B 77, 125214 (2008).

[39] G. A. Baraff and M. Schlüter, Phys. Rev. B 30, 3460 (1984).

[40] W. Frank, C. Elsässer, and M. Fähnle, Phys. Rev. Lett. 74, 1791 (1995).

[41] A. Togo, F. Oba, and I. Tanaka, Phys. Rev. B 78, 134106 (2008).

[42] G. Kresse, J. Furthmüller, and J. Hafner, Europhys. Lett. 32, 729 (1995).

[43] W. Frank, U. Breier, C. Elsässer, and M. Fähnle, Phys. Rev. Lett. 77, 518 (1996).

[44] J. H. Westbrook and R. L. Fleischer, eds., Intermetallic Compounds: Principles and Practice, Vol. 1: Principles, 1st ed. (John Wiley and Sons Ltd, Chichester, New York, 1995).

[45] J. P. Hirth and J. Lothe, Theory of Dislocations (Krieger Publishing Company, Malabar, FL, 1991).

[46] D. Seif, G. Po, M. Mrovec, M. Lazar, C. Elsässer, and P. Gumbsch, Phys. Rev. B 91, 184102 (2015).

[47] J. Rabier, L. Pizzagalli, and J. Demenet, Dislocat. Solids 16, 47 (2010).

[48] I. L. F. Ray and D. J. H. Cockayne, Philos. Mag. 22, 853 (1970).

[49] E. Aerts, P. Delavignette, R. Siems, and S. Amelinckx, J. Appl. Phys. 33, 3078 (1962).

[50] H. Föll and C. Carter, Philos. Mag. A 40, 497 (1979).

[51] B. Ziebarth, M. Mrovec, C. Elsässer, and P. Gumbsch, J. Appl. Phys. 116, 093510 (2014).

[52] P. Schwalbach, S. Laubach, M. Hartick, E. Kankeleit, B. Keck, M. Menningen, and R. Sielemann, Phys. Rev. Lett. 64, 1274 (1990).

[53] J. Lu, X. Yu, Y. Park, and G. Rozgonyi, J. Appl. Phys. 105, 073712 (2009).

[54] V. Kveder, M. Kittler, and W. Schröter, Phys. Rev. B 63, 115208 (2001).

[55] M. Seibt, V. Kveder, W. Schröter, and O. Voß, Phys. Status Solidi A 202, 911 (2005).

[56] M. Legros, G. Dehm, E. Arzt, and T. J. Balk, Science 319, 1646 (2008).

[57] K. Suzuki, Y. Yoshida, K. Hayakawa, K. Yukihira, M. Ichino, and K. Asahi, Hyperfine Interact. 197, 213 (2010).

[58] S. R. Bahn and K. W. Jacobsen, Comput. Sci. Eng. 4, 56 (2002).

[59] K. Momma and F. Izumi, J. Appl. Crystallogr. 44, 1272 (2011).