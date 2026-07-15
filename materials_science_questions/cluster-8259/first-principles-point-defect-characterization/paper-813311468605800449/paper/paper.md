# Frenkel pair recombinations in $UO_2$: Importance of explicit description of polarizability in core-shell molecular dynamics simulations

Fabien Devynck, Marcella Iannuzzi, $^{*}$ and Matthias Krack $^{\dagger}$

Laboratory for Reactor Physics and Systems Behaviour, Paul Scherrer Institute, CH-5232 Villigen PSI, Switzerland

(Received 23 March 2012; published 15 May 2012)

The oxygen and uranium Frenkel pair (FP) recombination mechanisms are studied in $UO_2$ using an empirical interatomic potential accounting for the polarizability of the ions, namely a dynamical core-shell model. The results are compared to a more conventional rigid-ion model. Both model types have been implemented into the CP2K program package and thoroughly validated. The overall picture indicates that the FP recombination mechanism is a complex process involving several phenomena. The FP recombination can happen instantaneously when the distance between the interstitial and the vacancy is small or can be thermally activated at larger separation distances. However, other criteria can prevail over the interstitial-vacancy distance. The surrounding environment of the FP defect, the mechanical stiffness of the matrix, and the orientation of the migration path are shown to be major factors acting on the FP lifetime. The core-shell and rigid-ion models provide a similar qualitative description of the FP recombination mechanism. However, the FP stabilities determined by both models significantly differ in the lower temperature range considered. Indeed, the recombination time of the oxygen and uranium FPs can be up to an order of magnitude lower in the core-shell model at $T = 600$ K and $T = 1800$ K, respectively. These differences highlight the importance of the explicit description of polarizability on some crucial properties such as the resistance to amorphization. This refined description of the interatomic interactions would certainly affect the description of the recrystallization process following a displacement cascade. In turn, the self-healing phase would be better accounted for in the core-shell model and the misestimate inherent to the lack of polarizability in the rigid-ion model corrected.

DOI: 10.1103/PhysRevB.85.184103
PACS number(s): 61.43.Bn, 61.72.jn, 83.10.Rs, 66.30.Lw

## I. INTRODUCTION

Uranium dioxide $(UO_2)$ is the standard nuclear fuel used in the present nuclear industry. Among other desirable quantities, such as chemical stability, high melting point, and ease of fabrication, $UO_2$ features over other potential nuclear fuels the advantage of being highly tolerant to irradiation. $^{1}$ Despite numerous experimental and theoretical studies, a fundamental understanding of the structural processes occurring at the atomic scale in $UO_2$ under irradiation or self-irradiation has not been achieved. Yet this knowledge is crucial for the design and the safety of nuclear plants and storage repositories.

Some studies have shed some light on the possible origins of this high tolerance to radiation. $^{2}$ It was suggested that the resistance to amorphization could be correlated to the high ionicity of the material, $^{3}$ to the topological freedom of the crystalline material, $^{4-6}$ and to the cation/anion radii ratio which determines the ease with which the cation disorder can be accommodated in the crystal. $^{7-9}$ The important effect of the degree of intrinsic structural order on the energetics (e.g., defect formation and migration energies) $^{10}$ as well as of the Frenkel pair recombinations $^{11}$ were also proposed.

In order to get insight into the nature of the primary damage state caused by an $\alpha$ decay and the evolution of the behavior of defects generated during irradiation or self-irradiation in $UO_2$, molecular dynamics (MD) simulations of single displacement cascades and cascade overlaps have been run with energies up to $80$ keV. $^{12-14}$ The simulations revealed no amorphization of the fluorite matrix, even for a primary knock-on atom (PKA) energy of $80$ keV. $^{12,14}$ Moreover, it was shown that these high-energy displacement cascades result in the creation of subcascade branches whose size is in the same order of magnitude as cascades initiated with an initial PKA energy of $20$ keV. $^{12,14}$ The primary damage state was shown to result in interstitials localized at the periphery of the cascade (or subcascade branches) and vacancies in the core of the cascade irrespective of the initial PKA energy, $^{12-14}$ these defects forming stable FPs at the time scale of the simulation. The fast recombination of close FPs is believed to play a major role in the self-healing behavior of $UO_2$ and in the radiation resistance of other materials. For example, it was recently shown through MD simulations that the cationic FP recombinations plays a key role in the radiation resistance of pyrochlores. $^{11,15,16}$ The recombination of FP was also investigated by means of MD calculations in different fluorite structures. $^{17,18}$ Frenkel pairs with separation distance between the vacancy and the interstitial up to $1.5a_0$ ($UO_2$ lattice parameter) have been studied. It was shown that the recombination processes are driven by the sublattice and the rank of the Frenkel pairs, characterized by distances between the vacancy and the interstitial and by the local symmetry of the interstitial. $^{17,18}$ In this study, the interatomic interactions were described using a conventional rigid-ion potential. $^{19}$ This interatomic potential was primarily developed to simulate displacement cascades in a $UO_2$ matrix. Thus, it is supposed to describe correctly the experimental energies of formation and migration of point defects and the structural effects created by decelerating recoil nuclei in a $UO_2$ matrix. $^{19}$ However, this type of rigid-ion potential lacks the adequate flexibility to properly describe the response of the material to important perturbations of the local environment around the ions. The rigid-ion model may then misestimate the FP recombination time and, in turn, the self-healing process time following a displacement cascade. For this reason, one would like to employ a model which offers a simple way to account for the polarizability of the ions. The core-shell model introduced by Dick and Overhauser $^{20}$ is such

a model. It is expected to describe defective systems more accurately than a rigid-ion model.

In this work we study the energetics and the dynamics of point defects in $\mathrm{UO}_{2}$ by means of structural optimizations, migration path searches via the nudged elastic band (NEB) method, $^{21}$ and MD simulations performed at different temperatures, ranging from 300 K to 2500 K. Two empirical force fields of different type, namely a rigid-ion and a core-shell potential, are employed for the presented simulations. For the MD simulations with the core-shell model, we adopt an adiabatic scheme which has been implemented through an extended Lagrangian formalism $^{22}$ into the CP2K program package. $^{23}$ Both force fields have already been tested in previous works. $^{14,17,19,24-27}$ The simulation results are compared to assess the impact of the ion polarizability on the FP defect recombination in bulk $\mathrm{UO}_{2}$.

The paper is organized as follows. In Sec. II, the computational methods are described. The FP defect properties, resulting from both optimization calculations without the inclusion of temperature effects and MD calculations at finite temperature, are presented in Sec. III. The differences between the core-shell and the rigid-ion models are highlighted in Sec. IV. Conclusions are drawn in Sec. V.

## II. COMPUTATIONAL METHODS

Two main categories of interatomic potentials are commonly used for the modeling of $\mathrm{UO}_{2}$. In the first category, conventionally referred to as rigid-ion models, the ions are represented as massive point charges. In the second type of models, the polarization effects are taken into account by means of a core-shell formalism, first introduced by Dick and Overhauser. In this core-shell model, the ions are described as a charged shell bound to a massive core by a spring usually harmonic. The shell is either massless as in the original scheme $^{20}$ or has a small fraction of the corresponding ion mass. $^{22}$ The first variant is called massless, static, or relaxed core-shell model, whereas the latter one is usually called dynamical or adiabatic core-shell model.

