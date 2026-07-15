![](./images/817058853458804737_1.jpg)

Applied Thermal Engineering 219 (2023) 119370

Contents lists available at ScienceDirect

Applied Thermal Engineering

journal homepage: www.elsevier.com/locate/apthermeng

![](./images/817058853458804737_2.jpg)

Research Paper
![](./images/817058853458804737_3.jpg)

# A combined solution of thermoelectric coolers and microchannels for multi-chip heat dissipation with precise temperature uniformity control

Bo Cong $^{a,b}$, Yanmei Kong $^{a,*}$, Yuxin Ye $^{a}$, Ruiwen Liu $^{a}$, Xiangbin Du $^{a}$, Lihang Yu $^{a,b}$, Shiqi Jia $^{a,b}$, Zhiguo Qu $^{c,*}$, Binbin Jiao $^{a,*}$

$^{a}$ Institute of Microelectronics of the Chinese Academy of Sciences, Beijing 100029, China
$^{b}$ University of Chinese Academy of Sciences, Beijing 100049, China
$^{c}$ School of Energy and Power Engineering, Xi'an Jiaotong University, Xian 710049, China

## ARTICLE INFO

**Keywords:**
Multi-chip temperature uniformity
Thermoelectric cooler
Thermal test chip
Microchannel heat sink

## ABSTRACT

Effective thermal management with precise temperature uniformity is necessary to improve the performance and stability of multi-chip devices such as active phased array antennas, semiconductor laser radar systems, and light emitting diode (LED) arrays. This study proposes a combined solution for multi-chip devices heat dissipation that integrates thermoelectric coolers (TECs) and microchannel heat sink to tune the temperature of each chip dynamically by controlling multiple TEC currents independently. The equivalent variable thermal resistance of the TEC can be dynamically adjusted under different TEC currents, thereby realizing the equivalent thermal resistance value of TECs change on the heat dissipation path of different chips and the precise temperature control and continuity at desired temperature range. A simplified thermal resistance network of multi-chip is established to illustrate the dynamic control mechanism of multi-chip temperature uniformity based on the variable thermal resistance. Not only the heat dissipation and temperature control of single chip under different operating conditions (TEC current, flow rate, and heat flux), but also the temperature uniformity control of multi-chip is studied. The combined cooling scheme is compared and analyzed with the microchannel cooling. The results show that this combined cooling scheme can achieve precise temperature control of multiple chips with maximum temperature difference less than $0.3\ ^{\circ}\text{C}$ and temperature standard deviation less than $0.07\ ^{\circ}\text{C}$, which is far less than the maximum temperature difference of $7.89\ ^{\circ}\text{C}$ and temperature standard deviation of $3.55\ ^{\circ}\text{C}$ when the heat flux is $50\ \text{W/cm}^2$. This represents a feasible solution for the realization of precise temperature uniformity and dynamic temperature control in multi-chip devices.

## 1. Introduction

The miniaturization and increased integration of multi-chip electronic devices causes high heat flux and temperature nonuniformity [1]. Multi-chip electronic devices that are sensitive to temperature nonuniformity include active phased array antennas, semiconductor laser radar devices, LED arrays. The power amplifier chip in the transmit/receive (T/R) components of active phased array antennas are sensitive to temperature, which affects their gain [2]. Thus, T/R modules require accurate phase control to guarantee the stability of an antenna, and the average temperature of two T/R modules should not exceed $10\ ^{\circ}\text{C}$ [3]. In laser diodes (LDs), the wavelength is affected by temperature and changes at a rate of $0.2\text{--}0.3\ \text{nm/}^{\circ}\text{C}$ [4]. Similarly, if an LED array has a nonuniform temperature distribution, then the luminous flux will be different for each LED [5]. Thus, effective thermal management is required to improve the reliability and efficiency of multi-chip electronic devices.

Microchannel cooling is a promising technique that could satisfy the heat dissipation requirements of high heat flux devices [6]. However, large increases in the temperature of the cooling fluid along the direction of flow can affect the temperature uniformity of multi-chip electronic devices [7]. Constructal-theory networks have the potential to improve the flow uniformity of coolants and the temperature uniformity of multi-chip devices [8]. Various microchannel shapes and configurations have been proposed to improve temperature uniformity in multi-chip devices. For example, H-type bifurcation structure [9], density-

Abbreviations: TEC, Thermoelectric cooler; TTC, Thermal test chip.
* Corresponding authors.
E-mail addresses: kongyanmei@ime.ac.cn (Y. Kong), zgqu@mail.xjtu.edu.cn (Z. Qu), jiaobinb@ime.ac.cn (B. Jiao).

https://doi.org/10.1016/j.applthermaleng.2022.119370
Received 15 June 2022; Received in revised form 12 September 2022; Accepted 20 September 2022
Available online 30 September 2022
1359-4311/© 2022 Elsevier Ltd. All rights reserved.

<table><caption>Table 1 Results of previous studies investigating the effect of microchannel structures on multi-chip heat dissipation and temperature uniformity.</caption>
<thead>
<tr>
<th rowspan="2">Study</th>
<th colspan="2">Research method</th>
<th rowspan="2">Microchannel structure</th>
<th rowspan="2">No. chips</th>
<th rowspan="2">Heat flux (W/cm²)</th>
<th colspan="2">Numerical results (°C)</th>
<th colspan="2">Experimental results (°C)</th>
</tr>
<tr>
<td>Simulation</td>
<td>Experiment</td>
<td>$\Delta T_{max}$</td>
<td>$\sigma_{T}$</td>
<td>$\Delta T_{max}$</td>
<td>$\sigma_{T}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>[9]</td>
<td>√</td>
<td>√</td>
<td>H-type bifurcation</td>
<td>16</td>
<td>500</td>
<td>&lt;1</td>
<td>×</td>
<td>8.8</td>
<td>×</td>
</tr>
<tr>
<td>[10]</td>
<td>√</td>
<td>×</td>
<td>Density-based Topology</td>
<td>36</td>
<td>10</td>
<td>×</td>
<td>0.378</td>
<td>×</td>
<td>×</td>
</tr>
<tr>
<td>[1]</td>
<td>√</td>
<td>√</td>
<td>Fractal tree-like</td>
<td>3</td>
<td>×</td>
<td>1.3</td>
<td>0.75</td>
<td>1.7</td>
<td>0.954</td>
</tr>
<tr>
<td>[11]</td>
<td>×</td>
<td>√</td>
<td>Hierarchical Manifold</td>
<td>9</td>
<td>&lt;75</td>
<td>×</td>
<td>×</td>
<td>&lt;3</td>
<td>×</td>
</tr>
<tr>
<td>[12]</td>
<td>√</td>
<td>√</td>
<td>Leaf vein-shape</td>
<td>32</td>
<td>100</td>
<td>×</td>
<td>1.8</td>
<td>×</td>
<td>2.03</td>
</tr>
<tr>
<td>[13]</td>
<td>√</td>
<td>√</td>
<td>Spider web-like</td>
<td>32</td>
<td>150/100</td>
<td>×</td>
<td>1.81</td>
<td>×</td>
<td>1.58</td>
</tr>
<tr>
<td>[14]</td>
<td>√</td>
<td>×</td>
<td>Staggered fins</td>
<td>25</td>
<td>125</td>
<td>1.8</td>
<td>×</td>
<td>×</td>
<td>×</td>
</tr>
</tbody>
</table>

based topology optimization [10], fractal tree-like structures [1], hierarchical manifolds [11], leaf vein-shaped structures [12], spider web-like structures [13], and staggered fins [14] have been investigated to optimize microchannel designs for multi-chip heat dissipation, and the details are shown in Table 1. The results of these studies show that the temperature uniformity of multi-chip can be improved by optimizing the microchannel structures, but the processing technology deviation, the actual working environment and thermal interface material different will affect the temperature uniformity of multi-chip devices. In addition, the optimization of the microchannel structures is a passive enhancement of the temperature uniformity in multi-chip devices, which cannot realize the dynamic active adjustment of the high precision temperature uniformity in multi-chip devices. Therefore, it is necessary to adopt active control method to improve the temperature uniformity of multi-chip devices.

