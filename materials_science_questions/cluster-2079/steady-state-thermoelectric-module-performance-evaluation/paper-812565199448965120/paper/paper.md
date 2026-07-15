# Parametric design and performance evaluation of a novel solar assisted thermionic generator and thermoelectric device hybrid system

Behzad ranjbar $^{a}$, Mehdi Mehrpooya $^{b, *}$, Mohammad Marefati $^{c}$

$^{a}$ Department of Mechanical Engineering, Faculty of Mechanical Engineering, University of Tabriz, Tabriz, Iran
$^{b}$ Department of Renewable Energies and Environment, Faculty of New Sciences and Technologies, University of Tehran, Tehran, Iran
$^{c}$ Department of Energy Engineering, Faculty of Natural Resources and Environment, Science and Research Branch, Islamic Azad University, Tehran, Iran

---

## ARTICLE INFO

**Article history:**
Received 12 May 2020
Received in revised form
18 August 2020
Accepted 14 September 2020
Available online 20 September 2020

**Keywords:**
Concentrated solar energy
Thermionic generator
Thermoelectric device
Hybrid system and parametric study

---

## ABSTRACT

A novel solar driven hybrid system composed of a concentrated solar collector, thermionic generator and thermoelectric device is proposed. Thermoelectric device uses the waste heat of the thermionic generator to generate further power and cooling. Analytical explanations for the power output and efficiency of the thermionic generator, thermoelectric device and hybrid system are investigated. In order to investigate the design parameters affecting proposed hybrid system performance such as solar irradiance density, anode work function, heat conductivity, ratio of resistances and cooled space temperature sensitivity analysis is discussed. Two different scenarios are considered: the former is assumed the values of climatic data constant and impractical but the latter considers the values of climatic data practically for the data of five different cities in Asia. The results show that since the proposed hybrid system performance depends on the TIG, the increase in ratio of resistances does not have a significant effect on the efficiency and power of the process. The highest and lowest average useful power produced by a solar collector is related to Riyadh and Inchon, respectively. The best optical performance is related to Riyadh (average daily optical efficiency $=67.5\%$).

© 2020 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

In recent years, due to declining conventional energy sources and increased emissions of environmental pollutants due to increased energy demand (50% increase until 2030 [1]), the energy sector future growth is primarily related to renewable energy sources [2]. The main concern of these energy sources is to replace clean and environmentally friendly fuel technologies so that they can solve the problem of fossil fuel scarcity [3]. The main nature of renewable energy is directly from the sun, indirectly from the sun, or from other environmental mechanisms [4]. In terms of energy security, investing in renewable energies can bring significant benefits [2]. Therefore, it is clear that the main and most abundant source of renewable energy is solar energy that is abundant throughout the world [5]. The use of solar energy comes in the form of three common technologies:

- Photovoltaic system(PV); Converting solar energy to electricity [6].
- Solar thermal systems; Producing hot water using solar energy [7].
- Concentrated solar power technology (CSP); Concentrating beam solar radiation to heat up the operating fluid to produce steam to generate electricity [8].

In CSP systems to generate solar power the sunlight concentrates onto the small area receiver using mirrors or lenses, this concentrated energy is then converted to thermal energy to generate electricity (using heat engines or steam turbines) [9]. The four major types of solar CSP technology are [10]:

(1) Parabolic trough collector (PTC); uses parabolic trough mirrors to concentrate the sun rays to the working fluid and then the produced heat drives the steam turbine,
(2) Linear Fresnel reflector (LFR); concentrate the sun rays on the fixed absorber using thin and long reflectors for transfer heat to a heat exchanger to turns the steam turbine [11],

---

* Corresponding author.
E-mail address: mehrpoya@ut.ac.ir (M. Mehrpooya).

https://doi.org/10.1016/j.renene.2020.09.068
0960-1481/© 2020 Elsevier Ltd. All rights reserved.

<div class="tab" data-bbox="62 84 937 448">
<table>
<tbody>
<tr>
<td colspan="3">Nomenclature</td>
<td>J</td>
<td>Electrical current (A)</td>
</tr>
<tr>
<td>amb</td>
<td>Ambient</td>
<td> </td>
<td>I₀</td>
<td>solar irradiance (W/m²)</td>
</tr>
<tr>
<td>c</td>
<td>Cathode</td>
<td> </td>
<td>K</td>
<td>Thermal conductivity (W/K)</td>
</tr>
<tr>
<td>cond</td>
<td>Conduction</td>
<td> </td>
<td>k_B</td>
<td>Constant of Boltzmann (J/K)</td>
</tr>
<tr>
<td>conv</td>
<td>Convection</td>
<td> </td>
<td>N</td>
<td>Number of PDC</td>
</tr>
<tr>
<td>H</td>
<td>Hot</td>
<td> </td>
<td>Nu</td>
<td>Nusselt number Power (W)</td>
</tr>
<tr>
<td>Opt R</td>
<td>Optical Receiver</td>
<td> </td>
<td>P</td>
<td>Prandtl number Thermal power (W)</td>
</tr>
<tr>
<td>rad</td>
<td>Radiation</td>
<td> </td>
<td>Pr</td>
<td>Total resistance of TD (Ω)</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td> </td>
<td>Q/q</td>
<td>External load resistance (Ω)</td>
</tr>
<tr>
<td colspan="3">Abbreviations</td>
<td>R</td>
<td>Reighley number</td>
</tr>
<tr>
<td>CCHP</td>
<td>Combined cooling, heating and power</td>
<td> </td>
<td>R₂</td>
<td>Temperature (°C)</td>
</tr>
<tr>
<td>CSP</td>
<td>Concentrated solar power</td>
<td> </td>
<td>Ra</td>
<td>TIG Voltage (V)</td>
</tr>
<tr>
<td>COP</td>
<td>coefficient of performance</td>
<td> </td>
<td>T</td>
<td>Semiconductor Figure of merit (K⁻¹)</td>
</tr>
<tr>
<td>CR</td>
<td>Cooling rate</td>
<td> </td>
<td>V</td>
<td>Seebeck coefficient</td>
</tr>
<tr>
<td>LFR</td>
<td>Linear Fresnel reflector</td>
<td> </td>
<td>Z</td>
<td>Azimuth angle (°)</td>
</tr>
<tr>
<td>PTC</td>
<td>Parabolic trough collector</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>PV</td>
<td>Photovoltaic</td>
<td> </td>
<td colspan="2">Greek symbol</td>
</tr>
<tr>
<td>ST</td>
<td>Solar tower</td>
<td> </td>
<td>α</td>
<td>Emissivity</td>
</tr>
<tr>
<td>TD</td>
<td>Thermoelectric device</td>
<td> </td>
<td>δ</td>
<td>efficiency</td>
</tr>
<tr>
<td>TEC</td>
<td>Thermoelectric cooler</td>
<td> </td>
<td>ε</td>
<td>Stefan-Boltzmann constant (W/m²K⁴)</td>
</tr>
<tr>
<td>TEG</td>
<td>Thermoelectric generator</td>
<td> </td>
<td>η</td>
<td>Anode work function (eV)</td>
</tr>
<tr>
<td>TIG</td>
<td>Thermionic generator</td>
<td> </td>
<td>σ</td>
<td>Anode</td>
</tr>
<tr>
<td>(m²)</td>
<td>Aperture area of solar collector</td>
<td> </td>
<td>φₐ</td>
<td>A₀</td>
</tr>
<tr>
<td>Aₐ</td>
<td>Constant of Richardson-Dushman (A/m²K²)</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>I</td>
<td>Current density (A/m²)</td>
<td> </td>
<td colspan="2">Subscripts</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td> </td>
<td>A</td>
<td> </td>
</tr>
</tbody>
</table>
</div>

