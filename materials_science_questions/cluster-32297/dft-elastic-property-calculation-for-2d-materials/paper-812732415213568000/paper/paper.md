![](./images/812732415213568000_1.jpg)

Subscriber access provided by Stony Brook University | University Libraries

# C: Physical Processes in Nanomaterials and Nanostructures

## Electronic Properties of a New Family of Layered Materials from Groups 14-15: First-Principles Simulations

Muhammad Sufyan Ramzan, Vladimir Ba#i#, Yu Jing, and Agnieszka Kuc

J. Phys. Chem. C, Just Accepted Manuscript • DOI: 10.1021/acs.jpcc.9b07068 • Publication Date (Web): 25 Sep 2019

Downloaded from pubs.acs.org on September 29, 2019

### Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

---

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Electronic Properties of a New Family of Layered Materials from Groups 14-15: First-Principles Simulations

Muhammad Sufyan Ramzan,† Vladimir Bacic, † Yu Jing, ‡,∥ and Agnieszka Kuc*,†,‡,⊥

†Department of Physics and Earth Sciences, Jacobs University Bremen, Campus Ring 1, 28759 Bremen, Germany

‡Wilhelm-Ostwald-Institut für Physikalische und Theoretische Chemie, Universität Leipzig, Linnéstr. 2, 04103 Leipzig, Germany

∥Jiangsu Co-Innovation Centre of Efficient Processing and Utilization of Forest Resources, College of Chemical Engineering, Nanjing Forestry University, Nanjing 210037, China

⊥Helmholtz-Zentrum Dresden-Rossendorf, Forschungsstelle Leipzig, Abteilung Reaktiver Transport, Permoserstr. 15, 04318 Leipzig, Germany

### ABSTRACT

Variety of 2D layered materials has gain tremendous focus of materials scientists, physics, chemistry, and other fields of science. This is due to the fact that thin films of layered materials often exhibit superior (for a given application) properties than the parental bulk materials. Thus, in this work, we studied a new family of layered materials with a general composition of $XY_3$ (where X and Y are elements from Group-14 and 15, respectively). Among the proposed materials, 3D bulk structures of layered $GeP_3$ and $SnP_3$ are stable, metallic, and already synthesized in the 1970s. We calculated cleavage energies of mono- and bilayers to be less than $1\ \text{J}\ \text{m}^{-2}$, what indicates possibility of exfoliation from the bulk materials. Many of the investigated monolayers are mechanically and thermally stable. Electronic structure calculations indicate strong interlayer quantum confinement and consequently a metal-to-semiconductor transition when going from bulk to a mono- or bilayer. These electronic properties promise interesting applications in nanoelectronic devices.

### 1. INTRODUCTION

Ever since the successful exfoliation of graphene,¹ layered two-dimensional (2D) materials have attracted considerable attention of various fields of science and technology, due to their phenomenal electronic, mechanical, and optical properties²⁻⁴ in the monolayer forms. Up to date, layered materials with different electronic properties are available, ranging from semi-metallic graphene⁵⁻⁷ to insulating hexagonal boron nitride⁸⁻¹⁰ with large variety of semiconducting systems, such as monolayer phosphorous, e.g., black phosphorene,¹¹ blue phosphorene,¹² and its

derivatives,¹³⁻¹⁸ transition-metal dichalcogenides (TMDCs) and oxides.¹⁹⁻²¹ Ultrahigh carrier mobility of pristine graphene,²² as high as $10^5$ cm² V⁻¹ s⁻¹, comes with the limitation of the zero band gap. In addition to TMDCs, several derivatives of phosphorene, i.e., GeP₃ ($8.84×10^3$ cm² V⁻¹ s⁻¹),¹⁶ InP₃ ($1.9×10^3$ cm² V⁻¹ s⁻¹),¹⁵ CaP₃ ($\sim$$2×10^4$ cm² V⁻¹ s⁻¹),¹⁷ and SnP₃ ($1.15×10^4$ cm² V⁻¹ s⁻¹),¹⁸ with finite gaps and high carrier mobilities, have been recently reported. 3D layered materials can be exfoliated to mono- or few-layered system and their properties may strongly differ from these of the parental bulks, and even become superior for different applications.²³ For instance, layered TMDCs from Group 6 show a transition from an indirect band gap in the bulk to a direct band gap character in the monolayers.²⁴,²⁵

Recent advancement²⁶,²⁷ in exfoliation techniques²⁸⁻³⁰ and chemical vapour deposition techniques³¹,³² motivated material scientists to search for potentially cleavable layered materials.¹⁶,³³ Our work is inspired by work of Jing et al.,¹⁶ where the authors reported theoretical cleavage energies of GeP₃ monolayers, potentially enabling exfoliation of this material from its bulk form. Bulk GeP₃ material is known from experiments and its crystal structure was reported in 1970.³⁴ It is a metallic system, but predicted by Jing et al.,¹⁶ to become semiconducting when thinned to mono- or bilayers, due to a strong vertical quantum confinement.¹⁶ Another experimental work³⁵ reports on the synthesis of SnP₃, also a Group 14-15 material. Recently, in a theoretical report, Sun et al.,¹⁸ anticipated the metal-to-semiconductor transition for SnP₃, similar to the case of GeP₃, when thinned to monolayers. Moreover, recently predicted potential of GeP₃ for hydrogen evolution reaction (HER),³⁶ gas sensing applications,³⁷ and as an excellent anode material for lithium³⁸ and non-lithium ion batteries³⁹ ensures that stable XP₃ layers will be a vital addition in the 2D material’s zoo. Thus, an obvious question arises weather or not other elements

