![](./images/1019554943180210181_1.jpg)
![](./images/1019554943180210181_2.jpg)

Article

# A Multiscale Simulation on Aluminum Ion Implantation-Induced Defects in 4H-SiC MOSFETs

Yawen Wang $^{1}$, Haipeng Lan $^{1}$, Qiwei Shangguan $^{1}$, Yawei Lv $^{1,*}$ and Changzhong Jiang $^{2,*}$

1.  School of Physics and Electronics, Hunan University, Changsha 410082, China; wangyawen2021@hnu.edu.cn (Y.W.); lanhaipeng@hnu.edu.cn (H.L.); shangguanqiwei@hnu.edu.cn (Q.S.)
2.  College of Materials Science and Engineering, Hunan University, Changsha 410082, China
*   Correspondence: lvyawei@hnu.edu.cn (Y.L.); czjiang@hnu.edu.cn (C.J.)

![](./images/1019554943180210181_3.jpg)

![](./images/1019554943180210181_4.jpg)

**Abstract:** Aluminum (Al) ion implantation is one of the most important technologies in SiC device manufacturing processes due to its ability to produce the p-type doping effect, which is essential to building p–n junctions and blocking high voltages. However, besides the doping effect, defects are also probably induced by the implantation. Here, the impacts of Al ion implantation-induced defects on 4H-SiC MOSFET channel transport behaviors are studied using a multiscale simulation flow, including the molecular dynamics (MD) simulation, density functional theory (DFT) calculation, and tight-binding (TB) model-based quantum transport simulation. The simulation results show that an Al ion can not only replace a Si lattice site to realize the p-doping effect, but it can also replace the C lattice site to induce mid-gap trap levels or become an interstitial to induce the n-doping effect. Moreover, the implantation tends to bring additional point defects to the 4H-SiC body region near the Al ions, which will lead to more complicated coupling effects between them, such as degrading the p-type doping effect by trapping free hole carriers and inducing new trap states at the 4H-SiC bandgap. The quantum transport simulations indicate that these coupling effects will impede local electron transports, compensating for the doping effect and increasing the leakage current of the 4H-SiC MOSFET. In this study, the complicated coupling effects between the implanted Al ions and the implantation-induced point defects are revealed, which provides new references for experiments to increase the accepter activation rate and restrain the defect effect in SiC devices.

**Keywords:** 4H-SiC; Al; implantation; defects; molecular dynamics (MD); density functional theory (DFT); tight-binding (TB) model; quantum transport

## 1. Introduction

Although silicon (Si) is still the most widely used material in power electronics due to its mature manufacturing technique, drawbacks stemming from its physical properties have already stimulated research on the replacement of Si material by wide bandgap materials. As a representative and compared with Si, silicon carbide (SiC) shows obvious advantages in bandgaps, breakdown field, thermal conductivity, and saturation drift velocity [1–5], making it suitable for a variety of novel device applications [6,7]. SiC is characterized by strong covalent bonds between Si and carbon (C) atoms, and the flexible directions of these bonds can lead to different spatial arrangements, resulting in different crystal structures, such as the hexagonal and cubic morphologies [8–10]. Among them, the hexagonal 4H-SiC emerges due to its comprehensive quality, which can realize a balance among excellent physical properties, low defect density, and moderate manufacturing cost [4,11].

Due to the high hardness and negligible impurity diffusion rate, ion implantation, followed by a mandatory post-annealing treatment, is almost the only way to tune the conductivity of SiC before its device applications. For example, the realization of p-type 4H-SiC relies on the aluminum (Al) ion implantation [12] since Al ions exhibit relatively low thermal ionization energy, high solubility limit, and good defect-suppression ability.

Electronics 2024, 13, 2758. https://doi.org/10.3390/electronics13142758

https://www.mdpi.com/journal/electronics

Compared with the n-type doping technology, Al ion implantation still suffers from electrical activation and defect problems today. Kawahara et al. had already observed two deep-level transient spectroscopy (DLTS) peaks, IN3 and IN9 ($E_c$—0.6 eV and $E_c$—1.6 eV), after low-dose Al ion implantation and post-annealing at 1700 °C. They assigned these trap levels to the well-known $Z_{1/2}$ and $EH_{6/7}$ levels, which could be induced by C vacancies ($V_C$). At high dose levels, the electrical activations of implanted Al become another problem, as it will reach a limit along the increasing annealing temperature and time [13–15]. There is a contradiction between the electrical activation of the Al ion and the control of the $V_C$ concentration. Nipoti et al. suggested that maintaining a post-implantation temperature of around 1600–1650 °C was beneficial to low $V_C$ concentrations while reaching a 69% electrical activation of $1 \times 10^{20}\ \text{cm}^{-3}$ Al ion implantation needed an annealing temperature of up to 1950 °C [15]. To realize an excellent p-type doping effect, theoretical models and simulations are seriously needed to investigate the atomic environments around the implanted Al ions after complicated cascade collisions and thermal treatments.

At the atomic scale level, Hornos et al. carried out early density functional theory (DFT) calculations on 4H-SiC supercells and found some stable and metastable Al ion-related complex defects [16], but their originations and stabilities are questionable due to the lacking of molecular dynamics (MD) simulations. Wu et al. studied the defect evolution and doping efficiency of Al ion implantation in 3C-SiC using the MD method, and they found surface recrystallizations that were closely related to compressive stresses [17]. Their defect descriptions stayed at the atom cluster level, leading to indistinguishable defect details, let alone their couplings with Al ions.

Not only the Al ion implantation-related defect structures studied above but also the defect-induced trap levels and their impacts on transport behaviors of 4H-SiC devices are also desired. Megherbi et al. carried out a numerical simulation study on 4H-SiC p-i-n diodes with electrically activated Al acceptors and implantation-induced trap concentrations [18]. By adding the charges due to traps and defects into their drift-diffusion (DD) models, their detrimental effects on carrier transport behaviors at different bias regions were observed. Aside from the DD model, the quantum tight-binding (TB) model had already been established 20 years ago [19]. Although it is believed to be more accurate to describe the defect effect, no work has used the TB model to directly assess the impacts of defects on carrier transport in 4H-SiC devices. We infer that the reason may be the complex model revisions towards building trap levels in the bandgap.

