ORIGINAL PAPER

# Structural characterization of two-dimensional granular systems during the compaction

S. Živković · Z. M. Jakšić · D. Arsenović · Lj. Budinski-Petković · S. B. Vrhovac

Received: 22 November 2010 / Published online: 7 April 2011
© Springer-Verlag 2011

**Abstract** We examine numerically the density relaxation of frictional hard disks in two dimensions (2D), subjected to vertical shaking. Dynamical recompression of the packing under the action of gravity is based on an efficient event-driven molecular-dynamics algorithm. To quantify the changes in the internal structure of packing during the compaction, we use the Voronoï tessellation and a certain *shape factor* which is a clear indicator of the presence of different domains in the packing. It is found that the narrowing of the probability distribution of the shape factor during the compaction is in accordance with the fact that the packings of monodisperse hard disks spontaneously assemble into regions of local crystalline order. An interpretation of the memory effects observed for a sudden perturbation of the tapping intensity is provided by the analysis the accompanying transformations of disk packings at a “microscopic” level. In addition, we investigate the distributions of the shape factor in a 2D granular system of metallic disks experimentally, and compare them with the simulation results.

**Keywords** Granular compaction · Memory effects · Shape factor · Molecular dynamics

## 1 Introduction

Granular compaction describes the phenomenon in which granular solids undergo an increase in the bulk density as a result of the action of external perturbations, such as shaking and tapping. The focus of the most studies on density relaxation was on the evolution of structural properties as a function of the number of taps applied to the sample. In the pioneering work, Knight et al. [1] showed that the density compaction under tapping follows an inverse logarithmic dependence on the tapping number, $\rho(\infty)-\rho(t)\sim1/\ln(t)$. More recently, Bideau and co-workers [2–4] showed that the compaction dynamics is consistent with the stretched exponential law $\rho(\infty)-\rho(t)\sim\exp[-(t/\tau)^{\alpha}]$. Experimental studies of Lumay and Vandewalle [5] for two-dimensional granular systems suggested that the slow compaction dynamics is related to the crystallization driven by the diffusion of defects. These experimental results have inspired the theoretical studies involving the parking lot model [6–8], the frustrated lattice gas models [9–13], and the one-dimensional lattice models with short-range dynamical constraints [14–16].

Because of the complexity of compaction experiments and some limitations of theoretical approaches, off-lattice models have been implemented in order to reproduce the compaction process [17–19]. These models may have limited application because of not taking into account the friction and other interparticle forces, although it is known that some aspects of granular dynamics are strongly dependent on friction [20,21]. Recently, we carried out the extensive simulations of the compaction dynamics for two-dimensional granular systems subjected to vertical shaking [22]. Unlike to almost all previous models for granular compaction, whose essential ingredient is geometrical frustration, our model is based on realistic granular dynamics. Shaking is modeled by a series of vertical expansion of the disk packing, followed by dynamical recompression of the assembly under the action of gravity. During the second phase of the shake cycle the whole system is reassembled by using the efficient

---

S. Živković · Z. M. Jakšić · D. Arsenović · S. B. Vrhovac (⊗)
Institute of Physics, University of Belgrade, Pregrevica 118, 11080 Zemun, Belgrade, Serbia
e-mail: vrhovac@ipb.ac.rs

Lj. Budinski-Petković
Faculty of Engineering, Trg D. Obradovića 6, 21000 Novi Sad, Serbia

![](./images/811672014904360960_1.jpg)

event-driven molecular-dynamics algorithm. We employed the Walton model [23,24] that captures the major features of granular interactions. The most realistic simulations using e.g. soft particle methods [25], allowing the determination of forces and inter-particle contacts, require much more com- putational power when applied to dense granular systems. It was shown that the compaction dynamics strongly depends on the material properties of the grains. The organization of grains at local level was studied by analyzing the time evolu- tion of connectivity numbers and through the distribution of the Delaunay “free” volumes. Pores have a distribution with a long tail which progressively reduces while the packing gets more compact.

In this paper we pay attention to the numerical study of the behavior of a granular system exposed to discrete taps. We explore the effects of several factors, e.g., the driving acceleration and dissipative properties of the grains, on the local organization of particles. Analysis at the “microscopic” scale is based on the Voronoï tessellation, which allows us to unambiguously decompose any arbitrary arrangement of disks (spheres in 3D) into space-filling set of cells. Our aim is to characterize the structure of disordered disk packings and to quantify the structural changes associated with different densities. Voronoï diagrams are used to visualize the struc- tural order in packing structures during the compaction pro- cess. Quantitative information on the type of order induced can be obtained by calculating the *shape factor* of the Voron- oï cells. The shape factor and its distribution was introduced in [26] for tracking the change in structure as a liquid-like system approaches a disordered jammed state. The shape fac- tor is a dimensionless measure of deviation of the Voronoï cells from circularity. Distribution of the shape factor clearly indicates the presence of different underlying substructures (domains) in the packing.

The phenomenology of the vibrated granular materials is very rich, showing many characteristic glassy behaviors. Here we will focus on one of them, namely on the response of the granular system to sudden perturbations of the “effec- tive temperature” given by the vibration intensity. It has been shown that, during the compaction, the response in the evo- lution of the density to a change in the vibration intensity or shear amplitude at a given time, is not determined by the den- sity at that time [27,28]. Our goal is to study the link between the macroscopic dynamics and the microscopic structure of the packing during the short-term memory effect.

Finally, we use the simple experimental set-up [29] to study the arrangement of granular particles in an experimen- tally realized packings in two dimensions. We image a rectan- gular region containing more than 4,500 metallic disks with a resolution of each disk position to better than 0.01 disk diameters. To validate the simulation results, we measure the probability distribution of the shape factor experimen- tally for various packing fractions. A quite good agreement between the experiment and the simulation is observed when the grains are modeled with the values of material parameters corresponding to the values for hard metal surfaces.

In Sec. 2 we summarize the most important features and technical details that are relevant to our numerical simulation. A more detailed description of our model can be found in Ref. [22]. The results of numerical simulation are presented in Sec. 3. In Sec. 4 we describe the experimental procedures and compare the simulation results to the experimental ones. In the last section, we draw some conclusions.

## 2 Simulation method

