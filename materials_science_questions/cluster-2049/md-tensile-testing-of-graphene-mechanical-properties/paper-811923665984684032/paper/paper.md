# Potential application of single-layered graphene sheet as strain sensor

A. Sakhaee-Pour$^{a,*}$, M.T. Ahmadian$^{a}$, A. Vafai$^{b}$

$^{a}$ Center of Excellence in Design, Robotics and Automation (CEDRA), Department of Mechanical Engineering, Sharif University of Technology, P. O. Box 11365-9567, Azadi Ave, Tehran, Iran
$^{b}$ Department of Civil Engineering, Sharif University of Technology, P. O. Box 11365-8639, Azadi Ave, Tehran, Iran

---

## ARTICLE INFO

Article history:
Received 12 December 2007
Received in revised form
3 March 2008
Accepted 10 April 2008 by E.G. Wang
Available online 18 April 2008

PACS:
46.40.-f
42.81.Pa
62.30.+d
81.07.b

Keywords:
A. Nanostructure
A. Single-layered graphene sheet (SLGS)
D. Strain sensor

---

## ABSTRACT

Molecular structural mechanics is implemented to investigate the vibrational characteristics of defect-free single-layered graphene sheets (SLGSs), which have potential applications as strain sensors. The effect of strain on the fundamental frequencies of the defect-free zigzag and armchair models with clamped-clamped boundary condition is studied. The atomistic modeling results reveal while sensitivities of the strain sensors are not influenced significantly by chirality, they can be slightly increased by decreasing aspect ratios of the sheets. It is further shown that the SLGSs-based strain sensors are more sensitive to the applied stretch than the SWCNTs versions.

© 2008 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

In recent years, a lot of research has been conducted to achieve a high level of sensitivity in nanoscale sensors [1]. Wood and his colleagues [2,3] implemented the Raman frequencies of carbon nanotubes (CNTs) to monitor pressure and strain. The feasibility of employing these nanostructures to enhance the resolution of surface imaging was assessed by Dai et al. [4]. Using CNTs, Wang and his co-workers [5] investigated mass measurements experimentally, and a high level of sensitivity, 22 fg, was observed. Li and Chou adopted an atomistic modeling, molecular structural mechanics [6], to explore the vibrational characteristics of cantilever and bridge single-walled carbon nanotubes (SWCNTs) with adsorbed mass [7]. Their findings at constant temperature demonstrate the SWCNTs have the capability of point mass detecting of the order of $10^{-6}$ fg. In addition, they proposed an equation to predict variation of the SWCNT fundamental frequency with respect to the magnitude of the point mass. They also examined the possibility of applying SWCNTs for strain and pressure measurements [8]. It was predicted that axial 7 percent strain would alter the fundamental frequency of the 8 nm long SWCNT about 3 kHz from 300 GHz. It was further reported that the fundamental frequencies of the SWCNTs change linearly versus strain.

Since fabrication of single-layered graphene sheets (SLGSs) was not feasible experimentally, fewer investigations in comparison with CNTs have been undertaken. While the peculiar physical and electrical characteristics of the graphene sheets have been studied by researchers [9-14], the mechanical properties are not addressed well in the literature. Behfar and Naghdabadi [15] have implemented a continuum-based method to explore the vibrational behavior of a multi-layered graphene sheet embedded in an elastic medium. They have further proposed an analytical approach for determination of the bending modulus for a multi-layered graphene sheet [16]. Kitipornchai and his co-workers have studied the vibrational characteristics of multi-layered graphene sheets using a continuum model [17]. They have also investigated the vibrational behavior of multi-layered graphene sheets embedded in an elastic matrix [18].

Stankovich et al. [19] have developed a process of obtaining SLGS from graphite. This method introduces the SLGS as an industrial preference to the much more expensive CNT. Industrial application of this two-dimensional layer requires the scientists to derive reliable physical and mechanical properties for it. Bunch et al. [20] have presented experimental results using electromechanical resonators made from suspended single- and

---

* Corresponding author.
E-mail addresses: Sakhaee@mech.sharif.edu, sakhaee@alum.sharif.edu (A. Sakhaee-Pour).

0038-1098/$ - see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ssc.2008.04.016

![](./images/811923665984684032_1.jpg)
![](./images/811923665984684032_2.jpg)

Fig. 1. Schematic illustration of zigzag and armchair SLGSs with clamped-clamped boundary condition.

multi-layered graphene sheets. Recently, the authors have studied the free vibrational behavior of the SLGSs while considering effects of chirality and aspect ratio as well as boundary conditions, and have proposed predictive models for computing natural frequencies [21]. Furthermore, the potential applications of the SLGSs as mass sensors and atomistic dust detectors have been investigated [22].

