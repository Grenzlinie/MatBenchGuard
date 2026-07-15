# A New Concept of Porous Thermoelectric Module
Using a Reciprocating Flow for Cooling/Heating System
(Numerical Analysis for Heating System)

*Shigeru Tada, Ryozo Echigo and Hideo Yoshida

Dept. of Mech. Eng. & Sci., Tokyo Institute of Technology,
2-12-1 Ohokayama, Meguro-ku, Tokyo 152, Japan,
Phone ; +81-3-5734-2179, E-Mail ; stada@mech.titech.ac.jp

## Abstract
The paper presents the conceptual design of a novel thermoelectric cooler and/or heater utilizing the heat transfer effect due to forced convection. A porous thermoelectric converter combined with a reciprocating flow system in which the flow direction of air passing through the element is reversed after regular intervals is proposed. This flow system in effect makes the thermal conductivity insignificant and contributes toward the achievement of a high efficient cooler and/or heater. A one-dimensional numerical analysis is performed to examine the detailed characteristics of the porous thermoelectric heater by systematically varying the relevant thermo-fluid parameters. In the calculation, for a fixed ambient temperature of 27 [degree C], dependences of the flow velocity, material porosity, and input power on the system performance are clarified. Moreover, a series of computation is carried out in order to obtain the system's COP.

## Nomenclature

|$A$| : surface area of an equivalent particle |$[1/\text{m}]$|
|---|---|---|
|$c_p$| : specific heat of gas |$[\text{kJ/kgK}]$|
|$c_s$| : specific heat of solid |$[\text{kJ/kgK}]$|
|$d_p$| : diameter of solid particle |$[\text{m}]$|
|$h$| : heat transfer coefficient |$[\text{W/m}^2\text{K}]$|
|$h_e$| : heat transfer coefficient at the end surface |$[\text{W/m}^2\text{K}]$|
|$j$| : electric current density |$[\text{A/m}^2]$|
|$P$| : input power $(=j\times V_{Bat})$ |$[\text{W}]$|
|$Q$| : heat |$[\text{W/m}^2]$|
|$q_h$| : absorbing heat |$[\text{W/m}^2]$|
|$r_e$| : internal specific electric resistance |$[\Omega\text{m}]$|
|$T$| : temperature |$[\text{K}]$|
|$T_0$| : inlet air temperature $(=300)$ |$[\text{K}]$|
|$\overline{T}_{ex}$| : outlet air temperature |$[\text{K}]$|
|$\overline{T}_{max}$| : average temperature in porous medium |$[\text{K}]$|
|$\Delta T$| : temperature difference $(=T^+-T^-)$ |$[\text{K}]$|
|$\Delta T_0$| : temperature difference $(=\overline{T}_{max}-T_0)$ |$[\text{K}]$|
|$t$| : time |$[\text{s}]$|
|$u$| : apparent flow velocity |$[\text{m/s}]$|
|$V_{Bat}$| : battery voltage |$[\text{V}]$|
|$x$| : axial coordinate |$[\text{cm}]$|
|$x_e$| : thickness of thermoelectric module |$[\text{cm}]$|
|$x_p$| : thickness of porous material |$[\text{cm}]$|
|$Z$| : figure-of-merit $(=\alpha^2\sigma/\lambda_s)$ |$[1/\text{K}]$|

### Greek Symbols

|$\alpha$| : Seebeck coefficient |$[\text{V/K}]$|
|---|---|---|
|$\delta$| : control volume thickness |$[\text{cm}]$|
|$\epsilon$| : porosity ||
|$\lambda$| : thermal conductivity of gas |$[\text{W/mK}]$|
|$\rho$| : density |$[\text{kg/m}^3]$|
|$\sigma$| : electric conductivity $(=1/r_e)$ |$[\text{S/m}]$|
|$\tau$| : half cycle |$[\text{s}]$|
|$\phi$| : coefficient of performance (COP) ||

### Superscripts and Subscripts

