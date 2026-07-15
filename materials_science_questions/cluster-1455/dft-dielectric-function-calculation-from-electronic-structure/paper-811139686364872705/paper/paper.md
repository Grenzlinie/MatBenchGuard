# Accepted Manuscript

Prediction of indirect to direct band gap transition under tensile biaxial strain in type-I guest-free silicon clathrate $Si_{46}$: A first-principles approach

Nassim Ahmed Mahammedi, Marhoun Ferhat, Rachid Belkada

![](./images/811139686364872705_1.jpg)

| PII: | S0749-6036(16)30373-1 |
|-----|------------------------|
| DOI: | 10.1016/j.spmi.2016.09.026 |
| Reference: | YSPMI 4516 |
| To appear in: | *Superlattices and Microstructures* |

Received Date: 27 June 2016

Revised Date: 19 September 2016

Accepted Date: 26 September 2016

Please cite this article as: N. Ahmed Mahammedi, M. Ferhat, R. Belkada, Prediction of indirect to direct band gap transition under tensile biaxial strain in type-I guest-free silicon clathrate $Si_{46}$: A first-principles approach, *Superlattices and Microstructures* (2016), doi: 10.1016/j.spmi.2016.09.026.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Prediction of indirect to direct band gap transition under tensile biaxial strain in type-I guest-free silicon clathrate $Si_{46}$: a first-principles approach.

Nassim Ahmed MAHAMMEDI¹, Marhoun FERHAT², Rachid BELKADA³

¹Laboratoire de physique des matériaux, Amar Télidji University of Laghouat, BP37G, Laghouat 03000, ALGERIA.
²Department of physics, The University of the West Indies, Mona, Kingston 07, JAMAICA.
³Research Center in Semiconductor Technology for the Energetic CRTSE, B.P.140, Algiers 16038, ALGERIA.

Corresponding author
Nassim Ahmed MAHAMMEDI
n.mahammedi@lagh-univ.dz

## Abstract
We suggest a bandgap engineering approach of first-principles calculations on basis of density functional theory (DFT), to monitor the bandgap transition from indirect to direct for the type-I guest-free silicon clathrate ($Si_{46}$). Hence, we have systematically investigated the effect of planar biaxial strain in either compressive or tensile directions on electronic and optical properties using both GGA-PBE and hybrid GGA-BLYP functionals as implemented in Castep and Dmol³ codes respectively. For unstrained $Si_{46}$, electronic structure has revealed a semiconducting behavior with quasi-direct bandgap estimated at 1.364eV (GGA-PBE) and 1.618eV (GGA-BLYP). Thus, we predict that tensile biaxial strain above +2% can trigger the indirect to direct bandgap transition, which will be located at the X(1/2,0,0) high symmetry point in the first Brillouin zone. The bandgap magnitude increases with the decreasing of biaxial strain and reaches a maximum value of 1.406eV (GGA-PBE) and 1.641eV (GGA-BLYP) at +1% tensile strain, and starts to decrease toward smaller values when the strain is increased. In addition, some relevant optical properties such as the complex dielectric function and the absorption coefficient are computed at each step of biaxial strain. Under tensile strain of +4%, results show better optical properties, the general magnitude of the absorption spectrum is increased by 17.5% with a maximum magnitude of $2.7x10^{4}$ in the visible range of the electromagnetic spectrum.

## Keywords
First-principles calculations, silicon clathrates, biaxial strain, direct bandgap.


### I. Introduction

Beside its leading status as key material in microelectronics and optoelectronics, silicon thrones the photovoltaic market by a dominative share. This leading position is actually due to its many advantages, it is the second most abundant substance on the earth's crust after oxygen (presenting about 25.8% earth's global mass), it has a very stable and excellent oxide SiO₂ [1], its physical-chemical properties are well established and mastered at both research and industrial levels. However, its development as a strategic material for photovoltaics is permanently challenged by its shortage related to the indirect nature of its bandgap, which means that an excited electron in valence band requires a change in its momentum to leap to conduction band by an intervention of a phonon in the bulk. In consequence, this makes silicon a very weak light absorber, the thickness of the absorber layer must be at least equal or superior to the mean-free path of charge carriers to skip the recombination phenomena in the bulk, making the first-generation solar cells of silicon relatively thick (about 200µm) [2]. In order to overcome this problem, the research society came with many innovative and diverse solutions, such as predicting semiconductors with direct bandgaps, as for the case of III-V (GaAs) [3], Chalcopyrites CIGS [4] and cadmium telluride CdTe [5] which already have revealed promising high efficiencies. So far the wide development and mass production of these materials is limited as they use expensive and rare precursor elements such as indium, gallium, and sometimes toxic as arsenic, selenium and cadmium. An ideal solution would be to keep silicon as the main material, and try to engineer its atomic structure to get desired properties [6]. In this context, other allotropic forms of silicon are explored and have exhibited promising physical-chemical properties that could be used in energy conversion systems.

