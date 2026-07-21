Materials Research Express

ACCEPTED MANUSCRIPT

# Impact of tensile strain on the thermal transport of zigzag hexagonal boron nitride nanoribbon: An equilibrium molecular dynamics study

To cite this article before publication: Ishtiaque Ahmed Navid *et al* 2018 *Mater. Res. Express* in press https://doi.org/10.1088/2053-1591/aaaa89

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2018 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.

As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 144.96.173.4 on 27/01/2018 at 15:44

# Impact of tensile strain on the thermal transport of zigzag hexagonal boron nitride nanoribbon: An equilibrium molecular dynamics study

Ishtiaque Ahmed Navid, Asir Intisar Khan and Samia Subrina$^\text{a}$

Department of Electrical and Electronic Engineering, Bangladesh University of Engineering and Technology, Dhaka, 1205, Bangladesh

The thermal conductivity of single layer strained hexagonal boron nitride nanoribbon (h-BNNR) has been computed using the Green-Kubo formulation of Equilibrium Molecular Dynamics (EMD) simulation. We have investigated the impact of strain on thermal transport of h-BNNR by varying the applied tensile strain from 1% upto 5% through uniaxial loading. The thermal conductivity of h-BNNR decreases monotonically with the increase of uniaxial tensile strain keeping the sample size and temperature constant. The thermal conductivity can be reduced upto 86% for an applied uniaxial tensile strain of 5%. The impact of temperature and width variation on the thermal conductivity of h-BNNR has also been studied under different uniaxial tensile strain conditions. With the increase in temperature, the thermal conductivity of strained h-BNNR exhibits a decaying characteristics whereas it shows an opposite pattern with the increasing width. Such study would provide a good insight on the strain tunable thermal transport for the potential device application of boron nitride nanostructures.

## I. INTRODUCTION

As the silicon-based microelectronic devices are progressively reaching their performance limit, we observe a considerably fast development of nanotechnology in potential next-generation device applications. Specifically, the remarkable progress in graphene [1], [2] research due to its intriguing electronic [3], thermal [4] and mechanical [5] properties has instigated new surge of research interest in other two dimensional (2D) nanomaterials. Hexagonal boron nitride nanoribbon (h-BNNR) is a 2D nanostructure which has a similar honeycomb lattice structure [6] like graphene nanoribbon (GNR) where carbon atoms are successively replaced by boron and nitrogen atoms. Hexagonal boron nitride (h-BN) also possesses notable electronic properties as well as some exceptional attributes different from graphene such as large bandgap of 5.5eV [7], deep ultra-violate photo emission [8] and innate half metallicity [9]. The ultra-thin h-BNNR layer is well suited for high density

$^\text{a}$Corresponding Author: E-Mail: samiasubrina@eee.buet.ac.bd; ssubr002@ucr.edu
Tel.: +880-19-3795-9083; +880-02-9668054; Fax: +88-02-9668054

integration, but the resulting heat from device operation might perturb the nano-device stability as well as reliability. As such, the efficient channeling of heat flow within the nano-device is of critical importance and thus requires a comprehensive study of the thermal transport in nanomaterials like h-BNNR. Particularly, in comparison with the reasonably wide range of investigations on the mechanical [6], [10]–[12] as well as electronic [13]–[17] properties of h-BN, its thermal property is yet to be well explored.

