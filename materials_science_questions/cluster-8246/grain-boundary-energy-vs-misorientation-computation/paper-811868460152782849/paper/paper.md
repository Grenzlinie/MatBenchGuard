# Mechanics of Superplastic Deformations at Atomic Scale

N. Chandra

Department of Mechanical Engineering, FAMU-FSU College of Engineering, Florida State University, Tallahassee, FL 32310, USA

**Keywords:** Atomistic Simulation, Embedded Atom Method (EAM), GBS, CSL, DSC

## ABSTRACT

The behavior of materials can be modeled at different hierarchical levels with varying spatial scales as shown in Figure 1. A structure or a specimen with a scale greater than $10^{-3}m$ represents the macroscopic scale where the principle of continuum mechanics is generally used. At this level, only materials macrostrcuture and global properties are considered; At the other extreme, atomic scale spans the lengths of a few nanometers $(10^{-9}-10^{-6}m)$, which is compatible with the length scale of crystalline defects (e.g. vacancy, impurity, dislocation, grain boundary and interface). Though at this level the structure cannot be directly related to the macro-level property, it provides very useful information for an understanding of mesoscopic $(10^{-6}-10^{-3}m)$ behavior. In order to understand the origin of superplasticity, it is important to understand the mechanics of grain boundary sliding, considere the primary source of the large strain. An appropriate scale to study grain boundary sliding is the atomic scale and is the focus of this paper. In the atomistic simulation, interatomic potentials using Embedded Atom Method (EAM) are used in conjunction with molecular statics calculations. Atomistic simulations are performed on a series of grain boundary structures in aluminum, and the energies associated with each of their equilibrium configurations are computed. The propensity for grain boundary sliding (GBS) is also evaluated by computing the energy associated with incremental equilibrium configurations during the sliding process, and GBS is compared with GB cleavage based on the energy consideration. It is also shown that in certain types of grain boundaries, GBS is always accompanied by GB migration. Also the amount of sliding and migration is proportional to the applied force levels, grain boundary energy and time.

## INTRODUCTION

A considerable work has been done in the macroscopic level modeling of SPF [1-3]. The modeling methods are based on the principles of continuum mechanics and can be numerically implemented using either simplified methods or finite element methods (FEM). Processing modeling is a tool used to study the effect of various parameters and to determine the optimum conditions for forming of various shapes. An uniform thinning model developed by N. Chandra and D. Kannan [2], and applied to a superplastic formed cone from Al-8090 sheet metal, is shown in Figure 2 along with the prescribed pressure - time profile.

The high-temperature deformation behavior of superplastic materials is characterized by a sigmoidal curve (regions I, II and III) spanning about seven to eight decades of strain rate in the log $\sigma$ - log $\dot{\epsilon}$ plot. A micromechanical polycrystalline model developed at grain-level [4-7] was extended to describe the material behavior in all the three regions by incorporating a threshold stress term (denoted by $\sigma_{*}$ in the slip plane level) [4]. This model is developed from the grain level to the level of the aggregate in an explicit manner (using self-consistent method). It computes the overall strain rate as the sum of the strain rates contributed by diffusions (lattice and boundary diffusions) and dislocations. The details of the mesoscale model is fully described in References 4 and 7. Figure 3

shows the predictive capability of the model when the temperature is varied, and Figure 4 when the grain size is varied. The model predictions are compared with the experimental data. It should be noted that in the numerical simulation all the material parameters are obtained based on a single experimental curve at a specific temperature and grain size.

