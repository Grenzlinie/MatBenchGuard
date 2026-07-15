Article

# Silicon Framework-based Lithium Silicides at High Pressures
Shoutao Zhang, Yanchao Wang, Guochun Yang, and Yanming Ma

ACS Appl. Mater. Interfaces, Just Accepted Manuscript • DOI: 10.1021/acsami.6b04308 • Publication Date (Web): 15 Jun 2016
Downloaded from http://pubs.acs.org on June 19, 2016

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/814511469700841472_1.jpg)

ACS Applied Materials & Interfaces is published by the American Chemical Society.
1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Silicon Framework-based Lithium Silicides at High Pressures

Shoutao Zhang¹, Yanchao Wang¹, Guochun Yang¹,²,* and Yanming Ma¹,*

¹State Key Laboratory of Superhard Materials, Jilin University, Changchun 130012, China
²Centre for Advanced Optoelectronic Functional Materials Research and Key Laboratory for UV Light-Emitting Materials and Technology of Ministry of Education, Northeast Normal University, Changchun 130024, China

**Abstract:** The bandgap and optical properties of diamond silicon (Si) are not suitable for many advanced applications such as thin-film photovoltaic devices and light-emitting diodes. Thus, finding new Si allotropes with better bandgap and optical properties is desirable. Recently, a Si allotrope with a desirable bandgap of ~1.3 eV was obtained by leaching Na from NaSi₆ that was synthesized under high pressure [*Nat. Mater.* 2015, 14, 169], paving the way to finding new Si allotropes. Li is isoelectronic with Na, with a smaller atomic core and comparable electronegativity. It is unknown whether Li silicides share similar properties, but it is of considerable interest. Here, a swarm intelligence-based structural prediction is used in combination with first-principles calculations to investigate the chemical reactions between Si and Li at high pressures, where seven new compositions (LiSi₄, LiSi₃, LiSi₂, Li₂Si₃, Li₂Si, Li₃Si, and Li₄Si) become stable above 8.4 GPa. The Si-Si bonding patterns in these compounds evolve with increasing Li content sequentially from frameworks to layers, linear chains, and eventually isolated Si ions. Nearest-neighbor Si atoms, in *Cmmm*-structured LiSi₄, form covalent open channels hosting one-dimensional Li atom chains, which have similar structural features to NaSi₆. The analysis of integrated crystal orbital Hamilton populations reveals that the Si-Si interactions are mainly responsible for the structural stability. Moreover, this structure is dynamically stable even at ambient pressure. Our results are also important for understanding the structures and electronic properties of Li-Si binary compounds at high pressures.

**Keywords:** Lithium silicide, Silicon allotrope, Structural prediction, Electronic property, High pressure

## 1. Introduction
Si is the basis of the semiconductor device industry because it can be doped with other elements, and it is abundant, cheap, and has a native oxide passivation layer. $^{1-3}$ Diamond Si ($cF8$) is the most stable form of Si under ambient conditions. However, its larger direct bandgap of ~3.2 eV is not suitable for many advanced applications such as light-emitting diodes, $^{4}$ higher-performance transistors, $^{5}$ and thin-film photovoltaic devices (~1.3 eV). $^{6}$ Therefore, much research has focused on finding new Si allotropes with suitable bandgaps and optical properties. For example, rhombohedral Si (Si-XII, R8) has a small indirect gap of 0.24 eV, $^{7}$ hexagonal Si (h-Si6) has a direct band gap of 0.61 eV, $^{8}$ and face-centered cubic Si (Si-III, BC8) is semi-metallic. $^{9}$ Moreover, theoretical calculations have proposed some Si allotropes possess with quasi-direct bandgaps, exhibiting improved visible light absorption characteristics. $^{3,6,10}$

Another route for synthesizing Si allotropes with advanced optical and electronic properties is to start from Si-rich compounds. $^{11}$ For example, a $NaSi_6$ precursor was synthesized under high pressure, $^{12}$ and then Na was removed from the precursor by a thermal 'degassing' process. Finally, a new orthorhombic Si allotrope, $Si_{24}$, with a quasi-direct bandgap of ~1.3 eV was obtained, which has many potential applications in photovoltaic devices. $^{11}$ A Si clathrate ($Si_{136}$) with a bandgap of $1.9\ eV^{13}$ was obtained by leaching Na from a $Na_xSi_{136}$ precursor. $^{14}$ This approach was also used to synthesize a Ge allotrope. $^{15}$ These findings mainly result from the effect of pressure on stabilities of Si clathrates. $^{16}$ Inspired by these results, we focus on finding Si framework-based Li silicides under high pressure. Li has the smallest radius of the alkali metals, which may allow Li to be leached from the Si framework, forming new Si allotropes.

Recently, Si has attracted attention as an anode material in Li-ion batteries because its specific energy is about 10 times larger than that of graphitic anodes. $^{17-20}$ To understand the discharge process and improve the performance of Li-ion batteries, extensive studies have been done on Li-Si binary compounds including LiSi, $Li_{12}Si_7$,

