# Entrainment coefficient and effective mass for conduction neutrons in neutron star crust : simple microscopic models

Brandon Carter$^a$, Nicolas Chamel$^a$, Pawel Haensel$^{a,b}$

$^a$ Observatoire de Paris, 92195 Meudon, France
(Brandon.Carter@obspm.fr, Nicolas.Chamel@obspm.fr)
$^b$ N. Copernicus Astronomical Center, Warsaw, Poland
(haensel@camk.edu.pl)

November 1, 2018

**Abstract.** In the inner crust of a neutron star, at densities above the "drip" threshold, unbound "conduction" neutrons can move freely past through the ionic lattice formed by the nuclei. The relative current density $n^i = n \bar{v}^i$ of such conduction neutrons will be related to the corresponding mean particle momentum $p_i$ by a proportionality relation of the form $n^i = \mathcal{K} p^i$ in terms of a physically well defined mobility coefficient $\mathcal{K}$ whose value in this context has not been calculated before. Using methods from ordinary solid state and nuclear physics, a simple quantum mechanical treatment based on the independent particle approximation, is used here to formulate $\mathcal{K}$ as the phase space integral of the relevant group velocity over the neutron Fermi surface. The result can be described as an "entrainment" that changes the ordinary neutron mass $m$ to a macroscopic effective mass per neutron that will be given – subject to adoption of a convention specifying the precise number density $n$ of the neutrons that are considered to be "free" – by $m_\star = n/\mathcal{K}$. The numerical evaluation of the mobility coefficient is carried out for nuclear configurations of the "lasagna" and "spaghetti" type that may be relevant at the base of the crust. Extrapolation to the middle layers of the inner crust leads to the unexpected prediction that $m_\star$ will become very large compared with $m$.


## 1 Introduction

The main purpose of this article is to show how a mean field treatment of neutron star crust matter can be used to address the previously unsolved problem of evaluating a quantity, namely the relevant neutron mobility coefficient $\mathcal{K}$ , that is essential for the astrophysical applications that will be described in a separate article [1]. In terms of the relevant number density $n$ of effectively unbound neutrons, this coefficient determines a corresponding effective mass $m_\star = n/\mathcal{K}$ that characterises their average motion on a macroscopic scale (meaning one that is large compared with the spacing between nuclei) and that we therefore refer to as the macro mass, to distinguish it from the microscopic effective mass, $m^\oplus$ say, characterising the dynamics of the neutrons on subnuclear scales. Whereas $m^\oplus$ is well known to be typically rather smaller than the ordinary neutron mass $m$ , we reach the previously unexpected conclusion that there is likely to be a strong "entrainment" effect whereby the macro mass $m_\star$ will typically become large, and in some layers extremely large, compared with $m$ .

A secondary purpose of this article is to draw the attention of nuclear theorists to the potentialities of the almost entirely unexplored branch of theoretical astrophysical nuclear physics that needs to be developed for this and many other purposes. The only relevant work of which we are aware so far is that of Oyamatsu and Yamada [2], who appear to be the only ones to have taken proper account of the neutron scattering by the nuclei inside the inner crust by the use of appropriate Bloch type periodicity conditions of the kind commonly employed for the treatment of electrons in ordinary terrestrial solid state physics. Their treatment however was restricted to a simple one dimensional model.

Under the conditions of ordinary terrestrial solid state physics, and even at the much higher densities characterising the matter in a white dwarf star, long range electric forces keep the nuclei so far apart that, in so far as the much stronger but short range nuclear interactions are concerned, each individual nucleus can be treated separately as if it were isolated. Until quite recently [2], such a separate treatment of individual nuclei (considered as if isolated each in its own cell - with Wigner Seitz type boundary conditions) has been used in nearly all quantum mechanical calculations on neutron star crust matter since the pioneer work of Negele and Vautherin [3]. That kind of approximation is fully justifiable in the outer crust , where the densities are not too much greater than those found in a white dwarf. However such a treatment can no longer be considered entirely satisfactory in the inner crust, meaning the part with density above the "neutron drip" threshold at about $10^{11}\ \mathrm{g/cm^3}$, where there are unconfined neutrons that travel between neighbouring nuclei, which thereby cease to be effectively isolated from one another.

While desirable for accuracy throughout the inner crust, a proper collective rather than individual treatment of the nuclei becomes not just desirable but absolutely essen- tial for treating the problem with which Oyamatsu and Yamada [2] [4] were concerned, namely that of the nuclear matter inside neutron star crust. Such a treatment is also essential for treating the problem with which the present work is concerned, namely

that of stationary but non static configurations in which a neutron current flows relative to the lattice formed by the nuclei, something that obviously can not be discussed in the usual approach that treats the nuclei as if they were isolated in individual (e.g. Wigner Seitz type) boxes.

The flow of neutrons is treated here as a perturbation of a zero temperature ground state characterised just by the location of the relevant Fermi surface in momentum space. We thereby obtain provisional rough estimates of the relevant mobility coefficient which suggest that (unlike what occurs in the fluid core and on a microscopic scale) the macro mass $m_\star$ that effectively characterises the neutron motion on a macroscopic scale can become very large compared with the ordinary neutron mass $m$ , particularly in the middle part of the conducting layer, for which three dimensional numerical results will be presented in a follow up article [6]. The present article deals more specifically with simplified rod and plate type models that are relevant near the crust core interface, where the mass enhancement will be less extreme.

Bulgac, Magierski and Heenen have recently pointed out the importance of shell effects induced by unbound neutrons in neutron star crust by evaluating the Casimir energy for neutron matter in the presence of inhomogeneities from a semiclassical approach and more recently by performing a Skyrme Hartree-Fock calculation with ordinary periodic boundary conditions (see [7, 8] and references therein). However this kind of boundary conditions does not properly account for Bragg scattering of dripped neutrons and is only a particular case of the more general Bloch type boundary conditions.

In the absence of any previous quantum mechanical calculation whereby nuclei on a crystal lattice are treated collectively (apart from the 1D calculation previously mentionned [2]), even at the simplest level of approximation, we shall adopt the simple model suggested by Oyamatsu and Yamada, supplemented with Bloch type boundary conditions, in order to estimate the effective neutron mass $m_\star$ . This model treats the neutrons as independent fermions subject to an effective potential. We wish to draw the attention of nuclear theorists to the problem of including Bloch boundary conditions in more sophisticated approximation schemes as a challenge for future work.

In the mean time, experience with the analogous problem of electron transport in ordinary solid state physics suggests that the results obtained from the Oyamatsu Yamada type treatment used here should not be too bad as a first approximation. Further encouragement comes from our own recent attempt to take up the challenge of allowing for coupling by an appropriate adaptation of the standard BCS pairing theory on which the prediction of neutron superfluidity (in the relevant low to moderate temperature range) is based: the upshot [9] is that (although it is essential for the inhibition of resistivity) as far as the "entrainment" phenomenon is concerned the effect of the ensuing pairing "gap" will not be very large nor very difficult to calculate.

## 2 Microscopic description of conduction neutrons in the inner crust

### 2.1 Single-particle Schrödinger equation

The basic principle of the conductivity model we wish to adapt from ordinary solid state theory to the context of a neutron star crust is that the "conduction band", and perhaps also some of the highest "confined" levels, can be analysed within the independent particle approximation, in terms of energy eigenstates for a single particle described by a Bloch type wave function $\varphi$ , satisfying the Bloch periodic boundary conditions as discussed below. In the rest frame of the crust, with respect to which the system will be assumed to be in stationary equilibrium, the single particle wave function will be taken to be governed by a Hamiltonian operator $\mathcal{H}$ that is given by

