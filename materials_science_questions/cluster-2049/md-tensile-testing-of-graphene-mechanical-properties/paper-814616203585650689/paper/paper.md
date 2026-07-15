# Molecular Dynamics Modeling of Buckling Behavior of Hydrogenated Graphyne

A. Montazeri\*,\(\mathfrak{I}\), S. Ebrahimi\(^\dagger\), A. Rajabpour\(^\ddagger\),\(\mathfrak{I}\) and H. Rafii-Tabar\(^\S\),\(\mathfrak{I}\),\(^\|\)

\*Faculty of Materials Science and Engineering
K.N. Toosi University of Technology, Tehran, Iran

\(^\dagger\)Department of Physics, Faculty of Science
University of Kurdistan, Sanandaj, Iran

\(^\ddagger\)Department of Mechanical Engineering
Imam Khomeini International University
Qazvin 14395-515, Iran

\(^\S\)Department of Medical Physics and Biomedical Engineering
Shahid Beheshti University of Medical Sciences
Evin, Tehran, Iran

\(\mathfrak{I}\)Computational Physical Sciences Research Laboratory
School of Nano-Science
Institute for Research in Fundamental Sciences (IPM)
Tehran, Iran

\(^\|\)rafii-tabar@nano.ipm.ac.ir

Received 13 May 2015
Accepted 30 June 2015
Published 27 August 2015

Molecular dynamics simulation is employed to explore the influence of hydrogen adsorption on the stability behavior of graphyne (GY) as a new allotrope of carbon. The strain for the onset of buckling is determined for pristine GY and the results are compared with those for perfect graphene nanoribbons under identical conditions. The results reveal that due to the presence of triple C–C bonds in the GY structure, which are harder to rotate and bend in compression compared to single bonds, the new allotrope is stiffer than graphene during buckling phenomenon. In addition, the effect of hydrogen adsorption on the stability behavior of GY is examined with different H coverage in the range 0–50%. It is concluded that this adsorption promotes a rapid buckling which is attributed to the conversion of the stiff in-plane carbon bonding in the GY structure to the out-of-plane bonding which is weaker and easier to bend in compression. Finally, a critical value of adsorption is found above in which such a trend is not observed.

**Keywords:** Graphyne; hydrogen adsorption; molecular dynamics simulation; buckling.


### Definition of technical terms.

| Term | Definition |
|------|------------|
| Area density | Number of atoms per unit area. It can show compactness of atoms in a 2D nanostructure. |
| Buckling deformation | Buckling is characterized by a sudden sideways failure of a structural member subjected to high compressive stress, where the compressive stress at the point of failure is less than the ultimate compressive stress that the material is capable of withstanding. |
| Buckling onset strain | Strain at which buckling occurs. At this point, the roughness of 2D nanostructures under compressive loading increases suddenly. |
| Euler buckling formulation | In structural mechanics, this formula involves defining the critical axial load for buckling of long columns. |
| Failure mechanisms | The basic material behavior that resulted in the failure. Examples of failure mode include: ductile fracture, brittle fracture, fatigue fracture, corrosion, erosion, wear and distortion. |
| In-plane stiffness | In-plane stiffness is the rigidity of a 2D nanostructure in response to an applied force on the surface of the structure. The in-plane stiffness of graphene has been determined experimentally to be 1 TPa, whereas its stiffness in the direction perpendicular to the layer is negligible. |
| Ripples | Ripples are small waves on the surface of 2D nanostructures due to functionalization and/or thermal fluctuations. |
| Simply supported boundary condition | A boundary condition in which both ends of the structure are free to rotate and cannot experience any deflection. |
| Thermal conductivity | A measure of the ability of a substance to conduct heat, determined by the rate of heat flow normally through an area in the substance divided by the area minus the component of the temperature gradient in the direction of flow. |
| Thermal fluctuations | In statistical mechanics, thermal fluctuations are random deviations of a system from its average state that occur in a system at equilibrium. All thermal fluctuations become larger and more frequent as the temperature increases, and likewise they decrease as temperature approaches absolute zero. |

