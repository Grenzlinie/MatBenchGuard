![](./images/812002393582469120_1.jpg)

Journal of Alloys and Compounds 457 (2008) 29-35

![](./images/812002393582469120_2.jpg)

www.elsevier.com/locate/jallcom

# Lattice stability of intermediate phases of the Sr-Si system

S. Brutti $^{a, *}$, D. Nguyen-Manh $^{b}$, D.G. Pettifor $^{c}$

$^{a}$ Dipartimento di Chimica, Università di Roma "La Sapienza", P.le A.Moro 5 00185 Rome, Italy
$^{b}$ UKAEA Culham Division, Culham Science Centre, Abingdon OX14 3DB, UK
$^{c}$ University of Oxford, Department of Materials, Oxford OX1 3PH, UK

Received 16 February 2007; received in revised form 2 March 2007; accepted 6 March 2007
Available online 12 March 2007

## Abstract

A computational study of the lattice stability of the intermediate phases of the Sr-Si system is presented. Nine compositions have been considered, investigating 26 different crystal lattices by means of density functional theory calculations and pseudopotentials within the generalized-gradient approximation using the VASP code. The heats of formation of the various polymorphs have been derived for all the investigated compositions and found to be in excellent agreement with the available experimental data in the literature. The $Sr_{2}Si$, $Sr_{5}Si_{3}$ and SrSi phases have been predicted to undergo high pressure transitions: the lattice transitions $Sr_{2}Si(oP12 \to hP6)$, $Sr_{5}Si_{3}(tI32-Cr_{5}B_{3} \to tI32-Mo_{5}Si_{3})$ and $SrSi(oC8 \to oP8 \to tP2)$ have been calculated to occur at 5.5, 19.9, 11.8 and 60 GPa, respectively. Electronic structure of the computed ground states and the predicted four new high pressure polymorphs of $Sr_{2}Si$, $Sr_{5}Si_{3}$ and SrSi phases are calculated and discussed in relation with their corresponding crystal structures and heats of formation. The band gap of the semiconducting oP12 $Sr_{2}Si$ ground state structure has been calculated to be 0.29 eV. The bonding of the Sr-Si phases is found to be mainly ionic, as expected from Pauling's electronegativities, although there is evidence of formation of directional covalent bonds between neighboring Si atoms in the silicon richest phases.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Silicides; Various; Bonding; Electronic structure of metals and alloys; Electronic structure; Calculation; Phase stability; Prediction; Physical properties; Miscellaneous

## 1. Introduction

Among the ecologically friendly Kankyo semiconductors [1] the silicides are attractive due to their potential applications in electronic devices as replacements for the more toxic and expensive heavy transition metal silicides [2]. Within this class Ca and Sr silicides are particularly promising as well as the more toxic barium silicides. Recently, semiconducting silicide layers made of $Ca_{2}Si$, $Sr_{2}Si$, $BaSi_{2}$ and $Ba_{1-x}Sr_{x}Si_{2}$ have been successfully grown on oriented Si surfaces or fused $SiO_{2}$ by high temperature annealing interdiffusion process, molecular beam and reactive deposition epitaxy techniques [3-6]. In addition $CaSi_{2}$ and $BaSi_{2}$ and several Ga or Al doped ternary alkaline earth metal (AEM, i.e. Ca, Sr and Ba) silicides show interesting superconducting properties at low temperatures [7-9] as well as some Ba- or Sr-based Si and Ge clathrates [10,11]. These interesting physical properties arise from the peculiar AEM-Si chemical bond in the solid state that is qualitatively predicted to be mainly ionic. Moreover, as pointed out for the Ca and Sr disilicides by several authors [12-14], the occurrence of a negatively charged covalently bonded Si-Si network led to the formation of Zintl phases [15,12,13].

The binary Sr-Si system shows four standard pressure intermediate phases: $Sr_{2}Si$, $Sr_{5}Si_{3}$, SrSi and $SrSi_{2}$. Experimentally these phases take the orthorhombic ($Sr_{2}Si$ oP12 anti-$PbCl_{2}$-type and SrSi oC8 CrB-type), tetragonal (tI32, $Cr_{3}B_{5}$-type) and cubic (cP12, $SrSi_{2}$-type) lattices at room temperature and standard (1 bar) pressure [13]. The disilicide phase, $SrSi_{2}$, also shows a tetragonal high temperature [13] and high pressure [16] polymorph structure (tI12, $\alpha$-ThSi$_{2}$-type), similar to $CaSi_{2}$.

