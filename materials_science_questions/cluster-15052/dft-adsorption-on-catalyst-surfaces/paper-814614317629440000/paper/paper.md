# A new C=C embedded porphyrin sheet with superior oxygen reduction performance

Yawei Li¹, Shunhong Zhang², Jiabing Yu¹, Qian Wang², Qiang Sun¹²³ (⊗), and Puru Jena³

¹ Department of Materials Science and Engineering, Peking University, Beijing 100871, China
² Center for Applied Physics and Technology, Peking University, Beijing 100871, China
³ Department of Physics, Virginia Commonwealth University, Richmond, VA 23284, USA

Received: 12 February 2015
Revised: 7 April 2015
Accepted: 14 April 2015

© Tsinghua University Press
and Springer-Verlag Berlin
Heidelberg 2015

## KEYWORDS
oxygen reduction reaction,
C=C porphyrin sheet,
density functional theory,
microkinetics modeling,
metal-free electrocatalysis

## ABSTRACT
C₂ is a well-known pseudo-oxygen unit with an electron affinity of 3.4 eV. We show that it can exhibit metal-ion like behavior when embedded in a porphyrin sheet and form a metal-free two-dimensional material with superior oxygen reduction performance. Here, the positively charged C=C units are highly active for oxygen reduction reaction (ORR) via dissociation pathways with a small energy barrier of 0.09 eV, much smaller than that of other non-platinum group metal (non-PGM) ORR catalysts. Using a microkinetics-based model, we calculated the partial current density to be 3.0 mA/cm² at 0.65 V vs. a standard hydrogen electrode (SHE), which is comparable to that of the state-of-the-art Pt/C catalyst. We further confirm that the C=C embedded porphyrin sheet is dynamically and thermally stable with a quasi-direct band gap of 1.14 eV. The superior catalytic performance and geometric stability make the metal-free C=C porphyrin sheet ideal for fuel cell applications.

## 1 Introduction
Because of the high theoretical efficiency, proton exchange membrane fuel cells (PEMFCs) have attracted considerable attention. Unlike combustion of conventional hydrogen or fossil fuels, PEMFCs offer solutions for green energy and mitigating global warming. However, sluggish oxygen reduction reaction (ORR) kinetics on the cathode is a major obstacle in the performance of PEMFCs [1]. The prototypical catalyst in PEMFC cathodes is Pt nanoparticles supported on carbon black (Pt/C), because they possess stable catalytic activity toward desired 4 electron (4e⁻) ORR. Unfortunately, there are several critical factors hampering the wider use of Pt/C as a commercial PEMFC cathode. First, an increase in catalytic activity by a factor of more than 4 per unit mass of Pt is required for practical automotive applications. Second, a 5-fold reduction in Pt usage in PEMFCs is necessary because of the high cost of Pt [2]. Third, loss of Pt surface area due to corrosive acidic electrolytes should be reduced to a minimum [1, 3]. Thus, it is desirable to develop

Address correspondence to sunqiang@pku.edu.cn

![](./images/814614317629440000_1.jpg)

non-platinum group metal (non-PGM) catalysts [4–15] with comparable, if not better, electrocatalytic ORR performance. Among the extensively studied systems, metal-free carbon-based ORR catalysts, such as N-doped carbon nanotubes [6], N-doped graphene [7], and $g\text{-}C_3N_4$ [8], are found to exhibit similar performance and better durability compared with traditional Pt/C catalysts. The advances in carbon-based ORR catalysts are motivating new research efforts, both experimentally and theoretically [16–25].

Unlike Pt-based catalysts, which interact strongly with $O_2$ through their d states near the Fermi level, the carbon-based ORR catalysts are electronically more inert and resistant to oxidation [22, 26]. $O_2$ adsorption and dissociation ($O_2(aq) \rightarrow O_2^* \rightarrow 2O^*$, * denotes surface species) on these materials are, thus, difficult because of large kinetic energy barriers [22]. Instead, $O_2$ adopts end-on adsorption configuration, with a favorable associative pathway ($O_2^* + H^+ + e^- \rightarrow OOH^*$) [16, 20–22, 26]. The carbon-based catalysts must be operated in alkaline electrolytes to lower the over-potential for the first electron transfer to un-dissociated $O_2$ [27]. Therefore, it is necessary to find metal-free catalysts that can bind and dissociate $O_2$ easily, so that oxygen reduction catalysis can be realized in acidic media.

To search for metal-free ORR catalysts for facile dissociation of $O_2$, it is important to incorporate two active sites that are adjacent to each other. Biologically inspired two-dimensional (2D) Fe/Co porphyrin sheets and their nanocomposites mimicking metalloporphyrin structure of chlorophyll and hemoglobin in nature have been identified as effective ORR catalysts [11, 12, 18, 28, 29]. Singly dispersed active metal sites only promote $O_2$ adsorption, but impede $O_2$ dissociation with relatively high energy barriers [30]. Recently, researchers have successfully incorporated a C=C dimer unit instead of a single metal atom into the center of the porphyrin ring [31]. This synthesis inspired us to investigate the ORR catalytic activity on a porphyrin sheet containing C=C units by using extensive first-principles calculations combined with microkinetics. We find that $O_2$ is easily adsorbed and dissociated on the C=C unit at the center of the porphyrin ring, with almost no energy barrier. Moreover, the facile $O_2$ dissociation is induced by an anti-aromatic to aromatic stabilizing effect that has never been discovered in any other non-PGM ORR catalysts. Our investigation suggests that the 2D C=C embedded porphyrin sheet is stable with excellent ORR performance, and can be used in acidic media where other metal-free catalysts exhibit weak performance.

## 2 Computational methods

Periodic calculations based on density functional theory (DFT) were performed using the Vienna *Ab initio* Simulation Package (VASP) 5.2 [32]. The ion-electron interaction was treated using the projector-augmented wave (PAW)[33] method. Exchange-correlation interactions were described by Perdew–Burke–Ernzerhof (PBE) functional[34] within the generalized gradient approximation (GGA). Wave functions of valence electrons were expanded using plane wave basis sets with a kinetic energy cutoff of 400 eV. K points in the Brillouin Zone were sampled using the Monkhorst-Pack method[35] with $3 \times 3 \times 1$ grids. We tested denser k-point sampling and the results were essentially the same. Partial occupancy of electrons was described using Gaussian smearing with a width of 0.01 eV. A vacuum space of $20 \mathring{A}$ was introduced in the direction normal to the nanosheets in order to avoid virtual interactions between the periodic images. Geometry optimizations were carried out using a conjugate gradient (CG) algorithm. Total energies and Hellmann-Feynman forces were converged to $10^{-4}$ eV and $0.02\ \text{eV}/\mathring{A}$, respectively. No symmetry constraints were imposed during the relaxation. Frequencies of adsorbates and free-standing molecules were calculated using the finite displacement method with a step size of $\pm 0.02\ \mathring{A}$. Zero-point energies of adsorbates and free-standing molecules were estimated based on the calculated frequencies. Entropies for gas phase molecules were taken from standard thermodynamic tables at 298.15 K and those for adsorbates were neglected because of the limited degree of freedom for the adsorbates. We further applied solvation corrections of –0.50 eV for $OH^*$, –0.30 eV for $OOH^*$, and –0.10 eV for other adsorbates because of the formation of hydrogen bonds. The energy values of solvation correction for different adsorbed species were justified by our molecular dynamics simulations with two water layers included, and they were in qualitative agreement with

