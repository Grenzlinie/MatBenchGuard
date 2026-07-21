EPJ manuscript No.
(will be inserted by the editor)

# Surface effects in nanoparticles: application to maghemite
$\gamma$-$\text{Fe}_2\text{O}_3$

H. Kachkachi$^{1a}$, A. Ezzir$^1$, M. Noguès$^1$, and E. Tronc$^2$

$^1$ LMOV-CNRS UMR 8634, Université de Versailles St. Quentin, 45, avenue des Etats-Unis, 78035 Versailles Cedex, France
$^2$ LCMC-CNRS URA 1466, Université Pierre & Marie Curie, 4 place Jussieu, 75252 Paris Cedex, France

Received: date / Revised version: date

**Abstract.** We present a microscopic model for nanoparticles, of the maghemite ($\gamma$-Fe$_2$O$_3$) type, and perform classical Monte Carlo simulations of their magnetic properties. On account of Mössbauer spectroscopy and high-field magnetisation results, we consider a particle as composed of a core and a surface shell of constant thickness. The magnetic state in the particle is described by the anisotropic classical Dirac-Heisenberg model including exchange and dipolar interactions and bulk and surface anisotropy. We consider the case of ellipsoidal (or spherical) particles with free boundaries at the surface. Using a surface shell of constant thickness ($\sim0.35$ nm) we vary the particle size and study the effect of surface magnetic disorder on the thermal and spatial behaviors of the net magnetisation of the particle. We study the shift in the surface "critical region" for different surface-to-core ratios of the exchange coupling constants. It is also shown that the profile of the local magnetisation exhibits strong temperature dependence, and that surface anisotropy is reponsible for the non saturation of the magnetisation at low temperatures.

**PACS.** 75.50.Tt Fine Particle Systems – 75.30.Pd Surface Magnetism – 75.10.Hk Classical Spin Models

## 1 Introduction
Surface effects in a nanoparticle are of great importance since they dominate the magnetic properties and become more important with decreasing size of the particle. In particular, the picture of a single-domain magnetic particle where all spins are pointing into the same direction, leading to coherent relaxation processes, is no longer valid when one considers the effect of misaligned spins on the surface on the global magnetic properties of the particle. Indeed, even for strong exchange interactions the surface is responsible for coordination defects, and in a particle of radius of the order of 4 nm, 50% (in the $\gamma$-Fe$_2$O$_3$ nanoparticles) of atoms lie on the surface, and therefore the effect of the latter cannot be neglected.

The magnetisation near the surface is generally lower than in the interior. This effect leads to a thermodynamic perturbation in exchange interactions near the surface, which can be sizable at high temperatures. In a finite system, the effect of temperature introduces, in addition to the usual renormalization of the spin-wave spectrum, a spatial dependence of the magnetisation (see [1] and references therein for the case of semi-infinite cubic crystals). Indeed, the symmetry breaking at the surface results in a surface anisotropy. In most cases, this happens to be strong enough as to compensate for the work needed against the exchange energy that prefers full alignment, and it is conceivable then that the magnetisation vector will point along the bulk easy axis in the core of the particle, and will then gradually turn into a different direction when it approaches the surface. In addition to the exchange interactions, which are the strongest interactions between atoms in a magnetic system, there are also the purely magnetic dipole interactions between the magnetic moments of the atoms and the interactions between the magnetic moments and the electric field of the crystal lattice (spin-orbit interactions). The last two types of interactions are relativistic in origin and therefore correspond to energies that are much smaller than the exchange energy on a short length scale, but as they are long range interactions they lead, in general, to non negligible contributions. Indeed, these interactions play an important role in that they introduce a preferred direction in the system as they correspond to a Hamiltonian (see below) that is not invariant under rotation operations. In other words, they lead to the appearance of an anisotropy energy, i.e. the dependence of the total energy of the system on the direction of magnetisation. Moreover, the most important feature of the relativistic interactions is that they change the magnetic moment of an atom from one site to another, and hence introduce a non uniform spatial distribution of the magnetic moment in the system. The treatment of the dipole-dipole interactions [2] leads to two energy terms corresponding to the volume and surface charges. In a small magnetic system, such as a nanoparticle, only

$^{a}$ Corresponding author kachkach@physique.uvaq.fr

the second contribution is important since it accounts for the shape anisotropy, and the former becomes negligible as one integrates over a small volume (see a detailed discussion in [3] and references therein).

Therefore, it is necessary to take into account all different contributions to the energy, exchange and dipolar interactions, bulk and surface anisotropies, in any study of spatial distributions of the magnetisation in a small magnetic system.

One of our ultimate goals is to understand the effect of surfaces on the thermodynamic and spatial behaviors of the magnetisation in small systems, since this is also of crucial importance to the study of the dynamics of such systems where the surface effects are considerable. In this case, the dynamics is rendered more complicated by the additional (metastable or stable) magnetic states corresponding to the surface configurations.

