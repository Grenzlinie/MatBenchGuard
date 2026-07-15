# The phonon transport properties in cubic graphene with entirely $\text{sp}^2$ hybridization state

Jianhua Zhou $^{a,*}$, Donghua Li $^{b}$

$^{a}$ School of Information Engineering, Shaoyang University, Shaoyang 422000, China
$^{b}$ Office of Journal of Shaoyang University, Shaoyang 422000, China

---

## A R T I C L E  I N F O

**Article history:**
Received 4 March 2021
Received in revised form 30 April 2021
Accepted 3 May 2021
Available online 7 May 2021
Communicated by L.M. Woods

**Keywords:**
Cubic graphene
Phonon transport
Thermal conductivity
First principles calculation

## A B S T R A C T

Cubic graphene is an intrinsic semiconductor with hollow geometric structure and entirely $\text{sp}^2$ hybridization state. In this paper, using first principles calculations, we investigate the phonon transport properties of this novel carbon allotrope. The calculations show that at room temperature the thermal conductivity of cubic graphene is approximately 266.17 W/mK, which is obviously lower than that of diamond with fully $\text{sp}^3$ hybridization state (2033 W/mK). Such low thermal conductivity mainly originated from the distorted $\text{sp}^2$ bond and complex structure which give rise to the flatted and mixed phonon branches as well as strong phonon anharmonicity. Meanwhile, to provide detectable structure fingerprints for experiment, the Raman spectrum and vibrational features of Raman-active phonon modes are also calculated in this work. These results elucidate the intrinsic phonon transport properties of cubic graphene as compared with the case of diamond, and could underpin its potential applications in the field of thermal management.

© 2021 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Thermal transport is the most fundamental physical properties of a material [1-6]. As we know that materials with high thermal conductivity could dissipate the accumulated heat energy in the micro-nano devices effectively and play critical roles in the appli- cation of integrated circuit [1,3]. Materials with low thermal con- ductivity, however, could capture the enormous amount of wasted heat to generate electricity and play important roles in the field of thermoelectric conversion [3,4]. Therefore, deep understanding of heat transport characteristics of materials is one of the key fac- tors for their actual applications, which have attracted tremendous interesting in current theoretical and experimental studies [5-8].

Carbon-based material is one of the current hot spots in the field of materials research. The unique ability of carbon atoms with three hybridization states (sp, $\text{sp}^2$, $\text{sp}^3$) endows them to form a wide variety of allotropes. At ambient conditions graphite formed by $\text{sp}^2$ hybridization states is the thermodynamically most stable carbon allotrope [9]. The diamond formed by $\text{sp}^3$ hybridization states is the hardest known natural material [10]. The cyclo$_{18}$carbon ($\text{C}_{18}$) formed by sp hybridization states is also prepared successfully in experiment [11]. In addition to these synthesized al- lotropes, some novel carbon structures have also been proposed theoretically, such as, M-carbon [12,13], SC24-carbon [14], BC12/8- carbon [15,16], Z-carbon [17,18], P-carbon [19], and rich graphene [20] and graphyne allotropes [21-24]. These carbon phases host fascinating physical and chemical properties and present great po- tential applications in future excellent optoelectronic devices. In recent years, the discovery of fullerene [25], nanotube [26], and graphene [27] has aroused the interests of exploration of carbon structure with all-$\text{sp}^2$ hybridization states. Some carbon networks with entirely $\text{sp}^2$ configuration have been reported as well, e.g., H6-carbon [28], fcc-$\text{C}_{20}$ [29], bct4-carbon [30], K4-carbon [31], and BCO $\text{C}_{16}$ [32]. Owning to the twisted $\pi$ states, most of these three- dimensional (3D) $\text{sp}^2$ carbon allotropes are dynamically unstable. Only the cubic graphene (6.8$^2$ D) is more stable than the fullerene and some of its structure fragments have been successfully syn- thesized [33-36]. However, it is a pity that until now, most of the previous studies on cubic graphene are mainly focused on the crys- tal structures and electronic properties. Systematic studies on the phonon transport properties of cubic graphene are still lacking, and there are no reliable reports on the thermal conductivity and me- chanical performance.