![](./images/814614317629440000_2.jpg)
![](./images/814614317629440000_3.jpg)
| www.editorialmanager.com/nare/default.asp

values set by previous theoretical investigations on ORR catalyzed by other surfaces [23, 25, 36, 37]. The DFT computed energies could then be converted into free energies by taking into consideration the zero-point energies, the entropies, as well as solvation corrections. The free energy of molecular $O_{2}$ was calculated with respect to $H_{2}$ and $H_{2}O$ to avoid the well-known poor description by the PBE functional [38]. Transition states were located using the nudged elastic band (NEB) [39] method as well as the improved dimer method [40]. The free energy changes between transition states and reactants were approximated by DFT-computed single point energy variations.

Dynamical stability of a C=C embedded porphyrin nanosheet was confirmed by calculating its phonon spectra in the whole Brillouin Zone based on linear response theory. Before the calculation of the phonons, the structures were re-optimized using a higher convergence criteria, namely, $10^{-8}$ eV for total energy and $10^{-6}$ eV/Å for Hellmann–Feynman Force, respectively. Ab initio molecular dynamics (AIMD) simulations were performed within a $2×2×1$ supercell to investigate the thermal stability. For this purpose, the energy convergence criterion and time steps were set to $5×10^{-4}$ eV/supercell and 1 fs, respectively. Each simulation lasted for over 5 ps. The canonical (NVT) ensemble was implemented in the simulation and the heat bath was realized by means of a Nosé thermostat [41]. To ensure accurate band gap estimation, we chose the hybrid Heyd–Scuseria–Ernzerhof functional (HSE06) [42, 43] instead of PBE to perform band structure calculations.

To understand the mechanisms involved in C=C embedded porphyrin sheet, we also carried out cluster calculations using the Gaussian 09 code [44]. Cluster calculations have been extensively used in previous studies of surface reactions such as ORR catalysis on doped graphene [45] and graphene oxidation loci distribution [46]. Furthermore, they have been proven to successfully account for electronic phenomena that happen during $H_{2}$ and $CO_{2}$ adsorption on metal phthalocyanine sheets in our previous works [47, 48]. Geometry optimization and frequency analysis were performed at the B3LYP/6-311G* level [49, 50] without any symmetry constraints. Quadratic synchronous transit (QST)[51] protocol was employed to locate the transition states. Natural bond orbital (NBO) analyses were performed using NBO 3.1 [52, 53] integrated in Gaussian 09. To manifest the aromaticity of planar and quasi-planar cluster models, a newly developed iso-chemical shielding surfaces (ICSS) method [54] was employed. This approach resembles the well-known nucleus-independent chemical shift (NICS) method [55]. However, ICSS calculation is handled in a three-dimensional grid of lattice points and direction and anisotropy effects can be quantified in a more straightforward way. Moreover, contrary to the NICS approach, positive ICSS values indicate diatropic ring currents and aromaticity, while negative values indicate paratropic ring currents and antiaromaticity. Here, we used $ICSS_{zz}(1)$, the shielding tensor component perpendicular to the studied ring planes at 1 Å above them, to better characterize $\pi$-electron aromaticity. $ICSS_{zz}(1)$ analyses were conducted using Gaussian 09 and Multiwfn 3.3.3 [56] at the B3LYP/6-311G* level of theory. The corresponding NBO and $ICSS_{zz}(1)$ results were visualized by VMD 1.9.1 [57].

## 3 Results and discussion
### 3.1 Stability
The geometrical structure of a C=C embedded porphyrin sheet is shown in Fig. 1(a). When in molecular form, both neutral and dicationic C=C embedded porphyrin adopt ruffled configurations [31]. However, in a 2D sheet, the periodic arrangement of the units enlarges the C=C bond length, resulting in a planar geometry. The primitive cell is rectangular with lattice parameters of 8.53 and 8.11 Å. Such a geometrical distinction between a C=C embedded porphyrin molecule and an extended C=C embedded porphyrin sheet is similar to those between polycyclic aromatic hydrocarbons with pentagonal defects (buckled)[58] and pentagon-containing Stone-Wales graphene sheets (planar) [59], as well as that between $B_{36}$ (buckled) [60] and $\alpha$-Boron (planar) [61, 62].

The ultimate prerequisite for a material to become an ORR catalyst is its stability. The calculated phonon dispersion spectra (see Fig. 1(b)) show no imaginary frequency modes, indicating that the planar C=C embedded porphyrin sheet is dynamically stable and

![](./images/814614317629440000_4.jpg)

Figure 1 (a) Top and side views of planar 2D C=C embedded porphyrin sheet. The primitive unit cell is marked by dashed magenta rectangle; (b) phonon dispersion; (c) band structure using HSE06 functional; (d) variation of total energy and geometry snapshot at 5 ps during AIMD simulation at 300 K; (e) ELF contour taken at 1 Å above the base plane.

can exist as a freestanding 2D crystal. The variation of the total energy as well as the snapshots of the atomic configuration during AIMD simulation is shown in Fig. 1(d). Both of these quantities remain almost invariant, and no notable buckling of geometry occurs. These results demonstrate that the studied planar C=C embedded porphyrin sheet, once synthesized for ORR applications, can remain robust at room temperature. Our free energy analyses further prove that under ORR operating potentials and acidic pH = 0, the C=C dimer in the embedded porphyrin sheet is resistant to dissociation into acetylene (Fig. S1 in the Electronic Supplementary Material (ESM)), corroborating its stability against corrosive acidic media.

### 3.2 Catalytic ORR reaction paths

