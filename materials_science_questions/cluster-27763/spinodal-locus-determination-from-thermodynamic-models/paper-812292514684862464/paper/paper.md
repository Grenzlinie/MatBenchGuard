Substitution of (17) and (18) into (16) yields
$\zeta = \zeta_0 + kT \times$

$$
\log\left[ \frac{\left(n_{1a}-\frac{N_a}{h_{1a}}\right)^a\left(n_{1b}-\frac{N_b}{h_{1b}}\right)^b\left(n_{1c}-\frac{N_c}{h_{1c}}\right)^c \dots}{\left(n_{2p}+\frac{N_p}{h_{2p}}\right)^p\left(n_{2q}+\frac{N_q}{h_{2q}}\right)^q\left(n_{2r}+\frac{N_r}{h_{2r}}\right)^r \dots} n_0^{p+q+r+\dots -a-b-c-\dots} \right]
$$

or
$$
\exp\left( \frac{\zeta - \zeta_0}{kT} \right) = \frac{\left(n_{1a}-\frac{N}{ah_{1a}}\right)^a\left(n_{1b}+\frac{N}{bh_{1b}}\right)^b\left(n_{1c}-\frac{N}{ch_{1c}}\right)^c \dots}{\left(n_{2p}+\frac{N}{ph_{2p}}\right)^p\left(n_{2q}+\frac{N}{qh_{2q}}\right)^q\left(n_{2r}+\frac{N}{rh_{2r}}\right)^r \dots} n_0^{p+q+r+\dots -a-b-c-\dots}
$$

This leads to a polynomial equation in $N$:
$$
\begin{aligned}
\exp\left( \frac{\zeta - \zeta_0}{kT} \right)&\left(n_{2p}+\frac{N}{ph_{2p}}\right)^p\left(n_{2q}+\frac{N}{qh_{2q}}\right)^q\left(n_{2r}+\frac{N}{rh_{2r}}\right)^r \dots = \\
&n_0^{p+q+r+\dots -a-b-c-\dots}\left(n_{1a}-\frac{N}{ah_{1a}}\right)^a\left(n_{1b}-\frac{N}{bh_{1b}}\right)^b\left(n_{1c}-\frac{N}{ch_{1c}}\right)^c \dots
\end{aligned} \tag{19}
$$

The degree of this equation equals
$$
\max(a + b + c + \dots,\ p + q + r + \dots)
$$

Solution of the equation gives the desired characteristic $N(\zeta)$.

It often happens that the equation yields more than one real solution. This gives rise to several branches $N(\zeta)$, as illustrated by an example in Figure 6. Of course only the branch that intersects the abscissa is physically relevant. This intersection, by the way, happens at $\zeta = \zeta_C$, given by

$$
\zeta_C = \zeta_0 + kT \log\left[ \frac{\left(\frac{n_{1a}}{n_0}\right)^a\left(\frac{n_{1b}}{n_0}\right)^b\left(\frac{n_{1c}}{n_0}\right)^c \dots}{\left(\frac{n_{2p}}{n_0}\right)^p\left(\frac{n_{2q}}{n_0}\right)^q\left(\frac{n_{2r}}{n_0}\right)^r \dots} \right]
$$

The physically meaningful branch has two horizontal asymptotes:
$$
\lim_{\zeta \to -\infty} N = \min(ah_{1a}n_{1a},\ bh_{1b}n_{1b},\ ch_{1c}n_{1c},\ \dots)
$$

$$
\lim_{\zeta \to +\infty} N = -\min(ph_{2p}n_{2p},\ qh_{2q}n_{2q},\ rh_{2r}n_{2r},\ \dots)
$$

This can be seen as follows. For $\zeta \to -\infty$, eq 19 becomes
$$
\left(n_{1a}-\frac{N}{ah_{1a}}\right)^a\left(n_{1b}-\frac{N}{bh_{1b}}\right)^b\left(n_{1c}-\frac{N}{ch_{1c}}\right)^c \dots = 0
$$
a polynomial equation in $N$ with obvious roots
$$
ah_{1a}n_{1a},\ bh_{1b}n_{1b},\ ch_{1c}n_{1c},\ \dots
$$

The smallest of these roots is the physically relevant $N(-\infty)$. Analogously, $\zeta \to +\infty$ yields the polynomial equation
$$
\left(n_{2p}+\frac{N}{ph_{2p}}\right)^p\left(n_{2q}+\frac{N}{qh_{2q}}\right)^q\left(n_{2r}+\frac{N}{rh_{2r}}\right)^r \dots = 0
$$
with roots
$$
-ph_{2p}n_{2p},\ -qh_{2q}n_{2q},\ -rh_{2r}n_{2r},\ \dots
$$
where again the value closest to zero has to be retained.

# Spinodal Curve of Some Supercooled Liquids

Pablo G. Debenedetti,* V. S. Raghavan, and Steven S. Borick

Department of Chemical Engineering, Princeton University, Princeton, New Jersey 08544-5263
(Received: November 15, 1990)

There exist two possible limits to the extent to which a liquid can be supercooled: the Kauzmann temperature and the spinodal curve. The virial theorem imposes severe constraints on the type of interactions that can give rise to loss of mechanical stability upon supercooling and therefore to a supercooled liquid spinodal. Systems composed of particles interacting via pair potentials whose repulsive core has a positive curvature (such as the Lennard-Jones potential) cannot become mechanically unstable upon supercooling. Systems composed of particles interacting via potentials whose repulsive core is softened by a curvature change are capable of losing stability upon supercooling, and of contracting when heated isobarically. This is consistent with the idea that loss of stability upon supercooling can only occur for liquids capable of contracting when heated. Microscopically, this occurs via the formation of open structures which can be collapsed into denser arrangements through the input of thermal and mechanical energy. In the quasichemical approximation, a very simple model of a core-softened fluid, the lattice gas with attractive nearest-neighbor and repulsive next-nearest-neighbor interactions, exhibits density anomalies in one, two, and three dimensions, and a reentrant, continuous spinodal bounding the superheated, supercooled, and subtriple liquid states in three dimensions.

## Introduction

Liquids can be cooled below their freezing temperature without solidifying: they can be supercooled. In an ideally purified liquid devoid of any suspended impurity, small nuclei of solid phase are formed exclusively as a result of spontaneous density fluctuations. When such nuclei reach a critical size they grow, and a solid phase is formed. The formation of critical nuclei (homogeneous nucleation) is a barrier which must be overcome in order for the phase transition to occur. $^{1-4}$ In the absence of dissolved impurities, homogeneous nucleation governs the initial rate at which the

---
*To whom correspondence should be addressed.

(1) Turnbull, D.; Fischer, J. C. *J. Chem. Phys.* 1949, 17, 71.
(2) Turnbull, D. *J. Phys. Chem.* 1962, 66, 609.
(3) Walton, A. G. *Science* 1965, 148, 601.
(4) Turnbull, D. *Contemp. Phys.* 1969, 10, 473.

Spinodal Curve of Some Supercooled Liquids
The Journal of Physical Chemistry, Vol. 95, No. 11, 1991 4541

metastable liquid relaxes toward a stable condition and solidifies. Homogeneous nucleation rates exhibit a very sharp dependence on the extent of supercooling. Consequently, when a liquid is supercooled, it evolves suddenly from a condition of apparent stability to one in which the solid phase grows spontaneously and very rapidly. As long as the sequence of events is kinetically controlled, the point at which the rapid growth of the new phase occurs can be varied by changing the design of the experiment. An example of this is the emulsification of supercooled liquid samples so that the rate of critical nuclei formation in any one droplet (nuclei per unit time) is small even though the intrinsic homogeneous nucleation rate (nuclei per unit time per unit volume) is large.⁵ Such a limit, however, is not a true property of a particular liquid so much as it is a characteristic of the experimental technique. Supercooling limits determined by kinetic considerations, in other words, are not infinitely sharp.

Nucleation is not the only kinetically controlled mechanism that can lead to solidification upon supercooling. If the rate of cooling is high enough for nucleation to be bypassed, the liquid can vitrify. Glass formation occurs when the relaxation time required for the liquid's molecules to rearrange their configurations in response to the imposed temperature change becomes comparable to the experimentally accessible time.⁴,⁶,⁷ Molecules then get trapped in a configuration and form an amorphous solid. The particular frozen-in configuration into which molecules get trapped is dependent on the cooling history to which the sample has been exposed. The cooling rate dependent temperature (or, more precisely, narrow temperature interval) at which the liquid solidifies is the glass transition temperature. Its lowest possible value is the temperature at which the entropy difference between the liquid and crystalline phases disappears (the Kauzmann temperature⁸). The Kauzmann temperature imposes a sharply defined (thermodynamic) lower limit to the possible existence of the liquid state of a given substance, since upon further supercooling the hypothetical liquid would have a lower entropy than the corresponding crystalline phase, a condition often referred to as entropy catastrophe. The Kauzmann temperature is unattainable because the slowing down of molecular motion inevitably gives rise to kinetically controlled glass transitions.

There is another theoretical limit to the extent of possible liquid supercooling, namely, attainment of the spinodal locus, beyond which the liquid becomes mechanically unstable.⁹ For a pure substance, the spinodal is defined by the simultaneous occurrence of the conditions
$$
K_T = \infty \tag{1}
$$
$$
c_p = \infty \tag{2}
$$
where $K_T$ is the isothermal compressibility, and $c_p$, the isobaric heat capacity. The critical point is the only stable condition along a spinodal, which is otherwise a locus of unstable limits of stability. For a stable or metastable pure substance, $c_p$ and $K_T$ are positive and finite except at the critical point. The mechanism of instability for a pure substance is the unbounded growth in density fluctuations¹⁰
$$
K_T = \frac{V}{kT\langle\rho\rangle^2}\langle(\delta\rho)^2\rangle \tag{3}
$$

