# Modeling for Structural Engineering and Synthesis of Two- Dimensional WSe₂ Using a Newly Developed ReaxFF Reactive Force Field

Nadire Nayir, Yuanxi Wang, Sharmin Shabnam, Danielle Reifsnyder Hickey, Leixin Miao, Xiaotian Zhang, Saiphaneendra Bachu, Nasim Alem, Joan Redwing, Vincent H. Crespi, and Adri C. T. van Duin*

Cite This: https://dx.doi.org/10.1021/acs.jpcc.0c09155
Read Online

ACCESS | Metrics & More | Article Recommendations | Supporting Information

**ABSTRACT:** Atomistic simulation techniques have become an indispensable tool to acquire a fundamental understanding of growth and structural characteristics of two-dimensional (2D) materials of interest, thereby accelerating experimental research in the same field. A new ReaxFF reactive force field presented here is the first comprehensive empirical potential that is explicitly designed to capture the most prominent features of 2D WSe₂ solid-phase chemistry, such as defect formation as a function of local geometry and chalcogen chemical potential, vacancy migration and phase transition, thus enabling cost-effective and reliable characterization of 2D WSe₂ at large length scales and time scales much longer than what is accessible by first-principles theory. This potential, validated using extensive first-principles energetics data on both periodic and nonperiodic systems and experimental measurements, can accurately describe the mechanochemical coupling between monolayer deformations and vacancy energetics, providing valuable atomistic insights into the morphological evolution of a monolayer in different environments in terms of loading conditions and various concentrations and distributions of defects. Since understanding how growth is affected by the local chemical environment is vital to fabricating efficient and functional atomically thin 2D WSe₂, the new ReaxFF description enables investigations of edge-controlled growth of single crystals of 2D WSe₂ using reactive environments closely matching experimental conditions at a low computational cost.

![](./images/812528762917748737_1.jpg)

## INTRODUCTION

Atomically thin layered transition metal dichalcogenides (TMDs) (i.e., WSe₂, MoSe₂, MoS₂, WS₂) offer immense potential for next-generation electronic and optoelectronic devices due to their tunability toward desirable functionalities.¹⁻⁶ Structural engineering strategies can help bridge the gap between properties and performance in TMDs and thus facilitate the creation of new high-performance devices. For example, the electronic configuration of d-orbitals in TMDs dominates their electrical conductivity, e.g., the 2H phase of TMDs is semiconducting while the 1T phase is metallic due to differing degeneracies of their d-orbitals. Phase engineering in TMDs is a powerful method to modulate the electronic properties of TMDs and thus enhances device performance in applications such as hydrogen evolution and optoelectronics.⁷⁻¹¹ Defect engineering attracts similar interest, since vacancies, antisites, adatoms, and ripples in atomically thin structures can strongly influence material properties. For example, ripplocations (described by Kushima et al.¹²), which are unique to van der Waals layers, have intriguing prospects for applications such as sweeping out undesirable defects,¹³ while point defects at the surface or edge could selectively promote vertical or lateral growth by generating active sites for gas-phase precursors to bind.¹⁴,¹⁵ The growth of TMD flakes is strongly modulated by the stability and configuration of their edges as a function of the local chemical environment, suggesting routes toward using edge engineering to control growth outcomes.¹⁶⁻²¹ Atomically thin TMDs are also promising candidates for strain engineering, since they sustain larger elastic strains than their bulk counterparts, and these can drastically modify band gaps, an effect of great interest for optoelectronic devices.²²,²³

Received: October 8, 2020
Revised: November 30, 2020

![](./images/812528762917748737_2.jpg)

© XXXX American Chemical Society
A
https://dx.doi.org/10.1021/acs.jpcc.0c09155
J. Phys. Chem. C XXXX, XXX, XXX−XXX

![](./images/812528762917748737_3.jpg)

Figure 1. Flowchart illustrating the workflow in constructing ReaxFF force fields.

Despite significant scientific interest and progress in TMD fabrication, the synthesis of large-scale, defect-free TMD materials with controllable thickness is still challenging. As such, there is a need for atomistic simulations that can accurately model TMD growth, thus prompting the development of empirical potentials that can enable large-scale simulations of TMDs at much lower computational costs than first-principles density functional theory (DFT) methods. $^{24,25}$ To date, several potentials have been proposed for 2D WSe$_{2}$. $^{26-30}$ The Stillinger−Weber (SW) potential was first developed by Norouzzadeh et al. $^{26}$ to study the thermal properties of 2D WSe$_{2}$. Mobaraki et al. $^{27}$ reported that this potential models the WSe$_{2}$ thermal conductivity less accurately than earlier DFT studies; therefore, they developed a new SW-type parameter set by fitting against a DFT-based training set of structural (lattice constants and interatomic bond distances), mechanical (elastic constants, Young's modulus, Poisson's ratio), and thermal (phonon frequencies) properties for single-layer WSe$_{2}$. Jiang et al. $^{28}$ proposed a distinct SW potential framework where parameters are analytically derived from a valence force field (VFF) model. The simple form of the SW potential enables fast numerical simulations of thermal and elastic properties. These SW-based potentials focus on lattice, elastic, and phonon properties of 2D WSe$_{2}$; however, they were not trained to reproduce bond formation and dissociation. Recently, a reactive REBO potential$^{29}$ was developed for Mo−W−Se−S interatomic interactions to model MoS$_{2}$−WSe$_{2}$ and WS$_{2}$−WSe$_{2}$ heterostructures. This REBO potential describes the dependence of interatomic separations on the local environment and thus allows covalent bond rupture and formation. However, it was trained against only the lattice parameters of WSe$_{2}$ (at the DFT level) and thus was not explicitly designed to capture the fundamentals of WSe$_{2}$ solid-phase chemistry such as phase transitions, defect formation, and vacancy migration. Recently, Xuan et al. $^{30}$ developed a multiscale framework that combines the ReaxFF reactive force field with continuum fluid dynamics to describe the kinetics of WSe$_{2}$ derived from gas-phase precursors W(CO)$_{6}$ and H$_{2}$Se (as in MOCVD growth) but without considering the surface interactions and solid-phase properties of 2D WSe$_{2}$, which come to the force once gas-phase species impinge on the substrate surface.

Here, we present an extended ReaxFF reactive force field that enables large-scale simulations of defect-, phase-, strain-, and edge engineering of 2D WSe$_{2}$ in a realistic reactive environment at a low computational cost. The potential parameters were fit to an extensive first-principles data set, including both periodic and nonperiodic systems. We subsequently tested the capability and transferability of the new potential by comparing to experimental measurements and DFT calculations, which are the post-training data set, thus providing validation for ReaxFF transferability. We computed the energy barriers against 2H → 1T phase transition and vacancy migration along with the formation energies of point defects as a function of the chalcogen chemical potential. The coupling of vacancies to ripplocations during the structural deformation of a WSe$_{2}$ monolayer was studied, as were the mechanical properties of pristine and defective WSe$_{2}$ under tensile strain. We further employed the potential to calculate the edge formation energies of WSe$_{2}$ nanoribbons with varying Se coverages depending on the local chemical environment and examined the interplay between kink nucleation and edge type. To the best of our knowledge, this new potential presents the first comprehensive computational tool describing the most prominent features of pristine and defect-free 2D WSe$_{2}$ and also its growth kinetics under varying conditions.

### METHODS

#### ReaxFF Force Field.
The ReaxFF reactive force field developed by van Duin et al. $^{31}$ is a bond-order-dependent potential that captures covalent bond breaking and formation by updating the bond order at each MD iteration. This force field allows large-scale reactive chemical systems and includes van der Waals interactions, which permits simulation of multilayer van der Waals hetero- and homostructures. ReaxFF differs from the previous reactive force fields such as the Tersoff$^{32}$ and Brenner$^{33,34}$ potentials by applying a significantly longer-ranged bond order relationship, which makes it possible to achieve more precise reaction kinetics. The ReaxFF framework has been successfully applied to many 2D systems, such as MoS$_{2}$, $^{35-37}$ MXenes, $^{38-41}$ h-BN, $^{42,43}$ and graphene. $^{44}$ A comprehensive description of ReaxFF formalism can be found in the study by Chenoweth et al. $^{45}$

#### Parametrization of ReaxFF Force Field.
The workflow followed during the force field optimization is discussed in the following sections, as illustrated in Figure 1

#### DFT Calculations.
Nonperiodic quantum mechanical calculations were performed using Jaguar$^{46}$ with the B3LYP functional and the LACV3P***++ effective core potential. Cell optimization and strain calculations based on the volumetric expansion/compression of condensed phases were conducted

![](./images/812528762917748737_4.jpg)

Figure 2. Structural properties of 2H-WSe₂ computed based on ReaxFF and DFT. (a) Top and (b) side views of the optimized 2H-WSe₂ monolayer and bilayer structures, respectively. (c) Structural constants of a 2D WSe₂ monolayer (ML) and bilayer (BL). (d, e) Equations of state of a 2H-WSe₂ ML and BL under uniaxial and biaxial compression and expansion.