$$
\mathcal{H}=-\hbar^{2} \nabla_{i} \frac{\gamma^{i j}}{2 m^{\oplus}} \nabla_{j}+V, \tag{2.1}
$$

where $\gamma^{i j}$ is just the space metric, while $V$ is the single particle potential, and $m^{\oplus}$ is the relevant local effective mass parameter.

The potential $V$ and the effective mass $m^{\oplus}$ will be periodic in the case of a regular crystalline solid lattice, though not for a fluid configuration such as will be relevant at higher temperatures. The value of the effective potential $V$ (and the associated deviation of the effective mass $m^{\oplus}$ from $m$ ) is supposed to allow not just for the attraction of the confined protons in the nuclei but also for the mean effect of the other fermions, which are electrons in the familiar solid state applications, but neutrons in the context under consideration here.

### 2.2 Boundary conditions

The preceding considerations apply even to disordered (glass like or liquid) configura- tions, but in order to proceede we shall now restrict our attention to cases for which the nuclei are assumed to be fixed and locally distributed in a regular crystal lattice configuration, in which an elementary cell consists of a parallelopiped of volume $\mathcal{V}_{\text {cell }}$ say spanned by a triad of basis vectors $\mathbf{e}_{a}$ labelled by an index with values $a=1$, 2, 3, so that the system is invariant with respect to translations generated by vectors of the form

$$
\mathbf{T}=\ell^{a} \mathbf{e}_{a} \tag{2.2}
$$

for integer values of the coefficients $\ell^{a}$ (in the following summation over repeated indices is assumed). This so called adiabatic or Born-Oppenheimer approximation is

justified by the large difference between the neutron and nucleus masses, since typically each nucleus contains several hundred nucleons [10].

It follows directly from the well-known Floquet-Bloch theorem [11] that the single particle wave function has to satisfy the following boundary conditions

$$
\varphi_{\mathbf{k}}\{\mathbf{r}+\mathbf{T}\}=\mathrm{e}^{\mathrm{i} \mathbf{k} \cdot \mathbf{T}} \varphi_{\mathbf{k}}\{\mathbf{r}\}. \tag{2.3}
$$

where $\mathbf{k}$ is the Bloch momentum covector.

It will therefore suffice to solve the Schrödinger equation just inside a single elemen- tary cell. Instead of using a primitive cell of parallelopiped, it is convenient for many purposes to work instead with the Wigner-Seitz (W-S) cell defined as the set of points that are closer to a given lattice node than to any other. Such a cell exhibits the full symmetry of the lattice. Its shape is determined by the crystal structure, a polyhedron in general, for instance a cube in a simple cubic lattice. This exactly defined W-S cell should not be confused with the widely employed eponymous "W-S approximation" [12] which consists in replacing this cell by a sphere (or more generally any convenient cell that simplifies the analysis).

The Bloch momentum $\mathbf{k}$ takes values inside the first Brillouin zone (B-Z), which is the W-S cell of the reciprocal lattice whose nodes are located at $\mathbf{K}=\ell_{a} \mathbf{l}^{a}$ for integer values of the coefficients $\ell_{a}$ where the dual basis vectors $\mathbf{l}^{a}$ are defined by the following scalar products

$$
\mathbf{l}^{a} \cdot \mathbf{e}_{b}=2 \pi \delta^{a}{ }_{b}, \tag{2.4}
$$

the $2 \pi$ normalization factor being introduced for convenience.

It must be emphasized that the single particle wave function will have to satisfy the relation (2.3) between two opposite faces of the cell. This means in particular that the Schrödinger equation has to be solved for each wave vector $\mathbf{k}$ inside the first B-Z. The ordinary periodic boundary conditions on the cell, which have been recently applied by Magierski and Heenen [8], are thus only a restricted subset of solutions, namely those with $\mathbf{k}=0$.

For each momentum $\mathbf{k}$, there exists only a discrete set of energy eigenvalues satis- fying the Bloch boundary conditions. The single particle energy spectrum is therefore a collection of sheets in momentum space, each sheet usually being referred as a band (labelled by the principal quantum number).

## 3 Microscopic dynamics in mean field of lattice
### 3.1 From microscopic to macroscopic observables

The linearisation involved in the neglect of direct two body or many body interactions in such a mean field treatment excludes allowance for higher order effects such as the

pairing responsible for a superfluid energy gap, but as discussed in a separate article [9], this limitation should not matter too much for the evaluation of the basic equation of state of the fluid, since the main effect of superfluidity is not to modify the equation of motion but just to restrain the class of the admissible solutions (by allowing only those that are irrotational).

The main limitation on the use of such a linearisation is that it makes sense only for configurations that do not differ too much from the static reference configuration on which the estimation of the effective potential energy function $V$ is based.

### 3.2 Fermi surface in ground state configuration
The zero temperature configuration is obtained by minimising an energy density $U$ subject to the constraint of a given value of the neutron density $n_\mathrm{n}$ , defined by

$$
n_{\mathrm{n}}=\int \frac{\mathrm{d}^{3} k}{(2 \pi)^{3}}. \tag{3.1}
$$

The energy density is expressible in terms of the single particle energies (in this work, we shall use braces instead of ordinary brackets for functional dependence, in order to avoid possibly confusion with simple multiplication)

$$
\mathcal{H} \varphi_{\mathbf{k}}=\mathcal{E}\{\mathbf{k}\} \varphi_{\mathbf{k}}, \tag{3.2}
$$

by an expression of the form

$$
U=U\{0\}+\int \mathcal{E}\{\mathbf{k}\} \frac{\mathrm{d}^{3} k}{(2 \pi)^{3}}, \tag{3.3}
$$

where, as a standard postulate, the contribution $U\{0\}$ is ignored in the minimisation procedure. This means that all single particle states of energy up to but not beyond some particular Fermi level, $\mu$ say, are occupied. This Fermi energy specifies the "Fermi surface", namely the locus, $S_{\mathrm{F}}$ say, in momentum space, where

$$
\mathcal{E}\{\mathbf{k}\}=\mu. \tag{3.4}
$$

It must be emphasised that the Fermi surface will in general consist of *disconnected* pieces unlike the homogenous case in which the Fermi surface is simply a sphere. From the property that $\mathcal{E}\{\mathbf{k}\}=\mathcal{E}\{-\mathbf{k}\}$, the ground state is thus completely symmetric in the sense that its total momentum density $\int \mathrm{d}^{3} k k^{i}$ vanishes. This is a generalized version of Unsöld theorem [13] according to which the all electron wave function of a closed shell atom is spherically symmetric.

### 3.3 Minimal conducting configurations

Our main concern in the present analysis is with current carrying configurations, as characterised by some given value of the physically well defined number current density with components $n^i$ given by

$$
n^i = \int v^i \frac{\mathrm{d}^3 k}{(2\pi)^3} \tag{3.5}
$$

in which the transport velocity $v^i$ is given by the formula

$$
v^i = \frac{1}{\hbar} \frac{\partial \mathcal{E}}{\partial k_i} . \tag{3.6}
$$

The kind of current carrying configurations that will presumably be relevant in the low temperature limit will be those for which the energy density $U$ is minimised for a given value of the neutron density $n_{\mathrm{n}}$ subject to the further constraint that the number current density also has the prescribed value $n^i$. It is evident that this constrained minimisation condition requires that the occupied states should consist just of those subject to an inequality of the form

$$
\mathcal{E} \leq \mu + p_i v^i , \tag{3.7}
$$

