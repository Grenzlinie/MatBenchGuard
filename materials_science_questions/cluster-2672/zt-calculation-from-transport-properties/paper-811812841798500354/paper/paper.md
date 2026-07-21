# On-Chip Thermal Management and Hot-Spot Remediation

Avram Bar-Cohen and Peng Wang

**Abstract** The rapid emergence of nanoelectronics, with the consequent rise in transistor density and switching speed, has led to a steep increase in die heat flux and growing concern over the emergence of on-chip "hot spots." The application of on-chip high heat flux cooling techniques provides a viable direction for the thermal management of such nanoelectronic components. Following a review of the relevant passive and active thermal management techniques, the physical phenomena underpinning the most promising on-chip thermal management approaches are described. Attention is devoted to thin-film and miniaturized thermoelectric coolers, orthotropic TIMs/heat spreaders, and phase-change microgap coolers for hot-spot remediation and thermal management of these nanoelectronic chips.

**Keywords** Nanoelectronics · Hot spots · Electronic cooling · Thermal management · Thermoelectric coolers · Microcoolers · Thermal interface materials (TIM)

## 1 Introduction

The Moore's law progression in semiconductor technology, leading to shrinking feature size, increasing transistor density, faster circuit speeds, and higher chip performance, continues unabated. As shown in Fig. 1, the 2005 International Technology Roadmap for Semiconductors (ITRS) [1], predicts a continuous decrease in transistor size, which can be expected to lead to functioning 20 nm devices at more than a billion transistors per square centimeter ($10^9$/cm²) by 2010 and to continue down to 10 nm, along with a rise in transistor density toward 10 billion transistors/cm² ($10^{10}$/cm²), by 2018. These changes in semiconductor technology can be expected

---

A. Bar-Cohen (⊗)
Department of Mechanical Engineering, University of Maryland, College Park, MD, USA
e-mail: abc@umd.edu

C.P. Wong et al. (eds.), *Nano-Bio- Electronic, Photonic and MEMS Packaging*,
DOI 10.1007/978-1-4419-0040-1_12, © Springer Science+Business Media, LLC 2010

to lead to ever faster and more computationally complex chips. Moreover, despite the extensive efforts that have been made to reduce both capacitance and operating voltage on the chip, the chip power dissipation – at the very cutting edge of the technology – continues to rise. In the absence of more aggressive thermal control techniques, the elevated temperatures resulting from higher power dissipation can be expected to decrease CMOS transistor switching speeds and accelerate some key failure mechanisms, thus compromising the performance and reliability of such advanced semiconductor devices.

![](./images/811812841798500354_1.jpg)

Fig. 1 The 2005 ITRS predictions of feature size, chip size, and transistor density for high-performance microprocessor chips [1]

The Moore’s law-driven transition to the widespread use of nanoscaled electronics poses three specific thermal management challenges, which have motivated significant recent activity in microprocessor cooling [2–7]. Foremost among these is the drive to improve component speed, which has motivated circuit designers to compress the “core” of the microprocessor to an ever smaller size. Along with the reduced “time-of-flight” between transistors, this spatial compression leads disproportionately to high heat flux in the “core” areas of the silicon chip. Second, higher interconnect current densities, due to higher chip power, and the extreme interconnect aspect ratios, resulting from the high transistor densities, result in rapidly increasing interconnect temperatures in today’s IC technology. The problem is aggravated by the trend to replace the $SiO_2$ interconnect passivation layer with

lower dielectric constant materials, such as novel organic and porous dielectrics, which also possess lower thermal conductivity and greatly impede the conduction of heat away from the interconnect and transistor. Third, the use of novel nanoscaled electronics technologies, e.g., narrow channels, further aggravates the local tem- perature rise around individual transistors. Figure 2 shows the temperature contour around a single nanoscaled transistor and indicates there is nanometer scale hot spot in the transistor drain region [8].

![](./images/811812841798500354_2.jpg)

Fig. 2 The temperature field from a device-like hot spot in bulk 90 nm silicon transistor [8]

Under the combined influence of these trends, chip power dissipation and heat flux are expected to increase further over the next decade. According to the International Electronics Manufacturing Initiative Technology Roadmap (iNEMI 2006) [9], the maximum chip power dissipation is projected to be 510 W and the maximum chip heat flux to be $300\ \text{W/cm}^2$ for the high-power automotive devices in 2015, as indicated in Fig. 3.

Moreover, as seen in Fig. 4, these advanced nanoelectronic chips are charac- terized by substantial nonuniformities in power dissipation, resulting in localized, high heat flux "hot spots" with a large on-chip temperature gradient [3]. Because chip thermal management must ensure that all junction temperatures in the micro- processor do not exceed an application-driven maximum temperature, typically in the range of $90$–$110^\circ\text{C}$, it is often these hot spots, not the entire chip power dissi- pation, that drive the thermal design. This leads to two undesirable consequences: (1) nonuniform heat generation limits the total heat dissipation that can be managed by a conventional thermal solution and, thus, a much more aggressive thermal solu- tion than would be required for uniform heating, is necessary and (2) the focus on controlling the temperature of the hot spot can lead to over-design of the micropro- cessor cooling solution. As shown in Fig. 5, the 2006 iNEMI Roadmap predicted that desktop PC second-level thermal solution requirements for a uniformly pow- ered chip will become more demanding, pushing the limits of current air-cooled systems. Once the nonuniform distribution of power across the chip is considered,

![](./images/811812841798500354_3.jpg)

Fig. 3 The 2006 iNEMI prediction of chip power dissipation and heat flux for the highest power automotive devices [9]

![](./images/811812841798500354_4.jpg)

Fig. 4 Schematic illustrating typical die power map

air-cooling system will have to be replaced with more aggressive cooling solutions. Due to its complexity, on-chip hot-spot cooling has become one of the most active and challenging research areas in thermal management of electronic devices and packages.

![](./images/811812841798500354_5.jpg)

Fig. 5 The 2006 iNEMI predictions of desktop PC second-level thermal solution requirement

### 1.1 Potential Hot-Spot Cooling Solutions

Thermal management for high-flux electronic silicon chips can be classified into two strategies: passive cooling and active cooling, both of which have continued to be extensively studied during the past few years.

#### 1.1.1 Passive Cooling Solutions

Passive cooling solutions are those that do not have moving parts and generally require no external electric power to activate or assist thermal transport. These techniques mainly rely on heat spreading in high-conductivity materials, such as bonded spreaders or diamond coatings on the silicon chip, and/or on vapor transport along with evaporation and condensation in tubes and channels, to transport the heat from the high-flux regions to the areas of lower heat flux. Due to the high thermal conductivity of silicon ($\sim$150 W/m K), only modest spreading improvements can be obtained from the use of traditional spreading materials, such as copper (390 W/m K), beryllia (250 W/m K), aluminum nitride (220 W/m K), or other composites [10]. Alternatively, diamond is a very attractive material for passive cooling of high-flux regions on a chip because it has the highest thermal conductivity of any known materials and also has a very high electric resistance ($\sim10^8\ \Omega$m). The

thermal conductivity is in the range of 1500–2100 W/m K for single-crystal diamond fabricated by the high-pressure synthesis method and 500–1300 W/m K for polycrystalline diamond fabricated by CVD low-pressure synthesis [11]. Deposition of diamond on substrates, such as silicon, is a reasonably mature technology and there are now multiple techniques that provide high-quality single-crystal or poly- crystalline diamond films. The fabrication of a diamond heat-spreading layer on silicon's active region includes direct growth of diamond on the silicon substrate or bonding of a polished diamond film onto the silicon substrate. Figure 6 shows an example of diamond deposited directly on the aluminum metallization layers of a silicon chip. However, the contamination with impurities that may occur in the silicon wafer during diamond deposition, associated with the carbon, nitrogen, oxygen, hydrogen, and other elements diffusing into the device wafer from reac- tive gases, have – thus far – kept diamond deposition from becoming the technique of choice To avoid these difficulties, diamond is often bonded to silicon using a gold–tin eutectic alloy solder film. However, the thermal contact resistance at the silicon substrate/diamond interface and metallization layers/diamond interface and poor adhesion of diamond to the metallization layer, aggravated by cyclic thermally induced stress variations, has restricted the application of diamond as a reliable heat spreader.

![](./images/811812841798500354_6.jpg)

Fig. 6 Diamond deposited on aluminum metallization in a silicon substrate using a microwave plasma technique [12]

Since the thermal conductivity of silicon is relatively high, while the heat-transfer resistance through the thickness is relatively small, a heat pipe micromachined in the silicon substrate or a flat-plate heat pipe attached to the silicon chip is advan- tageous in providing in-plane spreading of the heat released by localized regions of high heat flux [13, 14]. A heat pipe is a passive heat-transfer device with an extremely high effective thermal conductivity, resulting from the evaporation and

![](./images/811812841798500354_7.jpg)

Fig. 7 Structure of typical wicked heat pipe

condensation of a suitable working fluid within an evacuated, hermetically sealed enclosure. Figure 7 is a side view of a heat pipe showing the wick and the vapor/liquid flow characteristics.

In the past 10 years, extensive research has demonstrated that heat-spreading performance comparable to that of diamond substrates can be obtained [15–17]. In addition, the factors that affect the performance of micro or miniature heat pipes such as the frictional vapor flow, the vapor space, the shape and dimensions of the microchannels, the operating temperature, the disjoining pressure, and evaporating heat resistance have been systematically investigated. These investigations have pro- vided insight into the design of highly efficient heat pipes, which can meet the new requirements of high heat flux cooling. Adkins at Sandia National Laboratories, Albuquerque, NM, investigated a heat-pipe heat spreader embedded in a silicon substrate as an alternative to the conductive cooling of integrated circuits using dia- mond films. In their design miniaturized heat pipes, created by $35\ \mu$m grooves in the silicon wafer, function as highly efficient heat spreaders, collecting heat from the localized hot spots and dissipating the heat over the entire chip surface, with an effective thermal conductivity of at least 800 W/m K [18, 19].

Recently research has been focused on achieving further increases in perfor- mance by using thermally driven pulsating two-phase flows [20, 21], new capillary structures [22], and MEMS-based heat pipes [23, 24]. Plesch et al. reported that flat miniature heat pipes with axial grooves, using water as the working fluid, were capa- ble of sustaining heat fluxes on the order of $40\ \text{W/cm}^2$ [25]. Ma et al. fabricated the heat pipes with microscaled sintered powder wicks, which can remove heat fluxes of up to $80\ \text{W/cm}^2$ without any sign of evaporator dry out [26]. Gillot fabricated flat miniature heat pipes with microcapillary grooves inside a silicon substrate and the heat removal capability was reported to be $110\ \text{W/cm}^2$ [27]. Using miniaturized heat pipes Lin et al. reported that a cooling heat flux of $140\ \text{W/cm}^2$ was achieved [28]. While heat pipes possess certain inherent advantages and current research may raise the observed thermal performance limits, heat removal rates of the currently available heat pipes are generally still not suitable for controlling the temperature of the most severe, high-flux hot spots on the chip.

### 1.1.2 Active Cooling Solutions

Active cooling solutions usually involve moving parts and require the input of electric energy for their operation. The most common active cooling solution is air-cooled, forced convection heat sinks, which have been long used for a wide range of electronic equipment, including office and desktop computers. However, this conventional active cooling method has very limited capability for dealing with high-flux zones on microelectronic chips, due to its inherently low heat-transfer coefficients. Compared to air cooling, the use of liquid coolants has many advantages such as high thermal conductivity, high specific heat, low viscosity, and high latent heat of evaporation for two-phase application. As a result, different active liquid-cooling technologies, such as microchannel heat sinks and direct jet impingement, have been developed due to the higher heat-transfer coefficient and high cooling flux achieved as compared to air-cooling heat sink.

With microfabrication techniques developed by the electronics industry, it is possible to manufacture microscaled three-dimensional structures, typically consisting of closely spaced parallel channels with rectangular, trapezoidal, or triangular cross sections and hydraulic diameters ranging from 100 to $1000\ \mu\text{m}$ (see Fig. 8). Such microchannel "compact heat exchangers" may be fabricated in the chip itself or in the heat sink to which a chip or array of chips is attached. Microchannel heat sinks

![](./images/811812841798500354_8.jpg)

Fig. 8 SEM photos of cross sections of three different microchannels [30]

can be used either with single-phase flow, where heat is transferred from the elec- tronic chip via sensible heat gain to the coolant, or with two-phase flow, which also utilizes the latent heat of the coolant during liquid/vapor phase change. In both ther- mal transport modes, microchannel coolers are capable of significantly increasing the wetted surface area and of thinning the thermal boundary layers, thus achieving very high heat-transfer rates. Single-phase liquid-cooling systems utilize a pump to actively circulate the liquid to the microchannels and have been studied for many years. In their 1981 pioneering work Tuckerman and Pease used single-phase con- vection with water flowing through a microchanneled silicon chip to demonstrate heat removal of $790 ~W/cm^2$ with a flow rate of $1 \times 10^{-5} ~m^3/s$ and the pressure drop below $3.45 \times 10^5$ Pa [29]. Although the high heat flux capability is promis- ing, and considerable pressure reductions and improvements in flow distribution have been achieved in recent years, the integration of such a microchannel cooler into a closed-loop plumbing/pumping system and justifying the required pumping power has proven challenging. Moreover, the industry's resistance to flowing liquids directly through active microchanneled chips has necessitated the use of thermal interface materials for the attachment of the microchannel coolers and considerably raised the thermal resistance of this thermal management approach.

Two-phase microchannel cooling, exploiting the latent heat of the coolant to reduce the flow rates and pumping power requirements and the high heat-transfer coefficients associated with boiling, has received growing attention, focusing on reductions in pumping power and dealing with the performance limitations posed by flow instabilities and maldistribution. Bowers et al. showed that two-phase microchannels, operating with water flow rates of less than $1.08 \times 10^{-6} ~m^3/s$ and pressure drops of $3.45 \times 10^5$ Pa could remove more than $200 ~W/cm^2$ [31]. Mudawar also demonstrated a heat removal rate of $361 ~W/cm^2$ with two-phase forced con- vective cooling on an enhanced surface with FC-72 as the dielectric coolant [32]. However, in a recent study of water-cooled two-phase microchannel coolers, Prasher found the biggest challenge to the use of two-phase microchannel coolers in hot-spot cooling is the nonuniformity in flow distribution and the resulting large tempera- ture nonuniformities [30]. The testing results show that the worst-case temperature fluctuations are on the order of $30^{\circ}C$ for $0.6 ~W 400 \times 400 \mu m$ hot-spot heating con dition, on the order of $20^{\circ}C$ for $0.4 ~W 400 \times 400 \mu m$ hot-spot heating condition, and on the order of $15^{\circ}C$ for the uniform heating condition, showing that temper ature fluctuations depend on the power being dissipated from localized hot spots. In particular, poor flow distribution in two-phase microchannels might lead to less flow in the high-flux regions, leading to localized dry out on the hot spot, which will result in large and rapid increase in the hot-spot temperature.

Jet impingement cooling, with high-velocity liquid streams directly impinging onto the hot surface, is an alternative to microchannel coolers. This method offers several potential advantages, such as high heat-transfer coefficients associated with the evaporation of thin liquid films and the ability to form patterns during the liquid distribution through an array of jets. The jets can be fabricated by circular or slot- shaped orifices or nozzles of various cross sections and can flow into a gaseous medium (vapor or air) forming the so-called free-jets or into a liquid medium,

leading to a "submerged jet." As a final distinction, jet impingement cooling of electronic components may involve forced convection alone or localized flow boiling, with or without net vapor generation [33-35]. Although electronic cooling applications will require the use of dielectric liquids, much of the available data is for jet impingement of water, including the work by Zhang demonstrating that two-phase jet impingement is capable of removing a heat flux of more than $100\ \text{W/cm}^2$ at water flow rates below $2.5 \times 10^{-7}\ \text{m}^3/\text{s}$ [36], use of boiling macrojets for removal of a heat flux over $400\ \text{W/cm}^2$ [37], and the results by Kiper, using microscaled direct water impingement from an orifice plate to cool VLSI circuits dissipating more than $500\ \text{W/cm}^2$ [38]. The need to achieve this level of performance with dielectric coolants and concerns over the reliability, complexity, volume, weight, and cost of such jet impingement systems have posed significant barriers to the successful commercial implementation of these approaches.

### 1.1.3 Solid-State Cooling Solutions

In recent years there has been increased interest in the application of solid-state thermoelectric coolers for high-flux thermal management because of their compact structure, fast response, high-flux spot-cooling capability, and high reliability, and their absence of moving parts [39-46]. Another major advantage of a thermoelectric cooler is that it can be miniaturized and integrated into the chip package. A thermoelectric cooler is based on the Peltier effect and consists of N-type and P-type thermoelectric elements, as shown in Fig. 9, where the N-type and P-type thermoelectric elements are joined by metallic connectors at the top and bottom. When a

![](./images/811812841798500354_9.jpg)

Fig. 9 Schematic diagram of
a thermoelectric cooler

DC current goes through these thermoelectric element/metal contacts, heat is either released or absorbed in the contact region depending on the direction of the current. Attaching the TEC cold junction to a working device makes it possible to lower its temperature below its surroundings and possibly even below the ambient temperature.

In the conventional thermoelectric cooler (TEC) design, the maximum achievable temperature reduction across the thermoelectric cooler can be determined by:

$$
\Delta T_{\text {max }}=\frac{S^{2} T_{\mathrm{c}}^{2}}{2 \rho k} \tag{1}
$$

and the maximum achievable cooling flux on the cold side of thermoelectric cooler by Equation (2)

$$
q_{\max }^{\prime \prime}=\frac{S^{2} T_{\mathrm{c}}^{2}}{2 \rho d} \tag{2}
$$

where $S$ is the Seebeck coefficient, $k$ is the thermal conductivity, $\rho$ is the electrical conductivity, $T_{\mathrm{c}}$ is the absolute temperature at the cold side and $d$ is the thickness of thermoelectric elements [47-49]. Thus, the largest temperature reduction is attained for thermoelectric materials when the Seebeck coefficient is large and the electrical resistivity and the thermal conductivity are as small as possible. Equation (2) indicates that the maximum cooling flux is inversely proportional to thermoelectric element thickness and thus the main advantage of going to thin-film thermoelectric coolers (TFTECs) is the dramatic increase in cooling heat flux. As shown in Fig. 10, Fleurial estimated that the heat flux of several hundred Watt per square centimeter could be removed with thin film thermoelectric coolers when thermoelectric element thickness is on the order of $20 \mu \mathrm{m}$ [50].

Recent attempts to improve the cooling performance of TECs have focused on low-dimensional nanostructured superlattices which are capable of suppressing the thermal conductivity through phonon trapping and improving the TEC's figure of merit $Z\left(Z=S^{2} / k \rho\right)$. Venkatasubramanian reported thin-film superlattice $\mathrm{Bi}_{2} \mathrm{Te}_{3} / \mathrm{Sb}_{2} \mathrm{Te}_{3}$ coolers capable of providing up to $32^{\circ} \mathrm{C}$ net cooling measured on the cold side of the coolers and a maximum estimated cooling heat flux of $700 \mathrm{~W} / \mathrm{cm}^{2}$ at room temperature [51]. Harman demonstrated a thin-film cooler based on quantum dot n-type PbSeTe/PbTe superlattice structure, which provided $43.7^{\circ} \mathrm{C}$ net cooling at room temperature [52]. Fan and Shakouri demonstrated net cooling of up to $2.5^{\circ} \mathrm{C}$ at room temperature and $7^{\circ} \mathrm{C}$ at $100^{\circ} \mathrm{C}$ ambient temperature and a maximum cooling heat flux as high as $680 \mathrm{~W} / \mathrm{cm}^{2}$ on the surface of a microcooler for p-type thin-film superlattice SiGeC/Si microcoolers TEC device miniaturization [53], to extract greater performance from existing bulk thermoelectric materials, is the other approach to TEC improvement currently receiving attention. Using ceramic thinning technology, Semenyuk developed and commercialized a $130 \mu \mathrm{m}$-thick miniatured $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ thermoelectric cooler which can provide more than $100 \mathrm{~W} / \mathrm{cm}^{2}$ cooling heat

![](./images/811812841798500354_10.jpg)

Fig. 10 Cooling heat flux as a function of thermoelectric leg thickness when diamond is used as the TEC substrate and bulk $Bi_2Te_3$ as thermoelectric material ($ZT=0.9$)

flux at the cold side junction [54-57]. These reported results show solid-state ther- moelectric coolers that provide a powerful alternative to traditional high-flux coolers and offer great promise for reducing the severity of on-chip hot spots.

Succeeding sections of this chapter will address the possible application of these proposed approaches to the thermal management of nanoelectronic hot spots. Attention will be focused on silicon thermoelectric coolers, mini-contact, miniatur- ized TECs that overcome the present heat flux limitations of conventional $Bi_2Te_3$ devices, two-phase micro-gap coolers that can directly cool high heat flux chips without the deleterious effects of contact resistance, and the use of anisotropic ther- mal interface materials (TIM) to enhance the effectiveness of both passive and active cooling, in suppressing the temperature rise in high-flux regions of the chip.

## 2 On-Chip Hot-Spot Cooling Using Thermoelectric Microcoolers

Since the discovery of the Peltier effect in 1834, extensive research has been done to develop solid-state refrigeration devices and solid-state energy generators based on thermoelectric effects. However, only limited applications of thermoelectric cooling existed until the middle 1950s, when it was discovered that doped semiconduc- tors could achieve better thermoelectric properties than metallic materials. After

several decades of research, the efficiency of thermoelectric cooling devices still reached only about 10% of Carnot efficiency in comparison to the 30% efficiency typical of vapor compression refrigerators. The progress in thermoelectrics research declined until the early 1990s, when theoretical predications indicated that low-dimensional structures, such as two-dimensional superlattices, could be used to produce high-performance thermoelectric materials. Since then extensive studies, theoretical as well as experimental, have been conducted to explore new materials and new designs for fabrication of high-performance thermoelectric coolers. Since 2000, the demand for hot-spot cooling in microprocessors, as well as in power electronic, RF, and laser components, has generated renewed interest in exploring novel thermoelectric microcoolers, which can provide localized, high-flux cooling capability.

## 2.1 Principle of Conventional Thermoelectric Cooler (TEC)