In practice, a spinodal can be approached but never reached. Kinetically controlled relaxation mechanisms such as homogeneous nucleation will trigger a phase transition before a limit of stability can actually be attained. Nevertheless, it is of practical and theoretical significance to determine the location of the spinodal, since it represents a sharp limit beyond which a particular state of matter cannot exist and within which it can. The question naturally arises, therefore, as to the location of the spinodal for supercooled liquids.

Molecular considerations, however, lead one to investigate critically the very existence of a supercooled liquid spinodal before attempting to predict its location. Consider the usual case of a liquid that contracts upon freezing, for which supercooling can be caused by isothermal compression. A spinodal limit would then imply a condition of infinite compressibility brought about by compression (as with supercooled vapors), but at densities such that liquid behavior is largely dominated by repulsive interactions. Clearly, we must start by exploring the conditions under which such behavior can possibly occur.

In what follows, we investigate the necessary conditions for the existence of a spinodal limit to supercooling. In order to do so, we need to assume that the Kauzmann temperature is lower than the spinodal temperature, whenever the latter exists. This assumption needs to be verified for each specific substance but is required for an investigation of necessary conditions for spinodal collapse.

## Stability and the Virial Theorem

As a starting point for a molecular-based analysis of the existence of a supercooled liquid spinodal, we consider a fluid whose molecules interact via pairwise additive central forces. For such a fluid, we can write
$$
P = \rho[kT + (\Psi/6)] \tag{4}
$$
where $\Psi$, the virial, is given by
$$
\Psi = N\langle\mathbf{r}_{ij}\cdot\mathbf{f}_{ij}\rangle \tag{5}
$$
with $\mathbf{r}_{ij} = \mathbf{r}_i - \mathbf{r}_j$, $\mathbf{f}_{ij}$, the force on molecule $i$ due to $j$, and where angle brackets denote thermodynamic averaging. In eq 4 we have assumed $N^2 \approx N(N - 1)$. It follows from eq 4 that
$$
K_T = \frac{6}{\rho^2\left[\frac{6P}{\rho^2} + \left(\frac{\partial\Psi}{\partial\rho}\right)_{T,N}\right]} \tag{6}
$$

Therefore, for a stable or metastable fluid we must have
$$
\left(\frac{\partial\Psi}{\partial\rho}\right)_{T,N} > -\frac{6P}{\rho^2} \tag{7}
$$

This implies the following: (i) under conditions of temperature and density such that the virial increases upon isothermal compression, loss of stability can only occur under tension ($P < 0$); (ii) when loss of stability occurs under positive pressure, the virial decreases upon isothermal compression.

The former case corresponds to loss of stability in superheated liquids below a threshold temperature ($T/T_c = 27/32$ for a van der Waals fluid) or, equivalently, above a threshold density ($\rho/\rho_c = 3/2$ for a van der Waals fluid). The latter corresponds to loss of stability in supercooled vapors or in superheated liquids above a threshold temperature (or below a threshold density).

Consider for example the stability of a fluid whose molecules interact via a pair potential of the form
$$
\phi = \epsilon(\sigma/r)^n \tag{8}
$$
for which
$$
\Psi = Nn\epsilon\langle(\sigma/r)^n\rangle \tag{9}
$$
$$
\left(\frac{\partial\Psi}{\partial\rho}\right)_{T,N} = n\epsilon\sigma^n\left[\frac{\partial N\langle r^{-n}\rangle}{\partial\rho}\right]_{T,N} > 0 \tag{10}
$$
$$
P = \rho\left[kT + \frac{Nn\epsilon\sigma^n\langle r^{-n}\rangle}{6}\right] > 0 \tag{11}
$$

Since both the pressure and the virial's rate of change with respect

(5) Rasmussen, D. H.; MacKenzie, A. P. *J. Chem. Phys.* 1973, 59, 5003.
(6) Zallen, R. *The Physics of Amorphous Solids*; Wiley: New York, 1983; Chapter 1.
(7) Angell, C. A. 11th IUPAC Conf. Chem. Thermodyn., Plenary Lect.; Como, Italy, August 1990.
(8) Kauzmann, W. *Chem. Rev.* 1948, 43, 219.
(9) Modell, M.; Reid, R. C. *Thermodynamics and its Applications*, 2nd ed.; Prentice Hall: Englewood Cliffs, NJ, 1983; Chapter 9.
(10) Lifshitz, E. M.; Pitaevskii, L. P. *Statistical Physics*, Part 1, 3rd ed.; Vol. 5 of *Course of Theoretical Physics*; Landau, L. L., Lifshitz, E. M.; Pergamon: Oxford, 1980; Chapter 12.

![](./images/812292514684862464_1.jpg)

Figure 1. Density dependence of the attractive (a), repulsive (r), and total virial $(\Psi/N\epsilon)$ for a Lennard-Jones-type fluid below the Boyle temperature.

![](./images/812292514684862464_2.jpg)

Figure 2. Density dependence of the attractive and repulsive (a, top) and total (b, bottom) virial $(\Psi/N\epsilon)$ of the Lennard-Jonesium at its triple point temperature $(kT/\epsilon = 0.68)$ and in the vicinity of the liquid triple point density $(\rho\sigma^{3}=0.86)$. $NVT$ molecular dynamics of 500 atoms.

to isothermal density increase are positive, the stability inequality is never violated. There can be no supercooled liquid spinodal for a soft sphere fluid.

Consider now a fluid whose molecules interact via a Lennard-Jones-type potential
$$
\phi=\epsilon\left[(\sigma / r)^{n}-(\sigma / r)^{m}\right] \quad(n>m) \tag{12}
$$
for which the virial is given by
$$
\Psi=N \epsilon\left[n \sigma^{n}\left\langle r^{-n}\right\rangle-m \sigma^{m}\left\langle r^{-m}\right\rangle\right]=N \epsilon\left[n\left\langle(\sigma / r)^{n}\right\rangle-m\left\langle(\sigma / r)^{m}\right\rangle\right] \tag{13}
$$

For this type of potential, Figure 1 shows the density dependence of the attractive and repulsive contributions to the fluid's virial $(\Psi/N\epsilon)$ at low temperature. Above a certain temperature, the virial-density curve is monotonically increasing and has zero slope at the origin. As shown in the Appendix, this occurs when the second virial coefficient vanishes (i.e., at the Boyle temperature). Returning to Figure 1, it follows from eq 7 that the only density range where the fluid can lose stability under positive pressure is below $\rho^{*}$; above $\rho^{*}$, it can only lose stability under tension. Therefore, it is necessary (but not sufficient) in order for a supercooled liquid spinodal to exist at positive pressure that $\rho^{l}<\rho^{*}$, where $\rho^{l}$ is the liquid density in equilibrium with the solid at the given temperature. This is a stringent requirement. Figure 2 shows the density dependence of the Lennard-Jones fluid's virial at the triple-point temperature, over a range of densities comprising the liquid's triple point $(\rho\sigma^{3}=0.86)$. Clearly, $\rho^{l}>\rho^{*}$, and there can be no supercooled spinodal at this temperature, since the metastable region is accessed by compression and loss of stability can only occur under tension. Above the Boyle temperature, the virial behaves as shown in Figure 3. Under these conditions, there can be no supercooled liquid spinodal because the metastable region is accessed under pressure and the virial increases upon compression.

![](./images/812292514684862464_3.jpg)

Figure 3. High-temperature density dependence of the attractive, repulsive, and total virial $(\Psi/N\epsilon)$ for a Lennard-Jones fluid. $kT/\epsilon = 6.5$. $NVT$ molecular dynamics of 500 atoms.

Any fluid whose molecules interact via a potential whose repulsive core has a positive curvature, therefore, cannot possibly have a supercooled liquid spinodal above the Boyle temperature. Below the Boyle temperature, severe restrictions are imposed by the virial theorem on the possible divergence of a fluid's compressibility upon supercooling.

![](./images/812292514684862464_4.jpg)

Figure 4. A core-softened potential.

### Core Softening
Given the stringent limitations imposed by the virial theorem on the possible existence of a supercooled liquid spinodal, it is logical to inquire as to the type of potential, if any, that is consistent with loss of stability upon supercooling. Consider the potential shown in Figure 4, with inflection points within the repulsive core at $r_1$ and $r_2$. For $r_2 > r > r_1$, the force between two molecules decreases as they approach each other. This behavior will henceforth be referred to as core softening, a description that also applies to the case (not shown) in which a secondary well appears between $r_1$ and $r_2$. Mathematically, core softening means that $\Delta(rf)<0$ when $\Delta r<0$ for $r_2 > r > r_1$ (i.e., the product $rf$ decreases

Spinodal Curve of Some Supercooled Liquids
The Journal of Physical Chemistry, Vol. 95, No. 11, 1991 4543

when the separation decreases). Taking into account the relationship between force and potential, this condition can be expressed as
$$
r \phi^{\prime \prime}+\phi^{\prime}<0 \quad r_{2}>r>r_{1} \tag{14}
$$
and also
$$
\phi^{\prime \prime}>0 \quad r<r_{1} \text { and } r>r_{2} \tag{15}
$$
where the second condition imposes that the decrease in the virial upon approach occur within the repulsive core (therefore, we require that $\phi^{\prime \prime}>0$ for some $r>r_{2}$ and all $r<r_{1}$ ). Core softening has been extensively studied by Stell and co-workers. $^{11-16}$ They investigated phase transitions caused by an abrupt diminution of the core diameter, which they referred to both as core softening and as core collapse. Although the emphasis of that work was on phase behavior, Stell and Hemmer $^{12}$ reported density anomalies in one dimension for a linearly softened potential with long-range attractions.

