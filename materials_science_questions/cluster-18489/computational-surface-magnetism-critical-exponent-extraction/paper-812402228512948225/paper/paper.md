# Surface effects in nanoparticles: application to maghemite
$\gamma$-$\text{Fe}_2\text{O}_3$

H. Kachkachi$^{1\mathrm{a}}$, A. Ezzir$^1$, M. Noguès$^1$, and E. Tronc$^2$

$^1$ LMOV$^\text{b}$, Université de Versailles St. Quentin, 45 avenue des États-Unis, 78035 Versailles Cedex, France
$^2$ LCMC$^\text{c}$, Université Pierre & Marie Curie, 4 place Jussieu, 75252 Paris Cedex, France

Received 1 September 1999 and Received in final form 3 November 1999

**Abstract.** We present a microscopic model for nanoparticles, of the maghemite ($\gamma$-Fe$_2$O$_3$) type, and perform classical Monte Carlo simulations of their magnetic properties. On account of Mössbauer spectroscopy and high-field magnetisation results, we consider a particle as composed of a core and a surface shell of constant thickness. The magnetic state in the particle is described by the anisotropic classical Dirac-Heisenberg model including exchange and dipolar interactions and bulk and surface anisotropy. We consider the case of ellipsoidal (or spherical) particles with free boundaries at the surface. Using a surface shell of constant thickness ($\sim0.35$ nm) we vary the particle size and study the effect of surface magnetic disorder on the thermal and spatial behaviors of the net magnetisation of the particle. We study the shift in the surface "critical region" for different surface-to-core ratios of the exchange coupling constants. It is also shown that the profile of the local magnetisation exhibits strong temperature dependence, and that surface anisotropy is responsible for the non saturation of the magnetisation at low temperatures.

**PACS.** 75.50.Tt Fine particle systems – 75.30.Pd Surface magnetism – 75.10.Hk Classical spin models

## 1 Introduction
Surface effects in a nanoparticle are of great importance since they dominate the magnetic properties and become more important with decreasing size of the particle. In particular, the picture of a single-domain magnetic particle where all spins are pointing into the same direction, leading to coherent relaxation processes, is no longer valid when one considers the effect of misaligned spins on the surface on the global magnetic properties of the particle. Indeed, even for strong exchange interactions the surface is responsible for coordination defects, and in a particle of radius of the order of 4 nm, 50% (in the $\gamma$-Fe$_2$O$_3$ nanoparticles) of atoms lie on the surface, and therefore the effect of the latter cannot be neglected.

The magnetisation near the surface is generally lower than in the interior. This effect leads to a thermodynamic perturbation in exchange interactions near the surface, which can be sizable at high temperatures. In a finite system, the effect of temperature introduces, in addition to the usual renormalization of the spin-wave spectrum, a spatial dependence of the magnetisation (see [1] and references therein for the case of semi-infinite cubic crystals). Indeed, the symmetry breaking at the surface results in a surface anisotropy. In most cases, this happens to be strong enough as to compensate for the work needed against the exchange energy that prefers full alignment, and it is conceivable then that the magnetisation vector will point along the bulk easy axis in the core of the particle, and will then gradually turn into a different direction when it approaches the surface. In addition to the exchange interactions, which are the strongest interactions between atoms in a magnetic system, there are also the purely magnetic dipole interactions between the magnetic moments of the atoms and the interactions between the magnetic moments and the electric field of the crystal lattice (spin-orbit interactions). The last two types of interactions are relativistic in origin and therefore correspond to energies that are much smaller than the exchange energy on a short length scale, but as they are long range interactions they lead, in general, to non negligible contributions. Indeed, these interactions play an important role in that they introduce a preferred direction in the system as they correspond to a Hamiltonian (see below) that is not invariant under rotation operations. In other words, they lead to the appearance of an anisotropy energy, *i.e.* the dependence of the total energy of the system on the direction of magnetisation. Moreover, the most important feature of the relativistic interactions is that they change the magnetic moment of an atom from one site to another, and hence introduce a non uniform spatial distribution of the magnetic moment in the system. The treatment of the dipole-dipole interactions [2] leads to two energy

$^\text{a}$ e-mail: kachkach@physique.uvsq.fr
$^\text{b}$ CNRS UMR 8634
$^\text{c}$ CNRS URA 1466

terms corresponding to the volume and surface charges. In a small magnetic system, such as a nanoparticle, only the second contribution is important since it accounts for the shape anisotropy, and the former becomes negligible as one integrates over a small volume (see a detailed dis- cussion in [3] and references therein).

Therefore, it is necessary to take into account all dif- ferent contributions to the energy, exchange and dipolar interactions, bulk and surface anisotropies, in any study of spatial distributions of the magnetisation in a small magnetic system.

One of our ultimate goals is to understand the effect of surfaces on the thermodynamic and spatial behaviors of the magnetisation in small systems, since this is also of crucial importance to the study of the dynamics of such systems where the surface effects are considerable. In this case, the dynamics is rendered more complicated by the additional (metastable or stable) magnetic states corre- sponding to the surface configurations.