In this study, the possibility of employing SLGSs as strain sensors is assessed through an atomistic simulation method - the molecular structural mechanics. While considering the influences of length and aspect ratio for the zigzag and armchair models, shifts of the fundamental frequencies with respect to the strain are calculated. In addition, the sensitivities of the SLGSs-based strain sensors are compared with those of the SWCNTs.

### 2. Atomistic modeling of single-layered graphene sheets

To analyze the vibrational behavior of defect-free SLGSs as strain sensors at a constant temperature, the molecular structural mechanics method is adopted. In this atomistic modeling, equivalent structural beams and concentrated masses are employed to mimic carbon atoms which are connected via covalent bonds in the so-called honeycomb lattice. The elastic properties of the beam are computed in terms of the covalent bonds stiffnesses to model the interatomic forces and the concentrated masses are assumed to be at the nodes coincident with the atoms.

By considering the equivalent potential energies of the molecular and structural mechanics, the properties of the beam were developed [6]. To calculate the beam properties, force field constants of the covalent bonds are used as:

$$
\frac{EA}{L}=k_{r}, \quad \frac{EI}{L}=k_{\theta}, \quad \frac{GJ}{L}=k_{\phi} \tag{1}
$$

where the force field constants $k_{r}$, $k_{\theta}$ and $k_{\phi}$ represent bond stretching, angle bending and torsional stiffness of the covalent bonds, respectively, while $E$ and $G$ denote moduli of elasticity and shear of the beam, respectively. Moreover, $A$ is the cross section area, $I$, the moment of inertia, $J$, the polar moment of inertia, and $L$ the length of the beam. The length of the beam is assumed to be equal to the covalent bond distance of the carbon atoms in the hexagonal lattice. The beam properties with a circular cross section can be derived from the previous equation as:

$$
\begin{aligned}
d &=4 \sqrt{\frac{k_{\theta}}{k_{r}}} \\
E &=\frac{k_{r}^{2} L}{4 \pi k_{\theta}} \\
G &=\frac{k_{r}^{2} k_{\phi} L}{8 \pi k_{\theta}^{2}}
\end{aligned} \tag{2}
$$

where $d$ is the cross section diameter of the beam. In the molecular structural mechanics, Interatomic forces of the bonded carbon atoms are modeled through the equivalent structural beams.

By considering the radii of the carbon nuclei to be negligible ($r_{c}=2.7 \times 10^{-5} \mathring{A}$), concentrated masses are adopted to simulate carbon atoms. The concentrated masses with the carbon nuclei masses ($m_{c}=1.9943 \times 10^{-23}$ g) are positioned at the ends of the beams representing joints of the covalent bonds. It is assumed that the masses of the electrons are not significant in comparison to those of the nuclei.

In the molecular structural mechanics approach, the SLGSs are modeled as space-frame structures. Overall mass and stiffness matrices of the molecular structural mechanics models are generated from the equivalent matrices of the beams [6] and concentrated masses [7]. The overall mass and stiffness matrices are used to write equation of motion as:

$$
[M]\{\ddot{y}\}+[K]\{y\}=\{0\} \tag{3}
$$

where $\{y\}$ and $\{\ddot{y}\}$ represent position and acceleration vectors of the atoms, respectively. In addition, $[M]$ and $[K]$ are the overall mass and stiffness matrices, respectively.

Eigenvalues of the motion equation are calculated after imposing harmonic vibration. To find the eigenvalues, the condensed mass and stiffness matrices are employed. The condensed matrices have fewer components than the overall mass and stiffness matrices; therefore, using the condensed matrices eases the computation task. The condensed matrices are generated by the static condensation method [23]. The fundamental frequencies of the SLGSs are obtained from the minimum eigenvalues. Then, the feasibility of applying these two-dimensional layers as strain sensors is evaluated through computing fundamental frequency changes versus uniform strain. In order to implement the effect of the stretch, the overall stiffness matrix is adapted. The components of the adapted overall stiffness matrix are calculated by considering positions of the atoms of the elongated SLGS, increased side length, $a$, with constant width, $b$, (see Fig. 1).

![](./images/811923665984684032_3.jpg)

Fig. 2. Schematic of bridge (a) zigzag SLGSs for $\frac{a}{b}=0.8660$ with different side lengths (b) zigzag SLGSs for $a=8.5260$ nm with different aspect ratios (c) armchair SLGSs for $\frac{a}{b}=1.1547$ with different side lengths (d) armchair SLGSs for $a=7.8760$ nm with different aspect ratios.

