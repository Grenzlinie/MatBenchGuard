# Synthetic Access to Atomically Dispersed Metals in Metal-Organic Frameworks via a Combined Atomic-Layer-Deposition-in-MOF and Metal-Exchange Approach

Rachel C. Klet, $^{\dagger,\parallel}$ Timothy C. Wang, $^{\dagger,\parallel}$ Laura E. Fernandez, $^{\S}$ Donald G. Truhlar, $^{*, \S}$ Joseph T. Hupp, $^{*, \dagger}$ and Omar K. Farha $^{*, \dagger, \ddagger}$

$^{\dagger}$Department of Chemistry, Northwestern University, 2145 Sheridan Road, Evanston, Illinois 60208-3113, United States
$^{\ddagger}$Department of Chemistry, Faculty of Science, King Abdulaziz University, Jeddah, Saudi Arabia
$^{\S}$Department of Chemistry, Minnesota Supercomputing Institute, and Chemical Theory Center, University of Minnesota, 207 Pleasant Street SE, Minneapolis, Minnesota 55455-0431, United States

S Supporting Information

**ABSTRACT:** The combination (AIM-ME) of atomic layer deposition in metal-organic frameworks (MOFs) and metal exchange (ME) is introduced as a technique to install dispersed metal atoms into the mesoporous MOF, NU-1000. Zn-AIM, which contains four Zn atoms per $Zr_6$ node, has been synthesized through AIM and further characterized through density functional calculations to provide insight into the possible structure. Zn-AIM was then subjected to modification via transmetalation to yield uniform porous materials that present nonstructural Cu, Co, or Ni atoms.

![](./images/814555289998065664_1.jpg)

## INTRODUCTION

Atomically dispersed metals on solid supports are an emerging class of catalysts ranging from single atoms to anchored mononuclear transition metal complexes. $^{1-4}$ As the size of a supported catalyst is reduced from particles and clusters to single atoms or ions, its catalytic properties often change, thereby opening up the possible discovery of new catalysts. Thus, there is significant interest in new methods for the synthesis of materials with catalytically active, atomically dispersed metals. Ideally, these methods would allow for the preparation of materials containing active sites that are spatially isolated, uniformly distributed, and characterizable. $^{2,3}$

We have recently reported a method, known as AIM (ALD in MOFs), $^{5-7}$ for installing metals with atomic precision into metal-organic frameworks (MOFs) using atomic layer deposition (ALD). This method allows for self-limiting installation of single metal sites onto the nodes of the Zr based MOF NU-1000. NU-1000 is a crystalline porous material consisting of $Zr_6(\mu_3-OH)_4(\mu_3-O)_4(OH)_4(OH_2)_4$ nodes and tetratopic 1,3,6,8-(p-benzoate)pyrene (TBAPy$^{4-}$) linkers; it is an ideal platform for supporting atomically dispersed metals due to its spatially isolated grafting sites (in the form of $-OH$ and $-OH_2$ sites on the node), high thermal and chemical stability (for potentially demanding catalytic reactions), and hexagonal 31 Å mesopores (for facile diffusion of reactants and products throughout the material). $^{7-10}$ Additionally, the crystalline and periodic nature of the MOF facilitates characterization and ensures a uniform distribution of active sites. Thus, AIM with NU-1000 appears to be an excellent route for accessing atomically dispersed metals on a solid support for catalytic applications.

Although AIM appears to be accessible with a wide variety of commercially available ALD precursors, $^{5-7}$ we sought a complementary method to access single-atom metal sites. An alternative route may allow for installation of metal atoms for which no ALD precursor (or MOF-compatible precursor) is currently available and may also provide additional and potentially more economical routes to desired materials (particularly in cases in which ALD precursors are costly). To this end, we targeted a material, namely, Zn-AIM, that could be facilely and reproducibly obtained, and then modified via metal exchange with simple metal salts to obtain new materials.

Metal exchange in MOFs has previously been explored to exchange metal atoms in the node of the material or metal containing struts. $^{11,12}$ For our purposes, we sought only to exchange the atoms installed by AIM (i.e., nonstructural atoms) while leaving nodes intact, since the MOF in this case is serving as a scaffold. On the basis of literature precedents involving transmetalation in MOF nodes, $^{11,12}$ as well as the Irving Williams series, $^{13}$ we expected that $Zn^{2+}$ installed by ALD could be readily exchanged for other $M^{2+}$ metal ions. Notably, $ZnEt_2$ (used to synthesize Zn-AIM) is an economical and reliable ALD precursor. Here, we describe our success in installing dispersed single atoms of Cu, Ni, and Co by a combined AIM

Received: December 17, 2015
Revised: January 28, 2016

and metal-exchange (AIM-ME) approach starting from NU-1000 Zn-AIM material (Scheme 1).

Scheme 1. Schematic Illustration of AIM-Installed Metal Atoms in the Mesopores of NU-1000 Undergoing Metal Exchange

