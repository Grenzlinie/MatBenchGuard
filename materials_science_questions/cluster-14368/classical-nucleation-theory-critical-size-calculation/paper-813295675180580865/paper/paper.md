# ENERGETICS

## An Effect of Thermodynamic-Parameter Pulsations on the Condensation–Relaxation Process in a Supersaturated Vapor

N. M. Kortsenshteĭn and E. V. Samuĭlov
Presented by Academician A.I. Leont’ev June 5, 2001

Received June 6, 2001

We consider the volume condensation of vapor from a vapor–gas mixture after a sudden formation of the supersaturated state. Thermodynamic parameters of the mixture are assumed to undergo perturbation with a small amplitude of pulsations with respect to average values. On the basis of numerical simulation, it was revealed that for a pulsation frequency exceeding a certain minimum value, the effect of the pulsations is determined only by amplitude and is independent of frequency and phase. For this frequency region, we found expressions determining the relative decrease in the condensation-relaxation time and the relative increase in the droplet-number density. The upper and lower boundaries for the field of application of the dependences found was determined with respect to the pulsation frequency.

1. Let the mixture of an unsaturated vapor and a noncondensing gas be in an adiabatically insulated cylinder with a mobile piston (the piston is fixed). A rapid displacement of the piston makes it possible for the gas to expand and to pass from a stable unsaturated state into a metastable supersaturated state. Then we fix the piston in a new position. In the supersaturated vapor, the relaxation to the equilibrium state takes place as in an arbitrary metastable system. In the case under consideration, this is condensation relaxation involving the processes of nucleation (formation of viable nuclei of a new phase) and growth of the droplets formed. The metastable state of the supersaturated vapor is characterized by a degree of supersaturation

$$
s = \frac{p_{\mathrm{v}}}{p_{\mathrm{s}}(T)}, \tag{1}
$$

where $p_{\mathrm{v}}$ is the partial vapor pressure and $p_{\mathrm{s}}(T)$ is the saturation pressure above a flat liquid–vapor interface depending only on temperature. As a condensation–relaxation time $\tau_{\mathrm{c}}$, we imply an interval of time during which an initial degree of supersaturation $s_0$ caused by the vapor expansion decreases by a factor of $e$. For determining $\tau_{\mathrm{c}}$ and other characteristics of the condensation–relaxation process, we used the kinetic equation for the droplet-size distribution function [1]:

$$
\frac{\partial f}{\partial t} + \frac{\partial (f \dot{r})}{\partial r} = \frac{I}{\rho} \delta(r - r_{\mathrm{cr}}). \tag{2}
$$

To solve this equation, the moments method is used. Provided that the radius $r$ of nucleating and growing droplets is much smaller than the mean free path $\lambda$ for vapor molecules (this condition is assumed to be fulfilled), the moments method makes it possible to reduce equation (2) to the set of moment equations [1]

$$
\frac{d\Omega_i}{dt} = i \dot{r} \Omega_{i-1} + \frac{I}{\rho} r_{\mathrm{cr}}^i, \quad i = 0, 1, 2, 3, \tag{3}
$$

where

$$
\Omega_i = \int_{r_{\mathrm{cr}}}^{\infty} r^i f(r) dr
$$

is the distribution-function moment of the $i$th order. Here, $f(r)$ is the droplet-size distribution function normalized to the number of droplets per unit mass of the vapor–gas–droplet mixture, $I$ is the nucleation rate determining the number of nuclei of the critical size $r_{\mathrm{cr}}$ formed per unit time and per unit volume, $\dot{r}$ is the droplet-growth rate, and $\rho$ is the density of the vapor–gas–droplet mixture. The system of equations (3) supplemented by the equation of state and conservation laws for mass and energy composes a mathematical model of the condensation–relaxation process used in this study. Apart from the above relationship $r \ll \lambda$, we also assume that the following conditions are met:

$$
\tau_{\mathrm{c}} \gg \tau_{g}, \quad \tau_{\mathrm{c}} \gg \tau_{\text{lag}},
$$

AO Power Engineering Institute,
Leninskiĭ pr. 19, Moscow, 117927 Russia