### A. Interatomic potentials

The rigid-ion potential of Morelon $e t$ $a l.^{19}$ and the core-shell potential of Meis and Chartier $^{24}$ are selected for this study. The Morelon potential is supposed to work well, especially for defective $\mathrm{UO}_{2}$ systems. On the other hand, its performance for mechanical properties is only moderate. $^{25,26}$ By contrast, the Meis potential shows an excellent performance for structural and mechanical properties as it was fitted based on the corresponding experimental data. A comparison of the static defect formation and migration energies for the Morelon and the Meis potential is given in Sec. III.

Both potentials describe the short-range nonbonded interactions using a Buckingham potential form. In the case of the core-shell potential, nonbonded interactions are only considered between shells. The nonbonded U-U interactions are neglected. Only the repulsive exponential term $A_{i j} \exp (-B_{i j} r_{i j})$ of the Buckingham potential is considered for the nonbonded U-O interactions. The attractive $C_{i j} r_{i j}^{-6}$ term is discarded to avoid unphysically attractive forces at short interatomic distances. For the same reason, a more refined "Buckingham four range" potential form $^{28}$ is used for the nonbonded O-O interactions,

$$
V\left(r_{i j}\right)= \begin{cases}A_{i j} \exp \left(-B_{i j} r_{i j}\right) & \text { if } r_{i j} \leqslant r_{1}, \\
\text { 5th-degree polynomial } & \text { if } r_{1}<r_{i j} \leqslant r_{\text {min }}, \\
\text { 3rd-degree polynomial } & \text { if } r_{\text {min }}<r_{i j} \leqslant r_{2}, \\
-C_{i j} r_{i j}^{-6} & \text { if } r_{i j}>r_{2},\end{cases}
$$

where $A_{i j}$, $B_{i j}$, and $C_{i j}$ are adjustable parameters and $r_{i j}$ is the distance between the atoms $i$ and $j$. The details of the potential parameters $^{19,24}$ and their validation are reported elsewhere. $^{25,26,29}$ The six coefficients of the 5th- and the 4 coefficients of the 3rd-degree polynomial are automatically fitted within the CP2K code given the values for $r_{1}, r_{2}$, and $r_{\text {min }}$. An accuracy of at least $10^{-7}$ a.u. is imposed for the spline fit of the nonbonded interactions. Beyond a cut-off radius of $10.4 \AA$ (or $L / 2$ for simulation cells with an edge length $L<20.8 \AA$ ) any nonbonded interactions are ignored. The Coulomb interactions are accounted for through Ewald summation. $^{30}$ For this purpose, the smooth particle mesh Ewald (SPME) method $^{31}$ is employed using a meshing of about two grid points per angström. In the case of the core-shell potential, the Coulomb interaction between an ion core and its own shell is explicitly excluded.

### B. Relaxed versus adiabatic core-shell model

The relaxed core-shell model assumes that the massless shells follow instantaneously the motion of their corresponding ion cores which requires optimization of all shells iteratively to their zero-force positions after each movement of the ion cores, i.e., in each molecular dynamics time step. It turns out that these iterative optimization steps introduce a significant computational overhead. $^{32}$ A further drawback of the relaxed core-shell model is that even a tight optimization of the shell positions cannot avoid a noticeable energy drift, especially in long simulations of large systems, due to the limited numerical accuracy of the energy minimization.

In the adiabatic (dynamical) core-shell model the shells are treated using a method analogous to the Car-Parrinello method, $^{33}$ in which the shell degrees of freedom are introduced as fictitious dynamical variables, the shells being the equivalent of the electrons in the original scheme. During the simulation, a system of coupled equations of motion for both cores and shells is then solved. By contrast with the relaxed (static) shell model, an explicit minimization of the energy with respect to shell positions in each molecular dynamics time step is not needed. The fictitious dynamics of the shells keeps them close to their zero-force positions for each new ionic configuration visited along the dynamics, thus yielding accurate ionic forces.

To maintain the adiabaticity condition, it is necessary that the fictitious mass of the shell is chosen small enough with respect to the ion core mass, i.e., the frequency spectra of the ionic and of the shell motion should be well separated. A significant energy transfer from the core to the shell degrees of freedom is then prevented and the adiabaticity condition is preserved. Therefore, from an initial configuration in which the core-shell units have a negligible internal vibrational

energy, the units remain close to this condition throughout the simulation. There is, in practice, a slow leakage of kinetic energy into the core-shell units, but it is verified that this leakage remains negligible along the simulation. Moreover, the temperature of the shells can be controlled explicitly by a thermostat or other techniques can be applied to control the dissipative behavior if needed, e.g., by introducing a random noise term in the framework of a Langevin-type dynamics. $^{34}$

The relatively small mass of the shell particles, in turn, requires that the equations of motion are integrated using a smaller time step than the one commonly used in rigid-ion or massless shell molecular dynamics simulations. On the other hand, the iterative optimization needed in each MD time step using a relaxed (massless) core-shell model is not required. In practice one usually has to find a compromise between adiabaticity and computational efficiency, i.e., an improved adiabaticity requires smaller time steps concurrently degrading the computational efficiency. The adiabatic core-shell model has been implemented into the CP2K program package $^{23}$ and is employed for the core-shell model calculations performed in this work.

The following parameters for the core-shell model complement the parameters already given in Ref. 24. The spring constants for the oxygen and uranium core-shell units and the atomic masses for the oxygen and uranium atoms are given by

$$
k_{\mathrm{O}}=70.824 \mathrm{eV} / \mathring{\mathrm{A}}^{2}, \quad k_{\mathrm{U}}=171.556 \mathrm{eV} / \mathring{\mathrm{A}}^{2}, \tag{2}
$$

$$
m_{\mathrm{O}}=15.9994 \mathrm{u}, \quad m_{\mathrm{U}}=238.02891 \mathrm{u}. \tag{3}
$$

The shell masses for O and U are defined by the mass fractions $x_{\mathrm{O}}$ and $x_{\mathrm{U}}$ of the corresponding ion masses $m_{\mathrm{O}}$ and $m_{\mathrm{U}}$, respectively,

$$
m_{\mathrm{O}}^{\text{core}} = (1 - x_{\mathrm{O}})m_{\mathrm{O}}, \quad m_{\mathrm{O}}^{\text{shell}} = x_{\mathrm{O}}m_{\mathrm{O}}, \tag{4}
$$

$$
m_{\mathrm{U}}^{\text{core}} = (1 - x_{\mathrm{U}})m_{\mathrm{U}}, \quad m_{\mathrm{U}}^{\text{shell}} = x_{\mathrm{U}}m_{\mathrm{U}}. \tag{5}
$$

The mass fraction have been selected to be

$$
x_{\mathrm{O}}=0.1, \quad x_{\mathrm{U}}=0.01, \tag{6}
$$

which allows for the calculation of the corresponding natural core-shell vibration frequencies

$$
\begin{gathered}
\nu_{\mathrm{O}}^{\text{core-shell}} = \frac{1}{2\pi}\sqrt{\frac{k_{\mathrm{O}}}{x_{\mathrm{O}}(1 - x_{\mathrm{O}})m_{\mathrm{O}}}} = 109.8 \text{ THz}, \tag{7} \\
\tilde{\nu}_{\mathrm{O}}^{\text{core-shell}} = 3663.76 \text{ cm}^{-1}, \tag{8}
\end{gathered}
$$