$Li_7Si_3$, $Li_{13}Si_4$, and $Li_{21}Si_5$. $^{21-24}$ LiSi was synthesized at pressures of 1-2.5 GPa and temperatures of 773-973 K, and was recovered at ambient pressure. $^{25}$ In addition, the Li-Si phase diagram over a wide range of compositions has been extensively investigated at ambient pressure. $^{26-30}$ Several stable or metastable Li-Si compositions have been predicted. Tipton et al. predicted a new $R$-3m phase of $Li_5Si_2$ by using a genetic algorithm. $^{26}$ Irais et al. used the minima hopping method to identify two new stable phases (e.g., $Li_3Si$ and $Li_4Si$) and six metastable phases (e.g. $Li_3Si_2$, $Li_2Si$, $Li_9Si_4, Li_7Si_2, Li_5Si$, and $Li_6Si$). $^{30}$ Although the high-pressure phase transitions of LiSi have been studied, $^{27}$ the relative stabilities, structural characters, and electronic properties of Li-Si binary compounds with wide compositions under high pressures have not been explored.

In this work, the high-pressure phase diagram of the Li-Si system was explored by the swarm intelligence-based structural prediction (CALYPSO) method. $^{31,32}$ Compared with stable compositions at ambient pressure, unexpected Si-rich compositions ($LiSi_4$ and $LiSi_3$) are stable above 25 GPa. These metallic compounds exhibit intriguing structural properties such as Si covalent tunnels containing one-dimensional Li atom chains and a layered structure with alternating hexagonal and triangular Si rings. The $Cmmm$-structured $LiSi_4$ is dynamically stable under ambient pressure, which means that it might be recoverable. The Si-Si bonding patterns in these Li silicides can be tuned by varying the Li composition.

## 2. Computational Details

We performed a crystal structure prediction for the Li-Si system via global minimization of free energy surfaces as implemented in the CALYPSO code, $^{31,32}$ which has been validated with various known compounds, from elemental to binary and ternary compounds. $^{33-36}$ The ab initio structural relaxations and electronic property calculations were performed within the framework of density functional theory as implemented in the Vienna ab initio simulation package code. $^{37}$ The Perdew-Burke-Ernzerhof generalized gradient approximation $^{38}$ was used as the exchange-correlation functional. The electron-ion interaction was described by using

the all-electron projector augmented-wave method (PAW)³⁹ with $1s^22s^1$ and $3s^23p^2$ treated as the valences for Li and Si atoms, respectively. A plane-wave kinetic energy cutoff of 600 eV and appropriate Monkhorst-Pack $k$-meshes with grid spacing of $2\pi \times$ 0.025 Å⁻¹ were chosen to ensure that total energy calculations were well converged. The validity of the PAW pseudopotentials at high pressures was verified with the full-potential linearized augmented plane-wave method by using the WIEN2k code (Figure S1).⁴⁰ Phonon calculations were performed to determine the dynamical stability of the predicted structures by using the finite displacement approach as implemented in the Phonopy code.⁴¹ Bader's quantum theory of atoms in molecules analysis was used for the charge transfer calculations.⁴²

## 3. Results and Discussion

### 3.1 Phase stabilities of Li-Si compounds

We focused on our structure search among Si-rich compounds that are the potential precursors for obtaining new Si allotropes. The variable-composition structure searches were performed at a variety of $\text{Li}_x\text{Si}_y$ compositions ($x = 1$–4, $y = 1$–6) with up to four formula units (f.u.) per simulation cell at 25, 50, and 100 GPa. Figure 1a shows the convex hull for the Li-Si system at different pressures, constructed by calculating the average atom formation enthalpy of the compositions, $\Delta H_f = [H(\text{Li}_x\text{Si}_y) - xH(\text{Li}) - yH(\text{Si})]/(x + y)$. In general, structures sitting on the convex hull are stable to decomposition into elemental solids or other binary compounds, and thus are expected to be experimentally synthesizable, whereas structures above the convex hull are metastable. The known phase of solid LiSi ($I4_1/a$, 16 f.u. per cell) was reproduced readily in our structure searches at ambient pressure. Our calculated lattice parameters for LiSi ($I4_1/a$, 16 f.u. per cell) were $a = b = 9.343$ Å and $c = 5.734$ Å, in good agreement with the experimental values of $a = b = 9.353$ Å and $c = 5.743$ Å. To test the reliability of our approach further, we reconstructed the convex hull at 0 GPa including other experimental and theoretical structures.³⁰ As shown in Figure S2, our calculations reproduced the previous results well.²⁶,³⁰

Figure 1a shows that a series of thermodynamically stable Li-Si compounds emerged on the convex hull at 25 GPa, including $LiSi_4$, $LiSi_3$, $LiSi_2$, $Li_2Si_3$, $LiSi$, $Li_2Si$, $Li_3Si$, and $Li_4Si$. Notably, most of the Si-rich compositions became stable at 25 GPa, whereas at ambient pressure there were no stable Si-rich compounds (Figure S2). At 50 GPa, $LiSi_2$ and $Li_2Si_3$ became metastable, whereas the other stable compositions at 25 GPa were still on the convex hull. The stable compositions at 100 GPa were the same as those at 50 GPa. In total, we found four new Si-rich compounds and three new Li-rich compounds. The stable pressure ranges of the corresponding structures were calculated (Figure 1b). Stable Li-Si compounds underwent a series of structural phase transitions in the considered pressure range.

