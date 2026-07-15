# Investigation of the discontinuous precipitation of U-Nb alloys via thermodynamic analysis and phase-field modeling

Thien C. Duongⁿ, Robert E. Hackenbergᶜ, Vahid Attariᵃ, Alex Landaᵈ, Patrice E.A. Turchiᵈ, Raymundo Arróyaveᵃ,ᵇ,∗

ᵃ Department of Materials Science and Engineering, Texas A&M University, College Station, TX 77843-3123, United States
ᵇ Department of Mechanical Engineering, Texas A&M University, College Station, TX 77843-3123, United States
ᶜ Los Alamos National Laboratory, P.O. Box 1663, Los Alamos, NM 87545, United States
ᵈ Lawrence Livermore National Laboratory, 7000 East Ave., Livermore, CA 94550-9234, United States

---

## ARTICLE INFO

**Keywords:**
Phase-field modeling
Metallic fuels
U-Nb
Thermodynamics
Discontinuous precipitation

## ABSTRACT

U-Nb's discontinuous precipitation, $\gamma_{matrix}^{bcc} \rightarrow \alpha_{cellular}^{orth} + \gamma_{cellular}^{bcc}$, is intriguing in the sense that it allows formation and growth of the metastable $\gamma'$ phase during the course of its occurrence. Previous attempts to explain the thermodynamic origin of U-Nb's discontinuous precipitation hypothesized that the energy of $\alpha$ forms an intermediate common tangent with the first potential of the double-well energy of $\gamma$ at the $\gamma'$ composition. In this work, we examine different possible mechanisms by which the discontinuous precipitation product in the U-Nb system can be stabilized. We put forward a mechanism by which the bulk free energy of the $\gamma$ can develop a non-monotonic dependency with composition. Additionally we posit that local contributions due to lattice mismatch between the $\alpha$ and $\gamma$ phases may be responsible for the generation of metastable states that may stabilized by thermodynamics as well as by kinetics. Our work suggests that local misfit strain tends to play a crucial role in the growth of the discontinuous precipitation product. Depending on the magnitude of strain developed at the $\alpha/\gamma'$ interfaces, either an increasing $\gamma'$ composition or a random distribution of $\gamma'$ compositions around the equiatomic value with respect to increasing temperature could be expected. Moreover, we show how it is possible to stabilize the discontinuous precipitation front through highly anisotropic and fast interface diffusion.

---

## 1. Introduction

Given its high melting point, good corrosion resistance, good conductivity and continuous bcc region at high temperatures, the U-Nb system is considered a promising metallic fuel candidate for Gen-IV fast breeder reactors. This alloy system, however, exhibits various metastable phase transformations whose resulting microstructures strongly affect the fuel's performance (see, for instance, [1–4]). In the current work, the phase transformation of interest is discontinuous precipitation (DP) [5–7] whose lamellar microstructure is known to degrade U-Nb's corrosion resistance and ductility [8]. DP is the result of a decomposition from a supersaturated solid solution into a solute-depleted matrix and a precipitate across a moving grain boundary [6,7]. In the U-Nb system, DP occurs as part of the monotectoid decomposition:

$$\gamma \stackrel{DP}{\rightarrow} \alpha + \gamma' \stackrel{DC}{\rightarrow} \alpha + \gamma_{2}$$

in which, $\gamma$ is a quenched bcc matrix, $\alpha$ is orthorhombic precipitate, and $\gamma'$ is metastable bcc precipitate with an intermediate composition differing from that of stable $\gamma_{2}$ (see Fig. 1(a)), DP corresponds to discontinuous precipitation while DC is discontinuous coarsening.

Although the observations of DP in the U-Nb system have been commonly reported, the thermodynamic and/or kinetic origin of its occurrence was scarcely addressed. Djuric [9] examined the decomposition of the $\gamma$ phase in U-21.2Nb (at.%) alloy. The samples were first homogenized at $950\ ^{\circ}\text{C}$ for one week followed by water quenches. The samples were then solutionized at $900\ ^{\circ}\text{C}$ for 24 h and transferred to a tin bath for isothermal heat treatments at temperatures between $450\ ^{\circ}\text{C}$ and $600\ ^{\circ}\text{C}$. For longer isothermal heat treatments, a double-stage vacuum furnace where the upper part was held at the solution treatment temperature and the lower at isothermal treatment temperature was used. Based on the post-XRD analyses of the samples quenched from isothermal heat treatment, Djuric hypothesized that $\alpha$ and $\gamma$ form two local equilibria (LE) with each other, one at an intermediate composition, $\gamma'$, and the other at the global equilibrium composition, $\gamma_{2}$. Due to the former LE, $\gamma$ would decompose partially into $\alpha$ and metastable $\gamma'$, if

∗ Corresponding author.
E-mail address: rarrayave@tamu.edu (R. Arróyave).

https://doi.org/10.1016/j.commatsci.2020.109573
Received 30 June 2019; Received in revised form 17 December 2019; Accepted 28 January 2020
0927-0256/ © 2020 Elsevier B.V. All rights reserved.

![](./images/812670390399664129_1.jpg)

![](./images/812670390399664129_2.jpg)

Fig. 1. (a) Schematic representation of discontinuous monotectoid decomposition in uranium - niobium system; (b) Schematic energies describing Djuric's hypothesis [9].

its initial composition $\gamma_1$ was greater than $\gamma'$. This explains the occurrence of DP. After suitably long incubation, the $\gamma_2$ phase will nucleate in the system and, since it corresponds to the stable phase in equilibrium with $\alpha$, it would evolve spontaneously, resulting in discontinuous coarsening, DC. As the isothermal holding temperature increased, Djuric observed that the composition of the $\gamma'$ precipitate gradually shifted towards Nb-lean compositions. To demonstrate their hypothesis, Djuric schematically described energy profiles reproduced in Fig. 1(b).

More recent investigations of the DP and DC processes in U-13Nb and U-17Nb (at.%) [8] showed that the composition of the metastable $\gamma'$ precipitate was constant or perhaps evolved towards compositions richer in Nb as the aging temperature increased. The compositions in that earlier study were obtained by measuring, via XRD, the lattice parameters of the different product phases and then relating the measured lattice parameters through composition by using a quadratic relationship measured over uniform U-Nb alloys by Pfeil and collaborators [10]. However, a later update to this study [11] reported lamellar divergency and nonsteady-state growth in the same alloys, which called into question any temperature dependence inferred from [8], as the compositions at $450\ ^{\circ}\text{C}$ and higher are better represented by a spread of compositions (yet to be published) for a given aging temperature, not a single point. In any event, the larger question is what stabilizes the $\gamma'$ composition against immediate decomposition with respect toward the equilibrium $\gamma_2$ phase to begin with. The Gibbs energy schematic put forward by Djuric illustrates the generation of competing common tangent equilibria but in all cases the common tangent between $\alpha$ and $\gamma'$ is always metastable with respect to the $\alpha$ and $\gamma_2$ equilibrium. How the metastable equilibrium can persist over long aging conditions remains unclear.

To shed some light towards the addressing of these questions, we attempt, in the current work, the investigation of possible mechanisms that stabilize the DP product from the fundamental thermodynamic and kinetic points of view. We make use of phase-field theory in order to examine thermodynamic and kinetic factors responsible for the evolution of microstructures with arbitrary topologies [12-16]. Here, we use the phase-field interface dissipation model developed by Zhang and Steinbach et al. [17,18]. In contrast with previous phase-field [19,20] and sharp-interface [21-30] models, the finite interface dissipation model does not necessarily require local equilibrium conditions at phase interfaces and the degree to which this quasi-equilibrium condition is enforced can be controlled by a so-called permeability parameter that controls how easy or difficult is for solutes to cross phase interfaces. This feature makes it possible to examine the stabilization of highly metastable phases, such as $\gamma'$ in the DP process in U-Nb alloys that are the focus of the present work.

## 2. Methods

### 2.1. Thermodynamic analysis

To investigate the potential mechanisms responsible for the stabilization of the DP product in U-Nb alloys, the phase field finite interface dissipation model was implemented in place of a free-energy minimizer to investigate the CALPHAD free energies of $\alpha$ and $\gamma$ for their possible local equilibrium, LE, states (states of minimal energy). The idea is to utilize the verified CALPHAD description of the U-Nb binary system as a quantitative reference to examine different possible mechanisms for the stabilization of the DP microstructure in the U-Nb system.

Here, the thermodynamic energy functional or driving force for the interactions is taken to be a function of chemical interactions due to compositional fluctuations and the local contractions/expansions associated with the composition dependence of elastic constants and lattice parameters. While compositional changes are responsible for LE, strain energy resulting from local changes in lattice parameters can alter the path to LE, too. In principle, elastic interactions may have more complex effects on the final microstructure of the system due to elastic anisotropy and the long-range elastic interactions between the domains. To study this, we write the total free energy function as:

$$
\mathscr{F}^{\text{tot}}[c, \varepsilon] = \int_{v} (f_{\text{chemical}} + f_{\text{elastic}})dV \tag{1}
$$

where chemical energy, $f_{\text{chemical}}$, and strain energy, $f_{\text{elastic}}$ respectively are:

$$
f_{\text{chemical}} = f^{0}(c, T) \tag{2}
$$

$$
f_{\text{elastic}} = \frac{1}{2}\sigma_{ij}\varepsilon_{ij}^{el} \tag{3}
$$

where $f^{0}(c, T)$ describes the energy of the homogeneous region of the microstructure for a given composition (c) and temperature (T). We replace this by the previously optimized CALPHAD free energy formalism [31] for further thermodynamic analysis. $\sigma_{ij}$ and $\varepsilon_{ij}^{el}$ correspond to the local stress and elastic strain in the material, respectively. We determine the value of stress and elastic strain in the system within linear elasticity (i.e. elastic strain energy is a quadratic function of strain)

#### 3.2.1.

### 2.2. Phase-field method

We use the finite interface dissipation phase-field approach developed by Steinbach et al. [17] to further investigate the process of DP in U-Nb. In the present work, the free energy functional has contributions

from the local chemical free energy $(f_{chemical})$ and interfacial energy $(f_{interface})$:

$$
\mathscr{F}^{t o t}[c, \phi, \nabla c, \nabla \phi]=\int_{v}\left(f_{interface}+f_{chemical}\right) d V
\tag{4}
$$

$$
f_{\text {interface }}=\frac{4 \sigma_{\alpha \beta}}{\eta}\left\{-\frac{\eta^{2}}{\pi^{2}} \nabla \phi_{\alpha} \cdot \nabla \phi_{\beta}+\phi_{\alpha} \phi_{\beta}\right\}
\tag{5}
$$

$$
f_{\text {chemical }}=\phi_{\alpha} f_{\alpha}\left(c_{\alpha}\right)+\phi_{\beta} f_{\beta}\left(c_{\beta}\right)+\lambda\left\{c-\left(\phi_{\alpha} c_{\alpha}+\phi_{\beta} c_{\beta}\right)\right\}
\tag{6}
$$

where $\sigma_{\alpha \beta}, \eta, \phi_{\alpha / \beta}, c_{\alpha / \beta}$, and $c$ are interfacial energy, interface width, phase fractions of $\alpha / \beta$ phases, phase concentrations of $\alpha / \beta$ phases, and overall concentration, respectively. $\alpha$ is used interchangeably as the phase index in the model description and $\alpha$-U indicator throughout the paper. $f_{\alpha}$ and $f_{\beta}$ are the free energy densities. $\lambda$ is the Lagrange multiplier, which is introduced to assure the solute conservation constraint given by: $c=c_{\alpha} \phi_{\alpha}+c_{\beta} \phi_{\beta}$. The evolution equations are given as:

$$
\phi_{\alpha} \dot{c}_{\alpha}=\nabla\left(\phi_{\alpha} D_{\alpha} \nabla c_{\alpha}\right)+P^{\text {interface }} \phi_{\alpha} \phi_{\beta}\left(\frac{\partial f_{\beta}}{\partial c_{\beta}}-\frac{\partial f_{\alpha}}{\partial c_{\alpha}}\right)+\phi_{\alpha} \dot{\phi}_{\alpha}\left(c_{\beta}-c_{\alpha}\right)
\tag{7}
$$

$$
\dot{\phi}_{\alpha}=K\left\{\sigma_{\alpha \beta}\left[\nabla^{2} \phi_{\alpha}+\frac{\pi^{2}}{\eta^{2}}\left(\phi_{\alpha}-\frac{1}{2}\right)\right]-\frac{\pi^{2}}{8 \eta} \Delta g_{\alpha \beta}^{\phi}\right\}
\tag{8}
$$

where $D_{\alpha}, D_{\beta}$ are the chemical diffusivities in the $\alpha$ and $\beta$ phases, respectively, and $P^{\text {interface }}$ is the interface permeability defined as: $P^{\text {interface }}=\frac{8 M}{a \eta}$. Here, $M$ is the atomic mobility and $a$ is the lattice constant. Further information on the physical meaning of the interface permeability, $P^{\text {interface }}$, can be found in [17]. $K$ and $\Delta g_{\alpha \beta}^{\phi}$ are given as:

$$
K=\frac{8 P^{\text {interface }} \eta \mu_{\alpha \beta}}{8 P^{\text {interface }} \eta+\mu_{\alpha \beta} \pi^{2}\left(c_{\alpha}-c_{\beta}\right)^{2}}
\tag{9}
$$

$$
\Delta g_{\alpha \beta}^{\phi}=f_{\alpha}-f_{\beta}+\left(\phi_{\alpha} \frac{\partial f_{\alpha}}{c_{\alpha}}-\phi_{\beta} \frac{\partial f_{\beta}}{c_{\beta}}\right)\left(c_{\beta}-c_{\alpha}\right)
\tag{10}
$$

where $\mu_{\alpha \beta}$ is the interfacial mobility, $K$ is the kinetic coefficient describing the effect of finite diffusion and redistribution at the interface and $\Delta_{\alpha \beta}^{\phi}$ is the chemical driving force. An in-house Fortran code is developed where the governing equations are solved by means of a central difference explicit scheme. The code is also recently incorporated in the study of solidification of Ni-Nb alloy during additive manufacturing [32]. The summary of model parameters and physical parameters used in this work is given in Table 1. For solving the model's evolution equations, finite-difference method was utilized. The numerical stability of this linear solver was supported by dynamic time step.

### 3. Results and discussion

#### 3.1. 1-D phase-field study and local equilibria

To find possible LE between the CALPHAD energies of $\alpha$ and $\gamma$ using the proposed phase-field model, it is found that the diffusion-couple-type simulation is ideal for its simplicity as LE is sufficiently indicated when the Kirkendall interface stops moving, its driving force vanishes, and the compositions of the two reacting phases are homogeneous. The schematic demonstration of the phase-field diffusion couple is shown in Fig. 2.

The couple of interest is $1 \mu \mathrm{m}$ long and initially consists of $0.1 \mu \mathrm{m}$ of $\alpha$ and $0.9 \mu \mathrm{m}$ of $\gamma$. It has a total of 500 grid points with the step of $2 \mathrm{~nm}$ and interfacial width of $10 \mathrm{~nm}$. The initial compositions of $\alpha$ and $\gamma$ are 1 at.\% $\mathrm{Nb}$ and 13 at.\% $\mathrm{Nb}$ respectively. To estimate thermodynamic driving force (in form of energy density $\left[\mathrm{J} / \mathrm{cm}^{3}\right]$ ), the previously assessed CALPHAD energetic data are used [31]; for simplicity, the used molar volumes for this estimation are assumed to be constant and take the average value of those from the initial orthorhombic and bcc phases. The interfacial energies are taken as the averages of those evaluated in [8].

