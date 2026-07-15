# Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine

Xiuxiu Sun, Xingyu Liang, Gequn Shu, Hua Tian*, Haiqiao Wei, Xiangxiang Wang

State Key Laboratory of Engines, Tianjin University, Tianjin 300072, China

---

## ARTICLE INFO

**Article history:**
Received 9 January 2014
Received in revised form
5 September 2014
Accepted 12 September 2014
Available online xxx

**Keywords:**
Internal combustion engine
Thermoelectric generator
Performance
Optimization
Exhaust gas

---

## ABSTRACT

Models of two-stage serial and parallel thermoelectric generators have been established in this paper. Low-temperature thermoelectric material bismuth telluride and medium-temperature skutterudite are employed in the models and the exhaust gas of internal combustion engine is used as heat source. The properties of the thermoelectric materials are found to be temperature dependent. The performances including the output power, conversion efficiency and exergy efficiency vary with the temperatures of the heat and cold sources, the heat transfer coefficient between the hot and cold sides. The performances are influenced by the external resistances of the serial/parallel two-stage thermoelectric generators and the single-stage thermoelectric generator. The results show that the heat source temperature plays a key role in selection of the design of a thermoelectric generator when the heat transfer coefficient is more than $400\ \text{W/m}^2\ \text{K}$. The performances of the single-stage thermoelectric generator of thermoelectric material bismuth telluride is better than those of the two stage thermoelectric generator when the heat source temperature is less than 600 K; the maximum values of the output power and conversion efficiency of a serial two-stage thermoelectric generator are 10.9% and 12.4% higher, the maximum exergy efficiency is 12.5% higher than those of the single-stage one, when the temperature of the heat source is 800 K.

© 2014 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Environmental pollution and energy crisis have been attracting the world's attentions. The technologies of energy saving and emission reduction have been applied in various industries. The waste heat recovery has become one of important ways in automobile industry for energy saving and emission reduction. He et al. [1] made a steady-state heat balance test on FAW TOYOTA 8A-FE gasoline engine. The results showed that only about one third of a fuel's chemical energy was converted into effective work and the rest of the energy was wasted in the form of exhaust gas. Wang et al. [2] and Dolz et al. [3] analyzed the heat balance of Gasoline and Diesel engines and obtained similar results. That is to say, the quantity of the exhaust gas energy is promising. According to the research conducted by Wang et al. [4], the temperature of the exhaust gas was around $500\ ^\circ\text{C}$, which is of relatively high thermal quality. By effectively recycling the energy of the exhaust gas, the efficiency of ICE (internal combustion energy) can be improved, which would lead to huge economic and social benefits.

TEG (thermoelectric generation) as one of the ICE waste heat recovery technologies has an optimistic prospect [5], because it has small volume, light weight, no pollution and no moving parts. An ETEG (exhaust-based thermoelectric generator) has been developed since 1963. In the past 20 years, the thermoelectric power generation has become one of important research topics [6]. Hi-Z Company designed ETEG, which was able to produce 1 kW, but when it was applied in 14L, Cummins NTC 325 engine for the energy recovery, it was only able to produce 400 W. The target was met by the improved design [7]. Nissan company [8] used the self-developed 72 pieces of thermoelectric module recycling the energy of the gasoline engine exhaust gas, the research results showed that when vehicle climbing speed was 60 km/h, the exhaust temperature was 868 K, input and output temperatures of the TEG were 856 K and 791 K, the temperature difference was 65 K, the heat exchange efficiency of the generator from the primary exhaust gas energy flux was estimated to be 11%. The maximum temperature difference of both the hot and cold sides of the modules was 396 K and the minimum temperature difference was 372 K for the water cooling generators, the generated power through the generator was 0.9% of the energy of the heat flux, and the output power was

---

* Corresponding author. Tel.: +86 022 27406781.
E-mail addresses: thtju@tju.edu.cn, jeviwntian@tju.edu.cn (H. Tian).

http://dx.doi.org/10.1016/j.energy.2014.09.032
0360-5442/© 2014 Elsevier Ltd. All rights reserved.

---

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/j.energy.2014.09.032

35.6 W. The experimental results of 300 W produced by ETEG were published by Clarkson University and Delphi systems in 2004 in the research project funded by NYSERDA and the Department of En- ergy. The ETEG actually did not generate the most power since it was used in a light truck [9]. A TEG was developed by GM Ltd in the United States in 2008 in order to recycle the waste heat of the exhaust gas of an engine [10]. The test results of the TEG showed that under high speeds and the working conditions of FTP (federal test procedure), the thermoelectric generator was able to respec- tively recycle 350 W and 600 W of power. It was able to improve the fuel economy by nearly 5%. From a view of the current application of the thermoelectric generator in automobiles, thermoelectric generation has become one of methods for improving thermal ef- ficiency of internal combustion engines, in the major automobile companies of the developed countries. Since the output power and conversion efficiency of thermoelectric generation are low so that it is still in development and has not been widely used. In recent years, with the development of thermoelectric materials [11], application of thermoelectric generation technology in automo- biles has become one of hot research areas.