According to Mössbauer spectroscopy performed by Morrish et al. (see [4] for a review, and also the semi- nal work by Coey [5]), the iron cations at the surface of the $\gamma$-Fe₂O₃ particles have a noncolinear magnetic struc- ture from 4.2 K to room temperature. The Mössbauer- spectroscopy analysis performed in [6] on $\gamma$-Fe₂O₃ par- ticles show that the spectrum contains two components, one associated with the bulk and the other with iron atoms on the surface. The latter seems to disappear at temper- atures in the range 30-75 K, depending on the mean di- ameter of the particle assembly. From these Mössbauer- effect analyses it was also inferred that the surface shell has a thickness of about 0.35 nm, independently of the particle volume. This fact will be used in our simulations to determine the ratio of the surface and core number of atoms. In addition, measurements of the magnetisation at high fields performed on the $\gamma$-Fe₂O₃ nanoparticles [7] (see also [8] for cobalt particles) have shown that the mag- netisation is strongly influenced by the surface effects, de- pending on the particle size. In Figure 1 we show the field and thermal variation of the magnetisation for different particle sizes. In Figure 1a we see that there is a sudden increase of the magnetisation as a function of the applied field when the temperature reaches 70 K, and that the magnetisation does not saturate at the highest field value, i.e. 5.5 T. In Figure 1b there is an important increase of the magnetisation at low temperatures. In Figure 1c the thermal behaviour of the magnetisation at 5.5 T is shown for samples with different mean diameter. There we see that the smaller is the mean diameter of the particle the more important is the increase of the magnetisation at very low temperatures. This can be explained by the fact that the surface component corresponds to a state with canted atomic moments at low temperatures [5,6].

Furthermore, open hystereses were observed [9] in the nickel ferrite particles (NiFe₂O₄) up to fields of 16 T, while the anisotropy field of the bulk sample is ut- most $4 \times 10^{-2}$ T. The authors consider that the core spins are colinear whereas those on the surface are mis- aligned. In the case of $\gamma$-Fe₂O₃ particles, however, no such irreversibility in the magnetisation hysteresis loop was observed [6,9].

Therefore, according to Mössbauer spectroscopy and high-field magnetisation measurements, we may think of a particle as containing a magnetically disordered surface of a certain width and a core more or less ordered depending on the size of the particle. The net magnetisation of the particle is given by the (weighed) sum of the contributions from the surface and the core. The increase of the surface contribution at low temperatures becomes more important with decreasing size of the particle, as shown in Figure 1c.

In this work, we compute the thermal behavior of the different contributions to the magnetisation due to the surface and core for different values of exchange couplings and different surface-to-volume ratios of the number of spins. We also compute the spatial variation of the mag- netisation at different temperatures and the specific heat for different sizes. All calculations are performed in zero magnetic field.

## 2 Model for magnetic particles

### 2.1 Hamiltonian
As was discussed in the introduction, it is well- established [2,3] that any theory dealing with the spatial magnetisation distribution must consider all three energy contributions, exchange, anisotropy and magnetostatic, and that there is no obvious reason for neglecting any one of these. However, it should be emphasised that in very small particles the exchange interactions are too strong to allow for subdivision into domains, so that the magne- tostatic energy term is considered here only in order to account for the shape anisotropy in the case of ellipsoidal particles. It should also be stressed, as discussed in the in- troduction, that because of the surface anisotropy and the symmetry breaking at the surface, there is no reason to consider the exchange interactions on the surface as equal to those in the core, and thereby the particle may acquire a non uniform distribution of the magnetisation.

Therefore, to take account of all these energy con- tributions, we propose a model, based on the classi- cal anisotropic Dirac-Heisenberg (exchange and dipolar) Hamiltonian, describing the spinel structure of the (spher- ical or ellipsoidal) ferrimagnetic nanoparticles (e.g., $\gamma$- Fe₂O₃). In this article the calculations are performed us- ing classical Monte Carlo simulations of the magnetisation thermal behavior of the particle with open boundaries at the surface.

So, the exchange, anisotropy and Zeeman contri- butions are given by the following anisotropic Dirac- Heisenberg Hamiltonian
$$
\begin{aligned}
\mathcal{H}_{\mathrm{DH}}= & -\sum_{i, \mathbf{n}} \sum_{\alpha, \beta=\mathrm{A}, \mathrm{B}} J_{\alpha \beta} \mathbf{S}_{i}^{\alpha} \cdot \mathbf{S}_{i+\mathbf{n}}^{\beta}-K \sum_{i=1}^{N_{\mathrm{t}}}\left(\mathbf{S}_{i} \cdot \mathbf{e}_{i}\right)^{2} \\
& -\left(g \mu_{\mathrm{B}}\right) H \sum_{i=1}^{N_{\mathrm{t}}} \mathbf{S}_{i},
\end{aligned}
\tag{1}
$$

![](./images/812402228512948225_1.jpg)

Fig. 1. (a) Magnetisation as a function of the magnetic field of a diluted assembly of $\gamma$-Fe$_2$O$_3$ nanoparticles with a mean diameter of 2.7 nm. (b) Thermal variation of the magnetisation extracted from a) at a field of 55 kOe. (c) Thermal variation of the magnetisation in a field of 55 kOe for three samples with different mean diameters (2.7, 4.8, 7.1 nm).

