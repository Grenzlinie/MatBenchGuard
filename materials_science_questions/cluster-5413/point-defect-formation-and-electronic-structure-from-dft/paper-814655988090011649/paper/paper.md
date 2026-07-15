![](./images/814655988090011649_1.jpg)

# Hydrogen isotope in erbium oxide: Adsorption, penetration, diffusion, and vacancy trapping

Wei Mao $^{a,d,*}$, Takumi Chikada $^{b}$, Akihiro Suzuki $^{c}$, Takayuki Terai $^{a}$, Hiroyuki Matsuzaki $^{d}$

$^{a}$ Department of Nuclear Engineering and Management, School of Engineering, The University of Tokyo, 2-11-16 Yayoi, Bunkyo-ku, Tokyo 113-8656, Japan
$^{b}$ Department of Chemistry, Graduate School of Science, Shizuoka University, 836 Ohya, Suruga-ku, Shizuoka 422-8529, Japan
$^{c}$ Nuclear Professional School, School of Engineering, The University of Tokyo, 2-22, Shirakata-shirane, Tokai, Naka 319-1188, Ibaraki, Japan
$^{d}$ The University Museum, The University of Tokyo, 2-11-16 Yayoi, Bunkyo-ku, Tokyo 113-0032, Japan

## HIGHLIGHTS

- H adsorption on cubic $\text{Er}_2\text{O}_3$ surface results in electron transfer from H to the surface.
- The H penetration energy of at least 1.6 eV is required for cubic $\text{Er}_2\text{O}_3$ surface.
- The dominated mechanisms of H diffusion in bulk $\text{Er}_2\text{O}_3$ are elucidated.
- H diffusion near or at vacancies in $\text{Er}_2\text{O}_3$ is an exothermic reaction.

---

## ARTICLE INFO

**Article history:**
Received 10 July 2014
Received in revised form 6 January 2015
Accepted 6 January 2015
Available online 7 February 2015

**Keywords:**
Erbium oxide
Permeation process
Tritium
Density functional theory calculations

---

## ABSTRACT

In this study, we report results using first-principles density functional theory calculations for four critical aspects of the interaction: H adsorption on $\text{Er}_2\text{O}_3$ surface, surface-to-subsurface penetration of H into $\text{Er}_2\text{O}_3$, bulk diffusion of H in $\text{Er}_2\text{O}_3$, and trapping of H at vacancies. We identify surface stable adsorption positions and find that H prefers to transfer electrons to the surfaces and form covalent bonds with the nearest neighboring four oxygen atoms. For low surface coverage of H as in our case ($0.89 \times 10^{14}\ \text{H/cm}^2$), a penetration energy of at least 1.60 eV is required for cubic $\text{Er}_2\text{O}_3$ surfaces. Further, the H diffusion barrier between the planes defined by $\text{Er}_2\text{O}_3$ units along the favorable $\langle 1\ 1\ 1 \rangle$ direction is found to be very small – 0.16 eV – whereas higher barriers of 0.41 eV and 1.64 eV are required for diffusion across the planes, somewhat higher than the diffusion energy barrier of 0.20 eV observed experimentally at 873 K. In addition, we predict that interstitial H is exothermically trapped when it approaches a vacancy with the vacancy defect behaving as an electron trap since the H-vacancy defect is found to be more stable than the intrinsic defect.

© 2015 Elsevier B.V. All rights reserved.

---

## 1. Introduction

One of the key components of the D–T fuelling cycle in fusion blanket systems is tritium recovery. Tritium permeation barrier (TPB) plays an important role in the recovery by containing and handling deuterium and tritium within the reactor building and by controlling hydrogen isotope release to the environment without incurring exorbitant costs [1,2]. Erbium oxide ($\text{Er}_2\text{O}_3$) has attracted much attention as TPB material owing to its high permeation reduction factor (PRF) as well as high stability under strong reducing atmosphere [3,4]. The $\text{Er}_2\text{O}_3$ coating has been investigated as insulator for liquid lithium blanket system. In addition, $\text{Er}_2\text{O}_3$ has one of the lowest Gibbs free energy of formation among all binary oxide ceramics [5,6]. As a result, $\text{Er}_2\text{O}_3$ has been selected as one of the candidate materials for TPB coatings.

TPB coatings suppressing H isotope permeation explain the importance of interaction between atomic hydrogen and erbium oxide [7]. Hence, a thorough examination of the interaction requires to be performed both experimentally and theoretically. In the interaction, it is necessary to understand the thermodynamics and kinetics of hydrogen adsorption on $\text{Er}_2\text{O}_3$ surfaces and the subsequent behavior of hydrogen in bulk $\text{Er}_2\text{O}_3$, including its penetration, diffusion, and trapping. As reported in Refs. [8,9], density functional theory (DFT) calculations have become a valuable tool to elucidate the structures and determine the dynamics of interstitial H in metals, alloys, and ceramics. DFT