using the Vienna ab initio simulation package (VASP).⁴⁷ In these calculations, the electron−ionic core interactions were represented using a projected augmented potential,⁴⁸,⁴⁹ and exchange−correlation effects were treated using the Perdew−Burke−Ernzerhof parametrization of the generalized gradient approximation functional.⁵⁰,⁵¹ A Γ-centered Monkhorst-Pack (20×20×1) K-point mesh for a WSe₂ unit cell was applied to Brillouin zone integration with a plane-wave expansion energy cutoff of 500 eV. In geometry optimizations, the system was allowed to relax fully with an electronic loop threshold of 0.1 meV and a force relaxation threshold of 0.02 eV/Å. Gaussian smearing was used with a broadening of 0.05 eV, and van der Waals interactions were treated using the semiempirical correction of Grimme (zero damping DFT-D3)⁵² since PBE combined with DFT-D3 van der Waals corrections, has been proven to be a reliable scheme to yield the correct interlayer spacings,⁵³ where van der Waals interactions are appropriately accounted for. A vacuum layer of 20 Å was inserted normal to the monolayers/bilayers to minimize spurious interactions of periodic repetitions. Energy barriers were calculated by the climbing image nudged elastic band (CI-NEB) method.

Force Field Parametrization. Training data set taken from ref 30 includes the energy profiles of W−SeH, W = Se, and H− Se bond dissociation and HSe−W−SeH, Se = W−SeH, Se = W = Se, and H−Se−H angle bending in several small molecules (Figures S1−S3). This training set also contains the reaction energies of the W−Se−H compounds (Table S1). As summarized in Figure 1, we further expand the data set with periodic DFT calculations for the energetics of monolayer and bilayer WSe₂ under uniaxial and biaxial expansion/compression (Figure 2), the energy−volume equation of state of bcc-W (Figure S4), formation energies of bulk Se- and W-allotropes, vacancy defect energies in bulk bcc-W (Tables S2 and S3), formation energies of defective and defect-free ripplocations with varying buckling heights, and the excess edge energies of WSe₂ nanoribbons with different Se coverages. We then optimized the W/Se/H force field against the rich DFT data set by starting from the force field parameter set of a previous study:³⁴ W and Se atom, W−W, Se−Se, W−Se, and H−Se bonds; H−Se and W−Se off-diagonal; and H−Se−H− and W− Se-related valence angle parameters. As seen in Figures S1−S3, the energy curves derived from ReaxFF and DFT for bond dissociation and bond angle bending show good agreement, and ReaxFF also successfully reproduces DFT-based enthalpies of various chemical reactions displayed in Table S1. The equations of state of WSe₂ and W crystals (Figures 2 and S4) and heats of formation of W and Se crystals (Tables S2 and S3) generated by ReaxFF show reasonable agreement with the DFT values. The parameters of the new ReaxFF force field are presented in the Supporting Information. As described below, we employed and validated the newly developed force field through molecular dynamics (MD) simulations of solid-state 2D WSe₂ using ReaxFF/ADF⁵⁴ and LAMMPS,⁵⁵ visualized with OVITO⁵⁶ and VESTA.⁵⁷

## RESULTS AND DISCUSSION

Structural Properties of a Freestanding WSe₂ Monolayer. WSe₂ natively exists in the 2H-crystal configuration in which each transition metal is trigonally-prismatically coordinated by six chalcogen atoms, creating a sandwich structure where a central metal monolayer lies between two Se layers (Figure 2a,b). As seen in Figure 2c, the ReaxFF-based equilibrium lattice parameters of a 2H-WSe₂ monolayer are $a = 3.29$ Å, $\gamma = 120^\circ$, and $\text{d}_{\text{W-Se}} = 2.57$ Å at the minimum of the equation of state (Figure 2d,e), in good agreement with the DFT values of $a = 3.30$ Å, $\gamma = 120^\circ$, and $\text{d}_{\text{W-Se}} = 2.55$ Å. The Se, $\text{d}_{\text{Se-Se}}$, and W, $\text{d}_{\text{W-W}}$, bond distances within the ReaxFF framework are predicted as being equal to 3.29 Å with a slight shift of 0.06 Å from the DFT numbers. The in-plane ($\text{I}_{\text{Se-Se}}$) and interlayer ($\text{h}_{\text{Se-Se}}$) Se−Se and the interlayer W−W vertical separations ($\text{h}_{\text{W-W}}$) are computed as 3.41, 3.09, and 6.52 Å, in reasonable agreement with the DFT values of $\text{I}_{\text{Se-Se}} = 3.63$ Å, $\text{h}_{\text{Se-Se}} = 2.90$ Å, and $\text{h}_{\text{W-W}} = 6.52$ Å. ReaxFF predicts the nominal thickness of a 2H-WSe₂ monolayer (i.e., $\text{I}_{\text{Se-Se}} + \text{h}_{\text{Se-Se}}$) within 0.03 Å of the DFT value for 6.53 Å.

Phase Transition between Metallic and Semiconduc- ing WSe₂ Monolayers. WSe₂ exhibits different crystal phases with distinct structural and electronic properties. The thermodynamically favorable semiconducting 2H phase and the metastable metallic 1T phase in octahedral coordination are both possible for a WSe₂ monolayer,³,⁵⁷,⁵⁸ with a different spatial arrangement of Se atoms covalently bound to W. Recent theoretical studies show that phase transitions between them can be realized via either collective atomic displacements⁶⁰ or

![](./images/812528762917748737_5.jpg)

Figure 3. 1T → 2H phase transition. Top and cross-sectional views of (a) the 1T phase, (b) the transition state (TS), and (c) the 2H phase. (d) Transition pathway between the metallic 1T and semiconducting 2H phases of WSe₂ at ReaxFF and DFT levels. The relative energies with respect to the 2H phase within ReaxFF and DFT are indicated in black and red font colors, respectively.

the gliding of an intralayer metal and/or chalcogen atomic planes.⁶⁰,⁶¹ Using in situ electron microscopy, Lin et al.⁶² also propose that the experimentally observed 2H/1T phase transition in a MoS₂ monolayer involves the latter mechanism, i.e., gliding of atomic planes.

To validate our new ReaxFF potential, we first investigated the formation and stability of the semiconducting 2H and metallic 1T phases. ReaxFF predicts that 2H is the thermodynamically stable phase, as predicted by our DFT calculations and reported in previous theoretical studies.³,⁵⁸,⁵⁹ The formation energy of the 2H phase is −1.25 eV within ReaxFF, in good agreement with the DFT value of −1.26 eV. ReaxFF predicts the formation energy of the 1T phase to be −0.58 eV, reasonably close to the DFT value of −0.51 eV.

We computed the minimum energy pathway (MEP) for the 1T → 2H transition at ReaxFF and DFT levels (Figure 3d). Following the experimentally proposed mechanism,⁶² we generated five images between two local minima of a potential energy surface along the MEP by gliding Se atoms only on the upper layer of 2H-WSe₂, as depicted in Figure 3a−c. We then optimized the structures until the maximum norm of force acting on each replica was smaller than 0.05 eV/Å within a climbing image scheme at the DFT level using VASP⁴⁷ and using ReaxFFAMS software⁵⁴ at the force field level. As illustrated in Figure 3d, the new ReaxFF potential provides a reasonable description of the transition pathway from the 1T to 2H phase. The ReaxFF energy barrier for this transition is 0.63 eV, in reasonable agreement with the DFT value of 0.71 eV. The reverse energy barrier for the 2H → 1T phase transition is 1.30 eV within ReaxFF, which is 0.16 eV lower than the DFT prediction.

Point Defects in WSe₂ Monolayers. Despite the great extent of recent studies,⁶³⁻⁶⁶ there is still no reactive potential that is trained specifically for defective structures to enable cost-effective and reliable characterization of defective WSe₂ at large length scales and time scales. Our new reactive potential is trained against DFT formation energies for various point defects in a freestanding WSe₂ monolayer to meet the needs and interests of the 2D community. The seven representative defect models that were identified and characterized in previous studies⁶⁴,⁶⁷ were generated as follows: V_Se, one Se atom was detached from a WSe₂ sheet; V_2Se corresponds to a double (stacked) Se vacancy; and V_W is a single W vacancy. For the V_WSe3 model, one W and three adjacent Se atoms were removed, while V_WSe6 represents the absence of a W and all six neighboring Se atoms. For the antisite models, W_2Se corresponds to the replacement of one W atom by a Se₂ dimer, while 2Se_W refers to a Se₂ dimer substituted by a W atom. The defect structures were each introduced into a pristine 6×6 WSe₂ supercell containing 108 atoms (72 Se, 36 W) of dimensions 14.76×14.76×20 Å³. The atomic configurations of the optimized models at DFT and ReaxFF levels and the corresponding formation energies computed using eq 1 are illustrated in Figures S5 and 4.

$$
E_{\mathrm{f}}^{\text {defect }}=E^{\text {defective }}-E^{\text {pristine }}+n_{\mathrm{Se}} \mu_{\mathrm{Se}}+n_{\mathrm{W}} \mu_{\mathrm{W}} \tag{1}
$$

![](./images/812528762917748737_6.jpg)

Figure 4. Formation energies of point defects observed in 2D WSe₂ at ReaxFF and DFT levels.

