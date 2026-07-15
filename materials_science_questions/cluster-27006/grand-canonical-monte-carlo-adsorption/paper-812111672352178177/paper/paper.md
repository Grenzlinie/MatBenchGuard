# Molecular Simulation Study of Adsorption and Diffusion on Silicalite for a Benzene/CO₂ Mixture

Xiaopeng Yue and Xiaoning Yang*

Key Laboratory of Material-Orientated Chemical Engineering of Jiangsu Province, College of Chemistry and Chemical Engineering, Nanjing University of Technology, Nanjing 210009, P. R. China

Received October 22, 2005. In Final Form: January 11, 2006

The adsorption and diffusion of a binary mixture of supercritical CO₂ and benzene on silicalite (MFI-type) have been studied through the grand canonical Monte Carlo and molecular dynamics (MD) simulations. The adsorption behavior of pure CO₂ on silicalite was discussed in detail from the adsorption isotherms, adsorption sites, interaction energies, and isosteric heats of adsorption. For the mixture, the influences of temperature, pressure and composition on the adsorption isotherms have been examined. The adsorption site behavior of the mixture has been analyzed, and benzene molecules get adsorbed preferentially in the more spacious channel intersection positions. These simulation results suggest that SC−CO₂ fluid can be used as an efficient desorbent of larger aromatics in the zeolite material.
The diffusion characteristic for the benzene/CO₂ mixture was studied on the basis of MD simulation. It was found that the large coadsorbed benzene molecule has a pronounced effect on the CO₂ diffusion in the mixture, while the mobility of benzene molecules is very small due to geometrical restrictions.

## 1. Introduction

Supercritical carbon dioxide (SC-CO₂), as an environmentally benign solvent with favorable fluid properties, is receiving much attention and application in various processes, including separation,¹,² catalytic reaction,³,⁴ polymer preparation,⁵ surface cleaning and dryness,⁶,⁷ biological and pharmaceutical fields,⁸ and so forth. Especially, SC−CO₂ is a superior solvent in adsorption separation, such as the regeneration of adsorbents and the separation of isomers, which are very difficult to separate through conventional methods. For example, Iwai et al.² studied the adsorption separation of 2,6- and 2,7-dimethylnaphthalene using SC-CO₂ as the solvent and NaY zeolite as the adsorbent. They found that an efficient separation of the isomers could be achieved with proper adsorbents and operating conditions. Additionally, in the regeneration of adsorbents, the SC-CO₂ can efficiently desorb compounds from porous solid adsorbents.⁹

To develop and design these separation processes, it is very crucial to understand the mechanisms and properties for adsorption and diffusion between supercritical fluid mixtures and solid media. Although limited experimental data for solute adsorption from SC-CO₂ onto solid media are available,¹⁰⁻¹² they are still very scarce because the experimental measurement of adsorption is relatively complicated and time-consuming. It is highly desirable to provide a reasonable theoretical prediction and description for the complex adsorption equilibrium and dynamics diffusion of supercritical fluid mixtures in porous solid media. Several phenomenological models have been developed¹³,¹⁴ to correlate the solute adsorption from the near-critical CO₂ fluid. However, these models always need experimental data to obtain the fitting model parameters, and they are not able to provide any molecular-level microscopic information on the adsorption mechanism.

Recently, there has been rapid development in the application of molecular simulations for the theoretical study of adsorption. Molecular simulation is an attractive approach for predicting adsorption isotherms, adsorption heat, adsorption site location, and microporous diffusion; it gives insight into the adsorption and transport mechanisms of confined molecules. At the same time, molecular simulation can offer a foundation of theory development. There is an enormous amount of literature on the molecular simulation study of adsorption in porous zeolite solids, as reviewed recently by Fuchs and Cheetham.¹⁵ Nitta and Shigeta¹⁶ studied the adsorption characteristics of benzene on activated carbon from dense CO₂ fluid by using a simple Lennard-Jones model.

This paper presents a molecular simulation study for the adsorption and diffusion of a binary mixture containing SC-CO₂ and benzene on silicalite (MFI-type). For comparison, the adsorption behavior of pure SC-CO₂ has also been investigated because of an important competitive adsorption effect from the carrier fluid. MFI-type zeolite is made up of a set of straight channels $(5.4 \times 5.6$ Å) run in the $y$-direction, zigzag channels $(5.1 \times 5.4$ Å) run in the $x$-direction, and the intersection of channels that have an $\sim 8.7$ Å diameter, as measured by X-ray diffraction (XRD).¹⁷ It has found wide application in processes¹⁸⁻²² such as adsorption, separation, dewaxing, ion exchange, catalysis,

* To whom correspondence should be addressed. E-mail: Yangxia@njut.edu.cn.
(1) Tan, C. S.; Tsay, J. L. Ind. Eng. Chem. Res. 1990, 29 (3), 502−504.
(2) Iwai, Y.; Higuchi, M.; Nishioka, H.; Takahashi, Y.; Arai Y. Ind. Eng. Chem. Res. 2003, 42, 5261−5267.
(3) Glaser, R.; Weitkamp, J. Ind. Eng. Chem. Res. 2003, 42, 6294−6302.
(4) Olsen, M. H. N.; Salomao, G. C.; Drago, V.; Fernandes, C.; Horn Jr, A.; Cardozo Filho, L.; Antunes, O. A. C. J. Supercrit. Fluids. 2005, 34, 119−124.
(5) Li, D.; Liu, Z. M.; Song, L. P.; Yang, G. Y.; Jiang, T. Polymer 2002, 43 (19), 5363−5367.
(6) Marsal, A.; Celma, P. J.; Cot, J.; Cequier, M. J. Supercrit. Fluids 2000, 16, 217−223.
(7) Iwai, Y.; Amiya, M.; Murozono, T.; Arai Y. Ind. Eng. Chem. Res. 1998, 37, 2893−2896.
(8) Mesiano, A. J.; Beckman, E. J.; Russell, A. J. Chem. Rev. 1999, 99, 623−633.
(9) Reverchon, E.; Guerra, G.; Venditto, V. J. Appl. Polym. Sci. 1999, 74, 2077−2082.
(10) Kikic, I.; Alessi, P.; Cortesi, A.; Macnaughton, S. J.; Foster, N. R.; Spicka, B. Fluid Phase Equilib. 1995, 117, 304.
(11) Ryu, Y. K.; Kim, K. L.; Lee, C. H. Ind. Eng. Chem. Res. 2000, 39 (7), 2510−2518.
(12) Harikrishnan, R.; Srinivasan, M. P. Ching, C. B. AIChE J. 1998, 44 (12), 2620−2627.
(13) Yang, X. N. J. Colloid Interface Sci. 2004, 273, 362−368.
(14) Jha, S. K.; Madras, G. J. Supercrit. Fluids 2004, 32, 161−166.
(15) Fuchs, A. H.; Cheetham, A. K. J. Phys. Chem. B 2001, 105 (31), 7375−7383.
(16) Nitta, T.; Shigeta, T. Fluid Phase Equilib. 1998, 144, 245−256.
(17) Olson, D. H.; Kokotailo, G. T.; Lawton, S. L. J. Phys. Chem. 1981, 85 (15), 2238−2243.

