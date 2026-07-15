Accepted Manuscript

Lattice thermal conductivity of penta-graphene

Fancy Qian Wang, Jiabing Yu, Qian Wang, Yoshiyuki Kawazoe, Puru Jena

![](./images/814527540948369409_1.jpg)

PII: S0008-6223(16)30325-6

DOI: 10.1016/j.carbon.2016.04.054

Reference: CARBON 10935

To appear in: Carbon

Received Date: 22 February 2016

Revised Date: 15 April 2016

Accepted Date: 23 April 2016

Please cite this article as: F.Q. Wang, J. Yu, Q. Wang, Y. Kawazoe, P. Jena, Lattice thermal conductivity of penta-graphene, Carbon (2016), doi: 10.1016/j.carbon.2016.04.054.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Lattice thermal conductivity of penta-graphene

Fancy Qian Wang$^{a,b}$, Jiabing Yu$^b$, Qian Wang$^{a,b,c,*}$, Yoshiyuki Kawazoe$^d$, and Puru Jena$^c$

$^{a}$ Center for Applied Physics and Technology, College of Engineering, Peking University; IFSA Collaborative Innovation Center, Key Laboratory of High Energy Density Physics Simulation, Ministry of Education, Beijing 100871, China
$^{b}$ Department of Materials Science and Engineering, College of Engineering, Peking University, Beijing 100871, China.
$^{c}$ Department of Physics, Virginia Commonwealth University, Richmond, VA 23284, USA
$^{d}$ New Industry Creation Hatchery Center, Tohoku University, Sendai, 980-8577, Japan

## Abstract

Motivated by the unique geometry and novel properties of penta-graphene proposed recently as a new carbon allotrope consisting of pure pentagons [Zhang et al. *Proc. Natl. Acad. Sci.* **2015**, *112*, 2372], we systematically investigated its phonon transport properties by solving exactly the linearized phonon Boltzmann transport equation combined with first principles calculations. The intrinsic lattice thermal conductivity $K_{lat}$ of penta-graphene is found to be about 645 W/mK at room temperature, which is significantly reduced as compared to that of graphene. The underlying reason is the strong anharmonic effect introduced by the buckled pentagonal structure with hybridized $sp^2$ and $sp^3$ bonding. A detailed analysis of the phonons of penta-graphene reveals that the ZA mode is the primary heat carrier (nearly 60%). The $K_{lat}$ is dominated by three-phonon scattering where the scattering rate of the Normal scattering process is comparable to that of the Umklapp scattering process. The phonon mean free path of the collective phonon excitations is in the order of micrometers. Complementing the high thermal conductivity of graphene, the low thermal conductivity of penta-graphene adds additional features to the family of carbon materials for thermal applications.

### 1. Introduction

Lattice thermal conductivity, $K_{lat}$, is an important physical quantity used to characterize phonon transport properties in materials for thermal applications. Materials with high $K_{lat}$ are commonly used in cooling microelectronics for passive heat spreading while thermoelectric devices for energy conversion require materials with strongly suppressed $K_{lat}$ (< 3 W/mK). In terms of the ability to conduct heat, carbon allotropes are of special interest because their $K_{lat}$ spans an over extraordinary large range of five orders of magnitude [1]. Especially for materials at the nanoscale, the $K_{lat}$ exhibits intriguing features owing to their novel low-dimensional atomic configurations.

The $K_{lat}$ of graphene measured by Raman spectroscopy falls in the range of 3000~5800 W/mK [2-5] at room temperature, which exceeds that of diamond, the best bulk heat conductor. Such superior $K_{lat}$ can be attributed to the good combination of light-weight, strong bond stiffness and its planar honeycomb lattice where all carbon atoms are $sp^2$ hybridized [6]. However, when the geometrical structure is modified to graphyne or graphdiyne by introducing acetylenic units (-C≡C-) between the carbon hexagons, the $K_{lat}$ is substantially reduced as compared to that of graphene. This is due to the low atomic density in the $sp$ and $sp^2$ hybridized structures and the weak single bonds between the carbon atoms [7-10]. This shows that the intrinsic $K_{lat}$ has an intimate relationship with the topological arrangement of carbon atoms. The strong dependence of thermal conductivity on geometry and dimensionality provides the possibility to design new carbon structures with different thermal conductivity for diverse applications.

