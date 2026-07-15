![](./images/811644053815820289_1.jpg)

# Mechanical and thermal transport properties of graphene with defects

Feng Hao, Daining Fang, and Zhiping Xu

Citation: *Appl. Phys. Lett.* **99**, 041901 (2011); doi: 10.1063/1.3615290
View online: http://dx.doi.org/10.1063/1.3615290
View Table of Contents: http://apl.aip.org/resource/1/APPLAB/v99/i4
Published by the AIP Publishing LLC.

---

## Additional information on Appl. Phys. Lett.
Journal Homepage: http://apl.aip.org/
Journal Information: http://apl.aip.org/about/about_the_journal
Top downloads: http://apl.aip.org/features/most_downloaded
Information for Authors: http://apl.aip.org/authors

---

## ADVERTISEMENT

![](./images/811644053815820289_2.jpg)

# Mechanical and thermal transport properties of graphene with defects
Feng Hao, $^{1}$ Daining Fang, $^{1,2}$ and Zhiping Xu $^{1,3,a)}$
$^{1}$Department of Engineering Mechanics, Tsinghua University, Beijing 100084, China
$^{2}$College of Engineering, Peking University, Beijing 100871, China
$^{3}$Center for Nano and Micro Mechanics, Tsinghua University, Beijing 100084, China

(Received 18 May 2011; accepted 1 July 2011; published online 25 July 2011)

The roles of defects including monatomic vacancies and Stone-Wales dislocations in the mechanical and thermal properties of graphene are investigated here through molecular dynamics (MD) simulations. The results show that Young's modulus of a defected graphene sheet has a gentle dependence with the concentration of defects, while the thermal conductivity is much more sensitive. Analysis based on the effective medium theory (EMT) indicates that this sensitivity originates from the scattering of phonons by defects and delocalized interaction between them, which leads to a transition from propagating to diffusive mode as the concentration increases. © 2011 American Institute of Physics. [doi:10.1063/1.3615290]

Graphene, the extremely monolayer material, attracts intensive research interests recently owing to its outstanding mechanical, thermal, and electronic properties, which are, more interestingly, very sensitive to its microstructures. $^{1}$ For example, the tensile stiffness and strength of graphene sheet are on the order of 1 TPa and 100 GPa, respectively $^{2}$ and the thermal conductivity of monolayer graphene sheet is observed to be $5500 \ \text{W/mK},^{3-5}$ that is one order higher than common engineering materials with high thermal conductivities, such as copper that has a thermal conductivity of 400 W/mK. In contrast to metals where electrons carry most of the heat and define the heat transport processes, the high thermal conductivity of graphene is attributed to phonons. Apparently, the key of these features relies on the structural perfection of the hexagonal graphene lattice and strong in-plane $sp^{2}$ bond between carbon atoms. However, defects unavoidably present in the graphene materials from various synthesis methods and their effects on the mechanical and thermal properties need to be clarified. $^{6-8}$

The experimental techniques to produce graphene sheets can be classified into two categories. In physical methods including both mechanical peeling and chemical vapor deposition, defects such as vacancies and dislocations are widely observed, $^{6-8}$ for example, dislocation concentration as high as 3.6% is observed by atomic resolution transmission electron microscopy image. $^{8}$ In chemical methods such as reduced graphene oxide approach, epoxy groups reside on the graphene basal-plane. $^{9-11}$ Furthermore, under electron irradiation or severe Joule-heating condition, sublimation, evaporation, and doping can lead to considerable defects concentration. $^{12-14}$ Open edges and edge roughness also scatter the heat flux but are only critical for narrow graphene nanoribbons. $^{15}$ In order to evaluate their effects, here we pursue both equilibrium and nonequilibrium molecular dynamics (MD) simulations for some insights of the underlying mechanisms, which will advise fabrications of graphene materials towards specified mechanical and thermal applications.

In our MD simulations, we use the LAMMPS package. $^{16}$ Periodic boundary condition is applied to a square graphene sheet with length $L=6 \ \text{nm}$. The adaptive intermolecular reactive empirical bond-order potential functions and corresponding parameters are used for the interatomic interactions between carbon atoms. $^{17}$ This method is widely used to predict the mechanical and thermal transport properties of graphene materials and their derivatives. In this work, only monatomic vacancies and Stone-Wales (SW) dislocations with varying concentration are considered. The mechanical properties under tensile loads and in-plane thermal conductivities are calculated at a concentration up to the critical value (4%) that leads to structural failure at 300 K, for monatomic vacancies or saturation of Stone-Wales dislocations.

