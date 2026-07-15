![](./images/812121225152167938_1.jpg)

The properties of ion-water clusters. II. Solvation structures of Na + , Cl - , and H + clusters as a function of temperature

Christian J. Burnham, Matt K. Petersen, Tyler J. F. Day, Srinivasan S. Iyengar, and Gregory A. Voth

Citation: *The Journal of Chemical Physics* **124**, 024327 (2006); doi: 10.1063/1.2149375
View online: http://dx.doi.org/10.1063/1.2149375
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/124/2?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
On the stability of ion water clusters at atmospheric conditions: Open system Monte Carlo simulation
J. Chem. Phys. **137**, 124107 (2012); 10.1063/1.4754528

Comment on "Free energy of solvation of simple ions: Molecular dynamics study of solvation of Cl - and Na + in the ice/water interface" [J. Chem. Phys.123, 034706 (2005)]
J. Chem. Phys. **126**, 237101 (2007); 10.1063/1.2737662

Solute size effects on the solvation structure and diffusion of ions in liquid methanol under normal and cold conditions
J. Chem. Phys. **124**, 084507 (2006); 10.1063/1.2172598

The properties of ion-water clusters. I. The protonated 21-water cluster
J. Chem. Phys. **123**, 084309 (2005); 10.1063/1.2007628

Free energy of solvation of simple ions: Molecular-dynamics study of solvation of Cl - and Na + in the ice/water interface
J. Chem. Phys. **123**, 034706 (2005); 10.1063/1.1953578

![](./images/812121225152167938_2.jpg)

THE JOURNAL OF CHEMICAL PHYSICS 124, 024327 (2006)

# The properties of ion-water clusters. II. Solvation structures of Na⁺, Cl⁻, and H⁺ clusters as a function of temperature

Christian J. Burnham, Matt K. Petersen, and Tyler J. F. Day
Department of Chemistry and Center for Biophysical Modeling and Simulation, University of Utah,
315 South 1400 East, Room 2020, Salt Lake City, Utah 84112-0850

Srinivasan S. Iyengar
Department of Chemistry, Indiana University, 800 E. Kirkwood Avenue, Bloomington, Indiana 47405-7102
and Department of Physics, Indiana University, 727 E. Third Street, Bloomington,
Indiana 47405-7105

Gregory A. Voth⁽ᵃ⁾
Department of Chemistry and Center for Biophysical Modeling and Simulation, University of Utah,
315 South 1400 East, Room 2020, Salt Lake City, Utah 84112-0850

(Received 20 October 2005; accepted 14 November 2005; published online 13 January 2006)

Ion-water-cluster properties are investigated both through the multistate empirical valence bond potential and a polarizable model. Equilibrium properties of the ion-water clusters $H^+(H_2O)_{100}$, $Na^+(H_2O)_{100}$, $Na^+(H_2O)_{20}$, and $Cl^-(H_2O)_{17}$ in the temperature region 100–450 K are explored using a hybrid parallel basin-hopping and tempering algorithm. The effect of the solid-liquid phase transition in both caloric curves and structural distribution functions is investigated. It is found that sodium and chloride ions largely reside on the surface of water clusters below the cluster melting temperature but are solvated into the interior of the cluster above the melting temperature, while the solvated proton was found to have significant propensity to reside on or near the surface in both the liquid- and solid-state clusters. © 2006 American Institute of Physics. [DOI: 10.1063/1.2149375]

## I. INTRODUCTION

Small molecular clusters provide a model system for exploring solvation and thermodynamic properties, which can give important insight into macroscopic phenomena. They are also important in their own right for their role in atmospheric chemistry and for understanding molecular properties in the nanoscale regime. In a recent article, Garrett¹ has reviewed at some of the current literature pertaining to ions at the air/water interface, in which it is argued that experiment and simulation support the conclusion that certain ions can reside on (or near) the interfacial region, which has important ramifications for the surface chemistry of aqueous environments. The present work investigates the temperature-dependent solvation of $Na^+$, $Cl^-$, and $H^+$ ions in various water clusters with respect to their equilibrium properties, especially across the solid-liquid phase transition.

Perera and Berkowitz² performed molecular-dynamics simulations using both polarizable and nonpolarizable potentials for both $Na^+(H_2O)_n$ and $Cl^-(H_2O)_n$ clusters. They observed infrequent hops from structures with central $Na^+$ to surface sites and back again along trajectories for the small cluster $n$=4. They did not observe any qualitatively different behavior between polarizable and nonpolarizable models for the cation solvation. Carignano et al.³ performed bulk simulations using polarizable potentials for both $Na^+$ and $Cl^-$ in water. In particular, they examined the variation of trends with polarizability of the ions by performing simulations for varying values of the polarizability. Again, they found that polarizability plays a near negligible role for cations but a very important role for anions. Contradictory results were reported by Stuart and Berne⁴ in a study on the hydration of the chloride ion, in which it was claimed that water, not chloride, polarizability is the critical property. Solvation properties of small ($n$=1–10) ion-water clusters using polarizable potentials have been studied by Dang and co-workers⁵⁻⁷ and Knipping et al.,⁸ and Jungwirth and Tobias⁹,¹⁰ have also performed extensive molecular-dynamics (MD) calculations on $Na^+Cl^-$ water clusters in the size range $n$=9–288 in order to establish the solvation properties and surface concentration of ions. Low-lying stationary points of the potential-energy surface (PES) of singly protonated water clusters $H^+(H_2O)_n$ $n$=2–4,8,20–22 have also been enumerated¹¹⁻¹³ using the second generation multistate empirical valence bond (MS-EVB2) potential,¹²,¹³ *ab initio* calculations,¹⁴ and the Ojamae-Shavitt-Singer (OSS) potential.¹⁵ The effect of temperature on protonated water clusters has also been explored through *ab initio* MD and MS-EVB2 MD simulations.¹³,¹⁴ The latter papers reported for the first time that the proton resides on the surface of large water clusters at finite temperature (e.g., above 150 K).