Inspired by these needs, in this paper we investigate the phonon and mechanical properties of cubic graphene by means of first principles calculations. The results show that the room tem- perature of cubic graphene is about 266.17 W/mK, which is almost a magnitude lower than that of diamond with entirely $\text{sp}^3$ hy-

---

* Corresponding author.
E-mail address: zjh598@126.com (J. Zhou).

https://doi.org/10.1016/j.physleta.2021.127410
0375-9601/© 2021 Elsevier B.V. All rights reserved.

![](./images/812454377355739137_1.jpg)
![](./images/812454377355739137_2.jpg)
![](./images/812454377355739137_3.jpg)

![](./images/812454377355739137_4.jpg)

Fig. 1. (a) Schematic representation of cubic graphene super cell (2×2×2), where the yellow balls represent carbon atoms in primitive cell. (b) and (c) The crystalline views of cubic graphene primitive cell from the [001] direction and [111] direction. (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.)

bridization state. Meanwhile, the evaluated Raman spectrum and some typical intrinsic eigenvectors are also provided for identifying the cubic graphene in experiment. The rest of paper is organized as follows. In the next section, we give a brief description about the computational details in this work. In the third section, we present the phonon transport and mechanical properties of cubic graphene. Based on analysis of phonon mode information, we reveal the underline mechanism of such low thermal conductivity of cubic graphene. Finally, our discussions and concluding remarks are summarized in the fourth section.

## 2. Computational details

In this paper, all the calculations are performed within the framework of density functional theory (DFT), as implemented in the Vienna ab initio simulation package (VASP). The exchange-correlation potential is approximated by the generalized gradient approximation (GGA) developed by Perdew et al. [37-39]. The wave functions are expanded by plane-wave basis with the kinetic energy cut-off of 500 eV, and the Brillouin zones of primitive cell of cubic graphene are sampled with Monkhorst-Pack k-meshes of $11 \times 11 \times 11$. The lattice constants and atomic positions are fully optimized through the conjugate gradient algorithm until the maximum residual force on each atom is smaller than $1 \times 10^{-5}$ eV/Å. The phonon transport properties are calculated by means of phonon Boltzmann transport equation (PBTE) as implemented in the ShengBTE package [40] with $2^{nd}$ force constants (IFCs) and $3^{rd}$ IFCs as inputs. The phonon dispersion and $2^{nd}$ IFCs of cubic graphene are calculated via using VASP and PHONONPY packages [41] with $2 \times 2 \times 2$ super cell (192 carbon atoms) and $5 \times 5 \times 5$ k-mesh. Same super cell with cutoff of interaction ranges up to sixth nearest neighbors is adopted for calculating the anharmonic $3^{rd}$ IFCs. Taken the symmetry of cubic graphene into consideration, the total number of displacements is reduced to 120. Meanwhile, we also use the Lagrangian multiplier method to enforce the translational invariance constraint of $2^{nd}$ and $3^{rd}$ IFCs [42]. In order to obtain a convergent value, a dense phonon q-grid of $17 \times 17 \times 17$ is used to evaluate the lattice thermal conductivity of cubic graphene.

## 3. Results and discussion

As shown in Fig. 1, the cubic graphene is pure $sp^{2}$ carbon network with space group $Pn\overline{3}m$ (No. 224), where only one carbon atom occupies the symmetric Wyckoff positions (-0.25000, 0.41328, 0.08672) in each primitive unit cell. The optimized lattice constant of cubic graphene is $a{=}b{=}c{=}6.095$ Å, which agrees well with previous theoretical data [33,43].

