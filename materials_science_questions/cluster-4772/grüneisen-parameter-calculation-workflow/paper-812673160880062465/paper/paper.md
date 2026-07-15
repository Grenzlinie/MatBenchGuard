# Rapid initiation in condensed phases through resonant nonlinear acoustics

Robert Almgren, Andrew Majda, and Rodolfo R. Rosales

Citation: *Physics of Fluids A: Fluid Dynamics* **2**, 1014 (1990); doi: 10.1063/1.857639

View online: https://doi.org/10.1063/1.857639

View Table of Contents: https://aip.scitation.org/toc/pfa/2/6

Published by the American Institute of Physics
---
---

tive to the values of the coefficients $\alpha_1$, $\alpha_2$, $\alpha_3$, $A$, and $B$, and therefore we consider in detail how their values are determined by the equation of state and how we shall explore this parameter space. Before doing so we point out two facts.

(i) The absolute sizes of $\alpha_1$, $\alpha_2$, $\alpha_3$ have been fixed by the requirement that they sum to unity, by the choice of time scale. The important quantity is the ratio

$$
\alpha = (\alpha_1 + \alpha_3)/\alpha_2 = P/e_V, \tag{27}
$$

which measures the amount of chemical energy released into both sound waves compared to the amount of energy released into the entropy wave.

(ii) The absolute sizes of $A$ and $B$ are dependent on the high-frequency length scale via the factor $\kappa$. Only the ratio $B/A$ has intrinsic physical significance.
Thus a complete exploration of the coefficient space would vary $\alpha$ and $B/A$ independently through all positive values. Instead we vary them jointly through a one-parameter space, based on the following considerations.

First we consider the ratio $\alpha$. We shall see in Sec. IV that, for a temperature-dependent reaction rate, this parameter plays the controlling role in determining the nature of the blowup. When $\alpha$ becomes larger than 2, typical blowup behavior ceases to be a stationary explosion of the microstructure and shifts to blowup of a traveling acoustic mode.

By elementary thermodynamic reasoning, we calculate from (27)

$$
\alpha = 1/[(1/PV)(c_P/\beta) - 1], \tag{28}
$$

where

$$
c_P = T\left.\frac{\partial S}{\partial T}\right|_P,\quad \beta = \frac{1}{V}\left.\frac{\partial V}{\partial T}\right|_P \tag{29}
$$

are the specific heat at constant pressure and the thermal expansion coefficient. In terms of the standard thermodynamic derivatives,

$$
\begin{aligned}
\gamma &= -\left.\frac{\partial \log P}{\partial \log V}\right|_s,\quad \Gamma = -\left.\frac{\partial \log T}{\partial \log V}\right|_s, \\
g &= \left.\frac{PV}{TS}\frac{\partial \log T}{\partial \log S}\right|_V
\end{aligned} \tag{30}
$$

(the adiabatic exponent, the Gruneisen coefficient, and the dimensionless specific heat$^{17,18}$), we may write

$$
c_P = \frac{PV}{T}\frac{\gamma}{\gamma g - \Gamma^2},\quad \beta = \frac{1}{T}\frac{\Gamma}{\gamma g - \Gamma^2}, \tag{31}
$$

and so

$$
\alpha = 1/(\gamma/\Gamma - 1). \tag{32}
$$

If the material were a polytropic ideal gas with adiabatic exponent $= c_P/c_v = \gamma$, then $\Gamma = \gamma - 1$, $\alpha = \gamma - 1$. Since physical ideal gases necessarily have $\gamma < 2$, they always have $\alpha < 1$. Experimental results are available for reaction product gases under detonation conditions, $^{17}$ and though $\gamma$ and $\Gamma$ each vary by factors of 2 or more as density varies over several orders of magnitude, $\gamma/\Gamma$ generally remains roughly constant and $\alpha$ remains roughly equal to $\frac{1}{3}$.

Nonetheless, we want to explore the entire range of values of $\alpha$, in order to understand the full range of phenomena present in (2) and (6). For example, other calculations of the authors show that considering a reaction with a mole increment, as suggested by Stewart, $^{11}$ gives the same system (2) or (6), but with a value of $\alpha$ that is increased by the mole increment. Thus larger values of the ratio $\alpha$, even though not simple consequences of the equation of state, can be physically realistic.

Next we consider the quadratic coefficients $A$ and $B$. The formulas in Table II may be written in the simpler form$^{19}$

$$
A = \frac{\rho}{P} \mathscr{G},\quad B = \left.\frac{1}{4}\frac{\rho}{P}\Gamma\alpha\frac{\partial \log(\partial P/\partial T)}{\partial \log T}\right|_s, \tag{33}
$$

where $\mathscr{G}$, the "fundamental derivative of gasdynamics," is

$$
\mathscr{G} = \left.\frac{1}{2}\frac{V^2}{\gamma P}\frac{\partial^2 P}{\partial V^2}\right|_s \tag{34}
$$

and measures the nonlinearities of the acoustic wave fields.$^{18}$

These coefficients depend on second derivatives of the internal energy function, and are much harder to measure experimentally than the first derivatives. We know of no experiment giving reliable values for realistic materials under the extreme conditions characteristic of detonation.

If the material were a polytropic ideal gas with adiabatic exponent $\gamma$, then we would have [we have divided $\kappa$ in (3) by $\gamma(\gamma - 1)$ to make $B$ constant]

$$
A = \frac{1}{2}[(\gamma + 1)/(\gamma - 1)],\quad B = \frac{1}{4}. \tag{35}
$$

The ratio

$$
B/A = \frac{1}{2}[(\gamma - 1)/(\gamma + 1)] \tag{36}
$$

is zero at $\gamma = 1$ and varies slowly as $\gamma$ increases to $\infty$.

In view of the considerations presented above—our desire to consider all values of $\alpha$, and our lack of knowledge of realistic values for $B/A$—we adopt the following strategy for systematic study of the systems (2) and (6).

We shall assume that the material is a polytropic ideal gas with exponent $\gamma$. Then $\alpha = \gamma - 1$, and varying $\alpha$ from 0 to $\infty$ corresponds to varying $\gamma$ from 1 to $\infty$. Thus we take

$$
\alpha_1 = \alpha_3 = (\gamma - 1)/2\gamma,\quad \alpha_2 = 1/\gamma, \tag{37}
$$

and the values $A$, $B$ are the corresponding ones according to (35). This choice ensures that we always have a thermodynamically consistent set of parameters although, as discussed above, there is physically no such thing as a polytropic ideal gas with $\gamma > 2$. We use this model as a convenient way to vary $\alpha$ while keeping consistent values of $A$ and $B$.

### III. RESONANT ACOUSTICS FOR INERT MATERIALS

Here we consider the system describing small-amplitude periodic resonating waves,