We present the event-driven molecular dynamics simulations in two dimensions on a model system of $N = 1,000$ mono- disperse, frictional hard disks of diameter $d$ and mass $m$, under the influence of gravitational acceleration $g$. The sys- tem is spatially periodic in the $xy$ plane (gravitational field acts along the negative $y$ direction), with a unit cell of width $L = 1$, and is bounded in the $y$ direction by a rough bed at the bottom and an open top.

One “shake cycle” of the granular assembly, which mod- els the effects of a vibration cycle in a real powder is decom- posed in two stages. First, the effect of a single tap applied to a disk packing is idealized by lifting the entire disk assembly from the floor proportionally to factor $\xi$. A disk at height $y$ is raised to a new height $y'=(1+\xi)y$. The parameter $\xi$ in our model plays a similar role as the shaking acceleration $\Gamma$ in real experiments ($\Gamma$ is defined as the ratio of the peak acceler- ation of the tap to the gravitational acceleration $g$). Philippe and Bideau [19] have suggested that the expansion factor $\xi$ should be proportional to the square of the experimentally controlled parameter $\Gamma$.

At the beginning of the second phase of the shake cycle, we give a random initial velocity to each disk, in such a way that the total momentum is equal to zero. Let $\langle\Delta E_p\rangle$ denote the average increment of the potential en- ergy per disk during the vertical expansion of the disk pack- ing. Initial linear and angular velocities are chosen randomly from a uniform distribution in the intervals $[-2v_T, 2v_T]$ and $[-2\omega_T, 2\omega_T]$, respectively, where $v_T = [2\langle\Delta E_p\rangle/m]^{1/2}$, $\omega_T = [2\langle\Delta E_p\rangle/I]^{1/2}$, and $I$ is the moment of inertia about the center of disk.

The second part of the shake cycle is the formation of static granular pack in the presence of gravity. The packing is compressed and stabilized in a uniaxial external field, using an event-driven algorithm [30]. In the event driven method the disks follow an undisturbed motion, under the influence of gravity, until either the collision of two disks or the col- lision of one disk with the wall occurs. In order to proceed from one collision to the next, a search of all upcoming colli- sions, and the time required for collisions to occur, is made.

![](./images/811672014904360960_2.jpg)

Once the collision pair with the shortest time to the next col- lision is identified, the system is advanced by that amount of time, and the collision is resolved according to the collision rules. Using the velocities just before contact we compute the disks velocities after the contact following Eq. (A1). To prevent an inelastic collapse [31,32], we use a coefficient of restitution which depends on the relative colliding veloc- ity of the particles (see, Eq. (A4)). The disks are assumed to be inelastic with rough surfaces subject to Coulomb fric- tion, so that particle collisions are modeled using the Walton model [23,24]. This model takes into account a reduction of both normal and tangential component of the relative veloc- ity between particles. The collision rules for two disks are summarized in the Appendix A. The collisions with the wall are treated in the same way as collisions between particles, except the wall has infinite mass.

With such an algorithm, in which inelastic collapse does not occur, the potential energy of the system tends towards a constant, while its kinetic energy tends towards zero due to dissipative collisions in the long time limit. In our simula- tions, a disk is considered to be at rest if both translational and rotational kinetic energies of the disk in the last ten collisions fall below the threshold values $E_{tr}^{(t)}$ and $E_{tr}^{(r)}$, respectively. Here $E_{tr}^{(t)}$ and $E_{tr}^{(r)}$ are free parameters that are chosen to optimize the computational method.

The sequence of dissipative collisions during the second phase of a shake cycle brings the system to the state where neighboring disks are very close to contact, i.e., the system locally “solidifies”. In order to accelerate the settlement of the packing, we introduce an additional algorithm to handle the behavior of a disk which suffers successive inelastic col- lisions with another disk which is at rest. A simple algorithm (“detachment” procedure) used to detach one bouncing disk from the surface of the immovable disk was already described in details in the previous paper [22].

The initial state was constructed by inserting the $N =$ 1,000 disks at non-overlapping positions within a rectangu- lar region of width $L = 1$ that extends in $y$ from $y = 0$ to $y = 0.5L$. This dilute column of particles (with pack- ing fraction $\rho = 0.5$, fixing their diameter at $d = 0.01784$) is then allowed to settle down under the influence of grav- ity. This is done by applying the above described method for the formation of static granular pack. Repeated appli- cation of the shaking algorithm builds a sequence of sta- tic packings where each new packing is built from its predecessor.

In the simulations, we describe the roughness of the surfaces and the connected energy dissipation, using the parameters $\mu$ (coefficient of friction) and $\beta_0$ (“roughness coefficient”), as introduced in Appendix A. Further mech- anism of energy loss are the deformation of a particle dur- ing the contact, or the transfer of kinetic energy to thermal energy. We account for those effects, using the coefficient of normal restitution, $\varepsilon$. We used two sets of material parame- ters to analyse the effects of inelastic and friction properties of grains on the compaction dynamics. More dissipative and rough disks (referred hereafter as disks (A)) are characterized by coefficients $\varepsilon_0 = 0.6$ and $\mu = 0.4$, whereas with parame- ters $\varepsilon_0 = 0.9$ and $\mu = 0.2$ we characterize the less dissipative disks (disks (B)). We used the same inelasticity and friction coefficients for grain–grain and grain-wall collisions.

In our model, changing the parameters $\varepsilon$ and $\mu$ affects the relaxation dynamics during the second phase of a shake cycle by increasing the removal rate of kinetic energy. As a consequence, for very dissipative grains the system might be expected to stop readily in the dilute final state. The packing fraction in the system of less dissipative grains (B) is larger than in the system of more dissipative grains (A) prepared by the same number of taps, as more interstitial space is cre- ated by more efficient arch building in the latter case [22]. Therefore, an increase (decrease) in the steady-state density is always associated with decrease (increase) in the number and size of the arches depending on the dissipative proper- ties of grains. Consequently, the choice of material parame- ters plays a substantial role in our model. In our simulation these parameters are adjusted to produce significant changes in the granular compaction characteristics between grains of type (A) and (B). The values of parameters $\varepsilon$ and $\mu$, which correspond to the less dissipative grains (B), are chosen to represent the typical values for stainless steel particles used in our experiment. The values of material parameters for the grains of type (A) correspond to the values for some ceramic materials [32,33].

