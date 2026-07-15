![](./images/812417706333569027_1.jpg)

# A new Monte Carlo method for calculating surface tension

J. Miyazaki, J. A. Barker, and G. M. Pound

Citation: J. Chem. Phys. 64, 3364 (1976); doi: 10.1063/1.432627
View online: http://dx.doi.org/10.1063/1.432627
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v64/i8
Published by the American Institute of Physics.

---

Additional information on J. Chem. Phys.
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/812417706333569027_2.jpg)

# A new Monte Carlo method for calculating surface tension
J. Miyazaki* and J. A. Barker
IBM Research Laboratory, San Jose, California 95193

G. M. Pound
Department of Materials Science and Engineering, Stanford, California 94305
(Received 24 November 1975)

A new Monte Carlo method for calculating the surface tension of a liquid is described. The method is based on a direct evaluation of the free energy required to create a surface, unlike earlier Monte Carlo calculations which evaluated the surface stress. It is applied to the 6:12 fluid in conditions close to the triple point for argon. The calculated surface tension agrees within statistical uncertainty with previous Monte Carlo estimates, but the statistical uncertainty of the present method is much lower. Agreement with experimental data for argon is not good, as should be expected; estimates of the effects of using a correct pair potential and particularly of including three-body interactions indicate that they would lead to good agreement.

## I. INTRODUCTION

The surface tension of a liquid can be defined either as the surface excess tangential stress, or as $\partial F_{e} / \partial S$, where $F_{e}$ is the surface excess Helmholtz free energy and $S$ the surface area, or as $F_{e} / S$. Kirkwood and $Buff^{1}$ derived microscopic expressions for $\gamma$ based on the first definition, and $Buff^{2}$ showed that the second definition leads to the same result. The equivalence of the second and third definitions is based on the extensivity of surface properties and was known to Gibbs. Modern theories of surface tension have been based either on the first (mechanical) definition, following Kirkwood and Buff, $^{1}$ or, following van der Waals, on the third definition. A recent convenient comparison of these approaches is given by Lovett et al. $^{3}$ A review of quasithermodynamic methods useful near the critical point is given by Widom. $^{4}$

In the perturbation approach $^{5}$ the surface tension is obtained from an excess free energy calculation, in which the constancy of the chemical potential across the liquid-vapor interface is employed to determine the equilibrium density profile. Toxvaerd $^{5}$ extended the Barker-Henderson perturbation theory $^{6}$ for a nonuniform liquid and derived the expression for the Helmholtz free energy per molecule near the transition zone. The surface tension is calculated by minimizing the free energy in the surface layer.

The surface tension at the triple point is of great interest and it has been obtained by various workers based on the Kirkwood-Buff and the perturbation models. The Toxvaerd perturbation theory is a useful approach to the surface tension calculation, and it gives an excellent qualitative agreement with experiment. However, this theory involves several approximations whose validity may be somewhat uncertain, particularly at lower temperatures.

In principle, the most reliable method for calculation of surface tension is computer simulation via Monte Carlo or molecular dynamics methods. Lee et al. $^{7}$ carried out a Monte Carlo calculation in which the surface tension was calculated using the mechanical expression for the surface stress,

$$
\gamma=\frac{1}{S}\left\langle\sum_{i>j} \sum \frac{\left(x_{i j}^{2}-z_{i j}^{2}\right)}{r_{i j}} u^{\prime}\left(r_{i j}\right)\right\rangle_{0}, \tag{1}
$$

where $r_{i j}$ is the distance between $i$ th and $j$ th molecules, $\langle\rangle$ denotes canonical average, and

$$
u^{\prime}\left(r_{i j}\right)=\frac{d u\left(r_{i j}\right)}{d r_{i j}}, \quad x_{i j}=x_{i}-x_{j}, \quad z_{i j}=z_{i}-z_{j},
$$

while $u(r_{i j})$ is the pair potential. Unfortunately, this quantity fluctuates over a wide range, so that the statistical uncertainty in the result obtained with Monte Carlo runs of reasonable length is rather high.

In this paper, we present a new Monte Carlo method in which the free energy required to create reversibly a surface (actually two surfaces) in a bulk liquid is calculated directly. For a single component liquid the surface Helmholtz free energy and surface tension are identical; however, it turns out that the surface free energy can be estimated with less statistical uncertainty and therefore higher accuracy than the surface stress.