$$
\begin{aligned}
& \Sigma_{1 t}-A \Sigma_{1} \Sigma_{1}^{\prime}+B\left\langle\Sigma_{2}^{\prime}, \Sigma_{3}\right\rangle_{1}=0, \\
& \Sigma_{3 t}+A \Sigma_{3} \Sigma_{3}^{\prime}-B\left\langle\Sigma_{2}^{\prime}, \Sigma_{1}\right\rangle_{3}=0,
\end{aligned}\tag{38}
$$
with a background microstructure defined by a periodic en- tropy variation as described in Sec. II. Thus the entropy kernel $\Sigma_{2}(\theta_{2})$ is a specified function, periodic with period $\frac{1}{2} L$  and constant in time, while $\Sigma_{1}$ and $\Sigma_{3}$ are amplitudes for the left and right sound waves, and are periodic with period $L$ . A derivation of these equations in the context of nonlinearacoustics has been given earlier by Majda and Rosales. $^{10}$  When $B=0$ so that there are no resonant effects, the equa tions in (38) do not amplify acoustic waves. Here we empha- size the new phenomena involving acoustic wave amplifica- tion that occur through resonant effects of acoustics with the microstructure for $B \neq 0$ . These effects of resonant wave am plification are potentially very important for reacting mate- rials and will be analyzed in two different contexts in Secs. IV and V.

The main new phenomenon associated with solutions of(38) that we emphasize here is the amplification of a peak height through purely inert-gas mechanisms, by the interac- tion of the Burgers term and the resonant terms. This effect was discovered by Choi and Majda, $^{15}$ and we report on a more systematic study here. We take the entropy kernel
$$\Sigma_{2}\left(\theta_{2}\right)=\cos 4 \pi \theta_{2},\tag{39}$$
which is of period $\frac{1}{2} L=\frac{1}{2}$ , and sound wave initial data
$$\Sigma_{1}^{0}\left(\theta_{1}\right)=\cos 2 \pi \theta_{1}, \quad \Sigma_{3}^{0}\left(\theta_{3}\right)=\cos 2 \pi\left(\theta_{3}-\phi\right) \quad(40)$$
(period $L=1$ ) for $0<\phi<1$ . By varying the single param eter $\phi$ we cover all relative phases. We also vary the size of the Burgers coefficient $A$ , keeping $B$ constant at $\frac{1}{4}$ . We keep the amplitudes of all the waves at the fixed value 1, since varying the amplitude of $\Sigma_{2}$ relative to $\Sigma_{1}$ and $\Sigma_{3}$ would only amount to a rescaling of time and a different value of $A$ . Thus, within the context of two equal-amplitude sound waves and single-mode cosine data in all components, we have made a complete search of parameter space, with only the two parameters $\phi$ and $A$ .

First, we discuss an extremely simple effect where the two sound waves exchange energy and amplify. We set A =0 in (38) so that the nonlinear convective terms are absent but the resonant effects remain. In this case exact solutions for the initial data in (40) are written down expli- citly as rotations of the Fourier coefficients. For $\phi=0$ the solution has no propagation in $\theta_{1}$ or $\theta_{3}$ ; the waves simply exchange energy back and forth between each other. The maximum increase of peak height is $\sqrt{2}$ , by conservation of energy. For $\phi=\frac{1}{2}$ the solution is a traveling wave in each component, left sound $\Sigma_{1}$ propagating to the left and right sound $\Sigma_{3}$ to the right without amplification. Intermediate cases combine those two effects.

Next, we consider $A \neq 0$ and emphasize the case $\phi=\frac{1}{2}$  for the following reason. We have just discussed a simple sort of amplification of peak height as a result of the exchange of energy, one mode taking energy away from the other. Now we demonstrate a more interesting phenomenon in which the two sound modes maintain their symmetry: both in- crease their peak height at the same time. The resonant inter- action takes energy, not from one mode to the other, but from the troughs of both modes to the peaks of both modes. Figure 1 shows time histories for the case $\phi=\frac{1}{2}, A=0.2$ . The general dependence of maximum wave amplification on relative phase $\phi$ for $A=0.2$ is presented in Table III. The trends of our general parameter study are as follows: As $A$ is increased from zero, the peaks increase from constant- height traveling waves; as $A$ becomes large the Burgers dy namics takes over and the peak is cut down by shock forma- tion before it can increase substantially. The maximum peak height occurs for $\phi=\frac{1}{2}$ and $A=0.2$ ; there the increase is approximately $70 \%$ before shocks cause the decrease. The peak reaches its maximum height at time $t \approx 1.33$ . The peak growth is the result of an interplay between the resonance and the Burgers term: for this phase relationship $\phi=\frac{1}{2}$ ; if A =0 then the sound waves simply translate without change of shape. Conversely, if the resonant terms are absent, then the sound components solve the decoupled inviscid Burgers equations; the peaks will translate sideways at the same height until shocks form and diminish the peak height. When both effects are combined the result is an increase in peak height.

We will see in Secs. IV and V that such inert acoustic wave amplification through resonance with microstructure is one important mechanism for reduction of the induction time when coupled with chemical reactions exhibiting sensi- tive rate dependence. The interested reader can consult Majda et al. $^{14}$ and Pego $^{16}$ for other remarkable effects of the resonant terms in (38) on inert acoustic wave propagation.

## IV. NONLINEAR RESONANCE OF MICROSTRUCTURE WITH TEMPERATURE-SENSITIVE REACTION RATE
In this section we study solutions of the system (2) for the three high-frequency waves: $\Sigma_{1}(\theta_{1}, t), \Sigma_{2}(\theta_{2}, t)$ , and $\Sigma_{3}(\theta_{3}, t)$ , and the background temperature $\bar{T}(t)$ ,
$$
\begin{aligned}
\Sigma_{1 t} & -A \Sigma_{1} \Sigma_{1}^{\prime}+B\left\langle\Sigma_{2}^{\prime}, \Sigma_{3}\right\rangle_{1} \\
& =\alpha_{1} e^{\bar{T}}\left(\left\langle e^{\Sigma_{2}}, e^{\Sigma_{3}}\right\rangle_{1} e^{\Sigma_{1}}-\bar{M}\right), \\
\Sigma_{2 t} & =\alpha_{2} e^{\bar{T}}\left(\left\langle e^{\Sigma_{1}}, e^{\Sigma_{3}}\right\rangle_{2} e^{\Sigma_{2}}-\bar{M}\right), \\
\Sigma_{3 t} & +A \Sigma_{3} \Sigma_{3}^{\prime}-B\left\langle\Sigma_{2}^{\prime}, \Sigma_{1}\right\rangle_{3} \\
& =\alpha_{3} e^{\bar{T}}\left(\left\langle e^{\Sigma_{2}}, e^{\Sigma_{1}}\right\rangle_{3} e^{\Sigma_{3}}-\bar{M}\right), \\
\bar{T}_{t} & =e^{\bar{T}} \bar{M},
\end{aligned}\tag{41}
$$
where

