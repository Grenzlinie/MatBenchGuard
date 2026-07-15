# Jahn-Teller distortion affected Li ion migration in spinel TiO₂

Fanghua Ning^(a,b), Hewen Wang^a, Bo Xu^b, Chuying Ouyang^(a,b,*)

^a College of Chemistry and Chemical Engineering, Huanggang Normal University, Huanggang 438000, China
^b Department of Physics, Laboratory of Computational Materials Physics, Jiangxi Normal University, Nanchang 330022, China

---

## ARTICLE INFO
**Keywords:**
Jahn-Teller distortion
Li-ion battery
Li ion migration
First-principles calculation

## ABSTRACT
In this paper, we study the effect of the Jahn-Teller (JT) distortion on the Li ion migration energy barrier in spinel TiO₂ by using first-principles calculations. Our results show that the JT distortion can be beneficial and harmful, and unaffected to the Li ion migration, depending on the Li ion migration pathway and the orientation of the JT distortion. Bond length analysis demonstrates that the JT distortion of the Ti³⁺O₆ octahedron causes the variation of the linked Li–O bond lengths and the corresponding Li–O Coulomb energies, thus resulting in the diversity of Li ion migration barrier. In the lithiated LiTi₂O₄ state, the Li vacancy migration is also sub-stantially affected by the JT distortion, while the influence of the JT distortion is much more complicated as more Ti³⁺ ions are created and the distribution of them is random. Our results are helpful to reveal the mechanism of Li ion migration in the spinel structures with JT distortions.

---

### 1. Introduction

Spinel LiTi₂O₄ is a new promising anode in lithium ion batteries (LIBs) after carbon based components and Li₄Ti₅O₁₂ [1–2]. To be an anode material, Li ion migration is of importance to the performance of the rate capability [3–5]. Li ion migration is a complicated problem that depends on factors like the migration pathway, the space of the host structure that accommodates the Li ion, the variety of the electrostatic field surrounding the Li ion, and so on. Unfortunately, limited studies [6–8] on the factor determining the Li ion migration in spinel LiTi₂O₄ have been reported. Therefore, the Li ion migration in spinel LiTi₂O₄ needs further investigation.

Recently, the strong influence of Jahn-Teller (JT) distortion on Li ion migration has been found in another spinel structure λ-MnO₂, which is the fully delithiated spinel LiMn₂O₄ cathode material [9]. Since the structure of the spinel TiO₂ (fully delithiated spinel LiTi₂O₄) is like that of λ-MnO₂, whether the JT distortion is also the essential factor that affects the Li ion migration in spinel TiO₂ could also be of interest. In this work, we mainly focused on the effect of JT distortion of the Ti³⁺O₆ octahedron on Li ion migration. Our results are helpful to reveal the mechanism of the Li ion migration in spinel LiTi₂O₄ and therefore we can have a better understanding of the rate performance of the material as electrodes for Li ion batteries.

### 2. Computational details

All calculations were performed using the Vienna Ab-initio Simulation Package (VASP) [10]. A plane-wave basis set with the projector augmented wave (PAW) method [11] and the spin-polarized generalized gradient approximation (GGA) with the Perdew-Wang (PW91) [12] exchange-correlation functional are used. The original structure of spinel TiO₂ is modeled with a supercell of 16 TiO₂ formula units. The Monkhorst-Pack scheme [13] with 3 × 3 × 3 k-points mesh and the cutoff energy of 450 eV are employed. The atomic structure is fully relaxed until the final forces on each atom less than 0.01 eV/Å. The Li ion/vacancy migration pathways are optimized by using the climbing image nudged elastic band (CINEB) method [14–15].

In order to localize one electron to a specific Ti-3d orbital, GGA + U method [16–17] is used to account for the strong onsite Coulomb repulsion of Ti-3d electrons and the U_eff of the Ti-3d is chosen to be 5.0 eV [18]. In addition to the GGA + U, some technical treatment is neces-sary to obtain the JT distorted structure and the localized Ti-3d electron. If the initial atomic structure is not distorted, the electron will distribute to all Ti atoms in the unitcell and the electronic structure of the system is metallic. In this case, the JT distortion cannot be observed and the total energy of the system is high. In order to reproduce the JT-distortion, the initial target Ti³⁺O₆ structure should be distorted manually before relaxing the atomic structures. Therefore, the initial bond lengths of the Ti³⁺O₆ are adjusted according to the Ti-3d states in an octahedral crystal field. Then relaxation of the atomic structure will further optimize the local atomic structures and the JT-distorted structure can be obtained, as well as the lowered total energy of the system. We also mention here the Ti³⁺ is not changed during the NEB calculation, which was monitored directly by checking the magnetic

