![](./images/814675966092640257_1.jpg)

# Thermal transport behavior of polycrystalline graphene: A molecular dynamics study

P. H. Wu, S. S. Quek, Z. D. Sha, Z. L. Dong, X. J. Liu, G. Zhang, Q. X. Pei, and Y. W. Zhang

Citation: *Journal of Applied Physics* **116**, 204303 (2014); doi: 10.1063/1.4902852
View online: http://dx.doi.org/10.1063/1.4902852
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/116/20?ver=pdfcov
Published by the AIP Publishing

## Articles you may be interested in

**Thermal conductivity of sawtooth-like graphene nanoribbons: A molecular dynamics study**
J. Appl. Phys. **112**, 123508 (2012); 10.1063/1.4768445

**Study on the mechanical behavior of tilt bicrystal graphene by molecular dynamics simulations: Bulk verse nanoribbons**
J. Appl. Phys. **112**, 043519 (2012); 10.1063/1.4749812

**Molecular dynamics simulation study on heat transport in monolayer graphene sheet with various geometries**
J. Appl. Phys. **111**, 083528 (2012); 10.1063/1.4705510

**Interface thermal resistance and thermal rectification in hybrid graphene-graphane nanoribbons: A nonequilibrium molecular dynamics study**
Appl. Phys. Lett. **99**, 051917 (2011); 10.1063/1.3622480

**Chirality and thickness-dependent thermal conductivity of few-layer graphene: A molecular dynamics study**
Appl. Phys. Lett. **98**, 113107 (2011); 10.1063/1.3567415

![](./images/814675966092640257_2.jpg)

[This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to ] IP: 155.97.178.73 On: Sun, 30 Nov 2014 21:24:20

JOURNAL OF APPLIED PHYSICS 116, 204303 (2014)
![](./images/814675966092640257_3.jpg)

# Thermal transport behavior of polycrystalline graphene: A molecular dynamics study

P. H. Wu, $^{1,2}$ S. S. Quek, $^{1}$ Z. D. Sha, $^{3}$ Z. L. Dong, $^{2}$ X. J. Liu, $^{1}$ G. Zhang, $^{1}$ Q. X. Pei, $^{1,a)}$ and Y. W. Zhang $^{1,b)}$

$^{1}$ Institute of High Performance Computing, A*STAR, 1 Fusionopolis Way, Singapore 138632
$^{2}$ School of Materials Science and Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798
$^{3}$ International Center for Applied Mechanics, State Key Laboratory for Strength and Vibration of Mechanical Structures, Xi' an Jiaotong University, Xi' an 710049, China

(Received 15 July 2014; accepted 15 November 2014; published online 25 November 2014)

