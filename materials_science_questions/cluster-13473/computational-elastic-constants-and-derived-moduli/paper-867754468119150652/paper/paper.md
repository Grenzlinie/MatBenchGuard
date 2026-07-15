# Breakdown of continuum elasticity in amorphous solids

Edan Lerner¹, Eric DeGiuli¹, Gustavo Düring², and Matthieu Wyart¹

¹ New York University, Center for Soft Matter Research,
4 Washington Place, New York, NY, 10003, USA
² Facultad de Física, Pontificia Universidad Católica de Chile, Casilla 306, Santiago 22, Chile

We show numerically that the response of simple amorphous solids (elastic networks and particle packings) to a local force dipole is characterized by a lengthscale $\ell_c$ that diverges as unjamming is approached as $\ell_c \sim (z-2d)^{-1/2}$, where $z \geq 2d$ is the mean coordination, and $d$ is the spatial dimension, at odds with previous numerical claims. We also show how the magnitude of the lengthscale $\ell_c$ is amplified by the presence of internal stresses in the disordered solid. Our data suggests a divergence of $\ell_c \sim (p_c-p)^{-1/4}$ with proximity to a critical internal stress $p_c$ at which soft elastic modes become unstable.

## I. INTRODUCTION

At long wavelength, amorphous solids behave as isotropic elastic solids. At short wavelength, however, this continuum description breaks down, and the particle-scale disorder matters. This fact is well-known in granular materials where the response to a local perturbation leads to a heterogeneous response locally, and where the stress propagates along preferred paths, or force chains [1, 2]. In molecular glasses, the breakdown of a hydrodynamic description is visible in the density of vibrational modes, which departs from the Debye prediction (valid in the continuum) at frequencies typically about a tenth of the Debye frequency. At such frequencies the density of vibrational modes is larger than expected, a phenomenon referred to as the boson peak [3]. Converting the boson peak frequency to a length scale using the transverse speed of sound leads to a length scale on the order of ten particle diameters [4, 5]. What governs this length scale is debated [6-8].

Understanding amorphous solids at such intermediate scales is important, because it is the scale at which rearrangements responsible both for thermally activated and for plastic flows occur. For example, in fragile liquids the boson peak frequency appears to vanish as the glass is heated past its glass transition [9, 10]. This observation suggests that above some temperature an elastic instability occurs in these liquids, and that minima of energy disappear. This scenario was initially proposed by Goldstein [11], occurs in mean-field models where it strongly affects the dynamics [12], and has received empirical support in Lennard-Jones [13] and colloidal glasses [14]. However, which length scales are associated with this instability remains unclear. Mode coupling theory predicts that a dynamical length scale (extractable from a four-point correlation function) should diverge from both sides of this transition [15-17], but this is not seen in liquids, where the dynamical length scale continuously grows under cooling. Here we study the possibility that a length scale associated with linear elasticity diverges in the solid phase, as the instability is approached.

Elasticity in amorphous materials can be investigated numerically. Barrat, Tanguy and coworkers have focused in particular on silica, where they showed that a length scale can be consistently extracted from several observables: the response to a point force, the correlation of non-affine displacements, or the spatial fluctuation of elastic moduli [18, 19]. However, questions have remained, of what controls this length scale, and whether or not it is already present in the static structure of the system. Packings of repulsive particles are convenient to study this question, because length scales characterizing elasticity become large and even diverge at the unjamming transition where the pressure vanishes [20-23]. In these systems both the mean number of interactions between the particles (referred to in the following as the coordination $z$) and the applied pressure $p$ play a key role [24]. The effect of coordination alone can be studied in zero-pressure elastic networks of varying $z$ [25-27]. Two length scales appear in such networks at zero pressure. A point-to-set length scale $\ell^* \sim 1/(z-z_c) \equiv 1/\delta z$ characterizes the distance below which mechanical stability of the bulk material is affected by the boundaries [8], as observed numerically [26, 28-30]. Here $z_c=2d$ is the critical coordination required for stability, as predicted by Maxwell [31], and $d$ denotes the spatial dimension. Another length scale can be defined by considering the response of the system at the boson peak frequency, numerically one observes a length $\ell_c \sim \delta z^{-1/2}$ [32-34] as explained using effective medium [35]. For floppy networks with $z < z_c$ the response to a zero-frequency force dipole was computed explicitly [26], and was shown to decay on the length $\ell_c$. The same lengthscale characterizes the correlation of non-affine displacements under an imposed global shear [26]. These results supported that $\ell^*$ is a point to set length, whereas the response to a local perturbation, as well as two point correlation functions characterizing the response to a global strain, are both characterized by $\ell_c$. However, this interpretation contradicts early numerical findings supporting that $\ell^*$ characterizes the zero-frequency point response in packings of particles [36], raising doubts on the validity of these numerical results. Moreover, the role of pressure on both $\ell^*$ and $\ell_c$ is currently unclear.