(3) Solar towers (ST); concentrate the sun rays on the central receiver to heat the working fluid and then the produced heat drives the steam turbine,

(4) Parabolic dish collector (PDC); concentrate the sun rays on the central receiver using dish mirrors to produce steam needed for power turbine [12].

In this study, the PDC is used as a heat source. One of the major developed and widely used solar CSP technology is the PDC [13]. The PDC generates thermal energy at 100-1500 °C [14] for high-temperature thermal applications (due to the high-concentration ratio) [15] PDCs are possible (not proven) for storage with molten salt and demonstration projects for maturing technology, and have a medium risk of technology development [16].The efficiencies of commercial PDC plants are about 25-30%, which is higher than LFR (8-10%), ST (15-20%) and PTC (15%) [17]. In recent years, many efforts have been devoted on PDCs to achieving high-temperature levels, high thermal efficiency, and low cost of production as well as developing new cycles of bottoming power [18]. To now, many researchers have theoretically and experimentally investigated the performance of PDC. Ahmadi and Mehrpooya [19] developed the normalized objective function based on NSGA-II method to deter- mine the thermal efficiency and power output of the solar-driven heat engine. In another study [20] (PDC-powered Stirling engine), they concluded that optimization of multi-objective can achieve results with a relatively low deviation from the ideal solution compared to the conventional one objective approach. Yaqi et al. [13] reported the optimum values for thermal efficiency and con- centration ratio of 34% and 1300, respectively. Moradi and Mehr- pooya [21] used the PDC in a CCHP system with a solid oxide fuel cell in a commercial building in Tehran. In their proposed hybrid system the PDC supplies 602 kW of thermal power in maximum solar radiation. The overall efficiency and investment cost of the system are 79.5% and 3.5 million dollar, respectively. The design, simulation, and optimization of the PDC- Stirling engine system with consideration of the thermal effects on the solar system's power generation and different designs of PDC was investigated by Hafez et al. [12]. The cost analysis of a small scale PDC-gas turbine hybrid system based on original equipment manufacturers data is presented by Gavagnin et al. [22]. The installation cost of this sys- tem for solar-only and hybrid systems are 3250 and 3300 Euro/kW. In another study [23], the thermal energy produced by the PDC was used to produce hydrogen by a solid oxide electrolyzer. In this design one PDC reduce the fuel consumption of compressed air energy storage and another PDC generate thermal energy. The system is capable of generating 41.5 Kg of hydrogen per day and system efficiency equal to 72.7%.

In the CSP technologies, the thermal energy is first converted to mechanical energy and then by the generator to electrical energy (dynamic power). But in another way, can be directly convert thermal energy into electrical energy (static power). In recent years, the latter has been widely used with means such as therm- ionic generator (TIG), thermoelectric generator (TEG) and ther- moelectric cooler (TEC) [24]. As mentioned, the heat generated by CSP systems can be used in different applications. One of these applications is the use of heat generated in the TIG and TEG hybrid system [25]. TIG is one example of bottoming power cycle that directly produces electrical energy using two components: first heat (source of energy) and second electrons (substance of work- ing) [26]. The TIG consists of three components: cathode, anode and external load. The cathode absorbs heat from the solar system (as the heat source) and then anode releases waste heat into the heat sink. The external load allows the load to move. Therefore, electron emission from the hot electrode to the cold electron causes the electric current [27]. To generate this continuous electric cur- rent, the TIG needs a heat source with a temperature of about 1500 K [28]. In this research, the high temperature heat is supplied by the PTC. Lamba and Kaushik [29] investigated the energy and exergy analysis of TIG based on thermodynamic model and deter- mined the effect of various parameters such as work function of

anode and voltage on the TIG performance. Their results show that the energy and exergy efficiencies are 44% and 54%, respectively. Optimizing the TIG emitter -collector gaps to increase its conver- sion efficiency was performed by Lee et al. [30]. Another study investigated the usability of structure of few layer graphene as a TIG cathode [31]. Experimental performance of the TIG using molyb- denum electrodes was performed by El-Genk et al. [32], which had power density and efficiency of 3.2 W/cm² and 12.5%, respectively. Overcoming the obstacles related to the space barrier in the gap between the electrode and the high anodic work function was performed by Yuan et al. [33]. Two times as large as the power density for the thermionic-photovoltaic system compared to the thermophotovoltaic and TIG at temperature of 1650 K was reported by Datas [34].

On the other hand, the thermoelectric device (TD = TEG + TEC) can be used with low quality thermal energy sources to generate electricity and cooling load. Thus, the TD can be thermally con- nected to the TIG anode and used as a TIG-TD hybrid system to generate electricity and cooling [11]. This increases the use of heat released by the anode. Furthermore, using the electricity produced by the TEG, the cooling load can be generated by using the TEC, which is based on the voltage addition to two materials. TEGs produce power based on the Seebeck effect that results from the temperature difference between cold and hot junctions [35]. TEGs are ideal for small applications because of their advantages such as being compact, divisible and inexpensive [36]. Wang et al. [37] calculated the TIG and TEG temperatures using equations of energy balance. Furthermore, they considered the effect of system irre- versible losses, Thomson effect, TIG work function and TEG electric current. In another study based on non-equilibrium thermody- namic the effect of TIG work function and voltage as well as TEG resistance ware investigated [38]. A novel hybrid system consists of TIG, TEG and CSP technology with consideration irreversible losses proposed by Su et al. [39]. This system has a maximum efficiency of 45.7%. Furthermore, they obtained useful results for the optimal design of experimental hybrid works. Another combined system consisting of TIG-TEG refrigerator developed by Ding et al. [40]. Their study showed that the proposed combined system has the better performance than the independent TIG refrigerator system. The solar powered hybrid system consists of TIG and TEG devel- oped by Naito et al. [41]. In this design the temperature of solar receiver is 1965 K. A similar system designed by Bellucci et al. [42] for CSP applications. The conversion efficiency of this hybrid system is more than 30%. The reviews of performance of this hybrid system and methods that can improve its efficiency were conducted by Xiao et al. [43]. Hou and Zhang [44] proposed the cogeneration system consist of TIG, PDC and absorption refrigerator to produce cooling and electrical demands. In their proposed system the PDC provide the required heat of the TIG and TIG waste heat is used to produce cooling. The efficiency of this hybrid system is 27.1%.

A novel solar driven hybrid system composed of a concentrated solar collector, TIG and TD is proposed in present research, in which the TD uses the waste heat of the TIG to generate further power and cooling. The analytical explanations for the power output and ef- ficiency of the thermionic generator, TD and total system are investigated. In order to investigate the design parameters affecting proposed hybrid system performance such as solar irradiance density, anode work function, heat conductivity, ratio of resistances and cooled space temperature sensitivity analysis is discussed. Two different scenarios are considered: the former is assumed the values of climatic data constant and impractical but the latter considers the values of climatic data practically for the data of five different cities in Asia. The originality and major novelties of this research as follows:

- The proposed hybrid system innovation is in relationships be- tween its components, which has not been discussed in previ- ous studies;
- In previous similar works, climatic data are considered constant values, but in the present study real climate data for five cities in Asia are considered, in fact the performance of the proposed hybrid system for real weather data is investigated;
- By changing the climatic data, the obtained results of the pre- sent work can be applied to other regions;
- Decrease fossil fuel consumption and thus reduction green- house gas emissions through the use of solar energy;
- Apply the obtained results of sensitivity analysis for use in experimental works.