---

* Corresponding author at: Department of Nuclear Engineering and Management, School of Engineering, The University of Tokyo, 2-11-16 Yayoi, Bunkyo-ku, Tokyo 113-8656, Japan. Tel.: +81 03 5841 7420.
E-mail address: mao@nuclear.jp (W. Mao.).

http://dx.doi.org/10.1016/j.fusengdes.2015.01.002
0920-3796/© 2015 Elsevier B.V. All rights reserved.

has been used to successfully predict the microscopic behavior of H in oxides such as $\mathrm{Cr}_{2} \mathrm{O}_{3}, \mathrm{TiO}_{2}, \mathrm{SiO}_{2}$, and $\mathrm{Al}_{2} \mathrm{O}_{3}$ [10-13]. Therefore, it is essential to apply DFT calculations to investigate the interaction between atomic hydrogen and $\mathrm{Er}_{2} \mathrm{O}_{3}$.

Interest in the adsorption of hydrogen atoms on $\mathrm{Er}_{2} \mathrm{O}_{3}$ surfaces stems mainly from its relevance in TPB coatings. Cubic $\mathrm{Er}_{2} \mathrm{O}_{3}(001)$ surface was studied based on the experimental result that the (001) surface is the most stable after long-time hydrogen isotope (deuterium) permeation [7,14], when compared to other surfaces such as (111) and (110). Because of this, we have placed emphasis on the cubic $\mathrm{Er}_{2} \mathrm{O}_{3}(001)$ surface itself and then discussed $\mathrm{H}$ adsorption and penetration on and through this surface, respectively, via DFT calculations. Subsequently, we analyze $\mathrm{H}$ diffusion in bulk $\mathrm{Er}_{2} \mathrm{O}_{3}$ and $\mathrm{H}$ trapping at vacancies. We provide computational details in Section 2 and then present and discuss our results in Section 3. Finally, we summarize our work in Section 4.

## 2. Computational details

The computational simulations in this study were performed using spin-polarized DFT calculations as implemented in the Vienna Ab Initio Simulation Package (VASP), and the Generalized Gradient Approximation (GGA) of Perdew and Wang 91 (PW91) [15] for electron exchange and correlation. PW91 contains much of the underlying physics of exchange and correction interactions of local density approximation (LDA). Although Perdew, Burke, and Ernzerhof (PBE) is based on PW91 and contains the correct features of LDA, some important features of PW91 are sacrificed. These include (1) correct second-order gradient coefficients for the exchange energy $\left(E_{x}\right)$ and the correlation energy $\left(E_{C}\right)$ in the slowly non-adiabatic limit, and (2) correct non-uniform scaling of $E_{x}$ under the limiting condition where the reduced gradient $(s)$ tends to infinity $(\infty)[16,17]$. Hence, PW91 is used rather than PBE in the DFT calculations. The kinetic energy cutoff for the planewave basis set is set to $500.0 \mathrm{eV}$ for all DFT calculations: increasing the cutoff resulted in variations in the total energy of $<2 \mathrm{meV} /$ atom $(0.192 \mathrm{~kJ} / \mathrm{mol} /$ atom). The surface and the adsorbate systems have been simulated using a slab model, which includes 12-16 relaxed and unrelaxed atomic layers and a vacuum region $(>1.0 \mathrm{~nm})$. Periodic boundary conditions have been used, with the one electron pseudo-orbitals expanded over a plane wave basis set. The expansion includes all plane waves whose kinetic energy is less than a predetermined cutoff energy $E_{\text {cut }}$, i.e., $h^{-2} k^{2} / 2 m<E_{\text {cut }}$, where $h$ is Planck's constant, $k$ is the wave vector and $m$ is the electronic mass. The $k$ points were obtained from the Monkhorst-Pack scheme [18].