In this manuscript, we systematically study numerically the response to a local dipolar force in harmonic

spring networks and in packings of harmonic soft discs.
In agreement with effective medium [26,35], we find that the lengthscale beyond which a continuum elastic description captures correctly the zero-frequency response is actually $\ell_{c}$, and not $\ell^{*}$. We demonstrate how increasing pressure in packings of discs increases $\ell_{c}$. Finally, we show data suggesting that $\ell_{c}$ diverges as the pressure is increased towards the critical pressure at which an elastic instability occurs. The scaling we find is consistent with $\ell_{c}(p) \sim 1 /(p_{c}-p)^{1 / 4} \sim 1 / \omega_{B P}(p)$ where $\omega_{B P}(p)$ is the effective medium prediction for the pressure-dependent boson peak frequency as the critical pressure is approached, as derived in a companion paper [37].

## II. THEORETICAL FRAMEWORK

In this section we provide a general framework within which two response functions to a local dipolar force (as depicted in Fig. 1c) are defined. The first response function, $C(r)$, measures the amplitude of the change of contact forces at a distance $r$ away from the perturbation. The second response function, $V(r)$, measures the amplitude of the displacements as a function of $r$. A formal definition of these quantities is presented in this section. The numerical results are presented in Sect. III.

We consider assemblies of $N$ particles interacting via finite-range harmonic pair potentials, with a mean number of interactions per particle $2 N_{b} / N=z>2 d$, with $N_{b}$ the total number of interactions. We denote by $U$ the potential energy, $\vec{R}_{k}$ is the position of the $k^{\text {th }}$ particle, and the dynamical matrix is $\overleftrightarrow{M}_{j k} \equiv \frac{\partial^{2} U}{\partial \vec{R}_{j} \partial \vec{R}_{k}}$. We refer to pairs of interacting particles as bonds.

We next consider a displacement field $\delta \vec{R}_{k}$ on the coordinates; to linear order in $\delta \vec{R}_{k}$, this displacement field induces a change $\delta r_{i j}$ in the pairwise distances $r_{i j} \equiv\left\|\vec{R}_{j}-\vec{R}_{i}\right\|$ as
$$
\delta r_{i j} \simeq \vec{n}_{i j} \cdot\left(\delta \vec{R}_{j}-\delta \vec{R}_{i}\right), \quad(1)
$$
where $\vec{n}_{i j}$ is the unit vector pointing from $\vec{R}_{i}$ to $\vec{R}_{j}$. Eq.(1) defines a linear operator that takes vectors from the space of the particles' coordinates, to vectors in the space of bonds, defined here as the set of pairs of particles that interact. We denote the linear operator defined by Eq.(1) as $\mathcal{S}$, and re-write Eq. (1) using a bra-ket notation:
$$
|\delta r\rangle \simeq \mathcal{S}|\delta R\rangle. \quad(2)
$$

We next consider a set of forces $f_{i j}$ on each bond $\langle i j\rangle$, and compute the net force $\vec{F}_{k}$ that results from the bondforces exerted on the $k^{\text {th }}$ particle as
$$
\vec{F}_{k}=\sum_{j(k)} \vec{n}_{j k} f_{j k}, \quad(3)
$$
where $j(k)$ denotes the set of all particles $j$ that interact with particle $k$. Similarly to Eq.(1), Eq.(3) also defines a linear operator, but this time it takes vectors from the space of bonds, to vectors in the space of particles' coordinates. It is easy to show [38] that it is, in fact, the transpose of the operator $\mathcal{S}$ which is defined by Eq.(3), and we can therefore write Eq.(3) in bra-ket notation as
$$
|F\rangle=\mathcal{S}^{T}|f\rangle. \quad(4)
$$

![](./images/867754468119150652_1.jpg)

FIG. 1. Displacement response to a dipolar force, as shown in (c), for spring networks with $N=62500$ nodes, and coordinates $\delta z=0.8$ (a) and $\delta z=0.05$ (b). In this work we extract the lengthscale $\ell_{c}$ that characterizes this response, and study its dependence on coordination and pressure.

We next define $|\alpha\rangle$ as a vector in the space of bonds that has zeros in all components, and has one for the $\alpha$ component, which corresponds to a single bond $\langle i j\rangle$. The operation of $\mathcal{S}^{T}$ on the vector $|\alpha\rangle$ is a coordinate-space dipole vector that can be expressed as $\left(\delta_{j k}-\delta_{i k}\right) \vec{n}_{i j}$, whose squared magnitude is
$$
\left\langle\alpha\left|\mathcal{S} \mathcal{S}^{T}\right| \alpha\right\rangle=\sum_{k}\left(\delta_{j k}-\delta_{i k}\right)\left(\delta_{j k}-\delta_{i k}\right) \vec{n}_{i j} \cdot \vec{n}_{i j}=2. \quad(5)
$$