## 2. System description

Fig. 1 shows the schematic diagram of the proposed solar powered hybrid system, which consists of concentrated solar po- wer system (PDC-type), TIG, TEG and TEC to produce the electrical and cooling load. As a constant temperature heat source of TIG the PDC first absorbs beam solar irradiation and then converts it into thermal energy. The TIG consists of two cathode and anode plates that are connected to the solar collector and the hot end of the TEG, respectively. The principle of TIG performance is: the generated electrons pass through the gap between the electrodes, then condense in the anode and finally return to the cathode through an external load to convert the some of the heat to electrical energy [30]. In the next step, the waste of the anode plate of TIG to the TEG hot end and generates additional electrical power. In the final step, the TEC module provides the cooling load by absorbing heat from the cooled space. The electrical power required to do this is sup- plied by the TEG. Thus, the proposed hybrid system generates electrical and cooling load. It should be noted that in this study, the concentrator and the receiver details of the PDC are not discussed and the PDC is used only as an as a constant temperature of thermal energy production that converts the sun's light energy into heat. In addition, the assumptions considered in present paper are the same as Ref. [44].

### 2.1. Parabolic dish collector modeling

The thermal model of the PDC is shown in Fig. 2. The energy incident on the concentrator depends on two factors: direct normal irradiance and dish aperture area. The receiver absorbs a part of this energy depending on the PDC optical efficiency [45]. Geometry and material properties are two key factors in determining the PDC optical efficiency (see Fig. 3) [46]. The PDC sun tracking system is bi-axial. At high temperatures (up to 1450 K), resistant metals or resistant alloys should be used [46]. Determination of useful ther- mal energy (Q<sub>PDC</sub>), optical efficiency ($\eta_{opt}$) and thermal efficiency ($\eta_{PDC}$) of the PDC are the three main parameters for analyzing its performance. Table 1 presents the relationships related to PDC calculations. It should be noted that, the geometrical concentration ratio and aperture area of PDC are equal to 1800 and 12.5 m², respectively. So, the value of A<sub>c</sub> is obtained to 0.0069 m². Further- more, the value of A<sub>w</sub> is considered to 0.0645 m². Furthermore, in this paper it is assumed that, the tracking direction and orientation of PDC are east-west and north-south directions, respectively.

### 2.2. Thermionic generator modeling

Under normal operating conditions, after the TIG cathode ab- sorbs heat from the PDC (Q<sub>PDC</sub>), the thermalized electrons emit from the cathode to the anode [47]. The work functions difference

![](./images/812565199448965120_1.jpg)

Fig. 1. Schematic diagram of the proposed hybrid system.

between the two sides of the TIG plays an important role in the output voltage [37]. TIG net electrical current densities (based on Richardson-Dushman equation) are given by the following equation [48]:

$$J_{TIG}=J_{c}-J_{a} \tag{1}$$

where, $J_{c}$ anf $J_{a}$ are the cathode and anode current densities, respectively, and calculated by equations (2) and (3):

$$J_{c}=A_{0} × T_{c}^{2} × \exp \left(-\frac{\phi_{a}+q V}{k_{B} × T_{c}}\right) \tag{2}$$

$$J_{a}=A_{0} × T_{a}^{2} × \exp \left(-\frac{\phi_{a}}{k_{B} × T_{a}}\right) \tag{3}$$

In the above equations $T_{c}, T_{a}, \phi_{a}, V, A_{0}, q$ and $k_{B}$ are the cathode and anode temperatures, anode work function, TIG voltage, constant of Richardson-Dushman $(A_{0}=120 ~A /(cmK)^{2})$, electron charge value $(q=1.60 × 10^{-19} C)$ and constant of Boltzmann $(k_{B}=1.38 × 10^{-23} ~J / K)$, respectively.

Considering the losses of radiation heat between the two electrodes, the following equations can be used to determine the rates of heat absorbed by the cathode and released by the anode, respectively [49]:

$$
\begin{aligned}
q_{c}= & A_{c} × J_{c} ×\left(V+\frac{\phi_{a}+2 k_{B} T_{c}}{q}\right)-A_{a} × J_{a} ×\left(V+\frac{\phi_{a}+2 k_{B} T_{a}}{q}\right) \\
& +A_{c} \varepsilon_{L} \delta ×\left(T_{c}^{4}-T_{a}^{4}\right)
\end{aligned}
\tag{4}
$$

$$
\begin{aligned}
q_{a}= & A_{c} × J_{c} ×\left(\frac{\phi_{a}+2 k_{B} T_{c}}{q}\right)-A_{a} × J_{a} ×\left(\frac{\phi_{a}+2 k_{B} T_{a}}{q}\right)+A_{a} \varepsilon_{L} \delta \\
& ×\left(T_{c}^{4}-T_{a}^{4}\right)
\end{aligned}
\tag{5}
$$

According to equations (4) and (5), TIG power and efficiency are determined by the next relationships [44]:

$$
\begin{aligned}
P_{TIG}= & A_{c} × A_{0} × V ×\left\{T_{c}^{2} × \exp [\right. \\
& \left.\left.-\left(\phi_{a}+q V\right) /\left(k_{B} T_{c}\right)\right]-T_{a}^{2} \exp \left[-\phi_{a} /\left(k_{B} T_{a}\right)\right]\right\}
\end{aligned}
\tag{6}
$$

$$\eta_{TIG}=\frac{P_{TIG}}{q_{c}} \tag{7}$$

![](./images/812565199448965120_2.jpg)

Fig. 2. PDC thermal model [21].

### 2.3. Thermoelectric device modeling

The p-type and n-type semiconductors are connected together to form the thermoelectric device (TD). Thermoelectric device are of two types: TEG (series electrical connected) and TEC (parallel thermal connected) [50]. TEG uses the heat released from the TIG's anode and generates electrical energy. This generated energy is used to drive the TEC to produce cooling. Table 2 shows the principles of operation and relationships required for the thermoelectric device. Four important parameters in evaluating td performance are: output power and efficiency (related to TEG), coefficient of performance (COP) and the cooling rate (CR) (related to TEC) [36]. Note that, to solve the problem of large temperature gap, the effect of Thomas in the TEG is ignored. Furthermore, the requirement parameters for modeling of td are the same as Ref. [50].

### 2.4. Hybrid system modeling

By summing the TIG and TD power, the hybrid system power of can be obtained as follows [48,50]:
$$P=P_{TIG}+P_{TD} \tag{8}$$

Accordingly, the hybrid system efficiency can be calculated by the next equation [37]:
$$\eta=\frac{P}{Q_{PDC}}=\frac{P_{TIG}+P_{TD}}{Q_{PDC}} \tag{9}$$

### 2.5. Energy balance equations

Using the energy balance, the corresponding temperatures can be obtained under standard conditions as follows:

$$
\begin{aligned}
Q_{r}-Q_{loss} &=A_{0} × T_{c}^{2} × \exp \left(-\frac{\phi_{a}+q V}{k_{B} × T_{c}}\right) × \frac{\phi_{a}+q V+2 k_{B} T_{c}}{q} \\
& \quad -A_{0} × T_{a}^{2} × \exp \left(-\frac{\phi_{a}}{k_{B} × T_{a}}\right) × \frac{\phi_{a}+q V+2 k_{B} T_{a}}{q}+\varepsilon_{L} \delta ×\left(T_{c}^{4}-T_{a}^{4}\right)
\end{aligned} \tag{10}
$$

![](./images/812565199448965120_3.jpg)

