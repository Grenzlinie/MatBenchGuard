# Density functional theory analysis of structural and electronic properties of orthorhombic perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$

Yun Wang, $^{a}$ Tim Gould, $^{b}$ John F. Dobson, $^{b}$ Haimin Zhang, $^{a}$ Huagui Yang, $^{ac}$ Xiangdong Yao $^{b}$ and Huijun Zhao*$^{ad}$

The organic-inorganic hybrid perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$ is a novel light harvester, which can greatly improve the solar-conversion efficiency of dye-sensitized solar cells. In this article, a first-principle theoretical study is performed using local, semi-local and non-local exchange-correlation approximations to find a suitable method for this material. Our results, using the non-local optB86b + vdWDF functional, excellently agree with the experimental data. Thus, consideration of weak van der Waals interactions is demonstrated to be important for the accurate description of the properties of this type of organic-inorganic hybrid materials. Further analysis of the electronic properties reveals that I 5p electrons can be photo-excited to Pb 6p empty states. The main interaction between the organic cations and the inorganic framework is through the ionic bonding between $\text{CH}_3$ and I ions. Furthermore, I atoms in the Pb-I framework are found to be chemically inequivalent because of their different chemical environments.

## 1. Introduction

Dye-sensitized solar cells (DSCs) have stood out among various photovoltaic devices owing to their low cost, simple fabrication procedure, environmental friendliness, and relatively high efficiency. Consequently, DSCs are promising candidates for the next generation solar cells. $^{1–3}$ One recent breakthrough in DSCs is the introduction of organic-inorganic hybrid perovskite materials as novel light harvesters, such as $\text{CH}_3\text{NH}_3\text{PbI}_3$, which can improve the solar conversion efficiency of DSCs to the current best record, *ca.* $15\%^{4–10}$ The high efficiency has been demonstrated by the long exciton diffusion lengths in the perovskite materials. $^{11,12}$ Therefore, understanding the structures and chemistries of these prototype light harvesters is important for the molecular design of organic-inorganic perovskite materials with defined properties.

Perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$ was synthesized and characterized by Weber in $1978.^{13}$ He found that each $\text{Pb}^{2+}$ cation is coordinated to six $\text{I}^{-}$ anions to form $[\text{PbI}_6]$ octahedra, which are corner-connected to each other forming a three-dimensional Pb-I framework. Each $\text{CH}_3\text{NH}_3^{+}$ cation locates at the centre of four $[\text{PbI}_6]$ octahedra. Thus, each cation interacts with $12\ \text{I}^{-}$ anions. $^{14,15}$ Previous experiments demonstrate that the symmetry and structure of $\text{CH}_3\text{NH}_3\text{PbI}_3$ crystals are highly dependent on the temperature. $^{15}$ At low temperature, an orthorhombic phase (space group: *Pnma*) is found. The orthorhombic phase transforms into a tetragonal structure (space group: $I4/m$) above 161.4 K. The cubic phase (space group: $Pm\overline{3}m$) is observed when the temperature is higher than 330.4 K. The improved symmetry at the higher temperature is experimentally proposed to be related to the fast dynamic movement of $\text{CH}_3\text{NH}_3^{+}$ cations within the Pb-I framework. As a result, the location of $\text{CH}_3\text{NH}_3^{+}$ cations can only be determined experimentally in the orthorhombic phase at low temperature. $^{15}$ At the same time, the lattice constants of the orthorhombic crystal vary little at the low temperature. $^{15}$ Therefore, this investigation is focused on the orthorhombic perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$.

Both structural and electronic properties of organic-inorganic hybrid perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$ crystals are investigated in the present *ab initio* calculations. Density functional theory (DFT) is employed as it offers an efficient, yet accurate quantum mechanical method for theorists to optimize structures, determine energies of reactants and products, examine the nature of intermediates, and predict the reaction energies for elementary steps. $^{16–19}$

---
$^{a}$ Centre for Clean Environment and Energy, and Griffith School of Environment, Griffith University, Gold Coast, QLD 4222, Australia.
E-mail: h.zhao@griffith.edu.au