![](./images/812673160880062465_1.jpg)

FIG. 1. Amplification of an acoustic peak by inert resonance with entropy microstructure. The right sound component is shown; the left sound com- ponent is symmetric.

**TABLE III.** Maximum value of sound component due to inert resonance (initial amplitudes 1 in all components, $A=0.2$).

<table>
  <thead>
    <tr>
      <th>$\phi$</th>
      <th colspan="2">max $\Sigma$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>($t=0$)</td>
    </tr>
    <tr>
      <td>0.125</td>
      <td>1.20</td>
      <td>($t=0.35$)</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>1.40</td>
      <td>($t=0.50$)</td>
    </tr>
    <tr>
      <td>0.375</td>
      <td>1.66</td>
      <td>($t=1.01$)</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>1.71</td>
      <td>($t=1.33$)</td>
    </tr>
  </tbody>
</table>

$$
\bar{M}=\overline{\left\langle e^{\Sigma_{2}}, e^{\Sigma_{2}}\right\rangle_{1} e^{\Sigma_{1}}}=\overline{\left\langle e^{\Sigma_{1}}, e^{\Sigma_{1}}\right\rangle_{2} e^{\Sigma_{2}}}=\overline{\left\langle e^{\Sigma_{1}}, e^{\Sigma_{2}}\right\rangle_{3} e^{\Sigma_{3}}}.
\tag{42}
$$

The convolution integrals $\langle\cdot,\cdot\rangle_{k}$ are defined in (4). The initial microstructure is defined by periodic variations of $\Sigma_{2}$; the interactions between the nonlinear acoustics described by the amplitudes $\Sigma_{1}$ and $\Sigma_{3}$ and the microstructure $\Sigma_{2}$ is given in the first three equations in (41) while the complete microstructure and the mean-field temperature interact through the equations for $\bar{T}$ and $\bar{M}$. For the temperature-sensitive reaction rates considered here there are two mechanisms of nonlinear resonance of acoustics with microstructure:

The inert, quadratically nonlinear, convective
and acoustic resonance terms with the coefficients
$A$ and $B$, already discussed in Sec. III.
(43a)

The strongly nonlinear temperature-sensitive
resonance of linear acoustics with microstructure,
defined by the terms multiplying $\alpha_{1},\alpha_{2},$ and $\alpha_{3}$. The
relative size of $\alpha_{2}$ and $\alpha_{1}=\alpha_{3}$ measure the relative
importance of simple thermal explosion of the mi-
crostructure to the potential explosion through
acoustic resonance.
(43b)

The classical example of thermal explosion of the microstructure is readily understood for the special case of (41) with the sound waves $\Sigma_{1},\Sigma_{3}$ initially zero; then $\Sigma_{2}$ and $\bar{T}$ are the only dependent variables in (41). The microstructure defined by $\Sigma_{2}$ yields higher local values of the temperature than the mean field and explodes more rapidly because the local reaction rate is exponentially larger (the general case of thermal explosion of the microstructure has been studied exhaustively by Almgren$^{20}$). Naively, we might expect that such simple local explosions dominate the behavior of the solutions of (41); however, here in Sec. IV we show that there are regimes appropriate for condensed phase modeling where in fact completely different resonant nonlinear acoustic effects yield the blowup and the thermal explosion is suppressed. This regime of blowup through acoustic resonance is defined for ideal gas equations by the condition $\gamma>3$, while the requirement $\gamma<3$ defines the regime where the simpler mechanism of thermal explosion of microstructure is the dominant event. In this section, we also document the quantitative fashion in which the explosion time is dramatically shortened below the conventional thermal explosion time of the microstructure through a combination of the two resonant effects described in (43). In this section we assume ideal $\gamma$-gas laws with $1<\gamma<\infty$ so that the coefficients in (41) are given by (35) and (37) as $\gamma$ varies. As mentioned earlier, we consider large values of $\gamma$ as a simple way to vary the coefficients in (41) in a fashion to simulate behavior appropriate for condensed phases.

### A. Explosion through chemical-acoustic resonance versus classical thermal explosion of microstructure

We report on a series of numerical experiments with the same initial data as the gas constant $\gamma$ is varied. This will illustrate the effect mentioned earlier, that for $\gamma<3$ the entropy component is favored and thermal explosions of microstructure typically occur, while for $\gamma>3$ one or the other of the sound modes is favored to blow up so that the explosion occurs through nonlinear acoustics propagating in the microstructure. We take initial data

$$
\Sigma_{1}^{0}=\cos 2 \pi \theta_{1}, \quad \Sigma_{2}^{0}=\cos 8 \pi \theta_{2}, \quad \Sigma_{3}^{0}=\cos 6 \pi \theta_{3},
\tag{44}
$$

which have, in the periods $1,\frac{1}{2},1$, respectively, one wave of $\Sigma_{1}$, two waves of $\Sigma_{2}$, and three waves of $\Sigma_{3}$. We intentionally illustrate these phenomena with data with some asymmetry to indicate robust behavior. We take values $\gamma=1.1,1.5,2,3$, $4,5,7$, and 10; the results of the computations are shown in Figs. 2(a)-2(h).

For the small values of $\gamma$, shocks form immediately in the sound components. In fact, the case in Fig. 2(a) with $\gamma=1.1$ really illustrates a classical thermal explosion of microstructure. As $\gamma$ is increased with $\gamma<3$ there is strong shock formation, but small upturns may be seen in the sound amplitudes at the final stage when thermal explosion occurs. At $\gamma=3$, there is equal competition between thermal explosion and explosion through nonlinear acoustics [see Fig. 2(d)]. As $\gamma$ increases through 3, the explosion shifts from $\Sigma_{2}$ to the right sound component $\Sigma_{3}$. There are always shocks that form in $\Sigma_{1}$ and $\Sigma_{3}$ since the Burgers coefficient $A$ has the minimum value $\frac{1}{2}$. Note that when a sound component blows up, it typically does so right at the edge of a shock. As $\gamma$ increases to 10, the growth of $\Sigma_{2}$ becomes less and less without conventional thermal explosion. As the growth of $\Sigma_{2}$ becomes less because of the decreasing $\alpha_{2}$, the resonant contribution to $\Sigma_{1}$ from $\Sigma_{2}$ and $\Sigma_{3}$ also decreases, and the increase in amplitude of $\Sigma_{1}$ becomes less prominent. We emphasize the physical significance of this shift of blowup. If the mode that blows up is the entropy wave, then the blowup is a stationary peak with infinities in temperature and density. If it is a sound wave then there is a traveling singularity, with infinities in temperature, pressure, and density. Of course, since we are utilizing asymptotics, small-amplitude "infinities" simply mean that the wave has reached the large-amplitude regime.

