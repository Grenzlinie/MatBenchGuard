# Unravelling the Negative Role of Oxygen Vacancy Cluster on Ionic Conductivity in CeO₂: Hybrid Functional Study

Xiaoping Han¹, Noureddine Amrane¹, Zongsheng Zhang²,†, and Maamar Benkraouda¹,*

¹Department of Physics, United Arab Emirates University, Al-Ain, P.O.Box 15551, U.A.E.

²College of International Education, North University of China, Taiyuan 030051, China

* E-mail: maamar@uaeu.ac.ae

† E-mail: zhangzs@nuc.edu.cn


**ABSTRACT:**

Oxygen vacancy formation and migration play a critical role in the high performances of $CeO_2$ as a highly promising material for solving the environmental and energy issues. However, most of associated works were directed towards the single or isolated oxygen vacancies. In this contribution, the formation and migration of oxygen vacancy cluster in $CeO_2$ have been presented in detail using the Heyd-Scuseria-Ernzerhof (HSE) hybrid functional method. The results demonstrate that oxygen vacancies exhibit a strong tendency to cluster in the <111> direction of $CeO_2$. The detailed analyses of formation energy reveal the favorability of forming such a vacancy cluster under O-poor conditions. By means of the climbing-image nudged elastic band (cNEB) method and molecular dynamics (MD) simulations, the vacancy cluster is found to have a high kinetic stability and low mobility, thus becomes a challenge for achieving high ionic conductivity in $CeO_2$.

Attempts have been made to unravel the negative effect of vacancy clustering on ionic conductivity at an atomistic level, and possible means for avoiding or eliminating the vacancy clustering are proposed. The current work has implications for tailoring or optimizing the ionic conductivity in $CeO_2$-based materials or devices for environmental friendly applications.

### I. INTRODUCTION

CeO₂ and related compounds have attracted much interest, due to their extensive applications to dealing with the global environmental and energy issues.¹⁻⁴ For example, CeO₂ has been used as anode and electrolytic materials within the solid oxide fuel cell (SOFC), which is expected to become high-efficiency electrical power generators that enable clean energy production and support sustainable development.⁵⁻⁷ In the purification of automobile exhausts, CeO₂ often acts as three-way catalysts (TWC), oxidizing CO and hydrocarbons to CO₂ and reducing NOₓ to N₂.⁵⁻¹⁰

Also, materials based on CeO₂ are efficient to catalytically bind active species like ionic Au in the water-gas-shift reaction,⁵⁷¹¹⁻¹⁷ thus promoting activity of the catalysts. These outstanding performances are largely due to the good oxygen storage capacity (OSC) of CeO₂, i.e., the ability to store and release oxygen.²¹³¹⁸¹⁹ This originates from the unique redox properties of CeO₂ that, with a fast Ce⁴⁺/Ce³⁺ balance, CeO₂ can store O₂ under O-rich conditions and provide oxygen when O₂ partial pressure decreases, which is directly related to the oxygen vacancy formation and migration properties. Therefore, the favorability of oxygen vacancy formation and diffusion has become critical for enhancing the OSC and ionic conductivity and hence the efficiency of CeO₂-based materials or devices in environmental friendly applications.

It is well known that pure CeO₂ does not possess a good ionic conductivity because of very low concentration of oxygen vacancy. To achieve a good ionic conductivity, a general approach is to introduce more vacancies into CeO₂ through doping. Previous experimental and theoretical

studies showed that doping $CeO_2$ with transition metals like $Mn,^{20-25} Zr^{26-28}$ and rare earth metals (like Y, Pr, Gd, Sm and $Yb)^{20,21,29-35}$ effectively promotes the oxygen vacancy formation and migration, thus enhancing the OSC and ionic conductivity and making $CeO_2$ attractive for a wide variety of applications. However, these investigations were mostly related to the single or isolated vacancies. Actually, in some literatures $^{36-38}$ heavy doping with rare earth elements Sm, Y, Yb, Gd and Dy in $CeO_2$ was reported to cause the oxygen vacancies to cluster in the $<111>^{36}$ or $<110>^{37,38}$ directions, which was found to lower the ionic conductivity instead. This indicates the clustered vacancies influence the ionic conductivity in a different way from the single or isolated vacancies.

Apart from doped $CeO_2$, there have been some explorations performed on the clustered oxygen vacancies in undoped and surface structures of $CeO_2$. Hull et $al^{39}$ used Monte Carlo modelling to show that the oxygen vacancies preferentially align as pairs in the $<111>$ direction of $CeO_2$ as the degree of nonstoichiometry increases. A recently published paper $^{40}$ also reported that the oxygen vacancies tend to cluster in the $<111>$ direction, and the positive effect of such clustering on the photovoltaic, photocatalytic and ferromagnetic properties was proposed. Besides the $<111>$ direction, the $<110>$ was suggested by Murgida et $al^{41}$ to be a possible direction for the oxygen vacancies to cluster, while another investigation exhibited that oxygen vacancies prefer to align along $<110>$ than $<111>$ directions. $^{42}$ Also, a substantial number of associated examinations have been done on $CeO_2(111)$ surface. The vacancy clustering has also been proposed in reduced $CeO_2(111)$ surfaces in theoretical explorations. $^{43-45}$ Esch et al used high-resolution scanning

tunneling microscopy (STM) to investigate the oxygen vacancies on the $CeO_2$(111) surface, and found that two or more vacancies tend to form linear clusters.⁴⁶ The similar observations on $CeO_2$(111) surfaces were also obtained using atom-resolved noncontact atomic force microscopy (AFM)⁴⁷ and the dynamic force microscopy (DFM).⁴⁸ However, in either undoped or surface structures of $CeO_2$, there is a notable lack of systematic studies on the formation and migration properties of clustered vacancies. Even though in $CeO_2$ doped with rare earth elements³⁶⁻³⁸ the existence of clustered vacancies was found to induce the ionic conductivity to lower, little was done to probe into the fundamental mechanism underlying the lowered ionic conductivity. Such studies are necessary since the oxygen vacancy distributions and transport properties directly control the functionality of $CeO_2$-based materials and devices in many applications for solving environmental and energy issues. Understanding the atomistic mechanism of oxygen vacancy clustering and how the distributions affect the properties is not only of fundamental interest, but also highly desirable for tailoring or optimizing the functionality of $CeO_2$ for a wide variety of applications.