|$+$| : hot junction |
|---|---|
|$-$| : cold junction |
|$J$| : Joule heat |
|$P$| : Peltier heat |
|$s$| : solid |

## Introduction
On the thermoelectric (TE) conversion system, the theoretical studies have been executed to give the technical bases and to show the most important parameter, figure of merit $Z$. Thereafter the extensive studies have been directed toward the development of materials in order to separate the heat and electric conduction processes rather than the successive effort so as to improve the efficiency of the TE device in the light of energy conversion system.

The temperature differences are produced and maintained by heat conduction for the conventional solid state TE modules. However, it is important to notice that in the porous TE modules the convective heat transfer is dominant rather than the conduction, which may results in a separation of the conduction processes for the heat and electric current [1]. The porous TE module with the reciprocating flow system in which air is introduced alternately from both ends of the device with regular intervals is one of the most prominent schemes for the TE cooling/heating system. For instance in the porous TE cooler[2], ambient air entering from the one end of the device cools the hot junction at the inlet surface and releases the waste heat at the another end until the flow direction changes. The air flowing in this way effectively decreases the temperature of the cooling region of the device. That is, this flow system in effect makes the thermal conductivity of the TE module insignificant.

In this paper, on the basis of the heat transfer mechanism of the porous TE module, the theoretical investigation of design and construction development of porous TE heating device combined with a reciprocating flow system is performed. Numerical calculations are conducted to study the effects of the relevant parameters, i.e., flow velocity, porosity of the porous materials, and input power, on the thermoelectrical conversion installed in the reciprocating flow system.

## Mathematical Formulation
Figure 1 shows a schematic view of the porous TE reciprocating flow system and physical model assuming one-dimensional flow and heat transfer. A pair of porous TE modules of thickness $x_e$ and porosity $\epsilon$ are located in an insulated channel with a spacing $x_p$. Further, a plain porous material of thickness $x_p$ with the same porosity $\epsilon$ as porous TE modules is inserted in the center space of the device. In this system, the convective heat exchange between air and porous medium is primarily important because it leads to a favourable working performance as well as adverse heat losses to the up- and downstream sides. Here, we assume the porous medium are homogeneous and all the porous medium, i.e., the porous TE modules and the plain porous medium at the center, have the same thermal properties. The insu-


![](./images/812439010315075586_1.jpg)

Figure 1: Schematics of the system

lated channel is non-porous elsewhere. For each TE module, D.C. power is supplied in order to sustain a constant electric potential between the hot and cold junctions. The flow direc- tion is reversed at the regular intervals $\tau$, which represents the half cycle of the operation. The other assumptions taken are that:
- the flow velocity is constant during each half cycle.
- the physical properties are constant.

The governing equations for heat transfer in the system are derived from the conservation laws of energy. With the pre- ceding assumptions the energy equation for both gas and solid phases, taking into account the thermoelectric terms, can be formulated as follows:
- Gas phase in free space
$$
\rho c_{p} \frac{\partial T}{\partial t}+\rho c_{p} u \frac{\partial T}{\partial x}=\lambda \frac{\partial^{2} T}{\partial x^{2}} \tag{1}
$$

- Gas phase in porous medium of porosity $\epsilon$
$$
\epsilon \rho c_{p} \frac{\partial T}{\partial t}+\rho c_{p} u \frac{\partial T}{\partial x}=\epsilon \lambda \frac{\partial^{2} T}{\partial x^{2}}-A h\left(T-T_{s}\right) \tag{2}
$$

- Thermoelectric porous medium of porosity $\epsilon$
$$
\begin{aligned}
(1-\epsilon) \rho_{s} c_{s} \frac{\partial T_{s}}{\partial t}=&(1-\epsilon) \lambda_{s} \frac{\partial^{2} T_{s}}{\partial x^{2}} \\
&+A h\left(T-T_{s}\right)+Q_{J} \tag{3}
\end{aligned}
$$

