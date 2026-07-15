
# A Non-Equilibrium Dissipation Parameter and the Ideal Glass

Jun-Ying Jiang \( ^{①} \) , \( ^{1,*} \)  Liang Gao \( ^{①} \)  \( ^{1,*} \), and Hai-Bin Yu \( ^{①} \)  \( ^{1,†} \) 

 \( ^{1} \) Wuhan National High Magnetic Field Center and School of Physic,

Huazhong University of Science and Technology, Wuhan 430074, Hubei, China

(Dated: September 30, 2025)

Glass materials, as quintessential non-equilibrium systems, exhibit properties such as energy dissipation that are highly sensitive to their preparation histories. A key challenge has been identifying a unified order parameter to rationalize these properties. Here, we demonstrate that a configurational distance metric can effectively collapse energy dissipation data across diverse preparation histories and testing protocols, including varying cooling rates, aging processes, probing times, and the amplitudes of mechanical excitation, as long as the temperature remains above the so-called ideal glass transition (where the extrapolated structural relaxation time diverges). Our results provide a unified description for the non-equilibrium dissipation and suggest that the putative concept of the ideal glass transition is imprinted in material characteristics.

Unlike equilibrium systems, which are stable and time-invariant, non-equilibrium systems exhibit net flows of energy, matter, or information, leading to complex behaviors like aging and memory effects  \( [1-3] \) . Glass is a classic example of a non-equilibrium system. It forms when a liquid is cooled rapidly, preventing it from crystallizing into an ordered, equilibrium state. Instead, atoms or molecules become “frozen” in a disordered, amorphous structure, creating a solid that retains some liquid-like properties  \( [4-11] \) . The defining feature of glass materials is their thermodynamic non-equilibrium state, which makes them highly sensitive to their preparation history. Variations in cooling rates  \( [12, 13] \) , annealing times  \( [14, 15] \) , pressure conditions  \( [16-18] \) , or aging treatments  \( [19-21] \)  can significantly influence the materials’ microscopic structures and macroscopic properties. For example, rapid cooling leads to a higher-energy, more disordered structure, whereas slow cooling allows the material
 

to approach a more stable, lower-energy state  \( [22, 23] \) . Not only does this sensitivity to the preparation history present challenges for the study and application of glass materials, but it also creates opportunities to tune their properties  \( [4, 9, 24, 25] \) .

Although phenomenological models and the “materials time” concept exist, no unified order parameter has been established to characterize the history-dependent properties of amorphous materials. Recently, an order parameter—the inherent structural minimum displacement (IS  \( D_{min} \) , Eq. 1) [26], was proposed to theoretically rationalize the underlying mechanism of relaxation kinetics of various amorphous material systems at equilibrium liquid states.

 \[ \mathrm{I S}D_{\mathrm{m i n}}(t)=[\frac{1}{N}\mathrm{m i n}\sum_{i,j}^{N,N}C_{i j}(t)X_{i j}(t)]^{1/2} \quad (1) \] 

In Eq.1,  \( C_{i,j}(t) = [\vec{r_{i}}(t + t_{0}) - \vec{r_{j}}(t_{0})]^{2} \)  is denoted as the cost matrix, with  \( \vec{r_{i}} \)  is the position of i-th atom, and N is the number of atoms; X is a  \( N \times N \)  boolean matrix, where  \( X[i,j] = 1 \)  if row i is assigned to column j for the minimization of Eq. 1 and otherwise  \( X[i,j] = 0 \) .

This parameter treats all atoms in the system as a whole, assuming exchange symmetry among atoms. The configuration is considered unchanged if atomic position-replacing motions occur. It reduces to the root mean square displacement  \( [27] \)  when X is a unitary matrix under the condition of small displacements (no larger than half interatomic distance). When coarse-graining is applied, it becomes the overlap function of Parisi  \( [28, 29] \) . The solution of Eq.1 has been obtained by the Hungarian algorithm  \( [30] \) .

