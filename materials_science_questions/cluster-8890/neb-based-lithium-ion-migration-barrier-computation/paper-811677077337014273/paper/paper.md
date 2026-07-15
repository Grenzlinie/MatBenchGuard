# Electrical and Lithium Ion Dynamics in Three Main Components of Solid Electrolyte Interphase from Density Functional Theory Study

Y. C. Chen, $^{\dagger}$ C. C. Ouyang, $^{\ddagger,*}$ L. J. Song, $^{\S}$ and Z. L. Sun $^{\dagger,\S,*}$

$^{\dagger}$School of Chemistry and Chemical Engineering, Lanzhou University, Lanzhou 730000, People's Republic of China
$^{\ddagger}$Department of Physics, Jiangxi Normal University, Nanchang 330022, People's Republic of China
$^{\S}$Liaoning Key Laboratory of Petrochemical Engineering, Liaoning Shihua University, Liaoning 113001, People's Republic of China

**ABSTRACT**: $Li_2CO_3$, $Li_2O$, and LiF are three important inorganic components that build up the "compact" layer of the solid electrolyte interphase which adhere tightly to the graphite anode of lithium ion batteries. The electrical conductivity and the lithium ion diffusivity within this layer are relevant to the rate performance of the graphite anode. Using density functional theory, the electronic structures of the three compounds are calculated and lithium migration dynamics are simulated using nudged elastic band method. Results show that all three components have insulating electronic structures, while lithium vacancies create some strongly localized holes that do not contribute much to the electronic conduction. Lithium diffusion in $Li_2CO_3$ and $Li_2O$ can be very fast when lithium vacancies are available. The energy barriers of lithium migration in $Li_2CO_3$ (ranges from 0.227 to 0.491 eV) and $Li_2O$ (0.152 eV) are comparable to that in graphite with the help of vacancies. However, lithium migration in LiF (energy barrier 0.729 eV) is much slower even when there are lithium vacancies in the lattice.

![](./images/811677077337014273_1.jpg)

## 1. INTRODUCTION

The demand for lithium ion batteries has increased enormously as a power source for portable devices because of their excellent characteristics of high voltage, high energy density, and lightweight. Currently, large high power lithium ion batteries are expected to be used as the power supply of electrical vehicles. Graphite/carbon-based materials with good lithium ion diffusivity are extensively used as anodes for lithium ion batteries. The electrochemical behavior of the carbon anode in terms of rate performance and reversibility is affected by their surface characteristics. $^{1}$ It is reported that the high/low temperature performance $^{2}$ of the carbonaceous anodes and even the safety of the battery system $^{3}$ are strongly related to the solid electrolyte interphase (SEI), a surface passivating layer formed at lithium metal or carbonaceous anodes by a heterogeneous reaction between the electrolyte solvent and the anode. In the 1970s, Peled proposed the concept of SEI to explain the fact that lithium and other alkali metals are kinetically stable in certain solvents at moderate temperatures. $^{4,5}$ The SEI protects the anode from further reaction with the electrolyte solvent by decreasing the charge transfer from lithium metal to the molecule dissolved in the electrolyte. $^{6}$ Therefore, simple coating of the natural graphite with a $Li_2CO_3$ layer could improve its cycling performance. $^{7}$

In the past few years, many researchers have focused on the physical and chemical properties of the SEI. $^{8}$ Recently, Verma et al. $^{9}$ reviewed the key features of SEI in the performance of carbon anodes for lithium ion batteries. It is reported that there are mainly two mechanisms concerning the formation of SEI at the graphite surface, $^{10}$ which are sensitive to the surface morphology and orientation. $^{11}$ Furthermore, the content of the film is related to the intercalation state of the graphite anode. As reported by Zhang et al., $^{12}$ the first stage takes place before the intercalation of lithium ions into graphite and the SEI formed in this stage is structurally porous, highly resistive, and dimensionally unstable. The second stage occurs simultaneously with the intercalation of lithium ions and the resulting SEI layer is more compact. Dahn et al. reported that the thermal stability of the anode is related to the formation of SEI in carbon intercalation anodes. $^{13}$ Later, it was found that the thermal stability is related to the amount of LiF contained in the SEI. $^{14}$

