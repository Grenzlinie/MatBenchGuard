# Strain induced anisotropic mechanical and electronic properties of 2D-SiC

Manju M.S. $^{\text{a}}$, Ajith K.M. $^{*, \text{a}}$, M.C. Valsakumar$^{\text{b}}$

$^{\text{a}}$ Computational Physics Laboratory, Department of Physics, National Institute of Technology Karnataka (NITK), Surathkal, Mangaluru 575025, India
$^{\text{b}}$ Department of Physics, Indian Institute of Technology (IIT), Ahalia Campus, Kozhipara, Palghat 678557, India

---

## ARTICLE INFO

**Keywords:**
2D-SiC
Density functional theory
Mechanical properties
Non-linear elastic constants
Electronic properties
Ionic nature

## ABSTRACT

A silicene derivative of the form SiC was thoroughly investigated on its behaviour with changes in stress varying from around 140 N/m to around 20 N/m and strain from $-0.2$ to 0.3. Uniaxial stress (both zigzag and armchair) brought structural changes which reduced the symmetry of the system but biaxial stress brought no change in symmetry and shape of the material. Mechanical stability of the system was maintained upto a considerable stress in both uni- and biaxial cases and the system showed anisotropic behaviour with stress variations. Electronic structural variations showed strain engineering is a convenient method to tune the band gap very effectively causing semiconducting SiC to transform to metallic one at large stresses and direct to indirect bandgap in the semiconducting phase at lower stress. Charge density analysis showed a significant ionic nature of the material in the semiconducting phase.

---

## 1. Introduction

The past two decades have seen tremendous advancements in the prediction and synthesis of two dimensional materials having novel electronic, chemical, mechanical, optical and magnetic properties and their potential applications in various fields including mechanical engineering, electronics, information and energy technologies (Zhang et al., 2016). Graphene was the first of this kind which was extensively investigated theoretically prior to its experimental synthesis and its synthesis in 2004 opened a pathway for micro and nano device fabrications (Novoselov et al., 2004; Sahin and Peeters, 2013). Discovery of these two dimensional materials and their numerous applications have aroused interest in exploring new materials on the horizon of condensed matter physics and materials science (Lin and Ni, 2012; Wang et al., 2014). The advancement in practical synthesis of these materials will pave a way to the nanoelectronics. This generated interest in probing one and few atom thick materials for various practical applications. Most of the two dimensional materials tend to be anisotropic in nature. Anisotropic materials show different behaviour along different directions which could prove possibilities to design novel materials for sensors with anisotropic crystalline directions, electrical conductance, optical absorption and scattering etc. (Lang et al., 2016). Silicene, which was a monoatomic layer of silicon was another extensively explored candidate due to its potential application in silicon electronics (Kara et al., 2012).

Silicene is a monoatomic sheet with hexagonally arranged silicon atoms analogous to graphene buckled with sub-lattice displacement of 0.46 Å (Roman and Cranford, 2014; Kaloni and Schwingenschlögl, 2014). Graphene and silicene has zero band gap which reduces their functionality in electronic and optoelectronic applications which requires a sizeable and well defined band gap. Band gap in these materials can be tuned by introducing vacancies or by introducing foreign atoms or by applying external force or fields or by confining to 1D nanoribbons or by coupling with various other sheets (Kunstmann et al., 2017; Zhang et al., 2015; Tang et al., 2014; Ukpong, 2015). Graphene and also silicene were incorporated with various elements to verify if it could improve the properties of bare graphene and silicene (Ding and Wang, 2013). Among the various derivatives of silicene, SiC was found to be a promising candidate because of it's high mechanical strength, carrier mobility, thermal stability and thermal conductivity (Şahin et al., 2009).

SiC is a planar sheet akin to graphene with a lattice constant of 3.10 Å and Si−C bond length of 1.79 Å (Ding and Wang, 2013). SiC is a direct band gap semiconductor making it a futuristic material for electronic and optoelectronic applications (Shi et al., 2015). It is also assumed to play a major role as metal-free catalyst due to it's higher chemical reactivity towards foreign adsorbates (Wang et al., 2016). Kuzubov et al. (2013) claimed that they have been able to grow a monolayer of SiC on Mg(0001) and MgO(111) substrates, among which Mg tends to be the superior substrate over MgO, for growing 2D SiC. Chabi et al. (2016) also claimed that 2D SiC nanosheet was produced by carbothermal reaction and post sonication process. SiC nanowires and nanoribbons were also extensively studied and they were found to be a potential candidate for hydrogen storage, nanodevices and