The thermal transport behavior of polycrystalline graphene is studied using molecular dynamics simulations, with focus on the effects of grain size, tensile strain, and temperature on the thermal conductivity. All the simulation samples have the same overall dimensions of $30 \times 30$ nm with average grain sizes ranging from 2.5 to 12.5 nm. It is found that polycrystalline graphene exhibits a significant reduction in thermal conductivity compared to single-crystalline graphene, and the smaller the grain size is, the more the thermal conductivity drops. The thermal conductivity of polycrystalline graphene with average grain size of 2.5 nm is only about 20% of single-crystalline graphene. However, the thermal conductivity of polycrystalline graphene is less sensitive to both the applied strain and temperature than that of single-crystalline graphene. The underlying mechanisms for the differences in thermal behavior are examined and discussed. These findings are important for the thermal management of graphene-based devices. © 2014 AIP Publishing LLC.
[http://dx.doi.org/10.1063/1.4902852]

## I. INTRODUCTION
Graphene, a two-dimensional (2D) material consisting of a monolayer of $sp^{2}$ bonded carbon atoms, has attracted great interest in recent years due to its novel electronic properties, and superior mechanical and thermal properties. $^{1-4}$ With those exceptional properties, graphene has many potential applications such as in electronics, $^{5}$ sensors, $^{6}$ thermal management, $^{7,8}$ and energy storage. $^{9}$ For practical applications of graphene, it is important that the fabrication process is able to produce large-sized graphene sheets efficiently. Chemical vapor deposition (CVD) growth of graphene on metal foils appears to be one of the most promising routes to produce large graphene sheets. $^{10-13}$ However, polycrystalline graphene rather than single-crystalline graphene is often formed during the CVD growth. The grain boundaries (GBs) in polycrystalline graphene were shown to have a strong effect on the thermal transport in the graphene sheet. $^{14,15}$ Therefore, a complete understanding of the thermal properties of CVD-grown polycrystalline graphene sheets is important for the thermal applications of graphene.

Based on a bi-crystalline graphene model, the heat transport across the grain boundary was studied using non-equilibrium molecular dynamics (NEMD) simulations and non-equilibrium Green's function (NEGF). $^{14-18}$ Bagri et al. $^{14}$ observed a sharp temperature jump at the GB and found that the boundary conductance is significantly higher than that of other thermoelectric interfaces. Cao et al. $^{15}$ found that the boundary conductance is inversely proportional to the number of dislocations per length of grain boundaries. Lu et al. $^{16}$ further showed that the zigzag-oriented symmetric GB has the highest thermal conductance, and the out-of-plane mode is dominant in thermal transport in graphene GBs. The effect of strain on the thermal conductance of graphene GB was reported by Tang et al., $^{18}$ who found that the boundary thermal conductance shows a significant decrease under biaxial tension strain. While the above studies on bi-crystalline graphene provided us with much insight into the effects of GB on the thermal transport, their results may not be sufficient to describe the thermal transport in a polycrystalline graphene due to the diversity of GB structures and the presence of GB junctions. Recently, Wang et al. $^{19}$ developed an MD model of polycrystalline graphene to investigate the effects of grain size, alignment, and temperature on the thermal conductivity of polycrystalline graphene. The effective thermal conductivity was found to increase with the grain size and decrease with the misorientation angle and dislocation density at the GBs. However, their polycrystalline model only adopted equal-sized hexagonal grains, which is quite different from the structure of experimentally observed polycrystalline graphene, where the grains show various geometries. Although a very recent work by Mortazavi et al. $^{20}$ used a more realistic MD model for polycrystalline graphene, only the grain size effect was studied in their work. A more comprehensive study on the thermal conductivity of polycrystalline graphene is still lacking. In this work, we developed a realistic polycrystalline graphene model similar to that in Refs. 20 and 21 and performed systematic molecular dynamics simulations to investigate the effects of grain size, external tensile strain, and temperature on the thermal conductivity of polycrystalline graphene.

a)Electronic mail: peiqx@ihpc.a-star.edu.sg.
b)Electronic mail: zhangyw@ihpc.a-star.edu.sg.

0021-8979/2014/116(20)/204303/6/$30.00
116, 204303-1
© 2014 AIP Publishing LLC

## II. SIMULATION METHOD

The polycrystalline graphene structures are generated using the Voronoi tessellation method. $^{22,23}$ All the samples have the same overall dimensions of $30 \times 30$ nm with average grain sizes ranging from 2.5 to 12.5 nm. The Voronoi tessellation is implemented by first picking a random center position for each grain, and then placing/growing atoms out from this center position in the usual hexagonal crystal structure (oriented randomly between 0 rad and $\pi/3$ rad). Constructed in this random manner, the GBs contain a higher degree of disorder (i.e., more than just heptagon-pentagon pairs) than GBs of graphene films produced by micro-mechanical cleavage of highly oriented pyrolytic graphite. This kind of GB structures have been routinely reported in CVD grown graphene. $^{10,24}$ The created polycrystalline structure is annealed at a high temperature of 3000 K for 50 ps by performing MD simulation in constant volume and constant temperature (NVT) ensemble. The high mobility of carbon atoms at 3000 K allows rearrangement of atom positions, so that the unusually low or high atomic density regions at the GBs can be eliminated. Then the sample is cooled down to room temperature and subsequently equilibrated at 300 K for 10 ps. The sample is further relaxed to zero stress at room temperature in constant pressure and constant temperature (NPT) ensemble for another 10 ps. After that, the system is switched to constant volume and constant energy (NVE) ensemble for thermal conductivity calculation.

