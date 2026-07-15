# Competitive Adsorption on Wollastonite: An Atomistic Simulation Approach

T. K. Kundu and K. Hanumantha Rao*
Division of Mineral Processing, Luleå University of Technology, 971 87 Luleå, Sweden

S. C. Parker
School of Chemistry, University of Bath, Claverton Down, Bath BA2 7AY, United Kingdom

Received: February 2, 2005

Atomistic simulation techniques are used to simulate surface structure and adsorption behavior of scarcely floatable wollastonite mineral in the presence of molecular and dissociated water, methanoic acid, and methylamine. The latter two additives represent the two widely used collector head-group molecules. The static energy minimization code METADISE was used to perform the simulation to obtain pure surface energy and adsorption energy in the presence of added molecule. The hydroxylation was performed on those surfaces where low-coordinated silicon was made to saturate by bonding with hydroxyl group, and the subsequent charge neutralization was maintained by adding proton on single-coordinated surface oxygen. A comparison of surface energies revealed that all the surfaces become stabilized in the presence of added molecules; however, the presence of methylamine decreased the surface energy to lower values. Adsorption of dissociated water is preferred by the {100} and {102} surfaces, whereas the {001} surface preferred methylamine adsorption, because these show highly negative adsorption energies. In terms of molecular adsorption, the preferred adsorption sequence for all the surfaces is methylamine > methanoic acid > water without considering coadsorption. For the {100} and {102} surfaces, the adsorption energy values of carboxylic acid and amine are more negative than that of water and therefore we conclude that both carboxyl and amine head-group molecules adsorb preferably on wollastonite. Our simulation verify usability of carboxylic acid head group as widely used collectors for wollastonite flotation and, at the same time, it predicts the use of amine head-group collectors as possible modifiers, which corresponds well with our experimental findings.

## 1. Introduction

Wollastonite is a natural calcium metasilicate $(CaSiO_{3})$, formed by the metamorphism of siliceous limestone at temperatures of ~450 °C and higher, and usually occurs in high-grade regionally metamorphosed rocks and near igneous contact zones. $^{1}$ Wollastonite consumption recently has increased dramatically and is used mainly in resins and plastics as filler material, $^{2,3}$ as well as in other industrial products, $^{4,5}$ such as ceramics, metallurgy, paint, frictional products, and bio-material, $^{6}$ because of its chemical purity, low loss of ignition, high aspect ratio, and bright whiteness, coupled with its low thermal coefficient of expansion and fluxing capability. $^{7}$ Wollastonite is a rare example of a triclinic crystal with no symmetry elements. $^{8,9}$ Flotation separation of wollastinite is problematic from its associated minerals, because of its high dissolution tendency and consequent loss of surface $Ca^{2+}$ ions that can complex with fatty acid anionic collectors. Activation and depression of wollastonite with electrolytes result in some selectivity; however, the outcome is not optimum. For example, wollastonite is reported to be floatable from diopside-wollastonite mixtures by depressing diopside with tannic acid, using dodecylamine hydrochloride (DDA·HCl) at a pH range of 7.8−8.8. $^{10}$ Wollastonite−garnet mixtures are reported to be separable by depressing wollastonite using some acidic combination of depressant and flotation agent $(FeCl_{3}+$ sodium oleate). $^{11}$ The separation of wollastonite from quartz is of great industrial importance; however, it is troublesome, because of the similar physicochemical properties of the minerals. $^{12}$ We suppose that the difference in the crystal structures and the position of the constituent atoms and their geometrical, stereochemical, and electrostatic matching with the head group of the collector molecule is helpful for obtaining selective adsorption. We endeavor in this direction by using the static energy minimization technique METADISE $^{13}$ (minimum energy techniques applied to dislocation, interface, and surface energies) to illuminate various predominant Miller-indexed surface structures and their interaction behavior, with respect to water and the main functional group pertinent to collector molecules (namely, methanoic acid and methylamine). Not only in flotation but also in mineral-filled polymer composites, the surface structure has a great role, where it is treated with surface-modifying agents. Until now, there is no clear understanding about the atomic arrangements in wollastonite surfaces that affect collector−mineral interactions. Atomistic simulation is one of the techniques that can probe the surface at the atomic scale and track the additive molecules adsorption on the surface. It has been proven to be a successful and useful tool for constructing, interpreting, and predicting surface structures, $^{14-16}$ morphology, $^{17,18}$ and adsorption behavior. $^{19-21}$

In the following section, we will summarize the methodology that we have used for modeling surfaces, the approach for calculating surface energies, and the procedure followed for surface dissolution calculation. Surface structure, their reconstruction, and adsorption behavior are elaborated in the Results

* Author to whom correspondence should be addressed. Telephone: +46 920 491705. Fax: +46 920 497364. E-mail: Hanumantha.Rao@km.luth.se.

10.1021/jp0580367 CCC: $30.25  © 2005 American Chemical Society
Published on Web 05/13/2005

<table>
<caption>TABLE 1: Potential Energy Functions</caption>
<thead>
  <tr>
    <th>potentials</th>
    <th>expression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Coulombic</td>
    <td>$q_iq_j/(4\pi\epsilon_0r_{ij})$</td>
  </tr>
  <tr>
    <td>Buckingham</td>
    <td>$A_{ij}\exp(-r_{ij}/\rho_{ij}) - (C_{ij}/r_{ij}^6)$</td>
  </tr>
  <tr>
    <td>harmonic angle</td>
    <td>$k(\theta - \theta_0)^2/2$</td>
  </tr>
  <tr>
    <td>Lennard-Jones</td>
    <td>$F_{ij}r_{ij}^{-12} - G_{ij}r_{ij}^{-6}$</td>
  </tr>
  <tr>
    <td>Morse</td>
    <td>$D_{ij}[1 - \exp[-\alpha_{ij}(r_{ij} - r_{ij0})]]$</td>
  </tr>
</tbody>
</table>

and Discussion section. We have recently presented the wollastonite dissolution phenomenon. $^{22}$

### 2. Methodology
The ideal approach to determine the structure and bonding in a silicate mineral would be by direct solution of the Schrödinger equation, which addresses all atoms and electrons. The complexity of such a calculation makes it computationally prohibitive for all except very simple systems or those containing small fragments of a few tens of atoms. Atomistic simulations provide an alternative strategy to calculate the interaction between individual atoms and molecules, using simple parametrized analytical functions, named as the potential model.

