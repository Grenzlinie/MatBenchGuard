![](./images/813144599680778241_1.jpg)

Mesoscale properties of clay aggregates from potential of mean force representation of interactions between nanoplatelets

Davoud Ebrahimi, Andrew J. Whittle, and Roland J.-M. Pellenq

Citation: *The Journal of Chemical Physics* **140**, 154309 (2014); doi: 10.1063/1.4870932
View online: http://dx.doi.org/10.1063/1.4870932
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/140/15?ver=pdfcov
Published by the AIP Publishing

### Articles you may be interested in
Strengthening metal nanolaminates under shock compression through dual effect of strong and weak graphene interface
Appl. Phys. Lett. **104**, 231901 (2014); 10.1063/1.4882085

Size-dependent elasticity of amorphous silica nanowire: A molecular dynamics study
Appl. Phys. Lett. **103**, 201905 (2013); 10.1063/1.4830038

Aggregation in dilute aqueous tert-butyl alcohol solutions: Insights from large-scale simulations
J. Chem. Phys. **137**, 034509 (2012); 10.1063/1.4731248

Water properties and potential of mean force for hydrophobic interactions of methane and nanoscopic pockets studied by computer simulations
J. Chem. Phys. **127**, 054505 (2007); 10.1063/1.2749250

Competition of hydrophobic and Coulombic interactions between nanosized solutes
J. Chem. Phys. **121**, 5514 (2004); 10.1063/1.1783274

![](./images/813144599680778241_2.jpg)

THE JOURNAL OF CHEMICAL PHYSICS 140, 154309 (2014)
![](./images/813144599680778241_3.jpg)

# Mesoscale properties of clay aggregates from potential of mean force representation of interactions between nanoplatelets

Davoud Ebrahimi, $^{1}$ Andrew J. Whittle, $^{1}$ and Roland J.-M. Pellenq $^{1,2,3,a)}$

$^{1}$ Department of Civil and Environmental Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA
$^{2}$ Centre Interdisciplinaire de Nanosciences de Marseille, Aix-Marseille Université, CNRS, Campus de Luminy, 13288 Marseille Cedex 09, France
$^{3}\langle$ MSE $\rangle^{2}$, UMI 3466 CNRS-MIT, Cambridge, Massachusetts 02139, USA

(Received 16 January 2014; accepted 20 March 2014; published online 21 April 2014)

Face-to-face and edge-to-edge free energy interactions of Wyoming Na-montmorillonite platelets were studied by calculating potential of mean force along their center to center reaction coordinate using explicit solvent (i.e., water) molecular dynamics and free energy perturbation methods. Using a series of configurations, the Gay-Berne potential was parametrized and used to examine the meso-scale aggregation and properties of platelets that are initially random oriented under isothermal-isobaric conditions. Aggregates of clay were defined by geometrical analysis of face-to-face proximity of platelets with size distribution described by a log-normal function. The isotropy of the microstructure was assessed by computing a scalar order parameter. The number of platelets per aggregate and anisotropy of the microstructure both increases with platelet plan area. The system becomes more ordered and aggregate size increases with increasing pressure until maximum ordered state at confining pressure of 50 atm. Further increase of pressure slides platelets relative to each other leading to smaller aggregate size. The results show aggregate size of (3–8) platelets for sodium-smectite in agreement with experiments (3–10). The geometrical arrangement of aggregates affects mechanical properties of the system. The elastic properties of the meso-scale aggregate assembly are reported and compared with nanoindentation experiments. It is found that the elastic properties at this scale are close to the cubic systems. The elastic stiffness and anisotropy of the assembly increases with the size of the platelets and the level of external pressure. © 2014 AIP Publishing LLC.

[http://dx.doi.org/10.1063/1.4870932]

## INTRODUCTION

Clay is the most abundant mineral on the earth $^{1}$ and one of the most important industrial materials with a wide range of applications in construction, environmental, pharmaceutical, and process industries. $^{2}$ Aggregation of clay mineral plays an important role in calculating the physical properties of soils such as elastic stiffness properties that control elastic wave propagation and the transport of ionic substances required for applications in waste management and environmental protection. Aggregation or dispersion of clay particles also affects the viscosity of drilling fluids. For these reasons, the coagulation of clay particles has received prominent attention in the literature. $^{3-13}$

Clay minerals have a layered structure at the nanoscale. Each layer consists of some combination of silicon tetrahedra and aluminum octahedra mineral sheets as basic units. For instance, the structure of natural Wyoming Na-montmorillonite has the following experimental formula: $^{14}$ $Na_{0.75}nH_{2}O[Si_{7.75}Al_{0.25}][Al_{3.5}Mg_{0.5}]O_{20}(OH)_{4}$. This structure comprises two tetrahedral sheets sandwiching an octahedral sheet. Due to isomorphous substitutions of metal ions, the clay has a net negative surface charge. For the Wyoming Na-montmorillonite, $3.125\%$ of the silicon ions, $Si^{4+}$, in the tetrahedral sheet are substituted by aluminum, $Al^{3+}$, while $12.5\%$ of the aluminum ions, $Al^{3+}$, in the octahedral sheet are substituted by magnesium, $Mg^{2+}$. In the current research the negative charge is balanced by sodium ions, $Na^{1+}$ between the clay layers. In a recent study, $^{15}$ we characterized structural and mechanical properties of montmorillonite at the atomic scale. This paper presents a methodology to describe clay aggregates at the meso-scale from a simulation point of view.

The fundamental multi-scale approach toward the understanding clay behavior at the macroscopic scale (to address practical applications in geotechnical and petroleum engineering) aims at modeling the material at scales ranging from the atomistic level to the macroscopic system. Molecular dynamics simulation (MD) is a versatile technique to study interaction between colloidal nanoplatelets at the atomistic scale. In order to represent clay aggregates with mesopores and grain boundaries, the model must be scaled up from the atomistic level to the submicron length scale. This exceeds the computational possibilities of full atomistic models and motivates a multiscale and consistent approach. Porion et al. $^{16}$ were the first to study macroscopic mobility of water molecules within nematic suspension of Laponite clay by performing multiscale statistical analysis. Previous attempts to study clay aggregates were based on using quadrupoles $^{17,18}$ or pseudo-charge sites to represent clay platelets. $^{19-26}$ The multipole representation of platelets might not be effective

$^{a)}$ Author to whom correspondence should be addressed. Electronic mail: pellenq@mit.edu

0021-9606/2014/140(15)/154309/17/$30.00
140, 154309-1
© 2014 AIP Publishing LLC

because of difficulties in modeling the charge distributions and existence of local defects associated with isomorphous substitutions. To overcome these limitations, we have used an upscaling strategy to run MD at meso-scale through calcula- tion of free energy for face-to-face and edge-to-edge config- urations of clay nanoplatelets using full atomistic represen- tation of platelets, water molecules, and ions. We then use the thermodynamic perturbation method to calculate the po- tential of mean force (PMF) (e.g., free energy) as a function of the distance between the centers of two platelets, an ap- proach previously used for interaction between two graphene sheets. $^{27}$ The free energy is then used to calibrate the Gay Berne (GB) potential $^{28}$ for different platelet sizes to study meso-scale interactions of multiple platelets with different orientations. The resulting arrangements of particles deter- mine the microstructure of clay aggregates that control me- chanical properties such as elastic stiffness. We characterize microstructure of the stabilized systems and report their full elastic properties.

## NANO-SCALE PMF CALCULATION

The proposed methodology begins with the calculation of the free energy along a reaction coordinate which corresponds to the separation distance (Figure 1) for face-to-face and edge- to-edge interactions of two Wyoming Na-montmorillonite platelets in liquid water. In order to calculate the change in free energy of the system from state A, when clay platelets are far from each other, to state B, when they are in close proxim- ity, we define several intermediate states covering the change from state A to state B in small increments to enhance sam- pling of the phase space. Using a stratification strategy, suc- cessive states are separated by low energy barriers such that the phase space is fully explored enabling statistical averaging of the states. $^{29}$ We construct series of MD trajectories, each one representing one value of center to center distance. The trajectory of the MD simulation at one state is perturbed along the reaction coordinate to the target state, while all other de- grees of freedom are frozen. Free energy differences between two successive reference and target thermodynamic states will be calculated and added along the transformation path from state A to state B.

The analyses are carried out using the CLAYFF $^{30}$ force field that has been used successfully for simulation of clay minerals. $^{31,32}$ CLAYFF is a versatile force field built around the flexible version of the Simple Point Charge (SPC) water model. $^{33}$

Full atomistic MD simulations were carried out by us- ing the GROMACS $^{34}$ simulation package. The atomic struc tures were visualized using $VMD^{35}$ molecular graphic soft ware. The crystallography for 2:1 clay mineral was taken from Refson et al. $^{36}$ Isomorphous substitution was carried out randomly. We obeyed Lowenstein's rule for distribution of defects. Depending on the statistical ensemble, the Nosé- Hoover thermostat $^{37,38}$ is used to control temperature and the Parrinello-Rahman $^{39}$ barostat to control pressure in the sys tem. An integration time step of 1 fs (femto second) was used in all full atomistic simulations. Three-dimensional, pe- riodic boundary conditions were applied along with the min- imum image convention (a cutoff radius of $8.5\ \mathring{A}$ was used for short range interactions). The long range electrostatic Coulombic interactions were calculated using Particle Mesh Ewald summation. $^{40,41}$ Bond lengths and angles of the wa ter molecules were constrained using the SHAKE algorithm $^{42}$ and clay platelets were kept frozen and rigid at each specific

![](./images/813144599680778241_4.jpg)

FIG. 1. (a) Part of the typical simulation setup for studying edge-to-edge interaction (red, O; white, H; yellow, Si; grey, Al; cyan, Mg; blue, Na). (b) Detail of the edge [0 10] structure. Si tetrahedra end with an SiOH bond (top and bottom). Al octahedra end with AlOH inside the clay platelet and $AlOH_{2}$ on the broken edge. (c) Part of the typical simulation setup for studying face-to-face interaction.

separation distance. The following summarizes the simulation details for edge-to-edge and face-to-face interactions.

### Edge-to-edge
Two identical clay platelets were placed at center-to-center separations ranging from $\text{r}_i = 39.75$–$61.25$ Å with an increment of $0.25$ Å. Figure 1(a) shows the typical structure of the simulated system at one of the separation distances. From now on, each separation distance is called one state, unless otherwise stated. We performed 87 separate simulations at T = 300 K in the canonical (NVT) ensemble. Each platelet consists of 4×4 unit cells with the longest dimension along y axis. Four edge sites on each side (along y) corresponding to $\begin{bmatrix}0&1&0\end{bmatrix}$ edges obtained by cutting the unit cell. Broken bonds were saturated with H or OH groups. Figure 1(b) shows the geometry of the edge sites taken from *ab initio* simulations of Churakov. $^{43,44}$ Edge corrections introduce $\text{H}_{32}\text{O}_{16}$ extra atoms on each platelet. The average length of the platelet in the y direction is $\sim 40$ Å. We assigned a partial charge equal to 0.45e for a hydrogen atom on the edge (H) to keep the system neutral. Platelets are continuous in the x direction. The two platelets were solvated in the center of a rectangular box. The solvation process was performed by stacking equilibrated boxes of SPC water molecules$^{33}$ to form a rectangular box of $20.87$ Å(x)×$140$ Å(y)×$46.56$ Å(z) containing 3882 water molecules which is constant for all states. Water molecules have been removed from the box if the distance between an atom in the water molecule and an atom in the clay structure is less than sum of their van der Waals radii. It has been shown that structure and dynamics of water molecules on the clay surface are only affected over two to three molecular layers from the surface.$^{45}$ In our simulations, the thickness of water phase on each side of the clay platelet or on each edge at the largest separation distance is about 20 Å corresponding to more than six molecular water layers (diameter of a water molecule $\sim 3$ Å). As a result, the interaction of two clay platelets (edge-to-edge or face-to-face) separated by water layers with 40 Å thickness is efficiently shielded to have no interaction between a platelet and its image. Moreover, the simulation box is large enough so that properties of water molecules near to the boundaries of the box approximate closely to those of bulk water. After solvation, each system was equilibrated for 0.5 ns (nano second). Free energy differences between successive states are calculated over a 2.5 ns production period. Each state, $\text{r}_i$, was perturbed in two directions: forward and reverse, $\text{r}_{i\pm1} = \text{r}_i \pm \text{dr}_i$ where $\text{dr}_i = 0.25$ Å (except for the end states which perturbed in one direction only). Following Zwanzig,$^{46}$ the free energy difference between the reference state, $\text{r}_i$, and target state, $\text{r}_{i\pm1}$, can be calculated using free energy perturbation theory:

$$
\Delta G(r_i \to r_{i\pm1}) = G(r_{i\pm1}) - G(r_i) = -\frac{1}{\beta}\ln \langle exp(-\beta\Delta U)\rangle_i ,
\tag{1}
$$

$\Delta U = U(r_{i\pm1}) - U(r_i)$ and $\beta = (k_B T)^{-1}$ where T is the temperature, $k_B$ is Boltzmann’s constant, and $U$ denotes the potential energy of the system. The brackets denote canonical ensemble average over the trajectory and subscript $i$ indicates that the average is taken in the reference state. We calculated 172 free energy differences between successive states. In order to eliminate systematic sampling bias due to exponential averaging we used simple overlap sampling (SOS) of the forward and reverse perturbation as an estimate of $\Delta G$,$^{29,47}$

$$
\Delta G(r_i \to r_{i\pm1}) = -\frac{1}{\beta}\ln \left[ \frac{\langle exp(-\beta\Delta U/2)\rangle_i}{\langle exp(\beta\Delta U/2)\rangle_{i\pm1}} \right].
\tag{2}
$$

The total potential of mean force at each separation distance $(\text{r} = \text{r}_i)$ was calculated by sequentially summing up all the free energy changes from the largest separation $(\text{r} = 61.25$ Å) to that state $(\text{r} = \text{r}_i)$ assuming zero value for the free energy of the system at the largest separation $(\text{r} = 61.25$ Å). Figure 2(a) shows the potential of the mean force for edge-to-edge interactions calculated over the range of states for selected analysis production periods. The results converge after averaging over 2.5 ns (i.e., 3 ns simulation and perturbation for each MD state). The PMF shows an oscillatory behavior with distance between energy minimums (or plateau, e.g., $\text{r}_i = 48$ Å) reflecting the size of a water molecule (a,b $\sim 3$ Å). In other words, rearrangement of the water molecules determines favorable positions of the clay platelets. As platelets come closer to each other, the system crosses energy barriers to reach to the lowest free energy at $\text{r} = 45.5$ Å. For $\text{r} < 42$ Å, repulsion dominates the interaction of platelets indicating

![](./images/813144599680778241_5.jpg)

FIG. 2. Potential of mean force for edge-to-edge interaction of clay platelets. (a) Total PMF. a,b = 3.25, 3 Å, respectively. Distance between oscillations corresponds to diameter of a water molecule ($\sim 3$ Å). (b) PMF per length, there is one main minimum ($\text{X}_1$).

<table>
<caption>Table 1: Center to center distances ($r_i$) and number of water molecules ($N_w$) located between (I) and outside (O) the two clay platelets for each state used in (NVT) simulations. The equilibrium center-to-center separation distance ($\bar{r}$) and its standard deviation ($\pm$) are reported from (NPT) simulations.</caption>
<thead>
<tr>
<th rowspan="2">State</th>
<th rowspan="2">$r_i$($\text{\AA}$)</th>
<th colspan="2">$N_w$</th>
<th rowspan="2">$\bar{r}(\pm)$($\text{\AA}$)</th>
<th rowspan="2">State</th>
<th rowspan="2">$r_i$($\text{\AA}$)</th>
<th colspan="2">$N_w$</th>
<th rowspan="2">$\bar{r}(\pm)$($\text{\AA}$)</th>
</tr>
<tr>
<th>I</th>
<th>O</th>
<th>I</th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>9.23</td>
<td>0</td>
<td>3914</td>
<td>9.32(0.03)</td>
<td>20</td>
<td>13.99</td>
<td>112</td>
<td>3802</td>
<td>14.00(0.01)</td>
</tr>
<tr>
<td>2</td>
<td>9.48</td>
<td>4</td>
<td>3910</td>
<td>9.48(0.04)</td>
<td>21</td>
<td>14.24</td>
<td>113</td>
<td>3801</td>
<td>14.04(0.11)</td>
</tr>
<tr>
<td>3</td>
<td>9.74</td>
<td>7</td>
<td>3907</td>
<td>10.01(0.10)</td>
<td>22</td>
<td>14.49</td>
<td>116</td>
<td>3798</td>
<td>14.55(0.09)</td>
</tr>
<tr>
<td>4</td>
<td>9.99</td>
<td>7</td>
<td>3907</td>
<td>10.01(0.10)</td>
<td>23</td>
<td>14.74</td>
<td>118</td>
<td>3796</td>
<td>14.59(0.09)</td>
</tr>
<tr>
<td>5</td>
<td>10.24</td>
<td>7</td>
<td>3907</td>
<td>10.01(0.10)</td>
<td>24</td>
<td>14.99</td>
<td>119</td>
<td>3795</td>
<td>15.13(0.12)</td>
</tr>
<tr>
<td>6</td>
<td>10.49</td>
<td>8</td>
<td>3906</td>
<td>10.74(0.08)</td>
<td>25</td>
<td>15.24</td>
<td>130</td>
<td>3784</td>
<td>15.27(0.09)</td>
</tr>
<tr>
<td>7</td>
<td>10.74</td>
<td>8</td>
<td>3906</td>
<td>10.74(0.08)</td>
<td>26</td>
<td>15.49</td>
<td>148</td>
<td>3766</td>
<td>15.48(0.09)</td>
</tr>
<tr>
<td>8</td>
<td>10.99</td>
<td>14</td>
<td>3900</td>
<td>10.98(0.06)</td>
<td>27</td>
<td>15.74</td>
<td>159</td>
<td>3755</td>
<td>15.65(0.09)</td>
</tr>
<tr>
<td>9</td>
<td>11.24</td>
<td>18</td>
<td>3896</td>
<td>11.11(0.07)</td>
<td>28</td>
<td>15.99</td>
<td>174</td>
<td>3740</td>
<td>16.00(0.10)</td>
</tr>
<tr>
<td>10</td>
<td>11.49</td>
<td>24</td>
<td>3890</td>
<td>11.33(0.07)</td>
<td>29</td>
<td>16.24</td>
<td>177</td>
<td>3737</td>
<td>16.08(0.01)</td>
</tr>
<tr>
<td>11</td>
<td>11.74</td>
<td>32</td>
<td>3882</td>
<td>11.71(0.06)</td>
<td>30</td>
<td>16.49</td>
<td>178</td>
<td>3736</td>
<td>16.13(0.01)</td>
</tr>
<tr>
<td>12</td>
<td>11.99</td>
<td>42</td>
<td>3872</td>
<td>11.90(0.09)</td>
<td>31</td>
<td>16.72</td>
<td>178</td>
<td>3736</td>
<td>16.13(0.01)</td>
</tr>
<tr>
<td>13</td>
<td>12.24</td>
<td>54</td>
<td>3860</td>
<td>12.19(0.06)</td>
<td>32</td>
<td>16.97</td>
<td>179</td>
<td>3735</td>
<td>17.45(0.12)</td>
</tr>
<tr>
<td>14</td>
<td>12.49</td>
<td>79</td>
<td>3835</td>
<td>12.39(0.06)</td>
<td>33</td>
<td>17.22</td>
<td>179</td>
<td>3735</td>
<td>17.45(0.12)</td>
</tr>
<tr>
<td>15</td>
<td>12.74</td>
<td>80</td>
<td>3834</td>
<td>12.84(0.12)</td>
<td>34</td>
<td>17.47</td>
<td>179</td>
<td>3735</td>
<td>17.45(0.12)</td>
</tr>
<tr>
<td>16</td>
<td>12.99</td>
<td>87</td>
<td>3827</td>
<td>13.09(0.09)</td>
<td>35</td>
<td>17.72</td>
<td>197</td>
<td>3717</td>
<td>17.70(0.10)</td>
</tr>
<tr>
<td>17</td>
<td>13.24</td>
<td>93</td>
<td>3821</td>
<td>13.29(0.09)</td>
<td>36</td>
<td>17.97</td>
<td>210</td>
<td>3704</td>
<td>17.90(0.10)</td>
</tr>
<tr>
<td>18</td>
<td>13.49</td>
<td>101</td>
<td>3813</td>
<td>13.52(0.09)</td>
<td>37</td>
<td>18.22</td>
<td>228</td>
<td>3686</td>
<td>18.20(0.10)</td>
</tr>
<tr>
<td>19</td>
<td>13.74</td>
<td>108</td>
<td>3806</td>
<td>13.80(0.11)</td>
<td>38</td>
<td>18.47</td>
<td>232</td>
<td>3682</td>
<td>18.30(0.11)</td>
</tr>
</tbody>
</table>

work needed to remove water molecules and bring platelets close together. Figure 2(b) shows PMF per unit length of the platelet which will subsequently be scaled for different platelet sizes (assuming "D" as diameter of the platelet, values of the "x" axis are modified to "new $r_i$ = old $r_i -40$ $\text{\AA}$ + D" and values of the "y" axis are multiplied by the diameter of the platelet).

Face-to-face

Two identical clay platelets were placed at center to center separations of $\text{r}_i = 9.23$–$18.47$ $\text{\AA}$ with an increment of $0.25$ $\text{\AA}$. Figure 1(c) shows the typical structure of the simulated system in one of the separation distances. Platelets are continuous in x and y directions. We performed 38 separate simulations at $T = 300$ K in the canonical (NVT) ensemble. Table I summarizes the distribution of water molecules located between the platelets (I) and those outside (O). The initial number of confined water (I) for each center-to-center separation can be adsorbed using grand canonical Monte Carlo simulation$^{48}$ or the system can be equilibrated in (NPT) ensemble after specifying the number of water molecules in between clay layers.$^{49}$ In order to create structures with different amount of water between the clay platelets, we displaced the platelets to achieve different I/O ratios. For each state, we ran a 2 ns (NPT) simulation ($P = 1$ atm, $T = 300$ K). In Table I, equilibrium center-to-center distance and its standard deviation are reported. Initial states of each (NVT) simulation were taken from trajectories of (NPT) simulations (with an increment of $0.25$ $\text{\AA}$). Each platelet consists of $4 \times 4$ unit cells with the longest dimension along y axis. In order to be consistent with edge-to-edge simulations, we used 3914 water molecules in each system (i.e., $3882+[2 \times 16]$; taking into account extra H and OH due to edge corrections). The initial dimension of the rectangular box in each (NPT) simulation was $20.87$ $\text{\AA}$(x)$\times$$36.31$ $\text{\AA}$(y)$\times$$179.62$ $\text{\AA}$(z). The average final dimensions of the system were $20.72$ $\text{\AA}$(x)$\times$$36.05$ $\text{\AA}$(y)$\times$$179.07$ $\text{\AA}$(z). From this point, each (NVT) simulation was equilibrated for 0.5 ns. Free energy difference between successive states was calculated from a 3 ns production period. Each state was perturbed in two directions to create 74 perturbed states. The energy differences between successive states are then reported using the SOS method (Eq. (2)). Total potential of mean force at each separation distance ($\text{r} = \text{r}_i$) was calculated by sequentially summing up all the free energy changes from the largest separation ($\text{r} = 18.47$ $\text{\AA}$) to the state of interest ($\text{r} = \text{r}_i$) assuming zero value for the free energy of the system at the largest separation ($\text{r} = 18.47$ $\text{\AA}$).

Free energy for face-to-face interaction of clay platelets for different lengths of MD trajectory are shown in Figure 3(a). The calculated free energy converges after averaging over 3 ns (3.5 ns MD simulation). Similar to edge-to-edge interaction, local minima of the free energy curve are separated by distances comparable to the diameter of a water molecule (a,b$\sim$ 3 $\text{\AA}$ in Figure 3(a)). This is in agreement with previous studies reporting oscillatory changes in the interaction between two surfaces with periodicity corresponding to the diameter of a water molecule.$^{50–52}$ To have particles approach each other and reach the minimum free energy around 11 $\text{\AA}$, they should overcome energy barriers at larger distances. Due to large repulsive interactions at smaller distances ($\text{r}$<$11$ $\text{\AA}$), removing more water molecules is not favorable for the system. This is an indication of the existence of some bonded water molecules which cannot be removed easily. This is consistent with the experimental measurements using infrared spectroscopy$^{53–57}$ and molecular dynamics simulation in nanoconfined hydrophilic pores.$^{58}$ Figure 3(b) shows PMF for face-to-face interactions per surface area