Here, we combine the advanced theoretical models and simulation methods above to implement a multiscale simulation of the Al ion implantation and post-annealing processes. We focus on the implantation-induced point defects in 4H-SiC and their couplings with the Al ions. The attractions between Al ions and point defects and their coupling effects are revealed by DFT calculations. Moreover, TB models representing small parts of the 4H-SiC MOSFET channels are established, including the trap levels due to these defects. From the Poisson-nonequilibrium Green's function (NEGF) solver, the impacts of Al ion implantation on local carrier transports are finally obtained. From the simulation flow, the important Al ion-point defect coupling effects, which can seriously degrade local transport behaviors, are highlighted, offering new theoretical evidence for experiments to explain the complex doping results.

## 2. Simulation Methods
### 2.1. MD Simulation
We used the MD simulation software Large-scale Atomic/molecular Massively Parallel Simulator (LAMMPS) version (2 August 2023) to simulate the implantation and annealing process of Al ions [20]. The Open Visualization Tool (OVITO) was used to visualize the simulation model and analyze the data [21]. The size of the implantation and annealing model of 4H-SiC is 5.23 nm × 5.33 nm × 9.06 nm and contains 24,480 atoms. The whole system is divided into three distinct layers along the deep direction as follows: a 7.04 nm Newton layer, a 1.01 nm thermostat layer, and a 1.01 nm boundary layer. In the Newton

layer, atomic evolution was carried out according to the classical laws of dynamics using a microcanonical ensemble (NVE). The atoms directly involved in the displacement cascade followed the actual energy exchange process during implantation. In the thermostat layer, the Berendsen thermostat was used to simulate the heat exchange process inside the material under nonequilibrium conditions, as well as the temperature dissipation during the ion bombardment of the target [22]. The boundary layer limits the degree of freedom of the simulated system by fixing the boundary atoms. At the beginning of the simulation, the canonical ensemble (NVT) was used to relax the entire system at 300 K.

Then, we used a 1 keV Al ion to implant the 4H-SiC (0001) plane with a 7° angle from the z-axis to prevent the channeling effect, corresponding to the implantation region of 2 nm × 2 nm, and it was enough to cover the range of Al ion motion. It is also noted that 1 keV energy is enough to inject the Al ion into the bulk 4H-SiC, leading to abundant defect types that deserve further studies. To prevent the serious overestimation of the Al ion range, different energies obtained through the Stopping and Range of Ions in Matter (SRIM) software were used to calculate the corresponding electronic stopping force through linear interpolation [23]. The periodic boundary condition was adopted for the x- and y-directions and the non-periodic boundary condition was adopted in the z (deep)-direction. This allows atoms in the x- and y-directions to interact at the boundaries, exiting from one edge of the simulation box and re-entering from the opposite edge. Instead of the non-periodic surface energy, the surface energy under periodic boundary conditions can accurately simulate the surface changes in the target material in actual processing. Timestep $\Delta t$ can vary between 0.002 fs and 1 fs, based on the speed of the fastest particle in the system, which is specified to move no more than 0.02 Å in a single integration, ensuring the accuracy of the simulation under high-speed cascade collision.

Then, the annealing process was adopted in the Nose–Hoover thermostat NPT system to achieve temperature control. All boundaries were set as periodic. The time step was 0.5 fs from 300 K to 3300 K at a rate of 10 K/ps, and the temperature was held for 200 ps to achieve self-repair of the lattice damage and point defects [17]. The high annealing temperature of 3300 K was chosen due to the overestimation of the 4H-SiC melting point by the Tersoff potential. The whole implantation and annealing process simulations were repeated 10 times to find out the defect types as much as possible.

The accuracy of the potential function is the core of the MD to correctly describes the interaction between particles. For SiC systems, the Tersoff potential is often used to describe the covalent interaction between SiC atoms [24]. The Zigler–Biersack–Littmark (ZBL) repulsion potential is mainly used to describe the short-range interaction between C and Si atoms [25]. Previous studies have shown that the Tersoff force field cannot only accurately describe the amorphous phase, liquid phase, and quenching of the covalent bond system but can also obtain the solid-phase epitaxial growth simulation results of the amorphous covalent bond system with good consistency with the experimental regrowth rate. In addition, the SiC atom departure threshold energy, calculated by the Tersoff potential function, is basically consistent with the experimental results, which is the key to accurately calculating the cascade collision process and simulating the damage evolution. Secondly, Lampin et al. proved that there is a linear relationship between the recrystallization rate calculated using the Tersoff potential and the experimental value, and the actual corresponding temperature value can be obtained indirectly by calculating the temperature under the Tersoff potential. Therefore, the Tersoff/ZBL potential is selected in this paper to describe the interaction between SiC atoms during p-type doping ion implantation and post-annealing:

$$
E = \frac{1}{2} \sum_{i} \sum_{i \neq j} V_{ij} \tag{1}
$$

$$
V_{ij} = \left(1 - f_{F}(r_{ij})\right) V_{ij}^{ZBL} + f_{F}(r_{ij}) V_{ij}^{Tersoff} \tag{2}
$$

$$
f_{F}(r_{ij}) = \frac{1}{1 + e^{-A_{F}(r_{ij}-r_{c})}} \tag{3}
$$

Among them, $V_{ij}^{ZBL}$ and $V_{ij}^{Tersoff}$ are the functional parts of the Tersoff and ZBL potentials, respectively; $r_{ij}$ is the bond length between atom $i$ and atom $j$; $r_{c}$ is the cutoff range of the ZBL potential function; $A_{F}$ is used to determine the smoothness between the ZBL and Tersoff potentials; $f_{F}$ is the Fermi-like function of smoothing the ZBL repulsion potential; and $E$ is the total energy of the system.