---

*Corresponding author.
E-mail address: ajith@nitk.ac.in (A. K.M.).

https://doi.org/10.1016/j.mechmat.2018.02.005
Received 6 October 2017; Received in revised form 31 January 2018; Accepted 27 February 2018
Available online 07 March 2018
0167-6636/ © 2018 Elsevier Ltd. All rights reserved.

microelectrochemical systems (Gori et al., 2012; Bekaroglu et al., 2010). It is crucial to look into the stress dependent variation in properties of this material before deploying it for various applications.

The elastic constants of a material gives its response to external mechanical perturbation. Mechanical properties are divided into four strain domains based on loading : linear elastic, nonlinear elastic, plastic and fracture. Linear and nonlinear strain domains are reversible i.e., they are brought back to equilibrium after the removal of loads. Plastic and fracture domains are irreversible i.e., increase in strain nucleates and accumulates defects resulting in rupture (Peng et al., 2013b). Previous studies on various two dimensional materials have shown that they possess large non-linear elastic deformation in the tensile regime up to the intrinsic strength of the material and then strain softening until fracture (Peng et al., 2013a; Wang et al., 2010). Higher order elastic constants determine non-linear elastic response, anharmonic properties like phonon-phonon interactions, thermal expansion, Gruneisen parameter etc.

Stress or strain plays an important role in the physical properties of the materials. Application of stress or strain engineering is considered to be an efficient method to deform the material and determine the response of these materials looking into various behavioural changes occurring in the materials (Saxena and Tyson, 2008; Wang et al., 2012). Thorough understanding of the stress dependence of these materials is essential for their practical applications. Deformation brings changes in electronic as well as mechanical behaviours. Band gap tuning is essential for their potential applications in electromechanical devices, tunable photo detectors and lasers (Bhattacharyya and Singh, 2012). So, our efforts in this paper is to induce stress in SiC and understand the variation in properties with respect to variation in stress.

## 2. Computational methodology

Vienna Ab-Initio Simulation Package (VASP) was used to carry out the Density functional theory (DFT) calculations (Kresse and Hafner, 1993; 1994; Kresse and Furthmüller, 1996) which is based on Kohn--Sham density functional theory approach (KS-DFT), to understand the changes in structural, mechanical and electronic properties of SiC. Generalized gradient approximation (GGA) (Perdew et al., 1996) parametrized by Perdew-Burke-Ernzerhof (PBE) was used for the calculation of exchange-correlation potential. The valence electrons were considered explicitly for the calculations and the core electrons are incorporated using projected augmented wave method based pseudo-potential (Blöchl, 1994; Jones and Gunnarsson, 1989). The kinetic energy cutoff was maintained at 900 eV. Gamma-centered kpoint meshes were used to sample the Brillouin zone and it was found that a $20 \times 20 \times 1$ grid is sufficient to ensure convergence of energy and other physical properties. An interlayer spacing of $15\ \mathring{A}$ was found to be sufficient to make interlayer interactions, that arises because of the usage of periodic boundary conditions in VASP, to be negligible so that, for all practical purposes, the calculations being done pertain to a film of SiC. The energy was converged to 0.001 eV/atom between two ionic steps and a convergence of $10^{-8}$ eV was kept for each electronic self-consistency (SC) loop. Lattice parameters of the unitcell were changed corresponding to compression or elongation in both uni and biaxial directions and the stress required to equilibrate the system to a varied unit cell is considered as the applied stress. Stress was applied uniaxially both in zigzag and armchair directions and biaxially and the variation in structural, mechanical and electronic properties were noted for both compressive and tensile regimes. The structure with equilibrium lattice parameter is considered as the undeformed structure here, and the lattice parameters were varied, increased and decreased up to 20% from the undeformed lattice parameter.

![](./images/813051770249936901_1.jpg)

Fig. 1. Unitcell of SiC considered for Uniaxial and Biaxial stress. The cell in the form of a rhombus is used for biaxial stress and the cell in the form of rectangle for uniaxial application. The direction of zigzag and armchair is as marked.

![](./images/813051770249936901_2.jpg)

Fig. 2. Variation in strain energy per atom with strain for zigzag, armchair and biaxial cases. Strains are varied from -0.2 to 0.3 and all the three curves represents anharmonicity and anisotropy present in the material.