Generally, two distinct factors can be ascribed for the net thermal conductivity in a solid. The first contribution arises from phonons and the second one results from electrons. In case of an insulator like boron nitride, the electrons being firmly confined to the atomic nuclei, phonons play the principal role in carrying the thermal current. On top of that, two different types of parameters namely thermodynamic parameters and extrinsic parameters govern the effective thermal conductivity. Thermodynamic parameters include temperature and pressure whereas extrinsic parameters consist of impurities, defects and bounding surfaces. Among several possibilities of tuning thermal transport statically or dynamically, stress/strain effect as a result of uniform applied pressure is one of the possible options to explore. The impact of stress/strain on material properties ranging from electrical, optical to mechanical has already been investigated extensively. Silicon under stained condition has been utilized to increase the electron mobility in MOSFETs [18]–[20]. Strain has also been reported to impact and engineer the electronic properties of 2D nanomaterials like graphene [21], [22] and silicene [23] as well as the quality factor of nanowire resonator [24]. The gain of laser diode has been enhanced by lowering the threshold carrier density as a result of strain effect on optical properties [25]–[27]. Moreover, strain/stress effect has been employed in improving the performance of thermoelectric materials [28], [29] which indicates the potential application of strain/stress as a tuning mechanism of thermal conductivity. A considerable number of studies on the strain impact on thermal conductivity of bulk materials have already been carried out [30]–[33]. Furthermore, the effect of strain on the thermal conductivity of 2D materials like graphene [34], [35] as well as silicene [36] has also been analyzed. The impact of size and defect such as vacancy on the thermal conductivity of boron nitride nanostructure has been studied by Mortazavi *et al.* [37], Yuan *et al.* [38] and Yang *et al.* [39]. Le *et al.* [40] investigated the mechanical fracture toughness of boronitrene and four types of boronitrene and graphene interfaces considering both B-C and C-N bonds. Le also studied the size effects (i.e. length width ratio) on the mechanical properties such as Young's modulus, fracture stress and fracture strain of rectangular BNNR [41]. Again, the thermomechanical properties of single layer h-BN including thermal induced ripples, heat capacity and thermal lattice expansion have been studied and compared to those of graphene by Singh *et al.* using atomistic simulations [42]. An analytical formulation has also been proposed by Boldrin *et al.* [43] for the study of in-plane mechanical properties like tensile and shear rigidity and Poisson's ratio for h-BN nanosheets.


In this context, we investigate the impact of uniaxial tensile strain on the thermal transport of zigzag hexagonal boron nitride nanoribbon (h-BNNR). We use equilibrium molecular dynamics simulation (EMD) with the Tersoff potential field parameters proposed by Linsday *et al.* [44] in order to compute the thermal conductivity of nanometer sized single layer h-BNNR. The proposed parameters of Lindsay *et al.* include upto third nearest neighbor interactions between atoms in adjacent planes whereas the original Tersoff [45], [46] includes up to second nearest neighbor interactions. Particularly for the set of parameters proposed by Lindsay *et al.* [44] the quadratic out-of-plane phonon branch i.e. ZA modes and the transverse acoustic (TA) and longitudinal acoustic (LA) branches are accurately represented in the phonon spectrum. Next, the change in the thermal conductivity of zigzag h-BNNR in response to the different percentages of uniaxial tensile strain is explored. Subsequently, the width and temperature dependence of zigzag h-BNNR thermal conductivity at various values of exerted uniaxial tensile strain is studied.

## II. SIMULATION DETAILS

Classical molecular dynamics (MD) simulation has been performed using LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) [47]. The B-N bonding interaction in h-BNNR has been described using Tersoff potential with the parameters determined by Lindsay *et al.* [44]. We have considered a 10nm x 3nm zigzag h-BNNR with B-N bond length of 0.1446 nm in equilibrium i.e. for the strain-free case as depicted in Fig. 1. The figure also presents the nanoribbon under uniaxial tensile strain in the zigzag direction (x direction).

We have used EMD simulation in our work applying periodic boundary condition along zigzag direction. Initially, the system energy minimization was carried out using steepest descent algorithm. Velocity-Verlet integrator was used for numerically integrating the equations of atomic motions taking a time step of 0.4 fs. The system was equilibrated and thermalized executing Nose-Hoover thermostat for 1.6x10⁵ time steps. Subsequently, we switched to NVE ensemble for 2x10⁵ time steps. Thermal conductivity is calculated in EMD by applying the linear response theorem [48] where the heat current vectors and their correlations are computed throughout the simulation. Thermal conductivity is basically linked to the ensemble average of heat current autocorrelation (HCACF) function according to the following equation known as Green-Kubo formulation:

$$
K_{x}=\frac{1}{V K_{B} T^{2}} \int_{0}^{\tau}\left\langle J_{x}(t) . J_{x}(0)\right\rangle d t \tag{1}
$$


where, $K_x$ is the thermal conductivity in x direction, $K_B$ is the Boltzmann constant and $J_x(t)$ is the heat current in the x direction. $T$ and $V$ are system temperature and volume, respectively. The system volume is calculated as the product of the h-BNNR surface area and van der Waals thickness (3.3 Å). $\tau$ refers to the correlation time which is the time required for the considerable amount of HCACF decay.

