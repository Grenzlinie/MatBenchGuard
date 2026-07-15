# Impact of dihydrogen bonding on lattice energies and sublimation enthalpies of crystalline $\mathbf{[H_2GaNH_2]_3}$, $\mathbf{[H_2BNH_2]_3}$ and $\mathbf{[H_2GeCH_2]_3} \dagger$

Wayne L. Gladfelter*a and Christopher J. Cramer b

The lattice energies of $[\mathrm{H_2GaNH_2}]_3$, $[\mathrm{H_2BNH_2}]_3$ and $[\mathrm{H_2GeCH_2}]_3$ in their experimentally determined space groups, $P2_1/m$, $Pmn2_1$ and $Pbcm$, respectively, were calculated using density functional methods for periodic structures with the *ab initio* periodic code CRYSTAL17. Using the basis set pob-TZVP for all calculations, B3LYP including Grimme's D3 dispersion correction was found to reproduce experimental bond distances and angles most accurately. CRYSTAL17 was also used to optimize geometries and calculate energies of the molecular structures in the gas phase. While the chair conformation of the six-membered rings is found in all of the crystals, only $[\mathrm{H_2GeCH_2}]_3$ retains this as the preferred conformation in the gas phase. By contrast, a twist-boat conformation is preferred for both $[\mathrm{H_2GaNH_2}]_3$ and $[\mathrm{H_2BNH_2}]_3$ in the gas phase, and thus a correction for this change in conformation must be included in corresponding sublimation enthalpy calculations. In addition to the D3 dispersion correction, all lattice energies included a correction for basis set superposition error. The lattice energies for $[\mathrm{H_2GaNH_2}]_3$, $[\mathrm{H_2BNH_2}]_3$ and $[\mathrm{H_2GeCH_2}]_3$ were 153.5, 120.8 and 84.9 kJ mol$^{-1}$, respectively. These values were used to calculate the sublimation enthalpies, which exhibited good agreement for the single case where an experimental measurement is available, namely $[\mathrm{H_2BNH_2}]_3$ (exp $\Delta H_{\rm sub}(298)$, $119 \pm 12$ kJ mol$^{-1}$; calcd, 119.4 kJ mol$^{-1}$). The energetic impact of the crystal structure was assessed by minimizing the structures of each molecule in each of the three space groups spanned by them experimentally and calculating their respective lattice energies. In every case, the experimentally observed space group was the one computed to be the most stable.

## Introduction

Volatility is a necessary property for molecules to function as precursors in chemical vapor deposition and related processes. In the case involving solid precursors, the heat of sublimation ($\Delta H_{\rm sub}^\circ$) is useful for predicting the equilibrium gas-phase concentration of a precursor. For molecular solids, lattice energy, the energy per molecule required to separate the molecules to gas-phase species, is the major contributor to the value of $\Delta H_{\rm sub}^\circ$, and there has been much effort focused on using computational methods to predict $\Delta H_{\rm sub}^\circ$. $^{1-10}$

Lattice energy depends on the strength of intermolecular bonds present in the crystalline phase and there has been great interest in structures exhibiting dihydrogen bonds. Ammonia-borane and related compounds, including $[\mathrm{H_2BNH_2}]_3$, exhibit intermolecular dihydrogen bonds and have been the focus of study due to their potential application in hydrogen storage systems. $^{11-13}$ Numerous other main group metal compounds with hydrido ligands have been found to exhibit short intra- or intermolecular contacts with protic hydrogens. $^{1,11,14-22}$ Dihydrogen bonds can also be important in the reactivity of the compounds. $^{11-13,16,17}$ Structural studies of both cyclotrigallazane, $[\mathrm{H_2GaNH_2}]_3$, $^{16}$ and cyclotriborazane, $[\mathrm{H_2BNH_2}]_3$, $^{22}$ have revealed short intermolecular contacts between the hydridic hydrogens bound to the gallium or boron and the protic hydrogens bound to the nitrogens. A previous computational study of the gas phase dimers of $[\mathrm{H_2BNH_2}]_3$ and of $[\mathrm{H_2GaNH_2}]_3$ connected *via* dihydrogen bonds suggested a $\mathrm{H\cdots H}$ bond energy of 13 kJ mol$^{-1}$. $^{16}$

While the previous study modeled the dihydrogen bond strength computationally based on the difference in energy between gas phase monomers and dimers, the current study includes all intermolecular interactions and reports heats of sublimation that in one case, $[\mathrm{H_2BNH_2}]_3$, can be compared to an experimental value. $^{23}$ The current study expands on earlier work by calculating the lattice energy of crystalline $[\mathrm{H_2BNH_2}]_3$, $[\mathrm{H_2GaNH_2}]_3$ and $[\mathrm{H_2GeCH_2}]_3$. In the solid state, each of these molecules exist as a six-membered ring in a chair conformation. For convenience, the atomic labelling scheme was unified for all

---

$^{a}$Department of Chemistry, University of Minnesota, 207 Pleasant St., SE, Minneapolis, MN 55455, USA. E-mail: wlg@umn.edu
$^{b}$Department of Chemistry, Chemical Theory Center, Minnesota Supercomputing Institute, University of Minnesota, 207 Pleasant St., SE, Minneapolis, MN 55455, USA
$\dagger$ Electronic supplementary information (ESI) available. See DOI: 10.1039/c9ra07144j

three molecules and is shown in Fig. 1 using $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$ as an example. In their respective space groups, atoms 1 and 4 and their attached hydrogens of all three compounds reside on a crystallographic mirror plane. In this study, the lattice energy of each of the compounds in their native (experimentally determined) space group as well as in the space groups native to the other compounds was calculated. In each case the native space group was found to have the largest lattice energy, illustrating the manner in which the varying strengths of different intermolecular interactions can influence preferred packing arrangements.

## Computational methods

For calculations of crystalline $[\mathrm{H}_{2}\mathrm{BNH}_{2}]_{3}$ (ref. 22) and $[\mathrm{H}_{2}\mathrm{GeCH}_{2}]_{3}$ (ref. 24) the experimental crystal parameters and atomic coordinates obtained from single crystal X-ray diffraction results were used as the starting point. For $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$ the crystal parameters and atomic coordinates resulting from Rietveld refinement of the neutron powder diffraction of the corresponding perdeutero compound were used.¹⁶ All calculations were made using the CRYSTAL17 code.²⁵ The pob-TZVP basis set²⁶ was used in all DFT calculations, and a shrinking factor of 4 was used to generate a grid of $k$ points in reciprocal space. Four density functionals, B3LYP, PBE, PBE0 and M06-2x, were evaluated by comparing their results to the experimental structure of $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$. For calculations using B3LYP, PBE and PBE0, Grimme's D3 dispersion correction,²⁷⁻²⁹ including Becke-Johnson damping,³⁰ was employed by use of the keyword DFT-D3. Table 1 shows that the B3LYP and PBE functionals most closely reproduced the experimental results. B3LYP, which more closely reproduced the molecular structure, was chosen for all remaining calculations. Using the keyword MOLEBSSE invoked the counterpoise method to determine the basis set superposition error (BSSE).