Depending on their atomic arrangement and their method of synthesis different forms of silicon-based compounds are obtained. The second known crystalline form after diamond is the cage-like structures named 'Clathrate'. Clathrates are crystalline inclusion compounds in which the cage formed by host atoms (group IV: C, Si, Ge) encloses within guest atoms or molecules (mostly alkali metal, rare earth or alkaline atoms), [7]. Inspired from hydrate clathrates, their main framework structure consists of face-sharing polyhedrons whose are directly responsible for defining the clathrate's type. Since their synthetize in 1965 by two French groups Kasper et al [8] and Cros et al [9], group-IV clathrates due to their exceptional thermoelectric [10, 11] and superconductive [12, 13] properties, have encountered a great amount of experimental and theoretical investigations. Recently, this class of material has attracted more attention as candidate for photovoltaic applications, [6, 14]. Type-I Silicon clathrate with chemical formula X₈Si₄₆ where X is the guest atom, is the most studied clathrate among the other types, its properties are under investigations and are still revealing more new features, it has been synthetized through a diversity of technics such as arc-melting [15] or high pressure high temperature synthesis

HPHT [16, 17]. More recently, thin film based on clathrates including sodium doped silicon clathrates in type-I $Na_8Si_{46}$ and type-II $Na_xSi_{138}$ [18]. Germanium-gallium clathrates with the chemical formula of $Ba_8Ga_{16}Ge_{30}$ are successfully grown [19]. An attempt to grow a guest-free $Si_{46}$ silicon clathrate was reported [20], and lately a successful growth of thin film of $1\mu m$ of type-II guest free silicon clathrate $Si_{136}$ over a (111) Si substrate by thermal decomposition of NaSi precursor films and Na removal from the $Na_xSi_{136}$ film by a heat treatment with iodine [21].

In the present study, we aim to establish conditions to obtain direct bandgap silicon that can be useful to achieve better efficiencies for solar cells. To the best of our knowledge, strain technology is a well-known and practical technique used to engineer bandgap of semiconductors, it has been applied to improve performances of structures and devices based on diamond silicon [22-24], however, this technique has not been yet used to tune silicon clathrates properties. With this motivation, we have systematically investigated the impact of the in-plane compressive and tensile biaxial strains on the structural, electronic and optical properties of hypothetical guest-free type-I silicon clathrate $Si_{46}$ by means of first-principles calculation within the DFT approach.

## II. Theoretical approach

### II.1.Computational details

In this work, our first-principles calculations based on the density functional theory DFT [25, 26] are carried out by CASTEP (Cambridge Serial Total Energy Package) [27] and Dmol³ [28] codes. In order to solve the Kohn-Sham equations of the DFT, Ultrasoft pseudopotentials of Vanderbilt-model included in the Castep package were employed in real space [29]. The exchange and correlation energy (XC) was treated within generalized gradient approximation (GGA) using the Perdew-Burke-Erzenhorf PBE parameterization [30], this choice is justified by the fact that GGA-PBE functionals has revealed better convergence of the total energy, the ionization energy and the Si-Si bonds lengths and angles for silicon based compounds compared with the local density approximation (LDA) [31]. By means of a self-consistent-field (SCF) calculations, under criterion for the convergence of the total energy of $5.10^{-4}$ eV/atom and 0.001Gpa for pressure, the plane-wave cutoff-energy was set to 480eV, while the first irreducible Brillouin zone in the reciprocal space was sampled at a 6x6x6 grid using the Monkhorst-Pack scheme [32]. In order to minimize the total energy of the system, geometrical and internal coordinates were rigorously relaxed until obtaining 'Hellmann–Feynman' interatomic forces lower than $10^{-3}$eV/Å, this task was accomplished using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) optimization algorithm [33-36]. For the relaxed configuration, major optical properties were computed for each step of biaxial strain. However, for the calculation of the optical spectra of the dielectric

function a dense set of k-points sampling in the Brillouin zone are adopted using 14x14x14 grid of Monkhorst-Pack scheme, which is highly recommended for calculation of optical properties [37]. Hybrid GGA-BLYP [38, 39] functional was solicited through Dmol³ code [28] to recalculate band structures for optimized structures in order to improve bandgap magnitudes as they are expected to be underestimated by regular GGA-PBE functional. For that purpose, the Brillouin zone was sampled into a grid of 10x10x10 using Monkhorst scheme giving 75 k-points,

## II.2.Structural Aspects

Type-I guest-free silicon clathrate $Si_{46}$ crystallize in the simple cubic space group Pm-3n (number 223) [40]. Its unit cell contains 46 atoms, is formed by assembly of eight face-shared elemental cages: two dodecahedral $Si_{20}$ (twelve pentagonal faces with 20 atoms) and six tetrakadecahedral cages $Si_{24}$ (twelve pentagonal faces and two hexagonal faces with 24 atoms) [40, 41], the vacant cavities within the cages are often filled with guest atoms or molecules. In the present study, the initial lattice is built from crystalline parameters taken from reference [42] ($a$=10.055Å), then optimized along with internal atomic coordinates to reach the equilibrium state. At minimum of total energy and interatomic forces, our optimal internal atomic coordinates (following the Wyckoff notation) and lattice parameters are in a good agreement with previous HF-LCCO [43], LDA [44, 45], GGA [46], TBTEMD[42], GTBMD[47] and LDA[48] calculations. Table 1 summarizes our results in comparison with the literature. Figure.1(a) shows a unit cell of $X_{8}Si_{46}$ including the Wyckoff positions. Figure.1(b) illustrates the two initial polyhedrons forming the $Si_{46}$ main framework of the lattice. To the best of our knowledge, experimental values for guest-free type-I $Si_{46}$ are not reported so far, therefore, we took experimental values of $Na_{8}Si_{46}$ as a reference structure [49] ($a$=10.19 Å) to be compared with. This choice is justified as that due to relative large size of silicon frame-work cages, which is less affected by the presence of guest Na atom where the small atomic radius of Na induces no volume increase in the structural transition between $Si_{46}$ and $Na_{8}Si_{46}$ lattices according to [44]. As regard to the mechanical properties, the cubic nature of clathrate leads to define only three independent elastic constants which are given for type-I clathrate $Si_{46}$ as: $C_{11}$=155,140,135 GPa, $C_{12}$=65,47,58 GPa, and $C_{44}$=45,47,40 GPa, the density is ρ=2.1, 2.098, 2.05 g/cm³ as all respectively reported by [42, 50, 51]. We report a density of ρ= 2.01g/cm³.

