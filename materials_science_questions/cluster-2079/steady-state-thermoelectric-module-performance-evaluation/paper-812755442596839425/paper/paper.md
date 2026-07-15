# Improvement of Thermal Environment by Thermoelectric Coolers and Numerical Optimization of Thermal Performance

Ning Wang, Xiao-Chun Li, *Member, IEEE*, and Jun-Fa Mao, *Fellow, IEEE*

Abstract—Seeking for an available thermal runaway solution is becoming one important and challenging issue in current nanometer ICs. Thermoelectric coolers (TECs) may give a solution. In this paper, a simplified power model of circuits closely associated with temperature with and without repeaters is derived. Based on the surface temperature difference and heat-flow density, an equivalent thermal resistance model for powered TECs is proposed. According to the thermal profile model, the steady-state temperature is calculated for the same chip with two different package forms. Finally, optimizations of p-n couples are performed with the purpose of obtaining the maximum coefficient of performance (COP) and minimum TECs power. As compared with the traditional flip-flop controlled-collapse-chip-connection package, the results reveal desirable conclusions that a 15.8% decrease of the chip stability temperature with the COP optimization at $I = 2.5$ A and 11.4% steady-state power savings with the 13.2 W TEC power consumption are obtained in a 50-nm technology node. Analysis demonstrates that the maximum COP and minimum power consumed by TECs can be obtained at different optimum numbers of p-n couples, which is independent of electrical current across by TECs.

Index Terms—Controlled-collapse-chip-connection (C4), Seebeck, thermal runaway, thermal stability, thermoelectric coolers (TECs).

## I. INTRODUCTION

ACCOMPANIED with the constantly scaling CMOS devices, the increasing power density and the continuous rise of operating frequency will lead to a more-and-more serious heat problem for high-performance chips [1]. It has been reported that the peak interconnects temperature can rise up to $210\ {^\circ}\text{C}$ in worse case with a 50-nm technology node [2]. Higher leakage power, faster degradation of the material property, and reliability arise from higher chip temperature [3], which even results in thermal runaway, posting more severe challenge for thermal design of chip packages. Therefore, a proper thermal management solution is of crucial importance to a high-performance chip in order to achieve the satisfactory performance and reliability.

In the aspect of circuits, most dynamic thermal management schemes, such as the clock gating technique, power gating, and sleep transistor insertion techniques, are often implemented in low-power design to alleviate the thermal issue [4]. By decreasing frequency and voltage, even powering OFF some functional units to reduce the on-die junction temperature, a thermal throttling sensor was calibrated to keep the operating temperature within the specified range [5]. However, these techniques were carried out at the cost of extra area, performance, and sensor noise penalty. Therefore, to solve these issues, there is need to exploring an effective thermal management scheme without sacrificing the on-die performance. With substrate integrated with etched microchannel and cavity inside, microchannel fluidic cooler can provide the efficient heat transfer performance. However, the microchannel fluidic cooling has problems of complex machining process, easy blockage, and high cost. Thermoelectric coolers (TECs) in package can pump the electrically generated heat from one side to the other side based on the Peltier effect [6]. As we know, the maximum cooling capability is inversely proportional to the thickness of TECs, so as much as several hundred or even thousand $\text{W/cm}^2$ cooling power density can be attained, as the leg length is small enough [7]. In addition to the good cooling ability, compact size, reduced thermal resistance, silent operation, and high reliability make TECs widely used in electronic, optoelectronic, and bioanalytical devices [8]–[10]. With a thin-film TEC integrated into the package, Chowdhury *et al.* [10], [11] achieved temperature drop of $15\ {^\circ}\text{C}$ at a location where the heat flux reaches up to 1300 $\text{W/cm}^2$. Murphy *et al.* [12] explored semiconductor optical amplifiers packaged with a TEC in avionic applications, and the results indicated TEC were a favorable option for single isolated transmitters. TEC is expected to be applied to nanothermal trumpets that can control the sound information by the thermal process [13]. In addition, TECs were employed for the temperature control of lead-acid batteries and the climate control for electric vehicles [14]. A small number of earlier studies on the effect of parasitic electrical and thermal resistances for TECs are available in [6], [15], and [16].

Manuscript received August 13, 2014; revised May 17, 2015; accepted June 4, 2015. Date of publication June 25, 2015; date of current version July 21, 2015. This work was supported in part by the Shanghai Science and Technology Committee under Grant 13511500900, in part by the Specialized Research Fund for the Doctoral Program of Higher Education under Grant 20120073130003, in part by the Director Fund through the Key Laboratory of Ministry of Education of Design and Electromagnetic Compatibility of High Speed Electronic System under Grant 2014001, and in part by the National Natural Science Foundation of China under Grant 61234001. The review of this paper was arranged by Editor R. Venkatasubramanian.

The authors are with the Key Laboratory of Ministry of Education of Design and Electromagnetic Compatibility of High Speed Electronic System, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: ningw@sjtu.edu.cn; lixc@sjtu.edu.cn; jfmao@sjtu.edu.cn).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TED.2015.2442530

0018-9383 © 2015 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

Many studies investigated TECs transient activity to reveal the thermal dynamics law based on the Peltier effect. Zhang *et al.* [9] presented an analytical method with no need to resort to the thermoelectric parameters and geometric in an iterative procedure, and thermal enhancements are achieved by optimized currents and cooling configurations. Abramzon [17] used a multistart adaptive random search method to determine the optimum number of TECs when the maximized coefficient of performance (COP) of the whole cooling system is obtained. Recently, Cheng *et al.* [18] proposed a 3-D theoretical model for predicting the transient thermal behavior of TECs, which is derived by precisely partitioning p-n pair, and used the model to estimate the transient behavior of the cold and the hot ends in a TEC. Vermeersch *et al.* [19] obtained 2-D maps of the transient surface temperature and constituent Peltier and Joule components over the 50–750 ns time range. However, the most previous theoretical models and experiments are limited to carrying out a numerical analysis to evaluate the performance of the TECs; a few investigations are focused on the estimation of the steady-state temperature considering subthreshold current which is nonlinearly depended on the temperature with TECs integrated packages. Limited reports pay attention to the power dissipation of TECs which is also temperature dependent when improving the figure-of-merit and the cooling ability.

