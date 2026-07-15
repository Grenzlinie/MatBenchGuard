![](./images/811126415440216064_1.jpg)

Computational Materials Science 126 (2017) 321-325

Contents lists available at ScienceDirect

# Computational Materials Science

journal homepage: www.elsevier.com/locate/commatsci

![](./images/811126415440216064_2.jpg)

# Numerical investigation on mechanical properties of graphene covering silicon nanofilms

![](./images/811126415440216064_3.jpg)

Yunqing Tang $^{a}$, Bing Yang $^{a}$, Haiying Yang $^{a}$, Ping Yang $^{a,*}$, Jianming Yang $^{b}$, Yongle Hu $^{c}$

$^{a}$ Laboratory of Advanced Design, Manufacturing \& Reliability for MEMS/NEMS/ODES, Jiangsu University, Zhenjiang 212013, PR China
$^{b}$ Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St John's, NL, Canada
$^{c}$ Key Laboratory of Safety Design and Reliability Technology for Engineering Vehicle, Hunan Province, Changsha University of Science \& Technology, Changsha 410004, PR China

---

## ARTICLE INFO

**Article history:**
Received 5 May 2016
Received in revised form 19 September 2016
Accepted 25 September 2016

**Keywords:**
Graphene
Silicon
Nanofilm
Mechanical properties
Molecular dynamics

## ABSTRACT

The aim of this article is to perform an evaluation on mechanical properties of graphene covering silicon nanofilms by using molecular dynamics calculations. The deformation process of the composite film is simulated under uniaxial tensile loading to demonstrate the structural evolution, and the structural failure mode is discussed considering various film thicknesses and temperatures. The results show that size effect of thickness on the strength is significant at the thickness less than 4 nm and thinner thickness can help improve tensile properties of the nanofim. The 1 nm thick film has significantly better mechanical properties due to its different structural failure mode, and the substrate silicon is the weakness which limits mechanical properties of the composite film under high temperatures. It is hoped that our findings will be helpful for applications of graphene in silicon-based devices and materials.

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Since graphene was prepared for the first time in 2004 [1], much attention has been aroused for its extraordinary electron mobility, thermal transport and mechanical properties from both theoretical and experimental researches [2-10]. As a single atomic layer two-dimensional material, graphene has been proved to have an electron mobility up to 200,000 $\mathrm{cm^{2}/Vs}$ [2-5], a thermal conductivity up to 5300 W/mK [6,7] and an intrinsic strength up to 1100 GPa [9,10], which indicates enormous potential for the application in fields of electronics, semiconductors, materials and opto-electronics. In recent years, various methods have been developed for the preparation of graphene [11-13], which greatly promotes the exploration for more promising applications, including field effect transistors, flexible electrodes, energy storage materials, thermal interfacial materials and so on [14,15].

On the other hand, silicon is still the most attractive material in micro/nano manufacturing and new energy fields for its great electrical properties and relatively mature fabrication process. The excellent semiconductor property, good chemical stability, low discharge potential and high charge capacity make silicon the most important and widely used material in semiconductor devices, solar cells, integrated circuits and electrode materials [16,17], and corresponding composite materials are always research focus for the better performance of silicon-based devices [18-20], especially for nanoscale devices in which silicon-based electronics has approached the performance limit through dimensional scaling.

Although graphene has great advantages in nanoscale applications, it is hard to replace silicon completely due to its intrinsic zero bandgap. Nevertheless, it has demonstrated effectively improving silicon-based devices and materials, especially in high-speed electronics and lithium ion batteries [21-23]. As a key factor determining the device reliability, understanding mechanical properties of nanostructure is essential for the design of micro/nanoelectromechanical systems (MEMS/NEMS). Here, we investigate mechanical behaviors of a silicon nanofilm covered with graphene by using molecular dynamics calculations. The deformation process for silicon nanofilms with graphene covering is simulated under uniaxial tensile loading to demonstrate the structural evolution, and the structural failure mode is discussed considering various film thicknesses and temperatures. Our results are helpful for understanding mechanical properties of graphene covering silicon nanofilms and are expected to guide the application of graphene in silicon-based devices and materials.

---

* Corresponding author at: Laboratory of Advanced Manufacturing & Reliability for MEMS/NEMS/OEDS, School of Mechanical Engineering, Jiangsu University, Zhenjiang 212013, PR China.
E-mail addresses: yangpingdm@ujs.edu.cn, yangping1964@163.com (P. Yang).

http://dx.doi.org/10.1016/j.commatsci.2016.09.031
0927-0256/© 2016 Elsevier B.V. All rights reserved.

