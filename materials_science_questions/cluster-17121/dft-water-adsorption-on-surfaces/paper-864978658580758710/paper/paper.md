# Characterization of Hole States at the Zn-Doped Hematite/Water Interface from *Ab Initio* Simulations
Zachary K. Goldsmith,* Zhutian Ding, and Annabella Selloni*

ABSTRACT: Hole states at the surface of hematite ($\alpha$-Fe$_2$O$_3$) are highly influential in the material's performance as a photoanode for the oxygen evolution reaction. Zn-doping of hematite is known to both lower the overpotential for oxygen evolution and introduce hole carriers near the surface. In this work, hole states at the aqueous interface of hematite (0001) were characterized using density functional theory-based *ab initio* molecular dynamics (AIMD) together with hybrid density functional theory (DFT) calculations of the electronic structure. PBE0 with 12% exact exchange calculations of Zn-doped hematite (0001) slabs in vacuum revealed a hole state within the band gap of hematite, which was spatially localized on a Fe−O moiety in an adjacent layer of the slab. AIMD of the (0001) slab in contact with water was propagated at the PBE+D3 and PBE+U+D3 levels of theory, with hybrid PBE0 calculations performed on snapshots every 200 fs. Under both protocols we observed the fluctuation of the hole state energy within the band gap and the localization of the hole at the aqueous interface. Zn doping had an overall marginal effect on the interfacial hydration structure and hydrogen bonding dynamics. These calculations showed that Zn doping introduces surface-local hole states in the band gap at energies close to the O$_2$/H$_2$O redox level, providing atomistic insights into the lower overpotential observed for Zn-doped hematite and more broadly the potential role of surface-local hole states in driving water oxidation.

KEYWORDS: hematite, OER, doping, defect states, *ab initio* molecular dynamics

![](./images/864978658580758710_1.jpg)

## INTRODUCTION
Many earth-abundant transition metal oxides are efficient photoanodes for the oxygen evolution reaction (OER), a four-electron, four-proton reaction central to many renewable energy storage technologies. $^{1}$ Among the most promising of these photocatalysts is hematite ($\alpha$-Fe$_2$O$_3$), a highly stable oxide with a band gap of 2.0−2.2 eV that absorbs a significant portion of the visible spectrum. $^{2}$ The exciton photophysics of hematite photoanodes have been extensively studied such that the hematite OER photocurrent is known to be limited by the fast electron−hole recombination, $^{3,4}$ poor conductivity, $^{5}$ and trap states. $^{6}$ Recent experiments and simulations have also identified the ultrafast formation of polarons as a possible limitation on the photovoltage accessible to hematite-based photoelectrochemical cells. $^{7,8}$

Doping has been a productive means of enhancing the carrier density and photocatalytic efficiency in hematite cells. $^{9−14}$ $N$-type, redox doping of hematite has prominently been shown to increase the carrier density and catalytic current density for OER. $^{10,15−17}$ $P$-type doping of hematite, which has historically garnered less attention, introduces hole carriers to the system and has been understood to lower the overpotential for OER albeit while demonstrating lower current densities. $^{18,19}$ Most promisingly, tandem $n$- and $p$-type doping of hematite has been shown to achieve both lower overpotentials and equivalent or greater current densities. $^{20−22}$ Zn is one such $p$-type dopant in hematite understood to lower its overpotential for OER and improve its efficiency when codoped with $n$-type dopants such as Ti. $^{23−25}$ As a typically nonredox ion, experiments have demonstrated the selectivity of Zn for the surface of hematite photoanodes in contact with aqueous solution. $^{24}$ Calculations have further suggested that Zn at the hematite photocatalyst surface results in a lower activation barrier for the OER. $^{24,26}$ However, the character and dynamics of the excess hole carriers introduced by Zn doping of hematite in contact with water have not yet been elucidated.

Computational studies of hematite systems have been complicated by the system's inherent partially filled $d$ band, which is a fundamental challenge for semilocal density functional theory (DFT) methods, $^{27}$ and its antiferromagnetic structure, which incurs a computational cost associated with

Received: January 24, 2023
Revised: March 21, 2023
Published: April 4, 2023

![](./images/864978658580758710_2.jpg)

© 2023 The Authors. Published by
American Chemical Society
5298
https://doi.org/10.1021/acscatal.3c00357
ACS Catal. 2023, 13, 5298−5306

performing spin-polarized (unrestricted) calculations. While the optoelectronic properties of pure, bulk hematite have been well-characterized using many-body perturbation theory,²⁸ practical studies of interfacial, doped/defected systems must rely on DFT, for which best practices including employing a Hubbard $U$ and hybrid functionals have been established.⁹,²⁹⁻³¹ However, few dynamical studies of the hematite–water interface at the hybrid DFT level of theory or higher have been performed,³²,³³ let alone with excess charge carriers introduced by doping.

Recent spectroelectrochemical and DFT data for OER by pure hematite underscore the mechanistic importance of hole density at the hematite photoanode’s aqueous interface to the formation of O–O bonds.³⁴ The third-order OER rate dependence on surface hole density has also recently been observed *via* transient photocurrent measurements and DFT.³⁵ Spin-constrained DFT calculations furthermore have revealed the low mobility of hole carriers in hematite relative to electrons.³⁶ Therefore, it is imperative to elucidate the nature and dynamics of surface-local holes at the hematite–water interface.

Here, we perform a hybrid DFT-based analysis of Zn-doped hematite (0001) slabs in a vacuum and interfaced with water. The substitution of Fe with Zn into the hematite lattice introduces a hole defect state in the band gap, which we observe to be localized on the surface of hematite both in vacuum and in contact with water. More than 50 ps of DFT-based *ab initio* molecular dynamics (AIMD) of the Zn-doped hematite/water interface was accumulated to assess the effect of thermal fluctuations on the hole state and to determine whether its presence affected the properties of water at the interface. AIMD revealed the sensitivity of the hole state’s localization to the Fe–O bond lengths *vis-à-vis* the choice of DFT protocol. While the addition of a repulsive Hubbard $U$ term on the Fe 3d states (DFT+$U$) is known to improve the band gap of hematite, we observed the likely overdelocalization of the hole defect state at geometries predicted by DFT+$U$-based dynamics. In addition, AIMD revealed the fluctuations in energy, as computed at the hybrid DFT level, of the hole defect state with respect to the valence band edge. Through these simulations, the hole defect state remained not only energetically within the hematite band gap throughout the dynamics but also demonstrated an average energy level within 0.2 eV of the standard potential for OER. This effort highlights the important roles that aqueous interfacial dynamics and DFT protocol can play in elaborating the electronic and structural properties of materials for solar photocatalysis.

