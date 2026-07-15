First-principles investigation of spin-phonon coupling in vanadium-based molecular
spin qubits

$^{1}$Andrea Albino, $^{2}$Stefano Benci, $^{1}$Lorenzo Tesi, $^{3}$Matteo Atzori, $^{2}$Renato
Torre, $^{4}$Stefano Sanvito, $^{1}$Roberta Sessoli,$^{*}$ and $^{4}$ Alessandro Lunghi$^{\dagger}$

$^{1}$ Dipartimento di Chimica "Ugo Schiff" and INSTM RU,
Universitá degli Studi di Firenze, I50019 Sesto Fiorentino, Italy
$^{2}$ Dipartimento di Fisica ed Astronomia and European Laboratory for Nonlinear Spectroscopy,
Universitá degli Studi di Firenze, I50019 Sesto Fiorentino, Italy
$^{3}$ Dipartimento di Chimica "Ugo Schiff" and INSTM RU,
Universitá degli Studi di Firenze, I50019 Sesto Fiorentino,
Italy. Present address: Laboratoire National des Champs Magnetiques Intenses,
UPR 3228 - CNRS, F38042 Grenoble, France. and
$^{4}$ School of Physics, CRANN and AMBER, Trinity College, Dublin 2, Ireland

Paramagnetic molecules can show long spin-coherence times, which make them good
candidates as quantum bits. Reducing the efficiency of the spin-phonon interaction is
the primary challenge towards achieving long coherence times over a wide temperature
range in soft molecular lattices. The lack of a microscopic understanding about the
role of vibrations in spin relaxation strongly undermines the possibility to chemically
design better performing molecular qubits. Here we report a first-principles charac-
terization of the main mechanism contributing to the spin-phonon coupling for a class
of vanadium(IV) molecular qubits. Post Hartree Fock and Density Functional Theory
are used to determine the effect of both reticular and intra-molecular vibrations on
the modulation of the Zeeman energy for four molecules showing different coordination
geometries and ligands. This comparative study provides the first insight into the role
played by coordination geometry and ligand field strength in determining the spin-
lattice relaxation time of molecular qubits, opening the avenue to a rational design of
new compounds.

## I. INTRODUCTION

Quantum information science deals with the represen-
tation, storage and processing of information by means
of a quantum mechanical system. The basic element is
the quantum bit or qubit, namely the quantum analo-
gous of the classical bit $(0,1)$. Quantum computation
exploits the quantum properties of the qubit, such as
superposition and entanglement, [1] providing an ideal
platform for improving algorithms' efficiency. In particu-
lar, one can design a range of quantum algorithms, which
scale with the complexity of the problem in a much more
favourable way than their classical counterparts. Several
systems are currently investigated for the practical real-
ization of quantum devices. For example: superconduct-
ing circuits, [2] trapped ions [3] and polarized photons.[4]
Among the various physical systems with potential for
developing quantum technologies the spin, with its intrin-
sic two-levels qubit structure, occupies a special place.

Both nuclear spins[5] and electron spins,[6] as well as
electron-nuclear hybrid systems,[7, 8] can be exploited for
this purpose. Electron spins interact more strongly with
the environment, compared to the nuclear ones, and thus
they are easier to read out. In contrast, electrons have
shorter spin lifetimes and must be carefully protected
from the environment, while keeping the possibility to
interact with each others. In practice three physical sys-
tems implement spin qubits: nitrogen-vacancy centres
in diamond (NVC),[9] atomic impurities in semiconduc-
tors, such as P implanted in Si,[10] and paramagnetic
molecules.[11-13] In contrast to solid-state spin qubits
based on dopant atoms, such as the NVCs, molecules
show a significant advantage, namely the chemical sys-
tems hosting the spin can be tailored to tune the quan-
tum properties and the coupling to other qubits. This can
create quantum platforms,[8, 14, 15] providing a bottom-
up route to large-scale quantum register fabrication.

A spin lifetime at least $10^{4}$ times longer than the time
needed for an individual quantum operation[16, 17] rep-
resents the minimal requirement for the development of
a qubit. Accordingly, the figures of merit to consider in
the design of electronic spin molecular qubits are funda-
mentally two:[18] $i)$ the longitudinal (or spin-lattice[19])
relaxation time, $T_{1}$, which corresponds to the lifetime
of a classical bit; $ii)$ the coherence (or spin-spin relax-
ation) time, $T_{2}$, which is the time characteristic for a
spin to loose memory of a coherent quantum superpo-
sition state. In the last few years, remarkable results
have been achieved against both $T_{1}$ and $T_{2}$ by investigat-
ing mononuclear transition-metal complexes.[13, 18, 20-
28] These results place molecules containing light met-
als back in the quantum race. [29] Vanadium(IV)-based
complexes represent a promising class of compounds to
be used as fundamental components in quantum tech-

* roberta.sessoli@unifi.it
$^{\dagger}$ lunghia@tcd.ie

nologies. These spin 1/2 systems show long spin-spin relaxation time $T_2$, up to 1 millisecond at liquid helium temperature, when complexed with nuclear-spin free lig- ands and diluted in nuclear-spin free solvents.[30] This property makes $V^{IV}$-based compounds very attractive for further development.

A common trend found in molecular spins[27, 31] is the rapid decrease of $T_2$ on raising the temperature, a feature that limits their potential use at room temper- ature. The interaction with lattice vibrations, typically connected to the $T_1$-type relaxation, also contributes to the $T_2$-type one and becomes the predominant relaxation mechanism when increasing temperature.[24] In solids, thermal motion is usually described by phonons, which are energy quanta of lattice vibrations. Spin-lattice re- laxation is caused by the absorption/emission of phonons by the spin system. This process is possible due to the presence of spin-orbit coupling,[32] an interaction that couples atomic and spin degrees of freedom and enables the energy exchange among the two systems.

Although the experimental investigations in this field are numerous,[18, 26, 28, 31, 33] the theoretical descrip- tion is still at an early stage.[14, 34–37] In particular, the possibility to include molecules in a solid ab initio computational framework has been made possible only in the last few years, enabled by an extensive work of in- tegration of density functional theory (DFT), post Hatree Fock (postHF) methods and spin dynamics for the calcu- lation of the dynamical magnetic properties of multi-spin systems.

The present work introduces a comparative theoret- ical investigation of the spin-lattice relaxation in four $V^{IV}$ molecular complexes (Figure 1). In particular, we have focused on penta-coordinated vanadyl ($VO^{2+}$) and hexa-coordinated $V^{IV}$ molecules, where the coordination is obtained by cathecolate[31] and dithiolene[28] ligands, namely $[PPh_4]_2[VO(cat)_2]$ (1), $[PPh_4]_2[V(cat)_3]$ (2), $[PPh_4]_2[VO(dmit)_2]$ (3), $[PPh_4]_2[V(dmit)_3]$ (4) (cat = catecholate, dmit = 1,3-dithiole-2-thione-4,5-dithiolate, $PPh_4$ = tetraphenylphosphonium). These complexes have already experimentally shown to possess long co- herence times and remarkable differences in the temper- ature dependence of the spin-lattice relaxation time. Our approach consists in modelling their magnetic properties by first-principles, when perturbing the molecular struc- tures along the normal modes of vibration, following a strategy adopted in previous works.[34, 36] In order to correctly account for the vibrational properties of solid state systems, where intermolecular interactions become relevant, DFT calculations are performed in the crys- tal phase, in contrast to previous studies where the gas phase was taken into consideration.[34] The quality of our computed vibrational properties is ascertained by IR vibrational spectroscopy in the THz range. The informa- tion extracted from DFT and post Hartee-Fock methods together provide a fingerprint description of the inter- action between vibrations and magnetism, and directly correlate to the structure of each compound. The corre- lation found between the spin-phonon interaction ampli- tudes and experimental spin-lattice relaxation times for the four compounds is then discussed.

## II. METHODS

### A. Vibrational properties calculations

The simulations of the crystals' vibrational properties are performed with a Gaussian and plane waves (GPW) formalism as implemented in the Quickstep module[38] of the CP2K[39, 40] package. The GGA[41] functional in the *Perdew-Burke-Ernzerhof* approximation[42] (PBE) is chosen for all the calculations. Van-der-Waals inter-actions are taken into account with the non local rVV10 correction scheme.[43] The calculation of the Hessian ma- trix is performed by finite differences, the Hessian matrix is symmetrized averaging it with its transpose and the acoustic sum rule is applied to impose the translational invariance.[44] Each atomic coordinate is displaced by $\pm0.01\mathrm{\AA}$ around the equilibrium configuration, and such displacements are used to compute energies and forces. When displacing the atoms we have taken into account the crystal's symmetries and only inequivalent displace- ments have been considered (see Figure S1 in Supple- mentary Information - SI). The exploitation of symme- try allows us to reduce the computational overheads by a factor of four for all the systems considered. The diag- onalization of the Hessian matrix provides the phonons frequencies, $\omega_\alpha$ (Table S1 in SI), and the normal modes of vibrations, $q_\alpha$. The latter are stored in the columns of the Hessian's eigenvectors matrix $\mathbf{L}$.

### B. Spin-phonon coupling coefficients calculations

The calculation of the spin and the spin-phonon Hamiltonian parameters has been carried out with the ORCA[45, 46] package. The level of theory used is Com- plete Active Space Self Consistent Field plus second order perturbation theory (CASSCF+NEVPT2), with a def2- TZVP basis set for V, O and S, whereas def2-SVP is used for C and H. The active space includes one electron and the five $d$-orbitals of the molecule. The molecular geome- try used for these simulations is obtained by the periodic DFT calculation for the optimized crystal cell.

The calculation of the spin-phonon coupling coeffi- cients is performed following a tensor differentiation procedure as described in a previous report on Single Molecule Magnets (SMMs).[36] This procedure is here applied to the Landé $\mathbf{g}$ tensor that describes the coupling between the spins and an external magnetic field. Each element of the Landé tensor of the equilibrium structure (indicated by the subscript 0) is differentiated with re- spect to the $3M$ *atomic Cartesian positions* $(\partial\mathbf{g}/\partial\mathbf{X})_0$, where $M$ is the number of atoms in the molecule, in- stead of the $3N$ unit-cell vibrational coordinates, $q_\alpha$,[37]

![](./images/867772188499903077_1.jpg)

**FIG. 1.** Molecular structures of the dianionic complexes 1-4 with the first coordination sphere atom labelling scheme.

(see Figure S2 in SI). This approach requires a number of $\mathbf{g}$-derivatives equal to $3M=78$, instead of $3N=1392$ for $[\text{VO(cat)}_2]^{2-}$, and $3M=111$ instead of $3N=1524$ for $[\text{V(cat)}_3]^{2-}$ (see Table I). The $\mathbf{g}$ tensor is calculated for six displaced geometries ($\pm0.0050Å$, $\pm0.0075Å$, $\pm0.0150Å$) around the equilibrium configuration for the $3M$ molecular coordinates. The $\mathbf{g}$-versus-displacement curves are then fitted to a second order polynomial expression (see Figs. S3 and S4 in the SI for a demonstration of the fit quality).

The Cartesian derivatives of the $\mathbf{g}$ tensor are used to compute two important parameters: the average molecular spin-phonon coupling, $|\partial\mathbf{g}|$, and the phonon-projected spin-phonon coupling coefficients, $(\partial\mathbf{g}/\partial q_\alpha)_0$. The forms are defined as,
$$
|\partial\mathbf{g}| = \sum_{lv}^{M,3} \sum_{jr}^{3} \left| \left( \frac{\partial g_{jr}}{\partial X_{lv}} \right)_0 \right|, \tag{1}
$$
where the index $l$ runs over the number of atoms in the molecule and $v$ runs over the cartesian coordinates. The phonons projected spin-phonon coupling coefficients are instead defined as
$$
\left( \frac{\partial\mathbf{g}}{\partial q_\alpha} \right)_0 = \sum_{i}^{3M} \sqrt{\frac{\hbar}{\omega_\alpha m_i}} L_{i\alpha} \left( \frac{\partial\mathbf{g}}{\partial X_i} \right)_0, \tag{2}
$$
where the index $\alpha$ runs over the normal modes, the index $i$ over the $3M$ molecular degrees of freedom and $L_{i\alpha}$ is the Hessian's eigenvectors matrix.

### C. Experimental
Compounds 1-4 were prepared as described in the literature.[28, 31] THz spectra were measured by time-domain transmission spectroscopy using a table-top experimental set-up equipped with optical laser pulses (T-light 780 nm fiber laser, MenloSystems) and low-temperature GaAs photoconductive antennas. Low temperatures measurements are allowed by means of a closed-cycle Helium cryostat in the temperature range from 10 to 300 K. The developed acquisition procedure enables to achieve a signal-to-noise ratio higher than what is commonly achieved in standard far-infrared investigations. The accurate analysis of the data enables to disentangle the signals from spurious contributions coming from multiple reflections. The detailed description of the experimental set-up and of the material parameters extraction procedure (i.e. absorption coefficient, refractive index) is reported elsewhere.[47, 48] The spectra were measured in pellets of 13.2 mm diameter and thickness of about 0.7 mm. These were made by pressing under a manual hydraulic press ($\sim0.8$ GPa) a mixture of microcrystals and polyethylene powder (Merck).

## III. RESULTS
### A. Spin-phonon dynamics theory
If we limit ourselves to the study of spin dynamics in the presence of an external magnetic field, $\boldsymbol{B}$, the spin Hamiltonian of an $|\boldsymbol{S}|$=1/2 system will only contain the Zeeman term,
$$
\mathscr{H}_\text{s} = \mu_\text{B} \boldsymbol{B} \cdot \mathbf{g} \cdot \boldsymbol{S}, \tag{3}
$$
where $\mu_\text{B}$ is the Bohr magneton and $\mathbf{g}$ is the Landè tensor. The hyperfine and spin-spin dipolar interactions have been neglected in Equation 3 because in high fields their matrix elements are negligible.

When dealing with relaxation properties, it is necessary to introduce in the description the effects of the environment on the dynamics of the system described. For this we need an open quantum systems formalism.[50] Here the spin system interacts with an environment made of the crystal's phonons. Their Hamiltonian, describing the normal modes of vibration, is obtained as the second-order Taylor expansion of the nuclei potential energy surface and reads
$$
\mathscr{H}_\text{ph} = \sum_\alpha \hbar\omega_\alpha(n_\alpha + \frac{1}{2}), \tag{4}
$$


<table><thead><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Molecule</td><td>$[VO(cat)_{2}]^{2-}$</td><td>$[V(cat)_{3}]^{2-}$</td><td>$[VO(dmit)_{2}]^{2-}$</td><td>$[V(dmit)_{3}]^{2-}$</td></tr></thead><tbody><tr><td>Counter-ion</td><td>$2×[PPh_{4}]^{+}$</td><td>$2×[PPh_{4}]^{+}$</td><td>$2×[PPh_{4}]^{+}$</td><td>$2×[PPh_{4}]^{+}$</td></tr><tr><td>Molecule Atoms (M)</td><td>26</td><td>37</td><td>18</td><td>25</td></tr><tr><td>Crystal Cell Atoms (N)</td><td>464</td><td>508</td><td>432</td><td>460</td></tr><tr><td>Crystal System</td><td>monocline</td><td>monocline</td><td>monocline</td><td>monocline</td></tr><tr><td>Spatial Group</td><td>P21/c</td><td>C2/c</td><td>C2/c</td><td>P21/c</td></tr><tr><td>Site symmetry (Z)</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td></td><td>exp. sim.</td><td>exp. sim.</td><td>exp. sim.</td><td>exp. sim.</td></tr><tr><td>Cell Volume, Å³</td><td>4734.95 4477.07</td><td>5015.83 4758.34</td><td>5346.43 4941.81</td><td>5744.23 5428.57</td></tr><tr><td>a, Å</td><td>13.25 12.95</td><td>15.31 14.99</td><td>20.47 19.62</td><td>24.57 24.10</td></tr><tr><td>b, Å</td><td>12.25 11.95</td><td>13.23 13.16</td><td>12.73 12.29</td><td>13.81 13.69</td></tr><tr><td>c, Å</td><td>29.19 28.96</td><td>25.32 24.55</td><td>20.60 20.53</td><td>18.13 17.56</td></tr><tr><td>β, deg.</td><td>92.80 92.58</td><td>102.02 100.87</td><td>95.29 93.33</td><td>111.01 110.39</td></tr><tr><td>V-L, Å (av.)</td><td>1.973 1.974</td><td>1.946 1.959</td><td>2.387 2.382</td><td>2.386 2.373</td></tr><tr><td>V=O, Å (av.)</td><td>1.614 1.640</td><td>− −</td><td>1.594 1.621</td><td>− −</td></tr></tbody></table>

where $n_{\alpha}=a^{\dagger}a$ is the phonon density operator, $a^{\dagger}$ and $a$ the creation and annihilation operators. In first approximation, assuming a weak coupling between the phonons bath and the spin degrees of freedom, the spin-phonon coupling Hamiltonian can be taken as linear in the ionic displacement

$$
\mathscr{H}_{\text{s-ph}}=\sum_{\alpha}\left(\frac{\partial \mathscr{H}_{\mathrm{s}}}{\partial q_{\alpha}}\right)_{0} q_{\alpha}.\qquad(5)
$$

The spin dynamics can then be described by the Redfield equations,[51] where the reduced spin density matrix, $\rho^{S}(t)$, evolves in time because of the interaction with phonons

$$
\frac{d \rho_{a a}^{\mathrm{S}}(t)}{d t}=\frac{2}{\hbar^{2}} \sum_{\alpha} \sum_{b} \mathscr{M}_{a b}^{\alpha} \rho_{b b}^{\mathrm{S}}(t),
$$

$$
\mathscr{M}_{a b}^{\alpha}=-\sum_{j} V_{a j}^{\alpha} V_{j b}^{\alpha} G\left(\omega_{j b}, \omega_{\alpha}\right)+\left|V_{a b}^{\alpha}\right|^{2} G\left(\omega_{b a}, \omega_{\alpha}\right), \quad(6)
$$

where $G(\omega_{ij},\omega_{\alpha})$ is the Fourier transform of the phonon correlation function and it is defined as

$$
G\left(\omega_{i j}, \omega_{\alpha}\right)=\delta\left(\omega_{i j}-\omega_{\alpha}\right) \bar{n}_{\alpha}+\delta\left(\omega_{i j}+\omega_{\alpha}\right)\left(\bar{n}_{\alpha}+1\right). \quad(7)
$$