All of our simulations are run with a fixed diameter of disks $d = 0.01784$, and critical impact velocity $v_0 = 0.02$ (Eq. (A4)) [32] in dimensionless units in which the container width $L$, mass of disks $m$, and gravitational acceleration $g$ all equal unity. In this study, we used very small threshold values $E_{tr}^{(t)} = 5 \times 10^{-5}$ and $E_{tr}^{(r)} = 10^{-6}$ (in dimensionless units). In subsequent presentation of the results on the compaction dynamics time $t$ is measured in number of taps. The results reported here are for $N = 1,000$, although we also increased the system size by a factor of 4 and observed no significant changes in the compaction curves and distributions of the shape factor. Smaller systems ($N < 900$) produced larger fluctuations and slight variations in the density compared to the larger systems.

Both the event-driven and the soft-particle method [25] can handle the packing of large systems. However, these models describe the particle-particle interactions to different levels of complexity. Which of the two methods is to be pre- ferred depends on the problem studied and on the available computational resources. In our study we were repeating the compactification phase of the shake cycle 3,000–5,000 times for each value of parameters $\xi$, $\varepsilon$ and $\mu$, and made the aver- aging over 20–80 independent runs. Therefore we needed an

![](./images/811672014904360960_3.jpg)

efficient algorithm and opted for the event driven one. Our simulations were performed on the parallel cluster computer consisting of 128 Intel processors.

## 3 Results of numerical simulations

In [5] it has been pointed out that the competition between the tendency to form locally compact configurations and the geometrical frustration could be the key for understanding the mechanism of granular compaction. Revealing and quantifying of how space is shared among the grains is an important issue in establishing the nature of their local organization during the compaction. We investigate the correlation between the degree of disorder in the system of grains and the values of packing fraction. For this purpose we use the Voronoï partition and the novel concept of the shape factor to measure the topology of the Voronoï cells during the compaction process in detail.

Voronoï diagrams are a particular case of space tessellation where, given a set of centers, the space is divided according to their "spheres of influence". Formally, for a given two-dimensional set of monodispersed disks, the Voronoï tessellation is a uniquely defined set of space-filling, non-overlapping and convex cells, each of which encloses one and only one of these disks. A Voronoï cell (polygon in 2D) associated with a disk is defined as an assembly of points which are closer to that disk than to any of the other disks in the packing. Two disks sharing a common cell edge are neighbors. Each vertex of this tessellation is equidistant to three neighboring disks. In this work, the Quickhull algorithm [34] is used to compute the Voronoï diagrams for a given set of disks on a plane.

To characterize the Voronoï cells we used the shape factor $\zeta$ (parameter of nonsphericity) defined as

$$
\zeta=\frac{C^{2}}{4 \pi S}, \quad(1)
$$

where $C$ is the circumference of a Voronoï cell and $S$ is its surface [26,35]. Thus a circular structure has a shape factor of $\zeta=1$, while for a convex polygon, the more anisotropic is the polygon, the higher is $\zeta>1$. For a square $\zeta=4 / \pi \approx 1.273$, for a regular pentagon $\zeta=\pi / 5 \tan (\pi / 5) \approx 1.156$, and for a regular hexagon $\zeta=6 / \sqrt{3 \pi^{2}} \approx 1.103$. Generally, for a regular $N$-sided polygon we have $\zeta=(N / \pi) \tan (\pi / N)$, which sets a lower bound for other $N$-sided polygons. The shape factor is able to identify the occurrence of different domains in numerically obtained packings of particles. Every domain is made up of the grains whose Voronoï polygons have similar values of the shape factor. We calculate a shape factor for each Voronoï cell, except for the opened cells located on the boundaries which have incorrectly defined volumes.

In the present paper we report a set of representative results for the temporal evolution of distribution of the shape factor at two different tapping intensities, $\xi=0.7$ and $3.0 \%$. More details about the temporal behavior of the density $\rho(t)$ for various tapping intensities $\xi$ in a range between 0.1 and $5.0 \%$, and about its dependence on material properties of the grains, can be found in Ref. [22]. It was found that the evolution of density toward the steady-state value for $\xi=0.7$ and $3.0 \%$ takes place on different time scales. For these $\xi$ values, the differences in microstructural properties of the packing configurations, such as distributions of Delaunay free volumes were also notable. Among a number of important results, we showed that for values of $\xi$ below $0.5 \%$, density increases over the four decades of simulation time and the asymptotic plateau cannot be achieved in a reasonable simulation time. In the regime of strong tapping intensities, i.e, for values of $\xi$ above $5.0 \%$, density fluctuations are large and the slow relaxation feature disappears.

<table>
<caption>Table 1 Table summarizes the classification of Voronoï polygons into eight groups $G_{1}-G_{8}$ according to the values of the shape factor $\zeta$ (Eq. (1))</caption>
<thead>
  <tr>
    <th>Group</th>
    <th>Range</th>
    <th>Colour</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$G_{1}$</td>
    <td>$\zeta &lt; 1.108$</td>
    <td>Yellow</td>
  </tr>
  <tr>
    <td>$G_{2}$</td>
    <td>$1.108 &lt; \zeta &lt; 1.125$</td>
    <td>Magenta</td>
  </tr>
  <tr>
    <td>$G_{3}$</td>
    <td>$1.125 &lt; \zeta &lt; 1.130$</td>
    <td>Cyan</td>
  </tr>
  <tr>
    <td>$G_{4}$</td>
    <td>$1.130 &lt; \zeta &lt; 1.135$</td>
    <td>Red</td>
  </tr>
  <tr>
    <td>$G_{5}$</td>
    <td>$1.135 &lt; \zeta &lt; 1.140$</td>
    <td>Green</td>
  </tr>
  <tr>
    <td>$G_{6}$</td>
    <td>$1.140 &lt; \zeta &lt; 1.160$</td>
    <td>Blue</td>
  </tr>
  <tr>
    <td>$G_{7}$</td>
    <td>$1.160 &lt; \zeta &lt; 1.250$</td>
    <td>White</td>
  </tr>
  <tr>
    <td>$G_{8}$</td>
    <td>$1.250 &lt; \zeta$</td>
    <td>Black</td>
  </tr>
</tbody>
</table>

For the densities corresponding to the packings obtained in the simulation, the distribution of $\zeta$ diminishes above $\approx 1.30$