Fig. 3. Steps of optical-geometric analysis of PDC.

<table>
<caption>Table 1 Relationships related to PDC calculations [12,15,21].</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Equation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Useful thermal energy</td>
<td>$Q_{PDC}=Q_{r}-Q_{loss}$</td>
<td>$Q_{r}$: Energy absorbed by the receiver</td>
</tr>
<tr>
<td>Optical efficiency</td>
<td>$\eta_{opt}=\frac{Q_{r}}{Q_{S}}$</td>
<td>$Q_{S}$: Energy incident on the concentrator aperture</td>
</tr>
<tr>
<td>Thermal efficiency</td>
<td>$\eta_{PDC}=\frac{Q_{PDC}}{Q_{S}}$</td>
<td></td>
</tr>
<tr>
<td>Receiver total heat loss</td>
<td>$Q_{loss}=Q_{cond}+Q_{conv}+Q_{rad}$</td>
<td>cond: Conduction loss (neglected in this study)</td>
</tr>
<tr>
<td>Convection loss</td>
<td>$Q_{conv}=h_{c}×A_{w}×(T_{w}-T_{amb})$<br>$T_{w}$: Cavity wall temperature<br>Nu: Nusselt number<br>$Ra_{L}$: Reighley number<br>Pr: Prandtl number</td>
<td>$h_{c}=\frac{Nu×K}{L_{s}}$<br>$L_{s}=\left|\sum_{i=1}^{3}a_{i}\cos(\phi+\theta_{i})^{b_{i}}×L_{i}\right|$<br>$Nu = 0.0196×Ra_{L}^{0.41}×Pr^{0.13}$<br>$Ra_{L}=\frac{g\beta×(T_{w}-T_{amb})×L_{s}^{3}}{\alpha×v}$<br>$\Pr=v/\alpha$</td>
</tr>
<tr>
<td>Radiation loss</td>
<td>$Q_{rad}=A_{c}×\varepsilon_{eff}×\sigma×(T_{w}^{4}-T_{amb}^{4})$</td>
<td>$\varepsilon_{eff}=\frac{1}{1+\left(\frac{1}{\varepsilon_{c}}-1\right)×\frac{A_{c}}{A_{W}}}$<br>$A_{c}=\pi d^{2}/4$<br>$A_{W}=\pi d^{2}/4+\pi dL$</td>
</tr>
<tr>
<td>Note:</td>
<td>$0.8<\varepsilon_{c}<1$<br>$A_{W}/A_{c}>5$</td>
<td></td>
</tr>
</tbody>
</table>

(1) In the TIG cathode ($\mathrm{Q_{PDC}=q_{c}}$):

$$
=\frac{Z × K × T_{a} ×\left(T_{a}-T_{2}\right)}{1+\frac{R_{2}}{R}}+K ×\left(T_{a}-T_{2}\right)-\frac{Z × K ×\left(T_{a}-T_{2}\right)^{2}}{2 ×\left(1+\frac{R_{2}}{R}\right)^{2}}
\tag{11}
$$

(2) In the TIG anode ($\mathrm{q_{a}=Q_{H}}$):

$$
A_{c} × J_{c} ×\left(\frac{\phi_{a}+2k_{B}T_{c}}{q}\right)-A_{a} × J_{a} ×\left(\frac{\phi_{a}+2k_{B}T_{a}}{q}\right)+A_{a}\varepsilon_{L}\delta ×\left(T_{c}^{4}-T_{a}^{4}\right)
$$

(3) In the cold end of TEG:

<table>
<caption>Table 2 Principles of operation and relationships required for the thermoelectric device [11,48,52–54].</caption>
<thead>
<tr>
<th>Step</th>
<th>Description</th>
<th>Equation</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Assumption: T<sub>TEG hot end</sub> = T<sub>TIG anode</sub></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Calculate the heat absorbed by TEG hot end</td>
<td>$Q_{H}=\alpha T_{a}I + K\times(T_{a}-T_{2})-\frac{I^{2}\times R}{2}$<br>T<sub>2</sub>: Cold end temperature of TEG</td>
</tr>
<tr>
<td>3</td>
<td>Calculate the heat released from the TEG</td>
<td>$Q_{L}=\alpha T_{2}I + K\times(T_{a}-T_{2})+\frac{I^{2}\times R}{2}$</td>
</tr>
<tr>
<td>4</td>
<td>Calculate the TEG output power</td>
<td>$P_{TD}=P_{TEG}=Q_{H}-Q_{L}=I^{2}\times R_{2}$<br>R: Total resistance of TD<br>R<sub>2</sub>: External load resistance</td>
</tr>
<tr>
<td>5</td>
<td>Calculate the electric current of td</td>
<td>$I=\frac{\alpha\times(T_{a}-T_{2})}{R + R_{2}}$</td>
</tr>
<tr>
<td>6</td>
<td>Substitute step 5 into step 4</td>
<td>$P_{TD}=\frac{ZK\times(T_{a}-T_{2})^{2}}{\left(1+\frac{R_{2}}{R}\right)^{2}}\times\frac{R_{2}}{R}$</td>
</tr>
<tr>
<td>7</td>
<td>Calculate the TD efficiency</td>
<td>$\eta_{TD}=\frac{\frac{Z\times(T_{a}-T_{2})}{(1 + R_{2}/R)^{2}}\times\frac{R_{2}}{R}}{ZT_{a}/1 + R_{2}/R + 1-\frac{Z\times(T_{a}-T_{2})}{2\times(1 + R_{2}/R)^{2}}}$</td>
</tr>
<tr>
<td>8</td>
<td>Calculate the coefficient of performance</td>
<td>$COP=\frac{Q_{L}}{Q_{H}}$</td>
</tr>
<tr>
<td>9</td>
<td>Calculate the cooling rate</td>
<td>$CR = Q_{L}$</td>
</tr>
<tr>
<td>Note</td>
<td colspan="2">α: Seebeck coefficient, K: Total thermal conductivity of TD, Z: Figure of merit of semiconductor material</td>
</tr>
</tbody>
</table>

$$
\begin{aligned}
K_{L} \times\left(T_{2}-T_{L}\right)=& \frac{Z \times K \times T_{2} \times\left(T_{a}-T_{2}\right)}{1+\frac{R_{2}}{R}}+K \times\left(T_{a}-T_{2}\right) \\
&+\frac{Z \times K \times\left(T_{a}-T_{2}\right)^{2}}{2 \times\left(1+\frac{R_{2}}{R}\right)^{2}}
\end{aligned}
\tag{12}
$$

### 3. Validation of numerical modeling

The proposed hybrid system in this work has not been numerically and experimentally investigated and no study has reported numerical and experimental work on the proposed system, so the whole system cannot be validated with numerical and experimental data. But since PDC and TIG have been analyzed in some studies, they can be validated separately.Fig. 4-a and 4-b show the validation of thermal efficiency of PDC and validation of output power of TIG, respectively. Note that the design parameters mentioned in Refs. [38,51] are used for PDC and TIG validation, respectively. The Figures show that the maximum deviation in the graphs for PDC and TIG validation is 1.2% and 1.7%, respectively. Therefore, it can be said that the obtained results of numerical modeling in this paper are reasonable and acceptable.

![](./images/812565199448965120_4.jpg)

Fig. 4. Model validation with experimental data; (a) validation of thermal efficiency of PDC and (b) validation of output power of TIG.

### 4. Results and discussions

Two scenarios are considered in this section:

#### 4.1. First scenario

