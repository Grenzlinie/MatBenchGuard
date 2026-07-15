# Buckling failure of square ice-nanotube arrays constrained in graphene nanocapillaries

YinBo Zhu, FengChao Wang, and HengAn Wu

Citation: *The Journal of Chemical Physics* **145**, 054704 (2016); doi: 10.1063/1.4959902

View online: http://dx.doi.org/10.1063/1.4959902

View Table of Contents: http://aip.scitation.org/toc/jcp/145/5

Published by the **American Institute of Physics**

---

## Articles you may be interested in

Liquid-solid and solid-solid phase transition of monolayer water: High-density rhombic monolayer ice

*The Journal of Chemical Physics* **140**, 184507184507 (2014); 10.1063/1.4874696

---

![](./images/811176100787912705_1.jpg)

# Buckling failure of square ice-nanotube arrays constrained in graphene nanocapillaries

YinBo Zhu, FengChao Wang, $^{\text{a)}}$ and HengAn Wu

CAS Key Laboratory of Mechanical Behavior and Design of Materials, Department of Modern Mechanics, CAS Center for Excellence in Nanoscience, University of Science and Technology of China, Hefei, Anhui 230027, China

(Received 19 April 2016; accepted 14 July 2016; published online 1 August 2016)

Graphene confinement provides a new physical and mechanical environment with ultrahigh van der Waals pressure, resulting in new quasi-two-dimensional phases of few-layer ice. Polymorphic transition can occur in bilayer constrained water/ice system. Here, we perform a comprehensive study of the phase transition of AA-stacked bilayer water constrained within a graphene nanocapillary. The compression-limit and superheating-limit (phase) diagrams are obtained, based on the extensive molecular-dynamics simulations at numerous thermodynamic states. Liquid-to-solid, solid-to-solid, and solid-to-liquid-to-solid phase transitions are observed in the compression and superheating of bilayer water. Interestingly, there is a temperature threshold ($\sim$275 K) in the compression-limit diagram, which indicates that the first-order and continuous-like phase transitions of bilayer water depend on the temperature. Two obviously different physical processes, compression and superheating, display similar structural evolution; that is, square ice-nanotube arrays (BL-VHDI) will bend first and then transform into bilayer triangular AA stacking ice (BL-AAI). The superheating limit of BL-VHDI exhibits local maxima, while that of BL-AAI increases monotonically. More importantly, from a mechanics point of view, we propose a novel mechanism of the transformation from BL-VHDI to BL-AAI, both for the compression and superheating limits. This structural transformation can be regarded as the "buckling failure" of the square-ice-nanotube columns, which is dominated by the lateral pressure. *Published by AIP Publishing.* [http://dx.doi.org/10.1063/1.4959902]

## I. INTRODUCTION

Water and ice are omnipresent on the Earth and ubiquitous on comets, planets, and planet moons. The phase transition and phase behavior of water/ice and its intriguing properties have been a significant topic of extensive research interests in wide range of scientific and technological applications. $^{1–5}$ Less obvious but undoubtedly more ubiquitous is water confined in the microscopic environments. $^{6,7}$ Toward a better understanding of the influences of pressure and temperature on the phase behavior of confined and interfacial water would further the advancement of water science, including the polymorphism and polyamorphism in low-dimensional water. An abundance of low-dimensional crystalline and amorphous ice polymorphs have been observed from molecular dynamics (MD) simulations, density functional theory (DFT) calculations, and experiments, such as ice nanotubes, $^{8–11}$ monolayer, $^{12–19}$ bilayer, $^{18–32}$ and trilayer ice $^{18,19,31–39}$ polymorphs. Bai *et al.* and Takaiwa *et al.* systemically investigated the different phases of water confined in cylindrical pores (quasi-1D confinement) versus diameter of carbon nanotubes and axial pressure. $^{9,10}$ Two-dimensional (2D) bilayer hexagonal ice in hydrophobic nanopores was first obtained by Koga *et al.* through MD simulation. $^{21}$ When constrained in the nanoscale environment and under ultrahigh pressure, water and ice manifest dramatic differences from their bulk counterparts in part because the van der Waals pressure can induce water-to-ice transformation, known as the metastability limit of the 2D liquid. $^{7,18,40}$ Algara-Siller *et al.* recently demonstrated that when water is confined between two sheets of graphene, it becomes a 2D liquid and then transformed into an intriguing monolayer square ice. $^{7}$ In mechanics, this liquid-to-solid transformation characterizes the compression limit of 2D water. $^{18}$ Some subsequent MD simulations and DFT calculations reveal that 2D water constrained in graphene nanocapillaries can form rich crystalline and amorphous structures. $^{16,18,41–44}$

Polymorphic transition can occur in confined water under high lateral pressure, which had been investigated by Bai and Zeng. $^{20}$ Previous studies had obtained numerous bilayer crystalline and amorphous ices from computer simulations when bilayer water (BL-water) is confined in two parallel flat hydrophobic plates (silt pores), such as bilayer hexagonal ice (BL-ice I), $^{19–23}$ bilayer amorphous ice (BL-A), $^{23,25}$ bilayer mixed-polygonal ice, $^{23,25,26}$ bilayer-Cairo pentagonal ice, $^{26}$ bilayer very-high-density amorphous (BL-VHDA$_1$, BL-VHDA$_2$), $^{19,20,30}$ and square ice-nanotube arrays (BL-VHDI). $^{19,20,41}$ Some recent researches also observed several new bilayer ice structures in graphene confinement, including bilayer AB stacking amorphous (BL-AB), $^{18}$ bilayer triangular AA stacking ice (BL-AAI), $^{18,42}$ and square wave ice. $^{42}$ Liquid-to-solid, solid-to-solid, and solid-to-liquid-to-solid phase transitions were found between

$^{\text{a)}}$Author to whom correspondence should be addressed. Electronic mail: wangfc@ustc.edu.cn

