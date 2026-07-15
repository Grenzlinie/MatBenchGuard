![](./images/813152134575947776_1.jpg)

Vapor bubble nucleation by rubbing surfaces: Molecular dynamics simulations

Takahiro Ito, Henri Lhuissier, Sander Wildeman, and Detlef Lohse

Citation: *Physics of Fluids* (1994-present) **26**, 032003 (2014); doi: 10.1063/1.4868507
View online: http://dx.doi.org/10.1063/1.4868507
View Table of Contents: http://scitation.aip.org/content/aip/journal/pof2/26/3?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Molecular dynamics simulations of nucleation from vapor to solid composed of Lennard-Jones molecules
J. Chem. Phys. **134**, 204313 (2011); 10.1063/1.3593459

Comparative study on methodology in molecular dynamics simulation of nucleation
J. Chem. Phys. **126**, 224517 (2007); 10.1063/1.2740269

Molecular-dynamics simulation of homogeneous nucleation in the vapor phase
J. Chem. Phys. **115**, 8913 (2001); 10.1063/1.1412608

Molecular dynamics simulation of supersaturated vapor nucleation in slit pore. II. Thermostatted atomic-wall model
J. Chem. Phys. **114**, 9578 (2001); 10.1063/1.1370057

Molecular dynamics simulation of supersaturated vapor nucleation in slit pore
J. Chem. Phys. **112**, 4279 (2000); 10.1063/1.480973

![](./images/813152134575947776_2.jpg)

![](./images/813152134575947776_3.jpg)

PHYSICS OF FLUIDS 26, 032003 (2014)

# Vapor bubble nucleation by rubbing surfaces: Molecular dynamics simulations

Takahiro Ito, $^{1,2,a)}$ Henri Lhuissier, $^{1,3}$ Sander Wildeman, $^{1}$ and Detlef Lohse $^{1}$

$^{1}$ Physics of Fluids Group, Department of Science and Technology and Mesa+ Research Institute, Unversity of Twente, P.O. Box 217, 7500 AE Enschede, The Netherlands
$^{2}$ Department of Energy Engineering and Science, Nagoya University, Nagoya 464-8603, Japan
$^{3}$ Matière et Systèmes Complexes, CNRS and Université Paris Diderot UMR 7057 – Bâtiment Condorcet, 10 rue Alice Domon et Léonie Duquet, 75013 Paris, France

(Received 15 October 2013; accepted 23 February 2014; published online 19 March 2014)

We propose a new mechanism for bubble nucleation triggered by the rubbing of solid surfaces immersed in a liquid, in which the fluid molecules squeezed between the solids are released with high kinetic energy into the bulk of the liquid, resulting in the nucleation of a vapor bubble. Molecular dynamics simulations with a superheated Lennard-Jones fluid are used to evidence this mechanism. Nucleation is observed at the release of the squeezed molecules, for squeezing pressures above a threshold value and for all the relative velocities between the solids that we investigate. We show that the total kinetic energy of the released molecules for a single release event is proportional to the number of molecules released, which depends on the squeezing pressure, but is independent of the velocity. © 2014 AIP Publishing LLC.
[http://dx.doi.org/10.1063/1.4868507]

## I. INTRODUCTION

Rubbing two solids immersed in a liquid may induce the formation of bubbles. $^{1–4}$ This phenomenon, also called "tribonucleation," can be observed in situations such as bearing systems, lubrication in machinery, or even in the joints of animals. $^{5}$ It often results in the degradation of the lubricant in the bearings or in the enhancement of erosion at the solid surfaces. Many attempts have thus been made to provide a clear understanding of the phenomenon.

In tribonucleation, the bubble formation and growth has commonly been related to the pressure decrease due to the viscous shear flow in the gap between the solid surfaces. $^{4,6–8}$ Indeed, when the pressure in the liquid drops below the saturation pressure of the liquid, cavitation is expected, provided nucleation sites are present. This pressure drop in the gap is enhanced for thinner gaps, larger rubbing velocities, or larger viscosities of the liquid. For low viscosity liquids, the occurrence of cavitation would therefore require remarkably thin gaps between the solids, while the gap has to be thicker than the typical surface roughness. Recently, however, Wildeman et al. $^{9}$ showed that tribonucleation can also be observed for the gentle rubbing of solids immersed in ethanol, which has a relatively low viscosity (1.2 mPa s at $20\ ^{\circ}\text{C}$). They investigated the nucleation by rubbing a sapphire sphere on an aluminum plate, and found that the nucleation occurs above a threshold for both the rubbing load and velocity. This result suggests that the pressure drop due to the viscous flow is not the only mechanism responsible for the cavitation in tribonucleation. One of the other mechanisms could be the local increase in temperature induced by the rubbing. The actual contact between the solids is realized at the tips of the roughnesses of the solids, over an area which is much smaller than the nominal (or apparent) contact area. On rubbing, the local temperature at the contact surfaces could therefore rise beyond the boiling point, which would facilitate the nucleation

$^{a)}$ Author to whom correspondence should be addressed. Electronic mail: takaito@nucl.nagoya-u.ac.jp

1070-6631/2014/26(3)/032003/12/$30.00
26, 032003-1
© 2014 AIP Publishing LLC

of bubbles. For a dry contact, Kalin,¹⁰ for instance, concluded, by reviewing a number of studies, that the local temperature at the roughness tips, expressed in Celsius, could be up to one order of magnitude higher than that defined for the apparent contact area. The situation for immersed solid surfaces could however be different.