In addition to superior stability, the C=C embedded porphyrin sheet possesses a narrow band gap of only 1.14 eV (Fig. 1(c)), making it promising for (photo-) electrochemical applications. Therefore, we next aim for better insight into the electron population and bonding nature of C=C embedded porphyrin sheet, in order to identify possible active sites. Bader charge analysis [63-65] and electron localization function (ELF) analysis [66-68] were performed. Large charge depletion is found on the C=C unit at the center of the porphyrin ring. Each of the two C atoms of the C=C unit carries a positive charge of $+0.67e$, which is much larger than that in any of the other C atoms (Table S1 in the ESM). We attribute this to a synergetic effect between the electron-withdrawing ability of N atoms and the electron localized characteristic of C=C unit. The ELF slice taken at 1 Å above the C=C embedded porphyrin sheet (see Fig. 1(e)) clearly indicates that the $\pi$-electron density along the peripheral porphyrin ring is highly delocalized, while the $\pi$-electron density on the C=C dimer is strongly localized and does not conjugate with that along

the porphyrin ring. The notable electron-deficient characteristic on the C=C dimer induced by adjacent N atoms is, therefore, preserved by the localized π-electron density, whereas positive electron densities on other C atoms are much smaller. Previous theoretical investigations have suggested that positive electron density or spin density induced by breaking electron delocalization plays a significant role in facilitating the ORR process [16]. Therefore, we wonder whether the positively charged C=C dimer would catalyze ORR like Fe or Co ions in the corresponding metalloporphyrin sheets.

According to our results, the 2D C=C embedded porphyrin sheet can indeed easily catalyze ORR via low-barrier reaction pathways. First, we consider O₂ adsorption. As anticipated, the most favorable site for O₂ adsorption is the localized C=C dimer site. The free-standing O₂ molecule prefers to adsorb on the embedded C=C site in a side-on configuration, with each of the two O atoms binding to either of the two C atoms. Unlike other reported metal-free carbon-based catalysts having strong resistance to oxidation [22], O₂ adsorption on the embedded C=C site is spontaneous without any kinetic barrier. Bader charge analysis indicates that each O atom carries a net negative charge of -0.50e, and each C atom of the C=C dimer possesses a +1.10e positive charge (0.43e charge depletion, compared with the case in free-standing 2D C=C porphyrin sheet). The large charge transfer between the adsorbed O₂ and localized C=C dimer suggests that O₂ is strongly activated upon adsorption. As a result of such charge transfer mediated activation, the O-O bond length in adsorbed O₂ is elongated from 1.22 to 1.51 Å, rendering it facile to dissociate the O-O bond in successive reduction steps.

In order to identify the most favorable O₂ reduction mechanism on the C=C embedded porphyrin sheet, we plotted the free energy profiles with kinetic energy barriers in Fig. 2. We took into account both proton-coupled electron transfer (PCET) and surface H (denoted as H* in Fig. 2)-assisted reduction steps. However, in this work we mainly focus on PCET steps, because they generally have much smaller barriers than H-assisted reduction steps. We neglect the kinetic energy barrier for PCET steps because of the following two reasons: (1) Previous theoretical investigations have suggested that the kinetic barriers for PCET are easily surmountable at room temperature [23, 24, 69-72] because of a Brønsted-Evans-Polanyi relation [73, 74]. (2) Our DFT calculations reveal that when using H to simulate one pair of coupled H⁺ and e⁻, the barrier for O* hydrogenation to OH* on C=C embedded porphyrin sheet is only ~0.15 eV, which is too small to act as a rate-determining step (see Fig. S2 in the ESM).

In the electrochemical reactions that incorporate PCET steps, the free energy change of each PCET step can be regulated by applied potential, according to a recently developed computational hydrogen electrode (CHE) model [75] (details can be found in the supporting information). The rate-determining step (RDS) and the onset potential are defined therein as the step with the least negative free energy change when the kinetic barrier is small and the potential at which the free energy change of RDS becomes zero.

In acidic electrolytes, aqueous O₂ either adsorbs on the C=C embedded porphyrin sheet as O₂* or directly binds to H⁺ to become OOH⁺ [76] and subsequently adsorbs on the surface as OOH*. Starting with both initial adsorbates, we find that O₂* direct dissociation (O₂* → TS1 → 2O* in Fig. 2) and H⁺-mediated O₂ dissociation (O₂* → O* + OH* in Fig. 2) are each facile with kinetic barriers of 0.09 and 0 eV, respectively. The RDS for both kinds of dissociative pathways is OH* + OH* → OH* + H₂O with a free energy change of -0.40 eV. In contrast, OOH*-mediated associative pathway encounters a rougher RDS O* + H₂O → OH* + H₂O with a free energy change of 0.01 eV. The corresponding onset potentials for both dissociative and associative steps are therefore 0.40 and -0.01 V, respectively. The much larger onset potential value for dissociative steps indicate that both direct and H⁺-mediated O₂ dissociation mechanisms are the most favorable on a C=C embedded porphyrin sheet. The preference for O₂ dissociation decreases the possibility of H₂O₂ byproduct generation from OOH* (see Fig. 2). Furthermore, the thermodynamic barrier for H* formation and reaction with aqueous H⁺ (Volmer-Heyrovsky steps, Fig. S3 in the ESM), as well as the kinetic inhibition for two surface-bound H* to directly produce H₂ (Volmer-Tafel steps, Fig. S4 in the ESM), means that a hydrogen evolution reaction (HER) will

![](./images/814614317629440000_5.jpg)

Figure 2 (a) The whole ORR reaction free energy profile for a 2D porphyrin sheet embedded with C=C at 0 V vs. SHE. Regions with different colors denote different numbers of PCET steps. The most preferable dissociative reaction pathways are illustrated with dashed black lines. The reactants via both dissociative and associative mechanisms are marked in blue. (b) Geometry configurations of all reactants, reaction intermediates, transition states, and products corresponding to those are denoted in (a). Note that 2O* is simplified as O*, OH*+OH* is simplified as OH*, and O*+OH* is simplified as O-OH* in Fig. 4 and Fig. S7 in the ESM.

not compete with ORR at investigated potentials. All of these facts suggest that an efficient $4e^-$ ORR route happens on a C=C embedded porphyrin sheet.

### 3.3 Mechanism for the facile dissociation of $O_2$

According to the above reaction energy profile, the $O_2$ dissociation pathways are clearly dominant in the whole catalytic ORR process, because of both the higher onset potential and negligible kinetic barriers. The facile $O_2$ dissociation on the C=C embedded porphyrin sheet (dissociation barrier $E_a = 0.09$ eV) not only seems unique among all the reported metal-free catalysts but also surpasses most of the state-of-the-art ORR catalysts such as the Pt surface ($E_a = 0.58$ eV in gas phase calculations and 0.27 eV/0.74 eV in water solvated phase calculations) [77, 78] or even porphyrin-like Fe-$N_4$ catalysts ($E_a = 1.19$ eV) [30]. It is interesting to note that the oxygen dissociation barrier has been substantially reduced when a C=C dimer instead of an Fe ion is embedded into the porphyrin sheet. The geometrical configuration of the embedded C=C dimer enables easier O migration, in contrast to the fact that O atom needs to migrate a much longer path to the C atom in the porphyrin ring during $O_2$ dissociation on the embedded single Fe ion. Furthermore, we find that the electronic factor, namely, the anti-aromatic to aromatic