The creation of free surfaces in the Monte Carlo calculation is carried out basically in two stages. Starting with a bulk liquid with periodic boundary conditions, the system is separated by steps into a set of slabs, each contained between hard walls. The free energy change for the first stage is calculated by a direct method proposed by Bennett, $^{8}$ in which the free energy difference between two systems is calculated from the average acceptance probability of a Monte Carlo move. In the second stage the hard walls are moved outward so that the surface relaxes to a free surface; the free energy change for this process is evaluated by integrating the derivatives of the free energy with respect to the position of the wall, which can be evaluated directly from the density at the wall.

## II. CREATING THE SURFACE

Our objective is to start with a bulk liquid (with periodic boundary conditions) and to change this reversibly into a set of slabs of liquid, initially contained between hard walls (which are afterwards relaxed). To this end, we consider a set of $N$ molecules constrained

to lie in a box of dimensions $L_x$, $L_y$, and $L_z$. We consider a modified form of periodic boundary condition which is most simply described by writing an expression for the total potential energy $U$ of the system;

$$
\begin{aligned}
U &= \sum_{i<j=1}^{N} \sum_{l, m, n=-1}^{1} u\left\{\left[\left(x_{i}-x_{j}+l L_{x}\right)^{2}\right.\right. \\
&\left.\left.+\left(y_{i}-y_{j}+m L_{y}\right)^{2}+\left(z_{i}-z_{j}+n L_{z}+n \Delta\right)^{2}\right]^{1 / 2}\right\}.
\end{aligned}
$$

Here $u(r)$ is the pair potential function for which we use the 6:12 form. The terms with $l$, $m$, $n \neq 0$ in (2) correspond to interactions of the molecules in the central box with those in periodic image boxes. Actually, we truncated the potential at a finite range (and added corrections for the long-range part). The effect of this is that the nonzero terms in (2) are exactly those permitted by the usual "nearest neighbor image convention."

Thus, if the parameter $\Delta$ (which represents the separation between our slabs) is zero, we have exactly the usual representation of a bulk liquid with periodic boundary conditions. However, when $\Delta$ is nonzero, we have a set of interacting slabs of liquid, each contained between hard but "transparent" walls spaced by $L_z$; the distance between the walls for adjacent slabs is $\Delta$. By transparent, we mean that the molecular interactions are felt through the walls from one slab to the next; this is necessary so that for $\Delta=0$ we retain the bulk liquid behavior. When $\Delta$ becomes larger than the range of the truncated potential, the slabs are noninteracting, but constrained between hard walls at spacing $L_z$ (since we impose the condition that the molecules remain within the box). For this stage of the calculation we need to calculate the change of free energy as $\Delta$ varies from 0 to the range of the truncated potential; this is done by the method of Bennett.

In the second major stage of the calculation, performed on a single slab, we move the hard walls at $z=0$ and $L_z$ outwards symmetrically by steps, equilibrating and estimating the density $\rho_w$ at the wall at each step. The pressure on the wall is $\rho_w kT$, and this determines the derivative of the free energy with respect to the distance between the walls. By integrating this out to a distance large enough so that the density at the wall is negligible (at the temperature we used, the bulk vapor density is negligible in this sense), we found the free energy difference between the slab constrained by hard walls and the unconstrained slab held together by its own cohesion.

### III. DIRECT METHOD FOR FREE ENERGY CALCULATION

The Monte Carlo method⁹ has been commonly used to study the mechanical quantities of a classical thermodynamic system such as the pressure or potential energy of a system. Statistical quantities such as the free energy or entropy cannot be obtained directly from the Monte Carlo calculations, since these quantities cannot be expressed as ensemble averages.

Recently, Bennett derived an equation which relates the acceptance ratio of an ordinary Monte Carlo move to the Helmholtz free energy difference.

For the canonical ensemble system, the Helmholtz free energy of the system is determined by its configurational integral $Q$:

$$
Q=\int \cdots \int e^{-U\left(x_{1} \cdots z_{N}\right) / k T} d x_{1} \cdots d z_{N}.
$$