Recently a new carbon allotrope consisting entirely of pentagons named penta-graphene was proposed [11]. Unlike graphene or graphyne and graphdiyne, penta-graphene is a $sp^2$ and $sp^3$ hybridized system with two carbon atoms in $sp^3$ and four carbon atoms in $sp^2$ hybridized state in its unit cell [11]. Because of the tetrahedral character of the $sp^3$ hybridized carbon atoms, penta-graphene is a quasi-two dimensional (2D) sheet with a total thickness of 1.2 Å. Due to these unique geometrical features of penta-graphene, we wondered how high the thermal conductivity of penta-graphene could be? Which scattering mechanism does the thermal transport control? How important is the contribution of the phonon branches to $K_{lat}$? A systematic study of the phonon transport properties of penta-graphene has been carried out to answer these questions.

## 2. Computational Methods

In semiconductors, heat is carried primarily by phonons and the intrinsic $K_{lat}$ is dominated by phonon-phonon interactions resulting from the anharmonicity of interatomic potential around and above room temperature [6]. What is of interest here is the lowest order of anharmonic scattering, namely three-phonon scattering. However, the complex inelastic nature of three-phonon scattering makes it difficult to accurately predict phonon lifetimes [12]. Therefore, some approximations, such as single-mode relaxation time approximation (RTA) combined with Debye approximation was used to calculate $K_{lat}$ in previous theoretical studies, where the averaged Grüneisen parameters were used to evaluate the strength of anharmonic scattering [13, 14]. In addition, this method only describes the depopulation of the phonon states rigorously, but entirely neglects the effect of the corresponding

repopulation, which is assumed to have no memory of the initial phonon distributions [15,
16]. In other words, such an approach disregards the momentum-conserving nature of the
Normal ($N$) scattering process. Thus, its application becomes questionable particularly in the
low temperature region (< Debye temperatures $\Theta_D$), where the resistive Umklapp ($U$)
scattering process is frozen out, while the $N$ process dominates the phonon relaxation. As a
result, the calculated $K_{lat}$ is always underestimated due to the lack of information of the $N$
process [15, 17].

In this study, we have used an iterative approach, as implemented in the ShengBTE
package [18], to determine phonon lifetimes. This approach solves exactly the linearized
phonon Boltzmann transport equation (BTE) [19], which has been widely used to calculate
the $K_{lat}$ of various materials, showing satisfactory accuracy and predictive power [6, 20-25].
The inputs to the BTE for calculating $K_{lat}$ are the harmonic and anharmonic interatomic force
constants (IFCs) obtained from first principles calculations within the framework of density
functional theory (DFT) as implemented in the Vienna Ab initio Simulation Package (VASP)
[26]. The Perdew-Burke-Ernzerhof (PBE) functional within the generalized gradient
approximation (GGA) [27] is used to treat the electronic exchange-correlation interaction.
The kinetic energy cutoff of plane waves is set to 500 eV. The 8×8×1 and 5×5×1 supercells
are used to calculate the harmonic and anharmonic IFCs, respectively, and a cutoff radius of
6.5 Å (up to the $14^{\text{th}}$ nearest neighbors) is selected to ensure the accuracy of our calculations.
Specifically, the harmonic IFCs enter dynamical matrix determining the phonon dispersions,
velocities, and eigenvectors, while the anharmonic IFCs enter scattering matrix determining
phonon lifetimes and phonon mean free path (MFP). In addition, the presence of naturally