The thermodynamic stability at high temperature of the strontium silicides has been recently investigated by Balducci et al. [17] by experimental tensimetric techniques and the heats of formation of all the intermediate phases have been obtained.

From the computational side only a few, incomplete investigations of the energetics of the strontium silicides have been

* Corresponding author. Tel.: +39 06 49913640; fax: +39 06 49913951.
E-mail address: sergio.brutti@uniroma1.it (S. Brutti).

0925-8388/$ - see front matter © 2007 Elsevier B.V. All rights reserved.
doi:10.1016/j.jallcom.2007.03.023

reported by Imai et al. [18–20], Becker et al. [21] and Brutti et al. [14]. Imai et al. studied the electronic structures of the $Sr_2Si$, SrSi and $SrSi_2$ standard pressure phases by DFT calculations using generalized gradient approximation (GGA), also investigating the lattice stability of the disilicide phase. Becker et al. studied the structural and electronic properties of compounds crystallizing in a TII- or CrB-type lattices, including the $Sr_2Si$ phase by DFT-GGA calculations over a wide pressure range. In previous work [14] we studied in detail the lattice stability and the electronic structure of the $SrSi_2$ phase, in comparison with the $CaSi_2$ compound, by DFT-GGA calculations.

This paper presents a systematic study of the lattice stability of the intermediate phases of the Sr–Si system using first principle density functional theory (DFT) calculations. Nine compositions (i.e. $Sr_3Si$, $Sr_2Si$ $Sr_5Si_3$, $Sr_5Si_4$, SrSi, $Sr_3Si_4$, $Sr_3Si_5$, $SrSi_2$, $SrSi_3$) have been considered involving 26 different crystal lattices, predicting the ground state structures and the occurrence of the high pressure polymorphs and high volume structures. The corresponding heats of formation and equilibrium crystal structures have been computed using the generalized-gradient approximation (PW91-GGA) and compared with the sparse available literature. We should note that the results for the $SrSi_2$ phases have already been presented elsewhere [14] and are only partially reported here for the sake of completeness. Finally the bonding characteristics of the ground states of the Sr–Si phases have been discussed by analyzing the total (DOS) and partial (PDOS) electronic densities of states and the resultant charge transfers.

## 2. Computational details

The electronic structure calculations of the strontium silicides have been performed using the ab-initio total-energy program VASP (Vienna Ab-initio Simulation Program), developed at the Institute für Materialphysik (Universität Wien) [22–24]. The projector augment wave (PAW) method by Blochl [25] as implemented by Kresse and Joubert [26] has been employed. The PAW method is an all-electron DFT technique within the frozen core approximation. The generalized-gradient approximation PW91 functional [27] was applied for all calculations. Here we adopted the standard version of the PAW potentials for both Si and Sr atoms: these are supplied and recommended by the VASP compilers. For Sr 10 electrons were included in the valence shell whereas 4 electrons were considered in the basis set for Si. $\Gamma$-centered Monkhorst-Pack (MP) $k$-point grids [28] were used in all total energy calculations for the reciprocal-space integration. The number of irreducible $k$-points was different for the various lattices considered due to the different symmetries: these are listed in Table 1. The number of $k$-points and the kinetic energy cut-off have been assessed in order to achieve an accuracy in the total energies of better than $0.2\ \text{kJ mol at}^{-1}$; this implied an energy cut-off of 380 eV. The linear tetrahedron method [29] has been adopted to improve the convergence of the total energy with respect to the number of $k$-points. All structural optimizations have been carried out by full relaxation of the cell and internal parameters.