The contribution to the total virial due to a pair of molecules interacting via a core-softened potential does not increase monotonically as the separation decreases below $r^{\prime}$ (potential minimum). Therefore, upon compression, the total virial does not increase monotonically with density, and the stability inequality can now be violated at high density.

Consider now the thermal expansion coefficient of a core-softened fluid. Differentiating eq 4, we obtain
$$
\left(\frac{\partial P}{\partial T}\right)_{\rho}=\rho\left[k+\frac{1}{6}\left(\frac{\partial \Psi}{\partial T}\right)_{\rho}\right] \tag{16}
$$

Therefore, for a stable or metastable fluid, the thermal expansion coefficient will be positive so long as
$$
\left(\frac{\partial \Psi}{\partial T}\right)_{\rho}>-6 k \tag{17}
$$
where the restriction to stable fluids comes from equating the signs of $(\partial P / \partial T)_{v}$ and $(\partial T / \partial v)_{P}$, which is necessarily true so long as $(\partial P / \partial v)_{T}$ is negative. If a given number of molecules is heated inside a rigid container, the only new contributions to the virial are those due to interpenetration of repulsive cores by pairs of energetic molecules. For a potential with positive curvature in its repulsive core (no core softening), these new contributions must necessarily lead to an increase in the virial because at the point of closest approach between two molecules during a given collision the pairwise virial is larger than for all greater separations. Consequently, eq 17 is satisfied for fluids which interact via pair potentials whose repulsive cores have only positive curvature, and such fluids cannot exhibit density anomalies.

A necessary condition for a fluid to have a negative thermal expansion coefficient somewhere in its phase diagram is therefore that the isochoric rate of change of the virial with respect to temperature be negative for some condition of temperature and pressure. Core softening can lead to this condition because at the point of closest approach between two molecules during a given collision the pairwise virial is not necessarily larger than for all greater separations. Therefore, a core-softened fluid can have a negative thermal expansion coefficient and can become mechanically unstable at high density.

The effective pair potentials of several liquid metals determined from experimental structure factor data exhibit core softening. Examples include Al, In, Mg; $^{17} \mathrm{Na}, \mathrm{Al}, \mathrm{Mg}, \mathrm{K}, \mathrm{Ca}, \mathrm{Zn}, \mathrm{Ga}, \mathrm{Rb}$, $\mathrm{Sr}, \mathrm{In}, \mathrm{Sn}, \mathrm{Sb}, \mathrm{Cs}, \mathrm{Ba}, \mathrm{Tl}, \mathrm{Pb}, \mathrm{Bi} ;{ }^{18} \mathrm{Al} .{ }^{19}$ Three liquid metals (Ga, Sn, Bi) expand upon freezing. No density anomalies have been reported for liquid metals. However, we are not aware of any volumetric measurement for supercooled liquid metals. Expansion upon freezing certainly suggests the possible existence of density anomalies. A negative thermal expansion coefficient and expansion upon freezing were both obtained by Stillinger and Weber $^{20}$ in their computer simulation study of a model core-softened system: the Gaussian core fluid. In addition, the numerical angle-averaging of several asymmetric site-site water potentials yielded core-softened spherically symmetric potentials. $^{21}$

![](./images/812292514684862464_5.jpg)

Figure 5. Relationship between the continuous stability boundary (cgaf) within which the liquid phase can exist, and the locus of density maxima (aeg). Case in which density anomalies are confined to the metastable region. c is the critical point; b, the triple point; k, an isochore, and hb, bd, and bc, the sublimation, melting, and boiling curves. cga = spinodal; af = Kauzmann locus.

### Thermodynamic Implications
The relationship between density anomalies and loss of stability upon supercooling which we have so far mentioned in connection with core softening is central to the phenomenological treatment introduced by Speedy $^{22,23}$ to describe the stability boundaries of liquid water, and generalized by Debenedetti and D'Antonio $^{24}$ for any fluid exhibiting density maxima Its essential features are illustrated in Figure 5, which shows the continuous stability boundary (cgaf) of a liquid exhibiting density maxima (the locus of which is line aeg), along with the loci of solid-vapor (hb), liquid-vapor (bc; c is the critical point), and solid-liquid (bd) equilibria.

Figure 5 corresponds to a liquid which exhibits density maxima only in the metastable region, such as $\mathrm{SiO}_{2}{ }^{25}$ The picture is unchanged in its essentials in the case where aeg intersects the stable liquid region, except that the slope of line bd may then change from negative to positive at a pressure below which the liquid expands upon freezing, and above which it contracts upon freezing. Intersection with the locus of density maxima causes a change in the slope of the spinodal. At g, the liquid has attained its maximum tensile strength. Within the region bounded by aeg and the spinodal segment ag the liquid's thermal expansion coefficient is negative. Points a and g are therefore the extremes of temperature and pressure within which contraction upon isobaric heating is possible. Line k is a liquid isochore; its slope changes sign along aeg, and it becomes tangent to the spinodal. Line af is a spinodal in both Speedy's and Debenedetti and D'Antonio's treatments. $^{22-24}$ However, because the liquid has a positive thermal expansion coefficient upon approaching this limit, it is more appropriate to view line af as a Kauzmann locus.

(11) Hemmer, P. C.; Stell, G. Phys. Rev. Lett. 1970, 24, 1284.
(12) Stell, G.; Hemmer, P. C. J. Chem. Phys. 1972, 56, 4274.
(13) Kincaid, J. M.; Stell, G.; Hall, C. K. J. Chem. Phys. 1976, 65, 2161.
(14) Kincaid, J. M.; Stell, G.; Goldmark, E. J. Chem. Phys. 1976, 65, 2172.
(15) Kincaid, J. M.; Stell, G. J. Chem. Phys. 1977, 67, 420.
(16) Kincaid, J. M.; Stell, G. Phys. Lett. A 1978, 65, 131.
(17) Yokoyama, I.; Ono, S. J. Phys. F: Met. Phys. 1985, 15, 1215.
(18) Hoshino, K.; Leung, C. H.; McLaughlin, I. L.; Rahman, S. M. M.; Young, W. H. J. Phys. F: Met. Phys. 1985, 17, 787.
(19) March, N. H. Can. J. Phys. 1987, 65, 219.
(20) Stillinger, F. H.; Weber, T. A. J. Chem. Phys. 1978, 68, 3837.
(21) D'Antonio, M. C. Ph.D. Thesis, Princeton University, 1989.
(22) Speedy, R. J. J. Phys. Chem. 1982, 86, 982.
(23) Speedy, R. J. J. Phys. Chem. 1982, 86, 3002.
(24) Debenedetti, P. G.; D'Antonio, M. C. AIChE J. 1988, 34, 347.
(25) Angell, C. A.; Kanno, H. Science 1976, 193, 1121.

![](./images/812292514684862464_6.jpg)

Figure 6. A pair potential with nearest-neighbor attraction and next-nearest-neighbor repulsion.

Experimental evidence in support of spinodal collapse in supercooled liquids includes measurements of the isobaric heat capacity of supercooled water and heavy water²⁶²⁷ and of the isothermal compressibility of supercooled water.²⁸ Both properties showed anomalous increases; for water, the compressibility was fitted with a power law of the form $K_T = At^r$ [$t = (T - T_s)/T_s$] and yielded a spinodal temperature of 228 K at atmospheric pressure. An anomalous increase in the isobaric heat capacity of supercooled tellurium (Te) has recently been reported.²⁹

The slope of the pressure-temperature projection of the homogeneous nucleation temperatures of supercooled water and heavy water exhibits high-pressure discontinuities²⁵³⁰ similar to that occurring at point a in Figure 5. In the case of heavy water, furthermore, the relation between the locus of density maxima and the homogeneous nucleation temperature locus appears to be similar to that shown in Figure 5 between the locus of density maxima and the spinodal.²⁵ Both observations are consistent with the existence of strong pretransitional fluctuations due to the proximity to a spinodal having the same underlying shape. Angell and co-workers³¹ have recently used the general picture described in Figure 5 (continuous stability boundary, relationship between loss of stability and density anomalies) to explain and interpret their measurements of water and aqueous solutions at highly negative pressures.

Figure 5, which we do not rederive here, follows only from thermodynamic consistency arguments and the assumption of an analytic Helmholtz energy along the spinodal. It shows that density anomalies provide a mechanism for a continuous stability boundary spanning the supercooled, superheated, and simultaneously superheated and supercooled, or subtriple²¹ conditions, and hence also for a supercooled liquid spinodal. From a continuum, macroscopic perspective, there appears a fundamental connection between loss of stability upon supercooling and the ability of a liquid to contract when heated isobarically. This agrees with essential aspects of the behavior associated with core softening. This connection, however, needs to be established more rigorously, starting from a microscopic model. We address this question in the next section via a deliberately simple model which we use not to predict the stability boundaries of a specific substance but to demonstrate that the behavior shown in Figure 5 follows also from microscopic considerations.

### Microscopic Model and Implications