### 2. Simulation details

In this paper, we perform a series of molecular dynamics simulations to investigate mechanical properties of graphene covering silicon nanofilms. The silicon nanofilm is covered by monolayer graphene on its 100 surface through interlayer covalent bonds as shown in Fig. 1. The interface mismatch between the up layer graphene and substrate silicon is 5.76%. Atoms in gray and red are carbon atoms, cited as atom C1 and C2; atoms in yellow and green are silicon atoms, cited as atom Si1 and Si2; atoms C2 and Si2 are bonded by covalent bonds in the interface. The interaction between carbon atoms are described by AIREBO [24] potential which has been widely used in mechanical property calculations for graphene [25]. Interactions between carbon and silicon atoms and that between Si2 atoms are described by Erhart-Albe potential [26] for its good performance in previous related researches [27-29]. Interaction between Si1 atoms and that between Si1 and Si2 atoms in substrate silicon films are described by Stilinger-Weber potential [30]. After the structure is equilibrated for 10 ps without axial stress at desired temperature in NPT ensemble, a uniaxial tensile load is applied under deformation-control method by using an NVE ensemble. Homogeneous strain rate of $2 \times 10^9$ s$^{-1}$ is applied until the structure fails. The temperature control of molecular dynamics simulations is by using the Nose-Hoover Thermostat method, and the time integration is performed by using the Velocity-verlet Algorithm with an integration time step of 0.001 ps.

### 3. Results and discussion

As a commonly used calculation relating to the macroscopic (continuum) stress in molecular dynamics computations [31,32], the virial stress is used to derive the tensile stress in this study. The tensile stress is the average stress of all atoms in the tensile direction, and strain is the nominal strain. Both are expressed as follows,

$$
\begin{cases}
P_{ij} = \frac{1}{\Omega} \left[ -\sum_{\alpha=1}^{n} \left( m_{\alpha} \left( v_{i}^{\alpha} - \overline{v_{i}} \right) \left( v_{j}^{\alpha} - \overline{v_{j}} \right) \right) + \frac{1}{2} \sum_{\alpha \neq \beta} \left( x_{i}^{\beta} - x_{i}^{\alpha} \right) f_{j}^{\alpha \beta} \right] \\
\varepsilon = \frac{l - l_0}{l_0}
\end{cases}
$$

where $i$ and $j$ denote the indices in the Cartesian coordinate system, while $\alpha$ and $\beta$ are the atomic indices; $P_{ij}$ is the average stress in $i$ and $j$ directions; $\Omega$ is the volume; $m$ and $v$ are the mass and velocity of atoms, respectively; $\overline{v}$ represents the average velocity of all atoms; $x$ is the position of atom and $f^{\alpha \beta}$ is force between atoms $\alpha$ and $\beta$; $l$ and $l_0$ are lengths before and after the deformation.

In this study, tensile processes of graphene covering silicon nanofilms with thicknesses from 1 nm to 6 nm were simulated at temperatures ranging from 200 K to 1000 K. Fig. 2 shows the stress-strain dependence of films with different thicknesses at 300 K. It is clear that the ultimate tensile strength and Young's modulus are decreasing with the increase of thickness and tend to be stable values when the thickness is more than 4 nm. It implies that the size effect of thickness on the strength is significant at the thickness less than 4 nm and the thinner thickness can help improve tensile properties of the nanofim. It can be also seen that the shape of stress-strain curve for the 1 nm thick film is obviously different from shapes of other curves although they all have two crests during the tensile process. For the 1 nm thick film the top comes after the first crest, but for other films the top appears at the first crest, which indicates that the 1 nm thick film experiences a unique failure process compared with other films.

![](./images/811126415440216064_4.jpg)

Fig. 2. Stress-strain curves of graphene covering silicon nanofilms with thicknesses from 1 nm to 6 nm at 300 K.

To understand the size effect of thickness on stress-strain behaviors during tensile processes, especially for the anomalies in 1 nm thick film, tensile simulations of pristine silicon nanofilms with thicknesses from 1 nm to 4 nm at 300 K were conducted. The stress-strain curves are shown in Fig. 3. It can be seen that for the pristine silicon, nanofilms all get to their ultimate strain in the range of 0.27-0.29; tensile capacity of the 1 nm thick film is significantly lower than those of thicker films; films with thicknesses of 2-4 nm are in the same tensile failure mode with tensile strengths of similar values, while the Young's Modulus decreases slightly with the thickness increasing. The higher specific surface area of 1 nm thick film makes it easier to occur lattice mutation at surface, thus the 1 nm thick film reach to its yield strength, leading to the more significant size effect. When the thickness is more than 2 nm, the size effect is weakened, and films fracture once getting to their tensile strength, showing more brittleness with the thickness increasing. Comparing with the results for graphene covering silicon nanofilms, it can be seen that the mechanical proper-