different bilayer polymorph ice phases, including the first-order and the continuous-like phase transitions. $^{18-20,23-25,30,32}$ The compression limit of 2D water constrained in graphene nanocapillaries versus separation of two parallel graphene sheets at ambient temperature was investigated recently. $^{18}$ A semi-quantitative phase diagram of stable crystalline bilayer ices, $^{42}$ combining DFT calculations with MD simulations, was plotted in the $P$-$T$ plane by Corsetti *et al.* However, to our knowledge, a comprehensive perspective of the phase diagram of bilayer water/ice has not been achieved yet. Many previous investigations have focused on interfacial and confined water or on the water transport in a nanoscale channel. $^{3-7,45-47}$ The temperature-dependent compression limit of bilayer water/ice, including freezing and melting, needs much deeper research. It is of both fundamental and applied significance to study the mechanical stability of highly constrained water, including compression and superheating.

## II. SIMULATION METHOD

We performed MD simulations of BL-water confined in graphene nanocapillaries, using the LAMMPS program. $^{48}$ Our simulation system is similar to that used in previous studies. $^{7,18}$ Two water reservoirs containing 1000 molecules each were connected by a relatively long capillary formed by two parallel graphene sheets. The lateral pressure pushes water molecules in reservoirs into the graphene nanocapillary. The length and width of the graphene nanocapillary were fixed at $42.60$ Å and $36.89$ Å, respectively, in all simulations. The distance $h$ between the center plane of the graphene wall was fixed at $9.0$ Å. Periodic boundary conditions were imposed in all three directions. The MD simulations were performed in the isothermal-isobaric $(NP_{zz}T)$ ensemble, in which the temperature $(T)$ and lateral pressure $(P_{zz})$ were controlled by the Nosé-Hoover thermostat and barostat, respectively. The total number of water molecules $N$ in the nanocapillary can change depending on $P_{zz}$, $T$, and $h$. A time step of 1.0 fs is used for the velocity-Verlet integrator. The potential energy per molecule, the oxygen-oxygen radial distribution function [$g_{\text{O-O}}(r)$], and the mean-squared displacement (MSD) were computed in the simulations to characterize the phase transition of BL-water during the compression and superheating processes.

The total potential of interaction is taken as the sum of interactions $\Sigma\ \phi_{\text{water}}(\mathbf{r}_{i},\mathbf{r}_{j})$ among water molecules, and the external potential $\Sigma\ \phi_{\text{wall}}(\mathbf{r}_{i},\mathbf{r}_{j})$ of the interaction between water molecules and the graphene wall, $^{10}$ where $\mathbf{r}_{i}$ stands for the coordinate of water molecule $i$, $\phi_{\text{water}}$ is the extended four point charge (TIP4P/2005) potential of water, and $\phi_{\text{wall}}$ is the Lennard-Jones potential for water-graphene interaction. $^{10,18}$ The pairwise interactions between any two water molecules are described by the TIP4P/2005 model, $^{49,50}$ including the long-ranged Coulomb potential and the short-ranged Lennard-Jones (LJ) 12-6 potential between the interaction sites. The intermolecular interactions between sites $i$ and $j$ of different molecules are defined by the site-site potential as follows: $^{18,49}$

$$
U_{ij}=4\varepsilon_{ij}\left[\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12}-\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{6}\right]+\frac{e^{2}}{4\pi\varepsilon_{0}}\frac{q_{i}q_{j}}{r_{ij}},\tag{1}
$$

where $r$ denotes the distance of separation, $q$ denotes the electric quantity of the particle, $e$ is the proton charge, $\varepsilon_{0}$ is the permittivity of the vacuum, and the $\varepsilon$ and $\sigma$ characterize the energy and length scale, respectively. $^{18}$ The long-range Coulombic interaction is calculated using a particle-particle particle-mesh (PPPM) algorithm with an accuracy of $10^{-4}$. The cutoff distance is set to be $12.0$ Å for the LJ interaction, $^{17}$ and $8.5$ Å for the Coulombic interaction. The distance from oxygen atom to the massless charge site $d_{OM}=0.1546$ Å. The water LJ potential interaction parameters are $\sigma_{\text{OO}}=3.1589$ Å, $\varepsilon_{\text{OO}}=0.1852$ kcal/mol, $\sigma_{\text{OH}}=0$, $\varepsilon_{\text{OH}}=0$, $\sigma_{\text{HH}}=0$, and $\varepsilon_{\text{HH}}=0.^{51}$ The carbon-carbon interaction parameters are $\sigma_{\text{CC}}=3.2211$ Å and $\varepsilon_{\text{CC}}=0.0474$ kcal/mol. $^{18,52}$ The carbon-oxygen interaction parameters, $\sigma_{\text{CO}}=3.19$ Å, $\varepsilon_{\text{CO}}=0.093\,69$ kcal/mol, are taken from Ref. 52. The carbon-water potentials are based on the parameters for carbon, oxygen, and hydrogen obtained through the Lorentz-Berthelot mixing rule. $^{52}$

## III. RESULTS AND DISCUSSION

### A. Temperature-dependent compression limit

Evaluation of the metastability of a solid under conditions of compression is often performed since it is critical for the structure design. $^{18}$ Temperature and pressure are two obviously different but equivalently important factors in the phase transition of highly constrained water. At ambient temperature, a recent simulation study showed that BL-water can transform into BL-AB and BL-AAI when the lateral pressure is beyond the compression-limit. $^{18}$ To achieve more understanding of the compression limit of BL-water constrained in graphene nanocapillaries, a low temperature simulation ($T=240$ K, 25 ns) was performed. The results of potential energy (per molecule) and computed MSD are illustrated in Figure 1(a). Obviously different with those in Ref. 18, BL-water exhibits more complicated phase transitions at low temperature. The whole region in Figure 1(a) is mainly divided into five sub-regions: BL-A, BL-liquid phase, BL-VHDI, $^{20}$ curving BL-VHDI, and BL-AAI, respectively. BL-A is formed first at relatively low pressure ($P_{zz}<0.35$ GPa), and then the potential energy and MSD are increased at a faster rate with increasing lateral pressure until the BL-VHDI is formed ($P_{zz}>1.2$ GPa). The transformation from BL-A to BL-VHDI is a typical solid-to-liquid-to-solid phase transition (Movie S1), which exhibits the Oswald staging phenomenon, $^{20,25}$ namely, an intermediate liquid state arises between BL-A and BL-VHDI. In the middle Oswald stage, the diffusion constant of water stays above $10^{-7}\ \text{cm}/\text{s}^{2}$. With the continuous increasing lateral pressure, BL-VHDI will bend first ($P_{zz}>3.2$ GPa) and then transform into BL-AAI ($P_{zz}>4.15$ GPa) (Movie S2). More typical snapshots of bilayer bended tube phase are shown in Figure S1. When the lateral pressure is beyond $\sim4.7$ GPa, another solid-to-liquid-to-solid phase transition will happen. $^{39}$

