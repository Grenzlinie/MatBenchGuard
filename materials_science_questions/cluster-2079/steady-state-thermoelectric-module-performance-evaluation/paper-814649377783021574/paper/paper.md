Special Double Issue Article

Sebastian Schirrmacher*, Georg Ullmann and Ludger Overmeyer

# Thermoelectric Power Supply of Wireless Sensor Nodes in Marine Gearboxes

**Abstract:** This article presents a solution for the thermoelectric power supply of wireless sensor nodes for condition monitoring of marine gearboxes. Among the different ambient energy sources in marine gearboxes, frictional heat has been identified to be appropriate to thermally power a thermoelectric generator (TEG). The such generated electricity may power wireless sensor nodes for detecting temperature, vibration, torque and rotational speed. Requirements for a corresponding energy supply are formulated, constructive solutions are presented and thermal simulations and practical experiments are reviewed. The results are evaluated and a solution is selected for further implementation, which provides for an actively cooled TEG in the area of the ship gearbox's heat exchanger. This can provide continuous electrical power of up to 14 mW, thus supplying the planned sensor nodes. The disadvantage of this solution is that a comparatively extensive mechanical modification, for example, to the oil and cooling water pipelines is required.

**Keywords:** energy harvesting, thermoelectric generator, wireless sensor nodes, thermal simulation, condition monitoring

DOI 10.1515/ehs-2014-0044

## Introduction

The ship gearbox as shown in Figure 1 is of particular importance as a highly loaded element between diesel engine and propeller system, which ensures the reliability of the entire marine propulsion. Both from the economic and the safety point of view, very high requirements on the gearbox availability must be met. Against this background, the choice and implementation of an appropriate maintenance strategy gains great importance. The literature distinguishes between three strategies: (i) due to damage, (ii) depending on intervals and (iii) condition dependent (Eichler 1977; Silva 2005). Condition monitoring systems (CMSs) are the (information) technological and organizational framework for the implementation of the latter strategy.

The condition-based maintenance is already used in many industries as a standard method for machine monitoring. The aim is to increase the level of safety and machine availability while, at the same time, reducing maintenance costs (Wang and Gao 2006). In the marine environment, condition-based maintenance provides significant advantages. Certain components on board of a vessel are subject to regular inspection intervals, which are required by classification societies. The extension of inspection intervals is only granted if the machinery concerned is monitored with CMS, the crew is trained and the status data is regularly collected (Lösl 2006).

The disadvantages of existing CMS solutions (for a description, see Scharfetter 2007) are especially noticeable in very high cabling effort and the regular maintenance to replace the energy source in hard-to-reach areas of the ship gearbox. To avoid the mentioned disadvantages, the energy-autonomous sensor nodes record, for example, vibrations, temperature and torque and wirelessly transmit the measured data. The basis for such sensor nodes is an energy source independent from the on-board electrical system. With the help of energy harvesting, the sensor node converts energy from the ship gearbox environment into electrical energy to operate the sensors.

## Energy Sources in the Marine Gearbox

Energy harvesting is the suitable conversion of primary energy from the machine environment into electrical energy

*Corresponding author: Sebastian Schirrmacher, Department of Production Automation, IPH – Institut für Integrierte Produktion Hannover gGmbH, Hollerithallee 6, 30419 Hannover, Germany,
E-mail: schirrmacher@iph-hannover.de
Georg Ullmann: E-mail: ullmann@iph-hannover.de, Ludger
Overmeyer: E-mail: ludger.overmeyer@ita.uni-hannover.de,
Department of Production Automation, IPH – Institut für Integrierte Produktion Hannover gGmbH, Hollerithallee 6, 30419 Hannover,
Germany

![](./images/814649377783021574_1.jpg)

Figure 1: Marine gearbox, type WAF 665, weight 1,950 kg, rating 924–1,386 kW, maximum drive torque 7,353 Nm.
Source: REINTJES GmbH.

to power electric systems (Hudak and Amatucci 2008; Dembowski 2011; Moser 2012). Here, the primary energy can be kinetic in the form of vibrations, thermal in the form of temperature differences or as electromagnetic radiation (Penella and Gasulla 2007). To select a primary energy source suitable for the aforementioned application of energy-autonomous sensor nodes, preliminary investigations were carried out. These are briefly described below. Because the gearbox is located in the ship's hull, the use of electromagnetic radiation, e.g. from solar cells (Gessler and Krause 2009), is generally out of question and was not considered in the context of the investigations.

During the operation of the ship, vibrations are created in the gearbox, for example, through the meshing of the gears or other components of the drive train such as the engine. These vibrations can be converted into electrical energy via so-called kinetic harvesters usually based on spring-ground-damper systems (Spreemann et al. 2008). Characteristic for these systems is the resonance area that expresses the properties of spring, oscillating mass and damper in a discrete frequency. Sufficient energy can be harvested only in this resonance area. To verify the applicability of the kinetic harvester, vibrations in the vicinity of potential measurement points were recorded during different operating conditions of the vessel (e.g. in the form of varying travel speeds). Basically, amplitudes with potentially usable energy could be determined for all tested operating conditions. The corresponding frequencies varied, however, by more than 100 Hz. The use of kinetic harvesters with a discrete resonance frequency is therefore not possible for the safe operation of a sensor node when taking into account the strongly varying frequencies of the ship gearbox.

Another potential source of energy in the area of the ship gearbox environment exists in the form of heat. Frictional heat is generated during the operation of the gear wheels in the gearbox. With the help of supplied oil, the heat is transported away. The heated oil is fed back into a circuit and cooled with seawater in a heat exchanger. The hot oil causes gearbox surface temperatures of up to 70°C. The temperature of the seawater cooling varies with the location of the vessel. Usually this can be assumed to be from 10°C to 35°C. Because the cooling lines do not necessarily have to be located in the immediate vicinity of potential measurement points, the ambient temperature of 40°C can be made out as a further potential heat sink. The present differences in temperature are suitable for the use of thermoelectric generators (TEGs) (Moser 2012), which convert thermal energy into electrical energy using the Seebeck effect (Fahrner and Schwertheim 2009). Critical to the amount of generated voltage are the parameters of the TEG. The Seebeck coefficient of n- and p-doped thermolegs or the number of thermocouples which are connected in parallel, thermally and electrically in series influence the output voltage (Potje-Kamloth 2011; Nachtrab 2013).