<table>
<caption>Table 1<br>Composition, Pearson symbol, prototype lattice, number of irreducible $k$-points and heats of formation for the 20 new structures considered and for the 6 disilicide lattices already reported in Brutti et al. [14] for the $SrSi_2$ phase</caption>
<thead>
<tr>
<th>Composition</th>
<th>Pearson symbol</th>
<th>Prototypeᵃ</th>
<th>$k$-Points</th>
<th>Heats of formation [kJ mol at⁻¹]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Sr_3Si$</td>
<td>cP4</td>
<td>anti-$AuCu_3$</td>
<td>35</td>
<td>−6.5</td>
</tr>
<tr>
<td></td>
<td>tP4</td>
<td>anti-tetra-$AuCu_3$</td>
<td>75</td>
<td>−6.5</td>
</tr>
<tr>
<td></td>
<td>cP8</td>
<td>$Cr_3Si$</td>
<td>35</td>
<td>11.0</td>
</tr>
<tr>
<td>$Sr_2Si$</td>
<td>cF12</td>
<td>$Mg_2Si$</td>
<td>35</td>
<td>−35.0</td>
</tr>
<tr>
<td></td>
<td>hP6</td>
<td>$Ni_2In$</td>
<td>125</td>
<td>−23.7</td>
</tr>
<tr>
<td></td>
<td>oP12 (GS)</td>
<td>anti-$PbCl_2$</td>
<td>125</td>
<td>−37.6</td>
</tr>
<tr>
<td>$Sr_5Si_3$</td>
<td>tP32</td>
<td>$Ba_5Si_3$</td>
<td>18</td>
<td>−39.8</td>
</tr>
<tr>
<td></td>
<td>hP16</td>
<td>$Mn_5Si_3$</td>
<td>32</td>
<td>−27.5</td>
</tr>
<tr>
<td></td>
<td>tI32</td>
<td>$Mo_5Si_3$</td>
<td>18</td>
<td>−29.5</td>
</tr>
<tr>
<td></td>
<td>tI32 (GS)</td>
<td>$Cr_5B_3$</td>
<td>40</td>
<td>−40.2</td>
</tr>
<tr>
<td>$Sr_5Si_4$</td>
<td>oP36</td>
<td>$Sm_5Ge_4$</td>
<td>18</td>
<td>−37.3</td>
</tr>
<tr>
<td>SrSi</td>
<td>tP2</td>
<td>$AuCu$</td>
<td>75</td>
<td>−10.1</td>
</tr>
<tr>
<td></td>
<td>oC8 (GS)</td>
<td>CrB</td>
<td>125</td>
<td>−46.7</td>
</tr>
<tr>
<td></td>
<td>oP8</td>
<td>FeB</td>
<td>64</td>
<td>−45.9</td>
</tr>
<tr>
<td></td>
<td>cP2</td>
<td>$CsCl$</td>
<td>35</td>
<td>−8.7</td>
</tr>
<tr>
<td>$Sr_3Si_4$</td>
<td>hP42</td>
<td>$Ca_3Si_4$</td>
<td>15</td>
<td>−40.6</td>
</tr>
<tr>
<td></td>
<td>tP28</td>
<td>$Ba_3Si_4$</td>
<td>18</td>
<td>−39.3</td>
</tr>
<tr>
<td>$Sr_3Si_5$</td>
<td>hP8</td>
<td>$Th_3Pd_5$</td>
<td>125</td>
<td>−37.3</td>
</tr>
<tr>
<td>$SrSi_2$</td>
<td>hR3</td>
<td>$AlB_2$</td>
<td>60</td>
<td>−29.3</td>
</tr>
<tr>
<td></td>
<td>oP24</td>
<td>$BaSi_2$</td>
<td>27</td>
<td>−32.3</td>
</tr>
<tr>
<td></td>
<td>hR18</td>
<td>$CaSi_2$</td>
<td>85</td>
<td>−34.5</td>
</tr>
<tr>
<td></td>
<td>hP3</td>
<td>$CdI_2$</td>
<td>88</td>
<td>−35.6</td>
</tr>
<tr>
<td></td>
<td>cP12 (GS)</td>
<td>$SrSi_2$</td>
<td>120</td>
<td>−35.8</td>
</tr>
<tr>
<td></td>
<td>tI12</td>
<td>$\alpha$-$ThSi_2$</td>
<td>75</td>
<td>−35.7</td>
</tr>
<tr>
<td>$SrSi_3$</td>
<td>cP4</td>
<td>$AuCu_3$</td>
<td>35</td>
<td>21.7</td>
</tr>
<tr>
<td></td>
<td>tP4</td>
<td>tetra-$AuCu_3$</td>
<td>75</td>
<td>21.7</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">GS, ground state.<br>ᵃ All proto-type structures have been retrieved from Villars' compilation [35].</td>
</tr>
</tfoot>
</table>

The heat of formation per mole of atoms, $\Delta H$, of the generic compound $Sr_xSi_y$ is defined by:

$$
\Delta H=\frac{\left({ }^{\nu} E_{\text {coh }}^{S r_{x} S i_{y}}\right)-x\left({ }^{\text {fcc }} E_{\text {coh }}^{S r}\right)-y\left({ }^{\text {diamond }} E_{\text {coh }}^{S i}\right)}{x+y} \tag{1}
$$