## 1. Introduction

Graphyne (GY) is a hypothesized allotrope of graphene. It is a combination of sp and sp² hybridiza-tion states in a flat lattice one-atom thick (like graphene). It can be constructed by inserting acet-yelene bonds in place of carbon–carbon single bonds in two nearest-neighbor hexagonal rings in a gra-phene lattice in a uniform distribution.¹ There are various types of this nanostructure based on the number and the insertion positions of these acety-lenic groups in graphene. These are $\alpha$, $\beta$, and $\gamma$ types with GY and graphdiyne (GDY) being the subtypes under the $\gamma$-GY family. These two types have be-come a focal point of research in recent years due to their significant electronic, optical and mechanical properties.² It is to be noted that GDY contains two acetylenic linkages in each of its unit cells, and the single acetylenic group corresponds to the GY structure as depicted in Fig. 1. Thus, GDY is a softer material than GY in view of its mechanical properties. The atomic structure of GY was pro-posed for the first time by Baughman et al. in 1987.³ They found GY to be structurally stable and syn-thetically obtainable.⁴ In 2010, Li et al.⁵ successfully produced large films of GDY on copper surface via a cross-coupling reaction using hexaethynylbenzene. However, in spite of several organometallic syn-thetic methodologies that have been developed to synthesize GY, it has not been produced experi-mentally in significant quantities and only trace amounts have been fabricated at the molecular level.⁶,⁷ Considering the rapid progress in synthetic tools, it is expected that GY can also be obtained experimentally in the near future.

Motivated by the advances in synthesis, the in-triguing properties of GY due to its unique carbon lattice have attracted considerable attention in re-cent years. Currently there are very limited theo-retical and numerical works on the structural⁸,⁹ and electronic¹⁰,¹¹ properties of GY and even fewer reports on its mechanical properties. Conducting a molecular dynamics (MD) simulation, the mechani-cal properties and failure mechanisms of four differ-ent types of GY under tensile loading were explored by Zhang et al.² It was found that the presence of the acetylenic linkages in GYs has a significant effect on the deterioration of their mechanical properties, with the degree of reduction being proportional to

1550105-2

![](./images/814616203585650689_1.jpg)

Fig. 1. Atomic structure of (a) GY with single acetylenic linkages and (b) GDY with di-acetylenic linkages.

the percentage of linkages. Furthermore, Yang and $Xu^{4}$ performed MD simulations to obtain the fracture strains and the associated ultimate stresses of GY and its family in tension. They predicted that GY has direction-dependent mechanical properties implying that the GY family forms promising materials for applications in novel carbon-based nanocomposites. Also, the variation in GY mechanical properties due to the presence of structural defects was thoroughly studied in a series of MD simulations. $^{12}$ Regarding the strong mechanical properties and excellent chemical and thermal stability of GY, several methods, based on first-principles calculations, such as density functional theory (DFT) have been implemented. $^{13,14}$ Employing DFT, Cranford and Buehler, $^{1}$ obtained the equilibrium and the minimized structure of GY, and then implemented MD simulations using Large-scale Atomic/Molecular Massively Parallel Simulators (LAMMPs) $^{15}$ to explore its superior mechanical properties. They showed that this type of new material differs in important aspects from graphene, important for developing advanced composites. Moreover, using the same approach, Yue et al. $^{16}$ carried out first-principles calculations to find the elastic constants of GY family and found the relation between the in-plane stiffness and the number of acetylenic linkages in different types of this nanostructure.