![](./images/814511469700841472_2.jpg)

Figure 1. Chemical stabilities of the Li-Si compounds. (a) Calculated enthalpy of formation per atom of the Li-Si system with respect to decomposition into elemental Li and Si solid phases. The energetically stable phases at each pressure are shown by solid symbols, which are connected by the convex hull (solid lines). Dotted lines that directly connect data points are visual guides. The $Fm$-$3m$, $I$-$43d$, and $Cmca$-$24$ structures of elemental Li solids were used to calculate the formation enthalpies.$^{35,43}$ Elemental Si solids with $P6/mmm$, $P6_3/mmc$, and $Fm$-$3m$ symmetries were used.$^{44,45}$
(b) Pressure-composition phase diagram of stable Li-Si binary compounds.

### 3.2 Structures and dynamical stabilities of Li-Si compounds

LiSi₄ was predicted to be stable above 25 GPa in an orthorhombic structure (space group *Cmmm*, 2 f.u. per cell, Figure 2a), consisting of Si-sharing 12-fold LiSi₁₂ octahedrons. This phase had an unusual structural feature of alternating connections of quartet and hexagonal Si rings that formed tunnels, intercalating Li atoms along the *c*-axis. The Li atoms formed one-dimensional chains with equal Li-Li distances of 2.385 Å, which has been observed in Li₃Cs⁴⁶ and Li₅H⁴⁷ compounds. The Si-Si distances varied from 2.331 to 2.417 Å at 25 GPa, which was similar to the distances in Na₈Si₄₆ (2.333–2.413 Å),¹² and shorter than those in BaSi₆ (2.400–2.469 Å).⁴⁸ These Si-Si distances produced strong interatomic interactions, playing a key role in stabilizing the structure. The Li-Si distances were 2.641 and 2.684 Å, which were slightly larger than that of 2.627 Å in LiSi (*I4₁/a* structure) at 0 GPa. The Si atoms in this structure were not *sp³* hybridization, as observed in most Si allotropes,¹¹ in which the Si-Si-Si angles vary widely between 119.5° and 180.0°. Under compression, the *Cmmm* structure transformed into a tetragonal structure with *I4/m* symmetry (2 f.u. per cell, Figure 2b) at 34.5 GPa. There were twelve Si atoms surrounding each Li atom, forming a Si-Li tetradecahedron. The faces and vertexes of these tetradecahedrons were shared, forming a three-dimensional Si network. Consequently, the Li-Li distances lengthened greatly to 3.455 Å. The Si atoms formed tetrahedral bonds with Si-Si-Si angles between 58.80° and 120.37°, and Si-Si distances between 2.394 and 2.462 Å at 50 GPa, which were larger than those in *Cmmm*-structured LiSi₄ at 25 GPa. The Li-Si distances of 2.404 to 2.419 Å were much shorter than those in *I4₁/a*-structured LiSi at 0 GPa and *Cmmm*-structured LiSi₄ at 25 GPa.

LiSi₃ stabilized into a hexagonal structure at above 8.6 GPa (space group, *P6/mmm*, 1 f.u. per cell, Figure 2c) consisting of face- and vertex-sharing Li-Si octahedrons along the *c*-axis and *ab*-plane, respectively. There, Si atoms formed a layered structure of alternating hexagonal and triangular Si rings with an equivalent Si-Si distance of 2.391 Å. To the best of our knowledge, this is the first observation of this layered structure in Si systems. Li atoms formed one-dimensional chains along the *c*-axis with equal Li-Li distances of 2.423 Å. The *P6/mmm* phase transformed into

the tetragonal $P4/mmm$ phase (3 f.u. per cell, Figure 2d) at 32.4 GPa, consisting of face-sharing Si-Li tetradecahedrons. The square Si rings were interconnected to form a layer in the $ab$-plane with a Si-Si distance of 2.413 Å. The two kinds of Li-Si distances were 2.413 and 2.473 Å, respectively. Under further compression, $LiSi_3$ stabilized into an $Al_3Ti$-type structure (space group $I4/mmm$, 2 f.u. per cell, Figure 2e). The face-sharing Si tetradecahedrons in this structure enclosed a Li atom at their centers and formed a Si polymeric framework containing tunnels along the $a$-axis.

$LiSi_2$ became stable in the pressure range of 8.4-33.5 GPa adopting a structure with $P2/m$ symmetry, in which three inequivalent Si atoms (at the $1b$, $1f$, and $2n$ sites) and Li atoms (at the $2m$ sites) formed interpenetrating polymeric networks (2 f.u. per cell, Figure 2f). Each Li atom was eight-fold coordinated by Si. Our calculations predicted that $Li_2Si_3$ adopts a monoclinic $P2/m$ phase in the pressure range of 8.6-35.3 GPa (2 f.u. per cell, Figure 2g). Each Li atom was surrounded by 8 Si atoms in an irregularly shaped polyhedron $Si_8$. These polyhedrons were connected by sharing vertexes to form tunnels containing Li atoms along the $b$-axis.