At times very near the explosions, all our calculations for $\gamma>3$ show explosions at a shock as documented by Clarke$^{21}$ for single acoustic pulses. However, the time at which explosion occurs is significantly earlier through the effects of multiwave resonance. We document these effects in the remainder of this section.

From (37), we see that the coefficients $\alpha_{1}=\alpha_{3}$ and $\alpha_{2}$ yielding the effect of nonlinear combustion resonance on the acoustic modes and entropy mode, respectively, satisfy

![](./images/812673160880062465_2.jpg)

![](./images/812673160880062465_3.jpg)

![](./images/812673160880062465_4.jpg)

![](./images/812673160880062465_5.jpg)

FIG. 2. (a) Resonant acoustic blowup versus conventional thermal explosion. In (a) with $\gamma=1.1$, the sound components rapidly decay in shocks while the entropy mode blows up in a standard thermal explosion. The plot format shows, on the right, spatial profiles of the three components at successive times and, on the left, graphs over time of the spatial maximum and minimum at each time $t$. The little disks are placed at the times of the spatial slices. (b) Here $\gamma=1.5$. Decay of sound components is less severe than in (a). (c) Here $\gamma=2$. Sound components show slight increases as the entropy mode blows up. (d) Here $\gamma=3$. This is the "crossover point" where the growth of all three modes is equally favored. All three modes exhibit dramatic growth at the blowup time. The final peak locations are $\theta_{1}^{*}=0.882,2 \theta_{2}^{*}=0.009$, and $\theta_{3}^{*}=0.126$ with $\theta_{1}^{*}-2 \theta_{2}^{*}+\theta_{3}^{*}=0.999 \equiv-0.001(\bmod 1)$, illustrating the essential role of chemi-cal-acoustic resonance. (e) Here $\gamma=4$. For $\gamma>3$ we are in the regime of acoustic explosion; the right sound mode blows up while the entropy microstructure amplitude reaches a maximum final value of 2.94. Since in this regime blowup typically occurs right at the edge of a shock, there is strong interaction of nonlinear convection with combustion. (f) Here $\gamma=5$. Final entropy amplitude $=2.06$. (g) Here $\gamma=7$. Final entropy amplitude $=1.56$. (h) Here $\gamma=10$. The entropy mode reaches a maximum amplitude of only 1.33; it plays the role of a stationary constant microstructure mediating the interaction of the acoustic waves.

### B. Reduced explosion times through acoustic-combustion resonance

Here we give a careful quantitative assessment of the reduced thermal explosion times that occur through a combination of the nonlinear resonance effects given in (43a) and (43b). In Sec. III we discussed resonant acoustic wave amplification without combustion, isolating the effects in (43a). We begin by utilizing the same initial data and discussing the nonlinear resonances that occur for solutions of (41) as a result of the temperature-sensitive reaction rate and linear acoustic convection alone (43b) with both the nonlinear convective and acoustic resonant effects suppressed (i.e., $B = A = 0$). Then we report on calculations with the complete system in (41) where both resonant effects in (43) are active.

### 1. Resonance driven by temperature-dependent combustion alone

We neglect the quadratic fluid-mechanical terms and keep only the combustion source terms on the right-hand sides. Since the quadratic terms are the only ones that contain $\theta$ derivatives, striking them out of (41) we have the system of coupled integrodifferential ODE's for $\Sigma_1(\theta_1,t)$, $\Sigma_2(\theta_2,t)$, $\Sigma_3(\theta_3,t)$, and $\overline{T}(t)$:

$$
\begin{align}
\frac{\partial\Sigma_1}{\partial t} &= \alpha_1 e^{\overline{T}} \left( \langle e^{\Sigma_2},e^{\Sigma_3} \rangle_1 e^{\Sigma_1} - \overline{M} \right), \\
\frac{\partial\Sigma_2}{\partial t} &= \alpha_2 e^{\overline{T}} \left( \langle e^{\Sigma_1},e^{\Sigma_3} \rangle_2 e^{\Sigma_2} - \overline{M} \right), \\
\frac{\partial\Sigma_3}{\partial t} &= \alpha_3 e^{\overline{T}} \left( \langle e^{\Sigma_1},e^{\Sigma_2} \rangle_3 e^{\Sigma_3} - \overline{M} \right), \\
\frac{d\overline{T}}{dt} &= e^{\overline{T}} \overline{M},
\end{align} \tag{46}
$$

where

$$
\overline{M} = \langle e^{\Sigma_2},e^{\Sigma_3} \rangle_1 e^{\overline{\Sigma_1}} = \langle e^{\Sigma_1},e^{\Sigma_3} \rangle_2 e^{\overline{\Sigma_2}} = \langle e^{\Sigma_1},e^{\Sigma_2} \rangle_3 e^{\overline{\Sigma_3}}. \tag{47}
$$

There is one ODE at each point of $\theta_1$, $\theta_2$, and $\theta_3$, and one for $\overline{T}(t)$. Initial data $\Sigma_1^0(\theta_1)$, $\Sigma_2^0(\theta_2)$, and $\Sigma_3^0(\theta_3)$ of mean zero are specified [and $\overline{T}(0) = 0$]; the property of mean zero is preserved under the time evolution. All functions $\Sigma$ are periodic; $\Sigma_1$ and $\Sigma_3$ of period 1, and $\Sigma_2$ of period $\frac{1}{2}$.

Before studying the solutions of this system, we discuss the physical description. It is important to recognize that the system in (46) retains the interaction of transported linear acoustic effects with the microstructure. In most of our subsequent discussion we shall use terms such as "resonant superposition" of energy or temperature. This terminology is based on the form of the right-hand sides of (46), which are resonant integral source terms: In the equations two modes combine to stimulate the third. Physically there is only one temperature perturbation, $\epsilon[\overline{T}(t) + T_1]$ with $T_1$ given as the linear superposition

$$
\begin{align}
T_1 &= \Sigma_1(\theta_1,t) + \Sigma_2(\theta_2,t) + \Sigma_3(\theta_3,t), \\
\theta_j &= (\kappa/\epsilon)(x - \lambda_j t),
\end{align} \tag{48}
$$

and one local reaction rate that depends strongly nonlinearly on the local value of $T_1$. For example, if $\Sigma_1$ and $\Sigma_3$ have maxima at $\theta_1^*$ and $\theta_3^*$, then as these profiles propagate to the left and to the right at the characteristic speeds $\pm 1$, their sum will have maxima at points of a regular lattice. These lattice points will be characterized by

$$
\theta_2^* = \frac{1}{2}(\theta_1^* + \theta_3^*) + (n/2)L. \tag{49}
$$