Regarding the optical and electrical properties, however, it is noted that the special atomic structure (the existence of acetylenic linkages) may potentially lead to quite different physical properties from those of graphene. For example, Malko et al. $^{17}$ found that the electronic properties of one of the substructures of GY are more interesting than those of graphene This property could help researchers design faster transistors and other electronic components that process one-way current. Another important difference between GYs and graphene is that their thermal conductivity is due to the existence of acetylenic linkage in GYs. $^{18}$ These advantages have motivated researchers to investigate the tuning of physical properties of GYs One way of tuning these properties is their functionalization with hydrogen which has recently received increasing attention. $^{19,20}$ It should be pointed out that due to the presence of carbon-carbon triple bonds in GYs, the chance of introducing adatoms such as hydrogen is a possibility. Previous studies have indicated that because of their additional in-plane $\pi$ states, GYs display an enhanced binding energy to metals such as Li and Ca. These metal-decorated GYs can be ideal adsorbents for hydrogen as a renewable and environmentally friendly source of energy. Rajabpour et al. recently found that hydrogen functionalization can significantly change the thermal conductivity of GY. $^{18}$

Motivated by the advances made in GY hydrogenation, several studies have devoted to the analysis of the variations in the optical and electronic properties of this material with hydrogenation. Also, due to changes in the morphology of GY during hydrogen adsorption it is anticipated that the adsorption could result in a drastic deterioration in the mechanical behavior of the functionalized GYs. The subject of the mechanical behavior of hydrogenated graphene nanoribbons (HGNRs) has been thoroughly investigated. $^{21,22}$ Regarding the GY family, there are few works so far covering this issue. Using first-principles DFT approach, Mirnezahd et al. $^{23}$ showed that hydrogen functionalization can significantly alter the mechanical properties of these nanostructures under tensile loading. The behavior of the GY family under compressive loading has not, however, been examined.

1550105-3

A. Montazeri et al.

We now turn to the analysis of the buckling behavior of hydrogenated graphyne (HGY) subject to compressive loading to see how the general mechanical performance of this material is affected, and how efficiently external loads are transferred from the matrix to the nanoinclusions in GY-based composites. The primary objective of this paper is to examine, via MD simulations, the effect of hydrogen adsorption on the mechanical behavior of GYs under axial compressive loading. To our knowledge, no numerical modeling of the buckling of HGYs has been reported so far. In particular, we have considered the deterioration in the stability of HGYs due to adsorbed atoms at very low temperatures. In this way we make sure that any distortion in the geometry of the GY sheet, that might underlie its buckling behavior, is purely due to the action of interatomic forces rather than emanating from thermal fluctuations.

## 2. Details of MD Simulations
The procedure adopted for performing MD simulations of hydrogenated GYs is described in this section. The simulations were conducted using the massively parallelized LAMMPS software package.¹⁵ The adaptive intermolecular reactive bond order (AIREBO) potential,²⁴ which has proven its accuracy in modeling the mechanical properties of pristine graphene and HGNRs, was used to describe the energetics of all the C–C and C–H covalent bonds of HGYs.

The potential has the general form of

$$
E=\frac{1}{2} \sum_{i} \sum_{j \neq i}\left[E_{i j}^{\mathrm{REBO}}+E_{i j}^{L J}+\sum_{k \neq i, j} \sum_{l \neq i, j, k} E_{k i j l}^{\mathrm{TORSION}}\right],
\tag{1}
$$

where $E_{i j}^{\mathrm{REBO}}$ has the same functional form as the hydrocarbon REBO potential due to Brenner and the other two terms are included to model the long-ranged interactions and dihedral angle preferences in hydrocarbon configurations, respectively. Detailed explanation of the terms of this potential can be found in Refs. 24 and 25.