occurring isotopic purification ($^{12}$C=98.9%, $^{13}$C=1.1%) is also included to downscale the $K_{lat}$, as is the case with diamond [28], Ge [29], and GaN [30].

## 3. Results and discussions

### 3.1. Phonon spectra and group velocity

Since detailed information on the vibrational states is prerequisite for understanding $K_{lat}$, we begin with an investigation of the lattice dynamics of penta-graphene. The fully relaxed lattice constants are $a$=$b$=3.64 Å, in good agreement with previous calculation [11]. Considering the isotropy of penta-graphene ($K_{xx}$=$K_{yy}$) [25], the phonon spectrum along the $\Gamma$ – X high symmetry line is taken into account. The calculated results are displayed in Fig. 1a. Penta-graphene, with six atoms per unit cell, has three acoustic branches and fifteen optical branches. The acoustic branches include the in-plane transverse acoustic (TA) mode, longitudinal acoustic (LA) mode, and the out-of-plane flexural acoustic (ZA) mode. The TA and LA modes, as shown in Fig. 1a, have linear dispersions as the wave vector approaches the $\Gamma$ point, whereas the out-of-plane ZA mode exhibits a parabolic dispersion due to the rapid decay of the transversal forces [31], which is a general characteristic of 2D materials.

It is important to note that the three acoustic branches are much more dispersive as compared to the relatively localized optical branches, implying a smaller contribution of the optical branches to the $K_{lat}$, due to their lower group velocity ($V_{g}$). We calculate $V_{g}$ for the $n^{\text{th}}$ mode using $V_{n}$=$d\omega_{n}/dq$. The $V_{g}$ - $q$ and $V_{g}$-$\omega$ relationships are given in Fig. 1b and 1c, respectively. For the TA and LA modes along the $\Gamma$ – X high symmetry line, $V_{g}$ is 12.91 km/s and 17.17 km/s at the long-wavelength limit, respectively, which is quite large and comparable to that of graphene, namely, 13.6 (TA) and 21.3 (LA) km/s [32]. From the $V_{g}$-$\omega$

relationship, we note that $V_g$ of the TA and LA modes drops dramatically with increasing phonon frequency $(\omega)$, while that of the ZA mode increases with phonon frequency, and reaches its maximum at 6.62 THz. It then decreases and finally reaches zero at the zone edge. In addition, the frequency of the ZA mode is quite different from that of the TA and LA modes in the region between the $\Gamma$ and M points, providing opportunities for the ZA mode to carry more heat for transport.

![](./images/814527540948369409_2.jpg)

Fig. 1. (a) Phonon spectrum along the $\Gamma$ - X high symmetry line and PhDOS of penta-graphene. Variation of group velocity $V_g$ of the three acoustic branches (b) along the $\Gamma$ - X high symmetry line, and (c) with the frequency of penta-graphene.

### 3.2. Scattering mechanism and lattice thermal conductivity

The isotopic scattering and the anharmonic three-phonon scattering dominate the intrinsic $K_{lat}$. For comparison, the frequency dependence of the two scattering processes for penta-graphene at room temperature is calculated and plotted in Fig. 2a. This shows that the

three-phonon scattering is nearly ten times more intense than the isotopic scattering, implying that the effect of the three-phonon scattering on the $K_{lat}$ is much stronger than that of the isotopic scattering.

To further verify the above analysis, the temperature-dependent $K_{lat}$ of penta-graphene is calculated. The fitted $K_{lat}$-$T$ curve, as given in Fig. 2b, shows an approximate relationship of $K_{lat} \propto \frac{1}{T^{0.735}}$, confirming that the three-phonon scattering modulates the thermal transport. Our calculated $K_{lat}$ of penta-graphene is about 645 W/mK at room temperature, which is reduced by nearly 80%-90% from that of graphene. We note that the value of $K_{RTA}$ calculated using the RTA solution is only half as much as that of the $K_{lat}$ obtained by using the iterative approach at room temperature, as shown in Fig. 2b. Such difference occurs in materials where the scattering rate of the $N$ process is comparable to the $U$ process. This is because within the RTA solution [33] the $N$ process is incorrectly treated as an independent resistive process on the same footing as the $U$ process. Therefore, in penta-graphene, both the $N$ and $U$ processes play an important role in the phonon-phonon interactions at room temperature. Similar behavior was also observed in other carbon allotropes [12, 25, 34].