The exact composition/content of SEI is still a debated topic in the literature. Generally, it is dependent on a number of factors, including the type of carbon anode, the surface morphology of the anode, the electrolyte composition (salt and solvent), and so on. $^{9}$ According to Zhang et al., the content of the SEI formed at the first stage is mainly porous organic products that are dimensionally unstable. At the second stage, stable inorganic products are formed and the SEI film becomes more compact. Furthermore, the stable and compact inorganic layer is adhered tightly to the surface of the electrode, while the porous organic layer extends further out from the electrode. $^{15,16}$ Although the major composition is still under debate and might be varied with different experimental conditions, it is sure that $Li_2CO_3$, $^{17}$ $Li_2O$, $^{18}$ and $LiF^{19}$ are three major inorganic species of the stable SEI formed at the second stage.

Although numerous studies have been focused on the SEI formation mechanism, content of the SEI film, role of the SEI to the performance of the batteries and so forth, little information is available in the literature concerning the lithium ion dynamics in

Received: December 23, 2010
Revised: January 28, 2011
Published: March 07, 2011

<table>
<caption>Table 1. Calculated Lattice Parameters, Valence Band (VB) Widths, Band Gaps of $Li_2CO_3$, $Li_2O$ and $LiF$$^{a}$</caption>
<thead>
<tr>
<th></th>
<th>lattice parameters (Å)</th>
<th>space group</th>
<th>VB width</th>
<th>band gap</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Li_2CO_3$</td>
<td>$a = 8.370$ $[8.358]^{b}$<br>$b = 4.929$ $[4.974]^{b}$<br>$c = 5.870$ $[6.194]^{b}$<br>$\beta = 117.10$ $[114.79^{\circ}]^{b}$</td>
<td>$C2/c$ (no. 15)</td>
<td>$2.6$ $[2.7]^{c}$</td>
<td>$4.7$ $[5.0]^{c}$</td>
</tr>
<tr>
<td>$Li_2O$</td>
<td>$a = 4.503$ $[4.601]^{d}$</td>
<td>$Fm3m$ (no. 225)</td>
<td>$3.0$ $[2.7]^{e}$</td>
<td>$4.7$ $[5.3]^{f}[6.6]^{g}$</td>
</tr>
<tr>
<td>$LiF$</td>
<td>$a = 3.910$ $[4.04 - 4.05]^{h}$</td>
<td>$Fm3m$ (no. 225)</td>
<td>$3.6$ $[3.4 - 3.7]^{i}$</td>
<td>$8.9$ $[10.0]^{j}$</td>
</tr>
</tbody>
</table>

$^{a}$ The values in parentheses are theoretical or experimental values from literature. $^{b}$ Experimental, from ref 37. $^{c}$ DFT calculation, from ref 38. $^{d}$ Experimental, from ref 39. $^{e}$ From ref 40. $^{f}$ DFT calculations, from ref 41. $^{g}$ Experimental, from ref 42. $^{h}$ Experimental and theoretical, from ref 43. $^{i}$ Experimental, from ref 44. $^{j}$ Theoretical, from ref 45.

the SEI. Namely, how lithium ions diffuse in the SEI is far from clear in the literature, except for some experimental determination of the diffusion coefficient from analysis of the electrochemical impedance spectroscopy data. $^{2,20,21}$ Experimentally, it is quite difficult to measure lithium diffusion in the thin multi-component SEI layer at the electrode surface. However, first principles calculations have demonstrated their powerful capability of predicting the lithium ion dynamics in electrode materials for lithium ion batteries. $^{22-24}$ Except for some first principles calculations that have been carried out to investigate the SEI formation mechanism, $^{25,26}$ little theoretical work was done to understand the lithium ion dynamics in SEI. Very recently, Iddir et al. studied interstitial lithium ion diffusion in $Li_2CO_3$ from first principles calculations. They found that interstitial lithium ion diffuses along the [010] plane with a very low energy barrier, while across the plane it is much more difficult. $^{27}$ However, as the SEI is formed in a dynamic electrochemical environment, it is known that the structure of the SEI is abundant of defects. In fact, as mentioned above, the outer part of the SEI is in a porous structure. Therefore, lithium diffusion with the help of vacancies could be more relevant. In the present work, with an aim of understanding the lithium ion dynamic performance in the SEI layer, we studied vacancy assisted lithium diffusion in three major inorganic components of the SEI: $Li_2CO_3$, $Li_2O$, and $LiF$, together with analysis of the electronic structures of the corresponding compounds.