$$
\begin{gathered}
\nu_{\mathrm{U}}^{\text{core-shell}} = \frac{1}{2\pi}\sqrt{\frac{k_{\mathrm{U}}}{x_{\mathrm{U}}(1 - x_{\mathrm{U}})m_{\mathrm{U}}}} = 133.6 \text{ THz}, \tag{9} \\
\tilde{\nu}_{\mathrm{U}}^{\text{core-shell}} = 4457.39 \text{ cm}^{-1}, \tag{10}
\end{gathered}
$$

for both atomic kinds. This frequencies have to be well separated from the vibrational spectrum of the studied system. The adiabatic separation between the ionic and the core-shell motions can be verified by determining the vibrational spectrum of bulk $\mathrm{UO}_{2}$, which can be computed from the Fourier transform of the velocity-velocity autocorrelation function, as sampled along MD trajectories obtained at constant temperature. Two examples of such spectra, obtained at 500 K and 1500 K, are displayed in Fig. 1. It can be observed that the highest frequencies are below $800 \text{ cm}^{-1}$ and, thus, are well separated from the core-shell vibration frequencies of our setup given in Eqs. (8) and (10).

![](./images/813311468605800449_1.jpg)

FIG. 1. Fourier transform of the velocity-velocity autocorrelation function of $\mathrm{UO}_{2}$ calculated at 500 K and 1500 K using the adiabatic core-shell potential of Meis and Chartier $^{24}$ and a time step of 0.77 and 0.44 fs, respectively.

### C. MD simulation setup
We study in this work the recombination of oxygen and uranium FPs in the fluorite structure in line with Ref. 17. In the fluorite structure, the cation sublattice forms a face-centered cubic (fcc) lattice, and the anion sublattice forms a simple cubic lattice located at the tetrahedral sites of the cation fcc sublattice. Each conventional fluorite unit cell consists of four uranium and eight oxygen atoms.

A FP is defined as a pair of one interstitial and one vacancy of either the cation or anion sublattice. The interstitial positions for both the cation and anion are located at the octahedral sites of the fcc cation sublattice. The FPs are ranked according to the distance between the interstitial and the vacancy as in Ref. 17. Tables III and IV summarize the characteristics of the different FPs for the fluorite structure up to $1.5\ a_{0}$ for the oxygen and the uranium sublattice, respectively. When two different types of FPs correspond to different symmetries for a given rank, they are labeled as type I and type II.

A periodic simulation box containing $5 \times 5 \times 5$ conventional unit cells of $\mathrm{UO}_{2}$ in the fluorite structure is first equilibrated for 20 ps at the desired temperature and at constant external pressure (0 GPa) within the isobaric-isothermal (NPT) ensemble. A FP is then created by displacing an ion from its original lattice position to one of the interstitial positions located at the octahedral sites of the fcc cation sublattice. The system is then relaxed for 2 ns at constant temperature within the canonical (NVT) ensemble. A variable time-step algorithm is used to ensure that the fastest atom does not move farther than a given distance (0.04 $\mathring{\mathrm{A}}$ in our case) between two consecutive MD steps. Moreover, microcanonical (NVE) simulations are run using the core-shell model to check the validity of the chosen MD simulation setup for this potential type. An energy conservation within less than 0.01 K per

picosecond and atom is observed in the NVE runs at about 1500 K and 2500 K which shows the reliability of the employed MD simulation setup.

For each oxygen and uranium FP, we run 30 simulations using 3 different initial configurations and 10 different initial velocities for each initial configuration at 4 or 5 different temperatures. The temperature never exceeds 2500 K in order to stay in the range of validity of the interatomic potentials.

In this work, we also compare the FP recombination energies calculated with the rigid-ion model in the present study and in a previous investigation.¹⁷ The most obvious difference between our simulation settings and those of the study in Ref. 17 is the size of the system. In Ref. 17, a simulation box containing $3 \times 3 \times 3$ conventional unit cells of UO₂ is used, whereas we use in the present work a simulation box with $5 \times 5 \times 5$ unit cells. We therefore perform some test calculations with two different simulation box sizes ($3 \times 3 \times 3$ and $5 \times 5 \times 5$ unit cells) in order to quantify the bias introduced by the use of a smaller simulation box. The other settings remain equal. We find for both the rigid-ion and core-shell model higher recombination activation energies by 3 to 18% and 8 to 25% compared to our values obtained with the larger simulation box for oxygen and uranium FPs, respectively. The proximity of the defect images therefore appears to stabilize the defects. Hence, the differences with the calculations performed in Ref. 17 must stem from other settings in their calculations. As already mentioned, spurious periodic contributions could influence the dynamics of the recombination if the simulation box is too small with respect to the interstitial-vacancy distance. In the most dramatic case (uranium FPs of rank 5), the separation of the interstitial and the vacancy is indeed $1.5a_0$, half the side length of the simulation box when $3 \times 3 \times 3$ unit cells are used. We therefore expect the recombination activation energies calculated in the larger simulation box to be more reliable.

## III. RESULTS

### A. Frenkel pair formation energies

The Frenkel pair formation energies $E_f^X$ ($X=\text{O},\text{U}$) referring to infinite separations of the defect pairs for the selected potentials, namely the Morelon and Meis potentials, are calculated within the supercell approach using

$$
E_f^X = (E_V^X - E) + (E_I^X - E) \quad \text{with } X=\text{O},\text{U} \tag{11}
$$

where $E$, $E_V^X$, and $E_I^X$ are the energies of the pristine UO₂ system, the system with an $X$ atom vacancy, and the system with an interstitial $X$ atom, respectively. This approach is straightforward but is biased by the artificial interactions of the charged defect with its images due to the periodic boundary conditions.³⁷ Although the defect charge is compensated by a uniform background charge to ensure the charge neutrality of the supercell, the impact of the spurious Coulombic interactions between the defect an its images decays rather slowly due to its long-range character. For this reason, the Mott-Littleton method,³⁸ in which the defect is put in the center of a cluster of atoms embedded in an infinite dielectric medium, has so far been applied.²⁵,³⁹ This cluster approach requires some care concerning the radii of the spheres embedding the defect³⁹,⁴⁰ but converges for rather small systems, which is especially important when the system size for structural optimizations is limited by computational constraints.

![](./images/813311468605800449_2.jpg)

FIG. 2. Frenkel pair (FP) formation energies obtained for increasing cell sizes ranging from $2 \times 2 \times 2$ to $20 \times 20 \times 20$ for the core-shell potential of Meis and Chartier²⁴ and to $60 \times 60 \times 60$ for the rigid-ion potential of Morelon *et al.*, respectively.¹⁹ A cubic fit is applied for the extrapolation to an infinite cell size.

