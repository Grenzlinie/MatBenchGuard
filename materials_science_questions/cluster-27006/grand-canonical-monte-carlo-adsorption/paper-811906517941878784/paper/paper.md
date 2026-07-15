THE JOURNAL OF CHEMICAL PHYSICS 129, 075105 (2008)

# Water in hydrated orthorhombic lysozyme crystal: Insight from atomistic simulations

Zhongqiao Hu, Jianwen Jiang, $^{\text{a)}}$ and Stanley I. Sandler

Department of Chemical and Biomolecular Engineering, National University of Singapore, Singapore 117576, Singapore and Department of Chemical Engineering, University of Delaware, Newark, Delaware 19716, USA

(Received 21 April 2008; accepted 21 July 2008; published online 21 August 2008)

Biologically important water in orthorhombic lysozyme crystal is investigated using atomistic simulations. A distinct hydration shell surrounding lysozyme molecules is found from the number distribution of water molecules. While the number of water molecules in the hydration shell increases, the percentage decreases as the hydration level rises. Adsorption of water in the lysozyme crystal shows type-IV behavior. At low hydration levels, water molecules primarily intercalate the minor pores and cavity in the crystal due to the strong affinity between protein and water. At high hydration levels, the major pores are filled with liquidlike water as capillary condensation occurs. A type-H4 hysteresis loop is observed in the adsorption and desorption isotherms. The locations of the water molecules identified from simulation match fairly well with the experimentally determined crystallographic hydration sites. As observed in experiment, water exhibits anomalous subdiffusion because of the geometric restrictions and interactions of protein. With increasing hydration level, this anomaly is reduced and the diffusion of water tends to progressively approach normal Brownian diffusion. The flexibility of protein framework slightly enhances water mobility, but this enhancement decreases with increasing hydration level. © 2008 *American Institute of Physics.*

[DOI: 10.1063/1.2969811]

## I. INTRODUCTION

Protein crystals have recently emerged as fascinating nanoporous biomaterials for separation and purification. $^{1}$ For example, good resolution for chemically or optically different molecules through size exclusion or chiral discrimination has been observed in high performance liquid chromatography using a thermolysin crystal as the stationary phase. $^{2}$ The penetration of sodium fluorescein in lysozyme crystals (monoclinic, triclinic, and orthorhombic) measured by confocal laser scanning microscopy revealed that the diffusion rates in three orthogonal directions are different as a result of the complex morphology and anisotropy of crystalline structures. $^{3,4}$

While protein crystals have several features in common with the inorganic counterparts (e.g., zeolites), their biological nature offers more control over pore size, porosity, and surface properties. There exists a wide range of controllable pore sizes (1.5–10 nm) and porosities (0.5–0.8) in protein crystals. Naturally occurring $L$-amino acids create a chiral environment, which could lead to the separation of biological and pharmaceutical molecules. In the past, the applications of protein crystals were severely restricted by their fragility and unpredictable growth patterns. However, these problems have been solved to some degree, as chemically and mechanically stable protein crystals can be made by cross-linking techniques. The local charge and hydrophobicity microenvironment of protein crystals can be modified by designed techniques in protein chemistry or by the crystallization method. $^{5}$ An extremely large number of proteins exist in crystalline forms and that provides unlimited opportunities for new applications of protein crystals.

Current understanding of the microscopic behavior of fluids confined in protein crystals is largely incomplete, but insight into such behavior is crucial to their applications. With ever-increasing computational power, atomistic simulations have become increasingly important in the life sciences. At the atomic level, simulations can provide insightful information that would otherwise be experimentally difficult or impossible to obtain and immensely useful in complementing experimental studies. Earlier simulations of protein crystals were primarily focused on the difference of protein conformations in solution and crystalline environments. $^{6-10}$ Only recently have there been a few studies examining fluids in protein crystalline pores. The effective diffusion coefficient of water in tetragonal lysozyme crystal was estimated by a random-walk algorithm, and the reduction in diffusion was attributed to steric limitations. $^{11}$ The diffusion of spherical probes in lysozyme crystals was simulated by dynamic Monte Carlo and Brownian dynamics; the electrostatic interaction and steric confinement were found to restrict the mobility. $^{12}$ The diffusion rates of small molecules into protein crystals were evaluated using a phenomenological model in which the physical and chemical properties of both protein crystal and diffusing molecules were considered. $^{13}$ The spatial and temporal properties of water and counter-ions were simulated in three fully hydrated protein crystals with different morphologies and topologies. The mobility was found to