where $E^{\text{defective}}$ and $E^{\text{pristine}}$ are the total energies of defective and pristine freestanding monolayers, respectively, $\mu_{\mathrm{W}}$ and $\mu_{\mathrm{Se}}$ are the total energies of W and Se atoms in the bulk form of bcc-W and $\alpha$-Se crystals, respectively ($\mu_{\mathrm{W}} = 8.06$ eV and $\mu_{\mathrm{Se}} = 2.37$ eV within ReaxFF), and $\mathrm{n_{Se}}$ and $\mathrm{n_{W}}$ are the number of Se and W atoms, respectively, removed from a WSe₂ monolayer.

As seen in Figure 4, ReaxFF and DFT energies exhibit a good overall qualitative and quantitative agreement. Both DFT and ReaxFF predict that V_Se is the most stable defect type in a WSe₂ monolayer under the chemical potentials chosen above, as reported in an earlier study,⁶⁸⁻⁷¹ the other defect types being substantially less stable.⁶⁴,⁶⁵

To show the local strains associated with point defects, Figure 5a−c presents the atomic configurations and the ReaxFF- and DFT-based bond displacement maps of V_Se, V_2Se, and V_w defects in a WSe₂ layer. Both ReaxFF and DFT predict that the loss of chalcogen in the V_Se and V_Se2 models drives bond contraction between adjacent W atoms, reducing W−W distances by ∼15% and ∼24%, respectively, as the unsaturated W atoms marked by red triangles radially contract toward the chalcogen vacancy sites. These strain effects are also observed in experiments; Figure 5d shows high-angle annular dark-field scanning transmission electron microscopy (HAADF-STEM) images of V_Se and V_Se2 defects with overlaid maps of distances between neighboring W atoms. These maps were created by fitting each atomic position with a two-dimensional Gaussian function and plotting distances between atom centers. The distances between three W atoms adjacent to the V_Se and V_Se2 sites are contracted

![](./images/812528762917748737_7.jpg)

Figure 5. Point defects in a 2D WSe₂ ML. (a) Ball-stick representations and (b, c) W−W bond displacement maps of V-Se, V-Se₂, and V-W point defects based on ReaxFF and DFT methods. (d) HAADF-STEM images with overlaid maps of the distances between neighboring W atoms of V-Se and V-Se₂. The vacancies are marked by dotted white circles.

![](./images/812528762917748737_8.jpg)

Figure 6. (a, b) DFT and ReaxFF formation energies of the vacancy defects as a function of $\Delta\mu_{Se}$, where $\Delta\mu_{Se} = \mu_{Se(bulk)} - \mu_{Se}$, and Se-rich and W-rich correspond to $\mu_{Se(bulk)}$ and $\mu_{W(bulk)}$, respectively. (c) Reaction pathway of Se-vacancy-mediated diffusion based on ReaxFF and DFT.

by approximately 10 and 18%, respectively, in good agreement with the ReaxFF and DFT results. Our ReaxFF and DFT calculations also show that $V_{w}$ defect induces ~25% dilation in the distance between the W atoms neighboring the point defect (Figure 5b,c).

We next examined the stability of different vacancy defects as a function of the Se chemical potential $\mu_{Se}$ within ReaxFF and DFT, as depicted in Figure 6a,b, where the accessible range, $\mu_{WSe2}-\mu_{W(bulk)}/2 < \mu_{Se} < \mu_{Se(bulk)}$, is determined by the equation $\mu_{WSe2} = 2\mu_{Se} + \mu_{W} = 2\mu_{Se(bulk)} + \mu_{W(bulk)} + \Delta H_{WSe2}$ that satisfies the thermodynamic equilibrium condition, and $\Delta H_{WSe2}$ for ReaxFF is −1.25 eV, in good agreement with the DFT value of −1.26 eV. Figure 6a,b shows that the ReaxFF energies fall in reasonable agreement with the DFT values. The single Se- vacancy defect is the most abundant defect in a WSe₂ ML, with the lowest formation energy under all growth conditions from Se-rich to W-rich (and being most favorable in a W-rich environment), consistent with the growth of high-quality WSe₂ MLs in chalcogen-rich environments.⁷²,⁷³

To assess the mobility of the Se-vacancy defects in a monolayer, we performed NEB calculations for the $V_{Se}$ migration based on ReaxFF and DFT and computed the associated activation energies (Figure 6c). ReaxFF correctly produces the geometry of the transition state with an energy barrier of 2.55 eV, in close agreement with the DFT value of 2.45 eV.

Coupling of Bending to Se Vacancy Defects in a WSe₂ Monolayer. Recent studies¹²,³⁵,⁷⁴⁻⁷⁶ have explored the formation of ripplocations in 2D layers in response to mechanical loading. Ripplocation as described by Kushima et al.¹² is a line defect in a 2D material through buckling of surface layers into ripples that are registered to crystallographic dislocations. Ostadhossein et al.³⁵ and Tritsaris et al.⁷⁴ show how the formation of chalcogen vacancy defects can be regulated by the curvature of ripplocations, with such defects being most stable on surfaces with higher curvature, which suggests that coupling of buckled surfaces with vacancy defects may be able to sweep out defects from selected regions, if ripplocations can be mobilized.¹³ Ripples in MoS₂¹²,³⁵,⁷⁴ and graphite¹³,⁷⁶ layers have been reported previously; ripplocations in a WSe₂ ML are studied for the first time in this work. To capture the mechanochemical coupling between monolayer deformations

![](./images/812528762917748737_9.jpg)

Figure 7. (a) Initial configuration of the defective system including two Se vacancies on the top and bottom layers of a flat WSe₂ ML. (b) Optimized configuration of the defective system with the formation energies of 4.73 and 4.74 eV referencing the energy of a flat and pristine WSe₂ at ReaxFF and DFT levels, respectively, where the existence of vacancies drives the formation of two ripples with opposite signs in a monolayer. (c) Formation energies of the single vacancy (Vₛₑₜ (red circles) and Vₛₑᵦ (green circles)) in a WSe₂ ripplocation with a buckling height of 12.9 Å as a function of distance away from the ripplocation center.

![](./images/812528762917748737_10.jpg)

Figure 8. Ripplocation and vacancy coupling effect on the structural deformation of a WSe₂ ML. Optimized configurations of (a) a pristine and flat WSe₂ ML, R₀, and (b−e) four representative defect-free, R₁, R₂, R₃, and R₄, and (f−j) defective, R₁-vac, R₂-vac, R₃-vac, and R₄-vac, WSe₂ ripplocations, with two Se vacancies on the top and bottom layers of each model. (k, m) Formation energies of pristine, Eᵣᵢₚₚf, and defective, Eᵣᵢₚₚ₋ᵥₐc, ripplocations and the vacancy formation, Eᵥₐc, in each defective ML as a function of the buckling height, Δh. Note that the total energies of the pristine models are taken as the reference energy in the vacancy formation energy calculations.

and defect energetics, the new ReaxFF potential was trained against the DFT energies of pristine and defective ripplocations with variable buckling heights $\Delta h$, defined as the distance (normal to the undeformed monolayer plane) between the two most distant W atoms in the upper and lower layers of a rippled WSe₂ ML.

We applied our potential to examine first the effect of vacancy defects on the formation of ripplocations by creating two isolated Se-vacancy defects on the top (Vₛₑₜ) and bottom (Vₛₑᵦ) Se layers of a pristine flat WSe₂ (Figure 7a). Upon structural relaxation, the two isolated vacancies drove the formation of two out-of-plane ripples of opposite orientation by splitting the double-stacked Se atoms with the energy of 4.73 eV within ReaxFF, showing an excellent fit with the DFT value of 4.74 eV, that is, the energy required for the formation of two isolated vacancies in a pristine and flat WSe₂ (Figure 7b). Vacancies occupy highly curved concave surfaces where single vacancy formation is thermodynamically favored, as shown in Figure 7c.

The Se vacancy requires lower energy to form on highly curve concave surfaces and correspondingly higher energies on highly curved convex surfaces, in good agreement with the previous study on MoS₂.³⁵,⁷⁴³⁵,⁷⁴ Note that the ReaxFF and DFT formation energies, $E_{\text{vac}}$, of vacancies in a flat (Figure 7b) and buckled WSe₂ monolayer (Figures 7c and 8b,f−j) were computed using eq 1.

To separate the energetic contributions of the Se vacancy and the ripplocation to the structural deformation of a WSe₂ ML, four defect-free representative models with varying buckling heights (R₁ to R₄, depicted in Figure 8b−e) were generated by compressing a flat pristine R₀ (Figure 8a) laterally (along a zigzag direction) by 21.9, 33.6, 40.1, and 45.3%. Each model consists of an AB-stacked WSe₂ monolayer with 24×1 unit cells with 15 Å of vacuum along the z direction to avoid spurious interactions between periodic repetitions. To generate four representative models with defects, R₁-vac to R₄-vac (Figure 8g−j), a pair of Se atoms were removed from the concave region of

![](./images/812528762917748737_11.jpg)

Figure 9. (a) Stress and (b) strain energy density as a function of uniaxial strain along the ZZ and AC directions for pristine and defective sheets with VSe and VSe2 (enclosed with dashed black circles) at 300 K. Atomic representations of (c) the pristine and (d) VSe- and (e) VSe2-defective monolayers.