When $\Sigma_2$ is added, the complete sum $T_1$ will have maxima whose size depends on whether or not the maxima of $\Sigma_2$ are at the "resonance locations" $\theta_2^*$ in order to contribute to the maximum. If the peaks of $\Sigma_2$ are at $\theta_2^*$, then they superpose three at a time; if the peaks are at different places then, at most, two maxima meet each other at the same time. Since the combustion is so strongly nonlinear, the former releases energy much faster. The overall picture is that the combustion proceeds at all points according to the local temperature; the energy released is partitioned at each point among the modes according to the $\alpha_j$ and accumulated in each mode along the characteristic directions. We emphasize that the integral mean terms on the right-hand side of (46) are a consequence of having small-scale periodic wave patterns. These terms are identically 1 for pulsed high-frequency waves. Simple inequalities⁷ show that these mean terms always enhance the overall rate of combustion ($\overline{M} \geqslant 1$).

We present a numerical exploration of the effect of the relative phases of the components on the duration of the induction period, i.e., the time of blowup. We have mentioned the special importance of the phase relation $\theta_2 = \frac{1}{2}(\theta_1 + \theta_3)$ among the maxima of the components. This resonance effect may be expected to be seen most dramatically in the exponential terms, because of their strong nonlinearity; those are exactly the terms we have isolated here. We shall demonstrate a very strong dependence of the duration of the induction period on the locations of the maxima of the initial data.

We take initial data

$$
\Sigma_1^0 = \cos 2\pi\theta_1, \quad \Sigma_2^0 = \cos 4\pi\theta_2, \quad \Sigma_3^0 = \cos 2\pi(\theta_3 - \phi) \tag{50}
$$

for $\phi = 0, \frac{1}{8},\frac{1}{4},...,\frac{7}{8}$. This is the same initial data used in Sec. III to study inert acoustic resonance. We take all the combustion coefficients $\alpha_j$ equal to $\frac{1}{3}$, corresponding to $\gamma = 3$; by attempting to maintain a balance among the different components we expect to see the distinct effects of resonant phase shifts. The parameter $\phi$ sweeps over relative phases. Table IV lists certain interesting properties that we discuss next.

For $\phi = 0$, when the maxima of all components are exactly placed to reinforce each other, the peaks go to $\infty$ exactly at their initial locations. As $\phi$ changes from zero, the peaks no longer blow up at their initial locations, but at shifted locations that allow for resonant superposition of temperature. The locations of the final peaks are shown in Table IV; it is clear that they are positioned almost exactly in accordance with the phase relation $\theta_2 = \frac{1}{2}(\theta_1 + \theta_3)$, confirming our simple theory from (49) for the role of phase shifts in resonance. (This computation used $N = 1024$ points, so the best accuracy possible in peak location is 0.001.) The resonant superposition of energy is less efficient when energy is not deposited exactly on top of the peaks; for this reason the

<table>
<caption>TABLE IV. Effect of relative phase on peak locations and blowup time (linear acoustic resonance only; temperature-dependent chemistry). The star indicates that a valve is unusual (close to 0.5 instead of close to 0).</caption>
<thead>
<tr>
<th>$\phi$</th>
<th>$\theta_{1}^{*}$</th>
<th>$\theta_{2}^{*}$</th>
<th>$\theta_{3}^{*}$</th>
<th>$\theta_{1}^{*}-2\theta_{2}^{*}+\theta_{3}^{*}$</th>
<th>$t^{*}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.197</td>
</tr>
<tr>
<td>0.125</td>
<td>0.958</td>
<td>0.021</td>
<td>0.083</td>
<td>-- 0.001</td>
<td>0.214</td>
</tr>
<tr>
<td>0.25</td>
<td>0.917</td>
<td>0.042</td>
<td>0.167</td>
<td>0.000</td>
<td>0.269</td>
</tr>
<tr>
<td>0.375</td>
<td>0.875</td>
<td>0.063</td>
<td>0.250</td>
<td>-- 0.001</td>
<td>0.375</td>
</tr>
<tr>
<td>0.5</td>
<td>0.000</td>
<td>0.000</td>
<td>0.500</td>
<td>0.500*</td>
<td>0.506</td>
</tr>
<tr>
<td>0.625</td>
<td>0.125</td>
<td>0.438</td>
<td>0.750</td>
<td>-- 0.001</td>
<td>0.375</td>
</tr>
<tr>
<td>0.75</td>
<td>0.083</td>
<td>0.458</td>
<td>0.833</td>
<td>0.000</td>
<td>0.269</td>
</tr>
<tr>
<td>0.875</td>
<td>0.042</td>
<td>0.479</td>
<td>0.917</td>
<td>0.001</td>
<td>0.214</td>
</tr>
</tbody>
</table>

blowup time, also shown in Table IV, is delayed as $\phi$ moves away from zero. A special case is $\phi=\frac{1}{2}$, when the maxima are positioned exactly out of phase. Then the resonant interaction between the peaks of two modes deposits energy exactly at the trough of the third, where it does not reinforce the primary peak at all and instead creates a smaller peak. This resonant energy is therefore essentially lost since the overall rate of combustion is controlled by the height of the largest peak.

We have already indicated the variation of blowup time with phase, as shown in Table IV. The blowup time is the single most important physical quantity in this problem, in view of our stated interest in understanding the time scales of ignition in physical problems. To emphasize the dramatic dependence on $\phi$, in Fig. 3 we have plotted $t^{*}$ as a function of $\phi$ for both cases. The upper line shows the time of blowup for a single-mode wave alone, $\Sigma^{0}(\theta)=\cos 2 \pi \theta$, with no Burgers term, in the case $\gamma=3$ so $\alpha=\frac{1}{3}$. This time, the blowup time for the microstructure resulting from simple thermal explosion, is 0.627. For the case of poorest resonance, $\phi=\frac{1}{2}$, the blowup time is reduced only by $20 \%$ by the presence of the other two modes and the resonant interaction. But when $\phi=0$, the modes strongly reinforce each other, and the blowup time is reduced dramatically—a factor of 3 in this case of equal amplitude in all modes. We have performed other numerical tests with initial data with different amplitudes in the various components, with qualitatively similar results.

![](./images/812673160880062465_6.jpg)

FIG. 3. The importance of chemical-acoustic resonant superposition of temperature ($\gamma=3$). The time $t^{*}=0.627$ is the blowup time for a single entropy wave, representing standard localized thermal explosion. The line marked with circles shows the results for linear convective resonance alone; the blowup time varies by a factor of 2.5 between the best and worst relative phase relationships. The full system, shown marked by squares, exhibits nearly identical behavior, indicating that chemical-acoustic resonance is the controlling effect when the reaction rate depends on temperature. Inert-gas nonlinear resonance mechanisms accelerate the blowup slightly for $\phi \approx 0.5$.

## 2. The complete system