In order to compare the compression of BL-water at different system temperatures, four typical potential energy (per molecule) curves for the cases of 240 K, 260 K, 280 K, and

![](./images/811176100787912705_2.jpg)

FIG. 1. (a) Compression limit of bilayer liquid water constrained in graphene nanocapillary at $h = 9.0\mathring{A}$, $T = 240$ K, and $0.1$ GPa $\leq P_{zz} \leq 5.0$ GPa. The potential energy per molecule (black line), the number of water molecules (red line), and the MSD of water molecules (blue line) in the channel varied with increasing lateral pressure $P_{zz}$. The MSD is a statistical quantity on simulation time. The lateral pressure is increased gradually in a step of $0.2$ GPa/ns. The insets show the variation of ice structures in the compression process. (b) Potential energy (per molecule) curves at different system temperatures.

300 K are displayed in Figure 1(b). Apparently, the changes of potential energy for low and high system temperatures are obviously different. There is a large jump between the red line (260 K) and green line (280 K) at $P_{zz} \approx 1.5$–3.2 GPa, which indicates that the phase transitions depend on the system temperature. The obvious difference of potential energy shown in Figure 1(b) also indicates that BL-VHDI is a low-energy phase relative to BL-AAI. For the cases of low temperature ($T = 240$ and 260 K), the potential energy has a decrease at $P_{zz} \approx 1.2$–2.2 GPa and then increases gradually. Whereas, for the cases of high temperature ($T = 280$ and 300 K), the potential energy has a decrease at $P_{zz} \approx 2.5$–3.5 GPa and then increases gradually. Generally, potential energy exhibits a sudden change for the first-order phase transition,²³ while increases gradually for the continuous-like transition.¹⁸ˑ³⁰ The phase transition from BL-liquid to BL-VHDI is first-order, while that from BL-liquid to BL-AAI is continuous-like.¹⁸ˑ³⁰ We can calculate the energy difference between the solid ($P_{zz} = 2.0$ GPa) and corresponding liquid ($P_{zz} = 1.0$ GPa) phases; that is, $\Delta E_1 = (E_{solid} - E_{liquid})_{260K} = -0.0545$ kcal/mol $(k_BTN_A)_{260K} = 0.5167$ kcal/mol; $\Delta E_2 = (E_{solid} - E_{liquid})_{280K} = 0.1471$ kcal/mol $(k_BTN_A)_{280K} = 0.5564$ kcal/mol. The difference among $\Delta E_1$ and $\Delta E_2$ manifests that a temperature threshold should exist in the range of 260–280 K. Two-phase thermodynamic (2PT) model provides an effective way for calculating the free energy and the entropy of liquid.⁵³ˑ⁵⁵ The entropy and the driving force for the filling of graphene nanocapillaries with water require further study. Moreover, the transition from BL-A to BL-VHDI and then into BL-AAI (Movies S1 and S2) is widely existent in the compression of BL-water when the system temperature is lower than 275 K (temperature dependence compression limits will be shown in detail later). When the system temperature is higher than 275 K, the phase transition of BL-water is similar with that in Ref. 18 at ambient temperature (300 K). The structural transformations in these two different compression-limit processes are demonstrated in Figure 2. The red and blue arrows represent the compression at high and low system temperatures, respectively. Note that, the interim phase, curving BL-VHDI (Figure S1), exists in the transformation from BL-VHDI to BL-AAI. The structural transformation mechanism will be shown in detail later.

The former simulation shows that the compression limit of BL-water at low temperature obviously differs from that at ambient temperature. To gain more insight into the compression limit of BL-water, extensive MD simulations are performed over wide ranges of $T$ (100–400 K) and $P_{zz}$ (0.1–5.0 GPa) to explore the temperature-dependent compression-limit (phase) diagram in the $T$-$P_{zz}$ plane. Here, we mainly focus on the phase transition of BL-water ($h = 9.0\mathring{A}$) at different system temperatures. MD simulations are carried out to measure the compression-limit. A series of points marking the compression-limit at the given lateral pressure $P_{zz}$ are then plotted. The lateral pressure in the compression process is increased in a step of $0.2$ GPa/ns. At each temperature in the compression, the simulation time is 30 ns, including 5 ns in the initial equilibrium run. The obtained compression-limit versus temperature (phase) diagram for BL-water is demonstrated in Figure 3, where different regions divided by colored lines denote different phases. The colored symbols in Figure 3 represent the compression-limits for different BL-water phases at the corresponding temperature. This phase diagram can clearly reveal the phase transitions and phase behaviors of BL-water in graphene nanocapillaries. In summary, this diagram has three different bilayer AA-stacked ice phases, that is, BL-A (BL-ice I), BL-VHDI, and BL-AAI, respectively. BL-A and BL-ice I can exist at low temperature and low lateral pressure (BL-ice I needs a long time annealing from BL-A ice).²⁰ BL-VHDI can exist at low temperature and low pressure relative to that of BL-AAI. There are two different solid-to-liquid-to-solid, one solid-to-solid, and one liquid-to-solid phase transitions shown in Figure 3. When the system temperature is low ($T < 275$ K), water molecules which have entered into graphene channel will form BL-A ice first and then transform into BL-VHDI with an intermediate BL-liquid phase (solid-to-liquid-to-solid). With the increasing lateral pressure, the BL-VHDI will bend first and then

![](./images/811176100787912705_3.jpg)

FIG. 2. Structural evolution of bilayer water confined in graphene nanocapillaries ($h = 9.0$ Å) at different temperatures with increasing lateral pressure. Red and white balls denote oxygen and hydrogen atoms, respectively.

transform into BL-AAI (solid-to-solid). When the temperature is lower than 215 K, water molecules cannot enter into the channel at lower lateral pressure. It indicates that the low temperature and lateral pressure cannot provide the needed driving force to overcome the energy barriers at the entrances, resulting in that the water molecules in reservoirs cannot be pushed into the graphene channel. When the temperature is higher ($T > 275$ K), the BL-A phase cannot be obtained because the temperature is higher than the melting point of BL-A phase. $^{20}$ Water molecules entering into graphene channel will form BL-liquid first and then transform into BL-AAI (liquid-to-solid). Subsequently, the BL-AAI will transform into trilayer ice at higher lateral pressure (solid-to-liquid-to-solid). $^{39}$