![](./images/811139686364872705_2.jpg)

![](./images/811139686364872705_3.jpg)

FIG.1: Aspect of the crystalline structure of type-I Silicon clathrate $X_8Si_{46}$, (space group: Pm-3n, No 223). (a) A unit cell of $Ba_8Si_{46}$ containing 46 Si atoms occupying the following positions according to the Wyckoff notification: Si1(6c) (yellow), Si2(16i) (gray), Si3(24k) (blue), (6d and 2a) (dark and light red) are occupied by eight Ba guest atoms. (b) Two types of polyhedrons ($Si_{20}$ (yellow) + $Si_{24}$ (green)) forming the type-I $X_8Si_{46}$ clathrate framework with guest atoms inside (view down the (111) direction).

<table>
<caption>Table.I: Optimized lattice parameters and atomic positions of type-I guest-free silicon clathrate $Si_{46}$ (space group $Pm\overline{3}n$ (223)) using the GGA-PBE approximation.</caption>
<tr>
<td></td>
<td colspan="8">Lattice parameter $a_0(\mathring{A})$</td>
</tr>
<tr>
<td></td>
<td>$10.22^{\text{a}}$</td>
<td>$10.406^{\text{b}}$</td>
<td>$10.19^{\text{c}}$</td>
<td>$10.069^{\text{d}}$</td>
<td>$10.229^{\text{e}}$</td>
<td>$10.055^{\text{f}}$</td>
<td>$10.20^{\text{g}}$</td>
<td>$10.069^{\text{h}}$</td>
</tr>
<tr>
<td>Atom</td>
<td>Site: Wyckoff notation</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
</tr>
<tr>
<td>Si(1)</td>
<td>$6c$ ($x$, $y$, $z$)</td>
<td>$0.25^{\text{ a,b,c,f}}$</td>
<td>$0^{\text{ a,b,c,f}}$</td>
<td>$0.5^{\text{ a,b,c,f}}$</td>
</tr>
<tr>
<td rowspan="4">Si(2)</td>
<td rowspan="4">$16i$ ($x$, $x$, $x$)</td>
<td>$0.1836^{\text{a}}$</td>
<td>$0.1836^{\text{a}}$</td>
<td>$0.1836^{\text{a}}$</td>
</tr>
<tr>
<td>$0.1839^{\text{b}}$</td>
<td>$0.1839^{\text{b}}$</td>
<td>$0.1839^{\text{b}}$</td>
</tr>
<tr>
<td>$0.1835^{\text{c}}$</td>
<td>$0.1835^{\text{c}}$</td>
<td>$0.1835^{\text{c}}$</td>
</tr>
<tr>
<td>$0.1840^{\text{d}}$</td>
<td>$0.1840^{\text{d}}$</td>
<td>$0.1840^{\text{d}}$</td>
</tr>
<tr>
<td rowspan="4">Si(3)</td>
<td rowspan="4">$24k$ ($0$, $y$, $z$)</td>
<td rowspan="4">$0^{\text{ a,b,c,d}}$</td>
<td>$0.3079^{\text{a}}$</td>
<td>$0.1170^{\text{a}}$</td>
</tr>
<tr>
<td>$0.3070^{\text{b}}$</td>
<td>$0.1176^{\text{b}}$</td>
</tr>
<tr>
<td>$0.3077^{\text{c}}$</td>
<td>$0.1174^{\text{c}}$</td>
</tr>
<tr>
<td>$0.3080^{\text{d}}$</td>
<td>$0.1170^{\text{d}}$</td>
</tr>
<tr>
<td colspan="5">a: This work (GGA-PBE)
b: Data from reference [43] (HF-LCCO: Hartree-Fock linear combination of crystalline orbitals)
c: Data from reference [44] (LDA: Local density approximation)
d: Data from reference [45] (LAPW: Linearized augmented Plane Wave-LDA)
e: Data from reference [46] (GGA-PBE)
f: Data from reference [42] (TBTEMD: Tight binding total energy molecular dynamics)
g: Data from reference [47] (GTBMD: Generalized tight-binding molecular dynamics)
h: Data from reference [52] (LDA)</td>
</tr>
</table>

### II.3.Biaxial strain simulation

The biaxial strain is applied by imposing a biaxial stress tensor ($\sigma_{11}$=$\sigma_{22}$≠$\sigma_{33}$) on the material where the same amount of stress is applied along the <100> and <010> directions $\sigma_{11}$=$\sigma_{22}$≠0 and the out-of-plane axis along <001> direction is free of stress $\sigma_{33}$=0. The strain tensor can be determined through the Hooke's laws of general elasticity [53-55].

