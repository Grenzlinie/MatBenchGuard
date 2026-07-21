# First-Principles-Based Monte Carlo Simulation of Ethylene Hydrogenation Kinetics on Pd

Eric W. Hansen and Matthew Neurorock¹

Department of Chemical Engineering, University of Virginia, Charlottesville, Virginia 22903

Received March 6, 2000; accepted August 8, 2000

A first-principles-based kinetic Monte Carlo algorithm was used to simulate catalytic kinetics of ethylene hydrogenation on the well-defined Pd(100) surface. An intrinsic kinetic database was established from first-principles density functional quantum chemical calculations. This database was supplemented by an interaction model that was developed from 1750 extended Hückel calculations that explicitly examined adsorbate–adsorbate interactions between ethyl, ethylene, and hydrogen. Subsequently, this database was used to simulate ethylene hydrogenation kinetics via a multisite Monte Carlo algorithm that treats coverage-dependent activation energies through bond-order conservation methods. The simulated apparent activation energy for ethylene hydrogenation was found to be 9–12 kcal/mol, which compares well with experimental measurements of 6–11 kcal/mol. Kinetic orders vary with temperature and partial pressures of ethylene and hydrogen, but compare well with experiments under similar conditions. Simulated kinetic orders in hydrogen and ethylene are 0.65 to 0.85 and –0.4 to 0, respectively, under our conditions (298 K, $P_{\text{H}_2} = 100$ Torr, $P_{\text{C}_2\text{H}_4} = 25$ Torr). The simulation results suggest that interactions in the adlayer, ensemble size effects, and adsorption site competition contribute to hydrogen kinetic orders that are less than one and negative orders in ethylene.

Key Words: Monte Carlo; DFT; BOC; catalysis; ethylene hydrogenation; interaction models.

## INTRODUCTION

Olefin hydrogenation over supported group VIII metals plays an important role in refining hydrocarbon feedstocks in the petroleum industry. Ethylene is of particular importance due to its widespread use as a cheap raw material (1). Furthermore, the production of polymer-grade ethylene requires the selective hydrogenation of acetylene from ethylene feedstocks. Ethylene hydrogenation in this situation is an unselective route that needs to be minimized. Supported palladium particles that are alloyed with group IB metals are known to be quite effective for this chemistry (2, 3). Ethylene hydrogenation has been studied extensively on group VIII metals (4, 5) such as Pt (6–13) and Pd (14–20), due to their industrial use. The overall chemistry is thought to follow the Horiuti–Polanyi mechanism that is outlined in Fig. 1 (21). The mechanism that was established over 50 years ago captures the basic processes that occur. Molecular hydrogen adsorbs dissociatively, thus producing two surface hydrogen atoms. Ethylene adsorbs molecularly in either $\pi$ or di-$\sigma$ adsorption states. Surface hydrogen reacts with ethylene in two steps to form ethyl and then ethane, which desorbs from the surface. Despite the wealth of information that exists on ethylene hydrogenation, there are still a number of critical issues regarding the explicit details that remain unanswered. Although these reactions are relatively simple, the surface chemistry is complex due to the influence of the local reaction environment. At least three different schemes regarding the nature of the active surface site(s)/ensemble(s) that controls the mechanism have been outlined in the literature (22).

(i) Hydrogen and ethylene reversibly adsorb and compete for the same surface sites.

(ii) Hydrogen and ethylene reversibly adsorb in separate islands and the reaction occurs at the edges of the islands.

(iii) Hydrogen is adsorbed on two sites: one site is competitive with ethylene while the other is noncompetitive with ethylene.

The reaction models formulated for each of these schemes are different. In addition, the reaction kinetics for ethylene hydrogenation may fit into more than one of these schemes depending on temperature, partial pressure of reactants, and the actual catalyst used. In experimental studies on Pt, the kinetic reaction orders can change from 0.5 to 1.0 in hydrogen and from slightly negative to slightly positive in ethylene (7, 23). The apparent activation energy for ethylene hydrogenation decreases with increasing temperature. The experimentally reported values range from 6.5 to 10.7 kcal/mol based on supported Pd particles (4, 15, 16, 18, 22, 24). Because of the strong dependence on reaction conditions, the delineation of the elementary kinetics for ethylene hydrogenation over Pd has proven to be difficult

¹ To whom correspondence should be addressed. E-mail: mn4n@Virginia.edu.
![](./images/812456812748996610_1.jpg)

(20). Much of the difficulty in establishing the fundamental kinetics stems from our inability to monitor the molecular surface processes and the effects of the reaction environment. Instead, one typically adopts a Langmuir-Hinshelwood-type model and regresses kinetic parameters from it. However, the Langmiur-Hinshelwood model treats only average surface concentrations and ignores the effect of the explicit local environment on the kinetics. This can ultimately lead to the different interpretations of the surface kinetics.

Advances in both ab initio quantum chemical methods and atomistic simulation algorithms enable us to begin to model surface kinetic processes in greater detail. Kinetic Monte Carlo (MC) simulation, for example, can be used to simulate elementary surface rate processes and the explicit effects of surface coverage (25-35). Ab initio methods, on the other hand, can be used to begin to predict elementary energetic parameters for model catalytic systems (6, 36-41). By applying these two methods together, we can begin to simulate kinetics on ideal surfaces. Recently, there have been many advances in ab initio quantum mechanical methods and their application to catalytic systems, along with atomistic simulations. There have been a number of elegant microkinetic modeling (23, 46) and Monte Carlo simulation studies (49, 51, 52) that have been used to begin to capture the essential chemistry. These studies tend to typically employ empirical parameters established from experiments and do not take into account changes in the kinetics due to local surface coverage effects.

In this paper, we develop and apply a kinetic Monte Carlo approach that incorporates first-principle quantum chemical data to simulate the hydrogenation of ethylene over Pd (47, 50, 54). The algorithm explicitly tracks the spatial and temporal changes of all surface intermediates in order to simulate the kinetics. This enables us to begin to resolve some of the questions that refer to the effects of surface site and explicit environment on the measured kinetics. More generally, we develop an approach that combines first-principle quantum chemical results with a kinetic Monte Carlo method in order to simulate the elementary surface processes as well as the effects of the local reaction environment on the measured chemistry and kinetics. Adsorbates are allowed to occupy different surface sites (one-, two-, three-, and four-fold) whereby all neighboring interactions between surface species are accounted for. By explicitly following the atomic surface structure, the simulation can be used to track competing surface elementary steps, i.e., adsorption, desorption, surface reaction, and surface diffusion. This enables the incorporation of quantum-chemically derived energetics directly into the simulation of the kinetic behavior. First-principle density functional quantum chemical methods are currently able to predict chemisorption, activation, and overall reaction energies to within the range of 5 kcal/mol (56, 57). Differences of 5 kcal/mol in the activation barrier can significantly affect the accuracy of absolute rate constants. We therefore do not attempt to quantitatively match reaction rates in this work. The methods do, however, appear to be good enough to compute relative trends and establish the nature of the active surface complex along with factors that control the mechanism. As quantum mechanical methods become faster and more accurate, so too will this simulation approach.

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>$v_{for}$</th>
      <th>$v_{rev}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{C}_2\text{H}_4$</td>
      <td>+</td>
      <td>*</td>
      <td>$\rightleftharpoons$</td>
      <td>$\text{C}_2\text{H}_4^*$</td>
      <td>$\text{s}_\text{o}=1\ _{(46)}$</td>
      <td>$10^9\ \text{s}^{-1}_{(45)}$</td>
    </tr>
    <tr>
      <td>$\text{H}_2$</td>
      <td>+</td>
      <td>$2\ *$</td>
      <td>$\rightleftharpoons$</td>
      <td>$2\ \text{H}^*$</td>
      <td>$\text{s}_\text{o}=0.1\ _{(46)}$</td>
      <td>$10^{13}\ \text{s}^{-1}$</td>
    </tr>
    <tr>
      <td>$\text{C}_2\text{H}_4^*$</td>
      <td>+</td>
      <td>$\text{H}^*$</td>
      <td>$\rightleftharpoons$</td>
      <td>$\text{C}_2\text{H}_5^*$ + *</td>
      <td>$10^{13}\ \text{s}^{-1}$</td>
      <td>$10^{13}\ \text{s}^{-1}$</td>
    </tr>
    <tr>
      <td>$\text{C}_2\text{H}_5^*$</td>
      <td>+</td>
      <td>$\text{H}^*$</td>
      <td>$\rightleftharpoons$</td>
      <td>$\text{C}_2\text{H}_6$ + $2\ *$</td>
      <td>$10^{13}\ \text{s}^{-1}$</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>