Note that, this phase diagram is discontinuous at 270–280 K. The potential energy curves for the cases of 270 K and 275 K, shown in Figure S2, are different from those shown in Figure 1(b). It is worth noting that there exists

![](./images/811176100787912705_4.jpg)

FIG. 3. The temperature-dependent compression limit (phase) diagram of BL-water constrained in graphene nanocapillary ($h = 9.0$ Å, 100 K $\leq T$ $\leq$ 400 K, 0.1 GPa $\leq P_{zz} \leq$ 5.0 GPa). The green dashed line denotes the temperature threshold between BL-VHDI and BL-AAI. Colored symbols denote the compression-limits of different phases at the corresponding temperature.

a boundary (green dashed line) in Figure 3. The green dashed line shows that there is a temperature threshold (~275 K) between BL-VHDI and BL-AAI, which is corresponding to the difference of potential energy curves as shown in Figure 1(b). That is, the temperature threshold shown in Figure 3 is mainly due to that the phase transitions from liquid to these two bilayer ice polymorphs are different. BL-VHDI is a low-energy phase relative to BL-AAI. Moreover, this phase diagram directly manifests that the polymorphic transition can occur in the confined water system corresponding to Figure 2. The temperature threshold shown in Figure 3 also indicates that the structural transformation should be existent at a given lateral pressure if the system temperature is unfixed (e.g., cooling or heating).

Recently, Corsetti *et al.* found that square wave ice can be formed under ultrahigh lateral pressure based on the DFT calculations.⁴² BL-ice I and BL-VHDI are observed both from DFT calculations and MD simulations with different force-field models.²⁰,⁴² The square wave ice structure is not seen in our simulations and previous MD studies. In our MD simulations, BL-AAI can be seen as a crystalline-like structure consisting of BL-triangular cluster and bits of BL-rhombic cluster (the inset in Figure 1(b)). The BL-triangular cluster plays more roles in BL-AAI.¹⁸ The square wave ice⁴² in Corsetti *et al.* is more like the crystalline BL-rhombic cluster.

### B. Superheating limit (melting point)

Confined water has peculiar properties due to the additional thermodynamic term afforded by the confining surfaces.⁵⁶ In many respects, confined water most probably has the same properties with the superheated water.⁵⁷,⁵⁸ Having illustrated the temperature dependence compression-limit diagram of BL-water in graphene nanocapillaries, we attempt to simulate the superheating limit of bilayer ice. A typical heating process of BL-VHDI at a given lateral pressure $P_{zz}=2.0$ GPa (260–360 K, 20 ns) is demonstrated in Figure 4. From Figure 4(b), we can see that BL-VHDI transforms into bended tube phase first and then turns into BL-AAI when the temperature is beyond the superheating-limit (Movie S3).

The transformation from BL-VHDI to BL-AAI is a solid-to-solid phase transition. Interestingly, the structural evolution in the melting of BL-VHDI has some similarities with the compression process as shown in Figure 1; that is, BL-VHDI transforming into BL-AAI will bend first both in the compression and superheating. At last in Figure 4, BL-AAI turns into a disordered state at higher temperature, where the stacking order of oxygen atoms is not as ordered as AA-stacked order. The potential energy (red line in Figure 4(a)) has an abrupt jump nearby the superheating-limit, which indicates that the ordered hydrogen-bonding network of square tubes is broken. The details of this structural transformation are demonstrated in Figure S1 and Movie S4, in which the water molecules cannot form regular hydrogen bonds at the end of the bended tubes. An individual superheating-limit simulation of BL-AAI is shown in Figure S3, where the BL-AAI corresponds to the compression limit at high temperature ($T>275$ K). The potential energy as shown in Figure S3(b) does not appear a similar sudden jump with the melting of BL-VHDI. The abrupt change in MSD [Figure S3(a)] can characterize the melting of BL-AAI because the slope of MSD represents the diffusion behavior of water molecules.

The difference of potential energies in the heating processes between these two bilayer ices is mainly due to that the phase transition of BL-VHDI is first-order while that of BL-AAI is continuous-like.¹⁸,³⁰ The abrupt change of potential energy shown in Figure 4(a) demonstrates that the transformation between BL-VHDI and BL-AAI is a first order phase transition. Particularly, the number $N$ of water molecules in the graphene channel has some arresting change during the superheating process. The number $N$ decreases first when BL-VHDI is bending and then has a sudden jump when BL-VHDI transforms into BL-AAI. The distribution densities [$\rho=A/(N/2)$, the $A$ is the area of the channel] of BL-VHDI, bended BL-VHDI, and BL-AAI are 7.32 Å², 7.45 Å², and 7.21 Å², respectively. In the superheating of BL-VHDI, the increased temperature induces thermal expansion of ice-nanotubes. The adjacent square tubes will stagger much more in the heating process. Simultaneously,

![](./images/811176100787912705_5.jpg)

FIG. 4. Superheating limit (melting) of BL-VHDI at $h=9.0$ Å and $P_{zz}=2.0$ GPa (20 ns, 260–360 K). (a) The potential energy per molecule (red line) and the number of water molecules (blue line) in the channel varied with increasing temperature. (b) The computed MSD in the heating process. The insets demonstrate the structural variation during the melting process.

the lateral pressure leads to the bending of ice-nanotubes. Subsequently, when the temperature is gradually up to the superheating-limit, the square ice-nanotubes are unstable and then damaged. This phenomenon manifests that the action of temperature and lateral pressure is interactive and correlative in the superheating limit. The structural transformation mechanism will be shown in detail later.

