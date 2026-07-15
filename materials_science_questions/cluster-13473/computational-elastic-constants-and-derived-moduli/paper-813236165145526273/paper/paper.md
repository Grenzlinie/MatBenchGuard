# Mechanical properties of amorphous cellulose using molecular dynamics simulations with a reactive force field

Xiumei Zhang

College of Electromechanical Engineering,
Northeast Forest University,
Harbin 150040, China
E-mail: xiumeizhang1@gmail.com

Mark A. Tschopp and Mark F. Horstemeyer

Center for Advanced Vehicular Systems,
Mississippi State University,
Starkville, MS 39762, USA
E-mail: mtschopp@cavs.msstate.edu
E-mail: mfhorst@cavs.msstate.edu

Sheldon Q. Shi*

Mechanical and Energy Engineering,
University of North Texas,
Denton, TX 76207, USA
E-mail: Sheldon.Shi@unt.edu
*Corresponding author

Jun Cao

College of Electromechanical Engineering,
Northeast Forest University,
Harbin 150040, China
E-mail: zdhcj@126.com

**Abstract:** The research objective is to gain a better fundamental understanding of the mechanical behaviour of cellulose structure in wood microfibre for enhancing the mechanical properties of cellulosic-based composites. Molecular static and molecular dynamics simulations were used to both generate and deform the amorphous cellulose structure in a three-dimensional periodic simulation cell. The 14-β-D-glucose structure was chosen along with a reactive force field, ReaxFF, to model the atomic interactions and complex bonding of cellulose. Mechanical properties were calculated for these models and predicted geometric, energetic and elastic material properties were compared to published modelling results and experimental measurements. The significance of the research is that this sets the stage for future polymer-cellulose predictive micromechanical models. These predictive models can be used to elucidate the interfacial compatibility between the cellulose and polymer and how deposited nanoparticles and nanophases on cellulose surfaces affect this interfacial strength.

**Keywords:** amorphous cellulose; molecular dynamics; deformation; strain-stress behaviour.

Reference to this paper should be made as follows: Zhang, X., Tschopp, M.A., Horstemeyer, M.F., Shi, S.Q. and Cao, J. (2013) 'Mechanical properties of amorphous cellulose using molecular dynamics simulations with a reactive force field', *Int. J. Modelling, Identification and Control*, Vol. 18, No. 3, pp.211–217.

**Biographical notes:** Xiumei Zhang received her Bachelor's and Master's degree from Northeast Forestry University in 2005 and 2007, respectively. She studied at Mississippi State University as a doctoral student from September 2010 to December 2012. She is currently a PhD student at the College of Electromechanical Engineering, Northeast Forestry University of China. Her current research domain is the wood nanofibre modelling and simulation based on molecular dynamics methods.

Mark A. Tschopp is an Assistant Research Professor in the Computational Manufacturing and Design group within the Center for Advanced Vehicular Systems at Mississippi State University. Prior to coming to MSU, he received his BS (1998) and MS (1999) in Metallurgical Engineering from the University of Missouri-Rolla. He returned to academia in 2003 to obtain his Doctorate in Materials Science and Engineering from Georgia Institute of Technology. His research interests lie in theoretical, experimental, and/or computational physics/mechanics of materials over multiple length and time scales (atomistic to macroscale behaviour).

Mark F. Horstemeyer is a Professor in the Mechanical Engineering Department at Mississippi State University (MSU), where he holds a Chair position for the Center for Advanced Vehicular Systems in Computational Solid Mechanics.

Sheldon Q. Shi received his PhD in Wood Science from Michigan Technological University, USA, in 1997. Currently, he is a Professor working in Mechanical and Energy Engineering, University of North Texas. His main area of research includes wood and natural fibre composites, manufacturing and processing, bio-engineering, cellulose nanocomposites and mechanical manufacturing engineering.

Jun Cao is a Professor in the College of Electromechanical Engineering at Northeast Forestry University, where he holds the Vice President position for the university.

## 1 Introduction
Research on nanocellulose is currently a hot area. In particular, much interest revolves around incorporating nanophases into polymer composites, which can significantly improve the mechanical behaviour of the composite material. However, there is a lack of information available in the literature that pertains to how nanophases deposited on the cellulose fibre surface improve the interfacial compatibility between the fibre and polymer. Molecular dynamics simulations may shed light on this area and help to provide a fundamental understanding of the efficiency and roles of nanoparticles in the cellulosic fibres on the property enhancement of composites.

