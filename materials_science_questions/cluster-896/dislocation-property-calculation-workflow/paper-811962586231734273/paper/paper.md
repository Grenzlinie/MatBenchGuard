PHYSICAL REVIEW B 76, 144108 (2007)

# Activation enthalpy for kink-pair nucleation on dislocations: Comparison between static and dynamic atomic-scale simulations

David Rodney
Science et Ingénierie des Matériaux et Procédés (UMR CNRS 5266), INP Grenoble, Domaine Universitaire, Boîte Postal 46, 38402 Saint Martin d'Hères, France

(Received 27 June 2007; revised manuscript received 11 September 2007; published 19 October 2007)

We show in the case of a high-Peierls-stress Lomer dislocation in an aluminum crystal that the dependence of the kink-pair activation enthalpy on the stress obtained from static nudged elastic band method calculations agrees with that extracted from dynamical, constant strain-rate simulations. In order to perform the dynamical simulations, we first propose flexible boundary conditions to replace the rigid conditions that are usually applied. This removes the spurious forces on the dislocation that arise because of the mismatch between the elastic strain imposed by the rigid conditions and the plastic strain associated with the dislocation motion. Second, we present a statistical analysis to rigorously extract enthalpy-stress relations from dynamical simulations. We find that the activation enthalpy becomes zero for a stress (which we call the *Peierls stress for kink nucleation*) smaller than that required to move athermally a rigid straight dislocation (called here the *Peierls stress for rigid motion*). This effect may explain the discrepancy often reported in the literature between the Peierls stress predicted by atomistic calculations, determined on short two dimensional dislocations, i.e., the Peierls stress for rigid motion, and the Peierls stress extracted from experiments, which corresponds to that when kink pairs form on three dimensional dislocations without the help of thermal fluctuations, i.e., the Peierls stress for kink nucleation.

DOI: 10.1103/PhysRevB.76.144108
PACS number(s): 61.72.Bb, 62.20.Fe

## I. INTRODUCTION

In crystals such as covalent semiconductors¹ and body-centered-cubic (bcc)²⁻³ or hexagonal-close-packed (hcp)⁴ metals, the Peierls stress,⁵ which reflects the intrinsic resistance of a crystal to dislocation glide, can be as high as 0.5% of the shear modulus. Below this stress, dislocation glide occurs by the thermally activated nucleation and propagation of kink pairs along the dislocation line.⁶ In this regime, the dislocation velocity $v_D$ and also the plastic strain rate $\dot{\gamma}_{plastic}$ (through Orowan’s law $\dot{\gamma}_{plastic}=\rho b v_D$, with $\rho$ the mobile dislocation density and $b$ the Burgers vector) are expected to depend exponentially on the *activation ratio* between the kink-pair activation enthalpy $H$ (a function of the applied stress $\tau$) and the thermal energy,⁷⁸

$$
v_D \propto \dot{\gamma}_{plastic} \propto \exp\left(\frac{-H(\tau)}{k_B T}\right). \tag{1}
$$

The simulation of dislocations at the atomic scale using molecular dynamics (MD) is in rapid development,⁹ but studying thermally activated dislocation glide remains a difficult task, primarily because when the activation ratio increases, the waiting time between kink-pair nucleation events rapidly becomes longer than the time scale accessible to MD simulations, which is limited to only a few nanoseconds. The results obtained up to now with MD concern mainly screw dislocations in bcc crystals and are quite surprising. First, the Peierls stress of straight rigid screw dislocations predicted by interatomic potentials is two to three times higher than the values extrapolated from experiments¹⁰⁻¹³ (the only exception concerns molybdenum modeled via the model generalized pseudopotential theory¹⁴). Similar discrepancies were predicted by density functional theory calculations.¹⁵ Second, the dislocation velocities obtained by stress-controlled MD simulations¹⁶,¹⁷ are high compared to the values expected from experiments. In order to better understand these facts, it would be necessary to choose a computational model (i.e., an interatomic potential, a simulation cell geometry, and boundary conditions) and to compare in this model the activation enthalpies $H(\tau)$ obtained, on the one hand, from static saddle-point search algorithms, such as the nudged elastic band (NEB) method,¹⁸ and those obtained, on the other hand, from the temperature dependence of the velocity-stress relation in Eq. (1) determined from dynamical simulations. This comparison was done for the cross-slip rate of screw dislocation dipoles in face-centered-cubic (FCC) Cu,¹⁹ but not for thermally activated glide since earlier studies focused either on static calculations¹¹,¹⁴,²⁰,²¹ or on dynamical simulations¹⁶,¹⁷,²² with each time different interatomic potentials.

In addition, MD simulations are difficult because the boundary conditions imposed on the borders of the simulation cell influence the long-range stress and strain fields produced by the dislocations. Periodic boundary conditions should always be favored because they avoid the configurational forces related to the relative position of the dislocation in the simulation cell. However, periodicity in all three directions requires us to introduce at least a dipole of dislocations. The two dislocations then interact with one another with a periodic force that depends on their relative position.⁹ Also, in most cases, only one dislocation is of real interest. Breaking the periodicity perpendicularly to the dislocation glide plane allows the introduction of a single dislocation. Two types of boundary conditions are usually applied to the surfaces thus created. They depend on the choice of loading condition to produce the shear stress required to move the dislocation. The first option is *stress-controlled loading associated with free boundary conditions*, whereby external

1098-0121/2007/76(14)/144108(9)
144108-1
©2007 The American Physical Society

shear forces are added to the atoms in the outer surfaces [the latter may either be fully free²³ or constrained to two dimensional (2D) deformation²⁴]. The second option is strain-controlled loading in conjunction with rigid boundary conditions, in which case the atoms in the outer surfaces are displaced to impose a shear strain, the elastic part of which produces the shear stress.²⁵ By incrementing the stress (or strain) at each time step, a dynamical simulation can be performed at constant stress (or strain) rate.

