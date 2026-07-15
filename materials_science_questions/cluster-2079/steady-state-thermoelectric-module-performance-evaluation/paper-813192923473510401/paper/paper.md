# Improvement of SOFC System Efficiency by Incorporating Thermoelectric Power Generation Heat Exchanger

T. Terayama$^{a,b}$, S. Nagata$^{a}$, Y. Tanaka$^{a}$, A. Momma$^{a}$, T. Kato$^{a}$, A. Yamamoto$^{a}$

$^{a}$ Energy Technology Research Institute, National Institute of Advanced Industrial Science and Technology, 1-1-1 Umezono, Tsukuba, Ibaraki 305-8568, Japan
$^{b}$ Department of Electrical Engineering, Graduate School of Science and Technology, Tokyo University of Science, 2641 Yamazaki, Noda, Chiba 278-8510, Japan

The effects of replacing a water heater at a bottom of 700 W class SOFC system with thermoelectric generation heat exchanger (TEG-HEX) was investigated by numerical simulation. A 2205 $\text{cm}^3$ large TEG-HEX can generate additional power of 11.5 W in the case of each TE element height = 0.9 cm and heat transfer enhance rate = 3.0. This output power corresponds to improvement of SOFC power generation efficiency by 0.756 points. Increasing TE elements height are effective to increase output power of TEG-HEX, however, this leads to substantial decrease of power density estimated on TE elements volume. Decrease in the power density leads directly to higher cost, thus we should regard the power density as guiding principle of practical design. In addition, 30 % of the downstream of the TEG-HEX generate low power, thus cutting down this wasted part leads to improved power density and cost.

## Introduction

The solid oxide fuel cell (SOFC) is a highly-efficient power generator and being researched all over the world. The most efficient SOFC system currently available for sale in the world is BlueGen, developed by Ceramic Fuel Cells Ltd.. Generating efficiency of 60 % alternative current (AC) is achieved and additional heat of 25 % is available (1). In Japan, a compact SOFC system for residential use, known as ENE-FARM type S, is available in the market by Osaka Gas since 2012. It is rated at 700 W AC power, its generating efficiency is 46.5 % when 700 W outputted, and its overall efficiency, as a micro- combined heat and power (CHP), is 90 % (2). We are currently focusing on thermoelectric generation (TEG) technology as a means of improving the electrical efficiency of 700 W class SOFC systems.

The thermoelectric generation technology is one of the energy harvesting technology, generating electricity by being given difference of thermal potential in thermoelectric (TE) elements. A generator, composed of thermoelectric materials, is characterized as high reliability, noise-free, and maintenance-free due to having no moving parts.

In our recent work, we found that the electrical efficiency of 700 W class SOFC systems can be improved by incorporating thermoelectric power generation heat exchangers (TEG-HEXs), or thermoelectric module integrated heat exchangers, into an

air preheater, a steam generator, and a bottom of the system, shown in Figure 1. In addition, incorporating the TEG-HEX, composed of state-of-the-art TE elements, into the air preheater has potential to generate maximum 37.5 W, considering a size of the TEG-HEX and fluid characteristics, it is expected to generate power of 5 to 20 W (3).

At the bottom of the SOFC system, there is generally a cogeneration unit, such as a water heater, reutilizing the enthalpy of the exhaust to heat up water. In this work, we focused on the water heater, and analyzed effects of replacing the water heater with the TEG-HEX and evaluated favorable design by numerical simulation.

![](./images/813192923473510401_1.jpg)

Figure 1. Schematic of SOFC system.

## Simulation Model

This simulation model is based on data disclosed for a compact SOFC system for residential use rated AC power of 700 W (4). The TEG-HEX is placed at the bottom of the SOFC system, shown in Figure 1, and heats up water from 298.15 K to about 348 K by consuming enthalpy of exhaust, outputted from the system. The exhaust flows in the TEG-HEX at 538 K and composed of $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{O}_2$, and $\text{N}_2$. Details of the power generating unit are presented in previous research paper (3).

