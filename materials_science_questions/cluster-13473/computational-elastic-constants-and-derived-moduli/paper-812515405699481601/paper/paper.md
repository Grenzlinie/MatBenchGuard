ORIGINAL PAPER

![](./images/812515405699481601_1.jpg)

# The effects of the van der Waals potential energy on the Young's modulus of a polymer: comparison between molecular dynamics simulation and experiment

Iwan H Sahputra $^{1,2}$ • Andreas Echtermeyer $^{1}$

Received: 16 October 2020 / Accepted: 7 January 2021 / Published online: 14 January 2021
© The Polymer Society, Taipei 2021

## Abstract
Molecular dynamics simulation were employed to investigate the effect of changing the potential energies describing primary and secondary bonds on the Young's modulus of a polymer. The energies were changed by arbitrarily modifying the parameters of the potential energy model function. The parameters influence the structure of the polymer and its global energy, eventually causing changes to the Young's modulus. The van der Waals energy describing secondary bonds gives the most significant contribution to the changes. Increasing the energy increases the density and Young's modulus. The trends are in agreement with experimental data.

Keywords Van der Waals energy · Young's modulus · Polymer · Molecular dynamics simulation

## Introduction
Stiffness is one of the interesting mechanical properties of polymers in many applications. In most engineering applications, materials should not deform beyond the required tolerances. It is generally accepted that a material exposed to a certain load, has a stiffness related to the second derivative of the material´s potential energy and the potential energy of a material is related to the interactions between atoms.

Some research showed that the stiffness of polymers is related to the intermolecular forces of the polymer chains. For instance, Rackley et al. [1] presented that the Young´s modulus of a densified polystyrene was higher than for the original material due to effects of intermolecular forces. The original polystyrene had a density of $1.049\ \text{g.ml}^{-1}$ and a Young's modulus of $3.55\ \text{GN.m}^{-2}$ (average of 3 experiments) while the densified polystyrene had a density of $1.055\ \text{g.ml}^{-1}$ and a Young's modulus of $3.82\ \text{GN.m}^{-2}$ (average of 4 experiments). The densification was done by heating the polystyrene under high pressure to above the glass transition temperature (high-temperature high-pressure, HT/HP polymerization), and cooling down slowly to room temperature before the pressure was released. The densification process did not lead to forming a new network of the polymer chains. Thus, the authors concluded that this is an indication that the intermolecular forces largely determine the elastic properties. Moreover, HT/ HP polymerization has been reported to produce urethane dimethacrylate (UDMA) [2] and polymer-based composites [3] with improved flexural strength and density.

Holliday and White [4] reported a relationship between the elastic modulus perpendicular to the chain axis direction and the cohesive energy density for various polymers. The elastic moduli were measured using an X-ray approach that can measure the modulus of the crystalline region on a molecular scale. As shown in Fig. 1, the elastic modulus increases with cohesive energy density. In addition, Seitz [5] developed a semi-empirical relationship between bulk modulus and cohesive energy of a polymer showing that the modulus increases with the cohesive energy.

Cohesive energy density is the energy required to break all intermolecular physical links in a unit volume of the material. Practically, cohesive energy density is defined as the ratio of the energy of vaporization to the molar volume

---

✉ Iwan H Sahputra
iwanh@petra.ac.id

1 Department of Mechanical and Industrial Engineering, Norwegian University of Science and Technology (NTNU), Trondheim, Norway
2 Industrial Engineering Department, Petra Christian University, Surabaya, Indonesia

![](./images/812515405699481601_2.jpg)

![](./images/812515405699481601_3.jpg)

Fig. 1 Young's modulus vs. cohesive energy density. Data from refer- ence [4]

both at the same temperature. However, the experimental determination of cohesive energy for polymers is not straightforward, since polymers do not evaporate. The cohesive energy data of polymers are usually calculated indirectly from dissolution or swelling measurements of polymers in a variety of solvents [6]. Unfortunately, the experimental data of cohesive energy for some polymers show large variations.

Molecular dynamics (MD) simulations can predict material properties based on the atomistic forces between atoms. Mechanical properties of polymers, such as Young's modulus and Poisson's ratio, obtained from the MD simulations, have been found to be similar to experimental measurements [7-15]. This means that MD simulations are a potential tool to simulate and study properties of new imaginary polymeric materials by modifying the interactions between atoms. Such simulations can give a better understanding on how the physics of polymers and work and they can potentially guide the development of new polymers.