In addition, for the interaction of metal atoms, the embedded-atom method (EAM), developed by Winey et al., is used to describe the interaction between Al ions [26]:

$$
E_{ij}=\sum_{i} F_{i}\left(\rho_{i}\right)+\frac{1}{2} \sum_{i \neq j} \phi_{i j}\left(R_{i j}\right)
\tag{4}
$$

where $F_{i}(\rho_{i})$ is the atomic embedding energy, representing the energy required for atom $i$ to embed electron density; $\rho_{i}$ is the total electron density around atom $i$; and $\phi_{ij}(R_{ij})$ is the distance-dependent Al atomic pair potential. Dandekar and Shin developed the Morse potential between Al and 3C-SiC based on the potential energy curve obtained by Zhao et al. by using the ab initio method [27,28]. The form is as follows:

$$
E_{i j}=D_{0}\left[e^{-2 \alpha\left(r_{i j}-r_{0}\right)}-2 e^{-\alpha\left(r_{i j}-r_{0}\right)}\right]
\tag{5}
$$

where $r$ represents the distance between particle pairs; $r_{0}$ is the equilibrium bond length; and $D_{0}$ and $\alpha$ represent the depth and width of the potential well, respectively. $D_{0}$, $\alpha$, and $r_{0}$ of Al and C are 0.4691 eV, $1.738 \AA^{-1}$, and $2.246 \AA$, respectively. $D_{0}$, $\alpha$, and $r_{0}$ of Al and Si are 0.4824 eV, $1.322 \AA^{-1}$, and $2.92 \AA$, respectively.

### 2.2. Defect Statistics
The Wigner-Seitz (WS) analysis method was considered to calculate the change in the number of point defects before and after ion implantation and annealing, which is believed to accurately extract various point defects, and we needed two configurations of the atomic model as inputs as follows: the reference configuration and the displacement configuration. For the reference configuration, we selected the model before implantation and defined the position of the atoms in the crystal without defects. The initial sites of the atoms were divided by three-dimensional Voronoi space, and each atom was precisely assigned to a site. Displacement configuration is the configuration that needs to be analyzed and often contains some point defects such as vacancies, interstitials, and antisites. Eventually, some sites may not be occupied by atoms at all, which are called vacancies. Other sites may be occupied by multiple atoms, which are called interstitials, and the sites occupied by the atoms that are not the original ones are antisites. However, the error of this method in identifying point defects increases with significant changes in the volume of the system, as many atoms are almost removed from the original site of the reference configuration due to the expansion or contraction of the volume.

Next, we combined the identify diamond structure (IDS) method to visualize the defect steps further, considering that the WS method could be affected by the volume of the system [29]. The atoms of cubic diamond and hexagonal diamond structures indicate that the first- and second-nearest neighbor lattices are perfect. Specifically, the first-neighbor lattices in both the cubic diamond (first neighbor) and hexagonal diamond (first neighbor) are perfect, but the second-neighbor lattices are damaged. Conversely, atoms of cubic diamond (second neighbor) and hexagonal diamond (second neighbor) structures suggest a perfect second-neighbor lattice with a damaged first-neighbor lattice. If an atom belongs to another structure (none of the structures above), it is highly likely to be a defective atom. We used the IDS method to identify and extract atoms belonging to other structures and their nearby atoms with distances smaller than $5 \AA$ (including their first- and second-nearest neighbors). Then, the WS method was carried out to identify the point defect types in these atoms, thereby significantly reducing the identification error.

### 2.3. DFT Calculation

The DFT calculations using the Perdew–Burke–Ernzerhof (PBE) function are realized by the QUANTUM ESPRESSO software [30]. The ultrasoft pseudopotential (USPP) is selected for Si, and projector augmented wave (PAW) pseudopotentials are applied to C and Al. To facilitate the subsequent transport calculations, we used a $3 \times 5 \times 1$ supercell containing 240 atoms to calculate the defect effects, which is derived from a 16-atom rectangular unit cell. During the crystal force optimization process, the supercell variations are allowed until the force on each atom is smaller than $1 \times 10^{-3}$ Ry/bohr [31]. The energy cutoff of 30 Ry is used in the band structure calculations along the $\Gamma - \text{X} - \text{K} - \Gamma - \text{Y}$ high symmetry direction [12,32].

### 2.4. CI–NEB Calculation

The main purpose of the climbing image–nudged elastic band (CI–NEB) method is to find the minimum energy path (MEP) on the potential energy surface [33]. The highest energy point on the MEP connecting the initial and final states in the chemical reaction and atomic diffusion of solids is called the transition state (TS). We utilized seven images to pinpoint the TS, including the initial and final states. The energy convergence threshold of the images is $1 \times 10^{-6}$ Ry, and the forces convergence threshold is $1 \times 10^{-4}$ Ry/bohr. Additionally, the freezing parameter was set to true in order to halt the optimization when the error in the intermediate states fell below $0.05\ \text{eV}/\mathring{\text{A}}$, thereby enhancing the accuracy and efficiency of the calculations.

### 2.5. MLWF Transformation

Then, the Wannier90 software package was employed to generate a set of maximally localized Wannier functions (MLWFs) to transform the electron wavefunctions [34]. This process enables obtaining the tight-binding (TB) model and determining the hopping parameters between the defect-induced trap levels and the conduction/valence band (CB and VB) states of the defect structures. The trap levels can be induced into the 4H-SiC TB model by expanding and filling the matrix with new lines and rows, with the scattering rates being included in the TB models through the imaginary parts of the corresponding onset energies [35].

### 2.6. Quantum Transport Simulation