In addition, we further note that the $K_{RTA}$ gets closer to the $K_{lat}$ as temperature increases. Such phenomenon is partially attributed to the lower Debye temperature $\Theta_D$ of penta-graphene. Debye temperature $\Theta_D$ is defined as,$$\Theta_D = \frac{h v_m}{k_B}$$, where $h$ is Planck's constant, $v_m$ is the highest frequency of the corresponding phonon branches, and $k_B$ is the Boltzmann constant. Our calculated $\Theta_D$ of penta-graphene is 344.6 K (ZA), 692 K (TA), and 498.2 K (LA), respectively, much lower than the corresponding values of 675.6 K (ZA), 895 K (TA) and 1910 K (LA) of graphene. Consequently, more phonon branches are activated at a given

temperature (typically 300 K), leading to an increase in the phonon population and the phonon scattering rate, and hence a reduction of $K_{lat}$. Fig. 2b shows that the $K_{lat}$ decreases dramatically (about 70%) with elevated temperature from 300 K to 700 K, whereas it drops slowly above 700 K because of the characteristic $\Theta_{D}$ of the three acoustic branches. Note that $\Theta_{D}$ is a measurement of the temperature above which the corresponding mode begins to be excited and below which modes are frozen out [35]. The three acoustic branches, the primary heat carriers, are fully excited when temperature is higher than 692 K (the $\Theta_{D}$ of the TA), providing a reasonable explanation for the tendency of $K_{lat}$-$T$ curve. In addition, Fig. 2a shows that the anharmonic effect of the ZA mode is much weaker than that of the TA and LA modes in a large range of the low frequency, indicating that the ZA mode carries majority of the heat.

![](./images/814527540948369409_3.jpg)

Fig. 2. (a) Variations of the three-phonon scattering and the isotopic scattering rates of the acoustic branches with frequency at 300 K, and (b) variation of the $K_{lat}$ and $K_{RTA}$ with temperature in penta-graphene.

### 3.3. Mode Grüneisen parameter

To quantify the anharmonic interactions between the phonon branches, the mode Grüneisen parameter ($\gamma$) is calculated using the quasi-harmonic approximation (QHA). This is defined as $\gamma_{\lambda}=-\frac{A}{\omega_{\lambda}} \frac{\partial \omega_{\lambda}}{\partial A}$, where $A$ is the area of the unit cell and $\omega_{\lambda}$ is the angular frequency of a specific phonon mode ($\lambda$). The $\gamma$ dispersion and $\gamma$-$\omega$ relationship are presented in Fig. 3a and 3b, respectively. Obviously, a divergent and negative $\gamma_{ZA}$ is observed near the $\Gamma$ point, which is ubiquitous for the bending ZA mode in 2D systems [36, 37]. The ZA bending mode is analogous to the flexural vibration in guitar string, where a tensile strain makes the lattice stiffer to such bending vibration, resulting in an increased frequency, namely, negative $\gamma$ [38, 39]. Except for $\gamma_{ZA}$, the rather localized $\gamma_{TA}$ (-0.1~0.4) and $\gamma_{LA}$ (-0.6~0.4) also exhibit some small negative values due to the relatively weak C-C bonding in penta-graphene. In general, bond bending (negative $\gamma$) and bond stretching (positive $\gamma$) make opposite contributions to $\gamma$. 2D systems where the bond bending dominates over the bond stretching, exhibit negative $\gamma_{TA}$ and $\gamma_{LA}$. In addition, a negative $\gamma$ is also related to the negative thermal expansion coefficient $\alpha$ ($\alpha \propto \gamma$), which is critical for 2D electronic devices. This is because the strain effects resulting from different $\alpha$ between samples and substrates, affect the performance and reliability in applications [40].

