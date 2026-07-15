# MICROCHANNEL & MINICHANNEL HEAT EXCHANGERS IN ADVANCED ENERGY RECOVERY & CONVERSION SYSTEMS

Terry J. Hendricks

Computational Mechanics Division
Energy Science & Technology Directorate
Pacific Northwest National Laboratory¹
902 Battelle Boulevard
Richland, WA 99352

## Abstract
Energy recovery is gaining importance in various industrial process applications because of rising energy costs and geopolitical uncertainties impacting basic energy supplies. Various advanced energy recovery / conversion technologies will require high-performance heat transfer characteristics typical of micro- and mini-channel heat exchangers to achieve energy recovery performance targets and requirements. Initial engineering scoping studies have focused on advanced thermoelectric generator (TEG) systems assuming exhaust gas temperatures of 1033 K (1400 °F) and ambient environment temperatures of 300 K. The engineering analysis used a coupled, integrated thermoelectric (TE) system analysis accounting for the heat exchange / heat transfer performance at both the hot and cold sides and optimum TE device performance to properly predict the power output potential, resulting temperatures and temperature differentials, TEG design and interface requirements, and thermal characteristics across a wide spectrum of potential operating temperature conditions. Modular TEG's capturing about 5% of typical industrial process (e.g., glass manufacturing process) exhaust flows appear to have potential power outputs of 4 – 6 kW using advanced TE materials. Hot-side & cold-side heat exchange requirements were quantified and performance metrics evaluated to enable effective implementation of advanced TEG systems in industrial process energy recovery. Hot side heat transfer requirements create serious engineering, and possibly, scientific challenges to enabling energy conversion systems, including TEG's, in industrial process energy recovery. Future advanced heat transfer R&D is necessary and should occur in parallel with on-going advanced TE materials and systems R&D.

## Nomenclature
**English**
| Symbol | Definition |
|--------|------------|
| $A_{cr}$ | -Cross-sectional flow area [$m^2$] |
| $A_p$ | - p-type element area [$m^2$] |
| $A_n$ | - n-type element area [$m^2$] |
| $A_{tot}$ | - Total heat transfer area [$m^2$] |
| $C_p$ | - Specific heat of gas/liquid stream [J/kg-K] |
| $C_{min}$ | - Minimum heat exchanger fluid capacity rate [W/K] |
| $C_{max}$ | - Maximum heat exchanger fluid capacity rate [W/K] |
| $D$ | - Hydraulic diameter [m] |
| $f$ | - Friction factor |
| $G$ | - Mass flux rate or mass velocity [$kg/m^2$-sec] |
| $h$ | - Heat transfer coefficient [$W/m^2$–K] |
| $H_{ch}$ | - Channel height [m] |
| $K_c$ | - Abrupt contraction loss coefficient |
| $K_e$ | - Abrupt expansion loss coefficient |
| $L$ | - TE element length [m] |
| $\dot{m}_c$ | - Cold-side (ambient) mass flow rate [kg/sec] |
| $\dot{m}_h$ | - Hot-side (exhaust) mass flow rate [kg/sec] |
| $N$ | - Number of thermoelectric couples |
| $Nu$ | - Nusselt number |
| $NTU$ | - Number of Heat Transfer Units |
| $P$ | - Device power [W] |
| $q_h$ | - Hot-side thermal energy transfer [W] |
| $q_c$ | - Cold-side thermal energy transfer [W] |
| $R_{th,c}$ | - Cold-side TE/HX interface thermal resistance [K/W] |
| $R_{th,h}$ | - Hot-side TE/HX interface thermal resistance [K/W] |
| $Re$ | - Reynolds number |
| $T_{amb}$ | - Ambient temperature [K] |
| $T_{ex}$ | - Exhaust gas temperature [K] |

¹ Operated for the U.S. Department of Energy by Battelle Memorial Institute under Contract DE-AC05-76RL01830

© 2006 by Battelle Memorial Institute

$T_{\rm h}$ - TE hot-side temperature [K]
$T_{\rm c}$ - TE cold-side temperature [K]
UA - Effective heat exchanger conductance x area [W/K]
V - Device voltage [V]
$w_{\rm ch}$ - channel width [m]

__Greek__
$\Delta P$ - Pressure differential across heat exchanger [N/m²]
$\varepsilon$ - Heat Exchanger effectiveness
$\varepsilon_{\rm c}$ - Cold-side heat exchanger effectiveness
$\varepsilon_{\rm h}$ - Hot-side heat exchanger effectiveness
$\Gamma$ - Heat Transfer / Pumping Power Factor
$\eta$ - Thermoelectric conversion efficiency
$\lambda_{\rm p}$ - p-type element aspect ratio, $L/A_{\rm p}$ [m⁻¹]
$\lambda_{\rm n}$ - n-type element aspect ratio, $L/A_{\rm n}$ [m⁻¹]
$\kappa$ - thermal conductivity [W/m-K]
$\sigma$ - Parasitic heat loss fractions

__Subscripts__
c or cold - Cold-side of TE device
ch - Channel related
ex - Associated with heat exchanger
gas - Exhaust gas side
h or hot - Hot-side of TE device
i - n- or p-type element specification
pp - Peak power condition
TE - Associated with TE device
w - Water side