In order to realize the active control of temperature uniformity of chip, Laguna et al. confirmed that a cooling array with self-adaptive microvalves can proactively improve the temperature uniformity of chip and reduce the pumping power [15]. Li et al. reported the self-adaptive microchannel cooling with the thermal-sensitive nano-composite hydrogel, and the self-adaptive cooling is achieved by intelligently adjusting the coolant through the heat load variation caused by the thermal-sensitive property of the hydrogel [16]. Yan et al. investigated the adaptive cooling of single and multiple hotspots with different embedding positions and numbers of hydrogels in fractal microchannels, which can reduce the temperature of hotspots and improve the temperature uniformity of multiple hotspots [3,17]. Owing to the shape memory effect of shape memory alloy (SMA), the cooling capacity of microchannel heat sink can be matched intelligently without external control [18]. In the previous studies, the dynamic active temperature control of chip is mainly achieved by embedding the structures or materials that can be deformed by temperature in microchannel. Although these methods can achieve active temperature uniformity control of multi-chip, the control capability is effective and the manufacturing process is complex.

Thermoelectric cooler (TEC) is an active cooler that allows heat to dissipate from a surface via the Peltier effect, which can precisely control the temperature of chip by adjusting the current of TEC. The applied current causes charged carriers (electrons or holes) in the material, to diffuse from the cold side to the hot side of TEC [19]. Therefore, the external input current can pump heat away from the cold side to the hot side. It is necessary to adopt an effective heat dissipation scheme to cool the hot side of TEC. Different combined cooling methods were proposed to realize chip cooling and temperature control. Compared with AHS (air-cooled heat sink) + TEC cooling scheme, WMHS (water-cooled microchannel heat sink) + TEC cooling scheme has a better cooling performance by Lin et al, and they found that the hot side of a TEC can be effectively cooled by a water-cooled microchannel in the combined cooling solution using TEC and microchannels [20]. This can improve the cooling capacity of the TEC and the overall cooling performance of the combined system when the hot side is thermally regulated by liquid cooling systems [21–23]. Based on the TEC cooling performance changes with current, the stringent temperature control required by some optoelectronic components can be provided by TEC, so as to stabilize the temperature-dependent wave-lengths in laser beams [24,25]. In the research of chip temperature control by the combined cooling of TEC and microchannels, Hu et al. compared the dynamic performance under different operating conditions, including TEC with and without temperature control and water cooling [26]. They achieved temperature variations of less than 1.5 °C with temperature control and water cooling. Sullivan et al. [27] found that smaller TECs may be better at cooling localized hotspots and mitigating the temperature gradient across a chip. Therefore, the dynamic thermal management of multi-chip device can also be achieved by using a combined cooling scheme of multi-TEC and microchannel, and the multi-TEC can provide the on-demand cooling of each chip. Although the total thermal resistance of the package when the combined cooling scheme of microchannels and TEC is used, the limited cooling capacity and thicker thermoelectric elements (usually greater than 1 mm) of commercial TECs means that it is difficult to achieve high heat flux chip cooling. Therefore, in order to improve the cooling capacity of commercial TEC, a microchannel heat sink with higher heat dissipation capacity can be selected to conduct thermal management on the hot side of the TEC. Advance in the fabrication technique with micro-electromechanical systems (MEMS) technology has made it possible to fabricate micro-scale TEC, and the micro-scale can reduce the thermal and electrical contact resistances. Chowdhury et al. demonstrated the viability of refrigeration technology using superlattice-based thin-film thermoelectric for a hotspot with a high heat flux (1300 W/cm²) [28].

Previous studies have shown that combined cooling solution using TECs and microchannels are an effective cooling and precise temperature control method for a single-chip. However, there are few studies have applied this method to multi-chip devices, where temperature different of multiple chips remain a significant concern. Therefore, based on the potential of TECs to independently reduce hotspots to an acceptable value [29], this study proposes a method of cooling multi-chip devices using a combined cooling system of TECs and microchannels, and explain the dynamic control mechanism of chip temperature in terms of variable thermal resistance. By adjusting the cooling current of each TEC in the combined cooling, the variable thermal resistance value of the corresponding TEC can be adjusted, so as to realize the change of thermal resistance value on different chip cooling paths, and finally achieve the high precision temperature uniformity of multi-chip. So, each TEC will act as an active temperature control device and separately control heat dissipation for one chip with the aim of achieving a uniform temperature distribution across a multi-chip device. A microchannel cold plate will act as a heat sink on the hot side of TECs to improve their cooling capacity. In this paper, thermal test chip (TTC) will be used as thermal simulator chip to evaluate the thermo-hydraulic performance of the combined system at different heat fluxes, TEC currents, and coolant flow rates. Heat dissipation and temperature control are investigated for a single TTC, with the goal of achieving heat dissipation with precise temperature uniformity control for multiple TTCs.

![](./images/817058853458804737_4.jpg)

Fig. 1. (a) Structure of proposed multi-chip combined cooling system with temperature uniformity control based on TECs and microchannels. (b) Simplified thermal resistance network diagram of proposed system with four chips.

## 2. A combined cooling system with temperature uniformity control for a multi-chip test module

This section describes the concept of a combined cooling system with temperature uniformity control for a multi-chip test module for a multi-chip device, and proposes a simplified thermal resistance network, which can be used to understand the required temperature uniformity control mechanisms. A multi-layer test module was used to study the proposed combined cooling system under different experimental conditions, and details of its design, fabrication, and assembly are provided.

### 2.1. Concept and thermal resistance network

A combined cooling scheme of microchannels and TECs for multi-chip device was proposed in this paper. The microchannel structure and liquid separation structure of microchannel heat sink adopt multi-level bifurcation structure to reduce pressure loss and improve the flow uniformity of coolant. The microchannel heat sink effectively dissipates heat from the hot side of the TEC to increase the maximum cooling capacity of the TEC. The current of each TEC is independently controlled to achieve the on-demand cooling of each chip, thereby the total thermal resistance on the cooling path of different chips can be dynamically adjusted to achieve the high precise temperature uniformity of multi-chip.

Fig. 1(a) shows the structure of the combined cooling system with temperature uniformity control for a multi-chip device. Multiple TECs are combined with a microchannel cold plate to achieve combined cooling of a multi-chip device. Each chip is attached to the cold side of a TEC, and the hot side of the TEC is attached to the microchannel cold plate using a thermal interface material (TIM). Each TEC realizes the active control of chip temperature, and the microchannel cold plate realizes heat dissipation of each TEC hot side. The microchannel cold plate contains multiple arrays of microchannel heat sink units, and each heat sink unit includes a bank of high-aspect-ratio microchannels. Coolant is delivered to the microchannels from the fluid inlet, and is discharged from the fluid outlet after passing through the hierarchical multi-level bifurcation system (blue and red regions in Fig. 1(a)). This reduces the drop in pressure and improves the uniformity of the flow by reducing the length of microchannels [11].

Fig. 1(b) shows the thermal resistance network of the proposed model with the combined cooling. The heat of the chip is conducted to the cold side of the TEC through the thermal interface material, and the corresponding interface thermal resistance is $\theta_{a}$. The TECs operate based on the Peltier effect; that is, heat generated by the chip is absorbed by the cold side and emitted by the hot side as current passes through the TEC. Then, the heat on the hot side of TEC is conducted downward to the wall of the microchannels through the thermal interface material (the corresponding interface thermal resistance is $\theta_{b}$), and is absorbed by the cooling medium and flows out from the outlet of microchannel heat sink. The cooling capacity of a TEC depends on the current passing through it, so a TEC can be considered as a variable thermal resistance ($\theta_{thv}$) driven by the equivalent current sources of the cold and hot sides. Based on the Peltier and Seebeck effects, $\theta_{thv}$ can be used to convert electric power to heat, thus promoting or hindering heat transfer [30]. TECs are a type of heat engine driven by an external input current [31], so $\theta_{thv}$ is not strictly a thermal resistance, but can be considered as a peculiar thermal resistance with a negative value [32]. The different chips correspond to the different heat dissipation paths in the thermal resistance network. Each TEC cools one chip separately, and the equivalent thermal resistance of the corresponding TEC can be changed by changing the current of TEC, thereby realizing the heat dissipation with precise temperature uniformity control for multi-chip.