Another large number of MD simulations were performed at grid points on the $P_{zz}$-$T$ plane, each starting from an ice structure at the corresponding lateral pressure. These simulations provide the melting properties of BL-water confined in graphene nanocapillaries ($h = 9.0$ Å). In the compression process, ice structures can be obtained at different $P_{zz}$. Then we can gradually increase the global temperature in a step of 5 K/ns to obtain the melting point (superheating-limit) for each ice. At each lateral pressure in the superheating, the simulation time is 25–35 ns, including 5 ns in the initial equilibrium run. The superheating-limit (phase) diagram for BL-VHDI (initial temperature is 260 K) is shown in Figure 5, where the sub-regions correspond to the melting process shown in Figure 4. The whole region in Figure 5 is divided into four sub-regions according to its structural feature, including BL-VHDI, curving BL-VHDI, BL-AAI, and disordered state. For BL-AAI at high temperature ($T > 275$ K) in Figure 3, we also simulated the superheating limit then plot the diagram in Figure S4 (initial temperature is 300 K). The melting rule in Figure S4 is similar with the blue line (with solid circle symbols) in Figure 5. We define the melting point of BL-AAI via the $g_{O-O}(r)$ and the computed MSD of water molecules in the channel (Figure S3) because BL-AAI is a high-energy oxygen-ordered phase. BL-VHDI is a low-energy ordered phase with good hydrogen-bonding tubes, so the potential energy of the water molecules in the channel tends to exhibit an abrupt jump in the melting process (Figure 4(a)). The melting phase diagrams in Figures 5 and S4 indicate that the melting point of BL-AAI increases with increasing lateral pressure. Whereas, for BL-VHDI, the superheating-limit curve is convex with local maximum.

Unlike the bulk ice, the melting point of layered ice in confined environment is much higher. The melting temperature of bilayer ice is not only unusually high compared to the other confined ices, but also above the melting point of bulk hexagonal ice. $^{31}$ In our MD simulations, the computed melting point is 342 K for BL-AAI, and 322 K for BL-VHDI when the lateral pressure $P_{zz} = 2.0$ GPa (Figures 4 and 5). The slope of the melting curves satisfies the Clapeyron equation: $^{10,14}$

$$
\left(\frac{\partial T}{\partial P_{zz}}\right)_{h}=\frac{v^{\alpha}-v^{\beta}}{s^{\alpha}-s^{\beta}},\qquad(2)
$$

where $v$ and $s$ are the volume and entropy of per molecule in the channel, respectively. Let $\alpha$ and $\beta$ denote the ice phase (BL-AAI) and liquid phase in the melting process, respectively. The water molecule number $N$ in the channel decreases when the ice transforms into liquid, so $v^{\alpha}-v^{\beta}<0$. The $s^{\alpha}-s^{\beta}$ is equal to the corresponding enthalpy change divided by the temperature $T$ and the entropy increases upon melting, so $s^{\alpha}-s^{\beta}<0$. Thus, $\partial T/\partial P_{zz}>0$, indicating that the melting point of BL-AAI should increase with increasing $P_{zz}$. Let $\alpha$ and $\beta$ denote the BL-VHDI and BL-AAI in the superheating process of the tube phase, respectively. The water molecule number $N$ in the channel increases when BL-VHDI transforms into BL-AAI (Figure 4(a)), so $v^{\alpha}-v^{\beta}>0$. When the lateral pressure $P_{zz}$ is smaller than the optimal pressure, the effect of temperature is much more than that of pressure (the bending needs higher system temperature), so $s^{\alpha}-s^{\beta}>0$, and then $\partial T/\partial P_{zz}>0$. If $P_{zz}$ is larger than the optimal pressure, the larger lateral pressure will make the square-tubes bending first at initial system temperature, that is, the effect of pressure is much more than that of temperature in this case, so $s^{\alpha}-s^{\beta}<0$, and then $\partial T/\partial P_{zz}<0$. Thus, the melting curves of BL-VHDI are convex with local maximum.

Different with previous studies on the phase diagram of 2D water/ice, $^{14,18,20,30}$ we mainly focus on the polymorphic transition of AA-stacked bilayer water/ice in graphene nanocapillaries. Here, lateral pressure and system temperature are considered as dominating factors in the MD simulations. The behaviors of temperature and lateral pressure in the phase transition of constrained bilayer water/ice are interactive and correlative. The compression-limit and superheating-limit (phase) diagrams can directly demonstrate the structural transformation among different AA-stacked bilayer ice and provide some intriguing phenomena between the bilayer tube phase and triangular phase. Moreover, the phase transitions shown in Figures 4 and 5 indicate that the melting of bilayer tube ice via a two-stage process: first a first-order transition to

![](./images/811176100787912705_6.jpg)

FIG. 5. Superheating limit diagram of BL-VHDI ($h = 9$ Å). The melting point of BL-VHDI is computed at different $P_{zz}$. The superheating-limit (melting point) of BL-AAI increases with increasing $P_{zz}$. However, for BL-VHDI, the superheating-limit curve exists local maxima.

the bilayer triangular ice, followed by a continuous transition to the disordered state.

## C. Bucking failure of square ice-nanotube arrays
Note that an interesting structural transformation, BL-VHDI bends first and then transforms into BL-AAI, is observed both in the compression and superheating processes. The details of the bended tube phase are shown in Figure S1, where the typical snapshots of bended ice-nanotubes are more like the buckling state of compressive bar in mechanics. Here, from a mechanics point of view, we propose a novel transformation mechanism between the two AA stacking bilayer ice polymorphs.

Stability of compressive bar is a basic and important part in the mechanics of materials and structures.⁵⁹ Buckling failure is a common failure mode of beam column and shell structures in engineering. For example, in an elastic straight bar or column, buckling (bending) will occur when the axial load is beyond a critical value. In our simulations, BL-VHDI can be regarded as arrays of square ice-nanotube (hollow columns) under axial load (lateral pressure $P_{zz}$) in nano-mechanics. The interim phase, curving BL-VHDI, is widely existent both in the compression and superheating (Figures 1, 4, and S1; Movies S2 and S3). Therefore, every single ice-nanotube of BL-VHDI in this structural transformation can be seen as a compressive bar. Both for the compression and superheating limits, the transformation from BL-VHDI to BL-AAI is a nano-mechanics problem. The lateral pressure $P_{zz}$ is the primary factor and induces the bending of ice-nanotube columns. The oxygen atoms in the graphene channel maintain AA stacking order all the time, so we use a planar schematic diagram in Figure 6 to represent the ice structures. The length of the black solid and dashed lines in Figures 6(a) and 6(b) is ~2.79 Å, which is corresponding to the location of first sharp-peak (2.79 ± 0.06 Å) in the $g_{\text{O-O(r)}}$s of these two structures (Figure S5).

