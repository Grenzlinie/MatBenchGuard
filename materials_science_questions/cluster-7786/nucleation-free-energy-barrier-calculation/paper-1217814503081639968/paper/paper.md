# Effect of substrate mismatch, orientation, and flexibility on heterogeneous ice nucleation

M. Camarillo, $^{1}$ J. Oller-Iscar, $^{2}$ M.M. Conde, $^{2}$ Jorge Ramírez, $^{2}$ and E. Sanz*$^{1}$

$^{1)}$Departamento de Química Física, Facultad de Ciencias Químicas, Universidad Complutense de Madrid, 28040 Madrid, Spain
$^{2)}$Department of Chemical Engineering, Universidad Politécnica de Madrid, José Gutiérrez Abascal 2, 28006, Madrid, Spain

(*Electronic mail: esa01@ucm.es)

(Dated: 13 January 2026)

Heterogeneous nucleation is the main path to ice formation on Earth. The ice nucleating ability of a certain substrate is mainly determined by both molecular interactions and the structural mismatch between the ice and the substrate lattices. We focus on the latter factor using molecular simulations of the mW model. Quantifying the effect of structural mismatch alone is challenging due to its coupling with molecular interactions. To disentangle both factors, we use a substrate composed of water molecules in such a way that any variation on the nucleation temperature can be exclusively ascribed to the structural mismatch. We find that a one per cent increase of structural mismatch leads to a decrease of approximately 4 K in the nucleation temperature. We also analyse the effect of the orientation of the substrate with respect to the liquid. The three main ice orientations (basal, primary prism and secondary prism) have a similar ice nucleating ability. We finally asses the effect of lattice flexibility by comparing substrates where molecules are immobile with others where a certain freedom to fluctuate around the lattice positions is allowed. Interestingly, we find that the latter type of substrate is more efficient in nucleating ice because it can adapt its structure to that of ice.

## I. INTRODUCTION

Heterogeneous ice nucleation refers to the process by which ice crystals form on surfaces of foreign particles that act as ice-nucleating agents. It is a phenomenon of pivotal importance because it constitutes the main mechanism of ice formation on Earth$^{1}$. The study of heterogeneous ice nucleation is essential for a wide range of fields, including atmospheric science, climate research, biology, cryobiology, and various industrial applications. Advancements in understanding this phenomenon can lead to improved weather forecasting, climate models, cryopreservation techniques, aviation safety measures or artificial snow production$^{2}$.

There is a wide variety of ice nucleating agents$^{3–6}$ such as mineral dust, soot, biological aerosols or organic compounds that act as sites for ice crystal formation in clouds. Many experimental studies have been undertaken to understand and quantify the ice-nucleating ability of these and other particles$^{2,3,7–10}$.

Complementarily, models have been developed to understand and predict experiments$^{5,11–17}$, and simulations$^{18–27}$ are used to unveil key molecular features of ice-nucleating particles. The most common approach is to use realistic potentials for water and for the selected substrate under investigation.$^{10,20–31}$. This strategy enables making predictions directly relevant to experiments$^{20}$, although it requires a reliable substrate-water interaction potential, which is an aspect that has not been carefully taken into consideration.

In this work we trade realism of the substrate for the possibility of shedding light on fundamental questions regarding heterogeneous ice nucleation. In particular, our main goal is to unravel the effect of the mismatch between the ice and the substrate lattices, an issue raised by Turnbull in $1952^{32}$. The difficulty of answering this question lies on the fact that the influence of the mismatch is usually coupled to that of substrate-water interactions$^{8,22,27,33–43}$. To circumvent this problem we use substrates composed of water molecules, a strategy inspired by previous works$^{39,44,45}$. Our approach is similar in spirit to that taken by Mithen et al.$^{44,45}$ where the nucleation ability is probed as a function of the lattice mismatch for a substrate and a liquid both composed of Lennard-Jones particles. Reinhardt et al.$^{39}$ also used this strategy for water, although they mainly focused on the role of interactions and did not perform any quantitative analysis on that of lattice mismatch. In this work, we quantify ice nucleating ability by computing the temperature at which heterogeneous nucleation occurs at a certain rate for substrates with different structural mismatches with ice. We find that the nucleation temperature approximately decreases 4 K when the mismatch between ice and the substrate increases by 1 per cent.

Moreover, we interrogate other fundamental aspects of heterogeneous nucleation such as the effect of lattice flexibility or that of the orientation of the substrate. We analyse the former by comparing the ability to induce ice nucleation of substrates with fixed molecular positions with that of solids composed of molecules that can wander around their lattice sites. In accordance with studies using realistic substrate potentials$^{24}$, we find that flexibility favours nucleation via a mechanism in which stress is shared between the substrate and the emerging ice nucleus. Regarding the lattice orientation effect, we find that the three main ice directions, basal, primary prism (pI) and secondary prism (pII) have a very similar ability to induce ice nucleation, being pI and basal the most and the least efficient nucleants, respectively, by a narrow margin.

Overall, our work leaves aside the complexity found in real systems$^{46}$ to tackle fundamental questions regarding heterogeneous ice nucleation such as the effects of lattice mismatch, orientation and flexibility.

## II. METHODOLOGY

We use the mW water model⁴⁷, whose melting temperature is 273 K⁴⁸. We run our simulations with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) Molecular Dynamics package⁴⁹ in the NVT ensemble. Temperature is kept constant with the Nosé-Hoover thermostat⁵⁰,⁵¹. We integrate the equations of motion using the velocity-Verlet integrator with a 3 fs time step.

<table>
  <tr>
    <th>$L_x$</th>
    <th>$L_y$</th>
    <th>$L_z$</th>
  </tr>
  <tr>
    <td>8.853</td>
    <td>7.671</td>
    <td>7.203</td>
  </tr>
  <tr>
    <th>x</th>
    <th>y</th>
    <th>z</th>
  </tr>
  <tr>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>0.500</td>
    <td>0.000</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>0.250</td>
    <td>0.500</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>0.750</td>
    <td>0.500</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>0.250</td>
    <td>0.167</td>
    <td>0.125</td>
  </tr>
  <tr>
    <td>0.750</td>
    <td>0.167</td>
    <td>0.125</td>
  </tr>
  <tr>
    <td>0.000</td>
    <td>0.667</td>
    <td>0.125</td>
  </tr>
  <tr>
    <td>0.500</td>
    <td>0.667</td>
    <td>0.125</td>
  </tr>
  <tr>
    <td>0.250</td>
    <td>0.167</td>
    <td>0.500</td>
  </tr>
  <tr>
    <td>0.750</td>
    <td>0.167</td>
    <td>0.500</td>
  </tr>
  <tr>
    <td>0.000</td>
    <td>0.667</td>
    <td>0.500</td>
  </tr>
  <tr>
    <td>0.500</td>
    <td>0.667</td>
    <td>0.500</td>
  </tr>
  <tr>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.625</td>
  </tr>
  <tr>
    <td>0.500</td>
    <td>0.000</td>
    <td>0.625</td>
  </tr>
  <tr>
    <td>0.250</td>
    <td>0.500</td>
    <td>0.625</td>
  </tr>
  <tr>
    <td>0.750</td>
    <td>0.500</td>
    <td>0.625</td>
  </tr>
</table>

TABLE I. Sides ($L_x$, $L_y$ and $L_z$) in $\mathring{A}$ and particle coordinates in lattice units (x, y, z) of the ice Ih orthorhombic unit cell equilibrated at coexistence conditions, i. e. 1 bar and 273 K, we use to build our systems.

We generate the substrate coordinates by stretching/compressing an orthorhombic unit cell containing 16 molecules whose lattice parameters correspond to the solid at coexistence conditions (i. e. 273 K and 1 bar). We give in table I the sides of such unit cell and the coordinates of all particles in lattice units. An expanded/compressed unit cell is obtained by multiplying the three directions of the equilibrium unit cell at 273 K by a factor $f$. By replicating the resulting unit cell we obtain the coordinates of a deformed ice see Fig. 1 (left)) whose percent mismatch, $\delta$, is given by:

$$
\delta = 100 \cdot |(f - 1)|. \tag{1}
$$

A central slab of such solid, the substrate region, is kept frozen (orange particles in Fig. 1) and the rest is simulated at 300 K in the NVT ensemble. We apply periodic boundary conditions leaving an empty space along the direction perpendicular to the substrate to melt the outermost layer⁵²,⁵³ (Fig. 1(middle)). The molten region propagates up to the frozen substrate giving rise to an initial configuration (Fig. 1(right)).

