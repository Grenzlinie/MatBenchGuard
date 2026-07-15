# Coupling properties and parametric optimization of a photovoltaic panel driven thermoelectric refrigerators system

Tianjun Liao $^{a,b}$, Qijiao He $^{a}$, Qidong Xu $^{a}$, Yawen Dai $^{a}$, Chun Cheng $^{a}$, Meng Ni $^{a,*}$

$^{a}$ Department of Building and Real Estate, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, China
$^{b}$ Department of Physics and Energy, Chongqing University of Technology, Chongqing, 400054, China

---

## ARTICLE INFO
Article history:
Received 30 August 2020
Received in revised form
5 January 2021
Accepted 6 January 2021
Available online 9 January 2021

Keywords:
PV panel
Thermoelectric refrigerator
Cooling heat flow
Coupling properties
Parametric optimization

---

## ABSTRACT
The achievement of temperature and heat management by combining the photovoltaic (PV) power generation and semiconductor thermoelectric refrigerators (TERs) is significant for developing high performance and durable energy conversion systems. In this work, a new energy system combining PV with TERs is proposed and theoretically evaluated. At a given solar irradiance of $200\ \text{W}\ \text{m}^{-2}$, the electrical matching properties between two subsystems are studied and the TERs' operating regions are provided. The optimal efficiency of 13.9% is obtained by reasonably selecting the TERs' number and the structure parameters. Further, the effects of the solar irradiance on the optimal efficiency and the operating conditions are analyzed. The parametric optimal regions are identified to achieve a trade-off between the efficiency and the cooling heat flow rate. The impacts of the diode's ideal factor, the TERs' temperature span, and the PV panel's series internal resistance and shunt resistance on the system are revealed. The proposed model and the analysis may provide valuable strategies for designing PV-driven TERs.

© 2021 Elsevier Ltd. All rights reserved.

---

## 1. Introduction
Due to the increasingly energy crisis and environmental problems, the development and utilization of renewable energy have attracted tremendous attentions. Photovoltaic (PV) power generation technology is one of the key ways of solar energy utilization [1]. With the improvement and commercialization of silicon-based PV panel, the problems of electrical energy's storage and application need to be solved. Some researchers proposed solutions for storage the electrical energy by means of super-capacitors [2] and lithium-ion battery cells [3]. On the other hand, most of the solar energy is converted into irreversible thermal losses [4]. The finite-time heat transfer increases the temperature and decrease the photo-electric conversion efficiency. Consequently, it is of great importance for recovering the waste heat to achieve energy cascade utilization [5]. Researchers proposed methods of waste heat recovery and thermal management by attaching the thermoelectric devices (TEDs) [6] and thermoelectric refrigerators (TERs) [7] to the back-side of the PV panel. Yin et al. [6] proposed a concentration spectrum splitting PV-TEG coupling system. The optimal cut-off wavelength at the highest efficiency was obtained. The effects of the TEG's thermal resistance and structure factor on the system were discussed. The results are significant for analyzing and optimizing the PV-TEG systems. Kane et al. [7] attached a TER at the back side of PV panel for the purpose of thermal management. Considering the temperature dependence of material properties, a temperature based maximum power point tracking scheme was provided for operating TEM at optimal temperature of PV system. Najafi et al. [8] utilized the PV panel's electricity to drive TER. Genetic algorithm was utilized to optimize the supplied electrical current for the TER, resulting the maximum power generation in the PV panel. It has been demonstrated that the TER can assist the PV panel at a low-level temperature by using a reasonable amount of electricity. Although the decrease of temperature is achieved, the overall efficiency hasn't been improved due to the electrical energy consumption. As an important application, the electrical coupling models of solar cell driven TER systems were established [9,10]. The effects of the electrical and the thermal parameters on cooling heat flow rate and efficiency were discussed. Cheng et al. [11] utilized the solar cells driven TER system to cool the green building. Experimental results demonstrated that a $16.2\ ^\circ\text{C}$ temperature difference between environment and indoor space can be produced. Although some literatures reported the PV driven TERs, the coupling properties and parametric optimization should be further

---
* Corresponding author.
E-mail address: meng.ni@polyu.edu.hk (M. Ni).

https://doi.org/10.1016/j.energy.2021.119798
0360-5442/© 2021 Elsevier Ltd. All rights reserved.

### Nomenclature

| Symbol       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| $A$          | ($\text{m}^2$)                                                              |
| $E_g$        | silicon-based PV panel band-gap (eV)                                        |
| $G$          | solar irradiance ($\text{W} \cdot \text{m}^{-2}$)                            |
| $I$ area     | electrical current (A)                                                      |
| $I_0$        | reverse saturation current (A)                                               |
| $k_{\text{B}}$ | Boltzmann constant ($\text{J} \cdot \text{K}^{-1}$)                          |
| $K$          | thermal conductance ($\text{W} \cdot \text{K}^{-1}$)                        |
| $l$          | length (m)                                                                  |
| $m$          | ideal factor                                                                |
| $N$          | number of thermoelectric refrigerators                                      |
| $n_{\text{T}}$ | number of p-n couples                                                       |
| $n_{\text{PV}}$ | number of solar cells in series                                             |
| $P$          | power output (W)                                                            |
| $q$          | elementary positive charge (C)                                              |
| $\dot{Q}$    | heat flow (W)                                                               |
| $R_{\text{s}}$ | series internal resistance ($\Omega$)                                       |
| $R_{\text{sh}}$ | shunt resistance ($\Omega$)                                                 |
| $R_{\text{TERs}}$ | internal resistance of TERs ($\Omega$)                                      |
| $T$          | temperature (K)                                                             |
| $U$          | heat transfer coefficient ($\text{W} \cdot \text{m}^{-2} \cdot \text{K}^{-1}$) |
| $V$          | voltage (V)                                                                 |
| $Z$          | objective function (W)                                                      |

### Greek symbols

| Symbol | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| $\alpha$ | Seebeck coefficient ($\text{V} \cdot \text{K}^{-1}$)                        |
| $\rho$ | electrical resistivity ($\Omega \cdot \text{m}$)                            |
| $\kappa$ | thermal conductivity ($\text{W} \cdot \text{K}^{-1} \cdot \text{m}^{-1}$)    |