![](./images/813063011907403777_1.jpg)

Fig. 1: Schematic representation of h-BNNR under uniaxial strains along heat transfer direction (a) side view and (b) isometric view with zero strain; (c) side view and (d) isometric view with 5% tensile strain. Boron and Nitrogen atoms are represented by dark pink and blue colored balls respectively.

The heat current data were recorded in every 5 steps in order to obtain the HCACFs. Afterwards, the heat current autocorrelation values were calculated by taking the average of 10 obtained HCACFs. Finally, using equation (1), a

converged value of average thermal conductivity was computed which was taken as the average of 5 independent microcanonical ensembles with each starting at a different initial velocity.

## III. RESULTS AND DISCUSSIONS

First, we study the effect of tensile strain on the thermal conductivity of h-BNNR. In this work, we have applied uniaxial tensile strain in the x (zigzag) direction of the 10nm x 3nm h-BNNR at room temperature (300K) and the obtained thermal conductivities are depicted in Fig 2(a). The figure shows that the thermal conductivity of h-BNNR decreases monotonically with the increase in the applied tensile strain. A considerable reduction of approximately 86% in the thermal conductivity value is observed for 5% applied tensile strain, dropping from the strain-free value of 629 W/m-K to 87 W/m-K. Using molecular dynamics simulation, it is reported that graphene also shows strong strain impact on its thermal conductivity and thermal conductivity decreases with the increase of tensile strain [34], [35] which is in agreement with our results. On the contrary, using ab initio calculations, *Li et al.* found that there is an enhancement of thermal conductivity of monolayer h-BN with the increase of tensile strain [49]. These contrasting results can be attributed to the difference in calculation methods namely molecular dynamics and ab initio lattice dynamics. The discrepancies in the results of these two methods are expected as they consider different approximations. The consideration of anharmonic interactions is limited only to the first order for ab initio lattice dynamics whereas quantum effects cannot be included in molecular dynamics [50]. These factors eventually cause the opposing trend of results obtained from *Li et al.* [49] and our work. Again the study of the thermal transport properties of silicene [36], borophene [51] and phosphorene [52] showed an increasing trend of thermal conductivity with the increase in applied tensile strain as opposed to the results found for graphene [34], [35] and our work. The discrepancy of the results is originated from the initial buckled structures of silicene, borophene and phosphorene on the contrary to the flat structures of graphene and h-BNNR. With the increase of tensile strain on these structures, the buckled configuration becomes less buckled as there is a rotation in the bond. Consequently, there is an enhancement in both in-plane and out-of-plane phonon modes [36], [52] resulting in the increase of thermal conductivity. However, at larger tensile strains, the thermal conductivity starts exhibiting drooping characteristics with the applied strain [36], [52]. This can be attributed to the in-plane and out-of-plane phonon modes softening due to the excessively stretched bonds caused by the large tensile strains [36], [52].

![](./images/813063011907403777_2.jpg)

![](./images/813063011907403777_3.jpg)

Fig. 2: (a) Thermal conductivity of 10nm x 3nm sized h-BNNR as a function of tensile strain in zigzag direction at 300K. The solid line indicates the numerically fitted curve through the data. (b) Envelopes of decaying normalized heat current autocorrelation function (HCACF) profile as a function of correlation time for zero-strain and strained h-BNNRs

It can be seen from Fig. 2(a) that the thermal conductivity initially decreases at a higher rate with the increasing strain and then further increase of strain slowdowns the reduction of thermal conductivity. This trend is in agreement with the earlier reported studies [33], [34]. The figure further interprets the percentage reduction in thermal conductivity of 10 nm x 3 nm h-BNNRs at room temperature for increasing strain in comparison with the strain free sample of similar size. As interpreted in Fig. 2(a), the thermal conductivity reduces almost by 27% to 64% with the applied strain of 1% to 2%, respectively while 5% applied strain shows a decrease of about 86% from the thermal conductivity for zero strain h-BNNR of 629 W/m-K.

Fig. 2(b) shows decaying HCACF profile of h-BNNR which describes the convergence phenomena of strain dependence of thermal conductivity. An increase in the strain leads to stronger lattice anharmonicity. This causes a faster decay of HCACF profile with increased applied strain which rationalizes the reduction in thermal conductivity of h-BNNR.