In this paper, analytical expressions of the temperature-dependent power model of circuits are developed to obtain the steady-state temperature based on the thermal profile model. To evaluate the influence of a different package structure on the steady-state temperature of a system, the simplified controlled-collapse-chip-connection (C4) thermal resistance and equivalent thermal resistance models of TECs are derived, respectively. Based on numerical calculations with the proposed equivalent thermal resistance models, COP and power optimizations with p-n couples for TECs are presented. At last, we discuss the temperature drop of two different packages and the relationship between the optimum number of p-n couples and electrical current across by TECs.

## II. POWER CONSUMPTION MODEL

Repeater insertion is a key solution to reduce global interconnects delay and coupled noise from adjacent interconnects in CMOS ICs [20]–[22]. In order to lower propagation delay, a large number of repeaters are inserted in the physical design. However, thermal problems due to the excessive repeater power consumption become increasingly serious especially for the high-performance microprocessor. Subjected to the interconnect resistance and capacitance, the calculation of the repeater power consumption is different with the other circuits. In this paper, the total power dissipation, including the circuit power dissipation without repeater insertion $P_{\text{cwr}}$ and the repeater power consumption $P_{r}$, can be written as

$$
P_{\text{total}} = P_{\text{cwr}} + P_{r}. \tag{1}
$$

It is noted that only when the nMOS and the pMOS work simultaneously in an inverter circuit, the short-circuit power occurs, which is usually ignored due to its small numerical value compared with the dynamic power and leakage power. Therefore, the power dissipation of circuits without repeater insertion can be described as

$$
P_{\text{cwr}} = P_{\text{dynamic}} + P_{\text{leakage}}. \tag{2}
$$

Dynamic power, which is the main contributor for the total power in typical CMOS circuits, is temperature independent unless the frequency is indirectly influenced by temperature [23]. In this paper, we assume that the operating frequency is constant. Then, the dynamic power consumption of circuits is defined as [24]

$$
P_{\text{dynamic}} = NaCV_{\text{dd}}^{2}f \tag{3}
$$

where $a$ is the switching activity factor, $C$ is the average load capacitance per gate, and $N$ is the number of gates in circuits. The leakage power consumption cannot be neglected as technology advances and can be given by

$$
P_{\text{leakage}} = sNW_{\text{min}}I_{\text{sub\_}f}(T)V_{\text{dd}} \tag{4}
$$

where $W_{\text{min}}$ represents the minimized inverter width, $I_{\text{sub\_}f}$ denotes the subthreshold leakage current, which is dependent on temperature, and $s$ is a gate size. The temperature-dependent leakage power exponentially increases with the device scaling. It is reported that every $20\ \mathrm{^\circ C}$ rise in temperature will double the leakage power which is mainly induced by the subthreshold leakage current for nanometer ICs [24]. For a given design with the specific technology process, the temperature-dependent subthreshold leakage current can be simplified into the following polynomial form [23]:

$$
I_{\text{sub\_}f}(T) = I_{\text{sub0}}(k_1T^2 + k_2T + k_3) \tag{5}
$$

where $I_{\text{sub0}}$ is the subthreshold current per-unit width in room temperature, and $k_1$, $k_2$, and $k_3$ are fitting coefficients based on the current technology node.

When the signal frequency is not high enough, the signal response can reach steady state in a period and the effect of interconnect inductance can be omitted [25]. Similar to the circuit power, the repeater power also consists of the dynamic and leakage power consumption shown as follows:

$$
\begin{aligned}
P_{r} = \frac{L_{\text{int}}}{l}\Bigg[&aV_{\text{dd}}^{2}f\big((c_0 + c_p)s + cl\big) \\
&+ sW_{\text{min}}I_{l0}V_{\text{dd}}(c_1T^2 + c_2T + c_3)\Bigg] \tag{6}
\end{aligned}
$$

where $L_{\text{int}}$ is the total interconnect length to be derived by repeaters, $I_{l0}$ is the repeater leakage current per-unit width in room temperature, and $l$ is the interconnect length between two identical repeaters. $c_0$ and $c_p$ are the input and output capacitance of a minimum sized inverter, respectively, $c_1$, $c_2$, and $c_3$ are fitting coefficients of subthreshold current for repeaters, and $c$ is the capacitance per-unit length of interconnects. In order to obtain minimized delay, the optimum size $s_{\text{opt}}$ and interconnect length $l_{\text{opt}}$ are expressed as [26], [27]

$$
s_{\text{opt}} = \sqrt{\frac{r_0C}{rc_0}} \tag{7}
$$

$$
l_{\text{opt}} = \sqrt{\frac{2r_0(c_0 + c_p)}{rc}} \tag{8}
$$

where $r$ is the resistance per-unit length of interconnects, and $r_0$ is the equivalent resistance of the minimum repeater.

## III. THERMAL MODEL