Now we study the full system (41), including both resonance effects—the quadratic interactions of inert fluid mechanics discussed in Sec. III, and the exponential reinforcement of the combustion terms described above. Studying the two factors separately, we have exhibited a variety of interesting phenomena through acoustic waves interacting with microstructure: peak amplification by inert resonant mechanisms and peak reinforcement by resonant superposition of temperature perturbations. Now we illustrate the role in reducing the explosion time of all these effects in the full system in (41) by describing a number of numerical solutions.

We repeat the investigation of dependence of blowup structure on relative phase of the initial data for the same initial data from (40) and (50). Thus we take
$$\Sigma_{1}^{0}=\cos 2 \pi \theta_{1}, \quad \Sigma_{2}^{0}=\cos 4 \pi \theta_{2}, \quad \Sigma_{3}^{0}=\cos 2 \pi\left(\theta_{3}-\phi\right), \quad(51)$$
for $\phi=0, \frac{1}{8}, \frac{1}{4},..., \frac{7}{8}$. Earlier for (46) we took equal coefficients $\alpha_{1}=\alpha_{2}=\alpha_{3}=\frac{1}{3}$, corresponding to $\gamma=3$, in order to encourage interesting interplay among the modes. Now we take, in addition, $A=1, B=\frac{1}{4}$ corresponding to $\gamma=3$. As before, we tabulate various interesting properties of the solutions in Table V, and in Fig. 3 we graph the dependence of blowup time $t^{*}$ on relative phase $\phi$. We have superimposed this graph over the one for solutions of (46) without inert acoustic resonance to display the role of inert acoustic resonance in reducing the explosion time.

The last column in Table V indicates whether the blowup is a resonant explosion in the entropy mode or a blowup through nonlinear acoustics. The graphs at the beginning of this section document the time history of solutions with these two different types of blowup already so we do not display detailed time histories of the solutions here.

For the same initial data and the calculations presented above for the solutions of the equations in (46), without inert nonlinear acoustic resonance, all three components exploded simultaneously; thus the effects of nonlinear inert resonance and convection transfer the explosion to the resonant acoustics. From the graphs in Fig. 3, we observe that for phases in the vicinity of $\phi \approx 0.5$, the blowup time is reduced slightly by nonlinear acoustic resonance as compared with the linear acoustic combustion resonance mechanism described for (46); but for other values of $\phi$, nonlinear acoustic convection slightly lengthens the blowup time by defocusing the linear resonance relation (49). Thus for temperaturesensitive chemistry, the dominant effect in reducing the thermal explosion time is the chemical-acoustic resonant mechanism for the microstructure presented in (49). This mechanism involves the linear transport effects of acoustics and the nonlinear temperature-sensitive chemistry. In the next section, we obtain reduction of the explosion time for

<table><caption>TABLE V. Effect of relative phase on peak locations and blowup time (full temperature-dependent system, $\gamma = 3$). The star indicates that a valve is unusual (close to 0.5 instead of close to 0).</caption>
<thead>
  <tr>
    <th>$\phi$</th>
    <th>$\theta_{1}^{*}$</th>
    <th>$\theta_{2}^{*}$</th>
    <th>$\theta_{3}^{*}$</th>
    <th>$\theta_{1}^{*}-2\theta_{2}^{*}+\theta_{3}^{*}$</th>
    <th>$t^{*}$</th>
    <th>Blowup mode</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>0.838</td>
    <td>0.001</td>
    <td>0.161</td>
    <td>$-0.003$</td>
    <td>0.228</td>
    <td>Entropy</td>
  </tr>
  <tr>
    <td>0.125</td>
    <td>0.783</td>
    <td>0.013</td>
    <td>0.242</td>
    <td>$-0.001$</td>
    <td>0.250</td>
    <td>Left sound</td>
  </tr>
  <tr>
    <td>0.25</td>
    <td>0.720</td>
    <td>0.014</td>
    <td>0.269</td>
    <td>$-0.039$</td>
    <td>0.317</td>
    <td>Left sound</td>
  </tr>
  <tr>
    <td>0.375</td>
    <td>0.659</td>
    <td>0.009</td>
    <td>0.313</td>
    <td>$-0.046$</td>
    <td>0.419</td>
    <td>Left sound</td>
  </tr>
  <tr>
    <td>0.5</td>
    <td>0.626</td>
    <td>0.000</td>
    <td>0.883</td>
    <td>$-0.491^{*}$</td>
    <td>0.476</td>
    <td>Right sound</td>
  </tr>
  <tr>
    <td>0.625</td>
    <td>0.046</td>
    <td>0.491</td>
    <td>0.972</td>
    <td>0.036</td>
    <td>0.412</td>
    <td>Right sound</td>
  </tr>
  <tr>
    <td>0.75</td>
    <td>0.979</td>
    <td>0.485</td>
    <td>0.031</td>
    <td>0.040</td>
    <td>0.313</td>
    <td>Right sound</td>
  </tr>
  <tr>
    <td>0.875</td>
    <td>0.884</td>
    <td>0.486</td>
    <td>0.088</td>
    <td>0.000</td>
    <td>0.249</td>
    <td>Right sound</td>
  </tr>
</tbody>
</table>

pressure-sensitive reaction rates through the competing mechanism of inert nonlinear acoustic resonance.

## V. NONLINEAR RESONANCE OF MICROSTRUCTURE WITH PRESSURE-SENSITIVE REACTION RATE

Here we consider solutions of the asymptotic system of equations from (6) given by
$$
\begin{aligned}
& \Sigma_{1 t}-A \Sigma_{1} \Sigma_{1}^{\prime}+B\left\langle\Sigma_{2}^{\prime}, \Sigma_{3}\right\rangle_{3}=\frac{1}{2} e^{\bar{P}} \overline{e^{\Sigma_{3}}}\left(e^{\Sigma_{1}}-\overline{e^{\Sigma_{1}}}\right), \\
& \Sigma_{2 t}=(1 / \alpha) e^{\bar{P}}\left(\left\langle e^{\Sigma_{1}}, e^{\Sigma_{3}}\right\rangle_{2}-\overline{e^{\Sigma_{1}}} \overline{e^{\Sigma_{3}}}\right), \\
& \Sigma_{3 t}+A \Sigma_{3} \Sigma_{3}^{\prime}-B\left\langle\Sigma_{2}^{\prime}, \Sigma_{1}\right\rangle_{3}=\frac{1}{2} e^{\bar{P}} \overline{e^{\Sigma_{1}}}\left(e^{\Sigma_{3}}-\overline{e^{\Sigma_{3}}}\right), \\
& \bar{P}_{t}=e^{\bar{P}} \overline{e^{\Sigma_{1}}} \overline{e^{\Sigma_{3}}},
\end{aligned}\qquad(52)
$$
where the overbar indicates mean over the appropriate $\theta_{j}$. For an ideal $\gamma$-gas law the coefficients appearing on the left-hand side have the same values as in (35) while $\alpha=\gamma-1$. These equations define the nonlinear resonance of microstructure with acoustics for pressure-sensitive reaction rates, as are often appropriate for condensed phases. The terms on the left-hand side of (52) are the same ones as discussed in Secs. III and IV for inert acoustic resonance. The terms on the right-hand side of (52) involve pressure-sensitive chemistry and have completely different resonance behavior than those with temperature-sensitive chemistry discussed in Sec. IV. To illustrate one difference we remark that special solutions of (52) occur when there is no acoustics so that $\Sigma_{1}=\Sigma_{3} \equiv 0$; then (52) reduces to
$$
\begin{aligned}
& \Sigma_{2 t}=0, \\
& \bar{P}_{t}=e^{\bar{P}},
\end{aligned} \Rightarrow \bar{P}(t)=-\log (1-t).\qquad(53)
$$