The simulated system consisted of a rectangular GY of length 20 nm and width 4.4 nm composed of 3125 carbon atoms. To investigate the effects of hydrogen adsorption on the buckling behavior of GY, the hydrogen atoms, with a coverage in the range 0–50%, were initially randomly distributed on the GY. To avoid GY edge deformation, simply supported boundary conditions were imposed on both sides of HGYs to prevent the end atoms of the surface to move in the $z$-direction. To avoid the influence of thermal fluctuations on the buckling behavior, the simulations were performed in a canonical ensemble at a constant low temperature of $T=0.01$ K. The equilibrated dimensions of the computational cell were obtained within an NPT ensemble at the specified temperature. Initial velocities were sampled from a Maxwell–Boltzmann distribution at the given temperature. In order to control the simulation temperature, the Nose–Hoover thermostat²⁶ was implemented. The use of this thermostat leads to less fluctuations in the temperature. Moreover, the velocity-Verlet integration algorithm²⁷ was utilized for integrating the equations of motion with a time step $\delta t=0.5$ fs. This time step provided a good balance between accuracy and computational costs.

Following equilibration, in order to examine the effects of hydrogen adsorption on the stability behavior of GYs, an axial compression with appropriate boundary conditions, was applied to obtain the desired mechanical properties. To this end, the boundary atoms at both ends of HGYs were displaced incrementally toward each other with a strain rate of $0.85 \times 10^{-3} \mathrm{ps}^{-1}$ within an NVT ensemble. Each incremental end-displacement of the samples was then followed by re-equilibration of the whole system to acquire the new atomic positions. The incremental displacements were continued in each case until the onset of buckling.

## 3. Results and Discussions
Several cases involving functionalized GYs with different hydrogen coverage, and subject to a uniaxial compressive loading, were studied in a series of MD simulations. Firstly, in order to have a criterion for investigating the influence of the H adatoms on the stability behavior of a pristine GY, we computed the strain for the onset of buckling of the pure GY. It should be noted that there are several criteria available in the literature to obtain the strain for the onset of buckling in nanostructures subject to compressive loading conditions. Among these we chose a displacement-based approach, called the square-average method. According to this method, at the buckling point, the roughness of the system which can be measured by the square-average of the

1550105-4

out-of-plane displacements of the GY atoms ($\langle h^2 \rangle$), suddenly increases. Using this criterion, the strain for onset of buckling for the pristine GY was obtained to be 1.7%. Unfortunately, no data are available for the strain value pertinent to this new graphene allotrope. Thus, to validate the model, the result was compared with the corresponding values of pristine graphene nanoribbons that are available in the literature.

There are several numerical$^{28,29}$ and experimental investigations$^{30}$ that have reported the buckling strain of perfect GNRs under laterally supported boundary conditions to be of the order of 0.7%, which is much smaller than the same parameter for the GY under identical conditions. Comparing the buckling onset strain of these two structures, and considering the existence of triple C–C bonds in the GY structure which are stiffer and harder to rotate in compressive loading, it seems that our obtained results for GY are reasonable. Consequently, what we are proposing is that due to the larger bending rigidity of the triple bonds of the GY, the out-off plane rotation of this type of C–C bond due to application of an axial compressive loading is harder in comparison with the single bonds available in the GNR, and this may be responsible for delaying the onset of buckling.

The question can be raised as to why we have not employed, for example, the nonlinear stability theory, based on the Euler buckling formulation, and have opted for the MD simulation modeling. In this regard, it is worth mentioning that to examine the applicability of the Euler buckling theory to the dynamical compression of planar nanostructures, a comprehensive study is available in the literature.$^{31}$ In that work, several MD simulations were performed to examine the applicability of the Euler buckling theory to the dynamical compression of one of the most important 2D nanostructures, i.e., MoS$_2$ at different strain rates, and for different geometrical characteristics, and also for various patterns of the wrinkled morphology. It was found that the theory was not applicable in the presence of many ripples in the buckling mode, and the Euler buckling theory was valid only if it was applied to a single ripple in the buckled 2D nanostructure. As will be graphically displayed later, the hydrogen adsorption leads to a wrinkled structure of GY composed of many ripples. Thus, as anticipated in the aforementioned paper, we cannot compare the results of MD simulations with the theoretical results obtained from a nonlinear stability analysis.