Generally, interactions between atoms in the polymer system are represented in MD simulations by their potential energies, as follows:
$$
\mathrm{E}=\mathrm{E}_{\text {bond }}+\mathrm{E}_{\text {angle }}+\mathrm{E}_{\text {dihedral }}+\mathrm{E}_{\text {van der Waals }} \tag{1}
$$

The interactions include bonded interactions between atoms connected by chemical bonds and non-bonded interactions between atoms belonging to different chains or the same chain but not chemically bonded. The potential energies of bonded interactions are associated with the deviation of bond lengths, angles and rotations away from their equilibrium values ($\mathrm{E}_{\text {bond}}$, $\mathrm{E}_{\text {angle }}$ and $\mathrm{E}_{\text {dihedral}}$). They are much stronger than the non-bonded interaction.

The van der Waals (vdW) interactions are used to represent non-bonded interactions between atoms. The interactions include attractive and repulsive forces, due to dispersive forces during the fluctuations in the electronic clouds and due to electrons with the same spin respectively. The vdW energy calculated in MD simulations, thus, corresponds to cohesive energy measured experimentally. The Lennard-Jones 12-6 function is typically used to describe the vdW interactions, which takes the following form:
$$
V_{i j}=4 \varepsilon\left[\left(\frac{\sigma}{r_{i j}}\right)^{12}-\left(\frac{\sigma}{r_{i j}}\right)^{6}\right] \tag{2}
$$

where $\sigma$ is the collision diameter, $\varepsilon$ is the well depth constant, and r is the distance between two atoms. By increasing the $\varepsilon$ parameter of a polymer, a new imaginary simulated type of the polymer with higher vdW energy will be created. Theoretically, one can keep increasing or decreasing the $\varepsilon$ parameter and study its effect on the mechanical properties. Previous MD simulations have been performed to investigate the effect of $\varepsilon$ parameter on thermodynamics properties of polymers melts [16] and changes in the collective molecular motion that accompany the observed changes in the properties [17].

A short time simulation of a united atom model of Polyethylene under cyclic loading using a standard $\varepsilon$ parameter and an arbitrary higher $\varepsilon$ parameter was performed by the authors of this study [14]. The simulations were done for cycling in load control with a constant maximum load for each cycle. The simulated cyclic mean strain was lower for the polymer with a higher $\varepsilon$ parameter compared to the polymer with standard $\varepsilon$ parameter. Further, the mean strain did not seem to increase with the number of cycles, indicating that creep was reduced. This study extends the work to the Young's modulus of Polycarbonate (PC) using the previously developed model for PC [18]. PC is an amorphous polymer, which is widely used in many engineering applications. Various values of the $\varepsilon$ parameter were chosen to investigate their effect on the vdW energy and the Young's modulus was calculated at low strain deformation using MD simulations. In order to see how changing the primary bond characteristics would influence the results, the case of stronger bonded potentials (Ebond, Eangle and Edihedral) was also investigated.

## Methods

### System preparation

The initial structure of polycarbonate PC ($\mathrm{C}_{16}\mathrm{H}_{14}\mathrm{O}_{3}$) was built in the MD model using the Polymer and Amorphous

Builder function of MAPS software [19], containing 9902 atoms. The Dreiding potential energy parameters [20] were used as standard values of bonded and nonbonded interactions. The accuracy of the Dreiding force field has been tested by comparing measured and determined crystal structures of organic compounds, rotational barriers of a number of molecules and relative conformational energies and barriers of a number of molecules [20]. In the force field, charges are ignored except for peptides and nucleic acids systems.

MAPS creates the initial structure based on the Monte Carlo method combined with the recoil growth technique. Table 1 shows how equilibrium was approached in this work. An MD program designed for parallel computers, LAMMPS [21], was employed to perform MD simulations. All simulations were performed on the supercomputer at NTNU.