FIG. 1. Elementary reactions used in the simulation. Ethylene adsorption steps are considered to be in equilibrium. Preexponentials ($v_{for}$, $v_{rev}$) and sticking coefficients ($s_\text{o}$) are assumed or taken from the literature as described in the text.

## METHODS

The set of elementary reaction steps used in the simulation is shown in Fig. 1. The activation barriers for these steps were derived from first-principle density functional quantum chemical calculations. Preexponential factors and sticking coefficients used in the simulation are also shown (see Results for a more detailed discussion). The MC kinetic algorithm, which is written in the C++ object-oriented language, is composed of a series of objects that describe the surface, the species, the reactions, and the reaction environment to simulate molecular kinetics. A sketch of the hierarchical arrangement of the algorithm is given in Fig. 2. The adsorbates, the reactions, and the surface are a set of fundamental objects around which the code is constructed. More specific objects that link fundamentals are the interaction

![](./images/812456812748996610_2.jpg)

FIG. 2. General hierarchy of the object-oriented Monte Carlo methodology for simulating surface chemistry. Dependencies are indicated by arrows.

model, surface scenarios, and the simulation engine. We will first describe the fundamental objects in the simulation and then expound on supplementary objects that act to connect the fundamental objects.

### Fundamental Simulation Objects

Perhaps the most basic and fundamental object in the simulation is the species object. The species object defines each species (reactants, products, and intermediates) by its physical properties. Important properties for each species are its binding energy at each surface site and a reaction radius. The reaction distance is the maximum distance where we allow reaction to occur. The reaction radius is defined as the contribution to this distance from individual species. The reaction radius is $2.0\ \text{\AA}$ for ethylene, $2.0\ \text{\AA}$ for ethyl, and $1.39\ \text{\AA}$ for hydrogen. Additional information about each adsorbate is required such as its atomization energy and internal fragments that result from bond dissociation. Surface species are then used to build surface reaction objects. A surface reaction is defined by the type of reaction, the reactants, and the products. Each reaction is given a forward and reverse activation energy along with corresponding preexponential values that are valid in the *zero* coverage limit on the metal surface. To represent the well-defined single crystal (100) surface, we use a grid that has periodic boundary conditions and contains an array of grid site objects for the surface and metal layer. All atop, bridge, and hollow grid sites are defined by their specific location in space. Grid sites may contain a species, such as a metal atom or an adsorbate. In addition, each grid site recognizes neighbors and any intermolecular bonding that occurs within two times the metal-metal distance.

### Supplementary Simulation Objects

The interaction model object calculates the lateral interaction energy between different species as a function of their distance on the grid. In this work, we use a model that describes the interaction energy as a function of distance between adsorbates. This is termed the radial function (RF) model. Various different interaction models can easily be substituted into the simulation. The model was derived from a series of extended Hückel calculations of the interaction energies between different adsorbates at different coverages as will be discussed.

Surface scenarios are another object specific to our approach. Scenarios are structured events that can occur on the surface based on the local environment. The scenario builder is used to build possible reaction scenarios. Generally, input to the scenario builder includes two grid sites, a surface reaction, and an interaction model. Based upon the occupancy of the grid sites involved, the scenario builder then decides whether the reaction is possible. If the reaction is possible, more detailed calculations are performed. First, the builder decides whether the two chosen sites are within an acceptable proximity for the chosen reaction to occur. This decision is based on whether the distance between sites is less than the sum of the reactants' reaction radii. Second, if the two sites are within an acceptable proximity, the scenario builder must then determine the product state for the reaction. This is not trivial for a multisite grid. Consider the reaction of ethylene in a bridging site and hydrogen in a hollow site to form ethyl in an atop site. This reaction involves at least three sites since the overall metal ensemble must contain the bridging and three fold sites to accommodate the reactant as well as the atop product site. In order for the computer to follow multiple site reactions, it becomes necessary to define a protocol that relates the location of the product site(s) to those of the reactant site(s). The protocol developed here defines the product sites based on reflection and/or intermediate sites shown in Fig. 3. An intermediate site is defined by the user as a central site between two product (or reactant) fragments. This site may be necessary in order to model pairwise adsorption, pairwise desorption, surface reaction, and surface diffusion steps. If the intermediate site for these reactions is occupied, the reaction is disallowed. A reflection site is required for particular surface dissociation events. The reflection site is an alternate location where the dissociation fragment ends up on the surface. The pathway to a reflection site is also defined by the user, but it can be loosely quantified as the reflection of the second reactant site across the first site through a plane intersecting the first site and normal to the vector between the first and the second sites. This is shown schematically in Fig. 3. At longer distances, the reflection site is chosen to be as close to the initial site as possible along the vector between the first site and the reflection site. The reverse reaction of the above example, i.e., ethyl dissociation from the atop position to form a product state of both ethylene and hydrogen in bridging configurations, is an example of where a reflection site is needed. The occupancy and the binding energy in both the intermediate and the reflection sites affect the calculated reaction probabilities. We also note

![](./images/812456812748996610_3.jpg)

FIG. 3. Example of reflection and intermediate grid sites required for dissociation and reaction events with a multisite Monte Carlo approach.

that this results in a multisite Monte Carlo approach. So, although two sites are chosen, many are involved in the developing scenario. This is an attractive and realistic aspect of our method that has not yet been presented in the literature.

Should the scenario builder decide that a specific scenario is possible, a complex series of calculations to compute binding energies of reactants, intermediates, and products is performed at the appropriate surface sites. To model the effects of the local environment on the activation energies of surface processes, we have modified the activation barrier prediction methods in the bond order conservation (BOC) model developed by Shustorovich and Bell (42). In our approach, the reference states we use are density functional theory (DFT) calculations of the activation energies in the zero coverage limit. The equations given below are taken from Shustorovich and Bell for surface processes. However, the transition state energy for each reaction process is modified by a constant factor $\gamma$. This factor is used to force the BOC calculated activation energies to equal the intrinsic kinetics predicted by DFT that are input into the simulation. Consistency is maintained by scaling both the forward and the reverse reactions by the same factor $\gamma$. Written in general form, the binding energies of adsorbates A, B, and AB are given by $Q_{\text{A}}$, $Q_{\text{B}}$, and $Q_{\text{AB}}$ and the bond dissociation energy of a molecule AB is given by $D_{\text{AB}}$. The equations are formulated in terms of the BOC estimated barrier for dissociation of an AB molecule from the gas phase to the surface given by (33):