The mismatch parameter, $\delta$, is always referred to the unit cell at coexistence conditions. One may consider using the stretching/compressing factor with respect to the equilibrium unit cell at the temperature of interest instead of coexistence. This would be impractical because it would force us to build an initial configuration for every temperature. However, the error made by considering the deformation with respect to the unit cell at coexistence is very small: the ice density only increases by 0.2 per cent from coexistence to the lowest studied temperature, which means that the edges of the unit cell decrease by a factor of 1.00085 ($\delta = -0.085$). With such a small volume variation of the solid with temperature it is definitely not worth considering different unit cells for different temperatures.

![](./images/1217814503081639968_1.jpg)

FIG. 1. Sequence of snapshots illustrating our procedure to generate an initial configuration. Left: Snapshot of a side view of a replicated (and stretched for $\delta$ >0) unit cell in contact with a 15$\mathring{A}$ thick vacuum. Yellow particles correspond to the substrate (exposing the pII plane to the liquid) and blue particles will be melted to give rise to the initial configuration. Middle: At 300 K, a liquid layer is readily formed in the face of the replicated ice lattice in contact with vacuum. Right: At 300 K and in the NVT ensemble the liquid layer propagates up to the substrate surface giving rise to the initial configuration.

We work with two different types of substrate, both composed of water molecules of the same nature as those in the liquid phase: A *rigid* substrate where water molecules are immobile in their lattice positions, and a *wells* substrate where each molecule is given freedom to move within a potential energy well of 2.043 $\mathring{A}$ diameter and $8k_bT$ depth. Details on how we build the well-particle interaction are given in Ref.⁵⁴. The comparison of rigid versus wells substrates enables assessing the role of lattice rigidity on ice nucleating ability.

Due to the presence of a liquid-vapour interface the average pressure of the system is nearly 0 bar, which is essentially equivalent to 1 bar when dealing with condensed phases as we do in the present work. We use NVT instead of NpT simulations for these reasons: (i) a 0 bar pressure is perfectly maintained in the NVT ensemble (ii) it is easier to generate configurations in the NVT ensemble via melting at a free interface as previously explained (iii) we avoid altering the structure of the interface with volume moves. A system as that shown in Fig. 1(right) is first equilibrated at 300 K and then quenched to a temperature below melting where the simulation is run until ice crystallization is observed. In Table II we provide details on the size and the orientation of the substrate with respect to the liquid of the systems studied in this work with stretched substrates.

The heterogeneous nucleation rate is defined as the number of crystal clusters that appear and grow per unit time and unit

TABLE II. Specifications for the systems studied in this work with stretched substrates. $A_m$ is the area of the substrate face exposed to the liquid, $N_s$ is the number of molecules in the substrate, $N_l$ is the number of molecules in the liquid, $L_s$ is the substrate thickness and $n_xn_yn_z$ is the number of times that the original orthorhombic ice unit cell (reported in Table I) was replicated along x, y and z to build the initial lattice (see Fig. 1 (left)). The substrate face that is exposed to the liquid is also indicated (the basal, pI and pII orientations correspond to the the xy, xz and yz planes, respectively). $T_n$ is the nucleation temperature, defined as the temperature for which heterogeneous nucleation takes place at a rate of $10^{23.6}$ nuclei/(m²s). The error bar in the nucleation temperature is 0.5 K.

<table>
  <thead>
    <tr>
      <th colspan="7">Rigid substrate</th>
    </tr>
    <tr>
      <th>$\delta$</th>
      <th>$A_m$/(nm²)</th>
      <th>$N_s$</th>
      <th>$N_l$</th>
      <th>$L_s$</th>
      <th>$n_xn_yn_z$</th>
      <th>Plane</th>
      <th>$T_n$ / K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5</td>
      <td>137.1</td>
      <td>5400</td>
      <td>30600</td>
      <td>13.943</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>254.6</td>
    </tr>
    <tr>
      <td>7</td>
      <td>142.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>14.208</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>244.4</td>
    </tr>
    <tr>
      <td>8</td>
      <td>145.0</td>
      <td>5400</td>
      <td>30600</td>
      <td>14.341</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>241.4</td>
    </tr>
    <tr>
      <th colspan="7">Wells substrate</th>
    </tr>
    <tr>
      <td>5</td>
      <td>137.1</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.295</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>255.8</td>
    </tr>
    <tr>
      <td>7</td>
      <td>142.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.472</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>245.1</td>
    </tr>
    <tr>
      <td>8</td>
      <td>145.0</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.561</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>242.9</td>
    </tr>
    <tr>
      <td>5</td>
      <td>168.5</td>
      <td>5400</td>
      <td>30600</td>
      <td>10.399</td>
      <td>15x15x10</td>
      <td>basal</td>
      <td>255.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>158.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>10.737</td>
      <td>15x10x15</td>
      <td>pI</td>
      <td>257.0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>137.1</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.295</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>256.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>174.9</td>
      <td>5400</td>
      <td>30600</td>
      <td>10.597</td>
      <td>15x15x10</td>
      <td>basal</td>
      <td>245.5</td>
    </tr>
    <tr>
      <td>7</td>
      <td>164.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>8.208</td>
      <td>15x10x15</td>
      <td>pI</td>
      <td>247.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>142.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.472</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>246.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>178.2</td>
      <td>5400</td>
      <td>30600</td>
      <td>7.779</td>
      <td>15x15x10</td>
      <td>basal</td>
      <td>243.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>167.3</td>
      <td>5400</td>
      <td>30600</td>
      <td>8.285</td>
      <td>15x10x15</td>
      <td>pI</td>
      <td>244.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>145.0</td>
      <td>5400</td>
      <td>30600</td>
      <td>9.561</td>
      <td>10x15x15</td>
      <td>pII</td>
      <td>243.5</td>
    </tr>
  </tbody>
</table>

of substrate area. We use the following expression to obtain the nucleation rate from spontaneous nucleation events $^{55,56}$:

$$
J = \frac{1}{2At_{ind}} \tag{2}
$$

where $A$ is the area of the substrate in contact with the liquid (which is multiplied by 2 because there are two substrate-water interfaces as shown in Fig. 1 (right)), and $t_{ind}$ is the average induction time required for the nucleation of an ice embryo on the substrate. The numerator of this expression is 1 because only one nucleus appears when there is an induction period (that there is an induction period implies that a configuration with a critical nucleus is unlikely and, therefore, the likelihood of having two or more critical nuclei simultaneously is negligible). The induction time is identified by a sudden potential energy drop caused by the quick growth of the nucleated ice crystal. The use of Eq. 2 is limited to the temperature range where an induction period is appreciated. At too high temperatures no nucleation events are observed in our simulation time whereas at too low temperatures the induction time is zero because multiple nuclei readily appear and grow.

We compare the ability of different substrates to induce ice nucleation through the nucleation temperature, $T_n$, which is defined as the temperature for which a certain value of the nucleation rate is achieved. The question we try to answer is: how much does the temperature at which nucleation is observed change by modifying a certain parameter in the substrate (e. g. mismatch, lattice orientation or lattice flexibility)? Of course, such temperature depends on the substrate-water area and on the observation time (the larger the area and the observation time, the higher the temperature at which nucleation is observed). The idea is to establish the comparison between substrates exposing the same area during the same time to the liquid. Under fixed area and observation time, the temperature at which nucleation is observed corresponds to a certain value of the nucleation rate (constant denominator in Eq. 2). Fixing the area and the observation time naturally arises from the implementation of a set up to study nucleation. In simulations, for instance, typical areas and times are of the order of hundreds of nm² and hundreds of ns respectively. In summary, comparing the temperature at which nucleation happens at certain rate, is equivalent to compare the temperature at which ice formation takes place for a fixed substrate-water area and observation time. Thus, comparing nucleation temperatures permits quantify the relative ability of substrates with different characteristics. The substrate inducing nucleation at a higher temperature (or, in other words, the substrate that causes a given rate value at a higher temperature) is the better nucleant. Differences in nucleation temperatures between different substrates are expected to be fairly independent on the specific value of the rate chosen to define $T_n$. This is the case when the J(T) curves for different substrates are parallel to each other, as we will show later on.

To try understand the relative ice nucleating efficiency of different substrates we perform an analysis of the molecular structure across the interface. In particular, we compute the radial distribution function (rdf) of the particles contained in slabs of a few Å thick parallel to the interface and look for similarities to the bulk ice rdf. A more sophisticated analysis consists in identifying the first rdf peak for several slabs and plot its position as a function of the distance to the interface. This analysis evidences how the structure evolves from the interior of the substrate up the bulk fluid. In some cases, we complement this analysis with the average $q_{12}$ local bond order parameter$^{57}$ of the particles contained in each slab (considering for such calculation the 12 nearest neighbors of each particle, some of which may be placed in adjacent slabs).