In the thermal resistance network, the theoretical equations for the TECs are [33]:

$$Q_{c}=SI_{tec}T_{c}-\frac{1}{2}I_{tec}R^{2}-k_{tec}(T_{h}-T_{c})\tag{1}$$

$$Q_{h}=SI_{tec}T_{h}+\frac{1}{2}I_{tec}R^{2}-k_{tec}(T_{h}-T_{c})\tag{2}$$

$$P_{tec}=Q_{h}-Q_{c}=SI_{tec}(T_{h}-T_{c})+I_{tec}^{2}R\tag{3}$$

The Seebeck coefficient ($S$), thermal conductivity ($k_{tec}$), and electrical resistance ($R$) are physical characteristics of the TECs, and $I_{tec}$ and $P_{tec}$ are the current passing through TEC and the power consumed by the TEC, respectively. In addition, $T_{h}$ and $T_{c}$ are the temperature of the hot and cold side of the TEC, respectively.

According to the temperature node analysis of TEC cold side by energy conservation, Eq. (4) can be obtained [34].

$$\frac{T_{c}-T_{h}}{\theta_{th}}-\frac{1}{2}I_{tec}^{2}R+SI_{tec}T_{c}=\frac{T_{c}-T_{h}}{\theta_{thv}}\tag{4}$$

Here, $\theta_{th}$ is the basic thermal resistance of TEC.

The temperature of TEC cold side can be expressed as:

$$T_{c}=T_{j}-\theta_{a}Q\tag{5}$$

where $T_{j}$ is the junction temperature of chip.

Combining Eqs. (3), (4) and (5), the variable thermal resistance of TEC can be expressed as:

$$\theta_{thv}=\frac{(P_{tec}/I_{tec}^{2}-R)\theta_{th}}{(P_{tec}-R)+[0.5SI_{tec}R-S^{2}(T_{j}-\theta_{a}Q)]\theta_{th}}\tag{6}$$

For a given TEC, the variable thermal resistance will vary with $P_{tec}$, $I_{tec}$ and $T_{j}$.

In addition, the total thermal resistance ($\theta_{0}$) of the microchannel heat sink can be expressed by the following equation:

$$\theta_{0}=\frac{Q_{h1}+Q_{h2}+\cdots+Q_{hi}+\cdots+Q_{hn}}{T_{ch}-T_{in}}\tag{7}$$

where $Q_{hi}$ is the heat rejected from the hot side of TEC$_{i}$.


![](./images/817058853458804737_5.jpg)

Fig. 2. (a) Three-dimensional diagram showing structure of combined cooling system. (b) Coolant flow path. (c) Coolant flow in a single microchannel array unit. (d) Microchannel cold plate.

As shown in Fig. 1, heat flux of multi-chip is parallel connection in the microchannel heat sink. The assumption is that heat from different chips will flow along the microchannel cold plate and is absorbed by coolant, until heat flux converges to a region internal to heat sink, with a characteristic temperature $(T_{ch})$ [35]. In the TECs and microchannels combined cooling system, the multi-chip temperature is determined by self-heating effect and thermal coupling effect. The thermal coupling between different chips can be calculated by thermal resistance matrix. The thermal resistance matrix model is based on the principle of linear superposition, and the temperature rise of chip $i$ is obtained by superposition the temperature rise for chip $i$ when each chip acts alone. The thermal resistance matrix with n chips $[\theta_{j,in}]^{n,n}$ and the temperature of n chips $[T_{j}]^{n}$ can be expressed as the following equations [35,36].

$$
\theta_{i k}=\frac{T_{i k}-T_{i n}}{Q_{h k}} \tag{8}
$$

$$
\left[\theta_{j, i n}\right]^{n, n}=\left(\begin{array}{ccccc}
\theta_{11} & \theta_{12} & \theta_{13} & \cdots & \theta_{n 1} \\
\theta_{21} & \theta_{22} & \theta_{23} & \cdots & \theta_{n 2} \\
\theta_{31} & \theta_{32} & \theta_{33} & \cdots & \theta_{n 3} \\
\vdots & \vdots & \vdots & \theta_{i k} & \vdots \\
\theta_{n 1} & \theta_{n 2} & \theta_{n 3} & \cdots & \theta_{n n}
\end{array}\right) \tag{9}
$$

$$
\left[T_{j}\right]^{n}=\left(\begin{array}{c}
T_{j 1} \\
T_{j 2} \\
T_{j 3} \\
\vdots \\
T_{j 4}
\end{array}\right)=\left[\theta_{j, i n}\right]^{n, n} *\left(\begin{array}{c}
Q_{h 1} \\
Q_{h 2} \\
Q_{h 3} \\
\vdots \\
Q_{h n}
\end{array}\right)+T_{i n} \tag{10}
$$

where $\theta_{i k}(k=i)$ is the total thermal resistance along the heat transfer path of chip $i$ when there isn't thermal coupling effect, $\theta_{i k}(k \neq i)$ represents as the coupling thermal resistance from the chip k to i. Therefore, the temperature of chip $i$ can be calculated by Eq. (11).

$$
T_{j i}=\theta_{i 1} Q_{h 1}+\theta_{i 2} Q_{h 2}+\cdots+\theta_{i i} Q_{h i}+\cdots+\theta_{i n} Q_{h n} \tag{11}
$$

where $\theta_{i i}$ can be calculated by Eq. (12).

$$
\theta_{i i}=\theta_{a i}+\theta_{t h v, i}+\theta_{b i}+\frac{T_{c h}-T_{i n}}{Q_{h i}} \tag{12}
$$

The temperature uniformity of multi-chip devices can be affected by many factors, such as thermal interface material differences, thermal coupling effect, and machining deviations. In Eq. (6), the variable thermal resistance will vary with $P_{tec}, I_{tec}$ and $T_{j}$ for a given TEC type. Therefore, the value of $\theta_{t h v}$ is dynamically adjusted by independently controlling the corresponding TEC current to change $P_{tec}, T_{c}, T_{h}, Q_{c}$ and $Q_{h}$, so the thermal resistance of a chip can be adjusted independently to achieve precise temperature uniformity across a multi-chip device in the combined cooling.

### 2.2. Design, fabrication, and assembly of the test module

The design of a combined cooling structure based on TECs and microchannel cold plate is shown in Fig. 2(a); in includes a chip layer, TEC layer, microchannel cold plate layer, slot plate layer, and coolant distributor layer. Fig. 2(b) shows the coolant flow path in the coolant distributor, slot plate, and microchannel cold plate layer. The chip in this study was a $1 \times 1 \times 0.4 \mathrm{~mm}^{3}(\mathrm{~L} \times \mathrm{W} \times \mathrm{H})$ TTC, which can characterize the thermal behavior of power devices [37]. The TTC, with integrated silicon resistor strips and temperature-sensitive diode (TSD), was manufactured using a standard complementary metal--oxidesemiconductor (CMOS) process, with the TSD located at the center of device. The commercially available commercial TECs selected for this study were type TES1-00708, which contain seven pairs of $\mathrm{P}-\mathrm{N}$ semiconductor columns, and have an overall size of $5 \times 5 \times 3 \mathrm{~mm}^{3}(\mathrm{~L} \times$ W $\times$ H). The microchannel cold plate (Fig. 2(d)) was deep reactive ion etched (DRIE) into $500 \mu \mathrm{m}$-thick silicon via the Bosch process, and the microchannels were $50 \mu \mathrm{m}$ wide and $350 \mu \mathrm{m}$ deep. The 5 mm-thick slot plate and 8 mm-thick coolant distributor layer were made by processing polymethyl methacrylate (PMMA) sheets.