In Fig. 1 we show the Voronoï tessellation of packings formed in the simulation with the disks of type (A) and tapping intensity $\xi=0.7 \%$. Diagrams correspond to the packings after $t=$ (a) 2, (b) 8, (c) 15, (d) 30, (e) 50, and (f) 70 shake cycles. In order to clearly distinguish the domains made up of different Voronoï polygons, in Table 1 we classify the polygons according to their $\zeta$ values into eight groups $G_{1}-G_{8}$. Group $G_{1}$ comprises near-regular hexagons, while other groups include less regular figures. To differentiate polygons belonging to different groups $G_{1}-G_{8}$ we use the color coding in accordance with the definitions given in Table 1. This allows us to easily distinguish the local arrangements of grains for the used packings.

In Fig. 1a we observe a mixture of various Voronoï polygons. It is obvious that the figures belonging to class $G_{7}$ dominate, where $G_{7}$ polygons are mostly distorted pentagons and hexagons. It means that the grains are distributed quite randomly and no specific configurations of disks are formed. For $t=8$ (Fig. 1b), only small islands of near-regular hexagons belonging to class $G_{1}$ are found. Moreover, the small

![](./images/811672014904360960_4.jpg)

![](./images/811672014904360960_5.jpg)

Fig. 1 Voronoï diagrams of packings formed in the simulation at dif- ferent stages of compaction. Diagrams correspond to $t=$ (a) 2, (b) 8,(c) 15, (d) 30, (e) 50, and (f) 70 taps. Voronoï cells are colored according to their shape factor $\zeta$ (Eq. (1)). Color coding of the Voronoï polygons is defined in Table 1. These results refer to the disks of type (A). The tapping intensity is $\xi=0.7 \%$

domains made up of $G_{2}$ polygons can also be detected. As the number of taps increases further (Fig. 1c, d), more regular cells can be observed and their occurrence starts prevailing, though the structure of the system is still disordered. There are still a few disordered regions within the packing. After $t=50$ (Fig. 1e) we find large domains made up predomi nantly of more or less regular hexagons (figures belonging to classes $G_{1}$ and $G_{2}$ ). These clusters grow rapidly with a further increase of the number of taps. Ultimately, for the system near or in the steady-state regime, grains end up in configurations where large clusters of near-regular Voronoï cells (class $G_{1}$ ) are found (Fig. 1f). These blocks are clearlyseparated by thin disordered regions made up of Voronoï polygons belonging to the class of more distorted Voronoï cells $(G_{5}-G_{7})$ . The density of the system shown in Fig. 1f is $1.7 \%$ below the steady-state density. After $t=70$ , some vacancy defects disappear and at the end of the compaction the packing evolves to a polycrystalline state, made of many crystalline ordered domains. One salient feature of Fig. 1 is the fact that disks tend to organize themselves locally into close packing configurations during the compaction. At first, such local organization is limited to short distances yielding an overall disordered packing. Optical imaging brings evi- dence that disks tend to form spontaneously ordered hexag- onal patterns. The orientation of the clusters of near-regular Voronoï cells observed in the bulk is not always parallel to the walls, suggesting that the order is not only wall-induced, but nucleates and grows in the bulk.

To further quantify the structural changes in the packings of grains presented above, here we consider the probability distribution $P(\zeta)$ of the shape factor $\zeta$ . The distribution func tion $P(\zeta)$ is related to the probability of finding a Voronoï cell with the shape factor $\zeta$ . It is normalized to unity, namely,
$$\int _{0}^{\infty }d\zeta P(\zeta )=1.$$

Figure 2 shows the temporal evolution of $P(\zeta)$ for the more dissipative disks (A) at two different tapping intensi- ties: (a) $\xi=3 \%$ , and (b) $\xi=0.7 \%$ . In the initial stage of den sity relaxation, the Voronoï diagrams show a lot of cells with irregular rectangular, pentagonal or hexagonal structure (see, Fig. 1a, b), and we thus get a broad distribution $P(\zeta)$ with no significant maxima. The distribution $P(\zeta)$ tends to narrow during the compaction. As the density increases, the distribu- tion becomes more localized around the lowest values of the shape factor (for a regular hexagon, $\zeta=6 / \sqrt{3 \pi^{2}} \approx 1.103$ ). The curves of distribution $P(\zeta)$ are asymmetric with a long tail on the right-hand side, which progressively reduces while the packing structure gets more compact. This narrowing of the probability distribution $P(\zeta)$ corresponds to the decrease of the fraction of Voronoï polygons belonging to classes G5-G7. In other words, the Voronoï cells become more circular at higher values of the packing fraction. As one can see from Fig. 2, the narrowing of $P(\zeta)$ during the

![](./images/811672014904360960_6.jpg)

![](./images/811672014904360960_7.jpg)

Fig. 2 Temporal evolution of the probability distribution $P(\zeta)$ of the shape factor $\zeta$ for the more dissipative disks (A) at tapping intensity. a $\xi=3.0 \%$, and b $\xi=0.7 \%$

![](./images/811672014904360960_8.jpg)

Fig. 3 Temporal evolution of the probability distribution $P(\zeta)$ of the shape factor $\zeta$ for the less dissipative disks (B) at tapping intensity. a $\xi=3.0 \%$, and b $\xi=0.7 \%$

compaction is more pronounced for the larger tapping inten- sity $\xi$, because the compaction dynamics gets faster when the tapping intensity $\xi$ increases.

The probability distribution $P(\zeta)$ is also sensitive to the material properties of the grains. A typical distributions $P(\zeta)$ for the less dissipative disks (B) at two different tapping intensities $\xi=0.7 \%, 3 \%$ are shown in Fig. 3. Here again, the curves of distribution $P(\zeta)$ are asymmetric with a quite long tail on the right-hand side. The tails of such distributions reduce during the compaction more quickly for the system of less dissipative grains (B) than for the system of more dissipative grains (A). Indeed, for the less dissipative disks (B) there is a rapid approach of the system to the steady-state density [22]. Furthermore, for a given tapping intensity $\xi$, the system of disks (B) achieves a larger value of the asymptotic density than the system of disks (A) [22]. Consequently, in the case of disks (B), collective rearrangements of the grains lead to the growth of hexagonal domains [5] and the system ends up in the steady-state configurations where large clus- ters of near-regular Voronoï cells (hexagonal domains) are found. These large solid-like domains are clearly separated by thin disordered regions because rupture occurs inside the compact blocks of grains. We thus get a very narrow prob- ability distribution $P(\zeta)$ centered at $\zeta \approx 1.1$ (the value for regular hexagons).