![](./images/867754468119150652_2.jpg)

FIG. 2. a) Response functions $C(r)$ for spring networks in two dimensions at coordinations as indicated by the legend.
b) Plotting $r^4 C(r)$ reveals the continuum linear elastic behvior at large $r$, and indicates that as $\delta z \to 0$, $C(r) \sim c/r^{-2d}$ with $c$ independent of $z$. c) Plotting $r^4 C(r)$ vs. $r\sqrt{\delta z}$ results in the alignment of the peaks of $r^4 C(r)$ which indicates that the lengthscale dominating this response is $\ell_c \sim 1/\sqrt{\delta z}$. d) Plotting $r^4 C(r)$ vs. the rescaled length $r/\ell^* \sim r\delta z$ does not lead to the alignment of the peaks, reinforcing that $\ell_c \sim 1/\sqrt{\delta z}$ is the relevant lengthscale.

An example of the vector $\mathcal{S}^T |\alpha\rangle$ is depicted in Fig. 1,c.
We consider now the displacement response $|\delta R^{(\alpha)}\rangle$ to a dipolar force $\mathcal{S}^T |\alpha\rangle$:

$$
|\delta R^{(\alpha)}\rangle = \mathcal{M}^{-1} \mathcal{S}^T |\alpha\rangle, \tag{6}
$$

with $\mathcal{M}$ the dynamical matrix. Two examples of $|\delta R^{(\alpha)}\rangle$ for spring networks (see details below) are shown in Fig. (1,a,b). In this work we consider two response functions extracted from these displacement responses to dipolar forces in simple amorphous solids.

Before defining the first response function, we note that the displacement response $|\delta R^{(\alpha)}\rangle$ changes the distance between particles in the entire system. In particular, the change in distance between the particles that form the bond $\beta$, to first order in $||\delta R^{(\alpha)}||$, is given by

$$
\langle \delta R^{\alpha} | \mathcal{S}^T | \beta \rangle = \langle \alpha | \mathcal{S} \mathcal{M}^{-1} \mathcal{S}^T | \beta \rangle \equiv \langle \alpha | \mathcal{A} | \beta \rangle . \tag{7}
$$

Eq. (7) defines a symmetric, non-negative definite linear operator $\mathcal{A}$ of dimension $N_b \times N_b$, which operates on vectors in the space of bonds. We leave the eigenmode analysis of this operator for future work. The matrix elements $\langle \alpha | \mathcal{A} | \beta \rangle$ depend on the distance $r$ between the bonds $\alpha$ and $\beta$, which can be defined as the distance between the mean position of the particles that form each bond. We now define the response function

$$
C(r) \equiv \left[ \langle \alpha | \mathcal{A} | \beta \rangle^2 \right]_r , \tag{8}
$$

where the square brackets denoting averaging over all pairs of bonds $\alpha, \beta$ that are separated by a distance $r$. Continuum linear elasticity predicts $C(r) \sim r^{-2d}$, since $\mathcal{A}$ scales as the gradient of the displacement response, and the latter decays away from the perturbation as $r^{1-d}$.

The second response function we consider in the following is the square of the displacement response at a distance $r$ away from the dipolar force, namely

$$
V(r) \equiv \left[ ||\delta \vec{R}_k^{(\alpha)}||^2 \right]_r , \tag{9}
$$

where this time the square brackets denotes averaging over all particles $k$ that are located at a distance $r$ from the dipolar force applied to the bond $\alpha$. Continuum linear elasticity predicts $V(r) \sim r^{2(1-d)}$, as it is the square of the displacement response, which, as noted above, decays away from the perturbation as $r^{1-d}$.

In the following we use the continuum linear elastic predictions $C(r) \sim r^{-2d}$ and $V(r) \sim r^{2(1-d)}$ to extract the lengthscale $\ell_c$.

## III. RESULTS

In this work we focus on assemblies of particles interacting via harmonic pair-potentials: spring networks and disc packings. The energy is $U = \sum_{i<j} \phi_{ij}$, $\phi_{ij} = \tilde{k}(r_{ij} - d_{ij})^2$ with $\tilde{k}$ a spring constant (set in the following to unity), $d_{ij} = (d_i + d_j)/2$ for harmonic discs with diameters $d_k$, and $d_{ij}$ is the restlength of the $\langle ij \rangle$ spring for the spring networks.

### A. Spring networks

We consider first spring networks in which all of the springs are at their respective rest-lengths, which implies that there are no internal stresses in the system. Networks of up to $N = 10^6$ nodes in two dimensions were prepared following the protocol described in [25], which results in networks having small fluctuations of the coordination amongst the nodes. The mean spring length defines our unit of length.