Let $Q_0$ be the configurational integral defined for a reference state (state 0) with $N$ particles and the total potential energy $U_0$ and temperature $T$. Similarly, let $Q_1$ be the configurational integral for state 1 with $N$, $U_1$, and $T$. In our example, $U_0$ and $U_1$ will refer to the potential function of Eq. (2), with two different values of $\Delta$, say $\Delta_0$ and $\Delta_1$. The formula for $Q_1/Q_0$ in terms of canonical averages of the acceptance probability for a Monte Carlo move can be derived by using the Metropolis function $M(x)=\min\{1, \exp(-x)\}$. The Metropolis function is commonly used in the ordinary Monte Carlo method to assign a Boltzmann weighted acceptance probability to the trial move of a particle. Since this function has the property $M(x)/M(-x)=\exp(-x)$, we have

$$
M\left(U_{1}^{*}-U_{0}^{*}\right) \exp \left(-U_{0}^{*}\right)=M\left(U_{0}^{*}-U_{1}^{*}\right) \exp \left(-U_{1}^{*}\right),
$$

where
$U_{0}^{*}=U_{0}/kT$ and $U_{1}^{*}=U_{1}/kT$.

Integrating Eq. (4) over all configuration space and multiplying by $Q_0/Q_0$ and $Q_1/Q_1$ gives

$$
\begin{aligned}
& Q_{0} \frac{\int \cdots \int M\left(U_{1}^{*}-U_{0}^{*}\right) \exp \left(-U_{0}^{*}\right) d x_{1} \cdots d z_{N}}{Q_{0}} \\
& \quad=Q_{1} \frac{\int \cdots \int M\left(U_{0}^{*}-U_{1}^{*}\right) \exp \left(-U_{1}^{*}\right) d x_{1} \cdots d z_{N}}{Q_{1}}.
\end{aligned}
$$

This equation is expressed in terms of canonical averages which can be obtained during Monte Carlo runs:

$$
\frac{Q_{1}}{Q_{0}}=\frac{\left\langle M\left(U_{1}^{*}-U_{0}^{*}\right)\right\rangle_{0}}{\left\langle M\left(U_{0}^{*}-U_{1}^{*}\right)\right\rangle_{1}},
$$

where $\langle\,\rangle_0$ and $\langle\,\rangle_1$ denote canonical averages taken with potentials $U_{0}^{*}$ and $U_{1}^{*}$, respectively. The numerator is considered to be the average acceptance probability for the move from $U_{0}^{*}$ and $U_{1}^{*}$. Similarly, the denominator is the average acceptance probability for the move from $U_{1}^{*}$ to $U_{0}^{*}$.

In Eq. (6), if one of the acceptance probabilities is too low to be measured with considerable accuracy, this can be increased by compensating the other term by shifting the origin of the potential energy. If both of the terms are too low, there is insufficient overlap of the energy states between $U_{0}^{*}$ and $U_{1}^{*}$, and an intermediate state is required. Also, Bennett⁸ showed that an estimate with smaller uncertainty can be obtained by replacing the Metropolis function by the Fermi function; we quote his final result:

$$
\frac{Q_{1}}{Q_{0}}=\frac{\left\langle f\left(U_{1}^{*}-U_{0}^{*}+C\right)\right\rangle_{0}}{\left\langle f\left(U_{0}^{*}-U_{1}^{*}-C\right)\right\rangle_{1}} \exp (C),
$$

where $f$ is the Fermi function $[f(x)=1/(1+e^{x})]$. The value for $Q_1/Q_0$ is obtained by choosing the appropriate $C$ so as to make $\langle f(U_{1}^{*}-U_{0}^{*}+C)\rangle_{0}$ equal to $\langle f(U_{0}^{*}-U_{1}^{*}-C)\rangle_{1}$. For the optimum $C$ value, the Helmholtz free

energy difference between two states is expressed as

$$
\Delta F=-k T \ln \left(Q_{1} / Q_{0}\right)=-k T C. \tag{8}
$$

Thus, the Helmholtz free energy difference is obtained by performing two independent Monte Carlo runs.

### IV. SURFACE TENSION CALCULATION

As a simulation model, two cubic boxes each containing 108 molecules are combined to form a rectangular box with 216 molecules, and periodic boundary conditions are imposed for the $x$, $y$, and $z$ directions to make an infinitely large bulk liquid; the periodic length in the $z$ direction is twice that in $x$ and $y$ directions. The molecules in the system interact in pairs according to the Lennard-Jones $12:6$ potential

$$
u(r)=4 \epsilon\left[(\sigma / r)^{12}-(\sigma / r)^{6}\right], \tag{9}
$$