The principle of conventional thermoelectric coolers was developed 50 years ago by Ioffe and coworkers [58]. A typical TEC consists of an array of n-type and p-type thermoelectric elements, two ceramic substrates that provide mechanical support for the TEC, electric conductors that provide a serial electric connection for the thermoelectric elements and electric contacts to lead wires, solders that join the thermoelectric elements, and lead wires that are connected to the ending conductors and deliver power from a DC electrical source. When semiconductor TEC devices are assembled, the array of heavily doped p-type and n-type semiconductor elements is soldered to ceramic substrates so that they are connected electrically in series and thermally in parallel. As is known, electrons can move freely in electrical conductors but less in semiconductors. When the electrons leave an electric conductor and enter the p-type semiconductor, they drop down to a lower energy level and release heat at the interface. However, as the electrons move across the bonded interface from the p-type semiconductor into the electric conductor, they transition to a higher energy level and absorb heat. When these electrons then move into the n-type semiconductor, they rise further in energy level so that additional heat is absorbed. When the electrons leave the n-type semiconductor and enter the conductor they drop down to a lower energy level and release heat during the process. Thus, in this thermoelectric circuit, heat is always absorbed when electrons enter n-type semiconductor or leave p-type semiconductor, and heat is always released when electrons enter p-type semiconductor or leave n-type semiconductor. The precise heat pumping capacity of a TEC is proportional to the current and is dependent on the element geometry, number of couples, and thermoelectric properties of the materials.

Figure 11 shows the basic configuration of a thermoelectric cooler with one p-type element and one n-type element. For a single-stage TEC, as shown in Fig. 11, the amount of heat that can be pumped at the cold side of a TEC is the net of three contributions. If we assume to have perfect thermal interfaces at the cold side and

Fig. 11 Sketch of a
thermoelectric cooler

![](./images/811812841798500354_11.jpg)

the hot side and neglect the Thomson effect, the net cooling power on the cold side
of the TEC can be expressed by:

$$
q_{\mathrm{c}}=\left(S_{\mathrm{p}}-S_{\mathrm{n}}\right) I T_{\mathrm{c}}-K\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)-\frac{1}{2} I^{2} R_{e} \tag{3}
$$

where $R$ is the overall electrical resistance of the TEC:

$$
R_{e}=\rho_{\mathrm{p}} \frac{L_{\mathrm{p}}}{A_{\mathrm{p}}}+\rho_{\mathrm{n}} \frac{L_{\mathrm{n}}}{A_{\mathrm{n}}} \tag{4}
$$

$K$ is the overall thermal conductance of the TEC

$$
K=k_{\mathrm{p}} \frac{L_{\mathrm{p}}}{A_{\mathrm{p}}}+k_{\mathrm{n}} \frac{L_{\mathrm{n}}}{A_{\mathrm{n}}} \tag{5}
$$

and $S$, $k$, $\rho$, $A$, and $L$ represent the Seebeck coefficient, thermal conductivity, electrical resistivity, the cross-section area, and the thickness of thermoelectric element, respectively. The p and n denote p-type and n-type thermoelectric materials, while $T_{\mathrm{h}}$ and $T_{\mathrm{c}}$ are the temperatures at the cold side and the hot side of the TEC, respectively. The overall cooling rate is driven by the Peltier cooling (the first term) and reduced by the heat flowing back from the hot side to the cold side of the TEC (the second term) and Joule heating in the element (the third term).

When a current is applied to the TEC, a voltage drop is generated, which includes
the resistive voltages and the Seebeck voltages across the thermoelectric elements
and is given by:

$$
V=\left(S_{\mathrm{p}}-S_{\mathrm{n}}\right)\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)+I R \tag{6}
$$

Therefore, the electric power consumption of the TEC system is equal to

$$
W=(S_{\mathrm{p}}-S_{\mathrm{n}})(T_{\mathrm{h}}-T_{\mathrm{c}})I+I^{2}R \tag{7}
$$

The coefficient of performance (COP) is used to describe the cooling efficiency of the TEC, and is the ratio of the net cooling power at the cold side and the power consumption of the system and is given by:

$$
\mathrm{COP}=\frac{q_{\mathrm{c}}}{W}\frac{(S_{\mathrm{p}}-S_{\mathrm{n}})IT_{\mathrm{c}}-K(T_{\mathrm{h}}-T_{\mathrm{c}})-\frac{1}{2}I^{2}R_{\mathrm{e}}}{(S_{\mathrm{p}}-S_{\mathrm{n}})(T_{\mathrm{h}}-T_{\mathrm{c}})I+I^{2}R} \tag{8}
$$

The maximum cooling rate that can be achieved by this TEC device can be deter- mined by differentiating the cooling rate given in Equation (3) to find the optimal current $I_{\text{opt}}$:

$$
\left(\frac{dq_{\mathrm{c}}}{dI}\right)_{\mathrm{opt}}=0 \Rightarrow \quad I_{\mathrm{opt}}=\frac{(S_{\mathrm{p}}-S_{\mathrm{n}})T_{\mathrm{c}}}{R_{\mathrm{e}}} \tag{9}
$$

When $I=I_{\mathrm{opt}}$, the heat removal rate attains its maximum, value given by:

$$
q_{\mathrm{max}}=\frac{1}{2}\frac{(S_{\mathrm{p}}-S_{\mathrm{n}})^{2}T_{\mathrm{c}}^{2}}{R_{\mathrm{e}}}-K(T_{\mathrm{h}}-T_{\mathrm{c}}) \tag{10}
$$

To determine the largest temperature reduction, i.e., the deepest cooling, that the TEC can achieve, the heat removed from the cold side is set equal to zero, $q_{\text{max}}=$ 0, yielding the maximum temperature difference across the TEC, i.e., from the cold side to the hot side of the thermoelectric cooler:

$$
\Delta T_{\mathrm{max}}=\frac{(S_{\mathrm{p}}-S_{\mathrm{n}})^{2}T_{\mathrm{c}}^{2}}{2KR_{\mathrm{e}}}=\frac{ZT_{\mathrm{c}}^{2}}{2} \tag{11}
$$

where $Z$ is known as the TEC figure of merit, given by

$$
Z=\left[\frac{(S_{\mathrm{p}}-S_{\mathrm{n}})}{(k_{\mathrm{p}}\rho_{\mathrm{p}})^{0.5}+(k_{\mathrm{n}}\rho_{\mathrm{n}})^{0.5}}\right]^{2} \tag{12}
$$

For simplification, it is frequently assumed that the semiconductor Seebeck coef- ficients of the two materials are equal but opposite in sign, i.e., $S_{\mathrm{p}}=-S_{\mathrm{n}}=S$, and that the thermal conductivity, electrical resistivity, and dimensions are equal for the two elements, i.e., $\rho_{\mathrm{p}}=\rho_{\mathrm{n}}=\rho, k_{\mathrm{p}}=k_{\mathrm{n}}=k, A_{\mathrm{p}}=A_{\mathrm{n}}=A, L_{\mathrm{p}}=L_{\mathrm{n}}=L$, so Equation (12) can be simplified as

$$
Z=\frac{S^{2}}{k\rho} \tag{13}
$$

Then the maximum achievable temperature difference at the optimized current,
$I = I_{\text{opt}}$, when the heat flow is zero, can be calculated as

$$
\Delta T_{\max }=\frac{S^{2} T_{\mathrm{c}}^{2}}{2 k \rho}=\frac{1}{2} Z T_{\mathrm{c}}^{2}
\tag{14}
$$

Similarly, the maximum cooling rate at the optimized current ($I = I_{\text{opt}}$), when the
hot side and cold side are equal in temperature can be calculated as:

$$
q_{\max }=\frac{S^{2} T_{\mathrm{c}}^{2}}{2 R_{\mathrm{e}}}=\frac{S^{2} T_{\mathrm{c}}^{2} A}{2 d \rho}
\tag{15}
$$

The corresponding cooling heat flux at the cold side of the TEC can be calculated
as:

$$
q_{\max }^{\prime \prime}=\frac{q_{\max }}{2 A}=\frac{S^{2} T_{\mathrm{c}}^{2}}{2 d \rho}
\tag{16}
$$

It is interesting to note that the maximum achievable cooling $\Delta T_{\max }$ only depends
on the figure of merit Z and the temperature of the cold side of the TEC, but it does
not change with the cross-sectional area or thickness of the TEC elements. To attain
the lowest temperature, it is desirable to have a thermoelectric material with a high
value of Z. Alternatively, when thermal conduction is not an important parasitic
effect, the power factor $P$, defined by Equation (17), is often used to characterize
the thermoelectric properties of a given material:

$$
P \quad=\frac{S^{2}}{\rho}
$$

The maximum COP can be found by differentiating the COP given in Equation
(8) to find the COP-optimal current $I_{\text{COP,opt}}$:

$$
\left(\frac{\mathrm{dCOP}}{\mathrm{d} I}\right)_{\mathrm{opt}}=0 \Rightarrow \quad I_{\mathrm{COP}, \mathrm{opt}}=\frac{\left(S_{\mathrm{p}}-S_{\mathrm{n}}\right)\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)}{R_{\mathrm{e}}\left(1+Z T_{\mathrm{ave}}\right)^{0.5}-1}
\tag{18}
$$

When $I = I_{\text{COP,opt}}$, the maximum value of COP can be calculated:

$$
\mathrm{COP}_{\text {max }}=\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}-T_{\mathrm{c}}} \frac{\left(1+Z T_{\text {ave }}\right)^{0.5}-T_{\mathrm{h}} / T_{\mathrm{c}}}{\left(1+Z T_{\text {ave }}\right)^{0.5}+1}
\tag{19}
$$

where $T_{\text{ave}} = (T_{\mathrm{h}} + T_{\mathrm{c}})/2$ is the mean temperature of the TEC.

## 2.2 Thermoelectric Cooling Materials and Devices

As described in the last section, for conventional thermoelectric applications, the best thermoelectric materials are those providing the highest $Z$ values, usually associated with high Seebeck coefficients, high electrical conductivities and low thermal conductivities. So far, the best thermoelectric material properties are found in heavily doped semiconductors. In semiconductors, the thermal conductivity is established by the flow of both electrons and phonons, but with much of the thermal transport ascribed to phonons. The phonon thermal conductivity can be reduced without causing significant reduction in the electrical conductivity. A common approach to reduce the phonon thermal conductivity is through alloying or doping because the mass difference scattering in alloys or doped semiconductors reduces the lattice thermal conductivity significantly without much degradation in the electrical conductivity.

Bismuth telluride-based compounds, using alloys of $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ with $\mathrm{Sb}_{2} \mathrm{Te}_{3}$ (p-type) and $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ with $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ (n-type), are the best commercial state-of-the-art materials for thermoelectric cooling, with the highest values of the figure of merit $ZT$. In bulk materials, a $ZT$ of 0.75 for p-type $(\mathrm{BiSb})_{2} \mathrm{Te}_{3}$ at room temperature was reported about 40 years ago. Since the 1960s, much effort has been made to raise the $ZT$ of bulk materials based on bismuth telluride by doping or alloying other elements in various fabrication processes. Recently, a $ZT$ of 1.14 at 300 K has been reported for the p-type $(\mathrm{Bi}_{0.25} \mathrm{Sb}_{0.75})_{2}(\mathrm{Te}_{0.97} \mathrm{Se}_{0.03})_{3}$ alloy [59]. By annealing the ingots prepared by the Bridgman method, Yamashita et al. have most recently achieved a significant increase in the $ZT$ value to 1.19 at 298 K for the $n$-type $\mathrm{Bi}_{2}(\mathrm{Te}_{0.94} \mathrm{Se}_{0.06})_{3}$ and 1.41 at 308 K for the p-type $(\mathrm{Bi}_{0.25} \mathrm{Sb}_{0.75})_{2} \mathrm{Te}_{3}$ alloy, so that both $ZT$ values exceed 1 [60-62]. In addition to alloying, several other approaches have been proposed to enhance the $ZT$ value, through either improving electrical conductivity or reducing thermal conductivity. In this respect, low-dimensional materials, such as quantum wells, superlattices, quantum wires, and quantum dots offer new ways to manipulate the electron and phonon properties of a given material. Some experiments have demonstrated that superlattice thermoelectric materials can achieve $ZT$ values greater than 2.0. These inspiring results show the feasibility of applying thermoelectric materials to high-flux cooling applications.

Thermoelectric coolers (TECs) have traditionally been fabricated using bulk bismuth telluride materials and traditional processing techniques such as hot pressing sintering and extrusion. Commercial bulk thermoelectric coolers are made from such thermoelectric elements, typically several millimeters in thickness and combined into arrays that span $1.8 \times 3.4$ mm (and 2.4 mm thick) to $62 \times 62$ mm (and 5.8 mm thick). For such commercial TE modules, the maximum cooling at room temperature is about $70^{\circ} \mathrm{C}$, with relatively low cooling heat flux of 5–$10 \mathrm{~W} / \mathrm{cm}^{2}$, which makes it impossible to use such TECs for high-flux hot-spot cooling application [63]. Because the maximum cooling heat flux of a TEC is inversely proportional to the thickness of its elements, there have been extensive studies focusing on microscaled thin-film TECs, miniatured TECs, and nanostructured superlattice TECs, which could realize high-flux cooling requirement

for on-chip hot-spot reduction. In recent years, significant progresses have been reported in making microscaled thermoelectric coolers, as described in the three sections that follow.

### 2.2.1 Thin-Film Thermoelectric Coolers (TFTECs)
It is widely accepted that thin-film thermoelectric coolers (TFTECs) have great potential for high-flux cooling because of the dramatic theoretical increase in cool- ing heat flux made possible by decreasing thermoelectric element thickness as given by Equation (16). Among the available deposition methods, electrochemical depo- sition is very attractive from an application perspective, due to its ability to deposit thin films at high deposition rates of tens of microns per hour and at the much lower batch processing cost when compared to other state-of-the-art thin-film fabrication processes [64]. Snyder et al. used electrochemical-MEMS technique to fabricate thin-film thermoelectric microcoolers, which contains 63 n-type $Bi_2Te_3$ elements and 63 p-type $Bi_{2-x}Sb_xTe_3$ elements, each element being $20\ \mu m$ in thickness and $60\ \mu m$ in diameter with bridging metal interconnects, as shown in Fig. 12 [65]. Unfortunately, the defect structure in this MEMS TEC produced a high concen- tration of low-mobility carriers, yielding an estimated $Z$ value of $3.2\times 10^{-5}$ (1/K) and producing a maximum cooling of $2^\circ$C and a maximum cooling heat flux of $7\ W/cm^2$.

![](./images/811812841798500354_12.jpg)

Fig. 12 Thin-film thermoelectric microcooler fabricated by MEMS [65]

Using co-evaporation as the deposition method, da Silva et al. fabricated thin-film thermoelectric microcoolers, which provided 60 n-type and p-type thermoelectric element pairs, with the thickness and width of the elements approximately 4.5 and $40\ \mu m$, respectively, as shown in Fig. 13. In da Silva's most recent work, the Seebeck coefficient, electrical resistivity, and power factor values of $149\ \mu$V/K, $1.25\times 10^{-5}$ $\Omega$m, and $1.78\ mW/K^2m$, respectively, were achieved for p-type $Sb_2Te_3$ thin films at the optimized deposition temperature [66]. However, the overall thermoelec- tric cooling performance achieved with such improved thin films has not been reported.

Böttner et al. developed a two-wafer process to fabricate thin film thermoelectric coolers. Figure 14 depicts a schematic drawing of the two wafer process on the left

![](./images/811812841798500354_13.jpg)

Fig. 13 $Bi_2Te_3$ and $Sb_2Te_3$ films deposited on Cr/Au/Ti/Pt bottom connectors [66]

and a schematic drawing of the resulting device on the right. The polycrystalline n-type $Bi_2(Se,Te)_3$ and p-type $(Bi,Sb)_2Te_3$ materials were deposited by co-sputtering from 99.995% element targets (Bi, Sb, Te). However, these alloys were not grown very well in thin-film form due to delivery problems of the Se-target suppliers. For these coolers, the thickness of n-type $Bi_2Te_3$ elements and p-type $(Bi,Sb)_2Te_3$ elements is about 20 $\mu$m as shown in Fig. 14 [67]. While he initially reported a net cooling of $11^\circ$C at $60^\circ$C ambient, more recently, Böttner et al. reported achieving a maximum temperature differences of nearly $48^\circ$C at an applied current of 2.1 A, and a maximum cooling flux of $\sim$100 W/cm² for the complete device [68].

![](./images/811812841798500354_14.jpg)

Fig. 14 Micro-Peltier cooler. Left: Schematic drawing of the developed two wafer (I,II) concept. Right: Schematic drawing of the thermoelectric cooler used for telecommunication device [67]

Zou et al. found that direct vapor deposition of bismuth telluride compounds is made difficult by the large difference in the vapor pressure between antimony, bismuth, and tellurium, which could result in noncongruence and in a lack of stoichiometry. In his work, $Sb_2Te_3$ films were deposited by co-evaporation of antimony and tellurium and $Bi_2Te_3$ thin films by co-evaporation of bismuth and tellurium onto heated, clean glass substrates. The figure of merit Z for the p-type $Sb_2Te_3$ film and n-type $Bi_2Te_3$ film was calculated and found to be approximately $1.04 \times 10^{-3}$ at

room temperature, corresponding to $ZT$ of 0.32. The maximum temperature difference measured between the hot and cold ends was $15.5^\circ$C at a current of 55 mA, showing a promising procedure for fabricating thermoelectric microcooler [69].

In using the state-of-the-art deposition techniques to develop thermoelectric thin films, a primary difficulty is to maintain the stoichiometry of the bismuth telluride compounds. For example, the problem of resputtering during the film growth is present in sputter deposition, while differences in volatility of the component elements pose difficulty in vacuum evaporation. A large deviation from stoichiometry arises in vapor deposition because the constituent elements in the target exhibit dissimilar sticking coefficients on the substrate. In addition, there is a tendency for re-evaporation of certain elements from the deposited thin films because of their higher vapor pressure. Therefore, the thermoelectric properties of these thin films reported in the above publications vary widely and the figure of merit ($ZT$) is always much small than $\sim$1.0 for bulk bismuth telluride material. As shown in Table 1, to date thin film thermoelectric coolers are still not well developed and complete characterization of the material properties of the various TEC thin films is lacking.

<table>
<caption>Table 1 Summary of cooling performance of $Bi_2Te_3$-based thin-film TEC</caption>
<thead>
  <tr>
    <th>Author (year)</th>
    <th>Growth method</th>
    <th>$\Delta T_{\text{max}}$ ($^\circ$C)</th>
    <th>$q''^{\text{max}}$ ($\text{W/cm}^2$)</th>
    <th>TE properties</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Snyder (2002)</td>
    <td>Electrochemical deposition</td>
    <td>2@$80^\circ$C</td>
    <td>7</td>
    <td>$S=60$–$100\ \mu\text{V/K}$<br>$ZT$=0.01 (estimated)</td>
  </tr>
  <tr>
    <td>Zuo (2002)</td>
    <td>Co-sputtering</td>
    <td>15.5@$25^\circ$C</td>
    <td>N/A</td>
    <td>p-type:<br>$S=160\ \mu\text{V/K}$<br>$\rho=3.12\times10^{-5}\ \Omega\text{m}$<br>n-type:<br>$S=-200\ \mu\text{V/K}$<br>$\rho=1.29\times10^{-5}\ \Omega\text{m}$</td>
  </tr>
  <tr>
    <td>da Silva (2005)</td>
    <td>Co-evaporation</td>
    <td>1.0@$25^\circ$C</td>
    <td>N/A</td>
    <td>p-type:<br>$S=228\ \mu\text{V/K}$<br>$\rho=2.83\times10^{-5}\ \Omega\text{m}$<br>n-type:<br>$S=-149\ \mu\text{V/K}$,<br>$\rho=1.25\times10^{-5}\ \Omega\text{m}$</td>
  </tr>
  <tr>
    <td>Böttner (2005)</td>
    <td>Co-sputtering</td>
    <td>48@$25^\circ$C</td>
    <td>100@$25^\circ$C</td>
    <td>p-type:<br>$S=180\ \mu\text{V/K}$<br>$\rho=1.30\times10^{-5}\ \Omega\text{m}$<br>n-type:<br>$S=-175\ \mu\text{V/K}$<br>$\rho=1.95\times10^{-5}\ \Omega\text{m}$</td>
  </tr>
</tbody>
</table>

### 2.2.2 Bulk Miniaturized Thermoelectric Coolers

Although thin-film deposition technology has an advantage for mass production, currently it appears not to provide thermoelectric cooling performance comparable to that available in bulk TECs, due to the difficulty in controlling thin-film growth

conditions to obtain the desired stoichiometry and a defect-free microstructure. Alternatively, attention can be turned to miniaturized thermoelectric coolers, based on thinning of bulk materials, which can reduce thermoelectric element thickness down to tens of microns and, at the same time, maintain the excellent thermoelectric properties of the bulk materials. Table 2 shows the progress in developing bulk miniaturized TECs since the 1960s [70].

**Table 2 Thermoelectric cooling of bulk $Bi_2Te_3$-based miniaturized TEC**

<table>
<thead>
<tr>
<th rowspan="2">Year</th>
<th rowspan="2">TEC configuration</th>
<th colspan="2">TE element</th>
<th rowspan="2">$\Delta T_{\text{max}}$ ($^\circ$C)</th>
<th rowspan="2">$q''_{\text{max}}$ ($\text{W/cm}^2$)</th>
</tr>
<tr>
<th>Thickness ($\mu$m)</th>
<th>TE properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>1967</td>
<td>Single TE couple</td>
<td>130</td>
<td>$ZT=0.54$</td>
<td>38 @30$^\circ$C</td>
<td>95</td>
</tr>
<tr>
<td>1994</td>
<td>20 couple TECs</td>
<td>100</td>
<td>$ZT=0.78$</td>
<td>50 @30$^\circ$C</td>
<td>100</td>
</tr>
<tr>
<td>1997</td>
<td>120 couple TECs</td>
<td>200</td>
<td>$ZT=0.78$</td>
<td>67 @30$^\circ$C</td>
<td>65</td>
</tr>
<tr>
<td>2002</td>
<td>18 couple TECs</td>
<td>200</td>
<td>$ZT=0.90$</td>
<td>70.6 @30$^\circ$C<br>91.8 @85$^\circ$C</td>
<td>80<br>98</td>
</tr>
<tr>
<td>2006</td>
<td>18 couple TECs</td>
<td>130</td>
<td>$ZT$$=0.90$</td>
<td>64.2 @30$^\circ$C<br>83.5 @85$^\circ$C</td>
<td>110<br>132</td>
</tr>
</tbody>
</table>