To improve the efficiency of TEG, TEM design of TEG has been studied in deep details. Shiho [12] derived an analytic model describing the internal temperature difference as a function of the load current of a TEG. Hsu et al. [13] constructed a system comprised of 24 TEGs to recover waste heat, and established a fundamental low-temperature waste heat TEG system. The TEG performance was also studied from the reversible to the irrevers- ible by some researchers. Gou et al. [14] established a TEG model based on basic principles of TEG and finite time thermodynamics. Crane et al. [15] developed steady-state and transient models in a MATLAB/Simulink environment for high-power-density TEG. Some of researchers studied TEG from the stationary-stage to the dynamic-stage. Tilmann et al. [16] developed a dynamic model of the exhaust gas heat exchanger employing the moving-boundary principle. Meng et al. [17] developed a complete, three- dimensional and transient model to investigate the dynamic response characteristics of TEG. Shu et al. [18] combined TEG with organic Rankine cycle to recover the waste heat of ICE. Wang et al. [19] developed a heat exchanger of thermoelectric generation for the two-stage optimization to improve the performance of TEG. The TEG output power density was increased by 88.70%. Weng et al. [20] explored the relationship between the power generation performance and the quantities of TEMs. It was found that imple- menting more TE (thermoelectric) couples does not necessarily generate more power in total. Sahin et al. [21] studied the perfor- mance of thermoelectric generator from the irreversible point of view. The output power and conversion efficiency of TEG has a close relationship with the entropy generation.

Wang et al. [4] presented a mathematical model of a TEG device using the vehicle exhaust gas as a heat source. This model demonstrated that using the phase-change thermoelectric material could improve the performance of TEG. It disclosed that the ZT value variation depended on the temperature variation. The ZT value of thermoelectric material was closely related to the output power. During the last 50 years, a fairly large number of semi- conductor materials for have been studied for thermoelectricity [11]. About ten of thermoelectric materials can be considered to have potentials for use in vehicular generators. Among these ten materials, appropriate couples of N- and P-type thermoelectric generators were selected, yielding a total of six couples of ther- moelectric generators. The heat source temperature is high when using TEG to recover the exhaust gas heat of ICE. That is to say, the temperature difference of the two sides in TEM is large. Considering the nature of thermoelectric material, a model of two-stage serial and parallel thermoelectric generator will be presented where the low-temperature thermoelectric material bismuth telluride and medium-temperature skutterudite are employed and the exhaust gas of internal combustion engine will be used as a heat source, which resolves the problem of the poor conversion efficiency of TEG. Chen et al. [22] showed that the effects of the thermocouple number and the heat transfer area on the performance of the TTEG (two-stage thermoelectric generator), which was subjected to the low temperature and the variation of the thermoelectric material property with temperature. The single-stage TEM (thermoelectric model), two-stage TEM and multi-stage TEM were studied on solar thermoelectric generator by Xiao et al. [23]. Reasonable thermal design of solar thermoelectric generator took a full advantage of the characteristics of thermoelectric materials and effectively improved the power generation performance. High performance of thermoelectric module can be achieved within the large tempera- ture difference by using a multi-stage thermoelectric module. In a word, it is possible to recover the exhaust waste heat of ICE using a two-stage TEG.

The performance characteristics of the single-stage and two- stage TEGs will be discussed in this paper where different condi- tions, including different temperatures of the heat and cold sources, different external resistance, and different the heat transfer co- efficients on the cold and heat sides are applied. Higher conversion efficiency of a TEG design is expected from this research work, which will provide a guidance or direction for TEG to recover the exhaust waste heat of ICE.

## 2. Model of thermoelectric generator

### 2.1. Model of single-stage thermoelectric generator

Fig. 1(a) shows the model of single-stage thermoelectric generator. The TEM (thermoelectric module) consists of a number of thermocouples and thermal ceramic. Each thermocouple is composed of the P-type and N-type semiconductor legs. The TEM absorbs heat from the heat source, and then the heat flows to the cold source through the thermocouples, which leads to the tem- perature difference on the two sides of the thermocouples. The heat energy is then transformed into electrical energy. The TEM is connected with external resistance to form a closed circuit. Since the thermocouples are serial, the current is same for each of the thermocouples.

### 2.2. Model of two-stage thermoelectric generator

Thermoelectric generator consists of a lot of thermoelectric modules combined in different forms (serial or parallel). The per- formance of one TEM will be simulated by MATLAB in this article. The two-stage TEG has two different forms: serial (Fig. 1(b)) and parallel (Fig. 1(c)) for the top and bottom stages. The difference between the two-stage TEG and TEG is that the two-stage TEG thermocouples have two layer arrangements, materials and quan- tity of thermocouples in the top and bottom stages can be different, which is different from the single-stage TEG. The current of the serial TTEG is same for the top and bottom stages, while the current of the parallel two-stage TEG is independent for each of the stages. The insulating ceramic piece is inserted between the two layers, it has good thermal conductivity. The model of the two-stage ther- moelectric generator is based on the materials of the medium- temperature skutterudite $(P/N,(Zn_{0.9975}Ge_{0.0025})Sb_{3}$ [24] $/Ba_{0.4}In_{0.4}Co_{4}Sb_{12}$ [25]) and the low-temperature bismuth tellu- ride $(Bi_{2}Te_{3})$ [26] using the exhaust gas of internal combustion engine as the heat source. $Bi_{2}Te_{3}$ can be used in the material of HZ-20. These materials have higher ZT value in the range of the middle and low temperatures than others.

---
Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/ j.energy.2014.09.032

![](./images/814689052753133569_1.jpg)

Fig. 1. Geometric model of the thermoelectric generators: (a) single-stage thermoelectric generator, (b) serial two-stage thermoelectric generator, (c) parallel two-stage thermoelectric generator.

### 2.3. Material properties

Table 1 lists the parameters for the PN materials used in this paper. The Seebeck coefficient, electrical resistivity and thermal conductivity change with the temperature (see in references).

### 2.4. Boundary conditions

The following hypotheses are made in this paper:

(1) Heat conduction flows along the direction of the thermal couple leg. The heat conduction in the axial direction and the heat radiation are neglected.
(2) The thermal conductivity, electrical conductivity, and See- beck coefficient of the material change with the average temperature of the two sides of the thermocouple.
(3) Both the thermal and gas flow are steady.
(4) The temperature of the low-temperature end of the top stage is the same as that of the high-temperature end of the bot- tom stage.
(5) Thermal contact resistance is ignored.

The other parameters such as the cold source temperature and heat transfer coefficient are listed in Table 2. The exhaust gas and coolant flow through the surface of the two-stage TEG. The heat is transferred from the hot source at the temperature of $T_{h}$, and released at the temperature of $T_{c}$. A part of the absorbed heat is transformed into electricity through the two-stage TEG in this process. The size of TEM is so small that the temperature difference of the thermocouples in TEG is negligible. In other subsequent analysis, without special description, the parameters are taken from Tables 1 and 2 The assumption temperatures lie in these ranges when the effect of temperature of heat and cold source is researched on the performance of two-stage TEG. The values of heat transfer coefficient are also assumed in the range of changing. These values are reasonable for researching the performance of two-stage TEG in steady state.

### 3. Mathematical model of thermoelectric generator

Heat transfer process can be divided into three parts, from the heat source to the TEM, the TEM internal, and from the TEM to the cold source. According to the hypothesis, the mathematical model of a serial TTEG is developed as below.

The hot and cold sources will be formed on the surfaces. Assuming that the heat-transfer between the hot and cold junc- tions of the TEG and their hot and cold sources conform the New- ton's law [22], of which, the equations are given by

<table>
<caption>Table 1 Parameters of PN materials.</caption>
<thead>
<tr>
<th rowspan="2">Parameters</th>
<th colspan="2">Two-stage TEG (serial/parallel)</th>
<th colspan="2">Single-stage TEG</th>
</tr>
<tr>
<th>P</th>
<th>N</th>
<th>P</th>
<th>N</th>
</tr>
</thead>
<tbody>
<tr>
<td>Height $l$ [m]</td>
<td>0.003</td>
<td>0.003</td>
<td>0.006</td>
<td>0.006</td>
</tr>
<tr>
<td>Sectional area A [m²]</td>
<td>0.00248 (m²)</td>
<td>0.00248 (m²)</td>
<td>0.00248 (m²)</td>
<td>0.00248 (m²)</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Other parameters.</caption>
<tbody>
<tr>
<td>Exhaust gas temperature [K]</td>
<td>500/800</td>
</tr>
<tr>
<td>Cooling water temperature [K]</td>
<td>353.15</td>
</tr>
<tr>
<td>Heat transfer coefficient in hot side [W/m² K]</td>
<td>800</td>
</tr>
<tr>
<td>Heat transfer coefficient in hot side [W/m² K]</td>
<td>1000</td>
</tr>
<tr>
<td>Heat transfer area [m²]</td>
<td>0.005625</td>
</tr>
<tr>
<td>Ratio of external resistance to internal resistance</td>
<td>1</td>
</tr>
</tbody>
</table>

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/j.energy.2014.09.032

$$q_{1}=k_{1}F_{1}(T_{\mathrm{h}}-T_{1}) \tag{1}$$

$$q_{2}=k_{2}F_{2}(T_{2}-T_{\mathrm{c}}) \tag{2}$$

The heat rate consists of the Peltier heat, the conducted heat, and the Joule heat by the two-stage TEG per unit time, whereas the heat generated by the Thomson effect is ignored because the Thomson heat is negligible. The generated Joule heat is distributed homogenously on the two sides of the thermocouple. The ther- mocouples of the two stages are arranged serially, such that the heat rate is proportional to the number of the thermocouples. The current in the two stages is same. In this study, different materials are applied to the top and bottom modules. The characteristics of the materials vary with temperature. Based on the aforementioned assumptions, the heat rate from the top stage is the same as the heat rate with the bottom stage.

The following equations are applied to the internal heat transfer of the TEM while the heat loss of the ceramic medium is ignored:

$$q_{1}=\left(\alpha_{1}IT_{1}-\frac{I^{2}R_{1}}{2}+K_{1}(T_{1}-T_{3})\right)m \tag{3}$$

$$q_{3}=\left(\alpha_{1}IT_{3}+\frac{I^{2}R_{1}}{2}+K_{1}(T_{1}-T_{3})\right)m \tag{4}$$

$$q_{3}=\left(\alpha_{2}IT_{3}-\frac{I^{2}R_{2}}{2}+K_{2}(T_{3}-T_{2})\right)n \tag{5}$$

$$q_{2}=\left(\alpha_{2}IT_{3}+\frac{I^{2}R_{2}}{2}+K_{2}(T_{3}-T_{2})\right)n \tag{6}$$

However, the open circuit voltage of the two-stage TEG is the sum of the open circuit voltage of the top and bottom layers. The open circuit voltage of the thermocouple is equal to the product of the Seebeck coefficient and temperature difference. The total resistance is equal to the sum of external and inner resistance, which is proportional to the number of thermocouples. Thus, the current is expressed as follows:

$$I=\frac{mU_{1}+nU_{2}}{mR_{1}+nR_{2}+R_{\mathrm{L}}}=\frac{m\alpha_{1}(T_{1}-T_{3})+n\alpha_{2}(T_{3}-T_{2})}{mR_{1}+nR_{2}+R_{\mathrm{L}}} \tag{7}$$

A thermocouple is treated as a unit based on the assumptions. The properties of the P-leg and N-leg depend on the average temperature of the individual materials. The property of a PN unit at the top and bottom stages is described by the following equations:

$$\begin{aligned}
\alpha_{1} & =\alpha_{p1}-\alpha_{n1} \\
K_{1} & =\frac{\lambda_{p1}A_{p1}}{l_{p1}}+\frac{\lambda_{n1}A_{n1}}{l_{n1}} \\
R_{1} & =\frac{\rho_{p1}l_{p1}}{A_{p1}}+\frac{\rho_{n1}l_{n1}}{A_{n1}}
\end{aligned} \tag{8}$$

$$\begin{aligned}
\alpha_{2} & =\alpha_{p2}-\alpha_{n2} \\
K_{2} & =\frac{\lambda_{p2}A_{p2}}{l_{p2}}+\frac{\lambda_{n2}A_{n2}}{l_{n2}} \\
R_{1} & =\frac{\rho_{p2}l_{p2}}{A_{p2}}+\frac{\rho_{n2}l_{n2}}{A_{n2}}
\end{aligned} \tag{9}$$

The heat released rate of the hot source is equivalent to the heat generation rate of the two-stage TEG without considering the energy loss. Meanwhile, the heat rate of the cold fluid is also the same as the heat rate from the two-stage TEG. $T_{3}$ is given by

$$T_{3}=\frac{1}{2} \frac{ml^{2}R_{1}+2mK_{1}T_{1}+nl^{2}R_{2}+2nK_{2}T_{2}}{mK_{1}+nK_{2}+n\alpha_{1}-m\alpha_{2}} \tag{10}$$

The expression of $T_{3}$ is input into Equations (1-3) and (6) so that solves $T_{1}$ and $T_{2}$ from these equations by a MATLAB code from which the output power and conversion efficiency of the two-stage TEG can then be determined. A part of the exhaust heat energy is transformed into electricity by TEG. The output power and con- version efficiency are presented in Equations (11) and (12).

$$P=I^{2}R_{\mathrm{L}}=q_{1}-q_{2} \tag{11}$$

$$\eta=\frac{P}{q_{1}} \tag{12}$$

The TTEG works in the between heat source with temperature of $T_{\mathrm{h}}$ and cold source with temperature of $T_{\mathrm{c}}$. The TTEG will be as a system, so the maximum output power of this system through reversible engine can be defined as exergy $(E)$.

The exergy $(E)$ of the system is then given by

$$E=\left(1-\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}}\right)q_{1} \tag{13}$$

The second-law efficiency of the system, also referred to as the exergy efficiency, which is the ratio of the output power of TTEG, which is produced through external resistance, and the exergy.

So, the exergy efficiency can be defined as:

$$\eta_{\mathrm{e}}=\frac{P}{E} \tag{14}$$

As the heat transfer modes of the serial and parallel two-stage TEG are same, so their heat transfer equations of the serial TTEG and parallel TTEG are same. The current calculation equations of the serial TTEG and parallel TTEG are different. This is because voltage is generated from the independent top and bottom layers of the parallel two-stage TEG.

The calculation equations of the currents of the top and bottom stages are given by:

$$I_{1}=\frac{mU_{1}}{mR_{1}+R_{\mathrm{L}1}}=\frac{m\alpha_{1}(T_{1}-T_{3})}{mR_{1}+R_{\mathrm{L}1}} \tag{15}$$

$$I_{2}=\frac{nU_{2}}{nR_{2}+R_{\mathrm{L}2}}=\frac{n\alpha_{2}(T_{3}-T_{2})}{nR_{2}+R_{\mathrm{L}2}} \tag{16}$$

The mathematical model of the single-stage TEG is similar to that of the two-stage TEG. The material property is also dependent on the temperature. The heat transfer equations of the single-stage TEG are same as those of the two-stage TEG for the heat from the hot source to the TEM internal and from the TEM internal to the cold source. The heat transfer equations of the TEM internal are given by:

$$q_{1}=\left(\alpha_{1}IT_{1}-\frac{I^{2}R_{1}}{2}+K_{1}(T_{1}-T_{3})\right)m \tag{17}$$

$$q_{2}=\left(\alpha_{1}IT_{3}+\frac{I^{2}R_{1}}{2}+K_{1}(T_{1}-T_{3})\right)m \tag{18}$$

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/ j.energy.2014.09.032

![](./images/814689052753133569_2.jpg)
![](./images/814689052753133569_3.jpg)

Fig. 2. Validation of the numerical model with the previously published data [22] for TEG. (a): output power; (b): conversion efficiency.

![](./images/814689052753133569_4.jpg)

Fig. 3. Dependence of the output power on the heat source temperature.

### 4. Model validation

Numerical results are validated by comparing the values of power and conversion efficiency with in the research of Chen et al. [22]. The materials are the same at both stages, and the property of the material is set as a constant at different temperatures. For example, the Seebeck coefficient is $2.3 \times 10^{-4}$ V/K and the total internal electrical resistance of the thermocouple is $1.4 \times 10^{-3} \Omega$ m. The temperature of the heat source is 600 K, and the cold side temperature is 300 K. The transfer coefficient and heat transfer areas of the two heat exchangers are also constant. As shown in Fig. 2, good agreement is achieved between the present results and those in the research of Chen et al. [22]. Thus, the proposed model in this paper is reasonable.

### 5. Results and discussion

#### 5.1. The system performance comparison of different hot source temperatures

Based on the low-temperature material $Bi_2Te_3$, the single-stage TEG cannot withstand the high temperature of the hot source, so the performance can be calculated for the temperatures below 600 K of the hot source. The property parameters of the materials are given in Table 1. The temperature of the hot source changes from 400 K to 900 K, the other parameters remain unchanged (see Table 2). The system is assumed as steady state when the parameter varied. So, the equation of exergy can be used in all the simulation conditions.