![](./images/811126415440216064_5.jpg)

Fig. 1. The interfacial connection between graphene and silicon nanofilm.

![](./images/811126415440216064_6.jpg)

Fig. 3. Stress-strain curves of pristine silicon nanofilms with thicknesses from 1 nm to 4 nm at 300 K.

ties of the film are effectively enhanced by covering graphene. The reason could be that the surface effect of silicon is weakened as the silicon surface area is reduced by coating graphene on it, while the graphene surface is more stable than the silicon surface, and mechanical properties of the up layer graphene is superior to sili- con. For the 1 nm composite film, strain energies are mainly stored in graphene, so the strength of the film is significantly improved by covering graphene; while with the thickness of silicon increasing, more strain energies are stored in silicon and silicon will crack before the failure of graphene, so the strength of the film is lower compared to the 1 nm composite film and tending to a stable value.

For further insight into the failure mode of the graphene cover- ing silicon nanofilm, the failure process of the nanofilm was observed by using Visual Molecular Dynamics (VMD) software [33]. Fig. 4 shows the fracture process of the 1 nm thick film at the temperature of 300 K. The process can be divided into three stages. The first stage is the elastic stage, in which the stress is increasing with the strain linearly and the structure of the film is stable. In the second stage, the failure of silicon happens. We can see the substrate silicon begins to fail at position A when the strain comes to 0.37, corresponding to the first crest for the 1 nm film. At this time, the structure can still carry the load and the failure starts from position B at the strain of 0.4. The failure of graphene happens in the third stage. When the strain comes to 0.413, graphene cracks at position B and then the whole structure loses the load carrying capacity, corresponding to the second crest. It can be seen that the second crest is higher and graphene and silicon crack at the same time, although the silicon reaches to the yielding stage very early, hence it is considered that the graphene plays the main role in load carrying for the 1 nm thick composite film. However, the fracture process shown in Fig. 5 for the 3 nm thick film at the same temper- ature is obviously different from the 1 nm thick film as inferred from the stress-strain curves. The failure starts at the interface between graphene and silicon at the strain of 0.34 and develops at an angle of $45^{\circ}$ from the interface plane to the silicon surface, forming the glide plane, and lastly the substrate silicon loses the load carrying capacity, followed by the crack of the covering gra- phene, leading to the fracture of the whole structure. It indicates that the silicon plays the main role in load carrying for these thicker composite films.

![](./images/811126415440216064_7.jpg)

Fig. 4. Fracture process of the 1 nm thick graphene covering silicon nanofilm at the temperature of 300 K by VMD.

For the significantly better performance in both tensile strength and Young's modulus, more attentions are attracted in mechanical properties of the 1 nm thick graphene covering silicon nanofilm. Fig. 6 shows the stress-strain curves of the 1 nm thick graphene covering silicon nanofilm at temperatures ranging from 200 K to 1000 K. From the stress-strain curves, it can be seen that the1 nm thick film shows perfect tensile properties under relatively lower temperatures. When the temperature is less than 700 K, the ultimate strain of the structure is more than 0.4, indicating that the up layer graphene has a relatively stable mechanical property in this temperature range, and with the increase of the tempera- ture, the first crest, corresponding to the beginning of failure in substrate silicon, appears earlier with smaller stress values, indi- cating that the increase of temperature will obviously reduce the load carrying capacity of substrate silicon. When the temperature is more than 700 K, the first crest appears at the strain of about0.22 for different temperatures, the ultimate strain of the structure is obviously decreasing with the increase of temperature, and the curve becomes less steep after the first crest. Combining the failure process of the 1 nm thick film at 900 K shown in Fig. 7, it could be inferred that when under high temperatures, most of the substrate silicon comes into the plastic flow stage soon after the failure hap- pens, and the whole substrate silicon loses load carrying capacity

![](./images/811126415440216064_8.jpg)

Fig. 5. Fracture process of the 3 nm thick graphene covering silicon nanofilm at the temperature of 300 K by VMD.

![](./images/811126415440216064_9.jpg)

Fig. 6. Stress-strain curves of the 1 nm thick graphene covering silicon nanofilm at temperatures from 200 K to 1000 K.