10.1021/la052843f CCC: $33.50 © 2006 American Chemical Society
Published on Web 02/28/2006

and so forth. Many aromatic organic molecules, such as benzene and xylene, are comparable in size to the channels in the MFI zeolite; therefore, the adsorption of these molecules on MFI zeolite becomes very unique. Extensive experimental work $^{23-33}$ has been carried out to study the fundamental properties of aromatic sorbate in the ZSM-5 zeolite (MFI-type) and silicalite (MFI-type and pure silica) family. Meanwhile, molecular simulation studies of adsorption and diffusion for aromatic compounds on MFI zeolite have also been conducted. Gupta et al. $^{34}$ studied the adsorption of benzene on silicalite. A molecular simulation study for the adsorption of a liquid mixture of aromatics in silicalite was preformed. $^{35,36}$ Additionally, Song et al. $^{29,37}$ studied the adsorption and diffusion properties of pure benzene in silicalite by experiment and simulation.

In this work, grand canonical ensemble Monte Carlo (GCMC) simulation was employed to determine the adsorption isotherms of pure SC-CO₂ and the binary mixture of benzene and carbon dioxide on silicalite in different temperatures, pressures, and compositions. Molecular dynamics (MD) simulations were also performed to study the diffusion properties of the mixture on silicalite. The system was chosen because, if SC-CO₂ serves as a carrier solvent, the desorbent can be avoided, and the separation cost should obviously be reduced. This study will assist in understanding the adsorption mechanism and in developing the process of supercritical fluid adsorption. At present, relatively fewer molecular simulation studies were reported on the adsorption of supercritical fluid mixtures in zeolite adsorbents. The remainder of this paper is organized as follows: In the following sections, details of the model and simulation methodology will be given, followed by the simulation results and discussions, which include the GCMC and MD results, and a brief summary of our research as well as concluding remarks.

## 2. Model Representation and Methods
Model Representation. Silicalite (MFI-type) is known to have three different crystalline forms, $^{17,25,38}$ MONO $(P2_{1}/n)$, ORTHO (Pnma), and PARA $(P2_{1}2_{1}2_{1})$. The transition between these structural forms may be induced by the presence of a large adsorbate and its adsorbed amounts. It is usually accepted that the reasonable structure of silicalite is the ORTHO form for CO₂ adsorption. $^{39,40}$ However, for benzene adsorption on silicalite, various observations and arguments have been raised on the crystalline form based on different methods and techniques. The experimentally measured isotherms of aromatic $^{24-27}$ adsorption on silicalite exhibit a characteristic step or kink around 4 molecules/unit cell (u.c.) This phenomenon has been ascribed to a sorbate-induced phase transition of the framework from ORTHO to PARA, or coexisting ORTHO and PARA phases at 4-7 molecules/u.c based on molecular simulation, $^{41}$ molecular theories, $^{42}$ and experimental observations. $^{25,26}$ But other researchers $^{37,43}$ attributed this step change in isotherms to the rearrangement or reorientation of adsorbed benzene molecules, and they considered the tiny distinction in the phase transition of the framework structure to be insignificant to the adsorption isotherms. Huang and Havenga $^{28}$ studied the benzene adsorption in silicalite by Fourier transform (FT)-Raman spectroscopy and showed that the phase transformation of the framework emerges from MONO to PARA at the loading of 4-5 molecules/u.c, and from PARA to ORTHO at 6-7 molecules/u.c. By far, these are not very overwhelming conclusions for the detailed form of the silicalite solid framework for benzene adsorption.

To eliminate the complexity in this study, the ORTHO form of silicalite framework was adopted in our research of the mixture (CO₂ and benzene) adsorption. The silicon and oxygen atoms of the zeolite framework were fixed at the crystallographic coordinates determined from the X-ray powder diffraction of Olson et al. $^{17}$ The lattice parameters of the unit cell were reported for Pnma as $a = 20.07$ Å, $b = 19.92$ Å, and $c = 13.42$ Å.

Carbon dioxide and benzene were treated as rigid units with Lennard-Jones sites and partial point charges. Carbon dioxide was modeled as a rigid 3-center molecule, and a rigid 12-center model represents the benzene molecule. For the CO₂ molecule, the carbon-oxygen bond length was fixed at 1.16 Å. The carbon-hydrogen and carbon-carbon bond lengths for benzene were fixed at 1.40, 1.08 Å, respectively. The intermolecular interactions (1) involve the van der Waals (VdW) and Coulomb terms as follows: $^{34}$

$$
\phi_{ij}(r_{ij})=A/r_{ij}^{12}+B/r_{ij}^{6}+C/r_{ij}^{2}+D+q_{i}q_{j}/r_{ij} \quad (1)
$$

where $A$ and $B$ represent the repulsive and attractive interaction parameters, respectively. $C$ and $D$ were introduced to yield a correct Coulomb interaction for the benzene interaction. $^{34,44}$ $q_{i}$ and $q_{j}$ are the partial charges of the sites. The benzene/benzene interaction was calculated by the 12-6-2-0 model; $^{34}$ other intermolecular interactions were calculated using the conventional method including the Lennard-Jones (12-6) and Coulomb potentials. The long-range Coulomb interaction was handled using the Ewald technique in both the MD and GCMC simulations. The potential parameters for the CO₂ molecule were obtained from references. $^{39,45,46}$ For benzene and silicalite, the parameters were adopted from reference 34, where the model was successful in reproducing experimental isotherms of pure benzene on