The MD simulations are performed using the software Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) $^{25}$ with a time step of 0.1 fs for the integration of the equations for atomic motion. Periodic boundary conditions are imposed along the two in-plane directions, and the adaptive intermolecular reactive bond order (AIREBO) potential $^{26}$ is employed to describe the interactions between carbon atoms. The thermal conductivity is calculated using the reverse non-equilibrium molecular dynamics (RNEMD). $^{27}$ To do so, we divide the sample into 60 slabs along the x direction, which is one of the two in-plane directions. We define the middle slab as the hot region and two end slabs as the cold region. By continuously adding a small heat $\Delta \varepsilon$ to the hot region and removing it from the cold region, a heat flux from the hot region to the cold region is generated in the sample (see Fig. 1). The heat flux is calculated by

$$
J=\frac{\Delta \varepsilon}{2 A \Delta t}, \tag{1}
$$

where $J$ is the heat flux, $A$ is the cross-sectional area, and $\Delta t$ is the time step. The factor of 2 accounts for the fact that the heat current propagates in two directions away from the hot region. To obtain the temperature gradient in the sample along the x direction, the temperature in each slab is calculated based on the velocities of atoms inside that slab by

$$
T_{i}=\frac{1}{3 N_{i} k_{B}} \sum_{j=1}^{N_{i}} m_{j} v_{j}^{2}, \tag{2}
$$

where $N_i$ is the number of atoms in slab $i$, $m_j$, and $v_j$ are the mass and velocity of atom $j$ in the slab, and $k_B$ is the Boltzmann constant. After the heat flux is imposed, we first run $10^6$ time steps to allow the heat transport to reach steady state. Then, we run another $2 \times 10^6$ time steps to obtain the time-averaged temperature profile of the system, which is used to calculate the temperature gradient $\delta T/\delta x$. Based on Fourier's law of heat conduction, the thermal conductivity $K$ is calculated as

$$
K=\frac{J}{\partial T / \partial x}=\frac{\Delta \varepsilon}{2 A \Delta t(\partial T / \partial x)}. \tag{3}
$$

The calculation is repeated for another in-plane direction and the thermal conductivity of the polycrystalline graphene is taken as the average of the two directions.

![](./images/814675966092640257_4.jpg)

FIG. 1. Schematic of the simulation model for the non-equilibrium molecular dynamics. A small amount of heat is repeatedly added into the hot region and removed from the cold regions to create the heat fluxes. Periodic boundary conditions are applied in both the $x$ and $y$ directions.

## III. RESULTS AND DISCUSSION

### A. Grain size effect

We first study the grain size effect on thermal conductivity. The calculated thermal conductivities at room temperature for the samples with different average grain sizes are shown in Fig. 2. The normalized thermal conductivities, together with GB atom fractions, at different average grain sizes are listed in Table I. Here, the thermal conductivities are normalized with respect to the thermal conductivity of

![](./images/814675966092640257_5.jpg)

FIG. 2. Thermal conductivity of polycrystalline graphene sheets as a function of grain size. The thermal conductivity of polycrystalline graphene $K$ is normalized by the thermal conductivity of SC graphene $K_0$. The inset shows a typical structure of polycrystalline graphene with grain size of 10 nm.

<table><caption>TABLE I. The thermal conductivity and the density of grain boundary atoms in polycrystalline graphene samples of different grain sizes.</caption>
<thead>
<tr>
<th>Grain size (nm)</th>
<th>GB atoms (%)</th>
<th>K/K₀</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.5</td>
<td>19.5</td>
<td>0.19</td>
</tr>
<tr>
<td>5</td>
<td>10.7</td>
<td>0.32</td>
</tr>
<tr>
<td>7.5</td>
<td>7.6</td>
<td>0.39</td>
</tr>
<tr>
<td>10</td>
<td>6.1</td>
<td>0.47</td>
</tr>
<tr>
<td>12.5</td>
<td>4.9</td>
<td>0.57</td>
</tr>
</tbody>
</table>