<table>
<caption>Table 1
Elastic constants of SiC along with graphene, silicene and bulk $\alpha$-SiC. The values of $C_{11}$ and $C_{12}$ are in terms of N/m in the case of SiC, graphene, silicene and that of bulk $\alpha$-SiC is represented in GPa.</caption>
<thead>
<tr>
<th></th>
<th>SiC*</th>
<th>Graphene**</th>
<th>Silicene†</th>
<th>$\alpha$-SiC‡</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{11}$</td>
<td>179.2</td>
<td>358.1</td>
<td>71.3</td>
<td>397</td>
</tr>
<tr>
<td>$C_{12}$</td>
<td>54.5</td>
<td>60.4</td>
<td>23.2</td>
<td>136</td>
</tr>
</tbody>
</table>

* Present study, ** Shao et al. (2012), † (Ding and Wang, 2013) and ‡ (Malakkal et al., 2017).

## 3. Results and discussions

### 3.1. Structural properties

The structure of SiC is as shown in Fig. 1. It is planar in structure like graphene with Si and C atoms arranged alternatively in a hexagon. A system with hexagonal symmetry can be represented by an orthorhombic non-primitive unitcell which was considered for the application of uniaxial stress and the simulation cell was compressed and elongated along 'a' and 'b' thus obtaining zigzag direction along 'a' and armchair direction along 'b' and for biaxial the original unitcell with two atoms was considered as shown in Fig. 1. If a and b are equal, equal amount of stress is required to impart same amount of deformation along both directions. If a and b are terminated at $90^{\circ}$ (non-primitive unitcell), the amount of stress required to deform would be different leading to different physics.

![](./images/813051770249936901_3.jpg)

![](./images/813051770249936901_4.jpg)

![](./images/813051770249936901_5.jpg)

![](./images/813051770249936901_6.jpg)

![](./images/813051770249936901_7.jpg)

![](./images/813051770249936901_8.jpg)

Fig. 3. The graphs represents the variation in elastic constants, Young's modulus and Poisson's ratio along zigzag, armchair and biaxial directions. The three graphs on the left represents the changes in elastic constants with stress and on the right represents changes in Young's modulus and Poisson's ratio with stress.

Energy per atom of the system in the whole range of stress studied confirms the energetical stability of SiC when it is subjected to uniaxial stress along zigzag and armchair directions as well as under biaxial stress. SiC being planar in structure maintains hexagonal symmetry with a space group of P-6m2. The symmetry of the system is broken to orthorhombic when the stress is applied uniaxially along zigzag and armchair direction leading to different physics but biaxial stress maintains the symmetry of the material. Strain energy is the amount of energy stored in the system under deformation. Lagrangian strains ranging from −0.2 to 0.3 with an increment of 0.02 is considered for all three types of deformations. Strain energy per atom is defined as $E_s = (E_{tot} - E_0)/n$ where $E_{tot}$ is the energy of the strained system, $E_0$ is the energy of the unstrained or undeformed system and n is the total number of atoms present in the unitcell. The variation of strain energy per atom for zigzag, armchair and biaxial stress is plotted in Fig. 2. Variation in strain energy with strain is almost identical for uniaxial zigzag, uniaxial armchair and biaxial stresses but the values of biaxial stress being higher compared to the other two. The curve representing the variation in strain energy per atom with strain implies that the strain energy is asymmetric along compression and tension in all the three cases signifying the anharmonicity and anisotropy present in the system. The stresses are basically the derivatives of strain energies, in the harmonic region they maintain a linear relationship. But, in the anharmonic region stresses are non-linear with respect to strain energies (Peng et al., 2013b).

![](./images/813051770249936901_9.jpg)

Fig. 4. Contour plot of (a) $C_{11}$, (b) $C_{22}$ and (c) $C_{12}$. Strains along X and Y is plotted along X and Y axes respectively. The colour gradation from red to blue implies values in the descending order. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

### 3.2. Mechanical properties