According to Mössbauer spectroscopy performed by Morrish et al. (see [4] for a review, and also the seminal work by Coey [5]), the iron cations at the surface of the $\gamma$-Fe$_2$O$_3$ particles have a noncollinear magnetic structure from 4.2 K to room temperature. The Mössbauer-spectroscopy analysis performed in [6] on $\gamma$-Fe$_2$O$_3$ particles show that the spectrum contains two components, one associated with the bulk and the other with iron atoms on the surface. The latter seems to disappear at temperatures in the range 30 – 75 K, depending on the mean diameter of the particle assembly. From these Mössbauer-effect analyses it was also inferred that the surface shell has a thickness of about 0.35 nm, independently of the particle volume. This fact will be used in our simulations to determine the ratio of the surface and core number of atoms. In addition, measurements of the magnetisation at high fields performed on the $\gamma$-Fe$_2$O$_3$ nanoparticles [7] (see also [8] for cobalt particles) have shown that the magnetisation is strongly influenced by the surface effects, depending on the particle size. In Figs. 1 we show the field and thermal variation of the magnetisation for different particle sizes. In Fig. 1a we see that there is a sudden increase of the magnetisation as a function of the applied field when the temperature reaches 70 K, and that the magnetisation does not saturate at the highest field value, i.e. 5.5 T. In Fig. 1b there is an important increase of the magnetisation at low temperatures. In Fig.1c the thermal behaviour of the magnetisation at 5.5 T is shown for samples with different mean diameter. There we see that the smaller is the mean diameter of the particle the more important is the increase of the magnetisation at very low temperatures. This can be explained by the fact that the surface component corresponds to a state with canted atomic moments at low temperatures [5] [6]. Furthermore, open hystereses were observed [9] in the nickel ferrite particles (NiFe$_2$O$_4$) up to fields of 16 T, while the anisotropy field of the bulk sample is utmost $4 \times 10^{-2}$ T. The authors consider that the core spins are colinear whereas those on the surface are misaligned. In the case of $\gamma$-Fe$_2$O$_3$ particles, however, no such irreversibility in the magnetisation hysteresis loop was observed [6], [9].

Therefore, according to Mössbauer spectroscopy and high-field magnetisation measurements, we may think of a particle as containing a magnetically disordered surface of a certain width and a core more or less ordered depending on the size of the particle. The net magnetisation of the particle is given by the (weighed) sum of the contributions from the surface and the core. The increase of the surface contribution at low temperatures becomes more important with decreasing size of the particle, as shown in Fig.1c.

In this work, we compute the thermal behavior of the different contributions to the magnetisation due to the surface and core for different values of exchange couplings and different surface-to-volume ratios of the number of spins. We also compute the spatial variation of the magnetisation at different temperatures and the specific heat for different sizes. All calculations are performed in zero magnetic field.

## 2 Model for magnetic particles

### 2.1 Hamiltonian

As was discussed in the introduction, it is well established [2], [3] that any theory dealing with the spatial magnetisation distribution must consider all three energy contributions, exchange, anisotropy and magnetostatic, and that there is no obvious reason for neglecting any one of these. However, it should be emphasised that in very small particles the exchange interactions are too strong to allow for subdivision into domains, so that the magnetostatic energy term is considered here only in order to account for the shape anisotropy in the case of ellipsoidal particles. It should also be stressed, as discussed in the introduction, that because of the surface anisotropy and the symmetry breaking at the surface, there is no reason to consider the exchange interactions on the surface as equal to those in the core, and thereby the particle may acquire a non uniform distribution of the magnetisation.

Therefore, to take account of all these energy contributions, we propose a model, based on the classical anisotropic Dirac-Heisenberg (exchange and dipolar) Hamiltonian, describing the spinel structure of the (spherical or ellipsoidal) ferrimagnetic nanoparticles (e.g., $\gamma$-Fe$_2$O$_3$). In this article the calculations are performed using classical Monte Carlo simulations of the magnetisation thermal behavior of the particle with open boundaries at the surface.

So, the exchange, anisotropy and Zeeman contributions are given by the following anisotropic Dirac-Heisenberg Hamiltonian

$$
\begin{aligned}
\mathcal{H}_{D H}= & -\sum_{i, \mathbf{n}} \sum_{\alpha, \beta=A, B} J_{\alpha \beta} \mathbf{S}_{i}^{\alpha} \cdot \mathbf{S}_{i+\mathbf{n}}^{\beta}-K \sum_{i=1}^{N_{t}}\left(\mathbf{S}_{i} \cdot \mathbf{e}_{i}\right)^{2} \\
& -\left(g \mu_{B}\right) H \sum_{i=1}^{N_{t}} \mathbf{S}_{i},
\end{aligned}
\tag{1}
$$

where $J_{\alpha \beta}$ (positive or negative) are the exchange coupling constants between (the $\alpha, \beta=A, B$) nearest neighbors

![](./images/867747407591375369_1.jpg)

Fig. 1. a) Magnetisation as a function of the magnetic field of a diluted assembly of $\gamma$-Fe$_2$O$_3$ nanoparticles with a mean diameter of 2.7 nm. b) Thermal variation of the magnetisation extracted from a) at a field of 55 kOe. c) Thermal variation of the magnetisation in a field of 55 kOe for three samples with different mean diameters (2.7,4.8, 7.1 nm).