in these groups can exist with the same stoichiometry $(XY_3$ where X (Group-14) – C, Si, Ge, Sn, Pb and Y (Group-15) – P, As, Sb, Bi) with stable bulk or thin-film forms.

Search for new 2D materials with finite band-gaps for nanoscale (opto)electronic applications is a very active topic. Broad collection of 2D materials can significantly accelerate the advancement in this research area, which is the motivation of our present research. In this work, we investigated the stability and electronic properties of a new class of $XY_3$ layered materials (where X is an element from Group-14 and Y is an element from Group-15) by means of density functional theory simulations. We found that all bulk systems are dynamically stable and exhibit metallic character. Mono- and bilayers have low cleavage energies, however, not all of them are dynamically stable after exfoliation. This may suggest that strong surface reconstruction could occur after exfoliation. All $XP_3$ systems show relatively good thermal and dynamical stability. Stable monolayers are often semiconducting in contrast to the corresponding bulk forms, which might be interesting for nanoelectronics with single-material logical junctions.

## 2. COMPUTATIONAL METHODS

All calculations were carried out using density functional theory (DFT) simulations as implemented in the Vienna *ab-initio* simulation package (VASP).⁴⁰ We used the projector-augmented wave (PAW) method⁴¹ to describe the electron-nucleus interactions, while generalized-gradient approximation proposed by Perdew, Burke, and Ernzerhof (PBE)⁴² was adopted for the exchange and correlation terms, including the dispersion correction D3 approach.⁴³ Plane-wave cut-off of 500 eV was used. A vacuum region of $15\ \mathring{A}$ in the $c$ lattice direction was inserted to avoid spurious interactions between the periodic images in the slab calculations of mono- and bilayers. All structures were relaxed until all the forces acting on each atom were less than $2{\times}10^{-}$

$^{2}$ eV Å⁻¹ and the total energy change between two self-consistent steps was less than $1{\times}10^{-4}$ eV.

Both lattice vectors and atomic positions were fully relaxed. The $\Gamma$-centered $k$-point mesh with 8×8×1 grid was used to sample the Brillouin zone during geometry optimization of bi- (2L) and multilayers (of up to five layers, 5L), while 8×8×8 $k$-mesh for bulk forms in the hexagonal unit cell representation was used (see Figure 1). In order to capture the surface reconstruction that may prevail in the non-planar layered materials,⁴⁴ monolayers (1L) were studied also using larger, rectangular unit cells, for which 8×4×1 $k$-mesh was used. We found that this reconstruction, indeed, takes place for single layer systems, where rectangular unit cells with slight out-of-plane distortions of Y atoms have lower formation energies than in the hexagonal representation with no distortions. This reconstruction also affects the electronic properties, as shown in Figure S1 in the Supplementary Information (SI) for the exemplary case of 1L GeP₃. On the other hand, such a surface reconstruction was not observed for bi- and multilayer systems. Therefore, in this study, we used the rectangular unit cell representation for the monolayers and hexagonal representation for bi- or multilayer systems. Electronic structures were calculated using both PBE functional (for all systems)⁴² and the Heyd-Scuseria-Ernzerhos hybrid functional, HSE06, (for kinetically stable systems).⁴⁵ Finite displacement method, as implemented in the Phonopy,⁴⁶ was used to calculate the phonon dispersion relations, in order to check the dynamical stabilities. These were performed using 2×2×1, 3×3×1 and 3×3×3 $k$-mesh grids for 1L, 2L, and bulk systems, respectively. *Ab-initio* molecular dynamics (AIMD) simulations within the NVT ensemble were performed in order to check the thermal stabilities of the XP₃ monolayers. For AIMD calculations, a 3×3 supercell was used to lift the constraint of the unit cells and 400 K (or 300 K) temperature was held for 10 ps with the time step of 1 fs controlled via Nosé–Hoover thermostat.⁴⁷ For details on the cleavage energy calculations see SI.

![](./images/812732415213568000_2.jpg)

Figure 1 Crystal structures of bulk $XY_3$ systems in the 2×2×2 supercell representation: (a) side and (b) top views. Purple and grey represent $Y$ and $X$ atoms, respectively. (c) Top view of a $XY_3$ monolayer. Figures were created using 3D visualization package VESTA.⁵⁴

## 3. RESULTS AND DISCUSSION

### 3.1 Structural properties of bulk materials

The crystal structures of bulk $XY_3$ (see Figure 1) belong to the $R\overline{3}m$ space group. The calculated lattice parameters of $XP_3$ systems are listed in Table 1 together with the interlayer distances, while selected bond lengths are given in Table S1 (see Tables S2 and S3 in SI for the data on the $XAs_3$ and $XSb_3$ materials). Our relaxed lattice parameters for bulk $GeP_3$ and $SnP_3$ are $a = b = 7.088$ Å, $c = 9.830$ Å and $a = b = 7.422$ Å, $c = 10.550$ Å, respectively, which are in a good agreement with the experimentally obtained bulk systems ($a = b = 7.050$ Å, $c = 9.930$ Å for $GeP_3$ and $a = b = 7.380$ Å, $c = 10.510$ Å for $SnP_3$).³⁴,³⁵ Figures 1(a) and 1(b) show the top and side views of the $XY_3$ crystal bulk structure, where the layers are stacked in the $ABCABC$ order. Figure 1c shows the