### RESULTS

#### Effect of the mismatch

##### 1. Isotropic positive $\delta$

For no mismatch between ice and the substrate, $\delta=0$, we recover the behaviour expected for a direct coexistence simulation$^{58-60}$. At just 1 K below the melting temperature the substrate is immediately "wetted" by an ice-like layer (see Fig. 2(a)) that subsequently grows until the system fully crystallizes. The time evolution of the potential energy in such type of simulation is shown in Fig. 3(a). As can be seen, the

potential energy continuously goes down as the liquid turns into ice.

The phenomenology radically changes for $\delta > 0$. First of all, in order to observe ice formation, a significant supercooling must be applied (for $\delta = 5$ a supercooling of $\sim 20$ K is required). Secondly, there is no visible ice wetting layer percolating the simulation box. Instead, ice appears after some induction period via the stochastic nucleation of an ice seed on top of the substrate as that shown in Fig. 2(b). The potential energy curves shown in Fig. 3(b), corresponding to 9 different trajectories of the crystallization of mW water at 245.0 K on a wells substrate with $\delta = 7$, clearly show an initial plateau corresponding to the induction period followed by a sudden drop, that stochastically occurs at different times for different trajectories, due to ice nucleation and growth. After the first sudden drop, the potential energy remains flat again until there is a second abrupt drop due to ice nucleation and growth on the other side of the substrate. By averaging the time at which the first sudden drop takes place we can estimate an average induction time, $t_{ind}$, to obtain the heterogeneous nucleation rate via Eq. 2. Statistics could have been improved by also taking into account the second drop, but we preferred not using this information to avoid possible finite size effects by which crystallization in one side of the substrate influences ice formation on the other (e. g. by a sudden release of latent heat upon crystallization). The crystallization time inferred from a potential energy drop is the same as that obtained through an analysis of a more sophisticated local bond order parameter. This equivalence is shown in Fig. 3(c), where we compare, for a nucleation trajectory, the time evolution of the potential energy with that of the $q_{12}$ local bond order parameter$^{57}$ averaged over all particles (computed for each particle with its first 12 neighbours).

In summary, whereas a mold with $\delta = 0$ causes essentially the same effect as an ice slab in contact with the liquid and leads to crystallization just below the melting temperature, a substrate with $\delta > 0$ requires a finite supercooling to induce crystallization through a nucleation mechanism. Since we use substrates with the same inter-molecular interactions but a different and controlled lattice stretch, our approach enables us to isolate and quantify the effect of the mismatch on the ice nucleating ability of a substrate, which is the main target of this work. The idea of using substrates composed of molecules of the same nature as the those of the fluid is not entirely new. In Ref.$^{39}$ this approach was used to investigate how the strength of hydrogen bonding affects ice nucleation, although the effect of mismatch alone was not systematically quantified. Also in Ref.$^{44}$ a similar approach as employed for the Lennard-Jones system, although the liquid-substrate cross interaction was weakened with respect to the liquid-liquid one to avoid quick crystallization. In both cases, the effect of lattice mismatch was quantified in a different way as compared to our work.

The nucleation rates obtained for each of the studied molds exposing the pII plane to the liquid are plotted in Fig. 4 as a function of temperature. Triangles and circles correspond to wells and rigid molds respectively, whereas grey, brown and blue colors correspond to $\delta = 8$, 7 and 5, respectively. We have checked that the results shown in Fig. 4 do not depend on the substrate or the liquid thicknesses. The brown square (diamond) in Fig. 4 corresponds to the rate obtained with a substrate (liquid) twice as thick as that of the original system from which the brown circles were obtained. As can be seen, the results are fully consistent.

Two comments are due in view of the curves shown in Fig. 4. One is that, for a given $\delta$, the nucleation rate is lower for the rigid mold. The other is that the rate curves are shifted to lower temperatures as $\delta$ increases. We focus first on the later effect, the dependence of the rate on $\delta$, which is the strongest one and the main scope of this work. Understandably, the supercooling needed to achieve a certain heterogeneous nucleation rate increases with the mismatch between ice and the substrate.

To quantify to which extent the supercooling required for nucleation to occur increases with the mismatch we select a certain nucleation rate, $\log[\text{J}/(\text{m}^2/\text{s})) = 23.6$ (given by the dotted horizontal line in Fig. 4), and find the associated nucleation temperature, $T_n$, for each mismatch (and substrate type) by interpolation (reported in Table II).

The $10^{23.6}\ \text{m}^{-2}\text{s}^{-1}$ rate has been arbitrarily chosen in the range of nucleation rates accessible by means of simulations of spontaneous heterogeneous crystallization. Such range is determined by the area of the substrate and the simulation time according to Eq. 2. For an area of the order of a few hundred of squared nm and a time of tens of ns one gets $\log[\text{J}/(\text{m}^3\text{s})]$ in the range of 23-24. The specific rate value $10^{23.6}\ \text{m}^{-2}\text{s}^{-1}$ crosses all J(T) curves shown in Fig. 4 and enables obtaining a $T_n(\delta)$ curve by interpolation. Despite the fact that the absolute value of $T_n$ depends on this arbitrary choice of the rate, the slope of its variation with the lattice mismatch is not expected to be largely affected in view of the fact that the curves in Fig. 4 are parallel to each other. Therefore, a change in the rate used to define $T_n$ would shift by the same constant the nucleation temperature for each kind of substrate.

By performing independent sets of trajectories to determine the nucleation rate we estimate the error in $\log[\text{J}/(\text{m}^3\text{s})]$ to be $\pm$ 0.1. We note that, for a given mismatch, the nucleation rate is a very steep function of temperature. As a consequence, the uncertainty in the nucleation rate does not have a strong impact in $T_n$. We estimate such uncertainty to be $\pm$ 0.5 K.

In Fig. 5, which is the main figure of this work, we plot $T_n$ versus the mismatch for both sorts of substrates. Orange triangles and green dots correspond to wells and rigid substrates, respectively. As can be seen, as $\delta$ increases $T_n$ goes down approximately at a rate of 4 K per $\delta$ unit in both cases. In other words, if the substrate lattice is mismatched by one per cent with respect to the ice lattice, the nucleation temperature goes down by about 4 K. This slope of $4\ \text{K}/\delta$ nicely extrapolates the nucleation data up to the coexistence temperature (black dot in the figure) corresponding to no mismatch between ice and substrate. In fact, a line starting from coexistence with $-4\text{K}/\delta$ slope closely tracks the trend of the calculated nucleation temperatures (grey dashed line in the figure). Such a trend suggests a linear decrease of the nucleation temperature with the mismatch, at least up to the largest studied mismatch, $\delta = 8$. We could not tackle the study of $\delta$'s larger than 8 because

cause liquid particles entered into the substrate.

In summary, our main conclusion is that 1 per cent of structural mismatch between the nucleating and the substrate lattices roughly causes a 4 K decrease of the nucleation temperature. Given that, by construction, both lattices have the same sort of interactions, our study separates the effect of structural mismatch from that of inter-molecular interactions in heterogeneous ice nucleation. To our knowledge, this is the first quantification of the effect of the mismatch alone on the ice nucleation ability of a solid substrate. Of course, the ability to promote nucleation in real substrates is determined by coupled interaction and mismatch effects³⁴. However, isolating the effect of lattice mismatch may help understand and rationalize the ice nucleation ability of different solid substrates.

![](./images/1217814503081639968_2.jpg)

![](./images/1217814503081639968_3.jpg)

FIG. 2. (a) Snapshot shortly after starting a simulation with a $\delta=0$ rigid substrate at 1 K below the melting temperature. An ice layer wetting the mold is clearly seen. (b) Snapshot shortly after nucleation on a wells substrate with $\delta=5$ at 255.5 K.

![](./images/1217814503081639968_4.jpg)

![](./images/1217814503081639968_5.jpg)

![](./images/1217814503081639968_6.jpg)

FIG. 3. (a) Potential energy versus time for a trajectory at 272 K (1 K below the melting temperature) on a wells substrate with $\delta=0$. (b) Potential energy versus time for nine trajectories of a liquid at 245.0 K on a wells substrate with $\delta=7$. (c) Time evolution of the potential energy (green) compared to that of the average $q_{12}$ local bond order parameter⁵⁷ (orange) for a single nucleation trajectory of those shown in (b).

![](./images/1217814503081639968_7.jpg)