$^{b}$ Queensland Micro- and Nanotechnology Centre, Nathan Campus, Griffith University, QLD 4111, Australia

$^{c}$ Key Laboratory for Ultrafine Materials of Ministry of Education, School of Materials Science and Engineering, East China University of Science and Technology, 130 Meilong Road, Shanghai 200237, China

$^{d}$ Key Laboratory of Materials Physics, Hefei Key Laboratory of Nanomaterials and Nanotechnology, Institutes of Solid State Physics, Chinese Academy of Sciences, Hefei 230031, China

However, there are still areas where traditional DFT with local density (LDA) or generalized gradient (GGA) approximations has its difficulties, such as the depiction of the van der Waals (vdW) interactions.²⁰ This is because the local (LDA) or semi-local (GGA) exchange-correlation (XC) functional approximations neglect the necessary ingredients to describe non-local vdW interactions. The vdW force plays an important role in a range of systems with weak interactions, such as organic-inorganic hybrid materials, particularly in their geometries.²¹ Recently, GGA/DFT calculations have been performed to analyse the electronic properties of cubic, tetrahedral and orthorhombic CH₃NH₃PbI₃. In their study, the experimental structures were employed without considering vdW interactions.¹⁵ Thus, to get a precise theoretical understanding of organic-inorganic hybrids, methods beyond traditional DFT are required.

In the last decade, empirical and less empirical approaches have been developed for prediction of vdW interactions in the DFT context.²²,²³ The vdW-DF class of dispersion energy functionals is generally considered to be a good choice for large systems, except possibly for weakly bound layers,²³,²⁴ or where strongly non-additive effects are important.²⁵⁻²⁷ For the present system, a remaining issue regarding vdW-DF comes from the choice of associated semi-local exchange functionals. Here we will use a recently-proposed semi-local functional optB86b that has been shown to work well in conjunction with vdW-DF for the cohesive properties of conventional solids.²⁸ To confirm the importance of vdW effects for the properties of CH₃NH₃PbI₃, a systematic study using local, semi-local, and non-local XC functionals is performed herein. We present the results for fully optimized structures, density of states, band structures, and charge distributions, which are compared with the available experimental data.

## 2. Computational details

All the theoretical computations are performed by using the Vienna *ab initio* simulation package (VASP) based on DFT with the all-electron projected augmented wave (PAW) method in this study.²⁹,³⁰ Electron-ion interactions are described using ultrasoft pseudopotentials with a kinetic energy cut-off of 520.0 eV.³¹ Valence states included the Pb 6s, 6p, and 5d states, I 5s and 5p states, C 2s and 2p states, N 2s and 2p states, and the H 1s state. When the geometry is optimized, all atoms are allowed to relax. The cell optimization technique is employed to optimize the lattice constants. We perform Brillouin-zone integrations using Monkhorst-Pack grids of special points with $(4 \times 4 \times 4)$ and $(8 \times 8 \times 8)$ meshes for the calculations of structural and electronic properties, respectively. The supercell of orthorhombic CH₃NH₃PbI₃ includes 48 atoms.

A range of specific functionals have been developed for local LDA, semi-local GGA, and non-local vdW-DF approaches previously. In this study, typical functionals for each approach have been chosen to represent their respective class. The functionals parameterized by (PZ81)³² and Perdew-Burke-Ernzerhof (PBE)³³ are employed for local LDA and semi-local GGA methods, respectively. Here, we use the non-local vdW-DF method proposed by Dion *et al.* to describe the vdW interaction as modified by Klimes *et al.*²³,²⁸ In this approach, the XC energy $E_{\text{XC}}$ takes the form:

$$
E_{\text{XC}} = E_{\text{X}}^{\text{GGA}} + E_{\text{C}}^{\text{LDA}} + E_{\text{C}}^{\text{nl}}
$$

Here the exchange energy $E_{\text{X}}^{\text{GGA}}$ uses the optimized optB86b GGA functional,²⁸ and $E_{\text{C}}^{\text{LDA}}$ is the LDA functional for correlation energy. $E_{\text{C}}^{\text{nl}}$ is obtained using a relatively simple double space integration.

