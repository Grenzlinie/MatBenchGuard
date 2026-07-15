# Evolution of Physical, Thermal, and Mechanical Properties of Poly(methyl Methacrylate)-Based Elium Thermoplastic Polymer During Polymerization
Swapnil S. Bamane, Prathamesh P. Deshpande, Sagar U. Patil, Marianna Maiaru, and Gregory M. Odegard*

Cite This: J. Phys. Chem. C 2024, 128, 15639−15648

---

## ABSTRACT:
Elium-based thermoplastic composites are a key material for future use in the marine, wind energy, and automotive industries because of their recyclability and ease of manufacture. To optimize the processing of the Elium composites to yield optimal structural properties, computational process modeling can be used to relate processing parameters to residual stresses and material durability. The key ingredient for reliable and accurate process modeling is the evolution of physical, thermal, and mechanical properties during polymerization. The objective of this study is to use molecular dynamics to predict the mass density, bulk modulus, shear modulus, Young's modulus, Poisson's ratio, glass transition temperature, and coefficient of thermal expansion as a function of the extent of reaction of the polymer. The predicted properties compare favorably to the experimentally measured values in the fully polymerized state. This data set of properties provides needed input data for process modeling of Elium-based composites for process parameter optimization and improved durability and performance.

![](./images/1046644905620799491_1.jpg)

## 1. INTRODUCTION
Thermoplastic polymer matrix composites (TPMCs) are commonly used in the marine, energy, and automotive industries because of their excellent fracture toughness, fatigue resistance, impact strength, recyclability, and ease of joint welding. Specifically, Elium-based TPMCs have shown much promise because of these characteristics and because of their unique ability to polymerize during composite processing, similar to thermoset resins. $^{1−11}$ Low-viscosity Elium resins can be easily infused into composite molds and subsequently polymerized, providing the benefits of thermoset processing while simultaneously providing the advantages of TPMCs. These resins are a next-generation alternative for wind turbine blades due to their recyclability relative to state-of-the-art thermosets. $^{12−15}$ However, like thermosets, in situ polymerization of Elium during composite processing is accompanied by chemical shrinkage, which can result in residual stress formation that is detrimental to the laminate strength. $^{16−18}$

Computational, multiscale process modeling is a key tool for optimizing processing parameters (annealing temperatures, hold times, ramp rates) to yield composite structures with minimal residual stresses. $^{19−21}$ One critical ingredient of accurate processing modeling is a set of resin properties (physical, thermal, and mechanical) as a function of polymerization. Although these properties can be obtained experimentally, a much more efficient and cost-effective approach is through molecular dynamics (MD) simulation. MD simulation has been used to determine the properties of a wide range of thermoset resins during curing $^{19,21−26}$ and thermoplastics during crystallization. $^{27,28}$ However, the properties of Elium and the closely related poly(methyl methacrylate) (PMMA) have not been determined as a function of polymerization. Therefore, to enable process modeling and optimization of processing parameters for Elium-based composites, a comprehensive set of resin properties must be determined as a function of polymerization.

The objective of this study is to develop MD models to simulate the polymerization process of Elium thermoplastic resin and predict the thermo-mechanical properties as a function of polymerization. Specifically, the coefficient of thermal expansion (CTE), glass transition temperature ($T_g$), mass density, volumetric shrinkage, bulk modulus, shear

---

Received: June 18, 2024
Revised: August 26, 2024
Accepted: August 29, 2024
Published: September 10, 2024

![](./images/1046644905620799491_2.jpg)

© 2024 The Authors. Published by American Chemical Society
15639
https://doi.org/10.1021/acs.jpcc.4c04061
J. Phys. Chem. C 2024, 128, 15639−15648

modulus, Young's modulus, Poisson's ratio, and tensile strength are predicted at the molecular level. The prediction of these properties is necessary for the design and optimization of the next generation of recyclable and easily manufacturable composites.

## 2. METHODS
### 2.1. Material.
Elium resin is manufactured by Arkema and based on methyl methacrylate (MMA) and acrylic copolymers. $^{5,11}$ Although the chemistry of the acrylic copolymers and their exact concentration is proprietary, the polymerization process is primarily based on the free radical polymerization observed in MMA. $^{6}$ Therefore, to predict the thermo mechanical properties of this system as a function of polymerization, a mixture of MMA monomers and dimers with a stoichiometric ratio of 1:1 was modeled. Figure 1 shows the molecular structures of the MMA monomer and dimer. In this study, the predicted properties are compared with experimentally measured values for Elium and PMMA resins from the literature.

![](./images/1046644905620799491_3.jpg)

Figure 1. Molecular structure of (a) MMA monomer with a molecular weight of 100.12 g/mol and (b) MMA dimer with a molecular weight of 200.24 g/mol. The average molecular weight of the mixture of these two is 150.18 g/mol.

The Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) $^{29}$ software package was used to perform the MD simulations in this study. Simulation boxes with periodic boundaries in the x-, y-, and z-directions were used in all simulations discussed in this work. The Reactive Interface Forcefield (IFF-R) $^{30,31}$ was used to describe the interatomic and intermolecular interactions of the Elium resin. IFF-R is an all-atom forced field that utilizes Morse bonds to simulate the nonlinear response of stretched covalent bonds. IFF-R has previously been used to predict the thermo-mechanical and interfacial properties of thermosets such as epoxy, polybenzox- azine, and BMI. $^{19,21-26,32-36}$ In addition, IFF-R has also been used to model thermoplastics such as PEEK, cyanate esters, and polyamides. $^{28,33,35,37-40}$ These previous studies show that IFF-R is a reliable forcefield for predicting the thermo- mechanical properties of polymer materials. For all of the MD simulations performed in this study, the pairwise interactions were calculated using the Lenard Jones 12/6 equation. Both short-range and long-range Coulombic interactions were simulated with the "lj/class2/coul/long" LAMMPS command with a global cutoff distance of $10$ Å.

### 2.2. MD Models.
The monomers and dimers were initially created individually and relaxed by using the CHEM3D (PerkinElmer, INC., MA, USA) software package. These monomer and dimer structures were then imported into the LAMMPS environment (Figure 2a). The monomer and dimer molecules were replicated using the "replicate" command to create a bulk system of 15,435 atoms which included 343 MMA monomers and 343 MMA dimers with an initial mass density of 0.15 g/cc (Figure 2b). The number of atoms was determined based on the study performed by Kashmari et al. $^{41}$ on the effect of MD model size on the precision of predicted material properties.

![](./images/1046644905620799491_4.jpg)