- Plain porous medium of porosity $\epsilon$
$$
\begin{aligned}
(1-\epsilon) \rho_{s} c_{s} \frac{\partial T_{s}}{\partial t}=&(1-\epsilon) \lambda_{s} \frac{\partial^{2} T_{s}}{\partial x^{2}} \\
&+A h\left(T-T_{s}\right) \tag{4}
\end{aligned}
$$

The terms in eq. (1) represent the energy balance between the conduction and convective heat of the air. The terms in eq. (2) represent an energy balance between the enthalpy change of the air and the convective heat into or out of the solid. The terms in eq. (3) represent the conducted heat and the Joule heat in the solid. The terms in eq. (4) represent an energy balance between the enthalpy change of the air and the conducted heat into or out of the solid.

The surface area of an equivalent particle per unit volume $A$ can be written in the form:
$$
A=\frac{6(1-\epsilon)}{d_{p}}. \tag{5}
$$

The heat transfer coefficient $h$ is given by:
$$
h=2 \frac{\lambda}{d_{p}}. \tag{6}
$$
where the constant "2" is the Nusselt number around a sphere in thermo-fluid mechanics.

For the cold and hot junctions, located at $x=x_{1}, x_{4}$ and $x=x_{2}, x_{3}$ respectively, boundary conditions are given by in- troducing the Peltier heat terms into the energy equations at each junction. Equations (3), (4) are integrated over the control volume $\delta$ at $x=x_{1}, \cdots, x_{4}$:
- For the cold junction at $x=x_{1}$
$$
\begin{aligned}
&(1-\epsilon) \rho_{s} c_{s} \frac{\partial T_{s}}{\partial t} \\
&=\left.\frac{1-\epsilon}{\delta} \lambda_{s} \frac{\partial T_{s}}{\partial x}\right|_{x+\delta}+\frac{Q_{P}^{-}}{\delta}+Q_{J}+A h_{e}\left(T-T_{s}\right) \quad(7)
\end{aligned}
$$

- For the cold junction at $x=x_{4}$
$$
\begin{aligned}
&(1-\epsilon) \rho_{s} c_{s} \frac{\partial T_{s}}{\partial t} \\
&=\left.\frac{1-\epsilon}{\delta} \lambda_{s} \frac{\partial T_{s}}{\partial x}\right|_{x-\delta}+\frac{Q_{P}^{-}}{\delta}+Q_{J}+A h_{e}\left(T-T_{s}\right) \quad(8)
\end{aligned}
$$
where $h_{e}$ represents the sum of the heat transfer coefficient of the porous end surface and $h$ which is the heat transfer coeffi cient between porous medium and gas phase, given by eq.(6). From the detailed investigation performed previously[2], the heat transfer coefficient $h$ is much higher than those at the end surfaces. Therefore, we assume that the end surfaces have no influence on the energy balance of the porous TE module. Namely, $h_{e}$ is approximated as:
$$
h_{e} \simeq h. \tag{9}
$$

- For the hot junction at $x=x_{2}, x_{3}$
$$
\begin{aligned}
&(1-\epsilon) \rho_{s} c_{s} \frac{\partial T_{s}}{\partial t} \\
&=\left.\frac{1-\epsilon}{2 \delta} \lambda_{s} \frac{\partial T_{s}}{\partial x}\right|_{x+\delta}-\left.\frac{1-\epsilon}{2 \delta} \lambda_{s} \frac{\partial T_{s}}{\partial x}\right|_{x-\delta} \\
&-\frac{Q_{P}^{+}}{2 \delta}+Q_{J}+A h\left(T-T_{s}\right) \tag{10}
\end{aligned}
$$

The Joule heat and the Peltier heat are evaluated in terms of the electric current density $j$ and the battery voltage $V_{B a t}$ imposed on the open circuit of the module. They are:
- Joule heat
$$
\begin{aligned}
Q_{J} &=j^{2} \frac{r_{e}}{1-\epsilon} \\
&=\frac{(1-\epsilon)\left(V_{B a t}-\alpha \triangle T_{s}\right)^{2}}{r_{e} x_{e}^{2}} \tag{11}
\end{aligned}
$$


![](./images/812439010315075586_2.jpg)