The elastic constants are crucial for the determination of the mechanical properties of materials, providing important information on their mechanical response, stability, stiffness and strength (Wang et al., 2012). Second order elastic constants (SOEC) model the linear elastic response. Anisotropic elastic solids in three dimensions have 21 SOEC which reduces to 5 independent SOEC for a hexagonal structure due to the crystal symmetry (Mouhat and Coudert, 2014). The deformations in 2D material can be solely approximated as an in-plane deformation neglecting all the out of plane components (Cooper et al., 2013). This implies that the in-plane components are non-zero and out of plane deformations are ideally zero. This implies that the number of independent SOEC reduces to three, i.e., $C_{11}$ , $C_{22}$ and $C_{12}$ for the general case, and two, i.e., $C_{11}=C_{22}$ and $C_{12}$ for systems with hexagonal symmetry. The mechanical stability of a two-dimensional sheet is confirmed by Born-Huang stability criteria (Bom and Huang, 1954), according to which a mechanically stable sheet with hexagonal symmetry should satisfy $C_{11}>C_{12}$ and $C_{11}^{2}-C_{11}C_{12}>0$. Young's modulus (E) and Poisson's ratio ($\nu$) are calculated using the following equations

$$
Y_{s}=\frac{C_{11}^{2}-C_{12}^{2}}{C_{11}} \tag{1}
$$

and

$$
\nu=\frac{C_{12}}{C_{11}} \tag{2}
$$

Elastic constants of SiC at ambient conditions are $C_{11}=179.2\,\text{N/m}$ and $C_{12}=54.5\,\text{N/m}$ which matches with the values reported by Ding and Wang (2013) as tabulated in Table 1. Bulk SiC has polytypes and they exist in more than 250 crystalline forms. One of the most studied polymorph is $\alpha$-SiC which is hexagonal in symmetry which is used in the present work for comparison. The Young's modulus and Poisson's ratio of 2D-SiC are $162.7\,\text{N/m}$ and 0.30. SiC is found to be satisfying the above stability criterion thus confirming its mechanical stability. The variation in elastic constants with stress needs to be taken care for its practical applications. Fig. 3 below shows the variation in elastic constants as a function of uniaxial zigzag, uniaxial armchair and biaxial stresses. The values of second order elastic constants are consistent with mechanical stability of the system in general and their values are plotted in Fig. 3. In the case of uniaxial zigzag stress, the magnitudes of $C_{11}$ and $C_{12}$ increase as the compressive stress increases and they maintain the Born stability criteria till around $35\,\text{N/m}$. The system tends to resist the deformation which inturn is reflected in the higher magnitudes of elastic constants. It can be seen that $C_{11}=C_{22}$ only when the stress is equal to zero and as the stress changes this equality is no longer valid because of the presence of anisotropy as could be observed from Fig. 3 in the case of uniaxial stress along zigzag and armchiar directions. $C_{22}$ also increases with increasing compressive stress. Young's modulus increases with increasing compressive stress making the system stiffer. Poisson's ratio also shows an increasing trend along compressive regime. As the stress increases further to around $77\,\text{N/m}$ the mechanical stability is lost as $C_{12}$ becomes greater than $C_{11}$ violating Born criteria. The values of $C_{11}$ and $C_{12}$ tend to decrease as we increase the tensile stresses which corresponds to the less resistance offered by the system to deform itself. $C_{22}$ also follows the same trend.

![](./images/813051770249936901_10.jpg)

Fig. 5. Stress-strain curves of (a) uniaxial zigzag (b) uniaxial armchair (c) biaxial stresses. The ultimate tensile stress in each case is marked in the graph and toughness of the material is also calculated.

<table>
<caption>Table 2 Ultimate Tensile Strength of SiC along with graphene and silicene in units of N/m. $\Sigma^z$ - uniaxial zigzag, $\Sigma^a$ - uniaxial armchair and $\Sigma^b$ biaxial directions.</caption>
<thead>
<tr>
<th></th>
<th>SiC</th>
<th>Graphene</th>
<th>Silicene</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Sigma^z$</td>
<td>20.22</td>
<td>30.4</td>
<td>5.9</td>
</tr>
<tr>
<td>$\Sigma^a$</td>
<td>21.21</td>
<td>28.6</td>
<td>6.0</td>
</tr>
<tr>
<td>$\Sigma^b$</td>
<td>16.05</td>
<td>32.1</td>
<td>6.2</td>
</tr>
</tbody>
</table>

Also, Young's modulus and Poisson's ratio decreases as expected. Similar trend could be observed when uniaxial armchair stress is applied. SiC maintains mechanical stability up to the highest stress of 85 N/m confirming the elastic resistance of the material till this stress in the compressive regime and around 19 N/m in the tensile regime. Young's modulus shows an increasing trend implying that the system on increasing the stress, tries to become stiff and strong.