(18) Dunne, J. A.; Mariwala, R.; Rao, M.; Sircar, S.; Gorte, R. J.; Myers, A. L. Langmuir 1996, 12, 5888-5895.

(19) Bernal, M. P.; Coronas, J.; Menendez, M.; Santamaria J. AIChE J. 2004, 50 (1), 127-135.

(20) Sivasanker, S.; Ramaswamy, A. V.; Ratanasamy, P. Appl. Catal., A 1996, 138 (2), 369-379.

(21) Akah, A.; Cundy, C.; Garforth, A. Appl. Catal., B 2005, 59 (3-4), 221-226.

(22) Park, K. C.; Ihm, S. K. Appl. Catal., A 2000, 203, 201-209.

(23) Richards, R. E.; Rees, L. V. C. Zeolite 1988, 8, 35-39.

(24) Talu, O.; Guo, C. J.; Hayhurst, D. T. J. Phys. Chem. 1989, 93, 3, 7294-7298.

(25) Van Koningsveld, B. H.; Tuinstra, F.; Van Bekkum, A. H.; Jansen, J. C. Acta Cryst. 1989, B45, 423-431.

(26) Guo, C. J.; Talu, O. AIChE J. 1989, 35 (4), 573-578.

(27) Shah, D. B.; Hayhurst, D. T.; Evanina, G.; Guo, C. J. AIChE J. 1988, 34 (10), 1713-1717.

(28) Huang, Y. N.; Havenga, E. A. J. Phys. Chem. B 2000, 104, 5084-5089.

(29) Song, L. J.; Sun, Z. L.; Rees, L. V. C. Microporous Mesoporous Mater. 2002, 55, 31-49.

(30) Li, J. M.; Talu, O. Chem. Eng. Sci. 1994, 49 (2), 189-197.

(31) Zikanova, A.; Bulow, M.; Schlodder, H. Zeolites 1987, 7, 115-118.

(32) Shen D. M.; Rees, L. V. C. Zeolites 1991, 11, 666-671.

(33) Jobic, H.; Bee, M.; Pouget, S. J. Phys. Chem. B 2000, 104, 7130-7133.

(34) Gupta, A.; Clark, L. A.; Snurr, R. Q. Langmuir 2000, 16, 3910-3919.

(35) Mohanty, S.; Davis, H. T.; McCormick, A. V. Chem. Eng. Sci. 2000, 55, 2779-2792.

(36) Chempath, S.; Snurr, R. Q.; Low, J. J. AIChE J. 2004, 50 (2), 463-469.

(37) Song, L. J.; Sun, Z. L.; Ban, H. Y.; Dai, M.; Rees, L. V. C. Phys. Chem. Chem. Phys. 2004, 6, 4722-4731.

(38) Flanigen, E. F.; Bennett, J. M.; Grose, R. W.; Cohen, J. P.; Patton, R. L.; Kirchner, R. M. Nature 1978, 271, 512-516.

(39) Goj, A.; Sholl, D. S.; Akten, E. D.; Kohen, D. J. Phys. Chem. B 2002, 106, 8367-8375.

(40) Makrodimitris, K.; Papadopoulos, G. K.; Theodorou, D. N. J. Phys. Chem. B 2001, 105, 777-788.

(41) Snurr, R. Q.; Bell, A. T.; Theodorou, D. N. J. Phys. Chem. 1993, 97, 13742-13752.

(42) Snurr, R. Q.; Bell, A. T.; Theodorou, D. N. J. Phys. Chem. 1994, 98 (19), 5111-5119.

(43) Lee, C. K.; Chiang A. S. T.; Wu, F. Y. AIChE J. 1992, 38 (1), 128-135.

(44) Shi, X. Q.; Bartell, L. S. J. Phys. Chem. 1988, 92, 5667-5673.

(45) Hirotani, A.; Mizukami, K.; Miura, R.; Takaba, H.; Miya, T.; Fahmi, A.; Stirling, A.; Kubo, M.; Miyamoto, A. Appl. Surf. Sci. 1997, 120, 81-84.

(46) Kobayashi, Y.; Takami, S.; Kubo, M.; Miyamoto, A. Fluid Phase Equilib. 2002, 194-197, 319-326.

<table>
<thead>
<tr><th colspan="6">Table 1. Potential Parameters for CO₂, Benzene, and Silicalite</th></tr>
<tr><th>interaction</th><th>A (Å¹²·kcal·mol⁻¹)</th><th>B (Å⁶·kcal·mol⁻¹)</th><th>C (Å²·kcal·mol⁻¹)</th><th>D (kcal·mol⁻¹)</th><th>q (|e|)</th></tr>
</thead>
<tbody>
<tr><td colspan="6">CO₂</td></tr>
<tr><td>C−C</td><td>49835.46</td><td>−103.4166</td><td></td><td></td><td>0.574</td></tr>
<tr><td>O−O</td><td>406914.8</td><td>−505.4806</td><td></td><td></td><td>−0.287</td></tr>
<tr><td colspan="6">Benzene</td></tr>
<tr><td>C−C</td><td>698828.9</td><td>−569.7</td><td>8.389</td><td>−0.3346</td><td>−0.15</td></tr>
<tr><td>H−H</td><td>6630.0</td><td>−18.6</td><td>8.389</td><td>−0.3346</td><td>0.15</td></tr>
<tr><td>C−H</td><td>91826.0</td><td>−112.26</td><td>−8.389</td><td>0.3346</td><td></td></tr>
<tr><td colspan="6">Silicalite</td></tr>
<tr><td>O</td><td>165379.9</td><td>−343.1899</td><td></td><td></td><td>−1.0</td></tr>
<tr><td>Si</td><td></td><td></td><td></td><td></td><td>2.0</td></tr>
</tbody>
</table>

silicalite.⁴¹ The VdW interaction with the silicon atoms in the solid framework was neglected because of very weak contribution, and only electrostatic interaction was considered between the adsorbates and the Si atoms. All the interaction parameters for the CO₂, benzene, and zeolite atoms are listed in Table 1. The mixing interaction between different atoms was calculated by the Lorentz−Berthelot mixing rule, in which the Lennard-Jones parameters of the benzene molecule were obtained from the 12-6 terms of the original 12-6-2-0 model.⁴⁴ A spherical cutoff radius of 13 Å was used in calculating the adsorbate−adsorbate and adsorbate−zeolite interactions.