$^{\text{a)}}$Author to whom correspondence should be addressed. Electronic mail: chejj@nus.edu.sg.

0021-9606/2008/129(7)/075105/5/$23.00

129, 075105-1

© 2008 American Institute of Physics

be enhanced by increasing porosity and by protein flexibility. $^{14}$

In this work, atomistic simulations [both Monte Carlo and molecular dynamics (MD)] have been performed to investigate the mechanistic behavior of water in a partially hydrated orthorhombic lysozyme crystal. Lysozyme is a readily available protein with well-known structure. As the "matrix of life," water plays a biologically important role in determining the structure, dynamics, and functionality of proteins. Consequently, a clear understanding of water in protein crystal is of importance. To mimic the hydration of the lysozyme crystal in a humid atmosphere, the adsorption of water was determined from the Monte Carlo simulation. The number distribution of water molecules around lysozyme molecules was calculated as a function of hydration level. From MD simulation, the locations of water molecules were identified and compared to the available experimental hydration sites. Also, the diffusion of water in the crystal was examined at different hydration levels.

## II. MODEL AND METHODOLOGY

The crystal structure of orthorhombic lysozyme was constructed from the experimental crystallographic data (PDB ID: 1AKI). $^{15}$ In the crystallization of orthorhombic lysozyme, the $pH$ of lysozyme solution was initially at 4.5 and then adjusted to 9.6. Large crystals grew in 3 months, at which time the $pH$ dropped to 7.5. $^{15}$ Therefore, in our study the $pH$ was assumed to be neutral. At this $pH$, Arg and Lys residues are protonated, while Asp and Glu residues are deprotonated, leading to eight positive unit charges in a lysozyme molecule. $^{16}$ The major pore between lysozyme molecules in the crystal is approximately rectangular along the $z$-axis with pore dimensions of about $2.2 \times 1.3$ nm$^2$. There is a wide distribution of minor pores and cavities in the crystal, which are interconnected. The simulation box contained two unit cells with eight lysozyme molecules and 64 $Cl^-$ counter-ions. Periodic boundary conditions were applied in three dimensions to represent an infinitely large crystal. The free volume $V_{\text{free}}$ within the crystal was estimated from $V_{\text{free}} = \int_V \exp[-u_{\text{ad}}(\mathbf{r})/k_{\text{B}}T]d\mathbf{r}$, where $u_{\text{ad}}$ is the interaction between a helium atom and the crystal framework. Helium is a nonadsorbing species and commonly used as a probe to estimate the free volume of porous materials. In our calculation, the Lennard-Jones collision diameter $\sigma_{\text{He}}$ $=2.58$ Å and the well-depth $\varepsilon_{\text{He}}/k_{\text{B}}=10.22$ K for helium were used. $^{17}$ The porosity was calculated by $V_{\text{free}}/V_{\text{total}}$, in which $V_{\text{total}}$ is the total occupied volume. The porosity estimated in this way for the lysozyme crystal is approximately 0.45, indicating a highly porous structure.

When a dry protein crystal is exposed to a humid atmosphere, hydration or adsorption of water occurs. In our study, water adsorption in the lysozyme crystal was examined at ambient temperature and pressure (300 K and 1 bar). The extent of adsorption was determined as a function of relative humidity (RH), defined as the partial pressure of water vapor in the air to the saturated vapor pressure (3.1 kPa at 300 K). The adsorption was simulated using the grand canonical Monte Carlo (GCMC) method, which has been widely used in the simulation of adsorption as it naturally mimics an open system in equilibrium with bulk fluid reservoir. $^{18}$ Compared to highly polar water molecule, $O_2$ and $N_2$ in the atmosphere interact with lysozyme molecules very weakly. Consequently, the adsorption of $O_2$ and $N_2$ in the lysozyme crystal was neglected. Water was represented by a three-site rigid molecule with transferable intermolecular potential-three point (TIP3P). $^{19}$ The vapor pressures of water were low ($\leq$3.1 kPa) at the conditions considered here so that water in the reservoir was assumed to behave as an ideal gas. Lysozyme was modeled with the atomistic assisted model building with energy refinement (AMBER) 2003 force field. $^{20}$ The crystalline framework was assumed to be rigid during GCMC simulation, but the counter-ions were allowed to move. In the simulation of adsorption, low-energy equilibrium configurations are involved and structural flexibility has only a marginal effect. The interactions between water with lysozyme were modeled using the Lennard-Jones and Coulombic potentials. A cutoff 1.4 nm was used in the evaluation of the Lennard-Jones interactions with long-range corrections added. The Ewald sum with a tin-foil boundary condition was used for the Coulombic interactions. $^{21}$ The real/reciprocal space partition parameter and the maximum reciprocal lattice vectors were chosen to be 0.2 and 10 to ensure rapid convergence. A typical simulation was performed for 20 000 cycles, in which the first 10 000 cycles were used for equilibration and the remaining 10 000 cycles were used to compute ensemble averages. Each cycle consisted of 5000 attempted trial moves. Four types of trial moves were used separately for water molecules with the following probabilities: 15% translation, 15% rotation, 15% regrowth, and 55% exchange with the reservoir. For the $Cl^-$ counter-ions, only translation and regrowth moves were used.