The interaction energies between pairs or groups of atoms include several components. The largest component is due to the long-range Coulomb energy, which describes the electrostatic interaction between charges. Additional contributions of short distance range described by Buckingham and Lennard-Jones potentials are incorporated, which arise from the repulsion between neighboring charge clouds, the van der Waals attraction, and electronic polarizability. Bond stretching terms for organic molecules is included using Morse potential obtained from the InsightII cvff force field package. The electronic polarizability is particularly important for modeling highly polarizable anions such as oxygen in our case. It is defined using the shell model, $^{23}$ where the polarizable ion is represented by a mass-less shell attached to a core by a harmonic spring and the polarizability is expressed as $\alpha = Y^2/K$, where $\alpha$, $Y$, and $K$ are ionic polarizability, shell charge, and spring constant respectively and these are obtained by fitting experimental dielectric data. For covalently bonded molecules and polyanions, three-body harmonic potential and torsion forces are included as a final contribution to interaction energy. The functional forms of the potential and the parameters used are given in Tables 1−4, where $q_i$ an $q_j$ are the charges of ions $i$ and $j$ separated by a distance $r_{ij}$, and $A_{ij}$, $\rho_{ij}$, $F_{ij}$, $G_{ij}$, $D_{ij}$, $\alpha_{ij}$, $C_{ij}$, and $r_{ij0}$ are variable parameters. The method for obtaining the parameters is to fit the parameters empirically to reproduce experimental data. These data can include a range of properties, principally, the crystallographic structure and elasticity. $^{24}$ In mineral systems, there is often insufficient experimental data to be used for fitting potential parameters. Transferability of potential parameters adopted in an atomistic simulation is a useful concept and it has been proven to be highly successful for modeling silicate minerals. $^{25}$ The methodology that we have used to model surface structure and stability is based on the Tasker approach, $^{26}$ where the crystal is considered to be a series of charged planes lying parallel to the surface and periodic in two dimensions. The energy minimization code (METADISE) models the crystal as having two blocks, each comprising two regions, regions I and II, which are periodic in two dimensions lateral to the surface. The ions in region I, representing the surface layer and a few layers immediately below, are allowed to relax to their mechanical equilibrium, whereas those in region II, which represent the rest of the crystal, is kept fixed at their bulk equilibrium position, although region II, as a whole, is allowed to move with respect to region I. To ensure convergence of the energies, both regions I and II need to be sufficiently large. The two blocks together simulate the bulk of the crystal, whereas a single block represents the surface with the top of region I as the free surface cut. The sum of the energies of interaction between all the atoms gives the energies of the blocks. The long-range Coulombic interactions are calculated by the Parry method, $^{27,28}$ which is a special case of the Ewald method, $^{29}$ by considering the crystal to be composed of a series of charged planes, of infinite size, that terminate at a surface. This leads to three types of surfaces, as identified by Tasker: $^{30}$ types I, II, and III. In type I surfaces, the stacking plane is neutral and is composed of both cations and anions in a stoichiometric ratio with no dipole perpendicular to the surface. Type II surfaces contain a series of charged planes that comprise a repeat unit, which has no dipole perpendicular to the surface. Type III surfaces are composed of alternately charged planes that produce a dipole perpendicular to the surface if there is a cut between any planes. The Coulombic sum for such a surface cannot be evaluated, because it is divergent. $^{31}$ If such surfaces are to be studied, then the surface must be reconstructed such that the dipole is canceled. $^{32}$ The surface energy, which is an indication of the stability of a surface, is evaluated from the energy of the surface block of the crystal ($U_s$), the energy of an equal number of bulk ions ($U_b$), and the surface area ($A$), which are obtained using the METADISE computer code as follows:

$$
\gamma = \frac{U_{\mathrm{s}} - U_{\mathrm{b}}}{A} \tag{1}
$$

<table>
<caption>TABLE 2: Interacting Ions</caption>
<thead>
  <tr>
    <th rowspan="2">ion<sup>a</sup></th>
    <th rowspan="2">mass (amu)</th>
    <th colspan="2">Atomic Charge (e)</th>
    <th rowspan="2">$K$ (eV/Å²)</th>
  </tr>
  <tr>
    <th>core</th>
    <th>shell</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Si</td>
    <td>28.09</td>
    <td>+4.0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>H</td>
    <td>1.008</td>
    <td>+0.4</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>O</td>
    <td>15.99</td>
    <td>+0.848</td>
    <td>−2.848</td>
    <td>74.92038</td>
  </tr>
  <tr>
    <td>O<sub>h</sub></td>
    <td>15.99</td>
    <td>+0.90</td>
    <td>−2.30</td>
    <td>74.92038</td>
  </tr>
  <tr>
    <td>O<sub>w</sub></td>
    <td>15.99</td>
    <td>+1.25</td>
    <td>−2.05</td>
    <td>209.4496</td>
  </tr>
  <tr>
    <td>C<sub>f</sub></td>
    <td>12.01</td>
    <td>+0.31</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>O<sub>IC</sub></td>
    <td>15.99</td>
    <td>−0.38</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>O<sub>fH</sub></td>
    <td>15.99</td>
    <td>−0.38</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>H<sub>IC</sub></td>
    <td>1.008</td>
    <td>+0.1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>H<sub>fO</sub></td>
    <td>1.008</td>
    <td>+0.35</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>N</td>
    <td>14.007</td>
    <td>−0.5</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>C<sub>a</sub></td>
    <td>12.01</td>
    <td>−0.08</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>H<sub>aC</sub></td>
    <td>1.008</td>
    <td>+0.1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>H<sub>aN</sub></td>
    <td>1.008</td>
    <td>=0.14</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

<sup>a</sup> Legend is as follows: O, O<sub>h</sub>, O<sub>w</sub> denotes oxygen of wollastonite, hydroxyl, and water, respectively; H represents the hydrogen of hydroxyl and water; C<sub>f</sub> and C<sub>a</sub> represent carbon of methanoic acid and methylamine, respectively; O<sub>IC</sub> and O<sub>fH</sub> represent oxygen of methanoic acid connected via a double bond and a single bond, respectively, to C<sub>f</sub> ; H<sub>IC</sub> and H<sub>fO</sub> denotes hydrogen of methanoic acid connected to C<sub>f</sub> and O<sub>fH</sub>, respectively; N represents nitrogen of methylamine; and H<sub>aC</sub> and H<sub>aN</sub> denote hydrogen of methylamine connected to C<sub>a</sub> and N, respectively.