Stage 1 was done to speed up the relaxation of high potential energy created during the generation of the initial structure. Stage 2 and 3 used a temperature of 500 K, close to the melting temperature of PC [22]. In stage 4, the temperature was cooled down to room temperature (300 K). In stage 2-6, the time-reversible measure-preserving Verlet and rESPA integrators were used to integrate the equation of motion. Periodic boundary conditions were applied to all directions of the simulation box, simulating a bulk system. The quality of the equilibrium was checked by monitoring the fluctuations of energy, pressure and dimension of the simulation box.

## Tensile testing simulations

Deformation was simulated by changing the simulation box in one longitudinal direction during a dynamic run. The other two transverse directions of the box were set to zero pressures, allowing the box to contract sideways. The change in longitudinal dimension was set at a constant engineering strain rate $(10^8\ \text{s}^{-1})$. The tensile strain is unitless and is defined as the length change divided by the original simulation box length.

<table>
<caption>Table 1 Methods employed to reach equilibrium of the polymer configuration</caption>
<thead>
<tr>
<th>Stage</th>
<th>Method/technique</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Energy minimization, using Polak-Ribiere Conjugate Gradient algorithm<br>Energy stopping tolerance: $10^{-8}$</td>
</tr>
<tr>
<td>2</td>
<td>NVT ensemble, using Langevin thermostat<br>Temperature: 500 K</td>
</tr>
<tr>
<td>3</td>
<td>NPT ensemble, using Noose-Hoover thermostat and barostat<br>Temperature: 500 K<br>Pressure: 0 atm</td>
</tr>
<tr>
<td>4</td>
<td>NPT ensemble, using Noose-Hoover thermostat and barostat<br>Temperature: 500 K to 300 K<br>Pressure: 0 atm</td>
</tr>
<tr>
<td>5</td>
<td>NVT ensemble, using Langevin thermostat<br>Temperature: 300 K</td>
</tr>
<tr>
<td>6</td>
<td>NPT ensembles, using Noose-Hoover thermostat and barostat<br>Temperature: 300 K<br>Pressure: 0 atm</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Factors applied to the parameters of standard bonds</caption>
<thead>
<tr>
<th>Parameter</th>
<th colspan="3">Simulation</th>
</tr>
<tr>
<th></th>
<th>A</th>
<th>B</th>
<th>C</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bond</td>
<td>1</td>
<td>10</td>
<td>10</td>
</tr>
<tr>
<td>Angle</td>
<td>1</td>
<td>10</td>
<td>10</td>
</tr>
<tr>
<td>Dihedral</td>
<td>1</td>
<td>1</td>
<td>10</td>
</tr>
<tr>
<td>Van der Waals ($\varepsilon$)</td>
<td>0.5, 0.75, 1,<br>1.25,<br>1.5, 1.75, 2,<br>5, 10</td>
<td>0.5, 1, 2, 5, 10</td>
<td>0.5, 1, 2, 5, 10</td>
</tr>
</tbody>
</table>

Various values of the vdW potential´s energy parameter $\varepsilon$ (see Eq. 2) were applied to investigate their effect on the Young's modulus, as shown in Table 2—simulation A. The Dreiding $\varepsilon$ parameters of the vdW potential for C, O, and H atoms were 0.0951, 0.0957, and $0.0152\ \text{kcal.mol}^{-1}$ respectively. Therefore, for instance, in the case of the normalized $\varepsilon$ parameters of 2, the Dreiding $\varepsilon$ parameters for C, O, and H atoms will be 0.1902, 0.1914, and $0.0304\ \text{kcal. mol}^{-1}$ respectively. Each value was set up at the beginning of the system preparation, i.e. stage 1.

The Young's modulus was obtained from the slope of the stress-strain curve at low strain (2%). Three simulations were performed to calculate the Young's modulus. In each simulation, the simulation box was elongated in the $X$, $Y$ or $Z$ direction respectively and the obtained Young's moduli were averaged. Similar to real polymers, this approach investigates slightly different molecular structures in each case, giving statistically representative values of the polymer properties. According to the ASTM D638 (Standard Test Method for

![](./images/812515405699481601_4.jpg)

Tensile Properties of Plastics), several test specimens are needed for obtaining properties of isotropic polymers. The properties should not vary significantly from one orientation to the other. For anisotropic polymers, several series of specimens are needed to be tested normal to and parallel to the principle axis of anisotropy. For each series of tests, the arithmetic mean of all measured values is calculated and reported as the "average value" for the particular property in question.