The above two models represented analysis at the macroscopic and mesoscopic scales. They are incapable of providing insight into the structure, energy of the grain boundary (GB), or the mechanics of the process of GB sliding. We need to approach the problem at the atomistic scale using molecular statics and dynamics methods. Over the years, despite the important role of grain boundaries (GB) in influencing materials properties, such as superplasticity [8], our knowledge of how boundaries actually move at the microscopic level is limited. Much of the difficulty is due to the lack of a suitable means of observing the dynamical process (such as sliding and migration) with sufficient spatial and time resolution. One approach that has provided atomic-level insights in GB in metals is atomistic simulations. Though considerable work [9-17] has been done in recent years to study the equilibrium structures of grain boundaries using atomistic simulations, very limited research has focused on the atomistic simulation of grain boundary sliding (GBS) and migration. Yip and coworkers [18-20] studied grain boundary migration and sliding due to high temperature effect using pair-like potentials. They observed both migration and sliding purely due to the applied temperature. In general, however, the driving force for grain boundary movement is the internal strain and stress field [17]. Unfortunately there are very few studies having been done on grain boundary mobility under applied strains or stresses at atomic level. Very recently Molteni et al. [21] conducted an ab initio simulation of grain boundary sliding in germanium in a quasi-static way, by applying constant strain increment to one crystal of the bi-crystal boundaries. The problem with applied strain instead of stress is, as we will see in the present work, that the migration process is prevented. Such a preconstrained process experiences much larger energy barrier than a coupled sliding and migration process.

The main purpose of this paper is to understand the mechanics of deformation of symmetric tilt grain boundaries (STGB) of aluminum at the atomic level. In order to achieve this, the atomistic simulation methods and the interatomic potentials were first introduced. Based on the equilibrium GB structures obtained by energy minimization, grain boundary mobility (sliding and migration) was then simulated under both applied displacement and applied force conditions. The energetic and displacement fields associated with applied displacement and applied force were examined to elucidate the importance of coupled sliding and migration process.

## ATOMISTIC SIMULATION METHOD

Since GBS and GB migration are the interest of this work, grain boundaries are modeled as planar bicrystalline high-angle structures specified by coincident site lattice (CSL) models. High-angle grain boundaries (misorientation angle $\theta > 15^o$) are associated with higher grain boundary energy and are generally thought to promote GBS [8]. CSL grain boundaries are found to naturally occur in all polycrystalline materials, and their frequency of occurrence is strongly dependent on the processing history [22]. As the consequence of the CSL model, the lowest-energy grain boundary structure for a given misorientation (characterized by $\Sigma$) is postulated to be the symmetrical configuration. Figure 5 (case I) illustrates the designations of symmetric tilt grain boundaries (STGB) used throughout this work. In this figure the misorientation angle $\theta$ is computed from the two [001] directions of each of the bicrystals. For each of the CSL boundaries, the computational crystal was generated based on the orientation of a given grain and the symmetry between that and the adjacent grain across the boundary plane. The computational crystal composed of about 5000 atoms with approximate 35 atomic layers (in y-direction) in each grain.

A DYNAMO program developed at the Sandia National Laboratory Livermore [23] incorporated with the Embedded Atom Method (EAM) is used in this work. It has been proven that EAM potentials are more reliable in representing atomic interactions in metallic systems [15-16] than traditional pair potentials. The analytical EAM functions developed by Oh and Johnson [24] will be adopted in this work. At first, molecular statics (energy minimization) was carried out to obtain the equilibrium structures of grain boundaries. Since grain boundaries are extended defects in two dimensions, but inhomogeneous in the direction normal to the grain boundary plane, it is usual to construct a computational crystal that is periodic only in 2-D plane of the interface (x-

and z- directions in this work). In the grain boundary normal direction (y-direction), free-surface boundary conditions are imposed. Consequently, the crystals are designed to be large enough in y-direction to remove the free surface effects on the grain boundary structure. By minimizing the total energy of the crystal at 0 K under these boundary conditions, the equilibrium GB structures were obtained and next used as the input configurations for the study of grain boundary mobility under applied displacement and forces.