As the feature size in nanometer-scale ICs continues to shrink, the increased power caused by the subthreshold current will contribute to higher temperature, which in turn further increases the circuit power and produces an uncontrolled positive feedback in the end. This process is called thermal runaway which will lead to a destructive thermal environment if not controlled [28]. A proper thermal solution to maintain temperature within its operating limits is significant for the system reliability of high-power processors. Any attempt to operate the processor outside these operating limits may result in permanent damage to the processor and other components within the system. Reducing operation temperature for a proper thermal environment is indispensable to the system performance. Considering the system power and thermal resistance in the dissipated heat path, the junction temperature thermal profile model of die is given by [28]

$$
R_{j a} c_{\mathrm{sys}} \frac{d T_{j}}{d t}+T_{j}=R_{j a} P\left(T_{j}\right)+T_{a}
\tag{9}
$$

where $c_{\text {sys }}$ is the system thermal capacitance, $R_{j a}$ is the thermal resistance between the junction side and the ambient package, $T_{j}$ and $T_{a}$ are the junction temperature and ambient temperature, respectively, $P(T_{j})$ denotes temperature-dependent $P_{\text {total }}$, which can be calculated by (1).

From the power model in Section II, we know that the total power dissipation of a chip is a function of the junction temperature, which presents a positive feedback relationship. On one hand, power will increase as the junction temperature rises. On the other hand, the temperature will keep a rising trend caused by the increasing power consumption. Finally, the chip will reach a steady or divergent state. To obtain the derived formulas of the steady-state junction temperature after electrothermal coupling, we substitute (1) into (9)

$$
R_{j a} c_{\mathrm{sys}} \frac{d T_{j}}{d t}=A T_{j}^{2}+B T_{j}+X
\tag{10}
$$

where

$$
A=R_{j a} s W_{\min } V_{\mathrm{dd}}\left(k_{1} N I_{\mathrm{sub} 0}+c_{1} \frac{L_{\mathrm{int}}}{l} I_{l 0}\right)
\tag{11}
$$

$$
B=R_{j a} s W_{\min } V_{\mathrm{dd}}\left(k_{2} N I_{\mathrm{sub} 0}+c_{2} \frac{L_{\mathrm{int}}}{l} I_{l 0}\right)-1
\tag{12}
$$

$$
\begin{aligned}
X= & R_{j a} a V_{\mathrm{dd}}^{2} f\left(N C+\left(c_{0}+c_{p}\right) s+c l\right) \frac{L_{\mathrm{int}}}{l} \\
& +R_{j a} s W_{\min } V_{\mathrm{dd}}\left(k_{3} N I_{\mathrm{sub} 0}+c_{3} \frac{L_{\mathrm{int}}}{l} I_{l 0}\right)+T_{a}. \quad(13)
\end{aligned}
$$

When the system reaches a steady state, $d T_{j} / d t=0$, the following equation can be obtained:

$$
\begin{aligned}
A T_{j}^{2}+B T_{j}+X & =0 \\
\sqrt{B^{2}-4 A X} & \geq 0.
\end{aligned}
\tag{14}
$$

The term inside the square root has to be positive or zero for real solutions to suppress thermal runaways. In such a case, the solution of (14) can yield two results for the quadratic equation, and the larger one is omitted due to its metastable state which would be alternated by small perturbation [28]. Finally, the steady-state temperature can be obtained

$$
T_{\text {steady_state }}=\frac{-B-\sqrt{B^{2}-4 A X}}{2 A}.
\tag{15}
$$

It is noted that the value of $B$ in (15) is negative and its absolute value is large than the square root in the real calculation process. There is no doubt that the value of $A$ in (15) is positive, thus the final steady-state temperature $T_{\text {steady_state }}$ is also positive.

![](./images/812755442596839425_1.jpg)

Fig. 1. Cross section of flip-chip C4 package with CMOS chips.

## IV. TWO PACKAGE STRUCTURES

### A. Flip-Chip C4 Package

The traditional flip-chip C4 package structure is shown in Fig. 1 [3]. The C4 solder bump distributed over the next layer substrate is soldered and connected to the chip die. While, epoxy commonly used on large high-power chips is underfilled between the die and the substrate. Thermal paste, placed between the aluminum lid and the silicon die to establish good thermal contact, is widely used as thermal interface material and can provide protection to the chips from the mechanical damage [10]. The thermal on the powered die chip is spread quickly to the surrounding Al cap via thermal paste. An air-cooled heat sink is mounted on the Al cap via attached material to efficiently pump the heat to the ambient. Then, the heat produced in the chip die is finally dissipated to the ambient by a heat sink attached on the top of the Al cap.

Due to a small temperature difference between the two sides of Al cap, the thermal resistance of Al cap can be omitted for the first-order analysis [28]. Hence, the total thermal resistance of the C4 structure is given by

$$
R_{j a_{-} \mathrm{C} 4}=R_{\mathrm{TP}}+R_{\mathrm{HS}}
\tag{16}
$$

where $R_{\mathrm{TP}}$ and $R_{\mathrm{HS}}$ represent the thermal resistance of the thermal paste and the heat sink, respectively.

### B. Chip Package With TECs Device

The structure of TECs used for the hot-spot cooling is shown in Fig. 2(a). Many thermocouples consisting of a p-type semiconductor pellet and an n-type semiconductor pellet are connected by Cu interconnects. When the TECs are applied by electrical current from the n-type end to the p-type end, the heat will be absorbed at the bottom of TECs and released

![](./images/812755442596839425_2.jpg)

Fig. 2. Schematic of TECs module. (a) TEC devices chain with electrical current powered ON. (b) Electronic package with the TECs clamped by two thermal pad layers.