### Calculation of Flow Rate

The flow rate of water is set to consume 92% of enthalpy of the system exhaust to heat up itself from 298.15 K to about 348 K. The flow rate (mol/s) of water is expressed by following equations:

$$
M(\text{water})=0.92 \cdot \frac{\sum_{j} M_{j} H_{j}\left(T_{\text{ex,in}}\right)-\sum_{j} M_{j} H_{j}(298.15)}{H_{\text{water}}(348)-H_{\text{water}}(298.15)} \tag{1}
$$

where $M_j$ is the mole flow rate of gas species of $j$ (mol/s), $H_j$ is the enthalpy of gas spe-

cies $j$ (J/mol), $H_{\text{water}}$ is the enthalpy of liquid water (J/mol), $T_{\text{ex,in}}$ is the inlet temperature of the exhaust (K).

Computation methods for the flow rate of the exhaust are presented in previous research paper (3).

### Enthalpy Balance

The TEG-HEX is analyzed by using a finite-difference model, divided along the direction of gas and water flows. The schematic heat migration between each node is shown in Figure 2.

![](./images/813192923473510401_2.jpg)

Figure 2. Schematic of heat migration between each node. $i$: node number; $Q_{\text{cond}}$ is heat migration due to conduction heat transfer term in the aluminum alloy (Al alloy) plate 1; $Q_{\text{trans}}^{\text{w}}$ is heat migration due to convection heat transfer between the Al alloy plate 1 and exhaust; $Q_{\text{conv}}$ is the enthalpy of gasses; $Q_{\text{in}}^{\text{TE}}$ and $Q_{\text{out}}^{\text{TE}}$ are heat transfer induced by thermoelectric effect. Superscripts: Th and Tc, denote the high temperature side and low temperature side, respectively.

The enthalpy balance between adjacent nodes in node number $i$ is expressed as follows:

● Enthalpy Balance in Al alloy Plate 1.

$$
Q_{\text{cond}}^{\text{Th}}(i)-Q_{\text{cond}}^{\text{Th}}(i-1)=\sum Q_{\text{trans}}^{\text{w,Th}}(i)-Q_{\text{in}}^{\text{TE}}(i) \tag{2}
$$

$$
Q_{\text{cond}}^{\text{Th}}(i)=k_{\text{p}} \frac{d A_{\text{c}}}{d X_{\text{wid}}}\left(T_{\text{hj}}(i+1)-T_{\text{hj}}(i)\right) \tag{3}
$$

$$
\sum Q_{\text {trans }}^{\mathrm{w}, \mathrm{Th}}(i)=h_{\mathrm{ex}} d A_{\mathrm{w}}\left(T_{\mathrm{ex}}(i)-T_{\mathrm{hj}}(i)\right)
\tag{4}
$$

● Enthalpy Balance in Al alloy Plate 2.

$$
Q_{\text {cond }}^{\mathrm{Tc}}(i)-Q_{\text {cond }}^{\mathrm{Tc}}(i+1)=-\sum Q_{\text {trans }}^{\mathrm{w}, \mathrm{Tc}}(i)+Q_{\text {out }}^{\mathrm{TE}}(i)
\tag{5}
$$

$$
Q_{\text {cond }}^{\mathrm{Tc}}(i)=k_{\mathrm{p}} \frac{d A_{\mathrm{c}}}{d X_{\text {wid }}}\left(T_{\mathrm{cj}}(i-1)-T_{\mathrm{cj}}(i)\right)
\tag{6}
$$

$$
\sum Q_{\text {trans }}^{\mathrm{w}, \mathrm{Tc}}(i)=h_{\text {water }} d A_{\mathrm{w}}\left(T_{\mathrm{cj}}(i)-T_{\text {water }}(i)\right)
\tag{7}
$$

● Enthalpy Balance in Exhaust.

$$
Q_{\text {conv }}^{\mathrm{Th}}(i)-Q_{\text {conv }}^{\mathrm{Th}}(i-1)=-\sum Q_{\text {trans }}^{\mathrm{w}, \mathrm{Th}}(i)
\tag{8}
$$