It is a notoriously difficult problem to calculate equilibrium properties for low-temperature cluster systems. At a sufficiently low temperature the inherent free-energy barriers are larger than the equilibrium kinetic energy, thus trapping the system into glassy free-energy local minima from which it can take a large amount of time to escape through kinetic processes. In the $T\rightarrow0$ limit, the problem reverts to that of identifying the global minimum of the PES. Fortunately,

⁽ᵃ⁾Electronic mail: voth@chem.utah.edu

0021-9606/2006/124(2)/024327/9/$23.00
124, 024327-1
© 2006 American Institute of Physics

much progress has been made in recent years on global op- timization methods of the PES, and there are now a large number of possible alternatives to choose from. Even so, of more general interest than the global minimum is the larger problem of obtaining temperature-dependent properties across the entire range from the $T \to 0$ limit to the liquid cluster phase.

This present paper describes and applies an algorithm which combines a global optimization algorithm (basin- hopping Monte Carlo) with an algorithm for the evaluation of equilibrium properties for low temperature and high bar- rier systems (parallel tempering). The resulting hybrid will be referred to as parallel basin-hopping and tempering (PB- HaT) algorithm. This algorithm is a hybrid, in that it com- bines the strengths of both basin hopping and parallel tem- pering to yield a procedure that should ultimately give better statistics for low-temperature properties than either one alone. While Kuo and Klein $^{15}$ have also used basin-hopping Monte Carlo (MC) and parallel tempering together, the method described herein uses a different algorithm to gener- ate and seed the parallel-tempering replicas, yielding a more thorough and representative sampling of the PES.

Parallel tempering has been used with success in manystudies of small water clusters. For example, Nigra et al. $^{16}$  have used this method in combination with the multihisto- gram approach of Ferrenberg and Swendsen $^{17}$ to characterize solid-solid and solid-liquid phase changes for the water oc- tamer. Wang and Jordan performed parallel tempering for the hydrated electron cluster $(H_{2} O)_{6}^{-}$ to characterize temperature dependent dominant clusters. $^{18}$ Tharrington and Jordan used a similar approach to study the neutral cluster in the region $n=6-9$ waters. $^{19}$ Parallel tempering has also proved useful in the study of thermodynamics of Lennard-Jones clusters. Neirotti et al. have employed this method to characterize the phase change in the difficult Lennard-Jones 38-atom cluster. $^{20}$ Sabo et al. have performed both classical and path integral parallel-tempering calculations in a study of binaryLennard-Jones clusters. $^{21}$

The remaining sections of this paper are organized as follows: In Sec. II the basin-hopping and parallel-tempering algorithms will be reviewed, and the PBHaT method will be outlined. Section III details the parametrization of the ion- water models used for the resulting simulations. Simulation details are given in Sec. IV, results in Sec. V, and a summary and conclusions in Sec. VI.

## II. THE PBHaT ALGORITHM
### A. Parallel basin hopping
The implementation of PBHaT is a multistage process. The procedure in the first stage is to collect a representative sample of local minima of the PES, which ideally should include the global minimum of the system. These are ob- tained from the basin-hopping algorithm of Wales and Doye, $^{22}$ in which Monte Carlo steps are taken on the trans formed "staircase surface" of the PES $V(x)$ , given by

$$W(X)=\min [V(X)].\qquad(1)$$

The function $W(X)$ is the transformed surface obtained by performing a gradient optimization at $x$ on $V(x)$ , to the local minimum of $V(x)$ which occurs at the point $x=X$ , i.e., W(X)=V(X). In more recent implementations of this algo- rithm, $x$ is usually reset to $X$ after the gradient optimization is performed, so that $W(x)$ only exists at the discrete points where $x=X$ (i.e., at the minima).

In basin hopping the strategy is to then locate the global minimum of $V(x)$ by performing Metropolis MC steps on W(X). In practice, this requires taking a displacement from one minimum, $x=X_{1}$ on $V(x)$ , and then performing a gradient optimization from this new structure to reach the coordinate $x=X_{2}$ (which may or may not be different from $X_{1}$ ). The new coordinate is then accepted with probability

$$p=\min \left[1, \exp \left(-\beta\left[V\left(X_{2}\right)-V\left(X_{1}\right)\right]\right)\right].\qquad(2)$$

An attractive feature of the basin-hopping algorithm is that only one parameter is required-the inverse temperatureβ. This can be found through a trial and error process but is normally close to the melting temperature of the system. However, a poor choice for $\beta$ can lead to very inefficient sampling.

As a second stage, one can further improve the basin- hopping algorithm by using algorithms with improved sam- pling properties, so that $W(X)$ is explored more ergodically than by straight Metropolis MC alone. One way (which has recently been explored by Oppenheimer and Curotto in a study of Lennard-Jones dipole-dipole clusters $^{23}$ ) is to use the parallel-tempering method in which $N_{rep }$ trajectories are cal culated in parallel, each with a different inverse temperature $\beta_{p}$ , where $p$ takes values in the range of $1-N_{rep }$ . This method involves temperature swap MC steps in which a swap is attempted between two replicas with temperatures $\beta_{p}$ andβp+1 with a probability

$$p=\min \left[1, \exp \left(-\left[\beta_{1}-\beta_{2}\right]\left[V\left(X_{2}\right)-V\left(X_{1}\right)\right]\right)\right].\qquad(3)$$

The inclusion of parallel-tempering trajectories improves the search for low-lying minima in two ways: (1) a trajectory can heat up and effectively lower free-energy barriers and (2) the use of multiple trajectories improves the diversity of sampling of the PES and ensures that not all of the efforts are concentrated into any one region of the PES. An example of parallel basin-hopping trajectories is shown in Fig. 1.