spanned by the unit vector $\mathbf{n}$; $\mathbf{S}_i^\alpha$ is the (classical) spin vector of the $\alpha^{th}$ atom at site $i$; $H$ is the uniform field applied to all spins (of number $N_t$) in the particle, $K>0$ is the anisotropy constant and $\mathbf{e}_i$ the single-site anisotropy axis (see definition below). A discussion of the core and surface anisotropy will be presented below. In the sequel the magnetic field will be set to zero.

To the Dirac-Heisenberg Hamiltonian we add the pairwise long-range dipolar interactions

$$
\mathcal{H}_{dip} = \frac{(g\mu_B)^2}{2} \sum_{i \neq j} \frac{(\mathbf{S}_i \cdot \mathbf{S}_j) R_{ij}^2 - 3 (\mathbf{S}_i \cdot \mathbf{R}_{ij}) \cdot (\mathbf{R}_{ij} \cdot \mathbf{S}_j)}{R_{ij}^5}
\tag{2}
$$

where $g$ is the Landé factor, $\mu_B$ the Bohr magneton and $\mathbf{R}_{ij}$ the vector connecting any two spins on sites $i$ and $j$ of the particle, $R_{ij} \equiv \|\mathbf{R}_{ij}\|$.

### 2.2 Method of simulation

The particle we consider here is a spinel with two different iron sites, a tetrahedric $\text{Fe}^{3+}$ site (denoted by A) and an octahedric $\text{Fe}^{3+}$ site (denoted by B). The nearest neighbor exchange interactions are (in units of K) [10], [9] : $J_{AB}/k_B \simeq -28.1$, $J_{BB}/k_B \simeq -8.6$, and $J_{AA}/k_B \simeq -21.0$. These coupling constants are used in the Dirac-Heisenberg Hamiltonian $\mathcal{H}_{DH}$ in order to model the phase transition from the paramagnetic to ferrimagnetic order as the temperature is lowered down to zero through $T_c \simeq 906$ K. In the spinel structure an atom on site A has 12 nearest neighbors on the sublattice B and 4 on the sublattice A, and an atom on site B has 6 nearest neighbors on A and 6 on the B sublattice; the number of B sites is twice that of sites A. The nominal value of the spin on sites A and B is 5/2, and this justifies the use of classical spins. We have also taken account of $\frac{1}{3}$ of lacuna for each two B atoms randomly distributed in the particle. The nanoparticle we have studied contains $N_t$ spins $(\simeq 10^3 - 10^5)$, and its radius is in the range 2-3.5 nm. Our model is based on the hypothesis that the particle is composed of a core of radius containing $N_c$ spins, and a surface shell surrounding it that contains $N_s$ spins, so that $N_t = N_c + N_s$. Thus varying the size of the particle while maintaining the thickness of the surface shell constant $(\sim 0.35$ nm), is equivalent to varying the surface to total number of spins, $N_{st} = N_s/N_t$, and this allows us to study the effect of surfaces of different contributions. All spins in the core and on the surface are identical, but interact via the, $a$ priori, different couplings depending on their locus in the whole volume. We will consider both cases of identical interactions, and that of the general situation with different interactions on the surface and in the core. Although we treat only the crystallographically "ideal" surface, we do allow for perturbations in the exchange constants on the surface. This is meant to take into account, though in a somewhat phenomenological way, the possible defects on the surface, and the possible interactions between the particles and the matrix in which they are embedded. In [9] it was assumed that the pairwise exchange interactions are of the same magnitude for the core and surface atoms, but there was postulated the existence of a fraction of missing bonds on the surface. On the other hand, we consider that the exchange interactions between the core and surface spins are the same as those inside the core. We also stress that we are only concerned with non interacting particles, so we ignore the effect of interparticle interactions on the exchange couplings at the surface of the particle.

In our simulations we start with a regular box ($X \times Y \times Z$) of spins with the spinel structure having the properties mentioned above, and then given the radius or total number of spins in the particle, we cut in a sphere or an ellipsoid. We choose the center of the particle to lie at one of

![](./images/867747407591375369_2.jpg)

Fig. 2. Normalized distribution of the coordination number in a spherical and ellipsoidal particle for $N_{st}=40\%$.

the lattice sites. In all cases free boundary conditions are used, and thus a spin is considered as a core or surface spin depending on whether it has or not its full coordination number. Fig. 2 shows the distribution of the coordination numbers in a spherical and ellipsoidal particle. Therefore, in our simulations each spin has a structure associated with it that contains the coordinates of the corresponding site, the nature of the site in the spinel structure (i.e. A or B), its locus (core or surface), the number of its nearest neighbours, and the total number of such sites. Thus, once the structure of each spin is defined, the spins outside of the sphere or the ellipsoid are discarded. This accomplishes the simulation of the crystal structure and shape of the particle. Next, we proceed with the Monte Carlo calculations.

