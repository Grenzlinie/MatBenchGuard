# Formation of Ferroelectric Domains Observed in Simulation of Droplets of Dipolar Particles

Gunnar Karlström*

Department of Theoretical Chemistry, University of Lund, P.O.B. 124, SE-221 00 Lund, Sweden

Received: March 19, 2007; In Final Form: June 5, 2007

In this work it is shown that domains of ordered dipoles are formed in large droplets made from dipolar particles provided that the dipole−dipole interaction between nearest neighbors is larger than the thermal energy. The size of the domains grows almost linearly with the size of the droplets for droplets containing 1000−30 000 particles. The largest domains occupy around 25−35% of the droplet volume. The total dipole moment of a domain is of the order of 3−10% of the maximum dipole moment possible if all dipoles in the domain were parallel. The finding offers an explanation to the observation that different boundary conditions yield different long-range order for dipolar liquids and challenges the present view of a short-range dipolar order in polar solvents.

## 1. Introduction

The description of polar liquids is a long-standing issue in science. The origin of the problem is the, in principle, infinite range dipole−dipole interaction. A first step toward an understanding of the connection between the macroscopic dielectric behavior and the dipolar correlations was taken independently by Clausius¹ and Mossotti² with their well-known equation relating the molecular polarizability divided by the molecular volume to the dielectric permittivity.

$$
\frac{(\epsilon - 1)}{(\epsilon + 2)} = 4\frac{\pi}{3}N\alpha \tag{1}
$$

In this equation $\epsilon$ is the relative dielectric permittivity, $\alpha$ is the molecular polarizability, and $N$ is the number density (the number of particles per unit volume).

Later Langevin³ showed that for particles with small dipole moment (strictly speaking if $\mu^2/(4\pi\epsilon_0kTr^3) < 1$), where $\mu$ is the particle dipole moment, $k$ is Boltzmann's constant, $T$ is the absolute temperature, and $r$ is the interparticle distance, then the effect of a dipole could be reproduced by an effective polarizability and $\alpha$ in eq 1 replaced by an effective $\alpha_{\text{eff}} = \alpha_{\text{el}} + \mu^2/(3kT)$, where the last term is the equivalent polarizability of a dipole. Onsager⁴ showed that molecular dipole moments could be calculated from the frequency dependence of the dielectric permittivity of a medium.

The theory which our understanding of dipolar liquids is based on today has been outlined by Nienhuis and Deutch⁵⁻⁷ for nonpolarizable liquids and later generalized to polarizable dipolar liquids by Wertheim.⁸⁻¹¹ The basic assumption is that there is a short-range dipolar order around a dipole determined by the dipole−dipole interaction and a long-range correlation determined by the shape of the container of the liquid. The general belief, that will be questioned in this work, is that the short-range correlations extend at most a few molecular diameters, or around 1−1.5 nm for molecules with the size and dipole moment of a water molecule.

It is extremely difficult to study this phenomenon with experimental methods, and most of our knowledge about this type of system stems from computer simulations, but a few very recent publications by Shelton¹²⁻¹⁴ suggest the formation of ferroelectric domains, possibly with a radius of around 3 nm in polar liquids. The theoretical studies suffer from the severe problem that the range of the dipole−dipole potential is in principle infinite, whereas we can only treat finite nonperiodic or infinite periodic systems with computational modeling. Today there is a general consensus in the scientific community that the proper way to treat the problem is to study an infinite periodic system instead of a finite nonperiodic one. The advantage with the periodic approach is that one is treating a real infinite system and is handling all electrostatic interactions correct. The obvious drawback is that the periodicity in an effective way truncates the dipole−dipole interaction. Formally this term decays as $1/r^3$, and when it is integrated over all space it results in a logarithmic divergence. In real systems this does not occur since all dipoles are not oriented according to the field of one particular dipole but to the total field from all dipoles. However, in a periodic system one can use the technique designed by Ladd¹⁵,¹⁶ for the treatment of infinite periodic systems to show that for distances larger than the periodicity, the effective dipole−dipole interaction decays as a dipole−octopole interaction, that is as $1/r^5$. When such an interaction is integrated over space one obtains a $1/r^2$ behavior. From this it is clear that the long-range correlations in the studied systems could be influenced by the boundary conditions.

Fundamental problems of this type have obviously been extensively studied before. The starting point in most of these studies is to study an in principle infinite system by imposing periodic boundary conditions,¹⁷ implying that the central simulation box is surrounded by a number of replicas. After this there are in principle a few different possibilities to proceed. One possibility is to truncate the space over which the interactions between the dipoles are evaluated. Normally one chooses a sphere (spherical cutoff), but an alternative is to include all particles in the simulation box (cubic cutoff or minimum image model). One may then choose or choose not to include the effect of more distant particles by adding a reaction field from a dielectric medium. Alternatively, one may regard an infinite periodic system and evaluate the system energy partly in real space and partly in the reciprocal space as suggested by Ewald.¹⁸

10.1021/jp072178e CCC: $37.00
© 2007 American Chemical Society
Published on Web 08/17/2007

The system energy can also be evaluated using a multipole expansion scheme as devised by Ladd.¹⁵,¹⁶ The interested reader is referred to one of the standard text books for more information.¹⁷,¹⁹ During the years a large amount of information on how to perform simulations of dipolar liquids has been gathered.²⁰⁻²⁸ The main outcome from these studies was the knowledge/ assumption that the best way to perform this type of study was to use the Ewald summation technique or spherical truncation together with dielectric boundary conditions.²²⁻²⁸ A main reason was probably the superior convergence behavior observed in this type of simulation. Not only did one obtain reasonable values for $\langle\mu^2/v\rangle$, where $v$ is the particle volume, from simulations of fairly small systems, but also the system energy varied very little compared to the large variations observed from simulations using only spherical cutoff. The notation $\langle\ \rangle$ used above and below indicates that a statistic average has been evaluated.

The issue was "finally" settled with a thorough paper by Kusalik²⁹ from the beginning of the 1990s, where he shows that for a system containing 4000 particles and using the Ewald summation technique and a reaction field, one obtains a relatively rapid convergence for the system energy and the dielectric behavior of a highly polar liquid. This is the main argument for the superiority of the Ewald summation technique relative to other techniques. It should be noted that the fact that the results from a series of simulation seem to have converged, when the size of the system is increased, does not mean that simulations have converged to the correct result. It is possible that the properties of a periodic system are different from those of a nonperiodic one and/or that the results will change when even larger systems are studied.

There is an alternative approach to study the long-range solvation behavior of a dipole, which has been used a few times. In that approach one actually studies a real droplet of dipolar particles. Based on ideas of Fröhlich,³⁰ Berendsen³¹ calculated the profile that could be expected for $\langle\mu^2/v\rangle$ as a function of $R$ in a droplet, assuming it to behave as an ideal dielectric with a given dielectric permittivity, and he obtained
$$
\begin{aligned}
\left\langle\frac{(\langle\mu\rangle)^2}{\left(12 \pi \epsilon_{0} k T R^{3}\right)}\right\rangle= \\
\frac{(\epsilon-1)}{(9 \epsilon(\epsilon+2))}\left[(\epsilon+2)(2 \epsilon+1)-2(\epsilon-1)^{2}\left(\frac{R}{R_{\text {drop }}}\right)^{3}\right] \quad(2)
\end{aligned}
$$

In this equation, $R$ is the actual value of the radius inside which $\mu$ is evaluated and $R_{\text{drop}}$ is the radius of the studied droplet. An obvious advantage with this technique is that one is treating a real system and that its behavior will approach the proper macroscopic one with increasing system size. The method has been tested for small systems.³²,³³ Since the studied droplets are small it is difficult to judge if the obtained results are consistent with results obtained by the Ewald summation technique.

The formation of structures in finite cubic volumes containing Stockmayer particles has also been studied by Groh and Dietrich³⁴⁻³⁶ using density functional theory where they have found that the average structure is a vortex. These results as well as the experimental results by Shelton have been questioned by Kumar et al.³⁷

In this study we will present results from simulations of very large droplets. They will shed light on the long-range solvation of dipoles. It is important to keep in mind that the structures found in this work are not average structures but intermittent structures that are changing their location and orientation as the simulations proceed. First we will, however, introduce the Kirkwood $g$-factor³⁸ and discuss its distance dependence.

## 2. The Kirkwood $g$-Factor

The standard way to address the long-range structure in dipolar liquids is to study the so-called Kirkwood $g$-factor ($g_{\text{k}}$). Formally, this quantity is defined for a dipole located in the interior of a bulk liquid. Following the ideas of Kirkwood³⁸ we may write
$$g_{\mathrm{k}}=\lim \left(R_{\text {drop }} / R \rightarrow \infty\right) \lim (R \rightarrow \infty) 1 / \mu^{2}\langle\underline{\mu}_{1} \sum \underline{\mu}_{i}\rangle \quad(3)$$