### METHODS
#### DFT Calculations.
DFT calculations were performed using CP2K³⁷ with Goedecker–Teter–Hunter pseudopotentials,³⁸ a hybrid Gaussian (DZVP)-plane wave basis set with cutoff of 400 Ry, and the auxiliary density matrix method for wave function fitting.³⁹ Due to the AFM ordering of pure and Zn-doped hematite, all calculations were done using unrestricted Kohn–Sham DFT. Given the large supercells used to model the systems of interest (see below), k-space sampling was restricted to the $\Gamma$ point.

All electronic structure analyses herein are based on PBE0 level calculations with an exact exchange fraction $\alpha_{xc} = 0.12$ (denoted PBE0(0.12)), in accordance with the literature best practices for hematite systems,⁴⁰,⁴¹ and a cutoff radius of 4 Å. AIMD trajectories were propagated with the PBE functional and Grimme’s D3 dispersion corrections.⁴² A portion of the AIMD trajectory for Zn-doped hematite was performed with a PBE+$U$ scheme in which $U = 4.3$ eV was applied to the d orbitals of Fe, as has been shown previously to best approximate the band gap of bulk hematite.²⁸

Computational System. Calculations for bulk hematite were performed using a $2 \times 2 \times 1$ hexagonal supercell with 120 atoms ($\text{Fe}_{48}\text{O}_{72}$). The lattice vector lengths were $a = b \approx 10.1$ Å and $c \approx 13.8$ Å along the (0001) direction. The unit cell was initialized with antiferromagnetic ordering along (0001) (hereafter referred to as $z$ axis) in a $\alpha\beta\beta\alpha$ or + − − + pattern, in accordance with literature reports. The band gap for the pristine bulk after a cell relaxation with PBE0(0.12) was 2.53 eV, in good agreement with experimental estimates of $\sim$2.2 eV.² Zn was most stable in the bulk when incorporated into a characteristically $\beta$ spin Fe site, with the resulting system being a $S = 2$ quintet. The projected density of states (PDOS) for the pure and doped bulk systems are shown in Figures S1 and S2.

As in previous work on pure hematite–water interfaces,⁴¹,⁴³,⁴⁴ a six-layer (0001) slab was employed for surface and aqueous interfacial calculations. The slab with two fully hydroxylated surfaces had a stoichiometry of $\text{Fe}_{48}\text{O}_{84}\text{H}_{24}$ and more than 10 Å separated adjacent slabs in vacuum calculations. The surface unit cell was hexagonal with surface-parallel dimensions $\sim$10.1 Å (see Figure 1). The layers of the slab carried alternating characteristic $\alpha$ and $\beta$ magnetism such that there was one of each type of surface, and the same for subsurface and interior layers. This was consequential in choosing sites at which Zn may be most stably incorporated.

![](./images/864978658580758710_3.jpg)

Figure 1. Computational unit cell of Zn-doped hematite interfaced with water. Fe atoms are gray, O atoms are red, the Zn dopant is purple, and H atoms are white. Hydrogen bonds are indicated by dashed lines. The surface-perpendicular $z$ dimension is depicted here as the horizontal.

For aqueous interfacial calculations, we introduced 56 $\text{H}_{2}\text{O}$ molecules, which formed a water region of about 19 Å separating the surfaces. A representative snapshot of this computational unit cell is shown in Figure 1. Furthermore, Zn doping was accomplished by substituting one of the 48 Fe atoms for Zn. This doping fraction of $\sim$2% is lower than the optimal Zn loading of 8%²⁴ but enabled a straightforward analysis of the electronic and structural effects of Zn doping, especially near the water interface. For these calculations, a Zn dopant was introduced into one of the three characteristically spin $\beta$ Fe layers: the surface, subsurface, or interior. AIMD was performed with a slab with two H atoms removed from the surface proximal to a subsurface Zn dopant to better approximate the surface composition under working catalytic conditions (see Table S4 and the accompanying text).

Ab Initio Molecular Dynamics Protocol. The AIMD was performed starting from a relaxed, Zn-doped hematite (0001) slab that had been twice dehydrogenated on the surface proximal to the Zn dopant in contact with a random water configuration. After a short, 2.5 ps trajectory performed fully at the PBE0(0.12) level, more than 50 ps of AIMD was accumulated for the Zn-doped hematite/water system using CP2K/Quickstep.³⁷ We employed a Nosé–Hoover thermostat in the NVT ensemble at 300 K and with a 0.5 fs time step. The first ~35 ps of the trajectory were run using the PBE+D3 functional and the following ~15 ps utilized the PBE+U-D3 scheme. The structural and electronic consequences of the two different DFT protocols used to propagate the AIMD trajectory are discussed hereafter.

To analyze the electronic properties of Zn-doped hematite along the AIMD trajectory, we performed PBE0(0.12) calculations on snapshots every 200 fs. These PBE0(0.12) calculations were done for both the doubly dehydrogenated slab with which the dynamics was performed and with a fully rehydrogenated system that simplified the identification of the excess hole state associated with the Zn doping. The rehydrogenation of the slab was accomplished by identifying the deprotonated surface O atoms, inserting H atoms 1 Å away from these sites in the surface-perpendicular z direction, and performing a 10-step structural relaxation of the newly inserted H atoms with all else fixed. The electronic properties described in the main text refer primarily to the rehydrogenated system while electronic structure properties of the dehydrogenated slab are illustrated in Figures S12 and S13.

