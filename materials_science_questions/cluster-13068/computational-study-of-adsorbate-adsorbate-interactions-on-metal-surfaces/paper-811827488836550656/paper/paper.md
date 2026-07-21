# Fermi disks model for $^3$He films adsorbed on graphite within a density-functional approach

M. M. Calbi and E. S. Hernández

Departamento de Física, Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires
and Consejo Nacional de Investigaciones Científicas y Técnicas, Argentina, RA-1428 Buenos Aires, Argentina

(Received 7 July 1997; revised manuscript received 6 January 1998)

We investigate the energetics and structure of $^3$He layers adsorbed on graphite in the submonolayer regime. We have assumed translational invariance parallel to the substrate, however, taking into account the perpendicular motion of the atoms. The energetics and stability properties can be interpreted in terms of a model that regards the film as a collection of two-dimensional (2D) systems in momentum space, whose parameters, however, arise from a full 3D self-consistent calculation. The range of validity of the model is established, indicating that, in addition to describing the submonolayer regime, it can be applied as well to films admitting several fluid layers such as those appearing on weakly binding substrates. We can also make a preliminary analysis of the ability of the 3D-energy functional to reproduce the equation of state of the film.

[S0163-1829(98)13319-2]

## I. INTRODUCTION

Films of liquid helium adsorbed on substrates have constituted a vivid field of research for several years, in view of the various structural and thermodynamic aspects amenable to both experimental and theoretical approaches. In particular, the study of wetting phenomena and prewetting transitions has received considerable attention, both from the viewpoint of density-functional theory$^{1-4}$ and of variational hypernetted-chain-Euler-Lagrange (HNC-EL) descriptions of quantum liquids.$^{5}$ The theoretical effort related to $^3$He films has been concentrated on their formation and wetting behavior upon weakly binding substrates such as alkali metals,$^{2,3}$ and it is worthwhile recalling that the predictions of nonlocal density-functional theory concerning prewetting transitions are in satisfactory qualitative agreement with recent experimental data.$^{6}$ However, strong adsorbers may give rise to a different phase diagram; in particular, graphite has been shown to adsorb fluid helium monolayers up to an areal coverage of about $0.04$ A$^{-2}$, with subsequent layering being preceded by the formation of commensurate and incommensurate solid phases that permits a solid-liquid coexistence region within a certain range of coverages.$^{7-13}$ These solid, two-dimensional (2D) systems have been reported to appear in both the first and the second spatial layers of $^3$He films on graphite (for a review, see, for example, Ref. 14). Moreover, even in the monolayer regime, a strictly 2D description of the film is unable to provide self-binding,$^{15,16}$ while on the other hand, a variational approach that considers the motion of the helium atoms perpendicular to the substrate has been successful in predicting the existence of a self-bound fluid at submonolayer density.$^{16}$

Starting from the pioneering work of Stringari,$^{17}$ density functionals for quantum liquids have been improved in several steps in order to extend their application from the simplest homogeneous bulk system up to finite or dimensionality- reduced systems such as droplets,$^{18-21}$ films adsorbed on substrates,$^{3,22}$ and free surfaces.$^{23}$ Recently, it has been shown that a convenient choice and parametrization of a nonlocal, finite range density functional can account for a variety of properties of liquid $^3$He, $^3$He droplets, mixtures of both isotopes of liquid helium, and mixed $^3$He-$^4$He clusters.$^{21,24,25}$ Within this framework, it has been possible to describe the equation of state of liquid helium and its effective interaction with a good fit to both density and magnetic Landau parameters over the whole range of fluid densities, and stability of drops together with a prediction of their pairing behavior.$^{21}$ Furthermore, the zero sound dispersion relationship at zero and finite temperatures has been adequately reproduced, together with the location and widths of the paramagnon peaks,$^{24}$ and more recently, it has been demonstrated that the structure and energetics of mixed clusters presents features in good agreement with preliminary experimental observations.$^{25}$

It is then challenging to resort to the density-functional approach to investigate to what extent a monolayer or submonolayer of $^3$He adsorbed on graphite can be regarded as a 2D fluid. As a byproduct, it is worthwhile testing whether a density functional—whose parameters have been adjusted to fit properties of the bulk systems—can account for the phase diagrams of these films. Although there is not enough experimental evidence about the nature of the ground state, it is also important to know if the density functional predicts a gas or liquid ground state, in order to compare with other calculations.

