Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: B. Zheng, L. Wang, L. Du, J. Hui, H. Du and M. Zhu, *Dalton Trans.*, 2015, DOI: 10.1039/C5DT03861H.

![](./images/814570334232510464_1.jpg)

This is an **Accepted Manuscript**, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

**Accepted Manuscripts** are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this **Accepted Manuscript** with the edited and formatted Advance Article as soon as it is available.

You can find more information about **Accepted Manuscripts** in the [Information for Authors].

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions] and the [Ethical guidelines] still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this **Accepted Manuscript** or any consequences arising from the use of any information it contains.

![](./images/814570334232510464_2.jpg)

www.rsc.org/dalton

# Impact of mechanical deformation on guest diffusion in zeolitic imidazolate frameworks

Bin Zheng,‡*a Lian Li Wang,‡a Jia Chen Hui,‡a Lifei Du,‡a Huiling Du‡a and Ming Zhu‡a

The effect of the mechanical deformation of metal-organic frameworks on guest diffusion was investigated employing molecular dynamics simulations. Two basic deformation modes, uniaxial tensile and shear deformation, were considered. The computed shear modulus of the zeolitic imidazolate framework-8 (ZIF-8) model system was much lower than the Young's modulus, which is in agreement with experimental results. The diffusion rate in ZIF-8 was calculated for two types of guest molecules: the nonpolar H₂ and the quadrupolar CO₂. Under tensile strain, the diffusion of both H₂ and CO₂ was found to be enhanced, whereas the diffusion rates did not change significantly under shear loading. The evolution of the internal structure of ZIF-8 was studied to determine its effect on the guest diffusion. The organic-inorganic connection was identified as source of the framework's flexibility, and therefore we focused on the N-Zn bond and the N-Zn-N angle. Under stretching deformation, the N-Zn bond is elongated and the N-Zn-N angle remains constant. Thus, the length of the C2-C2 long bond, determining the size of the 6-membered ring (6MR) gate, increases and the gate is opened, allowing for a faster guest diffusion. Under shear deformation, the N-Zn bond length changes very little and the N-Zn-N angle is distorted. This results in the occurrence of three peaks in the C2-C2 bond length distribution. Although the 6MR gate is distorted, the variation of its average size is small, resulting in a very small effect on the guest diffusivity. In addition, we found that the fluctuation of the ZIF-8 cell can enhance the impact of the mechanical deformation of the host on the guest diffusion.

## 1. Introduction

Metal-organic frameworks (MOFs) are porous crystalline solids which exhibit a flexible and tunable porous structure. Due to their peculiar properties, MOFs received much attention and are considered for a wide range of applications, e.g., for gas storage, separation, sensing and catalysis. The mechanical deformation of MOFs has recently received special attention both from a perspective of fundamental research and due to practical requirements.¹⁻⁴

The exceptional properties of MOFs have sparked enormous efforts towards finding feasible fabrication methods, for instance, through the choice of a suitable linker molecule, topology, and metal-linker combination, resulting in an exponentially increasing number of synthesized MOFs.⁵ The major drawbacks of most MOFs are their weak thermal and mechanical stability. For existing stable MOFs, e.g., zeolitic imidazolate frameworks (ZIFs) and zirconium(IV)-based MOFs, the effect of mechanical deformation on the physico-chemical properties of MOFs is still not fully understood, which strongly limits their application potential.⁶

There are two main reasons for studying the effect of mechanical deformation on the properties of MOFs. On the one hand, mechanical deformation provides an opportunity to tune the size and shape of the window and cavity of MOFs and thereby adjust their physico-chemical properties for a certain target application.⁷ Here, we refer to the recoverable deformation, mainly breathing deformation and pure elastic loading in case of non-breathing MOFs. Breathing deformation occurs in soft porous crystals, and can be easily induced by a small change in pressure, even guest molecule adsorption.⁸ In contrast, very rigid frameworks like non-breathing MOFs are better able to withstand external pressure or friction. This modification of a material's properties via mechanical deformation is called elastic strain engineering and was first applied to small-volume or bulk-scale nanomaterials.⁹ On the other hand, engineers do not wish for a significant change of the physico-chemical properties of MOFs after mechanical deformation because it may lead to a deterioration of the chemical functionalities of MOFs.¹⁰

