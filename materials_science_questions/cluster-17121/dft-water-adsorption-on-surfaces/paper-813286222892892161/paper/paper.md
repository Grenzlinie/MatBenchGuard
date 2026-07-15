# The Role of Water in the Adsorption of Oxygenated Aromatics on Pt and Pd

Jin Yang,${}^{[a]}$ Paul J. Dauenhauer,$^{[a]}$ and Ashwin Ramasubramaniam${}^{[b]}$

Catalytic processing of biomass-derived oxygenates to valuable chemical products will contribute to a sustainable future. To provide insight into the conversion of processed sugars and lignin monomers, we present density functional theory studies of adsorption of phloroglucinol, a potentially valuable biomass derivative, on Pt(111) and Pd(111) surfaces. A comprehensive study of adsorption geometries and associated energies indicates that the bridge site is the most preferred adsorption site for phloroglucinol, with binding energies in the range of 2–3 eV in the vapor phase. Adsorption of phloroglucinol on these metal surfaces occurs via hybridization between the carbon p$_z$ orbitals and the metal d$_{z^2}$ and d$_{yz}$ orbitals. With explicit solvent, hydrogen bonds are formed between phloroglucinol and water molecules thereby decreasing binding of phloroglucinol to the metal surfaces relative to the vapor phase by 20–25%. Based on these results, we conclude that solvent effects can significantly impact adsorption of oxygenated aromatic compounds derived from biomass and influence catalytic hydrogenation and hydrodeoxygenation reactions as well. © 2012 Wiley Periodicals, Inc.

DOI: 10.1002/jcc.23107

## Introduction

The production of renewable fuels and chemicals from bio- mass has been identified as one of the major research chal- lenges of the 21st century.$^{[1,2]}$ One prospect for production of renewable chemicals involves chemical and/or thermal decom- position of biomass-derives macromolecules, such as lignin to monomers (6–15 mass%).$^{[3]}$ These monomers are typically oxy genated aromatic compounds, including phenols, benzene- diols, guaiacols and syringols.$^{[3,4]}$ Further hydrogenation of these high-oxygen content aromatics (up to 60 weight %)$^{[5]}$ is required to reduce their high reactivity and viscosity$^{[5–7]}$ to enable their use in conventional gasoline or diesel engines.

An alternative process to obtain commercially valuable chemicals involves hybrid processing of sugars, which com- bines both enzymatic and inorganic catalysts for optimal pro- cess efficiency. In this strategy, enzymatic catalysts convert sugars to bridge molecules, which are sufficiently reduced to be further processed using thermochemical catalysts such as noble metals. By combining the high selectivity of enzymes$^{[8]}$ with the high turnover frequencies of thermochemical cata- lysts,$^{[9]}$ it may be possible to develop new processes for biore- newable chemicals. One such process, outlined schematically in Figure 1, proposes the enzymatic conversion of glucose to the bridge molecule, *myo*-inositol,$^{[10]}$ which can subsequently be dehydrated to oxygenated aromatic chemicals such as phloroglucinol (1,3,5-trihydroxy-benzene).$^{[11]}$ The potential for producing higher value oxygenated aromatics, such as phenol or resorcinol, will then depend upon further reduction chemistry.

Either approach described above requires chemical technol- ogy for the elimination of oxygenated species since biomass is inherently oxygen rich.$^{[12]}$ Noble metal catalysts have been widely studied for the hydrogenation of $C—C$, $C=C$, $C—O^{[8,9,13,14]}$ bonds as well as aromatic molecules.$^{[1]}$ These cat- alysts demonstrate capability for hydrogenation of both aro- matic carbon–carbon bonds$^{[15–17]}$ and $C=O$ bonds.$^{[18–20]}$ Cata- lytic activity for hydrogenation of aromatic rings has been reported to be in the order of Pt $>$ Ni $>$ Pd.$^{[21,22]}$ Pt and Ni are capable of complete hydrogenation of aromatic $C=C$ and $C=O$ bonds to cyclohexanol.$^{[23,24]}$ Meanwhile, Pd exhibits tun- ability for hydrogenating carbonyl groups based on its prepa- ration techniques and selected support. Monometallic sup- ported Pd catalysts are reported to convert phenol to cyclohexanol,$^{[25,26]}$ while Pd/acid-supports have been shown to hydrogenate phenol to cyclohexanone.$^{[27]}$ There have not been any studies of hydrogenation of phloroglucinol on these metal surfaces, to the best of our knowledge.

At a fundamental level, the adsorption of aromatic mole- cules on noble metal surfaces has been studied extensively both theoretically and experimentally. For example, scanning tunneling microscopy has been used to examine structures of benzene molecules adsorbed on $Cu,^{[28,29]}$ Pt,$^{[18]}$ Pd,$^{[18]}$ and Rh.$^{[30]}$ In particular, a range of experimental techniques$^{[31–36]}$ and theoretical calculations have been used to understand the

---

[a] J. Yang, P. J. Dauenhauer
Department of Chemical Engineering, University of Massachusetts Amherst,
Amherst, Massachusetts, 01003
Fax: (+1)413 545 2819
E-mail: dauenhauer@ecs.umass.edu

[b] A. Ramasubramaniam
Department of Mechanical and Industrial Engineering, University of
Massachusetts Amherst, Amherst, Massachusetts 01003
E-mail: ashwin@engin.umass.edu