In the first scenario, the values of climatic data are considered constant and PDC performance is evaluated without considering the weather conditions and solar radiation, and at constant values. The proposed hybrid system in this work consists of PDC, TIG and TD to produce power and cooling. Therefore, in the present study, the main purpose of mathematical modeling is to determine the key parameters of the proposed system, namely output power, efficiency of conversion, cooling rate and coefficient of performance. The key parameters required for numerical modeling of the proposed system are given in Table 3. To solve the problem, iterative

<table>
<caption>Table 3
The key parameters required for numerical modeling [48,55].</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Richardson-Dushman constant</td>
<td>$1.2 × 10^6$A/m² K²</td>
<td>Thermoelectric module thermal conductivity</td>
<td>61.3 W/K</td>
</tr>
<tr>
<td>Stefan-Boltzmann constant</td>
<td>$5.67 × 10^{-8}$W/m² K⁴</td>
<td>Heat conductivity between TEG and TEC</td>
<td>60 W/K</td>
</tr>
<tr>
<td>Boltzmann constant</td>
<td>$1.38 × 10^{-23}$J/K</td>
<td>TIG voltage</td>
<td>0.2 V</td>
</tr>
<tr>
<td>Ambient temperature</td>
<td>25 °C</td>
<td>Anode work function</td>
<td>1 eV</td>
</tr>
<tr>
<td>Optical efficiency</td>
<td>0.95</td>
<td>Area of TIG plates</td>
<td>$1.6 × 10^{-2}$m²</td>
</tr>
<tr>
<td>Ratio of resistance</td>
<td>1</td>
<td>Aperture area of PDC</td>
<td>12.5 m²</td>
</tr>
<tr>
<td>solar irradiance</td>
<td>$1.2 × 10^6$ W/m²</td>
<td>Cavity wall temperature</td>
<td>827 °C</td>
</tr>
</tbody>
</table>

![](./images/812565199448965120_5.jpg)

Fig. 5. Performance of the proposed hybrid system versus solar irradiance density; (a) output power, (b) efficiency, (c) cooling rate and (d) COP.

method is used in MATLAB software. Given the appropriate initial values, the unknown parameters in equations (10)-(12) are determined. Then, the efficiency and power of TIG, TEG and the total system, as well as CR and COP of TEC are calculated. Since the performance of the TIG and the TD depends on the operation conditions and design parameters, the impacts of various parameters on the performance of them, and consequently, the performance of hybrid system should be investigated using sensitivity analysis.

### 4.1. Sensitivity analysis of solar irradiance

Based on the design parameters listed in Table 3, Fig. 5 gives the power and efficiency of TIG, TD, and the hybrid system, as well as CR and COP of TEC with solar irradiance density. Note that the solar irradiance density range is $0-3 × 10^6$W/m². Obviously, for the hybrid system, the TIG power rises initially until reaching a maximum value and then it starts to reduce, while the TD power rises faster with the solar irradiance increasing. Accordingly, the hybrid system total power first increases and then decreases with solar irradiance. This means that there is a critical point of the solar irradiance, which is equal to $2.3 × 10^6$ W/m². That is, with increasing the solar irradiance the hybrid system power does not increase uniformly, which is inconsistent with ordinary thinking. This trend reason is that, due to the fixed area of the two plates of TIG, the input solar energy increases linearly with the solar irradiance. However, the TD power grows faster than the input solar energy; therefore, the TIG power starts to decrease and even becomes less than that of TD with further increasing of solar irradiance. In addition, since the power of the system drops sharply after the critical point, it is necessary to adjust the value close to the

critical point. However, this issue will be investigated in the next scenario. Generally, it can be said that the TD increases more than 37% of the total power of the hybrid system.

According to Fig. 5-b for the hybrid system, the efficiency of TIG slowly decreases initially, but decreases faster after the solar irradiance reaches the critical point. While TD efficiency regularly increased with increasing solar irradiance. As a result, hybrid system efficiency increases initially and then decreases after reaching the critical point. So, it can be said that, the proposed system efficiency gives distinct tendency with the increasing solar irradiance. Finally, it can be stated that the TD increases the efficiency of the system by 3.3%. Fig. 5-c and 5-d show the performance of TEC. Clearly, with increasing the solar irradiance, the cooling rate increases but the COP decreases. However, the decrease in COP is not very noticeable but the CR increases faster. By changing the solar irradiance from $0.6 \times 10^6$ W/m² to $1.2 \times 10^6$ W/m², the CR increases by 94.8% but the COP decrease is only about 2.2%. To sum up, TIG is suitable for high temperature heat source and TD for low temperature heat source. But in practice high-temperature energy supplies require substantial preparations.

### 4.1.2. Sensitivity analysis anode work function

Fig. 6 shows the performance of the proposed hybrid system versus solar irradiance density at different work function of anode. It is clear that, as the anode work function increases, the total efficiency and power of the proposed system both decrease. In addition, the cooling rate increases with increasing anode work function but the COP decreases. With changing the anode work function from 1 eV to 1.4 eV, the proposed system total power and efficiency decrease by 12.42% and 2.86%, respectively. Furthermore, the CR increases by 9.1% but the COP decrease is only about 0.2%. Nevertheless, it can be said that the COP change is not significant. Further investigation of numerical modeling revealed that the total efficiency and power of the proposed system are affected by the performance of the TIG. Because with increasing anode work function, TIG efficiency drops by 3.45% but TD efficiency only increases by about 0.16%. Consequently, for better system performance it is suggested that to set the anode work function to a lower value.

### 4.1.3. Sensitivity analysis of heat conductivity

The heat conductivity presents the waste heat from the TEG to the TEC. In fact, it is assumed that heat loss affects the performance of the proposed system. The effect of heat conductivity on the performance of the proposed hybrid system is shown in Fig. 6. As shown in Fig. 7-a, it is obvious that due to the importance of the TD contribution, the total power of the proposed hybrid system will grow less slowly with increasing heat conductivity. When the heat conductivity doubles, the TIG power output does not change significantly (a 0.18% increase), but the TD power output increases

![](./images/812565199448965120_6.jpg)

Fig. 6. Performance of the proposed hybrid system versus solar irradiance density at different work function of anode; (a) output power, (b) efficiency, (c) cooling rate and (d) COP.

![](./images/812565199448965120_7.jpg)

Fig. 7. Performance of the proposed hybrid system versus heat conductivity; (a) output power, (b) efficiency, (c) cooling rate and (d) COP.

by 22.2%. Therefore, for the proposed system, the effect of heat conductivity is less important, because the TIG waste heat is recovered by the TD and the total power of the hybrid system increases greatly (an 8.35% increase). From the efficiency point of view, this is confirmed in Fig. 7-b, namely, when the heat conductivity doubles, the efficiency of TIG increase is only about 0.04%, but the efficiency of TD increases by 1.1%. In fact, doubling the heat conductivity does not significantly change the total efficiency of the proposed hybrid system and shows an increase of less than 1% (0.94%). TEC performance also decreases with increasing heat conductivity, as Fig. 6c and d confirm. However, this decrease is not very significant, since with doubling the heat conductivity, CR and COP decrease by only <1% and 1.17% respectively.