transformation induced by pronounced charge transfer, is the decisive factor that promotes $O_2$ dissociation on a metal-free sheet.

As molecular $O_2$ approaches the highly positively charged $C=C$ unit, it becomes adsorbed because of the strong hybridization between the bonding orbital of $C=C$ embedded porphyrin and anti-bonding orbital of $O_2$. Both $\pi$ bonds in the $C=C$ unit and $O_2$ diminish, leaving only $\sigma$ bonds between them. At the same time, new $C-O$ $\sigma$ bonds are generated, as confirmed by NBO analysis in Fig. S5 (in the ESM). Based on ICSS calculation, we find that the $\pi$-electron delocalization is highly anti-aromatic inside the ring of $C=C$ porphyrin-$O_2$ complex because of limited electron transfer from the $C=C$ embedded porphyrin to $O_2$ (1.22$e$ using Bader charge analysis), making it resemble the case of neutral $C=C$ porphyrin (see Figs. 3(a) and 3(c)). The anti-aromatic $C=C$ porphyrin-$O_2$ complex is, therefore, highly active and undergoes internal charge rearrangement. The porphyrin ring transfers more electrons to the anti-bonding orbital of $O_2$. As a result, the remaining O-O $\sigma$ bond is broken and $O_2$ finally dissociates. Interestingly, when $O_2$ undergoes dissociation and generates $C=C$ porphyrin-2O complex, $\pi$ electrons inside the whole molecule ring dramatically change from anti-aromatic to aromatic, reminiscent of a high $\pi$-electron aromaticity inside the dicationic $C=C$ porphyrin molecule (see Figs. 3(b) and 3(d)). The induced aromatic characteristic enhances the stabilization of the whole system. Bader charge analysis indicates that because of the large electronegativity of atomic O ($\chi$ = 3.44), 2.20$e$ net charge is transferred from the $C=C$ embedded porphyrin to two dissociated O atoms after $O_2$ dissociation. This makes the $C=C$ porphyrin moiety in $C=C$ porphyrin-2O complex nearly dicationic, consistent with $ICSS_{zz}(1)$ results. Therefore, the facile dissociation of $O_2$, once it is adsorbed, can be attributed to an increased amount of internal charge transfer. The dicationic characteristic of $C=C$ embedded porphyrin ring, due to the reinforced electron loss, endows the $C=C$ porphyrin-2O complex aromaticity. It further indicates that the $C=C$ embedded porphyrin sheet is capable of both $O_2$ adsorption and dissociation, owing to its peculiar electronic structure that other metal-free ORR catalysts do not possess.

![](./images/814614317629440000_6.jpg)

Figure 3 Results of $ICSS_{zz}(1)$ analyses for four different kinds of molecular $C=C$ porphyrin units: (a) slice of $ICSS_{zz}(1)$ value of neutral $C=C$ porphyrin and (b) slice of $ICSS_{zz}(1)$ value of dicationic $C=C$ porphyrin; (c) isosurface of $ICSS_{zz}(1)$ value of $C=C$ porphyrin-$O_2$ complex and (d) isosurface of $ICSS_{zz}(1)$ value of $C=C$ porphyrin-2O complex. Red and blue colors indicate aromatic and anti-aromatic regions, respectively. Isovalue is taken as 15 $e/\mathring{A}^3$.

### 3.4 ORR catalytic activity

From a purely thermodynamics point of view, we are able to identify the most preferable dissociative reaction pathways of ORR process on the $C=C$ embedded porphyrin sheet. $O_2$ facile dissociation renders metal-free ORR catalysts in acidic electrolytes possible and increases selectivity toward a more efficient $4e^-$ ORR process. However, detailed investigation of real-world catalytic activity is of more interest. By combining a thermodynamic free energy profile with a microkinetics analysis [79], we are able to calculate the theoretical partial current density under a given potential. We can then directly compare both ORR activity and efficiency with reported catalysts by referring to partial current density and the corresponding applied potential.

Based on the transition state theory, the forward reaction rate constant for a non-electrochemical step $i$ is

$$
k_{i}=\frac{k_{\mathrm{B}} T}{h} \mathrm{e}^{-\frac{\Delta G_{\mathrm{a} i}^{*}}{k_{\mathrm{B}} T}} \approx \frac{k_{\mathrm{B}} T}{h} \mathrm{e}^{-\frac{E_{\mathrm{a} i}}{k_{\mathrm{B}} T}}
\tag{1}
$$

where $k_{\mathrm{B}}$ is the Boltzmann constant, $h$ is the Planck constant, $\Delta G_{\mathrm{a} i}^{*}$ is the activation free energy, and $E_{\mathrm{a} i}$ is the DFT-computed activation energy for step $i$.

Therefore, the reverse reaction rate constant for non-electrochemical steps is

$$
k_{-i}=\frac{k_{i}}{K_{i}}=\frac{\frac{k_{\mathrm{B}} T}{h} \mathrm{e}^{-\frac{E_{\mathrm{ai}}}{k_{\mathrm{B}} T}}}{\mathrm{e}^{\frac{\Delta G_{i}}{k_{\mathrm{B}} T}}}
\tag{2}
$$

where $\Delta G_{i}$ is the reaction free energy change for step $i$.

For an electrochemical step $j$ that includes proton-electron couple transfer, the forward rate constant is

$$
k_{j}=A_{j} \mathrm{e}^{-\frac{E_{\mathrm{a} j}^{\mathrm{elec}}}{k_{\mathrm{B}} T}} \mathrm{e}^{\frac{e \beta\left(U-U_{j}^{0}\right)}{k_{\mathrm{B}} T}}
\tag{3}
$$

where $A_{j}$ is the effective pre-factor, $E_{\mathrm{a} j}^{\mathrm{elec}}$ is the activation energy for PCET processes, $\beta$ is the symmetric factor, $U$ is the applied potential, and $U_{j}^{0}$ is equal to $-\frac{\Delta G_{j}^{0}}{e}$. ($\Delta G_{j}^{0}$ is the potential-dependent reaction free energy change of step $j$.)

The backward rate constant for electrochemical steps is

$$
k_{-j}=\frac{k_{j}}{K_{j}}=\frac{A_{j} \mathrm{e}^{-\frac{E_{\mathrm{a} j}^{\mathrm{elec}}}{k_{\mathrm{B}} T}} \mathrm{e}^{\frac{e \beta\left(U-U_{j}^{0}\right)}{k_{\mathrm{B}} T}}}{\mathrm{e}^{-\frac{e\left(U-U_{j}^{0}\right)}{k_{\mathrm{B}} T}}}=A_{j} \mathrm{e}^{-\frac{E_{\mathrm{a} j}^{\mathrm{elec}}}{k_{\mathrm{B}} T}} \mathrm{e}^{\frac{e(1-\beta)\left(U-U_{j}^{0}\right)}{k_{\mathrm{B}} T}}
\tag{4}
$$