Figure 2. Molecular modeling workflow to create the polymerized models. Colors in the polymerized system represent the cluster analysis of the model. The atomic clusters in the model are color- coded by chain length.

After the low-density bulk system was created, a minimization step was performed using the "minimize" command with a conjugate gradient solver. The model was then densified using the "fix deform" command to the target density of 1.01 g/cc (Figure 2c) at a densification rate of 0.22 g/cc/ns in the NVT (constant volume and temperature) ensemble at 300 K. The densification step was followed by an annealing cycle where the temperature was ramped up from 300 to 500 K in the NPT (constant pressure and temperature) ensemble, followed by a temperature hold simulation using the NPT ensemble at 500 K temperature for 500 ps. For annealing, a temperature of 500 K was selected based on previous MD studies performed by Odegard et al. $^{22}$ that showed the stabilization of MD models after annealing at temperatures of 500 K and above. The model was subsequently cooled to 300 K at a cooling rate of 50 K/ns. This annealing cycle was simulated to equilibrate the models and relax the monomers to eliminate any residual stresses in the model after the densification step. The annealing cycle was followed by a relaxation simulation at 300 K using the NPT ensemble for 500 ps to relax the energies and conformations formed during the annealing cycle. For the densification, annealing, and relaxation simulations, the time step was set to 1 fs. This process was repeated to create five replicate models with unique initial velocities assigned to the atoms by using the "velocity" command. Previous studies have shown that the five replicate MD models accurately and efficiently predict the material properties of neat polymers. $^{22,28,41}$

### 2.3. Polymerization.
The polymerization process was simulated using the "fix bond/react" command in LAMMPS. $^{42}$ To implement the "fix bond/react" protocol for simulating the reaction, the topological conditions before and after the reaction between the atoms involved in the reaction were specified. This was performed by creating prereaction templates, postreaction templates, and mapping files of the

![](./images/1046644905620799491_5.jpg)

Figure 3. Polymer reaction possibilities with a mixture of MMA monomers and dimers.

![](./images/1046644905620799491_6.jpg)

Figure 4. Evolution of oligomers during polymerization including the (a) plot of percentage of atoms in the simulation box associated with the corresponding cluster as a function of extent of reaction and (b) evolution of clusters in the MD simulation box over a range of reaction levels. Error bars represent the standard error between the replicate models.

reaction sites. Detailed information on the "fix bond/react" command can be found elsewhere. $^{42,43}$

Elium undergoes a free radical polymerization reaction initiated by electron donor pairs associated with oxygen or nitrogen atoms $^{6}$ in initiator molecules. However, because the

initiator molecules are in very low concentrations (1.5–3 wt. %), it was assumed that their presence has a negligible effect on the properties, and thus they were not modeled directly in this study. Three reaction possibilities are shown in Figure 3 for an initial mixture of reacting MMA monomers and dimers. Dimer/dimer and dimer/monomer reactions result in a polymer chain that can continue to react with monomers, dimers, and other polymer chains. Detailed information on the template files used to simulate these reactions is provided in the Supporting Information (SI).

Polymerization was simulated while heating the simulation box from 300 to 800 K at a heating rate of 62.5 K/ns with a time step of 0.1 fs. This heating cycle was simulated to increase the mobility of the monomers to accelerate the polymerization. Reaction site stabilization was performed every 5000 timesteps using the "fix nve/limit" command in LAMMPS. Further, all nonreacting atoms during the polymerization simulation were controlled by the NVT thermostat. The polymerization was quantified by the extent of the reaction by calculating the number of functional bonds that reacted during polymer- ization. The extent of reaction at any given time $t$ is the number of reactive functional groups that have reacted divided by the number of reactive functional groups initially present.

The output data files of the polymerized structures were created at the extent of reaction intervals of 0.1 (i.e., 0.1, 0.2, 0.3, etc.). The simulations were run until the maximum polymerization level (i.e., 0.915 extent of reaction) was achieved with an average simulation time of 8 ns. This approach minimized the simulation time necessary for the complete polymerization. The polymerization step was then followed by a simulation at 300 K in the NPT ensemble with the "iso" pressure settings (for which simulation box sizes are controlled isometrically) for 500 ps to cool the models to room temperature with timesteps of 1 fs.

All polymerized models were subjected to high-temperature annealing simulations. The temperature was ramped up to 500 K using the NPT ensemble, and the models were subsequently cooled to 300 K at a cooling rate of 50 K/ns. This annealing step was performed to eliminate any residual stresses or unfavorable conformations in the simulation box during polymerization by allowing the model to expand at higher temperatures and cool at a controlled rate. Annealing simulations have previously been used in MD modeling studies to eliminate residual stresses. $^{19,21,22,28}$ Following the annealing, equilibration simulations were performed in the NPT ensemble at 300 K for 1 ns by using "aniso" pressure settings (simulation box sizes are controlled anisometrically) for 1 ns. Both annealing and equilibration simulations were performed with timesteps of 1 fs. Local density in the simulation box is a function of the spread of polymerization in the simulation box and the local conformations observed in the MD simulation box. $^{44}$ The spatial densities of the annealed models were analyzed for the local unfavorable conformations within the simulation box. This was performed by plotting density values of a one-dimensional bin along each axis with a bin size of $5\ \text{\AA}$, as shown in Figure S7 of the SI.

Figure 4a shows a plot of the evolution of the three largest clusters in the simulation box of a representative polymer model using the cluster analysis tool in the OVITO $^{45}$ visualization software package. Each color in the image represents a cluster of atoms bonded to covalent bonds. All three oligomer chains grow as polymerization progresses. The size of the largest cluster increases significantly from an extent of reaction of 0.8 to the fully polymerized state (i.e., an extent of reaction of 0.915). Figure 4b shows the visualization of clusters of polymer oligomers as a function of polymerization. It is evident that the highest polymerization simulation box shows a smaller number of individual clusters relative to the low polymerization states, as expected. MD models show the combination of atactic, syndiotactic, and isotactic config- urations. Detailed information on the tacticity observed is provided in Section S1 of the SI. Further, detailed information about the molecular weight distributions and the chain sizes is provided in Section S1 of the SI. However, it is important to note that the molecular weights observed in MD models at the nanoscale are not expected to match the results obtained from the macroscale experiment.

2.4. Physical Properties. The mass density and volumetric shrinkage (relative to the initial unpolymerized state) were predicted for each replicate at specific levels of extent of reaction ranging from 0 to 0.915. The mass density was determined after the equilibration step, and the volumetric shrinkage was calculated by