To assemble the multi-layer structure, thermal grease (GK-920) with a thermal conductivity $(k_{l})$ of $2 \mathrm{~W} / \mathrm{m}-\mathrm{k}$ was used to bond $\mathrm{TTC}_{i}$ to the center of the cold side of $\mathrm{TEC}_{i}$, and the hot side of $\mathrm{TEC}_{i}$ to the top of the microchannel array unit (where $i$ denotes the $i^{th}$ component). Lasermachined graphic polyimide film double-sided adhesive (Kapton) 100 $\mu \mathrm{m}$ thick was used to seal the bond between the coolant distributor and the slot plate, and the slot plate and the microchannel cold plate. In addition, a 3 mm-thick TEC fixture was used to match the bonding positions and fix the TECs, and a 0.5 mm-thick printed circuit board (PCB) was used to match the bond attaching positions of the TTCs and provide

![](./images/817058853458804737_6.jpg)

Fig. 3. (a) Microscope image showing the structure of the $1 \times 1 \times 0.4\ \text{mm}^3$ TTC. (b) Structure of $\text{TTC}_i$-on-$\text{TEC}_i$ assembly. (c) Test module after multi-layer assembly. (d) Location and distribution of TTCs.

![](./images/817058853458804737_7.jpg)

Fig. 4. (a) Schematic diagram of the experimental flow loop. (b) experimental photo of the flow loop.

an electrical connection to the heating resistors and TSDs in the TTCs.
The assembled test module is shown in Fig. 3(c).

### 3. Experimental details

The experimental test platform was built to characterize the heat dissipation and temperature uniformity control ability of the test module. The uncertainty of the experimental instruments was recorded to evaluate possible causes of deviation in the experimental data. According to the study of Lin et al., the current of TEC is most important effect of the factors on the cooling performance compared with the flow rate of coolant, inlet temperature of coolant, ambient temperature [20]. Therefore, this study mainly investigates the chip temperature change, thermal resistance change, and temperature control ability from the perspective of TEC current, and discusses the feasibility of controlling the temperature uniformity of multi-chip devices.

### 3.1. Experimental setup

An open fluid loop (Fig. 4) was constructed to evaluate the temperature of the TTCs, and the cooling and pumping power of the combined cooling system. The TTC temperature $T_{ttc}$ was measured by using a 64-bit standard temperature signal acquisition module, and the TECs were driven by direct current (DC) power (RIGOL DP832). Deionized water was used as the coolant, and an infusion pump (Y-600, XYHY) transported it from a large volume reservoir to the liquid inlet of the test module. The temperature of the coolant at the inlet was $23\ ^\circ\text{C}$. T-type thermocouples were used to measure the temperature of the coolant at the inlet and outlet of the test module, and a differential manometer (DPG409-050DWU, OMEGA) was used to measure the change in pressure.

### 3.2. Data reduction

The collected data included TTC temperature, TEC current, DC power, and pressure drop, and they were monitored until a steady value

<table><caption>Table 2 The datasheet parameters and calculation parameters of TES1-00708.</caption><thead><tr><th>Parameters</th><th>Value</th></tr></thead><tbody><tr><td>Dimension (mm)</td><td>$5 × 5 × 3$</td></tr><tr><td>$T_{h0}$ (K)</td><td>303.13</td></tr><tr><td>$\Delta T_{max}$ (K)</td><td>63</td></tr><tr><td>$I_{max}$ (A)</td><td>0.8</td></tr><tr><td>$V_{max}$ (V)</td><td>0.82</td></tr><tr><td>$Q_{c,max}$ (W)</td><td>0.38</td></tr><tr><td>$\theta_{th}$ (K/W)</td><td>102 ($I_{tec}=0$ A)</td></tr><tr><td>S (V/K)</td><td>0.0027</td></tr><tr><td>R ($\Omega$)</td><td>1.035</td></tr></tbody></table>

<table><caption>Table 3 Uncertainty and working range of experimental instruments.</caption><thead><tr><th>Parameter</th><th>Instrument</th><th>Range</th><th>Uncertainty</th></tr></thead><tbody><tr><td>Coolant temperature ($^\circ$C)</td><td>Thermocouple</td><td>$-50$–200</td><td>$\pm 1^\circ$C</td></tr><tr><td>Pressure drop (kPa)</td><td>Differential manometer</td><td>0–350</td><td>$\pm 0.1$ %</td></tr><tr><td>Volumetric flow rate (ml/min)</td><td>Infusion pump</td><td>0–1000</td><td>$\pm 0.5$ %</td></tr><tr><td>Power (W)</td><td>Power supply</td><td>0–195</td><td>0.05 % +20 mV<br>0.2 % +5 mA</td></tr></tbody></table>

was achieved. The TTC temperature was controlled and kept below $125^\circ$C based on the maximum permitted temperature of silicon-based devices [38,39]. The TTC temperature was obtained by monitoring the calibrated TSD output voltage.

The parameters in datasheet provided by manufacturers of TECs are mainly include $\Delta T_{max}$, $I_{max}$, $V_{max}$ and $Q_{max}$, among which $\Delta T_{max}$ is the maximum temperature difference between the hot and cold side at a given hot side temperature $T_{h0}$ and $Q_{c}$ is 0, $I_{max}$ and $V_{max}$ are the input current and voltage at $\Delta T=\Delta T_{max}$, and $Q_{c,max}$ is the maximum amount of heat that can be absorbed at cold side at $I=I_{max}$ and $\Delta T=0$. Table 2 shows the parameters of the TES1-00708. The following equations can be used to calculated the physical characteristics of TEC from datasheet [40].

$$
S=\frac{V_{\max }}{T_{h 0}} \tag{13}
$$

$$
R=\frac{\left(T_{h 0}-\Delta T_{\max }\right) V_{\max }}{T_{h 0} I_{\max }} \tag{14}
$$

The Q applied to each TTC was obtained by multiplying the TTC current $I_{ttc}$ by the voltage at each end $V_{ttc}$; that is,

$$
Q=I_{t t c} V_{t t c} \tag{15}
$$

$$
q=\frac{Q}{A_{t}} \tag{16}
$$

where $A_{t}$ is the surface area of each TTC ($1 × 1$ mm$^2$).

To evaluate the temperature uniformity of multiple TTCs, the standard deviation of the temperature ($\sigma_{t}$) of multiple TTCs is calculated using the equation:

$$
\sigma_{t}=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(T_{i}-\bar{T}\right)^{2}} \tag{17}
$$

Here, $T_{i}$ is the temperature of $\text{TTC}_{i}$ and $\bar{T}$ is the average temperature of multiple TTCs.

The thermal resistance ($\theta_{a}$ and $\theta_{b}$) of the thermal interface layer can be calculated by Eq. (18). The thickness of the interface layer is about 0.1 mm ($d_{i}$).

<table><caption>Table 4 Values of $\Delta T_{max}$ and $\sigma_{T}$ for the four TECs under different cases of cooling.</caption><thead><tr><th></th><th>Case 1</th><th>Case 2</th><th>Case 3</th><th>Case 4</th></tr></thead><tbody><tr><td>$\Delta T_{max}$ ($^\circ$C)</td><td>7.89</td><td>11.22</td><td>9.09</td><td>0.15</td></tr><tr><td>$\sigma_{t}$ ($^\circ$C)</td><td>3.55</td><td>4.84</td><td>3.96</td><td>0.07</td></tr></tbody></table>

$$
\theta=\frac{1}{k_{i}} \frac{d_{i}}{A} \tag{18}
$$

### 3.3. Uncertainty