Here $\bar{n}_{\alpha}=1 /(e^{\frac{\hbar \omega_{\alpha}}{k T}}-1)$ is the phonon occupation number, according to Bose-Einstein statistics, and $V_{a b}^{\alpha}=$ $\langle a|\frac{\partial \mathscr{H}_{\mathrm{s}}}{\partial q_{\alpha}}| b\rangle$ is the matrix element of the spin part of the spin-phonon coupling Hamiltonian, $\mathscr{H}_{\text{s-ph}}$, evaluated between two eigenfunctions, $|a\rangle$ and $|b\rangle$, of $\mathscr{H}_{\mathrm{s}}$. The approximations involved in this approach have been discussed elsewhere.[36] Understanding the interactions contributing to $V_{a b}^{\alpha}$ is the main focus of this work.

In order to understand the origin of the spin-phonon coupling is necessary to discuss the nature of the spin Hamiltonian that enters in Equation 5. The anisotropy of the spin Hamiltonian through the $\mathbf{g}$ tensor represents the fingerprint of the spin-lattice interaction, which is mediated by the presence of the spin-orbit coupling.[52, 53] Let us show explicitly the contribution of the $\mathbf{g}$ tensor to the spin-phonon coupling Hamiltonian

$$
\mathscr{H}_{\text{s-ph}}=\sum_{\alpha} \sum_{j r} \mu_{B} \hat{S}_{j} B_{r}\left(\frac{\partial g_{j r}}{\partial q_{\alpha}}\right)_{0} q_{\alpha}.\qquad(8)
$$

Estimating $\mathscr{H}_{\text{s-ph}}$ thus requires the calculation of the derivatives of $\mathbf{g}$ with respect to the structural perturbations and the calculation of the periodic crystal's normal modes.

### B. Structural and vibrational properties

The procedure outlined in the Computational Methods section has been employed for the 1-4 crystal structures, whose details are summarized in Table I and Figure S5 in the SI. The coordination geometries around the metal centres are square pyramidal, for the penta-coordinate compounds (1,3), and trigonally-distorted octahedral for the hexa-coordinate ones (2,4). It is worth noting that the metal-ligand (V-L) distances in sulphur-containing ligands are longer than those of the oxygen ones (Table I), consistent with the difference in atomic radius between O and S.

The starting point for understanding the effects of the first coordination shell on the spin-relaxation properties is the analysis of the crystal vibrations. One crystallographic cell (Γ-point approximation) is optimized and the Hessian matrix is calculated numerically. This gives $3N-3$ optical modes. Limiting our study to the Γ-point, the 3 acoustic modes have all $\omega_{\alpha}=0$.[44]

Experimental far-infrared (IR) THz spectroscopy as a function of temperature with a spectral window between 15 to $120 \mathrm{~cm}^{-1}$ is employed here to support the quality of our simulations for complexes 1-4 (see Fig. 2). The lowest temperature spectrum (10 K) shows an overall good agreement with our simulated spectra. A temperature

![](./images/867772188499903077_2.jpg)

FIG. 2. Experimental and simulated THz spectra for compounds 1-4. The former are measured at several temperatures between 10 and 300 K for powder-like samples embedded in polyethylene.

increase causes a red-shift of some vibrational modes be- cause of the presence of anharmonic interactions together with the softening of the crystal lattice. Simulations cor- responding to 0 K, indeed, show blue-shift with respect to the experimental lowest-temperature spectra. The first calculated vibrations occur at $13.3\ \mathrm{cm}^{-1}$ for 4 and 18.5 $\mathrm{cm}^{-1}$ for 3, while at $27.6\ \mathrm{cm}^{-1}$ for 2 and $20.7\ \mathrm{cm}^{-1}$ for 1. Dithiolene compounds show vibrations at lower frequen- cies with respect to the cathecolate ones, probably be- cause of the larger radius of first coordination sphere and the higher atomic weight of sulfur. Accordingly, longer bond lengths are generally associated to softer bonds and, therefore, to lower vibrational frequencies.

A deconvolution of the vibrational modes in molecu- lar translations, molecular rotations and intra-molecular motions, has been performed following the method out- lined in previous works,[44, 54] and the results are shown in Figure 3. The low-energy modes are dominated, for all compounds, by rigid translations and rotations of the molecule in the crystal, but internal contributions are also present and become the dominant ones on increasing the modes energy. The calculated decomposition shows, for hexa-coordinate compounds, an higher average in- ternal contribution. Among the hexa-coordinate, the cathecolate compound shows a reduced rotational con- tribution (see blue lines in Fig. 3).

### C. Spin-phonon coupling analysis
Table II shows the calculated and experimental $\mathbf{g}$- values. The deviation of $\mathbf{g}$ from the free electron value of 2.0023 is caused by the presence of spin-orbit coupling. In general, a good agreement between experimental and theory is observed and the trend in magnitude among the different molecules is correctly reproduced. Table II also reports the averaged molecular spin-phonon coupling co- efficients, as defined in the Computational Methods sec- tion. These parameters represent the sum of every atomic contribution to the spin-phonon coupling and allow us to define dynamical magneto-structural correlations. It should be noted that the differences in the average spin- phonon coupling across the series can be due to both the chemical nature of the ligand and the coordinating geometry around the metal centre. For complexes with the same ligand, the $\mathbf{g}$ tensor elements are less perturbed in the pyramidal coordination with respect to the octa- hedral one. When comparing complexes with the same coordination geometry but different ligands, it appears that a stronger effect on the spin-phonon coupling is ob- served, with the cathecolate being more prone to $\mathbf{g}$ tensor perturbations than the dithiolene ones.

![](./images/867772188499903077_3.jpg)

FIG. 3. The total molecular displacement associated to nor- mal modes with frequency in the range $0$–$150\ \mathrm{cm}^{-1}$ is decom- posed in intra-molecular motion (red), motion associated to molecular rotations (blue) and motion associated to molecular translations (yellow).

In order to explain these features it is important to correlate the $\mathbf{g}$-tensor anisotropy and how this is mod- ified by atomic displacements, i.e. $\mathbf{g}$ and $|\partial\mathbf{g}|$. These two quantities show the same trend across the series of molecules investigated as a consequence of a common mi- croscopic origin, namely the magnitude of orbital angu- lar momentum in the ground state.[55] This quantity, accessible from our ab initio calculations, can be conve- niently estimated from the magnitude of the 3d orbitals energy splitting,[55] showed in Figure 4 for the com- pounds 1-4. The first excited-state splitting, calculated by CASSCF+NEVPT2, shows a good correlation with both the $\mathbf{g}$ factors (Table II) and their derivatives, where

<table>
<caption>TABLE II. Best fit parameters extracted from simulation of the experimental CW-EPR X-band (ca. 9.7 GHz) spectra and CASSCF simulation results from optimized equilibrium geometry of 1-4.[28, 31]</caption>
<thead>
<tr>
<th>
</th>
<th>1
</th>
<th>2
</th>
<th>3
</th>
<th>4
</th></tr>
<tr>
<th>
</th>
<th>[VO(cat)₂]²⁻
</th>
<th>[V(cat)₃]²⁻
</th>
<th>[VO(dmit)₂]²⁻
</th>
<th>[V(dmit)₃]²⁻
</th></tr>
<tr>
<th colspan="5">Experimental Parameters (room T)
</th></tr></thead>
<tbody>
<tr>
<th>$g_x$
</th>
<td>1.980(1)
</td>
<td>1.945(1)
</td>
<td>1.986(1)
</td>
<td>1.961(1)
</td></tr>
<tr>
<th>$g_y$
</th>
<td>1.988(1)
</td>
<td>1.945(1)
</td>
<td>1.988(1)
</td>
<td>1.971(1)
</td></tr>
<tr>
<th>$g_z$
</th>
<td>1.956(1)
</td>
<td>1.989(2)
</td>
<td>1.970(1)
</td>
<td>1.985(1)
</td></tr>
<tr>
<th colspan="5">Simulated Parameters (0K)
</th></tr>
<tr>
<th>$g_x$
</th>
<td>1.978(1)
</td>
<td>1.906(1)
</td>
<td>1.987(1)
</td>
<td>1.943(1)
</td></tr>
<tr>
<th>$g_y$
</th>
<td>1.984(1)
</td>
<td>1.914(1)
</td>
<td>1.988(1)
</td>
<td>1.956(1)
</td></tr>
<tr>
<th>$g_z$
</th>
<td>1.935(1)
</td>
<td>1.997(1)
</td>
<td>1.953(1)
</td>
<td>1.997(1)
</td></tr>
<tr>
<th colspan="5">Average Spin-Phonon Coupling
</th></tr>
<tr>
<th>$|\partial \mathbf{g}|$
</th>
<td>1.5456
</td>
<td>6.1460
</td>
<td>0.3838
</td>
<td>2.5774
</td></tr></tbody>
</table>

larger $\mathbf{g}$-shifts and $\mathbf{g}$ derivatives correspond to smaller $\Delta E$. Interestingly, oxygen ligands yield a smaller splitting of the electronic states with respect to the sulphur ones.

![](./images/867772188499903077_4.jpg)

FIG. 4. CASSCF + NEVPT2 calculated energy ladder of the $3d$ valence shell of the four compounds analysed.

Although useful to understand general trends, the average spin-phonon coupling coefficients $|\partial \mathbf{g}|$ do not provide any information concerning the temperature at which specific atoms will start vibrating. This information can be obtained from the study of the spin-phonon coupling coefficients projected on the normal modes, as displayed in Figure 5a and 5b as a function of the phonons' vibrational frequency. The overall behaviour of the spin-phonon coupling follows the one observed for $|\partial \mathbf{g}|$, that is the strength of the coupling and ranks the molecules in the following order $\mathbf{3} < \mathbf{1} < \mathbf{4} < \mathbf{2}$. Thus, the spin-phonon coupling in vanadyl compounds is weaker than that in hexa-coordinated molecules. Furthermore, cathecolate ligands offer a stronger coupling than dithiolenes. The presence of different donor atoms has different effects on the low and high energy ranges of the vibrational spectrum. Indeed, dithiolene ligands, which exhibit a more diffuse coordination sphere due to the softer nature of S, show $i)$ the presence of several normal vibrations at lower frequencies, $ii)$ a weaker perturbation of the spin states by vibrational modes, as shown by the lower spin-phonon coupling amplitudes (see Table S1 in SI). The second effect is visible in the higher energy vibrations, suggesting a ligand dependence of $\tau$ vs. temperature.

![](./images/867772188499903077_5.jpg)

FIG. 5. Left panel: spin-phonon coupling coefficients in the 0-300 cm⁻¹ range for the four analysed compounds. A Gaussian line shape was applied to each harmonic normal mode, considering a width parameter equal to 2 cm⁻¹. Right panel: superposition of the first modes coupling coefficients with same Gaussian line broadening.

### IV. DISCUSSION

On the basis of the results obtained for the spin-orbit coupling projected onto the normal modes, it is now possible to draw some considerations regarding the experimental trends of the spin-lattice relaxation. Our methodology only includes the spin-phonon coupling originating from the modulation of the Zeeman energy by vibrations and, as discussed before, only the high-field regime can be considered. Figure 6a shows the field dependence of the relaxation time for the four compounds. This is characterized by a wide plateau at intermediate field values. We then fix the field at 1T and monitor the relaxation time as a function of temperature (Figure 6b). At this field the contribution to the relaxation coming from the hyperfine and dipolar interactions are expected to be reduced so that the spin-relaxation times can be correlated to our calculated spin-orbit coupling parameters.

Figures 6a and 6b show that at low temperature catecholate complexes relax slower than the dithiolene ones. This is consistent with the first vibrational modes structure of both compounds. Then, we note that molecules

![](./images/867772188499903077_6.jpg)

FIG. 6. Spin-lattice relaxation time extracted from AC sus- ceptometry measurements as a function of the external mag- netic field (left) and temperature (right) for compounds 1-4. Data have been taken by previous works.[28, 31]

presenting hexa-coordination relax faster than those with penta geometry, regardless of the chemical nature of the ligands.

Turning to the comparison of the relaxation time among iso-ligand species, we note that 2 relaxes faster than 1 in virtue of a much stronger spin-phonon cou- pling. This suggests that the spin-phonon coupling in- tensity and the structural rigidity, here assumed propor- tional to the frequency of the first $\Gamma$-point vibration, play together in determining the spin-lattice relaxation time.

This picture is confirmed by the behaviour of the relax- ation times when the temperature increases and higher energy modes become populated. The $\tau$ of molecule 3 de cays with temperature at a much slower pace than that of 1 and 2, and in fact there is a cross-over between the relaxation times of 2 and 3 at around 30 K, with another one between 1 and 3 expected at higher temper- atures. This experimental feature correlates well with the weak spin-phonon coupling observed over a wide fre- quency range for 3, when this is compared to that of 1 and 2.

Concerning compound 4, the AC susceptibility is mea- surable only in a quite limited temperature range, so that little conclusions can be drawn. However, previous pulsed electron paramagnetic resonance (EPR) investi- gations of crystalline compounds, diluted in diamagnetic analogues, have revealed that the coherence time of 4 col- lapses at $\sim$100 K as the result of a sharp decay of $T_1$ for temperatures above 30 K.[28] This observation correlates with the calculated spin-phonon coupling (Figure 5). In fact, spin-phonon couplings comparable between 3 and 4 are observed in the low-frequency range, while in the high-frequency one molecule 4 presents larger couplings. At high temperature, as the high-energy modes become more occupied, a significant enhancement of the spin- lattice relaxation in 4 is therefore expected. The ampli- tude of the calculated spin-phonon coefficients correlates with the measured temperature behaviours over a wide vibrational energy range, showing that the magnetiza- tion dynamics is determined by both the efficiency of the spin-phonon coupling as well as the vibrational density of states.

## V. OUTLOOK

The development of a rationale for the chemical design of new molecular qubits must proceed through the under- standing of the correlations between the spin-phonon dy- namics and the chemical identity of the molecular units. Our first-principles study of four different compounds made it possible to disentangle different contributions to the spin-phonon coupling and connect them to chemical features. The analysis of the derivatives of the $\boldsymbol{g}$ ten- sors highlights the importance of several factors, both intrinsic and extrinsic. The study of the molecular aver- aged spin-phonon coupling $|\partial \boldsymbol{g}|$ identifies the importance of intrinsic factors such as the efficiency of the spin-orbit coupling in the electronic ground-state. This quantity de- pends dramatically on structural features, such as the co- ordination geometry and the ligands field strength. The sensibility of the spin-phonon coupling on such structural features makes the design of new ligands, able to stabilize specific electronic ground states, a promising approach to new molecular qubits. From a theoretical perspec- tive our finding open the way to a systematic study of the connection between coordination geometry and lig- ands types with the spin-phonon coupling intensity. The correlation between structure and spin-phonon coupling is complex in nature and first-principles calculations are the only way to quantitatively unveil it. However, the average magnitude of the spin-phonon coupling has been found to correlate with experimentally accessible physi- cal quantities as the static g-shift and the energy of the first excited electronic state. This suggests an easy and qualitative way to experimentally assess the potential of a magnetic molecule to function as a qubit.

All these intrinsic factors must be optimized together with extrinsic factors, such as the composition and the energy of the phonons determined by the supramolecular arrangement. Such quantities do not only depends on the molecular features and include the effect of the retic- ular environment. The suppression of intra-molecular and rotational contributions to the vibrations at low en- ergy and the reduction of the phonon density of states in the same energy window has a remarkable effect on spin relaxation, as suggested by the behaviour of 2 at low temperature. The spin in this molecule, by virtue of a higher rigidity, relaxes slower than in 3 and 4 at low temperature, regardless of the higher spin-phonon coupling. This suggests that the role of extrinsic effects is strong enough to compensate large spin-phonon cou- plings. These extrinsic factors can be tuned following two possible strategies: by stiffening the metal-ligand bonds and by tayloring supramolecular structures where the

intra-molecular contribution to the normal modes is re-
duced and the phononic structure is modified and shifted
at higher frequencies.[56]

In conclusion, the results of our comparative first prin-
ciples investigation open new pathways for the rational
design of molecular qubits based on the combination of
the coordination geometry and ligang field with crystal
engineering.

# SUPPLEMENTARY MATERIAL

Supplementary materials contain the representation
of crystallographic cells, atomically projected cartesian
spin-phonon coupling coefficients, vibrational density of
states, fitting of spin-phonon coupling coefficients and list
of vibrational frequencies with the corresponding spin-
phonon coupling norm value.

# CONFLICTS OF INTEREST

There are no conflicts to declare.

# ACKNOWLEDGEMENTS

This work has been sponsored by Science Founda-
tion Ireland (grant 14/IA/2624), italian MIUR (through
Project QCNaMoS No. PRIN 2015-HYFSRT), MOL-
SPIN COST action CA15128 and by QuantERA Eu-
ropean Project SUMO. Computational resources were
provided by the Trinity Centre for High Performance
Computing (TCHPC) and the Irish Centre for High-End
Computing (ICHEC).

[1] A. Acín, Immanuel Bloch, Harry Buhrman, Tommaso
Calarco, Christopher Eichler, Jens Eisert, Daniel Es-
teve, Nicolas Gisin, Steffen J Glaser, Fedor Jelezko, Ste-
fan Kuhr, Maciej Lewenstein, Max F Riedel, Piet O
Schmidt, Rob Thew, Andreas Wallraff, Ian Walms-
ley, and Frank K Wilhelm, "The quantum technologies
roadmap: a European community view," New J. Phys.
20, 080201 (2018).

[2] M. H. Devoret and R. J. Schoelkopf, "Superconducting
circuits for quantum information: An outlook," Science,
Science 339, 1169-1174 (2013), arXiv:0402594 [cond-
mat].

[3] J. I. Cirac and P. Zoller, "Quantum computations with
cold trapped ions," Phys. Rev. Lett. 74, 4091-4094
(1995), arXiv:0305129 [quant-ph].

[4] M. Ringbauer, Exploring Quantum Foundations with Sin-
gle Photons (Springer-Verlag International, 2017) p. 20,
arXiv:1308.5688.

[5] J. J L Morton, Alexei M Tyryshkin, Richard M Brown,
Shyam Shankar, Brendon W Lovett, Arzhang Ardavan,
Thomas Schenkel, Eugene E Haller, Joel W Ager, and
S A Lyon, "Solid-state quantum memory using the 31P
nuclear spin," Nature 455, 1085 (2008).

[6] M. N. Leuenberger and D. Loss, "Quantum comput-
ing in molecular magnets," Nature 410, 789-793 (2001),
arXiv:0011415 [cond-mat].

[7] Riaz Hussain, Giuseppe Allodi, Alessandro Chiesa,
Elena Garlatti, Dmitri Mitcov, Andreas Konstantatos,
Kasper S. Pedersen, Roberto De Renzi, Stergios Piligkos,
and Stefano Carretta, "Coherent Manipulation of a
Molecular Ln-Based Nuclear Qudit Coupled to an Elec-
tron Qubit," J. Am. Chem. Soc. 140, 9814-9818 (2018).