The thermal conductivity decrement of h-BNNR under tensile strain can be attributed to the reduction of the in-plane stiffness resulting in the phonon modes softening and the increase of lattice anharmonicity [33]. According to the kinetic theory, the thermal conductivity is directly proportional to three quantities: the specific heat capacity, the phonon group velocity and the phonon mean free path [32]. In this study, the specific heat capacity is assumed to remain unchanged as the

simulation has been carried out at the room temperature which is above the Debye temperature. Again, the phonon group velocity is considered to be equal to the speed of sound through the medium as thermal transport is dominantly influenced by the long wavelength phonons. As the lattice elasticity is non-linear in nature, in-plane stiffness considerably varies with strain.

Then again, the speed of sound being proportional to the square root of the stiffness, changes significantly with strain. It is observed that stiffness decreases with the application of tensile strain which eventually contributes in the reduction of thermal conductivity. Moreover, the phonon mean free path is governed by the lattice anharmonicity which is a function of the applied strain. Therefore, the mean free path variation caused by the anharmonicity, in turns, the applied strain characterizes the strain dependence of the thermal transport whereas the overall impact of tensile strain is the reduction of thermal conductivity [33].

![](./images/813063011907403777_4.jpg)

Fig. 3: Total energy of the h-BNNR structure under different tensile strain conditions at room temperature

Fig. 3 depicts the total energy variation of h-BNNR configurations under various tensile strain conditions during the simulation time at room temperature. The curves display negligible amount of fluctuations in the total energy throughout the entire simulation time. This implies that the h-BNNR structures were well stable under the applied strained conditions at room temperature.

![](./images/813063011907403777_5.jpg)

Fig. 4: Thermal conductivity of 10nm x 3nm h-BNNR as a function of temperature under various tensile strain conditions.

The solid lines represent the numerically fitted curves through the data.

Next, the temperature dependence of thermal conductivity for h-BNNR has been studied under different tensile strain values. Fig. 4 shows the thermal conductivity of a 10 nm x 3 nm h-BNNR as a function of temperature for tensile ranging from 1% to 5%. The thermal conductivity of h-BNNR decays monotonically with the increase in temperature for a particular applied tensile strain. This trend is in line with the studies of Sevik *et al.* [53] and Khan *et al.* [54] where both the works have been carried out using Green-Kubo formulation of molecular dynamics simulation. On the other hand, in the works of Jiang *et al.* [55] employing self-consistent investigation and Chen *et al.* [56] using non-equilibrium molecular dynamics (NEMD) simulation along with Boltzmann Transport Equation (BTE), it is found that at low temperatures, the thermal conductivity of boron nitride nanostructures increases with increasing temperature followed by the decreasing trend at higher temperatures.

This difference in result at low temperature region is due to the fact that there is no consideration of quantum effect below Debye temperature in classical molecular dynamics simulation.

The decaying nature of thermal conductivity with the increasing temperature found in our study indicates the increase of non-linear thermal resistivity. This can be explained considering phonon phonon anharmonic interaction i.e. Umklapp scattering mechanism at an elevated temperature. In this study, thermal conductivity initially varies with temperature following an inverse relation $T^{-1}$, but at much higher temperature values, this relation no longer applies. This is due to the fact that, at high enough temperatures, phonon-phonon scattering process assumes a higher order mechanism on top of the increased anharmonic interactions between the two acoustic phonon modes [57]-[59]. Similar drooping characteristics of thermal conductivity with increased temperature are observed for a certain range of tensile strain while the curves shift downwards with the increasing strain.

![](./images/813063011907403777_6.jpg)

Fig. 5: Room temperature thermal conductivity of h-BNNR as a function of the nanoribbon width. The nanoribbon length is fixed at 10nm. The solid lines represent the numerically fitted curves through the data.

The width dependence of h-BNNR under tensile strain has also been investigated as presented in Fig. 5. The figure shows the variation of thermal conductivity of h-BNNR with respect to the ribbon width ranging from 1nm to 5nm for tensile strain of 1%, 2%, 3%, 4% and 5%. The thermal conductivity continues to rise with the increase of width under a specific applied strain. The studies of Sevik *et al.* [53] and Khan *et al.* [54] on width dependence of strain-free BNNR thermal conductivity found similar results. This is also in agreement with the investigation of Cao [60] and Yang *et al.* [61] on the width dependence of strain-free GNR thermal conductivity. The set of curves in Fig. 5 drift downwards for increased tensile strain.

