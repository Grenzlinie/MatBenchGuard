Accepted Manuscript

Research Paper

The optimization design and parametric study of thermoelectric radiant cooling and heating panel

Limei Shen, Zhilong Tu, Qiang Hu, Cheng Tao, Huanxin Chen

![](./images/811125987696705536_1.jpg)

<table>
  <tr>
    <td>PII:</td>
    <td>S1359-4311(16)32412-7</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.applthermaleng.2016.10.094</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>ATE 9296</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Applied Thermal Engineering</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>21 August 2016</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>13 October 2016</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>14 October 2016</td>
  </tr>
</table>

Please cite this article as: L. Shen, Z. Tu, Q. Hu, C. Tao, H. Chen, The optimization design and parametric study of thermoelectric radiant cooling and heating panel, Applied Thermal Engineering (2016), doi: http://dx.doi.org/10.1016/j.applthermaleng.2016.10.094

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

The optimization design and parametric study of thermoelectric radiant cooling and heating panel

Limei Shen; Zhilong Tu; Qiang Hu; Cheng Tao; Huanxin Chen*

Department of Refrigeration and Cryogenics, Huazhong University of Science and Technology, Wuhan, China

*Corresponding author, E-mail: chenhuanxin@tsinghua.org.cn

ABSTRACT:

Thermoelectric radiant air-conditioning (TE-RAC) system is a promising approach to implement thermoelectric technology in large-scale refrigeration system applications in future. However, no standard exists for the in situ design and the performance evaluation of thermoelectric radiant heating/cooling panel. Thus, this study aims to not only clarify the design procedure but also to share our thermal physical model and design configurations of the thermoelectric radiant panel to serve as a reference for other similar design cases. In addition, a simplified representation approach for the thermal characterization of thermoelectric panels is also discussed.

The main design variables are the number of thermoelectric modules and the size of radiant panels. The inner surface transient temperature distribution of thermoelectric radiant panels is discussed, and the approaches for improving the uniformity of the inner surface temperature are proposed. The influence of cooling/heating load on the uniformity of the inner surface temperature is a slight larger than the size of the panel,

so the matching design is very important. The results show that the optimal thickness of thermoelectric radiant panels is 4 mm, and the number of thermoelectric modules (TEM) is 16 per square meter, which also could solve the issues about dew formation and uniformity of inner surface temperature.

Keywords: Thermoelectric radiant air-conditioning; Thermal physical model; Design configurations; Thermoelectric radiant panel; Temperature distribution

Nomenclature

| $A_{TEM}$ | Surface area of thermoelectric module [$m^{2}$] |
|---|---|
| $C$ | Specific heat capacity at constant pressure of radiant plate [$J\cdot kg^{-1}\cdot K^{-1}$] |
| $COP$ | Coefficient of performance |
| $COP_{c,Qcmax}$ | The COP for achieving the maximum cooling capacity |
| $COP_{h,Qcmax}$ | The COP for achieving the maximum heating capacity |
| $h$ | Total heat transfer coefficient [$W\cdot K^{-1}\cdot m^{-2}$] |
| $I$ | Input electric current of thermoelectric module [A] |
| $K$ | Thermal conductance of thermoelectric module [$W\cdot K^{-1}$] |
| $L_{l}$ | The length from centre to boundary of the TE radiant panel unit [m] |
| $L_{t}$ | The thickness of the TE radiant panel unit [m] |
| $N$ | The number of TEM per square meter |
| $P$ | Input electrical power of each thermoelectric module [W] |
| $Q_{c}$ | Cooling capacity of each thermoelectric module [W] |
| $Q_{c,COPmax}$ | The cooling capacity for achieving the maximum COP [W] |
| $Q_{h}$ | Heating capacity of each thermoelectric module [W] |

$Q_{h,COPmax}$
The heating capacity for achieving the maximum COP [W]

$R$
Electrical resistance of thermoelectric module [$\Omega$]

$R_{o}$
Thermal resistance of heat radiator attached to TEM [K$\cdot$W$^{-1}$]

$t$
Time [s]

$T$
Temperature of radiant plate [K]

$T_{ai}$
The indoor air temperature [K]

$T_{ao}$
The outdoor air temperature [K]

$T_{c}$
Cold side temperature of thermoelectric module [K]

$T_{h}$
Hot side temperature of thermoelectric module [K]

$TEM$
Thermoelectric module

$TE$-$RAC$
Thermoelectric radiant air-conditioning

$x,\ z$
Coordinate

$ZT$
The dimensionless figure-of-merit of thermoelectric material

### Greek letters
$\alpha$
Seebeck coefficient of thermoelectric module [V$\cdot$K$^{-1}$]

$\kappa$
Heat conductivity of radiant plate [W$\cdot$m$^{-1}$$\cdot$K$^{-1}$)]

$\rho$
Density of radiant plate [kg$\cdot$m$^{-3}$]

### Subscripts
c
Cooling mode

h
Heating mode

max
The maximum value

###1. Introduction

The building industry nowadays is is facing three major challenges: the increased concern for environmental protection, the enhanced requirement for energy saving and the growing need for comfort improvements.These challenges have led many researchers to develop low energy green building systems[1].The use of radiant air- conditioning(RAC) systems as an efficient way to achieve occupant thermal comfort in buildings with low energy demands has increased over the years, but the traditional RAC system results in depletion of the ozone layer by the release of CFCs.