The response functions $C(r)$ are presented in Fig. 2 for networks of $N = 10^6$ nodes and various coordinations as indicated by the legend. In panel a) we plot the raw functions $C(r)$, which indeed seem to obey the asymptotic linear-elastic prediction $C(r) \sim r^{-2d}$. The

prefactor of this scaling seems to converge to a constant
as $\delta z \to 0$, as can be seen in panel $\mathbf{b)}$, where the products
$r^{2d}C(r)$ are plotted. The increase at large $r$ is an effect
of the periodic boundary conditions. In Fig. 2c we plot
the products $r^{2d}C(r)$ vs. the rescaled length $r\sqrt{\delta z}$. The
alignment of the peaks of the response functions validates
that the lengthscale dominating the response to a local
dipolar force is $\ell_{c} \sim 1/\sqrt{\delta z}$. Beyond $l_{c}$ we find a plateau
as expected for a continuous elastic medium. The lack of
alignment when $r^{2d}C(r)$ is plotted against the rescaled
length $r\delta z$ (see panel $\mathbf{d)}$) supports that $\ell_{c}$ is the relevant
lengthscale for this response, and not $\ell^{*} \sim 1/\delta z$.

![](./images/867754468119150652_3.jpg)

![](./images/867754468119150652_4.jpg)

FIG. 3. a) The products $r^{4}C(r)$ measured in two-dimensional
spring networks of various sizes and coordinations as indi-
cated by the legend. b) The products $r^{4}C(r)$ (squares) and
$r^{4}\tilde{C}(r)$ (circles) measured in packings of harmonic discs at
the pressure $p = 10^{-1}$. Both functions plateau at the same
lengthscale; however, it is apparent that $\tilde{C}(r)$ smooths out
the noise seen in $C(r)$.

In Fig. 3a we plot the products $r^{4}C(r)$ for coordina-
tions $\delta z = 0.8$ and $\delta z = 0.2$, measured in networks of
$N = 250^{2}$, $N = 500^{2}$ and $N = 1000^{2}$ nodes in two dimen-
sions. We find that the system size has no effect on the
response functions at lengths smaller than half the lin-
ear size of the system $r < L/2$. This result demonstrates
the validity of our procedure to extract the lengthscale $\ell_{c}$
from the positions of the peaks of the response functions.

In Fig. 4 we plot the response functions $V(r)$ mea-
sured in spring networks. Panel $\mathbf{a)}$ of Fig. 4 displays the
raw functions, which appear to obey the continuum lin-
ear elastic prediction $V(r) \sim r^{2(1-d)}$ at sufficiently large
$r$. In panel $\mathbf{b)}$ of Fig. 4 the products $r^{2}V(r)$ are plot-
ted vs. the rescaled length $r\sqrt{\delta z}$. The alignment of the
peaks demonstrates that the lengthscale characterizing

![](./images/867754468119150652_5.jpg)

![](./images/867754468119150652_6.jpg)

FIG. 4. a) The response functions $V(r)$ for spring networks in
two dimensions at coordinations as indicated by the legend.
b) The products $r^{2}V(r)$ are plotted vs. the rescaled length
$r\sqrt{\delta z}$. The vertical dashed line demonstrates that the peaks of
the response functions for different coordinations align when
plotted against the rescaled length.

this response function is also $\ell_{c} \sim 1/\sqrt{\delta z}$.

To rationalize these findings, we estimate the sum of
squares of the displacement response to a local dipolar
force (see Eq. (6)), $||\delta R^{(\alpha)}||^{2}$, as
$$
||\delta R^{(\alpha)}||^{2} = \langle \delta R^{(\alpha)} | \delta R^{(\alpha)} \rangle = \langle \alpha | \mathcal{S}\mathcal{M}^{-2}\mathcal{S}^{T} | \alpha \rangle. \quad (10)
$$

We denote by $|\Psi_{\omega}\rangle$ the eigenmode of $\mathcal{M}$ with the as-
sociated eigenvalue $\omega^{2}$. For our unstressed elastic net-
works with $\tilde{k} = 1$, $\mathcal{M} = \mathcal{S}^{T}\mathcal{S}$ [21], and we define
$\omega|\psi_{\omega}\rangle \equiv \mathcal{S}|\Psi_{\omega}\rangle$. The bond-space vectors $|\psi_{\omega}\rangle$ are nor-
malized:
$$
\langle \psi_{\omega} | \psi_{\omega} \rangle = \frac{\langle \Psi_{\omega} | \mathcal{S}^{T}\mathcal{S} | \Psi_{\omega} \rangle}{\omega^{2}} = \frac{\langle \Psi_{\omega} | \mathcal{M} | \Psi_{\omega} \rangle}{\omega^{2}} = 1. \quad (11)
$$

We can thus write Eq. (10) as
$$
||\delta R^{(\alpha)}||^{2} = \sum_{\omega} \frac{\langle \alpha | \mathcal{S} | \Psi_{\omega} \rangle^{2}}{\omega^{4}} = \sum_{\omega} \frac{\langle \alpha | \psi_{\omega} \rangle^{2}}{\omega^{2}}. \quad (12)
$$