### 3.1 Memory effects

Here we focus on the response of the granular system to sudden perturbation of the tapping intensity and discuss the accompanying transformations of disk packings at a micro- scopic level. In the simplest compaction experiment [27], the tapping intensity was instantaneously changed from a value $\Gamma_{1}$ to another $\Gamma_{2}$ , after $t_{w}$ taps. For a sudden decrease in $\Gamma(\Gamma_{1}>\Gamma_{2})$ it was observed that on short-time scales the compaction rate increases, while for a sudden increase in $\Gamma$ (Γ₁ < Γ₂) the system dilates for short times. Both results are opposite to what could be expected from the long-time

![](./images/811672014904360960_9.jpg)

![](./images/811672014904360960_10.jpg)

Fig. 4 Time evolution of the packing fraction $\rho(t)$ when the tapping intensity $\xi$ is changed from 3 to $0.5\%$ (dashed line) and from 0.5 to $3\%$ (solid line) at $t_w=30$. The points $A_1$ and $A_2$ correspond to the packings with equal density $\rho(t_w)=0.828$, at $t_w=t_1=30$ and $t_2=39$

behavior at constant $\Gamma$. This behavior is transient, and after several taps the usual compaction rate is recovered.

Figure 4 shows typical memory effects at short times after an abrupt change of the tapping intensity $\xi$. The tapping intensity $\xi$ is switched from 3 to $0.5\%$ and vice versa at $t_w=30$. We observe that after the transient regime the "anomalous" response ceases and there is a crossover to the "normal" behavior, with compaction rate becoming the same as in a constant forcing mode. These results indicate that the system can be found in states, characterized by the same packing fraction $\rho$, that evolve differently under further tapping with the same tapping intensity $\xi$. Both points $A_1$ ($t_1=t_w=30$) and $A_2$ ($t_2=39$) in Fig. 4 correspond to the packings with equal density $\rho(t_w)=0.828$, equal value of $\xi=3\%$, but different further evolution. Their responses to the same tapping intensity $\xi=3\%$ are different: packing $A_1$ becomes looser whereas packing $A_2$ pursues its compaction. In other words, the density evolution after the points $A_1$ and $A_2$ depends not only on the density $\rho(t_w)$, but also on the previous tapping history.

The response in the evolution of the density to a change in the tapping intensity at a given time is accompanied by transformation of the local configurations in the packing. Distributions of the shape factor shown in Fig. 5 correspond to packings having the same density $\rho(t_w)=0.828$. The behavior of distributions $P(\zeta)$ for $A_1$ ($t_w=30$) and $A_2$ ($t_1=39$) packings are globally similar, but the differences are perceptible. For $1.125\lesssim\zeta$, the distribution $P(\zeta)$ for packing $A_2$ is slightly lower than for packing $A_1$. However, for the $\zeta$ less than $\approx1.125$ we observe an opposite effect on $P(\zeta)$. Consequently, the probability distribution $P(\zeta)$ is not unambiguously determined by the density $\rho(t_w)$ and the tapping intensity $\xi$. The memory of the history up to the density $\rho(t_w)$ is encoded in the arrangement of the grains in the packing.

![](./images/811672014904360960_11.jpg)

Fig. 5 Distributions $P(\zeta)$ of the shape factor $\zeta$ for the packings at points $A_1$ (solid line) and $A_2$ (dashed line) in Fig. 4. These distributions correspond to the packings having the same density

## 4 Comparison with experimental results

A comparison between the numerical and experimental results provides insight into the physical accuracy of the numerical model. In this paper we present an experiment that enables the formation of mechanically stable granular packings of various densities and allows the precise detection of individual grains. To make a quantitative comparison, we measure the probability distribution $P(\zeta)$ of the shape factor $\zeta$ for various experimentally generated jammed disordered packings in two dimensions (2D).

The experimental setup was already described in details in the previous paper [29]. We shall therefore present it briefly. Experiments were carried out on a 2D granular medium, i.e., the motion of the grains was confined to a plane. The granular packing is constituted of metallic cylinders contained in a rectangular box made of two parallel glass plates, with an inner gap of thickness 3.4 mm, slightly larger than the height of the cylinders, $h=3.00\pm0.01$ mm. The lateral walls of the box delimit a rectangular frame of height $H=340$ mm and an adjustable width of typically $L=300$ mm. The box is secured on a heavy plane able to be inclined at different rates so that we could set an arbitrary inclination angle $\theta$ from the horizontal. The cylinders of diameter $d=4.00,5.00$, and $6.00\pm0.05$ mm were used to prepare the monodisperse packings containing about 4,500 grains.

Disordered packings are prepared by pouring grains onto an initially horizontal glass plate at once. They are then spread until a flat layer is obtained, where the cylinders are randomly deposited without contact between them. The angle of the plane is then slowly increased up to an angle $\theta=90^\circ$, at constant angular velocity of $\approx5^\circ s^{-1}$. During the plane rotation, grains therefore freely slide downward and reach a mechanically stable state. The measured packing fractions

![](./images/811672014904360960_12.jpg)

of these disordered packings are $\rho = 0.78 - 0.80 \pm 0.01$. Partially ordered packings are obtained by using the same initial procedure followed by the vibration of the inclined plane with a hammer-like device installed below the container. The packing fraction of densely packed systems is $\rho = 0.81 - 0.86 \pm 0.01$. Those densities are far from the close packing limit $\rho_{cp} = \pi/2\sqrt{3} \approx 0.91$. By means of the sample preparation procedure, it was not possible to make packings in the whole range of densities achieved in the simulation runs. This is because for the tapping intensities $\xi$ below $\approx$3%, the steady-state densities exceed $\approx$0.86 [22]. Consequently, we are not able to compare the experimental with simulation results obtained at small tapping intensities $(\xi < 3\%)$ and large times.