### Introduction
Researchers and designers of advanced light-duty and heavy-duty vehicles, and large energy-intensive industrial processes, are investigating the use of waste heat recovery to improve fuel economy, improve system energy efficiencies, and lower emissions and operating costs. Consequently, direct thermal energy recovery/conversion technologies to produce high-grade electrical energy from waste energy in transportation and industrial processes are receiving more research attention. Recent studies indicate there are about 5.8 Quads ($10^{15}$ Btus) of waste thermal energy dissipated nationwide in a number of industrial, petroleum, and chemical processes across a wide range of temperatures [1]. A significant fraction of this waste thermal energy occurs at high temperatures. Investigations are on-going comparing system power benefits and system thermal integration challenges of energy recovery / conversion systems using microchannel heat exchangers to provide high heat transfer performance on both high-temperature, high-enthalpy energy streams and low-temperature cooling streams. High-temperature thermal energy is available at various locations in industrial processes such as glass, aluminum, ethylene, and cement processing. Integrated system modeling and analyses are providing critical information on how much power would be available at various locations in exhaust streams of industrial processes, as well as critical heat exchanger design details for proposed systems. This paper discusses and compares microchannel integration requirements for various energy recovery technologies; heat exchanger system design details; system challenges, characteristics, and sensitivities of various microchannel design parameters. This work focuses on thermoelectric (TE) and piezoelectric (PE) energy recovery / conversion systems as current prime applications. Several Department of Energy (DOE) programs can ultimately benefit from this research in advanced microchannel heat exchanger design, including DOE's Waste Heat Recovery and Utilization project and Industrial Technology programs.

Hendricks and Lustbader [2,3,4] discuss the TE system-level analysis approach, where the heat exchanger performance is directly and simultaneously coupled with the thermoelectric device performance, to simultaneously analyze and characterize the expected heat transfer requirements and power available in various vehicle and industrial applications. The TE analysis defines optimum TE designs that maximize TE device conversion efficiency, while simultaneously coupling TE device performance to heat exchanger performance, for a variety of $T_{\rm h}$ and $T_{\rm c}$ combinations and a given $T_{\rm exh}$. This system analysis technique provides a system-level extension of TE device optimization techniques presented by Angrist [5] and Rowe [6]. This work has used this system-level analysis in parametric analyses to evaluate critical mass flow and heat exchanger UA requirements on the cold side and hot side of advanced TE systems. The work then investigates a spectrum of potential specific microchannel designs that can satisfy hot and cold-side heat exchanger requirements and various design tradeoffs. Crane and Jackson [7] have performed similar investigations where the heat exchanger was fixed and defined by heat exchanger design parameters, but did not specifically address microchannel designs.

### Microchannel Interface Requirements in Advanced Energy Conversion Systems
Many waste energy recovery applications in today's environment are requiring energy recovery solutions that are compact, environmentally friendly, with no noise, vibration, ozone-impacting fluids, and highly reliable with very few or no moving parts. Advanced, solid-state direct energy conversion systems (i.e., thermoelectric) envisioned in the future for these waste energy recovery applications generally require a temperature differential be maintained across the device while thermal energy is transferred in / out of the system. Piezoelectric generators, as they are currently envisioned [8], would operate at nearly isothermal conditions themselves, but there would be temperature differentials across the system (at hot- and cold-side heat exchangers) to transfer thermal energy into / out of the system. In any event, nearly isothermal interfaces are required on the hot- and cold-sides of the energy conversion device to achieve predictable maximum performance conditions. Therefore, heat exchanger configurations that transfer the thermal energy in / out of the energy device must be capable of providing and operating at these nearly isothermal conditions on the interfaces with the energy conversion device.

© 2006 by Battelle Memorial Institute

Kays and London [9] provide a comprehensive review and analysis of various basic heat exchanger configurations, counterflow, parallel flow, crossflow, and parallel counterflow. They describe the ε - NTU method of heat exchanger analysis used in this work. It is clear from Kays and London [9] that heat exchanger effectiveness, ε, is generally expressed by the following relationship for any flow configuration,

$$
\varepsilon=\varphi\left[N T U,\left(C_{\min } / C_{\max }\right), \text { flowconfiguration }\right] \text { (1) }
$$

Generally the $\varepsilon$ relationship in Eq. 1 is a rather complex relationship for the various heat exchanger flow configurations. In a heat exchanger that is providing or creating a nearly isothermal interface on one side as it transfers thermal energy the ratio:

$$
\left[C_{\min } / C_{\max }\right] \rightarrow 0 \tag{2}
$$

And the Eq. 1 relationship generally simplifies to:

$$
\varepsilon=1-\exp \left[\frac{-U A}{C_{\min }}\right] \tag{3}
$$

In the advanced waste energy recovery and conversion systems considered in this work, any microchannel heat exchangers coupling with the advanced energy conversion system must satisfy the nearly isothermal interface condition and will therefore closely follow the $\varepsilon$ relationship in Eq. 3. UA, the overall heat transfer conductance times the heat transfer surface area, and $C_{\min }$ are defined by Kays and London [9].

In the energy recovery applications found in the transportation sector and industrial processing sector, there is generally a large amount of waste energy available to be captured and converted. This can range from 10's of kilowatts to Megawatts of available thermal energy. There is also a general requirement to develop compact, light-weight, and low-cost energy conversion and heat exchange systems. Therefore, in almost all applications the heat exchange systems must satisfy a general requirement to transfer very high heat fluxes (i.e., 50-300 Watts/cm²) across nearly isothermal interface conditions. This is particularly true of the unique energy conversion systems using advanced conversion materials envisioned in the next 5-10 years. Microchannel heat exchangers are one heat transfer technology that is capable of providing this performance.

### Advanced Thermoelectric Systems Requirements