![](./images/814527540948369409_4.jpg)

Fig. 3. Calculated $\gamma$ of the three acoustic branches (a) along the $\Gamma$- X high symmetry line, and (b) that with the frequency of penta-graphene.

### 3.4. Three-phonon phase space

In majority of materials, primarily two types of three-phonon scattering channels are allowed: (1) scattering between three acoustic branches like acoustic + acoustic $\leftrightarrow$ acoustic $(aaa)$, and (2) decay of two acoustic branches into one optical branch or vice versa like acoustic + acoustic $\leftrightarrow$ optical $(a a o)$ [41, 42]. To find out which scattering channels manipulate the three-phonon scattering, we examine the allowed three-phonon phase space $P_{3}$ including both the absorption $(P_{3}^{+})$ and the emission $(P_{3}^{-})$ processes [42]. The calculated results are displayed in Fig. 4a, 4b and 4c, respectively, which show that for the ZA mode, the $P_{3}$ is much larger than that of the TA and LA modes in a large part of the low-frequency range due to its lower energy. Hence, the processes like ZA+ZA/LA/TA $\leftrightarrow$ LA/TA/OP (OP is short for the optical modes) are the predominant scattering channels in thermal transport. The $P_{3}^{+}(ZA)$ is much more intense than the $P_{3}^{-}(ZA)$ by about two orders of the magnitude, revealing that the processes of ZA+ZA/LA/TA $\leftrightarrow$ LA/TA/OP occur easier from left to right.

For the TA and LA modes, their $P_3$ is almost equal, and their $P_3{^+}$ is larger than the $P_3{^-}$, respectively, implying that the processes of TA+TA/LA/ZA→OP/LA/TA, LA+LA/TA/ZA→OP/LA/TA are preferable.

A further analysis of the contribution from each phonon branch to the $K_{lat}$ reveals that the ZA mode contributes nearly 60% to the $K_{lat}$, which is over three times larger than that from the TA (19.45%) and LA (16.02%) modes, as shown in Fig. 4d, due to its weaker anharmonic effect. However, such large contribution is still small as compared to that in graphene (80%) because the reflection symmetry breaks down in the quasi-2D buckled structure of penta-graphene [24]. In addition, the inverse relationship between the $P_3$ and the $K_{lat}$ is not preserved in penta-graphene due to the non-ignorable effect of the $N$ process in the three-phonon scattering.

![](./images/814527540948369409_5.jpg)

Fig. 4. Frequency-dependent three-phonon phase space of the three acoustic branches for (a)

all allowed three-phonon processes $P_3$, (b) the absorption process $P_3^+$, and (c) the emission process $P_3^-$ of penta-graphene. (d) Contributions of the acoustic branches and the optical branches to the $K_{lat}$ as a function of temperature.

### 3.5. Phonon mean free path

Before commenting on the reliability of simulation results, it is important to clarify the difference between the microscale and macroscale descriptions of $K_{lat}$. In microscale, a rigorous description of $K_{lat}$ requires an iterative solution of the Boltzmann transport equation, where the phonon branches behave like the collective excitations characterized by the phonon mean free path (MFP). At the macroscale, the Fourier's law satisfying experimental measurement, is used to determine the $K_{lat}$ of a material [16]. Fourier's law is applicable only when the condition $L>L_{max}$, where $L_{max}$ is the maximum phonon MFP in microscale and $L$ is a sample size in macroscale, is satisfied. Thus, the simulation results can be comparable to experimental data. On this account, we investigate the normalized $K_{lat}$ utilizing the phonon MFP accumulation function, which was demonstrated to be a particularly useful quantity to describe the MFP relevant for heat conduction [43]. Thus, two typical phonon transport regimes, namely, the ballistic and diffusive regimes of penta-graphene are calculated and presented in Fig. 5. One can see an extremely broad phonon MFP spectrum ranging from a few nanometers to 5 microns, where the phonon branches contribute unevenly to the $K_{lat}$. In the ballistic regime, the $K_{lat}$ increases with the elevated phonon MFP until reaching the thermodynamic limit in the diffusive regime, where the allowed phonon MFP is above $L_{max}$.

