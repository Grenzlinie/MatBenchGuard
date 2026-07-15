# Journal of Materials Chemistry A

## Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: S. Li, Z. Peng, J. Zheng and F. Pan, *J. Mater. Chem. A*, 2017, DOI: 10.1039/C7TA00698E.

![](./images/811048468343685120_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the [author guidelines](https://pubs.rsc.org/en/journals/author-guidelines?journalcode=mata).

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions](https://pubs.rsc.org/en/journals/terms-and-conditions) and the ethical guidelines, outlined in our [author and reviewer resource centre](https://pubs.rsc.org/en/journals/author-and-reviewer-resources?journalcode=mata), still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/811048468343685120_2.jpg)

rsc.li/materials-a

# Optimizing CdTe-Metal Interfaces for high performance Solar Cells
Sibai Li, $^{a}$ Zhi Peng, $^{a}$ Jiaxin Zheng $^{a}$ and Feng Pan $^{a}$

CdTe is widely applied in thin film solar cells as p-type layer, which usually contacts with a metal back electrode. Using ab initio energy band calculations, here we study the interfacial properties of CdTe (110)-metal interfaces (metals = Al, Ag, Au, Cu, and Ni) systematically. Weak chemisorption and large interfacial distance are found between CdTe and Al, Ag and Cu surfaces, while medium or strong chemisorption and small interfacial distance are found between CdTe and Au, Ni surface. After GW correction, it is found that CdTe forms n-type Schottky contacts with Ag, Al and Cu and p-type Schottky contacts with Au and Ni at the interface between metalized CdTe and semiconductive CdTe, consistent with previous experimental values. Besides the Schottky barrier, tunneling barriers also exist at the CdTe-metal contact interface. The potential profiles at the vertical CdTe-metal interfaces reveal that due to the medium or strong chemisorption, tunneling barrier is absent at CdTe-Au and CdTe-Ni contact, while the weak bonding interfaces (Ag, Al and Cu) have obvious tunneling barriers. Finally, methods to optimize the interface of CdTe-metal contact to further decrease the Schottky barrier at the CdTe-metal contact are discussed.

## Introduction
Due to it' s ideal band gap (1.51 eV)¹ for solar terrestrial photoconversion, CdTe is a well-known $p$-type layer material in thin film solar cells, which possess the representative device structure: front electrode/$n$-type layer/$p$-type layer/back electrode. Besides the CdTe $p$-type layer in such CdTe solar cell device, transparent conducting films (TCFs) such as FTO, ITO and AZO are usually used as the front electrode, CdS is often used as $n$-type layer,²⁻⁵ and kinds of metal thin films such as Cu, Al, Ag, Au, and Ni are used as the back electrode.⁶⁻¹³ A finite Schottky barrier usually appears at the interface between the CdTe layer and metal layer, which would lower the carrier transfer efficiency and decrease the power conversion efficiency (PCE). Therefore, it is important to decrease Schottky barrier height (SBH) by optimizing the contact interfaces between thin films to enhance the performance of a solar cell. Unfortunately, the SBH does not simply depend on the work function of a metal and the band structure of the semiconductor layer because of the complex interface property. Many other factors, including interface reconstruction, surface state, and Fermi level pinning may influence the SBH. Thus understanding the interfacial properties between CdTe and metal layer is crucial, which would share helpful clues on how to optimize the contact interface between thin films.

The property of CdTe-metal interface has been partly studied experimentally,¹⁴⁻²⁰ and theoretical research is limited. Recently, using first-principles calculations, Odkhuu et al. studied the formation energies and SBHs of interfaces between Cd(Zn)Te (111) and different layers of Cu, Pt and Al²¹. However, CdTe in orientation (110) also has a high stability and commonly used in experiments¹⁸,²⁰,²²,²³, and some other metals (e. g., Au and Ni) are also adopted as back electrode in CdTe solar cells.¹²,¹³ Apparently, the interfaces between more metals and different crystal faces are worth studied.

Herein, using first-principles electronic band simulations, we explore the interfacial properties of CdTe (110) on high function metals (Au and Ni) and low function metals (Al, Ag and Cu) systematically for the first time. It is found that the binding energy of CdTe-Ni is obviously larger than others, which leads to a strong distortion of the interface and the disappearance of tunneling barrier. In consideration of GW correction and metallization of CdTe, $n$-type Schottky contact is formed between CdTe and Al, Cu and Ag with SBH of 0.12, 0.63 and 0.26 eV, respectively, and $p$-type Schottky contact comes into being between CdTe and Au and Ni with SBH of 0.44 and 0.66 eV, respectively. It is also found that the weak bonding interfaces (Ag, Al and Cu) have obvious tunneling barriers, which is another important character of a semiconductor-metal contact, while the medium or strong bonding interface (Au and Ni) has no tunneling barrier due to the strong orbital hybridization between Au/Ni and CdTe.

$^{a}$ School of Advanced Materials, Peking University, Shenzhen Graduate School, Shenzhen 518055, China. Email: zhengjx@pkusz.edu.cn and panfeng@pkusz.edu.cn

**Table 1.** Calculated interfacial properties of CdTe on the metal surface. The lattice mismatch is $\mathcal{E}$ . The equilibrium distance $d_{\text{CdTe-M}}$ is the averaged distance between the surface Cd and Te atoms and relaxed positions of the topmost metal layer in the direction vertical to the interfaces. $E_b$ is the binding energy. $W_M$ and $W$ are the calculated work functions for the clean metal surface and the metal surface adsorbed by CdTe, respectively. $\Phi_C$ is the SBHs obtained from *ab initio* band calculations. $\Phi_{\text{Exp}}$ is the SBHs obtained from experiments. The work function of CdTe is 5.21 eV. $\Delta V$, $w_B$, and $T_B$ are the tunneling barrier height, tunneling barrier width, and tunneling possibility, respectively.ᵉ For electron SBH.ʰ For hole SBH.

<table>
<thead>
<tr>
<th>Metal</th>
<th>$\mathcal{E}$ (%)</th>
<th>$d_{\text{CdTe-M}}$ (Å)</th>
<th>$E_b$ (eV)</th>
<th>$W_M$ (eV)</th>
<th>$W$ (eV)</th>
<th>$\Phi_C$ (eV)</th>
<th>$\Phi_{\text{Exp}}$ (eV)</th>
<th>$w_B$ (Å)</th>
<th>$\Delta V$ (eV)</th>
<th>$T_B$ (%)</th>
<th>Ref</th>
</tr>
</thead>
<tbody>
<tr>
<td>Al</td>
<td>5.0</td>
<td>2.30</td>
<td>1.35</td>
<td>4.22</td>
<td>4.05</td>
<td>0.12ᵉ</td>
<td>0-0.40ᵉ</td>
<td>0.49</td>
<td>1.41</td>
<td>56.7</td>
<td>22</td>
</tr>
<tr>
<td>Ag</td>
<td>5.6</td>
<td>2.27</td>
<td>1.25</td>
<td>4.21</td>
<td>4.19</td>
<td>0.26ᵉ</td>
<td>0.69-1.00ʰ</td>
<td>0.51</td>
<td>1.87</td>
<td>49.0</td>
<td>20</td>
</tr>
<tr>
<td>Au</td>
<td>5.5</td>
<td>1.96</td>
<td>1.58</td>
<td>5.02</td>
<td>4.97</td>
<td>0.44ʰ</td>
<td>0.59-0.90ʰ</td>
<td>0</td>
<td>0</td>
<td>100</td>
<td>20, 22</td>
</tr>
<tr>
<td>Cu</td>
<td>4.2</td>
<td>2.29</td>
<td>1.26</td>
<td>4.31</td>
<td>4.56</td>
<td>0.63ʰ</td>
<td>0.90~1.30ʰ</td>
<td>0.44</td>
<td>1.68</td>
<td>55.8</td>
<td>20</td>
</tr>
<tr>
<td>Ni</td>
<td>4.1</td>
<td>1.14</td>
<td>2.80</td>
<td>4.77</td>
<td>4.74</td>
<td>0.66ʰ</td>
<td>0.40-0.70ᵉ</td>
<td>0</td>
<td>0</td>
<td>100</td>
<td>22, 23, 46</td>
</tr>
</tbody>
</table>

### Methodology
We use six layers of metal atoms to simulate the metal surface and build a supercell with six-layer CdTe adsorbed on the metal surface. Six-layer atoms to model the metal surfaces can give converged properties of the contact system for the convergence tests done in the previous studies.²⁴⁻²⁶ The lattice parameter of (110)-CdTe is $a = 6.48$ Å and $b = 9.16$ Å. Apparently, the upper and the lower (110) surface of CdTe are symmetric, so the (110) surface is nonpolar. We use Virtual NanoLab version 2016.1, QuantumWise A/S to model the contact systems. Metals in (110) orientation rather than (111) orientation are chosen in order to match (110)-CdTe well, because the former have square lattice the same as (110)-CdTe while the latter have hexagonal lattice. The (110)-CdTe $2 \times 1$ unit cell is adjusted to the $2\sqrt{2} \times 2\sqrt{2}$ unit cells of metals. The lattice mismatch in each metal is listed in Table 1, ranging from 4.1%-5.6%. To prevent spurious interaction between periodic images, a vacuum buffer space is set with the value of at least 15 Å. The topmost two-layer atoms of metal mainly interact with the topmost two-layer CdTe atoms, so the bottom four layers of metal and CdTe atoms are fixed in x and y directions.
We use plane wave basis set and projector augmented wave (PAW)²⁷,²⁸ method implemented in the Vienna *ab initio* simulation package (VASP)²⁹,³⁰ code to optimize the structures. The generalized gradient approximation (GGA) functional to the exchange-correction functional of Perdew-Burke-Ernzerhof (PBE)³¹ form is adopted. The plane-wave cut off energy is set to 450 eV to ensure the accuracy. The Brillouin zone are sampled by $3 \times 3 \times 1$ special k-points for optimizing these structures and $7 \times 7 \times 1$ to get the densities of states (DOS) and potential using the Monkhorst Pack scheme³². Van der Waals interaction is taken into account, with the vdW-DF level of optB88 exchange functional (optB88-vdW).³³ To obtain reliable optimized structures, the maximum residual force is less than 0.01 eV/Å and energies are converged to within $1 \times 10^{-5}$ eV per atom. Using DFT+U with U = 13 eV³⁴ can reproduce the experimental lattice parameter of bulk CdTe. The reconstruction of (110)-CdTe is observed in previous researches³⁵,³⁶ and our calculation. We test different values of U to optimize the surface of (110)-CdTe and compare the predicted surface atomic geometry with the results from low-energy electron diffraction (LEED) intensity analysis.³⁶ As the Figure. S3 shows, PBE functional gives the best surface parameters except that z1 changes a little with the increasing U value. So we did not choose DFT+U method to further calculate the electronic structures of CdTe-metal systems. And first-principles many-electron Green function approach within GW approximation³⁷ is employed to calculate the band gap for CdTe to improve the electronic structure calculation gained by DFT.

### Results and discussions
#### Geometry and stability of CdTe-metal interfaces
In general, a high-symmetry configuration is more stable than a low-symmetry one and often selected as initial configuration. We have considered all the possible stacking configurations with high symmetry. After structure optimizing, the energy of the configuration shown in Figure S1 is lowest, so we choose it for subsequent calculations. Table 1 is the summary of the calculated key results of CdTe-metal interfaces studied in this work. The optimized interfacial structures are shown in Figure 2. The equilibrium interfacial distances $d_{\text{CdTe-M}}$ is defined as the difference between the average z-coordinates (vertical to the

![](./images/811048468343685120_3.jpg)

Figure 1. Interfacial structures of CdTe-metal systems. The purple, green and light gray ball present Cd, Te and metal atom, respectively. (a) Side views of the first configuration of CdTe on the metal surfaces. (b) The Brillouin zone of CdTe-metal systems. (c) Top view of the first configuration of CdTe on the metal surfaces. (cd) Schematic diagram of a CdTe solar cell. Top view of the second configuration of CdTe on the metal surfaces. The purple, green and light gray ball present Cd, Te and metal atom, respectively.

interface) of the bottom layer Cd and Te atoms and the top- most layer metal atoms (Figure 1a). It varies from 1.14 ~ 2.30 Å, decreasing in the order of Al > Cu > Ag > Au > Ni. The binding energy per interfacial Cd or Te atom is defined as
$$E_{b}=(E_{\text{CdTe}}+E_{\text{metal}}-E_{\text{CdTe-metal}})/N_{\text{Cd}} \tag{2}$$
where $E_{\text{CdTe}}$, $E_{\text{metal}}$, $E_{\text{CdTe-metal}}$ are the relaxed energies for CdTe surface, the metal surface, and the CdTe-metal system, respectively, and $N_{\text{Cd}}$ is the number of interface Cd atoms in a supercell. The $E_{b}$, varying from 1.25 ~ 2.80 eV, increases in the order of Ag < Al < Cu < Au < Ni. The higher $E_{b}$ corresponds to shorter $d_{\text{CdTe-M}}$. Considering $d_{\text{CdTe-M}}$ and $E_{b}$, two types of adsorption of CdTe-metal interfaces are classified. Al, Ag and Cu have weak adsorption and large interfacial distances with CdTe ($E_{b}=1.25 \sim 1.35$ eV and $d_{\text{CdTe-M}}=2.27 \sim 2.30$ Å). Au has a medium adsorption and interfacial distance with CdTe ($E_{b}=1.58$ eV and $d_{\text{Se-M}}=1.96$ Å). Ni has a strong adsorption and short interfacial distance with CdTe ($E_{b}=2.80$ eV and $d_{\text{Se-M}}=1.14$ Å). Comparing with other semiconductor-metal interfacial systems, such as Phosphorene-metal$^{38}$ and MoSe$_2$-metal$^{25}$, the binding energy of CdTe-metal is obviously larger, which means strong hybridization occurs in these systems.

![](./images/811048468343685120_4.jpg)

Figure 2. Side view (from a-axis) of the optimized structures and average effective potentials in planes normal to the interface of CdTe- Ag, Al, Au, Cu and Ni systems, respectively. $\Delta V$ is the height of barrier and $W_{B}$ is the full width at half-maximum (fwhm) of the potential barrier. The Fermi level is set to zero. The last figure shows different layers of CdTe atoms on metal surfaces.

## Electronic structures of CdTe-metal interfaces

The band structures of the interfacial systems and free-standing CdTe are shown in Fig. 3. The direct band gap at $\Gamma$ point of the free-standing CdTe is 0.87 eV, which is much smaller than the experimental value of 1.51 eV$^{1}$ and a little larger than the previous DFT value of 0.63 eV.$^{34,39}$ A feasible method to determine the accurate band edge position of the semiconductor is the first-principles many-electron Green function approach within GW approximation, which can also give a band gap consistent with experimental values. We suppose that the $E_{f}$ and the energy between $E_{f}$ and the valence band maximum (VBM) or the conduction band minimum (CBM) is unchanged after GW correction, $E_{C}^{\text{GW}}$ and $E_{V}^{\text{GW}}$ can be obtained as follows:
$$E_{C}^{\text{GW}}=E_{f}+\frac{E_{C}^{\text{DFT}}-E_{f}}{E_{g}^{\text{DFT}}} \times E_{g}^{\text{GW}}$$
$$E_{V}^{\text{GW}}=E_{f}+\frac{E_{f}-E_{V}^{\text{DFT}}}{E_{g}^{\text{DFT}}} \times E_{g}^{\text{GW}}$$
where $E_{g}^{\text{GW}}$ is the band gap of CdTe by GW approximation. $E_{f}$, $E_{C}^{\text{DFT}}$, $E_{V}^{\text{DFT}}$ and $E_{g}^{\text{DFT}}$ is the Fermi level, CBM, VBM and band gap of CdTe obtained by the DFT calculation, respectively. Based on unchanged Fermi level, this correction method has been used to get the absolute band position by previous works.$^{26,40,41}$ The band gap of pure CdTe calculated by GW method is 1.47 eV, consistent with the experiments. The Fermi level difference of CdTe calculated by DFT and GW methods is only 0.02 eV, so this correction method is applicable for CdTe.

As shown in Figure 3, the band structures of CdTe are destroyed on all the metal surfaces, indicating an orbital hybridization and chemical bonding between CdTe and these metals. Because the Fermi level always crosses the CdTe derived band, part of CdTe (contacted with metal) gets metallization. By contrast, the band structures of graphene on metals are not destroyed, some band structures of MoSe$_2$ on metals are destroyed and all band structures of phosphorene on metals are destroyed.$^{25,38}$ This difference indicates that the interactions between CdTe and metal surface are stronger than graphene and MoSe$_2$ on metal surfaces.

To deeply understand the hybridization degree of the band structures for CdTe adsorbed on metals, we further calculate

![](./images/811048468343685120_5.jpg)

Figure 3. Band structures of pure CdTe and CdTe-Al, Ag, Au, Cu and Ni contacts, respectively. Grey line: band structures of CdTe-metal systems; blue line: band structures of CdTe. The line width is proportional to the weight. The Fermi level is at zero energy.

the partial density of states (PDOS) on Cd and Te orbitals of CdTe-metal systems, as shown in Figure 4. Large amounts of CdTe states distribute in the origin band gap of CdTe in all the interfacial systems, indicating the metallization for CdTe at these surfaces. It is mainly the Te p and Cd s states that arise

![](./images/811048468343685120_6.jpg)

Figure 4. Partial density of states (PDOS) (DOS on specified atoms and orbitals, for example, Cd-s (s-orbital on Cd) of CdTe on the Al, Ag, Au, Cu and Ni surfaces at the DFT level. The Fermi level is at zero energy (red dash line). The PDOS of free-standing CdTe is provided for comparison.

![](./images/811048468343685120_7.jpg)

Figure 5. PDOS of different layer atoms of CdTe on the Al, Ag, Au, Cu and Ni surfaces (see Figure 2) at the DFT level. The Fermi level is at zero energy (red dash line).

in the pristine band gap of CdTe, while the Te s, Cd p and Cd d states only change a little. The PDOS at $E_{f}$ of CdTe-Ni system is the largest among all the contact systems, which is consistent with the band structure hybridization degree. The different hybridization degree can be illustrated by the different occupied level of d-orbital of metals. Al has unfilled d-orbitals and Cu, Ag and Au have fully filled d-orbital, so it' s hard for them to form strong covalent bond with the orbitals of the contacted Te atoms. Cu has a smaller d-orbital radius than Ag, so it has a stronger hybridization degree. While Ni has partially filled d-orbital, which makes the binding energy of CdTe and Ni is larger than other systems. Figure 5 shows the PDOS on different layer CdTe of CdTe-metal systems. The first and second layer atoms of CdTe undergo an obvious metallization, while the fifth and sixth layer atoms of CdTe almost stay semiconductor nature.

Schottky barrier and tunneling barrier of the contact between CdTe and metals.

The schematic diagram of CdTe and metal solar cell is shown in Figure 6a. Schottky barriers may exist at either of two different interfaces of a CdTe solar cell: One is between metal and CdTe contacted surface (labeled interface B), the other is between metalized CdTe and semiconductive CdTe (labeled interface D). According to the band structure and PDOS analysis above, the strong interaction between CdTe and metal makes CdTe contacted with metal metalized. So the Schottky barrier is absent at interface B and only appears at interface D. Because the fifth and sixth layer atoms of CdTe almost stay semiconductor nature, we suppose that the interface D is between the fourth and fifth layer of CdTe. It should be noted that though no Schottky barrier at interface B, tunneling barrier would exist at interface B when electrons or holes cross the gap between metal and CdTe. Figure 6b shows the schematic diagram of band bending and illustrates the appearance tunneling barrier and Schottky barrier.

Figure 7a shows the line-up of the metal Fermi level with the electronic bands of CdTe before and after GW correction. The calculated work function and the electron affinity of CdTe after metalized CdTe and semiconductive CdTe, with SBHs $\Phi$ = 0.26, 0.12, 0.63, 0.44 and 0.66 eV, respectively. As shown in Figure 7b, the SBHs gained by ab initio energy band calculation and experiment are very close. Especially, CdTe and Al forms a

![](./images/811048468343685120_8.jpg)

Figure 6. (a) Schematic cross-sectional view of a typical metal contact to CdTe. A, C, and E denotes three regions, while B and D are the two interfaces separating them. Red rows show the pathway (E→D→C→B→A) of hole injection from CdTe (E) to the metal (A). (b) Illustrations of the band bending of p-type SBHs that occur at CdTe and metal contacts. EFm and EFs denote the Fermi level of the interfacial systems or metal and CdTe, respectively.

![](./images/811048468343685120_9.jpg)

Figure 7. (a) Line-up of the work functions with DFT and GW-corrected electronic bands of CdTe. The blue dashed line is the work function of the pure metal, and the red solid line is the work function of contacted systems (metal and 1~4 layer CdTe). (b) Comparison of the Schottky barrier heights ($\phi^{e}$ for electron and $\phi^{h}$ for hole) of CdTe-Ag, Al, Cu, Au and Ni systems, respectively, obtained from both the ab initio electronic band calculations and experiments.

quasi-ohmic contact with SBH $\Phi$ = 0.12 eV for electron in our calculation, consistent with some previous experiments that ohmic contact for electron is formed between CdTe and Al contact.¹⁸,⁴² As a p-type layer in solar cell, SBHs for hole is the important property which we care for. The SBHs for hole decrease in the order of Al (1.35 eV) > Ag (1.21 eV) > Cu (0.84 eV) > Ni (0.66 eV) > Au (0.44 eV). Due to the smallest Schottky barrier for hole, using Au as back electrode may gain the best performance among these metal candidates for back electrode.

The tunneling barrier is another important character of a semiconductor-metal contact. The potential profiles at the vertical CdTe-metal interfaces are shown in Figure 2. The weak bonding interfaces (Ag, Al and Cu) have obvious tunneling barrier, while the strong bonding interface (Au and Ni) has no tunneling barrier due to the strong orbital hybridization between Au/Ni and CdTe. The barrier height of CdTe-Ag, Al and Cu is 1.87, 1.41and 1.68 eV, respectively. We use a square potential barrier to estimate the real potential barrier. The tunneling probability $T_{\text{B}}$ is defined by⁴³:

$$
T_{\text{B}} = \exp\left(-2\frac{\sqrt{2m\Delta V}}{\hbar} \times w_{B}\right)
$$

where $m$ is the mass of the free electron, $\hbar$ is the reduced Planck's constant, $\Delta V$ is the height of barrier and $w_{\text{B}}$ is the full width at half-maximum (fwhm) of the potential barrier as shown is Figure. 2. The result of $T_{\text{B}}$ values are 49.0, 55.8, 56.7, 100 and 100% for CdTe-Ag, Cu, Al, Au and Ni contacts, respectively. Thus the strong bonding between CdTe and Ni makes electrons or holes transferring freely.

![](./images/811048468343685120_10.jpg)

Figure 8. (a) Top view of the configuration of CdTe on the Cu2Te surfaces (b) Side view (from a-axis) of the optimized structures and average effective potentials in planes normal to the interface of CdTe-Cu2Te systems. (c) Band structures of CdTe-Cu2Te systems; blue line: band structures of CdTe. The line width is proportional to the weight. The red arrow shows the SBH (d) PDOS of different layer atoms of CdTe on the Cu2Te surface at the DFT level. The Fermi level is set to zero.

### Discussuion
From the above calculations, we can see that Schottky barriers exist in all the interfaces of CdTe-metal contacts. Even for Au, which possesses the smallest SBH for hole, the barrier is as high as 0.44 eV. To further improve the PCE of CdTe solar cells, methods are developed to optimize the interface of CdTe-metal contact. For example, when Cu is used as the back electrode, controllable Cu diffusion into CdTe surface layer are usually adopted by annealing to form $\text{Cu}_2\text{Te}$ between CdTe and Cu back electrode in devices.⁴⁴ For this reason, we also calculate the property of CdTe-Cu₂Te interface, as shown in Figure 8. The binding energy $E_{\text{b}}$ is 2.13 eV and the equilibrium interfacial distance $d_{\text{CdTe-M}}$ is 2.25 Å. The covalent bond, formed between Cd and Te at the interface, which has similar bond length (2.99 Å at interface vs 2.87 Å in CdTe) to the Cd-Te bond in bulk CdTe leads to the high binding energy and the medium equilibrium interfacial distance. Apparently, tunneling barrier is absent at CdTe-Cu₂Te contact, which ensure the high efficiency of hole injection. The SBH for hole can be extracted from the band structure by comparing the Fermi level and the identifiable band edge of CdTe in the CdTe-Cu₂Te contact. From Figure 8c, the $\Phi^{\text{h}}$ and $\Phi^{\text{e}}$ is 0.37 eV and 0.50 eV, respectively. Using GW correction, the $\Phi^{\text{h}}$ and $\Phi^{\text{e}}$ can be corrected to 0.63 eV and 0.84 eV, respectively. Compared with CdTe-Cu contact, the hole SBH of CdTe-Cu₂Te contact is $\Phi^{\text{h}}$ = 0.63 eV, while $\Phi^{\text{h}}$ = 0.84 eV in CdTe-Cu contact, and the tunneling probability $T_{\text{B}}$ of CdTe-Cu₂Te contact is 100% while $T_{\text{B}}$ = 55.8% in CdTe-Cu contact. So the diffusion of Cu and formation of $\text{Cu}_2\text{Te}$ would obviously improve the performance of the device. Recently, we use $\text{Cu}_9\text{S}_5$ as a buffer layer between CdTe and Au films, which shows a very high PCE (11.3%).⁴⁵ Because $\text{Cu}_9\text{S}_5$ can forms ohmic contact with Au, and produces a successive gradient-doping region by the controllable Cu diffusion, which greatly reduces the contact Schottky barrier.

## Conclusions

In summary, this work presented a systematical theory study of the physical property of CdTe-Al, Ag, Au, Cu and Ni interfaces. The adsorption level can be classified into three categories: weak chemisorption in CdTe and Al, Ag and Cu contacts, medium chemisorption in CdTe and Au contact, and strong chemisorption in CdTe and Ni contact. The band structure of CdTe is destroyed in all cases due to the strong hybridization. All metals form Schottky contact with CdTe, and the $p$-type SBHs decrease in the order of Al (1.35 eV) > Ag (1.21 eV) > Cu (0.84 eV) > Ni (0.66 eV) > Au (0.44 eV). By contrast, the weak bonding interfaces (Ag, Al and Cu) have obvious tunneling barrier, while the medium or strong bonding interface (Au and Ni) has no tunneling barrier due to the strong orbital hybridization between Ni and CdTe, leading to the tunneling probability $T_{\text{B}}$ decreasing in the order Ni (100%) = Au (100%) > Al (56.7%) > Cu (55.8%) > Ag (49.0%). Finally, methods to optimize the interface of CdTe-metal contact to further decrease the Schottky barrier at the CdTe-metal contact are discussed.

## Acknowledgements

This work was supported by the National Materials Genome Project (2016YFB0700600), Guangdong Innovation Team Project (No. 2013N080), Shenzhen Science and Technology Research Grant (No. ZDSY20130331145131323, JCYJ20140903101633318, JCYJ20140903101617271).

## Notes and references

1 G. Fonthal, L. Tirado-Mejía, J. I. Marín-Hurtado, H. Ariza- Calderón and J. G. Mendoza-Alvarez, *J. Phys. Chem. Solids*, 2000, **61**, 579–583.
2 V. P. Singh, O. M. Erickson and J. H. Chao, *J. Appl. Phys.*, 1995, **78**, 4538–4542.
3 H. Bi, F. Huang, J. Liang, X. Xie and M. Jiang, *Adv. Mater.*, 2011, **23**, 3202–3206.
4 K. Zweibel, *Science* (80- .), 2010, **328**, 699–701.
5 J. D. Major, R. E. Treharne, L. J. Phillips and K. Durose, *Nature*, 2014, **511**, 334–337.
6 D. L. Bätzner, A. Romeo, H. Zogg, R. Wendt and A. N. Tiwari, *Thin Solid Films*, 2001, **387**, 151–154.
7 N. Romeo, A. Bosio, V. Canevari and A. Podestà, *Sol. Energy*, 2004, **77**, 795–801.
8 C. R. Corwine, A. O. Pudov, M. Gloeckler, S. H. Demtsu and J. R. Sites, *Sol. Energy Mater. Sol. Cells*, 2004, **82**, 481–489.
9 A. Gupta, V. Parikh and A. D. Compaan, *Sol. Energy Mater. Sol. Cells*, 2006, **90**, 2263–2271.
10 S. H. Demtsu, D. S. Albin, J. W. Pankow and A. Davies, *Sol. Energy Mater. Sol. Cells*, 2006, **90**, 2934–2943.
11 A. Niemegeers and M. Burgelman, *J. Appl. Phys.*, 1997, **81**, 2881–2886.
12 U. Kaufmann, J. Windscheif and G. Brunthaler, *J. Phys. C Solid State Phys.*, 1984, **17**, 6169.
13 K. Ernst, R. Engelhardt, K. Ellmer, C. Kelch, H.-J. Muffler, M.- C. Lux-Steiner and R. Könenkamp, *Thin Solid Films*, 2001, **387**, 26–28.
14 V. A. Gnatyuk, T. Aoki, Y. Hatanaka and O. I. Vlasenko, *Appl. Surf. Sci.*, 2005, **244**, 528–532.

15 J. L. Shaw, R. E. Viturro, L. J. Brillson and D. LaGraffe, *Appl. Phys. Lett.*, 1988, **53**, 1723.
DOI: 10.1039/C7TA00698E
16 A. E. Fowell, R. H. Williams, B. E. Richardson and T. H. Shen, *Semicond. Sci. Technol.*, 1990, **5**, 348–350.
17 H. Toyama, M. Yamazato, A. Higa, T. Maehama, R. Ohno and M. Toguchi, *Japanese J. Appl. Physics, Part 1 Regul. Pap. Short Notes Rev. Pap.*, 2005, **44**, 6742–6746.
18 A. K. Wahi, *J. Vac. Sci. Technol. A Vacuum, Surfaces, Film.*, 1990, **8**, 1926.
19 G. H. Parker and C. A. Mead, *Phys. Rev.*, 1969, **184**, 780–787.
20 S. E. Laboratories and S. Uniuersity, *Phys. Rev. B*, 1988, **37**, 731–739.
21 D. Odkhuu, M. S. Miao, F. Aqariden, C. Grein and N. Kioussis, *J. Appl. Phys.*, 2016, **120**, 185703.
22 T. Takabe, J. Saraie and T. Tanaka, *Phys. Status Solidi Appl. Res.*, 1978, **47**, 123–130.
23 M. H. Patterson and R. H. Williams, *J. Cryst. Growth*, 1982, **59**, 281–288.
24 Y. Wang, R. X. Yang, R. Quhe, H. Zhong, L. Cong, M. Ye, Z. Ni, Z. Song, J. Yang, J. Shi, J. Li and J. Lu, *Nanoscale*, 2016, 1179–1191.
25 Y. Pan, S. Li, M. Ye, R. Quhe, Z. Song, Y. Wang, J. Zheng, F. Pan, W. Guo, J. Yang and J. Lu, *J. Phys. Chem. C*, 2016, **120**, 13063–13070.
26 Y. Y. Pan, Y. Y. Wang, L. Wang, H. X. Zhong, R. G. Quhe, Z. Y. Ni, M. Ye, W. N. Mei, J. J. Shi, W. L. Guo, J. B. Yang and J. Lu, *Nanoscale*, 2015, **7**, 2116–2127.
27 P. E. Blöchl, *Phys. Rev. B*, 1994, **50**, 17953–17979.
28 G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 11–19.
29 G. Kresse and J. Furthmüller, *Comput. Mater. Sci.*, 1996, **6**, 15–50.
30 G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169–11186.
31 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, 3865–3868.
32 H. J. Monkhorst and J. D. Pack, *Phys. Rev. B*, 1976, **13**, 5188–5192.
33 J. K. and D. R. B. and A. Michaelides, *J. Phys. Condens. Matter*, 2010, **22**, 22201.
34 Y. Wu, G. Chen, Y. Zhu, W. J. Yin, Y. Yan, M. Al-Jassim and S. J. Pennycook, *Comput. Mater. Sci.*, 2015, **98**, 18–23.
35 Y. R. Wang, C. B. Duke, K. O. Magnusson and S. A. Flodström, *Surf. Sci.*, 1988, **205**, L760–L770.
36 R. J. Meyer, C. B. Duke, A. Paton, J. L. Yeh, J. C. Tsang, A. Kahn and P. Mark, *Phys. Rev. B*, 1980, **21**, 4740–4750.
37 L. Hedin, *Phys. Rev.*, 1965, **139**, A796--A823.
38 Y. Pan, Y. Wang, M. Ye, R. Quhe, H. Zhang, Z. Song, X. Peng, D. Yu, J. Yang, J. Shi and J. Lu, *Chem. Mater.*, 2016, **28**, 2100–2109.
39 E. Menéndez-Proupin, A. Amézaga and N. Cruz Hernández, *Phys. B Condens. Matter*, 2014, **452**, 119–123.
40 C. Gong, H. Zhang, W. Wang, L. Colombo, R. M. Wallace and K. Cho, *Appl. Phys. Lett.*, 2013, **103**, 53513.
41 H. Jiang, *J. Phys. Chem. C*, 2012, **116**, 7664–7671.
42 R. H. Williams and M. H. Patterson, *Appl. Phys. Lett.*, 1982, **40**, 484–486.
43 X. Ji, J. Zhang, Y. Wang, H. Qian and Z. Yu, *Phys. Chem. Chem. Phys.*, 2013, **15**, 17883–17886.
44 K. D. Dobson, I. Visoly-Fisher, G. Hodes and D. Cahen, *Sol. Energy Mater. Sol. Cells*, 2000, **62**, 295–325.
45 M. J. Zhang, Q. Lin, X. Yang, Z. Mei, J. Liang, Y. Lin and F. Pan, *Nano Lett.*, 2016, **16**, 1218–1223.
46 L. A. Kosyachenko, V. M. Sklyarchuk, O. F. Sklyarchuk, O. L. Maslyanchuk, V. A. Gnatyuk and T. Aoki, *IEEE Trans. Nucl. Sci.*, 2009, **56**, 1827–1834.