In the compression ($T < 275$ K), the increasing lateral pressure equivalently enlarges the “axial load” and then directly induces the bending of straight ice-nanotube columns. When the lateral pressure is beyond the compression-limit, most of the square elements in ice-nanotube columns turn into rhombs or triangles, and simultaneously, curving BL-VHDI transforms into BL-AAI. The critical pressure of this structural transformation in compression is the compression-limit boundary between BL-VHDI and BL-AAI as shown in Figure 3 (blue line with circle symbols). In the superheating, the increasing system temperature reduces the “stability” of ice-nanotube, which is just like reducing the elasticity modulus $E$ in the Euler formula of compressive bar.⁵⁹ In other words, the system temperature determines the intensity of hydrogen bonding force among water molecules in square-ice-nanotube. With the increasing temperature, the fixed lateral pressure will reach the critical pressure of the corresponding temperature. Simultaneously, the ice-nanotube columns bend and then continue to bend with increasing temperature. When the temperature is beyond the superheating-limit, the curving BL-VHDI transforms into BL-AAI accompanied with most of the square elements turning into rhombs or triangles. The critical temperature in superheating is the superheating-limit boundary between bended BL-VHDI and BL-AAI as shown in Figure 5 (blue line with hollow star symbols). This buckling-like transformation corresponds with the abrupt variation of the number $N$ of water molecules as shown in Figure 4(a). Similarly, in a large simulation system which two reservoirs contain 4000 water molecules (the channel size is 56.57 Å × 62.18 Å), the phase transition from BL-VHDI to BL-AAI with a bended interim phase also can be observed both in the compression and superheating processes. The critical stress ($\sigma_{cr}$) of the elastic buckling in compression bar satisfies the Euler formula⁵⁹

$$
\sigma_{c r}=\frac{\pi^{2} E I}{\mu^{2} l^{2} A}, \tag{3}
$$

where $E$, $I$, $A$, and $l$ are the elasticity modulus, inertia moment, cross sectional area, and length of compression bar, respectively. The length factor $\mu$ depends on the boundary conditions of the compression bar. In the MD simulations, the wavelength of the buckled pattern depends on the size of simulation system (length of the graphene channel). The critical pressure in the elastic buckling also depends on the size of simulation system because the critical stress is related to the length of bar [Eq. (3)]. In all simulations, periodic boundary conditions are imposed in all three directions. Therefore, the critical pressure and the wavelength of buckled pattern do not depend on the boundary conditions in the simulations.

![](./images/811176100787912705_7.jpg)

FIG. 6. A planar schematic diagram of the transformation from BL-VHDI to BL-AAI. (a) BL-VHDI. (b) BL-AAI. The schematic diagram in the blue dashed box illustrates the transformation mechanism, where the ice-nanotube can be seen as a compressive bar under axial load (lateral pressure). The length of all the black solid and dashed lines in (a) and (b) is 2.79 Å. The red balls represent the AA stacked oxygen atoms.

In this elastic "buckling failure" of square-ice-nanotube columns, the action of system temperature and lateral pressure is interactive and correlative both in the compression and superheating. Temperature dominates the intensity of hydrogen bonding force among water molecules in the square-ice-nanotube, while lateral pressure is the dominated factor in this structural transformation. Partly, the superheating of BL-VHDI can be seen as a compression with varying temperature.

## IV. CONCLUSION

In conclusion, we perform a comprehensive study of the compression and superheating limits of bilayer water constrained within a graphene nanocapillary ($h = 9$ Å). The compression-limit and superheating-limit (phase) diagrams are obtained, based on the comprehensive molecular-dynamics simulations at numerous thermodynamic states. Liquid-to-solid, solid-to-solid, and solid-to-liquid-to-solid phase transitions are observed in the compression and superheating of bilayer water, which demonstrate that polymorphic transition can occur in bilayer constrained water/ice system at different temperatures and lateral pressures. BL-VHDI is a low-energy phase relative to BL-AAI. The transformation from BL-VHDI to BL-AAI is a first order phase transition. The temperature threshold (~275 K) between BL-VHDI and BL-AAI is existent in the temperature-dependent compression-limit diagram, which indicates that the first-order and continuous-like phase transitions of bilayer water depend on the temperature. In the heating process, the superheating-limit (melting point) of BL-AAI increases with increasing lateral pressure $P_{zz}$. However, for BL-VHDI, the superheating-limit curve exists local maxima. The melting of bilayer tube ice via a two-stage process: first a first-order transition to the bilayer triangular ice, followed by a continuous transition to the disordered state. The phase transition from BL-VHDI to BL-AAI with a bended interim phase can be observed both in the compression and superheating processes. More importantly, from a mechanics point of view, we propose a novel mechanism of the transformation from BL-VHDI to BL-AAI, both for the compression and superheating limits. This transformation can be regarded as the "buckling failure" of square-ice-nanotube columns, in which the effects of system temperature and lateral pressure are interactive and correlative. Temperature determines the intensity of hydrogen bonding force in the square-ice-nanotube, while lateral pressure is the primary factor in this structural transformation.

## SUPPLEMENTARY MATERIAL

See supplementary material for movies of phase transition of BL-water in the compression limit (Movies S1 and S2), superheating limit (Movie S3), and the bended BL-VHDI (Movie S4); more structural details of the curving BL-VHDI (Figure S1); potential energy curves of 270 K and 275 K in compression limits (Figure S2); an individual superheating-limit simulation of BL-AAI when the initial temperature is 300 K (Figure S3); superheating-limit phase diagram of BL-AAI (Figure S4); and radial distribution functions of BL-VHDI and BL-AAI (Figure S5). These materials are free of charge.

## ACKNOWLEDGMENTS

This work was jointly supported by the National Natural Science Foundation of China (Grant Nos. 11525211, 11472263, and 11302218), Anhui Provincial Natural Science Foundation (Grant No. 1408085J08), and the Fundamental Research Funds for the Central Universities of China. The numerical calculations have been performed on the supercomputing system in the Supercomputing Center of University of Science and Technology of China.

The authors declare no competing financial interest.