$$(\sigma_{ij})=(C_{ij})\ (\varepsilon_{ij})\ ,\ i,j=1,2,3 \quad (1)$$

In order to simulate both compressive ($\varepsilon_{11}$= $\varepsilon_{22}$ <0) and tensile ($\varepsilon_{11}$= $\varepsilon_{22}$ >0) in-plane biaxial strains that any epitaxial thin film undergoes when it is grown over substrates with different lattice constants, the lattice parameters at the equilibrium state are modified according to the formulas (2) and (3),

$$\varepsilon_{11}=\varepsilon_{22}=\frac{a-a_{0}}{a_{0}}=\frac{\Delta a}{a_{0}} \tag{2}$$

$$\varepsilon_{33}=\frac{c-c_{0}}{c_{0}}=\frac{\Delta c}{c_{0}} \tag{3}$$

Where: ($\varepsilon_{11}$(%)= $\varepsilon_{22}$(%)) rate correspond to the simulated compressive ($\varepsilon_{11}$<0) and tensile ($\varepsilon_{11}$>0) planar biaxial strains along x- and y-axis respectively, whereas $\varepsilon_{33}$(%), presents the induced out-of-plane deformation rate due to the relative displacement along the z-axis. ($a_{0}$=$b_{0}$) are the optimized equilibrium lattice constants, while ($a$=$b$) represent the new lattice parameters induced from the strained structure of Si₄₆.

The formulas (2) and (3) are often used to model the lattice mismatch between an epitaxial grown thin film on a given substrate, which imposes its lattice parameters on the epitaxial film, consequently induces internal strain. For the obtained stable structure in-plane lattice parameters $a$ and $b$ are calculated and fixed at the values corresponding to a desired strain rate, while the out-of-plane lattice parameter $c$ is relaxed along with the internal atomic coordinates of the strained lattice using the BFGS optimization algorithm [33-36], keeping same criterions as described in the computational procedures section. Calculations including strain between -4% (compressive) to +4% (tensile) by steps of 1% were considered.

## III. Results and discussion

### III.1. Electronic properties of unstrained Si₄₆

Figure.2 depicts the calculated band structure with (a) GGA-PBE and (b) GGA-BLYP. In both figures the path of k-vector in the first Brillouin zone is chosen to follow the X-R-M-Γ-R high symmetry segments, and the Fermi energy is set to the zero energy reference. According to the chosen Ultrasoft pseudopotentials in GGA-PBE, each silicon atom is modeled using the following electronic configuration Si:[Ne] $3s^2$ $3p^2$ as given in [29], where 92 valence bands where considered. We have chosen 20 empty bands for setting the conduction bands in both cases. For the unstrained state, Si₄₆ exhibits an indirect bandgap with semiconductor feature, where the valence band maximum (VBM) appears between M(1/2,1/2,0) and Γ(0,0,0) segment, whereas, the conduction band minimum (CBM) lies at the X(1/2,0,0) point. The band structure of Si₄₆ was investigated from theoretical point of view. So far, no experimental data is reported due to the difficulty of obtaining a guest free type-I Si₄₆ cages where silicon stabilize under diamond structure during synthesis. For the present calculated band structure, comparison with guest-containing clathrates (such as Na₈Si₄₆) is possible since all type-I clathrates obey the rigid-band model, which means that all those compounds will have similar allures of band structures and differ only in the Fermi level position and the bandgap magnitude, which is affected by the type of the guest atom [45]. In this work we report a quasi-direct band gap equal to $E_g$=1.364eV (GGA-PBE) and $E_g$=1.618eV (GGA-BLYP). It is well-known that the ground state DFT calculations have a tendency to underestimate the bandgap [56], however, our results are in fair agreement with previous theoretical data: $E_g$= 1.26eV [40], 0.9eV [45], and 1.315eV [57]. As illustrated in figure.2(a) and 2(b), band structures of unstrained Si₄₆ indicate that the valence band is subdivided to two major regions counting each 46 band: the lower valence band (LVB) between -11eV and -4eV, which is mainly formed by a large electronic contribution of the 3s- and small contribution of 3p-states of Si atoms. Whereas, the upper valence band (UVB between -3eV to 0eV) is formed by a large contribution from 3p-states and a very small contribution from 3s-states. The conduction band (CB) is dominated by the 3p-states of silicon atoms. Total and partial density of states DOS plot illustrated in figure.3, were also computed using regular GGA-PBE and hybrid GGA-BLYP functionals. Figure.3(a) (GGA-PBE) indicates that the Si-Si bonding within the system is covalent and comes from the contribution of $3p^2$ and $3s^2$ states forming strong ($sp^3$) hybridization, in agreement with the common electronic features of silicon based structures. Thus, figure.3(b) (GGA-BLYP) shows similar allure of total DOS and an extra electronic contribution from Si-d orbitals.

### III.2.Electronic properties under biaxial strain