where $^{\nu} E_{\text {coh }}^{S r_{x} S i_{y}}$ is the calculated cohesive energy per formula unit of the compound in the $\nu$ structure, $^{\text {fcc }} E_{\text {coh }}^{S r}$ and $^{\text {diamond }} E_{\text {coh }}^{S i}$ are the cohesive energies per moles of atom of the bulk elements in their ground state structures, namely fcc for Sr and diamond for Si. The Wigner–Seitz radii used in the partial density of states (PDOS) and charge transfer calculations were computed by assuming that the ratio between the atomic volumes of the metals and Si was equal to their electronegativity ratio [30].

## 3. Results and discussion

### 3.1. Lattice stability of the Sr silicides

As already mentioned the DFT calculations were performed with respect to nine compositions (i.e. $Sr_3Si$, $Sr_2Si$ $Sr_5Si_3$, $Sr_5Si_4$, SrSi, $Sr_3Si_4$, $Sr_3Si_5$, $SrSi_2$, $SrSi_3$) involving 26 different crystal lattices. The computed crystal structures have been

![](./images/812002393582469120_3.jpg)

Fig. 1. Calculated heats of formation [kJ mol at $^{-1}$] for the Sr-Si intermediate compounds.

selected on the basis of the phenomenological Pettifor structure maps [31-33] and by considering the experimentally observed compositions and crystal structures for the similar alkaline-earth and Yb silicides [12,16,34].

A summary of the computed structures for each composition, the corresponding number of computed irreducible $k$-points and the resulting heats of formation is presented in Table 1. Results are also reported in Fig. 1 where the heat of formation of all the computed compositions and structures have been plotted against the composition, at% Si (atomic percent of silicon) and compared with the experimental literature data [17].

Within the ensemble of the considered compositions and structures, the GGA calculations correctly predict the stability at standard pressure of the sole experimentally observed compositions in their proper structures, i.e. $Sr_{2}Si$ (oP12), $Sr_{5}Si_{3}$ (tI32-$Cr_{5}B_{3}$), $SrSi$ (oC8) and $SrSi_{2}$ (cP12). As clearly shown in Fig. 1, all the other computed structures for the same or different compositions have been found to be thermodynamically metastable compared to the aforementioned ground state lattices. Even those compositions that in the very similar Ca-Si [12] and Yb-Si [34] systems crystallize in thermodynamically stable lattices such as $Ca_{3}Si_{4}$ (hP42), $Yb_{5}Si_{4}$ (oP36), $Yb_{3}Si_{4}$ (tP28) or $Yb_{3}Si_{5}$ (hP8), in the case of the strontium silicides are predicted not to form any stable compound. Indeed, for the $Sr_{5}Si_{4}$, $Sr_{3}Si_{4}$ and $Sr_{3}Si_{5}$ compositions, the corresponding mixtures of $Sr_{5}Si_{3}(tI32 Cr_{5}B_{3}$-type)/SrSi(oC8), in the first case, and $SrSi(oC8)/SrSi_{2}(cP12)$, for the last two, are more stable by 6.5, 1.4 and $1.2 kJ mol at^{-1}$, respectively, compared to the oP36, hP42 and hP8 lattices, well beyond the computational precision of $0.2 kJ mol at^{-1}$. Finally for the case of the strontium disilicide, as already discussed in ref. [14], the experimental ground state cP12 structure is slightly more stable than the tI12 lattice: however, we can only arbitrarily assign the cubic structure as the ground state as the energy difference is only $0.12 kJ mol at^{-1}$, which is below the convergence accuracy achieved using the current energy cut-off and $k$-point sampling.

Finally the computed heats of formation for the ground state structures are in good agreement with both the only available experimental determination by Balducci et al. [17] $(-39.7\pm 3.2$, $-43.8\pm 3.6$, $-51.7\pm 4.1$ and $-42.7\pm 4.3 kJ mol at^{-1}$ for $Sr_{2}Si$ (oP12), $Sr_{5}Si_{3}$ (tI32-$Cr_{5}B_{3}$), $SrSi$ (oC8) and $SrSi_{2}$ (cP12), respectively) and the previous DFT-LDA calculations by Imai et al. [18] $(-35.3$, $-43.5$ and $-34.7 kJ mol at^{-1}$ for $Sr_{2}Si$ (oP12), $SrSi$ (oC8) and $SrSi_{2}$ (cP12), respectively).