The structure with a certain defect concentration is firstly equilibrated at ambient condition (temperature $T=300 \ \text{K}$ where the quantum correction is negligible, and pressure $P=1 \ \text{atm}$) under a Nosé-Hoover thermostat for 500 ps. In the tensile simulation, a uniaxial load is applied in either the armchair and zigzag direction and the other direction is relaxed to obtain its Young's modulus. In the equilibrium Green-Kubo simulation, the system is subsequently switched to a microcanonical ensemble. The atomic positions and velocities are collected to calculate the thermal flux and its correlation functions. The thermal conductivity is thus obtained by following the Green-Kubo formula and averaging on three samples and two runs for each. In the nonequilibrium Müller-Plathe simulations, the graphene sheet with certain defects concentrations are sandwiched between two pristine graphene sheets of the same sizes. Elastic collisions between the hottest atom in the left and the right "contacts" are forced every 50 fs to produce a thermal flux. To utilize the periodic boundary condition, the sandwich structure is mirrored. $^{18,19}$ This simulation lasts for 5 ns to obtain the spatial pattern of directed thermal flux.

We define the concentration $f$ of monatomic vacancies as the number density of atoms removed from the pristine graphene sheet. For a Stone-Wales dislocation, $f$ is defined by considering two defected atoms. Young's modulus and thermal conductivity of the monolayer graphene sheets are

$^{a)}$Author to whom correspondence should be addressed. Electronic mail:
xuzp@tsinghua.edu.cn.


![](./images/811644053815820289_3.jpg)

FIG. 1. (Color online) (a) Young's modulus and (b) thermal conductivity of a monolayer graphene sheet with monatomic vacancies or Stone-Wales dislocations. Inset in (a): a monatomic vacancy and Stone- Wales defect in graphene as usually encountered in experiments. Numerical fitting and predictions from the Maxwell-Garnett EMT are also plotted for the thermal conductivities in subplot (b). Point defects scatter phonons at a larger scale than the defect size and scatter centers have strong correlation at elevated concentration. These effects are not included in EMT and lead to large deviation from the simulation results.

plotted in Figs. 1(a) and 1(b), where the results at various concentrations are summarized.

For the mechanical properties, it can be seen that Young's moduli $Y$ of defected graphene sheets feature a linear dependence on the defect concentration. Young's modulus $Y_0$ of a defect-free graphene sheet is 1.1 TPa when a thickness of 3.2 nm is used. We plot the relative Young's modulus of defect graphene sheets $Y_{\rm mv}/Y_0$ and $Y_{\rm SW}/Y_0$ in Fig. 1(a). The curve can be fitted into a linear function for monatomic vacancies as $Y_{\rm mv}/Y_0=0.996 - 0.028f$ and a much more smoothly decreasing for Stone-Wales dislocations, which can be explained as that it contains two heptagons and two pentagons, which preserve interatomic $sp^2$ bonding, while monatomic vacancy breaks the integrity of pristine sheet that results in a higher formation energy about $E_{\rm mv}=14$ eV in comparison with the nucleation energy $E_{\rm SW}=6$ eV for the Stone-Wales dislocation. A linear fitting for the Stone-Wales dislocations fails here as is hard to define the concentration.

In contrast to the gentle dependence of Young's modulus, the thermal conductivity $\kappa$, however, is much more sensitive to the presence of these two defects. We can consider the defected graphene sheet as a composite with the pristine graphene lattice as the matrix and defects as inclusions. The overall conductivity of a composite can be estimated by the thermal conductivities of the inclusion and matrix as $\kappa_{\rm comp}^{-1}=\kappa_{\rm inc}^{-1}+\kappa_{\rm mat}^{-1}$. Fitting the simulation results in Fig. 1(b) gives $\kappa_{\rm mv}/\kappa_0=(1.008 + 5.718f)^{-1}$ for monatomic vacancies and $\kappa_{\rm SW}/\kappa_0=(1.001+3.330f)^{-1}$, where $\kappa_0$ is the thermal conductivity of pristine graphene at 300 K. As a result, the thermal conductivity of a pristine monolayer graphene sheet is reduced to its half by introducing monatomic vacancies at a concentration $f_{1/2}=0.175\%$ or Stone-Wales defects at a concentration of $0.3\%$. Using a characteristic size $a=0.14$ nm that is the diameter of one carbon atom in the basal plane of graphene, the prediction from the Maxwell-Garnett formula based effective medium theory (EMT) $\kappa_{\rm EMT}/\kappa_0=(1-f)/(1+0.5f)$ is also plotted in Fig. 1(b), which shows distinct difference with the simulation results. The contradiction suggests that at this length scale of defect, the compatible boundary condition is broken by the strong scattering at the interfaces between pristine graphene lattice and defects. Thus, a question is raised for practical applications that how Maxwell-Garnett formula could be improved.