$^{1}$P. H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, "Phase behaviour of metastable water," Nature 360, 324 (1992).
$^{2}$A. K. Soper, "Water and ice," Science 297, 1288 (2002).
$^{3}$R. R. Nair, H. A. Wu, P. N. Jayaram, I. V. Grigorieva, and A. K. Geim, "Unimpeded permeation of water through helium-leak-tight graphene-based membranes," Science 335, 442 (2012).
$^{4}$R. K. Joshi, P. Carbone, F. C. Wang, V. G. Kravets, Y. Su, I. V. Grigorieva, H. A. Wu, A. K. Geim, and R. R. Nair, "Precise and ultrafast molecular sieving through graphene oxide membranes," Science 343, 752 (2014).
$^{5}$A. Kalra, S. Garde, and G. Hummer, "Osmotic water transport through carbon nanotube membranes," Proc. Natl. Acad. Sci. U. S. A. 100, 10175 (2003).
$^{6}$I. Brovchenko and A. Oleinikova, Interfacial and Confined Water (Elsevier, Amsterdam, 2008).
$^{7}$G. Algara-Siller, O. Lehtinen, F. C. Wang, R. R. Nair, U. Kaiser, H. A. Wu, A. K. Geim, and I. V. Grigorieva, "Square ice in graphene nanocapillaries," Nature 519, 443 (2015).
$^{8}$K. Koga, G. T. Gao, H. Tanaka, and X. C. Zeng, "Formation of ordered ice nanotubes inside carbon nanotubes," Nature 412, 802 (2001).
$^{9}$J. Bai, J. Wang, and X. C. Zeng, "Multiwalled ice helices and ice nanotubes," Proc. Natl. Acad. Sci. U. S. A. 103, 19664 (2006).
$^{10}$D. Takaiwa, I. Hatano, K. Koga, and H. Tanaka, "Phase diagram of water in carbon nanotubes," Proc. Natl. Acad. Sci. U. S. A. 105, 39 (2008).
$^{11}$G. Hummer, J. C. Rasaiah, and J. P. Noworyta, "Water conduction through the hydrophobic channel of a carbon nanotube," Nature 414, 188 (2001).
$^{12}$R. Zangi and A. E. Mark, "Monolayer ice," Phys. Rev. Lett. 91, 025502 (2003).
$^{13}$W.-H. Zhao, J. Bai, L.-F. Yuan, J. Yang, and X. C. Zeng, "Ferroelectric hexagonal and rhombic monolayer ice phases," Chem. Sci. 5, 1757 (2014).
$^{14}$K. Koga and H. Tanaka, "Phase diagram of water between hydrophobic surfaces," J. Chem. Phys. 122, 104711 (2005).
$^{15}$J. Bai, C. A. Angell, and X. C. Zeng, "Guest-free monolayer clathrate and its coexistence with two-dimensional high-density ice," Proc. Natl. Acad. Sci. U. S. A. 107, 5718 (2010).
$^{16}$F. Corsetti, P. Matthews, and E. Artacho, "Structural and configurational properties of nanoconfined monolayer ice from first principles," Sci. Rep. 6, 18651 (2016).
$^{17}$T. Kaneko, J. Bai, K. Yasuoka, A. Mitsutake, and X. C. Zeng, "Liquid-solid and solid-solid phase transition of monolayer water: High-density rhombic monolayer ice," J. Chem. Phys. 140, 184507 (2014).
$^{18}$Y. B. Zhu, F. C. Wang, J. Bai, X. C. Zeng, and H. A. Wu, "Compression limit of two-dimensional water constrained in graphene nanocapillaries," ACS Nano 9, 12197 (2015).
$^{19}$W. H. Zhao, L. Wang, J. Bai, L. F. Yuan, J. Yang, and X. C. Zeng, "Highly confined water: Two-dimensional ice, amorphous ice, and clathrate hydrates," Acc. Chem. Res. 47, 2505 (2014).
$^{20}$J. Bai and X. C. Zeng, "Polymorphism and polyamorphism in bilayer water confined to slit nanopore under high pressure," Proc. Natl. Acad. Sci. U. S. A. 109, 21240 (2012).
$^{21}$K. Koga, X. C. Zeng, and H. Tanaka, "Freezing of confined water: A bilayer ice phase in hydrophobic nanopores," Phys. Rev. Lett. 79, 5262 (1997).
$^{22}$J. Slovak, H. Tanaka, K. Koga, and X. C. Zeng, "Computer simulation of bilayer ice structures and thermodynamics," Physica A 319, 163 (2003).

$^{23}$K. Koga, H. Tanaka, and X. C. Zeng, "First order transition in confined water between high-density liquid and low-density amorphous phases," *Nature* **408**, 564 (2000).

$^{24}$R. Zangi and A. E. Mark, "Bilayer ice and alternate liquid phases of confined water," *J. Chem. Phys.* **119**, 1694 (2003).

$^{25}$J. Bai, X. C. Zeng, K. Koga, and H. Tanaka, "Formation of quasi two-dimensional bilayer ice in hydrophobic slits: A possible candidate for ice XIII?," *Mol. Simul.* **29**, 619 (2003).

$^{26}$J. C. Johnston, N. Kastelowitz, and V. Molinero, "Liquid to quasicrystal transition in bilayer water," *J. Chem. Phys.* **133**, 154516 (2010).

$^{27}$H. Qiu, X. C. Zeng, and W. Guo, "Water in inhomogeneous nanoconfine- ment: Coexistence of multilayered liquid and transition to ice nanoribbons," *ACS Nano* **9**, 9877 (2015).

$^{28}$J. Chen, J. Guo, X. Meng, J. Peng, J. Sheng, L. Xu, Y. Jiang, X. Z. Li, and E. G. Wang, "An unconventional bilayer ice structure," *Nat. Commun.* **5**, 4056 (2014).

$^{29}$D. J. Anick, "Static density functional study of graphene-hexagonal bilayer ice interaction," *J. Phys. Chem. A* **118**, 7498 (2014).

$^{30}$S. Han, M. Y. Choi, P. Kumar, and H. E. Stanley, "Phase transitions in confined water nanofilms," *Nat. Phys.* **6**, 685 (2010).

$^{31}$N. Kastelowitz, J. C. Johnston, and V. Molinero, "The anomalously high melting temperature of bilayer ice," *J. Chem. Phys.* **132**, 124511 (2010).