![](./images/812734235696693248_1.jpg)

Fig. 1 Atom labeling scheme for $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$. Atoms 1 and 4 (Ga1 and N4 in the figure) along with their attached hydrogens lie on a crystallographic mirror plane. This is also true for $[\mathrm{H}_{2}\mathrm{GeCH}_{2}]_{3}$ and $[\mathrm{H}_{2}\mathrm{BNH}_{2}]_{3}$ where Ge and B atoms, respectively, replace the Ga atoms and C replaces the N in $[\mathrm{H}_{2}\mathrm{GeCH}_{2}]_{3}$. The atom numbering is identical in all of the structures. The A and E labels on the hydrogens refer to the axial and equatorial positions, respectively.

Determination of the lattice energies required calculation of the energies of the isolated molecules in the chair conformation observed in the crystal structures. These calculations also used B3LYP and the same basis set used for the solid state calculations. For $[\mathrm{H}_{2}\mathrm{GeCH}_{2}]_{3}$ the chair conformation was preferred in the gas phase, however, the twist-boat conformation was more stable for both $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$ and $[\mathrm{H}_{2}\mathrm{BNH}_{2}]_{3}$. The energy associated with this conformational change was included in the determination of the sublimation enthalpy. Vibrational frequency calculations were performed on both the gas phase and solid state structures in their native space groups using the keyword FREQCALC. From these calculations, zero point vibrational energies (ZPVE) and vibrational contributions to the sublimation enthalpy of each species at 298 K were determined.

Analysis of the Hirshfeld surfaces for each of the crystals used CrystalExplorer17.³¹,³²

## Results and discussion

As reported previously the crystal and molecular structures of $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$ and $[\mathrm{D}_{2}\mathrm{GaND}_{2}]_{3}$ were solved by single crystal X-ray diffraction and Rietveld refinement of the powder neutron diffraction, respectively.¹⁶ For two reasons, the neutron diffraction results for $[\mathrm{D}_{2}\mathrm{GaND}_{2}]_{3}$ were chosen as the source for comparison with the computational results. First, bond distances between heavy atoms and hydrogen determined using X-ray methods are known to be the shortened relative to those obtained using neutron methods. Because the calculated structures will report distances between nuclei positions, results from the neutron diffraction were considered more appropriate. Second, the twinning present in the single crystals affected the accuracy of the distances and angles in $[\mathrm{H}_{2}\mathrm{GaNH}_{2}]_{3}$. Another difference between the two structural studies is the data collection temperature; 106 K for the X-ray diffraction experiment and 298 K for the neutron diffraction one. This led to a unit cell volume expansion of 1.97% for the higher temperature structure. As shown in Table 1, the calculated unit cell volumes at 0 K were 4–6% smaller regardless of the density functional used. At least part of this contraction can be assigned to the effect of temperature. In addition, part of the underestimation of the computed volumes could be ascribed to BSSE due to the finite basis set used for the calculations.³³

The choice of density functional used for the calculations was based on how well it reproduced the experimental neutron diffraction results. One functional (PBE) and three hybrid functionals (PBE0, B3LYP and M06-2X) were tested using the same basis set (pob-TZVP). For calculations using the PBE, B3LYP and PBE0 functionals, Grimme's D3 dispersion correction was applied. In all calculations, both the atomic positional and unit cell parameters were allowed to refine to convergence within the chosen space group. Although the cell parameters ($a$, $b$, $c$ and $\beta$ for the native space $P2_{1}/m$ of $[\mathrm{D}_{2}\mathrm{GaND}_{2}]_{3}$) were reproduced best using the PBE-D3 functional, B3LYP-D3 led to the smallest differences in bond lengths and angles of the molecular unit. The latter was chosen for all subsequent calculations. For purposes of comparison to the computational results, the density reported in Tables 1 and 2 for $[\mathrm{D}_{2}\mathrm{GaND}_{2}]_{3}$

<table>
<caption>Table 1 Comparison of experimental and calculated structures of $[H_2GaNH_2]_3$ using different density functionals</caption>
<thead>
<tr>
<th>
</th>
<th>Method
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
</tr>
<tr>
<th>
</th>
<th>XRD (EXP)
</th>
<th>ND (EXP)
</th>
<th>B3LYP
</th>
<th>M06-2X
</th>
<th>PBE
</th>
<th>PBE0
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Temp. (K)
</td>
<td>106
</td>
<td>298
</td>
<td>0
</td>
<td>0
</td>
<td>0
</td>
<td>0
</td>
</tr>
<tr>
<td>Lattice parameters
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>$a$ (Å)
</td>
<td>5.7615
</td>
<td>5.7893
</td>
<td>5.6471
</td>
<td>5.6861
</td>
<td>5.6607
</td>
<td>5.6572
</td>
</tr>
<tr>
<td>$b$ (Å)
</td>
<td>8.5079
</td>
<td>8.5635
</td>
<td>8.3703
</td>
<td>8.3289
</td>
<td>8.4648
</td>
<td>8.3929
</td>
</tr>
<tr>
<td>$c$ (Å)
</td>
<td>8.0848
</td>
<td>8.1617
</td>
<td>7.8564
</td>
<td>7.7462
</td>
<td>7.8960
</td>
<td>7.8331
</td>
</tr>
<tr>
<td>$\beta$ (°)
</td>
<td>110.843
</td>
<td>111.038
</td>
<td>110.347
</td>
<td>110.095
</td>
<td>110.846
</td>
<td>110.987
</td>
</tr>
<tr>
<td>Volume (Å³)
</td>
<td>370.37
</td>
<td>377.66
</td>
<td>348.18
</td>
<td>344.53
</td>
<td>353.58
</td>
<td>347.25
</td>
</tr>
<tr>
<td>Density (g cm⁻³)
</td>
<td>2.36
</td>
<td>2.31ᵃ
</td>
<td>2.49
</td>
<td>2.52
</td>
<td>2.45
</td>
<td>2.50
</td>
</tr>
<tr>
<td>Average absolute errors
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cell axis dimensions (Å)
</td>
<td>
</td>
<td>
</td>
<td>0.214
</td>
<td>0.251
</td>
<td>0.164
</td>
<td>0.210
</td>
</tr>
<tr>
<td>Bond lengths (Å)
</td>
<td>
</td>
<td>
</td>
<td>0.026
</td>
<td>0.037
</td>
<td>0.087
</td>
<td>0.115
</td>
</tr>
<tr>
<td>Bond angles (°)
</td>
<td>
</td>
<td>
</td>
<td>4.383
</td>
<td>4.689
</td>
<td>5.446
</td>
<td>5.646
</td>
</tr>
</tbody>
</table>