The effect of the $\varepsilon$ parameter of the vdW potential on the Young's modulus was initially investigated for standard PC. The other bonding energies describing the primary bonds along the chain's backbone ($\mathrm{E_{bond}}$, $\mathrm{E_{angle}}$ and $\mathrm{E_{dihedral}}$) had the typical values for PC. In order to see how changing the primary bond characteristics would influence the results, the cases of stronger bonding potentials ($\mathrm{E_{bond}}$, $\mathrm{E_{angle}}$ and $\mathrm{E_{dihedral}}$) were also investigated, as shown in Table 2 - simulations B and C.

In addition to room temperature (300 K), the effect of the $\varepsilon$ parameters of the vdW potential on the Young's modulus was also investigated at very low temperature. The previous system at 300 K was used and cooled down to 0.1 K. The next stage was done within the NVT ensemble at 0.1 K. The final stage was carried out within the NPT ensemble.

## Results and discussion

### Young´s modulus vs. local van der Waals potential energy

This study set out investigating the effect of the potential depth parameter ($\varepsilon$) of the van der Waals (vdW) potential on the Young´s modulus of an amorphous polymer resembling poly carbonate PC. The $\varepsilon$ parameter controls the depth of the local vdW potential energy acting between polymer chains.

Figure 2 presents the effect of the $\varepsilon$ parameter on the predicted Young's modulus from simulations at 300 K and at 0.1 K. The error bars refer to the standard error of the Young's modulus calculated by the following equation:

$$
\text{Standard error} = \frac{\sigma}{\sqrt{n}} \tag{3}
$$

where $\sigma$ is standard deviation and n is number of measurement.

Increasing the $\varepsilon$ parameter increases the calculated Young's modulus. It can be seen that there is a linear relationship between the $\varepsilon$ parameter value and the calculated Young's modulus. A higher $\varepsilon$ parameter causes stronger vdW interactions and more energy is needed to move the atoms from their initial positions, therefore, polymer chains are getting more difficult to slide against each other. This indicates that the ease of sliding chains against each other dominates the stiffness characteristics of the polymer.

For a very low $\varepsilon$ parameter, the polymer chains move like a liquid under tensile deformation. With a normalized $\varepsilon$ parameter of 0.5 (normalized against the standard values for PC), the calculated Young's modulus is almost zero. The Young's modulus calculated with a normalized $\varepsilon$ parameter of 10 is about ten times higher than calculated with a normalized $\varepsilon$ parameter of 1. For a very high $\varepsilon$ parameter, the chains may become tightly attached to each other and form a kind of crystal structure. The primary forces of bonds along the polymer chain may eventually become negligible. This extreme case would be very unrealistic, though.

The temperature significantly affects the predicted Young's modulus. Lower temperature produces a higher Young's modulus since the sections of the polymer chain have less kinetic energy due to low temperature reducing their ability to slide past each other. This is in agreement with most experimental data and was also shown by molecular

![](./images/812515405699481601_5.jpg)

Fig. 2 Effect of the $\varepsilon$ parameter on the predicted Young's modulus, comparison between simulations at 300 K (simulation A) and 0.1 K. The plot on the left is an enlarged plot for $\varepsilon$ parameters between 0.5—2

![](./images/812515405699481601_6.jpg)

Fig. 3 Effect of the $\varepsilon$ parameter on the predicted Young's modulus, comparison between simulations A, B, and C (Table 2) at 300 K. The plot on the left side is an enlarged plot for $\varepsilon$ parameters between 0.5—2

dynamics simulations [13, 15, 23]. Moreover, the linear increase of modulus with the $\varepsilon$ parameter is observed for both temperatures analyzed here, as presented in Fig. 2.

Figure 3 presents the comparison between simulations A, B, and C (see Table 2). The potentials of the primary bonds were increased in simulations B and C. The bond stretch and bond angle potential parameters were increased by a factor 10 in the simulation B, compared to the standard case in simulation A. In addition to that, in the simulation C, the dihedral angle potential parameter was increased by a factor of 10. Increasing of bond stretch, bond angle, and dihedral angle potential parameters does not give a significant increase of the Young's modulus. The main increase is still caused by the $\varepsilon$ parameter. The increase also remains linear with $\varepsilon$ in all cases. The small effect of changing the primary bonds (bond length, angle, dihedral) parameters of the polymer chain on the modulus strengthens the statement that the vdW depth parameter $\varepsilon$ is the most important one.