The experimental study of collective rearrangements of grains requires to get a precise measurement of the grain positions. For this reason, the granular layer is repeatedly scanned by means of HP Scanjet 3800. The scanner is firmly fixed to the plane narrowly below the bottom glass plate of the rectangular container. The scanner frame covers an area of 210 × 297 mm. The images are systematically acquired in resolution 600 × 600 dpi and 256 gray levels. Both the center and the diameter of each grain are accurately determined using the image processing program based on the Standard Hough Transform (SHT) [36]. In the output bitmap image, the diameters of grains are $d_1 \approx 94$, 118, and 142 pixels. This analysis allows one to detect both the centers and the diameters of cylinders with a high resolution of 0.04 mm.

Let us now compare the simulation results of Figs. 2 and 3 to the experimental ones. We analyze microstructural properties of experimentally generated jammed disordered packings with densities ranging from $\rho_1 \approx 0.78$ up to $\rho_2 \approx 0.86$. Figure 6 illustrates the agreement between the experimental and the numerical results. Experimental results for the distribution $P(\zeta)$ of the shape factor $\zeta$ are given for the packings of disks of diameters $d = 4$ and 6 mm at densities $\rho = 0.829 \pm 0.01$ and $0.828 \pm 0.01$, respectively. From these results we learn that the distribution $P(\zeta)$ does not depend on the diameter of the grains. Also included in Fig. 6 are the results from the numerical simulations for the less dissipative grains (B) in the early stage of granular compaction, at $\xi = 0.7\%$, and 3%. The corresponding packing fractions are close to the experimental ones ($\rho = 0.825$ (0.7%) and $\rho = 0.830$ (3.0%)). Here we see that the agreement between the simulation and the experimental results is very good. Similar degree of agreement has been found for all the experimentally studied values of density. Comparison of Fig. 2a with Fig. 6 shows that the numerical simulations for the more dissipative disks (A) do not fit the experimental results well. It is expected, since the values of $\varepsilon_0$, $\mu$, and $v_0$ which correspond to the less dissipative grains (B) are chosen to represent the typical values for very hard and smooth stainless steel particles used in our experiment [32,33].

![](./images/811672014904360960_13.jpg)

Fig. 6 Simulation (lines) and experimental (symbols) results for the probability distribution $P(\zeta)$ of the shape factor $\zeta$. Experimental results correspond to the packings of disks of diameter $d = 4$ (open square) and 6 (open circle) mm at densities $\rho = 0.829$ and 0.828, respectively. The simulation results correspond to the packings of the less dissipative disks (B) at densities $\rho = 0.825$ ($\xi = 0.7\%$) and 0.830 ($\xi = 3\%$), after the second tap $t = 2$

## 5 Conclusion

In this paper, we have reported some numerical and experimental results concerning the tapped density relaxation in granular media. Our simulation code captures the major features of granular interactions by means of the Walton collision model [23,24]. Based on the event-driven molecular-dynamics algorithm, we prepared the 2D static granular assemblies during the second phase of each shake cycle. A major mechanism of compaction of weakly vibrated granular materials is the gradual collapse of long-lived bridges, resulting in the disappearance of the voids [18,22,37,38]. It must be emphasized that our simulations, through the realistic granular dynamics, ensures the formation of cooperative structures such as arches or bridges [22]. Consequently, our model enables us to study the microstructural transformations of packing during the compaction.

The organization of grains at local level was studied by analyzing the shape factor $\zeta$ (Eq. (1)) of the Voronoï cells. The shape factor $\zeta$ is a quantifier of the circularity of the Voronoï cells associated with the individual particles. It gives a clear physical picture of the competition between less and more ordered domains of particles during the compaction. We found that disks tend to organize themselves locally into ordered hexagonal patterns. It was shown that the probability distribution $P(\zeta)$ of the shape factor $\zeta$ is very sensitive to small structural changes of the packing. The narrowing of distribution $P(\zeta)$ corresponds to the increase of the fraction of near-regular Voronoï cells. These hexagonal domains are clearly separated by the stringlike regions. Recent experiments have

![](./images/811672014904360960_14.jpg)

indicated that the same type of structural organization may occur in a quasi-two-dimensional driven system of hard spheres [39] where regions of crystalline order are interspersed by relatively disordered grain-boundary regions. Our observation indicates that compact clusters of particles are preserved for longer times for the lower tap intensities. During the compaction the grains spend most of the time trapped in localized regions and occasionally exhibit longer displacements [28,40,41]. As the packing progressively densifies, the time which grains spend in a cage becomes longer and longer and grains can only move through the system by cooperative rearrangements of many particles. It is interesting that some models [9,10], which contain the geometrical frustration as an essential ingredient, suggest that the extremely long life time of frozen clusters is responsible for the slow compaction of weakly vibrated granular materials.

Nicolas et al. [42] have studied the compaction of a granular assembly of spheres under a periodic shear deformation, and showed that crystalline arrangements are created in the bulk during the compaction. They have suggested that when the compaction occurs towards crystallization, previously proposed fits, like inverse logarithmic or stretched exponential function, do not provide a satisfactory description of the time evolution of density. Indeed, we have shown that the compaction dynamics in our simulation is consistent with the Mittag-Leffler law [22]. The same relaxation law was also obtained in numerical simulations of compaction by thermal cycling [43].

Memory effects reproduced in the present simulation imply that knowing the density of the packing is not sufficient to predict the behavior of the system under external excitation [27]. We have demonstrated that the packings with the same density, but reached with different compaction procedures, have different distributions $P(\zeta)$ of the shape factor, and consequently respond in a different way to the same tapping intensity. This qualifies the $P(\zeta)$ as a natural candidate for an additional parameter which unambiguously characterizes the macrostate of a granular system with fixed $\rho$ and $\xi$.

The probability distribution $P(\zeta)$ is also sensitive to the material properties of the grains. The agreement between the simulation and the experimental results has been found only for the less dissipative disks (B). Indeed, the set of material parameters $\varepsilon_{0}$, $\mu$, and $v_{0}$, characterizing the collisional properties of disks (B) is chosen to describe the very hard experimental disks.

### Appendix A: collision rules

We briefly recall the collision rules for two disks of diameter $d$, mass $m$ and moment of inertia $I=q m(d / 2)^{2}$. For two disks $\{1,2\}$ with velocities $\{\vec{v}_{1}, \vec{v}_{2}\}$ and angular velocities $\{\vec{\omega}_{1}, \vec{\omega}_{2}\}$, the post-collisional velocities are given by

