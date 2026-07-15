IOP Conference Series: Materials Science and Engineering

PAPER • OPEN ACCESS

# Investigation of cryogenic mixed-refrigerant cooled current leads in combination with peltier elements

To cite this article: E Shabagin *et al* 2020 *IOP Conf. Ser.: Mater. Sci. Eng.* **755** 012138

View the [article online](article online) for updates and enhancements.

This content was downloaded from IP address 64.119.200.11 on 04/11/2020 at 15:25

# Investigation of cryogenic mixed-refrigerant cooled current leads in combination with peltier elements

E Shabagin¹, K Raczka¹, S Grohmann¹,²

¹ Karlsruhe Institute of Technology (KIT), Institute of Technical Physics,
Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany
² Karlsruhe Institute of Technology, Institute of Thermodynamics and Refrigeration,
Engler-Bunte-Ring 21, 76131 Karlsruhe, Germany

E-mail: eugen.shabagin@kit.edu

**Abstract.** Current leads supply electrical energy from a room-temperature power supply to a superconducting application, representing thus a major thermal load. State-of-the-art cooling solutions use either open (vapor cooled) or multi-stage closed cycle systems. The multi-stage concept can be integrated in one cryogenic mixed refrigerant cycle (CMRC), where a wide-boiling fluid mixture absorbs the heat load continuously along the current lead. In this paper, we study the combination of CMRC cooling with Peltier elements at the warm end of DC current leads. The Peltier cooling may cause a temperature drop on the order of 80 K. This allows an optimization of the CMRC mixture composition towards lower temperatures, avoiding the use of high-boilers that risk to freeze out at low temperatures. Our studies suggest that Peltier and CMRC cooling can reduce the thermal load at the cold end by 30 to 45% compared to conventional conduction-cooled current leads.

## 1. Introduction

In superconducting direct current (DC) applications, current leads represent the major thermal load into the cryogenic system. The main contributions to the thermal load are the ohmic heating $\dot{Q}_{\rm el}$ and the heat conduction $\dot{Q}_{\lambda}$ from the warm terminal to the cold end. In an optimized current lead, the overall thermal load is minimized by selecting an appropriate geometry to reduce the heat input from the warm terminal to zero, yielding an adiabatic boundary condition [1]. Independent on the cooling method (i.e. conduction- or gas-cooled), the adiabatic boundary condition is usually aimed for in the design of current leads. This work refers to high-temperature superconducting (HTS) systems working at 78 K.

Optimized conduction-cooled current leads [1] are used in cryogen-free cryostat systems, working with one cold stage and yielding the highest heat leak $(42.5\,\rm W\,kA^{-1})$ compared to other cooling options. Forced flow nitrogen gas-cooled current leads [2–4] reduce the heat leak down to $18.2\,\rm W\,kA^{-1}$ [4] due to convective cooling, where the coolant is heated up in counter-flow to room-temperature in an open cycle system. Low heat leaks in a closed cycle system can be achieved by the application of several cooling stages [5–8] at intermediate temperatures (multi-stage cooled current lead). In [8], for example, a heat leak of $22.4\,\rm W\,kA^{-1}$ is reported using four individual cooling stages.

Another closed cycle system is the combination of the recuperative heat exchanger of a closed Joule-Thomson cycle working with a mixed refrigerant (cryogenic mixed-refrigerant cooled

![](./images/812594495622217735_1.jpg)
Content from this work may be used under the terms of the *Creative Commons Attribution 3.0 licence*. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd

![](./images/812594495622217735_2.jpg)

Figure 1. Concept of a 10 kA cryogenic mixed-refrigerant cooled current lead in combination with Peltier elements at the warm end. The middle part of the current lead (CuI), shown in (a) and (b), is connected with the heat exchanger of the pre-cooled Joule-Thomson cycle and is cooled with the LP stream of the mixed refrigerant. The lower part of the current lead is not connected to the mixture and is cooled with a cryocooler to 78 K.

current lead). The use of a mixed (rather than a pure) refrigerant is an advantageous cooling method for current leads [9-11] due to the thermodynamic benefit of absorbing heat over a broad temperature range [9-15]. Combinations of the cooling methods [4], the use of Peltier elements (PCL) [16-18] and the integration of high temperature superconductors [19] are further possibilities to reduce the heat leak.