We choose to formulate the problem in a lattice. The simplest case of core softening is a lattice fluid with single occupancy of sites (hard core repulsion), nearest-neighbor attraction $(-\epsilon; \epsilon >$ 0), and next-nearest-neighbor repulsion $(\lambda\epsilon, \lambda > 0;$ see Figure 6). Stell and co-workers studied phase transitions due to core softening by repulsive shoulders with and without long-range attractions.¹¹⁻¹⁶ We are interested in density anomalies and stability limits in addition to phase behavior. In magnetic terminology, the present problem is equivalent to solving the Ising model with ferromagnetic nearest-neighbor and antiferromagnetic next-nearest-neighbor interactions in nonzero field. Previous work on aspects of the Ising problem with next-nearest-neighbor interactions includes that of Domb and Potts,³² Fan and Wu,³³ Dalton and Wood,³⁴ Gibberd,³⁵ Stephenson and Betts,³⁶ Landau,³⁷³⁸ Campbell and Schick,³⁹ Nauenberg and Nienhuis,⁴⁰ Meijer and Cunningham,⁴¹ Takase,⁴²⁴³ Selke,⁴⁴ Binder and Landau,⁴⁵ and Binder.⁴⁶

Domb and Potts³² used series expansions to investigate the dependence of the critical temperature, energy, and entropy upon the sign and magnitude of $\lambda$ for a square, two-dimensional lattice. Fan and Wu³³ investigated the square Ising lattice with next-nearest-neighbor interactions in zero field and obtained expressions for the free energy, energy, specific heat, and critical temperature. Dalton and Wood³⁴ used series expansions to investigate the dependence of the critical temperature, critical exponents for the magnetization and susceptibility, critical energy, and critical entropy upon the ratio of next-nearest-to-nearest-neighbor interactions (both ferromagnetic) in two and three dimensions. Gibberd³⁵ investigated the two-dimensional problem on a square lattice and calculated the critical temperature and magnetization critical exponent for ferromagnetic nearest- and next-nearest interactions. Stephenson and Betts³⁶ calculated the value of $\lambda$ for which the phase transition disappears, as well as the $\lambda$-dependence of the critical temperature for a variety of lattices. Landau³⁷³⁸ used Monte Carlo simulations to calculate the critical temperature, as well as the behavior of the energy, specific heat, susceptibility, and magnetization in the vicinity of the critical point for the two-dimensional, zero-field next-nearest-neighbor problem. Campbell and Schick³⁹ studied the plane triangular lattice with nearest-neighbor repulsion and next-nearest-neighbor attraction in the Bethe-Peierls approximation. Nauenberg and Nienhuis⁴⁰ used the renormalization group method to obtain the $\lambda$-dependence of the critical temperature for a square Ising lattice in the range $-1 < \lambda < 1$. Meijer and Cunningham⁴¹ compared the Bethe-Peierls results of Campbell and Schick with their own Monte Carlo calculations. Takase⁴²⁴³ used Monte Carlo simulations and series expansions to explore the $\lambda$-dependence of the critical temperature (as well as of the energy and the magnetization in the vicinity of the critical point) for a square Ising lattice with repulsive next-nearest-neighbor interactions. Selke⁴⁴ performed Monte Carlo calculations to study the three-dimensional Ising model with next-nearest-neighbor repulsion along one direction only. Binder and Landau,⁴⁵ using Monte Carlo calculations, obtained the phase diagrams and critical behavior of two-dimensional antiferromagnets with next-nearest-neighbor interactions in nonzero field. Binder⁴⁶ used Monte Carlo methods to investigate the energy, free energy, entropy, and magnetization of the face-centered cubic Ising antiferromagnet with next-nearest-neighbor interactions in nonzero field.

The present model is also to be viewed in the context of several lattice-based studies of water and water-like behavior. These

(26) Rasmussen, D. H.; MacKenzie, A. P.; Angell, C. A.; Tucker, J. C. Science 1973, 181, 342.
(27) Angell, C. A.; Shuppert, J.; Tucker, J. C. J. Phys. Chem. 1973, 77, 3092.
(28) Speedy, R. J.; Angell, C. A. J. Chem. Phys. 1976, 65, 851.
(29) Angell, C. A. NATO Advanced Summer Institute on Correlation and Connectivity in Biophysics, Corsica, France, July 1990. de Neufville, J. Private communication to C. A. Angell.
(30) Kanno, H.; Speedy, R. J.; Angell, C. A. Science 1975, 89, 880.
(31) Green, J. L.; Durben, D. J.; Wolf, G. H.; Angell, C. A. Science 1990, 249, 649.

(32) Domb, C.; Potts, R. B. Proc. R. Soc. (London) 1951, A210, 125.
(33) Fan, C.; Wu, F. Y. Phys. Rev. 1969, 179, 560.
(34) Dalton, N. W.; Wood, D. W. J. Math. Phys. 1969, 10, 1271.
(35) Gibberd, R. W. J. Math. Phys. 1969, 10, 1026.
(36) Stephenson, J.; Betts, D. D. Phys. Rev. B 1970, 2, 2702.
(37) Landau, D. P. J. Appl. Phys. 1971, 42, 1284.
(38) Landau, D. P. Phys. Rev. B 1980, 21, 1285.
(39) Campbell, C. E.; Schick, M. Phys. Rev. A 1972, 5, 1919.
(40) Naunberg, M.; Nienhuis, B. Phys. Rev. Lett. 1974, 33, 944.
(41) Meijer, P. E.; Cunningham, G. W. Phys. Rev. B 1977, 15, 3436.
(42) Takase, S. J. Phys. Soc. Jpn. 1976, 40, 1240.
(43) Takase, S. J. Phys. Soc. Jpn. 1977, 42, 1819.
(44) Selke, W. Z. Phys. B 1978, 29, 133.
(45) Binder, K.; Landau, D. P. Phys. Rev. B 1980, 21, 1941.
(46) Binder, K. Z. Phys. B 1981, 45, 61.

include the work of Bell, Lavis, and co-workers,⁴⁷⁻⁵² Meijer and co-workers,⁵³⁻⁵⁵ and Fleming and Gibbs.⁵⁶,⁵⁷ Bell and Lavis⁴⁷,⁴⁸ introduced two plane (two-dimensional) models, the interstitial⁴⁷ and the orientable molecule⁴⁸ models on a triangular lattice, which they solved through a first-order (quasichemical) approximation.⁵⁸ The Bell-Lavis models are both characterized by a competition between a low-energy open structure and a high-energy close-packed structure brought about by the possibility of forming bonding and nonbonding interactions. In the interstitial model, there is a division of the original lattice into two sublattices (honeycomb and interstitial sublattices), with nearest-neighbor molecules on the honeycomb lattice forming bonded interactions (lower energy), while nearest-neighbor pairs belonging to different sublattices are unbonded. The open structure is then the completely filled honeycomb sublattice with an empty interstitial sublattice, both sublattices being filled in the close-packed structure. In the orientable molecule model, each molecule has three possible bonding directions and two possible orientations. If nearest-neighbor molecules have bonds pointing toward each other, bonding results (lower energy). A competition results between an open structure characterized by a honeycomb arrangement with 1/3 of the sites vacant, and the close-packed structure in which the lattice is completely filled. In both the interstitial and orientable molecule models, the open structure is stable at low temperatures and pressures, giving rise to water-like behavior (density maxima). Bell⁴⁹ extended these ideas to three dimensions. He considered a water model consisting of a body-centered lattice in which molecules can form tetrahedrally oriented bonds with their nearest-neighbors, when appropriately oriented. In addition, he introduced a (repulsive) energy penalty against close packing. Bell solved the problem in the quasichemical approximation. Density anomalies arise as a consequence of the competition between an open tetrahedrally bonded structure on a half-filled lattice and a close-packed network of interpenetrating tetrahedrally bonded structures, which Bell compared to ice I(c) and ice VII, respectively. Young and Lavis⁵⁰ and Southern and Lavis⁵¹ used real-space renormalization to investigate the critical behavior of the two-dimensional Bell-Lavis model. The three-dimensional model of Bell⁴⁹ was solved in the zeroth-order (Bragg-Williams) approximation by Bell and Salt.⁵² This caused the disappearance of density anomalies in the liquid phase, but enabled the incorporation of two long-range ordered (ice-like) solid phases, of which the open one melted into a denser liquid. Meijer and co-workers⁵³⁻⁵⁵ used the cluster variation method to solve Bell's three-dimensional water model and studied its phase behavior and stability limits. They pointed out explicitly the importance of next-nearest-neighbor repulsions. Fleming and Gibbs⁵⁶,⁵⁷ used a perturbation scheme to calculate the free energy and several thermodynamic properties of a model similar to Bell's three-dimensional model. They obtained density maxima, as well as a water-like vapor-liquid coexistence curve, with a maximum in the saturated liquid density.

The present treatment is not aimed at modeling water. Rather, we seek to establish a general microscopically based connection between density anomalies and loss of stability upon supercooling. The phenomenological arguments on which Figure 5 was originally based²²⁻²⁴ will thus be given a molecular basis. Core softening provides the simplest and most general microscopic model consistent with the complex behavior described in Figure 5. The lattice gas with attractive nearest-neighbor and repulsive next-nearest-neighbor interactions (Figure 6) is the simplest case of core softening. It will now be shown that the competition between nearest-neighbor attraction and next-nearest-neighbor repulsion is enough to give rise to density anomalies and hence to the possibility of loss of stability upon supercooling. The underlying mechanism, as in the case of water, will be shown to be the competition between open structures which can "melt" into denser, high-energy, close-packed configurations through the input of thermal or mechanical energy. To see this, consider the perfectly ordered two-dimensional arrangements shown in Figure 7. In the open structure, there are no next-nearest-neighbor (diagonal) interactions, and half of the sites are occupied. Then, with $N$ denoting the number of sites in the lattice, and $M$ the number of molecules,