$$
\Delta V = \frac{V_f - V_i}{V_i} \tag{1}
$$

where $V_f$ is the volume of the simulation box at specific levels of polymerization, and $V_i$ is the volume of the initial unpolymerized model.

2.5. Mechanical Properties. Odegard et al. $^{22}$ predicted the mechanical properties of epoxy systems using an MD framework as a function of cross-linking density. Similar MD procedures were implemented in this work to predict the mechanical properties. First, the bulk modulus was predicted for each replicate at each level of polymerization. These simulations were performed at 300 K with 1 fs timesteps using the NPT ensemble at 1 atm pressure for 1 ns, followed by a simulation at an increased pressure of 5000 atm for 1 ns. $^{22}$ The average volumes associated with these two pressures were determined and used to calculate bulk modulus using

$$
K = -V_0 \frac{\delta P}{\delta V} \tag{2}
$$

where $V_0$ is the average volume at equilibrium conditions, $\delta P$ is the change in pressure, and $\delta V$ is the change in volume of the simulation box.

Second, to predict shear modulus values, simulations were performed by applying a 20% shear strain in each of the three principal planes at a shear strain rate of $2 \times 10^8\ \text{s}^{-1}$. These simulations were performed at 300 K and 1 atm pressure using the NPT ensemble with a time step of 0.5 fs. For each replicate model, three shear stress−strain plots were obtained, corresponding to each principal plane. Using a Python script, the data was fit with a bilinear curve, and the corresponding breakpoint was determined. Figure S8 in the SI shows a representative shear stress-shear strain plot with the corre- sponding bilinear fit. The shear modulus was determined as the slope of the linear fit below the breakpoint. Assuming that the material is isotropic, the Young's modulus and Poisson's ratio were calculated using the following equations: $^{46}$

$$
E = \frac{9KG}{3K + G} \tag{3}
$$

$$
\nu = \frac{3K - 2G}{6K + 2G} \tag{4}
$$


![](./images/1046644905620799491_7.jpg)

Figure 5. Physical properties as a function of extent of reaction. (a) Plot of MD-predicted mass density values as a function of extent of reaction. A snapshot of a representative MD model is shown for visualization. (b) Plot of volumetric shrinkage as a function of extent of reaction. The error bars, which are partially hidden behind the data markers, represent the standard error between the replicate models. The equations of the sigmoidal curve fits of the data are shown in the plots. An exaggerated visual representation of the volumetric shrinkage of the MD simulation box is shown.

where $E$ is the Young's modulus, $K$ is the bulk modulus, $G$ is the shear modulus, and $v$ is the Poisson's ratio.

The von Mises stress was calculated from the stress components from the shear deformation simulations using

$$
\begin{aligned}
\sigma_{v M}= & \left\{\frac{1}{2}\left[\left(\sigma_{x}-\sigma_{y}\right)^{2}+\left(\sigma_{y}-\sigma_{z}\right)^{2}+\left(\sigma_{z}-\sigma_{x}\right)^{2}\right.\right. \\
& \left.\left.+6\left(\tau_{x y}{ }^{2}+\tau_{x z}{ }^{2}+\tau_{y z}{ }^{2}\right)\right]\right\}
\end{aligned}
$$

where, $\sigma_{x}, \sigma_{y}, \sigma_{z}$ are principal stresses in the $x, y$, and $z$ directions, and $\tau_{x y}, \tau_{x z}, \tau_{y z}$ are the shear stresses in the $x y, x z$, and $y z$ planes, respectively. The von Mises stress was plotted against the shear strain values, and the yield strength was computed at the corresponding bilinear breakpoint. More details on this procedure can be found elsewhere. $^{22}$ Figure S9 in the SI shows a representative plot of von Mises stress against shear strain and the bilinear fit calculated with the Python script.

2.6. Thermal Properties. The experimental measurement of $T_{g}$ is dependent on the cooling rate. ${ }^{47,48}$ Therefore, $T_{g}$ values were predicted through a simulated heating cycle for each replicate. The equilibrated models were subjected to a temperature ramp from 250 to $550 \mathrm{~K}$ at a heating rate of $50 \mathrm{~K} /$ ns in the NPT ensemble using 1 fs timesteps. The volume of the simulation box was recorded during the simulations and was plotted against the simulation temperature as shown in Figure S10 in the SI. The bilinear breakpoint was identified as the $T_{g}$ for the given model. $^{49}$ Further details on the procedure can be found elsewhere. ${ }^{22,23}$

The coefficient of thermal expansion (CTE) was calculated below and above the $T_{g}$. The slope values obtained from linear regression fits of volume versus simulation temperature plots were utilized to calculate the CTE values using

$$
\mathrm{CTE}=\frac{1}{3 V_{0}}\left(\frac{\mathrm{d} V}{\mathrm{~d} T}\right)
$$

where $V_{0}$ is the initial volume of the simulation box and $d V / d T$ is the rate of change of volume with respect to simulation temperature. More details on CTE calculations and procedures can be found elsewhere. ${ }^{22,23}$

## 3. RESULTS AND DISCUSSIONS

Figure 5a shows a plot of the mass density of Elium as a function of the extent of reaction calculated at room temperature. The mass density increases with increases in the extent of reaction because the formation of new covalent bonds results in a more compact structure. The MD-predicted mass density value of $1.172 \pm 0.001 \mathrm{~g} / \mathrm{cc}$ for the fully polymerized model is compared with the experimentally determined value of $1.183 \mathrm{~g} / \mathrm{cc}$ by Muthuraj et al., ${ }^{50}$ and the mass density of the unpolymerized resin is compared with the experimental value reported in the manufacturer's datasheet. ${ }^{51}$ Further, the mass density values of the fully polymerized models are compared with the experimental density value of PMMA of $1.18^{52}$ and $1.19 \mathrm{~g} / \mathrm{cc}^{53}$ from the literature. The MDpredicted mass density values of both polymerized and unpolymerized models agree with the experimental values of both Elium and PMMA.

Figure $5 \mathrm{~b}$ shows the volumetric shrinkage as a function of the extent of reaction predicted by MD. The volumetric shrinkage increases with increases in the extent of reaction. Significant volumetric shrinkage with increases in the extent of reaction is commonly observed in thermosets like epoxy. Previous experiments show a wide range of volumetric shrinkage for PMMA ranging from 9 to $20 \% .{ }^{54-60}$ The MDpredicted value of $13.09 \pm 0.3 \%$ is within the range of the values measured experimentally.