ᵃ Based on the formula $[H_2GaNH_2]_3$.

was calculated using the neutron diffraction cell volume for the protio formula. Tables 3 and 4 list the experimental and calculated metrical parameters for $[H_2GeCH_2]_3$ and $[H_2BNH_2]_3$, respectively.

The crystal and molecular structures of each of the compounds have been reported and compared elsewhere, and no further discussion of the molecular structure will be included here.¹⁶,²²,²⁴ An appreciation of the intermolecular interactions can be gleaned through the use of Hirshfeld surfaces as developed by Spackman and coworkers.³¹,³² Based on the calculated structures, the Hirshfeld surfaces are shown in Fig. 2. In each case the Hirshfeld surface is displayed for one molecule surrounded by 14 neighbors. The color code assesses the distance between the Hirshfeld surface and the neighboring atoms with red indicating the shortest distance, green intermediate and blue the longest. Despite their different space

<table>
<caption>Table 2 Selected metrical parameters of $[H_2GaNH_2]_3$</caption>
<thead>
<tr>
<th>
</th>
<th>Method
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
</tr>
<tr>
<th>
</th>
<th>XRD (EXP)
</th>
<th>ND (EXP)
</th>
<th>B3LYP
</th>
<th>B3LYP
</th>
<th>B3LYP
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Temp. (K)
</td>
<td>106
</td>
<td>298
</td>
<td>0
</td>
<td>0
</td>
<td>0
</td>
</tr>
<tr>
<td>Crystal system
</td>
<td>Monoclinic
</td>
<td>Monoclinic
</td>
<td>Monoclinic
</td>
<td>Orthorhombic
</td>
<td>Orthorhombic
</td>
</tr>
<tr>
<td>Space group
</td>
<td>$P2_1/m$
</td>
<td>$P2_1/m$
</td>
<td>$P2_1/m$
</td>
<td>$Pmn2_1$
</td>
<td>$Pbcm$
</td>
</tr>
<tr>
<td>$Z$
</td>
<td>2
</td>
<td>2
</td>
<td>2
</td>
<td>2
</td>
<td>4
</td>
</tr>
<tr>
<td>Lattice parameters
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>$a$ (Å)
</td>
<td>5.7615
</td>
<td>5.7893
</td>
<td>5.6471
</td>
<td>8.4203
</td>
<td>4.7423
</td>
</tr>
<tr>
<td>$b$ (Å)
</td>
<td>8.5079
</td>
<td>8.5635
</td>
<td>8.3703
</td>
<td>7.4080
</td>
<td>13.7297
</td>
</tr>
<tr>
<td>$c$ (Å)
</td>
<td>8.0848
</td>
<td>8.1617
</td>
<td>7.8564
</td>
<td>5.6075
</td>
<td>11.7629
</td>
</tr>
<tr>
<td>$\beta$ (°)
</td>
<td>110.843
</td>
<td>111.038
</td>
<td>110.347
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Volume (Å³)
</td>
<td>370.37
</td>
<td>377.66
</td>
<td>348.18
</td>
<td>349.78
</td>
<td>765.89
</td>
</tr>
<tr>
<td>Density (g cm⁻³)
</td>
<td>2.36
</td>
<td>2.31ᵃ
</td>
<td>2.49
</td>
<td>2.48
</td>
<td>2.26
</td>
</tr>
<tr>
<td>Average bond distances (Å)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Ga–N
</td>
<td>1.978
</td>
<td>1.976
</td>
<td>1.995
</td>
<td>1.995
</td>
<td>1.993
</td>
</tr>
<tr>
<td>Ga–HA
</td>
<td>
</td>
<td>1.577
</td>
<td>1.568
</td>
<td>1.567
</td>
<td>1.575
</td>
</tr>
<tr>
<td>Ga–HE
</td>
<td>
</td>
<td>1.537
</td>
<td>1.570
</td>
<td>1.571
</td>
<td>1.562
</td>
</tr>
<tr>
<td>N–HA
</td>
</td>
<td>1.046
</td>
<td>1.019
</td>
<td>1.019
</td>
<td>1.019
</td>
</tr>
<tr>
<td>N–HE
</td>
</td>
<td>1.026
</td>
<td>1.018
</td>
<td>1.018
</td>
<td>1.018
</td>
</tr>
<tr>
<td>Close H–H nonbonded contacts (Å)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>H2A–H3A
</td>
<td>
</td>
<td>1.972
</td>
<td>1.964
</td>
<td>1.914
</td>
<td>2.265
</td>
</tr>
<tr>
<td>H2A–H1A
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>2.082
</td>
</tr>
<tr>
<td>H1E–H4A
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>2.025
</td>
</tr>
</tbody>
</table>

ᵃ Based on the formula $[H_2GaNH_2]_3$.

### Table 3 Selected metrical parameters of $[H_2GeCH_2]_3$