In 1967 Semenyuk began developing bulk bismuth telluride material, which could be used to form very short thermoelectric elements [71]. Following years of development, in 2006 Semenyuk thinned the thermoelectric element down to 130 $\mu$m, as shown in Fig. 15. The extruded p-type and n-type bismuth telluride thermoelectric materials were in the form of rods with $Z$ values of $3.02\times 10^{-3}$ $\text{K}^{-1}$, corresponding to $ZT$ value of 0.9. The 200 $\mu$m thick p-type and n-type slices were initially cut from the rods using electroerosion process. Then the slices were lapped to the final thickness of 130 $\mu$m, etched electrochemically, and nickel plated.

![](./images/811812841798500354_15.jpg)

Fig. 15 Thermion TECs with 130 $\mu$m thick TE elements

AlN ceramic substrates were used with metal patterns obtained by standard micro-electronics processing, including vacuum deposition of thin-film adhesive layers followed by electrochemical growth of thick copper films through photoresist processing, nickel plating, and finally Tin solder electrodeposition. The modules were found to provide a maximum cooling of 64.2 and 83.5°C and a maximum cooling flux of 110 and 132 W/cm² when operated at 30°C and 85°C, respectively, offering somewhat lower temperature reductions than achieved by the miniaturized TEC with 200 µm thick elements but improving the cooling heat flux by 30% under both conditions.

### 2.2.3 Nanostructured Thermoelectric Cooler
Nanostructured low-dimensional materials, such as superlattices, quantum wells, quantum wires, and quantum dots, offer opportunities to manipulate the electron and phonon properties of a given material leading to new ways to increase *ZT*. In a low-dimensional n-type material, the Fermi level is lower and the Seebeck coefficient is higher than that for corresponding bulk semiconductors with the same electron concentration, enhancing the value of the product of $S^{2}/\rho$, the power factor. Dresselhaus and coworkers theoretically predicted that the use of quantum well nanostructures could increase the power factor via quantum size effects, which improve the electron performance by taking advantage of sharp features in the electron density of states and result in *ZT* values in the range of 2–3 [72]. In addition, thermal conductivity can be reduced due to significantly modified phonon dispersion and enhanced phonon scattering mechanisms using the short period superlattice to impede phonon transport without excessively restricting the carrier flow [73, 74]. Experimental studies have demonstrated significant thermal conductivity reduction in a wide variety of nanostructured superlattices [75], leading to significant enhancements of the thermoelectric figure of merit for $\text{Bi}_{2}\text{Te}_{3}/\text{Sb}_{2}\text{Se}_{3}$ and PbTe/PbTeSe superlattice nanomaterials [76, 77]. Table 3 compares the reported power factor, *ZT*, and thermal conductivity of these nanostructured materials with that of their corresponding bulk materials at room temperature. It is clear that thermal conductivity reduction plays a significant role in the reported *ZT* enhancement and consequently there is only a small improvement in the power factor. It is interesting to note that these nanostructured materials can also be used to achieve multilayer thermionic (TI) cooling,

**Table 3 Thermoelectric properties of nanostructured materials with high *ZT* [80]**

<table>
  <thead>
    <tr>
      <th rowspan="2">Thermoelectric properties at 25°C</th>
      <th>PbTe–PbSeTe quantum dot superlattices</th>
      <th>PbTe–PbSe bulk alloy</th>
      <th>$\text{Bi}_{2}\text{Te}_{3}$–$\text{Sb}_{2}\text{Te}_{3}$ superlattices</th>
      <th>$\text{Bi}_{2}\text{Te}_{3}$–$\text{Sb}_{2}\text{Te}_{3}$ bulk alloy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure of merit *ZT*</td>
      <td>1.6</td>
      <td>0.35</td>
      <td>2.4</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>Thermal conductivity (W/m K)</td>
      <td>0.6</td>
      <td>2.5</td>
      <td>0.5</td>
      <td>1.45</td>
    </tr>
    <tr>
      <td>Power factor (mW/K²·m)</td>
      <td>3.2</td>
      <td>2.8</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>

[78, 79] which allows for reduced parasitic Joule heating, since transport through the thin barriers is largely ballistic.

Venkatasubramanian used metal–organic chemical vapor deposition (MOCVD) to epitaxially grow a 5 $\mu$m thick $Bi_2Te_3/Sb_2Te_3$ nanostructured superlattice on GaAs substrates in 2001 [81]. These are phonon-blocking/electron-transmitting superlattices, which are produced by alternately depositing thin (1–4 nm) films of $Bi_2Te_3$ and $Sb_2Te_3$. $ZT$ was reported to be 2.4 for p-type $Bi_2Te_3/Sb_2Te_3$ superlattices and 1.4 for n-type $Bi_2Te_3/Bi_2Te_{2.83}Se_{0.17}$ at room temperature. This high $ZT$ was explained by a reduction of the lattice thermal conductivity due to scattering of the phonons at the superlattice interfaces. The maximum cooling of 32.2 and $40^\circ$C was measured using an infrared camera and the maximum cooling flux of 585 and $700\ W/cm^2$ was estimated for p-type $Bi_2Te_3/Sb_2Te_3$ superlattice at the temperatures of $25^\circ$C and $80^\circ$C, respectively, with a response time of only about $5\ \mu$s.

More recently, PbSeTe-based quantum dot superlattice grown by molecular beam epitaxy (MBE) was reported by Herman's group for thermoelectric cooling applications [39]. The superlattice thin film with a thickness of approximately 100 $\mu$m was grown on $BaF_2$ substrates. The developed superlattice thin-film n-type PbSeTe/PbTe has a $ZT$ of 1.6–2.0 at room temperature and achieved a maximum cooling of $43.7^\circ$C at 700 mA, under vacuum conditions, as shown in Fig. 16. It should be noted that theoretically increasing the $ZT$ value will increase the maximum temperature differential of the TEC through $\Delta T_{\text{max}} = 0.5ZTc_{\text{c}}^2$. However, for on-chip hot-spot cooling,

![](./images/811812841798500354_16.jpg)

Fig. 16 Thermoelectric cooling characteristics of one-leg device made from n-type PbSeTe/PbTe superlattice thermoelectric cooler. $\Delta T$ represents measured data points of temperature differential between the hot junction temperature $T_{\text{hot}}$ and $T_{\text{cold}}$ cold junction temperature

$ZT$ does not appear to be the relevant figure of merit. It was found that the materials with the same $ZT$ will not necessarily provide equal degrees of hot-spot cooling and, among three material parameters which determine $ZT$ value, increase of Seeback coefficient is most effective to improve hot-spot cooling than decrease of electrical resistivity and thermal conductivity of the thermoelectric materials [82].

Shakouri and coworkers fabricated thin-film SiGe/Si, and SiGeC/Si thermoelectric microcoolers based on superlattice nanostructures using molecular beam epitaxy (MBE) [83-87]. As the SiGe/Si superlattice microcoolers can be monolith- ically integrated with microelectronic components to achieve localized cooling and temperature control, such devices could provide advantages for on-chip hot-spot cooling. The microcooler structure is based on cross-plane electrical transport and the main part of the microcooler is a $3\ \mu$m thick strain-compensated SiGe/Si super- lattice, as shown in Fig. 17. It consists of 200 periods of 12 nm $Si_{0.9}Ge_{0.1}/3$ nm Si, doped with boron to about $6\times 10^{19}\ \mathrm{cm}^{-3}$. A maximum cooling of $4.5^{\circ}\mathrm{C}$ at $25^{\circ}\mathrm{C}$, $7^{\circ}\mathrm{C}$ at $100^{\circ}\mathrm{C}$ and $14^{\circ}\mathrm{C}$ at $250^{\circ}\mathrm{C}$ was demonstrated. The maximum cooling heat flux increases with decreasing microcooler size, increasing from 120 to $680\ \mathrm{W/cm^{2}}$ when the microcooler sizes reduces from $100\times 100\ \mu$m to $60\times 60\ \mu$m. Table 4 is the summary of cooling performance of thin-film nano-structured superlattice microcoolers developed since 2000.

![](./images/811812841798500354_17.jpg)

### 2.2.4 Silicon Thermoelectric Materials and Microcoolers

While single-crystal silicon has been the key semiconductor material for much of the microelectronics era, silicon's thermoelectric potential has been largely ignored because of its high thermal conductivity and thus low value of the traditional TEC figure of merit, $ZT(\approx 0.017)$ [88, 89]. However, silicon thermoelectric microcool- ers, when formed on the back of the silicon chip for hot-spot cooling, provide

<table>
<caption>Table 4 Summary of cooling performance of nanostructured superlattice TEC</caption>
<thead>
<tr>
<th>Year</th>
<th>Superlattice</th>
<th>$\Delta T_{\text{max}}$ (K)</th>
<th>$q_{\text{max}}$ ($\text{W/cm}^2$)</th>
<th>Properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>LaBounty (2000)</td>
<td>InGaAs/InGaAsP</td>
<td>1.2@$25^\circ$C<br>2.3@$90^\circ$C</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>Fan (2002)</td>
<td>SiGe/Si<br>SiGeC/Si</td>
<td>4.5@$25^\circ$C<br>7.0@$100^\circ$C<br>14.0@$250^\circ$C</td>
<td>680@$25^\circ$C</td>
<td>$S = 200\ \mu\text{V/K}$<br>$k = 6.8$–$8.7\ \text{W/m K}$<br>$P = 2.2\ \text{mW/K}^2\text{m}$<br>$ZT = 0.085$</td>
</tr>
<tr>
<td>Venkatasubramanian (2001)</td>
<td>$\text{Bi}_2\text{Te}_3/\text{Sb}_2\text{Te}_3$</td>
<td>32.2@$25^\circ$C<br>40@$80^\circ$C</td>
<td>585@$25^\circ$C<br>700@$80^\circ$C</td>
<td>$ZT = 2.4$<br>$P = 4.0\ \text{mW/K}^2\text{m}$</td>
</tr>
<tr>
<td>Herman (2002)</td>
<td>PbSeTe/PbTe</td>
<td>43.7 @$25^\circ$C</td>
<td>N/A</td>
<td>$ZT = 1.6$<br>$P = 3.2\ \text{mW/K}^2\text{m}$</td>
</tr>
<tr>
<td>Zhang (2003)</td>
<td>AlGaAs/GaAs</td>
<td>0.8@$25^\circ$C<br>2.0@$100^\circ$C</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

unique advantages over TFTECs. As may be seen in Table 5, which provides the thermal and electrical properties for three conventional thermoelectric materials – bulk $\text{Bi}_2\text{Te}_3$ alloy bulk SiGe alloy and single-crystal silicon – at room temperature, single-crystal silicon appears to offer the highest power factor of the materials shown, due to its high Seebeck coefficient and low electrical resistivity, and thus constitutes a very viable candidate for high-flux on-chip cooling.

