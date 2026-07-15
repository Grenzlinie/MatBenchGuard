# A numerical model and comparative investigation of a thermoelectric generator with multi-irreversibilities

Fankai Meng, Lingen Chen*, Fengrui Sun

College of Naval Architecture and Power, Naval University of Engineering, Wuhan 430033, PR China

---

## ARTICLE INFO

**Article history:**
Received 6 October 2010
Received in revised form
21 March 2011
Accepted 22 March 2011
Available online 19 April 2011

**Keywords:**
Thermoelectric generator
Power generation
Numerical model
Heat exchanger
Waste-heat recovery

---

## ABSTRACT

Taking into account inner and external multi-irreversibilities, a complete numerical model of commercial thermoelectric generator with finned heat exchangers is established by combining thermodynamics with heat transfer theory. A significant novelty is that physical properties, geometric dimensions, temperature parameters and flow parameters are all considered in the model. The inner effects include Seebeck effect, Fourier effect, Joule effect and Thomson effect. The irreversibilities include the heat transfer through the air gap (proposed and evaluated first time), the thermal and electrical resistance of the conducting strips, and the multiform external thermal resistances. Based on the numerical model, the performances of a typical commercial thermoelectric generator are simulated. Hot water at 60-100 °C and cold water at 27 °C are employed as heat source and sink of the generator module which consists of 127 thermoelectric elements. The results show that the maximum power output of 0.13 W and the maximum efficiency of 0.87% are available from the generator. The open circuit voltage is 1.80 V and the short circuit current is 0.28 A, respectively. The effects of external irreversibilities on the performance of the thermoelectric generator are analyzed by comparing this irreversible model with the exo-reversible model. The numerical model and calculation method can be applied to the performance prediction and optimization of thermoelectric generators with finned heat exchangers. The simulation results can be used as feasibility and effectiveness reference by employing low-grade energy or waste heat for power generation.

© 2011 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

There are several processes that can create electrical current from a thermal gradient: thermoelectric [1], thermionic, thermomagnetism, ferroelectricity, and the Nernst effect. Thermoelectric conversion is the most effective of these processes [2,3]. Moreover, the most successful approach employing indirect conversion of alpha or beta emissions into electricity is using thermoelectric effect. That is called a radioisotopic thermoelectric generator (RTG) [4] which is used in Micro-electromechanical Systems (MEMS) frequently. As a low-carbon energy technology, thermoelectrics have been used in military, aerospace, instrument, and industrial or commercial products, as a power generation for specific purposes. More widespread use of thermoelectric device requires not only improving the intrinsic energy-conversion efficiency of the materials [5,6], but also modeling and analyzing of thermoelectric device system [7,8].

In general, conventional non-equilibrium thermodynamics [9-11] is used to analyze the performance of one or multi-element thermoelectric generators. Considering the inner structure of a thermoelectric generator, a significant increase in the electrical power output from a module can be achieved by modifying the geometry of the thermoelectric elements [12,13]. Rowe investigated the efficiency of a single couple solar powered thermoelectric generator [14] and reviewed US applications of nuclear-powered thermoelectric generators in space [15]. Sisman and Yavuz [16] analyzed the effect of Joule losses on the total efficiency of a thermoelectric power-cycle. Chen et al. [17] investigated the influence of Thomson effect on the maximum power output and maximum efficiency of a thermoelectric generator. Xuan et al. [18] employed a phenomenological model to study the effects of internal and/or external interface layers on thermoelectric devices performance.

Thermoelectric devices cannot be used independently. They should be connected with heat exchangers to absorb and dissipate heat [19-21]. The theory of finite time thermodynamics (FTT) or entropy-generation minimization [22-31] is a powerful tool for the performance analysis and optimization of practical thermodynamic processes and devices with heat transfer. Some authors have investigated the performances of thermoelectric generators using a combination of finite time thermodynamics and non-equilibrium thermodynamics. Considering the external irreversibilities of

* Corresponding author. Tel.: +86 27 83615046; fax: +86 27 83638709.
E-mail addresses: lgchenna@yahoo.com, lingenchen@hotmail.com (L. Chen).

0360-5442/$ - see front matter © 2011 Elsevier Ltd. All rights reserved.
doi:10.1016/j.energy.2011.03.057

### Nomenclature

|  |  |  |  |
|---|---|---|---|
| $A$ | area ($\text{m}^2$) | $\nu$ | kinematic viscosity ($\text{m}^2\ \text{s}^{-1}$) |
| $a$ | thermal diffusivity ($\text{m}^2/\text{s}$) | $\omega$ | intermediate variable |
| $c$ | heat capacity ratio ($\text{J}\ \text{kg}^{-1}\ \text{K}^{-1}$) |  |  |
| $eJ$ | electrical current density ($\text{A}\ \text{m}^{-2}$) | **Subscripts** |  |
| $F$ | intermediate variable | a | side |
| $g$ | gravitational acceleration ($\text{m}\ \text{s}^{-2}$) | b | base, inner surface |
| $H$ | height (m) | c | cold junction, channel |
| $h$ | heat transfer coefficient ($\text{W}\ \text{m}^{-2}\ \text{K}^{-1}$) | cd | heat conduction |
| $I$ | electrical current output (A) | cp | ceramic plate |
| $K$ | thermal conductance ($\text{W}\ \text{K}^{-1}$) | cu | copper conducting strip |
| $k$ | thermal conductivity ($\text{W}\ \text{m}^{-1}\ \text{K}^{-1}$) | cv | heat convection |
| $L$ | length (m) | e | external |
| $m$ | intermediate variable | ex | exchanger |
| $N$ | number | er | external reversible |
| $P$ | power output (W) | f | fin, fluid |
| $p$ | perimeter (m) | g | generation, air gap |
| $Q$ | heat flow rate (W) | H | heat source |
| $R$ | electrical resistance ($\Omega$), thermal resistance ($\text{K}\ \text{W}^{-1}$) | h | hot junction |
| $S$ | entropy generation rate ($\text{W}\ \text{K}^{-1}$) | i | exterior surface |
| $T$ | temperature (K) | in | input |
| $U$ | voltage output (V) | J | Joule heat |
| $v$ | velocity ($\text{m}\ \text{s}^{-1}$) | K | heat conduction leakage |
| $x$ | coordinate | n | N-type semiconductor leg |
| $Z$ | figure of merit of a thermoelectric element $Z=\alpha^{2}/(KR)$ | out | output |
|  |  | p | P-type semiconductor leg |
| **Greek letters** |  | rd | heat radiation |
| $\alpha$ | Seebeck coefficient ($\text{V}\ \text{K}^{-1}$) | T | total |
| $\beta$ | coefficient of cubical expansion ($\text{K}^{-1}$) | te | thermoelectric element |
| $\Delta$ | difference |  |  |
| $\delta$ | thickness (m) | **Superscripts** |  |
| $\epsilon$ | blackness | $P$ | at maximum power output |
| $\varphi$ | kinetic viscosity ($\text{kg}\ \text{m}^{-1}\ \text{s}^{-1}$) | $\eta$ | at maximum efficiency |
| $\eta$ | Efficiency |  |  |
| $\mu$ | Thomson coefficient ($\text{V}\ \text{K}^{-2}$) | **Abbreviation** |  |
| $\theta$ | packed density | $Gr$ | Grashof number $Gr = g\beta\Delta TL^{3}/\nu^{2}$ |
| $\rho$ | electrical resistivity ($\Omega\text{m}$) | $Nu$ | Nusselt number $Nu = hH/k_{\text{f}}$ |
| $\sigma$ | electrical conductivity ($\Omega^{-1}\ \text{m}^{-1}$) | $Pr$ | Prandtl number $Pr = \nu/a$ |
|  |  | $Ra$ | Rayleigh number $Ra = g\beta\Delta TL^{3}/a\nu$ |
|  |  | $Re$ | Reynolds number $Re = v_{\text{f}}H/\nu_{\text{f}}$ |

a thermoelectric generator, much work has shown that the heat transfer irreversibilities between the device and its external reservoirs affect the performances of thermodynamic processes strongly. Gordon [32], Wu [33], Agrawal and Menon [34], Chen et al. [35,36] and Nuwayhid et al. [37,38] analyzed the effect of finite-rate heat transfer between the thermoelectric device and its external heat reservoirs on the performance of single-element thermoelectric generators.