for some fixed covector whose constant components $p_i$ have been introduced as Lagrange multipliers. The phase space volume specified in this way will have a boundary characterised by the condition

$$
\mathcal{E} = \mu + p_i v^i , \tag{3.8}
$$

which specifies a modified Fermi surface, $S$ say. The constraint of having a finite current breaks the symmetry and will thus necessarily lead to a new ground state with a non vanishing total momentum density vector $\int \mathrm{d}^3 k \, k^i \neq 0$ .

### 3.4 The uniform displacement of the Fermi surface

To justify the use of a Schrödinger type Hamiltonian $\mathcal{H}$ involving an effective potential of the same form as in the zero current case, we need to assume that (as will presumably be the case in the relevant context of pulsar glitches) the current density $n^i$ is small enough to be treated by linear perturbation theory. This means that the Lagrange multiplier $p_i$ should itself be considered just as a first order perturbation, having zero

![](./images/867773705680323305_1.jpg)

Figure 1: Sketch of energy against wave number, showing uniform displacement attributable to current.

value $p_i = 0$ in the static unperturbed configuration, and $p_i = \delta p_i$ in the perturbed current carrying configuration. For a given (unchanged) value of the chemical potential $\mu$, the difference between the new value (3.8) and the old value (3.4) of the Fermi energy level $\mathcal{E}$ will be given to first order by $\delta \mathcal{E} = \delta(p_i v^i) = v^i \delta p_i$ and thus in terms of the perturbed value of $p_i$ simply by

$$
\delta \mathcal{E} = p_i v^i. \tag{3.9}
$$

This change in energy can be interpreted as being attributable to a phase space displacement $\delta k_i$. Since this change will be given, according to (3.6), by

$$
\delta \mathcal{E} = \hbar v^i \delta k_i, \tag{3.10}
$$

it can be seen that the simplest possibility is to take the displacement to have the uniform value given just by

$$
\hbar \delta k_i = p_i, \tag{3.11}
$$

as illustrated on figure 1.

### 3.5 Relation between current and momentum
The relation (3.11) means that (in the infinitesimal limit) the Lagrange multipliers $p_i$ can be physically interpreted simply as components of a uniform pseudo momentum displacement of the occupied phase space region, and of its "Fermi surface" boundary.

The effect of this displacement on the Fermi surface element $\mathrm{d}S_{\mathrm{F}}{}^{i}$ as given – in terms of the corresponding surface measure element, $\mathrm{d}S_{\mathrm{F}}$ – by

$$
\mathrm{d}S_{\mathrm{F}}{}^{i} = (v^i / v)\mathrm{d}S_{\mathrm{F}}, \tag{3.12}
$$


will be to sweep out an infinitesimal phase space volume element given by

$$
\hbar \mathrm{d}^{3} k=p_{i} \mathrm{d} S_{\mathrm{F}}^{i}. \tag{3.13}
$$

It follows that, for the integral over the occupied region of any phase space function $f$, the difference between the value for the displaced (conducting) configuration and the value for the non conducting reference configuration will be given (to linear order) by the formula

$$
\hbar \delta \int f \mathrm{d}^{3} k=p_{i} \oint_{\mathrm{F}} f \mathrm{d} S_{\mathrm{F}}^{i}, \tag{3.14}
$$

in which it is to be understood that the integral on the right is taken over the entire Fermi surface.

We have already pointed out that the energy function $\mathcal{E}$ will be symmetric with respect to the origin, hence it follows that the Fermi surface element $\mathrm{d} S_{\mathrm{F}}^{i}$ will be antisymmetric about the origin so that its unweighted integral $\oint_{\mathrm{F}} \mathrm{d} S_{\mathrm{F}}^{i}$ will self cancel to give zero. We can thus see from (3.14) that for any phase space function $f$ that is symmetric about the origin the corresponding integral will be unaffected by the displacement, i.e. we shall get $\delta \int f \mathrm{d}^{3} k=0$. This contrasts with the case of an antisymmetric function, for which it is the unperturbed integral that will vanish, i.e. we shall have $\int f \mathrm{d}^{3} k=0$ in the static reference configuration, so that the corresponding value for the conducting configuration will be given by $\int f \mathrm{d}^{3} k=\delta \int f \mathrm{d}^{3} k$.

The antisymmetric case is illustrated by the application with which this work is principally concerned, namely the current density $n^{i}$ given by (3.5). Since we have $n^{i}=0$ in the reference configuration characterised by $p_{i}=0$, we shall have $n^{i}=\delta n^{i}$ in the conducting configuration characterised by $p_{i}=\delta p_{i}$. Thus by substituting $v^{i}$ for $f$ in (3.14) we see that in the linearised limit the current will be related to the pseudo momentum displacement $p_{i}$ by a relation of the form

$$
n^{i}=\mathcal{K}^{i j} p_{j}, \tag{3.15}
$$

in which the symmetric tensor $\mathcal{K}^{i j}$ is given as an integral over the Fermi surface by

$$
\mathcal{K}^{i j}=\frac{1}{(2 \pi)^{3} \hbar} \oint_{\mathrm{F}} \frac{v^{i} v^{j}}{v} d S_{\mathrm{F}}. \tag{3.16}
$$

Before continuing, it is to be remarked that this tensor $\mathcal{K}^{i j}$ is interpretable as being proportional to the zero temperature limit of the electric conductivity tensor $\sigma^{i j}$, defined in the usual way by $j^{i}=\sigma^{i j} \mathrm{E}_{j}$ where $\mathrm{E}_{j}$ is the relevant electric field and $j^{i}$ the electric current density, by a relation of the form $\sigma^{i j}=\tau e^{2} \mathcal{K}^{i j}$, where $\tau$ is the relevant relaxation time and $e$ the electric charge per particle.

In a entirely disordered (liquid or glass like) state the form of the energy function $\mathcal{E}$ and the consequent location in phase space of the Fermi surface will be difficult to evaluate theoretically, but there will be the partially compensating simplification that the result will automatically be isotropic. In the mathematically simpler case of a cubic crystalline lattice that is expected [14] to occur in a neutron star crust, this tensor $\mathcal{K}^{ij}$ will have the isotropic form

$$
\mathcal{K}^{ij} = \mathcal{K}\gamma^{ij} , \tag{3.17}
$$

in which the scalar coefficient will evidently be given by

$$
\mathcal{K} = \frac{1}{3}\gamma_{ij}\mathcal{K}^{ij} . \tag{3.18}
$$

However that may be, it can be seen from (3.16) that the scalar coefficient $\mathcal{K}$ will be given by a Fermi surface integral of the simple form

$$
\mathcal{K} = \frac{1}{3(2\pi)^3\hbar} \oint_{\mathrm{F}} v \mathrm{d}S_{\mathrm{F}} . \tag{3.19}
$$

In terms of this integral, the relation between current and momentum will be given by

$$
n^i = \mathcal{K}\gamma^{ij}p_j . \tag{3.20}
$$

### 3.6 The (cut-off dependent) concept of the effective mean mass

In order to relate the formula (3.19) to expressions used elsewhere in the literature, it is to be noted that we can introduce a mean velocity vector $\bar{v}^i$ and a conduction neutron density $n$ such that the current density can be expressed by

$$
n^i = n\bar{v}^i . \tag{3.21}
$$

Subject to the isotropy condition (3.17), the (pseudo) momentum covector $p_i$ will be expressible in terms of the corresponding covector $\bar{v}_i = \gamma_{ij}\bar{v}^j$ in the simple form

$$
p_i = m_\star \bar{v}_i , \tag{3.22}
$$