![](./images/814555289998065664_2.jpg)

## EXPERIMENTAL SECTION
General Procedure for Screening Metal-Exchange Conditions. Zn-AIM (10 mg) was added to a 2 dram vial, and 2.5 mL of 0.01 M methanolic metal salt stock solution was added to the vial via syringe. Reactions were left at room temperature ($CuCl_2$·$2H_2O$) or incubated in an oven set to 60 °C ($NiCl_2$·$6H_2O$ or $CoCl_2$·$6H_2O$). After the desired reaction time (3, 6, or 20 h), the solution was pipetted from the reaction vial and replaced with fresh methanol three times over the course of 1 day. The solution was then replaced with acetone, and after soaking for 8 h, the solution was pipetted out and the microcrystalline solid was dried in a vacuum oven at 60 °C.

Larger Scale Metal-Exchange Procedure. Zn-AIM (40 mg) was added to a 6 dram vial, and 10 mL of 0.01 M methanolic metal salt stock solution was added to the vial via syringe. Reactions were left at room temperature ($CuCl_2$·$2H_2O$) or incubated in an oven set to 60 °C ($NiCl_2$·$6H_2O$ or $CoCl_2$·$6H_2O$) for 20 h. After 20 h, the solution was pipetted from the reaction vial and replaced with fresh methanol three times over the course of 1 day. The solution was then replaced with fresh acetone three times over the course of 1 day. After solvent exchange, the solution was pipetted out, and the microcrystalline solid was dried in a vacuum oven at 60 °C. The samples were outgassed on a Micromeritics SmartVacPrep at room temperature (Co-AIM-ME) or 60 °C (Cu-AIM-ME and Ni-AIM-ME) for 12 h.

Optimizations of Structures Using DFT Calculations. Gaussian $09^{14}$ calculations were performed with the M06-L$^{15}$ density functional, a 6-31G(d) basis set for the carbon, hydrogen, and oxygen atoms, and the SDD$^{16}$ basis sets and effective core potentials for zinc and zirconium atoms. A cluster model of NU-1000 from ref 8 was used (150 atoms) in the gas-phase optimizations as the bare node and was used as the starting point for each calculation where the zinc precursor was added. For the optimizations, the carbons in the eight linkers of the cluster model were frozen while all other atoms were free. Electronic energies ($E$, including nuclear repulsion but excluding nuclear motion) and free energies ($G$, including nuclear motion at 383 K) were calculated; energies of reaction were determined by adding the energies of the products and subtracting the energies of the reactants.

## RESULTS AND DISCUSSION
Modified Synthesis of Zn-AIM. Further studies with AIM have revealed that dehydration of the node can alter the stoichiometry of deposition of metal ions. In a typical procedure, approximately 40 mg of NU-1000 is loaded into a home-built stainless steel powder holder and allowed to equilibrate in the reactor for 30 min prior to ALD deposition. Depending on the temperature of the ALD reactor during equilibration and deposition, we observed different ratios of incorporated metal ions (Zn) to $Zr_6$. (see the Supporting Information (SI), Figure S1). ALD performed with lower reactor temperatures prevented dehydration of the $Zr_6$ node and loss of grafting sites ($-OH$ and $-OH_2$ groups), resulting in consistent deposition of four Zn atoms per $Zr_6$ node. We determined an optimal temperature for ALD deposition of $ZnEt_2$ in NU-1000 to be 110 °C; all of the Zn-AIM material used for metal exchange was synthesized using this modified procedure. See the SI for details.

Quantum Mechanical Investigation of the Structure of Zn-AIM. To better understand the geometry and coordination environment of the Zn atoms in Zn-AIM, the reaction of $ZnEt_2$ with the NU-1000 node was modeled using quantum mechanical density functional calculations. The addition of $ZnEt_2$ occurs by ZnEt replacing a hydrogen, releasing ethane. There are four chemically distinct hydrogens that may be replaced, denoted HB, $H_2O$, OH, and $\mu$OH. The HB position is the hydrogen-bonded proton on the $Zr$-aquo ligands, the $H_2O$ position is the non-hydrogen-bonded proton on the aquo ligands, the OH position is the proton on the terminal $Zr$-hydroxo groups, and the $\mu$OH position is the proton bound to the $\mu_3$-bridging hydroxo groups (Figure 1).$^{8}$

![](./images/814555289998065664_3.jpg)

Figure 1. NU-1000 node showing the $H_2O$, HB, OH, and $\mu$OH protons. Carboxylate linkers have been omitted for clarity.

Each possible binding location was investigated for reaction with $ZnEt_2$ by calculating the energy to adsorb the $ZnEt_2$ precursor and transfer a hydrogen atom from the node to an ethyl group to form a molecule of ethane.$^{17}$ Table 1 shows the relative free energies of reaction at each location. These calculations indicate that initial coordination to the $H_2O$ binding site leads to the most stable product; however, reaction at the HB binding site is only slightly less favorable, and the structures arising from Zn coordination at these two sites are, in fact, rotamers that ultimately lead to the same structure (Figure S9, SI).