---

* Corresponding author at: College of Chemistry and Chemical Engineering, Huanggang Normal University, Huanggang 438000, China.
E-mail address: cyouyang@jxnu.edu.cn (C. Ouyang).

http://dx.doi.org/10.1016/j.ssi.2017.10.002
Received 24 July 2017; Received in revised form 4 October 2017; Accepted 5 October 2017
0167-2738/ © 2017 Published by Elsevier B.V.

![](./images/813093282702688256_1.jpg)

Fig. 1. Schematic view of the atomic structure of the spinel TiO₂. The black octahedrons are Ti-centered TiO₆ octahedrons.

moment of the Ti atoms.

## 3. Results and discussions

The optimized atomic structure of spinel TiO₂ is shown in Fig. 1. The lattice parameters are $a = b = c = 8.515$ Å, $\alpha = \beta = \gamma = 90^\circ$, which are in well agreement with other report [8]. Here each Ti ion is surrounded by six O ions forming a TiO₆ octahedron. All Ti ions in the spinel TiO₂ are Ti⁴⁺. Six Ti-O bonds in TiO₆ octahedron are equal with the length of 2.010 Å.

Then we move to study Li ion migration in spinel TiO₂. When one single Li atom is introduced into the lattice, the total energy calculations suggest that the Li ion prefers to locate at the tetrahedral site. Therefore, in our calculations Li ion migrate from one tetrahedral site (initial state, IS) through octahedral site (transition state, TS) to an adjacent tetrahedral site (final state, FS), as is shown in Fig. 2a. At the TS, Li ion in the LiO₆ octahedral centre is surrounded by six Ti ions forming a Ti₆-ring with the plane vertical to the Li ion migration pathway. Once a Li atom is introduced to the system, one Ti⁴⁺ ion changes into Ti³⁺ ion. Ti³⁺ ion (3d¹) is JT active, which results in elongation Ti-O bonds of the TiO₆ octahedron in certain directions, depending on which orbital of the Ti-3d is occupied by the electron. We have three kinds of Ti³⁺ ion based on their relative locations to the Li migration pathway, marked as Tiᵢ, Tiᵢᵢ, and Tiᵢᵢᵢ in Fig. 2a. The periodic boundary conditions are also included when these Ti sites are considered. Tiᵢ is right above the Li ion at the TS (along c-axis in Fig. 2a), which is near the migrating Li and locates at the extension line of Li-O bond (Li⁺ at the TS). Tiᵢᵢ is the furthest Ti ion away from the migrating Li. Tiᵢᵢᵢ is one of the six Ti ions in the Ti₆-ring, which is also near the migrating Li. We simulated Li ion migration along the same pathway for the three cases, named Tiᵢ³⁺, Tiᵢᵢ³⁺, and Tiᵢᵢᵢ³⁺ cases. In addition, another case (All-Ti⁴⁺) is employed for comparison. In All-Ti⁴⁺ case, the excess electron is taken away from the system, namely, one Li⁺ rather than Li atom is introduced into the system. Therefore, all Ti ions remain the valence states of + 4, indicating that no JT distortion occurs.

The energy profiles along the optimized Li ion migration pathway are shown in Fig. 2b. As it is shown, the energy profiles are symmetric, indicating that the pathway is symmetric to the Ti³⁺ ions for all cases. Here we mention that the symmetry is dependent on the periodic boundary conditions we used. As it can be seen, the periodic boundary condition does not change the total energy and therefore symmetric energy profiles are observed. The migration barriers for Tiᵢ³⁺, Tiᵢᵢ³⁺, Tiᵢᵢᵢ³⁺, and All-Ti⁴⁺ cases are 0.480, 0.595, 0.636, and 0.602 eV, respectively. This means that the migration barriers are sensitive to the position of Ti³⁺ ion. Comparing with the All-Ti⁴⁺ case without JT distortion, we can find a similar barrier for Tiᵢᵢ³⁺ case, and lower barrier for Tiᵢ³⁺ case, while higher barrier for Tiᵢᵢᵢ³⁺ case. These results are qualitatively consistent with that of λ-MnO₂ [9].

![](./images/813093282702688256_2.jpg)

Fig. 2. The migration pathways and the positions of Tiᵢ, Tiᵢᵢ and Tiᵢᵢᵢ, with Ti₆-ring zoomed in on the left-hand side (a), and the energy profiles of Li ion migration for Tiᵢ³⁺, Tiᵢᵢ³⁺, Tiᵢᵢᵢ³⁺ and All-Ti⁴⁺ cases (b).