### 3.2. Ground state structures and high pressure polymorphs
Among the computed compositions and structures, we have investigated the $Sr_{2}Si$, $Sr_{5}Si_{3}$ and $SrSi$ phases for possible phase transitions under pressure between the lattices considered. The corresponding binding energy curves are shown in Fig. 2. We see that these GGA calculations predict, for the halfsilicide phase $Sr_{2}Si$, beside the ground state lattice oP12, the occurrence of a hexagonal polymorphic structure, hP6 at high pressure with a computed transition pressure of 5.5 GPa. For the $Sr_{5}Si_{3}$ phase a transition from the tetragonal tI32 ground state ($Cr_{5}B_{3}$ prototype) to a very similar tetragonal tI32 lattice ($Mo_{5}Si_{3}$ prototype) is predicted to occur at about 19.9 GPa. Finally the monosilicide phase SrSi it is expected to undergo two sequential high-pressure transitions from the orthorhombic oC8 ground state, through an oP8 lattice, to a tP2 tetragonal structure at 11.8 and 60 GPa, respectively. This last transition pressure, although only indicative, is in agreement with the previous theoretical data by Becker et al. [21] that predicted, for all the AEM monosilicides, oP8 $\rightarrow$ tP2 transition pressures higher than 40 GPa. No further comparison with the literature is possible owing to the lack of any other experimental or theoretical investigation of the high-pressure transitions for these phases.

A summary of the computed equilibrium structures, lattice parameters, heats of formation and transition pressures for the ground states and the high pressure polymorphs of the $Sr_{2}Si$, $Sr_{5}Si_{3}$ and $SrSi$ phases is presented in Table 2. The lattice parameters, cell and internal parameters, for the ground states for all

![](./images/812002393582469120_4.jpg)

Fig. 2. Binding energy curves for (a) $Sr_{2}Si$, (b) $Sr_{5}Si_{3}$ and (c) SrSi phases.

<table>
<caption>Table 2 Equilibrium structures, heats of formation and transition pressures for predicted ground states and high-pressure polymorphs for $Sr_{2}Si$, $Sr_{5}Si_{3}$ and SrSi phases. Available literature values (ref. [13] for the lattice parameters and ref. [17] for the heats of formation) are reported in parentheses</caption>
<thead>
<tr>
<th>Phase</th>
<th>Lattice</th>
<th colspan="3">Lattice parameters</th>
<th rowspan="2">Internal parameters</th>
<th rowspan="2">$\Delta_{f}H^{\circ}_{0K}$ [kJ mol at$^{-1}$]</th>
<th rowspan="2">Transition pressure [GPa]</th>
</tr>
<tr>
<th></th>
<th></th>
<th>$a$ [Å]</th>
<th>$b$ [Å]</th>
<th>$c$ [Å]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Sr_{2}Si$</td>
<td>oP12</td>
<td>8.105 (8.111)</td>
<td>5.135 (5.132)</td>
<td>9.596 (9.545)</td>
<td>$x_{Si}=0.7522$; $z_{Si}=0.3973$; $x_{Sr(1)}=0.1507$;</td>
<td>$-37.6\ (-39.7)$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>hP6</td>
<td>5.469</td>
<td></td>
<td>6.697</td>
<td>$z_{Sr(1)}=0.4223$; $x_{Sr(2)}=0.019$; $z_{Sr(2)}=0.8262$</td>
<td>$-23.7$</td>
<td>5.5</td>
</tr>
<tr>
<td>$Sr_{5}Si_{3}$</td>
<td>tI32$^{\text{a}}$</td>
<td>8.073 (8.100)</td>
<td></td>
<td>15.845 (15.728)</td>
<td>$x_{Si}=0.3922$; $x_{Sr}=0.1802$; $z_{Sr}=0.1409$</td>
<td>$-40.2\ (-43.8)$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>tI32$^{\text{b}}$</td>
<td>12.636</td>
<td></td>
<td>6.2844</td>
<td>$x_{Si}=0.1547$; $x_{Sr}=0.0858$; $y_{Sr}=0.2109$</td>
<td>$-29.5$</td>
<td>19.9</td>
</tr>
<tr>
<td>SrSi</td>
<td>oC8</td>
<td>4.826 (4.814)</td>
<td>11.337 (11.288)</td>
<td>4.052 (4.040)</td>
<td>$x_{Si}=0.5639$; $x_{Sr}=0.8610$</td>
<td>$-46.7\ (-51.7)$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>oP8</td>
<td>8.903</td>
<td>4.045</td>
<td>6.131</td>
<td>$x_{Si}=0.0322$; $z_{Si}=0.6078$; $x_{Sr}=0.1808$;</td>
<td>$-45.9$</td>
<td>11.8</td>
</tr>
<tr>
<td></td>
<td>tP2</td>
<td>4.926</td>
<td></td>
<td>4.414</td>
<td>$z_{Sr}=0.1087$</td>
<td>$-10.1$</td>
<td>60</td>
</tr>
<tr>
<td colspan="8">$^{\text{a}}$ $Cr_{5}B_{3}$ prototype.</td>
</tr>
<tr>
<td colspan="8">$^{\text{b}}$ $Mo_{5}Si_{3}$ prototype.</td>
</tr>
</tbody>
</table>