## 2. COMPUTATIONAL DETAILS

All calculations reported herein were performed using the VASP (Vienna ab initio simulation package) code. $^{28,29}$ The core ion and valence electron interaction is described by the projector augmented-wave (PAW) method, $^{30}$ while the exchange-correlation part is described with generalized gradient approximation (GGA) by Perdew and Wang. $^{31}$ The valence electrons wave functions are expanded in plane wave basis sets with cutoff energies of 520 eV. To minimize the influence from the periodic boundary condition to the lithium diffusion, $2 \times 2 \times 2$ (LiF and $Li_2O$, both contain 32 formula units) and $1 \times 2 \times 2$ ($Li_2CO_3$, contains 16 formula units) supercell models are used. The convergence of the total energy with respect to the $k$-points sampling were carefully examined and finally $3 \times 3 \times 3$ (for LiF and $Li_2O$) and $4 \times 3 \times 3$ (for $Li_2CO_3$) Monkhorst-Pack $^{32}$ scheme $k$-point meshes are used for the $k$-points sampling in the Brillouin zone. The equilibrium lattice constant (see Table 1) was optimized by fitting the Murnaghan equation of state. $^{33}$ The atomic positions were fully relaxed and the final force on each atom was less than 0.005 eV/Å. The calculation of the density of states (DOS) was smeared by the Gaussian smearing method with a smearing width of 0.05 eV. Lithium ion diffusion is modeled in a system with one single lithium vacancy, the simplest and most common defect. Therefore, we manually remove one Li atom from the supercell and create one lithium vacancy. The migration pathway is optimized using the nudged elastic band (NEB) method, $^{34-36}$ with which the minimum energy paths together with the saddle points are calculated.

![](./images/811677077337014273_2.jpg)

Figure 1. Total density of states of $Li_2CO_3$, $Li_2O$, and LiF perfect bulk and bulk with one Li vacancy. The Fermi level is set to be zero in energy.

## 3. RESULTS AND DISCUSSION

3.1. Electronic Structure and Electrical Conduction. The electronic structures of the three typical inorganic compounds in SEI are first calculated. Total density of states (DOS) of $Li_2CO_3$, $Li_2O$, and LiF ideal bulk and bulk with one Li vacancy are shown in Figure 1. The $Li_2CO_3$, $Li_2O$ and LiF compounds are insulators, with energy gaps of about 4.7, 4.7, and 8.9 eV, respectively. Similar values have been reported in other theoretical works, as listed in Table 1. These theoretical predicted band gap values are all underestimated, due to the well-known intrinsic shortcoming of DFT calculations. $^{46}$ However, the strong insulating nature is very clear from our calculation, indicating that the dense and compact inorganic part of the SEI is highly prohibitive to electronic conduction. However, defects in these compounds might change the electronic structure around the Fermi level.

![](./images/811677077337014273_3.jpg)

Figure 2. Atomic projected density of states on O-2p states of (a) an O in $Li_{2}CO_{3}$ perfect lattice and (b) O near the vacancy in $Li_{2}CO_{3}$ with one Li vacancy. The Fermi level is set to be zero in energy.

![](./images/811677077337014273_4.jpg)

Figure 3. The iso-surfaces of the differential charge density of $Li_{2}CO_{3}$ (a), $Li_{2}O$ (b), and LiF (c). The green (small) and red (large) spheres are Li and O atoms, respectively. The black spheres in (a) and (c) are C and F atoms, respectively. White spheres in all cases indicate the Li vacancy position.

After removing one Li atom from the supercell, the Li vacancy produces some holes near the Fermi level. However, those defect states (holes) are strongly localized. The projected DOS (PDOS) shows that those holes are contributed by the nearest neighboring O or F atoms to the Li vacancy.