Methods. The single-component CO₂ and benzene/CO₂ mixture adsorption simulations were carried out using the conventional GCMC method.⁴⁷ The simulations were run using the MUSIC code.⁴⁸ Eight unit cells of silicalite (2 × 2 × 2) were used to construct the simulation box of the GCMC run, and the periodic boundary condition was applied for three directions. A combined energy/cavity biasing technique³⁶,⁴¹ for the adsorbate molecules was adopted for increasing the acceptance efficiency of insertion. With this technique, the molecule insertion was biased according to the energy of the zeolite, but it also tries to avoid overlaps with existing sorbate molecules in the framework.

To ensure fast equilibrium, the final configuration of the last run was used as the initial configuration of the next run. In our simulation, the single-component GCMC simulations were run for about 6 × 10⁶ Monte Carlo steps, while the simulations of the mixtures were run for 1 × 10⁷ steps. The first half of these simulation steps were discarded for equilibration, and the rest of the steps were included in the averaging. For the systems in this study, the corresponding chemical potential of the bulk phase was calculated using the Peng−Robinson equation of state (P−R EOS),⁴⁹ which is very efficient for the description of supercritical fluid mixtures. The relevant binary interaction parameters in the P−R EOS for the benzene/CO₂ mixture was obtained by fitting the relevant bulk-phase mixture equilibrium data.⁵⁰⁻⁵² To reduce the simulation time, the Coulomb interaction and the Lennard-Jones interaction between the adsorbate and the zeolite were calculated on the basis of a pretabulation of the potential at the nodes of a 0.2 × 0.2 × 0.2 Å cubic mesh constructed throughout the unit cell of silicalite.

MD simulations were used to study diffusion properties of binary mixtures (benzene/CO₂) in silicalite. The MD simulations were performed in a standard NVT ensemble at 328.2 K. The simulation cell is the same as that used in the previous GCMC run with three-dimensional periodic boundary conditions. The final configuration of the GCMC run in different pressures at 328.2 K was used as the initial configuration in the MD simulation. The time step is 1 fs in all the MD simulations. A first MD run of 100 ps was performed to ensure the system equilibrium. The product run was followed for the next 1000 ps. Molecule configuration data were saved every 0.1 ps, from which the diffusion analysis was undertaken.

![](./images/812111672352178177_1.jpg)

Figure 1. (a) Absolute adsorption isotherms of SC-CO₂ fluid. (b) Excess adsorption isotherms. (c) Excess adsorption amount as a function of fluid density. Lines were drawn to guide the eyes.

### 3. Results and Discussion

#### 3.1. GCMC Simulation. Single-Component CO₂ Adsorption.
The absolute adsorption isotherms of pure CO₂ on the silicalite were obtained based on the GCMC approach at 308.2, 318.2, and 328.2 K, in the pressure range of low pressure to 20 MPa. Figure 1a gives the obtained absolute adsorption isotherms plotted as a function of pressure. The absolute isotherms exhibit type I features with a steep rise at low pressure. This obvious adsorption of CO₂ is caused by an interaction of the quadrupole moment of CO₂ with the electrostatic field of the zeolite. At higher pressure (>5 MPa), there is almost complete filling of the zeolite pores, leading to the final plateau of isotherms, with the saturating adsorption amount being 3.4−3.7 mmol/g (≈19.6−21.3 molecules/u.c.), which is lower than the experimental data of CO₂ adsorption on 13X zeolite.⁵³ The excess adsorption amount, $n^{\text{ex}}$,

(47) Allen, M. P.; Tildesley, D. J. Computer Simulation of Liquids; Clarendon Press: Oxford, 1987.
(48) Gupta, A.; Chempath, S.; Sanborn, M. J.; Clark, L. A.; Snurr R. Q. Mol. Simul. 2003, 29 (1), 29−46.
(49) Elliott, J. R.; Lira, C. T. Introductory Chemical Engineering Thermodynamics; Prentice Hall PTR: London, 1999.
(50) Gupta, M. K.; Li, Y. H.; Huisey, B. J.; Robinson, R. L. J. Chem. Eng. Data 1992, 27, 55−57.
(51) Kim, C. H.; Vimalchand, P.; Donohue, M. D. Fluid Phase Equilib. 1986, 31, 299−311.
(52) Yan, B.; Yang, X. N. Ind. Eng. Chem. Res. 2004, 43, 6577−6586.

(53) Hocker, T.; Rajendran, A.; Mazzotti, M. Langmuir 2003, 19, 1254−1267.

![](./images/812111672352178177_2.jpg)

Figure 2. A comparison between the adsorption isotherms of the molecular simulation and those of the experimental data for pure CO₂ component. The inset shows the adsorption of low-pressure parts in a semilog scale.

is related to the absolute adsorption amount, $n^{\text{abs}}$, from the following equation:

$$
n^{\text{ex}} = n^{\text{abs}} - V^{\text{g}} \rho^{\text{g}} \tag{2}
$$

where the pore volume of silicalite ($V^{\text{g}}$) is adopted to be 175 cm³/kg from reference 54. $\rho^{\text{g}}$ is the molar density of the bulk fluid phase in mol/cm³, and it is estimated from the P−R EOS. As shown in Figure 1b, each excess adsorption isotherm shows a maximum in the medium-pressure range (4−5 MPa), which is a typical characteristic of supercritical adsorption. This phenomenon is usually caused by a significant change in the bulk CO₂ fluid density near its critical point.

Adsorption of pure CO₂ on silicalite from low to medium pressures has been measured previously. Figure 2 gives a comparison between the excess adsorption from the GCMC simulations and that from the experimental data.¹⁸,⁵⁵,⁵⁶ Even though there is a bit of a discrepancy at very low pressure, an overall good agreement between them is achieved, confirming that the model and method are reasonable.