At room temperature, the phonon branches with the MFP shorter than 278 nm contribute 50% to the $K_{lat}$, while those with the MFP longer than 585 nm only contribute 20% to the $K_{lat}$. The

MFPs corresponding to the 50% accumulation at 300, 500, 800 and 1000 K are calculated to be 278, 109, 52 and 39 nm, respectively. It is worthwhile to mention that the $K_{lat}$ of penta-graphene can be tuned through several possible ways such as isotope disorder, tensile strain and chemical functionalization, which can introduce defects, or change the bond strength for enhancing phonon scattering. However, further systematic studies are needed, which is ongoing and will be released elsewhere in due course. Here we only focus on the intrinsic $K_{lat}$ of penta-graphene.

![](./images/814527540948369409_6.jpg)

Fig. 5. Normalized $K_{lat}$ accumulation as a function of the phonon MFP of penta-graphene at different temperatures. The vertical dotted lines indicate the phonon MFPs corresponding to the 50% accumulation.

### 4. Conclusions

In conclusion, we investigate the lattice thermal conductivity of penta-graphene by solving exactly the linearized phonon Boltzmann transport equation combined with state-of-the-art theoretical calculations. We show that the intrinsic $K_{lat}$ of penta-graphene is

about 645 W/mK at room temperature which is significantly reduced as compared to that of graphene. The possible reasons are: (1) the buckled pentagonal structure of penta-graphene breaks the selection rule of graphene, thus more scattering channels are provided by the ZA mode. (2) The hybridized $sp^2$ and $sp^3$ bonding in penta-graphene enhances the anharmonicity of the phonon branches. (3) The lower Debye temperature leads to the higher phonon scattering rate because more phonon branches can be activated at a given temperature. (4) The three acoustic branches are the primary heat carriers with a dominate contribution coming from the ZA mode. The reduced thermal conductivity combined with the intrinsic band gap of 3.25 eV, the unusual negative Poisson's ratio, and the ultrahigh ideal strength makes penta-graphene attractive for potential applications.

AUTHOR INFORMATION

Corresponding Author

*E-mail: qianwang2@pku.edu.cn

ACKNOWLEDGEMENTS

This work is partially supported by grants from the National Natural Science Foundation of China (NSFC-51471004), the National Grand Fundamental Research 973 Program of China (Grant 2012CB921404), and the Doctoral Program of Higher Education of China (20130001110033). P.J. acknowledges support by the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering under Award #DE-FG02-96ER45579. Y.K. would like to thank ONR Global and ITC-PAC for the support

by the Grant No. N62909-16-1-2036. The authors thank the crew of the Center for Computational Materials Science, the Institute for Materials Research, Tohoku University (Japan), for their continuous support of the HITACHI SR11000 supercomputing facility.

## REFERENCES
[1] Balandin AA. Thermal properties of graphene and nanostructured carbon materials. Nat. Mater. 2011;10(8):569-81.

[2] Balandin AA, Ghosh S, Bao W, Calizo I, Teweldebrhan D, Miao F, et al. Superior thermal conductivity of single-layer graphene. Nano Lett. 2008;8(3):902-7.

[3] Cai W, Moore AL, Zhu Y, Li X, Chen S, Shi L, et al. Thermal Transport in Suspended and Supported Monolayer Graphene Grown by Chemical Vapor Deposition. Nano Lett. 2010;10(5):1645-51.