In this paper, we present a model for Peltier current leads cooled with a cryogenic mixed-refrigerant cycle (CMRC). The system concept is introduced in section 2, followed by the overall current lead design and integration in section 3. The numerical model of the current lead design is explained in section 4. Example calculations for 10 kA Peltier current leads cooled with a cryogenic mixed-refrigerant cycle and a pre-cooling stage are presented in section 5 and discussed in comparison to other technical options. Main conclusions are summarized in section 6.

### 2. System concept
The system concept of Peltier current leads cooled with a CMRC and a pre-cooling stage is shown in figure 1. At the room temperature terminal, Peltier elements ($\text{Bi}_2\text{Te}_3$) are inserted in the cooper current lead for an additional thermoelectric cooling effect, the so-called Peltier effect.

When electrical current is applied, a heat flux in the junctions between $\text{Cu}$ and $\text{Bi}_2\text{Te}_3$ is created, yielding a temperature drop from room temperature to about 230 K on the cold side and a thermal load on the warm side. This thermal load has to be removed with a water cooling system outside the cryostat to maintain the temperature at the warm end of the current lead. When no current is flowing, the thermoelectric cooling effect is zero, but due to the low thermal conductivity of $\text{Bi}_2\text{Te}_3$ of about 0.4% of cooper, the thermal load on the cold end of the current

lead is also reduced effectively.

The pre-cooling stage in the Joule-Thomson cycle is necessary to cool down the CMRC high-pressure (HP) stream to the temperature of the cold junction between Cu and $Bi_2Te_3$, in order to avoid a large temperature difference between the lead and the coolant. Using an independent pre-cooling process has the advantage of a larger cooling power of the main cycle with the same compressor [12]. In addition, the pre-cooling stage can be used for the separation of oil at low temperatures, thus improving the system's reliability [12,14,20].

### 3. Current lead design and integration
At the warm end of the current leads, 10 Peltier elements made of $Bi_2Te_3$ are placed in parallel as shown in figure 1a and 1b. The Peltier elements are designed for a current of $I_{PE}=1$ kA each, yielding a diameter of $d_{PE}=45$ mm and a length of $L_{PE}=7$ mm.

Below the Peltier elements, the upper part of the current leads is connected to the counter-flow heat exchanger (CFHX) of the CMRC. It has a length of $L_{CuI}=0.58$ m and a cross-sectional area of $A_{CuI}=2.0\times10^{-3}$ m$^2$. The low-pressure (LP) stream in the cycle cools the HP stream as well as the current leads continuously over the temperature range from 244 K to about 130 K with a mass flow of $3$ g s$^{-1}$. The lower part, which is $L_{CuII}=0.4$ m long with a cross-sectional area of $A_{CuII}=3.0\times10^{-3}$ m$^2$, is not yet cooled by the mixture, as appropriate fluid property data are still under investigation (cf. [21]). Therefore, it is modelled with a cryocooler that is stabilized at 78 K. The CFHX in the current lead is a $L_{CFHX}=5.5$ m long tubes-in-tube heat exchanger with a total of 7 tubes (1/16'') for the HP stream, which are separated by a spacer. The LP stream is flowing in countercurrent in the free space of the enclosing tube with an inner diameter of $D_i=10$ mm.

Material properties of the Peltier element are the thermal conductivity $\lambda_{PE}=1.7$ W m$^{-1}$ K$^{-1}$, the temperature dependent electrical resistivity $\rho_{PE}(T)=(3.5\times10^{-8}\cdot T-1.5\times10^{-6})$ $\Omega$ m and the Seebeck coefficient $\alpha_{PE}(T)=(3.1\times10^{-7}\cdot T+9.2\times10^{-5})$ V K$^{-1}$ derived from [22,23]. The residual resistance ratio of cooper is RRR= 50 and the material properties are taken from [24].