<table>
  <thead>
    <tr>
      <th></th>
      <th>Method</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>XRD (EXP)</th>
      <th>B3LYP</th>
      <th>B3LYP</th>
      <th>B3LYP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Temp. (K)</td>
      <td>213</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Crystal system</td>
      <td>Orthorhombic</td>
      <td>Orthorhombic</td>
      <td>Monoclinic</td>
      <td>Orthorhombic</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>$Pmn2_1$</td>
      <td>$Pmn2_1$</td>
      <td>$P2_1/m$</td>
      <td>$Pbcm$</td>
    </tr>
    <tr>
      <td>Z</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <td colspan="5">Lattice parameters</td>
    </tr>
    <tr>
      <td>$a$ (Å)</td>
      <td>8.663</td>
      <td>8.431</td>
      <td>5.847</td>
      <td>5.068</td>
    </tr>
    <tr>
      <td>$b$ (Å)</td>
      <td>7.783</td>
      <td>7.365</td>
      <td>8.336</td>
      <td>14.019</td>
    </tr>
    <tr>
      <td>$c$ (Å)</td>
      <td>6.124</td>
      <td>5.836</td>
      <td>7.833</td>
      <td>10.730</td>
    </tr>
    <tr>
      <td>$\beta$ (°)</td>
      <td></td>
      <td></td>
      <td>110.49</td>
      <td></td>
    </tr>
    <tr>
      <td>Volume (Å³)</td>
      <td>412.91</td>
      <td>362.39</td>
      <td>357.64</td>
      <td>762.32</td>
    </tr>
    <tr>
      <td>Density (g cm⁻³)</td>
      <td>2.14</td>
      <td>2.47</td>
      <td>2.51</td>
      <td>2.35</td>
    </tr>
    <tr>
      <td colspan="5">Average bond distances (Å)</td>
    </tr>
    <tr>
      <td>Ge–C</td>
      <td>1.951</td>
      <td>1.956</td>
      <td>1.957</td>
      <td>1.957</td>
    </tr>
    <tr>
      <td>Ge–HA</td>
      <td>1.572</td>
      <td>1.531</td>
      <td>1.536</td>
      <td>1.537</td>
    </tr>
    <tr>
      <td>Ge–HE</td>
      <td>1.548</td>
      <td>1.536</td>
      <td>1.532</td>
      <td>1.532</td>
    </tr>
    <tr>
      <td>C–HA</td>
      <td>1.107</td>
      <td>1.088</td>
      <td>1.088</td>
      <td>1.089</td>
    </tr>
    <tr>
      <td>C–HE</td>
      <td>0.972</td>
      <td>1.088</td>
      <td>1.087</td>
      <td>1.087</td>
    </tr>
    <tr>
      <td colspan="5">Close H–H nonbonded contacts (Å)</td>
    </tr>
    <tr>
      <td>H2A–H3A</td>
      <td>2.200</td>
      <td>2.101</td>
      <td>2.143</td>
      <td></td>
    </tr>
    <tr>
      <td>H2A–H1A</td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.186</td>
    </tr>
  </tbody>
</table>

groups, the Hirshfeld surfaces of $[H_2GaNH_2]_3$ and $[H_2GeCH_2]_3$ and the corresponding contacts with neighboring molecules (as indicated by the red to yellow regions) are remarkably similar.

In both cases all contacts result from Ga–H$\cdots$H–N or Ge–H$\cdots$H–C interactions. For both compounds the closest approach to the Hirshfeld surface can be seen at the top of the figure between

### Table 4 Selected metrical parameters of $[H_2BNH_2]_3$

<table>
  <thead>
    <tr>
      <th></th>
      <th>Method</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>XRD</th>
      <th>B3LYP</th>
      <th>B3LYP</th>
      <th>B3LYP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Temp. (K)</td>
      <td>180</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Crystal system</td>
      <td>Orthorhombic</td>
      <td>Orthorhombic</td>
      <td>Monoclinic</td>
      <td>Orthorhombic</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>$Pbcm$</td>
      <td>$Pbcm$</td>
      <td>$P2_1/m$</td>
      <td>$Pmn2_1$</td>
    </tr>
    <tr>
      <td>Z</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td colspan="5">Lattice parameters</td>
    </tr>
    <tr>
      <td>$a$ (Å)</td>
      <td>4.383</td>
      <td>4.248</td>
      <td>5.004</td>
      <td>7.358</td>
    </tr>
    <tr>
      <td>$b$ (Å)</td>
      <td>12.193</td>
      <td>11.914</td>
      <td>7.343</td>
      <td>6.635</td>
    </tr>
    <tr>
      <td>$c$ (Å)</td>
      <td>11.180</td>
      <td>10.917</td>
      <td>7.225</td>
      <td>5.025</td>
    </tr>
    <tr>
      <td>$\beta$ (°)</td>
      <td></td>
      <td></td>
      <td>112.39</td>
      <td></td>
    </tr>
    <tr>
      <td>Volume (cm³)</td>
      <td>597.50</td>
      <td>552.53</td>
      <td>245.48</td>
      <td>245.31</td>
    </tr>
    <tr>
      <td>Density (g cm⁻³)</td>
      <td>0.96</td>
      <td>1.05</td>
      <td>1.18</td>
      <td>1.18</td>
    </tr>
    <tr>
      <td colspan="5">Average bond distances (Å)</td>
    </tr>
    <tr>
      <td>B–N</td>
      <td>1.574</td>
      <td>1.576</td>
      <td>1.578</td>
      <td>1.578</td>
    </tr>
    <tr>
      <td>B–HA</td>
      <td>1.133</td>
      <td>1.208</td>
      <td>1.201</td>
      <td>1.203</td>
    </tr>
    <tr>
      <td>B–HE</td>
      <td>1.168</td>
      <td>1.206</td>
      <td>1.207</td>
      <td>1.205</td>
    </tr>
    <tr>
      <td>N–HA</td>
      <td>0.863</td>
      <td>1.020</td>
      <td>1.021</td>
      <td>1.021</td>
    </tr>
    <tr>
      <td>N–HE</td>
      <td>0.895</td>
      <td>1.020</td>
      <td>1.019</td>
      <td>1.019</td>
    </tr>
    <tr>
      <td colspan="5">Close H–H nonbonded contacts (Å)</td>
    </tr>
    <tr>
      <td>H2A–H3A</td>
      <td></td>
      <td></td>
      <td>1.882</td>
      <td>1.912</td>
    </tr>
    <tr>
      <td>H4E–H1E</td>
      <td>2.275</td>
      <td>2.022</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>H4E–H1A</td>
      <td>2.217</td>
      <td>1.984</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>H2E–H3A</td>
      <td>2.259</td>
      <td>2.009</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>H2E–H3E</td>
      <td>2.351</td>
      <td>2.173</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>


![](./images/812734235696693248_2.jpg)

Fig. 2 Hirshfeld surfaces of a molecule of $[H_2GaNH_2]_2$ (upper left), $[H_2GeCH_2]_3$ (upper right) and $[H_2BNH_2]_3$ (lower) shown surrounded by 14 neighboring rings. The range of colors on the surface indicates distance of surrounding atoms to the surface with red representing the closer and blue the longer contacts.

the axial hydrogens attached to the nitrogen (labelled N2) in $[H_2GaNH_2]_3$, and the carbon (C2) in $[H_2GeCH_2]_3$.