[8] Matteo Atzori, Alessandro Chiesa, Elena Morra, Mario
Chiesa, Lorenzo Sorace, Stefano Carretta, and Roberta
Sessoli, "A two-qubit molecular architecture for electron-
mediated nuclear quantum simulation," Chem. Sci. 9,
6183-6192 (2018).

[9] R. Hanson and D. D. Awschalom, "Coherent manipu-
lation of single spins in semiconductors," Nature 453,
1043-1049 (2008).

[10] E.T. Bowyer, M.L.Y. Pang, B.N. Murdin, B.J. Vil-
lis, P.T. Greenland, Juerong Li, A.F.G. van der Meer,
B. Redlich, N. Stavrias, R. Gwilliam, G. Matmon, K.L.
Litvinenko, G. Aeppli, and C.R. Pidgeon, "Coherent cre-
ation and destruction of orbital wavepackets in Si:P with
electrical and optical read-out," Nat. Commun. 6, 6549
(2015).

[11] Y. S. Ding, Y. F. Deng, and Y. Z. Zheng, "The Rise of
Single-Ion Magnets as Spin Qubits," Magnetochemistry
2, 40 (2016).

[12] W. Harneit, "Spin Quantum Computing with Endohe-
dral Fullerenes," Phys. Rev. A 65, 032322 (2002).

[13] M. Warner, Salahud Din, Igor S. Tupitsyn, Gavin W.
Morley, A. Marshall Stoneham, Jules A. Gardener, Zhen-
lin Wu, Andrew J. Fisher, Sandrine Heutz, Christo-
pher W.M. Kay, and Gabriel Aeppli, "Potential for
spin-based information processing in a thin-film molec-
ular semiconductor," Nature 503, 504-508 (2013).

[14] Jesús Ferrando-Soria, Samantha A. Magee, Alessan-
dro Chiesa, Stefano Carretta, Paolo Santini, Iñigo J.
Vitorica-Yrezabal, Floriana Tuna, George F.S. White-
head, Stephen Sproules, Kyle M. Lancaster, Anne Laure
Barra, Grigore A. Timco, Eric J.L. McInnes, and
Richard E.P. Winpenny, "Switchable Interaction in
Molecular Double Qubits," Chem 1, 727-752 (2016).