$$2M = N \tag{18}$$

$$E = -M\epsilon \tag{19}$$

$$H = -M\epsilon + 2Pv_0M = M\epsilon\left[\frac{2Pv_0}{\epsilon} - 1\right] \tag{20}$$

where $E$ and $H$ are the configurational energy and enthalpy, $P$ is the (two-dimensional) pressure, and $v_0$, the two-dimensional volume per site. For the compact structure, on the other hand,

$$M = N \tag{21}$$

$$E = 2M\epsilon(\lambda - 1) \tag{22}$$

$$H = M\epsilon\left[\frac{Pv_0}{\epsilon} + 2(\lambda - 1)\right] \tag{23}$$

where $\lambda$ is the height of the repulsive barrier in units of the attractive well (see Figure 6). Therefore, at absolute zero, the close-packed structure will be stable if

$$\frac{Pv_0}{\epsilon} > 2\left(\lambda - \frac{1}{2}\right) \tag{24}$$

![](./images/812292514684862464_7.jpg)

Figure 7. Formation of open (a) and close-packed (b) structures in a two-dimensional lattice fluid in the low-temperature limit.

![](./images/812292514684862464_8.jpg)

Figure 8. Pressure dependence of the low-temperature limits of the enthalpy and energy changes associated with the transition from open-to-close-packed structure in two dimensions. $M$ is the number of molecules in the lattice. $\Delta e$ and $\Delta h$ are the energy and enthalpy changes per molecule.

(47) Bell, G. M.; Lavis, D. A. *J. Phys. A: Gen. Phys.* **1970**, 3, 427.
(48) Bell, G. M.; Lavis, D. A. *J. Phys. A: Gen. Phys.* **1970**, 3, 568.
(49) Bell, G. M. *J. Phys. C: Solid State Phys.* **1972**, 5, 889.
(50) Young, A. P.; Lavis, D. A. *J. Phys. A: Math. Gen.* **1979**, 12, 229.
(51) Southern, B. W.; Lavis, D. A. *J. Phys. A: Math. Gen.* **1980**, 13, 251.
(52) Bell, G. M.; Salt, D. W. *J. Chem. Soc., Faraday Trans. 2* **1972**, 72, 76.
(53) Meijer, P. H. E.; Kikuchi, R.; van Royen, E. *Physica* **1982**, 115A, 124.
(54) van Royen, E.; Meijer, P. H. E. *Physica* **1984**, 127A, 87.
(55) van Royen, E.; Meijer, P. H. E. *Physica* **1986**, 139A, 412.
(56) Fleming, P. D.; Gibbs, J. H. *J. Stat. Phys.* **1974**, 10, 157.
(57) Fleming, P. D.; Gibbs, J. H. *J. Stat. Phys.* **1974**, 10, 351.
(58) Guggenheim, E. A.; McGlashan, M. C. *Proc. R. Soc.* **1951**, 206, 335.

<table>
<caption>TABLE I: Configurations, Energies, and Degeneracies for the One-Dimensional Model</caption>
<thead>
<tr>
<th>configurn no.</th>
<th>energy</th>
<th>degeneracy</th>
<th>$\psi_i^\infty$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1, $\boldsymbol{\bullet\!\!\!\boldsymbol{-}\!\!\!\boldsymbol{\bullet}}$</td>
<td>$(\lambda - 2)\epsilon$</td>
<td>1</td>
<td>$\rho^3$</td>
</tr>
<tr>
<td>2, $\boldsymbol{\bullet\!\!\!\boldsymbol{-}\!\!\!\boldsymbol{\bullet}\!\!\!\boldsymbol{-}\!\!\!\bigcirc}$</td>
<td>$-\epsilon$</td>
<td>2</td>
<td>$\rho^2(1 - \rho)$</td>
</tr>
<tr>
<td>3, $\boldsymbol{\bullet\!\!\!\boldsymbol{-}\!\!\!\bigcirc\!\!\!\boldsymbol{-}\!\!\!\boldsymbol{\bullet}}$</td>
<td>$\lambda\epsilon$</td>
<td>1</td>
<td>$\rho^2(1 - \rho)$</td>
</tr>
<tr>
<td>4, $\boldsymbol{\bullet\!\!\!\boldsymbol{-}\!\!\!\bigcirc\!\!\!\boldsymbol{-}\!\!\!\bigcirc}$</td>
<td>0</td>
<td>2</td>
<td>$\rho(1 - \rho)^2$</td>
</tr>
<tr>
<td>5, $\bigcirc\!\!\!\boldsymbol{-}\!\!\!\boldsymbol{\bullet}\!\!\!\boldsymbol{-}\!\!\!\bigcirc$</td>
<td>0</td>
<td>1</td>
<td>$\rho(1 - \rho)^2$</td>
</tr>
<tr>
<td>6, $\bigcirc\!\!\!\boldsymbol{-}\!\!\!\bigcirc\!\!\!\boldsymbol{-}\!\!\!\bigcirc$</td>
<td>0</td>
<td>1</td>
<td>$(1 - \rho)^3$</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE II: Configurations, Energies, and Degeneracies for the Two- and Three-Dimensional Models</caption>
<thead>
<tr>
<th>configurn no.</th>
<th>energy</th>
<th>degeneracy</th>
<th>$\psi_i^\infty$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1, ![](./images/812292514684862464_9.jpg)</td>
<td>0</td>
<td>1</td>
<td>$(1 - \rho)^4$</td>
</tr>
<tr>
<td>2, ![](./images/812292514684862464_10.jpg)</td>
<td>0</td>
<td>4</td>
<td>$\rho(1 - \rho)^3$</td>
</tr>
<tr>
<td>3, ![](./images/812292514684862464_11.jpg)</td>
<td>$-\epsilon$</td>
<td>4</td>
<td>$\rho^2(1 - \rho)^2$</td>
</tr>
<tr>
<td>4, ![](./images/812292514684862464_12.jpg)</td>
<td>$\lambda\epsilon$</td>
<td>2</td>
<td>$\rho^2(1 - \rho)^2$</td>
</tr>
<tr>
<td>5, ![](./images/812292514684862464_13.jpg)</td>
<td>$(\lambda - 2)\epsilon$</td>
<td>4</td>
<td>$\rho^3(1 - \rho)$</td>
</tr>
<tr>
<td>6, ![](./images/812292514684862464_14.jpg)</td>
<td>$2\epsilon(\lambda - 2)$</td>
<td>1</td>
<td>$\rho^4$</td>
</tr>
</tbody>
</table>

If $\lambda < 1/2$, the denser structure will always be favored at equilibrium when $T = 0$. Furthermore, the close-packed structure is energetically unfavorable only if $\lambda > 1/2$. These considerations are illustrated in Figure 8, where the vertical axis is the enthalpy (or energy) change associated with the transition open-to-close-packed as a function of pressure, at $T = 0$. The open structure is stable at pressures lower than that at which the enthalpy line intersects the horizontal axis. Under these conditions, isobaric heating leads to "melting" into denser configurations. This possibility of forming open structures stabilized by next-nearest-neighbor repulsion is obviously not limited to two dimensions. In a one-dimensional lattice, the ordered structure with no nearest-neighbor interactions occurs with pairs of neighboring sites alternatively vacant and full, and in three dimensions, by stacking planes such as the one shown in the left-hand side of Figure 7 separated by empty planes. In both cases, the dense structure is the completely filled lattice. The minimum $\lambda$-value below which the denser structure is always favored at $T = 0$ is also $1/2$ in one and three dimensions; the minimum pressures (in units of $\epsilon/v_0$) above which the denser structure is favored at $T = 0$ are $(\lambda - 1/2)$ and $4(\lambda - 1/2)/3$, respectively. The preceding analysis is identical with the one used by Bell and Lavis$^{47,48}$ and by Bell$^{49}$ to explore the low-temperature stability of open and close-packed structures in their two- and three-dimensional models.

The equation of state and chemical potential for the lattice gas with attractive nearest-neighbor and repulsive next-nearest-neighbor interactions were obtained through the application of the quasichemical approximation;$^{58}$ the technical details of the calculations follow closely the approach of Bell and co-workers.$^{47-49}$ In essence, the method involves choosing an elementary cell and approximating the number of configurations accessible to $M$ molecules on $N$ lattice sites ($\rho = M/N$) as

$$
\Omega(\rho, T)=\Omega_{0} \frac{N_{\text {cells }}!}{\prod_{i=1}^{m}\left[\left(N_{\text {cells }} \psi_{i}\right)!\right]^{\omega_{i}}}
\tag{25}
$$

where $N_{\text{cells}}$ is the number of cells into which the lattice has been divided, $\psi_i(\rho, T)$ is the probability of occurrence of the $i$th configuration of the elementary cell, $\omega_i$ is the degeneracy associated with the $i$th configuration, $m$ is the number of distinguishable configurations which can be assigned to an elementary cell, and $\Omega_0$ is a normalization constant. Configurations, degeneracies, energies, and $\psi_i^\infty$ [$=\psi_i(\rho, \infty)$] values for the one- two- and three-dimensional problems (the latter two on square and simple cubic lattices, respectively) are given in Tables I and II. The number of cells is determined by requiring that the total number of nearest-neighbor contacts be conserved upon tessellating the lattice with elementary cells