Figure $5 \mathrm{~b}$ also shows the wide range of experimentally reported values for cure shrinkage, ${ }^{54-60}$ which is likely a result of different molecular weights after polymerization. Figure S6

![](./images/1046644905620799491_8.jpg)
![](./images/1046644905620799491_9.jpg)

Figure 6. Moduli as a function of polymerization. (a) Plot of bulk modulus as a function of polymerization. The visualization of the bulk modulus loading conditions is shown in the inset. (b) Plot of shear modulus and Young’s modulus as a function of polymerization. Error bars represent the standard errors in the data. The equations of the sigmoidal curve fits in the data are shown in both plots.

![](./images/1046644905620799491_10.jpg)
![](./images/1046644905620799491_11.jpg)

Figure 7. (a) Plot of Poisson’s ratio as a function of extent of reaction. (b) Plot of yield strength as a function of extent of reaction. The error bars in both plots represent the standard errors in the data. The equations of sigmoidal curve fits in the data are shown in both plots.

shows a representative molecular weight distribution of the polymers in the simulation box. Because the molecular weight distributions between all the replicates were very similar, the precision in the MD-predicted cure shrinkage values is significantly higher than those reported in the literature.

The evolution of the bulk modulus as a function of the extent of reaction predicted by MD is shown in Figure 6a. The bulk modulus increases with increases in the extent of reaction with a sigmoidal trend. With increasing extent of reaction, more covalent bonds are formed in the molecular structure, resulting in increases in resistance to compressive deformation. Figure 6a also includes the experimental value of bulk modulus of 6 GPa from Mott et al.⁶¹ The fully polymerized value from MD simulation is $6.67 \pm 0.09$ GPa.

Figure 6b shows the MD-predicted evolution of the shear modulus and Young’s modulus as a function of the extent of reaction. Both moduli increase with increases in the extent of reaction in a sigmoidal trend. The shear modulus was negligible for models with an extent of reaction ranging from 0.0 to 0.3, which indicates that the material is still in the liquid phase and does not provide any resistance to the applied shear deformation. For the extent of reaction values of 0.4 and above, there is a significant increase in shear modulus that follows a sigmoidal pattern. The predicted Young’s modulus value of the fully polymerized system of $3.34 \pm 0.08$ GPa agrees with the value reported in the Elium technical data sheet (3.3 GPa)⁵¹ and the experimentally determined value of Elium 188 reported by Kazemi et al.⁶² (3.6 GPa). The Young’s modulus predictions also agree with the experimentally measured Young’s modulus value by Banks-Sills et al.⁵³ (3.1 GPa). Further, the MD-predicted shear modulus value of $1.18 \pm 0.02$ GPa compares well with the shear modulus value of PMMA of

![](./images/1046644905620799491_12.jpg)
![](./images/1046644905620799491_13.jpg)

Figure 8. Thermal properties as a function of extent of reaction. (a) Plot of $T_g$ as a function of extent of reaction and (b) plot of CTE as a function of extent of reaction. The error bars represent the standard errors in the data. The linear fit equations of the MD-predicted data are shown on both plots.

1.1 GPa from Mott et al.⁶¹ It can also be noted that the MD-predicted values in this work for shear and Young's modulus agrees with MD-predicted values of PMMA material using COMPASS force field of 1.257 and 3.184 GPa, respectively.⁶³ It is important to note that previous studies have analyzed the discrepancies with predicted elastic modulus and experimentally measured values resulting from the many order-of-magnitude differences in strain rates.¹⁹,²²,⁶⁴⁻⁶⁶ For some polymer systems, the so-called strain rate effect is significant,¹⁹,²²,⁶⁴,⁶⁵ while in other cases, it is minimal for predicted elastic modulus.²¹,²²,²⁷,²⁸ The relative magnitude of the strain-rate effect is related to the viscous nature of each individual polymer.⁶⁵ The results shown in Figure 6b indicate that this system shows a minimal strain rate effect for the elastic modulus because of the close correspondence of predicted and measured elastic modulus properties.

Figure 7a shows the response of Poisson's ratio as a function of the extent of reaction. For models with an extent of reaction of 0.4 and above, the Poisson's ratio decreases with increases in the extent of reaction. The experimentally measured values from the literature of Poisson's ratio for the Elium 188 system is 0.37⁶ and for PMMA is 0.39,⁵³ which are compared with the MD-predicted value of 0.42 for the fully polymerized system in Figure 7a. It is important to note that for an extent of reaction of 0.3 and below, the polymer is still in a liquid state and has a Poisson's ratio value (0.5) that is characteristic of many liquids.

Figure 7b shows the plot of predicted yield strength values as a function of the extent of reaction. The MD-predicted yield strength value of 245.6 ± 10 MPa for the fully polymerized system (i.e., 0.915 extent of reaction) is significantly higher than the experimental yield strength value of 76 MPa for Elium⁵¹ and 97.5 ± 12 for PMMA.⁶⁷ It has previously been shown that the yield strength of PMMA is highly dependent on the strain rate value at which the mechanical test experiments were performed.⁶⁸ It can also be noted that the MD-predicted value in this study agrees with the MD-predicted value of yield strength for neat PMMA material using a polymer consistent force field (PCFF) of 242 MPa.⁶⁹

In addition, thermosets like epoxies and polybenzoxazine have previously demonstrated significantly higher predicted values of yield strength due to their viscoelastic nature.²¹,²²,⁷⁰ Elium is a viscoelastic material. Discrepancies in the values of Young's modulus predicted by MD models and experimental values are the result of higher strain rates applied during the MD simulations. However, because of the differences between time and length scales compared to experiments, it is essential to apply such high strain rates for computational efficiency and remains a limitation of MD methods in predicting accurate yield strength for viscoelastic materials. For extents of 0.3 and below, the yield strength is negligibly small, indicating that the polymer does not have a load-carrying capacity.

Figure 8a shows the plot of $T_g$ values as a function of the extent of reaction. From Figures 6b and 7, it is clear that the polymer behaves as a liquid at extents of reaction of 0.3 and below at room temperature. Hence, the $T_g$ was calculated only for the extents of reaction ranging from 0.4 to 0.915. In this range, the $T_g$ values increase with increases in the extent of reaction. The MD-predicted value of the fully polymerized system of 116.7 ± 7 °C agrees with the experimental values of 115.6 °C by Tschentscher et al.⁴ of acetone recycled Elium and 123 °C by Raponi et al.⁷¹ of Elium measured by DMA. The MD-predicted value agrees with the experimentally measured $T_g$ values of PMMA of 108 °C by Porter et al.⁷² and 111 °C by Moller et al.⁵² The predicted value of $T_g$ using IFF-R compares with the MD-predicted value of $T_g$ for PMMA of 116 °C by Min et al.⁷³ using the Dreiding atomic potential, and 113 °C by Li et al.⁶³ using the COMPASS force field, 187 °C⁶⁹ using PCFF, and 208 °C⁷⁴ using OPLS-AA forcefield.