In order to investigate the impacts of the Al ion implantation-induced defects on 4H-SiC MOSFET channel transport behaviors, a local 10 nm channel region containing defects was considered (local channel), as shown in Figure 1. Since point defects like the C vacancies and C interstitials in 4H-SiC are highly localized, showing an extension of less than 1 nm [15], a 10 nm channel region containing these point defects is enough to study their local electrical behaviors. The oxide and gate thicknesses are 1 nm and 0.5 nm. To reduce the influence of the gate metal type, the work function of the gate was assumed to be equal to the perfect 4H-SiC crystal. The quantum transport problem was solved by the iterations between Schrodinger's equation in the NEGF form and Poisson's equation using the NanoTCAD ViDES code [36]. The gate voltages $(V_g)$ ranging from 0–6 V were applied, and the drain-to-source voltage $(V_d)$ was set to 0.3 V. The convergence criterion for the equation solution is that the magnitude of the difference in the grid potential vector between adjacent iterations is less than 0.01 V.

![](./images/1019554943180210181_5.jpg)

Figure 1. Schematic illustration of the quantum transport simulation model, in which a local channel region containing defects in 4H-SiC is considered.

## 3. Results and Discussions
### 3.1. Molecular Dynamics Simulations

The study starts from the MD simulations on the Al ion implantation and post-annealing processes. Before the implantation, the local structure of the implantation region only contained cubic diamond and hexagonal diamond atoms, as shown in Figure 2a. Then, the Al ion (red) was injected into the 4H-SiC (0001) plane at 300 K. It can be seen in Figure 2b that near the Al ion, there are many other structure atoms and defect clusters after implantation, indicating that the implantation has caused obvious lattice damage and point defects. After 3300 K high-temperature annealing, the number of other structure atoms decreases obviously, and defect clusters disappear entirely, as shown in Figure 2c. Figure 2d depicts the defect numbers of different types during the MD simulation using the WS and IDS method. The number of point defects increases significantly after the implantation. For example, the number of C vacancies ($V_{\text{C}}$) and C interstitials ($C_{\text{i}}$) are 9 and 7, respectively, while the number of other point defects, like Si replacing C ($Si_{\text{C}}$), C replacing Si ($C_{\text{Si}}$), Si interstitial ($Si_{\text{i}}$) and Si vacancy ($V_{\text{Si}}$), are all less than 4. After the annealing and the atoms cooled to 300 K, the number of $V_{\text{C}}$ and $C_{\text{i}}$ apparently decreased to 3 and 1, respectively. Other types of point defects were almost reduced to zero.

![](./images/1019554943180210181_6.jpg)

Figure 2. Schematic illustration of the MD simulations on the Al ion implantation and post-annealing processes. (a) 4H-SiC Newton layer before implantation. (b,c) 4H-SiC crystal structures after the implantation and annealing. (d) Statistic defect numbers during the two processes.

In order to explore the defect evolution, we extracted the damaged lattice atoms (pink) identified by the IDS method in Figure 3 at the moments just after implantation (0 ps), annealing (300 ps and 600 ps), and after annealing (900 ps). At 0 ps, it had the largest number of damaged lattice atoms and damaged area, in which the damaged atoms gather along the implantation trajectory of the Al ion. Then, they experienced a self-repairing stage

during the annealing (300 ps and 600 ps images), resulting in the continuously reduced damaged area. Finally, the damaged area and the number of damaged lattice atoms became the smallest after 900 ps annealing, which proves that a 3300 K high temperature is appropriate to repair the implantation damage.

![](./images/1019554943180210181_7.jpg)

Figure 3. Defect evolution during 3300 K annealing process.

In both Figures 2 and 3, there are still many defects clustered in the implantation trajectory of Al ion that failed to self-repair after high-temperature annealing. For example, the Al atom fails to perfectly replace Si atoms in this case. To catch all the stubborn defects that are important to 4H-SiC device performance, we repeated the MD simulation 10 times under the same condition. In each case, the Al ion and its nearby point defects were extracted using a supercell, as illustrated in Figure 4a, and Figure 4b–e shows four typical supercell results. It was found that after Al ion implantation and post-annealing, three configurations existed as follows: (i) Al replacing Si (Al<sub>Si</sub>), which is the perfect Al position to induce the p-type doping effect and the majority results in our MD simulations, (ii) Al replacing C (Al<sub>C</sub>), as shown in Figure 4c, and (iii) Al being an interstitial (Al<sub>i</sub>), as shown in Figure 4d. No matter whether the Al ion was perfectly doped, there were always many point defects around, including the frequent Si<sub>C</sub>, V<sub>C</sub>, C<sub>Si</sub>, antisites, C<sub>i</sub>, and unfrequent C-clusters. We also examined the cases under 350 eV and 2 keV implantation energies and 2900 K and 3700 K annealing temperatures. The results indicate that the defects all belong to the above types.

![](./images/1019554943180210181_8.jpg)

Figure 4. Schematic illustration of the implanted Al ion trajectory and the induced point defects in 4H-SiC. (a) The Al ion trajectory. (b–e) The final local crystal environments around Al.

### 3.2. DFT Calculation

The MD results reveal that the Al ion implantation and post-annealing processes will induce a variety of compound defects formed by the coupling of Al ion and point defects. In order to investigate the Al ion-point defect coupling effects, we constructed defect supercell models containing about 240 atoms and different defect types to calculate the electrical properties using the DFT method.

Before the consideration of Al ions, the intrinsic defects in 4H-SiC were studied first. As shown in Figure 5, among these defects, $C_{Si}$ has a negligible impact on the band structure of the perfect 4H-SiC crystal. The band structures of $Si_{C}$ and antisite cases are similar to each other, all showing shallow hole trap levels near the VB. Therefore, it is inferred that these levels are induced solely by the $Si_{C}$. Both $V_{C}$ and $C_{i}$ introduce a mid-gap trap and a shallow electron trap near the CB. They both can affect the transport behaviors by trapping electrons.

![](./images/1019554943180210181_9.jpg)

Figure 5. Band structures of 4H-SiC supercells containing 240 atoms and different point defects.
(a) Perfect crystal supercell. (b-f) Supercells containing $C_{Si}$, $Si_{C}$, antisite, $V_{C}$, and $C_{i}$ defects.