The PDOS of O atom near the Li vacancy in $Li_{2}CO_{3}$ are given in Figure 2. The O-2p states move up and cross the Fermi level after the Li atom is removed from the supercell, creating holes in the system. However, except for the nearest neighbor O atoms, Li vacancy does not change the electronic structure of other O atoms. Similar results are also observed in $Li_{2}O$ and LiF when Li vacancies are created. As the holes are strongly localized to those nearest neighboring O (or F in LiF) atoms next to the vacancy, they do not contribute much to the electronic conduction. Therefore, the electronic conduction is still very poor in the SEI film, although there are defect states around the Fermi level.

The strongly localized effect of those defect states can be directly viewed from a differential charge density analysis. Figure 3 gives the differential charge density of the three considered compounds defined as the charge density difference of the perfect supercell and the supercell with one Li vacancy. From this definition, integration of the differential charge density over the supercell obtains 1 e, which is the amount of charge removed from the system after one Li vacancy is created. That charge is donated by the nearest neighbor O (or F) atoms (see Figure 3) and holes are created accordingly. Except for the nearest neighboring O (or F) atoms, no contributions are observed from other atoms, which is in accordance with the above-mentioned DOS analysis.

![](./images/811677077337014273_5.jpg)

Figure 4. Energy profiles and migration pathways of single lithium migration in $Li_{2}CO_{3}$. Parts (a)−(e) are the corresponding migration energy profiles of the lithium ion diffusion along migration pathways from Nos. 1−5 that are schematically shown in part (f). The gray, red, and green spheres are C, O, and Li atoms, respectively. The migration pathways are marked with arrows.

### 3.2. Li Diffusion in $Li_{2}CO_{3}$, $Li_{2}O$, and LiF.
As there are many defects in the SEI film, diffusion of lithium in the SEI can always take advantage of those defects. In the present work, we focus on the lithium diffusion in bulk $Li_{2}CO_{3}$, $Li_{2}O$, and LiF with the help of lithium vacancies (the simplest defect in the bulk). When one lithium vacancy is created by removing one Li from the ideal supercell, lithium diffusion in the system can be represented by position exchange of the lithium ion and the vacancy.

Figure 4f schematically shows the possible migration pathways for single lithium diffusion in the $Li_{2}CO_{3}$ lattice with the help of the lithium vacancy. There are five (symmetrically identical pathways are not considered) different migration pathways for lithium diffuses to nearby vacancy site, which are numbered 1−5 in Figure 4. These migration pathways build up a three-dimensional migration network for lithium diffusion. Figure 4a−e are the corresponding optimized migration energy barriers for lithium diffusion along pathways of Nos. 1−5. The energy barriers of those pathways are not quite different from each other. The lowest energy barrier is about 0.227 eV along pathway No. 3, and the highest energy barrier is about 0.491 eV when lithium diffuses along pathway No. 1. It is important to mention that lithium can be diffused without significant changes to the lattice, only small atomic relaxations of the nearby atoms are observed at the transition state. The energy profiles along migration pathway Nos. 2 and 3 are not symmetrical, because the migration pathways are not symmetrical. To have a better look to the asymmetrical migration pathway with lowest migration energy barrier,

![](./images/811677077337014273_6.jpg)

Figure 5. Energy profiles and migration pathways of single lithium migration in $Li_2O$. Parts (a)−(c) are the corresponding migration energy profiles of the lithium diffusion along the migration pathways from Nos. 1−3 shown in (d). The red and green spheres are O and Li atoms, respectively. The white sphere indicates the Li vacancy position. The migration pathways are marked with arrows.

five intermediate images are used for pathway No. 3, whereas only three images are used for all other pathways. Apart from the different energy profiles along different migration pathways, those energy barriers are all quite small, indicating that lithium is able to diffuse very quickly through the $Li_2CO_3$ compound when vacancies are available in the lattice. Comparing with the migration energy barrier of 0.28 eV for interstitials Li ion diffusion along the [010] plane in $Li_2CO_3$ reported in ref 27 vacancy does not contribute much to the lithium diffusivity (see Figure 4c,d), although the energy barrier is slightly decreased. However, the energy barrier for lithium migration across the [010] plane is substantially decreased (see Figure 4a,b,e), compared to the 0.60 eV value reported in ref 27.

