# Shock Parameters in a Two Component Mixture
*

G. E. DUVALL

Department of Physics, Washington State University
Pullman, Washington 99163

AND

S. M. TAYLOR, JR.

Terminal Ballistics Lab., Ballistic Research Laboratories,
Aberdeen, Md.

(Received February 16, 1971)

## ABSTRACT
A thermodynamically consistent procedure, based on the Gibbs free energy, is described for computing the thermodynamic properties of a mixture in equilibrium at constant pressure and temperature. This is used to compute temperatures, pressures, Grüneisen parameters and sound velocities on the Hugoniot for mixtures of polyethylene and quartz. The results show that a simple mass-weighted average for the Grüneisen parameter is inaccurate and that the mixture of two materials for which $\Gamma/V =$ constant does not itself have a constant value of $\Gamma/V$. Some comments are made on problems of equilibrium of stress and temperature in composite materials.

## I. INTRODUCTION
WE DEFINE A COMPOSITE MATERIAL as one in which the physical properties vary from point to point, usually, but not necessarily, periodically. A lattice of mass points with interacting forces is an example of such a system, and the study of wave propagation in lattices is very old [1]. Sir Isaac Newton studied the propagation of waves in a one-dimensional lattice as substitute for a continuous string. With mathematical tools available to him he found the lumped constant system to be simpler than the continuum. Sir William Hamilton also studied the one-dimensional lattice and found the equivalent of the Schroedinger solution, though it was not so concisely expressed since Bessel functions had not yet been invented. In the latter part of the nineteenth century Lord Baden-Powell and later Lord Kelvin used the

* Part of this material was presented at a Conference on Nuclear Survivability, Air Force Weapons Laboratory, Dec. 3 & 4, 1969. The work was performed under sponsorship of Ballistic Research Laboratories, Contract #DA-04-200-AMC-1702X.

J. COMPOSITE MATERIALS, Vol. 5 (April 1971), p. 130

one-dimensional lattice as a model for the study of optical dispersion.

In modern physical science and technology, problems of x-ray diffraction, electronic, mechanical and thermal properties of solids, E-M antennae design, and even astrophysics all hinge upon the effects of wave propagation in periodic or aperiodic structures or systems.

Problems in the present context vary somewhat from those conventionally associated with lattices because it is not always possible to ignore the details of propagation within the components of the composite material and because problems of finite amplitude waves are often involved. This means that dispersion phenomena which are associated with any lattice become more complicated and that the superposition of multiple disturbances is no longer permitted. In spectral terms this means that propagation velocity depends on both frequency and amplitude and that waves of a single arbitrary frequency cannot be propagated. In such circumstances it is sometimes helpful to consider and attempt to understand a very specific and well-defined simple problem, which may then serve as basis for the understanding of more complicated problems.

For this purpose we consider a half-space of the composite material and suppose that the free surface is subjected to a step-change in pressure or velocity normal to the surface. This state of pressure or velocity at the free surface is maintained indefinitely and we may inquire about the development and structure of the wave front and the equilibrium states in a region long after the wave front has passed.

Simple as this problem is, its complete solution is still very ambitious and we confine ourselves for the present to questions about the equilibrium state, with some remarks about the developing wave front.

## II. EQUILIBRIUM COMPRESSION OF TWO FLUIDS

A. B. Wood many years ago considered a composite system consisting of small gas bubbles dispersed in water [2]. He argued that at low frequencies there should be local equilibrium of temperature and pressure amongst gas bubbles and water, that each should assume a volume appropriate to that pressure and temperature, and that the derivative of the resulting pressure-volume relation would accordingly give the sound velocity. To a first approximation the water could be assumed rigid; then the sound velocity is

$$
c \simeq\left(P / \rho_{o} R\right)(1+R) \tag{1}
$$

where $P$ is ambient pressure, $\rho_{o}=$ density of water and $R$ is the volume ratio of gas to water at pressure $P$ and temperature $T$.

As would be expected, sound velocities predicted by Equation (1) can be very low, as little as a few meters/second. Equation (1) has a broad minimum at $R=1$ with $c=10$ meters/sec when $P=1$ bar, with $c$ rising


![](./images/812013299733364737_1.jpg)

Figure 1. Velocity of sound in water containing air bubbles, reference 3, H. B. Karplus.

steeply for both large and small $R$ (Figure 1). H. B. Karplus, in work re- ported about ten years ago, refined Wood's model and tested it experi- mentally for a considerable range of parameters [3,4]. His results are sum- marized in Figure 1, taken from refer- ence [3]. The frequencies at which measurements were made were less than $10 \%$ of the mean resonant fre quency of the bubbles, and he con- cluded that there was no significant frequency dispersion.