In this work we apply the supercell approach, because CP2K allows for an efficient and accurate optimization of rather large supercells. In this way, $E_f^X$ is calculated using Eq. (11) for supercells of increasing size. A cubic fit is applied to obtain the correct $E_f^X$ value for a infinitely large cell as shown in Fig. 2. All fits are excellent and exhibit correlation coefficients of at least 0.9998 or even better. The intersections with the $y$ axis yield the extrapolated values for the uranium and oxygen Frenkel pair formation energies $E_f^{\text{U}}$ and $E_f^{\text{O}}$, respectively. The obtained values are collected in Table I and compared to theoretical and experimental values from the literature.

The agreement for the oxygen FP formation energies is quite good for both model types, whereas the FP formation energies for uranium are much higher than the experimental value. However, it has to be noted that it is very difficult to derive such defect formation energies from experiments. In particular, the values for $E_f^{\text{U}}$ might not be reliable and should be considered with caution. Indeed, electronic structure calculations based on density functional theory including a Hubbard $U$ term (DFT $+U$) indicate a FP formation energy for uranium of more than 15 eV which is much closer to the values obtained with the empirical potentials.³⁵

<table>
<caption>TABLE I. The Frenkel pair (FP) formation energies obtained for the rigid-ion potential of Morelon <i>et al.</i><sup>19</sup> and the core-shell potential of Meis and Chartier<sup>24</sup> are compared with theoretical (DFT $+U$) and experimental values from the literature. The FP formation energies are given in eV.</caption>
<tbody><tr><td></td><td colspan="2">Govers <i>et al.</i><sup>25</sup></td><td colspan="2">This work</td><td rowspan="2">DFT $+U^{35}$</td><td rowspan="2">Experiment<sup>36</sup></td></tr>
<tr><td></td><td>Rigid-ion</td><td>Core-shell</td><td>Rigid-ion</td><td>Core-shell</td></tr>
<tr><td>$E_{f}^{\text{O}}$</td><td>3.9</td><td>4.6</td><td>3.84</td><td>4.50</td><td>3.95</td><td>3.0–4.0</td></tr>
<tr><td>$E_{f}^{\text{U}}$</td><td>15.7</td><td>18.6</td><td>15.42</td><td>17.95</td><td>15.08</td><td>9.5</td></tr>
</tbody></table>

Our values are all slightly smaller than the values obtained using the Mott-Littleton method. $^{25}$ The Mott-Littleton method seems to slightly overestimate the FP formation energies, especially in the case of uranium defects which impose a larger distortion to the host lattice due to their larger charge and size. Therefore, the differences might be due to the fact that perturbations in the continuum region representing the dielectric medium are neglected in the Mott-Littleton method.

### B. Defect migration energies
The defect migration energies of an oxygen interstitial $I_{\text{O}}$, an oxygen vacancy $V_{\text{O}}$, a uranium interstitial $I_{\text{U}}$, and a uranium vacancy $V_{\text{U}}$ are calculated for an increasing cell size using the Morelon and the Meis potential. The climbing image nudged elastic band (CI-NEB) method$^{21}$ is employed for the calculation of the minimum energy path (MEP). Various initial paths are investigated using 10 replica. A larger number of replica does not change the results, i.e., 10 replica ensure a sufficient flexibility of the band. Subsequently, the band is tightly optimized including its end points. The migration energies obtained for a single defect in the supercell are listed in Table II. The corresponding CI-NEB calculations with the defect pair (maximally separated) in the supercell do not alter the migration energies in the case of the larger supercells ($5 \times 5 \times 5$ and $10 \times 10 \times 10$) which proves the validity of the selected approach. The results in Table II are also compared to experimental and theoretical values from the literature. Although the experimental determination of migration energies is difficult, recent electronic structure calculations using DFT $+U$ show a reasonable agreement for the migration energies of oxygen interstitials and vacancies. $^{41}$ The corresponding data for uranium are, however, more difficult to obtain experimentally as well as theoretically.

The interstitialcy mechanism already described by Catlow$^{40}$ is found to be the lowest in energy for the $I_{\text{O}}$ migration. The value of about 0.7 eV agrees very well with the results of previous studies$^{19,25}$ using the Morelon potential. However, a slightly lower value of 0.6 eV is obtained with the Meis potential. In any case, the potentials of Morelon and Meis exhibit very similar activation energies for the migration of an oxygen interstitial atom. The activation energy for the migration of an oxygen vacancy is even smaller, especially with the Morelon potential. There is, again, a fair agreement with the results of Govers <i>et al.</i> $^{25}$ The same agreement is also found for the uranium vacancy migration. However, significant discrepancies are found for the migration energies of an interstitial uranium atom with both the Morelon and the Meis potential. We find lower activation energies for the concerted motion of two uranium atoms, an interstitial one in an octahedral site and its neighboring lattice uranium atom, along a cell axis. Both atoms squeeze through a square of neighboring oxygen atoms and, finally, the originally interstitial uranium atom occupies the original lattice site of the other uranium atom, whereas the second uranium atom moves concurrently from its lattice site to the next octahedral site. In particular, a much lower activation energy of about 2.3 eV is found with the Morelon potential. The optimization of migration paths

<table>
<caption>TABLE II. Defect migration energies obtained with the CI-NEB method$^{21}$ for increasing cell sizes using the rigid-ion potential of Morelon <i>et al.</i> $^{19}$ and the core-shell potentials of Meis and Chartier. $^{24}$ The migration energies for an oxygen interstitial $I_{\text{O}}$, an oxygen vacancy $V_{\text{O}}$, a uranium interstitial $I_{\text{U}}$, and a uranium vacancy $V_{\text{U}}$ are listed in eV. The results are compared to experimental and theoretical values from the literature. The employed theoretical method is indicated by EP (empirical potential) or DFT $+U$ (density functional theory plus a Hubbard $U$ term).</caption>
<tbody><tr><td>System size</td><td></td><td colspan="4">Rigid-ion$^{19}$</td><td colspan="4">Core-shell$^{24}$</td></tr>
<tr><td>unit cells</td><td>Method</td><td>$I_{\text{O}}$</td><td>$V_{\text{O}}$</td><td>$I_{\text{U}}$</td><td>$V_{\text{U}}$</td><td>$I_{\text{O}}$</td><td>$V_{\text{O}}$</td><td>$I_{\text{U}}$</td><td>$V_{\text{U}}$</td></tr>
<tr><td>$2 \times 2 \times 2$</td><td>EP</td><td>0.71</td><td>0.39</td><td>3.25</td><td>4.07</td><td>0.66</td><td>0.58</td><td>3.96</td><td>4.51</td></tr>
<tr><td>$3 \times 3 \times 3$</td><td>EP</td><td>0.69</td><td>0.35</td><td>2.53</td><td>3.91</td><td>0.64</td><td>0.54</td><td>3.59</td><td>4.58</td></tr>
<tr><td>$4 \times 4 \times 4$</td><td>EP</td><td>0.69</td><td>0.34</td><td>2.38</td><td>3.89</td><td>0.63</td><td>0.54</td><td>3.55</td><td>4.57</td></tr>
<tr><td>$5 \times 5 \times 5$</td><td>EP</td><td>0.69</td><td>0.34</td><td>2.35</td><td>3.88</td><td>0.62</td><td>0.54</td><td>3.55</td><td>4.58</td></tr>
<tr><td>$10 \times 10 \times 10$</td><td>EP</td><td>0.69</td><td>0.34</td><td>2.33</td><td>3.86</td><td>0.61</td><td>0.54</td><td>3.55</td><td>4.57</td></tr>
<tr><td>Morelon <i>et al.</i> $^{19}$</td><td>EP</td><td>0.65</td><td>0.33</td><td>5.00</td><td>4.46</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Govers <i>et al.</i> $^{25}$</td><td>EP</td><td>0.7</td><td>0.3</td><td>4.2</td><td>3.9</td><td>0.7</td><td>0.5</td><td>4.5/1.3</td><td>4.5</td></tr>
<tr><td>Dorado <i>et al.</i> $^{41}$</td><td>DFT+U</td><td>0.93</td><td>0.67</td><td></td><td></td><td>0.93</td><td>0.67</td><td></td><td></td></tr>
<tr><td>Experiment$^{36}$</td><td></td><td>0.8–1.0</td><td>0.5–0.6</td><td>$\approx$2.0</td><td>$\approx$2.4</td><td>0.8–1.0</td><td>0.5–0.6</td><td>$\approx$2.0</td><td>$\approx$2.4</td></tr>
</tbody></table>