<table>
<caption>Table 5 Typical values on the thermoelectric properties for $\text{Bi}_2\text{Te}_3$, SiGe and single-crystal silicon at room temperature [90]</caption>
<thead>
<tr>
<th>Material</th>
<th>Seebeck coefficient, $S$ ($\mu\text{V/K}$)</th>
<th>Electrical resistivity, $\rho$ ($\mu\Omega\ \text{m}$)</th>
<th>Thermal conductivity, $k$ ($\text{W/m K}$)</th>
<th>Figure of merit</th>
<th>Power factor $P$ ($\text{mW/K}^2\text{m}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{Bi}_2\text{Te}_3$ (n-type)</td>
<td>$-240$</td>
<td>$10$</td>
<td>$2.02$</td>
<td>$Z = 2.85 \times 10^{-3}$<br>$ZT = 0.86$</td>
<td>$5.76$</td>
</tr>
<tr>
<td>$\text{Bi}_2\text{Te}_3$ (p-type)</td>
<td>$162$</td>
<td>$5.5$</td>
<td>$2.06$</td>
<td>$Z = 2.32 \times 10^{-3}$<br>$ZT = 0.70$</td>
<td>$4.77$</td>
</tr>
<tr>
<td>SiGe (n-type)</td>
<td>$-136$</td>
<td>$10.1$</td>
<td>$4.45$</td>
<td>$Z = 0.328 \times 10^{-3}$<br>$ZT = 0.1$</td>
<td>$1.83$</td>
</tr>
<tr>
<td>SiGe (p-type)</td>
<td>$144$</td>
<td>$13.2$</td>
<td>$4.80$</td>
<td>$Z = 0.413 \times 10^{-3}$<br>$ZT = 0.12$</td>
<td>$1.57$</td>
</tr>
<tr>
<td>Silicon (p-type)</td>
<td>$450$</td>
<td>$35$</td>
<td>$150$</td>
<td>$Z = 0.039 \times 10^{-3}$<br>$ZT = 0.012$</td>
<td>$5.79$</td>
</tr>
</tbody>
</table>

Zhang and Shakouri developed a silicon thermoelectric microcooler using bulk silicon which is p-type boron doped at a doping concentration of around $10^{19}\ \text{cm}^{-3}$ [91]. The device structure, which was fabricated with standard microfabrication techniques: dry etch, lithography, metal evaporation, etc., is illustrated in Fig. 18. They experimentally demonstrated the ability of such silicon thermoelectric

![](./images/811812841798500354_18.jpg)

Fig. 18 A SEM photo of silicon microcooler [91]

microcoolers to achieve a surface temperature reduction of $1.2^\circ$C and a cooling flux of $580\ \text{W/cm}^2$ for a $40\ \mu\text{m} \times 40\ \mu\text{m}$ microcooler operating at room temper- ature at an optimized current of 0.1 A. In anticipation of the application of these microcoolers to the thermal management of microprocessor hot spots, and using an analytical model – with the embedded temperature dependence of electrical resis- tivity, thermal conductivity, and Seebeck coefficient based on values reported for single-crystal silicon [92, 93], Bar-Cohen et al. predicted the achievable tempera- ture reduction, cooling heat flux, and parametric sensitivities of such thermoelectric microcoolers at $100^\circ$C [94]. The results displayed in Fig. 19 reveal that, in the absence of parasitic effects – Joule heating from electric contact resistance and heat conduction from metal lead, the silicon microcooler with the described configura- tion could achieve a maximum temperature reduction of $6.2^\circ$C on the microcooler at the optimum current of 0.9 A.

Figure 20 shows the maximum attainable temperature reduction on the micro- cooler, at an operating temperature of $100^\circ$C, for various doping concentrations with the microcooler size ranging from $20 \times 20\ \mu\text{m}$ to $100 \times 100\ \mu\text{m}$. The high- est maximum temperature reduction of $6.2^\circ$C is achieved at a doping concentration of $2.5 \times 10^{19}\ \text{cm}^{-3}$, and is independent of microcooler size. However, as shown in Fig. 20(b), smaller microcoolers do achieve the optimal performance at lower cur- rents. In Fig. 20(a), the maximum average temperature reduction over the entire microcooler surface (average cooling) is also included for comparison. It is found that the maximum average cooling is approximately 30% lower than the maximum peak cooling.

One of the main advantages of silicon microcoolers is the very high cooling heat flux made possible by the high power factor for silicon. As with any thermoelec- tric cooler, the maximum cooling flux is achieved at a negligibly small temperature

![](./images/811812841798500354_19.jpg)

Fig. 19 Variation of silicon microcooler performance with applied current

![](./images/811812841798500354_20.jpg)

Fig. 20 (a) Variation of maximum temperature difference with the doping concentration for the ideal case and (b) Dependence of temperature difference on the applied current for different microcooler sizes at 100°C

reduction, while the greatest temperature reduction is achieved with negligibly small heat flux. For the present microcooler configuration, Figure 21 shows that the maximum cooling heat flux attains a predicted maximum value of $1\ \text{kW/cm}^2$ for $100 \times 100\ \mu\text{m}$ microcooler and $6\ \text{kW/cm}^2$ for $20 \times 20\ \mu\text{m}$ microcooler. These

![](./images/811812841798500354_21.jpg)

Fig. 21 Variation of heat load flux with temperature difference on the microcooler at 100°C

results support the expectation that silicon microcoolers provide a very promising approach to high heat-flux spot cooling in silicon microprocessors.

### 2.3 Hot-Spot Cooling Using Silicon Thermoelectric Microcooler

The concept of silicon thermoelectric microcooler for on-chip hotspot cooling, fabricated on the back of the silicon chip, is illustrated in Fig. 22, which displays a single microcooler, activated by an electric current entering the silicon chip through the metal contact and the silicon cap, flowing laterally through the chip, and exiting at the ground electrode located on the periphery of the chip. In a thermoelectric circuit, the flow of electrons across the interface between dissimilar materials, each with a distinct Seebeck coefficient, induces the Peltier effect, providing localized cooling when the direction of the current flow is from the low Seebeck coefficient to the high Seebeck coefficient material. The flow of electric current also serves to transport the absorbed heat away from that junction and to deposit that heat at a secondary interface where the electric current flows from the high Seebeck coefficient to the low Seebeck coefficient material. Joule heating, associated with the resistance to electric current in the thermoelectric circuit, and heat conduction from the hot junction to the cold junction of the thermoelectric circuit limit the thermoelectric cooling that can be achieved. The possible use of silicon thermoelectric

![](./images/811812841798500354_22.jpg)

Fig. 22 Silicon thermoelectric microcooler for on-chip hot-spot cooling (The arrows indicate the direction for electric current)

microcoolers for the remediation of on-chip hot spots is facilitated by the use of well-established metal-on-silicon fabrication techniques, yielding a very low thermal contact resistance between the electrodes and the chip. In addition, incor- poration of the silicon chip into the thermoelectric circuit makes it possible to transfer the absorbed energy via the electric current to the edge of the chip, far from the location of the hot spot, thus substantially reducing the detrimental effect of thermoelectric heating on the temperature of the active circuitry.

Referring to the structure of the on-chip silicon microcooler depicted in Fig. 22, it may be seen that Peltier cooling occurs at the junction between the metal contact and the silicon cap which is highly doped silicon with a doping concentration of more than $1 \times 10^{20} \mathrm{~cm}^{-3}$ and again at the silicon cap/silicon chip interface, and that Peltier heating is encountered at the silicon chip/ground electrode interface, located on the periphery of the chip, where the electrons must shed some of their energy in entering the highly conductive metal. The overall Peltier heat-transfer (cooling) rate of the silicon microcooler can be expressed as:

$$
q_{\mathrm{TE} \times \mathrm{c}}=-S_{\mathrm{Si}} T_{\mathrm{c}} I \tag{20}
$$

where $T_{\mathrm{c}}$ is the absolute temperature at the microcooler, $S_{\mathrm{Si}}$ the Seebeck coefficient of the silicon chip, and $I$ the applied current. Similarly, the Peltier heating rate at the silicon chip/ground electrode interface can be represented as:

$$
q_{\mathrm{TE}, \mathrm{h}}=S_{\mathrm{Si}} T_{\mathrm{ed}} I \tag{21}
$$

where $T_{\mathrm{ed}}$ is the absolute temperature at the ground electrode. In addition to volumetric Joule heating inside the silicon chip, the silicon cap, and the metal con- tact, these parasitic effects also arise at both the metal contact/silicon cap interface

and the silicon chip/ground electrode interface. The interfacial Joule heating at the metal contact/silicon cap interface is given by:

$$q_{\text{contact}} = I^2 R_{\text{cont}} = I^2 \rho_{\text{c}} / A_{\text{cont}} \tag{22}$$

where $R_{\text{cont}}$ is the electric contact resistance, $A_{\text{cont}}$ the cross-sectional area of metal contact, and $\rho_{\text{c}}$ the specific electric contact resistance at this interface. Equation (22) applies as well at the peripheral ground electrode/silicon chip interface, with the appropriately adjusted contact area and the specific electric contact resistance.

In the work of Bar-Cohen [95] a test vehicle was used, consisting of a $12 \times 12$ mm silicon chip with $70 \, \text{W/cm}^2$ background heat flux and $70 \times 70 \, \mu\text{m}$ hotspot, with a heat flux of $680 \, \text{W/cm}^2$, located at the center of the active side of the chip, to explore the hot-spot cooling potential of this approach. In their extensive modeling studies, the back of the chip was cooled with a high-performance $25^\circ\text{C}$ air-cooled heat sink, capable of producing an effective heat-transfer coefficient of $8700 \, \text{W/m}^2\text{K}$ representing the combined effect of the heat sink, heat spreader, and thermal interface materials used for electronic packages [96, 97]. The thermal conductivity of the silicon chip is assumed to be $110 \, \text{W/mK}$, appropriate for $100^\circ\text{C}$ operating temperature [98].

The prediction of hot-spot cooling achievable with on-chip silicon microcooler, as described in Fig. 23, requires the solution of the three-dimensional Poisson's equation for the temperature distribution in a volume subjected to nonuniform heat generation, associated with the Joule heating in the silicon chip, heating and cooling boundary conditions, associated with Peltier cooling and Peltier heating on the back surface, along with the microprocessor heat generation on the front surface (active circuitry), i.e.,

![](./images/811812841798500354_23.jpg)

Fig. 23 (a) Coordinate system and (b) boundary conditions in the analytical model for the silicon chip integrated with silicon thermoelectric microcooler

$$
\frac{\delta^{2} T}{\delta x^{2}}+\frac{\delta^{2} T}{\delta y^{2}}+\frac{\delta^{2} T}{\delta z^{2}}+\frac{q_{\mathrm{Si}}^{\prime \prime \prime}(x, y, z)}{k_{\mathrm{Si}}}=0
\tag{23}
$$

where $q_{\mathrm{Si}}{ }^{\prime \prime \prime}(x, y, z)$ is the nonuniform volumetric heat generation due to the silicon Joule heating and $k_{\mathrm{Si}}$ is the thermal conductivity of the silicon chip. Unfortunately, solution of Equation (23) requires detailed knowledge of the internal heat generation function, $q_{\mathrm{Si}}{ }^{\prime \prime \prime}(x, y, z)$. Determination of this function requires a parallel solution of the Laplace's equation for the electric potential field, which will vary significantly with the geometries of the silicon chip and the silicon microcooler and the placement of the ground electrode. The resulting highly nonuniform heat generation function can be expected to render Equation (23) analytically unsolvable for all but the simplest approximations of $q_{\mathrm{Si}}{ }^{\prime \prime \prime}(x, y, z)$.

Alternatively, considering the common use of "allocation factors" in determining the performance of one-dimensional thermoelectric devices [99] and the successful application of this approach to silicon thermoelectric microcoolers in an earlier publication by the authors, it is possible to re-formulate Equation (23) in the Laplace's form by allocating an appropriate fraction of the Joule heating to the microcooler ($\alpha$) and the hot spot ($\beta$), respectively. With this approach, the volumetric silicon Joule heating is replaced with modified boundary conditions at the microcooler and the hot spot, respectively, and the Poisson's equation can then be transformed into the Laplace's equation for this same domain, which can be solved analytically.

In subsequent sections, the hot-spot remediation capability of silicon microcoolers will be characterized by three distinct metrics, including:

(1) $\Delta T$ - the temperature reduction anywhere in the studied domain that is achievable by activating the microcooler. This metric characterizes the intrinsic thermoelectric cooling capability of the silicon microcooler. It is generally applied to the hot spot or the microcooler in this study and given by:

$$
\Delta T=T_{\text {cooler, on }}-T_{\text {cooler, off }}
\tag{24}
$$

(2) $\Delta T_{\text {hot spot }}{ }^{*}$ - the ratio of the temperature change at the hot spot due to activating the microcooler to the temperature rise engendered by the hot spot. This metric quantifies the hot-spot cooling effectiveness of the silicon microcooler and is defined as:

$$
\Delta T_{\text {hot spot }}^{*}=\frac{T_{\text {hot spot on, cooler off }}-T_{\text {hot spot on, cooler on }}}{T_{\text {hot spot on, cooler off }}-T_{\text {hot spot off, cooler off }}}
\tag{25}
$$

For $\Delta T_{\text {hot spot }}{ }^{*}=1$, the temperature rise engendered by the hot spot can be completely removed by the microcooler. For $\Delta T_{\text {hot spot }}{ }^{*}=0$, the microcooler is totally ineffective and for $0<\Delta T_{\text {hot spot }}{ }^{*}<1$, the microcooler can achieve partial success in reducing the hot-spot temperature. For $\Delta T_{\text {hot spot }}{ }^{*}>1$, the microcooler is capable of "overcooling" the hot spot relative to the base temperature of the silicon chip.

(3) $\pi$ – the thermal impact factor, which provides a measure of the power needed, $P_{\text{in}}$, to achieve a specified temperature reduction at the hot spot, $\Delta T_{\text{hot spot}}$. This dimensional metric (K/W$_{\text{elec}}$) can be expressed as:

$$
\pi = \frac{-\Delta T_{\text{hot spot}}}{q_{\text{in}}} \tag{26}
$$

Clearly, as $\pi$ increases less electric power is required in order to achieve a specific temperature reduction at the hot spot.

Following the transformation above, Bar-Cohen and coworkers developed a three-dimensional analytical thermal model of on-chip hot-spot cooling to inves- tigate the effectiveness of such silicon thermoelectric microcoolers for a wide range of hot-spot sizes and heat fluxes, microcooler sizes, silicon chip thicknesses, doping concentrations, and electric contact resistances. The analytical solution yields the temperature distribution in the silicon chip, under the influence of hot-spot heating and background heating from related circuitry on the active surface, Peltier cooling, Peltier heating and conductive/convective cooling on the opposite surface, volumet- ric Joule heating inside the silicon chip, and interfacial Joule heating at the electric contact created by the silicon microcooler. The analytical solution employs numer- ically derived allocation factors to redistribute the Joule heating inside the chip to the hot spot and the microcooler. Results obtained from a three-dimensional electro- thermal finite-element numerical simulation were used to validate and calibrate the analytical model. The parametric trends revealed by use of this analytical model are presented and discussed in subsequent sections.

### 2.3.1 Doping Concentration Effect

The thermoelectric properties of semiconductors are strongly dependent on doping concentration but modestly on the doping type [100–103]. Figure 24 shows that the electrical resistivity of silicon decreases with increasing doping concentration, while the Seebeck coefficient also displays an inverse relationship with doping concentra- tion. Thus, increasing doping concentration results in lower electrical resistivity and, as a consequence, less Joule heating in the silicon chip, but, the associated decrease in the Seebeck coefficient leads to reduced thermoelectric cooling power.

The largest possible thermoelectric cooling power is attained by maximizing the thermoelectric power factor $P$ ($= S^2 \rho$), which for boron-doped single-crystal sili- con at $100^\circ$C occurs at about $2.5 \times 10^{19}\ \text{cm}^{-3}$. The variation of maximum hot-spot cooling with doping concentration for various microcooler sizes is presented in Fig. 24 for $100\ \mu\text{m}$ thick chip and the specific electric contact resistance ranging from $1 \times 10^{-7}$ to $1 \times 10^{-4}\ \Omega\text{cm}^2$, revealing – as expected – that across the range of microcooler sizes studied, with increasing doping concentration, the hot-spot cooling increases until reaching a maximum value and then decreases with further increases in the doping concentration.

![](./images/811812841798500354_24.jpg)

Fig. 24 Electrical resistivity ($\rho$), Seebeck coefficient ($S$), and power factor ($P$) as a function of boron doping concentration ($N_{\rm d}$) in single-crystal silicon [104-106]

It is interesting to find that, despite the three-dimensional characteristic of heat spreading and electrical current spreading in the silicon chip surrounding the micro- cooler, for small electric contact resistance, e.g., $\rho_{\rm c} < 1 \times 10^{-5}\ \Omega \, {\rm cm}^2$, the optimum

![](./images/811812841798500354_25.jpg)

Fig. 25 Hot-spot cooling as a function of boron doping concentration for various specific electric contact resistances. The hot spot is $70 \times 70\ \mu{\rm m}$ with a heat flux of $680\ {\rm W/cm}^2$ and the microcooler size is $600 \times 600\ \mu{\rm m}$. The microcooler size is $600 \times 600\ \mu{\rm m}$

doping concentration is nearly equal to $2.5 \times 10^{19}\ \text{cm}^{-3}$, which yields the maximum power factor shown in Fig. 24. However, it is to be noted that the parasitic effect from larger electric contact resistance does have an influence on the optimum doping concentration, yielding a lower optimized doping concentration of $1.5 \times 10^{19}\ \text{cm}^{-3}$ for a $600 \times 600\ \mu\text{m}$ microcooler with the specific electric contact resistance of $1.0 \times 10^{-4}\ \Omega\text{cm}^2$. It has been found that this trend becomes more pronounced as the microcooler size gets smaller.

It should be noted that the optimum doping level for a silicon thermoelectric microcooler is, thus, likely to be substantially higher than commonly used in semiconductor silicon chips. However, as is almost always the case for chip thermal management, the present analysis assumes that the back of the chip is used for cooling while the front is used for the active circuitry. Consequently, the doping concentration on the back side of the chip need not equal the more common doping concentration in the active semiconductor regions at the front of the chip, e.g., $1 \times 10^{16}\ \text{cm}^{-3}$. Due to the far higher electrical resistivity in the active silicon layer, the electric current that is used to activate thermoelectric cooling is not expected to penetrate into this region.

### 2.3.2 Microcooler Size Effect

The effect of microcooler size on cooling performance involves the interplay of thermoelectric cooling by the microcooler and thermal diffusion from the hot spot to the microcooler. With decreasing microcooler size, the effective cooling flux and thus the temperature reduction at the microcooler increases, while the thermal resistance between the hot spot and the microcooler also increases. Consequently, this larger cooling flux at smaller microcoolers cannot effectively translate into larger temperature reduction at the hot spot. On the other hand, with smaller thermal resistances between the hotspot and the microcooler, the more modest cooling flux on larger microcoolers can be projected effectively onto the hot spot, narrowing the temperature difference between the hot spot and the microcooler. However, the modest cooling flux achievable on the larger microcoolers reduces the beneficial temperature reduction at both the hot spot and the microcooler. The competition between these two effects results in an optimum microcooler size.

Figure 26 displays this behavior and shows the temperature reductions at the hot spot and the microcooler for a wide range of microcooler sizes for $100\ \mu\text{m}$ thick chip operating under the background and hot-spot heat fluxes of $70\ \text{W/cm}^2$ and $680\ \text{W/cm}^2$, respectively. For each microcooler, the applied current is carefully optimized in order to achieve the maximum temperature reductions at the hot spot. It is seen that the temperature reduction at the hot spot first increases with microcooler size and, after reaching the maximum value of $3.0^\circ\text{C}$ for $600 \times 600\ \mu\text{m}$ microcooler, decreases with a further increase in microcooler size. Interestingly, the temperature reduction at the microcooler varies monotonically with microcooler size, yielding progressively larger temperature reductions, to as much as $3.9^\circ\text{C}$, as the microcooler dimension shrinks to $100 \times 100\ \mu\text{m}$, which, however, only provides $1.6^\circ\text{C}$ temperature reduction at the hot spot.

![](./images/811812841798500354_26.jpg)

Fig. 26 Variation of temperature reductions at the hot spot and the microcooler with microcooler size. The hotspot is $70 \times 70\ \mu$m with a heat flux of $680\ \text{W/cm}^2$

### 2.3.3 Chip Thickness Effect

In the application of silicon microcoolers to hot-spot remediation, the silicon chip plays multiple roles, functioning as a thermoelectric material, to provide on-chip cooling and, at the same time, as an electrical conductor to transfer electrons from the ground electrode to the microcooler, and as a thermal conductor to provide a diffusion path for the heat generated in the chip to the ambient. Therefore, the chip thickness influences Joule heating distribution inside the chip, heat spreading from the hot spot, heat diffusion from the hot spot to the microcooler, and heat diffu- sion from the ground electrode, where Peltier heating occurs, to the hot spot. As the chip becomes thinner, the thermal resistance between the microcooler and the hot spot decreases, allowing the microcooler to achieve greater hot-spot temperature reductions, e.g., $2.05$–$3.03^\circ\text{C}$ as the chip thickness decreases from 500 to $100\ \mu$m, for the conditions of Fig. 28. However, due to the smaller heat-spreading effect in thinner chips, the temperature rise engendered by the hot spot is also higher for thinner chips and increases with decreasing chip thickness from $2.2^\circ\text{C}$ for a $500\ \mu$m thick chip to $2.9^\circ\text{C}$ for $100\ \mu$m thick chip. These two trends compete with each other, yielding the maximum hot-spot cooling effectiveness at the chip thickness of $200\ \mu$m, with $\Delta T_{\text{hot spot}^*}=1.2$ as shown in Fig. 27. At this chip thickness, the silicon microcooler is, thus, capable of reducing the hot-spot tempera- ture below the baseline temperature of the chip by approximately $0.5^\circ\text{C}$. Moreover, for the present $70 \times 70\ \mu$m hot spot with a heat flux of $680\ \text{W/cm}^2$, the silicon microcooler is capable of completely suppressing or over-cooling the hot spot, with $\Delta T_{\text{hot spot}^*}\geq1$, for the chip thicknesses between 100 and $475\ \mu$m.

![](./images/811812841798500354_27.jpg)

Fig. 27 Hot-spot cooling and hot-spot cooling effectiveness as a function of chip thickness. The hot spot is $70 \times 70\ \mu$m with a heat flux of $680\ \text{W/cm}^2$

It is interesting to find that the chip thickness also influences the optimum micro- cooler size. As shown in Figs. 28 and 29, the thicker the silicon chip the larger the optimized microcooler size. For $100\ \mu$m thick chip, the maximum hot-spot cooling of $3.0^\circ\text{C}$, for the conditions studied, is achieved with a $600 \times 600\ \mu$m

![](./images/811812841798500354_28.jpg)

Fig. 28 Hot-spot cooling as a function of microcooler size for various chip thicknesses. The hot spot is $70 \times 70\ \mu$m with a heat flux of $680\ \text{W/cm}^2$

![](./images/811812841798500354_29.jpg)

Fig. 29 Hot-spot cooling effectiveness as a function of microcooler size for various chip thicknesses. The hotspot is $70 \times 70\ \mu\text{m}$ with a heat flux of $680\ \text{W/cm}^2$

microcooler, while for $500\ \mu\text{m}$ thick chip, $2500 \times 2500\ \mu\text{m}$ silicon microcooler is required in order to attain the maximum hot-spot cooling of $2.1^\circ\text{C}$. It should be noted that the optimum ratio of microcooler size to chip thickness is, thus, approximately 5.5, with a modest sensitivity to chip thickness, reaching 6.0 for $100\ \mu\text{m}$, $200\ \mu\text{m}$ and $300\ \mu\text{m}$ thicknesses, dropping to 5.5 for the $400\ \mu\text{m}$ thick chip, and to 5.0 for the $500\ \mu\text{m}$ chip. This decreasing ratio can be related to the growing contributions of silicon Joule heating and Peltier heating to the hot-spot temperature as the optimized current – necessitated by the larger microcooler – increases.

Figure 30 shows the dependence of the thermal impact factor, $\pi$, of the silicon microcooler, on the microcooler size for different chip thicknesses, revealing that this factor and the relative benefit of input power decreases steeply with the microcooler size but more gently with the chip thickness. For example, $200 \times 200\ \mu\text{m}$ microcooler can achieve a $\pi$ of 17.0 in comparison with 1.2 for $4000 \times 4000\ \mu\text{m}$ microcooler on $100\ \mu\text{m}$ thick chip. With an increase of microcooler size, the effect of chip thickness on the thermal impact factor becomes less important. Consequently, this example for the specific parameters of the "test vehicle" used to explore the cooling potential of the silicon microcoolers, suggests that more generally the largest $\pi$ values and the best returns on invested energy are attained when smaller microcoolers are used to remediate hot spots on thinner chips.

![](./images/811812841798500354_30.jpg)

Fig. 30 Thermal impact factor as a function of microcooler size for various chip thicknesses. The hot spot is $70 \times 70\ \mu$m with a heat flux of $680\ \text{W/cm}^2$

### 2.3.4 Electric Contact Resistance Effect

The miniaturization of thermoelectric coolers tends to exacerbate the deleterious effects of the electric contact resistance, which is expected to occur at the interface between the metal contact and the silicon cap. The theoretical value of the specific electric contact resistance between highly doped silicon and a metal contact is in the range of $1 \times 10^{-9}\ \Omega\text{cm}^2$ at room temperature or above [104]. However, due to process-related limitations, the typical specific electric contact resistance at such an interface usually ranges from $1 \times 10^{-7}$ to $1 \times 10^{-5}\ \Omega\text{cm}^2$, with significant batch to batch variations. Figure 31 shows the impact of the electric contact resistance on hot-spot cooling for different microcooler sizes on $100\ \mu$m thick chip. It should be noted that for a typical state-of-the-art thin-film process, which yields an average specific electric contact resistance of approximately $1 \times 10^{-6}\ \Omega\text{cm}^2$ [105], the results displayed in Fig. 31 reveal that the electric contact resistance induced degradation in hot-spot cooling can be neglected.

More generally, as the specific electric contact resistance increases, hot-spot cooling performance is degraded, but the electric contact resistance has a larger impact for smaller microcooler sizes because the contact resistance is inversely proportional to the microcooler area. For an increase in the specific electric contact resistance from $1 \times 10^{-9}$ to $1 \times 10^{-4}\ \Omega\text{cm}^2$, hot-spot cooling will be degraded by a factor of 6.5 for $100 \times 100\ \mu$m microcooler but only by 5% for $3000 \times 3000\ \mu$m microcooler.

![](./images/811812841798500354_31.jpg)

Fig. 31 Hot-spot cooling as a function of specific electric contact resistance for various micro-
cooler sizes. The hot spot is $70 \times 70\ \mu$m with a heat flux of $680\ W/cm^2$

### 2.3.5 Hot-Spot Parameter Effect

Finally, attention is turned to the effects of the hot-spot parameters – namely, hot-
spot size and hot-spot heat flux – on cooling performance, as evaluated by the three
proposed metrics – $\Delta T$, $\Delta T^*$, and $\pi$. For each hot-spot size and hot-spot heat flux,
the applied current, the microcooler size, and the doping concentration have been
optimized in order to achieve the maximum hot-spot temperature reduction, while
the specific electric contact resistance is fixed at $1 \times 10^{-6}\ \Omega\mathrm{cm}^2$. It was found that
the optimized current and thus the optimized input power increase slightly with hot-
spot size and hot-spot heat flux if the chip thickness and the doping concentration
in the silicon chip remain constant. As may be seen in Figs. 32, 33, and 34 for
$100\ \mu$m thick chip, the efficacy of the silicon microcooler varies with these hot-spot
parameters in a complex manner. For example, the maximum temperature reduction
at the hot spot, shown in Fig. 32, increases from $3.0^\circ$C for $70 \times 70\ \mu$m hot spot
with $680\ W/cm^2$ heat flux to $3.90^\circ$C for $400 \times 400\ \mu$m hot spot with $1000\ W/cm^2$
heat flux, primarily because of the effect of the higher chip temperature (105 vs.
$150^\circ$C) on the Peltier cooling rate. However, as seen in Fig. 33, the maximum cool-
ing effectiveness decreases steeply with hot-spot size and hot-spot heat flux, from
1.05 for $70 \times 70\ \mu$m hot-spot with $680\ W/cm^2$ heat flux to 0.08 for $400 \times 400\ \mu$m
hot-spot with $1000\ W/cm^2$ heat flux. Interestingly, since as the hot-spot size and the
hot-spot heat flux increases, the maximum hotspot temperature reduction increases
while the optimized input power remains nearly constant, $\pi$, the thermal impact fac-
tor, increases with the hot-spot size and the heat flux, as shown in Fig. 34. It should,
thus, be understood that the silicon microcoolers can produce the largest cooling
effect for constant input power when encountering large, high heat flux hot spots.

![](./images/811812841798500354_32.jpg)

Fig. 32 Hot-spot temperature reduction as a function of hot-spot size and hot-spot heat flux

![](./images/811812841798500354_33.jpg)

Fig. 33 Hot-spot cooling effectiveness as a function of hot-spot size and hot-spot heat flux

![](./images/811812841798500354_34.jpg)

Fig. 34 Thermal impact factor as a function of hot-spot size and hot-spot heat flux. The microcooler size is $600 \times 600\ \mu\text{m}$

## 2.4 Mini-Contact-Enhanced TEC for Hot-spot Cooling

Solid-state thermoelectric coolers (TECs), which are highly reliable, can be locally applied for spot cooling, and can be integrated with IC processing, have been pro- posed for hot-spot thermal management. However, the relatively low cooling heat flux, $5$-$10\ \text{W/cm}^2$, of conventional TEC modules severely limits the application of these devices to hot-spot remediation. Recently, a novel use of a mini-contact pad, which connects the TEC and the silicon chip, thus concentrating the thermoelectric cooling power on the top of the silicon chip to significantly improve hot-spot cool- ing performance, was proposed and investigated [106]. The physical phenomenon underpinning the use of mini-contact-enhanced thermoelectric coolers is displayed in Fig. 35, where the mini-contact is seen to concentrate the thermoelectric cooling power on the reduced cross-sectional area of the mini-contact tip. It can be expected that, to a first approximation, the smaller the cross-sectional area of the mini-contact tip, the larger the cooling flux on the top of the silicon chip. Moreover, the local- ization of the TEC cooling flux to the region most affected by the hot spot reduces the overall cooling requirements and the input power needed to effectively utilize the TEC.

To analyze and optimize the on-chip hot-spot cooling performance of the mini-contact-enhanced TEC, a three-dimensional numerical thermal model was

![](./images/811812841798500354_35.jpg)

Fig. 35 Schematic of a TEC (consisting of numerous N-type and P-type TE elements sandwiched between two ceramic substrates) attached on silicon chip and embedded inside thermal interface material (TIM) of the chip package: (a) TEC without a mini-contact and (b) TEC with an integrated mini-contact. The arrows indicate the heat flow pattern in silicon chip and mini- contact. The detailed chip package is not shown in this figure

developed using the commercial finite element software ANSYS™ and applied
to a typical chip package with a mini-contact-enhanced TEC, as shown in Fig. 36.
This package consists of a silicon chip, thermal interface materials (TIM), a copper-
integrated heat spreader (IHS), an air-cooled aluminum heat sink, and a miniaturized
bismuth telluride-based TEC. The TEC is integrated with a mini-contact pad,
attached on the top of the silicon chip, and then embedded inside the thermal
interface materials, TIM1 and TIM2. These could be different thermal interface
materials such as solder or thermal grease. The TEC consists of a $4 \times 4$ array
of $400 \times 400 \times 20\ \mu$m thermoelectric elements that are sandwiched between two
$50\ \mu$m thick ceramic substrates, and is $120\ \mu$m in overall height [107]. The copper

![](./images/811812841798500354_36.jpg)

Fig. 36 Schematic of a typical chip package with a mini-contact-enhanced TEC

mini-contact pad features a $2.4\ \text{mm} \times 2.4\ \text{mm} \times 100\ \mu\text{m}$ base to facilitate heat spreading, and a $2.4\ \text{mm} \times 2.4\ \text{mm} \times 50\ \mu\text{m}$ tip to concentrate the thermoelectric cooling capability. For the purposes of this study, the thickness of TIM1 was held constant at $300\ \mu\text{m}$ so that the mini-contact enhanced TEC and the TIM1 layer could be accommodated within the height of the TIM1 thermal interface layer.

When a mini-contact-enhanced TEC is integrated into the chip package, it introduces several thermal interfaces. In consideration of possible assembly procedures for such an enhanced TEC, it is assumed that the two most important thermal interfaces occur between the top ceramic substrate and the TIM2, and between the mini-contact tip and the silicon die, as indicated in Fig. 36. $R_{\text{c1}}$ and $R_{\text{c2}}$ are used to represent these two thermal contact resistances, with each varying from $1 \times 10^{-7}$ to $1 \times 10^{-4}\ \text{m}^2\text{K/W}$, the typical range reported for electronic package application [108, 109]. In the simulation, thermoelectric cooling rate, $Q_{\text{TE cooling}}$, is determined as the product of the Seebeck coefficient, temperature, and current, $ST_{\text{c}}I$, where $S$ is the Seebeck coefficient of the thermoelectric material, $T_{\text{c}}$ the cold-side junction temperature at the TEC, and $I$ the applied electrical current on the TEC. Similarly, the Peltier heating rate at the heat rejection side of the device, $Q_{\text{TE heating}}$, is given by the product $ST_{\text{h}}I$, where $T_{\text{h}}$ is the hot-side junction temperature at the TEC. Thermoelectric cooling and heating effects are represented as heat flux boundary conditions in the numerical simulation and directly added to the cold and hot sides of the TEC, respectively, while Joule heating is modeled as uniform volumetric heat generation inside the bismuth telluride elements. Joule heating from the electrical contact resistance is modeled as a surface boundary condition at the two TEC junctions [110]. Since the hot-spot cooling performance is strongly dependent on the input power supplied to the TEC, in the course of this simulation, various electric currents are applied to the TEC until the lowest hot-spot temperature is achieved and usually it takes about 10 min to complete a simulation using Pentium IV processor.

### 2.4.1 Effect of Input Power on TEC

Thermoelectric cooling performance is dependent on the applied current or input power to the TEC in a nonlinear manner, as Peltier cooling has a favorable linear dependence on electric current, while the parasitic Joule heating effect has a quadratic dependence on electric current. The competition of these two opposite contributions leads to an optimum current or input power at which the maximum hot-spot cooling, or lowest hot-spot temperature, can be achieved. Figure 37 demonstrates the variation of the hot-spot temperature with the input power to the TEC, for a TE element thickness of $20\ \mu\text{m}$ and the mini-contact tip size of $1250 \times 1250\ \mu\text{m}$. The thermal contact resistance is chosen to be $1 \times 10^{-7}\ \text{Km}^2/\text{W}$ at both the mini-contact tip/silicon chip interface and the ceramic/TIM2 interfaces. For a $400 \times 400$ $\mu\text{m}$ hot spot with a heat flux of $1250\ \text{W/cm}^2$, if there is no TEC, the peak hot-spot temperature is found to reach $137.0^\circ\text{C}$. However, if the TEC is activated, the hot-spot temperature decreases steeply as the power increases, reaching a minimum of $120^\circ\text{C}$ at approximately 10 W, which corresponds to a temperature reduction of

![](./images/811812841798500354_37.jpg)

Fig. 37 Variation of typical hot-spot temperature with the input power on TEC (Thermoelectric element thickness $=20\ \mu\text{m}$, copper mini-contact tip size $=1250\times1250\ \mu\text{m}$)

17.0°C at the hot spot compared to the temperatures encountered without the TEC, and then rises slowly as the power increases further. It is worth noting that if the TEC is present but not activated, the hot-spot temperature will increase by 7°C, due to the additional thermal resistance to heat flow created by the presence of the TEC.

### 2.4.2 Effect of Mini-Contact Size

The mini-contact pad, sandwiched between the TEC and the silicon chip, is used to concentrate the thermoelectric cooling rate on the top of the silicon chip. Its ben- eficial effect on hot-spot cooling could be limited by the heat-spreading resistance inside the mini-contact pad as well as inside the silicon chip. Consequently, care should be taken to optimize the geometric configuration to achieve the maximum hot-spot cooling performance. Figure 38 shows the temperature profiles achieved along a line bisecting the bottom of the silicon chip, with and without an embedded TEC, and revealing the characteristic "W"-shaped temperature profile created by the mini-contact-enhanced TEC cooler. It may be seen that if there is no hot spot on the chip and no TEC embedded inside the package, the peak chip temperature is about $109^\circ\text{C}$. However, if there is a $400\times400\ \mu\text{m}$ hot spot with a heat flux of

![](./images/811812841798500354_38.jpg)

Fig. 38 Effect of mini-contact size on TEC-induced temperature profile (Thermoelectric element thickness $=20\ \mu$m, input power $=10$ W)

$1250\ \text{W/cm}^2$, the peak chip temperature will increase to $137^\circ\text{C}$. Therefore, the concentrated heat flux leads to about a $28^\circ\text{C}$ peak temperature rise on the chip. If the TEC with a thermoelectric element thickness of $20\ \mu$m is activated with a 10 W input and enhanced with a $600\times600\ \mu$m mini-contact pad, the temperature profile created around the high-flux region, shows a $9^\circ\text{C}$ reduction in the hot-spot temperature (to $128^\circ\text{C}$), a low-temperature ring with temperatures below the uniform heat dissipation values, and a warm outer ring with slowly decaying temperatures in the radial direction. If the mini-contact tip grows to $1250\times1250\ \mu$m, the hot-spot temperature will reduce further, down to $120^\circ\text{C}$, resulting in $17^\circ\text{C}$ maximum cooling at the hot spot. However, if we expand the mini-contact size further, to $2400\times2400\ \mu$m, the hot-spot cooling is limited to just $12^\circ\text{C}$. Obviously there exists an optimum mini-contact size for each configuration. The observed temperature increases in the outer ring or "side lobes" of the profile, as well as a very modest increase in the average chip temperature, is due to the additional power dissipation associated with the operation of the TEC device.

Figure 39 shows the heat flux distribution along the line bisecting the top surface of the silicon chip, just below the TEC enhanced with three different sizes of copper mini-contacts. On the top of the silicon chip and far away from the contact zone, the heat flux is approximately $70\ \text{W/cm}^2$, the same as the background heat flux on

![](./images/811812841798500354_39.jpg)

Fig. 39 Effect of mini-contact size on heat flux on the top of silicon chip (Thermoelectric element thickness $=20\ \mu$m, input power $=10$ W)

the bottom of the silicon chip. However, at the interface between the mini-contact and the silicon chip, the heat flux increases significantly, indicating a strong cooling effect from the activated TEC. The heat flux averaged over the entire surface of the mini-contact/silicon chip interface increases from 250 to $640\ \text{W/cm}^2$, and then to $1600\ \text{W/cm}^2$ when the copper mini-contact size decreases from $2400\times2400\ \mu$m to $1250\times1250\ \mu$m, and then to $600\times600\ \mu$m, suggesting that reduction of the mini-contact sizes can significantly increase the local cooling heat flux.

It is also interesting to note that the heat flux is highly nonuniform at the mini-contact/silicon chip interface, with the highest value occurring at the corner and the lowest value at the center. Although the cooling heat flux continues to increase with decreasing mini-contact size, the combined effect of the thermal resistance between the hot spot and the mini-contact area and this cooling flux results in the optimum mini-contact size previously shown in Fig. 38.

### 2.4.3 Effect of Thermoelectric Element Height
Thermoelectric element height is a key parameter for improving the hot-spot cooling performance as the maximum achievable cooling flux of the TEC is inversely proportional to the thermoelectric element thickness. Figure 40 illustrates the variation of hot-spot cooling with the mini-contact size for three different thermoelectric

![](./images/811812841798500354_40.jpg)

Fig. 40 Effect of thermoelectric element thickness $t_{TE}$ on the maximum hot-spot cooling performance. The optimized input power of 10, 7.5, and 6.1 W is applied on the TEC with the TE element thickness of 20, 50, and 100 $\mu$m, respectively

element heights, under optimized input power on the TEC. As is expected, shorter thermoelectric elements allow the TEC to achieve better hot-spot temperature reductions, e.g., $6^\circ$C to $11.2^\circ$C and to $17.0^\circ$C as the thermoelectric element decreases from 100 ${\mu}$m and to 20 ${\mu}$m in thickness, using the optimum mini-contact tip size. Even when the mini-contact tip size is kept constant, shorter thermoelectric elements always yield better hot-spot cooling than longer elements due to the higher fluxes extracted by the cold side of the TEC. However, it is interesting to find that for fixed contact resistances the optimum mini-contact tip size increases with decreasing element height, from $800 \times 800$ ${\mu}$m for a 100 ${\mu}$m thick element to $1000 \times 1000$ ${\mu}$m for a 50 ${\mu}$m thick element, and to $1250 \times 1250$ ${\mu}$m for a 20 ${\mu}$m high element.

As may be seen in Fig. 40, the TEC with 20 ${\mu}$m high elements has more dependence on the mini-contact size than the TECs with 50 ${\mu}$m or 100 ${\mu}$m high elements. It should be noted that the improvement provided by use of the mini-contact pad is larger with taller thermoelectric elements than with shorter elements. For the TEC with 20 ${\mu}$m thick elements, the addition of an optimally sized mini-contact pad improves the cooling by $4.3^\circ$C, from hot-spot cooling of $12.7^\circ$C with no mini-contact to $17^\circ$C with a $1250 \times 1250$ ${\mu}$m mini-contact. However, for the TEC with 100 ${\mu}$m thick elements, the addition of an optimally sized mini-contact pad reduces the hot-spot temperature by an additional $6^\circ$C, from hot-spot cooling of $0.1^\circ$C with no mini-contact to $6.1^\circ$C with a $800 \times 800$ ${\mu}$m mini-contact. Interestingly,

the deterioration in performance with suboptimum contact pads displays the reverse trend, with the hot-spot temperature rising steeply with reduced mini-contact area for the 20 µm thick TEC but more gradually for the 100 µm thick TEC.

### 2.4.4 Effect of Thermal Contact Resistance
Low thermal resistance interfaces are critical to mini-contact enhanced hot-spot cooling, since a high thermal resistance at the mini-contact/chip interface – where the cooling flux is highest – will significantly reduce the effectiveness of the mini-contact enhancement. Moreover, a bad thermal interface between the TEC and the TIM2 will impede the conduction of thermoelectric and Joule heat into the heat spreader and then into the heat sink and the ambient. Figure 41 displays the interplay between the thermal contact resistance and the achievable hot-spot cooling, with the assumption of equal thermal contact resistance at the two interfaces (e.g., $R_{\text{c1}} = R_{\text{c2}} = R_{\text{c}}$) and reveals that with increasing thermal contact resistance at both interfaces, the net cooling achievable on the hot spot diminishes. It may be seen that if the thermal contact resistance is $1 \times 10^{-5}\ \text{Km}^2/\text{W}$ or higher, the hot-spot temperature will exceed 140°C and the embedded TEC will raise rather than lower the hot-spot temperature.

The thermal contact resistance also has an impact on optimized mini-contact size. As shown in Fig. 41, with increasing thermal contact resistance, the optimized mini-contact increases from $1250 \times 1250\ \mu\text{m}$ for the thermal contact resistance of

![](./images/811812841798500354_41.jpg)

Fig. 41 Influence of thermal contact resistance on hot-spot cooling performance

$1 \times 10^{-7} \mathrm{Km}^{2} / \mathrm{W}$, representing a nearly perfect interface, to $2000 \times 2000 \mu \mathrm{m}$ for a thermal contact resistance of $1 \times 10^{-5} \mathrm{Km}^{2} / \mathrm{W}$, typical of thermal grease interfaces. It should be noted that if the thermal contact resistance is $5 \times 10^{-5} \mathrm{Km}^{2} / \mathrm{W}$ or lower, use of an optimized mini-contact tip always provides a lower hot-spot temperature than achieved without the mini-contact. However, the mini-contact is seen to provide diminishing returns as the contact resistances increase and to elevate the hot-spot temperatures for thermal contact resistances of $1 \times 10^{-5} \mathrm{Km}^{2} / \mathrm{W}$ or higher.

### 2.4.5 Experimental Demonstration
Thermal measurements were performed on the chip package test vehicle shown in Fig. 42 to quantify the spot cooling improvement provided by the mini-contact pad, and to determine its relationship to the TEC input power and power dissipation on the silicon chip. In this "proof of concept" experiment there are no micro-scaled hot spots and temperature sensors on the chip. Instead, a uniform heat flux is imposed on the bottom of the chip, by attaching four, thin-film heaters, and the mini-contact-enhanced TEC is used to locally cool that chip below the temperature of the surrounding silicon. The schematic of the experimental structure is shown in Fig. 42, displaying a $2.5 \mathrm{~mm} \times 2.5 \mathrm{~mm} \times 500 \mu \mathrm{m}$ silicon chip attached to four, thin-film heaters used to simulate chip power dissipation. The copper mini-contact pad with various mini-contact tip sizes, varying from $0.8 \times 0.8 \mathrm{~mm}$ to $3.6 \times 3.6 \mathrm{~mm}$, was bonded onto the silicon chip using an indium-based solder. To facilitate the sol-dering process, a $200 \mathrm{~nm}$ thick Ni thin-film adhesion layer deposited on the silicon and then a $200 \mathrm{~nm}$ thick Au layer deposited onto the Ni layer by an e-beam process were used [111]. The copper mini-contact pad was then soldered onto the silicon by indium solder, which reacted with the Au thin film at around $160^{\circ} \mathrm{C}$ to form an $\mathrm{AuIn}_{2}$ intermetallic compound.

![](./images/811812841798500354_42.jpg)

Fig. 42 Schematic of test vehicle for mini-contact-enhanced TEC for spot cooling

Miniaturized TECs from Thermion (model number: 1MC04-018-02-2200D) [112] with a dimension of $3.6 \times 3.6 \times 1.6$ mm and a total of 36 diced p-type and n-type $200 \, \mu\text{m}$ thick bismuth telluride thermoelectric elements, were used in these experiments. The thermal conductivity of bismuth telluride in the Thermion TEC is reported to be 1.3–1.4 W/m K, the Seebeck coefficient $200 \, \mu\text{V/K}$, and the electrical resistivity $10 \, \mu\Omega \text{m}$, with a figure of merit value $Z$ of $3 \times 10^{-3} \, \text{K}^{-1}$ [113]. The two ceramic substrates are made of AlN, each with a thickness of $635 \, \mu\text{m}$, and indium-tin solder was pre-tinned to the end faces to facilitate solder connections. In the present experiment, the TEC was attached to the mini-contact using thermal grease. The copper mini-contact pad and the TEC are accommodated inside the copper spacer. Above the copper spacer and the TEC, the copper heat spreader was attached using thermal grease. The heat spreader was then attached to the air-cooled copper heat sink.

Figure 43 shows the experimentally determined dependence of spot cooling on the TEC input power for a $500 \, \mu\text{m}$ thick silicon chip, with the mini-contact tip size kept at $1.8 \times 1.8$ mm and the power dissipation on the silicon chip varying from 0 to 67 W. It is found that the temperature reduction at the targeted spot (the center of the silicon chip) varies parabolically with the TEC input power, reflecting the competing mechanisms of rapidly improving Peltier cooling at lower input powers (or current) and progressively more damaging Joule heating, as well as reverse heat conduction, at the higher input powers. In this test vehicle, the silicon chip, thus, experiences its largest value of spot cooling at an input power of 3.5–5.5 W.

![](./images/811812841798500354_43.jpg)

Fig. 43 Variation of measured spot cooling with TEC input power

It is interesting to note that the power dissipation on the silicon chip has some effect on spot-cooling performance and that higher chip power dissipation leads to greater achievable spot cooling on the silicon chip. For example, if there is no power dissipation on the silicon chip, a maximum cooling of about $7.0^\circ$C can be achieved. However, if the power dissipation on the chip is increased to 67 W, the maximum spot cooling increases to around $9^\circ$C. This improvement in cooling performance is related primarily to the increase in the cold-side junction temperature of the TEC, which raises the Peltier cooling rate. Interestingly, this Peltier cooling improvement also leads to lower values of the optimum TEC input power, since at the higher temperature more effective cooling can be achieved at lower current or power. This trend is illustrated in Fig. 8, where an increase of the power dissipation on the silicon wafer from 0 to 70 W, is seen to produce a decrease in the optimum TEC input power from 5.7 to 3.6 W.

The experimentally observed effect of the mini-contact tip size on the temper- ature reduction at the targeted spot is displayed in Fig. 44. For the three different power dissipations and a $500\ \mu$m thick chip, the maximum spot cooling is seen to display a parabolic dependence on the mini-contact tip size, showing very favorable improvements as the mini-contact tip size decreases in area from the "full coverage" limit, but ultimately reversing direction as the tip size shrinks below an optimum value and approaches point contact. The presence of an optimum tip size reflects

![](./images/811812841798500354_44.jpg)

Fig. 44 Variation of measured maximum spot cooling on copper mini-contact size

the competing effects of the favorable cooling flux concentration and the parasitic spreading resistance in the mini-contact tip. As shown in Fig. 44, for the case of no power dissipation on the silicon chip, if the mini-contact is of the same size as the TEC base, the measured maximum spot cooling is about $3.3^\circ$C. However, if a $1.8 \times 1.8$ mm copper mini-contact is integrated onto the TEC, $7.1^\circ$C maximum spot cooling can be obtained, which results in 115% improvement on spot-cooling performance. Similarly, spot-cooling performance can be improved by 100 and 80% if the power dissipation of the silicon chip is 30 W and 67 W, respectively. It is interesting to note that the power dissipation on the silicon chip has an impact on the optimized mini-contact size and the larger the power dissipation on the silicon chip, the smaller the optimized mini-contact size. As clearly illustrated in Fig. 44, as the power dissipation on the silicon chip increases from 0 to 67 W, the optimum mini-contact size decreases from $1.8 \times 1.8$ mm to $1.3 \times 1.3$ mm.

## 2.5 Applications in Biomedical Systems

Temperature control is one of the most essential operations in many biomedical systems [114]. Active temperature control is capable of accurately and rapidly bringing the intended temperature above, below, or in between preset limits. In particular, in biomedicine thermal control systems are encountered frequently, for example, in electrophysiology [115], radiopharmaceutical synthesis [116], microbial studies [117], rapid thermal cycling of cells, [118] and DNA sequencing [119]. Wijngaards et al. developed a concept of an active micro-thermostat system using an integrated thin-film poly-SiGe thermoelectric cooler, capable of stabilizing the temperature of a suspended structure at ambient temperature and above. This opens up the way to a large number of applications that need to be thermally controllable in the range of $10$-$50^\circ$C, especially in the field of biomedicine.

Precise fluid temperature control in microfluidic channels is a requirement for many lab-on-a-chip and microreactor devices, especially in biotechnology where most processes are highly temperature sensitive. Microheaters integrated with microfluidic channels have been proposed but are of limited use for temperature control, as they can only be used for raising the fluid temperature. In addition, they are limited in creating large thermal gradients, in the order of 10 K/mm, due to thermal conduction in the substrate. One feasible method that scales well on the microscale is thermoelectric cooling. Maltezos demonstrated the concept of a $\text{Bi}_2\text{Te}_3$-based thermoelectric microcooler integrated into a microfluidic channel in order to give rapid and localized fluid cooling [120]. They reported an on-chip thermoelectric refrigerator and heat exchanger for microfluidic devices. The microfluidic chamber was cycled between $-3$ and over $120^\circ$C, thus spanning water freezing and boiling, and the entire PCR temperature range. For smaller chambers, it was shown that it is possible to cool reagent from room temperature to freezing within 10-20s, and to obtain relatively good temperature stability ($<\pm0.2^\circ$C) over long periods of time. The ability to localize heating and cooling in microfluidic chambers and channels enable massive parallelization of chemical reactions

in which the temperature of each reaction vessel can be independently controlled. Thus, these thermal management systems enable the fabrication of complex chip-based chemical and biochemical reaction systems in which the temperature of many processes can be controlled independently.

## 3 On-Chip Hot-Spot Cooling Using Anisotropic Heat Spreader

Anisotropic heat spreaders, with a high in-plane thermal conductivity, provide a very promising passive approach for hot-spot remediation and constitute a very attractive component for active cooling of nanoelectronic chips. This anisotropy can be used to laterally spread the hot spot heat to cooler regions of the chip and thus can significantly reduce the hot-spot temperature. Recently, Bar-Cohen et al. used analytical and numerical models to investigate the feasibility of hot-spot remediation using the lateral heat-spreading capability of a thermal interface material (TIM) with orthotropic thermal conductivity [121]. It was found that when used together with existing cooling solutions, such materials, bonded directly to the silicon chip as shown in Fig. 45, can substantially reduce the temperature rise associated with a severe flux spot and more uniformly distribute the heat at the interface between the TIM and the next element in the heat-transfer path.

![](./images/811812841798500354_45.jpg)

Fig. 45 Implementation of an anisotropic TIM/Spreader in a three-dimensional stack up

In their work, the bi-layer slab shown in Fig. 46 was used to investigate the hot-spot remediation provided by an orthotropic spreader attached directly to the back of a square chip with a single, centrally located, square flux spot. All external surfaces are assumed adiabatic, except for a heat flux boundary condition at the flux spot and a convective boundary condition on the back of the orthotropic spreader. Background heating on the active side of the chip is forgone because only the hot-spot temperature rise is sought. The boundary conditions are such that inclusion of background heating would simply elevate the entire temperature field. This effect becomes nontrivial if temperature-dependent material properties and heat-transfer coefficients are employed, but all properties and heat-transfer coefficients are taken to be constant in this analysis. The convective boundary condition represents the

![](./images/811812841798500354_46.jpg)

Fig. 46 Schematic of compound chip/spreader system

influence of the "global" cooling scheme and is modeled by a uniform heat-transfer coefficient on the back of the spreader.

Following Muzychka' work [122], an analytical solution was developed using the separation of variables method and the excess temperature on the active side of the chip ($z=0$) is given by the following equation:

$$
\begin{aligned}
\Delta T_{\text {bulk }}(x, y, z=0)= & A_{0}+\sum_{m=1}^{\infty} A_{m} \cos \left(\lambda_{m} x\right)+\sum_{n=1}^{\infty} A_{n} \cos \left(\delta_{n} y\right) \ldots \\
& +\sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{m n} \cos \left(\lambda_{m} x\right) \cos \left(\delta_{n} y\right)
\end{aligned} \tag{27}
$$

The eigenvalues in Equation (27) are given by $\lambda_{m}=\frac{m \pi}{L}, \delta_{n}=\frac{n \pi}{L}$, and $\beta_{m n}=$ $\sqrt{\lambda_{m}^{2}+\delta_{n}^{2}}$ and the Fourier coefficients, $A_{o}, A_{n}, A_{m}$, and $A_{m n}$, are found from the application of the boundary conditions in the $z$-direction. Imposing the boundary conditions at $z=0$ results in expressions for the " $A$ " coefficients as follows:

$$
A_{0}=\frac{Q}{L^{2}}\left(\frac{t_{1}}{k_{1}}+\frac{t_{2}}{k_{2}}+\frac{1}{h}\right) \tag{28}
$$

$$
A_{m}=\frac{2 Q\left[\sin \left(\frac{L+w}{2} \lambda_{m}\right)-\sin \left(\frac{L-w}{2} \lambda_{m}\right)\right]}{L^{2} w k_{1} \lambda_{m}^{2} \phi\left(\lambda_{m}\right)}
$$

$$
A_{n}=\frac{2 Q\left[\sin \left(\frac{L+w}{2} \delta_{n}\right)-\sin \left(\frac{L-w}{2} \delta_{n}\right)\right]}{L^{2} w k_{1} \delta_{n}^{2} \phi\left(\delta_{n}\right)} \tag{29}
$$

$$
A_{m n}=\frac{16 Q \cos \left(\frac{\lambda_{m} L}{2}\right) \sin \left(\frac{\lambda_{m} w}{2}\right) \cos \left(\frac{\delta_{n} L}{2}\right) \sin \left(\frac{\delta_{n} w}{2}\right)}{L^{2} w^{2} k_{1} \beta_{m n} \lambda_{m} \delta_{n} \phi\left(\beta_{m n}\right)}
$$

The parameter, $\phi$, appearing throughout Equation (29), is a spreading parameter that is a function of a dummy variable $\zeta$, with $\phi(\zeta)$ given by

$$
\varphi(\zeta)=\frac{\left(\alpha e^{4 \zeta t_{1}}-e^{2 \zeta t_{2}}\right)+\psi\left[e^{2 \zeta\left(2 t_{1}+t_{2}\right)}-\alpha e^{2 \zeta\left(t_{1}+t_{2}\right)}\right]}{\left(\alpha e^{4 \zeta t_{1}}+e^{2 \zeta t_{2}}\right)+\psi\left[e^{2 \zeta\left(2 t_{1}+t_{2}\right)}+\alpha e^{2 \zeta\left(t_{1}+t_{2}\right)}\right]}
\tag{30}
$$

and $\zeta$ is replaced by $\lambda_{m}, \delta_{n}$, or $\beta_{m n}$ in Equation (30) as appropriate. The new parameters in Equation (30) are to be evaluated as $\psi=\frac{\zeta+h / k_{2}}{\zeta-h / k_{2}}$ and $\alpha=\frac{1-k_{2} / k_{1}}{1+k_{2} / k_{1}}$ where $\zeta$ is again replaced by $\lambda_{m}, \delta_{n}$, or $\beta_{m n}$ as appropriate. The conductivity of the second layer, $k_{2}$, is assumed to be isotropic in the above expressions. However, as suggested in the literature, if either of the layers exhibits orthotropic conductivity, the solution for purely isotropic layers can be used when the following length scale and conductivity transformations are employed in the subject orthotropic layer:

$$
\begin{aligned}
&k \rightarrow k_{\mathrm{eq}}=\sqrt{k_{x y} k_{z}} \\
&t \rightarrow t_{\mathrm{eq}}=\frac{t}{\sqrt{k_{z} / k_{x y}}}
\end{aligned}
\tag{31}
$$

Thus, $k_{2}$ and $t_{2}$ in Equations (28), (29) and (30) can be replaced by the transformations in Equation (31) to account for the anisotropicity in the spreader.

Equations (27), (28), (29), (30), and (31) provide a full solution for the excess temperature on the active side of the compound structure shown in Fig. 46. The overall resistance to heat transmission for the system shown in Fig. 46 is comprised of (1) the resistance to one-dimensional heat flow and (2) the spreading resistance. The first term in Equation (27) is the Fourier coefficient, $A_{0}$, which is given by Equation (28) and is attributable to uniform one-dimensional conduction through the compound bi-layer slab. The three remaining terms are related to thermal spreading and thus vanish as the hot-spot size approaches the chip size. The total thermal resistance can be related to the average excess temperature at the hot spot through the following definition:

$$
R_{\mathrm{T}}=\frac{\overline{\Delta T_{\text {bulk }}}}{Q}
\tag{32}
$$

where $R_{\mathrm{T}}$ is the total thermal resistance, including thermal transport by both conduction and convection. The term $\overline{\Delta T_{\text {bulk }}}$ in Equation (32) is found by integrating Equation (27) over the flux-spot region and dividing by the flux-spot area, or, expressed mathematically:

$$
\overline{\Delta T_{\text {bulk }}}=\frac{1}{A_{\mathrm{s}}} \iint_{A_{\mathrm{s}}} \Delta T_{\text {bulk }}(x, y, 0) d A_{s}
\tag{33}
$$

As noted, the total thermal resistance is also the sum of the one-dimensional resistance and the spreading resistance as follows:

$$
R_{\mathrm{T}}=R_{1 \mathrm{D}}+R_{\mathrm{s}}
\tag{34}
$$

The one-dimensional resistance to heat conduction is easily found to be:

$$
R_{1 D}=\frac{t_{1}}{k_{1} L^{2}}+\frac{t_{2}}{k_{z} L^{2}}+\frac{1}{h L^{2}}
\tag{35}
$$

Meanwhile, the spreading resistance, $R_{\mathrm{s}}$, can be found by substituting Equations (32), (33), and (35) into Equation (34):

$$
R_{\mathrm{s}}=\frac{1}{A_{\mathrm{s}} Q} \iint_{A_{\mathrm{s}}} \Delta T_{\mathrm{bulk}}(x, y, 0) d A_{s}-\left(\frac{t_{1}}{k_{1} L^{2}}+\frac{t_{2}}{k_{z} L^{2}}+\frac{1}{h L^{2}}\right)
\tag{36}
$$

The integration in Equation (36) yields the following expression for the spreading resistance in a bi-layer structure with a centrally located flux spot:

$$
\begin{aligned}
R_{\mathrm{s}}= & \frac{1}{2\left(w / 2\right)^{2}\left(L / 2\right)^{2} k_{1}}\left[\sum_{m=1}^{\infty} \frac{\sin ^{2}\left(w \delta_{m} / 2\right)}{\delta_{m}^{3} \varphi\left(\delta_{m}\right)}+\sum_{n=1}^{\infty} \frac{\sin ^{2}\left(w \lambda_{n} / 2\right)}{\lambda_{n}^{3} \varphi\left(\lambda_{n}\right)}\right] \cdots \\
& +\frac{1}{\left(w / 2\right)^{4}\left(L / 2\right)^{2} k_{1}} \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(w \delta_{m} / 2\right) \sin ^{2}\left(w \lambda_{n} / 2\right)}{\delta_{m}^{2} \lambda_{n}^{2} \beta_{m n} \varphi\left(\beta_{m n}\right)}
\end{aligned}
\tag{37}
$$