For $[H_2GaNH_2]_3$ and $[H_2BNH_2]_3$, there are 22 and 30 intermolecular $H\cdots H$ contacts between 1.9 and $2.4\ Å$, respectively. In this same range, $[H_2GeCH_2]_3$ has 14 contacts among which only 4 shorter, symmetry equivalent contacts of $2.100\ Å$ are found. All contacts below $2.4\ Å$ occur between hydrides on a B, Ga or Ge and a hydrogen bound to a N or C. For the $66\ H\cdots H$ contacts in the three compounds, Fig. 3 shows a histogram of contact distances. Based on Bondi's van der Waal radius for hydrogen of $1.2\ Å$ (ref. 34) previous reports suggest $H\cdots H$ distances below $2.4\ Å$ constitute dihydrogen bonds. More recent studies of van der Waals radii suggest that a value of $1.1\ Å$ is more appropriate for the hydrogen radius. $^{35,36}$ Consistent with this shorter radius, the mode for the distribution in Fig. 3 includes contacts between 2.21 and $2.25\ Å$. All three compounds exhibit contacts shorter that $2.2\ Å$ that can be reasonably considered as dihydrogen bonds. The shortest, and presumably the strongest, occur in $[H_2GaNH_2]_3$ and $[H_2BNH_2]_3$.

The number of $H\cdots H$ contacts per hydrogen differs in the three structures. In $[H_2BNH_2]_3$ each of the axial hydrogens has three $H\cdots H$ contacts to neighboring molecules, whereas each of the equatorial hydrogens has two. The equatorial NH groups contact both hydrogens of an adjacent $BH_2$ moiety to form an unsymmetrical, bifurcated dihydrogen bond. The equatorial hydrogen H4E that lies within the crystallographic mirror plane exhibits the shortest $H\cdots H$ contact of $1.984\ Å$ (to H1A) and the

![](./images/812734235696693248_3.jpg)

Fig. 3 Histogram of the combined intermolecular $H\cdots H$ contacts for $[H_2GaNH_2]_3$, $[H_2BNH_2]_3$ and $[H_2GeCH_2]_3$. The labels on the three shortest contact bins refer to the compounds contributing to that distance bin; $Ga = [H_2GaNH_2]_3$, $B = [H_2BNH_2]_3$, $Ge = [H_2GeCH_2]_3$.

second short contact (2.021 Å) is to H1E; both H1A and H1E are bonded to B1 (Fig. 2). Close inspection of the Hirshfeld surface in the region adjacent to B1 reveals two red spots corresponding to the bifurcated interaction with H4E. This interaction generates a chain of molecules connected by dihydrogen bonds parallel to the crystallographic $b$-axis in the $bc$ plane. A second set of close contacts exists between the equatorial N-H (see N2 on Fig. 2) and the hydrides (H3A and H3E located within the Hirshfeld surface) attached to B3. The chain resulting from this interaction also lies in the $bc$ plane but runs parallel to the $c$-axis. Longer $\text{H}\cdots\text{H}$ interactions connect molecules in the $ab$ plane with the layers above and below. In contrast to $[\text{H}_2\text{BNH}_2]_3$, most of the hydrogens in $[\text{H}_2\text{GaNH}_2]_3$ and $[\text{H}_2\text{GeCH}_2]_3$ exhibit two and one $\text{H}\cdots\text{H}$ contacts, respectively. The predominance of bifurcated dihydrogen bonds in cyclotriborazane compared to the complete lack of such interactions in cyclotrigallazane is likely attributable to the longer Ga-H bonds (1.57 Å) vs. the B-H distance of 1.21 Å and the wider H-Ga-H angle (119.7°) vs. H-B-H (111.6°). These metrical parameters would require the H-N proton to span a much larger distance between the two hydrogens on an HGaH group (2.71 Å) compared to 2.00 Å for an HBH group.

The Mulliken charges on each of the atoms (Table 5) confirm the hydridic nature of hydrogens attached to gallium, germanium and boron and the protic nature of those bound to nitrogen. The small positive charges on the carbon-bound hydrogens in $[\text{H}_2\text{GeCH}_2]_3$ are undoubtedly a factor leading to the nonexistence of dihydrogen bonding in this compound.

## Calculated structures in non-native space groups

Considering the similar chair conformation of the molecular unit among these structures, we were curious to calculate each of the crystal and molecular structures in the alternative space groups. This was readily accomplished using the original atomic coordinates and lattice parameters as the starting point and changing the appropriate atoms for each calculation. All possibilities converged successfully. Table 2 compares the $[\text{H}_2\text{GaNH}_2]_3$ experimental and calculated structures in both the native space group ($P2_1/m$) and in the space groups for $[\text{H}_2\text{GeCH}_2]_3$ ($Pmn2_1$) and $[\text{H}_2\text{BNH}_2]_3$ ($Pbcm$). The space group choice has little impact on the intramolecular distances and parameters, but it is interesting that the closest calculated intermolecular contact for $[\text{H}_2\text{GaNH}_2]_3$ is slightly shorter (1.914 vs. 1.964 Å) in the non-native $Pmn2_1$ space group. All calculated intermolecular contacts in $Pbcm$ were longer than those found in $P2_1/m$ and $Pmn2_1$. The intermolecular $\text{H}\cdots\text{H}$ contacts in $[\text{H}_2\text{GeCH}_2]_3$ (Table 3) are longer than those calculated for $[\text{H}_2\text{GaNH}_2]_3$ but the shortest contact occurs in the native space group. In the native space group for $[\text{H}_2\text{BNH}_2]_3$ the intermolecular $\text{H}\cdots\text{H}$ contacts are longer than those calculated for either of the non-native space groups, which may reflect the impact of bifurcated bonding in determining the structure.

<table>
<caption>Table 5 Mulliken charges for the compounds in their native space groups</caption>
<thead>
<tr>
<th rowspan="2">Atom</th>
<th>$[\text{H}_2\text{BNH}_2]_3$</th>
<th>$[\text{H}_2\text{GaNH}_2]_3$</th>
<th>$[\text{H}_2\text{GeCH}_2]_3$</th>
</tr>
<tr>
<td>X = B,<br>Y = N</td>
<td>X = Ga,<br>Y = N</td>
<td>X = Ge,<br>Y = C</td>
</tr>
</thead>
<tbody>
<tr>
<td>X1</td>
<td>0.96</td>
<td>0.99</td>
<td>1.05</td>
</tr>
<tr>
<td>X3</td>
<td>0.95</td>
<td>1.00</td>
<td>1.03</td>
</tr>
<tr>
<td>Y2</td>
<td>−0.60</td>
<td>−0.89</td>
<td>−0.59</td>
</tr>
<tr>
<td>Y4</td>
<td>−0.58</td>
<td>−0.85</td>
<td>−0.59</td>
</tr>
<tr>
<td>H1A</td>
<td>−0.30</td>
<td>−0.27</td>
<td>−0.32</td>
</tr>
<tr>
<td>H1E</td>
<td>−0.31</td>
<td>−0.26</td>
<td>−0.28</td>
</tr>
<tr>
<td>H2A</td>
<td>0.12</td>
<td>0.22</td>
<td>0.07</td>
</tr>
<tr>
<td>H2E</td>
<td>0.13</td>
<td>0.20</td>
<td>0.07</td>
</tr>
<tr>
<td>H3A</td>
<td>−0.30</td>
<td>−0.28</td>
<td>−0.31</td>
</tr>
<tr>
<td>H3E</td>
<td>−0.30</td>
<td>−0.24</td>
<td>−0.27</td>
</tr>
<tr>
<td>H4A</td>
<td>0.13</td>
<td>0.18</td>
<td>0.07</td>
</tr>
<tr>
<td>H4E</td>
<td>0.11</td>
<td>0.22</td>
<td>0.07</td>
</tr>
</tbody>
</table>