<table>
<caption>TABLE 3: Harmonic Angle Potential Parameters for Interacting Ions</caption>
<thead>
  <tr>
    <th>interacting ions</th>
    <th>$k$ (eV/rad)</th>
    <th>$\theta_0$ (degrees)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>O<sub>h</sub>/O−Si−O/O<sub>h</sub></td>
    <td>2.09724</td>
    <td>109.47</td>
  </tr>
  <tr>
    <td>H−O<sub>w</sub>−H</td>
    <td>4.19978</td>
    <td>108.69</td>
  </tr>
  <tr>
    <td>H<sub>fO</sub>−O<sub>fH</sub>−C<sub>f</sub></td>
    <td>4.29</td>
    <td>112.0</td>
  </tr>
  <tr>
    <td>H<sub>IC</sub>−C<sub>f</sub>−O<sub>fH</sub></td>
    <td>4.72</td>
    <td>110.0</td>
  </tr>
  <tr>
    <td>H<sub>IC</sub>−C<sub>f</sub>−O<sub>IC</sub></td>
    <td>4.72</td>
    <td>120.0</td>
  </tr>
  <tr>
    <td>O<sub>fH</sub>−C<sub>f</sub>−O<sub>IC</sub></td>
    <td>12.45</td>
    <td>123.0</td>
  </tr>
  <tr>
    <td>H<sub>aN</sub>−N−C<sub>a</sub></td>
    <td>1.71</td>
    <td>106.4</td>
  </tr>
</tbody>
</table>

<sup>a</sup> See Table 2 footnote for a description of the legend of symbols.

<table>
<caption>TABLE 4: Potential Parameters Used</caption>
<thead>
<tr>
<th>interacting ions</th>
<th>$A_{ij}$ (eV)</th>
<th>$\rho_{ij}$ (Å)</th>
<th>$C_{ij}$ (eV Å⁶)</th>
<th>$F_{ij}$ (eV Å¹²)</th>
<th>$G_{ij}$ (eV Å⁶)</th>
<th>$D_{ij}$ (eV)</th>
<th>$\alpha_{ij}$ (Å⁻¹)</th>
<th>$r_{ij_0}$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si−Oh</td>
<td>983.907</td>
<td>0.321</td>
<td>10.662</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Si−O/Ow</td>
<td></td>
<td></td>
<td>10.662</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−O</td>
<td></td>
<td></td>
<td>27.88</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ca−O</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ca−Oh</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ca−Ow</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−Oh</td>
<td></td>
<td></td>
<td>13.94</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−Ow</td>
<td></td>
<td></td>
<td>28.92</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−H</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Oh−H</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td>7.05</td>
<td>3.17</td>
<td>0.94</td>
</tr>
<tr>
<td>Oh−Oh</td>
<td></td>
<td></td>
<td>6.97</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−Ow</td>
<td></td>
<td></td>
<td>28.92</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ow−H</td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td>6.20</td>
<td>2.22</td>
<td>0.92</td>
</tr>
<tr>
<td>Ca−O<sub>fC</sub>/O<sub>fW</sub></td>
<td></td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−O<sub>fC</sub>/O<sub>fH</sub></td>
<td></td>
<td></td>
<td></td>
<td>23430.0</td>
<td>32.12</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−H<sub>fC</sub>/O<sub>fO</sub></td>
<td></td>
<td></td>
<td></td>
<td>5600.0</td>
<td>12.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−C<sub>f</sub>/C<sub>a</sub></td>
<td></td>
<td></td>
<td></td>
<td>87327.5</td>
<td>56.32</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O<sub>fC</sub>/O<sub>fH</sub>−O<sub>fC</sub>/O<sub>fH</sub></td>
<td></td>
<td></td>
<td></td>
<td>11822.6</td>
<td>21.61</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O<sub>fC</sub>/O<sub>fH</sub>−C<sub>f</sub></td>
<td></td>
<td></td>
<td></td>
<td>38994.3</td>
<td>35.23</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O<sub>fC</sub>/O<sub>fH</sub>−H<sub>fC</sub>/H<sub>fO</sub></td>
<td></td>
<td></td>
<td></td>
<td>1908.1</td>
<td>5.55</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>C<sub>f</sub>−H<sub>fC</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.66</td>
<td>1.77</td>
<td>1.10</td>
</tr>
<tr>
<td>C<sub>f</sub>−O<sub>fC</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>6.22</td>
<td>2.06</td>
<td>1.23</td>
</tr>
<tr>
<td>C<sub>f</sub>−O<sub>fH</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.29</td>
<td>2.00</td>
<td>1.37</td>
</tr>
<tr>
<td>H<sub>fO</sub>−O<sub>fH</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.08</td>
<td>2.28</td>
<td>0.96</td>
</tr>
<tr>
<td>Ca−N</td>
<td>663.26</td>
<td>0.337</td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−H<sub>aC</sub>/H<sub>aN</sub></td>
<td></td>
<td></td>
<td></td>
<td>5600.0</td>
<td>12.0</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>O−N</td>
<td></td>
<td></td>
<td></td>
<td>67528.4</td>
<td>50.45</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>N−Ca</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2.95</td>
<td>2.29</td>
<td>1.47</td>
</tr>
<tr>
<td>Ca−H<sub>aC</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.71</td>
<td>1.77</td>
<td>1.11</td>
</tr>
<tr>
<td>N−H<sub>aN</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3.82</td>
<td>2.28</td>
<td>1.03</td>
</tr>
</tbody>
</table>

$^{a}$ See Table 2 footnote for a description of the legend of symbols. Note that the shell is the interacting part for the oxygen ion.

The adsorption energies ($U_{\text{ads}}$) were calculated by comparing the energy of the pure surface ($U_{\text{s}}$) and that of an isolated adsorbed molecule ($U_{\text{mol}}$) with the energy of the covered surface ($U_{\text{def}}$), as given below:

$$
U_{\text{ads}} = U_{\text{def}} - (U_{\text{s}} + U_{\text{mol}}) \tag{2}
$$

We have considered the most-common, low-energy, low-Miller-indexed surfaces and these are close-packed planes with large interplannar spacing. The final structure and energy is achieved by allowing the ions in the surface region to relax to the point where they experience zero force. Defects (unsaturated atoms) and impurities (added molecules) are accommodated in the surface as we assume periodic boundary conditions, while maintaining charge neutrality, because, otherwise, Coulombic energy would be divergent if the repeat cell is charged. In the calculation of the surface energy for a particular Miller index, there may be multiple unique units. In these cases, each case is considered separately and the surface energy corresponding to the lowest energy cut is reported in the paper. The simulation of the hydroxylated surfaces was achieved by adsorbing dissociated water molecules onto surface cation−oxygen pairs in such a way that the OH species was bonded to a surface cation and the H atom was bonded to a surface O atom. Two hydroxyl groups, i.e., in Kröger−Vink³³ notation, can be used to consider this as the replacement of surface oxygen with hydroxyl ions:

$$
\text{H}_2\text{O} + \text{O}_{\text{O}}^{\text{x}} \rightarrow (\text{OH})_{\text{O}}^{\bullet} + (\text{OH})_{\text{i}}^{\prime} \tag{3}
$$

where $\text{O}_{\text{O}}^{\text{x}}$ is an oxygen at a lattice oxygen site with zero charge, with respect to the lattice oxygen, $(\text{OH})_{\text{O}}^{\bullet}$ is a hydroxyl group at an oxygen lattice site with a charge of +1, and $(\text{OH})_{\text{i}}^{\prime}$ is a hydroxyl group at an interstitial site with a charge of −1. For hydration energy calculation we required a value for the energy of dissociation of a water molecule:

$$
\text{H}_2\text{O} + \text{O}_{(g)}^{2-} \rightarrow 2\text{OH}_{(g)}^{-} \tag{4}
$$

However, this requires the material-dependent second electron affinity of oxygen,³⁴ and this can be obtained using experimental heats of formation of metal hydroxide from wollastonite and water. Knowing the lattice energies of wollatonite, $\text{Ca(OH)}_2$, and $\text{Si(OH)}_4$, and with the Hess law of thermodynamic calculation, we came up to the dissociation energy value of water on wollastonite of reaction 4 to be −8.10 eV.

In the case of adsorption energy calculation, where there are more than one adsorbate on the chosen unit surfaces, adsorbate−adsorbate interactions are only of the electrostatic type.

### 3. Results and Discussion

3.1. Surfaces of Pure and Reconstructed Wollastonite. In our simulation, we have modeled the low-temperature polymorph α-wollastonite, which has a triclinic crystal structure with space group $P\overline{1}$.⁸,³⁵,³⁶ We have used a unit cell with parameters of $a = 7.93$ Å, $b = 7.32$ Å, $c = 7.07$ Å, $\alpha = 90.05^\circ$, $\beta = 95.22^\circ$, and $\gamma = 103.43^\circ$.³⁷ Using the potential model described, the bulk crystal was then allowed to relax to a minimum energy configuration, giving $a = 8.00$ Å, $b = 7.43$ Å, and $c = 7.12$ Å, with angles of $\alpha = 90.39^\circ$, $\beta = 93.57^\circ$, and $\gamma = 103.74^\circ$. It has a perfect cleavage plane of {100}, and the other good cleavage planes are {001} and {102}. Here, we have modeled all these three low-indexed planes. Table 5 summarizes the surface energies of the lowest energy cut after performing surface reconstruction, mainly transferring a single lone oxygen with calcium and, in the case of double lone oxygens, both of them are transferred to a lower layer, along with one Si atom. The charge and dipole free cuts are obtained using a layer peeling and stacking process that was performed by METADISE and subsequent energy minimization.

<table><caption>TABLE 5: Surface Energies and Adsorption Energies for Water, Hydroxyl, Methanoic Acid, and Methylamine on Low-Energy Pure Wollastonite Surfaces</caption>
<thead>
<tr>
<th rowspan="2">surface</th>
<th colspan="5">Surface Energy (J/m²)<sup>a</sup></th>
<th colspan="4">Adsorption Energy (kJ/mol)<sup>b</sup></th>
</tr>
<tr>
<th>SE<sub>P</sub></th>
<th>SE<sub>W</sub></th>
<th>SE<sub>H</sub></th>
<th>SE<sub>M</sub></th>
<th>SE<sub>A</sub></th>
<th>AE<sub>W</sub></th>
<th>AE<sub>H</sub></th>
<th>AE<sub>M</sub></th>
<th>AE<sub>A</sub></th>
</tr>
</thead>
<tbody>
<tr>
<td>{100}</td>
<td>0.72</td>
<td>0.44</td>
<td>0.69</td>
<td>0.43</td>
<td>0.40</td>
<td>−87.4</td>
<td>−462.23</td>
<td>−92.43</td>
<td>−100.88</td>
</tr>
<tr>
<td>{001}</td>
<td>1.42</td>
<td>1.18</td>
<td>0.46</td>
<td>1.02</td>
<td>-0.28</td>
<td>−85.34</td>
<td>−232.41</td>
<td>−139.92</td>
<td>−593.34</td>
</tr>
<tr>
<td>{102}</td>
<td>1.33</td>
<td>1.22</td>
<td>1.76</td>
<td>1.20</td>
<td>1.19</td>
<td>−93.23</td>
<td>−418.27</td>
<td>−102.18</td>
<td>−109.78</td>
</tr>
</tbody>
</table>

<sup>a</sup> SE<sub>P</sub>, SE<sub>W</sub>, SH<sub>H</sub>, SE<sub>M</sub>, and SE<sub>A</sub> denote the surface energy for pure wollastonite surfaces and wollastonite surfaces that contain water, hydroxyl, methanoic acid, and methylamine, respectively. <sup>b</sup> AE<sub>W</sub>, AE<sub>H</sub>, AE<sub>M</sub>, and AE<sub>A</sub> denote the adsorption energy for wollastonite surfaces that contain water, hydroxyl, methanoic acid, and methylamine, respectively.

![](./images/812276096081854465_1.jpg)