In Figure 1a, as expected, the absolute adsorption isotherms decrease with increasing temperature, and no crossover is observed among the three temperatures. However, the three excess adsorption isotherms in Figure 1b show a crossover in their descending part in the neighborhood of 7 MPa, which is near the critical pressure of CO₂. It can also be observed that, as temperature decreases, the location of the maximum adsorption slightly shifts to lower pressure. The crossover phenomenon will disappear if the data is plotted as a function of fluid density (Figure 1). This crossover behavior is not new and can often be observed in the temperature and pressure dependence of solute solubility in supercritical fluid.⁵²,⁵⁷ In general, it can be explained as the simultaneous contributions from two competitive factors:⁵² temperature and bulk fluid density. Throughout the remainder of this paper, all adsorption data are reported in terms of absolute adsorption amount.

On the basis of the simulation results, CO₂ molecules get occupied on all adsorption positions in silicalite, such as straight channel, zigzag channel, and intersection. The density distributions of adsorbed CO₂ molecules in silicalite, at 0.05 MPa/318.2 K and 8 MPa/318.2 K, are illustrated in Figure 3, where the number of CO₂ molecules was statistically counted for 3000 configurations along the z-direction. It is clearly observed that, at low pressure with low adsorption loading, the density distribution shows a maximum in the middle part of the straight channels, while, at high pressure corresponding to high loading, more and more CO₂ molecules are forced to adsorb into the intersection, leading to a larger density distribution in the intersection. The behavior of CO₂ adsorption sites is consistent with the average interaction energy between CO₂ and silicalite; that is, the weaker interaction energy occurs at the intersection position.

![](./images/812111672352178177_3.jpg)

Figure 3. Density distribution of the center-of-mass of CO₂ along the z-direction: (a) 0.05 MPa/318.2 K; (b) 8 MPa/318.2 K. The white section represents the solid framework of silicalite.

![](./images/812111672352178177_4.jpg)

Figure 4. The orientation probability distributions of pure CO₂ in silicalite by GCMC.

The orientation of CO₂ molecules in the silicalite pores at different bulk pressures is described in Figure 4, in the form of the orientation probability distribution $P(\varphi)$.⁵⁸ The $\varphi$ is defined

(54) Talu, O.; Myers, A. L. AIChE J. 2001, 47 (5), 1160−1168.
(55) Golden, T. C.; Sircar, S. J. Colloid Interface Sci. 1994, 162, 182−188.
(56) Sun, M. S.; Shah, D. B. Xu, H. H.; Talu, O. J. Phys. Chem. B 1998, 102, 1466−1473.
(57) Gurdial, G. S.; Foster, N. R. Ind. Eng. Chem. Res. 1991, 30, 575−580.

![](./images/812111672352178177_5.jpg)

Figure 5. The isosteric heat of adsorption for CO₂ on silicalite at 308.2 K, 318.2 K, and 328.2 K as a function of adsorbed amount; inset shows the average potential energy per CO₂ molecule at 318.2 K. Lines were drawn to guide the eyes.

as the angle between the vector along the z-direction and the CO₂ molecular axis. CO₂ molecules mainly orientate with $\varphi$ being 90°, which means that the CO₂ molecule prefers to be parallel to the x/y-plane. The orientation distributions show a similar orientation pattern for different bulk pressures, suggesting that enhancing CO₂−CO₂ interaction does not affect the main orientation manner of adsorbed CO₂ molecules.

We also computed the isosteric heats of adsorption ($Q_{\text{st}}$) of CO₂ on silicalite. $Q_{\text{st}}$ is defined as the difference between the partial molar enthalpy of CO₂ in the bulk phase and the partial molar internal energy in the adsorbed phase⁵⁹ as follows:

$$
Q_{\text{st}} = -\left(h^{\text{b},*} - h^{\text{b}}\right) + RT - \left(\partial U^{\text{a}}/\partial n^{\text{a}}\right)_{\text{T}} \tag{3}
$$

where the quantity $(h^{\text{b},*} - h^{\text{b}})$ is the departure function of the partial molar enthalpy of bulk CO₂ fluid, calculated by the P−R EOS. $U^{\text{a}}$ is the average internal energy of adsorbate in the adsorbed phase, obtained from the molecular simulation.

Figure 5 shows the isosteric heat of adsorption for CO₂ as a function of the adsorbed amount in silicalite at 308.2, 318.2, and 328.2 K. The isosteric heat of adsorption in the limit of zero loading is independent of temperature, being ~23.5 kJ/mol. This value is close to the experimental data of Golden and Sircar⁵⁵ (24.07 kJ/mol at 300 K), but lower than the data from Dunne et al.¹⁸ (27.2 kJ/mol) and higher than the result (20.0 kJ/mol) from Choudhary and Mayadevi.⁶⁰ Moreover, Sun et al.⁵⁶ reported a value of 28.5 kJ/mol at CO₂ loading 2.5 mmol/g, which is in very good agreement with our result. This comparison provides an additional check of the model and method in this work.

Under the three temperatures, the adsorption heat of CO₂ on silicalite increases slightly at first with the adsorption loading, and eventually decreases rapidly, as shown in Figure 5. The changing behavior of the adsorption heat has been observed in a previous study,³⁹ and it signifies that the CO₂ adsorption sites in this solid material are relatively homogeneous. The increase in $Q_{\text{st}}$ with loading can be attributed to an enhancing interaction between CO₂ molecules, whereas the interaction between CO₂ molecules and adsorbent remains essentially unchanged. The presence of maximum values in $Q_{\text{st}}$ at high adsorption occupancy is due to the increasing importance of the bulk fluid term in eq 3. This molecular energy has been given in the inset of Figure 5, where the average potential energy per CO₂ molecule on silicalite at 318.2 K is split into the adsorbate−adsorbate interaction and the adsorbate−adsorbent interaction.

Benzene/CO₂ Mixture. The adsorption loadings for both the solute (benzene) and the solvent (CO₂) on silicalite were calculated simultaneously by the GCMC simulation. Figure 6 shows the corresponding individual adsorption amounts against pressure at 318.2 and 328.2 K, with the bulk mole fraction of benzene being 0.001. As expected, with pressure increasing, the adsorption amount of benzene on silicalite decreases, while the adsorption of CO₂ gradually increases. Although the benzene adsorption display is somewhat scattered, it can still be seen that the adsorption has a weak temperature dependence. The inset of Figure 6 gives the corresponding mole fraction of benzene in adsorbed phase against pressure. At very low pressure, the adsorbed phase is greatly enriched in benzene as a result of the stronger affinity between benzene and zeolite. However, under high-pressure conditions, the benzene content in the adsorbed phase decreases remarkably. This result suggests that SC-CO₂ can be used as an efficient desorbent of larger aromatics in the zeolite material. With further increase in pressure (approximately 15 MPa), the adsorption loadings of the mixture approximately level off to constant values, meaning that it is not possible to further improve the regeneration performance beyond a certain pressure.