FIG. 4. (a) Heterogeneous nucleation rate versus temperature for the different mismatches and the different kinds of stretched substrates studied in this work as indicated in the legend. These results correspond to the pII orientation (exposing the yz plane of the stretched and replicated unit cell as indicated in table II). The open diamond (square) corresponds to a $\delta=7$ rigid substrate system having double liquid (substrate) depth than the system with which the filled brown dots were obtained. (b) Heterogeneous nucleation rate temperature dependence of expanded (exp) and compressed (comp) rigid substrates exposing the pII plane to the liquid.

## 2. Other types of mismatch

In this section we discuss the impact on ice nucleation of other sorts of deformation of the ice lattice substrate. We first consider performing an isotropic compression of the ice lattice (as opposed to an isotropic expansion as discussed so far). In this case, we deal with negative values of $(f-1)$, as defined in Eq. 1. However, according to our definition, $\delta$ is still positive because of the absolute value in Eq. 1. We only consider rigid substrates for this study. In Fig. 4(b) we compare the nucleation rate temperature dependence between compressed and expanded substrates. For a 5 per cent expansion/compression, J(T) is very similar between both types of deformations. However, as the deformation increases it seems evident that the nucleation rate is smaller for the compressed substrate (in other words, J takes the same value at lower temperatures). The nucleation temperature corresponding to the compressed substrates is represented as the empty green circles in Fig. 5. The trend for compressed and stretched substrates is similar, although the slope is slightly larger for the former (4.5 $\mathrm{K}/\delta$ versus $4\ \mathrm{K}/\delta$ approximately), consistently with the fact that compressed substrates yield smaller rates for a given temperature. This is in agreement with the observation that compressed substrates interact less favourably with water than stretched ones $^{61}$.

![](./images/1217814503081639968_8.jpg)

FIG. 5. Nucleation temperature versus the mismatch between ice and the substrate. The two different sorts of substrates studied in this work are compared for the pII orientation. The black point for $\delta=0$ corresponds to the ice melting temperature of the model (273 K). Empty green circles correspond to the rigid compressed substrate. In grey dashed, a line with -4 $\mathrm{K}/\delta$ slope starting at the coexistence point is shown for visual reference. Symbol size coincides with that of the estimated error bar.

We also consider the case in which only one side of the ice unit cell is stretched. In particular, we build a rigid substrate by stretching 5 per cent the $z$ direction of the unit cell given in Table I. We get a nucleation temperature for this substrate of 266 K (7 K supercooling) by exposing the pII orientation. This $T_n$ can be compared to the 254.6 K (18.4 K supercooling) corresponding to a substrate with a 5 per cent stretching in all directions. As expected, when only one dimension is stretched the nucleation temperature is higher because the substrate bears a stronger resemblance with ice.

## B. Nucleus and liquid structure

We focus on stretched substrates to perform an analysis of the liquid structure adjacent to the substrate prior to nucleation and of the crystal nucleus that finally grows.

![](./images/1217814503081639968_9.jpg)

FIG. 6. (a) Rdf of the particles contained in a 7.5 Å thick slab adjacent to a $\delta = 5$ and a $\delta = 8$ stretched wells substrate in green and blue respectively. In grey, the rdf of an ice slab of the same thickness. All rdf's presented correspond to simulations at 256 K. (b) q₁₂ profile across the interface (same color code as in (a)).

![](./images/1217814503081639968_10.jpg)

FIG. 7. A 7.5 Å thick liquid layer adjacent to a $\delta = 7$ wells substrate at 245.0 K. Several subcritical nuclei are highlighted with yellow circles.

### 1. Liquid structure

We first examine the structure of the liquid layer adjacent to the substrate. In Fig. 6(a), we compare the rdf's of the adjacent layers of two different wells substrates ($\delta = 5$ and $\delta = 8$) with the rdf of a bulk ice layer of the same thickness (7.5 Å). As expected, the rdf corresponding to the layer induced by the $\delta = 5$ substrate bears more resemblance with the ice layer rdf, thus facilitating ice nucleation. This conclusion is confirmed with an analysis of the q₁₂ order parameter⁵⁷ computed along 4 Å thick slabs parallel to the interface. In Fig. 6(b) we show the q₁₂ profiles for the $\delta = 5$ and the $\delta = 8$ substrates in green and blue respectively. Negative depth values correspond to the substrate interior and positive ones to the adjacent liquid. The grey horizontal line corresponds to the bulk ice value. The smaller the mismatch, the closer the q₁₂ profile to the ice value, thus confirming the expected facilitation of nucleation with a reduced $\delta$. For the $\delta = 5$ substrate, that causes nucleation at the temperature at which these profiles have been computed (256 K), the structure of the liquid is affected by that of the substrate up to a distance of 7-8 Å from the surface. For that point onward, q₁₂ takes bulk liquid values.

Both the rdf's and the q₁₂ profiles provide an averaged structural information. To better understand the molecular structure of the interface we look at the adjacent layer of a wells substrate with $\delta = 7$ (intermediate between those previously analysed). The snapshot shown in Fig. 7 reveals that the structure of the interface is heterogeneous (the snapshot has been taken at a temperature for which there is nucleation on this substrate, 245 K, but during the induction period prior to the appearance of the critical nucleus). One can clearly identify several sub-critical nuclei, highlighted within yellow circles, embedded in a liquid-like interface. These nuclei are likely responsible for the resemblance of the interface rdf with that of ice. Therefore, the interface cannot be viewed as a homogeneous wetting layer having a diffuse ice structure, but rather as a heterogeneous layer alternating ice with liquid-like patches. A visual inspection of the interface along the nucleation trajectory reveals that these nuclei continuously form and redissolve during the induction period until a fluctuation leads to the formation of a nucleus big enough to proliferate (the critical cluster).

It is also interesting to inspect the structure across the substrate-liquid interface, before the appearance of the crystal nucleus that eventually grows. The green and the pink curves in Fig. 8 correspond to the rdf first peak position across the solid-liquid interface for wells and rigid substrates, respectively. The peak position within the rigid substrate is fixed, whereas that in the wells substrate gradually goes down. We discuss such variation in Sec III C, and here we focus on the liquid side, where there is a minimum close to the interface for both types of substrates. The rdf peak position in the minimum (2.75 Å) is in between that of bulk liquid (2.8 Å), recovered at large distance from the interface, and that of bulk ice (2.7 Å). We recall that the ice-like layer at the interface is due to a heterogeneous distribution of alternating ice-like with liquid-like patches rather than to a homogeneous wetting of an ice-like layer (see Fig. 7).

### 2. Nucleus structure

To gain insight on the structure of crystal nuclei we visually inspect clusters formed on top of both types of substrates. Examples of such nuclei are shown in Fig. 9 for a given mismatch ($\delta = 7$). The enlargements in the right side of the figure show that both nuclei have tilted molecular columns in the cluster peripherals. Recall that the substrate structure is that of a stretched ice lattice, so the tiling is likely due to the gradual recovery of the thermodynamically stable lattice parameters from the contact plane (where the cluster matches the substrate) upward (where the cluster recovers the relaxed ice structure).

We show a more quantitative demonstration of the recovery of the ice structure along the cluster in Fig. 8, where we plot the position of the first peak of the radial distribution function (rdf) along the direction perpendicular to the substrate interface. The rdf is computed along consecutive $4$ Å thick slabs parallel to the interface. Values of the x-axis equal to or smaller than 0 correspond to the substrate whereas those larger than 0 correspond to the adjacent phase. Such phase corresponds, for the case of the orange and blue curves, to crystal nuclei as those shown in Fig. 9. The rdf first peak in these cases is computed along coin-like cylindrical slabs whose perimeter coincides with the liquid-substrate-nucleus contact line. The curves are averaged over several independent nuclei to improve statistics. To select a configuration with a nucleus we first identify from a potential energy drop as those shown in Fig. 3 the time at which nucleation takes place. We then look at the interface step by step starting from an earlier time and identify visually the emergence of the nucleus that expands and grows. We select a configuration where the nucleus looks as those shown Fig. 9: large enough to be analysed but not too big so that it reaches the liquid-vapor interface. Picking slightly smaller or bigger nuclei does not change the qualitative outcome of the analysis that follows. The orange curve in Fig. 8 corresponds to a nucleus on a $\delta =7$ rigid substrate. The rdf peak in the interior of the substrate is fixed by the lattice stretch and is obviously larger than that of bulk ice, indicated in the figure with a horizontal grey line. From the substrate surface onward, the peak position gradually decreases recovering in about $20$ Å the bulk ice value. This picture is fully consistent with the tilted molecular columns visible in Fig. 9. The blue curve, corresponding to a cluster on a wells substrate with the same mismatch ($\delta =7$) shows a qualitatively similar behaviour (in the following section quantitative differences are discussed). In summary, Fig. 8 confirms that the tilting of the molecular columns seen in Fig. 2 corresponds to a gradual change from the substrate to the ice structures along the cluster.