single-crystalline (SC) graphene since the absolute value of calculated thermal conductivity depends on the model size and interatomic potential used.¹⁴,²⁸⁻³³ It should be noted that the sample sizes in MD simulations are smaller than the phonon mean-free-path of graphene (~775 nm), the contribution from the long-wavelength phonon to the thermal conductivity is lost in MD simulations. Chen et al.³⁴ used a Klemens-type analytical model to estimate the long-wavelength phonon contribution to the thermal conductivity, so that their MD simulated thermal conductivities based on nano-meter size samples can be corrected to match with the measured ones based on micro-meter size samples.

It can be seen from Fig. 2 that the thermal conductivity of polycrystalline graphene decreases sharply as the grain size decreases. For the polycrystalline graphene with grain size of 10 nm, the thermal conductivity is about 50% of single-crystalline graphene. While for the polycrystalline graphene with a smaller grain size of 2.5 nm, the thermal conductivity is only about 20% of single-crystalline graphene. This dramatic reduction in thermal conductivity can be attributed to the increase in the fraction of GB atoms. It is known that GBs are crystallographic defects which distort the regular lattice structure. A polycrystalline graphene with a smaller grain size has a higher density of GB atoms, and thus, a higher defect density. It is also known from Boltzmann transport theory that a material with a higher defect density has a higher probability in phonon scattering, leading to a shorter phonon relaxation time,¹⁵,³⁵ and thus, a lower thermal conductivity.

Our calculations shown in Fig. 2 clearly indicate a linear relation between the thermal conductivity and the average grain size in the range of 2.5 nm to 12.5 nm. Hence, we consider the polycrystalline graphene as a two-phase composite consisting of the disordered GB phase and the ordered grain interior phase. The thermal resistance of the composite can be written as

$$
R_{Poly} = R_{GB} + R_{GI}, \tag{4}
$$

where $R_{Poly}$ is the thermal resistance of polycrystalline graphene, $R_{GB}$ is the thermal resistance of GB, and $R_{GI}$ is the thermal resistance of the grain interior.

Equation (4) can also be written as

$$
\frac{1}{K_{Poly}} = \frac{C_{GB}}{K_{GB}} + \frac{1 - C_{GB}}{K_{GI}}, \tag{5}
$$

where $K_{Poly}$ is the thermal conductivity of polycrystalline graphene, $K_{GB}$ is the thermal conductivity of GB phase, $K_{GI}$ is the thermal conductivity of grain interior phase, and $C_{GB}$ is the percentage of GB atoms. Based on Eq. (5) and Table I, we can deduce that the thermal conductivity ratio of the GB phase over the grain interior phase, $K_{GB}/K_{GI}$, which is found to be around 0.05. Hence, the thermal conductivity of the GB phase is only about 5% of the grain interior phase. This prediction is in line with previous studies³⁶⁻³⁸ that the presence of various defects in graphene could greatly reduce its thermal conductivity.

In order to look further into the underlying mechanism for the reduction in thermal conductivity of polycrystalline graphene, we calculate the phonon density of states (PDOS) of the graphene sheets. The vibrational spectrum $g(\omega)$ of a graphene sheet can be found by taking the Fourier transform of the velocity autocorrelation function for all the carbon atoms in the system

$$
g(\omega) = \frac{1}{\sqrt{2\pi}} \int e^{i\omega t} \frac{\langle v(t) v(0) \rangle}{\langle v(0) v(0) \rangle} dt. \tag{6}
$$

The PDOS is then calculated as $PDOS = [g(\omega)]^2$. The calculated PDOS curves of single-crystalline and polycrystalline graphene sheets are shown in Fig. 3. It can be seen that the location of the peaks, such as the peaks at 48 THz (G peak), is the same for both the single-crystalline and polycrystalline graphene sheets, however, the peak magnitudes are different at different grain sizes. This means that the increase in GB density does not change the peak location of phonon spectrum of graphene. Our calculations show that although the C-C bonds in GBs can be in tension or compression, the average C-C bond length is more or less the same as that in grain interior. This may explain why the peak position is unchanged. However, the peaks become more flattened with the decrease of the grain size, which suggests that the increased GB density reduces the density of phonon modes. The flattening of the phonon mode peaks can be attributed to the widened range of C-C bond length arising from bond compression and tension at GB, causing a reduction in phonon life-time and thus, a reduction in thermal conductivity.