The classical Monte Carlo method based on the Metropolis algorithm is now a standard method and detailed descriptions can be found in [11]; so here we summarize only the main procedure. We calculate the expectation value of a function $f(\{\mathbf{S}_{i}\})$ of the spins $\mathbf{S}_{i}$

$$
\langle f\rangle=\frac{Tr\left[\exp \left(-H / k_{B} T\right) f\right]}{Tr \exp \left(-H / k_{B} T\right)}\qquad(3)
$$

by generating a Markov chain of spin configurations $\{\mathbf{S}_{i}\}$ of the system and taking the average

$$
\bar{f}=\frac{1}{L} \sum_{c=1}^{L} f\left(\left\{\mathbf{S}_{i}^{c}\right\}\right).\qquad(4)
$$

From any initial (random in our case) configuration $c$ we generate a trial configuration by choosing the spin coordinates of a randomly chosen lattice site $i$ by $(\alpha=x, y, z)$

$$
S_{i}^{\alpha, c+1}=\frac{S_{i}^{\alpha, c}+X_{\alpha} \cdot \Delta}{\sqrt{\sum_{\alpha}\left(S_{i}^{\alpha, c}+X_{\alpha} \cdot \Delta\right)^{2}}},\qquad(5)
$$

where $X_{\alpha}$ are random numbers satisfying $-1 \leq X_{\alpha} \leq$ 1. Then the energy change $\delta E$ produced by this move is calculated from Eqs. (1) and (2). If $\delta E \geq 0$, one compares $\exp (-\delta E / k_{B} T)$ with a random number $\varsigma, 0 \leq \varsigma \leq 1$. If $\varsigma<\exp (-\delta E / k_{B} T)$ or $\delta E<0$, the trial configuration is accepted as new configuration, otherwise it is abandoned and the old one is counted once more. It is shown [11] that this prescription leads to

$$
\langle f\rangle=\lim _{L \rightarrow \infty} \bar{f}.\qquad(6)
$$

Since one uses a finite $L$, it is essential to choose the arbitrary step parameter $\Delta$ suitably so as to exclude an appropriate number of initial configurations from the average (4), and to estimate the "statistical error" in a reliable way. In our case, we always start with a configuration of randomly oriented spins and adjust $\Delta$ so that $75\%$ of the moves were successful, and it turned out that about 3000 Monte-Carlo steps per spin were sufficient to yield an accuracy of a few percent for the local magnetisation.

It is well known, of course, that spontaneous symmetry breaking, which is usually accompanied by a change from a disordered state at high temperatures to a spontaneously ordered state at temperatures below the critical one, can occur only in the thermodynamic limit. In a finite magnetic system the magnetisation at zero field

$$
\mathbf{m}(T, H=0)=\frac{1}{N} \sum_{i=1}^{N}\left\langle\mathbf{S}_{i}\right\rangle_{T, H=0}\qquad(7)
$$

vanishes at all nonzero temperatures irrespective of the number $N$ of spins in the system. In particular, even above the critical temperature (of the bulk system) a small magnetisation is found by Monte Carlo calculations, due to fluctuations which in a finite system observed over a finite time have not completely averaged out [11]. However, at very low temperatures there exist, even in an inhomogeneous system, clusters of spins aligned with respect to each other, and there should exist an intrinsic magnetisation. This is usually defined as follows

$$
M=\sqrt{\left\langle\left(\frac{1}{N} \sum_{i=1}^{N} \mathbf{S}_{i}\right)^{2}\right\rangle}.\qquad(8)
$$

Of course, in a finite system the magnetisation $M$ is nonzero at all temperatures. Even at temperatures well above the critical temperature one still obtains $M \propto 1/\sqrt{N}$, and this leads to the appearance of a magnetisation tail at high temperatures. The magnetisation $M$ tends to that of the bulk system (infinite size) in the limit $N \rightarrow \infty$. In the present case, we calculate the magnetisation defined in (8) for the core and surface by summing over the corresponding spins.

Anisotropy energies : In both cases of a spherical and ellipsoidal particle, we consider a uniaxial anisotropy in the core and single-site anisotropy on the surface. The easy axis in the core is chosen along our $z$ reference axis, and the sites on the boundary have uniaxial anisotropy,

with equal anisotropy constant $K_s$, whose axes $\mathbf{e}_i$ are chosen to point outward and normal to the surface ([9], [12]). More precisely, we define for each spin a unit gradient vector on which the spin magnetic moment has to be projected. In the case of a spherical particle these anisotropy axes are along the radius joining the center of the particle to the considered surface site. For an ellipsoidal particle the easy direction in the core is taken along the major axis of the ellipsoid, which is also along the $z$ direction. The bulk anisotropy constant was estimated by many authors (see e.g. [13] and references therein) to be $K_1 \simeq 4.7 \times 10^4 \mathrm{erg} / \mathrm{cm}^3$. In our simulations we normalized this constant to the number of sites and in units of K, $k_c \equiv\left(K_c / k_B\right) \simeq 8.13 \times 10^{-3} K$, $k_B$ being the Boltzmann constant. On the other hand, the surface anisotropy has not been determined experimentally in magnetic oxides, but it has become clear, however, that the corresponding contribution is very large as compared with the bulk one. In our calculations we took $k_s \equiv\left(K_s / k_B\right) \simeq 0.5 \mathrm{~K}$; the corresponding surface anisotropy constant $K_s$ was estimated to be $\simeq 0.06 \mathrm{erg} / \mathrm{cm}^2$ (see [14], [15]). In [9] $k_s$ was taken in the range $1-4 \mathrm{~K}$, but for these higher values of surface anisotropy the authors obtained high-field irreversibility whereas the experimental results (also presented in [9]) show none for the $\gamma-\mathrm{Fe}_2 \mathrm{O}_3$ particles.