in which the effective mean particle mass $m_\star$ – which we refer to as the "macro mass" in order to distinguish it from the locally effective ""micro mass" $m^\oplus$ – is defined in

terms of the integral (3.19) by the relation

$$
\frac{1}{m_{\star}}=\frac{\mathcal{K}}{n}. \tag{3.23}
$$

It is however to be remarked that whereas the specification of quantities such as $p_{i}$ and $\mathcal{K}$ is physically unambiguous, the specification of the effective mass $m_{\star}$ , like that of the mean transport velocity $\bar{v}^{i}$ , depends on how many "conduction states" are counted in the definition of the number density $n$ , and how many are left aside as dynamically inert "confined" states.

In the application to a neutron star crust, the situation is somewhat simpler than is usual in ordinary solid state physics because the relevant single particle Hamiltonian (2.1) will usually involve an effective potential function $V$ that tends rapidly [15] towards an almost exactly uniform value outside the ionic nuclei to which all the protons and some of the neutrons are effectively confined. It should be noticed that the single particle wave function of bound states will be vanishingly small at the W-S cell boundary and therefore those states will not be sensitive to the Bloch phase shift. The resulting single particle energies will thus be nearly independent of the Bloch momentum which means that the associated group velocities will be very small. The single particle energy spectrum can therefore be decomposed into a subset consisting of such confined states, and a remainder that will realistically be describable as "conduction" states. The separation between those two different subsets is not entirely sharp (borderline states are commonly refered to as valence states in ordinary solid state physics) and one has to rely on a more or less arbitrary convention.

In most layers of a neutron star crust, the most convenient possibility is usually to take the uniform value of $V$ outside nuclei, which can be taken as the energy origin, to specify a corresponding energy range $\mathcal{E}>0$ characterising "conduction" states. This specification may however be ambiguous in the bottom layers of the inner crust where nuclei are very close to each other. In order to deal with such cases, we shall adopt the convention, which agrees with the previous one when nuclei are very far apart, that conduction states are defined as states whose energy is larger than the maximum value of the potential.

It is to be remarked that in the uniform limit whereby the periodic potential $V$ and the local effective mass $m^{\oplus}$ are simply constants, the resulting Fermi surface is a sphere and the evaluation of the mobility scalar is straightforward. In this case, the associated macro mass is just equal to the micro mass $m_{\star}=m^{\oplus}$ provided all neutron states are counted as conduction states.

## 4 Quantitative estimates of the mobility tensor

### 4.1 Bottom layer of the inner crust

We shall focus for simplicity on the bottom of the inner crust near saturation density of the order of $10^{14} \mathrm{~g} / \mathrm{cm}^{3}$ where the transition to homogeneous fluid neutron matter

![](./images/867773705680323305_2.jpg)

Figure 2: Nuclear configurations for hexagonal spaghetti (rod) and lasagna (slab) lattices. Black - nuclear matter; grey - neutron gas. From [4], with kind permission of the author.

takes place, to evaluate the mobility scalar and the effective mass. In this region the crystal lattice is not expected to substantially alter the transport properties such as the mobility tensor. The aim of the following sections is not to provide astrophysically important information but rather to give some insight that may be valuable in the more general cases that will be dealt with in future work. Near the base of the crust, the nuclei are so strongly deformed by their neighbours that they may adopt non spherical shapes [16], sometimes idealised by 1D or 2D configurations such as slabs and rods respectively, which greatly simplifies the analysis. These "exotic" crust phases are illustrated on figure 2 taken from the work of Oyamatsu [4].

In views of the exploratory character of the present work, we shall use a simple model for the single particle equation. In particular, we shall drop the condition of strict self-consistency, and shall use a mean field model based on the work of Oyamatsu [4, 2]. He calculated the structure of the ground state of the inner neutron star crust using a phenomenological energy-density functional, fitted on the first hand to the smoothed nuclear masses and charged radii of laboratory nuclei on the $\beta$ stability line and on the other hand adjusted on the equation of state of pure neutron matter from the variational calculations of Friedman and Pandharipande [5] using two body as well as three body nucleon-nucleon interactions. He further investigated with Yamada the importance of shell effects with a single particle Schrödinger equation in the W-S approximation [2] (the reader is refered to those two papers for the details).

Unlike the calculations carried out by these authors, we shall apply the 1D or 2D Bloch type boundary conditions and we shall not make any approximations about the shape of the W-S cells which partition the crystal. The 3D configurations require specific numerical techniques and will be discussed in a separate work [6]. For consistency, the lattice parameters (whose values are found in [4]) will be defined so that the volume of the exact W-S cell is equal to the volume of the approximate cell. Within a W-S

cell, we approximate the single particle potential $V$ by the potential $U$ of Oyamatsu and Yamada [2]. A zeroth order approximation $U_0$ of the potential is obtained by differentiation of the potential part of an energy density functional $v\{n_{\rm n}, n_{\rm p}\}$ so that

$$
U_{0}=\frac{\partial v}{\partial n_{\mathrm{n}}}. \tag{4.1}
$$

Specifically we shall use the parameter set of model I of this paper. Then, the effect of the finite range of the nucleon-nucleon interaction is taken into account by using the folding of the potential $U_0$ with a gaussian smearing function of width $\kappa$. This potential is supplemented with a spin-orbit coupling term, which is parametrized as a functional of the density gradients. The gaussian width and the parameters of the spin- orbit potential are adjusted so as to reproduce the correct sequence of single particle energy levels of $^{208}$Pb. The potential $U$ thus obtained varies only near the nuclear surface. Therefore, close to the W-S cell boundary $U$ is constant. This enables us to express the periodic potential $V$ acting on a neutron moving in an infinite lattice of nuclei as

$$
V\{\mathbf{r}\}=\sum_{\mathbf{T}} U\{\mathbf{r}-\mathbf{T}\}, \tag{4.2}
$$

where the sum goes over all nuclei occupying the lattice sites, i.e. $\mathbf{T}=\ell^{a} \mathbf{e}_{a}$ , where $\ell^{a}$ are integers. The potential $V\{\mathbf{r}\}$ thus possesses all the symmetries of the crystal lattice. We neglect small changes in $U$ due to passing from a single W-S cell to an infinite lattice. The energy origin is taken as the value of the potential $V$ outside nuclei. Following Oyamatsu and Yamada [2] we do not include momentum dependent terms in the single particle potential. Consequently the microscopic effective neutron mass in this model is just equal to the bare neutron mass $m^{\oplus}=m$ . We have ignored the spin-orbit coupling since it is found to be about one order of magnitude smaller than the central potential [2].

The single-particle Schrödinger equation is solved here by the Rayleigh-Ritz varia- tional approach whereby the expectation value of the Hamiltonian is minimized subject to a normalization condition. The single particle wave function is expanded into plane waves defined by

$$
\varphi_{\mathbf{k}}\{\mathbf{r}\}=\frac{1}{\sqrt{\mathcal{V}_{\text {cell }}}} \sum_{\mathbf{K}} \tilde{\varphi}_{\mathbf{k}}\{\mathbf{K}\} \mathrm{e}^{\mathrm{i}(\mathbf{k}+\mathbf{K}) \cdot \mathbf{r}}, \tag{4.3}
$$

with the normalization

$$
\sum_{\mathbf{K}}\left|\tilde{\varphi}_{\mathbf{k}}(\mathbf{K})\right|^{2}=1. \tag{4.4}
$$