### 4.1.4. Sensitivity analysis of ratio of resistances
Fig. 8 shows the effect of ratio of $R_2/R$ on the performance of the proposed system. Obviously, with increasing ratio of resistances the TIG power output and efficiency is almost constant, but the efficiency and power of TD increases. However, the power output and efficiency of the TD remains constant after reaching the critical point ($R_2/R=1.6$). Therefore, since the proposed hybrid system performance is mainly dependent on that of the TIG, the increase in ratio of resistances does not have a significant effect on the efficiency and power of the proposed system. For example, by increasing the ratio of resistances from 1 to 2, the power and efficiency of the proposed process increase by only 3.5% and 1.03%, respectively. Performance of proposed hybrid system changes by ratio of resistances can be attributed to temperature changes. With the increasing of ratio of resistances, the temperature of TIG cathode remains constant, while the temperature of anode of TIG gently increases and the cold end of TEG temperature drops first and then switches off. The performance of TEC also decreases with increasing ratio of resistances, as Fig. 8-c, d confirm. By increasing the ratio of resistances from 1 to 2, the CR and COP decrease by 1.39% and 1.35%, respectively. So it can be said that this decrement is not very significant.

### 4.1.5. Sensitivity analysis of temperature of cooled space
The effect of temperature of cooled space on the performance of the proposed solar assisted TIG-TD hybrid system is shown in Fig. 9. As observed, both total efficiency and power of the proposed system are decreased as cooled space temperature increases. Furthermore, both CR and COP are increased as cooled space temperature increases. But all four of these parameters are very low sensitive to the variation of cooled space temperature. When the temperature of cooled space raises 10 °C, the proposed system power and efficiency decrease by only 0.65% and 0.07%, respectively. In addition, the CR and COP increase by only 0.07% and 0.09%,

![](./images/812565199448965120_8.jpg)

Fig. 8. Performance of the proposed hybrid system versus ratio of resistances; (a) output power, (b) efficiency, (c) cooling rate and (d) COP.

respectively. Therefore, it was found that temperature of cooled space is not a very effective parameter on the performance of the proposed system.

The features and limitations of the first scenario can be summarized as follows:

- Understand how the proposed hybrid system works and identify the relationships between its various components;
- Identification of parameters affecting system performance, using sensitivity analysis;
- This scenario is not practical because of the constant assumption of climatic data.

### 4.2. Second scenario

As mentioned, in the present study the PDC provides the required thermal power of the TIG cathode. In the previous scenario, the values of climatic data were considered constant and PDC performance was evaluated without considering the weather conditions and solar radiation, and at constant values. However, in this scenario the PDC performance for real weather conditions is investigated. Optical and thermal analysis should be considered to evaluate the performance of the PDC. Optical modeling is to determine the collector optical efficiency and thermal modeling is to determine the useful thermal power and the thermal efficiency of the collector. To evaluate the performance of this solar system the five cities in Asia are considered. These cities are Yazd (in Iran), Istanbul (in Turkey), Beijing (in China), Inchon (in Korea) and Riyadh (in Saudi Arabia). Fig. 10 shows the average solar insolation in these cities. Obviously, the annual average solar insolation in Yazd, Istanbul, Beijing, Inchon and Riyadh is 5.34, 3.91, 4.28, 4.01 and 5.69 kWh/m²/day, respectively. Table 3 shows the climate and geographic characteristics for these regions in selected day (8 Jun). From Table 3 and comparing the solar irradiance of different cities on a given day, the PDC performance in Riyadh is expected to be better than in other regions. In order to understand this, the PDC performance is evaluated using the environment of MATLAB software.

The mathematical numerical results of the PDC are shown in Figs. 11-14. By comparing the diagrams in Fig. 11, it is clear that the lowest and highest optical efficiency occur in Beijing (8 a.m.) and Riyadh (1 p.m.), which equal 53.71% and 78.13%, respectively. As shown in Table 4, clearly the PDC has the best optical performance in Riyadh because its average daily optical efficiency in selected day is 67.5%, which is higher than other regions. In addition, solar collector with the average daily optical efficiency of 63.38% in Beijing has the weakest optical performance among other regions. Moreover, the highest and lowest values of useful power are related to Riyadh (1 p.m.) and Inchon (8 a.m.), which are 692.88 W/m² and zero respectively (see Fig. 12). In such a context (8 a.m. in Inchon)

![](./images/812565199448965120_9.jpg)

Fig. 9. Performance of the proposed hybrid system versus solar irradiance density at different temperature of cooled space; (a) output power, (b) efficiency, (c) cooling rate and (d) COP.

![](./images/812565199448965120_10.jpg)

Fig. 10. Average solar insolation in different climatic zones [57].

![](./images/812565199448965120_11.jpg)

Fig. 11. Optical efficiency of PDC in different climatic zones on 8 Jun.

![](./images/812565199448965120_12.jpg)

Fig. 12. Useful power of PDC in different climatic zones on 8 Jun.

![](./images/812565199448965120_13.jpg)

Fig. 13. Thermal efficiency of PDC in different climatic zones on 8 Jun.

![](./images/812565199448965120_14.jpg)

Fig. 14. The number of PDC in different climatic zones on 8 Jun.

the PDC is unable to generate useful power due to the low intensity of solar irradiance $(7\ \text{W/m}^2)$. The highest and lowest average useful power produced by a solar collector is 507.95 and $132.99\ \text{W/m}^2$, respectively, whishes related to Riyadh and Inchon. Finally, in terms of thermal efficiency, the best and the weakest PDC performance are related to Riyadh and Incheon, respectively (see Fig. 13). The

<table>
<caption>Table 4 Climate and geographic characteristics for selected regions [56].</caption>
<thead>
<tr>
<th>Zone</th>
<th>Latitude (°)</th>
<th>Longitude (°)</th>
<th>Average daily solar irradiance (W/m²)*</th>
<th>Average ambient Temp (°C)*</th>
<th>Average air velocity (m/s)*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Yazd</td>
<td>31.9</td>
<td>54.3</td>
<td>435.1</td>
<td>31.9</td>
<td>1.9</td>
</tr>
<tr>
<td>Istanbul</td>
<td>40.9</td>
<td>28.8</td>
<td>711.9</td>
<td>22.1</td>
<td>3.4</td>
</tr>
<tr>
<td>Beijing</td>
<td>39.8</td>
<td>116.5</td>
<td>690.4</td>
<td>26.2</td>
<td>6.3</td>
</tr>
<tr>
<td>Inchon</td>
<td>37.5</td>
<td>126.5</td>
<td>251.8</td>
<td>21.1</td>
<td>6.6</td>
</tr>
<tr>
<td>Riyadh</td>
<td>24.7</td>
<td>46.8</td>
<td>784.6</td>
<td>39.5</td>
<td>2.6</td>
</tr>
</tbody>
</table>

* These data are average data from 8:00 a.m. to 4:00 p.m. in 8 Jun.

<table>
<caption>Table 5 Summary of Figs. 10-13.</caption>
<thead>
<tr>
<th>Zone</th>
<th>Average of optical efficiency (%)</th>
<th>Average of thermal efficiency (%)</th>
<th>Average of useful power (W/m²)</th>
<th>Average of collector number</th>
</tr>
</thead>
<tbody>
<tr>
<td>Yazd</td>
<td>67.08</td>
<td>61.1</td>
<td>265.71</td>
<td>355</td>
</tr>
<tr>
<td>Istanbul</td>
<td>65.94</td>
<td>62.92</td>
<td>446.01</td>
<td>214</td>
</tr>
<tr>
<td>Beijing</td>
<td>63.38</td>
<td>60.34</td>
<td>414.55</td>
<td>232</td>
</tr>
<tr>
<td>Inchon</td>
<td>63.84</td>
<td>40.67</td>
<td>132.99</td>
<td>1229</td>
</tr>
<tr>
<td>Riyadh</td>
<td>67.5</td>
<td>64.98</td>
<td>507.95</td>
<td>197</td>
</tr>
</tbody>
</table>

