# Vacancy ordering and electronic structure of $\gamma$-Fe₂O₃ (maghemite): a theoretical investigation

Ricardo Grau-Crespo,* Asmaa Y. Al-Baitai, Iman Saadoune and Nora H. De Leeuw

Department of Chemistry, University College London, 20 Gordon Street, London, United Kingdom, WC1H 0AJ.

Email: r.grau-crespo@ucl.ac.uk

Abstract. The crystal structure of the iron oxide $\gamma$-Fe₂O₃ is usually reported in either the cubic system (space group P4₃32) with partial Fe vacancy disorder or in the tetragonal system (space group P4₁2₁2) with full site ordering and $c/a$$\approx$3. Using a supercell of the cubic structure, we obtain the spectrum of energies of all the ordered configurations which contribute to the partially disordered P4₃32 cubic structure. Our results show that the configuration with space group P4₁2₁2 is indeed much more stable than the others, and that this stability arises from a favourable electrostatic contribution, as this configuration exhibits the maximum possible homogeneity in the distribution of iron cations and vacancies. Maghemite is therefore expected to be fully ordered in equilibrium, and deviations from this behaviour should be associated with metastable growth, extended anti-site defects and surface effects in the case of small nanoparticles. The confirmation of the ordered tetragonal structure allows us to investigate the electronic structure of the material using density functional theory (DFT) calculations. The inclusion of a Hubbard (DFT+U) correction allows the calculation of a band gap in good agreement with experiment. The value of the gap is dependent on the electron spin, which is the basis for the spin-filtering properties of maghemite.

### 1. Introduction

Maghemite ($\gamma$-Fe₂O₃) is the second most stable polymorph of iron oxide. Contrasting with antiferromagnetic hematite ($\alpha$- Fe₂O₃), maghemite exhibits ferrimagnetic ordering with a net magnetic moment (2.5 $\mu_\text{B}$ per formula unit) and high Néel temperature (~950 K), which together with its chemical stability and low cost led to its wide application as magnetic pigment in electronic recording media since the late 1940's [1]. Maghemite nanoparticles are also widely used in biomedicine, because their magnetism allows manipulation with external fields, while they are biocompatible and potentially non-toxic to humans [2, 3]. Another promising application is in the field of spintronics, where it has been suggested that $\gamma$-Fe₂O₃ can be used as a magnetic tunnelling-barrier for room-temperature spin-filter devices [4, 5].

Maghemite occurs naturally in soils as a weathering product of magnetite (Fe₃O₄), to which it is structurally related [6]. Both maghemite and magnetite exhibit a spinel crystal structure, but while the latter contains both $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ cations, in maghemite all the iron cations are in trivalent state, and the charge neutrality of the cell is guaranteed by the presence of cation vacancies. The unit cell of magnetite can be represented as $(\text{Fe}^{3+})_8[\text{Fe}^{2.5+}]_{16}\text{O}_{32}$, where the brackets () and [] designate tetrahedral and octahedral sites, respectively, corresponding to 8a and 16d Wyckoff positions in space group Fd3m. The maghemite structure can be obtained by creating 8/3 vacancies out of the 24 Fe sites in the cubic unit cell of magnetite. These vacancies are known to be located in the octahedral sites [7] and therefore the structure of maghemite can be approximated as a cubic unit cell with composition $(\text{Fe}^{3+})_8[\text{Fe}^{3+}_{5/6}\ \square_{1/6}]_{16}\text{O}_{32}$.

The nature and degree of ordering of the iron vacancies in the octahedral sites has been the subject of investigations for several decades. If the cation vacancies were randomly distributed over the octahedral sites, as it was initially assumed, the space group would be Fd3m like in magnetite [8, 9]. The first indication of a departure from the Fd3m symmetry was reported by Haul and Schoon [10], who noticed extra reflections in the powder diffraction pattern of maghemite prepared by oxidising magnetite. Braun [11] later noticed that maghemite exhibits the same superstructure as lithium ferrite ($\text{LiFe}_5\text{O}_8$), which is also a spinel with unit cell composition $(\text{Fe}^{3+})_8[\text{Fe}^{3+}_{3/4}\text{Li}^{1+}_{1/4}]_{16}\text{O}_{32}$, and suggested this was due to similar ordering in both compounds. In the space group P4₃32 of lithium ferrite, there are two types of octahedral sites, one with multiplicity 12 in the unit cell, and one with multiplicity 4, which is the one occupied by Li. In maghemite, the same symmetry exists if the Fe vacancies are constrained to these Wyckoff 4b sites, instead of being distributed over all the 16 octahedral sites. It should be