All the effects discussed above deal with increasing the superheating of the liquid, by either decreasing the pressure or increasing the temperature. In this paper, we are concerned with the nucleation itself, i.e., the inception of the vapor bubbles that will grow because of the superheating. We propose a microscopic mechanism: the occurrence of bubble nucleation caused by the sudden release of fluid molecules squeezed between two solid surfaces which are apparently in contact. Indeed, when two initially separated solids are approached in a liquid, some fluid molecules are transiently squeezed between them. In the case of immersed solids being rubbed together, new solid surfaces, at the tip of the roughness, are permanently put in contact, which permanently squeeze new molecules.

As will be detailed further, the squeezed molecules are released with a kinetic energy which is affected by the squeezing pressure, that is to say, the actual pressure exerted on the actual contact area. At any time, this actual contact area $A_{\text{ac}}$ is related to the apparent contact area $A_{\text{ap}}$ via the normal load on the solid $W$ and the surface hardness $M$ as
$$
\frac{A_{\text{ac}}}{A_{\text{ap}}}=\left(\frac{W}{A_{\text{ap}} M}\right)^{x}, \tag{1}
$$
where $x \simeq 0.83$ is an empirical constant.¹¹ For a typical situation⁹ in which a sapphire sphere with radius $R_{\text{s}}=2.5$ mm is rubbed against an aluminum plate under a normal load $W=0.1$ N, the apparent area is $A_{\text{ap}} \sim 2.7 \times 10^{-10}$ m². This gives an actual area $A_{\text{ac}} \sim 1.3 \times 10^{-11}$ m² and an actual pressure $W/A_{\text{ac}} \sim 8$ GPa at the contacts.¹²,²⁵ As the solids are rubbed under such a high pressure, the squeezed molecules are likely to be released with a large kinetic energy and might trigger the nucleation of vapor bubbles, which would then grow without limit as a consequence of the superheating.

The present study investigates this mechanism of bubble nucleation with the aid of molecular dynamics simulations. Section II presents the molecular dynamics model. Section III provides and discusses the results of the calculations, and a summary of the study is given in Sec. IV.

## II. PHYSICAL CONFIGURATION AND CALCULATION METHODS

Fig. 1 shows a schematic of the system we simulated. It consists of a liquid bulk enclosed between two parallel solid plates perpendicular to the direction $\mathbf{e}_{\mathbf{z}}$, the substrate and the top plate. A rectangular block, which idealizes the tip of an asperity of a macroscopic moving solid, is pressed with a pressure $p$ against the substrate, while being displaced tangentially to the substrate with velocity $V \mathbf{e}_{\mathbf{x}}$.

The dimensions $\{X, Y, Z\}$ of the simulation domain are $\{40,4.8,36\}$ nm³ (initial) along $\{\mathbf{e}_{\mathbf{x}}, \mathbf{e}_{\mathbf{y}}, \mathbf{e}_{\mathbf{z}}\}$, and periodic boundary conditions are imposed in $\{\mathbf{e}_{\mathbf{x}}, \mathbf{e}_{\mathbf{y}}\}$.¹³ The block is as wide as the domain ($Y=4.8$ nm) along $\mathbf{e}_{\mathbf{y}}$, but much smaller in the other directions (see Fig. 1). The aspect ratio of the system being close to ten, this results in an essentially two-dimensional motion of the fluid in the $\{\mathbf{e}_{\mathbf{x}}, \mathbf{e}_{\mathbf{z}}\}$ plane.

