# Thermodynamics and the structure of clusters in the dense Au vapor from molecular dynamics simulation

Cite as: J. Chem. Phys. 152, 224705 (2020); https://doi.org/10.1063/5.0010156
Submitted: 07 April 2020 . Accepted: 26 May 2020 . Published Online: 09 June 2020

D. I. Zhukhovitskii, and V. V. Zhakhovsky

![](./images/812601548793184256_1.jpg)
![](./images/812601548793184256_2.jpg)
![](./images/812601548793184256_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

How different are the dynamics of nanoconfined water?
The Journal of Chemical Physics 152, 224707 (2020); https://doi.org/10.1063/5.0010613

Optimized utilization of COMB3 reactive potentials in LAMMPS
The Journal of Chemical Physics 152, 224702 (2020); https://doi.org/10.1063/5.0009011

Non-Boltzmann vibrational energy distributions and coupling to dissociation rate
The Journal of Chemical Physics 152, 224301 (2020); https://doi.org/10.1063/1.5142732

![](./images/812601548793184256_4.jpg)

J. Chem. Phys. 152, 224705 (2020); https://doi.org/10.1063/5.0010156
© 2020 Author(s).
152, 224705

# Thermodynamics and the structure of clusters in the dense Au vapor from molecular dynamics simulation

Cite as: J. Chem. Phys. 152, 224705 (2020); doi: 10.1063/5.0010156
Submitted: 7 April 2020 • Accepted: 26 May 2020 •
Published Online: 9 June 2020

![](./images/812601548793184256_5.jpg) ![](./images/812601548793184256_6.jpg) ![](./images/812601548793184256_7.jpg)

D. I. Zhukhovitskii $^{a)}$ and V. V. Zhakhovsky $^{1,2}$

## AFFILIATIONS
$^{1}$Joint Institute of High Temperatures, Russian Academy of Sciences, Izhorskaya 13, Bd. 2, 125412 Moscow, Russia
$^{2}$Dukhov Research Institute of Automatics, 22 Sushchevskaya St., 127055 Moscow, Russia

$^{a)}$Author to whom correspondence should be addressed: dmr@ihed.ras.ru

## ABSTRACT
Clusters of atoms in dense gold vapor are studied via atomistic simulation with the classical molecular dynamics method. For this purpose, we develop a new embedded atom model potential applicable to the lightest gold clusters and to the bulk gold. Simulation provides the equilibrium vapor phases at several subcritical temperatures, in which the clusters comprising up to 26 atoms are detected and analyzed. The cluster size distributions are found to match both the two-parameter model and the classical nucleation theory with the Tolman correction. For the gold liquid-vapor interface, the ratio of the Tolman length to the radius of a molecular cell in the liquid amounts to ~0.16, almost exactly the value at which both models are identical. It is demonstrated that the lightest clusters have the chain-like structure, which is close to the freely jointed chain. Thus, the smallest clusters can be treated as the quasi-fractals with the fractal dimensionality close to two. Our analysis indicates that the cluster structural transition from the solid-like to chain-like geometry occurs in a wide temperature range around 2500 K.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0010156

## I. INTRODUCTION
Metal clusters are a subject of extensive research due to their numerous important applications. Among the most interesting objects are the gold clusters due to their key role in nanoscale electronics and optical and medical diagnostic devices. Metallic bonds of atoms comprising such clusters stipulate their peculiarities that are extensively studied both experimentally and theoretically. $^{1,2}$ The ground-state configurations and binding energies of metal clusters at zero temperature are calculated on the basis of density functional theory (DFT), which is commonly used for bulk metals. Nevertheless, extensions of DFT applicable to the nanoscale objects are developed. $^{3-9}$ Alternative jellium models of small metal clusters are proposed as well. $^{10,11}$

Metal clusters can be produced by nucleation in expanding metal vapor, which is typically formed in the laser-induced vaporization $^{12,13}$ and ablation of metals into vacuum $^{14,15}$ and liquids. $^{16,17}$ Since the vapor temperature in such high-power processes is initially well above the melting point and it drops rapidly below the critical temperature, the "hot" clusters of different sizes are produced and can grow up to the nanometer-sized particles. Because the cluster energy, geometry, and size distribution at several thousand K are difficult to obtain via experiment, the atomistic simulation of such clusters is urgent. This includes studying the kinetic processes involving cluster formation in the metal vapor $^{18,19}$ and the cluster thermodynamic properties. $^{20-22}$ Note that both cluster kinetics and thermodynamics are essential for the nucleation theory.

We are focusing on the equilibrium clusters present in sufficiently dense subcritical vapor near the saturation line. The fraction of clusters in such vapor must be sufficient for their analysis based on the classical molecular dynamics (MD) simulation. Moreover, the thermodynamic properties of the vapor with clusters are typically defined by the clusters comprising up to tens of atoms. A good approximation for the dense vapors is the model of an ideal mixture of clusters (see Ref. 23 and references therein). Clusters in the equilibrium and supersaturated dense argon-like vapor at constant pressure and temperature were extensively studied (see,

e.g., Refs. 24–26). It was found that the lightest argon-like clusters interacting via the Lennard-Jones pair additive potential have the structure of intersecting chains, and this made it possible to estimate their partition function within the framework of virtual chain approximation²⁵ and to find the chemical potential for the cluster comprising arbitrary number of atoms up to the macroscopic droplet on the basis of the two-parameter model (TPM). The latter suggests that the cluster chemical potential is a linear function of the numbers of core and surface atoms in a cluster.²⁶,²⁷ However, to the best of our knowledge, no systematic study of dense metal vapors and the cluster structure can be found in the literature.

The objective of this work is to investigate the dense gold vapor and the equilibrium clusters present in it, as gold is among the most demanded metals in production of nanoparticles and other applications. We perform both the MD simulation of the dense gold vapor in the phase states close to the saturation line in the temperature range from 4000 K to 6000 K and the model analysis of such a system. To observe the clusters comprising 2 to ~30 atoms, one has to simulate a MD system of about $10^6$ particles. Since an appropriate interatomic potential is required for realistic simulation of gold vapor, a new embedded atom model (EAM) potential was developed. Note that MD simulation of gold clusters using another EAM potential was performed in recent studies.¹⁸,¹⁹ In accordance with TPM, an appropriate EAM potential that is capable of describing metal clusters of arbitrary sizes must result in the experimental dimer binding energy and the surface tension, in addition to other properties of a bulk metal. Thus, it is essential to have those data in the EAM fitting database.

MD simulation of dense gold vapor enables the cluster size distribution to be calculated and then to be compared with the known results obtained with the cluster models. Surprisingly, a very good agreement between the cluster size distributions from MD, TPM, and the classical liquid drop model (LDM) with the Tolman correction points to the fact that the Tolman length must be relatively small and positive for gold, and it is very close to the particular Tolman length at which TPM and LDM almost coincide. A comparison between calculations and experimental $pVT$ data for the dense gold vapor justifies applicability of the developed EAM potential and consistency of MD results with those obtained from the cluster models and the model of ideal cluster mixture.

Detailed information on clusters from MD simulation suggests the next step, at which the structure of the lightest clusters is under investigation. The most vital question is whether metal clusters with the bond type entirely different from that of the argon-like clusters can exist in chain-like configurations. For the multi-body interaction between atoms in metals, which leads to sharp saturation of the binding energy per atom with the increasing number of cluster atoms, it is reasonable to introduce a special characteristic of the cluster structure determined as an ensemble-averaged ratio of the maximum to average distance between the atoms pertaining to the same cluster. This structure parameter as a function of the cluster size is an effective characteristic for the lightest clusters, which are, on average, sufficiently homogeneous in space. A comparison between the structure parameters calculated for the clusters and for different structures with the known fractal dimensionality that comprise the same number of atoms (linear chain, freely jointed chain, and a solid sphere) is a way to estimate the cluster fractal dimensionality. Because the clusters are the finite-size objects, they can only be treated as the fractal fragments or quasi-fractals.

Our analysis shows that the fraction of chain-like cluster configurations as compared to the solid-like (compact) ones is superior for the lightest clusters comprising less than ten atoms at temperatures higher than 4000 K. Thus, with respect to the fractal structure, there is no principal difference between gold and Lennard-Jones clusters. As for the heavier gold clusters, such fraction is no good characteristic because of their solid core that breaks the cluster spatial homogeneity. Existence of chain-like gold clusters in the vapor can be illustrated by the bond-length distribution function (BDF) calculated for different cluster sizes: for the lightest clusters at higher temperatures, the second BDF maximum is almost extinct, which is typical for the chain structure.

The chain-like structure that can be observed at high temperatures changes to the solid-like one as the temperature decreases. Therefore, a structural transition between these two structures takes place in some temperature range, where a competition occurs between the cluster potential energy and the accessible phase space volume (entropy). The estimates of changes in these characteristics, as the structure passes from the chain-like to solid-like one, performed in the way similar to that discussed in Refs. 23 and 25 lead to the conclusion that the transition temperature for gold vapor must be noticeably higher than the gold melting temperature and can be roughly estimated as 3000 K. In contrast, for the argon-like clusters, the transition temperature is appreciably lower than the temperature of solid melting.