<table>
<thead>
<tr><th colspan="11">Table 1. Experimental, ReaxFF, and DFT Elastic Constants of Pristine 2H-WSe2 a</th></tr>
<tr><th rowspan="2">method</th><th colspan="2">current study<br>ReaxFF</th><th colspan="3">ref a</th><th>ref b</th><th>ref c</th><th>ref d</th><th rowspan="2">ref e<br>experiment for 5 Layers</th></tr>
<tr><th>ZZ</th><th>AC</th><th>PBE</th><th>LDA</th><th>optB88</th><th>PBE-GGA</th><th>GGA-PBE</th><th>GGA-PBE</th></tr>
</thead>
<tbody>
<tr><td>Ys (GPa)</td><td>218</td><td>209</td><td>114.4</td><td>132.8</td><td>118.2</td><td>116</td><td>151.92</td><td>201.5</td><td>170 ± 7</td></tr>
<tr><td>υ</td><td>0.65</td><td>0.39</td><td>0.19</td><td></td><td></td><td>0.19</td><td>0.19</td><td>0.13</td><td></td></tr>
</tbody>
<tfoot>
<tr><td colspan="11">aRef a,83 Ref b,82 Ref c,82 Ref d,81 and Ref e.77</td></tr>
</tfoot>
</table>

highest curvature, i.e., the thermodynamically favored regions, on the top and bottom Se layers of each defect-free ML presented in Figure 8b−e. After the structural relaxation of the eight models, the pristine and defective ripplocation formation energies were computed within ReaxFF and DFT (Figure 8k,m), referencing the energies of the flat and pristine, Ro (Figure 8a), and flat-defective, Ro-vac (Figure 8f), systems, respectively, using the chemical potential of bulk α-Se for the comparisons involving vacancy defects. The computational details are presented under the section of "Ripplocations" in the Supporting Information.

Figure 8k,m summarizes the energy contributions of vacancies and pristine ripplocations (Figure 8b−e) to the formation of the resulting defective structures (Figure 8f−j) as a function of the buckling height Δh where ReaxFF and DFT energies are in good agreement. Ro-vac shows ripples without lateral compression; their sharpness relates to local bond angle deformations induced in the immediate vicinity of the vacancy defect (really a line of such defects). The energy of pristine ripplocations increases while the formation energies of vacancies decrease with increasing buckling height, resulting in the thermodynamically more favored defective ripplocations than the pristine ones (Figure 8k,m), suggesting that such impurities can be utilized to stabilize buckled structures by modulating the strain energy. Moreover, the vacancy formation energy is negative on the ripplocations with sufficiently higher curvature, indicating that a highly curved ripplocation is a favorable host for vacancy defects under thermodynamic equilibrium conditions and conversely that ripplocations tend to form in defective structures, suggesting that they can open a venue for sweeping out undesirable defects such as vacancies from 2D WSe2.

Elastic Properties of Freestanding 2H-WSe2. In this section, we investigated the in-plane stiffness of 2D WSe2 by applying uniaxial strain along zigzag and armchair directions (Figure 9). To this end, we constructed an atomic model consisting of 360 atoms in a 3.3 × 3.4 nm simulation box with a 20 Å vacuum buffer layer normal to the WSe2 sheet. After a conjugate gradient energy minimization with a tolerance of 10−6 eV, we relaxed and equilibrated the system at 300 K in an NPT ensemble for 1 ns, with temperature and pressure damping parameters of 100 and 5000 fs, respectively, to further relax residual stress. We then applied a tensile load along the zigzag or armchair direction at a constant engineering strain rate of 108 s−1 (applied at every simulation step). To ensure longitudinal loading conditions with zero transverse stress, the width of the simulation box was allowed to change along this direction within the NPT ensemble (whose simulation time step is 0.25 fs). To define stress values, we used dnominal = 6.50 Å as the nominal thickness for a WSe2 monolayer, as shown in Figure 2c. The elongation, ΔL, along the zigzag or armchair direction, is simply the constant engineering (nominal) strain rate, ε, multiplied by the loading time, t, and the initial length, L∘, of the system, as shown in the equation ΔL = εtL∘, and engineering (nominal) stress, σ, along the zigzag (ZZ) and armchair (AC) directions is defined as σ = 1/V∘ ∂U/∂ε, where V∘ = LAC∘LZZ∘dnominal is the initial volume of the relaxed system. The Young's modulus of the WSe2 ML along both directions was computed from the slope of the linear portion of the nominal stress−strain curve depicted in Figure 9a, where the material obeys Hooke's law.

![](./images/812528762917748737_12.jpg)

Figure 10. Edge formation energies of WSe₂ nanoribbons. Top and cross-sectional views of the optimized configurations of (a) Ant-Se₅₀/ZZ-Se₅₀, (b) Ant-Se₅₀/ZZ-Se₁₀₀, (c) Ant-Se₁₀₀/ZZ-Se₅₀, and (d) Ant-Se₁₀₀/ZZ-Se₁₀₀ and (e, f) associated edge formation energies as a function of the excess chemical potential, $\Delta\mu_{Se} = \mu_{Se}(\text{bulk}) - \mu_{Se}$, at ReaxFF and DFT levels.

As displayed in Table 1, the calculated Young’s moduli of WSe₂ slightly depend on the loading direction, being 209 and 218 GPa with the ultimate tensile strength of 23.7 and 28.4 GPa along the armchair and zigzag directions, respectively, at 300 K. The ReaxFF-based Poisson’s ratio (transverse over longitudinal strain) is 0.65 and 0.39 along the zigzag and armchair directions, respectively. To date, there is no experimental report of the Young’s modulus of single-layer WSe₂; Zhang et al.⁷⁷ only estimated Young’s modulus of a WSe₂ multilayer to be 167.3 ± 6.7 GPa from an experimental statistical analysis conducted for 5, 6, 12, and 14 layer thick WSe₂ flakes. Comparative in-plane stiffness measurements for 2D and conventional bulk materials (i.e., MoS₂, WS₂) show a drastic change in the elastic properties of 2D materials compared to their bulk form, Young’s moduli of bulk forms being lower than those of single-layered structures.⁷⁸⁻⁸⁰ Therefore, one may anticipate Young’s modulus for a WSe₂ monolayer to be higher than that of a multilayer. Additionally, DFT calculations of Deng et al.⁸¹ predict Young’s modulus of a WSe₂ monolayer to be 201.5 GPa and obtain a sequence of moduli for WS₂, MoS₂, WSe₂, and MoSe₂ as $Y_{WS2} > Y_{MoS2} > Y_{WSe2} > Y_{MoSe2}$. Within the ReaxFF framework, the MoS₂ value of 245 ± 15 GPa computed by Mortazavi et al.³⁶ is higher than the WSe₂ value of 218 ± 15 GPa from the present work, in good agreement with the ordering reported by Deng et al.⁸¹ Table 1 summarizes the ReaxFF, experimental,⁷⁷ and DFT⁸²⁻⁸⁵ values of elastic constants for a defect-free WSe₂ ML. Additionally, as seen in Figure 9a, subsequent increases in the stress caused a deviation from linearity in the stress−strain curve, particularly for the zigzag direction, in line with the observed onset of elastic nonlinearity in earlier studies.⁷⁸,⁸⁰

Since several studies⁸⁶⁻⁸⁸ report that impurities such as vacancies can significantly alter (generally weaken) the mechanical properties of 2D materials, we further examined the mechanical response of 2D WSe₂ under coupled effects of Se vacancies and strain. As depicted in Figure 9a,b, vacancies in the WSe₂ lattice soften the system and reduce the ultimate tensile strength, in line with expectations and in good agreement with a previous SW-based MD study.⁸⁹

Edge Excess Energies. The structural energetics of edges directly impact the stability and growth kinetics of TMD materials in both lateral and vertical directions. Therefore, understanding the edge evolution as a function of the local chemical environment is important for fabricating functional atomically thin 2D materials. Several DFT-based theoretical studies have investigated the thermodynamic evolution of WSe₂ edges in various atomic configurations.¹⁹,²⁰,⁹⁰,⁹¹ However, the lack of a reactive force field to cost-effectively model the edge-controlled growth and kinetics of single-crystal formation in 2D WSe₂ under different growth conditions at large scales hinders further progress that takes into account more complex transient local heterogeneities during growth. Our new ReaxFF potential was thus trained against the edge formation energies of multiple configurations with different Se coverages. As shown in Figure 10a−d, four types of WSe₂ zigzag edges in a nanoribbon configuration were generated, each made of two zigzag edge types, standard Se-terminated zigzag edges, “ZZ-Se”, and antenna-type zigzag edges, “Ant-Se”, which is the complementary W-terminated zigzag configuration with additional Se attached. The ZZ-Se₅₀ and ZZ-Se₁₀₀ edges are covered with 50 and 100% Se, respectively; Ant-Se₅₀ and Ant-Se₁₀₀ likewise have 50 and 100% Se coverage, respectively. Each ribbon model is denoted as “Ant-Seₚct/ZZ-Seₚct”, where “pct” refers to the percentage of Se coverage for that edge type. The excess edge energies $\gamma$ of the ribbon model were computed within ReaxFF and DFT using the equation $\gamma = [\text{E}_{WSe2} - \text{n}_{WSe2}\mu_{WSe2} + \text{n}_{Se}\mu_{Se}]/2\text{L}$ where the width of each model was 2.6 nm and $L = 0.65$ nm. $\mu_{WSe2}$ is the total energy of the WSe₂ unit in a pristine monolayer.