This paper presents the use of TEGs as an energy source for wireless sensor nodes in marine gearboxes. Requirements for a corresponding energy supply are formulated, constructive solutions are presented and thermal simulations and practical experiments are reviewed. Finally, the results are evaluated and a solution is selected for further implementation.

# Requirements for Thermoelectric Energy Harvesting

The essential requirements for a wireless CMS were first identified in collaboration with a manufacturer of marine gearboxes. Subsequently, a wireless sensor node was designed. On this basis, the requirements for the thermoelectric energy supply could finally be derived.

## Requirements for a CMS for Marine Gearboxes

As a rule, the CMS should be used both in container ships, which work almost around the clock as well as

for private yachts with significantly lower operating hours. If it goes to the measurement of temperature, vibration, torque and rotational speed, a 15 min interval satisfies both applications. The recording of 8,000 measurement values is required for a reliable and meaningful signal analysis of the vibrations occurring. Furthermore, a single measurement of data sets of temperature, torque and rotational speed is required every 15 min. For the reasons mentioned in the introduction, the CMS should work completely wirelessly. The data volume for a vibration diagnosis can be determined using eq. [1]:

$$
\mathrm{V}=\left(\text { Resolution } \cdot f_{\text {Sample }} \cdot n_{\text {Channel }}\right) \cdot t
\tag{1}
$$

With a typical resolution of an analog/digital (A/D) converter of 16 bit, a sampling rate $f_{\text{Sample}}$ of 30 kilo samples per second, two channels $n_{\text{Channel}}$ for communication and a transmission time $t$ of 10 s, the data volume $V$ amounts 1.2 MB. With a data transmission rate of 160 kbaud and 8 use bits per symbol, it is possible to transfer the data volume in 7.5 s. The radio-transmission should be possible even if the sensor is assembled on the metal housing of the gearbox, while the transmitter and receiver should have a distance of not more than 1 m. Furthermore, the CMS must be able to withstand the harsh environmental conditions (moisture, oil, salt, vibrations, shocks) of the ship gearboxes.

## Design of a Sensor Node

The choice of a suitable vibration sensor was made based on the functional criteria of signal bandwidth, range, sensitivity as well as the necessary supply voltage and power consumption. The analysis of various A/D sensors justified the selection of a vibration sensor with a signal bandwidth of 1,600 Hz, a measurement range of up to 78 m/s², a sensitivity of 512 least significant bits (LSB) per acceleration of gravity $g=9.81$ m/s² as well as an adjustable input voltage of 2–3.6 V and a power consumption of 140 µA. The vibration sensor also features a small footprint, as well as an integrated temperature sensor. Suitable sensors were also selected for the measurement of speed and torque.

For the realization of the autonomous functionality of the sensor nodes, a smart central processing unit (CPU) must control and monitor the necessary processes. Various microcontrollers were analysed with regard to their electrical power input. The chosen microcontroller requires only 19 µW in the operational state and has sleep modes, which only require current in the nA-range. At the same time, the microcontroller has a frequency of 48 MHz, enabling the pre-processing of vibration data recorded directly on the sensor node.

A ferroelectric random access memory (FRAM) was provided with 2 Mbit memory to save the measurement data. All components are designed to operate at 3.3 V input voltage and were added to a sensor board with the necessary interfaces (e.g. to connect the power supply or other sensors) as shown in Figure 2.

The sensor board is housed in a casing, which functions as an antenna for data communication through the integration of radio-frequency identification (RFID). An active reader unit is connected to an available electrical system source. This allows saving of additional

![](./images/814649377783021574_2.jpg)

Figure 2: Sensor board.
Source: microsensys GmbH.

energy, because the sensor nodes do not have to actively operate during the data transfer. A total of two sensor nodes on a marine gearbox are intended for the realization of the measurement task.

## Requirements for the Thermoelectric Energy Supply

With an electrical power demand $P_{\text{Sensor}}$ of 50 mW, an operation time $t_{\text{operating}}$ of 10 s and a harvesting interval $t_{\text{harvesting}}$ of 15 min minus the operating time, the continuous power output $P_{\text{TEG}}$ of the energy harvesting system can be calculated as given in eq. [2]:

$$
P_{\text{TEG}} = \frac{P_{\text{Sensor}} \cdot t_{\text{operating}}}{t_{\text{harvesting}} \cdot \eta_{\text{PM}}}
\tag{2}
$$

Because of a small temperature difference in the marine gearbox, $\Delta T \leq 20^\circ\text{C}$, a power management is necessary to boost the generated voltage to a constant level. For a voltage input of $V_{\text{In}} < 1$ V the power management works with an efficiency $\eta_{\text{PM}}$ of 30%. According to the calculation, a power of $P_{\text{TEG}} = 2$ mW should be harvested continuously. Taking into consideration the electrical energy demand as well as the thermal and spatial conditions of the ship gearbox, the following requirements for the thermoelectric energy supply result:

R.1 An electrical power output of 2 mW should be provided continuously by the TEG for the 10 s of operation of two sensor nodes.

R.2 The functionality of the TEG should be ensured at the ambient temperatures $T_{\text{hot}} = 50$–$70^\circ\text{C}$ and $T_{\text{cold}} = 10$–$35^\circ\text{C}$.

R.3 The design of the TEG should be small and compact so that the volume does not exceed $250\ \text{cm}^3$.

R.4 Furthermore, easy installation should be possible taking into account a robust design against the harsh environmental conditions. The design should conform the IP69 standard according to DIN EN 60529 (Deutsches Institut für Normung e. V. 1991) to resist even a high-pressure cleaner.

## Energy-Autonomous Sensor Nodes – Current State of Research