Extracting the activation enthalpy $H(\tau)$ from stress-controlled simulations is computationally expensive because for each stress, several simulations at different temperatures must be performed in order to extract the slope in Eq. (1) between $\ln v_{D}$ and $1/k_{B}T$. Constant strain-rate simulations have recently been performed to study the glide of screw dislocations in bcc Fe.²² At first glance, they appear better adapted to determine activation enthalpies because, from Eq. (1), if the plastic strain rate is constant, the activation enthalpy is proportional to the temperature. This property is well known experimentally²⁶⁻²⁸ and has been used to extract relationships between $H$ and $\tau$ in several high-Peierls-stress crystals.²⁹,³⁰ The method consists in performing constant strain-rate tensile tests at a given rate and different temperatures. From the above proportionality law, each temperature corresponds to an enthalpy $H(\tau)$, where $\tau$ is taken as the flow stress. However, application of this methodology at the atomic scale is not straightforward because, as will be seen in the following, at the time and space scales of MD simulations, neither the plastic strain rate nor the stress is constant with time. In particular, due to the limitation on the simulation cell size, the stress undergoes large drops each time the dislocation advances by one Peierls valley. Domain and Monnet²² proposed a relation between the effective and instantaneous stresses, but to the best of our knowledge, this relation is ad hoc and is not based on any statistical analysis of the dislocation jump process. We will also show in the following that the rigid boundary conditions usually employed in strain-controlled simulations are elastic in nature and can not adapt to plastic strains, leading to spurious forces on the dislocation.

The aim of the present article is a detailed study of the thermally activated glide of dislocations with constant strain-rate loading. We consider here a special type of dislocation, a Lomer dislocation in fcc aluminum, which is well known for being a nonconventional fcc dislocation with a high Peierls stress.³¹ We chose this dislocation as a benchmark, rather than a screw dislocation in a bcc or a hcp crystal because (1) there is no complication related to a nonplanar core and cross slip and (2) interatomic potentials are more realistic in fcc than in bcc or hcp crystals. The outline of the paper is as follows. In Sec. II, we propose boundary conditions that allow for constant strain-rate loading without rigid boundary conditions. In Sec. III, we present static simulations based on the NEB method to determine the enthalpy-stress relation for the Lomer dislocation. Using the same simulation cell, we perform in Sec. IV MD simulations at constant strain rate and determine a methodology to extract the enthalpy-stress relation from these simulations. In Sec. V, we discuss the agreement found between the static and dynamic enthalpies and introduce the distinction between the Peierls stresses for rigid motion, on the one hand, and for kink nucleation, on the other hand.

![](./images/811962586231734273_1.jpg)

FIG. 1. Schematic view of the simulation cell showing in the outer layers in direction $Z$ ($S^{\pm}$). Above and below the cell are shown the displacement profiles in the $Y$ direction due to a dislocation at the center of the cell and its evolution in case of either elastic ($\gamma_{elastic}$) or plastic ($\gamma_{plastic}$) strain increments.

## II. STRAIN-RATE CONTROLLED BOUNDARY CONDITIONS

### A. Simulation setup

We consider the case of a Lomer dislocation in an Al crystal. Atomic interactions are modeled by the embedded atom method (EAM) potential developed by Ercolessi and Adams.³² Lomer dislocations are edge dislocations with an $a/2\langle 110\rangle$ Burgers vector and a $\{001\}$ glide plane. They form in nondissociated junctions between perfect fcc dislocations³³ and are well known for having a high Peierls stress. They have a compact pentagonal-shaped core, as observed in high-resolution transmission electron microscopy³⁴ that is well reproduced by the present potential.³⁵

The simulation cell is schematically shown in Fig. 1. The $X=1/\sqrt{2}[110]$ axis is parallel to the dislocation line, the $Y=1/\sqrt{2}[\overline{1}10]$ axis is parallel to the dislocation Burgers vector, while the $Z=[001]$ axis is perpendicular to the dislocation glide plane. In order to reach long simulated times (6 ns), we used a small simulation cell with $L_{X}$=9.7 nm, $L_{Y}$=14.4 nm, and $L_{Z}$=8.0 nm. Similar sizes were used in Ref. 22. We apply periodic boundary conditions in the $X$ and $Y$ directions, as explained in Ref. 24. Periodicity is broken in the $Z$ direction in order to introduce a single dislocation. The boundary conditions applied in this direction depend on the choice of loading condition to produce a shear stress $\sigma^{YZ}$ to set the dislocation in motion.

A first possible loading condition is stress controlled. External forces in the $Y$ direction are added to the atoms in the outer layers in direction $Z$, noted $S^{+}$ and $S^{-}$ in Fig. 1. The width of these layers is the interatomic potential cutoff radius. The same force is added to all atoms in a given layer. The forces in $S^{\pm}$ are denoted as $F^{\pm}$. They are in opposite directions, and $F^{+}$ is scaled to account for the fact that there are more atoms in $S^{+}$ than in $S^{-}$ because of the extra half-plane of the edge dislocation. If $S$ is the area of the system in $Z$ planes, the applied stress is given by

144108-2

$$
\sigma^{Y Z}=\frac{\sum_{i \in S^{+}} F_{i}^{Y}}{S}=-\frac{\sum_{i \in S^{-}} F_{i}^{Y}}{S}=\frac{N^{+} F^{+}}{S}=-\frac{N^{-} F^{-}}{S}, \quad(2)
$$

where $N^{ \pm}$is the number of atoms in $S^{ \pm}$. Atoms in $S^{ \pm}$must be able to move in order to respond to the application of the external forces, which requires their motion to be either fully free $^{16,23}$ or constrained to a 2D motion in $Z$ planes. $^{24,36,37}$

The second possible loading condition is strain controlled, in which case the atoms in $S^{+}$and $S^{-}$are displaced in opposite directions in order to produce a shear strain $\gamma^{Y Z}$. A similar displacement is imposed to all atoms in a given layer. If we denote $u$ as the displacement in $S^{+}$from a reference configuration (the relaxed dislocation in the absence of external loading), the displacement in $S^{-}$is $-u$ and we have