where the eigenvalues are the same as those for Equation (27) and the parameter $\varphi$ is given by Equation (30).

### 3.1 Effect of In-Plane Spreader Thermal Conductivity

Successful hot-spot remediation via an orthotropic spreader depends on the ability of the spreader to conduct heat laterally from local regions of high heat flux to other parts of the chip with lower thermal loads and is most directly influenced by its in-plane thermal conductivity, $k_{x y}$. This conclusion is supported by the thickness and conductivity transformations in Equation (31), which clearly show that any increase in $k_{x y}$ for fixed values of $k_{z}$ and $t$ will result in larger values $k_{\text {eq }}$ and $t_{\text {eq }}$, through the indicated square root dependence. Therefore, an increase in the conductivity ratio, $k_{x y} / k_{z}$, leads to an attendant decrease in the overall thermal resistance, and thus a decrease in the average hot-spot temperature.

A representative chip/spreader system with the parameter settings listed in Table 6 was used to determine the magnitude of the benefits of increasing $k_{x y}$. Please note that, unless otherwise specified, the parameters in Table 6 will be used throughout this section. The thru-plane conductivity of the spreader, $k_{z}$, was chosen to be $5 \mathrm{~W} / \mathrm{m} \mathrm{K}$ because this is a nominal thru-plane conductivity for some natural graphite materials as well as pyrolytic graphite [123]. A heat-transfer coefficient of $10,000 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$ was applied to represent the presence of an aggressive cooling approach (e.g., pool boiling or a microchannel cold plate) [124]. The in-plane conductivity was varied between 5 and $1800 \mathrm{~W} / \mathrm{m} \mathrm{K}$ in order to determine the effect that the degree of anisotropy had on hot-spot remediation.