The sampling of the Brillouin zone was performed using $k$-points of $4 \times 4 \times 1$ for a $(1 \times 1)$ surface unit cell, which includes 24 $\mathrm{Er}$ and $36 \mathrm{O}$ atoms. For the bulk $\mathrm{Er}_{2} \mathrm{O}_{3}$ consisting of $32 \mathrm{Er}$ and 48 $\mathrm{O}$ atoms, we used a mesh size of $4 \times 4 \times 4$ for $k$-point sampling. The $k$-points above have been tested to converge to $<1 \mathrm{meV} /$ atom $(0.096 \mathrm{~kJ} / \mathrm{mol} /$ atom). Atomic relaxations were performed using a conjugate gradient alogirithm [19] with the force on each atom converged to less than $1 \mathrm{meV} / \mathrm{nm}(0.096 \mathrm{~kJ} / \mathrm{mol} / \mathrm{nm})$. During the optimization, both the adsorbate $(\mathrm{H})$ and the $\mathrm{Er}$ and $\mathrm{O}$ atoms in the top four atomic layers of the slab are allowed to relax while the remaining $\mathrm{Er}$ and $\mathrm{O}$ atoms of the slab are frozen at bulk optimized configurations, as indicated in Fig. 3(b). The relaxations in the inner atoms are rather small $(<0.1 \%)$ even if all the atoms are fully relaxed. Further, the number of atomic layers in the slab as well as the vacuum depth needed were carefully tested, i.e., increasing the number of atomic layers from 12 to 16 while keeping the top four relaxed and the other inner layers frozen, alters the energy of $\mathrm{H}$ adsorption by $<0.05 \mathrm{eV}$. In addition, dipole corrections originally introduced by Neugebauer and Scheffler [20] have been included in order to correct the errors introduced by the use of periodic boundary conditions. Thus, the adsorption energy $\left(E_{\text {ads }}\right)$ of the adsorbate $\mathrm{H}$ with the dipole correction can be calculated as

$$
\left(E_{\mathrm{ads}}\right)_{d}=E(\mathrm{~S})_{\mathrm{H} \rightarrow d}-E(\mathrm{~S})-0.5 E\left(\mathrm{H}_{2}\right) \tag{1}
$$

where $E(\mathrm{~S})_{\mathrm{H} \rightarrow d}$ refers to the energy of the system when the $\mathrm{H}$ atom is distance $d$ apart from the $\mathrm{Er}_{2} \mathrm{O}_{3}$ surface, $E(\mathrm{~S})$ is the energy of the $\mathrm{Er}_{2} \mathrm{O}_{3}$ surface, and $0.5 E\left(\mathrm{H}_{2}\right)$ is the energy of atomic hydrogen as half of the molecular hydrogen energy. $(1 \times 1)$ and $(1 \times 2)$ surface cells were tested using the three-dimensional slab models for $\mathrm{H}$ adsorption. Enlarging the size doesn't result in the change of $\mathrm{H}$ adsorption energy. $\mathrm{H}$ diffusion on the surface and from the surface to the solute site in the bulk has been calculated using the nudged elastic band (NEB) method [21] as implemented in DFT calculations. Twelve images were used in the NEB calculation.

To gain a further understanding of the interaction between the $\mathrm{H}$ atom and the cubic $\mathrm{Er}_{2} \mathrm{O}_{3}(001)$ surface, we have presented the difference of charge density plot calculated using the following equation:

$$
\Delta \rho=\rho_{(\mathrm{H} / \mathrm{S})}-\left(\rho_{(\mathrm{S})}^{\text {frozen }}+\rho_{(\mathrm{H})}^{\text {frozen }}\right) \tag{2}
$$

where is the electron density for the adsorbate- $\mathrm{Er}_{2} \mathrm{O}_{3}$ system in its minimum-energy configuration, is the electron density of the cubic $\mathrm{Er}_{2} \mathrm{O}_{3}(001)$ surface that is kept frozen in the positions of the $\mathrm{H}$ adsorbate-surface system, and is the electron density of the isolated $\mathrm{H}$ atom/ $\mathrm{H}_{2}$ molecule at the same position as in the adsorbatesurface system. The calculations of charge density were then carried out including the dipole correction.

In addition, we have attempted to find the minimum energy pathways and calculate diffusion barriers for $\mathrm{H}$ hopping into and out of a vacancy trap from a nearby interstitial site (e.g., tetrahedral site) by the NEB method using three images. H-vacancy interaction has also been studied by means of the projected density of states (PDOS) of perfect and imperfect $\mathrm{Er}_{2} \mathrm{O}_{3}$. The imperfection comes from point defects such as vacancies. Consideration of quantum effects [20] is important at low temperatures for light species such as atomic $\mathrm{H}$. Therefore, zero-point-energy (ZPE) corrections have been considered at the high-symmetry adsorption sites by summing up the zero-point vibrational energies of the H's normal mode, i.e., where $v_{i}$ is the real normal mode frequency [22,23].

## 3. Results and discussions

### 3.1. Bulk properties

