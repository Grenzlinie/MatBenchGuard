
# Transport phenomena in a free-standing two-dimensional sodium sheet

Ajit Jena \( ^{*} \)  and Wu Li

Institute for Advanced Study, Shenzhen University, Shenzhen 518060, China

(Dated: August 8, 2019)

The advances in the growth techniques provide numerous scope to explore the possibilities of new 2D materials for potential applications. With the aid of first-principle calculations we show that 2D Na can be a new addition to the family of thermodynamically stable 2D materials for device applications. Not surprisingly, due to half-occupied 3s orbital 2D Na possesses the features of the 2D electron gas (2DEG). The transport properties are examined based on the accurate solution of Boltzmann transport equation. With practically tunable carrier density in 2D materials, the intrinsic electrical resistivity of electron doped 2D Na is  \( \sim1.4 \)  times larger than that of graphene and falls below the latter 450 K onwards. The Bloch-Grüneisen temperature is almost constant at 50 K, independent of the type or density of the charge carriers. The electronic thermal conductivity of pure 2D Na is  \( \sim1.24 \)  times larger than that of its bulk counterpart at 300 K. The Wiedemann-Franz law stands tall in 2D Na with calculated Lorenz number  \( 2.41\times10^{-8}V^{2}/deg^{2} \)  at room temperature. The transport mechanism presented here is expected to occur in all Na like systems with a clean Fermi surface.

Keywords: 2D Na, 2DEG, Bloch-Grüneisen temperature, electron-phonon coupling, intrinsic electrical resistivity, Lorenz number

## I. INTRODUCTION

Two-dimensional (2D) materials have attracted considerable attention in the scientific community owing to their exceptional properties and promising applications. In this regard, graphene is at the forefront which has extremely large thermal conductivity and high mobile charge carriers having the dispersion curves similar to Dirac fermions with zero rest mass  \( [1-4] \) . In addition to graphene the other 2D materials which also receive interest for new-generation electronic and spintronic devices include hexagonal boron nitride and members of the transition-metal chalcogenides such as molybdenum disulfide and tungsten diselenide  \( [5-7] \) . There are also large number of literature which report the formation of 2D structures on a substrate or inside a material. For example, via scanning tunneling microscopy the existence of K islands ( \( \sim 5 - 500 \)  nm) is found on graphite surface  \( [8] \) . Superconductivity in one atomic layer metal film has been observed when Pb and In are grown epitaxially on Si(111) substrate  \( [9] \) . The fabrication of 2D crystalline layer of transition metal Hf on Ir(111) is also reported  \( [10] \) . A single atomic thick layer of Fe membrane is found to be suspended in graphene pores  \( [11] \) . In this context, theoretical work also predicts that Ag, Au and Cu can be the stable 2D materials  \( [12-14] \) . The recent development of advanced growth techniques overcomes the challenge of identifying the new and potentially rewarding 2D materials which include phosphorene  \( [15, 16] \)  and materials for 2D ferromagnetic  \( [17-19] \) .

Motivated by the intriguing physical properties of sodium and transition metal based layered oxides, we discuss the transport phenomena in a suspended sodium sheet. Sodium and transition metal based layered oxide,  \( Na_{x}CO_{2} \) , offers a wide range of physical phenomena with different Na concentrations. For examples,  \( Na_{x}CoO_{2} \)  shows interesting metal-insulator phase diagram, superconductivity is induced in  \( Na_{0.35}CoO_{2} \)  when it is intercalated with water and  \( Na_{x}Co_{2}O_{4} \)  is found to be a high thermoelectric power material [20–22]. All the above features make this hexagonal layered system an exciting transition metal oxide in which Na atoms lie in a plane. This encourages us to investigate the transport mechanism of a free-standing 2D Na. In a recent theoretical work, Nevalaita and Koskinen [23] have studied 45 atomically thin elemental 2D metal films in hexagonal, square, and honeycomb lattice structures. They have predicted that 2D Na is mechanically stable in hexagonal and honeycomb lattices while unstable in the square lattice system. Since 2D Na is stable in the hexagonal lattice system we consider the same lattice type in the present study. In addition to Na we have also examined the dynamical stability (see the supplementary information) of Li, Be, Mg, Al and K which are reported to be mechanically stable 2D elements [23]. However, we find that 2D Li and 2D Al have imaginary vibrational frequency in the phonon dispersion calculation (see the supplementary information). The absence of imaginary frequency in phonon dispersion and the energy evolution obtained from molecular dynamics (MD) run, shown in Fig. 1, suggest the thermodynamical stability of 2D Na.