At this stage, trial moves on $W(X)$ do not need to be limited to the usual translational and rotational displacements found in standard MC algorithms. One can also make use of the so-called wormhole moves in which one attempts a very large discrete jump from one part of the PES to another that would otherwise involve a large number of standard trial moves. One example of a wormhole used in the simulations described here is to swap a solvent and a random solute molecule so that the $Na^{+}$ cation can very quickly explore the possible sites available to it. These moves would be very inefficient on $V(x)$ , but they have a much higher acceptance rate on $W(X)$ , in which the structure is relaxed around the new solute position. The other type of wormhole move found useful in this study was to attempt to rearrange the hydrogen

![](./images/812121225152167938_3.jpg)

FIG. 1. (Color online) Typical parallel basin-hopping trajectories (energy against Monte Carlo step number).

configuration of the waters by “shuffling” the protons between oxygens for a given arrangement of oxygen sites in the system. This changes the H-bonding directionality and can lead to large concerted changes in the system in a single step. Similar ideas have been developed for MC steps on the untransformed $V(x)$ surface. For instance, the so-called swap Monte-Carlo algorithm of Grigera and Parisi in which different types of molecules are exchanged has been used in studies of glassy systems. $^{24}$

“Standard” translational Metropolis MC moves were found to be extremely inefficient on the transformed surface for our systems. Except on the cluster surface, there is generally not enough space to translate a molecule into a low-energy basin without colliding with another molecule. Conversely, molecular rotational moves were found to be an extremely useful method for the location of new minima. This type of move is particularly good at breaking and re-forming H bonds in an efficient way. In general, the type of move considered is system dependent, so that a move which works well for Lennard-Jones clusters might be extremely inefficient for water clusters.

The PBHaT algorithm must be run long enough for equilibration to be reached on the $W(X)$ surface, which is sampled according to the distribution
$$
Q^{0}(\beta)=\sum_{n} \exp \left(-\beta\left[W\left(X_{n}\right)-T S_{n}^{0}\right]\right),\qquad(4)
$$
where $S_{n}^{0}$ is given by
$$
S_{n}^{0}=k_{B} \ln \left(A_{n}\right),\qquad(5)
$$
where $A_{n}$ is the hyperarea associated with the basin of the $n$th minimum and the index $n$ runs over all minima.

### B. The superposition approximation

The ultimate aim is to evaluate properties for clusters under the canonical distribution. One could take $Q^{0}$ from Eq. (4) as an initial approximation to the canonical partition function, but in most cases this is not a very accurate starting point. This is because the $A_{n}$ factors can be quite different to the actual contribution to the partition function from the catchment basin of the $n$th minimum (see the discussion by Doye and Wales $^{25,26}$ ). The difference between these two factors is advantageous in locating hard to find low-lying minima (including the global minimum), and though $Q^{0}$ is not a good approximation to the true partition function, it is useful for obtaining good sampling of minima.

Instead, a more sophisticated distribution, previously used by Doye, $^{27}$ is implemented here which takes into account the harmonic part of the PES (Ref. 28) about each local minimum and has been shown to give a reasonable approximation to cluster partition functions. The harmonic superposition partition function is given as
$$
Q^{H}(\beta)=\sum_{n} \exp \left(-\beta\left[W\left(X_{n}\right)-T S_{n}^{H}\right]\right),\qquad(6)
$$
where $S_{n}^{H}$ is given by
$$
S_{n}^{H}=-k_{B} \sum_{m} \ln \left(\nu_{n}^{m}\right),\qquad(7)
$$
and is the entropic contribution from the normal modes. The sum is over all $N_{\text{dof}}$ normal modes of the isomer and $\nu_{n}^{m}$ is the frequency of the $m$th normal mode. The probability at a given temperature of finding the system in the catchment basin of the $n$th isomer is thus given by
$$
P_{n}=\left(1 / Q^{H}\right) \exp \left(-\beta\left[W\left(X_{n}\right)-T S_{n}^{H}\right]\right).\qquad(8)
$$

At each discretized temperature, a representative “seed” structure is then selected for use in the next stage of PBHaT. The structures are randomly picked from the “database” of structures collected over all basin-hopping trajectories according to the probability distribution from Eq. (8). This is done in turn for each temperature, $P=1-N_{\text{rep}}$. It is useful to work in normal mode coordinates, with eigenvectors $e_{n,i}^{m}$ ($m$th mode, $n$th replica, and $i$th particle) and associated eigenvalues $(\omega_{n}^{m})^{2}$. In this representation, the position vector can be expressed as $r_{n,i}=\overline{r_{n,i}^{\text{eq}}}+(1/\sqrt{m_{i}})\sum_{m}\lambda_{m}^{n}e_{n,i}^{m}$ in the harmonic superposition approximation. The ensemble average of an observable $A$ is then given by
$$
\langle A\rangle=Q^{-1} \sum_{n} \int \mathcal{D} \lambda^{n} \mathcal{D} \dot{\lambda}^{n} A \exp \left[-\beta \mathcal{H}_{n}\right],\qquad(9)
$$
where
$$
Q=Q^{H}\left(\frac{2 \pi}{\beta}\right)^{N_{\mathrm{dof}}} \frac{1}{\prod_{m} \omega_{m}}\qquad(10)
$$
and
$$
\mathcal{H}_{n}=W\left(X_{n}\right)+\frac{1}{2} \sum_{m}\left[\left(\lambda_{m}^{n} \omega_{n}^{m}\right)^{2}+\left(\dot{\lambda}_{m}^{n}\right)^{2}\right]-T S_{n}^{H}.\qquad(11)
$$

The next section presents results showing the radial distribution of molecules with respect to the center of mass of the cluster. If the distribution function $\rho(r,\beta)$ is defined such that the equilibrium average number of molecules in the distance interval from $r$ to $r+dr$ is given by $\rho(r,\beta)dr$, then the above results can be used to show that the distribution function is given by