Since chirality has a significant influence on the mechanical properties of the graphene sheets [15], the zigzag and armchair models are considered. The zigzag and armchair SLGSs with clamped-clamped boundary condition are demonstrated in Fig. 1. Sides of the SLGSs are introduced to be $a$ and $b$ with $\frac{a}{b}$ as an aspect ratio. $a$ and $b$ can also be defined via the lattice translation vector [24].

In order to examine the promising usage of the SLGS as strain sensor, the effects of the chirality and geometrical parameters are considered. For this purpose, the influence of the strain on the fundamental frequencies of the zigzag and armchair SLGSs with different geometrical parameters are explored. Ranges of the geometrical parameters $a$ and $\frac{a}{b}$ are assumed to be 5.9070-14.4972 nm and 0.2165-3.8490, respectively. Schematic representations of the SLGSs examined in this study are shown in Fig. 2. In addition, the sensitivities of the SLGSs-based strain sensors are compared with those of the SWCNTs. To compare the sensitivities, the side lengths, $a$, of the zigzag and armchair sheets are chosen to be in the same order with the investigation by Li and Chou on the feasibility of applying SWCNTs as strain sensors [8]. The changes of the frequencies versus strain of the SLGSs are calculated and contrasted with the results available for the SWCNTs-based strain sensors.

### 3. Results

The vibrational characteristics of the defect-free SLGSs using the force field constants [25] and graphene sheet thickness presented in Table 1 are investigated. For the strain free SLGSs, the fundamental frequencies are calculated by adopting the molecular structural mechanics. The fundamental frequencies of the zigzag and armchair models with clamped-clamped boundary condition are shown in Fig. 3. It is found that the frequencies are not influenced by the aspect ratio, $\frac{a}{b}$, or chirality. In addition, the frequencies decrease nonlinearly with respect to the side length [21,22].

![](./images/811923665984684032_4.jpg)

Fig. 3. Fundamental frequencies of bridge SLGSs versus side length with different aspect ratios.

The influence of strain on the fundamental frequencies of the SLGSs with different side lengths is explored. To this end, the fundamental frequencies of the stretched zigzag and armchair sheets with the aspect ratios of 0.8660 and 1.1547 are calculated. Then the frequency deviations from the strain free conditions are computed. The shifts of the frequencies of the zigzag and armchair

<table><caption>Table 1 Force field constants of the covalent bonds and graphene sheet thickness</caption>
<tbody><tr><td>$k_{r}$</td><td>6.52e−7 N nm−1</td></tr>
<tr><td>$k_{\theta}$</td><td>8.76e−10 N nm rad−2</td></tr>
<tr><td>$k_{\phi}$</td><td>2.78e−10 N nm rad−2</td></tr>
<tr><td>$t$</td><td>0.34 nm</td></tr>
</tbody></table>

![](./images/811923665984684032_5.jpg)

Fig. 4. Fundamental frequency changes of bridge zigzag SLGSs versus strain for $\frac{a}{b}=0.8660$ with different side lengths.

![](./images/811923665984684032_6.jpg)

Fig. 5. Fundamental frequency changes of bridge armchair SLGSs versus strain for $\frac{a}{b}=1.1547$ with different side lengths.

sheets with different side lengths versus strain are demonstrated in Figs. 4 and 5, respectively. It is observed that the frequency changes of the smaller sheets are greater than the larger ones. However, the ratios of the frequency changes with respect to the strain free conditions are greater for the sheets with larger side lengths. For example, imposing 1 percent strain on the zigzag sheet with $a =$ 5.98 nm increases the frequency from 79.53 GHz to 183.23 GHz, whereas for $a =$ 14.49 nm and the same strain the frequency of the zigzag sheet is changed from 13.82 GHz to 68.55 GHz. This could be due to the larger energy storage of the bigger sheet. Considering the results for the zigzag and armchair sheets, it shows chirality does not play an important role in the frequency changes. The identical influence of the geometry variation, the equal displacements applied to the graphene sheets, is the reason for the same frequency changes. On the other hand, it should be noted that the frequency changes of the zigzag and armchair sheets will be different if they undergo a certain tensile force instead of strain.

![](./images/811923665984684032_7.jpg)

Fig. 6. Fundamental frequency changes of bridge zigzag SLGSs versus strain for $a = 8.5260$ nm with different aspect ratios.

![](./images/811923665984684032_8.jpg)

Fig. 7. Fundamental frequency changes of bridge armchair SLGSs versus strain for $a = 7.8760$ nm with different aspect ratios.