The use and development of TEGs for the subsequent integration of the CMS is currently the subject of the research. Several investigations, which are relevant to the present application in marine gearboxes, are therefore briefly introduced.

Bartholomé et al. (2011) optimized the maintenance of an aircraft. The objective was the development and implementation of wireless and energy-autonomous monitoring systems for the monitoring of particularly heavy-load structures. TEGs were used, among other things, for supplying energy. These take advantage of the difference in temperature of $30^\circ\text{C}$ between the exterior of the aircraft and the cargo space and generate approximately 7 mW of continuous power. The ambient temperature of the aircraft has been identified as between $21.8^\circ\text{C}$ and $-50^\circ\text{C}$. Dilhac et al. (2014) also refer to the use of TEGs as an energy source for wireless sensor networks (WSNs) in aircraft as having great potential. These results are promising, but cannot be transferred directly to the application considered here, since the electrical performance of the selected TEG is temperature dependent and the temperature range available in marine transmission environment is around 10–$70^\circ\text{C}$ (see requirement R.2).

Wirth, Benecke, and Kravcenko (2012) designed a WSN for machine diagnosis in a paper mill. Here, a TEG was also used as an energy source which generates a maximum electrical output of 200 mW through the temperature difference between an engine at $58.7^\circ\text{C}$ and the ambient temperature of the room at $28^\circ\text{C}$. This allowed specific plant data to be transmitted wirelessly once daily. The dominant thermal boundary conditions in the paper mill are comparable to the application of the marine gearbox considered here. Accordingly, the relatively high electrical power of 200 mW promises to significantly exceed the power of 2 mW specified in requirement R.1. However, this is reached by the positioning of the TEG near an engine where forced convection is achieved by fan operation. In marine gearboxes, no auxiliary fans are integrated, which could force the convection in a similar manner.

Liu et al. (2000) realized an online monitoring system for diesel engines in a ship consisting of a particle detection in the lubricant, an analysis of the lubricant quality and a measurement of torque moment and rotation velocity. The detection of ferroparticles in the flow-back oil indicates wear from the cylinders and piston rings. Water leakages in the cylinders or fuel oil leakage can be detected by analysing some pollutants (including oxide, carbon laydown, water, etc.) of the lubricant. The shaft torque moment is regarded as a reference for judging the wear condition. Unfortunately the CMS has to be connected to the flow back oil pipe from the crankcase and a gear plate has to be fixed on the driving shaft. The electrical energy is taken from the board supply.

Kouremenos and Hountalas (1997) developed a method that can discover the current condition of a marine diesel engine and suggest whether a proper tuning or repair should be done. A pressure measurement of the cylinder and the fuel injection system is integrated in the diesel engine and connected to a computer for monitoring. The sensor node connected by wires to the monitoring system has to be integrated with specific adapters for each diesel engine.

The papers listed are designed for specific applications. The requirements of the energy harvesting vary with the electrical sensors to be operated and their measurement intervals. For this reason, a transfer of existing solutions is only conditionally possible. No reports on the application options in marine gearboxes are known of so far.

# Design Solutions
TEGs generate increasing voltage (Freunek 2010) with increasing temperature difference.

$$
U_{\text{Seebeck}} = \alpha \cdot n \cdot (T_{\text{hot}} - T_{\text{cold}}) \tag{3}
$$

Equation [3] shows that the generated voltage from a TEG depends on the Seebeck coefficient of the material $\alpha$, the number of thermocouples inside the TEG $n$ and the temperature difference across the thermocouples $T_{\text{hot}} - T_{\text{cold}}$.

Therefore, areas having high temperature differences are preferred for the placement of TEGs (see requirement R.2). In the area of the heat exchanger, the oil line and seawater cooling line pass each other in close proximity. However, no significant measurements can be performed in this area, since the distances to the components of the signal output (bearings, shafts and gears) are too long. To avoid the exclusion of the largest temperature difference, two fundamentally different design variants (A and B) were carried out below.

In the variants A-1 and A-2, the TEG is placed in the area near the heat exchanger in order to exploit the maximum temperature differences that can occur in the marine gearbox. While using the same TEG, the generated voltage increases proportional with the change in temperature difference (see eq. [3]). In addition to a wired connection between the TEG and the sensor nodes, these variants require an additional construction for the integration, resulting in a specific adjustment for each gearbox, which are shown in Table 1. A dummy plug in the temperature-controlled oil line offers the possibility to screw on an adapter, which provides a flat surface for the support of the TEG. The connection to the cooling water line is realized through hose connections. A spring-loaded punch is provided within the cooling water connection element to create the necessary contact pressure for the TEG.

In the variants B-1 to B-6, the surface of the ship gearbox in the immediate vicinity of the sensor positions serves as a heat source. Passive heat sinks are used. In contrast to variants A-1 and A-2, the temperature boundary conditions do not lead immediately to the temperature difference at the TEG surfaces. The passive heat sinks perform a heat exchange with ambient air, while their own temperature changes. To compare the different variants, the heatflow of the passive heat sinks is calculated using a thermal simulation. The main distinguishing feature is the size of the passive heat sink. A small and compact design with a volume requirement under $250\ \text{cm}^3$ is preferred in accordance with requirement R.3. The contacting of the TEG to the gearbox surface or the passive heat sink is realized with the help of the thermal conductive foil. In order to design the structure robustly (see requirement R.4) and to avoid a thermal bypass, the passive coolers are secured to the gearbox with plastic brackets.

Furthermore, the variants are distinguished with respect to the TEG used. On the one hand, the TEG 127-200-28 (manufacturer: thermalforce.de) was used, which withstands a maximum operating temperature of $200^\circ\text{C}$. In accordance with the manufacturer's instructions, at a temperature difference of $\Delta T=100^\circ\text{C}$, an electrical power of over 700 mW is reached. Also considering the thermal boundary conditions listed in the requirement R.2, this electrical power should be basically sufficient to realize the 2 mW required in requirement R.1. The TEG has a length of 30 mm, a width of 30 mm and a height of 4.8 mm and therefore should meet the installation space requirements (see R.3). The 127 thermocouples are based on p- and n-type bismuth-telluride and the module reaches a Seebeck coefficient of 0.056 V/K.