In 2D metal, the carrier dynamics originating from electron-phonon (e-ph) interactions is characterized by Bloch-Grüneisen temperature,  \( \Theta_{BG} \) .  \( \Theta_{B} \)  is defined as  \( 2\hbar k_{F}v_{s}/\kappa_{B} \) , where  \( \hbar \) ,  \( k_{F} \) ,  \( v_{s} \)  and  \( \kappa_{B} \)  are respectively the reduced Planck constant, Fermi wavevector, sound velocity and the Boltzmann constant.  \( \Theta_{BG} \)  is the temperature at which the resistivity starts deviating from the linear
 

T behavior. Below  \( \Theta_{BG} \)  the intrinsic electrical resistivity  \( (\rho_{e-ph}) \)  varies as  \( T^{4} \)  while  \( \rho_{e-ph} \)  is proportional to T above  \( \Theta_{BG} \)  [24]. Efetov and Kim have shown that  \( \Theta_{BG} \)  in graphene can be tuned up to  \( \sim1000 \)  K with high carrier density  \( (n=4\times10^{14}\mathrm{~cm}^{-2}) \)  by applying gate voltage [25]. However, the effect of external carrier density on  \( \rho_{e-ph} \)  in graphene is very negligible [25, 26]. The scenario is significantly different in borophene, 2D B, where  \( \rho_{e-ph} \)  is highly sensitive to the charge doping and  \( \Theta_{BG} \)  is almost constant at 100 K [27]. In a very recent article Liu et al. have shown that Bloch-Grüneisen theory is not applicable to  \( \beta_{12} \)  and  \( \gamma_{3} \)  allotropes of borophene [28]. We note that, in the present discussion,  \( \Theta_{BG} \)  in borophene refers to the temperature at which the resistivity starts showing non-linear T dependence on cooling. With electron and hole doping in 2D Na we show that  \( \Theta_{BG} \)  is nearly pinned at 50 K and with electron doping  \( \rho_{e-ph} \)  can be lower than that of graphene at high temperature (450 K onwards). The predicted results on the thermal transport in 2D Na are also promising when comparing with its bulk counterpart. We believe that 2D Na can be a new addition to the family of 2D materials for electronic and thermopower applications. The transport mechanism explained here is expected to be a prototype for the systems with clean Fermi surface and the work can also be useful to understand the transport phenomena in systems having a plane of Na atoms.

## II. COMPUTATIONAL METHODOLOGY

Boltzmann Transport Equation (BTE) is known to describe well the electrical and thermal transport in insulators, semiconductors and metals  \( [29–34] \) . We solve BTE accurately  \( [33] \)  where the key component is the calculation of e-ph coupling matrix elements. We employ pseudo-potential based density-functional theory (DFT) and density-functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO  \( [35] \)  within the framework of general gradient approximation (GGA) to compute the electron energies, vibrational frequencies and e-ph matrix elements. The matrix elements are calculated first on a coarse grid of  \( 8 \times 8 \times 1 \)  and then Wannier interpolated into a fine grid of  \( 200 \times 200 \times 1 \)  using electron-phonon Wannier (EPW) package  \( [34] \) . The calculations are performed using norm-conserving pseudo-potential and the kinetic energy cutoff for the planewave is taken as 60 Ry. The electronic integration over the Brillouin zone is approximated by the Gaussian smearing of 0.025 Ry for the self-consistent calculations. A single atom of Na is considered in the hexagonal lattice system (a = 3.66 Å) and the Na sheets are sufficiently isolated from each other by 10 Å of vacuum to ensure the negligible interlayer interaction. To carry out the MD simulation a supercell of  \( 4 \times 4 \times 1 \)  is used.

(a)

![](./images/867766869136769670_1.jpg)