$$
\gamma^{Y Z}=\frac{1}{L_{Z}}\left(\frac{\sum_{i \in S^{+}} u_{i}^{Y}}{N^{+}}-\frac{\sum_{i \in S^{-}} u_{i}^{Y}}{N^{-}}\right)=\frac{2 u}{L_{Z}}. \quad(3)
$$

This expression is equivalent to computing the shear strain due to the displacement of the centers of gravity of the two layers. With this loading condition, atoms in $S^{ \pm}$must be held in position to impose the strain, requiring fixed boundary conditions. Usually, atomic positions are fixed in all directions, $^{25,38,39}$ although only the constraint in direction $Y$ is required and the motion in directions $X$ and $Z$ could remain free. By increasing the applied strain at each time step in dynamical simulations, the simulation can be performed at a constant strain rate, which is equivalent to imposing a constant velocity to the atoms in $S^{ \pm}$. This type of loading condition is similar to that of most experimental tensile tests. Note, however, that because of the limitations on the computing time, the strain rates imposed in MD are much larger than in experiments $(\sim 10^{7} \mathrm{~s}^{-1}$ compared to $10^{-4} \mathrm{~s}^{-1})$.

In strain-controlled simulations, the internal stress is computed using Eq. (2), where the forces $F_{i}^{Y}$ are now the interatomic forces rather than the Virial stress $^{40}$ because the latter is influenced by surface effects in direction $Z$. Also, in dynamical simulations, the instantaneous stress computed with Eq. (2) undergoes large oscillations, the amplitude of which depends on the temperature and on the simulation cell size. For the present simulations, the amplitude is of the order of 150 MPa with a period of the order of 0.3 ps. In the following, as is customarily done, the stresses are averaged over 2.5 ps in order to eliminate these fast oscillations.

### B. Elastic and plastic strains

The strain rate is composed of an elastic term that produces the stress and a plastic term that is related to the dislocation motion through Orowan's law,

$$
\dot{\gamma}^{Y Z}=\dot{\gamma}_{\text {elastic }}^{Y Z}+\dot{\gamma}_{\text {plastic }}^{Y Z}=\dot{\sigma}^{Y Z} / \mu+\rho b v_{D}, \quad(4)
$$

where $\mu$ is the shear modulus, $\rho=1 / L_{Y} L_{Z}$ the dislocation density, $b$ the Burgers vector, and $v_{D}$ the instantaneous dislocation velocity.

To illustrate the two possible natures of the strain, consider in Fig. 1 the displacement profiles in $S^{ \pm}$in the presence of a dislocation at the center of the cell. They are shown schematically above and below the cell and correspond to displacements in the $Y$ direction. The profiles approximately follow inverse tangents, and in the absence of applied stress or strain, the displacement in $S^{+}(S^{-})$goes from about $+b / 2$ $(-b / 2)$ on the $Y<0$ side to about 0 on the $Y>0$ side.

An elastic strain corresponds to additional atomic displacements in $S^{ \pm}$given by $\pm u= \pm \gamma^{Y Z} L_{Z} / 2$, according to Eq. (3). An elastic strain appears in Fig. 1 as a homogenous shift of the displacement profiles toward higher absolute values. By way of contrast, a plastic strain is produced when the dislocation moves in the simulation cell. As illustrated in Fig. 1, it corresponds to a shift of the displacement profile in the glide direction in order to follow the position of the dislocation. The plastic strain, which is related to the incremental area below the displacement profiles, is inhomogeneous and localized above and below the dislocation position, in contrast with the elastic strain which is homogeneous in the layers.

In all constant strain-rate MD simulations performed to date, the upper and lower layers were displaced homogeneously with the same displacement for all atoms in each layer. This loading is thus elastic in nature, and when the dislocation starts to move, the displacement profiles in $S^{ \pm}$cannot follow the dislocation in its motion. This mismatch induces a configurational force on the dislocation that depends on its position in the simulation cell. As a consequence, the internal stress, which has to balance the configurational force in order to maintain a constant average dislocation velocity, also varies periodically with the dislocation position. As will be seen in the next section, the amplitude of stress variation may be large, making it impossible to define straightforwardly an effective stress during the glide process.

The methodology proposed by Osetsky and Bacon $^{25}$ is particular because the atoms in $S^{ \pm}$have a displacement that varies linearly in the outer layers, instead of the inhomogeneous displacement profiles shown in Fig. 1. The plastic strain is then consistent with a homogeneous shift of the profiles and can be applied by rigid boundary conditions without configurational forces. On the other hand, the mismatch between the imposed profile and the equilibrium displacement field of the dislocation strongly affects the dislocation structure in small simulation cells. Their methodology should therefore be used only in large cells.

### C. Flexible boundary conditions

Our aim is to apply strain-controlled boundary conditions while allowing for relaxations in the outer layers, such that the displacement profiles in these layers can adapt to the motion of the dislocation. We propose the following method. To perform a dynamical simulation at a constant strain rate $(\dot{\gamma}_{0})$, we first ensure that the average initial thermal velocity in direction $Y$ is zero in both layers. We then add to the atomic velocities in $S^{ \pm}$the velocities $\pm v= \pm \dot{\gamma}_{0} L_{Z} / 2$, which are thus the initial velocities of the centers of mass of the layers. At every time step, we then impose that the total force in direction $Y$ in the slabs $S^{ \pm}$is zero by subtracting off the average force in each layer. In $S^{+}$, we have

![](./images/811962586231734273_2.jpg)

FIG. 2. (Color online) Stress-strain relations during constant strain-rate simulations $(\dot{\gamma}_0=5 \times 10^{-5}\ \text{ps}^{-1})$ at 200 K with rigid (red) and flexible (black) boundary conditions. The dashed vertical lines indicate when the dislocation is at the center of the cell. For this test simulation, a short dislocation ($L_Y$=2 nm) was simulated.