In the present work, we use hybrid functional method to make detailed theoretical explorations of the formation and migration of clustered oxygen vacancies in bulk $CeO_2$, considering the more fundamental significance of undoped bulk $CeO_2$ compared to the doped and surface structures. To authors' best knowledge, this is the first attempt to theoretically elaborate the formation and migration of the clustered vacancies in $CeO_2$. Interestingly, systematic thermodynamic and kinetic investigations display the vacancy clustering in <111> direction, and the favorability of creating

this kind of vacancy cluster under the reducing condition as well. The presence of such oxygen vacancy clustering is proven to block the migration and transportation of oxygen vacancies, yielding a big challenge to achieve high ionic conductivity. The present work aims to provide a blueprint for enhancing the functionality of $CeO_2$-based materials or devices through unravelling the mechanism of vacancy cluster to negatively influence the ionic conduction.

## II. METHOD

All theoretical explorations of virgin and oxygen-deficient $CeO_2$ are performed using the Vienna Ab initio Simulation Package (VASP)$^{49,50}$ in terms of the projector augmented wave (PAW) method.$^{51,52}$ We employ the Heyd, Scuseria and Enrzerhof (HSE) hybrid method$^{53}$ to consider the nonlocal effect in the exchange-correlation (XC) functionals. With the HSE, the exchange potential is separated into a long-range and a short-range part, and a part of Hartree-Fock (HF) exchange is mixed with the Perdew-Burke-Ernzerhof (PBE) functional$^{54}$ only in the short-range part and the long-range part of the exchange potential is described by the PBE alone. The ($4f$, $5s$, $5p$, $5d$, $6s$) electrons of Ce atom and ($2s$, $2p$) electrons of O atom are treated as valence states with a plane-wave energy cutoff of 400 eV. The Brillouin zone is sampled using a 8×8×8 Monkhorst-Pack grid for the primitive cell of $CeO_2$, and a 2×2×2 grid for the 2×2×2 supercell of $CeO_2$ unit cell (which is used to construct the oxygen-deficient structures). A series of tests have been conducted to ensure convergence with respect to the number of k-points and energy cutoff. All structures are fully optimized first at the PBE level and further at the HSE level until the total force on each ion is less

### III. RESULTS AND DISCUSSIONS

Starting from the primitive cell of $CeO_2$, we use the different XC functionals, including the LDA+U, GGA(PBE)+U and HSE functionals, to consider the non-local effect. In the LDA+U and GGA+$U$ formalisms, the Coulomb repulsion $U$ and exchange interaction $J$ are treated by a single effective parameter $U_{\text{eff}} = U - J.^{69}$ Here, a wide range of $U_{\text{eff}}$ from 0 (LDA or GGA) to 10 eV are employed to make correction to the $4f$ electrons in Ce atoms. For the HSE, the proportion of 25% HF exchange is applied in the short-range mixing. Their calculated results for the lattice constant, band gaps (as shown in the following figures of band structure and densities of state, there exist two typical gaps in the band structure of pure $CeO_2$: O2p-Ce4f and O2p-Ce5d) and formation energy of $CeO_2$ are shown in Figure 1. In the LDA+U and GGA+$U$ cases, all calculated parameters linearly increase with $U_{\text{eff}}$, being consistent with the linear response of electronic and structural properties of correlated systems in the DFT functional with the correction of Hubbard $U.^{65}$ However, it is clear from Fig. 1 that, even though a certain $U_{\text{eff}}$ is used to successfully reproduce one of these parameters, the same $U_{\text{eff}}$ cannot yield others close to their experimental values. In contrast, the HSE-calculated values for lattice constant, band gaps and formation energy agree excellently with their corresponding experimental data, showing the effectiveness of the HSE in describing $CeO_2$.

Furthermore, we use the HSE to calculate the band structure and partial density of states (PDOS) for the primitive cell of $CeO_2$, as shown in Figure 2. One can see that both O2p-Ce4f and O2p-Ce5d band gaps are indirect, which is consistent with two recent theoretical explorations. $^{73,74}$ The

calculated valence band (VB) is mainly attributed to O 2p states and its width is about 4.1 eV, being in excellent agreement with the experimental value of 4.0 eV.⁷¹·⁷⁵ The VB is separated by a gap of 3.07 eV from the narrow unoccupied band predominantly composed of Ce 4f states and by a gap of 5.96 eV from the dispersive band with the most contributions from Ce 5d states. These are consistent with the experimental⁷¹ and theoretical⁷⁶ results.

Having confirmed that the utilization of HSE functional enables us to pursue the convincing investigations on CeO₂, let us examine 2×2×2 supercells with oxygen vacancy pair clusters over a short-range scale. Here the vacancy-vacancy separation is restricted to be no more than the lattice constant of a unit cell of CeO₂ (with the further increased vacancy-vacancy separation, the system is predicted to become more and more unstable, and the vacancies tend to be isolated not clustered). Figure 3 displays five configurations of distributing vacancy pairs in oxygen sub-lattice. We fully optimize all of them and find that the <111> cluster is the most energetically stable, indicating that this vacancy cluster is favorably formed compared to other configurations. This result is confirmed by two neutron diffraction studies on undoped CeO₂₋ₓ, where the vacancy pairs prefer to align in the <111> direction.³⁹·⁷⁷ Furthermore, we calculate the vacancy-vacancy interaction in the above five configurations using the equation in the literature⁷⁸ [ $E_{\text{int}} = E(\text{CeO}_2:2V_O) + E(\text{CeO}_2) - 2E(\text{CeO}_2:1V_O)$ , where $E(\text{CeO}_2:1V_O)$ and $E(\text{CeO}_2:2V_O)$ mean the total energies of the structures with one and two oxygen vacancies, and $E(\text{CeO}_2)$ represents that of perfect structure]. Results shows that the <111> vacancies are attractive to each other while there are repulsions in other clustered

vacancies. Evidently, such vacancy clustering is driven by the repulsion, which makes vacancies minimize their interaction by ordering the <111> direction.

Energetically, it is necessary to assess the likelihood of forming the <111> vacancy cluster considering the energetics of vacancy formation is of great interest. The formation energy of oxygen vacancies in $CeO_2$ can be expressed as$^{79}$