Recent advances in advanced TE materials have created new opportunities to use advanced thermoelectric generator (TEG) systems in high-temperature, industrial glass process energy recovery where exhaust gases contain significant recoverable energy. Initial engineering scoping studies have been performed assuming exhaust gas temperatures of 1033 K (1400 °F) and ambient environment temperatures of 300 K.

Figure 1 shows a schematic of the typical TEG system-level configuration considered in this study and the associated thermal flows. The power output from any advanced TEG system depends strongly on the absolute temperatures and temperature differentials maintained across the TEG and the TE materials used in the TEG, as thermal energy is delivered on the hot side and dissipated on the cold side. It is envisioned that advanced heat exchange/transfer mechanisms will be employed on both hot and cold sides of the system to deliver thermal energy to the TE device and provide the necessary cooling. The hot side heat exchanger absorbs heat from the glass process exhaust stream at $T_{ex}$, transfers that thermal energy to the TE device hot side at $T_{h}$, the TE device converts that thermal energy at a predictable conversion efficiency, the remaining unconverted thermal energy is transferred from the TE device cold side at $T_{c}$ to the cold side heat exchanger, and dissipated to the ambient environment at $T_{amb}$. This engineering analysis used a coupled, integrated TE system analysis accounting for the heat exchange / heat transfer performance at both the hot and cold sides and optimum TE device performance to properly predict the power output potential from the TEG, resulting temperatures and temperature differentials, TEG design and interface requirements, and thermal characteristics across a wide spectrum of potential operating temperature conditions.

Although advanced TE systems are the focus in this paper, similar system-level analyses are appropriate and possible with other energy conversion technologies such as piezoelectrics, thermionics, or thermophotovoltaics. These engineering scoping studies have provided valuable technical insights, understanding of sensitivities, potential benefits, system-level requirements, and potential technical barriers affecting R&D program planning and funding decisions.

Understanding the efficiency - power relationship of an advanced TE system is critical to evaluating sensitivities, potential benefits, and system-level requirements. Figure 2 demonstrates the typical efficiency - power relationship of an advanced TE system operating across the ultimate bounding exhaust-gas-to-ambient temperature differential given above for various possible combinations of $T_{h}$ and $T_{c}$. This analysis was performed for hot-side heat exchanger performance, $UA_{h}$ = 250 W/K and advanced TE materials with temperature-integrated ZT = 2. This relationship, previously presented and discussed by Hendricks and Lustbader [2-4, 10], shows the effect of the strong coupling between heat exchanger performance and TE energy conversion performance. It provides the foundation for evaluating thermal energy flows, potential power benefits, operating points, and subsequent system requirements. In particular, it clearly distinguishes points of maximum power production from those of maximum conversion efficiency, and provides insight into optimum operating points in energy recovery applications.

The power output at each point on the efficiency-power map, including the maximum power point, is strongly impacted by the hot-side mass flow rate, $\dot{m}_{h}$, and heat exchanger performance parameter, $UA_{h}$. Figure 3 displays the maximum point output dependency on $UA_{h}$ for two different TE material ZT values. Higher $UA_{h}$ performance

© 2006 by Battelle Memorial Institute

![](./images/811927998176428032_1.jpg)

Figure 1 – Advanced TE System Schematic & Thermal Flow

![](./images/811927998176428032_2.jpg)

Figure 2 – Maximum Efficiency–Power Output Map for Typical Glass Process Energy Recovery (ZT=2 TE Materials)
- $\text{UA}_\text{h} = 250$ W/K, $\text{T}_\text{ex} = 1033$ K, $\text{T}_\text{amb} = 300$ K

creates more thermal energy throughput into the TE device, and therefore higher maximum power output for given conversion efficiencies. The newest, advanced TE materials have material properties characteristic of temperature-integrated ZT ~ 2 [11-14], while TE materials with temperature-integrated ZT ~ 4 have been speculated as possible by some TE researchers. The $\text{UA}_\text{h}$ dependency is of most importance here and Figure 3 data shows the point of diminishing returns at about $\text{UA}_\text{h}$ ~ 300 W/K in either ZT case. This is important because higher $\text{UA}_\text{h}$ tends to create higher heat exchanger costs, either due to higher heat transfer area requirements or employing more exotic heat transfer processes and techniques. This relationship in Figure 3 helps one establish the "target zone" for hot-side heat exchanger performance in advanced TE systems directed toward glass industry energy recovery, which in this case is $\text{UA}_\text{h} = 250$-300 W/K. Going above this level creates higher system costs for smaller power output benefits.

![](./images/811927998176428032_3.jpg)

Figure 3 – Maximum Power Dependency on Hot-Side Heat Exchanger Performance, $\text{UA}_\text{h}$ - 5% of Total Exhaust Flow, $\text{T}_\text{amb} = 300$ K

Figure 4 shows the TE device area requirements using the advanced TE materials with ZT ~ 2. These TE material area requirements are much lower than required for older ZT ~ 1 TE materials that exist in current day TEG's. Figure 4 data shows that more TE material area is required as $\text{UA}_\text{h}$ increases, but a flattening out occurs just as in the Figure 3 power data, at $\text{UA}_\text{h} = 500$ W/K. This suggests that TE power density is staying relatively constant. The hot side heat exchanger "target zone" is depicted in Figure 4 with associated TE device area requirements of 100 – 110 $\text{cm}^2$ for ZT ~ 2 TE materials.