Free Energies of Dehydrogenation. Free energies of dehydrogenation, or equivalently proton-coupled redox potentials, of pure and doped hematite surfaces were computed based on the DFT energies of the dehydrogenated and hydrogenated surfaces in a vacuum, H₂, and entropic and zero-point energy terms. The free energy of dehydrogenation, ΔG, is defined here as,
$$
\Delta G = \Delta G^\circ - eE + k_{\text{B}}T \ln(10)\text{pH} \tag{1}
$$
where $\Delta G^\circ$ is the standard free energy of dehydrogenation, $e$ is the charge of an electron, $E$ is the applied potential, $k_{\text{B}}$ is Boltzmann's constant, and $T$ is temperature. The standard free energy of dehydrogenation is expressed as,
$$
\Delta G^\circ = \Delta U + \Delta\text{ZPE} - T\Delta S \tag{2}
$$
in which $\Delta U$ is the electronic/internal energy difference between the products and reactant of the dehydrogenation reaction, $\Delta\text{ZPE}$ is the zero-point energy difference between the product and reactant slabs, and $\Delta S$ is the corresponding entropic difference. ZPE and TS contributions for hematite surface oxide and hydroxide moieties and H₂ were taken from previous calculations by Hellman and Pala.⁴⁰ However, the effects of these quantities on the relative free energies of dehydrogenation between pure and Zn-doped hematite were very small. Finally, we further elaborate $\Delta U$ as,
$$
\Delta U = \Delta U_{\text{slab}} + \frac{1}{2}U_{\text{H}_2} \tag{3}
$$
where $\Delta U_{\text{slab}}$ refers to the electronic energy difference between the dehydrogenated and hydrogenated slabs and $U_{\text{H}_2}$ is the electronic energy of H₂ as determined by the same DFT methodology as described above for the hematite–water systems. Up to two dehydrogenation free energies were computed for pure and Zn-doped hematite surfaces.

Hydrogen Bonding Analysis. Structural information and survival probability of hydrogen bonds (H-bonds) at the aqueous Zn-doped hematite surface were collected for the fully protonated and doubly deprotonated sides separately. The following geometric criterion was used to define a hydrogen bond: O···O shorter than 3.5 Å and O···H–O angle larger than 135°.⁴⁵ The survival probability is defined as,
$$
P(\Delta t) = \sum_{t_0=0}^{t_{\text{max}}} \frac{\sum_{i=1}^{N} I_i(t_0,\ t_0 + \Delta t)}{N(t_0)} \tag{4}
$$
where $I(t_0,\ t_0 + \Delta t)$ is the indicator function that is one only when a H-bond stays for the entire period between $t_0$ and $t_0 + \Delta t$. $N$ is the number of hydrogen involved in hydrogen bonding, $N(t_0)$ is the number of H-bonds at time $t_0$. A step size of 1 fs was used when collecting statistics. The survival probabilities were fitted with an exponential function, $P(t) = a \cdot \exp(-t/\tau) + c$, with characteristic time $\tau$. To assess the goodness of the fit, $\chi^2$ tests were performed, with the null hypothesis that there is no significant difference between the observed curve and the theoretical (fitted) curve. The degree of freedom is taken to be $n - 1$, where $n$ is the number of data points.

## RESULTS AND DISCUSSION
Electronic Structure of Zn-Doped Hematite (0001) in Vacuum. PBE0(0.12) calculations of the hematite (0001) slab in a vacuum with Zn doped in each of the three inequivalent layers demonstrated that Zn incorporation introduced a unoccupied defect state (DS) in the band gap, as shown in Figure 2. While the location of the Zn dopant affected the energy of the DS relative to the VBM and CBM, the creation of a hole DS was consistent among each of the different doping sites (see Figures S4 and S5 for surface and interior Zn dopants). In addition, isosurfaces of the DS indicate that the hole defect state is localized on a Fe–O moiety adjacent to the Zn dopant. Because Zn was thermodynamically more stable in the surface and subsurface layers, in accordance with previous experiments and DFT calculations (Table S2),²⁴ we neglected further study of the interior Zn-doped slab. When Zn was doped on the surface of the slab itself, the DS localized in the subsurface layer (Figure S6A). In contrast, Zn doping of the $\beta$ subsurface layer of hematite gave rise to a hole DS in the adjacent surface layer, as is illustrated in Figure 2C. To most straightforwardly explore the effects of the aqueous interface on excess charge carriers in hematite and their potential role in catalysis, we therefore proceeded with the subsurface Zn-doped system.

The computed projected density of states (PDOS) for the pure hematite and subsurface Zn-doped hematite (0001) slabs are shown in Figure 2A,B. The pure slab exhibited a VBM–CBM gap of 2.35 eV in both the $\alpha$ and $\beta$ channels, whereas the Zn-doped system demonstrated eigenvalue gaps of 1.46 and 1.97 eV in the $\alpha$ and $\beta$ channels, respectively. The significantly diminished energy gap in the $\alpha$ channel of the doped system is a consequence of the unoccupied DS. Nonetheless, the energy gap for the Zn-doped slab between the highest occupied eigenvalue (i.e., VBM) and the second lowest unoccupied eigenvalue (i.e., CBM) is 2.39 eV, a value comparable to the eigenvalue gap of the pure system. In all cases of Zn-doped hematite, we observed a band narrowing in the $\beta$ channel, possibly due to enhanced screening induced by the doping.⁴⁶ Furthermore, Figure 2 demonstrates that electronic states

![](./images/864978658580758710_4.jpg)

![](./images/864978658580758710_5.jpg)

Figure 2. PDOS around the band gap for (A) the pure hematite (0001) slab and (B) the subsurface Zn-doped hematite (0001) slab in a vacuum. In both cases, the surfaces are fully hydroxylated. The dashed lines indicate the highest occupied eigenvalue, set to zero here. The smearing width used in this and all PDOS plots was 0.05 au. (C) Isosurface (value 0.03; green and yellow for positive and negative, respectively) of the unoccupied DS wave function in the Zn-doped hematite (0001) slab localized predominantly around a surface Fe−O moiety. Fe atoms are gray, O are red, H are white, and Zn is purple.

associated with Zn do not contribute to the frontier orbitals of the system. From the PDOS of the Zn-doped slab (Figure 2B) it is clear there is an unoccupied DS within the band gap in the $\alpha$ channel of Fe and O character. The DS lies 1.46 eV from the VBM and 0.93 eV from the CBM. We note that the appearance of the DS in the $\alpha$ channel is a consequence of substituting Zn for an Fe with unpaired electrons of $\beta$ spin, which resulted in a net magnetic moment of $\alpha$ character.

The unoccupied DS for the subsurface Zn-doped hematite slab in vacuum was mostly local to a Fe−O moiety in the neighboring surface layer. This observation is consistent with previous DFT calculations of bulk hematite with an excess positive charge³⁶ as well as with our results for Zn-doped bulk hematite where the DS localizes primarily on an Fe−O site in an adjacent layer (Figure S3). The shape of the DS isosurface and its contributions from both Fe and O states are suggestive of an $e_g$ state of the Fe−O moiety, as shown in Figure 2.

