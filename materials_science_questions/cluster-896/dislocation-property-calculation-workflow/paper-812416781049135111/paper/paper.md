# Atomistic Simulations of the Motion of an Edge Dislocation in Aluminum Using the Embedded Atom Method

N. Bhate, R. J. Clifton, and R. Phillips

Citation: *AIP Conference Proceedings* **620**, 339 (2002); doi: 10.1063/1.1483548
View online: https://doi.org/10.1063/1.1483548
View Table of Contents: http://aip.scitation.org/toc/apc/620/1
Published by the American Institute of Physics

---

## Articles you may be interested in

### Mobility of Dislocations in Aluminum
*Journal of Applied Physics* **40**, 833 (1969); 10.1063/1.1657472

### Dislocation Velocities, Dislocation Densities, and Plastic Flow in Lithium Fluoride Crystals
*Journal of Applied Physics* **30**, 129 (1959); 10.1063/1.1735121

### Mobility of Dislocations in Aluminum at 74° and 83°K
*Journal of Applied Physics* **40**, 903 (1969); 10.1063/1.1657491

### Elastic precursor wave decay in shock-compressed aluminum over a wide range of temperature
*Journal of Applied Physics* **123**, 035103 (2018); 10.1063/1.5008280

---

![](./images/812416781049135111_1.jpg)

CP620, Shock Compression of Condensed Matter - 2001
edited by M. D. Furnish, N. N. Thadhani, and Y. Horie
© 2002 American Institute of Physics 0-7354-0068-7/02/$19.00

# ATOMISTIC SIMULATIONS OF THE MOTION OF AN EDGE DISLOCATION IN ALUMINUM USING THE EMBEDDED ATOM METHOD

N. Bhate, R. J. Clifton and R. Phillips*

Division of Engineering, Brown University, Providence, Rhode Island 02912
*Graduate Aeronautical Laboratories, Caltech, Pasadena, California 91125

**Abstract.** The motion of an edge dislocation is analyzed for temperatures ranging from 10 K to 200 K and for stresses up to 5 GPa. The dislocation velocity versus the applied shear stress curve can be divided into four regimes corresponding to successively higher shear stresses. In the first regime, the applied shear stress is below the Peierls stress and the dislocation velocity is nominally zero. In the second regime, the dislocation velocity decreases with increasing temperature indicating the presence of a drag due to thermal phonons. In the third regime, the dislocation reaches a sub-sonic limiting velocity that can be predicted by a two-dimensional lattice-dynamics analysis. Such an analysis predicts a limiting velocity for a moving defect when the phase velocity and the group velocity are equal. If even higher shear stresses are applied, the dislocation travels with a transonic velocity of $\sqrt{2}$ times the shear wave speed.

## INTRODUCTION
Improved understanding of the mobility of dislocations is important to improved un- derstanding of the mechanical behavior of crystalline materials. While for many structural alloys the motion of dislocations is limited primarily by the presence of interstitials, solute atoms, and precipitates, there are cases for which the intrinsic resistance of the lattice plays a dom- inant role in limiting the motion of dislocations. Such cases include the plastic behavior of $Ni_3Al$ with its $L1_2$ crystal structure¹ and the brittle versus ductile failure of tungsten single crystals at different temperatures². Although most interest is in the subsonic motion of dislocations, there are phenomena — such as martensitic twinning and geophysical fault slip — where the transonic or supersonic motion of dislocations appears to be of interest. Several researchers have simulated the dynamics of dislocations, with particular emphasis on probing the high velocity regime³,⁴,⁵. In the present study⁶, molecular dynamics is used to examine the effects of applied stress and temperature on the mobility of an edge dislocation in Al.

## METHODOLOGY AND MODEL DESCRIPTION
The simulation cell geometry for modeling an edge dislocation in Al is shown in Figure 1. The crystal is oriented so that the X-axis is along the slip direction ⟨110⟩, the Y-axis is along the dislocation line ⟨112⟩ and the Z-axis is oriented along the normal ⟨111⟩ to the slip plane. The cell dimensions are $226.66\mathring{A} \times 4.59\mathring{A} \times 137\mathring{A}$ or $40 \times 2 \times 60$ atomic layers in the X, Y and Z directions, respectively. Periodic boundary conditions are imposed at cell boundaries that are perpendicular to the X and the Y directions. The cell is regarded as being finite along the Z direction. Interaction forces between atoms are described by the embedded atom method (EAM)⁴, using potentials for

![](./images/812416781049135111_2.jpg)

FIGURE 1: Schematic of the simulation cell.

aluminum developed by Ercolessi and Adams⁷.