$$
Q_{\text {conv }}^{\mathrm{Th}}(i)=\sum_{j} M_{j} H_{j}\left(T_{\mathrm{hj}}(i)\right)
\tag{9}
$$

● Enthalpy Balance in Water.

$$
Q_{\text {conv }}^{\mathrm{Tc}}(i)-Q_{\text {conv }}^{\mathrm{Tc}}(i+1)=\sum Q_{\text {trans }}^{\mathrm{w}, \mathrm{Tc}}(i)
\tag{10}
$$

$$
Q_{\text {conv }}^{\mathrm{Tc}}(i)=M(\text { water }) \cdot H_{\text {water }}\left(T_{\mathrm{cj}}(i)\right)
\tag{11}
$$

Here, $T_{\mathrm{hj}}, T_{\mathrm{cj}}, T_{\mathrm{ex}}$, and $T_{\text {water }}$ are the temperature of Al alloy plate 1, Al alloy plate 2, exhaust, and water (K), respectively, $h_{\mathrm{ex}}$ and $h_{\text {water }}$ are the heat transfer coefficient ($\mathrm{W} / \mathrm{m}^{2} \mathrm{~K}$), $k_{\mathrm{p}}$ is the thermal conductivity of Al alloy ($\mathrm{W} / \mathrm{mK}$), $d A_{\mathrm{c}}$ is the cross-sectional area of Al alloy plate $\left(\mathrm{m}^{2}\right)$, calculated as $d A_{\mathrm{c}}=N_{\mathrm{TE}} d X_{\mathrm{TE}} d X_{\mathrm{t}}, d A_{\mathrm{w}}$ is the surface area of each node $\left(\mathrm{m}^{2}\right)$, contacting gas or water, calculated as $d A_{\mathrm{w}}=N_{\mathrm{TE}} d X_{\mathrm{TE}} d X_{\text {wid }}, N_{\mathrm{TE}}$ is the number of TE elements. To facilitate calculation of conduction heat transfer, the width of each node, $d X_{\text {wid }}$, is set to be equal to the width of TE elements, $d X_{\mathrm{TE}}$.

**Condensation Heat Transfer.**

In the process of exchanging heat between the exhaust and water, water vapor in the exhaust starts to be condensed and $h_{\mathrm{ex}}$ is substantially changed. During condensation, because the volume flow rate of water in exhaust is less, compared to the cross-sectional area of the duct, we presumed that film condensation on vertical wall. To facilitate calculation of condensation, pure vapor condensation is presumed here. The condensing heat transfer coefficient is expressed as follows (5):

$$
h_{\text {dens }}(T)=0.943\left[\frac{\rho_{\mathrm{f}}\left(\rho_{\mathrm{f}}-\rho_{\mathrm{v}}\right) g h_{\mathrm{fg}} k_{\mathrm{f}}^{3}}{L \mu_{\mathrm{f}}\left(T_{\text {boil }}-T\right)}\right]^{1 / 4}
\tag{12}
$$

where $\rho$ is the density $\left(\mathrm{kg} / \mathrm{m}^{3}\right), g$ is the gravity acceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right), h_{\mathrm{fg}}$ is the latent heat $(\mathrm{J} / \mathrm{kg}), L$ is the condensation block distance $(\mathrm{m}), \mu$ is viscosity $(\mathrm{Pa} \cdot \mathrm{s}), T_{\text {boil }}$ is the boiling temperature (K). In this simulation, $T_{\text {boil }}$ is equal to 375.47 K since absolute pressure of

the exhaust is set to be 111.4 kPa. Subscripts: f and v, denote the film, vapor. In the case of $L=0.2$ m, $h_{\text{dens}}(T)$ at each temperature becomes as shown in Figure 3.

![](./images/813192923473510401_3.jpg)

Figure 3. Condensing heat transfer coefficient at each temperature.

### Thermoelectric Effect