Based on the optimized cubic graphene, we calculate the phonon dispersion and present the results in Fig. 2(a). As a comparison, we also plot the phonon spectrum of diamond with full $sp^{3}$ hybridization state (unit cell containing 8 carbon atoms). It can be seen clearly that no imaginary phonon branches are appeared in the phonon dispersion of cubic graphene, implying the dynamical stability of cubic graphene. Meanwhile, the maximum optical phonon branch of cubic graphene could approach 1542 $cm^{-1}$, which is larger than that of diamond (1300 $cm^{-1}$) [44]. Such phenomenon mainly originates from the intrinsic strong performance of $sp^{2}$ hybridization state. Each primitive cell of cubic graphene contains 24 carbon atoms, the corresponding phonon spectrum will possess 3 acoustic and 69 optical phonon branches. Because of such complex geometric structure, one can also note from Fig. 2(a) that the curve of phonon branches in cubic graphene is more flatted than that of diamond. This behavior could also been confirmed from the multiple peaks of phonon density of state (DOS) in cubic graphene shown in the Fig. 2(b). Meanwhile, the mixture among phonon branches in the cubic graphene is quite serious in the whole frequency region, which will play a critical

![](./images/812454377355739137_5.jpg)

Fig. 2. (a) The phonon dispersion of cubic graphene and diamond (unit cell) along several high-symmetry k-points in the first Brillouin Zone. The coordinates of the high-symmetry k-points are as following: X=0.5 0.0 0.0, R=0.5 0.5 0.5, M=0.5 0.5 0.0, G=0.0 0.0 0.0. (b) The phonon density of state of cubic graphene and diamond.

![](./images/812454377355739137_6.jpg)

Fig. 3. (a) The calculated Raman spectrum of cubic graphene. (b)-(d) Three typical Raman-active phonon modes of cubic graphene with frequencies 417.63, 1394.02, and 1504.15 cm⁻¹.

<table>
<caption>Table 1
The calculated lattice constant, Elastic constants Cᵢⱼ (GPa), bulk modulus B (GPa), shear modulus G (GPa), Young's modulus E (GPa), and Poisson's ratio v of cubic graphene and diamond.</caption>
<thead>
<tr>
<th>Materials</th>
<th>a (Å)</th>
<th>C₁₁</th>
<th>C₁₂</th>
<th>C₄₄</th>
<th>B</th>
<th>G</th>
<th>E</th>
<th>v</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cubic graphene</td>
<td>6.095</td>
<td>328</td>
<td>189</td>
<td>160</td>
<td>235</td>
<td>124</td>
<td>190</td>
<td>0.37</td>
</tr>
<tr>
<td>Diamond</td>
<td>3.566</td>
<td>1053</td>
<td>120</td>
<td>563</td>
<td>431</td>
<td>522</td>
<td>1116</td>
<td>0.07</td>
</tr>
</tbody>
</table>

role in determining the phonon transport in cubic graphene and will be explored in the following section.

By utilizing the interface code of Phonopy-Spectroscopy [45], one can calculate the Raman spectrum of cubic graphene. Accord- ing to the group theory prediction there exists following phonon modes at the $\Gamma$ point of the Brillouin Zone: $T_{1u}$, $T_{1g}$, $A_{2u}$, $T_{2g}$, $A_{2g}$, $T_{2u}$, $E_{g}$, $E_{u}$, $A_{1u}$, and $A_{1g}$. Among them the $T_{2g}$, $A_{1g}$, and $E_{g}$ are Raman-active modes. As shown in Fig. 3(a), the Raman- active phonon modes have the frequencies of 417.63, 1394.02, and $1504.15 ~cm^{-1}$ for $T_{2g}, A_{1g}$ , and $E_{g}$ , respectively. These Raman shift peaks could be used as detectable structure fingerprints for iden- tifying the cubic graphene from most other three-dimensional $sp^{2}$ carbon allotropes, e.g., H6-carbon, fcc-C $C_{20}$ , bct4-carbon, and BCO C16. In order to show the characteristics of the three Raman-active phonon modes more clearly, their intrinsic lattice vibrations at the I point are depicted in Figs. 3(b) and (d). Interestingly, it can be seen that in those phonon modes, some carbon atoms stay fixed, while other atoms have a counter phase motion with respect to the neighboring atoms. On considering of these features, these unique Raman-active phonon modes in cubic graphene are likely to be ob- served in experiment.