<table>
<thead>
<tr>
<th colspan="3">Table 1</th>
</tr>
<tr>
<th colspan="3">Numerical and material parameters for the calculations.</th>
</tr>
<tr>
<th>Parameters</th>
<th>Symbols</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Grid spacing</td>
<td>$\Delta x$ [nm]</td>
<td>2.0 (1D), 1.5 (2D)</td>
</tr>
<tr>
<td>Molar Volume</td>
<td>$V_{M}$ [cm³/mol]</td>
<td>12.27 a</td>
</tr>
<tr>
<td>Interface energy</td>
<td>$\sigma_{\alpha \gamma^{\prime}}$ [J/cm²]</td>
<td>$0.14 × 10^{-4}$ b</td>
</tr>
<tr>
<td></td>
<td>$\sigma_{\alpha \gamma}$ [J/cm²]</td>
<td>$0.35 × 10^{-4}$</td>
</tr>
<tr>
<td></td>
<td>$\gamma^{\prime}/\gamma$ [J/cm²]</td>
<td>$0.31 × 10^{-4}$</td>
</tr>
<tr>
<td>Permeability</td>
<td>$P_{\alpha \gamma}$ [cm³/Js]</td>
<td>$\frac{8M_{\gamma}}{a\eta}$</td>
</tr>
<tr>
<td>Lattice Parameter</td>
<td>$a$ [Å]</td>
<td>3.5 c</td>
</tr>
<tr>
<td>Interface width</td>
<td>$\eta$ [nm]</td>
<td>6 (1D), 4.5 (2D)</td>
</tr>
<tr>
<td>Atomic mobility of $\alpha$</td>
<td>$M_{\alpha}$ [cm⁵/Js]</td>
<td>$0.4314 × 10^{-5}$</td>
</tr>
<tr>
<td>Atomic mobility of $\gamma$</td>
<td>$M_{\gamma}$ [cm⁵/Js]</td>
<td>$0.6420 × 10^{-5}$</td>
</tr>
<tr>
<td>Atomic mobility of $\gamma'$</td>
<td>$M_{\gamma'}$ [cm⁵/Js]</td>
<td>$0.7991 × 10^{-5}$</td>
</tr>
<tr>
<td>Diffusivity of $\alpha$</td>
<td>$D_{\alpha}$ [cm²/s]</td>
<td>$0.2704 × 10^{-10}$</td>
</tr>
<tr>
<td>Diffusivity of $\gamma$</td>
<td>$D_{\gamma}$ [cm²/s]</td>
<td>$0.0901 × 10^{-10}$</td>
</tr>
<tr>
<td>Diffusivity of $\gamma'$</td>
<td>$D_{\gamma'}$ [cm²/s]</td>
<td>$0.0901 × 10^{-10}$</td>
</tr>
<tr>
<td>Interface mobility</td>
<td>$\mu_{\alpha \gamma}$ [cm⁴/Js]</td>
<td>$0.4384 × 10^{-18}$</td>
</tr>
<tr>
<td>Young modulus of $U$</td>
<td>$E_{U}$ [GPa]</td>
<td>114</td>
</tr>
<tr>
<td>Young modulus of $Nb$</td>
<td>$E_{Nb}$ [GPa]</td>
<td>57.786</td>
</tr>
<tr>
<td>Poisson coef. of $U$</td>
<td>$v_{U}$</td>
<td>0.36</td>
</tr>
<tr>
<td>Poisson coef. of $Nb$</td>
<td>$v_{Nb}$</td>
<td>0.45</td>
</tr>
<tr>
<td colspan="3">$^{a}$Approximate average of $\alpha$-U and $\gamma$-U-50 at.% Nb molar volumes (taken from the EMTO data).</td>
</tr>
<tr>
<td colspan="3">$^{b}$Approximate averages of $\sigma_{\alpha \gamma}^{D P}$ and $\sigma_{\alpha \gamma}^{D C}$ reported in [8].</td>
</tr>
<tr>
<td colspan="3">$^{c}$Effective lattice parameter of choice, corresponding to $V_{M}$.</td>
</tr>
</tbody>
</table>

![](./images/812670390399664129_3.jpg)

Fig. 2. Schematic representations of diffusion-couple simulations to investigate the LE between $\alpha$ and $\gamma$.

The interfacial mobilities are chosen according to our empirical formula: $\mu=s \frac{D_{i} M_{i}}{D_{i}+M_{i}}$, where $s=10^{6}$ is a scaling factor, $i$ indicates either $\alpha$ or $\gamma, M$ is the value of atomic mobility, and $D$ is the value of interdiffusivity. Here, the atomic mobility and interdiffusivity of $\gamma$ are taken from the previously assessed DICTRA database [31]; basing on the atomic packing factors of orth and bcc, it was assumed that the atomic mobility and diffusivity of $\alpha$ are three times faster than those of $\gamma$; since these kinetic coefficients do not affect the thermodynamic LE between the two reacting phases, their precise values are of only peripheral interest within the scope of this work. Nevertheless, it is noted that kinetic factors can play an important role in determining the lamellar microstructure of DP, as demonstrated later in this work; therefore a comprehensive knowledge of these physical quantities is beneficial for future developments and applications of the nuclear material.

Simulation results of the phase-field diffusion couples at $450{^\circ}C$ and $550{^\circ}C$ are shown in Fig. 3(a) and (b). Here, the 3-D plots represent the evolution of the diffused $\alpha/\gamma$ interface with respect to spatial distance (x-axis), time (y-axis) and composition (z-axis). The solid (green) lines with arrows in the 3-D plots indicate the evolutionary path (and

![](./images/812670390399664129_4.jpg)
![](./images/812670390399664129_5.jpg)

Fig. 3. Phase-field investigations of possible LE between $\alpha$ and $\gamma$ at (a) 450 °C, (b) 550 °C, and at (c, d) 605 °C. Here, the $\alpha$-growing/ $\gamma$-shrinking processes of diffusion couples occur from right to left of the figures; the insets are the projections of the 3-D evolutionary paths of $c_\gamma^{int}$ on the 'Mole fraction of Nb at.%' – 'Distance' plane and their colors indicate the magnitudes of the average chemical driving forces, $\triangle g_{\alpha\beta}^\phi$, at the interface along these paths.

directions) of the composition of $\gamma$ at the interface ($c_\gamma^{int}$) during the phase transformation. The insets feature the average chemical driving force, $\triangle g_{\alpha\beta}^\phi$, at the diffusion-couple interface plotted as a function of $c_\gamma^{int}$ and the position of the interface (for details about $\triangle g_{\alpha\beta}^\phi$ please check [17]). The color within the insets shows the order of magnitude of the chemical driving force (note that non-zero driving force is only located around the projection of the evolutionary path of $c_\gamma^{int}$ on the distance – composition (x–z) plane and that since the initial setups of the diffusion-couple simulations are out-of-equilibrium all average chemical driving forces at the beginnings of the simulations are non-zero).

It can be seen from Fig. 3 that after the evolution time is larger than $1.0 \times 10^{14}$ (s) for 450 °C or $2.0 \times 10^{11}$ (s) for 550 °C the Kirkendall interface stops moving; the interface's chemical driving force, $\triangle g_{\alpha\beta}^\phi$, vanishes (see insets); and, the compositions in both $\alpha$ and $\gamma$ reach their homogeneous values across the phase regions. These all indicate that the interface dissipation model has found, for each temperature, one LE, at which the $\gamma$ composition is identical to that of the stable $\gamma_2$ (79 at.% Nb for 450 °C and 76 at.% Nb for 550 °C as in [31]). We note that:

- The sluggish evolution time (of orders $10^{14}$ (s) for 450 °C and $10^{11}$ (s) for 550 °C) results from the estimated CALPHAD's slow bulk diffusivity (in orders of $10^{-23}$ [$cm^2/s$] for 450 °C and $10^{-21}$ [$cm^2/s$] for 550 °C [31], consistent with the experimental values from Peterson and Ogilvie [33,34]). In reality, the reaction happens much faster due to the fast boundary-diffusion condition at the reaction front of DP [7] as evidenced by the measured interphase boundary diffusivity triple products in [8].
- The sudden increase in $\triangle g_{\alpha\beta}^\phi$ from 40 to 60 at.% Nb for both simulation cases (red areas in insets) corresponds to the period within which $c_\gamma^{int}$ evolves through the center of the unstable region of the bcc miscibility gap. The significant driving force within this region causes $c_\gamma^{int}$ to quickly leave the unstable region for the following low-energy area of the $\gamma_2$ LE, creating essentially two noticeable necking points: one around 30 at.% Nb (vicinity of the first inflection point) and the other around 60 at.% Nb (vicinity of the second inflection point), along the evolutionary path of $c_\gamma^{int}$ for both simulation cases.

Further phase-field investigations of $\alpha - \gamma$ LE for both 450 °C and 550 °C with initial compositions of $\gamma$ higher than $\gamma_2$ all showed a convergence back to the same equilibrium state at $\gamma_2$. This essentially indicates that within the CALPHAD energy landscape at 450 °C and 550 °C the orthorhombic phase, $\alpha$, only forms with the bcc phase, $\gamma$, one LE which corresponds to the stable $\alpha + \gamma_2$ products of the monotectoid decomposition; no LE can be found at the intermediate composition of $\gamma'$ as hypothesized by Djuric. As a matter of fact, it is found that single

LE, i.e. $\alpha + \gamma_2$, is a common phenomenon throughout the temperature interval between 400 °C and 600 °C (actually up to 605 °C), within which Djuric's experiments were carried out.

Interestingly enough, we found that, within the higher temperature range from 605 °C to 647 °C, the CALPHAD energies do form two LE with each other and the first LE does lead to the thermodynamic state of DP, very much consistent with Djuric's proposed mechanism. The simulation results of the phase-field diffusion couple at 605 °C are shown in Fig. 3(c) and (d). As evidenced by this figure, the interface dissipation model finds two LEs: one at an intermediate $\gamma'$ composition of 24.49 at.% Nb, as shown in Fig. 3(c), and the other at the stable $\gamma_2$ composition of 73.95 at.% Nb, as shown in Fig. 3(d). There exists a region in Fig. 3(d) in which the chemical driving force is negative and an external driving force has to be artificially introduced to compensate for the negative value and to get the diffusion-couple system to evolve; the significance of this negative driving force is elucidated as follows. Within the framework of phase-field modeling, the process of finding the LE at 605 °C progressed as follows:

- First, phase-field diffusion couple was started with the initial composition of $\gamma$ at 13 at.% Nb. After the evolution time was greater than $2 \times 10^{11}$ (s), it was observed that the Kirkendall interface stopped moving, $\triangle g_{\alpha \beta}^{\phi}$ converged to a value of almost 0 J/mol, and the compositions within the bulk phases reached their homogeneous states. In other words, the interface dissipation model found the system's first (or intermediate) LE whose $\gamma$'s composition was 24.49 at.% Nb. Note here that the $\triangle g_{\alpha \beta}^{\phi}$ distribution along the evolutionary path of $c_{\gamma}^{int}$ and correspondingly the morphology of the path (inset of Fig. 3(c)) are different from those at lower temperatures (see insets of Fig. 3(a) and (b)); in particular, they do not exhibit unusual peak (red in color) and necking points along the evolution process respectively; this is due to the fact that $c_{\gamma}^{int}$ has not yet passed through the first inflection point of the bcc miscibility gap to enter the gap's unstable region. Further prolonging the simulation did not lead to any significant changes. The almost-zero $\triangle g_{\alpha \beta}^{\phi}$ at the found LE results in the system becoming trapped in this metastable state.
- In order to break this stasis and continue the phase-field investigation of $\alpha - \gamma$ LE, the composition of $\gamma$ was slightly shifted to a higher value while keeping the composition of $\alpha$ unchanged. The simulation now showed that, within this small deviation, the system tended to converge back to its initial LE. This was because here $\triangle g_{\alpha \beta}^{\phi}$ had negative values which tended to reverse the compositional increment in order to bring down the system's total energy. In other words, there existed a finite energy barrier after the first LE which tentatively prevented the system from further evolving to higher $\gamma$-composition after the first LE. This energy barrier together with the vanishing driving force (as described above) form an effective twofold obstacle which proceeds to interrupt the monotectoid decomposition and cause DP to become a stabilized microstructure product.
To force the system to overcome the energy barrier, a positive driving force was artificially introduced into the reacting interface in order to counter the negative value of $\triangle g_{\alpha \beta}^{\phi}$ when it was observed. This artificial driving force could in reality be legitimated by the fact that the relaxation of internal stresses (due to volume/strain mismatch) between $\alpha$ and $\gamma$ lamellae (with $\gamma'$ composition) after some sufficient aging time, will essentially break down the first LE between $\alpha$ and $\gamma$ (by altering their free energies to lower values) and likely put the system into an out-of-equilibrium condition with non-trivial thermodynamic driving force to continue evolving in the DC manner [9,8]. During the introduction of this artificial driving force, it was observed that the peak of the energy barrier that the system had to overcome was about 18.65 $J/mol$, as shown in Fig. 4.
- When $\triangle g_{\alpha \beta}^{\phi}$ turned positive, the artificial driving force was removed to allow the evolution of the system to resume as normal. At this moment, the system had already entered the unstable region of the bcc miscibility gap. The driving force here was so significant that it dramatically drove the system almost instantaneously out of the unstable region (inset of Fig. 3(d)). When the system's $c_{\gamma}^{int}$ passed through the second inflection point of the miscibility gap, $\triangle g_{\alpha \beta}^{\phi}$ started converging and eventually brought the system to its second LE located at the $\gamma_2$ composition of 73.95 at.% Nb. Note here that the entire process after the DP reaction (the first LE) practically represented the later DC reaction: $\alpha + \gamma' \rightarrow \alpha + \gamma_2$ [9,8]. After this, the system again stayed idle at the $\gamma_2$ LE. Further phase-field investigations at higher $\gamma$-compositions did not result in any additional LE. The interface dissipation model found a total of two LE between $\alpha$ and $\gamma$ in comparison to only one LE in the previous findings at lower temperatures.

![](./images/812670390399664129_6.jpg)

Fig. 4. Energy barrier introduced by the intermediate local equilibrium after the $\gamma'$ composition to hinder the discontinuous monotectoid decomposition. Note that negative average driving force at the interface, $-\triangle g_{\alpha \beta}^{\phi}$, is reported in this figure.

To confirm this, an additional minimization was implemented in MATLAB to double check the number of LE between $\alpha$'s and $\gamma$'s CALPHAD free energies. The minimization is conventionally done with respect to composition at a specific temperature. The size of compositional domain for each LE search is controllable, and the considered temperatures are from both 400 °C-605 °C and 605 °C-647 °C ranges. It was found that the CALPHAD free energies of $\alpha$ and $\gamma$ indeed form two LE with each other within the temperature range of 605 °C-647 °C while they exhibit only one LE within the temperature range of 400 °C-605 °C, which is consistent with the phase-field investigations.

The observation of two LE between $\alpha$ and $\gamma$ within the temperature range of 605 °C-647 °C tentatively indicates that Djuric's hypothesis is a possible explanation for the origin of U-Nb's discontinuous monotectoid decomposition Yet, this indication is not conclusive due to the fact that the CALPHAD free energies show only one LE within 400 °C-605 °C. To further investigate this, we revisited in the following the CALPHAD free energies of $\alpha$ and $\gamma$ within the temperature range between 400 °C and 605 °C.

### 3.2. Phase stabilities from a thermodynamic perspective: strain effect

#### 3.2.1. Strain energy

As a first simple attempt, we empirically sketched out new energetic profiles based on the CALPHAD free energies and following Djuric's proposal [9]. For this, a piecewise cubic polynomial with ten knots was used. This polynomial allowed the accurate fitting of the CALPHAD free

![](./images/812670390399664129_7.jpg)
![](./images/812670390399664129_8.jpg)

Fig. 5. Proposed strain-adjusted free energies of $\alpha$ and $\gamma$ at $450\ ^{\circ}\text{C}$ (a) and $550\ ^{\circ}\text{C}$ (b), plotted with reference to orth-U and bcc-Nb. Here, since additional strain energy was assumed to be insignificant in $\alpha$, the phase's proposed free energies were chosen to be the same as CALPHAD free energies to simplify the effort. Notice that the proposed free energies form two common tangents with each other. These strain-adjusted free energies can be seen as the realization of Djuric's hypothetical free energies via CALPHAD methodology.

energies around the compositions corresponding to the $\alpha$ and $\gamma_{2}$ equilibrium states while at the same time allowing for fine-tuned modifications of the bulk free energies within the metastable region of the $\gamma$ phase. The resulting energies for $450\ ^{\circ}\text{C}$ and $550\ ^{\circ}\text{C}$ are shown in Fig. 5. As demonstrated in this figure, the empirical estimations indicated that Djuric's hypothesis holds when the non-equilibrium energies around the lump of the bcc ($\gamma$ phase) miscibility-gap is slightly or moderately increased. Such positive contributions to the free energy of a phase may arise from elastic contributions, which led us to the following considerations:

- In the case of U-Nb's discontinuous monotectoid decomposition, due to the volume mismatch ($\sim$1%-15%) between $\alpha$ (20.8625 $\mathring{\text{A}}^{3}$/Atom [35]) and $\gamma$ (18.10 (pure Nb) – 20.65 (pure U) $\mathring{\text{A}}^{3}$/Atom [36] ), there exists a stress/strain field at around the interfacial region between the two phases. This stress/strain field is distributed around the lamellae where discontinuous monotectoid decomposition happens and thus such contributions cannot be ignored.
- CALPHAD free energies tend to be assessed for phases under bulk conditions in which interfacial effects can be safely ignored. In the case of the cooperative growth of $\alpha$ and $\gamma$ lamellaes, interfacial effects arising, for example, from coherency or elastic mismatch cannot be neglected, particularly during the initial stages of the microstructure evolution as the microstructural length scales tend to be quite small. In such cases, additional energetic contributions arising from interfacial effects must be explicitly taken into account.
- Since the energy raising from volumetric strain tends to be smaller at higher temperature (due to thermal relaxation), it is possible that the CALPHAD bulk energies can account for this energy under high temperature conditions, which is consistent with the observations of two LE within the $605\ ^{\circ}\text{C}$–$647\ ^{\circ}\text{C}$ range. In contrast, at lower temperature the (residual) strain energy tends to be larger and this tends to push the system out of the regime in which we can assume bulk thermodynamics to dominate.

Combining the above considerations, it may be possible that volumetric strain plays an important role in the stabilization of the intermediate $\gamma'$ phase during the discontinuous reaction. In this respect, a deviation is observed due to the fact that CALPHAD only accounts for bulk energies without accounting for interfacial energies and/or elastic energies at temperatures ranging from $400\ ^{\circ}\text{C}$ (and possibly lower) to $605\ ^{\circ}\text{C}$. Djuric's proposed phenomenological free energy may indeed arise from these contributions. To further investigate the possibility of this hypothesis, the elastic contribution of misfit strain is accounted for in an approximated manner assuming linear elastic contributions to the bulk free energy of the system.

Here, we make the following assumptions. First, we assume, that since $\gamma$ is a Nb-rich precipitate, it is considerably softer than $\alpha$ due to niobium's high ductility. Accordingly, the $\gamma$ phase gets strained more than the other phases. Second, we assumed that the lattice parameter of the soft(er) phase follows Vegard's law, albeit it was previously reported via first-principles calculations a small nonlinear behavior [31]. We assumed further that there are no shear components at the interface. By applying the fourth-rank stiffness tensor to the linear elasticity [37], the elastic stresses read:

$$\sigma_{zz}=0 \tag{11}$$

$$\sigma_{xx,yy}=\frac{E}{1-\nu}\epsilon_{xx,yy} \tag{12}$$

$$\sigma_{xy}=\sigma_{yz}=\sigma_{zx}=0 \tag{13}$$

where $\nu$ is the Poisson's ratio and $E$ is the Young's modulus. It follows that [38-40]:

$$
\begin{aligned}
f_{elas}&=\frac{1}{2}\int_{V}\sum_{i,j}\sigma_{ij}\epsilon_{ij}dV \\
&=\frac{E}{2(1-\nu)}\int_{V}\left(\epsilon_{xx}^{2}+\epsilon_{yy}^{2}\right)dV
\end{aligned} \tag{14}
$$

Since the elastic energy is in a quadratic form that implies small strains, it is expected to underestimate/overestimate the response of the system under high tensile/low compressive strain [39,40]. To identify the limit at which this approximation becomes less reliable, the cohesive energetic response of the $\gamma$ phase was investigated using the Exact Muffin Tin Orbital method [41]. The results in which the first-principles energy-strain responses are compared with the linear elastic behavior are reported in Fig. 6 at the compositions of 0, 50, and 100 at.% Nb. Here, for simplicity the quadratic approximation relating energy to strain are realized by using the data located within the proximity of the calculated cohesive curves. It is noted that the reported lattice parameters coincide with the entire atomic fraction of $\gamma$, i.e. from pure Nb on the left terminal to pure U on the right terminal of Fig. 6. As can be seen from this figure, the approximation works best within the vicinity of 50 at.% Nb and tends to deviate from this behavior near the endmembers (less profound for equiatomic $\gamma$ but noticeable in the low- and high-Nb $\gamma$). Generally speaking, it is expected to be qualitatively acceptable within $\pm\ 30\%$ lattice deviation which is correspondent to $\pm\ 30$ at.% Nb deviation from the $\gamma$'s composition at which the lattice

![](./images/812670390399664129_9.jpg)

Fig. 6. Validity of the approximation used for the strain energy within the considered range of lattice parameter of $\gamma$.

misfit between $\alpha$ and $\gamma$ is smallest.

It is also noted that the estimation of strain energy requires the identifications of habit planes between $\alpha$ and $\gamma$, which allows the estimation of misfit strain in Eq. (14). When the lattice parameters change with changing composition during the diffusion reaction, the identification of habit planes is composition dependent. This excludes the convenient adaptation of the $(111)_{\gamma} \|(200)_{\alpha}$ habit plane of U-7.5Nb-2.5Zr [42] not only due to the alloy's fixed composition but also due to its different lattice parameters as compared to those of the binary alloy. Since $\alpha$ is assumed earlier to not undergo misfit deformation and it does not deform by change of composition ($\alpha$'s composition appears almost constant [8]), this process reduces to a simpler case in which only the lattice parameter of $\gamma$ varies (during solute diffusion).

### 3.2.2. Minimal-deformation plane

To identify the habit planes between $\alpha$ and $\gamma$ phases, we follow the principle of invariant lines [43] which assumes that the common line between matrix and precipitate lattices is the favored nucleation site of the precipitate. To avoid the cases in which the rotation required to match the common lines between precipitate and matrix lattices results in a large strain along the other direction that forms the matrix-precipitate interface with the common line, we require further that this direction is also an invariant line. In other words, an invariant plane as habit plane. Such invariant planes, however, rarely exists in practice. There exists instead common planes between matrix and precipitate with minimal lattice deformations. This results in a new approach, which we name minimal-deformation plane. This approach although being less (physically) constrained is more practical than the invariant-plane (or ideal common-line) approach. The proposed numerical algorithm to identify minimal-deformation planes is summarized in Table 2, and is as follows:

First, super lattices are defined for the reacting structures. Here, we define the supercells of $2 \times 2 \times 2$ (2X), $3 \times 3 \times 3$ (3X), and $4 \times 4 \times 4$ (4X) for both $\alpha$ and $\gamma$ structures; and the cases of $(2X)_{\alpha} \|(2X)_{\gamma}$, $(2X)_{\alpha} \|(3X)_{\gamma}$, $(3X)_{\alpha} \|(3X)_{\gamma}$, and $(4X)_{\alpha} \|(4X)_{\gamma}$ are considered. The lattice parameters of $\alpha$ are collected from literature recorded in the ICSD database. For lowering computational expense, only the minimum, maximum, and mean values of the lattice parameters are considered for the evaluations of habit planes. The composition-dependent lattice parameters of $\gamma$ are adapted from Jackson's experiments [44]. Before selection, all parameters are converted to the same investigated temperature, hereinafter $450\ ^{\circ}\text{C}$, using the thermal expansion coefficients taken from [45,46].

<table>
<caption>Table 2 Algorithm: Minimizing misfit strain.</caption>
<tbody><tr><td colspan="2">Algorithm: Minimal-deformation plane</td></tr>
<tr><td>1.</td><td>Define super-lattices/supercell: lattice parameters and uncertainties chosen according to:
<br>Experimental (ICSD**) min, mean, and max values
<br>Temperature dependency accounted.</td></tr>
<tr><td>2.</td><td>Find minimal-deformation plane
<br>Establish 2 triangles, each defined arbitrarily by 3 atoms in corresponding super lattice (ie. establish lattice plane.).
<br>Compare 3 edges of one triangle (bcc) to those of another (orth), ie. shortest to shortest and longest to longest.
<br>Estimate planar misfit as total edge-misfit (note: translational and rotational matching throughout the interface is inherent).
<br>Repeat until lowest planar mismatch</td></tr>
<tr><td>3.</td><td>Estimate elastic energy: according to edge mismatches.</td></tr>
<tr><td>**</td><td>ICSD stands as Inorganic Crystal Structure Database.</td></tr>
</tbody></table>

Second, a triangle defining an interface within each super lattice is selected. Three edges of the triangle are estimated and compared to those of the other triangle in a sorted order. The pair of triangles with the lowest summation of squared edge mismatches is corresponds to the habit planes. To avoid the case in which minimal misfit exists for the smallest cells containing the triangles but not repeatable throughout the interface, planar periodic condition is enforced for each considered triangle. This is done not based on the original (3D) lattice references – which essentially gives rise to the need for explicit consideration of coupled translational and rotational degrees of freedom – but on (2D) references defined by the triangles themselves – which inherently imposes the translational and rotational matching throughout the interface.

### 3.2.3. Stochastic elastochemical energies

The Young's moduli were adapted from Jackson's experiments [47]. The resulting stochastic elastochemical energies are reported in Fig. 7 for the cases of $(2X)_{\alpha} \|(2X)_{\gamma}$, $(2X)_{\alpha} \|(3X)_{\gamma}$, $(3X)_{\alpha} \|(3X)_{\gamma}$, and $(4X)_{\alpha} \|(4X)_{\gamma}$. As can be seen from Fig. 7, the estimated elastic energies are higher for smaller cells. For the case of $(2X)_{\alpha} \|(2X)_{\gamma}$ the elastochemical energies are so high that even the stable $\gamma$ is hardly observable. $(2X)_{\alpha} \|(2X)_{\gamma}$ is as such not the system's preference and is subjected to further transformation to other habit planes of lower energies. Within the current analysis, these habit planes are $(2X)_{\alpha} \|(3X)_{\gamma}$, $(3X)_{\alpha} \|(3X)_{\gamma}$, and $(4X)_{\alpha} \|(4X)_{\gamma}$; the energy gain is considerably large for the former but not much so for the latter. Here, the reason for these lower energies is that the chance to find habit planes with smaller and smaller lattice misfit increases as more and more atoms are considered. These planes, however, are inevitably larger in matching units (i.e., the smallest misfit area between two periodic habit planes) and likely give rise to a larger barrier which the system has to overcome. Such barrier is not easy to assess; and for this reason, we choose $(2X)_{\alpha} \|(3X)_{\gamma}$ (Fig. 7(b)) and $(3X)_{\alpha} \|(3X)_{\gamma}$ (Fig. 7(c)) as, intuitively, the most likely habit planes among the predicted habit planes.

Along each elastochemical energy, there exists many energy valleys that are stabilized by local elastic strain. Of these energy valleys, many form common tangent with the $\alpha$ lamella at intermediate compositions and as such can be subjected to DP. This indicates that (composition-dependent) elastic strain can affect the system's thermodynamic properties. Analogous to phase transformation, the inflection points along each energy correspond to (first-order) transitions from one set of habit planes to another set of habit planes. Since these points locate within the accepted bounds of $\pm 30$ at.% Nb, the used approximations to account for strain energy effects are acceptable, according to the above analysis. It is noted here that the energies required for the interface transformations are relatively small, i.e. in order of a few kJ/mol taking both elastic (refer to Fig. 7) and interfacial energies (refer to [8]) into account, making the transformations competitive to dislocation

![](./images/812670390399664129_10.jpg)

Fig. 7. Elastochemical energy of $\gamma$ assuming that the mechanically stronger $\alpha$ lamella does not undergo any strain. Here, each elastochemical energy curve (e.g. the solid red curves ) within the uncertainty band (i.e. filled area) composes of different local valleys. Each local valley corresponds to an estimated habit system that is lowest in strain energy. Each necking point along the curve represents the (1st order) transformation that is associated with the transformation from one habit system to another when Nb content redistribute during DP. Note that the calculation of strain energy here only accounts for the misfit strain; and as such it favors habit system with larger (2-D) unit cells as these cells possess smaller misfit lattices; in practice, larger misfit unit cells would require higher formation energies, which could prevent a habit-plane structure from transformation to another structure along the diffusion path; estimation of such formation energy is unfortunately not simple.

formation¹ which would otherwise arise due to the same need of relaxing excess strain.

As evidenced by Fig. 7(b) and (c), there is a wide spectrum of elastochemical potentials, each results from one set of lattice parameters, and they all differ thermodynamically from each other. This emphasizes again that elastic strain plays an important role in the thermodynamic properties of the system. Among the predicted potentials, it is noted that many curves do not appear to promote energy valleys that could be related to DP. These are believed to result from the overestimation of elastic energy due to the use of first-principles (0 K) moduli. It is expected that these energies should be lower in practice and would as such show intermediate energy valleys corresponding to phases that are more stable than $\alpha$ . Such valleys increase the chance of having intermediate common tangents between $\alpha$ and $\gamma$, which in turn gives rise to the formation and growth of the intermediate $\gamma$ precipitate.

As such, we categorize the predicted potentials into two phenomenological groups. The first group (Group I) is characterized by weak elastic mismatch corresponds to the hypothetical energetics proposed by Djuric shown in Fig. 5. The energy valley in this group can either accommodate both the matrix and intermediate $\gamma$ compositions as in Fig. 7(c) or only the composition of the precipitate leaving the lower matrix composition at a another energy valley as in Fig. 7(a) (note that the $\alpha$'s a lattice parameter is smaller here than in the first group). As temperature increases, such an energy valley will promote a gradual increase in the intermediate $\gamma$ composition as the common tangent between this precipitate and the $\alpha$ precipitate will move towards higher Nb content. On the contrary, the second group (Group II) is characterized by two energy valleys: one is located near the equiatomic composition and the other is near the composition of the matrix. The potentials belong to this group are mainly distributed in Fig. 7(a) or (b) and are the results of a large difference in lattice parameter values. This group of elastochemical free energies leads to DP products with a $\gamma'$ composition close to 50% at. are in agreement with Hackenberg's earlier observation. Fig. 8 demonstrates a series of alternative elastochemical energies that are extracted from Fig. 7.

---
¹ The energy required for forming a dislocation, $F \approx Gb/A$ where $G$ [48] is shear modulus, $b$ is burger vector, and $A$ is molar area, is in the order of 10–100 kJ/mol·atom (depending on the composition of $\gamma$) given the <111> slip directions and two atoms reside along the burger vector

### 3.3. 2D kinetic study of evolution of phases: phase-field results

To further elucidate the influence of these elastochemical interactions on the microstructure evolution of DP, phase-field simulations are

![](./images/812670390399664129_11.jpg)

Fig. 8. Energy diagram for the case where an elastochemical local energy valley resides within the vicinity of 50 at.% Nb. This energy valley corresponds to the energy of the $\gamma$ precipitate. It forms (1) a common tangent with the free energy of the $\alpha$ precipitate and (2) a common tangent with $\gamma$ matrix's energy valley (which also belongs to the same elastochemical energy curve as that of the $\gamma$ precipitate). These two tangents define local equilibrium at the $\alpha$-$\gamma$ precipitate and $\gamma$ precipitate $-\gamma$ matrix respectively. At the interface between $\alpha$ precipitate and $\gamma$ matrix, the tangent can be either common tangent or parallel tangent, depending on the height of the matrix's energy valley. Together, these tangents govern DP's kinetic reaction.

conducted assuming two forms of thermodynamic inputs, 1) hypothetical group I similar/close to energetics proposed by Djuric shown in Fig. 5(a), 2) hypothetical group II shown in Fig. 8. In addition, for each case we investigate two common DP's kinetic conditions, 1) volume-diffusion-controlled [49] and 2) boundary-diffusion controlled [7,6]). The energy values of the $\gamma$ phase are approximations to the local valleys at around 20 at.% Nb and 45 at.% Nb of the highlighted elastochemical energy in Fig. 7(b).

For the case of volume-diffusion-controlled DP, interfacial diffusivities are chosen to be equal to bulk diffusivities, taken from the recent assessment [31]. For the case of boundary-diffusion-controlled, the bulk diffusivities are again taken from [31], the interfacial diffusivities at the reaction front/grain boundary are derived from the experimental interphase boundary diffusivity triple product $sD\delta$ [8], where $s$ is the segregation factor at the interface, $D$ is the needed diffusivity, and $\delta=1$ (nm) is interfacial width. Finally, the diffusivities at $\alpha/\gamma'$ interface are chosen to be $\sim10^{3}$ times smaller than those at the reaction front [19,20]. The size of the simulation domains are denoted in the caption of each result, and these reflect physical length scale of the system as measured in [8]. The initial domain consists of two $\alpha$ lamellae and two $\gamma$ lamellae whose compositions and sizes follows the LE partition in both cases. The boundary conditions are set to be periodic in left/right and no flux in top/bottom side of the domain.

Simulation results that use the Group I elastochemical free energies, featuring an energetic valley far below the equiatomic composition are illustrated in Fig. 9. The two groups shown in Fig. 9 correspond to volume-diffusion-controlled regime shown in Fig. 9(a and b) and boundary-diffusion-controlled regime shown in Fig. 9(c and d), respectively. In the former case, the $\gamma'$ phases are unable to grow and DP reaction is not observed. As can be seen from these figures, the initially nucleated $\alpha$ precipitates eventually impinge and coalesce while the $\gamma'$ precipitates fade out. The reason for this is that at the interface between the $\gamma$ matrix and $\gamma'$ lamellae there occurs a down-hill diffusion between the two bcc phases, i.e. a Nb flux flows from $\gamma'$ to $\gamma$.

This flux (vertical flux) dissipates a considerably large amount of Nb content out of the $\gamma'$ lamellae. Note that relative to this flux, there exists another flux (lateral flux) that flows along the tips of the $\alpha$ lamellae (due to the curvatures/gradients of these lamellae along the reaction front) and, in the opposite way, adds more Nb content to the $\gamma'$ lamellae to grow them. In this case the latter lateral flux is slower than the vertical flux and not able to sustain the Nb content within the $\gamma$ lamellae near its LE value. This essentially breaks down the equilibrium between the $\alpha$ and $\gamma'$ lamellae, allowing the $\alpha$ lamellae to expand into the $\gamma'$ lamellae until impingement. The evolving system therefore does not exhibit DP, and in this case an assumption resting only on the features of the bulk free energy of the $\gamma$ phase (as per Djuric's phenomenological model) does not seem to be sufficient to stabilize the metastable $\gamma'$ product.

On the contrary, the DP reaction is observed only when we imposed boundary-diffusion-controlled kinetics. In the case of the boundary-diffusion-controlled regime, the Nb-flux flowing into the $\gamma'$ lamellae from the tips of the $\alpha$ lamellae is much more significant than the Nb-flux flowing out of the $\gamma$ lamellae due to the down-hill diffusion. In other words, there is not much Nb leakage from the $\gamma$ lamellae into the $\gamma$ matrix and its LE state with the $\alpha$ lamellae is sustained during the reaction.

Analysis of the driving force at the $\alpha/\gamma'$ interfaces shown in Fig. 9(e) supports this observation. Accordingly, the driving force distributed at the $\gamma'/\gamma$ reaction front is considerably smaller than that at the $\alpha/\gamma$ interface. The existence of this driving force during down-hill diffusion is found to be in good agreement with Hillert's theory [25,26], which states that the driving energy for the growth of $\gamma'$ grain is identified with some fraction of the free energy which "would be lost due to volume diffusion if certain mechanisms did not interfere" [25]. In our case, there exists such interfering mechanisms, i.e. the fast flux along the reaction front acts as resistance to the down-hill diffusion, and hence the non-trivial driving force at the $\gamma'/\gamma$ interface. However, since the driving force at the $\gamma'/\gamma$ interface is considerably smaller than that at the $\alpha/\gamma$ interface, it can be argued that $\gamma'$ would not be able to keep up with $\alpha$ if the two phases could grow separately unless their interface mobility is significantly different. In this regard, the growth of $\gamma'$ lamellae is not mainly due to the driving force at the $\gamma'/\gamma$ interface but rather the continuous Nb-supply streaming from the growth of the $\alpha$ lamellae. In any case, the result is the stable growth of $\alpha/\gamma'$ lamellae and it demonstrates the role of kinetics (i.e. fast grain-boundary diffusion) under the two-local-equilibrium hypothesis on the origin of U-Nb's DP. Apparently, for the DP to happen within this assumption, both thermodynamics and kinetics play a role, with the latter being more important than former.

The simulation results for the hypothetical energy Group II (this work) are reported in Fig. 10. To investigate further, the same kinetic analyses as in the above case were conducted. As can be seen from the figure, stable growth of the intermediate $\gamma$ lamellae can be achieved for both volume-diffusion controlled and boundary-diffusion controlled regimes. Similarly to a eutectoid decomposition, the reason for this is because the reaction is mainly governed by the system's thermodynamics, i.e. equilibrium is well defined at all interfaces of the reaction. The difference though is that instead of having static global equilibria the system is trapped at local energy valleys along the dynamical decomposition from its initial matrix composition to a final stable $\gamma_2$, i.e. similar to that demonstrated above in the 1-D phase-field analysis. Also, in the current phase-field analysis, the interface between $\alpha$ precipitate and $\gamma$ matrix is specially defined by a parallel tangent rather than the usual common tangent. This parallel tangent always leaves the interface out of equilibrium and as such there always exists a driving force to grow the $\alpha$ precipitate. This would also enhance the growth of the $\gamma'$ via the faster Nb flux stemmed from the $\alpha$'s growth, essentially enhancing DP's overall growth rate. In the typical case when three common tangents exist between the phases - which may be missed due to existing uncertainty and used approximation, the growth would happen in a much more stable manner but at a slower rate. The role of kinetics in the stabilization of the metastable $\gamma$ phase as well as its (thermodynamically) stable growth is rather trivial. However, it

![](./images/812670390399664129_12.jpg)

affects the growth rate of the reaction and the morphologies of $\alpha$ and $\gamma$ phases, e.g. as shown in Fig. 10(a) and Fig. 10(b). Given as well that the incubation time for the nucleation of the stable $\gamma$ is longer than that of the intermediate $\gamma$ phase (due to its higher composition), the nucleation and (stable) growth of the intermediate $\gamma$ is expected from this (local equilibrium) thermodynamic and kinetic point of view.

It is interesting to note here that, due to the parabolic nature of the potentials within the second group (elastochemical free energies), the estimated composition of the intermediate phase is always found close to 50 at.% Nb composition under different aging temperatures. This is found to be in good qualitative agreement with the recent XRD measurements [8] on U-13Nb and U-17Nb aged at $450\ ^{\circ}\text{C}$ which show 54 and 55 at.% Nb, respectively. Fig. 10(c) shows a SEM image of U-7.5Nb (at.%) reacted at $450\ ^{\circ}\text{C}$ for 1000 min, depicting the well-defined DP lamellar structure and growth fronts. Given longer aging times, the entire microstructure is consumed by this DP reaction, with no signs of reversion of the DP product. For the cases when the potentials have to accommodate the compositions of both matrix and intermediate $\gamma$ precipitate phases within one energy valley (Group II), the DP reaction is not so well thermodynamically defined as in the previous case.

To remark, it is interesting to see from the above analyses how elastic strain affects in a non-trivial way the fundamental thermodynamics of the DP reaction. It is also interesting to see the reaction interface as a phase subjected to transformation and that such small changes in the lattice parameters of the reactants can alter the interface transformation path leading to a rich and rather-less-expected set of thermodynamic properties that explain experimental observations. Although the current theoretical analysis is by no means comprehensive, the authors expect that local strain's complicated relation to misfit lattices, its importance, and its impact on DP hold true in general.

### 4. Conclusion

In this work, we have investigated the discontinuous precipitation

![](./images/812670390399664129_13.jpg)

Fig. 10. Phase-field simulations at $450\ ^{\circ}\text{C}$ without (a) and with (b) fast boundary diffusion. The energy curves shown in Fig. 8 are used to reproduce these results and the initial bulk Nb concentration is 25%, used as the matrix phase ($\gamma_1$) in the calculations. Domain size is (a) $70 \times 255\ \text{nm}^2$ and (b) $70 \times 130\ \text{nm}^2$. c) SEM micrograph of U-17 at.% Nb aged $450\ ^{\circ}\text{C}$ for 1000 min showing DP colony. A magnified section of DP region is indicated in top right corner of this micrograph [Image courtesy of Pallas A. Papin, Los Alamos National Laboratory.]. For interpretation of the colors, please refer to the online version of this document. Updated Figure.

(DP) process in the U-Nb system from a thermodynamic and kinetic perspective. A major motivation for the present work is the puzzling fact that the DP product remains stable over prolonged aging condi- tions. While we showed that it is possible to stabilize the $\gamma'$ precipitate while invoking only bulk thermodynamics, our analysis suggested that local contributions arising from interfacial strains may play a very important role in this stabilization. We have found that these interfacial strain energy contributions help to stabilize the metastable $\gamma'$ phase by forming local energy valleys along the monotectoid decomposition path from initial $\gamma$ matrix to stable $\gamma_{2}$. Such energy valleys act as local traps that tend to arrest the reaction within the discontinuous-precipitation regime. The mechanism of the arrest can be strictly of (local) equili- brium nature similar to a eutectoid reaction or involve both thermo- dynamics and kinetics. We have also shown that highly anisotropic boundary diffusion can stabilize the DP front. The specific mechanism arresting the reaction within the discontinuous-precipitation regime affects the chemistry of the metastable DP product. While the available experimental data is not sufficient to deduce with absolute certainty the underlying mechanism for the stabilization of the DP process, this work has resulted in some plausible mechanisms that can be further tested with more experiments and more comprehensive characterization. Better understanding of the microstructure evolution of U-Nb alloys can potentially result in the development of better fuel forms that in turn will enable next generation reaction technology [5].

## Data availability
The data that support the findings of this study are openly available upon request if available.

## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influ- ence the work reported in this paper.

## Acknowledgments
This work was performed under the auspices of the United States Department of Energy by the Lawrence Livermore National Laboratory and Los Alamos National Laboratory under contract Nos. DE-AC52- 07NA27344 and DE-AC52-06NA25396, respectively. VA, TD and RA also acknowledge support from Lawrence Livermore National Laboratory under Collaborative R&D in Support of LLNL Missions, Task Order No. B623252 and Master Task Agmt. B575363. Thien C. Duong specially thanks Prof. Ingo Steinbach, Dr. Oleg Shchyglo, Dr. Reza Darvishi Kamachali, Matthias Stratmann, Adam A. Gießmann, and Efim Borukhovic for helpful discussions regarding phase-field theory and the interface dissipation model. Vahid Attari thanks the support by the National Science Foundation under NSF Grant No. CMMI-1462255. First-principles calculations were carried out at the Texas A&M High- Performance Research Computing Facility at Texas A&M University as well as at the Texas Advanced Computing Center at the University of Texas, Austin.

## References
[1] R. Vandermeer, Phase transformations in a uranium-14 at.% niobium alloy, Acta Metall. 28 (3) (1980) 383-393.
[2] K. Eckelmeyer, A. Romig, L. Weirick, The effect of quench rate on the micro- structure, mechanical properties, and corrosion behavior of U-6 wt pct Nb, Metall. Trans. A 15 (7) (1984) 1319-1330.
[3] H.M. Volz, R.E. Hackenberg, A.M. Kelly, W. Hults, A. Lawson, R. Field, D. Teter, D. Thoma, X-ray diffraction analyses of aged U-Nb alloys, J. Alloys Compd. 444-445 (2007) 217-225.
[4] A. Clarke, R. Field, R. Hackenberg, D. Thoma, D. Brown, D. Teter, M. Miller, K. Russell, D. Edmonds, G. Beverini, Low temperature age-hardening in U-13 at.% Nb: an assessment of chemical redistribution mechanisms, J. Nucl. Mater. 393 (2009) 282-291.
[5] M. Tałach-Dumańska, P. Zieba, A. Pawlowski, J. Wojewoda, W. Gust, Practical aspects of discontinuous precipitation and dissolution, Mater. Chem. Phys. 80 (2) (2003) 476-481.
[6] D. Williams, E. Butler, Grain boundary discontinuous precipitation reactions, Int. Met. Rev. 26 (1) (1981) 153-183.
[7] I. Manna, S. Pabi, W. Gust, Discontinuous reactions in solids, Int. Mater. Rev. 46 (2) (2001) 53-91.
[8] R.E. Hackenberg, H.M. Volz, P.A. Papin, A.M. Kelly, R.T. Forsyth, T.J. Tucker, K.D. Clarke, Kinetics of lamellar decomposition reactions in U-Nb alloys, Solid State Phenom. 172 (2011) 555-560.
[9] B. Djuric, Decomposition of gamma phase in a uranium-9.5 wt% niobium alloy, J. Nucl. Mater. 44 (2) (1972) 207-214.
[10] P. Pfeil, J. Browne, G. Williamson, The uranium-niobium alloy system in the solid state, J. Inst. Met. 87 (1958-59) 204-208.
[11] R.E. Hackenberg, M.G. Emigh, A.M. Kelly, P.A. Papin, R.T. Forsyth, T.J. Tucker, K.D. Clarke, The surprising occurrence of non-steady-state growth of divergent la- mellar decomposition products in uranium-niobium alloys: a preliminary report (Tech. rep., LA-UR-12-25218), Los Alamos National Lab.(LANL), Los Alamos, NM (United States), 2012.
[12] L.-Q. Chen, Phase-field models for microstructure evolution, Annu. Rev. Mater. Res.32 (1) (2002) 113-140.
[13] N. Moelans, B. Blanpain, P. Wollants, An introduction to phase-field modeling of microstructure evolution, Calphad 32 (2) (2008) 268-294.
[14] I. Steinbach, Phase-field models in materials science, Modell. Simul. Mater. Sci. Eng17 (7) (2009) 073001.
[15] V. Attari, R. Arroyave, Phase field modeling of joint formation during isothermal solidification in 3DIC micro packaging, J. Phase Equilibr. Diffus. 37 (4) (2016)469-480.
[16] V. Attari, S. Ghosh, T. Duong, R. Arroyave, On the interfacial phase growth and vacancy evolution during accelerated electromigration in Cu/Sn/Cu microjoints, Acta Mater. 160 (2018) 185-198.
[17] I. Steinbach, L. Zhang, M. Plapp, Phase-field model with finite interface dissipation, Acta Mater. 60 (6) (2012) 2689-2701.
[18] L. Zhang, I. Steinbach, Phase-field model with finite interface dissipation: extension to multi-component multi-phase alloys, Acta Mater. 60 (6) (2012) 2702-2710.
[19] L. Amirouche, M. Plapp, Phase-field modeling of the discontinuous precipitation reaction, Acta Mater. 57 (1) (2009) 237-247.
[20] L. Amirouche, M. Plapp, On the effect of bulk diffusion on the initiation of the discontinuous precipitation reaction: phase-field simulations, in: Solid State Phenomena, vol. 172, Trans Tech Publ, 2011, pp. 549-554.
[21] D. Turnbull, Theory of cellular precipitation, Acta Metall. 3 (1) (1955) 55-63.
[22] J.W. Cahn, The kinetics of cellular segregation reactions, Acta Metall. 7 (1) (1959)18-28.
[23] R. Fournelle, J. Clark, The genesis of the cellular precipitation reaction, Metall. Trans. 3 (11) (1972) 2757-2767.
[24] R. Fournelle, On the thermodynamic driving force for diffusion-induced grain boundary migration, discontinuous precipitation and liquid film migration in binary alloys, Mater. Sci. Eng.: A 138 (1) (1991) 133-145.
[25] M. Hillert, On theories of growth during discontinuous precipitation, Metall. Trans3 (11) (1972) 2729-2741.
[26] M. Hillert, An improved model for discontinuous precipitation, Acta Metall. 30 (8)(1982) 1689-1696.
[27] B.E. Sundquist, Cellular precipitation, Metall. Trans. 4 (8) (1973) 1919-1934.
[28] L. Klinger, Y. Brechet, G. Purdy, On velocity and spacing selection in discontinuous precipitation-I. simplified analytical approach, Acta Mater. 45 (12) (1997)5005-5013.
[29] G.R. Purdy, Interface migration in diffusional phase transformations: Thermodynamic and kinetic aspects, in: Defect and Diffusion Forum, vol. 194, Trans Tech Publ, 2001, pp. 1745-1758.
[30] J. Robson, Modeling competitive continuous and discontinuous precipitation, Acta Mater. 61 (20) (2013) 7781-7790.
[31] T.C. Duong, R.E. Hackenberg, A. Landa, P. Honarmandi, A. Talapatra, H.M. Volz, A. Llobet, A.I. Smith, G. King, S. Bajaj, et al., Revisiting thermodynamics and kinetic diffusivities of uranium-niobium with bayesian uncertainty analysis, Calphad 55(2016) 219-230.
[32] K. Karayagiz, L. Johnson, R. Seede, V. Attari, B. Zhang, X. Huang, S. Ghosh, T. Duong, I. Karaman, A. Elwany, R. Arroyave, Finite interface dissipation phase field modeling of ni-nb under additive manufacturing conditions, Acta Mater. 185(2020) 320-339.
[33] N.L. Peterson, R.E. Ogilvie, Diffusion studies in the uranium-niobium (columbium) system, Trans. Met. Soc. AIME 218 (1960) 439-444.
[34] N. Peterson, R. Ogilvie, Diffusion in the uranium-niobium (columbium) system, Trans. AIME 227 (1963) 1083-1087.
[35] W. Eeles, A. Sutton, X-ray determination of the atomic positions in alpha-uranium at 22 and 660 degree c, Acta Crystallogr. A 16 (6) (1963) 575.
[36] T.C. Duong, Integrated computational materials science and engineering for the research and development of gen-iv metallic fuels: application to uranium-niobium(Ph.D. thesis), A&M University, Texas, 2015.
[37] R.W. Balluffi, S. Allen, W.C. Carter, Kinetics of materials, John Wiley & Sons, 2005.
[38] J.W. Cahn, On spinodal decomposition, Acta Metall. 9 (9) (1961) 795-801.
[39] S.-I. Yi, V. Attari, M. Jeong, J. Jian, S. Xue, H. Wang, R. Arroyave, C. Yu, Strain- induced suppression of the miscibility gap in nanostructured Mg2Si-Mg2Sn solid solutions, J. Mater. Chem. A 6 (36) (2018) 17559-17570.
[40] V. Attari, A. Cruzado, R. Arroyave, Exploration of the microstructure space in TiAlZrN ultra-hard nanostructured coatings, Acta Mater. 174 (2019) 459-476.

[41] L. Vitos, Computational quantum mechanics for materials engineers: the EMTO method and applications, Springer Science & Business Media, 2007.

[42] A. Couterne, C. Collot, C. Guillaume, Etude de l'alliage mulberry [u-7, 5 nb-2, 5 zr (% ponderaux)]. diagramme de transformation en refroidissement continu-struc- tures et proprietes mecaniques, J. Nucl. Mater. 56 (2) (1975) 169-194.

[43] U. Dahmen, Orientation relationships in precipitation systems, Acta Metall. 30 (1) (1982) 63-73.

[44] R.J. Jackson, Reversible martensitic transformation between transition phases of uranium-base niobium alloys (Tech. Rep. RFP-1535), Dow Chemical Co., Golden, Colo. Rocky Flats Div., 1970.

[45] J. Bridge, C. Schwartz, D. Vaughan, X-ray diffraction determination of the coeffi- cients of expansion of alpha uranium, Trans. AIME 206 (1956) 1282-1285.

[46] F. Cverna, et al., ASM ready reference: thermal properties of metals, ASM Int.(2002).

[47] R. Jackson, J. Burke, Elastic, plastic, and strength properties of U-Nb and U-Nb-Zr alloys, in: Physical Metallurgy of Uranium Alloys, Brook Hill Publishing Co., 1976, pp. 611-656.

[48] A. Jain, S.P. Ong, G. Hautier, W. Chen, W.D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, K.a. Persson, The Materials Project: A materials genome approach to accelerating materials innovation, APL Mater. 1(1) (2013)011002.

[49] M. Korchynsky, R. Fountain, Precipitation phenomena in cobalt-tantalum alloys, Trans. Met. Soc. AIME 215 (1959) 1033-1093.