Cubic $\mathrm{Er}_{2} \mathrm{O}_{3}$ belongs to space group Ia3 and a unit cell has $32 \mathrm{Er}$ atoms occupying the $8 \mathrm{a}$ and $24 \mathrm{~d}$ equipoints and $48 \mathrm{O}$ atoms occupying $48 \mathrm{e}$ equipoints. A lattice constant of $1.0545 \mathrm{~nm}$ derived by DFT calculations and fitted to Birch-Murnaghan 3rd-order equation of state (EOS) [24] corresponds well with the experimental data of $1.05431 \mathrm{~nm}$ [5]. The corresponding bulk modulus has also been calculated using the above equation as $B_{0}=148.0 \mathrm{GPa}$, in good agreement with the experimental result $B_{0}=140.7 \mathrm{GPa}[6,24]$ within a deviation of $5 \%$. The electronic density of states (DOS) of bulk $\mathrm{Er}_{2} \mathrm{O}_{3}$ has been calculated using GGA, as shown in Fig. 1. The valence band maximum (VBM) exhibits mainly $\mathrm{O} 2 \mathrm{p}$ features while the conduction band minimum (CBM) mainly consists of Er 5d electrons, in which all $4 \mathrm{f}$ electrons are localized and may fully be treated as valence states. This suggests that strong ionic characteristics with weak covalency exist in $\mathrm{Er}-\mathrm{O}$ bonding in bulk $\mathrm{Er}_{2} \mathrm{O}_{3}$.

In addition, band structures of $\mathrm{Er}_{2} \mathrm{O}_{3}$ have been calculated at 45 regularly spaced $k$ points in the irreducible portion of the Brillouin zone (BZ) by straightforward matrix diagonalization. Calculated band structures along the high-symmetry axes of the BZ for $\mathrm{Er}_{2} \mathrm{O}_{3}$ are shown in Fig. 2. The calculated direct GGA gap of $4.01 \mathrm{eV}$ at $\Gamma$ is an underestimation compared to the experimental data of $5.30 \mathrm{eV}$

![](./images/814655988090011649_2.jpg)

Fig. 1. Total electronic density of states (DOS) of cubic Er₂O₃. VBM and CBM denote the valence band maximum and the conduction band minimum, respectively.

![](./images/814655988090011649_3.jpg)

Fig. 2. Calculated band structures of Er₂O₃.

[25]. As is well known, this discrepancy stems from the GGA in the density-functional theory. The discrepancy arising from the LDA may be larger than obtained using the GGA [26], i.e., the adsorption, penetration, and diffusion behaviors may be more accurately described by GGA functions [27]. We therefore choose to perform our calculations within the GGA.

### 3.2. H adsorption on cubic Er₂O₃(001) surface

As mentioned in the Introduction, cubic Er₂O₃(001) surface is chosen owing to experimental results [7,14]. This is basically similar to surfaces of hexagonal Al₂O₃ that are found to be surprisingly stable with metal Al-terminated surface layers in ultra high vacuum and theoretical simulations [28,29]. Therefore, a stoichiometric Er-terminated (001) surface is adopted in this study. The Er₂O₃(001) surface was reconstructed after surface relaxations to lower the surface energy. We analyzed several possibly attempted adsorption sites on this reconstructed surface, as shown in Fig. 3. Positions F and E are on top of an Er atom and an Er-Er bridge site in the first atomic layer, respectively. Positions C and D are on top of an O atom in the second atom layer and an O-O bridge site between the second and fourth atomic layer, respectively. Position A is on top of a fourfold hollow site surrounded by four neighboring O atoms from the second to the fourth atomic layer. Position B is on top of an Er-O bridge site between the first and fourth atomic layer. The most stable adsorption site for H on this surface is found to be related to position A, with an adsorption energy of -299.52 kJ/mol (-295.68 kJ/mol with ZPE corrections). It is a very strong chemisorption-prone surface, in which H preferentially adsorbs on the A hollow site and forms a strong covalent bond to oxygen by transferring charge to the surface and becoming ionized. The adsorption energies at the positions C and E are found to be -262.08 kJ/mol (-257.28 kJ/mol with ZPE corrections) and -261.12 kJ/mol (-256.32 kJ/mol with ZPE corrections), respectively, while those at the positions of B, D, and F do not exist because H spontaneously moves to bulk positions during the process of the energy minimization.

![](./images/814655988090011649_4.jpg)