In practice, a commercial thermoelectric generator is a multiel-ement device, which is composed of many fundamental thermoelectric elements. Many researchers investigated the characteristics of multielement thermoelectric generators with the irreversibility of finite-rate heat transfer, Joulean heat inside the thermoelectric device, and the heat leak through the thermoelectric element. Esarte et al. [39] analyzed the influence of fluid flow rate, heat exchanger geometry, fluid properties and inlet temperatures on the power supplied by the thermoelectric generator. Chen et al. [40,41] analyzed the effects of external heat conductance and the number of elements on the power and efficiency of a multielement generator. Yu and Zhao [42] presented a numerical model to predict the performance of thermoelectric generator with the parallel-plate heat exchanger. Niu et al. [43] constructed an experimental thermoelectric generator unit incorporating the commercially available thermoelectric modules with the parallel-plate heat exchanger. Behrens et al. [44] shown that the combustion of energy dense liquid fuels in a catalytic micro-combustor can combust completely for thermoelectric applications. Astrain et al. [45] studied the influence of heat exchangers' thermal resistances on a thermoelectric generation system without the internal factors of the system. Hsiao et al. [46] built a one-dimensional thermal resistance model to predict the behavior of thermoelectric modules applied in exhaust and radiator of an automobile without considering the Thomson effect and the heat transfer through the air gap of the module.

Reviewing the former literatures concerning thermoelectric generators, some features can be concluded as follows:

(1) Researches on the inner structure of a thermoelectric generator are without consideration of the effects of external heat transfer irreversibilities.
(2) Researches on the effects of external irreversibilities of a thermoelectric generator are without consideration of the Thomson effect, inner structure and geometric dimension of the thermoelectric generator.
(3) Most of the researches are without consideration of the effects of the conducting strips, ceramic plate and the heat transfer through the air gap of the module.

To sum up, there is a lack of a complete numerical model which can be applied to analyze the quantities of effects of inner and external factors on the performance of a commercial thermoelectric generator with heat exchangers, and can be applied to describe, calculate and predict the practical performance of a commercially available thermoelectric generator.

Taking into account inner and external multi-irreversibilities, this paper aims to establish a complete numerical model of commercial thermoelectric generator with finned heat exchangers by combining the thermodynamics with heat transfer theory. Based on the numerical model, the characteristic of a typical commercial thermoelectric generator is simulated. The effects of external irreversibilities on the performance of the thermoelectric generator are analyzed and compared with the exo-reversible model. The numerical model and calculation method may be applied to the calculation, prediction and further optimization study for thermoelectric generators. The simulation results can be used as feasibility and effectiveness reference by employing low-grade energy or waste heat for power generation.

## 2. Analysis of a thermoelectric generator and a complete numerical model

### 2.1. Structure of a thermoelectric generator module

A typical commercial thermoelectric generator with finned heat exchangers is shown in Fig. 1. A thermoelectric generator consists of positive-type (P-type) and negative-type (N-type) semiconductor legs. The thermoelectric semiconductor legs are connected by copper conducting strips in serials. A P-type and an N-type semiconductor leg compose a basic thermoelectric element. The structure of the thermoelectric element and the conducting strip is shown in Fig. 2. The length and the side length of the cross-section of a semiconductor leg are respectively $L$, $L_b$ and $L_b$. $L_a = L_b$ holds for a typical commercial thermoelectric module. The length and the thickness of the conducting strip are $L_{cu}$ and $\delta_{cu}$, respectively. The number of thermoelectric elements is $N$. The conducting strips of the thermoelectric elements are fixed at a thermal conducting and electrical insulting ceramic plate. For a typical commercial thermoelectric module, the ceramic plate is square. The area and thickness of the ceramic plate are respectively $A_{cp}$ and $\delta_{cp}$. The module is packaging by thermal insulation epoxy resin. The thermoelectric elements in most commercial thermoelectric generator modules are not closely arranged, that is, air gap exists in the module. The heat convection (or conduction) and radiative heat transfer occur between the two ceramic plates in the area where the thermoelectric elements don't occupy. It is assumed that the total area of the air gap is $A_g$.

![](./images/811666263204954115_1.jpg)

Fig. 1. Structure of a thermoelectric generator with finned heat exchangers.

![](./images/811666263204954115_2.jpg)

Fig. 2. Schematic diagram of a thermoelectric element.

### 2.2. Structure of a finned heat exchanger

A finned heat exchanger used for fluid heating or cooling is shown in Fig. 3. The base area, thickness and the side length of the exchanger are $A_b$, $\delta_{exb}$ and $L_{ex}$, respectively. The height, length and thickness of the fin are $H_f$, $L_f$ and $\delta_f$, respectively. The width of the channel is $\delta_c$. $L_{ex} = L_f$ holds for a heat exchanger with square base.

### 2.3. Thermal resistance network

The thermal resistance network of the whole device is shown in Fig. 4. All the heat transfers are finite-rate irreversible heat transfer.

The hot and cold junction temperatures of the thermoelectric elements are $T_H$ and $T_c$, respectively. The ceramic plate inner surface temperatures are $T_{cpbh}$ and $T_{cpbc}$. The ceramic plate exterior surface temperatures are $T_{cpih}$ and $T_{cpic}$. The fin base temperatures are $T_{exbh}$ and $T_{exbc}$. The heat source (hot fluid) and heat sink (cold fluid) temperatures are $T_H$ and $T_L$, respectively.

The heat conduction thermal resistance of a thermoelectric element is $R_{te} = 1/K$, where $K$ is the thermal conductance of a thermoelectric element. The conducting strip heat conduction thermal resistance are $R_{cutc}$ and $R_{cuth}$. The heat convection (or conduction) and radiative thermal resistance of the air gap are $R_{cvg}$ and $R_{rdg}$, respectively. The ceramic plate base heat conduction thermal resistance are $R_{cph}$ and $R_{cpc}$. The heat exchanger base heat conduction thermal resistance are $R_{exbh}$ and $R_{exbc}$. The heat convection thermal resistance between the heat exchangers and the heat reservoirs are $R_{cvh}$ and $R_{cvc}$.

![](./images/811666263204954115_3.jpg)

Fig. 3. Schematic diagram of a finned heat exchanger.

![](./images/811666263204954115_4.jpg)

Fig. 4. Schematic diagram of the thermal resistance network.

The heat flow rate absorbed from the heat source to the module is $Q_{\text{H}}$. The heat flow rate dissipated from the module to the heat sink is $Q_{\text{L}}$. The heat flow rate through the hot and cold junctions of the thermoelectric elements are $Q_{\text{h}}$ and $Q_{\text{c}}$. The heat flow rate of the air gap leakage is $Q_{\text{g}}$.

### 2.4. Electrical-resistance network

The electrical-resistance network of the whole device is shown in Fig. 5. The electrical resistance of the P- and N-type semiconductor leg are $R_{\text{p}}$ and $R_{\text{n}}$. The electrical resistance of the conducting strip are $R_{\text{cuh}}$ and $R_{\text{cuc}}$. The voltage output, electrical current output and load resistance are $U, I$ and $R_{\text{L}}$, respectively.

### 2.5. Energy equations

For a well-designed thermal insulation packaging module, the heat leakage through the surround of the module can be neglected. At steady work state, the temperature distribution of the air gap is the same with the thermoelectric elements, so the heat transfer of the whole device can be treated as one-dimensional heat transfer.

The infinitesimal as shown in Fig. 6 is considered. According to the non-equilibrium thermodynamics, the inner effects of the thermoelectric elements include Seebeck effect, Fourier effect, Joule effect and Thomson effect. The increment rate of inner energy of the infinitesimal is zero at steady-state, so one can obtain the energy conservation equation of P-type semiconductor leg as follows [1,2]

$$Q_{\text{Kin}} - Q_{\text{Kout}} + Q_{\text{J}} + Q_{\mu} = 0 \tag{1}$$

where $Q_{\text{Kin}}, Q_{\text{Kout}}, Q_{\text{J}}$ and $Q_{\mu}$ are the Fourier heat input, Fourier heat output, generated Joule heat and Thomson heat, respectively. Eq. (1) can be written as