[4] Ghosh S, Bao W, Nika DL, Subrina S, Pokatilov EP, Lau CN, et al. Dimensional crossover of thermal transport in few-layer graphene. Nat. Mater. 2010;9(7):555-8.

[5] Chen S, Moore AL, Cai W, Suk JW, An J, Mishra C, et al. Raman Measurements of Thermal Transport in Suspended Monolayer Graphene of Variable Sizes in Vacuum and Gaseous Environments. ACS Nano 2011;5(1):321-8.

[6] Lindsay L, Broido DA, Mingo N. Flexural phonons and thermal transport in multilayer graphene and graphite. Phys. Rev. B 2011;83(23):235428.

[7] Zhang YY, Pei QX, Wang CM. A molecular dynamics investigation on thermal conductivity of graphynes. Comput. Mater. Sci. 2012;65:406-10.

[8] Wang J, Zhang A-J, Tang Y. Tunable thermal conductivity in carbon allotrope sheets: Role of acetylenic linkages. J. Appl. Phys. 2015;118(19):195102.

[9] Tan X, Shao H, Hu T, Liu G, Jiang J, Jiang H. High thermoelectric performance in two-dimensional graphyne sheets predicted by first-principles calculations. Phys. Chem. Chem. Phys. 2015;17(35):22872-81.

[10] Wang X-M, Mo D-C, Lu S-S. On the thermoelectric transport properties of graphyne by the first-principles method. J. Chem. Phys. 2013;138(20):204704.

[11] Zhang S, Zhou J, Wang Q, Chen X, Kawazoe Y, Jena P. Penta-graphene: A new carbon allotrope. Proc. Natl. Acad. Sci. 2015;112(8):2372-7.

[12] Ward A, Broido DA, Stewart DA, Deinzer G. Ab initio theory of the lattice thermal conductivity in diamond. Phys. Rev. B 2009;80(12):125203.

[13] Callaway J. Model for Lattice Thermal Conductivity at Low Temperatures. Phys. Rev. 1959;113:1046-51.

[14] Ziman JM. Electrons and phonons: the theory of transport phenomena in solids: Oxford University Press; 1960.

[15] Fugallo G, Lazzeri M, Paulatto L, Mauri F. Ab initio variational approach for evaluating lattice thermal conductivity. Phys. Rev. B 2013;88(4):045430.

[16] Fugallo G, Cepellotti A, Paulatto L, Lazzeri M, Marzari N, Mauri F. Thermal Conductivity of Graphene and Graphite: Collective Excitations and Mean Free Paths. Nano Lett. 2014;14(11):6109-14.

[17] Guyer RA, Krumhansl JA. Solution of the Linearized Phonon Boltzmann Equation. Phys. Rev. 1966;148:766-78.

[18] Li W, Carrete J, A. Katcho N, Mingo N. ShengBTE: A solver of the Boltzmann transport equation for

phonons. Comput. Phys. Commun. 2014;185:1747-58.

[19] Omini M, Sparavigna A. An iterative approach to the phonon Boltzmann equation in the theory of thermal conductivity. Phys. B: Condens. Matter 1995;212(2):101-12.

[20] Kuang Y, Lindsay L, Shi S, Zheng G-P. Tensile strains give rise to strong size effects for thermal conductivities of silicene, germanene and stanene. Nanoscale 2016;8(6):3760-7.

[21] Kuang Y, Lindsay L, Huang B. Unusual Enhancement in Intrinsic Thermal Conductivity of Multilayer Graphene by Tensile Strains. Nano Lett. 2015;15(9):6121-7.

[22] Li W, Mingo N. Ultralow lattice thermal conductivity of the fully filled skutterudite YbFe4Sb12 due to the flat avoided-crossing filler modes. Phys. Rev. B 2015;91(14):144304.