Meanwhile, thermoelectric cooling/heating technology have gotten more attention due to CFC refrigererents free, especially as the development of novel high performance thermoelectric material.But the application of thermoelectric devices is still limited due to low coefficients of performance, especially in large-scale applications. while the innovative applications of current thermoelectric materials are crucial for thermoelectric technology and arguably even more urgent than improving the dimensionless figure-of-merer( ZT) of thermoelectric material[2. Therefore, a novel thermoelectric radiant air- conditioning( TE-RAC) system was proposed, which adopts thermoelectric modules(TEMs) instead of a hydronic source system as a radiant panel to remove the heat load of the the room by thermal convection and radiation.It not only takes advantage of radiant heat transfer as a comfortable, healthy and energy efficient way to remove thermal loads, but also operates in a more environmentally environmentally manner[3. TE-RAC systems can achieve high energy efficiency because of reduced distribution losses and the possibility of using low- and high-temperature of

thermoelectric modules for heating and cooling, respectively. It is also a promising approach to implement thermoelectric technology in large-scale refrigeration system applications in future [4; 5].

Then, researchers have carried out series of experiments to demonstrate the feasibility and assess its practical operating performance. Lertsatitthanakorn et al.[6] designed a thermoelectric ceiling cooling panel composed of 36 TEMs for a $4.5\ \text{m}^3$ room, the cooling capacity was 289.4 W with a maximum COP of 0.75. Liu and Luo et al.[5; 7; 8] presented a solar thermoelectric cooled ceiling combined with a displacement ventilation system and a solar thermoelectric radiant wall system for space cooling and heating. The $1.8\ \text{m}×0.6\ \text{m}$ thermoelectric cooled ceiling panel and $1.58\ \text{m}×0.81\ \text{m}$ thermoelectric wall panel were tested, respectively. The results showed that the total heat flux of the former system in cooling mode was higher than $60\ \text{W/m}^2$ and the system COP could reach 0.9 under an operating voltage of 5 V. And in the heating mode, the total heat flux under an operating voltage of 4 V is higher than $110\ \text{W/m}^2$ and the COP of the system could reach 1.9. The previous studies were all built a prototype of thermoelectric ceiling panel to investigate its performance and demonstrate its feasibility. But it should be noted that in the previous studies the design characteristics of the TE radiant panel were not described in detail, which is very important for the development of this novel air-conditioning system.

The TE radiant panel is composed of TEMs, the radiant plate and the heat sink attaching to TEMs. The dimension and material of the radiant plate, the number and type of TEMs and the thermal resistance of the heat sink are the most important

parameters for panel design. In addition, the TE radiant panel should be designed to maintain the indoor condition within the comfort range. KoChendörfer [9] gave an overview of standardized testing of the evaluation methods for cooling performance of panels and introduced a method by which the cooling capacity, measured under laboratory conditions, could be used as a basis parameter for design of panels. Tian et al.[10] experimentally studied the cooling performance of ceiling radiant cooling panels without mechanical ventilation in a real office room. It is showed that the inner surface temperature of panel mainly affected the cooling capacity of the ceiling radiant cooling panel. Atmaca et al.[11] analyzed the interior surface temperatures of wall and ceiling effect on thermal comfort. Furthermore, the manufacturer survey resulted in identifying commonly used categories of radiant heating/cooling surface temperature ranges, and the panel is selected according to the manufacturer's data in initial design phase, the cooling capacity is an extremely important basis for selection.

As mentioned above, the heat flux and surface temperature distribution are the main factors that influence the thermal comfort of occupants[12]. Therefore, heat flux and floor surface temperature distribution should be examined at the design stage, and the surface temperature and cooling capacity are representative of the thermal characteristics of the TE radiant panel. Luo et al.[8] established a heat transfer model of thermoelectric radiant ceiling panel to simulate its surface temperature field, but their model ignored the influence of the thickness of thermoelectric radiant ceiling panel. Thus, it can't be used to analyze the optimal thickness of the radiant plate.

Accordingly, this study establishes the energy transfer model to investigate the interior surface temperature distributions of a TE radiant panel. An optimal design methodology for thermoelectric panels is presented. Thereinto, the main design parameters of TE radiant panels, which are the concerning data of manufacturer in the design procedure, are discussed. The design flow charts are developed in order to help designers to consider heat flux, difference between maximum and minimum surface temperature at the design stage through investigating the relationships between temperature distribution and design parameters. The optimized design configurations are then validated by experiment results. Then some critical applications and limitations related to the TE radiant panel design were suggested.

### 2. Mathematical model

TE-RAC system is a novel RAC system[3], as shown in Fig.1. The TEMs are electrically and thermally in parallel and sandwiched between heat radiator and aluminum panel to substitute the hydronic panel of traditional RAC systems, and the so called TE radiant panel exchanges heat with other surfaces in the room by radiation, and exchanges heat with the room air by convection. A non-uniform temperature distribution is one of the main characteristics of radiant panels. The heat transfer model for optimizing the design of the TE radiant panel was established to obtain the temperature distribution and thermal characteristics of the panel. A TE radiant panel consists of a radiant plate, a number of TEMs connecting in series and a heat radiator for dissipating the heat generation of TEM in summer or absorbing heat from ambient

in winter. The TEM is assembled by connecting a number of thermoelectric elements electrically in series but thermally in parallel and sandwiched between two ceramic plates. The thermoelectric element is the basic working unit of thermoelectric heating and cooling. TEMs are also known as solid-state active heat pumps because their cold and hot sides can be switched by reversing the current direction.

The thermal characteristics in each TEM are identical, and temperature distributions from center to boundary of the radiant plate are almost the same. Therefore, only one diagonal element of the extract unit of panel is considered here, which is shown as in Fig.2(a). The exacting element is used to build the energy balance equations in cooling and heating mode, as shown in Fig.2(b). The blue and red solid arrow respectively shows the heat flux direction in cooling mode and heating mode. The theoretical heat transfer model is developed by basing on the following assumptions:

(1) The thermoelectric module is assumed to be a surface heat source which is closely adjacent to left face of the extracting element, and the cooling or heating load is constant.

(2) The thermal and electrical properties of the TE radiant panel are isotropic and independent of temperature.

(3) The total heat transfer coefficient ($h$) between the radiant ceiling and the room is constant, it is assigned the value of $11\ \text{Wm}^{-2}\text{K}^{-1}$ in the cooling mode and $6\ \text{Wm}^{-2}\text{K}^{-1}$ in the heating mode[13].

The governing equations for the present study are expressed in the following statement:

### 2.1. Cooling mode

The thermal partial differential equation of a TE radiant panel in cooling mode:
$$
\rho C \frac{\partial T}{\partial t}=\kappa \frac{\partial^{2} T}{\partial x^{2}}+\frac{h}{L_{t}}\left(T_{a i, c}-T\right) \tag{1}
$$

Initial conditions:
$$
\mathrm{T}(0,0)=T_{a o, c} \tag{2}
$$

$$
\mathrm{T}\left(L_{t}, 0\right)=T_{a o, c} \tag{3}
$$

Boundary conditions:
$$
\left.\rho C \frac{d x}{2} L_{t} d z \frac{d T}{d t}\right|_{x=0}=\left.\kappa L_{t} d z \frac{\partial T}{\partial x}\right|_{x=0}+h \frac{d x}{2} d z\left(\left.T_{a i, c}-T\right|_{x=0}\right)-\frac{Q_{c}}{A_{T E M}} L_{t} d z \tag{4}
$$

$$
\left.\rho C \frac{d x}{2} L_{t} d z \frac{d T}{d t}\right|_{x=\sqrt{2} L_{t}}=h \frac{d x}{2} d z\left(\left.T_{a i, c}-T\right|_{x=\sqrt{2} L_{t}}\right)-\left.\kappa L_{t} d z \frac{\partial T}{\partial x}\right|_{x=\sqrt{2} L_{t}} \tag{5}
$$

where, $\rho$, $\kappa$, C are respectively the density, heat conductivity and specific heat capacity of radiant plate. $L_1$ and $L_t$ are the length from centre to boundary and thickness of the TE radiant panel unit. $T_{ai}$ and $T_{ao}$ are respectively the indoor and outdoor temperature. The subscript c represents the cooling mode. T is the temperature of the radiant plate, which is the function of x (coordinate) and t (time).

$A_{TEM}$ is the surface area of TEM. $Q_c$ is the cooling capacity of TEM in the cooling mode, which can be calculated using Eq.(6)[14].

$$Q_{\mathrm{c}}=\alpha I T_{c}-0.5 I^{2} R-K\left(T_{h}-T_{c}\right) \tag{6}$$

Note that the first term on the right hand side of Eq.(6) represents the Peltier heat, which converts electrical energy into a temperature gradient resulting in cooling effect.
The second term represents the Joule heat, which is generated inside the TEM due to the electrical resistance. It assumes that 50% of the Joule heat goes to the cold side and the other 50% goes to the hot side[14]. The third term represents the Fourier heat, which is the heat conducted from the hot side to the cold side due to the heat conductivity of the thermoelectric material and the temperature gradient.

The heat balance equation at the hot side of TEM is given by

$$\left(T_{h}-T_{\mathrm{ao}, \mathrm{c}}\right) / \mathrm{R}_{\mathrm{o}}=\alpha I T_{h}+0.5 I^{2} R-K\left(T_{h}-T_{c}\right) \tag{7}$$

The left part of Eq.(7) is the heat taken by the outdoor air, the right part of the equation is the heat released by TEM. Note that the first term on the right hand side of Eq.(7) represents the Peltier heat, which converts electrical energy into a temperature gradient resulting in heating effect. The input electrical power (P) of the TEM is given by

$$P=\alpha I\left(T_{h}-T_{c}\right)+I^{2} R \tag{8}$$

The coefficient of performance of TEM in the cooling mode $(COP_{c})$ is given by

$$C O P_{c}=Q_{c} / P \tag{9}$$

where, $\alpha$, R and K are the Seebeck coefficient, the electrical resistance and the thermal conductance of thermoelectric cooler module respectively; I (A) is the input current of thermoelectric cooler module; $T_{c}$ (K) is a user-defined cold side

temperature of thermoelectric cooler module and $T_h$ (K) is hot side temperature of thermoelectric cooler module. $R_o$ is the thermal resistance of the heat radiator attached to the TEM.

### 2.2. Heating mode
The thermal partial differential equation of TE radiant panel in heating mode:

$$
\rho C \frac{\partial T}{\partial t}=\mathrm{K} \frac{\partial^{2} T}{\partial x^{2}}-\frac{h}{L_{t}}\left(T-T_{a i, h}\right) \tag{10}
$$

Initial conditions:

$$
\mathrm{T}(0,0)=T_{a o, h} \tag{11}
$$

$$
\mathrm{T}\left(L_{t}, 0\right)=T_{a o, h} \tag{12}
$$

Boundary conditions:

$$
\left.\rho C \frac{d x}{2} L_{t} d z \frac{d T}{d t}\right|_{x=0}=\frac{Q_{h}}{A_{T E M}} L_{t} d z-\left.K L_{t} d z \frac{\partial T}{\partial x}\right|_{x=0}-h \frac{d x}{2} d z\left(\left.T\right|_{x=0}-T_{a i, h}\right) \tag{13}
$$

$$
\left.\rho C \frac{d x}{2} L_{t} d z \frac{d T}{d t}\right|_{x=L_{t}}=\left.K L_{t} d z \frac{\partial T}{\partial x}\right|_{x=L_{t}}-h \frac{d x}{2} d z\left(\left.T\right|_{x=L_{t}}-T_{a i, h}\right) \tag{14}
$$

where, the subscript h represents the heating mode. $Q_h$ is the Heating capacity of TEM can be obtained by[14]

$$
\mathrm{Q}_{h}=\alpha I T_{h}+0.5 I^{2} R-K\left(T_{h}-T_{c}\right) \tag{15}
$$

The heat balance equation at the cold side of TEM in the heating mode can be shown by

$$
\left(T_{\mathrm{ao}, \mathrm{h}}-T_{\mathrm{c}}\right) / \mathrm{R}_{\mathrm{o}}=\alpha I T_{c}-0.5 I^{2} R-K\left(T_{h}-T_{c}\right) \tag{16}
$$

The coefficient of performance of the TEM in the heating mode $(COP_h)$ is given by

$$
C O P_{h}=Q_{h} / P \tag{17}
$$

The numerical calculation is performed using the finite volume method and the Gear's algorithm based on MATLAB[15; 16]. The design varies only one uncertain input each time while the others remain constant. A temperature search approach is proposed to calculate the input current of each TEM, and critical cooling/heating capacity and COP of the TE radiant panel.

### 3. Results and discussion
RAC systems normally control the indoor temperature by adjusting the surface temperature of radiant panels. The surface temperature of radiant panel is usually in the range of 17℃ - 20 ℃ for cooling and 27 ℃ - 100 ℃ for heating[17]. Note that the minimum value of surface temperature is 17 ℃ in cooling mode which was higher than the dew point temperature 16 ℃ for preventing potential condensation[18]. It also indicates that the only reliable or appropriate design consideration would involve analyzing the surface-to-air design process and not the mean radiant temperature.

There are many variations or schemes used to obtain appropriate surface temperature, while the size of the panel, the number of TEM and the input electric current could be the most concerning data for the designer and manufacturer. Furthermore, the temperature distribution of TE radiant panels is non-uniform, while the design of TE radiant panel should be ensure the temperature of entire surface is in the commented ranges. According to the above analysis, the design procedure of TE Radiant panel is built, as shown in Fig. 3.

### 3.1. Influence factors on design parameters

To conduct the design procedure, the selection of equipment and determining the thermal resistance of heat radiator are the most important steps. The selection of radiant plate, TEM and heat radiator affects the performance of TE radiant panel. each radiant panel design or product may be unique, while there is a common basis to expect lower operating and manufacturing cost. Meanwhile, considering the radiant plate of traditional RAC system, the aluminum alloy is usually selected as radiant plate for low cost and high heat conductivity. The density $\rho$, heat conductivity $\kappa$ and heat capacity C of the 6063 aluminum alloy plate are $2680\ \text{kgm}^{-3}$, $209\ \text{Wm}^{-1}\text{K}^{-1}$, $900\ \text{Jkg}^{-1}\text{K}^{-1}$, respectively. The performances of commercial TEM is almost the same for similar types, but the costs are almost different according to various manufacturers.

TEC1-12706 is a popular commercial TEM (4 USD) in China for low cost, which is chosen to build the TE radiant panels. Its performance is discussed in detail in Ref.3.

The Seebeck coefficient ($\alpha$), the electrical resistance (R) and the thermal conductance (K) of TEC1-12706 are $0.051\ \text{VK}^{-1}$, $1.9558\ \Omega$, and $0.5177\ \text{WK}^{-1}$, respectively[3]. The design indoor temperature was set to $26\ ^\circ\text{C}$ in cooling mode and $22\ ^\circ\text{C}$ in heating mode according to the recommendations of ASHRAE and associated Chinese design manual. The recommended indoor temperature of ASHRAE is in the range of 23-26 $^\circ\text{C}$ in summer and 21-24 $^\circ\text{C}$ in winter[19], and the recommended indoor temperature is in the range of 24-28 $^\circ\text{C}$ in summer and 18-22 $^\circ\text{C}$ in winter in the Chinese design guideline[20].

Furthermore, we discuss the maximum cooling/heating capacity and corresponding COP, maximum COP and corresponding cooling/heating capacity of TEMs under different thermal resistance, as shown in Fig.4 and Fig.5. Fig.4 (a) and (b) show that the maximum cooling capacity decreased and the corresponding $COP_c$ slowly decreased with the increase of the thermal resistance, and the change of $COP_c$ was relatively small when $R_o$ was in the range of 0.25-1.26 $KW^{-1}$. But the maximum cooling capacity was smaller than 7 W when $R_o$ was larger than $1.1\ KW^{-1}$ in Fig.4(a) and $1.25\ KW^{-1}$ in Fig.4(b), respectively. The electrical current for achieving maximum cooling capacity decreased with the increase of $R_o$. Fig.4 shows that the maximum $COP_c$ decreased and the corresponding $Q_c$ slowly decreased with the increase of the thermal resistance. There was a jumping point in the curve of corresponding $Q_c$. Since there was a critical thermal resistance $R_o$. When $R_o$ is smaller than $0.62\ KW^{-1}$, the electrical current for achieving maximum $COP_c$ was 1.398 A, and when $R_o$ is larger than $0.62\ KW^{-1}$, the electrical current for achieving maximum $COP_c$ suddenly changed into 1.2857 A. Thus, the jumping of electrical current was responsible for the jumping of cooling capacity. This kind critical value of $R_o$ was $0.58\ KW^{-1}$ in Fig. 4(b). In addition, the performance of TEC when $T_c=17\ ^\circ$C was little larger than that $T_c=20^\circ$C.

Fig.5(a) shows that the maximum heating capacity $Q_h$ and the corresponding $COP_h$ decreased with the increase of the thermal resistance. The maximum $COP_h$ decreased and the corresponding $Q_h$ slowly decreased with the increase of the thermal resistance, and the jumping critical value of $R_o$ was $0.95\ KW^{-1}$. Fig.5 (b) shows that the

maximum $Q_h/COP_h$ and the corresponding $COP_h/Q_h$ decreased with the increase of the thermal resistance, and the curves of $Q_{hmax}/Q_{hcopmax}$ and $COP_{hmax}/ COP_{hQcmax}$ were respectively overlapped. Because the corresponding electrical currents were all equal to the maximum input electrical current. Actually, if the maximum input electrical current was set as 10 A, the maximum $Q_h$ and the corresponding $Q_h$ quite slowly increase with the increase of the thermal resistance, and the electrical current for achieving maximum cooling capacity was 10 A. The maximum $COP_h$ decreased and the corresponding $Q_h$ slowly decreased with the increase of the thermal resistance, and the electrical current for achieving maximum $COP_h$ was 6.4 A.

Comparing Fig.4 and Fig.5, it is noted that the impact of $R_o$ on the cooling performance of TEMs appears is larger than on the heating performance. According to the above analysis, the thermal resistance of hot-side heat radiator ($R_o$) is assigned value of $1\ KW^{-1}$ for following discussion. Note that such thermal resistance of the hot-side heat radiator data is only used for the size determination in the design stage. For discussing the temperature distribution in the validation stage, the practical thermal resistance data is used.

### 3.2. Design parameters

The temperature distribution reflected the interaction between the size of TE radiant panel, the number of TEMs and the cooling/heating capacity of each TEM. Based on the basic heat transfer theory, we know that the temperature decreases or increases along the length direction which is far away from the heat or cold source. It

means that the maximum or minimum temperature must be appeared at the left or right hand of the extracting element. Thus, the left and right hand temperatures of the extracting element just have been studied. It also illustrates that the maximum or minimum value of the radiant panel is obtained at the centre or the corner of extracting unit, respectively. So the computed length of the extracting element equals to $\sqrt{2}L_{l}$. The temperature difference between the left and right hand increases with the increase of length of the panel and cooling capacity of TEM, and with the decrease of the thickness of the panel. Therefore, it's important to study the critical size and cooling capacity by discussing the interaction influence of these three parameters together, to ensure the whole surface temperature are in the required range.

The critical cooling/heating capacities and the corresponding required number of TEM according to various sizes of the TE panel unit are calculated and listed in Table 1. The critical values were obtained at the centre and corner of the extracting unit when the surface temperature was $17\ \mathrm{^\circ C}$ and $20^\circ\mathrm{C}$ in the cooling mode and $27\ \mathrm{^\circ C}$ and $100\ \mathrm{^\circ C}$ in the heating mode, respectively. For instance, if the thickness $L_{t}$ and extracting unit length $L_{l}$ of TE radiant panel are respectively 2 mm and 0.1 m, the cooling capacity of each TEM is 8.14 when the minimum surface temperature is $17\ \mathrm{^\circ C}$, and the cooling capacity is 9.57 when the maximum surface temperature is $20\ \mathrm{^\circ C}$. The maximum extracting unit length $L_{l}$ is 0.133 and critical cooling capacity of each TEM is 11.53 W when the thickness $L_{t}$ is 2 mm. It showed that the critical cooling/heating capacity, which is the range for satisfying the surface temperature requirement of TE radiant panel, respectively increased with the increase of length or with the decrease

of the thickness. The critical length increased with the increase of the thickness of TE radiant panel. This is because that the thermal resistance is proportional to length and inversely proportional to the thickness of the TE radiant panel. Then, the feasibility according to the space cooling sensible load ($90\ \text{W}\ \text{m}^{-2}$) and heating load ($70\ \text{W}\ \text{m}^{-2}$) for radiant air conditioning systems are discussed.

The feasible design data are used to compute the input parameters of TEM and the cooling/heating performance of TE radiant panel per square meter, which are listed in Table 2. The input electric current of TEM decreased with the increase of thickness and decrease of length. While the ranges of COP are almost equal to each other when the thickness is respectively equal to 3 mm, 4 mm and 5 mm.

The evaluation of the design according to the performance of TE radiant panel are presented. Combined the $\text{COP}_c/\text{COP}_h$ of TEM and cost of TE radiant panel, the best choice of design datum is that the thickness is 4 mm and the needed number of TEM is 16 per square meter. Because the operating cost is almost the same for the 'Good' groups, the initial cost of aluminum panel is almost 6.3 $\$$/kg and each TEM (TEC1-12706) is almost 4 $\$$ in China, so we should choose the design with few TEMs. It also could see that the COP of TE-RAC is larger than the COP of conventional TE air-conditioning system. Therefore, the TE-RAC system may be one of promising method for enlarging the market of TE technology in large cooling areas.

In conclusion, the selection criteria for design parameters of TE radiant panel consists of three parts, as shown in Fig.6. In the first part, the initial sizes of TE radiant panel are given by the designers. In the second part, the feasibility sizes are

selected based on critical performance of extract unit TE radiant panel at different thresholds. In the third part, the feasibility size of TE radiant panel is used to determine the COP of TE-RAC systems, the optimal size of TE radiant panel is then selected based on the minimum initial and operating cost using COP and number of TEMs.

### 3.3. Transient Temperature Distribution and Design Validation

To validate the design datum of TE radiant panel, a case study is conducted and the surface temperature is as the detecting parameters. A TE radiant panel unit was built to test the surface temperature distribution, the test measurement points are shown in Fig.6. The best choice for TE radiant panel design is that the thickness is set as 4 mm, and the number of TEM is set as 16, respectively. The cooling and heating load are respectively assumed to be $90\ \text{W/m}^2$ and $80\ \text{W/m}^2$, respectively. The input electrical current should be in the range of 1.43~1.68 A in cooling mode and 2.28~3.07 A in heating mode. The DC electrical current is supplied by a DC power source KXN-6020D, which measured the input electrical current for TEMs shown on the front screen with 1% accuracy. The surface temperature measured by T type thermocouples (TT-T-24-SLE-1000, accuracy $\pm0.5\ ^\circ\text{C}$) are transmitted to the recorder and then to the computer for analysis. The tests were conducted in an air conditioned room in which the air temperature was maintained at $35\ ^\circ\text{C}$ in cooling mode and $10\ ^\circ\text{C}$ in heating mode. The commercial TE module TEC1-12706 has the dimension of $40\ \text{mm (L)} \times 40\ \text{mm (W)} \times 3.8\ \text{mm (H)}$. The hot-end of TE module was connected with a water

radiator to improve the heat rejection at the hot end, which average heat transfer value was about $100\ \text{WK}^{-1}$. Note that the test temperatures are all independent variables, so the experimental error is determined by the accuracy of the corresponding instrument.

In the experiments, the temperature is in the range of 10-70 °C. Thus, the relative uncertainty of the current of measurement reaches a maximum 5% when the temperature is 10 °C; however, only 0.7 % is found when the temperature is 70 °C.

Two groups of experiment tests were performed. In the first group of tests, a series of tests in cooling mode were conducted when applied electrical current changes between 1 A to 2 A at the interval of 0.5 A. It found the surface temperatures of the TE radiant panel could sustain at the required range when the applied current equaled to 1 A. In the second group of tests, a series of tests in heating mode were conducted when applied electrical current changes between 2 A to 4 A at the interval of 1 A. It found the surface temperatures of TE radiant panel could sustain at the required range when the applied current equaled to 3 A. The temperatures of tested and simulated points are shown in Fig. 7.

Fig. 7 shows the experimental and theoretical transient temperature profile of TE radiant panel. The '$T_{\text{left}}$', '$T_{\text{middle}}$' and '$T_{\text{right}}$' curves respectively represent the 'Left', 'Middle' and 'Right' point temperature of the extracting element. They also represent the maximum, the middle and minimum temperature of the TE radiant panel. We could see that the surface temperature quickly decreased/increased with time, and finally reached stable value in the cooling/heating mode, respectively. This is because the Peltier heat is largest at first for its surface effect, the Peltier cooling occurs at the

surfaces of TEM and firstly cools the TE panel. However, the Joule heat occurs uniformly throughout the TEM. Therefore, when a power source is applied to the TEM, the Peltier cooling at the cold side occurs before the Joule heat reaches the cold end. The time for achieving the steady-state was about 35 minutes and it was in the required range at the steady-state, while the time for achieving the steady-state of traditional radiant air-conditioning system was larger than 1 hour[17; 21]. Therefore, the thermal response of TE panels is much faster than conventional hydronic panels so that the thermal inertial problem with RAC systems can be overcome to a large extent.

Comparing the simulation and experiment curves, the temperature profiles of numerical simulations well depicts the general trends as shown in the experiment tests. It finds the maximum temperature difference of radiant panel obtained in the experiment nearly equals to that of the simulation in the cooling mode, and the experiment and simulation curve of the minimum surface temperature in the heating mode are overlapped. Note that there is a little difference between simulation and experiment values: the experiment value is smaller than simulation value in the cooling mode and larger than simulation value in the heating mode, respectively. This is because three assumptions are introduced to simplify the simulation mode. And the total heat transfer coefficient ($h$) between the radiant ceiling and the room is mainly responsible for the difference between the experimental results and simulation results, because the actual total heat transfer coefficient changes with the TE panel surface temperature and indoor ambient temperature. It is very difficult to maintain its’ value

at constant in experimental condition as simulation. While the experimental results demonstrate our design data of TE radiant panel are feasible.

## 4. Conclusions
The design procedure and performance evaluation of TE radiant panel are studied. A thermal physical model of TE radiant panels is built in the cooling and heating mode. Using the critical temperature search approach method, the design data and thermal characters of thermoelectric radiant panel are discussed. The complex interactions between different parameters are also considered, and their variation ranges are identified. Combined the $COP_C/COP_H$ and cost, the best choice for TE radiant panel is that the thickness is set as 4 mm, and the number of TEM is set as 16 per square meter, respectively. Based on the optimal design values, the transient temperature distribution of TE radiant panel are investigated. It also found that the variation of surface temperature decreases along the direction away from the TEM. And the COP of TE-RAC is larger than the COP of conventional TE air-conditioning system, which illustrates that the TE-RAC system is a promising approach for enlarging the market of TE technology in large cooling field.

## ACKNOWLEDGEMENT
This work is jointly supported by the Natural Science Foundation of China (Grant No. 51506060 and 51376068) and the Fundamental Research Funds for the Central Universities (2016YXMS048). The supports are gratefully acknowledged.

### References:

[1] J. Zuo, Z. Zhao, Green building research - current status and future agenda: a review, Renew.
Sust. Energ. Rev. 30 (2014) 271-281.

[2] Z. Tian, S. Lee, G. Chen, Heat transfer in thermoelectric materials and devices, J. Heat
Transfer 135 (2013) 061605-061605.

[3] L.M. Shen, F. Xiao, H.X. Chen, S.W. Wang, Investigation of a novel thermoelectric radiant
air-conditioning system, Energy and Buildings 59 (2013) 123-132.

[4] D. Zhao, G. Tan, A review of thermoelectric cooling: materials, modeling and applications,
Applied Thermal Engineering 66 (2014) 15-24.

[5] Z. Liu, L. Zhang, G. Gong, Experimental evaluation of a solar thermoelectric cooled ceiling
combined with displacement ventilation system, Energy Conversion and Management 87
(2014) 559-565.

[6] C. Lertsatitthanakorn, W. Srisuwan, S. Atthajariyakul, Experimental performance of a
thermoelectric ceiling cooling panel, International Journal of Energy Research 32 (2008)
950-957.

[7] Z. Liu, L. Zhang, G. Gong, T. Han, Experimental evaluation of an active solar thermoelectric
radiant wall system, Energy Conversion and Management 94 (2015) 253-260.

[8] Y. Luo, L. Zhang, Z. Liu, Y. Wang, F. Meng, L. Xie, Modeling of the surface temperature
field of a thermoelectric radiant ceiling panel system, Applied Energy 162 (2016) 675-686.

[9] C. Kochendörfer, Standard testing of cooling panels and their use in system planning,
ASHRAE Transactions 102 (1996) 651-658.

[10] Z. Tian, X. Yin, Y. Ding, C. Zhang, Research on the actual cooling performance of ceiling
radiant panel, Energy and Buildings 47 (2012) 636-642.

[11] I. Atmaca, O. Kaynakli, A. Yigit, Effects of radiant temperature on thermal comfort, Building
and Environment 42 (2007) 3210-3220.

[12] M.S. Shin, K.N. Rhee, S.R. Ryu, M.S. Yeo, K.W. Kim, Design of radiant floor heating panel
in view of floor surface temperatures, Building and Environment 92 (2015) 559-577.

[13] B.W. Olesen, New european standards for design, dimensioning and testing embedded
radiant heating and cooling systems. in: O. Seppaenen, and J. Saeteri, (Eds.), Proceedings of
Clima 2007 WellBeing Indoors, FINVAC, Helsinki, Finland, 2007.

[14] D.M. Rowe, Thermoelectrics handbook macro to nano, CRC Press, Boca Raton,FL, 2005.

[15] P.D. Ariel, Generalized gear's method for computing the flow of a viscoelastic fluid,
Computer Methods in Applied Mechanics and Engineering 142 (1997) 111-121.

[16] L.M. Shen, F. Xiao, H.X. Chen, S.W. Wang, Numerical and experimental analysis of
transient supercooling effect of voltage pulse on thermoelectric element, International
Journal of Refrigeration 35 (2012) 1156-1165.

[17] R.D. Watson, K.S. Chapman, Radiant heating and cooling handbook, McGraw-Hill, New
York, 2002.

[18] Y.L. Yin, R.Z. Wang, X.Q. Zhai, T.F. Ishugah, Experimental investigation on the heat
transfer performance and water condensation phenomenon of radiant cooling panels,
Building and Environment 71 (2014) 15-23.

[19] ASHRAE, Ashrae handbook - hvac applications, American Society of Heating, Refrigerating,

and Air Conditioning Engineers, Atlanta, GA, 2011.

[20] Z.J. Wang, Low temperature radiant heating and radiant cooling, China Machine Press, Beijing, 2004.

[21] J. Miriel, L. Serres, A. Trombe, Radiant ceiling panel heating - cooling systems: experimental and simulated study of the performances, thermal comfort and energy consumptions, Applied Thermal Engineering 22 (2002) 1861-1873.

Figure Captions

Fig.1. The scheme of thermoelectric radiant air-conditioning system

Fig.2. The finite volume energy balance schematic of a TE radiant panel unit

Fig.3. The design procedure flow chart of TE radiant panel

Fig.4. The maximum cooling performance of TEM under different thermal resistance of outside heat exchanger

Fig.5. The maximum heating performance of TEM under different thermal resistance of outside heat exchanger

Fig.6. The selection criteria for design parameters of TE radiant panel

Fig.7. The test rig of TE radiant panel unit

Fig.8. Transient temperature distribution of TE radiant panel unit in (a) cooling mode and (b) heating mode

![](./images/811125987696705536_2.jpg)

Fig.1. The scheme of thermoelectric radiant air-conditioning system

![](./images/811125987696705536_3.jpg)

Fig.2. The finite volume energy balance schematic of a TE radiant panel unit

![](./images/811125987696705536_4.jpg)

![](./images/811125987696705536_5.jpg)

Fig.3. The design procedure flow chart of TE radiant panel

![](./images/811125987696705536_6.jpg)

(a) $\mathrm{T_c=17\ ^\circ C}$

![](./images/811125987696705536_7.jpg)

(b) $\mathrm{T_c=20\ ^\circ C}$

Fig.4. The maximum cooling performance of TEM under different thermal resistance of outside heat exchanger

![](./images/811125987696705536_8.jpg)

(a) $\mathrm{T_h=27\ ^\circ C}$

![](./images/811125987696705536_9.jpg)

(b) $\mathrm{T_h=100\ ^\circ C}$

Fig.5. The maximum heating performance of TEM under different thermal resistance of outside heat exchanger

![](./images/811125987696705536_10.jpg)

Fig.6. The selection criteria for design parameters of TE radiant panel

![](./images/811125987696705536_11.jpg)

Fig.7. The test rig of TE radiant panel unit

![](./images/811125987696705536_12.jpg)

Fig.8. Transient temperature distribution of TE radiant panel unit in (a) cooling mode
and (b) heating mode

### Table Captions

Table 1 The critical cooling capacities under different thickness and length of TE radiant panel

Table 2 The cooling and heating performance of TE panel (per square meter) when
$R_h$=1 $KW^{-1}$

<table>
<caption>Table 1 The critical cooling capacities under different thickness and length of TE radiant panel</caption>
<thead>
<tr>
<th>Thickness
(L<sub>t</sub>, mm)</th>
<th>Length
(L<sub>l</sub>, m)</th>
<th>Critical cooling capacity
per TEM (Q<sub>c</sub>, W)</th>
<th>Critical heating capacity per
TEM (Q<sub>h</sub>, W)</th>
<th>The number of TEM
per square meter(N)</th>
<th>Feasibility</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">2</td>
<td>0.1</td>
<td>8.14~9.57</td>
<td>6.78~83.00</td>
<td>25</td>
<td>YES</td>
</tr>
<tr>
<td>0.125</td>
<td>10.71~11.12</td>
<td>8.89~96.00</td>
<td>16</td>
<td>YES</td>
</tr>
<tr>
<td>0.133</td>
<td>11.53</td>
<td>9.63~99.60</td>
<td>16</td>
<td>YES</td>
</tr>
<tr>
<td rowspan="3">3</td>
<td>0.1</td>
<td>5.27~6.71</td>
<td>4.40~58.00</td>
<td>25</td>
<td>YES</td>
</tr>
<tr>
<td>0.125</td>
<td>6.83~7.93</td>
<td>5.67~68.70</td>
<td>16</td>
<td>YES</td>
</tr>
<tr>
<td>0.162</td>
<td>9.37</td>
<td>7.81~81.20</td>
<td>9</td>
<td>YES</td>
</tr>
<tr>
<td rowspan="4">4</td>
<td>0.1</td>
<td>3.91~5.16</td>
<td>3.25~44.60</td>
<td>25</td>
<td>YES</td>
</tr>
<tr>
<td>0.125</td>
<td>5.00~6.18</td>
<td>4.16~53.50</td>
<td>16</td>
<td>YES</td>
</tr>
<tr>
<td>1/6</td>
<td>7.02~7.58</td>
<td>5.84~65.50</td>
<td>9</td>
<td>NO</td>
</tr>
<tr>
<td>0.188</td>
<td>8.15</td>
<td>6.80~70.50</td>
<td>9</td>
<td>NO</td>
</tr>
<tr>
<td rowspan="3">5</td>
<td>0.1</td>
<td>3.10~4.20</td>
<td>2.59~36.30</td>
<td>25</td>
<td>YES</td>
</tr>
<tr>
<td>0.125</td>
<td>3.95~5.07</td>
<td>3.28~43.80</td>
<td>16</td>
<td>NO</td>
</tr>
<tr>
<td>0.210</td>
<td>7.30</td>
<td>6.08~63.00</td>
<td>4</td>
<td>NO</td>
</tr>
<tr>
<td rowspan="2">6</td>
<td>0.1</td>
<td>2.58~3.55</td>
<td>2.14~30.65</td>
<td>25</td>
<td>NO</td>
</tr>
<tr>
<td>0.227</td>
<td>6.62</td>
<td>5.46~57.16</td>
<td>4</td>
<td>NO</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 The cooling and heating performance of TE panel (per square meter) when $\mathrm{R_h=1\ KW^{-1}}$</caption>
<thead>
<tr>
<th>Thickness ($\mathrm{L_t}$, mm)</th>
<th>N</th>
<th>$\mathrm{I_c}$ (A)</th>
<th>$\mathrm{I_h}$ (A)</th>
<th>The cooling capacity of TE panel(W)</th>
<th>The heating capacity of TE panel(W)</th>
<th>$\mathrm{COP_c}$</th>
<th>$\mathrm{COP_h}$</th>
<th>Performance Evaluation</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">2</td>
<td>25</td>
<td>2.01~2.56</td>
<td>1.19~5.42</td>
<td>203.5~239</td>
<td>169.5~2075</td>
<td>0.58~0.84</td>
<td>0.48~1.68</td>
<td>Normal</td>
</tr>
<tr>
<td>16</td>
<td>/</td>
<td>1.34~5.67</td>
<td>/</td>
<td>142.2~1536</td>
<td>/</td>
<td>0.59~1.84</td>
<td>Bad</td>
</tr>
<tr>
<td>16</td>
<td>/</td>
<td>1.39~5.81</td>
<td>/</td>
<td>154.1~1539</td>
<td>/</td>
<td>0.62~1.89</td>
<td>Bad</td>
</tr>
<tr>
<td rowspan="3">3</td>
<td>25</td>
<td>1.37~1.94</td>
<td>1.01~4.50</td>
<td>131.8~67.75</td>
<td>110.0~1450</td>
<td>0.73~1.06</td>
<td>0.33~1.69</td>
<td>Good</td>
</tr>
<tr>
<td>16</td>
<td>1.68~2.36</td>
<td>1.11~4.90</td>
<td>109.3~126.9</td>
<td>90.72~1099</td>
<td>0.61~0.97</td>
<td>0.41~1.61</td>
<td>Normal</td>
</tr>
<tr>
<td>9</td>
<td>2.45~3.04</td>
<td>1.26~5.36</td>
<td>84.33</td>
<td>70.29~730.8</td>
<td>0.45~0.68</td>
<td>0.53~1.78</td>
<td>Normal</td>
</tr>
<tr>
<td rowspan="2">4</td>
<td>25</td>
<td>1.14~1.57</td>
<td>0.93~3.97</td>
<td>97.75~129.0</td>
<td>81.25~1115</td>
<td>0.81~1.06</td>
<td>0.26~1.79</td>
<td>Good</td>
</tr>
<tr>
<td>16</td>
<td>1.33~1.80</td>
<td>1.00~4.33</td>
<td>81.00~98.88</td>
<td>66.56~856.0</td>
<td>0.77~1.07</td>
<td>0.32~1.72</td>
<td>Good</td>
</tr>
<tr>
<td>5</td>
<td>25</td>
<td>1.03~1.38</td>
<td>0.88~3.63</td>
<td>81.00~105.0</td>
<td>64.75~907.5</td>
<td>0.78~1.07</td>
<td>0.21~1.87</td>
<td>Good</td>
</tr>
</tbody>
</table>

### Highlights

1. Design procedure of TE radiant panel is proposed.

2. Thermal physical model combined thermoelectric effect and radiation law is developed.

3. An optimization design configuration of TE radiant panel is presented and validated.

4. The temperature distribution uniformity of TE radiant panel are studied.

5. We discuss the thermal characterization representation approach of TE radiant.