The coupled, integrated TE system analysis also predicts the required cold-side mass flow rate and heat exchanger performance, $\text{UA}_\text{c}$, necessary to satisfy the cooling requirements on the system cold side. Cold-side cooling requirements are also dependent on the hot-side heat exchanger mass flow rate, $\dot{m}_h$, and $\text{UA}_\text{h}$ performance as these two dictate the thermal energy throughput, and therefore cold-side thermal energy dissipation, in the TEG system. Figure 5 shows the resulting relationship between cold-side cooling requirements and hot-side heat exchange conditions for industrial-glass-process analysis cases represented in Figures 2 and 3. The cold-side mass flow rate, $\dot{m}_c$, and $\text{UA}_\text{c}$ requirements are clearly depicted for the hot- side heat exchanger performance "target zone". In these cases, $\text{UA}_\text{c}$ ~

© 2006 by Battelle Memorial Institute

![](./images/811927998176428032_4.jpg)

Figure 4 – TE Area Requirements Dependency on Hot Side Heat Exchanger Performance, $UA_h$ - 5% of Total Exhaust Flow, $T_{amb}=300$ K

![](./images/811927998176428032_5.jpg)

Figure 5 – Required Cold-Side Mass Flow Dependency on Hot-Side Heat Exchanger Performance, $UA_h$

1780-1800 W/K and $\dot{m}_c=0.15-0.2$ kg/sec are necessary to satisfy cold-side cooling requirements for industrial glass TEG modules envisioned using advanced TE materials characterized by ZT = 2-4.

Figures 3, 4, and 5 give the general heat exchanger requirements that must be achieved to generate the power outputs shown in Fig. 3. It also is assumed that load matching requirements are met in the industrial application.

## Specific Microchannel Performance Characteristics

Various microchannel heat exchanger designs were investigated to identify possible design solutions to satisfy hot- and cold-side heat transfer requirements and critical design sensitivities in advanced thermoelectric systems. Microchannel designs were researched because they can provide high heat transfer performance in light-weight, compact designs. The investigation centered on what heat transfer performance was possible with various pumping power costs on both cold- and hot-side heat exchangers.

Cold Side Heat Exchanger - Water Cooling. In many industrial energy recovery applications, water at temperatures near 300 K is available for cooling the system cold side. The microchannel designs investigated were plate-fin configurations with the fin heights varying from 0.1 inch to 0.2 inch and microchannel widths varying from ~ 80 $\mu$m to 300 $\mu$m. Cold side heat exchanger studies focused on quantifying the $UA_c$ , as defined in Kays and London [9], possible using water cooling and interface TE device area requirements.

Water-cooled microchannel designs investigated here assumed fully-developed flow conditions, and generally exhibited laminar flow characteristics because of the small channel characteristic dimensions. Consequently, the heat transfer was generally defined by Nusselt number correlations of the form:

$$
Nu_D=\left[\frac{h_w \cdot D}{\kappa_w}\right]=g\left(\frac{H_{ch}}{w_{ch}}\right) \tag{4}
$$

where $H_{ch}$ and $w_{ch}$ are the channel rectangular dimensions. The typical Nu relationships used are given in Kays and London [9] and Kays and Crawford [16] for fully-developed laminar flow, constant heat rate cases. The heat transfer coefficient, $h_w$, the TE area requirements from Fig. 4, heat exchanger dimensions, and the cold-side mass flow rate requirements from Fig. 5 were then used to estimate $UA_c$ , estimate $\varepsilon_c$ from Eq. 3, and determine the total heat transfer, $Q_c$ given by [2]:

$$
Q_c=\frac{\left(T_c-T_{a m b}\right)}{\left(\frac{\left(1.-\sigma_{e x, c}\right)}{\dot{m}_c \cdot C_{p, c} \cdot \varepsilon_c}+R_{t h, c}\right) \cdot\left(1-\sigma_{T E, c}\right)} \tag{5}
$$

where $R_{th,c}$ was initially set at 0.0004 K/W and heat loss factors, $\sigma_{ex,c}$ and $\sigma_{TE,c}$ were set at 0.075. The $UA_c$ values were determined from equations and techniques described in Kays and London [9] and properly accounting for fin efficiencies and base material thermal conductance.

The amount of pumping power was also determined for these water microchannel designs. The pressure drop was estimated from relationships in Kays and London [9]:

$$
\Delta P=F\left(G, f, \frac{A_{t o t}}{A_{c r}}, K_c, K_e\right) \tag{6}
$$

© 2006 by Battelle Memorial Institute

where the friction factor, $f$, was determined by relationships in White [15]:

$$
f \cdot \operatorname{Re}=h\left(\frac{H_{c h}}{w_{c h}}\right) \tag{7}
$$

and $\mathrm{K}_{\mathrm{c}}$ and $\mathrm{K}_{\mathrm{e}}$ where determined by relationships in Kays and London [9]. The necessary cold-side pumping power, $\mathrm{P}_{\text{pump,c}}$ was determined by:

$$
P_{p u m p, c}=\dot{m}_{c} \cdot \Delta P \tag{8}
$$

Figure 6 shows the resulting $\mathrm{UA}_{\mathrm{c}}$ vs. pumping power for a 12.4 cm wide x 12.4 cm long x 0.6 cm high, copper microchannel heat exchanger design at water mass flow rates of 0.15 kg/sec and 0.18 kg/sec. Microchannel heights, $\mathrm{H}_{\mathrm{ch}}$, varied from 0.25 cm (0.10 inch) to 0.41 cm (0.16 inch) and micro channel widths, $\mathrm{w}_{\mathrm{ch}}$, varied from $82 \mu \mathrm{m}$ to $285 \mu \mathrm{m}$. Fin density was determined by microchannel width and the overall 12.4 cm width constraint. The 12.4 cm x 12.4 cm design would approximately match the TE area requirements shown in Figure 4 for ZT ~ 2 conditions, with a small area allowance for internal spacings and fabrication within the TE device.