$$\frac{\text{d}}{\text{d}x}(T_{\text{p}} + \text{d}T_{\text{p}}) k_{\text{p}}A_{\text{p}} - \frac{\text{d}T_{\text{p}}}{\text{d}x}k_{\text{p}}A_{\text{p}} + \left(eJ_{\text{p}}\right)^2\frac{A_{\text{p}}L_{\text{p}}}{\sigma_{\text{p}}}\frac{\text{d}x}{L_{\text{p}}} + \mu_{\text{p}}I\text{d}T_{\text{p}} = 0 \tag{2}$$

where $k_{\text{p}}, \sigma_{\text{p}}, \mu_{\text{p}}, A_{\text{p}}, L_{\text{p}}, T_{\text{p}}, eJ_{\text{p}}$ are respectively the thermal conductivity, electrical conductivity, Thomson coefficient, cross-section area, length, temperature and electrical current density of the P-type semiconductor leg. Reforming Eq. (2) and making same analysis on the N-type semiconductor leg, one can obtain the heat conduction differential equations (3) and (4), with boundary conditions (5) and (6) as follows [11]

$$\frac{\text{d}}{\text{d}x}\left(k_{\text{p}}\frac{\text{d}T_{\text{p}}}{\text{d}x}\right) + eJ_{\text{p}}\mu_{\text{p}}\frac{\text{d}T_{\text{p}}}{\text{d}x} + \frac{\left(eJ_{\text{p}}\right)^2}{\sigma_{\text{p}}} = 0 \tag{3}$$

$$\frac{\text{d}}{\text{d}x}\left(k_{\text{n}}\frac{\text{d}T_{\text{n}}}{\text{d}x}\right) - eJ_{\text{n}}\mu_{\text{n}}\frac{\text{d}T_{\text{n}}}{\text{d}x} + \frac{\left(eJ_{\text{n}}\right)^2}{\sigma_{\text{n}}} = 0 \tag{4}$$

$$T_{\text{p}}(0) = T_{\text{n}}(0) = T_{\text{c}} \tag{5}$$

$$T_{\text{p}}(L_{\text{p}}) = T_{\text{n}}(L_{\text{n}}) = T_{\text{h}} \tag{6}$$

where $k_{\text{n}}, \sigma_{\text{n}}, \mu_{\text{n}}, A_{\text{n}}, T_{\text{n}}, eJ_{\text{n}}$ respectively are the thermal conductivity, electrical conductivity, Thomson coefficient, temperature and electrical current density of the N-type semiconductor leg.

Taking into account the effect of temperature dependence of thermoelectric properties, $k_{\text{p}}, \sigma_{\text{p}}$ and $\mu_{\text{p}}$ are function of $T_{\text{p}}$; while $k_{\text{n}}$, $\sigma_{\text{n}}$ and $\mu_{\text{n}}$ are function of $T_{\text{n}}$. However, such a differential equation cannot be solved analytically. Replacing $k, \sigma$ and $\mu$ with the mean value $\bar{k}, \bar{\sigma}$ and $\bar{\mu}$ approximately gives approximation of Eqs. (3) and (4) as follows

$$\bar{k}_{\text{p}}A_{\text{p}}\frac{\text{d}T_{\text{p}}^2}{\text{d}x^2} + \bar{\mu}_{\text{p}}I\frac{\text{d}T_{\text{p}}}{\text{d}x} + \frac{I^2}{\bar{\sigma}_{\text{p}}A_{\text{p}}} = 0 \tag{7}$$

$$\bar{k}_{\text{n}}A_{\text{n}}\frac{\text{d}T_{\text{n}}^2}{\text{d}x^2} - \bar{\mu}_{\text{n}}I\frac{\text{d}T_{\text{n}}}{\text{d}x} + \frac{I^2}{\bar{\sigma}_{\text{n}}A_{\text{n}}} = 0 \tag{8}$$

where $\bar{k}_{\text{p}} = \left.k_{\text{p}}\right|_{T=(T_{\text{h}}+T_{\text{c}})/2}, \bar{\sigma}_{\text{p}} = \left.\sigma_{\text{p}}\right|_{T=(T_{\text{h}}+T_{\text{c}})/2}, \bar{\mu}_{\text{p}} = \left.\mu_{\text{p}}\right|_{T=(T_{\text{h}}+T_{\text{c}})/2}$

![](./images/811666263204954115_5.jpg)

Fig. 5. Schematic diagram of the electrical-resistance network.

![](./images/811666263204954115_6.jpg)

Fig. 6. Schematic diagram of the heat transfer of a thermoelectric element.

for P-type semiconductor leg and $\bar{k}_{\mathrm{n}}=\left.k_{\mathrm{n}}\right|_{T=\left(T_{\mathrm{h}}+T_{\mathrm{c}}\right) / 2}$, $\bar{\sigma}_{\mathrm{n}}=\left.\sigma_{\mathrm{n}}\right|_{T=\left(T_{\mathrm{h}}+T_{\mathrm{c}}\right) / 2}$, $\bar{\mu}_{\mathrm{n}}=\left.\mu_{\mathrm{n}}\right|_{T=\left(T_{\mathrm{h}}+T_{\mathrm{c}}\right) / 2}$ for N-type. Alteration method along with the following fitted formulas Eqs. (53)-(55) are adopted to determine the junction temperatures $T_{\mathrm{h}}$ and $T_{\mathrm{c}}$.

The total heat flow rates through the hot and cold junctions are

$$
Q_{\mathrm{h}}=N\left(\left(\alpha_{\mathrm{ph}}-\alpha_{\mathrm{nh}}\right) T_{\mathrm{h}} I+\left.\bar{k}_{\mathrm{p}} A_{\mathrm{p}} \frac{\mathrm{d} T_{\mathrm{p}}}{\mathrm{d} x}\right|_{x=L_{\mathrm{p}}}+\left.\bar{k}_{\mathrm{n}} A_{\mathrm{n}} \frac{\mathrm{d} T_{\mathrm{n}}}{\mathrm{d} x}\right|_{x=L_{\mathrm{n}}}\right) \quad(9)
$$

$$
Q_{\mathrm{c}}=N\left(\left(\alpha_{\mathrm{pc}}-\alpha_{\mathrm{nc}}\right) T_{\mathrm{c}} I+\left.\bar{k}_{\mathrm{p}} A_{\mathrm{p}} \frac{\mathrm{d} T_{\mathrm{p}}}{\mathrm{d} x}\right|_{x=0}+\left.\bar{k}_{\mathrm{n}} A_{\mathrm{n}} \frac{\mathrm{d} T_{\mathrm{n}}}{\mathrm{d} x}\right|_{x=0}\right) \quad(10)
$$

where $\alpha_{\mathrm{p}}$ and $\alpha_{\mathrm{n}}$ are the Seebeck coefficient of the P- and N-type semiconductor leg, and the subscript h and c represent the hot and cold side, respectively.

The heat flow rates through the conducting strips are given by

$$
Q_{\mathrm{hi}}=N\left(T_{\mathrm{cpbh}}-T_{\mathrm{h}}\right) / R_{\text {cuth }} \quad(11)
$$

$$
Q_{\mathrm{ci}}=N\left(T_{\mathrm{c}}-T_{\mathrm{cpbc}}\right) / R_{\text {cutc }} \quad(12)
$$

It is assumed that the total thermal resistance between the hot side ceramic plate inner surface and the heat source is $R_{\mathrm{eh}}=R_{\mathrm{cvh}}+R_{\mathrm{exbh}}+R_{\mathrm{cph}}$ (as shown in Fig. 4); the total thermal resistance between the cold side ceramic plate inner surface and the heat sink is $R_{\mathrm{ec}}=R_{\mathrm{cvc}}+R_{\mathrm{exbc}}+R_{\mathrm{cpc}}$. Then, one has

$$
Q_{\mathrm{H}}=\left(T_{\mathrm{H}}-T_{\mathrm{cpbh}}\right) / R_{\mathrm{eh}} \quad(13)
$$

$$
Q_{\mathrm{L}}=\left(T_{\mathrm{cpbc}}-T_{\mathrm{L}}\right) / R_{\mathrm{ec}} \quad(14)
$$

The heat flow rate through the air gap (gray arrows in Fig. 1) $Q_{\mathrm{g}}$ can be expressed as