at the top side owing to the Peltier effect. If the polarity of power supply is reversed, heat-pumping direction will be changed subsequently. Moreover, due to higher thermal conductance compared with the material surrounding it, a TEC still has the ability of cooling even when there is no electrical current across it [11]. In addition, the localized cooling can be achieved using microelectronic processing for the hot spot of interest [29]. Compared with the C4 package, the key advantages of integrated TECs with a large number of thermocouples are their ability to handle much higher heat fluxes. Fig. 2(b) shows a type of chip package structure with groups of embedded TECs covered by two ceramic plates. Together with the thermal paste, TECs are sandwiched between the cold plate and the heat sink. Here, the cold plate acts as a function of heat conversion not only due to its high thermal conductance but also due to the role of uniformly spreading heat over the underground plate. When the TECs are powered ON, heat is absorbed on the surface of the cold plate and released to the heat sink with thermal paste material as heat conduction medium. According to the dimensions, thermal resistance of the cold plate is formulated as follows:

$$
R_{\mathrm{CP}}=\frac{t_{\mathrm{CP}}}{k_{\mathrm{CP}} s_{\mathrm{CP}}} \tag{17}
$$

where $t_{\mathrm{CP}}$ represents the cold plate layer thickness, $k_{\mathrm{CP}}$ and $s_{\mathrm{CP}}$ are the thermal conductivity and area of the plate, respectively.

The cooling power of a TEC at the cold side is given by the following equation [17], [30]:

$$
Q_{\mathrm{cold}}=\alpha I T_{\mathrm{cold}}-\frac{1}{2} I^{2} R_{e}-K\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right) \tag{18}
$$

where $\alpha$ is the Seebeck coefficient, $I$ is the electric current, $R_{e}$ is the electric resistance of a TEC, $K$ is the thermal conductivity of the module, $T_{\text {hot }}$ and $T_{\text {cold }}$ represent the temperature of the hot side and the cold side, respectively. It is noted that the physical properties of the p-type and the n-type semiconductors used in TECs are close to one another apart from the sign of the Seebeck coefficient. For simplicity, the total Seebeck coefficient, $\alpha$, the total electric resistance, $R_{e}$, and the total thermal conductance of the module are calculated in this paper.

The electric voltage applied to the TEC is consumed to overcome the Seebeck effect and the resistive voltage drop

$$
U=I R_{e}+\alpha\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right). \tag{19}
$$

The electrically driven TECs power is

$$
P_{e}=I^{2} R_{e}+\alpha I\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right). \tag{20}
$$

Then, the total heat power generated at the hot side of TEC can be obtained by

$$
Q_{\mathrm{hot}}=Q_{\mathrm{cold}}+P_{e}. \tag{21}
$$

The COP, which is used to estimate the efficient of the TEC module, is expressed as follows:

$$
\mathrm{COP}=\frac{Q_{\mathrm{cold}}}{P_{e}}=\frac{\alpha I T_{\mathrm{cold}}-\frac{1}{2} I^{2} R_{e}-K\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right)}{I^{2} R_{e}+\alpha I\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right)}. \tag{22}
$$

## V. THERMAL RESISTANCE MODEL AND PERFORMANCE OPTIMIZATION FOR TECs

To obtain the steady-state temperature of system with integrated TECs package, it is necessary to calculate the thermal resistances on the cooling path. However, the Peltier effect makes the thermal resistance representation of TECs difficult to realize due to its active characteristic. Moreover, in the pursuit of maximum COP of TECs with optimized p-n couples, TEC's power dissipation is generally neglected, which is consumed by Joule thermal and worked against heat flow difference between the hot and the cold sides. Thus, in this paper, we proposed an equivalent thermal resistance model for TECs based on the surface temperature difference and heat-flow density. In addition, the power consumption cost is considered as the development of a numerical optimization for the COP.

### A. Equivalent Thermal Resistance Model of TECs

The thermal resistance of TECs cannot be calculated as the cold plate, since TEC is an active cooling device playing a role of producing a different temperature difference. Simulta- neously, it can act as cooling power and heat power under the condition of a different current intensity. According to the physical definition of thermal resistance, we proposed an equivalent thermal resistance model for TECs to evaluate the cooling ability of TECs

$$
\begin{aligned}
R_{\mathrm{TECs}} & =\frac{T_{\mathrm{hot}}-T_{\mathrm{cold}}}{Q_{\mathrm{hot}}+Q_{\mathrm{cold}}}=\frac{\Delta T}{2 Q_{\mathrm{cold}}+P_{e}} \\
& =\frac{\Delta T}{\alpha I\left(T_{\mathrm{cold}}+T_{\mathrm{hot}}\right)-2 K\left(T_{\mathrm{hot}}-T_{\mathrm{cold}}\right)}. \tag{23}
\end{aligned}
$$


It is deserved to mention that $R_{\text{TECs}}$ is negative for TECs' cooling ability instead of heating. Although TECs also consume a part of electrical power and produce Joule heat, the cooling ability is dominated on the whole. It can be seen from (23) that $R_{\text{TECs}}$ is a function of $T_{\text{cold}}$ and $T_{\text{hot}}$, where $T_{\text{hot}}$ can be derived as

$$
T_{\mathrm{hot}}=\frac{2 K R_{\mathrm{TECs}}+\alpha I R_{\mathrm{TECs}}+1}{2 K R_{\mathrm{TECs}}+\alpha I R_{\mathrm{TECs}}+1} T_{\mathrm{cold}}. \tag{24}
$$

For a given temperature control criterion $(T_{\text{cold}}, T_{\text{hot}})$ and TEC material $(\alpha, K)$, $R_{\text{TECs}}$ is influenced only by the electrical current passing through TECs devices. Consequently, the thermal resistance from the cold plate to the heat sink is evaluated by

$$
R_{j a_{-} \mathrm{CH}}=R_{\mathrm{CP}}+R_{\mathrm{HS}}+R_{\mathrm{TECs}}+2 R_{\mathrm{TP}}. \tag{25}
$$