With regard to requirement R.3, a smaller alternative was also considered. The $\mu$-TEG TGP-651 (manufacturer: Micropelt GmbH) is operational up to a temperature of $100^\circ\text{C}$ and is only 15 mm long, 10 mm wide and 9.3 mm high. At a temperature difference of $\Delta T=30^\circ\text{C}$, an electrical power of over 5 mW is reached. Because the surface of the heat sink is sufficiently large enough, four $\mu$-TEGs are installed under each. The thermal connection to the hot and cold side is also done using thermal conductive foil. With up to 100 thermocouples of bismuth-telluride per $\text{mm}^2$ the module reaches a Seebeck coefficient of 0.060 V/K. The elaborate design variants are listed in Table 1.

Table 1: Developed design variants for the power supply of wireless sensor nodes. In the variants A-1 and A-2 the TEGs are placed between the heated oil line and a spring-loaded punch, which is connected to the cooling water line. The TEGs in the variants B-1 to B-6 are connected to three different passive heat sinks and the gearbox surface.

<table>
<thead>
<tr>
<th>Variant</th>
<th>Heat sink</th>
<th>TEG</th>
<th>Design</th>
</tr>
</thead>
<tbody>
<tr>
<td>A-1</td>
<td>![](./images/814649377783021574_3.jpg)<br>Cooling water line<br>90 x 50 x 75 mm</td>
<td>![](./images/814649377783021574_4.jpg)<br>TEG 127-200-28<br>30 x 30 x 4.8 mm</td>
<td>![](./images/814649377783021574_5.jpg)<br>Installation space: 544.5 cm³</td>
</tr>
<tr>
<td>A-2</td>
<td>![](./images/814649377783021574_6.jpg)<br>Cooling water line</td>
<td>![](./images/814649377783021574_7.jpg)<br>TGP-651<br>15 x 10 x 9.3 mm</td>
<td>![](./images/814649377783021574_8.jpg)<br>Installation space: 572.22 cm³</td>
</tr>
<tr>
<td>B-1</td>
<td>![](./images/814649377783021574_9.jpg)<br>SK464-50<br>50 x 84 x 40 mm</td>
<td>![](./images/814649377783021574_10.jpg)<br>TEG 127-200-28</td>
<td>![](./images/814649377783021574_11.jpg)<br>Installation space: 188.2 cm³</td>
</tr>
<tr>
<td>B-2</td>
<td>![](./images/814649377783021574_12.jpg)<br>SK464-50</td>
<td>![](./images/814649377783021574_13.jpg)<br>TGP-651</td>
<td>![](./images/814649377783021574_14.jpg)<br>Installation space: 207.1 cm³</td>
</tr>
<tr>
<td>B-3</td>
<td>![](./images/814649377783021574_15.jpg)<br>SK472-50<br>50 x 41.5 x 22 mm</td>
<td>![](./images/814649377783021574_16.jpg)<br>TEG 127-200-28</td>
<td>![](./images/814649377783021574_17.jpg)<br>Installation space: 55.6 cm³</td>
</tr>
<tr>
<td>B-4</td>
<td>![](./images/814649377783021574_18.jpg)<br>SK472-50</td>
<td>![](./images/814649377783021574_19.jpg)<br>TGP-651</td>
<td>![](./images/814649377783021574_20.jpg)<br>Installation space: 64.9 cm³</td>
</tr>
<tr>
<td>B-5</td>
<td>![](./images/814649377783021574_21.jpg)<br>SK507-75<br>75 x 90 x 100 mm</td>
<td>![](./images/814649377783021574_22.jpg)<br>TEG 127-200-28</td>
<td>![](./images/814649377783021574_23.jpg)<br>Installation space: 707.4 cm³</td>
</tr>
<tr>
<td>B-6</td>
<td>![](./images/814649377783021574_24.jpg)<br>SK507-75</td>
<td>![](./images/814649377783021574_25.jpg)<br>TGP-651</td>
<td>![](./images/814649377783021574_26.jpg)<br>Installation space: 737.8 cm³</td>
</tr>
</tbody>
</table>

## Thermal Simulations

Finite-element method (FEM) simulations with regard to thermal behaviour were carried out to review and evaluate the performance of the different design variants. Especially the heating processes with passive heat sinks can be calculated to obtain indicative values for the different variants. The software ANSYS Workbench was used here. It enables an analysis of stationary temperature distributions (Gebhardt 2011).

The level of detail of the modelling has a significant impact on the results of the simulation. Therefore the structure of the TEGs was modelled with individual p- and n-doped thermolegs and electric copper compounds in addition to the macroscopic design elements (such as heat sinks and gearbox surface). Table 2 lists important material properties that were used as input parameters for the simulation.

The boundary conditions of the thermal simulation are shown in Figure 3. The temperature of the oil line is set at 70°C with the variants A-1 and A-2. Three temperatures to simulate the possible seawater temperature were assigned to the punch for the junction of the cooling water line. The temperatures of 35°C, 25°C and 10°C are set as constant values because a steady flow of oil and cooling water can be assumed. The design variants of B-1 to B-6 take the ambient conditions from the test bench measurements. The steel plate represents the gearbox surface with a temperature of 50°C. The ambient temperature was set to 25°C.

According to VDI e. V. (2013), heat transfer coefficients of 2–25 W/m²K can be assumed for free convection in gases. Since this range is relatively large, the passive cooler of each design variant is simulated with 5, 8 and 10 W/mm² K. The selected numerical values are located in the lower area of the possible range, which is explained by the relatively poor air circulation in the

Table 2: Material parameters for thermal simulations from ASTM (1993), ContiTech (2014), Fischer (2014), Moser (2012) and VDI (2013).