![](./images/814675966092640257_6.jpg)

FIG. 3. The calculated PDOS of single-crystalline and polycrystalline graphene with different average grain sizes.

### B. Strain effect

Next, we study the effect of strain on the thermal conductivity. Strain can be used to modify and tune the electronic properties of graphene $^{39,40}$—bandgap engineering. Therefore, one of the ways of using graphene in semiconductor-based electronic devices is through the application of strain. As such, the effect of strain on the thermal conductivity of graphene is also important in terms of the heat dissipation of these potential devices and has been studied recently for single-crystalline graphene. $^{41}$ However, the effect of strain on the thermal conductivity of polycrystalline graphene remains unexplored.

To study the effect of strain on the thermal conductivity, we varied the strain from 0 to 0.12 with a step size of 0.03 and ran MD simulations at each strain level to calculate the thermal conductivity. The simulated thermal conductivities of single-crystalline and polycrystalline graphene sheets at different strains are shown in Fig. 4. It can be seen in general that the thermal conductivity of graphene decreases with increasing strain. When the strain is increased to 0.12, the thermal conductivity of single crystalline graphene drops by 57%. However, it is interesting to note that the tensile strain has a relatively smaller effect on polycrystalline graphene. For example, at the strain of 0.12, the thermal conductivity undergoes relatively smaller drops of 41% and 32% for the polycrystalline graphene with grain sizes of 7.5 nm and 2.5 nm, respectively.

The phonon spectra of the single-crystalline and polycrystalline graphene sheets under different strains are calculated and shown in Fig. 5. The phonon spectra show that the G-bands exhibit obvious redshift. This redshift is caused by the collective changes in C-C bond length upon applying the tensile strain for both single-crystalline and polycrystalline graphene, leading to phonon softening. This strain-induced phonon softening could decrease the phonon group velocities and result in a lower thermal conductivity. $^{41,42}$ In addition to the phonon softening, it can also be observed from Figs. 5(a)-5(c) that tensile strain results in a lower density of phonon states, indicating that the life-time of phonons is shorter. The reduced phonon life-time also results in a lower thermal conductivity. Therefore, the lower thermal conductivity in strained single-crystalline and polycrystalline graphene could be attributed to both the phonon softening and shorter phonon life-time.

It can also be seen from Fig. 5 that the strain-induced variation of phonon spectra is different for different grain sizes. The change in phonon spectra for the smaller grain size (Fig. 5(c)) is not as significant as that of larger grain size (Fig. 5(b)) and that of single-crystalline graphene (Fig. 5(a)). Although there is a similar redshift of the G peaks for both single-crystalline and polycrystalline graphene, the peaks are broadened for polycrystalline graphene, in particular for polycrystalline graphene with a smaller grain size. This could explain why the thermal conductivity of polycrystalline graphene of a smaller grain size is less sensitive to the tensile strain than that of larger grain size and single-crystalline graphene.

![](./images/814675966092640257_7.jpg)

FIG. 4. The thermal conductivities of SC and polycrystalline graphene as a function of tensile strain. 2.5 nm and 7.5 nm are the average grain sizes for polycrystalline graphene.

![](./images/814675966092640257_8.jpg)

FIG. 5. The calculated PDOS under tensile strain. (a) Single-crystalline graphene. (b) and (c) Polycrystalline graphene with average grain size of 7.5 and 2.5 nm, respectively.

![](./images/814675966092640257_9.jpg)

FIG. 6. The thermal conductivities of SC and polycrystalline graphene as a function of temperature. 2.5 nm and 10 nm are the average grain sizes for polycrystalline graphene.

## C. Temperature effect