where $J_{\alpha\beta}$ (positive or negative) are the exchange coupling constants between (the $\alpha,\beta=$ A,B) nearest neighbors spanned by the unit vector $\mathbf{n}$; $\mathbf{S}_i^\alpha$ is the (classical) spin vector of the $\alpha$th atom at site $i$; $H$ is the uniform field applied to all spins (of number $N_\text{t}$) in the particle, $K>0$ is the anisotropy constant and $\mathbf{e}_i$ the single-site anisotropy axis (see definition below). A discussion of the core and surface anisotropy will be presented below. In the sequel the magnetic field will be set to zero.

To the Dirac-Heisenberg Hamiltonian we add the pairwise long-range dipolar interactions

$$
\mathcal{H}_{\text{dip}} = \frac{(g\mu_{\text{B}})^2}{2} \sum_{i\neq j} \frac{(\mathbf{S}_i \cdot \mathbf{S}_j) R_{ij}^2 - 3 (\mathbf{S}_i \cdot \mathbf{R}_{ij}) \cdot (\mathbf{R}_{ij} \cdot \mathbf{S}_j)}{R_{ij}^5}
\tag{2}
$$

where $g$ is the Landé factor, $\mu_{\text{B}}$ the Bohr magneton and $\mathbf{R}_{ij}$ the vector connecting any two spins on sites $i$ and $j$ of the particle, $R_{ij} \equiv \|\mathbf{R}_{ij}\|$.

### 2.2 Method of simulation

The particle we consider here is a spinel with two different iron sites, a tetrahedric $\text{Fe}^{3+}$ site (denoted by A) and an octahedric $\text{Fe}^{3+}$ site (denoted by B). The nearest neighbor exchange interactions are (in units of K) [10,9]: $J_{\text{AB}}/k_{\text{B}} \simeq -28.1$, $J_{\text{BB}}/k_{\text{B}} \simeq -8.6$, and $J_{\text{AA}}/k_{\text{B}} \simeq -21.0$. These coupling constants are used in the Dirac-Heisenberg Hamiltonian $\mathcal{H}_{\text{DH}}$ in order to model the phase transition from the paramagnetic to ferrimagnetic order as the temperature is lowered down to zero through $T_c \simeq 906$ K. In the spinel structure an atom on site A has 12 nearest neighbors on the sublattice B and 4 on the sublattice A, and an atom on site B has 6 nearest neighbors on A and 6 on the B sublattice; the number of B sites is twice that of sites A. The nominal value of the spin on sites A and B is $5/2$, and this justifies the use of classical spins. We have also taken account of $\frac{1}{3}$ of lacuna for each two B atoms randomly distributed in the particle. The nanoparticle we have studied contains $N_\text{t}$ spins ($\simeq 10^3 - 10^5$), and its radius is in the range 2-3.5 nm. Our model is based on the hypothesis that the particle is composed of a core of radius containing $N_\text{c}$ spins, and a surface shell surrounding it that contains $N_\text{s}$ spins, so that $N_\text{t}=N_\text{c}+N_\text{s}$. Thus varying the size of the particle while maintaining the thickness of the surface shell constant ($\sim 0.35$ nm), is equivalent to varying the surface to total number of spins, $N_{\text{st}}=N_\text{s}/N_\text{t}$, and this allows us to study the effect of surfaces of different contributions. All spins in the core and on the surface are identical, but interact *via* the, *a priori*, different couplings depending on their locus in the whole volume. We will consider both cases of identical interactions, and that of the general situation with different interactions on the surface and in the core. Although we treat only the crystallographically "ideal" surface, we do allow for perturbations in the exchange constants on the surface. This is meant to take into account, though in a somewhat phenomenological way, the possible defects on the surface, and the possible interactions between the particles and the matrix in which they are embedded. In [9] it was assumed that the pairwise exchange interactions are of the same magnitude for the core and surface atoms, but there was postulated the existence of a fraction of missing bonds on the surface. On the other hand, we consider that the exchange interactions between the core and surface spins are the same as those inside the core. We also stress that we are only concerned with non interacting particles, so we ignore the effect of interparticle interactions on the exchange couplings at the surface of the particle.

In our simulations we start with a regular box ($X \times Y \times Z$) of spins with the spinel structure having

![](./images/812402228512948225_2.jpg)

Fig. 2. Normalized distribution of the coordination number in
a spherical and ellipsoidal particle for $N_{\text{st}} = 40\%$.

the properties mentioned above, and then given the ra-
dius or total number of spins in the particle, we cut in a
sphere or an ellipsoid. We choose the center of the particle
to lie at one of the lattice sites. In all cases free bound-
ary conditions are used, and thus a spin is considered as a
core or surface spin depending on whether it has or not its
full coordination number. Figure 2 shows the distribution
of the coordination numbers in a spherical and ellipsoidal
particle.

Therefore, in our simulations each spin has a structure
associated with it that contains the coordinates of the cor-
responding site, the nature of the site in the spinel struc-
ture (i.e. A or B), its locus (core or surface), the number of
its nearest neighbors, and the total number of such sites.
Thus, once the structure of each spin is defined, the spins
outside of the sphere or the ellipsoid are discarded. This
accomplishes the simulation of the crystal structure and
shape of the particle. Next, we proceed with the Monte
Carlo calculations.