When applying displacement (Figure 5), specified levels of incremental displacements are applied to each of the atoms in the top grain and all the atoms in the bottom grain remain free. It is adequate to use free-surface boundary conditions in the grain boundary normal direction (y-direction). After each increment the configuration was relaxed using molecular statics to its local equilibrium state. When forces are applied on all the atoms in the top grain (Figure 6), it simulates the actual motion of the top grain as a single unit over the bottom grain. In this case, it is necessary to restrict the motion along the two surfaces in y-direction, which is achieved by setting y-displacement to zero on the atoms near the upper surface (four outmost layers in y direction) and fixing the bottom surface (four outmost layers in -y direction). These boundary conditions assure the simulation were performed at a constant volume condition. In this case molecular dynamics is used to study the time-related phenomena for structures subjected to external forces. As will be evident later, application of displacements and force yield different responses; displacement causes"pure" GBS whereas force induces sliding and migration. Though only the results for $\Sigma 3(1 \overline{1} 1)$ were given below for brevity, the effect of different GB structures (therefore GB energies) on GBS will also be discussed.

### GBS UNDER APPLIED DISPLACEMENT

Under the applied displacement conditions, grain boundary migration (atomic movement in the direction normal to the applied displacement direction) was virtually constrained. A "pure" GBS process is thus implemented by applying constant displacements, each increment followed by a complete relaxation (energy minimization) of the boundary structure. Since the CSL grain boundary structure studied in this work can be obtained by repeating the CSL cell in x- and z- directions, the structure with a displacement of $a_{CSL}$ ($a_{CSL}$ is the lattice parameter of the CSL cell in x-direction) is equivalent to the initial undisplaced structure under the periodic conditions described above. Therefore the total displacement in each case is limited to the value of $a_{CSL}$ for the given grain boundary. The increments (described in percentage of $a_{CSL}$) are selected to be small enough to capture all the energy jumps. After each increment the configuration is relaxed to its local equilibrium state and the grain boundary energy is computed. The grain boundary energy profile associated with the GBS process then provides the tool necessary to predict the grain boundary mobility.

Figure 5 shows the energy profile of "pure" GBS process in $\Sigma 3(1 \overline{1} 1)$ twin structure. It is seen from Figure 5 that there are two energy peaks and a energy valley between them. The first peak occurs when the shear displacement is about $17\%$ $a_{CSL}$ (case II in the figure), where the atoms represented by open (and filled) circles are directly above the filled (and open) circles across the boundary. This configuration corresponds to a set of atoms in adjacent (110) planes displaced by $d_{220}$ amount in the z-direction. When the shear displacement is about $66\%$ $a_{CSL}$ (case IV in the figure), the atoms across the interface plane are at positions directly facing each other, and furthermore these atoms facing each other are in the same (110) plane. It can be seen that open circle is the exactly above open circle (filled circle is exactly above filled circle). In case IV, the separation distances between atoms across the boundary is the smallest, and the corresponding energy value is the largest as seen in the energy plot. Between these two high energy states (cases II and IV), there is an energy valley at the $33\%$ $a_{CSL}$ shear displacement (see case III). The atomic arrangement at this displacement forms a twin structure equivalent to the initial structure. Though the interface of the twin has shifted (from AA to BB) with $d_{111}$ amount in the y-direction, this boundary has an energy equal to the initial twin structure. It is interesting to notice that though we intent to simulate "pure" GBS, a one-layer migration cannot be prevented for a specific displacement as shown in case III. This demonstrates the geometrical necessary of coupling between migration and sliding, and this aspect will be discussed in details in next sections.

# COUPLED SLIDING AND MIGRATION UNDER APPLIED FORCES