The thermal conductivity of a solid can be approximately estimated by $\kappa=Cvl/3$, where $C$ is the specific heat, and $v$ is the group speed of sound wave in solid in the spirit of Debye. For graphene $v=(Y/\rho)^{1/2}=21.3$ km/s for longitudinal acoustic (LA) phonons. $l$ is the mean phonon free path that is reported as 775 nm for graphene sheets from experimental measurements that is the origin of their ultrahigh thermal conductivities in combination with the high stiffness.⁵

We calculate the phonon spectrum based on the Fourier transformation of the velocity auto-correlation functions $\langle v(0)v(t)\rangle$ from molecular dynamics simulation.¹⁸ The results show that even at a monatomic vacancy concentration as high as 1%, the shape and peaks are preserved well, which demonstrates that the specific heat $C=k_{\rm B}(\hbar\omega/k_{\rm B}T)^2\exp(\hbar\omega/k_{\rm B}T)/[\exp(\hbar\omega/k_{\rm B}T)-1]^2$ and group velocities $v={\rm d}\omega/{\rm d}k$ for a phonon mode with a frequency $\omega$ and wave vector $k$ have negligible change. A quantitative estimation based on the shift of peaks shows that it only leads to less than 5% reduction of thermal conductivity if the reduction of $l$ is not taken into account.

This result suggests that the presence of defects of low concentration has less effects on the group speed $v$ and specific heat $C$ for the phonons in graphene that is consistent with the gentle reduction of Young's modulus as we observe before. However, the impacts of defects on the thermal conductivity $l_{\rm defect-phonon}$ is dominantly accounted by the mean free path $l^{-1}=l_{\rm defect-phonon}^{-1}+l_{\rm phonon-phonon}^{-1}$ in addition to the phonon-phonon scattering mechanism. Moreover, Fig. 1(b) also shows that when the defect concentration is high enough, $l$ becomes less sensitive in comparison with the situation of low concentration, suggesting a transition from propagating to diffusive mechanism.²⁰ This is also reflected in our further calculations for the temperature dependence of thermal conductivities when 2% monatomic vacancies are introduced. In Fig. 2, it is shown that not only the thermal conductivity $\kappa$ and the temperature dependence is much reduced but also there exists a peak at $T=200$ K, and the low-temperature reduction of $\kappa$ is attributed to scattering of phonons with small wave vectors.¹⁵ Moreover, as $f$ increases, the sensitivity of $\kappa$ on $f$ is much reduced due to the disorder nature of phonon transport processes.

To obtain more insights into the sensitivities of mechanical and thermal properties on the defect concentration, we plot the stress distribution around a monatomic vacancy in Fig. 3(a) and the heat flux in Fig. 3(b). These plots show distinct difference between the stress and heat flux distribution around the defect, i.e., the influence region of stress distribution is much more localized in comparison with the heat flux and significant scattering occurs around the defects.

To predict the effective thermal properties of a nanocomposite, Nan and his collaborators apply the Maxwell-Garnett effective medium theory by introducing a so-called

![](./images/811644053815820289_4.jpg)

FIG. 2. (Color online) Temperature dependence of the thermal conductivities $\kappa/\kappa_0$ of pristine graphene and defected graphene with monatomic vacancies.

Kapitza radius for the interfacial thermal resistance. $^{21}$ This theory is further modified for nanocomposites with spheroi-dal inclusions. $^{22,23}$ However, here it is difficult to define an interface between the defected atoms and others in a pristine hexagonal lattice. To quantitatively characterize this differ-ence, we introduce an influence coefficient $R$ in the Maxwell-Garnett formula instead, i.e.,

$$
\kappa_{\mathrm{eff}}=\kappa_{\mathrm{m}}\left(1+\frac{d(R f) \beta}{1-(R f) \beta}\right), \quad \beta=\frac{\kappa-\kappa_{\mathrm{m}}}{\kappa+(d-1) \kappa_{\mathrm{m}}}, \quad(1)
$$