When a Si atom is replaced by an Al ion, the perfect p-type doping is achieved, and the Fermi level goes into the VB edge of 4H-SiC, as shown in Figure 6a. The presence of $C_{Si}$ around $Al_{Si}$ has little impact on the p-type doping properties, as evidenced by the comparison between Figure 6a,c. However, Figure 6b,d illustrate that $Si_{C}$ and antisite around $Al_{Si}$ will induce additional trap levels near the VB. Although they maintain the p-type characteristic of the system, the free holes released by Al doping are trapped and will not contribute to the currents when bias is applied. It is also noted that these trap levels can be solely attributed to the $Si_{C}$. In contrast, as shown in Figure 6e,f, the $V_{C}$ and $C_{i}$ directly transform the system into an n-type property due to the half-filled trap state near the CB edge, which pins the Fermi level. Additionally, the C-cluster defect induces a near-neutral condition, with the half-filled trap levels located at the mid-gap in Figure 6g. The different defect couplings around $Al_{Si}$ may cause opposite doping effects, which greatly affects the doping results during the device manufacturing process.

When the Al substitutes for the C lattice site, it does not produce a doping effect but introduces three closely spaced trap levels in the mid-gap, as shown in Figure 7a. Meanwhile, Figure 7c illustrates that the presence of $C_{Si}$ leads to a downward shift of the two electron-occupied trap levels, indicating that their abilities to trap electrons during electron transport are weakened. When $Si_{C}$, antisite, and $V_{C}$ appear around $Al_{C}$, as indicated by Figure 7b,d,e, an additional trap level is induced. Moreover, the highest half-filled trap level pins the Fermi level near the VB edge, showing the n-type doping effect.

![](./images/1019554943180210181_10.jpg)

Figure 6. Band structures of 4H-SiC supercells containing 240 atoms and an Al ion. (a) Supercell only containing $Al_{Si}$ doping. (b-g) Supercells containing $Al_{Si}-Si_{C}$, $C_{Si}$, antisite, $V_{C}$, $C_{i}$, and C-cluster coupling defects.

![](./images/1019554943180210181_11.jpg)

Figure 7. Band structures of 4H-SiC supercells containing 240 atoms and an Al ion. (a) Supercell only containing $Al_{C}$ doping. (b-e) Supercells containing $Al_{C}-Si_{C}$, $C_{Si}$, antisite, and $V_{C}$ coupling defects.

When Al becomes an interstitial atom, the system exhibits distinct n-type doping characteristics, which is defined as the self-compensation effect by the previous literature [37]. From the real space deformation charge densities in Figure 8a below, the electron contribution to the system by the $Al_{i}$ is clearly observed. The delocalized electrons are injected into the CB and become free carriers. The presence of $Si_{C}$, $C_{Si}$, and $C_{i}$ defects will not significantly affect the system characteristics, as shown in Figure 8b,c,e. However, when there is an antisite around $Al_{i}$, as shown in Figure 8d, a trap state will be generated near the VB, and the free electrons injected into the SiC system by $Al_{i}$ will be captured, consequently restraining the n-type doping characteristics of the system.

![](./images/1019554943180210181_12.jpg)

Figure 8. Band structures of 4H-SiC supercells containing 240 atoms and an Al ion. (a) Supercell only containing $Al_i$ doping. The real space deformation charge densities near the $Al_i$ are also shown below, with blue and red isosurfaces representing missing and obtaining electrons. (b-e) Supercells containing an $Al_i$ and a $Si_C$, $C_{Si}$, antisite, and $C_i$.

### 3.3. NEB Calculation
When an Al atom replaces a C atom, three deep energy levels will be introduced, which will significantly affect the transport behaviors. However, we find that if an extra $C_i$ is induced near the $Al_C$, as shown in Figure 9a, the Al atom will directly migrate to the interstitial without a barrier, while the C atom will return to the original Al position.

![](./images/1019554943180210181_13.jpg)

Figure 9. Two metastable Al doping states. (a) Energy and structure variations after a $C_i$ move close to an $Al_C$. The $C_i$ will kick out the Al, resulting in an $Al_i$ without an energy barrier. (b) Energy variations during an $Al_i$ compensating a $V_C$. The left and right local structures correspond to two different paths. Note that the energies of (b) are from the NEB calculation, while the energies of (a) are from the Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton algorithm, adopted in the DFT calculation due to the zero-energy barrier.

However, the single $Al_i$ will also introduce a deep level and even lead to a serious n-type doping phenomenon. Therefore, we continued to study its couplings with other defects. It was found that when an $Al_i$ meets a $V_C$ near it, as shown in Figure 9b, it will occupy the vacancy in two almost barrier-free ways. The first one is that the $Al_i$ directly migrates to the $V_C$, resulting in an $Al_C$ and encountering an energy barrier of 0.2 eV. The second path is that the Al replaces the Si, and the Si migrates to the $V_C$, resulting in an $Al_{Si}-Si_C$ coupling and encountering an energy barrier of 0.17 eV. Both results will compensate for the n-type doping effect induced by $Al_i$, which is beneficial to the p-type doping purpose.

It seems that point defect densities are high near the Al from the MD simulation results. Next, we verified if point defects like $V_C$ and $C_i$ can be attracted or directly induced by

Al in 4H-SiC. First, the NEB calculations on the formation energies of generating a $C_i$-$V_C$ pair were carried out. As shown in Figure 10a, it was found that the potential barrier of the $C_i$-$V_C$ pair formation in the presence of Al ion is almost 1 eV lower than that in the perfect 4H-SiC crystal. Moreover, in the presence of Al ion, it provides a metastable state with a repairing barrier of 0.27 eV for the $C_i$-$V_C$ pair, indicating that $C_i$-$V_C$ pairs are easily induced by the Al ion implantation. Next, we calculated the total energies of the supercell structures with different Al-$V_C$ and Al-$C_i$ distances, as shown in Figure 10b,c. There is no doubt that $V_C$ can be attracted by the Al, reducing the system energies of nearly 1 eV. For the $C_i$ cases, the energy variations are complicated, and no obvious relationship can be established between the Al-$C_i$ distance and system energy. From the view of energy, the attraction between Al and $V_C$ also tends to separate the $C_i$-$V_C$ pairs and increase the related defect densities. These microscopic effects all support the contradiction between the electrical activation of the Al ion and the control of the $V_C$ concentration [15].