Contract grant sponsor: 3M Corporation Nontenured Faculty Award
Contract grant sponsor: National Science Foundation grant number
TG-CHE100112 [Extreme Science and Engineering Discovery
Environment (XSEDE)].

© 2012 Wiley Periodicals, Inc.

$$
\ce{
HO-C1(OH)C(OH)(H)C(O)C(OH)(H)C1(OH)
->[Enzymatic]
HO-C1(OH)C(OH)(H)C(OH)C(OH)(H)C1(OH)
->[-3H2O, [H+]]
HO-C1=CC(O)=CC(O)=C1
->[+2H2, -2H2O, Metal,[H+]]
C1=CC=CC=C1
}
$$
[1] [2] [3] [4]

Figure 1. Proposed reaction scheme for hybrid production of aromatic products from glucose. Initial conversion of D-Glucose $^{[1]}$ to the bridge-molecule myo-inositol $^{[2]}$ occurs through enzymatically driven cyclization to a six-carbon polyol ring. Myo-inositol will then be converted by catalyzed dehydration to 1,3,5-trihydroxy-benzene $^{[3]}$. Similar dehydration catalytic chemistry will occur to form phenol $^{[4]}$.

adsorption$^{[37-40]}$ and dehydrogenation$^{[41,42]}$ of benzene on Pt(111). Similarly, adsorption and hydrogenation studies have also been undertaken for oxygenated aromatics such as phenol$^{[43-46]}$ on Ni and Pd surfaces. In general, these studies of benzene and phenol adsorption and (de)hydrogenation on noble metal catalysts leads us to expect that these metals might also serve as efficient catalysts for partial and/or complete hydrogenation of phloroglucinol to a variety of useful aromatic products.

In this work, we address the role of water on the energetic and structural aspects of phloroglucinol adsorption on Pt(111) and Pd(111) surfaces with density functional theory (DFT) calculations; studies of reaction mechanisms and kinetics are deferred to future work. Although benzene and phenol are fairly volatile, making vapor-phase adsorption studies both experimentally feasible and relevant, phloroglucinol and many biomass-derived oxygenates are less easy to volatilize and must be subjected to aqueous-phase chemistry instead. Thus, while vapor-phase calculations can provide important insights into the geometry and bonding between adsorbed phloroglucinol molecules and the metal surface, the solvent phase must eventually be considered to obtain better insight into experiments. Previous DFT work$^{[47]}$ has examined the interaction between phloroglucinol and water molecules and shown that both oxygen and hydrogen atoms from phloroglucinol can form H-bonds with their surrounding water molecules; typically a solvated phloroglucinol molecule can form H-bonds with one to three water molecules at the same time.$^{[47]}$ However, there are no studies to date that investigate the more complicated problem of adsorption of phloroglucinol molecules on catalyst surfaces either with or without solvent. Additionally, recent work by Bhushan et al.$^{[48]}$ shows that water molecules can increase the selective oxidation of alcohols over Au(111) and Pt(111) surfaces. It would then appear that solvent effects could also play a critical role in the aqueous phase hydrogenation of phloroglucinol. For the moment, we restrict attention to the role of solvent effects on the adsorption energetics and site preference of phloroglucinol on Pt(111) and Pd(111); to the best of our knowledge, this work is the first to address these specific issues for phloroglucinol.

## Computational Methods

In this work, DFT is used to simulate the interaction of a phloroglucinol molecule with Pt(111) and Pd(111) surfaces both in the vapor and aqueous-phase. As, phloroglucinol is an aromatic molecule and the metals considered here are also open d-shell metals, van der Waals interactions are expected to be less important, making DFT a reliable and efficient calculation tool for our purposes. All calculations were performed with the Vienna Ab Initio Simulation Package (VASP).$^{[49]}$ Electron exchange and correlation was described with the Perdew-Wang-91$^{[50]}$ form of the Generalized Gradient Approximation. Based on systematic convergence tests, a kinetic energy cutoff of 400 eV was used, for plane-waves and a $5 × 5 × 1$ Monkhorst-Pack mesh$^{[51]}$ was used to discretize the Brillouin zone. A Gaussian smearing of 400 eV was used for Brillouin zone integration. Dipole corrections were applied in the direction normal to the slab to correct for long-range interactions between surface dipoles.$^{[52]}$ The bulk metal was represented by a four-layer slab separated by $10$ Å of vacuum in the direction normal to the slab to prevent spurious interactions between periodic images of the slab. To minimize electronic interactions between periodic images of phloroglucinol molecules adsorbed on the slab surface, a $4 × 4$ surface slab was chosen from adsorption energy convergence studies. Finally, to simulate the constraint arising from the bulk metal, only the three uppermost layers of the Pt slab and two uppermost layers of the Pd slab were allowed to relax during the adsorption process, which is sufficient to ensure that atoms in relaxed layers experience forces lesser than $0.01$ eV/Å while atoms in the layer immediately below the relaxed layers experience forces lesser than $0.1$ eV/Å. A force convergence of $0.01$ eV/Å was used in all subsequent structural relaxation calculations.