$$
N_{\text {cells }}=z N / 2 \eta
\tag{26}
$$

where $z$ is the coordination number (2, 4, 6 in one, two, and three dimensions, respectively), and $\eta$, the number of nearest-neighbor contacts in a cell (2, 4, 4 in one, two, and three dimensions, respectively). Tessellations for the one- two- and three-dimensional cases are shown in Figure 9. Note that cells share sites, but not interactions (contacts).

![](./images/812292514684862464_15.jpg)

![](./images/812292514684862464_16.jpg)

Figure 9. Tessellations for the quasichemical solution of the one-, two-, and three-dimensional problems. The tessellations preserve nearest-neighbor contacts.

![](./images/812292514684862464_17.jpg)

Figure 10. Bond-moving step required to preserve next-nearest-neighbor interactions upon tessellation.

The number of next-nearest-neighbor contacts is $N$, $2N$, and $6N$ in the linear, square, and simple cubic lattices. The tessellations shown in Figure 9, however, conserve only nearest-neighbor contacts, giving rise to $N/2$, $N$, and $3N/2$ next-neighbor contacts in one, two, and three dimensions, respectively. Therefore, the tessellation implies a bond-moving step (shown in Figure 10 for the two-dimensional case), such that $\lambda/\lambda_{\text{true}} = 2, 2, 4$ in one, two, and three dimensions, respectively (e.g., one-dimensional results for $\lambda = 1$ would represent the quasichemical approximation to the properties of a "true" system with $\lambda = 1/2$). Since our goal is not to model a particular true fluid, the bond-moving step is only formal. Two-dimensional phase envelopes for several values of $\lambda_{\text{true}}$ were obtained via grand canonical Monte Carlo simulations

on a $40 \times 40$ lattice with periodic boundary conditions; they were in good qualitative agreement with the corresponding quasi-chemical phase envelopes for $\lambda=2 \lambda_{\text {true }}$, except in the critical region.

The normalization constant in eq 25 is calculated by requiring that $\Omega(\rho, T)$ be exact in the high-temperature limit. In this case, molecules are distributed randomly in the lattice, and the number of configurations is $N! /\{(N \rho)![N(1-\rho)]!!\}$

$$
\frac{N!}{(N \rho)![N(1-\rho)]!}=\Omega_{0} \frac{\left(\frac{z N}{2 \eta}\right)!}{\prod_{i=1}^{m}\left[\left(\frac{z N}{2 \eta} \psi_{i}^{\infty}\right)!\right]^{\omega_{i}}} \quad(27)
$$

which gives

$$
N^{-1} \ln \Omega_{0}=\gamma[\rho \ln \rho+(1-\rho) \ln (1-\rho)] \quad(28)
$$

where $\gamma$ is $1 / 2,1$, and 2 in one, two, and three dimensions. The probabilities $\psi_{i}$ must satisfy the material balance constraints

$$
\rho=\frac{1}{\alpha} \sum_{i=1}^{m} \omega_{i} \psi_{i} n_{i}
$$

$$
1-\rho=\frac{1}{\alpha} \sum_{i=1}^{m}\left(\alpha-n_{i}\right) \omega_{i} \psi_{i}
$$

where $\alpha$ is the number of sites per cell and $n_{i}$, the number of occupied sites in the $i$ th configuration. Equations 29 and 30 imply the normalization condition

$$
\sum_{i=1}^{m} \omega_{i} \psi_{i}=1
$$

The energy is given by

$$
E(\rho, T)=\frac{z N}{2 \eta} \sum_{i=1}^{m} \epsilon_{i} \omega_{i} \psi_{i}
$$

and the canonical partition function, $Q$, by
$$
\begin{aligned}
A(N, \rho, T)=-k T & \ln Q(N, \rho, T)= \\
& -k T \ln \left\{\Omega(\rho, T) \exp \left[-\frac{E(\rho, T)}{k T}\right]\right\}
\end{aligned}
$$

where $A$ is the Helmholtz energy, and we have replaced the true partition function by its (still undetermined) maximum term. By use of eqs 25 and 32, the Helmholtz energy becomes $(a=N^{-1}A$ $=\rho a^{\prime} ; a^{\prime}=M^{-1} A$ )
$$
\begin{aligned}
& a(\rho, T)= \\
& \quad-\gamma k T[\rho \ln \rho+(1-\rho) \ln (1-\rho)]+\delta \sum_{i=1}^{m} \omega_{i} \psi_{i}\left(\epsilon_{i}+k T \ln \psi_{i}\right) \\
& \quad(34)
\end{aligned}
$$

where $\delta$ is $1 / 2,1 / 2$, and $3 / 4$ in one, two, and three dimensions, respectively, and $\psi_{i}$ is a (still undetermined) function of density and temperature. We minimize the Helmholtz energy by finding the probability distribution $\left(\psi_{i}\right)$ that maximizes $(\ln \Omega-E / k T)$. Then, as shown in the Appendix, we obtain, for the one-dimensional fluid's pressure and chemical potential

$$
P^{*}=\frac{T^{*}}{2} \ln \left\{\frac{\frac{1}{3}\left[2 x^{-(1+\lambda)}+1\right]+2 r+r^{2} x^{\lambda}}{r^{2} x^{\lambda}}\right\}
$$

$$
\mu^{*}=-\frac{T^{*}}{2} \ln \left(\frac{\rho r^{3}}{1-\rho}\right)
$$

In two dimensions,
$$
\begin{aligned}
& P^{*}=\frac{T^{*}}{2} \times \\
& \ln \left\{\frac{(1-\rho)\left[x^{(\lambda / 2-1)}+3 r^{1 / 2}+r\left(2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right)+r^{3 / 2}\right]}{x^{(\lambda / 2-1)}}\right\}
\end{aligned}
$$

$$
\mu^{*}=(\lambda-2)+T^{*} \ln \frac{r(1-\rho)}{\rho}
$$

and, in three dimensions,
$$
\begin{aligned}
& P^{*}=\frac{3 T^{*}}{4} \times \\
& \ln \left\{\frac{(1-\rho)^{5 / 3}\left[x^{(\lambda / 2-1)}+3 r^{1 / 2}+r\left(2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right)+r^{3 / 2}\right]}{x^{(\lambda / 2-1)}}\right\}
\end{aligned}
$$

$$
\mu^{*}=\frac{3(\lambda-2)}{2}+T^{*} \ln \left[r^{3 / 2}\left(\frac{1-\rho}{\rho}\right)^{2}\right]
$$

where
$$
P^{*}=P v_{0} / \epsilon
$$

$$
\mu^{*}=\mu / \epsilon
$$

$$
T^{*}=k T / \epsilon
$$

$$
x=\exp (-\epsilon / k T)
$$

In the above equations, $r$ is a parameter related to dimensionless density $\rho$ (fractional coverage) by the relations

$$
\rho=\frac{r^{-1} x^{-(2+\lambda)}+1 / 3\left[4 x^{-(1+\lambda)}+2\right]+r}{r^{-1} x^{-(2+\lambda)}+1 / 2\left[4 x^{-(1+\lambda)}+2\right]+3 r+r^{2} x^{\lambda}}
$$

$$
\rho=\frac{1+r^{1 / 2}\left[2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right]+3 r+x^{(\lambda / 2-1)} r^{3 / 2}}{r^{-1 / 2} x^{(\lambda / 2-1)}+4+2 r^{1 / 2}\left[2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right]+4 r+x^{(\lambda / 2-1)} r^{3 / 2}}
$$

where eq 45 is valid in one dimension and eq 46 in two and three dimensions. The quantity $r$ is defined in the Appendix (eqs A.6, A.11). The structure of the equations is therefore

$$
P^{*}=P^{*}(\rho, r, T)
$$

$$
\rho=\rho(r, T)
$$

$$
\mu^{*}=\mu^{*}(\rho, r, T)
$$

The pressure and chemical potential are given as functions of density and temperature by two pairs of parametric equations ((47) and (48) for the pressure, (49) and (48) for the chemical potential). $r$ is obtained numerically from eq 48 for any given $(\rho, T)$.

Figure 11 shows isobars for the one-dimensional fluid. Note that some curves have positive slope at low temperature, indicating that the fluid contracts when heated at constant pressure, and therefore has a negative thermal expansion coefficient. The region where density anomalies occur is bounded from above and from below in temperature, pressure, and density. Qualitatively very similar behavior was obtained by Bell $^{59}$ via a one-dimensional model in which next-nearest-neighbor molecules can form bonded (low-energy) interactions when the intermediate site is empty.

For pressures lower than 0.2, the first-order approximation predicts that as $T$ tends to 0 the fraction of nearest-neighbor contacts approaches $50 \%$, and the fraction of next-nearest-neighbor contacts vanishes (Figure 12). In the quasichemical approximation, this open structure is realized by tessellating the lattice with cells having configuration 2 (Table I) but alternating in direction $\left(e^{\prime}, f, f^{\prime}, f, e^{\prime}, f, f^{\prime}, f, e^{\prime}, \ldots\right.$; where e denotes empty, $\mathrm{f}$, full, and primes denote the beginning and end of a cell). For pressures above 0.067 (Figure 13a), this structure gives way, upon isobaric heating, to arrangements with a progressively larger fraction of completely filled cells (configuration 1; Table I), and hence to a density increase. For pressures below 0.067 (Figure 13b), the open structure gives way, upon isobaric heating, to arrangements with a progressively larger fraction of empty cells (configuration 6; Table I), and hence to a density decrease. Note the inversion in the relative stability of configurations 1 and 6 between parts $a$ and $b$ of Figure 13, which results in the disappearance of density