<table>
<caption>TABLE III. The characteristics of the oxygen FPs, i.e., their rank, the distance between the vacancy and the interstitial, the number of possible interstitial positions, the recombination type, and the expression of the recombination times given as an upper bound or an Arrhenius fit of the simulation data, are presented for the fluorite structure up to a vacancy-interstitial distance of $1.5\,a_0$.</caption>
<thead>
  <tr>
    <th>Rank</th>
    <th>Distance ($a_0$)</th>
    <th>Number of possible interstitial</th>
    <th>Recombination type</th>
    <th>Times (ps): $\begin{cases} \begin{aligned} &\tau_{\text{rigid}}\ \text{[17]} \\ &\tau_{\text{rigid}}\ \text{(this work)} \\ &\tau_{\text{core-shell}}\ \text{(this work)} \end{aligned} \end{cases}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1st</td>
    <td>$\sqrt{3}/4$</td>
    <td>4</td>
    <td>Instantaneous/direct</td>
    <td>&lt;0.2<br>&lt;0.1<br>&lt;0.1</td>
  </tr>
  <tr>
    <td>2nd</td>
    <td>$\sqrt{11}/4$</td>
    <td>12</td>
    <td>Instantaneous/direct</td>
    <td>&lt;0.5<br>&lt;0.4<br>&lt;0.3</td>
  </tr>
  <tr>
    <td>3rd</td>
    <td>$\sqrt{19}/4$</td>
    <td>12</td>
    <td>Thermally activated/indirect</td>
    <td>$0.36\ \text{exp}(0.16/k_{\text{B}}T)$<br>$0.26\ \text{exp}(0.18/k_{\text{B}}T)$<br>$0.06\ \text{exp}(0.32/k_{\text{B}}T)$</td>
  </tr>
  <tr>
    <td>4th type I</td>
    <td>$\sqrt{27}/4$</td>
    <td>4</td>
    <td>Thermally activated/indirect</td>
    <td>$0.47\ \text{exp}(0.06/k_{\text{B}}T)$<br>$0.42\ \text{exp}(0.08/k_{\text{B}}T)$<br>$0.16\ \text{exp}(0.11/k_{\text{B}}T)$</td>
  </tr>
  <tr>
    <td>4th type II</td>
    <td>$\sqrt{27}/4$</td>
    <td>4</td>
    <td>Thermally activated/indirect</td>
    <td>$0.86\ \text{exp}(0.21/k_{\text{B}}T)$<br>$0.27\ \text{exp}(0.26/k_{\text{B}}T)$<br>$0.03\ \text{exp}(0.51/k_{\text{B}}T)$</td>
  </tr>
  <tr>
    <td>5th</td>
    <td>$\sqrt{35}/4$</td>
    <td>4</td>
    <td>Thermally activated/indirect</td>
    <td>$0.28\ \text{exp}(0.27/k_{\text{B}}T)$<br>$0.15\ \text{exp}(0.30/k_{\text{B}}T)$<br>$0.01\ \text{exp}(0.57/k_{\text{B}}T)$</td>
  </tr>
</tbody>
</table>

via the [110] direction or combined motions along the [100] and [110] direction yield much higher activation barriers of about 4.7 eV with the Morelon potential and even 6.5 eV with the Meis potential. Therefore, we suppose that the migration paths were not fully optimized in previous studies and, thus, the correct transition path (MEP) was not detected.

Finally, Table II also gives information about the model system size required for the study of FP recombinations. A model system size of $3 \times 3 \times 3$ primitive unit cells is already sufficient to obtain converged migration energies for an oxygen interstitial or vacancy, irrespective of the employed potential. However, for the migration of a uranium interstitial atom or a uranium vacancy at least $4 \times 4 \times 4$( but, better, $5 \times 5 \times 5$) primitive unit cells are required. For this reason, a model system composed of $5 \times 5 \times 5$ primitive unit cells as described in the next section was employed throughout the present study.

<table>
<caption>TABLE IV. The characteristics of the uranium FPs, i.e., their rank, the distance between the vacancy and the interstitial, the number of possible interstitial positions, the recombination type, and the expression of the recombination times given as an upper bound or an Arrhenius fit of the simulation data, are presented for the fluorite structure up to a vacancy-interstital distance of $1.5\,a_0$.</caption>
<thead>
  <tr>
    <th>Rank</th>
    <th>Distance ($a_0$)</th>
    <th>Number of possible interstitials</th>
    <th>Recombination type</th>
    <th>Times (ps): $\begin{cases} \begin{aligned} &\tau_{\text{rigid}}\ \text{[17]} \\ &\tau_{\text{rigid}}\ \text{(this work)} \\ &\tau_{\text{core-shell}}\ \text{(this work)} \end{aligned} \end{cases}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1st</td>
    <td>$1/2$</td>
    <td>6</td>
    <td>Instantaneous/direct</td>
    <td>&lt;0.4<br>&lt;0.3<br>&lt;0.3</td>
  </tr>
  <tr>
    <td>2nd</td>
    <td>$\sqrt{3}/2$</td>
    <td>8</td>
    <td>None<br>Thermally activated/indirect</td>
    <td>No recombination<br>$0.03\ \text{exp}(1.35/k_{\text{B}}T)$<br>$0.03\ \text{exp}(1.35/k_{\text{B}}T)$</td>
  </tr>
  <tr>
    <td>3rd</td>
    <td>$\sqrt{5}/2$</td>
    <td>24</td>
    <td>Instantaneous/indirect</td>
    <td>&lt;1.0<br>&lt;1.1<br>&lt;0.9</td>
  </tr>
  <tr>
    <td>4th type I</td>
    <td>$3/2$</td>
    <td>24</td>
    <td>Thermally activated/indirect</td>
    <td>$0.91\ \text{exp}(0.64/k_{\text{B}}T)$<br>$0.003\ \text{exp}(1.63/k_{\text{B}}T)$<br>$0.001\ \text{exp}(2.19/k_{\text{B}}T)$</td>
  </tr>
  <tr>
    <td>4th type II</td>
    <td>$3/2$</td>
    <td>24</td>
    <td>Thermally activated/indirect</td>
    <td>$0.062\ \text{exp}(1.31/k_{\text{B}}T)$<br>$0.005\ \text{exp}(1.51/k_{\text{B}}T)$<br>$0.001\ \text{exp}(2.23/k_{\text{B}}T)$</td>
  </tr>