The normalization of the vectors $|\psi_{\omega}\rangle$ implies that, upon
averaging over contacts $\alpha$, $\langle \alpha | \psi_{\omega} \rangle^{2} \sim N^{-1}$, and we can
approximate the sum over eigenfrequencies by an integral
over the density of states $D(\omega)$:
$$
||\delta R^{(\alpha)}||^{2} \approx \int \frac{D(\omega)d\omega}{\omega^{2}}. \quad (13)
$$

In our unstressed elastic networks theory predicts [8, 35]
$D(\omega) \sim \delta z^{-d/2}\omega^{d-1}$ for $\omega < \omega^* \sim \delta z$, and $D(\omega) \sim$
constant for $\omega \gtrsim \omega^*$. The lowest mode is expected to
be a plane-wave with a frequency of order $\sqrt{\mu}/L$ with
shear modulus $\mu \sim \delta z$ , and $L$ the linear size of the sys-
tem. We decompose the integral of Eq. (13) as

$$
\begin{aligned}
\left\|\delta R^{(\alpha)}\right\|^{2} & \approx \int \frac{D(\omega) d \omega}{\omega^{2}} \quad(14) \\
& \sim \delta z^{-d / 2} \int_{\sqrt{\mu} / L}^{\omega^{*}} \omega^{d-3} d \omega+\int_{\omega^{*}}^{1} \omega^{-2} d \omega \\
& \sim\left\{\begin{array}{ll}
\frac{1}{\delta z} &, d \geq 3 \\
\frac{1}{\delta z}\left(1+B \log \left(L / \ell_{c}\right)\right) &, d=2
\end{array}.\right.
\end{aligned}
$$

We find that $\left\|\delta R^{(\alpha)}\right\|^{2}$ is dominated by the modes at $\omega^{*}$
(in $d \geq 3$, with logarithmic corrections in $d=2$ ), which
are correlated on the correlation length $\ell_{c}$ according to
effective medium [35, 37]. We therefore expect observ-
ables derived from the response to a local dipolar force,
such as $V(r)$ or $C(r)$, to be characterized by that scale,
as we indeed find.

## B. Packings of harmonic discs

We next show results of a similar analysis performed
on two dimensional packings of soft discs. Packings of
$N=360,000$ bi-disperse harmonic discs with a diameter
ratio 1.4 of were created by quenching a high-temperature
fluid to zero temperature using the FIRE algorithm [39],
and applying compressive or expansive strains followed
by additional quenches to obtain the target pressures.
The diameter of the small discs $d_{0}$ are taken as our units
of length, so that forces and pressure are measured in
units of $\tilde{k} d_{0}$ and $\tilde{k} d_{0}^{2-d}$ respectively.

Unlike unstressed spring networks, in packings parti-
cles exert contact forces on each other. These forces are
known to destabilize packings [24], and indeed they give
rise to much noisier responses compared to the unstressed
networks. To deal effectively with this noise, we define
the response function $\tilde{C}(r)$:

$$
\tilde{C}(r) \equiv \operatorname{median}_{r}\left(\langle\alpha|\mathcal{A}| \beta\rangle^{2}\right), \quad(15)
$$

where the median is taken over all pairs of contacts $\alpha, \beta$
that are separated by a distance $r$ from each other. In
Fig. 3b both response functions $C(r)$ and $\tilde{C}(r)$ measured
in packings at the pressure $p=10^{-1}$ are compared.

In Fig. 5 we plot the response functions $\tilde{C}(r)$ measured
in our two-dimensional packings at pressures indicated
by the legend. We find that although the shape of the
response function $\tilde{C}(r)$ slightly differs from $C(r)$ mea-
sured in spring networks, the main features are similar,
and in particular a crossover to $\tilde{C}(r) \sim r^{-2 d}$ occurs on
the scale $\ell_{c} \sim p^{-1 / 4} \sim \delta z^{-1 / 2}$ (the coordination in har-
monic packings scales as $\delta z \sim \sqrt{p}[20,24]$, verified in the
data of panel d of Fig. 5). Surprisingly, we find that the
fluctuations in $\tilde{C}(r)$ are largest for the highest pressure
$(p=10^{-1})$; we leave the investigation of the nature of
these fluctuations for future work.

![](./images/867754468119150652_7.jpg)

FIG. 5. a) The products $r^{4} \tilde{C}(r)$ measured in packings of
$N=360,000$ harmonic discs in two dimensions. b) Raw
response functions for packings, which scale as $\tilde{C}(r) \sim r^{-2 d}$
at large $r$. The products $r^{2 d} \tilde{C}(r)$ plotted against the rescaled
variable $r p^{-1 / 4}$ reveal the lengthscale $\ell_{c} \sim \delta z^{-1 / 2}$.

