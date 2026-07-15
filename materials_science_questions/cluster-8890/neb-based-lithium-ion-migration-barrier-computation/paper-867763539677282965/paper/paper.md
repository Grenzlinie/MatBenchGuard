### 1. Introduction

Research on advanced energy storage technology is significant for the development of modern society [1]. Rechargeable lithium-ion batteries (LIBs), one of the widely studied clean energy-storage technologies, have attracted increasing attention due to the combination of outstanding reversible capacity, high power density, superior energy efficiency, long cycle life, and portability [2-9]. Currently, LIBs are widely applied in portable electronics, electric vehicles, and electricity grid systems [10, 11]. In addition to LIBs, an alternative option is the rechargeable Na-ion batteries (NIBs), which have been found promising and can be a good candidate to replace LIBs in the future because sodium is more abundant and cheaper than lithium [12-16]. The capability of LIBs and NIBs is highly dependent on the performances of their electrode materials [17, 18]. Nowadays, graphite is commercially used as anode material for LIBs because of its high Coulombic efficiency, relatively good cycling stability, and low cost [19, 20], but the relatively low theoretical specific capacity (372 mAh/g) and poor rate capability restricts its further application [21]. In addition, graphite cannot be used in NIBs, because the Na-C interaction is found to be too weak to contribute to the necessary Coulomb interactions [22]. Therefore, seeking for new anode materials to further improve the performance of LIBs and NIBs is urgently needed [23-25].

2D materials [26, 27] are of special interest as anode materials for LIBs and NIBs because of their high surface area, remarkably high electron mobility and superior mechanical properties [28]. In recent years, many 2D materials have been investigated as anode materials and great success has been obtained [29-44]. Graphene represents the first example of a 2D electrode material for LIBs [45, 46]. Since then, novel 2D materials including $\text{MoS}_2$ [47], $\text{VS}_2$ [48], silicene [49], phosphorene [50-52], borophene [29, 53], borophane [35], boron phosphide [36], $\text{Mo}_2\text{C}$ [38], and so on have been investigated as anode materials for LIBs or NIBs. In addition, 2D transition metal carbides or nitrides, called MXenes [54, 55], have also attracted great interest in this field [30-32]. The MXenes can be synthesized by selective etching of A atoms

from MAX phases with hydrofluoric acid (HF) at room temperature [54, 55] and the advantage of easy fabrication offers an intrinsic potential for their practical applications [54, 56-59]. Although many 2D materials have been confirmed theoretically as potential electrode materials, the search for LIBs and NIBs with better performance is still necessary and significant. Very recently, Guo et al [60]. have investigated new 2D TMBs such as $Fe_2B_2$ and $Mo_2B_2$ for LIBs. As far as we know, this is the first time that 2D TMBs have been investigated as LIBs. These 2D TMBs belong to orthorhombic system and can be obtained from layered orthorhombic TMBs that possess highly structural similarity to the MAX phases. In addition to these orthogonal structures, there are also a family of layered TMBs which belong to hexagonal crystal system with the formula of $TMB_2$. These layered TMBs contain graphene-like honeycomb boron layers and can be transformed into 2D "sandwich" structures which consist of two boron honeycomb sheets and an intermediate hexagonal plane of TM atom (B-TM-B) [61, 62]. However, because the outermost sheets of MXenes are composed of metallic atoms, we are interested in whether the hexagonal TMBs can also be transformed into 2D structure consisting of an intermediate boron honeycomb and two outer hexagonal planes of TM atoms (TM-B-TM). Besides, it is our great interest to investigate the potential applications of these 2D materials as LIBs and NIBs.

In this work, we first report a series of 2D TMBs including $Sc_2B_2$, $Ti_2B_2$, $V_2B_2$, $Cr_2B_2$, $Y_2B_2$, $Zr_2B_2$, and $Mo_2B_2$. This monolayer $TM_2B_2$ belongs to the space group of P6/mmm with 4 atoms in a hexagonal unit cell, which is identified consisting of an intermediate boron honeycomb sheet sandwiched in between two hexagonal planes of TM atoms. These 2D TMBs can be produced from their bulk phase which is a family of layered TMBs of hexagonal crystal system with the formula of $TMB_2$. Furthermore, we choose $Ti_2B_2$ as the representative and investigate its performance as an anode material for LIBs and NIBs by performing first-principles calculations. Our results illustrate that $Ti_2B_2$ monolayer is a promising electrode material for LIBs and NIBs. This fact is encouraging and indicates that our predicted series of 2D TMBs could be

promising candidates for the next-generation portable batteries.

## 2. Computational method
The particle-swarm optimization (PSO) scheme, as implemented in the CALYPSO code [63-65], is employed to search for low energy 2D Ti₂B₂ structures.
The underlying energy calculations and structure optimizations are performed by using the plane-wave-based density-functional theory (DFT) method as implemented in the Vienna ab-initio Simulation Package (VASP) [66-68]. The computational details of the PSO and DFT methods are illustrated in the Supporting Information.
The adsorption energy of lithium and sodium atoms on the Ti₂B₂ monolayer is obtained from:

$$
E_{\mathrm{ad}}=\left(E_{T i_{2} B_{2} M}-E_{T i_{2} B_{2}}-n E_{M}\right) / n(M=L i, N a) \tag{1}
$$

where $E_{Ti_2B_2M}$ and $E_{Ti_2B_2}$ represent the total energies of the metal-ion adsorbed monolayer system and the isolated monolayer, respectively, $E_M$ represents the total energy of per atom for the bulk metal. The charge density difference $\Delta\rho$ are calculated based on the following equation:

$$
\Delta \rho=\rho_{T i_{2} B_{2} M}-\rho_{T i_{2} B_{2}}-\rho_{M}(M=L i, N a) \tag{2}
$$

where $\rho_{Ti_2B_2M}$，$\rho_{Ti_2B_2}$, and $\rho_M$ are the total charge of the Li/Na adsorbed system, the Ti₂B₂ monolayer, and the Li/Na atom, respectively. The open circuit voltage can be obtained using a well-established approach [69] according to the following formula:

$$
V=-\left(E_{T i_{2} B_{2} M}-E_{T i_{2} B_{2}}-n E_{M}\right) / n(M=L i, N a) \tag{3}
$$

