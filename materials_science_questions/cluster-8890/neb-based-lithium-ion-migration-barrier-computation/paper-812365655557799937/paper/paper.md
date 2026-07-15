ion batteries, in particular whether a monolayer of GmO can hold Li atoms in concentrations ranging from sparse to fully saturated, and to predict the theoretical maximum capacity of the material in its 2D form. Since there are no experimentally known periodic 3D GmO structures, computations with monolayers are basics of this work.

Graphite served as the anode material in the first commercial Li-ion battery made by Sony⁹ and is still a dominant anode material. The 3D crystal structure of graphite consists of AB stacking of graphene. When a battery is being charged, Li⁺-ions arrive at the anode, accept electrons conducted by graphite from the external source, and then intercalate as Li atoms. The maximum theoretical capacity for Li is 372 mAh/g, corresponding to one Li atom held by six C atoms (LiC₆).¹⁰ Because of this limit, much fundamental and applied research is devoted to the search for replacement materials that keep many of the desirable properties of graphite while safely increasing the key parameters such as gravimetric and/or volumetric specific capacity, charging speed, and operation at low temperatures. Graphite is used as one of the comparison test materials in this work.

Graphene monolayers have been studied previously for their promise to double the capacity of graphite to Li₂C₆ if Li could be held above and below the monolayer. First-principles calculations of Li adsorption on a graphene monolayer showed quite the opposite: Li does not bind to graphene and bulk Li metal is more stable than adsorbed Li near the surface of the graphene monolayer.¹¹⁻¹⁴ Hence, a monolayer of graphene is not an active anode material. For comparison, intercalation of Li into graphite for the LiC₆ compound is more favorable than bulk Li metal¹⁵ although Li atoms do not create bonds with C atoms. In addition to graphite, graphene is also used as a comparison test in this research.

In GmO, the presence of O atoms above and below the C plane in a 1,3-dioxetane¹⁶ configuration (Figure 1) leads to increased distance between two C atoms in the unit cell and a larger lattice constant. The most important difference between GmO and graphene is the fact that there is no known 3- dimensional equivalent for GmO as graphite is for graphene. Unlike in graphene oxide (GO), where various oxygen functional groups (e.g., epoxide C−O−C, carbonyl C═O, hydroxyl C−OH, and carboxyl OH−C═O) are attached to the graphene lattice in random locations, O atoms in GmO are arranged periodically and their number is equal to the number of C atoms. Compared to graphene, Li was shown to have enhanced attraction to GO layers due to the presence of O atoms.¹⁷ For these reasons, we investigate how Li atoms interact with a GmO monolayer and compare it to the graphene case.

### METHODS
All density functional theory (DFT) computations were performed with Quantum ESPRESSO 6.4.1¹⁸,¹⁹ and visualized via XCrySDen 1.6.2²⁰ and VESTA 3.4.8.²¹ Projector augmented-wave scalar-relativistic pseudopotentials for C, O, and Li atoms from PSlibrary 1.0.0²² were used, together with the Perdew−Burke−Ernzerhof (PBE) generalized gradient approximation for exchange−correlation. A plane wave kinetic energy cutoff of 50 Ry (180 eV) for the expansion of the wave functions and kinetic energy cutoff of 326 Ry (1175 eV) for the charge density and potential were applied. Periodic supercells ranging from 1 × 1 to 5 × 5 were considered depending on the concentrations of Li atoms.

To make energies for different concentrations of Li atoms comparable, simulations with equivalent Monkhorst−Pack k- point meshes were performed: an 18 × 18 × 1 grid for the 1 × 1 unit cell, a 9 × 9 × 1 for the 2 × 2 supercell, and a 6 × 6 × 1 for the 3 × 3 supercell. These were chosen since for hexagonal structures the (Γ-centered) k-point mesh must be of the form 3N × 3N in order to include the K point. However, due to computational limitations, only the 4 × 4 × 1 grid was used for the 4 × 4 and 5 × 5 supercells. To minimize interactions between periodic images, a vacuum separation of 20 Å between GmO layers was made. Furthermore, to avoid long-range electric dipole effects, two layers of GmO per supercell were used when the number of Li atoms above the monolayer was not equal to the number of Li atoms below. Adding the second layer of GmO with the inverted number of Li atoms above and below in the same supercell cancels a possible long-range electric dipole created by the periodic structure in the z- direction.

The adsorption energy (heat of formation) of Li on GmO per Li atom, relative to Li phase segregation, is

$$
\Delta E_{\mathrm{Li}}=\frac{E_{\mathrm{GmO}+\mathrm{Li}}-\left(E_{\mathrm{GmO}}+E_{\mathrm{Li}} \times N_{\mathrm{Li}}\right)}{N_{\mathrm{Li}}}
\tag{1}
$$