The principles on which Wood's model are based are well founded and can be extended to other materials. Sufficiently far behind a shock front, we expect stress and temperature equilib- rium to exist for any mixture of materi- als. If the materials be liquid, this re- duces to equilibrium in $P$ and $T$ . In either liquid or solid case the thermodynamics of compression are appropri- ately described by the Gibbs functions of the two components and of the mixture. If interfacial energies are negligible, we can disregard the sizes and shapes of the components and consider only their mass fractions. Let $\lambda$ be the mass fraction of component 2 and $1-\lambda$ that of component 1. Then the Gibbs function for unit mass of the mixture is

$$
G=(1-\lambda) G_{1}+\lambda G_{2} \quad(2)
$$

where subscripts "1" and "2" refer to the two components. Other thermo- dynamic functions are obtained as derivatives of Equation (2):

specific volume:
$$
\begin{aligned}
V & =(\partial G / \partial P)_{T} \equiv G_{P} & & (3) \\
& =(1-\lambda) V_{1}+\lambda V_{2} & & (4)
\end{aligned}
$$

specific entropy:
$$
\begin{aligned}
S & =-(\partial G / \partial T)_{P} \equiv-G_{T} & & (5) \\
& =(1-\lambda) S_{1}+\lambda S_{2} & & (6)
\end{aligned}
$$

isothermal compressibility:
$$
\beta=-(1 / V)(\partial V / \partial P)_{T}=-G_{P P} / V \quad(7)
$$

$$\beta V=(1-\lambda) \beta_{1} V_{1}+\lambda \beta_{2} V_{2} \tag{8}$$

thermal expansion coefficient:
$$\alpha=(1 / V)(\partial V / \partial T)_{P}=G_{P T} / V \tag{9}$$

$$\alpha V=(1-\lambda) \alpha_{1} V_{1}+\lambda \alpha_{2} V_{2} \tag{10}$$

specific heat at constant pressure:
$$C_{P}=T(\partial S / \partial T)_{P}=-T G_{T T} \tag{11}$$

$$C_{P}=(1-\lambda) C_{P 1}+\lambda C_{P 2} \tag{12}$$

$G$ and its derivatives are assumed to be continuous, so the definitions in Equations (7), (9) and (11) lead to the following identities, which can be of use in evaluating experimental data:
$$G_{P P T}=-(\partial \beta V / \partial T)_{P}=(\partial \alpha V / \partial P)_{T} \tag{13}$$

$$G_{T T P}=-(1 / T)\left(\partial C_{P} / \partial P\right)_{T}=(\partial(\alpha V) / \partial T)_{P} \tag{14}$$

In the application of Equations (2)-(12), we assume the thermodynamic properties of the two components to be known. These equations provide procedures for computing properties of the mixture.

If the compression front envisioned in this problem ever achieves what can be described as a steady profile, then the jump conditions can be applied to relate the equilibrium state behind the front to that ahead. The thermo- dynamics of compression are then summarized in the Rankine-Hugoniot Equation,
$$E=E_{o}+(1 / 2)\left(P+P_{o}\right)\left(V_{o}-V\right), \tag{15}$$
and in the first and second laws of thermodynamics. Differentiating Equation (15), we have
$$d E=(1 / 2)\left(V_{o}-V\right) d P-(1 / 2)\left(P+P_{o}\right) d V=T d S-P d V$$
or
$$T d S=(1 / 2)\left(V_{o}-V\right) d P+(1 / 2)\left(P-P_{o}\right) d V \tag{16}$$

Expressing both $V$ and $S$ in terms of $P$ and $T$, as in Equations (3) and (5), we obtain for the equation of the Hugoniot in the $T, P$ plane:
$$d T=d P\left[\left(V_{o}-V\right)-\beta V\left(P-P_{o}\right)+T \alpha V\right] /\left[2 C_{P}-\alpha V\left(P-P_{o}\right)\right] \quad(17)$$

Integration of Equation (17) makes it possible to evaluate any thermo- dynamic parameter in the equilibrium compressed state, provided $G_{1}(P, T)$, $G_{2}(P, T)$ and $\lambda$ are known.

The Gruneisen parameter $\Gamma$ and sound velocity $c$ are readily obtained from the above expressions. From the definition of sound velocity:
$$c^{2}=-V^{2}(\partial P / \partial V)_{S}=-V^{2} /\left((\partial V / \partial P)_{S}\right), \tag{18}$$

$$
\begin{aligned}
(\partial V / \partial P)_{S} & =(\partial V / \partial P)_{T}+\alpha V(\partial T / \partial P)_{S} \\
& =-\beta V+T \alpha^{2} V^{2} / C_{P}
\end{aligned}
\tag{19}
$$