Host deformation and flexibility have been widely studied in the field of zeolites. For instance, Auerbach *et al.*¹¹ simulated the effect of NaY zeolite framework vibrations on the thermodynamic and dynamic behaviours of benzene and reported that the rigid model approach yields results very close to the flexible system. Leroy *et al.*¹² used molecular dynamics (MD) simulations to calculate the diffusion rate of alkanes in rigid and flexible silicalite. However, a correlation between an enhanced diffusion and the host flexibility was only found for the lowest loadings and the shortest alkane

---

ᵃ School of Materials Science and Engineering, Xi'an University of Science and Technology, Xi'an 710054, PR China. E-mail: zhengbin@xust.edu.cn
‡The authors declare no competing financial interest.

molecules. In contrast, the mechanical deformation of both zeolites¹³⁻¹⁵ and MOFs¹,⁴,⁶ has been intensively studied. The elastic constants of zeolites are an order of magnitude lower compared to MOFs, and therefore the flexibility of MOFs enhances the adsorption and diffusion of guest molecules.¹⁶⁻¹⁷ Previous studies focused either on the effect of the flexibility or host deformation. To the best of our knowledge, studies also considering the influence of the coupling between the mechanical deformation and the flexibility on the behaviour of guest molecules, are scarce, both in the fields of zeolites and MOFs.

In this work, we studied the effect of elastic strain on the diffusion of guest molecules in a MOF. ZIF-8 was chosen as a model metal-organic framework because it combines the excellent properties of MOFs and zeolites.¹⁸ Here, we computed the H₂ and CO₂ diffusion rates in ZIF-8 for different shear and tensile strain values. The resulting pore structure under strain was analysed to better understand its effect on the guest diffusion. The obtained relationship between the elastic strain modes of the MOFs and the observed variation of the guest diffusivity is presented and discussed, and is expected to provide a framework and reference for future applications.

## 2. Computational method

![](./images/814570334232510464_3.jpg)

Fig. 1 Illustration of the two basic mechanical deformation modes (uniaxial stretching and shearing) in the ZIF-8.

The simulation box consists of 2×2×2 ZIF-8 unit cells with a lattice parameter of 16.985 Å (resulting in a total of 2208 atoms in the framework ), with periodic boundary conditions (PBC) applied along the three main coordinate directions. For all types of interaction (i.e., bonding, van der Waals, and electrostatic interactions), the verlet-velocity integration algorithm with a time step of 1.0 fs was used. The force parameters for ZIF-8 have been published earlier¹⁷ and all non-bonded interaction cutoff values were selected to 16.0 Å. For the simulation of the CO₂-ZIF interaction force field, we adopted the EPM2 model established by Harris and Yung.¹⁹ The H₂ molecule was treated as a single-centre Lennard-Jones molecule using the potential parameters proposed by Grazzi et al.²⁰

The LAMMPS software²¹, ²² was used to perform the molecular dynamics (MD) simulations. Before deformation, an energy minimization based on the conjugate gradient (CG) algorithm was performed at zero temperature to guarantee the atomic positions during geometric optimization. Then, the system was thermally equilibrated at 300 K for 10 ns using a Langevin thermostat (NVT) model.²³ In a stepwise manner, an external stretching and shearing force was then applied along the z and x direction, respectively. For each step, the uniform strain increment was set to ~1%, and the relaxation time at a constant temperature was set to 5 ns. A 50 ns microcanonical ensemble (NVE) run was then performed and employed to calculate the diffusion rates of the guest molecules in the flexible ZIF-8 matrix utilizing a mean-square-displacement (MSD) method based on the Einstein approximation. We also calculated the guest diffusion rates using an isothermal-isobaric ensemble (NPT), which includes all instantaneous fluctuations of the cell's shape, dimensions and internal structure.