Fig. 3. (a) Top view of the reconstructed Er₂O₃(001) surface with different hydrogen adsorption sites. The possible pathways for H diffusion on the surface are via (C-A-E-...), and to move to adjacent chains via A-C and A-E. (b) Side view of the reconstructed Er₂O₃(001) surface with different hydrogen adsorption sites. The Er₂O₃ slab includes 4 relaxed atomic layers and 10 unrelaxed atomic layers (24 Er, 36 O), along with a vacuum region of 14 Å.

A plot of charge density difference for H adsorption in the most stable A position is shown in Fig. 4 [30]. The charge density indicates a predominately covalent bonding of H-O via extensive charge transfer from the H atom to the surface, resulting in a slightly polarized H charge density. A clear gain of charge density appears in the region around the surface Er atoms near the F site, while a decrease of charge density around the adsorbed H atom occurs for the A site. Thus, the H atom forms strong interactions with neighboring four O atoms, and the electrostatic bond between the outermost Er atoms and their nearest O atoms is weakened. Fig. 4 shows that there is a slight charge accumulation above the Er atoms when the H atom is adsorbed at the A position. Such a charge accumulation is generally

![](./images/814655988090011649_5.jpg)

Fig. 4. The difference in charge density induced by the adatom (H). The contour values are $-5.0×10^{-5}$ e/nm³ (yellow) and $+5.0×10^{-5}$ e/nm³(blue) in which the blue and yellow planes correspond to accumulation and depletion of electrons, respectively [30]. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

regarded as originating from the polarization of the metal atoms because of the electronic field of the surface [31]. Alternately, this charge buildup can also be explained as a charge transfer from H to the Er-surface dangling bond. In Fig. 4, we show two isosurfaces at $D_q=-5.0×10^{-5}$ e/nm³ and $D_q=+5.0×10^{-5}$ e/nm³. This charge transfer and the concurrent ionization of the H atom allows for a subsequent electrostatic interaction with the neighboring four O atoms owing to their closed-shell character. The charge accumulation above the surface Er atoms accordingly results in the formation of a covalent H—O bond. The mechanism of H adsorption at the A site can be described as consisting of two processes. One is the valence electron transfer from the H atom to surface electron-poor Er atoms nearby. Charge densities of these surface Er atoms correspondingly increase when the H atom is ionized because of charge transfer. The other is the subsequent electron sharing between the $O^{-2}$ anion and the electron depleted H atom, i.e., electrostatic interaction between the ionized H and the four surrounding $O^{-2}$ anions, which is strong enough to form the covalent H—O bond.

### 3.3. H diffusion on and from cubic $Er_2O_3(001)$ surface