$$
\begin{aligned}
\rho(r, \beta) & \\
& =Q^{-1} \sum_{n} \exp \left[-\beta\left(W\left(X_{n}\right)+\frac{1}{2} \sum_{i} \kappa_{n, i}\left(r-r_{n, i}^{\mathrm{eq}}\right)^{2}-T S_{n}^{H}\right)\right], \\
&
\end{aligned}
$$

where the effective force constant $\kappa_{n, i}$ (which comes from projecting the thermal ellipses onto the radial direction) is given by
$$
\kappa_{n, i}=\left(\sum_{m} \frac{\left(e_{n, i}^{m} \cdot \dot{r}_{n, i}^{\mathrm{eq}}\right)^{2}}{m_{i}\left(\omega^{m}\right)^{2}}\right)^{-1}.
$$

## C. Parallel-tempering molecular dynamics and multihistogram methods

The third stage of PBHaT is also the final stage, in which parallel-tempering molecular dynamics (PT-MD) is run from the $N_{\text {rep }}$ seed randomly selected according to the probability distribution of Eq. (8). Note that there is no constraint that the same number of replicas need to be used in both the parallel basin-hopping and parallel-tempering stages of the algorithm.

Molecular dynamics (MD) is chosen as opposed to MC in the second stage because of its normally superior sampling properties on the continuous PES $V(x)$. At this stage each replica is attached to a Nosé-Hoover thermostat, $^{29-31}$ which gives the canonical distribution at that replica's temperature. Then, after a fixed number of parallel time steps, the parallel-tempering MC swap move is attempted with the probability in Eq. (3). If the move is successful, then the target temperature in the Nosé-Hoover algorithm is switched between the replicas. Note that parallel tempering is ideally suited for parallelization strategies across many processors as only the temperatures and energies need to be communicated. There is no need to communicate the structural coordinates from one processor to another.

The number of replicas used in PT-MD is chosen to give a reasonable acceptance probability in the attempted temperature swap moves. In turn, this requires that there should be sizable overlap in the energy histogram distributions between neighboring replica temperatures. It can be shown that optimal sampling is generally found for geometrically spaced inverse temperatures: $\beta_{n+1} / \beta_{n}=\beta_{n+2} / \beta_{n+1}$. Also note that since the energy fluctuations scale as $1 / \sqrt{N_{\text {atoms }}}$, the number of required replicas is expected to scale as $\sqrt{N_{\text {atoms }}}$.

At this stage the heat capacity can also be obtained from the fluctuation in potential energy. In the canonical distribution, the (dimensionless) heat capacity per degree of freedom is given as
$$
C=\frac{\beta^{2}}{N_{\text {dof }}}\left(\left\langle U^{2}\right\rangle-\langle U\rangle^{2}\right)+\frac{1}{2}.
$$

In the harmonic superposition approximation, the heat capacity is given as
$$
C^{H}=\frac{\beta^{2}}{N_{\text {dof }}}\left(\left\langle W^{2}\right\rangle-\langle W\rangle^{2}\right)+1.
$$

Another method for heat-capacity estimation is to calculate $\langle U\rangle$ as an average over the energy density of states $\rho(U)$. Using the multihistogram method of Ferrenberg and Swendsen $^{17}$ the estimated density of states calculated at each inverse temperature in the parallel-tempering trajectories is combined through a weighted sum into a density of states that is more accurate across the entire temperature range. The resulting caloric curves using this method should be more accurate than the fluctuation-derived results.

The multihistogram method can also be applied to the calculation of structural properties. A radial distribution function is first binned, $g(r, U)$, for distance $r$ and potential energy $U$ across both distance and energy intervals, where the data comes from all inverse temperatures in the PT-MD simulation. If $p(\beta, U) d U$ represents the probability of obtaining a potential energy between $U$ and $U+d U$ at inverse temperature $\beta$, then the canonical radial distribution function is obtained through the probability transform,
$$
g(r, \beta)=\int d U g(r, U) p(U, \beta).
$$

In the canonical distribution, the energy distribution function can be written in two alternative ways; first,
$$
p(U, \beta)=\frac{1}{Q} \exp \left(-\frac{\beta(U-\langle U\rangle)^{2}}{2(T \partial\langle U\rangle / \partial T)}\right)=\frac{1}{Q} \exp (-\beta U) p(U).
$$

This choice comes from assuming that the energies are Gaussian distributed about their mean and from using Eq. (14) for the Gaussian width. The second choice leads to the transform
$$
g(r, \beta)=\frac{1}{Q} \int d U \rho(r, U) \exp (-\beta U) \rho(U),
$$

where the multihistogram value of $\rho(U)$ is used. Thus, the familiar integral over the partition function can also be interpreted as a transform from the constant-potential distribution to the constant-temperature (canonical) distribution. Through taking logarithms, the above method for histogram reweighting of distribution functions can also be applied to the calculation of free-energy curves as a function of temperature and coordinate. This technique can be viewed as a special case of the method of Kumar and co-workers $^{32,33}$ (see also the discussion by Fasnacht et al. ${ }^{34}$ ).

Normally the multihistogram approach is to be preferred, but in the following calculations significant problems occurred when trying to iteratively converge the multihistogram density of states for a cluster of 100 molecules. In this case, the distribution functions were calculated using a smooth function $U=U(\beta)$ fitted across the calculated values $U_{p}$, which is then used to calculate the energy distribution function using the first expression on the right-hand side of Eq. (18).

## III. THE MODEL