corresponding top view of a monolayer. In each layer, atoms are placed in the two adjacent hexagonal planes such that they form a phosphorene-like puckered structure, where each Y atom is bound with two neighbouring Y atoms and one X atom. Each X atom forms three X−Y bonds with three neighbouring Y atoms. The in-plane lattice parameters increase with heavier element, as expected, for all the layered forms, 1L, 2L, and bulk. This is due to the strong variation of the X−Y bond lengths. Except for $CP_3$, also the interlayer distances increase for the heavier elements. The apparent difference in the $CP_3$ structure comes from the fact that C atoms are smaller than P atoms and, thus, the interlayer distance is rather defined by the distance between P atoms in the adjacent layers than between X atoms, as it is in the other XP3 systems.

We have also investigated the charge transfer between X and Y atoms in 1L, 2L, and bulk forms of $XP_3$ and 1L forms of $XAs_3$, as examples. For this, we used Bader atomic charge analysis. The results are given in Tables S4 and S5 in SI. In this particular type of structures, the X atoms donate electrons to P or As, creating an unshared electron pair on these atoms. Considering the number of neighbors in these systems, it is suggested that the X atoms have very unexpected oxidation state of +3. Normally, for the C-group, the oxidation state is preferably +2 or +4. However, as concluded also by Gullman et al.,$^{35}$s the oxidation number 3 appears to be more reasonable when considering the part played by the X atoms in the whole structure.

Table 1. Calculated lattice parameters of $XP_3$ (with $X - C, Si, Ge, Sn, Pb$) mono- (a, b), bilayers (a, b), and bulk (a, b, c) forms. For monolayer (1L), a and b lattice parameters are given for the rectangular unit cell representation, while for bilayer (2L) and bulk, hexagonal unit cells were used. Interlayer distances (d) along the z-axis are given for 2L and bulks.

<table>
<thead>
<tr>
<th>System</th>
<th colspan="3">Lattice vectors (Å)</th>
<th colspan="2">d (Å)</th>
</tr>
<tr>
<th></th>
<th>1L rectangular(a, b)</th>
<th>2L hexagonal(a=b)</th>
<th>Bulk hexagonal(a=b, c)</th>
<th>2L</th>
<th>Bulk</th>
</tr>
</thead>
<tbody>
<tr>
<td>$CP_3$</td>
<td>6.234, 10.806</td>
<td>6.215</td>
<td>6.243, 10.438</td>
<td>2.272</td>
<td>2.201</td>
</tr>
<tr>
<td>$SiP_3$</td>
<td>6.838, 11.841</td>
<td>6.793</td>
<td>6.938, 8.927</td>
<td>1.742</td>
<td>1.697</td>
</tr>
<tr>
<td>$GeP_3$</td>
<td>6.960, 12.055</td>
<td>6.958</td>
<td>7.088, 9.830</td>
<td>1.925</td>
<td>1.886</td>
</tr>
<tr>
<td>$SnP_3$</td>
<td>7.156, 12.387</td>
<td>7.252</td>
<td>7.422, 10.550</td>
<td>1.894</td>
<td>1.886</td>
</tr>
</tbody>
</table>

| PbP₃ | 7.292, 12.613 | 7.418 | 7.685, 10.856 | 1.937 | 1.982 |
|------|---------------|-------|---------------|-------|-------|

For example, the ${\rm GeP_3}$ or ${\rm SnP_3}$ can be described as a layered structure related to the As-type (A7) structure in which the corrugated layers are composed of puckered ${\rm P_6}$ rings. In order to explain such a A7-type structure, every atom has to contribute three electrons to the covalent bonding system. The remaining fourth valence electron of X atom goes to the conduction band. This explains the metallic character of the bulk and multilayer systems. In the monolayers, we do not have a metallic character, at least for the ${\rm XP_3}$ systems, however, additional surface reconstruction occurs in the layers and some of the atomic positions of P atoms are no longer equivalent, thus the bond lengths are not equivalent either. We anticipate that the fourth electron either stay on the X atom (less charge transfer) or is accommodated in some of the bonds between P and X atoms and forms semiconducting monolayers.

These analysis are supported by the Bader charges and the charge transfer between X and Y atoms. Except for C-based systems, the charge is always transferred from the X atoms to the 6-fold rings of Y atoms. We observe for heavier systems that the amount of transferred charge is larger for multilayers and bulk than for single layers.

### 3.2 Cleavage energies of 1L and 2L from bulk

Primarily, exfoliating mono- or few-layers from layered bulk materials is realizable by micromechanical cleavage or liquid exfoliation techniques, if the cleavage energy is equal or less than about $1\ {\rm J\ m^{-2}}$.^28,48^ To assess the possibility of mono- and bilayer exfoliation from multilayer (or bulk) ${\rm XP_3}$, we estimated the cleavage energies (see Figure 2 and SI for calculation details) for both 1L and 2L ${\rm XP_3}$ from a bulk-like 5L-slab model, as shown in the inset of Figure 2. Threshold cleavage energy of the mechanical or liquid exfoliation methods is indicated with a grey dashed line. We found that all 1L and 2L ${\rm XP_3}$ fall below the threshold limit, making them potentially