In order to investigate the effect of the applied planar biaxial-strain on the electronic properties of $Si_{46}$ clathrate, electronic band structures were computed for each step of tensile and compressive biaxial strains ranging from -4% to +4%.The calculated bandgap magnitude versus biaxial-strain is illustrated in Figure.4. Under biaxial strain, magnitude of bandgap changes significantly where a maximum value of 1.395eV is reached at tensile strain of +1%, it starts to decrease for higher tensile strains, while, for compressive strains below 0%, it decreases significantly until reaching its minimum value of 0.935eV at -4%. Figure.5 depicts the electronic band structures for -1% (a), -2% (b), -3% (c), -4% (d) +1% (e), +2%(f), +3%(g) and +4%(h) strained $Si_{46}$. We notice from these figures that the bandgap nature remains quasi-direct for compressive strains. For $\Delta a/a_0 = -3\%$ and -4% the valence band maximum is located in the $\Gamma(0,0,0)$-R(0,1/2,1/2) high symmetry segment, and the conduction band minimum remains at the X point. For the unstrained and the $\Delta a/a_0 = -1\%$, -2%, +1% and +2% states, the VBM will transit to the segment between $\Gamma(0,0,0)$ and M(1/2,1/2,0) the bandgap remains indirect though and the CBM still at the X point. For tensile strains equal and superior to +3% the valence band maximum VBM shifts down from its previous position between $\Gamma$ and R, and appears at the X(1/2,0,0) point to coincide with the CBM leading to the transformation of the quasi-direct bandgap into a direct bandgap. For more insight Figure.6 exhibits the influence of the biaxial strain on the higher valence bands of the unstrained and +3% -3% strained $Si_{46}$. Figure.7 shows the variation of the total density of states as a function of the applied strain, it indicates the increasing of the magnitude with the decreasing of the strain condition.

![](./images/811139686364872705_4.jpg)

FIG.2: The calculated band structure of unstrained type-I silicon clathrate $Si_{46}$ using (a) GGA-PBE and (b) hybrid GGA-BLYP functionals with Castep and Dmol³ respectively. Valence band maximums VBM and Conduction band minimums CBM are indicated in red dots.

![](./images/811139686364872705_5.jpg)

FIG.3: The calculated total and partial density of states for unstrained type-I silicon clathrate $Si_{46}$ using (a) GGA-PBE and (b) hybrid GGA-BLYP functionals with Castep and Dmol³ respectively.

![](./images/811139686364872705_6.jpg)

FIG.4: Band gap magnitude as a function of biaxial strain for type-I $Si_{46}$ calculated using GGA-PBE and hybrid GGA-BLYP

![](./images/811139686364872705_7.jpg)

FIG.5: Electronic structures of strained $Si_{46}$: (a) -1%, (b) -2%, (c) -3%, (d) -4%, (e) +1%, (f) +2%, (g) +3% and (h) +4%. VBM and CBM points are indicated in colored circles. For strains (> +2%) the bandgap is direct @ X(1/2,0,0).

![](./images/811139686364872705_8.jpg)

FIG.6: Valence band maximum VBM of $Si_{46}$ as function of biaxial strain

![](./images/811139686364872705_9.jpg)

FIG.7: Influence of biaxial strain on the total density of states of type-I $Si_{46}$.

### III.3. Optical properties under biaxial strain

All optical properties of materials are quantified by means of the frequency-dependent complex dielectric function $\varepsilon(\omega)$,expressed as: $\varepsilon(\omega)=\varepsilon_{1}(\omega)+i\varepsilon_{2}(\omega)$, which represents the linear response of the system to an external electromagnetic excitation [58]. The imaginary part $\varepsilon_{2}(\omega)$, is computed from the momentum matrix elements taking all possible transitions between the occupied and unoccupied wave functions following the selection rules [59, 60] using the following formula:

$$
\varepsilon_{2}(\omega)=\left(\frac{2 e^{2} \pi^{2}}{m^{2} \omega^{2}}\right) \sum_{i j} \int\left\langle i|M| j\right\rangle^{2} f_{i}\left(1-f_{i}\right) \delta\left(E_{f}-E_{i}-\omega\right) d^{3} k
\tag{4}
$$

Where: $i$ and $j$ are the initial and final states, M represents the dipole matrix, $f_{i}$ is the Fermi distribution function for the $\mathrm{i}^{\text {th }}$ state and $\mathrm{E}_{\mathrm{i}}$ is the energy of the electron in this state.

The real part $\varepsilon_{1}(\omega)$ is extracted from the imaginary part through the following Kramers-Kronig formulation [59, 60]:

$$
\varepsilon_{1}(\omega)=1+\frac{2}{\pi} P \int_{0}^{\infty} \frac{\omega^{\prime} \varepsilon_{2}\left(\omega^{\prime}\right) d \omega^{\prime}}{\left(\omega^{\prime 2}-\omega^{2}\right)}
\tag{5}
$$

From the complex dielectric function, other important optical properties such as absorption coefficient $\alpha(\omega)$ can be extracted. In this context, we have computed using GGA-PBE the complex dielectric function and the absorption coefficient as a function of the incident light energy for each rate of biaxial strain. Figure.8 shows the calculated imaginary and real parts of the complex dielectric function for strained and unstrained $Si_{46}$ following two different polarizations, i.e. the (001) transversal polarization (parallel to c-axis) and (100) normal polarization (perpendicular to c-axis). The real part of the dielectric function is calculated and illustrated in Figure.8(a) and 8(b) following the (001) and (100) polarizations respectively. Results in Figure.8(a) are clearly enhanced for the -4% compressively-strained $Si_{46}$, the maximum peak is located at 2.5ev and the minimum is found at 4.5eV energy. Figure.8(b) shows better values for the +4% tensile-strained $Si_{46}$, and the extreme peaks appear at the same values of energies as precedent, hence, the three plots have similar shapes, and tend towards zero for higher energies. Figure.8(c) displays the imaginary part of the dielectric function calculated through the (001) plan. The -4% compressively-strained $Si_{46}$ shows the highest magnitude curve and the maximum peak appears at about 3.8eV energy, while the minimum magnitude is obtained for the +4% strained $Si_{46}$ at 3.2eV, the unstrained $Si_{46}$ shows a maximum peak at 3.5eV energy. For the imaginary part calculated through a polarization following the (100) plan illustrated in figure.8(d), it can be noticed that the +4% strained $Si_{46}$ reveals highest magnitude, while the lowest is obtained for the -4% strained state, this improvement is related to the direct nature of the band gap obtained for tensile strains above +3%.