The classical Monte Carlo method based on the
Metropolis algorithm is now a standard method and
detailed descriptions can be found in [11]; so here we sum-
marize only the main procedure. We calculate the expec-
tation value of a function $f(\{\mathbf{S}_{i}\})$ of the spins $\mathbf{S}_{i}$
$$
\langle f \rangle = \frac{\mathrm{Tr}\left[\exp(-H/k_{\mathrm{B}}T)f\right]}{\mathrm{Tr}\exp(-H/k_{\mathrm{B}}T)}
\tag{3}
$$
by generating a Markov chain of spin configurations $\{\mathbf{S}_{i}\}$
of the system and taking the average
$$
\bar{f} = \frac{1}{L} \sum_{c=1}^{L} f(\{\mathbf{S}_{i}^{c}\}).
\tag{4}
$$

From any initial (random in our case) configuration $c$
we generate a trial configuration by choosing the spin
coordinates of a randomly chosen lattice site $i$ by $(\alpha =
x,y,z)$
$$
S_{i}^{\alpha,c+1} = \frac{S_{i}^{\alpha,c} + X_{\alpha} \Delta}{\sqrt{\sum_{\alpha} (S_{i}^{\alpha,c} + X_{\alpha} \Delta)^{2}}},
\tag{5}
$$
where $X_{\alpha}$ are random numbers satisfying $-1 \leq X_{\alpha} \leq 1$.
Then the energy change $\delta E$ produced by this move is cal-
culated from equations (1) and (2). If $\delta E \geq 0$, one com-
pares $\exp(-\delta E/k_{\mathrm{B}}T)$ with a random number $\varsigma, 0 \leq \varsigma \leq 1$.
If $\varsigma < \exp(-\delta E/k_{\mathrm{B}}T)$ or $\delta E < 0$, the trial configuration is
accepted as new configuration, otherwise it is abandoned
and the old one is counted once more. It is shown [11] that
this prescription leads to
$$
\langle f \rangle = \lim_{L \to \infty} \bar{f}.
\tag{6}
$$

Since one uses a finite $L$, it is essential to choose the ar-
bitrary step parameter $\Delta$ suitably so as to exclude an
appropriate number of initial configurations from the av-
erage (4), and to estimate the "statistical error" in a reli-
able way. In our case, we always start with a configuration
of randomly oriented spins and adjust $\Delta$ so that 75% of
the moves were successful, and it turned out that about
3 000 Monte-Carlo steps per spin were sufficient to yield
an accuracy of a few percent for the local magnetisation.

It is well-known, of course, that spontaneous symme-
try breaking, which is usually accompanied by a change
from a disordered state at high temperatures to a sponta-
neously ordered state at temperatures below the critical
one, can occur only in the thermodynamic limit. In a finite
magnetic system the magnetisation at zero field
$$
\mathbf{m}(T, H=0) = \frac{1}{N} \sum_{i=1}^{N} \langle \mathbf{S}_{i} \rangle_{T,H=0}
\tag{7}
$$
vanishes at all nonzero temperatures irrespective of the
number $N$ of spins in the system. In particular, even above
the critical temperature (of the bulk system) a small mag-
netisation is found by Monte Carlo calculations, due to
fluctuations which in a finite system observed over a finite
time have not completely averaged out [11]. However, at
very low temperatures there exist, even in an inhomoge-
neous system, clusters of spins aligned with respect to each
other, and there should exist an intrinsic magnetisation.
This is usually defined as follows
$$
M = \sqrt{\left\langle \left( \frac{1}{N} \sum_{i=1}^{N} \mathbf{S}_{i} \right)^{2} \right\rangle}.
\tag{8}
$$

Of course, in a finite system the magnetisation $M$ is
nonzero at all temperatures. Even at temperatures well
above the critical temperature one still obtains $M \propto
1/\sqrt{N}$, and this leads to the appearance of a magneti-
sation tail at high temperatures. The magnetisation $M$
tends to that of the bulk system (infinite size) in the limit
$N \to \infty$. In the present case, we calculate the magnetisa-
tion defined in (8) for the core and surface by summing
over the corresponding spins.

## Anisotropy energies

In both cases of a spherical and ellispoidal particle, we
consider a uniaxial anisotropy in the core and single-site

anisotropy on the surface. The easy axis in the core is chosen along our $z$ reference axis, and the sites on the boundary have uniaxial anisotropy, with equal anisotropy constant $K_{\mathrm{s}}$, whose axes $\boldsymbol{e}_{i}$ are chosen to point outward and normal to the surface [9,12]). More precisely, we define for each spin a unit gradient vector on which the spin magnetic moment has to be projected. In the case of a spherical particle these anisotropy axes are along the radius joining the center of the particle to the considered surface site. For an ellipsoidal particle the easy direction in the core is taken along the major axis of the ellipsoid, which is also along the $z$ direction. The bulk anisotropy constant was estimated by many authors (see e.g. [13] and references therein) to be $K_{1} \simeq 4.7 \times 10^{4} \mathrm{erg} / \mathrm{cm}^{3}$. In our simulations we normalized this constant to the number of sites and in units of $\mathrm{K}, k_{\mathrm{c}} \equiv\left(K_{\mathrm{c}} / k_{\mathrm{B}}\right) \simeq 8.13 \times 10^{-3} \mathrm{~K}$, $k_{\mathrm{B}}$ being the Boltzmann constant. On the other hand, the surface anisotropy has not been determined experimentally in magnetic oxides, but it has become clear, however, that the corresponding contribution is very large as compared with the bulk one. In our calculations we took $k_{\mathrm{s}} \equiv$ $\left(K_{\mathrm{s}} / k_{\mathrm{B}}\right) \simeq 0.5 \mathrm{~K}$; the corresponding surface anisotropy constant $K_{\mathrm{s}}$ was estimated to be $\simeq 0.06 \mathrm{erg} / \mathrm{cm}^{2}$ (see [14,15]). In [9] $k_{\mathrm{s}}$ was taken in the range 1-4 K, but for these higher values of surface anisotropy the authors obtained high-field irreversibility whereas the experimental results (also presented in [9]) show none for the $\gamma-\mathrm{Fe}_{2} \mathrm{O}_{3}$ particles.