## C. Effect of internal stresses

To directly probe the effect of internal stresses on the
response to a local dipolar force, we prepared packings
of $N=10^{6}$ harmonic discs at the packing fraction $\phi=$
0.86 , which have a mean coordination of $z \approx 4.4$ and
mean pressure of $p_{0} \approx 7.6 \times 10^{-3}$. We then consider the
response function $\tilde{C}^{(x)}(r)$ to a local dipolar force, which is
calculated with a dynamical matrix in which the contact
forces are multiplied by a factor $1-x$, namely

$$
\begin{aligned}
\stackrel{\leftrightarrow}{M}_{m q}^{(x)}= & \sum_{\langle i j\rangle}\left(\delta_{m j}-\delta_{m i}\right)\left(\delta_{q j}-\delta_{q i}\right)\left[\tilde{k} \vec{n}_{i j} \vec{n}_{i j}\right. \\
& \left.-(1-x)\left(\stackrel{\leftrightarrow}{I}-\vec{n}_{i j} \vec{n}_{i j}\right) f_{i j} / r_{i j}\right], \quad(16)
\end{aligned}
$$

where $\stackrel{\leftrightarrow}{I}$ is the unit tensor, and the sum is over all con-
tacts $\langle i j\rangle$. The original dynamical matrix (and hence the
original response function $\tilde{C}(r)$ ) is recovered for $x=0$.

![](./images/867754468119150652_8.jpg)

FIG. 6. a) The products $r^{2d}\tilde{C}^{(x)}(r)$ measured in packings of $N=10^{6}$ harmonic discs at the packing fraction $\phi=0.86$, for various factors $x$, see text for details. b) Plotting the rescaled products $r^{2d}\tilde{C}^{(x)}(r)/b^{(x)}$ vs. $r/\ell_{c}^{(x)}$ leads to a collapse for all $x$, from which we extract the lengthscales $\ell_{c}^{(x)}$ and the amplitudes $b^{(x)}$, which are plotted in panel d) on a semi-log scale. e) The lengthscale $\ell_{c}^{(x)}$ vs. the relative proximity to the critical pressure $p_{c}$, see text for details. c) The products $r^{2d}\tilde{C}(r)$ measured for packings at $\phi=0.86$ and various system sizes.

This rescaling of the forces leads to the rescaling of the pressure $p=(1-x)p_{0}$ where $p_{0}$ is the pressure of the original packing.

The products $r^{2d}\tilde{C}^{(x)}(r)$ are plotted in Fig. 6 for various values of $x$ as indicated by the legend. Here we find that the response is governed by an $x$-dependent lengthscale $\ell_{c}^{(x)}$, which is extracted by rescaling the axes by the appropriate lengths and amplitudes (plotted in panel d) of Fig. 6) such that the curves collapse. For distances $r>\ell_{c}^{(x)}$, $\tilde{C}^{(x)}(r)\sim b^{(x)}r^{-2d}$, with an $x$-dependent prefactor $b^{(x)}$.

Our results indicate clearly that the lengthscale $\ell_{c}$ that governs the response to a local dipolar force is sensitive to the presence of internal stresses in the solid, and, in particular, it decreases as the pressure is decreased by rescaling the contact forces. However, the question remains whether $\ell_{c}$ exhibits singular behavior as the internal stresses are increased. We clarify this issue by considering again the dynamical matrix $\mathcal{M}^{(x)}$ given by Eq. (16), and denoting the density of states associated to $\mathcal{M}^{(x)}$ by $D^{(x)}(\omega)$. In the companion paper [37] it is shown that $D^{(x)}(\omega)$ displays an $x$-dependent frequency scale $\omega_{0}(x)$, which characterizes the destabilizing effect of internal stresses. It is shown that for $x_{c}\approx-0.04$, $\omega_{0}(x_{c})$ vanishes, which corresponds to an elastic instability [24, 37]. $x_{c}$ defines a critical pressure $p_{c}=(1-x_{c})p_{0}$ at which this elastic instability occurs. The relative distance of the pressure $p=(1-x)p_{0}$ from the critical pressure $p_{c}$, given $x$, is thus

$$
\frac{p_{c}-p}{p_{c}}=\frac{x-x_{c}}{1-x_{c}}. \tag{17}
$$

When we plot the extracted lengthscale $\ell_{c}^{(x)}$ vs. the relative distance to the critical pressure $(p_{c}-p)/p_{c}$, we find $\ell_{c}^{(x)}\sim\left(\frac{p_{c}-p}{p_{c}}\right)^{-0.27}$, using $x_{c}=-0.04$, see panel e) of Fig. 6. This result suggests that (i) our original harmonic disc packings dwell at a pressure $p_{0}$ that is a fraction $(1-x_{c})^{-1}\approx96\%$ of the critical pressure $p_{c}$, i.e. very close to marginal stability [21, 24], and (ii) the lengthscale $\ell_{c}^{(x)}$ diverges at the critical pressure $p_{c}$. Although our variation of $\ell_{c}^{(x)}$ is mild due to the smallness of the exponent, there is no fitting involved once $x_{c}$ is independently determined, supporting that the power-law is genuine.