Figure 1. Side view of the wollastonite {100} surface, showing three tetrahedral repeat units parallel to the b-axis, one protruding upward and other two downward. Color keys: Ca = green, O = red, Si = gray tetrahedral.

In most of the Miller-indexed planes before minimization, the surfaces consist of low-coordinated silicon (with a coordination number of 2 or 3) mixed with usually four-coordinated silicon, low-coordinated (coordination numbers of 3, 4, and 5) calcium, along with nonbonded and/or dangling oxygen. After minimization, much surface reconstruction occurs, whereby some bonds are broken and more new bonds are formed, to have a minimum energy configuration. In this process, near-surface-region atoms have a tendency to have a similar or the same bulk coordination. In plane {100}, the fresh knife cut from the bulk before minimization leads to a surface that has CaO and SiO₂ clusters that consist of one Si atom connected to two O atoms and one nonbonded oxygen, per unit-cell surface area. After minimization, two-coordinated surface silicons bonded to the lone oxygen and with lower-layer silicon via its oxygen. On the other hand, oxygen that was connected to the lower layer silicon formed a bond with the top silicon. Finally, the surface consists of two edge-shared surface silicons that have a coordination number of five, and this surface corresponds to a minimum energy surface without performing any surface reconstruction. It does not depict the actual wollastonite surface, because this surface ends up having edge-shared silicon pentagon. We have searched for a surface cut that has four-coordinated surface silicon of neutral and dipole free before minimization. Here, we have a lone oxygen on the surface and transferred it along with surface calcium to the lower layer and performed energy minimization. The final surface configuration is shown in Figure 1. There are three repeating Si−O tetrahedron units running parallel to the b-axis. Of these three tetrahedrons, two remain parallel to the top surface, whereas the third one protrudes upward and, thus, making a rift-and-valley-type surface configuration. The top Ca atom remains between two side-by-side parallel running chains that were connected to four O atoms, at a distance of 2.25−2.41 Å. The distance between two Ca atoms is 7.43 Å, and, thus, we conclude one Ca atom remains on top of the surface per unit surface area. On the surface, the exposed atoms (and, thus, accessible to foreign adsorbing molecules) are mainly oxygen and calcium, whereas silicon is shielded by oxygen. In the surface region, the distance between silicon and oxygen in tetrahedron is within 1.60−1.67 Å and the minimum oxygen−oxygen distance belonging to two chains running parallel to the b-axis is 3.18 Å. As shown in Table 5, this is the lowest-energy surface in pure form and it corresponds to the perfect cleavage plane, as reported in the literature.

For the {001} surface, we have one surface cut that has all four-coordinated Si atoms without any lone oxygen. The energy

![](./images/812276096081854465_2.jpg)

Figure 2. Side view of the wollastonite {001} surface, showing three repeating tetrahedral units, parallel to the b-axis (two protrude upward and one protrudes downward). Color keys: Ca = green, O = red, Si = gray tetrahedral.

![](./images/812276096081854465_3.jpg)

Figure 3. Side view of the wollastonite {102} surface. Color keys: Ca = green, O = red, Si = gray tetrahedral.

minimized surface configuration is shown in Figure 2, and the surface energy value is tabulated in Table 5. This surface is similar to the {100} surface, where chains are in parallel to the b-axis but two out of three repeating Si−O tetrahedra protrude upward and the Ca atom between them constitutes a ridge, whereas the third tetrahedron is oriented downward, keeping its base parallel to the surface, and constitutes the valley region. Here, the exposed surface consists of calcium and oxygen, and the silicon is shielded by oxygen.

The fresh-cut neutral and dipole-moment-free {102} surface had two lone oxygens and two 3-coordinated silicons connected in chains. We transferred two lone oxygens, along with the silicon, to the lower layer to keep the surface charge-free. In this manner, the surface consists of one 3-coordinated Si atom with one lone oxygen. This configuration, and the other where we have transferred the remaining lone oxygen and calcium, is energy-minimized. However, the former reconstruction shows less surface energy than the latter as the 3-coordinated silicon bonded with the lone oxygen and all surface silicon and oxygen acquire bulk coordination status. The surface configuration after energy minimization is shown in Figure 3. This surface shows silicon, along with calcium and oxygen. In the surface layer, two of the top Ca atoms are connected to three and four O atoms, respectively keeping a distance between 2.09 Å and 2.75 Å. Here, the chain axis is not parallel to the top surface, and although it does not produce well-defined ridge and valleys, the surface is not smooth on an atomic scale.

3.2. Adsorption of Water on Pure Surfaces. The adsorption of water stabilizes all three surfaces, as revealed by the decrease in surface energies presented in Table 5. One water molecule per unit cell area was placed at a distance of 1.85 Å between the top surface calcium and the oxygen of water, and at a distance of 1.74 Å between the top oxygen of the wollastonite surface and the hydrogen of water. After minimization, the distance between these atoms became 2.34 and 1.55 Å, respectively, as shown in Figure 4. Water is thus bonded with one of its hydrogens to wollastonite oxygen by hydrogen bonding. Water on the {001} surface was placed at a distance of 1.63 Å between the hydrogen and the crystal oxygen. The energy-minimized structure is shown in Figure 5, where water is adsorbed on a flat orientation with distances of 1.94 and 2.19 Å between two hydrogens of water with two protruding crystal

![](./images/812276096081854465_4.jpg)

Figure 4. Side view of water adsorption on the wollastonite {100} surface, where water is shown as space filled and the crystal as Si tetrahedral unit and oxygen and calcium as balls. Color keys: Ca = green, O = red, Si = gray, H = white.

![](./images/812276096081854465_5.jpg)

Figure 5. Side view of water adsorption on wollastonite {001} surface where water is shown as space filled and the crystal as Si tetrahedral unit and oxygen and calcium as balls. Color keys: Ca = green, O = red, Si = gray, H = white.

oxygens. Water on this surface stabilizes the surface slightly, and more water adsorption per unit cell is needed for full stabilization. On the {102} surface, the water molecule was placed by keeping the oxygen of water at a distance of $1.38\ \mathrm{\mathring{A}}$ away from the surface top calcium and the assembly was energy-minimized. Water does not stabilize this surface too much, because the decrease in surface energy is much less; however, the negative hydration energy indicates that water adsorption is spontaneous. Here, one of the hydrogens of water is located at a hydrogen bond distance from the surface oxygen, whereas the other hydrogen is kept away from the surface. This perpendicular type of water adsorption in a relaxed structure is shown in Figure 6. The oxygen of water bends toward the surface calcium, maintaining a distance of $2.38\ \mathrm{\mathring{A}}$ between the two atoms.