The paper is organized as follows. In Sec. II, the procedure of MD simulation and the main results are briefly discussed. Section III is devoted to a theoretical background: the virtual chain approximation and TPM are discussed, and the resulting vapor compressibility factor and the Tolman length for liquid gold are estimated. In addition, it is established that for the obtained Tolman length, TPM is almost identical to LDM. In Sec. IV, the cluster fractal structure and the structural transition are discussed. The main results of our work are summarized in Sec. V. In the Appendix, development of the new EAM potential is discussed in detail.

## II. MOLECULAR DYNAMICS SIMULATION

In this section, we will treat the equilibrium dense gold vapor in the subcritical region at temperatures well above the gold melting temperature. Our objective is to investigate the clusters present in the vapor and their effect on the vapor non-ideality. To accurately describe this system, our MD simulations employ a new interatomic potential for Au using EAM. This potential is an advanced revision of Au EAM potential developed in Ref. 28 using the stress-matching method. In addition to the bulk properties of solid gold, including cold stress tensor components, the surface tension of molten gold and the energy of the dimer cluster were included in the fitting database (see details in the Appendix). The EAM potential we use does not include an explicit angular-dependent part, and therefore, it cannot take into account the electron spin-orbit effect. However, it is clearly seen from Table III that the difference between the EAM calculation and the DFT calculation that includes this effect is noticeably smaller than the temperature (~0.5 eV) that we prescribe to the treated system. The energy difference between EAM and different

DFT versions is on the same order of magnitude as that between different DFT versions, and all these differences do not exceed the system temperature. Thus, one can conclude that the EAM potential we have developed can provide a sufficient accuracy for treatment of dense metal cluster vapors at temperatures well above the melting point.

All MD simulations are performed with our in-house parallel code MD-VD³ utilizing the Voronoi dynamic domain decomposi-tion.²⁹,³⁰ Atoms of the gas are placed in the MD cubic box with the dimensions $L_x = L_y = L_z$, and the periodic boundary conditions are imposed along all three dimensions. Initially, a single crystal sample with the gas density a few percents less than the equilibrium vapor density on the liquid-vapor binodal line $T_s(\rho)$ at a given temperature is generated to ensure that this gas is not supersaturated. Such a precaution is required because the saturated vapor density presented in the Appendix was calculated with an accuracy of 1% or better.

Then, this sample is thermalized at the chosen temperature using the Langevin thermostat during a time long enough to reach an almost equilibrium state. At the next stage, the NVE simulation without a thermostat is performed until the equilibrium cluster distribution is established. During this stage, the temperature grows slowly by a few degrees while the potential energy drifts down until it reaches a plateau. After this stage, the final production simulations are performed during several tens of nanoseconds with the gas parameters listed in Table I. During the simulation time $t_{\text{sim}}$, all atom coordinates and momenta are saved each 19.2 ps for further cluster analysis. Such time frame separation is sufficiently long to ensure statistical independence of the saved data for each atom.

For each time frame, we perform the cluster analysis of the vapor, which enables one to isolate individual clusters. We used the Stillinger definition of a cluster³¹ according to which an atom pertains to the cluster if it has at least one neighbor atom at the distance less than $r_b$ pertaining to the same cluster. Hereafter, the number of such atoms $k$ defines the cluster size. It was demonstrated in Ref. 32 that there exists some range of $r_b$, in which the cluster size is almost independent of $r_b$. In this simulation, we set $r_b = 0.4057$ nm, thus providing a reliable cluster definition. Typical configurations of the detected clusters are shown in Figs. 1 and 2. The diameter of circles representing atoms corresponds to the interatomic spacing in the gold fcc lattice at $T = 0$ calculated using the EAM potential developed in this work. For each atom, the coordination number is defined as the number of its nearest neighbors within a sphere of the radius $1.11r_b$ that demonstrates, most vividly, the peculiarities of different cluster configurations. It is seen that for $k = 7$, two different configurations occur in the vapor, the chain-like and the compact one. The coordination numbers for the cluster (a) are low with two one-neighbor atoms at the cluster end points, which is typical for the chain-like structure, while for the cluster (b), such atoms are absent, and the coordination numbers are noticeably greater. This is indicative of the fact that the lightest clusters, which can undergo the structural transition from solid-like

<table>
<caption>TABLE I. MD simulation parameters: temperature $T$, pressure $p$, total atom number density $n$, number of atoms $N_a$, cubic box dimension, and simulation time $t_{\text{sim}}$.
</caption>
<thead>
  <tr>
    <th>$T$ (K)</th>
    <th>$p$ (MPa)</th>
    <th>$n$ (nm⁻³)</th>
    <th>$N_a$</th>
    <th>$L_x$ (nm)</th>
    <th>$t_{\text{sim}}$ (ns)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>4006</td>
    <td>0.465</td>
    <td>0.008 97</td>
    <td>415 292</td>
    <td>359</td>
    <td>86.6</td>
  </tr>
  <tr>
    <td>5005</td>
    <td>3.899</td>
    <td>0.064 9</td>
    <td>530 604</td>
    <td>201</td>
    <td>68.6</td>
  </tr>
  <tr>
    <td>6004</td>
    <td>16.16</td>
    <td>0.250</td>
    <td>442 368</td>
    <td>121</td>
    <td>68.9</td>
  </tr>
</tbody>
</table>

<bbox>566  108 878 350</bbox>

FIG. 1. Typical configurations of the lighter clusters ($k = 7$) at $T = 6004$ K in (a) the chain-like and (b) the solid-like states. The atom coordination number is color-coded (see legend). The circle diameter is 0.287 nm.

![](./images/812601548793184256_8.jpg)

FIG. 2. Typical configurations of the heavier clusters at $T = 6004$ K, (a) $k = 16$ and (b) $k = 26$. The atom coordination number is color-coded (see the legend). The circle diameter is 0.287 nm.

to chain-like configurations (see Sec. IV), are on the average in some mixed configurational state. Instead, the heavier clusters, $k = 16$ and $k = 26$, seem to occupy similar configurational states, which are neither chain-like nor solid-like. Note that the coordination numbers are greater near the centers of these clusters. Such shapeless configurations are similar to those observed for the Lennard-Jones clusters. $^{24}$

We have analyzed about 3000 time frames for each set of the state parameters corresponding to three temperatures. This provides sufficient statistics to estimate the number densities of the clusters of different sizes $n_k$, i.e., the cluster size distributions (Fig. 3). It is seen that $n_k$ increases sharply with temperature. The fraction of atoms bound in the clusters is high enough to have an effect on the vapor non-ideality or on the compressibility factor $Z$ (Fig. 4). It is of interest to compare $Z = p_sM/\rho_sT$ calculated from the MD simulation $pVT$ data for a two-phase system with that obtained from the cluster model of a dense vapor. This model implies that the nonideal vapor can be treated as an ideal mixture of clusters. $^{23,26}$ Hence, in this model, the vapor non-ideality is reduced to the formation of the clusters, and the vapor compressibility factor,

$$
Z = \sum_{k=1}^{\infty} n_k \left( \sum_{k=1}^{\infty} k n_k \right)^{-1}, \tag{1}
$$

is always less than unity. Figure 4 shows such a comparison. Calculation of the compressibility factor based on the cluster number densities determined from MD simulation and formula (1) is in a close agreement with the direct calculation of $Z$. To make sure that the proposed model can be applied for real dense gold vapor, one has to compare the obtained results with experiment. In view of the fact that there exist no data on the cluster composition of gold vapor, we can only use the $pVT$ data based on the wide-range equation of state (EoS). $^{33-36}$ A satisfactory agreement between the compressibility factor from both sets of MD data and the $pVT$ data $^{33-36}$ from the wide-range EoS suggests adequacy of such an approach.

![](./images/812601548793184256_9.jpg)

FIG. 3. Number densities of clusters in the vapor as a function of the cluster size for $T = 4006$ K (blue lines and circles), 5005 K (green lines and squares), and 6004 K (red lines and triangles). Solid lines indicate calculation using TPM and dashed lines, LDM; dots represent the results from MD simulation.

![](./images/812601548793184256_10.jpg)

FIG. 4. Compressibility factor of gold vapor at the saturation line as a function of temperature from MD simulation of the vapor and formula (11) (circles) and from MD simulation of a two-phase system (solid line). Calculation using (15) is shown by a dashed line; the dotted-dashed line indicates the equation of state (16). $pVT$ data taken from the wide-range EoS $^{33}$ are shown by the dotted line.

## III. CLUSTER SIZE DISTRIBUTION AND THE TOLMAN LENGTH

### A. Virtual chain approximation and the cluster partition function

To provide a theoretical interpretation of the cluster size distributions obtained from MD simulation, we will discuss the virtual chain approximation of the smallest clusters that are formed at equilibrium in the dense vapor in the subcritical region. Consider a small cluster of the size $k$. As its temperature is increased, its entropy increases. The latter depends sensitively on the cluster structure, namely, on the fractal dimension one can prescribe to a cluster of a certain size because it defines the phase space volume accessible for the cluster atoms. Thus, for the freely jointed chain in 3D space (fractal dimension $D_f = 2$), the accessible volume is superior to that for the crystal-like cluster ($D_f = 3$), although its potential energy is lower than that for the cluster with the structure close to the freely jointed chain. At sufficiently high temperature, the gain in the cluster entropy as it passes from the $D_f = 3$ to $D_f = 2$ structure can compete with the loss in its potential energy. Thus, the structural transition occurs, which takes place in a finite temperature range since the cluster is a finite object. $^{25}$