![](./images/812002393582469120_5.jpg)

Fig. 3. Density of the states [states eV⁻¹ formula unit⁻¹] and atomic partial density of states [states eV⁻¹ at⁻¹] for the ground state structures of (a–c) Sr₂Si (oP12), (d–f) Sr₅Si₃ (tI32 Cr₅B₃-type) and (g–i) SrSi (oC8) compounds.

compositions are accurately predicted: the deviation from the experimental data is in all cases smaller than 1%. As a consequence the computed equilibrium atomic volumes, i.e. 33.3, 32.3 and 27.7 Å³ for Sr₂Si, Sr₅Si₃ and SrSi, respectively, are in very good agreement with the experimental values 33.1, 32.2 and 27.4 Å³, derived from the crystallographic data by Palenzona et al. [13].

### 3.3. Sr–Si chemical bonding

The chemical bond between Sr and Si is predicted to be mainly ionic if we simply consider the difference in their electronegativity [30], i.e. $\varepsilon_{\mathrm{Si}}-\varepsilon_{\mathrm{Sr}}=\Delta \varepsilon=0.8$ Pauling units. As a consequence a large charge transfer from the Sr to the Si atoms is expected to occur and be reflected in both the behavior of the computed electronic density of states (DOS) and the charge densities. For the sake of simplicity the ground state structures of the Sr₂Si, Sr₅Si₃ and SrSi phases, i.e. oP12, tI32 (Cr₅B₃-type) and oC8 lattices respectively, will be referred by the simple chemical formula in this section.

The total and partial electronic DOS for the Sr₂Si, Sr₅Si₃ and SrSi phases are presented in Fig. 3. We see that the halfsilicide phase, Sr₂Si, is predicted to be an insulator with a band gap of 0.29 eV. Given the lack of any experimental determination, this is to be compared with the earlier result by Imai et al. [19] of 0.40 eV (direct band gap at $\Gamma$). In a previous paper Imai et al. [18] estimated from the DOS plot a band gap for the same compound of 0.75 eV apparently using the same computational method and conditions. However, our value is to be considered more reliable owing to the more accurate convergence criteria assumed: in terms of the computed total energies our computational accuracy is 0.2 meV at⁻¹ to be compared with the lower limit of 10 meV at⁻¹ estimated by Imai et al. in ref. [18].

The Sr₅Si₃ and SrSi phases are metals with DOS at the Fermi energy ($E_{\text{Fermi}}$) of 0.37 and 0.32 states eV⁻¹ at⁻¹ for Sr₅Si₃ and SrSi, respectively. For sake of completeness it is to be noted that the disilicide phase, SrSi₂, is predicted to be a semimetal with a narrow minimum at the Fermi energy (for more details see ref. [14]).

The analysis of the partial DOS clearly shows that a large charge transfer occurs between Sr and Si. The computed atomic charges are summarized in Table 3. Except for the SrSi₂ phase in which the charge transfer is almost complete, in all the other ground state structures the ionicity of the chemical bond is about 70% and the charge transfer is smaller than that expected for an ideal Zintl-phase of the same composition.

In Fig. 4 three planar sections of the crystal structures of the Sr₂Si, Sr₅Si₃ and SrSi phases are reported showing part of the polyanionic sublattices, and the corresponding charge density plots. It is interesting to observe the occurrence of a partially covalent bond between the Si atoms in the Sr₅Si₃ and SrSi ground states whereas the Si atoms appears as isolated anions in Sr₂Si (Si–Si mean distance $\sim 5$ Å). Quantitatively in the Sr₅Si₃ ground state, the pairs of silicon atoms form partially cova-