| Symbol | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| $\sigma$ | Stefan-Boltzmann constant ($\text{W} \cdot \text{K}^{-4} \cdot \text{m}^{-2}$) |
| $\beta$ | structure parameter of TER (m)                                              |
| $\mu$ | short-circuit current coefficient ($\text{A} \cdot \text{K}^{-1}$)          |
| $\eta$ | efficiency                                                                  |

### Subscript

| Symbol | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| avg    | average                                                                     |
| CP     | coupling point                                                              |
| E      | environment                                                                 |
| H      | hot side                                                                    |
| lb     | lower-bound                                                                 |
| L      | cold side                                                                   |
| n      | n-type semiconductor                                                        |
| max    | maximum                                                                     |
| opt    | optimal                                                                     |
| OC     | open-circuit                                                                |
| p      | p-type semiconductor                                                        |
| PV     | photovoltaic                                                                |
| ph     | photo-generation                                                           |
| Ref    | reference                                                                   |
| SC     | short-circuit                                                               |
| SU     | start-up                                                                    |
| ub     | upper-bound                                                                 |

### Abbreviations

| Symbol | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| COP    | coefficient of performance                                                  |
| PV     | photovoltaic                                                                |
| TED    | thermoelectric device                                                       |
| TERs   | thermoelectric refrigerators                                                |

studied.

In order to promote the application of PV panel in the field of refrigeration, we propose a model of PV panel driven TERs system in this work. The parameter coupling and matching characteristics between two subsystems are studied. The effects of solar irradiance, PV panel's diode ideal factor, and TERs' temperature span on the optimal performances and the operating conditions are discussed. The proposed model and the analysis can provide a theoretical basis for the design of solar refrigeration systems.

### 2. Model description of a PV panel driven TERs system

The schematic diagrams of a PV panel driven TERs system and an equivalent circuit of a silicon-based PV panel are illustrated in Fig. 1, where $V_{\text{PV}}$ and $I_{\text{PV}}$ denote the PV panel's output voltage and electrical current, $I_{\text{ph}}$ and $I_0$ denote the PV panel's photo-generation and reverse saturation currents, $R_{\text{s}}$ and $R_{\text{sh}}$ are, respectively, the series internal resistance and shunt resistance, $T_{\text{L}}$ and $T_{\text{H}}$ stand for the temperatures of the cold and hot reservoirs, $U_{\text{L}}$ and $U_{\text{H}}$ account for the heat transfer coefficients at the cold and hot sides [6], $A_{\text{L}}$ and $A_{\text{H}}$ mean the heat-transfer areas of the cold and hot junctions [12]. The PV panel converts sunlight into electrical energy based on the PV effect of the semiconductor p-n junction. Solar cells are connected in series and packaged to form a PV panel. In TERs, a thermocouple is composed of two types of doped semiconductor materials. As the system is in operation, the power generated in the PV panel is directly applied to driven the TERs. Meanwhile, the PV panel's electrical current enters into the TERs, which absorb heat $\dot{Q}_{\text{L}}$ from the cold reservoir and simultaneously release heat $\dot{Q}_{\text{H}}$ into the hot reservoir per unit time, resulting in temperature difference $(T_2 - T_1)$. Therefore, an inequality $(T_2 > T_{\text{H}} > T_{\text{L}} > T_1)$ should satisfy at the cooling process [12].

### 3. The overall efficiency of the coupling system

The overall efficiency $\eta$ of the PV panel driven TERs system is defined as [9].

$$
\eta=\frac{P_{\mathrm{PV}}}{G A_{\mathrm{PV}}} \frac{\dot{Q}_{\mathrm{L}}}{P_{\mathrm{TERs}}}, \tag{1}
$$

where $P_{\text{PV}} = V_{\text{PV}}I_{\text{PV}}$ and $P_{\text{TERs}} = \dot{Q}_{\text{H}} - \dot{Q}_{\text{L}} = V_{\text{TERs}}I_{\text{TERs}}$ are, respectively, the output electricity of the PV panel and the input power of the TERs. $V_{\text{TERs}}$ and $I_{\text{TERs}}$ account for the TERs' input voltage and electrical current. $G$ means the solar irradiance. $A_{\text{PV}} = 1.6434 \ \text{m}^2$ describes the PV panel's front surface area [14]. As the circuit of the PV panel is directly connected to that of the TER, the electrical coupling conditions: $V_{\text{PV}} = V_{\text{TERs}}, I_{\text{PV}} = I_{\text{TERs}}$, and $P_{\text{PV}} = P_{\text{TERs}}$ can be satisfied [9]. The previous works demonstrated that a part of the solar energy absorbed by the PV panel is converted into electricity to drive the external load, and the remaining energy is parasitic inside the PV panel in the form of thermalization, Joule heat, and non-radiative recombination heat, which leads to the increase of temperature and the heat transfer from the PV panel to the environment [15,16]. As two objects are operated an infinitely small temperature difference, the heat transfer is reversible. However, the PV panel's operating temperature $T_{\text{PV}}$ is higher than the normal environment temperature $T_{\text{E}} = 300 \ \text{K}$, the irreversible heat transfers is occurred. According to Newton's cooling law, black-body radiative law, and energy balance analysis, an equation can be given by Refs. [7,13].

![](./images/812514315398545408_1.jpg)

Fig. 1. (a) The schematic diagram of a PV-TERs system and (b) the equivalent circuit of a PV panel.

$$GA_{PV}-P_{PV}=U_{PV}A(T_{PV}-T_{E})+\sigma A\left(T_{PV}^{4}-T_{E}^{4}\right),\qquad(2)$$

where $U_{PV}=5\ \text{W·m}^{-2}·\text{K}^{-1}$ denotes the convective heat transfer coefficient [17]. $\sigma=5.67\times10^{-8}\text{W·K}^{-4}·\text{m}^{-2}$ is the Stefan-Boltzmann constant. $A=2A_{PV}$ means the total area by considering the waste heat emissions of the top and the bottom surface of the PV panel.