<table>
<thead>
<tr>
<th>binding site</th>
<th>$\Delta E$ (kcal/mol)</th>
<th>$\Delta G_{383}$ (kcal/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mu$-OH</td>
<td>4.95</td>
<td>4.64</td>
</tr>
<tr>
<td>OH</td>
<td>16.9</td>
<td>16.2</td>
</tr>
<tr>
<td>HB</td>
<td>0.27</td>
<td>1.16</td>
</tr>
<tr>
<td>$H_2O$</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

Table 1. Relative Energetics of ZnEt Substitution at Each Binding Site (kcal/mol)

Before investigating the full reaction going from the bare node to the node with four zincs deposited, the coordination of Zn was investigated. Optimizations of several possible structures of the NU-1000 node with a single coordinated Zn atom were done in order to determine the preferred coordination number and geometry of the Zn species in Zn-AIM. Structures with four-, five-, and six-coordinated Zn species

![](./images/814555289998065664_4.jpg)

Figure 2. Possible reaction pathways for the deposition of four Zn atoms from ZnEt₂ on NU-1000. For simplicity, the aromatic carboxylate linkers are not shown. N is the bare node; and HB, H₂O, OH, and $\mu$OH denote which proton has been replaced by a Zn ion. For structures with two Zn atoms that are not on the same side, A denotes that they are on adjacent sides, and O denotes that they are on opposite sides. In the bottom half of the table, the notation #Hy denotes the number of waters per Zr₆ cluster. Numbers in parentheses are $\Delta G_{383}^\circ$ relative to N plus four ZnEt₂ molecules and four water molecules, where, in every case, the energy of a structure relative to this includes the ZnEt₂ and water molecules not yet added to the node. Energies are given in kcal/mol.

were considered with tetrahedral, trigonal pyramidal, and octahedral geometries, respectively (see Figure S10 for details). On the basis of the calculated energetics and atom−atom distances between the Zn atom and the surrounding oxygen atoms (originating from the Zr₆ MOF node or coordinated water molecules), we conclude that Zn-AIM features four-coordinate Zn atoms with distorted tetrahedral geometry.

Upon determining the preferred tetrahedral geometry of the Zn ions, we next looked at possible AIM reaction pathways, with four Zn atoms, as shown in Figure 2. The bare node,

denoted N, is shown in the first row. This is the reactant node structure, to which all other energies are compared. The first step involves the binding of the first $ZnEt_2$ molecule, where the lowest energy product involves attachment at the $H_2O$ position, denoted as $H_2O$-1Et; this step has a $\Delta G_{383}^\circ$ of $-45.1$ kcal/mol.

Two different reactions can occur subsequent to the initial Zn binding: (1) elimination of a second ethyl group from the previously bound ZnEt group or (2) binding of an additional ZnEt moiety. The third row of Figure 2 presents seven possible secondary reactions corresponding to these possibilities. From left to right are shown three additions of another ZnEt moiety occurring on the same face as a previously bound ZnEt group (to OH, $\mu$OH, or HB protons, respectively), two additions of another ZnEt moiety to opposing faces (opposite or adjacent sides), and two ways of eliminating the second ethyl group from the bound ZnEt group (by reaction with an OH or $\mu$OH proton). In the case of a second equivalent of $ZnEt_2$ adding to the same face as the first ZnEt group, binding to $\mu$OH ($H_2O$/$\mu$OH-2Et) is favored relative to binding at the OH ($H_2O$/OH-2Et) or HB ($H_2O$/HB-2Et) protons. For binding of a second ZnEt to a different face, binding to the opposite face ($2H_2O$-2Et-O) with a $\Delta G_{383}^\circ$ of $-89.9$ kcal/mol is very slightly favorable to binding to an adjacent face ($2H_2O$-2Et-A). Elimination of a second ethyl group as ethane led to coordination of the Zn ion to either the $\mu$OH ($H_2O$,$\mu$OH) or the OH position ($H_2O$,OH), with the latter structure preferred by $-3.7$ kcal/mol. Similar pathways for the addition of a second equivalent of $ZnEt_2$ to HB-1Et and $\mu$OH-1Et were also considered and can be found in Schemes S1 and S2 of the SI.

After coordination of a second ZnEt moiety to the same face as the first ZnEt group, removal of the two remaining ethyl groups, which requires cleavage of $Zn-C$ bonds, is an endoergic reaction by $33.9$ kcal/mol. From here, one could repeat the reaction thus far for the opposite side (structure denoted as $2[H_2O/\mu OH]$) and then hydrate the Zn atoms. The final structure is a hydrated version, $2[H_2O/\mu OH]$-4Hy, of $2[H_2O/\mu OH]$ where each Zn atom is coordinated to one water molecule with a $\Delta G_{383}^\circ$ of $-218.4$ kcal/mol. This completes the AIM process for the reactions that result from the $H_2O/\mu$OH-2Et structure.

The species formed by the addition of ZnEt groups to opposite faces ($2H_2O$-2Et-O) can undergo a series of reactions similar to those considered above. In this case, both ethyl groups leave as ethane and one is left with two Zn atoms deposited on opposite sides (structure denoted as 2-$[H_2O,OH]$). We assume that the same process would be repeated for the other two faces of the node, leading to a $\Delta G_{383}^\circ$ of $-152.6$ kcal/mol ($4[H_2O,OH]$). From this point, the structure is then hydrated where each Zn atom is coordinated to one water molecule, giving the structure $4[H_2O,OH]$-4Hy with a $\Delta G_{383}^\circ$ of $-192.8$ kcal/mol. This completes the AIM process for the reaction that results from the $2H_2O$-2Et-O.

Finally, starting from a structure in which the first ZnEt group undergoes ethane elimination before the addition of subsequent ZnEt groups and repeating the reaction that led to $H_2O$,OH for the opposite side of the node leads to the same structure denoted as $2[H_2O,OH]$ with a $\Delta G_{383}^\circ$ of $-68.8$ kcal/mol as described above. The structure can then be hydrated to give the same structure as the $2H_2O$-2Et-O pathway for the AIM process.

Ultimately, we want to compare the energetics of the two possible structures where there are four Zn atoms deposited on the node. If we consider the unhydrated structures, the single Zn atom per face is favored by $12.6$ kcal/mol (by comparing $4[H_2O,OH]$ to $2[H_2O/\mu OH]$), while, for the hydrated species, the two Zn atoms per face structure is favored by $25.6$ kcal/mol over the one Zn atom per face structure (by comparing $4[H_2O,OH]$-4Hy to $2[H_2O/\mu OH]$-4Hy). However, since, during the AIM process, $ZnEt_2$ is added before $H_2O$ is introduced into the system (and, therefore, presumably before the structures are hydrated), our calculations suggest that the preferred four-Zn structure has one Zn ion on each side of the four faces of the NU-1000 node. The optimized structure of $4[H_2O,OH]$-4Hy that corresponds to the experimental product (called Zn-AIM) of the reaction of $ZnEt_2$ with NU-1000 can be seen in a more complete representation in Figure 3 where there are four Zn atoms per $Zr_6$ cluster, with one Zn atom per side of the node.¹⁸

![](./images/814555289998065664_5.jpg)

Figure 3. NU-1000 node showing the locations of the four Zn atoms attached to the node unhydrated (left) and hydrated (right). The red atoms represent O, light blue atoms represent Zr, purple atoms represent Zn, gray atoms represent C, and white atoms represent H.

Copper Exchange with Zn-AIM (AIM-ME-Cu). $Cu^{2+}$ exchange of $Zn^{2+}$ ions in MOF nodes is well precedented and often occurs to a greater extent compared to other $M^{2+}$ ions.¹¹,¹² We, therefore, chose to start with $Cu^{2+}$.

Samples of Zn-AIM were soaked in $0.01$ M methanolic solutions of $CuCl_2{\cdot}2H_2O$, $CuBr_2$, or $Cu(NO_3)_2{\cdot}2.5H_2O$ for 3, 6, and 20 h at room temperature, resulting in an observable color change of the yellow microcrystalline powder to pale green.¹⁹ The AIM-ME-Cu samples were washed repeatedly with fresh methanol and acetone and then subjected to analysis by inductively coupled plasma−optical emission spectroscopy (ICP−OES) to determine the metal content. As shown in Table 2, all of the Cu salts led to exchange of Zn for Cu with minimal leaching. Notably, under our conditions, the rates of metal exchange appear fairly similar for the three copper salts (Figure S3, SI). To better evaluate the effect of different anions on metal exchange, a weighted effective metal-exchange value was determined for each copper salt. This quantity is defined as the product of the mole fraction of nonstructural metal (both Zn and Cu) retained after metal exchange and the mole fraction of Cu among the nonstructural metal ions following metal exchange, with an ideal value of 1 representing complete exchange of zinc for copper with no leaching (Table 2). (This accounting informs us about the combined effects of metal loss (“leaching”) and incomplete displacement of zinc ions by copper ions.) On the basis of these data, we determined that $CuCl_2{\cdot}2H_2O$ was the most effective salt for Cu metal exchange in Zn-AIM in terms of maximal Cu incorporation.²⁰ Importantly, soaking bare NU-1000 in a methanolic $CuCl_2{\cdot}2H_2O$ solution at $60\ ^\circ C$ led to almost no copper incorporation

<table>
<thead>
<tr>
<th colspan="2">Table 2. ICP−OES Data for Zn-AIM Exchanged with Cu Salts</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th rowspan="2">Cu Salt</th>
<th rowspan="2">Zn/Zr₆</th>
<th rowspan="2">Cu/Zr₆</th>
<th>% nonstructural metal retained</th>
<th>% Cu exchange</th>
<th>weighted effective metal</th>
</tr>
<tr>
<th>((Zn + Cu)/4) × 100%</th>
<th>(Cu/(Cu + Zn)) × 100%</th>
<th>exchange</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuCl₂·2H₂O</td>
<td>0.00</td>
<td>3.7</td>
<td>93</td>
<td>100</td>
<td>0.93</td>
</tr>
<tr>
<td>CuBr₂</td>
<td>0.02</td>
<td>3.6</td>
<td>90</td>
<td>100</td>
<td>0.89</td>
</tr>
<tr>
<td>Cu(NO₃)₂·2.5H₂O</td>
<td>0.11</td>
<td>3.6</td>
<td>93</td>
<td>97</td>
<td>0.90</td>
</tr>
</tbody>
</table>

$(0.15\ Cu/Zr_6)$, suggesting that Zn is indeed necessary for the installation of Cu.

We next synthesized a larger sample of AIM-ME-Cu from Zn-AIM using $CuCl_2{\cdot}2H_2O$. After solvent exchange, the sample was subjected to activation under dynamic vacuum at $60\ ^{\circ}C$. Nitrogen sorption isotherm measurements on the evacuated material reveal that the metal-exchanged material retains porosity with a BET surface area of $1420\ m^2\ g^{-1}$ (Figure 4).

![](./images/814555289998065664_6.jpg)

Figure 4. $N_2$ sorption isotherms for parent Zn-AIM material (black), and metal-exchanged materials: AIM-ME-Cu (green), AIM-ME-Co (blue), and AIM-ME-Ni (red).

Powder X-ray diffraction (PXRD) measurements indicate that, following metal exchange, the material remains crystalline (Figure 5). Thermogravimetric analysis (TGA) of the solvent-evacuated material in nitrogen shows similar behavior to the parent MOF NU-1000 with stability up to $500\ ^{\circ}C$ (Figure S4, SI). Scanning electron microscopy−energy dispersive X-ray spectroscopy (SEM−EDX) indicates the presence of Cu throughout the crystallite (Figure S5, SI). Finally, diffuse reflectance infrared Fourier transform spectroscopy (DRIFTS) shows a similar spectrum to the Zn-AIM material with a peak in the $-OH/-OH_2$ region at $3680\ cm^{-1}$ (Figure S8, SI).

![](./images/814555289998065664_7.jpg)

Figure 5. PXRD patterns for Zn-AIM (black), AIM-Me-Ni (red), AIM-ME-Cu (green), and AIM-Me-Co (blue).

Although we cannot be certain of the exact coordination environment of the installed Cu atoms, based on the calculated coordination geometry and symmetry of the starting Zn-AIM material (vide supra) and the similar spectroscopic data obtained for AIM-ME-Cu, we propose that the Cu daughter materials retain the four-coordinate tetrahedral structure determined for the parent Zn-AIM material (albeit perhaps subjected to slight Jahn−Teller distortions typical of $Cu^{2+}$ complexes).²¹ Regardless of the exact coordination number and geometry of the copper ions in AIM-ME-Cu, we suspect that the templated metal-exchange approach leaves the copper ions sited on the node in a fashion similar to that of $Zn^{2+}$ in Zn-AIM.

Nickel Exchange with Zn-AIM (AIM-ME-Ni). We next sought to similarly install Ni. However, following the same procedure for $NiCl_2{\cdot}6H_2O$ as for $CuCl_2{\cdot}2H_2O$—soaking Zn-AIM in a 0.01 M methanolic solution of $NiCl_2$ for 3, 6, and 20 h at room temperature—resulted in a material with Ni constituting only about 60 mol % of the nonstructural metal ions (i.e., ~40% of the nonstructural metal ions are Zn). Accounting for leaching during exchange, the weighted effective metal-exchange value is only 0.45 (20 h) (Table S2 (SI) and Table 3). Employing $Ni(NO_3)_2{\cdot}6H_2O$ instead of $NiCl_2{\cdot}6H_2O$ led to even lower net conversions (Table 3). We, therefore, attempted metal exchange at elevated temperature, and indeed, soaking Zn-AIM in a 0.01 M methanolic solution of $NiCl_2{\cdot}6H_2O$ at $60\ ^{\circ}C$ yielded better conversion of Zn to Ni (ca. 70%; weighted effective metal-exchange value of 0.62), compared to the room temperature reaction, with less leaching of nonstructural metal ions (Table 3). Zn again appears necessary for the installation of Ni, as soaking bare NU-1000 in a methanolic $NiCl_2{\cdot}6H_2O$ solution at $60\ ^{\circ}C$ led to only minimal nickel incorporation $(0.35\ Ni/Zr_6)$.

The Ni material AIM-ME-Ni was synthesized on a larger scale and activated under dynamic vacuum at $60\ ^{\circ}C$. Like AIM-ME-Cu, the Ni sample retains porosity after metal exchange as indicated by $N_2$ sorption isotherm measurements. The BET surface area of activated AIM-ME-Ni was determined to be $1750\ m^2\ g^{-1}$ (Figure 4). The PXRD pattern of AIM-ME-Ni is in good agreement with that of the parent material (Figure 5), while TGA measurements indicate a slightly lower decomposition temperature (ca. $450\ ^{\circ}C$; Figure S4, SI). SEM−EDX shows a uniform distribution of Ni in the MOF crystallite (Figure S6, SI). Unlike the AIM-ME-Cu material, however, which has a nearly identical DRIFTS spectrum to Zn-AIM (i.e., the parent material), AIM-ME-Ni yields two new peaks (3660 and $3630\ cm^{-1}$) while lacking a peak at $3680\ cm^{-1}$ (Figure S8, SI). The shift in the peaks in the $-OH/-OH_2$ region of the IR could be indicative of a change in node-siting of the incoming Ni ions compared to the Zn ions they replace,²² or is perhaps instead evidence of a lower symmetry arrangement of installed ions, since the node contains approximately one residual Zn

<table>
<thead>
<tr>
<th colspan="7">Table 3. ICP−OES Data for Zn-AIM Exchanged with Ni or Co Salts</th>
</tr>
<tr>
<th>Ni Salt</th>
<th>temp. of metal exchange</th>
<th>Zn/ Zr₆</th>
<th>M/ Zr₆</th>
<th>% nonstructural metal retained ((Zn + M)/4) × 100%</th>
<th>% M exchange (M/(M + Zn)) × 100%</th>
<th>weighted effective metal exchange</th>
</tr>
</thead>
<tbody>
<tr>
<td>NiCl₂·6H₂O</td>
<td>rt</td>
<td>1.2</td>
<td>1.8</td>
<td>76</td>
<td>59</td>
<td>0.45</td>
</tr>
<tr>
<td>Ni(NO₃)₂·6H₂O</td>
<td>rt</td>
<td>2.1</td>
<td>1.0</td>
<td>78</td>
<td>33</td>
<td>0.26</td>
</tr>
<tr>
<td>NiCl₂·6H₂O</td>
<td>60 °C</td>
<td>0.96</td>
<td>2.5</td>
<td>86</td>
<td>72</td>
<td>0.62</td>
</tr>
<tr>
<td>CoCl₂·6H₂O</td>
<td>60 °C</td>
<td>0.43</td>
<td>3.3</td>
<td>93</td>
<td>88</td>
<td>0.82</td>
</tr>
</tbody>
</table>

atom per $Zr_6$ cluster and $\sim$2.5 Ni atoms per $Zr_6$ cluster (compared to AIM-ME-Cu, which contains nearly four Cu atoms per $Zr_6$ cluster and no residual Zn metal atoms).

Cobalt Exchange with Zn-AIM (AIM-ME-Co). Cobalt metal exchange on Zn-AIM was pursued using the same protocol as for Ni, i.e., soaking Zn-AIM in a 0.01 M methanolic solution of $CoCl_2$·6H₂O at 60 °C. This procedure resulted in nearly 90% replacement of Zn by Co, and a weighted effective metal-exchange value of 0.82. Subjecting bare NU-1000 to the same reaction conditions resulted in very little incorporation of Co (0.17 $Co/Zr_6$); the combined results imply that incorporation of metal ions using the method described here occurs via transmetalation of $Zn^{2+}$ rather than wet impregna- tion from the metal salt solution.

AIM-ME-Co was synthesized on a larger scale and then activated under dynamic vacuum at room temperature. Activated AIM-ME-Co yielded a measured BET surface area of 1580 $m^2$ $g^{-1}$ (Figure 4). The PXRD pattern of AIM-ME-Co indicates retention of crystallinity (Figure 5). TGA measurements reveal thermal stability for AIM-ME-Co similar to that for AIM-ME-Ni, i.e., up to 450 °C (Figure S4, SI). An SEM−EDX linescan of a single AIM-ME-Co crystallite revealed that Co is distributed throughout the particle (Figure S7, SI). Lastly, DRIFTS on AIM-ME-Co gave a spectrum in between those of AIM-ME-Cu and AIM-ME-Ni: AIM-ME-Co displays a small peak at 3680 $cm^{-1}$, like the parent Zn-AIM material and AIM-ME-Cu, but also features new peaks at 3660 and 3630 $cm^{-1}$ similar to AIM-ME-Ni (Figure S8, SI). These results seem to indicate that AIM-ME-Co is more structurally similar to Zn-AIM or AIM-ME-Cu than AIM-ME-Ni and are in line with the greater percentage metal exchange observed for Co compared to Ni.

## CONCLUSIONS
Zn-AIM-NU-1000 has been computationally examined via density functional calculations and experimentally examined via a battery of structure- and composition-sensitive measurements; these indicate that it is an excellent starting material for synthetically accessing atomically dispersed metal ions, including $Cu^{2+}$, $Ni^{2+}$, and $Co^{2+}$, in a MOF using the combined AIM and metal-exchange (AIM-ME) approach described here. We anticipate that this methodology will provide access to new, catalytically interesting, functional materials and will facilitate studies in the growing field of supported single-atom catalysis. Of particular interest will likely be (a) metals that cannot be easily and directly incorporated in MOFs via ALD-like chemistry, and (b) bimetallic combinations of installed ions—a notion that is hinted at by some of the results contained in Table 3, but that remains to be explored in a systematic fashion. Future work will focus on expanding the approach to other metal ions and on exploring the catalytic activity of the resulting functionalized materials, including the initial AIM-ME formulations presented here.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.chemma-ter.5b04887.

ALD procedure, DRIFTS, ICP−OES, TGA traces, SEM−EDX, further details of the density functional characterization of Zn-AIM, and coordinates of the computed structures (PDF)

## AUTHOR INFORMATION
### Corresponding Authors
*E-mail: truhlar@umn.edu (D.G.T.).
*E-mail: j-hupp@northwestern.edu (J.T.H.).
*E-mail: o-farha@northwestern.edu (O.K.F.).

### Author Contributions
∥These authors contributed equally. All authors have given approval to the final version of the manuscript.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This work was supported as part of the Inorganometallic Catalyst Design Center, an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, under Award DE-SC0012702. Metal analysis was performed at the Northwestern University Quantitative Bioelement Imaging Center. This work made use of the EPIC facility (NUANCE Center-Northwestern University), which has received support from the MRSEC program (NSF DMR-1121262) at the Materials Research Center; the International Institute for Nanotechnology (IIN); and the State of Illinois, through the IIN. This work made use of the J.B. Cohen X-ray Diffraction Facility supported by the MRSEC program of the National Science Foundation (DMR-1121262) at the Materials Research Center of Northwestern University. DRIFTS measurements were performed in the Keck-II facility of NUANCE Center at Northwestern University. The NUANCE Center is supported by the International Institute for Nanotechnology, MRSEC (NSF DMR-1121262), the Keck Foundation, the State of Illinois, and Northwestern University. The authors acknowledge the Minnesota Supercomputing Institute (MSI) at the University of Minnesota for providing resources that contributed to the research results reported in this paper.

## REFERENCES
(1) Liang, S.; Hao, C.; Shi, Y. The Power of Single-Atom Catalysis. ChemCatChem 2015, 7, 2559−2567.
(2) Thomas, J. M. The concept, reality and utility of single-site heterogeneous catalysts (SSH Cs). Phys. Chem. Chem. Phys. 2014, 16, 7647−7661.

(3) Flytzani-Stephanopoulos, M.; Gates, B. C. Atomically Dispersed Supported Metal Catalysts. Annu. Rev. Chem. Biomol. Eng. 2012, 3, 545−574.

(4) Thomas, J. M.; Saghi, Z.; Gai, P. L. Can a Single Atom Serve as the Active Site in Some Heterogeneous Catalysts? Top. Catal. 2011, 54, 588−594.

(5) Peters, A. W.; Li, Z.; Farha, O. K.; Hupp, J. T. Atomically Precise Growth of Catalytically Active Cobalt Sulfide on Flat Surfaces and within a Metal−Organic Framework via Atomic Layer Deposition. ACS Nano 2015, 9, 8484−8490.

(6) Kim, I. S.; Borycz, J.; Platero-Prats, A. E.; Tussupbayev, S.; Wang, T. C.; Farha, O. K.; Hupp, J. T.; Gagliardi, L.; Chapman, K. W.; Cramer, C. J.; Martinson, A. B. F. Targeted Single-Site MOF Node Modification: Trivalent Metal Loading via Atomic Layer Deposition. Chem. Mater. 2015, 27, 4772−4778.

(7) Mondloch, J. E.; Bury, W.; Fairen-Jimenez, D.; Kwon, S.; DeMarco, E. J.; Weston, M. H.; Sarjeant, A. A.; Nguyen, S. T.; Stair, P. C.; Snurr, R. Q.; Farha, O. K.; Hupp, J. T. Vapor-Phase Metalation by Atomic Layer Deposition in a Metal−Organic Framework. J. Am. Chem. Soc. 2013, 135, 10294−10297.

(8) Planas, N.; Mondloch, J. E.; Tussupbayev, S.; Borycz, J.; Gagliardi, L.; Hupp, J. T.; Farha, O. K.; Cramer, C. J. Defining the Proton Topology of the $Zr_6$-Based Metal−Organic Framework NU-1000. J. Phys. Chem. Lett. 2014, 5, 3716−3723.

(9) Yang, D.; Odoh, S. O.; Wang, T. C.; Farha, O. K.; Hupp, J. T.; Cramer, C. J.; Gagliardi, L.; Gates, B. C. Metal−Organic Framework Nodes as Nearly Ideal Supports for Molecular Catalysts: NU-1000- and UiO-66-Supported Iridium Complexes. J. Am. Chem. Soc. 2015, 137, 7391−7396.

(10) Yang, D.; Odoh, S. O.; Borycz, J.; Wang, T. C.; Farha, O. K.; Hupp, J. T.; Cramer, C. J.; Gagliardi, L.; Gates, B. C. Tuning $Zr_6$ Metal−Organic Framework (MOF) Nodes as Catalyst Supports: Site Densities and Electron-Donor Properties Influence Molecular Iridium Complexes as Ethylene Conversion Catalysts. ACS Catal. 2016, 6, 235−247.

(11) Brozek, C. K.; Dincă, M. Cation exchange at the secondary building units of metal-organic frameworks. Chem. Soc. Rev. 2014, 43, 5456−5467.

(12) Lalonde, M.; Bury, W.; Karagiaridi, O.; Brown, Z.; Hupp, J. T.; Farha, O. K. Transmetalation: routes to metal exchange within metal- organic frameworks. J. Mater. Chem. A 2013, 1, 5453−5468.

(13) Irving, H.; Williams, R. J. P. 637. The stability of transition-metal complexes. J. Chem. Soc. 1953, 3192−3210.

(14) Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Mennucci, B.; Petersson, G. A.; Nakatsuji, H.; Caricato, M.; Li, X.; Hratchian, H. P.; Izmaylov, A. F.; Bloino, J.; Zheng, G.; Sonnenberg, J. L.; Hada, M.; Ehara, M.; Toyota, K.; Fukuda, R.; Hasegawa, J.; Ishida, M.; Nakajima, T.; Honda, Y.; Kitao, O.; Nakai, H.; Vreven, T.; Montgomery, J. A., Jr.; Peralta, J. E.; Ogliaro, F.; Bearpark, M.; Heyd, J. J.; Brothers, E.; Kudin, K. N.; Staroverov, V. N.; Kobayashi, R.; Normand, J.; Raghavachari, K.; Rendell, A.; Burant, J. C.; Iyengar, S. S.; Tomasi, J.; Cossi, M.; Rega, N.; Millam, J. M.; Klene, M.; Knox, J. E.; Cross, J. B.; Bakken, V.; Adamo, C.; Jaramillo, J.; Gomperts, R.; Stratmann, R. E.; Yazyev, O.; Austin, A. J.; Cammi, R.; Pomelli, C.; Ochterski, J. W.; Martin, R. L.; Morokuma, K.; Zakrzewski, V. G.; Voth, G. A.; Salvador, P.; Dannenberg, J. J.; Dapprich, S.; Daniels, A. D.; Farkas, Ö.; Foresman, J. B.; Ortiz, J. V.; Cioslowski, J.; Fox, D. J. Gaussian 09, Revision D.01; Gaussian, Inc.: Wallingford, CT, 2009.

(15) Zhao, Y.; Truhlar, D. G. A new local density functional for main- group thermochemistry, transition metal bonding, thermochemical kinetics, and noncovalent interactions. J. Chem. Phys. 2006, 125, 194101.

(16) Nicklass, A.; Dolg, M.; Stoll, H.; Preuss, H. Ab initio energy- adjusted pseudopotentials for the noble gases Ne through Xe: Calculation of atomic dipole and quadrupole polarizabilities. J. Chem. Phys. 1995, 102, 8942−8952.

(17) Density functional calculations with the simpler model compound $ZnMe_2$ led to different results than with $ZnEt_2$ (possibly due to steric effects), so calculations were performed with the full compound.

(18) Also conceivable are structures in which the exothermicity of the AIM "B step" (hydrolysis step) is sufficiently large and negative that added metal atoms may move between node faces and form more compact cluster structures. This possibility is under active investigation by synchrotron X-ray techniques with metals that are better X-ray scatterers than zinc. The results of these studies will be reported in due course. The details of the final arrangement of zinc ions in Zn-AIM NU-1000 samples, while likely important for certain potential catalysis applications, are not of central importance to the interpretation of experimental metal-exchange studies.

(19) Higher concentrations (0.05 M) of $Cu^{2+}$ salts led to leaching. See the SI for details.

(20) Similar results could be obtained for $Cu(NO_3)_2\cdot2.5H_2O$ upon longer exposure times (44 h). See the SI for details.

(21) Cotton, F. A.; Wilkinson, G.; Murillo, C. A.; Bochmann, M. Advanced Inorganic Chemistry, 6th ed.; Wiley: New York, 1999.

(22) Dincă et al. have observed $Ni^{2+}$ in a tetrahedral geometry when constrained in a MOF. In our case, $Ni^{2+}$ is installed on the node rather than in the node, so it is unclear whether the $Ni^{2+}$ ion would be subjected to similar geometric constraints. See: Brozek, C. K.; Dinca, M. Lattice-imposed geometry in metal−organic frameworks: lacunary $Zn_4O$ clusters in MOF-5 serve as tripodal chelating ligands for $Ni^{2+}$. Chem. Sci. 2012, 3, 2110−2113.