Transition to the chain-like structure suggests that the number of bonds is close to its minimum, i.e., one can treat the cluster as a set of intersecting chains with the minimum number of bonds $k - 1$. Obviously, this model is limited by the cluster size; in fact, $k \lesssim 10$.

In this approximation, the cluster partition function,
$$
Z_{c}^{(k)}=\frac{1}{\lambda^{3 k}} \int \cdots \int^{\prime} \exp \left[-\frac{U\left(\mathbf{r}_{1}, \mathbf{r}_{2}, \ldots, \mathbf{r}_{k}\right)}{T}\right] d \mathbf{r}_{1} \ldots d \mathbf{r}_{k}, \quad(2)
$$
where $\lambda=(2 \pi \hbar^{2} / M T)^{1 / 2}$ is the atom thermal wavelength, $\hbar$ is the Planck constant, $M$ is the atom mass, $T$ is the temperature in the energy units (Boltzmann's constant is set to unity), $U(\mathbf{r}_{1}, \mathbf{r}_{2}, \ldots, \mathbf{r}_{k})$ is the potential energy of a cluster, $\mathbf{r}_{1}, \mathbf{r}_{2}, \ldots, \mathbf{r}_{k}$ are the radius-vectors of atoms, and the primed integrals exclude identical states from the integration space, is factorized: $^{25}$
$$
\begin{aligned}
Z_{c}^{(k)} & =\frac{V}{\lambda^{3 k}} \int \cdots \int^{\prime} \prod_{i=1}^{k-1} \exp \left[-\frac{u\left(r_{i}\right)}{T}\right] d \mathbf{r}_{1} \ldots d \mathbf{r}_{k-1} \\
& =\frac{V}{\lambda^{3 k}}\left\{\int^{\prime} \exp \left[-\frac{u\left(r_{1}\right)}{T}\right] d \mathbf{r}_{1}\right\}^{k-1} \\
& =\frac{V}{\lambda^{3 k}}\left[Z_{2} \exp \left(-\frac{D}{T}\right)\right]^{k-1},
\end{aligned}
$$
where $V$ is the system volume, $u(r)$ is the interatomic potential, which is assumed to be the pair, additive, and short-range one, $D$ is the dimer binding energy, and $Z_{2}$ is the internal partition function of a dimer,
$$
Z_{2}=\exp \left(\frac{D}{T}\right) \int^{\prime} \exp \left[-\frac{u\left(r_{1}\right)}{T}\right] d \mathbf{r}_{1}. \quad(4)
$$

Then, the cluster chemical potential $\mu_{k}$ in the vapor, which is assumed to be an ideal mixture of atoms and clusters of different sizes, is represented in the following form:
$$
\frac{\mu_{k}}{T}=\ln \left(n_{k} V\right)-\ln Z_{c}^{(k)}=\ln \left(n_{k} \lambda^{3}\right)+(k-1) \ln \left(K_{2} \lambda^{3}\right), \quad(5)
$$
where $n_{k}$ is the number density of clusters of the size $k$ and
$$
K_{2}(T) \equiv \frac{n_{1}^{2}}{n_{2}}=\frac{1}{\lambda^{3} Z_{2}} \exp \left(-\frac{D}{T}\right) \quad(6)
$$
is the equilibrium constant of the reaction of dimer formation.

We use the mass action law for the reaction of cluster formation in the vapor $\mu_{k}=k \mu_{1}$, where $\mu_{1}=T \ln \left(n_{1} \lambda^{3}\right)$ is the chemical potential of an atom, and (5) to derive the equilibrium cluster distribution over sizes $n_{k}=n_{1}^{k} K_{2}^{1-k}$, which can be rewritten as follows:
$$
n_{k}=n_{1} \exp \left(-\frac{\Delta \Phi_{k}}{T}\right), \quad(7)
$$
where
$$
\Delta \Phi_{k}=(1-k) T\left(\ln \frac{n_{1 s}}{K_{2}}+\ln S\right) \quad(8)
$$
is the work of formation for the cluster of the size $k, S=n_{1} / n_{1 s}$, and $n_{1 s}$ is the number density of monomers at the binodal (at saturation line). $^{26}$ In what follows, we will denote the quantities at the saturation line by the subscript $s$. Alternatively, distributions (7) and (8) can be deduced from the assumption concerning the linear dependence of $\mu_{k}$ on $k:^{23,27} \mu_{k}=T \ln p_{k}+\zeta_{k}(T)$ and $\zeta_{k}(T)=A(T) k+B(T)$, where $p_{k}=n_{k} T$ is the partial pressure of clusters of the size $k$, and $\zeta_{k}(T), A(T)$, and $B(T)$ are functions of the temperature. This model does not require that the interatomic potential be pair additive, i.e., it can be applied for metal clusters, albeit it is rigorously justified solely for pair additive short-range potentials at sufficiently high temperature. Our MD simulation makes it possible to check if the virtual chain approximation (3) is reasonable for gold clusters at sufficiently high temperatures when the chain-like cluster structure dominates over the solid-like one.

In the opposite limit of a large cluster, the latter is a macroscopic droplet whose work of formation is given by the classical nucleation theory (CNT), $^{37-39}$
$$
\Delta \Phi_{k}=4 \pi \sigma r_{\ell}^{2} k^{2 / 3}-(k-1) T \ln S, \quad(9)
$$
where $\sigma$ is the surface tension of a flat liquid-vapor interface, $r_{\ell}=(3 / 4 \pi n_{\ell})^{1 / 3}$ is the radius of a molecular cell in the liquid, and $n_{\ell}$ is the atom number density in a liquid phase. A simple approximation, the TPM, unifies (8) and (9), $^{26,27}$
$$
\Delta \Phi_{k}=4 \pi \sigma r_{\ell}^{2} \gamma(k) k^{2 / 3}-(k-1) T \ln S, \quad(10)
$$
where $\sigma \gamma(k)$ is the size-dependent cluster surface tension, $\gamma=(2 / 3)(\lambda$ $+2 \delta)^{-1}(k_{0}-1) k^{-2 / 3}$, and $k_{0}(k)$ is the root of the equation,
$$
k_{0}=\frac{1}{2}(\lambda+2 \delta)\left[3\left(k-k_{0}\right)^{2 / 3}+3 \lambda\left(k-k_{0}\right)^{1 / 3}+\lambda^{2}\right] \quad(11)
$$
if $k \geq(\lambda^{2} / 2)(\lambda+2 \delta)$ and $k_{0}=k$ if $k \leq \max \{(\lambda^{2} / 2)(\lambda+2 \delta), 2\}$. Here, two parameters are introduced, namely, the reduced Tolman length $\delta=l_{T}/r_{\ell}$, where $l_{T}$ is the Tolman length, and the reduced width $\lambda=l_{s}/r_{\ell}$, where $l_{s}$ is the width of the cluster surface layer. The parameters $\delta$ and $\lambda$ conform to the relationship $^{27}$
$$
\delta+\frac{\lambda}{2}=-\frac{4 \pi}{3} \frac{\sigma r_{\ell}^{2}}{T \ln \frac{n_{1 s}}{K_{2}}} \quad(12)
$$
that relates these parameters to the properties of a macroscopic substance and to that of a dimer. Equations (10) and (11) are indeed equivalent to the assumption that a cluster can be represented as a core of the internal atoms surrounded by a layer of the surface atoms whose width is independent of the cluster size. $^{27}$

In the CNT, the clusters are prescribed the properties of a macroscopic liquid droplet such as the density and surface tension. In the most advanced self-consistent version of CNT, $^{40}$ a correction factor is introduced that normalizes the cluster distribution to the monomer number density at $k=1$. If the Tolman correction for the size dependence of the surface tension $^{41}$ is properly taken into account, then the work of cluster formation (9) can be written as follows:
$$
\Delta \Phi_{k}=4 \pi \sigma r_{\ell}^{2} \bar{\gamma}(k) k^{2 / 3}-(k-1) T \ln S, \quad(13)
$$
where $\bar{\gamma}(k)=k^{-2 / 3}(k^{2 / 3}-1)(1-2 \delta k^{-1 / 3})$ is the Tolman size correction factor. In what follows, we will term (13) the LDM. Note that this expression is fully compatible with the Gibbs-Tolman thermodynamics of a curved liquid-vapor interface. $^{42}$ A question arises if there exist such $\delta$ and $\lambda$ that LDM is most effective in a wide range of the cluster sizes including the smallest ones. In other terms, when

are small clusters almost "classical" or when are they very close to the macroscopic droplets in their thermodynamic properties? If this is the case, TPM (10) and (11) and LDM (13) are not different, i.e., the equality $\gamma(k)=\bar{\gamma}(k)$ must hold. For different $k$ s, this equality defines a family of curves in Fig. 5. As is seen, at $\lambda>1.1$, the curves almost coincide, i.e., the relation $\gamma(k) \simeq \bar{\gamma}(k)$ is satisfied for the smallest sizes irrespective of $k$. To ensure consistency of this relation in the range of large $k$, we adopt the relation $^{26}$

$$
\frac{5}{4} \lambda^{2}=12 \delta^{2}+\frac{2}{\lambda+2 \delta}, \quad(14)
$$

that ensures identity of the works of the critical cluster formation in the supersaturated vapor (at $S>1$ ) calculated within the TPM and LDM approaches. Relation (14) means that the second-order term of the expansion of the work of formation in inverse powers of the cubic root of the critical cluster size vanishes. The cross at the curve $k=2$ whose coordinates $\lambda=1.15$ and $\delta=0.157$ satisfy (14) indicates a special pair of parameters for which TPM and LDM must yield the same results in a wide range of the cluster sizes from two to infinity. Thus, from comparison between TPM and LDM, one can conclude that for very small cluster sizes, the Tolman size correction is valid solely for $\delta=0.157$, and such Tolman reduced length is indica- tive of the fact that clusters can be treated as almost classical liquid droplets.

In the above-discussed model, the most "classical" cluster is associated with the formation of the core at a minimum cluster size. We estimate crudely the minimum threshold of the core formation as $(\lambda^{2} / 2)(\lambda+2 \delta)=1$. Then, we borrow a value $(\lambda+2 \delta) / 2 \simeq 0.8$ typical for most substances from Ref. 27 to derive $\lambda \simeq 1.12$, which matches closely the cross in Fig. 5.

![](./images/812601548793184256_11.jpg)

FIG. 5. Curves along which the equality $\gamma(k)=\bar{\gamma}(k)$ holds for $k=2$ (solid line), 3 (dashed line), and 5 (dotted line). Dots represent the best fit of Eqs. (10) and (11) to the cluster size distribution from MD simulation for gold at $T=4006 ~K$ (diamond),5000 K (square), and 6004 K (circle); see Table II. Cross indicates the point at the curve $k=2$ at which condition (14) is satisfied, i.e., the clusters are almost classical in the entire size range.

### B. Model compressibility factor

Based on the cluster size distributions (7), (10), and (11), one can calculate the vapor compressibility factor. If we use the model of an ideal mixture of clusters, Eq. (1) can be re-written in the following form: $^{23}$

$$
Z=\left[\sum_{k=1}^{\infty} S^{k-1}\left(\frac{p_{1 s}}{K_{2}}\right)^{k_{0}(k)-1}\right]\left[\sum_{k=1}^{\infty} k S^{k-1}\left(\frac{p_{1 s}}{K_{2}}\right)^{k_{0}(k)-1}\right]^{-1}, \quad(15)
$$

where $S=p_{1} / p_{1 s}$. If we assume that solely the lightest clusters with $k \lesssim 10$ contribute to the compressibility factor, then their size distri- bution can be approximated by Eqs. (7) and (8). This yields a simple equation of state, $^{23,27}$

$$
Z=\frac{1}{1+p K_{2}^{-1}}, \quad(16)
$$

where $p$ is the total vapor pressure.

The vapor density $\rho_{s}$ and pressure $p_{s}$ for a relatively small liquid-vapor equilibrium system at fixed temperature $T_{s}$ are obtained along a saturation line from several MD simulations. To maximize the number of atoms in the gaseous phase at a given tem- perature, which is necessary to broaden the range of detectable clus- ter sizes, we performed another set of large-scale single-phase MD simulations. To avoid simulation of supersaturated vapor at some fixed $T_{s}$, an equilibrium system was generated with the prescribed vapor density $\rho<\rho_{s}$ and pressure $p<p_{s}(T_{s})$ slightly below the satu ration line. From the data of this simulation set, the cluster number densities $n_{k}$ and their partial pressures $p_{k}$ are determined, which makes it possible to calculate, in particular, the equilibrium constant $K_{2}=n_{1}^{2} / n_{2}$. However, the monomer pressure $p_{1 s}$ is still unknown. Since $\rho_{s}=M \sum_{k=1}^{\infty} k n_{k s}$, it can be found from the transcendental equation,

$$
p_{1 s}=\frac{T \rho_{s}}{M}\left[\sum_{k=1}^{\infty} k\left(\frac{p_{1 s}}{K_{2}}\right)^{k_{0}(k)-1}\right]^{-1}. \quad(17)
$$

Then, we can determine the parameters $\delta$ and $\lambda$ when fitting the clus- ter distribution over sizes $n_{k}$ from MD simulation by the TPM (7),(10), and (11) with $p_{1 s}$ found from (17). The obtained results allow one to compare the compressibility factor (1) from MD simulation with that from the theory [Eqs. (15) and (16)].

We applied the above-discussed procedure to determine both the parameters $\delta$ and $\lambda$ and the ratio $S$. With due regard to relation(12), $\delta$ is a single parameter that fits the theoretical size distribution to that obtained from MD data. In so doing, we used the satura- tion vapor pressure, density and the surface tension calculated in our two-phase MD simulations; $K_{2}=n_{1}^{2} / n_{2}$ was estimated using the monomer and dimer number densities from our vapor MD sim- ulation. The obtained results are collected in Table II. With such parameters, the cluster size distribution from TPM is in a satisfac- tory agreement with the MD simulation results (Fig. 3). Here, we used Eq. (11) in the entire range $1<k \leq 26$ to smoothen the curve. It is noteworthy that LDM can be scarcely distinguished from TPM. The reason for this coincidence is the values of $\delta$ and $\lambda$ that lie in the vicinity of the curves of identity of TPM and LDM in Fig. 5. At T = 4006 K, this pair of parameters lie very close to a point of such an

<table><caption>TABLE II. Reduced parameters $\delta$ and $\lambda$ and the ratio $S$ for gold vapor at different temperatures $T$ from MD simulation.</caption>
<tbody><tr><td>$T$ (K)</td><td>$\delta$</td><td>$\lambda$</td><td>$S$</td></tr>
<tr><td>4006</td><td>0.1675</td><td>1.0877</td><td>0.9576</td></tr>
<tr><td>5005</td><td>0.1335</td><td>0.9517</td><td>0.9910</td></tr>
<tr><td>6004</td><td>0.1317</td><td>0.7125</td><td>1.000</td></tr>
</tbody></table>

identity at arbitrary $k$. Apparently, the visible disagreement between the simulation and theory in Fig. 3 and the dispersion of $\delta$-$\lambda$ points in Fig. 5 at $T = 6004$ K seems to arise both from the worse applicability of the "core + surface layer" model discussed in Sec. III A and from cluster mixture nonideality ignored in the ideal cluster mixture model. Hence, the accuracy of the theory decreases with the increase in temperature. Nevertheless, one can conclude that gold clusters seem to be fully classical in the entire range of their sizes. This "classical" behavior of light clusters ($\delta \sim 0.1$), which is not typical for, e.g., the Lennard-Jones clusters, is the result of a fast saturation of the atom binding energy specific for metals. Thus, similar behavior and the close Tolman lengths could be expected for most normal metals.

The theoretical equations of state are compared with those from our MD simulation and with the wide-range EoS$^{33}$ in Fig. 4. It is seen that Eq. (16) yields greater $Z$ than the TPM model (15) and overestimates $Z$ as it must because in this approximation, larger clusters are ignored. However, in the limited temperature range, it can provide a satisfactory accuracy. An agreement between the compressibility factor from MD simulation, the model calculation using TPM, and the $pVT$ data from the wide-range EoS$^{33}$ indicates that the proposed model represents the dense gold vapor adequately. Moreover, this model can be applied for nonequilibrium phenomena that depend sensitively on the properties of light clusters such as the vapor nucleation.

## IV. STRUCTURE OF THE LIGHTEST CLUSTERS

### A. Assessment of the structural transition temperature

According to the discussion in Sec. III A, the structure of the smallest clusters becomes chain-like (correspondingly, the TPM model is valid) at sufficiently high temperature. This transition temperature was estimated for the pair additive short-range potential in Ref. 25 and for the saturated many-body potentials typical for metals, in Ref. 23. It was shown that the ratio of the probabilities $P_{\text{ch}}$ and $P_{\text{sol}}$ to find a light cluster in the chain-like and in the solid-like state, respectively, is equal to the ratio of cluster partition functions in the corresponding states. The transition temperature $T_0$ can be estimated from the condition $P_{\text{ch}} = P_{\text{sol}}$. Simple estimates of the partition functions for the lightest clusters in the solid-like and chain-like states make it possible to write this condition in the following form:$^{23}$

$$
\exp(\tau) = \frac{\tau}{\varepsilon}\left(\frac{a}{r_0}\right)^2, \tag{18}
$$

where $\tau = 2\varepsilon D/T_0$, $\varepsilon = \lim_{k \to \infty} [\Delta E_k/(2k - 5)D]$, $\Delta E_k = E_{\text{ch}} - E_{\text{sol}}$ is the potential energy difference between the chain-like and the solid-like state energy, $a$ is the distance between dimer atoms at equilibrium, and $r_0$ is the half-width of the potential well. Equation (18) is valid for a short-range potential (not necessarily a pair additive one), for which $(a/r_0)^2 \gg 1$.

We have simulated the ground state potential energies of the gold clusters at zero temperature using the EAM potential discussed in Sec. III A. The energy of linear cluster configurations conform approximately to the linear dependence $E_{\text{ch}} = (1 - k)D$, where $D = 2.25$ eV (energy per bond $E_{\text{ch}}/(1 - k) \simeq 2$ eV). The energies per atom of solid-like clusters saturate and reach $q = 3.97$ eV as $k \to \infty$, so in this limit, $E_{\text{sol}} = (1 - k)q$. Thus, we arrive at the following estimation:

$$
\varepsilon = \frac{1}{2}\left(\frac{q}{D} - 1\right). \tag{19}
$$

For gold and used EAM potential, $\varepsilon = 0.382$.

To estimate $a/r_0$, we approximate the EAM potential $u(r)$ calculated for a pair of atoms (Fig. 6) by the parabolic potential $\bar{u}(r)$ with the hard core $a - r_0$ and the cutoff distance $a + r_0$ defined as follows: $\bar{u}(r) = \infty$ if $r < a - r_0$, $\bar{u}(r) = u''(a)(r - a)^2/2 - D$ for $a - r_0$ $\leq r \leq a + r_0$, and $\bar{u}(r) = 0$ if $r > a + r_0$ (cf. Ref. 25). It is seen that the parabolic approximation is quite satisfactory. For the dimer of gold, $(a/r_0)^2 = 19.6$, i.e., $u(r)$ is, in fact, a short-range potential. Given the obtained estimations of $\varepsilon$ and $a/r_0$, the solution of Eq. (18) is $\tau = 5.68$, which corresponds to $T_0 = 3513$ K. It was demonstrated in Ref. 25 that the structural transition is gradual in temperature, and it is similar to the crossover. Thus, one can expect that, in the temperature interval from 4000 K to 6000 K, the majority of clusters are in the chain-like state.

![](./images/812601548793184256_12.jpg)

FIG. 6. Interatomic potential for the dimer of gold calculated by EAM $u(r)$ and its parabolic approximation $\bar{u}(r)$. Intersection of dashed lines indicates the equilibrium interatomic distance $a$; $r_c$ labels the hard core distance, $u(r_c) = 0$.

### B. Clusters as quasi-fractals

Next, we will treat the clusters as quasi-fractal objects and try to estimate their fractal dimension $D_f$. Since the clusters are too small to apply common definitions of $D_f$, we will introduce a parameter that is sufficiently sensitive to $D_f$, the ratio of the maximum to average distance between the atoms pertaining to the same cluster ($\rho_{\text{max}}$ and $\rho_{\text{av}}$, respectively), $\eta = \rho_{\text{max}}/\rho_{\text{av}}$. Hereafter, this parameter will be termed the structure parameter. The quantities $\rho_{\text{max}}$ and $\rho_{\text{av}}$ are implied to be ensemble-averaged, and then all introduced quantities depend on $k$. To estimate $D_f$, one has to compare the structure parameter with model cluster structures. At zero temperature, all clusters have a solid-like structure ($D_f = 3$). The corresponding structure parameter will be denoted by $\eta_3$. If we neglect the angular-dependent part of the interatomic potential, then $\rho_{\text{max}} = \rho_{\text{av}} = a$ for $2 \leq k \leq 4$, where $a$ is the equilibrium interatomic distance for given $k$, i.e., $\eta_3 = 1$. In the opposite limit of a large cluster ($k \to \infty$), it is a macroscopic droplet that can be modeled by a solid sphere. Therefore, in this limit, $\rho_{\text{av}}$ can be estimated as the average distance between two points of a solid sphere, which is given by the following expression:

$$
\rho_{\mathrm{av}}=\frac{\iint\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right| d \mathbf{r}_{1} d \mathbf{r}_{2}}{2 \iint d \mathbf{r}_{1} d \mathbf{r}_{2}}. \tag{20}
$$

Here, integration is performed within a sphere of the radius $R$; the factor $1/2$ allows for the interchange of two points in the numerator of (20). Calculation of the integrals in (20) yields $\rho_{\text{av}} = (36/35)R$. Since $\rho_{\text{max}} = 2R$, we have $\eta_3(\infty) = 35/18$. In the intermediate range, $4 < k < \infty$, we performed simulation of the simple cubic crystal lattice with a constant spacing confined to a sphere and used the Padé approximation of the simulation results,

$$
\eta_{3}(k)=\left(\frac{35}{18} k+b\right)\left(k+b+\frac{34}{9}\right)^{-1}, \tag{21}
$$

which satisfies the boundary conditions $\eta_3(4) = 1$ and $\eta_3(\infty) = 35/18$; the constant $b = -2.91$ was found from the best fit condition for $4 \leq k \leq 100$. In such an approximation, the shell effect is smeared as well as for a macroscopic liquid droplet. The simulation results shown in Fig. 7 indicate that, in the cluster size range accessible for MD simulation, $\eta_3(k)$ is yet noticeably different from its asymptote.

For comparison, we select a linear cluster configuration with the constant interatomic spacing $a$ ($D_f = 1$) as a cluster structure alternative to the solid-like one. The average distance is calculated by consideration of all pairs of the distances between atoms, $\rho_{\text{av}} = a(k+1)/3$, while the maximum distance is $\rho_{\text{max}} = a(k-1)$. Then, the corresponding structure parameter $\eta_1$ for a linear cluster is

$$
\eta_{1}(k)=3\left(1-\frac{2}{k+1}\right). \tag{22}
$$

The asymptote of this parameter is 3, but in the interval $2 \leq k$ $\leq 26$, it increases sharply (Fig. 7).

As a model of the fractal object with $D_f = 2$, we have selected the freely jointed chain with the fixed distance between successive atoms and the angles between the successive bonds uniformly distributed between 0 and $\pi$. The corresponding structure parameter will be denoted by $\eta_2$. We simulated the chains of different numbers of atoms using the Monte Carlo simulation. Note that the simulated dependence $\eta_2(k)$ appears to be close to the median $(\eta_1 + \eta_3)/2$. In particular, the asymptote $\eta_2(\infty) \approx 2.65$ is not much different from $[\eta_1(\infty) + \eta_3(\infty)]/2 = 89/36 \approx 2.47$.

![](./images/812601548793184256_13.jpg)

FIG. 7. Structure parameter as a function of the cluster size for the solid-like clusters ($\eta_3$, dotted-dashed line), for the linear chain ($\eta_1$, dashed line), and for the freely jointed chain ($\eta_2$, solid line); dotted line shows the solid-like cluster asymptote. Dots indicate the MD simulation results (Sec. II) for 4006 K (squares), 5005 K (diamonds), and 6004 K (circles).

The fractal properties of the analyzed clusters can be elucidated by calculation of the structure parameter on the basis of the data from MD simulation. The results are shown in Fig. 7. The dots corresponding to the lightest clusters lie somewhat lower than the curve $\eta_2(k)$, which points to the fact that the clusters have a mixed structure. It is seen that the higher the temperature, the greater the $\eta$. This means that the fraction of chain-like configurations must dominate the solid-like ones at a temperature above the transitional one. The clusters up to $k = 26$, which are the largest detected clusters, show the same trend, but the corresponding dots lie below $\eta_2(k)$. Note that for $k > 10$, the structure parameter is no longer a good characteristic of the cluster fractal dimensionality. In fact, such clusters are significantly inhomogeneous formations with a relatively dense core. Strictly speaking, even the lightest clusters are inhomogeneous; therefore, they should be referred to as quasi-fractal objects.

Although one can expect that the simulation data pass through a maximum and then approach the solid state asymptote (dotted line in Fig. 7), this is not the case in Fig. 7. Apparently, such a maximum would correspond to a macroscopic droplet, whose size amounts to hundred atoms according to various estimates. For sufficiently large clusters, the size dependence of $\eta$ is defined by the amplitude of the thermal capillary oscillations proportional to $(\ln R)^{1/2}$, where $R$ is the cluster radius.⁴³ Thus, the investigated size range is too narrow to observe a maximum. We emphasize that from the viewpoint of the fractal dimensionality, even the clusters with $k > 10$ are far from being liquid droplets. At the same time, according to our discussion, they obey the classical thermodynamics of macroscopic liquid droplets.

To study the temperature dependence of the cluster structure, it is convenient to introduce the reduced structure parameter

$v=(\eta-\bar{\eta}) / \Delta \eta$, where $\bar{\eta}=\left(\eta_{2}+\eta_{3}\right) / 2$ and $\Delta \eta=\eta_{2}-\eta_{3}$. It is seen in Fig. 8 that, albeit $\eta, \bar{\eta}$, and $\Delta \eta$ are functions of $k$ (we adopt the same values of $\eta_{2}$ and $\eta_{3}$ as in Fig. 7), $v$ is almost independent of the cluster size (for the solid-like configuration, $v=-1 / 2$, and for the chain-like one, $v=1 / 2$ ). For $T \geq 4006 \mathrm{~K}$, dots represent the data from MD simulation of an equilibrium vapor shown in Fig. 7. For $T<3000 \mathrm{~K}$, the cluster number density in the equilibrium vapor is vanishingly small. Hence, we had to simulate individual equilibrated clusters using a standalone MD procedure, which was realized as follows. The cluster of seven or nine gold atoms initialized in the solid-like configuration at $T=0$ was placed in the $8 \times 8 \times 8 \mathrm{~nm}^{3} \mathrm{MD}$ simulation box, and the periodic boundary conditions were imposed along all three dimensions. The cluster was thermalized using the Langevin thermostat during a time long enough to equilibrate the cluster potential and kinetic energy at the chosen temperature. Then, the simulation was performed, during which the atom configurations were saved. The time frame separation was sufficiently long to ensure statistical independence of the saved data. The simulation was stopped when the first atom evaporation event occurred; then, the run was repeated until sufficient statistics was collected. At $T>2200 \mathrm{~K}$, the thermostat equilibration time becomes longer than the waiting time for evaporation. Therefore, the equilibrated clusters at higher temperatures cannot be obtained using this simulation technique.

Figure 8 demonstrates a good correspondence between the results for individual clusters and vapor. It is seen that for gold clusters, the structural transition takes place in a wide temperature range, and its characteristic temperature $T_{0}$, at which $v=0$, is much higher than the cluster melting temperature $(<1000 \mathrm{~K})$. Approximation of all shown simulation data by a parabola results in the estimation $T_{0}=2500 \mathrm{~K}$, which is in a satisfactory agreement with the rough assessment of the structural transition temperature (18) and (19), $T_{0}=3513 \mathrm{~K}$. One can conclude that, at $T \geq 4006 \mathrm{~K}$, the clusters are predominantly in the chain-like state, which justifies the virtual chain approximation discussed in Sec. III A.

![](./images/812601548793184256_14.jpg)

FIG. 8. Reduced structure parameter as a function of the temperature from MD simulation of individual clusters (crosses and squares) and equilibrium vapor (pluses and diamonds). Crosses and pluses indicate the cluster size 7, and squares and diamonds indicate the cluster size 9. The data from simulations are fitted by a parabola (solid line). The dashed line marks the boundary between the domains of predominant solid-like and chain-like configurations; labeled is the transitional temperature $T_{0}$ at which $v=0$.

![](./images/812601548793184256_15.jpg)

FIG. 9. Bond length distribution functions for the clusters of different sizes (solid lines, see legend) as compared to the radial distribution function for liquid gold (dashed line) from MD simulation. $T=6004 \mathrm{~K}$.

The structure of clusters can also be characterized by the BDF $f(\xi)$, where $\xi=r / a$. By definition, $f(\xi) d \xi$ is the probability that the dimensionless distance between given pair of atoms pertaining to the cluster of the size $k$ lies in the interval from $\xi$ to $\xi+d \xi$, so that $\int_{0}^{\infty} f(\xi) d \xi=1$. BDFs for the clusters of different sizes at different temperatures are shown in Figs. 9 and 10 and compared with the

![](./images/812601548793184256_16.jpg)

FIG. 10. Bond length distribution functions for the clusters ( $k=7$, solid lines) as compared to the radial distribution function for liquid gold (dashed lines) at $T=4006 \mathrm{~K}$ (blue lines) and $T=6004 \mathrm{~K}$ (red lines).

radial distribution functions (RDFs) for liquid gold. The BDFs are calculated based on the MD simulation of equilibrium vapor while the RDFs, on the MD simulation of a two-phase system. Figure 9 shows a gradual emergence of the second maximum in BDFs as $k$ is increased or temperature is decreased. It is seen that positions of the first and second maxima of BDFs shift toward larger distances with the increase in $k$ until the limit of bulk liquid is reached. The same trend is seen in Fig. 10 for different temperatures. It is worth mentioning that observable maxima both of BDFs and of RDFs shift toward larger distances as the temperature is decreased. Thus, thistrend is opposite to that observed for the Lennard-Jones liquid. $^{44}$  For the highest temperature, the second maxima are almost absent for the clusters with $k<10$ , which is a manifestation of the chainlike cluster structure. For $k>10$ or at the lowest temperature, Figs. 9 and 10 demonstrate a similarity between the BDFs and RDFs of a liquid. This is due to formation of the cluster core. Thus, anal- ysis of the cluster BDFs agrees with that based on the structure parameter $\eta$ .

## V. CONCLUSION
To summarize, we have performed MD simulation of the equi- librium dense gold vapor in the vicinity of the saturation line in a subcritical region, where the vapor non-ideality is primarily due to the presence of clusters comprising up to several tens of atoms. For this purpose, we have developed a new EAM potential that, in con- trast to its previous versions, is capable of accurate reproduction of the liquid gold surface tension along with the gold dimer binding energy, which are the key characteristics for a correct simulation of both thermodynamic and structural cluster properties. In this respect, a good agreement with the cold cluster energies calculated on the basis of different DFT versions is noteworthy. An agreement between the $p V T$ data from MD simulation and experiment is also worth mentioning. Since the new EAM potential proved to be effec- tive for the bulk solid, liquid, and gas, as well as for the arbitrary size clusters, it could be also used for the simulation of phenomena asso- ciated with high energy density input in condensed matter such as laser-induced vaporization and ablation followed by generation of nanoparticles.

The data from MD simulation enabled us to analyze the clus- ters present in the vapor. In particular, the cluster size distribution was compared to that obtained from different models, TPM and LDM, and the reduced Tolman length of gold liquid-vapor interface $\delta ≈0.16$ was determined from these distributions. It was found that both approaches yield almost the same results in a wide size range from the dimer to the macroscopic droplet. This means that the "hot" gold clusters are probably the most "classical" objects among other clusters. An agreement between the compressibility factor cal- culated for the gold vapor treated as an ideal mixture of clusters with different sizes and the wide-range $EoS^{33}$ justifies the assumptions of TPM.

We have investigated the peculiarities of spatial arrangement of atoms comprising the lightest gold clusters. An appropriate struc- ture parameter, $\eta$ , the ratio of the maximum to average distance between the atoms pertaining to the same cluster averaged over the cluster ensemble, is a good index of the cluster fractal structure. A comparison between $\eta$ s for gold clusters and the model objects whose fractal dimensionality is known beforehand shows that the clusters of less than ten atoms are most similar to the freely jointed chains with the fractal dimensionality of two. Thus, it was revealed that such clusters could be found in the chain-like configurations analogous to those previously found for the nonmetallic clusters in the argon-like vapor, in which atoms interact via a pairwise poten- tial. A temperature-driven transformation from the solid-like to chain-like structure is a structural transition. The proposed estima- tion of the temperature range, where this transition can occur for the metal-bond clusters, shows that the transition temperature is essentially higher than the melting temperature.

For investigation of the dependence of cluster structure on tem- perature, the reduced structure parameter $v$ was introduced. For the lightest clusters, this parameter proved to be independent of the cluster size. Its temperature dependence obtained using MD simulation of equilibrium vapor and individual clusters is indica- tive of the fact that the transitional temperature range is quite wide. The temperature of its central point is well above the gold melting point and amounts to $\sim 2500 ~K$ , which correlates with the estimation from the virtual chain approximation. The results of MD simulation show that the fraction of chain-like configurations decreases with the decrease in temperature. However, the virtual chain approximation is still applicable for the gold clusters at tem- peratures higher than $2500 ~K$ . Analysis of the cluster BDFs illus trates this conclusion: the second maximum of BDF almost vanishes for the small clusters with $k<10$ , but it is visible for the larger clusters.

An open issue is whether metal clusters other than gold have the reduced Tolman length close to that obtained in this work, i.e., whether all clusters with metallic bonds are almost "classi- cal." However, it seems unquestionable that this does not apply to "anomalous" metals such as mercury whose small clusters have a non-metallic bond type.

## SUPPLEMENTARY MATERIAL
See the supplementary material for a detailed discussion of the EAM potential development for gold. The newly developed potential is available in both a rational function set and a tabulated form for the LAMMPS simulation package

## APPENDIX: EAM POTENTIAL FOR GOLD
To develop a potential capable of a correct reproduction of the gold phase diagram in a wide range of compression and tempera- ture, the stress-matching method $^{28,45,46}$ is used here. The develop ment of interatomic potential will proceed through the following well-defined steps. The first step involves generating a database of the experimental data extrapolated to zero temperature (like the elastic constants, cohesion energy, and lattice constants) and the first-principle cold stress tensor curves obtained by density func- tional theory (DFT). The second step involves fitting the EAM func- tional parameters to the database, which, in its turn, produces sev- eral good EAM parameter sets (candidates). For the last step, which requires MD simulations, the best potential is selected from the can- didates depending on how well they reproduce important experi- mental properties not included in the fitting, such as the melting temperature and the surface tension. Final validation may be per- formed by simulation of material properties of interest, such as the

vacancy formation and migration energies, the surface tension as a function of temperature, the melting line (melting temperature vs pressure) and the shock Hugoniot (longitudinal stress vs volume), and comparing calculated results with the available experimental data. Because for shock waves with the pressures of up to a few hundred GPa, the thermal energy and the pressure are notably smaller than the corresponding cold energy and pressure in condensed-phase materials, we can expect that the potential provides also a reasonable thermodynamics of simulated material in a wide range of temperatures.

As in the original work,⁸ the fitting database contains the stress tensor components $\sigma_{\alpha\beta}(V) = -p_{\alpha\beta}(V)$ calculated by the DFT ABINIT code in the cold fcc lattice under continuous hydrostatic and uniaxial deformation along the [100]-axis. The fitting procedure implies also the constraints of monotonic behavior of $p_{\alpha\alpha}(V)$, including the requirement that the sound velocity increases with the compression. Experimental bulk modulus of 182 GPa and elastic constants of $c_{11} = 204$ GPa, $c_{12} = 171$ GPa, and $c_{44} = 55$ GPa⁴⁷ extrapolated to $T = 0$ K, the equilibrium density of 19.4963 g/cc with the lattice parameter of $a = 0.406\,365$ nm, and the cohesive energy 367.61 kJ/mol⁴⁸ of gold are also included in this database. Apart from those mentioned above, the experimental vacancy formation energy of 1.4 eV, the unrelaxed stacking fault energy of 0.06 J/m², and the surface energy of solid $\gamma_{s}(111) = 1.56$ J/m² are added to extend the database. It is worth mentioning that, since the surface energy $\gamma_{s}(111)$ of solid is not well-known, it was adjusted several times in fitting the intermediate potential candidates to obtain better agreement with the experimental surface tension of liquid gold at the melting point.

For reasonable MD simulation of dense vapor, an employed EAM potential must provide the dimer cluster energy very close to the experimental one of $E_{2} = 1.15$ eV per atom;⁵ therefore, it is also included in the database. As a result of forcing the candidates to fit $E_{2}$, our new potential gives $E_{2} = 1.126$ eV, as distinct from much lower $E_{2} = 0.3054$ eV provided by another popular EAM potential for gold.⁴⁹ The mathematical form of the EAM potential, fitting methods, and the stress-strain curves is presented in the supplementary material.

A good test of the new EAM potential is the calculation of binding energies for the cold ($T = 0$) Auₙ clusters (Table III). We include the solid-like (nanocrystal) cluster configurations. Table III compares our calculations with several versions of DFT. In DFT-TPSS and DFT-PBE versions,⁹ the same nanocrystal configurations are treated. The DFT-FSGB version⁵ based on norm-conserving pseudopotentials and numerical atomic basis sets includes explicitly the electron spin-orbit effect, which yields stable non-compact (chain-like and plane) configurations. Note that the difference between EAM and DFT is of the same order of magnitude as the difference between different DFT versions, and all size dependences of the binding energy per atom are monotone. A satisfactory agreement between EAM and DFT-TPSS and DFT-FSGB is worth mentioning. At the same time, EAM ensures the best extrapolation to the limits of dimer and bulk (as compared to DFT-TPSS and DFT-PBE).

The phase coexistence method is used to calculate the melting temperature at nearly zero pressure. Using the Langevin thermostat, a radial temperature profile $T(r) \sim r$ is applied to a free standing sphere of solid gold with the radius $R = 50$ nm. Because the temperature increases with the radius, an outer layer of the sphere melts, but the central part remains solid if the chosen $T(0)$ is below and $T(R)$ is above the melting point. After partial melting of the sphere, the thermostat is turned off and the two-phase system evolves as a NVE ensemble until equilibration between the solid and liquid phases at the melting point $T_{m}$. It is found that the new EAM potential provides $T_{m} = 1318$ K and the liquid density $\rho_{\ell} = 17.58$ g/cc, which are close to the experimental data $T_{m} = 1337.33$ K and $\rho_{\ell} = 17.31$ g/cc. The EAM potential⁴⁹ provides $T_{m} = 1130$ K by using the same coexistence method.

The liquid-vapor binodal is also calculated with the phase coexistence method. Initially, a sufficiently thick solid slab, which is infinite in $y$-axis and $z$-axis, was placed in a MD box with periodic boundary conditions along all three axes. The thermostat heats and melts the slab, which results in a free standing plane liquid film surrounded by vacuum in the $x$-direction. Evaporation of the liquid produces a gas whose density increases until the saturated vapor density is reached. Then, the thermostat is turned off, and the production simulation starts to gather data. Figures 11-13 show the calculated binodal line in the $T$-$\rho$, $p$-$\rho$, and $p$-$T$ phase planes, respectively.

The obtained equilibrium liquid-vapor systems are used for calculation of the surface tension as a function of temperature. According to the mechanical definition of surface tension $\sigma = \int[p_{n}(x) - p_{t}(x)]dx$, where $p_{n}$ and $p_{t}$ are the normal and tangential (with respect to the liquid film) components of the pressure tensor, respectively, and integration is performed over a thin interphase layer.⁴²,⁴⁴ Due to the mechanical equilibrium between vapor and liquid, the pressure $p_{n}(x) = p_{s}(T_{s})$ is constant throughout the

<table>
<caption>TABLE III. EAM binding energies per atom of Auₙ clusters (eV) vs three versions of DFT calculations for different atom configurations. DFT-TPSS and DFT-PBE are obtained from the linear approximations⁹ extrapolated to a wide size range (but for $n = 55$ and 147). For DFT-FSGB, the result for the lowest-energy isomer is shown.</caption>
<thead>
  <tr>
    <th>$n$</th>
    <th>EAM</th>
    <th>DFT-TPSS⁹</th>
    <th>DFT-PBE⁹</th>
    <th>DFT-FSGB⁵</th>
    <th>Experiment</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2</td>
    <td>1.126</td>
    <td>1.318</td>
    <td>1.303</td>
    <td></td>
    <td>1.15</td>
  </tr>
  <tr>
    <td>3</td>
    <td>1.594ᵃ</td>
    <td>1.567</td>
    <td>1.506</td>
    <td>1.66</td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>1.900ᵇ</td>
    <td>1.724</td>
    <td>1.635</td>
    <td>2.12</td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td>2.061</td>
    <td>1.836</td>
    <td>1.726</td>
    <td>2.28</td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td>2.210ᶜ</td>
    <td>1.921</td>
    <td>1.796</td>
    <td>2.56</td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td>2.671ᵈ</td>
    <td>2.231</td>
    <td>2.050</td>
    <td>2.96</td>
    <td></td>
  </tr>
  <tr>
    <td>38</td>
    <td>3.060ᵉ</td>
    <td>2.548</td>
    <td>2.310</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>55</td>
    <td>3.159ᶠ</td>
    <td>2.632ᶠ</td>
    <td>2.378ᶠ</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>98</td>
    <td>3.296ᵍ</td>
    <td>2.748</td>
    <td>2.473</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>147</td>
    <td>3.381ᶠ</td>
    <td>2.818ᶠ</td>
    <td>2.532ᶠ</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>∞</td>
    <td>3.970ʰ</td>
    <td>3.285</td>
    <td>2.913</td>
    <td></td>
    <td>3.81</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="6">ᵃTriangle.<br>ᵇTetrahedron.<br>ᶜOctahedron.<br>ᵈIcosahedron.<br>ᵉOctahedra.<br>ᶠIcosahedra.<br>ᵍTetrahedra.<br>ʰfcc.</td>
  </tr>
</tfoot>
</table>

![](./images/812601548793184256_17.jpg)

![](./images/812601548793184256_18.jpg)

$x$-axis, while $p_t$ is negative within the interphase layer and $p_t = p_n$ outside of it. At the experimental melting temperature, our new EAM potential yields $\sigma = 1.104\ \text{J/m}^2$, which is close to the experimental value $\sigma = 1.145\ \text{J/m}^2$, $^{51}$ while the surface tension from the original EAM potential$^{28}$ is twice as low, $\sigma = 0.565\ \text{J/m}^2$, and Grochola's potential$^{49}$ provides the notably higher surface tension of $1.295\ \text{J/m}^2$.

Obtaining the equilibrium two-phase systems in the vicinity of the critical point is extremely complicated in MD simulation. The closest point with the clear density separation was at $T = 9.2$ kK in our simulations. We estimate the critical temperature as $T_{cr} \approx 9.25$ kK because the large density fluctuations for $T > 9.25$ kK lead to an inability to realize two separated phases.

It is worth mentioning that the usage of surface tension for estimating the critical temperature is unreasonable since the calculation of tension is less accurate than the calculation of density. The calculated surface tension shown in Fig. 14 approaches zero and becomes very inexact for $T > 9$ kK, whereas the liquid-vapor transition layer is still well-defined. The surface tension can be fitted by $\sigma(T) = \sigma^*\theta^v$, where $\theta = 1 - T/T_{cr}$ and $\sigma^*$ and $v$ are the fitting parameters. With the fixed $T_{cr} \approx 9.25$ kK, fitting the surface tensions obtained for all simulated temperatures in the range from 1.33 kK to 9.14 kK yields $\sigma^* = 1.337\ \text{J/m}^2$ and $v = 1.26$.

The binodal pressure approaching the critical point is assumed to be proportional to $\theta$, which yields $p_{cr} \approx 0.22$ GPa. An estimate of the critical density can be derived from the rectilinear diameter law $p_{cr} - (\rho_\ell + \rho_v)/2 \propto \theta$, where $\rho_v$ is the vapor density. Using the densities $\rho_\ell = 5.734$ g/cc and $\rho_v = 2.244$ g/cc obtained from MD data at the highest $T = 9.14$ kK, at which the density can still be measured with a good accuracy, we arrive at $\rho_{cr} \approx (\rho_\ell + \rho_v)/2 = 3.99$ g/cc.

![](./images/812601548793184256_19.jpg)

![](./images/812601548793184256_20.jpg)

Figure 14 shows the calculated surface tension in comparison with the experimental linear fits,

$$\sigma(T)=1.105-0.28(T-1.336), \tag{A1}$$

$$\sigma(T)=1.145-0.20(T-1.338), \tag{A2}$$

$$\sigma(T)=1.150-0.14(T-1.337), \tag{A3}$$

$$\sigma(T)=1.337\left(1-T/T_{cr}\right)^{1.26}, \tag{A4}$$

where the temperature is measured in kK and the surface tension, in $J/m^{2}$. The linear fit (A1) of the experimental data in the temperature range from 1.35 kK to 1.775 kK was reported in Ref. 52. The average fit (A2) of many experimental data limited by the maximum temperature of 1.381 kK is borrowed from the review in Ref. 51. The linear fit (A3) for temperatures up to $T = 1.873$ kK was obtained recently in Ref. 53. Equation (A4) fits our MD results with a good accuracy, as it is seen in Fig. 14, where it lies between the above-mentioned experimental fits.

## DATA AVAILABILITY

The data that support the findings of this study are available within the article (and its supplementary material).

## REFERENCES

$^{1}$M. L. Cohen and W. D. Knight, Phys. Today 43(12), 42 (1990).
$^{2}$É. L. Nagaev, Sov. Phys. Usp. 35, 747 (1992).
$^{3}$A. Banerjee and M. K. Harbola, J. Chem. Phys. 113, 5614 (2000).
$^{4}$M. Payami, J. Chem. Phys. 111, 8344 (1999).
$^{5}$E. M. Fernández, J. M. Soler, I. L. Garzón, and L. C. Balbás, Phys. Rev. B 70, 165403 (2004).
$^{6}$I. L. Garzón, K. Michaelian, M. R. Beltrán, A. Posada-Amarillas, P. Ordejón, E. Artacho, D. Sánchez-Portal, and J. M. Soler, Phys. Rev. Lett. 81, 1600 (1998).
$^{7}$P. K. Jain, Struct. Chem. 16, 421 (2005).
$^{8}$A. A. Tal, W. Olovsson, and I. A. Abrikosov, Phys. Rev. B 95, 245402 (2017).
$^{9}$H. Li, L. Li, A. Pedersen, Y. Gao, N. Khetrapal, H. Jónsson, and X. C. Zeng, Nano Lett. 15, 682 (2015).
$^{10}$M. Payami and N. Nafari, J. Chem. Phys. 109, 5730 (1998).
$^{11}$Y. Noguchi, S. Ishii, K. Ohno, and T. Sasaki, J. Chem. Phys. 129, 104104 (2008).
$^{12}$V. E. Bondybey and J. H. English, J. Chem. Phys. 74, 6978 (1981).
$^{13}$T. Masubuchi, J. F. Eckhard, K. Lange, B. Visser, M. Tschurl, and U. Heiz, J. Chem. Phys. 89, 023104 (2018).
$^{14}$S. I. Anisimov and B. S. Luk'yanchuk, Phys. Usp. 45, 293 (2002).
$^{15}$B. Chimier and V. T. Tikhonchuk, Phys. Rev. B 79, 184107 (2009).
$^{16}$M. E. Povarnitsyn, T. E. Itina, P. R. Levashov, and K. V. Khishchenko, Phys. Chem. Chem. Phys. 15, 3108 (2013).

$^{17}$N. A. Inogamov, V. V. Zhakhovskii, and V. A. Khokhlov, J. Exp. Theor. Phys. 127, 79 (2018).
$^{18}$H. Yang, E. Goudeli, and C. J. Hogan, Jr., J. Chem. Phys. 148, 164304 (2018).
$^{19}$H. Yang, Y. Drossinos, and C. J. Hogan, J. Chem. Phys. 151, 224304 (2019).
$^{20}$Z. Fthenakis, A. N. Andriotis, and M. Menon, Chem. Phys. 119, 10911 (2003).
$^{21}$D. G. Andriotis, L. D. Schmidt, and R. Aris, J. Chem. Phys. 96, 6891 (1992).
$^{22}$S. Chiriki, S. Jindal, and S. S. Bulusu, J. Chem. Phys. 146, 084314 (2017).
$^{23}$D. I. Zhukhovitskii, J. Chem. Phys. 142, 164704 (2015).
$^{24}$D. I. Zhukhovitskii, J. Chem. Phys. 103, 9401 (1995).
$^{25}$D. I. Zhukhovitskii, J. Chem. Phys. 110, 7770 (1999).
$^{26}$D. I. Zhukhovitskii, J. Chem. Phys. 144, 184701 (2016).
$^{27}$D. I. Zhukhovitskii, J. Chem. Phys. 101, 5076 (1994).
$^{28}$V. V. Zhakhovskii, N. A. Inogamov, Y. V. Petrov, S. I. Ashitkov, and K. Nishihara, Appl. Surf. Sci. 255, 9592 (2009).
$^{29}$V. Zhakhovskii, K. Nishihara, Y. Fukuda, S. Shimojo, T. Akiyama, S. Miyanaga, H. Sone, H. Kobayashi, E. Ito, Y. Seo, M. Tamura, and Y. Ueshima, in IEEE Proceeding of the 5th International Symposium on Cluster Computing and Grid (CCGrid 2005) (IEEE Computer Society, 2006), Vol. 2, pp. 848-854.
$^{30}$M. S. Egorova, S. A. Dyachkov, A. N. Parshikov, and V. V. Zhakhovsky, Comput. Phys. Commun. 234, 112 (2019).
$^{31}$F. H. Stillinger, Jr., J. Chem. Phys. 38, 1486 (1963).
$^{32}$D. I. Zhukhovitskii, Russ. J. Phys. Chem. 75, 1043 (2001).
$^{33}$See http://teos.fic.ac.ru/rusbank for Shock Wave Database.
$^{34}$A. V. Bushman, G. I. Kanel', A. L. Ni, and V. E. Fortov, Intense Dynamic Loading of Condensed Matter (Taylor & Francis, 1993), p. 297.
$^{35}$K. V. Khishchenko, S. I. Tkachenko, P. R. Levashov, I. V. Lomonosov, and V. S. Vorob'ev, Int. J. Thermophys. 23, 1359 (2002).
$^{36}$I. V. Lomonosov, Laser Part. Beams 25, 567-584 (2007).
$^{37}$M. Volmer and A. Weber, Z. Phys. Chem. 199, 277 (1926).
$^{38}$R. Becker and W. Döring, Ann. Phys. 416, 719 (1935).
$^{39}$Ya. B. Zeldovich, J. Eksp. Teor. Fiz. 12, 525 (1942).
$^{40}$G. Wilemski, J. Chem. Phys. 103, 1119 (1995).
$^{41}$R. C. Tolman, J. Chem. Phys. 17, 333 (1949).
$^{42}$J. Rowlinson and B. Widom, Molecular Theory of Capillarity (Clarendon, Oxford, 1982).
$^{43}$D. I. Zhukhovitskii, J. Chem. Phys. 135, 044512 (2011).
$^{44}$S. I. Anisimov, D. O. Dunikov, V. V. Zhakhovskii, and S. P. Malyshenko, J. Chem. Phys. 110, 8722 (1999).
$^{45}$B. J. Demaske, V. V. Zhakhovsky, C. T. White, and I. I. Oleynik, AIP Conf. Proc. 1426, 1211 (2012).
$^{46}$V. V. Zhakhovsky, K. P. Migdal, N. A. Inogamov, and S. I. Anisimov, AIP Conf. Proc. 1793, 070003 (2017).
$^{47}$R. O. Simmons and H. Wang, Single Crystal Elastic Constants and Calculated Aggregate Properties: A Handbook (MIT Press, Cambridge, 1991).
$^{48}$C. Kittel, Introduction to Solid State Physics, 8th ed. (John Wiley & Sons, Inc., 2005).
$^{49}$G. Grochola, S. P. Russo, and I. K. Snook, J. Chem. Phys. 123, 204719 (2005).
$^{50}$F. Geiger, C. A. Busse, and R. I. Loehrke, Int. J. Thermophys. 8, 425 (1987).
$^{51}$B. J. Keene, Int. Mater. Rev. 38, 157 (1993).
$^{52}$K. Nogi, K. Oishi, and K. Ogino, Mater. Trans., JIM 30, 137 (1989).
$^{53}$I. Egry, G. Lohoefer, and G. Jacobs, Phys. Rev. Lett. 75, 4043 (1995).

J. Chem. Phys. 152, 224705 (2020); doi: 10.1063/5.0010156
Published under license by AIP Publishing

152, 224705-13