Diffusion of water was simulated using MD with Groningen machine for chemical simulations (GROMACS) v3.3.1 package. $^{22}$ Water was again represented by a three-site rigid molecule with the TIP3P potential $^{19}$ and its geometry was constrained using the SETTLE algorithm. As in the adsorption simulation, lysozyme was modeled using the AMBER 2003 force field. $^{20}$ The bond lengths with dangling hydrogen atoms in lysozyme molecules were constrained using the LINCS algorithm. The Lennard-Jones and Coulombic interactions were calculated separately with a cutoff of 1.4 nm and the particle mesh Ewald (PME) method. $^{23,24}$ In PME, the sum in the reciprocal space is evaluated using the fast Fourier transformation method with convolutions on a grid, to which charges are interpolated. A 0.12 nm grid and a fourth-order interpolation in the PME method were used here. To estimate the effect of lysozyme flexibility on water diffusion, two sets of simulations were performed at various RHs, one with the rigid framework at 300 K (NVT ensemble) and the other with the flexible framework at 300 K and 1 bar (NPT ensemble). The transformation of lysozyme crystal structure was thus investigated at different hydration levels. For each simulation set, the system was subject to energy minimization using the steepest decent method with a force tolerance of 1.0 kJ mol$^{-1}$ nm$^{-1}$, then the initial velocities were generated according to the Maxwell-Boltzmann distribution at

![](./images/811906517941878784_1.jpg)

FIG. 1. (Color) Snapshots of water adsorption in the lysozyme crystal at RH=5%, 20%, 50%, and 80%, respectively. Water molecules are in blue and Cl⁻ counter-ions are in green. The secondary structures of lysozyme: a-helices (red), β-sheets (cyan), and random coils (gray).

300 K. MD simulations were conducted in Berendsen thermostat with a relaxation time of 0.1 ps for both rigid and flexible frameworks and in Berendsen barostat with a relaxation time of 1 ps for the flexible framework. The total duration for one MD simulation was 5.5 ns with an integration time step of 2 fs. By monitoring the potential energy, the system was found to reach equilibrium in less than 0.5 ns, therefore, the final 5 ns was used for subsequent analysis.

## III. RESULTS AND DISCUSSION

Figure 1 shows simulation snapshots of water adsorption in the lysozyme crystal at RHs=5%, 20%, 50%, and 80% respectively. At low RHs, water molecules mainly intercalate the minor pores and cavities in the crystal and only a few water molecules exist in the major pores. This is attributed to the strong interaction between protein and water molecules. Proteins are studded with charges on their backbone carbonyl and amino groups, as well as on their side chains. The net charge on a lysozyme molecule is +8e at pH=7. The charges have a substantial effect on the lysozyme-water interaction. As a consequence, water is strongly attracted to the lysozyme surface. With increasing RH from 5% to 20% and on to 50%, water density is observed to increase in the crystal, but the major pore remains largely unoccupied. At RH=80%, however, the major pores are filled with liquidlike water molecules implying the occurrence of capillary condensation. As we shall see below, such behavior results in hysteresis. The locations of some Cl⁻ ions are found to be approximately the same at different RHs. This reveals that these Cl⁻ ions are nearly immobile and have strong interactions with the lysozyme molecules.