noted, however, that some level of disorder persists in this structure, as the 4b sites have fractional (1/3) iron occupancies.

Oosterhout and Rooijmans [12] first suggested a spinel tetragonal superstructure with $c/a$=3, where the Fe atoms are completely ordered. A neutron diffraction study by Greaves [13] confirmed a higher degree of ordering than the one implied by the cubic P4₃32 structure, and described this departure as a tetragonal distortion. The positions of the vacancies in the fully-ordered maghemite structure were obtained by Shmakov *et al.* [14] using synchrotron X-ray diffraction. This ordered maghemite structure has the tetragonal space group P4₁2₁2 with $a$=8.347 Å and $c$=25.042 Å (spinel cubic cell tripled along the $c$ axis). The ion coordinates in the P4₁2₁2 structure have been recently refined by Jorgensen *et al.* based on synchrotron X-ray powder diffraction data [15].

Despite this progress in the structure determination of maghemite, the phenomenon of vacancy ordering in the lattice is not yet fully understood. It is not clear, for example, under which conditions, if any, vacancy disorder occurs. It has been suggested that the degree of ordering depends on crystal size, and that very small particles of maghemite do now show vacancy ordering [6, 16], although a recent investigation of needle-shaped maghemite nanoparticles with average size 240nm x 30nm has found the same tetragonal distortion with space group P4₁2₁2 as in the ordered crystal [17]. The thermodynamics of vacancy ordering in maghemite has not been investigated so far, in part because of the difficulty to control experimentally the level of ordering of the iron vacancies.

In this paper, we present a computational investigation of the energetics of vacancy ordering in maghemite. We will show that a fully ordered structure with tetragonal space group P4₁2₁2 is indeed the most stable configuration among all the possible ionic arrangements that are compatible with the partially disordered P4₃32 structure, and that this stability arises from a most favourable electrostatic contribution. We then use this ordered structure to discuss the electronic properties of maghemite, which are relevant for potential applications of maghemite in the field of spintronics.

## 2. Computational details

The thermodynamics of ion disorder was investigated by the direct evaluation of the lattice energies of different ionic configurations, using interatomic potentials. This approach is based on the Born model of ionic solids [18], which assumes that the ions in the crystal interact via long-range electrostatic forces and short-range forces, including both the Pauli repulsion and dispersion attraction between neighbouring electron charge clouds. The

short-range contribution has a simple analytical form, in this case a Buckingham potential,
given by the expression:

$$
V_{i j}\left(r_{i j}\right)=A_{i j} \exp \left(-r_{i j} / \rho_{i j}\right)-C_{i j} / r_{i j}^{6} \tag{1}
$$

where $A_{i j}, \rho_{i j}$ and $C_{i j}$ are parameters specific to the interaction of the ions $i$ and $j$ and $r_{i j}$ is
the ion separation. The electronic polarisability of the ions is included via the shell model of
Dick and Overhauser [19], where each polarisable ion, here the oxygen ion, is represented
by a core and a massless shell, connected by a spring. The polarisability of the model ion is
then determined by the spring constant and the charges of the core and shell. The potential
parameters used in this study were derived by Lewis and Catlow [20], and the calculations
were performed with the GULP code [21-23].

The investigation of site-disordered structures using computer-modelling methods poses
the problem of the large number of possible configurations that can exist for a particular
supercell. We have used the methodology implemented in the program SOD (Site Occupancy
Disorder [24]), which generates the complete configurational space for each composition of the
supercell, and then extracts the subspace of symmetrically equivalent configurations. The
criterion for the equivalence of two configurations is the existence of an isometric
transformation that converts one configuration into the other and the transformations considered
are simply the symmetry operators of the parent structure (the structure from which all
configurations are derived via site substitution). This method typically reduces the size of the
configurational space by one or two orders of magnitude, making the problem more tractable.

Although simulations based on classical interatomic potentials are known to perform
very well in the description of ionic and semi-ionic solids, including iron oxides (e.g. [25-29]),
quantum mechanical calculations are required when investigating their electronic and magnetic
properties. We have performed electronic structure calculations, based on the density functional
theory (DFT) in the generalized gradient approximation (GGA), using the Vienna Ab Initio
Simulation Program (VASP) [30]. In order to improve the description of the Fe 3d orbitals, a
Hubbard correction was added, using the so-called GGA+U methodology [31-34], in the
approximation of Dudarev et al., (1998) where a single parameter, $U_{\text {eff }}$, determines an orbital-
dependent correction to the DFT energy. In this work we have used $U_{\text {eff }}=4 \mathrm{eV}$, which has been
shown to provide a good description of the electronic and magnetic structures of different $\mathrm{Fe}^{3+}$
oxides including hematite $(\alpha-\mathrm{Fe}_{2} \mathrm{O}_{3})$ [35, 36] and iron antimony oxide $(\mathrm{FeSbO}_{4})$ [37-40]. The
basis set size here is regulated by the cutoff energy ($E_{\text {cut }}=400$ eV in our study), in such a way
that all plane waves with energies less than $E_{\text {cut }}$ are included. We have used frozen-core