Similar trend in the case of elastic constants could be observed in the case of equi-biaxial stress also. SiC maintains mechanical stability until around 111 N/m confirming the elastic resistance of the material till this stress in the compressive regime and around 16 N/m in the tensile regime. When the material is further compressed, to around 135 N/m the mechanical stability is lost as $C_{12}$ becomes greater than $C_{11}$. Young's modulus tends to decrease along the compressive regime and tensile regime. The value of $C_{12}$ increases substantially compared to

![](./images/813051770249936901_11.jpg)

Fig. 6. (a) Electronic bands and (b) Dos diagram confirming the semiconducting nature of SiC. The contribution of partial dos is shown in the dos plot.

![](./images/813051770249936901_12.jpg)

Fig. 7. Electronic band and dos plot variations with respect to uniaxial zigzag stress. (a), (b) & (c) represents compressive regime and (d), (e) & (f) represents tensile regime. The band gap values are (a) Metallic, (b) $E_g = 1.98$ eV, (c) $E_g = 2.38$ eV, (d) $E_g = 2.34$ eV and (e) $E_g = 1.48$ eV and (f) $E_g = 0.57$ eV.

$C_{11}$ which inturn reduces the value of Young's modulus in the compressive regime. Poisson's ratio in the case of equi-biaxial stress is irrelevant as this is the phenomenon in which a material tries to expand in a direction perpendicular to the direction of application of stress. In a 2d material this perpendicular direction becomes the z-axis direction which is immaterial in these materials.

To have a complete non-linear behaviour of 2D-SiC, we have done an extensive calculations with unequal biaxial stress which means, strains of different magnitudes were applied in the material simultaneously within a range of $-0.1$ to $0.1$. A grid of increments $0.02$ was considered for both strains along X and strains along Y and elastic constants were calculated at each grid points. The obtained elastic constants were plotted as a contour plot as shown in Fig. 4. The colour gradation in the contour plot of $C_{11}$ and $C_{22}$ clearly signifies that $C_{11}$ and $C_{22}$ are not equal in all ranges of strains indicating an anisotropic behaviour of SiC in all ranges of strains applied.

Stress-strain curve is an important graphical representation of a material's mechanical properties. Stress increases linearly with strain in the harmonic region and Hooke's law is obeyed in this regime. Anisotropic region is the one where stress-strain relationship is no longer valid and the higher order terms become significant. With larger strain, stress will increase enormously and ultimately the system fails. The maximum stress a material bear before breaking itself is known as the untimate stress point or ultimate tensile strength (UTS) point. When the material undergoes stress beyond this point permanent damage occurs to the material and it can no longer restore its original shape.

![](./images/813051770249936901_13.jpg)
![](./images/813051770249936901_14.jpg)
![](./images/813051770249936901_15.jpg)
![](./images/813051770249936901_16.jpg)

Fig. 8. Electronic band and dos plot variations with respect to uniaxial armchair stress. (a), (b) & (c) represents compressive regime and (d), (e) & (f) represents tensile regime. The band gap values are (a) Metallic, (b) $E_g$ = 1.85 eV, (c) $E_g$ = 2.34 eV, (d) $E_g$ = 2.35 eV and (e) $E_g$ = 1.95 eV and (f) $E_g$ = 0.91 eV.

The typical stress - strain curves of SiC within uniaxial zigzag, uniaxial armchair and biaxial stresses are as shown in Fig. 5. Here, the ultimate stress and strain is 20.22 N/m and 0.24 for uniaxial zigzag, 21.21 N/m and 0.24 for uniaxial armchair and 16.05 N/m and 0.18 for biaxial direction respectively. UTS values of graphene, silicene is also tabulated along with SiC to have a comparison on the mechanical strength of these materials (Table 2). The values imply that SiC may be considered as a strong material. The values of stress in the compressive regime is larger compared to that in the tensile regime as compression brings the atoms closer which makes the system in need of larger stress to compress than to expand. Also, compression makes the atomic orbitals repel making the stress almost double in the case of biaxial stress. The whole area under stress-strain curve upto fracture gives the toughness of the material. It is actually the energy required or stored by the material before fracture. The calculated value of toughness is around 3.8 GPa implying that the material is quite tough compared to graphene having a value of 4.4 GPa.

### 3.3. Electrical properties

The electronic band structure of undeformed SiC is shown in Fig. 6. It is a wide direct band gap semiconductor having a direct band gap of 2.35 eV. Applying or inducing stress is an efficient method to tune the band gap of any material. Here, changes in electronic structure was determined with respect to varying stress. In the case of uniaxial zigzag stress, band gap decreases continuously in the compressive regime and