As depicted in Figure 10e,f, the ReaxFF-based edge excess energies show reasonable agreement with those from DFT. Both methods predict the Ant-Se₁₀₀/ZZ-Se₁₀₀ model to be most stable, followed by Ant-Se₅₀/ZZ-Se₁₀₀, in a Se-rich environment, while the formation of Ant-Se₅₀/ZZ-Se₁₀₀ is favored in a W-rich environment (but with a decreasing trend toward W-rich conditions). Ant-Se₅₀/ZZ-Se₅₀ is stoichiometric; therefore, its formation energy remains constant in varying growth conditions. Ant-Se₁₀₀/ZZ-Se₅₀ is the least stable edge in a W-rich environment.

![](./images/812528762917748737_13.jpg)

Figure 11. Step-flow growth process and associated kink formation energy evolution of (a) ZZ-Se₁₀₀ and (b) Ant-Se₁₀₀ edges in a Se-rich environment. The energies required for kink nucleation and propagation are indicated in red and black font colors, respectively. (c) Kink nucleation energy of each edge type as a function of the excess chemical potential, $\Delta\mu_{\text{Se}} = \mu_{\text{Se}}(\text{bulk}) - \mu_{\text{Se}}$, within ReaxFF.

environment, but its formation is more favored than Ant-Se₅₀/ ZZ-Se₅₀ under Se-rich conditions.

We also examined the energetics of kink nucleation and kink propagation along ZZ-Se₁₀₀ and Ant-Se₁₀₀ edges using a step- flow growth model.⁹² As illustrated in Figure 11a,b, the addition of the first WSe₂ unit onto both edges requires a high energy of 3.85 eV for ZZ-Se₁₀₀ and 1.13 eV for Ant-Se₁₀₀ in the Se-rich condition, while the consecutive addition of WSe₂ units to the edge after the kink nucleation requires negligible energy, implying that the WSe₂ edge-growth is governed by kink nucleation, the rate-limiting step, in good agreement with previous studies on 2D edge-growth.⁹³⁻⁹⁵ Additionally, kink nucleation on the ZZ-Se₁₀₀ edge costs more energy than on Ant- Se₁₀₀, indicating that antenna-type edges grow faster than standard zigzag edges.

Our benchmark presented throughout the paper reflects the applicability of a newly developed ReaxFF force field to the simulations of structural engineering and growth of 2D WSe₂, suggesting that this potential is a cost-effective exploratory tool to simulate atomic resolution images of structural deformations, such as crack, hole, line defect, grain boundaries, defect-induced phase transitions, and strain-induced morphological changes in a monolayer. Additionally, since multiscale approaches bridging spatial scales that range from $10^{-9}$ to $10^{-3}$ m in space have received increasing recognition in the materials science community,³⁰,⁹⁶,⁹⁷ the new potential can be integrated into macro- and mesoscale simulations to model the growth kinetics and morphological evolution of 2D WSe₂ islands at modest computational costs that can be validated through topographical images of the material using scanning probe microscopes. Given the increasing interest in machine learning-based data-driven approaches that can automatically detect and classify patterns in data,³⁷,⁸⁷ this potential can be effectively utilized in generating systematic and, more importantly, computationally cheap representative data to train machine learning algorithms for an observed feature in a WSe₂ monolayer.

## CONCLUSIONS

In summary, we developed a new ReaxFF reactive force field for W/Se/H interactions. Our comprehensive comparison of the ReaxFF results with the DFT and experimental measurements shows the capability, accuracy, and transferability of the new potential to perform large-scale simulations of 2D WSe₂ at modest computational costs. Since this potential was trained against extensive first-principles energetics data, which describes well fundamental solid-phase phenomena such as ground-state properties of 2H-WSe₂ (i.e., lattice constants, atomic positions, bond lengths, and the behavior of WSe₂ under compression or expansion), phase transformation, defect formation and vacancy migration, and formation energies of edges with varying coverages, it is a computational means that can provide atomistic insights into experimental efforts to modulate the properties of 2D WSe₂ by phase and defect engineering and to optimize edge-controlled growth of single-crystal 2D WSe₂ as a function of the local chemical environment. Strain engineering of 2D layers is one of the effective ways to modulate the mechanical and optoelectronic properties of the material. This potential is a cost-effective means that can elucidate the morphological evolution of a monolayer in different environ- ments in terms of loading conditions and various concentrations and distributions of defects. The coupling between ripplocations (recently described by Kushima et al.¹² for MoS₂ sheets) and Se vacancies in a structurally deformed WSe₂ monolayer is studied for the first time. The interactions between vacancies and ripplocations suggest that vacancies can be utilized to stabilize buckled structures by modulating the strain energy and that ripplocations can open a venue for sweeping out undesirable defects such as vacancies from 2D WSe₂ because a highly curved ripplocation is a favorable host for vacancy defects under thermodynamic equilibrium conditions and, conversely, ripplo- cations tend to form in defective structures.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.0c09155.

Comparative DFT and ReaxFF results for nonperiodic and periodic calculations included in the training set, and the details of the calculations for ripplocations (PDF)
ReaxFF reactive force field parameters for W/Se/H interactions (TXT)

## AUTHOR INFORMATION

### Corresponding Author
Adri C. T. van Duin − Department of Mechanical Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; https://orcid.org/0000-0002-3478-4945;
Email: acv13@psu.edu

### Authors
Nadire Nair − Department of Mechanical Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute, The Pennsylvania State

University, University Park, Pennsylvania 16802, United States; Department of Physics, Karamanoglu Mehmetbey University, Karaman 70000, Turkey; orcid.org/0000-0002-3621-2481

Yuanxi Wang − 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute and Department of Physics, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; orcid.org/0000-0002-0659-1134

Sharmin Shabnam − Department of Mechanical Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Danielle Reifsnyder Hickey − 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute and Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Leixin Miao − Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Xiaotian Zhang − Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Saiphaneendra Bachu − Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Nasim Alem − 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute and Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; orcid.org/0000-0003-0009-349X

Joan Redwing − 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute and Department of Materials Science and Engineering, The Pennsylvania State University, University Park, Pennsylvania 16802, United States; orcid.org/0000-0002-7906-452X

Vincent H. Crespi − 2-Dimensional Crystal Consortium (2DCC) Materials Research Institute and Department of Physics, The Pennsylvania State University, University Park, Pennsylvania 16802, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.0c09155

## Author Contributions
The manuscript was written through the contributions of all authors. All authors have given approval to the final version of the manuscript.

## Funding
The National Science Foundation (NSF) through the Pennsylvania State University 2D Crystal Consortium−Materials Innovation Platform (2DCC-MIP) under the NSF cooperative agreement DMR-1539916, the NSF CAREER program (DMR-1654107), NSF-MRSEC.

## Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This work was financially supported by the National Science Foundation (NSF) through the Pennsylvania State University 2D Crystal Consortium−Materials Innovation Platform (2DCC-MIP) under the NSF cooperative agreement DMR-1539916. D.R.H., S.B., and N.A. acknowledge support from the NSF CAREER program (DMR-1654107). This work utilized resources provided by the NSF-MRSEC-sponsored Materials Characterization Lab at Penn State.

## REFERENCES
(1) Lin, Z.; Carvalho, B. R.; Kahn, E.; Lv, R.; Rao, R.; Terrones, H.; Pimenta, M. A.; Terrones, M. Defect Engineering of Two-Dimensional Transition Metal Dichalcogenides. 2D Mater. 2016, 3, No. 022002.

(2) Voiry, D.; Mohite, A.; Chhowalla, M. Phase Engineering of Transition Metal Dichalcogenides. Chem. Soc. Rev. 2015, 44, 2702−2712.

(3) Chhowalla, M.; Voiry, D.; Yang, J.; Shin, H. S.; Loh, K. P. Phase-Engineered Transition-Metal Dichalcogenides for Energy and Electronics. MRS Bull. 2015, 40, 585−591.

(4) Fang, H.; Chuang, S.; Chang, T. C.; Takei, K.; Takahashi, T.; Javey, A. High-Performance Single Layered WSe2 p-FETs with Chemically Doped Contacts. Nano Lett. 2012, 12, 3788−3792.

(5) Gao, J.; Xu, Z.; Chen, S.; Bharathi, M. S.; Zhang, Y.-W. Computational Understanding of the Growth of 2D Materials. Adv. Theory Simul. 2018, 1, No. 1800085.

(6) Jiang, J.; Xu, T.; Lu, J.; Sun, L.; Ni, Z. Defect Engineering in 2D Materials: Precise Manipulation and Improved Functionalities. https://spj.sciencemag.org/research/2019/4641739/ ( accessed May 5 , 2020).

(7) Yu, Y.; Nam, G.-H.; He, Q.; Wu, X.-J.; Zhang, K.; Yang, Z.; Chen, J.; Ma, Q.; Zhao, M.; Liu, Z.; Ran, F.-R.; Wang, X.; Li, H.; Huang, X.; Li, B.; Xiong, Q.; Zhang, Q.; Liu, Z.; Gu, L.; Du, Y.; Huang, W.; Zhang, H. High Phase-Purity 1T'-MoS 2 - and 1T'-MoSe 2 -Layered Crystals. Nat. Chem. 2018, 10, 638−643.

