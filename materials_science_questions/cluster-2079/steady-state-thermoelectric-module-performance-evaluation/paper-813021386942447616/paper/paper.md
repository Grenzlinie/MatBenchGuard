# A solar hybrid system for power generation and water distillation

Moh'd A. Al-Nimr, Khaled S. Qananba*

Mechanical Engineering, Jordan University of Science and Technology, P.O. Box 3030, Irbid 22110, Jordan

---

## ARTICLE INFO

**Keywords:**
Solar energy
Hybrid
Thermoelectric generator
PV cell
Distillation

---

## ABSTRACT

A solar still of a single basin-slope coupled with a finned condensing chamber and photovoltaic cells immersed in the water basin and thermoelectric generators installed in the base of the basin has been presented in this paper. A mathematical model under steady-state conditions has been introduced and improved to investigate the system performance. An increase of solar radiation and ambient temperature or a decrease in wind velocity affect positively the distillation rate, still efficiency, system efficiency, and output power. Integrating fins through the wall of condenser increase the distillation rate of the proposed system. When the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, and system efficiency will be increased up to 27%, 21%, and 28% respectively, but the power output will be decreased up to 16.6% at solar radiation of $1000\ \text{W/m}^2$. Moreover, when the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, system efficiency, and power output will be decreased up to 37%, 32%, 34%, and 17%, respectively, at a wind speed of 10 m/s. Also, the water distillation, still efficiency, and system efficiency of the solar still with a condensing chamber will be higher than the conventional solar still up to 7%, 8%, and 7% respectively, but the power output will be decreased up to 3% at solar radiation of $1000\ \text{W/m}^2$. While in the third design, solar still with a finned condensing chamber, the water distillation, still efficiency, and system efficiency will be higher than the conventional solar still up to 14%, 12.5%, and 11% respectively, but the power output will be decreased up to 6% at solar radiation of $1000\ \text{W/m}^2$. The results of the simulation have been verified by comparing them with published theoretical and experimental results and the comparison shows very good agreement.

---

## 1. Introduction

Since we were children, our subjects at all grade levels dealt with the importance of saving water and energy in everyday uses, which we did not consider it as an important thing. Ignorance, unjust use and failure to take into account the importance of water and energy to us, to others and to those who will inhabit the earth in the future have established problems of limited or non-availability of these resources in some regions of the world. The process of producing energy requires water and the process of providing water for human use that needs energy. The process of water and energy dependence on each other has created a new and growing global challenge (Union of Concerned Scientists, 2017).

Most of the electricity generation sectors currently rely on water mainly. If we take into account, the power plants that use fuel in all forms in the generation of thermal energy to heat the water and convert it from liquid to steam to run steam turbines and many other applications. In order to solve this dilemma, the world is currently turning to a number of options that are easy to implement, such as applying the cost-effective principle, which is based on the working mechanism of appliances, tools, buildings, heavy machinery and transportation which has been applied in many major industrial countries. The process of using renewable energy, such as solar energy, wind energy, and many others, will reduce the use of water in the process of generating power, which does not need in both cases.

In the last decade, the renewable energy sector has developed, its efficiency and diversity of technology fields and the world's attention has increased because of its important impact in protecting the environment from pollution and its effects on the threat of life on earth. The solar energy is the most exploited in the renewable energy sector recently and the last decade has seen a lot of development in the field of tools and devices used in the generation of energy such as photovoltaic cells, the thermoelectric generators and solar concentrators (Nrel.gov, 2017). Photovoltaic systems have become used in many fields, whether industrial, commercial, domestic, and agricultural. Another application is the thermoelectric generator, a device that converts heat energy (temperature difference) to electrical energy directly through a phenomenon called the Seebeck effect. This device is new or not conventional compared to the photovoltaic cells and of these reasons it has a low efficiency, which may reach at the best conditions.

---

* Corresponding author.
E-mail addresses: malnimr@just.edu.jo (M.A. Al-Nimr), ksqananba15@eng.just.edu.jo (K.S. Qananba).

https://doi.org/10.1016/j.solener.2018.06.019
Received 12 February 2018; Received in revised form 7 May 2018; Accepted 4 June 2018
0038-092X/ © 2018 Elsevier Ltd. All rights reserved.

### Nomenclature

| $A_{b,f}$ | area of the base of the fins array ($\text{m}^2$) |
|-----------|---------------------------------------------------|
| $A_b$     | surface area of basin base ($\text{m}^2$)         |
| $A_c$     | surface area of all constructed fins ($\text{m}^2$) |
| $A_g$     | area of the glass cover ($\text{m}^2$)            |
| $A_{g,e}$ | effective area of glass cover ($\text{m}^2$)      |
| $A_w$     | free surface area of saline water ($\text{m}^2$)  |
| $A_{cf}$  | surface area of all constructed fins array on TEMs ($\text{m}^2$) |
| $A_p$     | cross-sectional area of the positive doped leg of each thermoelectric unit ($\text{m}^2$) |
| $A_N$     | cross-sectional area of the negative doped leg of each thermoelectric unit ($\text{m}^2$) |
| $\dot{E}_{in,1}, \dot{E}_{in,2}, \dot{E}_{in,3}, \dot{E}_{in,4}, \dot{E}_{in,5}$ | energy rate entering in system 1, 2, 3, 4, and 5 respectively (W) |
| $\dot{E}_{gen,1}$ | the rate of energy generation by the PV module (W) |
| $\dot{E}_{out,2}, \dot{E}_{out,3}, \dot{E}_{out,4}, \dot{E}_{out,5}$ | energy rate existing system 1, 2, 3, 4, and 5 respectively (W) |
| $G$       | solar radiation ($\text{W/m}^2$)                  |
| $h_{c,ga}$ | convective heat transfer coefficient from transparent glass cover to ambient ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{r,ga}$ | radiative heat transfer coefficient from transparent glass cover to ambient ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{c,wg}$ | convective heat transfer coefficient from water to transparent glass cover ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{ev,wg}$ | evaporative heat transfer coefficient from water to transparent glass cover ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{r,wg}$ | radiative heat transfer coefficient from water to glass cover ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{c,bw}$ | convective heat transfer coefficient from basin to water ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{k,bh}$ | conductive heat transfer coefficient from basin to TEMs hot surface ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{tt,ca}$ | overall heat transfer coefficient ($\text{W/m}^2 {^\circ}\text{C}$) |
| $h_{t,ca}$ | sum of convective and radiative heat transfer coefficients from TEMs cold surface to ambient ($\text{W/m}^2 {^\circ}\text{C}$) |
| $i_{fg,w}$ | latent heat of vaporization for water (J/kg)      |
| $I$       | generated electrical direct current (A)           |
| $K$       | total thermal conductance for n pairs of thermoelectric legs ($\text{W/m} {^\circ}\text{C}$) |
| $K_b$     | thermal conductivity of basin ($\text{W/m} {^\circ}\text{C}$) |
| $L_b$     | thickness of water basin (m)                       |
| $L_p$     | length of the positive doped leg in each thermoelectric unit (m) |
| $L_N$     | length of the negative doped leg in each thermoelectric unit (m) |
| $\dot{m}$ | mass flow rate (kg/s)                              |
| $m$       | matched load                                       |
| $n$       | number of thermoelectric pairs in each module      |
| $P_L$     | generated electrical power (W)                     |
| $P_{g,e}$ | effective saturated vapor pressure of water at $T_{g,e}$ ($\text{N/m}^2$) |
| $P_w$     | saturated vapor pressure of water at Tw ($\text{N/m}^2$) |
| $Q_{c,ga}$ | rate of convective heat transfer from glass cover to ambient (W) |
| $Q_{r,ga}$ | rate of radiative heat transfer from glass cover to ambient (W) |
| $Q_{c,wg}$ | rate of convective heat transfer from water to glass cover (W) |
| $Q_{ev,wg}$ | rate of evaporative heat transfer from water to glass cover (W) |
| $Q_{r,wg}$ | rate of radiative heat transfer from water to glass cover (W) |
| $Q_{s,w}$ | rate of energy absorbed by saline water (W)        |
| $Q_{s,b}$ | rate of energy absorbed by basin (W)               |
| $Q_{S,pv}$ | rate of energy absorbed by PV module (W)           |
| $Q_{c,bw}$ | rate of convective heat transfer from water basin to water (W) |
| $Q_{k,bh}$ | rate of conductive heat transfer between basin to TEMs surface (W) |
| $Q_{t,ca}$ | overall heat loss from the fins of cold-side TEMs to the ambient (W) |
| $Q_h$     | rate of heat transfer absorbed by the hot-side of the TEMs (W) |
| $Q_c$     | rate of heat transfer rejected by the cold-side of the TEMs (W) |
| $R$       | total electrical resistance of the thermoelectric modules ($\Omega$) |
| $R_L$     | external load resistance connected to the TEMs ($\Omega$) |
| $T_a$     | ambient temperature ($^\circ\text{C}$)             |
| $T_g$     | glass cover temperature ($^\circ\text{C}$)         |
| $T_{g,e}$ | effective glass cover temperature ($^\circ\text{C}$) |
| $T_{sky}$ | temperature of sky ($^\circ\text{C}$)              |
| $T_w$     | water temperature ($^\circ\text{C}$)               |
| $T_b$     | basin temperature ($^\circ\text{C}$)               |
| $T_h$     | TEMs hot surface temperature ($^\circ\text{C}$)    |
| $T_c$     | TEMs cold surface temperature ($^\circ\text{C}$)   |
| $V$       | wind velocity (m/s)                                |
| $z$       | the figure of merit                                |
| $\tilde{\alpha}$ | seebeck coefficient of tow junctions (average value) |
| $\alpha_g,\alpha_w,\alpha_b$ | absorptivity of glass cover, water, and basin respectively |
| $\varepsilon_g,\varepsilon_w$ | emissivity of glass cover and water respectively   |
| $\varepsilon_{eff}$ | effective emittance between water to glass cover   |
| $\eta_{pv}$ | the efficiency of the PV modules (%)               |
| $\eta_{still}$ | solar still efficiency (%)                         |
| $\eta_{\text{TEMs}}$ | the efficiency of the thermoelectric modules       |
| $\lambda_p$ | thermal conductivity of the positive leg of the thermoelectric junction |
| $\lambda_N$ | thermal conductivity of the negative leg of the thermoelectric junction |
| $\sigma$   | Stefan–Boltzmann constant ($5.67 \times 10^{-8} \text{W/m}^2\text{K}^4$) |
| $\sigma_N$ | electrical conductivity of the negative leg of the thermoelectric junction ($\Omega\text{m})^{-1}$ |
| $\sigma_p$ | electrical conductivity of the positive leg of the thermoelectric junction ($\Omega\text{m})^{-1}$ |
| $\tau_g, \tau_w$ | transmissivity of glass cover and water respectively |