$^{32}$N. Giovambattista, P. J. Rossky, and P. G. Debenedetti, "Phase transitions induced by nanoconfinement in liquid water," *Phys. Rev. Lett.* **102**, 050603 (2009).

$^{33}$N. Giovambattista, P. J. Rossky, and P. G. Debenedetti, "Effect of pressure on the phase behavior and structure of water confined between nanoscale hydrophobic and hydrophilic plates," *Phys. Rev. E* **73**, 041604 (2006).

$^{34}$N. Giovambattista, P. G. Debenedetti, and P. J. Rossky, "Hydration behavior under confinement by nanoscale surfaces with patterned hydrophobicity and hydrophilicity," *J. Phys. Chem. C* **111**, 1323 (2007).

$^{35}$M. Jia, W.-h. Zhao, and L.-f. Yuan, "New hexagonal-rhombic trilayer ice structure confined between hydrophobic plates," *Chin. J. Chem. Phys.* **27**, 15 (2014).

$^{36}$P. Kumar, S. V. Buldyrev, F. W. Starr, N. Giovambattista, and H. E. Stanley, "Thermodynamics, structure, and dynamics of water confined between hydrophobic plates," *Phys. Rev. E* **72**, 051503 (2005).

$^{37}$P. Kumar, F. W. Starr, S. V. Buldyrev, and H. E. Stanley, "Effect of water-wall interaction potential on the properties of nanoconfined water," *Phys. Rev. E* **75**, 011202 (2007).

$^{38}$R. Zangi and A. E. Mark, "Electrofreezing of confined water," *J. Chem. Phys.* **120**, 7123 (2004).

$^{39}$Y. B. Zhu, F. C. Wang, J. Bai, X. C. Zeng, and H. A. Wu, "Formation of trilayer ices in graphene nanocapillaries under high lateral pressure," *J. Phys. Chem. C* **120**, 8109–8115 (2016).

$^{40}$F. London, "The general theory of molecular forces," *Trans. Faraday Soc.* **33**, 8b–26 (1937).

$^{41}$J. Chen, G. Schusteritsch, C. J. Pickard, C. G. Salzmann, and A. Michaelides, "Two dimensional ice from first principles: Structures and phase transitions," *Phys. Rev. Lett.* **116**, 025501 (2016).

$^{42}$F. Corsetti, J. Zubeltzu, and E. Artacho, "Enhanced configurational entropy in high-density nanoconfined bilayer ice," *Phys. Rev. Lett.* **116**, 085901 (2016).

$^{43}$S. F. Mario, M. Neek-Amal, and F. M. Peeters, "AA-stacked bilayer square ice between graphene layers," *Phys. Rev. B* **92**, 245428 (2015).

$^{44}$S. Jiao, C. Duan, and Z. Xu, "Water under the cover: Structures and ther- modynamics of water encapsulated by graphene," *Phys. Rev. E* (to be pub- lished); e-print arXiv:1509.07215v2 [cond-mat.stat-mech].

$^{45}$S. Ban, J. Xie, Y. Wang, B. Jing, B. Liu, and H. Zhou, "Insight into the nanoscale mechanism of rapid H₂O transport within a graphene oxide membrane: Impact of oxygen functional group clustering," *ACS Appl. Mater. Interfaces* **8**, 321 (2016).

$^{46}$G. Carchini, M. García-Melchor, Z. Łodziana, and N. Lopez, "Understand- ing and tuning the intrinsic hydrophobicity of rare-earth oxides: A DFT + U study," *ACS Appl. Mater. Interfaces* **8**, 152 (2016).

$^{47}$N. Wei, X. Peng, and Z. P. Xu, "Undertanding water permeation in graphene oxide membranes," *ACS Appl. Mater. Interfaces* **6**, 5877 (2014).

$^{48}$S. Plimpton, "Fast parallel algorithms for short-range molecular dynamics," *J. Comput. Phys.* **117**, 1 (1995).

$^{49}$J. L. Abascal and C. Vega, "A general purpose model for the condensed phases of water: TIP4P-2005," *J. Chem. Phys.* **123**, 234505 (2005).

$^{50}$C. Vega, J. L. Abascal, M. M. Conde, and J. L. Aragones, "What ice can teach us about water interactions: A critical comparison of the performance of different water models," *Faraday Discuss.* **141**, 251 (2009).

$^{51}$C. Vega, E. Sanz, and J. L. Abascal, "The melting temperature of the most common models of water," *J. Chem. Phys.* **122**, 114507 (2005).

$^{52}$T. Werder, J. H. Walther, R. L. Jaffe, T. Halicioglu, and P. Koumoutsakos, "On the water-carbon interaction for use in molecular dynamics simu- lations of graphite and carbon nanotubes," *J. Phys. Chem. B* **107**, 1345 (2003).

$^{53}$T. A. Pascal, W. A. Goddard, and Y. Jung, "Entropy and the driving force for the filling of carbon nanotubes with water," *Proc. Natl. Acad. Sci. U. S. A.* **108**, 11794 (2011).

$^{54}$S.-T. Lin, M. Blanco, and W. A. Goddard, "The two-phase model for calculating thermodynamic properties of liquids from molecular dynamics: Validation for the phase diagram of Lennard-Jones fluids," *J. Chem. Phys.* **119**, 11792 (2003).

$^{55}$S.-T. Lin, M. Blanco, and W. A. Goddard, "Two-phase thermodynamic model for efficient and accurate absolute entropy of water from molecular dynamics simulations," *J. Phys. Chem. B* **114**, 8191 (2010).

$^{56}$L. Mercury and K. I. Shmulovich, "Experimental superheating and cavitation of water and solutions at spinodal-like negative pressures," in *Transport and Reactivity of Solutions in Confined Hydrosystems* (Springer, Netherlands, 2014), pp. 159–171.

$^{57}$F. Restagno, L. Bocquet, and T. Biben, "Metastability and nucleation in capillary condensation," *Phys. Rev. Lett.* **84**, 2433 (2000).

$^{58}$K. Morishige and H. Yasunaga, "Tensile effect on a confined phase," *J. Phys. Chem. B* **110**, 3864 (2006).

$^{59}$S. P. Timoshenko and J. M. Gere, *Theory of Elastic Stability*, 2nd ed. (McGraw-Hill, 1989).