Finally, we study the effect of temperature on the thermal conductivity of polycrystalline graphene. The simulated thermal conductivities at different temperatures are shown in Fig. 6. It can be seen that temperature has a strong effect on the thermal conductivity of single-crystalline graphene: The thermal conductivity shows an obvious decrease with increasing temperature. In contrast, the temperature has a much smaller effect on the thermal conductivity of polycrystalline graphene. In particular, Fig. 6 shows that the change in thermal conductivity is almost negligible for the case with the smallest grain size studied (2.5 nm). This behavior may be explained by the composite material model discussed earlier. On the one hand, as the temperature increases, the thermal conductivity of the grain interior decreases due to enhanced Umklapp scattering. $^{43,44}$ On the other hand, the thermal conductivity of GB increases with increasing temperature due to weakened GB scattering. $^{15}$ The net result is a combination of the two phenomena, and therefore, the thermal conductivity of polycrystalline graphene is less sensitive to temperature than that of single-crystalline graphene.

## IV. CONCLUSION

In summary, we constructed a series of polycrystalline graphene samples with average grain sizes ranging from 2.5 to 12.5 nm, and calculated the thermal conductivity of the polycrystalline graphene samples using molecular dynamics simulations. We found that the thermal conductivity of polycrystalline graphene is much lower than that of single-crystalline graphene. The smaller the grain size, the lower the thermal conductivity. In addition, we applied tensile strain on the samples and studied the strain effect on the thermal transport. It is found that strain reduces the thermal conductivity of both single-crystalline and polycrystalline graphene. However, the thermal conductivity of polycrystalline graphene is less sensitive to the strain than that of single-crystalline graphene. We also studied the effect of temperature on the thermal transport and found that the thermal conductivity of polycrystalline graphene is less sensitive to temperature change than that of single-crystalline graphene. These findings are important for the thermal management in graphene-based devices.

## ACKNOWLEDGMENTS

This work was supported by the A*STAR Computational Resource Centre through the use of its high performance computing facilities.