### 4. Numerical model
The calculation of the temperature profile of the current lead $T_{CL}(x)$ is performed based on three one-dimensional differential heat equations of second order for each part $\mathrm{i}=\{\mathrm{PE,CuI,CuII}\}$ of the current lead:

$$
\frac{\partial}{\partial x} \cdot \left( \lambda_{\mathrm{i}}(T_{\mathrm{i}}) \cdot A_{\mathrm{i}} \cdot \frac{\partial T_{\mathrm{i}}}{\partial x} \right) + I^2 \cdot \frac{\rho_{\mathrm{i}}(T_{\mathrm{i}})}{A_{\mathrm{i}}} - \left[ k_{\mathrm{LP}} \cdot U \cdot (T_{\mathrm{i}} - T_{\mathrm{LP}}) \right]_{\mathrm{i}=2} = 0, \tag{1}
$$

where $\lambda_{\mathrm{i}}$ is the thermal conductivity, $A_{\mathrm{i}}$ the cross-section area, $I$ the amperage, $\rho_{\mathrm{i}}$ the electrical resistivity, $k_{\mathrm{LP}}$ the heat transfer coefficient between the current lead and the low-pressure (LP) stream and $U$ the wetted perimeter. The boundary conditions for the Peltier part ($\mathrm{i}=\mathrm{PE}$) are the fixed temperature at the warm end $\left.T_{\mathrm{PE}}\right|_{x=0}=300$ K due to the water cooling system and

$$
n \cdot \left[ \lambda_{\mathrm{PE}} \cdot A_{\mathrm{PE}} \cdot \frac{\partial T_{\mathrm{PE}}}{\partial x} + \alpha_{\mathrm{PE}} \cdot I_{\mathrm{PE}} \cdot T_{\mathrm{PE}} \right]_{x=L_{\mathrm{PE}}} = \left. \lambda_{\mathrm{CuI}} \cdot A_{\mathrm{CuI}} \cdot \frac{\partial T_{\mathrm{CuI}}}{\partial x} \right|_{x=L_{\mathrm{PE}}} \tag{2}
$$

the boundary condition for the conservation of energy between PE and CuI including the Peltier cooling effect with $n=10$ Peltier elements. The boundary conditions for the upper part of the current lead CuI are the temperature at the junction PE-CuI and the conservation of energy

<table><caption>Table 1. Correlation used in the numerical calculation</caption>
<thead>
  <tr>
    <th>Mechanism</th>
    <th>Correlation</th>
    <th>Mechanism</th>
    <th>Correlation</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Single-phase heat transfer</td>
    <td>Gnielinski [29]</td>
    <td>Two-phase heat transfer</td>
    <td></td>
  </tr>
  <tr>
    <td>Single-phase pressure drop</td>
    <td>Gnielinski [29]</td>
    <td>Mixture boiling</td>
    <td>Sardesai [33]</td>
  </tr>
  <tr>
    <td>Two-phase pressure drop</td>
    <td>Lockhart [30]</td>
    <td>Mixture condensation</td>
    <td>SBG [34,35]</td>
  </tr>
  <tr>
    <td>Void fraction (Separated flow)</td>
    <td>Chrisholm [31]</td>
    <td>Pure boiling</td>
    <td>Liu [36]</td>
  </tr>
  <tr>
    <td>Correction factor $F_\text{c}$ for nucleate boiling</td>
    <td>Thome [32]</td>
    <td>Pure condensation</td>
    <td>Cavallini [37]</td>
  </tr>
</tbody>
</table>

between CuI and CuII:

$$
\left.T_{\text{PE}}\right|_{x=L_{\text{PE}}}=\left.T_{\text{CuI}}\right|_{x=L_{\text{PE}}} \tag{3}
$$

$$
\left.\lambda_{\text{CuI}} \cdot A_{\text{CuI}} \frac{\partial T_{\text{CuI}}}{\partial x}\right|_{x=L_{\text{PE}}+L_{\text{CuI}}}=\left.\lambda_{\text{CuII}} \cdot A_{\text{CuII}} \frac{\partial T_{\text{CuII}}}{\partial x}\right|_{x=L_{\text{PE}}+L_{\text{CuI}}} \tag{4}
$$