The adsorption energy of phloroglucinol on metal (111) surfaces in the vapor-phase is defined as
$$
E_{\text{ad,vac}} = E_{\text{slab+molecule}} - E_{\text{molecule}} - E_{\text{slab}}, \tag{1}
$$
where $E_{\text{ad,vac}}$ represents the adsorption energy, $E_{\text{slab+molecule}}$ is the total energy after phloroglucinol is adsorbed on the metal surface, $E_{\text{slab}}$ is the total energy of the slab, and $E_{\text{molecule}}$ is the energy of an isolated phloroglucinol molecule. As defined, a more negative adsorption energy signifies stronger binding between the molecule and the metal surface.

For the aqueous-phase calculations, the calculation procedures were slightly modified. As the interaction of water molecules with the phloroglucinol molecule as well as the metal surface is essentially stochastic, molecular dynamics (MD) simulations within the canonical (NVT) ensemble accompanied by statistical sampling is used to simulate the solvent interaction. Water molecules were introduced randomly at a density of $0.86$ g/cm$^{3}$ $^{[53,54]}$ in the vacuum region separating periodic images of the slab. To minimize the effects of surface dipoles, phloroglucinol molecules were introduced symmetrically on

both sides of the slab. Both surface layers of the four-layer slab were allowed to relax while holding the inner two layers fixed to mimic the bulk constraint. Because of the large number of atoms in the aqueous phase calculations, the kinetic energy cutoff was decreased to 250 eV. This does not lead to any substantive loss of accuracy (~20 meV differences in adsorption energies). The entire system was thermalized at 300 K and quenched over 700 fs to 0 K. The final energy at the end of the MD trajectory gives us the total energy of the system including interactions between all three phases (water, metal, and adsorbate). To generate a consistent reference state, the two phloroglucinol molecules were detached from the metal surfaces and brought toward the center of the water phase. An NVT MD quench from 300 K was again run and a final energy at 0 K obtained. The adsorption energy of phloroglucinol is then obtained as the difference between these two energies. The MD procedure can in principle be used to obtain adsorption enthalpies at any finite temperature, but the system is quenched to 0 K here to make direct comparison with the 0 K structural relaxation calculations.

## Results and Discussion

In comparison to benzene or phenol, the adsorption of phloroglucinol, which has three OH functional groups, is fairly complex. Figure 2 displays several possible adsorbed configurations of phloroglucinol on the (111) surface of an fcc metal. First, there are four possible adsorption sites on the (111) surface, namely, the atop site, bridge site, hcp hollow site, and fcc hollow site. $^{[31]}$ Second, at each of these sites, the aromatic ring can be oriented with C—C bonds either parallel (indicated by B in Fig. 2) or perpendicular (indicated by A in Fig. 2) to the horizontal in Figure 2. Third, the OH bond can be located either on a hollow (indicated by 1 in Fig. 2) or an atop (indicated by 2 in Fig. 2) site. Finally, there are two possible configurational isomers of phloroglucinol derived from the relative orientations of the OH groups (indicated by I and II in Fig. 2). Accounting for all the permutations, 20 different adsorbed configurations of the phloroglucinol on the metal surface are considered. Note that in the configurations discussed here the adsorbed molecule is parallel to the metal surface; tilted adsorption structures were found to be higher in energy and were eliminated from further consideration.

![](./images/813286222892892161_1.jpg)

Figure 2. Considered adsorption configurations of phloroglucinol. [Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com]

### Vapor-phase adsorption of phloroglucinol on Pt(111) and Pd(111)

Structural relaxations were performed in VASP for all 20 adsorption permutations on each metal surface. Of the 20 candidates, only seven per metal surface were found to be stably adsorbed (with negative adsorption energy) and are listed in Table 1. As seen from Table 1, the most stable adsorption configuration on Pt(111) is the II-Bri-A1 configuration (refer to Fig. 2) with an adsorption energy of $-2.91$ eV. On Pd(111), the most stable adsorption configuration is the II-Bri-A2 configuration (refer to Fig. 2) with an adsorption energy of $-2.73$ eV. Thus, the bridge site is the strongest adsorption site for both metal surfaces. Among the remaining sites, the fcc hollow sites are energetically preferred over the hcp hollow sites. The overall stability order also suggests that, at a given adsorption sites (fcc or hcp), configurational isomer II is the more strongly adsorbed than isomer I. In addition, the A type orientation of carbon ring is preferable for bridge sites and B type is preferable for hollow sites. Overall, the adsorption energies for all the secondary adsorption sites are in the range of $-2.4$ to $-2.6$ eV, indicating that the adsorption process is strongly thermodynamically favorable.

<table>
<caption>Table 1. Adsorption energy of phloroglucinol on Pt(111) and Pd(111).</caption>
<thead>
<tr>
<th rowspan="2">Configurations</th>
<th colspan="2">$E_{ad,vac}$ (eV)</th>
</tr>
<tr>
<th>Pt(111)</th>
<th>Pd(111)</th>
</tr>
</thead>
<tbody>
<tr>
<td>II-Bri-A1</td>
<td>−2.91</td>
<td>−</td>
</tr>
<tr>
<td>II-Bri-A2</td>
<td>−</td>
<td>−2.73</td>
</tr>
<tr>
<td>I-Bri-A2</td>
<td>−2.78</td>
<td>−2.58</td>
</tr>
<tr>
<td>II-Fcc-B1</td>
<td>−2.71</td>
<td>−2.63</td>
</tr>
<tr>
<td>II-Hcp-B1</td>
<td>−2.67</td>
<td>−2.59</td>
</tr>
<tr>
<td>I-Fcc-B1</td>
<td>−2.55</td>
<td>−2.53</td>
</tr>
<tr>
<td>I-Hcp-B1</td>
<td>−2.55</td>
<td>−2.45</td>
</tr>
<tr>
<td>I-Fcc-A2</td>
<td>−2.48</td>
<td>−</td>
</tr>
<tr>
<td>I-Hcp-A2</td>
<td>−</td>
<td>−2.43</td>
</tr>
</tbody>
</table>