There are several important design sensitivities and tradeoffs demonstrated in Figure 6. The sensitivity of $\mathrm{UA}_{\mathrm{c}}$ with pumping power as microchannel width is decreased is clearly evident. Initially large increases in $\mathrm{UA}_{\mathrm{c}}$ occur for correspondingly small increases in pumping power as microchannel widths decrease from $285 \mu \mathrm{m}$ to $\sim 116 \mu \mathrm{m}$. This is a very desirable design regime. This is followed by smaller, diminishing return increases in $\mathrm{UA}_{\mathrm{c}}$ as pumping power increases sharply when microchannel width reduces below $116 \mu \mathrm{m}$. This is an undesirable design regime and one to be avoided. This is a consistent effect at water mass flow rates of 0.15 kg/sec and 0.18 kg/sec.

The effect of increasing microchannel height also is clearly demonstrated in the Figure 6 results. Increasing microchannel height clearly drives the designs toward higher $\mathrm{UA}_{\mathrm{c}}$ and lower pumping power, an important desirable effect in the advanced TE systems design.

Finally, Figure 6 data shows the effect of larger mass flow rate is to simply increase the pumping power. This demonstrates one of the important characteristics of microchannel heat exchangers, that the heat transfer coefficient and $\mathrm{UA}_{\mathrm{c}}$ are de-coupled from mass flow velocity and therefore, the pressure drop. This can, however, affect the heat exchanger effectiveness, however, through Eq. 3.

The thermal entry lengths, estimated using techniques in Kays and Crawford [16] for the Figure 6 conditions, were approximately 1-2 cm. This confirms and justifies the fully developed flow conditions assumed for the analyses in Figure 5, since total flow lengths were 12.4 cm.

The critically important performance parameter is of course the heat transfer, given in Eq. 5, created by the various designs in Figure 6. It is necessary to refer to Figure 2 to determine the TE hot and cold side temperatures desired from the various potential operating points illustrated on the maximum efficiency vs. power map. For the purposes of this work, it is assumed one would operate along the $\mathrm{T}_{\text{cold}}\left(\mathrm{T}_{\mathrm{c}}\right)=$ 390 K curve in Figure 2, resulting in $\left(\mathrm{T}_{\mathrm{c}}-\mathrm{T}_{\mathrm{amb}}\right)=90 \mathrm{~K}$. This allows one to convert the Figure 6 data into heat transfer rates and determine the heat transfer/pumping power factor, $\Gamma$, expressed as:

$$
\Gamma=\left[\frac{Q_{c}}{P_{p u m p, c}}\right] \tag{9}
$$

![](./images/811927998176428032_6.jpg)

Figure 6 - Microchannel Heat Exchanger $\mathrm{UA}_{\mathrm{c}}$ vs. Pumping Power in Various Water-Copper Microchannel Designs

This important factor, serving as a heat exchanger figure-of-merit, fundamentally differentiates the various designs by quantifying how much heat transfer a given design is creating for the pumping power expended. What values of $\Gamma$ are acceptable are highly application-specific. In this particular application, heat transfer is highly valued and pumping power is an expensive parasitic, so low pumping power and high heat transfer (i.e., high $\Gamma$) is necessary. In other applications, pumping power may not be as valuable a commodity or important to mission success, so a lower $\Gamma$ could be tolerated. In any design and application, knowing $\Gamma$ and its sensitivity to various design parameters or environmental variables allows one to make intelligent design decisions up front.

Figure 7 demonstrates $\Gamma$ and $\mathrm{Q}_{\mathrm{c}}$ for the various microchannel designs in Figure 5 and quantifies the sensitivity of $\Gamma$ and $\mathrm{Q}_{\mathrm{c}}$ to increasing microchannel height and microchannel width. The cold side heat transfer requirement for advanced TE designs in Figure 3 using ZT ~ 2 and ZT ~ 4 TE materials are shown on the $\mathrm{Q}_{\mathrm{c}}$ axis. Intersection of these requirement lines with $\mathrm{Q}_{\mathrm{c}}$-lines determines the microchannel heights and widths that satisfy design requirements associated with advanced TE designs in Figure 3. Vertical lines drawn from these intersection points that then intersect the $\Gamma$-lines establish the heat transfer / pumping power ratio for the

© 2006 by Battelle Memorial Institute

![](./images/811927998176428032_7.jpg)

Figure 7 - Heat Transfer/Pumping Power Factor and Total Cold-Side Heat Transfer in Various Water-Copper Microchannel Designs

appropriate microchannel design. The ZT ~ 2 and ZT ~ 4 lines show that advanced TE designs using ZT ~ 2 materials generally will need narrower microchannel widths for a given microchannel height with a lower $\Gamma$ factor. The TE materials used in the advanced TE system and cold-side microchannel thermal design are therefore inextricably linked via the cold- side heat transfer.

Figure 7 also quantifies the link between increasing microchannel height that allows increased microchannel widths, and therefore higher $\Gamma$ factors, that satisfy the fundamental cold-side heat transfer requirement.

Figure 7 data demonstrates that water microchannel designs do exist with very high $\Gamma$ factors, on the order of 2000 to 4000, that satisfy the cold side thermal requirements. These represent highly efficient designs giving heat transfers 2000 to 4000 times the pumping power needed. Therefore, it is clear that cooling the cold side in advanced TE systems for industrial process applications is well within current capabilities and will require small pumping powers.