The measurement uncertainty and working range of each instrument is listed in Table 3. The uncertainties were obtained from the manufacturers' specifications, except for the TSDs. Before testing, the TTCs were placed in an oven (ESPEC, SH-242) and multi-point temperature calibration was used to improve the accuracy of the output voltage signal of the TSDs. The temperature accuracy of the TTCs was $\pm 0.1$ K, which was conservatively estimated by considering the accuracy of the oven and the fluctuation in the output signal of the calibrated TSDs. In this paper, the temperature of the TTCs was above 286 K, so the uncertainty in the TTC temperature was less than 0.07 % (($|0.1$ K$| + |-0.1$ K$|$) / (286 K) $× 100$ %) [41]. According to the uncertainty analysis method by Moffat [42], the uncertainty of $q$ can be calculated by the following formula, and the uncertainty of $q$ is about $\pm 0.21$ %.

$$
\frac{\delta q}{q}=\sqrt{\left(\frac{\delta V_{t t c}}{V_{t t c}}\right)^{2}+\left(\frac{\delta I_{t t c}}{I_{t t c}}\right)^{2}} \tag{19}
$$

## 4. Results and discussion

First, the heat dissipation and temperature control performance of the proposed combined cooling system were investigated using a single TTC ($\text{TTC}_{1}$). Then, the potential thermal coupling of a multi-chip device was investigated using multiple TTCs ($\text{TTC}_{1}$, $\text{TTC}_{2}$, $\text{TTC}_{3}$, and $\text{TTC}_{4}$). Finally, combined cooling with temperature uniformity control for multiple TTCs was studied. The location distribution of TTCs is shown in the Fig. 3(d) (see Table 4).

### 4.1. Combined cooling with temperature control for a single thermal test chip

As shown in Fig. 5(a), the $\text{TTC}_{1}$ temperature $T_{ttc1}$, $f$, and $\text{TEC}_{1}$ current $I_{tec1}$ are measured and analyzed. The temperature is mainly affected by the TEC current, and is less affected by the flow rate. This is because the TEC and thermal interface materials have high thermal resistances and the microchannel cooling is indirect cooling, so increasing flow rate doesn't significantly reduce the TTC temperature. At a constant $I_{tec1}$, $T_{ttc1}$ hardly change when $f$ exceeds 160 ml/min, which indicates that the heat from hot side of $\text{TEC}_{1}$ is efficiently transferred to the microchannel heat sink. Therefore, the flow rate of coolant is fixed at 160 ml/min in the subsequent analysis. $T_{ttc1}$ decreases as $I_{tec1}$ increased, but $T_{ttc1}$ at $I_{tec1}=1.2$ A is higher than that at $I_{tec1}=0.9$ A. The TEC operates on the basis of the Peltier effect by dumping heat from the hot side to the cold side when the applied current flows through it [43]. There is also Joule heating occurs within the TEC, and it directly proportional to the square value of the applied current passing through it, so the Joule heating exceeds the Peltier cooling at $I_{tec1}=1.2$ A. Thus, the optimum TEC cooling current $I_{opt}$ occurs between 0.9 and 1.2 A at 50 W/cm$^2$, and the optimal cooling current corresponds to the maximum cooling capacity of TEC in the combined cooling.

From Fig. 5(b), it is clear that the optimum cooling current for $\text{TEC}_{1}$ is approximately 1.1 A, and the corresponding minimum $\text{TTC}_{1}$ temperature is $43.15^\circ$C. When $I_{tec1}$ is greater than 1.1 A, the $\text{TTC}_{1}$ temperature increases as $I_{tec1}$ increased. The Peltier effect is not obvious when $I_{tec1}=$

![](./images/817058853458804737_8.jpg)

![](./images/817058853458804737_9.jpg)

![](./images/817058853458804737_10.jpg)

![](./images/817058853458804737_11.jpg)

Fig. 5. Combined cooling for TTC₁ at 50 W/cm². (a) TTC₁ temperature against flow rate at different TEC₁ currents. (b) TTC₁ temperature and TEC₁ power against TEC₁ current. (c) TTC₁ temperature change and temperature management efficiency against TEC₁ current. (d) The variable thermal resistance against TEC₁ current.

0.1 A, the TTC₁ temperature decreases slightly because the TEC₁ power $P_{tec1}$ is close to 0 W (TTC₁ heat load is 0.5 W). Fig. 5(c) shows that the temperature change $\Delta T_d$ and management gains $\eta_t$ varies with the current at 160 ml/min. The TEC temperature management gains is defined as the ratio of $\Delta T_d$ to $P_{tec}$ at the corresponding $I_{tec}$. The $\eta_t$ decreases as $I_{tec}$ increases, and the $\Delta T_d$ by a maximum of 36.64 °C at $I_{tec1}=1.1$ compared with the temperature at $I_{tec1}=0$ A. The TEC has higher $\eta_t$ when $I_{tec1}$ is low because the Joule heating is small. This indicates that the low applied current can reduce the effect of Joule heating and save the cooling power consumption. Fig. 5(d) shows the variation trend of $\theta_{thv}$ with TEC current, and the calculation formula is shown in Eq. (6). In this experiment, limited by the lower heat dissipation capability of TES1-00708 and the thicker thermoelectric element (about 2 mm), TEC has a larger thermal resistance. Owing to the higher thermal resistance of TEC compared with other thermal resistance (interface thermal resistance, microchannel heat sink thermal resistance), the temperature of TTC will change significantly at different $I_{tec}$. $\theta_{thv}$ decreases significantly when the $I_{tec}$ is small, which is due to the change of the internal heat transfer mechanism of the TEC after passing current. $\theta_{thv}$ slowly rises after reaching the minimum value (56.66 K/W) at $I_{tec1}=1$ A, since the Joule heat term is a power function, the proportion of Joule heat term in the heat exchange increases as the current increases. The difference between the experimental results and the calculated results is due to the

![](./images/817058853458804737_12.jpg)

Fig. 6. TTC₁ temperature against heat flux for different TEC₁ currents at a flow rate of 160 ml/min.

![](./images/817058853458804737_13.jpg)
![](./images/817058853458804737_14.jpg)

Fig. 7. Optimum TEC₁ cooling capacity with combined cooling at different heat fluxes. (a) Optimum TEC₁ cooling current and cooling power. (b) TTC₁ temperature at $I_{tec1}=0$ A and $I_{tec1}=I_{opt}$.

TEC module parameters ($S$, $R$ and $\theta_a$) are taken as constants. Actually, $S$ and $R$ depend on the temperature, and the thermal interface material may have small bubbles and the thickness is more or less deviated from 0.1 mm. In theory, $\theta_{thv}$ can be negative at low heat load. Based on the change of TEC equivalent thermal resistance, the chip temperature can be precisely regulated under different heat load. Therefore, the high precise temperature uniformity of multi-chip can be achieved by regulating the equivalent thermal resistance of TEC at different $I_{tec}$.

#### 4.1.1. Performance analysis at different heat fluxes

$T_{ttc1}$ against heat flux at different $I_{tec1}$ and a flow rate of 160 ml/min is shown in Fig. 6. The relationship between temperature and heat flux is approximately linear under the different $I_{tec1}$. The linear relation can be beneficial to predict the temperature of chip under different heat flux, which can prevent the chip temperature from being too high and help to select the appropriate TEC current. In order to further study the relationship between chip temperature and heat flux when $I_{tec}$ is low. The temperature curve for a TEC₁ current of 0.1 A approaches the temperature curve for a TEC₁ current of 0 A because the heat absorbed by the cold side is much less than heat load at high heat flux.