The edge localized phonon effect also known as boundary scattering effect as well as the phonon's Umklapp scattering effect, both have to be taken under consideration to elucidate the impact of width variation on the thermal conductivity of h-BNNR. With the increase in h-BNNR width, the influence of boundary scattering is abated which causes the rise of thermal conductivity. On the other hand, increase in the ribbon width intensifies the probability of Umklapp scattering as the number of available phonons increases and energy separation between them is truncated. These two mechanisms compete with each other and the more prevalent one actually governs the characteristics of the thermal conductivity variation. For narrower widths of h-BNNRs, as is the case of our study, the weakened boundary scattering effect shows more predominant impact than the Umklapp scattering effect which causes the thermal conductivity to rise with the increase in ribbon width [62]–[65].

## IV. CONCLUSIONS

In this paper, the uniaxial tensile strain effects on the thermal transport of zigzag h-BNNR have been explored systematically. The thermal conductivity exhibits a decaying trend with the increase of uniaxial tensile strain on h-BNNR primarily due to the impact of phonon modes softening and enhanced lattice anharmonicity. Again, it has been observed that the thermal conductivity decreases as the system temperature is gradually elevated at a fixed applied uniaxial tensile strain which can be attributed to the increased high frequency phonon-phonon scattering. This reflects both temperature and tensile strain have negative impact on the thermal conductivity of h-BNNR. Finally, we have studied the impact of width variation on the thermal conductivity of h-BNNR under different tensile strain conditions. Thermal conductivity continues to increase with the increasing width of our study range because of the dominant impact of boundary scattering. This scattering decreases with the increasing width over Umklapp scattering which in turn causes the rise of thermal conductivity. In all, our results provide a strong perception on the thermal transport phenomenon of h-BNNR under uniaxial tensile strain and lead us to a potential doorway of tunable thermal conductivity for thermal management and sensor applications with boron nitride nanostructures.

## REFERENCES

[1] A. K. Geim and K. S. Novoselov, "The rise of graphene.," *Nat. Mater.*, vol. 6, no. 3, pp. 183-91, 2007.

[2] K. S. Novoselov *et al.*, "Two-dimensional atomic crystals," *Sci. Am.*, vol. 102, no. 3, pp. 90-97, 2005.

[3] J. R. Williams, L. Dicarlo, and C. M. Marcus, "Quantum Hall Effect in a Gate-Controlled p-n Junction of Graphene," no. August, pp. 638-641, 2007.

[4] K. Nakada, M. Fujita, G. Dresselhaus, and M. S. Dresselhaus, "Edge state in graphene ribbons : Nanometer size effect and edge shape dependence," vol. 54, no. 24, pp. 954-961, 1996.

[5] C. Lee, X. Wei, J. W. Kysar, and J. Hone, "Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene," *Science (80- .)*, vol. 321, no. 5887, pp. 385-388, 2008.

[6] A. Nag, K. Raidongia, K. P. S. S. Hembram, R. Datta, U. V. Waghmare, and C. N. R. Rao, "Graphene analogues of BN: Novel synthesis and properties," *ACS Nano*, vol. 4, no. 3, pp. 1539-1544, 2010.

[7] X. Blase, a Rubio, S. G. Louie, and M. L. Cohen, "Stability and Band Gap Constancy of Boron Nitride Nanotubes," *Europhys. Lett.*, vol. 28, no. 5, pp. 335-340, 2007.

[8] D. Pacií, J. C. Meyer, Ç. Girit, and A. Zettl, "The two-dimensional phase of boron nitride: Few-atomic-layer sheets and suspended membranes," *Appl. Phys. Lett.*, vol. 92, no. 13, pp. 212-214, 2008.

[9] F. Zheng *et al.*, "Half metallicity along the edge of zigzag boron nitride nanoribbons," *Phys. Rev. B*, vol. 78, no. 20, p. 205415, 2008.

[10] Q. Peng, W. Ji, and S. De, "Mechanical properties of the hexagonal boron nitride monolayer: Ab initio study," *Comput. Mater. Sci.*, vol. 56, no. August 2017, pp. 11-17, 2012.