Absorption coefficient is among the most relevant quantities to evaluate if the material of interest appears to be promising for optoelectronics, photonics or photovoltaic applications; it is directly derived from the dielectric complex function through the formula (6) [59]:

$$
\alpha(\omega)=\frac{2 k \omega}{c \hbar} \tag{6}
$$

Where: $\omega$ and $c$ represent the incident light frequency and the celerity of the light in vacuum respectively. Figure.9 shows the computed absorption coefficient for -4%, +4% and unstrained $Si_{46}$ as a function of energy following the (001) polarization plan, it is noticed that for the tensile biaxial strain of +4% in which the bandgap is direct, the absorption is higher than that of the unstrained or compressively-strained $Si_{46}$. For unstrained $Si_{46}$, the maximum peak appears at 4.81eV energy, the magnitude of the peaks decrease for the -4% state, while, for the +4% state, the major peak appears at 4.94eV and the general magnitude of absorption spectrum is increased by 17.5%. This improvement is directly attributed to the direct bandgap at +4%. The magnitude is at the order of $2.7x10^{4}$ in the visible range within the electromagnetic spectrum (1eV to 4eV). It is primordial to report that in spite of optical

transitions are expected to be forbidden in this class of materials according to [44, 61], turning the bandgap into direct through biaxial-strain approach might be a solution to overcome this shortage, therefore, this hypothesis needs to be confirmed through further investigations.

![](./images/811139686364872705_10.jpg)

FIG.8: GGA-PBE calculated dielectric function for type-I guest-free $Si_{46}$, the real part following (a) the (001), and (b) (100) plans, the imaginary part following (c) the (001) and (d) the (100) crystallographic plans

![](./images/811139686364872705_11.jpg)

FIG.9: Optical absorption as a function of energy of unstrained and strained Si46 along the (001) c-axis perpendicular plane

## IV. CONCLUSION

In summary, we have investigated by means of first-principles calculations the effect of planar biaxial-strain on electronic and optical properties of the type-I guest-free silicon clathrate $Si_{46}$. It was demonstrated that this material could exhibit a direct bandgap under tensile-strains above +2% with magnitudes of 1.381eV (GGA-PBE) or 1.623eV (GGA-BLYP). At this rate, optical properties are clearly enhanced with increasing values for the dielectric function as well as the optical absorption. The tensile biaxial strain of +2% corresponds to a substrate lattice constant of about a=10.40Å, an adequate substrate to exert this strain can be searched following a systematic study. This finding indicates that the material in question is advantageous for direct bandgap applications such as optoelectronic or photovoltaic devices. We wish this work would provide more perspectives of strain tunability of properties of clathrates regarding their use many technological applications.

## V. ACKNOWLEDGEMENTS

The authors wish to thank the "Laboratoire de Physique des Matériaux" at the Amar Télidji University of Laghouat-Algeria, for providing access to Castep software and workstations.

### References