## 3. Results and discussion

Determining correct structural properties of materials is essential for the analysis of their other properties, such as the bandgap of semiconductors.³⁴ To compare the performance of various functionals, the structures of organic-inorganic hybrid perovskite CH₃NH₃PbI₃ crystals are firstly optimized. The initial lattice constants and atomic coordinates of orthorhombic CH₃NH₃PbI₃ crystals for theoretical optimizations are obtained from the X-ray diffraction (XRD) experiments at 100 K.¹⁵ The optimized lattice constants and volumes using the various functionals are listed in Table 1 with the available experimental values.¹⁴,¹⁵ In general, the PZ81/LDA functional underestimates all the lattice constants, while the PBE/GGA functional overestimates them.³⁵ The deviations in volumes of PZ81 and PBE are larger than 6.0%. The variations of the theoretical lattice constants using PZ81 and PBE are close to those of other solids using similar functionals.³⁶ In our calculation, the best structural descriptions are obtained using the non-local optB86b + vdWDF functional. The deviation with respect to the experimental data is less than 1.0%. To detect the origin of the improvement, we also calculate the structural properties of orthorhombic CsPbI₃ crystals, as listed in Table 1. It can be found that properties determined using PBE/GGA and optB86b + vdWDF methods are similar as that of orthorhombic CH₃NH₃PbI₃.³⁷ Considering that the main difference between CsPbI₃ and CH₃NH₃PbI₃ crystals is the cations. Thus, the significant improvement in the calculation accuracy of the orthorhombic CH₃NH₃PbI₃ crystals demonstrates that the weak vdW binding between the organic components across the inorganic framework is required to depict the structural properties of this type of organic-inorganic hybrid materials. This conclusion is different

Table 1 The theoretical lattice constants and Pb–I bond lengths of orthorhombic CH₃NH₃PbI₃ and CsPbI₃ in comparison with the experimental data

| | $a$ (Å) | $b$ (Å) | $c$ (Å) | $V$ (Å³) |
|---|---|---|---|---|
| CH₃NH₃PbI₃ | | | | |
| PZ81/LDA | 8.678 | 12.387 | 8.318 | 894.05 |
| PBE/GGA | 9.226 | 12.876 | 8.619 | 1023.88 |
| optB86b + vdWDF | 8.831 | 12.648 | 8.570 | 957.18 |
| Exp¹⁵ | 8.836 | 12.580 | 8.555 | 951.01 |
| Exp¹⁴ | 8.861 | 12.659 | 8.581 | 962.54 |
| CsPbI₃ | | | | |
| PZ81/LDA | 4.674 | 10.17 | 17.27 | 820.92 |
| PBE/GGA | 4.909 | 10.80 | 18.26 | 968.09 |
| optB86b + vdWDF | 4.793 | 10.45 | 17.74 | 888.97 |
| Exp³⁷ | 4.795 | 10.45 | 17.76 | 889.91 |

![](./images/813182032287891456_1.jpg)

Fig. 1 Atomic structures of orthorhombic perovskite $CH_{3}NH_{3}PbI_{3}$ crystals without (left) or with (right) the $[PbI_{6}]$ octahedra. Key: grey – Pb, purple – I, light blue – N, brown – C, and pink – H.

from the assumption used in the recent theoretical studies on organic-inorganic hybrid tetragonal perovskite materials. $^{38}$ The optimized atomic structure of the orthorhombic $CH_{3}NH_{3}PbI_{3}$ crystals using the optB86b + vdWDF functional is shown in Fig. 1.