(b)

![](./images/867766869136769670_2.jpg)

FIG. 1. (a) Phonon dispersion relation of optimized 2D Na along the high symmetry-lines of hexagonal lattice. (b) The room temperature energy evolution of 2D Na during MD simulation.

## III. RESULTS AND DISCUSSIONS

Before we analyze the transport properties we present the phonon dispersion of 2D Na in Fig. 1(a). The absence of imaginary frequency in the dispersion curve suggests its structural stability and thereby indicates that the experimental growth of the same can be plausible. The structural stability is further confirmed by the MD simulation carried out at 300 K. The change in the total energy is only within 2 meV (see Fig. 1(b)) over the time steps. The phonon dispersion of this suspended sodium sheet comprises an out-of-plane (ZA) and two in-plane (LA and TA) modes. While the in-plane modes obey the normal linear dispersion around the  \( \Gamma \) -point the soft ZA mode shows  \( q^{2} \)  frequency dispersion, typical in 2D materials, which is a consequence of  \( D_{6h} \)  point group [36]. As it can be seen from Fig. 1(a) the highest phonon energy ( \( \sim 130~cm^{-1} \) ) in 2D Na is significantly lower than (by  \( \sim 1 \)  order) that of graphene and borophene [27, 28, 37]. We note that the highest phonon energy in bulk Na [38, 39] is of similar magnitude to that of 2D Na. Therefore, the Debye temperature ( \( \Theta_{D} \) ) is lower in bulk Na as compared to B and C [40, 41].  \( \Theta_{D} \)  is the temperature that corresponds to the highest normal mode of vibration in crystal.  \( \Theta_{D} \)  in bulk systems is equivalent to  \( \Theta_{BG} \)  in 2D, systems with low electron density, while describing  \( \rho_{e-ph} \) . The high temperature behavior of  \( \rho_{c-ph} \)  in typical conductors (3D) is same as in 2D ( \( \propto T \) ). However,  \( \rho_{c-ph} \)  varies as  \( T^{5} \)  below  \( \Theta_{D} \)  in 3D systems. Due to large Fermi surface in most of the metals all phonons are able to scatter electrons [24] implying  \( \Theta_{BG} \)  is equal to  \( \Theta_{D} \) .

Charge carrier density is considered as an important parameter to engineer the physical properties in 2D materials. For example, with increasing carrier density  \( MoS_{2} \)  exhibits metal-insulator transition whereas a medium carrier density is needed for its transistor application [42]. It is reported that by hole doping  \( (n = +3.3 \times 10^{14} \, \text{cm}^{-2}) \) ,  \( \rho_{e-ph} \)  of pristine  \( \beta_{12} \)  borophene increases by  \( \sim 4.29 \)  times [27]. And as mentioned earlier,  \( \Theta_{BG} \)  of graphene can be varied from 100 to 1000 K with different carrier densities [25]. While the effect in the former example is due to strong electron-electron interaction, in the latter two cases it is limited by the electron-phonon
 
![](./images/867766869136769670_3.jpg)

FIG. 2. (a) Density of states (DOS) of 2D Na. The Fermi energy ( \( E_{F} \) ) is set to zero. The DOS around  \( E_{F} \)  is nearly constant, shows the typical nature of 2DEG. (b) Fermi surface of 2D Na in the first Brillouin zone.

![](./images/867766869136769670_4.jpg)

FIG. 3. (a) Temperature dependence intrinsic electrical resistivity of 2D Na for different shifting of  \( E_{F} \) . (b) Similar quantities as in (a) plotted in logarithm scale to distinguish the behavior of  \( \rho_{e-ph} \)  in two distinct temperature regimes.

coupling. Since the 2D metal surface is quite exposed to external gate the carrier density can be tuned considerably by applying gate voltage. Concurrently, the Fermi energy  \( \left(\mathrm{E}_{F}\right) \)  of the system changes with gate voltage. Park et al. have shown that the  \( E_{F} \)  in graphene is found to lie at  \( \sim0.65 \)  eV from the Dirac point corresponding to  \( 4\times10^{13} \)  cm \( ^{-2} \)  of the carrier density [43]. In borophene, 0.43 eV of shifting of  \( E_{F} \)  leads to the carrier density  \( n=3.3\times10^{14} \)  cm \( ^{-2} \)  [27]. The preexisting metallic nature of pristine borophene [27, 28] is attributed to this large carrier density with small change in  \( E_{F} \) .