Electronic Properties of the Zn-Doped Hematite−Water Interface. Given the high computational cost of running AIMD for this complex system with a hybrid functional and the lack of detailed experimental information on the atomic geometries, both PBE+D3 and PBE+U+D3 were used for the AIMD simulations. These simulations and the subsequent PBE0(0.12) calculations (every 200 fs) of the rehydrogenated slabs yielded the energy and localization of the excess hole DS at the Zn-doped hematite-water interface over more than 50 ps. The structures that resulted from the two different DFT schemes engendered qualitatively and quantita- tively different electronic properties with respect to the DS that we will delineate here.

The energy of the excess hole DS associated with Zn doping throughout the full AIMD trajectory is reported in Figure 3.

![](./images/864978658580758710_6.jpg)

Figure 3. Lowest five unoccupied energy eigenvalues in the $\alpha$ channel versus the energy of the VBM for Zn-doped hematite/water as a function of trajectory time. The lowest unoccupied eigenvalue (or LUMO) in this case is always the DS and is labeled as such. The vertical dashed line represents the change in AIMD protocol from PBE+D3 to PBE+U+D3.

The DS was on average at an energy 0.83 eV above the VBM during the PBE+D3 portion of the trajectory and 0.37 eV above the VBM during the PBE+U+D3 portion (Table 1).

<table><thead><tr><th>DFT protocol</th><th>trajectory time (ps)</th><th>DS energy vs VBM (eV)</th><th>VBM−CBM gap (eV)</th></tr></thead><tbody><tr><td>PBE+D3</td><td>35.7</td><td>0.83 ± 0.33</td><td>1.95 ± 0.22</td></tr><tr><td>PBE+U+D3</td><td>14.3</td><td>0.37 ± 0.20</td><td>2.06 ± 0.17</td></tr></tbody></table>
Table 1. DS Energies with Standard Deviations for the Trajectory Portions Accumulated Using PBE+D3 and PBE +U+D3

Given that these energies are both from PBE0(0.12) calculations, the lower DS energy within the band gap for the PBE+U+D3 portion can be ascribed to the structural differences associated with the two DFT protocols. These differences will be discussed in a later section. Table 1 also shows the small effect of the Hubbard $U$ on the PBE0(0.12)-computed band gap of the doped hematite−water system; the band gap is on average 1.95 eV with PBE+D3 structures and 2.06 eV with PBE+U+D3 structures. In addition, while the DS remained inside the VBM−CBM gap of hematite, its fluctuations in energy were significant, with standard deviations of 0.33 and 0.20 eV for the PBE+D3 and PBE+U+D3 trajectories, respectively. These fluctuations are comparable to those observed by hybrid DFT-based AIMD of frontier orbitals in $WO_3$ at 300 K.⁴⁷ From Figure 3 it also appears that for the rehydrogenated, Zn-doped hematite slab there is one unambiguous hole DS given that all of the higher energy unoccupied eigenvalues form the bottom of the conduction band. In the case of the doubly dehydrogenated slab with which the AIMD was run there were three unoccupied eigenvalues within the band gap that persisted throughout the dynamics (see Figure S13). The LUMO of the doubly dehydrogenated system demonstrated energies similar to, if not often slightly further from that of the VBM, the unambiguous DS from the reprotonated system (Figure S14).

PDOS plots for different snapshots along the AIMD trajectory are shown in Figure 4. For each snapshot, there is

![](./images/864978658580758710_7.jpg)

Figure 4. Projected density of states, computed with PBE0(0.12), as a function of energy referenced to the VBM (indicated by the dashed vertical lines) for Zn-doped hematite (0001) in contact with water for three snapshots from AIMD. The top snapshot is from the PBE+D3 portion of the trajectory and the central and bottom snapshots are from the PBE+U+D3 portion. $O_w$ and $H_w$ refer to the oxygen and hydrogen atoms of water molecules, respectively. Black arrows indicate the densities associated with the hole DS in each snapshot.

clearly a state of Fe and O character in the band gap in the $\alpha$ channel. In the PDOS for the snapshot at $t = 24.4$ ps, from the PBE+D3 portion of the trajectory, the DS is at higher energy relative to the VBM than in the PDOS for the snapshots at $t =$ 44.4 ps and at $t = 48.6$ ps, from the PBE+U+ D3 part. In addition, we note that electronic states associated with neither Zn nor water contributed to the frontier electronic states.

The localization of the excess hole DS also changed during the AIMD trajectory. During the PBE+D3 portion of the trajectory, the DS remained consistently localized on a surface Fe−O site, as illustrated by the $t = 24.4$ ps snapshot in Figure 5. The local character of the DS here is consistent with a larger inverse participation ratio, $P^{-1}$, of 2.27. Conversely, during the PBE+U+D3 trajectory portion the DS fluctuated between being delocalized across surface and subsurface O atoms (see Figure 5B) and being localized predominantly on one surface Fe−O site, similarly to the slab in a vacuum and PBE+D3 portion (Figure 5C). The delocalization of the hole DS across O sites has previously been observed for excess holes in doped hematite clusters by embedded unrestricted Hartree−Fock calculations.⁴⁸ The qualitative change in localization of the DS was correlated with a characteristic change in structure upon changing the DFT protocol, as will be shown in the section below. We note here that, while PBE+$U$ improves the band gap of hematite versus PBE, the DS is seemingly overdelocalized in PBE+$U$ geometries relative to PBE0(0.12), as demonstrated for the slab in a vacuum in Table S3.

These changes in (de)localization are quantified by the accompanying changes to the $P^{-1}$, as shown in Figure 6. While the calculated $P^{-1}$ values for the DS were consistently large during the PBE+D3 part of the trajectory, the DS $P^{-1}$ value was generally lower during the PBE+$U$+D3 portion and fluctuated significantly.

![](./images/864978658580758710_8.jpg)

Figure 6. Inverse participation ratio $P^{-1}$ for the HOMO, DS, and LUMO electronic states in the $\alpha$ channel during the AIMD of Zn-doped hematite/water. The dashed vertical line represents the time at which the DFT method changed from PBE+D3 to PBE+$U$+D3. Larger values of $P^{-1}$ are associated with more localized wave functions, and smaller values of $P^{-1}$ represent more delocalized wave functions.

The procedure for aligning the VBM and DS on the electrochemical scale, following literature protocol for semiconductor−water interfaces,⁴⁹,⁵⁰ is presented in Section S6 of the SI and illustrated by Figures S10 and S11. The result of the alignment at pH<sub>PZC</sub>³⁵ was a VBM level of 2.24 V vs RHE, in good agreement with experimental estimates for pure hematite.⁴,⁵¹ We thereafter estimated the DS level using its average level versus the VBM from the PBE+D3 portion of the trajectory of Zn-doped hematite (0001)/water (Table 1 and Figure 3). This yielded an average DS level of 1.41 V vs RHE, less than 0.2 V below the standard O₂/H₂O potential, a