Finally, in the case of a very small ellipsoidal particle, as discussed at the beginning of Section 1, the effect of the dipolar interactions $\mathcal{H}_{\text {dip }}$ boils down to a mere shape anisotropy, which is absent in a spherical particle. Therefore, the magnetostatic energy of an ellipsoid of semi-axes $\frac{X}{2}, \frac{Y}{2}, \frac{Z}{2}$, can be written as [2,3]

$$
E_{\mathrm{mag}}=\frac{1}{2 V}\left(D_{x} M_{x}^{2}+D_{y} M_{y}^{2}+D_{z} M_{z}^{2}\right)
\tag{9}
$$

where $D_{\alpha}, \alpha=x, y, z$, are the demagnetizing factors, $M_{\alpha}$ the components of the net magnetisation, and $V$ the volume of the particle, which is equal to $N_{\mathrm{t}}$ in our calculations. If all semi-axes are different it is not possible to express the $D^{\prime} s$ in closed form. However, this is possible in the case of a prolate or oblate spheroid. In the case of a prolate spheroid, as is very common in permanent-magnet materials, i.e. $Z>X=Y$, the demagnetizing factors are given by [16]

$$
D_{z}=4 \pi \frac{1-e^{2}}{2 e^{3}}\left[\log \left(\frac{1+e}{1-e}\right)-2 e\right],
\tag{10}
$$

$$
D_{x}=D_{y}=\frac{1}{2}\left(4 \pi-D_{z}\right),
$$

where $e=\sqrt{1-(X / Z)^{2}}, 0<e<1$, is the eccentricity of the ellipsoid. In these calculations we assumed that the easy axes of the magnetocrystalline and shape anisotropy are the same, though this is not the case in general.

We have found that using the long-range dipolar interactions $\mathcal{H}_{\text {dip }}$ involving all possible pairs of atoms in the particle, or the macroscopic magnetostatic energy $E_{\text {mag }}$ yields within numerical errors, the same results, only that the former contribution is much more time consuming than the latter.

### 2.3 Results and discussion

#### 2.3.1 Thermal variation of the magnetisation

In Figures 3a-c, we plot the computed thermal variation of the core and surface contributions to the magnetisation (per site) as a function of the reduced temperature $\tau^{\text {core }} \equiv$ $T / T_{\mathrm{c}}^{\text {core }}, T_{\mathrm{c}}^{\text {core }}$ being the highest core "critical temperature", for $N_{\mathrm{t}}=909,2009,3766$ with $N_{\mathrm{st}}=53 \%, 46 \%, 41 \%$, respectively. These values of $N_{\text {st }}$ have been determined by the fact that the thickness of the surface shell is constant $(\sim 0.35 \mathrm{~nm})$, according to Mössbauer-effect analysis [6]. They correspond to a diameter of circa 4,4.6 and $6 \mathrm{~nm}$, respectively.

In Figure 3d we plot the mean magnetisation defined as $M_{\text {mean }} \equiv\left(N_{\mathrm{s}} M_{\text {surface }}+N_{\mathrm{c}} M_{\text {core }}\right) / N_{\mathrm{t}}$ as a function of $\tau^{\text {core }}$, for the same values of $N_{\text {st }}$ as before. The exchange coupling in the core (i.e. $J_{\mathrm{AA}}, J_{\mathrm{AB}}, J_{\mathrm{BB}}$ ), generically denoted by $J_{\mathrm{c}}$, are taken as 10 times those on the surface, denoted by $J_{\mathrm{s}}$. Since there is no experimental estimation of the exchange couplings on the surface, the choice of such $J_{\mathrm{s}}$ was guided by the fact that the critical temperature of the bulk material is circa 906 K, while the hypothetical "surface transition" occurs in the temperature range of 3075 K (which is a factor of more than 10 smaller) according to Mössbauer spectroscopy and high-field magnetisation measurements. Nevertheless, we have also considered the effect of other ratios $J_{\mathrm{c}} / J_{\mathrm{s}}$ (see below).

