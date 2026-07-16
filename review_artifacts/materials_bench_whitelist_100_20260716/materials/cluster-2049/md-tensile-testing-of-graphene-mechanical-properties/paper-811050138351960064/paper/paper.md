Accepted Manuscript

Interfacial strengthening between graphene and polymer through Stone-Thrower-
Wales defects: *Ab initio* and molecular dynamics simulations

Janghyuk Moon, Seunghwa Yang, Maenghyo Cho

![](./images/811050138351960064_1.jpg)

PII:
S0008-6223(17)30262-2

DOI:
10.1016/j.carbon.2017.03.021

Reference:
CARBON 11828

To appear in:
*Carbon*

Received Date: 20 December 2016

Revised Date: 7 March 2017

Accepted Date: 8 March 2017

Please cite this article as: J. Moon, S. Yang, M. Cho, Interfacial strengthening between graphene and polymer through Stone-Thrower-Wales defects: *Ab initio* and molecular dynamics simulations, *Carbon* (2017), doi: 10.1016/j.carbon.2017.03.021.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

![](./images/811050138351960064_2.jpg)

![](./images/811050138351960064_3.jpg)

# Interfacial strengthening between graphene and polymer through Stone-Thrower-Wales defects: *Ab initio* and molecular dynamics simulations

Janghyuk Moon¹, Seunghwa Yang²⁎, and Maenghyo Cho³,†

¹*Department of Mechanical Design Engineering,*
Kumoh National Institute of Technology, 61 Daehak-ro, Gumi, Gyeongbuk, 39177, South Korea

²*School of Energy Systems Engineering,*
Chung-Ang University, Heukseok-Ro, Dongjak-Gu, 06974, South Korea

³*School of Mechanical and Aerospace Engineering,*
Seoul National University, 1 Gwanak-Ro, Gwanak-Gu, Seoul 08826, South Korea

## Abstract
In this study, we revealed the interfacial strengthening mechanism between a Stone- Thrower-Wales (STW) defective single layer graphene and polypropylene (PP), through a density functional theory (DFT) simulation and atomistic molecular dynamics simulations. In quantum mechanical simulation, the adhesion energy of propylene monomer on STW defective graphene is calculated with van der Waals interaction. An improved adsorption characteristic of propylene to the STW defective graphene is clearly observed, compared with a pristine counterpart. For deeper understanding of the adsorption, the electronic structure calculation and geometrical analysis of the adsorbed structures are also performed. In molecular dynamics simulation, three transversely isotropic nanocomposite unit cell

---
⁎Corresponding author. Tel: +82-2-820-5266
E-mail address: fafala@cau.ac.kr (S.Yang)
†Corresponding author. Tel/Fax: +82-2-880-1693/+82-2-886-1645.
E-mail address: mhcho@snu.ac.kr (M.Cho)

structures consisting of PP and single layer graphene having a different number of STW defects are constructed. The stress-strain curves of nanocomposites according to the density of STW defects are obtained from uniaxial tension and shear tests. Since the properties of graphene itself are degraded by the STW defects, the overall stress-strain characteristics of nanocomposites involving the deformation of graphene are degraded by the addressed STW defects. However, in longitudinal shearing, where interfacial shearing between graphene and PP is involved, the STW defect can critically improve the shear load bearing capability. The increased interfacial shear load transfer is mostly attributed to the rippling of graphene at the STW defective sites, and the resultant surface roughness of graphene.

Keywords: Nanocomposites, graphene, STW defects, Density functional theory, Molecular dynamics simulation.

## 1. Introduction

Together with carbon nanotube [1] and fullerene [2], graphene has become one of the most important nanostructured materials to be categorized as nanocarbon structure [3-4]. The fascinating physical properties of graphene, such as ultra-high elastic stiffness (~1TPa, [5]) and strength (~120GPa, [5]), as well as its thermal and electronic properties [6-7], have resulted in proposals for a variety of applications, including soft electronics [8], electrochemical sensors [9], hydrogen storage carrier [10], and structural multifunctional composites [11]. In most of the applications of graphene for which good electron transport capability is required, the achievement of high quality defect-free graphene is still the most challengeable task in bottom-up manufacture of graphene, such as the chemical vapor deposition (CVD) process [12]. On the other hand, in solution-based approaches, representatively Hummer's method [13-14], cost effectiveness, as well as high throughput of exfoliated graphene solution that is readily available from market or laboratory, are major concerns, rather than extremely high purity. Nonetheless, the reduction and desirable purification of graphene is also an important issue in solution-based approaches for graphene. Therefore, the growth method or solution-based methods are selected according to the applications, and the requirement of the impurity of graphene.

In general, several intrinsic defects remain after the manufacturing process of graphene, such as the Stone-Thrower-Wales (STW) defect [15-16], vacancies [17], oxidations [18], doping [19], and grain boundaries [20]. With the help of current quantum chemistry, some designed defects, such as inverse STW (ISTW) defects are demonstrated, and theoretically studied as a new building block of graphene. When such intrinsic defects are initiated, the change in $sp^2$ chemical bond order alters electronic properties of the graphene in detail, and degrades important physical properties. However, the interpretations of graphene or other nanocarbon defects have found negative, as well as positive aspects. Since the electron distribution of defective carbon sites is altered, the chemical reactivity and cohesive strength

of the defective carbon can also be altered. For example, in our previous works on STW defective carbon nanotube (CNT) reinforced nanocomposites [21-22], an improved interfacial bond strength between the defective CNT and surrounding polymer could be demonstrated by a molecular dynamics (MD) simulation. On the application of the graphene to the electrodes for electric double layer capacitors, it has been confirmed that the defects in graphene such as STW defect, vacancies and doping can enhance the quantum capacitance [23-24]. Using the quantum mechanics calculations as well as experimental measurement of carbon nanosheets, a new possibility of the vacancy defect that it can substantially improve the electrical conductivity of graphene [25] has been demonstrated. Since the graphene can easily be self-doped to alter the electronic properties, various attempts to engineer the graphene by incorporating the designed defects to attain new functionalities have been made by theoretical studies [26-27]. Moreover, recent works on the experimental introduction of extended defects of graphene [28], and on the reversible defect engineering of CNT using scanning tunneling microscopy [29], have improved the realization of defect engineering of nanocarbon structures. More information on the role of well-known structural defects in graphene are well summarized in ref. [30].

When graphene is used as a multifunctional reinforcing filler inside a polymer matrix, the defect can also be taken advantage of, because interfacial strengthening between the graphene and matrix is involved. In this study, we only focus on the topological STW defect in tailoring the interface properties. Recalling the rule of mixtures for composites, it is undoubtedly conjectured that the STW defective graphene degrades the overall properties of composites, since the properties of the reinforcement phase are primarily degraded. However, considering the two-dimensional structure of graphene and the interfacial load transfer mechanism of penny-shaped inclusion, an improved interfacial shear load transfer can be accomplished by the enhanced reactivity or cohesive energy between the STW defective

graphene and polymer. Therefore, it is essential for the design of graphene reinforced polymer composites to tackle the two rival effects of the degradation of graphene, and the improvement of interfacial strength. To the authors' best knowledge, however, a systematic research incorporating extreme scale computer simulation on this arguable issue of graphene has never been performed yet.