Because the C=C dimer active sites are separated from each other, we regard the C=C dimer site as a whole. For simplicity, we denote dissociative reaction intermediates as follows: $2\mathrm{O}^{*}$ as $\mathrm{O}^{*}$, $2\mathrm{OH}^{*}$ as $\mathrm{OH}^{*}$, $\mathrm{O}+\mathrm{OH}^{*}$ as $\mathrm{O}-\mathrm{OH}^{*}$, and $\mathrm{OH}^{* *}$ as $*$. If we denote surface coverage of each adsorbate during ORR as $\theta_{a}$, then, based on the steady-state approximation, the generation and elimination of each adsorbate will be in equilibrium, that is

$$
\frac{\partial \theta_{\mathrm{a}}}{\partial t}=0
\tag{5}
$$

Taking the following electrochemical reactions as an example,

$$
2 \mathrm{O}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \underset{k_{-1}}{\stackrel{k_{1}}{\rightleftharpoons}} \mathrm{O}^{*}+\mathrm{OH}^{*}
$$

$$
\mathrm{O}^{*}+\mathrm{OH}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \underset{k_{-2}}{\stackrel{k_{2}}{\rightleftharpoons}} 2 \mathrm{OH}^{*}
$$

the reaction rate of $\mathrm{O}+\mathrm{OH}^{*}$ can be calculated according to Eq. (6)

$$
\frac{\partial \theta_{\mathrm{O}-\mathrm{OH}^{*}}}{\partial t}=2 k_{1} \theta_{\mathrm{O}^{*}}-k_{-1} \theta_{\mathrm{O}-\mathrm{OH}^{*}}-k_{2} \theta_{\mathrm{O}-\mathrm{OH}^{*}}+2 k_{-2} \theta_{\mathrm{OH}^{*}}=0
\tag{6}
$$

Apart from steady-state approximation, the total coverage of all adsorbates conforms to site conserving rules

$$
\theta_{\mathrm{O}_{2}{ }^{*}}+\theta_{\mathrm{O}^{*}}+\theta_{\mathrm{O}-\mathrm{OH}^{*}}+\theta_{\mathrm{OH}^{*}}+\theta_{*}+\theta_{* *}=1
\tag{7}
$$

The coverages of adsorbates as well as partial current density can thus be solved analytically (details of further parameter fitting and approximation can be found in the supporting information).

Both the rate coefficient and the equilibrium constant of $\mathrm{O}_{2}$ dissociation to surface adsorbed $\mathrm{O}^{*}$ are quite large because of the extremely small activation barrier and negative reaction free energy. Therefore, the surface concentration of $\mathrm{O}_{2}{ }^{*}$ is negligible. Instead, the dominant surface species are mainly $\mathrm{O}^{*}$, $\mathrm{O}-\mathrm{OH}^{*}$, and double surface bare C–C site (**), as illustrated in Fig. 4(a). Under an applied potential of about 0.67 V (equal to only 0.56 V overpotential, comparable to ORR catalyzed by pyridinic N-doped graphene [23]), the relative surface concentration between the double bare C–C site and $\mathrm{O}-\mathrm{OH}^{*}$ changes sharply, leading to a large and sharp increase in partial current density from 0 to about $3.0\ \mathrm{mA/cm^{2}}$ (see Fig. 4(b)), which is comparable to that generated by the Pt-based catalyst from both experimental ($5.8\ \mathrm{mA/cm^{2}}$) [80] and theoretical ($6\ \mathrm{mA/cm^{2}}$ at 1,600 rpm) [81] perspectives. Moreover, the applied potential inducing partial current change is as large as 0.67 eV, which is within the ideal range of reported experimental data on half-wave potential in carbon-based catalysts [22]. Therefore, the micro-kinetically estimated results further support our claim that a C=C embedded porphyrin sheet can be a potential ORR catalyst.

![](./images/814614317629440000_7.jpg)
![](./images/814614317629440000_8.jpg)
www.editorialmanager.com/nare/default.asp

![](./images/814614317629440000_9.jpg)

Figure 4 Microkinetics results for a 2D C=C porphyrin sheet in catalyzing ORR under different applied cathode potentials vs. SHE.
(a) Variation of dominant surface species; (b) variation of partial current density.

## 4 Conclusions

Based on extensive calculations and analyses, we make the following conclusions: (1) The 2D C=C embedded porphyrin sheet is stable dynamically as well as ther- mally at room temperature. (2) Although $C_{2}$ dimer in the gas phase is a good electron acceptor with an electron affinity of 3.4 eV, it becomes a positively charged unit when embedded in porphyrin, and is highly active for ORR via dissociation pathways with a small energy barrier of 0.09 eV, much smaller than that of other non-PGM ORR catalysts. (3) The enhanced charge transfer in the dissociation pathway of $O_{2}$ on the sheet induces an antiaromatic-to-aromatic transition. (4) The partial current density of the sheet at 0.65 V vs. SHE is comparable to that of the state-of-the-art Pt/C catalyst. This study provides a good example for discovering new non-PGM PEMFC cathode catalysts that dissociate $O_{2}$ like Pt, but with better performance in acidic media. We hope that the present study will stimulate further experimental effort in this field.

## Acknowledgements

Q. S. acknowledges the grants from the National Natural Science Foundation of China (No. 21173007 and 11274023), the National Basic Research Program of China (No. 2012CB921404). P. J. acknowledges the grants from the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering under Award # DE-FG02-96ER45579.

Electronic Supplementary Material: Supplementary material (details of the computational hydrogen electrode model, details of microkinetic analysis and Figs. S1-S8) is available in the online version of this article at http://dx.doi.org/ 10.1007/s12274-015-0795-x.

## References

[1] Rabis, A.; Rodriguez, P.; Schmidt, T. J. Electrocatalysis for polymer electrolyte fuel cells: Recent achievements and future challenges. *ACS Catal.* 2012, 2, 864-890.

[2] Gasteiger, H. A.; Kocha, S. S.; Sompalli, B.; Wagner, F. T. Activity benchmarks and requirements for Pt, Pt-alloy, and non-Pt oxygen reduction catalysts for PEMFCs. *Appl. Catal. B: Environ.* 2005, 56, 9-35.

[3] Ramírez-Caballero, G. E.; Balbuena, P. B. Dissolution- resistant core-shell materials for acid medium oxygen reduction electrocatalysts. *J. Phys. Chem. Lett.* 2010, 1, 724-728.