<table>
<caption>Table 6 Parameter settings for $k_{xy}$ variation</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Value</th>
<th>Units</th>
</tr>
</thead>
<tbody>
<tr>
<td>$t_1$</td>
<td>Chip thickness</td>
<td>250</td>
<td>$\mu$m</td>
</tr>
<tr>
<td>$t_2$</td>
<td>Spreader thickness</td>
<td>500</td>
<td>$\mu$m</td>
</tr>
<tr>
<td>$k_1$</td>
<td>Isotropic chip conductivity</td>
<td>163</td>
<td>W/m K</td>
</tr>
<tr>
<td>$k_z$</td>
<td>Thru-plane spreader conductivity</td>
<td>5</td>
<td>W/m K</td>
</tr>
<tr>
<td>$k_{xy}$</td>
<td>In-plane spreader conductivity</td>
<td>Varies</td>
<td>W/m K</td>
</tr>
<tr>
<td>$q''$</td>
<td>Hot-spot heat flux</td>
<td>1.4</td>
<td>kW/cm²</td>
</tr>
<tr>
<td>$h$</td>
<td>Effective heat-transfer coefficient</td>
<td>10,000</td>
<td>W/m² K</td>
</tr>
<tr>
<td>$T_{bulk}$</td>
<td>Ambient temperature for convective transfer</td>
<td>25</td>
<td>C</td>
</tr>
<tr>
<td>$L$</td>
<td>Chip size, square</td>
<td>1</td>
<td>cm</td>
</tr>
<tr>
<td>$W$</td>
<td>Hot-spot size, square</td>
<td>500</td>
<td>$\mu$m</td>
</tr>
</tbody>
</table>

The excess temperature profiles on the active side of the chip, subjected to a 1.4 kW/cm², 0.5 mm² flux spot, are shown for several different in-plane conductivities in Fig. 47. The Gaussian-like temperature profile for the isotropic spreader ($k_z = k_{xy} = 5$ W/m K) is seen to yield a hot-spot temperature that is nearly 47.5 K above ambient. Use of the orthotropic spreaders is seen to produce similar profiles but to considerably reduce the peak temperature at the center of the hot spot and over the adjacent silicon, while modestly elevating the temperature ($\sim1^\circ$C), in the edge regions of the chip. As expected, increasing the in-plane conductivity, $k_{xy}$, decreases the excess temperature. Thus, for $k_z = 5$ and $k_{xy} = 350$, which is representative of natural graphite sheets, the hot-spot temperature is $\sim9.3^\circ$C below that obtained through use of the isotropic spreader. If the in-plane conductivity is further increased to 1800 W/m K, a hot-spot suppression of $\sim14.3^\circ$C is attained.

![](./images/811812841798500354_47.jpg)

Fig. 47 Excess temperature profiles taken through the middle of the active chip surface for various $k_{xy}$

The variation of hot-spot remediation with the in-plane thermal conductivity of an orthotropic heat spreader, relative to a low-conductivity isotropic spreader, is shown in Fig. 48. The peak temperature reduction is seen to asymptotically approach 15°C as the in-plane conductivity increases towards 1800 W/m K. In order to put these results into context, the performance of several spreaders with varying conductivities are evaluated for the same geometric parameters and thermal boundary conditions, as listed in Table 6. With the isotropic spreader ($k = 5$ W/m K) as a baseline, the hot-spot cooling achieved by each alternative spreader is shown on the right side of Fig. 48. The first data point corresponds to an isotropic spreader with conductivity of 160 W/m K, representing the use of a thick silicon chip. It is found that increasing the thickness of the silicon provides approximately 18.3°C of cooling, which exceeds by 4°C the best hot-spot suppression achieved. However, it can be seen in Fig. 48 that an orthotropic spreader with $k_z = 10$ W/m K and $k_{xy} = 1700$ W/m K – which is characteristic of annealed pyrolytic graphite (APG) [125] can provide the same hot-spot suppression as the thicker silicon chip.

![](./images/811812841798500354_48.jpg)

Fig. 48 Variation of hot-spot cooling with in-plane thermal conductivity in an orthotropic heat spreader

Implementation of a copper spreader with isotropic thermal conductivity of 400 W/m K provides further hot-spot suppression, reaching a temperature reduction of $\sim$23°C. Of the alternative spreaders considered, the best hot-spot suppression of $\sim$26.6°C was provided by isotropic CVD diamond film with a thermal conductivity of 1450 W/m K in all three directions.

The above results show that increasing the in-plane thermal conductivity of an orthotropic spreader can provide substantial hotspot temperature reduction. For the parameters considered, the cooling performance of a highly orthotropic APG spreader matches the cooling provided by an equal thickness of pure silicon. This is an important result given the general reluctance of chip manufacturers to allocate valuable semiconductor-grade silicon for thermal management functions. Despite the good performance of the best highly orthotropic spreaders, an equally sized

copper spreader provides about 4°C better hot-spot remediation for the conditions examined. However, natural graphite orthotropic spreaders can be made extremely pliable and offer a weight advantage over copper spreaders of equal size since the density of natural graphite is approximately just 25% that of copper. This weight difference could be significant in weight-constrained mobile applications. Furthermore, highly orthotropic spreaders with low thru-plane conductivity have the ability to reduce hot-spot temperatures while simultaneously insulating adjacent layers of a chip stack.

Figure 49 shows the temperature rise of the silicon, copper, and APG spreaders as a function of location on the back of the spreader. The excess temperature displayed in Fig. 49 is the difference between the local temperature and the edge tempera- ture; thus, the value of $\Delta T$ vanishes for all profiles as the edge of the spreader is approached. For the parameters considered it can be seen that the silicon and copper spreaders allow a maximum temperature variation of 8°C and 4.3°C on the back of the spreader, respectively, compared to a maximum variation of 0.05°C for the APG spreader. Consequently, in hybrid cooling systems – using two-phase cooling with an anisotropic spreader attached to the chip – an APG spreader would offer only a modest temperature rise on the rear of the spreader and yield a system that is less susceptible to local dryout or critical heat flux.

![](./images/811812841798500354_49.jpg)

Fig. 49 Temperature rise on the back of silicon, copper, and APG spreaders

### 3.2 Variation of Spreader Thickness

The thickness of the orthotropic TIM/spreader will not only establish the mag- nitude of hot-spot cooling, but will also determine the viability of this thermal solution for volume-constrained three-dimensional stacks of hot-spot-laden chips. It is, therefore, important to explore the tradeoffs between spreader thickness and

cooling performance when assessing the merits of an anisotropic spreader. The impact of spreader thickness on hot-spot remediation is best understood in terms of the overall thermal resistance of the system, $R_{\mathrm{T}}$, which is the sum of the spreading resistance, $R_{\mathrm{s}}$, and the resistance to one-dimensional conduction and convection, $R_{1 \mathrm{D}}$. MATLAB codes were developed to aid in the evaluation of $R_{1 \mathrm{D}}$ (Equation (35)) and $R_{\mathrm{s}}$ (Equation (37)) for various spreader thicknesses.

Using the model in Fig. 46 and the parameter settings in Table 6, the thickness of each of the spreaders represented in Fig. 48 was varied to determine the effect on $R_{1 \mathrm{D}}$, $R_{\mathrm{s}}$, and hence $R_{\mathrm{T}}$. Typical trends seen during this analysis are depicted in Fig. 50 where it is clear that the total thermal resistance generally experiences a minimum for some critical value of the spreader thickness. Near a spreader thickness of zero, the total thermal resistance of the system approaches that of a single layer of silicon. But, as the thickness increases, the one-dimensional resistance, $R_{1 \mathrm{D}}$, grows and the spreading resistance, $R_{\mathrm{s}}$, falls leading to a nonmonotonic variation in the overall thermal resistance. When the negative slope of $R_{\mathrm{s}}$ equals the positive slope of $R_{1 \mathrm{D}}$ the minimum thermal resistance, and hence minimum average hot-spot temperature, is attained. For any increase in spreader thicknesses beyond this optimum, the linear rise in $R_{1 \mathrm{D}}$ is greater than the decrease in $R_{\mathrm{s}}$ and the total thermal resistance increases.

Sensitivity of total thermal resistance to spreader thickness
![](./images/811812841798500354_50.jpg)

Fig. 50 Variation of $R_{\mathrm{T}}$ and average hot-spot excess temperature for increasing spreader thickness ($k_{z}=5$ W/m K)

The resulting variation in overall thermal resistance for a spreader with a thru-thickness conductivity of 5 W/m K is shown in Fig. 50 for a range of in-plane

conductivities. As anticipated, the total thermal resistance for each of the $k_{xy}$ curves approaches the resistance of a directly cooled chip, i.e., $R_{\mathrm{T}} \to 10.84$ K/W, as spreader thickness approaches zero. For increasing values of the in-plane conductivity (above 5 W/m K), the total thermal resistance and average hot-spot excess temperature generally decrease and display an optimum value. The specific optimum thickness varies with in-plane conductivity as shown in Fig. 51, exhibiting a peak optimum thickness of approximately $160\ \mu\mathrm{m}$ in the vicinity of $k_{xy}=200$ W/m K and of approximately $100\ \mu\mathrm{m}$ at a thermal conductivity of 1800 W/m K. However, as seen for the dashed lines where $k_{xy}=5$ and 25 W/m K, for low values of the in-plane conductivity, there is no optimum thickness and $R_{\mathrm{T}}$ continuously increases. For the parameters considered, it was found that the development of a monotonically increasing total thermal resistance occurs for $k_{xy} \leq 14.5$ W/m K.

![](./images/811812841798500354_51.jpg)

Fig. 51 Optimum spreader thickness varies with in-plane thermal conductivity

The variation of $R_{\mathrm{T}}$ with the TIM/spreader thickness, $t_{2}$, for each of these alter- natives can be seen in Fig. 52. It is found that the highly orthotropic APG exhibits similar behavior to that shown in Fig. 50, with a distinct minimum occurring at a spreader thickness of $157\ \mu\mathrm{m}$, for the stated conditions. However, the silicon, copper, and diamond spreaders all exhibit a broad "plateau" for which the thermal resistance remains relatively constant with thickness (these spreaders do indeed have minimum values of $R_{\mathrm{T}}$, but the minima occur beyond the 2 mm thickness at which plotting was stopped in Fig. 52).

Figures 51 and 52 reveal that highly orthotropic graphite TIMs/spreaders yield optimum hot-spot cooling performance at relatively low thicknesses - under $165\ \mu\mathrm{m}$ - for the conditions examined. Furthermore, it is interesting to note in Fig. 52 that the orthotropic APG spreader yields lower average hot-spot temperatures

# Sensitivity of total thermal resistance to spreader thickness

![](./images/811812841798500354_52.jpg)

Fig. 52 Variation of $R_\text{T}$ for increasing spreader thickness for alternative spreaders

than copper for thicknesses up to $\sim$200 $\mu$m and lower temperatures than silicon up to $\sim$500 $\mu$m. Also, the minimum average hotspot excess temperature for APG is 24.4 K at 157 $\mu$m, which is only 5.0°C and 1.3°C hotter than that provided by nine times the thickness of copper and silicon ($\sim$1.4 mm), respectively. The exceptional performance of highly orthotropic TIMs/spreaders at low thickness may lead them to be favored over conventional heat-spreading materials in space constrained 3D chip stacks.

Up to this point, the thickness of the silicon chip in Fig. 46 has been fixed at 250 $\mu$m for all cases. The variation of $R_\text{T}$ with spreader thickness for a spreader with $k_z = 5$ W/m K and $k_{xy} = 350$ W/m K, where each of the plotted line represents a different chip thickness (all other parameters remain unchanged, see Table 6) is shown in Figure 53. The total thermal resistance is seen to decrease with increasing chip thickness. However, it is clear that the additional hot-spot cooling provided by an optimally thick spreader becomes less dramatic for greater chip thicknesses. This is more clearly shown in Fig. 54 where the $R_\text{T}$ data for each plotted line in Fig. 53 has been normalized by the total thermal resistance that would exist if the spreader were removed and the bare chip were cooled directly (this resistance is called $R_\text{T,bare}$).

It is seen that an optimally thick spreader reduces $R_\text{T,bare}$ by $\sim$43% when the chip is 75 $\mu$m thick but reduces $R_\text{T,bare}$ by only $\sim$7% when the chip is 400 $\mu$m thick. The reduction in spreader effectiveness for increasing chip size is the result of more

![](./images/811812841798500354_53.jpg)

Fig. 53 Effect of chip thickness of spreader thickness variation for an orthotropic spreader with
$k_z = 5$ W/m K and $k_{xy} = 350$ W/m K

![](./images/811812841798500354_54.jpg)

Fig. 54 Normalized total resistance for different chip thicknesses and an orthotropic spreader with
$k_z = 5$ W/m K and $k_{xy} = 350$ W/m K

effective heat spreading in the thicker silicon, which reduces the role played by the orthotropic spreaders. Alternatively, as chip thicknesses shrink – the more likely sce- nario as chip manufacturers strive to more efficiently utilize valuable silicon ingots and package electronics in thinner packages – the orthotropic TIM/spreaders can compensate for the loss of inherent spreading in these thinner silicon chips of the future.

Figure 54 also reveals that increasing chip thicknesses are accompanied by a steady decrease in the optimum spreader thickness for a given $k_{xy}$. In order to better understand this variation, the plot in Fig. 51 was reproduced for different values of chip thickness, $t_1$. The results can be seen in Fig. 55 and it is clear that smaller chip thicknesses yield a larger optimum spreader thickness for a given $k_{xy}$. Also, thicker chips yield lower sensitivity of optimum thickness to in-plane conductivity, as evidenced by the suppression of the peak optimum thickness in Fig. 55 for larger values of $t_1$.

Optimum Spreader Thickness for Various $k_{xy}$ with $k_z$ = 5 W/m-K
![](./images/811812841798500354_55.jpg)

Fig. 55 Change in optimum spreader thickness for various $k_{xy}$ and $t_1$

### 3.3 Numerical Simulations and Contact Resistance Variation