![](./images/812111672352178177_6.jpg)

Figure 6. Adsorption isotherms of benzene/CO₂ as a function of pressure. The inset shows the mole fraction of benzene in the adsorbed phase as a function of pressure. The lines were drawn to guide the eyes.

The pressure dependence of the mixture adsorption in Figure 6 is similar to that observed for the mixture adsorption on activated carbon.¹⁶,⁵² It is mainly due to the fact that the solvating power of supercritical fluids is enhanced with increasing pressure. The variation in solvating power with pressure could be described by the fluid fugacity. The corresponding relations of the bulk fluid fugacities of benzene and CO₂ follow a similar pattern⁵² compared with the corresponding adsorption amounts. The fugacity of the nonideal mixture determines, to a larger extent, its nonideal adsorption performance.

Apart from the nonideal characteristics of the bulk phase, the competition adsorption of the CO₂ solvent also has an effect on the solute adsorption/desorption on silicalite. The density distribution of benzene and CO₂ molecules along the channels of the unit cell, in three different pressures and at 328.2 K, were plotted in Figure 7, where around 4000 configurations were collected and averaged. In Figure 7a,c, the high peaks along the x-direction correspond to the accumulating positions of molecules in the zigzag channels, whereas Figure 7b,d shows the relevant positions along the straight channels. As seen from Figure 7, under lower pressure, a considerable amount of benzene molecules is adsorbed on the silicalite, especially in the intersection locations. However, under higher pressure, benzene molecules get excluded from the channels due to competitive occupation from CO₂ molecules.

To further examine this adsorption behavior of the mixture, a series of configuration snapshots of the CO₂ and benzene molecules on the x/y-plane of silicalite, during the adsorption

(58) Yang, X. N.; Zhang, C. J. Chem. Phys. Lett. 2005, 407, 427−432.
(59) Karavaias, F.; Myers, A. L. Langmuir 1991, 7, 3118−3126.
(60) Choudhary, V. R.; Mayadevi, S. Zeolites 1996, 17, 501−507.

![](./images/812111672352178177_7.jpg)

**Figure 7.** Density distribution of molecules along the channels of a unit cell: (a) benzene along the $x$-direction; (b) benzene along the $y$-direction; (c) $\text{CO}_2$ along the $x$-direction; (d) $\text{CO}_2$ along the $y$-direction.

from low to high pressures, are shown in Figure 8a−f. As depicted in the snapshots, at low pressure with high loading of benzene, benzene molecules stay at both the spacious intersections and the comparatively narrow straight and zigzag channels. At medium pressure, benzene molecules preferentially occupy the intersection and straight channels. But, at high pressure corresponding to low loading of benzene, benzene is solely adsorbed in the intersection position. This observation further confirms that, because of $\text{CO}_2$ competition adsorption, benzenes in the zigzag channels are first forced to desorb with increasing pressure, then those in the straight channels, and finally those in the intersections. Furthermore, it also indicates that benzene molecules preferentially occupy the channel intersections at low loading, which is in agreement with the adsorption behavior of pure benzene on silicalite. $^{28,37,41,61}$ It was also observed that a benzene molecule and a $\text{CO}_2$ molecule cannot coexist in straight channels, due to limited space and adsorption sites.

We calculated the average potential energy of benzene/silicalite in three different adsorption sites at low coverage. The results are $-53.12$ kJ/mol in channel intersections, $-46.03$ kJ/mol in straight channels, and $-46.13$ kJ/mol in sinusoidal channels. These energies are consistent with the previously reported values from Snurr et al. $^{41,62}$ The difference in the adsorbate−adsorbent energy between the straight and sinusoidal channels is minor. Thus, the preferential benzene adsorption in straight channels relative to that in the sinusoidal channels reveals that the space effect could be apparent due to entropy contribution.

The average potential energies per adsorbed molecule in the mixture at 318.2 K were plotted against pressure in Figure 9. Obviously, the contribution from the adsorbate−adsorbent interaction is larger than the adsorbate−adsorbate interaction. This presentation in Figure 9 can be explained based on the adsorption performance in Figure 8 and the adsorbate−adsorbent interaction in different adsorption sites. With pressure increasing, the benzene loading in the straight and sinusoidal channels becomes reduced, and, at higher pressures, they are only located in the channel intersections. This means that the benzene molecules become more energetically favorable, leading to a decrease in the interaction energy of benzene/silicalite. Similarly, the interaction energy between $\text{CO}_2$ and silicalite increases slightly with pressure, indicating that more $\text{CO}_2$ adsorbs in the relatively less energetically favorable intersection sites. In the inset of Figure 9, the $\text{CO}_2/\text{CO}_2$ interaction energy becomes more attractive (negative) with pressure, while the benzene/benzene attractive interaction becomes weak. This is because, at low benzene loading (high pressure), only a few benzene molecules are adsorbed in the channel intersections, in which the distance between the benzene molecules is too far to experience significant adsorbate−adsorbate interactions.

GCMC simulation of the benzene/$\text{CO}_2$ system has also been performed for different bulk-phase compositions at 318.2 K and 328.2 K, when the total bulk-phase pressures were kept at 7, 9, and 15 MPa. According to the vapor−liquid equilibrium data of benzene/$\text{CO}_2$, $^{50,51}$ the chosen mole fractions of benzene in our simulations guarantee the bulk phase to be a single phase. The adsorbed amounts of each component, plotted as a function of the mole fractions of benzene, are shown in Figure 10. The adsorption amounts rise for benzene and reduce for $\text{CO}_2$ with an increase in the benzene composition. According to the simulation, benzene molecules first prefer to locate at the intersection positions, and then some of them are forced to fit into the narrow straight channels as benzene increases. This changing manner of adsorption agrees with the observation in Figure 8. However, in the mixture adsorption, benzene molecules could be adsorbed in the straight channels, even though there is still space available in the intersections. This is in contrast with the pure benzene adsorption on silicalite, $^{28,41}$ where benzenes only begin to occupy on the channels when the intersections have been fully loaded. This discrepancy could be explained by the existence of $\text{CO}_2$ in the intersection position, which might obstruct the further occupation of benzene molecules.