To assess the adsorption stability of Li/Na layer on the Ti₂B₂ monolayer, the average adsorption energies for each Li/Na layer are calculated according to the following equation:

$$
E_{\text {ave }}=\left(E_{T i_{2} B_{2} M_{n}}-E_{T i_{2} B_{2} M_{(n-1)}}-m E_{M}\right) / m(M=L i, N a) \tag{4}
$$

where $E_{Ti_2B_2M_n}$ and $E_{Ti_2B_2M_{(n-1)}}$ are the total energies of 2D Ti₂B₂ with n and (n-1) adsorbed Li/Na layers, $E_M$ stands for the total energy of per atom for the bulk metal.
The number m represents m adsorbed Li/Na atoms in each layer (for a 2×2 supercell

on both sides). The theoretical capacity can be obtained from:

$$C_{A}=c z F / M_{T i_{2} B_{2}} \tag{5}$$

where $c$ is the number of adsorbed Li/Na ions, $z$ is the valence number of Li/Na, $F$ is Faraday constant (26801 mAh/mol), and $M_{Ti_2B_2}$ is the molar weight of Ti₂B₂.

## 3. Results and Discussion
### 3.1 2D TM₂B₂ and Bulk TMB₂.

![](./images/867763539677282965_1.jpg)

Fig. 1. Top and side views of (a) global minimum phase of Ti₂B₂ monolayer and (b) bulk TiB₂. The Ti and B atoms are denoted by green and orange spheres, respectively.

Motivated by the excellent performance of the MXenes in energy storage [70], we investigate TM-B systems characterized by 2D "sandwich" structures. Interestingly, through structural prediction by using the CALYPSO code, we find several 2D Ti₂B₂ structures. The global minimum structure is shown in Fig. 1a and the other metastable isomers in Fig. S1 in the Supplementary information (SI). The obtained orthorhombic 2D Ti₂B₂ monolayer (Fig. S1a) possesses the same structure as those of 2D Fe₂B₂ and Mo₂B₂ reported by Guo *et al* [60]. According to our calculations, the energy of this orthorhombic 2D Ti₂B₂ monolayer is higher by 0.067 eV per atom than that of the obtained hexagonal 2D Ti₂B₂ which is the global minimum structure (Fig. 1a). This hexagonal 2D Ti₂B₂ consists of an intermediate boron honeycomb sheet sandwiched in between two hexagonal planes of Ti atoms.

Å) [72]. As shown in Fig. 2, the optimized lattice constants $(a)$ of other six 2D TM₂B₂ are all consistent with those of their corresponding bulk structures. This indicates that these 2D structures are easily obtained from their corresponding bulk phases.

![](./images/867763539677282965_2.jpg)

Fig. 3. (a) Total and partial density of states (TDOS and PDOS) of the 2D Ti₂B₂. The dash black line represents the TDOS while the solid red and solid blue lines stand for the Ti-$3d$ and B-$2p$ PDOS, respectively. The Fermi energy level is set at zero. (b) Phonon dispersion curves of the 2D Ti₂B₂. (c) Variation of the free energy in the AIMD simulations at 300 K during the time scale of 10 ps.

As shown in Fig. 3a, the 2D Ti₂B₂ exhibits metallic property contributed mainly by the Ti-$3d$ orbitals. The contribution from the B-$2p$ is ignorable. The TDOS and PDOS of 2D Sc₂B₂, V₂B₂, Cr₂B₂, Y₂B₂, Zr₂B₂, and Mo₂B₂ (shown in Fig. S2 in the SI) indicate that these six 2D materials, like 2D Ti₂B₂, present good conductivity. Owing to the outstanding electronic conductivity of these 2D TM₂B₂, they merit potential application as anode materials for LIBs and NIBs.

The stability of anode materials is critical important due to hundreds of charge-discharge cycles in practical applications. To examine the dynamic stability of 2D $Ti_2B_2$, we calculate its phonon dispersion curves. As shown in Fig. 3b, the absence of imaginary modes in the whole BZ confirms that 2D $Ti_2B_2$ is dynamically stable. The highest frequency of 2D $Ti_2B_2$ reaches up to 27.725 THz (924 cm⁻¹), which is higher than those of $FeB_2$ (854 cm⁻¹) [78], TiC (810 cm⁻¹) [79], $Cu_2Si$ (420 cm⁻¹) [80], and $MoS_2$ (473 cm⁻¹) [81] monolayers. The high value of frequencies in the phonon dispersion also indicates the stability of this 2D material. The phonon spectra of other six 2D $TM_2B_2$ are also calculated and shown in Fig. S3 in the SI. We find that these 2D $TM_2B_2$ are also dynamically stable. To check the thermal stability, we carry out AIMD simulations for the 2D $Ti_2B_2$ at temperatures of 300, 600, 1200, 1800, 2400, and 3000 K, respectively. At 300 K, the average value of free energy remains almost constant during the whole simulation (see Fig. 3c), confirming that the 2D $Ti_2B_2$ is thermally stable at room temperature. Even increasing the temperature up to 2400 K, the original geometry remains intact with only slight in-plane and out-of-plane deformations (see Fig. S4). The free energies fluctuate around constant values during the AIMD simulation below and at 2400 K (see Fig. S5). These results confirm that the 2D $Ti_2B_2$ is stable upon heating, which, supplies safeguard for practical applications.

3.2 Adsorption of Li and Na on the 2D $Ti_2B_2$ monolayer.

![](./images/867763539677282965_3.jpg)

Fig. 4. (a) High symmetry adsorption sites and (b) adsorption energies for Li/Na on the surface of 2D Ti₂B₂. The Ti and B atoms are denoted by green and orange spheres, respectively.