### C. Effect of the lattice flexibility

We have studied both rigid substrates, where particles are immobile, and wells substrates, where particles can move away from their lattice positions up to $1.0215$ Å. This enables assessing the effect of lattice rigidity on heterogeneous ice nucleation. Although our uncertainty of $0.1$ in $\log[\text{J}/(\text{m}^3\text{s})]$ and $0.5$ K in $T_n$ brings the results of both types of substrate close to each other, it is clear from Fig. 4(a) that, for a given temperature and $\delta$, the nucleation rate is systematically lower for a rigid substrate. In other words, for a given rate and mismatch, the nucleation temperature is higher for the wells substrate. This difference is seen Fig. 5, where the nucleation temperatures corresponding to the wells substrate systematically lie about 1-2 K above those of the rigid substrate. Therefore, our data suggests that lattice flexibility favours heterogeneous ice nucleation.

One can rationalise the better performance of the flexible substrate as an ice nucleant by looking back at the rdf first peak position profiles shown in Fig. 8. By comparing the blue (wells substrate-cluster) and the orange (rigid substrate-cluster) curves inside the substrate region it can be noticed that, despite the fact that both substrates have the same $\delta$, the rdf peak in the interior of the wells substrate is closer to the ice value. This suggests that particles of the flexible substrate use their freedom of motion within the wells to build a structure in closer resemblance to that of the thermodynamically stable ice lattice. Such a rearrangement may contribute to facilitate ice nucleation. In any case, such an "effective $\delta$ decrease" is only perceivable at the level of the rdf first peak. The second peak already appears at the position dictated by the imposed mismatch. This is shown in Fig. 8(b), where the following rdf's of $4$ Å thick slabs are compared: ice in grey, and $\delta =7$ rigid (flexible) substrate in contact with the fluid in pink (green). As previously indicated, the first peak of the wells substrate is in between those of ice and the rigid substrate whereas the second peak of the wells substrate pretty much coincides with that of the rigid substrate. Then, the effective $\delta$ reduction of the wells substrate means being closer to ice than the rigid substrate at the level of first neighbors, a parameter that has been already identified as a relevant predictor for ice nucleating ability$^{61}$.

Another aspect to consider is the structure of the wells substrate underneath the cluster. A closer inspection to the enlargements provided in Fig. 9 suggests that the tilting of the cluster molecular columns propagates down into the interior of the wells substrate, as if the substrate structure adapted to that of the cluster on top. Again, we resort to Fig. 8 to quantify and understand this effect. By comparing the green (wells substrate-nucleus) and the blue (wells substrate-liquid) curves in Fig. 8 one can check if the substrate structure changes when a nucleus appears on top. Clearly, in the vicinity of the interface, the blue curve is systematically below the green one, indicating that the substrate gets more ice-like (closer to the grey curve) when having a nucleus on top. This strongly supports the view that the substrate adapts its structure to that of the emerging nucleus.

In summary, there are two factors that may justify the better performance as an ice nucleant of the wells substrate: (i) the adaptation to the structure of the emerging cluster and (ii) the effective loss of mismatch. In any case, it is important to emphasize that flexibility is a second order effect. For instance, for a $\delta =8$ mismatch, the nucleation temperature of the rigid substrate is 31.6 K below melting whereas that of

the wells substrate is 30.1 K. Therefore, all the considerations about flexibility discussed in this section have an effect on the nucleation temperature of less than 2 K versus the 30 K caused by mismatch.

The adaptation effect resembles the enhanced ice nucle- ating ability in kaolinite due to reorientation of hydroxyl groups $^{24}$. However, flexibility does not always help ice nucle- ation. For instance, in the case of substrates composed of or- ganic molecules exposing hydroxyl groups to water, flexibility roughens the interface and is detrimental for ice nucleation $^{62}$. In our case, the substrate has a flat interface and flexibil- ity refers to the possibility of molecules to fluctuate around their lattice positions, which enhances the nucleating ability through adaptation to the emerging ice structure.

### D. Effect of the lattice orientation

The results discussed so far correspond to the pII plane be- ing exposed to the liquid. In this section we examine the ice nucleating ability of different orientations: basal, pI and pII. Details on the employed system sizes to study these orien- tations are given in Table II. We use wells stretched sub- states for this study. We have followed the same procedure as that described for the pII plane to obtain the data shown in Fig. 10, where the nucleation temperature as a function of the mismatch parameter is compared for the three orienta- tions of interest. Differences between orientations are small, but it seems that pI and basal are systematically the best and the worst ice nucleants, respectively, with a $T_{n}$ difference of about 1-2 K between them. Considering the temperature de- pendence of J shown in Fig. 4, this temperature difference means that the nucleation rate is 0,5-1 order of magnitude higher on the pI plane. The $T_{n}$ of the pII plane lies in be tween. This pattern repeats itself for the three studied values of $\delta$ . Thus, even though all orientations could be considered equally good ice nucleants taking a 0.5 K error bar in $T_{n}$ into account, we consider it is worth examining the structure of each interface in an attempt to correlate orientation with nu- cleation ability.

To understand the different nucleating abilities of the dif- ferent ice orientations we look at the structure of the liquid wetting each type of substrate. In Fig. 11 we show the rdf's obtained in a $4\ \mathring{A}$ thick slab adjacent to $\delta=5$ substrates at256 K. We also include, for comparison, the bulk ice rdf at the same temperature (multiplied by an arbitrary factor to en- able visual comparison with the un-normalised liquid slabs rdf's). Different orientations give rise to alike rdf's, which is unsurprising because they also yield similar nucleation tem- peratures. All orientations show a first maximum at $2.75\ \mathring{A}$ , at larger distances than the first peak of ice, which is positioned at $2.70\ \mathring{A}$ . Small but noticeable differences can be observed, however, in the second peak. Clearly, the rdf second peak ob- tained from the liquid layer adjacent to the basal plane is the one that lies furthest from the bulk ice second peak. This is consistent with the fact that the basal plane is the worst nucle- ant. The second peaks corresponding to the liquids adjacent to the pI and the pII orientations are very close to each other, although it seems that the former lies slightly closer to that of ice, again consistent with pI being the best nucleant. In sum- mary, the degree of structural similarity between the liquid adjacent to the substrate and ice is consistent with the relative ice nucleating abilities of different orientations, although this should be taken with caution considering our 0.5 K error bar

![](./images/1217814503081639968_11.jpg)

FIG. 8. (a) Position of the first peak of the radial distribution function along $4\ \mathring{A}$ thick slabs parallel to the interface. Orange (blue) curve corresponds to a rigid (wells) substrate in contact with a crystal nu- cleus whereas the pink (green) curve corresponds to the rigid (wells) substrate in contact with the liquid before the nucleus appears. Both substrates have the same mismatch $(\delta=7)$ and simulations are car ried out at a similar temperature (244.5 K and 245.0 K for the rigid and wells substrates, respectively). The substrate region corresponds to depths $\leq0$ (yellow background) and that of the adjacent phase(liquid or cluster) to positive depths (blue background). The grey horizontal line indicates the value of the first peak of the radial dis- tribution function for ice at 245 K. (b) rdf of $4\ \mathring{A}$ thick slabs of ice(grey) and of the $\delta=7$ substrates mentioned in (a) in contact with the fluid (pink and green correspond to rigid and flexible substrates as in (a)).

![](./images/1217814503081639968_12.jpg)

FIG. 9. a): Snapshot of a slab cut through an ice cluster (in blue) nucleating on top of a rigid substrate (in orange). The substrate exposes the pII plane to the liquid and has a $\delta=7$ structural mismatch with the ice lattice. In the right part, a zoom view of the marked region is provided to show the tilt of the molecular columns of the cluster. We have included, for visual reference, dashed lines perpendicular to the substrate and solid lines that follow the direction of the cluster molecular columns. b): Same as a) but for a wells substrate (in red).

in $T_n$.

![](./images/1217814503081639968_13.jpg)

FIG. 10. Nucleation temperature versus the mismatch for different orientations of stretched wells substrates.

![](./images/1217814503081639968_14.jpg)

FIG. 11. Radial distribution function computed in a $4\ \text{\AA}$ tick liquid slab adjacent to a $\delta=5$ stretched wells substrate exposing different orientations (orange, grey and blue curves correspond to the pI, pII and basal planes, respectively). The yellow curve is the bulk ice rdf. The temperature is $256\ \text{K}$ in all cases.

## IV. DISCUSSION