The elastic properties provide important information about the mechanical stability and the nature of forces operating of mate- rials. Here, we calculate the elastic constants of cubic graphene, together with elastic modulus, which are presented in Table 1. The criteria for mechanical stability of cubic symmetry group are given by: $C_{11}>0, C_{44}>0, C_{11}>|C_{12}|$ , and $(C_{11}+2 C_{12}>0)$ [46]. It is evi dent from Table 1 that the cubic graphene satisfies these criteria mentioned above, demonstrating cubic graphene is mechanically stable under small deformation. Through using Voigt-Reuss-Hill approximations [47,48], the bulk modulus B (describes volumet- ric elasticity) and shear modulus G (describes an object's tendency to shear when acted upon by opposing forces) can be obtained directly from the elastic constants. The Young's modulus E (de- scribes tensile elasticity) and Poisson's ratio v (exhibits the plas- ticity) are expressed as $E=9 B G /(3 B+G)$ and $v=(3 B-2 G) /[2(3 B+G)]$ . From Table 1, one can note clearly that the elastic modulus of cubic graphene is merely a half of that of diamond, while the Poisson's ratio is about five times of the later. Such results indicate that the cubic graphene hosts weak mechanical properties, which might be attributed to the intrinsic bonding feature of $sp^{2}$ and its hollow structure.

![](./images/812454377355739137_7.jpg)

Fig. 4. The contribution of TA1, TA2, LA, and optical phonons (OP) to the total thermal conductivity of cubic graphene as a function of temperature. The thermal conductivity of diamond is plotted as well for comparison.

![](./images/812454377355739137_8.jpg)

Fig. 5. The group velocity (a), phonon relaxation time (b), Grüneisen parameter (c), and phonon phase space (d) as a function of frequency of cubic graphene and diamond.

The lattice thermal conductivity along the $\alpha$ crystal direction $\kappa_{\alpha}$ can be calculated within the framework of Boltzmann equation [40]:

$$
\kappa_{\alpha}=\frac{1}{V} \sum_{\lambda} C_{\lambda} v_{\lambda \alpha}^{2} \tau_{\lambda \alpha} \tag{1}
$$

here V is crystal volume of primitive cell of cubic graphene, $\lambda$ denotes phonon mode index included with both phonon branch and wave vector, $C_{\lambda}$ is the mode dependent heat capacity, $v_{\lambda \alpha}$ and $\tau_{\lambda \alpha}$ represent the group velocity and phonon relaxation time of mode $\lambda$ along $\alpha$ crystal direction. The $C_{\lambda}$ and $v_{\lambda \alpha}$ could be evaluated from the harmonic $2^{\text {nd }}$ IFCs, and the phonon relaxation time which including the information of phonon-phonon scattering can be obtained directly from both $2^{\text {nd }}$ IFCs and $3^{\text {rd }}$ IFCs.

Owing to the intrinsic geometric symmetry, the lattice thermal conductivity in cubic graphene is isotropic (i.e., $\kappa_{x x}=\kappa_{y y}=\kappa_{z z}$ ). Therefore, we only present the lattice thermal conductivity of cubic graphene along xx crystal direction in this work, and the results together with the data of diamond are illustrated in Fig. 4. Obviously, the thermal conductivity of cubic graphene decreases monotonically with temperature, which is mainly attributed to the enhancement of intrinsic phonon scattering with temperature. At room temperature, the calculated lattice thermal conductivity of cubic graphene is about 266.17 W/mK, which is larger than the tradition semiconductor diamond silicon (d-Si, 137 W/mK) [49,50] and almost one order of magnitude lower than that for diamond (2033 W/mK) [44,51]. Moreover, in Fig. 4 we also calculate the contribution of different phonon modes to the lattice thermal conductivity of cubic graphene. Here, the different phonon modes are sorted according to their frequencies, which is also a common treatment method in previous studies [52,53]. It can be found that the three acoustic phonon modes dominate the thermal conductivity in the low temperature (< 200K). As the temperature increases further, however, the contributions came from the optical phonon modes gradually increases. At 600 K, the thermal conductivity contributed from the optical phonon modes is about 38.37 W/mK, which is about 43% of the total lattice thermal conductivity of cubic graphene. This behavior is quite different from the case of diamond [44], where only acoustic phonon modes play vital role on the lattice thermal conductivity.

In order to explore the physical insight of the low thermal conductivity of cubic graphene, we perform further calculations and discussion about the frequency-dependent group velocity and phonon relaxation time of each phonon modes. From the Fig. 5(a) one can see clearly that the phonon group velocities of cubic graphene are significantly lower than that of diamond, which is mainly ascribed to the flatter bands and multiple peaks of phonon DOS existing in the phonon spectrum of cubic graphene shown in Fig. 2. Analogous to the group velocity, obvious reduction of phonon relaxation time could also be found in the cubic graphene. The phonon relaxation time is determined by the scattering strength (characterized by the Grüneisen parameter) and scattering channel/probability (characterized by the phase space). It can be noted from the Fig. 5(c) that the Grüneisen parameter of cubic graphene is obviously larger than that of diamond in the whole frequency region, indicating there exists strong anharmonicity and phonon-phonon scattering. This is in consistent with the intrinsic feature of cubic graphene, where the bonds (including both lengths and angles) are distorted compared to the perfect $\mathrm{sp}^{2}$ hybridization bonds. As shown in Fig. 5(d), the cubic graphene also shows larger phonon scattering phase space.

This can be understood from the phonon spectrum. Just as we mentioned in the above section, the phonon branches of cubic graphene are mixed together serious. In this case, the requirement of energy and momentum conservation for phonon scattering will become more easily, and thus leading to the larger phonon scat- tering phase space. Based on the results presented in Fig. 5, one can get a conclusion that the distorted $sp^{2}$ bonds and complex geometric structure in cubic graphene lead to the strong phonon anharmonicity and flatted and mixed phonon modes, finally gives rise to the low lattice thermal conductivity.

## 4. Discussions and conclusion

In summary, we have investigated the phonon transport and mechanical properties of cubic graphene with fully $sp^{2}$ hybridiza- tion state by means of first principles calculations. The lattice thermal conductivity of cubic graphene at room temperature is about 266.17 W/mK, which is obviously lower than that of di- amond with fully $sp^{3}$ hybridization state. Owing to the intrinsic distorted $sp^{2}$ bond, the mechanical performance of cubic graphene is also weaker than that of diamond. To understand the under- line mechanism of the low thermal conductivity, we examined the phonon mode properties. The results revealed that the com- bined effect of small group velocity caused by the flatted phonon branches and strong phonon scattering including both strength and channels results in the low lattice thermal conductivity of cubic graphene. Moreover, the Raman spectrum and the corresponding Raman-active phonon modes are illustrated as well for provid- ing experimental detectable structure fingerprints. The information presented in this work shed light on the intrinsic phonon and me- chanical properties of cubic graphene, and could offer theoretical guidance for the thermal management of cubic graphene-based de- vices.

### CRediT authorship contribution statement

Jianhua Zhou: Writing-original draft, Model design, Theoreti- cal analysis, and Simulation. Donghua Li: Validation and Writing- review and editing.

### Declaration of competing interest

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Data availability

The data used to support the findings of this study are available from the corresponding author upon request.

### Acknowledgement

This work is supported by the Scientific Research Fund of Hu- nan Provincial Education Department (Grant No. 20A449) and Sci- entific research projects of Shaoyang science and Technology Bu- reau (Grant No. 2020GZ90).

### References

[1] E. Pop, S. Sinha, K.E. Goodson, Proc. IEEE 94 (2006) 1587-1601.
[2] N.P. Padture, M. Gell, E.H. Jordan, Science 296 (2002) 280.
[3] L.E. Bell, Science 321 (2008) 1457.
[4] G.J. Snyder, E.S. Toberer, Nat. Mater. 7 (2008) 105-114.
[5] D.G. Cahill, W.K. Ford, K.E. Goodson, G.D. Mahan, A. Majumdar, H.J. Maris, R. Merlin, S.R. Phillpot, J. Appl. Phys. 93 (2002) 793-818.
[6] Q. Chen, L.-M. Tang, K.-Q. Chen, Z.-K. Zhao, J. Appl. Phys. 114 (2013) 084301.
[7] G. Xie, Z. Ju, K. Zhou, X. Wei, Z. Guo, Y. Cai, G. Zhang, npj Comput. Mater. 4(2018) 21.
[8] G. Xie, D. Ding, G. Zhang, Adv. Phys.: X 3 (2018) 1480417.
[9] E.D. Miller, D.C. Nesting, J.V. Badding, Chem. Mater. 9 (1997) 18-22.
[10] A.J. Neves, Properties, Growth and Applications of Diamond, INSPEC, 2001.
[11] K. Kaiser, L.M. Scriven, F. Schulz, P. Gawel, L. Gross, H.L. Anderson, Science 365(2019) 1299.
[12] Q. Li, Y. Ma, A.R. Oganov, H. Wang, H. Wang, Y. Xu, T. Cui, H.-K. Mao, G. Zou, Phys. Rev. Lett. 102 (2009) 175506.
[13] A.R. Oganov, C.W. Glass, J. Chem. Phys. 124 (2006) 244704.
[14] J.-T. Wang, C. Chen, Y. Kawazoe, Phys. Rev. B 85 (2012) 214104.
[15] Z.-Z. Li, C.-S. Lian, J. Xu, L.-F. Xu, J.-T. Wang, C. Chen, Phys. Rev. B 91 (2015)214106.
[16] M.D. Knudson, M.P. Desjarlais, D.H. Dolan, Science 322 (2008) 1822.
[17] M. Amsler, J.A. Flores-Livas, L. Lehtovaara, F. Balima, S.A. Ghasemi, D. Machon, S. Pailhès, A. Willand, D. Caliste, S. Botti, A. San Miguel, S. Goedecker, M.A.L. Marques, Phys. Rev. Lett. 108 (2012) 065501.
[18] Z. Zhao, B. Xu, X.-F. Zhou, L.-M. Wang, B. Wen, J. He, Z. Liu, H.-T. Wang, Y. Tian, Phys. Rev. Lett. 107 (2011) 215502.
[19] C. He, L. Sun, C. Zhang, X. Peng, K. Zhang, J. Zhong, Phys. Chem. Chem. Phys.14 (2012) 8410-8414.
[20] H. Yin, X. Shi, C. He, M. Martinez-Canales, J. Li, C.J. Pickard, C. Tang, T. Ouyang, C. Zhang, J. Zhong, Phys. Rev. B 99 (2019) 041405.
[21] P. Yan, T. Ouyang, C. He, J. Li, C. Zhang, C. Tang, J. Zhong, Nanoscale 13 (2021)3564-3571.
[22] T. Ouyang, C. Cui, X. Shi, C. He, J. Li, C. Zhang, C. Tang, J. Zhong, Phys. Status Solidi (RRL) - Rapid Res. Lett. (2020) 2000437.
[23] V. Georgakilas, J.A. Perman, J. Tucek, R. Zboril, Chem. Rev. 115 (2015)4744-4822.
[24] Y. Lin, Z. Zhao, T.A. Strobel, R.E. Cohen, Phys. Rev. B 94 (2016) 245422.
[25] H.W. Kroto, J.R. Heath, S.C. O'Brien, R.F. Curl, R.E. Smalley, Nature 318 (1985)162-163.
[26] S. Iijima, Nature 354 (1991) 56-58.
[27] A.K. Geim, K.S. Novoselov, Nat. Mater. 6 (2007) 183-191.
[28] A.Y. Liu, M.L. Cohen, K.C. Hass, M.A. Tamor, Phys. Rev. B 43 (1991) 6742-6745.
[29] M. Côté, J.C. Grossman, M.L. Cohen, S.G. Louie, Phys. Rev. B 58 (1998) 664-668.
[30] R. Hoffmann, T. Hughbanks, M. Kertesz, P.H. Bird, J. Am. Chem. Soc. 105 (1983)4831-4832.
[31] M. Itoh, M. Kotani, H. Naito, T. Sunada, Y. Kawazoe, T. Adschiri, Phys. Rev. Lett.102 (2009) 055703.
[32] J.-T. Wang, H. Weng, S. Nie, Z. Fang, Y. Kawazoe, C. Chen, Phys. Rev. Lett. 116(2016) 195501.
[33] M. O'Keeffe, G.B. Adams, O.F. Sankey, Phys. Rev. Lett. 68 (1992) 2325-2328.
[34] X. Shen, D.M. Ho, R.A. Pascal, Org. Lett. 5 (2003) 369-371.
[35] X. Shen, D.M. Ho, R.A. Pascal, J. Am. Chem. Soc. 126 (2004) 5798-5805.
[36] B. Winkler, C.J. Pickard, V. Milman, W.E. Klee, G. Thimm, Chem. Phys. Lett. 312(1999) 536-541.
[37] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.
[38] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758-1775.
[39] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953-17979.
[40] W. Li, J. Carrete, N.A. Katcho, N. Mingo, Comput. Phys. Commun. 185 (2014)1747-1758.
[41] A. Togo, I. Tanaka, Scr. Mater. 108 (2015) 1-5.
[42] W. Li, L. Lindsay, D.A. Broido, D.A. Stewart, N. Mingo, Phys. Rev. B 86 (2012)174307.
[43] C. He, L. Sun, C. Zhang, J. Zhong, Phys. Chem. Chem. Phys. 15 (2013) 680-684.
[44] S.-Y. Yue, G. Qin, X. Zhang, X. Sheng, G. Su, M. Hu, Phys. Rev. B 95 (2017)085207.
[45] J.M. Skelton, L.A. Burton, A.J. Jackson, F. Oba, S.C. Parker, A. Walsh, Phys. Chem. Chem. Phys. 19 (2017) 12452-12465.
[46] Q. Wei, Q. Zhang, M. Zhang, Materials 9 (2016).
[47] R. Hill, Proc. Phys. Soc. A 65 (1952) 349-354.
[48] A. Reuss, ZAMM - J. Appl. Math. Mech. / Z. Angew. Math. Mech. 9 (1929) 49-58.
[49] A. Jain, A.J.H. McGaughey, Comput. Mater. Sci. 110 (2015) 115-120.
[50] T. Ouyang, P. Zhang, H. Xiao, C. Tang, J. Li, C. He, J. Zhong, J. Phys. D: Appl. Phys.50 (2017) 425501.
[51] D.A. Broido, L. Lindsay, A. Ward, Phys. Rev. B 86 (2012) 115203.
[52] H. Xie, M. Hu, H. Bao, Appl. Phys. Lett. 104 (2014) 131906.
[53] X. Gu, R. Yang, J. Appl. Phys. 117 (2015) 025102.