The statistical distributions of orientation for the adsorbed benzene and $\text{CO}_2$ molecules in the silicalite pores under different pressures are depicted in Figure 11, panels a and b, respectively. The definition of $P(\varphi)$ and $\varphi$ for $\text{CO}_2$ is the same as that in Figure 4, while, for benzene molecules, the orientation angle is defined as the angle between the $z$-axis and the normal vector of the benzene plane, which also stands for the angle between the plane of the benzene molecule and the solid $x/y$-plane. It can be seen from Figure 11a that, under relatively lower pressure, there are two orientation peaks in the angle distribution, corresponding to $15-18^\circ$ and $38-40^\circ$. However, as pressure increases, the orientation peak at $15-18^\circ$ becomes more apparent, and another orientation peak becomes minor. At high loading of benzene (low pressure), benzene molecules stay not only at the intersections, but also at the channels of the zeolite; thus, the two main orientations correspond to the two various adsorption sites of benzene in the framework. On the other hand, at high pressure (low benzene loading), benzene molecules mainly reside at the intersections, where the angle between the plane of benzene and the $x/y$-plane is only about $15^\circ$. This analysis shows that, at the intersection positions, the benzene molecule plane mainly orientates parallel to the solid $x/y$ plane with a slightly tilted angle (approximate $15^\circ$), whereas, at channel sites, they become more tilted due to the relatively narrow space. This orientation behavior can be clearly observed in Figure 8.

In Figure 11b, the $\text{CO}_2$ orientation distributions in the mixture show a pattern similar to those in a pure $\text{CO}_2$ system, especially for high-pressure conditions. At lower pressure, most $\text{CO}_2$ molecules stay on the narrow channels in the zeolite due to the competition effect of benzene. Thus, the peak of orientation distribution becomes comparatively sharper than that of pure $\text{CO}_2$ in Figure 4.

(61) Klemm, E.; Wang, J. G. *Microporous Mesoporous Mater.* **1998**, 26, 11−21.

(62) Clark, L. A.; Snurr, R. Q. *Chem. Phys. Lett.* **1999**, 308, 155−159.

![](./images/812111672352178177_8.jpg)

Figure 8. Typical x/y-plane snapshots of benzene/CO₂ mixtures in the zeolite at different pressures and 328.2 K: (a) 1 MPa; (b) 3 MPa; (c) 5 MPa; (d) 9 MPa; (e) 12 MPa; (f) 15 MPa. The red color represents oxygen atoms, the green is carbon, the yellow is silicon, and the black is hydrogen.

3.2. Molecular Dynamic Simulation. Presently, there are increasing MD studies of mixture diffusion in zeolites⁶³ (also see the relevant references cited therein); however, to our knowledge, very little MD research is available for the nonideal SC-CO₂ fluid mixtures. In this section, the self-diffusion behaviors of the benzene/CO₂ system have been studied through the MD simulation. The diffusion coefficients were calculated based on the Einstein relation, and the mean square displacement (MSD) was evaluated using the following expression:

$$
\text{MSD}(t) = 1/(N_{\text{m}}N_{t0})\sum_{\text{m}} \sum_{t0}[\mathbf{r}_{i}(t + t_{0}) - \mathbf{r}_{i}(t_{0})]^2 \tag{4}
$$

where $\mathbf{r}_{i}(t)$ is the position vector of the center-of-mass of molecule

(63) Gupta, A.; Snurr, R. Q. J. Phys. Chem. B 2005, 109, 1822−1833.

![](./images/812111672352178177_9.jpg)

Figure 9. The average interaction potential energy as a function of pressure at 318.2 K. The inset shows the adsorbate−adsorbate interaction potential energy.

![](./images/812111672352178177_10.jpg)

Figure 10. Adsorption isotherms of benzene/CO₂ mixtures as a function of the mole fraction of benzene at 318.2 K and under three different pressures.

![](./images/812111672352178177_11.jpg)

Figure 11. The individual orientation probability distribution in the mixture at 328.2 K.

$i$ at time $t$. $N_{\text{m}}$ is the number of diffusing molecules, and $N_{\text{t0}}$ is the number of time origins used in calculating the averaging properties.

The initial configuration of the mixture in the MD simulation was from the final equilibrium configuration of the GCMC adsorption simulation, from which the ratio of the number of molecules of CO₂ and benzene in the silicalite is chosen to be 153/4, 147/7, 134/18, 131/22, and 109/35 molecules per simulation cells, corresponding to 19.1/0.5, 18.4/0.9, 16.8/2.3, 16.4/2.8, and 13.6/4.4 per unit cell, respectively. These simulation situations represent the five different bulk fluid conditions at 328.2 K in Figure 6, with pressures from 3 to 15 MPa and a fixed mole fraction of benzene (0.001). For the five different bulk conditions, the obtained diffusion coefficients of CO₂ and the MSDs of benzene are shown in Figure 12. For the CO₂ molecule, the self-diffusion coefficient in the mixture is 1 order of magnitude lower than that in the pure component system.⁴⁰,⁶⁴⁻⁶⁶ However, we can clearly see that, as seen in Figure 12a, the diffusion coefficient of CO₂ increases with pressure (adsorption loading of CO₂), which is contrary to the observation for a pure CO₂ system in silicalite. This contrary behavior is mainly caused by the dominant blocking or trapping⁶³ effect from larger coadsorbed benzene molecules. This effect will become weak at higher pressure (lower benzene loading). There is a steep increase in the CO₂ diffusion coefficients between pressures of 9−12 MPa, which is probably due to the obvious drop in the loading of benzene molecules. In the inset of Figure 12a, the three components of MSD for CO₂ in a mixture at 15 MPa are shown. An anisotropic feature is apparently observed with the different slopes along the three directions, which is identical to those in the pure CO₂ system and other small molecules in silicalite.⁶⁷⁻⁶⁹

![](./images/812111672352178177_12.jpg)

Figure 12. The diffusion coefficient of CO₂ and the MSDs of benzene in the mixture at different bulk pressures, which correspond to the adsorption isotherms at 328.2 K in Figure 6. The inset shows the MSD of the CO₂ molecule of the mixture in different directions at 15 MPa.