LiSi was the only stoichiometry that was stable over the whole pressure range considered. The known phase of LiSi with $I4_1/a$ symmetry (16 f.u. per cell, Figure 2h) transformed into an AuCu-type structure with $P4/mmm$ symmetry at above 3.3 GPa (1 f.u. per cell, Figure 2i). This was a first-order transition, and it was accompanied by an increase in the coordination number of Li from 4 to 8. A CsCl-type structure became the most stable above 90 GPa (1 f.u. per cell, Figure 2j).

The stoichiometry of $Li_2Si$ was not stable at ambient pressure and stabilized into a $MgB_2$-type structure$^{49}$ (space group, $P6/mmm$, 1 f.u. per cell, Figure 2k) above 8.4 GPa, containing face-sharing Si-Li octahedrons. Consequently, the Li atoms formed a graphene-like layered structure in the $ab$-plane, whereas Si atoms formed one-dimensional chains along the $c$-axis with equal Si-Si distances of 2.378 Å. A graphene-like Li layered structure has also been observed in $Li_2Au.^{50}$ Under further compression, the $P6/mmm$ structure of $Li_2Si$ transformd into a $MoSi_2$-type structure (space group $I4/mmm$, 2 f.u. per cell, Figure 2l) at 93.8 GPa. The basic building block

of this structure was the Si-Li dodecahedron. The Li atoms formed bilayered structures consisting of triangular $Li_3$ rings and square $Li_4$ rings.

The stoichiometry of $Li_3Si$ stabilized into a $BiF_3$-type structure (space group, $Fm$-$3m$, 4 f.u. per cell, Figure 2m) above 8.4 GPa. The basic building blocks in this structure were square Li cages with alternating Li/Si atoms at the center. Above 48.4 GPa, the $Fm$-$3m$ phase transformed into an orthorhombic structure (space group $Fmmm$, 8 f.u. per cell, Figure 2n), consisting of face-sharing Li-Si octadecahedrons.

Our predictions showed that the Li-richest stoichiometry, $Li_4Si$, had three thermodynamically stable phases. The hexagonal $R$-$3m$ phase (3 f.u. per cell, Figure 2o) became stable above 8.4 GPa, consisting of Li-sharing 8-fold $SiLi_8$ hexahedrons. Above 40.5 GPa, the $R$-$3m$ phase transformed into a tetragonal structure (space group $I4/m$, 2 f.u. per cell, Figure 2p), which has also been observed in $Li_4C.^{51}$ This was a first-order phase transition with an increase in the coordination number of Si from 8 to 12. Upon compression, the $I4/m$ phase transformed to the orthorhombic phase (space group $Fddd$, 8 f.u. per cell, Figure 2q) at 48.5 GPa, consisting of face-sharing 16-fold $SiLi_{16}$ icosahedrons. The Li atoms in these structures formed a three-dimensional network, which has also been observed in Li-rich compounds ($Li_6B,^{52}$ $Li_4Cs,^{46}$ and $Li_8H^{47}$).

![](./images/814511469700841472_3.jpg)

Figure 2. Crystal structures of Li-Si compounds in their stable regions. (a) Low-pressure $Cmmm$ structure of $LiSi_4$. (b) High-pressure $I4/m$ structure of $LiSi_4$. (c) Low-pressure $P6/mmm$ structure of $LiSi_3$. (d) $P4/mmm$ structure of $LiSi_3$. (e) High-pressure $I4/mmm$ structure of $LiSi_3$. (f) $P2/m$ structure of $LiSi_2$. (g) $P2/m$ structure of $Li_2Si_3$. (h) Ambient-pressure $I4_1/a$ structure of $LiSi$. (i) Low-pressure $P4/mmm$ structure of $LiSi$. (j) High-pressure $Pm-3m$ structure of $LiSi$. (k) Low-pressure $P6/mmm$ structure of $Li_2Si$. (l) High-pressure $I4/mmm$ structure of $Li_2Si$. (m) Low-pressure $Fm-3m$ structure of $Li_3Si$. (n) High-pressure $Fmmm$ structure of

$Li_3Si$. (o) Low-pressure $R$-3$m$ structure of $Li_4Si$. (p) $I4/m$ structure of $Li_4Si$. (q) High-pressure $Fddd$ structure of $Li_4Si$. Detailed structural parameters of stable Li-Si compounds are shown in Table S1. In all the structures, the large green and small yellow balls represent Li and Si atoms, respectively.

To assess the dynamical stability of the Li-Si compounds, the quasi-harmonic mode was used to calculate their phonon spectra with the supercell method. There were no imaginary modes for these predicted structures in their stability pressure ranges (Figures 3a and S3-10). For $Cmmm$-structured $LiSi_4$, the motion of the Si ions nearly covered all the frequency regimes, which may result from the three-dimensional network formed by the nearest-neighbor Si atoms, whereas the motion of Li cations mainly contributed to the high frequency regimes (Figure 3b). This phase had no imaginary phonon modes in the Brillouin zone at ambient pressure (Figure 3c), which means that it might be recoverable under ambient conditions.

![](./images/814511469700841472_4.jpg)