The structures deduced from the XRD refinement experiments show angular distortions of the $[PbI_{6}]$ octahedra, $^{15}$ such as $\Gamma$ anions showing a significant transverse displacement from the mid-point of the Pb-Pb distance to which they are constrained in the ideal crystallographic description (see Fig. 1). The displacement of atoms causes a reduction in symmetry of the $CH_{3}NH_{3}PbI_{3}$ crystal from the cubic phase to the orthorhombic phase. Table 2 lists the theoretical displacement parameters of Pb1, I1 and I2 atoms, marked in Fig. 1, using various functionals compared with the experimental data. The displacement parameters are the differences in the fractional coordinates of atoms between optimized structures and ideal crystallographic structures. It can be seen that most of the theoretical displacement parameters are in very good agreement with the experimental values, except the displacement of I1 atoms along the $c$ direction. $^{15}$ Also, the displacements of the I1 atoms in $a$ and $c$ directions are larger than those of the I2 atoms. The I2 atoms shift more along the $b$ direction. The Pb-I1-Pb angle is about $159^{\circ}$ in optB86b + vdWDF results, which is $11^{\circ}$ larger than the Pb-I2-Pb angle. These structural differences indicate that I1 and I2 atoms are inequivalent atoms.

<table>
<caption>Table 2 The displacement parameters of Pb1, I1 and I2 atoms for orthorhombic $CH_{3}NH_{3}PbI_{3}$</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>$U_{x}$</th>
<th>$U_{y}$</th>
<th>$U_{z}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pb1</td>
<td>PZ81</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td></td>
<td>PBE</td>
<td>0.000</td>
<td>0.002</td>
<td>0.002</td>
</tr>
<tr>
<td></td>
<td>optB86b + vdWDF</td>
<td>0.001</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td></td>
<td>Exp$^{15}$</td>
<td>0.007</td>
<td>0.003</td>
<td>0.009</td>
</tr>
<tr>
<td>I1</td>
<td>PZ81</td>
<td>0.020</td>
<td>0.000</td>
<td>0.060</td>
</tr>
<tr>
<td></td>
<td>PBE</td>
<td>0.014</td>
<td>0.002</td>
<td>0.064</td>
</tr>
<tr>
<td></td>
<td>optB86b + vdWDF</td>
<td>0.023</td>
<td>0.000</td>
<td>0.065</td>
</tr>
<tr>
<td></td>
<td>Exp$^{15}$</td>
<td>0.019</td>
<td>0.002</td>
<td>0.018</td>
</tr>
<tr>
<td>I2</td>
<td>PZ81</td>
<td>0.013</td>
<td>0.016</td>
<td>0.007</td>
</tr>
<tr>
<td></td>
<td>PBE</td>
<td>0.015</td>
<td>0.024</td>
<td>0.013</td>
</tr>
<tr>
<td></td>
<td>optB86b + vdWDF</td>
<td>0.015</td>
<td>0.017</td>
<td>0.010</td>
</tr>
<tr>
<td></td>
<td>Exp$^{15}$</td>
<td>0.016</td>
<td>0.021</td>
<td>0.014</td>
</tr>
</tbody>
</table>

![](./images/813182032287891456_2.jpg)

Fig. 2 Total density of states (TDOS) of orthorhombic $CH_{3}NH_{3}PbI_{3}$ crystals and their bandgap energies using different functionals.

Since the organic-inorganic hybrid perovskite $CH_{3}NH_{3}PbI_{3}$ materials are used as light harvesters in DSCs, $^{4-6,10}$ their electronic structures are crucial factors for sunlight absorption. In this regard, the total density of states (TDOS) is calculated using the various functionals (see Fig. 2). In our calculations, the bandgap energy with the PZ81/LDA functional is 1.51 eV, which is 17.9% less than that with the PBE/GGA functional. Our bandgap energy of the PBE/GGA functional is $ca$. 10% larger than the previous theoretical value. $^{15}$ This is because the lattice constants used in our study are 8.0% larger than the previous one, in which the experimental lattice constants were used. Our results support the strong relationship between structural properties and bandgap energies, and highlight the importance of using approximations which accurately reproduce the correct geometry. $^{34}$ When the optB86b + vdWDF functional is employed, the theoretical bandgap energy is 1.74 eV, which is $ca$. 0.1 eV smaller than that with the PBE functional. This difference can also be ascribed to the different theoretical lattice constants given by various functionals. According to the optical absorption experiments, the electronic bandgap of orthorhombic $CH_{3}NH_{3}PbI_{3}$ crystals is 1.68–1.72 eV at low temperature. $^{39,40}$ Consequently, the experimental bandgap energies of hybrid $CH_{3}NH_{3}PbI_{3}$ are surprisingly close to the theoretical predictions at the semi-local and non-local levels. Previous DFT studies demonstrate that the bandgap energies of solid-state semiconductors are seriously underestimated by using pure DFT functionals. In some cases, the deviation is about 30%. $^{41,42}$ This is because good band gaps are not normally to be expected from functionals of the types tested here, which do not have hybrid characters. $^{42-44}$ This successful match is likely to be fortuitous, which is also observed in other Pb-based materials. $^{15,38,45}$ Fig. 2 also shows that the characteristics of peaks using various functionals in TDOS images are broadly similar, except for the locations of the peaks.