Figure 8b shows the plot of CTE as a function of the extent of reaction. Both CTE values above and below $T_g$ decrease with increases in the extent of reaction. The CTE values below $T_g$ are consistently lower than the CTE values above $T_g$. The MD-predicted CTE value of $6.8 \pm 0.5 \times 10^{-5}\ \mathrm{C}^{-1}$ for the fully polymerized system below $T_g$ is comparable to the experimentally measured CTE value of below $T_g$ of PMMA $9.3 \times 10^{-5}\ \mathrm{C}^{-1}$ by Han et al.⁷⁵ and the experimentally measured CTE value of $6.5 \times 10^{-5}\ \mathrm{C}^{-1}$ as reported in the Elium data sheet.⁵¹ The MD-predicted CTE values agree with the experimentally measured CTE values of PMMA and Elium.

## 4. CONCLUSIONS
Based on the MD predictions from this study, the mechanical properties of Elium evolve very quickly starting at an extent of reaction around 0.4 and approaching the fully polymerized values at an extent of reaction around 0.7. The predicted mechanical properties agree well with experiments, except for the yield strength, which is highly affected by the strain rate discrepancy between MD predictions and experimental measurements. The predictions demonstrate that the thermal properties evolve linearly with increases in the extent of reaction. The predicted $T_g$, CTE below $T_g$, and CTE above $T_g$ in the fully polymerized state match experimental measurements very closely.

The MD-predicted material properties as a function of polymerization provide a critical data set for computationally driven process-modeling of Elium composites. Such modeling is necessary for optimizing processing parameters to reduce process-induced residual stresses and deformations. $^{76,77}$ This optimization can ultimately improve the durability of composite structures for a wide range of applications, including wind energy, where composite material recyclability is a key driving force for utilizing thermoplastic composites.

## ■ ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.4c04061.

MD modeling: reaction templates, tacticity analysis, molecular weight distribution, density profile, shear stress−shear strain plot analysis, von Mises stress−shear strain plot analysis, $T_g$, and CTE analysis (PDF)

## ■ AUTHOR INFORMATION
### Corresponding Author
Gregory M. Odegard − Michigan Technological University, Houghton, Michigan 49931, United States; https://orcid.org/0000-0001-7577-6565; Email: gmodegar@mtu.edu

### Authors
Swapnil S. Bamane − Michigan Technological University, Houghton, Michigan 49931, United States; https://orcid.org/0000-0002-7537-1901

Prathamesh P. Deshpande − Michigan Technological University, Houghton, Michigan 49931, United States; https://orcid.org/0000-0003-1441-678X

Sagar U. Patil − Michigan Technological University, Houghton, Michigan 49931, United States; https://orcid.org/0000-0003-4301-777X

Marianna Maiaru − Columbia University, New York, New York 10027, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.4c04061

### Notes
The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS
This research was partially supported by the NASA Space Technology Research Institute (STRI) for Ultra-Strong Composites by Computational Design (US-COMP), grant NNX17AJ32G; NASA grants 80NSSC19K1246 and 80NSSC21M0104; NSF grant 2145387, and the Glenn H. Kemnitz Memorial Annual Fellowship. SUPERIOR, a high-performance computing cluster at Michigan Technological University, was used in obtaining the MD simulation results presented in this publication. The authors would like to thank the Computational Mechanics & Materials Research (CMMR) Lab members at Michigan Technological University for their valuable discussion and insights.

## ■ REFERENCES
(1) Allagui, S.; El Mahi, A.; Rebiere, J. L.; Beyaoui, M.; Bouguecha, A.; Haddar, M. Effect of Recycling Cycles on the Mechanical and Damping Properties of Flax Fibre Reinforced Elium Composite: Experimental and Numerical Studies. *J. Renewable Mater.* 2021, 9 (4), 695−721.

(2) Allagui, S.; El Mahi, A.; Rebiere, J. -l.; Beyaoui, M.; Bouguecha, A.; Haddar, M. In Thermoplastic Elium Recycling: Mechanical Behaviour and Damage Mechanisms Analysis by Acoustic Emission, *Advances in Acoustics and Vibration III*, 2021; Feki, N.; Abbes, M. S.; Taktak, M.; Amine Ben Souf, M.; Chaari, F.; Haddar, M., Eds. Springer International Publishing: 2021; pp 53−61.

(3) Allagui, S.; El Mahi, A.; Rebiere, J.-L.; Beyaoui, M.; Bouguecha, A.; Haddar, M. Experimental studies of mechanical behavior and damage mechanisms of recycled flax/Elium thermoplastic composite. *Polymers and Polymer Composites* 2022, 30, No. 09673911221090048.

(4) Tschentscher, C.; Gebhardt, M.; Chakraborty, S.; Meiners, D. In *Recycling of Elium CFRPs for high temperature dissolution: a study with different solvents, 4th Symposium Materials Technology*, 2021; 2021.

(5) Bhudolia, S. K.; Gohel, G.; Leong, K. F.; Joshi, S. C. Damping, impact and flexural performance of novel carbon/Elium® thermoplastic tubular composites. *Composites Part B: Engineering* 2020, 203, No. 108480.

(6) Kazemi, M. E.; Shanmugam, L.; Lu, D.; Wang, X.; Wang, B.; Yang, J. Mechanical properties and failure modes of hybrid fiber reinforced polymer composites with a novel liquid thermoplastic resin, Elium®. *Composites Part A: Applied Science and Manufacturing* 2019, 125, No. 105523.

(7) Bhudolia, S. K.; Gohel, G.; Leong, K. F.; Barsotti, R. J. Investigation on Ultrasonic Welding Attributes of Novel Carbon/Elium® Composites. *Materials* 2020, 1117.

(8) Bhudolia, S. K.; Gohel, G.; Kah Fai, L.; Barsotti, R. J. Fatigue response of ultrasonically welded carbon/Elium® thermoplastic composites. *Mater. Lett.* 2020, 264, No. 127362.

(9) Barbosa, L. C. M.; Bortoluzzi, D. B.; Ancelotti, A. C. Analysis of fracture toughness in mode II and fractographic study of composites based on Elium® 150 thermoplastic matrix. *Composites Part B: Engineering* 2019, 175, No. 107082.