## Lattice energies

In an attempt to quantify the energetic impact of the crystal structure, lattice energies, $E(\text{lattice})$, were calculated for the three molecules in both their native and non-native space groups. Lattice energy is defined as the energy required to separate a mole of the crystalline solid into isolated gas phase molecules having the same conformation as in the solid state. In addition, the atom-centered calculations of CRYSTAL mandate correction for basis set superposition error, $E(\text{BSSE})$. In eqn (1), $E(\text{crystal})$ equals the crystal energy, $Z$ equals the number of molecules in the unit cell, $E(C_\text{s})$ equals the energy of a gaseous molecule having the same chair conformation ($C_\text{s}$ point group) as observed in the solid. Density functional calculations for the gas phase molecules were conducted using the same functional and basis set (B3LYP-D3/pobTZVP) used for the solid-state structures.

$$
E(\text{lattice}) = E(C_\text{s}) - \frac{E(\text{crystal})}{Z} - E(\text{BSSE}) \tag{1}
$$

Table 6 lists each of the energies for the three compounds in each of the space groups. For each, the lattice energy calculated using CRYSTAL was largest for that compound's native space group. In each of the current compounds, the energy difference was less than 3 kJ mol⁻¹ between $P2_1/m$ and $Pmn2_1$. For $[\text{H}_2\text{GaNH}_2]_3$ and $[\text{H}_2\text{GeCH}_2]_3$, the lattice energy of the $Pbcm$ space group was smaller by 13 to 19 kJ mol⁻¹. For $[\text{H}_2\text{BNH}_2]_3$, the $Pbcm$ space was only 2.5 kJ mol⁻¹ more stable that either of the others. Although the energy differences among the three space groups is small, there are no experimental results establishing the existence of polymorphs for these compounds.

## Sublimation enthalpies

Eqn (2) was used to calculate the sublimation energy for each compound in their native space group (vibrational frequencies were not computed for the higher energy polymorphs). For $[\text{H}_2\text{GaNH}_2]_3$ and $[\text{H}_2\text{BNH}_2]_3$, the lowest energy conformation of the gas phase molecule differed from the molecular conformation in the solid state, thus requiring an additional term,

<table>
 <thead>
  <tr>
   <th colspan="4">
    Table 6 Lattice energies at 0 K (kJ mol-1)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    Compound
   </th>
   <td>
    $P2_{1}/m$
   </td>
   <td>
    $Pmn2_{1}$
   </td>
   <td>
    $Pbcm$
   </td>
  </tr>
  <tr>
   <th>
    [H₂GaNH₂]₃
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $E$(crystal)
   </th>
   <td>
    $-$31 222 293.41
   </td>
   <td>
    $-$31 222 290.63
   </td>
   <td>
    $-$62 444 488.70
   </td>
  </tr>
  <tr>
   <th>
    $Z$
   </th>
   <td>
    2
   </td>
   <td>
    2
   </td>
   <td>
    4
   </td>
  </tr>
  <tr>
   <th>
    $E(C_{s})$
   </th>
   <td>
    $-$15 610 951.15
   </td>
   <td>
    $-$15 610 951.15
   </td>
   <td>
    $-$15 610 951.15
   </td>
  </tr>
  <tr>
   <th>
    $E$(BSSE)
   </th>
   <td>
    42.06
   </td>
   <td>
    42.52
   </td>
   <td>
    36.24
   </td>
  </tr>
  <tr>
   <th>
    $E$(lattice)
   </th>
   <td>
    153.49
   </td>
   <td>
    151.65
   </td>
   <td>
    134.79
   </td>
  </tr>
  <tr>
   <th>
    [H₂GeCH₂]₃
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $E$(crystal)
   </th>
   <td>
    $-$33 356 028.40
   </td>
   <td>
    $-$33 356 025.40
   </td>
   <td>
    $-$66 711 984.15
   </td>
  </tr>
  <tr>
   <th>
    $Z$
   </th>
   <td>
    2
   </td>
   <td>
    2
   </td>
   <td>
    4
   </td>
  </tr>
  <tr>
   <th>
    $E(C_{s})$
   </th>
   <td>
    $-$16 677 867.31
   </td>
   <td>
    $-$16 677 867.31
   </td>
   <td>
    $-$16 677 867.31
   </td>
  </tr>
  <tr>
   <th>
    $E$(BSSE)
   </th>
   <td>
    64.7
   </td>
   <td>
    60.52
   </td>
   <td>
    60.11
   </td>
  </tr>
  <tr>
   <th>
    $E$(lattice)
   </th>
   <td>
    82.19
   </td>
   <td>
    84.87
   </td>
   <td>
    68.62
   </td>
  </tr>
  <tr>
   <th>
    [H₂BNH₂]₃
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $E$(crystal)
   </th>
   <td>
    $-$1292 625.17
   </td>
   <td>
    $-$1292 624.28
   </td>
   <td>
    $-$2585 245.45
   </td>
  </tr>
  <tr>
   <th>
    $Z$
   </th>
   <td>
    2
   </td>
   <td>
    2
   </td>
   <td>
    4
   </td>
  </tr>
  <tr>
   <th>
    $E(C_{s})$
   </th>
   <td>
    $-$646157.94
   </td>
   <td>
    $-$646157.94
   </td>
   <td>
    $-$646157.94
   </td>
  </tr>
  <tr>
   <th>
    $E$(BSSE)
   </th>
   <td>
    36.33
   </td>
   <td>
    35.91
   </td>
   <td>
    32.66
   </td>
  </tr>
  <tr>
   <th>
    $E$(lattice)
   </th>
   <td>
    118.32
   </td>
   <td>
    118.29
   </td>
   <td>
    120.77
   </td>
  </tr>
 </tbody>