## 3. Results and discussion

![](./images/814570334232510464_4.jpg)

Fig. 2 Variation of (a) the H₂ diffusion rate and (b) the CO₂ diffusion rate with the increasing of elastic strain for tensile and shear deformation. Microcanonical ensemble (NVE) was used to collect data for the diffusion rate calculation.

![](./images/814570334232510464_5.jpg)

Fig. 3 Illustration of the structure of ZIF-8: (a) basic structural unit of ZIF-8 consisting of one Zn atom and four imidazolate linkers, (b) a 4-membered ring gate and (c) a 6-membered ring gate constructed of basic structural units.

Figure 1 illustrates the two basic mechanical deformation modes (uniaxial stretching and shearing) in ZIF-8. All more complicated deformations can be treated as a combination of these two basic types of deformation. As shown in Fig. 1, the tensile and the shear deformation occur along the cube axes and on the {100} planes, respectively. The low anisotropy of the elastic modulus of ZIF-8, verified by the Brillouin scattering spectra,¹ indicates that the current tensile direction is acceptable. Shear deformation occurs on the {100} plane because the shear modulus is lowest for this plane, which has been verified by both experiments and theoretical calculations.¹

We started the validation of our model focusing on the Young's modulus and shear modulus of the empty ZIF-8 matrix. Therefore, we collected the stress data for every atom along the deformation direction and divided the sum of the stress by the system volume to obtain the deformation stress for the different strain values. Then, the stress–strain relation for the empty ZIF-8 was established and a linear fitting was performed to obtain the slope of the curves, i.e., the moduli. The shear modulus was calculated to 3.94 GPa and the Young's modulus to 16.52 GPa. Both values are much larger than the experimental values (0.97 GPa and 3.77 GPa, respectively).¹ This demonstrates the difficulty of predicting the absolute values of the mechanical moduli when employing MD simulation in combination with a semi-empirical force field. Although there is a rather large deviation between the predicated absolute values and the experimental data, our model was able to reproduce the small shear modulus to Young's modulus ratio. This result does satisfy the requirements of the current study, in which we focused only on the effect of the ZIF-8 deformation on the guest molecule diffusivity.

Figure 2 shows the variation of the guest diffusion rate with the elastic strain. In Fig. 2, three trends are of interest. First, an increase in tensile strain results in a higher diffusion rate for both the H₂/ZIF-8 and the CO₂/ZIF-8 system. The CO₂ diffusion rate under a tensile strain of 0.10 is about 4.5 times larger than the rate observed for zero strain, compared to an increase by a factor of 1.9 for H₂ guest molecules. Correspondingly, the H₂/CO₂ separation factor, computed by using the ratio of the diffusion rates, decreased from 141 to 58 with increasing tensile strain, due to the faster increase of the CO₂ diffusion rate. Second, the H₂ diffusivity is slightly reduced by up to 15% until the shear strain reaches 0.095. A further increase in shear strain had no effect on the H₂ diffusion rate. Finally, it is worth noting that the effect of shear deformation on the diffusion of CO₂ is ignorab le. The average CO₂ diffusion rate was determined to be 1.32 (10⁻¹⁰ m²/s) with a standard error of 0.152. The maximum fluctuation is 12%, which is comparable to the 15% decrease of the H₂ diffusion rate. Therefore, the effect of the shear deformation on the guest diffusivity is weak.

Both the preliminary results and previous studies¹, ²⁴ suggest an easy mechanical deformation of ZIF-8 under shear stress. This preferable deformation mode will not result in a significant reduction of the separation ability of ZIF-8 (Fig. 2). The H₂/CO₂ separation factor for ZIF-8 under shear stress is 136±24. This encourages the industrial application of MOFs, which requires a high stability of the physico-chemical properties under mechanical deformation.²⁵

To identify the main factor contributing to the variation if the diffusion rates, we studied the evolution of the structure of the host framework with increasing elastic strain. First, the structure of ZIF-8 is analysed in Fig. 3. The basic structural unit of ZIF-8 is constructed of one Zn atom and four imidazolate