The simulation cell is constructed as a perfect aluminum lattice. Two atomic half-layers are removed from the lower half of the cell. The remaining atoms are then displaced by the Volterra displacements in order to introduce an edge dislocation. The energy of the configuration is minimized subject to the requirement that the atoms in the top and bottom layers move only in the X-Y plane. The energy minimization results in dissociation of the edge dislocation into two partials separated by a stacking fault. The width of the stacking fault agrees well with that obtained using lattice statics. The configuration with the dissociated edge dislocation is used as the initial configuration for all of the molecular dynamics simulations.

Simulations have been carried out at four temperatures: 10 K, 50 K, 100 K and 200 K, and for shear stresses ranging from 1 MPa to 5000 MPa. At each temperature, the atoms in the initial configuration are given random initial velocities corresponding to the Maxwell- Boltzmann distribution at the test temperature. Temperature is maintained constant in the simulations by applying the Nose-Hoover drag⁸.

The initial configuration is allowed to equili- brate for 1 ps in order to achieve equipartitioning of the energy. An equal and opposite shear stress is then applied to the top and bottom surfaces by applying forces to the atoms in the top and bottom layers. The simulation is carried out for a total of 100 ps under application of the constant stress. The edge dislocation is observed to reach a steady velocity within the first 20-40 ps. The rise time corresponds to a few multiples of the time, $t_h \approx 4ps$, taken by an elastic shear wave to travel the thickness of the film.

![](./images/812416781049135111_3.jpg)

FIGURE 2: Dislocation velocity as a function of applied stress and temperature.

## COMPUTATIONAL RESULTS

The position of the edge dislocation as a func- tion of time is determined from the location of the peak in the slip distribution. It is clear from plotting dislocation position vs. time for various stresses and temperatures that the resistance to the motion of the dislocation is higher at higher temperatures, although at a shear stress of 500 MPa, the effect of temperature appears to be negligible. At the highest temperature, 200 K, and the lowest stress, 10 MPa, the dislocation is even arrested momentarily. In all cases, the dislocation approaches a steady velocity after 40 ps. The steady velocity reached for these edge dislocations is shown in Figures 2 and 3 as a function of the applied stress at each of the four temperatures. From the figures it is evident that there are four distinct regimes. In the first regime, the shear stress is sufficiently small that the dislocation is stationary, or essentially so. The behavior in this regime is governed by the Peierls barrier. In the second regime, the shear stress is large enough to cause dislocation motion — at a velocity that decreases with increasing temperature. In this regime the behavior is strongly affected by the

![](./images/812416781049135111_4.jpg)

FIGURE 3: Tangent lines, drawn from the origin, to estimate the dislocation drag coefficient.

interaction of dislocations with thermal phonons.
At still higher stresses, say greater than 100
MPa, the curves in Figure 2 approach a plateau
corresponding to a temperature-independent,
limiting dislocation velocity of approximately
$2.1nm/ps$, or approximately 70% of the speed of
elastic shear waves in aluminum. An explanation
of this limiting velocity is provided in the final
section of this paper. Finally, at the highest
shear stresses shown, there is a fourth regime
in which the dislocation velocity jumps to a
transonic speed of approximately $\sqrt{2}c_s$ where
$c_s$ is the elastic shear wave speed. Eshelby$^9$
has established that – in continuum elasticity –
transonic, radiation-free dislocation motion can
occur only at a dislocation velocity of $\sqrt{2}c_s$.

DISLOCATION DRAG COEFFICIENT

The applied shear stress $\tau$ and the dislocation
velocity $v$ are often related by the linear relation

$$
\tau = Bv/b, \tag{1}
$$

where $b$ is the magnitude of the Burgers vector
and B is a dislocation drag coefficient.

In the simulations the dislocation velocity
does not increase proportionally with increasing
stress. However, the dislocation drag coefficient
in such a relation can, for a given temperature,
be estimated by considering the slope of a line
radiating from the origin and becoming tangent
to the corresponding curve in Figure 3. Using
the tangent line to estimate $B$ minimizes effects
from the Peierls stress regime as well as from
the regime in which the dislocation velocity is
at its subsonic limiting value. The dislocation
drag coefficient determined in this way has the
temperature dependence shown in Figure 4.
While it is tempting to regard Figure 4 as giving
a prediction of the temperature dependence of
the drag coefficient B for aluminum, one should
remember that the plot of dislocation velocity vs.
applied stress in Figure 3 is strongly nonlinear.
Thus, Figure 4 should be interpreted as a means
of characterizing the dependence of dislocation
mobility on temperature over a certain range of
stresses, not as support for the validity of the
linear drag relation of Eqn. (1).

![](./images/812416781049135111_5.jpg)

FIGURE 4: Dislocation drag coefficient B as a
function of temperature.

LATTICE DYNAMICS PREDICTION
OF THE LIMITING DISLOCATION
VELOCITY