![](./images/864978658580758710_9.jpg)

Figure 5. Isosurfaces (value 0.03; green and yellow for positive and negative, respectively) of the unoccupied DS wave functions at the same AIMD configurations as the PDOS plots in Figure 4: (A) 24.4 ps, (B) 44.4 ps, and (C) 46.8 ps for Zn-doped hematite (0001) interfaced with water. Fe atoms are gray, O are red, H are white, and Zn is purple. Hydrogen bonds are indicated by gray dashed lines. At the bottom right of each isosurface panel is the inverse participation ratio, $P^{-1}$ of the illustrated DS, for which a higher value is characteristic of a more localized state.

difference smaller than the fluctuations of the DS level during AIMD. Note that Kohn−Sham defect levels tend to be similar to optical/vertical transition levels whereas adiabatic defect levels may be shallower (closer to the VBM).⁵² Although the adiabatic DS level for Zn-doped hematite should be closer to the VBM than our Kohn−Sham level, it nonetheless may enable a smaller overvoltage for the oxidation of water/ hydroxide than that of undoped hematite,²⁴ a result consistent with the overall importance of hole states to OER photocatalysis.³⁴,³⁵

Structural Properties of the Zn-Doped Hematite−Water Interface. AIMD of Zn-doped hematite/water furthermore enabled a structural analysis with regard to the effects of Zn doping and the presence of the surface-local hole DS. Figure 7A depicts the Fe−O radial distribution functions

![](./images/864978658580758710_10.jpg)

Figure 7. (A) Fe−O radial distribution functions, $P(r_{\text{Fe−O}})$, for the surface Fe site on which the hole is localized ($\text{Fe}_{\text{hole}}$, black), all other Fe centers on the surface proximal to the Zn dopant (red), and all Fe centers on the opposite, undoped surface (blue). (B) Zoom-in of the first peak of $P(r_{\text{Fe−O}})$ for $\text{Fe}_{\text{hole}}$ for the PBE+D3 and PBE+U+D3 portions of the AIMD separately. (C) Water O and H densities versus distance from the two hematite surfaces ($z - z_{\text{surf}}$) in the simulation: the surface proximal to the Zn dopant, which was doubly dehydrogenated (solid lines), and the opposite, undoped surface that remained fully hydroxylated throughout the simulation (dashed lines).

for the Fe site on which the hole tended to localize ($\text{Fe}_{\text{hole}}$) in comparison with the other Fe centers on the surface proximal to the Zn dopant and the other surface of the slab. From these RDFs, it is clear that the $\text{Fe}_{\text{hole}}−$O bonds were appreciably shorter than all other surface Fe−O bonds. This result is consistent with the oxidation of this high-spin Fe site by the excess hole.⁵³

We also analyzed the structural differences of the Zn-doped hematite slab in contact with water by the DFT protocol used in each trajectory segment. Figure 7B exhibits the first RDF peak for $\text{Fe}_{\text{hole}}$ from the PBE+D3 and PBE+U+D3 segments of the trajectory separately. On average, we observed shorter $\text{Fe}_{\text{hole}}−$O bond lengths during the PBE+D3 portion of the trajectory and longer $\text{Fe}_{\text{hole}}−$O bond lengths during the PBE +U+D3 portion. The average $\text{Fe}_{\text{hole}}−$O bond lengths as a function of trajectory time are depicted in Figure S16 as well. This observation is consistent with the greater localization of the DS on this one surface Fe site given the correlation between shorter Fe−O bond lengths and greater oxidation.⁵³

Zn doping and even the proton-coupled oxidation of the hematite (0001) surface proximal to the Zn dopant ultimately had a marginal effect on the interfacial hydration structure and hydrogen bonding dynamics. Figure 7C depicts the water O and H densities as a function of distance from the two surfaces in the simulation. This plot illustrates that a structural layer of water with a peak density more than $4\times$ that of bulk liquid water formed against both surfaces, consistent with previous AIMD simulations of pure hematite (0001)/water.⁴¹ The greater initial H density peak for the doped/dehydrogenated surface is consistent with this surface's increased propensity for accepting hydrogen bonds from water. However, these changes are small, and crucially, we did not observe the exchange of protons between the surface and water during the 50 ps of equilibrium, room temperature AIMD. This is consistent with the very small change in surface basicity vis-à-vis the computed free energies of dehydrogenation. The observed stability of the (0001) surface is also in contrast with the picosecond time scale water/oxygen exchange observed at the hematite (11̅02)/ water interface.⁵⁴,⁵⁵

To characterize the effect of Zn-doping on the structure of H-bonds at the interface, we computed the distribution of O··· H distances on the fully protonated (top) and partially deprotonated (bottom) surfaces of the hematite slab. As shown in Figure 8, the O···H distances of the doubly deprotonated surface are marginally longer for intrasurface ($\text{O}_{\text{surf}}−\text{H}_{\text{surf}}\cdots$ $\text{O}_{\text{surf}}$) and surface-accepting ($\text{O}_{\text{w}}−\text{H}_{\text{w}}\cdots\text{O}_{\text{surf}}$) H-bonds than for surface-donating H-bonds ($\text{O}_{\text{surf}}−\text{H}_{\text{surf}}\cdots\text{O}_{\text{w}}$). Based on the time evolution of H-bond counts (Figure S17), intrasurface H- bonds also exhibit a larger standard deviation. This trend is further observed in the characteristic decay times of H-bonds as reported in Table S5. The intrasurface H-bonds have a shorter lifetime on the deprotonated surface than on the fully protonated surface. Comparing across different types of H- bonds, we observe that surface donating H-bonds have a much longer lifetime than the other two types.

## CONCLUSIONS

Hybrid DFT and AIMD simulations of candidate OER photocatalyst Zn-doped hematite characterized the energy, localization, and structural consequences of hole carrier states at the aqueous interface. The incorporation of Zn in an Fe site in the hematite (0001) slab's subsurface layer introduced an excess hole with an energy inside the material's band gap. This hole DS was found to be local to a surface Fe−O site with $e_{g}$ character. Upon interfacing the Zn-doped hematite (0001) slab with water and evolving more than 50 ps of AIMD, we found the energy and localization character of the DS to fluctuate and be dependent on the local geometry. At longer Fe−O bond lengths, the DS was closer in energy to the VBM and delocalized over surface and subsurface O orbitals, whereas at shorter Fe−O bond lengths, the hole DS was higher in energy relative to the VBM and maintained a localized $e_{g}$-like