where $E_{\text{GmO}}$ is the total energy of one (super-) cell of GmO, $E_{\text{Li}}$ is the total energy of a Li in its bulk ground state, and $E_{\text{GmO+Li}}$ is the total energy of one (super-) cell of GmO with $N_{\text{Li}}$ intercalated Li atoms. $E_{\text{Li}}$ of a Li atom was found to be −204.67 eV for both body-centered cubic (bcc) and hexagonal closest packed (hcp) bulk lithium configurations. The difference in $E_{\text{Li}}$ between bcc and hcp was less than 0.5 meV/atom (in line with other DFT papers²³,²⁴), which is smaller than the 0.01 eV precision of the reported results.

### RESULTS
Li−Graphite and Li−Graphene. As a benchmark against which to compare the interaction of Li and GmO, we first consider the case of Li intercalation in graphite. During Li intercalation, the stacking of C layers changes from ABAB to AAAA and the spacing between layers increases from 3.35 to 3.70 Å.²⁵ Our calculations confirmed the published results for the fully Li-intercalated graphite−“hexal” ordering−LiC₆. Figure 2a shows the initial (ABAB) and final (AAAA) stages of relaxation of LiC₆ in graphite. Notably, Li intercalation into graphite is energetically favorable, with $\Delta E_{\mathrm{Li}}^{\text{graphite}}=-0.12$ eV, demonstrating that this LiC₆ configuration is stable.

For the case when LiC₆ consists of a graphene monolayer and all Li atoms are on one side of the monolayer, the relaxed structure places the Li atoms just above the hollow sites of graphene, Figure 2b. However, in contrast to Li intercalated into graphite, the adsorption energy is positive, $\Delta E_{\mathrm{Li}}^{\text{graphene}}=$ 0.60 eV, in agreement with published papers.¹³,²⁶ Thus, the Li atoms are more likely to form bulk lithium metal clusters than coating the graphene.

Increasing the Li concentration to Li₂C₆ by adding additional Li atoms to the other side of the graphene layer leads to a calculated formation energy of 0.60 eV, the same as for LiC₆. Thus, the calculated results strongly imply that for a graphene monolayer, the Li/C ratio will not reach that of graphite, let alone doubling it.

Single Li Atom near the GmO Monolayer. The first step toward understanding the interaction of Li atoms with GmO monolayers is to explore the preferred sites for

![](./images/812365655557799937_1.jpg)

Figure 2. Initial and relaxed structures of $LiC_6$ for (a) Li intercalated graphite and (b) Li on monolayer graphene. In the top views in (a), only two layers of C atoms are shown (C: gray; Li: blue).

![](./images/812365655557799937_2.jpg)

Figure 3. GmO high-symmetry sites shown in the $1 \times 1$ unit cell.

![](./images/812365655557799937_3.jpg)

Figure 4. (a) Li atom above the lowest energy site of GmO that corresponds to the hollow H-site; (b) S-site as a centroid of the green triangle formed by three neighboring O atoms. Equivalent GmO unit cells are shown in black. Top view (C: gray; O: red; Li: blue).

adsorption of a single Li atom on the GmO monolayer in the absence of other Li atoms by (i) finding the lowest energy site by probing high-symmetry sites and allowing full relaxation of all atoms and (ii) determining the energy surface for a Li atom above the GmO monolayer, fixing all coordinates of the C and O atoms and for each fixed $(x, y)$ position of the Li allow relaxation in the $z$-direction.

The five high-symmetry starting sites used for the relaxations, shown in Figure 3, are:
1. $T_O$-site: above the O atom.
2. $T_C$-site: top site above the C atom.
3. B-site: bridge above the middle of the C$-$C bridge.
4. S-site: special-site above the centroid of the triangle formed by three neighboring O atoms (Figure 4b).
5. H-site (hollow-site) above the quasi-hexagonal hollow.

![](./images/812365655557799937_4.jpg)

Figure 5. Changes with respect to lattice constant $a_{lat}$ and opening angle $\alpha$ of (a) total energy of a unit cell of a GmO monolayer, (b) height of the O atoms above the plane of the carbon atoms, and (c) $x$-coordinate of the C atoms relative to the O atoms. The area of the cell is constant along the red line and equal to that of the fully relaxed GmO unit cell denoted with the red circle (corresponding to the structure from Figure 1).