![](./images/811126415440216064_10.jpg)

Fig. 7. Failure process of the 1 nm thick graphene covering silicon nanofilm at the temperature of 900 K.

long before the graphene brakes, whose mechanical property is also much weakened by the high temperature. It suggests that the influence of temperature on mechanical properties of the substrate silicon is an important factor which limits mechanical properties of the composite film under high temperatures.

## 4. Conclusions

In summary, we have studied mechanical properties of the graphene covering silicon nanofilm by using molecular dynamics calculations. The tensile process for graphene covering silicon nanofilms with thicknesses of 1–6 nm is simulated under uniaxial tensile loading at temperatures ranging from 200 K to 1000 K. The results indicate that size effect of thickness on the strength is significant at the thickness less than 4 nm, and graphene contributes more in load carrying for the 1 nm thick composite film. Thinner thickness can help improve tensile properties of the nanofilm, and the 1 nm thick film has significantly better mechanical properties due to its different structural failure mode from other thicker films. Then mechanical properties of the 1 nm thick film under different temperatures are focused on. Results show that when the temperature is less than 700 K, the strength of the nanofilm structure is relative stability; when the temperature is more 700 K, the strength of the nanofilm is significantly decreased with the increasing. The influence of temperature on mechanical properties of the substrate silicon is obviously worse than that on up layer graphene, which is the main reason for the limitation of mechanical properties of the composite film under high temperatures. It suggests that the 1 nm graphene covering silicon nanofilm will keep good mechanical properties at temperatures less than 700 K. The findings will be helpful for applications of graphene in silicon-based devices and materials.

## Acknowledgments

The authors would like to acknowledge the support of National Natural Science Foundation of China (51575246 and 61076098), the support of Six talent peaks project in Jiangsu Province (JXQC-006), the support of A Project Funded by the Priority Academic Program Development of Jiangsu Higher Education Institutions, the support of China Postdoctoral Science Special Foundation (2014T70476), Innovative Science Foundation for Graduate Students of Jiangsu Province (KYLX15_1054, CXZZ13_0655, CXLX12_0622), during the course of this work.

## References