![](./images/812732415213568000_3.jpg)

Figure 2 Calculated cleavage energies of $XP_3$ ($X - C$, Si, Ge, Sn, Pb) 1L and 2L shown as solid and dashed lines, respectively, as function of the separation distance between 1L or 2L and the remainder of 5L slab. The distance zero refers to the equilibrium distance of bulk-like 5L-slab. Grey dashed line indicates the threshold energy for mechanically cleavable materials. The calculated cleavage energies fall below or about the threshold, suggesting that all systems, except 1L $SiP_3$, should be cleavable from their bulk or multilayer stacks.

cleavable, except for 1L $SiP_3$ (i.e. $1.36\ \text{J m}^{-2}$), however, this material is the only unstable 1L $XP_3$ system (see Section 3.3). For comparison, theoretically estimated exfoliation energies of $MoS_2,^{49}$ graphene, $^{50}$ 1L $SnP_3,^{18}$ 1L $GeP_3,^{16}$ and 1L $InP_3^{15}$ are $0.29\ \text{J m}^{-2}$, $0.32\ \text{J m}^{-2}$, $0.71\ \text{J m}^{-2}$, $1.14\ \text{J m}^{-2}$, and $1.32\ \text{J m}^{-2}$, respectively. The differences between the cleavage energies of 1L (solid lines) and 2L (dashed lines) indicate the material's affinity to be exfoliated either as mono- or bilayers, respectively. For example, 2L $SnP_3$ should be easier to exfoliate than 1L, whereas, for $CP_3$, these energies are very similar, indicating that both forms could be obtained (cf. Figure 2). The corresponding data for $XAs_3$ and $XSb_3$ are shown in Figure S3. In these cases, the cleavage energies for all systems fall below the threshold, however, as it will be discussed in Section 3.3, not all 1L and 2L of $XAs_3$ and $XSb_3$ are dynamically stable.

### 3.3 Phonon dispersion relation

Next, we have investigated the stability of bulk and exfoliated 1L and 2L systems. For this, we have calculated the phonon dispersion relations. All bulk $XY_3$ systems are stable with real frequencies throughout the Brillouin zone, as shown in Figure 3 (refer to Figure S2 for bulk $XAs_3$ and $XSb_3$). The same simulations were performed to check the stability of the exfoliated layers. Figure 4 shows the phonon dispersion relations of 1L and 2L $XP_3$ (refer to Figures S4 and S5 for the other materials). Due to the surface reconstruction in the monolayers, much larger supercells are required to correctly calculate the phonons. Since degree of reconstruction is not the same in each system, the required supercells are, therefore, different. For instance, 6×2×1 supercell is needed to accurately calculate phonons of 1L $CP_3$, while 5×2×1 supercells is sufficient for other $XP_3$ systems. All real phonon branches indicate mechanical stability of all monolayers, except for $SiP_3$, which has imaginary modes in the entire Brillouin zone, as shown in Figure 4(b). This may suggest either instability of such a monolayer or that the material may undergo yet another type of reconstruction (not taken into account in this study).

The results of 2L $XP_3$ systems indicate that all bilayers are fairly stable. Very small imaginary frequencies close to the $\Gamma$ point (e.g., for 2L $CP_3$) stem from too small unit cells used in the finite displacement calculations of phonons and could be removed by extension of the unit cell size. Larger supercells are, however, computationally too demanding and not affordable with our present resources, but our conclusions should be sound.

![](./images/812732415213568000_4.jpg)

Figure 3 Calculated phonon dispersion relations of bulk (a) $CP_3$, (b) $SiP_3$, (c) $GeP_3$, (d) $SnP_3$, and (e) $PbP_3$ using 2×2×2 supercells.

While most of the 1L and 2L systems of $XP_3$ seem to be stable, the corresponding $XAs_3$ and $XSb_3$ are not. Taking into account the unit cell size argument, we can conclude that the only stable materials are 1L $CAs_3$ ($CSb_3$) and $GeAs_3$ ($GeSb_3$), and 2L $CAs_3$ ($CSb_3$) and $SnAs_3$ ($SnSb_3$). All the other systems could be argued that another type of reconstruction is necessary to stabilize them. On the other hand, we have not considered thicker films, e.g., 3L, which might be kinetically stable.

To assess the thermal stability of 1L $XP_3$ systems, we performed molecular dynamics simulations at 300 K and 400 K (see Figures S6-S11). Similar to the results of phonons, all the 1L $XP_3$ are thermally stable at 300 K, while at 400 K, $CP_3$ and $SiP_3$ show some instability, indicating that synthesis of these materials as monolayers, should be implemented at ambient conditions.

![](./images/812732415213568000_5.jpg)

Figure 4 Phonon dispersion relations of monolayer (a) $CP_3$, (b) $SiP_3$, (c) $GeP_3$, (d) $SnP_3$, and (e) $PbP_3$ with $5{\times}2{\times}1$ supercells for all systems, except $1L$ $CP_3$, for which we used $6{\times}2{\times}1$ supercell. (f) - (j) Phonon dispersion relations of bilayer $XP_3$ with $3{\times}3{\times}1$supercells.