The parametric results above indicate that use of an orthotropic spreader is a promising approach to reducing hot-spot temperatures. However, it may be antic- ipated that the physical attachment of the orthotropic material to the back of the chip, as depicted in Fig. 46, may well result in the creation of a poten- tially significant and deleterious thermal contact resistance. Typical contact resis- tances for electronic packaging applications are reported to be in the range of

$10^{-7}$-$10^{-4}$ K m²/W. The thermal contact resistances of $\sim 10^{-7}$ K m²/W are representative of an excellent interface achieved by monolithic growth or eutectic interface attachment, while resistances of $\sim 10^{-4}$ K m²/W represent a relatively poor thermal interface achieved through the use of phase change materials and elastomeric pads [126]. While it is, thus, desirable to assess the impact of thermal contact resistance at the chip/spreader interface on hot-spot remediation, to the authors' knowledge, there is no analytical solution that explicitly accounts for this effect in a layered structure. Consequently, the parametric sensitivity of hot-spot temperature to contact resistance is explored through numerical simulations with ANSYS for contact resistances varying from 0 to $10^{-4}$ K m²/W.

Figure 56 shows the resulting heat flux vectors near the flux spot in the silicon chip for each contact resistance, with the results for perfect thermal contact on the top and poor thermal contact on the bottom, for the previously described conditions. Comparing the two heat flux plots reveals the subtle influence of contact resistance on the flow of heat in the system. In the case of perfect thermal contact, the heat flux vectors display a large thru-plane component, reflecting the relative ease with which heat can flow across the interface and into the spreader. Alternatively, the heat flux vectors for poor thermal contact exhibit a larger in-plane component, reflecting the additional resistance to heat flow across the interface. The contact resistance thus acts to more evenly distribute the heat flux imposed on the spreader, thereby reducing the spreader's effectiveness. Ultimately, the presence of the contact resistance results in larger peak and average temperature rises at the flux spot (these peak and average are 61.9 and 57.7°C for the perfect interface, respectively, with the poor thermal interface resulting in 96.2 and 91.6°C peak and average temperatures, respectively).

![](./images/811812841798500354_56.jpg)

Fig. 56 Heat flux plots in the silicon chip for perfect and poor thermal contact

With the expectation that hot-spot temperatures should increase for escalating contact resistance, a total of 78 ANSYS simulations were run for contact resistances ranging from 0 to $10^{-4}$ K m²/W, with model parameters defined in Table 6. Figure 57 depicts the increase in hot-spot temperature over the stated contact resistance range for differing degrees of spreader anisotropy. The reader is reminded that $10^{-7}$ K m²/W is a very low contact resistance that may be achieved by monolithic growth on the back of the chip or through the use of a soldered interface. Alternatively, a poor interface, such as a lightly loaded interface with a phase change material or elastomeric pad, is represented by a contact resistance near $10^{-4}$ K m²/W.

![](./images/811812841798500354_57.jpg)

Fig. 57 Hot spot vs. contact resistance for various $k_{xy}$

For the conditions studied, it is found that the contact resistance has a significant effect on hot-spot temperature, particularly when extreme anisotropy is present in the spreader. In order for a spreader with $k_z = 5$ W/m K and $k_{xy} = 1800$ W/m K to provide at least 10°C better hot-spot cooling than the isotropic spreader, the contact resistance must be maintained below $0.1 \times 10^{-4}$ K m²/W. However, even for a contact resistance of $0.5 \times 10^{-4}$ K m²/W, a nearly 5°C temperature reduction can be achieved by the best orthotropic material and 3 or 4°C for more commonly available graphite TIM/spreaders.

### 3.4 Experimental Demonstration

Graphite has an anisotropic crystal structure that results in different properties in different directions. Its in-plane thermal conductivity can range from 140 to 1650 W/m K, while its thru-thickness thermal conductivity is much lower and ranges

between 2 and 10 W/m K. Based on the analytical and numerical results described in the previous section, it would appear that such anisotropy can be used advan- tageously to both reduce the severity of a hot spot and to spread the heat in the TIM, thus shielding a surface adjacent to the heat source from a high heat flux. Recently, Xiong et al. experimentally demonstrated that a thin graphite heat spreader can reduce the hot spot significantly [127]. In his experiment, two graphite heat spreaders with different in-plane thermal conductivities and thicknesses were tested and compared. The first graphite material had an in-plane thermal conductivity of 425 W/m K, a thru-thickness thermal conductivity of 3.2 W/m K and a thickness of 110 $\mu$m. The second material was an experimental grade of graphite with an in-plane thermal conductivity estimated to be greater than 1000 W/m K, a thru- thickness thermal conductivity estimated between 5 and 6 W/m K, and a thickness of 30 $\mu$m. A 50 × 70 × 1 mm acrylonitrile butadiene styrene (ABS) plate was used as the substrate. A thin graphite heat spreader was adhesively bonded to the ABS sub- strate and a constant heat flux was applied over a limited area on one side, while the other side of the ABS substrate was exposed to the ambient for natural convection cooling. Three cases were investigated in their work:

Case 1: without a heat spreader and with a power of 0.75 W on the hot spot.

Case 2: with a 425 W/m K, 110 $\mu$m-thick graphite heat spreader and with a power of 3.0 W on the hot spot.

Case 3: with a 1000 W/m K, 30 $\mu$m-thick graphite heat spreader and with a power of 3.0 W on the hot spot.

Figure 58 shows the IR thermal image of the ABS substrate without an attached heat spreader, at a power dissipation of only 0.75 W on the hot spot. Because of the low thermal conductivity of the ABS ($\sim$0.25 W/m K), the heat from the hot spot did not spread well and thus there is a localized hot spot immediately above the heat source and the temperature drops dramatically a short distance away from

![](./images/811812841798500354_58.jpg)

Fig. 58 Surface temperature distribution on the ABS substrate without heat spreader (0.75 W was applied on the hot spot)

the heat source. The hot-spot temperature is $90^\circ$C and most of the spreader is at a temperature less than $30^\circ$C.

Figure 59 is a thermal image of the ABS with an attached 425 W/m K, 110 $\mu$m-thick graphite heat spreader, while Fig. 66 is a thermal image of the ABS plate with a 1000 W/m K, 30 $\mu$m-thick graphite heat spreader. Note that in both cases, the excellent spreading effect of graphite spreader allowed the hot spot power to be increased to 3.0 W. These results demonstrate the significant heat-spreading effect of graphite heat spreaders. As shown in Figs. 59 and 60, with much higher power applied on the hot spot, the hot-spot temperatures are only 64 and $69^\circ$C respectively, much lower than that of the ABS without the spreader as shown in Fig. 58. The

![](./images/811812841798500354_59.jpg)

Fig. 59 Surface temperature distribution on an ABS substrate with an attached 425 W/m K graphite heat spreader (3.0 W was applied on the hot spot)

![](./images/811812841798500354_60.jpg)

Fig. 60 Surface temperature distribution on an ABS substrate with an attached 1000 W/m K graphite heat spreader (3.0 W was applied on the hot spot)

temperature gradients across the surfaces are also much lower with the entire ABS plate now above $47^\circ$C. These results demonstrate that a very thin spreader made of graphite, with an in-plane thermal conductivity on the order of 500–1000 W/m K, or other highly orthotropic materials, is a practical thermal solutions for hot-spot remediation in both a passive cooling mode and an active cooling mode.

## 4 On-Chip Hot-Spot Cooling Using Micro-Gap Cooler

As is made abundantly clear in the previous sections of this chapter, the thermal interface resistance between the "cooling solution" and the chip poses a consid- erable barrier to effective remediation of on-chip hot spots. Direct liquid cooling techniques, which allow for direct contact between an inert dielectric liquid and the surface of the chip and eliminate the TIM (thermal interface material), hold great promise for hot-spot-driven thermal management of ICs. Moreover, use of phase-change processes, including pool boiling, gas-assisted evaporative cooling, jet impingement, and spray cooling, exploit the latent heat of these liquids to reduce the required mass flow rates and can provide the added advantage of inherently high heat-transfer coefficients.

However, direct cooling of microelectronic components imposes stringent chem- ical, electrical, and thermal requirements on the liquids to be used in this thermal control mode. Direct liquid cooling of microelectronic components requires com- patibility between the liquid coolant and a system-specific combination of the chip, chip package, substrate, and printed circuit board materials, e.g., silicon, silicon dioxide, silicon nitride, alumina, o-rings, plastic encapsulants, solder, gold, and epoxy glass. In addition, a liquid coolant must possess the dielectric strength needed to provide electrical isolation between adjacent power/ground conductors and sig- nal lines. Fortunately, 3 M's family of perfluorinated liquids possess the required attributes and has been used extensively in the electronic industry [128, 129].

Recently, Bar-Cohen et al. proposed the use of micro-gap coolers to achieve a volume-efficient application of direct liquid cooling, while providing high heat- transfer coefficients – in the range needed to control the temperature of on-chip hot spots – on the back of the chip [130]. As shown in Fig. 61, in a micro-gap

![](./images/811812841798500354_61.jpg)

Fig. 61 Schematic diagram of micro-gap cooler

cooler a narrow sub-millimeter channel is created above the chip or substrate and liquid is pumped through the channel, thus removing the heat dissipated from the chip. Compared with a more conventional microchannel cooler, which needs to be attached with a TIM to the chip/substrate, micro-gap coolers require no attachment and no micromachining and could be a very attractive cooling approach for on-chip hot-spot remediation. Subsequent subsections deal with the empirical validation of this novel thermal management approach.

### 4.1 Single-Phase Experiments

Following single-phase heat-transfer experiments, with water and FC-72 as the working fluid, and successful comparison to the predicted heat-transfer coeffi- cients obtained with established correlations and CFD simulation using IcePak [131], the researchers turned their attention to two-phase thermal transport in the microgap channel. The test results for the $210\ \mu$m gap two-phase heat-transfer experiment are shown in Fig. 62. In these experiments, the mass flux was var- ied from 130 to $660\ \text{kg/m}^2\text{s}$ in steps of $130\ \text{kg/m}^2\text{s}$ and the corresponding inlet fluid velocity was 0.0794, 0.159, 0.238, 0.317, 0.397 m/s. The average heat- transfer coefficient was found to generally display a parabolic variation with the heat flux, increasing toward a peak value as the channel condition changed from subcooled to saturated flow boiling and then decreasing with further increases of heat flux.

![](./images/811812841798500354_62.jpg)

Fig. 62 Average heat-transfer coefficient vs. heat flux of $210\ \mu$m-gap cooler

The 110 $\mu$m gap channel shows some similarities to the heat-transfer coefficient variation observed in the 210 $\mu$m gap but – as shown in Fig. 63 – it appears to possess only the down-sloping branch of the previously observed parabolic trend. The peak heat-transfer coefficients attained in the 110 $\mu$m gap channel are higher than the 210 $\mu$m gap or the 500 $\mu$m gap channels, and the downward trend with heat flux moderates substantially as the mass flux increases.

![](./images/811812841798500354_63.jpg)

Fig. 63 Average heat-transfer coefficient vs. heat flux for 110$\mu$m-gap cooler

The above and other reported results show that the area-averaged heat-transfer coefficients for FC-72, of between 7.5 and 15.5 kW/m$^2$ K, can be attained in micro-gap channels of 110–500 $\mu$m. These values are significantly higher than the single phase FC-72 values, showing that two-phase micro-gap cooler can provide the high cooling capability needed for hot spot remediation.

### 4.2 Application to Hot Spot Remediation

To assess the efficacy of micro-gap cooler for thermal management of hot spots, it is instructive to simulate the thermal performance of a notional advanced semiconductor chip cooled by the micro-gap coolers. A $10 \times 10$ mm silicon chip, 500 $\mu$m thick, dissipating a uniform heat flux of 100 W/cm$^2$ across nearly all the active chip area serves as the test vehicle for this simulation. In keeping with the theme of this Chapter, the chip is assumed to possess a central, circular hot spot, varying from 100 to 400 $\mu$m in diameter and dissipating between 1 and 2 kW/cm$^2$. It

is further assumed that the thermal conductivity of the silicon chip is invariant at 125 W/m K, that it is cooled from the back surface (opposite to that of the active circuitry) with heat-transfer coefficients that can vary from 5 to 20 kW/m² K, reflective of the values that can be potentially achieved with micro-gap coolers and that the liquid temperature is 22°C.

Figure 64 presents the three-dimensional temperature profile while Fig. 65 depicts the temperature along a diagonal, on the active face of the silicon chip for a baseline microgap-cooled chip configuration with a 400 µm hot spot, generating a 2 kW/cm² heat flux. As observed in Figs. 64 and 65, when this notional

![](./images/811812841798500354_64.jpg)

Fig. 64 Three-dimensional temperature profile for direct liquid cooling of advanced semiconductor chip [$10 \times 10 \times 0.5$ mm, $q'' = 100$ W/cm², $q''_{\text{hs}} = 2$ kW/cm², $d_{\text{hs}} = 400$ µm, $h = 10$ kW/m² K]

![](./images/811812841798500354_65.jpg)

Fig. 65 Temperature distribution across the diagonal of the chip [$q_{\text{chip}} = 100$ W/cm², $q_{\text{spot}} = 2000$ W/cm², $h = 10000$ W/m² K, $T_{\text{c}} = 22^\circ$C]

baseline chip, with a very severe hot spot, is cooled by a micro-gap cooler with an $h$ equal to $10\ \text{kW/m}^2\text{K}$, it experiences an elevated average temperature of approximately $130^\circ\text{C}$ and a significant hot spot with a maximum temperature of $163^\circ\text{C}$, or some $33^\circ\text{C}$ above the average chip temperature. The average and peak temperatures for various other combinations of the specified parameters are shown in Tables 7 and 8.

Tables 7 and 8 present the results for a hot-spot diameter of $100\ \mu\text{m}$ and $400\ \mu\text{m}$, respectively, with various hot-spot heat fluxes and a range of heat-transfer coefficients associated with the micro-gap coolers. In these tables, the first and second columns present the hot-spot flux and convective coefficients, respectively, while the next three columns provide: the average temperature on the active side of the chip, the average temperature on the cooled (back) side of the chip, and the average hot-spot temperatures. The last column in Tables 7 and 8 presents the maximum temperature on the active side of the silicon chip. Not surprisingly, the average chip temperature (on both the active and wetted surfaces) is seen to vary directly with the heat-transfer coefficient, while the on-chip hot-spot temperature rise is conduction limited and – for the fixed chip geometry and thermal conductivity – is driven by the heat flux and size of the hot spot. Thus, as seen in Table 8, while raising the heat-transfer coefficient to $20\ \text{kW/m}^2\ \text{K}$ lowers the average chip temperature to $77^\circ\text{C}$ for a chip heat flux of $100\ \text{W/cm}^2$, the on-chip temperature rise for a $1\ \text{kW/cm}^2$, $400\ \mu\text{m}$ hot spot, remains at approximately $15^\circ\text{C}$ across the range of heat-transfer coefficients from $5\ \text{kW}$ to $20\ \text{kW/cm}^2\text{K}$. However, since the peak chip temperature

Table 7 Temperatures for $100\ \mu\text{m}$ hot-spot diameter for various heat flux and cooling conditions

<table>
  <thead>
    <tr>
      <th>$q''_{\text{spot}}$ [W/cm²]</th>
      <th>$h$ [W/m²K]</th>
      <th>$T_{\text{chip}}$ [°C]</th>
      <th>$T_{\text{conv}}$ [°C]</th>
      <th>$T_{\text{spot}}$ [°C]</th>
      <th>$T_{\text{spot\_max}}$ [°C]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1000</td>
      <td>20,000</td>
      <td>76.2</td>
      <td>74.2</td>
      <td>78.9</td>
      <td>79.7</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>10,000</td>
      <td>126.2</td>
      <td>124.2</td>
      <td>129.0</td>
      <td>129.7</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>5000</td>
      <td>226.3</td>
      <td>224.3</td>
      <td>229.1</td>
      <td>229.8</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>20,000</td>
      <td>76.4</td>
      <td>74.4</td>
      <td>82.2</td>
      <td>83.8</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>10,000</td>
      <td>126.5</td>
      <td>124.6</td>
      <td>132.3</td>
      <td>134.0</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>5000</td>
      <td>226.7</td>
      <td>224.7</td>
      <td>232.5</td>
      <td>234.1</td>
    </tr>
  </tbody>
</table>

Table 8 Temperatures for $400\ \mu\text{m}$ hot-spot diameter for various heat flux and cooling conditions

<table>
  <thead>
    <tr>
      <th>$q''_{\text{spot}}$ [W/cm²]</th>
      <th>$h$ [W/m²K]</th>
      <th>$T_{\text{chip}}$ [°C]</th>
      <th>$T_{\text{conv}}$ [°C]</th>
      <th>$T_{\text{spot}}$ [°C]</th>
      <th>$T_{\text{spot\_max}}$ [°C]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1000</td>
      <td>20,000</td>
      <td>7.75</td>
      <td>75.6</td>
      <td>89.1</td>
      <td>92.2</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>10,000</td>
      <td>128.2</td>
      <td>126.4</td>
      <td>140.2</td>
      <td>143.3</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>5000</td>
      <td>229.4</td>
      <td>227.6</td>
      <td>241.6</td>
      <td>244.7</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>20,000</td>
      <td>79.2</td>
      <td>77.5</td>
      <td>103.7</td>
      <td>110.3</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>10,000</td>
      <td>130.7</td>
      <td>129.0</td>
      <td>155.9</td>
      <td>162.5</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>5000</td>
      <td>233.2</td>
      <td>231.6</td>
      <td>259.0</td>
      <td>265.6</td>
    </tr>
  </tbody>
</table>

is established by the superposition of these two effects, any reduction in the average chip temperature has a salutary effect on the peak chip temperature, as well.

Thus, as also revealed in Fig. 66, micro-gap coolers, along with effective thermal spreading in the chip, appears to offer the potential for successfully limiting the chip and hot-spot temperature rise to acceptable levels for a wide range of operating conditions. Most significantly, a heat-transfer coefficient of $20\ \text{kW/m}^2\text{K}$, which is thought to be attainable in a microgap cooler [132] could be used to effectively cool a most challenging $2\ \text{kW/cm}^2$, $400\ \mu\text{m}$ hot spot, along with maintaining an acceptable average temperature, for a $100\ \text{W/cm}^2$ chip.

![](./images/811812841798500354_66.jpg)

Fig. 66 Effect of convective coefficient on the hot-spot temperature for $q''_{\text{hs}} = 1000\ \text{W/cm}^2$

Interestingly, the on-chip temperature rise – of the hot-spot center relative to the chip average – can be seen to vary almost directly with the product of the heat flux and diameter, yielding a ninefold increase from $3.6^\circ\text{C}$ for a $100\ \mu\text{m}$, $1\ \text{kW/cm}^2$ hot spot to $32.4^\circ\text{C}$ for a $400\ \mu\text{m}$, $2\ \text{kW/cm}^2$ hot spot. Due to the superposition of the convective and conductive effects, it may also be noted that while a large change ($\sim$50%) in the maximum excess temperature results from increasing the micro-gap heat-transfer coefficient from $5$ to $10\ \text{kW/m}^2\text{K}$, further increases to $20\ \text{kW/m}^2\text{K}$ only reduces the maximum temperature rise by approximately 30%.

## 5 Conclusions

The preceding chapter addresses on-chip, hot-spot cooling, which has become one of the most active and challenging domains in the thermal management of nano- electronic devices and packages. Following a brief discussion of several passive

and active high heat flux thermal management techniques, attention was turned to the physical phenomena underpinning the most promising on-chip thermal man- agement approaches, including thin-film and miniaturized thermoelectric coolers, orthotropic TIMs/heat spreaders, and phase-change microgap coolers, and their use for remediation of these hot spots. It was shown that, with proper thermal opti- mization, mini-contact enhanced miniaturized "bulk" thermoelectric coolers can yield hot-spot temperature reductions in excess of $15^{\circ} C$ for near millimeter-sized hot spots with $kW / cm^{2}$ -level heat fluxes, but to be vulnerable to the deleterious effects of thermal contact resistance. Micro-scaled thin-film silicon thermoelectric coolers, monolithically grown, or fashioned, on the back of silicon chips, were similarly found to provide effective thermal management of high heat flux spots, and to be capable of neutralizing the local temperature rise for a large variety of sub-millimeter hot spots. Orthotropic TIM/spreaders with high in-plane thermal conductivities were also shown to offer significant temperature reduction capability even for large, high-flux spots, when used in conjunction with a more conventional, very high heat-transfer coefficient thermal management approaches. Initial research results for microgap coolers, relying on the boiling and evaporation of a dielectric liquid flowing in a miniature gap at the back of the chip, strongly suggest that this cooling technique could provide both the local and global heat-transfer coefficients needed to meet many of the most demanding nanoelectronic cooling challenges, including severe on-chip hot spots.

## References

1. ITRS, The International Technology Roadmap for Semiconductors, 2004, Semiconductor Industry Association, http://www.ITRSnemi.org.
2. Shelling P., Li S., and Goodson K. E. Managing heat for electronics, Materials Today, 2005;8:30-35.
3. Mahajan R., Chiu C., and Chrysler G. Cooling a microprocessor chip, Proceedings of IEEE,2006; 94: 1476-1486.
4. Pedram M., and Nazarian S. Thermal modeling, analysis, and management in VLSI circuits: principles and methods, Proceedings of the IEEE, 2006; 9: 1487-1501.
5. Bar-Cohen A., Arik M., and Ohadi M. Direct liquid cooling of high flux micro and nano electronic components, Proceedings of the IEEE, 2006; 94: 1549-1570.
6. Mudawar I. Assessment of high-heat-flux thermal management schemes, IEEE Transactionson Components and Packaging Technologies, Part A: Packaging Technologies, 2001; 24:122-141.
7. Garimella S. V. Advances in mesoscale thermal management technologies for microelec- tronics, Microelectronics Journal, 2006; 37: 1165-1185.
8. Sinha S., and Goodson K. E. Thermal conduction in sub-100 nm transistors, Microelectronics Journal, 2006; 37: 1148-1157.
9. NEMI, Electronics Manufacturing Initiative Technology Roadmap, 2006, http://www. nemi.org.
10. Jannadham K., Watkins T. R., and Dinwiddie R. B. Novel heat spreader coatings for high power electronic devices, Journal Materials Sciences, 2002; 37: 1363-1376.
11. Dahlgren S. High-pressure polycrystalline diamond as a cost effective heat spreader, Proceedings of Thermal and Thermomechanical Phenomena in Electronic Systems,(ITHERM 2000), 2000; 1:23-26.