### B. Optimization for COP and TECs Power

Now that the p-n couples are electrically connected in series and thermally connected in parallel between the cold plate and the heat sink, determining the optimum number of p-n couples to achieve the maximum thermal performance with smaller electrical power is indispensable. For $N_{\text{pn}}$ p-n couples, the electrical resistance rises by $N_{\text{pn}}$ times with one p-n couple, whereas the equivalent thermal resistance is lower than $N_{\text{pn}}$ times, which means an increase of the thermal conductivity. Therefore, the temperature at the hot side can be rewritten as

$$
T_{\mathrm{hot}}=\frac{2 K R_{\mathrm{TECs}}+\alpha I R_{\mathrm{TECs}}+N_{\mathrm{pn}}}{2 K R_{\mathrm{TECs}}+\alpha I R_{\mathrm{TECs}}+N_{\mathrm{pn}}} T_{\mathrm{cold}}. \tag{26}
$$

Similar to $T_{\text{hot}}$, the power consumed by $N_{\text{pn}}$ couples can be estimated as follows:

$$
P_{N e}=I^{2} N_{\mathrm{pn}} R_{e}+\frac{2 \alpha^{2} I^{2} R_{\mathrm{TECs}}}{2 K R_{\mathrm{TECs}}-\alpha I R_{\mathrm{TECs}}-N_{\mathrm{pn}}} T_{\mathrm{cold}}. \tag{27}
$$

For a given electrical current $I$ and cold side temperature $T_{\text{cold}}$, the power dissipated by p-n couples is a function as $N_{\text{pn}}$. By means of derivation of the (27), the optimum number of p-n couple with minimum TECs power can be found

$$
N_{\mathrm{pn}_{-} P}=\alpha I R_{\mathrm{TECs}}-2 K R_{\mathrm{TECs}}+\alpha \sqrt{\frac{2 R_{\mathrm{TECs}}}{R_{e}} T_{\mathrm{cold}}}. \tag{28}
$$

Substituting (26) and (27) into (22), the expression of COP with p-n multicouples can be provided as (29), shown at the bottom of this page.

Equation (29), can be simplified into the following expression:

$$
\mathrm{COP}=\frac{2 \alpha I T_{\text {cold }}}{2 I^{2} R_{e}\left[N_{\mathrm{pn}}+\frac{2 \alpha^{2} R_{\mathrm{TECs}} T_{\text {cold }}}{R_{e} N_{\mathrm{pn}}}+R_{\mathrm{TECs}}(2 K-\alpha I)\right]}-\frac{1}{2}. \tag{30}
$$

$$
\mathrm{COP}=\frac{-\frac{1}{2} I^{2} R_{e} N_{\mathrm{pn}}^{2}+\left[\alpha I T_{\mathrm{cold}}-\frac{1}{2} I^{2} R_{e} R_{\mathrm{TECs}}(2 K-\alpha I)\right] N_{\mathrm{pn}}-\alpha^{2} I^{2} R_{\mathrm{TECs}} T_{\mathrm{cold}}}{I^{2} R_{e} N_{\mathrm{pn}}^{2}+I^{2} R_{e} R_{\mathrm{TECs}}(2 K-\alpha I) N_{\mathrm{pn}}+2 \alpha^{2} I^{2} R_{\mathrm{TECs}} T_{\mathrm{cold}}} \tag{29}
$$

<table>
<caption>TABLE I Key Reference Data in a 50-nm Technology Node</caption>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Value</th>
    <th>Parameter</th>
    <th>Value</th>
    <th>Parameter</th>
    <th>Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$W$/nm</td>
    <td>500</td>
    <td>$r$/kΩ</td>
    <td>75</td>
    <td>$T_a$/K</td>
    <td>323</td>
  </tr>
  <tr>
    <td>$L$/nm</td>
    <td>20</td>
    <td>$r_0$/kΩ</td>
    <td>13.4</td>
    <td>$T_0$/K</td>
    <td>300</td>
  </tr>
  <tr>
    <td>$V_{dd}$/$V$</td>
    <td>1</td>
    <td>$c_{sys}$/pF</td>
    <td>185</td>
    <td>$R_{cp}$/K·W⁻¹</td>
    <td>0.085</td>
  </tr>
  <tr>
    <td>$f$/GHz</td>
    <td>5.49</td>
    <td>$c_0$/fF</td>
    <td>0.93</td>
    <td>$R_{pd}$/K·W⁻¹</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>$q$/c</td>
    <td>$1.6×10^{-19}$</td>
    <td>$c_p$/fF</td>
    <td>1.3</td>
    <td>$R_{hs}$/K·W⁻¹</td>
    <td>0.06</td>
  </tr>
  <tr>
    <td>$k_1$</td>
    <td>0.0051</td>
    <td>$k_2$</td>
    <td>-3.31</td>
    <td>$k_3$</td>
    <td>533.71</td>
  </tr>
</tbody>
</table>

After derivation calculus to the denominator of (30), we can get the maximum $\text{COP}_{\text{max}}$ and optimum $N_{\text{pn\_cop}}$, respectively

$$
\mathrm{COP}_{\max }=\frac{\alpha T_{\text {cold }}}{I R_{e} R_{\mathrm{TECs}}(2 K-\alpha I)-2 \alpha I \sqrt{2 R_{e} R_{\mathrm{TECs}} T_{\text {cold }}}}-\frac{1}{2} \tag{31}
$$

$$
N_{\text {pn_cop }}=\sqrt{\frac{2 \alpha^{2} R_{\text {TECs }}}{R_{e}} T_{\text {cold }}}. \tag{32}
$$