As we assume that series internal resistance $R_{s}\to0$ and shunt resistance $R_{sh}\to\infty$ are generally considered in the equivalent diode circuit model, the relationship between the electrical current $I_{PV}$ and the voltage $V_{PV}$ of the PV panel is expressed as [18].

$$I_{PV}=I_{ph}-I_{0}\left[\exp\left(\frac{qV_{PV}}{mk_{B}T_{PV}n_{PV}}\right)-1\right],\qquad(3)$$

where $m$ is the diode's ideal factor. $n_{PV}$ denotes the numbers of solar cells in series. $q=1.60\times10^{-19}\text{C}$ is the elementary charge. $k_{B}=1.38\times10^{-23}\text{J·K}^{-1}$ stands for the Boltzmann constant. The dependence of the photo-generation current $I_{ph}$ on the optical, thermal, and electrical parameters is defined as [7].

$$I_{ph}=\frac{G}{G_{\text{Ref}}}\left[I_{\text{ph,Ref}}+\mu\left(T_{PV}-T_{\text{Ref}}\right)\right],\qquad(4)$$

where $G_{\text{Ref}}=1000\text{W·m}^{-2}$ is the reference solar irradiance. $T_{\text{Ref}}=298\ \text{K}$ is the reference temperature. $I_{\text{ph,Ref}}=9.43\ \text{A}$ is the photo-generated current under reference solar irradiance [14]. $\mu=0.00047\ \text{A·K}^{-1}$ is the short-circuit current temperature coefficient [14].

The diode reverse saturation current $I_{0}$ varying with the band-gap $E_{\text{g}}$ and work temperature $T_{PV}$ is given by Ref. [18].

$$\frac{I_{0}}{I_{0,\text{Ref}}}=\left(\frac{T_{PV}}{T_{\text{Ref}}}\right)^{3}\exp\left[\frac{qE_{\text{g}}}{k_{\text{B}}}\left(\frac{1}{T_{\text{Ref}}}-\frac{1}{T_{PV}}\right)\right],\qquad(5)$$

where $I_{0,\text{Ref}}=1.25\ \text{nA}$ is the reverse saturation current at reference temperature $T_{\text{Ref}}$. The PV panel's band-gap $E_{\text{g}}$ as a function of the temperature $T_{PV}$ is defined as [19,20].

$$E_{\text{g}}=1.17-\frac{4.73\times10^{-4}T_{PV}^{2}}{T_{PV}+636}.\qquad(6)$$

For the convenience of discussion, we set a structure parameter $A_{\text{p}}/l_{\text{p}}=A_{\text{n}}/l_{\text{n}}=\beta$. The p- and n-doped $\text{Bi}_{2}\text{Te}_{3}$ based semiconductor elements are thermally in parallel and electrically connected in series to make a TER. Considering the Newton cooling law, the Joule law, and the Peltier effect within the TERs, the two heat flows $\dot{Q}_{\text{H}}$ and $\dot{Q}_{\text{L}}$ are given by Refs. [21-23].

$$\dot{Q}_{\text{H}}=\alpha T_{2}I_{\text{TERs}}-K\left(T_{2}-T_{1}\right)+\frac{1}{2}I_{\text{TERs}}^{2}R_{\text{TERs}}\qquad(7)$$

and

$$\dot{Q}_{\text{L}}=\alpha T_{1}I_{\text{TERs}}-K\left(T_{2}-T_{1}\right)-\frac{1}{2}I_{\text{TERs}}^{2}R_{\text{TERs}},\qquad(8)$$

where $\alpha T_{2}I_{\text{TERs}}$ and $\alpha T_{1}I_{\text{TERs}}$ are the Peltier heat generated at the hot end and cold sides per unit time. $K(T_{2}-T_{1})$ denotes the Newton heat flow between the hot and cold sides. $\alpha=Nn_{\text{T}}(\alpha_{\text{p}}-\alpha_{\text{n}})$, $K=Nn_{\text{T}}\beta(\kappa_{\text{p}}+\kappa_{\text{n}})$, and $R_{\text{TERs}}=Nn_{\text{T}}\beta^{-1}(\rho_{\text{p}}+\rho_{\text{n}})$ are, respectively, the Seebeck coefficient, thermal conductance, and electrical resistance of TERs. $N$ is the number of TERs in series. $n_{\text{T}}$ means the number of p-n TE couples in a TER. $A$ and $l$ stand for the cross-sectional area and the length of the semiconductor element. $\rho$ and $\kappa$ represent the electrical resistivity and the thermal conductivity of a TER. The subscripts n and p designate n- and p-type elements.

Commercial CP2-127-06 Melcor TER is applied in this work. A p-n TE couple's total Seebeck coefficient $(\alpha_{\text{p}}-\alpha_{\text{n}})$, resistivity $(\rho_{\text{p}}+\rho_{\text{n}})$, and thermal conductivity $(\kappa_{\text{p}}+\kappa_{\text{n}})$ are calculated by using the formulas as [24,25].

$$\alpha_{\text{p}}-\alpha_{\text{n}}=\left(22224.0+930.6\overline{T}-0.8805\overline{T}^{2}\right)\times10^{-9},\qquad(9)$$

$$\rho_{\text{p}}+\rho_{\text{n}}=\left(5112+163.4\overline{T}+0.6279\overline{T}^{2}\right)\times10^{-10},\qquad(10)$$

and

$$\kappa_{\text{p}}+\kappa_{\text{n}}=\left(62605.0-277.7\overline{T}+0.4131\overline{T}^{2}\right)\times10^{-4},\qquad(11)$$

where $\overline{T}=(T_{1}+T_{2})/2$ is the cold and hot sides' mean temperature.

According to Newton's cooling law, the heat flows $\dot{Q}_{\text{H}}$ and $\dot{Q}_{\text{L}}$ can be expressed as [24].

$$
\dot{Q}_{H}=U_{H} A_{H}\left(T_{2}-T_{H}\right)
$$

and

$$
\dot{Q}_{\mathrm{L}}=\mathrm{U}_{\mathrm{L}} \mathrm{A}_{\mathrm{L}}\left(\mathrm{T}_{\mathrm{L}}-\mathrm{T}_{1}\right),
$$

where $A_{\mathrm{H}} / N=A_{\mathrm{L}} / N=3.6 \times 10^{-3} \mathrm{~m}^{2}$.