Finally, in the case of a very small ellipsoidal particle, as discussed at the beginning of sect.2.A, the effect of the dipolar interactions $\mathcal{H}_{\text {dip }}$ boils down to a mere shape anisotropy, which is absent in a spherical particle. Therefore, the magnetostatic energy of an ellipsoid of semi-axes $\frac{X}{2}, \frac{Y}{2}, \frac{Z}{2}$, can be written as [2], [3]

$$
E_{\text {mag }}=\frac{1}{2 V}\left(D_{x} \cdot M_{x}^{2}+D_{y} \cdot M_{y}^{2}+D_{z} \cdot M_{z}^{2}\right) \quad(9)
$$

where $D_{\alpha}, \alpha=x, y, z$, are the demagnetizing factors, $M_{\alpha}$ the components of the net magnetisation, and $V$ the volume of the particle, which is equal to $N_{t}$ in our calculations. If all semi-axes are different it is not possible to express the $D^{\prime} s$ in closed form. However, this is possible in the case of a prolate or oblate spheroid. In the case of a prolate spheroid, as is very common in permanent-magnet materials, i.e. $Z>X=Y$, the demagnetizing factors are given by [16]

$$
\begin{gathered}
D_{z}=4 \pi \frac{1-e^{2}}{2 e^{3}}\left[\log \left(\frac{1+e}{1-e}\right)-2 e\right], \quad(10) \\
D_{x}=D_{y}=\frac{1}{2}\left(4 \pi-D_{z}\right),
\end{gathered}
$$

where $e=\sqrt{1-(X / Z)^2}, 0<e<1$, is the eccentricity of the ellipsoid. In these calculations we assumed that the easy axes of the magnetocrystalline and shape anisotropy are the same, though this is not the case in general.

We have found that using the long-range dipolar interactions $\mathcal{H}_{\text {dip }}$ involving all possible pairs of atoms in the particle, or the macroscopic magnetostatic energy $E_{\text {mag }}$ yields within numerical errors, the same results, only that the former contribution is much more time consuming than the latter.

### 2.3 Results and discussion

#### 2.3.1 Thermal variation of the magnetisation

In Figs. 3a-c, we plot the computed thermal variation of the core and surface contributions to the magnetisation (per site) as a function of the reduced temperature $\tau^{\text {core }} \equiv$ $T / T_{c}^{\text {core }}, T_{c}^{\text {core }}$ being the highest core "critical temperature", for $N_{t}=909,2009,3766$ with $N_{s t}=53 \%, 46 \%, 41 \%$, respectively. These values of $N_{s t}$ have been determined by the fact that the thickness of the surface shell is constant $(\sim 0.35 \mathrm{~nm})$, according to Mössbauer-effect analysis [6]. They correspond to a diameter of circa 4,4.6 and 6  nm, respectively.

In Fig. 3d we plot the mean magnetisation defined as $M_{\text {mean }} \equiv\left(N_{s} M_{\text {surface }}+N_{c} M_{\text {core }}\right) / N_{t}$ as a function of $\tau^{\text {core }}$, for the same values of $N_{s t}$ as before. The exchange coupling in the core (i.e. $J_{A A}, J_{A B}, J_{B B}$ ), generically denoted by $J_{c}$, are taken as 10 times those on the surface, denoted by $J_{s}$. Since there is no experimental estimation of the exchange couplings on the surface, the choice of such $J_{s}$ was guided by the fact that the critical temperature of the bulk material is circa 906  K, while the hypothetical "surface transition" occurs in the temperature range of $30-75 \mathrm{~K}$ (which is a factor of more than 10 smaller) according to Mössbauer spectroscopy and high-field magnetisation measurements. Nevertheless, we have also considered the effect of other ratios $J_{c} / J_{s}$ (see below). We see that the surface "critical region", corresponding to the would-be magnetic phase transition on the surface is in a range of temperatures lower than the critical temperature of the core. This is expected from the fact that since the molecular field acting on a surface spin is lower than the one acting on a core spin, as a consequence of the lower coordination number at the surface and hence the change in crystal field thereon [1], [17], and also because of the fact that $J_{s}$ are taken smaller than $J_{c}$. This is in agreement with the results of Mössbauer spectroscopy and the magnetisation measurements at high fields, since the surface component has a "critical temperature" in the range $30-75 \mathrm{~K}$ while for the core component the critical temperature is much higher $(\simeq 906 \mathrm{~K})$. Note that both transitions are smeared because of the finiteness of the system size (see discussion after Eq.(8)). We also note that the surface magnetisation $M_{\text {surface }}$ decreases more rapidly than the core contribution $M_{\text {core }}$ as the temperature increases, and has a positive curvature while that of $M_{\text {core }}$ is negative, as is most often the case. Moreover, it is seen that even the (normalized) core magnetisation per site does not reach its saturation value of 1 at very low temperatures, and this can be explained by the fact that the magnetic order in the core is disturbed by the relative disorder on the surface, or in other words, the magnetic disorder starts at the surface and gradually propagates into the core of the particle (see Fig. 6 below). The magnetic disorder on the surface is, of course, enhanced by the single-site surface anisotropy which tends to orientate the spins normal to the surface. In Fig. 3d we see that the more important is the surface contribution the more