Many researchers have recently gone on to create hybrid systems consisting of two or three systems that exploit as much as possible energy to improve system performance. These systems are diverse and exist in many applications whether they are based on fuel or renewable energy. A hybrid system consisting of four systems (photovoltaic cell system, wind energy conversion system, fuel cells and battery storage system) was built. This system produced electricity by two renewable energy sources (solar radiation and wind energy) and used fuel cells and batteries to keep the system working if any sources (solar radiation or wind energy) were interrupted. This system has the ability to operate independently and in different climatic conditions such as cloudy weather and makes it a destination for the use of people in remote areas (Fathabadi, 2017). Another hybrid system consisting of a conventional distillation system (conventional still) and a photovoltaic cell system has been studied. The system has been modified by adding a condenser, which improves the efficiency of the system. The results of the research have been compared and supported by other similar theoretical and experimental research. Some factors have been studied their effects on the system performance in terms of efficiency and productivity. Some of these factors are based on system design such as the installation of fins

on the back of the condenser or through certain weather factors such as the intensity of solar radiation and wind speed (Al-Nimr and Al-Ammari, 2016). The performance of solar still integrated with thermoelectric module immersed in the still basin has been investigated by Al-Nimr and Qananba (2018).

Some of these hybrid systems have focused on the use of concentrated solar energy as a new area of research and their promising applications in the field of energy. Another hybrid system consisted of a photovoltaic system and a concentrated solar system had been studied. This type was highly efficient due to the rapid improvement in both systems over the past five years. Several modifications have been introduced to this system, which have improved its performance through the use of high-temperature heat exchangers, high-temperature solar cells and spectral beam filters (Ju et al., 2017). A dual system combining a solar collector and thermoelectric generator also was designed under concentrated solar conditions. This system has been improved by an innovative idea of applying the effect of evaporative cooling on the cold surface of the thermoelectric generator to increase the temperature difference, which will increase the efficiency of this system to 19% in the case of focus ratio 20 suns. In the case of the effect of evaporative cooling, this system was more stable than the forced convection application. Several factors have been studied on this system performance (such as relative humidity and water flow ratio) (Al-Nimr et al., 2017).

Some other studies and researchers have focused on the behavior of solar stills under different modifications and parameters such as adding nanoparticles, using storage materials and phase change materials, design dimensions, depth of basin water, implemented reflectors and implemented condenser.

A numerical study was conducted on stepped solar still by adding nanofluid to it and studying its effect on improving system performance and its productivity. Where the sensitivity of productivity per hour was studied according to the height and length of the steps. An optimization

![](./images/813021386942447616_1.jpg)

Fig. 1. A graphical sketch of the hybrid solar system; (a) the system structure and its components, (b) the processes of energy transfer.

analysis was also performed by using the surface response method to obtain the best design for the solar still. Results showed that the system improved its productivity per hour by 22% when the concentration of nanofluid increased from 0% to 5% (Rashidi et al., 2018). An experi- mental study of the effect of high thermal conductivity sensible storage materials on thermal performance of a single basin solar still in the same weather conditions. The high thermal conductivity sensible sto- rage materials act as an alternative source of energy when solar ra- diation is low and graphite is one of the best materials. The resultsshowed that the daily output of the modified solar still was $7.73 l / m^{2}$  while it was $4.41 l / m^{2}$ in the traditional solar still. The efficiency of the modified solar still was 59.9-60.54% while it was 33.41-34.6% in the traditional solar still (Kabeel et al., 2018a,b).

In another experimental study, the effect of adding PCMs to solar still connected to a solar collector was studied. The effect of basin water level, circulation of the hot water flow rate, and flow rate of cooling water was studied on the productivity of the solar still. The results showed that the productivity of the system increased with the increase in ambient temperature and the increase in the circulation of the hot water flow rate. And the rate of productivity of the solar still was4300 ml / day, where $40 \%$ was produced after the sunset (Al-harahsheh et al., 2018). In another study, a comparison has been done of different PCMs to study its effect on the conventional solar still. The most ef- fective properties were chosen to investigate the system performance, such as organic and inorganic PCMs and their thermos-physical prop- erties and the melting temperature. Also, a feasibility study has been conducted on all PCMs used in the system to achieve the best selection of material for higher productivity and lower cost. The results show that both the organic PCM capric-palmic and organic PCM A48 have high productivity and low cost and increasing the thickness of PCMs does not have a positive effect on the productivity of the system, so small thickness is required to achieve lower cost (Kabeel et al., 2018a,b).