We finally discuss the possibility that the critical pressure $p_{c}$ approaches the pressure $p_{0}$ at which our packings dwell in the thermodynamic limit. If indeed $\ell_{c}^{(x)}$ diverges with proximity to the critical pressure $p_{c}$, assuming that $p_{c}\to p_{0}$ as $N\to\infty$ would imply that $\ell_{c}^{(x)}$ should increase as $N$ is increased. To rule out this possibility, we plot in panel c) of Fig. 6 the products $r^{4}\tilde{C}(r)$ measured in packings of $N=250^{2},N=500^{2}$, and $N=1000^{2}$, at the packing fraction $\phi=0.86$. We find that the lengthscale $\ell_{c}=\ell_{c}^{(x=0)}$ which characterizes these response functions does not change with increasing the system size $N$.

## IV. DISCUSSION

In elastic networks at zero pressure, our results support our earlier claim [26] that $\ell^{*}\sim1/\delta z$ is a point-to-set length associated with the dependence of mechanical stability on pinning or cutting boundaries, whereas the length $\ell_{c}\sim1/\sqrt{\delta z}$ characterizes the zero-frequency point response and two-point correlation functions, as justified here based on former results from effective medium. Note that the presence of two length scales is not related to the fact that in particle packings the longitudinal and transverse speed of sound scale differently, as proposed in [29]. Indeed in elastic networks both the shear and bulk moduli can be made to scale identically [21, 27], and these two length scales still differ. More work is needed to understand which of these length scales characterize certain finite size effects [26, 29, 40].

When pressure is increased toward a critical value $p_c$ at which the system becomes elastically unstable, we expect both $\ell^*$ and $\ell_c$ to grow. Our results are consistent with a divergence of $\ell_c \sim 1/(p_c-p)^{1/4}$. Our results (see also [37]) suggest that sphere packings are very close to, but at a finite distance from, an elastic instability with $(p_c-p)/p_c \approx 0.05\%$ independently of coordination, implying that $\ell_c$ in elastic networks at rest and in packings are proportional, thus depending on coordination as $\ell_c \sim 1/\sqrt{\delta z}$ in both cases. Our prediction of a diverging length scale near an elastic instability could be tested in various contexts, for example near an amorphization transition where the distance to the instability can be controlled by monitoring disorder [41], and experimentally in shaken grains [42] or colloidal systems [43].

These results resemble predictions of Mode Coupling Theory (MCT), believed to describe some kind of elas- tic instability [15–17]. MCT predicts a *dynamical* length scale $\xi$ diverging as $\xi \sim |T-T_c|^{-1/4}$. This is the same exponent as in our observation of a length $\ell_c \sim (p_c-p)^{-1/4}$ characterizing the zero-frequency response, since pressure and temperature should be linearly related. We observe that this scaling of $\ell_c(p)$ goes as the inverse boson peak frequency $\omega_{BP}(p)$ as predicted using effective medium in a companion paper [37], but this correspondence is currently unexplained. Overall, a systematic comparison between mode coupling and effective medium -in particu- lar on the length scales involved in each approach- would be valuable to clarify the relationship between dynamics and elasticity in supercooled liquids.

## ACKNOWLEDGMENTS

Acknowledgments: We thank Jie Lin, Le Yan and Marija Vucelja for discussions. MW acknowledges sup- port from NSF CBET Grant 1236378, NSF DMR Grant 1105387, and MRSEC Program of the NSF DMR- 0820341 for partial funding. GD acknowledges support from CONICYT PAI/Apoyo al Retorno 82130057.