The intrinsic metallicity and good stability of the 2D Ti₂B₂ make it a promising anode material for LIBs and NIBs. Next, we will further check its ability of adsorbing Li/Na atoms. We first investigate the adsorption behaviors of a single Li/Na atom on the surface of the 2D Ti₂B₂ by considering three high symmetry adsorption sites S1, S2, and S3 (see Fig. 4a). The adsorption energies of Li/Na atom on these sites are shown in Fig. 4b. We find that the Na-adsorbed configurations are more stable than the Li-adsorbed ones and the S1 is always the most stable adsorption site for both Li and Na atoms. Interestingly, the adsorption energies on S3 are very close to those on S1, suggesting that the Li/Na atoms are easy to diffuse along the S1-S3-S1 direction, i.e. the B-B bonding direction. The adsorption energies on S2 are smaller by 0.06-0.13 eV than those on S1 and S3. This indicates that the Li/Na atom is not possible to appear on top of the Ti atoms. To better understand the adsorption properties of Li/Na on the Ti₂B₂ surface, we calculate the difference charge density and present them in Fig. 5 (Li-adsorption) and Fig. S6 (Na-adsorption). It is clear that the electrons tend to accumulate in between Li/Na and its neighbor Ti atoms, thus, result in the Li/Na-Ti bonding. This chemical bonding between Li/Na atoms and 2D Ti₂B₂ are favorable to prevent the forming of Li/Na cluster and improve the safety and application availability for Li/Na storage in LIBs and NIBs.

![](./images/867763539677282965_4.jpg)

Fig. 5. The charge density difference plots for Li adsorption on the (a) S1, (b) S2, and (c) S3 sites of 2D Ti₂B₂ monolayer. The yellow and cyan areas represent electron gains and loses. The Ti, B, and Li atoms are denoted by green, orange, and violet spheres, respectively.

### 3.3 Theoretical specific capacity and average open-circuit voltage.

![](./images/867763539677282965_5.jpg)

Fig. 6. Top and side views of the structures of (a) Ti₂B₂Li₂, (b) Ti₂B₂Li₄, and (c) Ti₂B₂Li₆ with layers of Li ions adsorbed on the surface of 2D Ti₂B₂ monolayer. The Ti, B, and Li atoms are denoted by green, orange, and violet spheres, respectively.

For practical application, it is of great significance to investigate the storage capacity of the batteries for the electrode materials. Thus, the average adsorption energies are calculated to investigate the storage capacity of Li/Na on the Ti₂B₂ monolayer. The adsorptions of one, two, and three layers of Li on both sides of Ti₂B₂ monolayer are investigated using 2×2 supercells and can be labeled as Ti₂B₂Liₓ with x=2, 4 and 6, respectively. For the one-layer adsorption, shown in Fig. 6a, all Li atoms are absorbed at the S1 sites. In condition of saturation, there are eight Li atoms that can be adsorbed on both sides of the Ti₂B₂ monolayer. The average adsorption energy of Li atoms is -0.526 eV, which indicates that Li adatoms can be adsorbed stably without clustering. After the first layer being adsorbed fully, the subsequently added

Li atoms will form the second adsorbed layer. The Li atoms are also adsorbed at the S1 sites (see Fig. 6b). This can be regard as the two-layer adsorption and there are 16 Li atoms being adsorbed in condition of full adsorption. For the three-layer adsorption, the third-layer Li atoms are adsorbed at the S2 sites (Fig. 6c). In condition of full adsorption, there are 24 Li atoms being adsorbed. The adsorption energies for one-layer, two-layer, and three-layer adsorption are -4.208, -4.019, and -3.800 eV, respectively. However, according to Eq. (4), the calculated average adsorption energies for the second and third layers of Li atoms are 0.024 and 0.027 eV, respectively. The positive values of these adsorption energies mean that the adsorptions of two and three layers of Li are not stable in energy. The above results reveal that the $2×2$ supercell of $Ti_2B_2$ monolayer can accumulate 8 Li atoms at most, corresponding to $Ti_2B_2Li_2$ with symmetric configuration of adatoms on both sides of $Ti_2B_2$ monolayer. According to these results and Eqs (3) and (5), the corresponding theoretical specific capacity and average open-circuit voltage of the 2D $Ti_2B_2$ as electrode of LIBs are $\sim$456 mA h g⁻¹ and 0.526 eV, respectively.

![](./images/867763539677282965_6.jpg)

Fig. 7. Top views of (a) one-layer, (b) two-layers, and (c) three-layers adsorptions of Na ions on the 2D Ti₂B₂ monolayer. Na1, Na2, and Na3 represent the Na ions adsorbed in the first, the second, and the third layer, respectively. The black lines stand for the range of a 2×2 supercell.

Next, we turn our focus on the case of Na-adsorbed Ti₂B₂ system. The one-layer, two-layers, and three-layers adsorptions of Na on both sides of 2D Ti₂B₂ are calculated and the corresponding schematic pictures are presented in Fig. 7. For clarity, only Na atoms on single side of the 2D Ti₂B₂ are shown in this figure. The first layer can accommodate at most six Na atoms on both sides of the Ti₂B₂ monolayer, three Na atoms on each side. This number is less than that of Li adsorption. Since the atomic radius of Na is larger than that of Li, this fact is understandable. As shown in Fig. 7a, the three Na atoms form an equilateral triangle and the adsorption sites are

not at the S1. When the first layer is adsorbed fully, the additionally added Na atoms will form the second layer at the sites above the center of the equilateral triangles (Fig. 7b). The adsorption sites for the third layer are above the center of the equilateral triangles of the second layer (Fig. 7c). The second and the third layers can also accommodate as many as six Na atoms on both sides. The average adsorption energies are all negative for the first, the second, and the third layers (-0.502, -0.007, and -0.009 eV, respectively), indicating that Na atoms can be adsorbed stably without clustering. Furthermore, the adsorption of four layers of Na on the $Ti_2B_2$ monolayer is not energetically stable according to our calculation. The above results reveal that the $2×2$ supercell of $Ti_2B_2$ monolayer can accommodate 18 Na adatoms, corresponding to $Ti_2B_2Na_{4.5}$. Therefore, the calculated theoretical specific capacity of the 2D $Ti_2B_2$ as electrode of NIBs is ~1027 mA h g⁻¹. The average open-circuit voltage decreases from 0.502, via 0.255, to 0.173 eV with increasing of the adsorbed Na atoms from 6, via 12, to 18.