[23] Li W, Lindsay L, Broido DA, Stewart DA, Mingo N. Thermal conductivity of bulk and nanowire Mg2SixSn1-x alloys from first principles. Phys. Rev. B 2012;86(17):174307.

[24] Lindsay L, Broido DA, Mingo N. Flexural phonons and thermal transport in graphene. Phys. Rev. B 2010;82(11):115427.

[25] Lindsay L, Li W, Carrete J, Mingo N, Broido DA, Reinecke TL. Phonon thermal transport in strained and unstrained graphene from first principles. Phys. Rev. B 2014;89(15):155426.

[26] Kresse G, Furthmüller J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 1996;54(16):11169-86.

[27] Perdew JP, Burke K, Ernzerhof M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996;77(18):3865-8.

[28] Wei L, Kuo PK, Thomas RL, Anthony TR, Banholzer WF. Thermal conductivity of isotopically modified single crystal diamond. Phys. Rev. Lett. 1993;70(24):3764-7.

[29] Asen-Palmer M, Bartkowski K, Gmelin E, Cardona M, Zhernov AP, Inyushkin AV, et al. Thermal conductivity of germanium crystals with different isotopic compositions. Phys. Rev. B 1997;56:9431-47.

[30] Lindsay L, Broido DA, Reinecke TL. Thermal Conductivity and Large Isotope Effect in GaN from First Principles. Phys. Rev. Lett. 2012;109(9):095901.

[31] Şahin H, Cahangirov S, Topsakal M, Bekaroglu E, Akturk E, Senger RT, et al. Monolayer honeycomb structures of group-IV elements and III-V binary compounds: First-principles calculations. Phys. Rev. B 2009;80:155453.

[32] Nika DL, Pokatilov EP, Askerov AS, Balandin AA. Phonon thermal conduction in graphene: Role of Umklapp and edge roughness scattering. Phys. Rev. B. 2009;79(15):155413.

[33] Lindsay L, Broido DA, Reinecke TL. Ab initio thermal transport in compound semiconductors. Phys. Rev. B 2013;87(16):165201.

[34] Lindsay L, Broido DA, Mingo N. Diameter dependence of carbon nanotube thermal conductivity and extension to the graphene limit. Phys. Rev. B 2010;82(16):161402.

[35] Nakashima T, Umakoshi Y. Anisotropy of electrical resistivity and thermal expansion of single-crystal Ti5Si3. Phil. Mag. Lett. 1992;66(6):317-21.

[36] Fultz B. Vibrational thermodynamics of materials. Prog. Mater. Sci. 2010;55(4):247-352.

[37] Mounet N, Marzari N. First-principles determination of the structural, vibrational and thermodynamic properties of diamond, graphite, and derivatives. Phys. Rev. B 2005;71(20):205214.

[38] Huang LF, Gong PL, Zeng Z. Correlation between structure, phonon spectra, thermal expansion, and thermomechanics of single-layer MoS2. Phys. Rev. B 2014;90(4):045409.

[39] Huang L-F, Gong P-L, Zeng Z. Phonon properties, thermal expansion, and thermomechanics of silicene and germanene. Phys. Rev. B 2015;91(20):205433.

[40] Cai Y, Lan J, Zhang G, Zhang Y-W. Lattice vibrational modes and phonon thermal conductivity of

monolayer MoS2. Phys. Rev. B 2014;89(3):035438.

[41] Broido DA, Lindsay L, Reinecke TL. Ab initio study of the unusual thermal transport properties of boron arsenide and related materials. Phys. Rev. B 2013;88(21):214303.

[42] Lindsay L, Broido DA. Three-phonon phase space and lattice thermal conductivity in semiconductors. J. Phys.: Condens. Matter 2008;20(16):165209.

[43] Zhang H, Hua C, Ding D, Minnich AJ. Length Dependent Thermal Conductivity Measurements Yield Phonon Mean Free Path Spectra in Nanostructures. Sci. Rep. 2015;5:9121.