### Geometry and electronic structure of adsorbed phloroglucinol molecules

To better understand the adsorption of phloroglucinol on metal surfaces, various structural properties for most strongly adsorbed configuration were examined. The structural details are reported in Table 2; the corresponding structural parameters are illustrated in Figure 3b.

Figure 3a displays a side view of the adsorbed molecule on the metal surface. The average adsorption height on Pt(111) and Pd(111) is 2.16 and 2.15 Å, respectively. The aromatic ring is slightly distorted, with the leftmost and rightmost C atoms of the ring [atoms C1 and C4 in Fig. 3b] being closer than the average height by 0.09 and 0.1 Å on Pt(111) and Pd(111), respectively. Correspondingly, the two metal atoms M1 in

<table>
<caption>Table 2. Structural properties of phloroglucinol adsorbed at surface bridge site.</caption>
<thead>
<tr>
<th rowspan="2">Variables</th>
<th colspan="2">Gas Phase</th>
<th colspan="4">Aqueous phase</th>
</tr>
<tr>
<th>Pt</th>
<th>Pd</th>
<th colspan="2">Adsorbed Pt</th>
<th colspan="2">Adsorbed Pd</th>
</tr>
<tr>
<th></th>
<th></th>
<th>0 K</th>
<th>300 K</th>
<th>0 K</th>
<th>300 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>$d_{zmin}$ (Å)</td>
<td>1.94</td>
<td>1.97</td>
<td>1.85</td>
<td>$1.94 \pm 0.05$</td>
<td>1.88</td>
<td>$1.90 \pm 0.02$</td>
</tr>
<tr>
<td>$d_{zavg}$ (Å)</td>
<td>2.16</td>
<td>2.15</td>
<td>2.08</td>
<td>$2.11 \pm 0.07$</td>
<td>2.06</td>
<td>$2.06 \pm 0.02$</td>
</tr>
<tr>
<td>$r_{C1}$ (Å)</td>
<td>1.49</td>
<td>1.46</td>
<td>1.50</td>
<td>$1.47 \pm 0.02$</td>
<td>1.47</td>
<td>$1.46 \pm 0.03$</td>
</tr>
<tr>
<td>$r_{C2}$ (Å)</td>
<td>1.44</td>
<td>1.44</td>
<td>1.44</td>
<td>$1.44 \pm 0.03$</td>
<td>1.43</td>
<td>$1.44 \pm 0.02$</td>
</tr>
<tr>
<td>$r_{M1}$ (Å)</td>
<td>2.86</td>
<td>2.80</td>
<td>2.84</td>
<td>$2.81 \pm 0.01$</td>
<td>2.80</td>
<td>$2.79 \pm 0.01$</td>
</tr>
<tr>
<td>$r_{M2}$ (Å)</td>
<td>3.10</td>
<td>2.96</td>
<td>3.03</td>
<td>$2.89 \pm 0.01$</td>
<td>2.97</td>
<td>$2.99 \pm 0.02$</td>
</tr>
<tr>
<td>$r_{CM1}$ (Å)</td>
<td>2.16</td>
<td>2.17</td>
<td>2.12</td>
<td>$2.25 \pm 0.08$</td>
<td>2.13</td>
<td>$2.14 \pm 0.01$</td>
</tr>
<tr>
<td>$r_{CM2}$ (Å)</td>
<td>2.16</td>
<td>2.20</td>
<td>2.16</td>
<td>$2.25 \pm 0.08$</td>
<td>2.15</td>
<td>$2.13 \pm 0.02$</td>
</tr>
<tr>
<td>$r_{CM3}$ (Å)</td>
<td>2.30</td>
<td>2.24</td>
<td>2.30</td>
<td>$2.32 \pm 0.07$</td>
<td>2.22</td>
<td>$2.20 \pm 0.08$</td>
</tr>
<tr>
<td>$	heta 1$ (°)</td>
<td>113.9</td>
<td>115.4</td>
<td>119.4</td>
<td>$120 \pm 3$</td>
<td>121</td>
<td>$118.5 \pm 0.5$</td>
</tr>
<tr>
<td>$	heta 2$ (°)</td>
<td>122.5</td>
<td>122.5</td>
<td>120.3</td>
<td>$123 \pm 3$</td>
<td>120</td>
<td>$120 \pm 0.5$</td>
</tr>
<tr>
<td>$\alpha$ (°)</td>
<td>104.4</td>
<td>95.8</td>
<td>111.9</td>
<td>$95 \pm 3$</td>
<td>99.3</td>
<td>$101 \pm 2$</td>
</tr>
<tr>
<td>$\beta$ (°)</td>
<td>108.7</td>
<td>102.3</td>
<td>111.2</td>
<td>$97 \pm 10$</td>
<td>97.3</td>
<td>$99 \pm 3$</td>
</tr>
<tr>
<td>$\gamma$ (°)</td>
<td>55–56</td>
<td>55–63</td>
<td>3–44</td>
<td>10–70</td>
<td>39–75</td>
<td>107–167</td>
</tr>
<tr>
<td colspan="7">All parameters are illustrated in Figure 3 with the exception of $\gamma$, which is the dihedral angle formed by the plane containing C1, its connected O atom, and C4, with the plane containing C1 and its connected OH group.</td>
</tr>
</tbody>
</table>