This expansion into plane waves is actually exact, it merely makes more apparent the periodicity. The approximation lies in the fact that the summation needs to be truncated for practical calculations at some cut off energy $\mathcal{E}_\text{cutoff}$ (which thus makes this method adequate only for slowly varying potentials as in the present case), i.e. so as to include all reciprocal lattice vectors satisfying

$$
\frac{\hbar^{2}(\mathbf{k}+\mathbf{K})^{2}}{2 m}<\mathcal{E}_{\text {cutoff }}.\tag{4.5}
$$

The group velocity is found according to the Hellmann-Feynman theorem [17] to be equal to

$$
\mathbf{v}=\frac{\hbar \mathbf{k}}{m}+\sum_{\mathbf{K}} \frac{\hbar \mathbf{K}}{m}\left|\tilde{\varphi}_{\mathbf{k}}(\mathbf{K})\right|^{2}.\tag{4.6}
$$

This last equation shows that deviations from the homogeneous case arise from the spreading of the Bloch wave packet (4.3).

For each total neutron density $n_{\text{n}}$, the Fermi energy $\mu$ is determined as an integral over the first B-Z by

$$
n_{\mathrm{n}}=\frac{2}{(2 \pi)^{3}} \sum_{\alpha} \int_{\mathrm{BZ}} \mathrm{d}^{3} k \vartheta\left\{\mu-\mathcal{E}_{\alpha}\right\},\tag{4.7}
$$

where we have introduced the Heaviside unit step distribution defined by $\vartheta\{x\}=1$ if $x>0$ and zero otherwise (the factor of 2 is to account for the spin degeneracy).
The conduction neutron density is defined by the occupied single particle states whose energy is positive, i.e. $\mathcal{E}_{\alpha}>0$, namely

$$
n=\frac{2}{(2 \pi)^{3}} \sum_{\alpha} \int_{\mathrm{BZ}} \mathrm{d}^{3} k \vartheta\left\{\mu-\mathcal{E}_{\alpha}\right\} \vartheta\left\{\mathcal{E}_{\alpha}\right\}.\tag{4.8}
$$

It will be instructive to compare the Fermi surface area with that of a non interacting neutron gas of density $n_{\text{n}}$, which is given by

$$
S_{\text {gas }}=4 \pi\left(3 \pi^{2} n_{\mathrm{n}}\right)^{2 / 3}.\tag{4.9}
$$

### 4.2 “Lasagna” phase

In this model, the slab shaped nuclei or "lasagna" are parallel to each other and equally spaced by a distance $a$ . Hence the single particle potential $V$ is periodic along one

direction only, say the $z$ axis, and takes a constant value in the other two dimensions. The neutron band structure with a square well potential (whose analytic solution was found a long time ago by Kronig and Penney [18, 19]) was the only case discussed by Oyamatsu and Yamada [2].

The single particle wavefunction can be factored in the form

$$
\varphi_{\mathbf{k}}\{\mathbf{r}\}=\phi_{k_{z}}\{z\} \mathrm{e}^{\mathrm{i}\left(k_{x} x+k_{y} y\right)},\tag{4.10}
$$

in which the reduced wave funtion $\phi_{k_{z}}$ is the solution of a one dimensional equation of the form

$$
\frac{-\hbar^{2}}{2 m} \frac{d^{2} \phi_{k_{z}}}{d z^{2}}+V\{z\} \phi_{k_{z}}\{z\}=\varepsilon\left\{k_{z}\right\} \phi_{k_{z}}\{z\},\tag{4.11}
$$

satisfying the boundary conditions

$$
\phi_{k_{z}}\{z+a\}=e^{\mathrm{i} k_{z} a} \phi_{k_{z}}\{z\}.\tag{4.12}
$$

The first B-Z is defined by the set of Bloch wave vectors such that $-\pi / a \leq k_{z} \leq$ $\pi / a$. The B-Z in this peculiar case has an infinite extent as a result of the continuous translational invariance along planes parallel to the "lasagna". The single particle energy is thus given by an expression of the form

$$
\mathcal{E}_{\alpha}\{\mathbf{k}\}=\frac{\hbar^{2}\left(k_{x}^{2}+k_{y}^{2}\right)}{2 m}+\varepsilon_{\alpha}\left\{k_{z}\right\},\tag{4.13}
$$

where $\alpha$ is a band index. It follows that the neutron group velocity components parallel to the slabs coincide with the group velocity of a non interacting neutron gas while only the component perpendicular to the slabs is affected. It can be shown from group theoretical arguments, that this component of the group velocity must vanish at the Brillouin zone edge [20], i.e. at $k_{z}= \pm \pi / a$ . More generally whenever the Bloch wave vector lies on a symmetry plane, the group velocity component normal to the plane vanishes . It can also be shown that the energy bands do not cross [20](nevertheless bands may touch "accidentally" for some specific choice of potential, for instance a constant one).

The total neutron density is given by

$$
n_{\mathrm{n}}=\frac{m}{\pi^{2} \hbar^{2}} \sum_{\alpha} \int_{0}^{\pi / a} \mathrm{~d} k_{z}\left(\mu-\varepsilon_{\alpha}\right) \vartheta\left\{\mu-\varepsilon_{\alpha}\right\}.\tag{4.14}
$$

The mobility along the "lasagna" planes coincides with that of the uniform neutron gas with the same total neutron density:

$$
\mathcal{K}^{\parallel}=\mathcal{K}^{x x}=\mathcal{K}^{y y}=\frac{n_{\mathrm{n}}}{m}.\tag{4.15}
$$

The mobility in directions perpendicular to the "lasagna" may however differ from that of the non interacting neutron gas:

$$
\mathcal{K}^{\perp}=\mathcal{K}^{z z}=\frac{1}{4 \pi^{3} \hbar} \sum_{\alpha} \int \frac{\left(v^{z}\right)^{2}}{v} \mathrm{d} S_{\mathrm{F}}^{(\alpha)}=\frac{m}{\pi^{2} \hbar^{4}} \sum_{\alpha} \int_{0}^{\pi / a}\left(\frac{d \varepsilon_{\alpha}}{d k_{z}}\right)^{2} \vartheta\left\{\mu-\varepsilon_{\alpha}\right\} \mathrm{d} k_{z}.
\tag{4.16}
$$

Since the "lasagna" configuration is strongly anisotropic, it is more appropriate to define a transverse effective macro mass by

$$
m_{\star}^{\perp} \equiv \frac{n}{\mathcal{K}^{\perp}}.
\tag{4.17}
$$

The conduction neutron density is expressible as

$$
n=n_{\mathrm{n}}+\frac{4}{(2 \pi)^{3}} \sum_{\alpha} \int_{0}^{\pi / a} \pi \frac{2 m \varepsilon_{\alpha}}{\hbar^{2}} \vartheta\left\{\mu-\varepsilon_{\alpha}\right\} \vartheta\left\{-\varepsilon_{\alpha}\right\} \mathrm{d} k_{z}.
\tag{4.18}
$$

## 4.3 "Spaghetti" phase

In the spaghetti model, the crystal is composed of cylinder shaped nuclei arranged on a two dimensional lattice (the nuclear "spaghetti" are assumed to be parallel to each other along say the z axis). Since the single particle potential around one isolated nucleus only depends on the distance to the rod like nucleus, the corresponding contribution to the crystal potential does not depend on $z$ hence the wave function can be factored as

$$
\varphi_{\mathbf{k}}\{\mathbf{r}\}=\phi_{k_{x}, k_{y}}\{x, y\} \mathrm{e}^{\mathrm{i} k_{z} z}.
\tag{4.19}
$$

The two dimensional wave function obeys a Schrödinger equation of the form