Cellulose, the most abundant renewable organic substance in the world, is one of the most popular and the most used polysaccharides by industry in either its native or regenerated forms as a reinforcement material (Kamide, 2005; O'Sullivan, 1997; Yaqiu et al., 2011a, 2011b). The mechanical properties of cellulose strongly depend on the ratio between crystalline and amorphous phases. Several different crystalline forms have been identified since its discovery 160 years ago (de Souza Lima and Borsali, 2004), however, the structure and the morphology of the amorphous phase still has been the subject of a large amount of research. In particular, the mechanical behaviour of amorphous cellulose at the atomic level is a complex undertaking due to the complex structure and the various types of bonding.

Experimental techniques are often limited by both the time-intensive nature and the capability for preparing specimens, conducting experiments, and analysing the structural evolution during deformation. On the other hand, computer simulation is a powerful tool for investigating atomistic phenomena. Among the various computational methods, molecular dynamics simulations represent a useful technique for determining the nanoscale physical and mechanical material properties through iteratively solving Newton's equations of motion based on empirical or semi-empirical interatomic potentials to describe the forces between atoms (Frenkel et al., 1997; Leach, 2001; Xue et al., 2011). Nanoscale simulations can complement experimental work and in certain cases can provide additional information (e.g., atomic positions, velocities and forces) that are not easily obtained from experiments.

In recent years, numerous molecular dynamics simulations have been used on the mechanical properties of carbon nanotubes, graphite/epoxy nanocomposites and other polymers (Han and Elliott, 2007; Nouranian et al., 2011; Zhu et al., 2007; Lau et al., 2004; Er-Wei et al., 2009). Moreover, atomistic simulations have also been performed to evaluate the behaviour of cellulose. The mechanical properties of cellulose can be characterised by their properties in both the ordered (crystalline) and disordered (amorphous) regions of the molecules. The amorphous cellulose regions contribute to the flexibility and the plasticity of the bulk microfibril, while the crystalline cellulose regions contribute to the elasticity of the materials. The latter component has been studied by evaluating the behaviour of two native crystalline phase celluloses (I$\alpha$ and I$\beta$) properties, including glass transition temperature, thermal response and chain modulus of elasticity (Bergenstråhle et al., 2007; Eichhorn et al., 2004, Eichhorn and Davies, 2006; Tanaka and Iwata, 2004). Molecular modelling is a well-adapted technique to investigate the cellulose chains within the material. Modelling protocols using simple minimisations of finite-sized systems (without periodic boundary conditions), called 'minicrystals', allow predicting the relative stability of the different cellulosic allomorphs (Aabloo and French, 1994; French et al., 1993; Viëtor et al., 2000). However, significant uncontrolled edge effects are expected in such computations. NVT and NPT ensemble molecular dynamic computations have been performed to solve this issue and to reveal structural and energetic data on different crystalline forms (Mazeau and Heux, 2002). Altogether these studies allow us to get an overall realistic picture of the crystal structures. In contrast

to the efforts to characterise crystal structures of cellulose, the amorphous phase comparatively lacks studies that investigate the evolution of structure during deformation.

In this paper, molecular dynamics simulations were used to calculate the relevant strain-stress behaviour of amorphous cellulose during uniaxial tensile deformation. First, a three-dimensional (3D) periodic simulation cell of 14-β-D-glucose chains was generated with the same density as experiments. In contrast to previous molecular simulations in the literatures, a reactive force field (ReaxFF) was used here to describe the atomic interactions, which allows dynamic bond scission and bond formation. Simulation results show how the calculated geometric, energetic and elastic material properties compare with published modelling results and experimental measurements.

## 2 Modelling and simulation approach

### 2.1 Model building

The initial configuration of the system was generated using commercial Materials Studio software from Accelrys and the model cubic simulation cell was built using the Amorphous Cell Protocol, originally proposed by Theodorou and Suter (1985). The construction of amorphous cellulose models involved placing a specified number of 14-β-D-glucose chains into the periodic simulation cell. Figure 1 shows the chemical structure for cellobiose, which can be considered the repeat unit for cellulose. The potential influence of the simulation cell size was examined by testing two chain lengths: 20 and 50 repeat units per chain. Figure 2 shows the unit cell of 50 monomers in one chain with periodic boundary condition. The initial density of the system was $0.8\ \text{g/cm}^3$. However, as the simulation cell relaxed at 298 K to a zero pressure condition, the density varied between $1.28\ \text{g/cm}^3$ to $1.44\ \text{g/cm}^3$. Periodic boundary conditions were applied in all three directions.

All subsequent molecular dynamics simulations were performed using the LAMMPS simulation tool (Plimpton, 1995). The unit cell models were replicated by $3\times3\times3$ to simulate more atoms as shown in Figure 3. Standard energy minimisation procedures were applied to the constructed cell in order to minimise the energy of each system and relax the structure efficiently. Furthermore, the system was equilibrated at the chosen temperature using isothermal/isobaric (NPT) ensemble with a small time step ($\Delta t=0.5$ fs) for 250 ps equilibration time. The equilibrium density of the amorphous cell was subsequently achieved using the NPT ensemble at the chosen temperature and at a fixed atmospheric pressure ($P=0.0001$ GPa). The equilibrated systems were then used to perform the deformation simulations under a uniaxial tensile strain applied at a constant strain rate. The ReaxFF used here is able to describe the atomic interactions for dynamic bond scission and bond formation (van Duin et al., 2001; Chenoweth et al., 2008). Three different strain rates ($108\ \text{s}^{-1}$, $109\ \text{s}^{-1}$, and $1,010\ \text{s}^{-1}$) were applied to the simulation cell for different numbers of chains and chain lengths. The amorphous cellulose configurations were deformed at 298 K, well below the glass transition temperature. The pressure and temperature used in our simulation are convenient computational parameters to relax the amorphous cellulose structure and are not intended to reproduce the actual thermodynamic state ($P$, $V$, $T$) of the real structure.

**Figure 1** Chemical structure, atom names and torsion angles of cellobiose (see online version for colours)

![](./images/813236165145526273_1.jpg)

**Figure 2** Simulation cell modelled amorphous cellulose structures (see online version for colours)

![](./images/813236165145526273_2.jpg)

**Figure 3** Supercell of the unit cell model with three ranges (see online version for colours)

![](./images/813236165145526273_3.jpg)

All calculations were performed at the Center for Advanced Vehicular Systems (CAVS) of Mississippi State University.

### 2.2 ReaxFF method

In this work, we used the ReaxFF to simulate the bonding between the various elements of glucose. ReaxFF is a general bond-order-dependent force field that provides accurate descriptions of bond breaking and bond formation during dynamic simulations. The main difference between the traditional unreactive force fields and ReaxFF is that the connectivity in ReaxFF is determined by bond orders calculated from interatomic distances that are updated every MD step. This allows for bonds to break and form during the simulation. Similar to the empirical non-ReaxFFs, the ReaxFF divides the system energy $E_{system}$ into contributions from various partial energy terms, as demonstrated can be expressed as follows:

$$
\begin{aligned}
E_{system} &= E_{bond} + E_{under} + E_{over} + E_{val} + E_{pen} \\
&\quad + E_{tors} + E_{conj} + E_{vdwaals} + E_{coulomb}
\end{aligned} \tag{1}
$$

These partial energies include bond energy $E_{bond}$, atom under-/overcoordination $E_{under}$, $E_{over}$, valence angle $E_{val}$, penalty energy $E_{pen}$, torsion angle $E_{tors}$ and conjugation energy $E_{conj}$ terms to properly handle the nature of preferred configurations of atomic and resulting molecular orbitals and terms to handle van der Waals $E_{vdwaals}$ and Coulomb $E_{coulomb}$ interactions. These latter non-bonded interactions are calculated between every atom pair, irrespective of connectivity, and are shielded to avoid excessive repulsion at short distances. This treatment of non-bonded interactions allows ReaxFF to describe covalent, ionic, and intermediate materials, thus, greatly enhancing its transferability. The potential energy functions associated with each of these partial energy contributions are further described in the research of van Duin et al. (2001).

## 3 Results and discussions

### 3.1 Simulation conditions

With ReaxFF, a suitable time step is required because the charges and bond orders are allowed to change at every time step. The ultimate aim is to simulate the longest possible time with the smallest amount of computational effort. The choice of time step is therefore a compromise between a large value which will require less molecular dynamics MD steps for a given simulated time, and a small value which allow each time step to be calculated faster. The time step must be sufficiently small that dynamics correctly conserve the total energy of the system.

Figure 4 shows a greater temperature fluctuation from the initial value in the 1 fs time step case while the temperature is computed more stable using 0.5 fs time step. Noticed the large bump in temperature for the 1 fs timestep case as the simulation cell is equilibrated. Figure 5 shows the energy (total, kinetic, and potential) as a function of simulation time for the same configurations. The system with a time step of 0.5 fs performs faster to obtain equilibrium without noticeable drift. Splitting the total energy into its potential and kinetic energy shows that all of these values begin to oscillate if the initial velocities are assigned during the NVE molecular dynamics simulation with 1 fs time step. Another sign of instability with the 1 fs is the ejection of atoms from the simulation cell, which can occur if atoms get too close. Therefore, future simulations need to use a time step of lower than 0.5 fs.

**Figure 4** Evolution of temperature as a function of simulation time for 0.5 fs (a) and 1 fs (b) using a constant volume and energy (NVE) molecular dynamics simulation (see online version for colours)

![](./images/813236165145526273_4.jpg)

### 3.2 Physical and mechanical properties

To reflect the mechanical properties of real amorphous cellulose, the final model physical and mechanical properties such as density, Young's modulus, shear modulus and Poisson's ratio were chosen to evaluate the model parameters criteria. Because the cell parameters are allowed to vary during molecular dynamics simulations, the density can therefore vary. Density is a relevant parameter to evaluate the realism of the simulated microstructures. The calculated properties are given in Table 1. Compared with experimental and literature values (Chen et al., 2004), the

equilibrium amorphous cellulose model with ReaxFF had very similar properties as those in the literatures. The general agreement between the calculated MD results and the experimentally-measured properties is acceptable validation for further studies. Especially when considering that the molecular dynamics results herein utilise a semi-empirical potential with an idealised amorphous structure; experimental structures may have heterogeneities – a distribution of chain lengths, regions of crystallised and amorphous structure, and impurities/moisture – that can result in different properties than the idealised structure modelled here.

Figure 5 Evolution of the energy (Et Ep and Ek) as a function of simulation time for 0.5 fs (a) and 1 fs (b) using a constant volume and energy (NVE) molecular dynamics simulation (see online version for colours)

![](./images/813236165145526273_5.jpg)

Table 1 Mechanical properties of amorphous cellulose models at 298 K (28,404 atoms)

<table>
  <thead>
    <tr>
      <th>Properties</th>
      <th>ReaxFF</th>
      <th>Literature value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Density (g/cm³)</td>
      <td>1.347</td>
      <td>1.385</td>
    </tr>
    <tr>
      <td>Young’s modulus (GPa)</td>
      <td>9.37</td>
      <td>10.42 ± 1.08</td>
    </tr>
    <tr>
      <td>Shear modulus (GPa)</td>
      <td>3.94</td>
      <td>5.955 ± 0.673</td>
    </tr>
    <tr>
      <td>Poisson’s ratio</td>
      <td>0.189</td>
      <td>0.232 ± 0.0313</td>
    </tr>
  </tbody>
</table>

Figure 6 The histogram of potential energy of three atoms in initial deformation structure (28,404 atoms, C for 8,100, H for 13,554 and O for 6,750) (see online version for colours)

![](./images/813236165145526273_6.jpg)

Figure 7 The histogram of potential energy of three atoms after deformation (28,404 atoms, C for 8,100, H for 13,554 and O for 6,750) (see online version for colours)

![](./images/813236165145526273_7.jpg)

### 3.3 Potential energy

The goal of structure equilibration is to correspond to an energy minimum of the potential energy. The structure should be free of internal tension or compression. After equilibrating the amorphous cellulose structure, the potential energy of each atom was calculated and their evolutions were tracked to ensure that the structure was appropriate for deformation simulations. Figure 6 shows an example of the potential energy distributions of 28,404 atoms (8,100 carbon atoms, 13,554 hydrogen atoms and 6,750 oxygen atoms) in initial deformation structure. After tensile loading at a strain rate of 1,010 s⁻¹, the potential energy was changed as shown in Figure 7. The

potential energy of carbon atoms is more stable than the others. It is important to note that the potential energy of hydrogen atom was associated with modelling the H-bonding, which is a critical structural component. Splitting the total potential energy into its non-bonded (van der Waals and Coulomb) and bonded components shows that the most significant component is coulomb term which is large and negative. The improper van der Waals interaction is positive and very weak, which appears to have little effect in amorphous cellulose.

### 3.4 Strain-stress behaviour

The strain-stress behaviour of the amorphous cellulose was calculated by tensile loading in the x-direction while maintaining zero pressure on the directions orthogonal to the loading direction (i.e., uniaxial tension). Figure 8 shows the amorphous cellulose structure and unit cell parameters after equilibration (up) and after 100% true strain (down).

Figure 9 shows the stress-strain behaviour for a 28,404 atom amorphous cellulose simulation cell at a strain rate of $1,010\ \mathrm{s}^{-1}$. All stress values are plotted (loading direction is red, lateral directions are blue and green) as a function of strain and the black line is the averaged response; this scatter can be typical of polymer deformation in molecular dynamics. The strain-stress curve has three distinct regimes: elastic, yield and hardening. After an initial elastic regime, yield occurs and then strain hardening is observed. The stresses in the directions lateral to the loading direction are centred about 0 GPa as prescribed for the uniaxial tension boundary conditions. This stress-strain curve is similar to previous simulations in the literature as well as experimental results. Future work will explore the nanoscale mechanisms behind these different regimes.

Figure 8 The model system in equilibrium at 100 K and after being uniaxially deformed (see online version for colours)

![](./images/813236165145526273_8.jpg)

Note: Colours represent different atom types (C, H, and O).

Figure 9 A characteristic stress-strain curve for amorphous cellulose (28,404 atoms, 100 K temperature, $1,010\ \mathrm{s}^{-1}$ strain rate) (see online version for colours)

![](./images/813236165145526273_9.jpg)

Notes: Black line is the average stress response in the tensile direction. Red, green, and blue dots show the scatter of the instantaneous stresses the loading direction and two lateral directions, respectively

## 4 Conclusions and future work

Molecular dynamics simulations were used to study the strain-stress behaviour during uniaxial tensile loading of amorphous cellulose. The amorphous cellulose models were successfully generated with the use of ReaxFF. Preliminary molecular dynamic simulations have been presented for amorphous cellulose. We found that a suitable timestep of 0.5 fs should be used in future simulations with ReaxFF.

Molecular dynamics simulations were used to study the strain-stress behaviour during uniaxial tensile loading of amorphous cellulose. The amorphous cellulose models were successfully generated with the use of ReaxFF. Preliminary molecular dynamic simulations have been presented for amorphous cellulose. We found that a suitable timestep of 0.5 fs should be used in future simulations with ReaxFF. The calculated energies and mechanical properties of cellulose were comparable to those reported for previous molecular dynamics simulations and experimental studies. The simulated stress-strain behaviour using molecular dynamics showed similar trends both qualitatively and quantitatively as those observed in the experimental testing for amorphous cellulose. A linear relationship between stress and strain was observed at low strain, which corresponds to elastic deformation. At higher strains, the amorphous cellulose yielded and exhibited strain hardening. These predictive models can be used to elucidate the interfacial compatibility between the cellulose and polymer and how deposited nanoparticles and nanophases on cellulose surfaces affect this interfacial strength.

### Acknowledgements

This work was supported by National Science Foundation (NSF), Grant Number CMMI 0928641, National Natural Science Foundation of China (NSFC) 30972301/C040301, the Center for Advanced Vehicular Systems/CAVS of Mississippi State University, the Foundation of Excellent Doctoral Dissertation of NEFU (Grap09). Additionally, the authors would like to acknowledge the insightful comments from the reviewers.

### References

Aabloo, A. and French, A.D. (1994) ‘Preliminary potential energy calculations of cellulose iα crystal structure’, *Cellulose*, Vol. 3, No. 1, pp.185–191.

Bergensträhle, M., Berglund, L.A. and Mazeau, K. (2007) ‘Thermal response in crystalline Iβ cellulose: a molecular dynamics study’, *The Journal of Physical Chemistry B*, Vol. 111, No. 30, pp.9138–9145.

Chen, W., Lickfield, G.C. and Yang, C.Q. (2004) ‘Molecular modeling of cellulose in amorphous state. Part I: model building and plastic deformation study’, *Polymer*, Vol. 45, No. 3, pp.1063–1071.

Chenoweth, K., van Duin, A. and Goddard, W.A. (2008) ‘ReaxFF reactive force field for molecular dynamics simulations of hydrocarbon oxidation’, *The Journal of Physical Chemistry A*, Vol. 112, No. 5, pp.1040–1053.

de Souza Lima, M. and Borsali, R. (2004) ‘Rodlike cellulose microcrystals: structure, properties, and applications’, *Macromolecular Rapid Communications*, Vol. 25, No. 7, pp.771–787.

Eichhorn, S.J. and Davies, G.R. (2006) ‘Modelling the crystalline deformation of native and regenerated cellulose’, *Cellulose*, Vol. 13, No. 3, pp.291–307.

Eichhorn, S.J., Young, R.J. and Davies, G.R. (2004) ‘Modeling crystal and molecular deformation in regenerated cellulose fiber’, *Biomacromolecules*, Vol. 6, No. 1, pp.507–513.

Er-Wei, B., Sunaina, F. and Alan, M. (2009) ‘Modelling and parameter estimation of a cell system’, *International Journal of Modelling, Identification and Control*, Vol. 6, No. 1, pp.72–80.

French, A.D., Miller, D.P. and Aabloo, A. (1993) ‘Miniature crystal models of cellulose polymorphs and other carbohydrates’, *International Journal of Biological Macromolecules*, Vol. 15, No. 1, pp.30–36.

Frenkel, D., Smit, B. and Ratner, M. (1997) ‘Understanding molecular simulation: from algorithms to applications’, *Physics Today*, Vol. 50, No. 7, p.66.

Han, Y. and Elliott, J. (2007) ‘Molecular dynamics simulations of the elastic properties of polymer/carbon nanotube composites’, *Computational Materials Science*, Vol. 39, No. 2, pp.315–323.

Kamide, K. (2005) *Cellulose and Cellulose Derivatives: Molecular Characterization and its Applications*, Elsevier, Amsterdam, The Netherlands.

Lau, K., Chipara, M., Ling, H.Y. and Hui, D. (2004) ‘On the effective elastic moduli of carbon nanotubes for nanocomposite structures’, *Composites Part B: Engineering*, Vol. 35, No. 2, pp.95–101.

Leach, A. (2001) *Molecular Modeling: Principles and Applications*, Pearson Education EMA, UK.

Mazeau, K. and Heux, L. (2002) ‘Molecular dynamics simulations of bulk native crystalline and amorphous structures of cellulose’, *Journal of Physical Chemistry B*, Vol. 107, No. 10, pp.2394–2403.

Nouranian, S., Jang, C., Lacy, T., Gwaltney, S., Toghiani, H. and Pittman, C. (2011) ‘Molecular dynamics simulations of vinyl ester resin monomer interactions with a pristine vapor-grown carbon nanofiber and their implications for composite interphase formation’, *Carbon*, Vol. 49, No. 10, pp.3219–3232.

O'Sullivan, A. (1997) ‘Cellulose: the structure slowly unravels’, *Cellulose*, Vol. 4, No. 3, pp.173–207.

Plimpton, S. (1995) ‘Fast parallel algorithms for short-range molecular dynamics’, *Journal of Computer Physics*, Vol. 117, No. 1, pp.1–19.

Tanaka, F. and Iwata, T. (2004) ‘Estimation of the elastic modulus of cellulose crystal by molecular mechanics simulation’, *Cellulose*, Vol. 13, No. 5, pp.509–517.

Theodorou, D.N and Suter, U.W. (1985) ‘Detailed molecular structure of a vinyl polymer glass’, *Macromolecules*, Vol. 18, No. 7, pp.1467–1478.

van Duin, A., Dasgupta, S., Lorant, F. and Goddard, W.A. (2001) ‘ReaxFF: a reactive force field for hydrocarbons’, *The Journal of Physical Chemistry A*, Vol. 105, No. 41, pp.9396–9409.

Viëtor, R.J., Mazeau, K., Lakin, M. and Perez, S. (2000) ‘A priori crystal structure prediction of native celluloses’, *Biopolymers*, Vol. 54, No. 5, pp.342–354.

Xue, Z.W, Cai, Y.M. and Jian, W. (2011) ‘Pharmaceutical crystal shape control based on online image processing and multi-scale modelling’, *International Journal of Modelling, Identification and Control*, Vol. 12, Nos. 1–2, pp.96–100.

Yaqiu, L., Liang, C. and Liangkuan, Z. (2011a) ‘Modelling of airflow circulation systems in wood drying processes’, *International Journal of Modelling, Identification and Control*, Vol. 12, No. 4, pp.378–385.

Yaqiu, L., Liang, C., Liangkuan, Z. and Weipeng, J. (2011b) ‘Researching of airflow circulation system in wood drying kiln based on array fans’, *International Journal of Modelling, Identification and Control*, Vol. 13, Nos. 1–2, pp.126–133.

Zhu, R., Pan, E. and Roy, K. (2007) ‘Molecular dynamics study of the stress-strain behavior of carbon-nanotube reinforced Epon 862 composites’, *Materials Science and Engineering: A*, Vol. 447, Nos. 1–2, pp.51–57.