![](./images/813144599680778241_6.jpg)
![](./images/813144599680778241_7.jpg)

FIG. 3. Potential of mean force for face-to-face interaction of clay platelets. (a) Total PMF, a,b = 3, 3.22 Å, respectively. Distance between oscillations corresponds to diameter of a water molecule (~ 3 Å). (b) PMF per surface area, there are two comparable minima (X₁ and X₂). Width of the second energy well is wider than the first one (i.e., d > c).

which will be scaled for different platelet sizes (values of the "y" axis are multiplied by the surface area of the platelet).

Our simulations are performed in NVT ensemble to cal- culate the potential of mean force corresponding to relative Helmholtz free energy. It is well established that the cohe- sion between charged lamellae (with counter ions and solvent molecules) arises from so-called ionic correlation forces that relate to the thermal fluctuation, here associated with the dis- tribution of Na⁺ ions in the inter-lamellar void. These can be obtained by taking the z-derivative of the PMF presented in Figure 3.

The so-called primitive model was first used to estab- lish the existence of the ionic correlations forces between structure-less charged plane objects immersed in a bath of counter-ions (considered as charged hard spheres with an ef- fective diameter taken to be that of their hydration shell) in a dielectric continuum that mimics the screening ef- fects of ion-ion, ion-lamella, and lamella-lamella Coulombic interactions.⁵⁹⁻⁶² By definition, the primitive model is there- fore a meso-scale approach as it ignores any explicit atomistic texture of both the substrate and solvent molecules.

The limitation of the primitive model lies mainly in the fact that the solvent dielectric constant is considered to be that of the bulk as it ignores solvent structure close to the surface (adsorption) and in the neighborhood of ions (hydra- tion shell). The landmark of the primitive model was that one could predict that same-charged colloidal objects such as clay layers can be attracted through the ionic correlation forces akin to the dynamic distribution of ions in the inter-lamellar void, hence predicting phenomenon such as the flocculation of Ca-rich clays. The primitive model when implemented in a Monte-Carlo simulation numerical approach allows in a very straight fashion to describe ion density thermal fluctuations that are by construction completely ignored in the well-known DLVO (Derjaguin–Landau–Verwey–Overbeek) theory that is only a mean-field approach (i.e., the ion density distribution being the straight solution of the static Poisson-Boltzmann equation, we do not discuss here the fact that the only way the DLVO theory can predict cohesion is through van der Waals interactions, its Coulombic part being only able to predict re- pulsion between same charged objects immersed in an elec- trolyte). Hence the electrostatic Poisson-Boltzmann part of the DLVO theory is an exact solution of the primitive model in the limit of weak electrostatic coupling (low substrate charge, low ionic charge, high temperature, high dielectric solvent constant).

Very recently, Carrier⁶³ reconciled the molecular scale and the meso-scale of the primitive model using molecular dynamics by solving first long standing statistical physics er- godic problems for Coulombic systems. From full atomistic simulation, Carrier showed that the ionic correlation forces are indeed the origin of the cohesion between clay layers. He also showed that the solvent dielectric constant is strongly de- creased in the nanometric width on the interlayer void. He then introduced an explicit solvent primitive model that fully mimics the computationally heavy results of the full atomistic approach as presented in the current study. Carrier showed that the ionic correlation forces can be quantified from the magnitude of system's instantaneous effective ionic dipole moment obtained by dividing the interlayer void in two equiv- alent volume separated by a fictitious mid-plane and counting the number of ions in each two sub-systems over time and cal- culating the effective system's dipole moment with respect to the mid-plane. This can be done at various pressures in NPT simulations at constant water content.

We chose one of the systems (state 28) in Table I to study the effect of pressure. The dipole moment of the sodium ions is calculated using $\mu = |\sum_{i=1}^{last\ ion}(z_i - z_0).q_i|$, where $q_i = 1e$, $z_0$ is the z position of the plane in the middle of two platelets and $z_i$ is the z coordinate of the ion $i$.

Figure 4 shows fluctuation of the calculated dipole mo- ment for two different pressures on the system. The average values over the last 3 ns of trajectory (from 0.5 ns to 3.5 ns) are 1.6 and 1.4 eV nm for P= 1 atm and 800 atm, respectively. Clearly the magnitude of the interaction between these effec- tive dipole moment values does not change significantly when considering a pressurized system (compared to the unpressur- ized case).

The 12% difference in dipole moments at P = 1 and 800 atm can be understood from the fact that at higher pressure

![](./images/813144599680778241_8.jpg)

FIG. 4. Fluctuation of dipole moments of the sodium ions between clay lay- ers for state 28 (see Table I) at two pressures (P = 1 atm and P = 800 atm). Absolute dipole moment of sodium ions decreases as pressure increases.

some $\text{Na}^+$ ions which move to the mid-plane regions as shown in Figure 5 do not contribute to the effective system's dipole (that reflects the strength of the effective interaction between layers) anymore. Therefore, to a first approximation, one can consider that the layer to layer PMF calculated at 1 atm is not modified significantly for pressure changes up to 800 atm although more work is required to fully encompass the effect of temperature and pressure on the effective PMF interactions between clay platelets.

## MESO-SCALE: GAY-BERNE POTENTIAL

The meso-scale simulations are based on the Gay-Berne (GB) $^{28}$ potential as implemented $^{64}$ in LAMMPS code. $^{65}$ The GB potential is a single site potential used for interaction of two rigid, ellipsoidal particles. As we know from electron mi- croscopy, platelets of clay are approximately equidimentional in plan. $^{66}$ Moreover, analysis by atomic force microscopy shows that an ellipsoidal (oblate) geometry is a reasonable ap- proximation for describing the clay platelets. $^{67}$ Here, we treat each platelet of clay as an effective ellipsoidal GB particle. GB was originally developed for similar ellipsoidal particles and then generalized for dissimilar biaxial particles. $^{68}$ Using the notations of Everaers and Ejtehadi, $^{69}$ the GB potential can be written as

$$
U=4 \epsilon\left[\left(\frac{\sigma}{h_{12}+\sigma}\right)^{12}-\left(\frac{\sigma}{h_{12}+\sigma}\right)^{6}\right] \cdot \eta_{12} \cdot \chi_{12}. \quad (3)
$$

In the first term (which is similar to Lennard-Jones potential), $\epsilon=1$ determines the energy scale, $\sigma$ is the atomic interaction radius and function $h_{12}$ approximates anisotropic interparticle distance

$$
h_{12}=r-\sigma_{12} \quad (4)
$$

and

$$
\sigma_{12}=\left(\frac{1}{2} \hat{\mathbf{r}}_{12}^{T} \mathbf{G}_{12}^{-1} \hat{\mathbf{r}}_{12}\right)^{-1 / 2}, \quad (5)
$$

where $\mathbf{r}_{12}=\mathbf{r}_{2}-\mathbf{r}_{1}=r \hat{\mathbf{r}}_{12}$ is the center to center separation vector, r is center to center distance, $\hat{\mathbf{r}}_{12}$ is the unit vector and

$$
\mathbf{G}_{12}=\mathbf{A}_{1}^{T} \mathbf{S}_{1}^{2} \mathbf{A}_{1}+\mathbf{A}_{2}^{T} \mathbf{S}_{2}^{2} \mathbf{A}_{2}, \quad (6)
$$

where $\mathbf{S}_{\mathbf{i}}=\operatorname{diag}(a_{i}, b_{i}, c_{i})$ is shape matrix which is defined by three radii $a_{i}, b_{i}, c_{i}$. $\mathbf{A}_{i}$ represents rotation matrix which defines transformation of each particle from the local to global frame of reference. The second term characterizes anisotropic interactions of particles due to their shapes

$$
\eta_{12}=\left[\frac{2 s_{1} s_{2}}{\operatorname{det}(\mathbf{G}_{12})}\right]^{1 / 2} \quad (7)
$$

and

$$
s_{i}=\left[a_{i} b_{i}+c_{i} c_{i}\right]\left[a_{i} b_{i}\right]^{1 / 2}. \quad (8)
$$

The third term characterizes anisotropic interaction of parti- cles based on relative free energy well depths of edge-to-edge and face-to-face interactions

$$
\chi_{12}=\left(2 \hat{\mathbf{r}}_{12}^{T} \mathbf{B}_{12}^{-1} \hat{\mathbf{r}}_{12}\right)^{2} \quad (9)
$$

with

$$
\mathbf{B}_{12}=\mathbf{A}_{1}^{T} \mathbf{E}_{1} \mathbf{A}_{1}+\mathbf{A}_{2}^{T} \mathbf{E}_{2} \mathbf{A}_{2}, \quad (10)
$$

where $\mathbf{E}_{\mathbf{i}}=\operatorname{diag}(\epsilon_{i a}, \epsilon_{i b}, \epsilon_{i c})$ is the energy matrix which is de fined by relative well depths of edge-to-edge and face-to-face interactions. In summary, in order to define interactions be- tween two disc-like platelets (same x and y dimensions), we need to specify five parameters: $\mathbf{x}=\{a(b), c, \sigma, \epsilon_{a}(\epsilon_{b}), \epsilon_{c}\}$, two shape parameters $a(=b), c$ (with length dimension), one interaction distance parameter $\sigma$ (with length dimension) and two energy parameters per particle, $\epsilon_{a}(=\epsilon_{b}), \epsilon_{c}$ which are di mensionless. These parameters are adjusted by fitting Eq. (3) to edge-to-edge and face-to-face interactions of two platelets. Following Berardi et al., $^{70}$ we defined a cost function and op timized characteristic features (Figure 6) of edge-to-edge and face-to-face energy profiles to find parameters of GB poten- tial:

(1) The well depth, $P_{1}^{G B}=-\epsilon \cdot \eta_{12} \cdot \chi_{12}$.

![](./images/813144599680778241_9.jpg)

FIG. 5. Number density of sodium ions between clay layers for state 28 (see Table I) at two pressures (P = 1 atm and P = 800 atm). At higher pressure, more sodium ions come to the middle of the layers which decrease the con- tribution to their total dipole moment.

![](./images/813144599680778241_10.jpg)

FIG. 6. Fitting parameters of the GB potential.

(2) The separation distance corresponding to the well minimum, $P_{2}^{GB} = \sigma_{12} + \sigma(2^{1/6} - 1)$.
(3) The soft contact distance, $P_{3}^{GB} = \sigma_{12}$.
(4) Characteristic width of the potential energy well (at half depth),$P_{4}^{GB} = \sigma[(4 + 2\sqrt{2})^{1/6} - (4 - 2\sqrt{2})^{1/6}]$.

The following cost function was used in fitting procedure:

$$
\Omega(\mathbf{x}) = \frac{1}{4N_c} \sum_{N_c} \sum_{i=1}^{4} \left( \frac{P_{i}^{GB} - P_{i}^{CLAYFF}}{N_{i}^{f}} \right)^2. \tag{11}
$$

Superscript $CLAYFF$ denotes corresponding value from full atomistic simulation. $N_c$ is the number of arrangements (here $N_c = 2$ as we are fitting to face-to-face and edge-to-edge interactions) and $N_{i}^{f}$ is normalizing factor.

For $i = 1$, $N_{i}^{f} = P_{1}^{CLAYFF}$, well depth for face-to-face interaction. For $i = 2, 3, 4$, $N_{i}^{f} = P_{2}^{CLAYFF}$, distance of well minimum for edge-to-edge interaction.