Here, $R_{\text{drop}}$ is the radius of the considered system and $R$ is the radius of the volume over which the summation of the dipole moments $\underline{\mu}_{i}$ is to be performed. The dipole $\underline{\mu}_{1}$ defines the origin of the sphere where $R$ is the radius. The central idea is that all correlations are to be found within the volume defined by $R$. It is easy to show that there is a relation between the $g$-factor and $\langle\mu^2/v\rangle$,³⁸ saying that $\langle\mu^2/v\rangle = \mu_{\text{p}}^2g_{\text{k}}/v_{\text{p}}$. Here $\mu_{\text{p}}$ and $v_{\text{p}}$ are the particle dipole moment and volume, whereas $m$ and $v$ are the corresponding quantities for the studied volume. Associated with $g_{\text{k}}$ there is a function $G_{\text{k}}(R)$. $G_{\text{k}}(R)$ is the value obtained using eq 3 if the summation is only performed for all particles inside a sphere with radius $R$. Thus $g_{\text{k}}$ is the limiting value taken by $G_{\text{k}}(R)$ for infinite values of $R$. This means that $G_{\text{k}}(R)$ should approach a limiting value for sufficiently large values of $R$ provided that $R_{\text{drop}}$ is much large than $R$. Equation 3 clearly shows that $g_{\text{k}}$ and consequently $G_{\text{k}}(R)$ are quantities that must be calculated using statistical averages. Much of the analysis made below will be based on the calculation of $G_{\text{k}}(R)$ curves calculated for the individual dipoles present in the system.

Before starting to analyze the behavior of $G_{\text{k}}(R)$ it is of value to understand why dipoles that surround a dipole are oriented in such a way that they contribute to the Kirkwood $g$-factor. To start with we will consider a central dipole oriented along the $z$-axis, surrounded by a spherical shell of dipoles where all positions for these surrounding dipoles are equally probable.

If we initially assume that the energetic coupling between the field from the central dipole and the surrounding dipoles is small compared to the thermal energy, then the orientation of the dipoles will be proportional to the field. Since the integral of the $z$-component of the field over the spherical shell is 0 we see that in this simple model we should not expect any contribution to $g_{\text{k}}$ from the dipoles in the shell. Their only effect will be to create a field inside the spherical shell. This field interacts favorably with the central dipole. If we allow the density of the surrounding dipoles to vary with the position, and further assume that they prefer to be displaced to regions with a large electric field, this implies that there will be an increased density of dipoles in the backward and forward direction of the central dipole where the field is larger. In these regions the preferred orientation of the surrounding dipoles is parallel with the central one. This will give a positive contribution to the Kirkwood $g$-factor.

There is, however, an opposing effect originating from the fact that the field in these regions is larger, and using the ideas of Langevin³ we may conclude that the orientation of dipoles in the backward and forward directions of the central dipole has a tendency to be saturated. This will give a negative contribution to the Kirkwood factor. Both these effects depend on the coupling between the central dipole and the surrounding dipoles in relation to the thermal energy. Formally, we may write this coupling $\mu_{\text{c}}\mu/(kTR^3)$. The subscript c on the first $\mu$ indicates that the central dipole may be different from the

surrounding ones. In this way we can allow it to model the effect of a set of central spherical shells.

There is, however, a much more important contribution to the Kirkwood $g$-factor. To understand this we need to surround the first solvation sphere with a second one. This second spherical shell will, like the first one, give rise to an electric field inside itself. This field will polarize the dipoles in the more central spherical shell and thereby generate a positive contribution to the $g$-factor. To analyze the radial dependence of this effect we will use a simple dielectric model. If we assume a central dipole $\mu_{\mathrm{c}}$ located in an inner region with radius $R$ and an outer region characterized by the same radius $(R)$, the dipole of the inner region will generate a reaction field $^{4}-2(\epsilon-1) \mu_{\mathrm{c}} /$ $(R^{3}(2 \epsilon+1))$. If we regard the inner region as polarizable we can calculate its polarizability $^{39}$ to $R^{3}(\epsilon-1) /(\epsilon+2)$. Here, we note that the product of the reaction field and the polarizability is independent of $R$, indicating that we must expect this term to be important also in large systems.

The discussion above is based in the assumption that the studied system is isotropic in the length scale of the studied system. As will be seen below it is highly questionably if this true. We will return to this issue later in this work.

### 3. Simulation Protocol
In this work we will report the results obtained from a large set of simulations all of Monte Carlo type using the algorithm of Metropolis et al. $^{40}$ A common feature is that all particles are described with a so-called Stockmayer potential, implying that they interact with a Lennard-Jones potential and with dipole-dipole interactions.

$$
\begin{aligned}
& U_{\text {int }}= \\
& 4 \epsilon\left((\sigma / r)^{12}-(\sigma / r)^{6}\right)+1 /\left(4 \pi \epsilon_{0}\right)\left(\underline{\mu}_{1} \underline{\mu}_{2} / r^{3}-3\left(\underline{\mu}_{1} \underline{\mathrm{r}}\right)\left(\underline{\mu}_{2} \underline{\mathrm{r}}\right) / r^{5}\right) \quad(4)
\end{aligned}
$$

The quantities underlined in the equation are vectors, $\underline{\mu}$ is the dipole moment of the interacting dipoles, $\underline{\mathrm{r}}$ is the vector between the dipoles, and $r$ is its length. No truncation of the interaction potential was used apart from in the initial equilibration of the largest system. In this equation $\epsilon_{0}$ is the dielectric permittivity of vacuum. The values used for the LJ parameters are $\epsilon=$ $0.75 k T$ and $\sigma=2.8893 \AA$. These values are chosen to model a system with long-range properties similar to those of water. The dipole moment of the particles has been varied as well as the number of dipoles in the studied system, but a temperature of $315.8 \mathrm{~K}$ is used in all simulations.

The studied systems can also be characterized by a set of reduced variables. Normally these are defined as $\rho^{*}=\rho^{*} \sigma^{3}$, $T^{*}=k T / \epsilon$, and $\mu^{*}=\sqrt{ }\left(\mu^{2} / \epsilon \sigma^{3}\right)$. The first of these $\left(\rho^{*}\right)$ is not exactly defined here, since the volume and thus $\rho$ is somewhat arbitrary (vide infra), but effectively a value close to 0.92 is used in this study. $T^{*}$ has the value 1.3333 . Values for the reduced dipole moments of $1.86,1.57,1.29,1.00,0.72$, and 0.43 correspond to the dipole moments of $1.651,1.397,1.143$, $0.889,0.635$, and $0.381 \mathrm{D}$ that are used in this work.

The exact phase behavior of the studied systems is not known, but test calculations that we have done using both periodic boundary conditions and the minimum image approximation indicate that none of the studied systems prefers a solid-like phase but that the system with the largest dipole moment is fairly close to the phase boundary between the liquid and solid phases.

In order to confine the particles to the sphere we have used a potential of the form

$$
U_{\text {drop }}=P\left(s / R_{\text {drop }}\right)^{100}
$$

acting on each particle. The constant $P$ in the equation is given the value $100 k T$. Here, $s$ is the distance from the center of the droplet to the particle and $R_{\text {drop }}$ is a parameter determining the size of the droplet. For a particle located at $R_{\text {drop }}$ the potential takes the value $100 k T$. For a system with 10000 particles $R_{\text {drop }}$ has been given the value $40.088 \AA$. For systems containing another number of particles the radius is scaled by $\left(N_{\text {part }} /\right.$ $\left.10000)^{1 / 3}\right)$.

If the entire volume inside $R_{\text {drop }}$ is considered to be allowed for the particles, this corresponds to a volume per particle of $27.00 \AA^{3}$. Since not all the volume is accessible the actual volume will be slightly less. It is probably also so that with the choice of potential function used here, this volume/particle decreases slightly with increasing number of particles. The actual effective volume per particle is close to $25.93 \AA^{3}$ in these simulations. The volume of a water molecule is close to 29.9 $\AA^{3}$. We have tested the effect of varying the volume/particle, and no drastic changes has been seen. For a systems with 3000 and 10000 particles we have also tested the effect of changing the wall potential to a hard wall, but trying to preserve the accessible volume/particle. The behavior of these systems with respect to the sampled properties is almost independent of the shape of the wall potential, and some results will be presented for comparison.

Starting configurations were generated by assigning the dipolar particles to the lattice points of a primitive cubic lattice enclosed in the sphere defined by $R_{\text {drop }}$. Random orientations were given to the dipoles. New configurations were generated by a random displacement and rotation of one dipole at a time. The maximum translational and rotational parameters were 0.2 $\AA$ and 0.5 or $0.6 \mathrm{rad}$. The observed acceptance ratio was between 0.40 and 0.60 . Higher values were observed for systems with smaller dipole moments.

Typically after an equilibration which took around 300-1000 Monte Carlo steps/particle for the small systems and more than 15000 Monte Carlo steps/particle for the largest systems, the production calculations was conducted at least for twice as long. It should be noted that the equilibration required very many configurations for the larger systems.

The standard way to monitor that a simulation is carried out for long enough time is to study the correlation functions for the dipolar orientation of the particles and the diffusion of the particles. $^{41}$ For finite systems as these studied in this work it could also be appropriate to study the correlation function of the total dipole moment of the system. ${ }^{41}$ Since time does not exist in a Monte Carlo procedure one is forced to use the Monte Carlo steps as an artificial time. To illustrate that these basic conditions are fulfilled in these simulations we present in Figure 1a the dipolar autocorrelation function for the individual dipoles as well as the corresponding quantity for the total dipole of the droplet obtained for a system containing 30000 particles. From the figure it is clear that the autocorrelation function for the individual dipoles has decayed to values less than 0.01 after 2000 Monte Carlo steps/particle. The autocorrelation function for the total dipole moment of the droplet decays much faster, and the memory is lost after less than 500 Monte Carlo steps/ particle. (The much larger fluctuations for the latter curve are due to that the curve for the individual dipoles is averaged over 30000 particles.) In Figure $1 \mathrm{~b}$ we present the square of the displacement of the individual particles as a function of the Monte Carlo time. As expected, a linear relation is obtained for larger (Monte Carlo) times. The convergence behavior in the largest system is also illustrated in Table 1. After a fairly long equilibration where the interaction potential was truncated