$$
F_{i}^{Y} \equiv F_{i}^{Y}-\sum_{j \in S^{+}} F_{j}^{Y} / N^{+}, \tag{5}
$$

and we have the same in $S^{-}$. Forces and displacements in directions other than $Y$ are left unconstrained.

Since the total force in direction $Y$ in $S^{\pm}$ is zero at every time step, the centers of mass retain their initial velocity throughout the simulation, and according to Eq. (3), the simulation cell is sheared at a constant strain rate $\dot{\gamma}_0$. At the same time, atoms in $S^{\pm}$ still interact with one another, thus allowing for relaxations inside the layers. This flexible boundary condition leads to both elastic and plastic strains, the partition between them evolving spontaneously according to the dislocation motion. We should note that subtracting off the average forces in the outer layers is equivalent to applying to the system fictitious forces at every time step. These forces may produce a work that influences the energy and the temperature of the cell. However, in the following simulations, no temperature change was detected.

As a test, we compare in Fig. 2 the stress-strain curves obtained with either rigid or flexible boundary conditions. Both simulations start by an elastic regime during which the dislocation is immobile and the stress increases linearly. As expected, the two simulations are equivalent in this regime. The dislocation starts to glide when the stress reaches about 450 MPa. When rigid boundary conditions are used, the stress varies periodically with the position of the dislocation in the simulation cell. The amplitude of the variation is large, about 300 MPa. By way of contrast, with the flexible boundary conditions that adapt to the plastic strain, the stress varies around a well-defined average value. The serrations that remain on the stress-strain curve are associated with dislocation jumps from one Peierls valley to the next. They are analyzed in Sec. IV.

### III. ACTIVATION ENTHALPY FROM STATIC SIMULATIONS

We determined the activation enthalpy for kink-pair nucleation as a function of applied stress using the NEB method. $^{18}$ A chain of replicas is constructed between a reactant (the dislocation in a Peierls valley) and a product (the dislocation in the next Peierls valley). The replicas are linked in phase space by springs between first neighbors along the path. The energy of the path is minimized by relaxing the forces due to the atomic interactions perpendicularly to the path and relaxing the forces on the springs between replicas parallel to the path. We used an improved tangent calculation $^{41}$ and a climbing NEB procedure $^{42}$ at the end of the relaxation process to determine more precisely the configuration of maximum energy, which is the activated state. Since stresses are applied with this method and not strains, we used a stress-controlled loading with free boundary conditions in $S^{\pm}$. The NEB method has previously been used in the context of dislocations to determine the activation energy for kink-pair nucleation on a threefold extended screw dislocation in bcc Fe (Refs. 20 and 21) and for cross slip of a screw dislocation in fcc Cu. $^{19,43}$

The activated state corresponds to a critical kink pair. It is close to the reactant along the path which mostly consists of the extension of the kink pair along the dislocation line. We employed 20 replicas and a spring constant of 0.1 eV $\mathring{\text{A}}^{-1}$. The path was relaxed using a projected algorithm $^{18}$ with a time step of 10 fs. Relaxation was considered achieved when the maximum force on any atom along the path was less than 0.01 eV $\mathring{\text{A}}^{-1}$, which was typically reached within 100 steps. We used two different initial paths. Both consisted of an expanding kink pair, but in one case, the extension increased linearly along the path while in the other case, it increased quadratically in order to have initially a higher density of replicas near the reactant. Both initial paths led to similar results.

The result is shown in Fig. 5 as open squares. In this figure, the static data are compared with dynamic ones (filled diamonds) that are presented in next section. The kink-pair formation energy at zero applied stress is $H_{KP}$=0.41 eV. The Peierls stress for rigid motion, $\tau_{P}$=1600 MPa, was determined by performing a static simulation on a short dislocation at increasing applied stress and was defined as the lowest stress for which the straight dislocation advanced by at least one Peierls valley. The enthalpy obtained here is below 0.033 eV for stresses larger than 1000 MPa. We checked the influence of the dislocation length, $L_Y$, which sets an upper bound for the size of the activated kink pair, by using a cell twice longer in direction $Y$ and obtained an enthalpy curve identical to the one shown here.

### IV. ACTIVATION ENTHALPY FROM DYNAMICAL SIMULATIONS

#### A. Stress-strain curves

We performed constant strain-rate simulations at different temperatures using the flexible boundary conditions proposed in Sec. II. The imposed strain rate was $\dot{\gamma}_0$=1.5 $\times 10^{-5}\ \text{ps}^{-1}$, and the duration of the simulations was set to 6 ns for all temperatures. Since the dislocations travel limited distances during the simulations, no thermostat was needed. Figure 3 shows examples of stress-strain curves and time evolutions of the dislocation position at different tem-

![](./images/811962586231734273_3.jpg)

FIG. 3. (a) Stress-strain curves and (b) position of the dislocation during constant strain-rate $(\dot{\gamma}_{0}=1.5 \times 10^{-5} \mathrm{ps}^{-1})$ simulations at different temperatures. The dashed lines in (a) are the average jump stresses. The dashed line in (b) indicates the average dislocation velocity predicted by Orowan's law.