One may wonder what is the added value of using a model substrate having the same structure and the same interactions as the ice crystal. First of all, we are not the first ones to employ this strategy: it has been previously used for water$^{39}$ (although the effect of lattice mismatch on the nucleation temperature was not systematically quantified) and for a system of Lennard-Jones particles$^{44,45}$ (although the substrate-fluid interactions were weakened to prevent rapid crystallization). The main point of this approach is that it enables to unambiguously elucidate the role of lattice mismatch on heterogeneous ice nucleation, that has been long believed to be a key factor$^{32}$. In fact, a recent and very successful collaboration between simulations and experiments$^{20}$ explains the ice nucleating ability of feldspar with a match of a "$3\times1$ array of [ice] prism face unit cells within one unit cell of the feldspar (100) surface." However, the validity of the lattice match as a predictor for ice nucleating ability has been challenged$^{21,39,63}$. For instance, for a simulation study where the substrate has an fcc structure, it has been concluded that $\delta=0$ is not the optimal value for nucleation$^{34}$. Our approach, in apparent contrast, shows that the best crystallizing structure corresponds to $\delta=0$ and that the nucleation temperature decreases roughly linearly with $\delta$ (with a slightly larger slope for compressed than for expanded substrates). A similar conclusion, using an analogous approach, was found for the Lennard-Jones system$^{44,45}$ where the optimal mismatch is close to 0 (it is not strictly 0 because the crystal nucleus, due to the Laplace pressure, has a slightly different lattice parameter than the bulk solid). Is then the work published in Refs.$^{45}$ and$^{44}$ and our work in contradiction with Ref.$^{34}$? It is not in the sense that perhaps the best way to define structural simi-

larity when the substrate lattice is not wurtzite-like (that of ice Ih) is not through the lattice edges, but through another struc- tural feature that better accounts for the similarity between the ice and the substrate. In Ref. $^{61}$ , for instance, a match between first neighbour distance was found to be a better structural pre- dictor for ice nucleation on close packed surfaces. Also, in Ref. $^{22}$ alternative definitions to the conventional lattice mis match are found to better predict ice nucleation abilities in mineral lattices. Then, it may make more sense speaking of a structural rather than of a lattice mismatch. The problem is that the definition of the former concept is not unique and requires a systematic analysis of different sorts of substrate lattices, which is an interesting study for future work. In our work, since we use the ice lattice as a substrate, the structural match is uniquely defined.

Another issue to which our approach can provide some in- sight is the relative ice-nucleating ability of the different ori- entations of a wurtzite-like structure (that of ice Ih or of $\beta$ AgI, a powerful ice nucleant). Different simulation studies on $\beta$-AgI have reported nucleation on the basal plane $^{21,23}$. How ever, in Ref. $^{64}$ strongly different nucleating abilities between the different prism orientations of AgI were reported. Ice nu- cleation was observed on the pI plane but not on the pII "by details of the surface water interaction". Such details are not present in our approach because our substrate interacts with water in the same manner as water does with itself. In fact, in Ref. $^{64}$ nucleation on the pII plane is observed when an ice-like substrate is used like in the present work. Here, we quantify the nucleating ability of the three main wurtzite orientations and find similar nucleation rates for all of them. Thereby, our work serves to confirm that possible differences in nucleating abilities between the orientations of a wurtzite-type structure are not due to structural issues but rather to the specific nature of the substrate-water interactions.

In this respect, once again, one should reflect on the fact that the results obtained with simulations that aim to be realistic may strongly vary depending on the selected force field. This is acknowledged in Ref. $^{28}$ , where heterogeneous nucleation on kaolinite was studied with classical simulations: "fully atomistic models are needed to deal with water at complex interfaces, such as crystalline surfaces of organic crystals or mineral dust particles. In these cases, it remains to be seen whether the description of the surface, and most importantly of the water surface interaction, is accurate enough to allow for reliable results to be obtained." A clear example of this problem can be found in Ref. $^{21}$ , where nucleation was studied on AgI, the following issue was encountered: "in contrast to real AgI, the crystal began to quickly dissolve in water, and therefore, we constrained the $Ag^{+}$ and $I^{-}$ ions with a har monic potential." Therefore, studies on heterogeneous ice nu- cleation with realistic substrates, although certainly valuable and pioneer, may draw force-field dependent conclusions. As an effort in improving the existing force fields to describe het- erogeneous nucleants is under way, our work, even though not directly transferable to experiments due to the lack of realism of the substrate structure and potential, can serve to extract fundamental conclusions about structural effects on ice nucle- ating ability.

In a context where we do not have tested surface-water in- teractions, where the role of lattice mismatch is debated and where the nucleating ability of the main wurtzite orientations needs to be further examined, we believe it is worth pursuing a simple approach like ours, where the ambiguity in defining structural matching and the coupling between structure and interactions have been removed. In Section V we summa- rize the main conclusions we draw from our work. The added value of this paper is, therefore, having devised and applied a strategy to quantify and isolate the role of lattice mismatch on heterogeneous ice nucleation and to examine the effect of wurtzite lattice orientation and flexibility. We acknowledge that our strategy does not enable a direct comparison with ex- periments, but this is also a problem for simulations that rely on the performance of force fields that have not been thor- oughly tested. In order to test a force field it is necessary to check if it gives predictions that are close to experimental measurements. A property that can be computed in simula- tions and measured in experiments is the nucleation rate, that has been successfully compared for the case of homogeneous ice nucleation $^{65,66}$ . However, to our knowledge, there is no di rect comparison between experimental and simulated hetero- geneous nucleation rates to date and further work is required to achieve such milestone.

In immersion freezing experiments freezing takes place in an ensemble of supercooled water drops containing ice nu- cleating particles. The heterogeneous nucleation rate can be inferred by monitoring the fraction of frozen drops along time $^{67,68}$ . Through the nucleation rate, a direct comparison between simulations and real measurements could be estab- lished. This sort of comparison has been successfully done so far for homogeneous nucleation in supercooled water $^{66}$ . In contrast, we are unaware of the existence of a similar com- parison for heterogeneous nucleation. There are several rea- sons for this lack of simulation-experimental bridges in het- erogeneous ice nucleation. On the one hand, it is only re- cently that heterogeneous nucleation rates are being experi- mentally determined (traditionally, $n_{s}$ , the number of active sites per particle, has been used to characterise heterogeneous nucleation $^{3,67}$ , but this parameter does not take into account the stochastic and time dependent character of nucleation $^{67}$ ). On the simulation side, the main drawback is the lack of re- liable substrate-water interactions that enable for quantitative predictions of the nucleation rate. Moreover, running sim- ulations with atomistic models is much more complex than with the mW model. Even though it is not the purpose of this work to establish a direct comparison with experiments (we have used a model rather than a real susbstrate with the aim of investigating the influence of the substrate structure on ice nucleation), we can at least compare the order of magnitude of our rates with typical experimental values. In Ref. $^{68}$ , the nucleation rate reported for dust ice nucleating particles at 30 $K$ supercooling is of the order of $10^{10}m^{-2}s^{-1}$ . At this su percooling, the nucleation rate of the least efficient simulated substrate, the $\delta=8$ rigid one, is of the order of $10^{24}m^{-2}s^{-1}$ . There is a huge difference in orders of magnitude that goes in the expected direction: Obviously, an ice-like substrate with water-like interactions like ours, is much more efficient in nu-

cleating ice than a dust mineral that bears much less resemblance with ice. A great effort is needed, both from simulations and experiments, to get heterogeneous nucleation data that are consistent with each other. It would be highly desirable to achieve such consistence because it would greatly enhance our confidence in simulation predictions regarding the structure of the substrate-water interface. In the mean time, a study like the present one that focuses on understanding how the structure of a model substrate affects its nucleation efficiency can provide insights on the problem of heterogeneous ice nucleation.

We stress that we do not want our work to convey the message that lattice structure is the only important factor in heterogeneous ice nucleation. We have simply focused on this factor alone because we believe that when there are many variables affecting a complex phenomenon it is of interest to analyse them one by one. The message that, when all other factors are removed, lattice mismatch is important, does not contradict that such parameter may not be a good descriptor when coupled structural and interaction effects play a simultaneous role⁸,²²,²⁷,³³⁻³⁴.

## V. CONCLUSIONS

We have performed molecular simulations of supercooled water in contact with substrates composed of water molecules having a stretched/compressed ice structure. This strategy enables us to establish a direct relationship between the ice nucleating ability (quantified by means of the temperature at which nucleation is observed) and the mismatch between the ice and the substrate structures. These are the main conclusions we draw from our work:

- A one per cent increase of mismatch between a stretched ice lattice and ice itself decreases the nucleation temperature by approximately 4 K.
- Stretching causes a similar effect as compressing for low-moderate deformations. For high deformations compressing leads to poorer nucleants.
- The nucleating abilities of the main ice faces (basal, pI and pII) are very similar to each other, being the pI orientation the most efficient with a nucleation temperature about 1-2 K above that of the basal plane, which is the poorest nucleant.
- Lattice flexibility of the substrate enhances ice nucleation through both an effective loss of mismatch and an adaptation of the substrate structure to that of the emerging nucleus.
- The structure of the crystal nucleus matches that of the substrate in the contact plane and gradually recovers that of bulk ice in more distant planes.
- Sub critical clusters are formed and redissolved on the liquid-substrate contact plane during the induction period prior to the formation of the critical nucleus.

We have used a simplified monoatomic water model to perform this work. It would be interesting to test in the future whether a similar behaviour is recovered with more realistic potentials. One can also study with this approach the role of substrate-water interactions on heterogeneous ice nucleation or even explore substrate structures inspired in real nucleants like inorganic minerals.

## VI. DATA AVAILABILITY STATEMENT

The data that supports the findings of this study are available within the article.

## ACKNOWLEDGMENTS

This work was funded by Grants No. PID2019-105898GB-C21, PID2019-105898GA-C22, PID2022-136919NB-C31 and PID2022-136919NB-C32 of the MICINN. The authors gratefully acknowledge the Universidad Politecnica de Madrid (www.upm.es) for providing computing resources on Magerit Supercomputer. M.M.C. and J.R. acknowledge CAM and UPM for financial support of this work through the CavI-tieS project No. APOYO-JOVENES-01HQ1S-129-B5E4MM from "Accion financiada por la Comunidad de Madrid en el marco del Convenio Plurianual con la Universidad Politecnica de Madrid en la linea de actuacion estimulo a la investigacion de jovenes doctores" and CAM under the Multiannual Agreement with UPM in the line Excellence Programme for University Professors, in the context of the V PRICIT (Regional Programme of Research and Technological Innovation).

## VII. REFERENCES

¹E. Sanz, C. Vega, J. Espinosa, R. Caballero-Bernal, J. Abascal, and C. Valeriani, "Homogeneous ice nucleation at moderate supercooling from molecular simulation," Journal of the American Chemical Society **135**, 15008-15017 (2013).
²C. Hoose and O. Möhler, "Heterogeneous ice nucleation on atmospheric aerosols: a review of results from laboratory experiments," Atmospheric Chemistry and Physics **12**, 9817-9854 (2012).
³B. Murray, D. O'sullivan, J. Atkinson, and M. Webb, "Ice nucleation by particles immersed in supercooled cloud droplets," Chemical Society Reviews **41**, 6519-6554 (2012).
⁴Z. A. Kanji, L. A. Ladino, H. Wex, Y. Boose, M. Burkert-Kohn, D. J. Cziczzo, and M. Krämer, "Overview of ice nucleating particles," Meteorological Monographs **58**, 1-1 (2017).
⁵C. Hoose, J. E. Kristjánsson, J.-P. Chen, and A. Hazra, "A classical-theory-based parameterization of heterogeneous ice nucleation by mineral dust, soot, and biological particles in a global climate model," Journal of the Atmospheric Sciences **67**, 2483-2503 (2010).
⁶A. D. Harrison, T. F. Whale, M. A. Carpenter, M. A. Holden, L. Neve, D. O'Sullivan, J. Vergara Temprado, and B. J. Murray, "Not all feldspars are equal: a survey of ice nucleating properties across the feldspar group of minerals," Atmospheric Chemistry and Physics **16**, 10927-10940 (2016).
⁷J. D. Atkinson, B. J. Murray, M. T. Woodhouse, T. F. Whale, K. J. Baustian, K. S. Carslaw, S. Dobbie, D. O'Sullivan, and T. L. Malkin, "The importance of feldspar for ice nucleation by mineral dust in mixed-phase clouds," Nature **498**, 355-358 (2013).

$^{8}$Z. Zhang and X.-Y. Liu, "Control of ice nucleation: freezing and antifreeze strategies," Chemical Society Reviews 47, 7116-7139 (2018).

$^{9}$T. F. Whale, M. Rosillo-Lopez, B. J. Murray, and C. G. Salzmann, "Ice nu- cleation properties of oxidized carbon nanomaterials," The journal of phys- ical chemistry letters 6, 3012-3016 (2015).

$^{10}$G. C. Sosso, P. Sudera, A. T. Backes, T. F. Whale, J. Fröhlich-Nowoisky, M. Bonn, A. Michaelides, and E. H. Backus, "The role of structural order in heterogeneous ice nucleation," Chemical Science 13, 5014-5026 (2022).

$^{11}$D. A. Knopf and P. A. Alpert, "A water activity based model of hetero- geneous ice nucleation kinetics for freezing of water and aqueous solution droplets," Faraday discussions 165, 513-534 (2013).

$^{12}$R. Cabriolu and T. Li, "Ice nucleation on carbon surface supports the clas- sical theory for heterogeneous nucleation," Physical Review E 91, 052402 (2015).

$^{13}$V. I. Khvorostyanov and J. A. Curry, "A new theory of heterogeneous ice nucleation for application in cloud and climate models," Geophysical re- search letters 27, 4081-4084 (2000).

$^{14}$B. Zobrist, C. Marcolli, T. Peter, and T. Koop, "Heterogeneous ice nu- cleation in aqueous solutions: the role of water activity," The Journal of Physical Chemistry A 112, 3965-3975 (2008).

$^{15}$X. Liu and J. E. Penner, "Ice nucleation parameterization for global mod- els," Meteorologische Zeitschrift , 499-514 (2005).

$^{16}$J.-P. Chen, A. Hazra, and Z. Levin, "Parameterizing ice nucleation rates using contact angle and activation energy derived from laboratory data," Atmospheric Chemistry and Physics 8, 7431-7449 (2008).

$^{17}$D. Barahona and A. Nenes, "Parameterizing the competition between homogeneous and heterogeneous freezing in cirrus cloud formation-monodisperse ice nuclei," Atmospheric Chemistry and Physics 9, 369-381 (2009).

$^{18}$L. Lupi, B. Peters, and V. Molinero, "Pre-ordering of interfacial water in the pathway of heterogeneous ice nucleation does not lead to a two-step crystallization mechanism," The journal of chemical physics 145, 211910 (2016).

$^{19}$C. Li, X. Gao, and Z. Li, "Surface energy-mediated multistep pathways for heterogeneous ice nucleation," The Journal of Physical Chemistry C 122, 9474-9479 (2018).

$^{20}$A. Kiselev, F. Bachmann, P. Pedevilla, S. J. Cox, A. Michaelides, D. Gerth- sen, and T. Leisner, "Active sites in heterogeneous ice nucleation-the ex- ample of k-rich feldspars," Science 355, 367-371 (2017).

$^{21}$G. Fraux and J. P. Doye, "Note: Heterogeneous ice nucleation on silver- iodide-like surfaces," The Journal of chemical physics 141, 216101 (2014).

$^{22}$A. Soni and G. Patey, "How microscopic features of mineral surfaces crit- ically influence heterogeneous ice nucleation," The Journal of Physical Chemistry C 125, 10723-10737 (2021).

$^{23}$S. A. Zielke, A. K. Bertram, and G. N. Patey, "A molecular mechanism of ice nucleation on model agi surfaces," The Journal of Physical Chemistry B 119, 9049-9055 (2015).

$^{24}$S. A. Zielke, A. K. Bertram, and G. Patey, "Simulations of ice nucleation by kaolinite (001) with rigid and flexible surfaces," The Journal of Physical Chemistry B 120, 1726-1734 (2016).

$^{25}$A. Soni and G. Patey, "Unraveling the mechanism of ice nucleation by mica (001) surfaces," The Journal of Physical Chemistry C 125, 26927-26941 (2021).

$^{26}$P. Pedevilla, M. Fitzner, G. C. Sosso, and A. Michaelides, "Heterogeneous seeded molecular dynamics as a tool to probe the ice nucleating ability of crystalline surfaces," The Journal of chemical physics 149, 072327 (2018).

$^{27}$S. J. Cox, Z. Raza, S. M. Kathmann, B. Slater, and A. Michaelides, "The microscopic features of heterogeneous ice nucleation may affect the macro- scopic morphology of atmospheric ice crystals," Faraday Discussions 167, 389-403 (2013).

$^{28}$G. C. Sosso, G. A. Tribello, A. Zen, P. Pedevilla, and A. Michaelides, "Ice formation on kaolinite: Insights from molecular dynamics simulations," The Journal of chemical physics 145 (2016).