Figure 3b are slightly moved out of the surface plane by 0.13 and 0.12 Å for Pt(111) and Pd(111), respectively. A significant out of plane buckling of the OH group and the H atoms of phloroglucinol away from the metal surface is observed. All of these facts collectively point to strong interaction between phloroglucinol and the metal surface, with possible changes in the hybridization states of the C atoms. To confirm this, a more detailed structural analysis of the adsorbed molecule is performed next.

In vacuum, the isolated phloroglucinol molecule has a C—C bond length of 1.40 Å, which is essentially identical to the experimentally reported value of 139.15 pm for benzene.[⁴⁰] However, upon adsorption on Pt or Pd, there are significant changes in these bond lengths. As seen from Figure 3b, the aromatic ring symmetrically straddles the bridge site (formed by metal atoms M2); the bonds between the C atoms that are perpendicular to the bridge are stretched from 1.40 to 1.44 Å ($r_{C2}$) on both Pt(111) and Pd(111) surfaces. The bonds between the C atoms furthest from the bridge (C1 and C4) with their neighboring C atoms is stretched from 1.40 to 1.49 Å and 1.46 Å ($r_{C1}$) on Pt(111) and Pd(111) surfaces, respectively. Correspondingly, there are strong structural distortions of the metal surface in the vicinity of the adsorbed molecule as well. In particular, the distance between the metal atoms forming the bridge (M2) is modified upon adsorption of the phloroglucinol molecule from 2.81 Å to 3.10 Å for Pt(111) and from 2.79 to 2.96 Å for Pd(111). The metal-C—H ($\alpha$) and metal-C—O ($\beta$) angles were also measured: for adsorption on Pt(111), both $\alpha$ (104.4°) and $\beta$ (108.7°) angle are closer to the tetrahedral angle of sp³ carbon (109°), especially the $\beta$ angle. Similar results are found for adsorbed phloroglucinol on Pd(111) surface, although the angles ($\alpha = 95.8^\circ$ and $\beta = 102.3^\circ$) are smaller than those of adsorbed phloroglucinol on Pt(111).

Overall, these results also suggest that the aromatic ring carbons are closer to being sp³ hybridized upon adsorption.

To further analyze the bonding between the phloroglucinol C atoms and the metal surface, we performed a detailed analysis of the partial density of states (PDOS), partial charge densities, and charge density differences, which are all displayed in Figure 4. For brevity, we only focus on Pt(111) here. In Figure 4a, the summed PDOS of the d$_{z^2}$ and d$_{yz}$ orbitals of the four Pt atoms that are involved in bond formation with the C atoms, as well as the summed PDOS of the p$_z$ orbitals of these C atoms are displayed. From symmetry considerations, the other Pt d-orbitals are unimportant for bonding with the C atoms. Comparable density of states from the Pt d$_z$2 and d$_{yz}$ orbitals as well as the C p$_z$ orbitals within a range of –6.5 to –6 eV below the Fermi level are observed. To confirm that this is indicative of bonding, we display the partial charge density (i.e., charge density arising from all wavefunctions) within this energy window is displayed in Figure 4b—as evident, some of the charge density arising from wavefunctions within this energy window is indeed localized between the Pt and C atoms. However another confirmation of the strong interaction between the adsorbed phloroglucinol molecule comes from the charge density difference plots in Figure 4c, which indicate the relative redistribution of electron charge within the composite structure (adsorbed molecule + metal slab) relative to the reference states (isolated slab/molecule).† As seen qualitatively from this figure, there is a significant redistribution of charge within the molecule; a Bader analysis[⁵⁵,⁵⁶] indicates a net charge transfer of 0.17 electrons from the metal to phloroglucinol. The overall results for the Pd(111)-phloroglucinol system are qualitatively similar. Bonding between the Pd and C atoms is most clearly observable in a window of –5.8 to –5.3 eV below the Fermi level. There is much smaller net transfer of electrons (~0.05 e) from Pd to phloroglucinol.

Although there are no direct experimental measurements of phloroglucinol adsorption to compare our results with, the above observations are generally in qualitative agreement with previous studies of benzene adsorption on Pt(111).[⁵⁷⁻⁶¹] Specifically, those studies show that, at a low coverage, the benzene molecule is absorbed in a parallel or near-parallel geometry on the Pt(111) surface[⁵⁷⁻⁶¹] with an adsorption energy of ~1.1 eV[³⁷] and an adsorption height of ~2.1 Å.[⁵⁷]

## Adsorption of phloroglucinol in water solution on Pt(111) and Pd(111)

Having presented a detailed analysis of gas-phase adsorption of phloroglucinol on Pt(111) and Pd(111), we now turn our attention to the role of the solvent (water) in modifying the interaction between phloroglucinol and the metal surface. As noted before, this is of importance since phloroglucinol and many biomass-derived oxygenates are difficult to volatilize and