The hydrated protein is surrounded by water hydration shell in the vicinity of protein surface, which largely governs the structure, functionality and reactivity of protein.²⁵,²⁶ In our study, the hydration level is expected to influence water population in the hydration shell. To characterize this, the number distribution $N_n(r)$ of water molecules was calculated as a function of distance $r$ between water and the nearest protein atom. $N_n(r)$ is defined as $\langle\delta N(r)\rangle/(\delta r N_t)$, where $\langle\delta N(r)\rangle$ is the ensemble averaged number of water molecules within a layer of thickness $\delta r$, and $N_t$ is the total number of water molecules in the system. In our calculation, $\delta r$ was set equal to 0.01 nm and the van der Waals radius of each protein atom was taken into account. Figure 2 shows $N_n(r)$ at RHs=5%, 20%, 50%, and 80% respectively. A pronounced peak in $N_n(r)$ is observed at about 0.13 nm from the protein surface, which is close to the radius (0.14 nm) of a water molecule. This reveals the existence of a hydration shell surrounding lysozyme. If the shell thickness was set to 0.28 nm, about the size of a water molecule, the percentages of water within the hydration shell were about 99.4%, 97.9%, 94.2%, and 79.4% respectively at RHs=5%, 20%, 50%, and 80%. Although number of water molecules in the hydration shell is the lowest at RH=5%, the percentage of almost 100% is the highest. Consequently, at a low hydration level, the water molecules reside almost exclusively in the hydration shell. With increasing hydration level, the number of water molecules increases in the hydration shell and finally approaches saturation. Upon further increasing hydration level, water molecules start to reside away from the protein surface.

Figure 3 shows the isotherm of water in the lysozyme crystal as a function of RH. The adsorption belongs to type-IV (sigmoid) behavior according to the International Union of Pure and Applied Chemists classification. At low RHs(<5%), adsorption increases sharply indicating strong interactions between water and lysozyme. This is remarkably different from the adsorption of water in hydrophobic activated carbons or carbon nanotubes. As mentioned earlier,

![](./images/811906517941878784_2.jpg)

FIG. 2. (Color online) Number distributions of water molecules as the function of distance from lysozyme surface at RH=5%, 20%, 50%, and 80%, respectively. The values in parentheses are the percentages of water molecules in the hydration shell.

![](./images/811906517941878784_3.jpg)

FIG. 3. Adsorption (upper triangles) and desorption (lower triangles) isotherms of water as a function of RH. The inset is in the semilogarithmic scale.

protein molecules have strong affinity to water molecules because of charges. Adsorption increases gradually with increasing RH at RH>5%, and a bit more rapidly in the range of RH≈(60%,80%). Upon further increasing RH, adsorption is nearly saturated and only increases marginally. To study dehydration, the desorption of water was also simulated. As shown in Fig. 3, a hysteresis of type H4 is observed based on the adsorption and desorption isotherms. Hysteresis associated with the pore filling draining suggests the existence of metastable states and local minima in the grand free energy of the system. The states above the upper closure point or below the lower closure point are thermodynamically stable. For the hysteresis loop observed here, the upper closure point is close to the saturation pressure of water. This is different from type-H1 and type-H2 hystereses, which exhibit steep adsorption and /or desorption branches, and is often seen experimentally for a simple nonpolar gas (Ar, N₂, O₂, etc) in mesoporous materials (MCM-41 and SBA-15).²⁷

Figure 4 is a binocular three-dimensional view for the locations of water molecules in the vicinity of a lysozyme molecule. The hydration level is 78 water molecules per lysozyme, identical to the number of the hydration sites measured by x-ray diffraction (green spheres). It is usually difficult to accurately predict water molecules in a crystal by modeling and simulation. Despite some deviations, the locations of the hydrated water molecules from our MD simulation (in blue) match fairly well with the experimental crystallographic sites (in green). Additionally, the hydrated water molecules are found to locate preferentially near the charged residues, with which water molecule interacts more strongly.