In this work, we investigate the structure of $^3$He films adsorbed on graphite starting from density-functional theory, and develop a quasi-2D model that allows one to visualize the film in momentum space as a collection of Fermi disks whose Fermi momenta, provided by a self-consistent calculation, permit one to define associated areal densities on the spatial plane parallel to the substrate. The atomic motion along the $z$ coordinate is in charge of building the different bandheads for these Fermi disks, and the complete energetics of the film can be traced to a set of 2D thermodynamic variables, unambiguously constructed. This model is presented in Sec. III. In Sec. IV we display the results of our calculations for the submonolayer regime and show that these results can be interpreted in terms of the model for a unique disk. The summary is the subject of Sec. V.

## II. DENSITY-FUNCTIONAL MODEL FOR $^3$He FILMS

In order to investigate the energetics and structure of $^3$He films adsorbed on graphite, we consider a general, nonlocal density functional that describes bulk liquid $^3$He at zero temperature. The ground-state wave function of the film is assumed to be a Slater determinant of single particle (SP) states $\phi_i(\mathbf{r})$ and we write the total energy of the system in the form

$$
\begin{aligned}
E(\rho)= & \int d \mathbf{r} \frac{\hbar^{2}}{2 m^{*}(\mathbf{r})} \tau(\mathbf{r}) \\
& +\frac{1}{2} \int d \mathbf{r} \int d \mathbf{r}^{\prime} V\left(\mathbf{r}-\mathbf{r}^{\prime}\right) \rho(\mathbf{r}) \rho\left(\mathbf{r}^{\prime}\right) \\
& +\frac{1}{2} \int d \mathbf{r}\left\{c \rho^{\gamma+2}(\mathbf{r})+d_{1}[\nabla \rho(\mathbf{r})]^{2}+d_{2} \rho(\mathbf{r})\right. \\
& \left.\times[\nabla \rho(\mathbf{r})]^{2}\right\}+\int d \mathbf{r} V_{s}(\mathbf{r}) \rho(\mathbf{r}),
\end{aligned}
$$

where

$$
\rho(\mathbf{r})=2 \sum_{i}\left|\phi_{i}(\mathbf{r})\right|^{2},
$$

$$
\tau(\mathbf{r})=2 \sum_{i}\left|\nabla \phi_{i}(\mathbf{r})\right|^{2} .
$$

In applications to systems with finite or reduced dimensionality such as films and droplets, as well as to compute the dynamical susceptibility of liquid $^3$He, some densities $\rho$ appearing in Eq. (2.1) are replaced by a coarse grained one, $\widetilde{\rho}(\mathbf{r})$, averaged over a sphere of radius $h$ with a step weighting function $w(\mathbf{r}-\mathbf{r}')$. The kinetic energy term contains a density-dependent effective mass and the two-body interaction $V(\mathbf{r},\mathbf{r}')$ is a Lennard-Jones potential with either soft or truncated core. $^{3,21,24,25}$ The last term in Eq. (2.1) includes the interaction energy of the helium atoms with the substrate, through a potential $V_s$. If we assume that the SP wave functions take the form

$$
\phi_{\mathbf{k} \nu}\left(\mathbf{r}_{2}, z\right)=\frac{1}{\sqrt{A}} e^{i \mathbf{k} \cdot \mathbf{r}_{2}} f_{k \nu}(z)
$$

and minimize the energy functional with respect to $\rho(\mathbf{r})$, subjected to the constraint that the wave functions remain orthonormal, we arrive at a Hartree-Fock (HF) equation:

$$
\begin{gathered}
-\frac{d}{d z}\left[\frac{\hbar^{2}}{2 m^{*}(z)} \frac{d f_{k \nu}}{d z}\right]+\left[\frac{\hbar^{2}}{2 m^{*}(z)} k^{2}+V(\rho)\right] f_{k \nu}(z) \\
=\varepsilon_{k \nu} f_{k \nu}(z)
\end{gathered}
$$

with the SP potential

$$
V(\rho)=\frac{\delta E}{\delta \rho}.
$$

In addition, the particle and kinetic energy densities read

$$
\rho\left(\mathbf{r}_{2}, z\right)=2 \sum_{\nu} \int \frac{d \mathbf{k}}{(2 \pi)^{2}}\left(f_{k \nu}(z)\right)^{2},
$$

$$
\tau\left(\mathbf{r}_{2}, z\right)=2 \sum_{\nu} \int \frac{d \mathbf{k}}{(2 \pi)^{2}}\left[k^{2}\left(f_{k \nu}(z)\right)^{2}+\left(f_{k \nu}^{\prime}(z)\right)^{2}\right].
$$