To understand the bonding mechanisms between the atoms, the analysis of partial density of states (PDOS) has been performed. The calculations of TDOS reveal that the functionals have small effects on the main characteristics of peaks. Therefore, only the

![](./images/813182032287891456_3.jpg)

Fig. 3 TDOS and partial density of states (PDOS) of atoms in orthorhombic $CH_3NH_3PbI_3$ crystals using the optB86b + vdWDF functional. The black and red lines indicate s and p states, respectively.

analysis of PDOS using the optB86b + vdWDF functional is shown in Fig. 3. The PDOS images of I1 and I2 support the argument that these two kinds of I atoms are chemically inequivalent. The PDOS peaks of I2 atoms are closer to the Fermi energy and sharper than those of I1 atoms in the top valence bands. The stronger hybridization of the orbitals can shift the location of valence bands to the lower energy area with wider peaks. $^{46}$ Thus, the different PDOS images of I1 and I2 atoms indicate a weaker bonding between Pb and I2 atoms. From Fig. 3, it was found that organic $CH_3NH_3^+$ cations made little contribution to the top valence and bottom conduction bands around the Fermi energy level $(-4.0\ \text{eV} < E-E_{\text{Fermi}} < 4.0\ \text{eV})$. The main contribution to the top valence band is from the I 5p states with an overlapping of Pb 6s states. In the bottom conduction bands, the main components are Pb 6p states. The PDOS images suggest that I 5p electrons, especially the I2 5p electrons, can be photo-excited to Pb 6p empty states. Consequently, I atoms change into photohole sites and Pb atoms hold the photoelectrons after the photo-excitation. From Fig. 3, we also find that the highest C and N 2p bands and H 1s bands locate at $-6.8$ and $-4.8$ eV, which shows little overlap with the Pb and I orbitals. Thus, there is no covalent interaction between the organic cations and the inorganic Pb-I framework.

The band structures of orthorhombic $CH_3NH_3PbI_3$ using different functionals are shown in Fig. 4. Our results agree with previous studies in showing that orthorhombic $CH_3NH_3PbI_3$ is a direct-bandgap crystal with the minimum band gap at the $\Gamma$ symmetry point. $^{15}$ The minimum indirect bandgap is from the $\Gamma$ point to the $X$ point. For all band structures, several sets of bands can be found. They correspond to C 2p and $H\_C$ (the H atoms bonded to C atoms) 1s states around $-5$ eV, mainly I 5p states below the Fermi level and Pb 6p states above the Fermi level. Both the top valence band and the bottom conduction band are broad, indicating that these states are non-localized. This explains why the excitons can be transported to a long distance in this material. $^{11,12}$ Moreover, the fluctuations of the states in the bottom conduction band are stronger, indicating a faster transport of photoelectrons that matches the experimental observations. $^{12}$ In contrast, the band for organic fragments (the band around $-5$ eV) is flat and narrow, suggesting that the electrons around them are localized. It should also be noted that the band structure of the orthorhombic $CH_3NH_3PbI_3$ crystal is quite different from that of the cubic phase due to the lower symmetry and the bigger primitive cell. The main functional dependent properties are the locations of the bands, which confirm the conclusion from the analysis of DOS images.

![](./images/813182032287891456_4.jpg)