![](./images/867747407591375369_3.jpg)

Fig. 3. Thermal variation of the surface and core magnetisation (per site) (Figs.3a-c) and mean magnetisation (Fig.3d) as obtained from the Monte Carlo simulations of an ellipsoidal nanoparticle. The anisotropy constants are given in the text; the exchange interactions on the surface are taken to be 1/10 times those in the core.

enhanced and rapid is the raising of the mean magnetisation at low temperatures, and this behaviour bears some resemblance to Fig. 1c.

In Fig. 4 we plot the core magnetisation of an ellip- soidal nanoparticle with $N_t = 909, 3766, 6330$ and the magnetisation of the isotropic system with the spinel structure and periodic boundary conditions $^1$ as functions of the reduced temperature $\tau^{PBC} \equiv T/T_c^{PBC}$, and $N_{st} = 53\%, 41\%, 26\%$. Comparing the different curves, it is seen that both the critical temperature and the value of the magnetisation are dramatically reduced in the core of the particle. The reduction of the critical temperature is obviously due to the finite-size and surface effects [11]. There is a size-dependent reduction of the critical temperature by up to 50% for the smallest particle. The same result has been found by Hendriksen et al.[18] for small clusters of various structures (bcc, fcc, and disordered) using spin-wave theory. As to the magnetisation, the reduction shows that the core of the particle does not exhibit the same magnetic properties as the bulk material, and as discussed before, it is influenced by the misaligned spins on the surface. In Fig. 4 we can also see that the higher $N_t$ the lower the magnetisation in the critical region and the higher the temperature at which the magnetisation approaches zero, and this is consistent with the fact that $M \propto 1/\sqrt{N_t}$ at high temperatures, as discussed earlier. However, the increase of the critical temperature with $N_t$ is not as clear-cut as it could be expected, and this can be understood by noting that the disordered surface ($J_s = J_c/10$, small coordination numbers, and single-site anisotropy) strongly influences the magnetic order in the core through the relatively strong exchange couplings between surface and core spins, which are equal to those in the core.

![](./images/867747407591375369_4.jpg)

Fig. 4. Thermal variation of the magnetisation of the PBC system with $N_t = 40^3$, and the core magnetisation for $N_t = 909, 3766, 6330$ with $N_{st} = 53\%, 41\%, 26\%$, respectively, as functions of $\tau^{PBC}$ (see text). The exchange interactions on the surface are taken equal to 1/10 times those in the core.

### 2.3.2 Effect of the ratio $J_c/J_s$

In Fig. 5 we plot the thermal variation of the surface magnetisation as a function of the reduced temperature $\tau^{core}$ for $J_s = J_c/2, J_c$ and $2J_c$, and $N_t = 5269, N_{st} = 40\%$. Here the thickness of the surface shell is greater than 0.35

---
$^1$ This system is a perfectly ferrimagnetic material with periodic spinel structure and without vacancies, though such material does not exist in reality since all spinels present some degree of vacancy. This system will be referred to in the sequel as the PBC system.

![](./images/867747407591375369_5.jpg)

Fig. 5. The computed thermal variation of the surface contribution to the net magnetisation of an ellipsoidal nanoparticle as a function of $\tau^{core}$ for $J_s = J_c/2, J_c, 2J_c$ (see text).

![](./images/867747407591375369_6.jpg)

Fig. 6. Spatial variation of the local magnetisation of a spherical nanoparticle of 3140 spins, as a function of the radial distance, for $\tau^{core} \ll 1$, $\tau^{core} = 0.5$, and $\tau^{core} \simeq 1^-$.

nm, and is not taken from experiments, contrary to the values in Figs. 3. The reason for taking such $N_{st}$ is merely to compare the results for surfaces with different thickness. At any rate, our aim here is to maintain $N_{st}$ fixed to a given value and vary the ratio $J_c/J_s$. We see that the surface critical region is shifted to higher temperatures upon increasing $J_s$, and only when $J_s = 2J_c$ that both the core and surface magnetic "phase transitions" occur in the same temperature range, i.e. $\tau^{core} \simeq 1$. It is worth noting that the weaker the exchange interactions on the surface the lower the magnetisation of the latter. This result remains the same upon lowering the surface width. In this case the number of spins having smaller coordination numbers, and hence weaker effective exchange energy, i.e. those spins on the outer shell of the particle, is very small as compared with the rest of spins in the particle. Moreover, we may think that the spins on the outer shell follow the (strong) molecular field created by the other (inner) spins constituting a relatively ferrimagnetically ordered core. Setting $J_c = \lambda J_s$, we may determine the coefficient $\lambda$ at which the transition regions of the core and surface overlap. This may be done using the simple, though time consuming, cumulant method introduced a few years ago by Binder (see [11] for a review).