### 3.4 Electronic properties

All bulk $XY_3$ ($Y$ – P, As, Sb) systems are metallic, as shown in Figure S12. Our expectation was that in most of the cases, if not all, a metal-to-semiconductor transition will occur, when reducing the number of layers from bulk down to bi- or monolayers. While this expectation proofed correct for $XP_3$ systems, it completely failed for $XSb_3$. For As-based system, only a few materials became semiconducting under such a confinement.

We found that most P-based systems in 1L and 2L forms are semiconductors, while systems with three or more layers are essentially metallic or semi-metallic. Both PBE and HSE06 levels of theory predict the same band-gap character of all semiconducting system, with the former method

underestimating the band gap values by maximum of 0.34 eV for $1L\ GeP_3$ (see Figure 5). In details: Monolayers of $CP_3$ and $SiP_3$ are metallic, while monolayers of $GeP_3$, $SnP_3$, and $PbP_3$ are semiconducting. Interestingly, $2L\ SiP_3$ is semiconducting, while its single layer is metallic. This also indicates that $1L\ SiP_3$ may be unstable in the present configuration and another surface reconstruction might be more favourable. This is in accordance with the phonon dispersion relations for both systems (cf. Figure 4(b) and (g)), in which $2L\ SiP_3$ is stable, while 1L is not. For $CP_3$, both 1L and 2L forms are metallic, while the heaviest $PbP_3$ as 2L has a very small band gap of about 38 meV. All semiconducting systems are indirect band gap materials, with band gaps below 1 eV.

For the heavier elements, such as Ge, Sn or Pb, we have recalculated the band structures of monolayers with spin-orbit coupling (SOC), however, no significant changes in the band structures and band gaps were observed. Negligible SOC in $1L\ XP_3$ may be related to the stoichiometry, where heavier elements account for only 25% of the whole structure. Furthermore, partial density of states (PDOS), as shown in Figure S13, with indicated frontier bands (i.e. valence band maximum, VBM, and conduction band minimum, CBM) are predominantly formed by the P and X atom $2p$-orbitals.

The electronic structures of As- and Sb-based 1L and 2L systems are shown in Figures S14 and S15. The stable $2L\ SnAs_3$ and $SnSb_3$ systems become semiconducting, however, the latter's band gap is only about 50 meV. We expect that for $2L\ GeAs_3$ and $PbAs_3$, the semi-metallic character obtained at the PBE level might in fact become semiconducting (similar to 1L forms), if treated at the HES06 level. These systems are, however, kinetically unstable, what was shown in the phonon dispersion calculations, thus, band structures were not recalculated with the more expensive HSE06 (cf. Figure S4).

![](./images/812732415213568000_6.jpg)

Figure 5 Band structures of (a) – (e) monolayer and (f) – (j) bilayer $CP_3$, $SiP_3$, $GeP_3$, $SnP_3$, and $PbP_3$ respectively, calculated at the PBE (solid black) and HSE06 (dashed green) levels of theory. The horizontal dash lines indicate the Fermi levels, which for practical reasons were shifted to zero. For semiconducting systems, the Fermi levels are additionally shifted to the top of the valence bands.

Applying tensile strain or compression can modulate electronics of 2D layered materials. Here, we show the effect of compressive and tensile strain on the band structures of 1L $SnP_3$ and 1L $PbP_3$, as exemplary materials (see Figure S16). This effect in 1L $GeP_3$ has already been studied and reported earlier.¹⁶ The $SnP_3$ monolayer stays an indirect gap semiconductor for both tensile (+5%) and compressive (−5%) strains, with the direct gap at $\Gamma$ point just 4 meV and 30 meV larger than the indirect gap, respectively. For the case of 1L PbP3, the direct gap at $\Gamma$ point is larger than the indirect one by only 2 meV and 3 meV for the tensile and compressive strains, respectively. Moreover, opposite to effects observed in transition-metal dichalcogenides, e.g., $MoS_2$,⁵¹ the band

gap increases with increasing strain and decreases under compression. The same phenomenon was observed for $1\text{L GeP}_3.^{16}$

Thickness dependent electronic properties of the proposed materials could make it possible to fabricate devices on a single material. For example, field effect transistors with metallic electrode made of few-layer materials and the semiconductor channel of a monolayer of the same material, as proposed earlier for other layered systems. $^{52,53}$ This new family of Group 14-15 materials shows potential for such applications. Furthermore, unique crystal structure of few layers $\text{XY}_3$ anticipates a potential application in gas sensing and hydrogen evolution reactions, as reported already for $\text{GeP}_3.^{36,37}$

## CONCLUSION