$$
-\frac{\hbar^{2}}{2 m}\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}\right) \phi_{k_{x}, k_{y}}\{x, y\}+V\{x, y\} \phi_{k_{x}, k_{y}}\{x, y\}=\varepsilon\left\{k_{x}, k_{y}\right\} \phi_{k_{x}, k_{y}}\{x, y\}.
\tag{4.20}
$$

The energy is thus decomposible as

$$
\mathcal{E}_{\alpha}\{\mathbf{k}\}=\varepsilon_{\alpha}\left\{k_{x}, k_{y}\right\}+\frac{\hbar^{2} k_{z}^{2}}{2 m}.
\tag{4.21}
$$

The total neutron density is given by

$$
n_{\mathrm{n}}=\frac{4}{(2 \pi)^{3} \hbar} \sum_{\alpha} \int_{\mathrm{BZ}} \sqrt{2 m\left(\mu-\varepsilon_{\alpha}\right)} \vartheta\left\{\mu-\varepsilon_{\alpha}\right\} \mathrm{d} k_{x} \mathrm{~d} k_{y},
\tag{4.22}
$$

in which the factor of two arises from the restriction that $k_z > 0$ and where the integration is carried out over the 2D first B-Z illustrated on figure 4.

It is readily verified that the mobility tensor component along the cylindrical nuclei is merely equal to the mobility component of the non interacting neutron gas:

$$
\mathcal{K}^{\|}=\mathcal{K}^{z z}=\frac{n_{\mathrm{n}}}{m}.
\tag{4.23}
$$

The other components perpendicular to the "spaghetti" depend on the neutron-crystal interaction. It is convenient to defined a mean transverse mobility by

$$
\mathcal{K}^{\perp}=\sqrt{\frac{m}{2}} \frac{2}{(2 \pi)^{3} \hbar^{3}} \sum_{\alpha} \int_{\mathrm{BZ}} \frac{\mathrm{d} k_{x} \mathrm{~d} k_{y}}{\sqrt{\mu-\varepsilon_{\alpha}}}\left(\left(\frac{\partial \varepsilon_{\alpha}}{\partial k_{x}}\right)^{2}+\left(\frac{\partial \varepsilon_{\alpha}}{\partial k_{y}}\right)^{2}\right) \vartheta\left\{\mu-\varepsilon_{\alpha}\right\},
\tag{4.24}
$$

since it involves the integral of a completely symmetric function that can thus be factored into one irreducible domain of the first B-Z [21].

The Fermi surface area, the mobility tensor and the density involve integrations over the two dimensional first B-Z of functions weighted by a Fermi distribution. We have followed an idea due to Gilat and Raubenheimer for three dimensional crystals [22], and translated it into the two dimensional case. First of all the zone is decomposed into small identical cells within which the single particle energy is linearly extrapolated from the value of the energy and its gradient at the center of the cell. The integration is then performed analytically inside the cell. The integral is approximated by summing the contribution from each cell (properly weighted whenever the cells overfill the zone). Unlike the case of band crossing, extrapolation fails for band "kissing" where the energy gradient varies rapidly in the cell (see the schematic pictures on Figure 3). This problem becomes more and more acute as the number of bands to be included in the integration is increased. However those induced systematic errors will tend to vanish as the number of microcells is increased. Whereas the integrand could be integrated analytically inside each microcell, we found that it is better to take it as constant. The reason again lies in the band "kissing" problem. The integrand typically depends on the momentum via the single particle energy which is extrapolated. Near a band kissing region, the extrapolation errors in the integrand are integrated which lead to unstable results.

We have considered two lattice types: square and hexagonal crystals (whose recip- rocal lattices are also square and hexagonal respectively). The point group $\mathcal{P}$ (the set of point symmetries which send the lattice into itself) of the hexagonal lattice is $C_{6 v}$ (Schönflies notation [23]) whose order is equal to $|\mathcal{P}|=12$, thereby reducing


![](./images/867773705680323305_3.jpg)

Figure 3: Sketch of energy against wave number for crossing and “kissing” scenarios.

integrations of completely symmetric functions over the entire two dimensional first B-Z to $1/12^{\text{th}}$ of the zone. We mention that for this structure the lattice spacing $a$ (shortest distance between any two lattice points) is not equal to the value given by Oyamatsu $a_{\text{Oy}}$ but is given by

$$
a = \sqrt{\frac{2}{\sqrt{3}}} a_{\text{Oy}} \. \tag{4.25}
$$

Likewise, the first B-Z of a square lattice whose point group is $C_{4v}$ (lattice spacing $a = a_{\text{Oy}}$ ) can be partitionned into $8$ irreducible domains. These considerations are illustrated in Figure 4 with the conventional labelling (first B-Z in red, one irreducible domain in green). The most adequate cell for integrations is thus a rectangle since the irreducible B-Zs are rectangular triangles. The partition of this domain into microcells is thereby straightforward.

These two groups, $C_{6v}$ and $C_{4v}$, contains two dimensional irreducible representations [23] which means that unlike the 1D case, energy bands may cross each other [20]. The neutron band structure along high symmetry lines is shown on Figures 5 and 6 for energies in the vicinity of the Fermi energy and for the lattice spacing $a_{\text{Oy}} = 27.17 \, \text{fm}$.

The conduction neutron density is equal to

$$
n = n_{\text{n}} - \frac{4}{(2\pi)^3 \hbar} \sum_{\alpha} \int_{\text{BZ}} \sqrt{-2m\varepsilon_{\alpha}} \vartheta\{\mu - \varepsilon_{\alpha}\} \vartheta\{-\varepsilon_{\alpha}\} \mathrm{d}k_x \mathrm{d}k_y \. \tag{4.26}
$$

The transverse effective mass is defined by

$$
m_{\star}^{\perp} \equiv \frac{n}{\mathcal{K}^{\perp}} \. \tag{4.27}
$$

![](./images/867773705680323305_4.jpg)

Figure 4: First Brillouin zones and irreducible domains for square and hexagonal variants of spaghetti (rod) lattice.

![](./images/867773705680323305_5.jpg)

Figure 5: Neutron band structure around the Fermi energy $\mu$ , along directions shown on figure 4 for square variant of spaghetti (rod) lattice ($a_{\text{Oy}} = 27.17$ fm).

![](./images/867773705680323305_6.jpg)

Figure 6: Neutron band structure around the Fermi energy $\mu$ , along directions shown on figure 4 for hexagonal variant of spaghetti (rod) lattice with $a_{\text{Oy}}=27.17\,\text{fm}$ .

![](./images/867773705680323305_7.jpg)

Figure 7: Convergence of computed effective mass $m_{\star}^{\perp}/m$ as a function of cell number for an hexagonal lattice with $a_{\text{Oy}}=27.17\,\text{fm}$ .

![](./images/867773705680323305_8.jpg)

Figure 8: Effective mass of conduction neutrons $m_{\star}^\perp/m$ as a function of lattice spacing ($a_{\text{Oy}}$) below and above phase transition from lasagna (slab) regime to spaghetti (rod) regime.

The convergence of the integration scheme based on a decomposition into rectangular cells is illustrated on figure 7 for the hexagonal lattice with the lattice spacing $a_{\text{Oy}}=27.17\,\text{fm}$ . The convergence is much faster for the density than for the other quantities due to the absence of the singular square root integrand.

## 5 Discussion