Solar stills are still some of the low-water productivity devices that have not been studied for marketing. For this reason, many researchers are seeking to develop them in various ways, making them perform better so that they are traded as a commercial product. The results of different studies showed the possibility to improve the performance of the solar still through the use of energy storage materials, fins and multi-basin. As the use of energy stored materials is useful in the con- tinuation of the work of the still even after the absence of solar radia- tion to keep its production of water exists. The presence of fins is useful for increasing the contact surface of the water, which facilitates the process of heat transfer leading to increase the productivity of water. The use of several basin raises the water temperature by the latent heat of the condensation, leading to increase productivity. If all of the above applications are applied in the manufacture of the solar stills, then it will be possible to market it as a commercial product for the production of potable water, whether residential or industrial sector (Panchal and Mohan, 2017). Another study tried to improve the performance of solar stills through the use of nanofluids in the heat exchanger and predict the system's productivity of water and efficiency and efficiency of en- ergy use in the system. The temperature of the nanofluids rises in the flat plate collectors and moves to heat exchanger connected to the still to raise the saline water temperature in the solar still. This system has been studied under the influence of many factors such as the use of nanoparticles of different sizes, different water depths at different flow rates of nanofluids and different climatic conditions. After studying many different climate factors and their impact on the system, it showed that the intensity of solar radiation was the most influential on the system (Mahian et al., 2017).

Some other researchers have applied and investigated the thermo- electric phenome. An experimental study of the asymmetrical solar still which was designed and tested under weather conditions in the summer was studied. The effect of the thermoelectric cooler (TEC) on the per- formance and the productivity of the system was investigated. The re-sults showed that despite the small surface area of TEC, which was 2.8times smaller than the surface area of the glass, its productivity was 3.2 times higher (Rahbar and Asadi, 2016). In another application, the thermoelectric module was used to design an inexpensive pyranometer. The thermoelectric module is dependent on the intensity of solar ra- diation, the temperature of the surrounding, the characteristic of the thermoelectric module, radiation and convection coefficients, and de- sign dimensions. The results showed that the output voltage depends on the intensity of the solar radiation as two correlations were adopted with $10 \%$ accuracy to predict the solar radiation intensity in terms of the output voltage and ambient temperature (Esfahani et al., 2011).

In this paper, a hybrid system will be discussed in the process of producing potable water through the distillation of saline water and the production of electric power. The process of producing potable water is through the process of distillation, which occurs in a solar still. The production of electric energy is carried out through the built-in ther- moelectric generator and photovoltaic cells in the solar still system. The system consists of a solar still with single basin and connected to a condenser, solar reflectors, photovoltaic cells immersed in the water basin and in the bottom of the basin installed thermoelectric generators. This system was studied theoretically through computer simulations by MS Excel Solver software. The innovation in this system is to integrate thermoelectric module in the water basin which no one has done this before. This process increases the power generation of the system and improve the performance of the solar still which makes it economically feasible. The effects of many factors on this system were also studied, whether they were design parameters such as adding condenser or environmental parameters such as the intensity of solar radiation, ambient temperature, and wind speed.

2. Model description
Fig. 1 shows the components of the hybrid system to be studied in this paper. This system consists of a traditional solar still modified with an external condenser on its back and a model of photovoltaic cells submerged in the still water basin. Under these cells, the electrothermal generator model formed the bottom of the basin. Solar radiation is the engine of this system and its fuel, which enters through the transparent glass cover of the solar still to the basin containing saline water and photovoltaic cells and thermoelectric generators. Sun rays fall directly on the saline water and photovoltaic cells to raise the first temperature and being absorbed by the second to generate electricity. The high temperature of the saline water causes the evaporation process to start. The water vapor rises from the surface of the water. The water eva- porates in the evaporation chamber so that some of it will condense on the inner surface of the still and what left will diffuse into the con- denser. Photovoltaic cells absorb the solar radiation falling on them to convert part of it into electrical energy and the remaining transfers into thermal energy in saline water contributes to raise the water tem- perature and reduce the temperature of the photovoltaic cells. The flow of heat from the basin water into the surrounding through the bottom of the basin, which contains the thermoelectric generators to generate electricity and put the rest of the thermal energy to the surrounding.

The condenser chamber contains a wall with fins constructed on both sides, facilitating the heat transfer process and improving the quality and performance of the system, which reduces the vapor pres- sure in the evaporating chamber. All walls of the solar still were iso- lated except for the wall of the condenser, the transparent glass cover and the base of the basin with the thermoelectric generators. This hy- brid system will be extensively studied and reacted to various factors and its impact on its water productivity, the efficiency of the still, the efficiency of the system and its rate of energy production.

3. Mathematical modeling
The theoretical analysis shows the steps in which the system is si- mulated with some changes. The actual area of the transparent glass

cover, which is the total area of the transparent glass cover and the finned wall instead of the transparent glass cover area, has been substituted. While the actual temperature of the surface, which is the average temperature for both the transparent glass cover and the finned wall instead of the transparent glass cover temperature, has been substituted.

In the beginning, many assumptions were put in place to build the theoretical analysis of this proposed system, which would clarify and deepen the precise understanding of the system, especially through the energy transference processes described in the proposed system:

- Considering the mathematical model works under the steady state conditions.
- The mathematical model is based on the fact that the water depth is not more than 20 cm (which is relatively small), which it is considered the temperature of the upper surface is equal to the temperature of the bottom surface.
- All the walls of the solar still have been isolated except for the transparent glass cover, the finned wall and the bottom of the basin, which represents the thermoelectric generator model.
- Tilt the transparent glass cover at the top of the solar still at a relatively low angle.
- The transparent glass cover in the solar still has a small thickness.

In Fig. 1, as described, saline water will be considered as the first system, and energy balance equations can be derived as follows:

$$\dot{E}_{i n, 1}-\dot{E}_{o u t, 1}-\dot{E}_{g e n, 1}=0 \tag{1}$$

$$\dot{E}_{i n, 1}=Q_{S, p v}+Q_{S, w} \tag{2}$$

$$Q_{S, p v}=\tau_{g} \tau_{w} G A_{p v} \tag{3}$$

$$Q_{S, w}=\tau_{g} \alpha_{w} G A_{w} \tag{4}$$

$$\dot{E}_{o u t, 1}=Q_{c, w g}+Q_{r, w g}+Q_{e v, w g}+Q_{h} \tag{5}$$

$$\dot{E}_{g e n, 1}=\eta_{p v} Q_{S, p v} \tag{6}$$

Solar radiation falls on the solar still through the transparent glass cover, so that saline water absorbs part of the radiation energy, while the other part is absorbed by photovoltaic cells. Eq. (1) represents the energy balance equation of the first system. Eq. (2) represents the energy entering the system, which is the total energy that both saline water and photovoltaic cells absorbed, and their absorption of energy represented respectively in Eqs. (3) and (4). While Eq. (5) represents the energy out of the system and is composed of four extremes represented by the heat transfer of convection, radiation, evaporation, and energy moving to the bottom of the water basin containing the hot side of the thermoelectric generator model. Eq. (6) represents the electrical energy generated by photovoltaic cells, which are part of the first system.

First, the convection rate is represented in Eq. (7), where the transference from saline water to transparent glass ($Q_{c, w g}$) (Zurigate and Abu-Arabi, 2004).

$$Q_{c, w g}=h_{c, w g} A_{w}\left(T_{w}-T_{g, e}\right) \tag{7}$$

where $h_{c, w g}$ is given by (Dunkle, 1961),