We also estimate the varying of lattice constant and thickness of the $Ti_2B_2$ monolayer after the adsorption of layered Li/Na atoms. The lattice constant increases from 6.008 ($Ti_2B_2$) to 6.047 Å ($Ti_2B_2Li_2$) for Li adsorption (about 0.65% tensile strain), and slightly increases from 6.008 ($Ti_2B_2$), 6.040 ($Ti_2B_2Na_{1.5}$), and 6.054 ($Ti_2B_2Na_3$) to 6.070 Å ($Ti_2B_2Na_{4.5}$) for Na adsorption (about 1.03% tensile strain). The calculated thickness of the $Ti_2B_2$ monolayer for the one-layer adsorbed Li structure ($Ti_2B_2Li_2$) is 3.128 Å, which is larger by 0.29% than that of the bare monolayer (3.119 Å). However, the thicknesses of the $Ti_2B_2$ monolayer for the one-layer ($Ti_2B_2Na_{1.5}$), two-layer ($Ti_2B_2Na_3$), and three-layer ($Ti_2B_2Na_{4.5}$) adsorptions of Na are 3.108, 3.106, and 3.110 Å, respectively. These values are smaller by 0.35%, 0.42%, and 0.29% than the bare one, respectively. In view of these results, the $Ti_2B_2$ monolayer is robust to be used as anode material in both LIBs and NIBs.

### 3.4 Electronic structures of the 2D Ti₂B₂ monolayer with adsorbed Li/Na atoms.

![](./images/867763539677282965_7.jpg)

Fig. 8. TDOS and PDOS of the 2D Ti₂B₂ monolayer adsorbed with (a) one Li atom, (b) one-layer Li atoms, (c) two-layer Li atoms, (d) three-layer Li atoms, (e) one Na atom, (f) one-layer Na atoms, (g) two-layer Na atoms, and (h) three-layer Na atoms, respectively. The Fermi energy levels are set as zero.

It is well known that the electronic conductivity is closely associated with the rate capability of the anode materials in LIBs and NIBs. Unlike many other 2D materials that exhibit semi-conducting or semi-metallic characteristics [82, 83], our previous analyses have demonstrated that the pristine Ti₂B₂ monolayer exhibits intrinsic metallic behavior, which means a remarkable battery performance for the sheet. In order to gain insight into the electronic conductivity of the charge-discharge process, the evolutions of DOS for Ti₂B₂ monolayer adsorbed with Li/Na atoms are calculated (Fig. 8). Fig. 8a shows the DOS of single Li adsorbed on the Ti₂B₂ monolayer. Compared to the DOS of the pristine Ti₂B₂ monolayer (Fig. 3a), we find that the orbital contributions around the Fermi level mainly come from the sheet with

negligible components from the Li atoms, endowing the system with metallic characteristic. To be mentioned that $Ti_2B_2$ monolayer is easy to be terminated with multiple Li atoms, hence the modulation effect of surface atomic number on electronic structures has also been evaluated in the following sequence: one-layer (Fig. 8b), two-layer (Fig. 8c), and three-layer (Fig. 8d) adsorbed Li configurations. With the Li concentration increasing during the charging process, the orbital contributions from Li atoms near the Fermi level increase with the components of the monolayer showing no big fluctuations. Meanwhile, the Fermi level is getting away from the valley bottom of the DOS with the increasing number of Li atoms, indicating the growing instability of the system. These simulations explicitly demonstrate that the system retains the metallic nature during Li atomic adsorption process. Similar evolutions of DOS, for the host $Ti_2B_2$ monolayer with one-layer, two-layer, and three-layer Na adsorbed, are also found in Fig. 8. These robust electronic properties of $Ti_2B_2$ monolayer greatly expand its potential applications in anode materials and motivate subsequent experimental studies.

### 3.5 Li/Na diffusion on 2D $Ti_2B_2$ monolayer.

![](./images/867763539677282965_8.jpg)

Fig. 9. Top view of two pathways, (a) Path A-C and (b) Path B-D, for Li/Na diffusion on the 2D $Ti_2B_2$ monolayer. The Ti, B, and Li/Na atoms are denoted by green, orange, and violet spheres, respectively. (c) Energy profiles of the corresponding Li and Na diffusion pathways.

In addition to the high specific capacity, a good charge–discharge rate capability is of great significance for a promising anode material for LIBs and NIBs. The diffusion barrier of Li/Na is a key factor that determines the charge-discharge rate. In this part, we employ the CI-NEB method to investigate the diffusion barriers for Li and Na atoms on the surface of $Ti_2B_2$ monolayer. As Li and Na atoms preferentially occupy the S1 site, two possible pathways starting from one S1 site to another S1 site are considered. The first pathway is from A to C (Fig. 9a) and the second from B to D (Fig. 9b). Both these pathways are connected by four S1 and three S3 sites and can be viewed as S1-S3-S1-S3-S1-S3-S1. As illustrated in Fig. 9c, the energy barriers for Li diffusion along the A-C and B-D pathways are both 0.017 eV while that for Na diffusion are both 0.008 eV. The ultralow diffusion energy barriers indicate that Li and Na atoms can diffuse extremely easy on the $Ti_2B_2$ monolayer. Furthermore, due to the smaller diffusion energy barrier of Na than that of Li, the Na ions are easier to diffuse on the $Ti_2B_2$ monolayer than Li ions. The larger rate capacity for Na than Li is also found in other 2D materials, such as $B_2H_2$ [35] and $Mo_2C$ [38]. Here, the low diffusion energy barriers are due to the small difference of the Li/Na adsorption energies between the S1 and S3 sites. Since that the diffusion energy barriers for A-C and B-D pathways are the same, the two pathways are both possible routes for Li/Na ion diffusion, which, would beneficial to increase the charge-discharge rate of LIBs and NIBs.

![](./images/867763539677282965_9.jpg)

Fig. 10. Top and side views of the calculated (a) Li and (b) Na trajectories during the
10 ps AIMD simulations. The Ti, B, Li, and Na atoms are denoted by green, orange,
violet, and blue spheres, respectively.

To further investigate the diffusion kinetics of Li and Na atoms on the $Ti_2B_2$
monolayer, the AIMD simulations are performed at 300 K lasting for 10 ps. The Li
and Na diffusion trajectories during the 10 ps simulation, shown in Fig. 10a and 10b,
respectively, give direct visualizations of Li and Na diffusion on the $Ti_2B_2$ monolayer.
We see that the Li atom can travel through the entire region almost freely along the
A-C or B-D pathways, although the diffusion path is not that straight. Interestingly,
the Na atom can diffuse through the entire region in almost straight lines along the
A-C pathway. Similar behavior has been observed on borophene for Li diffusion [29].
The above AIMD simulation results explicitly exhibit an ultra-fast Li/Na diffusion on
the 2D $Ti_2B_2$ monolayer, giving a proof that this 2D material is a promising candidate
for the high rate LIBs and NIBs electrode materials.

