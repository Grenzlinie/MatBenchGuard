# Torsional characteristics of graphene nanoribbons encapsulated in single-walled carbon nanotubes

Te-Hua Fang $^{a}$, Win-Jin Chang $^{b, *}$, Yu-Lun Feng $^{a}$, Deng-Maw Lu $^{c}$

$^{a}$ Department of Mechanical Engineering, National Kaohsiung University of Applied Sciences, Kaohsiung 807, Taiwan, ROC
$^{b}$ Department of Mechanical Engineering, Kun Shan University, Tainan 710, Taiwan, ROC
$^{c}$ Department of Mechanical Engineering, Southern Taiwan University of Science and Technology, Tainan 710, Taiwan, ROC

---

### HIGHLIGHTS
- MD simulation was used study the torsional characteristics of a GNR@SWCNT.
- The shear stress increased with an increase in the twist angle before breaking.
- GNR@SWCNT endured a smaller twist angle than a single SWCNT.
- GNR@SWCNT fractured easily at a higher temperature.

---

### ARTICLE INFO
**Article history:**
Received 1 January 2016
Received in revised form
30 April 2016
Accepted 3 May 2016

**Keywords:**
Graphene nanoribbons
Single-walled carbon nanotubes
Torsion characteristics
Molecular dynamics simulations

---

### ABSTRACT
Molecular dynamics (MD) simulations were performed to study the torsional characteristics of a graphene nanoribbon encapsulated in a single-walled carbon nanotube (GNR@SWCNT) with different chiralities at different temperatures. Based on the simulations, the relationship between the shear stress and the twist angle was obtained. The maximum shear stress increases with an increase in chirality. However, the corresponding twist angle decreases with increasing chirality. GNR@SWCNT withstands a smaller twist angle compared with a single SWCNT. In addition, the interaction force between the GNR and the SWCNT increases with increasing temperature. GNR@SWCNT at an elevated temperature is easier to break during torsion with a lower twist angle. The results are valuable for the design of nanocomposites composed of carbon nanotubes and graphene materials.

© 2016 Published by Elsevier B.V.

---

## 1. Introduction
Over the last several years, carbon nanotubes (CNTs) and graphene nanoribbons (GNRs) have attracted great interest from all over the world because of their potential applications in nanotechnology [1–4]. Nanocomposites composed of CNTs, GNRs, and other nanomaterials have also attracted much attention [5–7]. This is because nanocomposites are expected to possess novel mechanical, electrical, and thermal properties.

CNTs filled with nanomaterials such as nanoparticles and nanowires have been intensively studied for potential applications in nanoelectronic devices, nanosensors, and nanobiotechnology. In addition, owing to the fact that experiments at the nanoscale are extremely difficult, molecular dynamics (MD) simulations are often used to explore the physical characteristics of CNTs filled with nanomaterials [8–12]. For example, Wu et al. [10] investigated the mechanical characteristics of a SWCNT filled with $C_{60}$ fullerene using MD simulations. They determined that the loading force, Young's modulus, elastic energy, and plastic energy of a $C_{60}$-filled CNT were proportional to the indentation velocity and tip size. Wu et al. [11] performed MD simulations to study the mechanical properties of Si-nanowire@CNT and found that Si nanowire is not coaxial with CNTs.

In addition, the physical and structural characteristics of GNRs encapsulated in CNTs have been increasingly studied. For example, Talyzin et al. [13] synthesized GNRs encapsulated in SWCNTs (GNR@SWCNT) and explored the electronic structure of the system. Lebedeva et al. [14] studied the structure and electronic properties of a sulfur-terminated zigzag GNR inside CNTs using calculations in the framework of dispersion-corrected density functional theory. Mandal et al. [15] utilized the self-consistent charge density-functional tight-binding method to study the energetic and electronic structure of encapsulated GNRs in CNTs and

---
*Corresponding author.
E-mail address: changwj@mail.ksu.edu.tw (W.-J. Chang).

http://dx.doi.org/10.1016/j.physe.2016.05.006
1386-9477/© 2016 Published by Elsevier B.V.

Please cite this article as: T.-H. Fang, et al., Physica E (2016), http://dx.doi.org/10.1016/j.physe.2016.05.006

found that the nanocomposites have higher hydrogen adsorption characteristics than the individual components, and that hydrogen adsorption is efficient only at high hydrogen concentrations.