The results concerning the macroscopic effective neutron mass are illustrated on figure 8 and numerical values can be found in the appendix. The macroscopic effective neutron mass appears to be increased compared to the ordinary neutron mass. The figure also shows that this renormalisation of the neutron mass is mostly significant at low densities and becomes negligible at higher densities where nuclei nearly merge into a uniform mixture. The deviations of the effective neutron mass from the bare one can be understood in terms of modifications of the Fermi surface from a sphere. In particular, as a result of the opening of band gaps the Fermi surface is not smooth but contains many holes as schematically illustrated on figure 9. Since the enclosed Fermi volume only depends on the density, this means that the Fermi surface area for a given density is reduced as compared to the corresponding sphere as shown on figure 10 (see the appendix for the numerical values). In the case for which the Fermi volume is equal to the volume of the first Brillouin zone, the Fermi sphere can be distorted and torn such that the resulting surface area simply vanishes while the volume remains finite. Such a situation occurs in ordinary electric insulators.

In the present work we have neglected the spin-orbit coupling which is a small per-

![](./images/867773705680323305_9.jpg)

Figure 9: Example of energy contours in extended Brillouin zone for square lattice. For sufficiently small Fermi energies the contours are approximately circular as in the free particle case, while at higher energies, the contours consist of disconnected pieces.

![](./images/867773705680323305_10.jpg)

Figure 10: Fermi surface area for neutrons $S_{\mathrm{F}}/S_{\mathrm{gas}}$ as a function of lattice spacing ($a_{\mathrm{Oy}}$) below and above phase transition from lasagna (slab) regime to spaghetti (rod) regime.

turbation in the density region we considered. Taking into account such term would raise some degeneracies. The most dramatic change concerns some regions in momen- tum space around which unperturbed bands are crossing. The breaking of the spin symmetry will entail that such configuration may be turned into band "kissing" (see figure 3) which means that the group velocity will be strongly reduced around those momenta. This means that the resulting mobility would be lower than the one we have found. Besides, since the conduction neutron density is rather unsensitive to such change, it would not be much affected and therefore the effective neutron mass would be slightly larger than the one calculated here.

## 6 Conclusion
The scattering of dripped neutrons by the nuclei in the inner crust leads on a macro- scopic scale to a modification of the neutron mass $m_{\star}$ , which can be expressed via a well defined mobility scalar $\mathcal{K}$ by $m_{\star}=n / \mathcal{K}$ in which $n$ is the (arbitrary) density of such unbound neutrons, and $\mathcal{K}$ is found to be expressible as an integral of the group velocity $v^{i}$ over the corresponding Fermi surface. This effective macro mass should not be confused with the effective micro mass, relevant for subnuclear scales, which is usually found to be smaller than the ordinary neutron mass.

Bragg scattering of dripped neutrons is taken into account here by applying Bloch type boundary conditions, which are well known in solid state physics but have been barely used in this nuclear context. We have computed numerical values of this mobility scalar in the bottom layers of the inner crust near the crust-core interface, for simple models in the "pasta" layers: equally spaced slab shaped nuclei ("lasagna") and rod like nuclei on either a square or an hexagonal 2D lattice ("spaghetti"). The (anisotropic) entrainment effect is small at such densities since the system is nearly homogeneous. It appears that the mobility scalar tends to be systematically reduced compared to the homogeneous expression and the farther from homogeneity, the smaller is the mobility scalar. The resulting effective mass $m_{\star}$ is found to be larger than the bare neutron mass. This results can be interpreted as a macroscopic manifestation of the modifica- tions in the shape of the Fermi surface. Notably as one goes from the homogeneous outer core to the crust, the spherical neutron Fermi surface gets distorted and even torn and pierced.

The main reason is that the neutron Bragg scattering by crustal nuclei leads to the opening of energy band gaps. A specific feature of those exotic phases is that the mobility scalar is bounded, $\mathcal{K} \geq 2 n_{\mathrm{n}} / 3 m$ for the "lasagna" phase and $\mathcal{K} \geq n_{\mathrm{n}} / 3 m$ for the "spaghetti" phase due to the fact that the neutrons are still free to move in one or two dimensions, respectively. There is no such bound for three dimensional crystals, for which smaller mobility scalars (larger effective masses) may be expected.

From these considerations, we can infer that the mobility scalar $\mathcal{K}$ will increase with the density, starting from zero in the outer crust below the neutron drip threshold where all neutrons are confined, since $v^{i}=0$ for all states, to its largest possible value

in the homogeneous neutron star mantle. At low densities near neutron drip, where the conduction neutron density is negligible compared to the total neutron density, $n \ll n_{\rm n}$ , the crystal potential $V$ is quite large but the fraction of the cell occupied by the nuclei is small so that dripped neutrons propagate essentially freely. Consequently we may expect to get $\mathcal{K} \simeq n/m$ and $m_\star \simeq m$ (on the understanding that, as discussed in Subsection 3.6, a conduction state is defined so as to have an associated group velocity that differs significantly from zero). On the other hand, at very high densities where nuclei nearly merge, the potential is much weaker and smoothly varying and we shall have $n \simeq n_{\rm n}$ , so we expect to find $m_\star \simeq m$ .

In other words the mean effective mass $m_\star$ is expected to be close to the ordinary mass $m$ at the top (above neutron drip density where neutrons start to leak out of nuclei) and bottom (where nuclei merge into a uniform mixture of neutrons, protons and electrons at density about 1/3 or 2/3 the nuclear saturation density $n_{\rm sat} \simeq 0.16 \, {\rm fm}^{-3}$ [24]) of the inner crust, but may reach a much larger value (with astrophysically interesting consequences) in the intermediate layers. This indicates that the unbound neutron band effects (that are effectively neglected in the commonly used W-S approximation) could have important consequences as concerns the equilibrium neutron star crust structure and composition.

The exploratory character of the present work, justifies the simplicity of the single particle model we used. In a more realistic, Hartree-Fock calculation, the single particle potential and effective micro mass should have to be determined self-consistently. The potential may contain momentum dependent terms, as with effective nucleon-nucleon interactions of the Skyrme type, which leads to space varying effective neutron masses $m^\oplus \{\mathbf{r}\}$ which are typically smaller than the bare neutron mass. However the general arguments we developed, relying on the shape of the Fermi surface, suggest that the qualitative results of our calculations, namely the enhancement of the macroscopic effective mass $m_\star$ will remain valid in more elaborate single particle schemes. Finally let us mention that as we have shown in a recent paper [9], the neutron pairing is not expected to qualitatively alter our present conclusions.

### Acknowledgements
One of the authors (PH) was partly supported by the KBN grant no. 1-P03D-008-27 and by the LEA Astro-PF PAN/CNRS program. We wish to thank the referee for questions that have helped us to improve the clarity of our presentation.


## APPENDIX

### A Numerical results

#### A.1 Slab shaped nuclei

<table>
  <thead>
    <tr>
      <th>$n_{\rm n}\,(\rm fm^{-3})$</th>
      <th>$\mu (\rm MeV)$</th>
      <th>$a_{\rm Oy}(\rm fm)$</th>
      <th>$n/n_{\rm n}$</th>
      <th>$\mathcal{K}^\parallel/\mathcal{K}^\perp$</th>
      <th>$m_\star^\perp/m$</th>
      <th>$S_{\rm F}/S_{\rm gas}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0735</td>
      <td>31.70</td>
      <td>23.71</td>
      <td>0.9634</td>
      <td>1.0698</td>
      <td>1.0307</td>
      <td>0.9878</td>
    </tr>
    <tr>
      <td>0.0749</td>
      <td>32.10</td>
      <td>23.07</td>
      <td>0.9646</td>
      <td>1.0664</td>
      <td>1.0286</td>
      <td>0.9885</td>
    </tr>
    <tr>
      <td>0.0773</td>
      <td>32.79</td>
      <td>22.23</td>
      <td>0.9666</td>
      <td>1.0605</td>
      <td>1.0251</td>
      <td>0.9896</td>
    </tr>
    <tr>
      <td>0.0792</td>
      <td>33.36</td>
      <td>21.84</td>
      <td>0.9687</td>
      <td>1.0526</td>
      <td>1.0196</td>
      <td>0.9910</td>
    </tr>
  </tbody>