### VI. RESULTS AND DISCUSSION

For the CP1.4-125-0.06L TEC device, the nominal performance parameters are $U_{\text{max}} = 15.4$ V, $Q_{\text{max}} = 51.4$ W, $T_{\text{hot}}^* = 300$ K, $I_{\text{max}} = 6$ A, and $\Delta T_{\text{max}} = 67$ °C. According to these overall characteristics, we can deduce the Seebeck coefficient, electrical thermal resistance, and thermal conductance of the total TECs modules [17]. Usually, the reference value of $T_a = 50$ °C and the system initial temperature $T_{\text{int}} = 120$ °C are employed. It is assumed that the thermal paste has the same size as TECs $(40 × 40$ mm²) with the thermal conductivity $k_{\text{TP}} = 3.2$ W/m · K and the thickness of 0.25 mm. Similar to the thermal paste, the thermal resistance of cold plate can be calculated as $R_{\text{CP}} = 0.085$ °C/W, while $R_{\text{HS}} = 0.06$ °C/W in [17]. For simplicity, the assumption is made that both the sides of the cold plate have the same temperature, which is reasonable due to its high thermal conductance. The model parameters and material properties in a 50-nm technology process used in this paper are based on International Technology Roadmap for Semiconductors provided in [3], which are described in Table I, including the fitted subthreshold current coefficients and calculated thermal resistance results. Based on the initial condition and material parameters above, a cooling package with $12$ mm $× 12$ mm $× 250$-$\mu$m-thick die, $40$ mm $× 40$ mm $× 1.66$ mm TEC array, and $52$ mm $× 52$ mm $× 5$ mm heat sink with the fin height of 10 mm and the fin thickness of 2 mm is established.

With the purpose of estimating the impacts of TECs on the steady-state temperature, we substitute (16) and (25) into (15). Consequently, the steady-state temperature adopting two packages form (C4 and TECs) and COP change with electrical current applied in TECs can be obtained. To verify the effectiveness of our proposed model, we make

![](./images/812755442596839425_3.jpg)

Fig. 3. Temperature distribution with 2.5 A drive electrical current.
(a) Package with the integrated TEC cooling system. (b) TEC arrays.

a comparison with the finite-element thermal–electric modeling using ANSYS 14.5. Based on the 3-D 20-node hexahedron Solid 226 brick from ANSYS element library, the coupled field for TECs with structural, thermal, and electrical degrees of freedom can be accurately calculated. With the same material and size, the final steady-state thermal profiles of 125 TEC arrays and a cooling package with TEC arrays when the excited current is 2.5 A are shown in Fig. 3. Hiding other modules, we can obtain the thermal contour of TEC structure arrays, as shown in Fig. 3(b). It is showed that the junction temperature of die along the bottom of cold plane remain unchanged due to the high thermal conductivity of material Cu.

Fig. 4 shows the cooling temperature and COP versus electrical current using different models and packages. As can be seen, the steady-state temperature predicted by the proposed thermal model is in excellent agreement with the ANSYS finite-element results. A big temperature drop with TECs package is observed when the electrical current across the integrated TECs increases from 1 to 3 A. This is due to small TEC power consumption and efficient working range around maximum COP. Furthermore, the fall trend becomes no more obvious as the electrical current rises beyond 4 A where the power load induced by large TEC current increases significantly. Meanwhile, COP reaches the optimized value at $I = 2.5$ A, while the steady-state temperature using the proposed method decreases to $112\ \mathrm{^\circ C}$. In addition, the calculated temperature results in just 2.3% relative error in the finite-element method at electrical current 2.5 A when COP reaches their maximum, which can validate the effectiveness of our proposed method for steady temperature. However, the steady-state junction temperature provided by the C4 package for the same design always maintains at $133\ \mathrm{^\circ C}$. On this basis, it can be concluded that the TECs can be seen as an accurate temperature tunable devices affording controllable efficiency by external current compared with the traditional C4 package.

![](./images/812755442596839425_4.jpg)

Fig. 4. Steady-state temperature of the system adopting the TECs package and COP versus electrical current applied in the TECs. Long dotted line: steady-state junction temperature at the chip surface in the C4 package.

TABLE II
COMPARISON OF TEMPERATURE AND POWER DISSIPATION
IN THE C4 AND TECs AT $I=2.5$ A

<table>
<thead>
<tr>
<th>Package Structure</th>
<th>Steady-state Temperature /℃</th>
<th>Chip Power /W</th>
<th>Power Consumed by Package /W</th>
</tr>
</thead>
<tbody>
<tr>
<td>C4</td>
<td>133</td>
<td>75.8</td>
<td>0</td>
</tr>
<tr>
<td>TECs</td>
<td>112</td>
<td>67.2</td>
<td>13.2</td>
</tr>
</tbody>
</table>

Table II presents the comparison of temperature and power dissipation with two different package structures when the chip turns into the stable state. After adopting TECs package structure, it is noted that the steady-state temperature and the chip total power consumption decrease by 15.8% and 11.4%, respectively. On the whole, the decreased temperature caused by TECs can lead to power dissipation reduction obviously. It should be considered that the TECs package also consumes a part of power dissipation when obtaining the maximum COP of the whole cooling system. Since lower steady-state temperature can lead to smaller delay, lower power, and higher system reliability by means of controlling thermal runaways, a portion sacrificial power consumption of TECs is acceptable.