The $\mathrm{H}^{+}\left(\mathrm{H}_{2} \mathrm{O}\right)_{100}$ cluster was modeled using the MS-EVB2 potential $^{12}$ while all other clusters were modeled using

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    O
   </th>
   <th>
    Na⁺
   </th>
   <th>
    Cl⁻
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $A_{16}^{O}$
   </th>
   <td>
    0
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{14}^{O}$
   </th>
   <td>
    4 957 010
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{12}^{O}$
   </th>
   <td>
    $-$3 209 430
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{10}^{O}$
   </th>
   <td>
    557 213
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{8}^{O}$
   </th>
   <td>
    0
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{6}^{O}$
   </th>
   <td>
    $-$2 681.08
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{16}^{Na^{+}}$
   </th>
   <td>
    0
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{14}^{Na^{+}}$
   </th>
   <td>
    80 204.5
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{12}^{Na^{+}}$
   </th>
   <td>
    $-$67 811.4
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{10}^{Na^{+}}$
   </th>
   <td>
    $-$6 545.84
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{8}^{Na^{+}}$
   </th>
   <td>
    17 372.7
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{6}^{Na^{+}}$
   </th>
   <td>
    $-$1 890.36
   </td>
   <td>
    0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    $A_{16}^{Cl^{-}}$
   </th>
   <td>
    144 235 000
   </td>
   <td>
    2 405 470
   </td>
   <td>
    $-$369 219 000
   </td>
  </tr>
  <tr>
   <th>
    $A_{14}^{Cl^{-}}$
   </th>
   <td>
    $-$113 874 000
   </td>
   <td>
    $-$5 114 960
   </td>
   <td>
    257 215 000
   </td>
  </tr>
  <tr>
   <th>
    $A_{12}^{Cl^{-}}$
   </th>
   <td>
    33 316 700
   </td>
   <td>
    4 283 360
   </td>
   <td>
    $-$71 382 700
   </td>
  </tr>
  <tr>
   <th>
    $A_{10}^{Cl^{-}}$
   </th>
   <td>
    $-$4 862 050
   </td>
   <td>
    $-$1 762 060
   </td>
   <td>
    9 059 780
   </td>
  </tr>
  <tr>
   <th>
    $A_{8}^{Cl^{-}}$
   </th>
   <td>
    433 851
   </td>
   <td>
    346 900
   </td>
   <td>
    $-$368 978
   </td>
  </tr>
  <tr>
   <th>
    $A_{6}^{Cl^{-}}$
   </th>
   <td>
    $-$15 413.4
   </td>
   <td>
    $-$20 015.6
   </td>
   <td>
    $-$6 030.7
   </td>
  </tr>
 </tbody>
</table>

Table I. Polynomial coefficients $A_{M}^{X,Y}$ for the model. The units are in Å$^{M}$ kcal/mol. As and example, the $A^{Na^{+},Cl^{-}}$ coefficients governing the Na⁺–Cl⁻ interaction are found in the third row, second column of numbers so that $A_{12}^{Na^{+},Cl^{-}}$=4 283 360 Å$^{12}$ kcal/mol. Because of the low polarizability of the Na⁺ cation, an adequate sodium-sodium interaction can be described using electrostatics alone and the $A^{Na^{+},Na^{+}}$ coefficients are zero. The Na⁺–Na⁺ and Cl⁻–Cl⁻ interactions are not used in this work but are included for completeness.

the polarizable flexible TTM2-F water model, which has been described in detail elsewhere.35–39 Considering the relatively large polarizability of the chloride anion, it seems necessary to use a polarizable model for those clusters.

The TTM2-F model uses the modified “smeared” dipole tensor interaction of Thole40 in which the electrostatics is calculated according to smeared-charge smeared-dipole interactions. The damping widths for the charge-charge, charge-dipole, and dipole-dipole interactions were unchanged from Ref. 39. The Na⁺ cation was assigned a polarizability of 0.13 Å³ and a charge of +1. The Cl⁻ anion was assigned a polarizability of 3.37 Å and a charge of $-$1. In addition to electrostatic interactions, the atomic sites interact under a pairwise polynomial in $r$ of the form

$$
U_{ij} = \sum_{k=3}^{8} \frac{A_{2k}^{X,Y}}{r_{ij}^{X,Y2k}}, \tag{19}
$$

where $r_{ij}^{X,Y}$ is the separation between the $X$ and $Y$ species (e.g., $r^{Na^{+},O}$ is the distance between a sodium cation and a water oxygen site). The coefficients were parametrized to reproduce electronic structure calculations and are given in Table I. Electronic structure points were calculated with the GAUSSIAN 98 software package⁴¹ using the (Møller-Plesset) MP2 level of perturbation with a 6-31++G∗∗ basis set on the Na⁺ and the Dunning correlation consistent aug-cc-pVDZ basis set41,42 on the Cl⁻.

## IV. SIMULATION DETAILS

Four different clusters were studied: (1) Na⁺(H₂O)₂₀, (2) Cl⁻(H₂O)₁₇, (3) Na⁺(H₂O)₁₀₀, and (4) H⁺(H₂O)₁₀₀. All parallel basin-hopping runs were performed using 16 replicas in the temperature range 100–450 K. For all but the larger 100 molecule cluster, the basin-hopping simulations were run long enough such that the putative global minimum structures were visited by at least three different replicas. It was not computationally feasible to locate the global minima for the 100 molecule cluster, and basin-hopping was run on these clusters long enough only to approximately converge the ion separation from the center of mass of the cluster. It should be noted that while James and Wales¹¹ found it necessary to modify the MS-EVB2 state search algorithm to avoid what they have termed “cold fusion” of the oxygen atoms, no such modification was used or was found to be necessary in the present work.

The PT-MD trajectories were performed using 32 replicas (for all clusters), also in the temperature range 100–450 K. Temperature swaps were attempted every 1000 time steps, with the time step set to 0.2 fs. In order to prevent evaporation from the cluster, each was enclosed with a $1/r^{12}$ repulsive sphere chosen to be several angstroms larger than the nominal cluster size. In effect, the constraining sphere encloses each cluster at the saturated vapor pressure for all temperatures considered.

## V. RESULTS

### A. Cluster structures