The output power variation with the exhaust gas temperature is shown in Fig. 3. Fig. 4 shows the variation of the conversion and exergy efficiencies. The performance of the single-stage TEG based on the lower-temperature material $Bi_2Te_3$ is better than that of the two-stage TEG for the temperature blow 600 K of the hot source. However the single-stage TEG cannot work at high temperatures of the hot source. The output power and conversion efficiency of the

![](./images/814689052753133569_5.jpg)
![](./images/814689052753133569_6.jpg)

Fig. 4. Dependence of the conversion efficiencies and exergy efficiencies on the heat source temperature.

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/ j.energy.2014.09.032

![](./images/814689052753133569_7.jpg)

Fig. 5. Dependence of thermocouples two ends temperature on the heat source temperature.

![](./images/814689052753133569_8.jpg)

Fig. 6. Dependence of the output power on the cold source temperature.

single-stage TEG with the thermoelectric material $Bi_2Te_3$ were
2.87 W and 4.15% when the hot source temperature was 500 K. At
this time, the performance of the single stage TEG was better than
the serial TTEG, as the output power and conversion efficiency of
the serial two stage TEG were 2.5 W and 3.4%. When the hot source
temperature rises from 600 K to 800 K, the output power of the
parallel TTEG would increase from 6.78 W to 19.52 W and the
conversion efficiency would increase from 5.54 % to 8.34 %. How-
ever, the output power and conversion efficiency of the serial two-
stage TEG would change from 6.5 W to 19.02 W and from 5.38 % to
8.11 %, which were less than those of the parallel two-stage TEG, but
higher than the output power and conversion efficiency of the
single-stage skutterudite TEG, which would change from 5.12 W to
17.18 W and from 4.03 % to 4.88 %. As the hot source temperature
increased, the conversion efficiency difference of the TTEG and
single-stage TEG would be increase first and then decrease. The
performances of the serial and parallel TTEG were very close. From
the exergy efficiency perspective, the performance of the single-
stage TEG based on the lower-temperature material $Bi_2Te_3$ is bet-
ter than that of the others when the hot source temperature is
below 600 K. The exergy efficiency of the parallel two-stage TEG is
higher than that of the others as shown in Fig. 4(b), however, the
trend of The two-stage TEG exergy efficiency tend to be flat. The
exergy efficiency of two-stage TEGs change from 8 % to 15 % when
the heat source temperature increases from 400 K to 900 K. How-
ever, the exergy efficiency of ORC (organic Rankine cycle) ranges
from 15 % to 24 % under different working conditions [27], which is
higher than that of two-stage TEG. The main reason of the low
exergy efficiency of TEG is that the temperature difference is large
between two ends of two-stage TEG, which can make the exergy
loss increase. The hot source temperature is very important for
selection of the TEG designs.

Fig. 5 shows the temperature of the two ends of the thermo-
couples versus the hot source temperature. The larger the ZT value
is, the higher the output power will be. The temperature of the two
ends of the thermocouples is almost same for the single and two-
stage TEG of the same hot source temperature, but the ZT value
of different materials are different. The ZT value of $Bi_2Te_3$ is higher
than that of the skutterudite when the average temperature of the
thermocouples is about 400 K. The different ZT value causes the
different performances of TEGs when the other parameters are
same. The ZT values of the two types of thermoelectric materials
are higher than that of the single material, at the hot source tem-
perature above 600 K. So the two-stage TEG performance is better
than that of the single-stage TEG using the engine exhaust gas as a
hot source.

### 5.2. The system performance comparison at different cold source temperatures

In the above discussion, the performances of three types of
different TEG designs have been discussed as the hot source tem-
perature changes. The analysis is the foundation for studying the
effect of the cold source temperature. The performance of the two-
stage TEG has been improved, as the hot source temperature

![](./images/814689052753133569_9.jpg)

Fig. 7. Dependence of the conversion efficiencies and exergy efficiencies on the cold source temperature.

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering
the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/
j.energy.2014.09.032

![](./images/814689052753133569_10.jpg)

Fig. 8. Dependence of thermocouples two ends temperature on the cold source temperature.

![](./images/814689052753133569_11.jpg)

Fig. 9. Dependence of the output power on the heat transfer coefficient in heat side.

increases. One of the reasons is the high hot source temperature. So the hot source temperatures of 500 K and 800 K are chosen for the following studies.

Fig. 6 shows that the output power of the three different TEG designs with the varied cold source temperature and the two hot source temperatures of 800 K and 500 K. The variations of conversion and exergy efficiency versus the temperature of the cold source are shown in Fig. 7. When the cold source temperature varied at the hot source temperature of 500 K, the output power and conversion efficiency of the single-stage TEG based on low-temperature material $Bi_2Te_3$ decrease from 6.7 W to 2.46 W and from 6.44 % to 3.82 %. However, the performance of the two-stage TEG is poor in this case. The output power and conversion efficiency of the parallel TTEG are reduced from 5.53 W to 2.12 W and from 5.09 % to 3.17 %. The single-stage TEG based on skutterudite material is worst. When the hot source temperature is 800 K, the difference of the output power and conversion efficiency between the two-stage TEG and single-stage TEG increases. However, the difference decreases as the cold source temperature increases, the difference of output power and conversion efficiency between the parallel TTEG and the single-stage TEG decrease from 6.19 W to 1.89 W and from 2.56 % to 0.86 %. With a lower cold source temperature, the single-stage TEG has higher output power and conversion efficiency. However, the exergy efficiencies of the single-stage TEGs based on the $Bi_2Te_3$ and skutterudite have different trends, and the exergy efficiency of the two-stage TEG is not changed with increasing cold source temperature under the hot source temperature of 500 K (see Fig. 7(b)). The single-stage TEG based on the $Bi_2Te_3$ has higher exergy efficiency than that of the other TEG designs. The performance of the parallel two-stage TEG is slightly better than that of the serial two-stage TEG.