Young´s modulus vs. global van der Waals potential energy

A different vdW depth parameter ($\varepsilon$) causes different molecular arrangements when the polymer is brought to equilibrium. This means the global vdW energy of the entire polymer body is not only affected by the parameter, but also by how the molecules arrange themselves. Figure 4 presents that not only the $\varepsilon$ parameter influences the global vdW potential energy of the system, but also the bonded potential parameters ($E_{bond}$, $E_{angle}$ and $E_{dihedral}$). All parameters of the potentials influence the structure of polymer during the equilibration processes and eventually, the polymer´s global vdW energy. However, the $\varepsilon$ parameter gives the most significant contribution to the global vdW energy of the polymer.

The arrangements of chains are also affected by the primary bonded potential parameters. Stronger primary potentials create a structure having lower vdW energy. This can be seen from simulation C having the lowest vdW energy, although its primary bonded potential parameters are 10 times higher than in simulation A. However, it was found that for each simulation, the global vdW energy, being the integrated value of the entire polymer´s local vdW potentials, is linearly correlated to the vdW depth parameter.

Figure 5 shows that in each simulation, increasing vdW energy increases the Young's modulus. However, it should be noted that considering the overall simulation results, the relationship is not simply linear. This indicates that, in addi- tion to the vdW energy, there are contributions from bonded potential energies to the stiffness property of the polymer.

![](./images/812515405699481601_7.jpg)

Fig. 4 Effect of $\varepsilon$ parameter on the absolute global vdW energy

![](./images/812515405699481601_8.jpg)

![](./images/812515405699481601_9.jpg)

Fig.5 Effect of the global vdW energy on the predicted Young's modulus

But, a fairly linear relationship between vdW energy and Young's modulus can still be observed for each simulation.

The vdW energy in the MD simulation is represented by the Lennard-Jones 12-6 function, which includes the attractive and repulsive interactions between two atoms. The attractive contribution is due to dispersive forces because of the instantaneous dipoles, which arise during the fluctuations in the electronic clouds. The repulsive interaction is based on quantum mechanics principles, that two electrons cannot have the same quantum numbers; they cannot occupy the same region. The vdW energy calculated in MD simulations, thus, corresponds to cohesive energy measured experimentally.

The relationship between the Young's modulus and the vdW energy predicted by MD simulations agrees with the experimental relationship between the elastic modulus perpendicular to the chain axis direction and cohesive energy density measured experimentally by Holliday and White [4]. Since they measured the experimental modulus using an X-ray method for the crystalline region, the intermolecular forces (represented by cohesive energy) should have a more significant role in governing the modulus perpendicular to the chain axis direction than the modulus parallel to the chain axis direction. In the later case, the contribution of intramolecular forces (primary bonds) would be more significant and the modulus should be higher.

Experimental data also show a relation between intermolecular forces, density and stiffness of a polymer [1]. Figure 6-left presents the relation between the density vs. global vdW energy (which represents the intermolecular forces) calculated from the simulations. The density increases as the global vdW energy increases. Increasing the global vdW energy makes closer molecular packing. The increase in the primary bonded potentials (stretch, angle and dihedral) also contributes to the change of density. However, the increased primary bonded potentials make the density increase less than when only the vdW energy increases. Figure 6-right presents the density vs. Young's modulus. For each simulation, increasing the density increases the Young's modulus, which is in agreement with the experimental data [1]. However, it should be noted that not only the change in density influences the Young's modulus but the interplay between changes in bonded and non-bonded potentials.

![](./images/812515405699481601_10.jpg)

Fig.6 Density vs vdW energy (left) and density vs. Young's modulus (right) calculated from the MD simulations

## Conclusions
It was shown by using MD simulations that there is a linear relationship between the van der Waals (vdW) depth parameter and the Young's modulus. Increasing the parameter increases global vdW energy, density and Young's modulus of the simulated polymer. Primary bond and vdW potential energy parameters influence the structure of the polymer and its global vdW energy, which eventually changes the Young's modulus. However, the vdW depth parameter gives the most significant contribution to the changes. The MD simulations have shown relationships between global vdW energy vs Young's modulus and global vdW energy vs density, in agreement with experimental data. Young's modulus and density increase along with vdW energy. These findings provide enhanced insights into the structure-property relationship of a polymer.