[15] David Aguilà, Leoní A. Barrios, Verónica Velasco, Olivier
Roubeau, Ana Repollés, Pablo J. Alonso, Javier Sesé, Si-
mon J. Teat, Fernando Luis, and Guillem Aromí, "Het-
erodimetallic [LnLn'] lanthanide complexes: Toward a
chemical design of two-qubit molecular spin quantum
gates," J. Am. Chem. Soc. 136, 14215-14222 (2014).

[16] P. W. Shor, "Algorithms for quantum computation: dis-
crete logarithms and factoring," Proceedings 35th An-
nual Symposium on Foundations of Computer Science,
124-134 (1994), arXiv:9605043 [quant-ph].

[17] John Preskill, "Quantum computing and the entangle-
ment frontier," Rapporteur talk at the 25th Solvay Con-
ference on Physics , 1-18 (2012), arXiv:1203.5813.

[18] L. Tesi, Eva Lucaccini, Irene Cimatti, Mauro Perfetti,
Matteo Mannini, Matteo Atzori, Elena Morra, Mario

Chiesa, Andrea Caneschi, Lorenzo Sorace, and Roberta. Sessoli, "Quantum coherence in a processable vanadyl complex: new tools for the search of molecular spin qubits," Chem. Sci. 7, 2074-2083 (2016).

[19] A. Abragam and B. Bleaney, *Electron Paramagnetic Res- onance of Transition Ions* (Clarendon Press: Oxford, 1970) arXiv:arXiv:1011.1669v3.

[20] Joseph M Zadrozny, Jens Niklas, Oleg G Poluektov, and Danna E Freedman, "Multiple Quantum Coherences from Hyper fine Transitions in a Vanadium(IV) Com- plex," J. Am. Chem. Soc. 1, 488-492 (2015).

[21] Michael J. Graham, Joseph M. Zadrozny, Muhandis Shiddiq, John S. Anderson, Majed S. Fataftah, Stephen Hill, and Danna E. Freedman, "Influence of electronic spin and spin-orbit coupling on decoherence in mononu- clear transition metal complexes," J. Am. Chem. Soc. 136, 7623-7626 (2014).

[22] Joseph M. Zadrozny, Audrey T. Gallagher, T. David Har- ris, and Danna E. Freedman, "A Porous Array of Clock Qubits," J. Am. Chem. Soc. 139, 7089-7094 (2017).

[23] Miguel A. Andrés, Ignacio Gascón, Eva Natividad, Michel Goldmann, Olivier Roubeau, Pablo J. Alonso, and Ainhoa Urtizberea, "A Porphyrin Spin Qubit and Its 2D Framework Nanosheets," Ad. F. M. 28, 1801695 1-15 (2018).

[24] K. Bader, D. Dengler, S. Lenz, B. Endeward, S.D. Jiang, P. Neugebauer, and J. van Slageren, "Room temperature quantum coherence in a potential molecular qubit." Nat. Commun. 5, 5304 (2014).

[25] K. Bader, M. Winkler, and J. van Slageren, "Tuning of molecular qubits: Very long coherence and spin-lattice relaxation times," Chem. Comm. 52, 3623-3626 (2016).

[26] L. Tesi, A. Lunghi, M. Atzori, E. Lucaccini, L. Sorace, F. Totti, and R. Sessoli, "Giant spin-phonon bottleneck effects in evaporable vanadyl-based molecules with long spin coherence," Dalton Trans. 45, 16635-16643 (2016).

[27] M. Atzori, Lorenzo Tesi, Elena Morra, Mario Chiesa, Lorenzo Sorace, and Roberta Sessoli, "Room- Temperature Quantum Coherence and Rabi Oscillations in Vanadyl Phthalocyanine: Toward Multifunctional Molecular Spin Qubits," J. Am. Chem. Soc. 138, 2154-2157 (2016).

[28] M. Atzori, Elena Morra, Lorenzo Tesi, Andrea Al- bino, Mario Chiesa, Lorenzo Sorace, and Roberta Sessoli, "Quantum Coherence Times Enhancement in Vanadium(IV)-based Potential Molecular Qubits: the Key Role of the Vanadyl Moiety," J. Am. Chem. Soc. 138, 11234-11244 (2016).

[29] R. Sessoli, "Toward the Quantum Computer: MagneticMolecules Back in the Race," ACS Cent. Sci. 1, 473-474(2015).

[30] J. M. Zadrozny, J. Niklas, Oleg G. Poluektov, and D. E. Freedman, "Millisecond Coherence Time in a Tunable Molecular Electronic Spin Qubit," ACS Cent. Sci. 1, 488-492 (2015).

[31] M. Atzori, Stefano Benci, Elena Morra, Lorenzo Tesi, Mario Chiesa, Renato Torre, Lorenzo Sorace, and Roberta Sessoli, "Structural Effects on the Spin Dynam- ics of Potential Molecular Qubits," Inorg. Chem. , 731-740 (2017).

[32] J. C. Gill, "The establishment of thermal equilibrium in paramagnetic crystals," Reports on Progress in Physics38, 91-150 (1975).

[33] Matteo Atzori, Lorenzo Tesi, Stefano Benci, Alessandro Lunghi, Roberto Righini, Andrea Taschin, Renato Torre, Lorenzo Sorace, and Roberta Sessoli, "Spin Dynam- ics and Low Energy Vibrations: Insights from Vanadyl- Based Potential Molecular Qubits," J. Am. Chem. Soc. ,4338-4341 (2017).

[34] L. Escalera-Moreno, N Suaud, A. Gaita-Ariño, and E Coronado, "Determining Key Local Vibrations in the Relaxation of Molecular Spin Qubits and Single-Molecule Magnets," J. Phys. Chem. Lett. 8, 1695-1700 (2017).

[35] S. Cardona-Serra and A. Gaita-Ariño, "Vanadyl dithio- late single molecule transistors: The next spintronic fron- tier?" Dalton Trans. 47, 5533-5537 (2018).

[36] A. Lunghi, Federico Totti, Stefano Sanvito, and Roberta Sessoli, "Intra-molecular origin of the spin-phonon cou- pling in slow-relaxing molecular magnets," Chem. Sci. 8,6051-6059 (2017).

[37] A. Lunghi, Federico Totti, Roberta Sessoli, and Ste- fano Sanvito, "The role of anharmonic phonons in under- barrier spin relaxation of single molecule magnets," Nat. Commun. 8, 14620 (2017).

[38] J. VandeVondele, M. Krack, F. Mohamed, M. Parrinello, T. Chassaing, and J. Hutter, "QUICKSTEP: Fast and accurate density functional calculations using a mixed Gaussian and plane waves approach," Comput. Phys. Comm. 167, 103-128 (2005).

[39] J. Hutter, M. Iannuzzi, F. Schiffmann, and J. VandeVon- dele, "Cp2k: Atomistic simulations of condensed matter systems," WIREs Comput. Mol. Sci. 4, 15-25 (2014), arXiv:9512004 [mtrl-th].

[40] "Cp2k version 5.1. cp2k is freely available from," https://www.cp2k.org/.

[41] J. P. Perdew, "Jacob's ladder of density functional ap- proximations for the exchange-correlation energy," AIP Conference Proceedings 577, 1-20 (2001).

[42] J. P. Perdew, K. Burke, and M. Ernzerhof, "Generalized gradient approximation made simple," Phys. Rev. Lett.77, 3865 (1996).

[43] R. Sabatini, T. Gorni, and S. De Gironcoli, "Non- local van der Waals density functional made simple and efficient," Phys. Rev. B 87, 041108 1-4 (2013), arXiv:1009.1421.

[44] S. Califano, V. Schettino, and N. Neto, *Lattice Dynam- ics of Molecular Crystals* (Springer-Verlag, Berlin Hei- delberg, 1981).

[45] F. Neese and F. Wennmohs, "Orca 4.0 Manual," (2017).

[46] F. Neese, "Software update: the ORCA program system, version 4.0," WIREs Comput. Mol. Sci. 8, 1-6 (2018).

[47] J. Tasseva, A. Taschin, P. Bartolini, J. Striova, R. Fontana, and R. Torre, "Thin layered drawing me- dia probed by THz time-domain spectroscopy," Analyst142, 42-47 (2017), arXiv:1610.01025.

[48] Andrea Taschin, Paolo Bartolini, Jordanka Tasseva, and Renato Torre, "THz time-domain spectroscopic investi-gations of thin films," Measurement (Lond) 118, 282-288(2018), arXiv:arXiv:1703.06755v1.

[49] Stephen R Cooper, Yun Bai Koh, and Kenneth N Ray- mond, "Synthetic , Structural , and Physical Studiesof Bis( triethylammonium) Tris( catecholato)vanadate( IV), Potassium Bis( catecholato)oxovanadate( IV), and Potassium Tris( catecholato)vanadate(III)," J. Am. Chem. Soc. 104, 5092-5102 (1982).

[50] F. Petruccione and H.P. Breuer, *The Theory of Open Quantum System* (Oxford University Press, New York,

2002).

[51] A G Redfield, "On the Theory of Relaxation Processes," IBM journal , 19-31 (1957).

[52] D. Gatteschi, R. Sessoli, and J. Villain, *Molecular Nano- magnet* (Oxford University Press, Oxford, 2006).

[53] F. Neese and E. I. Solomon, "Calculation of Zero-Field Splittings, g-Values, and the Relativistic Nephelauxetic Effect in Transition Metal Complexes. Application to High-Spin Ferric Complexes," Inorg. Chem. **37**, 6568-6582 (1998).

[54] N. Neto and L. Bellucci, "A new algorithm for rigid body molecular dynamics," Chem. Phys. **328**, 259-268 (2006).

[55] A. Barry P. Lever and Edward I. Solomon, *Inor- ganic Electronic Structure and Spectroscopy, Methodol- ogy*, Vol. 1 (John Wiley & Sons., New Jersey, 1999) p. 32.

[56] Tsutomu Yamabayashi, Matteo Atzori, Lorenzo Tesi, Goulven Cosquer, Fabio Santanni, Marie Emmanuelle Boulon, Elena Morra, Stefano Benci, Renato Torre, Mario Chiesa, Lorenzo Sorace, Roberta Sessoli, and Masahiro Yamashita, "Scaling Up Electronic Spin Qubits into a Three-Dimensional Metal-Organic Framework," J. Am. Chem. Soc. **140**, 12090-12101 (2018).

# First-principles investigation of spin-phonon coupling in Vanadium-based molecular spin qubits

Andrea Albino$^{a}$, Stefano Benci$^{b}$, Lorenzo Tesi$^{a}$, Matteo Atzori$^{c}$, Renato Torre$^{b}$, Stefano Sanvito$^{d}$, Roberta Sessoli,$^{a*}$ and Alessandro Lunghi$^{d*}$

## Supporting Information

$^{a}$ Dipartimento di Chimica "Ugo Schiff" and INSTM RU, Università degli Studi di Firenze, I50019 Sesto Fiorentino, Italy, roberta.sessoli@unifi.it
$^{b}$ Dipartimento di Fisica ed Astronomia and European Laboratory for Nonlinear Spectroscopy, Università degli Studi di Firenze, I50019 Sesto Fiorentino, Italy
$^{c}$ Dipartimento di Chimica "Ugo Schiff" and INSTM RU, Università degli Studi di Firenze, I50019 Sesto Fiorentino, Italy. Present address: Laboratoire National des Champs Magnétiques Intenses, UPR 3228 - CNRS, F38042 Grenoble, France.
$^{d}$ School of Physics, CRANN and AMBER, Trinity College, Dublin 2, Ireland, lunghia@tcd.ie
1

Crystallographic cells

![](./images/867772188499903077_7.jpg)

1. $[PPh_4]_2[VO(cat)_2]$

![](./images/867772188499903077_8.jpg)

2. $[PPh_4]_2[V(cat)_3]$

![](./images/867772188499903077_9.jpg)

3. $[PPh_4]_2[VO(dmit)_2]$

![](./images/867772188499903077_10.jpg)

4. $[PPh_4]_2[V(dmit)_3]$

Figure S1 Left column: orthographic projections of the crystallographic cells. Right column: orthographic projections of asymmetric units (or unit cells) of the four analysed compounds. Tetraphenylphosphonium cations were drawn with thin lines for clarity.

### Mean square cartesian derivatives

Derivatives arising from the three degrees of freedom of one atom ($v$) and from each of the nine components of the $\mathbf{g}$-tensor ($jr$) have been summed together in single bars in the graph, according to the equation:

$$
\sum_{jrv}^{3} \left| \frac{\partial g_{jr}}{\partial X_{lv}} \right|^2 \tag{1}
$$

This is an evidence of different effects of geometric perturbations on the $l$-th atom of the four systems.

![](./images/867772188499903077_11.jpg)

Figure S2 $l$-th atom mean square cartesian derivatives of Landè factor. Only central atom and first coordination shell is shown for the 1-4 compounds. Here L stands either for O or S, see Figure 1 for labeling. The derivatives smaller than a fixed cutoff $(1 \times 10^{-4})$ were not considered in the graph.

Spin-Phonon coupling coefficients

![](./images/867772188499903077_12.jpg)

Figure S3 Spin-phonon coupling coefficients are defined as the first order derivatives of the spin Hamiltonian parameters with respect to the normal mode of vibrations $\partial g_{jr}/\partial X_{lv}$. The strategy we employed to compute them starts with the evaluation of the numerical $\boldsymbol{g}$ tensor derivatives with respect to the cartesian coordinates of compounds 1-2. The resulting points calculated have then been interpolated with a second order polynomial expression $(bx^2+ax+c=y)$ in order to estimate the linear terms, that correspond to the $\partial g_{jr}/\partial X_{lv}$ coefficients. Here we would like to report a few examples to show the details of the method. Graphs reports the scanning of the nine independent $g_{jr}$ elements along the $\alpha$-th degree of freedom, $x$.


![](./images/867772188499903077_13.jpg)

Figure S4 Spin-phonon coupling coefficients are defined as the first order derivatives of the spin Hamiltonian parameters with respect to the normal mode of vibrations $\partial g_{jr}/\partial X_{lv}$. The strategy we employed to compute them starts with the evaluation of the numerical $\boldsymbol{g}$ tensor derivatives with respect to the cartesian coordinates of compounds 3-4. The resulting points calculated have then been interpolated with a second order polynomial expression $(bx^2 + ax + c = y)$ in order to estimate the linear terms, that correspond to the $\partial g_{jr}/\partial X_{lv}$ coefficients. Here we would like to report a few examples to show the details of the method. Graphs reports the scanning of the nine independent $g_{jr}$ elements along the $\alpha$-th degree of freedom, $x$.

5

Density of states

![](./images/867772188499903077_14.jpg)
1. $[PPh_4]_2[VO(cat)_2]$

![](./images/867772188499903077_15.jpg)
2. $[PPh_4]_2[V(cat)_3]$

![](./images/867772188499903077_16.jpg)
3. $[PPh_4]_2[VO(dmit)_2]$

![](./images/867772188499903077_17.jpg)
4. $[PPh_4]_2[V(dmit)_3]$

Figure S5 DFT calculated Density of States (DOS). The red graph shows the sum of squared atomic normal modes coefficients of the whole crystallographic cell. The yellow graph shows the sum of squared atomic normal modes coefficients of the four molecules in the crystallographic cell, neglecting the counterions contribution. The blue graph shows the sum of squared atomic normal modes coefficients of the four vanadium atoms in the crystallographic cell. All the coefficients are referred to a non mass-weighted basis set. Normal modes characterized by vanadium atom coefficients are predominantly the low energy ones, as noticeable from the blue graphs.

# Low energy phononic structure and spin-phonon coupling coefficients

This analysis grounds on projection of the tensor norm, $\left|\frac{\partial g_{jr}}{\partial U_{lv}}\right|$ on the cell normal modes through the equation:

$$
\frac{\partial g_{jr}}{\partial q_{\alpha}} = \sum_{l=1}^{M} \sum_{v=1}^{3} \frac{\partial U_{lv}}{\partial q_{\alpha}} \frac{\partial g_{jr}}{\partial U_{lv}}
$$

, where the index $\alpha$ runs on $3N$ normal modes, $l$ on $M$ atoms of the single molecule, $v$ on the three spatial directions (x, y and z) and the couples $j,r$ fix the nine components of the $\mathbf{g}$-tensor. In the table $\frac{\partial \mathbf{g}}{\partial q_{\alpha}} = \sum_{jr} \left| \frac{\partial g_{jr}}{\partial q_{\alpha}} \right|^2$ and the modes corresponding to $\alpha=1,2,3$ have zero energy in $\Gamma$-point approximation.

Table S1 Calculated frequencies and spin-phonon coupling coefficients.

<table>
  <thead>
    <tr>
      <th colspan="3">1</th>
      <th colspan="3">2</th>
      <th colspan="3">3</th>
      <th colspan="3">4</th>
    </tr>
    <tr>
      <th colspan="3">[VO(cat)₂]²⁻</th>
      <th colspan="3">[V(cat)₃]²⁻</th>
      <th colspan="3">[VO(dmit)₂]²⁻</th>
      <th colspan="3">[V(dmit)₃]²⁻</th>
    </tr>
    <tr>
      <th>$\alpha$</th>
      <th>$\omega_{\alpha}$</th>
      <th>$\partial \mathbf{g}/\partial q_{\alpha}$</th>
      <th>$\omega_{\alpha}$</th>
      <th>$\partial \mathbf{g}/\partial q_{\alpha}$</th>
      <th>$\omega_{\alpha}$</th>
      <th>$\partial \mathbf{g}/\partial q_{\alpha}$</th>
      <th>$\omega_{\alpha}$</th>
      <th>$\partial \mathbf{g}/\partial q_{\alpha}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4</td>
      <td>20.644</td>
      <td>1.0232E-007</td>
      <td>27.588</td>
      <td>8.4269E-007</td>
      <td>18.463</td>
      <td>3.4499E-007</td>
      <td>13.292</td>
      <td>1.1974E-007</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21.351</td>
      <td>8.2370E-008</td>
      <td>28.176</td>
      <td>1.1060E-006</td>
      <td>19.836</td>
      <td>5.8242E-008</td>
      <td>15.658</td>
      <td>7.7764E-007</td>
    </tr>
    <tr>
      <td>6</td>
      <td>21.505</td>
      <td>8.8421E-008</td>
      <td>29.209</td>
      <td>5.5647E-007</td>
      <td>20.316</td>
      <td>2.3428E-008</td>
      <td>17.895</td>
      <td>1.5743E-007</td>
    </tr>
    <tr>
      <td>7</td>
      <td>22.084</td>
      <td>1.7291E-007</td>
      <td>29.965</td>
      <td>1.7908E-007</td>
      <td>20.541</td>
      <td>2.1337E-008</td>
      <td>20.696</td>
      <td>1.7171E-007</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28.053</td>
      <td>1.0491E-007</td>
      <td>30.669</td>
      <td>1.1924E-006</td>
      <td>25.496</td>
      <td>2.3707E-008</td>
      <td>21.313</td>
      <td>1.0559E-007</td>
    </tr>
    <tr>
      <td>9</td>
      <td>30.474</td>
      <td>7.4614E-008</td>
      <td>32.206</td>
      <td>1.5491E-007</td>
      <td>26.694</td>
      <td>3.0795E-007</td>
      <td>23.113</td>
      <td>8.4825E-008</td>
    </tr>
    <tr>
      <td>10</td>
      <td>32.853</td>
      <td>2.5674E-008</td>
      <td>33.744</td>
      <td>6.3687E-007</td>
      <td>27.099</td>
      <td>9.1979E-008</td>
      <td>25.473</td>
      <td>9.3823E-008</td>
    </tr>
    <tr>
      <td>11</td>
      <td>33.178</td>
      <td>6.6524E-008</td>
      <td>34.335</td>
      <td>6.8184E-007</td>
      <td>27.244</td>
      <td>1.0867E-007</td>
      <td>26.949</td>
      <td>8.6910E-008</td>
    </tr>
    <tr>
      <td>12</td>
      <td>35.909</td>
      <td>4.1882E-008</td>
      <td>34.377</td>
      <td>5.2532E-008</td>
      <td>29.350</td>
      <td>2.5773E-008</td>
      <td>26.999</td>
      <td>3.1285E-008</td>
    </tr>
    <tr>
      <td>13</td>
      <td>35.945</td>
      <td>1.7127E-007</td>
      <td>39.203</td>
      <td>2.7567E-007</td>
      <td>32.188</td>
      <td>4.6094E-008</td>
      <td>27.476</td>
      <td>1.0124E-007</td>
    </tr>
    <tr>
      <td>14</td>
      <td>39.314</td>
      <td>4.2565E-007</td>
      <td>39.457</td>
      <td>6.3363E-007</td>
      <td>32.599</td>
      <td>1.4789E-007</td>
      <td>29.162</td>
      <td>2.8372E-007</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39.493</td>
      <td>1.9057E-007</td>
      <td>40.530</td>
      <td>3.1455E-007</td>
      <td>32.939</td>
      <td>8.5301E-008</td>
      <td>29.289</td>
      <td>2.3960E-007</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39.942</td>
      <td>6.3083E-008</td>
      <td>41.382</td>
      <td>9.3644E-007</td>
      <td>33.386</td>
      <td>3.5222E-008</td>
      <td>30.086</td>
      <td>3.4832E-007</td>
    </tr>
    <tr>
      <td>17</td>
      <td>41.292</td>
      <td>2.0550E-007</td>
      <td>42.796</td>
      <td>2.6685E-008</td>
      <td>33.753</td>
      <td>7.0698E-008</td>
      <td>30.665</td>
      <td>3.6759E-007</td>
    </tr>
    <tr>
      <td>18</td>
      <td>42.617</td>
      <td>4.3496E-008</td>
      <td>42.931</td>
      <td>1.9223E-007</td>
      <td>33.964</td>
      <td>5.7179E-008</td>
      <td>30.840</td>
      <td>7.5535E-008</td>
    </tr>
    <tr>
      <td>19</td>
      <td>43.774</td>
      <td>9.1177E-008</td>
      <td>42.978</td>
      <td>5.2649E-007</td>
      <td>35.442</td>
      <td>1.0198E-007</td>
      <td>32.998</td>
      <td>3.2151E-007</td>
    </tr>
    <tr>
      <td>20</td>
      <td>44.954</td>
      <td>7.4093E-007</td>
      <td>43.630</td>
      <td>3.1546E-007</td>
      <td>36.214</td>
      <td>2.7939E-008</td>
      <td>35.252</td>
      <td>8.9736E-007</td>
    </tr>
    <tr>
      <td>21</td>
      <td>45.593</td>
      <td>2.0271E-007</td>
      <td>45.104</td>
      <td>1.5048E-006</td>
      <td>36.882</td>
      <td>1.0122E-007</td>
      <td>35.270</td>
      <td>3.7876E-008</td>
    </tr>
    <tr>
      <td>22</td>
      <td>47.079</td>
      <td>9.2674E-008</td>
      <td>45.113</td>
      <td>8.8613E-007</td>
      <td>38.130</td>
      <td>2.0633E-008</td>
      <td>36.449</td>
      <td>3.6949E-007</td>
    </tr>
    <tr>
      <td>23</td>
      <td>47.320</td>
      <td>1.4246E-007</td>
      <td>45.317</td>
      <td>5.8062E-007</td>
      <td>39.383</td>
      <td>3.3704E-008</td>
      <td>37.675</td>
      <td>1.1736E-007</td>
    </tr>
    <tr>
      <td>24</td>
      <td>48.050</td>
      <td>8.6148E-008</td>
      <td>46.939</td>
      <td>6.1140E-007</td>
      <td>39.550</td>
      <td>8.1955E-008</td>
      <td>38.316</td>
      <td>8.3939E-008</td>
    </tr>
    <tr>
      <td>25</td>
      <td>48.624</td>
      <td>1.1932E-007</td>
      <td>49.078</td>
      <td>1.1769E-006</td>
      <td>40.751</td>
      <td>4.4798E-009</td>
      <td>38.915</td>
      <td>8.4889E-008</td>
    </tr>
    <tr>
      <td>26</td>
      <td>49.569</td>
      <td>3.5097E-007</td>
      <td>50.823</td>
      <td>4.9824E-007</td>
      <td>41.132</td>
      <td>5.7073E-008</td>
      <td>39.226</td>
      <td>1.2293E-007</td>
    </tr>
    <tr>
      <td>27</td>
      <td>49.871</td>
      <td>1.0348E-007</td>
      <td>51.869</td>
      <td>2.5414E-007</td>
      <td>41.234</td>
      <td>2.7436E-008</td>
      <td>39.497</td>
      <td>1.2127E-007</td>
    </tr>
    <tr>
      <td>28</td>
      <td>50.894</td>
      <td>3.0711E-007</td>
      <td>52.226</td>
      <td>2.8533E-007</td>
      <td>41.837</td>
      <td>1.4060E-008</td>
      <td>40.445</td>
      <td>6.5701E-007</td>
    </tr>
    <tr>
      <td>29</td>
      <td>51.259</td>
      <td>3.5777E-008</td>
      <td>52.754</td>
      <td>9.1620E-008</td>
      <td>45.234</td>
      <td>1.7890E-007</td>
      <td>41.601</td>
      <td>1.0834E-007</td>
    </tr>
    <tr>
      <td>30</td>
      <td>51.598</td>
      <td>9.5083E-008</td>
      <td>53.725</td>
      <td>1.5898E-006</td>
      <td>45.572</td>
      <td>5.2361E-008</td>
      <td>42.548</td>
      <td>7.6473E-008</td>
    </tr>
    <tr>
      <td>31</td>
      <td>52.586</td>
      <td>4.8449E-007</td>
      <td>53.960</td>
      <td>5.0974E-007</td>
      <td>46.155</td>
      <td>7.1211E-008</td>
      <td>42.987</td>
      <td>6.0444E-008</td>
    </tr>
    <tr>
      <td>32</td>
      <td>54.262</td>
      <td>2.3026E-007</td>
      <td>54.089</td>
      <td>7.9394E-009</td>
      <td>47.078</td>
      <td>8.7693E-009</td>
      <td>44.026</td>
      <td>3.1953E-007</td>
    </tr>
    <tr>
      <td>33</td>
      <td>54.293</td>
      <td>2.0403E-007</td>
      <td>54.332</td>
      <td>5.1476E-007</td>
      <td>47.423</td>
      <td>1.3398E-007</td>
      <td>44.035</td>
      <td>9.6114E-008</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54.647</td>
      <td>1.2787E-008</td>
      <td>55.327</td>
      <td>1.9838E-007</td>
      <td>47.812</td>
      <td>4.8163E-008</td>
      <td>45.266</td>
      <td>1.9130E-007</td>
    </tr>
    <tr>
      <td>35</td>
      <td>54.750</td>
      <td>1.9265E-007</td>
      <td>56.541</td>
      <td>8.3599E-008</td>
      <td>48.547</td>
      <td>2.1446E-008</td>
      <td>45.559</td>
      <td>5.2075E-008</td>
    </tr>
    <tr>
      <td>36</td>
      <td>55.468</td>
      <td>3.3186E-007</td>
      <td>56.822</td>
      <td>7.5422E-007</td>
      <td>48.563</td>
      <td>5.9456E-008</td>
      <td>45.719</td>
      <td>7.9977E-008</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55.749</td>
      <td>5.0054E-008</td>
      <td>57.314</td>
      <td>6.5367E-008</td>
      <td>49.341</td>
      <td>4.6502E-008</td>
      <td>45.763</td>
      <td>2.7718E-007</td>
    </tr>
    <tr>
      <td>38</td>
      <td>56.312</td>
      <td>2.7093E-007</td>
      <td>57.383</td>
      <td>5.5030E-007</td>
      <td>49.558</td>
      <td>1.5423E-007</td>
      <td>46.878</td>
      <td>8.3255E-008</td>
    </tr>
    <tr>
      <td>39</td>
      <td>56.924</td>
      <td>8.6275E-007</td>
      <td>57.873</td>
      <td>6.7987E-008</td>
      <td>49.916</td>
      <td>6.2783E-008</td>
      <td>47.199</td>
      <td>1.0246E-007</td>
    </tr>
    <tr>
      <td>40</td>
      <td>58.435</td>
      <td>3.7144E-008</td>
      <td>58.318</td>
      <td>7.6302E-007</td>
      <td>50.661</td>
      <td>8.2048E-008</td>
      <td>49.071</td>
      <td>1.3661E-008</td>
    </tr>
    <tr>
      <td>41</td>
      <td>59.340</td>
      <td>6.9049E-008</td>
      <td>58.339</td>
      <td>3.7614E-007</td>
      <td>51.313</td>
      <td>3.4277E-008</td>
      <td>49.515</td>
      <td>3.7234E-007</td>
    </tr>
    <tr>
      <td>42</td>
      <td>60.059</td>
      <td>1.3516E-007</td>
      <td>59.615</td>
      <td>1.5316E-007</td>
      <td>51.538</td>
      <td>3.9523E-008</td>
      <td>50.004</td>
      <td>1.0452E-007</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60.336</td>
      <td>9.2068E-008</td>
      <td>61.103</td>
      <td>1.0967E-007</td>
      <td>52.037</td>
      <td>4.4071E-008</td>
      <td>50.101</td>
      <td>3.5223E-007</td>
    </tr>
    <tr>
      <td>44</td>
      <td>61.174</td>
      <td>4.6134E-008</td>
      <td>61.158</td>
      <td>1.6413E-008</td>
      <td>52.182</td>
      <td>6.9512E-008</td>
      <td>51.297</td>
      <td>9.0644E-008</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62.058</td>
      <td>1.4565E-007</td>
      <td>61.330</td>
      <td>1.3014E-007</td>
      <td>53.498</td>
      <td>5.9477E-008</td>
      <td>51.659</td>
      <td>5.3504E-008</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63.828</td>
      <td>4.5577E-008</td>
      <td>61.387</td>
      <td>2.3300E-007</td>
      <td>54.240</td>
      <td>4.9551E-009</td>
      <td>51.917</td>
      <td>1.5877E-007</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63.867</td>
      <td>1.3820E-007</td>
      <td>61.652</td>
      <td>1.1789E-007</td>
      <td>55.117</td>
      <td>1.8928E-008</td>
      <td>52.663</td>
      <td>2.706E-009</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65.252</td>
      <td>2.2432E-007</td>
      <td>63.457</td>
      <td>7.8931E-007</td>
      <td>55.445</td>
      <td>2.3713E-008</td>
      <td>53.134</td>
      <td>1.3853E-007</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65.345</td>
      <td>9.5963E-008</td>
      <td>63.747</td>
      <td>4.6314E-007</td>
      <td>55.807</td>
      <td>7.4976E-008</td>
      <td>54.201</td>
      <td>7.1690E-008</td>
    </tr>
    <tr>
      <td>50</td>
      <td>65.804</td>
      <td>7.9840E-008</td>
      <td>64.264</td>
      <td>5.3866E-007</td>
      <td>56.223</td>
      <td>1.8121E-008</td>
      <td>54.374</td>
      <td>6.1649E-008</td>
    </tr>
  </tbody>
</table>


Calculated frequencies and spin-phonon coupling coefficients - continued.

<table>
<thead>
<tr>
<th colspan="2">1</th>
<th colspan="2">2</th>
<th colspan="2">3</th>
<th colspan="2">4</th>
</tr>
<tr>
<th colspan="2">[VO(cat)₂]²⁻</th>
<th colspan="2">[V(cat)₃]²⁻</th>
<th colspan="2">[V(dmit)₂]²⁻</th>
<th colspan="2">[V(dmit)₃]²⁻</th>
</tr>
<tr>
<th>$\alpha$</th>
<th>$\omega_{\alpha}$</th>
<th>$\partial g/\partial q_{\alpha}$</th>
<th>$\omega_{\alpha}$</th>
<th>$\partial g/\partial q_{\alpha}$</th>
<th>$\omega_{\alpha}$</th>
<th>$\partial g/\partial q_{\alpha}$</th>
<th>$\omega_{\alpha}$</th>
<th>$\partial g/\partial q_{\alpha}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>51</td>
<td>66.360</td>
<td>7.7333E-007</td>
<td>65.471</td>
<td>2.5984E-007</td>
<td>56.693</td>
<td>6.6835E-008</td>
<td>55.415</td>
<td>1.0351E-007</td>
</tr>
<tr>
<td>52</td>
<td>66.621</td>
<td>1.8625E-007</td>
<td>65.728</td>
<td>3.2692E-007</td>
<td>57.180</td>
<td>2.7339E-008</td>
<td>55.759</td>
<td>5.8494E-008</td>
</tr>
<tr>
<td>53</td>
<td>66.773</td>
<td>2.1934E-007</td>
<td>65.885</td>
<td>5.1765E-007</td>
<td>57.942</td>
<td>6.6987E-008</td>
<td>56.151</td>
<td>4.9083E-007</td>
</tr>
<tr>
<td>54</td>
<td>70.332</td>
<td>1.4267E-007</td>
<td>67.536</td>
<td>4.8555E-007</td>
<td>58.346</td>
<td>9.2155E-008</td>
<td>56.425</td>
<td>1.4421E-007</td>
</tr>
<tr>
<td>55</td>
<td>70.720</td>
<td>3.1728E-007</td>
<td>67.996</td>
<td>1.9353E-007</td>
<td>59.201</td>
<td>5.1890E-008</td>
<td>56.550</td>
<td>5.2619E-007</td>
</tr>
<tr>
<td>56</td>
<td>71.163</td>
<td>5.6629E-007</td>
<td>68.461</td>
<td>4.1400E-007</td>
<td>59.621</td>
<td>1.3411E-007</td>
<td>57.706</td>
<td>5.3909E-008</td>
</tr>
<tr>
<td>57</td>
<td>71.255</td>
<td>4.6811E-008</td>
<td>69.150</td>
<td>1.5603E-008</td>
<td>60.010</td>
<td>2.6316E-009</td>
<td>59.093</td>
<td>4.4491E-008</td>
</tr>
<tr>
<td>58</td>
<td>71.533</td>
<td>2.6501E-007</td>
<td>70.902</td>
<td>1.7979E-007</td>
<td>60.291</td>
<td>1.3141E-007</td>
<td>59.898</td>
<td>2.5507E-007</td>
</tr>
<tr>
<td>59</td>
<td>72.077</td>
<td>9.0718E-008</td>
<td>70.997</td>
<td>1.2877E-006</td>
<td>60.669</td>
<td>1.3346E-008</td>
<td>60.487</td>
<td>6.6417E-008</td>
</tr>
<tr>
<td>60</td>
<td>72.246</td>
<td>8.7471E-008</td>
<td>71.656</td>
<td>1.5903E-007</td>
<td>61.243</td>
<td>4.4730E-008</td>
<td>60.606</td>
<td>1.3367E-007</td>
</tr>
<tr>
<td>61</td>
<td>72.349</td>
<td>1.2347E-007</td>
<td>72.262</td>
<td>7.2610E-007</td>
<td>61.506</td>
<td>5.5195E-008</td>
<td>60.997</td>
<td>5.1360E-009</td>
</tr>
<tr>
<td>62</td>
<td>73.018</td>
<td>3.4721E-008</td>
<td>72.603</td>
<td>5.4286E-008</td>
<td>62.131</td>
<td>1.6983E-007</td>
<td>62.558</td>
<td>9.3394E-009</td>
</tr>
<tr>
<td>63</td>
<td>73.606</td>
<td>5.0101E-007</td>
<td>73.908</td>
<td>4.5065E-007</td>
<td>62.550</td>
<td>1.3069E-008</td>
<td>62.719</td>
<td>7.3922E-008</td>
</tr>
<tr>
<td>64</td>
<td>74.377</td>
<td>2.1201E-007</td>
<td>74.272</td>
<td>3.7883E-007</td>
<td>62.779</td>
<td>3.9172E-009</td>
<td>62.772</td>
<td>2.3832E-008</td>
</tr>
<tr>
<td>65</td>
<td>75.436</td>
<td>2.1108E-007</td>
<td>74.522</td>
<td>1.9208E-007</td>
<td>62.995</td>
<td>3.5947E-009</td>
<td>63.071</td>
<td>2.0524E-007</td>
</tr>
<tr>
<td>66</td>
<td>75.772</td>
<td>1.6148E-007</td>
<td>75.235</td>
<td>2.5083E-007</td>
<td>64.303</td>
<td>3.1505E-008</td>
<td>63.765</td>
<td>8.3914E-009</td>
</tr>
<tr>
<td>67</td>
<td>77.351</td>
<td>1.2148E-007</td>
<td>75.576</td>
<td>1.1575E-006</td>
<td>65.329</td>
<td>1.3923E-008</td>
<td>65.060</td>
<td>3.6975E-007</td>
</tr>
<tr>
<td>68</td>
<td>78.699</td>
<td>1.2696E-007</td>
<td>75.651</td>
<td>8.6741E-007</td>
<td>66.030</td>
<td>2.4465E-008</td>
<td>65.164</td>
<td>6.2206E-008</td>
</tr>
<tr>
<td>69</td>
<td>79.185</td>
<td>6.9450E-008</td>
<td>75.798</td>
<td>3.3234E-007</td>
<td>66.562</td>
<td>1.6637E-008</td>
<td>65.650</td>
<td>1.6413E-007</td>
</tr>
<tr>
<td>70</td>
<td>80.644</td>
<td>2.1424E-007</td>
<td>75.830</td>
<td>5.0256E-007</td>
<td>66.817</td>
<td>1.5381E-007</td>
<td>66.020</td>
<td>1.3752E-007</td>
</tr>
<tr>
<td>71</td>
<td>81.029</td>
<td>2.6138E-008</td>
<td>76.733</td>
<td>1.0364E-006</td>
<td>68.486</td>
<td>4.1444E-009</td>
<td>66.795</td>
<td>2.4252E-007</td>
</tr>
<tr>
<td>72</td>
<td>81.334</td>
<td>1.1347E-007</td>
<td>79.888</td>
<td>4.2455E-007</td>
<td>69.074</td>
<td>5.7855E-008</td>
<td>67.665</td>
<td>1.3559E-008</td>
</tr>
<tr>
<td>73</td>
<td>81.911</td>
<td>7.4538E-008</td>
<td>80.108</td>
<td>6.2856E-007</td>
<td>69.214</td>
<td>2.7536E-008</td>
<td>68.011</td>
<td>3.0810E-008</td>
</tr>
<tr>
<td>74</td>
<td>83.115</td>
<td>9.4244E-008</td>
<td>81.909</td>
<td>5.1258E-008</td>
<td>70.550</td>
<td>4.8304E-008</td>
<td>68.157</td>
<td>6.4534E-008</td>
</tr>
<tr>
<td>75</td>
<td>83.461</td>
<td>1.5224E-007</td>
<td>82.824</td>
<td>1.2287E-006</td>
<td>70.775</td>
<td>1.4771E-008</td>
<td>69.210</td>
<td>1.3544E-007</td>
</tr>
<tr>
<td>76</td>
<td>83.683</td>
<td>5.8304E-008</td>
<td>83.356</td>
<td>4.8517E-007</td>
<td>71.490</td>
<td>7.7973E-008</td>
<td>70.418</td>
<td>5.9445E-008</td>
</tr>
<tr>
<td>77</td>
<td>84.426</td>
<td>5.7657E-008</td>
<td>85.626</td>
<td>2.4951E-007</td>
<td>72.531</td>
<td>5.9074E-009</td>
<td>70.527</td>
<td>1.5249E-008</td>
</tr>
<tr>
<td>78</td>
<td>85.218</td>
<td>3.9978E-008</td>
<td>87.486</td>
<td>2.9662E-007</td>
<td>73.208</td>
<td>5.8452E-008</td>
<td>71.680</td>
<td>4.6407E-008</td>
</tr>
<tr>
<td>79</td>
<td>86.004</td>
<td>4.5555E-008</td>
<td>87.721</td>
<td>2.3003E-006</td>
<td>73.255</td>
<td>2.7441E-008</td>
<td>72.650</td>
<td>3.0102E-007</td>
</tr>
<tr>
<td>80</td>
<td>86.432</td>
<td>6.1075E-008</td>
<td>87.949</td>
<td>1.2929E-008</td>
<td>73.701</td>
<td>3.1752E-008</td>
<td>73.410</td>
<td>4.0450E-008</td>
</tr>
<tr>
<td>81</td>
<td>86.588</td>
<td>1.3923E-007</td>
<td>89.665</td>
<td>1.9216E-006</td>
<td>76.181</td>
<td>9.0524E-009</td>
<td>73.585</td>
<td>2.6206E-007</td>
</tr>
<tr>
<td>82</td>
<td>87.064</td>
<td>8.8434E-008</td>
<td>90.577</td>
<td>3.6708E-007</td>
<td>76.632</td>
<td>1.1239E-007</td>
<td>73.770</td>
<td>7.4051E-008</td>
</tr>
<tr>
<td>83</td>
<td>87.517</td>
<td>9.6641E-008</td>
<td>90.807</td>
<td>1.0334E-007</td>
<td>77.112</td>
<td>1.5115E-008</td>
<td>75.165</td>
<td>6.8001E-007</td>
</tr>
<tr>
<td>84</td>
<td>90.382</td>
<td>8.3972E-008</td>
<td>91.905</td>
<td>6.2384E-008</td>
<td>78.229</td>
<td>8.4785E-009</td>
<td>75.323</td>
<td>8.7276E-008</td>
</tr>
<tr>
<td>85</td>
<td>91.466</td>
<td>8.7116E-008</td>
<td>92.319</td>
<td>2.5949E-007</td>
<td>78.527</td>
<td>9.3164E-008</td>
<td>77.367</td>
<td>3.8415E-007</td>
</tr>
<tr>
<td>86</td>
<td>92.208</td>
<td>6.6777E-008</td>
<td>92.600</td>
<td>8.0923E-008</td>
<td>79.665</td>
<td>9.6545E-009</td>
<td>77.613</td>
<td>1.6004E-007</td>
</tr>
<tr>
<td>87</td>
<td>92.925</td>
<td>1.0648E-007</td>
<td>93.196</td>
<td>1.6114E-006</td>
<td>81.112</td>
<td>5.9639E-008</td>
<td>78.422</td>
<td>2.8869E-008</td>
</tr>
<tr>
<td>88</td>
<td>93.198</td>
<td>2.5523E-008</td>
<td>94.917</td>
<td>1.7816E-006</td>
<td>81.125</td>
<td>1.3514E-008</td>
<td>79.187</td>
<td>5.4862E-008</td>
</tr>
<tr>
<td>89</td>
<td>94.084</td>
<td>6.8305E-008</td>
<td>95.190</td>
<td>7.5503E-008</td>
<td>81.416</td>
<td>2.5649E-008</td>
<td>80.094</td>
<td>1.1048E-007</td>
</tr>
<tr>
<td>90</td>
<td>94.798</td>
<td>5.5089E-008</td>
<td>95.826</td>
<td>5.4135E-008</td>
<td>82.313</td>
<td>4.9433E-008</td>
<td>80.417</td>
<td>5.2911E-008</td>
</tr>
<tr>
<td>91</td>
<td>94.860</td>
<td>2.2057E-008</td>
<td>96.139</td>
<td>1.4672E-006</td>
<td>82.619</td>
<td>4.3491E-008</td>
<td>80.742</td>
<td>2.5274E-007</td>
</tr>
<tr>
<td>92</td>
<td>96.581</td>
<td>1.2503E-008</td>
<td>97.048</td>
<td>5.2547E-007</td>
<td>82.708</td>
<td>2.1339E-008</td>
<td>80.977</td>
<td>2.5251E-007</td>
</tr>
<tr>
<td>93</td>
<td>97.048</td>
<td>8.2044E-009</td>
<td>97.439</td>
<td>6.3924E-008</td>
<td>83.640</td>
<td>1.8090E-007</td>
<td>81.412</td>
<td>1.7911E-007</td>
</tr>
<tr>
<td>94</td>
<td>97.202</td>
<td>1.0220E-007</td>
<td>98.831</td>
<td>2.8398E-007</td>
<td>84.402</td>
<td>5.8675E-008</td>
<td>81.510</td>
<td>3.4149E-007</td>
</tr>
<tr>
<td>95</td>
<td>98.365</td>
<td>2.7582E-007</td>
<td>98.879</td>
<td>3.4321E-007</td>
<td>85.240</td>
<td>8.3743E-009</td>
<td>81.782</td>
<td>3.1237E-007</td>
</tr>
<tr>
<td>96</td>
<td>99.205</td>
<td>1.2356E-007</td>
<td>100.47</td>
<td>9.9736E-008</td>
<td>86.840</td>
<td>2.7602E-007</td>
<td>82.667</td>
<td>3.8941E-007</td>
</tr>
<tr>
<td>97</td>
<td>100.04</td>
<td>3.0971E-007</td>
<td>101.51</td>
<td>1.8051E-007</td>
<td>87.098</td>
<td>3.9266E-010</td>
<td>83.564</td>
<td>6.6325E-008</td>
</tr>
<tr>
<td>98</td>
<td>103.06</td>
<td>1.5006E-007</td>
<td>101.83</td>
<td>2.1466E-007</td>
<td>87.390</td>
<td>4.6343E-008</td>
<td>83.614</td>
<td>5.1282E-007</td>
</tr>
<tr>
<td>99</td>
<td>103.31</td>
<td>5.0562E-007</td>
<td>102.16</td>
<td>4.7901E-008</td>
<td>87.886</td>
<td>8.2900E-009</td>
<td>84.055</td>
<td>2.3725E-007</td>
</tr>
<tr>
<td>100</td>
<td>103.91</td>
<td>5.1884E-007</td>
<td>104.21</td>
<td>1.8931E-007</td>
<td>89.387</td>
<td>1.1563E-008</td>
<td>84.170</td>
<td>2.8840E-007</td>
</tr>
<tr>
<td>101</td>
<td>106.19</td>
<td>1.0284E-007</td>
<td>104.42</td>
<td>7.1584E-008</td>
<td>89.672</td>
<td>3.4961E-008</td>
<td>84.856</td>
<td>1.7212E-007</td>
</tr>
<tr>
<td>102</td>
<td>106.58</td>
<td>2.2197E-007</td>
<td>105.07</td>
<td>5.2913E-008</td>
<td>91.280</td>
<td>2.0469E-008</td>
<td>85.459</td>
<td>1.5385E-007</td>
</tr>
<tr>
<td>103</td>
<td>106.77</td>
<td>6.9550E-007</td>
<td>105.18</td>
<td>1.0835E-007</td>
<td>91.586</td>
<td>2.8360E-008</td>
<td>85.641</td>
<td>9.9365E-008</td>
</tr>
<tr>
<td>104</td>
<td>107.92</td>
<td>9.0080E-008</td>
<td>107.10</td>
<td>1.1350E-007</td>
<td>91.835</td>
<td>7.4435E-010</td>
<td>85.885</td>
<td>7.3637E-008</td>
</tr><tr>
<td>105</td>
<td>108.40</td>
<td>1.1513E-007</td>
<td>107.62</td>
<td>3.9032E-008</td>
<td>92.571</td>
<td>2.9086E-008</td>
<td>86.120</td>
<td>8.1652E-008</td>
</tr>
<tr>
<td>106</td>
<td>108.48</td>
<td>4.3167E-007</td>
<td>109.42</td>
<td>3.9411E-007</td>
<td>92.742</td>
<td>1.2279E-008</td>
<td>86.591</td>
<td>2.2150E-007</td>
</tr>
<tr>
<td>107</td>
<td>111.15</td>
<td>1.0263E-007</td>
<td>110.33</td>
<td>5.7193E-008</td>
<td>92.899</td>
<td>6.4619E-009</td>
<td>87.079</td>
<td>1.6330E-007</td>
</tr>
<tr>
<td>108</td>
<td>111.84</td>
<td>1.8084E-007</td>
<td>111.47</td>
<td>4.7477E-007</td>
<td>93.135</td>
<td>4.7828E-009</td>
<td>87.842</td>
<td>1.7683E-007</td>
</tr>
<tr>
<td>109</td>
<td>111.86</td>
<td>6.1438E-008</td>
<td>114.06</td>
<td>1.1790E-008</td>
<td>94.189</td>
<td>1.7638E-008</td>
<td>88.488</td>
<td>1.6688E-007</td>
</tr>
<tr>
<td>110</td>
<td>112.55</td>
<td>1.7305E-008</td>
<td>114.81</td>
<td>1.4719E-007</td>
<td>95.102</td>
<td>1.1705E-007</td>
<td>89.748</td>
<td>4.1722E-007</td>
</tr>
</tbody>
</table>

8

Calculated frequencies and spin-phonon coupling coefficients - continued.

<table>
  <thead>
    <tr>
      <th colspan="3">1</th>
      <th colspan="2">2</th>
      <th colspan="2">3</th>
      <th colspan="2">4</th>
    </tr>
    <tr>
      <th colspan="3">[VO(cat)₂]²⁻</th>
      <th colspan="2">[V(cat)₃]²⁻</th>
      <th colspan="2">[V(dmit)₂]²⁻</th>
      <th colspan="2">[V(dmit)₃]²⁻</th>
    </tr>
    <tr>
      <th>$\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>111</td>
      <td>113.60</td>
      <td>1.1809E-008</td>
      <td>115.50</td>
      <td>3.7923E-007</td>
      <td>96.263</td>
      <td>2.9778E-009</td>
      <td>90.208</td>
      <td>2.1870E-007</td>
    </tr>
    <tr>
      <td>112</td>
      <td>114.31</td>
      <td>3.7626E-008</td>
      <td>116.76</td>
      <td>1.4461E-007</td>
      <td>96.426</td>
      <td>1.0980E-007</td>
      <td>91.794</td>
      <td>4.3050E-008</td>
    </tr>
    <tr>
      <td>113</td>
      <td>114.41</td>
      <td>1.6799E-007</td>
      <td>117.58</td>
      <td>2.3533E-007</td>
      <td>97.411</td>
      <td>2.2726E-008</td>
      <td>91.934</td>
      <td>4.0672E-008</td>
    </tr>
    <tr>
      <td>114</td>
      <td>115.93</td>
      <td>1.0846E-007</td>
      <td>117.97</td>
      <td>3.3514E-007</td>
      <td>97.864</td>
      <td>1.3013E-008</td>
      <td>92.068</td>
      <td>1.6760E-007</td>
    </tr>
    <tr>
      <td>115</td>
      <td>116.52</td>
      <td>4.2130E-008</td>
      <td>119.02</td>
      <td>1.8904E-007</td>
      <td>98.891</td>
      <td>3.9249E-008</td>
      <td>93.745</td>
      <td>3.3097E-007</td>
    </tr>
    <tr>
      <td>116</td>
      <td>117.30</td>
      <td>3.8520E-009</td>
      <td>119.49</td>
      <td>2.5784E-006</td>
      <td>99.141</td>
      <td>1.0598E-007</td>
      <td>94.499</td>
      <td>2.5405E-007</td>
    </tr>
    <tr>
      <td>117</td>
      <td>118.46</td>
      <td>2.3980E-007</td>
      <td>119.84</td>
      <td>8.6115E-007</td>
      <td>99.398</td>
      <td>1.8361E-008</td>
      <td>94.689</td>
      <td>7.7525E-008</td>
    </tr>
    <tr>
      <td>118</td>
      <td>118.66</td>
      <td>2.1480E-007</td>
      <td>121.04</td>
      <td>2.4371E-007</td>
      <td>101.04</td>
      <td>1.0469E-008</td>
      <td>96.255</td>
      <td>6.8783E-008</td>
    </tr>
    <tr>
      <td>119</td>
      <td>120.59</td>
      <td>9.3138E-008</td>
      <td>121.36</td>
      <td>3.9478E-008</td>
      <td>101.82</td>
      <td>2.4965E-008</td>
      <td>96.651</td>
      <td>1.6860E-007</td>
    </tr>
    <tr>
      <td>120</td>
      <td>121.18</td>
      <td>7.4830E-008</td>
      <td>121.42</td>
      <td>2.2927E-007</td>
      <td>103.61</td>
      <td>6.8211E-008</td>
      <td>96.900</td>
      <td>5.0700E-008</td>
    </tr>
    <tr>
      <td>121</td>
      <td>122.88</td>
      <td>9.8126E-008</td>
      <td>121.91</td>
      <td>7.2945E-007</td>
      <td>104.41</td>
      <td>6.4282E-008</td>
      <td>98.283</td>
      <td>2.1139E-007</td>
    </tr>
    <tr>
      <td>122</td>
      <td>122.94</td>
      <td>5.8954E-008</td>
      <td>123.38</td>
      <td>4.4736E-006</td>
      <td>104.64</td>
      <td>7.5097E-008</td>
      <td>99.400</td>
      <td>3.1874E-007</td>
    </tr>
    <tr>
      <td>123</td>
      <td>123.29</td>
      <td>5.5598E-009</td>
      <td>123.64</td>
      <td>9.9337E-007</td>
      <td>105.61</td>
      <td>7.5986E-009</td>
      <td>100.21</td>
      <td>4.1129E-008</td>
    </tr>
    <tr>
      <td>124</td>
      <td>123.71</td>
      <td>3.7085E-008</td>
      <td>124.30</td>
      <td>5.9850E-007</td>
      <td>106.53</td>
      <td>1.8958E-008</td>
      <td>100.59</td>
      <td>5.8462E-009</td>
    </tr>
    <tr>
      <td>125</td>
      <td>123.74</td>
      <td>5.1999E-009</td>
      <td>124.78</td>
      <td>1.1200E-006</td>
      <td>107.08</td>
      <td>8.2679E-008</td>
      <td>101.78</td>
      <td>1.2759E-007</td>
    </tr>
    <tr>
      <td>126</td>
      <td>124.72</td>
      <td>8.8733E-008</td>
      <td>125.54</td>
      <td>6.6397E-007</td>
      <td>107.31</td>
      <td>6.9508E-008</td>
      <td>102.16</td>
      <td>6.0187E-008</td>
    </tr>
    <tr>
      <td>127</td>
      <td>124.95</td>
      <td>4.5834E-008</td>
      <td>126.18</td>
      <td>2.1057E-006</td>
      <td>108.04</td>
      <td>4.3097E-008</td>
      <td>103.46</td>
      <td>9.2810E-008</td>
    </tr>
    <tr>
      <td>128</td>
      <td>125.12</td>
      <td>1.2335E-007</td>
      <td>127.15</td>
      <td>4.6565E-006</td>
      <td>108.70</td>
      <td>3.8089E-008</td>
      <td>105.10</td>
      <td>2.0548E-007</td>
    </tr>
    <tr>
      <td>129</td>
      <td>125.29</td>
      <td>1.4935E-007</td>
      <td>128.38</td>
      <td>7.6166E-008</td>
      <td>108.79</td>
      <td>1.3685E-008</td>
      <td>105.75</td>
      <td>5.3222E-007</td>
    </tr>
    <tr>
      <td>130</td>
      <td>127.35</td>
      <td>3.4954E-008</td>
      <td>129.47</td>
      <td>5.4811E-006</td>
      <td>109.62</td>
      <td>8.3487E-008</td>
      <td>106.25</td>
      <td>5.1617E-007</td>
    </tr>
    <tr>
      <td>131</td>
      <td>127.57</td>
      <td>1.2550E-008</td>
      <td>129.90</td>
      <td>4.3866E-006</td>
      <td>109.67</td>
      <td>2.4483E-009</td>
      <td>106.40</td>
      <td>4.2170E-008</td>
    </tr>
    <tr>
      <td>132</td>
      <td>130.10</td>
      <td>7.2201E-008</td>
      <td>130.80</td>
      <td>5.5172E-007</td>
      <td>110.67</td>
      <td>4.1187E-008</td>
      <td>106.85</td>
      <td>7.2209E-008</td>
    </tr>
    <tr>
      <td>133</td>
      <td>130.40</td>
      <td>3.6390E-008</td>
      <td>131.05</td>
      <td>2.9497E-007</td>
      <td>111.52</td>
      <td>1.2299E-007</td>
      <td>107.35</td>
      <td>1.7269E-007</td>
    </tr>
    <tr>
      <td>134</td>
      <td>130.65</td>
      <td>4.3801E-008</td>
      <td>132.06</td>
      <td>8.3939E-008</td>
      <td>112.44</td>
      <td>4.1733E-008</td>
      <td>107.74</td>
      <td>2.1562E-007</td>
    </tr>
    <tr>
      <td>135</td>
      <td>131.55</td>
      <td>1.1103E-008</td>
      <td>133.48</td>
      <td>4.7635E-007</td>
      <td>113.06</td>
      <td>1.2866E-007</td>
      <td>108.05</td>
      <td>4.5165E-007</td>
    </tr>
    <tr>
      <td>136</td>
      <td>131.82</td>
      <td>4.2597E-008</td>
      <td>134.85</td>
      <td>1.0144E-005</td>
      <td>114.89</td>
      <td>4.6956E-008</td>
      <td>109.34</td>
      <td>5.4245E-008</td>
    </tr>
    <tr>
      <td>137</td>
      <td>134.50</td>
      <td>3.4916E-007</td>
      <td>136.02</td>
      <td>1.9876E-006</td>
      <td>116.20</td>
      <td>1.1254E-007</td>
      <td>110.94</td>
      <td>1.3189E-007</td>
    </tr>
    <tr>
      <td>138</td>
      <td>134.78</td>
      <td>2.0070E-007</td>
      <td>136.68</td>
      <td>8.6785E-007</td>
      <td>116.50</td>
      <td>2.3064E-008</td>
      <td>111.13</td>
      <td>1.6893E-007</td>
    </tr>
    <tr>
      <td>139</td>
      <td>135.69</td>
      <td>1.7387E-007</td>
      <td>137.18</td>
      <td>6.6807E-007</td>
      <td>117.15</td>
      <td>3.4071E-009</td>

Calculated frequencies and spin-phonon coupling coefficients - continued.

<table>
  <thead>
    <tr>
      <th colspan="3">1</th>
      <th colspan="2">2</th>
      <th colspan="2">3</th>
      <th colspan="2">4</th>
    </tr>
    <tr>
      <th colspan="3">[VO(cat)₂]²⁻</th>
      <th colspan="2">[V(cat)₃]²⁻</th>
      <th colspan="2">[V(dmit)₂]²⁻</th>
      <th colspan="2">[V(dmit)₃]²⁻</th>
    </tr>
    <tr>
      <th>$\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
      <th>$\omega_\alpha$</th>
      <th>$\partial g/\partial q_\alpha$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>171</td>
      <td>191.98</td>
      <td>5.1027E-007</td>
      <td>178.69</td>
      <td>9.7211E-007</td>
      <td>143.10</td>
      <td>5.8712E-008</td>
      <td>134.41</td>
      <td>6.4160E-008</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192.20</td>
      <td>3.8716E-007</td>
      <td>188.48</td>
      <td>7.8091E-008</td>
      <td>144.96</td>
      <td>6.9888E-008</td>
      <td>135.21</td>
      <td>1.3043E-007</td>
    </tr>
    <tr>
      <td>173</td>
      <td>193.17</td>
      <td>3.5103E-008</td>
      <td>190.36</td>
      <td>2.1344E-006</td>
      <td>146.10</td>
      <td>1.7930E-008</td>
      <td>136.28</td>
      <td>2.1810E-007</td>
    </tr>
    <tr>
      <td>174</td>
      <td>193.38</td>
      <td>7.4840E-008</td>
      <td>190.91</td>
      <td>5.5303E-006</td>
      <td>147.06</td>
      <td>2.3262E-008</td>
      <td>136.63</td>
      <td>2.4052E-007</td>
    </tr>
    <tr>
      <td>175</td>
      <td>193.48</td>
      <td>1.5443E-007</td>
      <td>191.90</td>
      <td>7.5185E-006</td>
      <td>147.56</td>
      <td>3.5861E-008</td>
      <td>137.32</td>
      <td>1.7731E-007</td>
    </tr>
    <tr>
      <td>176</td>
      <td>193.49</td>
      <td>2.1065E-007</td>
      <td>193.42</td>
      <td>1.4246E-005</td>
      <td>148.00</td>
      <td>1.1144E-008</td>
      <td>137.39</td>
      <td>2.1430E-007</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197.38</td>
      <td>1.6283E-008</td>
      <td>193.78</td>
      <td>6.2724E-007</td>
      <td>153.84</td>
      <td>5.5581E-008</td>
      <td>137.92</td>
      <td>6.7053E-007</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197.70</td>
      <td>2.5433E-009</td>
      <td>194.01</td>
      <td>1.1373E-006</td>
      <td>155.13</td>
      <td>2.5856E-008</td>
      <td>139.12</td>
      <td>4.5381E-007</td>
    </tr>
    <tr>
      <td>179</td>
      <td>198.73</td>
      <td>1.0857E-007</td>
      <td>194.27</td>
      <td>9.7570E-006</td>
      <td>155.46</td>
      <td>3.9088E-008</td>
      <td>139.36</td>
      <td>9.0578E-007</td>
    </tr>
    <tr>
      <td>180</td>
      <td>198.75</td>
      <td>9.3293E-008</td>
      <td>194.97</td>
      <td>1.0148E-007</td>
      <td>155.60</td>
      <td>3.3183E-008</td>
      <td>139.60</td>
      <td>3.4031E-007</td>
    </tr>
    <tr>
      <td>181</td>
      <td>200.52</td>
      <td>1.9381E-008</td>
      <td>195.32</td>
      <td>4.6722E-006</td>
      <td>157.36</td>
      <td>9.2393E-008</td>
      <td>141.25</td>
      <td>2.1137E-007</td>
    </tr>
    <tr>
      <td>182</td>
      <td>200.66</td>
      <td>1.0080E-008</td>
      <td>197.22</td>
      <td>1.7334E-007</td>
      <td>157.37</td>
      <td>7.3836E-008</td>
      <td>142.69</td>
      <td>1.0022E-006</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202.67</td>
      <td>1.2041E-008</td>
      <td>197.39</td>
      <td>3.4150E-006</td>
      <td>158.31</td>
      <td>9.2318E-008</td>
      <td>142.77</td>
      <td>3.5083E-007</td>
    </tr>
    <tr>
      <td>184</td>
      <td>202.74</td>
      <td>2.8567E-008</td>
      <td>197.98</td>
      <td>8.5009E-006</td>
      <td>159.25</td>
      <td>7.9055E-008</td>
      <td>143.26</td>
      <td>1.4197E-006</td>
    </tr>
    <tr>
      <td>185</td>
      <td>204.07</td>
      <td>7.4868E-008</td>
      <td>198.51</td>
      <td>1.6287E-005</td>
      <td>171.69</td>
      <td>5.0183E-007</td>
      <td>144.27</td>
      <td>7.2880E-007</td>
    </tr>
    <tr>
      <td>186</td>
      <td>204.48</td>
      <td>6.5525E-008</td>
      <td>198.97</td>
      <td>7.7767E-006</td>
      <td>173.32</td>
      <td>5.1355E-007</td>
      <td>145.53</td>
      <td>1.9361E-007</td>
    </tr>
    <tr>
      <td>187</td>
      <td>205.00</td>
      <td>3.6891E-008</td>
      <td>203.93</td>
      <td>1.6880E-006</td>
      <td>174.26</td>
      <td>5.4860E-007</td>
      <td>145.96</td>
      <td>9.1894E-007</td>
    </tr>
    <tr>
      <td>188</td>
      <td>205.29</td>
      <td>4.5090E-008</td>
      <td>204.60</td>
      <td>2.3339E-006</td>
      <td>174.40</td>
      <td>5.6319E-007</td>
      <td>147.24</td>
      <td>7.9819E-007</td>
    </tr>
    <tr>
      <td>189</td>
      <td>210.39</td>
      <td>5.6369E-008</td>
      <td>204.90</td>
      <td>1.8237E-006</td>
      <td>183.46</td>
      <td>4.9002E-009</td>
      <td>147.35</td>
      <td>5.0586E-007</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210.60</td>
      <td>5.3326E-008</td>
      <td>205.71</td>
      <td>3.1339E-006</td>
      <td>184.59</td>
      <td>1.8819E-008</td>
      <td>149.50</td>
      <td>3.4954E-007</td>
    </tr>
    <tr>
      <td>191</td>
      <td>211.89</td>
      <td>2.9798E-008</td>
      <td>207.67</td>
      <td>1.1584E-005</td>
      <td>185.25</td>
      <td>6.9432E-008</td>
      <td>150.03</td>
      <td>1.9594E-007</td>
    </tr>
    <tr>
      <td>192</td>
      <td>212.34</td>
      <td>2.9970E-008</td>
      <td>207.90</td>
      <td>7.8781E-006</td>
      <td>186.47</td>
      <td>1.0517E-009</td>
      <td>150.71</td>
      <td>3.1720E-007</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213.69</td>
      <td>3.3714E-007</td>
      <td>208.54</td>
      <td>1.3504E-005</td>
      <td>186.55</td>
      <td>4.7237E-008</td>
      <td>151.13</td>
      <td>7.5874E-007</td>
    </tr>
    <tr>
      <td>194</td>
      <td>213.80</td>
      <td>3.6879E-007</td>
      <td>210.38</td>
      <td>5.9826E-006</td>
      <td>186.59</td>
      <td>4.5904E-008</td>
      <td>152.17</td>
      <td>7.9484E-007</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214.84</td>
      <td>2.5518E-007</td>
      <td>210.61</td>
      <td>7.3747E-006</td>
      <td>187.02</td>
      <td>1.6462E-008</td>
      <td>152.25</td>
      <td>3.4463E-007</td>
    </tr>
    <tr>
      <td>196</td>
      <td>215.38</td>
      <td>2.9090E-007</td>
      <td>212.28</td>
      <td>6.5471E-006</td>
      <td>187.31</td>
      <td>6.8642E-010</td>
      <td>153.98</td>
      <td>9.4851E-007</td>
    </tr>
    <tr>
      <td>197</td>
      <td>224.71</td>
      <td>1.9642E-006</td>
      <td>213.97</td>
      <td>2.7585E-006</td>
      <td>188.77</td>
      <td>2.9942E-008</td>
      <td>154.25</td>
      <td>1.0741E-006</td>
    </tr>
    <tr>
      <td>198</td>
      <td>224.77</td>
      <td>1.9668E-006</td>
      <td>215.21</td>
      <td>3.4914E-006</td>
      <td>190.04</td>
      <td>2.9170E-008</td>
      <td>154.90</td>
      <td>7.6544E-008</td>
    </tr>
    <tr>
      <td>199</td>
      <td>225.09</td>
      <td>2.0068E-006</td>
      <td>215.61</td>
      <td>3.5717E-007</td>
      <td>190.41</td>
      <td>4.1011E-008</td>
      <td>155.56</td>
      <td>1.0832E-006</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225.27</td>
      <td>1.9919E-006</td>
      <td>215.76</td>
      <td>2.9846E-006</td>
      <td>191.32</td>
      <td>6.6322E-007</td>
      <td>156.60</td>
      <td>5.3060E-007</td>
    </tr>
    <tr>
      <td>201</td>
      <td>240.81</td>
      <td>8.2396E-008</td>
      <td>215.79</td>
      <td>3.3112E-006</td>
      <td>191.36</td>
      <td>6.6010E-007</td>
      <td>156.95</td>
      <td>3.4819E-007</td>
    </tr>
    <tr>
      <td>202</td>
      <td>241.80</td>
      <td>8.2823E-008</td>
      <td>215.86</td>
      <td>1.0394E-006</td>
      <td>192.01</td>
      <td>5.1191E-007</td>
      <td>158.99</td>
      <td>9.9168E-007</td>
    </tr>
    <tr>
      <td>203</td>
      <td>241.84</td>
      <td>2.3065E-008</td>
      <td>216.19</td>
      <td>4.5315E-006</td>
      <td>192.04</td>
      <td>6.0659E-007</td>
      <td>159.02</td>
      <td>5.5241E-007</td>
    </tr>
    <tr>
      <td>204</td>
      <td>242.52</td>
      <td>4.1321E-008</td>
      <td>217.66</td>
      <td>1.1699E-006</td>
      <td>192.93</td>
      <td>2.8889E-007</td>
      <td>161.98</td>
      <td>3.4182E-007</td>
    </tr>
    <tr>
      <td>205</td>
      <td>244.37</td>
      <td>4.6104E-009</td>
      <td>218.26</td>
      <td>1.8572E-006</td>
      <td>194.49</td>
      <td>2.9199E-007</td>
      <td>162.01</td>
      <td>9.2527E-007</td>
    </tr>
    <tr>
      <td>206</td>
      <td>246.16</td>
      <td>3.2731E-008</td>
      <td>219.72</td>
      <td>2.0147E-006</td>
      <td>195.01</td>
      <td>2.3306E-007</td>
      <td>162.09</td>
      <td>8.4655E-007</td>
    </tr>
    <tr>
      <td>207</td>
      <td>248.82</td>
      <td>2.9591E-007</td>
      <td>220.24</td>
      <td>3.8227E-006</td>
      <td>195.19</td>
      <td>4.2549E-008</td>
      <td>164.99</td>
      <td>8.2764E-007</td>
    </tr>
    <tr>
      <td>208</td>
      <td>249.12</td>
      <td>3.1704E-007</td>
      <td>220.70</td>
      <td>1.9433E-006</td>
      <td>195.55</td>
      <td>2.1268E-007</td>
      <td>166.04</td>
      <td>6.4237E-007</td>
    </tr>
    <tr>
      <td>209</td>
      <td>249.76</td>
      <td>7.3280E-007</td>
      <td>228.66</td>
      <td>3.0349E-006</td>
      <td>195.84</td>
      <td>4.5571E-007</td>
      <td>166.87</td>
      <td>9.9949E-007</td>
    </tr>
    <tr>
      <td>210</td>
      <td>249.90</td>
      <td>7.1966E-007</td>
      <td>229.75</td>
      <td>3.6739E-006</td>
      <td>196.00</td>
      <td>3.6546E-007</td>
      <td>170.86</td>
      <td>1.5259E-007</td>
    </tr>
    <tr>
      <td>211</td>
      <td>250.33</td>
      <td>3.8932E-007</td>
      <td>230.32</td>
      <td>7.0557E-006</td>
      <td>196.87</td>
      <td>1.1579E-007</td>
      <td>171.20</td>
      <td>4.6035E-008</td>
    </tr>
    <tr>
      <td>212</td>
      <td>250.73</td>
      <td>4.1167E-007</td>
      <td>230.98</td>
      <td>2.4012E-007</td>
      <td>197.35</td>
      <td>6.0593E-007</td>
      <td>171.79</td>
      <td>7.1667E-007</td>
    </tr>
    <tr>
      <td>213</td>
      <td>253.77</td>
      <td>2.2905E-007</td>
      <td>232.61</td>
      <td>3.8977E-006</td>
      <td>197.56</td>
      <td>6.1675E-008</td>
      <td>174.71</td>
      <td>1.8749E-006</td>
    </tr>
    <tr>
      <td>214</td>
      <td>253.99</td>
      <td>4.0914E-008</td>
      <td>233.19</td>
      <td>4.1034E-006</td>
      <td>197.68</td>
      <td>2.9542E-010</td>
      <td>175.40</td>
      <td>1.1725E-006</td>
    </tr>
    <tr>
      <td>215</td>
      <td>254.18</td>
      <td>5.2875E-008</td>
      <td>234.62</td>
      <td>3.5977E-006</td>
      <td>198.89</td>
      <td>2.0454E-007</td>
      <td>175.57</td>
      <td>1.2033E-006</td>
    </tr>
    <tr>
      <td>216</td>
      <td>254.25</td>
      <td>1.9810E-007</td>
      <td>234.82</td>
      <td>3.2734E-006</td>
      <td>199.53</td>
      <td>3.3551E-008</td>
      <td>177.09</td>
      <td>1.5447E-006</td>
    </tr>
    <tr>
      <td>217</td>
      <td>256.29</td>
      <td>1.2556E-008</td>
      <td>241.72</td>
      <td>5.6143E-007</td>
      <td>200.22</td>
      <td>2.6547E-008</td>
      <td>183.37</td>
      <td>9.3929E-008</td>
    </tr>
    <tr>
      <td>218</td>
      <td>256.91</td>
      <td>2.6775E-008</td>
      <td>242.19</td>
      <td>2.1014E-007</td>
      <td>200.36</td>
      <td>3.0343E-009</td>
      <td>184.86</td>
      <td>3.5974E-008</td>
    </tr>
    <tr>
      <td>219</td>
      <td>257.38</td>
      <td>1.7291E-007</td>
      <td>243.02</td>
      <td>2.7904E-006</td>
      <td>200.93</td>
      <td>9.3171E-009</td>
      <td>186.54</td>
      <td>5.0202E-008</td>
    </tr>
    <tr>
      <td>220</td>
      <td>257.44</td>
      <td>1.7607E-007</td>
      <td>243.51</td>
      <td>9.7616E-007</td>
      <td>201.89</td>
      <td>2.2013E-008</td>
      <td>188.37</td>
      <td>5.7220E-008</td>
    </tr>
    <tr>
      <td>221</td>
      <td>258.67</td>
      <td>1.8369E-007</td>
      <td>243.60</td>
      <td>6.0704E-008</td>
      <td>238.54</td>
      <td>1.8075E-007</td>
      <td>191.62</td>
      <td>7.1535E-008</td>
    </tr>
    <tr>
      <td>222</td>
      <td>258.68</td>
      <td>1.4162E-007</td>
      <td>244.47</td>
      <td>4.6374E-006</td>
      <td>238.63</td>
      <td>1.0778E-007</td>
      <td>191.64</td>
      <td>5.9602E-009</td>
    </tr>
    <tr>
      <td>223</td>
      <td>259.50</td>
      <td>8.1225E-008</td>
      <td>244.56</td>
      <td>1.7448E-006</td>
      <td>240.68</td>
      <td>5.3495E-007</td>
      <td>191.71</td>
      <td>6.8937E-008</td>
    </tr>
    <tr>
      <td>224</td>
      <td>260.23</td>
      <td>8.0417E-008</td>
      <td>244.85</td>
      <td>2.7443E-006</td>
      <td>241.10</td>
      <td>6.6001E-007</td>
      <td>192.83</td>
      <td>8.9936E-008</td>
    </tr>
    <tr>
      <td>225</td>
      <td>261.39</td>
      <td>2.2709E-008</td>
      <td>245.49</td>
      <td>7.6219E-006</td>
      <td>241.18</td>
      <td>5.2565E-007</td>
      <td>193.92</td>
      <td>5.3117E-008</td>
    </tr>
    <tr>
      <td>226</td>
      <td>261.67</td>
      <td>2.4840E-008</td>
      <td>246.15</td>
      <td>1.1672E-005</td>
      <td>241.36</td>
      <td>5.4115E-007</td>
      <td>194.83</td>
      <td>2.1631E-008</td>
    </tr>
    <tr>
      <td>227</td>
      <td>261.91</td>
      <td>4.7062E-008</td>
      <td>247.49</td>
      <td>6.8944E-006</td>
      <td>242.00</td>
      <td>2.4276E-008</td>
      <td>195.17</td>
      <td>9.8798E-009</td>
    </tr>
    <tr>
      <td>228</td>
      <td>262.44</td>
      <td>4.1428E-009</td>
      <td>247.63</td>
      <td>6.8983E-006</td>
      <td>242.32</td>
      <td>5.0445E-008</td>
      <td>195.25</td>
      <td>4.4480E-008</td>
    </tr>
    <tr>
      <td>229</td>
      <td>262.72</td>
      <td>9.1651E-009</td>
      <td>250.69</td>
      <td>7.8885E-006</td>
      <td>243.29</td>
      <td>8.8984E-009</td>
      <td>195.35</td>
      <td>3.2451E-008</td>
    </tr>
    <tr>
      <td>230</td>
      <td>263.84</td>
      <td>4.9713E-008</td>
      <td>251.02</td>
      <td>7.7284E-007</td>
      <td>243.47</td>
      <td>1.9803E-008</td>
      <td>196.08</td>
      <td>8.2544E-008</td>
    </tr>
  </tbody>
</table>

10

Calculated frequencies and spin-phonon coupling coefficients - continued.

<table>
<thead>
<tr>
<th></th>
<th colspan="3">1<br>$\left[\text{VO(cat)}_2\right]^{2-}$</th>
<th colspan="3">2<br>$\left[\text{V(cat)}_3\right]^{2-}$</th>
<th colspan="3">3<br>$\left[\text{V(dmit)}_2\right]^{2-}$</th>
<th colspan="3">4<br>$\left[\text{V(dmit)}_3\right]^{2-}$</th>
</tr>
<tr>
<th>$\alpha$</th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th></th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th></th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th></th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
</tr>
</thead>
<tbody>
<tr>
<td>231</td>
<td>263.88</td>
<td>1.6685E-008</td>
<td></td>
<td>251.42</td>
<td>2.2277E-008</td>
<td></td>
<td>244.38</td>
<td>5.7762E-008</td>
<td></td>
<td>196.15</td>
<td>2.6179E-008</td>
</tr>
<tr>
<td>232</td>
<td>263.96</td>
<td>4.3072E-009</td>
<td></td>
<td>251.88</td>
<td>3.0495E-006</td>
<td></td>
<td>244.46</td>
<td>8.0996E-008</td>
<td></td>
<td>196.52</td>
<td>4.4193E-008</td>
</tr>
<tr>
<td>233</td>
<td>264.91</td>
<td>7.2602E-008</td>
<td></td>
<td>251.97</td>
<td>1.7743E-006</td>
<td></td>
<td>245.44</td>
<td>3.0421E-008</td>
<td></td>
<td>197.87</td>
<td>1.0086E-008</td>
</tr>
<tr>
<td>234</td>
<td>264.92</td>
<td>3.2670E-008</td>
<td></td>
<td>252.59</td>
<td>1.8240E-007</td>
<td></td>
<td>245.69</td>
<td>2.1594E-008</td>
<td></td>
<td>198.14</td>
<td>1.1862E-007</td>
</tr>
<tr>
<td>235</td>
<td>266.16</td>
<td>3.2434E-008</td>
<td></td>
<td>252.86</td>
<td>8.5685E-009</td>
<td></td>
<td>246.12</td>
<td>4.8374E-008</td>
<td></td>
<td>198.27</td>
<td>1.0119E-008</td>
</tr>
<tr>
<td>236</td>
<td>266.72</td>
<td>4.7487E-009</td>
<td></td>
<td>253.58</td>
<td>3.9226E-007</td>
<td></td>
<td>246.14</td>
<td>7.4376E-009</td>
<td></td>
<td>199.76</td>
<td>4.5887E-008</td>
</tr>
<tr>
<td>237</td>
<td>271.24</td>
<td>3.4938E-007</td>
<td></td>
<td>253.94</td>
<td>7.3693E-008</td>
<td></td>
<td>246.72</td>
<td>7.6149E-010</td>
<td></td>
<td>204.45</td>
<td>1.6502E-008</td>
</tr>
<tr>
<td>238</td>
<td>271.24</td>
<td>3.6055E-007</td>
<td></td>
<td>255.23</td>
<td>2.7174E-007</td>
<td></td>
<td>246.94</td>
<td>1.3805E-007</td>
<td></td>
<td>205.73</td>
<td>8.7199E-008</td>
</tr>
<tr>
<td>239</td>
<td>271.36</td>
<td>3.6086E-007</td>
<td></td>
<td>255.30</td>
<td>1.8803E-006</td>
<td></td>
<td>247.31</td>
<td>5.2186E-008</td>
<td></td>
<td>208.08</td>
<td>1.8731E-008</td>
</tr>
<tr>
<td>240</td>
<td>271.86</td>
<td>3.2774E-007</td>
<td></td>
<td>255.91</td>
<td>8.9943E-007</td>
<td></td>
<td>247.57</td>
<td>2.9305E-008</td>
<td></td>
<td>208.36</td>
<td>5.2308E-008</td>
</tr>
<tr>
<td>241</td>
<td>275.08</td>
<td>2.3280E-007</td>
<td></td>
<td>256.10</td>
<td>6.6696E-006</td>
<td></td>
<td>247.57</td>
<td>7.3042E-010</td>
<td></td>
<td>211.51</td>
<td>1.4888E-008</td>
</tr>
<tr>
<td>242</td>
<td>275.11</td>
<td>2.1776E-007</td>
<td></td>
<td>256.57</td>
<td>9.8427E-007</td>
<td></td>
<td>247.95</td>
<td>3.0840E-008</td>
<td></td>
<td>212.68</td>
<td>8.1302E-009</td>
</tr>
<tr>
<td>243</td>
<td>276.85</td>
<td>3.8949E-007</td>
<td></td>
<td>257.17</td>
<td>1.4990E-006</td>
<td></td>
<td>247.99</td>
<td>3.2773E-008</td>
<td></td>
<td>213.88</td>
<td>1.0559E-008</td>
</tr>
<tr>
<td>244</td>
<td>277.26</td>
<td>3.8791E-007</td>
<td></td>
<td>257.29</td>
<td>3.3981E-007</td>
<td></td>
<td>248.25</td>
<td>2.8349E-009</td>
<td></td>
<td>213.92</td>
<td>5.1461E-009</td>
</tr>
<tr>
<td>245</td>
<td>279.83</td>
<td>4.8297E-008</td>
<td></td>
<td>262.62</td>
<td>2.8130E-007</td>
<td></td>
<td>254.78</td>
<td>1.6226E-008</td>
<td></td>
<td>227.97</td>
<td>8.4154E-008</td>
</tr>
<tr>
<td>246</td>
<td>280.31</td>
<td>7.9446E-008</td>
<td></td>
<td>262.86</td>
<td>6.9088E-007</td>
<td></td>
<td>255.09</td>
<td>1.7983E-008</td>
<td></td>
<td>228.61</td>
<td>2.4206E-007</td>
</tr>
<tr>
<td>247</td>
<td>280.34</td>
<td>3.7135E-008</td>
<td></td>
<td>263.72</td>
<td>1.6051E-007</td>
<td></td>
<td>255.75</td>
<td>1.4088E-009</td>
<td></td>
<td>229.39</td>
<td>3.4078E-008</td>
</tr>
<tr>
<td>248</td>
<td>280.49</td>
<td>7.0714E-008</td>
<td></td>
<td>263.97</td>
<td>2.1567E-007</td>
<td></td>
<td>256.13</td>
<td>2.1532E-008</td>
<td></td>
<td>229.74</td>
<td>2.2690E-007</td>
</tr>
<tr>
<td>249</td>
<td>281.17</td>
<td>6.9719E-007</td>
<td></td>
<td>265.35</td>
<td>6.1549E-008</td>
<td></td>
<td>256.22</td>
<td>1.6813E-008</td>
<td></td>
<td>230.64</td>
<td>2.1732E-007</td>
</tr>
<tr>
<td>250</td>
<td>281.33</td>
<td>6.2095E-007</td>
<td></td>
<td>265.62</td>
<td>8.1056E-009</td>
<td></td>
<td>257.60</td>
<td>3.2737E-009</td>
<td></td>
<td>231.11</td>
<td>3.6046E-007</td>
</tr>
<tr>
<td>251</td>
<td>282.04</td>
<td>6.9302E-007</td>
<td></td>
<td>265.86</td>
<td>1.5758E-007</td>
<td></td>
<td>257.96</td>
<td>6.8931E-010</td>
<td></td>
<td>231.30</td>
<td>3.2681E-007</td>
</tr>
<tr>
<td>252</td>
<td>282.67</td>
<td>8.2543E-007</td>
<td></td>
<td>266.37</td>
<td>2.9375E-008</td>
<td></td>
<td>258.03</td>
<td>3.9636E-009</td>
<td></td>
<td>231.35</td>
<td>1.9211E-007</td>
</tr>
<tr>
<td>253</td>
<td>287.64</td>
<td>1.5612E-008</td>
<td></td>
<td>266.99</td>
<td>6.8812E-007</td>
<td></td>
<td>258.17</td>
<td>4.8463E-009</td>
<td></td>
<td>233.56</td>
<td>3.4049E-007</td>
</tr>
<tr>
<td>254</td>
<td>287.77</td>
<td>1.2599E-007</td>
<td></td>
<td>267.31</td>
<td>1.2426E-007</td>
<td></td>
<td>258.39</td>
<td>4.1436E-010</td>
<td></td>
<td>234.11</td>
<td>3.6399E-007</td>
</tr>
<tr>
<td>255</td>
<td>288.43</td>
<td>4.8708E-008</td>
<td></td>
<td>267.53</td>
<td>8.2087E-009</td>
<td></td>
<td>258.53</td>
<td>1.6700E-009</td>
<td></td>
<td>235.07</td>
<td>3.0707E-007</td>
</tr>
<tr>
<td>256</td>
<td>288.75</td>
<td>1.8501E-008</td>
<td></td>
<td>267.55</td>
<td>1.9774E-008</td>
<td></td>
<td>259.04</td>
<td>1.2927E-008</td>
<td></td>
<td>236.35</td>
<td>2.9367E-007</td>
</tr>
<tr>
<td>257</td>
<td>292.48</td>
<td>1.7712E-008</td>
<td></td>
<td>268.47</td>
<td>8.5795E-008</td>
<td></td>
<td>259.32</td>
<td>8.1486E-011</td>
<td></td>
<td>238.96</td>
<td>2.1996E-008</td>
</tr>
<tr>
<td>258</td>
<td>292.52</td>
<td>1.9020E-008</td>
<td></td>
<td>268.57</td>
<td>3.4090E-007</td>
<td></td>
<td>259.74</td>
<td>2.2842E-009</td>
<td></td>
<td>240.30</td>
<td>1.0955E-008</td>
</tr>
<tr>
<td>259</td>
<td>292.78</td>
<td>3.6965E-008</td>
<td></td>
<td>268.68</td>
<td>2.5389E-007</td>
<td></td>
<td>259.93</td>
<td>4.8110E-009</td>
<td></td>
<td>242.60</td>
<td>4.8192E-008</td>
</tr>
<tr>
<td>260</td>
<td>293.06</td>
<td>6.4495E-008</td>
<td></td>
<td>269.30</td>
<td>5.7865E-008</td>
<td></td>
<td>260.23</td>
<td>7.9404E-010</td>
<td></td>
<td>244.26</td>
<td>5.6077E-008</td>
</tr>
<tr>
<td>261</td>
<td>329.86</td>
<td>2.7928E-007</td>
<td></td>
<td>274.18</td>
<td>2.1318E-007</td>
<td></td>
<td>260.26</td>
<td>6.2693E-009</td>
<td></td>
<td>249.83</td>
<td>1.1872E-006</td>
</tr>
<tr>
<td>262</td>
<td>329.92</td>
<td>2.8298E-007</td>
<td></td>
<td>274.23</td>
<td>3.3341E-008</td>
<td></td>
<td>260.64</td>
<td>1.3531E-008</td>
<td></td>
<td>250.06</td>
<td>1.2695E-006</td>
</tr>
<tr>
<td>263</td>
<td>329.96</td>
<td>2.7815E-007</td>
<td></td>
<td>274.60</td>
<td>3.1373E-008</td>
<td></td>
<td>260.82</td>
<td>1.4831E-009</td>
<td></td>
<td>250.74</td>
<td>1.1573E-006</td>
</tr>
<tr>
<td>264</td>
<td>330.04</td>
<td>2.8294E-007</td>
<td></td>
<td>275.67</td>
<td>3.4051E-007</td>
<td></td>
<td>261.68</td>
<td>4.0306E-009</td>
<td></td>
<td>250.94</td>
<td>4.1308E-006</td>
</tr>
<tr>
<td>265</td>
<td>345.93</td>
<td>7.1460E-007</td>
<td></td>
<td>276.13</td>
<td>3.9288E-009</td>
<td></td>
<td>266.79</td>
<td>4.6512E-009</td>
<td></td>
<td>253.07</td>
<td>2.6612E-007</td>
</tr>
<tr>
<td>266</td>
<td>345.96</td>
<td>7.0947E-007</td>
<td></td>
<td>276.79</td>
<td>2.6629E-007</td>
<td></td>
<td>267.60</td>
<td>1.8068E-009</td>
<td></td>
<td>253.25</td>
<td>2.4102E-007</td>
</tr>
<tr>
<td>267</td>
<td>346.02</td>
<td>7.0084E-007</td>
<td></td>
<td>276.82</td>
<td>9.7962E-009</td>
<td></td>
<td>268.30</td>
<td>1.0538E-008</td>
<td></td>
<td>253.40</td>
<td>2.1782E-007</td>
</tr>
<tr>
<td>268</td>
<td>346.12</td>
<td>7.0089E-007</td>
<td></td>
<td>277.38</td>
<td>1.0839E-008</td>
<td></td>
<td>268.64</td>
<td>5.0423E-010</td>
<td></td>
<td>253.68</td>
<td>1.5026E-007</td>
</tr>
<tr>
<td>269</td>
<td>366.88</td>
<td>9.3382E-007</td>
<td></td>
<td>277.75</td>
<td>2.1118E-009</td>
<td></td>
<td>269.18</td>
<td>7.8565E-010</td>
<td></td>
<td>254.20</td>
<td>1.4559E-007</td>
</tr>
<tr>
<td>270</td>
<td>367.32</td>
<td>9.3576E-007</td>
<td></td>
<td>286.21</td>
<td>1.5891E-007</td>
<td></td>
<td>269.31</td>
<td>1.5366E-009</td>
<td></td>
<td>254.97</td>
<td>9.2662E-007</td>
</tr>
<tr>
<td>271</td>
<td>367.85</td>
<td>9.2835E-007</td>
<td></td>
<td>286.51</td>
<td>1.l0124E-007</td>
<td></td>
<td>270.46</td>
<td>2.5453E-009</td>
<td></td>
<td>254.98</td>
<td>5.7108E-007</td>
</tr>
<tr>
<td>272</td>
<td>367.90</td>
<td>9.3357E-007</td>
<td></td>
<td>287.39</td>
<td>7.2101E-008</td>
<td></td>
<td>270.75</td>
<td>3.1261E-009</td>
<td></td>
<td>255.43</td>
<td>.68547E-007</td>
</tr>
<tr>
<td>273</td>
<td>386.66</td>
<td>6.6103E-009</td>
<td></td>
<td>287.76</td>
<td>1.4342E-008</td>
<td></td>
<td>271.95</td>
<td>4.3536E-008</td>
<td></td>
<td>255.43</td>
<td>9.3919E-007</td>
</tr>
<tr>
<td>274</td>
<td>386.66</td>
<td>6.3600E-009</td>
<td></td>
<td>288.56</td>
<td>1.9836E-007</td>
<td></td>
<td>272.08</td>
<td>4.5560E-008</td>
<td></td>
<td>255.48</td>
<td>7.8432E-007</td>
</tr>
<tr>
<td>275</td>
<td>386.82</td>
<td>2.4200E-009</td>
<td></td>
<td>288.64</td>
<td>1.4658E-007</td>
<td></td>
<td>272.54</td>
<td>2.7847E-008</td>
<td></td>
<td>255.57</td>
<td>1.5127E-006</td>
</tr>
<tr>
<td>276</td>
<td>386.84</td>
<td>3.6613E-009</td>
<td></td>
<td>290.12</td>
<td>6.3410E-008</td>
<td></td>
<td>272.76</td>
<td>3.7627E-008</td>
<td></td>
<td>256.08</td>
<td>3.2037E-008</td>
</tr>
<tr>
<td>277</td>
<td>387.97</td>
<td>1.8677E-009</td>
<td></td>
<td>290.48</td>
<td>5.8046E-009</td>
<td></td>
<td>287.52</td>
<td>4.3717E-008</td>
<td></td>
<td>256.43</td>
<td>1.2728E-007</td>
</tr>
<tr>
<td>278</td>
<td>388.11</td>
<td>1.9326E-009</td>
<td></td>
<td>298.84</td>
<td>1.0202E-008</td>
<td></td>
<td>287.64</td>
<td>1.8765E-009</td>
<td></td>
<td>257.19</td>
<td>1.4175E-007</td>
</tr>
<tr>
<td>279</td>
<td>388.26</td>
<td>4.2620E-009</td>
<td></td>
<td>303.45</td>
<td>6.2593E-010</td>
<td></td>
<td>287.92</td>
<td>1.3081E-008</td>
<td></td>
<td>257.75</td>
<td>5.2238E-007</td>
</tr>
<tr>
<td>280</td>
<td>388.39</td>
<td>2.8464E-009</td>
<td></td>
<td>320.83</td>
<td>4.1497E-006</td>
<td></td>
<td>287.98</td>
<td>2.7041E-009</td>
<td></td>
<td>258.45</td>
<td>6.8391E-008</td>
</tr>
<tr>
<td>281</td>
<td>391.57</td>
<td>1.0680E-009</td>
<td></td>
<td>322.32</td>
<td>3.2779E-006</td>
<td></td>
<td>288.25</td>
<td>3.7877E-009</td>
<td></td>
<td>258.49</td>
<td>1.0607E-008</td>
</tr>
<tr>
<td>282</td>
<td>391.80</td>
<td>2.2883E-009</td>
<td></td>
<td>328.25</td>
<td>1.3896E-008</td>
<td></td>
<td>288.44</td>
<td>2.4528E-008</td>
<td></td>
<td>259.34</td>
<td>5.1027E-008</td>
</tr>
<tr>
<td>283</td>
<td>391.86</td>
<td>3.0748E-008</td>
<td></td>
<td>331.01</td>
<td>9.8498E-006</td>
<td></td>
<td>288.63</td>
<td>5.0703E-010</td>
<td></td>
<td>260.32</td>
<td>7.5671E-008</td>
</tr>
<tr>
<td>284</td>
<td>392.04</td>
<td>2.8284E-008</td>
<td></td>
<td>331.45</td>
<td>1.1154E-005</td>
<td></td>
<td>288.70</td>
<td>3.5557E-010</td>
<td></td>
<td>260.39</td>
<td>3.6588E-008</td>
</tr>
<tr>
<td>285</td>
<td>392.86</td>
<td>5.7008E-009</td>
<td></td>
<td>331.45</td>
<td>2.2037E-005</td>
<td></td>
<td>289.54</td>
<td>2.5647E-008</td>
<td></td>
<td>261.10</td>
<td>5.3493E-008</td>
</tr>
<tr>
<td>286</td>
<td>393.21</td>
<td>1.5620E-008</td>
<td></td>
<td>335.37</td>
<td>1.9940E-005</td>
<td></td>
<td>289.85</td>
<td>1.6632E-008</td>
<td></td>
<td>261.35</td>
<td>8.9406E-008</td>
</tr>
<tr>
<td>287</td>
<td>393.37</td>
<td>4.4897E-008</td>
<td></td>
<td>336.17</td>
<td>1.7194E-007</td>
<td></td>
<td>290.42</td>
<td>3.0090E-009</td>
<td></td>
<td>261.60</td>
<td>3.0801E-007</td>
</tr>
<tr>
<td>288</td>
<td>393.49</td>
<td>6.2764E-008</td>
<td></td>
<td>337.56</td>
<td>1.9272E-009</td>
<td></td>
<td>290.51</td>
<td>6.4828E-009</td>
<td></td>
<td>261.93</td>
<td>4.9173E-008</td>
</tr>
<tr>
<td>289</td>
<td>393.81</td>
<td>1.6158E-008</td>
<td></td>
<td>340.08</td>
<td>1.8906E-009</td>
<td></td>
<td>291.71</td>
<td>1.3461E-007</td>
<td></td>
<td>261.97</td>
<td>4.2707E-007</td>
</tr>
<tr>
<td>290</td>
<td>393.87</td>
<td>8.0449E-009</td>
<td></td>
<td>349.09</td>
<td>3.9168E-010</td>
<td></td>
<td>291.73</td>
<td>1.1278E-007</td>
<td></td>
<td>262.25</td>
<td>2.3761E-009</td>
</tr>
</tbody>
</table>

11

Calculated frequencies and spin-phonon coupling coefficients - continued.

<table>
<thead>
<tr>
<th colspan="3">1<br>[VO(cat)₂]²⁻</th>
<th colspan="2">2<br>[V(cat)₃]²⁻</th>
<th colspan="2">3<br>[VO(dmit)₂]²⁻</th>
<th colspan="2">4<br>[V(dmit)₃]²⁻</th>
</tr>
<tr>
<th>$\alpha$</th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
<th>$\omega_\alpha$</th>
<th>$\partial g/\partial q_\alpha$</th>
</tr>
</thead>
<tbody>
<tr>
<td>291</td>
<td>394.99</td>
<td>1.8826E-009</td>
<td>352.94</td>
<td>3.4144E-008</td>
<td>292.05</td>
<td>1.1396E-007</td>
<td>262.71</td>
<td>8.3423E-008</td>
</tr>
<tr>
<td>292</td>
<td>395.02</td>
<td>2.7115E-009</td>
<td>360.62</td>
<td>1.9746E-006</td>
<td>292.90</td>
<td>1.1072E-007</td>
<td>263.22</td>
<td>2.8865E-008</td>
</tr>
<tr>
<td>293</td>
<td>398.97</td>
<td>7.1517E-010</td>
<td>361.92</td>
<td>1.6501E-006</td>
<td>321.51</td>
<td>1.2392E-007</td>
<td>263.39</td>
<td>4.3057E-007</td>
</tr>
<tr>
<td>294</td>
<td>399.10</td>
<td>2.9424E-010</td>
<td>385.22</td>
<td>1.4070E-007</td>
<td>321.63</td>
<td>9.9861E-008</td>
<td>263.94</td>
<td>4.6892E-007</td>
</tr>
<tr>
<td>295</td>
<td>399.12</td>
<td>2.0646E-009</td>
<td>386.21</td>
<td>2.5579E-009</td>
<td>321.68</td>
<td>2.1451E-007</td>
<td>264.21</td>
<td>1.2473E-007</td>
</tr>
<tr>
<td>296</td>
<td>399.52</td>
<td>2.1152E-009</td>
<td>386.89</td>
<td>5.1078E-008</td>
<td>321.80</td>
<td>2.1361E-007</td>
<td>264.79</td>
<td>9.4583E-008</td>
</tr>
<tr>
<td>297</td>
<td>406.53</td>
<td>4.6229E-007</td>
<td>387.05</td>
<td>9.0680E-008</td>
<td>322.38</td>
<td>1.6842E-007</td>
<td>266.98</td>
<td>1.6420E-008</td>
</tr>
<tr>
<td>298</td>
<td>406.64</td>
<td>7.3818E-007</td>
<td>387.42</td>
<td>1.1577E-008</td>
<td>322.50</td>
<td>1.9508E-007</td>
<td>267.66</td>
<td>3.7313E-008</td>
</tr>
<tr>
<td>299</td>
<td>406.81</td>
<td>6.1140E-007</td>
<td>387.66</td>
<td>9.0464E-009</td>
<td>323.22</td>
<td>7.4303E-008</td>
<td>268.00</td>
<td>1.7615E-008</td>
</tr>
<tr>
<td>300</td>
<td>406.92</td>
<td>7.6441E-007</td>
<td>388.44</td>
<td>1.2779E-007</td>
<td>323.32</td>
<td>7.2305E-008</td>
<td>268.11</td>
<td>1.9330E-009</td>
</tr>
<tr>
<td>301</td>
<td>407.75</td>
<td>1.2410E-007</td>
<td>388.83</td>
<td>1.7950E-008</td>
<td>327.38</td>
<td>1.4749E-007</td>
<td>269.03</td>
<td>2.9241E-008</td>
</tr>
<tr>
<td>302</td>
<td>408.49</td>
<td>2.8759E-007</td>
<td>389.32</td>
<td>1.5605E-009</td>
<td>328.15</td>
<td>1.4237E-007</td>
<td>269.05</td>
<td>1.5038E-008</td>
</tr>
<tr>
<td>303</td>
<td>409.45</td>
<td>4.0014E-009</td>
<td>390.14</td>
<td>1.5073E-008</td>
<td>328.82</td>
<td>1.4439E-007</td>
<td>269.45</td>
<td>3.5371E-008</td>
</tr>
<tr>
<td>304</td>
<td>409.68</td>
<td>1.0381E-008</td>
<td>391.23</td>
<td>1.5746E-008</td>
<td>330.47</td>
<td>1.4171E-007</td>
<td>271.36</td>
<td>2.8361E-008</td>
</tr>
<tr>
<td>305</td>
<td>413.14</td>
<td>4.5750E-009</td>
<td>391.61</td>
<td>1.8808E-008</td>
<td>353.93</td>
<td>5.5707E-008</td>
<td>274.41</td>
<td>8.4533E-008</td>
</tr>
<tr>
<td>306</td>
<td>413.77</td>
<td>3.1952E-009</td>
<td>394.75</td>
<td>3.6652E-008</td>
<td>353.95</td>
<td>5.5348E-008</td>
<td>274.68</td>
<td>7.3827E-008</td>
</tr>
<tr>
<td>307</td>
<td>414.18</td>
<td>1.5696E-009</td>
<td>394.81</td>
<td>1.7944E-009</td>
<td>354.48</td>
<td>5.7394E-008</td>
<td>274.83</td>
<td>1.5120E-007</td>
</tr>
<tr>
<td>308</td>
<td>414.65</td>
<td>5.5673E-009</td>
<td>394.95</td>
<td>2.3468E-008</td>
<td>354.52</td>
<td>5.9667E-008</td>
<td>274.95</td>
<td>1.0778E-007</td>
</tr>
<tr>
<td>309</td>
<td>426.85</td>
<td>1.3436E-009</td>
<td>395.07</td>
<td>2.5746E-008</td>
<td>376.47</td>
<td>2.0625E-007</td>
<td>276.49</td>
<td>2.8044E-008</td>
</tr>
<tr>
<td>310</td>
<td>426.88</td>
<td>5.3541E-010</td>
<td>396.07</td>
<td>1.9000E-009</td>
<td>376.57</td>
<td>1.9343E-007</td>
<td>277.03</td>
<td>1.6389E-008</td>
</tr>
<tr>
<td>311</td>
<td>427.51</td>
<td>5.6715E-010</td>
<td>399.77</td>
<td>1.5210E-008</td>
<td>377.00</td>
<td>1.8867E-007</td>
<td>277.39</td>
<td>3.2679E-008</td>
</tr>
<tr>
<td>312</td>
<td>427.58</td>
<td>6.6787E-010</td>
<td>399.84</td>
<td>3.1999E-007</td>
<td>377.05</td>
<td>1.9995E-007</td>
<td>278.75</td>
<td>1.5631E-008</td>
</tr>
<tr>
<td>313</td>
<td>428.75</td>
<td>1.4411E-008</td>
<td>400.37</td>
<td>6.9648E-008</td>
<td>383.33</td>
<td>1.1296E-007</td>
<td>279.89</td>
<td>3.7612E-007</td>
</tr>
<tr>
<td>314</td>
<td>428.99</td>
<td>1.0311E-009</td>
<td>400.69</td>
<td>2.0309E-008</td>
<td>383.61</td>
<td>1.0042E-007</td>
<td>280.30</td>
<td>3.8848E-007</td>
</tr>
<tr>
<td>315</td>
<td>429.34</td>
<td>9.4996E-009</td>
<td>400.94</td>
<td>2.7034E-007</td>
<td>383.70</td>
<td>9.6314E-008</td>
<td>280.90</td>
<td>3.1385E-007</td>
</tr>
<tr>
<td>316</td>
<td>429.40</td>
<td>9.5756E-010</td>
<td>401.90</td>
<td>1.8213E-009</td>
<td>384.13</td>
<td>1.1637E-007</td>
<td>281.37</td>
<td>3.0747E-007</td>
</tr>
<tr>
<td>317</td>
<td>434.66</td>
<td>1.5688E-009</td>
<td>402.21</td>
<td>2.3178E-008</td>
<td>387.51</td>
<td>3.9726E-008</td>
<td>291.80</td>
<td>6.9059E-009</td>
</tr>
<tr>
<td>318</td>
<td>434.82</td>
<td>3.2561E-009</td>
<td>402.77</td>
<td>7.1457E-008</td>
<td>387.62</td>
<td>3.8856E-008</td>
<td>292.08</td>
<td>2.0994E-009</td>
</tr>
<tr>
<td>319</td>
<td>434.90</td>
<td>4.8442E-010</td>
<td>403.38</td>
<td>6.6511E-007</td>
<td>388.34</td>
<td>3.7795E-008</td>
<td>293.33</td>
<td>7.4716E-009</td>
</tr>
<tr>
<td>320</td>
<td>434.95</td>
<td>6.4826E-010</td>
<td>403.86</td>
<td>5.2060E-007</td>
<td>388.41</td>
<td>3.6935E-008</td>
<td>293.63</td>
<td>2.0487E-008</td>
</tr>
<tr>
<td>321</td>
<td>438.66</td>
<td>6.1907E-011</td>
<td>403.92</td>
<td>3.3117E-008</td>
<td>390.97</td>
<td>1.0406E-010</td>
<td>294.02</td>
<td>1.4756E-008</td>
</tr>
<tr>
<td>322</td>
<td>438.73</td>
<td>1.4032E-010</td>
<td>404.22</td>
<td>4.3434E-008</td>
<td>391.54</td>
<td>3.3443E-009</td>
<td>294.53</td>
<td>3.7001E-008</td>
</tr>
<tr>
<td>323</td>
<td>440.58</td>
<td>3.7124E-010</td>
<td>404.87</td>
<td>6.7443E-007</td>
<td>392.32</td>
<td>2.1182E-009</td>
<td>295.32</td>
<td>2.3920E-008</td>
</tr>
<tr>
<td>324</td>
<td>440.63</td>
<td>4.5393E-010</td>
<td>405.55</td>
<td>1.6963E-007</td>
<td>392.43</td>
<td>7.4768E-010</td>
<td>295.37</td>
<td>4.3229E-008</td>
</tr>
<tr>
<td>325</td>
<td>447.27</td>
<td>5.7540E-008</td>
<td>406.64</td>
<td>3.5433E-007</td>
<td>392.72</td>
<td>1.3288E-009</td>
<td>305.51</td>
<td>4.3161E-006</td>
</tr>
<tr>
<td>326</td>
<td>447.40</td>
<td>4.8382E-008</td>
<td>407.16</td>
<td>6.3086E-009</td>
<td>393.15</td>
<td>2.3448E-010</td>
<td>306.39</td>
<td>4.3765E-006</td>
</tr>
<tr>
<td>327</td>
<td>447.42</td>
<td>5.6155E-008</td>
<td>410.56</td>
<td>2.4774E-005</td>
<td>393.52</td>
<td>9.2514E-010</td>
<td>308.08</td>
<td>4.4462E-006</td>
</tr>
<tr>
<td>328</td>
<td>447.54</td>
<td>5.1256E-008</td>
<td>411.24</td>
<td>1.4097E-005</td>
<td>393.94</td>
<td>1.6952E-010</td>
<td>308.20</td>
<td>4.5791E-006</td>
</tr>
<tr>
<td>329</td>
<td>449.68</td>
<td>1.6560E-008</td>
<td>411.24</td>
<td>2.2824E-005</td>
<td>393.96</td>
<td>6.9487E-010</td>
<td>310.01</td>
<td>3.2526E-006</td>
</tr>
<tr>
<td>330</td>
<td>449.77</td>
<td>1.8271E-008</td>
<td>411.90</td>
<td>2.2147E-005</td>
<td>394.27</td>
<td>8.2713E-009</td>
<td>310.18</td>
<td>2.3415E-006</td>
</tr>
<tr>
<td>331</td>
<td>450.20</td>
<td>3.0157E-008</td>
<td>429.91</td>
<td>2.0983E-007</td>
<td>394.58</td>
<td>1.0668E-009</td>
<td>310.54</td>
<td>2.2680E-006</td>
</tr>
<tr>
<td>332</td>
<td>450.33</td>
<td>3.4849E-008</td>
<td>429.97</td>
<td>3.6394E-008</td>
<td>394.76</td>
<td>3.4646E-009</td>
<td>310.60</td>
<td>2.4550E-006</td>
</tr>
<tr>
<td>333</td>
<td>450.93</td>
<td>3.8846E-009</td>
<td>430.45</td>
<td>3.0378E-007</td>
<td>395.04</td>
<td>7.5814E-010</td>
<td>313.44</td>
<td>5.4890E-006</td>
</tr>
<tr>
<td>334</td>
<td>451.03</td>
<td>8.8625E-009</td>
<td>430.80</td>
<td>3.3928E-007</td>
<td>395.09</td>
<td>2.9306E-009</td>
<td>313.64</td>
<td>5.3825E-006</td>
</tr>
<tr>
<td>335</td>
<td>452.13</td>
<td>3.3724E-009</td>
<td>431.45</td>
<td>7.7721E-008</td>
<td>396.29</td>
<td>7.9198E-011</td>
<td>314.01</td>
<td>5.2625E-006</td>