daily average PDC thermal efficiency in Riyadh and Incheon is 64.98% and 40.67%, respectively. Therefore, as expected, Riyadh has the best performance in comparison to other regions; because Riyadh has the highest intensity of solar irradiance among other cities (see Table 5).

In continuation of discussion with considering the optional conditions ($\phi_a = 1^{eV}$, $V = .0.2^V$, $I = 1.2 \times 10^6 W/m^2$ and $\eta_{opt} = 0.95$), and from the relationships in Table 1, it can be said that to provide the required thermal power of the TIG cathode, the PDC must be capable of producing a thermal power of $1134.8\ kW/m^2$. Fig. 14 shows the number of collectors needed to supply this thermal power for different cities. Note that a zero value for Inchon at 8 a.m. means that the PDC cannot generate thermal power at this hour. The maximum and minimum numbers of collector required are 3888 and 130, respectively, corresponding to Inchon (4 p.m.) and Riyadh (1 p.m.). In addition, on average, the lowest and highest number of collectors needed to supply the thermal power in these cities is 197 collectors for Riyadh and 1229 collectors for Inchon. Note that the arrangement of collectors is not the subject of this study. The main advantage of this scenario is its practicality compared to the former.

## 5. Conclusions

In present research a novel solar driven hybrid system composed of a concentrated solar collector (PDC-type), TID and TD is proposed, in which the TD uses the waste heat of the TIG to generate further power and cooling. The analytical explanations for the power output and efficiency of the TIG, TD and proposed system are investigated. In order to investigate the design parameters affecting proposed hybrid system performance such as solar irradiance density, anode work function, heat conductivity, ratio of resistances and cooled space temperature sensitivity analysis is discussed. Two different scenarios are considered: the former is assumed the values of climatic data constant and impractical but the latter considers the values of climatic data practically for the data of five different cities in Asia. The features and limitations of both scenarios are discussed. The main obtained results of the study are:

- With increasing solar irradiance the TIG power rises initially and reaches a maximum value and then it starts to drop, while the TD power increases faster and faster. Accordingly, the hybrid system total power first increases and then decreases with solar irradiance. Furthermore, the critical point of the solar irradiance corresponding to a maximum power equal to $2.3 \times 10^6\ W/m^2$. So, since the power of the system drops sharply after the critical point, it is necessary to adjust the value close to the critical point.
- TIG and TD are suitable for high-temperature and low-temperature heat source, respectively. But in practice high-temperature energy supplies require substantial preparations.
- As the anode work function increases, the total power and efficiency of the proposed system both drop. In addition, the cooling rate increases with increasing anode work function but the COP decreases.
- For the proposed system, the effect of K is less important, because the TIG waste heat is recovered by the TD and the hybrid system total power increases greatly. In addition, doubling the heat conductivity does not significantly change the total efficiency of the proposed hybrid system and shows an increase of less than 1%.
- Since the proposed hybrid system performance is mainly dependent on that of the TIG, the increase in ratio of resistances does not have a significant effect on the efficiency and power of the proposed system.
- Both total efficiency and power of the proposed system are decreased as cooled space temperature increases. Furthermore, both CR and COP are increased as cooled space temperature increases. But all four of these parameters are very low sensitive to the variation of cooled space temperature.
- PDC has the best optical performance in Riyadh (average daily optical efficiency = 67.5%). In addition, solar collector with the average daily optical efficiency of 63.38% in Beijing has the weakest optical performance among other regions.
- The highest and lowest average useful power produced by a solar collector is related to Riyadh and Inchon, respectively. Furthermore, in terms of thermal efficiency, the best and the weakest PDC performance are related to Riyadh and Incheon, respectively.
- Riyadh has the best performance in comparison to other regions; because Riyadh has the highest intensity of solar irradiance among other cities.
- The first scenario is not practical because of the constant assumption of climatic data. The main advantage of second scenario is its practicality compared to the former.

### CRedit

Behzad ranjbar: Investigation, Methodology, Writing. Mehdi Mehrpooya: Supervision, Conceptualization, Methodology, Investigation, software. Mohammad Marefati: Investigation, Methodology, Writing software.

### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### References

[1] O. Siddiqui, I. Dincer, Analysis and performance assessment of a new solar-based multigeneration system integrated with ammonia fuel cell and solid oxide fuel cell-gas turbine combined cycle, J. Power Sources 370 (2017) 138-154.

[2] O. Ellabban, H. Abu-Rub, F. Blaabjerg, Renewable energy resources: current status, future prospects and their enabling technology, Renew. Sustain. Energy Rev. 39 (2014) 748-764.

[3] M. Marefati, M. Mehrpooya, S.A. Mousavi, Introducing an integrated SOFC, linear Fresnel solar field, Stirling engine and steam turbine combined cooling, heating and power process, Int. J. Hydrogen Energy 44 (57) (2019) 30256-30279.

[4] A. Brown, S. Müller, Z. Dobrotkova, Renewable Energy: Markets and Prospects by Technology, IEA information paper, 2011.

[5] F. Calise, et al., Transient analysis of solar polygeneration systems including seawater desalination: a comparison between linear Fresnel and evacuated solar collectors, Energy 172 (2019) 647-660.

[6] M. Marefati, M. Mehrpooya, M.B. Shafii, Optical and thermal analysis of a parabolic trough solar collector for production of thermal energy in different climates in Iran with comparison between the conventional nanofluids, J. Clean. Prod. 175 (2018) 294-313.

[7] M. Marefati, M. Mehrpooya, M.B. Shafii, A hybrid molten carbonate fuel cell and parabolic trough solar collector, combined heating and power plant with carbon dioxide capturing process, Energy Convers. Manag. 183 (2019) 193-209.

[8] M. Reyes-Belmonte, et al., Optimization of a recompression supercritical carbon dioxide cycle for an innovative central receiver solar power plant, Energy 112 (2016) 17-27.

[9] A.D. Post, B.V. King, E.H. Kisi, Computational model and optimisation of a vacuum diode thermionic generator for application in concentrating solar thermal power, Appl. Therm. Eng. 117 (2017) 245-253.

[10] J. Khan, M.H. Arsalan, Solar power technologies for sustainable electricity generation-A review, Renew. Sustain. Energy Rev. 55 (2016) 414-425.

[11] M. Marefati, M. Mehrpooya, Introducing and investigation of a combined molten carbonate fuel cell, thermoelectric generator, linear fresnel solar reflector and power turbine combined heating and power process, J. Clean. Prod. 240 (2019), 118247.

[12] A. Hafez, et al., Solar parabolic dish Stirling engine system design, simulation, and thermal analysis, Energy Convers. Manag. 126 (2016) 60-75.

[13] L. Yaqi, H. Yaling, W. Weiwei, Optimization of solar-powered Stirling heat engine with finite-time thermodynamics, Renew. Energy 36 (1) (2011) 421-427.

[14] S.A. Kalogirou, Solar Energy Engineering: Processes and Systems, Academic Press, 2013.

[15] P.D. Malali, S.K. Chaturvedi, T. Abdel-Salam, Performance optimization of a regenerative Brayton heat engine coupled with a parabolic dish solar collector, Energy Convers. Manag. 143 (2017) 85-95.

[16] S. Kuravi, et al., Thermal energy storage technologies and systems for concentrating solar power plants, Prog. Energy Combust. Sci. 39 (4) (2013) 285-319.

[17] X. Ju, et al., A review on the development of photovoltaic/concentrated solar power (PV-CSP) hybrid systems, Sol. Energy Mater. Sol. Cell. 161 (2017) 305-327.