![](./images/814570334232510464_6.jpg)

Fig. 4 Distributions obtained for (a) the N–Zn bond length, (b) the N–Zn–N angle and (c) the length of the C2–C2 long bond of ZIF-8 for different applied uniaxial tensile strains. Two different systems, H₂/ZIF-8 (left) and CO₂/ZIF-8 (right), were investigated.

![](./images/814570334232510464_7.jpg)

Fig. 5 Distributions obtained for (a) the N-Zn bond length, (b) the N-Zn-N angle and (c) the length of the C2-C2 long bond for different applied shear strains. Two different systems, $H_2$/ZIF-8 (left) and $CO_2$/ZIF-8 (right), were investigated.

linkers with a tetrahedral topology (Fig. 3a). This configuration, consisting of N-Zn bonds and N-Zn-N angles, corresponds to a hybrid structure featuring both organic and inorganic parts, and is believed to be weakly in ZIF-8, allowing it to resist external loading. $^{1}$ Using the pliant $ZnN_4$ tetrahedra, a model consisting of two completely flexible gates, a 4-membered ring (Fig. 3b) and a 6-membered ring (6MR) gate (Fig. 3c) can be constructed. Especially the 6MR gate with a diameter of $3.4\ \mathring{A}$ serves as the main access point for guest molecules, allowing them to jump between adjacent cavities. The size of the 6MR gate can be described using the length of the C2-C2 long bond (yellow). $^{26}$ Therefore, the N-Zn bond, the N-Zn-N angle and the C2-C2 long bond in ZIF-8 are the three most important structural parameters responding to an external load.

The distribution of the structural parameters was studied to investigate the flexibility of ZIF-8 under loading. $^{27}$ For every complete distribution, the ZIF-8 configurations were recorded at intervals of 0.5 ps during a 50 ns trajectory, and all N-Zn bond lengths, N-Zn-N angles and C2-C2 bond lengths included in each configuration were calculated. The resulting distributions of the characteristic bond lengths and angles are illustrated in Fig. 4 and Fig. 5.

For both the $H_2$/ZIF-8 and the $CO_2$/ZIF-8 system, Fig. 4(a) shows that the N-Zn bond becomes more and more stretched with increasing tensile strain, corresponding to a right shift of the distribution. In contrast, the shift of the N-Zn-N angle distribution is inconspicuous (Fig. 4b), although there is a slight broadening of the peaks under high strain. As a result, the increase of the N-Zn bond length under uniaxial loading is responsible for the right shift of the C2-C2 long bond distribution (Fig. 4c). An increase of the C2-C2 bond length opens the gate, thereby enhancing the guest diffusion in ZIF-8 (cp. Fig. 2). This effect is more prominent for the $CO_2$/ZIF-8 system than for the $H_2$/ZIF-8 system. However, the $CO_2$ molecule is larger and therefore the $CO_2$ diffusion is more sensitive to a change in gate size.

Compared to the stretching deformation, the variation of the characteristic structural parameters of ZIF-8 under shear loading is totally different. Fig. 5(a) reveals that the length of the N-Zn bonds remains constant even under a high shear strain of 0.12. The length distributions for different strains obtained for both the $H_2$/ZIF-8 and the $CO_2$/ZIF-8 system coincide. However, shearing deformation was found to have a strong impact on the N-Zn-N angles (Fig. 5b). The main peaks of the angle distributions shift to the left with increasing shear strain. At the same time, a new shoulder peak appears on the right, corresponding to a larger angle. The shoulder peak can clearly be seen in the distribution corresponding to a strain of 0.12 (Fig. 5b). Although hidden by the low resolution, the shoulder exits even during the initial stage of shearing deformation. Compared to the N-Zn bond, the N-Zn-N angle more strongly responds to the shear loading, which confirms that the ZIF-8 is susceptible to shearing deformation.