[4] Lefèvre, M.; Proietti, E.; Jaouen, F.; Dodelet, J.-P. Iron- based catalysts with improved oxygen reduction activity in polymer electrolyte fuel cells. *Science* 2009, 324, 71-74.

[5] Cheng, F. Y.; Shen, J.; Peng, B.; Pan, Y. D.; Tao, Z. L.; Chen, J. Rapid room-temperature synthesis of nanocrystalline spinels as oxygen reduction and evolution electrocatalysts. *Nat. Chem.* 2011, 3, 79-84.

[6] Gong, K. P.; Du, F.; Xia, Z. H.; Durstock, M.; Dai, L. M. Nitrogen-doped carbon nanotube arrays with high

electrocatalytic activity for oxygen reduction. *Science* **2009**, 323, 760-764.

[7] Qu, L. T.; Liu, Y.; Baek, J.-B.; Dai, L. M. Nitrogen-doped graphene as efficient metal-free electrocatalyst for oxygen reduction in fuel cells. *ACS Nano* **2010**, 4, 1321-1326.

[8] Zheng, Y.; Jiao, Y.; Chen, J.; Liu, J.; Liang, J.; Du, A. J.; Zhang, W. M.; Zhu, Z. H.; Smith, S. C.; Jaroniec, M. et al. Nanoporous graphitic-$\text{C}_3\text{N}_4$@carbon metal-free electrocatalysts for highly efficient oxygen reduction. *J. Am. Chem. Soc.* **2011**, 133, 20116-20119.

[9] Bashyam, R.; Zelenay, P. A class of non-precious metal composite catalysts for fuel cells. *Nature* **2006**, 443, 63-66.

[10] Grumelli, D.; Wurster, B.; Stepanow, S.; Kern, K. Bio-inspired nanocatalysts for the oxygen reduction reaction. *Nat. Commun.* **2013**, 4, 2904.

[11] Yuan, S. W.; Shui, J.-L.; Grabstanowicz, L.; Chen, C.; Commet, S.; Reprogle, B.; Xu, T.; Yu, L. P.; Liu, D.-J. A highly active and support-free oxygen reduction catalyst prepared from ultrahigh-surface-area porous polyporphyrin. *Angew. Chem., Int. Ed.* **2013**, 52, 8349-8353.

[12] Xiang, Z. H.; Xue, Y. H.; Cao, D. P.; Huang, L.; Chen, J.-F.; Dai, L. M. Highly efficient electrocatalysts for oxygen reduction based on 2D covalent organic polymers complexed with non-precious metals. *Angew. Chem., Int. Ed.* **2014**, 53, 2433-2437.

[13] Li, W. M.; Yu, A. P.; Higgins, D. C.; Llanos, B. G.; Chen, Z. W. Biologically inspired highly durable iron phthalocyanine catalysts for oxygen reduction reaction in polymer electrolyte membrane fuel cells. *J. Am. Chem. Soc.* **2010**, 132, 17056-17058.

[14] Liu, Z. Y.; Zhang, G. X.; Lu, Z. Y.; Jin, X. Y.; Chang, Z.; Sun, X. M. One-step scalable preparation of N-doped nano-porous carbon as a high-performance electrocatalyst for the oxygen reduction reaction. *Nano Res.* **2013**, 6, 293-301.

[15] Han, C. L.; Wang, S. P.; Wang, J.; Li, M. M.; Deng, J.; Li, H. R.; Wang, Y. Controlled synthesis of sustainable N-doped hollow core-mesoporous shell carbonaceous nanospheres from biomass. *Nano Res.* **2014**, 7, 1809-1819.

[16] Zhang, L. P.; Xia, Z. H. Mechanisms of oxygen reduction reaction on nitrogen-doped graphene for fuel cells. *J. Phys. Chem. C* **2011**, 115, 11170-11176.

[17] Hijazi, I.; Bourgeteau, T.; Cornut, R.; Morozan, A.; Filoramo, A.; Leroy, J.; Derycke, V.; Jousselme, B.; Campidelli, S. Carbon nanotube-templated synthesis of covalent porphyrin network for oxygen reduction reaction. *J. Am. Chem. Soc.* **2014**, 136, 6348-6354.

[18] Jahan, M.; Bao, Q. L.; Loh, K. P. Electrocatalytically active graphene-porphyrin MOF composite for oxygen reduction reaction. *J. Am. Chem. Soc.* **2012**, 134, 6707-6713.

[19] Jiao, Y.; Zheng, Y.; Jaroniec, M.; Qiao, S. Z. Origin of the electrocatalytic oxygen reduction activity of graphene-based catalysts: A roadmap to achieve the best performance. *J. Am. Chem. Soc.* **2014**, 136, 4394-4403.

[20] Uosaki, K.; Elumalai, G.; Noguchi, H.; Masuda, T.; Lyalin, A.; Nakayama, A.; Taketsugu, T. Boron nitride nanosheet on gold as an electrocatalyst for oxygen reduction reaction: Theoretical suggestion and experimental proof. *J. Am. Chem. Soc.* **2014**, 136, 6542-6545.

[21] Lyalin, A.; Nakayama, A.; Uosaki, K.; Taketsugu, T. Functionalization of monolayer h-BN by a metal support for the oxygen reduction reaction. *J. Phys. Chem. C* **2013**, 117, 21359-21370.

[22] Chai, G.-L.; Hou, Z. F.; Shu, D.-J.; Ikeda, T.; Terakura, K. Active sites and mechanisms for oxygen reduction reaction on nitrogen-doped carbon alloy catalysts: Stone-Wales defect and curvature effect. *J. Am. Chem. Soc.* **2014**, 136, 13629-13640.

[23] Saidi, W. A. Oxygen reduction electrocatalysis using N-doped graphene quantum-dots. *J. Phys. Chem. Lett.* **2013**, 4, 4160-4165.

[24] Gao, F.; Zhao, G.-L.; Yang, S. Z. Catalytic reactions on the open-edge sites of nitrogen-doped carbon nanotubes as cathode catalyst for hydrogen fuel cells. *ACS Catal.* **2014**, 4, 1267-1273.

[25] Yu, L.; Pan, X. L.; Cao, X. M.; Hu, P.; Bao, X. H. Oxygen reduction reaction mechanism on nitrogen-doped graphene: A density functional theory study. *J. Catal.* **2011**, 282, 183-190.

[26] Ikeda, T.; Boero, M.; Huang, S.-F.; Terakura, K.; Oshima, M.; Ozaki, J. Carbon alloy catalysts: Active sites for oxygen reduction reaction. *J. Phys. Chem. C* **2008**, 112, 14706-14709.