When the valence state of the Ti atom changes from Ti⁴⁺ into Ti³⁺, JT distortion occurs to the objective Ti³⁺O₆ octahedron structure and a polaron state is formed around the Ti³⁺. The polaron state is negatively charged and therefore it will have attractive interactions with the positively charge Li⁺ ion. Namely, the Li⁺ and the polaron state traps to each other. As a result, the total energy of the system is low when the distance between the Li⁺ and the Ti³⁺O₆ is short, while the total energy is higher when the distance is long. This trapping effect will influence the Li diffusion. However, our results show that the influence is quite small, as the magnitude of the trapping energy is much smaller comparing with the Li migration energy barrier. Table 1 gives the total energy of the system with Li located at the initial and final states for cases of the trivalent Ti³⁺ located at Tiᵢ, Tiᵢᵢ, and Tiᵢᵢᵢ sites. The Li⁺-Ti³⁺ distance is ~ 3.5 Å for cases of Tiᵢ, and Tiᵢᵢᵢ sites, while it is ~ 5.7 Å for cases of Tiᵢᵢ. As it is shown in Table 1, the energy difference is only ~ 20 meV for the three cases, although the Li⁺-Ti³⁺ distance differs substantially. This energy difference is much smaller comparing with the Li migration energy barriers (480 meV to 636 meV), showing that the trapping effect is negligible to the Li diffusion.

It is easy to accept that the Tiᵢᵢ³⁺ case has the similar migration barrier with that of the All-Ti⁴⁺ case, because the influence of Ti³⁺ ion could be ignored when the Ti³⁺ ion is relatively far away from the migrating Li ion. However, the Tiᵢ³⁺ and Tiᵢᵢᵢ³⁺ cases are more