</table>

#### A.2 Rod like nuclei

##### A.2.1 hexagonal lattice

<table>
  <thead>
    <tr>
      <th>$n_{\rm n}\,(\rm fm^{-3})$</th>
      <th>$\mu (\rm MeV)$</th>
      <th>$a_{\rm Oy}(\rm fm)$</th>
      <th>$n/n_{\rm n}$</th>
      <th>$\mathcal{K}^\parallel/\mathcal{K}^\perp$</th>
      <th>$m_\star^\perp/m$</th>
      <th>$\mathcal{S}_{\rm F}/\mathcal{S}_{\rm gas}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0581</td>
      <td>27.2461</td>
      <td>27.17</td>
      <td>0.9553</td>
      <td>1.4102</td>
      <td>1.3471</td>
      <td>0.8898</td>
    </tr>
    <tr>
      <td>0.0630</td>
      <td>28.7422</td>
      <td>25.77</td>
      <td>0.9578</td>
      <td>1.2972</td>
      <td>1.2425</td>
      <td>0.9145</td>
    </tr>
    <tr>
      <td>0.0678</td>
      <td>30.1836</td>
      <td>24.62</td>
      <td>0.9606</td>
      <td>1.2225</td>
      <td>1.1744</td>
      <td>0.9322</td>
    </tr>
    <tr>
      <td>0.0716</td>
      <td>31.2812</td>
      <td>23.97</td>
      <td>0.9632</td>
      <td>1.1668</td>
      <td>1.1239</td>
      <td>0.9471</td>
    </tr>
  </tbody>
</table>

##### A.2.2 square lattice

<table>
  <thead>
    <tr>
      <th>$n_{\rm n}\,(\rm fm^{-3})$</th>
      <th>$\mu (\rm MeV)$</th>
      <th>$a_{\rm Oy}(\rm fm)$</th>
      <th>$n/n_{\rm n}$</th>
      <th>$\mathcal{K}^\parallel/\mathcal{K}^\perp$</th>
      <th>$m_\star^\perp/m$</th>
      <th>$\mathcal{S}_{\rm F}/\mathcal{S}_{\rm gas}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0581</td>
      <td>27.2461</td>
      <td>27.17</td>
      <td>0.9553</td>
      <td>1.4673</td>
      <td>1.4016</td>
      <td>0.8778</td>
    </tr>
    <tr>
      <td>0.0630</td>
      <td>28.7422</td>
      <td>25.77</td>
      <td>0.9578</td>
      <td>1.3231</td>
      <td>1.2673</td>
      <td>0.9085</td>
    </tr>
    <tr>
      <td>0.0678</td>
      <td>30.1797</td>
      <td>24.62</td>
      <td>0.9606</td>
      <td>1.2124</td>
      <td>1.1647</td>
      <td>0.9347</td>
    </tr>
    <tr>
      <td>0.0716</td>
      <td>31.2812</td>
      <td>23.97</td>
      <td>0.9632</td>
      <td>1.1473</td>
      <td>1.1051</td>
      <td>0.9524</td>
    </tr>
  </tbody>
</table>

## References

[1] B. Carter, N. Chamel, P. Haensel, "Entrainment coefficient and effective mass for conduction neutrons in neutron star crust: macroscopic treatment", preprint, [astro-ph/0408083]

[2] K. Oyamatsu, Y. Yamada "Shell energies of non spherical nuclei in the inner crust of a neutron star", *Nucl. Phys.* **A578** (1994) 184-203.

[3] J.W. Negele, D. Vautherin, "Neutron star matter at subnuclear densities", Nucl. Phys. **A207** (1973) 298-320.

[4] K. Oyamatsu, "Nuclear shapes in the inner crust of a neutron stars", Nucl. Phys. **A561** (1993) 431-452.

[5] B. Friedman, V. R. Pandharipande, "Hot and cold, nuclear and neutron matter", Nucl. Phys. **A361** (1981) 502-520.

[6] N. Chamel, "Band structure effects for dripped neutrons in neutron star crust", Nucl. Phys. **A747** (2005) 109-128. [nucl-th/0405003]

[7] A. Bulgac, P. Magierski, P.H. Heenen, "Neutron stars and the fermionic Casimir effect", Int. J. Mod. Phys.**A17** (2002) 1059-1054. [nucl-th/0112002]

[8] P. Magierski & P. H. Heenen, "Structure of the inner crust of neutron stars: crystal lattice or disordered phase?", Phys. Rev. C **V65** (2002) 045804, 1-13. [nucl-th/0112018]

[9] B. Carter, N. Chamel, P. Haensel, "Effect of BCS pairing on entrainment in neutron superfluid current in neutron star crust", preprint [astro-ph/0406228]

[10] F. Douchin, P. Haensel, "Inner edge of neutron-star crust with SLy ef- fective nucleon-nucleon interactions", Phys. Lett.**B 485** (2000) 107-114. [astro-ph/0006135]

[11] Ashcroft & Mermin Solid State Physics (Holt-Saunders International Editions, 1981)

[12] E. P. Wigner & F. Seitz "On the constitution of metallic sodium", Phys. Rev. **43** (1933) 804-810 ; Phys. Rev. **46**, (1934) 509-524.

[13] R.D. Cowan, The theory of atomic structure and spectra (Univ. California Press, 1981) 107.

[14] M.A. Ruderman, "Crystallization and torsional oscillations of superdense stars", Nature **218** (1968) 1128-1129.

[15] F. Douchin, P. Haensel, J. Meyer, "Nuclear surface and curvature properties for SLy Skyrme forces and nuclei in the inner neutron-star crust", Nucl. Phys. **A665** (2000) 419.

[16] C. J. Pethick, D. G. Ravenhall, "Matter at large neutron excess and the physics of neutron star crusts", Annu. Rev. Part. Sci. **45** (1995) 429-484.

[17] R. Feynman, "Forces in molecules", Phys. Rev. **56** (1939) 340-343

[18] R. de L. Kronig & W. G. Penney, "Quantum Mechanics of Electrons in Crystal Lattices", *Proc. Roy. Soc. (London)* **A130** (1931)

[19] N. O. Folland, "Energy bands and forbidden gaps in the Kronig-Penney model", *Phys. Rev.* **B28** (1983) 6068-6070.

[20] S.L. Altmann, *Band theory of solids: an introduction from the point of view of symmetry*, (Clarendon Press-Oxford, 1991).

[21] D. F. Johnston, "Group theory in solid state physics", *Rep. Prog. Phys.* **23** (1960), 66-153.

[22] G. Gilat & L.J. Raubenheimer "Acurate Numerical Method for Calculating Frequency distribution Functions in Solids", *Phys. Rev* **144** (1966) 390-395.

[23] M. Hamermesh, *Group theory and its application to physical problems* (Dover, New York, 1989)

[24] P. Haensel, "Neutron star crusts", *Physics of Neutron Star Interiors*, ed. D. Blaschke, N.K. Glendenning, A. Sedrakian, Lecture Notes in Physics **578** (Heidelberg: Springer, 2001), p. 127