Fig. 7(a) shows the optimum TEC₁ cooling current and corresponding optimum cooling power ($P_{opt}$) under different heat fluxes at a flow rate of 160 ml/min. The optimum TEC₁ cooling current and cooling power gradually increase as the heat flux increases, which may be because the temperature difference between the hot and cold sides of TEC₁ is greater when the heat flux is higher. Fig. 7(b) shows $T_{ttc1}$ at a flow rate of 160 ml/min when $I_{tec1}$ is 0 A and $I_{opt}$. As the heat flux increases, $\Delta T_d$ gradually increases because the TEC₁ optimum cooling power increases. The combined cooling system reduces $T_{ttc1}$ by 39.86 °C at a heat flux of $70\ \text{W/cm}^2$ when $I_{tec1}$ is $I_{opt}$. Therefore, the temperature uniformity of multi-chip can be achieved by independently controlling different TEC currents in the combined cooling system, even if there are large temperature difference among multi-chip.

### 4.2. Combined cooling with temperature control for multiple thermal test chips

TECs can achieve independent temperature control for each TTC in

![](./images/817058853458804737_15.jpg)
![](./images/817058853458804737_16.jpg)

Fig. 8. Temperature and thermal resistance distribution of four TTCs at a flow rate of 160 ml/min when the heat flux at TTC₁ is varied. (a) Temperature distribution of four TTCs. (b) Thermal resistance distribution of four TTCs.

![](./images/817058853458804737_17.jpg)
![](./images/817058853458804737_18.jpg)

Fig. 9. Combined cooling with temperature uniformity control for two TTCs at a flow rate of 160 ml/min. (a) Temperature and power distributions for TTC₁ (60 W/
cm²) and TTC₃ (40 W/cm²). (b) Temperature uniformity control for TTC₁ (60 W/cm²) and TTC₃ (40 W/cm²). (c) Temperature and power distribution for TTC₁ (55
W/cm²) and TTC₃ (40 W/cm²). (d) Temperature uniformity control for TTC₁ (55 W/cm²) and TTC₃ (40 W/cm²).

the combined cooling system so, owing to the structural symmetry of the test module, two and four TTCs are used to study cooling with temperature control uniformity.

### 4.2.1. Thermal coupling for multiple thermal test chips
There may be thermal coupling between chips in multi-chip devices, which will affect the independent temperature control for each chip. In this paper, TTC₁, TTC₂, TTC₃, and TTC₄ are selected to analyze thermal coupling in the test module. Fig. 8(a) shows the temperature curves of the four TTCs when a heat flux of 0–80 W/cm² is applied to TTC₁ alone, and all the TECs are turned off. The results show that thermal coupling is related to the distance between the TTCs. The TTC₂ temperature is affected by heat conduction from TTC₁, and the TTC₂ temperature increases by 3.8 °C when there is a heat flux of 80 W/cm² at TTC₁. The different positions of multi-chip have different heat dissipation paths, and the thermal coupling of adjacent chips may affect the temperature uniformity of multi-chip devices. The corresponding thermal resistance matrix is shown in Eq. (20) when the power is applied only to TTC₁, and the thermal resistance $\theta_{21}$, $\theta_{31}$, and $\theta_{41}$ represents as the coupling thermal resistance from the TTC₁ to TTC₂, TTC₃, and TTC₄, respectively. The thermal resistance can be calculated by Eq. (8). Obviously, the coupling thermal resistance is much less than the total thermal resistance of TTC₁ from Fig. 8(b), which is due to the high base thermal resistance of TEC. Therefore, the influence of thermal coupling on the temperature uniformity control of multi-chip devices can be ignored.

$$
\left[\theta_{j, i n}\right]^{4,4}=\left(\begin{array}{cccc}
\theta_{11} & 0 & 0 & 0 \\
\theta_{21} & 0 & 0 & 0 \\
\theta_{31} & 0 & 0 & 0 \\
\theta_{41} & 0 & 0 & 0
\end{array}\right) \tag{20}
$$

### 4.2.2. Combined cooling with temperature uniformity control for two thermal test chips
Owing to their very small thermal coupling, TTC₁ and TTC₃ are selected to investigate the combined cooling system with temperature uniformity control for two TTCs. The current of TEC₁ and TEC₃ is regulated independently at a constant flow rate (160 ml/min) in the combined cooling system, thereby the temperature of TTC₁ and TTC₃ is controlled independently.

Fig. 9(a) shows the $T_{ttc1}$ and $T_{ttc3}$ at heat fluxes of 60 and 40 W/cm², respectively, and $P_{tec1}$ and $P_{tec3}$ at different $I_{tec}$. $P_{tec1}$ and $P_{tec3}$ are slightly different at the same current, which may be due to deviation in the TIM and TEC characteristic parameters. Temperature uniformity across TTC₁ and TTC₃ is achieved by increasing $I_{tec1}$ to decrease $T_{ttc1}$, which can reduce the equivalent thermal resistance of TEC₁. As shown in Fig. 9(b),

![](./images/817058853458804737_19.jpg)

![](./images/817058853458804737_20.jpg)

![](./images/817058853458804737_21.jpg)

![](./images/817058853458804737_22.jpg)

Fig. 10. Temperature of four TTCs against heat flux under (a) case 1 and (b) case 2 cooling. (c) Temperature standard deviation curves for TTCs in (a) and (b). (d) Temperature of four TTCs under different types of cooling. Case 1, microchannel cooling (without TECs); case 2, combined cooling ($I_{tec}=0$ A, the four TECs are switched off); case 3, combined cooling ($I_{tec}=I_{opt}$, the four TECs are working at optimum cooling currents); and case 4, combined cooling ($I_{tec3}=I_{opt}$, the other three TECs are working) with temperature uniformity control. The four TECs are TEC₁, TEC₂, TEC₃, and TEC₄.

the difference in temperature between TTC₁ and TTC₃ is kept below 0.3 °C by adjusting the TEC₁ current. Precise temperature uniformity ($\Delta T_{max}<0.3$ °C) across TTC₁ and TTC₃ is achieved by adjusting $I_{tec1}$ when the $T_{ttc1}$ exceeds 55.14 °C, because $T_{ttc1}$ is 55.14 °C when TEC₁ reaches the optimum cooling capacity.

As shown in Fig. 9(c), compared with Fig. 9(a), the difference in temperature between TTC₁ and TTC₃ reduces because the heat flux of TTC₁ is decreased to 55 W/cm². Fig. 9(d) shows that increasing $I_{tec1}$ can bring the temperature difference between TTC₁ and TTC₃ to 0.3 °C when $T_{ttc3}$ exceeds 49.98 °C. Therefore, the TEC optimum cooling capacity of the combined system will limit the adjustable range of temperature uniformity control, and the adjustable range of temperature uniformity control is smaller when the difference in the heat flux across a multi-chip device is bigger. Furthermore, the combined cooling system can achieve a maximum temperature difference within 0.3 °C when there are more chips.

### 4.3. Comparative analysis of combined cooling and microchannel cooling for four thermal test chips

In order to further analyze and compare the effects of combined cooling and microchannel cooling on multi-chip heat dissipation and temperature uniformity. Four types of cooling are considered in this experiment: case 1, microchannel cooling (Four TTCs are bonded to the microchannel cold plate by the thermal interface material and without TECs); case 2, combined cooling ($I_{tec}=0$ A, the four TECs are switched off); case 3, combined cooling ($I_{tec}=I_{opt}$, the four TECs are working at optimum cooling currents); and case 4, combined cooling ($I_{tec3}=I_{opt}$, the other three TECs are working) with temperature uniformity control.

Fig. 10(a) shows the temperature curves for four TTCs with case 1 cooling. The temperature across the four TTCs became less uniform as the heat flux increases. The maximum temperature difference is 31.25 °C at 150 W/cm², which may be attributed to the effects of flow maldistribution and the thermal interface materials. As shown in Fig. 10(b), the maximum temperature difference between the four TTCs with