<table>
<thead>
<tr>
<th>site</th>
<th>$\Delta E_{Li}$, eV</th>
<th>$z_{Li}$, Å</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T_O$</td>
<td>0.03</td>
<td>2.85</td>
</tr>
<tr>
<td>$T_C$</td>
<td>0.01</td>
<td>2.68</td>
</tr>
<tr>
<td>B</td>
<td>−0.08</td>
<td>2.40</td>
</tr>
<tr>
<td>S</td>
<td>−0.21</td>
<td>2.31</td>
</tr>
<tr>
<td>H</td>
<td>−0.36</td>
<td>2.44</td>
</tr>
</tbody>
</table>
$^{a}$The GmO structure is constrained to have $\alpha = 130^\circ$ and $a_{lat} = 3.13$ Å.

For computational purposes, a $4 \times 4$ periodic supercell of GmO was used to approximate a single Li atom interacting with the monolayer. Upon periodic continuation, this guaranteed a distance of about 24 Å between neighboring Li atoms in the plane parallel to the monolayer. Variable-cell relaxation placed the Li at the H-site, 2.37 Å above the plane of the C atoms. The H-site was identified as the most preferable, with a negative formation energy with respect to the bulk lithium metal of $\Delta E_{Li} = -0.59$ eV. Above the H-site, a Li forms two bonds with two O atoms, Figure 4a.

Including Grimme's DFT-D3 van der Waals correction$^{27}$ with Becke-Jonson (BJ)$^{28}$ damping, the formation energy $\Delta E_{Li}$ for Li at the H-site was only 0.02 eV less negative, and the Li atom moved 0.01 Å closer to the monolayer. The order of magnitude of these dispersion contributions is comparable to Li$-$graphene DFT results reported before.$^{29}$ In addition, with

![](./images/812365655557799937_5.jpg)

Figure 6. (a) $\Delta E_{Li}$ relative to bulk bcc Li; for the values at the high-symmetry points (c.f., Figure 3), see Table 1. (b) Relaxed height of a Li atom above the GmO monolayer. Black lines represent boundaries of the GmO unit cell.

![](./images/812365655557799937_6.jpg)

Figure 7. (a) Front view and (b) side view of the change in the electron density distribution $\Delta \rho_{\text{GmO+Li}}$ around the Li atom. Seven isosurfaces are shown, with yellow to red (green to violet) showing the gain (loss) of electron density on selected isosurfaces. (c) Change in the planar-averaged density, $\Delta \lambda(z)$. Arrows denote the z-coordinates of the atoms.

![](./images/812365655557799937_7.jpg)

Figure 8. Top views of (a) $\text{Li}_2\text{C}_6\text{O}_6$ ($\text{Li}_{0.67}\text{C}_2\text{O}_2$) similar to the $\text{LiC}_6$ hexal structure of lithiated graphite but with Li atoms above and below the plane of GmO and (b) $\text{Li}_2\text{C}_2\text{O}_2$, with the densest packing and highest concentration of Li.

<table>
 <thead>
  <tr>
   <th>structure</th>
   <th>$\text{Li}_x\text{C}_2\text{O}_2$</th>
   <th>$\Delta E_{Li}$ eV</th>
   <th>$\alpha$ °</th>
   <th>$a_{\text{lat}}$ Å</th>
   <th>capacity mAh/g</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>$\text{Li}_2\text{C}_2\text{O}_2$</td>
   <td>$\text{Li}_2\text{C}_2\text{O}_2$</td>
   <td>0.06</td>
   <td>134</td>
   <td>3.34</td>
   <td>957</td>
  </tr>
  <tr>
   <td>$\text{LiC}_2\text{O}_2$</td>
   <td>$\text{Li}_1\text{C}_2\text{O}_2$</td>
   <td>0.12</td>
   <td>134</td>
   <td>3.34</td>
   <td>478</td>
  </tr>
  <tr>
   <td>$\text{Li}_2\text{C}_6\text{O}_6$</td>
   <td>$\text{Li}_{0.67}\text{C}_2\text{O}_2$</td>
   <td>−0.04</td>
   <td>133</td>
   <td>3.22</td>
   <td>319</td>
  </tr>
  <tr>
   <td>$\text{LiC}_4\text{O}_4$</td>
   <td>$\text{Li}_{0.5}\text{C}_2\text{O}_2$</td>
   <td>0.06</td>
   <td>132</td>
   <td>3.20</td>
   <td>239</td>
  </tr>
  <tr>
   <td>$\text{Li}_2\text{C}_8\text{O}_8$</td>
   <td>$\text{Li}_{0.5}\text{C}_2\text{O}_2$</td>
   <td>−0.11</td>
   <td>132</td>
   <td>3.22</td>
   <td>239</td>
  </tr>
  <tr>
   <td>$\text{LiC}_6\text{O}_6$</td>
   <td>$\text{Li}_{0.33}\text{C}_2\text{O}_2$</td>
   <td>−0.07</td>
   <td>131</td>
   <td>3.18</td>
   <td>159</td>
  </tr>
  <tr>
   <td>$\text{LiC}_8\text{O}_8$</td>
   <td>$\text{Li}_{0.25}\text{C}_2\text{O}_2$</td>
   <td>−0.16</td>
   <td>131</td>
   <td>3.17</td>
   <td>120</td>
  </tr>
  <tr>
   <td>$\text{Li}_2\text{C}_{18}\text{O}_{18}$</td>
   <td>$\text{Li}_{0.22}\text{C}_2\text{O}_2$</td>
   <td>−0.44</td>
   <td>131</td>
   <td>3.18</td>
   <td>106</td>
  </tr>
  <tr>
   <td>$\text{Li}_2\text{C}_{32}\text{O}_{32}$</td>
   <td>$\text{Li}_{0.13}\text{C}_2\text{O}_2$</td>
   <td>−0.58</td>
   <td>132</td>
   <td>3.13</td>
   <td>60</td>
  </tr>
  <tr>
   <td>$\text{LiC}_{18}\text{O}_{18}$</td>
   <td>$\text{Li}_{0.11}\text{C}_2\text{O}_2$</td>
   <td>−0.45</td>
   <td>130</td>
   <td>3.19</td>
   <td>53</td>
  </tr>
  <tr>
   <td>$\text{LiC}_{32}\text{O}_{32}$</td>
   <td>$\text{Li}_{0.06}\text{C}_2\text{O}_2$</td>
   <td>−0.59</td>
   <td>130</td>
   <td>3.09</td>
   <td>30</td>
  </tr>
  <tr>
   <td>$\text{LiC}_{50}\text{O}_{50}$</td>
   <td>$\text{Li}_{0.04}\text{C}_2\text{O}_2$</td>
   <td>−0.58</td>
   <td>130</td>
   <td>3.09</td>
   <td>19</td>
  </tr>
 </tbody>