</tbody>
</table>

![](./images/813311468605800449_3.jpg)

FIG. 3. (Color online) Arrhenius plots of the lifetimes of the oxygen FPs of rank (a) 1, (b) 2, (c) 3, (d) 4 of type I, (e) 4 of type II, and (f) 5 for different temperatures in the rigid-ion (black) and core-shell (red) model. The results of the simulations (data points and error bars) are shown together with the best fits of Eq. (12).

### C. Defect dynamics at finite temperature

The recombination data for the oxygen and uranium FP ranks are summarized in Tables III and IV, respectively. The lifetimes calculated in a previous study $^{17}$ with the same rigid-ion potential $^{19}$ are also presented for comparison. The lifetimes of the oxygen and uranium FPs calculated with the rigid-ion and core-shell model are compared in Fig. 3 and Fig. 4, respectively. The results are plotted using a logarithmic scale against $1/k_B T$, where $k_B$ is the Boltzmann constant and $T$ is the temperature. The data points and error bars are, respectively, the average over 30 simulations using 3 different initial configurations and 10 different initial velocities for each initial configuration and the corresponding standard deviation. The straight lines are the best fit using an Arrhenius function,
$$
\tau=\tau_{0} \exp \left(\frac{E_{a}}{k_{B} T}\right),\qquad(12)
$$
where $E_a$ is the recombination activation energy or energy barrier that an interstitial must overcome to recombine with the vacancy and $\tau_0$ is a pre-exponential factor.

The recombination energies for the oxygen FPs calculated in the present study and in the previous investigation $^{17}$ with the rigid-ion model are overall rather similar. However, the activation energies calculated in the present study are 10% to 25% higher than in the previous study (cf. comments in Sec. II C).

For rank 1 and rank 2 of the oxygen FPs, the lifetimes are insensitive to the temperature and the recombination occurring in both models in less than 0.1 and 0.4 ps, respectively, can be regarded as instantaneous. As shown in Fig. 5(a), the recombination of the FP of rank 1 is direct along the [111] crystallographic direction while the recombination of rank 2 is indirect with a first hop of the vacancy along the [100] crystallographic direction followed by the recombination along the [111] crystallographic direction [cf. Fig. 5(b)].

For the higher ranks, the lifetimes of the FPs are clearly temperature dependent. As already mentioned in Ref. 17 for the rigid-ion model, the lifetimes do not increase regularly in correspondence of the rank, e.g., the separation distance between the interstitial and the vacancy. The lifetimes of rank 3 are higher than those of rank 4 of type I with an activation energy of 0.18 and 0.08 eV in the rigid-ion model, respectively, and 0.32 and 0.11 eV in the core-shell model, respectively. By contrast, the lifetimes of rank 4 of type II and rank 5 follow a similar evolution with activation energies of 0.26 and 0.30 eV in the rigid-ion model, respectively, and 0.51 and 0.57 eV in the core-shell model, respectively. The same evolution trend with the rank is, therefore, observed in both models. As suggested in Ref. 17, this behavior probably originates in the differences of the migration paths. While the recombination path involves two hops along the [001] and [010] directions, and then a recombination along [111] for the FP of rank 3 [cf.

![](./images/813311468605800449_4.jpg)

FIG. 4. (Color online) Arrhenius plots of the lifetimes of the uranium FPs of rank (a) 1, (b) 2, (c) 3, and (d) 4 of type I and (e) 4 of type II for different temperatures in the rigid-ion (black) and core-shell (red) model. The results of the simulations (data points and error bars) are shown together with the best fits of Eq. (12).

Fig. 5(c)], it, first, takes place with two hops in the same [100] direction for the FP of rank 4 of type I [cf. Fig. 5(d)]. The change of direction between the hops of the recombination path therefore appears to have a major impact on the lifetime of the FP. This contribution is even more significant in the case of the core-shell model. For the FPs of ranks 3 and 4 of type II and rank 5 which involve an important reorientation of the recombination path between the hops [cf. Fig. 5], the difference of the lifetimes calculated in the rigid-ion and core-shell model can reach an order of magnitude at low temperatures ($T < 600$ K). At higher temperatures ($T > 1000$ K), the kinetic energy is so high that the difference between the recombination activation energies calculated with the rigid-ion and core-shell model cannot be monitored and the lifetimes become similar. On the other hand, the difference is much less pronounced at any temperature in the case of the FP of rank 4 of type I which features a straighter recombination path [cf. Fig. 5(d)].

The recombinations of the uranium FPs are then analyzed. As already mentioned, regarding the oxygen FPs, the recombination activation energies calculated in the present study are overall higher than those found by Van Brutzel et al.¹⁷ (cf. comments in Sec. II C). Moreover, the difference between our results and those found by Van Brutzel et al.¹⁷ is much higher than in the case of the oxygen FPs. In the case of the uranium FP of rank 4 type I, the activation energies are 0.64 and 1.63 eV in the previous¹⁷ and present study, respectively. An even more striking difference arises in the case of the FP of rank 2, for which Van Brutzel et al.¹⁷ found no recombination in contrast with our study.

For the uranium FP of rank 1, the recombination is direct and instantaneous along the [100] direction both in the rigid-ion and core-shell model [see Fig. 6(a)]. The lifetimes do not exceed 0.3 ps at any temperature in both models. The recombination of the FP of rank 2 is thermally activated and indirect. It takes place with a first hop along the [100] direction followed by a second hop along the [110] direction. As mentioned in Ref. 17, one possible reason for the stability of this FP is the difficulty of the oxygen atom present along the [111] direction between the uranium interstitial and the vacancy to move away from the vacancy to facilitate its migration. This configuration would hinder the hop along the [110] direction and explain the high energy barrier of 1.35 eV for the recombination in both models. In this case, the explicit description of the polarizability would not play a major role and its effect would be screened by the mechanical stiffness of the structure.

For the uranium FP of rank 3, the recombination is insensitive to the temperature and occurs in less than 1.1 and 0.9 ps in the rigid-ion and core-shell model, respectively.

![](./images/813311468605800449_5.jpg)

FIG. 5. (Color online) Schematic representations of the migration paths for the recombination of the oxygen FPs of rank (a) 1, (b) 2, (c) 3, and (d) 4 of types I and II and (e) 5.

The recombination occurs through a first hop along the [110] direction followed by a second hop along the [100] direction.

There are two types of uranium FPs of rank 4 due to the symmetry. Both are temperature dependent and recombine in an indirect manner. For type I, the recombination occurs with three successive replacements consisting of two hops of the vacancy along the [110] direction and a recombination along the [100] direction. For type II, the vacancy hops along the [100] direction and then recombines with the interstitial along the same direction. The activation energies for both types are similar modelwise. The energy barrier for the FPs of type I and II is 1.63 and 1.51 eV in the rigid-ion model, respectively, and 2.19 and 2.23 eV in the core-shell model, respectively.