The sensitivity of the SLGS-based strain sensor is compared with that of the SWCNT. For this purpose, the side lengths, $a$, of the zigzag and armchair sheets are selected to be 8.5260 nm and 7.8760 nm, respectively, and the frequency deviations are calculated after applying strain to the sheets. The fundamental frequency shifts of the zigzag and armchair sheets with different aspect ratios versus strain are demonstrated in Figs. 6 and 7, respectively. The atomistic modeling shows the frequencies of the clamped-clamped zigzag and armchair sheets under 7% strain increase about 250 GHz from 39 GHz and 45 GHz, respectively. This reveals the SLGSs-based strain sensors are more sensitive to the stretch than the SWCNTs versions [8]. To shed light on the comparison, it is noted that the fundamental frequency mode shape of the SWCNT, depending on the geometrical parameters,

is breathing or bending [26] and it is under combination of compression and tension. As a result, the fundamental frequency variation of the SWCNT versus strain is smaller than that of the SLGS which is subjected to pure tension in the first mode. The large variation of the SLGS frequency with strain is further confirmed by the experimental results available in the literature [20], as reported that the tension causes the frequency to be shifted drastically. The atomistic modeling also indicates the sensitivity of the SLGS can be slightly enhanced by the aspect ratio reduction. Furthermore, it is discerned that the rate of the SLGS frequency change with strain, in contrast to the SWCNT, is not constant.

## 4. Conclusions

To propose a nanoscale strain sensor, the vibrational behavior of defect-free single-layered graphene sheet (SLGS) has been analyzed. For this purpose, the molecular structural mechanics is adopted to explore the influence of strain on the principal frequencies of the sheets with bridge configuration. The atomistic modeling approach exhibits chirality does not play an important role in the frequency shifts, whereas these shifts are slightly greater for the sheets with smaller aspect ratios. Furthermore, the principal frequencies vary nonlinearly with respect to the strain.

The sensitivities of the SLGS and SWCNT fundamental frequencies to the applied strain have been compared with each other. In this regard, the frequency changes of the nanostructures subjected to the strain with equivalent lengths are considered. It is observed that the fundamental frequency variation of the SLGS is larger than that of the SWCNT. The low cost manufacturing process and the extraordinary high level of sensitivity of the SLGS introduce this two-dimensional layer as an ideal preference to the SWCNT.

## References

[1] P. Poncharel, et al., Science 283 (1999) 1513.
[2] J.R. Wood, et al., J. Phys. Chem. B 47 (1999) 10388.
[3] J.R. Wood, et al., Appl. Phys. Lett. 76 (2000) 2883.
[4] H. Dai, et al., Nature 384 (1996) 147.
[5] Z.L. Wang, P. Pocharel, W.A. de Heer, J. Phys. Chem. Solids 61 (2000) 1025.
[6] C. Li, T-W. Chou, Int. J. Solids Struct. 40 (2003) 2487.
[7] C. Li, T-W. Chou, Appl. Phys. Lett. 84 (2004) 5246.
[8] C. Li, T-W. Chou, Nanotechnology 15 (2004) 1493-1496.
[9] K.S. Novoselov, et al., Nature 438 (2005) 197.
[10] Y. Zhang, et al., Nature 438 (2005) 201.
[11] C.J. Meyer, et al., Nature 446 (2006) 60.
[12] Y. Zhang, et al., Phys. Rev. Lett. 94 (2005) 176803.
[13] C. Berger, et al., Science 312 (2006) 1191.
[14] T. Ohta, et al., Science 313 (2006) 951.
[15] K. Behfar, R. Naghdabadi, Compos. Sci. Technol. 65 (2005) 1159.
[16] K. Behfar, et al., J. Thin Solid Films 496 (2006) 475.
[17] S. Kitipornchai, X.Q. He, K.M. Liew, Phys. Rev. B 72 (2005) 075443.
[18] K.M. Liew, X.Q. He, S. Kitipornchai, Acta Mater. 54 (2006) 4229.
[19] S. Stankovich, et al., Nature 442 (2006) 282.
[20] J. Bunch, et al., Science 315 (2007) 490.
[21] A. Sakhaee-Pour, M.T. Ahmadian, R. Naghdabadi, Nanotech. 19 (2008) 085702.
[22] A. Sakhaee-Pour, M.T. Ahmadian, A. Vafai, Solid State Commun. 4 (2008) 168-172.
[23] J.W. Tedeso, W.G. McDougal, C.A. Ross, Structural Dynamics: Theory and Applications, Addison Wesley-Longman, CA, 1999.
[24] K-T. Lau, D. Hui, Compos. Part B Eng. 33 (2002) 263-277.
[25] A.K. Rappe, et al., J. Am. Chem. Soc. 114 (1992) 10024.
[26] C. Li, T-W. Chou, Appl. Phys. Lett. 84 (2004) 121.