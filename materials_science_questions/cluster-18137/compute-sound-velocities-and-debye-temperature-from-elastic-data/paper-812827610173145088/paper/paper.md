# Physical properties of spinel-type superconductors $CuRh_2S_4$ and $CuRh_2Se_4$:
## A DFT study

Md. Ibrahim Kholil, Md. Tofajjol Hossen Bhuiyan*

Department of Physics, Pabna University of Science and Technology, Pabna 6600, Bangladesh

---

## ARTICLE INFO

**Keywords:**
Elastic properties
Bonding analysis and Vickers hardness
Optical properties
Vibrational properties and electron-phonon
coupling constant

## ABSTRACT

The structural, elastic, electronic, Vickers-Hardness, vibrational, Optical and thermodynamical properties of potentially technologically significant superconductors $CuRh_2S_4$ and $CuRh_2Se_4$ have calculated using density functional theory (DFT) with CASTEP code. The calculated lattice parameters and other properties have compared with available experimental values and found good agreement with them. The mechanical stability found for $CuRh_2S_4$ and $CuRh_2Se_4$ under Born stability conditions. Pugh's ratio indicates the both are ductile and Poisson's ratio reveals the brittle nature. The valence band and conduction bands overlapped each other at the Fermi level indicates the metallic nature of $CuRh_2S_4$ and $CuRh_2Se_4$. The density of states shows that S-3p and Se-4p states are more effective at the Fermi level. The charge density difference maps indicates the Cu-Rh bonds are stronger than Cu-S. The chemical bonding shows a combination of ionic, covalent and metallic nature for $CuRh_2S_4$ and $CuRh_2Se_4$. The Vickers-Hardness indicates the soft material with comparing to Diamond and suitable to use wires and ribbon cables. The electron- and hole-like sheets make the complex multisheet Fermi surface of $CuRh_2S_4$. The different optical functions are also observed clearly. The absorption spectra indicate that $CuRh_2S_4$ is more suitable to use in solar cell rather than $CuRh_2Se_4$. The reflectivity spectrum indicates that these compounds are promising candidate for reflector material. Debye temperature indicates that $CuRh_2S_4$ and $CuRh_2Se_4$ should have advantages to use as a thermal barrier coating (TBC) material. The electron-phonon coupling constant indicates the phonon-mediated medium coupled BCS superconductors. The obtained potential results in present calculation could provide a significant movement for future studies.

---

## Introduction

Chalcogenide spinel compounds show wide variety of attractive physical properties such as the magnetic ordering [1], the metal-insulator transition [2,3], and superconductivity [4]. Further, spinel compounds have potential of the technological applications. Due to this attractive physical properties spinel compunds have gained much interest and great attention of researchers. The general formula of chalcogenide spinels is $AB_2X_4$, where A and B are the transition metals and X is the chalcogen [5]. The sulpo- and selenospinels $CuRh_2S_4$ and $CuRh_2Se_4$ exhibit an extensive variety of electrical and magnetic properties such as ferromagnetic and antiferromagnetic [6]. These spinels have normal cubic structure where the Cu atoms occupy the A (tetrahedral) sites and the Rh atoms occupy the B (octahedral) sites [4]. Further, they exhibit metallic conduction and temperature-independent susceptibility. The superconductivity of the ternary sulfo- and selenospinels $CuRh_2S_4$ and $CuRh_2Se_4$ have been found at transition temperature 4.70 K and 3.48 K, respectively [4]. T. Hagino et al. predicted the lattice constant $a=9.787$ Å and 10.269 Å for $CuRh_2S_4$ and $CuRh_2Se_4$, respectively [4].

Lotgering and Van staple discuss about electrical and magnetic properties of $CuRh_2S_4$ and $CuRh_2Se_4$ and reported that these compounds show superconducting transition between 3 and 4 K [7-9]. M. Ito and his co-workers investigated the magnetic properties of chalcogenide spinel superconductor $CuRh_2S_4$ under pressure and evaluated the pressure dependence of the superconducting parameters [5]. Shelton et al. investigated the pressure dependence transition temperature $(T_c)$ up to $P=2.2$ GPa for the spinels $LiTi_2O_4$, $CuRh_2Se_4$, and $CuRh_2S_4$ [10]. Due to enhancement of the Debye temperature $(\theta)$ they predicted that the superconducting transition temperature $(T_c)$ increase with pressure $(P)$. M. Ito et al. calculated electric resistivity under pressure and predicted the phenomenon of the pressure-induced transition of $CuRh_2S_4$ from a superconductor to an insulator [11]. The highest superconductivity was found in the spinel isostructural compound $LiTi_2O_4$ [12]. T. Oda et al. investigated the band structure, density of states, Fermi surface and charge density of sulphide spinels $CuM_2S_4$ (M = Co, Rh, Ir) [13]. G.L Hart et al. also investigated the band structure of $Cu_{1-x}Ni_xRh_2S_4$ and $CuRh_2Se_4$ [14].

In this paper we have tried to investigate the details physical properties of $CuRh_2S_4$ and $CuRh_2Se_4$ theoretically. Though some

---

* Corresponding author.
E-mail address: thbapon@gmail.com (Md. T.H. Bhuiyan).