Hot Side Heat Exchanger - Exhaust Gas Energy. The exhaust gas flows in industrial glass processes are typically very large (e.g. ~ 6-9 kg/sec). It was decided early on that the TEG system should be designed in a modular fashion to efficiently design the systems for flow length temperature gradient effects, maintaining adequate TEG temperature isothermality, controlling pressure drops and pumping power, effectively packaging the TEG system within the glass exhaust system dimensions, and providing a logical module trial and growth plan in the industrial physical and business environment. A typical TEG "building-block" module appeared to be one designed to intercept approximately 5% of the total glass process exhaust flow at an exhaust flow temperature of 1400 F (1033.2 K). Consequently, the exhaust gas flow rate was assumed to be 0.3 kg/sec for this analysis.

Exhaust gas compositions in industrial glass exhaust flows typically have various combinations of $CO_{2}, H_{2} O, N_{2}$, and $O_{2}$. These compositions have thermophysical properties that are slightly modified from those of air, but generally are within about 10-20% of the thermophysical properties of air. As a result, the exhaust gas flow analyses for engineering scoping studies assumed air thermophysical properties, with the intent of making small corrections as necessary for thermophysical property variations.

Various hot-side heat exchanger designs were investigated using analysis techniques discussed above, with the important difference that flow in the heat exchanger was necessarily considered to be fully developed turbulent flow. Consequently, the heat transfer was determined by the Nusselt number relationship given by Gnielinski [17]:

$$
N u_{D}=\left[\frac{h_{g a s} \cdot D}{\kappa_{g a s}}\right]=\frac{(f / 8) \cdot\left(\operatorname{Re}_{D}-1000\right) \cdot \operatorname{Pr}}{1+12.7 \cdot(f / 8)^{1 / 2} \cdot\left(\operatorname{Pr}^{2 / 3}-1\right)} \quad(10)
$$

where the friction factor is defined by:

$$
f=\left(1.82 \cdot \log _{10} \operatorname{Re}_{D}-1.64\right)^{-2} \quad(11)
$$

The heat transfer coefficient, $h_{gas}$, the TE area requirements from Fig. 4, heat exchanger dimensions, and the hot-side mass flow rate of 0.3 kg/sec were then used to estimate $UA_{h}$, estimate $\varepsilon_{h}$ from Eq. 3, and determine the total heat transfer, $Q_{h}$ given by [2]:

$$
Q_{h}=\frac{\left(T_{e x}-T_{h}\right) \cdot\left(1-\sigma_{T E, h}\right)}{\left(\frac{1}{\dot{m}_{h} \cdot C_{p, h} \cdot \varepsilon_{h} \cdot\left(1-\sigma_{e x, h}\right)}+R_{t h, h}\right)} \quad(12)
$$

where $R_{th,h}$ was initially set at 0.00035 K/W and heat loss factors, $\sigma_{ex,h}$ and $\sigma_{TE,h}$ were set at 0.025. The $UA_{h}$ values were determined from equations and techniques described in Kays and London [9] and properly accounting for fin efficiencies and base material thermal conductance. The gas flow pressure drop, $\Delta P$, was determined from Eqs. 6 and 11, which then allowed one to determine the necessary hot-side exhaust gas pumping power, $P_{pump,h}$ from an equation similar to Eq. 8.

Figure 8 shows the resulting $UA_{h}$ vs. pumping power for 17.8 cm wide x 11.1 cm length x 7.3 cm high copper heat exchanger designs at an exhaust flow rate of 0.3 kg/sec. This set of designs was seeking a $UA_{h} \sim 100$ W/K, and therefore was not satisfying the "target zone" hot side requirements shown in Figures 2-4. Because of the decreased gas densities, these heat exchanger designs are much larger than the cold- side water microchannel designs shown in Figure 6 in order to reduce pumping powers and achieve the required heat transfers. Channel widths from $1750 \mu m$ to $2030 \mu m$ and channel heights of 6.35 cm to 6.86 cm were necessary just to

© 2006 by Battelle Memorial Institute

lower pressure drops and pumping powers to the still absurdly high levels shown in Figure 8. It is completely unacceptable to incur exhaust gas pumping powers of 1200-1500 watts to achieve the $UA_h$ levels shown in Figure 8. Figure 8 data suggests that increasing channel height would gain some thermal performance, but this would require more weight, volume, and cost. These heat exchanger designs are already larger than TE area requirements shown in Figure 4. As the Figure 8 data indicates, trying to achieve $UA_h$ ~ 250 W/K would create even higher pumping power requirements and a more untenable situation.

The thermal entry lengths were estimated for the Figure 8 conditions using techniques of White [15] and Kays and Crawford [16]. The thermal entry lengths were estimated to be ~ 7 cm, which is a significant portion of the 11.1 cm length. The momentum entry lengths were estimated to be somewhat shorter than this. Even with these rather significant thermal entry lengths, the effect on the Nusselt number was only to increase it about 6% over fully developed conditions (See Eq. 10). The effect on friction factors was estimated to be smaller than this.

The hot side heat transfer, given by Eq. 12, is again a critical performance parameter. Figure 2 as before provides the TE hot and cold side temperatures desired from the

![](./images/811927998176428032_8.jpg)

**Figure 8 - Heat Exchanger $UA_h$ vs. Pumping Power in Various Exhaust Gas Flow Designs**