### 2.3.3 Profile of the magnetisation

We have determined the spatial variation of the local magnetisation of a spherical particle of a fixed radius as we move from the center out onto the surface, at different temperatures. At nearly zero temperature ($\tau^{core} \ll 1$), the local magnetisation decreases with increasing radial distance in the particle. It starts from the saturation value of an iron atom (in fact, we computed the mean value of A and B atoms, to take into account the possibility of starting at either atom) at the center of the particle and decreases down to the value of a surface atom. Note that what is plotted in Fig. 6 is in fact the (normalized) projection of the atomic magnetic moment along the easy axis (z-axis for the core, and normal for the surface spins), which is proportional to $\cos\theta$, and thus Fig. 6 also shows the spatial evolution of the orientation of the magnetic moment inside the particle as the radial distance is varied. The decreasing of the local magnetisation confirms what was said before, that is even at very low temperature the surface is in a magnetic order which is different from that in the core, and as discussed earlier, the misalignement of spins starts at the surface and gradually propagates into the core. This could be related with the gradual canting of spins confirmed by Mössbauer spectroscopy [4], [5], [6] even at 4.2 K. As the temperature increases ($\tau^{core} = 0.5, \tau^{core} \simeq 1^-$), the local magnetisation exhibits a jump of temperature-dependent height, and continues to decrease. Since the local magnetisation depends on the direction of the radius vector, especially in an ellipsoidal particle, the curves in Fig. 6 present, in addition to the usual numerical inaccuracy (especially for $\tau^{core} \simeq 1^-$), some fluctuations due to the spatial non homogeneities inherent to the lacunous spinel structure of the $\gamma$-Fe$_2$O$_3$ particles ($\frac{1}{3}$ for each two B atoms, randomly distributed).

### 2.3.4 Specific heat

In Fig. 7 we plot the computed specific heat of the PBC system ($N_t = 40^3$) and that of an ellipsoidal nanoparticle with $N_t = 909, 3766, 6330$ (with the corresponding values of $N_{st}$ given earlier). There is a transition marked by a sharp peak for the PBC system and a broad peak for the three particle sizes. This broadening is an obvious illustration of the finite-size effects. Note also the shift by 50% to

![](./images/867747407591375369_7.jpg)

Fig. 7. Thermal variation of the specific heat of the PBC system with $N_t=40^3$, and that of an ellipsoidal nanoparticle with $N_t=909,3766,6330$, and for the same energy parameters as in Figs. 3).

lower temperatures of the critical region, as in the mag- netisation thermal behaviour in Fig. 4. We are intending to prepare appropriate samples for the specific heat mea- surements. To our knowledge, such measurements have never been performed on nanoparticle assemblies.

## 3 Conclusion
We have presented a microscopic model for magnetic nano- scale particles including exchange and dipolar interactions, and bulk and surface anisotropy, and investigated the ther- mal and spatial behaviours of the core and surface mag- netisation of a nanoparticle of different sizes, and hence of different surface contributions. We have found that the finiteness of the system size and free boundaries lead to a non uniform magnetisation profile decreasing toward the surface in the particle. Moreover, it turns out that surface anisotropy also leads to non saturation of the magnetisa- tion at low temperatures.

In order to compare our results obtained for a single nanoparticle with our experiments on dilute assemblies of nanoparticles [7], and in particular to compare with the curve of magnetisation vs. temperature given in Fig. 1b, we have to include the Zeeman energy term in our Hamil- tonian and run our program for different particle sizes with randomly distributed easy axes. Unfortunately, this will require several days of CPU time, since a temperaturesweep takes about 30 hours (without dipolar interactions) on a two-processor Alpha Work Station. It also remains to study the interplay between finite-size and surface effects in a nanoparticle of round shape (sphere or ellipsoid), as is the case here, since for a box-shaped particle one can treat separately finite-size and surface effects by consider- ing both cases of free boundaries where these two effects are mixed and that of periodic boundary conditions where only the former are present. In the present case, it can be seen from Fig. 4 that the magnetisation of the PBC system where only finite-size effects are present is larger than the bulk magnetisation, while the magnetisation of a (anisotropic) nanoparticle is lower. This implies, as was analytically shown in [19] for a box-shaped particle with simple-cubic structure, that finite-size effects yield a posi- tive contribution to the magnetisation while surface effects render a larger and negative contribution, resulting in a net magnetisation that is lower than that of the bulk sys- tem. In [20] it was also shown that the difference between the finite-size and surface contributions is enhanced by surface anisotropy, which leads to non saturation of the magnetisation at low temperatures (see Figs. 3-5). Nev- ertheless, already from the present single-particle prelimi- nary study we can infer some conclusions about the effect of the magnetically disordered surface on the global mag- netic properties of nanoparticles. The surface contribution to the magnetisation presents a rather different behaviour from the core contribution. Furthermore, even at very low temperatures, the local magnetisation decreases with the distance from the center, showing that the magnetic state on the surface is definitely different from that in the core. We have also shown that there is a drastic reduction of both the critical temperature and the value of the mag- netisation in the core of the particle. The reduction of the critical temperature is obviously due to the finite-size and surface effects. As to the magnetisation, the reduc- tion shows that the magnetic properties of the particle core are different from those of bulk material, because of the strong influence of the misalignement of spins on the surface, driven by symmetry breaking of the cristal field and surface anisotropy, which propagates from the bound- ary into the core. Finally, we note that our results on the thermal and spatial behaviour of the magnetisation are in qualitative agreement with those obtained by Binder et al. [21] for spherical particles with simple-cubic crystalline structure.