peratures. In all cases, the simulation starts with an elastic regime, during which the dislocation is immobile at the bot- tom of a Peierls valley and the stress increases linearly with the strain at a rate $\dot{\tau}_{0}=\mu \dot{\gamma}_{0}$ , in agreement with Eq. (4). When the stress reaches a critical value, the dislocation undergoes a first jump from its initial Peierls valley to the next. It pro- duces a plastic strain given by Orowan's law: $\Delta \gamma_{P}=\rho b d$ , where $d$ is the distance between Peierls valleys. In the case of Lomer dislocations, $d=b$ . After nucleation, the kink pair expands rapidly along the dislocation line (or, more pre- cisely, the duration of expansion, $\sim 10 ps$ , is shorter than the characteristic time $\Delta \gamma_{P} / \dot{\gamma}_{0} \sim 60 ps$ ). We see from Eq. (4) that an instantaneous plastic strain increment leads to a stress drop $\Delta \tau=\mu \Delta \gamma_{P}$ . With the present parameters $(\mu \sim 35 GPa$ , $b=d=0.2851 ~nm, \ \rho=1 / L_{Y} L_{Z}=10^{-2} ~nm^{-2})$ , we have $\Delta \tau$ =30 MPa, which is consistent with the serrations visible in Fig. 3(a). The rest of the simulation is composed of elastic periods during which the stress increases linearly, separated by plastic events marked by stress drops when the disloca- tion changes the Peierls valley. As seen in Fig. 3(b), the dislocation usually advances by one Peierls valley at a time. In some instances, however, such as around $1.5 ~ns$ at $100 ~K$ , the dislocation may jump over several valleys in one plastic event. Such events have a low frequency and are neglected in the following analysis. Finally, we see from Fig. 3(b) that the dislocation adopts an average velocity given by Orowan's law: $\langle v_{d}\rangle=\dot{\gamma}_{0} / \rho b=6 \times 10^{-3} ~nm ps^{-1}$ . This equality is verified because the stress in the cell varies around an average con- stant value, such that, according to Eq. (4), the average elas- tic strain rate is zero and the average plastic strain rate is equal to the imposed strain rate. As will be emphasized in the next section, this relation is only true on the average due to the intermittent motion of the dislocation.

## B. Stochastic jump process
The question now is: Can we extract the relation between the enthalpy $H$ and the stress $\tau$ from these dynamical simu lations? The difficulty comes from the fact that the stress is not constant and the activation enthalpy changes continu- ously, such that we cannot use a priori the proportionality law between enthalpy and temperature mentioned in the In- troduction. In order to gain insights into the jump process, we use the following stochastic model. We consider a dislo- cation in a medium deformed at a constant strain rate. When the dislocation is immobile, the stress $\tau$ increases at a rate $\dot{\tau}_{0}$ .The dislocation has a jump probability per unit time, $^{7,44,45}$ 

$$p(\tau)=\nu \frac{b}{\ell_{c}} \frac{L_{Y}}{\ell_{c}} \exp \left(\frac{-H(\tau)}{k_{B} T}\right) \equiv \nu^{*} \exp [-\beta H(\tau)], \quad(6)$$

where $\nu$ is a characteristic frequency of the order of the Debye frequency and $\ell_{c}$ is the size of the critical kink pair. The latter decreases with the stress. However, the influence of this variation is small compared to that of the activation enthalpy and will be neglected in the following, where we assume $\ell_{c}=b$ . The relation in Eq. (6) expresses that along a dislocation of length $L_{Y}$ , there are $L_{Y} / \ell_{c}$ potential kink-pair nucleation sites with an activation enthalpy $H$ and an attempt frequency $\nu b / \ell_{c}$ which is the vibration frequency of an elas tic string of length $\ell_{c}$ . If the dislocation jumps, the stress instantaneously decreases by $\Delta \tau=\mu \rho b^{2}$ . Jumps over multiple Peierls valleys are neglected.
We denote $W(\tau, \tau_{i})$ as the survival probability, $^{46}$ i.e., the probability density that, starting at a moment when the stress is $\tau_{i}$ , no jump occurs until the stress is at least $\tau$ . We have

$$\frac{d W}{d t}=-p(\tau) W.\qquad(7)$$

Since, in the absence of jumps, the stress increases lin- early at a rate $\dot{\tau}_{0}$ , we have

$$\frac{d W}{d \tau}=-\frac{p(\tau)}{\dot{\tau}_{0}} W,\qquad(8)$$

which can be formally integrated to express $W$ as a function of the integral of $p$ between $\tau_{i}$ and $\tau$ .
We denote $w(\tau, \tau_{i})$ as the jump probability, i.e., the prob ability density that the first jump occurs at $\tau$ . We have

$$w\left(\tau, \tau_{i}\right)=-\frac{d W}{d \tau}=\frac{p(\tau)}{\dot{\tau}_{0}} \exp \left(\frac{-1}{\dot{\tau}_{0}} \int_{\tau_{i}}^{\tau} p(u) d u\right).\qquad(9)$$

Figure 4 shows jump probabilities at different tempera- tures obtained using the expression for $p$ in Eq. (6), using $\nu=5 ×10^{13} ~s^{-1}, L_{Y}=14.4 ~nm, \ell_{c}=b=0.2851 ~nm$ , and $H(\tau)$ 

![](./images/811962586231734273_4.jpg)

FIG. 4. Jump probability distributions at different temperatures.
The solid curves assume an initial zero stress. The dashed curve is
the distribution at 100 K with an initial stress of 520 MPa, i.e., the
stress of maximum probability $(\tau_{max})$ minus the plastic drop $(\Delta \tau)$
(see text for details).

fitted from the NEB calculation presented in Sec. III. At all
temperatures, the distributions are peaked around a maxi-
mum, $\tau_{max}$, that satisfies

$$
\beta H^{\prime}\left(\tau_{\max }\right)=-\frac{\nu^{*}}{\tau_{0}} \exp \left[-\beta H\left(\tau_{\max }\right)\right].\qquad(10)
$$

The distributions depend very weakly on $\tau_{i}$, as long as it
is below $\tau_{max}$. This can be seen from the above equation
where $\tau_{max}$ is independent of $\tau_{i}$. For comparison, we have
added in Fig. 4 the distribution at 100 K with $\tau_{i}=\tau_{max}-\Delta \tau$.
During the glide process when the dislocation undergoes a
succession of jumps, the first jump occurs at a stress (called
the jump stress) taken from the distribution $w(\tau,0)$. From the
peaked shape of this distribution, this jump stress is close to
$\tau_{max}$. The stress then decreases to about $\tau_{max}-\Delta \tau$. The second
jump stress will sample $w(\tau,\tau_{max}-\Delta \tau)$, which according to
the above remark is essentially the same as $w(\tau,0)$ and has
the same maximum. Jump stresses averaged over multiple
jumps will therefore yield an estimate of $\tau_{max}$.