where $r$ is the intermolecular separation, $\sigma$ is the separation at the zero of the pair potential, and $\epsilon$ is the depth of the potential well. In describing the properties of this model, the reduced temperature $T^*(=kT/\epsilon)$ and reduced density $\rho^*(=N\sigma^3/V)$ are employed.

The entire procedure of this surface calculation is divided into several steps. Initially, we start from the bulk liquid and the liquid is gradually separated in the $z$ direction to form surfaces. The surfaces are normal to the $z$ axis, and periodic boundary conditions are still imposed in $x$- and $y$ directions in the separation process to make an infinitely large slab. The system with 216 molecules is taken through several steps from the bulk state to the final state with two free surfaces. These steps are listed below:

(a) the bulk liquid (reference state);
(b) the bulk liquid using truncated potential $(R_{\text{max}} = 2.5\sigma)$;
(c) the slab shaped liquid with two hard walls using truncated potential;
(d) the slab shaped liquid with two hard walls using "nearly" nontruncated potential $(R_{\text{max}} = 5.0\sigma)$;
(e) the slab shaped liquid with two free surfaces using "nearly" nontruncated potential;
(f) the slab shaped liquid with two free surfaces using nontruncated potential.

The cut-off distance $R_{\text{max}}$ of the potential function used in the separation process is $2.5\sigma$, which is a little less than half the edge of the cubic box with 108 molecules. The nearly nontruncated potential means that the cut-off distance is large enough so that the effect of the tail of the potential function is almost negligible. This nearly nontruncated potential is used in the relaxation process of the hard walls to minimize the effect of the potential tail. The surface tension and excess internal energy are obtained as the free energy and potential energy differences per unit surface area between state (a) and (f). The direct method is applied for estimating the Helmholtz free energy difference between states (b) and (c), and also between (c) and (d). The free energy difference between (d) and (e) is due to the surface relaxation and is calculated from the density data at the walls during the relaxation process.

The bulk liquid with reduced density 0.85 at the reduced temperature 0.7 is chosen as a reference state. This liquid is almost at the triple point and shows nearly zero pressure from the Monte Carlo calculation which includes a long range correction.

Since we adopt the truncated L-J $12:6$ potential during the Monte Carlo calculation for the slab separation, the free energy difference between the bulk state using a nontruncated potential [state (a)] and the bulk state using a truncated potential [state (b)] must be considered. Both states are bulk liquid, and the free energy difference is assumed to be equal to the potential energy difference in a uniform liquid. This potential energy difference is the same as the long-range correction for the tail of the potential function, and it can be estimated by the numerical integration of the tail of the L-J potential function assuming a uniform radial distribution function beyond $R_{\text{max}}$:

$$
\Delta F=\Delta U=\frac{N \rho}{2} \int_{R_{\text{max}}}^{\infty} u(r) 4 \pi r^{2} d r. \tag{10}
$$

The obtained free energy difference $F_b - F_a$ is $96.72\epsilon$ for the system.

In the separation process, the direct method is applied to the free energy difference calculation by using the Monte Carlo method. In order to make a surface, the bulk liquid is separated gradually using the slab shaped liquid model and the free energy difference is calculated by varying the slab separation $\Delta$. The interaction between two slabs disappears when the slab separation becomes larger than the cut-off distance $2.5\sigma$, and at this stage the slabs are separated.

In this free energy difference calculation due to slab separation we adopt 17 intermediate states from the bulk state to the completely separated state and 200 000 configurations are called for each calculation. In this process, the surfaces of the slab are not relaxed, that is, the molecules are not allowed to pass through the "wall" at $z=0$ and $L_z$. The $C$ values obtained for each step and their standard errors are shown in Table I.

The change in separation length at each step must be small to avoid a large error, especially at small separations, because the steep region of the potential function plays a major role in calculating average Fermi functions. At large separations, the error is small compared with the $C$ value. These $C$ values are obtained independently and the standard error for the total $C$ value is $1.3\%$. The cumulative free energy change due to the slab separation process is shown in Fig. 1. The rate of free energy change becomes a maximum around $\Delta=0.8\sigma$, and it decreases rapidly beyond $\Delta=1.2\sigma$. The calculated free energy difference is $55.73\epsilon$ for the system. This free energy difference depends on the cut-off distance and is expected to increase with increasing $R_{\text{max}}$. The potential tail has a large influence on this free energy calculation due to slab separa-