$^{1}$A. A. Balandin, *Nat. Mater.* **10**, 569 (2011).
$^{2}$A. A. Balandin, S. Ghosh, W. Bao, I. Calizo, D. Teweldebrhan, F. Miao, and C. N. Lau, *Nano Lett.* **8**, 902 (2008).
$^{3}$A. K. Geim and K. S. Novoselov, *Nat. Mater.* **6**, 183 (2007).
$^{4}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, *Science* **306**, 666 (2004).
$^{5}$P. Avouris and F. Xia, *MRS Bull.* **37**, 1225 (2012).
$^{6}$Y. Shao, J. Wang, H. Wu, J. Liu, I. A. Aksay, and Y. Lin, *Electroanalysis* **22**, 1027 (2010).
$^{7}$S. Ghosh, I. Calizo, D. Teweldebrhan, E. P. Pokatilov, D. L. Nika, A. A. Balandin, W. Bao, F. Miao, and C. N. Lau, *Appl. Phys. Lett.* **92**, 151911 (2008).
$^{8}$M. Hu and D. Poulikakos, *Int. J. Heat Mass Transfer* **62**, 205 (2013).
$^{9}$D. A. C. Brownson, D. K. Kampouris, and C. E. Banks, *J. Power Sources* **196**, 4873 (2011).
$^{10}$L. P. Biro and P. Lambin, *New J. Phys.* **15**, 035024 (2013).
$^{11}$B. Hu, H. Ago, Y. Ito, K. Kawahara, M. Tsuji, E. Magome, K. Sumitani, N. Mizuta, K.-i. Ikeda, and S. Mizuno, *Carbon* **50**, 57 (2012).
$^{12}$L. Jiang, T. Yang, F. Liu, J. Dong, Z. Yao, C. Shen, S. Deng, N. Xu, Y. Liu, and H.-J. Gao, *Adv. Mater.* **25**, 250 (2013).
$^{13}$A. Reina, X. Jia, J. Ho, D. Nezich, H. Son, V. Bulovic, M. S. Dresselhaus, and J. Kong, *Nano Lett.* **9**, 30 (2009).
$^{14}$A. Bagri, S. P. Kim, R. S. Ruoff, and V. B. Shenoy, *Nano Lett.* **11**, 3917 (2011).
$^{15}$A. Cao and J. Qu, *J. Appl. Phys.* **111**, 053529 (2012).
$^{16}$Y. Lu and J. Guo, *Appl. Phys. Lett.* **101**, 043112 (2012).
$^{17}$A. Y. Serov, Z. Y. Ong, and E. Pop, *Appl. Phys. Lett.* **102**, 033104 (2013).
$^{18}$S. Tang and Y. Kulkarni, *Appl. Phys. Lett.* **103**, 213113 (2013).
$^{19}$Y. Wang, Z. Song, and Z. Xu, *J. Mater. Res.* **29**, 362 (2014).
$^{20}$B. Mortazavi, M. Poetschke, and G. Cuniberti, *Nanoscale* **6**, 3344 (2014).
$^{21}$J. Kotakoski and J. C. Meyer, *Phys. Rev. B* **85**, 195447 (2012).
$^{22}$W. Brostow, J. P. Dussault, and B. L. Fox, *J. Comput. Phys.* **29**, 81 (1978).
$^{23}$J. L. Finney, *J. Comput. Phys.* **32**, 137 (1979).
$^{24}$L. Tapaszto, P. Nemes Incze, G. Dobrik, K. J. Yoo, C. Hwang, and L. P. Biro, *Appl. Phys. Lett.* **100**, 053114 (2012).
$^{25}$S. Plimpton, *J. Comput. Phys.* **117**, 1 (1995).
$^{26}$S. J. Stuart, A. B. Tutein, and J. A. Harrison, *J. Chem. Phys.* **112**, 6472 (2000).
$^{27}$F. Muller-Plathe, *J. Chem. Phys.* **106**, 6082 (1997).
$^{28}$J. Chen, G. Zhang, and B. Li, *Nanoscale* **5**, 532 (2013).
$^{29}$W. Huang, Q. X. Pei, Z. S. Liu, and Y. W. Zhang, *Chem. Phys. Lett.* **552**, 97 (2012).
$^{30}$D. L. Nika, A. S. Askerov, and A. A. Balandin, *Nano Lett.* **12**, 3238 (2012).
$^{31}$D. L. Nika and A. A. Balandin, *J. Phys.: Condens. Matter* **24**, 233203 (2012).
$^{32}$Q. X. Pei, Z. D. Sha, and Y. W. Zhang, *Carbon* **49**, 4752 (2011).
$^{33}$Q. X. Pei, Y. W. Zhang, Z. D. Sha, and V. B. Shenoy, *Appl. Phys. Lett.* **100**, 101901 (2012).
$^{34}$S. Chen, Q. Wu, C. Mishra, J. Kang, H. Zhang, K. Cho, W. Cai, A. A. Balandin, and R. S. Ruoff, *Nat. Mater.* **11**, 203 (2012).
$^{35}$W. Kim and A. Majumdar, *J. Appl. Phys.* **99**, 084306 (2006).
$^{36}$B. Mortazavi and S. Ahzi, *Carbon* **63**, 460 (2013).
$^{37}$J. Y. Yeo, Z. Liu, and T. Y. Ng, *Nanotechnology* **23**, 385702 (2012).
$^{38}$Y. Zhang, Y. Cheng, Q. X. Pei, C. M. Wang, and Y. Xiang, *Phys. Lett. A* **376**, 3668 (2012).

$^{39}$V. M. Pereira and A. H. C. Neto, *Phys. Rev. Lett.* **103**, 046801 (2009).

$^{40}$K. Xue and Z. P. Xu, *Appl. Phys. Lett.* **96**, 063103 (2010).

$^{41}$N. Wei, L. Xu, H. Q. Wang, and J. C. Zheng, *Nanotechnology* **22**, 105705 (2011).

$^{42}$Z. Xu and M. J. Buehler, *Nanotechnology* **20**, 185701 (2009).

$^{43}$D. G. Cahill, P. V. Braun, G. Chen, D. R. Clarke, S. Fan, K. E. Goodson, P. Keblinski, W. P. King, G. D. Mahan, A. Majumdar, H. J. Maris, S. R. Phillpot, E. Pop, and L. Shi, *Appl. Phys. Rev.* **1**, 011305 (2014).

$^{44}$D. L. Nika, E. P. Pokatilov, A. S. Askerov, and A. A. Balandin, *Phys. Rev. B* **79**, 155413 (2009).