(8) Liu, Q.; Fang, Q.; Chu, W.; Wan, Y.; Li, X.; Xu, W.; Habib, M.; Tao, S.; Zhou, Y.; Liu, D.; Xiang, T.; Khalil, A.; Wu, X.; Chhowalla, M.; Ajayan, P. M.; Song, L. Electron-Doped 1T-MoS2 via Interface Engineering for Enhanced Electrocatalytic Hydrogen Evolution. Chem. Mater. 2017, 29, 4738−4744.

(9) Voiry, D.; Salehi, M.; Silva, R.; Fujita, T.; Chen, M.; Asefa, T.; Shenoy, V. B.; Eda, G.; Chhowalla, M. Conducting MoS2 Nanosheets as Catalysts for Hydrogen Evolution Reaction. Nano Lett. 2013, 13, 6222−6227.

(10) Lu, N.; Zhang, C.; Lee, C.-H.; Oviedo, J. P.; Nguyen, M. A. T.; Peng, X.; Wallace, R. M.; Mallouk, T. E.; Robinson, J. A.; Wang, J.; Cho, K.; Kim, M. J. Atomic and Electronic Structures of WTe2 Probed by High Resolution Electron Microscopy and Ab Initio Calculations. J. Phys. Chem. C 2016, 120, 8364−8369.

(11) Lukowski, M. A.; Daniel, A. S.; Meng, F.; Forticaux, A.; Li, L.; Jin, S. Enhanced Hydrogen Evolution Catalysis from Chemically Exfoliated Metallic MoS2 Nanosheets. J. Am. Chem. Soc. 2013, 135, 10274−10277.

(12) Kushima, A.; Qian, X.; Zhao, P.; Zhang, S.; Li, J. Ripplocations in van Der Waals Layers. Nano Lett. 2015, 15, 1302−1308.

(13) Sun, J.-S.; Jiang, J.-W.; Park, H. S.; Zhang, S. Self-Cleaning by Harnessing Wrinkles in Two-Dimensional Layered Crystals. Nanoscale 2018, 10, 312−318.

(14) Stern, C.; Grinvald, S.; Kirshner, M.; Sinai, O.; Oksman, M.; Alon, H.; Meiron, O. E.; Bar-Sadan, M.; Houben, L.; Naveh, D. Growth Mechanisms and Electronic Properties of Vertically Aligned MoS2. Sci. Rep. 2018, 8, No. 16480.

(15) Li, H.; Wu, H.; Yuan, S.; Qian, H. Synthesis and Characterization of Vertically Standing MoS 2 Nanosheets. Sci. Rep. 2016, 6, No. 21171.

(16) Shang, S.-L.; Lindwall, G.; Wang, Y.; Redwing, J. M.; Anderson, T.; Liu, Z.-K. Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS2. Nano Lett. 2016, 16, 5742−5750.

(17) Gao, Y.; Hong, Y.-L.; Yin, L.-C.; Wu, Z.; Yang, Z.; Chen, M.-L.; Liu, Z.; Ma, T.; Sun, D.-M.; Ni, Z.; Ma, X.-L.; Cheng, H.-M.; Ren, W. Ultrafast Growth of High-Quality Monolayer WSe2 on Au. Adv. Mater. 2017, 29, No. 1700990.

(18) Deng, Q.; Thi, Q. H.; Zhao, J.; Yun, S. J.; Kim, H.; Chen, G.; Ly, T. H. Impact of Polar Edge Terminations of the Transition Metal Dichalcogenide Monolayers during Vapor Growth. J. Phys. Chem. C 2018, 122, 3575−3581.
J
https://dx.doi.org/10.1021/acs.jpcc.0c09155
J. Phys. Chem. C XXXX, XXX, XXX−XXX

(19) Chen, S.; Gao, J.; Srinivasan, B. M.; Zhang, G.; Sorkin, V.; Hariharaputran, R.; Zhang, Y.-W. Origin of Ultrafast Growth of Monolayer WSe 2 via Chemical Vapor Deposition. *Npj Comput. Mater.* **2019**, *5*, No. 28.

(20) Yue, R.; Nie, Y.; Walsh, L. A.; Addou, R.; Liang, C.; Lu, N.; Barton, A. T.; Zhu, H.; Che, Z.; Barrera, D.; Cheng, L.; Cha, P.-R.; Chabal, Y. J.; Hsu, J. W. P.; Kim, J.; Kim, M. J.; Colombo, L.; Wallace, R. M.; Cho, K.; Hinkle, C. L. Nucleation and Growth of WSe 2: Enabling Large Grain Transition Metal Dichalcogenides. *2D Mater.* **2017**, *4*, No. 045019.

(21) Xiao, S.-L.; Yu, W.-Z.; Gao, S.-P. Edge Preference and Band Gap Characters of MoS2 and WS2 Nanoribbons. *Surf. Sci.* **2016**, *653*, 107−112.

(22) Dhakal, K. P.; Roy, S.; Jang, H.; Chen, X.; Yun, W. S.; Kim, H.; Lee, J.; Kim, J.; Ahn, J.-H. Local Strain Induced Band Gap Modulation and Photoluminescence Enhancement of Multilayer Transition Metal Dichalcogenides. *Chem. Mater.* **2017**, *29*, 5124−5133.

(23) Deng, S.; Che, S.; Debbarma, R.; Berry, V. Strain in a Single Wrinkle on an MoS2 Flake for In-Plane Realignment of Band Structure for Enhanced Photo-Response. *Nanoscale* **2019**, *11*, 504−511.

(24) Momeni, K.; Ji, Y.; Wang, Y.; Paul, S.; Neshani, S.; Yilmaz, D. E.; Shin, Y. K.; Zhang, D.; Jiang, J.-W.; Park, H. S.; Sinnott, S.; van Duin, A.; Crespi, V.; Chen, L.-Q. Multiscale Computational Understanding and Growth of 2D Materials: A Review. *Npj Comput. Mater.* **2020**, *6*, No. 22.

(25) Senftle, T. P.; Hong, S.; Islam, M. M.; Kylasa, S. B.; Zheng, Y.; Shin, Y. K.; Junkermeier, C.; Engel-Herbert, R.; Janik, M. J.; Aktulga, H. M.; Verstraelen, T.; Grama, A.; van Duin, A. C. T. The ReaxFF Reactive Force-Field: Development, Applications and Future Directions. *Npj Comput. Mater.* **2016**, *2*, No. 15011.

(26) Norouzzadeh, P.; Singh, D. J. Thermal Conductivity of Single-Layer WSe2 by a Stillinger−Weber Potential. *Nanotechnology* **2017**, *28*, No. 075708.

(27) Mobaraki, A.; Kandemir, A.; Yapicioglu, H.; Gülseren, O.; Sevik, C. Validation of Inter-Atomic Potential for WS2 and WSe2 Crystals through Assessment of Thermal Transport Properties. *Comput. Mater. Sci.* **2018**, *144*, 92−98.

(28) Jiang, J.-W.; Zhou, Y.-P. Parameterization of Stillinger-Weber Potential for Two-Dimensional Atomic Crystals. In *Handbook of Stillinger-Weber Potential Parameters for Two-Dimensional Atomic Crystals*; IntechOpen, 2017.

(29) Han, Y.; Li, M.-Y.; Jung, G.-S.; Marsalis, M. A.; Qin, Z.; Buehler, M. J.; Li, L.-J.; Muller, D. A. Sub-Nanometre Channels Embedded in Two-Dimensional Materials. *Nat. Mater.* **2018**, *17*, 129−133.

(30) Xuan, Y.; Jain, A.; Zafar, S.; Lotfi, R.; Nayir, N.; Wang, Y.; Choudhury, T. H.; Wright, S.; Feraca, J.; Rosenbaum, L.; Redwing, J. M.; Crespi, V.; van Duin, A. C. T. Multi-Scale Modeling of Gas-Phase Reactions in Metal-Organic Chemical Vapor Deposition Growth of WSe2. *J. Cryst. Growth* **2019**, *527*, No. 125247.

(31) van Duin, A. C. T.; Dasgupta, S.; Lorant, F.; Goddard, W. A. ReaxFF: A Reactive Force Field for Hydrocarbons. *J. Phys. Chem. A* **2001**, *105*, 9396−9409.

(32) Tersoff, J. Empirical Interatomic Potential for Carbon, with Applications to Amorphous Carbon. *Phys. Rev. Lett.* **1988**, *61*, 2879−2882.

(33) Brenner, D. W.; Shenderova, O. A.; Harrison, J. A.; Stuart, S. J.; Ni, B.; Sinnott, S. B. A Second-Generation Reactive Empirical Bond Order (REBO) Potential Energy Expression for Hydrocarbons. *J. Phys.: Condens. Matter* **2002**, *14*, 783−802.

(34) Brenner, D. W. Empirical Potential for Hydrocarbons for Use in Simulating the Chemical Vapor Deposition of Diamond Films. *Phys. Rev. B* **1990**, *42*, 9458−9471.