In fact, the decrease of the cold source temperature reduces the cold side temperature of the thermocouple (see Fig. 8), although the cold source temperature is limited by the environment. The hot and cold sides' temperatures of the thermocouples are almost same for the analyzed TEGs at the same hot and cold source temperatures, but the ZT values of the materials are different. The performance of the TEG is associated with the ZT value. Therefore the cooling water of the internal combustion engine is recommended to be the cold source of the TEG.

### 5.3. The system performance comparison for different heat transfer coefficients on the hot side

It can be seen from the previous analysis that, the cold source temperature does not affect the selection of the TEG designs; therefore the cooling water can be used as the cold source. In this section, the hot source temperature is assumed to be 500 K and 800 K to illustrate advantages of the two-stage TEG under a high hot source temperature.

Fig. 9 shows that the output power versus the heat transfer coefficient on the hot side. The variations of conversion efficiency and exergy efficiency are shown in Fig. 10. The output power and efficiency increase as the heat transfer coefficient increases, but the

![](./images/814689052753133569_12.jpg)

Fig. 10. Dependence of the conversion efficiencies and exergy efficiencies on the heat transfer coefficient in heat side.

![](./images/814689052753133569_13.jpg)

Fig. 11. Dependence of thermocouples two ends temperature on the heat transfer coefficient in heat side.

![](./images/814689052753133569_14.jpg)

Fig. 12. Dependence of the output power on the heat transfer coefficient in cold side.

trends of the conversion and exergy efficiency curves increase slowly when the heat transfer coefficient is above one point. When the hot source temperature is 500 K, the heat transfer coefficient increases from $50\ \text{W/m}^2\ \text{K}$ to $400\ \text{W/m}^2\ \text{K}$, the output power and conversion efficiency of the single-stage $\text{Bi}_2\text{Te}_3$ material TEG increase from 0.47 W to 2.39 W, and from 1.75 % to 3.8 %. But when the heat transfer coefficient rises to $1000\ \text{W/m}^2\ \text{K}$, the output power and conversion efficiency can only increase up to the limits of 2.98 W and 4.22%. When the heat transfer coefficient increases from $50\ \text{W/m}^2\ \text{K}$ to $400\ \text{W/m}^2\ \text{K}$, then to $1000\ \text{W/m}^2\ \text{K}$, the output power and conversion efficiency of the parallel TTEG increase from 0.35 W to 2 W, then to 2.57 W, and from 1.29 % to 3.08 %, then to 3.9%. That is to say, the trend increases lowly when the heat transfer coefficient is more than $400\ \text{W/m}^2\ \text{K}$, which is independent of the hot source temperature. When the hot source temperature is 800 K, the output power and conversion efficiency of the serial and parallel two-stage TEG are higher 14.4%, 18% and 16.6%, 20.1%. From the exergy efficiency perspective (Fig. 10(b)), the performance of the parallel is also slightly higher than that of the serial two-stage TEG. However the exergy efficiency of the single-stage TEG based on the low-temperature materials $\text{Bi}_2\text{Te}_3$ is much higher than that of the other TEG design in the same range of the heat transfer coefficient value on the hot side.

The hot side temperature of the thermocouples increases quickly, then slowly as the heat transfer coefficient increases (see Fig. 11). The trend of the middle temperature is similar to that of the two-stage TEG, leading to a quick and large temperature difference. The voltage is proportional to the temperature difference, so the current increases quickly. The output power is proportional to the square of the current, so the output power increases quickly when the heat transfer coefficient is less than $400\ \text{W/m}^2\ \text{K}$. Of course, the ZT value plays a key role for this phenomenon.

### 5.4. The system performance comparison of for different heat transfer coefficients on the cold side

Fig. 12 shows that the output power versus the heat transfer coefficient on the cold side. The variations of the conversion efficiency and exergy efficiency are shown in Fig. 13. The performance of the single-stage TEG based on the material skutterudite is better than that of the TTEG for the heat transfer coefficient lower than $400\ \text{W/m}^2\ \text{K}$ when the hot source temperature is 800 K. When the hot source temperature is 500 K, the output power and conversion efficiency of the single-stage TEG based on material $\text{Bi}_2\text{Te}_3$ is higher than those of the other TEG designs. The exergy efficiency of the single-stage TEG under the hot source temperature of 500 K is higher than that under the hot source temperature of 800 K, when the heat transfer coefficient is below $650\ \text{W/m}^2\ \text{K}$ on the cold side. The performance of the single-stage TEG is relatively poor when the heat transfer coefficient is below $50\ \text{W/m}^2\ \text{K}$ on the cold side.

The cold side temperature of the thermocouples in the bottom stage decreases as the heat transfer coefficient increase (see Fig. 14). At this time, the temperature difference of the hot and cold sides of the two-stage TEG is small, because the cold side temperature becomes higher when the heat transfer coefficient is less than 400 W/

![](./images/814689052753133569_15.jpg)

Fig. 13. Dependence of the conversion efficiencies and exergy efficiencies on the heat transfer coefficient in cold side.

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/ j.energy.2014.09.032

![](./images/814689052753133569_16.jpg)

Fig. 14. Dependence of thermocouples two ends temperature on the heat transfer coefficient in cold side.

![](./images/814689052753133569_17.jpg)

Fig. 15. Dependence of the output power on the external resistance.