The SP energies $\varepsilon_{k\nu}$ form a discrete set of 2D momentum continua, each labeled by the index $\nu$ that indicates the number of nodes of the function $f_{k\nu}(z)$. Since the system is not spin-polarized, the particles occupy the $N/2$ states of lowest energy, filling each continuum up to a maximum momentum $k_{F\nu}$ so that

$$
\sum_{\nu}\left(k_{F \nu}\right)^{2}=2 \pi \rho_{2} \equiv 2 \pi \sum_{\nu} \rho_{2 \nu},
$$

where the coverage $\rho_2$ is a homogeneous 2D density:

$$
\rho_{2}=\int d z \rho(\mathbf{r})=\frac{N}{A}.
$$

In Eq. (2.9), the partial areal density $\rho_{2\nu}$ is defined through the 2D relationship to the corresponding Fermi momentum $k_{F\nu}$. The occupancy of the SP states is thus determined by the competition between the binding ability of the substrate and the diluteness of the layer. For each coverage, the HF equation must be solved self-consistently; in this work, the occupied SP levels are those with energies $\varepsilon_0(k)$, with $0 \leqslant k \leqslant \sqrt{2 \pi \rho_{2}}$.

## III. THE FERMI DISKS MODEL

If the HF solutions are such that

$$
f_{k \nu}(z) \equiv f_{\nu}(z),
$$

the momentum dependence of the SP energies for each coverage can be written as

$$
\varepsilon_{k \nu}=\varepsilon_{\nu}+a_{\nu} k^{2}
$$

with a 2D wave vector $\mathbf{k}$, and one can thus detect the formation of well defined Fermi disks upon different bandheads $\varepsilon_{\nu}$, where $a_{\nu}$ is an inertial parameter for the $\nu$th disk. We can then regard the film as a collection of quasi-2D systems, since the mass and kinetic energy densities can be written as

$$
\rho\left(\mathbf{r}_{2}, z\right)=\sum_{\nu} \rho_{2 \nu} \rho_{\nu}(z),
$$

$$
\tau\left(\mathbf{r}_{2}, z\right)=\sum_{\nu} \rho_{2 \nu}\left[\frac{1}{2} k_{F \nu}^{2} \rho_{\nu}(z)+\tau_{\nu}(z)\right],
$$

where

$$
\rho_{\nu}=\left[f_{\nu}(z)\right]^{2}
$$

and

$$
\tau_{\nu}(z)=\left[f_{\nu}^{\prime}(z)\right]^{2} .
$$

Using these definitions and relations, the areal energy density becomes

$$
\begin{aligned}
\frac{E}{A}= & \sum_{\nu} \rho_{2 \nu}\left[\frac{1}{2} \frac{\hbar^{2}}{2 m_{\nu}^{*}} k_{F \nu}^{2}\right. \\
& \left.+\int d z \frac{\hbar^{2}}{2 m^{*}(z)} \tau_{\nu}(z)+\int d z V_{s}(z) \rho_{\nu}(z)\right] \\
& +\frac{1}{2} \sum_{\nu \nu^{\prime}} \rho_{2 \nu} \rho_{2 \nu^{\prime}}\left\{\int d z \int d z^{\prime} V\left(z-z^{\prime}\right) \rho_{\nu}(z) \rho_{\nu^{\prime}}\left(z^{\prime}\right)\right. \\
& +\frac{1}{2} \int d z c \rho(z)^{\gamma} \rho_{\nu}(z) \rho_{\nu^{\prime}}(z) \\
& \left.+\frac{1}{2} \int d z\left[d_{1}+d_{2} \rho(z)\right] \rho_{\nu}^{\prime}(z) \rho_{\nu^{\prime}}^{\prime}(z)\right\}
\end{aligned}
$$

with the disk effective mass
$$
\frac{\hbar^{2}}{2 m_{\nu}^{*}}=\int d z \frac{\hbar^{2}}{2 m^{*}(z)} \rho_{\nu}(z). \quad (3.8)
$$

The above expression for the energy density indicates that the film consists of a set of broad spatial slices, each of them homogeneous on the plane parallel to the substrate with 2D density $\rho_{2 \nu}$ and extended along the $z$ direction according to a local density $\rho_{\nu}(z)$. The total energy of such a system clearly includes the 3D kinetic and the substrate potential energy of each separate slice, together with their mutual interaction driven by the softened Lennard-Jones potential and by the repulsive, density-dependent term. This view of the film is consistent with the whole set of thermodynamic functions requested to establish the stability of the film. In fact, expression (3.3) for the total density permits us to identify a local 3D one for each disk $\nu$ :
$$
\rho_{3 \nu}(z)=\rho_{2 \nu} \rho_{\nu}(z), \quad (3.9)
$$
showing that the 2D homogeneous density $\rho_{2 \nu}$ is
$$
\rho_{2 \nu}=\int d z \rho_{3 \nu}(z). \quad (3.10)
$$