$$
\Delta E_{\mathrm{AB}, \mathrm{g}}^{*, \mathrm{LJ}}=D_{\mathrm{AB}}-\left(Q_{\mathrm{A}}+Q_{\mathrm{B}}\right)+\frac{Q_{\mathrm{A}} \cdot Q_{\mathrm{B}}}{Q_{\mathrm{A}}+Q_{\mathrm{B}}} \tag{1}
$$

This equation is a balance of the energy required for the dissociation of AB in the gas phase and the energy gained by adsorption of the products A and B plus an extra resistance term based on product binding energies.

Bond Breaking

AB dissociation from gas $(\mathrm{A}-\mathrm{B}+{ }^{*} \rightarrow \mathrm{A}^{*}+\mathrm{B}^{*})$

$$
\Delta E_{\mathrm{AB}, \mathrm{g}}^{*}=0.5 \cdot\left(\Delta E_{\mathrm{AB}, \mathrm{g}}^{*, \mathrm{LJ}}-Q_{\mathrm{AB}}\right)+\gamma \tag{2}
$$

AB dissociation on the surface $(\mathrm{A}-\mathrm{B}^{*}+{ }^{*} \rightarrow \mathrm{A}^{*}+\mathrm{B}^{*})$

$$
\Delta E_{\mathrm{AB}, \mathrm{s}}^{*}=\Delta E_{\mathrm{AB}, \mathrm{g}}^{*}+Q_{\mathrm{AB}} \tag{3}
$$

Bond Making

Surface recombination of A and B $(\mathrm{A}^{*}+\mathrm{B}^{*} \rightarrow \mathrm{A}-\mathrm{B}^{*}+{ }^{*})$

$$
\Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{s}}^{*}=Q_{\mathrm{A}}+Q_{\mathrm{B}}-D_{\mathrm{AB}}+\Delta E_{\mathrm{AB}, \mathrm{g}}^{*} \tag{4}
$$

Recombination of A and B to the gas phase $(\mathrm{A}^{*}+\mathrm{B}^{*} \rightarrow \mathrm{A}-\mathrm{B}+{ }^{*})$

$$
\Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{g}}^{*}=\Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{s}}^{*, \mathrm{LJ}} \quad \text{if } \Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{g}}^{*, \mathrm{LJ}} \geq 0 \tag{5}
$$

else

$$
\Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{g}}^{*}=Q_{\mathrm{A}}+Q_{\mathrm{B}}-D_{\mathrm{AB}}+\gamma=\Delta E_{\mathrm{A}-\mathrm{B}, \mathrm{s}}^{*}-\Delta E_{\mathrm{AB}, \mathrm{g}}^{*}+\gamma.
$$

Equations [1]–[5] provide activation barriers for all bond breaking and making scenarios that arise in the simulation. The activation energy for desorption of surface species without bond breaking or making is given by the binding energy. We define the adsorption rate of gaseous species $i$ for each surface site as

$$
r_{\mathrm{ads}, \mathrm{i}}=S_{\mathrm{o}} \cdot P_{i} \cdot \mathrm{Area} \cdot\left(2 \cdot \pi \cdot \mathrm{MW}_{i} \cdot R \cdot T\right)^{-0.5} \exp \left(-\frac{E_{\mathrm{a}}}{R T}\right), \tag{6}
$$

where $S_{\mathrm{o}}$ is the sticking coefficient for the adsorption process, $P_{i}$ is the partial pressure of the adsorbing species, Area is the area of one surface site (metal-metal distance$^{2}$/4), $\mathrm{MW}_{i}$ is the molecular weight of $i$, and $E_{\mathrm{a}}$ is the activation energy for adsorption.

Monte Carlo Approach to Surface Kinetics

The simulation object inventories all possible scenarios, determines the outcome, equilibrates the surface, performs the simulation analysis, and generates the output. A rough outline of the Monte Carlo algorithm is shown in Fig. 4.

![](./images/812456812748996610_4.jpg)

FIG. 4. Schematic flowchart illustrating the variable time step Monte Carlo approach for simulating surface chemistry and kinetics.

The grid initially contains no surface adsorbates. The total rate of all events is calculated by summing the rates of all possible scenarios. Pairwise reactions are evaluated by examining all interacting pairs (adsorbates that are less than two times the M-M distance on the surface) and testing all possible surface reactions for each pair. Unimolecular adsorption and desorption steps are also evaluated at each surface site. All possible surface scenarios along with associated kinetics are computed and then stored. The rates of all scenarios are self-consistently adjusted to offset the inherent difference in the rate of unimolecular and pairwise surface processes that are important for appropriately treating multisite systems. This difference occurs since the surface area of adsorbed species often encompasses more than one grid site.

To compensate, we first calculate a rate constant for each surface process $i$, ($k_i$), based on the number of possible scenarios ($n$) and the corresponding rate of each scenario $j$:

$$
k_{i}=\frac{\sum_{j=1}^{n} k_{i, j}}{n}. \tag{7}
$$

Next, a correction to the number of surface pairs in the ideal limit for each pairwise reaction is calculated. Specifically, the correction ($C$) is defined as

$$
C_{\mathrm{AB}}=\frac{P_{\mathrm{AB}}}{P_{\mathrm{A}} \cdot P_{\mathrm{B}}} \cong \frac{\theta_{\mathrm{AB}}}{\theta_{\mathrm{A}} \cdot \theta_{\mathrm{B}}}, \tag{8}
$$

where $P_{\mathrm{AB}}$ is the probability of encountering a surface AB pair, and $P_{\mathrm{A}}$ and $P_{\mathrm{B}}$ are the probabilities of encountering A and B, respectively. This factor is used to estimate the true rate of pairwise surface processes using a traditional rate equation. For example, the surface reaction rate ($r$) for the reaction of $\mathrm{A}+\mathrm{B} \rightarrow \mathrm{AB}$ is

$$
\begin{aligned}
r_{\mathrm{AB}} &=\frac{z \cdot M}{2} \cdot C_{\mathrm{AB}} \cdot k_{\mathrm{AB}} \cdot \theta_{\mathrm{A}} \cdot \theta_{\mathrm{B}} \\
&=\left(\frac{z \cdot M}{2 \cdot n} \cdot C_{\mathrm{AB}} \cdot \theta_{\mathrm{A}} \cdot \theta_{\mathrm{B}}\right) \cdot \sum_{j=1}^{n} k_{\mathrm{AB}, j}, \tag{9}
\end{aligned}
$$

where $z$ is the surface coordination (4 for the 100 surface), $M$ is the number of metal atoms, and $\theta$ is the adsorbate surface concentration. Similar equations can be developed for the other pairwise processes. The concentration of surface vacancy sites ($\theta_{*}$) depends on the adsorbate size through the number of sites capable of accepting the adsorbate; i.e., the interaction energy does not exceed the binding energy.

After recalculating the rate of all surface scenarios, we then classify each reaction as being either in equilibrium or dynamic based on its overall forward and reverse rates as calculated by Eq. [7]. The rates of all dynamic processes are then summed to give a total surface rate. Time is computed by drawing a random number and substituting into

$$
\Delta t_{\mathrm{v}}=\frac{-\ln (\mathrm{RN})}{\sum_{i} r_{i}}, \tag{10}
$$

where $\Delta t_{\mathrm{v}}$ is the variable time step, $\sum r_{i}$ is the sum of the rates of all dynamic surface processes given by Eq. [9], and RN is a random number between 0 and 1. The reaction that occurs in the calculated time step is then chosen by sampling a cumulative probability distribution based on a selectivity for each event

$$
\text { Selectivity of reaction AB, Event } 2=\frac{r_{\mathrm{AB}, 2}}{\sum_{i} r_{i}}, \tag{11}
$$