In conclusion, we report on a new class of layered materials, $\text{XY}_3$ (X – Group-14, Y – Group-15 element), where metallic bulks turn to semiconducting 1L and 2L systems, indicating a strong vertical quantum confinement effects. Small cleavage energies of 1L and 2L forms, less than $1\ \text{J m}^{-2}$, suggest the possibility of exfoliation from the corresponding bulk or multilayer phases. All bulk materials and most of the proposed 1L and 2L structures are kinetically and thermally stable. Monolayers, however, undergo surface reconstruction, which has to be taken into account with care, when optimizing their geometries. Surface reconstruction also affects the electronics of 1L forms. Surfaces of bi- and multi-layers are not a subject to such a reconstruction. Many 1L and 2L system become semiconducting, with band gaps below $1\ \text{eV}$, while all the bulk systems are metallic. Moreover, the band gaps of 1L and 2L materials could be tuned by tensile strain or compression, because they increase while the material is strained and decrease when it is compressed. If the film thickness of these materials could be experimentally controlled, this new

family of 2D materials would be available to fabricate unique devices, e.g., transistors built from a single material, which would strongly reduce the power losses at the electrode-channel junctions.

## ASSOCIATED CONTENT

The Supplementary Information is available and contains following information:

Structural, energetic, vibrational, and electronic properties of $XAs_3$ and $XSb_3$ materials; additional details on methods and simulations; molecular dynamics simulations of 1L $XP_3$ systems; exemplary simulations of strain influence on electronic properties.

## AUTHOR INFORMATION

Corresponding Authors: *(A.K) a.kuc@hzdr.de

## ACKNOWLEDGEMENTS

Financial support by the Deutsche Forschungsgemeinschaft (GRK 2247/1 (QM3)) and the high-performance computing resources of ZIH Dresden are gratefully acknowledged. The authors thank Prof. Thomas Heine for his insightful comments and fruitful discussions.

### Notes

There are no conflicts to declare.

## REFERENCES

(1) Novoselov, K. S.; Geim, A. K.; Morozov, S. V.; Jiang, D.; Zhang, Y.; Dubonos, S. V.; Grigorieva, I. V.; Firsov, A. A. Electric Field In Atomically Thin Carbon Films. *Science* (80-. ). **2004**, *306*, 666–669.

(2) Wang, Q. H.; Kalantar-Zadeh, K.; Kis, A.; Coleman, J. N.; Strano, M. S. Electronics And Optoelectronics Of Two-Dimensional Transition Metal Dichalcogenides. *Nat. Nanotechnol.* **2012**, 7, 699–712.

(3) Qian, X.; Liu, J.; Fu, L.; Li, J. Quantum Spin Hall Effect In Two-Dimensional Transition Metal Dichalcogenides. *Science* (80-. ). **2014**, 346, 1344–1347.

(4) Singh, A. K.; Mathew, K.; Zhuang, H. L.; Hennig, R. G. Computational Screening Of 2D Materials For Photocatalysis. *J. Phys. Chem. Lett.* **2015**, 6, 1087–1098.

(5) Castro Neto, A. H.; Guinea, F.; Peres, N. M. R.; Novoselov, K. S.; Geim, A. K. The Electronic Properties Of Graphene. *Rev. Mod. Phys.* **2009**, 81, 109–162.

(6) Allen, M. J.; Tung, V. C.; Kaner, R. B. Honeycomb Carbon: A Review Of Graphene. *Chem. Rev.* **2010**, 110, 132–145.

(7) Avouris, P. Graphene: Electronic And Photonic Properties And Devices. *Nano Lett.* **2010**, 10, 4285–4294.

(8) Nag, A.; Raidongia, K.; Hembram, K. P. S. S.; Datta, R.; Waghmare, U. V.; Rao, C. N. R. Graphene Analogues Of BN: Novel Synthesis And Properties. *ACS Nano* **2010**, 4, 1539–1544.

(9) Jin, C.; Lin, F.; Suenaga, K.; Iijima, S. Fabrication Of A Freestanding Boron Nitride Single Layer And Its Defect Assignments. *Phys. Rev. Lett.* **2009**, 102, 195505.

(10) Warner, J. H.; Rümmeli, M. H.; Bachmatiuk, A.; Büchner, B. Atomic Resolution Imaging And Topography Of Boron Nitride Sheets Produced By Chemical Exfoliation. *ACS Nano* **2010**, 4, 1299–1304.

(11) Qiao, J.; Kong, X.; Hu, Z.-X.; Yang, F.; Ji, W. High-Mobility Transport Anisotropy And

Linear Dichroism In Few-Layer Black Phosphorus. *Nat. Commun.* 2014, 5, 4475–4482.

(12) Zhu, Z.; Tománek, D. Semiconducting Layered Blue Phosphorus: A Computational Study. *Phys. Rev. Lett.* 2014, 112, 176802–176805.

(13) Schusteritsch, G.; Uhrin, M.; Pickard, C. J. Single-Layered Hittorf’s Phosphorus: A Wide-Bandgap High Mobility 2D Material. *Nano Lett.* 2016, 16, 2975–2980.

(14) Guan, J.; Liu, D.; Zhu, Z.; Tománek, D. Two-Dimensional Phosphorus Carbide: Competition Between Sp 2 And Sp 3 Bonding. *Nano Lett.* 2016, 16, 3247–3252.

(15) Miao, N.; Xu, B.; Bristowe, N. C.; Zhou, J.; Sun, Z. Tunable Magnetism And Extraordinary Sunlight Absorbance In Indium Triphosphide Monolayer. *J. Am. Chem. Soc.* 2017, 139, 11125–11131.