![](./images/1019554943180210181_14.jpg)

Figure 10. Probabilities of $Al_{Si}$ doping inducing or attracting additional points defects. (a) Energy variations to generate a $V_C$-$C_i$ pair due to the movements of C atoms denoted by the red arrows, with or without an $Al_{Si}$. (b,c) Energy variations along the $Al_{Si}$-$V_C$ and $Al_{Si}$-$C_i$ distances.

### 3.4. Impact of Defects on Carrier Transport of 4H-SiC MOSFET Channel

#### 3.4.1. Couplings between $Al_{Si}$ and Other Defects

The transfer characteristics of the 4H-SiC MOSFETs with only $Al_{Si}$ are shown as green lines in Figure 11a,b. Compared with the perfect channel without any defect and Al ion, the local p-type doping effect is clearly observed at the $Al_{Si}$ channel since the carriers are mainly holes at $V_g = 0$ V. Along the increasing $V_g$, the hole current is reduced rapidly, and then the electron current dominates the transport. To further verify the transport mechanism, the channel density-of-states (DOS) (background color) and current spectrum (pink lines with peaks along the $x$-axis) of the $Al_{Si}$ channel were calculated and shown in Figure 11c,e. The bright DOS regions represent the VB and CB, while the blue dark regions are bandgaps. Since the 0.3 V $V_d$ is applied by setting the Fermi levels of the source and drain regions to $\pm 0.15$ eV, the DOS, located at the $\pm 0.15$ eV transport window, will obtain high probabilities to contribute currents. At $V_g = 0$ V, the VB DOS are closer to the transport window, and a hole current peak is clearly observed, which not only verifies the hole current phenomenon but also shows that the p-type doping has moved up the VB of the local 10 nm channel to become a p-type region. At $V_g = 2$ V, both the CB and VB are moved down, and the CB DOSs are closer to the transport window, resulting in the majority of carriers changing from holes to electrons.

In contrast, the $Al_{Si} + Si_C$ and $Al_{Si} +$ antisite channels do not show much threshold voltage ($V_{th}$) moving behavior, but their hole currents are severely reduced. Taking the $Al_{Si} + Si_C$ channel shown in Figure 11d as an example, the free holes from Al ions are captured by the mid-gap trap levels. Although these levels have already entered the transport window, they can hardly contribute to the currents due to the carrier trapping effect. On the other hand, the $Si_C$ or antisite coupling to $Al_{Si}$ maintains the p-type property of the local channel, and this is the reason that the $V_{th}$ variations are negligible.

![](./images/1019554943180210181_15.jpg)

Figure 11. Transfer characteristics of the 4H-SiC MOSEFT local channels when an AlSi couples with another point defect. (a,b) Transfer characteristic curves of the local channels in log and linear axes. (c-e) DOS of the channels containing AlSi, AlSi + SiC, and AlSi + VC at different $V_g$.

For the AlSi + VC, AlSi + Ci, and AlSi + C-cluster channels, the p-type property of the local channels is flipped completely, and the $V_{th}$ shifts towards the negative x-axis are significant. In Figure 11e, the two bright dots correspond to the two trap levels, as shown in Figure 6e, verifying that the trap levels have been successfully incorporated into the channel transport simulation. Moreover, they exhibit obvious resistance to $V_g$. As shown on the right side, the CB edge (bright line on the top of the two trap states) shows a small peak at the trap position, which will block electron transports, corresponding to the classical Fermi level pinning effect caused by trap states. The pinning effect cannot only cause serious leakage currents at $V_g = 0$ V but can also impede the CB moving downwards at $V_g > 0$ and form electron barriers.

To exclude the potential influences caused by gate oxide thickness and $V_d$, the 4H-SiC MOSEFT local channels with a 3 nm oxide layer and 0.1 V $V_d$ are simulated and shown in Figure 12a,b. When the oxide thickness increases, the gate control ability is weakened. But the defect-induced transport behaviors do not change obviously. The results in Figure 12b are similar, such as that reducing the $V_d$ only leads to some current drops. Therefore, the defect impacts on local carrier transports are persistent in SiC MOSEFT channels. Moreover, the coupling effect of the AlSi + VC + Ci ternary defect is studied in Figure 12c. Clearly, the transport ability is further degraded, indicating that the defect clusters could cause serious local current unbalance, which could be a fatal reason for the device failure.

![](./images/1019554943180210181_16.jpg)

Figure 12. Transfer characteristics of the 4H-SiC MOSEFT local channels. (a) Comparisons between 1 nm and 3 nm thickness gate oxide cases. (b) Comparisons between $V_d = 0.1$ V and $V_d = 0.3$ V cases. (c) Transfer characteristics of the channel containing AlSi + VC + Ci and comparisons with other relevant cases.

### 3.4.2. Couplings between Al$_C$ and Other Defects

Figure 13a,b show the transfer characteristics of the 4H-SiC MOSFET local channels in the presence of Al$_C$ and are coupled with other defects. From Figure 7, Al$_C$ does not contribute to the doping effect, but it induces three mid-gap trap states. These states seriously impede the carrier transport, as the subthreshold swings (SS) of the Al$_C$ and Al$_C$ + C$_{Si}$ channels are obviously enlarged compared with the perfect channel. These phenomena can also be well explained in Figure 13c, as these trap states induce a non-negligible electron barrier at $V_g = 2$ V.

When the Si$_C$ appears near the Al$_C$ in Figure 13d, the channel exhibits a n-type characteristic due to the new trap level showing in the upper panel of the bandgap, leading to the increasing leakage current at $V_g = 0$ V. When an antisite appears near the Al$_C$ in Figure 13e, three of the four trap levels move into the bottom panel of the bandgap, which will not significantly influence the electron transports.

![](./images/1019554943180210181_17.jpg)