The differences between the recombination activation energies calculated with the rigid-ion and the core-shell model are less pronounced in the case of the uranium FPs than in the case of the oxygen FPs. In the cases of the uranium FPs, the correlation between the changes of direction between the hops of the recombination path and the lifetime of the corresponding FP is also not found. While the recombination path of the uranium FP of rank 4 of type I follows several modifications of direction, that of the uranium FP of rank 4 of type II is straight. Yet the comparison of the calculated recombination energies in the rigid-ion and core-shell formalism is similar in both cases. In the case of the uranium FPs, the distance between the interstitial and the vacancy is then the only factor influencing the lifetime of the FP that can be identified.

![](./images/813311468605800449_6.jpg)

FIG. 6. (Color online) Schematic representations of the migration paths for the recombination of the uranium FPs of rank (a) 1, (b) 2, (c) 3, and (d) 4 of type I and (e) 4 of type II.

It is also instructive to compare the oxygen diffusion coefficients corresponding to the recombination of the oxygen FPs of ranks 3 to 5 with those calculated in a stoichiometric $\mathrm{UO}_{2}$ matrix and in a hypostoichiometric $\mathrm{UO}_{1.95}$ matrix containing pre-existing oxygen vacancies (cf. Fig. 7). The oxygen diffusion coefficients corresponding to the recombination of the oxygen FPs of ranks 3 to 5 are expressed by the following expression:
$$
D=\frac{d^{2}}{\tau_{0}} \exp \left(E_{a} / k_{B} T\right),\qquad(13)
$$
where $d$ is the distance between the vacancy and the interstitial, $\tau_{0}$ is the pre-exponential factor, and $E_{a}$ is the activation energy found in Sec. III. The oxygen diffusion coefficients calculated from the mean-square displacements of the oxygen atoms

![](./images/813311468605800449_7.jpg)

FIG. 7. (Color online) Arrhenius plots of the oxygen diffusion coefficients in $UO_2$ and $UO_{1.95}$ compared with the oxygen diffusion coefficients for the FP recombination. The simulation data and fits are represented by closed symbols and solid lines for the rigid-ion model and open symbols and dashed lines for the core-shell model, respectively.

in a stoichiometric $UO_2$ matrix and in a hypostoichiometric $UO_{1.95}$ matrix containing pre-existing oxygen vacancies are also plotted in Fig. 7 (for uranium atoms, no diffusion occurred in either model even in matrices containing pre-existing uranium vacancies). The oxygen diffusion is significantly accelerated in both models in the presence of pre-existing vacancies. The migration energy drops from 2.74 to 0.83 eV and from 2.94 to 0.62 eV in the rigid-ion and core-shell model, respectively. However, in both models, the recombination diffusion coefficients corresponding to all oxygen Frenkel pairs are at least two orders of magnitude higher than the oxygen diffusion coefficients in $UO_2$ and $UO_{1.95}$. Moreover, the activation energies for the recombination are lower than the defect migration energies (0.30 and 0.57 eV for the highest with rank 5 in the rigid-ion and core-shell model, respectively, to be compared with 0.83 and 0.62 eV in $UO_{1.95}$). It should be noted that the oxygen diffusion coefficients in $UO_2$ and $UO_{1.95}$ in the core-shell model follow the trend of the oxygen diffusion coefficients related to the recombination of the oxygen FPs to be lower than in the rigid-ion model.

## IV. DISCUSSION

The results regarding the recombination of the oxygen and uranium FPs presented in the previous section show that the rigid-ion and core-shell model provide a similar qualitative description of the FP stabilities. In both models, two regimes of FP defect stability can be identified. Moreover, a given FP defect falls into the same regime regardless of the model description. In the first regime, the recombination of the FP defect happens in 1 ps or less and can be considered instanta- neous. In the second regime, the recombination mechanism is thermally activated and activation energies representing the energies to be overcome for the recombination to happen are determined using the Arrhenius representation for the evolution of the FP lifetimes. Two reference recombination distances then can be defined as already mentioned in Ref. 17. The "spontaneous recombination distance" below which the recombination is instantaneous (>1 ps) and is thermally independent was found in Ref. 17 to be $6/5 a_0$ for the uranium FPs and $4/5 a_0$ for the oxygen FPs, where $a_0$ is the lattice parameter. Similar values are found in the present study if we exclude the uranium FP of rank 2 which was found to be stable on the time scale of the simulation in Ref. 17. The "thermal recombination distance" below which the recombination of the FP is thermally dependent could only be assigned a lower bound corresponding to $3/2 a_0$ for both uranium and oxygen FPs (due to the maximum interstitial-vacancy distance considered herein), in agreement with Ref. 17. However, the separation distance between the interstitial and the vacancy is not the only factor accounting for the stability of the FPs. Indeed, a dependence of the recombination time of the FP defect with respect to the direction of the migration path in the matrix and more specifically of the change of direction between the hops of the recombination path can be identified in the case of the oxygen FPs. For the FPs of ranks 3 and 4 of type II and rank 5 which involve an important reorientation of the recombination path between the hops, the polarizability stabilizes the FP defect and the difference of the lifetimes calculated in the rigid-ion and core-shell model can reach an order of magnitude at low temperatures ($T < 600$ K). On the other hand, the difference is much less pronounced at any temperature in the case of the FP of rank 4 of type I when the recombination path is straighter. On the contrary, a similar trend cannot be straightforwardly identified for the uranium FPs where the activation energies are closer together. A second factor acting on the FP stability atop the interstitial-vacancy distance is the mechanical stiffness of the surrounding matrix. This effect is illustrated in the case of the uranium FP of rank 2, in which recombination is thermally activated, whereas the recombination of the uranium FP of rank 3 is athermal in both models. In the former instance, similar values for the activation energies are found in both models. Even if the separation distance between the interstitial and the vacancy is relatively small, the recombination mechanism is hindered by the neighboring atoms, resulting in a high activation energy. The mechanical stiffness of the structure is then preponderant compared to the polarizability. On the other hand, in the case of uranium FP of rank 3, even if the separation distance between the interstitial and the vacancy is higher, the recombination is not hindered by the matrix structure and the recombination occurs instantaneously.

These differences in the recombination time between the rigid-ion and the core-shell model at low temperatures ($T < 800$ K for oxygen FPs and $T < 2000$ K for uranium FPs) are relevant for the simulations of displacement cascades. Even though the temperature can be higher at the heart of the cascade where the first interatomic collision occurs, the two models may lead to significantly different descriptions of the recrystallization at the periphery of the cascade where the temperature is lower. The explicit treatment of polarizability in the core-shell model is expected to provide a better representation of the displacement cascade mechanism and a better estimation of the timing of the self-healing process in $UO_2$, responsible for its tolerance to irradiation.

## V. CONCLUSIONS