$$
Q_{\mathrm{g}}=Q_{\mathrm{cvg}}+Q_{\mathrm{rdg}} \quad(15)
$$

$$
Q_{\mathrm{cvg}}=\left(T_{\mathrm{cpbh}}-T_{\mathrm{cpbc}}\right) / R_{\mathrm{cvg}} \quad(16)
$$

$$
Q_{\mathrm{rdg}}=\left(T_{\mathrm{cpbh}}^{4}-T_{\mathrm{cpbc}}^{4}\right) / R_{\mathrm{rdg}} \quad(17)
$$

where $Q_{\mathrm{cvg}}, Q_{\mathrm{rdg}}, R_{\mathrm{cvg}}$ and $R_{\mathrm{rdg}}$ represent the convection heat rate, radiative heat rate, heat convection resistance and heat radiative resistance, respectively.

The relations of heat flow rates can be expressed as follows:

$$
Q_{\mathrm{H}}=Q_{\mathrm{h}}+Q_{\mathrm{g}} \quad(18)
$$

$$
Q_{\mathrm{h}}=Q_{\mathrm{hi}} \quad(19)
$$

$$
Q_{\mathrm{c}}=Q_{\mathrm{ci}} \quad(20)
$$

$$
Q_{\mathrm{L}}=Q_{\mathrm{c}}+Q_{\mathrm{g}} \quad(21)
$$

## 3. Solution of the model

### 3.1. Solution of the thermoelectric element

The temperature distribution of the P- and N-type semiconductor leg can be obtained by solving Eqs. (7) and (8) as follows:

$$
T_{\mathrm{p}}(x)=T_{\mathrm{c}}-F_{\mathrm{p}} x+\frac{T_{\mathrm{h}}-T_{\mathrm{c}}+F_{\mathrm{p}} L_{\mathrm{p}}}{\left(e^{-\omega_{\mathrm{p}} L_{\mathrm{p}}}-1\right)}\left(e^{-\omega_{\mathrm{p}} x}-1\right)
$$

$$
T_{\mathrm{n}}(x)=T_{\mathrm{c}}+F_{\mathrm{n}} x+\frac{T_{\mathrm{h}}-T_{\mathrm{c}}-F_{\mathrm{n}} L_{\mathrm{n}}}{\left(e^{\omega_{\mathrm{n}} L_{\mathrm{n}}}-1\right)}\left(e^{\omega_{\mathrm{n}} x}-1\right)
$$

where $\omega_{\mathrm{p}}=\bar{\mu}_{\mathrm{p}} I /\left(\bar{k}_{\mathrm{p}} A_{\mathrm{p}}\right), F_{\mathrm{p}}=I /\left(\bar{\sigma}_{\mathrm{p}} \bar{\mu}_{\mathrm{p}} A\right), \omega_{\mathrm{n}}=\bar{\mu}_{\mathrm{n}} I /\left(\bar{k}_{\mathrm{n}} A_{\mathrm{n}}\right)$ and $F_{\mathrm{n}}=I /\left(\bar{\sigma}_{\mathrm{n}} \bar{\mu}_{\mathrm{n}} A\right)$.

For maximum figure of merit of the thermoelectric element $Z=\alpha^{2} /(K R)$, the geometry dimension of the thermoelectric element and the physical property of the material should satisfy the following equation [1,2]

$$
\frac{A_{\mathrm{p}}^{2} L_{\mathrm{n}}^{2}}{A_{\mathrm{n}}^{2} L_{\mathrm{p}}^{2}}=\frac{k_{\mathrm{n}} \sigma_{\mathrm{n}}}{k_{\mathrm{p}} \sigma_{\mathrm{p}}} \quad(24)
$$

To reduce the cost of manufacture, the P- and N-type semiconductor legs are made with same geometry dimensions i.e. $A_{\mathrm{p}}=A_{\mathrm{n}}=A$ and $L_{\mathrm{p}}=L_{\mathrm{n}}=L$. So one has $k_{\mathrm{n}} \sigma_{\mathrm{n}} /\left(k_{\mathrm{p}} \sigma_{\mathrm{p}}\right)=1$ by Eq. (24). Similar doped alloys are adopted to make P- and N-type semiconductor legs. That is $\sigma_{\mathrm{p}}=\sigma_{\mathrm{n}}=\sigma, k_{\mathrm{p}}=k_{\mathrm{n}}=k, \alpha_{\mathrm{p}}=-\alpha_{\mathrm{n}}, \mu_{\mathrm{p}}=-\mu_{\mathrm{n}}$. According to Taylor's formula, when $|x| \ll 1, e^{x} \approx 1+x$ holds true. Based on above assumption, Eqs. (9) and (10) can be approximated as follows at the case of $\bar{\mu} I / K \ll 1$

$$
Q_{\mathrm{h}}=N\left[\alpha_{\mathrm{h}} I T_{\mathrm{h}}+K\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)-0.5 I^{2} R-0.5 \bar{\mu} I\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right] \quad(25)
$$

$$
Q_{\mathrm{c}}=N\left[\alpha_{\mathrm{c}} I T_{\mathrm{c}}+K\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)+0.5 I^{2} R+0.5 \bar{\mu} I\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right] \quad(26)
$$

where $\alpha_{\mathrm{h}}=\alpha_{\mathrm{hp}}-\alpha_{\mathrm{hn}}$ and $\alpha_{\mathrm{c}}=\alpha_{\mathrm{cp}}-\alpha_{\mathrm{cn}}$ are the Seebeck coefficient of the thermoelectric elements at hot and cold side. $\bar{\mu}=\bar{\mu}_{\mathrm{p}}-\bar{\mu}_{\mathrm{n}}=2 \bar{\mu}_{\mathrm{p}}, K$ and $R$ are respectively the total Thomson coefficient, thermal conductance and electrical resistance of a thermoelectric element. $\alpha I T, K \Delta T, I^{2} R$ and $\bar{\mu} I \Delta T$ are the rates of Peltier heat, Fourier heat, Joule heat and Thomson heat, respectively. $K$ and $R$ are given by

$$
K=K_{\mathrm{p}}+K_{\mathrm{n}}=\bar{k}_{\mathrm{p}} A_{\mathrm{p}} / L_{\mathrm{p}}+\bar{k}_{\mathrm{n}} A_{\mathrm{n}} / L_{\mathrm{n}}=2 \bar{k} A / L \quad(27)
$$

$$
R=R_{\mathrm{p}}+R_{\mathrm{n}}=L_{\mathrm{p}} /\left(\bar{\sigma}_{\mathrm{p}} A_{\mathrm{p}}\right)+L_{\mathrm{n}} /\left(\bar{\sigma}_{\mathrm{n}} A_{\mathrm{n}}\right)=2 L /(\bar{\sigma} A) \quad(28)
$$

The power output is the difference between the absorbed and dissipated heat flow rate and results in

$$
P=Q_{\mathrm{h}}-Q_{\mathrm{c}}=N I\left[\alpha_{\mathrm{h}} T_{\mathrm{h}}-\alpha_{\mathrm{c}} T_{\mathrm{c}}-I R-\bar{\mu}\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right] \quad(29)
$$

Taking the Joule heat generated by the conducting strips as the thermoelectric elements generated and replacing $R$ with $R_{\mathrm{t}}=R+R_{c u}$ gives the modified power output as follows

$$
P=N I\left[\alpha_{\mathrm{h}} T_{\mathrm{h}}-\alpha_{\mathrm{c}} T_{\mathrm{c}}-I R_{\mathrm{t}}-\bar{\mu}\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right] \quad(30)
$$

The thermal efficiency $\eta=P / Q_{\mathrm{H}}$ is given by

$$
\eta=\frac{N I\left[\alpha_{\mathrm{h}} T_{\mathrm{h}}-\alpha_{\mathrm{c}} T_{\mathrm{c}}-I R_{\mathrm{t}}-\bar{\mu}\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right]}{\left(T_{\mathrm{H}}-T_{\mathrm{cpbh}}\right) / R_{\mathrm{eh}}} \quad(31)
$$

Taking the heat source, heat sink, thermoelectric generator and heat exchangers as an isolated system, the entropy production rate of the system is the entropy increase of the system, and results in