†To produce a charge density difference plot, the molecule and the slab are sequentially eliminated from the relaxed composite structure (molecule + slab) and the charge density calculated with the atoms frozen in their distorted, adsorbed configuration.

![](./images/813286222892892161_2.jpg)

Figure 3. Geometric properties of adsorbed phloroglucinol. (a) A side view of adsorbed phloroglucinol. The minimum (d<sub>zmin</sub>) and average (d<sub>zavg</sub>) distance for the adsorption of phloroglucinol on the top layer of a metal surface is indicated. (b) Illustration of structural variables tabulated in Table 2. [Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.]

must instead be subjected to solution (aqueous) processing. The details of the simulation procedure have been discussed in Computational Methods section. As the aqueous phase cal- culations are computationally demanding, we only restrict attention to adsorption of phloroglucinol molecules in the lowest energy configuration found in the gas-phase calcula- tions (II-Bri-A1 for Pt and II-Bri-A2 for Pd). Over the course of our finite temperature MD simulations at 300 K (as well as tests at elevated temperatures up to 500 K), we did not find any propensity for thermal excitations to switch the adsorption configuration to a different lower-energy one. Therefore, while not exhaustive, our aqueous phase calculations are certainly representative of the solvent effect on the adsorp- tion of phloroglucinol on the selected metal surfaces.

Table 3 displays the adsorp- tion energy for phloroglucinol on Pt(111) and Pd(111) in the presence of water. In compari- son to gas-phase adsorption energies of $-2.91$ and $-2.73$ eV for Pt(111) and Pd(111) surfaces, respectively, the adsorption energies are, now $-2.22$ and $-2.12$ eV, respectively. This indicates a significant decrease in binding (20-25%) between the adsorbate and the metal surface. Note that this is not a finite temperature effect as the system was quenched to 0 K before computing adsorp- tion energies. Since phloroglucinol has three OH groups, H- bonds are readily formed between phloroglucinol and water molecules (Fig. 5); this has already been reported before for solvated phloroglucinol molecules. $^{[47]}$ Thus, the formation of H-bonds between phloroglucinol and water reduces the strength of the bonding between phloroglucinol and the metal surface, leading to a lower binding energy (less negative

![](./images/813286222892892161_3.jpg)

Figure 4. Detailed electronic structure of adsorbed phloroglucinol (II-Bri- A1) on Pt(111) surface. (a) PDOS for Pt atoms involved in bond formation with phloroglucinol. (b) Partial charge density from states within a window of -6.5 to -6 eV [indicated by black vertical lines in (a)] showing evidenceof bonding between the Pt and C atoms (isosurfaces are plotted at 0.050 e/Å³). (c) Charge density difference plot for phloroglucinol adsorbed on Pt(111) (isosurfaces are plotted at 0.037 e/Å³).

<table><caption>Table 3. Adsorption energies of phloroglucinol in the presence of water.</caption>
<thead>
<tr>
<th rowspan="2">Temperature (K)</th>
<th colspan="2">$E_{ad,aquo}$ (eV)</th>
</tr>
<tr>
<th>Pt(111)</th>
<th>Pd(111)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>$-2.22$</td>
<td>$-2.12$</td>
</tr>
<tr>
<td>300</td>
<td>$-1.67$</td>
<td>$-1.68$</td>
</tr>
</tbody>
</table>

![](./images/813286222892892161_4.jpg)

Figure 5. Snapshot of adsorbed phloroglucinol molecules in water (quenched to 0 K) with a closer view of the molecules adsorbed on the upper and lower slab faces. Dotted lines indicate hydrogen bonds.

$E_{ad,aquo}$). The magnitude of the adsorption energies are nevertheless large enough to preclude easy desorption of the adsorbate from the metal surface *in aquo*. Upon inclusion of finite temperature effects (sampling at 300 K), we see from Table 3 that the binding energies further decrease by another 20–25% from the 0 K aqueous phase result. Nevertheless, the binding energies are still strong enough to preclude desorption of the absorbate molecule at typical processing temperatures (0–300 K).

We also examined the detailed structure of adsorbed phloroglucinol molecules at 0 and 300 K; the results are displayed in Table 2. These data are obtained by averaging over 20 instantaneous configurations, 30 fs apart, after the system achieves equilibrium. From the data, we see that the overall structural details of the molecule do not differ significantly from the gas-phase results. There are a few subtle differences though. First, the distance between the bridge metal atoms (M2) decreases to compensate for the decreased interaction with the phloroglucinol molecule. This decreased adsorbate–metal interaction also explains why the angles between C atoms become closer to $120^\circ$, like phloroglucinol in gas phase. Second, the most obvious structural changes are manifested in the orientations of the OH group, which rotate freely about the C—O bond as H-bonds are randomly formed and broken with mobile surrounding water molecules. Because of these random variations in orientation of OH groups, all the corresponding angular structural variables within phloroglucinol vary accordingly, resulting in a larger spread for the $\alpha$, $\beta$, and $\gamma$ angle.

Overall, we conclude that the solvent can play a significant role in decreasing the binding between a phloroglucinol molecule and the catalyst metal surface. The implications of this finding for hydrogenation kinetics remain to be explored. Also, the randomly fluctuating reorientation of OH groups could play a role in decreasing steric hindrance for direct reaction of H atoms with the aromatic ring. This issue also remains to be explored in future work.