Taking into account Eq. (3.9), the disk local pressure is then
$$
P_{3 \nu}(z)=\rho_{3 \nu}^{2}(z) \frac{\partial}{\partial \rho_{3 \nu}}\left(\frac{E}{N}\right)=\rho_{\nu}(z) \rho_{2 \nu}^{2} \frac{\partial}{\partial \rho_{2 \nu}}\left(\frac{E}{N}\right),
$$
from which we can define a quasi-2D pressure for the $\nu$ th disk,
$$
P_{2 \nu}=\int d z P_{3 \nu}(z)=\rho_{2 \nu}^{2} \frac{\partial}{\partial \rho_{2 \nu}}\left(\frac{E}{N}\right). \quad (3.12)
$$

Furthermore, the local 3D chemical potential is
$$
\mu_{3 \nu}=\frac{E}{N}+\frac{P_{3 \nu}(z)}{\rho_{3 \nu}(z)}=\frac{E}{N}+\frac{P_{2 \nu}}{\rho_{2 \nu}}, \quad (3.13)
$$
which is independent of $z$ and can be identified as the quasi-2D chemical potential
$$
\mu_{2 \nu} \equiv \mu_{3 \nu} \equiv \mu_{\nu}. \quad (3.14)
$$

If we consider, additionally, the 3D local inverse compressibility $\kappa_{3 \nu}$ :
$$
\frac{1}{\kappa_{3 \nu}}=\rho_{\nu}(z) \rho_{2 \nu} \frac{\partial P_{2 \nu}}{\partial \rho_{2 \nu}}, \quad (3.15)
$$
after the $z$ integration, the corresponding quasi-2D expres sion is
$$
\frac{1}{\kappa_{2 \nu} \rho_{2 \nu}}=\frac{\partial P_{2 \nu}}{\partial \rho_{2 \nu}}. \quad (3.16)
$$

In addition, we can verify the relationship
$$
\frac{\partial P_{2 \nu}}{\partial \rho_{2 \nu}}=\rho_{2 \nu} \frac{\partial \mu_{\nu}}{\partial \rho_{2 \nu}} \quad (3.17)
$$
so that the quasi-2D inverse compressibility can be calcu- lated from the standard thermodynamic rule
$$
\frac{1}{\kappa_{2 \nu} \rho_{2 \nu}}=\rho_{2 \nu} \frac{\partial \mu_{\nu}}{\partial \rho_{2 \nu}}. \quad (3.18)
$$

A further consistency relationship arises from the fact that the common Fermi energy of the disks can be written as
$$
\varepsilon_{F}=\varepsilon_{\nu}+\frac{\hbar^{2} k_{F \nu}^{2}}{2 m_{\nu}^{*}} \quad (3.19)
$$
for all $\nu$, which shows that the disk parameters $\varepsilon_{\nu}, k_{F \nu}$ (or $\rho_{2 \nu}$ ), and $m_{\nu}^{*}$ are not independent.

## IV. RESULTS AND DISCUSSION

In this work we have performed an exploration of the available density functionals in order to discern their simi- larities and differences in what concerns the description of a film with very low areal density adsorbed on a strong poten- tial. We have found that density functionals such as those presented in Refs. 21 and 24 present some inconveniences in their application to these strongly confined, quasi-2D sys- tems. On the one hand, the parabolic effective mass of these functionals, i.e.,
$$
\frac{\hbar^{2}}{2 m^{*}}=\frac{\hbar^{2}}{2 m}+A \rho+\tilde{A} \rho^{2}, \quad (4.1)
$$
acquires negative values within a small interval of high den- sities that may, however, appear in the largely compressed film. As in previous applications to the structure of pure and doped droplets, $^{25,31}$ this can be circumvented adopting the parametrization of the form originally proposed by Stringari,
$$
\frac{\hbar^{2}}{2 m^{*}}=\frac{\hbar^{2}}{2 m}\left(1-\frac{\tilde{\mu}(\mathbf{r})}{\rho_{c}}\right)^{2}, \quad (4.2)
$$
which coincides with the preceding one in the density do- main of the homogeneous 3D liquid. Moreover, the coarse- grained density
$$
\tilde{\mu}\left(\mathbf{r}_{2}, z\right)=\sum_{\nu} \rho_{2 \nu} \tilde{\rho}_{\nu}(z) \quad (4.3)
$$

![](./images/811827488836550656_1.jpg)