$$
\Delta E_{f}(\mathrm{n} V_{O}^{q})=E(\mathrm{CeO}_{2}: \mathrm{n} V_{O})-E(\mathrm{CeO}_{2})+n \mu_{O}+q(E_{F}+E_{\mathrm{VBM}}+\Delta E_{\mathrm{VBM}}), \tag{1}
$$

where $E(\mathrm{CeO}_{2}: \mathrm{n} V_{O})$ and $E(\mathrm{CeO}_{2})$ are the total energies of 2×2×2 supercells with and without $n V_O$ in the charge state $q$. $E_F$ is the Fermi level with respect to the VBM ($E_{\mathrm{VBM}}$), and $\Delta E_{\mathrm{VBM}}$ aligns the VBM in the supercells with and without $V_O$. The chemical potential $\mu_{O}=\mu_{O}^{\mathrm{elem}}+\Delta \mu_{O}$, where $\mu_{O}^{\mathrm{elem}}$ refers to the atomic total energy of O and the extraneous chemical potential $\Delta \mu_{O}$ is subject to the surrounding environment, i.e., O-poor and O-rich conditions. Here $\Delta \mu_{O}$ is limited by the constraints: $\Delta \mu_{O} \leq 0$ and $\Delta \mu_{\mathrm{Ce}}+2 \Delta \mu_{O}=E_{f}(\mathrm{CeO}_{2})$, where $E_{f}(\mathrm{CeO}_{2})$ refers to the formation energy of $CeO_2$ (its HSE-calculated $E_f$(CeO₂) is -11.32 eV per molecule unit, agreeing excellently with the experimental value of -11.29 eV$^{72}$). Under the O-rich condition, $\Delta \mu_{O}$ is 0 eV, and $\Delta \mu_{\mathrm{Ce}}=E_{f}(\mathrm{CeO}_{2})$. Under the O-poor condition (where $CeO_2$ is reduced into $Ce_2O_3$), $\Delta \mu_{O}$ and $\Delta \mu_{\mathrm{Ce}}$ are limited by the constraints: $\Delta \mu_{\mathrm{Ce}}+2 \Delta \mu_{O}=E_{f}(\mathrm{CeO}_{2})$ and $2 \Delta \mu_{\mathrm{Ce}}+3 \Delta \mu_{O}=E_{f}(\mathrm{Ce}_{2} O_{3})$. Here $E_f$(Ce₂O₃) is the formation energy of $Ce_2O_3$, which is calculated to be -18.54 eV per molecule unit, very close to the experimental value of -18.63 eV.$^{72}$ Figure 4a illustrates $\Delta \mu_{O}$ and $\Delta \mu_{Ce}$ between the O-rich limit ($\Delta \mu_{O}=0$ eV and $\Delta \mu_{Ce}=-11.32$ eV) and the O-poor limit ($\Delta \mu_{O}=-4.10$eV and $\Delta \mu_{Ce}=-3.12$ eV),