## Conclusions
We performed DFT calculations to examine the adsorption of phloroglucinol on Pt(111) and Pd(111) in the gas-phase and aqueous-phase. We found that bridge sites on Pt(111) and Pd(111) surfaces are the most preferred adsorption sites, followed by fcc and hcp hollow sites; atop sites are never preferred for adsorption. From an analysis of the PDOS, a tendency for hybridization between C $p_z$ and metal $d_{z^2}$ and $d_{yz}$ orbitals deep within the valence band is found, indicating strong carbon-metal bond formation. This strong bonding between the adsorbed molecule and the metal surfaces is also reflected in significant structural distortions of the adsorbed phloroglucinol molecule relative to its isolated state. *Ab initio* MD calculations with water molecules as solvent reveal that the solvent decreases adsorption energies on Pt(111) and Pd(111) surfaces by about 25% relative to gas-phase adsorption. The cause for this decrease in binding to the metal surface is attributed to hydrogen bonds that are dynamically formed between the phloroglucinol molecules. Although the structural differences between an adsorbed phloroglucinol molecule in the vapor and aqueous phase are minor, an important effect of the solvent is to facilitate free rotation of the OH bond relative to the carbon ring as H-bonds are dynamically formed and broken with mobile solvent atoms. As the water/metal interface is a unique environment for surface reactions, it will be interesting to examine the role of the solvent in the sequential hydrogenation of phloroglucinol on Pt and Pd surfaces to produce valuable bio-renewable chemicals.

**Keywords:** surface chemistry · catalysis · density functional theory · green chemistry

How to cite this article: J. Yang, P. J. Dauenhauer, A. Ramasubramaniam, *J. Comput. Chem.* **2012**, 00, 000–000. DOI: 10.1002/jcc.23107

[1] C. Satterfield, Heterogeneous Catalysis in Industrial Practice, 2nd ed.; McGraw-Hill, New York, **1991**; p. 1.
[2] A. J. Ragauskas, C. K. Williams, B. H. Davison, G. Britovsek, J. Cairney, C. A. Eckert, W. J. Frederick Jr., J. P. Hallett, D. J. Leak, C. L. Liotta, J. R. Mielenz, R. Murphy, R. Templer, T. Tschaplinski, *Science* **2006**, 311, 484.
[3] M. Garcia-Perez, A. Chaala, H. Pakdel, D. Kretschmer, C. Roy, *Biomass Bioenergy* **2007**, 31, 222.
[4] J. P. Diebold, In Fast Pyrolysis of Biomass: A Handbook, Vol. 2; A. V. Bridgwater CPL Press: Newbury, UK, **2002**; p. 243.
[5] T. P. Vispute, H. Y. Zhang, A. Sanna, R. Xiao, G. W. Huber, *Science* **2010**, 330, 1222.
[6] A. Oasmaa, S. Czernik, *Energy Fuels* **1999**, 13, 914.
[7] M. M. Wright, D. E. Daugaard, J. A. Satrio, R. C. Brown, *Fuel* **2010**, 89, S2.
[8] S. Atsumi, T. Hanai, J. C. Liao, *Nature* **2008**, 451, 86.
[9] L. D. Schmidt, P. J. Dauenhauer, *Nature* **2007**, 447.
[10] K. Sanderson, *Nature* **2006**, 444, 673.
[11] L. Rocha, A. Marston, O. Potterat, M. A. C. Kaplan, K. Hostettmann, *Phytochemistry* **1996**, 42, 185.
[12] P. H. Raven, R. F. Evert, S. E. Eichhorn, Biology of Plants; W.H. Freeman and Company Publishers: New York, **2005**; p. 124.
[13] C. J. Kliewer, C. Aliaga, M. Bieri, W. Huang, C. K. Tsung, J. B. Wood, K. Komvopoulos, G. A. Somorjai, *J. Am. Chem. Soc.* **2010**, 132, 13088.
[14] J. C. Serrano-Ruiz, J. A. Dumesic, *Green Chem.* **2009**, 11, 1101.
[15] K. Tsai, I. Wang, T. Tsai, *Catal. Today* **2011**, 166, 73.
[16] F. Cardenas-Lizana, D. Lamey, S. Gomez-Quero, N. Perret, L. Kiwi-Minsker, M. A. Keane, *Catal. Today* **2011**, 173, 53.
[17] M. Reinhard, C. Schuth, *Appl. Catal. B Environ.* **1998**, 18, 215.
[18] F. Delbecq, P. Sautet, *J. Catal.* **1994**, 152, 217.
[19] P. Claus, *Top. Catal.* **1998**, 5, 51.
[20] M. Englisch, *J. Catal.* **1997**, 166, 25.
[21] G. Harold, *Ann. N. Y. Acad. Sci.* **1973**, 24, 233.
[22] H. Takagi, T. Isoda, K. Kusakabe, S. Morooka, *Energy Fuels* **1999**, 13, 1191.
[23] K. Amouzegar, O. Savadogo, *J. Appl. Electrochem.* **1997**, 27, 539.
[24] A. Martel, B. Mahdavi, L. Jean, B. Louis, H. Menard, *Can. J. Chem.* **1997**, 75, 1862.
[25] S. Scirè, M. Minicò, C. Crisafulli, *Appl. Catal. A Gen.* **2002**, 235, 21.
[26] H. Li, J. Liu, S. H. Xie, M. H. Qiao, W. L. Dai, Y. F. Lu, H. X. Li, *Adv. Funct. Mater.* **2008**, 18, 3235.
[27] K. V. R. Chary, D. Naresh, V. Vishwanathan, M. Sadakane, W. Ueda, *Catal. Commun.* **2007**, 8, 471.
[28] L. J. Lauhon, W. Ho, *J. Phys. Chem. A* **2000**, 104, 2463.
[29] P. S. Weiss, M. M. Kamna, T. M. Graham, S. J. Stranick, *Langmuir* **1998**, 14, 1284.
[30] D. N. Futaba, S. Chiang, *Jpn. J. Appl. Phys.* **1999**, 38(Part 1, No. 6B), 3809.
[31] M. Abon, J. C. Bertolini, J. Billy, J. Massardier, B. Tardy, *Surf. Sci.* **1985**, 162, 395.