Substituting (19) into (18) yields
$$
c^{2}=V^{2} /\left(\beta V-T \alpha^{2} V^{2} / C_{P}\right)
\tag{20}
$$

The Gruneisen parameter is calculated in similar fashion:
$$
\Gamma=\left(V / C_{V}\right)(\partial P / \partial T)_{V}=V \alpha / C_{V} \beta
\tag{21}
$$

Since
$$
C_{V}=C_{P}-\alpha^{2} V T / \beta,
$$

Equation (21) becomes
$$
\Gamma=\alpha V^{2} /\left(\beta V C_{P}-\alpha^{2} V^{2} T\right)
\tag{22}
$$

In computing $c$ and $\Gamma$ for the mixture, $V$, $\alpha V$, $\beta V$ and $C_{P}$ are to be deter- mined from Equations (4), (8), (10) and (12), then substituted in Equa- tions (20) and (22).

In illustrating the above relations and procedures, we would like to say that we had created Gibbs functions for two substances which were con- sistent with all available experimental data and had all of the proper limiting behavior. Unfortunately we can't. What we have done is to create rather conventional descriptions of a quartz-like material and a polyethylene-like material and to use these to illustrate the effects of varying $\lambda$ on the above parameters. The following assumptions were made for each material:
$$
P_{i}(V, T)=P_{i}\left(V, T_{o}\right)+b_{i} C_{V i}\left(T-T_{o}\right), \quad i=1,2
\tag{23}
$$

$$
C_{V i}=\text { constant }
\tag{24}
$$

$$
b_{i}=\Gamma_{i} / V_{i}=\text { constant }
\tag{25}
$$

$$
P_{i}\left(V, T_{o}\right)=\frac{1}{\gamma_{i o} \beta_{i o}}\left[\left(\frac{V_{i o}}{V_{i}}\right)^{\gamma_{i o}}-1\right]
\tag{26}
$$

$$
T_{o}=293^{\circ} \mathrm{K}.
$$

The following constants were used:

<table>
  <thead>
    <tr>
      <th><i>i</i></th>
      <th>Polyethylene<br>1</th>
      <th>Quartz<br>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>b<sub>i</sub></i>, g/cc</td>
      <td>.3887</td>
      <td>.7832</td>
    </tr>
    <tr>
      <td><i>C<sub>Vi</sub></i>, Mbcc/g<sup>o</sup></td>
      <td>$1.436\times10^{-5}$</td>
      <td>$.56\times10^{-5}$</td>
    </tr>
    <tr>
      <td><i>V<sub>io</sub></i>, cc/g</td>
      <td>1.035</td>
      <td>.378</td>
    </tr>
    <tr>
      <td><i>γ<sub>io</sub></i></td>
      <td>10.2</td>
      <td>5.58</td>
    </tr>
    <tr>
      <td><i>β<sub>io</sub></i>, Mb<sup>-1</sup></td>
      <td>19.31</td>
      <td>2.70</td>
    </tr>
  </tbody>
</table>

![](./images/812013299733364737_2.jpg)

The results of computations are shown in Figures 2-6. Most are not particularly remarkable. Figure 2 shows that temperature along the Hugoniot increases at a greater-than-linear rate when polyethylene is added to quartz, and that the rate of change of temperature decreases as the amount of polyethylene increases. This is the kind of effect to be expected when a compressible material is added to a relatively incompressible one. Figure 3 shows only that volume is but little affected by temperature changes on the Hugoniot, again as expected. In Figure 4 the Gruneisen parameter, computed from Equation (22), is compared for $\lambda=0.50$ with a simple mass-weighted average:

$$
\Gamma=(1-\lambda) \Gamma_{1}+\lambda \Gamma_{2} \tag{27}
$$

Figure 5 shows perhaps the most interesting result. Although $\Gamma / V$ is assumed constant for each component, the resultant for the mixture is quite strongly volume dependent; the mass weighted average values differ appreciably from the correct values. Sound velocities, shown in Figure 6, change almost linearly with $\lambda$.

The influence of varying $\Gamma$ on the stress field has been the subject of extensive debate. It seems fairly certain that in some circumstances it can have a substantial effect. For that reason it is most appropriately calculated by the procedure given here when equilibrium conditions are expected. If they are not, it is of no significance anyway.

![](./images/812013299733364737_3.jpg)

Figure 3. Pressures and volumes on the Hugoniots of mixtures of quartz and polyethylene.

![](./images/812013299733364737_4.jpg)

Figure 4. Grüneisen parameters for mixtures of quartz and polyethylene.

![](./images/812013299733364737_5.jpg)

Figure 5. $\Gamma/V$ for mixtures of quartz and polyethylene.