To study grain boundary mobility under applied force conditions, a force of specific value (ranging from 0.01 to 0.04 $eV/\mathring{A}$) is applied in the $x$ direction (to the right) on the atoms in upper-half of the bicrystals. Figure 6 shows the simulation result for $\Sigma3(1\overline{1}1)$ boundary under a applied force of 0.02 $eV/\mathring{A}$. It can be seen that applied forces cause relative motion across the boundary between two grains leading to GB sliding. This is evident from the relative position of the atoms numbered R, 1 and 2. Atom R is in the bottom grain, atom 1 is on the GB and atom 2 in the top grain away from the boundary. It should be noted that the periodic boundary condition fills in new atoms from the left as atoms slide to the right of the computational crystal. Apart from sliding, GB also migrates, i.e. the interface that forms the boundary between two grains moves perpendicular (in y-direction) to the original GB plane. Such motion can be observed at 2 ps where the GB interface has moved one atomic layer (dotted line), and by about 3 atomic layers at 5 ps (see Figure 6). Also shown in Figure 6 is the GB energy during the deformation process as a function of time. This figure indicates that the energy continuously varies with a few peaks and valleys, which corresponds to the evolving GB structure during the deformation. For example a peak is observed at 1.5 ps because the atoms in the layer just above the interface are directly face the atoms in the interface. In this case, the interplanar spacing in y-direction ($0.577a$) is substantially less than the equilibrium nearest-neighbor distance in the perfect crystal ($0.707a$ in FCC structure), the atoms facing each other across the grain boundary are too close to each other and hence repel each other. The several energy valleys (at 2, 3.5 and 5 ps) correspond to new twin configurations (with different interface positions).

To get a quantitative understanding of the grain boundary sliding, the average displacement in x-direction of atomic layers (along y axis) compared to initial position (at 0 ps), as a function of simulation time were computed and plotted in Figure 7. As seen from this figure, the displacement field shows a sharp discontinuity across the interface indicating relative motion of atoms across the boundary resulting in GB sliding. The figure also shows that the magnitude of GB sliding increases with time. Thus Figure 7 (showing sliding) and Figure 6 (showing migration and sliding) demonstrate that sliding and migration are coupled in this system.

The magnitude of applied force and also the grain boundary structures themselves have great effect on GBS (and therefore GB migration). Figure 8 shows the displacement field changes under three levels of applied forces for $\Sigma3(1\overline{1}1)$. The sliding displacements were computed from the relative position of two grain across the interface (see Figure 7). The migration displacements were the difference in y-direction between the positions of new interface and the original equilibrium position of the interface. As can be seen from these two figures, as the applied force increases (from 0.01 to 0.04 $eV/\mathring{A}$), both the sliding and migration displacements increase but in different manners. Sliding displacements increase in a linear-like manner as the time increases. Migration displacement increases in steps, each step indicates the interface has migrated one atomic layer along the y-direction. However, the sliding and migration are coupled and proportional, anything which inhibits sliding also inhibits migration.

In order to understand the effect of grain boundary structure (energy) on grain boundary mobility, we examined many other STGB structures under applied force conditions. Similar cou-pled sliding and migration process was observed in all the STGB structures studied though the GB mobility is different for differnt structures. Figure 9 shows the GBS displacement for four grain boundaries under same total applied force per unit volume. It is clearly shown that GBS displace-ment is proportional to the grain boundary energy of the given structure. For example, at 5 ps, $\Sigma3(1\overline{1}1)$ boundary slides 3.3, 5.5 and 7.2 angstroms at applied forces 0.58, 1.17 and 2.32 (in unit of $\times10^{-3}eV/\mathring{A}^4$ per volume) respectively, while $\Sigma9(2\overline{2}1)$ slides 5.9, 7.4 and 8.5 angstroms under the same levels of applied forces. It is believed that higher energy boundary such as $\Sigma9(2\overline{2}1)$ has lower energy barriers for grain boundary movements and hence produces more sliding and migration displacements.

# COMPARISON BETWEEN APPLIED DISPLACEMENT AND APPLIED STRESS CONDITIONS

From the foregoing discussions, it is clear that in STGB, when forces are applied GB sliding is always accompanied by grain boundary migration and they are proportional to each other. Such coupled process has been observed by Ashby [25] based on the bubble raft model and by Bishop et al. [19,20] based on purely geometric considerations for STGB. This coupling process is of practical importance, and hence examined from geometry and energy considerations in the followings.