<table>
<caption>TABLE I. $C$ value at each separation process and its standard error.</caption>
<thead>
<tr>
<th colspan="2">Separation $\Delta(\sigma)$</th>
<th rowspan="2">$C$</th>
<th rowspan="2">Standard error of $C$ value</th>
</tr>
<tr>
<th>From</th>
<th>To</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0.05</td>
<td>$-0.19$</td>
<td>0.23</td>
</tr>
<tr>
<td>0.05</td>
<td>0.1</td>
<td>$-0.21$</td>
<td>0.24</td>
</tr>
<tr>
<td>0.1</td>
<td>0.15</td>
<td>$-1.12$</td>
<td>0.21</td>
</tr>
<tr>
<td>0.15</td>
<td>0.2</td>
<td>$-1.27$</td>
<td>0.23</td>
</tr>
<tr>
<td>0.2</td>
<td>0.25</td>
<td>$-1.72$</td>
<td>0.18</td>
</tr>
<tr>
<td>0.25</td>
<td>0.30</td>
<td>$-1.66$</td>
<td>0.21</td>
</tr>
<tr>
<td>0.30</td>
<td>0.35</td>
<td>$-1.66$</td>
<td>0.22</td>
</tr>
<tr>
<td>0.35</td>
<td>0.4</td>
<td>$-2.02$</td>
<td>0.18</td>
</tr>
<tr>
<td>0.4</td>
<td>0.45</td>
<td>$-2.83$</td>
<td>0.17</td>
</tr>
<tr>
<td>0.45</td>
<td>0.5</td>
<td>$-2.73$</td>
<td>0.20</td>
</tr>
<tr>
<td>0.5</td>
<td>0.55</td>
<td>$-3.12$</td>
<td>0.14</td>
</tr>
<tr>
<td>0.55</td>
<td>0.6</td>
<td>$-3.56$</td>
<td>0.18</td>
</tr>
<tr>
<td>0.6</td>
<td>0.7</td>
<td>$-6.35$</td>
<td>0.51</td>
</tr>
<tr>
<td>0.7</td>
<td>0.8</td>
<td>$-9.68$</td>
<td>0.28</td>
</tr>
<tr>
<td>0.8</td>
<td>0.9</td>
<td>$-10.71$</td>
<td>0.19</td>
</tr>
<tr>
<td>0.9</td>
<td>1.0</td>
<td>$-9.69$</td>
<td>0.12</td>
</tr>
<tr>
<td>1.0</td>
<td>1.2</td>
<td>$-13.92$</td>
<td>0.26</td>
</tr>
<tr>
<td>1.2</td>
<td>3.0</td>
<td>$-7.17$</td>
<td>0.37</td>
</tr>
</tbody>
</table>

tion. This correction can also be made by using the direct method.

Throughout the separation process, the truncated potential is used and the long-range correction for the potential function must be taken into account in order to calculate the free energy difference between states (c) and (d). In the completely separated state, the free energy difference is not equal to the long-range correction term of the potential energy, because the density profiles in states (c) and (d) differ owing to the tail of the potential function and the rigid surfaces. The free energy difference is calculated again using the direct method. In this case, the state 0 is the system using truncated potential and the state 1 is the system using the nearly nontruncated potential. The free energy difference is calculated by increasing and decreasing the cut-off distance of the potential function. The obtained free energy difference $F_{d}-F_{c}$ is $69.69 \epsilon$, and the error is less than $0.3 \%$ and therefore negligible.

The slab shaped liquid has two unrelaxed surfaces and there is a density discontinuity at the liquid-vapor interfaces (walls). In our study the effect of the transition zone is estimated by relaxing the surfaces. The surfaces are relaxed in the direction of $z$, gradually taking out the restriction on the two surfaces with the center of the slab fixed at $z=0.5 L_{z}$. The thickness of the slab is initially $L_{z}$ and the relaxation effect is expressed as a function of $t_{1}$ and $t_{2}$, the values of the $z$ coordinate at which the walls are located (initially $L_{z}$ and 0).

Throughout this relaxation process, the density in the central region of the slab is maintained equal to 0.85 in order to have a bulk liquid whose thermodynamic properties are the same as the initial bulk liquid. This condition is attained by increasing the cut-off distance of the potential function to $5.0 \sigma$. Actually, the density in the bulk region of the slab is around 0.85 during the relaxation process and the Gibbs dividing surface is maintained at the same position.

The configurational integral of this system is expressed as