[27] Wang, D.-W.; Su, D. S. Heterogeneous nanocarbon materials for oxygen reduction reaction. *Energy Environ. Sci.* **2014**, 7, 576-591.

[28] Wang, X. X.; Yang, J. D.; Yin, H. J.; Song, R.; Tang, Z. Y. "Raisin bun"-like nanocomposites of palladium clusters and porphyrin for superior formic acid oxidation. *Adv. Mater.* **2013**, 25, 2728-2732.

[29] Tang, H. J.; Yin, H. J.; Wang, J. Y.; Yang, N. L.; Wang, D.; Tang, Z. Y. Molecular architecture of cobalt porphyrin multilayers on reduced graphene oxide sheets for high-performance oxygen reduction reaction. *Angew. Chem., Int. Ed.* **2013**, 52, 5585-5589.

[30] Kattel, S.; Wang, G. F. Reaction pathway for oxygen reduction on $\text{FeN}_4$ embedded graphene. *J. Phys. Chem. Lett.* **2014**, 5, 452-456.

[31] Vaid, T. P. A porphyrin with a C=C unit at its center. *J. Am.

![](./images/814614317629440000_10.jpg)

Chem. Soc. 2011, 133, 15838-15841.

[32] Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 1996, 54, 11169-11186.

[33] Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 1994, 50, 17953-17979.

[34] Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 1996, 77, 3865-3868.

[35] Monkhorst, H. J.; Pack, J. D. Special points for Brillouin-zone integrations. Phys. Rev. B 1976, 13, 5188-5192.

[36] Tripković, V.; Skúlason, E.; Siahrostami, S.; Nørskov, J. K.; Rossmeisl, J. The oxygen reduction reaction mechanism on Pt(111) from density functional theory calculations. Electrochim. Acta 2010, 55, 7975-7981.

[37] Calle-Vallejo, F.; Martinez, J. I.; Rossmeisl, J. Density functional studies of functionalized graphitic materials with late transition metals for oxygen reduction reactions. Phys. Chem. Chem. Phys. 2011, 13, 15639-15643.

[38] Calle-Vallejo, F.; Martínez, J. I.; García-Lastra, J. M.; Mogensen, M.; Rossmeisl, J. Trends in stability of perovskite oxides. Angew. Chem., Int. Ed. 2010, 49, 7699-7701.

[39] Mills, G.; Jónsson, H. Quantum and thermal effects in $H_2$ dissociative adsorption: Evaluation of free energy barriers in multidimensional quantum systems. Phys. Rev. Lett. 1994, 72, 1124-1127.

[40] Heyden, A.; Bell, A. T.; Keil, F. J. Efficient methods for finding transition states in chemical reactions: Comparison of improved dimer method and partitioned rational function optimization method. J. Chem. Phys. 2005, 123, 224101.

[41] Nosé, S. A unified formulation of the constant temperature molecular dynamics methods. J. Chem. Phys. 1984, 81, 511-519.

[42] Heyd, J.; Scuseria, G. E.; Ernzerhof, M. Hybrid functionals based on a screened Coulomb potential. J. Chem. Phys. 2003, 118, 8207-8215.

[43] Heyd, J.; Scuseria, G. E.; Ernzerhof, M. Erratum: "Hybrid functionals based on a screened Coulomb potential" [J. Chem. Phys. 118, 8207 (2003)]. J. Chem. Phys. 2006, 124, 219906.

[44] Frisch, M. J. T., G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Mennucci, B.; Petersson, G. A.; Nakatsuji, H.; Caricato, M.; Li, X.; Hratchian, H. P.; Izmaylov, A. F.; Bloino, J.; Zheng, G.; Sonnenberg, J. L.; Hada, M.; Ehara, M.; Toyota, K.; Fukuda, R.; Hasegawa, J.; Ishida, M.; Nakajima, T.; Honda, Y.; Kitao, O.; Nakai, H.; Vreven, T.; Montgomery, J. A., Jr.; Peralta, J. E.; Ogliaro, F.; Bearpark, M.; Heyd, J. J.; Brothers, E.; Kudin, K. N.; Staroverov, V. N.; Kobayashi, R.; Normand, J.; Raghavachari, K.; Rendell, A.; Burant, J. C.; Iyengar, S. S.; Tomasi, J.; Cossi, M.; Rega, N.; Millam, N. J.; Klene, M.; Knox, J. E.; Cross, J. B.; Bakken, V.; Adamo, C.; Jaramillo, J.; Gomperts, R.; Stratmann, R. E.; Yazyev, O.; Austin, A. J.; Cammi, R.; Pomelli, C.; Ochterski, J. W.; Martin, R. L.; Morokuma, K.; Zakrzewski, V. G.; Voth, G. A.; Salvador, P.; Dannenberg, J. J.; Dapprich, S.; Daniels, A. D.; Farkas, Ö.; Foresman, J. B.; Ortiz, J. V.; Cioslowski, J.; Fox, D. J. GAUSSIAN 09, Revision C.01; Gaussian, Inc.: Wallingford, CT, 2010.

[45] Zheng, Y.; Jiao, Y.; Ge, L.; Jaroniec, M.; Qiao, S. Z. Two-step boron and nitrogen doping in graphene for enhanced synergistic catalysis. Angew. Chem., Int. Ed. 2013, 52, 3110-3116.

[46] Yang, J. R.; Shi, G. S.; Tu, Y. S.; Fang, H. P. High correlation between oxidation loci on graphene oxide. Angew. Chem., Int. Ed. 2014, 53, 10190-10194.

[47] Lü, K.; Zhou, J.; Zhou, L.; Wang, Q.; Sun, Q.; Jena, P. Sc- phthalocyananine sheet: Promising material for hydrogen storage. Appl. Phys. Lett. 2011, 99, 163104.

[48] Lü, K.; Zhou, J.; Zhou, L.; Chen, X. S.; Chan, S. H.; Sun, Q. Pre-combustion $CO_2$ capture by transition metal ions embedded in phthalocyanine sheets. J. Chem. Phys. 2012, 136, 234703.

[49] Becke, A. D. Density-functional thermochemistry. III. The role of exact exchange. J. Chem. Phys. 1993, 98, 5648-5652.

[50] Krishnan, R.; Binkley, J. S.; Seeger, R.; Pople, J. A. Self- consistent molecular orbital methods. XX. A basis set for correlated wave functions. J. Chem. Phys. 1980, 72, 650-654.

[51] Halgren, T. A. The synchronous-transit method for determining reaction pathways and locating molecular transition states. Chem. Phys. Lett. 1977, 49, 225-232.

[52] Reed, A. E.; Weinstock, R. B.; Weinhold, F. Natural popula- tion analysis. J. Chem. Phys. 1985, 83, 735-746.

[53] Glendening, E. D. R., A. E.; Carpenter, J. E.; Weinhold, F. NBO, Version 3.1.