### 3.6 Comparison with other anode materials.

In order to evaluate the superiority of our studied $Ti_2B_2$ monolayer as an electrode
material for LIBs and NIBs, we compare the theoretical specific capacity and
diffusion barrier of it with other widely investigated anode materials [8, 29, 31, 33-35,

38, 47-53, 60, 84-92] in Table 1 and Table 2. For Li storage, the theoretical specific capacity of the $Ti_2B_2$ monolayer is 456 mAhg⁻¹, which is greater than that of the well-established graphite [8, 84, 85], phosphorene [50, 51], $Ti_3C_2$ [31], or $Li_4Ti_5O_{12}$ [86], and comparable to that of the $Mo_2C$ [38], $VS_2$ [48], $B_2H_2$ [35], and planar $TiB_4$ [92]. Compared to the orthorhombic 2D MBenes [60], the theoretical specific capacity of the hexagonal 2D $Ti_2B_2$ is in between those of the 2D $Mo_2B_2$ and the 2D $Fe_2B_2$ [60]. Although the theoretical specific capacity is lower than that of silicon [87], silicene [49], and Sn [86, 88], the energy barrier (0.017 eV) for Li diffusion is the lowest one among the listed materials in Table 1 besides borophene [29]. This indicates that the 2D $Ti_2B_2$ possesses a very high rate capability for Li diffusion.

In the case of Na storage and diffusion, as shown in Table 2, the $Ti_2B_2$ monolayer has the second largest theoretical specific capacity. The value of 1027 mAhg⁻¹ is larger than that of phosphorene [89] and boron-doped graphene [90] and close to the highest theoretical specific capacity we found in literature for $Ca_2N$ [34]. When compared with other 2D materials, the theoretical specific capacity of $Ti_2B_2$ is about 2 to 3 times of that reported in $Ti_3C_2$ [33], borophene [53], $B_2H_2$ [35], and $Sr_2N$ [34], and is more than 7 times of that reported in $MoS_2$ [47] and $Mo_2C$ [38]. In addition, the diffusion energy barrier (0.008 eV) of Na ion on $Ti_2B_2$ monolayer is much lower than that of any other typical promising anode materials, shown in Table 2, indicating a very high rate capability.

In the end, we also compare the properties as an anode material for 2D $Ti_2B_2$ with the hexagonal 2D $TiB_4$ whose atomic stacking is B-Ti-B (Fig. S7a). The calculated energy of this 2D $TiB_4$ (Fig. S7a) is lower by 0.198 eV per atom than the most stable planar 2D $TiB_4$ (Fig. S7b) [92], indicating the stability of this hexagonal 2D $TiB_4$. The most stable adsorption sites and the corresponding adsorption energies are presented in Fig. S8. The 2×2 supercell of the hexagonal 2D $TiB_4$ can accommodate 8 Li or Na atoms (Fig. S9), corresponding to $TiB_4Li_2$ and $TiB_4Na_2$, respectively. The theoretical specific capacity of this hexagonal 2D $TiB_4$ are both 588 mAhg⁻¹ for Li and Na storage, indicating a higher Li storage but a lower Na storage than those of the 2D

Ti₂B₂. However, the diffusion energy barriers of Li (0.712 eV) and Na (0.377 eV) on the hexagonal 2D TiB₄ are much larger than those on the 2D Ti₂B₂ (Fig. S10), indicating that the 2D Ti₂B₂ is more suitable to be an electrode material than the 2D TiB₄.

Table 1. Summary of theoretical specific capacities (mAhg⁻¹) and diffusion barriers (meV) of some widely investigated promising anode materials for LIBs.

<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Theoretical specific capacity</th>
      <th>Diffusion barrier</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ti₂B₂</td>
      <td>456</td>
      <td>17</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>Graphite</td>
      <td>372</td>
      <td>450~1200</td>
      <td>[8, 84, 85]</td>
    </tr>
    <tr>
      <td>Phosphorene</td>
      <td>433</td>
      <td>80</td>
      <td>[50, 51]</td>
    </tr>
    <tr>
      <td>Silicon</td>
      <td>4200</td>
      <td>580</td>
      <td>[87]</td>
    </tr>
    <tr>
      <td>Silicene</td>
      <td>954</td>
      <td>230</td>
      <td>[49]</td>
    </tr>
    <tr>
      <td>Sn</td>
      <td>994</td>
      <td>390</td>
      <td>[86, 88]</td>
    </tr>
    <tr>
      <td>1T-Ti₃C₂</td>
      <td>320</td>
      <td>70</td>
      <td>[31]</td>
    </tr>
    <tr>
      <td>1H-Mo₂C</td>
      <td>526</td>
      <td>35</td>
      <td>[38]</td>
    </tr>
    <tr>
      <td>VS₂</td>
      <td>466</td>
      <td>220</td>
      <td>[48]</td>
    </tr>
    <tr>
      <td>Borophene</td>
      <td>1860</td>
      <td>2.6</td>
      <td>[29]</td>
    </tr>
    <tr>
      <td>B₂H₂</td>
      <td>504</td>
      <td>210</td>
      <td>[35]</td>
    </tr>
    <tr>
      <td>Li₄Ti₅O₁₂</td>
      <td>175</td>
      <td>300</td>
      <td>[86, 91]</td>
    </tr>
    <tr>
      <td>Orthorhombic Fe₂B₂</td>
      <td>665</td>
      <td>240</td>
      <td>[60]</td>
    </tr>
    <tr>
      <td>Orthorhombic Mo₂B₂</td>
      <td>444</td>
      <td>270</td>
      <td>[60]</td>
    </tr>
    <tr>
      <td>Planar TiB₄</td>
      <td>588</td>
      <td>180</td>
      <td>[92]</td>
    </tr>
  </tbody>
</table>

Table 2. Summary of theoretical specific capacities (mAhg⁻¹) and diffusion barriers (meV) of some widely investigated promising anode materials for NIBs.