To reveal the physics behind the positive and negative aspects of the STW defects, and to correlate the defective structure with the macroscopic properties, computational studies capable of describing the charge redistribution of defective carbon, geometrical distortion, and rippling of graphene embedding designed defects are of primary importance. In this respect, both quantum mechanical calculations and molecular dynamics simulations can be effectively used. Using quantum mechanics approaches, the electronic structure of defective graphene is calculated within density functional theory. The physical non-bonding interaction can be described with van der Waals formalism, and the resultant cohesive strength between the defective sites and other species of atoms constituting the polymer matrix is accurately quantified. Moreover, the optimum physisorption sites on the defects on top of the carbon, such as carbon-carbon bridge, penta- or hepta-hole, can be determined in detail [23]. Therefore, material interface level characterization of between the STW defect and polymer chain, and the screening of defect-to-polymer type combination, are readily available using the DFT simulation.

For the representative volume element (RVE) level modeling and prediction of composites properties according to the STW defects, molecular level simulation is rather more useful than the quantum level approach for its ability to consider rather larger molecular systems than quantum simulations, as has been demonstrated in many literatures [21-22, 31-32]. However, in regard to the chemical reactivity of carbons in defects, existing classical potential models, such as the consistent valence force field (CVFF) [33] and polymer

consistent force field (PCFF) [34], do not distinguish the van der Wales potential parameter of carbon atoms in octagonal or pentagonal ring, from that of carbons in hexagonal ring. Therefore, the classical potential models cannot describe the intrinsic adhesion characteristics of the STW defects to the typical engineering polymers. Nonetheless, local geometry changes of defective sites, such as out-of-plane distortion and rippling, which are described by DFT simulation [35], can also be described by MD simulations. In interfacial load transfer between an inclusion and a rigid polymer, the surface roughness of the inclusion plays a very important role. Therefore, the effect of geometrical change by the STW defect on the mechanical properties of graphene reinforced nanocomposites can be readily studied within the classical MD simulations.

In this study, the interfacial strengthening mechanism between STW defective graphene and polypropylene (PP) matrix is examined by DFT simulation and MD simulations, respectively. The DFT simulation focuses on the intrinsic binding energy between the STW defect and PP monomer and dimer. The detailed adhesive energy and distance according to the adsorption site of PP monomer in the STW defect, and the charge difference of the adsorbed molecular structure are analyzed to evaluate the intrinsic adhesive nature of the STW defect with the PP monomer. In MD simulations, transversely isotropic nanocomposites unit cell structure is considered, and the stress-strain curves are obtained from tensile and shear tests according to the number of STW defects. To correlate the change in surface distortion and the resultant shear moduli of nanocomposites, the mean arithmetic surface roughness is analyzed according to the density of the STW defect.

### 2. Density Functional Theory
To investigate the STW defective single layer graphene-PP chain, density functional theory calculations are performed using the Vienna Ab initio Simulation Package (VASP) [36-37].

Both the local density approximation (LDA) and the generalized gradient approximation (GGA) are used for comparison. The local and semi local density functional theory calcualtions are unable to correctly describe the van der Waals interaction resulting from dynamical correlations between fluctuating charge distribution. Therefore, the DFT-D2 method of Grimme is added to the conventional Kohn-Sham DFT energy [38–39]. We use the projector augmented wave (PAW) method with a plane wave basis set [40–41]. The polypropylenes are linear, saturated hydrocarbon chains absent of branches, with the general formula $(C_3H_6)n$, where n is the number of monomers in one chain. In this work, we analyze the adsorption of propylene monomer and several short polymers (0<n<15) on graphene and STW defective graphene. The migration energy barriers of polypropylene monomer are calculated using the climbing-image nudged elastic band (NEB) method on the tangential direction of graphene [42].

### 2.1 Model configuration and structure relaxation
The STW defect on graphene or CNT is formed by a 90 degree rotation of two neighboring carbon atoms in a hexagonal ring. As a result, four hexagonal rings surrounding the rotated carbon-carbon bond are transformed into two pentagons and heptagons (5-7-7-5 defect), as Fig. 1 shows. Even if the STW defect does not collapse $sp^2$ hybridization of graphene, the flat resonant structure of graphene is distorted to sine-like or cosine-like structures, which can result in chemical activities [43], and band-gap opening [44].

Experimental lattice parameters are used to generate graphene supercells (C-C bond length – 1.42 Å, in plane lattice, a = b = 2.46 Å). The DFT calculation was performed using the LDA and GGA with augmented-plane wave method (PAW), with a 7x7x3 Monkhorst-Pack k-point mesh, and a 500 eV plane-wave cutoff. These sets of parameters are then reduced to 3x3x1 for larger 4x4 and 4xN (N = 4 x n, n = 1~5) supercells.

![](./images/811050138351960064_4.jpg)

Fig. 1 Formation of STW defects in graphene by a 90 degree rotation of two neighboring carbon-carbon bonds (left), and locally distorted periodic structure of five STW-defective single layer graphene after the energy minimization process (right).

Propylene monomer and polymer structures are initially optimized using a molecular static scheme with a steepest descent algorithm, and a force convergence criterion of 0.1 kcal/molÅ. Then the free energies of each molecule are minimized again by using DFT with a force convergence criterion of 0.01 eV/Å. Figure S1a shows the atomic configurations of the optimized propylene structures.

To investigate the intrinsic adhesion strength between propylene and graphene, Fig. 2 (a) shows that a propylene monomer is placed above three different sites for adsorption: on top of a carbon atom (Top), at the center of a hexagon (Hole), and in the middle of a carbon-carbon covalent bond (Bridge) of the graphene. Since the STW defect has pentagons and heptagons, we defined nine more sophisticated adsorption sites for the STW defective graphene than the pristine one. Figure 2 (b) shows in detail that Bridge, Top, and Hole sites are again atomized to four (1-4), three (5-7), and two (8-9) different adsorption locations.

![](./images/811050138351960064_5.jpg)
![](./images/811050138351960064_6.jpg)

Fig. 2 Structure of graphene and STW defective graphene prepared for DFT calculation and adsorption sites on graphene. (a) Bridge (blue), Top (orange), Hole (green) on pristine graphene, and (b) Bridge 1-4, Top 5-7, and Hole 8-9.

The supercells of graphene as well as SW defective graphene that are shown in Fig. 2 are made of 32 carbon atoms, and are large enough to prevent spurious self-interaction of the propylene monomer due to cell periodicity. The through-the-thickness direction of the graphene unit cell is assigned adequate space of $20$ $\mathring{A}$ for the cell. Therefore, various distances between the adsorbed propylene and graphene, as well as the orientation of propylene, can be considered. In addition, $20$ $\mathring{A}$ of cell dimension is enough to prevent the effect of nonlocal interactions between adjacent graphene in periodic boundary conditions.

In other to evaluate the stability of the STW defect, the total energies of the pristine and STW defective graphene are calculated. For comparison, we considered additional defects of mono and di vacancies. Comparison of the total energies of pristine, mono vacancy, di vacancies, and STW defective graphene is provided in the supplemental information (Fig. S2). The total energy of the STW defective graphene is -9.99 eV/C atom, which is lower than the -9.89 eV/atom (mono) and -9.91 eV/atom (di-vacancy), and larger than the -10.14 eV/atom of

the pristine. Therefore, STW defect is more stable than the vacancy type of defects, and less stable that the pristine graphene.

### 2.2 Adsorption energy and distance of propylene on graphene

The adsorption energy of propylene on graphene $E_{\text{Ad}}$ is calculated as,

$$
E_{\text{Ad}}=E_{\text{PP+G/TSWG}}-E_{\text{PP}}-E_{\text{G/TSWG}} \tag{1}
$$