Fig. 4 Calculated band structure of orthorhombic $CH_3NH_3PbI_3$ crystals along the high-symmetry lines in the first Brillouin zone using PZ81/LDA, PBE/GGA, and optB86b + vdWDF functionals.

The Bader charges of Pb, I1, I2, N and C atoms in orthorhombic perovskite $CH_3NH_3PbI_3$ crystals based on the pseudo valence density using different functionals are listed in Table 3. In general, the charge analysis provides a picture of ionic interactions between the inorganic Pb-I framework and organic $CH_3NH_3^+$ cations since the average charge per $PbI_3$ and $CH_3NH_3$ units is $ca$. $-0.7\ e$ and $+0.7\ e$. In contrast, charges of Pb and I atoms correspond to significant deviations from purely ionic interactions ($i.e.$, $Pb^{2+}$ and $\Gamma^-$), which suggests a combined covalent and ionic bonding mechanism between Pb and I atoms. The Pb-I covalent bonding characteristics can also be supported by the hybridization of the Pb 6s, 6p states with the I 5p states at the top valence bands shown in Fig. 3. Within $CH_3NH_3^+$ cations, the $NH_3$ group is almost charge neutral; and most of the positive charge is due to the contribution from the $CH_3$ group. This charge distribution matches the chemical instinct because $NH_3$ is a charge neutral molecule and $CH_3$ is a positively charged cation in the gas phase. The charge distribution shown in Table 3 indicates that there is a slightly stronger ionic interaction between the $CH_3$ group and I1 atoms. From the

<table><caption>Table 3 Bader atomic charges of $CH_3NH_3PbI_3$ using various functionals</caption>
<tbody>
<tr>
<td>
</td>
<td>
LDA
</td>
<td>
PBE
</td>
<td>
optB86b + vdWDF
</td>
<td>
optB86b + vdWDF (AE)
</td>
</tr>
<tr>
<td>Pb</td>
<td>+0.85</td>
<td>+0.95</td>
<td>+0.92</td>
<td>+0.86</td>
</tr>
<tr>
<td>I1</td>
<td>−0.52</td>
<td>−0.57</td>
<td>−0.55</td>
<td>−0.55</td>
</tr>
<tr>
<td>I2</td>
<td>−0.50</td>
<td>−0.55</td>
<td>−0.54</td>
<td>−0.54</td>
</tr>
<tr>
<td>N</td>
<td>−3.01</td>
<td>−2.96</td>
<td>−2.95</td>
<td>−1.33</td>
</tr>
<tr>
<td>C</td>
<td>+0.35</td>
<td>+0.53</td>
<td>+0.48</td>
<td>+0.44</td>
</tr>
<tr>
<td>$PbI_3$</td>
<td>−0.67</td>
<td>−0.72</td>
<td>−0.70</td>
<td>−0.77</td>
</tr>
<tr>
<td>$CH_3$</td>
<td>+0.67</td>
<td>+0.67</td>
<td>+0.64</td>
<td>+0.68</td>
</tr>
<tr>
<td>$NH_3$</td>
<td>−0.01</td>
<td>+0.04</td>
<td>+0.05</td>
<td>+0.02</td>
</tr>
</tbody>
</table>

PDOS analysis, it was found that there is a stronger Pb-I1 covalent bonding. Thus, I1 atoms have overall stronger interactions with their adjacent atoms, which explains why I1 and I2 atoms are chemically inequivalent, as observed in Fig. 3. In the tetragonal and cubic phases, the symmetries of Pb-I frameworks are improved due to the thermal movement of organic cations.¹⁵ In those cases, the inequivalence of I atoms may be eliminated. A study on the thermal effect on the phase change and properties of $CH_3NH_3PbI_3$ materials is currently underway. Since the charge analysis using the all-electron (AE) reconstructed valence density could give more accurate results,⁴⁷ the calculations based on the AE data using optB86B + vdWDF are also performed, as listed in Table 3. It can be seen that conclusions drawn from both sets of data are almost identical. The main difference is the charge of N atoms and the H atoms bonded with N atoms.