<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Theoretical specific capacity</th>
      <th>Diffusion barrier</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ti₂B₂</td>
      <td>1027</td>
      <td>8</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>Phosphorene</td>
      <td>865</td>
      <td>40</td>
      <td>[52]</td>
    </tr>
    <tr>
      <td>graphene</td>
      <td></td>
      <td>130</td>
      <td>[89]</td>
    </tr>
    <tr>
      <td>Boron-doped graphene</td>
      <td>762</td>
      <td>160-220</td>
      <td>[90]</td>
    </tr>
    <tr>
      <td>1T-MoS₂</td>
      <td>146</td>
      <td>280</td>
      <td>[47]</td>
    </tr>
    <tr>
      <td>1T-Ti₃C₂</td>
      <td>352</td>
      <td>96</td>
      <td>[33]</td>
    </tr>
    <tr>
      <td>1H-Mo₂C</td>
      <td>132</td>
      <td>15</td>
      <td>[38]</td>
    </tr>
    <tr>
      <td>Borophene</td>
      <td>496/596</td>
      <td>300/12</td>
      <td>[53]</td>
    </tr>
    <tr>
      <td>B₂H₂</td>
      <td>504</td>
      <td>90</td>
      <td>[35]</td>
    </tr>
    <tr>
      <td>Ca₂N</td>
      <td>1138</td>
      <td>80</td>
      <td>[34]</td>
    </tr>
    <tr>
      <td>Sr₂N</td>
      <td>283</td>
      <td>16</td>
      <td>[34]</td>
    </tr>
  </tbody>
</table>

## 4. Conclusion

Searching for suitable electrode materials with good performance is urgently needed for energy storage. In this work, we firstly reported a series of hexagonal 2D transition metal borides (TMBs) including Sc₂B₂, Ti₂B₂, V₂B₂, Cr₂B₂, Y₂B₂, Zr₂B₂, and Mo₂B₂ by using first-principles method and crystal structure prediction techniques. Through the calculated phonon spectra and DOS, we confirmed that these TMBs possess great stability and excellent electronic conductivity.

Then, we investigated the potential of 2D Ti₂B₂ monolayer as the anode material for LIBs and NIBs on the basis of first-principles simulations. The Ti₂B₂ monolayer shows negative adsorption energies for Li and Na of -0.674 and -0.879 eV, respectively, on the most stable S1 site. The calculated theoretical specific capacity values for Li on Ti₂B₂ monolayer is 456 mAhg⁻¹, which is larger than the well-established graphite, phosphorene, and Ti₃C₂. Interestingly, the theoretical specific capacity for Na is investigated to be 1027 mAhg⁻¹, which is much larger than

most other 2D materials. More excitingly, we found that the $Ti_2B_2$ monolayer shows very high Li and Na diffusivity with ultralow energy barrier of 0.017 and 0.008 eV, respectively, indicating an excellent charge-discharge capability for Li and Na. Moreover, the $Ti_2B_2$ monolayer was found to exhibit metallic nature after the adsorption of Li and Na ions at any concentrations, indicating that the $Ti_2B_2$ monolayer possesses an excellent electronic conductivity. Finally, the $Ti_2B_2$ monolayer just has a small change in volume after the adsorption of one, two, and three layers of Li and Na ions, indicating the robustness of this material.

Considering the above advantages, it is expected that the $Ti_2B_2$ monolayer and its alike materials would be used as anode materials for LIBs and NIBs with high specific capacity and fast diffusivity.

### Corresponding Author
*E-mail: wangbt@ihep.ac.cn

### Notes
The authors declare no competing financial interest.

### Acknowledgments
F.W.W. and J.R.Z. acknowledge financial support from National Natural Science Foundation of China under Grants No. 11675255, No. 11634008, and No. 11675195. J.R.Z. acknowledges financial support from The National Key Basic Research Program under Grants No. 2017YFA0403700. The calculations were performed at Supercomputer Centre in China Spallation Neutron Source.

### Supplementary information
Supplementary information associated with this article can be found in the online version at:
(I) Computational method, (II) metastable isomers of 2D $Ti_2B_2$, (III) lattice constants (Å) of the bulk $TMB_2$ phases and the 2D $TM_2B_2$ structures, (IV) DOS and phonon

dispersion curves of the other six 2D TM₂B₂, (V) snapshots and variation of the free energy for 2D Ti₂B₂ in the AIMD simulations from 300 to 3000 K, (VI) charge density difference plots for Na adsorption, (VII) 2D TiB₄ structures and the adsorption and diffusion of Li/Na on the hexagonal TiB₄ monolayer.

REFERENCES

[1] J.R. Miller, Science 335 (2012) 1312-1313.

[2] A.S. Aricò, P. Bruce, B. Scrosati, J.-M. Tarascon, W. van Schalkwijk, Nat. Mater. 4 (2005) 366-377.

[3] M. Armand, J.M. Tarascon, Nature 451 (2008) 652-657.

[4] D.P. Dubal, O. Ayyad, V. Ruiz, P. Gomez-Romero, Chem. Soc. Rev. 44 (2015) 1777-1790.

[5] Y. Idota, T. Kubota, A. Matsufuji, Y. Maekawa, T. Miyasaka, Science 276 (1997) 1395-1397.

[6] N. Oyama, T. Tatsuma, T. Sato, T. Sotomura, Nature 373 (1995) 598-600.

[7] P. Simon, Y. Gogotsi, B. Dunn, Science 343 (2014) 1210-1211.

[8] J.M. Tarascon, M. Armand, Nature 414 (2001) 359-367.

[9] M.S. Whittingham, Science 192 (1976) 1126-1127.

[10] Y. Wang, B. Liu, Q. Li, S. Cartmell, S. Ferrara, Z.D. Deng, J. Xiao, J. Power Sources 286 (2015) 330-345.

[11] A. Barré, B. Deguilhem, S. Grolleau, M. Gérard, F. Suard, D. Riu, J. Power Sources 241 (2013) 680-689.

[12] W. Luo, F. Shen, C. Bommier, H. Zhu, X. Ji, L. Hu, Accounts Chem. Res. 49 (2016) 231-240.