![](./images/864978658580758710_11.jpg)

Figure 8. Distribution of O⋯H distances for intrasurface, surface-donating, and surface-accepting H-bonds at fully protonated (top) and partially deprotonated (bottom) hematite (0001) surfaces in contact with liquid water.

character on a surface Fe−O site. Nonetheless, this charge carrier remained within the band gap and mostly surface-local for the duration of the AIMD, demonstrating the utility of Zn doping in generating catalytically useful carriers. Moreover, that the DS appeared to fluctuate in energy near the level of the $O_2/H_2O$ redox couple further supports the utility of excess holes generated by Zn doping in lowering the OER overpotential. The Zn dopant lastly did not seem to appreciably alter the aqueous interfacial structure or hydrogen bonding properties relative to the pure hematite aqueous interface. These simulations provide insight into the role of p-doping in the OER on hematite and more broadly demonstrate the interplay between aqueous interfacial dynamics and charge carriers at a transition metal oxide surface.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acscatal.3c00357.

Figures of projected density of states, electronic structure of pure and Zn-doped hematite in the bulk and (0001) slab, plane-averaged electrostatic potential, lowest five unoccupied energy eigenvalues in the $\alpha$ channel, DS energy vs VBM from the reprotonated AIMD configuration, number density versus surface perpendicular $z$ for Fe, O, and H species, average bond lengths, and time evolution of the counts of H-bonds, tables of band gaps in the $\alpha$ and $\beta$ channels of pure and Zn-doped hematite, bulk and (0001) slab, electronic energies of Zn-doped hematite (0001) slabs, PBE0(0.12) DS energies versus the VBM, VBM-CBM energy gaps, and DS inverse participation ratio, free energies of dehydrogenation, and characteristic times from the exponential fitting of survival probability of three types of H-bonds, and discussions of inverse participation ratio, free energies of dehydrogenation, and level alignment of Zn-doped hematite VBM and DS on the electrochemical scale (PDF)

## AUTHOR INFORMATION

### Corresponding Authors
Zachary K. Goldsmith − Department of Chemistry, Princeton University, Princeton, New Jersey 08540, United States;
orcid.org/0000-0002-5556-4079; Email: zkg@princeton.edu

Annabella Selloni − Department of Chemistry, Princeton University, Princeton, New Jersey 08540, United States;
orcid.org/0000-0001-5896-3158; Email: aselloni@princeton.edu

### Author
Zhutian Ding − Department of Chemistry, Princeton University, Princeton, New Jersey 08540, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acscatal.3c00357

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors wish to thank Prof. Emily Carter and Dr. John Mark Martirez for fruitful conversations about the direction of this work. The authors acknowledge support from the Computational Chemical Science Center: Chemistry in Solution and at Interfaces, funded by the DoE under Award DE-SC0019394 and acknowledge use of the TIGRESS High Performance Computer Center at Princeton University.

## REFERENCES
(1) Walter, M. G.; Warren, E. L.; McKone, J. R.; Boettcher, S. W.; Mi, Q.; Santori, E. A.; Lewis, N. S. Solar Water Splitting Cells. Chem. Rev. 2010, 110, 6446−6473.
(2) Sivula, K.; LeFormal, F.; Grätzel, M. Solar Water Splitting: Progress Using Hematite ($\alpha$-Fe₂O₃) Photoelectrodes. ChemSusChem 2011, 4, 432−449.
(3) Huang, Z.; Lin, Y.; Xiang, X.; Rodríguez-Córdoba, W.; McDonald, K. J.; Hagen, K. S.; Choi, K.-S.; Brunschwig, B. S.; Musaev, D. G.; Hill, C. L.; et al. In situ probe of photocarrier dynamics in water-splitting hematite ($\alpha$-Fe₂O₃) electrodes. Energy Environ. Sci. 2012, 5, 8923−8926.
(4) Barroso, M.; Pendlebury, S. R.; Cowan, A. J.; Durrant, J. R. Charge carrier trapping, recombination and transfer in hematite ($\alpha$-

Fe₂O₃) water splitting photoanodes. *Chemical Science* **2013**, *4*, 2724–2734.

(5) Iordanova, N.; Dupuis, M.; Rosso, K. M. Charge transport in metal oxides: A theoretical study of hematite -Fe₂O₃. *J. Chem. Phys.* **2005**, *122*, 144305.

(6) Klahr, B.; Gimenez, S.; Fabregat-Santiago, F.; Hamann, T.; Bisquert, J. Water Oxidation at Hematite Photoelectrodes: The Role of Surface States. *J. Am. Chem. Soc.* **2012**, *134*, 4294–4302.

(7) Carneiro, L. M.; Cushing, S. K.; Liu, C.; Su, Y.; Yang, P.; Alivisatos, A. P.; Leone, S. R. Excitation-wavelength-dependent small polaron trapping of photoexcited carriers in α-Fe2O3. *Nat. Mater.* **2017**, *16*, 819–825.

(8) Pastor, E.; Park, J.-S.; Steier, L.; Kim, S.; Grätzel, M.; Durrant, J. R.; Walsh, A.; Bakulin, A. A. In situ observation of picosecond polaron self-localisation in α-Fe2O3 photoelectrochemical cells. *Nat. Commun.* **2019**, *10*, 1–7.

(9) Huda, M. N.; Walsh, A.; Yan, Y.; Wei, S.-H.; Al-Jassim, M. M. Electronic, structural, and magnetic effects of 3d transition metals in hematite. *J. Appl. Phys.* **2010**, *107*, 123712.

(10) Liao, P.; Keith, J. A.; Carter, E. A. Water oxidation on pure and doped hematite (0001) surfaces: Prediction of Co and Ni as effective dopants for electrocatalysis. *J. Am. Chem. Soc.* **2012**, *134*, 13296–13309.

(11) Engel, J.; Tuller, H. L. The electrical conductivity of thin film donor doped hematite: from insulator to semiconductor by defect modulation. *Phys. Chem. Chem. Phys.* **2014**, *16*, 11374–11380.

(12) Nguyen, M.-T.; Piccinin, S.; Seriani, N.; Gebauer, R. Photo-Oxidation of Water on Defective Hematite(0001). *ACS Catal.* **2015**, *5*, 715–721.