</table>

$\Delta E$(conf), in the calculation. For [H₂GaNH₂]₃ and [H₂BNH₂]₃ the twist-boat was preferred over the chair conformation by $- 16.8$ and $- 5.0$ kJ mol⁻¹, respectively. These values compare to $- 10.9$ and $- 3.8$ kJ mol⁻¹, respectively, based on the earlier calculations at the MP2/VDZ level of theory.¹⁶ For [H₂GeCH₂]₃, the chair was calculated to be more stable than the twist-boat conformation by 4.4 kJ mol⁻¹, and thus no conformation correction was needed.

$$
\Delta H_{\text{sub}}(T) = E(\text{lattice}) + \Delta E_{\text{conf}} + \Delta E_{\text{ZPVE}} + \Delta E_{\text{vib}}(T) + 4RT \ (2)
$$

The next two terms in eqn (2) are the difference in zero point vibrational energy between the crystalline and gaseous states, $\Delta E_{\text{ZPVE}}$, and the difference in the vibrational contributions at temperature $T$ of the crystalline and gaseous states, $\Delta E_{\text{vib}}(T)$. The $4RT$ term accounts for the rotational, translational and $pV$ work contributions to the energy of the gaseous product. Table 7 summarizes all contributions and the final $\Delta H_{\text{sub}}$ for each molecule at 298 K.

Experimentally, neither [H₂BNH₂]₃ nor [H₂GaNH₂]₃ exhibited a detectable melting point prior to decomposing at 150 °C.¹⁶,²³ Both sublimed under high vacuum above temperatures of 80–90 °C, whereas [H₂GeCH₂]₃ had a melting point of $- 14$ °C and was purified by distillation at 65 °C under reduced pressure (11 mbar).²⁴ Using a Knudson cell, Shore and coworkers measured the vapor pressure of [H₂BNH₂]₃ in the range from 47.5 to 75.5 °C to establish its heat of sublimation as $105 \pm 13$ kJ mol⁻¹.²³ Using the center of their temperature range, the $\Delta H_{\text{sub}}$ was converted to the value at 298.15 K using the method described by Chickos and Acree and the calculated heat capacities for the crystalline and molecular states.³⁷ The agreement was good between the experimental ($119 \pm 12$ kJ mol⁻¹) and calculated (119.4 kJ mol⁻¹) values.

<table>
 <thead>
  <tr>
   <th colspan="4">
    Table 7 Enthalpies of sublimation at 298 K. All energies have units of kJ mol⁻¹
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    Compound
   </th>
   <td>
    [H₂GaNH₂]₃
   </td>
   <td>
    [H₂GeCH₂]₃
   </td>
   <td>
    [H₂BNH₂]₃
   </td>
  </tr>
  <tr>
   <th>
    Space group
   </th>
   <td>
    $P2_{1}/m$
   </td>
   <td>
    $Pmn2_{1}$
   </td>
   <td>
    $Pbcm$
   </td>
  </tr>
  <tr>
   <th>
    $Z$
   </th>
   <td>
    2
   </td>
   <td>
    2
   </td>
   <td>
    4
   </td>
  </tr>
  <tr>
   <th>
    $T$ (K)
   </th>
   <td>
    298.15
   </td>
   <td>
    298.15
   </td>
   <td>
    298.15
   </td>
  </tr>
  <tr>
   <th>
    $E$(lattice)
   </th>
   <td>
    153.49
   </td>
   <td>
    84.87
   </td>
   <td>
    120.77
   </td>
  </tr>
  <tr>
   <th>
    $\Delta E$(conf)
   </th>
   <td>
    $-$16.83
   </td>
   <td>
    0.00
   </td>
   <td>
    $-$4.95
   </td>
  </tr>
  <tr>
   <th>
    ZPVE(crystal)/$Z$
   </th>
   <td>
    341.06
   </td>
   <td>
    347.41
   </td>
   <td>
    427.74
   </td>
  </tr>
  <tr>
   <th>
    ZPVE(gas)
   </th>
   <td>
    334.31
   </td>
   <td>
    343.04
   </td>
   <td>
    422.61
   </td>
  </tr>
  <tr>
   <th>
    $E_{\text{vib}}$(crystal)/$Z$ at $T$
   </th>
   <td>
    29.76
   </td>
   <td>
    26.83
   </td>
   <td>
    18.51
   </td>
  </tr>
  <tr>
   <th>
    $E_{\text{vib}}$(gas) at $T$
   </th>
   <td>
    30.11
   </td>
   <td>
    26.29
   </td>
   <td>
    17.89
   </td>
  </tr>
  <tr>
   <th>
    $4RT$(gas)
   </th>
   <td>
    9.92
   </td>
   <td>
    9.92
   </td>
   <td>
    9.92
   </td>
  </tr>
  <tr>
   <th>
    $\Delta H_{\text{sub}}(T$, calcd)
   </th>
   <td>
    140.18
   </td>
   <td>
    89.89
   </td>
   <td>
    119.43
   </td>
  </tr>
  <tr>
   <th>
    $\Delta H_{\text{sub}}(T$, exp)
   </th>
   <td>
    na
   </td>
   <td>
    na
   </td>
   <td>
    $119 \pm 12$
   </td>
  </tr>
 </tbody>
</table>

## Conclusions

The crystal and molecular structures of [H₂BNH₂]₃, [H₂GaNH₂]₃ and [H₂GeCH₂]₃ were successfully modeled using periodic DFT calculations in their native space groups of ($Pbcm$, $P2_{1}/m$ and $Pmn2_{1}$, respectively). The calculated structures provided a basis for a more uniform comparisons among the structures. In each compound, all intermolecular H$\cdots$H contacts occur between hydridic and protic hydrogens, and the majority of the H$\cdots$H distances occur at or slightly above the expected van der Waals distance (2.2 Å). Both [H₂BNH₂]₃ and [H₂GaNH₂]₃ exhibit several contacts that are $\sim$0.2 Å shorter than the van der Waals contact distance, which places them in the range of typical dihydrogen bonds. The shortest H$\cdots$H contacts in [H₂GeCH₂]₃ (2.1 Å) are intermediate between the van der Waals and dihydrogen bonding distances. Comparison of the crystal energies to the energy of the gas phase molecules having the same chair conformation found in the solid state yielded lattice energies of 120.77, 153.49 and 84.87 kJ mol⁻¹, respectively. For comparison, the crystal and molecular structure of each compound were also calculated in the two non-native space groups (e.g. $P2_{1}/m$ and $Pmn2_{1}$ for [H₂BNH₂]₃). In each case the largest lattice energy corresponded to the experimentally observed (native) space group. For the gas phase molecules and the compounds in their native space group, vibrational frequency calculations allowed calculation of their sublimation enthalpies. For [H₂BNH₂]₃ and [H₂GaNH₂]₃ the sublimation enthalpy calculation included a contribution associated with the conformational difference between the solid state and gas phase conformations. Good agreement was found between the calculated sublimation energy of [H₂BNH₂]₃ (119.4 kJ mol⁻¹) and the published experimental value ($119 \pm 12$ kJ mol⁻¹).

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