various potential operating points illustrated on the maximum efficiency vs. power map. Assuming one would operate along the $T_{cold}$ ($T_c$) =390 K curve in Figure 2, the hot side temperature of 680 K creates the maximum power conditions, resulting in $(T_{ex}-T_h)=353.2$ K. This allows one to convert the Figure 8 data into heat transfer rates, $Q_h$ and determine the heat transfer/pumping power factor, $\Gamma_h$.

Figure 9 displays the $\Gamma$ and $Q_h$ for the various gas heat exchanger designs in Figure 8 and quantifies the sensitivity of $\Gamma$ and $Q_h$ to increasing channel height and channel width. It is clear the $\Gamma$ factors are much lower, generally in the 15 - 20 range, because of the low gas conductance in the exhaust gas heat exchanger and the high pumping powers in Figure 8. This is at least 2 orders of magnitude below the $\Gamma$ factors in Figure 5. The horizontal $Q_h$ requirement line is shown on Figure 9 to indicate what design cases meet the hot side thermal requirement for $UA_h = 100$ W/K conditions. The $Q_h$ requirement for $UA_h = 250$ W/K conditions (i.e., $Q_h$ ~ 43,000 W) does not even appear on the Figure 9 scale, indicating how severe this requirement would be on the system design. It is evident from this work that, even dealing with 5% of the total glass process exhaust flow, the there is a major engineering, and possibly scientific, challenge in satisfying the exhaust gas heat transfer requirements on the hot side of an advanced TE system in glass process energy recovery.

![](./images/811927998176428032_9.jpg)

**Figure 9 - Heat Transfer/Pumping Power Factor and Total Hot-Side Heat Transfer in Various Exhaust Gas Flow Designs for 5% Exhaust Flow**

It should also be noted that these heat exchanger designs were assuming a high thermal conductivity base material (i.e., copper) for the exhaust gas heat exchanger. It is highly likely that a high-temperature Inconel or other low-thermal- conductivity material would be required to survive the hot exhaust gas environment in the glass process. Therefore, the $UA_h$ performance would be significantly below that shown in Figure 8 and the $\Gamma$ factors would also be significantly lower than those shown in Figure 9. This simply increases the exhaust gas heat transfer challenges that are readily apparent on the hot side of the advanced TE system.

## Future Research Directions in Energy Recovery

It is clear from data in Figures 8 and 9 and the surrounding discussion that hot-side exhaust heat transfer in the advanced TE systems for glass process energy recovery will be

© 2006 by Battelle Memorial Institute

extremely challenging. Achieving high enough $\Gamma$ factors and therefore low enough pumping powers for the required heat transfer will require significant attention. Future research and development (R&D) work in both fundamental research and system research is necessary to improve the exhaust gas heat transfer, pressure drop and pumping power characteristics in glass process exhaust gas energy recovery.

Figures 10 and 11 show potential cold-side microchannel performance improvements and potential hot-side exhaust gas heat exchange performance one could gain and will need from innovative system approaches involving multiple stacking of heat exchange systems. These innovative system approaches will be a subject of future publications in this area, but the potential performance results are provided here to show the possibilities. In Figure 10, for example, $\Gamma$ factors are at least 2 orders of magnitude larger than the results shown in Figure 7. In Figure 11, addressing hot side exhaust gas heat exchanger possibilities, $\Gamma$ factors are 2-3 times larger than the results shown in Figure 9. Figure 11 demonstrates the level of performance improvement that is required, and appears possible, on hot-side exhaust gas heat exchangers under laminar flow conditions. This performance level would enable effective glass process energy recovery.

Future advanced heat transfer R&D must proceed in order to realize advanced TE system performance potentials in glass process energy recovery. In addition, there are needs to develop more robust base heat exchanger materials, corrosion-resistant coatings, and thermal interface materials that have high thermal conductivity, can survive the high temperature and potentially corrosive environments, and can satisfy reliability, lifetime and cost requirements in glass-process exhaust energy recovery. This R&D must occur in parallel with the search for high-ZT, low-cost, highly-manufacturable advanced TE materials already underway at several research organizations. This R&D need applies regardless of what energy conversion technology is employed.

## Conclusions

Preliminary engineering analyses were performed on advanced TE systems for glass process exhaust energy and other industrial process applications. The results have quantified the system performance possibilities and provided a foundation for extrapolation of future system potentials. This work focused on a systems-level analysis approach in which the advanced TE device design and performance was considered simultaneously with the hot-side and cold-side heat exchangers design and performance.

TE design performance was quantified for advanced TE materials, characterized by temperature-integrated ZT values of ~2 and ~4, at exhaust mass flow rates about 5% of total glass process exhaust mass flows. The dependencies of potential power output, TE device area requirements and cold-side cooling requirements on TE materials and hot-side heat exchanger performance $\mathrm{UA_h}$ were evaluated and quantified. TE materials with ZT ~ 2 generated large power outputs resulting in significant energy recovery potentials in glass process exhaust flows. At exhaust flow temperatures of 1033 K, the power output potential was significant at ~6000 W for a hot-side $\mathrm{UA_h}$ target of ~250 W/K.

![](./images/811927998176428032_10.jpg)

Figure 10 - Potential Cold Side Water Microchannel Performance from Innovative System Approaches

Potential water-copper microchannel designs were investigated for system cold-side cooling, various design sensitivities were evaluated, and critical design-distinguishing metrics were quantified. Water microchannel designs exhibited the heat transfer, pressure drop, and pumping power characteristics required to enable advanced TE systems in glass process energy recovery. Performance metrics, such as $\mathrm{UA_c}$ and $\Gamma$ factors, were high enough to satisfy cold-side thermal requirements at low pumping power expense.