Migration pathways in $Li_2O$ and LiF are simpler than pathways in $Li_2CO_3$. Within the $Li_2O$ lattice, Li sites form a simple cubic structure. Therefore, three independent pathways are considered and numbered 1−3 in Figure 5d: migration along anyone of the diagonal faces (Path-1), the diagonal body (Path-2), and anyone of the cubic edges (Path-3). However, the results show that the lithium migration energy barriers of pathway Nos. 1 and 2 are very high, which makes lithium diffusion along those pathways very difficult. On the contrary, migration along the cubic edge is very easy, with a very small energy barrier of 0.152 eV. As the vacancy is surrounded by six Li atoms that are all along the cubic edge, vacancies can be diffused very quickly in a three-dimensional network in the $Li_2O$ compound. In the case of LiF, the Li vacancy is surrounded by twelve nearest neighboring Li atoms, which are all symmetrically equivalent (see Figure 6). Therefore, only one of them is simulated with the NEB calculation. The results show that the migration energy barrier is about 0.729 eV, which is very high for lithium diffusion at room temperatures.

The large energy barrier difference of lithium migration along different migration path in $Li_2O$ is interesting. $Li_2O$ is a typical ionic compound, which binds tightly through electrostatic interactions among $Li^+$ and $O^{2-}$. In the symmetrical atomic lattice, each ion is in an equilibrium position, where the attraction and repulsion forces from other ions are completely canceled. The creation of one Li vacancy breaks down the equilibrium, and the nearby atoms undergo relaxations until the system reaches a new equilibrium. In order to reach a new equilibrium, charge redistribution is necessary around nearby atoms, which results in certain polarization to those nearby atoms around the vacancy. When the lithium ion migrates along a pathway to which the nearby atoms are more symmetric, the migration is then less difficult. However, when the nearby atoms are less symmetric, the movement of lithium ion will induce more polarization to them, which in turn increases the electrostatic energy. As schematically shown in the inset of Figure 7, two nearest neighboring O atoms are symmetric to migration Path-3, while there are three O atoms that are not symmetric to Path-1. We mention here that Li atoms are also symmetric to Path-3, although only the moving Li atom (vacancy) is shown in Figure 7. The polarization effect can also be demonstrated by the projected DOS. As shown in Figure 7a, the DOS shifts to a higher energy level when the lithium moves from initial state (IMG-0 in Figure 7a) to the transition state (IMG-2 in Figure 7a). On the contrary, this shift is reversed in Figure 7b (refer to the two

![](./images/811677077337014273_7.jpg)

Figure 6. Energy profile and migration pathway (inset) of single lithium migration in LiF. The gray and green spheres are F and Li atoms, respectively. The white sphere indicates the position of the Li vacancy.

![](./images/811677077337014273_8.jpg)

Figure 7. Atomic projected density of states on O-2p states of nearest neighboring O atoms of three images along path-1 (a) and path-3 (b). The atomic positions of the moving lithium and the nearby O atoms are schematically shown by the inset. Red (large) and green (small) cycles denotes O and Li atoms, respectively. The numbers given in the inset are distances (in Å) between the moving lithium and the neighboring O atoms.

arrows in Figure 7), indicating that the polarization of the nearest neighboring O atoms is slightly decreased during the lithium migration along Path-3.

According to the energy barriers obtained from NEB calculations, we may conclude that lithium diffusion in $Li_2CO_3$ and $Li_2O$ can be very fast. The lithium migration energy barriers in them are comparable to lithium migrations in electrode materials. From NEB calculations, the energy barrier for lithium migration along the $XY$-plane in graphite ranges from 0.308 to 0.400 eV in $Li_xC_6$ for different $x$ values. $^{47}$ As the energy barriers for lithium diffusion in $Li_2CO_3$ are very close to the energy barrier for Li diffusion in graphite and the energy barriers are even lower (0.152 eV) in $Li_2O$, lithium diffusion through the SEI seems not to be a problem in affecting the rate performance of the battery. However, when the amount of LiF is high in the SEI, the situation could be changed, since the energy barrier for lithium migration in LiF (0.729 eV) is much higher than lithium migration in graphite. Experimentally, it is reported that the activation energy for lithium diffusion in the SEI ranges from 0.37 to 0.67 eV, $^{2,20,21,48,49}$ depending on factors like the charge/discharge state, the operating temperature, the content of the electrolyte, et al. Therefore, quantitative comparison of the experimental data with our calculated energy barrier is not possible. However, qualitatively, our data are in good agreement with those experimental findings. Furthermore, as the energy barrier for lithium diffusion in LiF is substantially higher than in $Li_2CO_3$ and $Li_2O$, it is reasonable to think that low lithium diffusivity could be a side evidence of more amount of LiF in the SEI when other conditions are similar.