Figure 2: Temperature distribution in the device for various power input

![](./images/812439010315075586_3.jpg)

Figure 3: Temperatures as a function of current density at different battery voltage $V_{Bat}$

• Peltier heat

$$
\begin{aligned}
Q_{P}^{ \pm} &=j \alpha T_{s}^{ \pm} \\
&=\frac{(1-\epsilon)\left(V_{B a t}-\alpha \triangle T_{s}\right) \alpha T_{s}^{ \pm}}{r_{e} x_{e}}
\end{aligned} \tag{12}
$$

## Results and Discussion

Here, the figure-of-merit of the porous TE modules is assumed to be $ZT_0 = 1$, which is the most likely performance for future TE materials. Other relevant physical properties are assumed to be the same as for $\text{Bi}_2\text{Te}_3$-based TE materials.

The flow velocity $u$ ( or the TE module thickness $x_e$ ) and porosity of materials $\epsilon$ are expected to be the most important parameters which directly affect the device performance so that a series of computations to systematically study their influence was carried out. The thickness of the porous TE module $x_e$ and of the porous material $x_p$ were taken to be 2.5 cm and 5 cm, respectively. The half cycle of the operation is fixed to $\tau$=10 s. During calculations, a relative convergence criterion of $10^{-6}$ was specified for the iterations and an overall energy balance of approximately 1% ( maximum 4% ) was achieved for most of the cases.

![](./images/812439010315075586_4.jpg)

Figure 4: Temperatures as a function of current density for various flow velocity $u$

Figure 2 shows the typical air temperature distribution developed within the device. Figure shows the temperature profiles at the end of a half cycle $\tau$ just before the flow direction is reversed. It can be seen that inside both porous TE modules, temperature distributions with steep gradients are sustained and that the portion with the highest temperature in the device is established along the entire length of the center porous medium ($x$=5~10cm). Air of initially ambient temperature $T_0$=27 °C coming from the outside with velocity 0.35 m/s is cooled when it reaches the cold junction ($x_1$=2.5cm). Thereafter, the temperature rapidly increases as the air travels through the porous TE module, until it reaches the upstream hot junction ($x_2$=5cm). The air passes through the center porous medium with constant temperature until it reaches the downstream hot junction ($x_3$=10cm). Here, the air is further heated by the Peltier heat generation before it is cooled with distance $x_e$ from $x = x_3$, and finally leaves the porous body with a temperature $T_{ex}$ at $x_4$=12.5cm. The heat conducting from the heating region back to the cold part is markedly reduced. Furthermore, cold junctions located at both ends of the system are always heated by the inlet air of room temperature or the exhaust air which leaves the system. Therefore, the hot junction whose temperature is related to that of cold junction through the Seebeck effect is able to sustain a higher temperature than that of the conventional TE module without any additive heat source for the cold side.

Figure 3 shows the dependence of the air temperatures at the heating region and outlet on the current density at different battery voltage $V_{Bat}$. The "temperature at the heating region" is the time average of the mean air temperature within the center porous material. The "outlet temperature" is also the time averaged temperature of the exhaust air. The porosity of the material $\epsilon$, air velocity $u$, and half cycle $\tau$ were kept constant; they were $\epsilon$=0.5, $u$=0.35 m/s and $\tau$=10 s , respectively. Temperatures of the air at the heating region and outlet increase parabolically with the increase in the input power $P$ $(=j \times V_{Bat})$. The temperature difference between the heating region and outlet also increases with increasing $V_{Bat}$. For lower input powers, temperatures of the heating region and outlet take almost the same value, however for $V_{Bat}$=17 ($\times$ 0.708 V), temperature difference between them becomes $\sim 310$ °C.

Figure 4 shows the dependence of the temperatures at the heating region and outlet on the flow velocity $u$. Temperatures of the air both at the heating region and outlet of

![](./images/812439010315075586_5.jpg)

Figure 5: Temperatures as a function of current density at different material porosity $\epsilon$