![](./images/811927998176428032_11.jpg)

Figure 11 - Potential Hot Side Exhaust Gas Heat Exchanger Performance from Innovative System Approaches

© 2006 by Battelle Memorial Institute

Innovative design approaches could increase $\Gamma$ factors on cold-side microchannel designs by another 2 orders of magnitude.

Potential exhaust gas heat exchanger designs were investigated to quantify the performance possible toward satisfying hot side heat exchanger requirements. Critical performance metrics, such as $\Gamma$ factors, were found to be too small by factors of 2-3. It was clear from analysis results that there will be large engineering, and possibly scientific, challenges to surmount in achieving the hot-side heat exchange requirements. Innovative design approaches appear promising in closing this performance gap. Future R&D efforts and resources should be directed toward these challenges to ensure that advanced TE systems can achieve their full potential in glass process and other industrial process energy recovery. This R&D must occur in parallel with the search for high-ZT, low-cost, highly-manufacturable advanced TE materials. Finally, the hot-side heat transfer R&D is critical regardless of what energy conversion technology is employed, be it thermoelectrics, piezoelectrics, thermionics, or thermophotovoltaics.

## Acknowledgments
The author would like to thank Sara Dillich and John Fairbanks at the U.S. Department of Energy, Industrial Technologies Program Office and FreedomCAR & Vehicle Technologies Office, respectively, Washington, DC for their support of this work.

## References
1. Energy Use, Loss, and Opportunity Analysis: U.S. Manufacturing and Mining, Energetics, Inc., E3M., Incorporated, December 2004.
2. Hendricks, T.J. and Lustbader, J.A., "Advanced Thermoelectric Power System Investigations for Light- Duty and Heavy-Duty Vehicle Applications: Part I," Proceedings of the $21^{st}$ International Conference on Thermoelectrics, Long Beach, CA, IEEE Catalogue #02TH8657, pp. 381-386, 2002.
3. Hendricks, T.J. and Lustbader, J.A., "Advanced Thermoelectric Power System Investigations for Light- Duty and Heavy-Duty Vehicle Applications: Part II," Proceedings of the $21^{st}$ International Conference on Thermoelectrics, Long Beach, CA, IEEE Catalogue #02TH8657, pp. 387-394, 2002.
4. Hendricks, T.J. and Lustbader, J.A., "Thermoelectric Energy Recovery Systems in Future Advanced Vehicles," Proceedings of the $6^{th}$ ASME-JSME Thermal Engineering Joint Conference, Japan Society of Mechanical Engineers, Paper #A4-334, 2003.
5. Angrist, S.W., "Direct Energy Conversion", $4^{th}$ Ed., Allyn and Bacon, Boston, MA, 1982.
6. Rowe D.M.,Ed., "CRC Handbook of Thermoelectrics" CRC Press Boca Raton, FL, 1995.
7. Crane, D.T. and Jackson, G.S., "Systems-Level Optimization of Low-Temperature Thermoelectric Waste Heat Recovery," Proceedings of the $37^{th}$ Intersociety Energy Conversion Engineering Conference, IECEC Paper #20076, 2002.
8. Cho, J., Anderson, M., Richards, R., Bahr, D., and Richards, C., "Optimization of Electromechanical Coupling for a Thin-Film PZT Membrane: II. Experiment", Journal of Micromechanics and Microelectronics, 15, 1804-1809, 2005.
9. Kays, W.M. and London, A.L., "Compact Heat Exchangers," $3^{rd}$ Edition, McGraw-Hill, New York, 1984.
10. Hendricks, T.J., "Comparison of Skutterudites and Advanced Thin-Film $B_4C/B_9C$ and Si/SiGe Materials in Advanced Thermoelectric Energy Recovery Systems," Proceedings of the $24^{th}$ International Conference on Thermoelectrics, Clemson, SC, IEEE Catalogue #05TH8854, pp. 369-375, 2005.
11. Ghamaty, S. and Elsner, N., "Quantum Well Thermoelectric Device," Proceedings of 2004 Department of Energy/Electric Power Research Institute High-Efficiency Thermoelectrics Workshop, Office of FreedomCAR & Vehicle Technologies, U.S. Department of Energy, San Diego, CA, 2004.
12. Caillat, T., Fleurial, J.-P., Snyder, G.J., and Borshchevsky, "Preparation and thermoelectric properties of semiconducting $Zn_4Sb_3$" Journal of Phys. Chem. Solids, 7, 1119, (1997).
13. Kanatzidis, M.G., "The Nanostructured Thermoelectric Materials $AgPb_mSbTe_{2+m}$ (LAST-m)", Proceedings of Materials Research Society 2005 Fall Meeting, Boston, MA, Dec. 2005.
14. Venkatasubramanian, R., Siivola, E., Colpitts, T., O'Quinn, B., "Thin-Film Thermoelectric Devices With High Room-Temperature Figures of Merit", Nature, 413, 597-602, October 2001.
15. White, F. M., "Fluid Mechanics", $2^{nd}$ Ed., McGraw-Hill, Inc., New York, 1986.
16. Kays, W.M. and Crawford, M.E., "Convective Heat and Mass Transfer", $2^{nd}$ Ed., McGraw-Hill, Inc., New York, 1980.
17. Gnielinski, V., Int. Chem. Eng., 16, 359, 1976.

© 2006 by Battelle Memorial Institute

10