$$
Q=\int \cdots \int e^{-U / k T} \prod_{i}\left\{H\left(t_{1}-z_{i}\right) H\left(z_{i}-t_{2}\right)\right\} d x_{1} \cdots d z_{N},
$$

where $H(x)$ is the Heaviside step function which is 0 for $x<0$ and 1 for $x>0$; the derivative of $H(x)$ is the Dirac delta function, $\delta(x)$.

Taking the logarithm of this configurational integral and differentiating with respect to $t_{1}$, we have

$$
\frac{\partial \ln Q}{\partial t_{1}}=\frac{\int \cdots \int\left(\sum\left[\delta\left(t_{1}-z_{i}\right) / H\left(t_{1}-z_{i}\right)\right]\right) e^{-U / k T} \prod_{i}\left[H\left(t_{1}-z_{i}\right) H\left(z_{i}-t_{2}\right)\right] d x_{1} \cdots d z_{N}}{\int \cdots \int e^{-U / k T} \prod_{i}\left[H\left(t_{1}-z_{i}\right) H\left(z_{i}-t_{2}\right)\right] d x_{1} \cdots d z_{N}}.
$$

At $z=t_{1}-0, H\left(t_{1}-z_{i}\right)$ is equal to unity, and this equation can be expressed in terms of the canonical average,

$$
\frac{\partial \ln Q}{\partial t_{1}}=\left\langle\sum \delta\left(t_{1}-z_{i}\right)\right\rangle.
$$

Let $Q_{0}$ and $Q_{1}$ be the configurational integrals for the system before and after relaxation of one surface, respectively.

Integrating Eq. (13),

$$
\int_{L_{z}}^{\infty} \frac{\partial \ln Q}{\partial t_{1}} d t_{1}=\int_{L_{z}}^{\infty}\left\langle\sum \delta\left(t_{1}-Z_{1}\right)\right\rangle d t_{1}.
$$

The free energy difference due to the relaxation per surface is

$$
\begin{aligned}
\Delta F & =-k T \ln \left(Q_{1} / Q_{0}\right) \\
& =-k T \int_{L_{z}}^{\infty}\left\langle\sum \delta\left(t_{1}-z_{i}\right)\right\rangle d t_{1}.
\end{aligned}
$$

The canonical average $\left\langle\sum \delta\left(t_{1}-z_{i}\right)\right\rangle$ can be obtained from the ordinary Monte Carlo calculations by extrapolating the density data near the surface. In this calculation, more than 240 000 configurations are called for at each relaxation point. The quantity $k T\left\langle\sum \delta\left(t_{1}-z_{i}\right)\right\rangle$ is the force on an inside wall of the slab, and this value is obtained by averaging the values from the two surfaces. The relation between the force and the relaxation length $l$ is shown in Fig. 2. The area under the curve is the free energy change due to relaxation, and this change is $9.97 \epsilon$ for the system. The estimated error for this calculations is $9.4 \%$, and the error is much larger than that of the direct method. This is due to the relatively large statistical uncertainties of the density data at the surfaces. However, the contribution of the relaxation effect to the surface tension is $15 \%$ and the estimated error of $9.4 \%$ in the relaxation process does not lead to a serious error to the final surface tension value.

![](./images/812417706333569027_3.jpg)

FIG. 1. Cumulative Helmholtz free energy change due to liquid separation process. Each circle shows the excess free energy relative to the reference bulk liquid at each separation point. There is no free energy change beyond the cut-off distance $R_{\text{max}}$ (shown in the figure by the arrow).

After increasing the cut-off distance to $5\sigma$, the long-range correction for the potential energy is very small compared to that of the system with a cut-off distance of $2.5\sigma$. This correction term is so small that it can be neglected when calculating the total potential energy of that system. However, in case of a surface tension calculation, the excess quantities of the thermodynamic function are significant, and this small correction term must be included. This correction term is calculated by performing the numerical integration for the potential tail, and the obtained value is $-7.86\epsilon$ for the system. In this case, the free energy difference is set equal to the long-range correction of the potential tail. The estimated error for this integration is negligible.