![](./images/811968386136276992_1.jpg)

![](./images/811968386136276992_2.jpg)

Figure 1. (a) Dipolar autocorrelation functions as defined in ref 41 for the individual dipoles (full line) and for the total dipole moment of the droplet circles, as a function of the number of moves/particle for a system containing 30 000 particles with a dipole moment of 1.651 D. (b) Quadratic displacement of the dipolar particles $\langle r^2\rangle$ as defined in ref 41 as a function of the number of moves/particle for the system in (a).

![](./images/811968386136276992_3.jpg)

![](./images/811968386136276992_4.jpg)

Figure 2. $\langle \mu^2/(3kTR^3)\rangle$ as a function of $R$ (a) and as a function of $(R/R_{\text{drop}})^3$ (b) for systems with different numbers of particles. The particle dipole moment is 1.651 D. Full line = 30 000 particles, full line with diamonds = 10 000 particles, dashed line = 3000 particles, long dashed line with circles = 1000 particles, and dot-dashed line = 300 particles.

![](./images/811968386136276992_5.jpg)

Figure 3. Distance-dependent Kirkwood factor $G_{\text{k}}(R)$ as a function of $R$ for different sizes of the droplets. The particle dipole moment is 1.651 D. The meaning of the symbols is the same as in Figure 2.

at 50 Å the full interaction potential, i.e., all particles interact with all other particles, was turned on. (The data in the table shows the behavior after the long-range part of the potential was turned on. It should be noted that the system was not completely equilibrated with the truncated potential when the full potential was turned on.) In the table, subaverages evaluated over 3000 Monte Carlo steps/particle are presented for the dipolar, Lennard-Jones, and the total energy/particle in the system. The much smaller cavity interaction energy term is not presented in the table but can be calculated as the difference between the total energy and the other two terms.

From the table it is seen that after the initial 15 000 Monte Carlo steps/particle the energetics is more or less constant with typical fluctuations of 0.01 kJ/mol between different subaverages, and no drift is seen in the calculated energies.

Since the obtained results (vide infra) are in contradiction with the present view that the dipolar order is short-ranged, a number of measures have been taken to ensure that the obtained results are not numerical artifacts. These measures will be presented and discussed at the end of the next section after the presentation of the results.

The fact that more than15 000 Monte Carlo steps are needed to equilibrate a droplet containing 30 000 particles seems to be in contradiction with the data presented in Figure 1, parts a and b. The only possible explanation to the slow equilibration process is that there is some intermediate structure that equilibrates slower than both the autocorrelation functions of

![](./images/811968386136276992_6.jpg)

Figure 4. Distance-dependent Kirkwood factor $G_{\text{K}}^{(1)}(R)$ as a function of $R$ for different particle dipole moments. Panels a−e correspond to droplets with 300, 1000, 3000, 10 000, and 30 000 particles, respectively. Different curves correspond to different dipole moments for the particles. Full line, $\mu = 0.381$ D; full line with circles, $\mu = 0635$ D; dashed line with squares, $\mu = 0.889$ D; long dashed line with diamonds, $\mu = 1.143$ D; dot-dashed line, $\mu = 1.397$ D; full line with triangles $\mu = 1.651$ D.

the total dipole moment of the droplet and autocorrelation function of the individual dipoles. This means that some structure must exist on the intermediate length scale. The issue will be further discussed in connection with Figure 5.

Finally it should be said that the calculations presented here are large, and for comparison it could be mentioned that 3000 Monte Carlo steps/particle for the system containing 30 000 particles takes roughly 1 week on an ordinary PC with a 2.2 GHz processor. This corresponds to that roughly 150 new conformations can be generated in 1 s. A new sampling of information was collected when every particle had been moved 20 times.

## 4. Droplet Simulations

Equation 2 was originally derived by Berendsen$^{31}$ and has been used by Powles et al.$^{32}$ and Senapati and Chandra$^{33}$ to analyze the results obtained from simulations of Stockmayer droplets. It should be noted that only small systems, with a few