(16) Jing, Y.; Ma, Y.; Li, Y.; Heine, T. GeP3: A Small Indirect Band Gap 2D Crystal With High Carrier Mobility And Strong Interlayer Quantum Confinement. *Nano Lett.* 2017, 17, 1833–1838.

(17) Lu, N.; Zhuo, Z.; Guo, H.; Wu, P.; Fa, W.; Wu, X.; Zeng, X. C. CaP 3 : A New Two-Dimensional Functional Material With Desirable Band Gap And Ultrahigh Carrier Mobility. *J. Phys. Chem. Lett.* 2018, 9, 1728–1733.

(18) Sun, S.; Meng, F.; Wang, H.; Wang, H.; Ni, Y. Novel Two-Dimensional Semiconductor SnP 3 : High Stability, Tunable Bandgaps And High Carrier Mobility Explored Using First-Principles Calculations. *J. Mater. Chem. A* 2018, 6, 11890–11897.

(19) Nicolosi, V.; Chhowalla, M.; Kanatzidis, M. G.; Strano, M. S.; Coleman, J. N. Liquid Exfoliation Of Layered Materials. *Science* (80-. ). 2013, 340, 1226419–1226419.

(20) Kuc, A.; Heine, T. The Electronic Structure Calculations Of Two-Dimensional Transition-

Metal Dichalcogenides In The Presence Of External Electric And Magnetic Fields. *Chem. Soc. Rev.* 2015, 44, 2603–2614.

(21) Heine, T. Transition Metal Chalcogenides: Ultrathin Inorganic Materials With Tunable Electronic Properties. *Acc. Chem. Res.* 2015, 48, 65–72.

(22) Novoselov, K. S.; Geim, A. K.; Morozov, S. V.; Jiang, D.; Katsnelson, M. I.; Grigorieva, I. V.; Dubonos, S. V.; Firsov, A. A. Two-Dimensional Gas Of Massless Dirac Fermions In Graphene. *Nature* 2005, 438, 197–200.

(23) Gillen, R.; Maultzsch, J. Light-Matter Interactions In Two-Dimensional Transition Metal Dichalcogenides: Dominant Excitonic Transitions In Mono- And Few-Layer $MoX_2$ And Band Nesting. *IEEE J. Sel. Top. Quantum Electron.* 2017, 23, 219–230.

(24) Mak, K. F.; Lee, C.; Hone, J.; Shan, J.; Heinz, T. F. Atomically Thin MoS2 : A New Direct-Gap Semiconductor. *Phys. Rev. Lett.* 2010, 105, 136805.

(25) Splendiani, A.; Sun, L.; Zhang, Y.; Li, T.; Kim, J.; Chim, C. Y.; Galli, G.; Wang, F. Emerging Photoluminescence In Monolayer MoS2. *Nano Lett.* 2010, 10, 1271–1275.

(26) Sun, J.; Li, X.; Guo, W.; Zhao, M.; Fan, X.; Dong, Y.; Xu, C.; Deng, J.; Fu, Y. Synthesis Methods Of Two-Dimensional MoS2: A Brief Review. *Crystals* 2017, 7, 198–209.

(27) Paton, K. R.; Varrla, E.; Backes, C.; Smith, R. J.; Khan, U.; O’Neill, A.; Boland, C.; Lotya, M.; Istrate, O. M.; King, P.; et al. Scalable Production Of Large Quantities Of Defect-Free Few-Layer Graphene By Shear Exfoliation In Liquids. *Nat. Mater.* 2014, 13, 624–630.

(28) Coleman, J. N.; Lotya, M.; O’Neill, A.; Bergin, S. D.; King, P. J.; Khan, U.; Young, K.; Gaucher, A.; De, S.; Smith, R. J.; et al. Two-Dimensional Nanosheets Produced By Liquid Exfoliation Of Layered Materials. *Science* (80-. ). 2011, 331, 568–571.

(29) Zhou, K.-G.; Mao, N.-N.; Wang, H.-X.; Peng, Y.; Zhang, H.-L. A Mixed-Solvent Strategy For Efficient Exfoliation Of Inorganic Graphene Analogues. *Angew. Chemie Int. Ed.* 2011, 50, 10839–10842.

(30) Li, L. H.; Chen, Y.; Behan, G.; Zhang, H.; Petravic, M.; Glushenkov, A. M. Large-Scale Mechanical Peeling Of Boron Nitride Nanosheets By Low-Energy Ball Milling. *J. Mater. Chem.* 2011, 21, 11862–11866.

(31) Ling, X.; Lee, Y. H.; Lin, Y.; Fang, W.; Yu, L.; Dresselhaus, M. S.; Kong, J. Role Of The Seeding Promoter In MoS2 Growth By Chemical Vapor Deposition. *Nano Lett.* 2014, 14, 464–472.

(32) Lee, Y.-H.; Zhang, X.-Q.; Zhang, W.; Chang, M.-T.; Lin, C.-T.; Chang, K.-D.; Yu, Y.-C.; Wang, J. T.-W.; Chang, C.-S.; Li, L.-J.; et al. Synthesis Of Large-Area MoS 2 Atomic Layers With Chemical Vapor Deposition. *Adv. Mater.* 2012, 24, 2320–2325.

(33) Ma, Y.; Kuc, A.; Heine, T. Single-Layer Tl2O: A Metal-Shrouded 2D Semiconductor With High Electronic Mobility. *J. Am. Chem. Soc.* 2017, 139, 11694–11697.