<table>
<caption>Table 3
Computed mean charge on the Sr and Si atoms, percentage of ionic character for the Sr–Si bonding, predicted band gap [eV] of Sr₂Si, for the standard pressure ground state silicides; in the last row the Si charge for the case of an ideal Zintl compound is reported (under this assumption Sr are always +2 charged)</caption>
<thead>
<tr>
<th>
</th>
<th>
Sr₂Si
</th>
<th>
Sr₅Si₃
</th>
<th>
SrSi
</th>
<th>
SrSi₂ᵃ
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Sr
</td>
<td>
1.48
</td>
<td>
1.52
</td>
<td>
1.38
</td>
<td>
1.94
</td>
</tr>
<tr>
<td>
Si
</td>
<td>
−2.97
</td>
<td>
−2.53
</td>
<td>
−1.38
</td>
<td>
−0.97
</td>
</tr>
<tr>
<td>
%Ionic
</td>
<td>
74
</td>
<td>
76
</td>
<td>
69
</td>
<td>
97
</td>
</tr>
<tr>
<td>
Band gap
</td>
<td>
0.29
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Zintl-phase Si charge (8-N rule)
</td>
<td>
−4
</td>
<td>
−3.33
</td>
<td>
−2
</td>
<td>
−1
</td>
</tr>
</tbody>
</table>
<p>ᵃ Data reported in ref. [14].</p>

lently bonded dimers between negatively charged Si⁻².⁵³ ions, whereas the SrSi lattice shows isolated silicon zig-zag chains along the (0 0 1) direction. The occurrence of this covalent chemical interaction between silicon atoms in the Sr₅Si₃ and SrSi compounds is clear also from the analysis of the corresponding partial Si DOS plots. Indeed in both, Fig. 3e and h, large bands with main sp character due to a direct Si–Si interaction can be observed from $-3$ eV to the $E_{Fermi}$ for Sr₅Si₃, from $-10$ eV to $-5$ eV and from $-4$ eV to $E_{Fermi}$ for the SrSi phase.

Finally it is interesting to note that, as discussed in ref. [14], the strontium disilicide groundstate cP12 shows a three-dimensional arrangement of the Si sublattice in which flat Si₄ trigonal pyramids are twisted against each other along the c-axis. Moreover, as in this last case a complete charge transfer occurs between Sr and Si (see Table 3) and the silicon sublattice is a true three-dimensional network, the SrSi₂ oP12 phase is a true Zintl-phase in its original definition by Zintl [15] (isolated cations stuffed within a three dimensional negatively charged three-dimensional network), whereas all the other strontium silicides, except the halfsilicide Sr₂Si oP12, can be assimilated as Zintl-phases only in its widest present definition (compounds formed by an sp element, electronically balanced, with no homogeneity width, semiconductor or poor conductor, diamagnetic and brittle) [15]. In conclusion is to be noted that in the case of the Sr₅Si₃, where the general Zintl-phase 8-N rule gives a broken number (silicon formal charge would be $-3.33$), the application of the Zintl-Klemm-Bussmann concepts may suggest the occurrence of structurally distinguished Si atoms beyond the assumed symmetry of the lattice. This could be a clue of the existence of a superstructure. However in present calculations, the structural relaxations were performed keeping constant the symmetry of the lattices without considering supercells or allowing distortions. This choice did not allow for the observation of the occurrence of possible superstructures with symmetry reduction, starting from the basic highly symmetric ground state lattices. We believe that further work is needed in order to investigate this issue both from theoretical and experimental points of view.

![](./images/812002393582469120_6.jpg)

Fig. 4. Schematic sketches of three planar sections of the ground state crystal structures of (a) Sr₂Si (oP12), (b) Sr₅Si₃ (tI32 Cr₅B₃-type) and (c) SrSi (oC8) phases and corresponding charge density maps. (Asterisks (*) indicate out of plane Sr atoms, in the charge Sr₂Si (4 0 0) density map these correspond to the white spots.)

## 4. Conclusions

In this paper a systematic study of the lattice stability of the intermediate phases of the Sr–Si system has been presented using first principle density functional theory (DFT) calculations in the GGA approximation. Nine compositions have been considered, involving 26 different crystal lattices, predicting the ground state structures and the occurrence of new high-pressure polymorphs for the Sr₂Si, Sr₅Si₃ and SrSi phases. The corresponding heats of formation and equilibrium structures have been computed and compared with the literature data. The Sr–Si bonding characteristics in the ground states and the occurrence of Zintl phases have been discussed by analyzing the DOS and PDOS plots, charge density maps and the computed charge transfers for all the strontium silicides.

## Acknowledgements

Sergio Brutti would like to thank the Department of Materials at the University of Oxford for its hospitality during a 6 months visit where this work was carried out in the Materials Modeling Laboratory. Duc Nguyen-Manh was supported by EURATOM and the United Kingdom EPSRC.

## References