For the lower part, the boundary conditions are the temperatures at the junction CuI-CuII and at the cold end with

$$
\left.T_{\text{CuI}}\right|_{x=L_{\text{PE}}+L_{\text{CuI}}}=\left.T_{\text{CuII}}\right|_{x=L_{\text{PE}}+L_{\text{CuI}}} \tag{5}
$$

$$
\left.T_{\text{CuII}}\right|_{x=L_{\text{PE}}+L_{\text{CuI}}+L_{\text{CuII}}}=78\ \text{K}. \tag{6}
$$

The temperature of the LP stream $T_{\text{LP}}$ is found by modelling the heat exchanger with the numerical solution algorithm from [25]. This model takes into account the two-phase heat transfer and pressure drop of the HP and LP streams inside the heat exchanger under consideration of parasitic heat loads, like the ohmic heating of the current lead, and the fluid property variation. The correlation used for the calculation of the heat transfer coefficient $k_{\text{LP}}$ and the pressure drop inside the heat exchanger tubes are shown in table 1. The modelling of the heat exchanger/current lead is done in Mathematica [26]. The explicit Runge-Kutta method is used for the calculation of the temperature change and pressure drop of the HP and LP streams. The three coupled equations (1) to (3) are solved using the explicit midpoint method. Both methods are implemented in a modified iterative calculation loop compared to [25].

For the CMRC circuit, a hydrocarbon mixture of nitrogen, methane, ethane and propane is used with the mass concentrations of 35.9%, 31.9%, 18.2% and 14% respectively. The fluid properties are calculated in Aspen Plus [27] with the Peng-Robinson equation of state [28].

## 5. Numerical results