where $\tau_g$ is the time of vapor expansion and $\tau_{\text{lag}}$ is the time lag in the nucleation theory determined as the time of establishing the equilibrium size distribution for new-phase nuclei. The former condition makes it possible to consider the process of the transition of vapor into the metastable state as reasonably fast and to omit processes accompanying the vapor expansion. The latter condition makes it possible to calculate the nucleation rate and the droplet-growth rate in a quasi-steady approximation. The model of the condensation-relaxation process based on the system of equations (3) makes it possible to determine the time dependence of such quantities as the droplet-number density $n_{\text{d}} = \rho\Omega_0$, their average radius $r_{\text{d}} = \frac{\Omega_1}{\Omega_0}$, the degree of condensation $\xi = \frac{4\pi\rho_l\Omega_3}{3\ c^0_{\text{v}}}$ ($\rho_l$ is the density of condensate, and $c^0_{\text{v}}$ is the vapor mass concentration at the initial time moment), and also pressure, temperature, the degree of supersaturation and, thus, the condensation-relaxation time. Analysis of our results for the mathematical simulation of the condensation-relaxation process has shown that, at the initial moment of time, the quantities $\tau_{\text{c}}$ and $n_{\text{d}}$ are the power function of the nucleation rate:

$$
\tau^0_{\text{c}} \backsim I_0^{-1/4}, \quad n^0_{\text{c}} \backsim I_0^{3/4}.
$$

Similar dependences were obtained in [3] when considering the relaxation processes in glasses. In this study, for calculating the steady-state nucleation rate, we used the expression from the classical Zel’dovich–Frenkel’ theory [2]. With allowance for this fact, we can write out the explicit expressions for $\tau_{\text{c}}$ and $n_{\text{d}}$ as functions of the initial degree of supersaturation:

$$
\tau_{\text{c}} \backsim \exp\left\{ \frac{A}{\left[ \ln s_0 \right]^2} \right\}, \tag{4}
$$

$$
n_{\text{c}} \backsim \exp\left\{ -\frac{3A}{\left[ \ln s_0 \right]^2} \right\}, \tag{5}
$$

where $A$ is the constant. As it must be, with approaching the stability region ($s_0 \longrightarrow 1$), the condensation-relaxation time tends to infinity, while the droplet-number density tends to zero.

2. The thermodynamic parameters of the system under consideration are assumed to undergo perturbations during the condensation relaxation. We consider perturbations of all the parameters to be related by the Poisson adiabatic equation. Therefore, we consider furthermore only the perturbations of temperature, nevertheless taking into account the perturbations of all thermodynamic parameters. We now analyze how these perturbations affect the condensation–relaxation process.

In the case of perturbations (pulsations with respect to an average value), the temperature can be represented in the form

$$
T = \langle T \rangle(1 + \vartheta), \tag{6}
$$

where $\langle T \rangle$ is the averaged temperature, $T'$ is the pulsation component, and $\vartheta \equiv \frac{T'}{\langle T \rangle}$ is the relative pulsation.

In this case, the degree of supersaturation according to (1) with allowance for the temperature dependence of the saturated-vapor pressure $p_{\text{s}} \backsim \exp\left( \frac{L}{[RT]} \right)$ and a smallness of pulsations ($\vartheta \ll 1$) can be transformed into the form

$$
\ln s = \ln s(\langle T \rangle) - \vartheta\left( \frac{L}{R\langle T \rangle} - \frac{\gamma}{\gamma - 1} \right). \tag{7}
$$

Here, $s(\langle T \rangle)$ is the degree of supersaturation at the averaged temperature, $L$ is the evaporation heat, $R$ is the universal gas constant, and $\gamma$ is the adiabatic index. In our study, we consider perturbations of thermodynamic parameters in the form of harmonic pulsations

$$
\vartheta = \vartheta_0 \sin(2\pi v t + \varphi_0). \tag{8}
$$

Expressions (6)–(8) were used for the calculation of values entering into Eqs. (3). When simulating on the basis of Eqs. (3), we were able to clarify the effect of the initial degree of supersaturation $s_0$ and also the amplitude $\vartheta_0$, the frequency $v$, and the initial pulsation phase $\varphi_0$ on the condensation-relaxation process. The typical time dependences for the degree of supersaturation and for the droplet-number density are shown in Fig. 1. The data were obtained from the results of solving the set of equations (3) for the cesium–argon mixture (the volume ratio is $1:7$) for $s_0 = 6$, $\vartheta_0 = 1\%$, $v = 100$ Hz, and $\varphi_0 = 0$. In the same figure, we show similar results obtained for the case of ignoring pulsations. As is seen, in the presence of pulsations, the condensation–relaxation time decreases, while the droplet-number density increases compared to the case without pulsations. It should be noted that the curve for the $n_{\text{d}}(t)$ dependence traces pulsations of the degree of supersaturation. This curve abruptly increases with the degree of supersaturation and attains a plateau with its decrease compared to the value at the averaged temperature. Similar calculations were carried out within a reasonably wide interval of variation of pulsation characteristics of the condensation process: $\vartheta_0 = 0.05$–$5\%$, $v = 10^{-1}$–$10^4$ Hz, and $\varphi_0 = -\pi - \pi$. In this case, $s_0$ varied from 3 to 6. Such an interval of variation for all indi-