The global minima of several clusters are shown in Fig. 2. For example, the global minimum for the Na⁺(H₂O)₂₀ structure is seen in Fig. 2(a). Perhaps this structure is best described as a solvated Na⁺H₂O because there is also a fully solvated water in the interior of the cluster. Hartke et al.⁴³ have used genetic algorithm global optimization methods to search for global minima of Na⁺(H₂O)ₙ clusters in the range $n$=4–20 using the pairwise-additive (TIP4P/OPLS) models.⁴⁴ The global minima were shown to have unusual solvation properties. Up to $n$=17 the global minima were found to place the sodium cation at a roughly central site, but a transition occurs at the $n$=18 cluster for which it was found that the Na⁺ moved to an off-center site, with a water instead being located inside the solvation shell. The off-center displacement of the Na⁺ appears to continue up to the largest cluster examined ($n$=25). In particular, it was found that at $n$=20 the dodecahedral global minimum with a central Na⁺ was not favored by the potential. The transition seems to be a result of competition between the system trying to minimize all water-cation separations (dominant for $n$$&lt;$17) and the waters trying to reorient to more favorable first shell Na⁺–H₂O orientations at the expense of reducing the occupancy of waters in the second shell. Schulz and Hartke⁴⁵ have also recently investigated the predicted IR spectra from the TIP4P/OPLS global minima.

Figure 3 shows the temperature-dependent radial distributions [distance to center-of-mass (COM)] for Na⁺(H₂O)₂₀ calculated both by the harmonic superposition approximation

![](./images/812121225152167938_4.jpg)
![](./images/812121225152167938_5.jpg)

![](./images/812121225152167938_6.jpg)
![](./images/812121225152167938_7.jpg)

![](./images/812121225152167938_8.jpg)
![](./images/812121225152167938_9.jpg)

FIG. 2. (Color online) Structures for the putative global minimum: (a) Na⁺(H₂O)₂₀, (b) Cl⁻(H₂O)₁₇, and (c) Na⁺(H₂O)₁₀₀.

and by PT-MD. (Similar plots have been presented for the 38-atom Lennard-Jones cluster by Neirotti et al.²⁰) The Na⁺ cation remains in its off-center position to around 250 K at which point the cluster melts and the Na⁺ distribution spreads out around the center. It is immediately apparent that

![](./images/812121225152167938_10.jpg)

FIG. 3. (Color online) Na⁺(H₂O)₂₀ cluster distribution function. (a) Harmonic $g(R_{\text{com}},T)$ from the superposition approximation. (b) PBHaT calculation of $g(R_{\text{com}},T)$. Darker colors show water density while lighter colors show Na⁺ density.

although the superposition approximation broadly gives the correct distribution, it fails to give the melting behavior observed in the PT-MD results at $\sim$250 K.

A comparison of the heat capacities using (1) the fluctuation formula, (2) harmonic superposition, and (3) Ferrenberg-Swendsen reweighting is shown in Fig. 4. It is clear that the harmonic result grossly underestimates the latent heat associated with melting the cluster. Unfortunately there is about a 20% discrepancy between the histogram and fluctuation results, and the fluctuation-derived heat capacity somewhat underestimates the low-temperature limit of $C$ =1/2. One likely reason for this could be that the coupling between the thermostat and nuclear degrees of freedom is too weak on the time scale between temperature exchanges. As discussed by Holian et al.,²⁹ this can give rise to noncanonical temperature fluctuations. It may be necessary in the future to explore the use of separate thermostats for the O and H species which have well-separated time scales of motion.

The global minimum for Cl⁻(H₂O)₁₇ shown in Fig. 2(b) is a box-shaped structure with the chloride ion adopting a threefold-coordinated position midway along one of the box vertices. The chloride ion exhibits interesting temperature-dependent properties, which can be observed from the

![](./images/812121225152167938_11.jpg)

FIG. 4. (Color online) Caloric curve, excluding the kinetic degrees of freedom, for ${\rm Na^+(H_2O)_{20}}$ calculated by fluctuation formula of Eq. (14) (solid circles), using the harmonic-superposition-derived partition function (red curve) and from Swendsen-Ferrenberg, multihistogramming (green curve).

temperature-dependent radial distribution function in Fig. 5. At low temperatures box-shaped clusters are favored in which the ion adopts one of the surface lattice sites. Past the melting point, however, the chloride becomes preferentially solvated into the interior of the cluster. The switch from ex-

![](./images/812121225152167938_12.jpg)

FIG. 5. (Color online) ${\rm Cl^-(H_2O)_{17}}$ cluster distribution function. (a) Harmonic $g(R_{\rm com},T)$ from superposition approximation. (b) PBHaT calculation of $g(R_{\rm com},T)$. Darker colors show water density while lighter colors show ${\rm Cl^-}$ density.

terior to interior can be rationalized by observing that ice is a much poorer solvent than the liquid, and so it is perhaps not unexpected that melting should have such dramatic changes on some ion distribution functions. We note that in this case a global optimization study in and of itself would not be able to predict the solvation properties of the chloride ion in the liquid. Even the harmonic superposition approximation can- not reproduce the favorable interior solvation of the ion at high temperatures.

At the low-temperature end of the distribution, two peaks in the ${\rm Cl^-}$ distribution are evident. The strongest peak is at $3.5\ \mathring{A}$ and corresponds to the aforementioned edge-centered lattice site on the box water structure. The much weaker peak at $2.5\ \mathring{A}$ can be traced to the ion adopting a combination of corner and face-centered positions in the (nearly equivalent) $1×3×3$ box structure.

The ${\rm Na^+(H_2O)_{100}}$ cluster is shown in Fig. 2(c) and the radial distribution function is shown in Fig. 6. As mentioned before, for this system it was not feasible to perform an exhaustive global optimization search. However, we were able to perform $\sim 30\,000$ basin-hopping steps in which the low-energy structures were all found to result in the ${\rm Na^+}$ cation adopting near-surface site positions on the roughly spherical water cluster below 250 K. It would be misleading