case 2 cooling gradually increases as the heat flux increases, from
3.62 °C at 20 W/cm² to 13.07 °C at 80 W/cm². Due to the high thermal
resistance of the TEC and the effect of the two-layer interface materials,
the temperature of TTC₃ exceeds 125 °C when the heat flux is 80 W/cm².
Fig. 10(c) shows the temperature standard deviation curves, $\sigma_{t,1}$ and $\sigma_{t,2}$,
for the TTCs shown in Fig. 10(a) and (b), respectively. When the heat
flux exceeds 50 W/cm², the small variations in $\sigma_{t,2}$ may be attributed to
the lower heat dissipation capacity resulting from the longer heat
dissipation path and the greater thermal resistance in combined cooling
system.

Fig. 10(d) shows the temperatures of the four TTCs with each type of
cooling when the heat flux is 50 W/cm². $T_{ttc3}$ as the adjustment target
temperature of other TTCs. After modulating the three remaining TEC
currents in case 4, the maximum temperature difference and tempera-
ture standard deviation of the four TTCs are 0.15 °C and 0.07 °C,
respectively. The small cooling capacity of the commercial TECs meant
that, at a heat flux of 50 W/cm², combined cooling does not significantly
improve the performance compared to microchannel cooling alone.
However, precise temperature uniformity control can be achieved for
multi-chip devices using a combined cooling system to regulate the
equivalent thermal resistance of different chip heat dissipation paths.
The details of the maximum temperature difference and temperature
standard deviation for the four TTCs under the different cases of cooling
are shown in Table 3, and the corresponding heat flux is 50 W/cm².
Compared with the data in Table 1 of improving the temperature uni-
formity of multi-chip by using the optimized microchannel structure, the
combined cooling based on TECs and microchannels has higher tem-
perature uniformity, simple operation method and high control
precision.

## 5. Conclusions

In this work, a combined cooling solution based on TECs and a
microchannel heat sink was proposed for multi-chip heat dissipation. A
test module was assembled and tested to investigate the effectiveness of
the proposed system at different TEC currents and heat fluxes. By
adjusting each TEC current independently, the cooling capacity of the
TEC and the thermal resistance of each heat dissipation path along the
multi-layer structure could be modulated, realizing independent and
active temperature control for a multi-chip device. The conclusions can
be summarized as follows:

(1) The TEC current can achieve a large change of the TEC equivalent
thermal resistance. So, the TEC current is dominant in reducing
and maintaining the chip temperature compared with the flow
rate of the coolant.

(2) Combined cooling system can realize efficient thermal manage-
ment of chip. For example, at a heat flux of 50 W/cm², the TTC₁
temperature dropped by 36.64 °C when the combined cooling
reached its maximum cooling capacity, compared to the case
where TEC₁ was not working. This can provide a wide range of
temperature adjustment for multi-chip temperature uniformity.

(3) In combined cooling system, the heat dissipation with precision
temperature control of each chip is achieved by adjusting the
corresponding TEC current. Experimental results show that the
maximum temperature difference of multi-chip is less than
0.3 °C.

So, the multi-chip temperature uniformity control combined solution
based on TEC currents has high flexibility, which can compensate the
influence of processing technology deviation, interface material differ-
ence and external environment on the temperature uniformity of multi-
chip. And future studies will aim to realize automatic temperature
uniformity control for a greater number of chips using a proportional
integral derivative (PID) controller, and high heat flux multi-chip heat
dissipation with temperature uniformity control via combined cooling of
superlattice-based thin-film TECs integrated with microchannels.

## Declaration of Competing Interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgements

This work was supported by the National Key R&D Program of China
(grant number 2020YFB2008900). We also thank Suzhou Rich Sensor
Science & Technology Co., Ltd for providing the thermal test chip and
technical support.

## References

[1] X. Luo, Z. Mao, Thermal modeling and design for microchannel cold plate with
high temperature uniformity subjected to multiple heat sources, Int. Commun. in
Heat Mass 39 (6) (2012) 781–785. <https://doi.org/10.1016/j.
icheatmasstransfer.2012.05.007>.

[2] J. Ge, D. Jin, Z. Qian, Research on heat dissipation technology of the high-power
array antenna, in: Proceedings of the Seventh Asia International Symposium on
Mechatronics, 2019, pp. 400–412, https://doi.org/10.1007/978-981-39-9441-7_
52.

[3] L. Wang, Z. Wang, C. Wang, G. Yin, Multiobjective optimization method for
multichannel microwave components of active phased array antenna, Math. Probl.
Eng. 2016 (2016), https://doi.org/10.1155/2016/5398308.

[4] Y. Park, Y. Cho, J. You, C. Park, H. Yoon, S. Lee, B. Na, G. Ju, H. Choi, Y. Lee,
A robust design and fabrication of micromachined electro-absorptive optical
modulator for 3D imaging. MOEMS and Miniaturized Systems XIII, 2014.

[5] H. Chen, X. Zhou, Y. Zhang, S. Lin, J. Zhou, Y. Fei, Study on the staggered array of
an LED system for improved thermal behavior, Appl. Opt. 54 (22) (2015)
6752–6757, https://doi.org/10.1364/AO.54.006752.

[6] G. Hetsroni, A. Mosyak, Z. Segal, G. Ziskind, A uniform temperature heat sink for
cooling of electronic devices, Int. J. Heat Mass Transf. 45 (16) (2002) 3275–3286,
https://doi.org/10.1016/S0017-9310(02)00048-0.

[7] W. Qu, I. Mudawar. Analysis of three-dimensional heat transfer in micro-channel
heat sink, Int. J. Heat Mass Transf. 45 (19) (2002) 3973–3985. <https://doi.org/
10.1016/S0017-9310(02)00101-1>.

[8] A. Bejan. Constructal-theory network of conducting paths for cooling a heat
generating volume, Int. J. Heat Mass Transf. 40 (4) (1997) 799–811. <https://doi.
org/10.1016/0017-9310(96)00175-5>.

[9] T. Wei, H. Huang, Y. Ma, J. Qian, Design and fabrication of multi-layer silicone
microchannel cooler for high-power chip array. 22nd International Conference on
Electronic Packaging Technology, 2021.

[10] S. Qian, W. Wang, C. Ge, S. Lou, E. Miao, B. Tang, Topology optimization of fluid
flow channel in cold plate for active phased array antenna, Struct. Multidiscip. O.
57 (6) (2017) 2223–2232. <https://doi.org/10.1007/s00158-017-1852-8>.

[11] K.P. Drummond, D. Back, M.D. Sinanis, D.B. Janes, D. Peroulis, J.A. Weibel, S.
V. Garimella, A hierarchical manifold microchannel heat sink array for high-heat-
flux two-phase cooling of electronics, Int. J. Heat Mass Transf. 117 (2018).

[12] H. Tan, K. Zong, P. Du, Temperature uniformity in convective leaf vein-shaped
fluid microchannels for phased array antenna cooling, Int. J. Therm. Sci. 150
(2020) 106224, https://doi.org/10.1016/j.ijthermalsci.2019.106224.

[13] H. Tan, P. Du, K. Zong, G. Meng, X. Gao, Y. Li, Investigation on the temperature
distribution in the two-phase spider netted microchannel network heat sink with
nonuniform heat flux, Int. J. Therm. Sci. 169 (2021) doi:107079.https://doi.org/
10.1016/j.ijthermalsci.2021.107079.

[14] L. Yuan, L. Sheng, M. Chen, X. Luo, Thermal analysis of high power LED array
packaging with microchannel cooler, in: 7th International Conference on
Electronic Packaging Technology, 2006, pp. 1–5, https://doi.org/10.1109/
ICEPT.2006.359826.

[15] G. Laguna, M. Vilarrubí, M. Ibañez, Y. Betancourt, J. Illa, H. Azarkish, A. Amnache,
L.M. Collin, P. Coudrain, L. Fréchette, J. Barrau, Numerical parametric study of a
hotspot-targeted microfluidic cooling array for microelectronics, Appl. Therm. Eng.
144 (2018) 71–80, https://doi.org/10.1016/j.applthermaleng.2018.08.030.