We now have to extract $H(\tau_{max})$. We show that it is close
to the effective enthalpy $H^{*}$ determined from the average
relation equivalent to Eq. (1): $\dot{\gamma}_{0}=\rho b v_{D}=\rho b d \nu^{*} \exp (-\beta H^{*})$,
i.e., from the expressions of $\Delta \tau$ and $\tau_{0}$,

$$
H^{*}=k_{B} T \ln \left(\frac{\nu^{*} \Delta \tau}{\tau_{0}}\right).\qquad(11)
$$

Replacing the derivative in Eq. (10) by a finite difference,
we have

$$
\beta \frac{H\left(\tau_{\max }\right)-H\left(\tau_{\max }-\Delta \tau\right)}{\Delta \tau} \sim-\frac{\nu^{*}}{\tau_{0}} \exp \left[-\beta H\left(\tau_{\max }\right)\right].\qquad(12)
$$

Using the expressions of $H^{*}$ in Eq. (11), we have

$$
\frac{H^{*}-H\left(\tau_{\max }\right)}{H\left(\tau_{\max }\right)} \sim \frac{\ln \left\{\beta\left[H\left(\tau_{\max }\right)-H\left(\tau_{\max }-\Delta \tau\right)\right]\right\}}{\beta H\left(\tau_{\max }\right)},\quad(13)
$$

which is less than 5% for all practical values of the tempera-
ture and the stress.

![](./images/811962586231734273_5.jpg)

FIG. 5. Activation enthalpy for kink-pair nucleation as a func-
tion of stress obtained from static NEB (open squares) and dynami-
cal (filled diamonds) simulations. The solid line is the fit used in the
statistical analysis.

We conclude from the above analysis that in a MD simu-
lation at a constant strain rate, the average jump stress is an
estimate of $\tau_{max}$ and the corresponding enthalpy $H(\tau_{max})$ can
be approximated by $H^{*}$. The accuracy of these estimates was
checked numerically by simulating the stochastic model with
a Monte Carlo algorithm.

### C. Enthalpy-stress relation

Figure 5 presents the enthalpy-stress curves obtained from
the static NEB method (open squares) and from the dynami-
cal simulations (filled diamonds). As proposed in the previ-
ous section, the effective stress, in the dynamical simulations
was obtained by averaging the jump stresses and the effec-
tive enthalpy is $H^{*}$ computed from Eq. (11). In the expres-
sion of $\nu^{*}=\nu b L_{Y} / \ell_{c}^{2}$, $\ell_{c}$ and $\nu$ are not known with precision.
Assuming $\ell_{c}=b$, a best fit was obtained for $\nu=5 × 10^{13} \mathrm{~s}^{-1}$,
close to the usual estimate of the Debye frequency. Tempera-
tures below 100 K could not be simulated because over-
shoots were then observed; i.e., the stress increased to large
values during the elastic periods, and dislocation jumps came
in avalanches with large stress drops that are outside the
statistical treatment presented above. Temperatures higher
than 300 K could not be simulated either because in this
range, no waiting time could be clearly detected. Figure 5,
with only $\nu$ as a fitting parameter, shows a very good agree-
ment between the static and dynamic results, showing that
the thermally activated motion of the dislocation is captured
by the simple law presented in Eq. (6). This result is further
discussed in next section.

### V. DISCUSSION

We find that the nucleation process is well captured by the
simple thermally activated law in Eq. (6). The latter is con-
sistent with the harmonic transition state theory, $^{47}$ with an
attempt frequency related to the vibrations of the system in
its reactant state since the attempt frequency is that of a set of
independent elastic strings of length $\ell_{c}$ vibrating at the bot-

tom of the initial Peierls valley. Equation (6) has been used in several dislocation dynamics simulations of high-Peierls-stress metals. $^{29,30}$ Interestingly, the estimate used in the dynamical simulations, $H^{*}$ in Eqs. (1) and (11), corresponds to that evaluated experimentally, even though the stress cannot be considered constant in the atomistic simulations. This enthalpy is proportional to the thermal energy, $H^{*}=Ck_{B}T$, but note that because of the high strain rates imposed here, the proportionality coefficient $C$ is significantly smaller in the present simulations than in experiments: 11.3 instead of 20-30 (see, for example, Ref. 28). The scaling of the temperature in MD simulations proposed in Ref. 22 aims also at accounting for this difference when one compares experimental and simulated data.

We considered here the simple case of an edge Lomer dislocation in a fcc crystal, but the agreement between static and dynamical results should hold for other high-Peierls-stress dislocations in other crystalline structures. Consequently, further studies of the thermally activated glide of dislocations may focus only on static activation enthalpies determined from saddle-point search methods $^{48}$ that are more easily computed than their dynamical counterparts, which require long simulations and are limited to a smaller range of stresses, as seen in Fig. 5.

The flexible boundary conditions employed here have been shown to remove the fictitious forces that arise with rigid boundary conditions because the latter are elastic in nature and cannot adapt to plastic deformations. With the flexible boundary conditions, the jump stresses were found to fluctuate around well-defined averages at all temperatures. These boundary conditions can thus be used in all cases to replace rigid boundary conditions and avoid configurational forces. As discussed above, they cannot be used in dynamical simulations at too low temperatures and/or too high strain rates because overshoots are then observed, but the same limitations also apply to rigid boundary conditions. They can be used in static simulations if a force-based energy minimization algorithm is used (such as the projected algorithm used in Ref. 18). For example, the Peierls stress for rigid motion can be determined by applying increments of shear strain, and for each increment, by relaxing the system with the flexible boundary conditions and a zero applied strain rate. The outer layers are thus allowed to relax while the applied shear strain remains constant.