</table>

$^{a}$Li is on one side only for $\text{LiC}_n\text{O}_n$ structures and on both for $\text{Li}_2\text{C}_n\text{O}_n$.

![](./images/812365655557799937_8.jpg)

Figure 9. Band structure of the (a) GmO monolayer and (b) $\text{Li}_2\text{C}_{32}\text{O}_{32}$ and (c) $\text{Li}_2\text{C}_2\text{O}_2$ configurations. Energies are given relative to the Fermi level.

![](./images/812365655557799937_9.jpg)

Figure 10. DOSs (per GmO formula unit) for the fully relaxed GmO monolayer and $\text{LiC}_6\text{O}_6$, $\text{Li}_2\text{C}_6\text{O}_6$, and $\text{Li}_2\text{C}_2\text{O}_2$ structures. The Fermi energy is at 0 eV.

DFT-D3 (BJ) dispersion corrections, the formation energy of GmO from its constituents—carbon and oxygen—was found to be 0.03 eV/atom more negative compared to only PBE calculation. The DFT-D3 (BJ) form was chosen because it provides the best description of the AB stacking properties of the graphene bilayer and graphite when compared to the experiment.⁽³⁰⁾ It is possible that other dispersion corrections would work better in the presence of O and Li atoms, but in the absence of experimental constraints to select the best dispersion approximation, further results are presented without any dispersion correction.

![](./images/812365655557799937_10.jpg)

Figure 11. Planar-averaged charge density normalized to the unit cell of GmO, for $\frac{2}{3}$ GmO states above the Fermi level (red) and $\frac{2}{3}$ Li₂C₆O₆ states below the Fermi level (green).