Figure 3. Phonon dispersion curves and partial phonon density of states (PHDOS) of LiSi₄ in the *Cmmm* structure at 25 (a and b) and 0 (c and d) GPa. The Li and Si PHDOS are shown as red and blue lines, respectively.

### 3.3 Electronic structures and chemical bonds
To obtain deeper insight into the electronic structures and chemical bonding of these predicted Li-Si compounds, we calculated their band structures and projected density of states (PDOS). We found that all the stable phases of LiSi₄, LiSi₃, LiSi₂, Li₂Si₃, LiSi, Li₂Si, Li₃Si, and Li₄Si are metallic (Figures S11-18). Figure 4a shows that in *Cmmm*-structured LiSi₄ there was strong hybridization of Si 3s and 3p, whereas the coupling between Li and Si was weak.⁵³ There was an overlap between Li 2s and 2p, originating from the linear Li atom chains, as shown in the structural analysis. The PDOS near the Fermi energy mainly came from the contributions of Si 3s and 3p, which were responsible for its metallicity. To confirm this, we constructed a hypothetical model of Li₀Si₄, in which all Li atoms were removed from LiSi₄ with *Cmmm* symmetry at 25 GPa. The calculated PDOS showed that Li₀Si₄ still possessed metallicity (Figure 4c), which remained even at ambient pressure (Figure 4d). LiSi₂ with the *P2/m* symmetry exhibited similar electronic properties (Figure 4e). In the Li-richest composition, *R-3m*-structured Li₄Si, there was a large overlap between Si 3p and Li 2s or 2p, indicating that a charge transfer could occur from Li 2s or 2p to Si 3p. Based on the Bader charge analysis, each Si atom gained 3.077 electrons from Li atoms. However, the hybridization of Si 3s and 3p weakened (Figure 4f). This was in sharp contrast to the *Cmmm*-structured LiSi₄.

Based on this analysis, there may be a big difference in interatomic interactions between Si-rich and Li-rich compounds. Subsequently, we examine these interactions by calculating their integrated crystal orbital Hamilton populations (ICOHPs) as implemented in the LOBSTER package.⁵⁴ The calculated ICOHP values can be used to scale with the bond strength in compounds by counting the energy-weighted population of wavefunctions between two atomic orbitals. In the *Cmmm*-structured LiSi₄, the ICOHP values between Si-Si and Li-Si pairs were 1.684 and 1.242 eV per

pair, respectively, indicating that the Si-Si interaction strength was much larger than that of Li-Si. The major contributions to the Si-Si interaction came from 3p–3p, 3p–3s, and 3s–3s, corresponding to the decomposed ICOHP of 1.244, 0.495, and 0.055 eV per pair, respectively. In the $R$-$3m$-structured $\text{Li}_4\text{Si}$, the ICOHP value between Li-Si pairs was 4.366 eV per pair, which was much larger than in $Cmmm$-structured $\text{LiSi}_4$. Therefore, Li-Si interactions in the Li-rich composition were mainly responsible for the structural stability, whereas it was Si-Si interactions in Si-rich compositions.

![](./images/814511469700841472_5.jpg)

Figure 4. Electronic structures and chemical bonding of Li-Si compounds. (a) PDOS calculated by using the Perdew–Burke–Ernzerhof functional for $\text{LiSi}_4$ in the $Cmmm$ structure. The vertical solid line indicates the Fermi energy level. (b) Calculated ELF

for $LiSi_4$ in the $(\begin{array}{lll}0 & 0 & 1 / 2\end{array})$ plane in the $C m m m$ structure. (c) PDOS for $Li_{0} Si_{4}$ in the Cmmm structure at 25 GPa. (d) PDOS for $Li_{0} Si_{4}$ in the Cmmm structure at 0 GPa. (e) PDOS for $LiSi_{2}$ in the $P 2 / m$ structure. (f) PDOS for $Li_{4} Si$ in the $R-3 m$ structure.

Electron localization function (ELF) maps the likelihood of finding an electron in the neighborhood space of a crystal. $^{55}$ In general, large ELF values (>0.5) correspond to covalent bonds and lone pair or inner shell electrons, whereas smaller ELF values correspond to ionic and metallic bonds. Figures 4b and S19 show that the ELF values between the nearest neighboring Si atoms in $C m m m$ -structured $LiSi_{4}$ were large(approximately 0.85 ), indicating a covalent bonding character, $^{33}$ and that the nearest Si atoms in this structure formed a covalent framework. Between the Li and Si atoms, there were large areas with small ELF values, which is typical of ionic or metallic bonds. $^{56}$

## 4. Conclusions
To find new Si-rich compounds, we have explored the crystal structures and phase stabilities of the Li-Si system under high pressure by using an unbiased structure prediction method in conjunction with density functional total energy calculations. At ambient pressure, Si-rich compositions were unstable and Li-rich compositions were stable, whereas above $25 GPa, Si$ -rich compositions of $LiSi_{4}$ and $LiSi_{3}$ were stable and metallic. In the $C m m m$ -structured $LiSi_{4}$ , the $Si$ atoms formed covalent open channels with alternating hexagonal and square Si rings hosting linear Li chains along the $c$-axis, similar to the Na chains observed in $NaSi_{6}$ . The Si atoms in the open channel formed strong covalent bonds. $LiSi_{4}$ was dynamically stable at $0-25 GPa$ , which means that it might be recoverable to ambient pressure. Our work provides the basis for future experimental investigations of the Li-Si system.