where, $E_{\text{PP+G/TSWG}}$ is the total energy of the whole structure, including the graphene and propylene, while $E_{\text{PP}}$ and $E_{\text{G/TSWG}}$, respectively, are the total energy of free-standing propylene and graphene (pristine or STW defective). To establish the adsorption distance to the adsorption energy relationship, the adsorption energy was systematically calculated by varying the distance between the propylene and graphene. The distances between the propylene and graphene sheet are defined as the closest distance between carbon atom in graphene, and hydrogen atom in the methyl group of propylene chains.

## 3. Molecular Dynamics Simulation

A commercial molecular simulation program, Material Studio (MS 5.5) [45] is used for the molecular modeling of STW defective single layer graphene-PP nanocomposites. The amorphous cell® module is used to construct the PP matrix unit cell and PP-graphene composites unit cell having amorphous conformations. Discover module® is used for geometry optimization via the conjugate gradient method, and annealing through the isothermal (NVT) ensemble simulation for preparing energetically minimized unit cell structure. An open source molecular dynamics program, Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) [46] is used for the production runs, including the

equilibration run through the isothermal-isobaric (NPT) ensemble simulation, and uniaxial tension and shearing simulation. All the inter- and intra-molecular interactions within the PP matrix, and between the graphene and PP, are described using the PCFF force field [34]. For the graphene, Adaptive Intermolecular Reactive Empirical Bond Order potential (AIREBO) [47] is used to describe the realistic plastic deformation and bond scission of $sp^2$ carbon at high strain.

The PCFF forcefield used to describe the interaction between the graphene and PP matrix does not distinguish the van der Walls (vdW) potential parameters of carbon atoms in STW defect and perfect hexagon and is a nonreactive potential. Therefore, neither new bond formation between carbon atoms in graphene and other atoms in PP matrix nor description of different interfacial adhesion characteristics according to the STW defect is accounted for. Nonetheless, the PCFF forcefield can describe various conformational change of organic materials including the graphene and various thermoplastics. Therefore, the MD simulation part focus on the conformation change of graphene and the resultant mechanical behavior of nanocomposites even without addressing bond order reactivity of carbon atoms in graphene.

### 3.1 Unit cell modeling of graphene, polymer, and nanocomposites

In this study, a total of three different graphene having 0, 5, and 10 STW defects are considered. To correlate the locally distorted structure to the macroscopic shear stress - shear strain relation of nanocomposites, the mean arithmetic roughness is calculated as,

$$
\delta=\frac{\sum_{i}\left|z_{i}-z_{\text {centroid }}\right|}{N} \tag{2}
$$

where, $N$ is the total number of carbon atoms in graphene, $z_{i}$ and $z_{centroid}$ indicate the vertical position of the $\mathrm{i}^{\text {th }}$ carbon atom and the centroid of the graphene, respectively.

![](./images/811050138351960064_7.jpg)

Fig. 3 (a) Transversely isotropic nanocomposites unit cell embedding different single layer graphene, and (b) coordinate system of nanocomposites, where y and z directions correspond to the two longitudinal directions of graphene.

The molecular unit cell structure of graphene-PP composites is constructed as a transversely isotropic periodic unit cell. One single layer is embedded in the middle of the hexahedron cell, as Fig. 3 (a) shows. For convenience, the coordinate systems are defined as shown in Fig. 3 (b). The PP matrix consists of 64 linear PP chains polymerized by 20 propylene monomers, and has amorphous structures. First, both amorphous PP and graphene are independently constructed using the Amorphous cell module, followed by a potential energy minimization using the conjugated gradient method, with a maximum energy derivative of 0.1 kcal/mole for the convergence criteria. Then, the two systems are vertically stacked without any vacuum area inside the layered unit cell, followed by the same energy minimization process. Using the layered structure shown in Fig. 3 (a) as the reference unit cell having no STW defects, a finite number of the STW defects are arbitrarily formed by hand. Since the addressed STW defect is distorted, and affects the arrangement of surrounding polymer molecules, the systems are finally optimized using the same

convergence criterion prior to the equilibration simulation.

### 3.2 Equilibration and computational tensile and shear tests via ensemble simulation
Prior to the production run to derive stress-strain curves, all the unit cells are equilibrated at 200 K and 1 atm through 3 nsec of the NPT ensemble simulation. For thermostat and barostat, the Nosé-Hoover extended Hamiltonian method [48] is used with 1 fsec of time step for the time integration of the equations of motion. The damping coefficient for the temperature and pressure control is 10 and 20 respectively at the give time step. Table 1 summarizes the composition of the nanocomposites unit cell after the NPT equilibration process.

Table 1. Composition of graphene reinforced nanocomposites after minimization at 200 K and 1 atm for 3 nsec.