where $d=3$ is dimension of the problem, and $\kappa_{\text {eff }}, \kappa$, and $\kappa_{\mathrm{m}}$ are the thermal conductivities of the whole defected gra-phene sheet, defects, and the pristine graphene sheet, respec-tively. Our calculations show that $R$ is strongly correlated to the defect concentration $f$, which can be fitted into $R=(0.002+0.011 f)^{-1}$. At low defect concentration, the point defects serve as local scattering centers to the heat flux through them. While at elevated concentrations, the fast decaying of $R$ with respect to increasing $f$ indicates that dif-ferent scattering centers interact with each other, which results in a delocalized scattering to the propagating modes phonons and the overall scattering cross-section is reduced in comparison with discrete and non-interacting defects. When this delocalization is established as the defect concen-tration is high enough, both $R$ and $l$ become less sensitive with respect to that of low concentration.

In summary, we performed molecular dynamics simula-tions for defected graphene sheets. It is found that Young's modulus is reduced with a linear dependence for vacancies and a much more smooth decrease for Stone-Wales dislocations. On the other hand, thermal conductivity relies dramatically on the defect concentration, especially at low concentration. The shortening of phonon mean free path $l$ is responsible for this reduction. At higher defect concentrations, the scattering cen-ters percolates throughout the whole material and the thermal conductivity of defected graphene sheet behaves similarly as in disordered materials, where diffusive modes dominates the thermal transfer process and the temperature dependence is much reduced. These understadings could be used to evaluate the quality of graphene for related applications. Similar phenomena are expected for functionalized or doped graphene sheets, e.g., hydrogenated, oxidized, or fluorinated ones where functional groups behave as the scattering centers as defects do here, that could inspire nanoengineering approaches to tune the mechanical and thermal properties of graphene. $^{11,24}$

![](./images/811644053815820289_5.jpg)

FIG. 3. (Color online) (a) Stress and (b) heat flux distribution in a pristine graphene sheet and around a monatomic vacancy defect.

This work is supported by Tsinghua University through the Key Talent Support Program and the National Science Foundation of China through Young Scholar Grant 11002079 (Z.X.). This work is also supported by the Shanghai Super-computer Center of China.

$^{1}$Z. Xu, Q.-S. Zheng, and G. Chen, Appl. Phys. Lett. 90(22), 223115 (2007).
$^{2}$Z. Xu, J. Comput. Theor. Nanosci. 6(3), 625 (2009).
$^{3}$J. H. Seol et al., Science 328(5975), 213 (2010).
$^{4}$A. A. Balandin et al., Nano Lett. 8(3), 902 (2008).
$^{5}$S. Ghosh et al., Appl. Phys. Lett. 92(15), 151911 (2008).
$^{6}$D. Sen et al., Small 6(10), 1108 (2010).
$^{7}$S. S. Verbridge et al., Appl. Phys. Lett. 93(1), 013101 (2008).
$^{8}$J. Kotakoski et al., Phys. Rev. Lett. 106(10), 105505 (2011).
$^{9}$C. Gómez-Navarro et al., Nano Lett. 10(4), 1144 (2010).
$^{10}$W. Gao et al., Nat. Chem. 1(5), 403 (2009).
$^{11}$Z. Xu and K. Xue, Nanotechnology 21(4), 045704 (2010).
$^{12}$J. Y. Huang et al., Proc. Natl. Acad. Sci. U.S.A. 106(25), 10103 (2009).
$^{13}$J.-W. Jiang, B.-S. Wang, and J.-S. Wang, Appl. Phys. Lett. 98(11), 113114 (2011).
$^{14}$M. Engelund et al., Phys. Rev. Lett. 104(3), 036807 (2010).
$^{15}$D. L. Nika et al., Phys. Rev. B 79(15), 155413 (2009).
$^{16}$S. Plimpton, J. Comp. Phys. 117(1), 1 (1995).
$^{17}$D. W. Brenner et al., J. Phys.: Condens. Matter 14(4), 783 (2002).
$^{18}$Z. Xu and M. J. Buehler, Nanotechnology 20(18), 185701 (2009).
$^{19}$Z. Xu and M. J. Buehler, ACS Nano 3(9), 2767 (2009).
$^{20}$Y. He et al., ACS Nano 5(3), 1839 (2011).
$^{21}$C.-W. Nan et al., Appl. Phys. Lett. 85(16), 3549 (2004).
$^{22}$A. Minnich and G. Chen, Appl. Phys. Lett. 91(7), 073105 (2007).
$^{23}$J. Ordonez-Miranda, R. Yang, and J. J. Alvarado-Gil, Appl. Phys. Lett. 98(23), 233111 (2011).
$^{24}$S.-K. Chien, Y.-T. Yang, and C.-K. Chen, Appl. Phys. Lett. 98(3), 033107 (2011).