![](./images/812121225152167938_13.jpg)

FIG. 6. (Color online) ${\rm Na^+(H_2O)_{100}}$ cluster distribution function. (a) Harmonic $g(R_{\rm com},T)$ from superposition approximation. (b) PBHaT calculation of $g(R_{\rm com},T)$. Darker colors show water density while lighter colors show ${\rm Na^+}$ density.

![](./images/812121225152167938_14.jpg)

FIG. 7. (Color online) H⁺(H₂O)₁₀₀ cluster distribution function. (a) Harmonic $g(R_{\text{com}},T)$ from superposition approximation. (b) PBHaT calculation of $g(R_{\text{com}},T)$. Darker colors show water density while lighter colors show H⁺ density.

to label these as “pure” surface sites; a more accurate description is that the cation tends to be either recessed into the surface at around the 1 monolayer depth [cf. Fig. 2(c)]. Also, it is worth pointing out that the 2 Å gap between the low-temperature ion position and the remote tail of the water distribution that is evident in the temperature-dependent structural distributions is mostly due to both the oblateness of the water cluster and the Na⁺ molecular-scale roughness of the surface.

The conclusion that the Na⁺ ion adopts surface sites at low temperatures in the 100 molecule cluster may be something of a surprise given that we observed that the interior was favored for the 20 water cluster. It should, however, be noted that the 20 molecule cluster is at most only 2 monolayer thick, so at this size the water clusters are nearly all surface. At ~250 K the 100 water molecule Na⁺ cluster melts and the sodium becomes largely solvated into the interior of the cluster, no longer showing any preference for adopting surface sites. A similar surface to interior transition was observed for the Cl⁻(H₂O)₁₇ system and presumably a similar cause is responsible.

The H⁺(H₂O)₁₀₀ cluster distribution function is shown in Fig. 7. This singly protonated cluster, like the sodium analog, displays significant surface residence below the melting point of the cluster. However, unlike the sodium analog, for temperatures sampled above the cluster melting point the hydrated proton continues to reside primarily at the surface. While this surface solvation is perhaps counterintuitive with respect to the corresponding sodium clusters bias for interior solvation sites, this phenomenon has also been seen in previous studies of water liquid/vapor interfaces⁴⁶ and smaller protonated water clusters.¹⁴ This preference for surface solvation sites of the excess proton can be attributed to the anisotropic solvation of the hydronium cation, resulting in amphiphile like solvation. On average the center of positive charge in the cation resides on the hydronium oxygen, reducing the overall coordination from the approximately four hydrogen bonds of water to three strongly solvating water molecules hydrogen bonded to the hydronium hydrogen atoms. Additionally, these solvating waters themselves have been shown⁴⁷ to display a reduced coordination relative to bulk water, contributing to the depleted water density which results in the observed anisotropic solvation.

## VI. SUMMARY AND CONCLUSIONS

This work has reported the development and use of a hybrid algorithm, specifically (PBHaT), designed for efficient sampling of the partition function from the global minimum (0 K) to the liquid state. The PBHaT algorithm is a promising hybrid between the successful basin-hopping global optimization and parallel-tempering methods. It is to be preferred over basin hopping alone in cases where there is interest in more than just the global minimum. Also, it is to be preferred over parallel tempering alone for difficult low-temperature cases in which parallel tempering will have difficulty in locating the global minimum. PBHaT will be useful in general for simulation of molecular clusters and could also be applied to glassy systems.

There are many possible modifications to the underlying algorithm that could be considered. The first stage requires an efficient method to generate low-lying local minima down to the global minimum. This was done by basin-hopping techniques, but most global-optimization methods, such as the genetic-algorithm-based approaches of Hartke,⁴³ would probably be suitable.

In the second stage, the harmonic superposition approximation to the partition function is evaluated in order to seed the parallel-tempering molecular-dynamics trajectories. It is clear from a comparison of the harmonic and final MD distribution functions that the superposition approximation only works well in the solid phase and does not predict the liquid-solid transition with any accuracy. This limitation can, in principle, be overcome by the use of anharmonic corrections, such as those employed with success by Doye and Wales.²⁵,²⁶ However, even without such corrections, the MD equilibration will eventually give all anharmonic effects.

As has been found by other authors, a combination of parallel-tempering and multihistogram methods is a particularly effective way for obtaining good statistics over the entire temperature range of interest. This work has made use of histogram reweighting in the calculation of the caloric curves

and the temperature-dependent structural distributions. In both cases, the histogram method was found to give a dra- matic improvement in statistics.

The most significant difficulty with the algorithm pre- sented here is the generation of good canonical fluctuations using Nosé-Hoover thermostatting that must be produced on the time scale between temperature exchanges in the parallel- tempering molecular dynamics. Though it is true that the Nosé-Hoover thermostat will sample the long-time canonical limit, future work would ideally explore sampling ap- proaches carried out in the shortest possible time.

This study has also reported results using the PBHaT algorithm in a study of the solvation of $Na^{+}$, $Cl^{-}$, and $H^{+}$ ions in water clusters. Below the water-cluster freezing tempera- ture all ions studied were generally excluded from the cluster interior and tend to reside within a few monolayers of the surface (noting that the smaller clusters only include a few monolayers). Above the cluster melting point, both the so- dium and chloride ions are excluded from the surface of the cluster in the liquid region whereas the solvated proton was found to still be biased toward surface sites. It should be noted that the exclusion of the $Cl^{-}$ ion from the cluster sur face was far less dramatic than that for the $Na^{+}$ clusters stud ied. With increasing temperature the $Cl^{-}$ maxima transitions occur gradually from near surface to interior, displaying a significant interior bias only at the highest temperatures considered.

## ACKNOWLEDGMENT
This work was supported by a grant from the National Science Foundation (CHE-0317132).