[11] D. Golberg *et al.*, "Boron nitride nanotubes and nanosheets," *ACS Nano*, vol. 4, no. 6, pp. 2979-2993, 2010.

[12] M. Topsakal, E. Akturk, and S. Ciraci, "Two and One-dimensional Honeycomb Structure of Boron Nitride," pp. 1-11, 2008.

[13] D. Golberg *et al.*, "Recent advances in boron nitride nanotubes and nanosheets," *Isr. J. Chem.*, vol. 50, no. 4, pp. 405-416, 2010.

[14] N. Ooi, A. Raikar, L. Lindsley, and J. Adams, "Electronic structure and bonding in hexagonal boron nitride," *J. Phys. Condens. Matter*, vol. 97, no. 18, pp. 97-115, 2006.

[15] J. Furthmuller, J. Hafner, and G. Kresse, "Ab initio calculation of the structural and electronic properties of carbon and boron nitride using ultrasoft pseudopotentials," *Phys. Rev. B*, vol. 50, no. 21, pp. 606-622, 1994.

[16] Q. Tang, Z. Zhou, and Z. Chen, "Molecular charge transfer: A simple and effective route to engineer the band

structures of BN nanosheets and nanoribbons," *J. Phys. Chem. C*, vol. 115, no. 38, pp. 18531–18537, 2011.

[17] Q. Peng, A. Zamiri, and S. De, "Tunable Band Gaps of Mono-layer Hexagonal BNC Heterostructures," vol. 1, no. 518, pp. 1–16, 2011.

[18] K. Ismail, S. F. Nelson, J. O. Chu, and B. S. Meyerson, "Electron transport properties of Si/SiGe heterostructures: Measurements and device implications," *Appl. Phys. Lett.*, vol. 63, no. 5, pp. 660–662, 1993.

[19] X. Li, K. Maute, M. L. Dunn, and R. Yang, "Strain effects on the thermal conductivity of nanostructures," *Phys. Rev. B*, vol. 81, no. 24, p. 245318, 2010.

[20] T. Vogelsang and K. R. Hofmann, "Electron transport in strained Si layers on Si1-xGex substrates," *Appl. Phys. Lett.*, vol. 63, no. 2, pp. 186–188, 1993.

[21] V. M. Pereira and A. H. C. Neto, "Strain Engineering of Graphene’s Electronic Structure," *Phys. Rev. Lett.*, vol. 46801, no. July, pp. 1–4, 2009.

[22] K. Xue, Z. Xu, K. Xue, and Z. Xu, "Strain effects on basal-plane hydrogenation of graphene : A first-principles study Strain effects on basal-plane hydrogenation of graphene : A first-principles study," *Appl. Phys. Lett.*, vol. 96, no. 2010, pp. 33–36, 2012.

[23] G. LIU, M. S. WU, C. Y. OUYANG, and B. XU, "Strain-induced semimetal-metal transition in silicene," *Europhys. Lett.*, vol. 99, no. January 2016, 2012.

[24] S. Y. Kim and H. S. Park, "Utilizing Mechanical Strain to Mitigate the Intrinsic Loss Mechanisms in Oscillating Metal Nanowires," *Phys. Rev. Lett.*, vol. 215502, no. November, pp. 1–4, 2008.

[25] O. Stier, M. Grundmann, and D. Bimberg, "Electronic and optical properties of strained quantum dots modeled by 8-band k – p theory," *Phys. Rev. B*, vol. 59, no. 8, pp. 5688–5701, 1999.

[26] R. Ghosh, D. Basak, and S. Fujihara, "Effect of substrate-induced strain on the structural , electrical , and optical properties of polycrystalline ZnO thin films Effect of substrate-induced strain on the structural , electrical , and optical," *J. Appl. Phys.*, vol. 2689, no. 2004, 2012.

[27] M. Suzuki and T. Uenoyama, "Strain effect on electronic and optical properties of GaN / AlGaN quantumwell lasers Strain effect on electronic and optical properties of GaN / AlGaN quantum-well lasers," *J. Appl. Phys.*, vol. 80, no. 6868, 1996.

[28] J. F. Meng, N. V. C. Shekar, and J. V Badding, "Multifold enhancement of the thermoelectric figure of merit in p-type BaBiTe 3 by pressure tuning," *J. Appl. Phys.*, vol. 90, no. 6, 2001.