From Fig. 4, we can see that the COP changes with the electrical current. When the electrical current across by TECs is applied to 2.5 A, the maximum COP can reach up to 1.4. However, it is not the key variable that affects COP optimum value. Assuming $T_{\text{cold}}$ maintains the steady-state temperature, Fig. 5 shows the COP curves as a function of $N_{\text{pn}}$ and $I$. It is shown that the rise of electrical current on the basis of the optimal value ($I = 2.5$ A) will decrease the maximum COP with fixed $N_{\text{pn}}$. When $N_{\text{pn}} = 96$, COP reaches the maximum regardless of the value of electrical current. As the 2-D parabolic, it is the $N_{\text{pn}}$ that determines the position of maximum COP, while electrical current controls the magnitude

![](./images/812755442596839425_5.jpg)

Fig. 5. COP as a function of $N_{\text{pn}}$ at a different TEC electrical current.
Dotted line: COP achieves maximum at the same abscissa value.

![](./images/812755442596839425_6.jpg)

Fig. 6. TEC power as a function of $N_{\text{pn}}$ at a different TEC electrical current.
Dotted line: power of TECs reaches minimum at the same abscissa value.

of COP in TEC structure. However, it cannot be ignored that larger electrical current means high system power dissipation. Thus, the power consumed by those TECs is necessary to be controlled, while the performance is guaranteed. Fig. 6 shows the curves of the power dissipated by TECs versus $N_{\text{pn}}$ with a different electrical current. It can be seen that the power consumption of TECs is minimized when $N_{\text{pn}} = 34$ independent with the electrical current, which verifies (32). Besides, the power dissipation of TECs shows the modest improvement when the numbers of p-n couples exceed the optimum due to the decrease of thermal resistance of TECs. Thus, as shown in Figs. 5 and 6, a system optimization to achieve both the maximum COP and the lowest TECs power dissipation is impossible. The tradeoff between them depends on the performance requirement and thermal limits.

### VII. CONCLUSION

In this paper, the power model of circuits with and without repeaters is derived, and the steady-state temperature of two packages structures is calculated based on the thermal profile model. To obtain the maximum COP and minimum TECs power, an equivalent thermal resistance model of TECs is proposed and the optimization of p-n couples is performed. The simulation results show that the system steady-state temperature with integrated TECs package can be reduced by as much as 10.6 °C when the COP reaches the maximum, compared with the cases of traditional C4 package.

Simultaneously, the temperature-dependent power decreases by 11.4%. Optimized p-n couple numbers can be directly obtained by the curves of the TECs power or COP as a function of $N_{\text{pn}}$ with a different electrical current. Packaging technology with integrated TECs can be used to prevent the thermal runaways and provide an effective thermal management solution for nanometer ICs.

### REFERENCES

[1] H. F. Hamann et al., "Hotspot-limited microprocessors: Direct temperature and power distribution measurements," *IEEE J. Solid-State Circuits*, vol. 42, no. 1, pp. 56-65, Jan. 2007.

[2] A. H. Ajami, K. Banerjee, and M. Pedram, "Modeling and analysis of nonuniform substrate temperature effects on global ULSI interconnects," *IEEE Trans. Comput.-Aided Design Integr. Circuits Syst.*, vol. 24, no. 6, pp. 849-861, Jun. 2005.

[3] Semiconductor Industry Association. (2012). *International Technology Roadmap for Semiconductors (ITRS)*. [Online]. Available: http://www.itrs.net/

[4] S.-C. Lin and K. Banerjee, "Cool chips: Opportunities and implications for power and thermal management," *IEEE Trans. Electron Devices*, vol. 55, no. 1, pp. 245-255, Jan. 2008.

[5] M. Igarashi *et al.*, "10.2 A 28 nm HPM heterogeneous multi-core mobile application processor with 2 GHz cores and low-power 1 GHz cores," in *IEEE Int Solid-State Circuits Conf. Dig. Tech. Papers*, Feb. 2014, pp. 178-179.

[6] M. Redmond, K. Manickaraj, O. Sullivan, S. Mukhopadhyay, and S. Kumar, "Hotspot cooling in stacked chips using thermoelectric coolers," *IEEE Trans. Compon., Packag., Manuf. Technol.*, vol. 3, no. 5, pp. 759-767, May 2013.

[7] S. Ramanathan and G. M. Chrysler, "Solid-state refrigeration for cooling microprocessors," *IEEE Trans. Compon. Packag. Technol.*, vol. 29, no. 1, pp. 179-183, Mar. 2006.

[8] D. Mitrani, J. Salazar, A. Turó, M. J. García, and J. A. Chávez, "One-dimensional modeling of TE devices considering temperature-dependent parameters using SPICE," *Microelectron. J.*, vol. 40, no. 9, pp. 1398-1405, Sep. 2009.

[9] H. Y. Zhang, Y. C. Mui, and M. Tarin, "Analysis of thermoelectric cooler performance for high power electronic packages," *Appl. Thermal Eng.*, vol. 30, nos. 6-7, pp. 561-568, May 2010.

[10] I. Chowdhury *et al.*, "On-chip cooling by superlattice-based thin-film thermoelectrics," *Nature Nanotechnol.*, vol. 4, no. 4, pp. 235-238, Jan. 2009.

[11] I. Chowdhury *et al.*, "Site-specific and on-demand high heat-flux cooling using superlattice based thin-film thermoelectrics," in *Proc. ASME InterPACK Conf.*, 2010, pp. 521-526.

[12] E. Murphy, C. Michie, H. White, W. Johnstone, A. E. Kelly, and I. Andonovic, "High temperature wavelength division network for avionic applications," *J. Lightw. Technol.*, vol. 31, no. 18, pp. 3006-3013, Sep. 15, 2013.

[13] R. Venkatasubramanian, "Applied physics: Nanothermal trumpets," *Nature*, vol. 463, p. 619, Feb. 2010.

[14] C. Alaoui, "Solid-state thermal management for lithium-ion EV batteries," *IEEE Trans. Veh. Technol.*, vol. 62, no. 1, pp. 98-107, Jan. 2013.