![](./images/813051770249936901_17.jpg)

Fig. 9. Electronic band and dos plot variations with respect to biaxial stress. (a), (b) & (c) represents compressive regime and (d), (e) & (f) represents tensile regime. The band gap values are (a) $E_g$ = 2.56 eV, (b) $E_g$ = 2.88 eV, (c) $E_g$ = 3.12 eV, (d) $E_g$ = 2.65 eV, (e) $E_g$ = 1.83 eV, and (f) Metallic.

the nature of the transition changes from direct to indirect with a slight change in stress value, the band gap reduces further and becomes metallic at the highest stress of 77 N/m. It shows a decreasing trend in the tensile regime maintaining the direct nature till 12 N/m and then transforming into an indirect band gap semiconductor at 15 N/m as seen from Fig. 7. With increasing stress both in compressive and tensile regime, the valence and conduction bands shift causing a decrease of the band gap. The change in inter atomic distance and bond length due to the applied stress causes different superposition of Kohn-Sham orbitals causing a decrease of band gap. In the tensile regime, as the stress increases valence and conduction bands shift towards Fermi level reducing the band gap. As the stress increases more and more Kohn-Sham orbitals come closer to the Fermi level contributing to the reduction in band gap. The observation on band gap reduction could also be confirmed by looking at the DOS plot as shown in Fig. 8. Similar trend is observed in uniaxial armchair stress with the transition from direct to indirect with a slight compressive stress. The system turns metallic at the highest stress of 85 N/m as observed. The indirect nature is maintained in the whole tensile regime.

In the case of biaxial stress, the band gap shows an increasing trend upto 40 N/m and then shows a decreasing trend. With increasing compressive stress upto 40 N/m, the atomic orbitals that contribute to the band gap are mainly the Si($p_z$) and C($p_z$) orbitals which could be seen from the DOS plot (Fig. 9). Further increase in stress induces other atomic orbitals also to come closer to the Fermi level which inturn makes the system metallic at the highest applied stress (139 N/m), $p_x$,

![](./images/813051770249936901_18.jpg)

Fig. 10. Charge density plot of undeformed SiC. The red to blue represents maximum to minimum levels of charge distribution. This plot shows the maximum charge accumulation around C atom instead of a uniform distribution pointing towards the ionic nature of the 2D-SiC. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

$p_y$, $p_z$ orbitals of Si and C contribute more towards the Fermi level thus reducing the band gap. Here, system transforms to indirect band gap semiconductor at a very small stress of around 5 N/m and then transforms to direct after 40 N/m. In the tensile regime, band gap decreases continuously maintaining the direct nature and the system turns metallic around 16 N/m. Thus, application of stress is a convenient way to easily tune the band gap of materials.

Charge density contours helps to understand the interactions between different atoms. The charge density contour was plotted for the undeformed SiC and for the maximum compressive and tensile stresses in zigzag, armchair and biaxial directions. The charge density plot for the undeformed SiC shows a maximum charge density around C atom implying an ionic character by SiC rather than a covalent nature which may be because of the higher electronegativity of C compared to Si. Charge density on each atom was calculated using Bader analysis by partitioning the charge density along zero-flux surfaces (Henkelman et al., 2006). Zero-flux surface is a 2D-surface where the charge density is minimum perpendicular to the surface. Bader analysis done on SiC also confirms this observation and the charge density value obtained was $7.99/\AA^3$. The charge density plot of SiC is as shown in Fig. 10.

Fig. 11 shows the charge density plots for the maximum compressive and maximum tensile stresses for uniaxial zigzag, uniaxial armchair and biaxial directions respectively. In the case of compressive stress, the bond length reduces which causes orbitals to overlap to a

![](./images/813051770249936901_19.jpg)

Fig. 11. Charge density plot for (a) and (b) uniaxial zigzag, (c) and (d) uniaxial armchair, (e) and (f) biaxial. Plots for maximum compressive and maximum tensile are plotted in each case. Red to blue represents the maximum to minimum levels of charge distribution. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

greater extent thus increasing the extent of charge density. But in the case of tensile regime, the bond length increases causing reduced overlapping of orbitals thus the extent of charge density decreases but in all the cases the maximum charge density is accumulated around C atom which is also confirmed by the Bader charge analysis.

## 4. Conclusions