<table>
<thead>
<tr>
<th>Material</th>
<th>Component</th>
<th>Thermal conductivity in W/mK</th>
<th>Specific heat in J/kg K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silicone oxide</td>
<td>Substrate of the μ-TEG</td>
<td>1.5 (0°C)</td>
<td>745 (0°C)</td>
</tr>
<tr>
<td>Polyethylene</td>
<td>Insulation in the μ-TEG module</td>
<td>0.28 (150°C)</td>
<td>296 (150°C)</td>
</tr>
<tr>
<td>Copper</td>
<td>Electrical connections</td>
<td>377 (20°C)</td>
<td>385 (20°C)</td>
</tr>
<tr>
<td>FullCure 720 (3D-Material)</td>
<td>Fastening material TEG</td>
<td>0.21 (20°C)</td>
<td>296 (20°C)</td>
</tr>
<tr>
<td>Extruded aluminium</td>
<td>Passive cooler</td>
<td>205 (20°C)</td>
<td>900 (20°C)</td>
</tr>
<tr>
<td>Bismuth-telluride</td>
<td>Thermoelectric material</td>
<td>2 (20°C)</td>
<td>178 (10°C)</td>
</tr>
<tr>
<td>Structural steel</td>
<td>Gearbox surface</td>
<td>60.5 (21°C)</td>
<td>434 (21°C)</td>
</tr>
<tr>
<td>Aluminium oxide</td>
<td>Ceramic plates</td>
<td>36 (0°C)</td>
<td>765 (0°C)</td>
</tr>
<tr>
<td>Thermoprotect</td>
<td>Insulation material</td>
<td>0.06 (20°C)</td>
<td>1,725 (20°C)</td>
</tr>
<tr>
<td>42CrMo₄</td>
<td>Oil line adapter</td>
<td>42 (20°C)</td>
<td>470 (20°C)</td>
</tr>
<tr>
<td>AlMg₃</td>
<td>Cool line adapter</td>
<td>134 (0°C)</td>
<td>875 (0°C)</td>
</tr>
<tr>
<td>Aluminium</td>
<td>TEG module</td>
<td>236 (0°C)</td>
<td>837 (0°C)</td>
</tr>
</tbody>
</table>

![](./images/814649377783021574_27.jpg)

Figure 3: Different boundary conditions of the construction variants A and B. (a) Variant A-2 with a hot temperature at the oil line of 70°C and different temperatures of the cooling water line of 35°C, 25°C and 10°C. (b) Variant B-2 with a hot temperature of the gearbox surface of 50°C, an ambient temperature of 25°C and different heat transfer coefficients of 5, 8 and 10 W/m² K.

ship gearbox compared to natural air flow, such as that in large production halls.

## Simulation Results
The stationary thermal FEM simulation supplies detailed temperature distributions of the design variants. Four of the seven results are represented in Figure 4. Tables 3 and 4 also show the temperature differences on the TEG surfaces as well as the continuous electrical power determined from each.

The simulation results of variant A-1 indicate that the temperature of the punch is largely determined by the temperature of the cooling line. A temperature difference of 26.22°C with a seawater temperature of 35°C occurs on the surfaces of the TEG 127-200-28. Variant A-2 shows a similar picture with a temperature difference of 26.10°C

![](./images/814649377783021574_28.jpg)

Figure 4: FEM simulation results of the different design variants. (a) Variant A-1 with a temperature difference of 44.9°C at the TEG surfaces, (b) variant B-2 with a temperature difference of 17.44°C at the μ-TEGs surfaces, (c) variant B-3 with a temperature difference of 6.08°C at the TEG surfaces, (d) variant B-6 with a temperature difference of 19.76°C at the μ-TEG surfaces.

Table 3: Temperature differences $\Delta T$ on the TEG surfaces and the continuous power $P_{\text{el}}$ of the design variants A-1 and A-2 as obtained from FEM simulations.

<table>
<thead>
<tr>
<th>Variant</th>
<th colspan="2">Cooling line 35°C</th>
<th colspan="2">Cooling line 25°C</th>
<th colspan="2">Cooling line 10°C</th>
</tr>
<tr>
<th></th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
</tr>
</thead>
<tbody>
<tr>
<td>A-1 TEG 127-200-28</td>
<td>26.22</td>
<td>4.916</td>
<td>33.71</td>
<td>8.128</td>
<td>44.99</td>
<td>14.477</td>
</tr>
<tr>
<td>A-2 TGP-651</td>
<td>26.10</td>
<td>2.175</td>
<td>33.59</td>
<td>3.605</td>
<td>44.85</td>
<td>6.426</td>
</tr>
</tbody>
</table>

Table 4: Temperature differences $\Delta T$ on the TEG surfaces and the continuous power $P_{\text{el}}$ of the design variants B-1 to B-6 as obtained from FEM simulations with different heat transfer coefficients from passive heat sinks to ambient air.

<table>
<thead>
<tr>
<th>Variant</th>
<th colspan="2">Heat transfer coefficient<br>5 W/m² K</th>
<th colspan="2">Heat transfer coefficient<br>8 W/m² K</th>
<th colspan="2">Heat transfer coefficient<br>10 W/m² K</th>
</tr>
<tr>
<th></th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
<th>$\Delta T$ in °C</th>
<th>$P_{\text{el}}$ in mW</th>
</tr>
</thead>
<tbody>
<tr>
<td>B-1 TGP- 127-200-28</td>
<td>8.61</td>
<td>0.531</td>
<td>10.94</td>
<td>0.855</td>
<td>12.02</td>
<td>1.033</td>
</tr>
<tr>
<td>B-2 TGP-651</td>
<td>13.79</td>
<td>0.607</td>
<td>16.36</td>
<td>0.855</td>
<td>17.44</td>
<td>0.971</td>
</tr>
<tr>
<td>B-3 TEG 127-200-28</td>
<td>4.29</td>
<td>0.132</td>
<td>6.08</td>
<td>0.264</td>
<td>7.06</td>
<td>0.357</td>
</tr>
<tr>
<td>B-4 TGP-651</td>
<td>7.08</td>
<td>0.160</td>
<td>9.25</td>
<td>0.274</td>
<td>10.32</td>
<td>0.340</td>
</tr>
<tr>
<td>B-5 TEG 127-200-28</td>
<td>15.29</td>
<td>1.673</td>
<td>16.68</td>
<td>1.991</td>
<td>17.21</td>
<td>2.118</td>
</tr>
<tr>
<td>B-6 TGP-651</td>
<td>19.76</td>
<td>1.247</td>
<td>19.87</td>
<td>1.262</td>
<td>21.28</td>
<td>1.446</td>
</tr>
</tbody>
</table>