(35) Ostadhossein, A.; Rahnamoun, A.; Wang, Y.; Zhao, P.; Zhang, S.; Crespi, V. H.; van Duin, A. C. T. ReaxFF Reactive Force-Field Study of Molybdenum Disulfide (MoS2). *J. Phys. Chem. Lett.* **2017**, *8*, 631−640.

(36) Mortazavi, B.; Ostadhossein, A.; Rabczuk, T.; Duin, A. C. T. van. Mechanical Response of All-MoS2 Single-Layer Heterostructures: A ReaxFF Investigation. *Phys. Chem. Chem. Phys.* **2016**, *18*, 23695−23701.

(37) Patra, T. K.; Zhang, F.; Schulman, D. S.; Chan, H.; Cherukara, M. J.; Terrones, M.; Das, S.; Narayanan, B.; Sankaranarayanan, S. K. R. S. Defect Dynamics in 2-D MoS2 Probed by Using Machine Learning, Atomistic Simulations, and High-Resolution Microscopy. *ACS Nano* **2018**, *12*, 8006−8016.

(38) Lotfi, R.; Naguib, M.; Yilmaz, D. E.; Nanda, J.; Duin, A. C. T. van. A Comparative Study on the Oxidation of Two-Dimensional Ti3C2 MXene Structures in Different Environments. *J. Mater. Chem. A* **2018**, *6*, 12733−12743.

(39) Sang, X.; Xie, Y.; Yilmaz, D. E.; Lotfi, R.; Alhabeb, M.; Ostadhossein, A.; Anasori, B.; Sun, W.; Li, X.; Xiao, K.; Kent, P. R. C.; Duin, A. C. T.; van Gogotsi, Y.; Unocic, R. R. In Situ Atomistic Insight into the Growth Mechanisms of Single Layer 2D Transition Metal Carbides. *Nat. Commun.* **2018**, *9*, No. 2266.

(40) Osti, N. C.; Naguib, M.; Ganeshan, K.; Shin, Y. K.; Ostadhossein, A.; van Duin, A. C. T.; Cheng, Y.; Daemen, L. L.; Gogotsi, Y.; Mamontov, E.; Kolesnikov, A. I. Influence of Metal Ions Intercalation on the Vibrational Dynamics of Water Confined between MXene Layers. *Phys. Rev. Mater.* **2017**, *1*, No. 065406.

(41) Osti, N. C.; Naguib, M.; Ostadhossein, A.; Xie, Y.; Kent, P. R. C.; Dyatkin, B.; Rother, G.; Heller, W. T.; van Duin, A. C. T.; Gogotsi, Y.; Mamontov, E. Effect of Metal Ion Intercalation on the Structure of MXene and Water Dynamics on Its Internal Surfaces. *ACS Appl. Mater. Interfaces* **2016**, *8*, 8859−8863.

(42) Liu, S.; Comer, J.; Duin, A. C. T.; van Duin, D. M.; van Liu, B.; Edgar, J. H. Predicting the Preferred Morphology of Hexagonal Boron Nitride Domain Structure on Nickel from ReaxFF-Based Molecular Dynamics Simulations. *Nanoscale* **2019**, *11*, 5607−5616.

(43) Liu, S.; van Duin, A. C. T.; van Duin, D. M.; Liu, B.; Edgar, J. H. Atomistic Insights into Nucleation and Formation of Hexagonal Boron Nitride on Nickel from First-Principles-Based Reactive Molecular Dynamics Simulations. *ACS Nano* **2017**, *11*, 3585−3596.

(44) Yoon, K.; Rahnamoun, A.; Swett, J. L.; Iberi, V.; Cullen, D. A.; Vlassiouk, I. V.; Belianinov, A.; Jesse, S.; Sang, X.; Ovchinnikova, O. S.; Rondinone, A. J.; Unocic, R. R.; van Duin, A. C. T. Atomistic-Scale Simulations of Defect Formation in Graphene under Noble Gas Ion Irradiation. *ACS Nano* **2016**, *10*, 8376−8384.

(45) Chenoweth, K.; van Duin, A. C. T.; Goddard, W. A. ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation. *J. Phys. Chem. A* **2008**, *112*, 1040−1053.

(46) Bochevarov, A. D.; Harder, E.; Hughes, T. F.; Greenwood, J. R.; Braden, D. A.; Philipp, D. M.; Rinaldo, D.; Halls, M. D.; Zhang, J.; Friesner, R. A. Jaguar: A High-Performance Quantum Chemistry Software Program with Strengths in Life and Materials Sciences. *Int. J. Quantum Chem.* **2013**, *113*, 2110−2142.

(47) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. *Phys. Rev. B* **1996**, *54*, 11169−11186.

(48) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Phys. Rev. B* **1999**, *59*, 1758−1775.

(49) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* **1994**, *50*, 17953−17979.

(50) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple [Phys. Rev. Lett. 77, 3865 (1996)]. *Phys. Rev. Lett.* **1997**, *78*, 1396.

(51) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865−3868.

(52) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate Ab Initio Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. *J. Chem. Phys.* **2010**, *132*, No. 154104.

(53) Hentz, A.; Parkinson, G. S.; Quinn, P. D.; Muñoz-Márquez, M. A.; Woodruff, D. P.; Grande, P. L.; Schiwietz, G.; Bailey, P.; Noakes, T. C. Q. Direct Observation and Theory of Trajectory-Dependent Electronic Energy Losses in Medium-Energy Ion Scattering. *Phys. Rev. Lett.* **2009**, *102*, No. 096103.

(54) Amsterdam Modeling Suite Making Computational Chemistry Work For You. https://www.scm.com/ ( accessed Oct 16 , 2019).

K
https://dx.doi.org/10.1021/acs.jpcc.0c09155
*J. Phys. Chem. C* XXXX, XXX, XXX−XXX

(55) Plimpton, S. Fast Parallel Algorithms for Short-Range Molecular Dynamics. J. Comput. Phys. 1995, 117, 1−19.

(56) Stukowski, A. Visualization and Analysis of Atomistic Simulation Data with OVITO−the Open Visualization Tool. Modell. Simul. Mater. Sci. Eng. 2010, 18, No. 015012.

(57) Momma, K.; Izumi, F. VESTA 3 for Three-Dimensional Visualization of Crystal, Volumetric and Morphology Data. J. Appl. Crystallogr. 2011, 44, 1272−1276.

(58) Eftekhari, A. Tungsten Dichalcogenides (WS2, WSe2, and WTe2): Materials Chemistry and Applications. J. Mater. Chem. A 2017, 5, 18299−18325.

(59) Choi, W.; Choudhary, N.; Han, G. H.; Park, J.; Akinwande, D.; Lee, Y. H. Recent Development of Two-Dimensional Transition Metal Dichalcogenides and Their Applications. Mater. Today 2017, 20, 116−130.

(60) Jin, Q.; Liu, N.; Chen, B.; Mei, D. Mechanisms of Semi- conducting 2H to Metallic 1T Phase Transition in Two-Dimensional MoS2 Nanosheets. J. Phys. Chem. C 2018, 122, 28215−28224.

(61) Gao, G.; Jiao, Y.; Ma, F.; Jiao, Y.; Waclawik, E.; Du, A. Charge Mediated Semiconducting-to-Metallic Phase Transition in Molybde- num Disulfide Monolayer and Hydrogen Evolution Reaction in New 1T’ Phase. J. Phys. Chem. C 2015, 119, 13124−13128.

(62) Lin, Y.-C.; Dumcenco, D. O.; Huang, Y.-S.; Suenaga, K. Atomic Mechanism of the Semiconducting-to-Metallic Phase Transition in Single-Layered MoS2. Nat. Nanotechnol. 2014, 9, 391−396.

(63) Zhang, C.; Wang, C.; Yang, F.; Huang, J.-K.; Li, L.-J.; Yao, W.; Ji, W.; Shih, C.-K. Engineering Point-Defect States in Monolayer WSe2. ACS Nano 2019, 13, 1595−1602.

(64) Zheng, Y. J.; Chen, Y.; Huang, Y. L.; Gogoi, P. K.; Li, M.-Y.; Li, L.- J.; Trevisanutto, P. E.; Wang, Q.; Pennycook, S. J.; Wee, A. T. S.; Quek, S. Y. Point Defects and Localized Excitons in 2D WSe2. ACS Nano 2019, 13, 6050−6059.

(65) Yang, D.; Fan, X.; Zhang, F.; Hu, Y.; Luo, Z. Electronic and Magnetic Properties of Defected Monolayer WSe2 with Vacancies. Nanoscale Res. Lett. 2019, 14, No. 192.

(66) Zhang, S.; Wang, C.-G.; Li, M.-Y.; Huang, D.; Li, L.-J.; Ji, W.; Wu, S. Defect Structure of Localized Excitons in a $\mathrm{WSe}_{2}$ Monolayer. Phys. Rev. Lett. 2017, 119, No. 046101.

(67) Yang, D.; Fan, X.; Zhang, F.; Hu, Y.; Luo, Z. Electronic and Magnetic Properties of Defected Monolayer WSe2 with Vacancies. Nanoscale Res. Lett. 2019, 14, No. 192.

(68) Li, L.; Carter, E. A. Defect-Mediated Charge-Carrier Trapping and Nonradiative Recombination in WSe2 Monolayers. J. Am. Chem. Soc. 2019, 141, 10451−10461.