<table>
  <thead>
    <tr>
      <th>No. of defects</th>
      <th>Volume fraction</th>
      <th colspan="3">Cell length</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>X(Å)</th>
      <th>Y(Å)</th>
      <th>Z(Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.05</td>
      <td>41.82</td>
      <td>38.65</td>
      <td>67.70</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.05</td>
      <td>41.36</td>
      <td>38.82</td>
      <td>67.82</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.05</td>
      <td>40.88</td>
      <td>38.97</td>
      <td>68.36</td>
    </tr>
  </tbody>
</table>

wall thickness of $3.4\ \mathrm{\mathring{A}}$ is used to calculate the volume fraction of graphene

The production runs to derive stress-strain curves of nanocomposites are implemented using the LAMMPS program. With a constant true strain rate of 0.0002 /ps, nanocomposite unit cells are continuously stretched or distorted, until the total true strain reaches 0.16 (16%). During the tensile and shear tests, a constant strain is applied at every 2,000 steps, followed by a short relaxation. The virial stress components [49] averaged over the relaxation period at each strain step are stored as the corresponding stress to complete the stress-strain curves. In applying the strain, we used a non-affine deformation scheme, and the velocity of cell edge in

tension is slower enough, compared with the velocity of sound of typical polymers ranging between 2,000 and 3,000 m/s [50]. Obviously the strain rate applied in this study is much faster than that in actual laboratory level tensile or shear tests. Nevertheless, the primary objective of our study on graphene nanocomposites is the qualitative evaluation of the effect of the addressed STW defect on the interfacial characteristics between graphene and PP matrix. Since we apply the same strain rate to all of the systems, regardless of the number of STW defects, the high strain rate in our MD simulation does not affect our deriving a useful qualitative conclusion on the effect of the STW defect. In the shearing of nanocomposites involving face-to-face shearing between graphene and PP matrix, the shear tests are repeated three times, by assigning a different random number seed to set the initial velocities of individual atoms. The resultant shear stress-shear strain relation is then averaged over the three different simulation results. Likewise, the tensile test in the z direction is also repeated three times, and the averaged stress-strain curves are obtained. For the rest of the tensile and shear tests (tension in the x and y direction, and shearing in the xy plane), where graphene resists most of the applied stress according to the periodicity of graphene, repeated simulation is not required. All the tensile and shear tests are implemented at 200 K, which is sufficiently lower than the glass transition temperature of PP to more clearly observe the effect of STW defect on the mechanical behavior of nanocomposites.

The stress-strain relations of single layer graphene having different numbers of STW defects are independently estimated. The periodic graphene unit cells are prepared by removing all of the PP molecules in nanocomposites. Therefore, these leave vacuum areas in the unit cell, which naturally hinder the periodicity in the z direction, which is essentially required for the mechanical characterization of freestanding single layer graphene. After 300 psec of NPT equilibration, each graphene unit cell is stretched in the x and y directions, until the strain of graphene reaches 15%, with the same strain rate of 0.0002 /psec.

## 4. Results and discussions

### 4.1 Adsorption energy between propylene and graphene (DFT simulation result)

The energy calculation in DFT simulation is usually affected by the exchange-correlation term, as well as consideration of the vdW interaction. To account for the effect of different simulation conditions, and to establish the baseline of adsorption energy according to the conditions, the adsorption energy of propylene monomer on each adsorption site defined in Fig. 2 is compared according to the aforementioned conditions. Table 2 shows that for the pristine graphene, the lowest adsorption energy of -0.4087 eV determined using the LDA-vdW condition is observed at Hole sites. Moreover, the interaction energy between propylene and graphenes calculated using the LDA approach is greater than those using the GGA approach in all cases. It is well known that the LDA's over binding tends to overestimate the adhesion energy between molecules and the GGA often underestimate it [51]. The interaction energy between graphene and propylene is strongly affected by the application of the vdW condition as well. Regardless of the choice of exchange-correlation function, the interaction energy with the vdW condition is prominently larger than those without the vdW condition. Therefore, the results using the LDA process and the DFT-D2 method are chosen in our DFT simulation. Figure S3 compares the variations of the adsorption between propylene and graphene according to the intermolecular distance for the adsorption sites of Top, Bridge, and Hole, respectively. The results using LDA-vdW formalism show the most distinct repulsive-attractive interaction among the four different exchange-correlation conditions. The results also support the well-known fact that the van der Waals interaction plays a very important role in describing the interaction between polymer and graphene [52-54].

Table 2. Adhesion energy of propylene on various sites of pristine and defective graphene.

<table>
  <thead>
    <tr>
      <th rowspan="2">Type</th>
      <th rowspan="2">Site</th>
      <th colspan="4">Adhesion energy (eV)</th>
    </tr>
    <tr>
      <th>LDA</th>
      <th>LDA-vdW</th>
      <th>GGA</th>
      <th>GGA-vdW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Graphene</td>
      <td>Bridge</td>
      <td>-0.09266</td>
      <td>-0.30801</td>
      <td>-0.01093</td>
      <td>-0.14016</td>
    </tr>
    <tr>
      <td>Top</td>
      <td>-0.09257</td>
      <td>-0.30913</td>
      <td>-0.01104</td>
      <td>-0.14069</td>
    </tr>
    <tr>
      <td>Hole</td>
      <td>-0.11640</td>
      <td>-0.40870</td>
      <td>-0.01455</td>
      <td>-0.16635</td>
    </tr>
    <tr>
      <td rowspan="9">STW<br>defective<br>graphene</td>
      <td>Bridge 1</td>
      <td>-0.63565</td>
      <td>-0.84466</td>
      <td>-0.53213</td>
      <td>-0.70653</td>
    </tr>
    <tr>
      <td>Bridge 2</td>
      <td>-0.61959</td>
      <td>-0.91033</td>
      <td>-0.50214</td>
      <td>-0.68665</td>
    </tr>
    <tr>
      <td>Bridge 3</td>
      <td>-0.67792</td>
      <td>-1.03600</td>
      <td>-0.55069</td>
      <td>-0.74057</td>
    </tr>
    <tr>
      <td>Bridge 4</td>
      <td>-0.68673</td>
      <td>-0.80547</td>
      <td>-0.55219</td>
      <td>-0.75523</td>
    </tr>
    <tr>
      <td>Top 5</td>
      <td>-0.63422</td>
      <td>-0.93491</td>
      <td>-0.50174</td>
      <td>-0.69874</td>
    </tr>
    <tr>
      <td>Top 6</td>
      <td>-0.66939</td>
      <td>-0.95872</td>
      <td>-0.54603</td>
      <td>-0.72359</td>
    </tr>
    <tr>
      <td>Top 7</td>
      <td>-0.67876</td>
      <td>-0.79027</td>
      <td>-0.55198</td>
      <td>-0.74298</td>
    </tr>
    <tr>
      <td>Hole 8</td>
      <td>-0.62550</td>
      <td>-0.79825</td>
      <td>-0.52335</td>
      <td>-0.68751</td>
    </tr>
    <tr>
      <td>Hole 9</td>
      <td>-0.67448</td>
      <td>-0.81692</td>
      <td>-0.54805</td>
      <td>-0.73625</td>
    </tr>
  </tbody>
</table>

Figure 2 shows the nine different positions a propylene molecule is placed over for the STW defective graphene, while Table 2 shows the interaction energies for each case. In STW defective graphene, the lowest adsorption energy of -1.036 eV is found when propylene is placed on the Bridge 3 position. Although the adsorption energy between propylene and STW defective graphene varies depending on the adsorption sites, the results obviously confirm that the STW defect strongly promotes the interaction between propylene and graphene. According to our DFT simulation, the STW defect not only alters the intrinsic adhesion energy between propylene and graphene, but also their equilibrium distance. Understanding the equilibrium distance is of primary importance for the non-bond potential energy

parameterization of carbon atoms in hexagonal and pentagonal rings for molecular dynamics.

Table S2 shows the equilibrium distance according to the adsorption sites. For example, regardless of the position, the equilibrium distance between propylene monomer and pristine graphene is about 2.2 Å; while when propylene is put on the Bridge 2 position in STW defect, it decreases to 1.74 Å.

The STW defect affects the geometry of graphene, as well as the intrinsic physical interaction between propylene and graphene. The local geometry change of defective sites can be obtained from both DFT calculation and MD simulation. Figure S4 shows the caved-in configuration of the STW defective graphene interacting with PP monomer simulated by DFT. The out-of-plane distortion and rippling of carbon atoms in STW defect is known to stabilize free-standing STW defective graphene [35]. According to our simulation, such distortion is also affected by the interaction with adsorbed propylene. Such a geometric change affects the shear stress transfer, and the resultant enhancement of the shear modulus of graphene/PP nanocomposites, and is further discussed in the MD simulation part below.

![](./images/811050138351960064_8.jpg)

Fig. 4 NEB calculation of monomer propylene migration in the tangential direction of (a) graphene, and (b) STW defective graphene.

Figures 4 (a) and (b) show migration energy barriers of propylene monomer to the armchair direction on pristine and STW defective graphene, respectively. The higher the

migration energy barrier, the more difficult the sliding of propylene on graphene. The migration energy barrier of the STW defective graphene is almost twice the migration energy barrier of the pristine, since the adsorption energy depends on the adsorption sites, as well as the non-flat geometry of graphene. From this result, we gain insight into the enhancement of the mechanical properties of PP/STW defective graphene nanocomposite.

The effect of polymer chain length is further explored by calculating the adhesion energy of prepared PP chains with graphene and STW defective graphene (Fig. 5). As the number of monomers (n) in the PP chain increases, the interaction between PP and graphene increases linearly, until n becomes four. However, the adhesion energy shows the discontinuity passing through n=5. This is related to the contact area between PP and graphene. It is well known that the van der Waals interaction is proportional to the surface contact area. Figure 5 shows that the optimum configuration of PP4 (n=4) has negligible curvature, while PP5 (n=5) has non-negligible finite curvature. For PP8 (n=8), both flat and curved configurations are observed at the same time. The same tendency is also shown in STW defective graphene. However, as the number of propylene monomers increases, the difference in adhesion energy between graphene and the STW defective graphene case does not change.

![](./images/811050138351960064_9.jpg)

Fig. 5 (a) Adhesion energy of polypropylene as the number of chain: graphene and STW defective graphene. (b) The calculation results of PP4, PP5, and PP8 cases.

![](./images/811050138351960064_10.jpg)

Fig. 6 (a) Adhesion energy PP chain (n=5) to the graphene according to the number of STW defects, and (b) the locally distorted structure of graphene interacting with propylene.

Finally, to understand the relation between STW defect density and the resultant adhesion energy, we investigated the adhesion energy of PP on graphene according to the number of STW defects. As the number of STW defects increases from one to four, the adsorption energies of PP chain (n=5) are calculated to be -1.17, -1.64, -1.78, and -2.31 eV, respectively.
Figure 6 shows that as the number of STW defects increases, the local geometry experiences severe distortion and bending. As is elucidated in the MD simulation part below, the distortion of graphene contributes to the promotion of interfacial shear stress transfer through the increased surface roughness. Therefore, it can be confirmed that the designed STW defects can promote the interfacial strength between PP and graphene. According to our DFT simulation results, there is a room for defect engineering in designing various multifunctional composites, addressing graphene as reinforcement.

![](./images/811050138351960064_11.jpg)

Fig. 7 Stress-strain curves of graphene according to the number of STW defects. (a) In the x (zigzag) direction, and (b) in the y (armchair) direction.

### 4.2 Stress-strain curves of graphene and nanocomposites (MD simulation results)

Figure 7 shows the stress-strain relation of single layer graphene according to the STW defects. As the literature has shown [55], failure stress and strain in the armchair direction are larger than those in the zigzag direction. As the number of STW defects in graphene increases, both the Young's modulus and the failure stress of graphene decrease. On the same defect, it has even been reported that the STW defect does not affect the Young's modulus of graphene, while the strength prominently decreases [56]. However, our study did not observe such a critical degradation. In particular, the graphene can still resist more than 10% of tensile strain, even with 10 STW defects. This is mainly attributed to the difference in strain rate considered in MD simulations (the strain rate in the current study is five times slower than that in Ref. [56]).

Since the degradation of graphene itself is not the major concern of our current study, further discussion on the degradation of graphene is beyond our scope. However, the degradation of graphene is clearly observed, and one can presume the stress-strain curves of nanocomposites involving the elongation of graphene from the degradative stress-strain relation of defective

graphene. In this respect, the STW defect is a negative one for the efficient reinforcing effect of nanocomposites. Even if the slope of the stress-strain curve of defected graphene decreases as the number of STW defect increases from 5 to 10, the failure strain increases from 0.085 to 0.1. This is due to the local energy dissipation at the STW defect sites. In usual, the STW defect cannot withstand larger stress value than perfect hexagonal carbon rings. As a result, the elastic energy dissipation occurs at lower stress level. Such an energy dissipation delays crack propagation into hexagonal carbon rings. Therefore, 10STW defected has more chances of local energy dissipation by the covalent bond collapse at the STW defect, global failure strain increases. Since the stress-strain curve of graphene is readily affected by the strain rate, the variation of the failure strain of graphene according to the SWT defect will may differ at different strain rate.

![](./images/811050138351960064_12.jpg)
(a) Longitudinal tension

![](./images/811050138351960064_13.jpg)
(b) Transverse tension

![](./images/811050138351960064_14.jpg)
(c) In-plane shear

![](./images/811050138351960064_15.jpg)
(d) Longitudinal shear

Fig. 8 Stress-strain curves of nanocomposites according to the number of STW defects.

Figure 8 shows the transversely isotropic stress-strain curves of nanocomposites according to the number of STW defects. In longitudinal tension, the degradative feature of the graphene by the STW defect in tension is reflected in the stress-strain curve of nanocomposites, since the graphene inside the composite is stretched according to the applied strain of composites. In this respect, the STW defect is not desirable for an efficient reinforcing effect. In transverse tension, the PP matrix primarily governs the overall stress-strain behavior, because the through-the-thickness deformation of graphene is not possible for its single layered structure. Figure 8 (b) shows that in the linear elastic region of less than 3% of strain, the STW defects slightly degrade the slope of the stress-strain relation. This is mainly attributed to the rippled structure of graphene, and insufficient adsorption of PP atoms

onto the wavy surface of graphene. Therefore, tiny voids are left between the rippled part of graphene and PP. This is later confirmed from the concentration profile of PP according to the number of STW defects. Since the PCFF force field does not distinguish carbon atoms in hexagonal, pentagonal, and heptagonal rings in describing the vdW interaction, intrinsic non-bond interaction tailored by the addressed STW defect confirmed from the current DFT simulation is not described in MD simulation using the PCFF force field. If the vdW force field parameters of carbon atoms in pentagonal and heptagonal rings were modified according to the DFT simulation results shown in Table 2, the adsorption of PP onto the defective graphene and the resultant stress-strain relation in transverse tension would be different. Modification of the non-bond interaction force field parameter for carbon atoms and MD simulation on STW defective graphene/polymer nanocomposites using the modified potential will be implemented elsewhere.

In in-plane shearing of nanocomposites where wrinkling of graphene is involved, the shear stress of nanocomposites prominently increases, as in the case of longitudinal tension. Since pure shear loading of a solid is analogous to the combined tension and compression in a biaxial loading condition, an abrupt drop of the composites shear stress is observed, which is attributed to the failure of the defective graphene. Since the boundary condition applied to distort the nanocomposites unit cell in the current MD simulation fully constrains the recovery of the graphene in the relaxation process, the magnitude of the shear stress shown in Fig. 8 (c) is an ideal upper bound stress value. According to the longitudinal tensile test and in-plane shear test, the STW defect is undoubtedly a negative one for efficient reinforcing. However, the abovementioned results are based on the assumption that graphene is subjected to the same amount of strain applied to the nanocomposites RVE shown in Fig. 3 with PBC. In real nanocomposites structures, where graphenes are fully embedded and weakly bonded to the host polymer matrix, such a large strain in graphene is not realistic. This is discussed in

detail in the next subchapter.

However, a totally different trend is observed in the longitudinal shearing of nanocomposites. Figure 8 (d) shows that when the embedded graphene is defect-free, the magnitude of the longitudinal shear stress does not increase. This result coincides with the mode II decohesion test by the MD simulation that the interfacial shear load transfer from graphene to polymer is very poor [57]. Similar results of the weakened interface condition between CNT and PP matrix in shearing have been reported [21]. However, as the number of STW defects increases, the magnitude of the longitudinal shear stress prominently increases to a maximum of 30 MPa with 10 STW defects. Since the embedded graphene is a single-layered structure, longitudinal shear deformation of graphene is physically not allowed. Therefore, the increase in shear stress is attributed to the increased shear stress of PP matrix. When graphene in composites is pristine and has a flat surface, neither anchoring of atoms in PP matrix by strong non-bond interaction, nor friction and the resultant interfacial interlocking are possible. The former and the latter are classified as chemical and geometrical factors, respectively, of the interfacial strengthening mechanism. However, Table 3 shows that when STW defects are addressed, slippage of the PP molecules on the surface of graphene in longitudinal shearing is prevented by the increased surface roughness. Figure 4 shows the NEB calculation result that also confirms this phenomenon. Since the PCFF force field does not describe different cohesive energy of carbon atoms in defective sites and perfect hexagonal rings at the interface with PP matrix, the chemical factor is not taken into account. Even without considering the improved adhesion energy between defects and PP as confirmed by the DFT simulation shown in Table 2, the increased surface roughness could accomplish a noticeable increase in shear moduli and deformation energy absorption.

Table 3. Surface roughness of graphene and maximum displacement of $sp^2$ carbon atoms according to the number of STW defects in graphene.

<table>
  <thead>
    <tr>
      <th>No. of defects</th>
      <th>Roughness (Å)</th>
      <th>Max. Displacement (Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.2640</td>
      <td>0.7914</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.3539</td>
      <td>1.3752</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.5242</td>
      <td>1.5415</td>
    </tr>
  </tbody>
</table>

### 4.3 Discussion on the boundary condition and load transfer in MD simulation

The fact that the STW defect can improve the surface roughness and interfacial shear load transfer investigated in MD simulations supports the defect engineering of graphene using intrinsic defects. In penny-shaped inclusion inside a matrix, the load transfer from matrix to inclusion and vice versa is mostly by the face-to-face shearing of graphene and PP matrix. In particular for the single layered graphene, interaction between carbon atoms in the basal plane and PP molecules, rather than the interaction between edge atoms and surrounding PP molecules, is the dominant load transfer mechanism. Therefore, in longitudinal tension the periodic boundary conditions (PBC) applied in current MD simulation assume that the interaction between edge carbon atom and PP molecules is strong enough, and perfect. In this respect, pull-out test of single layer graphene from PP matrix needs to be implemented, to draw more complete conclusions on the degradative or beneficial aspect of the defects.

If the strength between edge atoms and PP molecules is not enough to assume a perfect bonding condition, the PBC condition applied to longitudinal tension is obviously unrealistic. Since the degradation of composites' stress in Fig. 8 (a) is attributed to the degradation of graphene undergoing tensile behavior, a forcibly applied boundary condition enabling finite stretch of the graphene in nanocomposites unit cell is not realistic. In the same manner, the magnitude of the in-plane shear stress of composites shown in Fig. 4 (c) is interpreted as an upper bound. The applied shear loading condition with PBC to the nanocomposites unit cell

assumes that the graphene has exactly the same shear strain to the composites and matrix. Such a loading condition can be assumed without controversy only if the graphene and PP matrix are perfectly bonded at the interface. However, as has been proven in the longitudinal shear test shown in Fig. 8 (d), the interface between the graphene and PP is weak in nature. Therefore, the sword-in-sheath mode fracture can easily occur, unless graphene is strongly covalently grafted to the matrix to assume perfect interface between graphene and polymer in the longitudinal tension of nanocomposites. In sword-in-sheath mode interfacial sliding, the strain in graphene is not as large as the strain applied to the nanocomposites. Therefore, the degradation of real nanocomposites by the STW defects in longitudinal tension and in-plane shear is not as severe as is shown in the present MD simulation study.

According to the transformation of the transversely isotropic stiffness tensor [58], variation of the Young's moduli is very sensitive to the off-axis angle, while that of the shear moduli is less sensitive. Therefore when graphenes are randomly oriented inside the PP matrix, the dominance of the improved interfacial shear stress transfer confirmed in Fig. 4 (d) by the STW defect might be relatively high. Further parametric studies on the effect of graphene orientation and relative dominance of the stress-strain relation in tension and compression require application of mean field micromechanics models or mathematical homogenization theory considering the polydispersed representative volume element (RVE) [59] and imperfect interfacial bonding condition [32, 60].

Even if the periodic boundary condition applied to the nanocomposites is ideal, MD simulation using such condition is still meaningful in characterizing the nanoscale special effect. In characterizing the interphase zone, which plays a very important role in nanocomposites, through the inverse analysis [32], the transversely isotropic stiffness tensor of nanocomposites is obtained from the MD simulation using infinitely long CNT or graphene reinforced unit cell with periodicity. By equating the MD simulation result to the

conventional predictive micromechanics models with the same geometric condition, interfacial strength between CNT or graphene with polymer matrix is evaluated, and the properties of interphase zone are inversely characterized [32]. Once these characterizations are completed, the properties of nanocomposites at various compositions are determined under a realistic loading condition using the modified micromechanics models that include the interphase zone and interface condition.

### 4.4 Distribution of atoms and formation of material interphase zone

It is now well understood that both the interface and interphase zone are key factors to take advantage of when addressing nanoparticles and nanocarbon to make composites [61]. The interphase zone in the vicinity of the nanofillers consists of densified and crystallized matrix molecules, and has different physical properties from its original amorphous state [31-32, 60]. Usually, evolution of the unique properties of the interphase zone and its non-negligible contribution to the filler size dependent properties of composites is confined to very small size of the filler of less than the radius of gyration of typical polymers. On the other hand, the bond strength at the material interface is the intrinsic characteristics of two different materials. No matter how densely the interphase zone is formed, load transfer from the interphase zone to inclusion or vice versa is by the intrinsic strength of the interface. For example, typical engineering polymers usually form a unique interphase zone in the vicinity of graphene or CNTs; however, interfacial strength between them is poor, and separation and sliding at the interface can easily occur [32, 60]. Moreover, interfacial strength and tailoring of the surface properties of CNT or graphene can affect the formation of the interphase zone.

![](./images/811050138351960064_16.jpg)

Fig. 9 Relative atomic concentration profile indicating the spatial distribution of (a) graphene, and (b) PE matrix and interphase zone of graphene and PE matrix.

Since the STW defect roughens the graphene to which the matrix PP molecules are adsorbed and densified, we analyzed the relative atomic concentration of graphene and PP molecules in the transverse direction (z direction), to distinguish each phase in nanocomposites. Figure 5 (a) shows the concentration profile of graphene. As the number of STW defects increases, the concentration of the carbon atoms in graphene is broadened as a result of local rippling by the defects. The profile shown in Fig. 9 (a) coincides very well with the surface roughness of the graphene shown in Table 3.

In the concentration profile of PP matrix, the existence of the interphase zone is clearly confirmed, as is denoted by a blue square box in Fig. 9 (b). The zero profile zone in Fig. 9 (b)

corresponds to the graphene. Right in the vicinity of the graphene zone, there exist two distinguishable peaks indicating higher population of PP atoms than for other regions. Even if the graphene can have several ripples into which PP molecules can penetrate, according to the concentration profile of PP molecules, no noticeable evidence of the penetration of PP to the rippled sites is observed. Moreover, there is no distinguishable difference in the concentration profile of the interphase zone. Therefore, it can be concluded that the addressed STW defects do not prominently affect the formation of the interphase zone.

### 5. Conclusion
In this paper, the interfacial strengthening mechanism by the STW defects in single layer graphene in PP-based nanocomposites was studied using DFT simulation and MD simulations, respectively. In the DFT simulation, the adsorption energy of propylene monomer on graphene and STW defective graphene was calculated with the van der Waals interaction. It was found that the carbon atoms in defective graphene show stronger adhesion characteristics with propylene, than those in hexagon rings. As a result, an improved adhesive strength of propylene to the STW defective graphene was observed, which is dependent on the number of STW defects and propylene chain length. According to the electronic structure calculation, the difference of the magnitude in charge difference density was not noticeable at the interface between propylene and graphene with, and without, the STW defects. Therefore, the interaction between propylene and graphene is mainly governed by van der Waals force. Moreover, the STW defects increase the sliding resistance of propylene on graphene, as has been confirmed by the NEB calculation.

From the MD simulation, the degradation of single layer graphene by the STW defects was observed in tensile test of the graphene in the zigzag and armchair directions. On transversely isotropic nanocomposites unit cell, shearing simulation could confirm a clear improvement of

the interfacial shear strength between the STW defective graphene and PP matrix. The improved longitudinal shear modulus of nanocompoistes by the STW defect was mostly attributed to the increased surface roughness of the graphene. Since an infinitely long graphene in PP matrix was assumed via periodic boundary conditions, the graphene in PP matrix was artificially forced to stretch and distort by the same amount of strain to the composites in longitudinal tension, and in-plane shear. As a result, a clear degradative feature in the stress-strain behavior was observed in these two loading conditions. However, such a boundary condition is not realistic in describing the deformation of graphene in polymer matrix, in the sense that the bonding between graphene and PP matrix is not strong enough to assume a perfect interfacial bonding condition. Even if due to the computational costs, fully embedded graphene was not considered in this study, it can be reasonably conjectured that the degradation in longitudinal moduli and in-plane shearing is not as severe as has been observed in this study, or even negligible. Therefore, the rivaling effects of STW defects – degradation of the graphene, and improvement of the interfacial strength between graphene and the surrounding PP polymer – are very important design variables in taking advantage of the designed defects.

Most of the applications of graphene for multifunctional composites are accompanied by sophisticated purification and reduction of oxidation defects. Since a defect-free condition is ideal in maximizing the reinforcing effect of graphene, such devoted efforts are essential. Nevertheless, the performance of nanocomposites is affected not only by the properties of the embedded graphene, but also by the interfacial bonding condition. In this respect, the current study can confirm the new possibility of defect engineering to tailor the interfacial properties between the graphene and polymer, not by chemistry oriented functionalization, but by intrinsic defects.

### Acknowledgment

This work was supported by a National Research Foundation of Kroea (NRF) grant (No. 2012R1A3A2048841) funded by the Korean government (MSIP), and a Basic Science Research Program grant (2014R1A1A2054798) through the National Research Foundation of Korea (NRF), funded by the Ministry of Education Science and Technology. This research was also supported by the Chung-Ang University Research Grants in 2015.

## References

[1] S. Iijima, Helical microtubules of graphitic carbon, Nature 354(6348) (1991) 56-58.

[2] H.W. Kroto, J.R. Heath, S.C. O'Brien, R.F. Curl, R.E. Smalley, C60: Buckminsterfullerene, Nature 318(6042) (1985) 162-163.

[3] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, Y. Zhang, S.V. Dubonos, I.V. Grigorieva, A.A. Firsov, Electric Field Effect in Atomically Thin Carbon Films, Science 306(5696) (2004) 666.

[4] K.I. Bolotin, F. Ghahari, M.D. Shulman, H.L. Stormer, P. Kim, Observation of the fractional quantum Hall effect in graphene, Nature 462(7270) (2009) 196-199.

[5] C. Lee, X. Wei, J.W. Kysar, J. Hone, Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene, Science 321(5887) (2008) 385.

[6] I. Jung, D.A. Dikin, R.D. Piner, R.S. Ruoff, Tunable Electrical Conductivity of Individual Graphene Oxide Sheets Reduced at "Low" Temperatures, Nano Letters 8(12) (2008) 4283-4287.

[7] W. Cai, A.L. Moore, Y. Zhu, X. Li, S. Chen, L. Shi, R.S. Ruoff, Thermal Transport in Suspended and Supported Monolayer Graphene Grown by Chemical Vapor Deposition, Nano Letters 10(5) (2010) 1645-1651.

[8] K.S. Kim, Y. Zhao, H. Jang, S.Y. Lee, J.M. Kim, K.S. Kim, J.-H. Ahn, P. Kim, J.-Y. Choi, B.H. Hong, Large-scale pattern growth of graphene films for stretchable transparent electrodes, Nature 457(7230) (2009) 706-710.

[9] M. Pumera, A. Ambrosi, A. Bonanni, E.L.K. Chng, H.L. Poh, Graphene for electrochemical sensing and biosensing, TrAC Trends in Analytical Chemistry 29(9) (2010) 954-965.

[10] G.K. Dimitrakakis, E. Tylianakis, G.E. Froudakis, Pillared Graphene: A New 3-D Network Nanostructure for Enhanced Hydrogen Storage, Nano Letters 8(10) (2008) 3166-

3170.

[11] L.-C. Tang, Y.-J. Wan, D. Yan, Y.-B. Pei, L. Zhao, Y.-B. Li, L.-B. Wu, J.-X. Jiang, G.-Q. Lai, The effect of graphene dispersion on the mechanical properties of graphene/epoxy composites, Carbon 60 (2013) 16-27.

[12] Y. Zhang, L. Zhang, C. Zhou, Review of Chemical Vapor Deposition of Graphene and Related Applications, Accounts of Chemical Research 46(10) (2013) 2329-2339.

[13] W.S. Hummers, R.E. Offeman, Preparation of Graphitic Oxide, Journal of the American Chemical Society 80(6) (1958) 1339-1339.

[14] J. Chen, B. Yao, C. Li, G. Shi, An improved Hummers method for eco-friendly synthesis of graphene oxide, Carbon 64 (2013) 225-229.

[15] P.A. Thrower, Chemistry and physics of carbon, Chemistry and Physics of Carbon 5 (1969) 217-320.

[16] A.J. Stone, D.J. Wales, Theoretical studies of icosahedral C60 and some related species, Chemical Physics Letters 128(5) (1986) 501-503.

[17] C. Jin, K. Suenaga, S. Iijima, Vacancy Migrations in Carbon Nanotubes, Nano Letters 8(4) (2008) 1127-1130.

[18] Y. Zhu, S. Murali, W. Cai, X. Li, J.W. Suk, J.R. Potts, R.S. Ruoff, Graphene and Graphene Oxide: Synthesis, Properties, and Applications, Advanced Materials 22(35) (2010) 3906-3924.

[19] J.C. Charlier, Defects in Carbon Nanotubes, Accounts of Chemical Research 35(12) (2002) 1063-1069.

[20] P.Y. Huang, C.S. Ruiz-Vargas, A.M. van der Zande, W.S. Whitney, M.P. Levendorf, J.W. Kevek, S. Garg, J.S. Alden, C.J. Hustedt, Y. Zhu, J. Park, P.L. McEuen, D.A. Muller, Grains and grain boundaries in single-layer graphene atomic patchwork quilts, Nature 469(7330) (2011) 389-392.

[21] S. Yang, S. Yu, M. Cho, Influence of Thrower-Stone-Wales defects on the interfacial properties of carbon nanotube/polypropylene composites by a molecular dynamics approach, Carbon 55 (2013) 133-143.

[22] S. Yang, J. Choi, M. Cho, Intrinsic defect-induced tailoring of interfacial shear strength in CNT/polymer nanocomposites, Composite Structures 127 (2015) 108-119.

[23] S. Yadav, Z. Zhu, C.V. Singh, Defect engineering of graphene for effective hydrogen storage, International Journal of Hydrogen Energy 39(10) (2014) 4981-4995.

[24] P.T. Araujo, M. Terrones, M.S. Dresselhaus, Defects and impurities in graphene-like materials, Materials Today 15(3) (2012) 98-109.

[25] L.D. Carr, M.T. Lusk, Defect engineering: Graphene gets designer defects, Nat Nano 5(5) (2010) 316-317.

[26] A.J. Pak, E. Paek, G.S. Hwang, Tailoring the performance of graphene-based supercapacitors using topological defects: A theoretical assessment, Carbon 68 (2014) 734-741.

[27] E. Paek, A.J. Pak, G.S. Hwang, Large Capacitance Enhancement Induced by Metal- Doping in Graphene-Based Supercapacitors: A First-Principles-Based Assessment, ACS Applied Materials & Interfaces 6(15) (2014) 12168-12176.

[28] S.H.M. Jafri, K. Carva, E. Widenkvist, T. Blom, B. Sanyal, J. Fransson, O. Eriksson, U. Jansson, H. Grennberg, O. Karis, R.A. Quinlan, B.C. Holloway, K. Leifer, Conductivity engineering of graphene by defect formation, Journal of Physics D: Applied Physics 43(4) (2010) 045404.

[29] M. Berthe, S. Yoshida, Y. Ebine, K. Kanazawa, A. Okada, A. Taninaka, O. Takeuchi, N. Fukui, H. Shinohara, S. Suzuki, K. Sumitomo, Y. Kobayashi, B. Grandidier, D. Stiévenard, H. Shigekawa, Reversible Defect Engineering of Single-Walled Carbon Nanotubes Using Scanning Tunneling Microscopy, Nano Letters 7(12) (2007) 3623-3627.

[30] H. Terrones, R. Lv, Mauricio Terrones, M. S. Dresselhaus, The role of defects and doping in 2D graphene sheets and 1D nanoribbons, Reports on Progress in Physics 75(6) (2012) 062501.

[31] C. Wei, D. Srivastava, K. Cho, Structural Ordering in Nanotube Polymer Composites, Nano Letters 4(10) (2004) 1949-1952.

[32] S. Yang, S. Yu, W. Kyoung, D.-S. Han, M. Cho, Multiscale modeling of size-dependent elastic properties of carbon nanotube/polymer nanocomposites with interfacial imperfections, Polymer 53(2) (2012) 623-633.

[33] P. Dauber-Osguthorpe, V.A. Roberts, D.J. Osguthorpe, J. Wolff, M. Genest, A.T. Hagler, Structure and energetics of ligand binding to proteins: Escherichia coli dihydrofolate reductase-trimethoprim, a drug-receptor system, Proteins: Structure, Function, and Bioinformatics 4(1) (1988) 31-47.

[34] H. Sun, COMPASS: An ab Initio Force-Field Optimized for Condensed-Phase ApplicationsOverview with Details on Alkane and Benzene Compounds, The Journal of Physical Chemistry B 102(38) (1998) 7338-7364.

[35] J. Ma, D. Alfè, A. Michaelides, E. Wang, Stone-Wales defects in graphene and other planar $s{p}^{2}$-bonded materials, Physical Review B 80(3) (2009) 033407.

[36] G. Kresse, J. Hafner, Ab-Initio Molecular-Dynamics for Open-Shell Transition-Metals, Physical Review B 48(17) (1993) 13115-13118.

[37] G. Kresse, J. Furthmuller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Physical Review B 54(16) (1996) 11169-11186.

[38] S. Grimme, Accurate description of van der Waals complexes by density functional theory including empirical corrections, Journal of Computational Chemistry 25(12) (2004) 1463-1473.

[39] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range

dispersion correction, Journal of Computational Chemistry 27(15) (2006) 1787-1799.

[40] P.E. Blochl, Projector Augmented-Wave Method, Physical Review B 50(24) (1994) 17953-17979.

[41] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Physical Review B 59(3) (1999) 1758-1775.

[42] G. Henkelman, B.P. Uberuaga, H. Jonsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J Chem Phys 113(22) (2000) 9901-9904.

[43] X. Zhou, W. Liu, X. Yu, Y. Liu, Y. Fang, S. Klankowski, Y. Yang, J.E. Brown, J. Li, Tin Dioxide@Carbon Core–Shell Nanoarchitectures Anchored on Wrinkled Graphene for Ultrafast and Stable Lithium Storage, ACS Applied Materials & Interfaces 6(10) (2014) 7434-7443.

[44] V.M. Pereira, A.H. Castro Neto, H.Y. Liang, L. Mahadevan, Geometry, Mechanics, and Electronics of Singular Structures and Wrinkles in Graphene, Physical Review Letters 105(15) (2010) 156603.

[45] Accelrys Inc. San Francisco. <https://accelrys.com >).

[46] S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, Journal of Computational Physics 117(1) (1995) 1-19.

[47] S.J. Stuart, A.B. Tutein, J.A. Harrison, A reactive potential for hydrocarbons with intermolecular interactions, The Journal of Chemical Physics 112(14) (2000) 6472-6486.

[48] W.G. Hoover, Canonical dynamics: Equilibrium phase-space distributions, Physical Review A 31(3) (1985) 1695-1697.

[49] D.A. McQuarrie, Statistical Mechanics, University Science Books2000.

[50] D.R. Lide, CRC Handbook of Chemistry and Physics:1990-1991/ Davide R.Lide, 71.ed.. ed., Boca Raton: CRC Press, 1990., Boca Raton, 1990.

[51] J. Jilili, A. Abdurahman, O. Gülseren, U. Schwingenschlögl, Non-covalent functionalization of single wall carbon nanotubes and graphene by a conjugated polymer, Applied Physics Letters 105(1) (2014) 013103.

[52] T. Kerber, M. Sierka, J. Sauer, Application of semiempirical long-range dispersion corrections to periodic systems in density functional theory, Journal of Computational Chemistry 29(13) (2008) 2088-2097.

[53] P. Rubio-Pereda, N. Takeuchi, Density Functional Theory Study of the Organic Functionalization of Hydrogenated Graphene, The Journal of Physical Chemistry C 117(36) (2013) 18738-18745.

[54] M. Hassan, M. Walter, M. Moseler, Interactions of polymers with reduced graphene oxide: van der Waals binding energies of benzene on graphene with defects, Physical Chemistry Chemical Physics 16(1) (2014) 33-37.

[55] H. Zhao, K. Min, N.R. Aluru, Size and Chirality Dependent Elastic Properties of Graphene Nanoribbons under Uniaxial Tension, Nano Letters 9(8) (2009) 3012-3015.

[56] L. He, S. Guo, J. Lei, Z. Sha, Z. Liu, The effect of Stone–Thrower–Wales defects on mechanical properties of graphene sheets – A molecular dynamics study, Carbon 75 (2014) 124-132.

[57] Y. Li, G.D. Seidel, Multiscale modeling of the effects of nanoscale load transfer on the effective elastic properties of unfunctionalized carbon nanotube-polyethylene nanocomposites, Modelling and Simulation in Materials Science and Engineering 22(2) (2014) 025023.

[58] H.T. Hahn, S.W. Tsai, Introduction to Composite Materials, Taylor & Francis1980.

[59] S. Chang, S. Yang, H. Shin, M. Cho, Multiscale homogenization model for thermoelastic behavior of epoxy-based composites with polydisperse SiC nanoparticles, Composite Structures 128 (2015) 342-353.

[60] S. Yang, S. Yu, J. Ryu, J.-M. Cho, W. Kyoung, D.-S. Han, M. Cho, Nonlinear multiscale modeling approach to characterize elastoplastic behavior of CNT/polymer nanocomposites considering the interphase and interfacial imperfection, International Journal of Plasticity 41 (2013) 124-146.

[61] C.M. Hadden, D.R. Klimek-McDonald, E.J. Pineda, J.A. King, A.M. Reichanadter, I. Miskioglu, S. Gowtham, G.M. Odegard, Mechanical properties of graphene nanoplatelet/carbon fiber/epoxy hybrid composites: Multiscale modeling and experiments, Carbon 95 (2015) 100-112.