Thus the microstructure of the condensed phase alone does not reduce the normalized explosion time below the homogeneous time $t=1$; this fact contrasts strongly with the temperature-sensitive case where the superimposed microstructure by itself already reduced the induction time through classical thermal explosions as discussed in Sec. IV [see Fig. 2(a), for example]. Furthermore, since the chemical source terms on the right-hand side involve pressure, and only the sound waves are pressure waves, we anticipate that the inert resonant wave amplifying mechanisms for the system (38) discussed in Sec. III now have a very prominent role in controlling the induction time. In fact, we show that the induction time is much more sensitive to nonlinear resonant acoustic interactions with the microstructure for pressuresensitive chemistry than for the temperature-sensitive chemistry discussed in Sec. IV. In the remainder of this section we present the results of a number of systematic numerical experiments with (52) that confirm the above description.

### A. Resonance of linear acoustics and combustion

In order to demonstrate the difference between the system in (52) and the one in (41), we consider, as in (46), the reduced system derived from (52) by suppressing the nonlinear convective terms and the quadratic wave resonance terms on the left-hand side of (52). The reduced system is the coupled set of integrodifferential ODE's given by
$$
\begin{aligned}
& \Sigma_{1 t}=\frac{1}{2} e^{\bar{P}} \overline{e^{\Sigma_{3}}}\left(e^{\Sigma_{1}}-\overline{e^{\Sigma_{1}}}\right), \\
& \Sigma_{2 t}=(1 / \alpha) e^{\bar{P}}\left(\left\langle e^{\Sigma_{1}}, e^{\Sigma_{3}}\right\rangle_{2}-\overline{e^{\Sigma_{1}}} \overline{e^{\Sigma_{3}}}\right), \\
& \Sigma_{3 t}=\frac{1}{2} e^{\bar{P}} \overline{e^{\Sigma_{1}}}\left(e^{\Sigma_{3}}-\overline{e^{\Sigma_{3}}}\right), \\
& \bar{P}_{t}=e^{\bar{P}} \overline{e^{\Sigma_{1}}} \overline{e^{\Sigma_{3}}},
\end{aligned}\qquad(54)
$$
where an overbar indicates mean over the period length $L$ and $\alpha=\gamma-1$ for a polytropic ideal gas. This system retains the effects of linear acoustic transport on the microstructure as well as the nonlinear effects of pressure-sensitive chemistry. We observe the following facts.

(1) The entropy component $\Sigma_{2}$ appears nowhere on the right-hand sides; this is because it represents a disturbance of density and temperature at constant pressure. Therefore the ODE for $\Sigma_{2}$ may be considered auxiliary, to be solved after $\Sigma_{1}, \Sigma_{3}$, and $\bar{P}$ are known, if desired. Here $\Sigma_{2}$ cannot blow up since it does not reinforce itself; the feedback mechanism necessary for thermal explosion is absent as we have mentioned earlier.

(2) The sound amplitudes $\Sigma_{1}$ and $\Sigma_{3}$ affect each other and the mean pressure $\bar{P}$ only through the mean values of their exponentials, not by a convolution integral [compare with (46)].

Therefore the relative phases of $\Sigma_{1}, \Sigma_{2}$, and $\Sigma_{3}$ can have no effect on the dynamics of $\Sigma_{1}$ and $\Sigma_{3}$, or on the time of blowup; there is no preferred phase relationship for this system. However, the sound wave components are still strongly coupled by the presence of the exponential means. Just as the mean field accelerates the growth of the high-frequency waves via the factor $e^{\bar{P}}$, and the high-frequency waves feed back into the mean via their exponential means, so the expo-

Dependence of Blowup Time on Phase
Pressure-Dependent Chemistry

![](./images/812673160880062465_7.jpg)

FIG. 4. The analog of Fig. 3 for pressure-dependent reaction rate ($\gamma=3$). There is no chemical-acoustic resonance since only the sound waves con- tribute pressure perturbations. Now the blowup is fastest when the inert resonance mechanisms are most effective.

affect the reaction. Thus we certainly expect that inert reso- nance mechanisms as described in Sec. III will play an im- portant role during the induction time.

An important natural physical mechanism for produc- ing such a large entropy kernel is provided by the following scenario for initiation of a heterogeneous condensed-phase explosive, which will be discussed in more detail in a later work by two of the authors. We consider a material that initially contains high-frequency microstructure, modeled as an entropy perturbation. When a strong shock runs over the microstructure two things happen: First, the material is heated to a temperature at which reaction begins ($t=0$ in our model). Second, the entropy perturbation is transmitted through the shock, remaining primarily a much larger en- tropy wave, for a strong shock, but also generating a substan- tially weaker sound perturbation in the shocked region. These transmitted waves correspond to the initial data in our model, and motivate our consideration of an initial entropy wave much larger than the sound wave.

We take the initial data
$$
\begin{aligned}
& \Sigma_{1}\left(\theta_{1}\right)=\cos 2 \pi \theta_{1}, \quad \Sigma_{2}\left(\theta_{2}\right)=10 \cos 4 \pi \theta_{2}, \\
& \Sigma_{3}\left(\theta_{3}\right)=\cos 2 \pi\left(\theta_{3}-\phi\right),
\end{aligned}\qquad(56)
$$
for the relative phase $0<\phi<1$. We take $\gamma=3$. To illustrate the behavior, we show solutions for $\phi=\frac{1}{8}$ and for $\phi=\frac{1}{2}$ in Figs. 5(a) and 5(b), respectively. In both pictures we can clearly see the inert resonance effects acting in the induction time before the blowup.