Using a similar approach, we now proceed further to investigate the coverage-dependent stability behavior of HGYs. This should be taken into account when analyzing the load-bearing characteristics of these nanostructures in advanced composites. In order to find the buckling threshold of HGYs, the $\langle h^2 \rangle$ of the GY atoms subjected to an axial compression was computed and is depicted in Fig. 2. This figure shows the variation of $\langle h^2 \rangle$ with the applied compressive strain for different hydrogen coverage in the range 0–50%. Also, Fig. 3 indicates

![](./images/814616203585650689_2.jpg)

Fig. 2. Variations in the square-average out-of-plane displacement with applied compressive strain, for GYs with different hydrogen coverage.

![](./images/814616203585650689_3.jpg)

Fig. 3. Variations of the buckling onset strain for GYs with various adsorbed H atoms coverage.

![](./images/814616203585650689_4.jpg)

Fig. 4. Variations in the compressive stress with applied strain for GYs with different hydrogen coverage (Solid circles show buckling onset points).

the corresponding strain for the onset of buckling for these cases. For more clarity, Fig. 4 has been calculated to show the variations of the compressive stress with the applied strain. As can be seen from this figure, the magnitude of the stress first increases and then, beyond the buckling onset point its behavior is reversed. The solid circles indicate the buckling onset point for each case indicating that Fig. 4 is in good agreement with the results from Figs. 2 and 3.

As can be concluded from these results, GYs with a higher hydrogen adsorption buckle at smaller compressive strains. This emanates from the fact that hydrogen adsorption changes the morphology of the GY by conversion of the stiff in-plane carbon bonding in its structure to the out-of-plane bonding which is weaker and easier to bend during compression. To better understand this phenomenon, the structure of pristine GY, the sample containing $5\%$ H atoms, and the case with $50\%$ H atoms in the equilibrium state and also at the buckling onset are illustrated in Figs. 5-7, respectively. It is noted that as mentioned earlier, during all the simulations, the temperature was set at a very low value of $T=0.01$ K to avoid the contribution of thermal fluctuations to the results. In this manner, it is concluded that H adsorption was the only dominant mechanism in the buckling of HGYs. Such a mechanism was derived before by the authors in the case of HGNRs.$^{32}$

To have a better comparison, all results of $\langle h^{2}\rangle$ for the hydrogenated GYs at the equilibrated state, and the corresponding strain for the buckling onset are summarized in Table 1. The results show that in spite of the detrimental role of the H adsorption on the stability of GYs for the small number of adsorbed hydrogen atoms, beyond a critical value $(\sim 30\%)$, this phenomenon does not have any significant extra effect and that the results eventually reach a plateau. In other words, beyond the critical value, the GY stability is independent of hydrogen adsorption. Such a behavior was formerly observed for the HGNRs.$^{32}$ In the case of HGNRs, it was previously reported by the authors that, when the H coverage exceeded a critical value, less ripples

![](./images/814616203585650689_5.jpg)

Fig. 5. Snapshots of the structure of pristine GY in equilibrium (a) and at the buckling onset strain of $1.7\%$ (b).

![](./images/814616203585650689_6.jpg)

Fig. 6. Snapshots of the structure of GY containing $5\%$ hydrogen atoms in equilibrium (a) and at the buckling onset strain of $0.8\%$ (b).

![](./images/814616203585650689_7.jpg)

Fig. 7. Snapshots of the structure of GY containing $5\%$ hydrogen atoms in equilibrium (a) and at the buckling onset strain of $1\%$ (b).

1550105-6

**MD Modeling of Buckling Behavior of HGY**

Table 1. Buckling onset strain and $\langle h^2 \rangle$ for the samples with different hydrogen coverage.

<table>
  <thead>
    <tr>
      <th>H coverage (%)</th>
      <th>Buckling onset strain (%)</th>
      <th>$\langle h^2 \rangle$ at the equilibrium state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1.7</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.15</td>
      <td>1.1</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.9</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.8</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.7</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>15</td>
      <td>0.7</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.7</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>25</td>
      <td>0.7</td>
      <td>0.42</td>
    </tr>
    <tr>
      <td>30</td>
      <td>0.8</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td>40</td>
      <td>1.0</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td>50</td>
      <td>1.0</td>
      <td>0.51</td>
    </tr>
  </tbody>