## Associated Content
Supporting Information: Main structural parameters, Birch-Murnaghan equation of states, electron energy band structures, phonon dispersion curves, and projected density of states.

## Author Information
Corresponding Authors: yanggc468@nenu.edu.cn; mym@calypso.cn

## Notes
The authors declare no competing financial interest.

## Acknowledgements
This work is supported by the China 973 Program (2011CB808200); the Natural Science Foundation of China under Nos. 21573037, 51202084, 11474125, 11534003, and 11274136; the 2012 Changjiang Scholars Program of China; Changjiang Scholar and Innovative Research Team in University (IRT1132); The Natural Science Foundation of Jilin Province (20150101042JC); The Postdoctoral Science Foundation of China under grant 2013M541283; Parts of the calculations were performed in the High Performance Computing Center of Jilin University.

## References
(1) Jelle, B. P.; Breivik, C.; Røkenes, H. D. Building Integrated Photovoltaic Products: A State-of-the-Art Review and Future Research Opportunities. *Sol. Energy Mater. Sol. Cells* **2012**, 100, 69–96.

(2) Huang, B.; Deng, H. X.; Lee, H.; Yoon, M.; Sumpter, B. G.; Liu, F.; Smith, S. C.; Wei, S. H. Exceptional Optoelectronic Properties of Hydrogenated Bilayer Silicene. *Phys. Rev. X* **2014**, 4, 021029.

(3) Xiang, H. J.; Huang, B.; Kan, E.; Wei, S. H.; Gong, X. G. Towards Direct-Gap Silicon Phases by the Inverse Band Structure Design Approach. *Phys. Rev. Lett.* **2013**, 110, 118702.

(4) Ng, W. L.; Lourenço, M. A.; Gwilliam, R. M.; Ledain, S.; Shao, G.; Homewood, K. P. An Efficient Room-Temperature Silicon-Based Light-Emitting Diode. *Nature* **2001**, 410, 192–194.

(5) Theis, T. N.; Solomon, P. M. It’s Time to Reinvent the Transistor. *Science* **2010**, 327, 1600–1601.

(6) Botti, S.; Flores-Livas, J. A.; Amsler, M.; Goedecker, S.; Marques, M. A. L.

Low-Energy Silicon Allotropes with Strong Absorption in the Visible for Photovoltaic Applications. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2012**, 86, 121204.

(7) Malone, B. D.; Sau, J. D.; Cohen, M. L. Ab Initio Survey of the Electronic Structure of Tetrahedrally Bonded Phases of Silicon. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2008**, 78, 035210.

(8) Guo, Y.; Wang, Q.; Kawazoe, Y.; Jena, P. A New Silicon Phase with Direct Band Gap and Novel Optoelectronic Properties. *Sci. Rep.* **2015**, 5, 14342.

(9) Besson, J. M.; Mokhtari, E. H.; Gonzalez, J.; Weill, G. Electrical Properties of Semimetallic Silicon III and Semiconductive Silicon IV at Ambient Pressure. *Phys. Rev. Lett.* **1987**, 59, 473–476.

(10) Amsler, M.; Botti, S.; Marques, M. A. L.; Lenosky, T. J.; Goedecker, S. Low-Density Silicon Allotropes for Photovoltaic Applications. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2015**, 92, 014101.

(11) Kim, D. Y.; Stefanoski, S.; Kurakevych, O. O.; Strobel, T. A. Synthesis of an Open-Framework Allotrope of Silicon. *Nat. Mater.* **2015**, 14, 169–173.

(12) Kurakevych, O. O.; Strobel, T. A.; Kim, D. Y.; Muramatsu, T.; Struzhkin, V. V. Na-Si Clathrates Are High-Pressure Phases: A Melt-Based Route to Control Stoichiometry and Properties. *Cryst. Growth Des.* **2013**, 13, 303–307.

(13) Dong, J.; Sankey, O.; Kern, G. Theoretical Study of the Vibrational Modes and Their Pressure Dependence in the Pure Clathrate-II Silicon Framework. *Phys. Rev. B* **1999**, 60, 950.

(14) Gryko, J.; McMillan, P. F.; Marzke, R. F.; Ramachandran, G. K.; Patton, D.; Deb, S. K.; Sankey, O. F. Low-Density Framework Form of Crystalline Silicon with a Wide Optical Band Gap. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2000**, 62, R7707(R).

(15) Guloy, A. M.; Ramlau, R.; Tang, Z.; Schnelle, W.; Baitinger, M.; Grin, Y. A Guest-Free Germanium Clathrate. *Nature* **2006**, 443, 320–323.

(16) Kume, T.; Koda, T.; Sasaki, S.; Shimizu, H.; Tse, J. S. High-Pressure Raman Study of the Potassium-Doped Silicon Clathrate K8Si46. *Phys. Rev. B:*

Condens. Matter Mater. Phys. 2004, 70, 052101.