Groteleuschen$^{10}$ and Gumbsch and Gao$^3$
observed a relationship between dislocation
velocity and applied stress that is similar to the
one shown in Figure 2. The limiting velocity in
the third regime (about 70% of the slowest shear
wave speed) cannot be explained by continuum
elasticity. The lattice-dynamics model by Celli
and Flytzanis$^{11}$ suggests a means for providing
a possible explanation.

Using lattice dynamics with nearest-neighbor
interactions, Celli and Flytzanis$^{11}$ derived the

relation between dislocation velocity and applied strain for a screw dislocation in a two- dimensional lattice. The Celli-Flytzanis analysis suggests that the limiting dislocation velocity is a phonon velocity having equal values for its phase velocity and its group velocity, in the direction of the motion of the dislocation. To obtain such a limiting dislocation velocity for aluminum, dispersion relations are obtained using the EAM potentials. These dispersion relations are represented as plots of the frequency $\omega$ as a function of the components $k_x, k_y$ and $k_z$ of the wave number $\mathbf{k}$ of harmonic plane waves.

The equations of motion for atoms in a three- dimensional lattice can be expressed as,

$$
M \ddot{\mathbf{u}}(\mathbf{R})=-\sum_{\mathbf{R}^{\prime}} \mathbf{D}\left(\mathbf{R}-\mathbf{R}^{\prime}\right) \mathbf{u}\left(\mathbf{R}^{\prime}\right), \quad(2)
$$

where $M$ is the mass matrix, $\mathbf{u}$ are the displacements and $\mathbf{D}$ is the *force-constant* matrix formed using the interaction between the atoms of the lattice. Dispersion relations are obtained by considering plane wave solutions for the displacements $\mathbf{u}$ to obtain the characteristic condition

$$
\left|\tilde{\mathbf{D}}-M \omega^{2} \mathbf{I}\right|=0, \quad(3)
$$

where $\tilde{\mathbf{D}}$ is the dynamical matrix. Eq. (3) can be solved numerically to obtain the eigenvalues, $\omega^{2}$ for given $\mathbf{k}$. A numerical program, vibra, developed at Sandia National Laboratories was used for this purpose.

Based on the Celli-Flytzannis analysis, phonons associated with the limiting dislocation velocity, say $v_1$, are expected to satisfy $\partial \omega / \partial k_y=0, \partial \omega / \partial k_z=0, \partial \omega / \partial k_x=v_1$. For a lattice having fcc symmetry, and for the dislocation orientation of Figure 1, the first two conditions are satisfied for $k_y=2 \sqrt{2} /(a_0 \sqrt{3})$ and $k_z=2 \pi /(a_0 \sqrt{3})$. For these values of $k_y$ and $k_z$, Figure 5 shows the dispersion relation for aluminum based on the Ercolessi-Adams potentials. The group velocity and the phase velocity in the x-direction are equal for the wave number at which a radial line from the origin is tangent to one of the dispersion curves. The wave number and velocity at the first such tangent point are $k_x=3.28 \AA^{-1}, \quad v_1=1.56 \mathrm{~nm} / \mathrm{ps}$. The velocity $v_1$ is approximately $25 \%$ less than the velocity at the plateau in Figure 2. Better agreement is obtained as the computational effects of cell size are reduced. For example, doubling and halving the spacing of dislocations in the x-direction leads to an extrapolated value for the plateau velocity of approximately $v_1$ as the reciprocal of the dislocation spacing approaches zero.

![](./images/812416781049135111_6.jpg)

FIGURE 5: Dispersion relation for aluminum, based on Ercolessi-Adams EAM potentials.

## ACKNOWLEDGEMENTS
The authors gratefully acknowledge the sup- port of the NSF-MRSEC at Brown University.

## REFERENCES
1. Jiang, C. B., Patu, S., Lei, Q. Z. and Shi, C. X., Philos. Mag. Lett., 78, pp. 1-8 (1998).
2. Gumbsch, P., Riedle, J., Hartmaier, A. and Fischmeister, H. F., Science, 282, pp. 1293-1295 (1998).
3. Gumbsch, P. and Gao, H. Science, 283, pp. 965-968 (1999).
4. Daw, M. S., Foiles, S. M. and Baskes, M. I. Material Science Reports, 9, pp. 251-310 (1993).
5. Grujicic, M., Journal of Materials Science, 32, pp. 1749-1757 (1997).
6. Bhate, N., PhD Thesis, Brown University (2001).
7. Ercolessi, F. and Adams, J. Europhysics Letters, 26, pp. 583-588 (1993).
8. Hoover, W.G., Computational Statistical Mechanics, Elsevier (1991).
9. Eshelby, J. D., Proc. R. Soc. London A, 62 (1949).
10. Groteleuschen, L. P., PhD Thesis, Brown University (1993).
11. Celli, V. and Flytzanis, N., J. Appl. Phys., 41, pp. 4443-4447 (1970).

342