</table>

in the GNR were observed due to the presence of vastly compressive surface stresses induced by the compactified atoms. Here again this fact manifested itself by stopping the formation of extra ripples in the GY morphology due to H adsorption beyond a critical value. It is noted that there is little difference between these two cases (HGNRs versus HGYs). The previous computational works show that physisorption and chemisorption of $H_2$ molecules$^{33}$ and H atoms$^{34}$ on GNRs cause the intensity of the ripples of GNR to first increase with increasing $H_2$ (H) coverage until a critical value is reached, and then begins to decrease. Meanwhile, in the case of GY, the trend gradually changes and reaches a plateau as mentioned before. This is due to the lower density of the GY in comparison with the GNRs. As has been mentioned in the literature,$^{1,2}$ the density of GY is only one-half of that of graphene nanoribbons. Zhao *et al.*$^{35}$ calculated the area density of these two carbon allotropes. The results specified that this parameter is $0.2902\ \text{\AA}^{-2}$ for the GY, which is smaller than that of the graphene which was found to be $0.3818\ \text{\AA}^{-2}$ [Fig. 1(a)]. Thus, hydrogen atoms are less compactified in the case of GY leading to a different trend, verifying our results.

## 4. Conclusions
In summary, MD simulations were carried out to explore the effects of hydrogen adsorption on the stability behavior of GY. To eliminate the influence of thermal fluctuations on the results, the temperature was set at a very low value of $T=0.01\ \text{K}$ in all simulations. The calculated results show that, under identical conditions, this new graphene allotrope is stiffer against buckling in comparison with the graphene nanoribbon. This behavior is contributed to the existence of triple C–C acetylene bonds available in the GY structure which are hard to rotate and bend in compression, and can thus postpone the onset of buckling. The verified model was then used in the next step to evaluate the effect of H adsorption on the buckling onset strain of HGYs. The results reveal that GYs with higher H adatoms buckle at smaller values of compressive strain. This behavior comes from the fact that hydrogen adsorption changes the morphology of GY by conversion of the stiff in-plane carbon bonds in its structure to the out-of-plane bonds which are weaker and easier to bend in compression. Finally, it was found that there is a critical value of adsorption above which the stability behavior of HGYs is *slightly* affected by the presence of more hydrogen atoms. The present work offers a better insight into the mechanical properties of HGYs in compression when analyzing the load-bearing characteristics of these nanostructures in advanced composites.

## References
1. S. W. Cranford and M. J. Buehler, *Carbon* **49**, 4111 (2011).
2. Y. Y. Zhang, Q. X. Pei and C. M. Wang, *Appl. Phys. Lett.* **101**, 081909 (2012).
3. R. H. Baughman, H. Eckhardt and M. Kertesz, *J. Chem. Phys.* **87**, 6687 (1987).
4. Y. Yang and X. Xu, *Comput. Mater. Sci.* **61**, 83 (2012).
5. G. X. Li, Y. L. Li, H. B. Liu, Y. B. Guo, Y. J. Li and D. B. Zhu, *Chem. Commun.* **46**, 3256 (2010).
6. M. M. Haley, *Pure Appl. Chem.* **80**, 519 (2008).
7. K. S. Kim, Y. Zhao, H. Jang, S. Y. Lee, J. M. Kim, K. S. Kim, J. H. Ahn, P. Kim, J. Y. Choi and B. H. Hong, *Nature* **457**, 706 (2009).
8. N. Narita, S. Nagai, S. Suzuki and K. Nakao, *Phys. Rev. B* **58**, 11009 (1998).
9. Q. Zheng, G. Luo, Q. Liu, R. Quhe, J. Zheng, K. Tang, Z. Gao, S. Nagase and J. Lu, *Nanoscale* **4**, 3990 (2012).
10. J. Zhou, K. Lv, Q. Wang, X. S. Chen, Q. Sun and P. Jena, *J. Chem. Phys.* **134**, 174701 (2011).
11. K. Srinivasu and S. K. Ghosh, *J. Phys. Chem. C* **116**, 5951 (2012).
12. S. Ajori, R. Ansari and M. Mirnezhad, *Mater. Sci. Eng. A* **561**, 34 (2013).
13. J. Kang, J. Li, F. Wu, S. S. Li and J. B. Xia, *J. Phys. Chem. C* **115**, 20466 (2011).