Figure 12b demonstrates the MSD of the center-of-mass of a benzene molecule for the different bulk pressures in the mixture. Although the MSDs show a general behavior to some extent, that is, decreasing with benzene loading, the trend of MSD against

(64) Papadopoulos, G. K.; Jobic, H.; Theodorou, D. N. *J. Phys. Chem. B* **2004**, 108, 12748−12756.

(65) Karger, J.; Pfeifer, H.; Stallmach, F.; Feoktistova, N. N.; Zhdanov, S. P. *Zeolites* **1993**, 13, 50−55.

(66) Shen, D.; Rees, L. J. *J. Chem. Soc., Faraday Trans.* **1994**, 90 (19), 3011−3015.

(67) Luca, G. D.; Pullumbi, P.; Barbieri, G.; Fama, A. D.; Bernardo, P.; Drioli, E. *Sep. Purif. Technol.* **2004**, 36, 215−228.

(68) Fritzsche, S.; Karger, J. *J. Phys. Chem. B* **2003**, 107, 3515−3521.

(69) June, R. L.; Bell, A. T.; Theodorou, D. N. *J. Phys. Chem.* **1992**, 96 (3), 1051−1060.

simulation time is notably nonlinear. The most striking feature is that the MSDs show a sharp rise at the beginning, and then oscillate around a constant value.⁷⁰ The estimated diffusion coefficient is very small, with an order of magnitude of $10^{-15}-$$10^{-12}$ m²/s. This phenomenon of MSD for benzene is related to a tight adsorption of benzene in silicalite pores, leading to trouble in movement. This anomalous behavior of benzene diffusion is analogous to the previous report of the diffusion of pure benzene in rigid silicalite from MD simulation,⁷¹ in which the Burchart–Dreiding force field has been applied and the estimated diffusion coefficient is between $2.0 × 10^{-15}$ and $3.7 × 10^{-12}$ m²/s. In addition, for pure benzene diffusion on silicalite, various experimental data are available in the range of $9 × 10^{-15}$ to $1.24 × 10^{-13}$ based on different experimental methods.²⁷,²⁹,³¹⁻³³,³⁷

Figure 13 gives the obtained moving trajectory of benzene and $\mathrm{CO}_{2}$ molecules, where three $\mathrm{CO}_{2}$ molecules and two benzene molecules in different adsorption sites were picked up from the simulation of 35 benzene and $109 \mathrm{CO}_{2}$ molecules in the simulation cell. In this figure, a series of configurations during a 50 ps MD simulation run were collected and drawn. It can be seen that the benzene molecule in the intersection shows slight translational and rotational movement, but, in the straight channel, the benzene molecule only has very weak vibration around the original position. In both cases, benzene diffusion is practically forbidden. On the other hand, for $\mathrm{CO}_{2}$ molecules, the translational and rotational motions are relatively apparent because of its small molecular size.

All MD simulations and experimentally reported results imply the near immobility of benzene molecules confined in the silicalite pores. Thus, the conventional MD technique may not be the appropriate choice for the large benzene molecule, and the slow diffusion behavior should be studied through a rare event technique.⁷²,⁷³ Additionally, a fixed rigid framework was applied in this work. For a benzene molecule (kinetic diameter: $5.85 \mathring{A}$) with tight adsorption in the nanopore, it appears that a large induced distortion in the framework structure may occur, and this flexibility of the framework might produce an effect on the benzene diffusion within the zeolite.

![](./images/812111672352178177_13.jpg)

Figure 13. Typical moving trajectory of benzene and $\mathrm{CO}_{2}$ molecules from the MD simulation. The yellow represents the framework, the red represents the oxygen of $\mathrm{CO}_{2}$, the gray represents carbon, and the white represents hydrogen.

### 4. Conclusions

In this study, GCMC and MD simulations were performed to study the adsorption equilibrium and dynamical diffusion for a benzene/$\mathrm{CO}_{2}$ mixture. The effect of pressure, temperature, and bulk composition on the adsorption behavior of the supercritical fluids was investigated. The adsorption isotherm and adsorption heat of pure $\mathrm{CO}_{2}$ were obtained, which are in good agreement with available experimental data. The favorable sorption site for benzene in a mixture is the intersection position, with favorable energy and space effects. At high loading, benzene molecules begin to fill the straight channels. An analysis of mixture configurations indicates that $\mathrm{CO}_{2}$ molecules mainly orientate parallel to the $x$/$y$-plane, while benzene molecules mainly stay at the intersections and show a tilted pattern. Benzene molecules and $\mathrm{CO}_{2}$ molecules cannot coexist in the straight channels because of limited space and adsorption competition. The simulation results suggest that $\mathrm{SC-CO}_{2}$ can be used as an efficient desorbent of larger aromatics in the zeolite material.

A tentative study of the diffusion behaviors of the benzene/ $\mathrm{CO}_{2}$ mixture has been carried out. For the $\mathrm{CO}_{2}$ molecule, the self-diffusion coefficient in the mixture is 1 order of magnitude lower than that in the pure component system, and the diffusion coefficient of $\mathrm{CO}_{2}$ increases with loading of $\mathrm{CO}_{2}$, which is contrary

(70) Hou, T. J.; Zhu, L. L.; Xu, X. J. J. Phys. Chem. B 2000, 104, 9356−9364.
(71) Fried, J. R.; Werver, S. Comput. Mater. Sci. 1998, 11, 277−293.
(72) Dubbeldam, D.; Beerdsen, E.; Vlugt, T. J. H.; Smit, B. J. Chem. Phys. 2005, 122, 224712.
(73) Vlugt, T. J. H.; Dellago, C.; Smit, B. J. Chem. Phys. 2000, 113 (19), 8791−8799.

to the observation for pure $CO_2$ systems in silicalite. This contrary behavior is mainly caused by the dominant blocking or trapping effect from larger coadsorbed benzene molecules. The diffusion rate of benzene in the mixture is very small, indicating the near immobility of benzene molecules tightly confined in the zeolite pores.

**Acknowledgment.** This work has been supported by the National Natural Science Foundation of China through Grant No. 20276028. The starting research funding of overseas scholars from the Ministry of Education of China is greatly acknowledged.

LA052843F