i.e., the thermodynamically allowed range of $CeO_2$. Based on the above formula and data, we calculate the formation energies of a single vacancy and the <111> vacancy cluster in different charge states, and the transition levels $E_F(q/q')$ between charge states $q$ and $q'$ [which can be derived from the equation $\Delta E_f(V_o^q) = \Delta E_f(V_o^{q'})$] as well.

Figure 4b shows the calculated formation energies of $V_O$ in different charge states (0, +1 and 2+). Clearly, the 1+ state is unstable for all values of $E_F$: when $E_F$ is less than 1.75 eV, the 2+ state is stable; beyond this value, the neutral state is stable. Namely, its transition level $E_F(2+/0)$ is at 1.75 eV, or 1.32 eV below the conduction band minimum (CBM, $E_{CBM}$). The formation energies of the <111> vacancy cluster in 0, +1, +2, +3 and +4 states are shown in Figure 4c. Here, the 1+, 2+ and 3+ states of the <111> vacancy cluster are unstable, and its transition level $E_F(4+/0)$ is at 1.81 eV. In order to simplify the presentation, only the stable states for a single vacancy ($1V_O$) and a <111> vacancy cluster ($2V_O$) under the O-poor and O-rich conditions are illustrated in Figure 4d. Apparently, the O-poor condition encourages the formation of oxygen vacancies while the O-rich chemical potential is energetically inferior due to the very high formation energy. Under the O-poor condition, the highest formation energy of a single vacancy is just a small positive value, suggesting that it would be readily surmountable. More interestingly, the formation energies of the vacancy cluster under the same condition are negative, demonstrating that it is highly favourable to form a <111> vacancy cluster. These results reveal that, if a single vacancy forms first, it can easily grow into vacancy cluster even without further requiring the external force.

Furthermore, we use the cNEB method to examine the migration of the <111> vacancy cluster along the <100>, <110> and <111> directions. Evidently, with respect to a single vacancy, the vacancy cluster has a greatly increased number of possible migration paths, which makes it much more complicated to investigate the migration of the vacancy cluster. In general, it is energetically much cheaper for a vacancy pair to migrate by successive jumps of individual vacancies than by the simultaneous diffusions of both vacancies, so we focus on the successive monovacancy diffusions in inspecting the migration of the <111> vacancy cluster. For the migration along the <100> directions, four typical migration paths (as illustrated in Figure 6) are examined, and their corresponding migration barriers are shown in Figure 7. Apparently, Path A is the most favourable among four paths investigated (it is worth stressing that there may be other diffusion paths which has the lower migration barriers than Path A. But this will not influence the subsequent conclusion that the vacancy cluster prefers to migrate along the <100> direction. As will be detailed below, the much higher migration barriers in <110> and <111> directions compared to the existent values in <100> direction reveal that it is very hard for the vacancy cluster to migrate along the <110> and <111> directions). In the same way, we investigate the migration of the vacancy cluster along the <110> and <111> directions, and their minimum-energy diffusion paths and corresponding migration barriers are shown in Figure 8, where the migration barriers in the <110> and <111> directions are found to be at least two times as high as that in <100> direction (Path A in Figure 7).

As a result, the vacancy cluster is predicted to predominantly migrate along the <100> direction.

However, the significantly enhanced migration barriers of the vacancy cluster (see Figures 5 and 7) indicate that the vacancy cluster has a lower mobility and higher kinetic stability with respect to a single vacancy, negatively influencing the ionic conduction in $\mathrm{CeO}_2$.

To further gain more insight into the microscopic nature of oxygen vacancy motion and better characterize the negative effect of vacancy cluster on ionic conductivity at an atomistic level, we run *ab initio* molecular dynamics (AIMD) simulations on bigger $3 \times 3 \times 3$ $\mathrm{CeO}_2$ supercells (containing 108 Ce cations and 216 O anions) with a single vacancy and a $<111>$ vacancy cluster. Considering the increasingly expensive computation for AIMD simulations, the PBE (not HSE) is chosen for the XC functional. In all simulations, we employ a NVT ensemble with a constant volume and temperature (1000 K), integrating the equations of motion at 1 fs time intervals and controlling temperature via the Nosè-Hoover thermostat. At each time-step, the total energy is evaluated to an accuracy of $10^{-4}$ eV/atom with a plane-wave energy cutoff of 400 eV, while sampling the $\Gamma$-point in the Brillouin zone. For both systems with a single vacancy and a $<111>$ vacancy cluster, a 2-ps simulation is first performed for equilibration, followed by the 4-ps simulations for statistical analysis. We have observed the frequent diffusions of the single vacancy. Most of these diffusions manifest themselves in the jumps of an oxygen anion into the vacancy site along the $<100>$ direction, which is consistent with the above calculated results of migration barriers. In contrast, the clustered vacancies are observed to mainly vibrate around their equilibrium positions, suggesting that vacancies are trapped and hard to diffuse. Occasionally, one vacancy of

the cluster is observed to jump, but often followed by a successive jump back to its original position, and seldom followed by the jump of the other. Understandably, it is the correlation between clustered vacancies that limits the mobility of vacancies, hindering ion conduction.

Another unneglectable factor influencing the ion conduction in the case of vacancy cluster is the existence of more $Ce^{3+}$ ions. It is generally accepted that creating an O vacancy by the removal of an O atom from $CeO_2$ causes two excess electrons to transfer to two $Ce^{4+}$ ions near the vacancy, reducing them into $Ce^{3+}$ ions. Though the distribution of these two $Ce^{3+}$ ions is still under intense debate (they were reported to prefer to be nearest neighbors to the vacancy by some studies$^{6,9,30,40,55-57,87-89}$ while others suggested the next nearest neighbors are energetically more favorable$^{41,58,60,90}$), the bigger-size $Ce^{3+}$ ions (compared to $Ce^{4+}$ ones) definitely influence the vacancy migration through appearing near the migration path. In order to elaborate this point, we have investigated the migration of a single vacancy with different distributions of oxygen vacancy and $Ce^{3+}$ ions. As shown in Figure 9A, two adjacent tetrahedra composed of $Ce^{4+}$ ions are used to define the path of oxygen vacancy migration along the <100> direction, with an oxygen vacancy being in one of two tetrahedra and an oxygen ion in the other. Here we use an approach by Zacherle et $al^{91}$ to control the positions of $Ce^{3+}$ ions, where an electron polaron is prepared to make the additional electron well localized on the chosen Ce ion. The configurations of oxygen vacancy relative to $Ce^{3+}$ ions are listed in Figure 9(B-H), displaying 7 possible models with 1 and 2 $Ce^{3+}$ ions near the migration path. Their migration barriers have been calculated and shown in Fig. 10 (for the sake of

comparison, the barrier for Model A is also listed together with those of Models B and C in Figure 10a). Apparently, the vacancy migration barrier has a strong dependence on the amount of $Ce^{3+}$ ion around the vacancy: the migration barrier remarkably increases with the amount of $Ce^{3+}$ ion (from 0 to 1 and 2), making the hopping probabilities of oxygen vacancy greatly reduced. In the case of a single vacancy, the amount of $Ce^{3+}$ is very limited, which makes $Ce^{3+}$ ions impossible of appearing near all lowest-energy migration paths. Comparatively, the clustered vacancies induce the increased occurrence of $Ce^{3+}$ even $Ce^{3+}$ pairs near the migration paths, significantly enhancing the difficulty of vacancy cluster in diffusing. Indeed, it should be fairly effective to hinder the migration of vacancy cluster as long as a single $Ce^{3+}$ ion or $Ce^{3+}$ pairs just appear near one vacancy of the cluster.

The negative effect that the vacancy clustering has on ionic conductivity accounts well for the presence of a maximum in the ionic conductivity of $CeO_{2-\delta}$ in theoretical$^{92}$ and experimental$^{85}$ literatures (where the ionic conductivity increases initially with the non-stoichiometry $\delta$, and reaches a maximum at a certain $\delta$ then falls): At low concentrations, oxygen vacancies are isolated or randomly distributed and the ionic conductivity increases with $\delta$; when $\delta$ is increased up to a critical value, the oxygen vacancies start to cluster, thus inducing the ionic conductivity to decrease. The similar phenomenon was reported in the systems of Y-doped $CeO_{2}$ ($Ce_{1-x}Y_{x}O_{2-x/2}$, x is the dopant concentration),$^{36}$ which is also closely related to the oxygen vacancy clustering in $CeO_{2}$ doped with high concentrations of Y, although other effects may also contribute to this, such as the

interaction between the dopant Y and oxygen vacancy. In another studies³⁷,³⁸ using electron energy loss spectroscopy and select area electron diffraction (SAED) on CeO₂ doped with rare-earth metals Y, Sm, Gd, Dy and Yb, an evident decrease in ionic conductivity was observed as the concentration of each dopant increased from 15 to 25 at%. Clearly, the common phenomenon for different dopants, i.e., the decrease in ionic conductivity, is regardless of dopants. What really takes effect is the higher degree of the clustering of the dense oxygen vacancies originating from the higher concentration of dopants (although the different dopants have different effect on the clustering degree of vacancies). Therefore, the consideration for improving ionic conductivity of CeO₂-based materials should be taken at the range of lower vacancy concentrations.

Overall, the vacancy cluster has become the challenge for achieving a high ionic conductivity in CeO₂, leading to the degradation in the related performances. Once the vacancy cluster forms, higher additional energies are required for overcoming its negative influence on diffusion. It is therefore for one to try to avoid or eliminate the clustering of oxygen vacancies. First, a strongly reducing condition like high-temperature atmosphere ought not to be used when preparing or processing CeO₂. A short-range ordering of the anion vacancies has been reported in theoretical³⁹ and experimental⁹³ investigations on CeO₂ under the condition of the high temperature (1273K). Another experimental and molecular-dynamic studies of Y-doped CeO₂ also showed that at 1073K the vacancies would rather cluster along the <111> direction than distribute randomly while the vacancy clustering becomes less pronounced at 873K.³⁶ On the other hand, strict control should be

made on the concentration of dopants which are used to promote the ion conduction. Although many transition metals or rare-earth metals can be used to dope $CeO_2$ for enhancing ionic conductivity, it is only effective when the vacancies are isolated or randomly distributed at low dopant concentrations. Higher dopant concentrations induce the dense vacancies to cluster, $^{36-38}$ which in turn hinders the ion conduction. In addition, some external processing treatments have been found to notably influence oxygen vacancy clustering in real applications. For instance, photoexcitation can effectively induce the dissociation of clustered vacancies at the $LaAlO_3/SrTiO_3$ interface $^{94}$ while the tensile strain imposed on $CaMnO_3$ is beneficial for oxygen vacancy clustering. $^{95}$ Undoubtedly, these are useful for weakening or adjusting the clustering of oxygen vacancies.

Actually, apart from $CeO_2$, the strong ordering of oxygen vacancies along the <111> direction has been found in other fluorite oxides. Two experimental literatures reported that the vacancy pairs cluster in the <111> direction of $PrO_2^{96}$ and $TbO_2.^{97}$ The same clustering of anion vacancies in $ZrO_2$ compounds was also confirmed using the neutron diffraction, Monte Carlo and impedance spectroscopy measurements. $^{98-101}$ Taking these into account, it appears that the presence of the <111> vacancy pair is a common feature of oxygen-deficient fluorite oxides. Accordingly, the outcome of this work is expected to be generalized to fluorite oxides.

## IV. CONCLUSIONS

In summary, we have investigated the formation and migration of oxygen vacancy cluster in bulk
CeO₂ using the HSE hybrid functional method, and found that oxygen vacancies energetically
cluster in the <111> direction. The detailed analyses of formation energy show that it is rather easy
to form such vacancy cluster under the O-poor condition. The explorations using the cNEB and
MD simulation demonstrate that the vacancy cluster is kinetically stable and hard to diffuse,
indicative of a low ionic conductivity. Efforts have been done to fundamentally unravel the
negative effect of vacancy clustering on the ionic conduction in CeO₂. Appropriate means should
be taken to eliminate or weaken oxygen vacancy clustering, so that the functionality of CeO₂-based
materials for solving the environmental and energy issues can be maximized. The outcome of this
work is expected to be generalized to other fluorite oxides.

## ACKNOWLEDGEMENT
This work was supported by United Arab Emirates University through the University Program for
Advanced Research (No. 31S109-UPAR and 31R109-Research Center-ECEER-9-2016). Part of
computing time was provided by North University of China.

Temperature Solid Oxide Fuel Cell in Hydrocarbon-Air Mixtures. *Science* **2000**, 288, 2031-2033.

(20) Gupta, A.; Waghmare, U. V.; Hegde, M. S. Correlation of Oxygen Storage Capacity and Structural Distortion in Transition-Metal-, Noble-Metal-, and Rare-Earth-Ion-Substituted CeO₂ from First Principles Calculation. *Chem. Mater.* **2010**, 22, 5184-5198.

(21) Tang, Y. H.; Zhang, H.; Cui, L. X.; Ouyang, C. Y.; Shi, S. Q.; Tang, W. H.; Li, H.; Lee, J. S.; Chen, L. Q. First-Principles Investigation on Redox Properties of M-Doped CeO₂ (M = Mn, Pr, Sn, Zr). *Phys. Rev. B* **2010**, 82, 125104.

(22) Cen, W. L.; Liu, Y.; Wen, Z. B.; Wang, H. Q.; Weng, X. L. A Theoretic Insight into the Catalytic Activity Promotion of CeO₂ Surfaces by Mn Doping. *Phys. Chem. Chem. Phys.* **2012**, 14, 5769-5777.

(23) Li, H. F.; Lu, G. Z.; Dai, Q. G.; Wang, Y. Q.; Guo, Y.; Guo, Y. L. Efficient Low-Temperature Catalytic Combustion of Trichloroethylene over Flower-Like Mesoporous Mn-Doped CeO₂ Microspheres. *Appl. Catal. B: Environ.* **2011**, 102, 475-483.

(24) Hsu, L. C.; Tsai, M. K.; Lu, Y. H.; Chen, H. T. Computational Investigation of CO Adsorption and Oxidation on Mn/CeO₂(111) Surface. *J. Phys. Chem. C* **2013**, 117, 433-441.

(25) Krcha, M. D.; Janik, M. J. Examination of Oxygen Vacancy Formation in Mn-Doped CeO₂(111) Using DFT+U and the Hybrid Functional HSE06. *Langmuir* **2013**, 29, 10120-10131.

(26) Chen, H. T.; Chang, J. G. Oxygen Vacancy Formation and Migration in Ce₁₋ₓZrₓO₂ Catalyst: a DFT+U Calculation. *J. Chem. Phys.* **2010**, 132, 214702.

(27) Wang, H. F.; Gong, X. Q.; Guo, Y. L.; Guo, Y.; Lu, G. Z.; Hu, P. A Model to Understand the

(35) Vanpoucke, D. E. P; Bultinck, P.; Cottenier, S.; Speybroeck, V. V.; Driesschea I. V. Aliovalent Doping of $CeO_2$: DFT Study of Oxidation State and Vacancy Effects. *J. Mater. Chem. A* **2014**, 2, 13723-13737.

(36) Burbano, M.; Norberg, S. T.; Hull, S.; Eriksson, S. G.; Marrocchelli, D.; Madden, P. A.; Watson, G. W. Oxygen Vacancy Ordering and the Conductivity Maximum in $Y_2O_3$-Doped $CeO_2$. *Chem. Mater.* **2012**, 24, 222-229.

(37) Ou, D. R.; Mori, T.; Ye, F.; Zou, J.; Auchterlonie, G.; Drennan, J. Oxygen-vacancy Ordering in Lanthanide-doped Ceria: Dopant-type Dependence and Structure Model. *Phys. Rev. B* **2008**, 77, 024108.

(38) Ou, D. R.; Mori, T.; Ye, F.; Kobayashi, T. Oxygen Vacancy Ordering in Heavily Rare-earth-doped Ceria. *Appl. Phys. Lett.* **2006**, 89, 171911.

(39) Hull, S.; Norberg, S. T.; Ahmed, I.; Eriksson, S. G.; Marrocchelli, D.; Madden, P. A. Oxygen Vacancy Ordering within Anion-Deficient Ceria. *J. Solid State Chem.* **2009**, 182, 2815-2821.

(40) Han, X.; Amrane, N.; Zhang, Z.; Benbraouda, M. Oxygen Vacancy Ordering and Electron Localization in $CeO_2$: Hybrid Functional Study. *J. Phys. Chem. C* **2016**, 120, 13325-13331.

(41) Murgida, G. E.; Ferrari, V.; Ganduglia-Pirovano, M. V.; Llois, A. M. Ordering of Oxygen Vacancies and Excess Charge Localization in Bulk Ceria: A DFT+U Study. *Phys. Rev. B* **2014**, 90, 115120.

(42) Gopal, C. B.; van de Walle, A. Ab Initio Thermodynamics of Intrinsic Oxygen Vacancies in

Ceria. *Phys. Rev. B* **2012**, 86, 134117.

(43) Murgida, G. E.; Ganduglia-Pirovano, M. V. Evidence for Subsurface Ordering of Oxygen Vacancies on the Reduced $CeO_2$(111) Surface Using Density-Functional and Statistical Calculations. *Phys. Rev. Lett.* **2013**, 110, 246101.

(44) Sutton, J. E.; Beste, A.; Overbury, S. H. Origins and Implications of the Ordering of Oxygen Vacancies and Localized Electrons on Partially Reduced $CeO_2$(111). *Phys. Rev. B* **2015**, 92, 144105.

(45) Zhang, C.; Michaelides, A.; King, D. A.; Jenkins, S. J. Anchoring Sites for Initial Au Nucleation on $CeO_2${111}: O Vacancy versus Ce Vacancy. *J. Phys. Chem. C* **2009**, 113, 6411-6417.

(46) Esch, F.; Fabris, S.; Zhou, L.; Montini, T.; Africh, C.; Fornasiero, P.; Comelli, G.; Rosei, R. Electron Localization Determines Defect Formation on Ceria Substrates. *Science* **2005**, 309, 752-755.

(47) Namai, Y.; Fukui, K. I.; Iwasawa, Y. Atom-Resolved Noncontact Atomic Force Microscopic Observations of $CeO_2$(111) Surfaces with Different Oxidation States: Surface Structure and Behavior of Surface Oxygen Atoms. *J. Phys. Chem. B* **2003**, 107, 11666-11673.

(48) Torbrugge, S.; Reichling, M.; Ishiyama, A.; Morita, S.; Custance, O. Evidence of Subsurface Oxygen Vacancy Ordering on Reduced $CeO_2$(111). *Phys. Rev. Lett.* **2007**, 99, 056101.

(49) Kresse G.; Hafner, J. Ab Initio Molecular Dynamics for Liquid Metals. *Phys. Rev. B* **1993**, 47, 558.

(50) Kresse G.; Hafner, J. Ab Initio Molecular-dynamics Simulation of the Liquid-Metal-Amorphous-Semiconductor Transition in Germanium. *Phys. Rev. B* **1994**, 49, 14251.

(51) Blochl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* **1994**, *50*, 17593.

(52) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Phys. Rev. B* **1999**, *59*, 1758.

(53) Heyd, S.; Scuseria, G. E.; Ernzerhof, M. Hybrid Functionals Based on a Screened Coulomb Potential. *J. Chem. Phys.* **2003**, *118*, 8207.

(54) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865.

(55) Plata, J. J.; Marquez, A. M.; Sabz, J. F. Improving the Density Functional Theory+U Description of $CeO_2$ by Including the Contribution of the O 2p Electrons. *J. Chem. Phys.* **2012**, *136*, 041101.

(56) Hellman, O.; Skorodumova, N. V.; Simak, S. I. Charge Redistribution Mechanisms of Ceria Reduction. *Phys. Rev. Lett.* **2012**, *108*, 135504.

(57) Molinari, M.; Parker, S. C.; Sayle, D. C.; Islam, M. S. Water Adsorption and Its Effect on the Stability of Low Index Stoichiometric and Reduced Surfaces of Ceria. *J. Phys. Chem. C* **2012**, *116*, 7073-7082.

(58) Allen, J. P.; Watson, G. W. Occupation Matrix Control of d- and f-Electron Localisations Using DFT + U. *Phys. Chem. Chem. Phys.* **2014**, *16*, 21016-21031.

(59) Plata, J. J.; Marquez, A. M.; Sabz, J. F. Transport Properties in the $CeO_{2-x}$(111) Surface: From Charge Distribution to Ion-Electron Collaborative Migration. *J. Phys. Chem. C* **2013**, *117*, 25497-25503.

(60) Kullgren, J.; Hermansson, K.; Castleton, C. Many Competing Ceria (110) Oxygen Vacancy Structures: From Small to Large Supercells. *J. Chem. Phys.* **2012**, *137*, 044705.

(61) Fabris, S.; Vicario, G.; Balducci, G.; de Gironcoli, S.; Baroni, S. Electronic and Atomistic Structures of Clean and Reduced Ceria Surfaces. *J. Phys. Chem. B* **2005**, *109*, 22860-22867.

(62) Yang, Z.; Woo, T. K.; Hermansson, K. Effects of Zr Doping on Stoichiometric and Reduced Ceria: A First-Principles Study. *J. Chem. Phys.* **2006**, *124*, 224704.

(63) Mayernick, A. D.; Janik, M. J. Methane Activation and Oxygen Vacancy Formation over CeO₂ and Zr, Pd Substituted CeO₂ Surfaces. *J. Phys. Chem. C* **2008**, *112*, 14955-14964.

(64) Keating, P. R. L.; Scanlon, D. O.; Watson, G. W. Intrinsic Ferromagnetism in CeO₂: Dispelling the Myth of Vacancy Site Localization Mediated Superexchange. *J. Phys.: Condens. Matter* **2009**, *21*, 405502.

(65) Cococcioni, M.; de Gironcoli, S. Linear Response Approach to the Calculation of the Effective Interaction Parameters in the LDA+U Method. *Phys. Rev. B* **2005**, *71*, 035105.

(66) Guss, P.; Foster, M. E.; Wong, B. M.; Doty, F. P.; Shah, K.; Squillante, M. R.; Shirwadkar, U.; Hawrami, R.; Tower, J.; Yuan, D. Results for Aliovalent Doping of CeBr₃ with Ca²⁺. *J. Appl. Phys.* **2014**, *115*, 034908.

(67) Hedin, L. New Method for Calculating the One-Particle Green's Function with Application to the Electron-Gas Problem. *Phys. Rev.* **1965**, *139*, A796.

(68) Hybertsen, M. S.; Louie, S. G. Electron Correlation in Semiconductors and Insulators: Band Gaps and Quasiparticle Energies. *Phys. Rev. B* **1986**, *34*, 5390.

(69) Dudarev, S. L.; Botton, G. A.; Savrasov, S. Y.; Humphreys, C. J.; Sutton, A. P. Electron-Energy-Loss Spectra and the Structural Stability of Nickel Oxide: An LSDA+U Study. *Phys. Rev. B* **1998**, *57*, 1505.

(70) Gschneider, K. A.; Eyring, L. *Handbook on the Physics and Chemistry of Rare Earths*; North-Holland, Amsterdam, 1979.

(71) Wuilloud, E.; Delley, B.; Schneider, W. D.; Baer, Y. Spectroscopic Evidence for Localized and Extended $f$-Symmetry States in CeO₂. *Phys. Rev. Lett.* **1984**, *53*, 202.

(72) Lide, D. R. *CRC Handbook of Chemistry and Physics*; CRC Press: London, U.K., 1999.

(73) Sun, L.; Huang, X.; Wang, L.; Janotti, A. Disentangling the Role of Small Polarons and Oxygen Vacancies in CeO₂. *Phys. Rev. B* **2017**, *95*, 245101.

(74) Gillen, R.; Clark, S. J.; Robertson, J. Nature of the Electronic Band Gap in Lanthanide Oxides. *Phys. Rev. B* **2013**, *87*, 125116.

(75) Marabelli, F.; Wachter, P. Covalent Insulator CeO₂: Optical Reflectivity Measurements. *Phys. Rev. B* **1987**, *36*, 1238.

(76) Koelling, D. D.; Boring, A. M.; Wood, J. H. The Electronic Structure of CeO₂ and PrO₂. *Solid State Commun.* **1983**, *47*, 227-232.

(77) Buban, J. P.; Iddir, H.; Ogut, S. Structural and Electronic Properties of Oxygen Vacancies in Cubic and Antiferrodistortive Phases of $SrTiO_3$. *Phys. Rev. B* **2004**, *69*, 180102.

(78) Kummerle, E. A.; Heger, G. The Structures of C-$Ce_2O_{3+\delta}$, $Ce_7O_{12}$, and $Ce_{11}O_{20}$. *J. Solid State Chem.* **1999**, *147*, 485-500.

(79) Van de Walle, C. G.; Neugebauer, J. First-principles Calculations for Defects and Impurities: Applications to III-nitrides. *J. Appl. Phys.* **2004**, *95*, 3851-3879.

(80) Henkelman, G.; Jonsson, H. A Climbing Image Nudged Elastic Band Method for Finding Saddle Points and Minimum Energy Paths. *J. Chem. Phys.* **2000**, *113*, 9901.

(81) Henkelman, G.; Jonsson, H. Improved Tangent Estimate in the Nudged Elastic Band Method for Finding Minimum Energy Paths and Saddle Points. *J. Chem. Phys.* **2000**, *113*, 9978.

(82) Gotte, A.; Spangberg, D.; Hermansson, K.; Baudin, M. Molecular Dynamics Study of Oxygen Self-Diffusion in Reduced $CeO_2$. *Solid State Ionics* **2007**, *178*, 1421-1427.

(83) Nilsson, J. O.; Vekilova, O. Y.; Hellman, O.; Klarbring, J.; Simak, S. I.; Skorodumova, N. V. Ionic Conductivity in Gd-Doped $CeO_2$: Ab Initio Color-Diffusion Nonequilibrium Molecular Dynamics Study. *Phys. Rev. B* **2016**, *93*, 024102.

(84) Yashima, M.; Kobayashi, S.; Yasui, T. Positional Disorder and Diffusion Path of Oxide Ions in the Yttria-Doped Ceria $Ce_{0.93}Y_{0.07}O_{1.96}$. *Faraday Discuss.* **2007**, *134*, 369-376.

(85) Tuller, H. L.; Nowick, A. S. Small Polaron Electron Transport in Reduced $CeO_2$ Single Crystals. *J. Phys. Chem. Solids* **1977**, *38*, 859-867.

(86) Mills, G.; Jonnson, H.; Schenter, G. K. Reversible Work Transition State Theory: Application to Dissociative Adsorption of Hydrogen. *Surf. Sci.* **1995**, *324*, 305-337.

(87) Keating, P. R. L.; Scanlon, D. O.; Morgan, B. J.; Galea, N. M.; Watson, G. W. Analysis of Intrinsic Defects in CeO₂ Using a Koopmans-Like GGA+U Approach. *J. Phys. Chem. C* **2012**, *116*, 2443-2452.

(88) Shi, L.; Vathonne, E.; Oison, V.; Freyss, M.; Hayn, R. First-principles DFT+U Investigation of Charged States of Defects and Fission Gas Atoms in CeO₂. *Phys. Rev. B* **2016**, *94*, 115132.

(89) Han, X.; Amrane, N.; Zhang, Z.; Benkraouda, M. Reply to “Comment on ‘Oxygen Vacancy Ordering and Electron Localization in CeO₂: Hybrid Functional Study’”. *J. Phys. Chem. C* **2017**, *121*, 21084-21086.

(90) Wang, B.; Xi, X.; Cormack, A. N. Chemical Strain and Point Defect Configurations in Reduced Ceria. *Chem. Mater.* **2014**, *26*, 3687-3692.

(91) Zacherle, T.; Schriever, A.; De Souza, R. A.; Martin, M. Ab Initio Analysis of the Defect Structure of Ceria. *Phys. Rev. B* **2013**, *87*, 134104.

(92) Cui, Z.; Sun, Y.; Qu, J. Molecular Dynamics Simulation of Reduced CeO₂. *Solid State Ionics* **2012**, *226*, 24-29.

(93) Wang, S.; Katsukib, M.; Hashimotoa, T.; Dokiyab, M. Expansion Behavior of Ce_(1-y)GdyO_(2·0-0.5y-δ) under Various Oxygen Partial Pressures Evaluated by HTXRD. *J. Electrochem. Soc.* **2003**, *150*, A952-A958.

(94) Lei, Y.; Li, Y.; Chen, Y. Z.; Xie, Y. W.; Chen, Y. S.; Wang, S. H.; Wang, J.; Shen, B. G.; Pryds, N.; Hwang, H. Y., et al. Visible-Light-Enhanced Gating Effect at the LaAlO₃/SrTiO₃ Interface. *Nature Comm.* **2014**, 5, 5554.

(95) Aschauer, U.; Pfenninger, R.; Selbach, S. M.; Grand, T.; Spaldin, N. A. Strain-Controlled Oxygen Vacancy Formation and Ordering in CaMnO₃. *Phys. Rev. B* **2013**, 88, 054111.

(96) Schweda, E.; Bevan, D. J. M.; Eyring, L. On the PrₙO₂ₙ₋₂ Series of Oxides and the Structure of Pr₂₄O₄₄: An Investigation by High-resolution Electron Microscopy. *J. Solid State Chem.* **1991**, 90, 109-125.

(97) Baenziger, N. C.; Eick, H. A.; Schuldt, H. S.; Eyring, L. Terbium Oxides. III. X-Ray Diffraction Studies of Several Stable Phases. *J. Am. Chem. Soc.* **1961**, 83, 2219-2223.

(98) Norberg, S. T.; Hull, S.; Ahmed, I.; Eriksson, S. G.; Marrocchelli, D.; Madden, P. A.; Li, P.; Irvine, J. T. S. Structural Disorder in Doped Zirconias, Part I: The Zr₀.₈Sc₀.₂₋ₓYₓO₁.₉ (0.0 ≤ x ≤ 0.2) System. *Chem. Mater.* **2011**, 23, 1356-1364.

(99) Marrocchelli, D.; Madden, P. A.; Norberg, S. T.; Hull, S. Structural Disorder in Doped Zirconias, Part II: Vacancy Ordering Effects and the Conductivity Maximum. *Chem. Mater.* **2011**, 23, 1365-1373.

(100) Norberg, S. T.; Ahmed, I.; Hull, S.; Marrocchelli, D.; Madden, P. A. Local Structure and Ionic Conductivity in the Zr₂Y₂O₇-Y₃NbO₇ system. *J. Phys.: Condens. Matter* **2009**, 21, 215401.

(101) Marrocchelli, D.; Madden, P. A.; Norberg, S. T.; Hull, S. Cation Composition Effects on Oxide Conductivity in the Zr₂Y₂O₇–Y₃NbO₇ system. *J. Phys.: Condens. Matter* **2009**, 21, 405403.

![](./images/813057127940620288_1.jpg)

Figure 1. Effect of $U_{\text{eff}}$ on the lattice constant $a$ (a), O2$p$-Ce4$f$ band gap (b), O2$p$-Ce5$d$ band gap (c) and formation energy (d) of CeO$_2$. The Hubbard correction is applied to the $4f$ electrons. The dot lines represent the corresponding experimental values (the experimental lattice constant of 5.41 Å is from Ref. 70, the experimental O2$p$-Ce4$f$ band gap of 3.0 eV and O2$p$-Ce5$d$ band gap of 6.0 eV are from Ref. 71, and the experimental formation energy of -11.29 eV is from Ref. 72). For the sake of comparison, the corresponding HSE values are marked using red squares.

![](./images/813057127940620288_2.jpg)

Figure 2. Calculated band structure (a) and partial density of states (b) for the primitive cell of CeO₂ using the HSE formalism. The dot-dashed lines at energy zero represent the Fermi level.

![](./images/813057127940620288_3.jpg)

Figure 3. Schematic configurations of short-range vacancy pairs in $CeO_2$, where the vacancy-vacancy separation is set to be no more than the lattice constant of a unit cell of $CeO_2$. Each dashed cube corresponds to a unit cell of $CeO_2$ and each solid cube represents an O sublattice. Here only the oxygen vacancies are marked with red cubes. The <100>, <110> and <111> structures represent the vacancy pairs within the unit cell of $CeO_2$ along <100>, <110> and <111> directions, while the $<100>_e$ and $<111>_e$ ones represent the vacancy pairs along the <100> and <111> directions extending out of the unit cell, respectively. For the $<100>_e$, the vacancy-vacancy separation equal to the unit-cell lattice constant. The $<111>_e$ structure, in spite of having the same vacancy-vacancy separation to the above <111> structure, includes a face-centered Ce atom halfway between.

![](./images/813057127940620288_4.jpg)

Figure 5. Migration barriers of a single oxygen vacancy. On the left, four paths for the migration of a single oxygen vacancy in the directions of $<100>$, $<110>$ and $<111>$ are illustrated. Here only the O sublattice is shown. The O vacancy and O atoms are represented by a red cube and a yellow sphere, respectively. Note Paths 3 and 4 show two different diffusion paths in the $<111>$ direction, distinguished by whether or not the path contains a Ce atom (represented by a blue sphere).

![](./images/813057127940620288_5.jpg)

Figure 6. Schematic for four typical paths (Paths A-D) for the migration of the <111> vacancy cluster along the <100> direction, including their corresponding initial, intermediate and final configurations (Configurations 1-4). Here only the O sublattices along the migration direction are shown. The O vacancy, O atom and Ce atom are represented by a red cube, yellow and blue spheres, respectively.

![](./images/813057127940620288_6.jpg)

Figure 7. The migration barriers of the <111> vacancy cluster along the paths described in Fig. 6.

![](./images/813057127940620288_7.jpg)

Figure 8. The migration barriers of the <111> vacancy cluster along <110> (a) and <111> (b) directions, with the corresponding minimum-energy paths listed along the horizontal axis. The O vacancy, O atom and Ce atom are represented by a red cube, yellow and blue spheres, respectively.

![](./images/813057127940620288_8.jpg)

Figure 9. Possible migration models of a single vacancy in the cases of 0 (A), 1 (B,C) and 2 (D-H)
$Ce^{3+}$ ions. The O vacancy is marked with a red cube, and $O^{2-}$, $Ce^{4+}$ and $Ce^{3+}$ ions are represented
by red, yellow and purple spheres, respectively.

![](./images/813057127940620288_9.jpg)

Figure 10. (a-b) The migration barriers of a single vacancy in the models shown in Figure 9.

TOC Graphic

![](./images/813057127940620288_10.jpg)