![](./images/813295675180580865_1.jpg)

Fig. 1. (a) Degree of supersaturation and (b) droplet-number density as functions of time with (solid line) and without (dashed line) allowance for pulsations of thermodynamic parameters. The dotted line is the degree of supersaturation at the averaged temperature.

![](./images/813295675180580865_2.jpg)

Fig. 2. (a) Condensation-relaxation time and (b) droplet-number density as functions of pulsation frequency for various pulsation amplitudes and phases. Triangles mark the data obtained without regard for pulsations.

cated quantities enabled us to envelop five decimal orders of variation in the condensation-relaxation time ($10^{-4}$–10 s) and 15 decimal orders of variation in the droplet-number density ($10^{-1}$–$10^{14}\ \text{m}^{-3}$). Certain results of calculations shown in Fig. 2 make it possible to draw further qualitative conclusions about the effect of pulsations on the condensation-relaxation process. It should be noted that for each value of the pulsation amplitude there exists such a minimum frequency $\nu_{\text{min}}$ above which the process under consideration is independent of both the frequency and the initial phase of pulsations. It can be seen that $\nu_{\text{min}}$ increases with $\vartheta_0$. At the same time, according to the results of the calculations performed, the product $\nu_{\text{min}}\tau_{\text{c}}$ varies insignificantly (within the factor 2 to 4) for the entire spectrum of $\vartheta_0$ and $s_0$ values. Consequently, $\nu_{\text{min}}$ can be determined from the relationship

$$
\nu_{\text{min}} = \frac{4}{\tau_{\text{c}}}. \tag{9}
$$

Taking into account that $\nu^{-1}$ is the pulsation period, in accordance with relation (9), the physical meaning of the quantity $\nu_{\text{min}}$ is the following: during the condensation-relaxation time, four or more pulsations are sufficient for the system to forget the initial phase of oscillations of thermodynamic parameters. From this standpoint, the resonance-like maxima of $\tau_{\text{c}}$ and minima of $n_{\text{d}}$, which are observed in Fig. 2 for $\nu \leq \nu_{\text{min}}$, are likely associated with the coincidence of the pulsation period and the condensation-relaxation time. A weak dependence of $\tau_{\text{c}}$ and $n_{\text{d}}$ on $\nu$ for even lower values of the frequency (Fig. 2) corresponds to the process of condensation relaxation for slowly varying (for the time $\tau_{\text{c}}$) conditions. These are either elevated (for $\varphi_0 = -\pi/2$) or reduced (for $\varphi_0 = 0$) values of the degree of supersaturation compared to $s_0$, which manifests itself in the dependence of the quantities $\tau_{\text{c}}$ and $n_{\text{d}}$ on $\varphi_0$.

3. Further investigation was focused in the region

$$
\nu_{\text{min}} < \nu < \nu_{\text{max}} \tag{10}
$$

in which the effect of pulsations on the condensation-relaxation process depends only on their amplitude and increases with its growth. The value of $\nu_{\text{min}}$ was determined according to relation (9). As an upper boundary of the frequency interval under consideration, it was natural to choose the value

$$
\nu_{\text{max}} = \frac{1}{\tau_{\text{lag}}}. \tag{11}
$$

DOKLADY PHYSICS  Vol. 46  No. 12  2001

We analyzed the results of simulating the condensation–relaxation process for various values of $s_0$ and $\vartheta_0$. These results are shown in Fig. 3. The quantities $\tau_{\rm c}$ and $n_{\rm d}$ are seen to be well described by the dependences of the form

$$
\tau_{\rm c} = A_{\tau}(\vartheta_0)\exp\left\{\frac{B_{\tau}(\vartheta_0)}{[\ln s_0]^2}\right\},
$$