We see that the surface "critical region", corresponding to the would-be magnetic phase transition on the surface is in a range of temperatures lower than the critical temperature of the core. This is expected from the fact that since the molecular field acting on a surface spin is lower than the one acting on a core spin, as a consequence of the lower coordination number at the surface and hence the change in crystal field thereon [1,17], and also because of the fact that $J_{\mathrm{s}}$ are taken smaller than $J_{\mathrm{c}}$. This is in agreement with the results of Mössbauer spectroscopy and the magnetisation measurements at high fields, since the surface component has a "critical temperature" in the range $30-75 \mathrm{~K}$ while for the core component the critical temperature is much higher ( $\simeq 906 \mathrm{~K})$. Note that both transitions are smeared because of the finiteness of the system size (see discussion after Eq. (8)). We also note that the surface magnetisation $M_{\text {surface }}$ decreases more rapidly than the core contribution $M_{\text {core }}$ as the temperature increases, and has a positive curvature while that of $M_{\text {core }}$ is negative, as is most often the case. Moreover, it is seen that even the (normalized) core magnetisation per site does not reach its saturation value of 1 at very low temperatures, and this can be explained by the fact that the magnetic order in the core is disturbed by the relative disorder on the surface, or in other words, the magnetic disorder starts at the surface and gradually propagates into the core of the particle (see Fig. 6 below). The magnetic disorder on

![](./images/812402228512948225_3.jpg)

Fig. 3. (a)-(c) Thermal variation of the surface and core magnetisation (per site) (Fig. 3d) and mean magnetisation as obtained from the Monte Carlo simulations of an ellipsoidal nanoparticle. The anisotropy constants are given in the text; the exchange interactions on the surface are taken to be 1/10 times those in the core.

the surface is, of course, enhanced by the single-site sur- face anisotropy which tends to orientate the spins normal to the surface. In Figure 3d we see that the more impor- tant is the surface contribution the more enhanced and rapid is the raising of the mean magnetisation at low tem- peratures, and this behavior bears some resemblance to Figure 1c.

In Figure 4 we plot the core magnetisation of an el- lipsoidal nanoparticle with $N_{\rm t}=909, 3766, 6330$ and the magnetisation of the isotropic system with the spinel structure and periodic boundary conditions¹ as functions of the reduced temperature $\tau^{\rm PBC}\equiv T/T_{\rm c}^{\rm PBC}$, and $N_{\rm st}=$ 53%,41%,26%. Comparing the different curves, it is seen that both the critical temperature and the value of the magnetisation are dramatically reduced in the core of the particle. The reduction of the critical temperature is obvi- ously due to the finite-size and surface effects [11]. There is a size-dependent reduction of the critical temperature by up to 50% for the smallest particle. The same result has been found by Hendriksen *et al.* [18] for small clus- ters of various structures (bcc, fcc, and disordered) using spin-wave theory. As to the magnetisation, the reduction shows that the core of the particle does not exhibit the same magnetic properties as the bulk material, and as discussed before, it is influenced by the misaligned spins on the surface.

![](./images/812402228512948225_4.jpg)

Fig. 4. Thermal variation of the magnetisation of the PBC system with $N_{\rm t}=40^{3}$, and the core magnetisation for $N_{\rm t}=$ 909,3766,6330 with $N_{\rm st}=53\% ,41\% ,26\%$, respectively, as functions of $\tau^{\rm PBC}$ (see text). The exchange interactions on the surface are taken equal to 1/10 times those in the core.

In Figure 4 we can also see that the higher $N_{\rm t}$ the lower the magnetisation in the critical region and the higher the temperature at which the magnetisation approaches zero, and this is consistent with the fact that $M\propto 1/\sqrt{N_{\rm t}}$ at high temperatures, as discussed earlier. However, the increase of the critical temperature with $N_{\rm t}$ is not as clear-cut as it could be expected, and this can be under- stood by noting the disordered surface ($J_{\rm s}=J_{\rm c}/10$, small coordination numbers, and single-site anisotropy) strongly influences the magnetic order in the core through

---
¹ This system is a perfectly ferrimagnetic material with peri- odic spinel structure and without vacancies, though such ma- terial does not exist in reality since all spinels present some degree of vacancy. This system will be referred to in the sequel as the PBC system.

![](./images/812402228512948225_5.jpg)

Fig. 5. The computed thermal variation of the surface contri- bution to the net magnetisation of an ellipsoidal nanoparticle as a function of $\tau^{core}$ for $J_{s}=J_{c}/2, J_{c}, 2J_{c}$ (see text).

the relatively strong exchange couplings between surface and core spins, which are equal to those in the core.

### 2.3.2 Effect of the ratio $J_{c}/J_{s}$

In Figure 5 we plot the thermal variation of the surface magnetisation as a function of the reduced temperature $\tau^{core}$ for $J_{s}=J_{c}/2, J_{c}$ and $2J_{c}$, and $N_{t}=5269$, $N_{st}=$ 40%. Here the thickness of the surface shell is greater than 0.35 nm, and is not taken from experiments, contrary to the values in Figure 3. The reason for taking such $N_{st}$ is merely to compare the results for surfaces with different thickness. At any rate, our aim here is to maintain $N_{st}$ fixed to a given value and vary the ratio $J_{c}/J_{s}$.