on the surfaces of the four TGP-651. In the case of a very low seawater temperature of only $10^\circ\text{C}$, temperature differences of as high as nearly $45^\circ\text{C}$ can be reached. A thermal bypass through the screw connections is not detectable.

The design variants B-1 to B-6 simulation results show that the solutions with passive heat sinks can significantly lower temperature differences on the surface of the TEGs. In the considered range of heat sinks it can be recognized that with increasing size of the heat sink its cooling performance rises and leads to a higher temperature difference. With a cross-sectional area $A$ the thermal resistance $R_{\text{th}}$ decreases according to eq. [4]:

$$
R_{\text{th}} = \frac{l}{\lambda \cdot A} \tag{4}
$$

As all passive heat sinks are made of extruded aluminium, their thermal conductivity $\lambda$ is equal. The ratio between length $l$ and cross-sectional area reaches its minimum for heat sink SK507. The temperature difference ranges from $4.29^\circ\text{C}$ (B-3 with a heat transfer coefficient 5 W/m² K) to a maximum of $21.28^\circ\text{C}$ (B-6 with a heat transfer coefficient 10 W/m² K). It is apparent that four TEG-651 in the same heat sink have a higher temperature difference.

The electrical performances of the design variants were determined on the basis of preliminary experiments on the TEGs used. The various TEGs were mounted between two defined tempered heating plates and integrated into an electrical circuit, which corresponds to the electrical equipment of the sensor board. By varying the temperatures and recording the voltage, characteristic curves for the TEGs were recorded to confirm the ratio between electrical power output and temperature difference given in the manufacturers data sheets. The electrical power of the design variants was then determined based on the simulation results and the characteristic curves of the TEGs. The determined electrical performances can be found in Tables 3 and 4.

According to requirement R.1, a positive energy balance is obtained when the continuous electrical power is more than 2 mW. This is achieved by the variants A-1 and A-2 even in case of warm seawater temperature of $35^\circ\text{C}$ with a power of 4.916 mW (A-1) and 2.175 mW (A-2). At a low seawater temperature of $10^\circ\text{C}$, a power of 14.477 mW is achievable with version A-1. Taking a favourable heat transfer coefficient of 10 W/m² K into account, the simulation also shows that the TEG 127-200-28 can provide sufficient electric power (2.118 mW) for the operation of the sensor node in combination with the passive heat sink SK507 in variant B-5.

## Practical Experiments

Practical experiments were carried out to check the simulated results. To avoid expensive installations on a gearbox test bench, a simplified structure was developed with which the simulated design variants could be checked in practice. The equivalent circuit for the practical test is shown in Figure 5. A temperature-regulated heating plate was used to reproduce the hot side.

The joints between the heating plate surface and the TEG as well as the TEG and the heat sink were realized with a thermal conductive foil. Both the ambient and the surface temperatures of the heating cartridge as well as the voltage $U$ occurring in the TEG were recorded during the experiments. The electric consumers of the sensor node were simulated in a simplified manner via an electrical circuit with defined resistance $R_{\text{Load}}$. By knowing the resistance of the load, the electrical power $P_{\text{Variant}}$ of the variants could be determined using eq. [5].

![](./images/814649377783021574_29.jpg)

Figure 5: Equivalent circuit for the practical tests. $V_{\text{TEG}}$ symbolizes the generated voltage from the TEG, $R_{\text{TEG}}$ represents the internal resistance of the TEG and $R_{\text{Load}}$ stands for the resistance of the connected load.

$$
P_{\text{Variant}} = \frac{U}{R_{\text{Load}}^2} \tag{5}
$$

The calculated results of the thermal simulations can now be compared to the measurement results of the practical experiments, which were carried out over a period of 24 h to average random peaks. Different temperature ranges were documented due to the long duration of measurement since the ambient temperature fluctuated. For the comparison of the practical experiments with the simulation results, the appropriate temperature differences were extracted with corresponding voltage values from the logged data. An active cooling system would have been required for the realization of the cold side of the design variants A-1 and A-2. Since this would have only been possible with relatively high costs and simulation results with 4.916 mW (A-1) or 2.175 mW (A-2) can be expected for a requirement fulfilment, it was not done and only experiments for the passively cooled variants B-2 to B-6 were conducted. The results of the comparison are represented in Figure 6.

The electrical performance, which is determined in the practical experiment of the TEGs, matches the simulated data in most cases. The deviation in percent is smaller than 10%. Only the simulated results of variants B-4 and B-6 show higher deviations. Practical

![](./images/814649377783021574_30.jpg)

Figure 6: Comparison of the provided electrical power of the simulation and the practical experiments.

experiments offered more electrical power than the simulated μ-TEG variants. This may occur by better material properties than mentioned in the manufacturer's data sheet, which was used as input for the simulations. It should be noted that the use of four μ-TEGs with the same heat sink selection produces more electrical power than the conventional TEG 127-200-28. However, the various forms of variant B do not reach the required 2 mW according to requirement R.1. However, the use of the passive heat sink SK507 shows that the electrical power can almost be achieved. In the case of B-5, 1.6 mW is generated, with B-6, 1.8 mW.

# Evaluation and Selection of a Design Variant

The requirement fulfilment of design variants was assessed after the conclusion of the thermal simulations and practical experiments. The evaluation was done qualitatively based on the characteristics "high" (3), "medium" (2) or "low" (1). Furthermore, the evaluation factors were weighted. The provision of the required electrical power of a continual 2 mW (R.1) is the most important criterion for the power supply of the sensor system and is weighted with a factor of 0.5. The functionality at the ambient conditions (R.2) and the maximum design size (R.3) is weighted by a factor of 0.2. The easy installation according to R.4 is weighted by the factor 0.1. Table 5 lists the assessment results.