Figure 5(a), $\phi=\frac{1}{8}$, illustrates the phenomenon of ex- change of energy between modes that we described in Sec. III. Initially $\Sigma_{1}$ increases and $\Sigma_{3}$ decreases, and at $t \approx 0.04$, $\Sigma_{1}$ is at a local maximum while $\Sigma_{3}$ has decreased near to zero. The oscillation continues, with peaks of $\Sigma_{1 max }$ and minima of $\Sigma_{3 max }$ occurring at approximately $t \approx 0.04,0.22$, and 0.39 until an explosion occurs in $\Sigma_{3}$ at $t^{*}=0.45$. Note that $\Sigma_{2}$ remains very nearly constant; therefore this is a very plausible example of two acoustic waves resonantly interact- ing with each other as they cross over a fixed microstructure. As a further example of the very interesting wave dynamics resulting from this interaction, we point out that by $t=0.4$ both $\Sigma_{1}$ and $\Sigma_{3}$ have developed two shocks each, although their initial data were simple cosine waves. In fact, the blowup in $\Sigma_{3}$ occurs at the edge of the shock, which was initially the smaller of the two.

![](./images/812673160880062465_8.jpg)

FIG. 5(a). Acoustic wave interaction with a large entropy kernel; $\gamma=3$, $\phi=\frac{1}{8}$. The entropy wave acts as a fixed microstructure controlling the non- linear interaction of the sound waves, which exchange energy back and forth and develop two shocks each before $\Sigma_{3}$ blows up. (b) Acoustic wave interaction with large entropy kernel; $\gamma=3, \phi=\frac{1}{2}$ . For this value of the relative initial phase, the sound components form the cusped profiles of steady-state traveling waves before the peaks blow up. The blowup time $t^{*}=0.319$ is substantially less than in (a), in agreement with the trend shown by Fig. 4.

Our other example, Fig. 5(b) for $\phi=\frac{1}{2}$, illustrates traveling-wave solutions of the inert system with cosine entropy microstructure, as described by Majda et al. $^{14}$ and Pego. $^{16}$ Those wave profiles have sharp upward points separated by broad rounded minima. These waves assume that shape by $t=0.3$, and then the acoustic peaks $\Sigma_{1}$ and $\Sigma_{3}$ quickly explode. Note that the entropy amplitude $\Sigma_{2}$ in fact diminishes slightly as $\Sigma_{1}$ and $\Sigma_{3}$ blow up.

## VI. CONCLUSIONS
We have proposed and analyzed through numerical experiments a system of simplified asymptotic equations describing multiwave interactions with microstructure in reacting materials. For temperature-sensitive reaction rates, we have documented that the multiwave resonating environment leads to either conventional thermal explosion of microstructure or transported acoustic explosion. We have demonstrated that by varying parameters in the equation of state either mechanism can be selected.

The simplified asymptotic system exhibits a variety of multiwave resonant mechanisms: inert resonant acoustic interaction with the microstructure (Sec. III), and linear resonant averaged superposition of temperature or pressure (Secs. IV and V)—all of these effects occur only because we have a small-amplitude multiwave environment. We have documented different dependence on relative phase of the initial data for these mechanisms individually. For temperature-sensitive reaction rates, we have shown that the linear resonant averaged superposition of temperature controls the reduction of the induction time. For pressure-sensitive reaction rates, we have found that since only the acoustic waves generate pressure perturbation, the inert resonant mechanisms control the reduction in induction time. In all cases the multiwave environment leads to significant reduction in the induction times.

## ACKNOWLEDGMENTS
The authors thank J. Bdzil for generating their interest in the problems studied here through his stimulating lecture at the Cornell workshop on high Mach number combustion in May, 1987.

R. Almgren was supported as a graduate student at Princeton University by Army Research Office (ARO) Fellowship DAAL03-86-G-0027; A. Majda was partially supported by ARO Contract No. DAAL03-89-K-0013, Office of Naval Research (ONR) Contract No. N00014-89-5-1044, and National Science Foundation Contract No. DMS-87-02864; R. R. Rosales was partially supported by National Science Foundation Contract No. DMS-8702625 and a Wade Foundation fellowship.

## APPENDIX: NUMERICAL TECHNIQUES
We use the technique of operator splitting, with three fractional steps: Burgers dynamics (coefficient $A$), inert resonance (coefficient $B$), and combustion (coefficients $\alpha_{1}, \alpha_{2}, \alpha_{3}$). We solve the Burgers equation step with the random choice method; it is essential that this method has no artificial viscosity since typical solutions become infinite right at shock edges. We solve the inert resonance using fast Fourier transforms (FFT's) and exact linear solutions. $^{14}$ We solve the combustion using the simple forward Euler method; the time step is determined so that no component increases more than a fixed small amount in one time step. Typical runs illustrated used $N=2048$ spatial grid points in each component; with that resolution the peaks shown are adequately resolved.

¹A. W. Campbell, W. C. Davis, and J. R. Travis, Phys. Fluids 4, 498 (1961).
²A. W. Campbell, W. C. Davis, J. B. Ramsay, and J. R. Travis, Phys. Fluids 4, 511 (1961).
³R. Engelke and J. B. Bdzil, Phys. Fluids 26, 1210 (1983).
⁴R. Engelke, Phys. Fluids 26, 2420 (1983).
⁵S. A. Sheffield, R. Engelke, and R. R. Alcon, in *Proceedings of the Ninth Symposium (International) on Detonation*, Office of Naval Research (U.S.G.P.O., Washington, DC, 1989).
⁶J. Bdzil (private communication).
⁷A. Majda and R. Rosales, SIAM J. Appl. Math. 47, 1017 (1987).
⁸R. Klein and N. Peters, J. Fluid Mech. 187, 197 (1988).
⁹E. N. Ferm and J. B. Bdzil, submitted to SIAM J. Appl. Math.
¹⁰A. Majda and R. Rosales, Stud. Appl. Math. 71, 149 (1984).
¹¹D. S. Stewart, Combust. Sci. Technol. 48, 309 (1986).
¹²Y. Choquet-Bruhat, J. Math. Pures Appl. 48, 117 (1969).
¹³J. K. Hunter and J. B. Keller, Comm. Pure Appl. Math. 36, 547 (1983).
¹⁴A. Majda, R. Rosales, and M. Schonbek, Stud. Appl. Math. 79, 205 (1988).
¹⁵Y. S. Choi and A. Majda, SIAM Rev. 31, 401 (1989).
¹⁶R. Pego, Stud. Appl. Math. 79, 263 (1988).
¹⁷W. Davis, in *Proceedings of the Eighth Symposium (International) on Detonation* Office of Naval Research (U.S.G.P.O., Washington, DC, 1985), pp. 785–795.
¹⁸R. Menikoff and B. J. Plohr, Rev. Mod. Phys. 61, 75 (1989).
¹⁹J. Bdzil (private communication).
²⁰R. Almgren, to appear in SIAM J. Appl. Math.
²¹J. F. Clarke, J. Fluid Mech. 89, 343 (1978).
²²R. Almgren, Ph.D. thesis, Princeton University, 1989.