https://doi.org/10.1016/j.rinp.2018.11.026
Received 21 September 2018; Received in revised form 7 November 2018; Accepted 9 November 2018
Available online 20 November 2018
2211-3797/ © 2018 Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license
(http://creativecommons.org/licenses/BY-NC-ND/4.0/).

![](./images/812827610173145088_1.jpg)
![](./images/812827610173145088_2.jpg)

Fig. 1. Crystal structure of CuRh₂X₄ (where, X = S, Se) (a) Conventional unit cell, (b) Primitive cell.

theoretical work found in ref. [13] and [14] but still absent about the elastic, vibrational, Vickers-Hardness, optical and thermodynamic properties. Furthermore, considerable progresses have been made after details physical properties calculation of these two spinel superconductors due to rich physical properties. That's why we have investigated the structural, elastic, electronic, bonding, vibrational, optical and thermodynamic properties and electron-phonon coupling constant by using the first principles method base on the density functional theory with CASTEP code.

Finally, the remaining parts of this article are arranged as follows: A brief description of computational method shown in section 2, Investigated results and its related discussion are shown in section 3 and the summary of this work are displaced in section 4.

### Computational methods

The present first principle calculations have been performed using the density functional theory (DFT) based on Cambridge Serial Total Energy Package (CASTEP) computer program [15-18]. The electronic exchange-correlation interaction has been treated by utilizing the generalized gradient approximation (GGA) within the scheme described by Perdew-Burke-Ernzerhof (PBE) [18]. The interactions between ions and electrons are represented with Vanderbilt-type ultrasoft pseudopotentials for Cu, Rh, S and Se atoms [19]. The valence electron configurations of CuRh₂S₄ and CuRh₂Se₄ superconductors have considered Cu-3d¹⁰ 4s¹, Rh-4d⁸ 5s¹, S-3s² 3p⁴ and Se-4s² 4p⁴, respectively for pseudo atomic calculations. The plane-wave cutoff energy has used 350 eV for present calculation. Monkhorst-Pack scheme has used to generate 8 × 8 × 8 k-point grids for the sampling of the Brillouin zone [20]. The Broyden-Fletcher-Goldfarb-Shanno (BFGS) minimizations have used to perform the structural optimizations [21]. In the case of geometry optimization the convergence tolerance have selected as follows: the total energy convergence value is within 2.0 × 10⁻⁵ eV/atom, the maximum Hellmann-Feynaman force is within 0.05 eV/Å; the maximum displacement is within 0.002 Å; the maximum stress is within 0.01 GPa; and the maximum iterations is within 100. The elastic constants of CuRh₂S₄ and CuRh₂Se₄ have investigated by the stress-strain method [22]. The maximum strain amplitude have elected to 0.003. The criteria for convergence tolerance to evaluate the elastic constants have used to 4.0 × 10⁻⁶ eV/atom for the total energy, 0.01 eV/Å for maximum force and 4.0 × 10⁻⁴ Å for maximum displacement. The four numbers of steps have selected for each strain.

### Physical properties

In this section the investigated different physical properties of spinel-type compounds CuRh₂S₄ and CuRh₂Se₄ are presented and analyzed with comparison.

<table>
<caption>Table 1 Calculated lattice parameter $a$ (Å), unit cell volume $V$ (in Å³), $u$ (internal structural parameter) and bulk modulus $B$ (in GPa) for CuRh₂S₄ and CuRh₂Se₄.</caption>
<thead>
<tr>
<th>Compounds</th>
<th></th>
<th>$a$</th>
<th>$V$</th>
<th>$u$</th>
<th>$B$</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuRh₂S₄</td>
<td>Calculated values</td>
<td>9.887</td>
<td>241.69</td>
<td>0.366</td>
<td>95.66</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>Experimental values</td>
<td>9.787</td>
<td>234.36*</td>
<td>0.384</td>
<td>–</td>
<td>Expt. [4]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>9.780</td>
<td>233.86*</td>
<td>–</td>
<td>–</td>
<td>Expt. [6]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>9.790</td>
<td>234.57*</td>
<td>–</td>
<td>–</td>
<td>Expt. [14]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>9.790</td>
<td>234.57*</td>
<td>–</td>
<td>–</td>
<td>Expt. [24]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>9.784</td>
<td>234.15*</td>
<td>0.385</td>
<td>–</td>
<td>Expt. [25]</td>
</tr>
<tr>
<td>CuRh₂Se₄</td>
<td>Calculated values</td>
<td>10.336</td>
<td>276.12</td>
<td>0.366</td>
<td>111.50</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>Experimental values</td>
<td>10.269</td>
<td>270.72*</td>
<td>0.384</td>
<td>–</td>
<td>Expt. [4]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10.340</td>
<td>276.37*</td>
<td>–</td>
<td>–</td>
<td>Expt. [6]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10.270</td>
<td>270.80*</td>
<td>–</td>
<td>–</td>
<td>Expt. [14]</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10.263</td>
<td>270.25*</td>
<td>–</td>
<td>–</td>
<td>Expt. [24]</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">* Calculated.</td>
</tr>
</tfoot>
</table>

### Structural properties

The sulfo- and selenospinels CuRh₂S₄ and CuRh₂Se₄ belongs to the cubic structure with space group Fd$\overline{3}$m (No.227) [4,14]. The cubic structure contains 56 atoms in each unit cell. The Wyckoff positions of both these superconductors are 8a (0.125, 0.125, 0.125) for Cu, 16d (0, 0, 0.5) for Rh and 32e (u, u, u) for S or Se, where $u$ is the internal structural parameter [13]. The conventional and primitive unit cells of these spinels have shown in Fig. 1. The optimized equilibrium crystal structure has obtained by minimizing the total energy. The investigated structural parameters are recorded in Table 1 with available experimental values. The present investigated parameters are well agreed with experimental values. It is found that the evaluated present lattice parameters ($a$) deviate by 1.01% and 0.65% from experimental values for CuRh₂S₄ and CuRh₂Se₄. The investigated values and experimental values appears slight difference due to the temperature dependency of cell parameters and GGA process [23]. The variation of lattice parameter, unit cell volume and bulk modulus for CuRh₂S₄ and CuRh₂Se₄ is appears due to the replacement of atoms by similar atoms which is presented in Fig. 2.

### Elastic properties

Elastic constants describe the details mechanical properties and bonding behaviors of solids. Further, those constants use to justify the mechanical stability of solid and connecting the relation with phonon spectrum and Debye temperature of crystals. The elastic properties of any compound nearly related to the long-wavelength phonon spectrum, thus the elastic properties of superconducting material must be investigated [26]. The investigation of the elastic properties further

![](./images/812827610173145088_3.jpg)

Fig. 2. Variation of lattice parameter, unit cell volume and bulk modulus due to the replacement of atoms by similar atoms.

<table>
<caption>Table 2
Calculated elastic constants $C_{ij}$ (GPa), bulk modulus $B$ (GPa), shear modulus $G$ (GPa), Young's modulus $E$ (GPa), $B/G$ ratio, elastic anisotropic factor $A$, Poisson's ratio $\nu$, Burger's vector $b$ (Å), interlayer distance $d$ (Å), and Peierls stress $\sigma_p$ for CuRh$_2$S$_4$ and CuRh$_2$Se$_4$.</caption>
<thead>
<tr>
<th>Compounds</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{44}$</th>
<th>$B$</th>
<th>$G$</th>
<th>$E$</th>
<th>$B/G$</th>
<th>$A$</th>
<th>$\nu$</th>
<th>$b$</th>
<th>$d$</th>
<th>$\sigma_p$</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuRh$_2$S$_4$</td>
<td>129.25</td>
<td>94.67</td>
<td>30.23</td>
<td>106.20</td>
<td>25.05</td>
<td>69.67</td>
<td>4.23</td>
<td>1.74</td>
<td>0.39</td>
<td>9.887</td>
<td>4.94</td>
<td>0.47</td>
</tr>
<tr>
<td>CuRh$_2$Se$_4$</td>
<td>120.78</td>
<td>81.51</td>
<td>19.47</td>
<td>94.60</td>
<td>19.53</td>
<td>54.81</td>
<td>4.84</td>
<td>0.99</td>
<td>0.40</td>
<td>10.336</td>
<td>5.16</td>
<td>0.35</td>
</tr>
</tbody>
</table>

provides frequent knowledge about the dynamical properties of crystalline solids. The elastic constants of crystal have investigated from a linear fit of the evaluated stress-strain function according to the Hook's law [27]. The three independent elastic constants are $C_{11}$, $C_{12}$ and $C_{44}$ for a cubic type crystal structure. For the first time the investigated elastic constant for CuRh$_2$S$_4$ and CuRh$_2$Se$_4$ are listed in Table 2. The cubic crystal should be mechanically stable when fulfill the well known Born stability criteria [28]. These criteria are,

$$C_{11}>0,\ C_{44}>0,\ C_{11}-C_{12}>0 \text{and} \ C_{11}+2C_{12}>0$$

From Table 2, it is evident that the above criteria are satisfied for the present investigated results, which indicating that the CuRh$_2$S$_4$ and CuRh$_2$Se$_4$ superconductors are mechanically stable. We are not able to compare the present calculated values due to unavailable theoretical elastic constants values.

The mechanical properties such as the bulk modulus $B$, shear modulus $G$, Young's modulus $E$ and Poisson's ratio $\nu$ of CuRh$_2$S$_4$ and CuRh$_2$Se$_4$ have calculated by using the Voigt-Reuss-Hill (VRH) equating method [29]. The Voigt and Reuss bounds of $B$ and $G$ have calculated by using the equations for any cubic crystal, as follows [30]:

$$B_v = B_R = \frac{C_{11}+2C_{12}}{3} \tag{1}$$

$$G_v = \frac{(C_{11}-C_{12}+3C_{44})}{5} \tag{2}$$

$$G_R = \frac{5C_{44}(C_{11}-C_{12})}{[4C_{44}+3(C_{11}-C_{12})]} \tag{3}$$

The Hill took an arithmetic mean values of $B$ and $G$ by using the above two paths as follows,

$$B = \frac{1}{2}(B_R+B_v) \tag{4}$$

$$G = \frac{1}{2}(G_v+G_R) \tag{5}$$

Young's modulus $(E)$ and Poisson's ratio $(\nu)$ have calculated by using the Hill's bulk modulus $(B)$ and shear modulus $(G)$ as follows,

$$E = \frac{9GB}{3B+G} \tag{6}$$

$$\nu = \frac{3B-2G}{2(3B+G)} \tag{7}$$

The Zener anisotropy factor $A$ have calculated by applying the degree of anisotropy in solid [31] and obtained by the following relation,

$$A = \frac{2C_{44}}{(C_{11}-C_{12})} \tag{8}$$

The evaluated values of the bulk modulus $(B)$, shear modulus $(G)$, Young's modulus $(E)$ and Poisson ratio $(\nu)$, $B/G$ ratio and elastic anisotropic factor $A$ are tabulated in Table 2. From Table 2, it can be seen that the bulk modulus for CuRh$_2$Se$_4$ relatively low $(< 100$ GPa) and for CuRh$_2$S$_4$ relatively $(> 100$ GPa) high indicating the soft and hard material by comparing to each other.

The value of bulk modulus is larger than the value of shear modulus $(B > G)$ indicating that the shear modulus is the remarkable parameter associating with the stability of CuRh$_2$S$_4$ and CuRh$_2$Se$_4$ [32]. Further the larger value of bulk modulus than shear modulus denoting the capacity is stronger of resist deformation. Furthermore shear and Young's

![](./images/812827610173145088_4.jpg)

Fig. 3. Variation of the Pugh's ratio of spinels $CuRh_2S_4$ and $CuRh_2Se_4$. The horizontal dotted line considers the Border line between Ductile and Brittle.

modulus indicate the measure of resist reversible deformation by shear stress and stiffness of solid. The calculated values of Pugh's ratio $(B/G)$ for $CuRh_2S_4$ and $CuRh_2Se_4$ are found to be 4.23 and 4.84, respectively. The critical value of Pugh's ratio for any material is 1.75, separates the ductile $(>1.75)$ and brittle $(<1.75)$ nature of crystals [29]. The present calculated Pugh's ratio for $CuRh_2S_4$ and $CuRh_2Se_4$ indicates the ductile nature. The graphical representations of variation of the Pugh's ratio of spinels have shown in Fig. 3. The critical value of ductility-brittle manner of Poisson's ratio is 0.33 and above this value the material behaves brittle nature and lower value indicates the ductile nature [33]. The present investigated value indicates the brittle nature. Further, the value of Poisson's ratio gives vital information about the nature of bonding force in solids [34]. The value of $v$ between 0.25 and 0.5 denote that the material is central force solid [35]. From Table 2, we see that the value of $v$ is 0.39 and 0.40 for $CuRh_2S_4$ and $CuRh_2Se_4$ denotes the force exists in the material is central. The failure mode of material is known as Cauchy pressure $(C_{12}-C_{44})$, when the value is positive and negative then it behaves ductile and brittle nature, respectively [36]. The present value of Cauchy pressure is positive and behaves ductile nature for $CuRh_2S_4$ and $CuRh_2Se_4$. The similar result of Pugh's ratio and Cauchy pressure indicate the credibility of present DFT base work. The degree of elastic anisotropy measure by the Zener anisotropy factor in solid [31]. The unit value $(A=1)$ of anisotropy factor indicating the completely isotropic material and the greater or less value from unity $(A<1$ or $A>1)$ denotes the degree of elastic anisotropy of material. The present values are 1.74 for $CuRh_2S_4$, indicating the degree of elastic anisotropy and 0.99 for $CuRh_2Se_4$, indicating the approximately isotropic material.

The Peierls stress of dislocation is the most vital quantity that indicating the strength of a crystal [37] and denotes the force requisite for a dislocation to be in motion within an atomic plane in the unit cell of a crystal. The Peierls stress $(\sigma_{p})$ can be calculated by the following formula [38].

$$
\sigma_{P}=\frac{G}{1-v} \exp \left(-\frac{2 \pi d}{b(1-v)}\right) \tag{9}
$$

where, $b$ is the Burgers vector and $d$ is the interlayer distance between two glide planes. The calculated values of Burgers vector and interlayer distance with Peierls stress are also recorded in Table 2. Mirza HK Rubel et al [37] have proved the sequence $(\sigma_{p})$ (MAX phases) $<(\sigma_{p})$ (new double perovskite) $<(\sigma_{p})$ (analogue double perovskite) $<<(\sigma_{p})$ (binary carbides) for Peierls stress value and several Max phase have the values within the ranges 0.7-0.98 GPa [39]. They also proved that the dislocations for MAX phase can move easily than perovskite and not possible move for binary carbides. The present calculated values of Peierls stress are 0.47 and 0.35 for spinel compounds $CuRh_2S_4$ and $CuRh_2Se_4$. From the above discussion, it is manifest that the value of Peierls stress of present calculation is less than MAX phase. So, it concludes that the dislocations move very easily for the spinels type compounds.

### Electronic properties

In this present study, we have calculated the band structure along the high symmetry directions in the Brillouin zones as well as total and partial density of states. The band structure and DOS closely related with the charge density difference and Fermi surface. For this reason we have also calculated Fermi surface and charge density difference for $CuRh_2S_4$ and $CuRh_2Se_4$. The Fermi surface and charge density difference farther related with the bonding nature and different bonding properties. The calculated electronic band structure is shown in Fig. 4. The horizontal dotted line between the valence band and conduction band considers the Fermi level. From the Figure of band structure it is manifest that the valence bands and conduction bands overlap each other at the Fermi level. Actually, few bands (colored lines) have crossed the Fermi level for the reason no band gap appears between valence bands and conduction bands, which indicates the metallic conductivity of $CuRh_2S_4$ and $CuRh_2Se_4$.

The calculated total and partial density of states have shown in Fig. 5. The most contributed state at Fermi level is S-3p rather than Rh

![](./images/812827610173145088_5.jpg)

Fig. 4. Electronic band structures of (a) $CuRh_2S_4$ and (b) $CuRh_2Se_4$. The horizontal dotted line considers the Fermi level.

![](./images/812827610173145088_6.jpg)

Fig. 5. Total and partial density of states of (a) $CuRh_2S_4$ and (b) $CuRh_2Se_4$. The vertical dotted line considers the Fermi level.

and Cu states. The higher peak appears from Cu-3d states at 3 eV than Rh and S states. Most of the peaks appears below the Fermi level for these two compounds. The band gaps have found between $-3$eV to Fermi level energy for Cu and Rh states. The Rh-4d and Cu-3d states for $CuRh_2Se_4$ is more contributed than $CuRh_2S_4$. The overall contribution for $CuRh_2Se_4$ is higher than $CuRh_2S_4$. The calculated total density of states are 13.06 states/eV for $CuRh_2Se_4$ and 11.96 states/eV for $CuRh_2S_4$.

In the contour plot of charge density difference, the collection of charges between two atoms can be made covalents bonds and the ionic bonds can be predicted by the balance of negative and posivite charge at the atom positions [40]. The contour plot of valence electron charge density difference is shown in Fig. 6 along with the 100 crystallographic plane. A scale have shown at the right side (color line) of the contour plot in the units of $e/\mathring{A}^3$. The red and blue color of scale indicates the high and low electron densities. In the plot, the spherical charge distribution appears around S and Se atoms that denote the ionic nature of S-S and Se-Se bonds. The S and Se atoms also highly contributed in the density of states map (Fig. 5) for this reason the charge distribution is maximum for S-S and Se-Se bonds. The ionic character describes the metallic nature of S-S and Se-Se bonds [41]. The electronegativity appears at Cu is relatively high in the charge density difference map because the distribution of charge around Cu is highly uniform and near Cu atoms more charge is accumulated. The covalent bonds nature have found between Cu-Rh bonds because the hybridization found between Cu and Rh atoms. We have also investigated the charge density difference map in different crystallographic plane and have found the same results as well as that found in the present investigation. The charge distributed between S-Cu and Se-Cu is very low due to interatomic distance. Fruther, the lower charge distribution appears between S-Rh and Se-Rh bonds in case of interatomic distance. The overall superior discussion of the charge density difference map reflects that $CuRh_2S_4$ and $CuRh_2Se_4$ can be designated as an exceedingly anisotropic combination between ionic, covalent and metallic nature.

The notion of the topology of Fermi surface (FS) can support us to reveals the proper theoretical models concerning the pairing symmetry for any superconducting materials and find the relation between structural and electronic properties [37]. We have plotted the FS topology in Fig. 7 for $CuRh_2S_4$. The FS have calculated with band crossing lines (color lines) in the Fermi level as shown in Fig. 4(a) and have also calculated with the 3D cross section of the Brillouin zone. In the FS topology, we have found eight sheets because of eight band crossing in the Fermi level (as shown in band structure diagram). There are four Fermi-sheets appears at the corner of the topology that indicate hole-like concave sheets at the R-points of the Brillouin zone and another three hole-like sheets found inside the topology at around the $\Gamma$ point. The spheroid sheet at gamma point in the middle of topology indicates the electron-like sheets [37]. So, overall we conclude that the both electron- and hole-like sheets make the complex multisheet FS of $CuRh_2S_4$. In the present calculation, we are not able to calculate the FS for $CuRh_2Se_4$ due to theoretical process. Hope this will be investigated further in any other theoretical calculation.

### Population analysis and Vickers hardness

To obtain the different bonding behavior in any crystal system the more investigation is required about the Mulliken atomic populations [42]. The present investigated Mulliken atomic populations of $CuRh_2S_4$ and $CuRh_2Se_4$ superconductors have tabulated in Table 3. In Table 3, we conclude that the S atoms bearing negative charge whereas Cu and Rh bearing positive charge. For the above reason, the charge transfer from Cu and Rh atom to S atom. The charge transformation towards the S atoms from Cu and Rh atoms is equal to 0.05e for $CuRh_2S_4$. For $CuRh_2Se_4$ superconductor, the charge transformation is opposite of $CuRh_2S_4$. The charge is transfer from Se atoms to Cu and Rh atoms which is equal to 0.36e and 0.73e. In the present Mulliken atomic

![](./images/812827610173145088_7.jpg)

Fig. 6. Charge density difference of CuRh₂S₄ and CuRh₂Se₄ for 100 planes.

![](./images/812827610173145088_8.jpg)

Fig. 7. Fermi surface of CuRh₂S₄.

populations S-Rh and S-Cu bonds for CuRh₂S₄ behaves high value due to positive population and indicating the increasing level of covalency i.e., highly covalent nature [43]. For CuRh₂Se₄ superconductors the Se-Rh and Cu-Se bonds also indicating the covalent nature.

In present investigation, we have also investigated the ionicity of a material ($f_h$) due to understanding the further crucial bonding behavior by using the following equation [44],

$$
f_{h}=1-e^{-\left|P_{c}-P\right| / P} \tag{10}
$$

where, P_C represents the bond overlap population in a pure covalent crystal and when the value is one then represents the pure covalent nature whereas P is the bond overlap population. The value of $f_h$ is one (1) and zero (0) indicates the ionic and covalent bond nature of any material. In the present investigation the S-Cu, Se-Rh and Cu-Se bonds represent the relatively ionic nature which contradicts from Mulliken atomic bond nature and only S-Rh bonds relatively covalent nature. To exceed this contradiction more investigation is required.

Hardness evaluates or estimates the resistance to localized plastic deformation initiated by either mechanical indentation or abrasion. Furthermore, evaluating the hardness of a material the amount of force per unit area accomplished the plastic deformation and higher hardness indicates the higher resistance to deformation of a material [45]. The present calculated Vickers hardness have tabulated in Table 4. The Vickers hardness ($H_v$) of a compound acquired from the Mulliken bond population data by using the following relations [46,47],

$$
H_{v}=\left[\prod^{\mu}\left(H_{v}^{\mu}\right)^{n^{\mu}}\right]^{1 / \sum n^{\mu}} \tag{11}
$$

$$
H_{v}^{\mu}=740\left(P^{\mu}-P^{\mu^{\prime}}\right)\left(v_{b}^{\mu}\right)^{-5 / 3} \tag{12}
$$

$$
v_{b}^{\mu}=\left(d^{\mu}\right)^{3} / \sum_{v}\left[\left(d^{v}\right)^{3} N_{b}^{v}\right] \tag{13}
$$

$$
P^{\mu^{\prime}}=n_{\text {free }} / V \tag{14}
$$

$$
n_{\text {free }}=\frac{\text { difference }}{3}[1 s t+4 \times \text { odd }+2 \times \text { even }+ \text { Last }] \tag{15}
$$

where, $P^{\mu}$ called the Mulliken population of the μ-type bond, $P^{\mu^{\prime}}$ denotes the metallic population of the μ-type bond, $v_{b}^{\mu}$ is the volume of a bond of type μ, $n_{free}$ is the number of free electrons, V is the cell volume, $d^{\mu}$ is the bond length of type μ and $N_{b}^{v}$ called the bond number of type v per unit volume.

Table 3
Population analysis of CuRh₂S₄ and CuRh₂Se₄ superconductors.

<table>
<thead>
<tr>
<th>Compounds</th>
<th>Species</th>
<th>s</th>
<th>p</th>
<th>d</th>
<th>Total</th>
<th>Charge</th>
<th>Bond</th>
<th>Population</th>
<th>$f_h$</th>
<th>Lengths (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuRh₂S₄</td>
<td>S</td>
<td>1.85</td>
<td>4.20</td>
<td>0.00</td>
<td>6.05</td>
<td>−0.05</td>
<td>S-Rh</td>
<td>0.65</td>
<td>0.42</td>
<td>2.27954</td>
</tr>
<tr>
<td></td>
<td>Cu</td>
<td>0.67</td>
<td>0.64</td>
<td>9.60</td>
<td>10.90</td>
<td>0.10</td>
<td>S-Cu</td>
<td>0.36</td>
<td>0.83</td>
<td>2.39458</td>
</tr>
<tr>
<td></td>
<td>Rh</td>
<td>0.47</td>
<td>0.42</td>
<td>8.09</td>
<td>8.98</td>
<td>0.02</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>CuRh₂Se₄</td>
<td>Se</td>
<td>1.53</td>
<td>4.11</td>
<td>0.00</td>
<td>5.64</td>
<td>0.36</td>
<td>Se-Rh</td>
<td>0.38</td>
<td>0.81</td>
<td>2.39060</td>
</tr>
<tr>
<td></td>
<td>Cu</td>
<td>0.80</td>
<td>0.92</td>
<td>9.64</td>
<td>11.36</td>
<td>−0.36</td>
<td>Cu-Se</td>
<td>0.39</td>
<td>0.79</td>
<td>2.49946</td>
</tr>
<tr>
<td></td>
<td>Rh</td>
<td>0.78</td>
<td>0.78</td>
<td>8.16</td>
<td>9.73</td>
<td>−0.73</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4
Calculated Mulliken bond overlap population of $\mu$-type bond$P^{\mu}$, $n^{\mu}$ is the number of bonds, bond length$d^{\mu}$, metallic population$P^{\mu'}$, bond volume $v_{b}^{\mu}$ ($\mathring{\text{A}}^3$) and Vickers hardness of $\mu$-type bond $H_{v}^{\mu}$ (GPa) and total hardness $H_{v}$ (GPa) of CuRh₂S₄ and CuRh₂Se₄ superconductors.</caption>
<thead>
<tr>
<th>Compounds</th>
<th>bond</th>
<th>$n^{\mu}$</th>
<th>$d^{\mu}$</th>
<th>$p^{\mu}$</th>
<th>$p^{\mu'}$</th>
<th>$v_{b}^{\mu}$</th>
<th>$H_{v}^{\mu}$</th>
<th>$H_{v}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuRh₂S₄</td>
<td>S-Rh</td>
<td>8</td>
<td>2.27954</td>
<td>0.65</td>
<td>0.1612</td>
<td>13.9921</td>
<td>4.45</td>
<td>2.51</td>
</tr>
<tr>
<td rowspan="2">CuRh₂Se₄</td>
<td>S-Cu</td>
<td>8</td>
<td>2.39458</td>
<td>0.36</td>
<td>0.1612</td>
<td>16.2203</td>
<td>1.42</td>
<td rowspan="2">1.56</td>
</tr>
<tr>
<td>Se-Rh</td>
<td>8</td>
<td>2.39060</td>
<td>0.38</td>
<td>0.1422</td>
<td>16.1060</td>
<td>1.71</td>
</tr>
<tr>
<td></td>
<td>Cu-Se</td>
<td>8</td>
<td>2.49946</td>
<td>0.39</td>
<td>0.1422</td>
<td>18.4085</td>
<td>1.43</td>
<td></td>
</tr>
</tbody>
</table>

At present to my knowledge, Diamond is the much hardest material rather than all others materials with range of Vickers hardness 70–150 GPa [45]. The present calculated values for CuRh₂S₄ and CuRh₂Se₄ superconductors are 2.51 GPa and 1.56 GPa, respectively. With comparing to Diamond, we finally conclude that the present calculated materials are obviously soft material and deformation resistance is low. These materials also have low dimension and suitable to use in wires and ribbon cables.

### Optical properties

The optical properties of a material describe the interaction nature with light and describe the more about the electronic structure. The optical properties of a matter include the different terms like as dielectric function, refractive index, extinction coefficient, absorption, conductivity, loss function, reflectivity etc. The present calculated optical properties for CuRh₂S₄ and CuRh₂Se₄ are recorded in Fig. 8 and this calculations stand on up to 25 eV energy range. The value of 0.5 eV Gaussian smearing has elected for all optical properties calculations. For analysis of dielectric function, we have used a semi-empirical Drude term with unscreened plasma frequency 3 eV and Drude damping 0.05 eV because of metallic nature of CuRh₂S₄ and CuRh₂Se₄ [48].

The optical properties have calculated by using the frequency dependent dielectric function $\varepsilon\ (\omega)=\varepsilon_{1}\ (\omega)+i\varepsilon_{2}\ (\omega)$, Where the imaginary part [$\varepsilon_{2}\ (\omega)$] obtained from the momentum matrix elements between the filled and the unfilled electronic eigenstates. The real part of dielectric function [$\varepsilon_{1}\ (\omega)$] obtained from the Kramers-Kronig transform of imaginary part and the real part have defined by the Eqs. 49–54 in ref [16]. Further, the imaginary part defined by the following equation [16],
$$
\varepsilon_{2}(\omega)=\frac{2 \mathrm{e}^{2} \pi}{\Omega \varepsilon_{0}} \sum_{k, v, c}|\tilde{\mathrm{N}} \pm_{k}^{c}| u. r\left|\tilde{\mathrm{N}} \pm_{k}^{v}\right|^{2} \delta\left(E_{k}^{c}-E_{k}^{v}-E\right)
\tag{16}
$$
where, $u$ and $\Omega$ are denoted as the polarization of the incident electric field and the unit cell volume, $\omega$ and $e$ are reveals the frequency of light and the charge of electron, $\tilde{\mathrm{N}} \pm_{k}^{c}$ and $\tilde{\mathrm{N}} \pm_{k}^{v}$ are defined as the conduction band wave function and the valence band wave function at $K$ respectively.

The real and imaginary parts of the dielectric function for both the material are displayed in Fig. 8(a) and (b). From Fig. 8(a) and (b), we observed that the real part [$\varepsilon_{1}\ (\omega)$] goes through zero from below and the imaginary part approaches zero from above indicating the metallic nature of CuRh₂S₄ and CuRh₂Se₄. The negative value of $\varepsilon_{1}\ (\omega)$ also reveals the Drude-like metallic nature of these compound. The real part goes to above zero at around 0.5 eV which shows a peak and became zero at around 13 eV. The imaginary part decrease sharper and approaches zero at around 12 eV. The real and imaginary both part becomes zero after 12 eV indicating that no dielectric effect appears after 12 eV in ultraviolet region. This corresponds to the energy at which the absorption and reflectivity displays a sharp drop (Fig. 8(e) and (h)) and the energy loss function (Fig. 8(g)) exhibits a first peak. The dielectric function for CuRh₂S₄ and CuRh₂Se₄ is almost similar in whole energy region. The overall discussion indicates the CuRh₂S₄ and CuRh₂Se₄ compounds behave as transparent in high energy region.

The real part of refractive index known as the phase velocity which have displaced in Fig. 8(c). The similar contribution found for CuRh₂S₄ and CuRh₂Se₄ in the whole graph but at zero energy point refractive index value is high for CuRh₂S₄. The static value of refractive index is 20 for CuRh₂S₄ and 15 for CuRh₂Se₄ in the infrared region. The extinction coefficient (imaginary part) reveals the amount of absorption loss when the electromagnetic wave (as light) passes through the material. The extinction coefficients have also shown in Fig. 8(d). From this graph, it is manifest that the value of extinction coefficient for CuRh₂S₄ is higher than CuRh₂Se₄. For the reason, CuRh₂S₄ is more concentrated than CuRh₂S₄. Further, we conclude that CuRh₂S₄ strike more electromagnetic wave than CuRh₂Se₄.

The absorption coefficient is evaluating the rate of decrease in the intensity of electromagnetic radiation (as light) as it passes via a given substance before it is absorbed. The calculated absorption coefficients are shown in Fig. 8(e). Fig. 8(e) exhibits the absorption coefficients of both the material which start at 0 eV due to their metallic nature. The more effective value for absorption coefficient has found in the ultraviolet region and overall contribution for CuRh₂S₄ is more than CuRh₂Se₄. So, we conclude that CuRh₂S₄ is more suitable to use in solar cell rather than CuRh₂Se₄.

The present calculated conductivity spectra have displaced in Fig. 8(f) and the effect of conductivity found in the beginning energy region for both materials. The more conductivity is found for CuRh₂S₄ than CuRh₂Se₄. For the reason, CuRh₂S₄ is better to use in electrical conductors rather than CuRh₂Se₄.

The loss function represent the loss of energy when fast electron traversing any materials. The point in which energy loss appears maximum then this point is called the Bulk plasma frequency and this happen only for the conditions, $\varepsilon_{2}\ (\omega)$ is less than one ($\varepsilon_{2}<1$) and $\varepsilon_{1}\ (\omega)$ is equal to the zero ($\varepsilon_{1}=0$) [49,50]. The present calculated loss functions have shown in Fig. 8(g). The calculated bulk frequencies are 12.00 eV and 14.00 eV for CuRh₂Se₄ and CuRh₂S₄, respectively. When the incident photon frequency is greater the present materials appears as the transparent materials.

Reflectivity of a material measures the efficiency of a surface to reflect radiation. The present calculated [as shown in Fig. 8(h)] reflectivity represents the good reflectivity in IR and ultraviolet region. The overall reflectivity has found for both the materials as like as same and both materials have suitable to use as reflector material.

### Debye temperature

In a fixed temperature or minimum temperature, the highest frequency mode of vibration is known as Debye temperature. The different physical properties have influence by the Debye temperature such as melting point, specific heat, thermal expansion etc. Debye temperature discuss about the high region of temperature and for the condition $T>\theta_{\text{D}}$ the vibration mode is equal with $K_{\text{B}}T$ energy in every case otherwise vibration mode found at rest. Low temperature region also discuss by the Debye temperature and this mainly comes from acoustic vibration.

The Debye temperature determine only from approximation method because this is not an accurately determined parameter for any material. Various data can be used to approximate the Debye temperature of a material but in present calculation this determine by using the elastic modulus data. The standard method for determination of Debye temperature only depends on the elastic modulus data [51]. The Debye temperature and its related component have calculated by using the following equations [52–55],
$$
\theta_{D}=\frac{h}{k}\left[\frac{3 n}{4 \pi}\left(\frac{N_{A} \rho}{M}\right)\right]^{\frac{1}{3}} v_{m}
\tag{17}
$$

![](./images/812827610173145088_9.jpg)

Fig. 8. Energy dependent optical functions (a) real part of dielectric function, (b) imaginary part of dielectric function, (c) refractive index, (d) extinction coefficient, (e) absorption, (f) real part of conductivity, (g) loss function, and (h) reflectivity of CuRh₂S₄ and CuRh₂Se₄ along [1 0 0] polarization directions.

$$
v_{m}=\left[\frac{1}{3}\left(\frac{2}{v_{t}^{3}}+\frac{1}{v_{l}^{3}}\right)\right]^{-\frac{1}{3}}
\tag{18}
$$

$$
v_{l}=\left(\frac{B+\frac{4}{3} G}{\rho}\right)^{\frac{1}{2}}
\tag{19}
$$

$$
v_{t}=\left(\frac{G}{\rho}\right)^{\frac{1}{2}}
\tag{20}
$$

where, $h$ and $k$ are the Planck constant and Boltzmann constant, $N_{\mathrm{A}}$ is the Avogadro's number, $\rho$ is the density, $M$ is known as the molecular weight and $n$ is the number of atoms in the unit cell of CuRh₂S₄ and CuRh₂Se₄ superconductors.

The present calculated values of $\rho$, $v_{t}$, $v_{l}$, $v_{m}$ and $\theta_{\mathrm{D}}$ have listed in Table 5. The present evaluated Debye temperatures are 294.23 K and 215.57 K, respectively. The present calculated Debye temperature for CuRh₂S₄ contradicts with the experimental value. The contradiction found due to theoretical process and to overcome this contradiction more investigation is required. For CuRh₂Se₄ the value of Debye temperature coincides with experimental value.

The calculated material CuRh₂S₄ and CuRh₂Se₄ have lower Debye temperature with comparison to a candidate thermal barrier coating material Y₄Al₂O₉ [56]. Since lower Debye temperature depends in a lower phonon thermal conductivity, hence CuRh₂S₄ and CuRh₂Se₄ have a lower thermal conductivity. For the reason, CuRh₂S₄ and CuRh₂Se₄ should have advantages to use as a thermal barrier coating (TBC) material.

<table>
<caption>Table 5
The calculated density $\rho$ (in gm/cm³), transverse ($v_{t}$), longitudinal ($v_{l}$), and average sound velocity $v_{m}$ (m/s) and Debye temperature $\theta_{\mathrm{D}}$ (K) of CuRh₂S₄ and CuRh₂Se₄ superconductors.</caption>
<thead>
<tr>
<th>Compound</th>
<th>$\rho$ (gm/cm³)</th>
<th>$v_{t}$ (m/s)</th>
<th>$v_{l}$ (m/s)</th>
<th>$v_{m}$ (m/s)</th>
<th>$\theta_{\mathrm{D}}$ (K)</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuRh₂S₄</td>
<td>4.91</td>
<td>5332.14</td>
<td>2258.72</td>
<td>2553.63</td>
<td>294.23</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>230</td>
<td>Expt. [4]</td>
</tr>
<tr>
<td>CuRh₂Se₄</td>
<td>6.55</td>
<td>4291.65</td>
<td>1726.75</td>
<td>1955.63</td>
<td>215.57</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>211</td>
<td>Expt. [4]</td>
</tr>
</tbody>
</table>

## Thermodynamic properties

The temperature in which the solid change its state to liquid at atmospheric pressure then this phenomenon is known as melting point of solid. The solid and liquid also found in equilibrium at the melting point. Fine et al. proposed a formula for cubic material which has used to calculate the melting temperature, as follows [57],

$$
T_{m}=553+5.91 C_{11}
\tag{21}
$$

where, the unit of $T_{m}$ is in K and $C_{11}$ in GPa. The calculated melting temperature recorded in Table 6. The melting temperature of CuRh₂S₄ is higher with compare to CuRh₂Se₄. For the reason, the material CuRh₂Se₄ has more convenient to melt down than CuRh₂S₄.

Thermal conductivity is the essential property of any material that reveals the conduction of heat. The dependency found for thermal conductivity with temperature. The temperature dependent conductivity of any material has increase gradually when temperature decreases to a certain extent [58]. Many different methods have been

**Table 6**
The calculated melting temperature, $T_m$ (K), minimum thermal conductivity, $K_{min}$ (in $\text{Wm}^{-1}\text{K}^{-1}$) and the Dulong-Petit limit (J/mole.K) of $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ superconductors.

<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>$T_m$</th>
      <th>$K_{min}$</th>
      <th>Dulong-Petit limit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{CuRh}_2\text{S}_4$</td>
      <td>1316.86</td>
      <td>0.49</td>
      <td rowspan="2">174.55</td>
    </tr>
    <tr>
      <td>$\text{CuRh}_2\text{Se}_4$</td>
      <td>1266.81</td>
      <td>0.35</td>
    </tr>
  </tbody>
</table>

used for evaluating minimum thermal conductivity ($K_{\text{min}}$) but for present investigation we have chosen Clarke method [59]. Clarke method is as follows,

$$
K_{min} = K_Bv_m\left(\frac{M}{n\rho\mathrm{N_A}}\right)^{-2/3}
\tag{22}
$$

where, $K_B$ and $v_m$ are the Boltzmann constant and the average sound velocity, $M$ is the molecular mass, $n$ is the number of atoms per molecule and $N_A$ is the Avogadro's number.

The calculated temperature dependent minimum thermal conductivity for $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ are listed in **Table 6**. The calculated minimum thermal conductivity of $\text{CuRh}_2\text{S}_4$ is slightly higher than $\text{CuRh}_2\text{Se}_4$ but with comparison both are relatively same. For the reason, we conclude that those materials bear low thermal conductivity at ambient conditions.

Dulong-Petit limit reveals the anharmonic effect of the specific heat capacity $C_V$ that is suppressed and close to a limit at high temperature [60]. The examined Dulong-Petit limit of a material have found by using the following equation [60],

$$
\text{Dulong} - \text{Petit limit} = 3\text{nN_A}K_B
\tag{23}
$$

where, $N_A$ is the Avogadro's number and $K_B$ is the Boltzmann constant. The calculated value of Dulong-Petit limit has found 174.55 J/mole.K for both the materials.

### Electron-phonon coupling constant

Electron-phonon coupling constant is the most essential superconducting parameter for evaluating superconducting critical temperature. In case of determination of transition temperature electron-phonon coupling constant must be needed to accuracy measurement. For the accuracy measurement of electron-phonon coupling QUANTUM- ESPRESSO program provides good impact [61]. Further, the requirement of double-delta function integration over a dense net of electron and phonon vectors $k$ and $q$ vectors have also needed for accuracy measurement [62].

Moreover, the electron-phonon coupling constant measures accurately by using the experiment value of specific heat coefficient $\gamma$. The experiment value of specific heat coefficient has also available in literature [4] but we are unable to measure the electron-phonon coupling constant accurately due to theoretical process. For the above reason we have not ensured the accuracy of critical temperature ($T_c$) calculation.

In case of above fact the electron-phonon coupling constant have calculated circuitously by using the McMillan formula [63].

$$
\lambda_{ep} = \frac{1.04 + \mu^*\ln\left(\frac{\theta_D}{1.45T_c}\right)}{\left(1 - 0.62\mu^*\right)\ln\left(\frac{\theta_D}{1.45T_c}\right) - 1.04}
\tag{24}
$$

where, $\theta_D$ denotes the Debye temperature and $\mu^*$ define as coulomb pseudo potential.

Since, coulomb pseudo potential is less sensitive for evaluate the electron-phonon coupling, we take on empirically $\mu^* = 0.13$ [63]. The Debye temperatures have used in this section which calculated earlier in present investigation and the experiment transition temperatures are 4.70 K and 3.48 K for $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ [4]. After computing this above values, we have found electron-phonon coupling constant$\lambda_{ep} = 0.632$ ($\text{CuRh}_2\text{S}_4$) and$\lambda_{ep} = 0.634$ ($\text{CuRh}_2\text{Se}_4$). These values of $\lambda_{ep}$are well agreed with experiment values in ref. [4]. This good agreement with experimental values indicates the reliability of present calculation.

### Conclusion

In brief, the structural, elastic, electronic, Vickers hardness, vibrational, optical and thermodynamics properties and electron phonon coupling constant of $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ have been calculated by using the density functional theory. The optimized structural parameters well agreed with available values. The valence and conduction band overlapped with each other at Fermi level denotes the metallic character of $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$. The partial density of state shows that S-3p and Se-4p states are more significant at the Fermi level. The mechanical stability of $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ has found by fulfills the Born stability conditions. The Pugh's ratio and Poisson's ratio indicate the ductile and brittle nature, respectively. The bonding properties indicate the ionic, covalent and metallic nature of $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$. The electron and hole-type sheets appear from the Fermi surface of $\text{CuRh}_2\text{S}_4$. The value of Vickers-Hardness indicates the soft material with compare to Diamond. The reflectivity spectra indicate that $\text{CuRh}_2\text{S}_4$ and $\text{CuRh}_2\text{Se}_4$ have more effect to use a solar reflector. The absorption spectra reveal that $\text{CuRh}_2\text{S}_4$ behaves good absorber rather than $\text{CuRh}_2\text{Se}_4$. Debye temperature indicates that these compounds have also more potential to use as a thermal barrier coating (TBC) material. The study of melting temperature of $\text{CuRh}_2\text{S}_4$ is higher than that of $\text{CuRh}_2\text{Se}_4$ superconductor and indicates that the materials bear low thermal conductivity at ambient conditions. The melting temperature notifies that the material $\text{CuRh}_2\text{Se}_4$ has more convenient effect to melt down than $\text{CuRh}_2\text{S}_4$. The calculated value of Dulong-Petit limit is 174.55 J/mole.K. The electron-phonon coupling constant exhibits that the materials are phonon-mediated medium coupled BCS superconductors. These investigated results could provide great knowledge for other theoretical and experimental spinel-type compounds.

### References

[1] Lotgering FK. Philips Res Rep 1956;11:190.
[2] Nagata S, Hagino T, Seki Y, Bitoh T. Phys B 1994;194:1077.
[3] Radaelli PG, et al. Nature (London) 2002;416:155.
[4] Hagino T, Seki Y, Wada N, Tsuji S, Shirane T, Kumagai KI, et al. Phys Rev B 1995;51:12673.
[5] Ito M, Taira A, Sonoda K. Acta Physica Polonica A 2017;131.
[6] Van Maaren NH, Schaeffer GM, Lotgering FK. Phys Lett A 1967;25:238.
[7] Lotgering FK, Van Stapele RP. J Appl Phys 1968;39:417.
[8] Lotgering FK. J Phys Chem Solids 1969;30:1429.
[9] DiSalvo FJ, Waszczak JV. Phys Rev B 1982;26:2501.
[10] Shelton RN, Johnston DC, Adrian H. Solid State Commun 1976;20:1077.
[11] Ito M, Hori J, Kurisaki H, Okada H, Perez Kuroki AJ, Ogita N, et al. Phys Rev Lett 2003;91:077001.
[12] Johnston DC, Prakash H, Zachariasen WH, Viswanathan R. Mat Res Bull 1973;8:777.
[13] Oda T, Shirai M, Suzuki N, Motizuki K. J Phys: Condens Matter 1995;7:4433.
[14] Hart GL, Pickett WE, Kurmaev EZ, Hartmann D, Neumann M, Moewes A, et al. Phys Rev B 2000;61:4230.
[15] Clark SJ, Segall MD, Pickard CJ, Hasnip PJ, Probert MJ, Refson K, et al. Z Kristallogr 2005;220:567.
[16] Materials Studio CASTEP manual © Accelrys 010. <http://www.tcm.phy.cam.ac.uk/castep/documentation/WebHelp/CASTEP.html>.
[17] Hohenberg P, Kohn W. Phys Rev 1964;136:B864.
[18] Perdew JP, Ruzsinszky A, Csonka GI, Vydrov OA, Scuseria GE, Constantin LA, et al. Phys Rev Lett 2008;100:136406.
[19] Vanderbilt D. Phys Rev B 1990;41:7892.
[20] Monkhorst HJ, Pack JD. Phys Rev B 1976;13:5188.
[21] Fischer TH, Almlof J. J Phys Chem 1992;96:9768.
[22] Feng J, Xiao B, Zhou R, Pan W, Clarke DR. Acta Mater 2012;60:3380.
[23] Zhu YD, et al. Comput Mater Sci 2016;123:70.
[24] Robbins M, Willens RH, Miller RC. Solid State Commun 1967;5:933.
[25] Furubayashi T private communications.
[26] Karaca Ertuğrul, et al. Phil Mag 2017:1.

[27] Nye JF. Propriétés physiques des matériaux. Paris: Dunod; 1961.
[28] Born M, in On the Stability of Crystal Lattices. I (Cambridge University Press, 1940) 160.
[29] Hill R. Proc Phys Soc A 1952;65(65):349.
[30] Wu ZJ, Zhao EJ, Xiang HP, Hao XF, Liu XJ, Meng J. Phys Rev B 2017;76:054115.
[31] Zener C. Elasticity and Anelasticity of Metals. Chicago: University of Chicago Press; 1948.
[32] Liu QJ, Liu ZT, Feng LP, Tian H. Comput Mater Sci 2011;50:2822.
[33] Haines J, Leger J, Bocquillon G. Ann. Rev Mater Res 2001;31:1.
[34] Shirai KJ. Solid State Chem 1997;133:327.
[35] Pfrommer BG, Côté M, Louie SG, Cohen ML. J Comput Phys 1997;131:233.
[36] Pettifor DG. Mater Sci Tech 1992;8:345.
[37] Rubel Mirza HK, Hadi MA, Rahaman MM, Ali MS, Aftabuzzaman M, Parvin R, et al. Comput Mater Sci 2017;138:160.
[38] Lu G. The Peierls-Nabarro model of dislocations: a venerable theory and its current development. In: Yip S, editor. Handbook of Materials Modeling. Amsterdam: Springer; 2005. p. 1–19.
[39] Pugh SF. Phil Mag 1954;45:823.
[40] Ernst F, Rühle M, editors. High-Resolution Imaging and Spectrometry of Materials. Berlin Heidelberg New York: Springer-Verlag; 2003.
[41] Singh RP. J Magnesium Alloys 2014;2:349.
[42] Mulliken RS. J Chem Phys 1955;23:1833.

[43] Segall MD, Shah R, Pickard CJ, Payne MC. Phys Rev B 1996;54:16317.
[44] Tian W, Chen H. Sci Rep 2016;6:19055.
[45] Kholil MI, Ali MS, Aftabuzzaman M. J Alloy Compd 2018;740:754.
[46] Gao FM. Phys Rev B 2006;73:132104.
[47] Gou HY, Hou L, Zhang JW, Gao FM. Appl Phys Lett 2008;92:24190.
[48] Saniz R, Ye LH, Shishidou T, Freeman AJ. Phys Rev B 2006;74:014209.
[49] Hossain MA, Ali MS, Islam AKMA. Eur Phys J B 2012;85:396.
[50] Roknuzzaman M, Islam AKMA. arXiv preprint arXiv 2012;1206:4514.
[51] Anderson OL. J Phys Chem Solids 1963;24:909.
[52] Wei JC, Chen HC, Huang W, Long JP. Mater Sci Semicond Process 2014;27:883.
[53] Zhou SY, Long JP, Huang W. Mater Sci Semicond Process 2014;27:605.
[54] Long JP, Yang LJ, Huang W. Comp Mater Sci 2014;91:315.
[55] Huang W, Chen HC. Phys B 2014;449:133.
[56] Zhou Y, Xiang H, Lu X, Feng Z, Li ZJ. Adv Ceram 2015;4:83.
[57] Mehl Michael J, Klein Barry M, Papaconstantopoulos Dimitri A. Intermetallic Compd: Principles Appl 1994;1:195.
[58] Shen Y, Clarke DR, Fuierer PPA. Appl Phys Lett 2008;93:102907.
[59] Clarke DR. Surf Coat Technol 2003;163:67.
[60] Mao XC, et al. J Phys Soc Jpn 2016;85:114605.
[61] Giannozzi P, et al. J Phys: Condens Matter 2009;21.
[62] Hadi MA, et al. Chin Phys B 2017;26:037103.
[63] McMillan WL. Phys Rev 1968;167:331.