<table>
<caption>Table 1<br>Simulation assumptions of the proposed solar still system.</caption>
<thead>
<tr>
<th>Parameters</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Saline water surface area ($A_{w}$)</td>
<td>1.2 m²</td>
</tr>
<tr>
<td>Transparent glass cover area ($A_{g}$)</td>
<td>1.3 m²</td>
</tr>
<tr>
<td>Base area of the finned condenser wall ($A_{b,f}$)</td>
<td>0.6 m²</td>
</tr>
<tr>
<td>All constructed fins surface area of condenser ($A_{c}$)</td>
<td>1.8 m²</td>
</tr>
<tr>
<td>Surface area of the array of thermoelectric generators ($A_{cf}$)</td>
<td>1.2 m²</td>
</tr>
<tr>
<td>Transitivity of the glass cover($\tau_{g}$)</td>
<td>0.79</td>
</tr>
<tr>
<td>Transitivity of the glass cover($\tau_{w}$)</td>
<td>0.9</td>
</tr>
<tr>
<td>Transparent glass cover absorptivity ($\alpha_{g}$)</td>
<td>0.21</td>
</tr>
<tr>
<td>Saline water absorptivity ($\alpha_{w}$)</td>
<td>0.05</td>
</tr>
<tr>
<td>Emissivity of the glass cover ($\varepsilon_{g}$)</td>
<td>0.8</td>
</tr>
<tr>
<td>Emissivity of the saline water($\varepsilon_{w}$)</td>
<td>0.8</td>
</tr>
<tr>
<td>Thermal conductivity of basin ($K_{b}$)</td>
<td>0.0351 W/m °C</td>
</tr>
<tr>
<td>Thickness of water basin ($L_{b}$)</td>
<td>0.005 m</td>
</tr>
<tr>
<td>Heat transfer coefficient by convection of summer season ($h_{c,b-w}$)</td>
<td>612 (W/m² °C)</td>
</tr>
<tr>
<td>Summation of convective and radiative heat transfer coefficients of TEMs ($h_{t,c-a}$)</td>
<td>5.7 (W/m² °C)</td>
</tr>
<tr>
<td>Ambient temperature ($T_{a}$)</td>
<td>(10–35) °C</td>
</tr>
<tr>
<td>Wind speed (V)</td>
<td>(1–10) m/s</td>
</tr>
<tr>
<td>Solar intensity (G)</td>
<td>(100–1000) W/m²</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Simulation inputs of a commercial thermoelectric module (Bitschi, 2009).</caption>
<thead>
<tr>
<th>Parameters</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Averaged value of Seebeck coefficient</td>
<td>$\bar{\alpha}=3.47 × 10^{-4}$ V/K</td>
</tr>
<tr>
<td>Thermal conductivity</td>
<td>$\lambda_{p}=\lambda_{N}=0.97$ W/mK</td>
</tr>
<tr>
<td>Averaged value of electrical resistivity</td>
<td>$\sigma_{p}=\sigma_{N}=75.2 × 10^{3} PleaseCheck$</td>
</tr>
<tr>
<td>Leg lengths</td>
<td>$L_{p}=L_{N}=1.4$ mm</td>
</tr>
<tr>
<td>Legs cross section area</td>
<td>$A_{p}=A_{N}=19$ mm²</td>
</tr>
<tr>
<td>Insulator thickness</td>
<td>0.7 mm</td>
</tr>
<tr>
<td>Electrical conductor thickness</td>
<td>0.7 mm</td>
</tr>
<tr>
<td>Number of couples in each module</td>
<td>127</td>
</tr>
</tbody>
</table>

![](./images/813021386942447616_2.jpg)

Fig. 2. The flow chart of the model calculation.

![](./images/813021386942447616_3.jpg)

![](./images/813021386942447616_4.jpg)

Fig. 3. A graphical sketch of the hybrid solar system showing the system dimensions of (a) the still and (b) the back view of fins arrangement (cm).

$$
h_{c, w g}=0.884\left[T_{w}-T_{g, e}+\frac{\left(P_{w}-P_{g, e}\right)\left(T_{w}+273\right)}{268.9 \times 10^{3}-P_{w}}\right]^{\frac{1}{3}}
\tag{8}
$$

$$
P_{w}=\exp \left[25.317-\left(\frac{5144}{273+T_{w}}\right)\right]
\tag{9}
$$

$$
P_{g, e}=\exp \left[25.317-\left(\frac{5144}{273+T_{g, e}}\right)\right]
\tag{10}
$$

While the rate of heat transfer by radiation was expressed in Eq. (11), where heat transfer from saline to transparent glass $(Q_{r, w g})$ (Incropera et al., 2011).

$$
Q_{r, w g}=h_{r, w g} A_{w}\left(T_{w}-T_{g}\right)
\tag{11}
$$

$$
h_{r, w g}=\varepsilon_{e f f} \sigma\left[\left(T_{w}+273\right)^{2}+\left(T_{g}+273\right)^{2}\right]\left[\left(T_{w}+273\right)+\left(T_{g}+273\right)\right]
\tag{12}
$$

$$
\varepsilon_{e f f}=\frac{1}{\left(1 / \varepsilon_{g}\right)+\left(1 / \varepsilon_{w}\right)-1}
\tag{13}
$$

The rate of heat transfer by evaporation from saline water to transparent glass cover is shown in Eq. (14) $(Q_{e v, w g})$ (Zurigate and Abu Arabi, 2004). The heat transfer coefficient for evaporation is shown in Eq. (15) $(h_{e v, w g})$ (Kumar and Tiwari, 1996).

$$
Q_{e v, w g}=h_{e v, w g} A_{w}\left(T_{w}-T_{g, e}\right)
\tag{14}
$$

$$
h_{e v, w g}=16.273 \times 10^{-3} \times h_{c, w g} \times\left[\frac{P_{w}-P_{g, e}}{T_{w}-T_{g, e}}\right]
\tag{15}
$$

In Fig. 1, as shown, the actual surface of the transparent glass cover will be considered as the second system, through which energy balance equations can be derived as follows:

$$
\dot{E}_{i n, 2}-\dot{E}_{o u t, 2}=0
\tag{16}
$$

$$
\dot{E}_{i n, 2}=\alpha_{g} G A_{g}+Q_{c, w g}+Q_{r, w g}+Q_{e v, w g}
\tag{17}
$$

$$
\dot{E}_{o u t, 2}=Q_{c, g a}+Q_{r, g a}
\tag{18}
$$

The extremes of heat transfer in Eq. (18) represented by convection and radiation heat transfer will be illustrated as follows: The convective

![](./images/813021386942447616_5.jpg)

Fig. 4. The effect of solar radiation on (a) still distillation rate, (b) still efficiency, (c) system efficiency (d) power output of the system at 5 m/s wind speed and different ambient temperature.

heat transfer rate is represented by Eq. (19), where the heat transfer is carried out from the actual area of the transparent glass cover to the surrounding ($Q_{c,ga}$). The convection heat transfer coefficient is shown in Eq. (20) (Zurigate and Abu-Arabi, 2004).

$$
Q_{c,ga} = h_{c,ga}A_{g,e}(T_{g,e}-T_{a}) \tag{19}
$$

$$
h_{c,ga} = 2.8 + (3.0 \times V) \tag{20}
$$

The rate of heat transfer by radiation is represented in Eq. (21), where the heat transfer is from the actual area of the transparent glass cover to the surrounding ($Q_{r,ga}$). The heat transfer coefficient is shown in Eq. (22) ($h_{r,ga}$) (Badran and Abu-Khader, 2006).

$$
Q_{r,ga} = h_{r,ga}A_{g}(T_{g,e}-T_{a}) \tag{21}
$$

$$
h_{r,ga} = \varepsilon_{g}\sigma\left[\frac{(T_{g,e} + 273)^4-(T_{sky} + 273)^4}{T_{g,e}-T_{a}}\right] \tag{22}
$$

And from Akhtar and Mullick (2007), the sky temperature ($T_{sky}$) is:

$$
T_{sky} = [0.0552 \times (T_{a} + 273)^{1.5}-273] \tag{23}
$$