$$
n_{\rm d} = A_n(\vartheta_0)\exp\left\{-\frac{B_n(\vartheta_0)}{[\ln s_0]^2}\right\}.
$$

The method of analyzing the calculation results involves the following. For each value of $\vartheta_0$, we determined the values $\log A$ and $B$. The values obtained were approximated by polynomials in powers of $\vartheta_0$. The use of a second-order polynomial for $\ln A$ and of a third-order polynomial for $B$ enabled us to reproduce reasonably well the results of calculations (solid lines in Fig. 3). The terms of the zeroth order in the expansions obtained coincided with the values obtained previously in the simulations of the condensation–relaxation process without pulsations taken into account in expressions (4) and (5). This allowed us to obtain in a compact form the expressions determining the effect of thermodynamic-parameter pulsations on the condensation–relaxation process restricting the expansions by both the zero order for $\ln A$ and the first order for $B$:

$$
\frac{\tau_{\rm c}^0}{\tau_{\rm c}} = 1.06\exp\left\{\frac{2.15\vartheta_0}{[\ln s_0]^2}\right\}, \tag{12}
$$

$$
\frac{n_{\rm d}}{n_{\rm d}^0} = 0.88\exp\left\{\frac{6.5\vartheta_0}{[\ln s_0]^2}\right\}. \tag{13}
$$

Here, the superscript 0 marks the quantities calculated from relationships (4) and (5) without allowance for pulsations. It is natural that the ratios $\frac{\tau_{\rm c}^0}{\tau_{\rm c}}$ and $\frac{n_{\rm d}}{n_{\rm d}^0}$ must be equal to 1 for $\vartheta_0 = 0$. In the expressions obtained, this passage to the limit is fulfilled only approximately, using simplified approximations for $\ln A$ and $B$. The relationship

$$
\frac{\tau_{\rm c}^0}{\tau_{\rm c}} = \left(\frac{n_{\rm d}}{n_{\rm d}^0}\right)^{1/3},
$$

which follows from (12) and (13) as approximate, is satisfied to a high accuracy in the processing of the primary calculation data. As follows from the obtained expressions (12) and (13) and from the data shown in Fig. 3, the effect of pulsations on the condensation relaxation increases with the decrease in the degree of

![](./images/813295675180580865_3.jpg)

Fig. 3. (a) Condensation-relaxation time and (b) droplet-number density as functions of the initial degree of supersaturation for various pulsation amplitudes. Triangles mark the data obtained without regard for pulsations.

![](./images/813295675180580865_4.jpg)

Fig. 4. Upper (dashed line) and lower (solid lines) ultimate frequencies as functions of the degree of supersaturation for various pulsation amplitudes.

the vapor supersaturation. On the other hand, the dependence of final results for the condensation–relaxation process $(\tau_{\rm c}, n_{\rm d})$ on the initial degree of supersaturation is weakened with the growth of the pulsation amplitude. The field of application of formulas (12)

and (13), which is determined by relations (9)–(11), extends with increasing initial degree of supersatura- tion and decreasing pulsation amplitude (Fig. 4). For the entire spectrum of the input calculation parameters under consideration, the variation interval at the lower boundary ($v_{\text{min}}$) attained five orders of magnitude (from tenths of a hertz to tens of kilohertz. The frequencies corresponding to the upper boundary ($v_{\text{max}}$) were found within one order of magnitude at the level of 100 kHz.

In conclusion, we should present the following arguments. Along with the effect of pulsations of medium parameters on the process of vapor condensa- tion, an inverse effect is also possible. Both phenomena were investigated in detail by M.E. Dečich with cowork- ers (see [4, 5] and relevant references).

## REFERENCES
1. L. E. Sterin, *Foundations of Gas Dynamics for Two-Phase Flows in Nozzles* (Énergiya, Moscow, 1972).
2. D. Kashchiev, *Nucleation: Basic Theory with Applica- tions* (Butterworth Heinemann, Oxford, 2000).
3. V. V. Slezov and Yu. Schmeltser, Fiz. Tverd. Tela (St. Petersburg) **39**, 2210 (1997) [Phys. Solid State **39**, 1971 (1997)].
4. M. E. Dečich and G. A. Filippov, *Gas Dynamics of Two-Phase Media* (Énergoizdat, Moscow, 1981).
5. M. E. Dečich, *Gas Dynamics of Turbomachine Grids* (Énergoatomizdat, Moscow, 1996).

*Translated by V. Bukhanov*