The enthalpy-stress $H(\tau)$ relation shown in Fig. 5 has the particularity of reaching zero for a stress smaller than the Peierls stress for rigid motion. The same result was obtained by Duesbery and Basinski for screw dislocations in bcc potassium. $^{11}$ These authors computed numerically the stress needed to equilibrate a kink pair on a screw dislocation as a function of the separation between kinks. The $H(\tau)$ relation was obtained by integrating the stress-separation relation and subtracting the work done by the stress during the kink-pair expansion. The activation enthalpy thus obtained was added in Fig. 6 [Duesbery-Basinski (DB) data]. It is compared to the present data by scaling the enthalpy by the kink-pair formation energy and the stress by the Peierls stress for rigid motion. As can be seen, the two curves are similar at low stresses. At higher stresses, they slightly deviate, but both reach zero well below the Peierls stress for rigid motion (which corresponds to a scaled value of 1). The present NEB calculations were stopped at a stress of $1000$ MPa $(\sigma/\sigma_{p}$=0.625), above which the calculations gave a zero enthalpy; i.e., the first replica along the NEB path had an energy lower than that of the reactant. We could refine the path between these two configurations to determine a nonzero activation enthalpy, but in any case, the latter will be lower than 0.033 eV, which is small enough to ensure that the dislocation motion is not thermally activated. The threshold enthalpy for athermal glide depends on the temperature and dislocation length. It can be simply estimated from Eq. (6), which gives an average waiting time between jumps equal to $b\exp(H/k_{B}T)/L_{Y}\nu$. The waiting time is thus smaller than the inverse Debye frequency when $H<k_{B}T\ln(L_{Y}/b)$. In typical tensile tests, the dislocation density is $\sim 10^{12}$ m$^{-2}$, yielding an average dislocation length between obstacles $L_{Y}\sim 1/\sqrt{\rho}$ $=10^{-6}$ m and a threshold enthalpy at 300 K equal to 0.2 eV.

![](./images/811962586231734273_6.jpg)

FIG. 6. Comparison between the enthalpy-stress relations obtained with the present NEB calculations on a Lomer dislocation in fcc Al (squares) and on a screw dislocation in bcc Fe with the potential developed by Wen and Ngan in Ref. 20 (squares, denoted as WN potential). Also shown are the data reported in Ref. 11 by Duesbery and Basinski for a screw dislocation in bcc potassium (triangles, denoted as DB data). Enthalpies are scaled by the kink-pair formation energy and stresses by the Peierls stress for rigid motion.

Another published atomic-scale $H(\tau)$ relation concerns screw dislocations in bcc Fe. It was obtained by Wen and Ngan using a modified NEB method. $^{20,21}$ We reproduced their calculations using our implementation of the NEB method and the same EAM potential as in their work $^{20}$ and added the result in Fig. 6 [Wen-Ngan (WN) data]. In agreement with their results, we obtained a zero enthalpy above 1000 MPa. However, we found a Peierls stress for rigid motion equal to 1400 MPa. More precisely, this EAM potential predicts a threefold degenerate core for the screw dislocation, with two critical stresses: When the applied stress reaches a lower critical stress, the dislocation advances by one atomic distance, adopts a metastable configuration, and remains fixed until a second upper critical stress is reached, above which the motion becomes unbounded. Double critical stresses were reported with other potentials. $^{17,49}$ We obtained a lower stress of 1400 MPa and an upper stress of 1900 MPa and identified the Peierls stress for rigid motion with the

former. The data thus obtained are shown in Fig. 6.

In conclusion, we find that in all three cases considered here, the activation enthalpy becomes zero, or at least negli- gible, for a stress, which we call the *Peierls stress for kink nucleation*, well below the Peierls stress for rigid motion. In atomistic simulations, the Peierls stress is usually associated with the crystal resistance to the glide of a straight rigid dislocation and is thus the Peierls stress for rigid motion. On the other hand, in dynamical simulations as well as in experi- mental traction tests, the resistance of the crystal is tested against the motion of a dislocation that may acquire kink pairs. The relevant critical stress in this case is the Peierls stress for kink nucleation above which the kink-pair activa- tion enthalpy is zero or negligible. Although these two criti- cal stresses have not been distinguished up to now, Fig. 6 shows that they are different and that the relative difference, which depends on the interatomic potential, can be as high as 50%. This effect may explain the difference reported be- tween atomistic and experimental estimates of the Peierls stress. $^{10-13,15}$

The main perspective of the present work is to understand the physical origin of the difference between the two critical stresses, that is, to understand how a kink pair may form for negligible energy above a certain stress while the dislocation is still stable in its initial Peierls valley. This effect is not predicted, for example by the line tension model, $^{6,44}$ which is usually employed to model kink-pair nucleation at high stresses. Within this simple model, the nucleation enthalpy becomes zero only at the Peierls stress for rigid motion, and the two critical Peierls stresses are thus equal. Their distinc- tion will certainly involve the three dimensional atomistic structure of the dislocations. We are currently studying sev- eral potentials in different high-Peierls-stress systems in or- der to analyze the factors that govern the shape of the en- thalpy curve.

## ACKNOWLEDGMENTS

The author would like to thank R. Miller for insightful discussions that led to the flexible boundary conditions, C. Marinica for explaining the subtleties of the NEB method, and L. Proville for an ongoing collaboration on thermally activated processes.