[29] D. A. Polvani, J. F. Meng, N. V. C. Shekar, J. Sharp, and J. V Badding, "Large Improvement in Thermoelectric

Properties in Pressure-Tuned p-Type Sb 1 . 5 Bi 0 . 5 Te 3,” CHEM MATER, vol. 13, no. 6, pp. 2068–2071, 2001.

[30] P. Andersson, R. Ross, and G. Backstrom, “Thermal resistivity of ice Ih near the melting point,” J. Phys. C Solid State Phys., vol. 13, 1980.

[31] R. Ross and O. Sandberg, “The thermal conductivity of four solid phases of NH , F , and a comparison with H , O,” J. Phys. C Solid State Phys., vol. 11, 1978.

[32] S. Bhowmick and V. B. Shenoy, “Effect of strain on the thermal conductivity of solids,” J. Chem. Phys., vol. 125, no. 16, 2006.

[33] R. C. Picu, T. Borca-Tasciuc, and M. C. Pavel, “Strain and size effects on heat transport in nanostructures,” J. Appl. Phys., vol. 93, no. 6, pp. 3535–3539, 2003.

[34] Z. Guo, D. Zhang, and X.-G. Gong, “Thermal conductivity of graphene nanoribbons,” Appl. Phys. Lett., vol. 95, no. 16, p. 163103, 2009.

[35] N. Wei, L. Xu, H.-Q. Wang, and J.-C. Zheng, “Strain engineering of thermal conductivity in graphene sheets and nanoribbons: a demonstration of magic flexibility,” Nanotechnology, vol. 22, no. 10, p. 105705, 2011.

[36] Q. X. Pei, Y. W. Zhang, Z. D. Sha, and V. B. Shenoy, “Tuning the thermal conductivity of silicene with tensile strain and isotopic doping: A molecular dynamics study,” J. Appl. Phys., vol. 114, no. 3, 2013.

[37] B. Mortazavi and Y. Rémond, “Investigation of tensile response and thermal conductivity of boron-nitride nanosheets using molecular dynamics simulations,” Phys. E Low-Dimensional Syst. Nanostructures, vol. 44, no. 9, pp. 1846–1852, 2012.

[38] Y. Zhang, Y. Zhu, and M. Li, “Lattice thermal conductivity of boron nitride nanoribbon from molecular dynamics simulation,” Wuhan Univ. J. Nat. Sci., vol. 21, no. 6, pp. 461–465, 2016.

[39] K. Yang, Y. Chen, Y. Xie, X. L. Wei, T. Ouyang, and J. Zhong, “Effect of triangle vacancy on thermal transport in boron nitride nanoribbons,” Solid State Commun., vol. 151, no. 6, pp. 460–464, 2011.

[40] M. Q. Le and Y. Umeno, “Fracture of monolayer boronitrene and its interface with graphene,” Int. J. Fract., vol. 205, no. 2, pp. 151–168, 2017.

[41] M. Q. Le, “Size effects in mechanical properties of boron nitride nanoribbons,” J. Mech. Sci. Technol., vol. 28, no. 10, pp. 4173–4178, 2014.

[42] S. K. Singh, M. Neek-Amal, S. Costamagna, and F. M. Peeters, “Thermomechanical properties of a single hexagonal boron nitride sheet,” Phys. Rev. B, vol. 87, no. 184106, pp. 1–7, 2013.

[43] L. Boldrin, F. Scarpa, R. Chowdhury, and S. Adhikari, “Effective mechanical properties of hexagonal boron nitride

nanosheets," *Nanotechnology*, vol. 22, no. 50, 2011.

[44] L. Lindsay and D. A. Broido, "Enhanced thermal conductivity and isotope effect in single-layer hexagonal boron nitride," *Phys. Rev. B*, vol. 84, no. 15, p. 155421, 2011.

[45] J. Tersoff, "Empirical Interatomic Potentials for Carbon, with Applications to Amorphous Carbon," *Phys. Rev. Lett.*, vol. 61, no. 25, 1988.

[46] J. Tersoff, "Modeling solid-state chemistry: Interatomic potentials for multicomponent systems," *Phys. Rev. B*, vol. 39, no. 8, 1989.

[47] S. Plimpton, *Fast Parallel Algorithms for Short-Range Molecular Dynamics*, vol. 117, no. June 1994. 1995.