(59) Bell, G. M. J. Math. Phys. 1969, 10, 1753.

![](./images/812292514684862464_18.jpg)

Figure 11. Density-temperature relationship for the one-dimensional fluid. Labels on each curve are dimensionless pressures.

![](./images/812292514684862464_19.jpg)

Figure 12. Fraction of active nearest-neighbor (nn) and next-nearest- neighbor (nnn) contacts for the one-dimensional fluid. Labels on the curves are dimensionless pressures.

anomalies at low pressure. This is illustrated in Figure 14, which shows loci of density maxima for different values of $\lambda$. The fractions of active nearest- and next-nearest-neighbor contacts (fnn, fnnn) were calculated as follows

$$
\mathrm{fnn} = \sum_{i=1}^{m} \omega_{i} \psi_{i} \mathrm{nn}_{i} / \eta \tag{50}
$$

$$
\mathrm{fnnn} = 2 \sum_{i=1}^{m} \omega_{i} \psi_{i} \mathrm{nnn}_{i} / \eta \tag{51}
$$

where $\eta$ has already been defined (see eq 26) and $\mathrm{nn}_{i}$ and $\mathrm{nnn}_{i}$ represent the number of active nearest- and next-nearest-neighbor contacts in the $i$th configuration.

From Figures 11-14 it can be seen that indeed core softening gives rise to density anomalies in one dimension and that this behavior results from the possibility of forming an open structure which can be disrupted into closer packed configurations by input of thermal or mechanical energy. The normalization constant in eq 25, however, is exact in the high-temperature limit. This means that the quasichemical approximation becomes progressively less accurate at low temperatures. Important aspects of the behavior shown in Figures 11-14 as $T$ tends to 0 need to be critically examined. In the first place, the perfectly regular open structure described above has a true fractional occupancy of $3/4$, whereas the quasichemical approximation predicts a value of $2/3$ (100% of the cells are in configuration 2, whose fractional oc- cupancy is $2/3$). Secondly, there are no next-nearest-neighbor contacts in configuration 2, whereas $1/2$ of the next-nearest- neighbor contacts in the tessellation $e',f,f',f,e',...,$ are active. These discrepancies arise from applying a cell-based configuration counting to a perfectly ordered lattice. Such inconsistencies disappear at higher temperatures; at low temperatures, they be- come progressively less severe in higher dimensional lattices, as will be shown below in connection with the two-dimensional fluid.

![](./images/812292514684862464_20.jpg)

Figure 13. Fraction of cells in configurations 1, 2, and 6 (see Table I) for the one-dimensional fluid. $P^{*}$ = 0.15 (a, top); 0.05 (b, bottom).

![](./images/812292514684862464_21.jpg)

Figure 14. Loci of density maxima for the one-dimensional fluid for different values of $\lambda$.

Figure 15 shows the coexistence region and spinodal curves for the two-dimensional fluid for different values of $\lambda$. There is no phase transition for $\lambda \geq 1$. The critical temperature for $\lambda = 0$ is 0.696 (in units of $\epsilon/k$); the exact value for the two-dimensional Ising model is 0.567 27, and the prediction of the quasichemical approximation using a two-site linear cell, 0.721 347. Stable density maxima occur only for $\lambda \geq 1$. In the low-temperature limit, the minimum and maximum pressures between which density maxima are possible are $0.125z(\lambda - 1)$ and $0.25z(\lambda - 1)$, respectively. These bounds are valid in two and three dimensions. Figure 16a shows the $P^{*} = 0.23$ isobar for the two-dimensional fluid with $\lambda = 1.2$. Since this pressure exceeds 0.2, there are no density maxima. In the low-temperature limit the lattice is completely filled, and the fraction of active nearest- and next-

![](./images/812292514684862464_22.jpg)

Figure 15. Binodal and spinodal curves for the two-dimensional fluid for different values of $\lambda$.

![](./images/812292514684862464_23.jpg)

![](./images/812292514684862464_24.jpg)

Figure 16. Density, fractional occupancies of the various types of cells (see Table II), and fraction of active nearest-neighbor (nn) and next-nearest-neighbor (nnn) contacts for the two-dimensional fluid. $P^{*}=0.23$ (a, top); 0.20 (b, bottom). All nn, but only active nnn contacts shown in squares.

nearest-neighbor contacts approaches 100% (configuration 6). Upon increasing the temperature isobarically, the lattice at first becomes progressively populated with cells having configuration 3. The fraction of these cells peaks slightly below $T^{*}=0.2$ and decreases thereafter. Figure 16b shows the $P^{*}=0.2$ isobar. In two dimensions and for $\lambda=1.2$, this is the upper limit of pressure above which density maxima no longer occur. Note that in the low-temperature limit 75% of the cells are in configuration 3, and 25% in configuration 6, giving an overall fractional coverage of 62.5%. Below $P^{*}=0.2$ (Figure 17a), the lattice is populated completely by cells having configuration 3, giving rise to a fractional coverage of $1/2$ and fractions of active nearest- and next-nearest-neighbor contacts of 50% and 25%, respectively. This is exactly the open structure shown in Figure 7. It can be generated by tessellating the lattice with cells in configuration 3 with orientations which alternate from row to row. Note that there is perfect agreement between the cell-based predicted fractions of occupied sites and of active nearest- and next-nearest-neighbor contacts $(1/2,1/4,0)$ and the true values, in contrast to the one-dimensional case. Density maxima occur as a consequence of the gradual population of the lattice by completely filled cells (configuration 6) in agreement with the discussion of Figure 7. Below $P^{*}=0.1$ density anomalies disappear due to the inversion in the relative stability of configurations 1 and 6 (Figure 17b). Although in the low-temperature limit the structure of the lattice is identical for $P^{*}=0.18$ and 0.1 (Figure 17, a and b), isobaric heating at or below $P^{*}=0.1$ now leads to a preferential population with empty cells (configuration 1), and hence density anomalies disappear.

![](./images/812292514684862464_25.jpg)

![](./images/812292514684862464_26.jpg)

Figure 17. Density, fractional occupancies of the various types of cells (see Table II), and fraction of active nearest-neighbor (nn) and next-nearest-neighbor (nnn) contacts for the two-dimensional fluid. $P^{*}=0.18$ (a, top); 0.10 (b, bottom). All nn, but only active nnn contacts shown in squares.

Figure 18 shows the coexistence region for the three-dimensional fluid, for different values of $\lambda$. The critical temperature for $\lambda=$ 0 is 1.225; the best accepted numerical value for the three-dimensional Ising model is 1.12428, and the prediction of the quasichemical approximation using a two-site linear cell, 1.2333. As $\lambda$ is increased above 0.9, a second phase transition occurs. This is an example of the type of phase transition due to core softening investigated by Stell and co-workers. $^{11-16}$ In the present case, both transitions have the same critical temperature and are symmetric about $\rho=1/2$, the triple-point liquid density. The phase diagram is shown in pressure-temperature coordinates in Figure 19. It can be seen that the effect of increasing $\lambda$ is to decrease the critical temperature, decrease the critical pressure of the low-density transition, and increase the critical pressure of the high-density transition. The appearance of a second phase transition is significant in the context of core softening, because it allows the liquid to become supercooled with respect to a denser phase. The nature

![](./images/812292514684862464_27.jpg)

Figure 18. Phase envelopes for the three-dimensional fluid for different values of $\lambda$.

![](./images/812292514684862464_28.jpg)

Figure 19. Pressure-temperature projection of the phase diagram of the three-dimensional fluid for different values of $\lambda$.

of the latter, however, plays no role in the mechanical stability (or lack thereof) of the supercooled phase. Hence, it will be possible to test the stability of a supercooled core-softened fluid with considerably more generality than would at first appear possible from the fluid-fluid character of the high-density tran- sition.

Figure 20 shows the relationship between the phase boundaries, stability limits, and density anomalies for the three-dimensional core-softened fluid with $\lambda=1$. The lettering corresponds to that of Figure 5. The superheated liquid spinodal of the low-density transition (cg) exhibits a change in slope upon encountering the (entirely metastable) locus of density maxima (aeg). Curve af is the spinodal along which the supercooled core-softened fluid becomes unstable. Portions of the superheated high-density fluid spinodal (m, corresponding to transition bd) and the supercooled vapor spinodal (cn, corresponding to transition bc) are also shown. The similarity between Figures 5 and 20 is obvious.

The behavior shown in Figure 20 occurs for $0.99 \leq \lambda \leq 1.001$. Since the maximum pressure at which density maxima occur in the low-temperature limit is $(z / 4)(\lambda-1)$ in this model, $^{60}$ the high-pressure intersection of density maxima and spinodal loci (point a, Figure 5) occurs at pressures very close to zero. Except for this limitation, all the other features shown in Figure 5 are reproduced by the lattice model. The complex predicted behavior (density maxima in conjunction with a tensile strength maximum or reentrant spinodal, loss of stability upon supercooling) is therefore in qualitative agreement with phenomenological ther- modynamic arguments and experiments. The most significant aspect of Figure 20 is the reentrant spinodal (cag) and its rela- tionship to density anomalies. Curve af is simply the spinodal associated with the second fluid-fluid transition. It is a conse- quence of core softening but bears little relation to a limit of stability associated with a solid-liquid transition.

![](./images/812292514684862464_29.jpg)