With the help of the thermal simulation, it could be verified that the variant A-1 has the greatest harvesting potential with more than 4 mW of continuous electrical power. Variant A-2 also meets the requirement R.1 to the full extent (R.1=3). Taking into account of the lower temperature of seawater, even significantly higher power output of up to 14.77 mW (Variant A-1) can be achieved. The requirement R.2 (ambient temperatures $T_{\text{hot}}=50$-$70^\circ$C and $T_{\text{cold}}=10$-$35^\circ$C) is also met by the design variants of A-1 and A-2 (R.2=3). The design size of $250\ \text{cm}^3$ is exceeded by both variants of the type A (R.3=2). Because the significant measurement points are not in the area of the heat exchanger, additional connections are necessary between the TEG and the sensor nodes. Mechanical modifications remain necessary in the oil and cooling water piping for the installation of the TEG. Requirement R.4 is therefore not met (R.4=1).

The electrical power generated by the design variants of B-1 to B-6 does not meet the requirement R.1 (R.1=1). Only by extending the measurement cycle to 17 min and 30 s (Variant B-5) or 15 min and 30 s (Variant B-6) could a passive cooling in conjunction with a TEG be considered as an energy source (R.1=2). Similar to the design variants A-1 and A-2, the requirements R.2 (ambient temperatures $T_{\text{hot}}=50$-$70^\circ$C and $T_{\text{cold}}=10$-$35^\circ$C) are fulfilled through all design variants of B-1 to B-6 (R.2=3). The maximum design size is adhered by the variants B-1 to B-4 (R.3=3), while the variants B-5 and B-6 represent the bulkiest designs of the investigation (R.3=1). In contrast to the design variants of A-1 and A-2, the design variants B-1 to B-6 meet the requirement R.3, because no significant mechanical modifications need to be made to the marine gearboxes and easy installation is possible (R.4=3).

The variant A-1 for the design of a first demonstrator was selected after the evaluation of the requirement fulfilment. These showed the overall highest requirement fulfilment (see Table 5). In particular, this solution provides the highest electrical power even when the

Table 5: Evaluation of the requirement fulfilment of design variants. Fulfilling of requirement is high (3), medium (2) or low (1).

<table>
<thead>
<tr>
<th>Variant</th>
<th>Requirement R.1</th>
<th>Requirement R.2</th>
<th>Requirement R.3</th>
<th>Requirement R.4</th>
<th>Average</th>
</tr>
<tr>
<th></th>
<th>Electrical power</th>
<th>Functionality with $T_{\text{h}}=50$-$70^\circ$C and $T_{\text{c}}=10$-$35\ ^\circ$C</th>
<th>Installation space$<250\ \text{cm}^3$</th>
<th>Easy installation; IP69</th>
<th></th>
</tr>
<tr>
<th></th>
<th>Weighting 0.5</th>
<th>Weighting 0.2</th>
<th>Weighting 0.2</th>
<th>Weighting 0.1</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>A-1</td>
<td>3</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>2.6</td>
</tr>
<tr>
<td>A-2</td>
<td>3</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>2.6</td>
</tr>
<tr>
<td>B-1</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>B-2</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>B-3</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>B-4</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>B-5</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>3</td>
<td>2.1</td>
</tr>
<tr>
<td>B-6</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>3</td>
<td>2.1</td>
</tr>
</tbody>
</table>

installation costs are assessed higher when compared to the other design variants.

## Implementation of WSN in Marine Gearbox

The selected variant A-1 is currently being used for the realization of a first practical demonstrator. This consists of a TEG (according to variant A-1), two sensor nodes (see section "Requirements for Thermoelectric Energy Harvesting") as well as four other, individual sensors for vibration, torque and rotational speed measurement connected to the sensor nodes as shown in Figure 7. It is planned to test the demonstrator on a ship gearbox of type WAF 665 (see Figure 1) for use in fast boats, patrol boats, yachts and other vessels with similar requirements.

The TEG including power management is installed in the area of the heat exchanger and connected to the oil and cooling water pipelines. The sensor node 1 is placed on the gearbox housing on the side of the drive shaft. In conjunction with sensor 3, the vibrations of the gearbox are recorded at the drive side in order to monitor the conditions of the drive shaft's bearing points and the gear wheel meshing. Sensor node 2 is mounted on the housing of the output side. There, the speed and torque of the output shaft can be monitored. The connection between TEG, sensor nodes and individual sensors is realized via cable (laid cable length approximately 1 m).

The data transmission between the sensor nodes and a parent evaluation unit takes place once every 15 min wirelessly via RFID in a 865-868 MHz frequency band. Twenty-three significant signal characteristics are calculated and transferred on the sensor nodes within 8.5 s. The entire raw data set of vibrational measurements is transmitted once a day. The transmission time for 8,000 measurement readings was 61 s.

Analysing the potential of thermoelectric power supply with the considered solutions is the first step to integrate wireless sensor nodes in marine gearboxes. In comparison to other CMSs, the presented demonstrator works without wired energy supply from the board network as well as the data transfer. The development with non-moving parts results in a renouncing of maintenance as well as the exchange of limited energy sources like batteries. By demonstrating the functionality of the wireless condition monitoring, a simplified CMS for marine transmissions should be established on the one hand and on the other hand, the potential of the thermoelectric energy supply for other industries should be shown.

**Acknowledgement:** The presented research findings have been developed as part of the research project entitled "Application of wireless technology for economic monitoring of maritime gearboxes". The project is funded by the Federal Ministry for Economic Affairs and Energy on the basis of a decision of the German Bundestag and supported by the Project Management Jülich. Furthermore the authors would like to thank the project partners from Bachmann Monitoring GmbH, HSG-IMIT - Institut für

![](./images/814649377783021574_31.jpg)

Figure 7: Scheme of the WSN with variant A-1 as power supply.

Mikro- und Informationstechnik der Hahn-Schickard- Gesellschaft e.V., microsensys GmbH and REINTJES GmbH for the excellent cooperation.