Eq. (24) shows the actual temperature of the solar still, while Eq. (25) shows the actual area of the transparent glass cover of the solar still.

$$
T_{g,e} = \frac{T_{g}A_{g} + T_{a}A_{c}}{A_{g} + A_{c}} \tag{24}
$$

$$
A_{g,e} = A_{g} + A_{c} \tag{25}
$$

In Fig. 1, the cold surface of the thermoelectric generator model, which the thermal energy is transferred to the surrounding, will be considered as the third system where the energy balance equations can be derived as follows:

$$
\dot{E}_{in,3}-\dot{E}_{out,3} = 0 \tag{26}
$$

![](./images/813021386942447616_6.jpg)
![](./images/813021386942447616_7.jpg)

Fig. 5. The effect of wind speed on (a) still distillation rate, (b) still efficiency, (c) system efficiency (d) power output of the system at solar radiation of $600\ \text{W/m}^2$ and different ambient temperature.

$$\dot{E}_{in,3}=Q_c \tag{27}$$

$$\dot{E}_{out,3}=Q_{t,ca} \tag{28}$$

The rate of heat loss from the cold surface of the thermoelectric generator model to the surrounding is represented by Eq. (29) $(Q_{t,ca})$, which the heat transfer is carried out by convection and conduction and is represented by the total heat transfer coefficient $(h_{tt,ca}$ (as set out in Eq. (22) (Shukla and Sorayan, 2005; Tiwari, 2003)).

$$Q_{t,ca}=h_{tt,ca}A_{cf}(T_c-T_a) \tag{29}$$

$$h_{tt,ca}=\left(\frac{L_b}{K_b}+\frac{1}{h_{t,ca}}\right)^{-1} \tag{30}$$

where $h_{t,ca}$is taken as recommended by Watmuff et al. (1997) and Dehghan et al. (2015).

Using a thermodynamic analysis of the thermoelectric phenomena generated in the thermoelectric generator model, it will then be possible to determine the rate of heat transfer from and to the thermoelectric generator model by thermoelectric model parameters.

In the thermoelectric model, the total electrical resistance of the N pairs of thermoelectric semi-conductive legs is given in Eq. (31), which are connected in series, while the total thermal conductivity of N pairs of thermoelectric semi-conductive legs is given in Eq. (32), which are connected in parallel (Bitschi, 2009).

$$R=n\cdot\left[\left(\sigma_p\cdot\frac{A_p}{L_p}\right)^{-1}+\left(\sigma_N\cdot\frac{A_N}{L_N}\right)^{-1}\right] \tag{31}$$

$$K=n\cdot\left[\left(\lambda_p\cdot\frac{A_p}{L_p}\right)+\left(\lambda_N\cdot\frac{A_N}{L_N}\right)\right] \tag{32}$$

The heat transfer rate absorbed by the hot-side of the thermoelectric

# POWER OUTPUT OF PV VS. WIND SPEED

![](./images/813021386942447616_8.jpg)

# POWER OUTPUT OF TEMS VS. WIND SPEED

![](./images/813021386942447616_9.jpg)

Fig. 6. The effect of wind speed on (a) power output of PV system and (b) power output of TEMs module at solar radiation of 600 W/m² and different ambient temperature.

generator model and the heat transfer rate from the cold-side of the thermoelectric generator model respectively are expressed in Eqs. (33) and (34) (Bitschi, 2009; Manikandan and Kaushik, 2015).

$$
Q_{h}=n \cdot \alpha T_{h} \cdot I+K \cdot\left(T_{h}-T_{c}\right)-\frac{1}{2} I^{2} R
\tag{33}
$$

$$
Q_{c}=n \cdot \alpha T_{c} \cdot I+K \cdot\left(T_{h}-T_{c}\right)+\frac{1}{2} I^{2} R
\tag{34}
$$

From Bitschi (2009) and Manikandan and Kaushik (2015), the power output of the solar still system is:

$$
P_{L}=Q_{h}-Q_{c}=I^{2} R_{L}
\tag{35}
$$

The following equations will be substituted: (2)-(15) into Eq. (1), (17)-(23) into Eqs. (16) and (27)-(30) into Eq. (26). So, three non-linear equations of the previous systems with three unknown variables (Tw, Tg, and Tc). Excel software was used to solve these equations numerically and also explained the effect of many factors on the performance of the solar still such as the ambient temperature, the intensity of solar radiation, the condensing chamber and wind speed.

From Al-Nimr and Dahdolan (2015a,b), the distillation rate of the solar still system is:

$$
\dot{m}=\frac{Q_{e v, w g}}{i_{f g, w}}
\tag{36}
$$

Finally, the still and system efficiency of the solar still system are (see Fig. 2):

$$
\eta_{\text {still }}=\frac{Q_{e v, w g}}{G A_{w}-\left(P_{L}+\dot{\mathrm{E}}_{\mathrm{gen}, 1}\right)}
\tag{37}
$$

$$
\eta_{\text {system }}=\frac{Q_{e v, w g}}{G A_{w}}+\frac{P_{L}}{G A_{b}}+\frac{\dot{\mathrm{E}}_{\mathrm{gen}, 1}}{G A_{P V}}
\tag{38}
$$

$$
P_{\text {output }}=\dot{\mathrm{E}}_{\text {gen, } 1}+P_{L}
\tag{39}
$$

Tables 1 and 2, and Fig. 3 contain all the assumptions used for simulating the proposed system. The weather conditions for summer in Jordan have been adopted to be applied in this system, whether the degree of ambient temperature or wind speed or the intensity of solar radiation.

## 4. Results and discussion

### 4.1. The intensity of solar radiation and its impact on the system

The intensity of solar radiation is one of the most important factors affecting the systems of solar distillation and we have shown previously that some of the results of studies have proved to be one of the most influential factors on solar stills. Fig. 4 shows the effect of solar radiation intensity on the distillation rate, the power produced, the still efficiency and the efficiency of the system when the wind speed is 5 m/s and different ambient temperatures.

In Fig. 4(a), it is clear that the rate of distillation in the system increases with the increase in the intensity of solar radiation due to the increase of energy entering the system, which increases the temperature of the saline water, thus facilitating the evaporation process. The graph shows the effect of ambient temperature, which shows its effect on the system and distillation in particular, as it is clear that the higher the ambient temperature, the greater the rate of distillation, applied in the same weather conditions of the intensity of solar radiation and wind speed.

When the solar radiation increases from 100 to 1000 W/m² and the ambient temperature varies from 10 to 35 °C, the water distillation, still efficiency, system efficiency, and power output will be increased from 0.3 to 8.8 kg/day, 12 to 50%, 23 to 70%, and 13 to 131 W, respectively. In conclusion, when the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, and system efficiency will be increased up to 27%, 21%, and 28% respectively, but the power output will be decreased up to 16.6% at solar radiation of 1000 W/m².

From Fig. 4(b) and (c), it is clear that the efficiency of the still and the entire system increases with increasing solar radiation intensity due to the increase of energy entering the system. The increase of the saline water temperature increases the efficiency of the still, facilitating evaporation, which improves the performance of the solar still. The increased efficiency of the system is due to the increased efficiency of the still and the increase of the power produced by photovoltaic cells and thermoelectric generator model. The graph shows the effect of ambient temperature, which shows how it affects the entire system generally and the efficiency of the still and the system particularly. As it is clear that the higher ambient temperature, the more efficient still and system, applied in the same weather conditions of the intensity of solar radiation and wind speed.

From Fig. 4(d), it is clear that electricity production increases with


![](./images/813021386942447616_10.jpg)

![](./images/813021386942447616_11.jpg)

![](./images/813021386942447616_12.jpg)

![](./images/813021386942447616_13.jpg)

Fig. 7. The effect of different designs of solar still on (a) still distillation rate, (b) still efficiency, (c) system efficiency (d) power output of the system at 5 m/s wind speed and variant solar intensities.

increasing solar radiation intensity due to the increase of energy entering the system. Increasing the intensity of solar radiation leads to an increase in the energy absorbed by the photovoltaic cells leading to an increase of the power produced. The intensity of solar radiation has an indirect effect on thermoelectric generators. As the increase in the intensity of solar radiation raises the temperature of saline water in the basin, which the thermoelectric generator model forms the bottom of the basin, leading to increasing the power produced. The graph shows the effect of ambient temperature, which shows its effect on the system and on the power produced generally, as it is clear that the higher the ambient temperature, the lower the power production, applied in the same weather conditions of solar radiation and wind speed, due to the high temperature of photovoltaic cells and thermoelectric generators, which reduce their efficiency.

### 4.2. Wind speed and its impact on the system

Wind speed is one of the most important factors affecting solar distillation systems. We have already shown that some of the results of the studies have proved how they affect the solar still system. Fig. 5 shows the effect of wind speed on the distillation rate, the power produced, the still efficiency and system efficiency when the solar radiation intensity is $600\ \text{W/m}^2$ and different ambient temperatures.

In Fig. 5(a), it is clear that the rate of distillation of the system decreases with the increase in wind speed. This is due to the increase in the rate of energy lost as the wind speed increases by the forced convection, which is one of the most efficient ways of transferring energy. The increase in wind speed increases the difference in temperature between the saline water and transparent glass cover, facilitating their loss of energy to the surrounding. The graph shows the effect of the ambient temperature, which shows how it affects the system generally and distillation particularly, as it is clear that the higher the ambient temperature, the higher rate of distillation in the system, applied in the same weather conditions of the intensity of solar radiation and wind speed.

From Fig. 5(b) and (c), it is clear that the efficiency of the still and the entire system decreases with the increase in wind speed. This is due to the increase in the rate of energy lost as the wind speed increases by the forced convection, which is one of the most effective methods of transferring energy. The drop in the efficiency of the still is due to the

![](./images/813021386942447616_14.jpg)

Fig. 8. The effect of different designs of solar still on (a) power output of PV system and (b) power output of TEMs module at 5 m/s wind speed and variant solar intensities.

increase of the lost energy as the wind speed increases. As the increase in wind speed increases the temperature difference between saline water and transparent glass cover, facilitating the loss of energy to the ambient. The graph shows the effect of ambient temperature, which shows how it affects the system generally and the efficiency of the still and the system particularly. As it is clear that the higher the ambient temperature, the greater the efficiency of the still and the system, applied in the same weather conditions of the intensity of solar radiation and wind speed.

From Fig. 5(d), it is clear that the output of electric power decreases with the increase in wind speed due to the increase in the rate of energy lost as the wind speed increases. The drop of energy produced is due to the increase of the energy loss as the wind speed increases. As the increase in wind speed increases the temperature difference between saline water and transparent glass cover, facilitating the energy loss to the surrounding. The graph shows the effect of ambient temperature, which shows the effect on the system and the product of electric power, as it is clear that the higher the ambient temperature, the lower productivity of generated power, applied in the same weather conditions of solar radiation and wind speed.

When the wind speed increases from 1 to 10 m/s and the ambient temperature varies from 10 to 35 °C, the water distillation, still efficiency, system efficiency, and power output will be decreased from 5.8 to 2.8 kg/day, 50 to 24%, 79 to 41%, and 94 to 70.5 W, respectively. In conclusion, when the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, system efficiency, and power output will be decreased up to 37%, 32%, 34%, and 17%, respectively, at wind speed of 10 m/s.

In Fig. 6, the effect of wind velocity on the produced electrical power of photovoltaic cells and thermoelectric generators will be illustrated. As mentioned above, increasing wind speed increases the temperature difference between saline water and transparent glass cover, thus facilitating its loss of energy to the surrounding. This decrease in temperature within the system will improve the efficiency of photovoltaic cells and their product of electrical power and, conversely, the higher the temperature the less efficient. While affecting the drop in the temperature of the system negatively on the thermoelectric generators. The higher the system temperature, the less system efficiency and less power produced. Overall, and from the figure, we will notice that the biggest decline in the electric power produced is in the thermoelectric generators, so it is the dominant of the low system production of power.

### 4.3. Add the condensation chamber and its effect on the system

In this section, three different designs of solar stills have been studied. The difference is in the condition of the condensation chamber. In the first design, the still system was built without the condensation chamber, as in conventional stills. In the second design, a condensing chamber was added to the still system. In the third design, a condensing chamber was added to the still system with a finned wall. Fig. 7 shows the effect of each of these different designs on the distillation rate, the power produced, the efficiency of the still and the system efficiency when the wind speed is 5 m/s and the intensity of the solar radiation is different.

The process of heat loss in previous designs varies in their quantity and quality. Where the heat loss of the first design only through the transparent glass cover while in the second design is made by the glass cover in addition to the condensation chamber, while the third design has been reinforced by a finned wall to support the process of heat transfer with the surrounding medium. The presence of condenser in the design of the still improves the performance of the solar still, as it facilitates the exchange of heat with the surrounding environment to lead the system to better stability. The presence of the condenser helps to reduce the pressure caused by the evaporation process in the water evaporation chamber and prevent the process of re-condensation of the water before reaching the place of collection and reduce the amount of water evaporated from the surface of saline water in the basin due to pressure evaporated water in the evaporation chamber. From the diagram, we can see that the condenser with the finned wall is the best in terms of the distillation rate and the efficiency of the still and the system. On the contrary, Fig. 7 shows that the conventional still produces electricity more than other designs and in Fig. 8 this will be explained.

When the solar radiation increases from 100 to 1000 W/m² for three different designs of solar still. In the first design, the conventional still, the water distillation, still efficiency, system efficiency, and power output will be increased from 0.2 to 6.8 kg/day, 20 to 35%, 35 to 57%, and 18 to 126 W, respectively. While in the second design, solar still with a condensing chamber, the water distillation, still efficiency, and system efficiency will be higher than the first design up to 7%, 8%, and 7% respectively, but the power output will be decreased up to 3% at solar radiation of 1000 W/m². And in the third design, solar still with a

<table>
<caption>Table 3 Comparisons of different theoretical and experimental studies for single basin solar still.</caption>
<thead>
<tr>
<th>No.</th>
<th>Other works</th>
<th>Weather conditions</th>
<th>Daily yield of other works & Still Efficiency</th>
<th>Daily yield of the proposed work & Still Efficiency</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Al-Nimr and Al-Ammari (2016)</td>
<td>Solar radiation of 1000 W/m²<br>Wind velocity of 2 m/s<br>Ambient temperature of 30 °C</td>
<td>7.6 kg/m²/h<br>58.2%</td>
<td>8.28 kg/m²/h<br>57.3%</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Solar radiation of 200 W/m²<br>Wind velocity of 20 m/s<br>Ambient temperature of 10 °C</td>
<td>0.7 kg/m²/h<br>26.8%</td>
<td>0.59 kg/m²/h<br>17.26%</td>
</tr>
<tr>
<td>2</td>
<td>Medugu and Ndatuwong (2009)</td>
<td>Solar radiation of 1238 W/m²<br>Wind velocity of 3.40 m/s<br>Ambient temperature of 31.6 °C</td>
<td>1.5942 kg/m²/h<br>85.49%</td>
<td>1.67 kg/m²/h<br>84.60%</td>
</tr>
<tr>
<td>3</td>
<td>El-Sebaii et al. (2009)</td>
<td>Solar radiation up to 900 W/m²<br>Wind velocity of 5.1 m/s<br>Ambient temperature of 30 °C</td>
<td>4.998 kg/m²/day</td>
<td>5.117 kg/m²/day</td>
</tr>
<tr>
<td>4</td>
<td>Abdullah (2013)</td>
<td>Solar radiation 1000 W/m²<br>Wind speed up to 3.5 m/s<br>Ambient temperature from 27 to 35 °C</td>
<td>3.350 l/m²/day</td>
<td>3.825 l/m²/day</td>
</tr>
<tr>
<td>5</td>
<td>El-Bahi and Inan (1999)</td>
<td>Solar radiation 1000 W/m²<br>Ambient temperature up to 40 °C</td>
<td>8 kg/m²/day</td>
<td>7.809 kg/m²/day</td>
</tr>
<tr>
<td>6</td>
<td>Fath (1996)</td>
<td>Solar radiation 1000 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>10.7 kg/m²/day</td>
<td>9.703 kg/m²/day</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Solar radiation 900 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>7.9 kg/m²/day</td>
<td>7.662 kg/m²/day</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Solar radiation 700 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>5.8 kg/m²/day</td>
<td>5.682 kg/m²/day</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4 the advantage of different similar theoretical and experimental studies for single basin solar still.</caption>
<thead>
<tr>
<th>No.</th>
<th>weather conditions</th>
<th>Power generation of other works</th>
<th>Power generation of the proposed work</th>
<th>Overall efficiency of other works</th>
<th>Overall efficiency of the proposed work</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Solar radiation of 1000 W/m²<br>Wind velocity of 2 m/s<br>Ambient temperature of 30 °C</td>
<td>80 W</td>
<td>117.8 W</td>
<td>61.5%</td>
<td>79.6%</td>
</tr>
<tr>
<td></td>
<td>Solar radiation of 200 W/m²<br>Wind velocity of 20 m/s<br>Ambient temperature of 10 °C</td>
<td>18.6 W</td>
<td>31.8 W</td>
<td>33.6%</td>
<td>29.44%</td>
</tr>
<tr>
<td>2</td>
<td>Solar radiation of 1238 W/m²<br>Wind velocity of 3.40 m/s<br>Ambient temperature of 31.6 °C</td>
<td>0</td>
<td>132.3 W</td>
<td>85.49%</td>
<td>91.45%</td>
</tr>
<tr>
<td>3</td>
<td>Solar radiation up to 900 W/m²<br>Wind velocity of 5.1 m/s<br>Ambient temperature of 30 °C</td>
<td>0</td>
<td>107.7 W</td>
<td>–</td>
<td>65.12%</td>
</tr>
<tr>
<td>4</td>
<td>Solar radiation 1000 W/m²<br>Wind speed up to 3.5 m/s<br>Ambient temperature from 27 to 35 °C</td>
<td>0</td>
<td>114.45 W</td>
<td>–</td>
<td>66.9%</td>
</tr>
<tr>
<td>5</td>
<td>Solar radiation 1000 W/m²<br>Ambient temperature up to 40 °C</td>
<td>0</td>
<td>128 W</td>
<td>–</td>
<td>71.65%</td>
</tr>
<tr>
<td>6</td>
<td>Solar radiation 1000 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>0</td>
<td>121.24 W</td>
<td>–</td>
<td>70%</td>
</tr>
<tr>
<td></td>
<td>Solar radiation 900 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>0</td>
<td>104.6 W</td>
<td>–</td>
<td>68.4</td>
</tr>
<tr>
<td></td>
<td>Solar radiation 700 W/m²<br>Ambient temperature from 30 to 40 °C</td>
<td>0</td>
<td>84.2 W</td>
<td>–</td>
<td>66.6</td>
</tr>
</tbody>
</table>

finned condensing chamber, the water distillation, still efficiency, and system efficiency will be higher than the first design up to 14%, 12.5%, and 11% respectively, but the power output will be decreased up to 6% at solar radiation of 1000 W/m².

Fig. 8 shows the effect of each of the three designs on the power produced by both photovoltaic cells and thermoelectric generators with the intensity of solar radiation. The results in Fig. 7 show that the conventional still exceeds the modified distillates in the power output.

If we look at Fig. 8, we will note that the photovoltaic cell production of power is higher in the modified stills than the conventional still slightly. Conversely, the power production of thermoelectric generators of conventional still is higher than the other modified stills, with a fairly good margin, which is the dominant reason for this simple rise in power production of conventional still. The presence of condenser reduces the temperature of saline water, which raises the productivity of stills and the power produced by photovoltaic cells. The higher temperature of

the photovoltaic cells, the less efficient and the power produced system. Conversely, the presence of the condenser and its reduction of the saline water temperature negatively affects the power production of the thermoelectric generators, which depend entirely on the high temperature of the submerged medium.

## 5. Comparison
All the applied conditions in the simulation system are the weather conditions of Jordan for the summer. Where the values vary of solar radiation intensity (100–1000 W/m²), wind speed (1–10 m/s) and ambient temperature (10–35 °C). The results of the simulation are recorded at the highest value at the intensity of solar radiation of 1000 W/m², wind speed of 5 m/s and ambient temperature of 35 °C, where the rate of distillation, efficiency of the still, system efficiency and power produced are 8.73 kg/day, 50.42%, 70%, 114.45 W, respectively. While the lowest values are recorded at the intensity of solar radiation of 100 W/m², wind speed of 5 m/s and ambient temperature of 10 °C, where the rate of distillation, efficiency of the still, system efficiency and power produced are 0.23 kg/day, 13.81%, 24.75%, and 15.68 W, respectively.

Table 3 has comparisons of different theoretical and experimental studies for single basin solar still which are similar to the proposed system. In the comparison of each system, the same weather conditions have been applied.

Table 4 has shown the advantages of the proposed system over different theoretical and experimental studies for single basin solar still which are similar to the proposed system. Most likely, the proposed system has advantages of power generation and higher overall efficiency which make the solar still economically feasible and consider as one of the valuable systems.

The efficiency of the thermoelectric generators in our study shows the compatibility with those researches which have studied many types of thermoelectric generators and the materials manufactured. Certainly, the efficiency of the thermoelectric generators varies depending on the materials manufactured and the difference of temperature on each side. There are many different materials that form these thermoelectric generators, which are still in the process of discovery and development. The most known materials that thermoelectric generator made of Bi2Te3, Sb2Te3, (BiSb)2Te3, and Bi2(TeSe)3 (Chen et al., 2016).

The efficiency of the thermoelectric generators of our proposed system at the best conditions is 5.12%, while the average efficiency was 3.47%. These results are consistent with the results of published studies, where the efficiency of 4.3% when the temperature difference on each side of the thermoelectric generators 15 °C (Jang et al., 2011; Chen et al., 2016). The temperature difference values on the thermoelectric generators sides of our system have reached 22 °C, thus showing this compatibility clearly.

In conclusion, to adopt the verification of the proposed work, the results of other similar works at specific conditions have been compared with the results of the proposed system at the same conditions which must be somewhat close. In comparison to the results of theoretical and experimental published studies, we can confirm the validity of what has been achieved in this research paper, since the results are close to each other at similar parameters that have been done by all systems.

## 6. Conclusion
Raising the efficiency of the solar still makes it marketable and available in the market for different uses. As it is an idea that has not been promoted or applied for reasons of low efficiency. There are many studies that have developed stills through hybrid systems that make them economically marketable. In this study, the still system is hybridized by two systems: the photovoltaic system and the thermoelectric generator system. This hybridization improves the efficiency of the still at its best conditions from 50.42% to 70% in addition to its production of electric power. The addition of the condenser also helps the solar still to improve its performance and increases the efficiency of both the still and the system and its water production. The system was studied theoretically through a mathematical model representing the system steady-state. The effects of many parameters such as the intensity of solar radiation, wind speed, ambient temperature and the design parameters were discussed. In general, increased solar radiation intensity and temperature improve the system performance and their relationship is positive while increasing wind speed negatively affects the performance of the still as its relationship is inverse.

In conclusion, when the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, and system efficiency will be increased up to 27%, 21%, and 28% respectively, but the power output will be decreased up to 16.6% at solar radiation of 1000 W/m². When the ambient temperature increases from 10 to 35 °C, the water distillation, still efficiency, system efficiency, and power output will be decreased up to 37%, 32%, 34%, and 17%, respectively, at wind speed of 10 m/s. Also, the water distillation, still efficiency, and system efficiency of the solar still with a condensing chamber will be higher than the conventional solar still up to 7%, 8%, and 7% respectively, but the power output will be decreased up to 3% at solar radiation of 1000 W/m². While in the third design, solar still with a finned condensing chamber, the water distillation, still efficiency, and system efficiency will be higher than the conventional solar still up to 14%, 12.5%, and 11% respectively, but the power output will be decreased up to 6% at solar radiation of 1000 W/m².

In comparison to the results of theoretical and experimental published studies. We can confirm the validity of what has been achieved in our research paper, since the values of the results are close to each other at the same parameters that have been done by all systems.

## Conflict of interest
The authors declared that there is no conflict of interest.

## References
Abdullah, A., 2013. Improving the performance of stepped solar still. Desalination 319, 60–65.

Akhtar, N., Mullick, S., 2007. Computation of glass-cover temperatures and top heat loss coefficient of flat-plate solar collectors with double glazing. Energy 32 (7), 1067–1074.

Al-harahsheh, M., Abu-Arabi, M., Mousa, H., Alzghoul, Z., 2018. Solar desalination using solar still enhanced by external solar collector and PCM. Appl. Therm. Eng. 128, 1030–1040.

Al-Nimr, M., Dahdolan, M., 2015a. Modeling of a novel concentrated PV/T distillation system enhanced with a porous evaporator and an internal condenser. Sol. Energy 120, 593–602.

Al-Nimr, M., Dahdolan, M., 2015b. Modeling of a novel concentrated solar still enhanced with a porous evaporator and an internal condenser. Sol. Energy 114, 8–16.

Al-Nimr, M., Qananba, K., 2018. A solar hybrid thermoelectric generator and distillation system. Int. J. Green Energy 1–16.

Al-Nimr, M., Al-Ammari, W., 2016. A novel hybrid PV-distillation system. Sol. Energy 135, 874–883.

Al-Nimr, M., Tashtoush, B., Khasawneh, M., Al-Keyyam, I., 2017. A hybrid concentrated solar thermal collector/thermo-electric generation system. Energy 134, 1001–1012.

Badran, O., Abu-Khader, M., 2006. Evaluating thermal performance of a single slope solar still. Heat Mass Transfer 43 (10), 985–995.

Bitschi, A., 2009. Modelling Of Thermoelectric Devices for Electric Power Generation.

Chen, W., Wu, P., Wang, X., Lin, Y., 2016. Power output and efficiency of a thermoelectric generator under temperature control. Energy Convers. Manage. 127, 404–415.

Dehghan, A., Afshari, A., Rahbar, N., 2015. Thermal modeling and exegeretic analysis of a thermoelectric assisted solar still. Sol. Energy 115, 277–288.

Dunkle, R., 1961. Solar Water Distillation. [Melbourne]: [C.S.I.R.O.].

El-Bahi, A., Inan, D., 1999. Analysis of a parallel double glass solar still with separate condenser. Renew. Energy 17 (4), 509–521.

El-Sebaii, A., Al-Ghamdi, A., Al-Hazmi, F., Faidah, A., 2009. Thermal performance of a single basin solar still with PCM as a storage medium. Appl. Energy 86 (7–8), 1187–1195.

Esfahani, A., Rahbar, N., Lavvaf, M., 2011. Utilization of thermoelectric cooling in a portable active solar still – an experimental study on winter days. Desalination 269 (1–3), 198–205.

Fath, H., 1996. High performance of a simple design, two effect solar distillation unit. Desalination 107 (3), 223–233.

Fathabadi, H., 2017. Novel standalone hybrid solar/wind/fuel cell/battery power generation system. Energy 140, 454-465.

Incropera, F.P.D., Dewitt, P., Bergman, T.L., Lavine, A.S., 2011. Principles of Heat and Mass Transfer. International Student Version, seventh ed. Wiley.

Jang, B., Han, S., Kim, J., 2011. Optimal design for micro-thermoelectric generators using finite element analysis. Microelectron. Eng. 88 (5), 775-778.

Ju, X., Xu, C., Hu, Y., Han, X., Wei, G., Du, X., 2017. A review on the development of photovoltaic/concentrated solar power (PV-CSP) hybrid systems. Sol. Energy Mater. Sol. Cells 161, 305-327.

Kabeel, A., Abdelgaied, M., Eisa, A., 2018. Enhancing the performance of single basin solar still using high thermal conductivity sensible storage materials.

Kabeel, A., El-Samadony, Y., El-Maghlany, W., 2018b. Comparative study on the solar still performance utilizing different PCM. Desalination 432, 89-96.

Kumar, S., Tiwari, G., 1996. Estimation of convective mass transfer in solar distillation systems. Sol. Energy 57 (6), 459-464.

Mahian, O., Kianifar, A., Heris, S., Wen, D., Sahin, A., Wongwises, S., 2017. Nanofluids effects on the evaporation rate in a solar still equipped with a heat exchanger. Nano Energy 36, 134-155.

Manikandan, S., Kaushik, S., 2015. Thermodynamic studies and maximum power point tracking in thermoelectric generator-thermoelectric cooler combined system. Cryogenics 67, 52-62.

Medugu, D., Ndatuwong, L., 2009. Theoretical analysis of water distillation using solar Still. Int. J. Phys. Sci. 4 (11), 705-712.

Nrel.gov, 2017. NREL's III-V Team Demonstrates Record Efficiency Dual-Junction Solar Cell | NREL. [online] Available at: < https://www.nrel.gov/news/program/2017/team-demonstrates-record-efficiency-dual-junction-solar-cell.html > (accessed 12 Oct. 2017).

Panchal, H., Mohan, I., 2017. Various methods applied to solar still for enhancement of distillate output. Desalination 415, 76-89.

Rahbar, N., Asadi, A., 2016. Solar intensity measurement using a thermoelectric module; experimental study and mathematical modeling. Energy Convers. Manage. 129, 344-353.

Rashidi, S., Bovand, M., Rahbar, N., Esfahani, J., 2018. Steps optimization and productivity enhancement in a nanofluid cascade solar still. Renew. Energy 118, 536-545.

Shukla, S., Sorayan, V., 2005. Thermal modeling of solar stills: an experimental validation. Renew. Energy 30 (5), 683-699.

Tiwari, G.N., 2003. Solar Energy, Fundamental, Design, Modeling and Applications, first ed. Narosa Publishing House, New Delhi.

Union of Concerned Scientists, 2017. Our Energy Choices: Energy and Water Use. [online] Available at: < http://www.ucsusa.org/clean-energy/energy-water-use#. WbDwUcgjHIU > (accessed 12 Oct. 2017).

Watmuff, J.H., Characters, W.W.S., Proctor, D., 1977. Solar and wind induced external coefficients for solar collectors. Cooperation Mediterraneenne pour l'Energie Solaire. Rev. Int. Heliotech. 2nd Quarter 56.

Zurigat, Y., Abu-Arabi, M., 2004. Modelling and performance analysis of a regenerative solar desalination unit. Appl. Therm. Eng. 24 (7), 1061-1072.