$^{29}$B. Glatz and S. Sarupria, "The surface charge distribution affects the ice nucleating efficiency of silver iodide," The Journal of Chemical Physics 145 (2016).

$^{30}$G. C. Sosso, T. F. Whale, M. A. Holden, P. Pedevilla, B. J. Murray, and A. Michaelides, "Unravelling the origins of ice nucleation on organic crys- tals," Chemical science 9, 8077-8088 (2018).

$^{31}$P. Pedevilla, S. J. Cox, B. Slater, and A. Michaelides, "Can ice-like struc- tures form on non-ice-like substrates? the example of the k-feldspar micro- cline," The Journal of Physical Chemistry C 120, 6704-6713 (2016).

$^{32}$D. Turnbull and B. Vonnegut, "Nucleation catalysis." Industrial & Engi- neering Chemistry 44, 1292-1298 (1952).

$^{33}$Y. Bi, B. Cao, and T. Li, "Enhanced heterogeneous ice nucleation by spe- cial surface geometry," Nature communications 8, 15372 (2017).

$^{34}$M. Fitzner, G. C. Sosso, S. J. Cox, and A. Michaelides, "The many faces of heterogeneous ice nucleation: Interplay between surface morphology and hydrophobicity," Journal of the American Chemical Society 137, 13658-13669 (2015).

$^{35}$B. Glatz and S. Sarupria, "Heterogeneous ice nucleation: Interplay of sur- face properties and their impact on water orientations," Langmuir 34, 1190-1198 (2018).

$^{36}$S. J. Cox, S. M. Kathmann, B. Slater, and A. Michaelides, "Molecu- lar simulations of heterogeneous ice nucleation. i. controlling ice nucle- ation through surface hydrophilicity," The Journal of chemical physics 142, 184704 (2015).

$^{37}$S. J. Cox, S. M. Kathmann, B. Slater, and A. Michaelides, "Molecular simulations of heterogeneous ice nucleation. ii. peeling back the layers," The Journal of chemical physics 142, 184705 (2015).

$^{38}$C. Valeriani, "Deep learning for unravelling features of heterogeneous ice nucleation," Proceedings of the National Academy of Sciences 119, e2211295119 (2022).

$^{39}$A. Reinhardt and J. P. Doye, "Effects of surface interactions on heteroge- neous ice nucleation for a monatomic water model," The Journal of chemi- cal physics 141, 084501 (2014).

$^{40}$C. Li, X. Gao, and Z. Li, "Roles of surface energy and temperature in heterogeneous ice nucleation," The Journal of Physical Chemistry C 121, 11552-11559 (2017).

$^{41}$L. Lupi and V. Molinero, "Does hydrophilicity of carbon particles improve their ice nucleation ability?" The Journal of Physical Chemistry A 118, 7330-7337 (2014).

$^{42}$H. Lu, Q. Xu, J. Wu, R. Hong, and Z. Zhang, "Effect of interfacial dipole on heterogeneous ice nucleation," Journal of Physics: Condensed Matter 33, 375001 (2021).

$^{43}$M. Fitzner, P. Pedevilla, and A. Michaelides, "Predicting heterogeneous ice nucleation with a data-driven approach," Nature communications 11, 4777 (2020).

$^{44}$J. Mithen and R. Sear, "Epitaxial nucleation of a crystal on a crystalline surface," Europhysics Letters 105, 18004 (2014).

$^{45}$J. Mithen and R. Sear, "Computer simulation of epitaxial nucleation of a crystal on a crystalline surface," The Journal of Chemical Physics 140 (2014).

$^{46}$P. W. Wilson, A. Heneghan, and A. Haymet, "Ice nucleation in nature: supercooling point (scp) measurements and the role of heterogeneous nu- cleation," Cryobiology 46, 88-98 (2003).

$^{47}$V. Molinero and E. B. Moore, "Water modeled as an intermediate element between carbon and silicon," The Journal of Physical Chemistry B 113, 4008-4016 (2009).

$^{48}$A. Hudait, S. Qiu, L. Lupi, and V. Molinero, "Free energy contributions and structural characterization of stacking disordered ices," Physical Chemistry Chemical Physics 18, 9544-9553 (2016).

$^{49}$S. Plimpton, "Fast parallel algorithms for short-range molecular dynamics," Journal of computational physics 117, 1-19 (1995).

$^{50}$S. Nosé, "A unified formulation of the constant temperature molecular dy- namics methods," The Journal of chemical physics 81, 511-519 (1984).

$^{51}$W. G. Hoover, "Canonical dynamics: Equilibrium phase-space distribu- tions," Physical review A 31, 1695 (1985).

$^{52}$C. Vega, M. Martin-Conde, and A. Patrykiejew, "Absence of superheat- ing for ice ih with a free surface: A new method of determining the melt- ing point of different water models," Molecular Physics 104, 3583-3592 (2006).

$^{53}$B. Slater and A. Michaelides, "Surface premelting of water ice," Nature Reviews Chemistry 3, 172-188 (2019).

$^{54}$I. Sanchez-Burgos, A. R. Tejedor, C. Vega, M. M. Conde, E. Sanz, J. Ramirez, and J. R. Espinosa, "Homogeneous ice nucleation rates for mw and tip4p/ice models through lattice mold calculations," The Journal of Chemical Physics 157, 094503 (2022).

$^{55}$L. Filion, M. Hermes, R. Ni, and M. Dijkstra, "Crystal nucleation of hard spheres using molecular dynamics, umbrella sampling, and forward flux sampling: A comparison of simulation techniques," The Journal of chemi- cal physics 133 (2010).

$^{56}$J. R. Espinosa, C. Vega, C. Valeriani, D. Frenkel, and E. Sanz, "Heteroge- neous versus homogeneous crystal nucleation of hard spheres," Soft Matter 15, 9625-9631 (2019).

$^{57}$P. J. Steinhardt, D. R. Nelson, and M. Ronchetti, "Bond-orientational order in liquids and glasses," Physical Review B 28, 784 (1983).

$^{58}$A. Ladd and L. Woodcock, "Triple-point coexistence properties of the lennard-jones system," Chemical Physics Letters 51, 155-159 (1977).

$^{59}$R. García Fernández, J. L. Abascal, and C. Vega, "The melting point of ice ih for common water models calculated from direct coexistence of the solid-liquid interface," The Journal of chemical physics 124 (2006).

$^{60}$M. Conde, M. Gonzalez, J. Abascal, and C. Vega, "Determining the phase diagram of water from direct coexistence simulations: The phase diagram of the tip4p/2005 model revisited," The Journal of Chemical Physics 139 (2013).

$^{61}$S. J. Cox, S. M. Kathmann, J. A. Purton, M. J. Gillan, and A. Michaelides, "Non-hexagonal ice at hexagonal surfaces: The role of lattice mismatch," Physical Chemistry Chemical Physics 14, 7944-7949 (2012).

$^{62}$Y. Qiu, N. Odendahl, A. Hudait, R. Mason, A. K. Bertram, F. Paesani, P. J. DeMott, and V. Molinero, "Ice nucleation efficiency of hydroxylated organic surfaces is controlled by their structural fluctuations and mismatch to ice," Journal of the American Chemical Society 139, 3052-3064 (2017).

$^{63}$W. G. Finnegan and S. K. Chai, "A new hypothesis for the mechanism of ice nucleation on wetted agi and agi· agcl particulate aerosols," Journal of the atmospheric sciences 60, 1723-1731 (2003).

$^{64}$A. Soni and G. Patey, "Ice nucleation by the primary prism face of silver iodide," The Journal of Physical Chemistry C 126, 6716-6723 (2022).

$^{65}$J. R. Espinosa, A. Zaragoza, P. Rosales-Pelaez, C. Navarro, C. Valeriani, C. Vega, and E. Sanz, "Interfacial free energy as the key to the pressure- induced deceleration of ice nucleation," Physical review letters 117, 135702 (2016).

$^{66}$J. R. Espinosa, C. Vega, and E. Sanz, "Homogeneous ice nucleation rate in water droplets," The Journal of Physical Chemistry C 122, 22892-22896 (2018).

$^{67}$D. A. Knopf, P. A. Alpert, A. Zipori, N. Reicher, and Y. Rudich, "Stochas- tic nucleation processes and substrate abundance explain time-dependent freezing in supercooled droplets," NPJ climate and atmospheric science 3, 2 (2020).

$^{68}$G. C. Cornwell, C. S. McCluskey, P. J. DeMott, K. A. Prather, and S. M. Burrows, "Development of heterogeneous ice nucleation rate coefficient pa- rameterizations from ambient measurements," Geophysical Research Let- ters 48, e2021GL095359 (2021).