### 3.3. Adsorption of Dissociated Water on Pure Surfaces.
While grinding wollastonite, the possible exposed sites with broken bonds are $-\mathrm{O}-\mathrm{Si}^{+}$ and $-\mathrm{O}-\mathrm{Ca}^{+}$, which are electron-pair acceptors (Lewis acids) and $-\mathrm{Si}-\mathrm{O}^{-}$ and $-\mathrm{Ca}-\mathrm{O}^{-}$, which are electron-pair donors or bases. $^{38}$ It is plausible that $\mathrm{Si}-\mathrm{O}$ bonds along the chain direction have a stronger linkage energy, of partial covalent nature, than $\mathrm{Ca}-\mathrm{O}$ bonds between chains, which are weak ionic bonds. $^{11}$ Thus, $\mathrm{Ca}-\mathrm{O}$ bonds break off earlier than $\mathrm{Si}-\mathrm{O}$ bonds. As a result, the crystal preferentially cleaves along the planes of high silicon content, so that the exposed surface are probably closer to $-\mathrm{O}-\mathrm{Si}^{+}$ and $-\mathrm{Si}-\mathrm{O}^{-}$. In aqueous media, $\mathrm{H}^{+}$ was attracted to $-\mathrm{Si}-\mathrm{O}^{-}$ and $\mathrm{OH}^{-}$ was attracted toward $-\mathrm{O}-\mathrm{Si}^{+}$ while making the surface charge neutral. Here, we have followed the procedure as in eqs 3 and 4 for surface hydroxylation, where $\mathrm{OH}^{-}$ is added to low-coordinated silicon on a fresh-cut surface, and $\mathrm{H}^{+}$ is attached to a dangling oxygen. Lone oxygen, if present, is transferred, along with equivalent charged calcium, to the bottom of the surface, to make the surface more realistic.

![](./images/812276096081854465_6.jpg)

Figure 6. Side view of the water adsorption on the wollastonite {102} surface, where water is shown as space filled, the crystal is shown as an Si tetrahedral unit, and oxygen and calcium are shown as balls. Color keys: Ca = green, O = red, Si = gray, H = white.

Table 5 summarizes the surface energy and reaction energy for hydroxylation on the three predominant wollastonite surfaces discussed here. Hydroxylation stabilizes all the surfaces, as evident from the lower surface energy in the presence of a hydroxyl group than pure surfaces, and highly negative reaction energy is indicative of a high tendency toward hydroxylation. For {100} surfaces, the decrease in surface energy is minute but the reaction energy is highly negative, because its surface conformation resembles that of the bulk and the coordinate saturation tendency is highest in the presence of dissociated water, as shown in Figure 7. Here, the hydroxyl ions are the isolated type, because they are $>2.98\ \mathrm{\mathring{A}}$ away from each other. Hydrogen bends toward the bridging oxygen and keeps a minimum distance of $2.75\ \mathrm{\mathring{A}}$ between the atoms. Surface characteristics of hydroxylated {001} are similar to that of hydroxylated {100} surface; however, in this case, the surface energy value decreased by almost 3-fold. On the {102} surface, the hydroxyl ions are of the isolated type, with a minimum interaction distance of $2.67\ \mathrm{\mathring{A}}$ between the atoms. Here, the chains are broken and two $\mathrm{Si}-\mathrm{O}$ tetrahedral that contain one hydroxyl ion each remain as an isolated group, whereas three silicons make one full ring with oxygen between the atoms. One of the silicons in this ring is in the 5-coordinated state and the remaining silicons are edge-shared with the nearby tetrahedra. The hydroxylated surface assembly is shown in Figure 8.

### 3.4. Adsorption of Methanoic Acid on Pure Surfaces.
Methanoic acid was placed on a reconstructed low-energy {100} surface with its double-bonded oxygen $(\mathrm{O}_{\mathrm{fc}})$ at a distance of $1.42\ \mathrm{\mathring{A}}$ away from the surface calcium. Methanoic acid stabilizes the surface, and its adsorption energy is more negative than pure water adsorption but less negative than the dissociative water adsorption. Thus, methanoic acid will be able to replace adsorbed water but not in an acidic or alkaline environment. The energy-minimized assembly is shown in Figure 9, where the double-bonded oxygen $(\mathrm{O}_{\mathrm{fc}})$ of methanoic acid is adsorbed

![](./images/812276096081854465_7.jpg)

Figure 7. Perspective view of dissociative water adsorption on the wollastonite {100} surfac, all shown as space filled. Color keys: Ca = green, O = red, Si = gray, $O_{hydroxyl}$ = sky blue, H = white.

![](./images/812276096081854465_8.jpg)

Figure 8. Top view of hydroxylated {102} wollastonite surface showing isolated Si−O−OH group as space filled, surface Si−O rings as ball-and-sticks and underlying chains as Si tetrahedral unit with calcium and crystal as balls. Color keys: Ca = green, O = red, Si = gray, $O_{hydroxyl}$ = sky blue, H = white.

at a distance of 2.18 Å away from the surface calcium and its hydrogen ($H_{fo}$) is adsorbed at a distance of 2.44 Å away from the surface oxygen. The methanoic acid is on the ridge portion and covers all exposed top Ca atoms. Methanoic acid had been placed on the {001} wollastonite surface, by keeping its double-bonded oxygen ($O_{fc}$) at a distance of 1.54 Å away from the surface calcium and the assembly was energy-minimized. This phenomenon stabilized the surface and the adsorption energy is more negative than that for pure water adsorption, as seen in Table 5. As shown in Figure 10, the methanoic acid molecule lies flat on the surface and it adsorbs with its two oxygens ($O_{fc}$ and $O_{fh}$) with two surface calciums that were 2.17 and 2.94 Å apart, respectively. Hydrogen ($H_{fo}$) bends toward the surface oxygen and the distance between them was 2.71 Å. Methanoic acid was placed on the {102} surface at a distance of 1.46 Å between the double-bonded oxygen ($O_{fc}$) and surface calcium, and then energy minimization was conducted. This stabilizes the surface, and its adsorption energy is more negative than that of pure water adsorption but less negative than that of dissociated water adsorption. The energy-minimized adsorption assembly is shown in Figure 11, where the double-bonded oxygen ($O_{fc}$) is connected to the surface calcium that had a distance of 2.30 Å between the atoms. Hydrogen ($H_{fo}$) interacts with two surface oxygens and orients itself 2.63 and 3.01 Å away from them. Almost 20% of the exposed Ca atom is covered by one methanoic acid per unit-cell surface area.