[13] N. Yabuuchi, K. Kubota, M. Dahbi, S. Komaba, Chem. Rev. 114 (2014) 11636-11682.

[14] H. Pan, Y.-S. Hu, L. Chen, Energ. Environ. Sci. 6 (2013) 2338-2360.

[15] M.D. Slater, D. Kim, E. Lee, C.S. Johnson, Adv. Funct. Mater. 23 (2013) 947-958.

[16] Y. Wang, R. Chen, T. Chen, H. Lv, G. Zhu, L. Ma, C. Wang, Z. Jin, J. Liu, Energ. Storage Mater. 4 (2016) 103-129.

[17] R. Zhao, J. Liu, J. Gu, Appl. Energ. 139 (2015) 220-229.

[18] Y. Lee, B. Son, J. Choi, J.H. Kim, M.-H. Ryou, Y.M. Lee, J. Power Sources 275 (2015) 712-719.

[19] M. Endo, C. Kim, K. Nishimura, T. Fujino, K. Miyashita, Carbon 38 (2000) 183-197.

[20] J.R. Dahn, T. Zheng, Y. Liu, J.S. Xue, Science 270 (1995) 590-593.

[21] M. Winter, J.O. Besenhard, M.E. Spahr, P. Novák, Adv. Mater. 10 (1998) 725-763.

[22] D.P. DiVincenzo, E.J. Mele, Phys. Rev. B 32 (1985) 2538-2553.

[23] S. Meini, R. Elazari, A. Rosenman, A. Garsuch, D. Aurbach, J. Phys. Chem. Lett. 5 (2014) 915-918.

[24] D. Takamatsu, T. Nakatsutsumi, S. Mori, Y. Orikasa, M. Mogi, H. Yamashige, K. Sato, T. Fujimoto, Y. Takanashi, H. Murayama, M. Oishi, H. Tanida, T. Uruga, H. Arai, Y. Uchimoto, Z. Ogumi, J. Phys. Chem. Lett. 2 (2011) 2511-2514.

[25] K. Song, D.-H. Seo, M.R. Jo, Y.-I. Kim, K. Kang, Y.-M. Kang, J. Phys. Chem. Lett. 5 (2014) 1368-1373.

[26] W. Sun, Y. Li, B. Wang, X. Jiang, M.I. Katsnelson, P. Korzhavyi, O. Eriksson, I. Di Marco, Nanoscale 8 (2016) 15753-15762.

[27] P.F. Liu, Y. Wu, T. Bo, L. Hou, J. Xu, H.J. Zhang, B.T. Wang, Phys. Chem. Chem. Phys. 20 (2018) 732-737.

[28] A. Gupta, T. Sakthivel, S. Seal, Prog. Mater. Sci. 73 (2015) 44-126.

[29] H.R. Jiang, Z. Lu, M.C. Wu, F. Ciucci, T.S. Zhao, Nano Energy 23 (2016) 97-104.

[30] C. Eames, M.S. Islam, J. Am. Chem. Soc. 136 (2014) 16270-16276.

[31] Q. Tang, Z. Zhou, P. Shen, J. Am. Chem. Soc. 134 (2012) 16909-16916.

[32] Y. Xie, M. Naguib, V.N. Mochalin, M.W. Barsoum, Y. Gogotsi, X. Yu, K.W. Nam, X.Q. Yang, A.I. Kolesnikov, P.R. Kent, J. Am. Chem. Soc. 136 (2014) 6385-6394.

[33] D. Er, J. Li, M. Naguib, Y. Gogotsi, V.B. Shenoy, ACS Appl. Mater. Interfaces 6 (2014) 11173-11179.

[34] J. Hu, B. Xu, S.A. Yang, S. Guan, C. Ouyang, Y. Yao, ACS Appl. Mater. Interfaces 7 (2015) 24016-24022.

[35] N.K. Jena, R.B. Araujo, V. Shukla, R. Ahuja, ACS Appl. Mater. Interfaces 9 (2017) 16148-16158.

[36] H.R. Jiang, W. Shyy, M. Liu, L. Wei, M.C. Wu, T.S. Zhao, J. Mater. Chem. A 5 (2017) 672-679.

[37] J. Liu, T. Zhao, S. Zhang, Q. Wang, Nano Energy 38 (2017) 263-270.

[38] Q. Sun, Y. Dai, Y. Ma, T. Jing, W. Wei, B. Huang, J. Phys. Chem. Lett. 7 (2016) 937-943.

[39] D. Wang, Y. Gao, Y. Liu, D. Jin, Y. Gogotsi, X. Meng, F. Du, G. Chen, Y. Wei, J. Phys. Chem.
C 121 (2017) 13025-13034.

[40] Y. Zhou, X. Zu, Electrochim. Acta 235 (2017) 167-174.

[41] L. Dong, H. Kumar, B. Anasori, Y. Gogotsi, V.B. Shenoy, J. Phys. Chem. Lett. 8 (2017)
422-428.

[42] R.P. Joshi, B. Ozdemir, V. Barone, J.E. Peralta, J. Phys. Chem. Lett. 6 (2015) 2728-2732.

[43] Q. Peng, Z. Wang, B. Sa, B. Wu, Z. Sun, ACS Appl. Mater. Interfaces 8 (2016) 13449-13457.

[44] Q. Peng, K. Hu, B. Sa, J. Zhou, B. Wu, X. Hou, Z. Sun, Nano Res. 10 (2017) 3136-3150.

[45] M. Liang, L. Zhi, J. Mater. Chem. 19 (2009) 5871-5878.

[46] G. Kucinskis, G. Bajars, J. Kleperis, J. Power Sources 240 (2013) 66-79.

[47] M. Mortazavi, C. Wang, J. Deng, V.B. Shenoy, N.V. Medhekar, J. Power Sources 268 (2014)
279-286.

[48] Y. Jing, Z. Zhou, C.R. Cabrera, Z. Chen, J. Phys. Chem. C 117 (2013) 25409-25413.

[49] G.A. Tritsaris, E. Kaxiras, S. Meng, E. Wang, Nano Lett. 13 (2013) 2258-2263.

[50] R. Zhang, X. Wu, J. Yang, Nanoscale 8 (2016) 4001-4006.

[51] W. Li, Y. Yang, G. Zhang, Y.-W. Zhang, Nano Lett. 15 (2015) 1691-1697.