Figure 13. Transfer characteristics of the 4H-SiC MOSEFT local channels when an Al$_C$ coupling with another point defects. (a,b) Transfer characteristic curves of the local channels in log and linear axes. (c-e) Calculated density-of-states (DOS) of the channels containing Al$_C$, Al$_C$ + Si$_C$, and Al$_C$ + antisite at different $V_g$.

### 3.4.3. Couplings between Al$_i$ and Other Defects

When an Al ion replaces C, it has already lost the p-type doping effect, as shown above. In Figure 14 below, the doping effect could further be flipped completely if an Al ion became an interstitial in 4H-SiC. When an Al$_i$ locates at the MOSEFT channel, it simultaneously injects electrons into the CB and induces a mid-gap trap level, as shown in Figure 14c. Therefore, the CB is moved close to the transport window, leading to significant leakage currents at $V_g = 0$ V. Under this circumstance, an antisite coupling with the Al$_i$ could relieve the n-type doping effect. As shown in Figure 14d, the antisite coupling causes more trap levels, which can not only trap excessive free electrons but can also prevent the downward movement of CB. However, the n-type doping can hardly be eliminated. Due to its strong ability to destroy the p-type doping effect, it is therefore suggested that the Al$_i$ should be avoided to the maximum extent at the ion implantation and post-annealing processes.

![](./images/1019554943180210181_18.jpg)

Figure 14. Transfer characteristics of the 4H-SiC MOSEFT local channels when an Alᵢ coupling with another point defects. (a,b) Transfer characteristic curves of the local channels in log and linear axes. (c,d) Calculated density-of-states (DOS) of the channels containing Alᵢ and Alᵢ + antisite at different V<sub>g</sub>.

## 4. Conclusions

The Al ion implantation and post-annealing processes were studied using MD simulations in this work. Except for the Al<sub>Si</sub>, the non-ideal Al<sub>C</sub> and Alᵢ were also observed. Moreover, additional point defects caused by the Al ion bombardment also frequently appeared and exhibited tendencies of moving towards the Al ion. The DFT and quantum simulation results show that the Al<sub>C</sub> will cause dense trap levels at the mid-gap of 4H-SiC, and the Alᵢ even leads to an n-type doping effect. When they couple with the additional point defects nearby, more complicated doping and trap levels will be generated, increasing the leakage current and SS, shifting the V<sub>th</sub>, and reducing the carrier mobility. This study provides new theoretical evidence for experiments to explain complex doping results.

Author Contributions: Conceptualization and methodology, Y.L.; software, validation, and investigation, Y.W. and H.L.; resources, C.J.; data curation, Q.S.; writing—original draft preparation, Y.L., Y.W. and H.L.; writing—review and editing, C.J. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by the National Key R&D Program of China (2023YFB3611600), the Science and Technology Innovation Program of Hunan Province (2023RC3112), the Natural Science Foundation of Hunan Province (2022JJ40094), and the Creative Research Groups Program of the National Natural Science Foundation of China (62321003).

Data Availability Statement: The simulation codes are available from the authors upon request.

Conflicts of Interest: The authors declare no conflicts of interest.

## References

1. Kimoto, T.; Watanabe, H. Defect engineering in sic technology for high-voltage power devices. *Appl. Phys. Express* 2020, 13, 120101. [CrossRef]

2. Deng, H.; Wei, S.; Li, S. Review of defect physics and doping control in wide-band-gap semiconductors. *Chin. Sci. Bull.* 2023, 68, 1753–1761. [CrossRef]

3. Puschkarsky, K.; Grasser, T.; Aichinger, T.; Gustin, W.; Reisinger, H. Review on sic mosfets high-voltage device reliability focusing on threshold voltage instability. *IEEE Trans. Electron Devices* 2019, 66, 4604–4616. [CrossRef]

4. Han, L.; Liang, L.; Kang, Y.; Qiu, Y. A review of sic igbt: Models, fabrications, characteristics, and applications. *IEEE Trans. Power Electron.* 2021, 36, 2080–2093. [CrossRef]

5. She, X.; Huang, A.Q.; Lucia, O.; Ozpineci, B. Review of silicon carbide power devices and their applications. IEEE Trans. Ind. Electron. 2017, 64, 8193–8205. [CrossRef]

6. Liu, Y.; Yuan, L.; Sun, C.; Zhang, Y.; Tang, X.; Zhang, Y. Three-dimensional design of a 4h-sic npn lateral phototransistor for micro-pixel in ultraviolet optoelectronic integration. IEEE Trans. Electron Devices 2023, 70, 6399–6405. [CrossRef]

7. Yang, W.; Sun, Y.; Qi, M.; Tang, Z.; Mao, S.; Yuan, L.; Sun, L.; Zhang, Y.; Zhang, Y. Wide temperature range modeling of implanted resistors based on 4h-sic cmos process. IEEE Trans. Electron Devices 2024, 71, 3575–3581. [CrossRef]

8. Fan, Y.; Song, Y.; Xu, Z.; Dong, B.; Wu, J.; Rommel, M.; Zhang, K.; Zhao, J.; Zhu, R.; Li, B.; et al. Molecular dynamics simulation of color centers in silicon carbide by helium and dual ion implantation and subsequent annealing. Ceram. Int. 2021, 47, 24534–24544. [CrossRef]

9. Wachowicz, E.; Ossowski, T.; Kiejna, A. Dft study of stepped 4h-sic{0001} surfaces. Appl. Surf. Sci. 2017, 420, 129–135. [CrossRef]

10. Wellmann, P.J. Review of sic crystal growth technology. Semicond. Sci. Technol. 2018, 33, 103001. [CrossRef]

11. Tsuchida, H.; Kamata, I.; Miyazawa, T.; Ito, M.; Zhang, X.; Nagano, M. Recent advances in 4h-sic epitaxy for high-voltage power devices. Mater. Sci. Semicond. Process. 2018, 78, 2–12. [CrossRef]

12. Huang, Y.; Qian, Y.; Zhang, Y.; Yang, D.; Pi, X. Kick-out diffusion of al in 4h-sic: An ab initio study. J. Appl. Phys. 2022, 132, 015701. [CrossRef]