(17) Kasavajjula, U.; Wang, C.; Appleby, A. J. Nano- and Bulk-Silicon-Based Insertion Anodes for Lithium-Ion Secondary Cells. J. Power Sources 2007, 163, 1003–1039.

(18) Yao, Y.; Liu, N.; McDowell, M. T.; Pasta, M.; Cui, Y. Improving the Cycling Stability of Silicon Nanowire Anodes with Conducting Polymer Coatings. Energy Environ. Sci. 2012, 5, 7927–7930.

(19) Wu, H.; Chan, G.; Choi, J. W.; Ryu, I.; Yao, Y.; McDowell, M. T.; Lee, S. W.; Jackson, A.; Yang, Y.; Hu, L.; Cui, Y. Stable Cycling of Double-Walled Silicon Nanotube Battery Anodes Through Solid–Electrolyte Interphase Control. Nat. Nanotechnol. 2012, 7, 310–315.

(20) Ogata, K.; Salager, E.; Kerr, C. J.; Fraser, A. E.; Ducati, C.; Morris, A. J.; Hofmann, S.; Grey, C. P. Revealing Lithium-Silicide Phase Transformations in Nano-Structured Silicon-Based Lithium Ion Batteries via in Situ NMR Spectroscopy. Nat. Commun. 2014, 5, 3217.

(21) Chan, M. K. Y.; Wolverton, C.; Greeley, J. P. First Principles Simulations of the Electrochemical Lithiation and Delithiation of Faceted Crystalline Silicon. J. Am. Chem. Soc. 2012, 134, 14362–14374.

(22) Kuhn, A.; Sreeraj, P.; Pottgen, R.; Wiemhofer, H.-D.; Wilkening, M.; Heitjans, P. Li Ion Diffusion in the Anode Material Li12Si7: Ultrafast Quasi-1D Diffusion and Two Distinct Fast 3D Jump Processes Separately Revealed by 7Li NMR Relaxometry. J. Am. Chem. Soc. 2011, 133, 11018–11021.

(23) Liu, X. H.; Zhang, L. Q.; Zhong, L.; Liu, Y.; Zheng, H.; Wang, J. W.; Cho, J. H.; Dayeh, S. A.; Picraux, S. T.; Sullivan, J. P.; Mao, S. X.; Ye, Z. Z.; Huang, J. Y. Ultrafast Electrochemical Lithiation of Individual Si Nanowire Anodes. Nano Lett. 2011, 11, 2251–2258.

(24) Lee, S. W.; McDowell, M. T.; Berla, L. A.; Nix, W. D.; Cui, Y.; Woo, S.; McDowell, M. T.; Berla, L. A.; Nix, W. D.; Cui, Y. Fracture of Crystalline Silicon Nanopillars During Electrochemical Lithium Insertion. Proc. Natl. Acad. Sci. U. S. A. 2012, 109, 4080–4085.

(25) Braga, M. H.; Debski, A.; Gasior, W. Li-Si Phase Diagram: Enthalpy of Mixing, Thermodynamic Stability, and Coherent Assessment. *J. Alloys Compd.* 2014, 616, 581-593.

(26) Tipton, W. W.; Bealing, C. R.; Mathew, K.; Hennig, R. G. Structures, Phase Stabilities, and Electrical Potentials of Li-Si Battery Anode Materials. *Phys. Rev. B: Condens. Matter Mater. Phys.* 2013, 87, 184114.

(27) Morris, A. J.; Grey, C. P.; Pickard, C. J. Thermodynamically Stable Lithium Silicides and Germanides from Density Functional Theory Calculations. *Phys. Rev. B: Condens. Matter Mater. Phys.* 2014, 90, 054111.

(28) Zeilinger, M.; Kurylyshyn, I. M.; Häussermann, U.; Fässler, T. F. Revision of the Li-Si Phase Diagram: Discovery and Single-Crystal X-Ray Structure Determination of the High-Temperature Phase Li4.11Si. *Chem. Mater.* 2013, 25, 4623-4632.

(29) Okamoto, H. Li-Si (Lithium-Silicon). *J. Phase Equilib. Diffus.* 2009, 30, 118-119.

(30) Valencia-Jaime, I.; Sarmiento-Perez, R.; Botti, S.; Marques, M. A. L.; Amsler, M.; Goedecker, S.; Romero, A. H. Novel Crystal Structures for Lithium-Silicon Alloy Predicted by Minima Hopping Method. *J. Alloys Compd.* 2016, 655, 147-154.

(31) Wang, Y.; Lv, J.; Zhu, L.; Ma, Y. Crystal Structure Prediction via Particle-Swarm Optimization. *Phys. Rev. B: Condens. Matter Mater. Phys.* 2010, 82, 094116.

(32) Wang, Y.; Lv, J.; Zhu, L.; Ma, Y. CALYPSO: A Method for Crystal Structure Prediction. *Comput. Phys. Commun.* 2012, 183, 2063-2070.

(33) Zhu, L.; Liu, H.; Pickard, C. J.; Zou, G.; Ma, Y. Reactions of Xenon with Iron and Nickel Are Predicted in the Earth's Inner Core. *Nat. Chem.* 2014, 6, 644-648.