(10) Han, N.; Baran, I.; Zanjani, J. S. M.; Yuksel, O.; An, L.; Akkerman, R. Experimental and computational analysis of the polymerization overheating in thick glass/Elium® acrylic thermoplastic resin composites. *Composites Part B: Engineering* 2020, 202, No. 108430.

(11) Bhudolia, S. K.; Joshi, S. C.; Bert, A.; Yi Di, B.; Makam, R.; Gohel, G. Flexural characteristics of novel carbon methylmethacrylate composites. *Composites Communications* 2019, 13, 129−133.

(12) Cassano, A. G.; Dev, S.; Maiaru, M.; Hansen, C. J.; Stapleton, S. E. Cure simulations of thick adhesive bondlines for wind energy applications. *J. Appl. Polym. Sci.* 2021, 138 (10), 49989.

(13) Shah, S. P.; Olaya, M. N.; Plaka, E.; McDonald, J.; Hansen, C. J.; Maiarù, M. Effect of moisture absorption on curing of wind blades during repair. *Composites Part A: Applied Science and Manufacturing* 2023, 173, No. 107706.

(14) Shah, S. P.; Patil, S. U.; Hansen, C. J.; Odegard, G. M.; Maiarù, M. Process modeling and characterization of thermoset composites for residual stress prediction. *Mechanics of Advanced Materials and Structures* 2023, 30 (3), 486−497.

(15) Lux, P.; Cassano, A. G.; Johnson, S. B.; Maiaru, M.; Stapleton, S. E. Adhesive curing cycle time optimization in wind turbine blade manufacturing. *Renewable Energy* 2020, 162, 397−410.
15646
https://doi.org/10.1021/acs.jpcc.4c04061
*J. Phys. Chem. C* 2024, 128, 15639−15648

(16) Maiaru, M., Effect of uncertainty in matrix fracture properties on the transverse strength of fiber reinforced polymer matrix composites. In 2018 AIAA/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference; American Institute of Aeronautics and Astronautics: 2018.

(17) Shah, S.; Maiaru, M. In Microscale Analysis of Virtually Cured Polymer Matrix Composites Accounting for Uncertainty in Matrix Properties During Manufacturing, 33rd Technical Conference of the American Society of Composites, Seattle, WA; American Society of Composites: Seattle, WA, 2018.

(18) Shah, S. P.; Maiarù, M. Effect of Manufacturing on the Transverse Response of Polymer Matrix Composites. Polymers 2021, 2491.

(19) Patil, S. U.; Shah, S. P.; Olaya, M.; Deshpande, P. P.; Maiaru, M.; Odegard, G. M. Reactive Molecular Dynamics Simulation of Epoxy for the Full Cross-Linking Process. ACS Applied Polymer Materials 2021, 3 (11), 5788−5797.

(20) D'Mello, R. J.; Waas, A. M.; Maiaru, M.; Koon, R., Integrated Computational Modeling for Efficient Material and Process Design for Composite Aerospace Structures. In AIAA Scitech 2020 Forum; American Institute of Aeronautics and Astronautics: 2020.

(21) Gaikwad, P. S.; Krieg, A. S.; Deshpande, P. P.; Patil, S. U.; King, J. A.; Maiaru, M.; Odegard, G. M. Understanding the Origin of the Low Cure Shrinkage of Polybenzoxazine Resin by Computational Simulation. ACS Applied Polymer Materials 2021, 3 (12), 6407−6415.

(22) Odegard, G. M.; Patil, S. U.; Deshpande, P. P.; Kanhaiya, K.; Winetrout, J. J.; Heinz, H.; Shah, S. P.; Maiaru, M. Molecular Dynamics Modeling of Epoxy Resins Using the Reactive Interface Force Field. Macromolecules 2021, 54 (21), 9815−9824.

(23) Odegard, G. M.; Patil, S. U.; Gaikwad, P. S.; Deshpande, P.; Krieg, A. S.; Shah, S. P.; Reyes, A.; Dickens, T.; King, J. A.; Maiaru, M. Accurate predictions of thermoset resin glass transition temperatures from all-atom molecular dynamics simulation. Soft Matter 2022, 18 (39), 7550−7558.

(24) Deshpande, P.; Shah, S.; Patil, S. U.; Olaya, M.; Odegard, G. M.; Maiaru, M. In Process Modelling the Cure of Bisphenol-A Epoxy/Jeffamine System using ICME, 36th American Society for Composites Conference; Virtual, Virtual, 2021 DOI:10.12783/asc36/35812.

(25) Deshpande, P. P.; Shah, S.; Patil, S.; Kashmari, K.; Odegard, G. M.; Maiaru, M. In A Multi-Scale Approach for Modelling the Cure of Thermoset Polymers within ICME, 34th Technical Conference for the American Society of Composites, Atlanta, GA, 2019; American Society of Composites: Atlanta, GA, 2019.

(26) Patil, S.; Shah, S.; Deshpande, P.; Kashmari, K.; Olaya, M.; Odegard, G. M.; Maiaru, M., Multi-Scale Approach To Predict Cure-Induced Residual Stresses In An Epoxy System. In 35th American Society for Composites Conference; American Society for Composites: Jersey City, NJ, 2020.

(27) Pisani, W. A.; Radue, M. S.; Chinkanjanarot, S.; Bednarcyk, B. A.; Pineda, E. J.; Waters, K.; Pandey, R.; King, J. A.; Odegard, G. M. Multiscale modeling of PEEK using reactive molecular dynamics modeling and micromechanics. Polymer 2019, 163, 96−105.

(28) Kashmari, K.; Al Mahmud, H.; Patil, S. U.; Pisani, W. A.; Deshpande, P.; Maiaru, M.; Odegard, G. M. Multiscale Process Modeling of Semicrystalline PEEK for Tailored Thermomechanical Properties. ACS Applied Engineering Materials 2023, 1 (11), 3167−3177.

(29) Thompson, A. P.; Aktulga, H. M.; Berger, R.; Bolintineanu, D. S.; Brown, W. M.; Crozier, P. S.; in't Veld, P. J.; Kohlmeyer, A.; Moore, S. G.; Nguyen, T. D.; Shan, R.; Stevens, M. J.; Tranchida, J.; Trott, C.; Plimpton, S. J. LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales. Comput. Phys. Commun. 2022, 271, No. 108171.