<table>
<caption>Table 1
The total energies of the initial/final states for Li migration for Tiᵢ³⁺, Tiᵢᵢ³⁺, and Tiᵢᵢᵢ³⁺ cases.</caption>
<thead>
<tr>
<th>Cases</th>
<th>Energy of the IS (eV)</th>
<th>Energy of the FS (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tiᵢ³⁺</td>
<td>− 369.522</td>
<td>− 369.522</td>
</tr>
<tr>
<td>Tiᵢᵢ³⁺</td>
<td>− 369.505</td>
<td>− 369.506</td>
</tr>
<tr>
<td>Tiᵢᵢᵢ³⁺</td>
<td>− 369.526</td>
<td>− 369.526</td>
</tr>
</tbody>
</table>

![](./images/813093282702688256_3.jpg)

![](./images/813093282702688256_4.jpg)

Fig. 3. (a) The average Li-O distances at the TS as well as the corresponding migration barriers in $Ti_{I}^{3+}$, $Ti_{II}^{3+}$, $Ti_{III}^{3+}$ and All-Ti$^{4+}$ cases; (b) Local atomic structures of $LiO_{6}$ octahedron with the linked $Ti^{3+}$-centered $Ti^{3+}O_{6}$ octahedron at the TS for $Ti_{I}^{3+}$ case and $Ti_{III}^{3+}$ case. The green arrows indicate the variation of Ti-O bond length for Ti$^{4+}$ ion changing into $Ti^{3+}$. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

complicated. The differences of the migration barriers for the four cases are brought by $Ti^{3+}$ ion, more specifically by the JT distortion of $Ti^{3+}O_{6}$ octahedron. The JT distortion of $Ti^{3+}O_{6}$ octahedron changes the Li-O distances. As O atoms are the nearest atoms to the migrating Li ion regardless of Li in $LiO_{4}$ tetrahedron at IS/FS or in $LiO_{6}$ octahedron at the TS, the Li-O Coulomb interaction energy should essentially affect the Li ion migration barrier. Thus, the Li-O distances are carefully studied. Since migration barrier is the difference of total energy between the TS and the IS/FS, we focused on the average Li-O distances at both the TS and the IS/FS. For the IS/FS, the average Li-O distances in $LiO_{4}$ tetrahedron in $Ti_{I}^{3+}$, $Ti_{II}^{3+}$, and $Ti_{III}^{3+}$ cases are very close, which are 2.011, 2.005 and 2.011 Å respectively. For the TS, however, the average Li-O distances in $LiO_{6}$ octahedron in $Ti_{I}^{3+}$, $Ti_{II}^{3+}$, and $Ti_{III}^{3+}$ cases vary considerably, which are 2.193, 2.212 and 2.223 Å, respectively. The main differences among the three cases are the average Li-O distances of $LiO_{6}$ octahedron at the TS. The average Li-O distances at the TS as well as the corresponding migration barriers in the three cases are plotted in Fig. 3a. Obviously, the trend of the migration barriers meets very well with that of the average Li-O distances at the TS. Therefore, the change of Li migration barrier should originate from the variation of the average Li-O distance induced by the JT distortion of Li-O distance. It is the different average Li-O distance that leads to the different Coulomb energy, thus migration barrier eventually.

To find the relationship between the JT distortion and the variation of average Li-O distances, we analyzed the local structures of $LiO_{6}$ octahedron with the linked $Ti^{3+}O_{6}$ octahedron at the IS and the TS for the $Ti_{I}^{3+}$, $Ti_{II}^{3+}$, $Ti_{III}^{3+}$ and All-Ti$^{4+}$ cases (see Fig. 3b). Taken the $Ti_{I}^{3+}$, and $Ti_{III}^{3+}$ for example, the green arrows in Fig. 3b show the variation of Ti-O bond length when $Ti^{4+}$ transforming into $Ti^{3+}$. In the $Ti_{I}^{3+}$ case, the elongated Ti-O bonds are quasi-collinear with the linked Li-O bond, thus compressing the linked Li-O bond. In this situation, a lower Li-O Coulomb energy at the TS occurs, consequently lowering the migration barrier. By contrast, in the $Ti_{III}^{3+}$ case, the elongated Ti-O bonds are approximately vertical to the linked Li-O bonds, hence increasing the distance of the linked Li-O bonds. Likewise, a higher Li-O Coulomb energy at the TS means the higher migration barrier. Thus, we shed light on how the JT distortion changes the Li-O distance at the TS, and proving that the average Li-O distance is a good index to describe the Li migration barrier in spinel $TiO_{2}$.

From the above discussions, it is clear that Li migration in the spinel $TiO_{2}$ is substantially affected by the JT distortion. However, the Li concentration is small in the model as there is only one Li atom in the unitcell and thus one JT distorted $Ti^{3+}O_{6}$ octahedron is considered. When more Li atoms are intercalated into the spinel $TiO_{2}$ lattice, more $Ti^{4+}$ will change into $Ti^{3+}$. After all the tetrahedral sites (8a sites) are occupied with Li, the stoichiometry of the spinel structure becomes $LiTi_{2}O_{4}$ and half of the Ti ions are JT active $Ti^{3+}$. As JT distortion affects Li migration substantially, it is expected that the influence of the JT distortion to the Li vacancy migration is also important in $LiTi_{2}O_{4}$. However, as the concentration of the $Ti^{3+}$ is high, the influence can be much more complicated in the case of $LiTi_{2}O_{4}$. First of all, the distribution of the $Ti^{3+}$ in the unitcell will be the most important factor to influence the Li diffusion, since the migration energy barrier is directly associated with the relative location of the migration pathway and the $Ti^{3+}$. However, the distribution of the $Ti^{3+}$ in the $LiTi_{2}O_{4}$ is not clear in literature. At room temperature, the distribution could be random as no charge ordering is observed. This is similar to the case of $LiMn_{2}O_{4}$ spinel, in which the $Mn^{3+}$ ions also distribute randomly in the unitcell under room temperature and therefore cubic lattice is observed experimentally [19]. Therefore, Li vacancy migration in the $LiTi_{2}O_{4}$ could be very complicated. As a compromise and to have a gloss view on how the JT distortion affected the Li vacancy migration in $LiTi_{2}O_{4}$, we build a model of the $LiTi_{2}O_{4}$ with $Ti^{3+}$ ions randomly distributed in the lattice, as shown in Fig. 4a, and studied the Li vacancy migration within this model. Four Li vacancy migration pathways are selected arbitrary as denoted in the Fig. 4a. The relative location of the migration pathway and the $Ti^{3+}$ in the model is different for the considered four pathways, which are optimized with the CINEB method. The Li vacancy migration energy profiles are given in Fig. 4b. The energy barriers are 0.635, 0.335, 0.607 and 0.245 eV for migration pathways from 1 to 4, respectively. As the choice of the migration pathways is arbitrary and the $Ti^{3+}$ distribution is random, the energy barriers can only give a cursory evaluation on how the JT distortion affected the Li vacancy migration. Nevertheless, from the energy barrier values, we can conclude that JT distortion has strong influence to the Li diffusion, since the energy barrier for certain pathway can be lowered substantially to as low as ~0.25 eV.

Finally, it would be interesting to know if it is possible that the charge localized on $Ti^{3+}$ (or more specifically the polaron state) also migrates with Li. It is reported that the energy barrier for a polaron migration in the $LiMn_{2}O_{4}$ spinel ranges from 0.22 to 0.45 eV [20], and it might be similar in the case of $LiTi_{2}O_{4}$ spinel. The migration of the polaron states might be affected by the migration of the Li ions. As discussed above, the trapping energy between the Li ion and the polaron state is small and lower than the polaron migration energy barriers, it is expected that the polaron state does not migrate with Li. However, if we need to evaluate accurate Li ion migration energy barriers, the interaction between the polaron state and the Li ion should

![](./images/813093282702688256_5.jpg)

Fig. 4. (a) The $LiTi_2O_4$ model with four Li vacancy migration pathways denoted with arrows. The large purples, middle sized (green for $Ti^{3+}$ and gray for $Ti^{4+}$), and small red spheres are Li, Ti and O atoms, respectively; (b) Li vacancy migration energy profiles along four pathways optimized with CINEB calculations. The colors of the arrows denoting the migration pathways in (a) are in accordance with the colors of the line in (b). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

be considered.

## 4. Conclusions

In summary, Li ion migration in spinel $TiO_2$ is studied by first-principles calculations. We found that the JT distortion obviously affect the activation barrier of Li ion migration in spinel $TiO_2$. Three kinds of results could be found, which are beneficial, harmful, and unaffected to the Li ion migration. Further analysis shows that the influence of JT distortion on migration barriers is related to the average Li-O distances during the migration progress. It is the JT distortion that causes the different Li-O distances and the variation of Li-O Coulomb energy, thus resulting in the different migration energy barriers. The energy barriers of the vacancy migration in the $LiTi_2O_4$ also confirmed the strong influence of the JT distortion to the Li diffusion.

## Acknowledgments

This work was financially supported by the National Natural Science Foundation of China (Grant Nos. 11664012, 11564016), the Natural Science Foundation of Jiangxi Province of China (Grant Nos. 20171BCB23035, 20152ACB21014, 20151BAB202006). The computations were partly performed on TianHe-1(A) at the National Supercomputer Center in Tianjin.

## References

[1] K.M. Colbow, J.R. Danh, R.R. Haering, J. Power Sources 26 (1989) 397-402.
[2] D.C. Johnston, H. Prakash, W.H. Zachariasen, R. Viswanathan, Mater. Res. Bull. 8 (1973) 777-784.
[3] M.G.S.R. Thomas, P.G. Bruce, J.B. Goodenough, Solid State Ionics 18 (1986) 794-798.
[4] H. Yang, H.J. Bang, J. Prakash, J. Electrochem. Soc. 151 (2004) A1247-A1250.
[5] K. Kang, G. Ceder, Phys. Rev. B 74 (2006) 094105.
[6] J. Sugiyama, H. Nozaki, I. Umegaki, K. Miwa, et al., Phys. Rev. B 92 (2015) 014417.
[7] J. Bhattacharya, A. Van der Ven, Phys. Rev. B 81 (2010) 104304.
[8] Y.H. Liu, J.Y. Wu, W. Zhao, J.L. Chu, T. Qi, Chin. J. Chem. 31 (2013) 1257-1262.
[9] F.H. Ning, B. Xu, J. Shi, H.B. Su, M.S. Wu, G. Liu, C.Y. Ouyang, J. Mater. Chem. A 5 (2017) 9618-9626.
[10] G. Kresse, J. Furthmuller, Phys. Rev. B 54 (1996) 11169.
[11] G. Kresse, J. Joubert, Phys. Rev. B 59 (1999) 1758.
[12] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671.
[13] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[14] G. Henkelman, H. Jonsson, J. Chem. Phys. 113 (2000) 9978-9985.
[15] G. Henkelman, B.P. Uberuaga, H. Jonsson, J. Chem. Phys. 113 (2000) 9901-9904.
[16] V.I. Anisimov, J. Zaanen, O.K. Andersen, Phys. Rev. B 44 (1991) 943.
[17] V.I. Anisimov, F. Aryasetiawan, A.I. Lichtenstein, J. Phys. Condens. Matter 9 (1997) 767-808.
[18] S. Tanaka, M. Kitta, T. Tamura, Y. Maeda, T. Akita, M. Kohyama, J. Mater. Sci. 49 (2014) 4032-4037.
[19] J. Rodriguez-Carvajal, G. Rousse, C. Masquelier, M. Hervieu, Phys. Rev. Lett. 81 (1998) 4660-4663.
[20] C.Y. Ouyang, Y.L. Du, S.Q. Shi, M.S. Lei, Phys. Lett. A 373 (2009) 2796-2799.