where $r_{\mathrm{AB}, 2}$ denotes the corrected rate constant. The resulting stochastic Monte Carlo approach proceeds through event-space, following events and updating the time and surface structure. This enables us to follow spatiotemporal surface compositions. Diffusion for the systems studied here is assumed to be an equilibrium process. All equilibrium processes are allowed to occur after every time step using the Metropolis algorithm (43).

## Results for Ethylene Hydrogenation

The input to the simulation involves a set of binding and reaction energies. To model surface coverage-dependent kinetics, an interaction model that is based on a series of extended Hückel calculations was developed. Simulated turnover frequencies are determined by maintaining background reactant partial pressures and holding the temperature constant. Observed kinetics are represented here as turnover frequencies, including the activation energy and reaction orders with respect to hydrogen and ethylene.

## Reaction Thermodynamics and Kinetics

The results from a series of DFT calculations for ethylene hydrogenation kinetics are presented in Fig. 5. The

![](./images/812456812748996610_5.jpg)

FIG. 5. Potential energy diagram for ethylene hydrogenation on Pd(100) as determined through DFT calculations and literature estimates.

<table>
<caption>TABLE 1<br>DFT Calculated Binding Energies Used in the Simulation of Ethylene Hydrogenation on Pd(100)</caption>
<thead>
  <tr>
    <th>Energy (kcal/mol)</th>
    <th>Atop</th>
    <th>Bridging</th>
    <th>Hollow</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Hydrogen</td>
    <td>47.3</td>
    <td>58.3</td>
    <td>62.9</td>
  </tr>
  <tr>
    <td>Ethylene</td>
    <td>7</td>
    <td>14</td>
    <td>—</td>
  </tr>
  <tr>
    <td>Ethyl</td>
    <td>31</td>
    <td>17.9</td>
    <td>—</td>
  </tr>
</tbody>
</table>

*Note.* See Ref. (44).

energy diagram here is estimated to be the isolated reactants on the surface, or more specifically the zero coverage limit. Reactant adsorption modes and corresponding energies were inferred from DFT calculations (44, 53). Table 1 highlights the binding energies that are used in the simulation. Figure 5 is simplified since only the most favorable adsorption energies were used in constructing the potential energy diagram shown. For example, the desorption energy of ethylene is given as 14 kcal/mol from a di-$\sigma$ configuration instead of 7 kcal/mol from a $\pi$ configuration. In the simulation, however, all modes remain possible. Although lateral interactions are ignored in this energetic diagram, they are included in the simulation. To complete the intrinsic kinetic database, the preexponential factors shown in Fig. 1 were assumed to be $10^{13}\text{s}^{-1}$ except for the desorption of ethylene, which was taken as $10^{9}\text{s}^{-1}$ from the literature (14). These values are consistent with transition state theory. The sticking coefficients for ethylene and hydrogen were chosen to be 1 and 0.1, respectively, based on results reported in a previous modeling study (46).

The binding energies and activation energies for ethylene hydrogenation kinetics were determined through DFT calculations for Pd(111) (44). We make an assumption based on BOC principles that the adsorbate binding energy does not change very much between the (111) and (100) surfaces for atop and bridging sites. On the bare Pd(100) surface, ethylene prefers the di-$\sigma$ adsorption site. DFT calculations predict a binding energy of 14–15 kcal/mol. This is consistent with the experimental desorption barrier for ethylene of 13 kcal/mol on Pd(111) (14). Hydrogen prefers the hollow sites on both the Pd(111) and the Pd(100) surfaces. The DFT-computed binding energy for hydrogen is 61.4 kcal/mol for a full monolayer of hydrogen on Pd(111) (53). At lower surface coverages, the adsorption energy is somewhat stronger. Repulsive interactions between surface hydrogen atoms at a full monolayer are approximately 2.5 kcal/mol (58). We therefore used a value of 62.9 kcal/mol, consistent with a modeling study by Wilke *et al.* that suggested a binding energy of 62.9 kcal/mol in the no-neighbor limit for Pd(100) (48). The experimental binding energy for hydrogen on Pd(111) and Pd(100) is 62.1 and 63.6 kcal/mol, respectively (55). The ethyl intermediate that forms prefers to sit at an atop adsorption site with a binding energy of 31 kcal/mol (44, 53). An activation barrier for the hydrogenation of ethylene to ethyl was computed to be 16.5 on a Pd(111) cluster (44) and 19.6 kcal/mol on a high-coverage Pd(111) slab (53). The barrier for the second hydrogenation step was computed to be 16.0 kcal/mol in the low coverage limit (44). Both hydrogenation barriers used in the simulation (15 and 14.5 kcal/mol) are just 1.5 kcal/mol lower than barriers that were later calculated directly from DFT. In addition, the magnitude of the hydrogenation barriers is also corroborated through experiments on Pt(111) (9).

### Interaction Model

To simulate the coverage dependence of H, $\text{C}_{2}\text{H}_{4}$, and $\text{C}_{2}\text{H}_{5}$ on the Pd(100) surface, lateral interactions were calculated through a series of extended Hückel theory (EHT) calculations on model metal clusters. In this model, 1750 interaction ensemble calculations were performed to determine the energy of the system as a function of coverage. These EHT calculated interaction energies were calculated consistently by *cutting out* grids from the surface for representative surface structures that were found during a preliminary simulation with a BOC interaction model. First, an adsorbate is chosen to calculate the interaction energy. Then, metal atoms and adsorbates within a cutoff radius (2.5 times the bulk Pd–Pd distance) are *cut* from the surface and included in an EHT interaction energy calculation. A model was then developed to describe the results in terms of simple pairwise interactions. This model was subsequently fitted to the EHT data to determine its parameters. The interactions in the model are based solely on the distance of separation between two adsorbates. Therefore, the interaction model is termed the Radial Function model. The RF interaction model used in the kinetic studies of ethylene hydrogenation is outlined in Fig. 6. A more sophisticated approach would be to regress the EHT parameters against DFT calculations. The model consists of 12 parameters for this three-component system. The first interaction constant, $\zeta_{ij}$, scales the interactions and accounts for cross-terms between adsorbates. The second interaction constant, $\varepsilon_{i}$, is a relative measure of how quickly the interactions decay

$$
\text{Interaction}(r)=\frac{\zeta_{ij}}{2}\left[\frac{\exp(-(r-\gamma_{ij})/\varepsilon_{i})}{r}+\frac{\exp(-(r-\gamma_{ij})/\varepsilon_{j})}{r}\right]
$$

$$
\gamma_{ij}=\frac{\gamma_{i}+\gamma_{j}}{2}
$$

![](./images/812456812748996610_6.jpg)

**FIG. 6.** Radial function interaction model used in simulations of ethylene hydrogenation. The model was found via regression of 1750 interaction calculations using extended Hückel as described in the text. *r* is in angstroms.

with distance. The third interaction constant, $\gamma_i$, is a relative measure of the physical size of the adsorbates. This model was used for all simulations presented here.

## Hydrogenation Kinetics

Kinetic simulations of ethylene hydrogenation require following the complex sequence of adsorption, surface reaction, surface diffusion, and surface desorption processes. Unless otherwise specified, the ethylene partial pressure was set at 25 Torr and the hydrogen partial pressure was set at 100 Torr. Our goal was to map simulated kinetics to apparent macroscopic kinetics that one would observe experimentally, such as the preexponential factor ($v$), the activation energy ($E_{\text{a}}$), and the reaction orders with respect to hydrogen ($x$) and ethylene ($y$) as shown in

$$
\text{Hydrogenation rate} = v \cdot \exp\left(\frac{-E_{\text{a}}}{R \cdot T}\right) \cdot P_{\text{H}_2}^x \cdot P_{\text{C}_2\text{H}_4}^y. \quad [12]
$$