[32] S. Lehwald, H. Ibach, J. E. Demuth, *Surf. Sci.* **1978**, *78*, 577.

[33] J. A. Horsley, J. Stöhr, A. P. Hitchcock, D. J. Newbury, A. L. Johnson, F. Sette, *J. Chem. Phys.* **1985**, *83*, 6099.

[34] F. Cemic, *Surf. Sci.* **1995**, *342*, 101.

[35] D. F. Ogletree, M. A. van Hove, G. A. Somorjai, *Surf. Sci.* **1987**, *183*, 1.

[36] A. Wander, G. Held, R. Q. Hwang, G. S. Blackman, M. L. Xu, P. Andres, M. A. van Hove, G. A. Somorjai, *Surf. Sci.* **1991**, *249*, 21.

[37] M. Saeys, M. F. Reyniers, M. Neurock, G. B. Marin, *J. Phys. Chem. B* **2002**, *106*, 7489.

[38] P. Sautet, M. Bocquet, *Phys. Rev. B. Condens. Matter* **1996**, *53*, 4910.

[39] P. Weiss, D. Eigler, *Phys. Rev. Lett.* **1993**, *71*, 3139.

[40] J. Gauss, J. F. Stanton, *J. Phys. Chem. A* **2002**, *104*, 2865.

[41] M. Saeys, M. F. Reyniers, M. Neurock, G. B. Marin, *J. Phys. Chem. B* **2005**, *109*, 2064.

[42] M. Saeys, M. F. Reyniers, M. Neurock, G. B. Marin, *J. Phys. Chem. B* **2003**, *107*, 3844.

[43] E. J. Shin, M. A. Keane, *Ind. Eng. Chem. Res.* **2000**, *39*, 883.

[44] E. Díaz, A. F. Mohedano, L. Calvo, M. A. Gilarranz, J. A. Casas, J. J. Rodríguez, *Chem. Eng. J.* **2007**, *131*, 65.

[45] H. Liu, T. Jiang, B. Han, S. Liang, Y. Zhou, *Science* **2009**, *326*, 12502.

[46] L. Delle Site, A. Alavi, C. F. Abrams, *Phys. Rev. B* **2003**, *67*, 1.

[47] L. Mammino, M. M. Kabanda, *J. Mol. Struct. (Theochem)* **2008**, *852*, 36.

[48] N. Z. Bhushan, D. D. Hibbitts, M. Neurock, R. J. Davis, *Science* **2010**, *330*, 74.

[49] G. Kresse, J. Hafner, *Phys. Rev. B* **1993**, *47*, 558.

[50] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, C. Fiolhais, *Phys. Rev. B* **1992**, *46*, 6671.

[51] H. J. Monkhorst, J. D. Pack, *Phys. Rev. B* **1976**, *13*, 5188.

[52] J. Neuegebauer, M. Scheffler, *Phys. Rev. B* **1992**, *46*, 16067.

[53] C. D. Taylor, S. A. Wasileski, J. Filhol, M. Neurock, *Phys. Rev. B*, **2006**, *73*, 165402.

[54] D. R. Lide, *CRC Handbook of Chemistry and Physics*; CRC Press: Boca Raton, FL, **1992**.

[55] R. Bader, *Atoms in Moleculaes: A quantum Theory*; Oxford University Press: New York, **1990**.

[56] G. Henkelman, A. Arnaldsson, H. Jónsson, *Comput. Mater. Sci.* **2006**, *36*, 354.

[57] D. G. Ogletree, M. A. Van Hove, G. A. Somorjai, *Surf. Sci.* **1987**, *183*, 1.

[58] J. L. Gland, G. A. Somorjai, *Surf. Sci.* **1973**, *38*, 157.

[59] A. Dedieu, *Chem. Rev.* **2000**, *100*, 543.

[60] M. Abon, J. Billy, J. C. Bertolini, B. Tardy, *Surf. Sci.* **1986**, *167*, L187.

[61] J. Somers, M. E. Ridge, D. R. Lloyd, T. McCabe, *Surf. Sci.* **1987**, *181*, L167.

Received: 22 June 2012
Accepted: 26 June 2012
Published online on

---

*Journal of Computational Chemistry* **2012**, *00*, 000–000  7