## 4. CONCLUSIONS
Through electronic structure analysis and simulation of lithium migration in three inorganic compounds $Li_2CO_3$, $Li_2O$, and LiF, we have investigated the influence of the SEI to the dynamic (rate) performance of the graphite anodes. Our results support the general conclusion that SEI is prohibitive to electronic conduction. The electronic structures of the three species are all insulated with a large forbidden band gap. Although Li vacancies create holes near the Fermi level, those holes are strongly localized to those anions (O or F) that are nearest neighbors of the vacancy, and therefore, contribute little to the electronic conduction. However, lithium diffusion in $Li_2CO_3$ and $Li_2O$ is very fast with the help of Li vacancies. The energy barriers for single lithium diffusion in $Li_2CO_3$ and $Li_2O$ are close to (or even somewhat smaller than) that of lithium diffusion in bulk graphite. However, lithium diffusion in LiF is more difficult than in $Li_2CO_3$ and $Li_2O$, since the calculated lithium diffusion energy barrier is about 0.729 eV, much higher than diffusion in graphite.

## AUTHOR INFORMATION
### Corresponding Author
*E-mail: cyouyang@jxnu.edu.cn; zlsun56@hotmail.com.

## ACKNOWLEDGMENT
This work was supported by the NSFC under Grant No. 11064004, Science Foundation from Department of Education of Jiangxi Province under Grant No. GJJ10398. C.Y.O. is also supported by the Scientific Research Foundation for the Returned Overseas Chinese Scholars.