Turnover frequencies are calculated by counting the number of ethane molecules that desorb from the surface in a given time interval. The uncertainty of calculating turnover frequencies is associated with how many desorption events can be observed over a reasonable amount of time. We have found that approximately 100 desorption events is a compromise between accuracy and calculation time provided the coverage is at steady state. An example of one such measurement of a turnover frequency is shown in Fig. 7. In order to resolve the turnover frequency from the calculation results, the raw data for ethane desorption as a function of time are fitted to both a first-order exponential decay and a line. The long-time behavior is the turnover frequency and is given by the slope of this line. All measurements are performed subject to this protocol. Turnover frequencies are calculated under different reaction conditions and subsequently used to parameterize Eq. [12]. We find that the effect of grid size is not substantial for these simulations. This has been supported by others (49), so smaller 400 metal atom grids were used. Along with shorter run times, diffusion equilibrium is achieved more easily using this smaller grid.

![](./images/812456812748996610_7.jpg)

FIG. 7. Example of simulation data and how turnover frequencies are extracted from these data. The raw simulation data are fitted to a line and a first-order decay with the slope of the line representing the turnover frequency.

![](./images/812456812748996610_8.jpg)

FIG. 8. Arrhenius plot for ethylene hydrogenation. The partial pressure of hydrogen is 100 Torr and the partial pressure of ethylene is 25 Torr. The activation energy according to Eq. [12] varies from 12 kcal/mol at 248 K to 9 kcal/mol at 436 K.

The simulation was run at a series of temperatures to extract Arrhenius data. Figure 8 shows a traditional Arrhenius plot of the turnover frequency at the temperatures of 248, 273, 298, 336, 386, and 436 K. $E_{\text{a}}$ and $v$ vary over this temperature range. The activation energy ranges from 12 kcal/mol at lower temperatures to 9 kcal/mol at higher temperatures. These values are in good agreement with measured experimental values which range from 6–11 kcal/mol. An average value of $v$ is $\sim10^6 \text{kPa}^{-0.5} \text{s}^{-1} \text{site}^{-1}$ and this compares well with an experimental value of $2 \times 10^6 \text{kPa}^{-0.5} \text{s}^{-1} \text{site}^{-1}$ (16). An experimental estimate for Pd hydrogenation at 248 K is a turnover frequency of 7, whereas simulations suggest a turnover frequency of $2 \times 10^{-3}$. We are comparing simulation results from a well-defined single crystal Pd(100) surface with experimental results on supported particles. Only trends, and not quantitative agreement, in the magnitude of the turnover frequency are expected. Figure 8 also shows the effect of grid size on reaction kinetics.

The partial pressures of both ethylene and hydrogen were varied to determine their respective kinetic orders. The orders were found by regressing the coefficients in Eq. [12] to the kinetic data. The reference state used was 25 Torr of

![](./images/812456812748996610_9.jpg)

FIG. 9. Simulation orders with respect to hydrogen and ethylene at 298 K using a $20 \times 20$ grid. For reference, pressures are given as 25 Torr of ethylene and 100 Torr of hydrogen. The order with respect to ethylene varies from $-0.4$ to 0. The order with respect to hydrogen is more constant, ranging from 0.65 to 0.85.

ethylene and 100 Torr of hydrogen. In Fig. 9, we show the resulting simulation orders with respect to ethylene and hydrogen at 298 K. The hydrogen order was 0.85 at higher partial pressures of hydrogen and decreases slightly to 0.65 at lower hydrogen partial pressures. The kinetic order with respect to ethylene varied more substantially with ethylene partial pressure. At lower partial pressures of ethylene, the ethylene order was $-0.4$, whereas at higher partial pressures of ethylene the ethylene order was near zero or slightly positive.

Table 2 lists simulated binding energies, surface coverages, and estimated barriers for surface reactions at different temperatures. These values are averaged over the final quarter of the simulation run, when the system is closest to equilibrium. Most of the simulation runs appear to have achieved a near-equilibrium state, as shown by the estimated rates. Unimolecular desorption barriers reported here are shown as the binding energies. The activation barrier for reaction $i$ is estimated with the protocol

$$
E_{i}=-R T \cdot \ln \left(\frac{\bar{r}_{i}}{v_{i} \cdot \frac{z}{2} \cdot M \cdot f(\bar{\theta})_{i}}\right), \tag{13}
$$

where $f(\theta)$ is a function of the surface coverage, e.g., $\theta_{\mathrm{A}} \theta_{\mathrm{B}}$ for reaction of A and B on the surface. Overbars in Eq. [13] denote the simulation average. In formulating the activation energy in this manner, several assumptions were made that are common for analyzing reaction rates. First, it is assumed that the preexponential and statistic factors are ideal. Second, site balance reclaims the surface vacancy concentration by assuming all site concentrations sum to 1

<table>
<caption>TABLE 2 Simulation Variables for a $20 \times 20$ Grid Size as a Function of Temperature</caption>
<thead>
<tr>
<th></th>
<th>436 K</th>
<th>386 K</th>
<th>336 K</th>
<th>298 K</th>
<th>273 K</th>
<th>248 K</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">Coverage (ML)</td>
</tr>
<tr>
<td>Hydrogen</td>
<td>0.157</td>
<td>0.276</td>
<td>0.419</td>
<td>0.422</td>
<td>0.508</td>
<td>0.568</td>
</tr>
<tr>
<td>Ethylene</td>
<td>0.141</td>
<td>0.136</td>
<td>0.146</td>
<td>0.182</td>
<td>0.178</td>
<td>0.178</td>
</tr>
<tr>
<td>Ethyl</td>
<td>0.00244</td>
<td>0.00243</td>
<td>0.0024</td>
<td>0.0021</td>
<td>0.0021</td>
<td>0.0021</td>
</tr>
<tr>
<td colspan="7">Binding energy (kcal/mol)<sup>a</sup></td>
</tr>
<tr>
<td>Hydrogen</td>
<td>62.7</td>
<td>62.6</td>
<td>62.5</td>
<td>62.5</td>
<td>62.4</td>
<td>62.4</td>
</tr>
<tr>
<td>Ethylene</td>
<td>13</td>
<td>12.8</td>
<td>12.1</td>
<td>9.05</td>
<td>8.81</td>
<td>8.69</td>
</tr>
<tr>
<td colspan="7">Estimated rates (TOF)<sup>b</sup></td>
</tr>
<tr>
<td>Ethyl dissociation</td>
<td>5400</td>
<td>1200</td>
<td>110</td>
<td>8.7</td>
<td>1.1</td>
<td>0.09</td>
</tr>
<tr>
<td>Ethylene hydrogenation</td>
<td>5400</td>
<td>1200</td>
<td>130</td>
<td>12</td>
<td>1.9</td>
<td>0.06</td>
</tr>
<tr>
<td>Ethyl hydrogenation</td>
<td>13</td>
<td>3</td>
<td>0.72</td>
<td>0.015</td>
<td>0.007</td>
<td>0.004</td>
</tr>
<tr>
<td>Hydrogen desorption</td>
<td>11</td>
<td>1.6</td>
<td>0.065</td>
<td>0.0011</td>
<td>$7.5 \times 10^{-5}$</td>
<td>$1.9 \times 10^{-6}$</td>
</tr>
<tr>
<td>Hydrogen adsorption</td>
<td>27</td>
<td>8.3</td>
<td>0.79</td>
<td>0.18</td>
<td>0.022</td>
<td>0.0018</td>
</tr>
<tr>
<td colspan="7">Barrier estimates (kcal/mol)<sup>c</sup></td>
</tr>
<tr>
<td>Ethyl dissociation<sup>d</sup></td>
<td>4.4–8.3</td>
<td>5.0–8.4</td>
<td>5.6–8.7</td>
<td>6.1–9.1</td>
<td>6.4–9.3</td>
<td>6.7–9.5</td>
</tr>
<tr>
<td>Ethylene hydrogenation<sup>d</sup></td>
<td>10.6</td>
<td>11.0</td>
<td>11.3</td>
<td>11.6</td>
<td>11.7</td>
<td>12.4</td>
</tr>
<tr>
<td>Ethyl hydrogenation</td>
<td>8.2–12.3</td>
<td>9.0–12.5</td>
<td>9.0–12.1</td>
<td>9.9–12.9</td>
<td>9.4–12.3</td>
<td>8.8–11.6</td>
</tr>
<tr>
<td>Hydrogen desorption</td>
<td>16.2</td>
<td>16.6</td>
<td>17.1</td>
<td>17.6</td>
<td>17.8</td>
<td>18.1</td>
</tr>
<tr>
<td>Hydrogen adsorption</td>
<td>1.2</td>
<td>1.8</td>
<td>2.7</td>
<td>3.2</td>
<td>3.9</td>
<td>4.6</td>
</tr>
</tbody>
</table>