3.5. Adsorption of Methylamine on Pure Surfaces. Me- thylamine adsorption stabilizes all the wollastonite surfaces, and,

![](./images/812276096081854465_9.jpg)

Figure 9. Side view of methanoic acid adsorption on wollastonite {100} surface shown as space filled. Color keys: Ca = green, O = red, Si = gray, C = blue, O(methanoic acid) = violet, H = white.

![](./images/812276096081854465_10.jpg)

Figure 10. Top view of methanoic acid adsorption on the wollastonite {001} surface, shown as space filled. Color keys: Ca = green, O = red, Si = gray, C = blue, O(methanoic acid) = violet, H = white.

![](./images/812276096081854465_11.jpg)

Figure 11. Side view of methanoic acid adsorption on the wollastonite {102} surface, shown as space filled. Color keys: Ca = green, O = red, Si = gray, C = blue, O(methanoic acid) = violet, H = white.

for the {001} surface, the surface energy is negative and the adsorption energy is also highly negative, compared to other surfaces. For the {100} surface, methylamine was arranged on the surface so that the hydrogen connected to the nitrogen $(H_{aN})$ is 1.82 Å away from the surface oxygen and the $-CH_3$ component is perpendicular to the surface and the resulting assembly was energy-minimized. The relaxed surface structure is shown in Figure 12, where methylamine adsorbs by keeping its C−N bond parallel to the ridge region of the wollastonite surface. The distances between the surface calcium and nitrogen, and the two hydrogens of methylamine that are attached to carbon $(H_{aC})$ with two surface oxygens, are 2.75, 2.75, and 2.69 Å, respectively. The two H atoms that are connected to nitrogen $(H_{aN})$ are kept away from the surface without interaction with the surface atoms. Methylamine on the {001} surface was placed with its hydrogen connected to nitrogen $(H_{aN})$ at a distance of 1.35 Å away from the surface oxygen. After energy minimization, the configuration of the assembly is shown in Figure 13. The tendency of methylamine to adsorb is stronger, as revealed by the huge negative adsorption energy. Here, the C−N bond remains parallel to the surface and the molecule occupies one valley region of the surface. Methylamine did not form any valence bond here but was attracted by dispersive forces with two surface calciums that had a distance of 2.84 and 3.06 Å between them. One hydrogen that was attached to nitrogen $(H_{aN})$ remains in the same plane of C−N, and the interacting distance between this and one surface oxygen is 3.07 Å. The other $H_{aN}$ atom remains away from the surface. One hydrogen that was connected to the carbon atom of the methylamine molecule $(H_{aC})$ is situated between two surface oxygens by a distance of 2.53 and 2.80 Å from each of them. Keeping its N atom at 2.10 Å away from the surface calcium, methylamine was placed on the wollastonite {102} surface and the assembly was subjected to energy minimization. This shows surface stabilization, and the adsorption energy is similar to that of methanoic acid adsorption. Methlyamine adsorbs on the valley region of the surface with its C−N axis between the grooves of two sets of parallel running exposed surface calcium, as shown in Figure 14. The nitrogen is 3.01 and 3.75 Å away from two surface calciums. Two of the three hydrogens connected to carbon $(H_{aC})$ are 2.52 and 2.61 Å away from two surface oxygens, and a hydrogen connected to nitrogen $(H_{aN})$ is 2.76 Å away from one surface calcium, whereas the other hydrogen $(H_{aN})$ is kept away from the surface.

![](./images/812276096081854465_12.jpg)

Figure 12. Side view of methylamine adsorption on the wollastonite {100} surface shown, as space filled. Color keys: Ca = green, O = red, Si = gray, C = blue, N = yellow, H = white.

## 4. Conclusions
We have used a static energy minimization code (minimum energy techniques applied to dislocation, interface, and surface energies, METADISE) to obtain three morphologically pre-dominant wollastonite surfaces. The potential parameters used in this simulation study predict crystal unit-cell parameters satisfactorily. In a comparison of surface energies in the presence of added molecules, we noticed that, in all cases, the adsorption stabilized the wollastonite surface and methylamine was the best candidate. Among the added molecules, dissociated water adsorption shows the lowest adsorption energy on the {100} and {102} surfaces, whereas methylamine shows the least adsorption energy on the {001} surface. Thus, if all the

![](./images/812276096081854465_13.jpg)

Figure 13. Perspective view of the wollastonite {001} surface in the presence of methylamine, shown as space filled. Color keys: Ca = green,
O = red, Si = gray, C = blue, N = yellow, H = white.

![](./images/812276096081854465_14.jpg)

Figure 14. Side view of methylamine adsorption on the wollastonite
{102} surface and (b) top view of the same, all shown as space filled.
Color keys: Ca = green, O = red, Si = gray, C = blue, N = yellow,
H = white.

molecules were present, the {100} and {102} surfaces would
prefer to be hydroxylated. This finding indicates that we need
to consider hydroxylated surfaces for adsorption of other
molecules to understand this phenomenon more clearly. If we
consider the adsorption only in molecular form, then the
adsorption energy for methylamine is the most negative and
the preferred adsorption tendency in molecular form would be
methylamine > methanoic acid > water, for isolated adsorbates
without considering coadsorption. For the {100} and {102}
surfaces, being the two most predominant surfaces, we can say,
from the consideration of the above observations, that the
carboxylic acid and methylamine head groups would be the
adsorbing species and replace water from the wollastonite
surface. Experiments that have been performed in our labora-
tory³⁹ show that ether carboxylic acid gives an 85% wollastonite
flotation recovery and, together with the presence of cationic
polyacrylamide, the flotation recovery is enhanced to 94%. Thus,
our simulation work predicted the well-established trend of
wollastonite flotation behavior while considering only the head-
group molecule. Extension of this work by considering ionic
collectors with a large alkyl chain length and the use of
molecular dynamics simulation would be rewarding, and we
look forward to achieving this in our next endeavour.