$$
\begin{aligned}
& \vec{v}_{1}^{\prime}=\vec{v}_{1}+\frac{1}{m} \Delta \vec{P}, \quad \vec{v}_{2}^{\prime}=\vec{v}_{2}-\frac{1}{m} \Delta \vec{P}, \\
& \vec{\omega}_{1}^{\prime}=\vec{\omega}_{1}-\frac{2}{q m d} \vec{n} \times \Delta \vec{P}, \quad \vec{\omega}_{2}^{\prime}=\vec{\omega}_{2}-\frac{2}{q m d} \vec{n} \times \Delta \vec{P},
\end{aligned} \quad \text { (A1) }
$$

where $\Delta \vec{P}$ is the change of linear momentum of particle 1:

$$
\begin{aligned}
\Delta \vec{P}= & -\frac{m}{2}(1+\varepsilon)\left[\vec{n} \cdot\left(\vec{v}_{1}-\vec{v}_{2}\right)\right] \vec{n}-\frac{m}{2} \frac{q(1+\beta(\gamma))}{1+q} \vec{n} \\
& \times\left[\left(\vec{v}_{1}-\vec{v}_{2}\right) \times \vec{n}+\frac{d}{2}\left(\vec{\omega}_{1}+\vec{\omega}_{2}\right)\right].
\end{aligned}
$$

Vector $\vec{n}$ is the unit vector pointing from the center of disk 2 to the center of disk 1.

The inelasticity of collisions between grains is modeled by means of the coefficient of normal restitution $\varepsilon$, defined in the interval $0<\varepsilon \leq 1$. Energy dissipation due to the surface roughness is modeled by an impact angle dependent coefficient of tangential restitution [24]

$$
\beta(\gamma)=\min \left\{\beta_{0},-1-\mu\left(1+\frac{1}{q}\right)(1+\varepsilon) \cot \gamma\right\},
$$

where $\mu$ is the Coulomb friction coefficient and $\gamma$ is the angle between $\vec{n}$ and the relative velocity of the contact points, $\vec{v}_{r}=\left(\vec{v}_{1}-\vec{v}_{2}\right)-$ $(d / 2)\left(\vec{\omega}_{1}+\vec{\omega}_{2}\right) \times \vec{n}$. For all of the simulations in this paper we set $\beta_{0}=0.5$ ("roughness coefficient") [44].

The problem of the inelastic collapse [45,46] is handled by using the normal restitution coefficient $\varepsilon$ dependent on the impact velocity $v=\left|\vec{n} \cdot \vec{v}_{r}\right|$ of the colliding particles [32]:

$$
\varepsilon(v)= \begin{cases}1-\left(1-\varepsilon_{0}\right)\left(v / v_{0}\right)^{1 / 5}, & v \leq v_{0}, \\ \varepsilon_{0}\left(v / v_{0}\right)^{-1 / 4}, & v \geq v_{0}.\end{cases}
$$

The velocity dependent restitution coefficient model (A4) is frequently used to reduce the dissipation in the low velocity regime. It is well known that the TC model [47] allows the simulations in the ranges of density and restitution coefficient where the inelastic hard-sphere model breaks down due to the inelastic collapse. Here, we use the velocity-dependent restitution coefficient and join the two regimes of dissipation (viscoelastic and plastic). For metallic particles [31], when the impact velocity is large $(v>5 \mathrm{~m} / \mathrm{s})$, the colliding particles deform fully plastically. When $v<0.1 \mathrm{~m} / \mathrm{s}$, the deformations are elastic with mainly viscoelastic dissipation. The critical impact velocity $v_{0}$ (Eq. (A4)) depends chiefly on the density of the material and on the details of surface processing. The value $v_{0}=0.02 L / \sqrt{L / g}$ is chosen, throughout the paper, to be similar to the values for hard metal surfaces.

Acknowledgments This work was supported by the Ministry of Science of the Republic of Serbia, under Grants Nos. ON171017 and III45016. The presented work was also supported by the Swiss National Science Foundation through the SCOPES grant IZ73Z0-128169.

### References

1. Knight, J.B., Fandrich, C.G., Lau, C.N., Jaeger, H.M., Nagel, S.R.: Density relaxation in a vibrated granular material. Phys. Rev. E **51**, 3957–3963 (1995)
2. Philippe, P., Bideau, D.: Compaction dynamics of granular medium under vertical tapping. Europhys. Lett. **60**, 677 (2002)
3. Ribière, P., Richard, P., Bideau, D., Delannay, R.: Experimental compaction of anisotropic granular media. Eur. Phys. J. E **16**, 415–420 (2005)
4. Ribière, P., Richard, P., Philippe, P., Bideau, D., Delannay, R.: On the existence of stationary states during granular compaction. Eur. Phys. J. E **22**, 249–253 (2007)

![](./images/811672014904360960_15.jpg)

5. Lumay, G., Vandewalle, N.: Experimental study of granular com- paction dynamics at different scales: grain mobility, hexagonal do- mains, and packing fraction. Phys. Rev. Lett. **95**, 028002 (2005)

6. Kolan, A.J., Nowak, E.R., Tkachenko, A.V.: Glassy behavior of the parking lot model. Phys. Rev. E **59**, 3094 (1999)

7. Talbot, J., Tarjus, G., Viot, P.: Adsorption-desorption model and its application to vibrated granular materials. Phys. Rev. E **61**, 5429–5438 (2000)

8. Talbot, J., Tarjus, G., Viot, P.: Aging and response properties in the parking-lot model. Eur. Phys. J. E **5**, 445–449 (2001)

9. Coniglio, A., Herrmann, H.J.: Phase transition in granular pack- ing. Phys. A **255**, 1–6 (1996)

10. Nicodemi, M., Coniglio, A., Herrmann, H.J.: The compaction in granular media and frustrated Ising models. J. Phys. A Math. Gen. **30**, L379–385 (1997)

11. Nicodemi, M., Coniglio, A.: Aging in out-of-equilibrium dynam- ics of models for granular media. Phys. Rev. Lett. **82**, 916–919 (1999)

12. Barrat, A., Loreto, V.: Response properties in a model for granularmatter. J. Phys. A Math. Gen. **33**, 4401–4426 (2000)