13. Nipoti, R.; Carnera, A.; Alfieri, G.; Kranz, L. About the electrical activation of 1×1020 cm-3 ion implanted al in 4h-sic at annealing temperatures in the range 1500–1950 °C. Mater. Sci. Forum 2018, 924, 333–338. [CrossRef]

14. Poggi, A.; Bergamini, F.; Nipoti, R.; Solmi, S.; Canino, M.; Carnera, A. Effects of heating ramp rates on the characteristics of al implanted 4h-sic junctions. Appl. Phys. Lett. 2006, 88, 162106. [CrossRef]

15. Nipoti, R.; Ayedh, H.M.; Svensson, B.G. Defects related to electrical doping of 4h-sic by ion implantation. Mater. Sci. Semicond. Process. 2018, 78, 13–21. [CrossRef]

16. Hornos, T.; Gali, A.; Son, N.T.; Janzén, E. A theoretical study on aluminium-related defects in sic. Mater. Sci. Forum 2007, 556–557, 445–448. [CrossRef]

17. Wu, J.; Xu, Z.; Liu, L.; Hartmaier, A.; Rommel, M.; Nordlund, K.; Wang, T.; Janisch, R.; Zhao, J. Md simulation study on defect evolution and doping efficiency of p-type doping of 3c-sic by al ion implantation with subsequent annealing. J. Mater. Chem. C 2021, 9, 2258–2275. [CrossRef]

18. Asada, S.; Murata, K.; Tsuchida, H. Modeling of stacking faults in 4h-sic n-type epilayer for tcad simulation. IEEE Trans. Electron Devices 2023, 70, 1757–1762. [CrossRef]

19. Bernstein, N.; Gotsis, H.J.; Papaconstantopoulos, D.A.; Mehl, M.J. Tight-binding calculations of the band structure and total energies of the various polytypes of silicon carbide. Phys. Rev. B 2005, 71, 075203. [CrossRef]

20. Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. J. Comput. Phys. 1995, 117, 1–19. [CrossRef]

21. Stukowski, A. Visualization and analysis of atomistic simulation data with ovito–the open visualization tool. Model. Simul. Mater. Sci. Eng. 2010, 18, 015012. [CrossRef]

22. Berendsen, H.J.; Postma, J.v.; Van Gunsteren, W.F.; DiNola, A.; Haak, J.R. Molecular dynamics with coupling to an external bath. J. Chem. Phys. 1984, 81, 3684–3690. [CrossRef]

23. Ziegler, J.F. Srim-2003. Nucl. Instrum. Methods Phys. Res. Sect. B: Beam Interact. Mater. At. 2004, 219–220, 1027–1036. [CrossRef]

24. Tersoff, J. Modeling solid-state chemistry: Interatomic potentials for multicomponent systems. Phys. Rev. B 1989, 39, 5566–5568. [CrossRef]

25. Biersack, J.P.; Ziegler, J.F. The stopping and range of ions in solids. Ion Implant. Sci. Technol. 1984, 1, 51–108.

26. Jacobsen, K.W.; Norskov, J.K.; Puska, M.J. Interatomic interactions in the effective-medium theory. Phys. Rev. B 1987, 35, 7423–7442. [CrossRef] [PubMed]

27. Dandekar, C.R.; Shin, Y.C. Molecular dynamics based cohesive zone law for describing al-sic interface mechanics. Compos. Part A Appl. Sci. Manuf. 2011, 42, 355–363. [CrossRef]

28. Zhao, H.; Chen, N.; Long, Y. Interfacial potentials for al/sic(111). J. Phys. Condens. Matter 2009, 21, 225002. [CrossRef] [PubMed]

29. Maras, E.; Trushin, O.; Stukowski, A.; Ala-Nissila, T.; Jónsson, H. Global transition path search for dislocation formation in ge on si(001). Comput. Phys. Commun. 2016, 205, 13–21. [CrossRef]

30. Giannozzi, P.; Andreussi, O.; Brumme, T.; Bunau, O.; Buongiorno Nardelli, M.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Cococcioni, M.; et al. Advanced capabilities for materials modelling with quantum espresso. J. Phys. Condens. Matter. 2017, 29, 465901. [CrossRef]

31. Lv, Y.; Tong, Q.; Liu, Y.; Li, L.; Chang, S.; Zhu, W.; Jiang, C.; Liao, L. Band-offset degradation in van der waals heterojunctions. Phys. Rev. Appl. 2019, 12, 044064. [CrossRef]

32. Yan, X.; Li, P.; Kang, L.; Wei, S.-H.; Huang, B. First-principles study of electronic and diffusion properties of intrinsic defects in 4h-sic. J. Appl. Phys. 2020, 127, 085702. [CrossRef]

33. Henkelman, G.; Uberuaga, B.P.; Jónsson, H. A climbing image nudged elastic band method for finding saddle points and minimum energy paths. J. Chem. Phys. 2000, 113, 9901–9904. [CrossRef]

34. Pizzi, G.; Vitale, V.; Arita, R.; Blügel, S.; Freimuth, F.; Géranton, G.; Gibertini, M.; Gresch, D.; Johnson, C.; Koretsune, T.; et al. Wannier90 as a community code: New features and applications. J. Phys. Condens. Matter. 2020, 32, 165902. [CrossRef] [PubMed]

35. Datta, S. Nanoscale device modeling: The green’s function method. Superlattices Microstruct. 2000, 28, 253–278. [CrossRef]

36. Marian, D.; Marin, E.G.; Perucchini, M.; Iannaccone, G.; Fiori, G. Multi-scale simulations of two dimensional material based devices: The nanotcad vides suite. J. Comput. Electron. 2023, 22, 1327–1337. [CrossRef]

37. Huang, Y.; Wang, R.; Zhang, Y.; Yang, D.; Pi, X. Compensation of p-type doping in al-doped 4h-sic. J. Appl. Phys. 2022, 131, 185703. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.