[54] Klod, S.; Kleinpeter, E. Ab initio calculation of the anisotropy effect of multiple bonds and the ring current effect of arenes-Application in conformational and configurational analysis. J. Chem. Soc., Perkin Trans. 2 2001, 1893-1898.

[55] von Ragué Schleyer, P.; Maerker, C.; Dransfeld, A.; Jiao, H. J.; van Eikema Hommes, N. J. R. Nucleus-independent chemical shifts: A simple and efficient aromaticity probe. J. Am. Chem. Soc. 1996, 118, 6317-6318.

[56] Lu, T.; Chen, F. W. Multiwfn: A multifunctional wavefunction analyzer. J. Comput. Chem. 2012, 33, 580-592.

[57] Humphrey, W.; Dalke, A.; Schulten, K. VMD: Visual molecular dynamics. J. Mol. Graph. 1996, 14, 33-38.

[58] King, B. T. Polycyclic hydrocarbons: Nanographenes do the twist. Nat. Chem. 2013, 5, 730-731.

[59] Ma, J.; Alfè, D.; Michaelides, A.; Wang, E. G. Stone-Wales

defects in graphene and other planar $sp^2$-bonded materials. Phys. Rev. B 2009, 80, 033407.

[60] Piazza, Z. A.; Hu, H.-S.; Li, W.-L.; Zhao, Y.-F.; Li, J.; Wang, L.-S. Planar hexagonal $B_{36}$ as a potential basis for extended single-atom layer boron sheets. Nat. Commun. 2014, 5, 3113.

[61] Tang, H.; Ismail-Beigi, S. Novel precursors for boron nano- tubes: The competition of two-center and three-center bonding in boron sheets. Phys. Rev. Lett. 2007, 99, 115501.

[62] Penev, E. S.; Bhowmick, S.; Sadrzadeh, A.; Yakobson, B. I. Polymorphism of two-dimensional boron. Nano Lett. 2012, 12, 2441-2445.

[63] Bader, R. F. W. A quantum theory of molecular structure and its applications. Chem. Rev. 1991, 91, 893-928.

[64] Henkelman, G.; Arnaldsson, A.; Jónsson, H. A fast and robust algorithm for Bader decomposition of charge density. Comput. Mater. Sci. 2006, 36, 354-360.

[65] Sanville, E.; Kenny, S. D.; Smith, R.; Henkelman, G. Improved grid-based algorithm for Bader charge allocation. J. Comput. Chem. 2007, 28, 899-908.

[66] Becke, A. D.; Edgecombe, K. E. A simple measure of electron localization in atomic and molecular systems. J. Chem. Phys. 1990, 92, 5397-5403.

[67] Savin, A.; Nesper, R.; Wengert, S.; Fässler, T. F. ELF: The electron localization function. Angew. Chem., Int. Ed. 1997, 36, 1808-1832.

[68] Silvi, B.; Savin, A. Classification of chemical bonds based on topological analysis of electron localization functions. Nature 1994, 371, 683-686.

[69] Nørskov, J. K.; Bligaard, T.; Hvolbæk, B.; Abild-Pedersen, F.; Chorkendorff, I.; Christensen, C. H. The nature of the active site in heterogeneous metal catalysis. Chem. Soc. Rev. 2008, 37, 2163-2171.

[70] Janik, M. J.; Taylor, C. D.; Neurock, M. First-principles analysis of the initial electroreduction steps of oxygen over Pt(111). J. Electrochem. Soc. 2009, 156, B126-B135.

[71] Tripković, V.; Skúlason, E.; Siahrostami, S.; Nørskov, J. K.; Rossmeisl, J. The oxygen reduction reaction mechanism on Pt(111) from density functional theory calculations. Electrochim. Acta 2010, 55, 7975-7981.

[72] Keith, J. A.; Jacob, T. Theoretical studies of potential- dependent and competing mechanisms of the electrocatalytic oxygen reduction reaction on Pt(111). Angew. Chem., Int. Ed. 2010, 49, 9521-9525.

[73] Nørskov, J. K.; Bligaard, T.; Logadottir, A.; Bahn, S.; Hansen, L. B.; Bollinger, M.; Bengaard, H.; Hammer, B.; Sljivancanin, Z.; Mavrikakis, M. et al. Universality in heterogeneous catalysis. J. Catal. 2002, 209, 275-278.

[74] Bligaard, T.; Nørskov, J. K.; Dahl, S.; Matthiesen, J.; Christensen, C. H.; Sehested, J. The Brønsted-Evans-Polanyi relation and the volcano curve in heterogeneous catalysis. J. Catal. 2004, 224, 206-217.

[75] Nørskov, J. K.; Rossmeisl, J.; Logadottir, A.; Lindqvist, L.; Kitchin, J. R.; Bligaard, T.; Jónsson, H. Origin of the overpotential for oxygen reduction at a fuel-cell cathode. J. Phys. Chem. B 2004, 108, 17886-17892.

[76] Wu, P.; Du, P.; Zhang, H.; Cai, C. X. Graphyne as a promising metal-free electrocatalyst for oxygen reduction reactions in acidic fuel cells: A DFT study. J. Phys. Chem. C 2012, 116, 20472-20479.

[77] Sha, Y.; Yu, T. H.; Liu, Y.; Merinov, B. V.; Goddard, W. A. Theoretical study of solvent effects on the platinum-catalyzed oxygen reduction reaction. J. Phys. Chem. Lett. 2010, 1, 856-861.

[78] Wei, G.-F.; Fang, Y.-H.; Liu, Z.-P. First principles Tafel kinetics for resolving key parameters in optimizing oxygen electrocatalytic reduction catalyst. J. Phys. Chem. C 2012, 116, 12696-12705.

[79] Gokhale, A. A.; Kandoi, S.; Greeley, J. P.; Mavrikakis, M.; Dumesic, J. A. Molecular-level descriptions of surface chemistry in kinetic models using density functional theory. Chem. Eng. Sci. 2004, 59, 4679-4691.

[80] Greeley, J.; Stephens, I. E. L.; Bondarenko, A. S.; Johansson, T. P.; Hansen, H. A.; Jaramillo, T. F.; Rossmeisl, J.; Chorkendorff, I.; Nørskov, J. K. Alloys of platinum and early transition metals as oxygen reduction electrocatalysts. Nat. Chem. 2009, 1, 552-556.

[81] Hansen, H. A.; Viswanathan, V.; Nørskov, J. K. Unifying kinetic and thermodynamic analysis of $2\ \text{e}^-$ and $4\ \text{e}^-$ reduction of oxygen on metal surfaces. J. Phys. Chem. C 2014, 118, 6706-6718.

![](./images/814614317629440000_11.jpg)