The fluid is simulated with monatomic molecules. All molecules have the same mass $m=20$ g mol⁻¹. The interactions between molecules, except the inside of each solid, are defined by the Lennard-Jones potential
$$
\phi_{i j}=4 \epsilon_{i j}\left[\left(\frac{\sigma_{i j}}{r}\right)^{12}-\left(\frac{\sigma_{i j}}{r}\right)^{6}\right], \tag{2}
$$
where $\epsilon_{i j}$ and $\sigma_{i j}$ are, respectively, the characteristic energy and the equilibrium distance of interaction between two molecules of type $i$ and $j$, separated by a distance $r$. The values of $\epsilon$ and $\sigma$ are listed in Table I. The coefficients for the fluid–fluid interaction, $\epsilon_{\text{FF}}$ and $\sigma_{\text{FF}}$, are the same as those used in Ref. 14 for the simulation of a surface nanobubble. Although these parameters do not represent a particular material, they permit to simulate a liquid with a low effective viscosity (estimated as

![](./images/813152134575947776_4.jpg)

FIG. 1. Schematic of the simulation.

$0.9\sqrt{m\epsilon_{\text{FF}}}/\sigma_{\text{FF}} \sim 0.1$ mPa s, based on Ref. 15, that is to say, approximately 1/4 of the viscosity of the ethanol used in the experiments by Wildeman *et al.*, $^{9}$ which is 0.44 mPa s at its boiling point. A truncation of the potential function is applied at $r = 1.19$ nm (corresponding to $3.5\sigma_{\text{FF}}$). The solids consist of face-centered cubic lattices with a lattice constant of 0.4 nm. The first and second neighbor molecules in the solids are bonded together by a harmonic potential, with a rigidity constant of $1.4 \times 10^{4}$ kJ mol$^{-1}$ nm$^{-2}$, corresponding to a Young's modulus of 290 GPa, which matches that of the solids used in the experiment by Wildeman *et al.* $^{9}$ The substrate and the top plate are, respectively, 8 and 1 lattice constant thick along $\mathbf{e}_{\mathbf{z}}$.

In order to simulate that the block is a part of a massive object with large heat capacity and mass with respect to molecular scales, two distinct layers of molecules, which do not interact with the fluid molecules, are added on the top surface of the block, as indicated in Fig. 1. The lower layer, referred to as "thermostat layer," consists of thermostat molecules. The temperature in this layer is controlled with a Langevin method. In the upper layer, referred to as "constraint layer," the motion of the molecules in the $\{\mathbf{e}_{\mathbf{x}}, \mathbf{e}_{\mathbf{z}}\}$ plane is constrained. That is, their velocity along $\mathbf{e}_{\mathbf{x}}$ is set at the target value $V$, to generate the relative motion of the block with respect to the substrate, while their motion along $\mathbf{e}_{\mathbf{z}}$ is homogenized by replacing the force exerting on each molecule with the averaged value of this force over all the molecules in the layer, so as to avoid any deformation or rotation of the top surface of the block. To impose the desired pressure $p$ between the block and the substrate, a constant downward force is applied to the molecules in the constraint layer. A thermostat and a constraint layers are also added to the lower surface of the substrate, in order to keep the substrate motionless and at the desired temperature.

<table>
<caption>TABLE I. Lennard-Jones parameters of the molecular interactions.</caption>
<thead>
<tr>
<th>Interaction type</th>
<th>Fluid–fluid</th>
<th>Fluid–solid</th>
<th>Solid (substrate)–solid (block)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\epsilon$ (kJ mol$^{-1}$)</td>
<td>3.0</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>$\sigma$ (nm)</td>
<td>0.34</td>
<td>0.34</td>
<td>0.252</td>
</tr>
</tbody>
</table>

The ambient pressure in the system is set by controlling the motion of the top plate along $\mathbf{e}_z$, with a similar method as for the constraint layer of the block. "Dummy molecules" are distributed at each point of the lattice in the top plate. They have a mass of $2\ \text{g}\ \text{mol}^{-1}$ and do not interact with the fluid molecules. They are bonded with the actual molecules, which can interact with the fluid molecules, and a constant downward force corresponding to the target ambient pressure is applied on them. The motion of the dummy molecules is restricted so that the lattice only moves along $\mathbf{e}_z$, without any deformation or rotation. This method achieves a constant pressure below the plate, except just after nucleation when a pressure peak of typically 20 MPa and lasting typically 10 ps is observed, as a consequence of the rapid expansion of the fluid evaporating into the bubble.

The calculations were performed with the LAMMPS software package, $^{16,17}$ and each simulation followed the same procedure. First, an equilibrium calculation at a temperature of $T_\infty=372\ \text{K}$ $(=1.03\epsilon_{\text{FF}}/k)$ and a system pressure of $p_{\text{sat}}=5.33\ \text{MPa}$ $(=0.042\epsilon_{\text{FF}}/\sigma_{\text{FF}}^3)$, equal to the saturation pressure of the liquid at $T_\infty$, is performed for $1400\ \text{ps}$ $(=1595\sqrt{m\sigma_{\text{FF}}^2/\epsilon_{\text{FF}}})$, with the block located 1.8 nm apart from the top surface of the substrate. In this equilibrium calculation, the fluid temperature is controlled by the Nosé-Hoover method. $^{18,26}$ Next, a downward force is imposed on the constraint layer of the block to descend the block toward the substrate (a damping term is also applied to limit the descending velocity). Most of the fluid molecules between the block and the substrate are expelled into the bulk during the descent of the block. However, the fluid molecules in the vicinity of the solids surfaces, which are presumably adsorbed on the solids as commonly observed when the wettability is not too low, $^{19}$ are not expelled during the descent (but only during the rubbing, as will be discussed further). At the same time, the pressure of the system is reduced to $p_\infty=2.47\ \text{MPa}$ $(=0.019\epsilon_{\text{FF}}/\sigma_{\text{FF}}^3)$, at which the saturation temperature is $331\ \text{K}$ $(=0.92\epsilon_{\text{FF}}/k)$. This sudden pressure reduction eventually put the liquid in a metastable state, equivalent to a superheating of $41\ \text{K}.^{20}$

These final pressure and temperature conditions, applied for the rubbing of the block, are chosen so as to achieve a small superheat. The extent of this superheat can be characterized by the Jakob number $Ja$, which represents the ratio between the latent heat and the excess enthalpy of the superheated liquid. It is defined as

$$
Ja=\frac{\rho_{\text{l}}c_{\text{pl}}(T_\infty-T_{\text{sat}})}{\rho_{\text{v}}L}, \tag{3}
$$

where $\rho_{\text{l}}$ and $\rho_{\text{v}}$ are, respectively, the liquid and vapor densities, $c_{\text{pl}}$ is the specific heat of the liquid, and $L$ is the latent heat of vaporization. The value of $Ja$ in the present simulations is 1.9, which corresponds to a superheat of 1.2 K in the case of ethanol at ambient pressure. Under these conditions, the critical work of nucleation, i.e., the activation energy required to create a two-dimensional vapor bubble with width $Y$ in the bulk of the liquid (which represents the difference between the work required for the creation of the bubble interface and the work done by the pressure difference between the inside and the outside of the bubble) is

$$
\begin{aligned}
Q_{\text{c}}&=2\pi R_{\text{c}}Y\gamma-\pi R_{\text{c}}^2Y(p_{\text{sat}}-p_\infty) \\
&=\pi R_{\text{c}}^2Y(p_{\text{sat}}-p_\infty)\simeq380\ \text{kJ}\ \text{mol}^{-1}\ (=126.7\epsilon_{\text{FF}}),
\end{aligned} \tag{4}
$$

where

$$
R_{\text{c}}=\frac{\gamma}{p_{\text{sat}}-p_\infty}\simeq3.8\ \text{nm}\ (=11.2\sigma_{\text{FF}}) \tag{5}
$$

is the critical radius, i.e., the radius at which the reversible work of formation is maximal, which follows from the two-dimensional Young-Laplace equation, $^{21,27}$ and $\gamma$ stands for the surface tension of the liquid. The value $\gamma=10.9\ \text{mN}\ \text{m}^{-1}$ was obtained from a simulation for an equilibrated flat liquid-vapor surface at $T_\infty$. Although the applicability of Eq. (5) for the bubble nucleation at nanometer scale is still unclear, $^{22,23}$ the present results on the nucleation are consistent with Eq. (5) as will be shown in Sec. III.

Approximately 260 ps $(= 296\sqrt{m\sigma_{\mathrm{FF}}^2/\epsilon_{\mathrm{FF}}})$ after the block reached the surface, the pressure and velocity imposed on top of the block are set to $p$ and $V$, respectively. The time origin $t = 0$ is taken at the initiation of this last motion. Each simulation was performed until all the molecules squeezed under the block during its descent are released into the bulk of the fluid.

## III. RESULTS AND DISCUSSIONS

### A. Preliminary observations

When the block is set into motion, different behaviors are observed in the simulations, depending on the pressure $p$ and the velocity $V$ between the block and the substrate. When the pressure is sufficiently large, nucleation and further growth of a vapor bubble occur. Fig. 2 shows the typical dynamics in this case. At $t = 0$ (Fig. 2(a) (Multimedia view)) some fluid molecules are squeezed between the block (light-gray molecules (yellow online)) and the substrate (dark-gray molecules (orange online)), as a consequence of the previous descent of the block. At $t = 1312.5$ ps (Fig. 2(b)), some of the squeezed molecules have been released in the bulk of the liquid and a "proto-bubble," i.e., a precursor cavity for a potential bubble, appearing as a dark region with a very low density in molecules, has formed. Once nucleated, the bubble grows with apparently no other limits than those of the system (Fig. 2(c)).

To understand the mechanism behind this nucleation, we represent, in Fig. 3(a), the time evolution of the proto-bubble equivalent radius $R$, the number of squeezed molecules $N$, and the instantaneous kinetic energy $E_{\text{inst}}$ of the molecules being released during the event shown in Fig. 2. For comparison, the same quantities are also shown in Fig. 3(b) for the case when the pressure under the block is four times smaller, for which nucleation did *not* occur. The proto-bubble radius is defined as $R = \sqrt{S/\pi}$, where $S$ stands for the area of the vapor region in the $\{\mathbf{e}_\mathbf{x}, \mathbf{e}_\mathbf{z}\}$ plane. $S$ is itself determined by dividing the fluid domain into subcells of $0.4 \times 0.4$ nm$^2$ in the $\{\mathbf{e}_\mathbf{x}, \mathbf{e}_\mathbf{z}\}$ plane with the same width as the domain. The phase of the fluid is then determined from the density in the fluid molecules: Subcells with a density larger than a threshold of $10.4$ nm$^{-3}$, corresponding to the average density between the liquid and vapor phases, are considered as in the liquid state and do not contribute to $S$, while those with a density smaller than the threshold are considered as in the vapor state and do contribute to $S$. $N$ is obtained by counting the number of fluid molecules located between the bottom surface of the block and the substrate. The energy $E_{\text{inst}}$ is calculated as the sum of the individual kinetic energy of the molecules which have been released during a sampling interval of 0.35 ps.

The nucleation is clearly related to the release of squeezed molecules. Fig. 3(a) indeed shows that in the case when nucleation occurs, the proto-bubble radius precisely starts to increase when $N$ suddenly decreases, from 188 to 58, around $t = 1279$ ps, that is to say, when there is a "burst" in the number of molecules being released (hereafter we will simply refer to such release events, in which more than several tens of molecules are released within approximately 10 ps, as "bursts"). At the same time, a pronounced peak in $E_{\text{inst}}$ reaching $907$ kJ mol$^{-1}$, which betrays the large kinetic energy

![](./images/813152134575947776_5.jpg)

FIG. 2. Snapshots of a typical dynamics of nucleation and growth of a vapor bubble ($p = 6.3$ GPa, $V = 1$ m s$^{-1}$) for $t =$ 0 ps (a), 1312.5 ps (b), and 1837.5 ps (c). The inset in (a) shows an enlarged view of the squeezed molecules. (Multimedia view) [URL: http://dx.doi.org/10.1063/1.4868507.1]

![](./images/813152134575947776_6.jpg)

FIG. 3. Time evolution of the equivalent proto-bubble radius, of the number of molecules squeezed under the block and of the instantaneous kinetic energy of the molecules being released. (a) Same bubble nucleation event as in Fig. 2 ($p = 6.3$ GPa, $V = 1$ m s$^{-1}$). (b) A case when no nucleation is observed ($p = 1.6$ GPa, $V = 1$ m s$^{-1}$). The critical radius $R_{\rm c}$ is indicated as a dashed line.

of the molecules being released during the burst, is observed. After the proto-bubble radius has reached the critical value $R_{\rm c}$, it monotonically increases with an essentially constant growth rate. For a much lower pressure $p$ (Fig. 3(b)), a burst in the emission of molecules is also observed, although it is less pronounced and occurs later ($t = 5696$ ps) than in the previous case. A proto-bubble also forms, but it only transiently grows up to a radius $R \simeq 2.1$ nm that is smaller than $R_{\rm c}$ before it shrinks within 370 ps.

The nucleation actually occurs as a consequence of the diffusion of the kinetic energy which is released with the squeezed molecules to the surrounding fluid molecules in the bulk. Fig. 4 illustrates this diffusion in terms of the temperature of the molecules in the bulk for the nucleation event shown in Fig. 3(a).$^{24}$ It also represents the density in fluid molecules for the same event. It shows that the squeezed molecules are released locally at the rear-bottom edge of the block, and that their kinetic energy diffuses as thermal energy to the surrounding fluid just after the initiation of the release at $t = 1279$ ps (Figs. 4(a) and 4(e)). The region with relatively high temperatures ($T \gtrsim 435$ K, delimited by a white broken line in Fig. 4(b)) expands rapidly, but, remarkably, the size of the proto-bubble, in which the density is smaller than $10.4$ nm$^{-3}$ (almost identical to that illustrated by the lower bound of the color code $15$ nm$^{-3}$ in Fig. 4(f)), remains smaller, illustrating that the heat diffuses faster than the vaporization front is progressing. At the same time, a high density ridge (delimited by a black broken line in Fig. 4(f)) forms around the proto-bubble, due to the rapid expansion of the latter. Since the proto-bubble remains surrounded by a region of high temperature, it keeps growing until it eventually reaches the critical size (at $t = 1350$ ps in Figs. 4(d) and 4(h)). Above this size, i.e., for $R > R_{\rm c}$, the bubble grows spontaneously. That is, it grows even if the temperature of the surrounding liquid decreases down to the initial ambient temperature $T_\infty$, because the energy barrier of the nucleation has been overcome. The important point on this diffusion of heat and the emission of a pressure wave is that only a part of the kinetic energy from the released molecules is actually used for the nucleation; the rest is dissipated in the bulk.

These behaviors, together with direct observations of the dynamics, reveal crucial preliminary information about the nucleation process:

![](./images/813152134575947776_7.jpg)

FIG. 4. Local temperature (a)-(d) and density in molecules (e)-(h), at $t=1282.8$, 1288.3, 1294.0, and 1350.0 ps, for the same simulation as in Fig. 3(a). For the sake of clarity, each figure duplicates the periodic domain along $\mathbf{e}_x$. The color scale is the same for the four sub-figures for each quantity. Shaded areas represent the block and the substrate (color online).

- First, the bubble inception is triggered by the sudden release of some of the molecules squeezed under the block. The released molecules have a typical kinetic energy of order $50\ \text{kJ}\ \text{mol}^{-1}$ which is much larger than the typical kinetic energy $3kT_{\infty}/2\simeq4.7\ \text{kJ}\ \text{mol}^{-1}$ of the molecules in the bulk. They collide and share their large kinetic energy with the closest molecules from the bulk, creating a proto-bubble: A region where the density of molecules is low and their kinetic energy is large, with respect to ambient conditions.
- Second, depending on the pressure applied on the block, the proto-bubble may or may not reach the critical size $R_{\text{c}}$ and grow unboundedly.

## B. Results and interpretation

Our observations of nucleation events in the simulations are summarized in Fig. 5 in the form of a phase diagram for the occurrence of nucleation. The criterion for nucleation is chosen as $R > R_{\text{c}}$, as defined in Eq. (5). Since a nucleation event is, by its nature, sensitive to the instantaneous distribution of the fluid molecules, two runs with different initial positions of the molecules were performed for each velocity condition for $p=1.6\ \text{GPa}$, and at least four runs for each velocity and pressure condition for $p\geq3.1\ \text{GPa}$. As Fig. 5 illustrates, the threshold for nucleation is independent of the rubbing velocity $V$, but does depend on the applied pressure $p$. For the cases when $p=1.6\ \text{GPa}$, 20%-38% of the runs show a nucleation event, meaning that the pressure is very close to the effective threshold.

This dependence of nucleation on $p$, and independence from $V$, can be explained from the total energy released during a single burst of molecules. Indeed, the duration of a burst is typically 10 ps, which is shorter than the inertial time $\sqrt{\rho R_{\text{c}}^3/\gamma}\sim50$ ps for the evolution of the critical bubble (the typical time scale $R_{\text{c}}^2/D\sim500$ ps for the diffusion of the molecules at the scale of the bubble, where $D$ is the molecular self-diffusivity, is even much longer and is therefore subdominant to the proto-bubble dynamics). All the molecules emitted during one burst are therefore expected to contribute additively to the nucleation of the same bubble. It is then more relevant to consider the total energy $E_{\text{burst}}$ released during a single burst, which is computed as the sum of $E_{\text{inst}}$ over the burst

![](./images/813152134575947776_8.jpg)

FIG. 5. Phase diagram for nucleation. In the case when both nucleation and absence of nucleation are observed, the number of runs for which nucleation is observed respective to the total number of runs is mentioned above the marker.

duration, rather than the instantaneous energy $E_{\text{inst}}$ itself. Fig. 6 indeed illustrates the key role of $E_{\text{burst}}$ for the nucleation. As shown in Fig. 6(a), $E_{\text{burst}}$ increases with $p$. The nucleation is observed for all the pressure conditions except for the minimum value $p = 1.6$ GPa, for which nucleation occurs only for a portion of the runs. For this last condition, $E_{\text{burst}}$ ranges from 1820 to $3280$ kJ mol$^{-1}$, that is to say, 5-10 times larger than $Q_{\text{c}} \simeq 380$ kJ mol$^{-1}$ (this suggests that only 10%-20% of the kinetic energy of the molecules is effectively transferred to the proto-bubble, the rest diffusing around in the bulk, which is consistent with the discussion of Fig. 4). From these results, it appears that the occurrence of nucleation for increasing $p$ is in fact a consequence of the increase in $E_{\text{burst}}$ with $p$, while the independence of nucleation from $V$ can be attributed to the almost constant value of $E_{\text{burst}}$ as $V$ is increased.

The origin of the kinetic energy of the released molecules is better understood by also looking at the number of molecules that are released. Fig. 7 shows the energy $E_{\text{burst}}$ released during each burst versus the number of molecules $\Delta N_{\text{burst}}$ being released during the same burst, for all the conditions except when nucleation is not observed (i.e., $p = 0.6$ GPa). The two quantities are clearly related linearly to each other. The least mean square fit to the data passing through the origin, plotted as a solid line in the figure, yields a proportional constant $E_{\text{mol0}} = 53.5$ kJ mol$^{-1}$, which corresponds to the average kinetic energy *per molecule* released, measured at the time when it is expelled into the bulk. Although $E_{\text{burst}}$ is somewhat scattered around the fitted line, 88% of the data points lie between

![](./images/813152134575947776_9.jpg)

FIG. 6. Total kinetic energy $E_{\text{burst}}$ emitted during a single burst. (a) Dependence on $p$. The circles (blue onlie) and squares (red online) correspond to $V = 1$ and $0.5$ m s$^{-1}$, respectively. (b) Dependence on $V$. The circles (blue onlie) and squares (red online) correspond to $p = 6.3$ and $3.1$ GPa, respectively. The value plotted for each run corresponds to the first burst which causes the nucleation, for the cases with nucleation, or to the largest burst, for the cases without nucleation. The error bars indicate the maximum and the minimum values for the same conditions. The dashed line represents the critical work of nucleation $Q_{\text{c}}$ defined in Eq. (4).

![](./images/813152134575947776_10.jpg)

FIG. 7. The kinetic energy $E_{\text{burst}}$ versus the number of molecules being released in the same burst. The solid line, with slope $E_{\text{mol0}}$ of $53.5\ \text{kJ}\ \text{mol}^{-1}$, is the least mean square fit to all the data points. The dashed lines have a slope of $(1\pm0.3)E_{\text{mol0}}$. The dashed-dotted line represents $Q_{\text{c}}$.

the dashed lines $(1\pm0.3)E_{\text{mol0}}\Delta N_{\text{burst}}$. This indicates that the kinetic energy *per molecule* released is essentially constant, i.e., neither depends on $p$ nor on $V$, and that the variation in $E_{\text{burst}}$ is only due to the variation in the number of molecules that are released during a single burst. The reason for this increase in $\Delta N_{\text{burst}}$ with $p$ is probably due to the larger amplitude of the stick-and-slip motion of the block as the pressure is increased: A stronger stick is caused by a larger bending of the block, which would release more molecules and thus more energy in a single burst. Indeed, as shown in Fig. 8, the amplitude of the bending depends on $p$, but not on $V$. This is consistent with the observation in Figs. 5 and 6. More generally, in our simulations the stick-and-slip motion and the concomitant bending of the block seem to be governed by a quasi-static equilibrium. We therefore think that the independence on $V$ should persist for lower velocities. There is *a priori* no definite reason why this independence should persist for ever increasing $V$. However, the typical velocity of the released molecules ($\sim2300\ \text{m}\ \text{s}^{-1}$) is three orders of magnitude larger than $V$, and we thus speculate that a $V$-dependence might be observed only for much larger $V$ than those used in our simulations.

More information on the nucleation dynamics can also be obtained by tracking the molecules which were initially squeezed under the block. Fig. 9 presents the time evolution of the ratio $C$ of the current number $n_{\text{sq}}$ of those fluid molecules inside the vapor proto-bubble which were initially squeezed (i.e., which have been released during the motion of the block) to the total number $n_{\text{bubble}}$ of the fluid molecules currently in the proto-bubble, i.e.,

$$
C=\frac{n_{\text{sq}}}{n_{\text{bubble}}}.\tag{6}
$$

For all the pressure and velocity conditions, $C$ peaks at 0.4-0.7 within approximately 5 ps after the initiation of nucleation. It then decreases very rapidly during 10 ps before slowly decreasing to zero within a few hundreds picoseconds. When the proto-bubble reaches the critical size, typically several tens of picoseconds after nucleation, $C\simeq0.1$-0.2. This means that the critical vapor bubble is not filled only with molecules having been squeezed. It is actually mainly filled with molecules that were initially in the bulk, and which evaporated in the proto-bubble as a consequence of the diffusion of the kinetic energy of the released molecules. For this period, the trend in $C$ does neither depend on

![](./images/813152134575947776_11.jpg)

FIG. 8. Bending of the bottom surface of the block and of the substrate induced by the rubbing for $p=6.3\ \text{GPa}$, $V=1\ \text{m}\ \text{s}^{-1}$ (a), $p=6.3\ \text{GPa}$, $V=0.2\ \text{m}\ \text{s}^{-1}$ (b) and $p=1.6\ \text{GPa}$, $V=1\ \text{m}\ \text{s}^{-1}$ (c). The bending in (a) is similar to that in (b) but much larger than that in (c).

![](./images/813152134575947776_12.jpg)

FIG. 9. Evolution of the ratio of those molecules inside the proto-bubble which were initially squeezed under the block. (a) Dependence on $p$ ($V = 1$ m s$^{-1}$). (b) Dependence on $V$ ($p = 6.3$ GPa). Two runs are shown for each condition. The insets show an enlarged view of the initial evolution of $C$ until 20 ps.

$p$ nor on $V$. This indicates that the diffusion of the squeezed molecules is mainly determined by the conditions of the surrounding liquid, i.e., the bulk temperature and pressure, which were not varied in the present simulations.

Finally, the nucleation of a vapor bubble close to solids surface is also expected to be influenced by the wettability of the solids by the liquid. In order to study this effect, we varied the value of the fluid-solid interaction energy $\epsilon_{\text{FS}}$. Fig. 10 shows snapshots of the simulations with different values of $\epsilon_{\text{FS}}$, ranging from 0.8 kJ mol$^{-1}$ (Fig. 10(a)) to 2.0 kJ mol$^{-1}$ (Fig. 10(c)), compared with the case discussed until now, referred to as "base case," with $\epsilon_{\text{FS}} = 1.0$ kJ mol$^{-1}$ (Fig. 10(b)). Although differences in the bubble shape near the contact line, due to different contact angles are observed, nucleation occurred for all the cases. For the largest value of $\epsilon_{\text{FS}}$ (Fig. 10(c)), the solids are completely wetted, and the bubble is formed away from the substrate surface, consistently with a previous study of homogeneous nucleation with molecular dynamics.$^{22}$ As shown in Table II, $\Delta N_{\text{burst}}$, as well as $E_{\text{burst}}$, increase with $\epsilon_{\text{FS}}$. This dependence of $\Delta N_{\text{burst}}$ on $\epsilon_{\text{FS}}$ actually results from the variation in the initial number of the squeezed molecules $N_{\text{ini}}$ shown in the table. $N_{\text{ini}}$ is affected by the density in fluid molecules in the vicinity of the solid surfaces: for large $\epsilon_{\text{FS}}$, the strong attraction between the fluid and solid molecules induces the formation of a dense adhesion layer of fluid molecules there. This results in a larger number of squeezed molecules and explains why $\Delta N_{\text{burst}}$ is larger. In contrast, the value of $E_{\text{mol}}$ appears to be insensitive to $\epsilon_{\text{FS}}$. The ratio $E_{\text{mol}}/E_{\text{mol0}} \sim 1.2$, which is within the bounds $(1 \pm 0.3)E_{\text{mol0}}$ of the scattering in Fig. 7. This indicates that the surface energy between the solid and the fluid does not contribute to the kinetic energy of the squeezed molecules at the release. As a consequence, the total energy $E_{\text{burst}} = \Delta N_{\text{burst}}E_{\text{mol}}$ released during a single burst also increases as $\epsilon_{\text{FS}}$ is increased. This, in turn, should lower the threshold pressure for nucleation observed in Fig. 5.

![](./images/813152134575947776_13.jpg)

FIG. 10. Snapshots of the system after nucleation occurred, for different values of $\epsilon_{\text{FS}}$ corresponding to different wetting behaviors of the liquid on the solids. (a) $\epsilon_{\text{FS}} = 0.8$ kJ mol$^{-1}$. (b) $\epsilon_{\text{FS}} = 1.0$ kJ mol$^{-1}$ (base case). (c) $\epsilon_{\text{FS}} = 2.0$ kJ mol$^{-1}$. The larger $\epsilon_{\text{FS}}$, the smaller the contact angle of the liquid on the solid.

<table>
<caption>TABLE II. Influence of the wettability of the solids on the number of molecules and on the energy released ($p = 12.6$ GPa, $V = 1$ m s$^{-1}$). The values of $\epsilon_{\text{FS0}} = 1.0$ kJ mol$^{-1}$ and $E_{\text{mol0}} = 53.5$ kJ mol$^{-1}$ correspond to the base case discussed in the previous figures. Except for the base case, the values are obtained from a single run for each condition.</caption>
<thead>
<tr>
<th>$\epsilon_{\text{FS}}/\epsilon_{\text{FS0}}$</th>
<th>$N_{\text{ini}}$</th>
<th>$\Delta N_{\text{burst}}$</th>
<th>$E_{\text{burst}}$<br>(kJ mol$^{-1}$)</th>
<th>$E_{\text{mol}} = E_{\text{burst}}/\Delta N_{\text{burst}}$<br>(kJ mol$^{-1}$)</th>
<th>$E_{\text{mol}}/E_{\text{mol0}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.8</td>
<td>125</td>
<td>80</td>
<td>4436</td>
<td>55.5</td>
<td>1.04</td>
</tr>
<tr>
<td>1.0</td>
<td>203</td>
<td>124</td>
<td>8359</td>
<td>67.4</td>
<td>1.26</td>
</tr>
<tr>
<td>2.0</td>
<td>312</td>
<td>183</td>
<td>10088</td>
<td>55.1</td>
<td>1.03</td>
</tr>
</tbody>
</table>

## IV. CONCLUSION

The nucleation process for the formation of vapor bubbles by rubbing solids immersed in superheated liquid was studied with the help of molecular dynamics simulations. A new mechanism was investigated: nucleation induced by the release of the fluid molecules which are squeezed between the two solids, nominally in contact with each other.

The simulations, performed with a Lennard-Jones fluid, revealed that, during the rubbing, the molecules that are initially squeezed between the solids are intermittently released into the bulk with a large kinetic energy. This energy may be larger than the critical work of nucleation, leading to the nucleation of a vapor bubble which then grows without limits. More precisely, the nucleation was observed when the pressure between the solids is higher than a threshold value. The rubbing velocity, however, did not show any threshold value for the nucleation in the examined range. Such dependence on the pressure and independence from the velocity originate from the fact that the kinetic energy for a single release event of molecules, or “burst,” varies with the pressure but is unaffected by the velocity. By contrast, the kinetic energy per molecule released is almost constant throughout the simulations regardless of the pressure, velocity or the solid-fluid surface energy.

## ACKNOWLEDGMENTS

This work was sponsored by the Stichting Nationale Computer faciliteiten (National Computing Facilities Foundation, NCF) for the use of supercomputer facilities, and ERC (the European Research Council) advanced grant.

$^{1}$S. Skinner, “On the occurrence of cavitation in lubrication,” Proc. Phys. Soc. London 19, 73 (1903).
$^{2}$A. T. J. Hayward, “Tribonucleation of bubbles,” Br. J. Appl. Phys. 18, 641 (1967).
$^{3}$K. G. Ikels, “Production of gas bubbles in fluids by tribonucleation,” J. Appl. Physiol. 28, 524–527 (1970).
$^{4}$J. Ashmore, C. del Pino, and T. Mullin, “Cavitation in a lubrication flow between a moving sphere and a boundary,” Phys. Rev. Lett. 94, 124501 (2005).
$^{5}$P. McDonough and E. Hemmingsen, “Bubble formation in crabs induced by limb motions after decompression,” J. Appl. Physiol. 57, 117–122 (1984).
$^{6}$G. I. Taylor, “Cavitation of a viscous fluid in narrow passages,” J. Fluid Mech. 16, 595 (1963).
$^{7}$J. Campbell, “The tribonucleation of bubbles,” J. Phys. D: Appl. Phys. 1, 1085 (1968).
$^{8}$D. Dowson and C. M. Taylor, “Cavitation in bearings,” Annu. Rev. Fluid Mech. 11, 35–65 (1979).
$^{9}$S. Wildeman, H. Lhuissier, C. Sun, A. Prosperetti, and D. Lohse, “Writing bubbles,” Bulletin of the American Physical Society – 65th Annual Meeting of the APS Division of Fluid Dynamics, San Diego, CA, 18–20 November 2012. Available online at http://meetings.aps.org/link/BAPS.2012.DFD.A11.2.
$^{10}$M. Kalin, “Influence of flash temperatures on the tribological behaviour in low-speed sliding: A review,” Mater. Sci. Eng. A 374, 390–397 (2004).
$^{11}$K. L. Woo and T. R. Thomas, “Contact of rough surfaces: A review of experimental work,” Wear 58, 331–340 (1980).
$^{12}$The apparent contact area $A_{\text{ap}}$ between a sphere and a solid plate can be estimated from Hertz’s equation as $A_{\text{ap}} = 1.21\pi[W R_{\text{s}}(E_{1}^{-1} + E_{2}^{-1})/2]^{2/3}$, where $E_{1}$ and $E_{2}$ are the Young’s moduli of the sphere and the plate, respectively.$^{25}$ Substituting $E_{1} = 420$ GPa (sapphire) and $E_{2} = 400$ GPa (alumina which is expected to cover the surface of the aluminum plate) yields the value for $A_{\text{ap}}$, while $A_{\text{ac}}$ follows from Eq. (1) with $M \sim 15$ GPa for alumina.
$^{13}$The simulation system is large enough to behave as infinite with respect to nucleation. Indeed, if the kinetic energy of the released molecules was dissipated equally throughout the whole of the bulk, the liquid temperature would only increase by about 2 K, which is only 5% of the actual superheat ($= 41$ K). This means that the transfer of energy across the (non-physical) periodic boundaries has a negligible influence on the nucleation process.

$^{14}$ J. Weijs, J. H. Snoeijer, and D. Lohse, "Formation of surface nanobubbles and the universality of their contact angles: A molecular dynamics approach," *Phys. Rev. Lett.* **108**, 104501 (2012).

$^{15}$ V. G. Baidakov, S. P. Protsenko, and Z. R. Kozlova, "Shear and bulk viscosity in stable and metastable states of a Lennard-Jones liquid," *Chem. Phys. Lett.* **517**, 166–170 (2011).

$^{16}$ S. Plimpton, "Fast parallel algorithms for short-range molecular dynamics," *J. Comput. Phys.* **117**, 1–19 (1995).

$^{17}$ LAMMPS is an open source code for a classical molecular dynamics on, e.g., solid-state materials, soft matter and droplets, distributed by Sandia National Laboratories. Available at http://lammps.sandia.gov/.

$^{18}$ The Nosé-Hoover method, $^{26}$ by which a canonical ensemble is able to be obtained, was used with success for the equilibration of the liquid. However, it did not work for the thermostat layer in the solids. We think that this is because the molecules of which kinetic energy should be controlled were bonded with molecules constrained to be motionless.

$^{19}$ B. R. Novak, E. J. Maginn, and M. J. McCready, "Comparison of heterogeneous and homogeneous bubble nucleation using molecular simulations," *Phys. Rev. B* **75**, 085413 (2007).

$^{20}$ During the depressurization, only the number of molecules and the temperatures of the block and the substrate are actually constrained to be constant. However, as for a real liquid far away from the critical point, the simulated liquid is almost incompressible, and therefore its temperature is almost constant under depressurization (the global variation we observed was below the statistical fluctuations). Eventually, both the liquid and solid temperatures were unchanged by the depressurization process.

$^{21}$ We consider here a two-dimensional critical bubble, since for a three-dimensional configuration the critical diameter $2R_c = 2\gamma/(p_{\text{sat}} - p_\infty) \simeq 7.6$ nm is much larger than the computational domain width $Y$, which means that the system behaves as a two-dimensional fluid with respect to nucleation. $^{27}$

$^{22}$ G. Nagayama, T. Tsuruta, and P. Cheng, "Molecular dynamics simulation on bubble formation in a nanochannel," *Int. J. Heat Mass Tranfer* **49**, 4437–4443 (2006).

$^{23}$ S. Tsuda, S. Takagi, and Y. Matsumoto, "A study on the growth of cavitation bubble nuclei using large-scale molecular dynamics simulations," *Fluid Dyn. Res.* **40**, 606–615 (2008).

$^{24}$ The values are averaged over 5.6 ps over a rectangular mesh of $0.5 \times 4.8 \times 0.5$ nm$^3$. The temperature is defined as $m\langle \mathbf{v} - \langle \mathbf{v} \rangle \rangle^2/3k$, where $\mathbf{v}$ is velocity of each molecule, $k$ is the Boltzmann constant, and $\langle \cdot \rangle$ denotes the averaging.

$^{25}$ F. P. Bowden and D. Tabor, *The Friction and Lubrication of Solids* (Oxford University Press, New York, 1950).

$^{26}$ S. Nosé, "A unified formulation of the constant temperature molecular dynamics methods," *J. Chem. Phys.* **81**, 511–519 (1984).

$^{27}$ V. P. Skripov, *Metastable Liquids* (Wiley, New York, 1974).