This work was funded in part by a grant from the National Science Foundation (DMR 1607318). The authors

acknowledge the Minnesota Supercomputing Institute (MSI) at the University of Minnesota for providing resources that contributed to the research results reported within this paper.

## References

1 C. A. Morrison and M. M. Siddick, *Chem.–Eur. J.*, 2003, **9**, 628–634.

2 C. A. Morrison and M. M. Siddick, *Angew. Chem., Int. Ed.*, 2004, **43**, 4780–4782.

3 B. Civalleri, K. Doll and C. M. Zicovich-Wilson, *J. Phys. Chem. B*, 2007, **111**, 26–33.

4 B. Civalleri, C. M. Zicovich-Wilson, L. Valenzano and P. Ugliengo, *CrystEngComm*, 2008, **10**, 1693.

5 A. Otero-de-la-Roza and E. R. Johnson, *J. Chem. Phys.*, 2012, **137**, 054103.

6 A. M. Reilly and A. Tkatchenko, *J. Chem. Phys.*, 2013, **139**, 024705.

7 J. G. Brandenburg, M. Alessio, B. Civalleri, M. F. Peintinger, T. Bredow and S. Grimme, *J. Phys. Chem. A*, 2013, **117**, 9282–9292.

8 J. Yang, W. F. Hu, D. Usvyat, D. Matthews, M. Schutz and G. K. L. Chan, *Science*, 2014, **345**, 640–643.

9 G. J. O. Beran, *Chem. Rev.*, 2016, **116**, 5567–5613.

10 C. Cervinka and M. Fulem, *J. Chem. Theory Comput.*, 2017, **13**, 2840–2850.

11 X. N. Chen, J. C. Zhao and S. G. Shore, *Acc. Chem. Res.*, 2013, **46**, 2666–2675.

12 A. Staubitz, A. P. M. Robertson and I. Manners, *Chem. Rev.*, 2010, **110**, 4079–4124.

13 F. H. Stephens, V. Pons and R. T. Baker, *Dalton Trans.*, 2007, 2613–2626.

14 T. B. Richardson, S. deGala, R. H. Crabtree and P. E. M. Siegbahn, *J. Am. Chem. Soc.*, 1995, **117**, 12875–12876.

15 C. J. Cramer and W. L. Gladfelter, *Inorg. Chem.*, 1997, **36**, 5358–5362.

16 J. P. Campbell, J. W. Hwang, V. G. Young, R. B. Von Dreele, C. J. Cramer and W. L. Gladfelter, *J. Am. Chem. Soc.*, 1998, **120**, 521–531.

17 R. Custelcean and J. E. Jackson, *J. Am. Chem. Soc.*, 1998, **120**, 12935–12941.

18 L. M. Epstein, E. S. Shubina, E. V. Bakhmutova, L. N. Saitkulova, V. I. Bakhmutov, A. L. Chistyakov and I. V. Stankevich, *Inorg. Chem.*, 1998, **37**, 3013–3017.

19 W. T. Klooster, T. F. Koetzle, P. E. M. Siegbahn, T. B. Richardson and R. H. Crabtree, *J. Am. Chem. Soc.*, 1999, **121**, 6337–6343.

20 N. V. Belkova, L. M. Epstein, O. A. Filippov and E. S. Shubina, *Chem. Rev.*, 2016, **116**, 8545–8587.

21 J. Echeverria, *Cryst. Growth Des.*, 2017, **17**, 2097–2103.

22 H. K. Lingam, C. Wang, J. C. Gallucci, X. N. Chen and S. G. Shore, *Inorg. Chem.*, 2012, **51**, 13430–13436.

23 D. R. Leavers, J. R. Long, S. G. Shore and W. J. Taylor, *J. Chem. Soc. A*, 1969, 1580–1581.

24 H. Schmidbaur, J. Rott, G. Reber and G. Mueller, *Z. Naturforsch., B: J. Chem. Sci.*, 1988, **43**, 727–732.

25 R. Dovesi, A. Erba, R. Orlando, C. M. Zicovich-Wilson, B. Civalleri, L. Maschio, M. Rérat, S. Casassa, J. Baima, S. Salustro and B. Kirtman, *Wiley Interdiscip. Rev.: Comput. Mol. Sci.*, 2018, e1360.

26 M. F. Peintinger, D. V. Oliveira and T. Bredow, *J. Comput. Chem.*, 2013, **34**, 451–459.

27 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, *J. Chem. Phys.*, 2010, **132**, 154104.

28 S. Grimme, S. Ehrlich and L. Goerigk, *J. Comput. Chem.*, 2011, **32**, 1456–1465.

29 S. Grimme, A. Hansen, J. G. Brandenburg and C. Bannwarth, *Chem. Rev.*, 2016, **116**, 5105–5154.

30 E. R. Johnson and A. D. Becke, *J. Chem. Phys.*, 2005, **123**, 024101.

31 M. A. Spackman and P. G. Byrom, *Chem. Phys. Lett.*, 1997, **267**, 215–220.

32 M. A. Spackman and D. Jayatilaka, *CrystEngComm*, 2009, **11**, 19–32.

33 D. V. Oliveira, J. Laun, M. F. Peintinger and T. Bredow, *J. Comput. Chem.*, 2019, **40**, 2364–2376.

34 A. Bondi, *J. Phys. Chem.*, 1964, **68**, 441–451.

35 M. Mantina, A. C. Chamberlin, R. Valero, C. J. Cramer and D. G. Truhlar, *J. Phys. Chem. A*, 2009, **113**, 5806–5812.

36 R. S. Rowland and R. Taylor, *J. Phys. Chem.*, 1996, **100**, 7384–7391.

37 J. S. Chickos and W. E. Acree, *J. Phys. Chem. Ref. Data*, 2002, **31**, 537–698.