[1] T. S. Majmudar and R. P. Behringer, Nature **435**, 1079 (2005).
[2] S. Majumdar, O. Narayan, and T. Witten, Science **269**, 513 (1995).
[3] A. C. Anderson, in *Amorphous Solids, Low Temperature Properties*, edited by W. A. Phillips (Springer, Berlin, 1981).
[4] F. Sette, M. H. Krisch, C. Masciovecchio, G. Ruocco, and G. Monaco, Science **280**, 1550 (1998).
[5] G. Monaco and S. Mossa, Proc. Nat. Acad. Sci. **106**, 16907 (2009).
[6] V. Lubchenko and P. G. Wolynes, Proceedings of the National Academy of Sciences **100**, 1515 (2003).
[7] W. Schirmacher, G. Ruocco, and T. Scopigno, Phys. Rev. Lett. **98**, 025501 (2007).
[8] M. Wyart, S. R. Nagel, and T. A. Witten, EPL **72**, 486 (2005).
[9] N. Tao, G. Li, X. Chen, W. Du, and H. Cummins, Phys- ical Review A **44**, 6665 (1991).
[10] A. I. Chumakov, I. Sergueev, U. van B¨urck, W. Schirma- cher, T. Asthalter, R. R¨uffer, O. Leupold, and W. Petry, Phys. Rev. Lett. **92**, 245508 (2004).
[11] M. Goldstein, J. Chem. Phys. **51**, 3728 (1969).
[12] J. Kurchan and L. Laloux, J. Phys. A **29**, 1929 (1996).
[13] T. S. Grigera, A. Cavagna, I. Giardina, and G. Parisi, Phys. Rev. Lett. **88**, 055502 (2002).
[14] C. Brito and M. Wyart, J. Chem. Phys. **131**, 024504 (2009).
[15] G. Biroli, J.-P. Bouchaud, K. Miyazaki, and D. R. Re- ichman, Phys. Rev. Lett. **97**, 195701 (2006).
[16] S. Franz and A. Montanari, J. Phys. A **40**, F251 (2007).
[17] A. Montanari and G. Semerjian, Journal of statistical physics **124**, 103 (2006).
[18] F. Leonforte, A. Tanguy, J. P. Wittmer, and J.-L. Bar- rat, Phys. Rev. B **70**, 014203 (2004).
[19] F. Leonforte, R. Boissi`ere, A. Tanguy, J. P. Wittmer, and J.-L. Barrat, Phys. Rev. B **72**, 224206 (2005).

[20] C. S. O’Hern, L. E. Silbert, A. J. Liu, and S. R. Nagel, Phys. Rev. E **68**, 011306 (2003).
[21] M. Wyart, Annales de Phys **30 (3)**, 1 (2005).
[22] A. J. Liu, S. R. Nagel, W. van Saarloos, and M. Wyart, in *Dynamical heterogeneities in glasses, colloids, and gran- ular media*, edited by L.Berthier, G. Biroli, J. Bouchaud, L. Cipeletti, and W. van Saarloos (Oxford University Press, Oxford, 2010).
[23] M. Van Hecke, Journal of Physics: Condensed Matter **22**, 033101 (2010).
[24] M. Wyart, L. E. Silbert, S. R. Nagel, and T. A. Witten, Phys. Rev. E **72**, 051306 (2005).
[25] M. Wyart, H. Liang, A. Kabla, and L. Mahadevan, Phys. Rev. Lett. **101**, 215501 (2008).
[26] G. During, E. Lerner, and M. Wyart, Soft Matter **9**, 146 (2013).
[27] W. G. Ellenbroek, Z. Zeravcic, W. van Saarloos, and M. van Hecke, EPL (Europhysics Letters) **87**, 34004 (2009).
[28] M. Mailman and B. Chakraborty, Journal of Statisti- cal Mechanics: Theory and Experiment **2011**, L07002 (2011).
[29] S. S. Schoenholz, C. P. Goodrich, O. Kogan, A. J. Liu, and S. R. Nagel, Soft Matter , DOI:10.1039/C3SM51096D (2013).
[30] B. P. Tighe, Physical review letters **109**, 168303 (2012).
[31] J. Maxwell, Philos. Mag. **27**, 294 (1864).
[32] L. E. Silbert, A. J. Liu, and S. R. Nagel, Phys. Rev. Lett. **95**, 098301 (2005).
[33] V. Vitelli, N. Xu, M. Wyart, A. J. Liu, and S. R. Nagel, Phys. Rev. E **81**, 021301 (2010).
[34] A. Ikeda, L. Berthier, and G. Biroli, The Journal of Chemical Physics **138**, 12A507 (2013).
[35] M. Wyart, Europhys. Lett. **89**, 64001 (2010).
[36] W. G. Ellenbroek, E. Somfai, M. van Hecke, and W. van Saarloos, Phys. Rev. Lett. **97**, 258001 (2006).
[37] E. DeGiuli, et al., in progress (2013).

[38] E. Lerner, G. Düring, and M. Wyart, (2011), arXiv 1111.7225.

[39] E. Bitzek, P. Koskinen, F. Gähler, M. Moseler, and P. Gumbsch, Phys. Rev. Lett. 97, 170201 (2006).

[40] C. F. Moukarzel, EPL (Europhysics Letters) 97, 36008 (2012).

[41] H. Mizuno, S. Mossa, and J.-L. Barrat, arXiv preprint arXiv:1308.5135 (2013).

[42] C. Coulais, R. Behringer, and O. Dauchot, Soft Matter (2013).

[43] K. Chen, W. G. Ellenbroek, Z. Zhang, D. T. Chen, P. J. Yunker, S. Henkes, C. Brito, O. Dauchot, W. Van Saar- loos, A. J. Liu, *et al.*, Physical review letters 105, 025501 (2010).