(30) Heinz, H.; Lin, T. J.; Kishore Mishra, R.; Emami, F. S. Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 2013, 29 (6), 1754−1765.

(31) Winetrout, J. J.; Kanhaiya, K.; Sachdeva, G.; Pandey, R.; Damirchi, B.; van Duin, A.; Odegard, G.; Heinz, H.Implementing Reactivity in Molecular Dynamics Simulations with the Interface Force Field (IFF-R) and Other Harmonic Force Fields2021, p. arXiv:2107.14418. https://ui.adsabs.harvard.edu/abs/2021arXiv210714418W (accessed July 01, 2021).

(32) Deshpande, P. P.; Radue, M. S.; Gaikwad, P.; Bamane, S.; Patil, S. U.; Pisani, W. A.; Odegard, G. M. Prediction of the Interfacial Properties of High-Performance Polymers and Flattened CNT-Reinforced Composites Using Molecular Dynamics. Langmuir 2021, 37 (39), 11526−11534.

(33) Pisani, W. A.; Radue, M. S.; Patil, S. U.; Odegard, G. M. Interfacial modeling of flattened CNT composites with cyanate ester and PEEK polymers. Composites Part B: Engineering 2021, 211, No. 108672.

(34) Sachdeva, G.; Patil, S. U.; Bamane, S. S.; Deshpande, P. P.; Pisani, W. A.; Odegard, G. M.; Pandey, R. Mechanical response of polymer/BN composites investigated by molecular dynamics method. J. Mater. Res. 2022, 37 (24), 4533−4543.

(35) Bamane, S. S.; Gaikwad, P. S.; Radue, M. S.; Gowtham, S.; Odegard, G. M. Wetting Simulations of High-Performance Polymer Resins on Carbon Surfaces as a Function of Temperature Using Molecular Dynamics. Polymers 2021, 13 (13), 2162.

(36) Bamane, S. S.; Jakubinek, M. B.; Kanhaiya, K.; Ashrafi, B.; Heinz, H.; Odegard, G. M. Boron Nitride Nanotubes: Force Field Parameterization, Epoxy Interactions, and Comparison with Carbon Nanotubes for High-Performance Composite Materials. ACS Applied Nano Materials 2023, 6 (5), 3513−3524.

(37) Pineda, E. J.; Husseini, J.; Kemppainen, J.; Odegard, G. M.; Bednarcyk, B. A.; Pisani, W.; Stapleton, S. E., Multiscale Modeling of Thermoplastics Using Atomistic-informed Micromechanics. In AIAA SCITECH 2023 Forum; American Institute of Aeronautics and Astronautics: 2023.

(38) Patil, S. U.; Radue, M. S.; Pisani, W. A.; Deshpande, P.; Xu, H.; Al Mahmud, H.; Dumitrică, T.; Odegard, G. M. Interfacial characteristics between flattened CNT stacks and polyimides: A molecular dynamics study. Comput. Mater. Sci. 2020, 185, No. 109970.

(39) Pisani, W. A.; Wedgeworth, D. N.; Roth, M. R.; Newman, J. K.; Shukla, M. K. Computational Prediction of Mechanical Properties of PA6−Graphene/Carbon Nanotube Nanocomposites. The Journal of Physical Chemistry C 2021, 125 (28), 15569−15578.

(40) Pisani, W. A., Exploration of Two Polymer Nanocomposite Structure-Property Relationships Facilitated by Molecular Dynamics Simulation and Multiscale Modeling; US Army Engineer Research and Development Center, Environmental Laboratory and Geotechnical and Structures Laboratory, 2023.APAPisani, W. A., Roth, M. R., Shukla, M. K. 2023.

(41) Kashmari, K.; Patil, S. U.; Kemppainen, J.; Shankara, G.; Odegard, G. M. Optimal Molecular Dynamics System Size for Increased Precision and Efficiency for Epoxy Materials. The Journal of Physical Chemistry B 2024, 128 (17), 4255−4265.

(42) Gissinger, J. R.; Jensen, B. D.; Wise, K. E. Modeling chemical reactions in classical molecular dynamics simulations. Polymer 2017, 128, 211−217.

(43) Gissinger, J. R.; Jensen, B. D.; Wise, K. E. REACTER: A Heuristic Method for Reactive Molecular Dynamics. Macromolecules 2020, 53 (22), 9953−9961.

(44) Hadden, C. M.; Jensen, B. D.; Bandyopadhyay, A.; Odegard, G. M.; Koo, A.; Liang, R. Molecular modeling of EPON-862/graphite composites: Interfacial characteristics for multiple crosslink densities. Compos. Sci. Technol. 2013, 76, 92−99.

(45) Stukowski, A. Visualization and analysis of atomistic simulation data with OVITO-the Open Visualization Tool. Model. Simul. Mater. Sci. 2010, 18 (1), No. 015012.

(46) Malvern, L. E., Introduction to the Mechanics of a Continuous Medium; Prentice-Hall, Inc.: Upper Saddle River, NJ, 1969.

(47) Vollmayr, K.; Kob, W.; Binder, K. How do the properties of a glass depend on the cooling rate? A computer simulation study of a Lennard-Jones system. The Journal of Chemical Physics 1996, 105 (11), 4714−4728.

---
15647
https://doi.org/10.1021/acs.jpcc.4c04061
J. Phys. Chem. C 2024, 128, 15639−15648

(48) Odegard, G. M.; Bandyopadhyay, A. Physical aging of epoxy polymers and their composites. *Journal of Polymer Science Part B: Polymer Physics* **2011**, *49* (24), 1695−1716.

(49) Muggeo, V. M. R. Estimating regression models with unknown break-points. *Stat Med* **2003**, *22* (19), 3055−3071.

(50) Muthuraj, R.; Grohens, Y.; Seantier, K. Mechanical and thermal insulation properties of elium acrylic resin/cellulose nanofiber based composite aerogels. *Nano-Structures & Nano-Objects* **2017**, *12*, 68−76.

(51) Arkema, *Technical Data Sheet: Elium 150*.

(52) Moller, K.; Bein, T.; Fischer, R. X. Entrapment of PMMA Polymer Strands in Micro- and Mesoporous Materials. *Chem. Mater.* **1998**, *10* (7), 1841−1852.

(53) Banks-Sills, L.; Shiber, D. G.; Fourman, V.; Eliasi, R.; Shlayer, A. Experimental determination of mechanical properties of PMMA reinforced with functionalized CNTs. *Composites Part B: Engineering* **2016**, *95*, 335−345.