1.  Ullah, S., et al., *Enhanced photocatalytic properties of core@shell SiO2@TiO2 nanoparticles*. Applied Catalysis B: Environmental, 2015. **179**: p. 333-343.
2.  Lee, J.-K., et al., *6" crystalline silicon solar cell with electron-beam melting-based metallurgical route*. Solar Energy, 2015. **115**: p. 322-328.
3.  Lei, P.-H., C.-T. Lin, and S.-J. Ye, *Improved efficiency of GaInP/(In)GaAs/Ge solar cells using textured liquid-phase-deposited (LPD) ZnO*. Journal of Physics D: Applied Physics, 2013. **46(12)**: p. 125105.
4.  Marlein, J., K. Decock, and M. Burgelman, *Analysis of electrical properties of CIGSSe and Cd-free buffer CIGSSe solar cells*. Thin Solid Films, 2009. **517(7)**: p. 2353-2356.
5.  Spalatu, N., et al., *Plasmonic effect of spray-deposited Au nanoparticles on the performance of CSS CdS/CdTe solar cells*. Applied Surface Science, 2015. **350**: p. 69-73.
6.  Botti, S., et al., *Low-energy silicon allotropes with strong absorption in the visible for photovoltaic applications*. Physical Review B, 2012. **86(12)**: p. 121204.
7.  Baranowski, L.L., et al., *Synthesis and optical band gaps of alloyed Si-Ge type II clathrates*. J. Mater. Chem. C, 2014. **2(17)**: p. 3231-3237.
8.  Kasper, J.S., et al., *Clathrate structure of silicon Na8Si46 and NaxSi136 (x< 11)*. Science, 1965. **150(3704)**: p. 1713-1714.
9.  Cros, C., M. Pouchard, and P. Hagenmuller, *Sur une nouvelle famille de clathrates minéraux isotypes des hydrates de gaz et de liquides. Interprétation des résultats obtenus*. Journal of Solid State Chemistry, 1970. **2(4)**: p. 570-581.
10. Akai, K., K. Koga, and M. Matsuura, *Electronic Structure and Thermoelectric Properties of Noble Metal Clathrates: Ba8M6Ge40(M = Cu, Ag, Au)*. Materials Transactions, 2007. **48(4)**: p. 684-688.
11. Koga, K., et al., *Electronic Structure and Thermoelectric Properties of Si-Based Clathrate Compounds*. Journal of Electronic Materials, 2009. **38(7)**: p. 1427-1432.
12. Connétable, D., et al., *Superconductivity in Dopedsp3Semiconductors: The Case of the Clathrates*. Physical Review Letters, 2003. **91(24)**.
13. Fukuoka, H., J. Kiyoto, and S. Yamanaka, *Superconductivity and crystal structure of the solid solutions of Ba8-δSi46-xGex (0⩽x⩽23) with Type I clathrate structure*. Journal of Solid State Chemistry, 2003. **175(2)**: p. 237-244.
14. Martinez, A.D., et al., *Synthesis of Group IV Clathrates for Photovoltaics*. Photovoltaics, IEEE Journal of, 2013. **3(4)**: p. 1305-1310.
15. Liu, L., et al., *Synthesis and thermoelectric properties of rare earth Yb-doped Ba8-xYbxSi30Ga16 clathrates*. Journal of Alloys and Compounds, 2014. **588**: p. 271-276.
16. Fukuoka, H., J. Kiyoto, and S. Yamanaka, *Synthesis and superconductivity of barium deficient type I silicon clathrate compounds, Ba8-xSi46*. Journal of Physics and Chemistry of Solids, 2004. **65(2-3)**: p. 333-336.
17. Imai, M., et al., *Synthesis of ternary Si clathrates in the A-Al-Si (A = Na and K) system*. Japanese Journal of Applied Physics, 2015. **54(7S2)**: p. 07JC02.
18. Ohashi, F., et al., *Thin-film formation of Si clathrates on Si wafers*. Journal of Physics and Chemistry of Solids, 2014. **75(4)**: p. 518-522.

19. Miao, L., et al., *Epitaxial growth of BaGa16Ge30 clathrate film on Si substrate by RF helicon magnetron sputtering with evaluation on thermoelectric properties*. Applied Surface Science, 2007. **254**(1): p. 167-172.

20. Narita, T., et al., *Preparation of NaSi thin films for the guest free Si clathrate thin films by heat resistance apparatus using NaSi target materials*. physica status solidi (c), 2010: p. NA-NA.

21. Kume, T., et al., *Thin film of guest-free type-II silicon clathrate on Si(111) wafer*. Thin Solid Films, 2016. **609**: p. 30-34.

22. Ungersboeck, E., et al., *The effect of general strain on the band structure and electron mobility of silicon*. Electron Devices, IEEE Transactions on, 2007. **54**(9): p. 2183-2190.

23. Hinsche, N.F., I. Mertig, and P. Zahn, *Effect of strain on the thermoelectric properties of silicon: an ab initio study*. J Phys Condens Matter, 2011. **23**(29): p. 295502.

24. Lee, H. and E.D. Jones, *Dielectric function of biaxially strained silicon layer*. Applied Physics Letters, 1996. **68**(22): p. 3153.

25. Hohenberg, P. and W. Kohn, *Inhomogeneous Electron Gas*. Physical Review, 1964. **136**(3B): p. B864-B871.

26. Kohn, W. and L.J. Sham, *Self-Consistent Equations Including Exchange and Correlation Effects*. Physical Review, 1965. **140**(4A): p. A1133-A1138.

27. Clark, S.J., et al., *First principles methods using CASTEP*. Zeitschrift für Kristallographie, 2005. **220**(5/6/2005): p. 567-570.

28. Delley, B., *An all-electron numerical method for solving the local density functional for polyatomic molecules*. J Chem Phys, 1990. **92**(1): p. 508-517.

29. Vanderbilt, D., *Soft self-consistent pseudopotentials in a generalized eigenvalue formalism*. Physical Review B, 1990. **41**(11): p. 7892.

30. Perdew, J.P., K. Burke, and M. Ernzerhof, *Generalized gradient approximation made simple*. Physical Review Letters, 1996. **77**(18): p. 3865.

31. Lee, I.-H. and R.M. Martin, *Applications of the generalized-gradient approximation to atoms, clusters, and solids*. Physical Review B, 1997. **56**(12): p. 7197-7205.

32. Monkhorst, H.J. and J.D. Pack, *Special points for Brillouin-zone integrations*. Physical Review B, 1976. **13**(12): p. 5188-5192.

33. Broyden, C.G., *The convergence of a class of double-rank minimization algorithms 1. general considerations*. IMA Journal of Applied Mathematics, 1970. **6**(1): p. 76-90.

34. Fletcher, R., *A new approach to variable metric algorithms*. The computer journal, 1970. **13**(3): p. 317-322.

35. Goldfarb, D., *A family of variable-metric methods derived by variational means*. Mathematics of computation, 1970. **24**(109): p. 23-26.

36. Shanno, D.F., *Conditioning of quasi-Newton methods for function minimization*. Mathematics of computation, 1970. **24**(111): p. 647-656.