Heat flow and power, obtained by thermoelectric effect, are calculated at each node by following equations.

$$
Q_{\text{in}}^{\text{TE}}(i)=\alpha T_{\text{hj}}(i) I_{\text{TEG}}(i)-\frac{1}{2} R_{\text{TEG}} {I_{\text{TEG}}}^{2}(i)+K\left(T_{\text{hj}}(i)-T_{\text{cj}}(i)\right) \tag{13}
$$

$$
Q_{\text{out}}^{\text{TE}}(i)=\alpha T_{\text{cj}}(i) I_{\text{TEG}}(i)+\frac{1}{2} R_{\text{TEG}} {I_{\text{TEG}}}^{2}(i)+K\left(T_{\text{hj}}(i)-T_{\text{cj}}(i)\right) \tag{14}
$$

$$
I_{\text{TEG}}(i)=\alpha\left(T_{\text{hj}}(i)-T_{\text{cj}}(i)\right) /\left(R_{\text{TEG}}+R_{L}\right) \tag{15}
$$

$$
P_{\text{TEG}}(i)=R_{\text{L}} {I_{\text{TEG}}}^{2}(i) \tag{16}
$$

$$
\eta_{\text{TE, total}}=\sum_{i} P_{T E G}(i) / \sum_{i} Q_{i n}^{T E}(i) \cdot 100 \% \tag{17}
$$

Here, $\alpha$ is the Seebeck coefficient (V/K), $R_{\text{TEG}}$ is the TEG module internal resistance ($\Omega$), $R_{\text{L}}$ is the load resistance ($\Omega$), $K$ is the TEG module thermal conductance (W/K), $I_{\text{TEG}}$ is the current, output from each node (A).

### Simulation Conditions

A Simulation was carried out under the conditions presented in TABLEs I to III. To take account of heat transfer enhancement by fins and whatnot, heat transfer enhancement rate, $r_{\text{hte}}$, is incorporated and $A_{\text{w}}$ is multiplied by $r_{\text{hte}}$, except in condensation section.

TE materials are presumed p-type $(Bi_2Te_3)_{0.24}(Sb_2Te_3)_{0.76}$ (6) and n-type $Bi_2(Te,Se)_3$ (7), and average values of these physical properties are used for the calculation. These physical properties and average values are shown in Figure 4.

![](./images/813192923473510401_4.jpg)

Figure 4. Physical properties of TE materials. Subscript: p, n, and ave, denote p-type, n-type, average, respectively. $\alpha_{\text{ave}}$ is expressed as $\left(\alpha_{p}+\left|\alpha_{n}\right|\right) / 2$ (6), (7).