### 4. Conclusions

In summary, first-principle DFT calculations have been performed to study structural and electronic properties of orthorhombic perovskite $CH_3NH_3PbI_3$ materials. Our results demonstrate that the employment of the optB86b + vdWDF XC functional improves the accuracy of the calculated structural properties significantly compared with the non-vdW functionals employed here. Thus, consideration of the vdW interactions is important for theoretical studies of this organic-inorganic hybrid material. The main interaction between the organic groups and the inorganic framework is through the ionic bonding between $CH_3^+$ cations and $I^-$ anions. The different interaction strengths between I atoms with their adjacent atoms cause the formation of two kinds of I atoms in the Pb-I framework. Analysis of the electronic properties supports the conclusion that orthorhombic $CH_3NH_3PbI_3$ is a direct-bandgap crystal with the minimum band gap at the $\Gamma$ symmetry point. During light harvesting, I 5p electrons can be photo-excited to Pb 6p empty states. Our results, therefore, pave the way for the further theoretical studies on this type of organic-inorganic hybrid perovskite materials for sensitized solar cells.

### Acknowledgements

We thank the Australian Research Council for funding. This research was undertaken at the National Computational Infrastructure (NCI) in Canberra, Australia, which is supported by the Australian Commonwealth Government.

## Notes and references

1 M. Gratzel, *Nature*, 2001, **414**, 338-344.

2 B. Oregan and M. Gratzel, *Nature*, 1991, **353**, 737-740.

3 S. F. Zhang, X. D. Yang, Y. H. Numata and L. Y. Han, *Energy Environ. Sci.*, 2013, **6**, 1443-1464.

4 J. Burschka, N. Pellet, S. J. Moon, R. Humphry-Baker, P. Gao, M. K. Nazeeruddin and M. Gratzel, *Nature*, 2013, **499**, 316-320.

5 J. Bisquert, *J. Phys. Chem. Lett.*, 2013, **4**, 2597-2598.

6 H. S. Kim, C. R. Lee, J. H. Im, K. B. Lee, T. Moehl, A. Marchioro, S. J. Moon, R. Humphry-Baker, J. H. Yum, J. E. Moser, M. Gratzel and N. G. Park, *Sci. Rep.*, 2012, **2**, 591.

7 M. M. Lee, J. Teuscher, T. Miyasaka, T. N. Murakami and H. J. Snaith, *Science*, 2012, **338**, 643-647.

8 N. G. Park, *J. Phys. Chem. Lett.*, 2013, **4**, 2423-2429.

9 D. Q. Bi, L. Yang, G. Boschloo, A. Hagfeldt and E. M. J. Johansson, *J. Phys. Chem. Lett.*, 2013, **4**, 1532-1536.

10 M. Liu, M. B. Johnston and H. J. Snaith, *Nature*, 2013, **501**, 395-398.

11 S. D. Stranks, G. E. Eperon, G. Grancini, C. Menelaou, M. J. Alcocer, T. Leijtens, L. M. Herz, A. Petrozza and H. J. Snaith, *Science*, 2013, **342**, 341-344.

12 G. Xing, N. Mathews, S. Sun, S. S. Lim, Y. M. Lam, M. Gratzel, S. Mhaisalkar and T. C. Sum, *Science*, 2013, **342**, 344-347.

13 D. Weber, *Z. Naturforsch., B: J. Chem. Sci.*, 1978, **33**, 1443-1445.

14 A. Poglitsch and D. Weber, *J. Chem. Phys.*, 1987, **87**, 6373-6378.

15 T. Baikie, Y. N. Fang, J. M. Kadro, M. Schreyer, F. X. Wei, S. G. Mhaisalkar, M. Graetzel and T. J. White, *J. Mater. Chem. A*, 2013, **1**, 5628-5641.

16 W. Kohn and L. J. Sham, *Phys. Rev. A*, 1965, **140**, 1133.

17 Y. Zhao, N. E. Schultz and D. G. Truhlar, *J. Chem. Theory Comput.*, 2006, **2**, 364-382.