projector augmented wave (PAW) potentials [41], where the core consisted of orbitals up to and including $3p$ of Fe and $1s$ of O atoms. The Brillouin zone was sampled by a 3x3x1 Monkhorst-Pack mesh of k-points for the (1x1x3) supercell for the geometry optimisation, while a mesh of 6x6x2 was employed for the calculation of the electronic density of states. The calculations allow for spin polarisation of the wave functions, to reflect the magnetic character of maghemite. In maghemite, as in magnetite, the magnetic moments on the tetrahedral and octahedral sites are oriented in opposite directions, leading to ferrimagnetic behaviour [42], and we have therefore used the same magnetic configuration in our calculations.

## 3. Results and Discussion

### 3.1 Configurational spectrum

We first employ interatomic potential calculations to investigate the ordering of cation vacancies in $\gamma$-Fe₂O₃. Our starting point is the partially disordered cubic spinel structure with space group P4₃32 initially suggested by Braun [11], where Fe ions and vacancies are distributed in the Wyckoff 4b octahedral positions. This structure is equivalent to lithium ferrite LiFe₅O₈, where the 4b positions are occupied by the Li cations. For this reason, we will call these positions "L" (for lithium) sites, even though we have no Li in the structures investigated in this work. An iron occupancy of 1/3 on the L sites makes the stoichiometry Feᴸ₁/₃Fe₅O₈. In the partially disordered cubic cell of maghemite, the 2.667 (or 8/3) iron vacancies are randomly distributed over the four L sites, together with 1.333 (or 4/3) iron cations. In order to have integer occupancies, we triple the unit cell along one axis (chosen to be $c$, to be consistent with the traditional convention for tetragonal systems). This 1x1x3 supercell thus contains 8 vacancies, which are now distributed, together with 4 iron cations, over the 12 L sites, and the coordinates of these positions for the 1x1x3 supercell are given in Table 1. Note that there are 12 layers, perpendicular to the <001> direction, containing octahedral sites with only one L-type site in each layer per simulation cell (Fig. 1).

The total number of combinations of the 4 Fe ions on the L sites of the supercell is 12!/(4! ×8!)=495, but only 29 of these are inequivalent, as determined using the SOD program. Table 2 lists the positions of the cations in each of the inequivalent configurations, together with their space groups, their degeneracies (how many times they are repeated in the full configurational space) and their relative energies, as calculated with the interatomic potential model. This information defines a multi-configurational model of vacancy ordering in maghemite, which is capable of describing the two extreme cases: if the energies of all the configurations are very similar, or differ very little compared with the thermal energy at the

equilibration temperature, then the system is expected to be fully disordered. On the other hand, if one of the configurations is much more stable than the others, then the system should be ordered. A number of intermediate situations can also be described within the same framework, depending on the distribution of configuration energies.

The full configurational spectrum is shown in Fig. 2. Only one of these configurations has the space group $P4_12_12$, found by Shmakov *et al.* [14] for fully ordered maghemite. This configuration is indeed the most stable one, with a significant energetic separation from the second most stable configuration (32 kJ/mol). The energy range covered by the configurational spectrum is quite wide (~850 kJ/mol), indicating that full disorder is very unlikely. A more detailed analysis of the consequences of this energy spectrum will be given in section 3.3.

### 3.2 The fully ordered maghemite structure: origin of its stabilisation

The distinctive feature of the most stable configuration ($P4_12_12$) is the maximum possible homogeneity of iron cations and vacancies over the L sites. This configuration is the only one in which vacancies never occupy three consecutive layers; there are always two layers containing vacancies separated by a layer without vacancies, which instead contains $Fe^{3+}$ cations in the L sites (e.g. positions L1 - L4 - L7 - L10) and the $P4_12_12$ configuration is therefore the one that minimizes the electrostatic repulsion between these cations.