(34) Donohue, P. C.; Young, H. S. Synthesis, Structure, And Superconductivity Of New High Pressure Phases In The Systems GeP And GeAs. *J. Solid State Chem.* 1970, 1, 143–149.

(35) Gullman, J.; Olofsson, O. The Crystal Structure Of SnP3 And A Note On The Crystal Structure Of GeP3. *J. Solid State Chem.* 1972, 5, 441–445.

(36) Wu, H.-H.; Huang, H.; Zhong, J.; Yu, S.; Zhang, Q.; Zeng, X. C. Monolayer Triphosphates MP3 (M=Sn, Ge) With Excellent Basal Catalytic Activity For Hydrogen Evolution Reaction. *Nanoscale* 2019, 11, 12210–12219.

(37) Niu, F.; Cai, M.; Pang, J.; Li, X.; Zhang, G.; Yang, D. A First-Principles Study: Adsorption

Of Small Gas Molecules On GeP 3 Monolayer. *Surf. Sci.* **2019**, *684*, 37–43.

(38) Zhang, C.; Jiao, Y.; He, T.; Ma, F.; Kou, L.; Liao, T.; Bottle, S.; Du, A. Two-Dimensional GeP3 As A High Capacity Electrode Material For Li-Ion Batteries. *Phys. Chem. Chem. Phys.* **2017**, *19*, 25886–25890.

(39) Deng, X.; Chen, X.; Huang, Y.; Xiao, B.; Du, H. Two-Dimensional GeP 3 As A High Capacity Anode Material For Non-Lithium-Ion Batteries. *J. Phys. Chem. C* **2019**, *123*, 4721–4728.

(40) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes For Ab Initio Total-Energy Calculations Using A Plane-Wave Basis Set. *Phys. Rev. B* **1996**, *54*, 11169–11186.

(41) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials To The Projector Augmented-Wave Method. *Phys. Rev. B* **1999**, *59*, 1758–1775.

(42) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865–3868.

(43) Barbiellini, B.; Bansil, A. Dyson Orbitals, Quasi-Particle Effects And Compton Scattering. *J. Phys. Chem. Solids* **2004**, *65*, 2031–2034.

(44) Cahangirov, S.; Topsakal, M.; Aktürk, E.; Şahin, H.; Ciraci, S. Two- And One-Dimensional Honeycomb Structures Of Silicon And Germanium. *Phys. Rev. Lett.* **2009**, *102*, 236804.

(45) Krukau, A. V.; Vydrov, O. A.; Izmaylov, A. F.; Scuseria, G. E. Influence Of The Exchange Screening Parameter On The Performance Of Screened Hybrid Functionals. *J. Chem. Phys.* **2006**, *125*, 224106.

(46) First Principles Phonon Calculations In Materials Science. *Scr. Mater.* **2015**, *108*, 1–5.

(47) Martyna, G. J.; Klein, M. L.; Tuckerman, M. Nosé–Hoover Chains: The Canonical Ensemble Via Continuous Dynamics. *J. Chem. Phys.* 1992, 97, 2635–2643.

(48) Lee, C.; Yan, H.; Brus, L. E.; Heinz, T. F.; Hone, J.; Ryu, S. Anomalous Lattice Vibrations Of Single- And Few-Layer $\ce{MoS_{2}}$. *ACS Nano* 2010, 4, 2695–2700.

(49) Björkman, T.; Gulans, A.; Krasheninnikov, A. V.; Nieminen, R. M. Van Der Waals Bonding In Layered Compounds From Advanced Density-Functional First-Principles Calculations. *Phys. Rev. Lett.* 2012, 108, 235502–235505.

(50) Ziambaras, E.; Kleis, J.; Schröder, E.; Hyldgaard, P. Potassium Intercalation In Graphite: A Van Der Waals Density-Functional Study. *Phys. Rev. B* 2007, 76, 155425.

(51) Ghorbani-Asl, M.; Borini, S.; Kuc, A.; Heine, T. Strain-Dependent Modulation Of Conductivity In Single-Layer Transition-Metal Dichalcogenides. *Phys. Rev. B* 2013, 87, 235434–235436.

(52) Ghorbani-Asl, M.; Kuc, A.; Miró, P.; Heine, T. A Single-Material Logical Junction Based On 2D Crystal PdS2. *Adv. Mater.* 2016, 28, 853–856.

(53) Yamaguchi, H.; Blancon, J.-C.; Kappera, R.; Lei, S.; Najmaei, S.; Mangum, B. D.; Gupta, G.; Ajayan, P. M.; Lou, J.; Chhowalla, M.; et al. Spatially Resolved Photoexcited Charge-Carrier Dynamics In Phase-Engineered Monolayer $\ce{MoS_{2}}$. *ACS Nano* 2015, 9, 840–849.

(54) Momma, K.; Izumi, F. VESTA 3 For Three-Dimensional Visualization Of Crystal, Volumetric And Morphology Data. *J. Appl. Crystallogr.* 2011, 44, 1272–1276.

![](./images/812732415213568000_7.jpg)

![](./images/812732415213568000_8.jpg)

TOC graphics: New $XY_3$ family of layered materials.