We parametrized the GB potential for three different platelet sizes: $100$ Å, $500$ Å, and $1000$ Å. In all those the GB potential was fitted to the main (first) free energy minimum ($X_1$, Figures 2(b) and 3(b)). A second set of GB parameters was chosen for the $1000$ Å platelet by fitting to the second free energy minimum of the face-to-face interaction ($X_2$, Figure 3(b)) and the main (first) minimum of edge-to-edge interaction ($X_1$, Figure 2(b)). Figures 7(a)-7(d) show fitted GB to full atomistic simulations for D = 100, 500, and $1000$ Å (fitted to $X_1$ or $X_2$, Figure 3(b)). The GB parameters for different cases are listed in Table II. By increasing diameter of the platelet, potential wells become deeper. Moreover, difference between face-to-face and edge-to-edge interaction increases since face-to-face free energy scales with $[\text{L}]^2$ (L is length), while edge-to-edge interaction scales with [L]. This is reflected in the change of energy parameters ($\epsilon_a(\epsilon_b)$ and $\epsilon_c$ Table II).

For each case, ten different samples were prepared with initial random orientation of particles by putting 1000 platelets in a simple cubic lattice with interatomic spacing of $(r_a)$ larger than diameter of a platelet. For each sample, a NPT simulation was performed at constant temperature, T = 300 K to find the final "jamming state" configuration which is characterized by no further change in potential energy of the system. Figure 8 shows step function of applied pressure in these simulations. Table III lists details of the simulations for each size of platelet. The Nosé-Hoover thermostat $^{37,38}$ is used to control temperature and the Parrinello-Rahman $^{39}$ barostat to control pressure in the system. The pressure and temperature damping parameters were 1 ns and 0.001 ns, respectively. For each column, ten simulations were performed to sample phase space and report average properties of the final state. Initial state of each sample with P >1 was taken from the end of D = 1000 Å simulations (P = 1 atm).

## MESO-SCALE AGGREGATION

The meso-scale aggregation of clay platelets can be examined by considering snapshots of the simulation at selected timesteps using QMGA $^{71}$ molecular graphics software. Each simulation, uses a total number of 1000 equal-sized clay platelets with random orientations in a unit cell with different GB calibrations for different particle sizes and confining pressures (Table III). Geometrical and mechanical properties are averaged over ten samples for each type of simulation. A qualitative picture of the evolution of the system of particles during MD simulations for a typical sample can be seen in Figure 9. This example shows snapshots of a sample D = 1000 Å GB case (P = 1 atm and T = 300 K). Platelets are color coded based on the orientation of their normal vector with respect to the Z axis ($\phi$ angle). When platelets become clustered into aggregates, their normal vectors point in the same direction and the spectrum of colors decreases with time as the sample compresses to the fully jammed configuration (t = 1200 ns, Figure 9(c)). In this case, Figure 10(a) shows that there are no further changes in the total energy of the system for t $\geq$ 1000 ns (D = 1000 Å, P = 1 atm case). Figure 11 shows that systems with smaller platelets have larger kinetic energy compared to the total energy scale (Ke/Te). For instance, the percentage of kinetic energy to total energy decreases from 0.25% to 0.0026% as the size of the platelet increases from 100 Å to 1000 Å. In other words, temperature becomes irrelevant which is characteristic of the jamming state. In Figure 11, the transition to the jamming state can be identified from the sudden removal of the scatter in the Ke/Te function which occurs around 20 ns, 500 ns, and 1000 ns for 100 Å, 500 Å, and 1000 Å platelets, respectively. The rotational autocorrelation function of the normal vectors of platelets after jamming (not shown) becomes equal to unity (relaxation time becomes infinite) which is another indication of the jamming state.

Smaller particles need longer simulation times to reach to their final jammed state as seen in Figure 10(b) for a D = 100 Å, P = 1 atm simulation case. In this example, the final state is attained at t $\sim$ 5000 ns. Moreover, for 1000 Å platelets (Figure 10(a)) the energy decays smoothly with time,

![](./images/813144599680778241_11.jpg)

FIG. 7. Fitting GB potential to face-to-face and edge-to-edge interactions for different platelet diameters, D: (a) D = 100 Å; (b) D = 500 Å; (c) D = 1000 Å, fitted to the first well of face-to-face interaction. (d) D = 1000 Å, fitted to the second well of face-to-face interaction ("..." denotes contraction of the x scale).

<table>
<caption>TABLE II. Parameter values of the GB potential for different platelet diameters, D.</caption>
<thead>
<tr>
<th rowspan="2">D (Å)</th>
<th colspan="4">GB calibration case</th>
</tr>
<tr>
<th>100</th>
<th>500</th>
<th>1000</th>
<th>1000ª</th>
</tr>
</thead>
<tbody>
<tr>
<td>2a,2b(Å)</td>
<td>104.12</td>
<td>504.12</td>
<td>1004.12</td>
<td>1004.05</td>
</tr>
<tr>
<td>2c(Å)</td>
<td>9.62</td>
<td>9.62</td>
<td>9.62</td>
<td>12.25</td>
</tr>
<tr>
<td>σ(Å)</td>
<td>11.00</td>
<td>11.00</td>
<td>11.00</td>
<td>14.00</td>
</tr>
<tr>
<td>$\epsilon_a$, $\epsilon_b$</td>
<td>12.37</td>
<td>12.88</td>
<td>12.94</td>
<td>16.47</td>
</tr>
<tr>
<td>$\epsilon_c$</td>
<td>105.99</td>
<td>551.81</td>
<td>1108.46</td>
<td>1252.60</td>
</tr>
</tbody>
</table>

ªGB fitted to the second minimum of face-to-face interaction.

![](./images/813144599680778241_12.jpg)

FIG. 8. Step function of applied pressure, p(t), in NPT simulations.

while for the 100 Å platelets (Figure 10(b)) the changes are stepwise. This is an evidence of passing into a glassy regime, where stepwise reduction of energy is indicative of crossing of barriers on the rugged free energy surface. Larger platelets are stuck in a single well, unable to cross any barriers.

### Geometrical analysis

Following Chen *et al.,*⁷² we used two criteria to deter- mine whether two platelets are stacked on top of each other. Figure 12 shows the two criteria used for the analysis of

<table>
<caption>TABLE III. Details of simulations performed in NPT (T = 300 K) ensemble for different platelet diameter, D and confining pressure, P. dt: time step, $r_a$: initial interatomic spacing, $r_c$: cutoff radius.</caption>
<thead>
<tr>
<th>D (Å)</th>
<th>100</th>
<th>500</th>
<th>1000</th>
<th>1000ª</th>
<th>1000</th>
<th>1000</th>
<th>1000</th>
<th>1000</th>
</tr>
</thead>
<tbody>
<tr>
<td>P (atm)</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>10</td>
<td>50</td>
<td>300</td>
<td>800</td>
</tr>
<tr>
<td>dt(fs)</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
</tr>
<tr>
<td>$r_a$, $r_c$(Å)</td>
<td>120</td>
<td>520</td>
<td>1020</td>
<td>1020</td>
<td>1020</td>
<td>1020</td>
<td>1020</td>
<td>1020</td>
</tr>
<tr>
<td>p₀(atm)</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>p₁(atm)</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>10</td>
<td>50</td>
<td>300</td>
<td>800</td>
</tr>
<tr>
<td>t₁(ns)</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>40</td>
<td>120</td>
<td>120</td>
<td>120</td>
<td>120</td>
</tr>
<tr>
<td>t_f(ns)</td>
<td>5000</td>
<td>1200</td>
<td>1200</td>
<td>1200</td>
<td>360</td>
<td>320</td>
<td>240</td>
<td>200</td>
</tr>
</tbody>
</table>

ªGB fitted to the second minimum of face-to-face interaction.

![](./images/813144599680778241_13.jpg)

FIG. 9. Snapshots showing aggregation of $D = 1000$ Å ($P = 1$ atm) simulation at: (a) $t = 40$ ns; (b) $t = 200$ ns; (c) $t = 1200$ ns. The particles orientations are color coded according to the $\phi$ angle, orientation of their normal vector with respect to the $Z$ axis (colorbar A).

![](./images/813144599680778241_14.jpg)

FIG. 10. Total energy of the system of platelets for typical samples from simulations (see Table III): (a) $D = 1000$ Å ($P = 1$ atm); (b) $D = 100$ Å ($P = 1$ atm). System with smaller platelets can travel between energy minima and its stepwise reduction in potential energy is a sign of passing into glassy regime.

platelets stacking. Two platelets are assumed to belong to the same clay aggregate (stack) if:

(a) their interlayer distance, r, is less than an upper limit, $r_u$. The current analysis assumes that $r_u$ is 25% larger than the equilibrium distance for face-to-face interactions to allow for offsetting of platelets. For GB calibration cases fitted to the first face-to-face minimum, $r_u = 13.75$ Å; while $r_u = 17.5$ Å for $D = 1000$ Å case which was fitted to the second face-to-face minimum.

(b) the absolute value of scalar product of the two normal vectors of the platelets is greater than 0.95 ($n_1.n_2 > 0.95$).

Figures 13 and 14 illustrate probability distribution of aggregate stack sizes averaged over ten simulations and fitted to log-normal distribution functions for GB cases with $P = 1$ atm and $P > 1$ atm, respectively. Log-normal distribution of stack sizes was reported in X-ray diffraction (XRD) and transmission electron microscopy (TEM) of Na-smectite.⁷³ In each case the goodness of fit is assessed using the chi-squared $\chi^2$ test (see Table IV), at $\chi^2_{0.05} = 0.05$ significance level. The histograms of stack sizes were grouped into $\text{n}_{\text{bins}} = 10$–14

![](./images/813144599680778241_15.jpg)

FIG. 11. Kinetic energy over total energy ($K_e/T_e$) decreases as platelet size increases, i.e., temperature becomes irrelevant. Sudden removal of scatter in $K_e/T_e$ is an indication of final (jamming) state of the system which occurs around 20 ns, 500 ns, and 1000 ns for 100 Å, 500 Å, and 1000 Å platelets, respectively.

![](./images/813144599680778241_16.jpg)

FIG. 12. Criteria used for analysis of aggregation. (a) Distance criterion; (b) orientation criterion. Both distance and orientation criteria should be satisfied in order to assign two platelets to one aggregate.

centered on integer number of stacks. The last bins in the right tail of the distribution were merged together until the count in the extreme bin is at least 5. Degrees of freedom of the test, dof = n_bins-3 to take into account the two estimated parameters of the test, $(\mu,\sigma)$, i.e., (mean, standard deviation) of the log-normal distribution. In all cases $\chi^{2}<\chi_{0.05}^{2}$ which confirms that the log-normal distribution is able to represent the distribution of stack sizes at $\alpha=0.05$ significance level. The average stack size (n) increases from 3.05 to 5.01 for platelets with size increasing from $D=100\ \mathring{A}$, $P=1$ atm to $D=1000$ $\mathring{A}$, $P=1$ atm (Table IV). This is in agreement with small angle X-ray scattering (SAXS) experiments of Segad et al. $^{74}$ who reported an increase in size of aggregates with increase in the platelet size for Ca-montmorillonite. As the surface area of a platelet increases the number of platelets subtended in its solid angle also increases. This means that each platelet would interact with many more other platelets. Moreover, since the interaction energy scales with the surface area, the attraction force between platelets increases which results in larger stack sizes. Increasing pressure from 1 atm to 10 atm (see Table IV) has similar effect with the average size of the aggregates increasing from 5.01 to 7.07. Figures 15 and 16 show typical equilibrated systems of platelets for samples with $P=1$ atm and $P>1$ atm, respectively. The effect of increase in pressure can be seen by comparing Figures 15(c) and 16(a) $(D=1000$ $\mathring{A}$, $P=1$ atm vs $P=10$ atm). However, fitting GB to the first or second potential energy well for face-to-face interaction, has no effect on the size of the aggregates $(D=1000\ \mathring{A}$, $P$ = 1 atm). By increasing pressure to 50 atm, average stack size increases to 8.33. Further increase in pressure results in decrease of the stack size (from 8.33 to 6.68 and 4.46 as pressure increases from 50 atm to 300 atm and 800 atm, respectively). This is due to the sliding of the platelets (more than $r_{u}$).

![](./images/813144599680778241_17.jpg)

FIG. 13. Probability distributions and fitted log-normal distributions to the stack size analysis for different types of simulations (P = 1 atm): (a) $D=100\ \mathring{A}$; (b) $D=500\ \mathring{A}$; (c) $D=1000\ \mathring{A}$; (d) $D=1000\ \mathring{A}$, fitted to the second minimum of face-to-face interaction.

![](./images/813144599680778241_18.jpg)