The variation of the N-Zn-N angle affected the distribution obtained for the C2-C2 long bond. In Fig. 5(c), two new peaks appeared under shear loading, located at the left and right side of the original peak. The three peaks in Fig. 5(c) correspond to the three C2-C2 bond lengths describing one 6MR gate (yellow). This means that the 6MR gate is distorted under shear loading. The distortion is triggered by the new peak in the N-Zn-N angle distribution. As shown in Fig. 3(c), one N-Zn-N angle can control the orientation of one imidazolate linker which influences two C2-C2 long bonds in one gate. That is why there are two peaks in the N-Zn-N angle distribution (Fig. 5b) but three peaks in the C2-C2 long bond distribution (Fig. 5c).

According to the analysis above, tensile and shear loading result in an opening of the 6-MR gate (Fig. 4c) and gate distortion (Fig. 5c), respectively. The faster diffusion of the guest molecules in ZIF-8 can be easily traced back to the larger 6MR gate diameter. It is more difficult to understand, why the distortion of the gate has little effect on the diffusion rates. On the one hand, the gate distortion during elastic deformation of ZIF-8 is not large enough to block or push the guest molecules. The biggest deviation in length observed for the C2-C2 long bond during shear loading is around 10%. The diffusion of point-like ($H_2$) and linear ($CO_2$) guest molecules is not affected by this small distortion. On the other hand, the average length of the C2-C2 long bond (cp. Table 1) under shear stress is almost constant (an increase by 1.7%), compared to the increase by 8% under stretching deformation. This small opening of the 6MR gate has little effect on the diffusion rate

of H₂ and CO₂ guest molecules. Therefore, the effect of shear strain on the guest molecule diffusion is weak.

**Table 1. Average length of C2–C2 long bond under different tensile and shear strain. The definition of C2–C2 long bond can be found in Figure 3(c).**

| | 0% Strain | 7% Strain | 10% Strain |
| --- | --- | --- | --- |
| Average length of the C2–C2 long bond (Å) in ZIF-8 under tensile strain | 5.15 | 5.40 | 5.54 |
| Average length of the C2–C2 long bond (Å) in ZIF-8 under shear strain | 5.15 | 5.20 | 5.24 |

The simulation and analysis results presented above, which were obtained at a constant-volume in the (NVT) and (NVE) ensembles, neglect the effect of the fluctuations of the unit cell's shape and dimensions. In order to consider all fluctuations, we performed an isothermal–isobaric ensemble (NPT) run to collect data for the calculation of the diffusion rates (Fig. 6). As shown in Fig. 6(a), the effect of shear deformation of ZIF-8 on the guest diffusivity is weaker than the effect of tensile deformation, which is in good agreement with the results obtained for the NVE ensemble. When comparing the diffusion data in Fig. 2(a) and Fig. 6(a), we found two significant differences. First, we obtained much smaller diffusion rates for the NPT ensemble (Fig. 3a) than for the NVE ensemble (Fig. 2a). Using an NPT ensemble leads to a reduction of the CO₂ diffusion rates by about 90%. This strong reduction is attributed to the shrinking of the cell, which narrows the ZIF-8 gates, regardless whether the gate is open or closed. In contrast, the small expansion of the cell observed for the NPT ensemble has little effect on the guest diffusion, especially when the gate is closed. However, the shrinking of the cell has a tremendous effect on the self-diffusivity of sorbate molecules whose dynamic radius is comparable to the gate size, such as the CO₂ molecules. Second, the impact of the host deformation on the guest diffusion is underestimated when using the NVE ensemble. Figure 6(b) presents the ratios of the CO₂ diffusion rate in strained ZIF-8 to the diffusion rate in the unstrained framework. Obviously, the diffusion rates calculated using the NPT ensemble more strongly increase with the deformation strain. This is especially true for the shear deformation mode, where the CO₂ diffusion rates remain almost constant in the NVE ensemble run but obviously increase in the NPT ensemble run.

![](./images/814570334232510464_8.jpg)