The total free energy difference between the bulk state and the completely relaxed state is $64.93\epsilon$ for the system. The surface tension and the excess internal energy are calculated for liquid argon at the triple point using the parameters determined by Michels et al. $^{10}$ ($\epsilon/k=119.8^\circ\text{K}$, $\sigma=3.405$ Å). The obtained $\gamma$ is 18.3 dyn/cm, and $U_s$ is $38.9\ \text{erg/cm}^2$. The estimated error is 0.3 dyn/cm for $\gamma$ and $0.8\ \text{erg/cm}^2$ for $U_s$. Both values are compared with those obtained from other methods and also with experimental values in Table II. The surface tension is 36% higher and excess internal energy is 11% higher than the experimental values when the 6:12 potential is used.

<table>
<caption>TABLE II. Comparison of results for surface properties of liquid argon at the triple point ($83.86^\circ\text{K}$).</caption>
<thead>
<tr>
<th></th>
<th>Surface tension (dyn/cm)</th>
<th>Excess internal energy $U_s$ ($\text{erg/cm}^2$)</th>
<th>Excess entropy $S_s$ ($\text{erg/cm}^2\cdot^\circ\text{K}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present work</td>
<td>$18.3\pm0.3$</td>
<td>$38.9\pm0.8$</td>
<td>0.244</td>
</tr>
<tr>
<td>Perturbation$^{\text{a}}$</td>
<td>19.7</td>
<td>$\cdots$</td>
<td>$\cdots$</td>
</tr>
<tr>
<td>Monte Carlo$^{\text{b}}$</td>
<td>$16.5\pm2.6$</td>
<td>$\cdots$</td>
<td>$\cdots$</td>
</tr>
<tr>
<td>BFW+ATM$^{\text{c}}$</td>
<td>14.1</td>
<td>34.7</td>
<td>0.244</td>
</tr>
<tr>
<td>Experimental$^{\text{c}}$</td>
<td>13.4</td>
<td>34.8</td>
<td>$0.255^{\text{d}}$</td>
</tr>
</tbody>
</table>

$^{\text{a}}$Perturbation theory for nonuniform fluid (calculated by F. F. Abraham$^{11}$).
$^{\text{b}}$Monte Carlo method using mechanical definition (Ref. 7).
$^{\text{c}}$Sprow and Prausnitz (Ref. 12).
$^{\text{d}}$Obtained from $S_s=-\partial\gamma/\partial T$.
$^{\text{e}}$Obtained by perturbation theory from 6:12 Monte Carlo results.

## V. DISCUSSION

In our calculation, the effect of the surface relaxation is found to be fairly large, and it decreases $\gamma$ by 13% and increases $U_s$ by 36%. During the relaxation process, the values for $\gamma$ and $U_s$ are calculated at various points including a long-range correction, and these values are listed in Table III. In case of $l=0$, the two surfaces are not relaxed and these values satisfy the inequalities $\gamma$ (step) $>\gamma$ (exp) and $U_s$ (step) $<U_s$ (exp). The surface tension decreases and excess internal energy increases as the surfaces are relaxed, and the change in $U_s$ is much larger than that of $\gamma$.

In the usual Monte Carlo calculation, the thermodynamic quantities are obtained for the bulk liquid where the effect of the potential tail on the molecular configuration is negligible when $R_{\text{max}}$ is larger than $2.5\sigma$. However, in our Monte Carlo model which has two surfaces, the effect of the potential tail is significant and the change in cut-off distance results in a drastic change in $U_s$.

The excess internal energy was calculated in two ways. As the first attempt we performed Monte Carlo runs using a truncated potential with a cut-off distance of $2.5\sigma$ throughout the calculation, and the long-range correction was made at the final stage of the calculation. The obtained excess internal energy is $54.2\ \text{erg/cm}^2$. For the second attempt, as reported in this paper, the

![](./images/812417706333569027_4.jpg)

FIG. 2. Force on a wall of the slab vs relaxation length.

<table>
<caption>TABLE III. The effect of surface relaxation on $\gamma$ and $U_s$.</caption>
<thead>
<tr>
<th>Relaxation length $l$ (Å)</th>
<th>$\gamma$ (dyn/cm)</th>
<th>$U_s$ ($\text{erg/cm}^2$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>21.1</td>
<td>28.5</td>
</tr>
<tr>
<td>0.69</td>
<td>19.7</td>
<td>31.6</td>
</tr>
<tr>
<td>1.71</td>
<td>18.7</td>
<td>35.9</td>
</tr>
<tr>
<td>$>3.77$</td>
<td>18.3</td>
<td>38.8</td>
</tr>
</tbody>
</table>

truncated potential with cut-off distance $2.5\sigma$ is used in separating the slabs but the cut-off distance is increased to $5.0\sigma$ before performing the surface relaxation. The obtained excess energy is $38.9\ \mathrm{erg/cm^2}$. There is a large discrepancy between the two results. This discrepancy shows that the excess internal energy is very sensitive to the density profile. In the former case, the density profile is flatter than the latter owing to the lack of the attractive force between the molecules, and the density at the center of the slab is around 0.8, which is much lower than the initial bulk density. This is the source of the serious error in the excess internal energy calculation, especially for the relaxation process. The density near the center of the slab where the liquid has the bulk properties must be maintained equal to the initial bulk density ($\rho^* = 0.85$); otherwise, the excess internal energy due to not only the surface formation but also to the density change in the bulk region is calculated. The density change in the bulk region during the relaxation process may lead to a large error for $U_s$ even in a 216 molecule system. The use of the larger cut-off distance of $5.0\sigma$ maintains the density at the center of the slab equal to the initial bulk value and the excess internal energy due to the density change in a bulk region does not arise. The thickness of the slab must be large enough to have a bulk liquid region, but employing a much thicker slab may cause a large effect on $U_s$ and also on $\gamma$ unless the density in the bulk region is carefully maintained equal to the initial bulk density. The surface tension values obtained from both approaches are the same. This shows that the surface tension is insensitive to the density profile, but this coincidence is somewhat fortuitous owing the cancellation of errors.

The overestimations of the surface tension and excess internal energy compared with the experimental values are most likely due to the use of the Lennard-Jones 12:6 potential function, which does not represent an accurate potential function for argon.

The surface tension value for a realistic (BFW) argon potential (Barker et al. $)^{13}$ were calculated by perturbation theory from the molecular configurations obtained through our Monte Carlo calculation using the 12:6 potential; three-body interactions were also considered (the Axilrod-Teller-Muto or ATM interaction). The assumptions we made are those of first-order perturbation theory: (a) The use of the Barker potential gives the same molecular configurations. (b) Three-body interactions do not affect the molecular configurations. The surface tension value for the two-body BFW potential is $17.7\ \mathrm{dyn/cm}$ and $14.1\ \mathrm{dyn/cm}$ for the two-body plus three-body interactions. The latter value is in fair agreement with the experimental value for argon.

We note that our Monte Carlo chains would not have been long enough $^{14,15}$ to determine the smooth density profile of the free surface, but in view of the relative insensitivity of the surface tension to density profile, this probably does not affect seriously our calculated surface tension. In any case it should only affect the relatively small "relaxation" contribution.

*Graduate Student, Materials Science and Engineering Department, Stanford University, Stanford, CA.

$^{1}$J. G. Kirkwood and F. P. Buff, J. Chem. Phys. 17, 338 (1949).
$^{2}$F. P. Buff, Z. Elektrochem. 56, 311 (1952).
$^{3}$R. Lovett, P. W. DeHaven, J. J. Vieceli, and F. P. Buff, J. Chem. Phys. 58, 1880 (1973).
$^{4}$B. Widom, in *Phase Transitions and Critical Phenomena*, edited by C. Domb and M. S. Green (Academic, New York, 1973), Vol. 2, Chap. 3.
$^{5}$S. Toxvaerd, J. Chem. Phys. 55, 3116 (1971).
$^{6}$J. A. Barker and D. Henderson, J. Chem. Phys. 47, 4714 (1967).
$^{7}$J. K. Lee, J. A. Barker, and G. M. Pound, J. Chem. Phys. 60, 1976 (1974).
$^{8}$C. H. Bennett (preprint).
$^{9}$N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, J. Chem. Phys. 21, 1087 (1953).
$^{10}$A. Michels, Hub. Wijker, and Hk. Wijker, Physica (Utrecht) 15, 627 (1949).
$^{11}$F. F. Abraham (private communication); cf. J. Chem. Phys. 63, 157 (1975).
$^{12}$F. B. Sprow and J. M. Prausnitz, Trans. Faraday Soc. 62, 1097 (1966).
$^{13}$J. A. Barker, R. A. Fisher, and R. O. Watts, Mol. Phys. 21, 657 (1971).
$^{14}$F. F. Abraham, D. E. Schreiber, and J. A. Barker, J. Chem. Phys. 62, 1958 (1975).
$^{15}$G. A. Chapela, G. Saville, and J. S. Rowlinson, Discuss. Faraday Soc. (to be published).