[15] M. K. Russel, D. Ewing, and C. Y. Ching, "Numerical and experimental study of a hybrid thermoelectric cooler thermal management system for electronic cooling," *IEEE Trans. Compon., Packag., Manuf. Technol.*, vol. 2, no. 10, pp. 1608-1616, Oct. 2012.

[16] M. P. Gupta, M.-H. Sayer, S. Mukhopadhyay, and S. Kumar, "Ultrathin thermoelectric devices for on-chip peltier cooling," *IEEE Trans. Compon., Packag., Manuf. Technol.*, vol. 1, no. 9, pp. 1395-1405, Sep. 2011.

[17] B. Abramzon, "Numerical optimization of the thermoelectric cooling devices," *J. Electron. Packag.*, vol. 129, no. 3, pp. 339-347, Nov. 2007.

[18] C.-H. Cheng, S.-Y. Huang, and T.-C. Cheng, "A three-dimensional theoretical model for predicting transient thermal behavior of thermoelectric coolers," *Int. J. Heat Mass Transf.*, vol. 53, nos. 9-10, pp. 2001-2011, Apr. 2010.

[19] B. Vermeersch, J.-H. Bahk, J. Christofferson, and A. Shakouri, "Thermoreflectance imaging of sub 100 ns pulsed cooling in high-speed thermoelectric microcoolers," *J. Appl. Phys.*, vol. 113, no. 10, pp. 104502-1-104502-8, Mar. 2013.

[20] X.-C. Li, J.-F. Mao, H.-F. Huang, and Y. Liu, "Global interconnect width and spacing optimization for latency, bandwidth and power dissipation," IEEE Trans. Electron Devices, vol. 52, no. 10, pp. 2272-2279, Oct. 2005.

[21] R. Jakushokas and E. G. Friedman, "Resource based optimization for simultaneous shield and repeater insertion," IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 18, no. 5, pp. 742-749, May 2010.

[22] Z. Li, Y. Zhou, and W. Shi, "O(mn) time algorithm for optimal buffer insertion of nets with m sinks," IEEE Trans. Comput.-Aided Design Integr. Circuits Syst., vol. 31, no. 3, pp. 437-441, Mar. 2012.

[23] J. C. Ku and Y. Ismail, "Area optimization for leakage reduction and thermal stability in nanometer-scale technologies," IEEE Trans. Comput.-Aided Design Integr. Circuits Syst., vol. 27, no. 2, pp. 241-248, Feb. 2008.

[24] J. C. Ku and Y. Ismail, "Thermal-aware methodology for repeater insertion in low-power VLSI circuits," in Proc. ACM/IEEE Int. Symp. Low Power Electron. Design, Aug. 2007, pp. 86-91.

[25] X.-C. Li, J.-F. Mao, and W.-Y. Yin, "Dynamic power model of CMOS gates driving transmission lines based on Fourier analysis," IEEE Trans. Electron Devices, vol. 55, no. 2, pp. 594-600, Feb. 2008.

[26] L. Jiang, Y. Cheng, and J. Mao, "Analysis and optimization of thermal-driven global interconnects in nanometer design," IEEE Trans. Compon., Packag., Manuf. Technol., vol. 1, no. 10, pp. 1564-1572, Oct. 2011.

[27] A. H. Ajami, K. Banerjee, and M. Pedram, "Analysis of substrate thermal gradient effects on optimal buffer insertion," in IEEE/ACM Int. Conf. Comput. Aided Design Dig. Tech. Papers, Nov. 2001, pp. 44-48.

[28] J. C. Ku and Y. Ismail, "Area optimization for leakage reduction and thermal stability in nanometer scale technologies," in Proc. Asia South Pacific Conf. Design Autom., Jan. 2005, pp. 231-236.

[29] R. Venkatasubramanian, E. Siivola, T. Colpitts, and B. O'Quinn, "Thin-film thermoelectric devices with high room-temperature figures of merit," Nature, vol. 413, pp. 597-602, Oct. 2001.

[30] S. H. Choday and K. Roy, "Sensitivity analysis and optimization of thin-film thermoelectric coolers," J. Appl. Phys., vol. 113, no. 21, pp. 214906-1-214906-7, 2013.

![](./images/812755442596839425_7.jpg)

Ning Wang was born in 1984. He received the B.S. degree in microelectronics from the Guilin University of Electronic Technology, Guilin, China, in 2007, and the M.S. and Ph.D. degrees in micro- electronics from Xidian University, Xi'an, China, in 2009 and 2012, respectively.

He is currently a Post-Doctoral Researcher with Shanghai Jiao Tong University, Shanghai, China.

![](./images/812755442596839425_8.jpg)

Xiao-Chun Li (M'08) was born in 1977. She received the B.S. degree in electronic engi- neering and the M.S. degree in telecommunication and information systems from Tianjin University, Tianjin, China, in 1999 and 2002, respectively, and the Ph.D. degree from Shanghai Jiao Tong Univer- sity, Shanghai, China, in 2007.

She has been with the Department of Electronic Engineering, Shanghai Jiao Tong University, since 2002, where she is currently an Associate Professor.

![](./images/812755442596839425_9.jpg)

Jun-Fa Mao (M'92-SM'98-F'12) received the B.S. degree in radiation physics from the National University of Defense Technology, Changsha, China, in 1985, the M.S. degree in experimental nuclear physics from the Shanghai Institute of Nuclear Research, Shanghai, China, in 1988, and the Ph.D. degree in electronic engineering from Shanghai Jiao Tong University, Shanghai, in 1992.

He has been with Shanghai Jiao Tong University since 1992.