We see that the surface critical region is shifted to higher temperatures upon increasing $J_{s}$, and only when $J_{s}=2J_{c}$ that both the core and surface magnetic "phase transitions" occur in the same temperature range, *i.e.* $\tau^{core}\simeq 1$. It is worth noting that the weaker the exchange interactions on the surface the lower the magnetisation of the latter. This result remains the same upon lowering the surface width. In this case the number of spins having smaller coordination numbers, and hence weaker effective exchange energy, *i.e.* those spins on the outer shell of the particle, is very small as compared with the rest of spins in the particle. Moreover, we may think that the spins on the outer shell follow the (strong) molecular field cre- ated by the other (inner) spins constituting a relatively ferrimagnetically ordered core. Setting $J_{c}=\lambda J_{s}$, we may determine the coefficient $\lambda$ at which the transition regions of the core and surface overlap. This may be done using the simple, though time consuming, cumulant method in- troduced a few years ago by Binder (see [11] for a review).

### 2.3.3 Profile of the magnetisation

We have determined the spatial variation of the local mag- netisation of a spherical particle of a fixed radius as we move from the center out onto the surface, at different temperatures. At nearly zero temperature $(\tau^{core}\ll 1)$, the local magnetisation decreases with increasing radial dis- tance in the particle. It starts from the saturation value of an iron atom (in fact, we computed the mean value of A and B atoms, to take into account the possibility of starting at either atom) at the center of the particle and decreases down to the value of a surface atom. Note that what is plotted in Figure 6 is in fact the (normal- ized) projection of the atomic magnetic moment along the easy axis ($z$-axis for the core, and normal for the surface spins), which is proportional to $\cos\theta$, and thus Figure 6 also shows the spatial evolution of the orientation of the magnetic moment inside the particle as the radial distance is varied.

![](./images/812402228512948225_6.jpg)

Fig. 6. Spatial variation of the local magnetisation of a spher- ical nanoparticle of 3140 spins, as a function of the radial dis- tance, for $\tau^{core}\ll 1$, $\tau^{core}=0.5$, and $\tau^{core}\simeq 1^{-}$.

The decreasing of the local magnetisation confirms what was said before, that is even at very low temper- ature the surface is in a magnetic order which is differ- ent from that in the core, and as discussed earlier, the misalignement of spins starts at the surface and gradu- ally propagates into the core. This could be related with the gradual canting of spins confirmed by Mössbauer spec- troscopy [4-6] even at 4.2 K. As the temperature increases ($\tau^{core}=0.5, \tau^{core}\simeq 1^{-}$), the local magnetisation exhibits a jump of temperature-dependent height, and continues to decrease. Since the local magnetisation depends on the direction of the radius vector, especially in an ellipsoidal particle, the curves in Figure 6 present, in addition to the usual numerical inaccuracy (especially for $\tau^{core}\simeq 1^{-}$), some fluctuations due to the spatial non homogeneities inherent to the lacunous spinel structure of the $\gamma$-Fe₂O₃ particles ($\frac{1}{3}$ for each two B atoms, randomly distributed).

### 2.3.4 Specific heat

In Figure 7 we plot the computed specific heat of the PBC system $(N_{t}=40^{3})$ and that of an ellipsoidal nanoparticle with $N_{t}=909, 3766, 6330$ (with the corresponding val- ues of $N_{st}$ given earlier). There is a transition marked by a sharp peak for the PBC system and a broad peak for the three particle sizes. This broadening is an obvious

![](./images/812402228512948225_7.jpg)

Fig. 7. Thermal variation of the specific heat of the PBC system with $N_{\mathrm{t}}=40^{3}$, and that of an ellipsoidal nanoparticle with $N_{\mathrm{t}}=909,3766,6330$, and for the same energy parameters as in Fig. 3).

illustration of the finite-size effects. Note also the shift by 50% to lower temperatures of the critical region, as in the magnetisation thermal behavior in Figure 4.

We are intending to prepare appropriate samples for the specific heat measurements. To our knowledge, such measurements have never been performed on nanoparticle assemblies.

## 3 Conclusion
We have presented a microscopic model for magnetic nano-scale particles including exchange and dipolar interactions, and bulk and surface anisotropy, and investigated the thermal and spatial behaviors of the core and surface magnetisation of a nanoparticle of different sizes, and hence of different surface contributions. We have found that the finiteness of the system size and free boundaries lead to a non uniform magnetisation profile decreasing toward the surface in the particle. Moreover, it turns out that surface anisotropy also leads to non saturation of the magnetisation at low temperatures.