FIG. 14. Probability distributions and fitted log-normal distributions to the stack size analysis for different types of simulations (D = 1000 Å and P >1 atm, see Table III): (a) P = 10 atm; (b) P = 50 atm; (c) P = 300 atm; (d) P = 800 atm. By increasing pressure, distribution is skewed more to the left, i.e., number of isolated platelets increases or stack size decreases.

We can see sliding of platelets from Figures 16(a) to 16(d). The same effect is reflected in the stack size distributions in Figure 14. By increasing pressure, the distribution is skewed more to the left and the number of isolated platelets increases. As a result, the average number of platelets per stack decreases. Using transmission electron microscopy, scanning electron microscopy, SAXS, and X-ray diffraction experiments⁷³,⁷⁵⁻⁷⁸ on different types of Na-smectites have found that particles typically comprise three to ten layers of platelets, consistent with the current numerical simulations.

In order to study the degree of orientation of particles, we use a scalar measure of the orientation as an order parameter⁷⁹

$$
S = \left\langle\frac{3\cos^{2}\theta - 1}{2}\right\rangle, \tag{12}
$$

where $\theta$ is the angle of normal vector of a platelet $(\mathbf{u})$ with director of the system $(\mathbf{n})$. The brackets denote average over all the particles. The director vector of a system of particles, $(\mathbf{n})$, is a measure of the average orientation of the particles in the system. Director is the eigenvector corresponding to

<table>
<thead>
<tr>
<th colspan="8">TABLE IV. Results of geometrical analysis of aggregates for different platelet diameter, D and confining pressure, P.</th>
</tr>
</thead>
<tbody>
<tr>
<td>D (Å)</td>
<td>100</td>
<td>500</td>
<td>1000</td>
<td>1000ᵃ</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
</tr>
<tr>
<td>P (atm)</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>10</td>
<td>50</td>
<td>300</td>
<td>800</td>
</tr>
<tr>
<td>n₍bins₎</td>
<td>10</td>
<td>10</td>
<td>13</td>
<td>13</td>
<td>13</td>
<td>14</td>
<td>14</td>
<td>13</td>
</tr>
<tr>
<td>dof</td>
<td>7</td>
<td>7</td>
<td>10</td>
<td>10</td>
<td>10</td>
<td>11</td>
<td>11</td>
<td>10</td>
</tr>
<tr>
<td>$\chi^{2}$</td>
<td>4.16</td>
<td>4.16</td>
<td>8.33</td>
<td>8.13</td>
<td>2.86</td>
<td>7.90</td>
<td>17.07</td>
<td>11.90</td>
</tr>
<tr>
<td>$\chi_{0.05}^{2}$</td>
<td>14.06</td>
<td>14.06</td>
<td>18.30</td>
<td>18.30</td>
<td>18.30</td>
<td>19.67</td>
<td>19.67</td>
<td>18.30</td>
</tr>
<tr>
<td>$(\mu,\sigma)$</td>
<td>(0.94,0.59)</td>
<td>(1.01,0.62)</td>
<td>(1.38,0.68)</td>
<td>(1.38,0.68)</td>
<td>(1.69,0.73)</td>
<td>(1.80,0.80)</td>
<td>(1.26,1.13)</td>
<td>(0.89,1.10)</td>
</tr>
<tr>
<td>n</td>
<td>3.05</td>
<td>3.33</td>
<td>5.01</td>
<td>5.01</td>
<td>7.07</td>
<td>8.33</td>
<td>6.68</td>
<td>4.46</td>
</tr>
<tr>
<td>S</td>
<td>0.11 ± 0.03</td>
<td>0.10 ± 0.04</td>
<td>0.23 ± 0.08</td>
<td>0.21 ± 0.05</td>
<td>0.46 ± 0.12</td>
<td>0.65 ± 0.10</td>
<td>0.65 ± 0.13</td>
<td>0.67 ± 0.17</td>
</tr>
<tr>
<td colspan="9">ᵃGB fitted to the second minimum of face-to-face interaction.</td>
</tr>
</tbody>
</table>

![](./images/813144599680778241_19.jpg)

FIG. 15. Equilibrated system from different types of simulations (P = 1 atm, see Table III): (a) D = 100 Å; (b) D = 500 Å; (c) D = 1000 Å; (d) D = 1000 Å, GB fitted to the second minimum of face-to-face interaction. The particles orientations are color coded according to the $\phi$ angle, orientation of their normal vector with respect to the Z axis (colorbar A).

![](./images/813144599680778241_20.jpg)

FIG. 16. Equilibrated system from different types of simulations (D = 1000 Å, P > 1 atm, see Table III): (a) P = 10 atm; (b) P = 50 atm; (c) P = 300 atm; (d) P = 800 atm. By increasing pressure, platelets start to slide against each other. The particles orientations are color coded according to the $\phi$ angle, orientation of their normal vector with respect to the Z axis (colorbar A).

biggest absolute eigenvalue of the order tensor, $q_{ij}$,

$$
q_{ij} = \frac{1}{N} \sum_{m=1}^N \left(u_i u_j - \frac{1}{3} \delta_{ij}\right), \tag{13}
$$

where $N$ is the number of particles and $\delta_{ij}$ is the Kronecker delta function. For completely isotropic and randomly oriented system $S=0$, while perfectly aligned systems have $S=1$. Results of the calculated order parameter are listed in Table IV. As the size of the platelets increases from $100\ \mathring{\text{A}}$ to $500\ \mathring{\text{A}}$ there is little change in the order parameter of the particles (from 0.11 to 0.10 for $\text{D}=100\ \mathring{\text{A}}$ ($\text{P}=1$ atm) and $\text{D}=500\ \mathring{\text{A}}$ ($\text{P}=1$ atm), respectively). Similarly, fitting to the first or second potential energy well of the face-to-face interaction has little effect on $S$ (from 0.23 to 0.21 for $\text{D}=1000\ \mathring{\text{A}}$). However, there is a more pronounced change in $S$ for $\text{D}=1000\ \mathring{\text{A}}$ ($\text{P}=1$ atm) simulations vs $\text{D}=100$ and $500\ \mathring{\text{A}}$ ($\text{P}=1$ atm) cases (0.23/0.21 vs 0.10/0.11). In other words, as size of the platelets decreases the system becomes more isotropic since smaller particles have more freedom to move around due to their sizes. This is in agreement with experiments done by Hetzel $et\ al.^{78}$ who showed that lateral extension of particles decreases disorder in the geometrical arrangements of particles and the system becomes more anisotropic. Increasing the confining pressure has a significant effect on ordering of particles reflected in an increase in the order parameter from $S=0.23$ to $0.46$ for $\text{P}=1$ to 10 atm ($\text{D}=1000\ \mathring{\text{A}}$) then to $0.65$ for $\text{P}=50$ atm. More increase in pressure has small effect on the order parameter. The effect of pressure can be seen by comparing Figures 15(c) and 16. In summary, as pressure increases system becomes more ordered and the number of platelets per stack increases until reaching to the maximum ordered state (here at $\text{P}=50$ atm where we have $S=0.65$). More increase of the pressure decreases the average stack size due to sliding of platelets at fixed orientation (constant $S$) which means much smaller deviations in particle orientations at high confining pressure such that platelets can cross energy barriers, and as a result, become more aligned. Increasing pressure results in increasing concentration of particles due to decrease in volume. This result is in agreement with isotropic (orientationally disordered) to nematic (orientationally ordered) phase transition for nonspherical charged objects known as the Onsager transition. $^{80}$ According to Onsager theory at low concentration the system of particles is isotropic and orientational entropy of particles are maximum. As the density of particles increases, nonspherical objects start to align to maximize the free volume in which they can move leading to the nematic phase.

## Calculation of elastic properties of meso-scale aggregate assemblies

We have used quasi-static algorithm to construct stress-strain behaviors and interpret elastic stiffness properties of the particle assemblies with $500\ \mathring{\text{A}}$ and $1000\ \mathring{\text{A}}$ platelets. This algorithm consists of two steps: (1) application of a small homogeneous strain to the system (2) relaxing strain step over a relaxation time period using a NVT ensemble ($\text{T}=0.01$ K). The procedure was used previously to build stress-strain curves for gold crystal structure. $^{81}$ We applied six different strains on the system and computed stress components. The elastic constants are determined from Hooke's law

$$
\sigma_{ij} = \sum_{k,l} C_{ijkl} \epsilon_{kl}, \tag{14}
$$

where $C_{ijkl}$ represents fourth order elasticity tensor and $\epsilon_{kl}$ is the $kl$ element of the second order strain tensor. We use the Voigt notation in representing components of the $C_{ijkl}$ with indices: $11 \to 1$, $22 \to 2$, $33 \to 3$, $23 \to 4$, $13 \to 5$, and $12 \to 6$. In this notation, fourth order elasticity tensor can be represented by a symmetrical matrix with components $C_{ij}$. In the Cartesian coordinate indices 1, 2, and 3 map to x, y, and z, respectively. The internal stress tensor of the system are given by $^{82}$

$$
\sigma_{ij} = \frac{1}{V} \sum_{\alpha} \left(m^{\alpha} v_i^{\alpha} v_j^{\alpha} + \sum_{\beta} f_i^{\alpha \beta} r_j^{\alpha \beta}\right), \tag{15}
$$

where $V$ is the volume of the system, $m^{\alpha}$ and $v^{\alpha}$ are mass and velocity of platelet $\alpha$, respectively. $f_i^{\alpha \beta}$ is the force acting on platelet $\alpha$ by platelet $\beta$ in the $i$ direction and $r_j^{\alpha \beta}$ is the Cartesian component of the vector from platelet $\beta$ to platelet $\alpha$ in the $j$ direction. Compressive and shear strain steps applied using a (NVT) ensemble ($\text{T}=0.01$ K). Each strain step was relaxed over a relaxation time period. The stress values were averaged over the last $10\%$ of the relaxation time. Simulation details for calculation of elastic properties are summarized in Table V. Elastic constants were obtained from a linear fit over the initial part of the stress strain curve representing values from $\epsilon=0\%$ to $0.01\%$ for $500\ \mathring{\text{A}}$ platelets and $\epsilon=0\%$-$0.03\%$ for $1000\ \mathring{\text{A}}$ platelets. Figure 17 shows typical stress-strain curves used to calculate elasticity for a sample comprised of $500\ \mathring{\text{A}}$ platelets. Values of elastic properties are averaged over ten samples for each type of simulation (i.e., each GB calibration case). Table VI summarizes the mean and standard deviation of the elastic constants.

It can be seen that diagonal terms can be approximated with two parameters: $\overline{C}_{11}=1/3(C_{11}+C_{22}+C_{33})$ and $\overline{C}_{44}=1/3(C_{44}+C_{55}+C_{66})$. For instance, in the case of $500\ \mathring{\text{A}}$ the normal stiffness values are 0.51, 0.50, and 0.52 GPa ($\sim$0.51 GPa) and shear stiffness values are 0.1, 0.1, and 0.09 GPa ($\sim$0.1 GPa). In the off diagonal terms, $C_{12}$, $C_{13}$, and $C_{23}$ are close together and one order of magnitude larger than the rest of the off diagonal terms. For example, in the case of $500\ \mathring{\text{A}}$ the values of these terms are 0.12, 0.14, and 0.12 GPa

<table>
<caption>TABLE V. Details of simulations to calculate elastic properties. dt: time step, d$\epsilon$: strain step, $\text{n}_s$: number of steps, $\text{t}_r$ and $\text{t}_s$: relaxation time and sampling period for each strain step, D: diameter of the platelet.</caption>
<thead>
  <tr>
    <th>D ($\mathring{\text{A}}$)</th>
    <th>500</th>
    <th>1000</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>dt(fs)</td>
    <td>5</td>
    <td>5</td>
  </tr>
  <tr>
    <td>d$\epsilon$</td>
    <td>$2.5 \times 10^{-5}$</td>
    <td>$5 \times 10^{-5}$</td>
  </tr>
  <tr>
    <td>$\text{n}_s$</td>
    <td>25</td>
    <td>50</td>
  </tr>
  <tr>
    <td>$\text{t}_r$(ps)</td>
    <td>800</td>
    <td>100</td>
  </tr>
  <tr>
    <td>$\text{t}_s$(ps)</td>
    <td>80</td>
    <td>10</td>
  </tr>