After analyzing H adsorption on $Er_2O_3(001)$ surface, we employed the previous slabs model to derive the diffusion process of hydrogen through this surface, in terms of H diffusion on $Er_2O_3(001)$ surface and H penetration from the surface to the bulk sites. We identify three possible pathways to describe the hops between the sites: A–A′ (where A′ is A's symmetric position), A–E, and A–C (Fig. 3(a)). The energy barrier for A–A′ hopping is predicted to be 0.26 eV (0.24 eV with ZPE corrections), A–E hopping to be 0.27 eV (0.23 eV with ZPE corrections), and A–C hopping to be 0.34 eV (0.31 eV with ZPE corrections) and the reverse process of C–A hopping to be 0.12 eV (0.09 eV with ZPE corrections), using the NEB method. It is worth mentioning that the highest energy of the minimum energy pathway (A–C) is located towards the end of the pathway, with a migration barrier of 0.34 eV (0.31 eV with ZPE corrections), while the energy barriers along the rest of the path are less than 0.22 eV each (0.20 eV with ZPE corrections). The maximum in the pathway of A–C diffusion corresponds to the location where atomic H goes through the highest number of bond making/breaking events during the diffusion, i.e., with the atomic H migrating between sites where it is highly coordinated with oxygen [32]. According to the activation energies of hydrogen diffusion, it can be concluded that H is predicted to diffuse along zigzag chains via (C–A–E–. . .), and to move to adjacent chains via A–C and A–E.

![](./images/814655988090011649_6.jpg)

Fig. 5. Energy profile for H adsorption and permeation for $Er_2O_3(001)$ surface with a penetration energy of 1.61 eV. ZPE corrections are not included in the profile of energies. The vertical dashed lines show the positions of the surfaces.

After surface stable sites (e.g., A, C, E) for H adsorption on $Er_2O_3(001)$ surface are determined, it is essential to define bulk sites (solution site) for H penetration. Fig. 5 shows a possible high-symmetry solution site, L2, located at a tetrahedral site (TS). As a TS is energetically favorable for H penetration, we investigate hydrogen penetration from the $Er_2O_3(001)$ surface with the pathway from the A site to the L2 site. For our low surface coverage of hydrogen $(0.89×10^{14} H/cm^{2})$, a penetration energy of at least 1.61 eV (1.60 eV with ZPE corrections) is required for cubic $Er_2O_3(001)$ surface.

### 3.4. H diffusion in bulk $Er_2O_3$

In a previous work [33], the diffusion behavior of H in bulk $Er_2O_3$ has been studied using DFT calculations. In this study, we have analyzed three different pathways for H diffusion among neighboring tetrahedral sites or between a TS and an octahedral site (OS). TS and OS positions of bulk $Er_2O_3$ are depicted in Fig. 6(a) and (b), respectively. Nudged elastic band calculations have been performed for the unit cell of $Er_2O_3$. Energy barriers of 0.21 eV (0.16 eV with ZPE corrections), 0.43 eV (0.41 eV with ZPE corrections), and 1.63 eV (1.64 eV with ZPE corrections) have been determined for H hopping from TS-to-TS (along ⟨1 1 1⟩ direction), TS-to-OS, and OS-to-OS positions, respectively. However, H diffusion for OS-to-OS sites is a rare event even at a considerable temperature (e.g., 1400 K). This is confirmed by the calculated H trajectory in ab initio molecular dynamics (MD) simulations, in which the timestep is set to 0.5 fs, and the temperature is set to 1100–1400 K in a grand-canonical ensemble (constant chemical potential, volume, and temperature). As a result, the dominant mechanisms of H diffusion in bulk $Er_2O_3$ are diffusion from TS-to-TS and TS-to-OS rather than OS-to-OS positions directly.

![](./images/814655988090011649_7.jpg)

Fig. 6. Stable sites for H interstitial found by bonding the neighboring Er atoms in which local minima positions are located either in the (a) tetrahedral site (TS) or in the (b) octahedral site (OS) of bulk $Er_2O_3$. TS/OS positions are surrounded by Er atoms.

![](./images/814655988090011649_8.jpg)

Fig. 7. Calculated total density of states (DOS) for a perfect $\text{Er}_2\text{O}_3$ crystal, an $\text{Er}_2\text{O}_3$ crystal with a neutral oxygen vacancy defect, and an $\text{Er}_2\text{O}_3$ crystal with an isolated neutral oxygen vacancy containing one H atom.

### 3.5. H-vacancy interaction in bulk $\text{Er}_2\text{O}_3$

Vacancy defects behave as electron traps since the hydrogen-vacancy defect is regarded as more stable than vacancy defects. This can be verified by an analysis of the total DOS of perfect and imperfect $\text{Er}_2\text{O}_3$. The imperfection comes from point vacancy defects, such as the oxygen vacancy as indicated in Fig. 7. Hydrogen's promotion of oxygen vacancy stability is related to its ability to form multicenter bonds [34-36]. The loss of oxygen breaks 2 or 3 Er–O bonds, leaving dangling bonds and two electrons which may be trapped by an unbalanced Coulomb potential associated with the vacancy. A DOS peak caused by a neutral oxygen vacancy is noticeably reduced when the oxygen vacancy traps a hydrogen atom (Fig. 7). Hydrogen therefore appears to form chemical bonds with one or more surrounding Er atoms. The PDOS in Fig. 8 is given at a TS position in the vacancy, which is the most stable configuration of H-vacancy interaction. In this configuration, H 1s orbital strongly interacts with the neighboring Er atoms (mainly 5d orbital) to form multicenter bonds. Thus, H atoms play an important role in making passivating vacancies stable by diffusion.

After analyzing H-vacancy interaction via PDOS using the supercell with a small concentration of vacancies and hydrogen, we keep all cell lattice parameters fixed and calculate migration barriers of H diffusion near an O vacancy for H trapping by the NEB method. When trapped near the vacancy, H is predicted to situate at a tetrahedral-like site where it is surrounded by O atoms (Fig. 9). It is energetically favorable for an H atom to reside near a vacancy relative to a bulk tetrahedral site. In addition, we attempt to find the minimum energy pathway for H hopping into and out of a vacancy trap from a nearby interstitial site. For the case of the O vacancy, we predict that H diffuses from TS near the vacancy (initial point) to TS at the vacancy via an exothermic reaction, as indicated in Fig. 9. In the case of an Er vacancy, we predict that H diffusion from TS/OS to OS near the vacancy is energetically favorable due to an exothermic reaction. Therefore, it is considered that H atom can be readily trapped when it is close to an O/Er vacancy.

### 3.6. Quantum effects on H behavior in bulk $\text{Er}_2\text{O}_3$

Quantum effects on H behavior in $\text{Er}_2\text{O}_3$ were considered in terms of zero-point energy (ZPE) corrections and H isotope effect. Total potential energies at critical points, such as TS/OS positions and saddle sites, were calculated for H behaviors including the ZPE corrections. Considering the isotope effect of hydrogen, we substituted deuterium/tritium for hydrogen to simulate its behavior in $\text{Er}_2\text{O}_3$ via DFT calculations. The potentials for H, D, and T are different due to their distinct masses. The total potential energies were therefore calculated for H, D, and T, respectively.

![](./images/814655988090011649_9.jpg)

Fig. 8. Projected density of states (PDOS) on the nearest Er neighbor of oxygen vacancy (a) of a perfect $\text{Er}_2\text{O}_3$ lattice, (b) in a lattice with an oxygen atom, (c) in a lattice with an oxygen vacancy containing an H atom, and (d) PDOS of the single H atom with 1s channel. From (a) to (c), 5d channel of Er atoms is shown in PDOS.

From the DFT calculations, we found that the difference in total potential energies, at the critical sites between interstitial H, D, and T atoms, was less than $10^{-4}$ eV in terms of perfect and imperfect $\text{Er}_2\text{O}_3$. Although H, D, and T atoms possess different normal mode

![](./images/814655988090011649_10.jpg)

Fig. 9. H diffusion near an oxygen vacancy defect in $\text{Er}_2\text{O}_3$, calculated by the NEB method using three images.

frequencies [23], ZPE corrections of H/D/T adsorption energies, penetration and diffusion energy barriers reinforce the fact that the deviation of the energies is less than 0.05 eV between H, D, and T atoms. Consequently, the isotope effect may be ignored within ±0.05 eV. In other words, H is eligible for substituting D/T for simu- lating their behavior in $Er_2O_3$. This approach is reasonable because an H/D/T atom is much lighter than the oxygen and erbium atoms.

## 4. Conclusions

In this work, we have performed ab initio calculations based density functional theory to investigate H isotope behaviors in $Er_2O_3$, such as adsorption, penetration, diffusion, and vacancy trapping. We found that H preferentially adsorbs on top of a fourfold-hollow site and forms strong covalent bonds via charge transfer from H to the surface, thereby resulting in a slightly polarized H charge density. For low surface coverage of hydrogen $(0.89 × 10^{14} H/cm^2)$ as considered by us, H diffusion barrier on the cubic $Er_2O_3(001)$ surface is predicted to be a small energy bar- rier of ~0.20 eV along zigzag pathways, while a penetration energy of at least 1.60 eV is required for the surface. As for H diffusion in bulk $Er_2O_3$, the migration barrier for H diffusion between the planes defined by $Er_2O_3$ units along the favorable $\langle 111 \rangle$ direction is found to be very small at 0.16 eV, while higher migration barriers of 0.41 eV and 1.64 eV have been determined for diffusion across the planes, somewhat higher than the 0.20 eV observed experimentally at 873 K [37]. Additionally, interstitial H is predicted to be exother- mically trapped on approaching a vacancy in $Er_2O_3$. It is worth mentioning that H isotope effect may be neglected within an energy deviation of 0.05 eV, thus H may be substituted by D/T to simulate their behavior in bulk $Er_2O_3$. Our calculations provide some insight into microscopic behaviors of H in $Er_2O_3$. As H behavior plays an important role in the processes of H isotope permeation, the results of H adsorption, penetration, diffusion, and trapping enable a fun- damental understanding of H isotope permeation on the basal plane of erbium atoms, with the adsorption, penetration, and diffusion energies in $Er_2O_3$ predicted to be much larger than those obtained in bare Fe [27]. This suggests that there is a low H permeability in $Er_2O_3$, which places it as a strong candidate material for TPB coatings.

## Acknowledgments

This work was supported in part by the Global Center of Excel- lence (G-COE) Program of the Nuclear Education and Research Initiative of the Japan Society for the Promotion of Sciences (JSPS).

## References

[1] V.A. Maroni, Tritium Processing and Containment technology for fusion reactors: perspective and status, in: Proc. Second Topical Meeting on the Technology of Controlled Nuclear Fusion, 1976, p. P799, USERDA Report CONF-760935-P3.
[2] F.N. Flakus, At. Energy Rev. 13 (1975) 587.
[3] D. Levchuk, S. Levchuk, H. maier, H. Bolt, A. Suzuki, J. Nucl. Mater. 1033 (2007) 367-370.
[4] Z. Yao, A. Suzuki, T. Muroga, K. Katahira, J. Nucl. Mater. 1414 (2004) 329-333.
[5] Y.E. Bogatov, A.K. Molodkin, M.G. Safronenko, Y.Y. Nevyadomskaya, Russ. J. Inorg. Chem. 39 (1994) 211.
[6] L. Eyring, The binary rare earth oxides, in: K.A. Gschneider Jr., L. Eyring (Eds.), Handbook on the Physics and Chemistry of Rare Earths, vol. 3, North Holland Publishing Co., Amsterdam, Netherlands, 1979, pp. 337-398.
[7] T. Chikada, A. Suzuki, C. Adelhelm, T. Terai, T. Muroga, Nucl. Fusion 51 (2011) 063023.
[8] K. Honkala, A. Hellman, I.N. Remedeiakis, Á. Logadóttir, A. Carlsson, S. Dahl, et al., Science 507 (2005) 555.
[9] D.S. Sholl, J. Alloys Compd. 462 (2007) 446-447.
[10] C.F. Chen, H.B. Yu, S.Q. Zheng, Sci. China, Ser. E: Technol. Sci. 54 (2010) 88.
[11] S.C. Li, Z.R. Zhang, D. Sheppard, B.D. kay, J.M. White, Y.G. Du, et al., J. Am. Chem. Soc. 130 (2008) 28.
[12] B. Tuttle, Phys. Rev. B: Condens. Matter 61 (2000) 4417.
[13] A.B. Belonoshko, A. Rosengren, Q. Dong, G. Hultquist, C. Leygraf, Phys. Rev. B: Condens. Matter 69 (2004) 024302.
[14] T. Chikada, A. Suzuki, T. Kobayashi, H. Maier, T. Muroga, J. Nucl. Mater. 417 (2011) 1241.
[15] G. Kresse, J. Furthmuller, Phys. Rev. B: Condens. Matter 54 (1996) 11169.
[16] J.P. Perdew, Y. Wang, Phys. Rev. B: Condens. Matter 45 (13244) (1992).
[17] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (3865) (1996).
[18] H.J. Monkhorst, J.D. Pack, Phys. Rev. B: Condens. Matter 13 (1976) 5188.
[19] B. Hinnemann, E.A. Carter, J. Phys. Chem. 111 (2007) 7105.
[20] J. Neugebauer, M. Scheffler, Phys. Rev. B: Condens. Matter 46 (1992) 16067.
[21] H. Jonsson, G. Mills, K.W. Jacobsen, in: B.J. Berne, G. Ciccotti, D.F. Coker (Eds.), Classical and Quantum Dynamics in Condensed Phase Simulations, World Sci- entific, Singapore, 1998, pp. 385-404.
[22] D.E. Jiang, E.A. Cater, Phys. Rev. B: Condens. Matter 70 (2004) 064102.
[23] D.F. Johnson, E.A. Cater, J. Mater. Res. 25 (2010) 315.
[24] F. Birch, Phys. Rev. 71 (1947) 809.
[25] A.A. Sharif, F. Chu, A. Misra, T.E. Mitchell, J.J. Petrovis, J. Am. Soc. 83 (2000) 2246.
[26] F. Wallin, J.M. Andersson, E.P. Münger, V. Chirita, U. Helmersson, Phys. Rev. B: Condens. Matter 74 (2004) 125409.
[27] D.C. Sorescu, Catal. Today 105 (2005) 44.
[28] P.D. Tepesch, A.A. Quong, Phys. Status Solidi 217 (2000) 377.
[29] J. Toofan, P.R. Watson, Surf. Sci. 401 (1998) 162.
[30] W. Mao, T. Chikada, K. Shimura, A. Suzuki, K. Yamaguchi, T. Terai, J. Nucl. Mater. 443 (2013) 555.
[31] N.C. Hernandez, J.F. Sanz, J. Phys. Chem. B 106 (2002) 11495.
[32] H. Iddir, L.A. Curtiss, J. Phys. Chem. C 114 (2010) 20903.
[33] W. Mao, T. Chikada, K. Shimura, A. Suzuki, T. Terai, Fusion Eng. Des. 88 (2013) 2646.
[34] J. Kang, E.C. Lee, K.J. Chan, Appl. Phys. Lett. 84 (2004) 3894.
[35] A. Janotti, C.G. Van De Walle, Nat. Mater. 6 (2007) 44.
[36] M.H. Du, K. Biswas, Phys. Rev. Lett. 106 (2011) 115502.
[37] T. Chikada, A. Suzuki, H. Maier, T. Terai, T. Muroga, Fusion Sci. Technol. 60 (2011) 389.