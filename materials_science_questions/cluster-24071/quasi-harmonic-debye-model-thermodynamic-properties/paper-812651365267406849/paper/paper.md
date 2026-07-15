Journal Pre-proof

![](./images/812651365267406849_1.jpg)

Study of the structural, mechanical and thermodynamic properties of the new MAX phase compounds $(Zr_{1-x}Ti_x)_3AlC_2$

Ismail Ouadha, Habib Rached, Ahmed Azzouz-Rached, Abderrahmane Reggad, Djamel Rached

|PII:|S2352-2143(20)30014-9|
|---|---|
|DOI:|https://doi.org/10.1016/j.cocom.2020.e00468|
|Reference:|COCOM 468|

To appear in:  *Computational Condensed Matter*

Received Date: 10 February 2020

Revised Date: 22 March 2020

Accepted Date: 23 March 2020

Please cite this article as: I. Ouadha, H. Rached, A. Azzouz-Rached, A. Reggad, D. Rached, Study of the structural, mechanical and thermodynamic properties of the new MAX phase compounds $(Zr_{1-x}Ti_x)_3AlC_2$, *Computational Condensed Matter* (2020), doi: https://doi.org/10.1016/j.cocom.2020.e00468.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier B.V.

# Study of the structural, mechanical and thermodynamic properties of the new MAX phase compounds $(Zr_{1-x}Ti_x)_3AlC_2$

Ismail OUADHA¹, Habib RACHED¹,², *, Ahmed AZZOUZ-RACHED², Abderrahmane REGGAD³ and Djamel RACHED¹.

¹ Magnetic Materials Laboratory, Faculty of exact Sciences, Djillali Liabes University of Sidi Bel-Abbes, Algeria
² Department of physics, Faculty of exact Sciences and informatics, Hassiba Benbouali University of Chlef, Algeria.
³ C2MO, Engineering Physics Laboratory, Matter Sciences Faculty, Ibn Khaldoun University, Tiaret, Algeria

## ABSTRACT

The structural, electronic, mechanical and the thermodynamic properties of the MAX phases $(Zr_{1-x}Ti_x)_3AlC_2$ compounds have been investigated by using the full-potential plane-wave FP-LAPW method as implemented in the Wien2k code. The exchange-correlation (XC) energy of electrons was treated using the Perdew–Burke–Ernzerhof parametrization. The ground-state properties for the studied compounds were calculated and compared with available experimental and theoretical data. The calculated lattice parameters are reasonably comparable with experimental and theoretical results. The formation energy has been evaluated in order to determinate the stability of our compounds. The calculation of the electronic structure was predicted for the first time for the present MAX phase compounds. These results indicate that, all our compounds exhibit metallic behavior and this metallicity is due to the p-d hybridization. The elastic constants have also evaluated by the Hex-elastic package. The mechanical stability reveal that, all our compounds are stable mechanically. The bulk modulus, shear modulus, Young's modulus, Poisson's ratio and Cauchy pressure were calculated and discussed in detail. Furthermore, the temperature and pressure effect on: Bulk modulus, Debye temperature and heat capacity at constant volume and constant pressure $C_V$ and $C_P$, respectively have been investigated by the quasi-harmonic Debye model.

**Keywords:** New MAX phases; mechanical properties; thermodynamic properties; bonding nature.

* Corresponding authors: +213661223197, **E-mail address:** habib_rached@yahoo.fr (Dr. H. Rached).

### 1. Introduction