Stress was applied on SiC to understand the change in its structural, mechanical and electronic behaviours. SiC is energetically stable in the studied stress range for both compressive and tensile regime. The uni-axial zigzag and armchair stress changes the structure and symmetry of the system from hexagonal to orthorhombic whereas biaxial stress maintains the hexagonal symmetry. The mechanical stability of the system was studied in terms of the magnitudes of second order elastic constants. SiC shows considerable stability with uniaxial zigzag, arm- chair and biaxial stresses and showed anisotropic behaviour along different directions and along the strain grids from $-0.1$ to $0.1$. The band gap tuning of SiC was achieved using stress thus transforming the material from direct to indirect band gap semiconductor. Application of stress also reduces the band gap making the system metallic. Thus, inducing stress is an efficient way to easily tune the band gap of ma- terials. Charge density plot and Bader analysis confirmed the ionic nature of SiC in two dimension.

## References

Bekaroglu, E., Topsakal, M., Cahangirov, S., Ciraci, S., 2010. First-principles study of defects and adatoms in silicon carbide honeycomb structures. Phys. Rev. B 81 (7), 075433.

Bhattacharyya, S., Singh, A.K., 2012. Semiconductor-metal transition in semiconducting bilayer sheets of transition-metal dichalcogenides. Phys. Rev. B 86 (7), 075454.

Blöchl, P.E., 1994. Projector augmented-wave method. Phys. Rev. B 50 (24), 17953.

Born, M., Huang, K., 1954. Dynamical Theory of Crystal Lattices. Clarendon, Oxford.

Chabi, S., Chang, H., Xia, Y., Zhu, Y., 2016. From graphene to silicon carbide: ultrathin silicon carbide flakes. Nanotechnology 27 (7), 075602.

Cooper, R.C., Lee, C., Marianetti, C.A., Wei, X., Hone, J., Kysar, J.W., 2013. Nonlinear elastic behavior of two-dimensional molybdenum disulfide. Phys. Rev. B 87 (3), 035423.

Ding, Y., Wang, Y., 2013. Density functional theory study of the silicene-like SiX and XSi₃ (X= B, C, N, Al, P) honeycomb lattices: the various buckled structures and versatile electronic properties. J. Phys. Chem. C 117 (35), 18266-18278.

Gori, P., Pulci, O., Marsili, M., Bechstedt, F., 2012. Side-dependent electron escape from graphene-and graphane-like sic layers. Appl. Phys. Lett. 100 (4), 043110.

Henkelman, G., Arnaldsson, A., Jónsson, H., 2006. A fast and robust algorithm for bader decomposition of charge density. Comput. Mater. Sci 36 (3), 354-360.

Jones, R.O., Gunnarsson, O., 1989. The density functional formalism, its applications and prospects. Rev. Mod. Phys. 61 (3), 689.

Kaloni, T.P., Schwingenschlögl, U., 2014. Effects of heavy metal adsorption on silicene. Phys. Status Solidi-Rapid Res. Lett. 8 (8), 685-687.

Kara, A., Enriquez, H., Seitsonen, A.P., Voon, L.L.Y., Vizzini, S., Aufray, B., Oughaddou, H., 2012. A review on silicenew candidate for electronics. Surf. Sci. Rep. 67 (1), 1-18.

Kresse, G., Furthmüller, J., 1996. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54 (16), 11169.

Kresse, G., Hafner, J., 1993. Ab initio molecular dynamics for liquid metals. Phys. Rev. B 47 (1), 558.

Kresse, G., Hafner, J., 1994. Ab initio molecular-dynamics simulation of the liquid-me- tal-amorphous-semiconductor transition in germanium. Phys. Rev. B 49 (20), 14251.

Kunstmann, J., Wendumu, T.B., Seifert, G., 2017. Localized defect states in MoS₂ monolayers: electronic and optical properties. Phys. Status Solidi (B) 254 (4).

Kuzubov, A., Eliseeva, N., Krasnov, P., Tomilin, F., Fedorov, A., Tolstaya, A., 2013. Possibility of a 2d SiC monolayer formation on Mg (0001) and MgO (111) substrates. Russ. J. Phys. Chem. A 87 (8), 1332-1335.

Lang, H., Zhang, S., Liu, Z., 2016. Mobility anisotropy of two-dimensional semi- conductors. Phys. Rev. B 94 (23), 235306.

Lin, X., Ni, J., 2012. Electronic and magnetic properties of substitutionally Fe-, Co-, and Ni-doped BC3 honeycomb structure. J. Appl. Phys. 111 (3), 4309.