$^{1}$H. Alexander, in *Dislocations in Solids*, edited by F. Nabarro (North-Holland, Amsterdam, 1986), Vol. 8, p. 115.
$^{2}$V. Vitek, Cryst. Lattice Defects $\boldsymbol{5}$, 1 (1974).
$^{3}$L. Kubin, Rev. Deform. Behav. Mater. $\boldsymbol{1}$, 244 (1977).
$^{4}$A. Couret and D. Caillard, J. Phys. III $\boldsymbol{1}$, 885 (1991).
$^{5}$R. Peierls, Proc. Phys. Soc. London $\boldsymbol{52}$, 34 (1940).
$^{6}$A. Seeger, Philos. Mag. $\boldsymbol{1}$, 651 (1956).
$^{7}$U. Kocks, A. Argon, and M. Ashby, Prog. Mater. Sci. $\boldsymbol{19}$, 122 (1975).
$^{8}$D. Caillard and J. Martin, *Thermally Activated Mechanisms of Crystal Plasticity* (Pergamon, New York, 2003).
$^{9}$V. Bulatov and W. Cai, *Computer Simulations of Dislocations* (Oxford University Press, New York, 2006).
$^{10}$Z. Basinski, M. Duesbery, and G. Murthy, Acta Metall. $\boldsymbol{29}$, 801 (1981).
$^{11}$M. Duesbery and Z. Basinski, Acta Metall. Mater. $\boldsymbol{41}$, 643 (1993).
$^{12}$K. Ito and V. Vitek, Philos. Mag. A $\boldsymbol{81}$, 1387 (2001).
$^{13}$L. Yang, P. Söderlind, and J. Moriarty, Philos. Mag. A $\boldsymbol{81}$, 1355 (2001).
$^{14}$J. Moriarty, V. Vitek, V. Bulatov, and S. Yip, J. Comput.-Aided Mater. Des. $\boldsymbol{9}$, 99 (2002).
$^{15}$C. Woodward and S. I. Rao, Phys. Rev. Lett. $\boldsymbol{88}$, 216402 (2002).
$^{16}$J. Marian, W. Cai, and V. Bulatov, Nat. Mater. $\boldsymbol{3}$, 158 (2004).
$^{17}$J. Chaussidon, M. Fivel, and D. Rodney, Acta Mater. $\boldsymbol{54}$, 3407 (2006).
$^{18}$H. Jónsson, G. Mills, and K. Jacobsen, in *Classical and Quantum Dynamics in Condensed Phase Simulations*, edited by G. C. B. J. Berne and D. F. Coker (World Scientific, Singapore, 1998), p. 385.
$^{19}$T. Vegge, T. Rasmussen, T. Leffers, O. B. Pedersen, and K. W. Jacobsen, Phys. Rev. Lett. $\boldsymbol{85}$, 3866 (2000).
$^{20}$M. Wen and A. Ngan, Acta Mater. $\boldsymbol{48}$, 4255 (2000).
$^{21}$A. H. W. Ngan and M. Wen, Phys. Rev. Lett. $\boldsymbol{87}$, 075505 (2001).
$^{22}$C. Domain and G. Monnet, Phys. Rev. Lett. $\boldsymbol{95}$, 215506 (2005).
$^{23}$B. D. Wirth, V. V. Bulatov, and T. de la Rubia, J. Eng. Mater. Technol. $\boldsymbol{124}$, 329 (2002).
$^{24}$D. Rodney and G. Martin, Phys. Rev. B $\boldsymbol{61}$, 8714 (2000).
$^{25}$Y. Osetsky and D. Bacon, Modell. Simul. Mater. Sci. Eng. $\boldsymbol{11}$, 427 (2003).
$^{26}$Z. Basinski, Philos. Mag. $\boldsymbol{3}$, 393 (1959).
$^{27}$L. Kubin and B. Jouffrey, Philos. Mag. $\boldsymbol{27}$, 1369 (1973).
$^{28}$D. Brunner and J. Diehl, Phys. Status Solidi A $\boldsymbol{124}$, 455 (1991).
$^{29}$M. Tang, L. Kubin, and G. Canova, Acta Mater. $\boldsymbol{46}$, 3221 (1998).
$^{30}$G. Monnet, B. Devincre, and L. Kubin, Acta Mater. $\boldsymbol{52}$, 4317 (2004).
$^{31}$W. Lomer, Philos. Mag. $\boldsymbol{42}$, 1327 (1951).
$^{32}$F. Ercolessi and J. Adams, Europhys. Lett. $\boldsymbol{26}$, 583 (1994).
$^{33}$D. Rodney and R. Phillips, Phys. Rev. Lett. $\boldsymbol{82}$, 1704 (1999).
$^{34}$M. Mills and P. Stadelmann, Philos. Mag. A $\boldsymbol{60}$, 355 (1989).
$^{35}$M. Mills, S. Murray, and S. Foiles, Ultramicroscopy $\boldsymbol{56}$, 79 (1994).
$^{36}$D. Rodney, Acta Mater. $\boldsymbol{52}$, 607 (2004).
$^{37}$E. Bitzek and P. Gumbsch, Mater. Sci. Eng., A $\boldsymbol{400-401}$, 40 (2005).
$^{38}$T. Hatano and H. Matsui, Phys. Rev. B $\boldsymbol{72}$, 094105 (2005).
$^{39}$R. Schaublin and Y. Chiu, J. Nucl. Mater. $\boldsymbol{362}$, 152 (2007).
$^{40}$D. Tsai, J. Chem. Phys. $\boldsymbol{70}$, 1375 (1979).
$^{41}$G. Henkelman and H. Jónsson, J. Chem. Phys. $\boldsymbol{113}$, 9978 (2000).
$^{42}$G. Henkelman, B. Uberuaga, and H. Jónsson, J. Chem. Phys. $\boldsymbol{113}$, 9901 (2000).
$^{43}$T. Rasmussen, K. W. Jacobsen, T. Leffers, O. B. Pedersen, S. G. Srinivasan, and H. Jónsson, Phys. Rev. Lett. $\boldsymbol{79}$, 3676 (1997).
$^{44}$P. Guyot and J. Dorn, Can. J. Phys. $\boldsymbol{45}$, 983 (1967).
$^{45}$M. Duesbery, Philos. Mag. $\boldsymbol{19}$, 501 (1969).

$^{46}$N. Van Kampen, *Stochastic Processes in Physics and Chemistry* (North-Holland, Amsterdam, 1992).

$^{47}$G. Vineyard, J. Phys. Chem. Solids **3**, 121 (1957).

$^{48}$G. Henkelman, G. Jóhannesson, and H. Jónsson, *Progress on Theoretical Chemistry and Physics* (Kluwer Academic, Dor- drecht, 2000), p. 269.

$^{49}$M. Duesbery, V. Vitek, and D. Bowen, Proc. R. Soc. London, Ser. A **332**, 85 (1973).