</tbody>
</table>

![](./images/813144599680778241_21.jpg)

FIG. 17. Stress-strain curves for a typical sample of 500 Å platelets. By applying strain in the z direction, $\epsilon_{33}$, associated column in the stiffness matrix can be determined. (a) $\sigma_{ii}$-$\epsilon_{33}$ curves. m = 1,2,3. (b) $\sigma_{ij}$-$\epsilon_{33}$ curves. m = 4,5,6.

($\sim$0.13 GPa), respectively, and the absolute values of the remaining off-diagonal terms are between 0.00 and 0.03 GPa. This suggests that the particle assemblies approximate cubic symmetry of the full elasticity tensor with three independent elastic constants: $C_{11}$, $C_{12}$, and $C_{44}$. Table VII summarizes the cubic average of the elastic properties calculated via simple averaging over the three directions, [100], [010], and [001]: $\overline{C}_{11}$, $\overline{C}_{44}$, and $\overline{C}_{12}=1/3(C_{12}+C_{13}+C_{23})$. By increasing the size of the platelets, $\overline{C}_{11}$ increases from 0.51 GPa to 0.98 GPa. The increase in compressive stiffness is expected for larger platelets as the cohesion between the platelets increases due to the larger surface area. The value of $\overline{C}_{12}$ is related to the lateral Poisson's ratio connecting deformation between orthogonal axes. There is a negligible change in this elastic constant (from 0.13 to 0.14 GPa). Similarly the shear stiffness, $\overline{C}_{44}$, has a small change with changing size of the platelet (from 0.10 to 0.08 GPa). For a system equilibrated at larger pressures (D = 1000 Å cases), all elastic constants increase as expected. Comparing D = 1000 Å, P = 1 atm fitted to the first or second minimum of face-to-face interaction shows decrease in all stiffness values for the case we have larger face-to-face distance at equilibrium condition. Shear stiffness decreases by 38% (from 0.08 to 0.05 GPa), normal stiffness decreases by 23% (from 0.98 to 0.75 GPa) and the stiffness related to Poisson's effect, $\overline{C}_{12}$, decreases by 21% (from 0.14 to 0.11 GPa). This change can be explained by difference in

TABLE VI. Elastic constant properties (in GPa) calculated for D = 500 Å and D = 1000 Å platelets at different confining pressure, P. $\langle.\rangle$ symbol denotes average of the property (bold face).

<table>
  <thead>
    <tr>
      <th>D (Å)</th>
      <th colspan="2">500</th>
      <th colspan="2">1000</th>
      <th colspan="2">1000ª</th>
      <th colspan="2">1000</th>
      <th colspan="2">1000</th>
      <th colspan="2">1000</th>
      <th colspan="2">1000</th>
    </tr>
    <tr>
      <th>P (atm)</th>
      <th colspan="2">1</th>
      <th colspan="2">1</th>
      <th colspan="2">1</th>
      <th colspan="2">10</th>
      <th colspan="2">50</th>
      <th colspan="2">300</th>
      <th colspan="2">800</th>
    </tr>
    <tr>
      <th></th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
      <th>$\langle.\rangle$</th>
      <th>$\pm$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$C_{11}$</td>
      <td>0.51</td>
      <td>0.05</td>
      <td>0.96</td>
      <td>0.19</td>
      <td>0.76</td>
      <td>0.22</td>
      <td>3.58</td>
      <td>0.95</td>
      <td>5.69</td>
      <td>1.58</td>
      <td>12.89</td>
      <td>5.51</td>
      <td>26.00</td>
      <td>13.30</td>
    </tr>
    <tr>
      <td>$C_{22}$</td>
      <td>0.50</td>
      <td>0.06</td>
      <td>1.07</td>
      <td>0.39</td>
      <td>0.74</td>
      <td>0.17</td>
      <td>4.02</td>
      <td>1.15</td>
      <td>7.42</td>
      <td>3.33</td>
      <td>15.37</td>
      <td>6.06</td>
      <td>33.47</td>
      <td>15.57</td>
    </tr>
    <tr>
      <td>$C_{33}$</td>
      <td>0.52</td>
      <td>0.08</td>
      <td>0.92</td>
      <td>0.13</td>
      <td>0.75</td>
      <td>0.18</td>
      <td>4.59</td>
      <td>2.37</td>
      <td>6.15</td>
      <td>1.93</td>
      <td>14.24</td>
      <td>5.19</td>
      <td>28.02</td>
      <td>11.90</td>
    </tr>
    <tr>
      <td>$C_{44}$</td>
      <td>0.10</td>
      <td>0.05</td>
      <td>0.09</td>
      <td>0.06</td>
      <td>0.05</td>
      <td>0.03</td>
      <td>0.42</td>
      <td>0.29</td>
      <td>0.75</td>
      <td>0.42</td>
      <td>2.06</td>
      <td>1.26</td>
      <td>5.22</td>
      <td>2.85</td>
    </tr>
    <tr>
      <td>$C_{55}$</td>
      <td>0.10</td>
      <td>0.03</td>
      <td>0.07</td>
      <td>0.03</td>
      <td>0.06</td>
      <td>0.03</td>
      <td>0.46</td>
      <td>0.28</td>
      <td>0.54</td>
      <td>0.31</td>
      <td>1.53</td>
      <td>0.94</td>
      <td>4.20</td>
      <td>2.72</td>
    </tr>
    <tr>
      <td>$C_{66}$</td>
      <td>0.09</td>
      <td>0.02</td>
      <td>0.09</td>
      <td>0.05</td>
      <td>0.05</td>
      <td>0.03</td>
      <td>0.43</td>
      <td>0.12</td>
      <td>0.70</td>
      <td>0.58</td>
      <td>2.13</td>
      <td>1.48</td>
      <td>4.62</td>
      <td>2.14</td>
    </tr>
    <tr>
      <td>$C_{12}$</td>
      <td>0.12</td>
      <td>0.02</td>
      <td>0.14</td>
      <td>0.07</td>
      <td>0.11</td>
      <td>0.07</td>
      <td>0.49</td>
      <td>0.45</td>
      <td>1.36</td>
      <td>0.72</td>
      <td>4.24</td>
      <td>1.45</td>
      <td>8.60</td>
      <td>2.54</td>
    </tr>
    <tr>
      <td>$C_{13}$</td>
      <td>0.14</td>
      <td>0.03</td>
      <td>0.13</td>
      <td>0.06</td>
      <td>0.11</td>
      <td>0.04</td>
      <td>0.57</td>
      <td>0.61</td>
      <td>0.97</td>
      <td>0.56</td>
      <td>3.75</td>
      <td>1.02</td>
      <td>8.46</td>
      <td>2.81</td>
    </tr>
    <tr>
      <td>$C_{14}$</td>
      <td>$-0.01$</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>$-0.02$</td>
      <td>0.18</td>
      <td>$-0.03$</td>
      <td>0.25</td>
      <td>0.20</td>
      <td>0.47</td>
      <td>$-0.49$</td>
      <td>1.32</td>
    </tr>
    <tr>
      <td>$C_{15}$</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.09</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.18</td>
      <td>0.62</td>
      <td>0.43</td>
      <td>0.57</td>
      <td>$-0.01$</td>
      <td>1.73</td>
      <td>$-0.18$</td>
      <td>4.21</td>
    </tr>
    <tr>
      <td>$C_{16}$</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.06</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>$-0.15$</td>
      <td>0.61</td>
      <td>0.19</td>
      <td>0.32</td>
      <td>0.99</td>
      <td>1.07</td>
      <td>1.30</td>
      <td>1.99</td>
    </tr>
    <tr>
      <td>$C_{23}$</td>
      <td>0.12</td>
      <td>0.03</td>
      <td>0.16</td>
      <td>0.09</td>
      <td>0.11</td>
      <td>0.04</td>
      <td>0.54</td>
      <td>0.42</td>
      <td>1.41</td>
      <td>0.60</td>
      <td>4.37</td>
      <td>1.49</td>
      <td>9.33</td>
      <td>2.97</td>
    </tr>
    <tr>
      <td>$C_{24}$</td>
      <td>$-0.03$</td>
      <td>0.03</td>
      <td>0.02</td>
      <td>0.05</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.33</td>
      <td>0.31</td>
      <td>0.20</td>
      <td>0.23</td>
      <td>0.00</td>
      <td>0.82</td>
      <td>0.18</td>
      <td>3.71</td>
    </tr>
    <tr>
      <td>$C_{25}$</td>
      <td>$-0.02$</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>$-0.03$</td>
      <td>0.10</td>
      <td>0.05</td>
      <td>0.42</td>
      <td>$-0.13$</td>
      <td>1.08</td>
      <td>0.09</td>
      <td>2.78</td>
    </tr>
    <tr>
      <td>$C_{26}$</td>
      <td>$-0.01$</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>0.03</td>
      <td>0.03</td>
      <td>0.14</td>
      <td>0.64</td>
      <td>0.26</td>
      <td>0.46</td>
      <td>0.81</td>
      <td>1.31</td>
      <td>1.53</td>
      <td>2.23</td>
    </tr>
    <tr>
      <td>$C_{34}$</td>
      <td>$-0.02$</td>
      <td>0.03</td>
      <td>0.02</td>
      <td>0.07</td>
      <td>0.02</td>
      <td>0.02</td>
      <td>$-0.15$</td>
      <td>0.77</td>
      <td>0.02</td>
      <td>0.57</td>
      <td>0.29</td>
      <td>0.92</td>
      <td>$-0.33$</td>
      <td>4.45</td>
    </tr>
    <tr>
      <td>$C_{35}$</td>
      <td>$-0.02$</td>
      <td>0.03</td>
      <td>0.01</td>
      <td>0.11</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.11</td>
      <td>0.72</td>
      <td>0.05</td>
      <td>1.19</td>
      <td>$-0.12$</td>
      <td>1.83</td>
      <td>0.89</td>
      <td>5.18</td>
    </tr>
    <tr>
      <td>$C_{36}$</td>
      <td>$-0.01$</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.00</td>
      <td>0.10</td>
      <td>0.26</td>
      <td>0.29</td>
      <td>0.39</td>
      <td>0.31</td>
      <td>0.54</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>$C_{45}$</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.00</td>
      <td>0.23</td>
      <td>0.11</td>
      <td>0.24</td>
      <td>0.26</td>
      <td>0.42</td>
      <td>0.30</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>$C_{46}$</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>$-0.01$</td>
      <td>0.08</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>$-0.01$</td>
      <td>0.30</td>
      <td>0.26</td>
      <td>0.78</td>
      <td>$-0.05$</td>
      <td>0.43</td>
      <td>0.25</td>
      <td>0.78</td>
    </tr>
    <tr>
      <td>$C_{56}$</td>
      <td>$-0.01$</td>
      <td>0.02</td>
      <td>$-0.01$</td>
      <td>0.03</td>
      <td>$-0.01$</td>
      <td>0.02</td>
      <td>$-0.04$</td>
      <td>0.12</td>
      <td>$-0.12$</td>
      <td>0.21</td>
      <td>0.00</td>
      <td>0.47</td>
      <td>$-0.62$</td>
      <td>1.51</td>
    </tr>
  </tbody>
</table>

ªGB fitted to the second minimum of face-to-face interaction.

<table><caption>TABLE VII. Cubic averaged elastic properties (in GPa) and Euclidean distance between averaged and full elasticity tensors for different platelet diameter, D and confining pressure, p.</caption>
<tbody>
<tr>
<td>D (Å)</td>
<td>500</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000ª</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
</tr>
<tr>
<td>P (atm)</td>
<td>1</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td></td>
<td>10</td>
<td></td>
<td>50</td>
<td></td>
<td>300</td>
<td></td>
<td>800</td>
</tr>
<tr>
<td>$\overline{C}_{11}$</td>
<td>0.51</td>
<td></td>
<td>0.98</td>
<td></td>
<td>0.75</td>
<td></td>
<td>4.07</td>
<td></td>
<td>6.42</td>
<td></td>
<td>14.17</td>
<td></td>
<td>29.16</td>
</tr>
<tr>
<td>$\overline{C}_{12}$</td>
<td>0.13</td>
<td></td>
<td>0.14</td>
<td></td>
<td>0.11</td>
<td></td>
<td>0.53</td>
<td></td>
<td>1.24</td>
<td></td>
<td>4.12</td>
<td></td>
<td>8.80</td>
</tr>
<tr>
<td>$\overline{C}_{44}$</td>
<td>0.10</td>
<td></td>
<td>0.08</td>
<td></td>
<td>0.05</td>
<td></td>
<td>0.44</td>
<td></td>
<td>0.66</td>
<td></td>
<td>1.91</td>
<td></td>
<td>4.68</td>
</tr>
<tr>
<td>$\frac{d_{E}(C_{ij},\overline{C}_{ij})}{\| \overline{C}_{ij} \|}$</td>
<td>0.18 ± 0.05</td>
<td></td>
<td>0.22 ± 0.08</td>
<td></td>
<td>0.17 ± 0.07</td>
<td></td>
<td>0.43 ± 0.11</td>
<td></td>
<td>0.38 ± 0.12</td>
<td></td>
<td>0.42 ± 0.12</td>
<td></td>
<td>0.47 ± 0.10</td>
</tr>
</tbody>
</table>