According to Eqs. (7) and (8), the input power $P_{\text {TERs }}$ of the TERs can be obtained as

$$
P_{\mathrm{TERs}}=\dot{Q}_{\mathrm{H}}-\dot{Q}_{\mathrm{L}}=\alpha\left(T_{2}-T_{1}\right) I_{\mathrm{TERs}}+I_{\mathrm{TERs}}^{2} R_{\mathrm{TERs}},
$$

where $\alpha\left(T_{2}-T_{1}\right) I_{\text {TERs }}$ represents the electrical work that overcomes the thermoelectric potential. $I_{\text {TERs }}^{2} R_{\text {TERs }}$ denotes the TERs' power consumption due to the TERs' internal resistance $R_{\text {TERs }}$.

Thus, the input voltage $V_{\text {TERs }}$ of the TERs is derived as.

$$
V_{\mathrm{TERs}}=P_{\mathrm{TERs}} / I_{\mathrm{TERs}}=\alpha\left(\mathrm{T}_{1}-\mathrm{T}_{2}\right)+\mathrm{I}_{\mathrm{TERs}} \mathrm{R}_{\mathrm{TERs}},
$$

## 4. Coupling properties and parametric optimization

By using Eqs. (2)-(6), the dependence of the operating tem- perature $T_{\mathrm{PV}}$ on the voltage $V_{\mathrm{PV}}$ can be numerically determined for given related parameters. Inserting $T_{\mathrm{PV}}$ into Eq. (3), the curve of the electrical current $I_{\mathrm{PV}}$ as a function of the voltage $V_{\mathrm{PV}}$ can be generated, as shown in Fig. 2(a). Combining Eqs. (7)-(13), the variations of the temperatures $T_{1}$ and $T_{2}$ with the electrical current $I_{\text {TERs }}$ can be obtained, as displayed in Fig. 2(b). Inserting $T_{1}$ and $T_{2}$ into Eqs. (9)-(11) and (15), the relationship between $I_{\text {TERs }}$ and $V_{\text {TERs }}$ can be derived, as depicted in Fig. 2(a). It is observed from Fig. 2(a) that $I_{\text {TERs }}$ monotonically increases of $V_{\text {TERs }}$. We can determine a coupling point $\left(V_{\mathrm{CP}}, I_{\mathrm{CP}}\right)$ in the two voltage-current characteristics curves of the TERs and the PV panel as $V_{\mathrm{PV}}=V_{\mathrm{TERs}}=V_{\mathrm{CP}}=29.3 \mathrm{~V}$ and $I_{\mathrm{PV}}=I_{\mathrm{TERs}}=I_{\mathrm{CP}}=1.55 \mathrm{~A}$. Only when the system is operated at the coupling point, the cooling process can be achieved. Fig. 2(b) shows that two temperatures $T_{1}=T_{1, \mathrm{CP}}=287 \mathrm{~K}$ and $T_{2}=T_{2, \mathrm{CP}}=$ $315 \mathrm{~K}$ are obtained as $V_{\text {TERs }}=V_{\mathrm{CP}}$. The case $\dot{Q}_{\mathrm{L}}=0$ can be achieved by adjusting the input voltage $V_{\text {TERs }}$. The result $T_{1}=T_{\mathrm{L}}$ is occurred based on Eq. (13). The voltage under the condition $\dot{Q}_{\mathrm{L}}=0$ is denoted as start-up voltage $V_{\mathrm{SU}}$. Fig. 2(b) shows that $T_{2}$ is close to $T_{\mathrm{H}}$ under the condition of $V_{\text {TERs }}=V_{\text {SU }}$. When the voltage $V_{\text {TERs }}$ locates in the region of $V_{\text {TERs }}<V_{\text {SU }}$, the temperatures $T_{1}$ and $T_{2}$ locate in the regions of $T_{1}>T_{\mathrm{L}}$ and $T_{2}<T_{\mathrm{H}}$. In the above regions, the purpose of the refrigeration process isn't achieved, while the TERs can work as a heat pump. On the other hand, the PV panel's maximum output voltage is equal to the open-circuit voltage $V_{\text {OC }}$. Thus, the voltage $V_{\text {TERs }}$ shouldn't operate in the region of $V_{\text {TERs }} \geq V_{\text {OC }}$. Thus, the voltage $V_{\text {TERs }}$ should locate in the region

$$
V_{\mathrm{SU}}<V_{\mathrm{TERs}}<V_{\mathrm{OC}} \text {. }
$$

As set $V_{\text {TERs }}=V_{\text {OC }}$, a lower-bound temperature $T_{1, \mathrm{lb}}$ and a upper-bound temperature $T_{2, \mathrm{ub}}$ can be determined. Based on the in-equation (16), the operating regions of the temperatures $T_{1}$ and $T_{2}$ should be situated in:

$$
T_{\mathrm{L}}>T_{1}>T_{1, \mathrm{lb}}
$$

and

$$
T_{2, \mathrm{ub}}>T_{2}>T_{\mathrm{H}} \text {. }
$$

Inserting $T_{1, \mathrm{CP}}$ into Eq. (13), the cooling heat flow rate $\dot{Q}_{\mathrm{L}}$ can be computed. Further, substituting $\dot{Q}_{\mathrm{L}}$ in Eq. (1), the energy conversion efficiency $\eta=13.9 \%$. As we set $U_{\mathrm{H}} \rightarrow \infty$ and $U_{\mathrm{L}} \rightarrow \infty$, infinitely small temperature differences are occurred, i.e., $T_{1}-T_{\mathrm{L}} \rightarrow 0$ and $T_{2}-$ $T_{\mathrm{H}} \rightarrow 0$. Under the reversible heat transfer conditions, the system's efficiency $\eta=20.9 \%$ and the coupling parameters $V_{\mathrm{CP}}=28.7 \mathrm{~V}$ and $I_{\mathrm{CP}}=1.66 \mathrm{~A}$ can be obtained. Making comparisons between the non-ideal and the ideal cases, one can find that the impacts of the irreversible heat transfer losses on the efficiency are obviously. We should enhance the system' efficiency by reducing heat transfer losses at the boundaries, e.g., selecting material with high heat transfer coefficient. For a given solar irradiance $G$, we can adjust the parameters $\beta$ and $N$ to make system present high performances. In next section, the effects of $\beta$ and $N$ on the system's coupling properties will be discussed.