For understanding the geometrical aspects of coupling migration with sliding, it is easier to analyze the motion in terms of displacement shift completed (DSC) lattice vectors. Translations of one crystal with respect to another by a DSC lattice vector (the finer mesh in Figure 5) restore the coincidence pattern, although the coincidence sites will shift to a different location. This GB shift corresponds to the GB migration. For example, $\Sigma3(1\overline{1}1)$ boundary has following DSC lattice parameters: $a_{DSC}=1/3a_{CSL}=d_{112}$, $b_{DSC}=1/3b_{CSL}=d_{111}$ and $c_{DSC}=c_{DSC}=d_{110}$. When the relative translation of the crystals is $a_{DSC}$ in the x direction, the boundary migrates by $b_{DSC}$ in the y direction. The CSL structure is reestablished one unit away in the y direction. The ratio (R) of migration distance (M) to sliding displacement (U) is

$$
R = \frac{M}{U} = \frac{b_{DSC}}{a_{DSC}} = \epsilon \tan \frac{\theta}{2} \tag{1}
$$

Here the misorientation angle $\theta$ is defined as the angle between the two [001] directions of each of the bicrystals (see Figure 5), $\epsilon$ is a integer whose value depends on the details of geometry. Equation (1) is valid for all symmetric tilt boundaries as pointed out by Ashby [25]. It should be noted that this geometric argument is truly valid only for STGB [20]. It does not preclude coupling to occur in other types of boundaries. In the applied displacement case, after a displacement of $a_{DSC}$ to the top grain, GB moves by $b_{DSC}$ (see III in Figure 5). However, when the displacement is further applied (including layer BB), GB interface moves back to the original position (line AA). However when forces are applied (Figure 6), GB migrates upwards continuously after each $a_{DSC}$. This difference will be clear from energy consideration discussed below.

The energy necessary to couple sliding and migration can be readily seen by comparing the grain boundary energy profiles shown in Figures 5 and 6 for $\Sigma3(1\overline{1}1)$ boundary. The initial energy profiles in both cases (0-40%$a_{CSL}$ displacement in Figure 5 and 0-2ps in Figure 6) are similar. This indicates that the deformation processes are same at this stage regardless of whether force or displacement is applied. Also, when the structures are examined it is seen that the grain boundary shown in Figure 6 only experienced GBS without migration which is in the same situation shown in Figure 5, and therefore these two energy profiles are very similar. However, the energy profiles are very different in the subsequent stages. The results shown in Figure 6 (applied force) confirm that when sliding is accompanied by migration, boundary structure never passes through a highly perturbed configuration (e.g. Case IV in Figure 5). By virtue of the coupling between sliding and migration, the energy barrier for grain boundary motion is greatly reduced from about $2.5×10^{-2}eV/\mathring{A}^2$ in Figure 5 to $0.5×10^{-2}eV/\mathring{A}^2$ in Figure 6. This results indicate that the high energy state during the pure GBS (e.g. Figure 5 IV) is never reached in the coupled GBS and migration process. Simulation of a perfect crystal with the same orientation as shown in in Figure 5 indicated that an peak energy of $9.3×10^{-2}eV/\mathring{A}^2$ is required to displace one portion of the crystal against the other. This indicates that the high energy peak in Figure 5 (applied displacement) corresponds to sliding in a less defect region (line AA) rather than along the new GB interface (line BB).

# SUMMARY

Interatomic potentials using Embedded Atom Method (EAM) are used in conjunction with molecular statics and dynamics calculations to study the sliding and migration of (110) STGB in aluminum, under both applied displacement and force conditions. *"Pure"* GBS without migration is implemented by applying external displacement. The propensity for *"pure"* GBS is evaluated by computing the energy associated with incremental equilibrium configurations during the sliding

process, and the magnitude of the energy barriers is found to be much higher than that with migration. In contrast, in the applied stress conditions, the energy barriers are reduced due to the fact that grain boundary sliding of STGB is always coupled with apparent migration. The amount of sliding and migration is proportional to the applied force levels, grain boundary energy and time.