![](./images/812013299733364737_6.jpg)

Figure 6. Sound velocities on the Hugoniot for mixtures of quartz and polyethylene.

### III. DEVIATIONS FROM EQUILIBRIUM

When a compression front passes over a mixture of two materials there will be an initial period in which stress equilibrium is being established. The duration of this period will be the order of several times the larger of the two numbers $l_i/c_i, i=1,2$, where $l$ and $c$ are characteristic dimension and sound velocity of the two components respectively. As a result of compression, each component will experience a temperature rise determined by the stress field and by its own material properties. Roughly speaking, when stress equilibrium has been established, temperatures $T_1$ and $T_2$ will exist in two components. Neglecting convection and radiation, which will accelerate the process, these two temperatures will be equalized in a time the order of several times the larger of the two numbers $C_{i}\rho_{i}l_{i}^{2}/k_{i}, i=1,2$ where $C_{i}, \rho_{i}, l_{i}$, $k_i$ are specific heat, density, dimension and thermal conductivity of the $i$th component, respectively. The time required for thermal equilibration is normally much greater than that required for stress equilibration. The ratio of the former time to the latter is the order of $l/\Lambda$, where $\Lambda$ is the scattering mean free path for phonons. $\Lambda$ may range from a single lattice cell diameter in a disordered structure to the size of a grain in a highly ordered structure.

In many real and experimental situations, thermal equilibrium will not be reached. Fortunately wave propagation is sometimes insensitive to thermal effects, unless they produce phase transitions or chemical reactions. In any exceptional cases which must be treated, the effects can be bounded by assuming isothermal compression on the one hand and adiabatic on the other.

For inert, fixed inhomogeneities, stress equilibration time will usually be a reliable guide to the conditions required for establishment of equilibrium. If the inhomogeneities are not inert or are not fixed, a new set of rules applies. The most notable example is in effect of dislocations on precursor decay [5]. The mechanics of any such case must be examined in detail in order to make an estimate of equilibration time. Another practical example of such a case is that of a granular material in which small grains may slide over one another under the influence of shear forces and friction. A similar effect occurs when the components of a laminar composite are shocked with sufficient force to produce debonding. The consequences of this have been discussed by Tsou and Chou [6] and by Ben-Amoz [7].

It is not likely, in fact, that real composites will behave very much as described in Section II. The principal values of such a computation lie in the specifying of a bound on composite behavior and in suggesting the proper averaging procedures for determining mean bulk properties of such materials on a rather gross scale.

### NOMENCLATURE

$c$ = Sound velocity

$P$ = Pressure
$\rho$ = Density
$R$ = Volume ratio of two components
$T$ = Temperature, $^\circ$K
$G$ = Gibbs function
$\lambda$ = Mass fraction of second component
$V$ = Volume per unit mass
$S$ = Entropy per unit mass
$\beta$ = Isothermal compressibility
$\alpha$ = Thermal expansion coefficient at constant pressure
$C_P$ = Specific heat at constant pressure
$E$ = Internal energy per unit mass
$\Gamma$ = Grüneisen parameter
$C_V$ = Specific heat at constant volume
$b$ = $\Gamma/V$

Subscript "o" refers to conditions at $293^\circ$K, 1 atmosphere
Subscripts "1" and "2" refer to the two components of a mixture

## REFERENCES

1. A brief historical review of the lattice problem is given by Léon Brillouin and Maurice Parode in *Propagation des Ondes dan Les Milieux Périodiques*, Dunod, Paris, (1956).

2. A. B. Wood, *A Textbook of Sound*, McMillan (1930), p. 328.

3. H. B. Karplus, "The Velocity of Sound in a Liquid Containing Gas Bubbles," AEC Res. & Dev. Report C00-248, (TID-4500, 13th Ed. Rev.) UC-80, Special Distribution (1958).

4. H. B. Karplus, "An Analytical Study of the Propagation of Pressure Waves in Liquid Hydrogen-Vapor Mixtures," NASA CR 45015, IITRI N6054-6 (1964).

5. J. N. Johnson, O. E. Jones and T. E. Michaels, "Dislocation Dynamics and Single-Crystal Constitutive Relations: Shock-Wave Propagation and Precursor Decay," *J. Appl. Phys.*, Vol. 41, #6, (May 1970), p. 2330.

6. F. K. Tsou and P. C. Chou, "Analytical Study of Hugoniot in Uni-Directional Fiber Reinforced Composites," *J. Composite Materials*, Vol. 3 (1969), p. 500.

7. M. Ben-Amoz, "Investigation of Shock Propagation in Fibre-Reinforced Materials," to be published in the *Journal of the Mechanics and Physics of Solids*.

139