37. Ouahrani, T., et al., *Ab-initio study of the structural, linear and nonlinear optical properties of CdAl2Se4 defect-chalcopyrite*. Journal of Solid State Chemistry, 2010. **183**(1): p. 46-51.

38. Becke, A.D., *Density-functional exchange-energy approximation with correct asymptotic behavior*. Physical Review A, 1988. **38**(6): p. 3098-3100.

39. Lee, C., W. Yang, and R.G. Parr, *Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density*. Physical Review B, 1988. **37**(2): p. 785-789.

40. San-Miguel, A. and P. Toulemonde, *High-pressure properties of group IV clathrates*. High Pressure Research, 2005. **25**(3): p. 159-185.

41. He, Y., et al., *Si-based Earth abundant clathrates for solar energy conversion*. Energy & Environmental Science, 2014. **7**(8): p. 2598.

42. Kahn, D. and J. Ping Lu, *Structural properties and vibrational modes of $\{\mathrm{Si}\}_{34}$ and $\{\mathrm{Si}\}_{46}$ clathrates*. Physical Review B, 1997. **56**(21): p. 13898-13901.

43. Perottoni, C.A. and J.A.H.d. Jornada, *The carbon analogues of type-I silicon clathrates.* Journal of Physics: Condensed Matter, 2001. **13**(26): p. 5981.

44. Saito, S. and A. Oshiyama, *Electronic structure ofSi46andNa2Ba6Si46.* Physical Review B, 1995. **51**(4): p. 2628-2631.

45. Kurganskii, S.I., N.A. Borshch, and N.S. Pereslavtseva, *Electronic structure and spectral properties of Si46 and Na8Si46 clathrates.* Semiconductors, 2005. **39**(10): p. 1176-1181.

46. Norouzzadeh, P., C.W. Myles, and D. Vashaee, *Prediction of a large number of electron pockets near the band edges in type-VIII clathrate Si46 and its physical properties from first principles.* J Phys Condens Matter, 2013. **25**(47): p. 475502.

47. Menon, M., E. Richter, and K. Subbaswamy, *Structural and vibrational properties of Si clathrates in a generalized tight-binding molecular-dynamics scheme.* Physical Review B, 1997. **56**(19): p. 12290.

48. Moriguchi, K., et al., *Electronic structures of Na 8 Si 46 and Ba 8 Si 46.* Physical Review B, 2000. **61**(15): p. 9859.

49. Moewes, A., et al., *Electronic structure of alkali-metal-dopedM8Si46(M=Na,K)clathrates.* Physical Review B, 2002. **65**(15).

50. Connétable, D., *First-principles calculations of carbon clathrates: Comparison to silicon and germanium clathrates.* Physical Review B, 2010. **82**(7).

51. Moriguchi, K., et al., *Empirical potential description of energetics and thermodynamic properties in expanded-volume silicon clathrates.* Physical Review B, 2001. **64**(19).

52. Kitano, A., et al., *Structural properties and thermodynamic stability of Ba-doped silicon type-I clathrates synthesized under high pressure.* Physical Review B, 2001. **64**(4).

53. Yang, C.H., et al., *Dependence of electronic properties of germanium on the in-plane biaxial tensile strains.* Physica B: Condensed Matter, 2013. **427**: p. 62-67.

54. Ghosh, C.K., et al., *Electronic structure and optical properties of CuAlO2 under biaxial strain.* J Phys Condens Matter, 2012. **24**(23): p. 235501.

55. Liou, B.-T. and Y.-K. Kuo, *Effect of biaxial strain on the band gap of wurtzite Al x Ga1−x N.* Applied Physics A, 2012. **106**(4): p. 1013-1016.

56. Imai, Y. and M. Imai, *Chemical trends of the band gaps of idealized crystal of semiconducting silicon clathrates, M8Si38A8 (M=Na, K, Rb, Cs; A=Ga, Al, In), predicted by first-principle pseudopotential calculations.* Journal of Alloys and Compounds, 2011. **509**(9): p. 3924-3930.

57. Imai, Y. and A. Watanabe, *Chemical trends of the band gaps in semiconducting silicon clathrates.* Physics Procedia, 2011. **11**: p. 59-62.

58. Korba, S.A., et al., *First principles calculations of structural, electronic and optical properties of BaLiF3.* Computational Materials Science, 2009. **44**(4): p. 1265-1271.

59. Nath, P., et al., *Ab-initio calculation of electronic and optical properties of nitrogen and boron doped graphene nanosheet.* Carbon, 2014. **73**: p. 275-282.

60. Liu, Q.-J., et al., *Structural, mechanical, electronic, optical properties and effective masses of CuMO2 (M = Sc, Y, La) compounds: First-principles calculations.* Solid State Sciences, 2014. **31**: p. 37-45.

61. Connétable, D., *Structural and electronic properties ofp-doped silicon clathrates.* Physical Review B, 2007. **75**(12).

### Highlights

- Systematic investigation of the effect of biaxial strain on the electronic and optical properties
- First principles calculations in the frame of density functional theory DFT were employed.
- Biaxial strain was applied through a biaxial strain tensor and lattice mismatch formulas.
- A direct band gap was found in tensile strains above +3%.
- Calculation of electronic band structure for unstrained and strained $Si_{46}$ clathrate.
- Calculation of optical properties for unstrained and strained Si46 clathrate.