In order to compare our results obtained for a single nanoparticle with our experiments on dilute assemblies of nanoparticles [7], and in particular to compare with the curve of magnetisation *vs*. temperature given in Figure 1b, we have to include the Zeeman energy term in our Hamiltonian and run our program for different particle sizes with randomly distributed easy axes. Unfortunately, this will require several days of CPU time, since a temperature sweep takes about 30 hours (without dipolar interactions) on a two-processor Alpha Work Station. It also remains to study the interplay between finite-size and surface effects in a nanoparticle of round shape (sphere or ellipsoid), as is the case here, since for a box-shaped particle one can treat separately finite-size and surface effects by considering both cases of free boundaries where these two effects are mixed and that of periodic boundary conditions where only the former are present. In the present case, it can be seen from Figure 4 that the magnetisation of the PBC system where only finite-size effects are present is larger than the bulk magnetisation, while the magnetisation of a (anisotropic) nanoparticle is lower. This implies, as was analytically shown in [19] for a box-shaped particle with simple-cubic structure, that finite-size effects yield a positive contribution to the magnetisation while surface effects render a larger and negative contribution, resulting in a net magnetisation that is lower than that of the bulk system. In [20] it was also shown that the difference between the finite-size and surface contributions is enhanced by surface anisotropy, which leads to non saturation of the magnetisation at low temperatures (see Figs. 3-5). Nevertheless, already from the present single-particle preliminary study we can infer some conclusions about the effect of the magnetically disordered surface on the global magnetic properties of nanoparticles. The surface contribution to the magnetisation presents a rather different behavior from the core contribution. Furthermore, even at very low temperatures, the local magnetisation decreases with the distance from the center, showing that the magnetic state on the surface is definitely different from that in the core. We have also shown that there is a drastic reduction of both the critical temperature and the value of the magnetisation in the core of the particle. The reduction of the critical temperature is obviously due to the finite-size and surface effects. As to the magnetisation, the reduction shows that the magnetic properties of the particle core are different from those of bulk material, because of the strong influence of the misalignement of spins on the surface, driven by symmetry breaking of the crystal field and surface anisotropy, which propagates from the boundary into the core. Finally, we note that our results on the thermal and spatial behavior of the magnetisation are in qualitative agreement with those obtained by Binder *et al.* [21] for spherical particles with simple-cubic crystalline structure.

H.K. thanks L. Reynaud for his considerable help in these simulations and D. Garanin for his valuable remarks and suggestions. The present numerical calculations have been performed on the Alpha Work Station of the Genome Laboratory of the University of Versailles to which we are greatly indebted.

## References
1. R.E. De Wames, T. Wolfram, *Progress in Surface Sciences*, vol. 2, edited by S.G. Davison (Oxford Pergamon, 1972), p. 23; T. Kaneyoshi, J. Phys. Cond. Mat. **3**, 4497-4522 (1991); D. Garanin, J. Phys. A **29**, (1996) L257-L262; D. Garanin, Phys. Rev. E **58**, 254 (1998).
2. A.I. Akhiezer, V.G. Bar'yakhtar, S.V. Peletminskii, *Spin waves* (North-Holland Publ. Company, 1968).
3. A. Aharoni, *Introduction to the theory of ferromagnetism* (Oxford Science Pubs., 1996).

4. K. Haneda, Can. J. Phys. **65**, 1233 (1987), and references therein.

5. J.M.D. Coey, Phys. Rev. Lett. **27**, 1140 (1971).

6. P. Prené *et al.*, Hyperfine Int. **93**, 1049 (1994); P. Prené, Ph.D. thesis of the Université Pierre & Marie Curie, July 1995; E. Tronc *et al.*, Hyp. Int. **112**, 97 (1998).

7. A. Ezzir, Ph.D. thesis of the Université Paris XI-Orsay, December 1998.

8. J.P. Chen *et al.*, Phys. Rev. B **51**, 11527 (1995).

9. R. H. Kodama, A.E. Berkovitz, E.J. Mcniff, S. Foner, Phys. Rev. Lett. **77**, 394 (1996); R.H. Kodama, A. E. Berkovitz, Phys. Rev. B **59**, 6321 (1999); and references therein.

10. J.S. Smart, in *Magnetism*, edited by G.T. Rado, H. Suhl (Academic Press New York 1963) p. 63.

11. K. Binder, D.W. Heermann, *Monte Carlo simulation in statistical physics* (Springer-Verlag, Berlin 1992); K. Binder, Physica **62**, 508 (1972); K. Binder, D. Landau, Surface Science **151**, 409 (1985).

12. D.A. Dimitrov, G.M. Wysin, Phys. Rev. B **50**, 3077 (1994); *ibid* **51**, 11947 (1994).

13. S. Krupicka, K. Zaveta, in *Magnetic Oxides*, Part I, edited by D.J. Craik (A Wiley-Interscience Publication, 1975).

14. J.L. Dormann *et al.*, Phys. Rev. B **18**, 1 (1996); F. Gazeau *et al.*, Europhys. Lett. **40**, 575 (1997).

15. A. Aharoni, J. Appl. Phys. **81**, 830 (1997).

16. B.K.P. Scaife, *Principles of dielectrics* (Oxford Science Pubs., 1989).

17. O. Eriksson *et al.*, Phys. Rev. B **45**, 2868 (1992).

18. P.V. Hendriksen, S. Linderoth, P.-A. Lindgard, Phys. Rev. B **48**, 7259 (1993).

19. H. Kachkachi, D.A. Garanin, *Boundary and finite-size ef- fects in small magnetic systems*, submitted to J. Phys. Cond. Matter.

20. H. Kachkachi, M. Noguès, E. Tronc, D.A. Garanin, *Finite-size versus surface effects in nanoparticles*, Cond-mat/9910393, invited paper to 3rd *EuroConference* on Magnetic Properties of Fine Nanoparticles, Barcelona, October 99 (submitted to J. Magn. Magn. Mat.).

21. K. Binder, H. Rauch, V. Wildpaner, J. Chem. Solids **31**, 391 (1970); V. Wildpaner, Z. Physik **270**, 215 (1974).