Note. Binding energies are in kcal/mol, surface coverages are in ML, and reaction rates on a turnover basis are roughly estimated over simulation time.

<sup>a</sup> Ethyl binding energy measures between 30.9 and 31 kcal/mol for all runs.
<sup>b</sup> Ethylene adsorption in equilibrium.
<sup>c</sup> Assumes $\theta_{*}=1-\sum \theta_{i}$ and an ideal form for preexponential and statistical factors.
<sup>d</sup> Uncertainty due to low ethyl concentrations at minimum grid coverage.

(see Table 2). The assumption of site balance can introduce large errors since vacancy concentrations are different for different species and the saturation coverage for ethylene and ethyl is less than 1 ML. With these assumptions, changes in the barriers shown in Table 2 may be due to deviations from nonideality of the preexponential factor. Therefore, the barriers in Table 2 are only estimates and should not be compared rigorously with zero coverage values presented in Fig. 5. The trends are more important and demonstrate significant changes from ideality of the reaction rates of these elementary reaction steps.

Surface coverage is an important factor in hydrogenation kinetics. As expected, surface coverage decreases as the temperature increases. Surface coverage of ethylene changes only slightly from 0.18 ML at 248 K to 0.14 ML at 436 K. Coverage changes in hydrogen are much more pronounced, from 0.57 ML at 248 K to 0.16 ML at 436 K. Higher surface coverages are indicative of greater repulsive surface interactions that influence both the binding energies of adsorbates and the reaction rates.

Table 2 shows a consistent increase with temperature in the time-averaged simulated binding energies, coinciding with a reduction in surface coverage. The binding energy of ethylene is 8.7 kcal/mol at 248 K and increases to 13 kcal/mol at 436 K. There is a weaker dependence of temperature on the hydrogen binding energy. At 248 K, the binding energy of hydrogen is 62.4 kcal/mol and increases to only 62.7 kcal/mol at 436 K. However, hydrogen occupies states between 55 and 60 kcal/mol for very short time periods, but these states do not contribute significantly to the time-averaged binding energy.

The estimates of the barrier heights reported in Table 2 show a trend of decreasing activation energy with increasing surface temperature. This seems counterintuitive, since a reduction in binding energy should lead to reduced barriers. A reduction in the barrier with increasing temperature can be associated with three phenomena. First, the aforementioned changes in the statistical factor are reflected in the estimated barrier; Second, there is a change in the distribution of energy states for surface pairs. Plots of the density of binding energy states suggest differences here. Third, there is a change in surface overlayer structure that allows sites to be populated as the surface coverage decreases that previously could not be populated due to site blocking. For example, ethyl adsorption requires a large vacancy site that is difficult to create on the surface at high coverages.

Relative trends in activation energies are revealed in Table 2 for the first and second hydrogenation steps. During the simulation, the initial hydrogenation step is in equilibrium. While the simulated barrier for the initial hydrogenation step is comparable to or greater than that of the second hydrogenation step, the simulated barrier for the reverse reaction of ethyl dissociation back to ethylene and hydrogen is low. Therefore, ethyl is more likely to react back to ethylene and hydrogen than to hydrogenate to form ethane. A cyclic pattern within the simulation emerges where ethylene reacts with hydrogen only to dissociate again back to ethylene and hydrogen, i.e., hydrogen exchange. If a second hydrogen exists in the near vicinity of ethyl at the time of the first hydrogenation, the second hydrogenation step can occur, resulting in the product ethane. The chance that ethylene is surrounded by two hydrogen atoms capable of hydrogenation is dictated by the interaction model. Barrier estimates of the first and second hydrogenation steps suggest greater hydrogen exchange at higher temperatures. As the temperature is increased, the first hydrogenation step becomes consistently more endothermic while the second hydrogenation step changes little in comparison. An increase in hydrogen exchange with temperature has been shown experimentally for Pt catalysts using deuterium tracing (23).

Two snapshots of simulation overlayer structure are shown in Fig. 10. Ethylene is bound in the di-σ position and hydrogen adsorbs in the hollow sites on the surface. In the surface overlayer, hydrogen has a much greater mobility due to its smaller size. Simulations proceed with a sea of hydrogen atoms moving around the more stationary hydrocarbon species. Ethyl and ethylene are less mobile since movement involves strong repulsions with neighboring hydrocarbons. The hydrocarbons occupy greater surface area than the hydrogen atoms do. Since hydrogen does not interact as strongly with the hydrocarbons, it is free to maneuver around and near the hydrocarbons.

The simulation results indicate that the hydrogenation proceeds primarily through a weakly bound di-σ- and π-bound species that occupies only 1.5–4.5% of the catalyst surface. This can be compared to a value of 4% determined on Pt(111) under nearly identical conditions using sum frequency generation (10) techniques to follow the nature of the active surface intermediates. Similar observations for the weakly bound ethylene on Pt(111) have been made by Ofner and Zaera based on molecular beam studies (11). There are, however, differences between the experiments and the simulations. We have not modeled the effect of the decomposition fragments, such as CH, CH₂, CHCH₂, CCH₃, and CHCH₃. Ethylene hydrogenation experiments on Pd/Al₂O₃ show the formation of ethylidyne (CCH₃) with a saturation coverage of about 15% (20). Pd(111) forms ethylidyne quite readily (14). Other carbonaceous deposits are more favorable than ethylidyne for Pd(100) (45). Despite a significant coverage of ethylidyne on Pd/Al₂O₃, ethylene hydrogenation is not significantly affected (20). Although the role of ethylidyne and other carbonaceous deposits on ethylene hydrogenation has yet to be determined, experiments on Pt suggest that these species block sites for ethylene adsorption and are of secondary importance (10–12). Pathways to decomposition fragments can be included in this approach; however, establishing

![](./images/812456812748996610_10.jpg)

FIG. 10. Snapshots of the surface during ethylene hydrogenation at 298 K, 25 Torr of ethylene, and 100 Torr of hydrogen.

kinetics and interactions between species would take a much greater effort. Therefore, only the elementary reactions in the Horiuti-Polanyi mechanism and interactions between ethylene, ethyl, and hydrogen were explored here.

## DISCUSSION