To incorporate the charge doping we have shifted the  \( E_{F} \)  with respect to the  \( E_{f} \)  of pristine 2D Na. Then from density of states (DOS) we have estimated the carrier density. At  \( E_{F} = 0.5 \)  eV the carrier density is found to be  \( 2.23 \times 10^{14} \)  cm \( ^{-2} \) . Achieving such a carrier density is feasible in 2D materials by external gate voltage [25]. The DOS of 2D Na is shown in Fig. 2(a) which explains the typical nature of 2DEG, DOS is independent of energy. Therefore, we have also calculated the electron effective mass by using the relation in 2DEG,  \( n = 2m^{*}E_{F}/\pi\hbar^{2} \) , where  \( m^{*} \)  is effective mass of the electron. For  \( E_{F} = 0.5 \)  eV, we get  \( m^{*} \)  as  \( 0.53 m_{e} \)  with  \( m_{e} \) , being the mass of electron. This is nearly equal to the effective mass of  \( 0.47 m_{e} \) , that we have calculated from the  \( E(k) \) -k dispersion. The characteristic features of electron-phonon interaction driven resistivity of 2D Na are shown in Fig. 3. Fig. 3(a) represents  \( \rho_{e-ph}(T) \)  for different  \( E_{F} \) . For pure case  \( E_{F}=0.5 \)  eV, we get  \( 0(E_{F} > 0(E_{F}<0) \)  represents electron (hole) doping. The results suggest that  \( \rho_{e-ph} \)  is largely dependent on  \( E_{F} \) . For  \( E_{F}=-0.5 \) , 1.5 and -1.5 eV,  \( \rho_{e-ph} \)  is respectively  \( \sim1.5 \) ,  \( \sim4.0 \)  and  \( \sim7.0 \)  times larger than the  \( \rho_{e-ph} \)  (at T = 500 K) of pristine 2D Na. However with  \( E_{F}=0.5 \)  eV,  \( \rho_{e-ph}(T) \)  lies below the  \( \rho_{E-ph}(T) \) , of pure compound. The mechanism behind this reduced resistivity is discussed later. We believe it is one of the important predictions in this new 2D material.

The carrier density that is obtained from  \( E_{F} = \pm1.5 \)  eV is yet to be achieved by experiment in 2D materials. We note that  \( E_{F} = \pm1.5 \)  eV are the two hypothetical case studies carried out for comparison purpose only. At  \( E_{F} = 1.5 \)  eV, we have two bands across the Fermi energy (see Fig. 5(b)). Therefore, the transport mechanism at  \( E_{F} = 1.5 \)  eV can not be simple like at  \( E_{F} = 0.0 \)  and 0.5 eV. In fact, due to intricate Fermi surface (FS) Bloch-Grüneisen theory is not satisfied in  \( \beta_{12} \)  and  \( \gamma_{3} \)  borophene [28]. In contrast to borophene, the FS in 2D Na is clean up to  \( E_{F} \approx 0.79 \)  eV. Fig. 2(b) represents the FS of 2D Na at  \( E_{F} = 0.0 \)  eV. The circular shape of the FS holds another characteristic of 2DEG. Though it is not shown here the FS at 0.5 eV is also a circle. Up to  \( E_{F} \approx 0.79 \)  eV, the electronic conduction can be described by a single band (3s). Hence, the associated FS is isotropic which indicates the applicability of Bloch-Grüneisen theory. Fig. 3(b) represents  \( \rho_{e-ph}(T) \)  in the logarithm scale for various  \( E_{F} \) . Two distinct regimes of  \( \rho_{e-ph}(T) \)  are well noticed from the plot. The crossover between the two regimes occurs at temperature,  \( \Theta_{BG} \) ,  \( \sim 50 \)  K and is independent of  \( E_{F} \)  and n (n is proportional to  \( E_{F}) \) . The phonons are excited at low temperature to scatter the carriers in this soft-mode system. The carrier density dependence behavior of  \( \Theta_{BG} \)  in 2D Na is similar to the borophene case and is different from graphene.

The  \( \rho_{e-ph}(T) \)  of 2D Na that we discussed above are calculated with Allen's model [29]. We have also calculated  \( \rho_{e-ph}(T) \)  with an exact solution [33]. We find that the results are in good agreement in both the calculations. However, at very low temperature Allen's model explains accurately the  \( T^{4} \)  behavior of 2D Na as shown in Fig. 4(a). To demonstrate the low and high temperature
 
![](./images/867766869136769670_5.jpg)

![](./images/867766869136769670_6.jpg)

FIG. 4. (a) Normalised electrical resistivity, in the double log scale, of 2D Na calculated using Allen's model and an exact solution with different grids. The dashed blue and dashed black lines are fitted by the functions  \( \rho \sim T^{4} \)  and  \( \rho \propto T \)  respectively. (b) Variation of  \( \rho \)  with  \( E_{F} \) . The  \( E_{F}^{-} \) values are w.r.t. the band minimum and the latter is taken as origin

![](./images/867766869136769670_7.jpg)

![](./images/867766869136769670_8.jpg)

FIG. 5. (a) Temperature dependence intrinsic electrical resistivity of 2D Na in comparison with graphene. (b) Band structure of 2D Na along the high-symmetry lines of hexagonal lattice. The  \( E_{F} \)  is 0.0 eV for the pure case.

behaviors of resistivity we have shown the normalised resistivity  \( (\rho/\rho_{T=300K}) \) , in the double log scale, calculated using the aforementioned approximations with different grids. The gird of  \( 200 \times 200 \times 1 \)  is represented by “nf 200” in the figure. We have fitted  \( \rho/\rho_{T=300K} \)  to  \( AT^{4} \)  and BT respectively for the low and high temperature regimes with  \( A = 2.9 \times 10^{-8}/K^{4} \)  and  \( B = 3.3 \times 10^{-3}/K \) . The low and high temperature fitted lines are intersected at  \( \Theta_{BG} \)  ( \( \sim 50 \)  K). As we have seen from Fig. 3(a), besides the case of  \( E_{F} = 1.5 \)  eV, the resistivity increases monotonically with  \( E_{F} \) . At  \( E_{F}=1.5 \)  eV, we have another band across the Fermi energy (see Fig. 5(b)). We have included more studies to see the behavior of resistivity with  \( E_{F} \)  (see the supplementary information) for which the band minimum is taken as origin. The power law dependence of  \( \rho \)  on  \( E_{F} \)  is explained through Fig. 4(b) for a particular temperature ( \( =50K \) ). The resistivity varies as  \( 1/E_{F} \)  and  \( 1/E^{2}_{F} \)  respectively for the lower and higher  \( E_{F} \) . This can be understood through the relation,  \( \rho = 2/(e^{2}v^{2}_{F}D(E_{F})\tau(E_{F})) \) , where  \( v_{F} \)  ( \( \propto \sqrt{E_{F}} \) ) is the Fermi velocity and  \( \tau \)  is the carrier life time [44]. Near the band edge i.e. for lower  \( E_{F} \) , the scattering rate  \( (1/\tau) \)  mimics the DOS of 2D Na, constant of energy. Relation between the scattering rates and DOS near the band edge has already been discussed in references [33, 45]. The scattering rates at an energy away from the band edge decreases with energy where DOS is still independent of energy. The scattering rates at lower and higher energies are provided in the supplementary information for different temperatures. This suggests that the resistivity varies as  \( 1/E_{F} \)  and  \( 1/E^{2}_{F} \)  respectively in the lower  \( E_{F} \)  and higher  \( E_{F}\) . This also implies that  \( \rho \)  is proportional to  \( 1/n \)  ( \( 1/n^{2} \) ) at low (high) electron density ( \( n \propto E_{F} \) ). The electrical transport in bilayer graphene, also a system with parabolic band dispersion, has similar behavior [44]. In the following paragraph we discuss the conductive behavior for a specific carrier density that can be achieved in practice ( \( E_{F} = 0.5 \)  eV).

Since we have enhanced conductivity for  \( E_{F} = 0.5 \)  eV in 2D Na it is important to compare the values quantitatively with the 2D material with least known electrical resistivity, graphene. Through Fig. 5(a) we have presented the phonon limited temperature dependence electrical resistivity of graphene with pure and doped 2D Na. The  \( \rho_{e-ph} \)  of electron doped ( \( E_{F} = 0.5 \)  eV) 2D Na is about 1.4 times larger than the  \( \rho_{e-ph} \)  of graphene. But, interestingly the former falls below the latter 450 K onwards. The phonons in graphene are excited around this temperature to scatter the carriers and possesses the increased resistivity. To understand the improved conductivity in doped 2D Na, compared to the pure case, we have calculated the slope ( \( \propto \)  velocity) of the 3s energy band in both cases. We find that the slope around  \( E_{F} = 0.5 \)  eV is  \( \sim 1.3 \)  times larger than around 0.0 eV. This suggests that the 3s band is more dispersive at 0.5 eV than at 0.0 eV. More dispersion leads to smaller effective mass and hence the electron mobility increases. A flat band possesses large effective mass with weak conductivity. In Fig. 5(b) we have labelled different Fermi energies in the electronic band structure of 2D Na. A careful observation of Fig. 5(b) tells us that the Fermi energy is close to the flat regime of the 3s orbital at large hole doping ( \( E_{F} = -1.5 \)  eV). This leads to substantial increase in the resistivity values (see Fig. 3(a)). Therefore, pinning  \( E_{F} \)  at a particular energy one can manipulate the conductive behavior in 2D Na. It is expected that all Na like systems will have similar kind of transport mechanism as
 
![](./images/867766869136769670_9.jpg)

![](./images/867766869136769670_10.jpg)

FIG. 6. (a) Temperature dependence electronic thermal conductivity of bulk and pure and doped 2D Na. (b) Comparison of Lorenz number in bulk and pure 2D Na.

explained above.

We now examine the thermal transport and the validity of Wiedemann-Franz law in 2D Na. In metals, the total thermal conductivity  \( \kappa \)  is defined as  \( \kappa_{e} + \kappa_{ph} \) , where  \( \kappa_{e} \)  is contributed by the electrons and  \( \kappa_{ph} \)  is due to phonons. However in free-electron-like systems (e.g. Na and K),  \( \kappa_{ph} \)  is negligible and  \( \kappa \)  is mainly contributed by the electrons. We also calculate  \( \kappa_{ph} \)  by modifying ShengBTE package [32] and find that  \( \kappa_{e}/\kappa_{ph} \approx 8.8 \times 10^{4} \)  at 300 K in 2D Na. Therefore,  \( \kappa_{ph} \)  is not considered in the further discussion and we are interested only on  \( \kappa_{e} \) . In typical metals,  \( \kappa_{c} \)  is  \( \propto T \)  in the low temperature limit and at high temperature  \( \kappa_{e} \)  is independent of T. Fig. 6(a) shows the temperature dependence features of  \( \kappa_{e} \)  for pure and electron doped ( \( E_{F} = 0.5 \)  eV) 2D Na in comparison with bulk Na. The figure demonstrates that the theory of electronic thermal transport is not violated both in low and high temperature limits. Moreover, we find that  \( \kappa_{e} \)  of pure 2D Na is  \( \sim 1.24 \)  times larger than the  \( \kappa_{e} \)  of bulk Na at room temperature. It is due to the reason that 2D Na has increased electron life time. The scattering rates of the bulk and 2D Na are compared in the supplementary information.

Additionally, it is found that  \( \kappa_{e}^{doped-2DNA} > \kappa_{e}^{pure-2DNA} \) , where  \( \kappa_{e}^{doped-2DNA} \)  stands for  \( \kappa_{e} \)  of doped 2D Na. Previously we have seen that  \( \rho_{e}^{doped-2DNA} \)  ( \( E_{F} = 0.5 \, eV \) ) <  \( \rho_{e}^{pure-2DNA} \) . Hence,  \( \kappa_{e}^{doped-2DNA} \)  ( \( E_{F} = 0.5 \, eV \) ) >  \( \kappa_{e}^{pure-2DNA} \)  can only happen when the ratio of the thermal conductivity ( \( \kappa \) ) to the electrical conductivity ( \( \sigma \) ) is constant. For metals, at not too low temperature  \( \kappa/\sigma \)  is directly proportional to the temperature and is defined as  \( \kappa/\sigma = LT \) , where  \( L = (\pi^{2}\kappa_{B}^{2}/3e^{2}) \)  is termed as the Lorenz number [46]. The Lorenz number does not depend on the scattering mechanisms or on the dimensionality of the system. The calculated L combinedly for pure and doped 2D Na lies in the range  \( 2.35 - 2.41 \times 10^{-8} V^{2}/deg^{2} \)  (see Fig. 6(b)) which is not much deviated from the theoretical value,  \( L_{0} = (2.45 \times 10^{-8} V^{2}/deg^{2}) \) . In the supplementary information we have included the derivation of L both for 2D and 3D metals. The derivation is based on the postulate that the free electrons are the primary carriers both for charge and heat current.

## IV. SUMMARY AND CONCLUSIONS

In summary, we carry out ab initio calculations to investigate the electrical and thermal transport of a free-standing two-dimensional (2D) sodium sheet based on the accurate solution of Boltzmann transport equation. The results suggest that 2D Na behaves like 2DEG where the electronic conduction is primarily driven by the half-filled 3s orbital. With achievable carrier density in 2D systems, we find that the temperature dependence intrinsic electrical resistivity of electron doped 2D Na is  \( \sim 1.4 \)  times larger than that of graphene and lies below than that of the latter 450 K onwards. Bloch-Grüneisen temperature is predicted to lie at  \( \sim 50 \)  K in this soft-phonon-mode system and is not dependent on the type or concentration of the charge carriers. The electronic thermal conductivity ( \( \kappa_{e} \) ) of pure 2D Na is  \( \sim 1.24 \)  times larger than the  \( \kappa_{e} \)  of bulk Na at 300 K. The Wiedemann-Franz law is not violated in 2D Na. The results presented here are not only encouraging from the 2D electronic and thermopower devices viewpoint but are also important for the bulk systems having a plane of Na atoms.

## ACKNOWLEDGEMENTS

A. Jena acknowledges the financial support from Shenzhen Science, Technology and Innovation Commission.

[1] K. S. Novoselov et al., Proc. Natl. Acad. Sci. U.S.A. 102, 10451 (2005).

[2] K. S. Novoselov et al., Nature (London) 438, 197 (2005).
[3] A. A. Balandin et al., Nano Lett. 8, 902 (2008).
 

[4] J. H. Seol et al., Science 328, 213 (2010).

[5] S. Z. Butler et al., ACS Nano 7, 2898 (2013).

[6] P. Miro, M. Audiffred, and T. Heine, Chem. Soc. Rev. 43, 6537 (2014).

[7] X. Zou and B. I. Yakobson, Acc. Chem. Res. 48, 73 (2015).

[8] F. Yin, J. Akola, P. Koskinen, M. Manninen, and R. E. Palmer, Phys. Rev. Lett. 102, 106102 (2009).

[9] T. Zhang, P. Cheng, W.-J. Li, Y.-J. Sun, G. Wang, X.-G. Zhu, K. He, L. Wang, X. Ma, X. Chen, et al., Nat. Phys. 6, 104 (2010).

[10] L. Li, Y. Wang, S. Xie, X.-B. Li, Y.-Q. Wang, R. Wu, H. Sun, S. Zhang, and H.-J. Gao, Nano Lett. 13, 4671 (2013).

[11] J. Zhao, Q. Deng, A. Bachmatiuk, G. Sandeep, A. Popov, J. Eckert, and M. H. Rammeli, Science 343, 1228 (2014).

[12] L.-M. Yang, T. Frauenheim, and E. Ganz, Phys. Chem. Chem. Phys. 17, 19695 (2015).

[13] L.-M. Yang, M. Dornfeld, T. Frauenheim, and E. Ganz, Phys. Chem. Chem. Phys. 17, 26036 (2015).

[14] L.-M. Yang, T. Frauenheim, and E. Ganz, J. Nanomater. 2016, 8429510 (2016).

[15] H. Liu, A. T. Neal, Z. Zhu, Z. Luo, X. Xu, D. Tománek, and P. D. Ye, ACS Nano 8, 4033 (2014).

[16] L. Li, Y. Yu, G. J. Ye, Q. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen, and Y. Zhang, Nat. Nanotechnol. 9, 372 (2014).

[17] D. Zhong et al., Sci. Adv. 3, 1603113 (2017).

[18] Y. Guo et al., Adv. Mater. 29, 1700715 (2017).

[19] W. Luo, K. Xu, and H. Xiang, Phys. Rev. B 96, 235415 (2017).

[20] M. L. Foo, Y. Wang, S. Watauchi, H. Zandbergen, T. He, R. J. Cava, and N. P. Ong, Phys. Rev. Lett. 92, 247001 (2004).

[21] K. Takada, H. Sakurai, E. Takayama-Muromachi, F. Izumi, R. A. Dilanian, and T. Sasaki, Nature (London) 422, 53 (2003).

[22] Y. Wang, N. S. Rogado, R. J. Cava, and N. P. Ong, Nature (London) 423, 425 (2003).

[23] J. Nevalaita and P. Koskinen, Phys. Rev. B 97, 035411 (2018).

[24] M. S. Fuhrer, Physics 3, 106 (2010).

[25] D. K. Efetov and P. Kim, Phys. Rev. Lett. 105, 256805 (2010).

[26] C.-H. Park, N. Bonini, T. Sohier, G. Samsonidze, B. Kozinsky, M. Calandra, F. Mauri, and N. Marzari, Nano Lett. 14, 1113 (2014).

[27] J. Zhang, J. Zhang, L. Zhou, C. Cheng, C. Lian, J. Liu, S. Tretiak, J. Lischner, F. Giustino, and S. Meng, Angew. Chem. 130, 4675 (2018).

[28] Z. Liu, M. Zhu, and Y. Zheng, J. Mater. Chem. C 7, 986 (2019).

[29] P. B. Allen, Phys. Rev. B 17, 3725 (1978).

[30] L. Lindsay, D. A. Broido, and T. L. Reinecke, Phys. Rev. Lett. 109, 095901 (2012).

[31] L. Lindsay, D. A. Broido, and T. L. Reinecke, Phys. Rev. Lett. 111, 025901 (2013).

[32] W. Li, J. Carrete, N. A. Katcho, and N. Mingo, Comput. Phys. Commun. 185, 1747 (2014).

[33] W. Li, Phys. Rev. B 92, 075405 (2015).

[34] S. Poncé, E. R. Margine, C. Verdi, and F. Giustino, Comput. Phys. Commun. 209, 116 (2016).

[35] P. Giannozzi et al., J. Phys.: Condens. Matter 21, 395502 (2009).

[36] R. Saito, G. Dresselhaus, and M. Dresselhaus, Imperial College Press, London (1998).

[37] L. Wirtz and A. Rubio, Solid State Commun. 131, 141 (2004).

[38] S. Kushwaha and J. Rajput, Phys. Rev. B 2, 3943 (1970).

[39] C. M. Goel, B. . P. Pandey, and B. Dayal, Phys. Stat. Sol. (b) 69, 589 (1975).

[40] A. Tari, Imperial College Press, London, p. 37 (2003).

[41] C. Kittel, Wiley, New York, 7th edition, p. 126 (1996).

[42] B. Radisavljevic and A. Kis, Nat. Mater. 12, 815 (2013).

[43] C.-H. Park, F. Giustino, M. L. Cohen, and S. G. Louie, Phys. Rev. Lett. 99, 086804 (2007).

[44] S. D. Sarma, S. Adam, E. H. Hwang, and E. Rossi, Rev. Mod. Phys. 83, 407 (2011).

[45] M. Lundstrom, Cambridge University Press, Cambridge, UK, 2nd edition, p. 67 (2000).

[46] C. Kittel, Wiley, New York, 7th edition, p. 168 (1996).
 