<table>
<caption>TABLE I. Simulation conditions for calculation of flow rate.</caption>
<thead>
<tr>
<th>AC output target (W)</th>
<th>Ratio of steam to methane, S/C</th>
<th>AC efficiency target (%)</th>
<th>Fuel utilization, $U_F$</th>
<th>Oxygen utilization, $U_{ox}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>700</td>
<td>2.0</td>
<td>46.0</td>
<td>0.7</td>
<td>0.3</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE II. Simulation conditions for calculation of heat migration balance.</caption>
<thead>
<tr>
<th>Heat transfer coefficient of exhaust, $h_{\text{ex}}$ (W/m²K) *</th>
<th>Heat transfer coefficient of water, $h_{\text{water}}$ (W/m²K)</th>
<th>Number of TE elements at each node, $N_{\text{TE}}$</th>
<th>TE element cross-sectional area, $dA_{\text{TE}}$ (cm²)</th>
<th>Thermal conductivity of Al alloy plate, $k_{\text{p}}$ (W/mK)</th>
<th>Thickness of Al alloy plate, $dX_{\text{t}}$ (cm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>50</td>
<td>400</td>
<td>35</td>
<td>0.09</td>
<td>200</td>
<td>0.2</td>
</tr>
</tbody>
</table>

* $h_{\text{dens}}$ is used instead of $h_{\text{ex}}$ in condensation section.

<table>
<caption>TABLE III. Heat transfer enhancement rate and TE element height.</caption>
<thead>
<tr>
<th>Heat transfer enhancement rate, $r_{\text{hte}}$</th>
<th>TE element height (cm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.0, 2.5, 3.0</td>
<td>0.3, 0.6, 0.9</td>
</tr>
</tbody>
</table>

To keep $T_{\text{water}} = 348$ K at the outlet of TEG-HEX, sum of $Q_{\text{out}}^{\text{TE}}$ is maintained at 630 W by tuning the TEG-HEX length.

# Results and Discussions

## Evaluating Total Performance

Total output power, efficiency, volume of the TEG-HEX, and power density are shown in Figure 5 (a), (b), Figure 6, and Figure 7.

![](./images/813192923473510401_5.jpg)

Figure 5. (a): Total output power of the TEG-HEX. (b): Total efficiency of the TEG-HEX. (or "Total output power (a) and efficiency (b) of the TEG-HEX.")

Output power and efficiency show a tendency to increase with increase in $r_{\text{hte}}$ and $L_{\text{TE}}$ as shown in Figure 5(or (a) and (b)). In the case of $r_{\text{hte}} = 3.0$ and $L_{\text{TE}} = 0.9$ cm, power and efficiency reach 11.5 W and 1.79 %, respectively. This output power corresponds to improvement of SOFC generating efficiency by 0.756 points, or improvement of efficiency from 46.0 % to 46.8 %.

However, increasing $L_{\text{TE}}$ resulted in enlargement of TEG-HEX volume and sum of TE elements volume, $V_{\text{WH}}$ and $V_{\text{TE}}$, as shown in Figure 6. Therefore, power density based on $V_{\text{WH}}$ and $V_{\text{TE}}$, expressed as $P_{\text{den}}$ and $P_{\text{TE,den}}$, show trajectories as shown in Figure 7(or (a) and (b)). In the cases of $r_{\text{hte}} = 2.0$ and $r_{\text{hte}} = 2.5$, $P_{\text{den}}$ exhibits peaks at 3.93 and 4.96 mW/cm³ when $L_{\text{TE}} = 0.6$ cm, and a peak can be expected less than $L_{\text{TE}} = 0.3$ cm when $r_{\text{hte}} = 3.0$. On the other hand, $P_{\text{TE,den}}$ shows no peaks and a tendency to decrease with increase in $L_{\text{TE}}$. Because the cost of TE material is generally higher, for example, BiTe costs about 1 $/cm³, a decrease in $P_{\text{TE,den}}$ leads directly to increasing the cost of TEG-HEXs. In

addition, since curves of $P_{\text{den}}$ looks relatively flat, $P_{\text{TE,den}}$, showing large gradient, is more effective in practical design. Therefore, it is expected that we should take into account the effect of $P_{\text{TE,den}}$ rather than the effect of $P_{\text{den}}$.

![](./images/813192923473510401_6.jpg)

Figure 6. Volume of the TEG-HEX. Height of exhaust and water duct were presumed to be 1.0 cm and 0.5 cm, respectively.

![](./images/813192923473510401_7.jpg)

Figure 7. (a): Power density based on TEG-HEX volume. (b): Power density based on sum of TE elements volume.( or "Power density based on TEG-HEX volume (a) and sum of TE elements volume (b)").

### Evaluating Temperature Distribution in the TEG-HEX

In this section, we focused attention on characteristics in the TEG-HEX when $L_{\text{TE}} =$ 0.6 cm and $r_{\text{hte}} = 2.5$. $T_{\text{ex}}$, $T_{\text{water}}$, $T_{\text{hj}}$, $T_{\text{cj}}$, and temperature difference between $T_{\text{hj}}$ and $T_{\text{cj}}$, $dT$, are shown in Figure 8(or (a) and (b)). The abscissa, $x$, is expressed as the distance from the exhaust inlet to each point over length of the TEG-HEX times 100 (%). In

almost all points, temperature difference between $T_{\mathrm{ex}}$ and $T_{\mathrm{hj}}$ is larger than that of between $T_{\mathrm{water}}$ and $T_{\mathrm{cj}}$ due to low $h_{\mathrm{ex}}$, thus $dT$ doesn't become as large as temperature difference between $T_{\mathrm{ex}}$ and $T_{\mathrm{water}}$. However, in the condensation section, $T_{\mathrm{hj}}$ can be approximately equal to $T_{\mathrm{ex}}$ and then $dT$ reaches at maximum of 46.2 K.

![](./images/813192923473510401_8.jpg)

Figure 8. (a): $T_{\mathrm{ex}}$, $T_{\mathrm{water}}$, $T_{\mathrm{hj}}$, and $T_{\mathrm{cj}}$ at each point. (b): Temperature difference, $dT$, at each point.

![](./images/813192923473510401_9.jpg)

Figure 9. Cumulative power from the exhaust inlet to each point.

As discussed in previous section, because the power of TEG-HEXs is generally improved by increasing $L_{\mathrm{TE}}$, in other word, increasing thermal resistance, there is a trade-off relationship between increasing power of TEG-HEXs and making TEG-HEXs smaller. To keep compact design and large power, the low-power generation part of TEG-HEX should be cut down. Therefore we focused on cumulative power from the exhaust to each point presented in Figure 9. As shown in the figure, 80 % of the generated power is obtained from near the exhaust inlet and condensation section, and the rest of the part, such as about $x=70$ % to 100 %, shows a little contribution to the total power output. Optimum design with the idea that omitting this low-power part could be reasonable to enhance the cost-benefit performance.

### Conclusion

In this research, we focused on the water heater at the bottom of 700 W class SOFC system, and analyzed effects of substituting the TEG-HEX for the water heater and evaluated favorable design by numerical simulation.

TEG-HEX becomes $2205\ \text{cm}^3$ and can generate additional power of 11.5 W in the case of TE element height is 0.9 cm and heat transfer enhance rate is 3.0, and this output power corresponds to improvement of SOFC system efficiency by 0.756 points, or improvement of efficiency from 46.0 % to 46.8 %. Increasing TE elements height and using high performance fins are effective to increase output power of TEG-HEX, however, increasing its height leads to decreasing power density based on TE elements volume substantially. Because TE materials cost is higher than other materials used for TEG-HEX, decrease in this power density leads directly to being expensive. Therefore, we should take into consideration power density based on TE elements volume in practical design stage.

We found that high power output is obtained near the exhaust inlet and condensation area, however, there are some TE elements generating low power in 30 % of the last of the TEG-HEX. Therefore, cutting down this 30 % of the last leads to improved power density and cost.

In the water heater, the air preheater, and so on, output power of each TEG-HEX is small, however, it is expected that aggregating each power leads to improvement of SOFC system electrical efficiency by a few points.

### Acknowledgments

The authors would like to express special thanks to Ken Nozaki for valuable comments on the system analysis and to Yoko Iimura for general support for the research activity. Authors would also like to thank Sumio Kogoshi and Noboru Katayama of Tokyo University of Science for important advice and for supporting the collaborative research of SOFC with AIST.

### References

1. R. Payne, J. Love, M. Kah, *ECS Trans.*, **25(2)**, 231 (2009).
2. Fuel Cells Bulletin, 2012(4), p.4 (2012).
3. T. Terayama, et al., in press *J. Electron. Mater.* (2012).
4. Y. Kayahara, Proc. Solid Oxide Fuel Cell Demonstration Program, New Energy Foundation, 96, (2011).
5. J. P. Holman, Heat transfer (Japanese edition), p. 360, Maruzen, Tokyo (1982).
6. J. Jiang, L. Chen, Q. Yao, Q. Wang, *Materials Trans.*, **46(5)**, 959 (2005).
7. J. Jiang, L. Chen, S. Bai, Q. Yao, Q. Wang, *Materials Science and Engineering: B*, **117**, 334 (2005).