It is possible to check that the electrostatic interactions indeed dominate the relative stability of the different configurations over the whole spectrum: the total energies correlate well with the Coulomb-only energies obtained using formal charges for all ions (Fig. 3). The polarization of the anions is mainly responsible for the difference in the two energy scales, as polarization is known to compensate for the introduction of formal ionic charges in interatomic potential models [21]. Deviations from the straight line are mainly caused by relaxation effects, which are stronger for the least stable configurations. Based on this analysis, it is not surprising that the least stable configuration is the one with the maximum segregation of iron ions and vacancies over the L sites (iron cations in consecutive layers, e.g. L1 to L4, and vacancies in consecutive layers, L5 to L12), with an energy 847 kJ/mol above the $P4_12_12$ configuration.

The relaxed cell parameters for the ordered $P4_12_12$ structure are $a$=8.359 Å and $c$=24.854 Å. The ratio $c/3a$=0.991 shows a small but significant deviation from the cubic symmetry. In the paper by Shmakov *et al.* [14] no cell parameters are precisely given for the $P4_12_12$ structure, apart from stating that the cell is tripled along the $c$ axis with respect to the original cubic structure (with $a$=8.347 Å). However, our result of $c/3a < 1$ is consistent with the observation by Greaves from neutron diffraction, that the tetragonal distortion accompanying

vacancy ordering in maghemite slightly shrinks the crystal along the $c$ axis with respect to $a$ [13]. The bulk modulus obtained from our calculation of the ordered structure (211 GPa) is also in good agreement with the experimental value of Jiang *et al.* (203 GPa) [43].

Finally, we should note that, besides the ordered structure described here, there is another possible distribution of vacancies that gives the same $P4_12_12$ symmetry. This distribution, which is not listed in Table 2 as a configuration because it is partially disordered, can be described as follows. In the $P4_12_12$ space group, the L sites are divided into two symmetrically distinct positions, one with four-fold degeneracy, and the other with eight-fold degeneracy. While the ordered structure described above corresponds to full iron occupancy of the fourfold position, the distribution with half occupancy of the eightfold position also leads to $P4_12_12$ symmetry. However, we will show below that our calculated energetic spectrum of configurations strongly supports the full order scenario.

### 3.3 Thermodynamics of ordering from canonical statistical mechanics

In order to interpret the energy differences in the configurational spectrum in terms of the degree of vacancy ordering in the solid, we can estimate the probability of occurrence of each independent configuration $m$ as a function of its energy $E_m$, its degeneracy $\Omega_m$ and the equilibration temperature $T$, using Boltzmann's statistics [24, 44, 45]:

$$
P_{m}=\frac{\Omega_{m}}{Z} \exp \left(-E_{m} / k_{B} T\right) \tag{2}
$$

where $k_B$=8.314×10⁻³ kJ/mol K is Boltzmann's constant, and

$$
Z=\sum_{m} \Omega_{m} \exp \left(-E_{m} / k_{B} T\right) \tag{3}
$$

is the canonical partition function, which ensures that the sum of probabilities equals one. Figure 4 shows the probabilities of the most stable configuration ($P4_12_12$) and of the second most stable configuration (with space group $C222_1$) as a function of temperature. At 500 K, a typical synthesis temperature for maghemite [14], the cumulative probabilities of all the configurations excluding the most stable $P4_12_12$ is less than 0.1%. This contribution increases slowly with temperature, but at 800 K this cumulative probability, which measures the expected level of vacancy disorder, is still less than 2%. At temperatures above 700-800 K maghemite transforms irreversibly to hematite ($\alpha$-$Fe_2O_3$), and considering higher temperatures is therefore irrelevant. It thus seems clear that perfect crystals of maghemite in configurational equilibrium should have a fully ordered distribution of cation vacancies.

It is important to realize that, in real samples, several factors can prevent this ordering to develop completely. First, synthesis temperatures are typically too low and preparation times too short to allow complete equilibration of the ionic configurations during the synthesis. Second, the nature of the ordering in the structure means that disorder of anti-site type is expected to be abundant. For example, if the ordering sequence along the $c$ axis (two layers including vacancies plus one layer including iron cations in the L sites) is locally broken every few unit cells (for example, leading to two layers with iron cations in the L sites separated by only with vacancy layer), the overall symmetry of the crystal is not retained and the sample will appear disordered to diffraction methods. Third, in very small particles, surface effects might also alter the preferential distribution of cations, which could contribute to the absence of ordering reported in some maghemite nanoparticles [6, 16] .

### 3.4 Electronic structure and magnetism

The existence of a well-defined ordered structure of maghemite has an important advantage for the theoretical investigation of this material, as traditional electronic structure calculation techniques with periodic boundary conditions can be applied to the investigation of the electronic properties. In this section we discuss the electronic structure of ordered maghemite based on the results of our density functional theory (DFT) calculations.