![](./images/812514315398545408_2.jpg)

Fig. 2. (a) The current-voltage characteristics curves of the PV and the TERs and (b) the cold-side's temperature $T_{1}$ and hot-side's temperature $T_{2}$ of the TERs varying with the voltage $V$ , where the parameters $G=200 ~W \cdot m^{-2}, T_{L}=290 ~K, T_{H}=310 ~K, m=1$ , $U_{H}=U_{L}=1000 ~W \cdot m^{-2} \cdot K^{-1}, n_{T}=127, n_{PV}=60, N=5$ , and $\beta=1.00 ×10^{-3} ~m$ are selected.

The variations of the coupling voltage $V_{CP}$ , the coupling current $I_{CP}$ , the cold-side's coupling temperature $T_{1, CP}$ , the hot-side's coupling temperature $T_{2, CP}$ , and the efficiency $\eta$ with $N$ and $\beta$ are

depicted in Fig. 3. Fig. 3(a) shows that the coupling voltage $V_{\mathrm{CP}}$ monotonically increases with $N$ as $\beta$ is fixed, because increasing the number of TERs leads that we should increase the voltage $V_{\mathrm{CP}}$ to achieve the cooling process, and thus, $V_{\mathrm{CP}}$ increases. Fig. 3(b) shows that the voltage $V_{\mathrm{CP}}$ monotonically decreases with $\beta$ for given $N$, because the decrease of internal resistance $R_{\mathrm{TERs}}$ with structure parameter $\beta$ causes that only decreasing the voltage $V_{\mathrm{CP}}$ can achieve the cooling process, and thus, $V_{\mathrm{CP}}$ decreases. The two sub-systems' current-voltage properties and the variations of $V_{\mathrm{CP}}$ with $N$ and $\beta$ determine the dependences of the $V_{\mathrm{CP}}$ on $N$ and $\beta$, as demonstrated in Fig. 3(b). Fig. 3(c) shows that the temperature $T_{1, \mathrm{CP}}$ first decreases and then increases as $\beta$ is increased, and thus, there exists a minimum value of $T_{1, \mathrm{CP}}$. Fig. 3(d) displays that the temperature $T_{2, \mathrm{CP}}$ is a monotonically decreasing function of $N$, while it first increases and then decreases as $\beta$ is increased. Fig. 3(e) reveals that an optimal efficiency $\eta_{\mathrm{opt}}=14.4 \%$ and the corresponding conditions $\beta_{\mathrm{opt}}=1.21$ and $N_{\mathrm{opt}}=5$ can be determined. Based on the values $\beta_{\mathrm{opt}}$ and $N_{\mathrm{opt}}$, the optimal values $V_{\mathrm{opt}}=28.1 \mathrm{~V}$ and $I_{\mathrm{opt}}=1.75 \mathrm{~A}$ of $V_{\mathrm{CP}}$ and $I_{\mathrm{CP}}$ can be calculated. Therefore, the results reveal that selecting optimal values $V_{\mathrm{opt}}, I_{\mathrm{opt}}, \beta_{\mathrm{opt}}$, and $N_{\mathrm{opt}}$ can make the coupled system present high performance. Based on the optimal efficiency $\eta_{\text {opt }}$ and Eq. (1), the optimal cooling heat flow $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$ is determined as

![](./images/812514315398545408_3.jpg)

Fig. 3. The 3-D graphs of (a) the coupling voltage $V_{\mathrm{CP}}$, (b) the coupling current $I_{\mathrm{CP}}$, (c) the cold-side's coupling temperature $T_{1, \mathrm{CP}}$, (d) the hot-side's coupling temperature $T_{2, \mathrm{CP}}$, and (e) the energy conversion efficiency $\eta$ varying with $N$ and $\beta$, where the related parameters are same as Fig. 2.

$$\dot{Q}_{\mathrm{L}, \mathrm{opt}}=\eta_{\mathrm{opt}}\left(G A_{\mathrm{PV}}\right).\tag{19}$$

The variations of $\eta_{\mathrm{opt}}$, $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$, $N_{\mathrm{opt}}$, $V_{\mathrm{opt}}$, and $I_{\mathrm{opt}}$ with the solar irradiance $G$ are shown in Fig. 4. Fig. 4(a) presents that the optimized efficiency $\eta_{\mathrm{opt}}$ attains a maximum value $\eta_{\max }=20.0 \%$ at $G_{\eta}$, while there exists the positive correlation between $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$ and $G$. It is seen from Fig. 4(a) that $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$ is negligibly in the region of $G<G_{\eta}$. In order to discuss the parametric optimal selection of $G$, an objective function $Z=\eta_{\mathrm{opt}} \dot{Q}_{\mathrm{L}, \mathrm{opt}}$ is introduced. The curve of $Z$ varying with $G$ is depicted in Fig. 4(b). Fig. 4(b) shows that $Z$ attains a maximum value $Z_{\max }$ at $G_{Z}$. In the region of $G>G_{Z}$, the efficiency $\eta_{\mathrm{opt}}$ decrease as the incident solar irradiance $G$ increases. Only the solar irradiance $G$ locates in the region of

$$G_{\eta} \leq G \leq G_{Z},\tag{20}$$

we can make trade-off between $\eta_{\mathrm{opt}}$ and $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$ to present high performances.

Fig. 4(c) shows that the structure parameter $\beta_{\mathrm{opt}}$ monotonically increases with increase in solar irradiance $G$. Based on in-equation (20), the optimal region of $\beta$ is determined as

$$\beta_{\mathrm{lb}} \leq \beta \leq \beta_{\mathrm{ub}},\tag{21}$$

where $\beta_{\mathrm{lb}}$ is a lower-bound value at $G_{\eta}, \beta_{\mathrm{ub}}$ is an upper-bound value at $G_{Z}$.