(34) Miao, M. Caesium in High Oxidation States and as a P-Block Element. *Nat. Chem.* 2013, 5, 846-852.

(35) Lv, J.; Wang, Y.; Zhu, L.; Ma, Y. Predicted Novel High-Pressure Phases of

Lithium. *Phys. Rev. Lett.* **2011**, *106*, 015503.

(36) Yang, G.; Wang, Y.; Ma, Y. A Stable, Magnetic, and Metallic Li3O4 Compound as a Discharge Product in a Li-Air Battery. *J. Phys. Chem. Lett.* **2014**, *5*, 2516–2521.

(37) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using A Plane-Wave Basis Set. *Phys. Rev. B* **1996**, *54*, 11169–11186.

(38) Perdew, J.; Chevary, J.; Vosko, S.; Jackson, K.; Pederson, M.; Singh, D.; Fiolhais, C. Atoms, Molecules, Solids, and Surfaces: Applications of the Generalized Gradient Approximation for Exchange and Correlation. *Phys. Rev. B* **1993**, *48*, 4978.

(39) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* **1994**, *50*, 17953.

(40) Blaha, P.; Schwarz, K.; Sorantin, P.; Trickey, S. B. Full-Potential, Linearized Augmented Plane Wave Programs for Crystalline Systems. *Comput. Phys. Commun.* **1990**, *59*, 399–415.

(41) Togo, A.; Oba, F.; Tanaka, I. First-Principles Calculations of the Ferroelastic Transition between Rutile-Type and CaCl2-Type SiO2 at High Pressures. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2008**, *78*, 134106.

(42) Bader, R. F. W. Atoms in Molecules. *Acc. Chem. Res.* **1985**, *18*, 9–15.

(43) Degtyareva, V. F. Potassium under Pressure: Electronic Origin of Complex Structures. *Solid State Sci.* **2014**, *36*, 62–72.

(44) Duclos, S.; Vohra, Y. K.; Ruoa, A. L. Hcp-to-Fcc Transition in Silicon at 78 GPa and Studies to 100 GPa. *Phys. Rev. Lett.* **1987**, *58*, 775–777.

(45) Olijnyk, H.; Sikka, S. K.; Holzapfel, W. B. Structural Phase Transitions in Si and Ge under Pressures up to 50 GPa. *Phys. Lett. A* **1984**, *103*, 137–140.

(46) Botana, J.; Miao, M.-S. Pressure-Stabilized Lithium Caesides with Caesium Anions beyond the -1 State. *Nat. Comm.* **2014**, *5*, 4861.

(47) Hooper, J.; Zurek, E. Lithium Subhydrides under Pressure and Their Superatom-like Building Blocks. *ChemPlusChem* **2012**, *77*, 969–972.

(48) Yamanaka, S.; Maekawa, S. Structural Evolution of the Binary System Ba-Si under High-Pressure and High-Temperature Conditions. *Zeitschrift für Naturforschung B* **2006**, *61*, 1493–1499.

(49) Nagamatsu, J.; Nakagawa, N.; Muranaka, T.; Zenitani, Y.; Akimitsu, J. Superconductivity at 39 K in Magnesium Diboride. *Nature* **2001**, *410*, 63–64.

(50) Yang, G.; Wang, Y.; Peng, F.; Bergara, A.; Ma, Y. Gold as a 6p-Element in Dense Lithium Aurides. *J. Am. Chem. Soc.* **2016**, *138*, 4046–4052.

(51) Lin, Y.; Strobel, T. A.; Cohen, R. E. Structural Diversity in Lithium Carbides. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2015**, *92*, 214106.

(52) Peng, F.; Miao, M.; Wang, H.; Li, Q.; Ma, Y. Predicted Lithium-Boron Compounds under High Pressure. *J. Am. Chem. Soc.* **2012**, *134*, 18599–18605.

(53) Wan, W.; Zhang, Q.; Cui, Y.; Wang, E. First Principles Study of Lithium Insertion in Bulk Silicon. *J. Phys.: Condens. Matter* **2010**, *22*, 415501.

(54) Dronskowski, R.; Blochl, P. E. Crystal Orbital Hamilton Populations (COHP): Energy-Resolved Visualization of Chemical Bonding in Solids Based on Density-Functional Calculations. *J. Phys. Chem.* **1993**, *97*, 8617–8624.

(55) Becke, A. D.; Edgecombe, K. E. A Simple Measure of Electron Localization in Atomic and Molecular Systems. *J. Chem. Phys.* **1990**, *92*, 5397–5403.

(56) Gennari, C.; Salom, B.; Potenza, D.; Williams, A. Synthesis of Sulfonamido-Pseudopeptides: New Chiral Unnatural Oligomers. *Angew. Chem., Int. Ed. Engl.* **1994**, *33*, 2067–2069.

Table of Content (TOC) Image

![](./images/814511469700841472_6.jpg)

Crystal structure (left panel) and 2D ELF contour plot in the $(0\ 0\ 1/2)$ plane (right panel) of ${\text{LiSi}}_4$ with $Cmmm$ symmetry at 25 GPa