As discussed in the methodology section, the ferrimagnetic ordering of the cation was forced in the calculation by assigning initial magnetic moments with opposite directions to $\mathrm{Fe}^{3+}$ cations in octahedral and tetrahedral sites. However, the total magnetization of the $(\mathrm{Fe})_{24}[\mathrm{Fe}]_{40} \mathrm{O}_{96}$ cell was allowed to relax, and after self-consistency it reached the value of $80.0 \mu_{\mathrm{B}}$. This is the expected value if all the iron cations are in high-spin state, and corresponds to $2.5 \mu_{\mathrm{B}}$ per $(\mathrm{Fe})_{3 / 4}[\mathrm{Fe}]_{5 / 4} \mathrm{O}_{3}$ formula unit, in agreement with experimental measurements [1]. The magnetic moments are well localized on the Fe ions, and the integration of the spin density inside PAW spheres around the cations yields $4.19 \mu_{\mathrm{B}}$ for the octahedral Fe ions at L sites, $4.16 \pm 0.01 \mu_{\mathrm{B}}$ for the other octahedral Fe ions, and $-4.03 \pm 0.01 \mu_{\mathrm{B}}$ for the tetrahedral cations. There are small net moments $(0.14 \mu_{\mathrm{B}}$ or less) on the $\mathrm{O}$ anions. The iron magnetic moments obtained by Greaves [13] from neutron diffraction were $4.41 \mu_{\mathrm{B}}$ for octahedral and $-4.18 \mu_{\mathrm{B}}$ for tetrahedral sites, in good agreement with our results.

Figure 5 shows the total electronic density of states and its projections over the $3 d$ orbitals of octahedral and tetrahedral iron cations, and the $2 p$ orbitals of the $\mathrm{O}$ anions. The top of the valence band is mainly of $\mathrm{O} 2 p$ character, while the occupied $3 d$ levels of Fe lie around 6-7 eV below the Fermi level. The bottom of the conduction band is mainly populated by the

unoccupied $3d$ levels of (octahedrally coordinated) Fe. Therefore, maghemite is a charge-transfer type of insulator, and the first excitation term should correspond to the transfer of electrons from the $\mathrm{O}^{2-}$ anions to the octahedral $\mathrm{Fe}^{3+}$ cations.

The calculated band gap of around 2 eV is in agreement with experiment (2.0 eV according to Ref. [46]). However, the DOS around the Fermi level is not symmetric, and there is a difference in band gap between majority spin (2.2 eV) and minority spin (1.8 eV) electrons. The top of the valence band is higher in energy for majority spin electrons while the bottom of the conduction band is lower in energy for minority spin electrons. This is an important feature of the electronic structure of maghemite, as it is related to its potential use as a magnetic tunnelling-barrier for spin-filter devices. In these devices, the spin of the current electrons is controlled by an insulator film with an exchange splitting in the conduction band, through which tunnelling occurs preferentially for one of the spin components [47]. The potential of maghemite for this application has been previously suggested by other authors [4, 5].

## 4. Conclusions
This work represents the first attempt to investigate the phenomenon of vacancy ordering in $\gamma$-$Fe_2O_3$ (maghemite) from an energetic point of view. Our results show clearly that full vacancy ordering, in a pattern with space group $P4_12_12$, is the thermodynamically preferred situation in the bulk material. This stability arises from a minimal Coulombic repulsion between $\mathrm{Fe}^{3+}$ cations for this configuration. However, deviation from perfect order can be expected because the low-temperature formation of maghemite does not guarantee an equilibrium growth of the crystals. Also, the presence of anti-site type disorder and surface effects in nanocrystals could contribute to deviation from the ideal ordering of the vacancies. We have also shown that maghemite is a charge-transfer type insulator with a spin-dependent band gap, which suggests its suitability for applications in spintronics.

## Acknowledgments
This work made use of the facilities of HECToR, the UK's national high-performance computing service, via our membership of the UK's HPC Materials Chemistry Consortium, which is funded by EPSRC (EP/F067496). We acknowledge support from the EU-funded Marie Curie research and training network MIN-GRO (grant MRTN-CT-2006-035488). A.Y. A-B. is grateful to UCL for an Overseas Research Studentship (ORS) Award and the Iraqi government for funding.

Table 1.
Coordinates of the L sites in the calculation supercell. These positions corresponds to the Wyckoff 4b sites of cubic space group P4₃32, expanded to a 1x1x3 supercell.