Acknowledgment. We gratefully acknowledge the financial
support from the European Union (EU) within the framework
of the EU project, Surface Phenomena and New Reagent
Scheme for Separation of Feldspar from Quartz (Contract No.
BRPR-CT98-0619).

References and Notes

(1) Berry, L. G.; Mason, B. *Mineralogy—Concepts, Descriptions and
Determinations*; W. H. Freeman and Company: San Francisco, 1959.
(2) George C. *Eng. Min. J.* 1997, 198, 63.
(3) Virta, R. L. Wollastonite. In *U.S. Geological Survey Minerals
Yearbook*; U.S. Geological Survey: Washington, DC, 1999; Vol. 83, p 1.
(4) Lind, B.-B.; Ban, Z.; Bydén, S. *Bioresour. Technol.* 2000, 73, 169.
(5) Andrea, S. B.; Melissa, N. R.; Larry, D. G.; Leonard, W. L.;
Tammo, S. S. *Ecol. Eng.* 2000, 15, 121.
(6) Duskova, M.; Kozák, J.; Mazánek, J.; Smahel, Z.; Vohradnik, M.
*Eur. J. Plast. Surg.* 2000, 23, 57.
(7) Power, T. Wollastonite, Performance Filler Potential. *Ind. Miner.*
1986, 220, 19.
(8) Bragg, L.; Claringbull, G. F.; Taylao, W. H. *Crystal Structure of
Minerals*; G. Bell and Sons, Ltd.: London, 1965.
(9) Deer, W. A.; Howie, R. A.; Zussman, J. *An Introduction to the
Rock-Forming Minerals*, 2nd Edition; Longman Scientific & Technical:
Harlow, Essex, U.K., 1992.
(10) Jizu, Y.; Mingli, C.; Chuxlong, Y. *J. Wuhan Univ. Technol.* 1994,
1, 59.
(11) Fang, H.; Xu, X.; Luo, Y. *J. Wuhan Univ. Technol.* 1994, 1, 65.
(12) Goumin, M.; Wenmao, T.; Xianbin, Z. *J. Wuhan Univ. Technol.*
1994, 1, 177.
(13) Watson, G. W.; Kelsey, E. T.; de Leeuw, N. H.; Harris, D. J.;
Parker, S. C. *J. Chem. Soc., Faraday Trans.* 1996, 92, 433.
(14) Parker. S. C.; Kelsey, E. T.; Oliver, P. M.; Titiloye, J. O. *Faraday
Discuss.* 1993, 95, 75.
(15) Davies, M. J.; Parker, S. C.; Watson, G. W. *J. Mater. Chem.* 1994,
4, 813.
(16) Purton, J.; Bullett, D. W.; Oliver, P. M.; Parker, S. C. *Surf. Sci.*
1995, 336, 166.
(17) Didymus, J. M.; Oliver, P.; Mann, S.; De Vries, A. L.; Hauschka,
P. V.; Westbroek, P. *J. Chem. Soc., Faraday Trans.* 1993, 89, 2891.
(18) Oliver, P. M.; Parker, S. C.; Mackrodt, W. C. *Modell. Simul. Mater.
Sci. Eng.* 1993, 1, 755.
(19) de Leeuw, N. H.; Watson, G. W.; Parker, S. C. *J. Phys. Chem.*
1995, 99, 17219.

(20) de Leeuw, N. H.; Watson, G. W.; Parker, S. C. *J. Chem. Soc., Faraday Trans.* **1996**, *92*, 2081.

(21) de Leeuw, N. H.; Parker S. C. *J. Chem. Soc., Faraday Trans.* **1997**, *93*, 467.

(22) Kundu, T. K.; Rao, K. H.; Parker, S. C. *Chem. Phys. Lett.* **2003**, *377*, 81.

(23) Dick, B. G.; Overhauser, A. W. *Phys. Rev.* **1958**, *112*, 90.

(24) Lewis, G. V.; Catlow, C. R. A. *J. Phys. C: Solid State Phys.* **1985**, *18*, 1149.

(25) Parker, S. C.; Price, G. D. *Adv. Solid State Chem.* **1989**, *1*, 295.

(26) Tasker, P. W. *Philos. Mag. A* **1979**, *39*, 119.

(27) Parry, D. E. *Surf. Sci.* **1975**, *49*, 433.

(28) Parry, D. E. *Surf. Sci.* **1976**, *54*, 195.

(29) Ewald, P. P. *Ann. Phys.* **1921**, *64*, 253.

(30) Tasker, P. W. *J. Phys. C: Solid State Phys.* **1979**, *12*, 4977.

(31) Bertaut, F. *Comput. Rend.* **1958**, *246*, 3447.

(32) Oliver, P. M.; Parker, S. C.; Mackrodt, W. C. *Modell. Simul. Mater. Sci. Eng.* **1993**, *1*, 755.

(33) Kröger, F. A. *The Chemistry of Imperfect Crystals*; North−Holland Press: Amsterdam, 1964.

(34) Harding, J. H.; Pyper, N. C. *Philos. Mag. Lett.* **1995**, *71*, 113.

(35) Deer, W. A.; Howie, R. A.; Zussman, J. *An Introduction to the Rock-Forming Minerals*, 2nd Edition; Longman Scientific & Technical: Harlow, Essex, U.K., 1992.

(36) Mazzucato, E.; Gualtieri, A. F. *Phys. Chem. Miner.* **2000**, *27*, 565.

(37) Dana, J. D. *Dana's New Mineralogy: The System of Mineralogy of James Dwight Dana and Edward Salisbury Dana*, 8th Edition; Wiley: New York, 1997.

(38) Pugh, R. J.; Kizling, M.; Palm, C. O. *Miner. Eng.* **1995**, *8*, 1239.

(39) Rao, K. H.; Pugh, R. J.; Kundu, T. K.; Rath, R. K.; Vidyadhar, A. Surface Phenomena and New Reagent Scheme for Separation of Feldspars from Quartz, RESEPAR, 5th Progress Report, Contract No. BRPR-CT98-0619, Project Funded by the European Community under the BRITE/EURAM Programme.