Fig. 6 (a) The CO₂ diffusion rates with the increasing of elastic strain for tensile and shear deformation calculated in NPT ensemble. (b) The ratio of CO₂ diffusion rate at strained ZIF-8 (D) to that at unstrained ZIF-8 (D₀) in both of NVE and NPT ensemble. Distributions obtained for the volume of the 2×2×2 ZIF-8 super cell for different applied tensile (c) and shear (d) strains.

In order to better understand the enhancing effect of the host deformation on the guest diffusion in the NPT ensemble, we analysed the variation of the framework volume as a function of the strain. It should be noted that, when using the NVE ensemble, the system volume was fixed while the mechanical strain was increased, which excludes any effect of the framework volume on the guest diffusion rate. Fig. 6(c) and (d) show the volume distribution of the framework for the NPT ensemble for different values of the tensile and shear strain, respectively. The expansion (right shift of the peak in Fig. 6c and d) of the system observed for both deformation modes is responsible for the fast increase of the diffusion rates observed for the NPT ensemble. Why does the system volume expand under high deformation? Coudert et al.³ calculated the elastic constants of ZIF-8 as a function of the mechanical pressure and found that the C₄₄ value drastically decreases, a phenomenon known as shear-mode softening. The softening of the framework under high deformation results in the expansion of ZIF-8.

The framework expansion occurs in both cases, i.e., under both tensile and shear deformation, and thus the enhancing effect of the host deformation on the guest diffusion is independent of the deformation mode. Therefore, the observed effect of the mechanical deformation on the diffusion of guest molecules in ZIF-8 can be mainly attributed to the variation of the internal structure of the framework (cp. Fig. 4 and 5).

## Conclusions
In this work, we have employed molecular dynamics simulations to investigate the relationship between the mechanical deformation of a ZIF-8 host and the diffusion rate of guest molecules. Our model showed that the ratio of the shear modulus to the Young's modulus of ZIF-8 is 0.19, which is low enough to correspond to the susceptibility to shear stress observed in other simulations and experiments. Using this validated model, we found that both the non-polar H₂ and the quadrupolar CO₂ molecules diffuse faster with increasing tensile strain, whereas the effect of shear deformation on the diffusion can be ignored. The size of the 6MR gate under elastic strain is closely related to the variation of the guest molecule diffusion rate. A detailed structural analysis revealed

that a gate-opening and gate-distortion occur under stretching and shearing deformation, respectively. The gate-opening is triggered by an elongation of the N-Zn bond, whereas the gate-distortion is caused by the distortion of the N-Zn-N angle. A larger 6MR gate diameter undoubtedly allows guest molecules to diffuse faster. At the same time, the variation of the average size of the distorted gates is too small to have a significant effect on the guest diffusion. The effect of the mechanical deformation of the host on the diffusion of guest molecules can be enhanced by considering the fluctuation of the ZIF-8 unit cell in an *NPT* ensemble. Framework softening and then volume expansion under high strain lead to the above enhancing effect. This work therefore demonstrates that a tuning of the guest diffusivity can be achieved by choosing proper deformation modes, which, on the one hand, shed a light on the potential application of mechanical deformation to adjust the physico-chemical properties of MOFs, and, on the other hand, may inspire the design and manufacturing of novel MOFs with acceptable losses in chemical functionality.

## Acknowledgements
This work was supported by the Natural Science Foundation of China under grant 21503165, 51372197, the Science and Technology Program of Shaanxi Province (2013KJXX-42), the Key Innovation Team of Shaanxi Province (2014KCT-04), the Major International Joint Research Program of Shaanxi Province (2012KW-10).