Fig. 4(c) shows that the two subsystems can be matched when the TERS' number $N_{\text {opt }}$ keeps at a constant in certain region. The intrinsic regime is revealed as follows. As we further increase $N$, the result occurred $V_{\mathrm{SU}}>V_{\mathrm{OC}}$ leads that the PV panel can not drive the TERS. As we further decrease $N$, the coupling point is not close to the maximum power point of the PV panel. As a result, the phenomenon is caused by optimization and matching. Based on in-equation (20), the upper value $N_{\mathrm{ub}}=6$ and the lower-bound value $N_{\mathrm{lb}}=5$ are obtained. The results indicate that two values of the TERS' number $N_{\text {opt }}$ can be chosen to optimally design the system. Furthermore, the problem of matching number of solar cells and TERS are solved. Fig. 4(d) shows that $V_{\text {opt }}$ and $I_{\text {opt }}$ monotonically increases with increase in solar irradiance $G$. Due to the increase of $V_{\text {opt }}$ and $I_{\text {opt }}$, the optimal structure parameter $\beta_{\text {opt }}$ should be increased to meet Eq. (15). Due to the optimal region of $G$, the optimal operating regions of $V_{\mathrm{CP}}$ and $I_{\mathrm{CP}}$ can be determined as

$$V_{\mathrm{lb}} \leq V_{\mathrm{TERS}} \leq V_{\mathrm{ub}}\tag{22}$$

and

$$I_{\mathrm{lb}} \leq I_{\mathrm{TERS}} \leq I_{\mathrm{ub}}.\tag{23}$$

It is observed from Fig. 4(d) that the optimal current $I_{\text {opt }}$ is too much small in the region of $G \leq G_{\eta}$, which leads that the TERS absorb small heat flow $\dot{Q}_{\mathrm{L}}$ from the cold reservoir, and thus, $\dot{Q}_{\mathrm{L}, \mathrm{opt}}$ is negligibly, as verified in Fig. 4(a).

The effects of the diode ideal factor $m$ and the hot reservoir's temperature $T_{\mathrm{H}}$ on the system's performances are revealed in Tables 1 and 2. The results in Tables 1 and 2 shows that the increase of $m$ and the decrease of $T_{\mathrm{H}}$ lead to the enhancement of system performance. The ideal factor $m$ influences the PV panel's electrical properties, e.g., the open-circuit voltage $V_{\mathrm{OC}}$

$$V_{\mathrm{OC}}=\frac{m k_{\mathrm{B}} T_{\mathrm{PV}} n_{\mathrm{PV}}}{q} \ln \left[\frac{I_{\mathrm{ph}}}{I_{0}}+1\right].\tag{24}$$

![](./images/812514315398545408_4.jpg)

Fig. 4. (a) The optimal efficiency $\eta_{opt }$ and cooling heat flow rate $\dot{Q}_{L, opt }$ , (b) the objective function $Z=\eta_{opt } ×\dot{Q}_{L, opt }$ , (c) the optimal structure parameter $\beta_{opt }$ and TERS number $N_{opt }$ , and (d) the optimal voltage $V_{opt }$ and electrical current $I_{opt }$ as a function of the solar irradiance $G$ , where the related parameters are same as Fig. 2.