FIG. 1. Density profiles for coverages $\rho_2 = 0.02, 0.04$, and 0.07
Å $^{-2}$, from bottom to top.

with
$$
\tilde{\rho}_{\nu}(z)=\int d z^{\prime} w\left(z-z^{\prime}\right) \rho_{\nu}(z),\qquad(4.4)
$$
where $w(z-z')$ is the reduced weight function with radius
$h$,
$$
w\left(z-z^{\prime}\right)=\int d \mathbf{r}_{2} w\left(\mathbf{r}-\mathbf{r}^{\prime}\right),\qquad(4.5)
$$
takes the place of $\rho$ in the local contribution $\rho^{\gamma}$ of Eq. (2.1).
However, the most notable inconvenience arises from the
fact that these density functionals predict a too large binding
energy for the fluid in the submonolayer regime. This is due
to the fact that this density functional has been parametrized
in such a way that the coefficients $d_1$ and $d_2$ of the gradient
terms vanish. Although this gives rise to an adequate de-
scription of soft surfaces, i.e., the free one in semi-infinite
$^3$He, where the soft-core LJ potential accounts for the sur-
face tension, we have verified that when sharp surfaces ap-
pear such as those of the density profiles of an adsorbed
submonolayer of $^3$He on graphite, a properly parametrized
curvature energy is requested in order to increase its binding
energy. In fact, replacement of the effective mass (4.1) by
(4.2) is equivalent to reparametrizing the density functional
and is not consistent with vanishing gradient terms. This ef-
fect is taken into account in the density functional of Ref. 3,
which is thus selected to illustrate our results, together with
the substrate potential
$$
V_{s}(z)=A e^{-\alpha z}-\frac{C_{3}}{z^{3}}-\frac{C_{4}}{z^{4}}\qquad(4.6)
$$
with $A=226.7$ K, $\alpha=3.175$ A$^{-1}$, $C_3=1830.9$ K A$^3$, and
$C_4=10305.9$ K A$^4$. Although this adsorption potential is
probably not the most accurate one, the choice is convenient
to compare our results with those in Ref. 16.

We have solved the HF equation for coverages between
0.002 and 0.07 A$^{-2}$. In Figs. 1 and 2 we show the equilib-
rium density profiles $\rho(z)$ and the corresponding $z$ depen-
dence of the HF mean field for several coverages. We can
observe the existence of only one layer and, in fact, the onset
of the second fluid layer of $^3$He on graphite has been experi-
mentally located at $\rho_2=0.108$ A$^{-2}$. $^{16}$ It is important to no-
tice that for a given coverage, the height of the peak exceeds
by a factor of about 3 the corresponding one for a Cs
substrate. $^{3}$ This behavior, easily traceable to the strong bind-
ing ability of the graphite field, has also been found for lay-
ers of $^4$He on graphite as compared to those on Na, however
for much larger areal densities than those here employed. $^{2}$
By contrast, variational HNC/EL calculations performed in a
$\rho_2$ range between 0.05 and 0.18 A$^{-2}$ do not seem to exhibit
such large differences. $^{5}$ We stress that above $\rho_2$
$\approx 0.04$ A$^{-2}$, the 3D peak densities are compatible with
those of bulk solid helium; it should be kept in mind, how-
ever, that the present description is not able to deal with such
structured phases as the registered or incommensurate ones
that have been experimentally detected. $^{14}$

![](./images/811827488836550656_2.jpg)

FIG. 2. Mean single-particle field for the same coverages of Fig.
1, from bottom to top.

We display in Fig. 3 the bandheads $\varepsilon_{\nu}(0)$ for $\nu=0,1,2$ as
well as the chemical potential $\mu$ at zero temperature, which
in this work is the Fermi energy $\varepsilon_0(k_F)$, as functions of $\rho_2$.
It should be noticed that in the current scale, the chemical
potential can be hardly distinguished from the lowest band-
head; the numerical size of $|\mu - \varepsilon_0|$ remains of the order of 1
K, similar to the values encountered for weaker substrates. $^{3}$
We observe that filling of the second 2D disk has to begin at
coverages greater than 0.07 A$^{-2}$. At these areal densities, it
seems that the formation of a second spatial layer, namely
the appearance of a well defined peak in the density profile,
also takes place, in agreement with the occupancy of a new
Fermi disk. The same behavior is observed for the growth of
the second layer of $^3$He adsorbed on weak binding
substrates $^{3}$ although in this case, while the number of occu-
pied disks keeps on increasing with coverage, the number of
spatial layers remains constant as the film approaches the
bulk limit.

It is worthwhile noticing that whenever one can describe
the $z$ dependence of all SP states with the same function
$f_{\nu}(z)$ labeled by a given number of nodes [cf. Eq. (3.1)], the
Fermi disks model permits us to understand the thermody-

![](./images/811827488836550656_3.jpg)

FIG. 3. Bandhead energies as functions of the coverage. The crosses represent the values of the zero temperature chemical potential.

namic behavior of this submonolayer film as a 2D system driven by the 3D character of the interaction between par- ticles and that of the substrate field. In the present work, where the substrate potential is strongly attractive, we find that the model is legitimized up to coverages around 0.07 A⁻², which corresponds to only one occupied disk ($\rho_2$ = $\rho_{20}$). This is due to the fact that the validity of the qua- dratic approximation (3.2) cannot be asserted beyond $\rho_2$ ≈0.07 A⁻², since the various bandheads resemble each other closely, as seen in Fig. 3, so that coupling between disks becomes more effective . We have verified that while for the lowest areal densities the wave functions $f_{k\nu}(z)$ re- main insensitive to the value of the 2D momentum $k$, this is no longer true for values of $\rho_2$ close to or above 0.07 A⁻². On the other hand, taking into account the results of Ref. 3, we can expect that for weak binding substrates the model holds up to higher coverages (near 0.4 A⁻²), compatible with the filling of many Fermi disks.

In Fig. 4, we have plotted the effective mass given by Eq. (3.8) as a function of the coverage. We have also calculated three other quantities that could be associated with a disk effective mass

(i) An average of $m^*(z)$ weighted with the kinetic energy density
$$
\frac{\hbar^{2}}{2 m_{\tau}^{*}}=\frac{\int d z \frac{\hbar^{2}}{2 m^{*}(z)} \tau(z)}{\int d z \tau(z)}.\qquad(4.7)
$$

(ii) The inverse of the inertial parameter $a_0$ arising from a quadratic fit of the SP spectrum for the first Fermi disk,
$$
m_{a}^{*}=\frac{\hbar^{2}}{2 a_{0}}.\qquad(4.8)
$$

(iii) A simple spatial average,
$$
m_{z}^{*}=\frac{1}{d} \int d z m^{*}(z),\qquad(4.9)
$$
where $d$ is the film thickness associated with the density profile.

![](./images/811827488836550656_4.jpg)

FIG. 4. Comparison among various possible definitions of the effective mass. The full circles are experimental values from Ref. 26.

We observe in Fig. 4 that although $m^*, m_{\tau}^{*}$ , and $m_{a}^{*}$ take similar values at coverages smaller than 0.03 A⁻², their dif- ferences increase with $\rho_2$. The trivial 2D reduction given by a simple average turns out to be definitively unsuitable. As a reference, we have included some experimental values ex- tracted from heat capacity data.²⁶

Figure 5 shows the dependence of the total energy per particle $E/N$ with coverage. We have numerically calculated the disk pressure (3.12) and the 2D Landau parameter $F_0^s$ given by
$$
\frac{1}{\kappa\left(\rho_{2}\right) \rho_{2}^{2}}=\frac{\partial \mu}{\partial \rho_{2}}=\frac{\pi \hbar^{2}}{m^{*}\left(\rho_{2}\right)}\left[1+F_{0}^{s}\left(\rho_{2}\right)\right]\qquad(4.10)
$$

![](./images/811827488836550656_5.jpg)

FIG. 5. Total energy per particle as a function of coverage.

![](./images/811827488836550656_6.jpg)

FIG. 6. Pressure and Landau parameter $F_{0}^{s}$ as functions of the coverage.

with the effective mass $m_{a}^{*}$ (see Fig. 6). The values presented here are in excellent agreement with a careful computation of the effective interaction between the helium atoms. $^{27}$

We find that the ground state of the film is a gas in the attractive well provided by the adsorber. Although the interaction between the helium atoms contains an attractive tail, the only negative contribution to the total energy comes from the substrate energy
$$E_{s}=\int d \mathbf{r} V_{s}(\mathbf{r}) \rho(\mathbf{r}).\qquad(4.11)$$

This is a consequence of two facts. On the one hand, the many-body wave function proposed here does not make room for correlations in the plane parallel to the substrate, so that the LJ interaction acts only between planes, contributing an areal energy density
$$\frac{E_{L J}}{A}=\frac{1}{2} \int d z \int d z^{\prime} V\left(z-z^{\prime}\right) \rho(z) \rho\left(z^{\prime}\right)\qquad(4.12)$$
with
$$\begin{aligned}
& V\left(z-z^{\prime}\right) \\
& = \begin{cases}4 \pi \epsilon \sigma^{2}\left[\left(\frac{1}{5} \frac{\sigma}{z-z^{\prime}}\right)^{10}-\frac{1}{2}\left(\frac{\sigma}{z-z^{\prime}}\right)^{4}\right], & \left|z-z^{\prime}\right| \geqslant h_{l} \\
16.05, & \left|z-z^{\prime}\right| \leqslant h_{l}.\end{cases}
\end{aligned}$$

On the other hand, the density $\rho(z)$ is nonvanishing at a width of about $2 \AA$ in the $z$ direction, within which the particles are correlated by the repulsive core of the full interaction. In fact, one can see that the self-bound state found in Ref. 16 does not arise from the competition between kinetic and interaction terms, but rather from the more indirect balance that originates the dependence of the substrate energy on the areal coverage; the density dependence of the attractive LJ contribution compensates for that of the kinetic energy in such a way that their sum remains almost constant. The same effect takes place in the current HF energy; the sum of all contributions, except the substrate one, is practically independent of the coverage, and the density dependence of the total energy comes basically from the adsorber energy. The main difference between the present work and the variational calculation in Ref. 16 rests precisely on this contribution, which strongly depends on the model used to calculate the density profiles.

In Ref. 2, it has been pointed out that the density-functional frame attributes gas character to a purely $2 D^{3} He$  fluid. The same result can be obtained using a variational Monte Carlo technique. When one takes into account the perpendicular motion of the atoms, the Monte Carlo method predicts a bound fluid state $^{16}$ but, in contrast to that result, we find here that the effect of the $z$ delocalization of the atoms is not enough to form a self-bound state. There is as yet no conclusive experimental evidence favoring the existence of a self-bound state in a submonolayer fluid adsorbed on graphite; in particular, specific heat measurements $^{8-10}$ provide information on transitions from a fluid to a solid phase, but do not account for the $E$ vs $\rho$ equation of state. However, we note that if the film is self-bound, the binding energy of the atoms may be very small, so that a very accurate model together with a proper choice of the substrate potential would be required to reproduce such a sensitive equation of state.

The deficiency of density functionals to predict the binding energies of these nonuniform systems has already been indicated for a strictly $2 D^{4} He$ fluid. $^{28}$ The Monte Carlocalculation $^{29}$ as well as the experimental measurements $^{30}$  predict a bound state, while the zero range density functional yields an insignificant binding. $^{5}$ This situation is, however, improved in the framework of a new functional for nonhomogeneous $^{4} He$ systems, $^{28}$ whose accuracy can be compared to that of microscopic calculations. With respect to the $^{3} He$  films, we have to observe that the gradient terms, which have not been included to investigate other nonhomogeneous systems such as helium droplets, $^{25,31}$ represent a large contribution for these strongly adsorbed films and it is strictly necessary to obtain reasonable figures for their equation of state.

## V. SUMMARY
We have explored a problem investigated previously, namely, the structure of helium films, focusing on (i) a substrate such as graphite, whose deep attractive field for the3He atoms permits the formation of submonolayers exhibiting solid phases, and (ii) a finite range density functional that has been proven capable of describing structure and thermodynamics of bulk helium and droplets, plus dynamical density and spin susceptibility of the liquid at low temperatures. Within this density-functional frame, it has been possible to develop a model of the film in momentum space that allows us to interpret the system as a collection of 2D ones with well defined 2D parameters such as disk effective mass and disk areal density. Although our calculations can be extended to higher areal coverages, we have here preferred to remain at submonolayer densities in order to test the abilities of the present model, which is not supposed to remain applicable when the various bandheads become too close together. Applications to layering on weak binding substrates appear to be promising, in view of the apparent decoupling between

disks that supports the quadratic fit to the spectrum (3.2) up to moderately large coverages. $^{3}$

A byproduct of the Fermi disks model is a straightforward interpretation of the effective atom-atom interaction obtained from double functional differentiation of the total energy density. $^{27}$ The dynamical susceptibility of these films is a challenging issue, since it presents several interesting com- plexities. It can be seen that the strength of particle-hole transitions taking place either inside a Fermi disk or between two of these bands is the essential ingredient for a proper understanding of the free response of these systems. $^{32}$ Al though, according to the present work, the response of sub- monolayers adsorbed in graphite can be calculated on the basis of a pure 2D Fermi liquid, $^{33}$ multiple layer films may offer a richer range of possibilities. Calculations are in progress and will be presented elsewhere.

## ACKNOWLEDGMENTS
It is a pleasure to thank Dr. S. M. Gatica for discussions and exchange. This work has been performed under Grant No. Ex100/95 from Universidad de Buenos Aires, Argentina.

$^{1}$ E. Cheng, Milton W. Cole, W. F. Saam, and J. Treiner, Phys. Rev. Lett. 67, 1007 (1991).
$^{2}$ E. Cheng, Milton W. Cole, W. F. Saam, and J. Treiner, Phys. Rev. B 46, 13 967 (1992).
$^{3}$ L. Pricaupenko and J. Treiner, Phys. Rev. Lett. 72, 2215 (1994).
$^{4}$ E. Cheng, M. W. Cole, J. Dupon-Roc, W. F. Saam, and J. Treiner, Rev. Mod. Phys. 65, 557 (1993).
$^{5}$ B. E. Clements, H. Forbert, E. Krotscheck, and M. Saarela, J. Low Temp. Phys. 95, 849 (1994).
$^{6}$ D. Ross, J. A. Phillips, J. E. Rutledge, and P. Taborek, J. Low Temp. Phys. 106, 81 (1997).
$^{7}$ H. Franco, R. E. Rapp, and H. Godfrin, Phys. Rev. Lett. 57, 1161 (1986).
$^{8}$ D. S. Greywall, Phys. Rev. B 41, 1842 (1990).
$^{9}$ D. S. Greywall and P. A. Busch, Phys. Rev. Lett. 65, 2788 (1990).
$^{10}$ D. S. Greywall, Physica B 197, 1 (1994).
$^{11}$ H. J. Lauter, H. Godfrin, V. L. Pl. Frank, and H. P. Schildberg, Physica B 165-166, 597 (1990).
$^{12}$ J. Saunders, C. P. Lusher, and B. P. Cowan, Phys. Rev. Lett. 64, 2523 (1990).
$^{13}$ K. D. Morhard, C. Bäuerle, J. Bossy, Yu. Bunkov, S. N. Fisher, and H. Godfrin, Phys. Rev. B 53, 2658 (1996).
$^{14}$ J. Saunders, C. P. Lusher, and B. P. Cowan, in Excitations in Two-Dimensional and Three-Dimensional Quantum Liquids, ed- ited by A. G. F. Waytt and H. J. Lauter (Plenum Press, New York, 1991), p. 453.
$^{15}$ M. D. Miller and L. H. Nosanow, J. Low Temp. Phys. 32, 145 (1978).

$^{16}$ B. Brami, F. Joly, and C. Lhuillier, J. Low Temp. Phys. 94, 77 (1994).
$^{17}$ S. Stringari, Phys. Lett. 106A, 267 (1984).
$^{18}$ S. Stringari, Phys. Lett. 107A, 36 (1985).
$^{19}$ S. Stringari and J. Treiner, J. Chem. Phys. 87, 5021 (1987).
$^{20}$ S. Weisgerber and P. G. Reinhard, Phys. Lett. A 158, 407 (1991).
$^{21}$ M. Barranco, D. M. Jezek, E. S. Hernández, J. Navarro, and Ll. Serra, Z. Phys. D 28, 257 (1993).
$^{22}$ L. Pricaupenko and J. Treiner, J. Low Temp. Phys. 96, 19 (1994).
$^{23}$ S. Stringari and J. Treiner, Phys. Rev. B 36, 8369 (1987).
$^{24}$ M. Barranco, E. S. Hernández, J. Navarro, Phys. Rev. B 54, 7394 (1996).
$^{25}$ M. Barranco, M. Pi, S. M. Gatica, E. S. Hernández, and J. Na- varro, Phys. B 56, 8997 (1997).
$^{26}$ K. D. Morhard, J. Bossy, and H. Godfrin, Phys. Rev. B 51, 446 (1995).
$^{27}$ M. M. Calbi, S. M. Gatica, and E. S. Hernández (unpublished).
$^{28}$ F. Dalfovo, A. Lastri, L. Pricaupenko, S. Stringari, and J. Treiner, Phys. Rev. B 52, 1193 (1995).
$^{29}$ P. A. Whitlock, G. V. Chester, and M. H. Kalos, Phys. Rev. B 38, 2418 (1988).
$^{30}$ D. S. Greywall and P. A. Busch, Phys. Rev. Lett. 67, 3535 (1991).
$^{31}$ M. Garcías, Ll. Serra, M. Casas, and M. Barranco, J. Chem. Phys. (to be published).
$^{32}$ E. S. Hernández, Physica A (to be published).
$^{33}$ M. M. Calbi, S. M. Gatica, and E. S. Hernández, Phys. Rev. B 54, 13 097 (1996).