The MAX phases $\text{M}_{\text{n+1}}\text{AX}_{\text{n}}$ are compounds with specific composition where M is an early transition metal, A is an A-group element and X is C and/or N, knows as 211, 312, 413 MAX phases for n=1, 2 and 3, respectively. They have attracted an intensive interest at the community of science for nearly two decades. This group of compounds crystallizes with the hexagonal P6₃/mmc space group (#194) [1-3]. The first study of this type of compounds was done on the $\text{Ti}_3\text{SiC}_2$ powder to determine its specific properties [3]. The interest on the MAX phases increased since mid- 1990s after the intrinsic properties of the compounds became known [4, 5]. By combining the properties of metals and ceramics, MAX phases have an exceptional properties: high elastic stiffness, high melting temperature, high thermal shock resistance and high electrical conductivity [6, 7].

In 2016, T. Laupauw et al. were the first to succeed to synthesize experimentally a new compound $\text{Zr}_3\text{AlC}_2$ of MAX family (312) [8]. The MAX phase materials are known to enter into many industrial applications for their desirable property [9], such as in aerospace, automotive, defense, medical and nuclear reactors [10-12]. A lot of MAX phase compounds are studied in the recent years by Gokhan Surucu et al. [13-18]. The structural, mechanical, electronic and lattice dynamic properties of hypothetical $\text{Sc}_2\text{AlB}_{0.5}\text{C}_{0.5}$, $\text{Sc}_2\text{AlB}_{0.5}\text{N}_{0.5}$ and $\text{Sc}_2\text{AlC}_{0.5}\text{N}_{0.5}$ compounds are investigated by CASTEP plane-wave pseudo-potential code. These compounds have hexagonal crystal structure and show a metallic behavior. The same author Gokhan have also investigate the structural, electronic, dynamic, and thermo-elastic properties of $\text{M}_2\text{AlB}$ (X = V, Nb, Ta) MAX phase borides by VASP code, which are found to be energetically, mechanically and dynamically stable. To get better properties of the MAX family compounds, Zapata-Solvas et al. synthesized experimentally solid solutions $(\text{Zr}_{3-\text{x}}\text{Ti}_\text{x})\text{AlC}_2$ by mixing Zr with Ti for different x concentration [9, 19, 20]. M.A. Hadi et al. have studied the structural and optical properties of these solutions $(\text{Zr}_{1-\text{x}}\text{Ti}_\text{x})_3\text{AlC}_2$ [19]. The elastic and thermodynamic properties also were studied by M.A. Hadi et al. to understand their mechanical comportment under extreme conditions [20].

In order to widen previous works on $\text{Zr}_3\text{AlC}_2$ and $\text{Ti}_3\text{AlC}_2$ compounds and enriched literature by the as yet uninvestigated properties of the $(\text{Zr}_{3-\text{x}}\text{Ti}_\text{x})\text{AlC}_2$, we have investigated the structural, mechanical electronic and thermodynamic properties of new quaternary MAX phases

$(Zr_{1-x}Ti_x)_3AlC_2$ for different concentrations (x=0, 0.5, 1) by using a first-principles density functional theory (DFT) [21, 22].

## 2. Computational method

To doing our calculation, we have employed full potential linearized augmented plane wave (FP-LAPW) method [23] implemented in the Wien2k code [24] and based on the density functional theory (DFT) which has proven to be one of the most accurate theory for the calculation of the electronic and structural properties of solids [25-40]. In the FP-LAPW method, the space is divided into two regions: the first is a non-overlapping muffin-tin (MT) spheres where the basis set inside this region is described by radial solutions of the one-particle Schrodinger equation and their energy derivatives multiplied by spherical harmonics and the second one which is interstitial region (IR) the basis set consists of plane waves [41]. For the exchange-correlation functional we have adopted the generalized gradient approximation (GGA) parametrized by Perdew-Burke-Ernzerhof (PBE) [42]. The convergence tests allow us to choose the parameter $R_{mt}*K_{max}$=8 where $R_{mt}$ is the smallest atomic sphere radius and Kmax is the plane wave cut-off [43]. The chosen $R_{MT}$ values of Zr, Ti, Al and C are 1.96, 1.96, 2.38 and 1.74 Bohr, respectively. The $G_{max}$ was chosen to equal the 14 value where $G_{max}$ is defined as the magnitude of the largest vector in the charge density Fourier expansion. The MT sphere were considered up to $l_{max}$=10. The Monkorst-Pack method in the first Brillouin zone (IBZ) was performed using 1500 kpoints. The charge convergence was set to $10^{-4}$.

The $M_3AlC_2$ compounds crystallize in a hexagonal structure with the $P6_3/mmc$ space group (#194) [8, 44] as shown in Fig.1. The atoms Zr occupy the Wyckoff positions 2a and 4f with $Z_M$ ~ 0.12. The Al atoms occupy 2b atomic positions while the C atoms reside in 4f with $Z_C$ ~ 0.07 (Table. 1).

## 3. Results and discussions

### 3.1. Structural properties

We have used the 2D-optimize package developed by J. Morteza [45] to determine the structural lattice parameters of our compounds. In the Table. 2, we presented our results and some other experimental and theoretical results recently obtained for comparison. We can see

that our results are in good agreement with corresponding experimental and theoretical results.
We can see also that when the x concentration increase, all the lattice parameters a and c and the volume of unit cell decrease while the hexagonal ration c/a increase. We can interpret that by the decrease of the atomic radius because the atomic radius of Ti atom is less than the one of the Zr atom. In attempt to identify the effect of pressure on the structural properties, we have investigate the parameters constants a and c under pressure effect in the range from 0 to 25 GPa. The Fig. 2 illustrate the Lattice parameters a and c as function of pressure. We can note that when the pressure is enhanced the compression along the (a,c)-axis decreases.

To calculate the stability of our compounds, the best indicator is their formation energy. The formation energy is calculated using the following equation [18, 46]:

$$
\Delta E_{f_{\left(\mathrm{Zr}_{1-x} \mathrm{Ti}_{x}\right)_{3} \mathrm{AlC}_{2}}}=E_{t o t_{\left(\mathrm{Zr}_{1-x} \mathrm{Ti}_{x}\right)_{3} \mathrm{AlC}_{2}}}-\left(3(1-x) E_{Z r}+3 x E_{T i}+E_{A l}+2 E_{C}\right) \quad(1)
$$

where $\Delta E_{f}(Pb_{2} FeMO_{6})$ is the formation enthalpy of $(Zr_{1-x}Ti_{x})_{3}AlC_{2}$ with ((x=0, 0.5, 1), $E_{tot}$ is the total energy per unit cell of the bulk compounds, E(X= Zr, Ti, Al and C), it represents the total energy per atom of the element in pure solid state. The calculated formation enthalpies of our compounds are regrouped in Table 2. To the best of our knowledge, the formation enthalpy has not been measured or calculated yet for these compounds, hence our result maybe considered as a quantitative theoretical prediction. From these results, it is obvious that the calculated formation enthalpies are negative, which indicates that the examined compounds are quite stable even at high temperatures.

### 3.2. Mechanical properties

The study of the mechanical properties is based upon the determination of the elastic parameters. These parameters allow us to get knowledge about the structural stability and anisotropic character of a material. Furthermore, when a pressure is applied on a material, these parameters are able to provide information about the mechanical stability, and strength under compression. In our hexagonal system of $(Zr_{1-x}Ti_{x})_{3}AlC_{2}$ MAX phases, there are six different elastic constants $C_{11}, C_{12}, C_{13}, C_{33}, C_{44}$ and $C_{66}$ where $C_{66}=\frac{(C 11-C 12)}{2}$. We have used the Hex-elastic package of Jamal Morteza to determine the elastic constants of our compounds at their

equilibrium lattice constants [47]. The elastic constants are derived by means of a Taylor expansion of the total energy $E(V, \varepsilon_{i})$ of the system with respect to the strain tensor $\varepsilon_{i}$:

$$
E(V, \varepsilon_{i})=E_{0}(V_{0}, 0)+V_{0}\left(\sum_{i} \tau_{i} \xi_{i} \varepsilon_{i}+\frac{1}{2} \sum_{i j} c_{i j} \varepsilon_{i} \xi_{i} \varepsilon_{j} \xi_{j}\right)+O\left(\varepsilon^{3}\right) \tag{2}
$$

Where $E_{0}$ and $V_{0}$ are the energy and the volume of unstrained hexagonal system respectively. The factor $\xi_{i}$, takes the value 1 if the index $i$ is equal to 1,2 or 3 and the value 2 if it is equal to 4,5 or 6. In the above equation $\tau_{i}$ are related to the strain on the crystal. For our compounds, the total energy from equation (2) is modified by applying six distortions described as follows:

$$
D_{1}=\left(\begin{array}{ccc}
1+\varepsilon & 0 & 0 \\
0 & 1+\varepsilon & 0 \\
0 & 0 & 1
\end{array}\right) \tag{2}
$$

$$
D_{2}=\left(\begin{array}{ccc}
1+\varepsilon & 0 & 0 \\
0 & 1+\varepsilon & 0 \\
0 & 0 & \frac{1}{(1+\varepsilon)^{2}}
\end{array}\right) \tag{3}
$$

$$
D_{3}=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1+\varepsilon
\end{array}\right) \tag{4}
$$

$$
D_{4}=\left(\begin{array}{ccc}
\left(\frac{1+\varepsilon}{1-\varepsilon}\right)^{\frac{1}{2}} & 0 & 0 \\
0 & \left(\frac{1-\varepsilon}{1+\varepsilon}\right)^{\frac{1}{2}} & 0 \\
0 & 0 & 1
\end{array}\right) \tag{5}
$$

$$
D_{5}=\left(\begin{array}{ccc}
1 & 0 & \varepsilon \\
0 & 1 & \varepsilon \\
\varepsilon & \varepsilon & 1+\varepsilon^{2}
\end{array}\right) \tag{6}
$$

$$
D_{6}=\left(\begin{array}{ccc}
\left(1+\varepsilon^{2}\right)^{\frac{1}{2}} & \varepsilon & 0 \\
\varepsilon & \left(1+\varepsilon^{2}\right)^{\frac{1}{2}} & 0 \\
0 & 0 & 1
\end{array}\right) \tag{7}
$$

The energy for these distortions can be obtained as:

$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(\left(C_{11}+C_{12}\right) \varepsilon^{2}+O\left(\varepsilon^{3}\right)\right) \quad(8)
$$

$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(\frac{C_{33}}{2} \varepsilon^{2}+O\left(\varepsilon^{3}\right)\right) \quad(09)
$$

$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(\left(C_{z z}\right) \varepsilon^{2}+O\left(\varepsilon^{3}\right)\right) \quad(10)
$$

with
$$
C_{z z}=C_{11}+C_{12}+2 C_{33}-4 C_{13} \quad(11)
$$

$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(\left(C_{11}-C_{12}\right) \varepsilon^{2}+O\left(\varepsilon^{4}\right)\right) \quad(12)
$$

$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(4\left(C_{44}\right) \varepsilon^{2}+O\left(\varepsilon^{3}\right)\right) \quad(13)
$$

and
$$
E(V, \varepsilon)=E\left(V_{0}, 0\right)+V_{0}\left(2\left(C_{66}\right) \varepsilon^{2}+O\left(\varepsilon^{3}\right)\right) \quad(14)
$$

respectively.

Our results of these elastic constants are illustrated in Table. 3. To date, there is no experimental report in the elastic constants for the herein investigated compounds. We can observe obviously that all these elastic constants $C_{i j}$ are positive and completely satisfy the conditions of mechanic stability of compounds for hexagonal structure [49]:

$$
\mathrm{C}_{11}>0, \mathrm{C}_{33}>0, \quad \mathrm{C}_{44}>0, \quad \mathrm{C}_{11}-\mathrm{C}_{12}>0, \quad\left(\mathrm{C}_{11}+\mathrm{C}_{12}\right) \mathrm{C}_{33}>2 \mathrm{C}_{13}^{2} \quad(15)
$$

These results confirm the stability of the $(Zr_{1-x} Ti_{x})_{3} AlC_{2}$ MAX phases against any elastic deformation. Meanwhile, the present results of the elastic constants shows that $C_{33}$ is larger than $C_{11}$ for all our compounds, which reveals that the $a$ and $b$-axes are more compressible than the $c$-axis. These results can be explained in terms of the existence of strong covalent bonding in the [001] direction for the studied compounds. Also, we can note that the $C_{11}$ and $C_{33}$ are considerably higher than other elastic constants, which divulge an elastic anisotropy in these compounds.

From the elastic constants we have calculate the elastic modulus which allow us to determine all the mechanical properties. These modulus are the bulk modulus B and the shear modulus G. The B measures the resistance of a material to volume change and provides us an estimate of its response to a hydrostatic pressure, while G describes the resistance of a material to shape change [50]. From the Hill approximation which based on the Reuss and Voigt

approaches, the compressibility modulus B and the shear modulus G are given by these following expressions [51-53]:

$$
B_{V}=\frac{2\left(C_{11}+C_{12}\right)+C_{33}+4 C_{13}}{9} \tag{16}
$$

$$
B_{R}=\frac{\left(C_{11}+C_{12}\right) C_{33}-2 C_{13}^{2}}{C_{11}+C_{12}+2 C_{33}-4 C_{13}} \tag{17}
$$

$$
B_{H}=\frac{B_{V}+B_{R}}{2} \tag{18}
$$

$$
G_{V}=\frac{C_{11}+C_{12}+2 C_{33}-4 C_{13}+12\left(C_{44}+C_{66}\right)}{30} \tag{19}
$$

$$
G_{R}=\frac{5}{2} \frac{\left[\left(C_{11}+C_{12}\right) C_{33}-2 C_{13}^{2}\right] C_{44} C_{66}}{3 B_{V} C_{44} C_{66}+\left[\left(C_{11}+C_{12}\right) C_{33}-2 C_{13}^{2}\right]\left(C_{44}+C_{66}\right)} \tag{20}
$$

$$
G_{H}=\frac{G_{V}+G_{R}}{2} \tag{21}
$$

Where B = $B_H$ (the Hill bulk modulus) and G = $G_H$ (the Hill shear). The Young's modulus E and Poisson's ratio $v$ of a hexagonal structure are also calculated by using the following expressions [54]:

$$
E=\frac{9 \mathrm{BG}}{3 \mathrm{~B}+\mathrm{G}} \tag{22}
$$

$$
v=\frac{3 \mathrm{~B}-\mathrm{E}}{6 \mathrm{~B}} \tag{23}
$$

The Young's modulus is considered as a measure of the material's ability to resist stress and pressure in the elastic deformation range [55]. More Young's modulus is bigger, more the deformation of matter is difficult. The values of the B, G and E magnitudes for our compounds $\mathrm{Zr}_{3} \mathrm{AlC}_{2}$, $\left(\mathrm{Zr}_{0.5} \mathrm{Ti}_{0.5}\right)_{3} \mathrm{AlC}_{2}$ and $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$ are represented in the Table. 3. We can see that, when the concentration x increase, the values of B, G and E increase. The compound $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$ present a higher ability to resist deformation, while it's the inverse in the case of the compound $\mathrm{Zr}_{3} \mathrm{AlC}_{2}$. The Poisson's ratio $v$ is frequently used to deduce the type of the chemical bonding. When its value is less than 0.25, the chemical bonding has a covalent, while if its value

is more than 0.25, the bonding will be a typical ionic [56]. The calculated values of the Poisson's ratio $v$ are $0.255, 0.249$ and 0.233 for $Zr_{3} AlC_{2},(Zr_{0.5} Ti_{0.5})_{3} AlC_{2}$ and $Ti_{3} AlC_{2}$ respectively, which indicate that the chemical bonding nature is more ionic for $Zr_{3} AlC_{2}$, have a mixed nature for $(Zr_{0.5} Ti_{0.5})_{3} AlC_{2}$ and more covalent for $Ti_{3} AlC_{2}$. It's also possible to study the nature of the chemical bonding using the Cauchy pressure. When the value of Cauchy pressure is positive, then the ionic bonding is dominant, while the covalent bonding is dominant when its value is negative [57]. In hexagonal system, the Cauchy pressure is estimated for the different directions as follows:

$$
\mathrm{p}_{\mathrm{x}}^{\text {Cauchy }}=\mathrm{C}_{13}-\mathrm{C}_{44} \tag{24}
$$

$$
\mathrm{p}_{\mathrm{y}}^{\text {Cauchy }}=\mathrm{C}_{12}-\mathrm{C}_{66} \tag{25}
$$

From the Table. 3, it clear that for the $Ti_{3} AlC_{2}$ compound, all the values of Cauchy pressure $\mathrm{p}_{x}^{\text {Cauchy }}$ or $\mathrm{p}_{y}^{\text {Cauchy }}$ are negative, which confirm the more covalent character for this compound, while the compounds $Zr_{3} AlC_{2}$ and $(Zr_{0.5} Ti_{0.5})_{3} AlC_{2}$ have positive values of $\mathrm{p}_{x}^{\text {Cauchy }}$ and negative values of $\mathrm{p}_{y}^{\text {Cauchy }}$ which indicate the mixed nature for these compounds, especially in for the compound $Zr_{3} AlC_{2}$ where the ionic character is clear. In engineering science, calculating the Poisson ratio allow us to classify materials as brittle or ductile. If the Poisson ratio of a material is greater than the value 0.26, it is considered as ductile, otherwise if it is considered as brittle [58]. For our compounds, we have found that all Poisson ratio values are less than 0.26, which means that they are all classified as brittle. Another criterion called Pugh criterion can also make classification of ductile and brittle materials. When B/G is greater than 1.75, the material will be ductile, and if not, it will be considered brittle [59]. From our results of B/G ratio in the Table. 3, we obtained that all the B/G values are less than 1.75 which confirms that these compounds exhibit a brittle nature.

The calculation of the shear anisotropic factors of materials is extremely important to study the degree of durability related mainly to micro-cracks in crystals. In our hexagonal system, we have calculated three elastic anisotropy factors $A_{1}, A_{2}$ and $A_{3}$ [60], where $A_{1}$ for $\{100\}$ planes between the [011] and [010] directions, $A_{2}$ for $\{010\}$ shear planes between the [101] and [001] directions and $A_{3}$ for $\{001\}$ shear planes between the [110] and [010] directions, where:

$$
A_{1}=\frac{C_{11}+C_{12}+2 C_{33}-4 C_{13}}{6 C_{44}} \tag{26}
$$

$$
A_{2}=\frac{2 C_{44}}{C_{11}+C_{12}} \tag{27}
$$

$$
A_{3}=\frac{C_{11}+C_{12}+2 C_{33}-4 C_{13}}{3\left(C_{11}-C_{12}\right)} \tag{28}
$$

All the values of $A_{1}, A_{2}$ and $A_{3}$ must be equal to 1 for an isotropic crystal while they differ from 1 for anisotropic crystal [61]. According to our results reported in Table. 3, all the anisotropy factors are greater or smaller than 1, which indicates that the $(Zr_{1-x}Ti_{x})_{3}AlC_{2}$ MAX phase compounds exhibit an anisotropy behavior.

Hardness is another mechanical property of a material related to the elastic and plastic response of a material. In general, hardness is an important indicator of corrosion resistance of materials, so the most corrosion-resistant materials are those with the greater hardness [62]. We have used the formula of Chen of Vickers's Hardness [63]:

$$
H_{V}=2\left(\frac{G^{3}}{B^{2}}\right)^{0.585}-3 \tag{29}
$$

The calculated results are found to equal 12.48 GPa, 13.52 GPa and 16.74 GPa for $Zr_{3}AlC_{2}$, $(Zr_{0.5}Ti_{0.5})_{3}AlC_{2}$ and $Ti_{3}AlC_{2}$, respectively. The hardness of $Zr_{3}AlC_{2}$ is the smallest among of the three compounds, and the hardness of $Ti_{3}AlC_{2}$ is the greatest among of them.

### 3.3. Effect of the pressure on the mechanical properties
We have also studied the effect of the pressure on the mechanical properties of our compounds $(Zr_{1-x}Ti_{x})_{3}AlC_{2}$ (where x=1, 0.5 and 1). The Fig. 3 show change of the elastic constants under different pressures from 0 to 25 GPa. We can see that the elastic constants of our compounds increase when the pressure increase, but despite that, the mechanical stability condition is kept fulfilled. The Fig. 4 shows the change of elastic modulus under different pressures from 0 to 25 GPa. We can notice that all the bulk modulus B, shear modulus G and Young's modulus E increase almost linearly when the pressure increases. That means these compounds maintain their mechanical stability under pressures up to 25GPa.

### 3.4. Electronic properties

The calculation of the electronic properties of a material is extremely important, as it informs us about the electronic conductivity, the nature of the connections that are formed between the different elements of this material, and these properties include band structures, state density and charge densities. In the Fig. 5, we illustrate the band structures for $Zr_3AlC_2$, $(Zr_{0.5}Ti_{0.5})_3AlC_2$ and $Ti_3AlC_2$ compounds along the high-symmetry axes of the first Brillouin zone. We can note from this figure that the three band structure are topologically identical and we can easily observe the overlap between the valence and conduction bands at the Fermi level of all these diagrams. Consequently, no band gap is found at the Fermi level and as a result all these compounds show metallic nature. We can also observe a great dispersion at both the valence and conduction bands. In order to further understanding the nature of the calculated band structures, we have also calculate the total density of states (TDOS) and partial density of states (PDOS) for the studied compounds in a wide energy interval [-6 eV , 6 eV] symmetric around the Fermi level . We illustrate in Figs. 6 (a, b and c) the TDOS and PDOS of $Zr_3AlC_2$, $(Zr_{0.5}Ti_{0.5})_3AlC_2$ and $Ti_3AlC_2$, respectively. The Fermi level is taken as the origin of the energies. The TDOS results confirm the metallic nature for our compounds. We can divide the valence region into two parts: the first part where the valence band between -5.0 eV to -1.5 eV and the second part where the valence band between -1.5 eV to 0.0 eV. The first part is mostly dominated by the p-d of the transition element (Zr and Ti), $s$-Al and $p$-C for the three investigated compounds. The second part present a strong $p$-$d$ hybridization between the $d$ orbital of transition metal elements (Ti and Zr) and $p$ orbital of Al. While, the conduction band are originated mainly to the $d$-Zr contributions with a minor contribution of s-p states of Al and p states of C. The presence of p-d and s-p hybridization reveal that the chemical bonding are mixed ionic-covalent for our compounds, which confirm the result obtained from mechanical properties. The hybridization $p$-$d$ contribute to forming the metallicity of our compounds. It is important to emphasize that, to our knowledge; there are no experimental or theoretical results about the electronic properties for these compounds.

### 3.5. Thermodynamic properties

In solid states physics, the Debye temperature $\theta_D$ and the sound $v$ velocity play a very important role to study the thermodynamic properties. The determination of both values is calculated as follows [64, 65]:

$$
\theta_{D}=\frac{h}{k_{B}}\left[\left(\frac{3 n}{4 \pi}\right) \frac{N_{A} \rho}{M}\right]^{\frac{1}{3}} \tag{30}
$$

$$
v_{m}=\left[\frac{1}{3}\left(\frac{2}{v_{t}^{3}}+\frac{1}{v_{l}^{3}}\right)\right]^{-\frac{1}{3}} \tag{31}
$$

$$
v_{l}=\left(\frac{3 B+4 G}{3 \rho}\right)^{\frac{1}{2}} \tag{32}
$$

$$
v_{t}=\left(\frac{G}{\rho}\right)^{\frac{1}{2}} \tag{33}
$$

where $h$ is Plank's constant, $k_{B}$ is Boltzmann's constant, n is the number of atoms per formula unit, $N_{A}$ is Avogadro's number, $\rho$ is the density, $M$ is the molecular weight, $v_{m}$ is the average sound velocity, $v_{l}$ and $v_{t}$ are the longitudinal and transverse sound velocities, respectively. The values of $\rho$, $v_{t}$, $v_{l}$, $v_{m}$ and $\theta_{D}$ are shown in the Table. 4. We can note the values of density $\rho$ of $(Zr_{1-x}Ti_x)_3AlC_2$ are decrease when x increase where x=0, 0.5and 1. All the values of $v_{l}$, $v_{t}$ and $v_{m}$ and $\theta_{D}$ are increase with x. To the best of our knowledge, there is no experimental report in the literature about these quantities for our compounds up to now.

We have also evaluated the Debye temperature, bulk modulus and heat capacity under temperatures from 0 to 600 K and the pressure from 0 to 30 GPa by employing the quasi-harmonic Debye model as implemented in the Gibbs code [66], which is based on the estimation of the Debye temperature by using the following formulas [67]:

$$
\theta_{D}=\frac{\hbar}{K_{B}}\left[6 \pi^{2} V^{\frac{1}{2}} r\right]^{\frac{1}{3}} f(v) \sqrt{\frac{B_{s}}{M}}(34)
$$

Where V is the molecular volume, M the molecular mass of the compound, $k_{B}$ is the Boltzman constant and f (v) the scaling function [68, 69], that depends on the Poisson's ratio v of the isotropic material [70]:

$$
f(v)=\left\{3\left[2\left(\frac{2}{3} \frac{1+v}{1-2 v}\right)^{\frac{3}{2}}+\left(\frac{1}{3} \frac{1+v}{1-v}\right)^{\frac{3}{2}}\right]^{-1}\right\}^{\frac{1}{3}}(35)
$$

$B_s$ the adiabatic bulk modulus given by the static compressibility:

$$
B_{s} \cong B_{static}=V\left(\frac{d^{2} E(V)}{d V^{2}}\right)(36)
$$

Where E (V) is the total energy per unit cell for our compounds, determined from the ground-state calculation established in section 3.1. The heat capacity is given by:

$$
C_{V}=3 n k_{B}\left(4 D\left(\frac{\theta_{D}}{T}\right)-\frac{\frac{3 \theta_{D}}{T}}{e^{\frac{\theta_{D}}{T}}-1}\right)(40)
$$

Where $D\left(\frac{\theta_{D}}{T}\right)$ denote the Debye integral and n is the number of atoms per unit cell.

The calculated Bulk modulus and the Debye temperature of $Zr_{3} AlC_{2},(Zr_{0.5} Ti_{0.5})_{3} AlC_{2}$ and $Ti_{3} AlC_{2}$ are displayed in Figs. 7 and 8 (a, b and c), respectively. From these Figures, we can

observe that the values of bulk modulus B and Debye temperature $\theta_{D}$ decrease slowly when the temperature increase under constant pressure, but they increase rapidly when the pressure increase under constant temperature for all our compounds. We point out that Debye temperature $\theta_{D}$ and Bulk modulus change similarly for all our compounds.

The heat capacity $C_{p}$ and $C_{v}$ are also investigated under the pressure and temperature changes. The Figs. 9 and 10 (a, b and c) show the variation of the heat capacity $C_{p}$ and $C_{v}$ of $Zr_{3}AlC_{2}$ $(Zr_{0.5}Ti_{0.5})_{3}AlC_{2}$ and $Ti_{3}AlC_{2}$ as a function of temperature and pressure, respectively. We can note from these figures that the $C_{p}$ and $C_{v}$ values for all our compounds increase rapidly with increasing temperature when the temperature is inferior than 200K and continue to increase weakly as the temperature rises. The values of $C_{p}$ and $C_{v}$ decrease slowly when the pressure increases under a constant temperature for all of our compounds except when the temperature equals zero where all the values of $C_{p}$ and $C_{v}$ remain zero.

## 4. Conclusion

In summary, we have presented a report on the structural, electronic, mechanical and the thermodynamic properties of the MAX phases (Zr1-xTix)3AlC2 compounds by means of the ab-initio plane-wave (FP-LAPW) method. The equilibrium properties were calculated and compared with others work. The lattice constants a and c as function of pressure were evaluated. We found that, the compression along the (a,c)-axis decreases with linear dependence when the pressure increase. The results of the formation energy show that, the examined compounds are quite stable even at high temperatures. The obtained independent elastic constants confirm the stability of the $(Zr_{1-x}Ti_{x})_{3}AlC_{2}$ compounds against any elastic deformation. The bulk modulus, shear modulus, Young's modulus E, Poisson's ratio, Cauchy pressure and Vickers hardness are calculated. The chemical bonding between the nearest neighbor atoms which is dominant is the ionic for $Zr_{3}AlC_{2}$, mixed ionic-covalent for $(Zr_{0.5}Ti_{0.5})_{3}AlC_{2}$ and covalent for $Ti_{3}AlC_{2}$. Also, all these compounds present a brittle nature and anisotropy behavior. The Hardness calculation show that, the $Ti_{3}AlC_{2}$ is harder than $(Zr_{0.5}Ti_{0.5})_{3}AlC_{2}$ and $Zr_{3}AlC_{2}$ compounds. Sine all the electronic structure haven't band gap at Fermi level so the studied compounds show a metallic behavior. The TDOS and PDOS curves reveal the existence of $p$-$d$ and $s$-$p$ hybridization. Finally, by the

quasi-harmonic Debye model we have calculated the variation of the bulk modulus, Debye temperature and heat capacity as function of temperature and pressure. The bulk modulus and the Debye temperature in each compound increase significantly with increasing pressure and decrease slowly with increasing temperature. Conversely, the heat capacity increases with increasing temperature and slightly decreasing with increasing temperature.

REFERENCES:

[1] M.W. Barsoum, M. Radovic. Annu Rev Mater Res 41 (2011) 195- 227.

[2] W. Jeitschko, H. Nowotny, F. Benesovsky, Monatsh. Chem 94 (1963) 1201.

[3] H. Nowotny, Prog. Solid State Chem 2 (1970) 27.

[4] M.W. Barsoum, L. Farber, I. Levin, A. Procopio, T. El-Raghy, A. Berner. American Ceramic Society 82 (1999) 2545-2547.

[5] C. Hu, F. Li, J. Zhang, J. Wang, J. Wang, Y. Zhou. Scripta Materialia 57 (2007) 893- 896.

[6] M.W. Barsoum, T. El-Raghy. American Scientist 89 (2001) 334-343.

[7] H. Yoo, M.W. Barsoum, T.El-Raghy. Nature 407 (2000) 581.

[8] T. Lapauw, J. Halimc, J. Lu, T. Cabioc'h, L. Hultman, M.W. Barsoum, K. Lambrinou and J. Vleugels, Euro. Ceram. Soc 36 (2016) 943.

[9] E. Zapata-Solvas, S-R.G. Christopoulos, N. Ni, D.C. Parfitt, D. Horlait, M. E. Fitzpatrick, A. Chroneos, W. E. Lee, J. Am Ceram Soc 100 (2017) 1377.

[10] T. El-Raghy, M.W. Barsoum, A. Zavaliangos, S.R. Kolidindi, J. Am. Ceram. Soc. 82 (1999) 2855.

[11] M.W. Barsoum, L. Farber, T. El-Raghy, Metall. Mater. Trans. A 30 (1999) 1727

[12] D. Tallman, Acta Mater. 85 (2014) 132.

[13] Gokhan Surucua,b,c and Aytac Erkisi, Materials Research Express, Volume 4 (2017) 106520.

[14] Gokhan Surucu, Aysenur Gencer, Xiaotian Wang, Ozge Surucu, Journal of Alloys and Compounds 819 (2020) 153256.

[15] Aysenur Gencera and Gokhan Surucu, Materials Research Express 5 (2018) 076303.

[16] GOKHAN SURUCU, KEMAL COLAKOGLU, ENGIN DELIGOZ and NURETTIN KOROZLU, Journal of Electronic Materials 45 (2016) 4256-4264.

[17] Gokhan Surucu, Aytac Erkisi, BORON 3 (2018) 24 – 32.

[18] Gokhan Surucu, Materials Chemistry and Physics 203 (2018) 106-117

[19] M.A. Hadi, Y. Panayiotatos, A. Chroneos, Journal of Materials Science: Materials in Electronics 28 (2016) 3386-3393.

[20] M.A. Hadi, M. Roknuzzaman, A. Chroneos, S. H. Naqib, A.K.M.A. Islam, R.V. Vovk, K. Ostrikov, Comput. Mater. Sci 137 (2017) 318.

[21] P. Hohenberg, W. Kohn, Phys. Rev. B 136 (1964) 864.

[22] W. Kohn, L.S. Sham, Phys. Rev. A 140 (1965) 113.

[23] J.C. Slater, Adv. Quantum Chem. 1 (1994) 5564.

[24] Blaha P., Schwarz K., Madsen G.K.H., Kvasnicka D. and J. Luitz, WIEN2K, an Augmented Plane Wave +Local orbitals program for calculating crystal properties, ISBN 3-9501031-1-2, (2001).

[25] S. Aouimer, M. Ameri, D. Bensaid, N.E. Moulay, A.Z. Bouyakoub, F.Z. Boufadi, I. Ameri and Y. Al-Douri, ACTA PHYSICA POLONICA A 136 N°1 (2019) 127-134.

[26] A. Bouhemadou, D. Allali, K. Boudiaf, B. Al Qarni, S. Bin-Omran, R. Khenata, Y. Al Douri, Journal of Alloys and Compounds 774 (2019) 299-314.

[27] Friha Khelfaoui, Mohammed Ameri, Djillali Bensaid, Ibrahim Ameri and Yarub Al-Douri, Journal of Superconductivity and Novel Magnetism 31 (2018) 3183–3192.

[28] M.H. Benkabou, M. Harmel, A. Haddou, A. Yakoubi, N. Baki, R. Ahmed, Y. Al-Douri, S.V. Syrotyuk, H. Khachai, R. Khenata, C.H. Voon, Mohd Rafie Johan, Chinese Journal of Physics 56 (2018) 131–144.

[29] Z. Souadia, A. Bouhemadou, O. Boudrifa, S. Bin-Omran, R. Khenata & Y. Al Douri, High Pressure Research 37, Issue 4 (2017) 558-578.

[30] Kada Bidai, Mohammed Ameri, Slamani Amel, Ibrahim Ameri, Y. Al-Douri, Dinesh Varshney, C.H. Voon, Chinese Journal of Physics 55, Issue 5 (2017) 2144-2155.

[31] K. BIDAI, M. AMERI, I. AMERI, D. BENSAID, A. SLAMANI, A. ZAOUI, Y. AL- DOURI, Arch. Metall. Mater. 62, N° 2 (2017) 865-871.

[32] Nadjia Tayebi, Kada Bidai, Mohammed Ameri, Slamani Amel, Ibrahim Ameri, Y. Al- Douri, Dinesh Varshney, Chinese Journal of Physics 55 (2017) 769-779.

[33] A. Bennadji, M. Ameri, D. Hachemane, Y. Al-Douri, I. Ameri, D. Varshney, C.H. Voon, Chinese Journal of Physics 55 (2017) 386-399.

[34] Kada Bidai, Mohammed Ameri, Ali Zaoui, Ibrahim Ameri, Yarub Al-Douri, Chinese Journal of Physics 54 (2016) 678-694.

[35] Mohammed Ameri, Faiza Bennar, Slamani Amel, Ibrahim Ameri, Y. Al-Douri & Dinesh Varshney, Phase Transitions 89 (2016) 1236-1252.

[36] Samir Mustapha Laoufi, Amina Touia, Mohammed Ameri, Ibrahim Ameri, Fatima Boufadi, Keltouma Boudia, Amel Slamani, Fadila Belkharroubi and Y. Al-Douri, Optik 127 (2016) 7382-7393.

[37] A. Benkabou, H. Bouafia, B. Sahli, B. Abidri, M. Ameri, S. Hiadsi, D. Rached, B. Bouhafs, N. Benkhettou and Y. Al-Douri, Chinese Journal of Physics 54 (2016) 33-41.

[38] Kada Bidai, Mohammed Ameri, Djillali Bensaid, Slamani Amel, Ibrahim Ameri and Y. Al- Douri, Optik 127 (2016) 5155-5162.

[39] Nadhira Bioud, Optik 127 (2016) 4559-4573.

[40] S. Daho, M. Ameri, Y. Al Douri, D. Bensaid, D. Varshney, I. Ameri, Materials Science in Semiconductor Processing 41 (2016) 102-108

[41] A. Reggad, R. Lardjani, R. Baghdad, B. Bouhafs, Physica B 526 (2017) 89-95.

[42] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[43] S. Berri, D. Maouche, F. Zerarga, Y. Medkour. Physica B 407 (2012) 3328-3334.

[44] M. Pietzka, J. Schuster, J. Phase Equilib. 15 (1994) 392.

[45] 2Doptimize package is provided by M. Jamal as part of the commercial code WIEN2K, http://www.wien2k.at/

[46] Gokhan Surucu, Cagil Kaderoglu, Engin Deligoz, Haci Ozisik, Materials Chemistry and Physics 189 (2017) 90-95.

[47] A.H. Reshak, Moreteza Jamal, Int. J. Electrochem. Sci. 8 (2013) 12252-12263.

[48] E. Zapata, M.A. Hadi, D. Horlait, D.C. Parfitt, A. Thibaud, A. Chroneos, W.E. Lee, Journal of the American Ceramic Society, 100(2017) 3393-3401.

[49] H. Rached, D. Rached, S. Benalia, A.H. Reshak, M. Rabah, R. Khenata, S. Bin Omran, Materials Chemistry and Physics 143 (2013) 93-108.

[50] J. Wang, J. Wang, Y Zhou, C. Hu, Acta Materialia 56 (2008) 1511-1518.

[51] R. Hill, Proc, Phys. Soc. A 65 (1952) 349-354.

[52] W. Voigt, Leipzig: Teubner (1928) 95-100.

[53] A. Reuss, Z. Angew. Math. Mech. 9 (1929) 49-58.

[54] X. TaO, J. Yang, L. Xi, Y. Ouyang, J. Solid State Chem, 194 (2012) 179-187.

[55] Y. Tu, Y. Wang, Solid State Communications. 151 (2011) 238-241.

[56] A. Yildirim, H. Koc, E. Deligoz. Chin. Phys B 21 (2012) 037101.

[57] M. Jamal, N. Kamali Sarvestani, A. Yazdani, A. H. Reshak, RSC Adv.4 (2014)57903-57915.

[58] G. Vaitheeswaran, V. Kanchana, A. Svane, A. Delin, J. Phys: Conden. Matter 19 (2007) 326214.

[59] S. F. Pugh, Phil. Mag. 45 (1954) 823.

[60] H. M. Ledbetter, J. Phys. Chem. 6 (1977) 1181.

[61] Z.E. Biskri, H. Rached, M. Bouchear, D. Rached, J. Mech, Behav. Biomed. Mater 32 (2014) 345-350.

[62] A.L. Ding, C. M. Li, J. Wang, J. Ao, Z-Q. Chen. Chin. Phys B 23 (2014) 096201.

[63] X.Q. Chen, H. Niu, D. Li, Y. Li, Intermetallics 19 (2011)1275-1281.

[64] M.H. Elahmar, H. Rached, D. Rached, R. Khenata, G. Murtaza, S. Bin Omran, W.K. Ahmed, Journal of Magnetism and Magnetic Materials 393 (2015) 165-174.

[65] M. Benkabou, H. Rached, A. Abdellaoui, D. Rached, R. Khenata, M.H. Elahmar, B. Abidri, N. Benkhettou, S. Bin-Omran, Journal of Alloys and Compounds 647, (2015), 276-286.

[66] M.A. Blanco, E. Francisco, V. Luaña, Comput. Phys. Commun. 158 (2004) 57.

[67] A.G. McLellan; The Classical Thermodynamics of Deformable Materials 165, Cambridge University Press, Cambridge (1980).

[68] E. Francisco, J.M. Recio, M.A. Blanco, A. Martín Pendás, J. Phys. Chem. 102 (1998) 1595.

[69] E. Francisco, G. Sanjurjo, M.A. Blanco, Phys. Rev. B 63 (2001) 094107.

[70] J.P. Poirier, Introduction to the Physics of the Earth's Interior, Cambridge University Press (1991).

## Figure Captions

Fig. 1: A view of the crystal structure of the MAX Phase $Zr_3AlC_2$ compound.

Fig. 2: The Lattice parameters a and c as function of pressure.

Fig. 3: Variation of the elastic constants Cij under different pressures from 0 to 25 GPa

Fig. 4: Variation of the Bulk modulus B, shear modulus G and Young's modulus E under different pressures from 0 to 25 GPa.

Fig. 5: The band structures for $Zr_3AlC_2$, $(Zr_{0.5}Ti_{0.5})_3AlC_2$ and $Ti_3AlC_2$ compounds along the high-symmetry axes of the first Brillouin zone.

Fig. 6. a: The Total and Partial density of states (TDOS, PDOS) of $Zr_3AlC_2$ compound.

Fig. 6. b: The Total and Partial density of states (TDOS, PDOS) of $(Zr_{0.5}Ti_{0.5})_3AlC_2$ compound.

Fig. 6. c: The Total and Partial density of states (TDOS, PDOS) of $Ti_3AlC_2$ compound.

Fig. 7.a: The Bulk modulus of $Zr_3AlC_2$ compound as a function of temperature and pressure.

Fig. 7.b: The Bulk modulus of $(Zr_{0.5}Ti_{0.5})_3AlC_2$ compound as a function of temperature and pressure.

Fig. 7.c: The Bulk modulus of $Ti_3AlC_2$ compound as a function of temperature and pressure.

Fig. 8.a: The Debye temperature of $Zr_3AlC_2$ compound as a function of temperature and pressure.

Fig. 8.b: The Debye temperature of $(Zr_{0.5}Ti_{0.5})_3AlC_2$ compound as a function of temperature and pressure.

Fig. 8.c: The Debye temperature of $Ti_3AlC_2$ compound as a function of temperature and pressure.

Fig. 9.a: The Heat capacity Cp of $Zr_3AlC_2$ compound as a function of temperature and pressure.

Fig. 9.b: The Heat capacity Cp of $(Zr_{0.5}Ti_{0.5})_3AlC_2$ compound as a function of temperature and pressure.

Fig. 9.c: The Heat capacity Cp of $Ti_3AlC_2$ compound as a function of temperature and pressure.

Fig. 10.a: The Heat capacity Cv of $Zr_3AlC_2$ compound as a function of temperature and pressure.

Fig. 10.b: The Heat capacity Cv of $(Zr_{0.5}Ti_{0.5})_3AlC_2$ compound as a function of temperature and pressure.

Fig. 10.c: The Heat capacity Cv of $Ti_3AlC_2$ compound as a function of temperature and pressure.

Tables

<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Atom</th>
      <th>Site</th>
      <th>Coordinates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">M₃AlC₂<br>M= Zr , Ti<br>P6₃/mmc<br>(#194)</td>
      <td rowspan="2">M</td>
      <td>2a</td>
      <td>(0,0,0) $(0,0,\frac{1}{2})$</td>
    </tr>
    <tr>
      <td>4f</td>
      <td>$(\frac{1}{3},\frac{2}{3}, z_M)$ $(\frac{2}{3},\frac{1}{3}, z_M+\frac{1}{2})$ $(\frac{2}{3},\frac{1}{3},-z_M)$ $(\frac{1}{3},\frac{2}{3}, -z_M+\frac{1}{2})$</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>2b</td>
      <td>$(0,0,\frac{1}{4})$ $(0,0,\frac{3}{4})$</td>
    </tr>
    <tr>
      <td>C</td>
      <td>4f</td>
      <td>$(\frac{1}{3},\frac{2}{3}, z_C)$ $(\frac{2}{3},\frac{1}{3}, z_C+\frac{1}{2})$ $(\frac{2}{3},\frac{1}{3},-z_C)$ $(\frac{1}{3},\frac{2}{3}, -z_C+\frac{1}{2})$</td>
    </tr>
  </tbody>
</table>

Table.1.The Wyckoff positions for Zr₃AlC₂ compounds.

<table>
  <thead>
    <tr>
      <th>Compounds</th>
      <th>a (Å)</th>
      <th>c (Å)</th>
      <th>c/a</th>
      <th>$V\left(\mathring{A}^3\right)$</th>
      <th>$\Delta H_f$ (eV/f.u.)</th>
      <th>Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Zr₃AlC₂</td>
      <td>3.341</td>
      <td>19.960</td>
      <td>5.974</td>
      <td>193.02</td>
      <td rowspan="3">-0.8176</td>
      <td>Calcᵃ</td>
    </tr>
    <tr>
      <td>3.333</td>
      <td>19.951</td>
      <td>5.986</td>
      <td>191.95</td>
      <td>Exptᵇ</td>
    </tr>
    <tr>
      <td>3.335</td>
      <td>19.961</td>
      <td>5.985</td>
      <td>192.27</td>
      <td>Calcᶜ</td>
    </tr>
    <tr>
      <td rowspan="3">(Zr₀.₅Ti₀.₅)₃AlC₂</td>
      <td>3.230</td>
      <td>19.366</td>
      <td>5.995</td>
      <td>175.02</td>
      <td rowspan="3">-0.7765</td>
      <td>Calcᵃ</td>
    </tr>
    <tr>
      <td>3.232</td>
      <td>19.397</td>
      <td>6.002</td>
      <td>175.45</td>
      <td>Exptᵈ</td>
    </tr>
    <tr>
      <td>3.197</td>
      <td>19.220</td>
      <td>6.012</td>
      <td>170.11</td>
      <td>Calcᶜ</td>
    </tr>
    <tr>
      <td rowspan="3">Ti₃AlC₂</td>
      <td>3.077</td>
      <td>18.638</td>
      <td>6.057</td>
      <td>152.78</td>
      <td rowspan="3">-0.8262</td>
      <td>Calcᵃ</td>
    </tr>
    <tr>
      <td>3.075</td>
      <td>18.578</td>
      <td>6.042</td>
      <td>152.16</td>
      <td>Exptᵉ</td>
    </tr>
    <tr>
      <td>3.078</td>
      <td>18.670</td>
      <td>6.065</td>
      <td>153.19</td>
      <td>Calcᶜ</td>
    </tr>
  </tbody>
</table>

ᵃPresent work. ᵇRef [8]. ᶜRef [19]. ᵈRef [48]. ᵉRef [44].

Table. 2. The calculated lattice parameters, Hexagonal ration c/a and unit cell volume of Zr₃AlC₂, (Zr₀.₅Ti₀.₅)₃AlC₂ and Ti₃AlC₂.

<table>
<thead>
<tr>
<th>Compound</th>
<th>Zr₃AlC₂</th>
<th>(Zr₀.₅Ti₀.₅)₃AlC₂</th>
<th>Ti₃AlC₂</th>
</tr>
</thead>
<tbody>
<tr>
<td>C₁₁ (GPa)</td>
<td>308.59</td>
<td>313.41</td>
<td>358.86</td>
</tr>
<tr>
<td>C₁₂ (GPa)</td>
<td>89.33</td>
<td>90.86</td>
<td>99.95</td>
</tr>
<tr>
<td>C₁₃ (GPa)</td>
<td>97.37</td>
<td>97.20</td>
<td>92.33</td>
</tr>
<tr>
<td>C₃₃ (GPa)</td>
<td>318.24</td>
<td>331.38</td>
<td>366.22</td>
</tr>
<tr>
<td>C₄₄ (GPa)</td>
<td>82.27</td>
<td>89.09</td>
<td>102.19</td>
</tr>
<tr>
<td>C₆₆ (GPa)</td>
<td>109.63</td>
<td>111.28</td>
<td>129.45</td>
</tr>
<tr>
<td>B (GPa)</td>
<td>167.01</td>
<td>169.76</td>
<td>183.68</td>
</tr>
<tr>
<td>G (GPa)</td>
<td>97.33</td>
<td>102.11</td>
<td>119.10</td>
</tr>
<tr>
<td>E (GPa)</td>
<td>244.50</td>
<td>255.16</td>
<td>293.80</td>
</tr>
<tr>
<td>B/G</td>
<td>1.72</td>
<td>1.66</td>
<td>1.54</td>
</tr>
<tr>
<td>ν</td>
<td>0.255</td>
<td>0.249</td>
<td>0.233</td>
</tr>
<tr>
<td>p<sub>x</sub><sup>cauchy</sup></td>
<td>15.1</td>
<td>8.1</td>
<td>−9.86</td>
</tr>
<tr>
<td>p<sub>y</sub><sup>cauchy</sup></td>
<td>−20.30</td>
<td>−20.42</td>
<td>−29.5</td>
</tr>
<tr>
<td>A₁</td>
<td>1.30</td>
<td>1.27</td>
<td>1.24</td>
</tr>
<tr>
<td>A₂</td>
<td>0.75</td>
<td>0.80</td>
<td>0.79</td>
</tr>
<tr>
<td>A₃</td>
<td>0.98</td>
<td>1.01</td>
<td>1.06</td>
</tr>
<tr>
<td>H<sub>V</sub> (Gpa)</td>
<td>12.48</td>
<td>13.52</td>
<td>16.74</td>
</tr>
</tbody>
</table>

Table. 3. Calculated elastic constants C<sub>ij</sub> (GPa), elastic modulus (B , G and E) (GPa),
Poisson's ratio ν, B/G ratio, shear anisotropic factor for the three different shear planes (A₁, A₂
and A₃ ), Cauchy pressure and Vickers hardness H<sub>V</sub> (GPa) for Zr₃AlC₂ , (Zr₀.₅Ti₀.₅)₃AlC₂ and
Ti₃AlC₂ compounds.

<table>
<thead>
<tr>
<th>Composition</th>
<th>$\rho$</th>
<th>$v_l$</th>
<th>$v_t$</th>
<th>$v_m$</th>
<th>$\theta_D$</th>
<th>Remark</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zr₃AlC₂</td>
<td>5.59</td>
<td>7.29</td>
<td>4.17</td>
<td>4.64</td>
<td>546.8</td>
<td>Calcᵃ</td>
</tr>
<tr>
<td></td>
<td>5.61</td>
<td>12.74</td>
<td>4.57</td>
<td>5.19</td>
<td>613</td>
<td>Calcᵇ</td>
</tr>
<tr>
<td>(Zr₀.₅Ti₀.₅)₃AlC₂</td>
<td>4.93</td>
<td>7.88</td>
<td>4.55</td>
<td>5.05</td>
<td>615.8</td>
<td>Calcᵃ</td>
</tr>
<tr>
<td></td>
<td>5.07</td>
<td>14.16</td>
<td>5.14</td>
<td>5.83</td>
<td>718</td>
<td>Calcᵇ</td>
</tr>
<tr>
<td>Ti₃AlC₂</td>
<td>4.22</td>
<td>9.01</td>
<td>5.31</td>
<td>5.89</td>
<td>749.9</td>
<td>Calcᵃ</td>
</tr>
<tr>
<td></td>
<td>4.22</td>
<td>15.48</td>
<td>5.64</td>
<td>6.40</td>
<td>815</td>
<td>Calcᵇ</td>
</tr>
</tbody>
</table>

$^{\text{a}}$Present work. $^{\text{b}}$Ref. [20].

Table. 4. Density ($\rho$ in (g/cm³)), longitudinal, transverse and average sound velocity $v_l$, $v_t$ and $v_m$ in (Km/s) as well as Debye temperature $\theta_D$ in (K) for Zr₃AlC₂, (Zr₀.₅Ti₀.₅)₃AlC₂ and Ti₃AlC₂ compounds.

![](./images/812651365267406849_2.jpg)

![](./images/812651365267406849_3.jpg)

![](./images/812651365267406849_4.jpg)

![](./images/812651365267406849_5.jpg)

![](./images/812651365267406849_6.jpg)

![](./images/812651365267406849_7.jpg)

![](./images/812651365267406849_8.jpg)

![](./images/812651365267406849_9.jpg)

![](./images/812651365267406849_10.jpg)

![](./images/812651365267406849_11.jpg)

![](./images/812651365267406849_12.jpg)

![](./images/812651365267406849_13.jpg)

![](./images/812651365267406849_14.jpg)

![](./images/812651365267406849_15.jpg)

![](./images/812651365267406849_16.jpg)

![](./images/812651365267406849_17.jpg)

![](./images/812651365267406849_18.jpg)

![](./images/812651365267406849_19.jpg)

![](./images/812651365267406849_20.jpg)

![](./images/812651365267406849_21.jpg)

### Highlights

- Based on the first-principle calculation, the MAX-phase $(Zr_{1-x}Ti_x)_3AlC_2$ compounds have been investigated.

- The elastic constants reveals that these alloys are stable against any elastic deformations.

- The mechanical and electronic properties are investigated and discussed in details.

- The thermodynamic properties are predicted.

### Declaration of interests

☒ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

☐The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

<table>
  <tr>
    <td></td>
  </tr>
</table>