<table>
  <thead>
    <tr>
      <th><i>Position</i></th>
      <th colspan="3"><i>Coordinates</i></th>
    </tr>
    <tr>
      <th><i>Label</i></th>
      <th><i>x</i></th>
      <th><i>y</i></th>
      <th><i>z</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>L1</td>
      <td>7/8</td>
      <td>3/8</td>
      <td>1/24</td>
    </tr>
    <tr>
      <td>L2</td>
      <td>1/8</td>
      <td>7/8</td>
      <td>3/24</td>
    </tr>
    <tr>
      <td>L3</td>
      <td>5/8</td>
      <td>5/8</td>
      <td>5/24</td>
    </tr>
    <tr>
      <td>L4</td>
      <td>3/8</td>
      <td>1/8</td>
      <td>7/24</td>
    </tr>
    <tr>
      <td>L5</td>
      <td>7/8</td>
      <td>3/8</td>
      <td>9/24</td>
    </tr>
    <tr>
      <td>L6</td>
      <td>1/8</td>
      <td>7/8</td>
      <td>11/24</td>
    </tr>
    <tr>
      <td>L7</td>
      <td>5/8</td>
      <td>5/8</td>
      <td>13/24</td>
    </tr>
    <tr>
      <td>L8</td>
      <td>3/8</td>
      <td>1/8</td>
      <td>15/24</td>
    </tr>
    <tr>
      <td>L9</td>
      <td>7/8</td>
      <td>3/8</td>
      <td>17/24</td>
    </tr>
    <tr>
      <td>L10</td>
      <td>1/8</td>
      <td>7/8</td>
      <td>19/24</td>
    </tr>
    <tr>
      <td>L11</td>
      <td>5/8</td>
      <td>5/8</td>
      <td>21/24</td>
    </tr>
    <tr>
      <td>L12</td>
      <td>3/8</td>
      <td>1/8</td>
      <td>23/24</td>
    </tr>
  </tbody>
</table>

Table 2.
Fully ordered configurations in the 1x1x3 supercell. The labels of the iron positions in the L sites follow the convention given in Table 1. Energies are given with respect to the lowest energy configuration.