ªGB fitted to the second minimum of face-to-face interaction.

the width of the second energy well compared to the first (Figure 3(b)). As c < d the second derivative of the energy with respect to strain (i.e., elastic properties) are larger for GB calibrated to the first potential well.

The accuracy of the cubic-averaged elastic constants $(\overline{C}_{ij})$ in representing the full elastic stiffness matrix was evaluated using Euclidean distance metric. This metric has been used previously to assess similarity between full elastic constant matrix and averaged symmetric one.⁸³ The Euclidean distance between two square matrices, ${\mathbf{A}}_{\mathbf{1}}$ and ${\mathbf{A}}_{\mathbf{2}}$, is calculated as follows:

$$
d_{E}(\mathbf{A}_{1}, \mathbf{A}_{2}) = \|\mathbf{A}_{1} - \mathbf{A}_{2}\|_{E} \tag{16}
$$

and the associated norm is defined by

$$
\|\mathbf{A}\|_{E} = \sqrt{tr(\mathbf{A}^{\mathbf{T}}\mathbf{A})}, \tag{17}
$$

where $tr(\cdot)$ stands for the trace and the superscript T denotes the transpose. Smaller values of the metric mean more similarity between matrices. Smaller values of this metric indicate better approximation of the full elastic matrix using cubic-averaged values. In other words, when there is no preferred direction in the microstructure, elastic constant values over three directions become close together and can be well approximated using cubic symmetry assumptions. For each sample, the dimensionless Euclidean distance metric (divided by norm of the cubic averaged elastic matrix) was calculated. By averaging over ten samples, the mean and standard deviation of the metrics are reported in Table VII. By increasing platelet size, distance metric increases from 0.18 to 0.22. By applying confining pressure up to 10 atm, we see a more pronounced increase to 0.43. Increasing pressure to 50 atm shows decrease in distance metric to 0.38 and metric starts to increase again as pressure increases (to 0.42 and 0.47 for P = 300 atm and 800 atm, respectively). In general distance metric increases with pressure with an exception at P = 50 atm. The exception occurs at the onset of the maximum ordering (i.e., at P = 50 atm, S = 0.65). More increase of the pressure slides platelets against each other leading to more anisotropic system (compare Figures 16(a) and 16(b) with 16(c) and 16(d)). This is consistent with the change of microstructure. Figure 16 shows that there is less variation in particle orientation at higher pressure and hence, greater discrepancy from cubic symmetry approximation. Moreover, a decrease in the order parameter S with decreasing platelet size (Table IV) indicates more randomness in orientation distribution for smaller platelets. This leads to better approximation of the elasticity matrix with cubic symmetry. Mechanical properties at the meso-scale should be validated against experimental data.

Nanoindentation is a submicrometer experiment used to measure material stiffness parameters. So far, we scaled up our simulations to submicron length scale, the scale accessible by indentation tests. We compared our meso-scale mechanical properties with the nanoindentation experiments performed by Bobko and Ulm⁸⁴ on a range of shale and clay materials. The current simulations clearly do not represent the formation conditions of the shale and clay specimens but provide a first order comparison based on micro-porosity. The largest dimension of clay platelet used in simulation was 1000 Å which is at least ten times smaller than size of nanoplatelets found in shale. We believe that the microstructure from the current mesoscale simulations is similar to random oriented clay platelets which form phyllosilicate framework (PF) pores in shale at submicron length scale.⁸⁵,⁸⁶ They are the most abundant pores in shales formed by framework of platy phyllosilicates. As will be shown, resulted microstructure can capture overall response of shale nanoindentation results. To compare our results, we calculated values of indentation modulus from elasticity components $(C_{ij})$ using the derivation by Delafargue and Ulm⁸⁷ for an orthotropic solid (see the

<table><caption>TABLE VIII. Average packing density and indentation modulus (in GPa) for different platelet diameter, D and confining pressure, p. $\langle . \rangle$ symbol denotes average of the property (bold face).</caption>
<tbody>
<tr>
<td>D (Å)</td>
<td>500</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000ª</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
<td></td>
<td>1000</td>
</tr>
<tr>
<td>P (atm)</td>
<td>1</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td></td>
<td>10</td>
<td></td>
<td>50</td>
<td></td>
<td>300</td>
<td></td>
<td>800</td>
</tr>
<tr>
<td></td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
<td>$\langle . \rangle$</td>
<td>±</td>
</tr>
<tr>
<td>$\eta$</td>
<td>0.23</td>
<td>0.02</td>
<td>0.21</td>
<td>0.02</td>
<td>0.20</td>
<td>0.02</td>
<td>0.43</td>
<td>0.07</td>
<td>0.63</td>
<td>0.04</td>
<td>0.77</td>
<td>0.04</td>
<td>0.87</td>
<td>0.03</td>
</tr>
<tr>
<td>$\overline{M}_{1}$</td>
<td>0.37</td>
<td>0.03</td>
<td>0.50</td>
<td>0.11</td>
<td>0.36</td>
<td>0.15</td>
<td>2.16</td>
<td>0.61</td>
<td>2.97</td>
<td>0.83</td>
<td>7.66</td>
<td>3.02</td>
<td>16.75</td>
<td>7.32</td>
</tr>
<tr>
<td>$\overline{M}_{2}$</td>
<td>0.36</td>
<td>0.04</td>
<td>0.55</td>
<td>0.24</td>
<td>0.35</td>
<td>0.09</td>
<td>2.22</td>
<td>0.82</td>
<td>3.82</td>
<td>1.82</td>
<td>8.99</td>
<td>3.26</td>
<td>20.50</td>
<td>7.97</td>
</tr>
<tr>
<td>$\overline{M}_{3}$</td>
<td>0.38</td>
<td>0.07</td>
<td>0.48</td>
<td>0.13</td>
<td>0.36</td>
<td>0.10</td>
<td>2.40</td>
<td>1.29</td>
<td>3.32</td>
<td>1.15</td>
<td>8.08</td>
<td>2.41</td>
<td>17.57</td>
<td>6.28</td>
</tr>
<tr>
<td>$\overline{M}$</td>
<td>0.37</td>
<td>0.05</td>
<td>0.51</td>
<td>0.17</td>
<td>0.36</td>
<td>0.11</td>
<td>2.26</td>
<td>0.92</td>
<td>3.37</td>
<td>1.33</td>
<td>8.24</td>
<td>2.87</td>
<td>18.27</td>
<td>7.16</td>
</tr>
</tbody>
</table>

ªGB fitted to the second minimum of face-to-face interaction.

![](./images/813144599680778241_22.jpg)

FIG. 18. Indentation modulus versus clay packing density, $\eta$. Shale has parallel layering of platelets in the microscale. The experimental data in the normal ($x_3$ direction) and parallel ($x_1(x_2)$ directions) to the layering are taken from Bobko and Ulm.⁸⁴

Appendix). Each value of packing density (one minus porosity) at the final state is calculated using 11 Å as the thickness of a platelet which corresponds to the minimum favorable face-to-face distance (Figure 3). Table VIII summarizes average packing density and indentation modulus for different types of simulations. In our upscaled model, values of indentation modulus show no preferential direction (almost identical) which is consistent with cubic symmetry assumption for the elasticity tensor. The mean indentation modulus is used to compare with experiment. Figure 18 shows indentation modulus versus packing density from experiment and simulations. Three simulation points (associated with P = 1 atm) lie on the left side of the graph (around packing density of 0.2) which correspond to a colloidal clay system. The other indentation values from simulations of confined clay (P > 1 atm) show a good agreement with simulation and the change follows the trend of the experiment.

## CONCLUSIONS

Meso-scale aggregates of clay were studied using Gay-Berne potential calibrated from full atomistic simulations. The free energy of face-to-face and edge-to-edge interactions of clay platelets were calculated as the elementary configurations for calibration. Minima of the free energy are separated with $\sim 3$ Å distance which corresponds to the diameter of a water molecule. The meso-scale simulations show that structural and mechanical properties of the aggregates are related to the clay platelet size and external applied pressure. Simulations for Wyoming Na-montmorillonite have shown that aggregate size distributions are well described by log-normal functions with mean stack size that increases from 3 to 8 platelets per aggregate. Smaller platelets have less order (more isotropic) structures while confining pressure generates more ordered structures (more anisotropic).

The microstructure of the system of particles plays an important role in their mechanical properties. We found that larger aggregates produce more anisotropic structure with higher compressive and shear stiffness due to higher attraction between larger platelets. These features become more pronounced by increasing external pressure on the system until reaching to the maximum ordered state. More increase of the pressure, reduces aggregate size due to sliding of platelets against each other, whereas mechanical properties are still increasing. While the size of the aggregates remains constant by their formation in the second energy minimum of face-to-face interaction, the mechanical properties of the microstructure decreases due to wider width of the second energy well.

## ACKNOWLEDGMENTS

The computational resources used for this project have been provided by the National Science Foundation through the Extreme Science and Engineering Discovery Environment (XSEDE) and the Texas Advanced Computing Center under Grant No. TG-DMR100028. The first author wishes to acknowledge the X-Shale Hub at MIT and the Singapore-MIT Alliance for Research and Technology (SMART) for partial support of this project. The authors gratefully acknowledge Professor M. J. Buehler at MIT for useful discussions on the geometrical analysis of clay aggregates. We would also like to acknowledge advice and suggestion given by Professor G. C. Rutledge at MIT. We wish to thank M. J. Abdolhosseini Qomi and M. Pourmand for the fruitful discussions.

## APPENDIX: INDENTATION MODULUS OF AN ORTHOTROPIC SOLID

The equations relating elastic constants ($C_{ij}$) to indentation modulus ($M_1$, $M_2$, $M_3$) for an orthotropic solid are summarized in this Appendix:⁸⁷

$$
\begin{aligned}
M_{1} & \approx \sqrt{M_{12} M_{13}}, \\
M_{2} & \approx \sqrt{M_{21} M_{23}}, \\
M_{3} & \approx \sqrt{M_{31} M_{32}},
\end{aligned} \tag{A1}
$$

where

$$
\begin{aligned}
M_{21} & =2 \sqrt{\frac{C_{11} C_{22}-C_{12}^{2}}{C_{11}}\left(\frac{1}{C_{66}}+\frac{2}{C_{11} C_{22}+C_{12}}\right)^{-1}}, \\
M_{31} & =2 \sqrt{\frac{C_{11} C_{33}-C_{13}^{2}}{C_{11}}\left(\frac{1}{C_{55}}+\frac{2}{C_{11} C_{33}+C_{13}}\right)^{-1}}, \\
M_{32} & =2 \sqrt{\frac{C_{22} C_{33}-C_{23}^{2}}{C_{22}}\left(\frac{1}{C_{44}}+\frac{2}{C_{22} C_{33}+C_{23}}\right)^{-1}},
\end{aligned} \tag{A2}
$$

and

$$
\begin{aligned}
M_{12} & =M_{21} \sqrt{\frac{C_{11}}{C_{22}}}, \\
M_{13} & =M_{31} \sqrt{\frac{C_{11}}{C_{33}}}, \\
M_{23} & =M_{32} \sqrt{\frac{C_{22}}{C_{33}}}.
\end{aligned} \tag{A3}
$$

$^{1}$A. Meunier, Clay Miner. 41, 551 (2006).