We studied oxygen and uranium point defects in the $\mathrm{UO}_{2}$ fluorite structure with two models of empirical interatomic potentials, namely a rigid-ion and a core-shell model. The oxygen and uranium FP formation energies and the defect migration energies of the oxygen and uranium interstitials and vacancies were first calculated through optimization calculations without the inclusion of temperature effects. A slightly better description is achieved with the rigid-ion model$^{17}$ as it was specifically fitted to the defect formation and migration energies. However, the description of the FP recombination mechanism requires a potential featuring the flexibility to properly describe the response of the material to important pertubations of the local environment around the ions. The overall picture indicates that the FP recombination mechanism is a complex process involving several phenomena. The FP recombination can happen instantaneously when the distance between the interstitial and the vacancy is relatively small or can be thermally activated at larger distances. However, the interstitial-vacancy distance is not the only criterion and other factors can prevail, such as the surrounding environment of the FP defect, the mechanical stiffness of the matrix, and the orientation of the migration path. The rigid-ion and core-shell models provide a similar qualitative description of the FP recombination mechanism. However, significant quantitative differences arise at low temperatures regarding the FP stability. Indeed, the recombination time of the oxygen and uranium FPs can be up to an order of magnitude lower in the core-shell model at $T=600$ K and $T=1800$ K, respectively. These differences would certainly affect the description of the recrystallization process following a displacement cascade. The self-healing phase then could be better accounted for in the core-shell model and the misestimate inherent to the lack of polarizability in the rigid-ion model could be corrected.

## ACKNOWLEDGMENTS

We acknowledge useful interactions with G. Martin and L. Van Brutzel. This research is supported by the European Commission through the FP7 F-BRIDGE Project (Contract No. 211690). The generous allocation of computer time and the support from the Swiss National Supercomputing Centre (CSCS, Manno) is also acknowledged.

*Current address: Institute of Physical Chemistry, University of Zurich, Winterthurerstrasse 190 CH-8057 Zurich, Switzerland.
†Corresponding author: matthias.krack@psi.ch
$^{1}$H. Matzke and J. L. Whitton, Can. J. Phys. 44, 995 (1966).
$^{2}$K. Trachenko, J. Phys.: Condens. Matter 16, 1491R (2004).
$^{3}$H. M. Naguib and R. Kelly, Radiat. Eff. 25, 1 (1975).
$^{4}$L. W. Hobbs, Nucl. Instrum. Methods B 91, 30 (1994).
$^{5}$L. W. Hobbs, F. W. C. Jr., S. J. Zinkle, and R. C. Ewing, J. Nucl. Mater. 216, 291 (1994).
$^{6}$L. W. Hobbs, J. Non-Cryst. Solids 182, 27 (1995).
$^{7}$K. E. Sickafus, L. Minervini, R. W. Grimes, J. A. Valdez, M. Ishimaru, F. Li, K. J. McClellan, and T. Hartmann, Science 289, 748 (2000).
$^{8}$K. E. Sickafus, L. Minervini, R. W. Grimes, J. A. Valdez, and T. Hartmann, Radiat. Eff. Defects Solids 155, 133 (2001).
$^{9}$K. E. Sickafus, J. A. Valdez, J. R. Williams, R. W. Grimes, and H. T. Hawkins, Nucl. Instrum. Methods B 191, 549 (2002).
$^{10}$J. Lian, L. M. Wang, R. C. Ewing, S. V. Yudintsev, and S. V. Stefanovsky, J. Appl. Phys. 97, 113536 (2005).
$^{11}$A. Chartier, C. Meis, J.-P. Crocombette, W. J. Weber, and L. R. Corrales, Phys. Rev. Lett. 94, 025505 (2005).
$^{12}$L. V. Brutzel, M. Rarivomanantsoa, and D. Ghaleb, J. Nucl. Mater. 354, 28 (2006).
$^{13}$L. Brutzel and M. Rarivomanantsoa, J. Nucl. Mater. 358, 209 (2006).
$^{14}$G. Martin, S. Maillard, L. V. Brutzel, P. Garcia, B. Dorado, and C. Valot, J. Nucl. Mater. 385, 351 (2009).
$^{15}$J.-P. Crocombette and A. Chartier, Nucl. Instrum. Methods B 250, 24 (2006).
$^{16}$A. Chartier, G. Catillon, and J.-P. Crocombette, Phys. Rev. Lett. 102, 155503 (2009).
$^{17}$L. Van Brutzel, A. Chartier, and J. P. Crocombette, Phys. Rev. B 78, 024111 (2008).
$^{18}$N. Pannier, A. Guglielmetti, L. V. Brutzel, and A. Chartier, Nucl. Instrum. Methods B 267, 3118 (2009).
$^{19}$N. D. Morelon, D. Ghaleb, J. M. Delaye, and L. Van Brutzel, Philos. Mag. 83, 1533 (2003).
$^{20}$B. G. Dick and A. W. Overhauser, Phys. Rev. 112, 90 (1958).
$^{21}$G. Henkelman, B. P. Uberuaga, and H. Jonsson, J. Chem. Phys. 113, 9901 (2000).
$^{22}$P. J. Mitchell and D. Fincham, J. Phys.: Condens. Matter 5, 1031 (1993).
$^{23}$ CP2K developers group 2000–2012, http://www.cp2k.org.
$^{24}$C. Meis and A. Chartier, J. Nucl. Mater. 341, 25 (2005).
$^{25}$K. Govers, S. Lemehov, M. Hou, and M. Verwerft, J. Nucl. Mater. 366, 161 (2007).
$^{26}$K. Govers, S. Lemehov, M. Hou, and M. Verwerft, J. Nucl. Mater. 376 66 (2008).
$^{27}$G. Martin, P. Garcia, L. V. Brutzel, B. Dorado, and S. Maillard, Nucl. Instrum. Methods B 269, 1727 (2011).
$^{28}$R. A. Jackson, A. D. Murray, J. H. Harding, and C. R. A. Catlow, Philos. Mag. A 53, 27 (1986).
$^{29}$M. Krack, in Material Challenges in Current and Future Nuclear Technologies, Vol. 1383 (Materials Research Society, Warrendale, PA, 2012).
$^{30}$P. P. Ewald, Ann. Phys. 369, 253 (1921).
$^{31}$U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee, and L. G. Pedersen, J. Chem. Phys. 103, 8577 (1995).
$^{32}$P. J. D. Lindan and M. J. Gillan, Philos. Mag. B 69, 535 (1994).
$^{33}$R. Car and M. Parrinello, Phys. Rev. Lett. 55, 2471 (1985).
$^{34}$T. D. Kühne, M. Krack, F. R. Mohamed, and M. Parrinello, Phys. Rev. Lett. 98, 066401 (2007).

$^{35}$P. Nerikar, T. Watanabe, J. S. Tulenko, S. R. Phillpot, and S. B. Sinnott, *J. Nucl. Mater.* **384**, 61 (2009).

$^{36}$H. Matzke, *J. Chem. Soc., Faraday Trans. 2* **83**, 1121 (1987).

$^{37}$M. Leslie and N. J. Gillan, *J. Phys. C* **18**, 973 (1985).

$^{38}$N. F. Mott and M. J. Littleton, *Trans. Faraday Soc.* **34**, 485 (1938).

$^{39}$M. S. Read and R. A. Jackson, *J. Nucl. Mater.* **406**, 293 (2010).

$^{40}$C. R. A. Catlow, *Proc. Roy. Soc. Ser. A* **353**, 533 (1977).

$^{41}$B. Dorado, P. Garcia, G. Carlot, C. Davoisne, M. Fraczkiewicz, B. Pasquet, M. Freyss, C. Valot, G. Baldinozzi, D. Siméone, and M. Bertolus, *Phys. Rev. B* **83**, 035126 (2011).