[52] V.V. Kulish, O.I. Malyi, C. Persson, P. Wu, Phys. Chem. Chem. Phys. 17 (2015)
13921-13928.

[53] P. Liang, Y. Cao, B. Tai, L. Zhang, H. Shu, F. Li, D. Chao, X. Du, J. Alloy. Compd. 704 (2017)
152-159.

[54] M. Naguib, O. Mashtalir, J. Carle, V. Presser, J. Lu, L. Hultman, Y. Gogotsi, M.W. Barsoum,
ACS Nano 6 (2012) 1322-1331.

[55] M. Naguib, M. Kurtoglu, V. Presser, J. Lu, J. Niu, M. Heon, L. Hultman, Y. Gogotsi, M.W.
Barsoum, Adv. Mater. 23 (2011) 4248-4253.

[56] J. Halim, S. Kota, M.R. Lukatskaya, M. Naguib, M.-Q. Zhao, E.J. Moon, J. Pitock, J. Nanda,
S.J. May, Y. Gogotsi, M.W. Barsoum, Adv. Funct. Mater. 26 (2016) 3118-3127.

[57] K. Wang, Y. Zhou, W. Xu, D. Huang, Z. Wang, M. Hong, Ceram. Int. 42 (2016) 8419-8424.

[58] A. Mishra, P. Srivastava, H. Mizuseki, K.-R. Lee, A.K. Singh, Phys. Chem. Chem. Phys. 18 (2016) 11073-11080.

[59] M. Naguib, Y. Gogotsi, Accounts Chem. Re. 48 (2015) 128-135.

[60] Z. Guo, J. Zhou, Z. Sun, J. Mater. Chem. A 5 (2017) 23530-23535.

[61] S. Ma, K. Bao, Q. Tao, C. Xu, X. Feng, P. Zhu, T. Cui, Inorg. Chem. 55 (2016) 11140-11146.

[62] S.-Y. Xie, X.-B. Li, W.Q. Tian, N.-K. Chen, X.-L. Zhang, Y. Wang, S. Zhang, H.-B. Sun, Phys. Rev. B 90 (2014) 035447.

[63] Y. Wang, J. Lv, L. Zhu, Y. Ma, Phys. Rev. B 82 (2010) 094116.

[64] Y. Wang, M. Miao, J. Lv, L. Zhu, K. Yin, H. Liu, Y. Ma, J. Chem. Phys. 137 (2012) 224108.

[65] Y. Wang, J. Lv, L. Zhu, Y. Ma, Comput. Phys. Commun. 183 (2012) 2063-2070.

[66] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169-11186.

[67] G. Kresse, J. Furthmuller, Comp. Mater. Sci. 6 (1996) 15-50.

[68] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558-561.

[69] Z. Guo, J. Zhou, C. Si, Z. Sun, Phys. Chem. Chem. Phys. 17 (2015) 15348-15354.

[70] B. Anasori, M.R. Lukatskaya, Y. Gogotsi, Nat. Rev. Mater. 2 (2017) 16098.

[71] B.T. Wang, P. Zhang, H.L. Shi, B. Sun, W.D. Li, Eur. Phys. J. B 74 (2010) 303-308.

[72] S. Otani, Y. Ishizawa, J. Cryst. Growth 140 (1994) 451-453.

[73] H. Klesnar, T.L. Aselage, B. Morosin, G.H. Kwei, J. Alloy. Compd. 241 (1996) 180-186.

[74] H. P. Klesnar, P. Rogl, High Temp. High Press. 22 (1990) 453-457.

[75] L.N. Kugai, Inorg. Mater. 4 (1972) 669-670.

[76] B.-T. Wang, W. Zhang, W.-D. Li, Sci. Adv. Mater. 5 (2013) 1916-1921.

[77] G. Levchenko, A. Lyashchenko, V. Baumer, A. Evdokimova, V. Filippov, Y. Paderno, N. Shitsevalova, J. Solid State Chem. 179 (2006) 2949-2953.

[78] H. Zhang, Y. Li, J. Hou, A. Du, Z. Chen, Nano Lett. 16 (2016) 6124-6129.

[79] Z. Zhang, X. Liu, B.I. Yakobson, W. Guo, J. Am. Chem. Soc. 134 (2012) 19326-19329.

[80] L.M. Yang, V. Bacic, I.A. Popov, A.I. Boldyrev, T. Heine, T. Frauenheim, E. Ganz, J. Am. Chem. Soc. 137 (2015) 2757-2762.

[81] A. Molina-Sánchez, L. Wirtz, Phys. Rev. B 84 (2011) 155413.

[82] H. Liu, A.T. Neal, Z. Zhu, Z. Luo, X. Xu, D. Tománek, P.D. Ye, ACS Nano 8 (2014)

4033-4041.

[83] K.F. Mak, C. Lee, J. Hone, J. Shan, T.F. Heinz, Phys. Rev. Lett. 105 (2010) 136805.

[84] K. Toyoura, Y. Koyama, A. Kuwabara, F. Oba, I. Tanaka, Phys. Rev. B 78 (2008) 214303.

[85] P. Ganesh, J. Kim, C. Park, M. Yoon, F.A. Reboredo, P.R.C. Kent, J. Chem. Theory Comput.
10 (2014) 5318-5323.

[86] W.-J. Zhang, J. Power Sources 196 (2011) 13-24.

[87] W. Wenhui, Z. Qianfan, C. Yi, W. Enge, J. Phys. Condens. Mat. 22 (2010) 415501.

[88] C.-Y. Chou, H. Kim, G.S. Hwang, J. Phys. Chem. C 115 (2011) 20018-20026.

[89] K. Nakada, A. Ishii, Solid State Commun. 151 (2011) 13-16.

[90] C. Ling, F. Mizuno, Phys. Chem. Chem. Phys. 16 (2014) 10419-10424.

[91] B. Ziebarth, M. Klinsmann, T. Eckl, C. Elsässer, Phys. Rev. B 89 (2014) 174301.

[92] X. Qu, J. Yang, Y. Wang, J. Lv, Z. Chen, Y. Ma, Nanoscale 9 (2017) 17983-17990.

Graphical Abstract:

![](./images/867763539677282965_10.jpg)