## Acknowledgments
HK thanks L. Reynaud for his considerable help in these simulations and D. Garanin for his valuable remarks and suggestions. The present numerical calculations have been performed on the Alpha Work Station of the Genome Laboratory of the University of Versailles to which we are greatly endebted.

## References
1. R. E. De Wames and T. Wolfram, Progress in Surface Sci- ences 2, ed. by S.G. Davison, Oxford Pergamon, 1972, p.23; T. Kaneyoshi, J. Phys. Cond. Mat. 3 (1991) 4497-4522; D. Garanin, J. Phys. A: Math. Gen. 29 (1996) L257-L262; D. Garanin, "Semi-infinite anisotropic spherical model: Cor- relations at $T \geq T_{c}$", submitted to Phys. Rev. E, January1998.
2. A.I. Akhiezer, V.G. Bar'yakhtar and S.V. Peletminskii, Spin waves, North-Holland Publ. Company, 1968.

3. A. Aharoni, *Introduction to the theory of ferromagnetism*, Oxford Science Pubs., 1996.

4. K. Haneda, Can. J. Phys. **65** (1987) 1233, and references therein.

5. J.M.D. Coey, Phys. Rev. Lett. **27** (1971) 1140.

6. P. Prené et al., Hyperfine Int. **93** (1994) 1049; P. Prené, Ph.D. thesis of the Université Pierre & Marie Curie, July 1995; E. Tronc et al., Hyp. Int. **112** (1998) 97.

7. A. Ezzir, Ph.D. thesis of the Université de Paris XI-Orsay, December 1998.

8. J.P. Chen et al., Phys. Rev. B **51** (1995) 11527.

9. R. H. Kodama, A. E. Berkovitz, E.J. Mcniff, and S. Foner, Phys. Rev. Lett. **77** (1996) 394; R. H. Kodama and A. E. Berkovitz, *"Atomic-Scale Magnetic Modeling of Oxide Nanoparticles"*, Phys. Rev. **B59** (1999) 6321; and references therein.

10. J. S. Smart, in *Magnetism*, eds. G.T. Rado and H. Suhl, Academic Press New York 1963, p.63.

11. K. Binder and D.W. Heermann, *"Monte Carlo simulation in statistical physics"*, Springer-Verlag, Berlin 1992; K. Binder, Physica **62** (1972) 508-526; K. Binder and D. Landau, Surface Science **151** (1985) 409-429.

12. D. A. Dimitrov and G. M. Wysin, Phys. Rev. B **50** (1994) 3077; *ibid* **51** (1994) 11947.

13. S. Krupicka and K. Zaveta, in *Magnetic Oxides*, Part I, ed. D.J. Craik, A Wiley-Interscience Publication, 1975.

14. J.L. Dormann et al., Phys. Rev. **B18** (1996) 1; F. Gazeau et al., Europhys. Lett. **40** (1997) 575.

15. A. Aharoni, J. Appl. Phys. **81** (1997) 830.

16. B.K.P. Scaife, *Principles of dielectrics*, Oxford Science Pubs., 1989.

17. O. Eriksson et al., Phys. Rev. **B45** (1992) 2868-2875.

18. P.V. Hendriksen, S. Linderoth, and P.-A. Lindgard, Phys. Rev. **B48** (1993) 7259.

19. H. Kachkachi and D.A. Garanin, *"Boundary and finite-size effects in small magnetic systems"*, submitted to J. Phys. Condensed Matter.

20. H. Kachkachi, M. Noguès, E. Tronc, and D.A. Garanin, *"Finite-size versus surface effects in nanoparticles"*, cond-mat/9910393, invited paper to 3rd EuroConference on Magnetic Properties of Fine Nanoparticles, Barcelona, October 99, to appear in J. Mag. Mag. Mat..

21. K. Binder, H. Rauch, and V. Wildpaner, J. Chem. Solids **31** (1970) 391; V. Wildpaner, Z. Physik **270** (1974) 215-223.