$^{1}$ B. C. Garrett, Science 303, 1146 (2004).
$^{2}$ L. Perera and M. L. Berkowitz, J. Chem. Phys. 95, 1954 (1991).
$^{3}$ M. A. Carignano, G. Karlström, and P. Linse, J. Phys. Chem. B 101, 1142 (1997).
$^{4}$ S. J. Stuart and B. J. Berne, J. Phys. Chem. 100, 11934 (1996).
$^{5}$ L. X. Dang, J. Chem. Phys. 110, 1526 (1999).
$^{6}$ L. X. Dang and D. E. Smith, J. Chem. Phys. 99, 6950 (1993).
$^{7}$ D. E. Smith and L. X. Dang, J. Chem. Phys. 101, 7873 (1994).
$^{8}$ E. M. Knipping, M. J. Lakin, K. L. Foster, and P. Jungwirth, Science 288, 301 (2000).
$^{9}$ P. Jungwirth and D. Tobias, J. Phys. Chem. B 106, 6361 (2002).
$^{10}$ P. Jungwirth and D. Tobias, J. Phys. Chem. B 105, 10468 (2001).
$^{11}$ T. James and D. J. Wales, J. Chem. Phys. 122, 134306 (2005).

$^{12}$ T. J. F. Day, A. V. Soudackov, M. Čuma, U. W. Schmitt, and G. A. Voth, J. Chem. Phys. 117, 5839 (2002).
$^{13}$ S. S. Iyengar, M. K. Petersen, C. J. Burnham, T. J. F. Day, and G. A. Voth, J. Chem. Phys. 123, 084309 (2005).
$^{14}$ S. S. Iyengar, T. J. F. Day, and G. A. Voth, Int. J. Mass. Spectrom. 241, 197 (2005).
$^{15}$ J. Kuo and M. L. Klein, J. Chem. Phys. 122, 024516 (2005).
$^{16}$ P. Nigra, M. A. Carignano, and S. Kais, J. Chem. Phys. 115, 2621 (2001).
$^{17}$ A. M. Ferrenberg and R. H. Swendsen, Phys. Rev. Lett. 63, 1195 (1989).
$^{18}$ F. Wang and K. D. Jordan, J. Chem. Phys. 119, 11645 (2003).
$^{19}$ A. N. Tharrington and K. D. Jordan, J. Phys. Chem. A 107, 7380 (2003).
$^{20}$ J. P. Neirotti, F. Calvo, D. L. Freeman, and J. D. Doll, J. Chem. Phys. 112, 10340 (2000).
$^{21}$ D. Sabo, C. Predescu, J. D. Doll, and D. Freeman, J. Chem. Phys. 121, 856 (2004).
$^{22}$ D. J. Wales and J. P. K. Doye, J. Phys. Chem. A 101, 5111 (1997).
$^{23}$ C. A. Oppenheimer and E. Curotto, J. Chem. Phys. 121, 6226 (2004).
$^{24}$ T. S. Grigera and G. Parisi, Phys. Rev. E 63, 045102 (2001).
$^{25}$ J. P. K. Doye and D. J. Wales, Phys. Rev. Lett. 80, 1357 (1998).
$^{26}$ J. P. K. Doye and D. J. Wales, J. Chem. Phys. 102, 9659 (1995).
$^{27}$ J. P. K. Doye, Ph. D. thesis, University of Cambridge, 1996.
$^{28}$ W. Frost, Theory of Unimolecular Reaction (Acedemic, New York, 1973).
$^{29}$ B. L. Holian, A. F. Voter, and R. Ravelo, Phys. Rev. E 52, 2338 (1995).
$^{30}$ S. Nosé, J. Chem. Phys. 81, 511 (1984).
$^{31}$ S. Nosé, Mol. Phys. 52, 255 (1984).
$^{32}$ S. Kumar, D. Bouzida, R. H. Swendsen, P. A. Kollman, and J. M. Rosen- berg, J. Comput. Chem. 13, 1011 (1992).
$^{33}$ S. Kumar, J. Rosenberg, D. Bouzida, R. Swendsen, and P. Kollman, J. Comput. Chem. 16, 1339 (1995).
$^{34}$ M. Fasnacht, R. H. Swendsen, and J. M. Rosenberg, Phys. Rev. E 69, 056704 (2004).
$^{35}$ C. J. Burnham, J. Li, S. S. Xantheas, and M. Leslie, J. Chem. Phys. 110, 4566 (1999).
$^{36}$ C. J. Burnham and S. S. Xantheas, J. Chem. Phys. 116, 1479 (2002).
$^{37}$ C. J. Burnham and S. S. Xantheas, J. Chem. Phys. 116, 1500 (2002).
$^{38}$ C. J. Burnham and S. S. Xantheas, J. Chem. Phys. 116, 5115 (2002).
$^{39}$ S. S. Xantheas, C. J. Burnham, and R. J. Harrison, J. Chem. Phys. 116, 1493 (2002).
$^{40}$ B. T. Thole, J. Chem. Phys. 59, 341 (1981).
$^{41}$ M. A. Frisch, G. W. Trucks, H. B. Schlegel et al., GAUSSIAN 98, revision A.1, Gaussian Inc., Pittsburgh, PA, 1998.
$^{42}$ T. H. Dunning, Jr., J. Chem. Phys. 90, 1007 (1989).
$^{43}$ B. Hartke, A. Charvet, M. Reich, and B. Abel, J. Chem. Phys. 116, 3588 (2002).
$^{44}$ W. L. Jorgensen, J. Chem. Phys. 77, 4156 (1982).
$^{45}$ F. Shultz and B. Hartke, Phys. Chem. Chem. Phys. 5, 5021 (2003).
$^{46}$ M. K. Petersen, S. S. Iyengar, T. J. F. Day, and G. A. Voth, J. Phys. Chem. B 108, 14804 (2004).
$^{47}$ H. Lapid, N. Agmon, M. K. Petersen, and G. A. Voth, J. Chem. Phys. 122, 014506 (2004).