(13) Rauf, A.; Adil, M.; Mian, S. A.; Rahman, G.; Ahmed, E.; Mohy Ud Din, Z.; Qun, W. Tuning the optoelectronic properties of hematite with rhodium doping for photoelectrochemical water splitting using density functional theory approach. *Sci. Rep.* **2021**, *11*, 1–11.

(14) El-Gibally, H.; Shousha, S.; Allam, N. K.; Youssef, M. Maximizing the electronic charge carriers in donor-doped hematite under oxygen-rich conditions via doping and co-doping strategies revealed by density functional theory calculations. *J. Appl. Phys.* **2022**, *131*, 155705.

(15) Kleiman-Shwarsctein, A.; Hu, Y.-S.; Forman, A. J.; Stucky, G. D.; McFarland, E. W. Electrodeposition of α-Fe₂O₃ doped with Mo or Cr as photoanodes for photocatalytic water splitting. *J. Phys. Chem. C* **2008**, *112*, 15900–15907.

(16) Liu, Y.; Yu, Y.-X.; Zhang, W.-D. Photoelectrochemical properties of Ni-doped Fe₂O₃ thin films prepared by electrodeposition. *Electrochim. Acta* **2012**, *59*, 121–127.

(17) Pan, H.; Ao, D.; Qin, G. Synergistic effects of dopant (Ti or Sn) and oxygen vacancy on the electronic properties of hematite: A DFT investigation. *RSC Adv.* **2020**, *10*, 23263–23269.

(18) Kay, A.; Grave, D. A.; Ellis, D. S.; Dotan, H.; Rothschild, A. Heterogeneous doping to improve the performance of thin-film hematite photoanodes for solar water splitting. *ACS Energy Lett.* **2016**, *1*, 827–833.

(19) Tsyganok, A.; Klotz, D.; Malviya, K. D.; Rothschild, A.; Grave, D. A. Different Roles of Fe₁₋ₓNiₓOOH Cocatalyst on Hematite (α-Fe₂O₃) Photoanodes with Different Dopants. *ACS Catal.* **2018**, *8*, 2754–2759.

(20) Mirbagheri, N.; Wang, D.; Peng, C.; Wang, J.; Huang, Q.; Fan, C.; Ferapontova, E. E. Visible Light Driven Photoelectrochemical Water Oxidation by Zn- and Ti-Doped Hematite Nanostructures. *ACS Catal.* **2014**, *4*, 2006–2015.

(21) Singh, A. P.; Tossi, C.; Tittonen, I.; Hellman, A.; Wickman, B. Synergies of co-doping in ultra-thin hematite photoanodes for solar water oxidation: In and Ti as representative case. *RSC Adv.* **2020**, *10*, 33307–33316.

(22) Garcés-Pineda, F. A.; Chuong Nguyen, H.; Blasco-Ahicart, M.; García-Tecedor, M.; de Fez Febré, M.; Tang, P.-Y.; Arbiol, J.; Giménez, S.; Galán-Mascarós, J. R.; López, N. Push-Pull Electronic Effects in Surface-Active Sites Enhance Electrocatalytic Oxygen Evolution on Transition Metal Oxides. *ChemSusChem* **2021**, *14*, 1595–1601.

(23) Zhu, Q.; Yu, C.; Zhang, X. Ti, Zn co-doped hematite photoanode for solar driven photoelectrochemical water oxidation. *J. Energy Chem.* **2019**, *35*, 30–36.

(24) Nguyen, H. C.; Garcés-Pineda, F. A.; de Fez-Febré, M.; Galán-Mascarós, J. R.; López, N. Non-redox doping boosts oxygen evolution electrocatalysis on hematite. *Chemical Science* **2020**, *11*, 2464–2471.

(25) Li, J.; Wang, H.; Li, Y.; Xue, S.; Wang, Y. Hematite Photoanodes Decorated with a Zn-doped Fe₂O₃ Catalyst for Efficient Photoelectrochemical Water Oxidation. *Int. J. Electrochem. Sci.* **2022**, *17*, 22106.

(26) Simfukwe, J.; Mapasha, R. E.; Braun, A.; Diale, M. Exploring the stability and electronic properties of Zn-doped hematite surfaces for photoelectrochemical water splitting. *J. Phys. Chem. Solids* **2020**, *136*, 109159.

(27) Cococcioni, M.; De Gironcoli, S. Linear response approach to the calculation of the effective interaction parameters in the LDA+U method. *Phys. Rev. B* **2005**, *71*, 035105.

(28) Piccinin, S. The band structure and optical absorption of hematite (α-Fe₂O₃): a first-principles GW-BSE study. *Phys. Chem. Chem. Phys.* **2019**, *21*, 2957–2967.

(29) Pozun, Z. D.; Henkelman, G. Hybrid density functional theory band structure engineering in hematite. *J. Chem. Phys.* **2011**, *134*, 224706.

(30) Ansari, N.; Ulman, K.; Camellone, M. F.; Seriani, N.; Gebauer, R.; Piccinin, S. Hole localization in Fe₂O₃ from density functional theory and wave-function-based methods. *Phys. Rev. Mater.* **2017**, *1*, 035404.

(31) Rostami, S.; Seriani, N.; Gebauer, R. Hematite surfaces: Band bending and local electronic states. *Phys. Rev. Mater.* **2022**, *6*, 104604.

(32) Futera, Z.; English, N. J. Water Breakup at Fe₂O₃-Hematite/Water Interfaces: Influence of External Electric Fields from Non-equilibrium Ab Initio Molecular Dynamics. *J. Phys. Chem. Lett.* **2021**, *12*, 6818–6826.

(33) Wang, H.; Zhou, Z.; Long, R.; Prezhdo, O. V. Passivation of Hematite by a Semiconducting Overlayer Reduces Charge Recombination: An Insight from Nonadiabatic Molecular Dynamics. *J. Phys. Chem. Lett.* **2023**, *14*, 879–887.

(34) Mesa, C. A.; Francas, L.; Yang, K. R.; Garrido-Barros, P.; Pastor, E.; Ma, Y.; Kafizas, A.; Rosser, T. E.; Mayer, M. T.; Reisner, E.; et al. Multihole water oxidation catalysis on haematite photoanodes revealed by operando spectroelectrochemistry and DFT. *Nat. Chem.* **2020**, *12*, 82–89.