13. Fierro, A., Nicodemi, M., Coniglio, A.: Thermodynamics and sta- tistical mechanics of frozen systems in inherent states. Phys. Rev. E **66**, 061301 (2002)

14. Brey, J.J., Prados, A., Sanchez-Rey, B.: Simple model with facil- itated dynamics for granular compaction. Phys. Rev. E **60**, 5685–5692 (1999)

15. Prados, A., Brey, J.J.: Effective dynamics and steady state of an ising model submited to tapping processes. Phys. Rev. E **66**, 041308 (2002)

16. Brey, J.J., Prados, A.: Closed model for granular compaction underweak tapping. Phys. Rev. E **68**, 051302 (2003)

17. Barker, G.C., Mehta, A.: Vibrated powders: structure, correlations,and dynamics. Phys. Rev. A **45**, 3435–3446 (1992)

18. Mehta, A., Barker, G.C., Luck, J.M.: Cooperativity in sandpiles:statistics of bridge geometries. J. Stat. Mech. Theor. Exp. P10014(2004)

19. Philippe, P., Bideau, D.: Numerical model for granular compactionunder vertical tapping. Phys. Rev. E **63**, 051304 (2001)

20. Nasuno, S., Kudrolli, A., Gollub, J.P.: Friction in granular layers:hysteresis and pre-cursors. Phys. Rev. Lett. **79**, 949–952 (1997)

21. Moon, S.J., Swift, J.B., Swinney, H.L.: Role of friction in pattern formation in oscillated granular layers. Phys. Rev. E **69**, 031301 (2004)

22. Arsenović, D., Vrhovac, S.B., Jakšić, Z.M., Budinski-Petković, L.,Belić, A.: Simulation study of granular compaction dynamics undervertical tapping. Phys. Rev. E **74**, 061302 (2006)

23. Walton, O.R., Braun, R.L.: Viscosity, granular temperature, and stress calculations for shearing assemblies of inelastic, frictionaldisks. J. Rheol. **30**, 949–980 (1986)

24. Herbst, O., Huthmann, M., Zippelius, A.: Dyamics of inelas- tically colliding spheres with Coulomb friction. Granul. Mat-ter **2**, 211 (2000)

25. Cundall, P.A., Strack, O.D.L.: A discrete numerical model for gran-ular assemblies. Geotechnique **29**, 47–65 (1979)

26. Moučka, F., Nezbeda, I.: Detection and characterization of struc- tural changes in the harddisk fluid under freezing and melting con-ditions. Phys. Rev. Lett. **94**, 040601 (2005)

27. Josserand, C., Tkachenko, A., Mueth, D.M., Jaeger, H.M.: Memoryeffects in granular materials. Phys. Rev. Lett. **85**, 3632–3635 (2000)

28. Pouliquen, O., Belzons, M., Nicolas, M.: Fluctuating particle motion during shear induced granular compaction. Phys. Rev.Lett. **91**, 014301 (2003)

29. Jakšić, Z.M., Vrhovac, S.B., Panić, B.M., Nikolić, Z., Jelenk- ović, B.M.: Upward penetration of grains through a granularmedium. Eur. Phys. J. E **27**, 345–356 (2008)

30. Lubachevsky, B.D.: How to simulate billiards and similar sys-tems. J. Comp. Phys. **94**, 255 (1991)

31. Falcon, E., Laroche, C., Fauve, S., Coste, C.: Behavior of one inelas- tic ball bouncing repeatedly off the ground. Eur. Phys. J. B **3**, 45–57 (1998)

32. McNamara, S., Falcon, E.: Simulations of vibrated granu- lar medium with impact-velocity dependent restitution coeffi-cient. Phys. Rev. E **71**, 031302 (2005)

33. Johnson, K.L.: Contact Mechanics. Cambridge UniversityPress, Cambridge, UK (1985)

34. Barber, C.B., Dobkin, D.P., Huhdanpaa, H.: The quickhull algo-rithm for convex hulls. ACM Trans. Math. Softw. **22**, 469 (1996)

35. Richard, P., Troadec, J.P., Oger, L., Gervois, A.: Effect of the anisot- ropy of the cells on the topological properties of two- and three-dimensional froths. Phys. Rev. E **63**, 062401 (2001)

36. Drew, B.: Hough transform. From MathWorld-A Wolfram Web Re- source, created by Eric W. Weisstein. http://mathworld.wolfram.com/HoughTransform.html

37. Pugnaloni, L.A., Barker, G.C.: Structure and distribution of archesin shaken hard sphere deposits. Phys. A **337**, 428–442 (2004)

38. Pugnaloni, L.A., Valluzzi, M.G., Valluzzi, L.G.: Arching in tappeddeposits of hard disks. Phys. Rev. E **73**, 051302 (2006)

39. Berardi, C.R., Barros, K., Douglas, J.F., Losert, W.: Direct obser- vation of stringlike collective motion in a two-dimensional drivengranular fluid. Phys. E **81**, 041301 (2010)

40. Ribière, P., Richard, P., Delannay, R., Bideau, D.: Effect of rare events on out-ofequilibrium relaxation. Phys. Rev.Lett. **95**, 268001 (2005)

41. Marty, G., Dauchot, O.: Subdiffusion and cage effect in a shearedgranular material. Phys. Rev. Lett. **94**, 015701 (2005)

42. Nicolas, M., Duru, P., Pouliquen, O.: Compaction of a granularmaterial under cyclic shear. Eur. Phys. J. E **3**, 309–314 (2000)

43. Vargas, W.L., McCarthy, J.J.: Thermal expansion effects and heatconduction in granular materials. Phys. Rev. E **76**, 041301 (2007)

44. Foerster, S.F., Louge, M.Y., Chang, H., Allia, K.: Measurements ofthe collision properties of small spheres. Phys. Fluids **6**, 1108 (1994)

45. Bernu, B., Delyon, F., Mazighi, R.: Steady states of a column ofshaken inelastic beads. Phys. Rev. E **50**, 4551 (1994)

46. McNamara, S., Young, W.R.: Inelastic collapse in two dimen-sions. Phys. Rev. E **50**, R28 (1994)

47. Luding, S., McNamara, S.: How to handle the inelastic collapse of a dissipative hard-sphere gas with TC model. Granul. Matter **1**, 113–128 (1998)

![](./images/811672014904360960_16.jpg)