[18] V.P. Stefanovic, et al., A detailed parametric analysis of a solar dish collector, Sustain. Energy Technol. Assess. 25 (2018) 99-110.

[19] M.H. Ahmadi, M. Mehrpooya, Thermo-economic modeling and optimization of an irreversible solar-driven heat engine, Energy Convers. Manag. 103 (2015) 616-622.

[20] M.H. Ahmadi, et al., Designing a solar powered Stirling heat engine based on multiple criteria: maximized thermal efficiency and power, Energy Convers. Manag. 75 (2013) 282-291.

[21] M. Moradi, M. Mehrpooya, Optimal design and economic analysis of a hybrid solid oxide fuel cell and parabolic solar dish collector, combined cooling, heating and power (CCHP) system used for a large commercial tower, Energy 130 (2017) 530-543.

[22] G. Gavagnin, et al., Cost analysis of solar thermal power generators based on parabolic dish and micro gas turbine: manufacturing, transportation and installation, Appl. Energy 194 (2017) 108-122.

[23] A. Mohammadi, M. Mehrpooya, Techno-economic analysis of hydrogen production by solid oxide electrolyzer coupled with dish collector, Energy Convers. Manag. 173 (2018) 167-178.

[24] S.Y. Wu, L. Xiao, Y.D. Cao, A review on advances in alkali metal thermal to electric converters (AMTECs), Int. J. Energy Res. 33 (10) (2009) 868-892.

[25] D.K. De, O.C. Olukunle, A theoretical study on solar thermionic (thermoelectronic) power conversion with a parabolic concentrator, in: 2015 International Conference on Energy Economics and Environment (ICEEE), IEEE, 2015.

[26] C. Huang, et al., An efficient hybrid system using a thermionic generator to harvest waste heat from a reforming molten carbonate fuel cell, Energy Convers. Manag. 121 (2016) 186-193.

[27] G. Hatsopoulos, E. Gyphtopoulos, Thermionic Energy Conversion: Theory, Technology and Application, vol. 2, MIT Press, 1979.

[28] M. Lodhi, A. Mustafa, Use of waste heat of TIEC as the power source for AMTEC, J. Power Sources 158 (1) (2006) 740-746.

[29] R. Lamba, S. Kaushik, Energy and exergy analysis of an irreversible thermionic generator, in: IEEE 7th Power India International Conference (PIICON). 2016. IEEE, 2016.

[30] J.-H. Lee, et al., Optimal emitter-collector gap for thermionic energy converters, Appl. Phys. Lett. 100 (17) (2012) 173904.

[31] S. Mishra, M.U. Kahaly, S. Misra, Efficient utilization of multilayer graphene towards thermionic convertors, Int. J. Therm. Sci. 121 (2017) 358-368.

[32] M.S. El-Genk, Y. Momozaki, An experimental investigation of the performance of a thermionic converter with planar molybdenum electrodes for low temperature applications, Energy Convers. Manag. 43 (7) (2002) 911-936.

[33] H. Yuan, et al., Back-gated graphene anode for more efficient thermionic energy converters, Nano Energy 32 (2017) 67-72.

[34] A. Datas, Hybrid thermionic-photovoltaic converter, Appl. Phys. Lett. 108 (14) (2016) 143503.

[35] G. de Almeida, Model and Simulation of the Energy Retrieved by Thermoelectric Generators in an Underwater Glider, Energy conversion and management, 2018.

[36] M. Wu, H. Zhang, T. Liao, Performance assessment of an integrated molten carbonate fuel cell-thermoelectric devices hybrid system for combined power and cooling purposes, Int. J. Hydrogen Energy 42 (51) (2017) 30156-30165.

[37] Y. Wang, et al., Performance evaluation and parametric optimum design of an updated thermionic-thermoelectric generator hybrid system, Energy 90 (2015) 1575-1583.

[38] T. Liao, Z. Yang, B. Lin, Investigation on the optimal performance of the thermionic-thermoelectric hybrid power generation device, SCIENTIA SINICA Physica, Mechanica & Astronomica 44 (2) (2014) 125-133.

[39] S. Su, et al., Material optimum choices and parametric design strategies of a photon-enhanced solar cell hybrid system, Sol. Energy Mater. Sol. Cell. 128 (2014) 112-118.

[40] Z. Ding, L. Chen, F. Sun, Optimum performance analysis of a combined thermionic-thermoelectric refrigerator with external heat transfer, J. Energy Inst. 88 (2) (2015) 169-180.

[41] H. Naito, et al., Development of a solar receiver for a high-efficiency thermionic/thermoelectric conversion system, Sol. Energy 58 (4-6) (1996) 191-195.

[42] A. Bellucci, et al., Preliminary characterization of ST2G: solar thermionic-thermoelectric generator for concentrating systems, in: AIP Conference Proceedings, AIP Publishing LLC, 2015.

[43] G. Xiao, et al., Thermionic energy conversion for concentrating solar power, Appl. Energy 208 (2017) 1318-1342.

[44] S. Hou, H. Zhang, A novel solar assisted vacuum thermionic generator-absorption refrigerator cogeneration system producing electricity and cooling, Energy Convers. Manag. 187 (2019) 83-92.

[45] S.A. Kalogirou, Solar thermal collectors and applications, Prog. Energy Combust. Sci. 30 (3) (2004) 231-295.

[46] S.-Y. Wu, et al., A parabolic dish/AMTEC solar thermal power system and its performance evaluation, Appl. Energy 87 (2) (2010) 452-462.

[47] S.-J. Liang, L. Ang, Electron thermionic emission from graphene and a thermionic energy converter, Phys. Rev. Appl. 3 (1) (2015), 014002.

[48] L. Xiao, S.Y. Wu, S.L. Yang, Parametric study on the thermoelectric conversion performance of a concentrated solar-driven thermionic-thermoelectric hybrid generator, Int. J. Energy Res. 42 (2) (2018) 656-672.

[49] L. Chen, et al., Thermodynamic performance optimization for an irreversible vacuum thermionic generator, European Phys. J. Plus 132 (7) (2017) 293.

[50] M. Marefati, M. Mehrpooya, Introducing a hybrid photovoltaic solar, proton exchange membrane fuel cell and thermoelectric device system, Sustain. Energy Technol. Assess. 36 (2019), 100550.

[51] R. Karimi, T.T. Gheinani, V.M. Avargani, Coupling of a parabolic solar dish collector to finned-tube heat exchangers for hot air production: an experimental and theoretical study, Sol. Energy 187 (2019) 199-211.

[52] I.M. Abdel-Motaleb, S.M. Qadri, Thermoelectric Devices: Principles and Future Trends. arXiv Preprint arXiv:1704.07742, 2017.

[53] Q. Cao, W. Luan, T. Wang, Performance enhancement of heat pipes assisted thermoelectric generator for automobile exhaust heat recovery, Appl. Therm. Eng. 130 (2018) 1472-1479.

[54] S. Wu, H. Zhang, M. Ni, Performance assessment of a hybrid system integrating a molten carbonate fuel cell and a thermoelectric generator, Energy

112 (2016) 520-527.

[55] H. Zhang, et al., Application of cascading thermoelectric generator and cooler for waste heat recovery from solid oxide fuel cells, Energy Convers. Manag. 148 (2017) 1382-1390.

[56] Meteotest, Weather data for every place on Earth [cited April 5, 2019; Available from: https://meteonorm.com/en/, 2000.

[57] Greenstream Publishing, Solar electricity handbook [cited April 5, 2019; Available from: http://www.solarelectricityhandbook.com/, 2019.