12. Goodson K. E., and Ju Y. S. Heat conduction in novel electronic films, Annual Review of Materials Science, 1999; 29: 261–293.

13. Le Berre M., Pandraud G., Morfouli P., and Lallemand M. The performance of micro heat pipes measured by integrated sensors, Journal of Micromechanics and Microengineering, 2006; 16: 1047–1050.

14. Peterson G. P., Duncan A. B., and Weichold M. H. Experimental investigation of micro heat pipes fabricated in silicon wafers, Journal of Heat Transfer, 1993; 115: 750–756.

15. Peterson G. P., Duncan A. B., and Weichold M. H. Experimental investigation of micro heat pipes fabricated in silicon wafers, ASME Journal of Heat Transfer, 1993; 115: 751–756.

16. Mallik A. K., Peterson G. P., and Weichold M. H. Fabrication of vapor deposited micro heat pipes arrays as an integral part of semiconductor devices, IEEE Journal of Microelectromechanical System, 1995; 4: 119–131.

17. Karimi G., and Culham J. R. Review and assessment of pulsating heat pipe mechanism for high heat flux electronic cooling, Proceedings of ITHERM, 2004; 2: 52–59.

18. Benson D. A., Adkins D. R., Peterson G. P., Mitchell R. T., Tuck M. R., and Palmer D. W., Turning silicon substrates into diamond: micro machining heat pipes, in Proc. Adv. Design Mater. Process, Apr. 1996, pp. 19–21.

19. Suman B. Modeling, experiment, and fabrication of micro-grooved heat pipes: an update, Applied Mechanics Reviews, 2007; 60: 107–119.

20. Akachi H., Structure of a heat pipe, U.S. Patent #4,921,041, 1990.

21. Zuo Z. J., North M. T., and Wert K. L. High heat flux heat pipe mechanism for cooling of electronics, IEEE Transactions on Components and Packaging Technologies, 2001; 24: 220–225.

22. Lin C., Ponnappan R., and Leland J. High performance miniature heat pipe, International Journal of Heat and Mass Transfer, 2002; 45: 3131–3142.

23. Lee M., Wong M., and Zohar Y. Integrated micro-heat-pipe fabrication technology, Journal of Microelectromechanical Systems, 2003; 12: 138–146.

24. Lee M., Wong M., and Zohar Y. Characterization of an integrated micro heat pipe, Journal of Micromechanics and Microengineering, 2003; 13: 58–64.

25. Khrustalev D., and Faghri A. Thermal characteristics of conventional and flat miniature axially-grooved heat pipes, Journal of Heat Transfer, 1995; 117: 740–747.

26. Ma H. B., Lofgreen K. P., and Peterson G. P. An experimental investigation of a high flux heat pipe heat sink, Journal of Electronic Packaging, 2006; 128: 18–22.

27. Gillot G., Avenas Y., Cezac N., Poupon G., Schaeffer C., and Fournier E. Silicon heat pipes used as thermal spreaders, IEEE Transactions on Components and Packaging Technologies, 2003; 26: 332–339.

28. Lin C., Ponnappan R., and Leland J. High performance miniature heat pipe, International Journal of Heat and Mass Transfer, 2002; 45: 3131–3142.

29. Tuckerman D. B., and Pease R. F. W. High-performance heat sinking for VLSI, IEEE Electron Device Letters, 1981; EDL-2: 143–150.

30. Prasher R., Chang J., Sauciuc I., Narasimhan S., Chau D., Chrysler G., Myers A., Prstic A., and Hu C. Nano and micro technology-based next-generation package level cooling solutions, Intel Journal of Technology, 2005; 9: 285–296.

31. Bowers M., and Mudawar I. High-flux boiling in low-flow rate, low-pressure drop mini-channel and microchannel heat sinks, International Journal of Heat and Mass Transfer, 1994; 37: 321–332.

32. Mudawar I., and Maddox D. E. Enhancement of critical heat flux from high power micro-electronic heat sources in a flow channel, Journal of Electronic Packaging, 1990; 112: 241–248.

33. Bar-Cohen A., Arik M., and Ohadi M. Direct liquid cooling of high flux micro and nano electronic components, Proceedings of the IEEE, 2006; 94: 1549–1570.

34. Garimella S. V., Singhal V., and Liu D. On-chip thermal management with microchannel heat sinks and integrated micropumps, Proceedings of the IEEE, 2006; 94: 1534–1548.

35. Prasher R. Thermal interface materials: historical perspective, status and future directions, Proceedings of the IEEE, 2006; 94: 1571-1586.

36. Zhang L., Wang E. N., Koo J. M., Goodson K. E., Santiago J. G., and Kenny T. W. Microscale liquid jet impingement, Proceedings of AMSE IMECE, 2001; Vol.2: Paper No. MEME-23820.

37. Wolf D. H., Incropera F. P., and Viskanta R. Local jet impingement boiling heat transfer, International Journal of Heat and Mass Transfer, 1996; 39: 1395-1406.

38. Kiper A. M. Impinging water jet cooling of VLSI circuits, International Communications in Heat and Mass Transfer, 1984; 11: 126-129.

39. Harman T. C., Taylor P. J., Walsh M. P., and LaForge B. E. Quantum dot superlattice thermoelectric materials and devices, Science, 2002; 297: 2229-2232.

40. Venkatasubramanian R., Siivola E., Colpitts T., and O'Quinn B. Thin-film thermoelec- tric devices with high room-temperature figures of merit, Nature (London), 2001; 413: 597-602.

41. Fan X., Zeng G., LaBounty C., Bowers J., Croke E., Ahn C., Huxtable S., and Majumdar A. SiGeC/Si superlattice micro-coolers, Applied Physics Letters, 2001; 78: 1580-1600.

42. Chen C., Yang B., and Liu W. L. Engineering nanostructures for energy conversion, Heat Transfer and Fluid Flow in Microscale and Nanoscale Structures, Faghri, M. and Sunden, B., Eds., Southampton, UK: WIT Press, 2004.

43. Yang B., Liu W. L., Wang K. L., and Chen G. Simultaneous measurements of Seebeck coefficient and thermal conductivity across superlattice, Applied Physics Letters, 2002; 80: 1758-1760.

44. Shakouri A., and Zhang Y. On-chip solid-state cooling for integrated circuits using thin-film microrefrigerators, IEEE Transactions on Components and Packaging Technologies, 2005; 28: 65-69.

45. Zhang Y., Zeng G. H., Piprek J., Bar-Cohen A., and Shakouri A. Superlattice microrefrig- erators fusion bonded with optoelectronic devices, IEEE Transactions on Components and Packaging Technologies, 2005; 28: 658-666.

46. Simons R. E., Ellsworth M. J., and Chu R. C. An assessment of module cooling enhancement with thermoelectric coolers, Journal of Heat Transfer, 2005; 127: 76-84.

47. Yeh L., and Chu C. Thermal Management of Microelectronic Equipment, New York: ASME Press, 2002.

48. Kraus A. D., and Bar-Cohen A. Thermal Analysis and Control of Electronic Equipment, New York, USA: Hemisphere Publishing Corporation, 1983.

49. Fan X., Ph. D. Thesis, University of California at Santa Barbara, March 2002.

50. Fleurial J. -P., Borshchevsky A., Ryan M. A., Phillips W., Kolawa E., Kacisch K., and Ewell R., Thermoelectric microcoolers for thermal management applications, Proceedings of 16th International Conference on Thermoelectrics, 1997; 641-645.

51. Venkatasubramanian R., Siivola E., Colpitts T., and O'Quinn B. Thin-film thermoelec- tric devices with high room-temperature figures of merit, Nature (London), 2001; 413: 597-602.

52. Harman, T.C., Taylor, P. J., Walsh, M. P. and LaForge, B. E., Quantum Dot Superlattice Thermoelectric Materials and Devices, *Science*, Vol. 297, No. 2229, 2002.

53. Fan, X, Zeng, G., Croke, E., LaBounty, C., Shakouri, A., and Bowers, J. E., Integrated SiGeC/Si Micro Cooler, Applied Physics Letters, Vol. 78, No.11, 12 March 2001.

54. Semenyuk V., Thermoelectric micro modules for spot cooling of high density heat sources, Proceedings of the 20th International Conference on Thermoelectrics, 2001; 391-396.

55. Semenyuk V., Cascade Thermoelectric micro modules for spot cooling high power electronic components, Proceedings of the 21st International Conference on Thermoelectrics, 2002; 531-534.

56. Semenyuk V. Thermoelectric cooling of electro-optic components, Thermoelectrics Handbook: Macro to Nano, Rowe, D. M., Ed., Boca Raton, FL: CRC Press, 2006.

57. www.thermion-company.com.

58. Ioffe A. F. Semiconductor Thermoelements and Thermoelectric Cooling, London, UK: Infosearch Ltd., 1957.

59. Ettenberg M. H., Jesser M. A., and Rosi E. D., A new n-type and improved p-type pseudo-ternary $(Bi_{2}Te_{3})(Sb_{2}Te_{3})(Sb_{2}Se_{3})$ alloy for Peltier cooling, Proceedings of the 15th International Conference on Thermoelectrics, 1996; 52-56.

60. Yamashita O., and Tomiyoshi S. Effect of annealing on thermoelectric properties of bismuth telluride compounds, Japan Journal of Applied Physics, 2003; 42: 492-500.

61. Yamashita O., Tomiyoshi S., and Makita K. Bismuth telluride compounds with high thermoelectric figures of merit, Journal of Applied Physics, 2003; 93: 368-374.

62. Yamashita O., and Tomiyoshi S. High performance n-type bismuth telluride with highly stable thermoelectric figure of merit, Journal of Applied Physics, 2004; 95: 6277-6283.

63. Shakouri A., and Zhang Y. On-chip solid-state cooling for integrated circuits using thin-film microrefrigerators, IEEE Transactions on Components and Packaging Technologies, 2005; 28: 65-69.

64. Pandey R. K., Sahu S. N., and Chandra S., Handbook of Semiconductor Deposition, Ed., New York: Marcel Dekker, 1996.

65. Snyder G. J., Lim J. R., Huang C., and Fleurial J. -P. Thermoelectric microdevice fabricated by a MEMS-like electrochemical process, Nature Materials, 2003; 2: 528-531.

66. da Silva L. W., Kaviany M., and Uher C. Thermoelectric performance of films in the bismuth-tellurium and antimony-tellurium systems, Journal of Applied Physics, 2005; 97: 114903.

67. Böttner H., Nurnus J., Gavrikov A., Kühner G., Jägle M., Künzel C., Eberhard D., Plescher G., Schubert A., and Schlereth K. New thermoelectric components using microsystem technologies, Journal of Microelectromechanical Systems, 2004; 13: 414-420.

68. Bottner H., Micropelt miniaturized thermoelectric devices: small size, high cooling power densities, short response time, Proceedings of the 24th International Conference on Thermoelectrics, 2005;1-8.

69. Zhou H., Rowe D. M., and Williams S. Peltier effect in a co-evaporated Sb2Te3(P)- Bi2Te3(N) thin film thermocouple, Thin Solid Films, 2002; 408: 270-274.

70. Semenyuk V., Miniature thermoelectric modules with increased cooling power, Proceedings of the 25th International Conference on Thermoelectrics, 2006; 322-326.

71. Semenyuk V., and Ph. D.. Dissertation, Odessa Technological Institute of Food and Refrigeratinbg Engineering, Odessa, USSR, 1967 (in Russian).

72. Hicks L. D., and Dresselhaus M. S. Thermoelectric figure of merit of a one-dimensional conductor, Physics Review B, 1993; 47: 16631-16634.

73. Balandin A., and Wang K. L. Effect of phonon confinement on the thermoelectric figure of merit of quantum wells, Journal of Applied Physics, 1998; 84: 6149-6153.

74. Balandin A., and Lazarenkova O. L. Mechanism for thermoelectric figure-of-merit enhance- ment in regimented quantum dot superlattices, Applied Physics Letters, 2003; 82: 415-417.

75. Yang B., and Chen G. Thermal Conductivity: Theory, Properties and Application, Tritt, T. M., Ed., New York: Kluwer Press, 2005.

76. Harman T. C., Taylor P. J., Walsh M. P., and LaForge B. E. Quantum dot superlattice thermoelectric materials and devices, Science, 2002; 297: 2229-2232.

77. Venkatasubramanian R., Silvona E., Colpitts T., and O'Quinn B. Thin-film thermoelectric devices with high room-temperature figures of merit, Nature, 2001; 413: 597-602.

78. Mahan G. D., and Woods L. M. Multilayer thermionic refrigeration, Physical Review Letter, 1998; 80: 4016-4019.

79. Shakouri A., LaBounty C., Piprek J., Abraham P., and Bowers J. E. Thermionic emission cooling in single barrier heterostructures, Applied Physics Letters, 1999; 74: 88-89.

80. Rowe D. M. Thermoelectrics Handbook Macro to Nano, Boca Raton, FL: CRC Press, 2005.

81. Venkatasubramanian R., Colpitts T., Liu S., El-Masry N., and Lamvik M. Low-temperature organometallic epitaxy and its application to superlattice structures in thermoelectrics, Applied Physics Letters, 1999; 75: 1104-1106.

82. Zhang Y., Zeng G., Bar-Cohen A., and Shakouri A. Is ZT the main performance factor for hot spot cooling using 3D microrefrigerators?, IMAPS on Thermal Management, 2005, Oct. 26th -28th, Palo Alto, CA.

83. Zeng G., Shakouri A., LaBounty C., Robinson G., Croke E., Abraham P., Fan X., Reese H., and Bowers J. E. SiGe micro-cooler, Electronics Letter, 1999; 35: 2146-2147.

84. Zeng G., Fan X., LaBounty C., Croke E., Zhang Y., Christofferson J., Vashaee D., Shakouri A., and Bowers J. E. Cooling power density of SiGe/Si superlattice micro refrigerators, Proceedings of Thermoelectric Materials Research and Applications, 2003; 793: 43-49.

85. Fan X., Zeng G., LaBounty C., Vashaee D., Christofferson J., Shakouri A., and Bowers J. E., Integrated cooling for Si-based microelectronics: Proceedings of 20th International Conference on Thermoelectrics, 2001; 405-408.

86. Fan X. SiGeC/Si superlattice microcoolers, Applied Physics Letters, 2001; 78: 1580-1582.

87. Fan X., Zeng G., LaBounty C., Croke E., Vashaee D., Shakouri A., Ahn C., and Bowers J. E. High cooling power density SiGe/Si micro coolers, Electronics Letter, 2001; 37: 126-127.

88. Herwaarden A. W., and Sarro P. M. Thermal sensors based on the Seebeck effect, Sensors and Actuators, 1986; 10: 321-346.

89. Geballe T. H., and Hull G. W. Seebeck effect in silicon, Physical Review, 1955; 98: 940-970.

90. Rowe D. M. CRC Handbook of Thermoelectrics, Roca Raton, FL: CRC Press, 1995.

91. Zhang Y., Shakouri A., and Zeng G. High-power-density spot cooling using bulk thermo- electrics, Applied Physics Letters, 2004; 85: 2977-2979.

92. Nieveld G. D. Thermopiles fabricated using silicon planar technology, Sensors and Actuators, 1983; 3: 179-183.

93. Chapman P. W., Tfte O. N., Zook J. D., and Long D. Electrical properties of heavily doped silicon, Journal of Applied Physics, 1963; 34: 3291-3295.

94. Wang P., Bar-Cohen A., and Yang B. Analytical modeling of silicon thermoelectric microcooler, Journal of Applied Physics, 2006; 100: 14501.

95. Wang P., and Bar-Cohen A. On-chip hot spot cooling using silicon-based thermoelectric microcooler, Journal of Applied Physics, 2007; 102: 034503.

96. Solbrekken G. L., Zhang Y., Bar-Cohen A., and Shakouri A., Use of superlattice thermionic emission for "Hotspot" reduction in convectively-cooled chip, Proceedings of 9th ITHERM's;04, 2004; 610-616.

97. Wang P., Bar-Cohen A., Yang B., Solbrekken G. L., Zhang Y., and Shakouri A., Thermoelectric microcooler for hotspot thermal management, Proceedings of InterPACK's;05, 2005; Paper No: 2005-7324.

98. Lide D. R., CRC Handbook of Chemistry and Physics, 75th edition, Boca Raton, USA: CRC Press, 1994.

99. Kraus A. D., and Bar-Cohen A. Thermal Analysis and Control of Electronic Equipment, New York, USA: Hemisphere Publishing Corporation 1983.

100. Geballe T. H., and Hull G. W. Seebeck effect in silicon, Physical Review, 1955; 98: 940-970.

101. Herwaarden A. W., and Sarro P. M. Thermal sensors based on the Seebeck effect, Sensors and Actuators, 1986; 10: 321-346.

102. Horn F. H. Densitometric and electrical investigation of boron in silicon, Physical Review, 1955; 97: 1521-1525.

103. Fritzsche H. A General expression for the thermoelectric power, Solid State Communication, 1971; 9: 1813-1815.

104. Chang C. Y., Fang Y. K., and Sze S. M. Specific contact resistance of metal-semiconductor barriers, Solid State Electronics, 1971; 14: 541-550.

105. Fan X., Silicon M., Ph. D. Thesis, University of California at Santa Barbara, 2002.

106. Yang B., Wang P., and Bar-Cohen A. Mini-contact enhanced thermoelectric cooling of hot spot in high power devices, IEEE Transactions on Components and Packaging Technologies, Part A, 2007; 30: 432-438.

107. Narasimhan S., Lofgreen K., Chau D., and Chrysler G., Thin film thermoelectric cooler thermal validation and product thermal performance estimation, Proceedings of 10th Intersociety Conference on Thermal and Thermo-mechanical Phenomena in Electronics Systems, San Diego, CA, May 30-June 2, 2006.

108. Gwinn J. P., and Webb R. L. Performance and testing of thermal interface materials, Microelectronics Journal, 2003; 34: 215-222.

109. Singhal V., Siegmund T., and Garimella S. V. Optimization of thermal interface materi- als for electronics cooling applications, IEEE Transactions on Components and Packaging Technologies, 2004; 27: 244-252.

110. Labudovic M., and Li J. Modeling of TE cooling of pump lasers, IEEE Transactions on Components and Packaging Technologies, 2004; 27: 724-730.

111. So W. W., and Lee C. C. Fluxless process of fabricating In-Au joints on copper substrates, IEEE Transactions on Components and Packaging Technologies, 2000; 23: 377-382.

112. www.thermion-company.com.

113. Semenyuk V. Thermoelectric cooling of electro-optic components, Thermoelectrics Handbook: Macro to Nano, Rowe, D. M. , Ed., Boca Raton, FL: CRC Press, 2006.

114. Wijngaards D. D. L., de Graaf G., and Wolffenbuttel R. F. Single-chip micro-thermostat applying both active heating and active cooling, Sensors and Actuators A, 2004; 110: 187-195.

115. Corrèges P., Bugnard E., Millerin C., Masiero A., Andrivet J. P., Bloc A., and Dunant Y. A simple, low-cost and fast Peltier thermoregulation set-up for electrophysiology, Journal of Neuroscience Methods, 1998; 83: 177-184.

116. McKinney C. J., and Nader M. W. A Peltier thermal cycling unit for radiopharmaceutical synthesis, Applied Radiation and Isotopes, 2001; 54: 97-100.

117. Elsgaard L., and Jørgensen L. W. A sandwich-designed temperature gradient incubator for studies of microbial temperature responses, Journal of Microbiological Methods, 2002; 49: 19-29.

118. Reid G., Amuzescu B., Zech E., and Flonta M. L. A system for applying rapid warm- ing or cooling stimuli to cells during patch clamp recording or ion imaging, Journal of Neuroscience Methods, 2001; 111: 1-8.

119. Hodgson J. Gene sequencing's industrial revolution, IEEE Spectrum, 2000; 37: 36-42.

120. Maltezos G., Johnston M., and Scherer A. Thermal management in microfluidics using micro-Peltier junctions, Applied Physics Letters, 2005; 87: 154105.

121. Bachmann C., and Bar-Cohen A., Hotspot remediation with anisotropic thermal interface materials, Proceedings of ITHERM 2008, 2008; 238-247.

122. Muzychka Y. S., Culham J. R., and Yovanovich M. M. Thermal spreading resistance of eccentric heat sources on rectangular flux channels, Journal of Electronic Packaging, 2003; 125: 178-185.

123. Smalc M., Thermal performance of natural graphite heat spreaders, Proceedings IPACK2005, San Francisco, California, USA, July 17-22, PaperNumber: IPACK2005-73073.

124. Bar-Cohen A., Arik M., and Ohadi M. Direct liquid cooling of high flux micro and nano electronic components, Proceedings of the IEEE, 2006; 94: 1549-1570.

125. Montesano M., Annealed pyrolytic graphite, Advanced Materials and Processes, 2006; June:1-3.

126. Viswanath R., Wakharkar V., Watwe A., and Lebonheur V. Thermal performance challenges from silicon to systems, Intel Technology Journal, 2000; Quarter 3: 1-16.

127. Xong Y., Smalc M. et al., Thermal tests and analysis of thin graphite heat spreader for hot spot reduction in handheld devices, Proceedings of ITHERM 2008, 2008; 583-590.

128. Bergles A. E., and Bar-Cohen A. Immersion cooling of digital computers, Cooling of Electronic Systems, Kakac, S., Yuncu, H. and Hijikata, K., Eds., Boston, MA: Kluwer Academic Publishers, 1994, 539-621

129. Bergles A. E., and Bar-Cohen A. Direct liquid cooling of microelectronic components, Advances in Thermal Modeling of Electronic Components and Systems, A. Bar-Cohen and A. D. Kraus, Eds., New York: ASME, 1990; 2: 241-250.

130. Kim D., Rahim E., Bar-Cohen A., and Han B., Thermofluid characteristics of two-phase flow in micro-gap channels, Proceedings of ITHERM 2008, 2008; 979-992.

131. Kim D. W., Ph.D. Thesis, University of Maryland, 2007.

132. Bar-Cohen A., and Rahim E. Modeling and prediction of two-phase microgap channel heat transfer characteristics, Heat Transfer Engineering, 2009; 30: 601-625.