Zhang et al. [16] investigated the elastic response of CNTs in torsion through a density-functional-based tight-binding model and obtained that the band gap of CNTs is dominated by rippling. SWCNTs are prone to significant rippling with the smaller diameter tubes being more stable than larger ones. Nikiforov et al. [17] studied the torsional deformation of freestanding GNRs with hydrogen (H) and fluorine (F) armchair edges. They found that the F-GNR tends to form a helix with a smaller radius even at higher twist rates and then it is more prone to helical packing into CNTs with narrow diameters.

The earlier reports mentioned above focused on the structural and electronic characteristics of a GNR@CNT. To our knowledge, only a few studies have been reported on the mechanical characteristics of nanocomposites. Recently, Fang et al. [18] performed MD simulations to investigate the superelastic property of a GNR@SWCNT using the nanoindentation technique. They found that GNR@SWCNT has a $> 15\%$ rate of springback, exhibiting a superelastic nanocomposite behavior. In this article, the torsional mechanical properties of GNR@SWCNT are studied. In addition, the effects of different sizes and temperatures on the torsional characteristics are examined.

## 2. Simulation method

A schematic of the MD model for an armchair graphene nanoribbon with a horizontal configuration encapsulated in a suspended SWCNT with length $L=15$ nm is illustrated in Fig. 1. Five layers of atoms at both ends of the suspended SWCNT were fixed. Four layers of thermostat atoms that obey Newton's second law close to the fixed layers were set to dissipate any excess heat generated during the torsion period. A constant angular velocity of $\pi/180$ rad/ps was used for the torsion test. Constant-temperature simulations at 300 K were performed using a simple velocity scaling thermostat for temperature control. The GNR@SWCNT was subjected to unilateral torsion performed with clockwise rotation until failure. The twist applied to the carbon nanotube and transmitted to the graphene ribbon via van der Waals forces.

MD simulations with different potentials were used to study the mechanical characteristics of the GNR@SWCNT by solving the Hamilton equations of motion using Gear's fifth predictor-corrector method [19]. The Tersoff potential [20-24] was selected to calculate the interactions among carbon atoms of the nanoribbon graphene and the carbon nanotube. In addition, the Lennard-Jones potential was adopted to model interactions between graphene nanoribbons and nanotube atoms.

![](./images/814527968058540033_1.jpg)

Fig. 1. Schematic of an MD model of a GNR@SWCNT subjected to a torsion loading.

## 3. Results and discussion

### 3.1. The size effect

We investigated the torsional characteristics of GNR@SWCNT with different chiralities of (10, 10), (13, 13), and (15, 15) using MD simulations. Snapshots of the vector distribution of atoms for a GNR@SWCNT with a chirality of (11,11) subjected to torsion with torsional angles of $180^\circ$, $360^\circ$, $720^\circ$, and $835^\circ$ at 300 K are shown in Fig. 2(a)-(d), respectively. The lower halves of the figures show the deformation configuration of the graphene nanoribbon. A longer arrow indicates a larger vector displacement. From Fig. 2 (a) to (c), it can be observed that both GNR and SWCNT experienced a larger twist deformation as the torsional angle increased. The deformation on the right region relative to the left region is larger because of unilateral torsion on the right side of the nanocomposite. In addition, Fig. 2(d) shows that the SWCNT breaks open and the GNR is exposed at a torsional angle of $835^\circ$. This is because the shear stress of the SWCNT induced by torsion reached its fracture strength.

In order to examine the size effect, we investigated the torsional characteristics of a GNR@SWCNT with different chiralities of (11,11), (13,13), and (15,15). The atoms and widths of different

![](./images/814527968058540033_2.jpg)

Fig. 2. Snapshots of vector distribution of atoms for a GNR@SWCNT with a chirality of (11,11) subjected to torsion with different torsional angles of (a) $180^\circ$, (b)$360^\circ$, (c)$720^\circ$, and (d)$835^\circ$ at 300 K.

---
Please cite this article as: T.-H. Fang, et al., Physica E (2016), http://dx.doi.org/10.1016/j.physe.2016.05.006