## References
1.  J.-C. Tan, B. Civalleri, C.-C. Lin, L. Valenzano, R. Galvelis, P.-F. Chen, T. D. Bennett, C. Mellot-Draznieks, C. M. Zicovich-Wilson and A. K. Cheetham, *Phys. Rev. Lett.*, 2012, **108**, 095502.
2.  Z. Su, Y.-R. Miao, S.-M. Mao, G.-H. Zhang, S. Dillon, J. T. Miller and K. S. Suslick, *J. Am. Chem. Soc.*, 2015, **137**, 1750-1753.
3.  A. U. Ortiz, A. Boutin, A. H. Fuchs and F.-X. Coudert, *J. Phys. Chem. Lett.*, 2013, **4**, 1861-1865.
4.  J. C. Tan, T. D. Bennett and A. K. Cheetham, *Proc. Natl. Acad. Sci. U.S.A.*, 2010, **107**, 9938-9943.
5.  Y. J. Colon and R. Q. Snurr, *Chem. Soc. Rev.*, 2014, **43**, 5735-5749.
6.  J. C. Tan and A. K. Cheetham, *Chem. Soc. Rev.*, 2011, **40**, 1059-1080.
7.  W. Lu, Z. Wei, Z.-Y. Gu, T.-F. Liu, J. Park, J. Park, J. Tian, M. Zhang, Q. Zhang, T. Gentle III, M. Bosch and H.-C. Zhou, *Chem. Soc. Rev.*, 2014, **43**, 5561-5593.
8.  A. U. Ortiz, A. Boutin, A. H. Fuchs and F.-X. Coudert, *Phys. Rev. Lett.*, 2012, **109**, 195502.
9.  J. Li, Z. Shan and E. Ma, *MRS Bull.*, 2014, **39**, 108-114.
10. M. J. Cliffe, W. Wan, X. Zou, P. A. Chater, A. K. Kleppe, M. G. Tucker, H. Wilhelm, N. P. Funnell, F.-X. Coudert and A. L. Goodwin, *Nat. Commun.*, 2014, **5**, 4176.
11. F. Jousse, D. P. Vercauteren and S. M. Auerbach, *J. Phys. Chem. B*, 2000, **104**, 8768-8778.
12. F. Leroy, B. Rousseau and A. H. Fuchs, *Phys. Chem. Chem. Phys.*, 2004, **6**, 775-783.
13. R. Astala, S. M. Auerbach and P. A. Monson, *J. Phys. Chem. B*, 2004, **108**, 9208-9215.
14. R. Astala, S. M. Auerbach and P. A. Monson, *Phys. Rev. B*, 2005, **71**, 014112.
15. M. H. Ford, S. M. Auerbach and P. A. Monson, *J. Chem. Phys.*, 2004, **121**, 8415-8422.
16. H. Tanaka, S. Ohsaki, S. Hiraide, D. Yamamoto, S. Watanabe and M. T. Miyahara, *J. Phys. Chem. C*, 2014, **118**, 8445-8454.
17. B. Zheng, M. Sant, P. Demontis and G. B. Suffritti, *J. Phys. Chem. C*, 2012, **116**, 933-938.
18. L. Bouëssel du Bourg, A. U. Ortiz, A. Boutin and F.-X. Coudert, *APL Mat.*, 2014, **2**, 124110.
19. J. G. Harris and K. H. Yung, *J. Phys. Chem.*, 1995, **99**, 12021-12024.
20. F. Grazzi, M. Santoro, M. Moraldi and L. Ulivi, *Phys. Rev. B*, 2002, **66**, 144303.
21. S. Plimpton, *J. Comput. Phys.*, 1995, **117**, 1-19.
22. http://lammps.sandia.gov.
23. T. Schneider and E. Stoll, *Phys. Rev. B*, 1978, **17**, 1302-1322.
24. S. Cao, T. D. Bennett, D. A. Keen, A. L. Goodwin and A. K. Cheetham, *Chem. Commun.*, 2012, **48**, 7805-7807.
25. D. Bazer-Bachi, L. Assié, V. Lecocq, B. Harbuzaru and V. Falk, *Powder Technol.*, 2014, **255**, 52-59.
26. B. Zheng, Y. Pan, Z. Lai and K.-W. Huang, *Langmuir*, 2013, **29**, 8865-8872.
27. E. Haldoupis, T. Watanabe, S. Nair and D. S. Sholl, *ChemPhysChem*, 2012, **13**, 3449-3452.