[16] X. Li, Y. Xuan, Q. Li, Self-adaptive chip cooling with template-fabricated
nanocomposite P(MEO2MA-co-OEGMA) hydrogel, Int. J. Heat Mass Transf. 166
(2021) 120790, https://doi.org/10.1016/j.ijheatmasstransfer.2020.120790.

[17] Y. Yan, Z. He, G. Wu, L. Zhang, Z. Yang, L. Li, Influence of hydrogels embedding
positions on automatic adaptive cooling of hot spot in fractal microchannel heat
sink, Int. J. Therm. Sci. 155 (2020) 106428, https://doi.org/10.1016/j.
ijthermalsci.2020.106428.

[18] X. Chu, H. You, X. Tang, W. Zhou, X. Li, D. Yuan, S. Zhou, Smart microchannel heat
exchanger based on the adaptive deformation effect of shape memory alloys,

Energy Convers. Manage. 250 (15) (2021) 114910, https://doi.org/10.1016/j. enconman.2021.114910.

[19] C.H. Cheng, S.Y. Huang, T.C. Cheng, A three-dimensional theoretical model for predicting transient thermal behavior of thermoelectric coolers, Int. J. Heat Mass Transf. 53 (9-10) (2010) 2001-2011. <https://doi.org/10.1016/j. ijheatmasstransfer.2009.12.056>.

[20] X. Lin, S. Mo, L. Jia, Z. Yang, Y. Chen, Z. Cheng, Experimental study and Taguchi analysis on LED cooling by thermoelectric cooler integrated with microchannel heat sink, Appl. Energy 242 (2019) 232-238, https://doi.org/10.1016/j. apenergy.2019.03.071.

[21] T. Guclu, E. Cuce, Thermoelectric Coolers (TECs): from theory to practice, J. Electron Mater. 48 (2019) 211-230, https://doi.org/10.1007/s11664-018-6753-0.

[22] W. Zhu, Y. Deng, Y. Wang, A. Wang, Finite element analysis of miniature thermoelectric coolers with high cooling performance and short response time, Microelectron. J. 44 (9) (2013) 860-868, https://doi.org/10.1016/j. mejo.2013.06.013.

[23] E. Cuce, T. Guclu, P.M. Cuce, Improving thermal performance of thermoelectric coolers (TECs) through a nanofluid driven water to air heat exchanger design: an experimental research, Energy Convers. Manage. 214 (2020) 112893, https://doi. org/10.1016/j.enconman.2020.112893.

[24] N. Ahammed, L.G. Asirvatham, S. Wongwises, Entropy generation analysis of graphene-alumina hybrid nanofluid in multiport minichannel heat exchanger coupled with thermoelectric cooler, Int. J. Heat Mass Transf. 103 (2016) 1084-1097, https://doi.org/10.1016/j.ijheatmasstransfer.2016.07.070.

[25] Y.W. Gao, H. Lv, X.D. Wang, W.M. Yan, Enhanced Peltier cooling of two-stage thermoelectric cooler via pulse currents, Int. J. Heat Mass Transf. 114 (2017) 656-663, https://doi.org/10.1016/j.ijheatmasstransfer.2017.06.102.

[26] H. Hu, T. Ge, Y. Dai, R. Wang, Experimental study on water-cooled thermoelectric cooler for CPU under severe environment, Int. J. Refrig. 62 (2016) 30-38, https:// doi.org/10.1016/j.ijrefrig.2015.10.015.

[27] O. Sullivan, M.P. Gupta, S. Mukhopadhyay, S. Kumar, Array of thermoelectric coolers for on-chip thermal management, J. Electro. Packag. 134 (2) (2012) 021005, https://doi.org/10.1115/1.4006141.

[28] I. Chowdhury, R. Prasher, K. Lofgreen, G. Chrysler, S. Narasimhan, R. Mahajan, D. Koester, R. Alley, R. Venkatasubramanian, On-chip cooling by superlattice- based thin-film thermoelectrics, Nat. Nanotechnol. 4 (4) (2009) 235-238, https:// doi.org/10.1038/NNANO.2008.417.

[29] H.H. Saber, S.A. AlShehri, W. Maref, Performance optimization of cascaded and non-cascaded thermoelectric devices for cooling computer chips, Energy Convers. Manage. 191 (2019) 174-192, https://doi.org/10.1016/j.enconman.2019.04.028.

[30] K. Xie, Y. Zheng, The temperature-controlled system of variable thermal resistance based on self-powered thermoelectric effect, Aip Adv. 10 (2020) 075318, https:// doi.org/10.1063/5.0011459.

[31] Y. Chang, C. Chang, M. Ke, S. Chen, Thermoelectric air-cooling module for electronic devices, Appl. Therm. Eng. 29 (13) (2009) 2731-2737, https://doi.org/ 10.1016/j.applthermaleng.2009.01.004.

[32] P. Fredes, U. Raff, E. Gramsch, J. Pascal, J. Cuenca, Junction temperature control of UV-C LEDs based on a thermoelectric cooler device, Microelectron. Reliab. 98 (2019) 24-30, https://doi.org/10.1016/j.microrel.2019.04.011.

[33] Y. Cai, D. Liu, F.Y. Zhao, J.F. Tang, Performance analysis and assessment of thermoelectric micro cooler for electronic devices, Energy Convers. Manage. 124 (2016) 203-211, https://doi.org/10.1016/j.enconman.2016.07.011.

[34] V. Szekely, G. Mezosi, Design issues of a variable thermal resistance. 12th International Workshop on Thermal Investigations of ICs, 2006.

[35] J. Cheng, X. He, Research on thermal coupling effect of multi-heating sources in MCM, in: 17th International Conference on Electronic Packaging Technology, 2016, pp. 1469-1475, https://doi.org/10.1109/ICEPT.2016.7583401.

[36] D. Zhong, H. Qin, C. Wang, Z. Xiao, Thermal performance of heatsink and thermoelectric cooler packaging designs in LED, in: 11th International Conference on Electronic Packaging Technology, 2010, pp. 1377-1381, https://doi.org/ 10.1109/ICEPT.2010.5582819.

[37] Y. Ye, R. Liu, X. Du, N. Zhang, Y. Kong, B. Jiao, D. Chen, Investigation on multidimensional test vehicle for embedded microfluidic cooling performance evaluation, Appl. Therm. Eng. 195 (2021) 117149, https://doi.org/10.1016/j. applthermaleng.2021.117149.

[38] H. Lee, Y. Jeong, J. Shin, S. Kim, M. Kim, M. Kang, K. Chun, Package embedded heat exchanger for stacked multi-chip module, Sensor Actuat. A- Phys. 114(2-3) (2004) 204-211. <https://doi.org/10.1109/sensor.2003.1216956>.

[39] R. Singh, S. Sundaresan, Fulfilling the promise of high-temperature operation with silicon carbide devices: eliminating bulky thermal-management systems with SJTs, in: IEEE Power Electronics Magazine, vol. 2, 2015, pp. 27-35. https://doi.org/ 10.1109/MPEL.2014.2383328.

[40] Z. Luo, A simple method to estimate the physical characteristics of a thermoelectric cooler from vendor datasheets, Electron. Cool. 14 (2008) 22-27.

[41] R. Zheng, Y. Wu, Y. Li, G. Wang, G. Ding, Y. Sun, Development of a hierarchical microchannel heat sink with flow field reconstruction and low thermal resistance for high heat flux dissipation, Int. J. Heat Mass Transf. 182 (2022) 121925, https:// doi.org/10.1016/j.ijheatmasstransfer.2021.121925.

[42] R.J. Moffat, Describing the uncertainties in experimental results, Exp. Therm. Fluid Sci. 1 (1) (1988) 3-17. <https://doi.org/10.1016/0894-1777(88)90043-X>.

[43] B. Alexandrov, O. Sullivan, W.J. Song, S. Yalamanchili, S. Kumar, S. Mukhopadhyay, Control principles and on-chip circuits for active cooling using integrated superlattice-based thin-film thermoelectric devices. IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2014.
12