[48] D. Frenkel and B. Smit, *Understanding Molecular Simulation: From Algorithms to Applications*. San Diego, CA,USA: Academic Press, 2002.

[49] S. Li and Y. Chen, "Thermal transport and anharmonic phonons in strained monolayer hexagonal boron nitride," *Sci. Rep.*, vol. 7, no. October 2016, pp. 1-7, 2017.

[50] L. F. C. Pereira and D. Donadio, "Divergence of the thermal conductivity in uniaxially strained graphene," *Phys. Rev. B*, vol. 87, no. 12, p. 125424, 2013.

[51] B. Mortazavi, M. Le, T. Rabczuk, and L. F. C. Pereira, "Anomalous strain effect on the thermal conductivity of borophene: a reactive molecular dynamics study.," 2017.

[52] Y.-Y. Zhang, Q.-X. Pei, J.-W. Jiang, N. Wei, and Y.-W. Zhang, "Thermal conductivities of single- and multi-layer phosphorene: a molecular dynamics study," *Nanoscale*, vol. 8, no. 1, pp. 483-491, 2016.

[53] C. Sevik, A. Kinaci, J. B. Haskins, and T. ÇagIn, "Characterization of thermal transport in low-dimensional boron nitride nanostructures," *Phys. Rev. B*, vol. 84, no. 8, p. 85409, 2011.

[54] A. I. Khan, I. A. Navid, M. Noshin, and S. Subrina, "Thermal transport characterization of hexagonal boron nitride nanoribbons using molecular dynamics simulation," *AIP Adv.*, vol. 7, no. 105110, 2017.

[55] J.-W. Jiang and J.-S. Wang, "Self-consitent study of thermal conductivity in single-walled boron nitride nanotubes," *Phys. Rev. B*, vol. 84, no. 8, p. 85439, 2011.

[56] Y. C. Chen, S. C. Lee, T. H. Liu, and C. C. Chang, "Thermal conductivity of boron nitride nanoribbons: Anisotropic effects and boundary scattering," *Int. J. Therm. Sci.*, vol. 94, pp. 72-78, 2015.

[57] J. M. ZIMAN, *Electrons and Phonons: The Theory of Transport Phenomena in Solids*. Amen House, London, UK: Oxford University Press, 1960.

[58] D. J. Ecsedy and P. G. Klemens, "Thermal resistivity of dielectric crystals due to four-phonon processes and optical

modes," *Phys. Rev. B*, vol. 15, no. 12, pp. 5957–5962, 1977.

[59] E. F. Steigmeier and I. Kudman, "Acoustical-optical phonon scattering in Ge, Si, and III-V compounds," *Phys. Rev.*, vol. 141, no. 2, pp. 767–774, 1966.

[60] A. Cao, "Molecular dynamics simulation study on heat transport in monolayer graphene sheet with various geometries," *J. Appl. Phys.*, vol. 111, no. 8, p. 83528, 2012.

[61] D. Yang, F. Ma, Y. Sun, T. Hu, and K. Xu, "Influence of typical defects on thermal conductivity of graphene nanoribbons: An equilibrium molecular dynamics simulation," *Appl. Surf. Sci.*, vol. 258, no. 24, pp. 9926–9931, 2012.

[62] W. J. Evans, L. Hu, and P. Keblinski, "Thermal conductivity of graphene ribbons from equilibrium molecular dynamics: Effect of ribbon width, edge roughness, and hydrogen termination," *Appl. Phys. Lett.*, vol. 96, no. 20, p. 203112, 2010.

[63] M. Yamada, Y. Yamakita, and K. Ohno, "Phonon dispersions of hydrogenated and dehydrogenated carbon nanoribbons," *Phys. Rev. B*, vol. 77, no. 5, p. 54302, 2008.

[64] H. Cao, Z. Guo, H. Xiang, and X. Gong, "Layer and size dependence of thermal conductivity in multilayer graphene nanoribbons," *Phys. Lett. A*, vol. 376, no. 4, pp. 525–528, 2011.

[65] Y. Sonvane, S. K. Gupta, P. Raval, I. Lukacevic, and P. B. Thakor, "Length, width and roughness dependent thermal conductivity of graphene nanoribbons," *Chem. Phys. Lett.*, vol. 634, pp. 16–19, 2015.