Malakkal, L., Szpunar, B., Szpunar, J., 2017. Comparative study of thermal conductivity of SiC and BeO from ab initio calculations. Energy Materials 2017. Springer, pp. 377-384.

Mouhat, F., Coudert, F.-X., 2014. Necessary and sufficient elastic stability conditions in various crystal systems. Phys. Rev. B 90 (22), 224104.

Novoselov, K.S., Geim, A.K., Morozov, S.V., Jiang, D., Zhang, Y., Dubonos, S.V., Grigorieva, I.V., Firsov, A.A., 2004. Electric field effect in atomically thin carbon films. Science 306 (5696), 666-669.

Peng, Q., Chen, X.-J., Liu, S., De, S., 2013. Mechanical stabilities and properties of gra- phene-like aluminum nitride predicted from first-principles calculations. RSC Adv. 3 (19), 7083-7092.

Peng, Q., Liang, C., Ji, W., De, S., 2013. A first principles investigation of the mechanical properties of g-ZnO: the graphene-like hexagonal zinc oxide monolayer. Comput. Mater. Sci 68, 320-324.

Perdew, J.P., Burke, K., Ernzerhof, M., 1996. Generalized gradient approximation made simple. Phys. Rev. Lett. 77 (18), 3865.

Roman, R.E., Cranford, S.W., 2014. Mechanical properties of silicene. Comput. Mater. Sci 82, 50-55.

Şahin, H., Cahangirov, S., Topsakal, M., Bekaroglu, E., Akturk, E., Senger, R.T., Ciraci, S., 2009. Monolayer honeycomb structures of group-iv elements and iii-v binary com- pounds: First-principles calculations. Phys. Rev. B 80 (15), 155453.

Şahin, H., Peeters, F.M., 2013. Adsorption of alkali, alkaline-earth, and 3 d transition metal atoms on silicene. Phys. Rev. B 87 (8), 085423.

Saxena, S., Tyson, T.A., 2008. Pressure effects on the atomic and electronic structure of aligned small diameter carbon nanotubes. arXiv preprint arXiv:0805.0614.

Shao, T., Wen, B., Melnik, R., Yao, S., Kawazoe, Y., Tian, Y., 2012. Temperature depen- dent elastic constants and ultimate strength of graphene and graphyne. J. Chem. Phys. 137 (19), 194901.

Shi, Z., Zhang, Z., Kutana, A., Yakobson, B.I., 2015. Predicting two-dimensional silicon carbide monolayers. ACS Nano 9 (10), 9802-9809.

Tang, Q., Bao, J., Li, Y., Zhou, Z., Chen, Z., 2014. Tuning band gaps of BN nanosheets and nanoribbons via interfacial dihalogen bonding and external electric field. Nanoscale 6 (15), 8624-8634.

Ukpong, A.M., 2015. First principles study of van der waals heterobilayers. Comput. Condens. Matter 2, 1-10.

Wang, H., Cao, J., Huang, X., Huang, J., 2012. Pressure dependence of elastic and dy- namical properties of zinc-blende ZnS and ZnSe from first principle calculation. arXiv preprint arXiv:1204.6102.

Wang, N., Tian, Y., Zhao, J., Jin, P., 2016. Co oxidation catalyzed by silicon carbide (SiC) monolayer: a theoretical study. J. Mol. Graphics Modell. 66, 196-200.

Wang, R., Wang, S., Wu, X., Liang, X., 2010. First-principles calculations on third-order elastic constants and internal relaxation for monolayer graphene. Physica B 405 (16), 3501-3506.

Wang, Y., Cheng, R., Dong, J., Liu, Y., Zhou, H., Yu, W.J., Terasaki, I., Huang, Y., Duan, X., 2014. Metal-semiconductor transition in atomically thin Bi₂Sr₂Co₂O₈ nanosheets. APL Mater. 2 (9), 092507.

Zhang, S., Yan, Z., Li, Y., Chen, Z., Zeng, H., 2015. Atomically thin arsenene and anti- monene: semimetal-semiconductor and indirect-direct band-gap transitions. Angew. Chem. Int. Ed. 54 (10), 3112-3115.

Zhang, Z., Liu, X., Yu, J., Hang, Y., Li, Y., Guo, Y., Xu, Y., Sun, X., Zhou, J., Guo, W., 2016. Tunable electronic and magnetic properties of two-dimensional materials and their one-dimensional derivatives. Wiley Interdiscip. Rev.