## REFERENCES
1. J. Pilling and N. Ridley, Superplasticity in Crystalline Solids, The Institute of Metals, UK, 1989.
2. N. Chandra and D. Kannan, Journal of Materials Engineering and Performance, 1 (1992), 810.
3. N. Chandra and S.C. Rama, ASME Journal for Engineering and Industry, **114**, 4, 452-459, (1992).
4. K. Murali and N. Chandra, Acta Metall., **43, 5**, 1783-1795, (1995)
5. N. Chandra and P. Dang, Scripta Mater., **36**, 1327-1332, (1997)
6. N. Chandra, J. Rama and P. Dang, Mater. Sci. Eng., **A 231**, 134-142, (1997)
7. P. Dang and N. Chandra, Acta Metall., **46, 8**, 2851-2857, (1998)
8. T. R. McNelly and M.E. McMahon, Mater. Trans. A, 27 (1996) 2252.
9. D. Wolf, Acta Metall., 32 (1984) 245.
10. Y. OH and V. Vitek, Acta Metall., 34 (1986) 1491.
11. D. Wolf, Acta Metall., 32 (1984) 245.
12. G. J. Wang, A. P. Sutton and V. Vitek, Acta metall., 32 (1994) 1093.
13. D. Wolf, J. Appl. Phys., 68 (1990) 3221.
14. D. Wolf, J. Appl. Phys., 69 (1990) 185.
15. M. J. Mills, Mater. Sci. Eng., A166 (1993) 35.
16. A. P. Sutton and R. W. Balluffi, Interface in Crystalline Materials, Oxford University Press, 1995.
17. J. M. Rickman, S. R. Fillet, D. Wolf, D. L. Woodraska and S. Yip, J. Mater. Res., 6 (1991) 2291.
18. G. H. Bishop, Jr, R. J. Harrison, T. Kwok and S. Yip, J. Appl. Phys., 53 (1982) 5609.
19. G. H. Bishop, Jr, R. J. Harrison, T. Kwok and S. Yip, J. Appl. Phys., 53 (1982) 5596.
20. C. Molteni, G. P. Francis, M. C. Payne and V. Heine, Mater. Sci. Eng., B37 (1996) 121.
21. G. Palumbo, E. M. Lehockey and P. Lin, JOM, 50 (1998) 40.
22. S. F. Foiles, private communication, 1996.
23. D. J. Oh and R. A. Johnson, Atomistic Simulations of Material: Beyond Pair Potentials, Edited by V. Vitek and D. J. Srolovitz, Plenum Press, 223, 1989.
24. M. F. Ashby, Surf. Sci., 31 (1972) 498.

![](./images/811868460152782849_1.jpg)

Fig.1 Modeling of high-temperature defomation process at three length scales

![](./images/811868460152782849_2.jpg)

Figure 2: SPF forming condition (pressure-time) and resulting cone (macro)

![](./images/811868460152782849_3.jpg)

Fig.3 Micromechanics prediction of the temperature effect on flow stress-strain rate behavior in Al7475 (Meso) [6]

![](./images/811868460152782849_4.jpg)

Fig.4 Independent prediction of the grain size effect on flow stress-strain rate behavior in Al7475 (Meso) [6]

![](./images/811868460152782849_5.jpg)

Figure 5: Energy evolutions during "pure GBS" process of Σ3[1$\overline{1}$1] tilt CSL boundary

![](./images/811868460152782849_6.jpg)

Figure 6: Σ 3[1$\overline{1}\overline{1}$] Grain boundary structure and energy evolution under applied shear stress

![](./images/811868460152782849_7.jpg)

Figure 7: Relative displacement in x-direction as a function of time

![](./images/811868460152782849_8.jpg)

Figure 8: The displacement fields in $\Sigma3$ (1$\overline{1}$1) grain boundary

![](./images/811868460152782849_9.jpg)

Figure 9: Grain Boundary energy effect on GBS (F/V is the total force per unit volume)

<br>

Towards Innovation in Superplasticity II
10.4028/www.scientific.net/MSF.304-306

Mechanics of Superplastic Deformations at Atomic Scale
10.4028/www.scientific.net/MSF.304-306.411