Figure 20. Continuous stability boundary (cgaf) and locus of density maxima (aeg) for the three-dimensional liquid; $\lambda=1$. b and c are triple and critical points. cn and m are portions of the supercooled vapor and superheated high-density fluid spinodals.

### Conclusion
There are two possible absolute limits to the extent of super- cooling to which liquids can be subjected: the Kauzmann tem- perature and the spinodal condition. In this paper we have in- vestigated the necessary conditions for spinodal collapse. A consistent picture of this phenomenon is gradually emerging. In this view, spinodal collapse is possible only for liquids capable of contracting when heated isobarically. Microscopically, this occurs via the formation of open structures which are stabilized by re- pulsions and which can be collapsed into denser arrangements through the input of thermal or mechanical energy.

Within the context of a pairwise additive and spherically symmetric description, both negative thermal expansion coeffi- cients and loss of stability at high density can be explained by core softening. Effective pair potentials for several liquid metals exhibit core softening. To the best of our knowledge, no stable density maxima for liquid metals have been reported. Never- theless, Ga, Bi, and Sn expand on freezing. Density measurements in the supercooled region as well as heat capacity and isothermal compressibility data for these elements should shed considerable light on the general problem of the stability boundaries of su- percooled liquids which we have addressed in this paper. The possibility of spinodal collapse in supercooled Ge and Te has recently been suggested, evidence of heat capacity anomalies insupercooled Te having recently been reported. $^{29}$

A lattice model with nearest-neighbor attraction and next- nearest-neighbor repulsion exhibits density anomalies in one, two, and three dimensions, and a reentrant spinodal in three dimensions. This model is deliberately simple. Consequently, the phase with respect to which the supercooled liquid becomes metastable is not solid in the extended first-order approximation. However, the purpose of the model is not to mimic the behavior of a particular real fluid, much less to predict the location of stability boundaries of, say, water. Rather, it shows how a system capable of forming stable open structures at low temperatures and pressures can exhibit density anomalies and become mechanically unstable when supercooled, leading to a reentrant spinodal.

It is hoped that a combination of more sophisticated models, together with the availability of data on the behavior of supercooled liquid metals such as Ga, Sn, Bi, Te, and Ge, will contribute toward an improved understanding of the important yet currently poorly understood problem of determining the absolute boundaries within which the liquid state of matter can exist.

Acknowledgment. We gratefully acknowledge the financial support of the National Science Foundation (Presidential Young

(60) Raghavan, V. S. MS Thesis, Princeton University, 1990.

Spinodal Curve of Some Supercooled Liquids

Investigator Award CBT-8657010 to P.G.D.), the Camille and Henry Dreyfus Foundation (1989 Teacher-Scholar Award to P.G.D.), and the U.S. Department of Education for a Fellowship for Graduate Assistance in Chemical Engineering to SSB. We are indebted to Ariel Chialvo for the simulation results of Figures 2 and 3.

### Appendix
We first prove that, for a potential such as that defined by eq 12, the virial is a monotonically increasing function of density above the temperature at which the second virial coefficient vanishes (the Boyle temperature). To this end, we write the virial equation of state
$$
P=\rho k T\left(1+\rho B+\rho^{2} C+\ldots\right)=\rho k T+\rho k T\left(\rho B+\rho^{2} C+\ldots\right) \quad \text { (A.1) }
$$

Comparison with eq 4 yields
$$
\psi=6 k T\left(\rho B+\rho^{2} C+\ldots\right) \quad \text { (A.2) }
$$
and, therefore,
$$
\frac{1}{6}\left(\frac{\partial \psi}{\partial \rho}\right)_{T}=B k T+2 \rho k T C+\ldots \underset{\rho=0}{\longrightarrow} B k T \quad \text { (A.3) }
$$

Equation A.3 shows that the sign of the slope of an isotherm in the virial-density plane is that of the second virial coefficient in the zero density (ideal gas) limit. Therefore, the initial slope of the virial-density curve decreases with density below the Boyle temperature and increases with density at higher temperatures. Since isotherms necessarily have positive curvature in the virial-density plane for a potential such as that defined by eq 12 (see Figures 1, 2, and 3), it follows that above the Boyle temperature the virial is a monotonically increasing function of density at a given temperature.

We now give the derivation of the equilibrium values for $\psi_{i}(\rho, T)$, the equation of state, and the chemical potential. The goal is to find the probability distribution of cells that maximizes the Helmholtz energy, $\ln \Omega-E / k T$. To this end, we write
$$
\begin{aligned}
& \left(\frac{\partial a}{\partial \psi_{j}}\right)_{\rho, T, \psi_{l \neq j, k, l}}= \\
& \left(\frac{\partial a}{\partial \psi_{j}}\right)_{\rho, T}+\left(\frac{\partial a}{\partial \psi_{k}}\right)_{\rho, T}\left(\frac{\partial \psi_{k}}{\partial \psi_{j}}\right)\left(\frac{\partial a}{\partial \psi_{l}}\right)_{\rho, T}\left(\frac{\partial \psi_{l}}{\partial \psi_{j}}\right)=0 \text { (A.4) }
\end{aligned}
$$
where $\psi_{k}$ and $\psi_{l}$ are the two independent probabilities. The existence of two independent probabilities follows from the two material balance conditions (eqs 29 and 30). The partial derivatives of the independent probabilities with respect to $\psi_{j}$ are obtained from solving eqs 29 and 30 for $\psi_{k}$ and $\psi_{l}$. In addition, from eq 34 we obtain
$$
\left(\frac{\partial a}{\partial \psi_{j}}\right)_{\rho, T}=\delta \sum_{i=1}^{m} \omega_{i}\left[\epsilon_{i}+k T\left(1+\ln \psi_{i}\right)\right] \quad \text { (A.5) }
$$

The Journal of Physical Chemistry, Vol. 95, No. 11, 1991

In one dimension, we choose $\psi_{3}$ and $\psi_{4}$ as independent (see Table I) to obtain
$$
\frac{\psi_{i}}{\psi_{3}}=r^{2-n_{i}} x^{\lambda\left(1-n_{i}\right)} e^{-\epsilon_{i} / k T} ; \quad r=\frac{\psi_{4}}{\psi_{3}} \quad \text { (A.6) }
$$
where $n_{i}, x$, and $\epsilon_{i}$ have already been defined. Then, using eqs 29 and 30
$$
\begin{gathered}
\rho=\psi_{3} \theta \\
1-\rho=\psi_{3} \Phi
\end{gathered} \quad \text { (A.7) }
$$
and, therefore,
$$
\rho(r, T)=\frac{\theta}{\theta+\Phi} \quad \text { (A.8) }
$$
with
$$
\begin{aligned}
& \theta=r^{-1} x^{-(2+\lambda)}+1 / 3\left[4 x^{-(1+\lambda)}+2\right]+r \quad \text { (A.9) } \\
& \Phi=1 / 3\left[2 x^{-(1+\lambda)}+1\right]+2 r+r^{2} x^{\lambda} \quad \text { (A.10) }
\end{aligned}
$$

The analogous equations for the two- and three-dimensional cases, with $\psi_{2}$ and $\psi_{5}$ as independent variables, are
$$
\psi_{i} / \psi_{2}=r^{\left(n_{i}-1\right) / 2} e^{-\epsilon_{i} / k T} x^{(\lambda-2)\left(1-n_{i}\right) / 2} ; \quad r=\psi_{5} / \psi_{2} \quad \text { (A.11) }
$$
$$
\begin{aligned}
& \theta=1+r^{1 / 2}\left(2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right)+3 r+x^{(\lambda / 2-1)} r^{3 / 2} \quad \text { (A.12) } \\
& \Phi=r^{-1 / 2} x^{(\lambda / 2-1)}+3+r^{1 / 2}\left[2 x^{-\lambda / 2}+x^{(1+\lambda / 2)}\right]+r \quad \text { (A.13) } \\
& \rho(r, T)=\frac{\theta}{\theta+\Phi} \quad \text { (A.14) }
\end{aligned}
$$

The equation of state for $M$ molecules in $N$ lattice sites is obtained from the identities
$$
P=-\left(\frac{\partial A}{\partial V}\right)_{T, M}=-N\left(\frac{\partial a}{\partial V}\right)_{T, M}-\frac{a}{v_{0}}=\frac{1}{v_{0}}\left[\rho\left(\frac{\partial a}{\partial \rho}\right)_{T}-a\right]_{\text {(A.15) }}
$$
and the chemical potential, from
$$
\mu=\frac{G}{M}=\frac{A+P V}{M}=\frac{1}{\rho}\left(a+P v_{0}\right)=\left(\frac{\partial a}{\partial \rho}\right)_{T} \quad \text { (A.16) }
$$
where $v_{0}$ is the volume of a unit cell, and $\rho=M / N$. Note that $a$ is related to the Helmholtz energy per molecule $(a')$ by
$$
a=\rho a^{\prime} \quad \text { (A.17) }
$$

The partial derivative in eq A.16 is evaluated as
$$
\left(\frac{\partial a}{\partial \rho}\right)_{T}=\left(\frac{\partial a}{\partial \rho}\right)_{T,\{\psi\}}+\frac{\partial a}{\partial \psi_{k}} \frac{\partial \psi_{k}}{\partial \rho}+\frac{\partial a}{\partial \psi_{l}} \frac{\partial \psi_{l}}{\partial \rho} \quad \text { (A.18) }
$$
where $\{\psi\}$ denotes constancy of all $\psi_{i}$. Equations 35-40 then follow after straightforward, if tedious, algebra. Equations A.8-A.10 yield eq 45; eqs A.12-A.14 yield eq 46.