## REFERENCES
(1) Chusid, O.; Ely, Y.; Aurbach, D.; Babai, M.; Carmeli, Y. J. Power Sources 1993, 43, 47.
(2) Churikov, A. V. Electrochim. Acta 2001, 46, 2415.
(3) Park, G.; Nakamura, H.; Lee, Y.; Yoshio, M. J. Power Sources 2009, 189, 602.
(4) Peled, E.; Straze, H. J. Electrochem. Soc. 1977, 124, 1030.
(5) Peled, E. J. Electrochem. Soc. 1979, 126, 2047.
(6) Peled, E.; Golodnitsky, D.; Ardel, G. J. Electrochem. Soc. 1997, 144, L208.
(7) Zhang, S. S.; Xu, K.; Jow, T. R. Electrochem. Commun. 2003, 5, 979.
(8) Balbuena, P. B.; Wang, Y. Lithium Ion Batteries: Solid Electrolyte Interphase; Imperial College Press: London, 2004.
(9) Verma, P.; Maire, P.; Novák, P. Electrochim. Acta 2010, 55, 6632.
(10) Zhang, S. S. J. Power Sources 2006, 162, 1379.
(11) Aurbach, D.; Ein-Eli, Y. J. Electrochem. Soc. 1995, 142, 1746.
(12) Zhang, S. S.; Xu, K.; Jow, T. R. Electrochim. Acta 2006, 51, 1636.
(13) Sacken, U.; von; Nodwell, E.; Sundher, A.; Dahn, J. R. Solid State Ionics 1994, 69, 284.
(14) Herstedt, M.; Stjerndahl, M.; Gustafsson, T.; Edström, K. Electrochem. Commun. 2003, 5, 467.
(15) Edström, K.; Herstedt, M.; Abraham, D. P. J. Power Sources 2006, 153, 380.
(16) Andersson, A. M.; Henningsson, A.; Siegbahn, H.; Jansson, U.; Edstrom, K. J. Power Sources 2003, 119−121, 522.
(17) Aurbach, D.; Zaban, A. J. Electroanal. Chem. 1993, 348, 155.
(18) Morigaki, K. I.; Ohta, A. J. Power Sources 1998, 76, 159.
(19) Peled, E.; Golodnitsky, D.; Menachem, C.; Bar-Tow, D. J. Electrochem. Soc. 1998, 145, 3482.
(20) Schranzhofer, H.; Bugajski, J.; Santner, H. J.; Korepp, C.; Möller, K. C.; Besenhard, J. O.; Winter, M.; Sitte, W. J. Power Sources 2006, 153, 391.
(21) Levi, M. D.; Wang, C.; Aurbach, D. J. Electrochem. Soc. 2004, 151, A781.
(22) Ouyang, C. Y.; Shi, S. Q.; Fang, Q.; Lei, M. S. J. Power Sources 2008, 175, 891.
(23) Ouyang, C. Y.; Shi, S. Q.; Wang, Z. X.; Li, H.; Huang, X. J.; Chen, L. Q. J. Phys: Condens. Matter 2004, 16, 2265.
(24) Ouyang, C. Y.; Zeng, X. M.; Sljivancanin, Z.; Baldereschi, A. J. Phys. Chem. C 2010, 114, 4756.
(25) Tasaki, K.; Kanda, K.; Kobayashi, T.; Nakamura, S.; Ue, M. J. Electrochem. Soc. 2006, 153, A2192.
(26) Leung, K.; Budzien, J. L. Phys. Chem. Chem. Phys. 2010, 12, 6583.
(27) Iddir, H.; Curtiss, L. A. J. Phys. Chem. C 2010, 114, 20903.
(28) Kresse, G.; Hafner, J. Phys. Rev. B 1993, 47, 558.
(29) Kresse, G.; Furthmuller, J. Comput. Mater. Sci. 1996, 6, 15.
(30) Blöchl, P. E. Phys. Rev. B 1994, 50, 17953.
(31) Wang, Y.; Perdew, J. P. Phys. Rev. B 1991, 44, 13298.
(32) Monkhorst, H. J.; Pack, J. D. Phys. Rev. B 1976, 13, 5188.
(33) Fu, C. L.; Hu, K. M. Phys. Rev. B 1983, 28, 5480.
(34) Henkelman, G.; Uberuaga, B. P.; Jonsson, H. J. Chem. Phys. 2000, 113, 9901.
(35) Henkelman, G.; Jonsson, H. J. Chem. Phys. 2000, 113, 9978.
(36) Sheppard, D.; Terrell, R.; Henkelman, G. J. Chem. Phys. 2008, 128, 134106.
(37) Idemoto, Y.; Richardson, J. W.; Koura, N.; Kohara, S.; Loong, C. K. J. Phys. Chem. Solids 1998, 59, 363.
(38) Zhuravlev, Y. N.; Fedorov, I. A. J. Struct. Chem. 2006, 47, 206.
(39) Hull, S.; Farley, T.W. D.; Hayes, W.; Hutchings, M. T. J. Nucl. Mater. 1988, 160, 125.
(40) Mikajlo, E. A.; Nixon, K. L.; Coleman, V. A.; Ford, M. J. J. Phys.: Condens. Matter 2002, 14, 3587.
(41) Albrecht, S.; Onida, G.; Reining, L. Phys. Rev. B 1997, 55, 10278.
(42) Ishii, Y.; Murakami, J.; Itoh, M. J. Phys. Soc. Jpn. 1999, 68, 696.

7048
dx.doi.org/10.1021/jp112202s | J. Phys. Chem. C 2011, 115, 7044−7049

(43) Cortona, P. *Phys. Rev. B* **1992**, *46*, 2008.

(44) Poole, R. T.; Jenkin, J. G.; Liesegang, J.; Leckey, R. C. G. *Phy. Rev. B* **1975**, *11*, 5179.

(45) Carlsson, A. E. *Phys. Rev. B* **1985**, *31*, 5178.

(46) Fiorentini, V.; Baldereschi, A. *Phys. Rev. B* **1995**, *51*, 17196.

(47) Persson, K.; Sethuraman, V. A.; Hardwick, L. J.; Hinuma, Y.; Meng, Y. S.; Ven, A.; van der; Srinivasan, V.; Kostecki, R.; Ceder, G. *J. Phys. Chem. Lett.* **2010**, *1*, 1176.

(48) Geronov, Y.; Schwager, F.; Muller, R. H. *J. Electrochem. Soc.* **1982**, *129*, 1422.

(49) Verbrugge, M. W.; Koch, B. J. *J. Electrochem. Soc.* **1994**, *141*, 3053.