The temperature profile of the 10 kA current lead as a function of the length is shown in figure 2. The heat load on the warm end of the current lead to be removed by water cooling is 557 W. The Peltier cooling effect (390 W) leads to a temperature drop from room temperature to about 236 K and has a slight lower temperature than the inlet temperature of the HP stream, yielding a heat flow to the current lead. This yields an almost adiabatic boundary condition at the junction between PE and CuI with a heat flow of 27 W only. The electrical power dissipation inside CuI is 286 W, from which 167 W is absorbed by the CMRC LP stream. The minimal temperature difference between the HP and the LP stream is $\Delta T_{\text{min}}=3\ \text{K}$ at the heat exchanger length of 3.5 m (corresponding to $x\approx0.35\ \text{m}$ in figure 2. The temperature of the LP stream at the

![](./images/812594495622217735_3.jpg)

Figure 2. Temperature profile of the CMRC cooled 10 kA current lead with Peltier elements at the warm end (PE). The CuI part is connected to the heat exchanger of the Joule-Thomson cycle, were the HP and LP streams are flowing in the multi-tube-in-tube heat exchanger with a length of 5.5 m. The lower part CuII is connected to a cryocooler at 78 K. For comparison, the temperature profiles of a conventional conduction cooled current lead and of a CMRC cooled current lead (CMRC-CL) without Peltier elements are shown.

cold end and therefore the temperature of the junction CuI-CuII is determined by the Joule-
Thomson effect of throttling the HP stream, controlled by the iterative calculation loop. The fluid temperatures before and after the throttling valve are 135 K and 125 K, respectively. This process takes place inside the two-phase region of the mixture as shown in the $T,h$-diagram in figure 3. With the electrical power dissipation in CuII of 59 W, the heat load at the cold end sums up to 205 W, i.e. $20.5\,\mathrm{W\,kA^{-1}}$. This corresponds to a reduction of the thermal load by 51% compared to a conventional conduction cooled current lead and is lower than the value achieved with a multi-stage cooled current lead [8]. Without electrical current, the heat load yields 140 W, which is also a reduction of about 46% compared to a conventional conduction cooled current lead. In addition, the temperature profile of a cryogenic mixed-refrigerant cooled current lead (CMRC-CL) without Peltier elements is shown in figure 2. It also has an adiabatic boundary at the warm end and is cooled by a mixture with a mass composition of 30% $\mathrm{N_2}$, 20% $\mathrm{CH_4}$, 20% $\mathrm{C_2H_6}$ and 30% $\mathrm{C_3H_8}$. The heat load at the cold end is 310 W, i.e. $31\,\mathrm{W\,kA^{-1}}$.

6. Summary and conclusion
The investigation of cryogenic mixed-refrigerant cooled current leads in combination with Peltier elements is presented in this work. The design current is 10 kA, using 10 $\mathrm{Bi_2Te_3}$ Peltier elements of 1 kA in parallel. This concept yields a reduction of the thermal load at the cold end by 51% down to $20.5\,\mathrm{W\,kA^{-1}}$, compared to conventional single-stage conduction-cooled current leads. The high efficiency, however, comes at the cost of five cooling stages (water, Peltier, pre-cooling,

![](./images/812594495622217735_4.jpg)

Figure 3. $T,h$-diagram of the $\mathrm{N_2}$, $\mathrm{CH_4}$, $\mathrm{C_2H_6}$ and $\mathrm{C_3H_8}$ mixture with mass concentrations of 35.9%, 31.9%, 18.2% and 14%, respectively. The two phase region is confined by the saturated liquid line (left side) and the saturated vapor line (right side). Isobars for the HP stream and for the LP stream are shown. The HP stream enters the CFHX with (19 bar, 244 K), is then throttled from (10 bar, 135 K) to (4 bar, 125 K). The LP stream leaves the CFHX at (3 bar, 240 K).

CMRC and cryocooler) and is therefore not likely to become an economic solution. This conflict may only be solved in the future, if the three systems from pre-cooling to 78 K can be covered by a single CMRC cooling system. Studies on fundamental fluid property data are ongoing in this regard [21].

Typically, the adiabatic boundary at the warm end and the minimum heat load at the cold end are design goals in current lead optimization. These criteria, however, are thermodynamically incorrect, which is illustrated in this work by the non-adiabatic boundary at the warm end. From an energetic point of view, the design goal is the minimum power dissipation, comprising the ohmic power dissipation in the current leads and the power input to the cooling system(s). The latter strongly depends on the thermal integration between current leads and cooling systems and is worst for the conduction cooled solution. From an economic point of view, the technical effort should be minimized. The combined consideration of operating and investment cost yields a minimum in the total cost of ownership.

References
[1] McFee R 1959 Rev. Sci. Instrum. 30 98-102; doi:10.1063/1.1716499.
[2] Chang H M, Choi Y S, Van Sciver S W and Miller J R 2004 AIP Conf. Proc. 710 944-51; doi:10.1063/1.1774775.
[3] Jiahui Z, Juntao T, Ming Q et al. 2010 IEEE Trans. Appl. Supercond. 20 1705-09; doi:10.1109/TASC.2010.2040949.
[4] Yamaguchi S, Emoto M., Yamamoto N et al. 2013 IEEE Trans. Appl. Supercond. 23 4802304; doi:10.1109/TASC.2013.2243896.
[5] Jeong S and Smith J.L 1994 Cryogenics 34 929-33; doi:10.1016/0011-2275(94)90078-7.

[6] Bromberg L, Michael P C , Minervini J V, and Miles C 2010 *AIP Conf. Proc.* **1218** 577-84; doi:10.1063/1.3422405.

[7] Yamaguchi S, Emoto M, Kawahara T et al. 2012 *Physics Procedia* **27** 448-51; doi:10.1016/j.phpro.2012.03.508.

[8] Schreiner F, Gutheil B, Noe M et al. 2017 *IEEE Trans. Appl. Supercond.* **27** 4802405; doi:10.1109/TASC.2017.2655108.

[9] Nellis G F, Pfotenhauer J M and Klein S A 2004 *ASME Int. Mechanical Engineering Congress and Exposition* 339-46; doi:10.1115/IMECE2004-60284.

[10] Pfotenhauer J M, Pettitt J F, Hoch D W and Nellis G F 2006 *Cryocoolers* **14** 443-452.

[11] Shabagin E and Grohmann S 2019 *IOP Conf. Ser.: Mater. Sci. Eng.* **502** 01213; doi.org/10.1088/1757-899X/502/1/012138.

[12] Venkatarathnam G 2008 *Cryogenic mixed refrigerant processes* Int. cryogenics monograph series (New York: Springer).

[13] Alexeev A, Haberstroh Ch and Quack H 2000 *Adv. Cryog. Eng.* **45** 307-314.

[14] Alexeev A, Haberstroh Ch and Quack H 2002 *Cryocoolers* **10** 475-79; doi:10.1007/0-306-47090-X_56.

[15] Kochenburger T M, Grohmann S and Oellrich L R 2015 *Physics Procedia* **67** 227-32; doi:10.1016/j.phpro.2015.06.039.

[16] Yamaguchi S, Takita K and Motojima O 1996 *ICEC/ICMC Proc.* **16** 1159-62.

[17] Okumura H and Yamaguchi S 1997 *IEEE Transactions on Applied Superconductivity* **7** no.2 715-18; doi.org/10.1109/77.614604.

[18] Liu M, Wang Y et al. 2019 *IEEE Transactions on Applied Superconductivity* **29** 4802504; doi.org/10.1109/TASC.2019.2903385.

[19] Chang H M and Van Sciver S W 1998 *Cryogenics* **38** 729-36; doi:10.1016/S0011-2275(98)00043-5.

[20] Alexeev A and Quack H 2000 *Vorrichtung und Verfahren zur Kryolagerung biologischer Stoffe.* German Patent 19922364.

[21] Tamson,J, Stamm M and Grohmann S 2019 *IOP Conf. Ser.: Mat. Sci. and Eng.* **502** 012087; doi.org/10.1088/1757-899x/502/1/012087.

[22] Michael P C, Galea C A and Bromberg L 2015 *IEEE Trans. Appl. Supercond.* **25** 4801805; doi.org/10.1109/TASC.2014.2373512.

[23] Hasegawa Y 2001 *Cryogenics* **41** 495-500; doi.org/10.1016/S0011-2275(02)00048-6.

[24] Cryocomp, Hepak, CRYODATA software, Cryodata Inc. 1999.

[25] Gomse D, Kochenburger T M and Grohmann S 2018 *J. Heat Transfer* **140** 051801; doi:10.1115/1.4038852.

[26] Wolfram Research 2017 Mathematica 11.2.0.0 Wolfram Research Inc. Campaign IL.

[27] Aspen Technology 2017 Aspen plus v10.

[28] Peng D Y and Robinson D B 1976 *Ind. Eng. Chem. Fundamen.* **15** 59-64; doi:10.1021/i160057a011.

[29] VDI, 2010, *VDI Heat Atlas*, 2nd ed., Springer, Berlin.

[30] Lockhart R and Martinelli R 1949 *Chemical Engineering Progress* **45** 39-48.

[31] Chrisholm D 1972 *Equation for Velocity Ratio in Two-Phase Flow - NEL Report* **535**

[32] Thome J R and Shakir S 1987 *AIChE Symp. Ser.* **257** 46-51.

[33] Sardesai R G, Shock R A W and Butterworth D 2007 *Heat Transfer Engineering* **3** 104-14; doi.org/10.1080/01457638108939589.

[34] Silver L 1947 *Trans. Inst. Chem. Eng.* **25**.

[35] Bell K J and Ghaly M A 1973 *AIChE Symposium Series* **69** 72-79.

[36] Liu Z and Winterton R H S 1991 *International Journal of Heat and Mass Transfer* **34** 2759-66; doi.org/10.1016/0017-9310(91)90234-6.

[37] Cavallini A, Del Col D et al. 2006 *Heat Transfer Engineering* **27** 31-38; doi.org/10.1080/01457630600793970.

## Acknowledgments
The authors would like to acknowledge the support from the Karlsruhe School of Elementary Particle and Astroparticle Physics: Science and Technology (KSETA).