<table><caption>Table 1 The effects of the diode ideal factor $m$ on the system's performances.</caption>
<thead>
<tr>
<th>$m$</th>
<th>$\eta_{\text{max}}$</th>
<th>$Z_{\text{max}}$
(W)</th>
<th>$G_{Z}$
(W$\cdot$m$^{-2}$)</th>
<th>$G_{\eta}$
(W$\cdot$m$^{-2}$)</th>
<th>$V_{\text{lb}}$
(V)</th>
<th>$V_{\text{ub}}$
(V)</th>
<th>$I_{\text{lb}}$
(A)</th>
<th>$I_{\text{ub}}$
(A)</th>
<th>$\beta_{\text{lb}}$
(mm)</th>
<th>$\beta_{\text{ub}}$
(mm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.0</td>
<td>20.0%</td>
<td>7.03</td>
<td>259</td>
<td>18.1</td>
<td>24.5</td>
<td>28.5</td>
<td>0.165</td>
<td>2.22</td>
<td>0.123</td>
<td>1.53</td>
</tr>
<tr>
<td>1.5</td>
<td>30.2%</td>
<td>15.9</td>
<td>275</td>
<td>19.8</td>
<td>37.3</td>
<td>42.7</td>
<td>0.178</td>
<td>2.39</td>
<td>0.142</td>
<td>1.53</td>
</tr>
<tr>
<td>2.0</td>
<td>40.3%</td>
<td>28.6</td>
<td>265</td>
<td>19.9</td>
<td>49.9</td>
<td>57.5</td>
<td>0.179</td>
<td>2.27</td>
<td>0.147</td>
<td>1.56</td>
</tr>
</tbody>
</table>

<table><caption>Table 2 The effects of the temperature $T_{\text{H}}$ on the system's performances, where $m=1$ is chosen.</caption>
<thead>
<tr>
<th>$T_{\text{H}}$
(K)</th>
<th>$\eta_{\text{max}}$</th>
<th>$Z_{\text{max}}$
(W)</th>
<th>$G_{Z}$
(W$\cdot$m$^{-2}$)</th>
<th>$G_{\eta}$
(W$\cdot$m$^{-2}$)</th>
<th>$V_{\text{lb}}$
(V)</th>
<th>$V_{\text{ub}}$
(V)</th>
<th>$I_{\text{lb}}$
(A)</th>
<th>$I_{\text{ub}}$
(A)</th>
<th>$\beta_{\text{lb}}$
(mm)</th>
<th>$\beta_{\text{ub}}$
(mm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>310</td>
<td>20.0%</td>
<td>7.03</td>
<td>259</td>
<td>18.1</td>
<td>24.5</td>
<td>28.5</td>
<td>0.165</td>
<td>2.22</td>
<td>0.123</td>
<td>1.53</td>
</tr>
<tr>
<td>305</td>
<td>28.1%</td>
<td>11.9</td>
<td>249</td>
<td>16.4</td>
<td>24.6</td>
<td>28.4</td>
<td>0.148</td>
<td>2.15</td>
<td>0.154</td>
<td>1.76</td>
</tr>
<tr>
<td>300</td>
<td>43.6%</td>
<td>22.6</td>
<td>201</td>
<td>12.3</td>
<td>24.1</td>
<td>28.4</td>
<td>0.111</td>
<td>2.10</td>
<td>0.165</td>
<td>1.72</td>
</tr>
</tbody>
</table>

<table><caption>Table 3 Systems' performance comparisons under the conditions of PV panel's ideal and actual equivalent circuits.</caption>
<thead>
<tr>
<td>$R_{\text{s}}$
($\Omega$)</td>
<td>$R_{\text{sh}}$
($\Omega$)</td>
<td>$\eta_{\text{max}}$</td>
<td>$Z_{\text{max}}$
(W)</td>
<td>$G_{Z}$
(W$\cdot$m$^{-2}$)</td>
<td>$G_{\eta}$
(W$\cdot$m$^{-2}$)</td>
<td>$V_{\text{lb}}$
(V)</td>
<td>$V_{\text{ub}}$
(V)</td>
<td>$I_{\text{lb}}$
(A)</td>
<td>$I_{\text{ub}}$
(A)</td>
<td>$\beta_{\text{lb}}$
(mm)</td>
<td>$\beta_{\text{ub}}$
(mm)</td>
</tr>
</thead>
<tbody>
<tr>
<td>0.01</td>
<td>$10^{4}$</td>
<td>19.9%</td>
<td>6.39</td>
<td>230</td>
<td>17.3</td>
<td>24.3</td>
<td>27.4</td>
<td>0.157</td>
<td>1.95</td>
<td>0.118</td>
<td>1.40</td>
</tr>
<tr>
<td>0</td>
<td>$\infty$</td>
<td>20.0%</td>
<td>7.03</td>
<td>259</td>
<td>18.1</td>
<td>24.5</td>
<td>28.5</td>
<td>0.165</td>
<td>2.22</td>
<td>0.123</td>
<td>1.53</td>
</tr>
</tbody>
</table>

The positive relation between $V_{\text{OC}}$ and $m$ changes the voltage-current characteristics resulting the variation of coupling point ($V_{\text{CP}}, I_{\text{CP}}$) with $m$, and thus, the performances of the system are adjusted accordingly.

The decrease of $T_{\text{H}}$ is accompanied by decrease of temperature span ($T_{\text{H}}-T_{\text{L}}$). Because the TERs' coefficient of performance $\dot{Q}_{\text{L}}/P_{\text{TERs}}$ is bounded by the Carnot limit, i.e.,
$$
\frac{\dot{Q}_{\text{L}}}{P_{\text{TERs}}} \leq \frac{T_{\text{L}}}{T_{\text{H}}-T_{\text{L}}}. \tag{25}
$$

Therefore, the improvement of the TERs' $\dot{Q}_{\text{L}}/P_{\text{TERs}}$ enhances the system's overall efficiency. Generally, the series internal resistance $R_{\text{s}}$ and shunt resistance $R_{\text{sh}}$ meet $R_{\text{s}} \neq 0$ and $R_{\text{sh}} \neq \infty$. Thus, Eq. (1) should be rewritten as [25]:
$$
I_{\mathrm{PV}}=I_{\mathrm{ph}}-I_{0}\left\{\exp \left[\frac{q\left(I_{\mathrm{PV}} R_{\mathrm{s}}+V_{\mathrm{PV}}\right)}{k_{\mathrm{B}} T_{\mathrm{PV}}}\right]-1\right\}-\frac{V_{\mathrm{PV}}+I_{\mathrm{PV}} R_{\mathrm{s}}}{R_{\mathrm{sh}}}. \tag{26}
$$

For given $R_{\text{s}}$ and $R_{\text{sh}}$, Table 3 list the parametric values at the maximum efficiency $\eta_{\text{max}}$ and the maximum objective function $Z_{\text{max}}$, which are helpful for the parametric choices of actual systems.

## 5. Conclusions
We have conceptually established and theoretically studied a model of the PV panel driven TERs system. Through the analysis of the coupling characteristics of the subsystem, the following research results are obtained.

(1) Using the parameters selections in Fig. 2, the efficiency $\eta=13.9\%$ and the operating conditions $T_{1,\text{CP}}=287$ K, $T_{2,\text{CP}}=315$ K, $V_{\text{CP}}=29.3$ V, and $I_{\text{CP}}=1.55$ A of the non-ideal irreversible TERs system are obtained. Ignoring the TERs' boundary heat transfers, we can obtain the ideal system's efficiency $\eta=20.9\%$ at $V_{\text{CP}}=28.7$ V and $I_{\text{CP}}=1.66$ A.

(2) According to optimize the number $N$ and the structure parameter $\beta$ of the TERs, the optimal efficiency $\eta_{\text{opt}}=14.4\%$ and the corresponding conditions $\beta_{\text{opt}}=1.21$, $N_{\text{opt}}=5$, $V_{\text{opt}}=28.1$ V, and $I_{\text{opt}}=1.75$ A are achieved.

(3) Through the analysis of the effects of the solar irradiance $G$ on the system's optimal performances, a maximum efficiency $\eta_{\text{max}}=20.0\%$ and the positive correlation between $Q_{\text{L,}\text{opt}}$ and $G$ are found.

(4) The impacts of the diode's ideal factor $m$, the hot reservoir's temperature $T_{\text{H}}$, and internal resistance $R_{\text{s}}$ and shunt resistance $R_{\text{sh}}$ on the system are revealed. Increasing $m$ and decreasing $T_{\text{H}}$ can improve the system's performance. Considering the non-ideal PV circuit model, the performances of the system are reduced relatively.

The theoretical works proven that the structure parameter of the TERs could be optimized to obtain the maximum efficiency [9]. The results are consistent with the analysis in the present work. The previous experimental work demonstrated that performance of the system is strongly dependent on solar irradiance and temperature difference of hot and cold sides for the TER [10]. The cold reservoir's temperature could maintain the temperature in the refrigerator at $510^{\circ}$C, and have a coefficient of performance (COP) about 0.30. The recent work demonstrated that the cold reservoir's temperature could reach of about $10^{\circ}$C, while the hot reservoir's temperature was about $40^{\circ}$C, resulting a higher COP of about 0.61 [26]. Set $T_{\text{L}}=283$ K and $T_{\text{H}}=313$ K, the TER's highest COP and the PV-TER system's maximum efficiency can, respectively, reach 0.55 and 11% in this work, one can find that the COP is close to that in the Ref. [26].

The proposed model and the analysis provide valuable strategies for solving the parametric design problems between the TERs and the external power devices. Especially, the continuous efficiency enhancement of the perovskite solar cells will further promote the development of solar energy driven TERs.

### Credit author statement
Tianjun Liao: Conceptualization, Methodology, Data curation, Writing- Original draft preparation. Qijiao He: Investigation. Qidong Xu: Formal analysis. Yawen Dai: Validation. Chun Cheng: Visualization. Meng Ni: Project administration; Resources;

Supervision; Writing – review & editing.

Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Acknowledgements

This work has been supported by the Chongqing Research Program of Basic Research and Frontier Technology (cstc2020jcyj-msxmX0001); the Science and Technology Research Program of Chongqing Municipal Education Commission (Grant No. KJQN201901144); Scientific Research Foundation of Chongqing University of Technology (Grant No. 2019ZD22); and Hong Kong Polytechnic University (Project ID: P0014036, account: G-YW3T)..

References

[1] Nayak PK, Mahek S, Snaith HJ, Cahen D. Photovoltaic solar cell technologies: analysing the state of the art. Nat. Rev. Mater. 2019;4:269–85.

[2] Lechene BP, Clerc R, Arias AC. Theoretical analysis and characterization of the energy conversion and storage efficiency of photo-supercapacitors. Sol Energy Mater Sol Cells 2017;172:202–12.

[3] Joos S, Weishar B, Bessler WG. Passive hybridization of a photovoltaic module with lithium-ion battery cells: a model-based analysis. J Power Sources 2017;348:201–11.

[4] Pourkiaei SM, Ahmadi MH, Sadeghzadeh M, Moosavi S, Pourfayaz F, Chen L, Yazdi MAP, Kumar P. Thermoelectric cooler and thermoelectric generator devices: a review of present and potential applications, modeling and materials. Energy 2019;186:115849.

[5] Li G, Shittu S, Zhao X, Ma X. Preliminary experiment on a novel photovoltaic-thermoelectric system in summer. Energy 2019;188:116041.

[6] Yin E, Li Q, Xuan Y. A novel optimal design method for concentration spectrum splitting photovoltaic–thermoelectric hybrid system. Energy 2018;163:519–32.

[7] Kane A, Verma V, Singh B. Optimization of thermoelectric cooling technology for an active cooling of photovoltaic panel. Renew Sustain Energy Rev 2017;75:1295–305.

[8] Najafi H, Woodbury KA. Optimization of a cooling system based on Peltier effect for photovoltaic cells. Sol Energy 2013;91:152–60.

[9] Su S, Chen X, Wang J, Chen J. Performance evaluation and parametric optimum design of a thermoelectric refrigerator driven by a dye-sensitized solar cell. Int. J. Refrigeration 2015;60:62–9.

[10] Dai YJ, Wang RZ, Ni L. Experimental investigation and analysis on a thermoelectric refrigerator driven by solar cells. Sol Energy Mater Sol Cell 2003;77:377–91.

[11] Cheng TC, Cheng C, Huang ZZ, Liao GC. Development of an energy-saving module via combination of solar cells and thermoelectric coolers for green building applications. Energy 2011;36(1):133–40.

[12] Pan Y, Lin B, Chen J. Performance analysis and parametric optimal design of an irreversible multi-couple thermoelectric refrigerator under various operating conditions. Appl Energy 2007;84(9):882–92.

[13] Al-Nimr MA, Mugdad B. A hybrid absorption/thermo-electric cooling system driven by a concentrated photovoltaic/thermal unit. Sustainable Energy Technologies and Assessments 2020;40:100769.

[14] https://www.wholesalesolar.com/1524436/suniva/solar-panels/suniva-opt285-60-4-100-silver-mono-solar-panel.

[15] Shen L, Li Z, Ma T. Analysis of the power loss and quantification of the energy distribution in PV module. Appl Energy 2020;260:114333.

[16] Shang A, Li X. Photovoltaic devices: opto-electro-thermal physics and modeling. Adv Mater 2017;29:1603492.

[17] Ordonez-Miranda J, Ezzahri Y, Drevillon J, Joulain K. Transistorlike device for heating and cooling based on the thermal hysteresis of VO₂. Phys. Rev. Appl. 2016;6:054003.

[18] Liao T, Lin B, Yang Z. Performance characteristics of a low concentrated photovoltaic-thermoelectric hybrid power generation device. Int J Therm Sci 2014;77:158–64.

[19] Liao T, Xiao J, Tao C. Optimal design of a solar cell-driven electroluminescent refrigerator. J Photon Energy 2020;10(4):044502.

[20] Varpula A, Prunnila M. Diffusion-emission theory of photon enhanced thermionic emission solar energy harvesters. J Appl Phys 2012;112(4):044506.

[21] Zhao Q, Zhang H, Hu Z, Hou S. Achieving a broad-spectrum photovoltaic system by hybridizing a two-stage thermoelectric generator. Energy Convers Manag 2020;211:112778.

[22] Kishore RA, Nozariasbmarz A, Poudel B, Sanghadasa M, Priya S. Ultra-high performance wearable thermoelectric coolers with less materials. Nat Commun 2019;10:1765.

[23] Yin E, Li Q, Xuan Y. One-day performance evaluation of photovoltaic-thermoelectric hybrid system. Energy 2018;143:337–46.

[24] Lin J, Liao T, Lin B. Performance analysis and load matching of a photovoltaic–thermoelectric hybrid system. Energy Convers Manag 2015;105:891–9.

[25] Liao T, He Q, Xu Q, Dai Y, Cheng C, Ni M. Performance evaluation and optimization of a perovskite solar cell-thermoelectric generator hybrid system. Energy 2020;201:117665.

[26] Rahman SMA, Hachicha AA, Ghenai C, Saidur R, Said Z. Performance and life cycle analysis of a novel portable solar thermoelectric refrigerator. Case Studies in Thermal Engineering 2020;19. 100599.