<table>
  <thead>
    <tr>
      <th>Iron positions</th>
      <th>Degeneracy</th>
      <th>Space group</th>
      <th>$\Delta E/kJ.mol^{-1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>L1, L4, L7, L10</td>
      <td>3</td>
      <td>P4₁2₁2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>L1, L3, L7, L9</td>
      <td>6</td>
      <td>C222₁</td>
      <td>32</td>
    </tr>
    <tr>
      <td>L1, L3, L7, L10</td>
      <td>24</td>
      <td>P1</td>
      <td>53</td>
    </tr>
    <tr>
      <td>L1, L5, L6, L10</td>
      <td>12</td>
      <td>P2₁</td>
      <td>77</td>
    </tr>
    <tr>
      <td>L1, L5, L6, L8</td>
      <td>12</td>
      <td>C2</td>
      <td>87</td>
    </tr>
    <tr>
      <td>L1, L3, L7, L11</td>
      <td>12</td>
      <td>C2</td>
      <td>106</td>
    </tr>
    <tr>
      <td>L1, L2, L5, L9</td>
      <td>24</td>
      <td>P1</td>
      <td>116</td>
    </tr>
    <tr>
      <td>L1, L3, L7, L8</td>
      <td>24</td>
      <td>P1</td>
      <td>136</td>
    </tr>
    <tr>
      <td>L1, L2, L5, L8</td>
      <td>24</td>
      <td>P1</td>
      <td>149</td>
    </tr>
    <tr>
      <td>L1, L2, L7, L8</td>
      <td>6</td>
      <td>P2₁2₁2₁</td>
      <td>167</td>
    </tr>
    <tr>
      <td>L1, L3, L6, L8</td>
      <td>12</td>
      <td>P2₁</td>
      <td>182</td>
    </tr>
    <tr>
      <td>L1, L2, L5, L10</td>
      <td>12</td>
      <td>P2₁</td>
      <td>213</td>
    </tr>
    <tr>
      <td>L1, L3, L5, L10</td>
      <td>12</td>
      <td>P1</td>
      <td>215</td>
    </tr>
    <tr>
      <td>L1, L2, L6, L7</td>
      <td>12</td>
      <td>C2</td>
      <td>235</td>
    </tr>
    <tr>
      <td>L1, L3, L7, L12</td>
      <td>24</td>
      <td>P1</td>
      <td>276</td>
    </tr>
    <tr>
      <td>L1, L3, L6, L7</td>
      <td>24</td>
      <td>P1</td>
      <td>280</td>
    </tr>
    <tr>
      <td>L1, L4, L5, L6</td>
      <td>24</td>
      <td>P1</td>
      <td>310</td>
    </tr>
    <tr>
      <td>L1, L3, L5, L7</td>
      <td>12</td>
      <td>C2</td>
      <td>343</td>
    </tr>
    <tr>
      <td>L1, L3, L4, L10</td>
      <td>24</td>
      <td>P1</td>
      <td>380</td>
    </tr>
    <tr>
      <td>L1, L3, L4, L7</td>
      <td>24</td>
      <td>P1</td>
      <td>413</td>
    </tr>
    <tr>
      <td>L1, L2, L5, L6</td>
      <td>12</td>
      <td>P2₁</td>
      <td>425</td>
    </tr>
    <tr>
      <td>L1, L2, L3, L8</td>
      <td>12</td>
      <td>C2</td>
      <td>470</td>
    </tr>
    <tr>
      <td>L1, L2, L3, L7</td>
      <td>24</td>
      <td>P1</td>
      <td>501</td>
    </tr>
    <tr>
      <td>L1, L3, L5, L6</td>
      <td>24</td>
      <td>P1</td>
      <td>560</td>
    </tr>
    <tr>
      <td>L1, L2, L3, L6</td>
      <td>24</td>
      <td>P1</td>
      <td>608</td>
    </tr>
    <tr>
      <td>L1, L3, L4, L6</td>
      <td>12</td>
      <td>P2₁</td>
      <td>640</td>
    </tr>
    <tr>
      <td>L1, L2, L4, L5</td>
      <td>12</td>
      <td>P1</td>
      <td>652</td>
    </tr>
    <tr>
      <td>L1, L2, L3, L5</td>
      <td>24</td>
      <td>P1</td>
      <td>722</td>
    </tr>
    <tr>
      <td>L1, L2, L3, L4</td>
      <td>12</td>
      <td>P2₁</td>
      <td>847</td>
    </tr>
  </tbody>
</table>

Figure captions:

Figure 1: Possible positions for the iron vacancies in the 1x1x3 supercell. The 12 L sites, which should be populated with 4 iron ions and 8 vacancies, are marked as larger spheres.

Figure 2: Energetic spectrum of configurations for 4 iron ions and 8 vacancies distributed over the L sites in a 1x1x3 supercell of the cubic maghemite structure.

Figure 3: The relationship between the total lattice energies and the electrostatic energies of the different vacancy configurations.

Figure 4: Probabilities of the configurations as a function of temperature.

Figure 5: Electronic density of states corresponding to the ordered structure and its projection over Fe $3d$ and O $2p$ orbitals.

![](./images/867773547810915190_1.jpg)

Figure 1

![](./images/867773547810915190_2.jpg)

Figure 2

![](./images/867773547810915190_3.jpg)

Figure 3

![](./images/867773547810915190_4.jpg)

Figure 4

![](./images/867773547810915190_5.jpg)

Figure 5

### References

[1] Dronskowski R., *Adv. Funct. Mater.* 11 (2001) 27.

[2] Pankhurst Q.A., Connolly J., Jones S.K., and Dobson J., *J. Phys. D.-Appl. Phys.* 36 (2003) R167.

[3] Levy M., Wilhelm C., Siaugue J.M., Horner O., Bacri J.C., and Gazeau F., *J. Phys. - Condens. Mat.* 20 (2008).

[4] Wiemann J.A., et al., *J. Appl. Phys.* 87 (2000) 7001.

[5] Yanagihara H., Hasegawa M., Kita E., Wakabayashi Y., Sawa H., and Siratori K., *J. Phys. Soc. Jap.* 75 (2006) 054708.

[6] Cornell R.M. and Schwertman U., *The Iron Oxides, Structure, Properties , Reactions , Occurences and Uses.* . 2003, Weinheim: Wiley-VCH.

[7] Waychunas G.A., in *Oxide Minerals petrolic and magnetic significance*, D.H. Lindsley, Editor. 1991, Miner. Soc. Am. p. 11.

[8] Hagg G., *Z. Physik. Chem.* 29B (1935) 95.

[9] Verwey E.J.W., *Z. Krist. A.* 91 (1935) 65.

[10] Haul R. and Schoon T., *Z. Physik. Chem.* 44B (1939) 216.

[11] Braun P.B., *Nature.* 170 (1952) 1123.

[12] van Oosterhout G.W. and Rooijmans C.J.M., *Nature.* 181 (1958) 44.

[13] Greaves C., *J. Solid State Chem.* 49 (1983) 325.

[14] Shmakov A.N., Kryukova G.N., Tsybulya S.V., ChuviIin A.L., and Solovyeva L.P., *J. Appl. Crystallogr.* 28 (1995) 141.

[15] Jorgensen J.E., Mosegaard L., Thomsen L.E., Jensen T.R., and Hanson J.C., *J. Solid State Chem.* 180 (2007) 180.

[16] Bastow T.J., Trinchi A., Hill M.R., Harris R., and Muster T.H., *J. Magn. Magn. Mater.* 321 (2009) 2677.

[17] Somogyvari Z., et al., *Applied Physics a-Materials Science & Processing.* 74 (2002) S1077.

[18] Born M. and Huang K., *Dynamical theory of crystal lattices.* 1954, Oxford: Oxford University Press.

[19] Dick B.G. and Overhauser A.W., *Phys. Rev.* 112 (1958) 90.

[20] Lewis G.V. and Catlow C.R.A., *Journal of Physics C-Solid State Physics.* 18 (1985) 1149.

[21] Gale J.D., *J Chem Soc Faraday T.* 93 (1997) 629.

[22] Gale J.D., *Z. Kristallogr.* 220 (2005) 552.

[23] Gale J.D. and Rohl A.L., *Mol. Simul.* 29 (2003) 291.

[24] Grau-Crespo R., Hamad S., Catlow C.R.A., and de Leeuw N.H., *J. Phys. - Condens. Mat.* 19 (2007) 256201.

[25] Benny S., Grau-Crespo R., and De Leeuw N.H., *Phys. Chem. Chem. Phys.* 11 (2009) 808

[26] Chamritski I. and Burns G., *J. Phys. Chem. B.* 109 (2005) 4965.

[27] Cooke D.J., Redfern S.E., and Parker S.C., *Phys. Chem. Miner.* 31 (2004) 507.

[28] Donnerberg H. and Catlow C.R.A., *J. Phys. - Condens. Mat.* 5 (1993) 2947.

[29] de Leeuw N.H. and Cooper T.G., *Geochim. Cosmochim. Acta.* 71 (2007) 1655.

[30] Hafner J., *Comput. Phys. Commun.* 177 (2007) 6.

[31] Anisimov V.I., Zaanen J., and Andersen O.K., *Phys. Rev. B.* 44 (1991) 943

[32] Rohrbach A., Hafner J., and Kresse G., *J. Phys. - Condens. Mat.* 15 (2003) 979

[33] Liechtenstein A.I., *Phys. Rev. B.* 52 (1995) R5467

[34] Dudarev S.L., Botton G.A., Savrasov S.Y., Humphreys C.J., and Sutton A.P., *Phys. Rev. B.* 57 (1998) 1505.

[35] Rollmann G., Rohrbach A., Entel P., and Hafner J., *Phys. Rev. B.* 69 (2004) art. no.

[36] Rohrbach A., Hafner J., and Kresse G., *Phys. Rev. B.* 70 (2004) 125426.

[37] Gabitov R.I., Cohen A.L., Gaetani G.A., Holcomb M., and Watson E.B., *Geochim. Cosmochim. Acta.* 70 (2006) A187.

[38] Grau-Crespo R., Catlow C.R.A., and De Leeuw N.H., *J. Catal.* 248 (2007) 77.

[39] Grau-Crespo R., Cora F., Sokol A.A., de Leeuw N.H., and Catlow C.R.A., *Phys. Rev. B.* 73 (2006) 035116.

[40] Grau-Crespo R., Moreira I.D.R., Illas F., de Leeuw N.H., and Catlow C.R.A., *J. Mater. Chem.* 16 (2006) 1943.

[41] Blochl P.E., *Phys. Rev. B.* 50 (1994) 17953.

[42] Neel L., *Ann. Phys. Paris* 3(1948) 137.

[43] Jiang J.Z., Staun Olsen J., Gerward L., and Morup S., *Europhysics Letters.* 44 (1998) 620.

[44] Grau-Crespo R., Peralta A.G., Ruiz-Salvador A.R., Gomez A., and Lopez-Cordero R., *Phys. Chem. Chem. Phys.* 2 (2000) 5716.

[45] Grau-Crespo R., de Leeuw N.H., and Catlow C.R.A., *J. Mater. Chem.* 13 (2003) 2848.

[46] Litter M.I. and Blesa M.A., *Can. J. Chem.* 70 (1992) 2502.

[47] Moodera J.S., Santos T.S., and Nagahama T., *J. Phys. - Condens. Mat.* 19 (2007).