Previous work has shown a power-law scaling relationship between the relaxation dissipation of disordered materials (characterized by internal dissipation  \( \delta \) ) and IS  \( D_{min} \) , indicating that the relaxation dissipation of liquids can be revealed across different materials and time scales. However, these findings were limited to steady-state liquids and did not explore its applicability to non-equilibrium glassy states [26]. Extending this parameter to non-equilibrium regimes could provide a unified framework to characterize aging, memory, and preparation-history-dependent effects in glasses.

Moreover, the non-equilibrium glassy state invites a long-standing question about the so-called ideal glass transition and ideal glass state. The ideal glass transition refers to a pure thermodynamic ideal phase transition that occurs when a supercooled liquid is cooled to the Kauzmann temperature  \( (T_{K}) \) , where the extrapolated entropy of the liquid equals
 
![](./images/1179759838075289606_1.jpg)

(c)

![](./images/1179759838075289606_2.jpg)

(b)

![](./images/1179759838075289606_3.jpg)

(d)

![](./images/1179759838075289606_4.jpg)

FIG. 1. Dynamic mechanical response of the Kob-Andersen model obtained from MD-DMS simulations at different cooling rates. (a) for Storage shear modulus  \( G' \) , (b) for loss shear modulus  \( G'' \) , (c) for phase angle  \( \delta \) , and (d) for IS  \( D_{min} \) .

that of the crystal, eliminating kinetic effects. In many cases, the Kauzmann temperature is demonstrated to be the temperature at which the viscosity diverges  \( (T_{0}) \) , i.e.,  \( T_{K} = T_{0} \)  [31].

The concept of ideal glass transition is considered as a rescue of the 3rd thermodynamic law in liquid science. However, as the liquid becomes very slow in dynamics, no real experiments can probe it. There have been substantial discussions and debates around it  \( [32, 33] \) . Whether such a thermodynamic limit exists, and whether it can be captured by an appropriate structural or dynamical order parameter, remains one of the key challenges in glass physics.

Several attempts have been conducted to verify the existence of  \( T_{0} \)  or the ideal glass state [34–36]. For example, Ozawa et al. [37] conducted a computer simulation study on the thermodynamic and kinetic characteristics of the glass morphology that undergoes ideal glass transition due to randomly fixed particles. They discovered that even in the state of deep equilibrium, the particles would explore multiple inherent structures (IS) within the local minimum of free energy.
 
![](./images/1179759838075289606_5.jpg)

(c)

![](./images/1179759838075289606_6.jpg)

(b)

![](./images/1179759838075289606_7.jpg)

(d)

![](./images/1179759838075289606_8.jpg)

FIG. 2. Strain amplitude influence on dynamics of Kob-Andersen model. (a) for Storage shear modulus  \( G' \) , (b) for loss shear modulus  \( G'' \) , (c) for phase angle  \( \delta \) , and (d) for IS  \( D_{min} \) . This model glass is cooled with a cooling rate of 0.1 in LJ unit.

So far, no unified order parameter has been proposed to describe its characteristics. The concept of local IS clusters within minima aligns directly with the structural metric IS  \( D_{min} \) , which quantifies inherent differences in precisely such local configuration basins. IS  \( D_{min} \)  thus offers a natural framework to characterize the structural heterogeneity governing partial relaxation near arrest.

This study aims to validate whether the order parameter IS  \( D_{min} \)  can describe the relaxation-dissipation behavior of non-equilibrium glasses and what happens around  \( T_{0} \) . Our results show that IS  \( D_{min} \)  is related to the loss phase angle when the temperature is kept above the ideal glass transition, including different cooling rates, aging processes, probing times, and mechanical excitations. In contrast, below the ideal glass transition temperature, IS  \( D_{min} \)  decouples from the phase angle without direct correlation. These findings not only provide a much-needed order parameter for characterizing non-equilibrium dissipation but also lend substantial support to the concept of ideal glass.

As a typical example, we study the Kob-Andersen binary Lennard-Jones (LJ) mixture, consisting 80% large A particles and 20% small B particles [38, 39]. In this mixture, all par-
 

ticles have the same mass and interact via LJ pair potentials  \( v(r)=4\varepsilon\left[(r/\sigma)^{-12}-(r/\sigma)^{-6}\right] \) , truncated and shifted to zero at  \( 2.5\sigma \) . The interaction parameters are  \( \sigma_{BB}/\sigma_{AA}=0.88 \) ,  \( \sigma_{AB}/\sigma_{AA}=0.8 \) ,  \( \varepsilon_{BB}/\varepsilon_{AA}=0.5 \) , and  \( \varepsilon_{AB}/\varepsilon_{AA}=1.5 \) . All quantities are in the LJ units: length in units of  \( \sigma_{AA} \) , temperature in units of  \( {\sigma_{AA}}/{k_{\mathrm{B}}} \) , time in the units of  \( \sqrt{m\sigma_{AA}^{2}/\varepsilon_{AA}} \) , pressure and modulus in the units of  \( \sigma_{AA}^{3}/\varepsilon_{AA} \) . We kept the number of density N/V=1.2. This model has good glass-forming ability and enables us to study equilibrium supercooled liquids, and glasses with cooling rates ranging from  \( 10^{4} \)  to  \( 10^{-1} \)  in LJ units (the functional relationship between temperature and potential energy is shown in FIG. S1).

Using molecular dynamics simulations of dynamic mechanical spectra (MD-DMS) in LAMMPS  \( [40, 41] \) , we explore the relaxation-dissipation behaviors in both equilibrium liquids and non-equilibrium glasses  \( [42–45] \) . In MD-DMS, a sinusoidal shear strain is applied with an oscillation period  \( t_{\omega} \)  (related to frequency  \( f = 1/t_{\omega} \) ) and a strain amplitude  \( \varepsilon_{A} \) . The resulting stress  \( \sigma(t) \)  and the phase difference  \( \delta \)  between stress and strain are measured and adapted by  \( \sigma(t) = \sigma_{0} + \sigma_{A}\sin(2\pi t/t_{\omega} + \delta) \) . The storage and loss moduli are calculated by  \( G' = \sigma_{A}/\varepsilon_{A}\cos(\delta) \)  and  \( G'' = \sigma_{A}/\varepsilon_{A}\sin(\delta) \) , respectively.

We determine the  \( \alpha \)  relaxation time  \( \tau_{\alpha} \)  and the characteristic period  \( t_{w} \)  from the peak time of the isothermal and equilibrium MD-DMS (see FIG. S2). Afterwards, these data can be well fitted by a Vogel-Fulcher-Tammann (VFT) function [20, 46],  \( \tau_{\alpha} = \tau_{0} \exp(DT_{0}/(T - T_{0})) \) , with a divergent temperature  \( T_{0} = 0.27 \)  (FIG. S3). This temperature has been considered the ideal glass transition temperature; below which, if the liquid could be equilibrated, it would enter an ideal glass phase.

Figure 1 shows typical relaxation dynamics data for varied cooling rates, with a single probing time of  \( t_{w} = 1000 \)  in LJ time unit. At temperatures below 0.45, the system exhibits characteristic non-equilibrium behaviors. With decreasing cooling rate, the storage modulus  \( G' \)  increases, while the loss modulus  \( G'' \)  and the phase angle  \( \delta \)  decrease. Specifically, the variation of  \( \delta \) , can be up to 10 times at lower temperatures, particularly for T < 0.35. In FIG. 1(d), we also present the IS  \( D_{min} \)  during the MD-DMS. Similarly as in (c), these values exhibit a clear dependence on the cooling rate, with slower cooling resulting in smaller  \( D_{min} \) .

In addition, we have explored non-equilibrium dynamics under various conditions, including strain amplitude (FIG. 2), equilibrium isothermal (by varying the probing  \( t_{w} \) , FIG. S4), aging (FIG. S5), and heating rate (FIG. S6). For example, as shown in FIG. 2, increasing the strain amplitude for MD-DMS leads to higher values of both  \( \delta \)  and IS  \( D_{min} \) , and shifts the
 
![](./images/1179759838075289606_9.jpg)

![](./images/1179759838075289606_10.jpg)

FIG. 3. Correlation between phase angle  \( \delta \)  and IS  \( D_{min} \)  in the Kob–Andersen model at temperatures (a) above and (b) below  \( T_{0} \)  ( \( \sim 0.27 \) ). The legend entries correspond to different simulation protocols: ‘cooling rate’ represents samples prepared under different cooling rates (FIG. 1); ‘isothermal’ refers to samples equilibrated at fixed temperatures (FIG. S4); ‘aging’ indicates samples aged at various temperatures after quenching (FIG. S5); ‘periodic time’ denotes the various time intervals in MD-DMS at the slowest cooling rate (FIG. S2); ‘strain amplitude’ refers to different amplitudes of applied strain in MD-DMS (FIG. 2); and ‘heating rate’ represents samples subjected to varying heating rates (FIG. S6). Comparative results of  \( \delta \)  and IS  \( D_{min} \)  across all conditions are shown in FIG. S7.

α-relaxation to lower temperatures. These observations highlight characteristic non-linear and non-equilibrium behaviors.

Figures 3(a) and 3(b) plot  \( \delta \)  against IS  \( D_{min} \)  in the Kob–Andersen model for temperatures above and below  \( T_{0} \) , respectively. We find, in FIG. 3(a), the data  \( T > T_{0} \)  are well correlated. A power-law fit using Eq. 2 yields an exponent of  \( b = 2.02 \pm 0.03 \) .

 \[ \delta\propto(\mathrm{IS}D_{\min})^{b} \quad (2) \]
 

These results illustrate that the non-equilibrium dissipation at  \( T > T_{0} \)  can be uniquely determined by IS  \( D_{min} \) , consistent with our previous findings on equilibrium dynamics. Remarkably, we now find that all the dissipation data, including those from non-equilibrium glasses, equilibrium supercooled liquids, and strain-driven non-linear data, follow this relation.

![](./images/1179759838075289606_11.jpg)

![](./images/1179759838075289606_12.jpg)

![](./images/1179759838075289606_13.jpg)

![](./images/1179759838075289606_14.jpg)

![](./images/1179759838075289606_15.jpg)

FIG. 4. Identical correlation between the phase  \( \delta \)  (rad) and IS  \( D_{min} \)  ( \( \mathring{A} \) ) for (a)  \( Ni_{65}Nb_{35} \) , (b)  \( Ni_{80}P_{20} \) , (c)  \( Cu_{50}Zr_{50} \)  and (d)  \( Al_{90}Sm_{10} \)  models, which have  \( T_{0} \)  of 490 K, 390 K, 540 K, and 480 K, respectively. The corresponding details are provided in FIGs. S8-S14, respectively.

On the other hand, the data are scattered at  \( T < T_{0} \)  in FIG. 3(b), and  \( \delta \)  and IS  \( D_{min} \)  are no longer correlated in a united manner. It is intriguing that  \( T_{0} \)  defines the temperature range where Eq. 2 holds. This implies that  \( T_{0} \)  might indeed be a relevant temperature for non-equilibrium glass states.

Our results are not limited to the Kob-Andersen models; we have also verified that the main findings apply to metallic glass models with many body interactions. As shown in Figure 4, the same conclusions as in Figure 3 are obtained for the (a)  \( Ni_{65}Nb_{35} \)  [47], (b)  \( Ni_{80}P_{20} \) , (c)  \( Cu_{50}Zr_{50} \) , and (d)  \( Al_{90}Sm_{10} \)  models (data for these models were sourced from [7]). Additional details on these metallic glass models are provided in Supplementary Material.

Why is the order parameter IS  \( D_{min} \)  effective for describing non-equilibrium dissipation when  \( T > T_{0} \) ? One plausible explanation involves the potential energy landscape (PEL) [48–51], which is a potential energy function of an N-body system,  \( \Phi(r_{1}, r_{2}, \ldots, r_{N}) \) . Here, the vectors  \( r_{i} \)  include position, orientation, and intermolecular coordinates. For example,
 

for a system of N identical atoms, this landscape is a  \( (3N + 1) \) -dimensional object. As schematically shown in FIG. 5, IS  \( D_{min} \)  characterizes the shortest distance between two local energy minima (inherent structures).

![](./images/1179759838075289606_16.jpg)

FIG. 5. A schematic of potential energy landscape (PEL) illustrates the process of dissipation relaxation. At temperatures above the  \( T_{g} \) , the structural energy barriers are sufficiently low, allowing the system to undergo frequent structural transformations. In the intermediate temperature range,  \( T_{0} < T < T_{g} \) , the system can across barriers. When the temperature falls below  \( T_{0} \) , the energy barriers become so high that structural rearrangements are essentially suppressed.

Previous work has shown that the power-law scaling in Eq. 2 results from activation between different local minima with distinct configurations [26]. Given that energy dissipation is associated with activation, and assuming the energy barrier is harmonic, one obtains  \( \delta \propto (\mathrm{IS} D_{\mathrm{min}})^{2} \) . However, Eq. 2 with a power b > 2 suggests that the activation barrier is not purely harmonic. Instead, b characterizes the local curvature of the PEL.

The breakdown of Eq. 2 at  \( T < T_{0} \)  may be due to high energy barriers and insufficient thermal energy for activation. This suggests that dissipation at  \( T < T_{0} \)  is primarily due to other motions rather than the configurational changes captured by IS  \( D_{min} \) . Atomic vibrations are one such motion, quasi-localized vibrations are dissipative but would not change the IS  \( D_{min} \) . For example, the so-called Boson peak could yield substantial dissipation in the low temperature range [52]. Additionally, liquid-like clusters that are dissipative but non-diffusive have recently been identified as the source of low-temperature  \( \gamma \)  relaxation in
 

glasses. These arguments imply that relaxation dissipation at low temperatures is different from the normal glass  \( (T > T_{0}) \) . These arguments are consistent with the prevalent view that the glass have a PEL dominated temperature range.

To summarize, this work proposes the order parameter IS  \( D_{min} \)  as a universal descriptor of non-equilibrium dissipation in glassy materials. Specifically, the ideal glass transition temperature  \( T_{0} \)  emerges as a fundamental threshold: dissipation follows a power-law scaling with IS  \( D_{min} \)  for  \( T > T_{0} \)  through activation over PEL barriers; while below  \( T_{0} \) , this relationship breaks down as dissipation shifts to non-configurational mechanisms. Our findings provide a fundamental framework for understanding and predicting dissipation mechanisms in glassy materials.

## ACKNOWLEDGMENTS

The computational work was carried out on the public computing service platform provided by the Network and Computing Center of HUST. We are thankful for the support of the National Science Foundation of China (52071147).

[1] D. Tapias, C. Marteau, F. Aguirre-López, and P. Sollich, Bringing together two paradigms of nonequilibrium: Fragile versus robust aging in driven glassy systems, Phys. Rev. Lett. 133, 197101 (2024).

[2] M. Baity-Jesi, E. Calore, A. Cruz, L. A. Fernandez, J. M. Gil-Narvion, I. Gonzalez-Adalid Pemartin, A. Gordillo-Guerrero, D. Iñiguez, A. Maiorano, E. Marinari, V. Martin-Mayor, J. Moreno-Gordo, A. Muñoz Sudupe, D. Navarro, I. Paga, G. Parisi, S. Perez-Gaviro, F. Ricci-Tersenghi, J. J. Ruiz-Lorenzo, S. F. Schifano, B. Seoane, A. Tarancon, and D. Yllanes, Memory and rejuvenation effects in spin glasses are governed by more than one length scale, Nat. Phys. 19, 978 (2023).

[3] C. Scalliet and L. Berthier, Rejuvenation and memory effects in a structural glass, Phys. Rev. Lett. 122, 255502 (2019).

[4] V. Bapst, T. Keck, A. Grabska-Barwińska, C. Donner, E. D. Cubuk, S. S. Schoenholz, A. Obika, A. W. R. Nelson, T. Back, D. Hassabis, and P. Kohli, Unveiling the predictive
 

power of static structure in glassy systems, Nat. Phys. 16, 448 (2020).

[5] H. Tanaka, H. Tong, R. Shi, and J. Russo, Revealing key structural features hidden in liquids and glasses, Nat. Rev. Phys. 1, 333 (2019).

[6] S. Ishino, Y.-C. Hu, and H. Tanaka, Microscopic structural origin of slow dynamics in glass-forming liquids, Nat. Mater. 24, 268 (2025).

[7] L. Gao, H.-B. Yu, T. B. Schröder, and J. C. Dyre, Unified percolation scenario for the  \( \alpha \)  and  \( \beta \)  processes in simple glass formers, Nat. Phys. 21, 471 (2025).

[8] M. Frey, N. Neuber, S. S. Riegler, A. Cornet, Y. Chushkin, F. Zontone, L. M. Ruschel, B. Adam, M. Nabahat, F. Yang, J. Shen, F. Westermmeier, M. Sprung, D. Cangialosi, V. Di Lisio, I. Gallino, R. Busch, B. Ruta, and E. Pineda, Liquid-like versus stress-driven dynamics in a metallic glass former observed by temperature scanning X-ray photon correlation spectroscopy, Nat. Commun. 16, 4429 (2025).

[9] L. Berthier and G. Biroli, Theoretical perspective on the glass transition and amorphous materials, Rev. Mod. Phys. 83, 587 (2011).

[10] J. C. Dyre, Solid-that-flows: Picture of glass-forming liquids, J. Phys. Chem. Lett. 15, 1603 (2024).

[11] P. Lunkenheimer, A. Loidl, B. Riechers, A. Zaccone, and K. Samwer, Thermal expansion and the glass transition, Nat. Phys. 19, 694 (2023).

[12] D. Granata, E. Fischer, V. Wessels, and J. Löffler, Fluxing of Pd-Si-Cu bulk metallic glass and the role of cooling rate and purification, Acta Mater. 71, 145 (2014).

[13] A. Atila, S. V. Sukhomlinov, M. J. Honecker, and M. H. Müser, Plasticity of metallic glasses dictated by their state at the fragile-to-strong transition temperature, Acta Mater. 286, 120753 (2025).

[14] J. E. Schawe and J. F. Löffler, Kinetics of structure formation in the vicinity of the glass transition, Acta Materialia 226, 117630 (2022).

[15] M. W. Da Silva Pinto, L. Daum, H. Rösner, and G. Wilde, Correlations between shadow glass transition, enthalpy recovery and medium range order in a  \( Pd_{40}Ni_{40}P_{20} \)  bulk metallic glass, Acta Mater. 275, 120034 (2024).

[16] F. Spieckermann, D. Šopu, V. Soprunyuk, M. B. Kerber, J. Bednarcík, A. Schökel, A. Rezvan, S. Ketov, B. Sarac, E. Schafler, and J. Eckert, Structure-dynamics relationships in cryogenically deformed bulk metallic glass, Nat. Commun. 13, 127 (2022).
 

[17] T. Böhmer, J. P. Gabriel, L. Costigliola, J.-N. Kociok, T. Hecksher, J. C. Dyre, and T. Blochowicz, Time reversibility during the ageing of materials, Nat. Phys. 20, 637 (2024).

[18] P. Saini, Y. Zhao, B. Li, L. Zhang, U. Ramamurty, and R. Narayan, Temperature dependence of pressure sensitive flow in bulk metallic glass composites, J. Mater. Sci. Technol. 181, 165 (2024).

[19] M. Lüttich, V. M. Giordano, S. Le Floch, E. Pineda, F. Zontone, Y. Luo, K. Samwer, and B. Ruta, Anti-aging in ultrastable metallic glasses, Phys. Rev. Lett. 120, 135504 (2018).

[20] L. Wang, N. Xu, W. H. Wang, and P. Guan, Revealing the link between structural relaxation and dynamic heterogeneity in glass-forming liquids, Phys. Rev. Lett. 120, 125502 (2018).

[21] W. Peter G., Spatiotemporal structures in aging and rejuvenating glasses, Proc. Nat. Acad. Sci. 106, 1353 (2009).

[22] J. E. K. Schawe and J. F. Löffler, Existence of multiple critical cooling rates which generate different types of monolithic metallic glass, Nat. Commun. 10, 1337 (2019).

[23] A. L. Greer, New horizons for glass formation and stability, Nat. Mater. 14, 542 (2015).

[24] Y. D. Cheng, Q. Yang, J. J. Wang, T. Dimitriadis, M. Schumacher, H. R. Zhang, M. J. Müller, N. Amini, F. Yang, A. Schoekel, J. Pries, R. Mazzarello, M. Wuttig, H.-B. Yu, and S. Wei, Highly tunable  \( \beta \) -relaxation enables the tailoring of crystallization in phase-change materials, Nat. Commun. 13, 7352 (2022).

[25] E. Lázaro-Lázaro, J. A. Perera-Burgos, P. Laermann, T. Sentjabrskaja, G. Pérez-Ángel, M. Laurati, S. U. Egelhaaf, M. Medina-Noyola, T. Voigtmann, R. Castañeda-Priego, and L. F. Elizondo-Aguilera, Glassy dynamics in asymmetric binary mixtures of hard spheres, Phys. Rev. E 99, 42603 (2019).

[26] H.-B. Yu, L. Gao, J.-Q. Gao, and K. Samwer, Universal origin of glassy relaxation as recognized by configuration pattern matching, Natl. Sci. Rev. 11, nwae091 (2024).

[27] Z.-Y. Zhou, Y. Sun, L. Gao, Y.-J. Wang, and H.-B. Yu, Fundamental links between shear transformation,  \( \beta \)  relaxation, and string-like motion in metallic glasses, Acta Mater. 246, 118701 (2023).

[28] G. Parisi, Order parameter for spin-glasses, Phys. Rev. Lett. 50, 1946 (1983).

[29] B. Guiselin, G. Tarjus, and L. Berthier, On the overlap between configurations in glassy liquids, J. Chem. Phys. 153, 224502 (2020).

[30] D. F. Crouse, On implementing 2D rectangular assignment algorithms, IEEE Trans. Aerosp.
 

Electron. Syst. 52, 1679 (2016).

[31] H. Tanaka, Relation between thermodynamics and kinetics of glass-forming liquids, Phys. Rev. Lett. 90, 055701 (2003).

[32] T. Hecksher, A. I. Nielsen, N. B. Olsen, and J. C. Dyre, Little evidence for dynamic divergences in ultraviscous molecular liquids, Nat. Phys. 4, 737 (2008).

[33] M. Adhikari, S. Karmakar, and S. Sastry, Dependence of the glass transition and jamming densities on spatial dimension, Phys. Rev. Lett. 131, 168202 (2023).

[34] H. Yoon and G. B. McKenna, Testing the paradigm of an ideal glass transition: Dynamics of an ultrastable polymeric glass, Sci. Adv. 4, eaau5423 (2018).

[35] X. Monnier, J. Colmenero, M. Wolf, and D. Cangialosi, Reaching the ideal glass in polymer spheres: Thermodynamics and vibrational density of states, Phys. Rev. Lett. 126, 118004 (2021).

[36] C. Cammarota and G. Biroli, Ideal glass transitions by random pinning, Proc. Nat. Acad. Sci. 109, 8850 (2012).

[37] M. Ozawa, A. Ikeda, K. Miyazaki, and W. Kob, Ideal glass states are not purely vibrational: Insight from randomly pinned glasses, Phys. Rev. Lett. 121, 205501 (2018).

[38] W. Kob and H. C. Andersen, Kinetic lattice-gas model of cage effects in high-density liquids and a test of mode-coupling theory of the ideal-glass transition, Phys. Rev. E 48, 4364 (1993).

[39] R. S. L. Stein and H. C. Andersen, Scaling analysis of dynamic heterogeneity in a supercooled lennard-jones liquid, Phys. Rev. Lett. 101, 267802 (2008).

[40] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton, Lammps - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Comput. Phys. Commun. 271, 108171 (2022).

[41] W. M. Brown and M. Yamada, Implementing molecular dynamics on hybrid high performance computers—three-body potentials, Comput. Phys. Commun. 184, 2785 (2013).

[42] G.-J. Lyu, J.-C. Qiao, Y. Yao, Y.-J. Wang, J. Morthomas, C. Fusco, and D. Rodney, Microstructural effects on the dynamical relaxation of glasses and glass composites: A molecular dynamics study, Acta Mater. 220, 117293 (2021).

[43] H.-B. Yu, R. Richert, and K. Samwer, Structural rearrangements governing johari-goldstein
 

relaxations in metallic glasses, Sci. Adv. 3, e1701577 (2017).

[44] L. Zella, J. Moon, D. Keffer, and T. Egami, Transient nature of fast relaxation in metallic glass, Acta Mater. 239, 118254 (2022).

[45] J. F. Douglas, Q.-L. Yuan, J. Zhang, H. Zhang, and W.-S. Xu, A dynamical system approach to relaxation in glass-forming liquids, Soft Matter 20, 9140 (2024).

[46] K. Ngai, Universal properties of relaxation and diffusion in complex materials: Originating from fundamental physics with rich applications, Prog. Mater Sci. 139, 101130 (2023).

[47] Y. Zhang, R. Ashcraft, M. Mendelev, C. Z. Wang, and K. F. Kelton, Experimental and molecular dynamics simulation study of structure of liquid and amorphous  \( Ni_{62}Nb_{38} \)  alloy, J. Chem. Phys. 145, 204505 (2016).

[48] K. Shiraishi, H. Mizuno, and A. Ikeda, Johari-goldstein  \( \beta \)  relaxation in glassy dynamics originates from two-scale energy landscape, Proc. Natl. Acad. Sci. 120, e2215153120 (2023).

[49] J. Ding, Y. Q. Cheng, H. Sheng, M. Asta, R. O. Ritchie, and E. Ma, Universal structural parameter to quantitatively predict metallic glass properties, Nat. Commun. 7, 13733 (2016).

[50] L. Zella, J. Moon, and T. Egami, Ripples in the bottom of the potential energy landscape of metallic glass, Nat. Commun. 15, 1358 (2024).

[51] Y. Fan, T. Iwashita, and T. Egami, Energy landscape-driven non-equilibrium evolution of inherent structure in disordered material, Nat. Commun. 8, 15417 (2017).

[52] Y. Hara, R. Matsuoka, H. Ebata, D. Mizuno, and A. Ikeda, A link between anomalous viscous loss and the boson peak in soft jammed solids, Nat. Phys. 21, 262 (2025).
 