After computations for Li adsorption above the H-site on the GmO monolayer in the 4 × 4 supercell, and smaller cells (1 × 1, 2 × 2, and 3 × 3) with variable-cell relaxation, it was noted that GmO easily changes its structure as described by the opening angle $\alpha$ and lattice constant of the unit cell $a_{lat}$. Figure 5 shows the variations of the energy and the positions of the C and O atoms with respect to $\alpha$ and $a_{lat}$ for a GmO monolayer without Li. Red lines connect points that have the same area (obey Vegard's Law) as the area of the fully relaxed GmO unit cell with $a_{lat} = 3.13$ Å and $\alpha = 130^\circ$. As seen in Figure 5a, there is a large shallow energy minimum in terms of $\alpha$ and $a_{lat}$, which implies that the structure of a GmO monolayer may be easily disturbed by interaction with Li. The internal positions of the C and O atoms roughly change as would be expected from simple geometric arguments related to changes in the shape and size of the unit cell (c.f., Figure 1); for example, Figure 5b shows that the height of the O atoms above the C plane depends mostly on the lattice constant $a_{lat}$ and decreases as $a_{lat}$ increases (with a maximum for $\alpha$ between 120 and $125^\circ$).

Because of this softness of the GmO monolayer and the tendency of O atoms to shift toward Li, the in-plane positions of all the C and O atoms and size of the 4 × 4 supercell were fixed in order to make energies of the Li atom above the high-symmetry sites comparable. The adsorption energies of a single Li and height above the high-symmetry sites of the constrained GmO monolayer are given in Table 1.

The H-site is the lowest energy site for a single adsorbed Li atom. Even though $\Delta E_{Li}$ is less negative for S- and B-sites than for the H-site, the binding of Li at these sites is still preferable compared to forming Li bulk clusters. Thus, there is a likelihood that both the S- and B-sites may be occupied during Li adsorption at higher concentrations. The energies and heights throughout the unit cell are given in Figure 6.

As shown in Figure 6a, energetically Li has a preference to be near the H-site, and a Li atom has, Figure 6b, its closest approach to the GmO monolayer at the S-site. Thus, since the energy difference between the H- and S-sites is small, the S-site may be favorable for a multilayer system when Li intercalates between GmO layers because the added constraints imposed by having layers above and below could force the Li closer to the GmO plane.

When two systems, A and B, interact, the difference in charge density $\Delta \rho$ of the interacting system relative to the superposition of the individual densities

$$
\Delta \rho_{\mathrm{A+B}} = \rho_{\mathrm{A+B}} - \left( \rho_{\mathrm{A}} + \rho_{\mathrm{B}} \right) \tag{2}
$$

may provide a direct measure of the bonding. The calculated $\Delta \rho_{\mathrm{GmO+Li}}$ for a single Li atom above the H-site is shown in Figure 7. These results show a general loss of charge around the Li but a gain along the Li−O bond, demonstrating that the bonding of Li to GmO has both ionic and covalent characteristics. Thus, a Li atom can relatively easily lose its electron as it leaves the GmO, turning into a Li⁺-ion. Such behavior is necessary for the GmO to function as an anode in a Li-ion battery.

That the bonding causes a more complicated redistribution of charge than a simple ionic picture would suggest can be seen by considering the difference in the planar averaged densities, $\lambda(z) = \int \rho(x, y, z)\mathrm{d}x\mathrm{d}y$,

$$
\Delta \lambda(z) = \lambda_{\mathrm{GmO+Li}}(z) - \left( \lambda_{\mathrm{GmO}}(z) + \lambda_{\mathrm{Li}}(z) \right) \tag{3}
$$

Figure 7c presents $\Delta \lambda(z)$ for Li + GmO corresponding to Figure 7a,b. The Li clearly shifts charge from the vacuum side toward O, with a net loss. In the GmO, there is an increase in the $\pi$ ($p_z$) states of C together with a loss in $\sigma$ ($p_{x,y}$) in-plane orbitals. Although the Li atom donates charge to the GmO monolayer, there are additional bonding effects going on.

**Parameters for Different Concentrations of Li Atoms on a Single GmO Monolayer.** To simplify the analysis, we assume that Li atoms stay above and below the hollow sites of the GmO monolayer. Using the terminology for Li-intercalated graphite, where the highest concentration of Li, and hence for charge, is denoted as LiC₆, Li₂CₙOₙ structures have pairs of Li atoms above and below the same hollow sites (e.g., see Figure 8) and LiCₙOₙ structures have Li atoms only on one side of the

![](./images/812365655557799937_11.jpg)

Figure 12. Path for the transport of Li (a) through and (c) between hollow sites above the GmO monolayer. The corresponding changes in the total energy of the of the 4 × 4 GmO supercell (b) z coordinate of the Li or (d) along the surface path.

GmO monolayer. Other configurations are out of the scope of this paper. The $Li_{2}C_{6}O_{6}$ ($Li_{0.67}C_{2}O_{2}$) and $Li_{2}C_{2}O_{2}$ configurations are shown in Figure 8.

Table 2 shows the formation energy per Li for the fully relaxed structures. The results demonstrate that Li atoms are generally more bound to the GmO monolayer at low Li concentrations that correspond to a low charge capacity. It also suggests that Li atoms tend to repel each other rather than form Li clusters on the monolayer. The tendency of the Li atoms to remain far apart from one another is important for the Li transport on GmO and possible application for fast charging in batteries.

Theoretical capacities are computed via
$$
c_{\mathrm{Li}_{x} \mathrm{C}_{y} \mathrm{O}_{y}}=\frac{x \times e}{y \times\left(m_{\mathrm{C}}+m_{\mathrm{O}}\right)} \tag{4}
$$
where $e$ is the elementary charge (in mAh) and $m_{C}$ and $m_{O}$ are atomic masses (in grams) of the C and O atoms correspondingly. The largest theoretical capacity of 957 mAh/g is predicted for the $Li_{2}C_{2}O_{2}$ configuration when Li atoms are placed above and below each hollow site of the GmO monolayer. This capacity is 2.6 times higher than the theoretical capacity of graphite (372 mAh/g for $LiC_{6}$). The case when each hollow site holds a Li atom on only one side of the GmO monolayer ($LiC_{2}O_{2}$) has a capacity that is 1.3 times higher than that of graphite. All other configurations have lower capacities than graphite. The gradual increase in capacity from the bottom to the top of the table is equivalent to the increase in capacity of graphite as more Li intercalates to reach the final hexal ordering of $LiC_{6}$.

Although the highest capacities $Li_{2}C_{2}O_{2}$ and $LiC_{2}O_{2}$ from Table 2 have $\Delta E_{Li}>0$ eV, and hence are less stable than the formation of bulk Li metal, these energies are much smaller in magnitude than their equivalents in graphene. For example, the hexal structure equivalent of Li atoms on both sides of graphene ($Li_{2}C_{6}$) has a predicted energy gain of +0.60 eV per Li atom while the same structure on GmO ($Li_{2}C_{6}O_{6}$) gives $\Delta E_{Li}$ of −0.04 eV. In addition, previous experience with graphene and graphite suggests that these structures would be feasible in multilayers of GmO for use in anodes of Li-ion batteries, similar to the situation where $LiC_{6}$ concentration is not energetically favorable for graphene while it is favorable for graphite. It should be noted that inclusion of the DFT-D3 (BJ) dispersion correction for $Li_{2}C_{2}O_{2}$ lowered $\Delta E_{Li}$ from 0.06 to 0.04 eV, confirming that the dispersion corrections are small even for the fully lithiated structure.

Band Structure and Density of States. Energy bands for lithiated and unlithiated structures were compared along the $K_{1} \to M_{1} \to \Gamma \to K_{2} \to M_{2} \to \Gamma \to K_{1} \to M_{2}$ path in the first Brillouin zone of GmO, Figure 9a. When supercells were required, a $k$-projection unfolding scheme $^{31−34}$ was applied in order to extract only those parts of the supercell energy bands that are relevant to the unit cell. Figure 9 shows energy bands for the pure GmO monolayer and $Li_{2}C_{32}O_{32}$ and $Li_{2}C_{2}O_{2}$ structures.

The pure GmO monolayer is a semiconductor with a 3.03 eV direct band gap at the $\Gamma$-point and an indirect band gap of 0.58 eV for the $M_{1}−\Gamma$ transition (Figure 9a), in agreement with previous work. $^{1,3}$ Even at the low Li concentrations of $Li_{2}C_{32}O_{32}$, the GmO-Li structure turns into a conductor as seen in Figure 9b: the Fermi level crosses one of the conduction bands of the pure GmO monolayer at the $\Gamma$-point. The highest considered concentration of Li in $Li_{2}C_{2}O_{2}$ from Figure 8 has metallic properties with the Fermi level crossing three conduction bands of the pure GmO monolayer at the $\Gamma$-point, Figure 9c. To a first approximation, the metallic nature induced by Li adsorption is a rigid band-filling mechanism.

Density of states (DOSs) for the fully relaxed GmO monolayer and the $LiC_{6}O_{6}, Li_{2}C_{6}O_{6}$, and $Li_{2}C_{2}O_{2}$ structures are shown in Figure 10. The considered lithiated configurations have more states around the Fermi energy and are conductive, which is consistent with the reported band structure and desirable for a battery anode. The pure GmO monolayer does not have states at the Fermi energy but it has a small band gap. If each Li atom donates one electron to the GmO without introducing additional states, the Fermi level should increase into the conduction band of the GmO; for $LiC_{6}O_{6}$ and $Li_{2}C_{6}O_{6}$, when the DOS is normalized from the $C_{6}O_{6}$ to the $C_{2}O_{2}$ formula unit of GmO, this would correspond to raising the Fermi level to accommodate $\frac{1}{3}$ and $\frac{2}{3}$ electrons for Li and $Li_{2}$, respectively.

The DOSs are crudely consistent with this rigid band filling. To demonstrate this more clearly, the normalized planar averaged charge DOSs for $\frac{2}{3}$ unoccupied GmO states above the Fermi level and $\frac{2}{3}$ occupied $Li_{2}C_{6}O_{6}$ states below the Fermi level are shown in Figure 11. These two curves show almost identical charge distributions, demonstrating that Li effectively donates its electron to GmO, driving the semiconductor-to- metal transition. Overlap of the curves indicates prevalent ionic interaction between Li and the GmO monolayer while differences also show the presence of covalent behavior.

Li Transfer near the GmO Monolayer with the Nudged Elastic Band Method. The energy landscape, Figure 12, for Li transport near the GmO monolayer was obtained with the nudged elastic band $^{35}$ method as implemented in Quantum ESPRESSO. Transfer of Li through the GmO hollow is unlikely due to the large energy barrier of 4.3 eV (Figure 12a,b). Li transfer on the surface of the GmO monolayer, Figure 12c,d, from one H-site to the next H-site traverses the S-, B-, and S-sites, causing slight distortions of the GmO atoms nearby, with an energy barrier of 0.14 eV at the B- site. This reasonably small value suggests that this is a dominant path for diffusion of Li on the surface of GmO.

## CONCLUSIONS

DFT computations for the Li atom interaction with the GmO monolayer were performed for various $Li_{x}C_{y}O_{y}$ structures to determine if the monolayer of GmO can hold Li atoms and to predict the maximum theoretical capacity of this possible new anode material for Li-ion batteries. Our results show that, unlike the graphene monolayer, the GmO monolayer holds Li atoms by making covalent $Li−O$ bonds while Li donates its charge to the GmO layer. The preferred adsorption site for low concentrations of Li is the hollow site (H-site) of the carbon sublattice. The hollow site of the oxygen sublattice (S-site) may be preferable, however, for multilayer systems because the S-site can accommodate Li closer to the GmO plane.

The calculated results show that the formation energy per Li is more binding for lower concentrations, implying that the $Li−Li$ interaction will tend to keep them apart rather than clustering, similar to the situation for Li-intercalated graphite. This behavior may be of substantial benefit for fast charging in Li-ion−GmO batteries. The highest considered concentration

of Li in the $Li_2C_2O_2$ configuration has a superior charge capacity of 957 mAh/g that is 2.6 times higher than in graphite. Although this self-standing 2D structure has a slightly higher energy (by 0.06 eV/Li) than bulk lithium metal, previous theoretical studies of Li with graphene and graphite strongly suggest that multilayer structures such as $Li_2C_2O_2$ could exist, for example, the $Li_2C_6O_6$ configuration is energetically stable while an equivalent configuration for graphene $(Li_2C_6)$ is not.

Analysis of the band structure and DOSs confirms the conducting properties of the GmO-Li monolayer structures even at low Li concentrations for $Li_2C_{32}O_{32}$. Integration of the DOSs for different structures around the Fermi energy and analysis of the charge density redistribution demonstrate that a rigid-band filling argument is a reasonable first approximation, that is, Li can easily donate electrons—although not a full electron per Li because a fraction goes into the formation of the covalent bonds with oxygen—facilitating the formation of $Li^+$-ions leaving the GmO. This property makes GmO a good candidate as a battery anode material.

## AUTHOR INFORMATION
### Corresponding Author
Marija Gajdardziska-Josifovska − Department of Physics, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53211, United States; COnovate Inc., Milwaukee, Wisconsin 53211, United States; https://orcid.org/0000-0003-0702-872X;
Email: mgj@uwm.edu

### Authors
Danylo Radevych − Department of Physics, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53211, United States; https://orcid.org/0000-0002-3556-2850

Carol J. Hirschmugl − Department of Physics, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53211, United States; COnovate Inc., Milwaukee, Wisconsin 53211, United States

Michael Weinert − Department of Physics, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53211, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.1c01069

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This work was supported by the National Science Foundation (EFMA-1741673), (IIP-1843306).

## REFERENCES
(1) Mattson, E. C.; Pu, H.; Cui, S.; Schofield, M. A.; Rhim, S.; Lu, G.; Nasse, M. J.; Ruoff, R. S.; Weinert, M.; Gajdardziska-Josifovska, M.; et al. Evidence of Nanocrystalline Semiconducting Graphene Monoxide during Thermal Reduction of Graphene Oxide in Vacuum. ACS Nano 2011, 5, 9710−9717.

(2) Chen, J.; Gajdardziska-Josifovska, M.; Hirschmugl, C.; Mattson, E.; Pu, H.; Weinert, M. Synthesis and applications of graphene based nanomaterials. U.S. Patent 9,236,633 B2, 2016, Filed June 12th., 2013, Issued Jan. 12th., 2016.

(3) Pu, H. H.; Rhim, S. H.; Hirschmugl, C. J.; Gajdardziska-Josifovska, M.; Weinert, M.; Chen, J. H. Strain-induced band-gap engineering of graphene monoxide and its effect on graphene. Phys. Rev. B 2013, 87, 085417.

(4) Woo, J.; Yun, K.-H.; Chung, Y.-C. Graphene Monoxide Bilayer As a High-Performance on/off Switching Media for Nanoelectronics. ACS Appl. Mater. Interfaces 2016, 8, 10477−10482.

(5) Habibzadeh Mashatooki, M.; Sardroodi, J. J.; Ebrahimzadeh, A. R. Molecular Dynamics Investigation of the Interactions Between RNA Aptamer and Graphene-Monoxide/Boron-Nitride Surfaces: Applications to Novel Drug Delivery Systems. J. Inorg. Organomet. Polym. Mater. 2019, 29, 1252−1264.

(6) Pu, H. H.; Mattson, E. C.; Rhim, S. H.; Gajdardziksa-Josifovska, M.; Hirschmugl, C. J.; Weinert, M.; Chen, J. H. First-principles studies on infrared properties of semiconducting graphene monoxide. J. Appl. Phys. 2013, 114, 164313.

(7) Pu, H. H.; Rhim, S. H.; Hirschmugl, C. J.; Gajdardziska-Josifovska, M.; Weinert, M.; Chen, J. H. Anisotropic thermal conductivity of semiconducting graphene monoxide. Appl. Phys. Lett. 2013, 102, 223101.

(8) Woo, J.; Yun, K.-H.; Cho, S. B.; Chung, Y.-C. Defect-induced semiconductor to metal transition in graphene monoxide. Phys. Chem. Chem. Phys. 2014, 16, 13477−13482.

(9) Abraham, K. M. Prospects and Limits of Energy Storage in Batteries. J. Phys. Chem. Lett. 2015, 6, 830−844.

(10) Tarascon, J.-M.; Armand, M. Issues and challenges facing rechargeable lithium batteries. Nature 2001, 414, 359−367.

(11) Zhou, L.-J.; Hou, Z. F.; Wu, L.-M. First-Principles Study of Lithium Adsorption and Diffusion on Graphene with Point Defects. J. Phys. Chem. C 2012, 116, 21780−21787.

(12) Zhou, L.-J.; Hou, Z. F.; Wu, L.-M.; Zhang, Y.-F. First-Principles Studies of Lithium Adsorption and Diffusion on Graphene with Grain Boundaries. J. Phys. Chem. C 2014, 118, 28055−28062.

(13) Lee, E.; Persson, K. A. Li Absorption and Intercalation in Single Layer Graphene and Few Layer Graphene by First Principles. Nano Lett. 2012, 12, 4624−4628.

(14) Liu, M.; Kutana, A.; Liu, Y.; Yakobson, B. I. First-Principles Studies of Li Nucleation on Graphene. J. Phys. Chem. Lett. 2014, 5, 1225−1229.

(15) Thinius, S.; Islam, M. M.; Heitjans, P.; Bredow, T. Theoretical Study of Li Migration in Lithium-Graphite Intercalation Compounds with Dispersion-Corrected DFT Methods. J. Phys. Chem. C 2014, 118, 2273−2280.

(16) Taylor, D. Comprehensive Heterocyclic Chemistry III; Katritzky, A. R., Ramsden, C. A., Scriven, E. F., Taylor, R. J., Eds.; Elsevier: Oxford, 2008; pp 775−794.

(17) Dobrota, A. S.; Pašti, I. A.; Skorodumova, N. V. Oxidized graphene as an electrode material for rechargeable metal-ion batteries - a DFT point of view. Electrochim. Acta 2015, 176, 1092−1099.

(18) Giannozzi, P.; Baroni, S.; Bonini, N.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Chiarotti, G. L.; Cococcioni, M.; Dabo, I.; et al. QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials. J. Phys.: Condens. Matter 2009, 21, 395502.

(19) Giannozzi, P.; Andreussi, O.; Brumme, T.; Bunau, O.; Buongiorno Nardelli, M.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Cococcioni, M.; et al. Advanced capabilities for materials modelling with Quantum ESPRESSO. J. Phys.: Condens. Matter 2017, 29, 465901.

(20) Kokalj, A. XCrySDen-a new program for displaying crystalline structures and electron densities. J. Mol. Graphics Modell. 1999, 17, 176−179.

(21) Momma, K.; Izumi, F. VESTA 3for three-dimensional visualization of crystal, volumetric and morphology data. J. Appl. Crystallogr. 2011, 44, 1272−1276.

(22) Corso, A. D. Pseudopotentials periodic table: From H to Pu. Comput. Mater. Sci. 2014, 95, 337−350.

(23) Faglioni, F.; Merinov, B. V.; Goddard, W. A. Room-Temperature Lithium Phases from Density Functional Theory. J. Phys. Chem. C 2016, 120, 27104−27108.

(24) Hutcheon, M.; Needs, R. Structural and vibrational properties of lithium under ambient conditions within density functional theory. Phys. Rev. B 2019, 99, 014111.