(54) Umemoto, K.; Kurata, S. Basic study of a new denture base resin applying hydrophobic methacrylate monomer. *Dent Mater J* **1997**, *16* (1), 21−30.

(55) Darvell, B. W., Chapter 5 - Acrylic. In *Materials Science for Dentistry(NinthEdition)*, Darvell, B. W., Ed.; Woodhead Publishing:2009; pp 108-127.

(56) McCabe, J. F.; Wilson, H. J. The use of differential scanning calorimetry for the evaluation of dental materials. *J Oral Rehabil* **1980**, *7* (3), 235−243.

(57) Evans, S. L. Effects of porosity on the fatigue performance of polymethyl methacrylate bone cement: an analytical investigation. *Proc Inst Mech Eng H* **2006**, *220* (1), 1−10.

(58) Pickett, H. G.; Appleby, R. C. A Comparison of Six Acrylic Resin Processing Technics. *The Journal of the American Dental Association* **1970**, *80* (6), 1309−1314.

(59) Dumond, J. J.; Mahabadi, K. A.; Yee, Y. S.; Tan, C.; Fuh, J. Y. H.; Lee, H. P.; Low, H. Y. High resolution UV roll-to-roll nanoimprinting of resin moulds and subsequent replication via thermal nanoimprint lithography. *Nanotechnology* **2012**, *23* (48), No. 485310.

(60) Iyoshi, S.; Miyake, H.; Nakamatsu, K.-i.; Matsui, S. UV-curable resins appropriate for UV nanoimprint. *Journal of Photopolymer Science and Technology* **2008**, *21* (4), 573−581.

(61) Mott, P. H.; Dorgan, J. R.; Roland, C. M. The bulk modulus and Poisson’s ratio of “incompressible” materials. *J Sound Vib* **2008**, *312* (4), 572−575.

(62) Kazemi, M. E.; Shanmugam, L.; Chen, S.; Yang, L.; Yang, J. Novel thermoplastic fiber metal laminates manufactured with an innovative acrylic resin at room temperature. *Composites Part A: Applied Science and Manufacturing* **2020**, *138*, No. 106043.

(63) Li, J.; Jin, S.; Lan, G.; Chen, S.; Li, L. Molecular dynamics simulations on miscibility, glass transition temperature and mechanical properties of PMMA/DBP binary system. *Journal of Molecular Graphics and Modelling* **2018**, *84*, 182−188.

(64) Odegard, G. M.; Jensen, B. D.; Gowtham, S.; Wu, J.; He, J.; Zhang, Z. Predicting mechanical response of crosslinked epoxy using ReaxFF. *Chem. Phys. Lett.* **2014**, *591*, 175−178.

(65) Patil, S. U.; Krieg, A. S.; Odegard, L. K.; Yadav, U.; King, J. A.; Maiaru, M.; Odegard, G. M. Simple and convenient mapping of molecular dynamics mechanical property predictions of bisphenol-F epoxy for strain rate, temperature, and degree of cure. *Soft Matter* **2023**, *19* (35), 6731−6742.

(66) Radue, M. S.; Jensen, B. D.; Gowtham, S.; Klimek-McDonald, D. R.; King, J. A.; Odegard, G. M. Comparing the Mechanical Response of Di-, Tri-, and Tetra-functional Resin Epoxies with Reactive Molecular Dynamics. *J Polym Sci B Polym Phys* **2018**, *56* (3), 255−264.

(67) Samavedi, S.; Poindexter, L. K.; Van Dyke, M.; Goldstein, A. S., Chapter 7 - Synthetic Biomaterials for Regenerative Medicine Applications. In *Regenerative Medicine Applications in Organ Transplantation*, Orlando, G.; Lerut, J.; Soker, S.; Stratta, R. J., Eds.; Academic Press: Boston, 2014; pp 81-99.

(68) Moy, P.; Gunnarsson, C. A.; Weerasooriya, T.; Chen, W. In Stress-Strain Response of PMMA as a Function of Strain-Rate and Temperature, *Dynamic Behavior of Materials, Volume 1*, New York, NY, 2011; Proulx, T., Ed. Springer New York: New York, NY, 2011; pp 125-133.

(69) Ju, S. P.; Chen, H. Y.; Shih, C. W. Investigating mechanical properties of polymethylmethacrylate/silver nanoparticle composites by molecular dynamics simulation. *J. Nanoparticle Res.* **2017**, *20* (1), 1.

(70) Odegard, G. M.; Jensen, B. D.; Gowtham, S.; Wu, J. Y.; He, J. Y.; Zhang, Z. L. Predicting mechanical response of crosslinked epoxy using ReaxFF. *Chem. Phys. Lett.* **2014**, *591*, 175−178.

(71) Raponi, O. d. A.; Barbosa, L. C. M.; de Souza, B. R.; Ancelotti Junior, A. C. Study of the influence of initiator content in the polymerization reaction of a thermoplastic liquid resin for advanced composite manufacturing. *Advances in Polymer Technology* **2018**, *37* (8), 3579−3587.

(72) Porter, C. E.; Blum, F. D. Thermal Characterization of PMMA Thin Films Using Modulated Differential Scanning Calorimetry. *Macromolecules* **2000**, *33* (19), 7016−7020.

(73) Min, K.; Silberstein, M.; Aluru, N. R. Crosslinking PMMA: Molecular dynamics investigation of the shear response. *Journal of Polymer Science Part B: Polymer Physics* **2014**, *52* (6), 444−449.

(74) Tang, Z.; Okazaki, S. All-atomistic molecular dynamics study of the glass transition of amorphous polymers. *Polymer* **2022**, *254*, No. 125044.

(75) Han, G.; Huan, S.; Han, J.; Zhang, Z.; Wu, Q. Effect of acid hydrolysis conditions on the properties of cellulose nanoparticle-reinforced polymethylmethacrylate composites. *Materials* **2014**, *7* (1), 16−29.

(76) Shah, S.; Patil, S.; Deshpande, P.; Krieg, A. S.; Kashmari, K.; Al Mahmud, H.; King, J. A.; Odegard, G. M.; Maiaru, M., Multiscale Modeling for Virtual Manufacturing of Thermoset Composites. In *AIAA SciTech Conference*; American Institute of Aeronautics and Astronautics: Orlando, FL, 2020.

(77) Deshpande, P.; Shah, S.; Patil, S.; Kashmari, K.; Odegard, G. M.; Maiaru, M., Multiscale Modelling of the Cure Process in Thermoset Polymers using ICME. In *35th American Society for Composites Conference*; American Society for Composites: Jersey City, NJ, 2020.