<table>
<caption>TABLE I. Crystal lattice parameters at different RHs.</caption>
<thead>
<tr>
<th>Hydration level</th>
<th>a (nm)</th>
<th>b (nm)</th>
<th>c (nm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RH=5%</td>
<td>5.46</td>
<td>6.33</td>
<td>5.64</td>
</tr>
<tr>
<td>RH=20%</td>
<td>5.52</td>
<td>6.39</td>
<td>5.70</td>
</tr>
<tr>
<td>RH=50%</td>
<td>5.59</td>
<td>6.48</td>
<td>5.77</td>
</tr>
<tr>
<td>RH=80%</td>
<td>5.81</td>
<td>6.73</td>
<td>6.02</td>
</tr>
<tr>
<td>Native</td>
<td>5.91</td>
<td>6.85</td>
<td>6.10</td>
</tr>
</tbody>
</table>

Table I lists the lattice parameters of the lysozyme crystal simulated at different RHs. A slight contraction of the crystal is observed compared to the native structure. The contraction of the lattice length from the native structure is about 7% at RH=5%, and reduces to 2% at RH=80%. The lattice length in each dimension increases with increasing RH.

Mobility of water in the lysozyme crystal was examined by calculating the mean square displacement (MSD) defined as MSD=⟨|$\vec{\text{r}}(t)$−$\vec{\text{r}}(0)$|²⟩, where the $\vec{\text{r}}(t)$ are the positions of the centers of mass of water molecules at time t and ⟨…⟩ refers to the ensemble average. Figure 5 shows the MSDs of water as a function of time at hydration levels of RH=5%, 20%, 50%, and 80% for both rigid and flexible frameworks. At a given RH, the MSD increases monotonically with time as the water molecules are driven away from their initial locations by thermal motion. At a fixed time, the MSD is greater with increasing RH, indicating the important effect of the hydration level. At a low RH, water molecules are strongly bound due to their high affinity for the protein surface, and hence the water mobility is small. At a high RH, the binding sites are almost saturated and additional water

![](./images/811906517941878784_4.jpg)

FIG. 4. (Color) Binocular three-dimensional view for the locations of water molecules at a hydration level of 78 water molecules per lysozyme. The blue spheres are from MD simulation of this work, and the green spheres indicate the crystallographic sites from x-ray diffraction.

![](./images/811906517941878784_5.jpg)

FIG. 5. Color online Mean square displacements of water at RH=5%, 20%, 50%, and 80%, respectively, with the rigid and flexible frameworks. $\gamma$ is the exponent in the power law $t^{\gamma}$.

molecules are farther away from the protein surface. Conse- quently, the attraction between the protein and these water molecules is weaker and the water mobility increases. This is consistent with the findings of the number distributions dis- cussed earlier. The MSDs of water can be correlated as a power law versus time, i.e., $MSD \propto t^{\gamma}$. The exponent $\gamma$ was evaluated by fitting the MSD data over the time range from 10 to 100 ps. At RHs=5%, 20%, 50%, and 80%, $\gamma$ are 0.66, 0.77, 0.81, and 0.87, respectively. This indicates anoma- lous subdiffusion for water in the lysozyme crystalline struc- ture, resulting from the physical interactions and geometric restrictions of protein. With increasing RH, $\gamma$ increases pro gressively to unity and water diffusion tends to approach a normal Brownian motion. Such behavior was also observed in hydrated water molecules around plastocyanin a copper containing protein), $^{28}$ and is consistent with the neutron scattering analysis for hydrated water around myoglobin. $^{29}$ Compared to the results for the rigid lysozyme framework, the flexible framework exhibits slightly enhanced water mo- bility. At each hydration level, the exponent $\gamma$ for flexible framework is marginally larger. Nevertheless, the degree of enhancement drops with increasing hydration level. For ex- ample, at a high RH=80%, the flexible framework has a negligible impact on water mobility.

## IV. SUMMARY

The simulation study provides an insight into the mo- lecular behavior of water in a partially hydrated orthorhom- bic lysozyme crystal. Because of the strong affinity with pro- tein molecules, water is strongly bound to the crystal surface. The majority of water molecules are found to reside in a hydration shell surrounding lysozyme, and the percentage of water molecules in the shell drops with increasing hydration level. Water in the crystal exhibits type-IV adsorption behav- ior and type-H4 hysteresis. The simulated locations of water molecules agree well with the experimental hydration sites. Anomalous diffusion is observed for water in the crystal and its mobility increases with hydration level. The flexibility of protein framework enhances water mobility, but the influence appears to vanish at high hydration levels. This work reveals the importance of the hydration level in the adsorption and diffusion of water molecules in the lysozyme crystal. The hydration level could play a key role in governing protein functionality as it alters the rate at which water, and therefore also a substrate can reach the active site of protein molecule.

## ACKNOWLEDGMENTS

We are grateful to the National University of Singapore Grant No. R-279-000-238-112 for the support.

$^{1}$ A. L. Margolin and M. A. Navia, Angew. Chem., Int. Ed. 40, 2204 2001.