Data availability Data available on request from the authors.

## References
1. Rackley FA, Turner HS, Wall WF, Haward RN (1974) Preparation of crosslinked polymers with increased modulus by high-pressure polymerization. J Polym Sci Polym Phys 12:1355-1370
2. Phan AC, Tang M-L, Jean-François Nguyen N, Ruse D, Sadoun M (2014) High temperature high-pressure polymerized urethane dimethacrylate-Mechanical properties and monomer release. Dent Mater 30(3):350-356
3. Nguyen J-F, Véronique Migonney N, Ruse D, Sadoun M (2012) Resin composite blocks via high-pressure high-temperature polymerization. Dent Mater 28(5):529-534
4. Holliday L, White J (1971) The stiffness of polymers in relation to their structure. Pure Appl Chem 26:545
5. Seitz JT (1993) The estimation of mechanical properties of polymers from molecular structure. J Appl Polym Sci 49:1331-1351
6. Fedors R (1974) Method for Estimating Both the Solubility Parameters and Molar Volumes of liquids. Polym Eng Sci 14:472
7. Brown D, Clarke JHR (1991) Molecular dynamics simulation of an amorphous polymer under tension: I. Phenomenology. Macromolecules 24(8):2075-2082
8. Yang L, Srolovitz DJ, Yee AF (1997) Extended ensemble molecular dynamics method for constant strain rate uniaxial deformation of polymer systems. J Chem Phys 107:4396

9. Fortunelli A, Geloni C (2004) Simulation of the plastic behavior of amorphous glassy bis-phenol-A-polycarbonate. J Chem Phys 121(10):4941-4950
10. Lyulin AV, Li J (2006) Atomistic Simulation of Bulk Mechanics and Local Dynamics of Amorphous Polymers. Macromolecular Symposia 237(1):108-118
11. Capaldi F, Boyce MC, Rutledge GC (2004) Molecular response of a glassy polymer to active deformation. Polymer 45:1391-1399
12. Hossain D, Tschopp M, Ward D, Bouvard J, Wang P, Horstemeyer M (2010) Molecular dynamics simulations of deformation mechanisms of amorphous polyethylene. Polymer 51:6071-6083
13. Sahputra IH, Echtermeyer A (2013) Effects of temperature and strain rate on the deformation of amorphous polyethylene: a comparison between molecular dynamics simulations and experimental results. Model Simul Mater Sci Eng 21:065016
14. Sahputra IH and Echtermeyer AT, (2014) "Creep-fatigue relationship in polymer: a molecular dynamics simulations approach," Macromolecular Theory and Simulations
15. Sahputra IH, Alexiadis A, Adams MJ (2018a) Temperature and configurational effects on the Young's modulus of poly (methyl methacrylate): a molecular dynamics study comparing the DREI-DING, AMBER and OPLS force fields. Mol Simul 44(9):774-780
16. Wen-Sheng Xu, Douglas JF, Freed KF (2016) Influence of Cohesive Energy on the Thermodynamic Properties of a Model Glass-Forming Polymer Melt. Macromolecules 49(21):8341-8354
17. Xu W-S, Douglas JF, Freed KF (2016) Influence of cohesive energy on relaxation in a model glass-forming polymer melt. Macromolecules 49(21):8355-8370
18. Sahputra IH and Echtermeyer A, (2013) "Molecular Dynamics Simulation of Polycarbonate Deformation: Effect of Temperature and Strain Rate," in International Conference on Computational Mechanics (CM13), Durham
19. http://www.scienomics.com/
20. Mayo SL, Olafson BD (1990) DREIDING: a generic force field for molecular simulations. J Phys Chem 94(26):8897-8909
21. Plimpton S (1995) Fast parallel algorithms for short-range molecular dynamics. J Comput Phys 117(1):1-19
22. Bicerano J, (2002) Prediction of Polymer Properties, Marcel Dekker
23. Sahputra IH, Alexiadis A, Adams MJ (2018b) Temperature dependence of the Young's modulus of polymers calculated using a hybrid molecular mechanics-molecular dynamics method. J Phys: Condens Matter 30(35):355901

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812515405699481601_11.jpg)