the device decrease with increasing air velocity. Contrasting with the temperature at the heating region, that gradually decreases with the increase in the flow velocity, the outlet air temperature rapidly decrease over the range where the air velocity is smaller than $\simeq 0.5$ m/s. For higher velocity greater than $u$=0.5 m/s, outlet temperature asymptotically closes to the room temperature with increasing flow velocity. In addition, the current density also increases when the air velocity increases. The reason is as follows. In the calculation, the electric potential between the hot junction and cold electrode was kept constant during the operation. Therefore, even if the amount of heat transferred by convection to the outside becomes greater, the system can compensate for such a heat loss by the "ideal" power source which would be able to infinitely supply the electric energy to the system.

Figure 5 shows the dependence of the temperature of the heating region and outlet on the material porosity $\epsilon$. A larger value of $\epsilon$ means that the mesh of the porous medium is denser. For $\epsilon$=0.1, the temperature of air rises from $27\ ^{\circ}\text{C}$ to $167\ ^{\circ}\text{C}$ at the heating region. The outlet temperature for $\epsilon$=0.1 is $52\ ^{\circ}\text{C}$. The temperature of the heating region gradually decreases with increasing porosity of the porous medium while the outlet air temperature hardly decrease. As the calculation were carried out under the condition of a constant mass flow rate, the flow velocity inside the porous media increases with the increase in material porosity $\epsilon$; leading to a stronger heat convection by the air flow.

Figure 6 shows both the dependence of the rate of heat release $q_h$ on the electrical current density $j$ and COP of heating mode for several temperature differences $\Delta T_0(=\overline{T}_{max}-T_0)$. The COP for the overall heating cycle $\psi$ in the present device is defined as:

$$
\psi = \frac{\text{heat release}}{\text{required input}} = \frac{q_h}{P}, \tag{13}
$$

where the "heat release" is the heat transfer from the heating region to the ambient air and the "required input" is the electric power necessary to generate such a heat release. In the calculations, heat sinks are located on both end surfaces of the center porous medium. The rate of the heat absorption is varied for each calculation in order to evaluate the system performance.

The device performance parameters to be calculated are specified at a constant inlet air temperature $T_0$=300 K, contrary to that conventionally specified at a constant cold junction temperature, since the cold junction temperature $T_s^-$ plays a minor role in evaluating the COP of the device.

![](./images/812439010315075586_6.jpg)

Figure 6: $\triangle T_0$ and COP ( $u$=0.35 m/s, $\epsilon$=0.5, $\tau$=10 s )

The heating performance gradually decreases with respect to the increase in the temperature difference $\Delta T_0$. Furthermore, the result shows a higher performance than that of conventional TE modules. This is because in conventional TE modules which consist of heat sink, TE module and cold sink, significant thermal resistances existing between the heat sink and the hot junction, and between the cold junction and the cold sink, can not be avoided. In other words, in the proposed device, the heat is mainly transferred by the effect of convection, unlike in conventional TE modules. Therefore, thermal resistances present among constituent items have fairly small influence on the device performance.

### Concluding Remark
A porous thermoelectric module employing a reciprocating flow for heating system is proposed. A set of basic equations which governs the heat transfer within the system is solved numerically. The dependence of temperatures of the heating part and outlet air on the imposed power, flow velocity of the air, and the porosity of the material is clarified. Moreover, a set of COP curves for overall heating cycle is obtained through the additional parameterised calculations.

Although discussion herein is just limited on showing a highly potential of the corresponding system as a heater and/or cooler, results presented in the paper indicate that a properly designed porous TE heater is expected to be a novel TE heating device having markedly higher performance than the conventional TE device.

### References
[1] R. Echigo, et al., "An Extended Analysis on Thermodynamic Cycle of Advanced Heating/Cooling Method by Porous Thermoelectric Conversion Device", 12th ICT, Yokohama, JAPAN, VI-5(1993).

[2] S. Tada, et al., "A New Concept of Porous Thermoelectric Module Using a Reciprocating Flow for Cooling/Heating System", 15th ICT, Pasadena, U.S.A, 264(1996).