The RF model used here is different than the interaction model we previously reported (50). The RF model we report here was found directly from EHT cluster interactions and not scaled to match any experimental data. However, trends in kinetics results are not greatly affected. We believe that the RF model has a greater self-consistency than arbitrarily choosing different functions for different interactions. The RF model is simple and the parameters appear to be meaningful. In addition, the database of hundreds of EHT calculations ensures that the values are statistically relevant. The parameters in the RF model are regressed over the entire database. As shown in Fig. 6, the RF model predicts little interaction between hydrogen and the hydrocarbons (ethene and ethyl). In fact, many EHT configurations suggested a slight attraction between ethyl and hydrogen. Both ethyl and ethylene have interaction energies of comparable magnitude. However, ethyl interactions are more expansive. As one may expect intuitively, ethyl seems to occupy a larger area on the surface while hydrogen occupies the least surface area as can be seem from $\varepsilon_{i}$ and $\gamma_{i}$.

In general, simulated apparent activation energies and kinetic orders are in good agreement with those determined experimentally. Experimentally reported activation energies vary between 6 and 11 kcal/mol where literature values have been cited as 10.7 (22), 10.4 (4), 9.7 (18), 9.3 (15), 8.4 (24), and 6.5 (16) kcal/mol for Pd catalysts. This compares favorably with a simulated activation energy of 9-12 kcal/mol. Overall, activation energies and kinetic orders agree with the comprehensive set of experimental kinetic studies of ethylene hydrogenation on Pt (7, 46) and Pd (16, 20). Beebe and Yates studied ethylene hydrogenation on $\mathrm{Pd} / \mathrm{Al}_{2} \mathrm{O}_{3}$ crystallites with an average particle size of $75 \AA$ (20) under conditions of 0.05-0.4 Torr in ethylene and hydrogen and 250-400 K. Under these conditions, the activation barrier was found to decrease slightly with increasing temperature, suggesting a decrease in equilibrium surface concentration of reactant species leading to lower rates. Since the pathway to ethane production involves two recombinative steps, the drop in the turnover frequency becomes more substantial. Experimentally at 292 K, the kinetic order with respect to hydrogen was calculated to be 0.84-0.98 while the kinetic order with respect to ethylene was -0.3-0. Davis and Boudart also studied ethylene hydrogenation kinetics on Pd at 193 K and at partial pressures similar to those simulated here (16). They found that at these temperatures, the hydrogen kinetic order is 0.5 and the ethylene kinetic order is 0. On Pt/Cab-O-Sil and Pt wire catalysts, the activation energy is ~9.5 kcal/mol and the hydrogen and ethylene kinetic orders are 0.77 and -0.2 at the same temperature and partial pressures simulated herein (46). Simulated orders in hydrogen of 0.65-0.85 and in ethylene of -0.4-0 compare well with these experimental measurements.

For ethylene hydrogenation on Pt, a microkinetic model reported in the literature explains the kinetic data using a noncompetitive adsorption model where hydrogen adsorbs on two different sites (46). Hydrogen adsorption is thought to occur either on the same site that ethylene adsorbs on

(competitively) or on a site that does not adsorb ethylene (noncompetitively). In the noncompetitive adsorption model, hydrogen kinetic orders vary between 0.5 and 1. For kinetic orders that are 0.5 in hydrogen, the model asserts that dissociation of hydrogen is an equilibrated process on the noncompetitive site and the surface is covered with hydrocarbons on the competitive adsorption site. First-order hydrogen kinetics then result when the adsorption of hydrogen becomes irreversible, adsorbing on either the competitive or the noncompetitive adsorption site. Furthermore, the noncompetitive adsorption model predicts negative ethylene kinetic orders. These negative ethylene kinetic orders are a result of a more competitive adsorption between hydrogen and ethylene on the competitive adsorption site as the surface coverage (of ethylene) decreases. Therefore, a competitive hydrogenation mechanism begins to supplement the noncompetitive mechanism.

The nature of the kinetic orders for ethylene and hydrogen are best explained in terms of changes in surface coverage, the size difference between ethylene and hydrogen, lateral interactions on the surface, and different adsorption sites for ethylene and hydrogen with different energetics. In many respects, the simulation results can be construed as being similar to a deterministic competitive adsorption model. However, the simulation results are different than the competitive adsorption model in many notable respects that have been drawn out by the simulations. The surface adsorption size of ethylene and hydrogen is unequal and not integer based. Most mathematical reaction models developed for ethylene hydrogenation assume that ethylene occupies exactly two sites and hydrogen exactly one. Stochastic simulations allow us to maintain a better accounting of molecular size associated with surface interactions. However, the earlier competitive deterministic models that exist in the literature where ethylene and hydrogen adsorb on the same type of site are rough approximations since the type and size of the active site are notably different. A noncompetitive adsorption model can begin to compensate for this size difference by allowing noncompetitive adsorption sites for hydrogen adsorption at higher coverages. However, this does not directly correspond to the adsorption mechanism. Simulations suggest that hydrogen kinetic orders may be the consequence of lateral interactions on the surface and different sites for hydrogen adsorption and not reversibility of the hydrogen adsorption step. At low temperatures, a kinetic model by Davis and Boudart highlights irreversible hydrogen adsorption and tries to explain the hydrogen half-order reaction kinetics in terms of interactions in the overlayer (16). Simulations show no reversibility of hydrogen adsorption at lower temperatures, yet we note that we do not allow molecular adsorption of hydrogen without dissociation. Furthermore, these simulations suggest that ethylene adsorption is more reversible than hydrogen adsorption. Although simulations predict hydrogen orders less than one, our results suggest that this is due to interactions or energetically different adsorption states that are close in energy in the overlayer rather than reversibility of hydrogen adsorption. In fact, simulations show that the relative magnitude of the lateral interactions increases with decreasing temperature due to higher surface coverages. Therefore, a kinetic order in hydrogen of 1 occurs at high temperatures with fewer interactions, while kinetic orders are reduced as the temperature is decreased. Simulations also suggest that the ethylene kinetic order is a more complex function of lateral interactions. Variation in the ethylene partial pressure in Fig. 9 seemed to produce a more weakly bound ethylene at lower partial pressures of ethylene, thereby increasing its hydrogenation rate. A more weakly bound ethylene in this instance may be associated with an increase in hydrogen coverage that destabilizes the ethylene through an increased number of surface interactions. However, the change in hydrogen coverage seemed to increase only slightly or remain constant. We also note that EHT calculations suggest that the interaction between ethyl and hydrogen may in fact be attractive in certain configurations and warrants further study since the RF interaction model is incapable of including attractive interactions explicitly.

## CONCLUSIONS

First-principles DFT calculations were performed for ethylene hydrogenation on Pd. The energies were found to adequately describe the kinetics of ethylene hydrogenation in the low (zero) coverage limit where there are no lateral surface interactions. Interactions between ethyl, ethylene, and hydrogen on the surface are described by an interaction model (Fig. 6) that was derived from 1750 extended Hückel calculations. Interaction model parameters are feasible with respect to the magnitude of the interaction energies and the physical size of ethyl, ethylene, and hydrogen on the surface. Coupling the interaction model and DFT reaction energetics with BOC methods for calculating activation energies is a viable means of estimating coverage dependence in the activation energies.

Using this first-principles-based approach, a multisite kinetic Monte Carlo (Fig. 4) algorithm was used to simulate ethylene hydrogenation kinetics. An apparent activation energy of 9–12 kcal/mol (Fig. 8) compares with experimental estimates of 6–11 kcal/mol on supported palladium catalysts. The simulated activation energy decreases with increasing temperature. In addition, a preexponential of $10^6\ \text{kPa}^{-0.5}\text{s}^{-1}\text{site}^{-1}$ compares well with an experimental value of $2 \times 10^6\ \text{kPa}^{-0.5}\text{s}^{-1}\text{site}^{-1}$ (16). Kinetic orders in both ethylene and hydrogen compare well with available experiments (Fig. 9). At 298 K, the kinetic order in ethylene was –0.4 at lower partial pressures of ethylene and zero at higher partial pressures of ethylene while the hydrogen