(69) Lin, J.; Pantelides, S. T.; Zhou, W. Vacancy-Induced Formation and Growth of Inversion Domains in Transition-Metal Dichalcogenide Monolayer. ACS Nano 2015, 9, 5189−5197.

(70) Haldar, S.; Vovusha, H.; Yadav, M. K.; Eriksson, O.; Sanyal, B. Systematic Study of Structural, Electronic, and Optical Properties of Atomic-Scale Defects in the Two-Dimensional Transition Metal Dichalcogenides $\mathrm{MX}_{2}$ ($\mathrm{M} = \mathrm{Mo}$, $\mathrm{X} = \mathrm{S}$, Se, Te). Phys. Rev. B 2015, 92, No. 235408.

(71) Jeong, T. Y.; Kim, H.; Choi, S.-J.; Watanabe, K.; Taniguchi, T.; Yee, K. J.; Kim, Y.-S.; Jung, S. Spectroscopic Studies of Atomic Defects and Bandgap Renormalization in Semiconducting Monolayer Tran- sition Metal Dichalcogenides. Nat. Commun. 2019, 10, No. 3825.

(72) Zhang, X.; Choudhury, T. H.; Chubarov, M.; Xiang, Y.; Jariwala, B.; Zhang, F.; Alem, N.; Wang, G.-C.; Robinson, J. A.; Redwing, J. M. Diffusion-Controlled Epitaxy of Large Area Coalesced WSe2 Monolayers on Sapphire. Nano Lett. 2018, 18, 1049−1056.

(73) Yue, R.; Nie, Y.; Walsh, L. A.; Addou, R.; Liang, C.; Lu, N.; Barton, A. T.; Zhu, H.; Che, Z.; Barrera, D.; Cheng, L.; Cha, P.-R.; Chabal, Y. J.; Hsu, J. W. P.; Kim, J.; Kim, M. J.; Colombo, L.; Wallace, R. M.; Cho, K.; Hinkle, C. L. Nucleation and Growth of WSe2: Enabling Large Grain Transition Metal Dichalcogenides. 2D Mater. 2017, 4, No. 045019.

(74) Tritsaris, G. A.; Şensoy, M. G.; Shirodkar, S. N.; Kaxiras, E. First- Principles Study of Coupled Effect of Ripplocations and S-Vacancies in MoS2. J. Appl. Phys. 2019, 126, No. 084303.

(75) Gruber, J.; Barsoum, M. W.; Tucker, G. J. Characterization of Ripplocation Mobility in Graphite. Mater. Res. Lett. 2020, 8, 82−87.

(76) Savin, A. V.; Korznikova, E. A.; Dmitriev, S. V. Dynamics of Surface Graphene Ripplocations on a Flat Graphite Substrate. Phys. Rev. B 2019, 99, No. 235411.

(77) Zhang, R.; Koutsos, V.; Cheung, R. Elastic Properties of Suspended Multilayer WSe2. Appl. Phys. Lett. 2016, 108, No. 042104.

(78) Liu, K.; Yan, Q.; Chen, M.; Fan, W.; Sun, Y.; Suh, J.; Fu, D.; Lee, S.; Zhou, J.; Tongay, S.; Ji, J.; Neaton, J. B.; Wu, J. Elastic Properties of Chemical-Vapor-Deposited Monolayer MoS2, WS2, and Their Bilayer Heterostructures. Nano Lett. 2014, 14, 5097−5103.

(79) Bertolazzi, S.; Brivio, J.; Kis, A. Stretching and Breaking of Ultrathin MoS2. ACS Nano 2011, 5, 9703−9709.

(80) Kim, J. H.; Jeong, J. H.; Kim, N.; Joshi, R.; Lee, G.-H. Mechanical Properties of Two-Dimensional Materials and Their Applications. J. Phys. D: Appl. Phys. 2019, 52, No. 083001.

(81) Deng, S.; Li, L.; Li, M. Stability of Direct Band Gap under Mechanical Strains for Monolayer MoS2, MoSe2, WS2 and WSe2. Phys. E 2018, 101, 44−49.

(82) Çakır, D.; Peeters, F. M.; Sevik, C. Mechanical and Thermal Properties of H-MX2 (M = Cr, Mo, W; X = O, S, Se, Te) Monolayers: A Comparative Study. Appl. Phys. Lett. 2014, 104, No. 203110.

(83) Zeng, F.; Zhang, W.-B.; Tang, B.Y. Electronic structures and elastic properties of monolayer and bilayer transition metal dichalcogenides MX2 (M= Mo, W; X= O, S, Se, Te): A comparative first-principles study. Chinese Phys. B 2015, 24, 097103 DOI: 10.1088/ 1674-1056/24/9/097103.

(84) Kang, J.; Tongay, S.; Zhou, J.; Li, J.; Wu, J. Band Offsets and Heterostructures of Two-Dimensional Semiconductors. Appl. Phys. Lett. 2013, 102, No. 012111.

(85) Persson, K. Materials Data on WSe2 (SG:194) by Materials Project. In LBNL Materials Project; Lawrence Berkeley National Laboratory (LBNL): Berkeley, CA, 2014.

(86) Iberi, V.; Liang, L.; Ievlev, A. V.; Stanford, M. G.; Lin, M.-W.; Li, X.; Mahjouri-Samani, M.; Jesse, S.; Sumpter, B. G.; Kalinin, S. V.; Joy, D. C.; Xiao, K.; Belianinov, A.; Ovchinnikova, O. S. Nanoforging Single Layer MoSe 2 Through Defect Engineering with Focused Helium Ion Beams. Sci. Rep. 2016, 6, No. 30481.

(87) Wang, X.; Han, D.; Hong, Y.; Sun, H.; Zhang, J.; Zhang, J. Machine Learning Enabled Prediction of Mechanical Properties of Tungsten Disulfide Monolayer. ACS Omega 2019, 4, 10121−10128.

(88) Li, H.; Zhang, H.; Cheng, X. The Effect of Temperature, Defect and Strain Rate on the Mechanical Property of Multi-Layer Graphene: Coarse-Grained Molecular Dynamics Study. Phys. E 2017, 85, 97−102.

(89) Ding, W.; Han, D.; Zhang, J.; Wang, X. Mechanical responses of WSe2 monolayers: a molecular dynamics study. Mater. Res. Express 2019, 6 (8), 085071.

(90) Addou, R.; Smyth, C. M.; Noh, J.-Y.; Lin, Y.-C.; Pan, Y.; Eichfeld, S. M.; Fölsch, S.; Robinson, J. A.; Cho, K.; Feenstra, R. M.; Wallace, R. M. One Dimensional Metallic Edges in Atomically Thin WSe 2 Induced by Air Exposure. 2D Mater. 2018, 5, No. 025017.

(91) Da Silva, A. C. H.; Caturello, N. A. M. S.; Besse, R.; Lima, M. P.; Da Silva, J. L. F. Edge, Size, and Shape Effects on WS2, WSe2, and WTe2 Nanosflake Stability: Design Principles from an Ab Initio Investigation. Phys. Chem. Chem. Phys. 2019, 21, 23076−23084.

(92) Chen, S.; Gao, J.; Srinivasan, B. M.; Zhang, G.; Sorkin, V.; Hariharaputran, R.; Zhang, Y.-W. Origin of Ultrafast Growth of Monolayer WSe 2 via Chemical Vapor Deposition. Npj Comput. Mater. 2019, 5, No. 28.

(93) Ma, T.; Ren, W.; Zhang, X.; Liu, Z.; Gao, Y.; Yin, L.-C.; Ma, X.-L.; Ding, F.; Cheng, H.-M. Edge-Controlled Growth and Kinetics of Single-Crystal Graphene Domains by Chemical Vapor Deposition. Proc. Natl. Acad. Sci. U.S.A. 2013, 110, 20386−20391.

(94) Li, X.; Dong, J.; Idrobo, J. C.; Puretzky, A. A.; Rouleau, C. M.; Geohegan, D. B.; Ding, F.; Xiao, K. Edge-Controlled Growth and Etching of Two-Dimensional GaSe Monolayers. J. Am. Chem. Soc. 2017, 139, 482−491.

(95) Gao, Y.; Hong, Y.-L.; Yin, L.-C.; Wu, Z.; Yang, Z.; Chen, M.-L.; Liu, Z.; Ma, T.; Sun, D.-M.; Ni, Z.; Ma, X.-L.; Cheng, H.-M.; Ren, W.

Ultrafast Growth of High-Quality Monolayer WSe 2 on Au. *Adv. Mater.* 2017, 29, No. 1700990.

(96) Momeni, K.; Ji, Y.; Wang, Y.; Paul, S.; Neshani, S.; Yilmaz, D. E.; Shin, Y. K.; Zhang, D.; Jiang, J.-W.; Park, H. S.; Sinnott, S.; van Duin, A.; Crespi, V.; Chen, L.-Q. Multiscale Computational Understanding and Growth of 2D Materials: A Review. *Npj Comput. Mater.* 2020, 6, No. 22.

(97) Momeni, K.; Ji, Y.; Zhang, K.; Robinson, J. A.; Chen, L.-Q. Multiscale Framework for Simulation-Guided Growth of 2D Materials. *Npj 2D Mater. Appl.* 2018, 2, No. 27.