[1] K. Miyake, Y. Makita, Y. Maeda, T. Suemasu, Symposium on silicide kankyo semiconductors-ecologically friendly semiconductors-opto-electronic and energy research for next generation, Thin Solid Films 381 (Special issue (2)) 2001 vii.

[2] Y. Makita, in: R.D. Mc Connel (Ed.), The First NREL Conference on “Future Generation Photovoltaic Technologies, AIP, New York, 1997.

[3] K. Miura, T. Ohishi, T. Inaba, Y. Mizuyoshi, N. Takagi, T. Matsuyama, Y. Momose, T. Koyama, Y. Hayakawa, H. Tatsuoka, Thin Solid Film 508 (2006) 74–77.

[4] K. Morita, M. Kobayashi, T. Suemasu, Jpn. J. Appl. Phys. Part 2 45 (2006) L390-L392.

[5] Y. Inomata, T. Nakamura, T. Suemasu, F. Hasegawa, Jpn. J. Appl. Phys. Part 1 43 (2004) 4155-4156.

[6] H. Tatsuoka, N. Takagi, S. Okaya, Y. Sato, T. Inaba, T. Ohishi, A. Yamamoto, T. Matsuyama, H. Kuwabara, Thin Solid Films 461 (2004) 57-63.

[7] J.L. Wang, Z. Zeng, Q.Q. Zheng, Phys. C 408-410 (2004) 264-265.

[8] I.R. Shein, N.I. Medvedeva, A.L. Ivanovskii, J. Phys. Condens. Matter 15 (2003) 1541-1545.

[9] I.R. Shein, N.I. Medvedeva, A.L. Ivanovskii, Comput. Mater. Sci. 36 (2006) 203-206.

[10] P. Poulemonde, Ch. Adessi, X. Blase, A. San Miguel, J.L. Tholence, Phys. Rev. B 71 (2005) 034504.

[11] Y. Mudryk, P. Rogl, C. Paul, S. Berger, E. Bauer, G. Hilscher, C. Godart, H. Noel, A. Saccone, R. Ferro, Phys. B 328 (2003) 44-48.

[12] P. Manfrinetti, M.L. Fornasini, A. Palenzona, Intermetallics 8 (2000) 223-228.

[13] A. Palenzona, M. Pani, J. Alloys Compd. 373 (2004) 214-219.

[14] S. Brutti, D. Nguyen Manh, D.G. Pettifor, Intermetallics 14 (2006) 1472-1486.

[15] S.C. Sevov, Zintl phases, in: J.H. Westbrook, R.L. Fleisher (Eds.), Inter- metallic Compounds, vol. 3, John Wiley & Sons, 2002.

[16] M. Imai, T. Kikegawa, Chem. Mater. 15 (2003) 2543-2551.

[17] C. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona, M Pani, Intermetallics 14 (2006) 578-583.

[18] Y. Imai, A. Watanabe, Intermetallics 10 (2002) 333-341.

[19] Y. Imai, A. Watanabe, M. Mukaida, J. Alloys Compd. 358 (2003) 257-263.

[20] Y. Imai, A. Watanabe, Intermetallics 14 (2006) 666-671.

[21] D. Becker, H.P. Beck, Z. Kristallogr. 218 (2004) 348-358.

[22] G. Kresse, J. Hafner. Phys. Rev. B 49 (1994) 14251-14269.

[23] G. Kresse, J. Furthmuller, Comp. Mater. Sci. 6 (1996) 15-50.

[24] G. Kresse, J. Furthmuller, Phys. Rev. B 54 (1996) 11169-11186.

[25] P.E. Blochl, Phys. Rev. B 50 (1994) 17953-17979.

[26] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758-1775.

[27] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671-6687.

[28] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188-5192.

[29] A.H. MacDonald, S.H. Vosko, P.T. Coleridge, J. Phys. C Solid State Phys. 12 (1979) 2991-3002.

[30] L. Pauling, The Nature of the Chemical Bond, third ed., Cornell University, USA, 1960.

[31] D.G. Pettifor, J. Phys. C Solid State Phys. 19 (1986) 285-313.

[32] D.G. Pettifor, J. Phase Equilib. 17 (1996) 384-395.

[33] D.G. Pettifor, J. Phys. Condens. Matter 15 (2003) V13-V15.

[34] A. Palenzona, P. Manfrinetti, S. Brutti, G. Balducci, J. Alloys Compd. 348 (2002) 100-105.

[35] P. Villars, L.D. Calvert, Pearson's Handbook of Crystallographic Data for Intermetallics Phases, vol. 1, first ed., Metals Park, OH, 1985.