<table>
<caption>TABLE 1: Behavior of the Average Energy/Particle and Its Components for a System with 30 000 Dipolar Particles with a Dipole Moment of 1.651 Da</caption>
<thead>
<tr>
<th>configuration no.</th>
<th>total energy (kJ/mol)</th>
<th>dipolar energy (kJ/mol)</th>
<th>Lennard-Jones energy (kJ/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>90 000 000</td>
<td>−21.551</td>
<td>−11.974</td>
<td>−10.011</td>
</tr>
<tr>
<td>180 000 000</td>
<td>−21.745</td>
<td>−12.068</td>
<td>−10.017</td>
</tr>
<tr>
<td>270 000 000</td>
<td>−21.796</td>
<td>−12.078</td>
<td>−10.038</td>
</tr>
<tr>
<td>360 000 000</td>
<td>−21.838</td>
<td>−12.097</td>
<td>−10.047</td>
</tr>
<tr>
<td>450 000 000</td>
<td>−21.863</td>
<td>−12.102</td>
<td>−10.063</td>
</tr>
<tr>
<td>540 000 000</td>
<td>−21.848</td>
<td>−12.100</td>
<td>−10.057</td>
</tr>
<tr>
<td>630 000 000</td>
<td>−21.855</td>
<td>−12.104</td>
<td>−10.051</td>
</tr>
<tr>
<td>720 000 000</td>
<td>−21.857</td>
<td>−12.101</td>
<td>−10.057</td>
</tr>
<tr>
<td>810 000 000</td>
<td>−21.851</td>
<td>−12.097</td>
<td>−10.058</td>
</tr>
<tr>
<td>900 000 000</td>
<td>−21.863</td>
<td>−12.111</td>
<td>−10.053</td>
</tr>
<tr>
<td>990 000 000</td>
<td>−21.852</td>
<td>−12.108</td>
<td>−10.045</td>
</tr>
<tr>
<td>1 080 000 000</td>
<td>−21.857</td>
<td>−12.106</td>
<td>−10.051</td>
</tr>
<tr>
<td>1 170 000 000</td>
<td>−21.859</td>
<td>−12.110</td>
<td>−10.051</td>
</tr>
<tr>
<td>1 260 000 000</td>
<td>−21.865</td>
<td>−12.112</td>
<td>−10.051</td>
</tr>
<tr>
<td>1 350 000 000</td>
<td>−21.870</td>
<td>−12.108</td>
<td>−10.052</td>
</tr>
<tr>
<td>1 440 000 000</td>
<td>−21.873</td>
<td>−12.107</td>
<td>−10.063</td>
</tr>
<tr>
<td>1 530 000 000</td>
<td>−21.858</td>
<td>−12.106</td>
<td>−10.051</td>
</tr>
<tr>
<td>1 620 000 000</td>
<td>−21.866</td>
<td>−12.106</td>
<td>−10.058</td>
</tr>
<tr>
<td>1 710 000 000</td>
<td>−21.856</td>
<td>−12.102</td>
<td>−10.053</td>
</tr>
<tr>
<td>1 800 000 000</td>
<td>−21.880</td>
<td>−12.114</td>
<td>−10.059</td>
</tr>
<tr>
<td>1 890 000 000</td>
<td>−21.859</td>
<td>−12.098</td>
<td>−10.059</td>
</tr>
</tbody>
</table>

a Each of the estimated energy averages are evaluated over 90 000 000 configurations, corresponding to 3000 Monte Carlo steps/particle.

hundred particles have been studied. Recently the dielectric behavior of polar fluids confined to spherical droplets has been studied by other means.42,43 It also deserves to be mentioned that the convergence behavior of Ewald summation and droplet simulations have been compared.44 The conclusion from that work is that the Ewald summation technique yields superior convergence behavior. The systems studied in ref 44 are, however, so small (1000−2000 particles) that the effects discussed in this work are not present or strongly influenced by the limited size of the system.

In Figure 2a we present calculated values for $\langle \mu^2/(12\pi kTR^3)\rangle$ as a function of $R$ for particles with a dipole moment of 1.651 D. From Figure 2a it is clearly seen that the maximum value for $\langle \mu^2/(12\pi kTR^3)\rangle$ increases when the size of the system is increased from 300 to 10 000 particles. However, when the number of particles is further increased the curve changes its shape.

In Figure 2b we have plotted $\langle \mu^2/(12\pi kTR^3)\rangle$ as a function $R^3$ to allow for evaluation of the dielectric permittivity according to eq 2. The standard way to analyze the data is to extrapolate the almost linear part of the curve to its intersection with the $y$-axis. The intercept should take the value $(\epsilon - 1)(2\epsilon + 1)/9\epsilon$. For large $\epsilon$ this simplifies to that the intercept equals $\epsilon/4.5$. When plotted in this way one clearly sees that the major part of the difference seen in Figure 2a between the 1000 and 3000 particles system are picked up by the equation and that both these systems yield a dielectric permittivity close to 180. For the 300 particle system we obtain a much smaller value (around 120). The system with 10 000 particles yields a permittivity of close to 350. We also see that we do not obtain a perfect straight line in any of the systems and that the results are dependent on the way the extrapolation is performed. The most interesting observation is, however, that the curve describing a system with 30 000 particles behaves differently and that the evaluation of a permittivity is difficult since two regions can be found. This curve shows a more rapid decrease than the others when the $x$-coordinate is increased from 0.5 to 1.0. However, for smaller $x$-values a plateau is reached.

There is a technical detail that also may be of interest. The sampling of different quantities was very easy for the systems containing 1000−3000 particles and, e.g., after less than 500 Monte Carlo steps/particle we obtained curves similar to the one presented in Figure 2a for the system containing 1000 particles. However, for the system containing 30 000 particles the sampling showed a slow convergence and different subav- erages evaluated over 3000 Monte Carlo steps/particle looked very different. The curves presented in Figure 2, parts a and b, are obtained for 30 000 particles and calculated from $3 \times 10^5$ Monte Carlo steps/particle. The impression one gets is that there are several almost equally good, but very different ways to organize the system containing 30 000 particles. Despite the fact that time does not exist in Monte Carlo simulations one is tempted to conclude that the observed behavior may correspond to the presence of a long relaxation time for an intermediate size structure present in the system. We will return to this issue later.

Inspired by this, but partly also by the work of Shelton,12−14 and by the different convergence behavior induced in simula- tions of bulk dipolar systems by the boundary conditions, we decided to see if we could locate any domains with dipolar order. To our knowledge there does not exist any established procedure for this task. The Kirkwood $g$-factor seems to be a natural starting point, since it measures exactly this type of behavior. Thus, in a first step we calculated the distance-dependent Kirkwood factor $G_{\text{k}}(R)$, discussed above, for each particle in a configuration generated by the Monte Carlo chain that we were to investigate for domains. In practice we evaluated $G_{\text{k}}(R)$ in discrete steps of 0.53 Å. For such a function there exists at least one maximum. In some cases the function showed more than one maximum. In these cases we used the one occurring at the smallest value of $r$, provided that this maximum was separated from higher values of $G_{\text{k}}(R)$ observed for larger $r$ by at least an increase in $r$ of 1.59 Å. In practice this last criteria was introduced to allow the domain to grow outside the oscillatory behavior induced by the packing at short distances (3−6 Å). Thus the domain associated with a particular dipole was characterized by the radius yielding maximum value for $G_{\text{k}}(R)$ and the $G_{\text{k}}(R)$ value. The definition is operational and implies that we consider the domain to grow as long as the average order of the dipoles in the spherical shell that surrounds the domain gives a positive contribution to the dipole moment of the domain in the direction of the central dipole.

To identify the most important domain we decided that this was the domain with the largest value for $G_{\text{k}}(R)$ and that the size was the corresponding radius. The domains defined in this way may not be the regions with largest order that can be observed in the studied droplets. There may be other regions (larger or with higher order). These domains may escape detection if the normalized scalar products of their dipole moment and the dipole moment of the central dipoles in the domains is not large enough. This is however not crucial since the main purpose is to prove the existence of large ordered regions.

To locate the second most important domain we decided that its origin must not be located inside the sphere defining the first domain. The second domain was then identified as the largest value of $G_{\text{k}}(R)$ remaining when all particles inside the previously defined domains had been excluded from the search. The procedure was repeated several times to locate more domains until at most 20 domains were located. To remove small domains we introduced the condition that the maximum value of $G_{\text{k}}(R)$ must be at least 10% of that for the most

![](./images/811968386136276992_7.jpg)

Figure 5. (a) Distance-dependent Kirkwood factor for the most central dipole in a droplet with 30 000 particles with a dipole moment of 1.651 D. Both subaverage curves (thin line) obtained from 3000 Monte Carlo steps/particle and average curves (thick line) calculated from 24 000 Monte Carlo steps/particle are presented. In panel b the same data is presented for the central dipole in the most important domain for the same system and the same configurations.

<table>
<caption>TABLE 2: Properties of the Domains Observed in Simulations of Droplets with 300, 1000, 3000, 10 000, and 30 000 Particles with a Dipole Moment of 1.651 D</caption>
<thead>
<tr>
<th>no. of particles</th>
<th>droplet radius $R_{\text{drop}}$ (Å)</th>
<th>domain radius $R$ (Å)</th>
<th>$R/R_{\text{drop}}$</th>
<th>max $G_{\text{k}}(R)$</th>
<th>% alignment</th>
<th>$\mu^{2}(G_{\text{k}}^{\text{m}})^{2}/(8\pi\epsilon_{0}ktR^{3})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>12.5</td>
<td>10.6</td>
<td>0.85</td>
<td>18.3</td>
<td>9.9</td>
<td>8.81</td>
</tr>
<tr>
<td>1000</td>
<td>18.6</td>
<td>13.2</td>
<td>0.71</td>
<td>37.9</td>
<td>9.5</td>
<td>19.4</td>
</tr>
<tr>
<td>3000</td>
<td>27.5</td>
<td>19.1</td>
<td>0.69</td>
<td>69.3</td>
<td>7.0</td>
<td>21.8</td>
</tr>
<tr>
<td>10000</td>
<td>40.1</td>
<td>28.0</td>
<td>0.70</td>
<td>195</td>
<td>5.7</td>
<td>53.9</td>
</tr>
<tr>
<td>30000</td>
<td>57.8</td>
<td>40.2</td>
<td>0.70</td>
<td>331</td>
<td>3.2</td>
<td>67.5</td>
</tr>
</tbody>
</table>

important domain for the configurations, otherwise the domain was discarded.

This procedure deserves a few comments. First of all we have assumed that the domains are spherical. This is not necessarily the optimal choice, but as will be seen below it is sufficient to localize a set of meaningful domains. It could be argued that a spherical shape is arbitrary. However, since dipoles located on a spherical shell, surrounding the central dipole in the domain, on the average gives a zero contribution to the Kirkwood $g$-factor, provided that the dipole−dipole coupling is weak enough, this seems to be a natural choice.

It should be noted that for other choices of shells, e.g., ellipsoidal ones, it is no longer true that the long-range contribution to the Kirkwood factor cancels, implying that domains with infinite size and Kirkwood factor are possible in infinite systems. There is naturally also the possibility to interpret the structures formed in terms of a vortex as suggested by Groh and Dietrich. To perform such an analysis is more complicated in a sphere than in a cube since the direction of the vortex is arbitrary in the sphere. We note, however, that if the preferred structure was vortex-like, then it would be possible to identify spherical domains in such a system with the procedure used in this work. We note again that the structures identified here in this work are intermittent structures, whereas the vortex-like structures of Groh and Dietrich are average structures. There is thus no conflict between the results reported here and their results. The important issue in this work is to demonstrate that there exist long-range structures and correlations in a droplet made from dipolar particles, and their exact shape is a much less important issue.

Second the calculated radii for the domains indicate often a volume that is too large for the domain, since many domains are located a good distance from the origin of the droplet. Thus, part of these domains is actually in regions outside the droplet. In Table 2 we give average values for properties associated with the most important domain identified in droplets with 300 to 30 000 particles. The maximum $G_{\text{k}}^{\text{m}}$ values reported in the table show that regions with a substantial dipolar orientation are observed in the studied droplets. (The superscript m is introduced to indicate that the $G_{\text{k}}$ value applies to the most important domain.) For example, in the droplets with 30 000 particles, on the average one finds one domain with a dipole moment that is around 430 times the dipole moment of one dipole and that this domain has a radius of 40 Å, which is close to 70% of the droplet radius. From the table it is thus clear that domains are formed, that their size is increased when the size of the droplet is increased, and that the maximum value of the Kirkwood factor for the central dipole in the most important domain $G_{\text{k}}^{\text{m}}(R)$ grows faster than the domain or droplet radius and slower than the domain or droplet volume.

For clarity we note that the average value of the dipole moment of the domain in the direction of an arbitrary dipole in the domain is not proportional to $G_{\text{k}}^{\text{m}}$, but rather to the square root of this quantity as is suggested by eq 3, but that the dipole moment of the domain in the direction of the central dipole in the domain equals $\mu G_{\text{k}}^{\text{m}}$.

It also deserves to be said that the search for domains in the larger systems with large dipole moment was made in only around half of all the generated configurations. We have, however, ensured that the presented data have a good numerical accuracy and we have also observed that the convergence of the data describing the domains is much easier to obtain than the convergence for the data describing the entire droplet presented in Figure 2, parts a and b. This will be further discussed in connection with the presentation of Figure 5. Before doing this it is appropriate to return to the discussion about the results presented in Figure 2. Since we have shown that domains with a radius of around 70% of the droplet radius are formed one should no longer be surprised that the analysis of data obtained for the largest system based on an isotropic model did not work. It is probably more relevant to ask why the analysis seemed to work for the smaller systems studied.

<table><thead><tr><th>configuration no.</th><th>importance no.</th><th>R-cord (Å)</th><th>θ-cord (deg)</th><th>φ-cord (deg)</th><th>R (Å)</th><th>$G_{\text{K}}^{\text{m}}$</th><th>$\mu_{x}$ (D)</th><th>$\mu_{y}$ (D)</th><th>$\mu_{z}$ (D)</th></tr></thead><tbody><tr><td>180000000</td><td>1</td><td>27.8</td><td>87.9</td><td>344.1</td><td>32.3</td><td>390</td><td>590.3</td><td>294.0</td><td>−14.3</td></tr><tr><td>180000000</td><td>2</td><td>41.9</td><td>89.6</td><td>87.3</td><td>35.4</td><td>332</td><td>−497.0</td><td>−172.6</td><td>−158.2</td></tr><tr><td>180000000</td><td>3</td><td>46.2</td><td>54.4</td><td>50.9</td><td>32.8</td><td>294</td><td>−504.9</td><td>173.3</td><td>−32.9</td></tr><tr><td>90000000</td><td>1</td><td>13.6</td><td>84.9</td><td>12.4</td><td>36.0</td><td>524</td><td>582.6</td><td>654.3</td><td>−73.9</td></tr><tr><td>90000000</td><td>2</td><td>39.0</td><td>75.3</td><td>176.1</td><td>36.0</td><td>305</td><td>128.1</td><td>−445.3</td><td>210.4</td></tr><tr><td>90000000</td><td>3</td><td>45.2</td><td>111.7</td><td>125.7</td><td>36.5</td><td>268</td><td>−277.9</td><td>−109.4</td><td>372.3</td></tr><tr><td>0</td><td>1</td><td>27.1</td><td>117.7</td><td>129.6</td><td>31.7</td><td>281</td><td>−392.4</td><td>−234.2</td><td>−118.6</td></tr><tr><td>0</td><td>2</td><td>19.0</td><td>94.5</td><td>16.9</td><td>36.0</td><td>268</td><td>−326.5</td><td>148.3</td><td>286.0</td></tr><tr><td>0</td><td>3</td><td>54.0</td><td>108.0</td><td>181.6</td><td>30.7</td><td>199</td><td>−159.4</td><td>−270.0</td><td>159.8</td></tr></tbody></table>

$^{a}$ The different domains are separated by 3000 Monte Carlo steps/particle. The location is presented in polar coordinates, and angles are given in degrees.

In order to illustrate the structure, "dynamics", and energetics of the domains, Table 3 presents the origin and dipole moment of the three most important domains in configurations that are separated with 90 000 000 moves of the particles (3000 Monte Carlo steps/particle). The system that is studied is the largest one with 30 000 particles with a dipole moment of 1.651 D. The data presented in the table gives also an idea of the relative orientation and location of the most important domains in the droplet. The domain importance number is given in the table. Inspection of the data in the table suggests that the most important domain in configuration number 180 000 000 is rather similar to the most important domain in configuration number 90 000 000. The origin is displaced around $17\ \mathring{\text{A}}$ and the angle between the two dipolar vectors is $24.5\ ^{\circ}$. There is no obvious relation between the other domains listed in the table.

In Figure 3 we present average value curves for the distance- dependent Kirkwood factor calculated for the central dipole in the most important domain in the five systems studied in Table 2. The data presented in the figure clearly shows that the domain size, as defined by the maximum value for the Kirkwood factor in the figure, increases with the size of the droplet. This is partly an effect of the increased size of the droplet that would be seen even if the dipoles were noninteracting. To investigate the importance of this effect we have calculated similar curves as presented in Figure 3, where we have varied the particle dipole moment.

In Figure 4a we present similar data for a system with 300 particles where the particle dipole moment has been varied from 0.381 to 1.651 D in steps of 0.254 D. In Figure 4b−e we present the corresponding information for systems containing 1000, 3000, 10 000, and 30 000 particles.

A good starting point for the analysis of the data presented in Figure 4a−e is the observation that for each size of the system, the curves obtained for the two smallest dipole moments are almost identical. For these systems the dipole−dipole interaction between nearest neighbors is smaller than $kT$, and we can expect the size of the observed regions to reflect the formation of polarized region due to entropical reasons. The regions observed for these dipole moments are almost inde- pendent of the dipole−dipole interaction and reflect conse- quently the size of the regions that would be observed in systems of a given size if the dipoles were energetically uncorrelated. There is, however, an indication that not even in the system made from particle with the smallest dipole moments the dipoles are completely uncorrelated. The long-range tail of the distance- dependent Kirkwood factor decreases slightly. This is an illustration of that there is an energetic cost of creating a dipole in vacuum.

If the dipole moment of the particles is increased, the ordered regions become smaller for the smaller systems and larger for the larger systems. From the data presented in Figure 4a−e it is clear that for the two smallest systems (300 and 1000 particles) the size of the regions, as defined by the maximum values of the curves presented in the figures, is slowly decreasing when the particle dipole moment is increased. The orientational order within the regions decreases first when the dipole moment of the particles is increased but starts to increase when the nearest neighbor interaction becomes larger than $kT$ ($\mu = 0.889$ D). One explanation to that the domains get smaller when the dipole moment is increased is that the entropically formed domains for the small droplets are large compare to the entire droplet and that the energetically stabilized domains need a surrounding. It is thus necessary for the domains to shrink in order that there should be space for a surrounding. For the larger droplets (10 000 and 30 000 particles) both the size of the regions and the orientational order within the regions are more pronounced for the larger dipole moments. Here the sizes of the entropically stabilized domains are smaller than the energetically stabilized domains, that seem to prefer a radius of around 70% of the droplet radius.

The presented data clearly shows the formation of electro- statically stabilized domains in the larger systems with large particle dipole moment. The domains formed under these conditions are much larger than the regions that are formed for entropical reasons, and they must have an energetic origin.

For comparison, in Figure 4, parts c and d, we also show the curves calculated when the standard wall potential (eq 6) is replaced with a hard wall. Only calculations with a dipole moment of 1.651 D are presented. The influence of the wall potential is relatively small indicating that the domain formation is fairly insensitive to the shape of the wall potential although the maximum value for $G_{\text{K}}^{\text{m}}$ decreases with 20% in the largest system with the hard wall. The hard wall is located 0.5 (3000 particles) and $1\ \mathring{\text{A}}$ (10 000 particles) inside the value given to $R_{\text{drop}}$ in the two simulations to compensate for the fact that not all the volume inside the $R_{\text{drop}}$ is accessible to the particles when eq 5 is used.

The most important observation that can be made from Figure 4a−e is that the observed structures are growing rapidly with the size of the system and that no saturation can be seen. If the structures were induced by the surrounding of the droplet one would expect that the observed domains should decrease in importance as the system grows.

In Figure 5a we present the distance-dependent Kirkwood factor for the dipolar particle that is closest to the center of the droplet. This particle is the one that fulfills the requirements given by eq 3 best. Several curves are presented. Each thin line curve represents the results from sampling of 3000 Monte Carlo steps/particle, and the thick line is the corresponding average curve. The data is collected from our simulation of 30 000

particles with a dipole of 1.651 D. Several interesting observa- tions can be made. First of all it is clear that the different subaverages are very different and that we cannot expect the average curve to be of high accuracy. In Figure 5b for comparison the corresponding curves from the same simulations calculated for the central dipole in the most important domain are presented. These latter curves show a much better conver- gence.⁴⁵ The origin of the difference is obvious. The central dipole in the most important domain is always surrounded by dipoles with a preferential orientation parallel with itself, whereas the dipole that is central in the droplet sometime is close to a domain origin with a parallel orientation and sometime with an antiparallel orientation, or it may be located at or close to the boundary between different domains. Thus, it is clear that the fluctuations in the distance-dependent Kirkwood factor for the dipole that is central in the droplet are much larger than the fluctuations for the dipole that is central in the most important domain. If we consider this information together with the information obtained from Figure 1a, that the dipolar autocorrelation function decayed fast, one reaches the conclusion that the location of the domains change rather rapidly, faster than the diffusion of the dipoles.

Second it is clear that the region that appears to be ordered around the dipole that is central in the droplet is around 25 Å, if we look at the curve presenting the average values in Figure 5a. However, if we look at the curves for each of the 3000 Monte Carlo steps/particle simulations the structure is much more long-ranged (around 45 Å) as are the curves for the central dipole in the most important domain presented in Figure 5b. We also note that the maximum value for the Kirkwood factor for the two situations differs by a factor of 10 or so. These observations may at first seem anti-intuitive, but if one analyzes the situation starting from a liquid built up from ordered domains it is obvious that the ordered region around the dipole that is central in a domain is larger than the ordered region a round a dipole that is closer to the boundary of the domain and obviously the observed Kirkwood factor for the central dipole is larger that that for the more distal dipole. We thus reach the important conclusion that the domains present in a dipolar system are considerably larger than the correlation length observed via the distance-dependent Kirkwood factor for the average dipole.

We will now for a while focus on the energetic origin of the domain formation. As a start we will analyze the energetics between the domains presented in Table 3. Looking on the configuration labeled 18 000 000 we can see that the distances between the three domains are 55.3, 45.1 and 36.6 Å for domains 1 and 2, domains 1 and 3, and domains 2 and 3, respectively. The corresponding pair interactions are $-47kT$, $-95kT$, and $-82\ kT$. For the other two conformations we can calculate the distances 51.5, 52.1 and 43.3 Å for the configu- ration labeled 90 000 000 and 37.5, 41.3 and 71.4 Å for the conformation labeled 0. The corresponding energies are $-65kT$, $-37kT$, and $-90kT$ for the conformation labeled 90 000 000 and $-76kT$, $-80kT$, and $-3kT$ for the conformation labeled 0.

If we estimate the solvation energy of a domain using

$$
G_{\mathrm{solv}}=-1/(4\pi \epsilon_{0})(\epsilon-1)/(2\epsilon+1)\mu^{2}/R^{3} \tag{6}
$$

and assign the value $\mu G_{\mathrm{k}}^{\mathrm{m}}$ to the domain dipole moment and the value 0.5 to the factor $(\epsilon-1)/(2\epsilon+1)$, we see that the domain solvation energy in $kT$ equals $\mu^{2}(G_{\mathrm{k}}^{\mathrm{m}})^{2}/(8\pi \epsilon_{0}kTR^{3})$. From Table 2 we see that this quantity increases with droplet size and that the quantities are of the same order of magnitude as the calculated domain-domain interactions.

<table>
<caption>TABLE 4: Interaction of the Most Important Domain with Other Domains (in $kT$) Observed in a Droplet Made from 30 000 Particles with a Dipole Moment of 1.651 D for Varying Number of Dipolar Particles</caption>
<thead>
<tr>
<th>no. of particles in the system</th>
<th>no. of particles in the domain</th>
<th>domain interaction ($kT$)</th>
<th>domain interaction/particle ($kT$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>183</td>
<td>−56</td>
<td>−0.306</td>
</tr>
<tr>
<td>1000</td>
<td>361</td>
<td>−99</td>
<td>−0.274</td>
</tr>
<tr>
<td>3000</td>
<td>995</td>
<td>−133</td>
<td>−0.134</td>
</tr>
<tr>
<td>10000</td>
<td>3425</td>
<td>−284</td>
<td>−0.083</td>
</tr>
<tr>
<td>30000</td>
<td>10113</td>
<td>−430</td>
<td>−0.043</td>
</tr>
</tbody>
</table>

To get further insight into this we have chosen to study the domain-domain interaction in more detail. In Table 4 we present estimated interactions between the most important domain and all other domains, assuming that each domain can be represented with its total dipole moment ($\mu G_{\mathrm{k}}$). In the table we also present an estimate of the number of particles in the domain and the average interaction energy for one of these particles with all other domains. It is easy to see that the domain interaction scales almost as $\mu^{2}(G_{\mathrm{k}}^{\mathrm{m}})^{2}/(8\pi \epsilon_{0}kTR^{3})$ although it is somewhat larger than the dielectric estimate. One must keep in mind that the numbers presented in Table 4 should be divided by 2 in order to be compared with the dielectric estimate, since the number in the table refers to the interactions between the most important domain and all other domains. It seems reasonable that half of this energy is associated with the domains solvating the central domain.

One can compare the domain interaction per particle with the solvation energy of a dipole in a dielectric medium (eq 6) and use the domain radius as cavity radius. One obtains $(6.2 \times 10^{-4})kT$ for our largest system using a domain radius of 37 Å. This value is almost 2 orders of magnitude smaller than the value in Table 4 for the corresponding system. The main reason for the difference is that in the dielectric model, it is assumed that the dipoles responsible for the solvation of the central dipole are ordered by the interaction with the field from the central dipole, whereas in our system these dipoles are ordered by the field from all dipoles in the domain of the central dipole. This is verified by calculating the angular part of the dipole-dipole interaction. This function takes the value $-2$ when the dipoles are parallel and displaced along the dipole vector; it assumes the value $+2$ for the same positions when the dipoles are antiparallel. Negative values indicate an attractive orientation and positive values a repulsive interaction. Typical average values between the most important domains in our systems with a dipole moment of 1.651 D are between $-0.9$ and $-1.2$. This shows a strong attractive correlation between the domains. The corresponding value calculated for smaller dipole moments is much closer to 0.

It could be argued that, with the present definition of the domains, they are partly overlapping and that the analysis above is not strict. If we, however, use half the domain radius defined above as a more conservative definition of the domain radius, then there will be no overlap between the domains and the Kirkwood factor for the particles in the domain will roughly be between 30% and 50% of the values quoted in Table 4, resulting in a domain-domain interaction that is a factor of 4−10 smaller than the values in the table for the domain- domain interactions. These interactions will in any way be orders of magnitude larger than $kT$ for the larger systems. We also note that the number of particles in the domains will be a factor of 8 smaller thus resulting in a particle-domain interaction of approximately the same strength as quoted in Table 4.

Many of the domains are located close to the surface of the droplet. This is particularly important for the smaller droplets.

One may ask the question if the increase in domain size and maximum value of the Kirkwood factor for the domains are linked to this fact. There is an obvious connection since the observed domain radii are close to 70% of the droplet radius for all but the smallest droplets. Using scaling arguments one would expect that the maximum value of the Kirkwood factor for a domain would be proportional to the domain volume and thus to the number of particles in the domain/droplet. From Table 2 we see that the alignment of the dipoles in the domains decreases with increasing droplet or domain size. At present it is not possible to answer the question if the observed domains are a consequence of the surface or if they also exist in the bulk, but we note that for the droplet sizes studied in this work the domains seem to increase in importance with increasing domain size.

In Figure 6a−c we present calculated values for the dipolar part of the domain−domain interactions for the 20 most important domains with the 19 other domains that are identified in the studied systems. The domains are represented with their total dipole moment localized to the central dipole of the domain. Figure 6a−c corresponds to the 300, 3000, and the 30 000 particle systems. The different curves correspond to different values of the particle dipole moment. The trends are clear. Larger values for the particle dipole moment correspond to larger domain−domain stabilization, larger droplets yield larger domain−domain stabilization, and the domains that have been identified as more important are more stabilized by the domain−domain interaction than less important domains. It should be noted that these energetic consequences are a very strong support for the idea that the definition of the domains made in this work is fruitful. It is difficult to explain why the orientations of the central dipoles in the identified domains have orientations that corresponds to a strong attractive coupling if the identified domains lacked physical relevance, since the direct energetic coupling between the two dipoles are close to $0.001kT$ if we assume a distance between the dipoles of $40$ Å.

If the domains are an important property of a droplets made from dipolar particles, it could be argued that it should be possible to see this directly in the distance-dependent dipole−dipole interaction. It should be possible to see it for the average dipole and not only for the central one in a domain. It is of course possible to calculate the average effective interaction between two dipoles in the droplets as a function of the distance between the dipolar particles. Simple theory suggests (see, e.g., ref 37 pp 75−76) that this interaction decays as $1/r^6$, where $r$ is the interparticle distance. We have calculated this interaction and multiplied the calculated effective interactions with $r^6$ in order to show the deviation from the expected behavior. The results obtained for the two larger systems with a dipole moment of 1.651 D are presented in Figure 7a. (In the three smaller systems with 300, 1000 and 3000 particles we do not see clear signs of domain formation, but the curve obtained for 3000 particles is included for comparison.) The theoretical arguments given above suggest that the calculated curves should be independent of $r$ for large $r$. We observe, however, that for intermediate distances and all droplets it looks as if the effective interaction decays roughly as $1/r^5$. For longer distances where we could expect influence from the surface of the droplet we see an oscillatory behavior that might reflect the packing structure of the domains in the larger droplets. If this is correct also for a bulk system and longer distances we would expect the dipole solvation energy to converge as $1/r^2$ at least for intermediate distances (15−30 Å). In order to investigate the reliability of the data presented in Figure 7a we present the results obtained from different smaller simulations each representing 8000 Monte Carlo steps/particle obtained for the system containing 10 000 particles with a dipole moment of 1.651 D. Five different curves are presented together with the average curve. The first 25−30 Å are very well converged, whereas the outer parts are very different. The only possible explanation is the formation of domains that have a “lifetime” in the simulations that corresponds roughly to 8000 Monte Carlo steps/particle in the studied system. It also means that the long-range part of the curve is not well described. It should be noted that the sampling of the distance-dependent energetics has only been performed in around 10% of the generated configurations for

![](./images/811968386136276992_8.jpg)

**Figure 6.** (a−c) Domain interaction as a function of domain importance for different dipole moments and droplet sizes. Panels a−c correspond to droplets with 300, 3000, and 30 000 particles, respectively. The meaning of the symbols is explained in the figures.

![](./images/811968386136276992_9.jpg)

Figure 7. (a) Effective dipole−dipole interaction $\times r^{6}$ as a function of the distance $r$ between the dipoles, for systems containing 30 000, 10 000, and 3000 particles with a dipole moment of 1.651 D. The color code is explained in the figure. Panel b displays the convergence behavior observed in the system containing 10 000 particles. The full line corresponds to the average curve (the same as in panel a), and the other symbols correspond to different subaverages of 8000 Monte Carlo steps/particle.

the systems containing 10 000 and 30 000 particles so the convergence of other quantities are much better.

It is possible to integrate the effective interaction curves and calculate the corresponding contribution to the solvation energy of a dipole. If we evaluate this integral from 20 to $50\ \mathring{A}$ assuming bulk density at all distances for the system containing 30 000 particles we obtain a contribution to the electrostatic part of the solvation energy of $-0.11kT$. Half of this can be assigned to the considered dipole, (the other half should be assigned to the solvating dipoles), and we can thus estimate the long-range part of the solvation energy for the studied dipole to $-0.055kT$. If we use eq 4, which assumes a dielectric behavior, to calculate the solvation energy of a dipole in a dielectric sphere with a radius of $20\ \mathring{A}$ and assign the value 0.5 to the term containing $\epsilon$, we obtain a value of $-0.004kT$, a value which is an order of magnitude smaller. Again we see that there is an energetic origin behind the structuring of the liquid. A third possibility to estimate this long-range part of dipole solvation is to sum up this interaction directly in the simulation. In this way we also take account of that the average dipole is not completely surrounded by a sphere of other dipoles with a radius of $50\ \mathring{A}$. This last estimate gives the value $-0.033kT$ for the discussed solvation energy.

![](./images/811968386136276992_10.jpg)

Figure 8. Order parameter $S$, as defined in the text, for the domain as a function of radial coordinate of the domains. Different curves correspond to different dipole moments. Full line, dipole moment = 1.651 D; dashed line, dipole moment = 1.143 D; dashed-dotted line with circles, dipole moment = 0.635 D; dashed-dotted line, dipole moment = 0.381 D.

In the presentation of data above we have given results both as a function of particle dipole moment and number of particles in the droplet. Below we will focus on the properties of the observed domains and mainly focus on systems with 30 000 particles and a dipole moment of 1.651 D, but for comparison we will also show data obtained for smaller dipole moments when relevant.

In Figure 8 we investigate how the formed domains are ordered relative to the surface of the droplet. For this purpose we define the quantity $S=\langle(\underline{r}\underline{\mu})^{2}\rangle$ which we study as a function of the location of the origin of the domain. Here $\underline{r}$ is a unit vector pointing from the droplet center to the center of the domain. The vector $\underline{\mu}$ is a unit vector in the direction of the domain dipole moment. If the dipole moment was randomly oriented one would expect this quantity to take the value 1/3. We can, however, expect that domains close to the surface would prefer an orientation of their dipoles perpendicular to $\underline{r}$, thereby minimizing the electric field in the vacuum surrounding the droplet. This would result in a lower value for the orientational parameter $S$. This is clearly seen in the figure for the systems made from particles with larger dipole moments, whereas the systems made from small dipoles show values for $S$ that are close to 1/3 for all distances. (The low value seen for very small $r$ values is due to bad statistics, since very few domains are located close to the origin of the droplet.)

In Figure 9 we address the question where in the droplet the domains are located. For the systems built from small dipoles the domains are almost randomly located in the droplets, but for larger dipoles correlations can be seen if one calculates the volume-corrected probability for a domain to be located at a certain distance form the origin of the droplet. What we actually do is that we sample $1/r^{2}$ for the center of the domains, thereby taking care of the trivial volume dependence. In the figure we have chosen to partition the observed domains into four groups according to their importance. Only data for the system with 30 000 dipoles with a dipole moment of 1.651 D is presented. From the figure it is seen that the important domains (the ones with a large total dipole moment) prefer a location in the center of the droplet, whereas the less important domains preferentially are found closer to the surface. It could be argued that this is a trivial effect originating from that part of the domains located closer to the surface contains a smaller number of dipoles, since

![](./images/811968386136276992_11.jpg)

Figure 9. Unnormalized volume-corrected probability for the radial location of a domain. Different curves correspond to domains of different importance as defined in the text. Full line = domains with importance number 1−5, full line with circles = domains with importance number 6−10, dashed line with squares = domains with importance number 11−15, and dashed-dotted line = domains with importance number 16−20.

![](./images/811968386136276992_12.jpg)

Figure 10. Probability distribution of the domain dipole moment in D, for a system containing 30 000 particles with a dipole moment of 1.651 D. Different curves correspond to domains of different importance. Full line = domain importance number 1−3, full line with circles = domain importance number 4−6, dashed line with squares = domain importance number 7−10, dashed line = domain importance number 11−15, and full line with diamonds = domain importance number 16−20.

parts of the domains are outside the droplet. However, systems constructed from dipolar particles with smaller dipole moment do not show this behavior at all or to a much lesser extent. Instead, the distributions of the domains seem to be independent of the domain importance number for smaller dipoles.

In Figures 10 and 11 we present probability distributions for the system built from 30 000 dipoles with a dipole moment of 1.651 D describing the dipole moment of the domains and the radial location of the domains. Again, we have chosen to calculate independent probability distributions for domains of differing importance.

From Figure 10, describing the distribution of the domain dipole moments we see that there is a fairly large overlap between the different probability distributions. Since for a given conformation the dipole moment of a domain in group 1−3 always is larger than the dipole moment of a domain in group 4−6, this shows that there is a strong coupling between the dipole moments of the different domains. For some sampled conformations the dipole moments of several domains are large, whereas for other conformations the domain dipole moments are smaller. What we see is simply that the domains are strongly coupled.

![](./images/811968386136276992_13.jpg)

Figure 11. Probability distribution of the domain size in Å, for a system containing 30 000 particles with a dipole moment of 1.651 D. Different curves correspond to domains of different importance. The meaning of the symbols is the same as in Figure 10.

There is an apparent discrepancy between the most likely dipole moment of a domain with importance number 1−3, which according to Figure 10 is around 750 D and the data presented in Table 2 and Figure 3. A dipole moment of 750 D corresponds to a maximum value for the Kirkwood factor of around 450. From Table 2 and from Figure 3 we obtain a maximum value for the Kirkwood factor for the same system of around 330. The difference originates form the way the different numbers have been calculated. The curves presented in Figure 10 show the distribution of the actual maximum values for the Kirkwood factor observed in the different conformations analyzed. The data presented in Table 2 and Figure 3 are calculated by adding the curves describing the distance-dependent Kirkwood factor $G_{\rm k}(R)$ for the same domains and calculating an average curve. This means that also contributions from the region after the maximum of the individual curves are included, and since the decrease in these curves after the maximum is more rapid than the increase before the maximum, we obtain this apparent discrepancy. The observed difference is thus linked to a different way of defining the average size of the domains.

In Figure 11 we show the probability distribution describing the domain size. Again the data have been partitioned according to the importance of the domains. Here we see a clear correlation, showing that more important domains correspond to a larger domain radius.

We will finally shortly address the important question of the effect of a dielectric surrounding on the studied droplet. Preliminary calculations, where the leading term (the response to the dipole moment of the droplet) has been included in the Hamiltonian describing the system, are presented in Figure 12. This has formally been done by adding a term corresponding to eq 6 to the Hamiltonian. The dipole moment used here is the total dipole moment of the droplet. Again the system containing 30 000 particles with a dipole moment of 1.651 D is studied. The dielectric discontinuity is placed 1.06 Å outside the droplet radius, and a relative permittivity of 100 is assigned to the surrounding. The data presented in the figure shows the distance-dependent Kirkwood factor $G_{\rm k}^{\rm m}(R)$ for the central dipole in the most important domain. For comparison, the corresponding curve obtained without a dielectric surrounding is included in the figure. A small decrease in the dipole moment and in the

![](./images/811968386136276992_14.jpg)

Figure 12. Distance-dependent Kirkwood factor for a system containing 30 000 particles with a dipole moment of 1.651 D. The full line corresponds to a droplet in vacuum, and the dashed line corresponds to a droplet surrounded by a relative dielectric permittivity of 100.

size of the domain is seen. The observed difference is within the estimated errors due to the incomplete sampling. It is clear that a dielectric surrounding modeled as above does not significantly change the importance of the formed domains. At distances larger than the size of the domains there is a marked difference between the two curves presented in Figure 12. The curve corresponding to a droplet in a medium levels off at a much larger value for $G_{k}^{m}(R)$ than the corresponding curve in vacuum. This corresponds to that the total dipole moment of the droplet is much larger when surrounded by a dielectric medium than when surrounded by vacuum.

As was mentioned in the section describing the computational protocol, the entire body of observed results presented above is in sharp contrast with the present view that the dipolar order is short-ranged also when the dipole−dipole coupling is large compared to the thermal energy $kT$. In order to ensure that the observed results are not numerical artifacts the following measures have been taken.

(i) For the system containing 10 000 particles two independent starting configurations were chosen, and they both resulted in similar structural parameters and energetics. Note that energetically stabilized domains are clearly seen already in this system.

(ii) The simulation performed for systems with 3000 and 10 000 particles, where the particles were confined into a hard wall sphere, also yielded similar structural data as obtained with the standard boundary. These simulations were also started from independent conformations.

(iii) For the smaller systems (300−3000 particles) several starting conformations were generated, and they all resulted in similar structural and energetic information.

(iv) A strong additional argument in favor of that the observed behavior corresponds to the equilibrium properties of the studied systems and not numerical artifacts is the consistent behavior observed when the size of the dipole moment is increased. In particular, we note that increased domain sizes are observed also for the system with a dipole moment of 1.397 D for systems containing and 10 000 and 30 000 particles. The observed increase is small but statistically significant. The sampling of the configurational space in these systems with a smaller dipole moment is relatively easy. Careful inspection of Figure 4e reveals that small but statistically clear signs of domain formation are present also in the largest system (30 000 particles) with a dipole moment of 1.143 D. The simulation of this system is very easy.

(v) We have shown that for the type of structural ordering observed in this work there exist correlations in dipolar order on a length scale that is roughly twice the length on which the Kirkwood factor for the average dipole has converged. It is important to note that this applies to all the studied systems in this work where the dipole−dipole interaction between neighbors are larger than $kT$. For the smaller systems and for the systems with a dipole moment of 1.397 D there are no problems with the sampling, so the observation is general for dipolar particles in a droplet. If the structural order obtained using other boundary conditions shows the same behavior, we will have to reconsider the interpretation of data obtained from bulk simulations. Typically, in bulk simulations the observed Kirkwood factor has converged on a length scale that is half the distance from a central dipole to the boundary of the simulation box, or formulated differently one-quarter of the box length. We will study this issue in a future work.

(vi) The simulations performed on the system made from 30 000 particles with a dielectric boundary yielded similar structural data as was obtained with a vacuum surrounding.

(vii) The by far strongest argument in favor of that the found domains are real and not a function of nonequilibrium properties of the system is the large attractive energetic coupling between the different domains. This means that the used definition of the domain is meaningful. It is also hard to imagine that this long-range energetic coupling could be a consequence of nonequilibrium conditions.

(viii) There is an alternative way to analyze what has been done in this work. We have started by looking for regions with high dipolar order and in this way identified a set of dipoles that are the central particle in these domains. Typically these dipoles are located at least 40 Å from each other in the largest system studied. When we calculate the dipole−dipole interaction between these dipoles we find that it is always attractive and the angular part of this interaction is on average between −0.9 and −1.2. This is a very strong argument showing that long-range order exists in droplets made from particles with a large dipole moment.

### 5. Discussion

We have in the preceding section presented results obtained from droplet simulations of dipolar particles. We have seen that for dipolar particles for which the Clausius Mossotti equation (eq 1) can be used to calculate a meaningful dielectric permittivity, i.e., when $\mu^{2}/(4\pi\epsilon_{0}kTr^{3}) < 1$, where $r$ is the nearest neighbor distance between the dipoles, the droplet systems behaves as expected in that the dipolar structure is short-ranged and that the interaction between distant parts of the system is unimportant for the system behavior. However for larger dipole moments and larger droplets we see the formation of regions with enhanced dipolar order. The size of these regions grows with the size of the studied system. The orientations of different regions are strongly correlated, and the dipolar domains gain their stability partly from an attractive domain−domain interaction. For these systems one can truly say that the entire systems are strongly coupled. If the orientation of one dipole is changed, the entire system responds to this perturbation.

The observed domains may explain the very different results with respect to long-range dipolar order that are observed when the boundary conditions are changed in bulk simulations and that was noted above. It is obvious that the studied system must be much larger than the largest structures formed, in order that the modeling of a bulk system should be reliable. In fact, domain formation is the only explanation given so far for this observation.

It should be stressed that we have not shown the existence of domains in bulk liquids, only in droplets, but for the size of

droplets studied in this work the domains increase in importance (the domain−domain interaction gets larger (more negative)) with the droplet size.

Furthermore, we note that a dielectric surrounding hardly changes the formed domains at least if only the total dipole moment of the droplet is allowed to couple to the surrounding. We also note that clear signs of domain formation cannot be seen in systems containing 3000 particles or less, provided that the particle dipole moment is equal to or smaller than 1.651 D for particles with the size studied in this work.

The ferroelectric domains presented in this work challenge our present picture of dipolar order in polar solvents, and if they are considered together with the experimental observations made by Shelton, we are forced to consider the possibility of very long-range dipolar order and the formation of domains in dipolar liquids. In this work we have also shown a new principle, that is domain−domain interaction, for generating long-range dipolar order and that the dipolar order is more long-ranged than suggested by the standard Kirkwood factor. Roughly speaking, the correlations measured by $G_{\mathrm{K}}^{\mathrm{m}}$ are twice as long-ranged as the correlations seen in the Kirkwood factor for the average dipole. We have also observed that the size of ordered regions increases with system size. If this observation holds also in bulk systems, our view of polar liquids will change completely.

The main conclusion from this work is that there are still many unanswered questions concerning the properties and behavior of dipolar liquids.

Acknowledgment. This work was supported by the Swedish Research Council in general and in particular by the Linne' excellence project Organizing Molecular Matter.

### References and Notes

(1) Clausius, R. *Die Mechanische Wärmetheorie*; Friedrich Vieweg und Sohn: Braunschweig, 1879; Vol. II, p 62.
(2) Mossotti, O. F. *Bibl. Univ. Modena* **1847**, 6, 193.
(3) Langevin, P. *J. Phys.* **1905**, 4, 678.
(4) Onsager, L. *J. Am. Chem. Soc.* **1936**, 58, 1486.
(5) Nienhuis, G.; Deutch, J. M. *J. Chem. Phys.* **1971**, 55, 4213.
(6) Nienhuis, G.; Deutch, J. M. *J. Chem. Phys.* **1972**, 56, 235.
(7) Nienhuis, G.; Deutch, J. M. *J. Chem. Phys.* **1972**, 56, 1819.
(8) Wertheim, M. S. *Mol. Phys.* **1973**, 25, 211.
(9) Wertheim, M. S. *Mol. Phys.* **1973**, 26, 1425.
(10) Wertheim, M. S. *Mol. Phys.* **1977**, 33, 1109.
(11) Wertheim, M. S. *Annu. Rev. Phys. Chem.* **1979**, 30, 471.
(12) Shelton, D. P. *Phys. Rev. B* **2005**, 72, 020201.
(13) Shelton, D. P. *J. Chem. Phys.* **2002**, 117, 9374; *J. Chem. Phys.* **2004**, 121, 3349.
(14) Shelton, D. P. *Chem. Phys.* **2005**, 123, 084502; *J. Chem. Phys.* **2005**, 123, 111103.

(15) Ladd, A. J. C. *Mol. Phys.* **1977**, 33, 1039.
(16) Ladd, A. J. C. *Mol. Phys.* **1978**, 36, 463.
(17) Allen, M. P.; Tildesley, D. J. *Computer Simulations of Liquids*; Oxford University Press: Oxford, 1989; p 24.
(18) Ewald, P. *Ann. Phys.* **1921**, 64, 253.
(19) Frenkel, D.; Smit, B. *Understanding Molecular Simulation, From Algorithms to Applications*; Academic Press: San Diego, CA, 1996.
(20) Adams, D. J.; McDonald, I. R. *Mol. Phys.* **1976**, 32, 931.
(21) Neumann, M. *Mol. Phys.* **1983**, 50, 841.
(22) Levesque, D.; Patey, G. N.; Weis, J. J. *Mol. Phys.* **1977**, 34, 1077.
(23) Adams, D. J.; Adams, E. M.; Hills, G. J. *Mol. Phys.* **1979**, 38, 387.
(24) Adams, D. J. *Mol. Phys.* **1980**, 40, 1261.
(25) Adams, D. J. *Mol. Phys.* **1981**, 42, 907.
(26) Neumann, M.; Steinhauser, O.; Pawley, G. S. *Mol. Phys.* **1984**, 52, 97.
(27) Neumann, M. *Mol. Phys.* **1987**, 60, 225.
(28) Kusalik, P. G. *J. Chem. Phys.* **1990**, 93, 3520.
(29) Kusalik, P. G. *Mol. Phys.* **1991**, 73, 1349.
(30) Fröhlich, H. *Theory of Dielectrics*; Claradon Press: Oxford, 1949.
(31) Berendsen, H. J. C. *Molecular Dynamics and Monte Carlo Calculations on Water*; CECAM Report; Centre Europeen de Calcul Atomique et Moleculaire: Orsay, France, 1972.
(32) Powles, J. G.; Fowler, R. F.; Evans, W. A. B. *Chem. Phys. Lett.* **1984**, 107, 280.
(33) Senapati, S.; Chandra, A. *J. Phys. Chem. B* **2001**, 105, 5106.
(34) Groh, B.; Dietrich, S. *Phys. Rev. E* **1997**, 55, 2892.
(35) Groh, B.; Dietrich, S. *Phys. Rev. Lett.* **1997**, 79, 749.
(36) Groh, B.; Dietrich, S. *Phys. Rev. E* **1998**, 57, 4535.
(37) Kumar, P.; Franzese, G.; Buldyrev, S. V.; Stanley, H. E. *Phys. Rev. E* **2006**, 73, 041505.
(38) Kirkwood, J. G. *J. Chem. Phys.* **1939**, 7, 911.
(39) Israelachvili, J. N. *Intermolecular and Surface Forces*; Academic Press: San Diego, CA, 1996.
(40) Metropolis, N. A.; Rosenbluth, A. W.; Rosenbluth, N. M.; Teller, A.; Teller, E. *J. Chem. Phys.* **1953**, 21, 1087.
(41) The autocorrelation function for the total dipole moment of the droplet is defined through $\Phi(t) = \langle \underline{\mathbf{M}}(0) \cdot \underline{\mathbf{M}}(t) \rangle / \langle M^2 \rangle$, where $\underline{\mathbf{M}}(0)$ is the total dipole moment of the at the time $0$ (Monte Carlo step 0) and $\underline{\mathbf{M}}(t)$ is the total dipole moment after $t$ Monte Carlo steps. M is the length of the dipole moment vector. $\phi(t)$ is the autocorrelation function for the individual dipoles and is defined as the average value of the of $\phi_i(t) = \langle \underline{\mu}_i(0) \cdot \underline{\mu}_i(t) \rangle / \langle \mu^2 \rangle$, where $\underline{\mu}_i$ in a similar way is the dipole moment of dipole number $i$. The displacement of a particle from its position at time 0 can be calculated using Fick's law, $R^2 = 6Dt$, where $D$ is the diffusion constant and $t$ is the time. This means that if the average value of the displacement of the molecules is calculated as a function of the number of Monte Carlo steps/particle a straight line should be obtained in the limit of many Monte Carlo steps for a bulk system. For the droplet studied here we will anyway obtain a straight line since the displacement is small compared to the droplet dimension.
(42) Ballenegger, V.; Hansen, J.-P. *J. Chem. Phys.* **2005**, 122, 114711.
(43) Blaak, R.; Hansen, J.-P. *J. Chem. Phys.* **2006**, 124, 144714.
(44) Wang, Z.; Holm, C.; Muller, H. W. *J. Chem. Phys.* **2003**, 119, 379.
(45) There is a small difference between the average curve in Figure 5b and the curve describing the same system in Figure 4e. The origin of the difference is due to that the curve in Figure 4e is averaged over all equilibrated conformations, whereas the data presented in Figure 5, parts a and b, are sampled over a smaller subset.