$^{2}$H. H. Murray, Appl. Clay Sci. 17, 207 (2000).

$^{3}$S. Goldberg and R. A. Glaubig, Clays Clay Min. 35, 220 (1987).

$^{4}$E. Tombácz, C. Csanaky, and E. Illés, Colloid Polym. Sci. 279, 484 (2001).

$^{5}$G. Lagaly and S. Ziesmer, Adv. Colloid Interface Sci. 100-102, 105 (2003).

$^{6}$E. Tombácz, T. Nyilas, Z. Libor, and C. Csanaki, From Colloids to Nanotechnology (Springer, 2004), pp. 206-215.

$^{7}$L. J. Michot, I. Bihannic, K. Porsch, S. Maddi, C. Baravian, J. Mougel, and P. Levitz, Langmuir 20, 10829 (2004).

$^{8}$L. J. Michot, I. Bihannic, S. Maddi, S. S. Funari, C. Baravian, P. Levitz, and P. Davidson, Proc. Natl. Acad. Sci. 103, 16101 (2006).

$^{9}$S. García-García, S. Wold, and M. Jonsson, J. Colloid Interface Sci. 315, 512 (2007).

$^{10}$L. J. Michot, I. Bihannic, S. Maddi, C. Baravian, P. Levitz, and P. Davidson, Langmuir 24, 3127 (2008).

$^{11}$D. Zhou, A. I. Abdel-Fattah, and A. A. Keller, Environ. Sci. Technol. 46, 7520 (2012).

$^{12}$L. J. Michot, I. Bihannic, F. Thomas, B. S. Lartiges, Y. Waldvogel, C. Caillet, J. Thieme, S. S. Funari, and P. Levitz, Langmuir 29, 3500 (2013).

$^{13}$B. Carrier, L. Wang, M. Vandamme, R. J.-M. Pellenq, M. Bornert, A. Tanguy, and H. Van Damme, Langmuir 29, 12823 (2013).

$^{14}$A. C. D. Newman, Chemistry of Clays and Clay Minerals, Mineralogical Society monograph (Longman Scientific and Technical, 1987).

$^{15}$D. Ebrahimi, R. J.-M. Pellenq, and A. J. Whittle, Langmuir 28, 16855 (2012).

$^{16}$P. Porion, M. A. Mukhtar, A. Faugere, R. J.-M. Pellenq, S. Meyer, and A. Delville, J. Phys. Chem. B 107, 4012 (2003).

$^{17}$M. Dijkstra, J. P. Hansen, and P. A. Madden, Phys. Rev. Lett. 75, 2236 (1995).

$^{18}$M. Dijkstra, J. P. Hansen, and P. A. Madden, Phys. Rev. E 55, 3044 (1997).

$^{19}$A. Mourchid, A. Delville, J. Lambard, E. Lecolier, and P. Levitz, Langmuir 11, 1942 (1995).

$^{20}$S. Kutter, J. P. Hansen, M. Sprik, and E. Boek, J. Chem. Phys. 112, 311 (2000).

$^{21}$S. Meyer, P. Levitz, and A. Delville, J. Phys. Chem. B 105, 9595 (2001).

$^{22}$G. Odriozola, M. Romero-Bastida, and F. D. J. Guevara-Rodriguez, Phys. Rev. E 70, 021405 (2004).

$^{23}$S. Mossa, C. De Michele, and F. Sciortino, J. Chem. Phys. 126, 014905 (2007).

$^{24}$B. Jönsson, C. Labbez, and B. Cabane, Langmuir 24, 11406 (2008).

$^{25}$M. Jardat, J. F. Dufrêche, V. Marry, B. Rotenberg, and P. Turq, Phys. Chem. Chem. Phys. 11, 2023 (2009).

$^{26}$A. Thuresson, M. Ullner, T. Åkesson, C. Labbez, and B. Jonsson, Langmuir 29, 9216 (2013).

$^{27}$N. Choudhury and B. M. Pettitt, J. Am. Chem. Soc. 127, 3556 (2005).

$^{28}$J. G. Gay and B. J. Berne, J. Chem. Phys. 74, 3316 (1981).

$^{29}$C. Chipot and A. Pohorille, Free Energy Calculations (Springer, 2007).

$^{30}$R. T. Cygan, J. J. Liang, and A. G. Kalinichev, J. Phys. Chem. B 108, 1255 (2004).

$^{31}$X. Liu, X. Lu, R. Wang, H. Zhou, and S. Xu, Clays Clay Miner. 55, 554 (2007).

$^{32}$J. L. Suter, P. V. Coveney, H. C. Greenwell, and M. A. Thyveetil, J. Phys. Chem. C 111, 8248 (2007).

$^{33}$H. J. C. Berendsen, J. R. Grigera, and T. P. Straatsma, J. Phys. Chem. 91, 6269 (1987).

$^{34}$D. Van Der Spoel, E. Lindahl, B. Hess, G. Groenhof, A. E. Mark, and H. J. C. Berendsen, J. Comput. Chem. 26, 1701 (2005).

$^{35}$W. Humphrey, A. Dalke, and K. Schulten, J. Mol. Graph. 14, 33 (1996).

$^{36}$K. Refson, S. H. Park, and G. Sposito, J. Phys. Chem. B 107, 13376 (2003).

$^{37}$S. Nosé, J. Chem. Phys. 81, 511 (1984).

$^{38}$W. G. Hoover, Phys. Rev. A 31, 1695 (1985).

$^{39}$M. Parrinello and A. Rahman, J. Appl. Phys. 52, 7182 (1981).

$^{40}$T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089 (1993).

$^{41}$U. Essmann, L. Perera, M. Berkowitz, T. Darden, H. Lee, and L. G. Pedersen, J. Chem. Phys. 103, 8577 (1995).

$^{42}$J. P. Ryckaert, G. Ciccotti, and H. J. C. Berendsen, J. Comput. Phys. 23, 327 (1977).

$^{43}$S. V. Churakov, J. Phys. Chem. B 110, 4135 (2006).

$^{44}$S. V. Churakov, Geochim. Cosmochim. Acta 71, 1130 (2007).

$^{45}$V. Marry, B. Rotenberg, and P. Turq, Phys. Chem. Chem. Phys. 10, 4802 (2008).

$^{46}$R. W. Zwanzig, J. Chem. Phys. 22, 1420 (1954).

$^{47}$C. Y. Lee and H. L. Scott, J. Chem. Phys. 73, 4591 (1980).

$^{48}$T. J. Tambach, E. J. M. Hensen, and B. Smit, J. Phys. Chem. B 108, 7586 (2004).

$^{49}$E. S. Boek, P. V. Coveney, and N. T. Skipper, Langmuir 11, 4629 (1995).

$^{50}$J. N. Israelachvili and R. M. Pashley, Nature (London) 306, 249 (1983).

$^{51}$R. M. Pashley and J. N. Israelachvili, J. Colloid Interface Sci. 101, 511 (1984).

$^{52}$M. Autognozzi, A. D. L. Humphris, and M. J. Miles, Appl. Phys. Lett. 78, 300 (2001).

$^{53}$J. J. Fripiat, J. Chaussidon, and R. Touillaux, J. Phys. Chem. 64, 1234 (1960).

$^{54}$J. D. Russell and V. C. Farmer, Clay Miner. Bull. 5, 443 (1964).

$^{55}$V. M. Malhotra and A. A. Ogloza, Phys. Chem. Miner. 16, 386 (1989).

$^{56}$C. T. Johnston, G. Sposito, and C. Erickson, Clays Clay Miner. 40, 722 (1992).

$^{57}$W. Xu, C. T. Johnston, P. Parker, and S. F. Agnew, Clays Clay Miner. 48, 120 (2000).

$^{58}$M. J. A. Qomi, M. Bauchy, F.-J. Ulm, and R. J.-M. Pellenq, J. Chem. Phys. 140, 054515 (2014).

$^{59}$B. Jonsson, P. G. Nilsson, B. Lindman, L. Guldbrand, and H. Wennentrom, in Surfactants in Solution, edited by K. L. Mittal and B. Lindman (Plenum Press, New York, 1984), Vol. 1, p. 3.

$^{60}$J. P. Valleau, R. Ivkov, and G. M. Torrie, J. Chem. Phys. 95, 520 (1991).

$^{61}$R. J.-M. Pellenq, J. M. Caillol, and A. Delville, J. Phys. Chem. B 101, 8584 (1997).

$^{62}$A. Delville, R. J.-M. Pellenq, and J. M. Caillol, J. Chem. Phys. 106, 7275 (1997).

$^{63}$B. Carrier, “Influence of water on the short term and long term mechanical properties of swelling clays: Experiments on self supporting films and molecular simulations,” Ph.D. thesis (ENPC, Paris, 2013).

$^{64}$W. M. Brown, M. K. Petersen, S. J. Plimpton, and G. S. Grest, J. Chem. Phys. 130, 044901 (2009).

$^{65}$S. Plimpton, J. Comput. Phys. 117, 1 (1995).

$^{66}$G. Brown, A. C. D. Newman, J. H. Rayner, and A. H. Weir, The Chemistry of Soil Constituents (Wiley, 1978), p. 29.

$^{67}$A. Cadene, S. Durand-Vidal, P. Turq, and J. Brendle, J. Colloid Interface Sci. 285, 719 (2005).

$^{68}$R. Berardi, C. Fava, and C. Zannoni, Chem. Phys. Lett. 236, 462 (1995).

$^{69}$R. Everaers and M. R. Ejtehadi, Phys. Rev. E 67, 041710 (2003).

$^{70}$R. Berardi, C. Fava, and C. Zannoni, Chem. Phys. Lett. 297, 8 (1998).

$^{71}$A. T. Gabriel, T. Meyer, and G. Germano, J. Chem. Theory Comput. 4, 468 (2008).

$^{72}$C. T. Chen, V. Ball, J. J. de Almeida Gracio, M. K. Singh, V. Toniazzo, D. Ruch, and M. J. Buehler, ACS Nano 7, 1524 (2013).

$^{73}$K. Mystkowski, J. Środoń, and F. Elsass, Clay Miner. 35, 545 (2000).

$^{74}$M. Segad, B. Jönsson, and B. Cabane, J. Phys. Chem. C 116, 25425 (2012).

$^{75}$D. Tessier and G. Pedro, in Proceedings of the International Clay Conference, Bologna and Pavia, Italy (Elsevier Scientific Publ. Co., Amsterdam, 1981), pp. 6-12.

$^{76}$C. H. Pons, D. Tessier, H. B. Rhaiem, D. Tchoubar, H. Van Olphen, and F. Veniale, in Proceedings of the International Clay Conference, Bologna and Pavia, Italy (Elsevier Scientific Publ. Co., Amsterdam, 1981), pp. 177-185.

$^{77}$B. Rhaiem, C. H. Pons, and D. Testier, in Proceedings of the International Clay Conference, 1985, Denver (Clay Minerals Society, 1987).

$^{78}$F. Hetzel, D. Tessier, A. M. Jaunet, and H. Doner, Clays Clay Miner. 42, 242 (1994).

$^{79}$J. Prost, The Physics of Liquid Crystals (Oxford University Press, 1995), Vol. 83.

$^{80}$L. Onsager, Ann. N. Y. Acad. Sci. 51, 627 (1949).

$^{81}$A. Aghaei, M. J. Abdolhosseini Qomi, M. T. Kazemi, and A. R. Khoei, Int. J. Solids Struct. 46, 1925 (2009).

$^{82}$V. Vitek and T. Egami, Phys. Status Solidi B 144, 145 (1987).

$^{83}$R. Shahsavari, R. J.-M. Pellenq, and F. J. Ulm, Phys. Chem. Chem. Phys. 13, 1002 (2011).

$^{84}$C. Bobko and F. J. Ulm, Mech. Mater. 40, 318 (2008).

$^{85}$J. Schieber, in Proceedings of the SPE Unconventional Gas Conference (Society of Petroleum Engineers, 2010).

$^{86}$M. E. Curtis, R. J. Ambrose, D. Energy, C. H. Sondergeld, and C. S. Rai, in Canadian Unconventional Resources and International Petroleum Conference (Society of Petroleum Engineers, 2010).

$^{87}$A. Delafargue and F. J. Ulm, Int. J. Solids Struct. 41, 7351 (2004).