$\mathrm{m}^{2} \mathrm{~K}$. It is also because the ZT value of $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ is lower than that of the skutterudite when the temperature of thermocouples is high in the bottom stage. When the heat transfer coefficient increases, the cold side temperature of the thermocouples in the bottom stage decreases, the temperature difference of the hot and cold sides of the two-stage TEG increases. This makes the performance of the two-stage TEG better than that of the single-stage TEG gradually. The thermoelectric material $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ is recommended for use in the low temperatures. The performance of the parallel TTEG is slightly higher than that of the serial two-stage TEG. In general, the heat transfer coefficient of the cooling water is large. The advantage of the TTEG is more obvious from using the cooling water than using other mediums as the cold source.

### 5.5. The system performance comparison for different external resistances

In the above sections, the effect of the parameters of the chosen TEG designs has been analyzed. It can be seen that the performance of the two-stage TEG is better than that of the single TEG using the engine exhaust gas and cooling water as hot and cold sources. All the simulations were conducted under the condition that the internal resistance was equal to the external resistance where the effect of the external resistance was studied. In fact, the effect of the external resistance needs to be considered.

Fig. 15 shows that the output power versus the external resistance. The variations of conversion efficiency and exergy efficiency are shown in Fig. 16. The trend of the output power curve is like a parabola versus the external resistance. There exists an optimum external resistance, which leads to an optimum output power. The trend of conversion efficiency is similar to that of the output power. In fact, the external resistances are different for the maximum output power and maximum conversion efficiency. When the hot source temperature is 500 K, the maximum output power and conversion efficiency of the single-stage TEG based on material $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ are 2.85 W and 4.28%. However, the output power and conversion efficiency values of the two-stage TEG are lower, the maximum output power and conversion efficiency of the serial and parallel two-stage TEG are 2.34 W, 2.46 W and 3.37%, 3.51%. When the hot source temperature is 800 K, the maximum conversion efficiencies of the serial and parallel two-stage TEG are higher than those of the single-stage TEG based on the material skutterudite, which are 13.6% and 17.2%. The performance of the serial two-stage TEG is worse than that of the parallel TTEG, the maximum output power and conversion efficiency of the serial TTEG are 2.4% and 2.3% less than those of the parallel TTEG. The variation of exergy efficiency is similar to that of the conversion efficiency, but different from the variation of the single-stage TEG based on the low-temperature material $\mathrm{Bi}_{2} \mathrm{Te}_{3}$. That is to say: the external resistance has an important effect on the chosen TEG design.

### 6. Conclusion

A model of the two-stage thermoelectric generator including the serial and parallel forms is established. The model is based on the low-temperature thermoelectric material bismuth telluride

![](./images/814689052753133569_18.jpg)

Fig. 16. Dependence of the conversion efficiencies and exergy efficiencies on the external resistance.

Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/j.energy.2014.09.032

and medium-temperature skutterudite and to use the engine exhaust gas as the hot source. Performance analysis under different operating conditions has been carried out. The results show that the performance of the two-stage TEG is better than that of the single-stage TEG when the hot source temperature is high, except for the condition of the heat transfer coefficient on the cold side less than $400\ \text{W/m}^2\ \text{K}$. Because the exergy efficiency of the single-stage TEG based on low-temperature material $\text{Bi}_2\text{Te}_3$ is higher than that of TTEG, under the heat source temperature of $800\ \text{K}$. Performance of the single-stage TEG with the material $\text{Bi}_2\text{Te}_3$ is better than that of the other TEG designs for the low temperature hot source. The hot source temperature plays a decisive role in selection of the TEG design. The performance of the parallel TTEG is better than that of the serial TTEG, but the parallel TTEG is more complicated when connected with other circuit elements. As manufacturing technology develops, the two-stage thermoelectric generator for a recovery of the engine exhaust gas waste heat will have a good application prospects.

## Acknowledgments
This work was supported by the National Basic Research Program of China (973 Program, No. 2011CB707201), the National Nature Science Foundation of China (No. 51206117), and Natural Science Foundation of Tianjin (No. 12JCQNJC04400). The authors gratefully acknowledge them for support of this work.

## Nomenclature

### Abbreviation
| TE   | thermoelectric                                     |
|------|---------------------------------------------------|
| TEG  | thermoelectric generator                           |
| ICE  | internal combustion energy                         |
| TEM  | thermoelectric module                              |
| TTEG | two-stage thermoelectric generator                 |
| ZT   | thermoelectric figure of merit, a property of thermoelectric materials |

### Symbols
| $q$   | heat rate [W]                                  |
|-------|------------------------------------------------|
| $P$   | output power [W]                               |
| $\eta$| conversion efficiency [%]                       |
| $T$   | temperature [K]                                |
| $R$   | resistance [$\Omega$]                          |
| $R_\text{L}$ | external resistance [$\Omega$]                |
| $k$   | heat transfer coefficient [$\text{W/m}^2\ \text{K}$] |
| $F$   | heat transfer area [$\text{m}^2$]              |
| $\alpha$ | Seebeck coefficient [V/K]                     |
| $I$   | current [A]                                    |
| $\lambda$ | thermal conductivity [W/m. K]                 |
| $M$   | the total number of thermocouples              |
| $m$   | number of thermocouples in top stage           |
| $n$   | number of thermocouples in bottom stage        |
| $U$   | voltage [V]                                    |
| $l$   | length of thermocouple [m]                     |
| $A$   | cross sectional area of thermocouple [$\text{m}^2$] |
| $\rho$ | electric resistivity [$\Omega\ \text{m}$]      |

### Subscript
| 1 | hot side                |
|---|-------------------------|
| 2 | cold side               |
| 3 | medium layer            |
| P | P leg of thermocouple   |
| N | N leg of thermocouple   |
| h | heat source             |
| c | cold source             |