[1] K.S. Novoselov, A.K. Geim, S.V. Morozov, et al., Electric field effect in atomically thin carbon films, Science 306 (2004) 666.
[2] A.K. Geim, K.S. Novoselov, The rise of graphene, Nat. Mater. 6 (3) (2007) 183.
[3] K.I. Bolotin, K.J. Sikes, Z. Jiang, et al., Ultrahigh electron mobility in suspended graphene, Solid State Commun. 146 (9) (2008) 351.
[4] A.H.C. Neto, The electronic properties of graphene, Rev. Mod. Phys. 81 (1) (2007) 109.
[5] S. Das Sarma, Shaffique Adam, E.H. Hwang, et al., Electronic transport in two-dimensional graphene, Rev. Mod. Phys. 83 (2) (2011) 407.
[6] A.A. Balandin, Thermal properties of graphene and nanostructured carbon materials, Nat. Mater. 10 (8) (2011) 569.
[7] J.W. Jiang, J.S. Wang, B. Li, Thermal conductance of graphene and dimerite, Phys. Rev. B: Condens. Matter 79 (20) (2009).
[8] P. Yang, Y. Tang, H. Yang, et al., Thermal management performance of bent graphene nanoribbons, RSC Adv. 3 (2013) 17349.
[9] I.W. Frank, D.M. Tanenbaum, A.M.V.D. Zande, et al., Mechanical properties of suspended graphene sheets, J. Vac. Sci. Technol., B 25 (6) (2007) 2558.
[10] L. Changgu, W. Xiaoding, J.W. Kysar, et al., Measurement of the elastic properties and intrinsic strength of monolayer graphene, Science 321 (2008) 38.
[11] S. Peter, Epitaxial graphene: how silicon leaves the scene, Nat. Mater. 8 (3) (2009) 171.
[12] H.M. Wang, Y.H. Wu, Z.H. Ni, et al., Electronic transport and layer engineering in multilayer graphene structures, Appl. Phys. Lett. 92 (5) (2008) 053504.
[13] M. Choucair, P. Thordarson, J.A. Stride, Gram-scale production of graphene based on solvothermal synthesis and sonication, Nat. Nanotechnol. 4 (1) (2009) 30-33.
[14] X. Wang, Y. Ouyang, X. Li, et al., Room temperature all semiconducting sub-10 nm graphene nanoribbon field-effect transistors, Phys. Rev. Lett. 100 (20) (2008) 1586.
[15] X. Zhang, K.Y. Kan, Z. Gao, et al., Exceptional thermal interface properties of a three-dimensional graphene foam, Carbon 66 (3) (2014) 201.
[16] S.A. Dayeh, J. Wang, N. Li, et al., Growth, defect formation, and morphology control of germanium-silicon semiconductor nanowire heterostructures, Nano Lett. 11 (10) (2011) 4200.
[17] K. Dae-Hyeong, A. Jong-Hyun, C. Won Mook, et al., Stretchable and foldable silicon integrated circuits, Science 320 (5875) (2008) 507.
[18] J. Saint, M. Morcrette, D. Larcher, et al., Towards a fundamental understanding of the improved electrochemical performance of silicon-carbon composites, Adv. Funct. Mater. 17 (11) (2007) 1765.
[19] R. Yi, F. Dai, M.L. Gordin, et al., Influence of silicon nanoscale building blocks size and carbon coating on the performance of micro-sized Si-C composite Li-Ion anodes, Adv. Energy Mater. 3 (11) (2013) 1507.
[20] J.Y. Eom, H.S. Kwon, Preparation of single-walled carbon nanotube/silicon composites and their lithium storage properties, ACS Appl. Mater. Interf. 3 (4) (2011) 1015.
[21] C.C. Chen, M. Aykol, C.C. Chang, et al., Graphene-silicon Schottky diodes, Nano Lett. 11 (5) (2011) 1863-1867.
[22] H. Xiang, K. Zhang, G. Ji, et al., Graphene/nanosized silicon composites for lithium battery anodes with improved cycling stability, Carbon 49 (5) (2011) 1787.
[23] T. Ceren, Z. Zhen, B. Matteo, et al., Optimizing electronic structure and quantum transport at the graphene-Si(1 1 1) interface: an ab initio density-functional study, Phys. Rev. Lett. 110 (17) (2013) 176805.
[24] S.J. Stuart, A.B. Tutein, J.A. Harrison, A reactive potential for hydrocarbons with intermolecular interactions, J. Chem. Phys. 112 (14) (2000) 6472.
[25] H. Zhao, K. Min, N.R. Aluru, Size and chirality dependent elastic properties of graphene nanoribbons under uniaxial tension, Nano Lett. 9 (8) (2009) 3012.
[26] P. Erhart, K. Albe, Analytical potential for atomistic simulations of silicon, carbon, and silicon carbide, Phys. Rev. B 71 (3) (2005) 035211.
[27] Y. Jing, N.R. Aluru, Atomistic simulations on the mechanical properties of a silicon nanofilm covered with graphene, Comput. Mater. Sci. 50 (10) (2011) 3063.

[28] Y. Jing, L. Guo, Y. Sun, et al., Mechanical properties of a silicon nanofilm covered with defective graphene, Surf. Sci. 611 (5) (2013) 80.

[29] X. Wang, X. Tang, J. Gong, et al., Mechanical property of a graphene/silicon interface: an atomistic simulation research, Int. J. Mater. Struct. Integr. 8 (1-3) (2014) 161.

[30] F.H. Stillinger, T.A. Weber, Computer simulation of local order in condensed phases of silicon, Phys. Rev. B 31 (8) (1985) 5262.

[31] D.H. Tsai, The virial theorem and stress calculation in molecular dynamics, J. Chem. Phys. 70 (3) (1979) 1375.

[32] J.A. Zimmerman, E.B. WebbIII, J.J. Hoyt, et al., Calculation of stress in atomistic simulation, Modell. Simul. Mater. Sci. Eng. 12 (4) (2004) S319.

[33] W. Humphrey, A. Dalke, K. Schulten, VMD: visual molecular dynamics, J. Mol. Graph. 14 (1) (1996) 33.

Ping Yang is currently a professor in Jiangsu University in China, also is currently an editorial Member of Microsystem Technologies, an editorial Member of Interna- tional Journal of Materials and Product Technology, Associate Editor in Chief of International Journal of Materials and Structural Integrity, a director of China Pre- cision Machine Society and a senior member of Chinese Institute of Electronics. He received his Ph.D in mechanical engineering from Huazhong University of Science & Technology (HUST) in 2001. He engaged in sciences research in Concordia University. His research interests focus on the theoretical aspect, materials and mechanical system for the purposes of design and control. He has authored over 130 professional and scholarly publications in famous international journal in the very specialized field of the theoretical aspect, materials and micro/nano- mechanical system for the purposes of design and control.