$$
S_{\mathrm{g}}=\Delta S_{\mathrm{H}}+\Delta S_{\mathrm{L}}+\Delta S_{\mathrm{TEG}}=-Q_{\mathrm{H}} / T_{\mathrm{H}}+Q_{\mathrm{L}} / T_{\mathrm{L}} \quad(32)
$$

where $\Delta S_{\mathrm{H}}$, $\Delta S_{\mathrm{L}}$ and $\Delta S_{\mathrm{TEG}}$ are the entropy increase of the heat source, heat sink and the thermoelectric generator, respectively. $\Delta S_{\mathrm{TEG}}=0$ because the thermoelectric generator is in steady.

### 3.2. Calculation method of the thermal and electrical resistances

The heat conduction thermal resistance of a conducting strip and a ceramic plate are as follows:

$$
R_{\mathrm{cut}}=\delta_{\mathrm{cu}} /\left(k_{\mathrm{cu}} A\right) \tag{33}
$$

$$
R_{\mathrm{cp}}=\delta_{\mathrm{cp}} /\left(k_{\mathrm{cp}} A_{\mathrm{cp}}\right) \tag{34}
$$

The heat conduction thermal resistance of the heat exchanger base is

$$
R_{\mathrm{exb}}=\delta_{\mathrm{b}} /\left(k_{\mathrm{ex}} A_{\mathrm{b}}\right) \tag{35}
$$

According to the heat transfer theory [47-49], the heat convection thermal resistance between the finned heat exchanger and the heat reservoir is

$$
R_{\mathrm{cv}}=\frac{1}{h_{\mathrm{cv}} A_{\mathrm{eff}}} \tag{36}
$$

where $h_{\mathrm{cv}}$ and $A_{\mathrm{eff}}$ are respectively the coefficient of heat convection and the effective heat transfer area. $h_{\mathrm{cv}}$ can be calculated by

$$
h_{\mathrm{cv}}=\frac{N u k_{\mathrm{f}}}{H_{\mathrm{f}}} \tag{37}
$$

where $N u$, $k_{\mathrm{f}}$ and $H_{\mathrm{f}}$ are the Nusselt number of the flow, thermal conductivity of the fluid and the height of the fins, respectively. $N u$ can be calculated by [49]

$$
\begin{aligned}
&N u=0.664 \mathrm{Re}^{1 / 2} \mathrm{Pr}_{\mathrm{f}}^{1 / 3}, \quad \operatorname{Re}<5 \times 10^{5} \quad (\text { Laminar flow }) \\
&N u=0.037 \mathrm{Re}^{4 / 5} \mathrm{Pr}_{\mathrm{f}}^{1 / 3}, \quad \operatorname{Re} \geq 5 \times 10^{5} \quad (\text { Turbulent flow })
\end{aligned} \tag{38}
$$

where $\operatorname{Pr}_{\mathrm{f}}$ and $R e$ are the Prandtl number of the fluid and the Reynolds number of the flow, respectively. They can be calculated by

$$
\operatorname{Pr}_{\mathrm{f}}=\frac{v_{\mathrm{f}}}{a_{\mathrm{f}}}=\frac{c_{\mathrm{pf}} \varphi_{\mathrm{f}}}{k_{\mathrm{f}}} \tag{39}
$$

$$
\operatorname{Re}=v_{\mathrm{f}} H_{\mathrm{f}} / v_{\mathrm{f}} \tag{40}
$$

where $v_{\mathrm{f}}$, $a_{\mathrm{f}}$, $c_{\mathrm{pf}}$, $k_{\mathrm{f}}$, $\varphi_{\mathrm{f}}$, $\rho_{\mathrm{f}}$ and $v_{\mathrm{f}}$ are the Kinematic viscosity, thermal diffusivity, constant pressure heat capacity ratio, thermal conductivity, kinetic velocity, density and the viscosity of the fluid, respectively. The effective heat transfer area is given by [47]

$$
A_{\mathrm{eff}}=\eta_{\mathrm{f}}\left(2 N_{\mathrm{f}} L_{\mathrm{f}} H_{\mathrm{f}}\right)+\left(N_{\mathrm{f}}-1\right) \delta_{\mathrm{c}} L_{\mathrm{f}} \tag{41}
$$

where the fin efficiency $\eta_{\mathrm{f}}$ is given by

$$
\eta_{\mathrm{f}}=\frac{\tanh \left(m H_{\mathrm{f}}\right)}{m H_{\mathrm{f}}} \tag{42}
$$

where

$$
m=\sqrt{\frac{2 h_{\mathrm{cv}}\left(\delta_{\mathrm{f}}+L_{\mathrm{f}}\right)}{k_{\mathrm{f}} \delta_{\mathrm{f}} L_{\mathrm{f}}}} \tag{43}
$$

To describe the geometry of the thermoelectric module air gap, a ratio is introduced from Ref. [13] and defined as module packed density $\theta$

$$
\theta=2 A N / A_{\mathrm{cp}} \tag{44}
$$

The electrical resistance of a conducting strip is given as follows

$$
R_{\mathrm{Cu}}=\frac{1}{\sigma_{\mathrm{cu}}} \frac{L_{\mathrm{Cu}}}{\delta_{\mathrm{cu}} L_{\mathrm{b}}}=\frac{1}{\sigma_{\mathrm{cu}}} \frac{2 L_{\mathrm{a}}+L_{\mathrm{a}}(1-\theta) / \theta}{\delta_{\mathrm{cu}} L_{\mathrm{b}}}=\frac{1}{\sigma_{\mathrm{cu}}} \frac{1+1 / \theta}{\delta_{\mathrm{cu}}} \tag{45}
$$

where $\sigma_{\mathrm{cu}}$ and $\delta_{\mathrm{cu}}$ are the electrical conductivity and thickness of the conducting strip, respectively.

The air gap of the module can be considered as a restricted horizontal interlayer. There are two cases: when the underside is cold side, the heat transfer is heat conduction; when the underside is hot side, the heat transfer mode is dependent on the $Ra$ number (the product of $Gr$ and $Pr$) which is given by [47]

$$
R a=\frac{g \beta_{\mathrm{air}} \Delta T L^{3}}{v_{\mathrm{air}}^{2}} \frac{v_{\mathrm{air}}}{a_{\mathrm{air}}}=\frac{g \beta_{\mathrm{air}} \Delta T L^{3}}{a_{\mathrm{air}} v_{\mathrm{air}}} \tag{46}
$$

where $\beta_{\mathrm{air}}$, $a_{\mathrm{air}}$, $v_{\mathrm{air}}$ and $g$ are the coefficient of cubical expansion, thermal diffusivity and kinematic viscosity of air, and gravitational acceleration, respectively.

(1) When $Ra<1700$, the heat transfer is heat conduction and then the thermal resistance is

$$
R_{\mathrm{cdg}}=\frac{L}{A_{\mathrm{g}} k_{\mathrm{air}}}=\frac{L}{A_{\mathrm{cp}} k_{\mathrm{air}}(1-\theta)} \tag{47}
$$

(2) When $Ra \geq 1700$, the heat conduction develops to natural convection and then the thermal resistance is

$$
R_{\mathrm{cvg}}=\frac{1}{h_{\mathrm{cvg}} A_{\mathrm{g}}} \tag{48}
$$

where

$$
h_{\mathrm{cvg}}=N u k_{\mathrm{air}} / L \tag{49}
$$

$$
\begin{aligned}
&N u=0.59 R a^{0.4}, \quad 1.7 \times 10^{3} \leq R a<7.0 \times 10^{3} \\
&N u=0.212 R a^{1 / 4}, \quad 7.0 \times 10^{3} \leq R a<3.2 \times 10^{5} \\
&N u=0.061 R a^{1 / 3}, \quad R a \geq 3.2 \times 10^{5}
\end{aligned} \tag{50}
$$

The radiative heat flow rate between two parallel plates with same area is given by

$$
Q_{\mathrm{rd}}=A_{\mathrm{rd}} \frac{\sigma_{\mathrm{b}}\left(T_{1}^{4}-T_{2}^{4}\right)}{1 / \epsilon_{1}+1 / \epsilon_{2}-1}=\frac{T_{1}^{4}-T_{2}^{4}}{R_{\mathrm{rdg}}} \tag{51}
$$