Funding: This work was funded by Bundesministerium fur Wirtschaft und Technologie (grant/award number: 03SX350A).

# References

ASTM Committee E20 on Temperature Measurement. 1993. “Manual on the Use of Thermocouples in Temperature Measurement.” In *Revision of Special Technical Publication (STP) 470b*, edited by American Society for Testing and Materials (ed.), Vol. 4. Philadelphia, PA: ASTM.

Bartholomé, K., M. Bartel, R. Binninger, and I. Schumacher. 2011, “Energy-Autarkic Sensors in Aircrafts”, *Proceedings SENSOR*, 07/06/2011–09/06/2011, Nürnberg, pp. 417–423.

Contitech. 2014. *Conti®Thermo-Protect - Die flexible Isolierung für die Industrie*. Accessed 9 February 2015. http://www.contitech.de/pages/produkte/dichtsysteme/brochures/WT9101_CT-Thermo-Protect_de.pdf.

Dembowski, K. 2011. *Energy Harvesting Für Die Mikroelektronik – Energieeffiziente Und -Autarke Lösungen Für Drahtlose Sensorsysteme*. Berlin, Offenbach: VDE Verlag.

Deutsches Institut für Normung e. V & Vde Verband der Elektrotechnik Elektronik Informationstechnik e. V. 1991. *DIN EN 60529:1991, Schutzarten Durch Gehäuse (IP-Code)*. Berlin: Beuth-Verlag.

Dilhac, J.-M., R. Monthéard, M. Bafleur, V. Boitier, P. Durand-Estère, and P. Tounsi. 2014. “Implementation of Thermoelectric Generators in Airliners for Powering Battery-Free Wireless Sensor Networks.” *Journal of Electronic Materials*, The Minerals, Metals & Materials Society, 43 (6):2444–51.

Eichler, C. 1977. *Instandhaltungstechnik*. Berlin: VEB Verlag Technik.

Fahrner, W. R., and S. Schwertheim. 2009. *Semiconductor Thermoelectric Generators*. Stafa-Zurich: Trans Tech Publications Ltd.

Fischer Elektronik GmbH & Co. Kg. 2014, *f.cool.d 2015 – Strangkühlkörper, LED-Kühlkörper, Lüfteraggregate*. Accessed 9 February 2015. http://www.fischerelektronik.de/fileadmin/fischertemplates/download/Katalog/kuehlkoerper.pdf.

Freunek, M. 2010. “Untersuchung Der Thermoelektrik Zur Energieversorgung Autarker Systeme.” In *RF MEMS and Applications*, Volume 4, edited by L. Reindl. Tönning, Lübeck, Marburg: Der Andere Verlag.

Gebhardt, C. 2011. *Praxisbuch FEM Mit ANSYS Workbench - Einführung in Die Lineare Und Nichtlineare Mechanik*. Munich: Carl Hanser Verlag.

Gessler, R., and T. Krause. 2009. *Wireless-Netzwerke Für Den Nahbereich*, 1st ed. Wiesbaden: Vieweg + Teubner Verlag.

Hudak, N. S., and G. G. Amatucci. 2008. “Small-Scale Energy Harvesting Through Thermoelectric, Vibration, and Radiofrequency Power Conversion.” *Journal of Applied Physics* 103:101301/1–101301/24.

Kouremenos, D. A., and D. T. Hountalas. 1997. “Diagnosis and Condition Monitoring of Medium-Speed Marine Diesel Engines.” *Tribotest Journal* 4:63–91.

Liu, Y., Z. Liu, Y. Xie, and Z. Yao. 2000. “Research on an on-Line Wear Condition Monitoring System for Marine Diesel Engine.” *Tribology International*, Elsevier, 33:829–35.

Lösl, J. 2006. “Implementierung Von Condition Based Maintenance (CBM) Auf Schiffen.” *Telediagnose - Service-Magazin Der Prüftechnik-Gruppe* 9:4–5.

Moser, A. 2012. “Thermoelectric Energy Harvesting From Small Ambient Temperature Transients.” In *Design of Microsystems*, Vol. 7, edited by P. Woias. Ulvesbüll: Der Andere Verlag.

Nachtrab, J. 2013. “Herstellung Thermoelektrischer Generatoren Mit Textilen Methoden.” In *Schriftenreihe Des Lehrstuhls Für Prozessmaschinen Und Anlagentechnik*, Band 19, edited by E. Schlücker. Aachen: Shaker Verlag.

Penella, M. T., and M. Gasulla. 2007. “A Review of Commercial Energy Harvesters for Autnomous Sensors”, *2007 IEEE Instrumentation and Measurement Technology Conference Proceedings*, 01/13/2007–03/03/2007, Warsaw, pp. 1–5.

Potje-Kamloth, K. 2011. “Low-Cost-Thermogeneratoren Auf Folienbasis.” *Oberflächentechnik Und Galvanotechnik* 66:331–7.

Scharfetter, C. 2007. *Zustandsanalyse für schiffstechnische Anlagen durch kombinierte Auswertung vorhandener Messgrößen*, doctoral thesis, Technische Universität Hamburg-Harburg, Aachen.

Silva, C. W. 2005. *Vibration and Shock Handbook*. Boca Raton, FL: Taylor & Francis Group.

Spreemann, D., D. Hoffmann, F. Folkmer, Y. Manoli, and D. Maurath. 2008. “Design-Flow Am Beispiel Elektromagnetischer Vibrationswandler.” In *Energy Harvesting - Grundlagen Und Praxis Energieautarker Systeme*, edited by U. Brill. Renningen: Expert Verlag.

VDI e. V. (ed). 2013. *VDI-Wärmeatlas*. Berlin, Heidelberg: Springer Verlag.

Wang, L., and R. Gao. 2006. *Condition Monitoring and Control for Intelligent Manufacturing*. London: Springer Verlag.

Wirth, R., S. Benecke, and E. Kravcenko. 2012. *Energieautarkes Condition Monitoring System: Effiziente Energieversorgung*. Berlin: Technische Universität Berlin.