<table>
<caption>Table 1 Atoms and width of nanocomposite with 15 nm length.</caption>
<thead>
<tr>
<th>Chirality (n,m)</th>
<th>Atoms of nanotube</th>
<th>Atoms of graphene</th>
<th>Graphene width (nm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>(11,11)</td>
<td>2728</td>
<td>497</td>
<td>0.7</td>
</tr>
<tr>
<td>(13,13)</td>
<td>3224</td>
<td>710</td>
<td>1.1</td>
</tr>
<tr>
<td>(15,15)</td>
<td>3720</td>
<td>852</td>
<td>1.3</td>
</tr>
</tbody>
</table>

![](./images/814527968058540033_3.jpg)

Fig.3. The relationship between the shear stress and twist angle for a GNR@SWCNT with different chiralities of SWCNT at 300 K.

nanocomposites with a length of 15 nm used in the simulations are listed in Table 1. Fig. 3 illustrates the shear stress-twist angle curve for GNR@SWCNT with different SWCNT chiralities at 300 K. The shear stress induced by torsion increased with increasing twist angle before breaking. Maximum shear stresses of 72, 74, and 78 GPa were obtained for chiralities of (11,11), (13,13), and (15,15), respectively. The corresponding twist angles for chiralities of (11,11), (13,13), and (15,15) were 750°, 665°, and 581°, respectively. This indicates that the maximum shear stress increased with increasing chirality because of the size effect. However, the twist angle decreased with increasing chirality. The reason is that the interaction between the GNR and the SWCNT results in a decrease in torsional rigidity, especially at a larger chirality. To verify the interaction effect, we also conducted a torsion test for a (11,11) SWCNT. The result shows that the SWCNT broke at a torsional angle of 1040°, larger than the 835° for GNR@SWCNT. This indicates that the nanocomposite endures a smaller twist angle than a single SWCNT because of the interaction effect.

Fig. 4 shows the potential energy-twist angle curve for GNR@SWCNT with different SWCNT chiralities at 300 K. A positive potential energy represents a repulsive interaction between carbon atoms, and negative energy represents an attractive interaction. The potential energy decreased sharply when the critical twist angle was reached and failure occurred. The critical twist angles for chiralities of (11,11), (13,13), and (15,15) were 835°, 670°, and 590°, respectively. Snapshots of GNR@SWCNT with different SWCNT chiralities subjected to torsion until failure at 300 K are illustrated in Fig. 5. The dashed lines indicate the locations where the GNR is exposed from the broken SWCNT. The interaction force-twist angle curve for GNR@SWCNT with different SWCNT chiralities at 300 K is shown in Fig. 6. The interaction force is seen to increase slightly with increasing twist angle until failure.

![](./images/814527968058540033_4.jpg)

Fig.4. The relationship between the potential energy and twist angle for a GNR@SWCNT with different chiralities of SWCNT at 300 K.

![](./images/814527968058540033_5.jpg)

Fig. 5. Snapshots of a GNR@SWCNT with different chiralities of SWCNT subjected to torsion until failure at 300 K.

![](./images/814527968058540033_6.jpg)

Fig.6. The relationship between the interaction force and twist angle for a GNR@SWCNT with different chiralities of SWCNT at 300 K.

### 3.2. The temperature effect

Fig. 7 shows the shear stress-twist angle curves for a GNR@SWCNT with a chirality of (11,11) at different temperatures. The area under a shear stress-twist angle curve represents the strain energy being input into the nanocomposite. The strain energy decreased with an increase in the temperature. This indicates

Please cite this article as: T.-H. Fang, et al., Physica E (2016), http://dx.doi.org/10.1016/j.physe.2016.05.006

![](./images/814527968058540033_7.jpg)

Fig.7. The relationship between the shear stress and twist angle for a GNR@SWCNT with a chirality of (11,11) at different temperatures.

that the nanocomposite is easier to fracture at a higher temperature.

Fig. 8 depicts the potential energy-twist angle curve for a GNR@SWCNT with a chirality of (11,11) at different temperatures. When the critical twist angle was reached and failure occurred, the potential energy decreased sharply. Snapshots of a GNR@SWCNT subjected to torsion until failure at different temperatures are illustrated in Fig. 9. The locations where the SWCNT broke open are indicated by dashed lines. The interaction force-twist angle curve for a GNR@SWCNT with a chirality of (11,11) at different temperatures is shown in Fig. 10. The interaction force is observed to increase with increasing temperature because of an increase in the kinetic energy. This is also the reason why the nanocomposite breaks easily at an elevated temperature during torsion with a lower twist angle as shown in Figs. 7 and 8.

## 4. Conclusions

In this study, we performed MD simulations to investigate the mechanical properties of GNR@SWCNT subjected to torsion. The effects of different chiralities and temperatures on the torsional characteristics of GNR@SWCNT were examined. Results show that the shear stress induced by torsion increased with an increase in the twist angle before breaking. Maximum shear stresses of 72, 74, and 78 GPa were obtained for GNR@SWCNT with chiralities of (11,11), (13,13), and (15,15), respectively. The corresponding twist angles for chiralities of (11,11), (13,13), and (15,15) were 750°, 665°, and 581°, respectively. GNR@SWCNT endured a smaller twist angle than a single SWCNT. In addition, the interaction force increased with increasing temperature. GNR@SWCNT also fractured easily at a higher temperature.

![](./images/814527968058540033_8.jpg)

Fig.8. The relationship between the potential energy and twist angle for a GNR@SWCNT with a chirality of (11,11) at different temperatures.

![](./images/814527968058540033_9.jpg)

Fig. 9. Snapshots of a GNR@SWCNT with a chirality of (11,11) subjected to torsion until failure at different temperatures.

![](./images/814527968058540033_10.jpg)

Fig. 10. The relationship between the interaction force and twist angle for a GNR@SWCNT with a chirality of (11,11) at different temperatures.

## Acknowledgments

The authors wish to thank the Ministry of Science and Technology of Taiwan for providing financial supports for this study under projects MOST 103-2221-E-151-007 -MY3 and MOST 103-2221-E-168-006.

Please cite this article as: T.-H. Fang, et al., Physica E (2016), http://dx.doi.org/10.1016/j.physe.2016.05.006

### References

[1] T.W. Ebbesen (Ed.), Carbon Nanotubes Preparation and Properties, CRC Press,
New York, 1997.

[2] Trends in Nanotechnology Research, in: V. Eugene (Ed.), Dirote, Nova Science,
Publishers, New York, 2004.

[3] Carbon Nanotubes: New Research, in: P. Avery (Ed.), Ottenhouse, Nova Science,
Publishers, New York, 2009.

[4] C.N.R. Rao, A.K. Sood (Eds.), Graphene: Synthesis, Properties, and Phenomena,
Wiley, 2013.

[5] A. Chuvilin, E. Bichoutskaia, M.C. Gimenez-Lopez, T.W. Chamberlain, G.
A. Rance, N. Kuganathan, J. Biskupek, U. Kaiser, A.N. Khlobystov, Nat. Mater. 10
(2011) 687.

[6] L. Kou, C. Tang, T. Frauenheim, C. Chen, J. Phys. Chem. Lett. 4 (2013) 1328.

[7] Y.J. Dappe, J. Phys. D: Appl. Phys. 47 (2014) 083001.

[8] L. Wang, H.W. Zhang, Z.Q. Zhang, Y.G. Zheng, J.B. Wang, Appl. Phys. Lett. 91
(2007) 051122.

[9] S.H. Guo, B.E. Zhu, X.D. Ou, Z.Y. Pan, Y.X. Wang, Carbon 48 (2010) 4129.

[10] C.D. Wu, T.H. Fang, C.Y. Chan, Carbon 49 (2011) 2053.

[11] J. Wu, K.W. Zhang, X.Y. Peng, S.M. Li, L.Z. Sun, J.X. Zhong, Comput. Mat. Sci. 79
(2013) 650.

[12] C.C. Ling, Q.Z. Xue, D. Xia, M.X. Shan, Z.D. Han, RSC Adv. 4 (2014) 1107.

[13] A.V. Talyzin, I.V. Anoshkin, A.V. Krasheninnikov, R.M. Nieminen, A.
G. Nasibulin, H. Jiang, E.I. Kauppinen, Nano Lett. 11 (2011) 4352.

[14] I.V. Lebedeva, A.M. Popov, A.A. Knizhnik, A.N. Khlobystov, B.V. Potapkin, Na-
noscale 4 (2012) 4522.

[15] B. Mandal, S. Sarkar, P. Sarkar, J. Phys. Chem. A 117 (2013) 8568.

[16] D.B. Zhang, R.D. James, T. Dumitrică, Phys. Rev. B 80 (2009) 115418.

[17] I. Nikiforov, B. Hourahine, Th Frauenheim, T. Dumitrică, J. Phys. Chem. Lets 5
(2014) 4083.

[18] T.H. Fang, W.J. Chang, Y.L. Feng, Appl. Surf. Sci. 356 (2015) 221.

[19] J.M. Haile, Molecular dynamics simulation: elementary methods, Wiley, New
York, 1992.

[20] J. Tersoff, Phys. Rev. Lett. 56 (1986) 632.

[21] J. Tersoff, Phys. Rev. B 37 (1988) 6991.

[22] J. Tersoff, R.S. Ruoff, Phys. Rev. Lett. 73 (1994) 676.

[23] T.H. Fang, W.J. Chang, J.C. Yang, Dig. J. Nanomater. Biostruct. 7 (2012) 1811.

[24] T.H. Fang, W.J. Chang, K.P. Lin, S.T. Shen, Curr. Appl. Phys. 14 (2014) 533.

Please cite this article as: T.-H. Fang, et al., Physica E (2016), http://dx.doi.org/10.1016/j.physe.2016.05.006