1550105-7

A. Montazeri et al.

14. Q. Peng, W. Ji and S. De, *Phys. Chem. Chem. Phys.* **14**, 13385 (2012).

15. S. Pilmpton, *J. Comput. Phys.* **117**, 1 (1995).

16. Q. Yue, S. Chang, J. Kang, S. Qin and J. Li, *J. Phys. Chem. C* **117**, 14804 (2013).

17. D. Malko, C. Neiss, F. Viñes and A. Görling, *Phys. Rev. Lett.* **108**, 086804 (2012).

18. A. Rajabpour, S. M. VaezAllaei and M. Jalalvand, Thermal conductivity of hydrogen functionalized graphyne and graphdiyne: A nonequilibrium mo- lecular dynamics study, *5th Int. Conf. Nanos- tructures (ICNS5)*, Kish Island, Iran (2014).

19. A. Rajabpour, S. M. VaezAllaei and F. Kowsary, *Appl. Phys. Lett.* **99**, 051917 (2011).

20. Y. Ma, Y. Dai, Y. Lu and B. Huang, *J. Mater. Chem. C* **2**, 1125 (2014).

21. Q. X. Pei, Y. W. Zhang and V. B. Shenoy, *Carbon* **48**, 898 (2010).

22. N. A. Popova and E. F. Sheka, *J. Phys. Chem. C* **115**, 23745 (2011).

23. M. Mirnezhad, R. Ansari, H. Rouhi, M. Seifi and M. Faghihnasiri, *Solid State Commun.* **152**, 1885 (2012).

24. S. Stuart, A. B. Tutein and J. A. Harrison, *J. Chem. Phys.* **112**, 6472 (2000).

25. D. W. Brenner, O. A. Shenderova, J. A. Harrison, S. J. Stuart, B. Ni and S. B. Sinnott, *J. Phys. Condens. Mater.* **14**, 783 (2002).

26. W. G. Hoover, *Phys. Rev. A* **31**, 1695 (1985).

27. M. P. Allen and D. J. Tildesley, *Computer Simula- tion of Liquids* (Oxford University Press, New York, 1986).

28. M. Neek-Amal and F. M. Peeters, *Appl. Phys. Lett.* **97**, 153118 (2010).

29. Q. Lu and R. Huang, *Int. J. Appl. Mech.* **1**, 443 (2009).

30. G. Tsoukleri, J. Parthenios, K. Papagelis, R. Jalil, A. C. Ferrari, A. K. Geim, K. S. Novoselov and C. Galiotis, *Small* **5**, 2397 (2009).

31. J. W. Jiang, *Sci. Rep.* **5**, 7814 (2015).

32. A. Montazeri, S. Ebrahimi and H. Rafii-Tabar, *Mol. Simul.* **41**, 1212 (2015).

33. S. Ebrahimi, A. Montazeri and H. Rafii-Tabar, *Solid State Commun.* **159**, 84 (2014).

34. Z. Zhang, B. Liu, K. C. Hwang and H. Gao, *Appl. Phys. Lett.* **98**, 121909 (2001).

35. J. Zhao, N. Wei, Z. Fan, J. Jiang and T. Rabczuk, *Nanotechnology* **24**, 095702 (2013).

1550105-8