18 A. Vittadini, M. Casarin and A. Selloni, *Theor. Chem. Acc.*, 2007, **117**, 663-671.

19 E. A. Carter, *Science*, 2008, **321**, 800-803.

20 Y. Andersson, D. C. Langreth and B. I. Lundqvist, *Phys. Rev. Lett.*, 1996, **76**, 102-105.

21 J. P. P. Ramalho, J. R. B. Gomes and F. Illas, *RSC Adv.*, 2013, **3**, 13085-13100.

22 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, *J. Chem. Phys.*, 2010, **132**, 154104.

23 M. Dion, H. Rydberg, E. Schroder, D. C. Langreth and B. I. Lundqvist, *Phys. Rev. Lett.*, 2004, **92**, 246401.

24 T. Bjorkman, A. Gulans, A. V. Krasheninnikov and R. M. Nieminen, *Phys. Rev. Lett.*, 2012, **108**, 235502.

25 J. F. Dobson, A. White and A. Rubio, *Phys. Rev. Lett.*, 2006, **96**, 073201.

26 J. F. Dobson and T. Gould, *J. Phys.: Condens. Matter*, 2012, **24**, 073201.

27 V. Gobre and A. Tkatchenko, *Nat. Commun.*, 2013, **4**, 2341.

28 J. Klimes, D. R. Bowler and A. Michaelides, *Phys. Rev. B*, 2011, **83**, 195131.

29 G. Kresse and J. Furthmuller, *Comput. Mater. Sci.*, 1996, **6**, 15-50.

30 G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 1758-1775.

31 D. Vanderbilt, *Phys. Rev. B*, 1990, **41**, 7892.

32 J. P. Perdew and A. Zunger, *Phys. Rev. B*, 1981, **23**, 5048.

33 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

34 I. Borriello, G. Cantele and D. Ninno, *Phys. Rev. B*, 2008, **77**, 235214.

35 A. E. Mattsson, R. Armiento, J. Paier, G. Kresse, J. M. Wills and T. R. Mattsson, *J. Chem. Phys.*, 2008, **128**, 084714.

36 G. I. Csonka, J. P. Perdew, A. Ruzsinszky, P. H. T. Philipsen, S. Lebegue, J. Paier, O. A. Vydrov and J. G. Angyan, *Phys. Rev. B*, 2009, **79**, 155107.

37 C. K. Moller, *Nature*, 1958, **182**, 1436.

38 E. Mosconi, A. Amat, M. K. Nazeeruddin, M. Gratzel and F. De Angelis, *J. Phys. Chem. C*, 2013, **117**, 13902-13913.

39 T. Ishihara, *J. Lumin.*, 1994, **60-1**, 269-274.

40 G. C. Papavassiliou and I. B. Koutselas, *Synth. Met.*, 1995, **71**, 1713-1714.

41 Y. Wang, T. Sun, D. J. Yang, H. W. Liu, H. M. Zhang, X. D. Yao and H. J. Zhao, *Phys. Chem. Chem. Phys.*, 2012, **14**, 2333-2338.

42 Y. Wang, H. M. Zhang, P. R. Liu, X. D. Yao and H. J. Zhao, *RSC Adv.*, 2013, **3**, 8777-8782.

43 J. Heyd, G. E. Scuseria and M. Ernzerhof, *J. Chem. Phys.*, 2006, **124**, 2204597.

44 Y. Wang, S. de Gironcoli, N. S. Hush and J. R. Reimers, *J. Am. Chem. Soc.*, 2007, **129**, 10402-10407.

45 H. Z. Lv, H. W. Gao, Y. Yang and L. K. Liu, *Appl. Catal., A*, 2011, **404**, 54-58.

46 R. Hofmann, *Solids and surfaces: A chemist's view of bonding in extended structures*, VCH publishers, Inc., New York, 1988.

47 E. Aubert, S. Lebegue, M. Marsman, T. T. B. Thai, C. Jelsch, S. Dahaoui, E. Espinosa and J. G. Angyan, *J. Phys. Chem. A*, 2011, **115**, 14484-14494.