## References
[1] He MG, Zhang XX, Zeng K, Gao KA. combined thermodynamic cycle used for waste heat recovery of internal combustion engine. Energy 2011;36(12):6821-9.

[2] Wang EH, Zhang HG, Zhao Y, Fan BY, Wu YT, Mu QH. Performance analysis of a novel system combining a dual loop organic Rankine cycle (ORC) with a gasoline engine. Energy 2012;43(1):385-95.

[3] Dolz V, Novella R, Garcia A, Sanchez J. HD diesel engine equipped with a bottoming Rankine cycle as a waste heat recovery system. Part 1: study and analysis of the waste heat energy. Appl Therm Eng 2012;36:269-78.

[4] Wang YC, Dai CS, Wang SX. Theoretical analysis of a thermoelectric generator using exhaust gas of vehicles as heat source. Appl Energy 2013;112:1171-80.

[5] Liang XY, Sun XX, Shu GQ, Sun K, Wang X, Wang XL. Using the analytic network process (ANP) to determine method of waste energy recovery from engine. Energy Convers Manag 2013;66:304-11.

[6] Saqr KM, Mansour MK, Musa MN. Thermal design of automobile exhaust based thermoelectric generators: objectives and challenges. Int J Automot Technol 2008;9(2):155-60.

[7] Kushch AS, Bass JC, Ghamaty S, Elsner NB. Thermoelectric development at Hi-Z technology. In: Proc.. 20th int. Conf. Thermoelectrics, Beijing, China; 2001. p. 422-30.

[8] Ikoma K, Munekiyo M, Furuya K, Kobayashi M, Izumi T, Shinohara K. Thermoelectric module and generator for gasoline engine vehicle. In: Proc.. 20th int. Conf. Thermoelectrics, IEEE, Nagoya, Japan; 1998. p. 464-7.

[9] Thacher EF, Helenbrook BT, Karri MA, Richter CJ. Testing of an automobile exhaust thermoelectric generator in a light truck. Proc Inst Mech Eng Part D J Automob Eng 2007;221(1):950-1007.

[10] Yang JH. Development of thermoelectric technology for automotive waste heat recovery. 2008 DOE Vehicle Technologies Annual Merit Review, Bethesda, MD. 2008.

[11] Anatchuk LI, Kuz RV. Materials for vehicular thermoelectric generators. J Electron Mater 2012;41(6):1778-84.

[12] Kim S. Analysis and modeling of effective temperature differences and electrical parameters of thermoelectric generators. Appl Energy 2013;102:1458-63.

[13] Hsu CT, Huang GY, Chu HS, Yu B, Yao DJ. Experiments and simulations on low-temperature waste heat harvesting system by thermoelectric power generators. Appl Energy 2011;88(4):1291-7.

[14] Gou XL, Xiao H, Yang SW. Modeling, experimental study and optimization on low-temperature waste heat thermoelectric generator system. Appl Energy 2010;87(10):3131-6.

[15] Crane DT, Koripella CR, Jovovic V. Validating steady-state and transient modeling tools for high-power-density thermoelectric generators. J Electron Mater 2012;41(6):1524-34.

[16] Horst TA, Rottengruber HS, Seifert M, Ringler J. Dynamic heat exchanger model for performance prediction and control system design of automotive waste heat recovery systems. Appl Energy 2013;105:293-303.

[17] Meng JH, Zhang XX, Wang XD. Dynamic response characteristics of thermoelectric generator predicted by a three-dimensional heat-electricity coupled model. J Power Sources 2014;245(0):262-9.

[18] Shu GQ, Zhao J, Tian H, Liang XY, Wei HQ. Parametric and exergetic analysis of waste heat recovery system based on thermoelectric generator and organic Rankine cycle utilizing R123. Energy 2012;45(1):806-16.

[19] Wang CC, Hung CI, Chen WH. Design of heat sink for improving the performance of thermoelectric generator using two-stage optimization. Energy 2012;39(1):236-45.

[20] Weng CC, Huang MJ. A simulation study of automotive waste heat recovery using a thermoelectric power generator. Int J Therm Sci 2013;71:302-9.

[21] Sahin AZ, Yilbas BS. Thermodynamic irreversibility and performance characteristics of thermoelectric power generator. Energy 2013;55:899-904.

[22] Chen LG, Li J, Sun FR, Wu C. Performance optimization of a two-stage semiconductor thermoelectric-generator. Appl Energy 2005;82(4):300-12.

[23] Xiao JS, Yang TQ, Li P, Zhai PC, Zhang QJ. Thermal design and management for performance optimization of solar thermoelectric generator. Appl Energy 2012;93:33-8.

[24] Wang SY. The preparations and thermoelectric properties of P-and n-type materials for 400-650 K Power generations. Doctoral thesis. Wuhan University of Technology; 2012.

[25] Zhou HY. The design and properties of $\text{Bi}_2\text{Te}_3$/$\text{CoSb}_3$ thermoelectric generator with wide temperature range. Master thesis. Wuhan University of Technology; 2012.

[26] www.hi-z.com/. Hi-Z technology. INC. 30/6/2014.

[27] Yu GP, Shu GQ, Tian H, Wei HQ, Liu LN. Simulation and thermodynamic analysis of a bottoming Organic Rankine Cycle (ORC) of diesel engine (DE). Energy 2013;51:281-90.

---
Please cite this article in press as: Sun X, et al., Comparison of the two-stage and traditional single-stage thermoelectric generator in recovering the waste heat of the high temperature exhaust gas of internal combustion engine, Energy (2014), http://dx.doi.org/10.1016/j.energy.2014.09.032