$^{2}$ L. Z. Vilenchik, J. P. Griffith, N. St Clair, M. A. Navia, and A. L. Mar- golin, J. Am. Chem. Soc. 120, 4290 1998.

$^{3}$ A. Cvetkovic, M. Zomerdijk, A. J. J. Straathof, R. Krishna, and L. A. M. van der Wielen, Biotechnol. Bioeng. 87, 658 2004.

$^{4}$ A. Cvetkovic, A. J. J. Straathof, R. Krishna, and L. A. M. van der Wielen, Langmuir 21, 1475 2005.

$^{5}$ U. Ryde and K. Nilsson, J. Am. Chem. Soc. 125, 14232 2003.

$^{6}$ W. F. van Gunsteren, H. J. C. Berendsen, J. Hermans, W. G. J. Hol, and J. P. M. Postma, Proc. Natl. Acad. Sci. U.S.A. 80, 4315 1983.

$^{7}$ A. P. Heiner, H. J. C. Berendsen, and W. F. Vangunsteren, Proteins: Struct., Funct., Genet. 14, 451 1992.

$^{8}$ R. Walser, P. H. Hunenberger, and W. F. van Gunsteren, Proteins: Struct., Funct., Genet. 48, 327 2002.

$^{9}$ H. B. Yu, M. Ramseier, R. Burgi, and W. F. van Gunsteren, ChemPhy- sChem 5, 633 2004.

$^{10}$ D. M. York, T. A. Darden, L. G. Pedersen, and M. W. Anderson, Biochemistry 32, 1443 1993.

$^{11}$ V. N. Morozov, G. S. Kachalova, V. U. Evtodienko, N. F. Lanina, and T. Y. Morozova, Eur. Biophys. J. 24, 93 1995.

$^{12}$ K. Malek, T. Odijk, and M. O. Coppens, ChemPhysChem 5, 1596 2004.

$^{13}$ S. Geremia, M. Campagnolo, N. Demitri, and L. N. Johnson, Structure 14, 393 2006.

$^{14}$ Z. Q. Hu and J. W. Jiang, Langmuir 24, 4215 2008.

$^{15}$ P. J. Artymiuk, C. C. F. Blake, D. W. Rice, and K. S. Wilson, Acta Crystallogr. 38, 778 1982.

$^{16}$ D. E. Kuehner, J. Engmann, F. Fergg, M. Wernick, H. W. Blanch, and J. M. Prausnitz, J. Phys. Chem. B 103, 1368 1999.

$^{17}$ J. O. Hirschfelder, C. F. Curtiss, and R. B. Bird, Molecular Theory of Gases and Liquids Wiley, New York, 1964.

$^{18}$ D. Frenkel and B. Smit, Understanding Molecular Simulations: From Algorithms to Applications, 2nd ed. Academic, San Diego, 2002.

$^{19}$ W. L. Jorgensen, J. Am. Chem. Soc. 103, 335 1981.

$^{20}$ Y. Duan, C. Wu, S. Chowdhury, M. C. Lee, and G. M. Xiong, J. Comput. Chem. 24, 1999 2003.

$^{21}$ D. M. Heyes, Phys. Rev. B 49, 755 1994.

$^{22}$ D. Van der Spoel, E. Lindahl, B. Hess, G. Groenhof, A. E. Mark, and H. J. C. Berendsen, J. Comput. Chem. 26, 1701 2005.

$^{23}$ T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089 1993.

$^{24}$ D. M. York, A. Wlodawer, L. G. Pedersen, and T. A. Darden, Proc. Natl. Acad. Sci. U.S.A. 91, 8715 1994.

$^{25}$ F. Merzel and J. C. Smith, Proc. Natl. Acad. Sci. U.S.A. 99, 5378 2002.

$^{26}$ D. I. Svergun, S. Richard, M. H. J. Koch, Z. Sayers, S. Kuprin, and G. Zaccai, Proc. Natl. Acad. Sci. U.S.A. 95, 2267 1998.

$^{27}$ A. Grosman and C. Ortega, Langmuir 21, 10515 2005.

$^{28}$ A. R. Bizzarri and S. Cannistraro, Phys. Rev. E 53, R3040 1996.

$^{29}$ M. Settles and W. Doster, Faraday Discuss. 103, 269 1996.

The Journal of Chemical Physics is copyrighted by the American Institute of Physics (AIP). Redistribution of journal material is subject to the AIP online journal license and/or AIP copyright. For more information, see http://ojps.aip.org/jcpo/jcpcr/jsp