(35) Righi, G.; Plescher, J.; Schmidt, F.-P.; Campen, R. K.; Fabris, S.; Knop-Gericke, A.; Schlögl, R.; Jones, T. E.; Teschner, D.; Piccinin, S. On the origin of multihole oxygen evolution in haematite photoanodes. *Nature Catalysis* **2022**, *5*, 888–899.

(36) Ahart, C. S.; Rosso, K. M.; Blumberger, J. Electron and Hole Mobilities in Bulk Hematite from Spin-Constrained Density Functional Theory. *J. Am. Chem. Soc.* **2022**, *144*, 4623–4632.

(37) Kühne, T. D.; et al. CP2K: An electronic structure and molecular dynamics software package - Quickstep: Efficient and accurate electronic structure calculations. *J. Chem. Phys.* **2020**, *152*, 194103.

(38) Goedecker, S.; Teter, M.; Hutter, J. Separable dual-space Gaussian pseudopotentials. *Phys. Rev. B* **1996**, *54*, 1703–1710.

(39) Guidon, M.; Hutter, J.; VandeVondele, J. Auxiliary Density Matrix Methods for HartreeFock Exchange Calculations. *J. Chem. Theory Comput.* **2010**, *6*, 2348–2364.

(40) Hellman, A.; Pala, R. G. S. First-Principles Study of Photoinduced Water-Splitting on Fe₂O₃. *J. Phys. Chem. C* **2011**, *115*, 12901–12907.

(41) von Rudorff, G. F.; Jakobsen, R.; Rosso, K. M.; Blumberger, J. Hematite(001)-liquid water interface from hybrid density functional-based molecular dynamics. *J. Phys.: Condens. Matter* **2016**, *28*, 394001.

(42) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion

correction (DFT-D) for the 94 elements H-Pu. *J. Chem. Phys.* 2010, 132, 154104.

(43) von Rudorff, G. F.; Jakobsen, R.; Rosso, K. M.; Blumberger, J. Fast Interconversion of Hydrogen Bonding at the Hematite (001)−Liquid Water Interface. *J. Phys. Chem. Lett.* 2016, 7, 1155−1160.

(44) McBriarty, M. E.; von Rudorff, G. F.; Stubbs, J. E.; Eng, P. J.; Blumberger, J.; Rosso, K. M. Dynamic Stabilization of Metal Oxide−Water Interfaces. *J. Am. Chem. Soc.* 2017, 139, 2581−2584.

(45) Cicero, G.; Grossman, J. C.; Schwegler, E.; Gygi, F.; Galli, G. Water Confined in Nanotubes and between Graphene Sheets: A First Principle Study. *J. Am. Chem. Soc.* 2008, 130, 1871−1878.

(46) Atambo, M. O.; Varsano, D.; Ferretti, A.; Ataei, S. S.; Caldas, M. J.; Molinari, E.; Selloni, A. Electronic and optical properties of doped TiO₂ by many-body perturbation theory. *Phys. Rev. Mater.* 2019, 3, 045401.

(47) Gerosa, M.; Gygi, F.; Govoni, M.; Galli, G. The role of defects and excess surface charges at finite temperature for optimizing oxide photoabsorbers. *Nat. Mater.* 2018, 17, 1122−1127.

(48) Liao, P.; Carter, E. A. Hole transport in pure and doped hematite. *J. Appl. Phys.* 2012, 112, 013701.

(49) Guo, Z.; Ambrosio, F.; Chen, W.; Gono, P.; Pasquarello, A. Alignment of Redox Levels at Semiconductor−Water Interfaces. *Chem. Mater.* 2018, 30, 94−111.

(50) Hörmann, N. G.; Guo, Z.; Ambrosio, F.; Andreussi, O.; Pasquarello, A.; Marzari, N. Absolute band alignment at semiconductor-water interfaces using explicit and implicit descriptions for liquid water. *npj Computational Materials* 2019, 5, 100.

(51) Tamirat, A. G.; Rick, J.; Dubale, A. A.; Su, W.-N.; Hwang, B.-J. Using hematite for photoelectrochemical water splitting: a review of current progress and challenges. *Nanoscale Horizons* 2016, 1, 243−267.

(52) Deák, P.; Aradi, B.; Frauenheim, T. Polaronic effects in TiO₂ calculated by the HSE06 hybrid functional: Dopant passivation by carrier self-trapping. *Phys. Rev. B* 2011, 83, 155207.

(53) Balasubramanian, M.; Melendres, C.; Mini, S. X-ray absorption spectroscopy studies of the local atomic and electronic structure of iron incorporated into electrodeposited hydrous nickel oxide films. *J. Phys. Chem. B* 2000, 104, 4300−4306.

(54) McBriarty, M. E.; von Rudorff, G. F.; Stubbs, J. E.; Eng, P. J.; Blumberger, J.; Rosso, K. M. Dynamic Stabilization of Metal Oxide−Water Interfaces. *J. Am. Chem. Soc.* 2017, 139, 2581−2584.

(55) Jakub, Z.; Meier, M.; Kraushofer, F.; Balajka, J.; Pavelec, J.; Schmid, M.; Franchini, C.; Diebold, U.; Parkinson, G. S. Rapid oxygen exchange between hematite and water vapor. *Nat. Commun.* 2021, 12, 6488.

### Recommended by ACS

**Insights into Photoinduced Carrier Dynamics and Overall Water Splitting of Z-Scheme van der Waals Heterostructures with Intrinsic Electric Polarization**
Juan Wang, Mingwen Zhao, *et al.*
JANUARY 18, 2023
THE JOURNAL OF PHYSICAL CHEMISTRY LETTERS
READ ➔

**Competitive Photo-Oxidation of Water and Hole Scavengers on Hematite Photoanodes: Photoelectrochemical and Operando Raman Spectroelectrochemistry Study**
Vivek Ramakrishnan, Iris Visoly-Fisher, *et al.*
DECEMBER 22, 2022
ACS CATALYSIS
READ ➔

**Modulating WO₃ Crystal Orientation to Suppress Hydroxyl Radicals for Sustainable Solar Water Oxidation**
Xiaobing Shi, Chunhua Cui, *et al.*
JANUARY 10, 2023
ACS CATALYSIS
READ ➔

**Elucidating the Role of Surface Energetics on Charge Separation during Photoelectrochemical Water Splitting**
Zhenhua Pan, Kenji Katayama, *et al.*
NOVEMBER 16, 2022
ACS CATALYSIS
READ ➔

Get More Suggestions >

---

5306
https://doi.org/10.1021/acscatal.3c00357
*ACS Catal.* 2023, 13, 5298−5306