kinetic order was nearly constant at 0.8. These values compare well with experimental estimates of a hydrogen order of 0.7–0.9 and an ethylene order of −0.2–0 under similar conditions for Pd and Pt catalysts. Both the apparent activation barriers and the kinetic reaction orders were found to be significantly affected by lateral surface interactions.

## ACKNOWLEDGMENTS

The authors acknowledge the support from the NSF CAREER Award (CTS-9702762) from the National Science Foundation.

## REFERENCES

1. Miller, S. A., "Ethylene and Its Industrial Derivatives" Ernest Benn Limited, London, 1969, and references therein.
2. Derrien, M. L., *Stud. Surf. Sci. Catal.* **27**, 613 (1986).
3. Bos, A. N. R., and Westerterp, K. R., *Chem. Eng. Proc.* **32**, 1 (1993).
4. Beeck, O., *Rev. Mod. Phys.* **17**, 61 (1945).
5. Beeck, O., *Discuss. Faraday Soc.* **8**, 118 (1950).
6. Anderson, A., and Choe, S., *J. Phys. Chem.* **93**, 6145 (1989).
7. Cortright, R., Goddard, S., Reskoske, J., and Dumesic, J., *J. Catal.* **127**, 342 (1991).
8. Cremer, P. S., and Somorjai, G. A., *J. Chem Soc. Faraday Trans.* **91**, 3671 (1995).
9. Zaera, F., *Acc. Chem. Res.* **25**, 260 (1992).
10. Cremer, P., Su, X., Shen, Y., and Somorjai, G., *Catal. Lett.* **40**, 143 (1996).
11. Ofner, H., and Zaera, F., *J. Phys. Chem. B* **101**, 396 (1997).
12. Zaera, F., *Langmuir* **12**, 88 (1996).
13. Zaera, F., Janssens, T., and Ofner, H., *Surf. Sci.* **368**, 371 (1996).
14. Tysoe, W., Nyberg, G., and Lambert, R., *J. Phys. Chem.* **88**, 1960 (1984).
15. Takasu, Y., Sakuma, T., and Matsuda, Y., *Chem. Lett.* **48**, 1179 (1985).
16. Davis, R., and Boudart, M., *Catal. Sci. Technol.* **1**, 129 (1991).
17. Sekitani, T., Takaoka, T., Fujisawa, M., and Nishijima, M., *J. Phys. Chem.* **96**, 8462 (1992).
18. Bos, A. N. R., Bootsma, E. S., Foeth, F., Sleyster, H. W. J., and Westerterp, K. R., *Chem. Eng. Proc.* **32**, 53 (1993).
19. Guo, X., and Madix, R., *J. Catal.* **155**, 336 (1995).
20. Beebe, T. P., and Yates, J. T., *J. Am. Chem. Soc.* **108**, 663 (1986).
21. Horiuti, J., and Polanyi, M., *Trans. Faraday Soc.* **30**, 1164 (1934).
22. Eley, D., *in* "Catalysis" (P. Emmett, Ed.), p. 49. Reinhold, New York, 1955.
23. Goddard, S., Cortright, R., and Dumesic, J., *J. Catal.* **137**, 186 (1992).

24. Schuit, G. C. A., and Reijen, L. L. V., *Adv. Catal.* **10**, 242 (1958).
25. Lombardo, S. J., and Bell, A. T., *Surf. Sci. Rep.* **13**, 1 (1991).
26. Lombardo, S. J., and Bell, A. T., *Surf. Sci.* **245**, 213 (1991).
27. Lombardo, S. J., and Bell, A. T., *Surf. Sci.* **224**, 451 (1989).
28. Kang, H. C., and Weinberg, W. H., *Surf. Sci.* **299/300**, 755 (1994).
29. Kang, H. C., and Weinberg, W. H., *Acc. Chem. Res.* **25**, 253 (1992).
30. Meng, B., and Weinberg, W. H., *J. Chem. Phys.* **102**, 1003 (1994).
31. Meng, B., and Weinberg, W. H., *J. Chem. Phys.* **100**, 5280 (1994).
32. Fichthorn, K., and Weinberg, W. H., *J. Chem. Phys.* **95**, 1090 (1991).
33. Shustorovich, E., and Sellers, H., *Surf. Sci. Rep.* **31**, 1 (1998).
34. Sellers, H., *in* "Catalysis Modeling Employing Ab Initio and Bond Order Conservation—Morse Potential Methods," Vol. 35–56. Plenum, Brookings, SD, 1993.
35. Stampfl, C., Kreuzer, H. J., Payne, S. H., Pfnür, H., and Scheffler, M., *Phys. Rev. Lett.* **83**, 2993 (1999).
36. Parr, R. G., and Yang, W., "Density-Functional Theory of Atoms and Molecules." Clarendon, New York, 1989.
37. Hehre, W. J., Radom, L., Schleyer, P. V. R., and Pople, J. A., "Ab-Initio Molecular Orbital Theory." Wiley, New York, 1986.
38. Neurock, M., *Stud. Surf. Sci.* **109**, 3 (1998).
39. Santen, R. A. V., *in* "Theoretical Heterogeneous Catalysis," Vol. 5. World Scientific, Singapore, 1991.
40. Santen, R. A. V., and Neurock, M., *in* "Theory of Surface-Chemical Reactivity," Vol. 3, p. 991. VCH, Weinheim/New York, 1997.
41. Sautet, P., and Paul, J., *Catal. Lett.* **9**, 245 (1991).
42. Shustorovich, E., and Bell, A., *Surf. Sci.* **222**, 371 (1989).
43. Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., and Teller, E., *J. Chem. Phys.* **21**, 1087 (1953).
44. Neurock, M., and Santen, R. V., Submitted for publication.
45. Stuve, E. M., and Madix, R. J., *J. Phys. Chem.* **89**, 105 (1985).
46. Rekoske, J., Cortright, R., Goddard, S., Sharma, S., and Dumesic, J., *J. Phys. Chem.* **96**, 1880 (1992).
47. Neurock, M., and Hansen, E., *Comput. Chem. Eng.* **22**, S1045 (1998).
48. Wilke, S., Hennig, D., Lober, R., Methfessel, M., and Scheffler, M., *Surf. Sci.* **307–309**, 76 (1994).
49. Duca, D., Baranyai, P., and Vidóczy, T., *J. Comp. Chem.* **19**, 396 (1998).
50. Hansen, E., and Neurock, M., *Chem. Eng. Sci.* **54**, 3411 (1999).
51. Duca, D., Botár, L., and Vidóczy, T., *J. Catal.* **162**, 260 (1996).
52. McLeod, A. S., and Gladden, L. F., *J. Chem. Phys.* **110**, 4000 (1999).
53. Venkataraman, P. S., and Neurock, M., *J. Catal.* **191**, 301 (2000).
54. Hansen, E., and Neurock, M., *Surf. Sci.*, in press.
55. Christmann, K., *Surf. Sci. Rep.* **9**, 1 (1988).
56. Ziegler., *Chem. Rev.* **91**, 651 (1991).
57. Santen, R. A. V., and Neurock, M., *Catal Rev.* **37**, 557 (1995).
58. Neurock, M., Pallassana, V., and Santen, R. A. V., *J. Am. Chem. Soc.* **122**, 1150 (2000).