where $\epsilon_{1}$, $\epsilon_{2}$, $T_{1}$, $T_{2}$ and $A_{\mathrm{rd}}$ are the blackness, temperature and area of the two plates, respectively. $\sigma_{\mathrm{b}}$ is the Stefan-Boltzmann constant. So one can derive the radiative thermal resistance of the air gap as follows

$$
R_{\mathrm{rdg}}=\frac{1 / \epsilon_{\mathrm{cp}}+1 / \epsilon_{\mathrm{cp}}-1}{\sigma_{\mathrm{b}} A_{\mathrm{g}}}=\frac{2 / \epsilon_{\mathrm{cp}}-1}{\sigma_{\mathrm{b}} A_{\mathrm{cp}}(1-\theta)} \tag{52}
$$

where $\epsilon_{\mathrm{cp}}$ is the blackness of the ceramic plates.

<table>
<caption>Table 1: Geometric dimensions of the thermoelectric module [51].</caption>
<thead>
<tr>
<th>$A$ (mm²)</th>
<th>$L$ (mm)</th>
<th>$\delta_{\mathrm{cu}}$ (mm)</th>
<th>$\delta_{\mathrm{cp}}$ (mm)</th>
<th>$A_{\mathrm{cp}}$ (mm²)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1.9</td>
<td>0.2</td>
<td>0.9</td>
<td>$29.7\times29.7$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2
Physical properties of conducting strip, ceramic plate, and heat exchangers [52].</caption>
<thead>
<tr>
<th>$\rho_{\text{cu}}$ ($\Omega$m)</th>
<th>$k_{\text{cu}}$ ($\text{W m}^{-1}\text{K}^{-1}$)</th>
<th>$k_{\text{cp}}$ ($\text{W m}^{-1}\text{K}^{-1}$)</th>
<th>$\epsilon_{\text{cp}}$</th>
<th>$k_{\text{Al}}$ ($\text{W m}^{-1}\text{K}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1.7\times10^{-8}$</td>
<td>386</td>
<td>35.3</td>
<td>0.9</td>
<td>204</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4
Parameters of air [48].</caption>
<thead>
<tr>
<th>$k_{\text{air}}$ ($\text{W m}^{-1}\text{K}^{-1}$)</th>
<th>$Pr_{\text{air}}$</th>
<th>$\beta_{\text{air}}$ ($\text{K}^{-1}$)</th>
<th>$\varphi_{\text{air}}$ ($\text{kg m}^{-1}\text{s}^{-1}$)</th>
<th>$v_{\text{air}}$ ($\text{m}^{2}\text{s}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$2.57\times10^{-2}$</td>
<td>0.713</td>
<td>$3.43\times10^{-3}$</td>
<td>$1.82\times10^{-5}$</td>
<td>$1.52\times10^{-5}$</td>
</tr>
</tbody>
</table>

## 4. Simulation and comparison

The characteristic of the thermoelectric generator, including voltage output, power output, efficiency, entropy production rate, temperature and heat flow rate features is investigated by numerical simulation. Water represents a growing concern for meeting future power generation, especially thermoelectric power generation needs [50]. Almost all of the energy can be absorbed by the water to convert to available energy. So hot water at 60–100 °C and cold water at 27 °C (room temperature) are employed as heat source and sink of the generator. A typical commercial thermoelectric generator made by Ferrotec (China) [51] (8001/127/040B) which consists of 127 thermoelectric elements is chosen for this simulation. The simulation results can be used for reference by employing low-grade energy or waste heat for power generation.

The physical properties of the commercially available material by Melcor [52] used for this simulation are shown as follows

$$
\alpha_{\mathrm{p}}=\left(22224.0+930.6 T-0.9905 T^{2}\right) 10^{-9} \mathrm{~V} \mathrm{~K}^{-1} \quad(53)
$$

$$
\rho=\left(5112.0+163.4 T+0.6279 T^{2}\right) 10^{-10} \Omega \mathrm{m} \quad(54)
$$

$$
k=\left(62605.0-277.7 T+0.4131 T^{2}\right) 10^{-4} \mathrm{Wm}^{-1} \mathrm{~K}^{-1} \quad(55)
$$

where $\alpha_{\mathrm{p}}$, $\rho$ and $k$ are the Seebeck coefficient, electrical resistivity and thermal conductivity, respectively. $T=(T_{\mathrm{h}}+T_{\mathrm{c}})/2$ is the mean temperature of the hot and cold junction.

The geometric dimensions of the thermoelectric module are shown in Table 1 [51]. The physical properties of the conducting strip, ceramic plate and heat exchanger are shown in Table 2 [52]. The geometric dimensions of heat exchangers are shown in Table 3 [47]. The physical properties and flow parameters of air and water [48] are shown in Tables 4 and 5, respectively.

Fig. 7 shows the temperature difference between the hot and cold junction $\Delta T_{\mathrm{hc}}=T_{\mathrm{h}}-T_{\mathrm{c}}$ versus electrical current output. It can be seen that the temperature difference is linear and decreasing function of the electrical current output. Actually, the linear relationship is approximate because there are factors (such as heat convections and radiative heat transfer) which caused nonlinearity. However, they affected the linearity little. The temperature difference is affected by the electrical current output little, but affected by the hot water temperature strongly.

Fig. 8 shows the voltage output versus electrical current output. The curves plotted by dotted lines in this figure (and following Figures) are calculated based on the exo-reversible model, i.e., all the external irreversibilities are neglected. It can be seen that the output voltages are linear and decreasing functions of the electrical current output. The slopes of the curves are the same. That is for any output current, the external irreversibilities decrease the output voltage with a same value 10% and the heat reservoir temperature difference does not affect the slopes of the curves. Specially, when the hot water temperature is 100 °C, the open circuit voltage $U_{\text{open}}=1.80\ \text{V}$ ($I=0$) and the short circuit current $I_{\text{short}}=0.28\ \text{A}$ ($U=0$).

Fig. 9(a) and (b) shows the power output and efficiency versus electrical current output, respectively. It can be seen that $P$–$I$ and $\eta$–$I$ curves, in Fig. 9(a) and (b), are both parabolic-like, which means there is one optimal current output $I^{P}$ corresponding to the maximum power output $P_{\text{max}}$ and another optimal current output $I^{\eta}$ corresponding to the maximum efficiency $\eta_{\text{max}}$. The external irreversibilities decrease power output and efficiency by 17% and 5%, respectively. When the hot water temperature increases, the maximum power and maximum efficiency along with the corresponding optimal currents increase. When the hot water temperature is 100 °C, the maximum power output of 0.13 W and the maximum efficiency of 0.87% are available from the generator.

Fig. 10 shows the entropy production rate versus electrical current output. It can be seen that the entropy production rate is increasing function of the electrical current output. When $I\rightarrow0$, the entropy production rate tends to the minimum. The reason is that the entropy production rate by the Joule heat tends to zero, all the entropy production is generated by inner and external heat transfer which can be expressed by $S_{\text{g},I=0}=Q_{\text{H}}(1/T_{\text{L}}-1/T_{\text{H}})=Q_{\text{L}}(1/T_{\text{L}}-1/T_{\text{H}})$. It should be noted that the external irreversibilities decrease the entropy production rate for fixed electrical current output. On the one hand, the external irreversibilities cause external entropy production but the lower temperature difference between the hot and cold junction of the thermoelectric elements decreases the inner entropy production rate. On the other hand, the external irreversibilities decrease the rate of heat transfer from the heat source to the heat sink. When the external thermal resistance tends to infinite, the rate of heat transfer and then the entropy production rate tends to zero. Certainly, the decrease of entropy production rate is at a cost of the decrease of power output and efficiency. On the whole, the entropy generation minimization is not suitable for the electrical current optimization of a thermoelectric generator. Only power and efficiency maximization are useful and possible in this case.

Fig. 11(a) and (b) shows the surface temperatures versus electrical current output. It can be seen that all the hot side temperatures decrease while all the cold side temperatures increase with the increase in the electrical current output. So the temperature difference between the hot and cold junctions decreases (Fig. 7). Comparing the temperature difference caused by different parts, the following equation holds: $\Delta T_{\text{Cv}}>\Delta T_{\text{Cp}}>\Delta T_{\text{Exb}}>\Delta T_{\text{Cu}}$, where $\Delta T_{\text{Cv}}$, $\Delta T_{\text{Cp}}$, $\Delta T_{\text{Exb}}$ and $\Delta T_{\text{Cu}}$ are the temperature differences caused by the fins heat convection, ceramic plate, heat exchanger base and conducting strips, respectively. The temperature differences reflect the different effect of the thermal resistance on the performance of the device.

<table>
<caption>Table 3
Geometric dimensions of heat exchangers [47].</caption>
<thead>
<tr>
<th>$A_{\text{b}}$ ($\text{mm}^{2}$)</th>
<th>$\delta_{\text{b}}$ (mm)</th>
<th>$\delta_{\text{f}}$ (mm)</th>
<th>$\delta_{\text{c}}$ (mm)</th>
<th>$H_{\text{f}}$ (mm)</th>
<th>$N_{\text{f}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$29.7\times29.7$</td>
<td>4</td>
<td>2.7</td>
<td>2.7</td>
<td>20</td>
<td>6</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5
Parameters of water [48].</caption>
<thead>
<tr>
<th>$k_{\text{water}}$ ($\text{W m}^{-1}\text{K}^{-1}$)</th>
<th>$Pr_{\text{water}}$</th>
<th>$v$ ($\text{m s}^{-1}$)</th>
<th>$T_{\text{H}}$ (°C)</th>
<th>$T_{\text{L}}$ (°C)</th>
<th>$\Delta T$ (°C)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$5.99\times10^{-2}$</td>
<td>7.02</td>
<td>0.5</td>
<td>60–100</td>
<td>27</td>
<td>33–73</td>
</tr>
</tbody>
</table>

![](./images/811666263204954115_7.jpg)

Fig. 7. Temperature difference between the hot and cold junctions versus electrical current output. $T_{H}$ and $T_{L}$ are the temperatures of the hot and cold water, respectively.

Fig. 12(a) and (b) shows the heat flow rates versus electrical current output. It can be seen that the heat flow rates can be classified into two groups according to the quantity of the heat flow rates. Heat flow rates in one group are of large quantity (Fig. 12(a)) and others in another group are of small quantity (Fig. 12(b)). $Q_{H}$, $Q_{L}$, $Q_{h}$, $Q_{c}$, $Q_{j}$, $Q_{\alpha}$ and $Q_{\mu}$ are increasing functions of current output. The inner heat leakage $Q_{K}$ decreases because of the decrease of $\Delta T_{hc}$ (see Fig. 7). It should be noted that the Thomson heat $Q_{\mu}$ is considerable and cannot be neglected. Among the heat flow rates caused by inner effects i.e. the rates of Peltier heat, Fourier heat, Joule heat and Thomson heat, the Fourier heat leakage is the main loss. The inner heat leakage doesn't affect the power output but increase the absorbed heat and then decrease the efficiency. The Seebeck power is a linear function of current output approximately, but the Joule heat is a quadratic function of electrical current output. This is the reason why there is an optimal current corresponding to the maximum power output. The calculation shows that the heat transfer through the air gap is heat conduction and radiative heat transfer because the heat transfer cannot develop to natural convection heat transfer. The narrow space and low temperature difference are the main factors. However, the heat

![](./images/811666263204954115_8.jpg)

Fig. 8. Electrical voltage output versus electrical current output. $T_{H}$ and $T_{L}$ are the temperatures of the hot and cold water, respectively.

![](./images/811666263204954115_9.jpg)

Fig. 9. (a) Power output versus electrical current output. $T_{H}$ and $T_{L}$ are the temperatures of the hot and cold water, respectively. (b) Efficiency versus electrical current output. $T_{H}$ and $T_{L}$ are the temperatures of the hot and cold water.

![](./images/811666263204954115_10.jpg)

Fig. 10. Entropy production rate versus electrical current output. $T_{H}$ and $T_{L}$ are the temperatures of the hot and cold water, respectively.

![](./images/811666263204954115_11.jpg)

Fig. 11. (a) Surface temperatures versus electrical current output. $T_{\text{h}}$, $T_{\text{cpbh}}$, $T_{\text{cpih}}$, $T_{\text{exbh}}$ are thermoelectric element junction temperature, ceramic plate inner and exterior surface temperature, and fins base temperature of the hot side, respectively. $T_{\text{H}}$ and $T_{\text{L}}$ are the temperatures of the hot and cold water, respectively. (b) Surface temperatures versus electrical current output. $T_{\text{c}}$, $T_{\text{cpbc}}$, $T_{\text{cpic}}$, $T_{\text{exbc}}$ are thermoelectric element junction temperature, ceramic plate inner and exterior surface temperature, and fins base temperature of the cold side, respectively. $T_{\text{H}}$ and $T_{\text{L}}$ are the temperatures of the hot and cold water.

![](./images/811666263204954115_12.jpg)

Fig. 12. (a) Heat flow rates versus electrical current output. $Q_{\text{H}}$ is the total absorbed heat rate input to the thermoelectric generator, $Q_{\text{L}}$ is the total rejected heat rate output to the thermoelectric generator, $Q_{\text{h}}$ is the absorbed heat rate input to the thermoelectric elements, $Q_{\text{c}}$ is the rejected heat rate output to the thermoelectric elements, $Q_{\text{K}} = NK(T_{\text{h}} - T_{\text{c}})$ is the inner heat leakage, and $P = Q_{\text{H}} - Q_{\text{L}} = Q_{\text{h}} - Q_{\text{c}}$ is power output. $T_{\text{H}}$ and $T_{\text{L}}$ are the temperatures of the hot and cold water. (b) Heat flow rates versus electrical current output. $Q_{\alpha} = N\alpha I(T_{\text{h}} - T_{\text{c}})$ is the Seebeck power rate, $Q_{\text{J}} = NI^{2}R$ is the Joule heat rate, $Q_{\mu} = N\mu I(T_{\text{h}} - T_{\text{c}})$ is the Thomson heat rate, and $P = Q_{\alpha} - Q_{\text{J}} - Q_{\mu}$ is power output, respectively. $Q_{\text{g}} = Q_{\text{cvg}} + Q_{\text{rdg}}$ is the heat flow rate through the air gap, where $Q_{\text{cvg}}$ and $Q_{\text{rdg}}$ represent the heat conduction rate and heat radiative rate, respectively. $T_{\text{H}}$ and $T_{\text{L}}$ are the temperatures of the hot and cold water, respectively.

flow rate through the air gap $Q_{\text{g}}$ is considerable and even larger than the power output generally. The heat flow rate through the air gap decreases with the increase in electrical current output because of the decrease of $\Delta T_{\text{hc}}$ (Fig. 7).

## 5. Conclusions
A complete numerical model with inner and external multi-irreversibilities of commercial thermoelectric generator with finned heat exchangers is established, in which physical properties, geometric dimensions, and flow parameters are all considered.

Applying the numerical model to a typical commercial thermoelectric generator, the characteristic of the thermoelectric generator is simulated. Hot water at 60–100 °C and cold water at 27 °C (room temperature) are employed as heat source and sink of the generator. It is found that

(1) The temperature difference between the junctions and voltage output is a linear function of the electrical current output approximately. $P$–$I$ and $\eta$–$I$ curves are both parabolic-like. When the hot water temperature is 100 °C, the open circuit voltage is 1.80 V, the short circuit current is 0.28 A, the maximum power output is 0.13 W and the maximum efficiency is 0.87%, respectively. The entropy generation minimization is not suitable for the electrical current optimization of a thermoelectric generator.

(2) The Fourier heat leakage is the main loss among the losses caused by inner effects. The heat transfer through the air gap is heat conduction and radiative heat transfer. The heat flow through the air gap and Thomson heat is considerable and even larger than the power output generally. Sorting by the quantity of effect on the performance of the device, the maximum is the thermal resistance of the heat convection between the heat exchanger and the fluid, followed by the heat leakage through the air gap, ceramic plates, and thermal resistance of the heat exchanger base, the minimums are the thermal and electrical resistance of the conducting strips.

The numerical model and calculation method may be applied to the prediction and optimization study of thermoelectric generator with finned heat exchangers. The simulation results obtained herein along with the researches by Astrain et al. [45] (studied the thermal resistances of heat exchangers specially) and Hsiao et al. [46] (employed waste heat of gas as heat source for thermoelectric power generation) can be used for reference by employing low-grade energy or waste heat for power generation.

### Acknowledgements

This paper is supported by the National Natural Science Foun- dation of P. R. China (Project No. 10905093), Program for New Century Excellent Talents in University of P. R. China (Project No. NCET-04-1006) and the Foundation for the Author of National Excellent Doctoral Dissertation of P. R. China (Project No. 200136). The authors wish to thank the reviewers for their careful, unbiased and constructive suggestions, which led to this revised manuscript.

### References

[1] Rowe DM. CRC handbook of thermoelectrics. 1st ed. Boca Raton: CRC Press; 1995.
[2] Thomas JP, Qidwai MA, Kellogg JC. Energy scavenging for small-scale unmanned systems. J Power Sources 2006;159(2):1494-509.
[3] Rowe DM. Thermoelectrics handbook: macro to nano. Boca Raton: CRC Press; 2005.
[4] Whalen SA, Applett CA, Aselage TL. Improving power density and efficiency of miniature radioisotopic thermoelectric generators. J Power Sources 2008; 180(1):657-63.
[5] Poudel B, Hao Q, Ma Y, Lan Y, Minnich A, Yu B, et al. High-thermoelectric performance of nanostructured bismuth antimony telluride bulk alloys. Science 2008;320(5876):634-8.
[6] Heremans JP, Jovovic V, Toberer ES, Saramat A, Kurosaki K, Charoenphakdee A, et al. Enhancement of thermoelectric efficiency in PbTe by distortion of the electronic density of states. Science 2008;321(5888):554-7.
[7] Bell LE. Cooling, heating, generating power, and recovering waste heat with thermoelectric systems. Science 2008;321(5895):1457-61.
[8] Riffat SB, Ma X. Thermoelectrics: a review of present and potential applica- tions. Appl Thermal Eng 2003;23(8):913-35.
[9] Bejan A. Advanced engineering thermodynamics. New York: Wiley; 1988.
[10] Angrist SW. Direct energy conversion. 4th ed. Boston: Allyn and Bacon; 1992.
[11] Bejan A. Advanced engineering thermodynamics. 3rd ed. Hoboken, NJ: John Wiley & Sons; 2006.
[12] Min G, Rowe DM. Optimisation of thermoelectric module geometry for 'waste heat' electric power generation. J Power Sources 1992;38(3):253-9.
[13] Rowe DM, Min G. Evaluation of thermoelectric modules for power generation. J Power Sources 1998;73(2):193-8.
[14] Rowe DM. A high performance solar powered thermoelectric generator. Appl Energy 1981;8(4):269-73.
[15] Rowe DM. Applications of nuclear-powered thermoelectric generators in space. Appl Energy 1991;40(4):241-71.
[16] Sisman A, Yavuz H. The effect of Joule losses on the total efficiency of a ther- moelectric power-cycle. Energy, The Int J 1995;20(6):573-6.
[17] Chen J, Yan Z, Wu L. The influence of Thomson effect on the maximum power output and maximum efficiency of a thermoelectric generator. J Appl Phys 1996;79(11):8823-8.
[18] Xuan XC, Ng KC, Yap C, Chua HT. A general model for studying effects of interface layers on thermoelectric devices performance. Int J Heat Mass Transfer 2002;45(26):5159-70.
[19] Yamanashi M. A new approach to optimum design in thermoelectric cooling systems. J Appl Phys 1996;80(9):5494-502.
[20] Crane DT, Jackson GS. Optimization of cross flow heat exchangers for thermo- electric waste heat recovery. Energy Convers Manage 2004;45(6):1565-82.

[21] Chen L, Li J, Sun F, Wu C. Effect of heat transfer on the performance of two- stage semiconductor thermoelectric refrigerators. J Appl Phys 2005;98(3):34507.
[22] Bejan A. General criterion for rating heat-exchanger performance. Int J Heat Mass Transfer 1978;21(5):655-8.
[23] De Vos A. Efficiency of some heat engines at maximum-power conditions. Am J Phys 1985;53(6):570-3.
[24] Chen L, Sun F, Chen W. Optimization of the specific rate of refrigeration in combined refrigeration cycles. Energy, The Int J 1995;20(10):1049-53.
[25] Wu C, Chen L, Sun F. Effect of heat transfer law on finite time exergoeconomic performance of heat engines. Energy, The Int J 1996;21(12):1127-34.
[26] Hoffmann KH, Burzler JM, Schubert S. Endoreversible thermodynamics. J Non- Equilibr Thermodyn 1997;22(4):311-55.
[27] Chen L, Sun F. Advances in finite time thermodynamics: analysis and opti- mization. New York: Nova Science Publishers; 2004.
[28] Kolenda Z, Donizak J, Hubert J. On the minimum entropy production in steady state heat conduction processes. Energy, The Int J 2004;29(12-15):2441-60.
[29] Bonjour J, Bejan A. Optimal distribution of cooling during gas compression. Energy 2006;31(4):409-24.
[30] Sieniutycz S, Jezowski J. Energy optimization in process systems. Oxford: Elsevier; 2009.
[31] Xia S, Chen L, Sun F. Power-optimization of non-ideal energy converters under generalized convective heat transfer law via Hamilton-Jacobi-Bellman theory. Energy 2011;36(1):633-46.
[32] Gordon JM. Generalized power versus efficiency characteristics of heat engines: the thermoelectric generator as an instructive illustration. Am J Phys 1991;59(6):551-5.
[33] Wu C. Analysis of waste-heat thermoelectric power generators. Appl Thermal Eng 1996;16(1):63-9.
[34] Agrawal DC, Menon VJ. The thermoelectric generator as an endorevesible Carnot engine. J Phys D: Appl Phys 1997;30(2):357-9.
[35] Chen J, Andresen B. New bounds on the performance parameters of a ther- moelectric generator. Int J Power Energy Syst 1997;17(1):23-7.
[36] Chen J, Wu C. Analysis on the performance of a thermoelectric generator. Trans ASME, J Energy Res Technol 2000;122(2):61-3.
[37] Nuwayhid RY, Moukalled F. Evolution of power and entropy in a temperature gap system with electric and thermoelectric influences. Energy Convers Manage 2003;44(5):647-65.
[38] Nuwayhid RY, Shihadeh A, Ghaddar N. Development and testing of a domestic woodstove thermoelectric generator with natural convection cooling. Energy Convers Manage 2005;46(7):1631-43.
[39] Esarte J, Min G, Rowe DM. Modelling heat exchangers for thermoelectric generators. J Power Sources 2001;93:72-6.
[40] Chen L, Gong J, Sun F, Wu C. Effect of heat transfer on the performance of thermoelectric generators. Int J Thermal Sci 2002;41(1):95-9.
[41] Chen L, Li J, Sun F, Wu C. Performance optimization of a two-stage semi- conductor thermoelectric-generator. Appl Energy 2005;82(4):300-12.
[42] Yu J, Zhao H. A numerical model for thermoelectric generator with the parallel-plate heat exchanger. J Power Sources 2007;172(1):428-34.
[43] Niu X, Yu J, Wang S. Experimental study on low-temperature waste heat thermoelectric generator. J Power Sources 2009;188(2):621-6.
[44] Behrens DA, Lee IC, Waits CM. Catalytic combustion of alcohols for micro- burner applications. J Power Sources 2010;326(1):11-26.
[45] Astrain D, Vian JG, MartCnez A, RodCguez A. Study of the influence of heat exchangers' thermal resistances on a thermoelectric generation system. Energy 2010;35(2):602-10.
[46] Hsiao YY, Chang WC, Chen SL. A mathematic model of thermoelectric module with applications on waste heat recovery from automobile engine. Energy 2010;35(3):1447-54.
[47] Cengel YA. Heat transfer: a practical approach. New York: McGraw-Hill;1998.
[48] Bejan A. Convection heat transfer. 3th ed. New York: John Wiley & Sons; 2004.
[49] Incropera F, Witt DD. Fundamentals of heat and mass transfer. 6th ed. New York: Wiley; 2007.
[50] Thomas J, Feeley I, Timothy J, Skone A, Gary J. Water: a critical resource in the thermoelectric power industry. Energy 2008;33(1):1-11.
[51] Ferrotec. 2010. Available from: http://www.Ferrotec.com.cn.
[52] Melcor. Thermoelectric handbook. Available from: http://www.Laridtech. com; 2010.
