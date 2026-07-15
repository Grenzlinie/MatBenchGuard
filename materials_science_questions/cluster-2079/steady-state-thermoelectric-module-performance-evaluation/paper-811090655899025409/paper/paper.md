# Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter and Nonlinear Optimization Method

LANLAN CAI, $^{1}$ PENG LI, $^{1,3}$ QI LUO, $^{1}$ PENGCHENG ZHAI, $^{2}$
and QINGJIE ZHANG $^{2}$

1.—School of Mechanical and Electrical Engineering, Wuhan University of Technology, Wuhan 430070, Hubei, China. 2.—State Key Laboratory of Advanced Technology for Materials Synthesis and Processing, Wuhan University of Technology, Wuhan 430070, Hubei, China.
3.—e-mail: lp1968@whut.edu.cn

As no single thermoelectric material has presented a high figure-of-merit (ZT) over a very wide temperature range, segmented thermoelectric generators (STEGs), where the $p$- and $n$-legs are formed of different thermoelectric material segments joined in series, have been developed to improve the performance of thermoelectric generators. A crucial but difficult problem in a STEG design is to determine the optimal values of the geometrical parameters, like the relative lengths of each segment and the cross-sectional area ratio of the $n$- and $p$-legs. Herein, a multi-parameter and nonlinear optimization method, based on the Improved Powell Algorithm in conjunction with the discrete numerical model, was implemented to solve the STEG’s geometrical optimization problem. The multi-parameter optimal results were validated by comparison with the optimal outcomes obtained from the single-parameter optimization method. Finally, the effect of the hot- and cold-junction temperatures on the geometry optimization was investigated. Results show that the optimal geometry parameters for maximizing the specific output power of a STEG are different from those for maximizing the conversion efficiency. Data also suggest that the optimal geometry parameters and the interfacial temperatures of the adjacent segments optimized for maximum specific output power or conversion efficiency vary with changing hot- and cold-junction temperatures. Through the geometry optimization, the $CoSb_3$/ $Bi_2Te_3$-based STEG can obtain a maximum specific output power up to 1725.3 W/kg and a maximum efficiency of 13.4% when operating at a hot-junction temperature of 823 K and a cold-junction temperature of 298 K.

**Key words:** Geometry optimization, segmented thermoelectric generator, multi-parameter, powell method

## Abbreviations
| | |
| --- | --- |
| STEG | Segmented thermoelectric generator |
| STEGs | Segmented thermoelectric generators |
| TEG | Thermoelectric generator |
| TEGs | Thermoelectric generators |
| DNM | Discrete numerical model |

## Symbols
| | |
| --- | --- |
| $\alpha$ | Seebeck coefficient (V/K) |
| $\sigma$ | Electrical conductivity (S/m) |
| $\kappa$ | Thermal conductivity (W/(mK)) |
| $K$ | Heat transfer coefficient (W/K) |
| $T$ | Temperature (K) |
| ZT | Figure-of-merit |
| CP | Characteristic power ($CP = T^2Z\kappa$) |
| $T_{nf}$ | Interface temperature between the hot-segment and the cold-segment in the $n$-leg (K) |

(Received May 29, 2016; accepted December 2, 2016)

Published online: 04 January 2017

$T_{\text{pf}}$
Interface temperature between the hot-segment and the cold-segment in the $p$-leg (K)

$T_{\text{c}}$
Temperature at the cold-junction of the thermoelectric module (K)

$T_{\text{h}}$
Temperature at the hot-junction of the thermoelectric module (K)

$\rho_{\text{nh}}$
Density of the hot-segment material in the $n$-leg ($\text{kg/m}^3$)

$\rho_{\text{ph}}$
Density of the hot-segment material in the $p$-leg ($\text{kg/m}^3$)

$\rho_{\text{nc}}$
Density of the cold-segment material in the $n$-leg ($\text{kg/m}^3$)

$\rho_{\text{pc}}$
Density of the cold-segment material in the $p$-leg ($\text{kg/m}^3$)

$N_{\text{nh}}$
Element number of the hot-segment in the $n$-leg

$N_{\text{ph}}$
Element number of the hot-segment in the $p$-leg

$N_{\text{nc}}$
Element number of the cold-segment in the $n$-leg

$N_{\text{pc}}$
Element number of the cold-segment in the $p$-leg

$L$
Total length of the thermoelectric leg (m)

$L_{\text{nh}}$
Length of the hot-segment of the $n$-leg (m)

$L_{\text{nc}}$
Length of the cold-segment of the $n$-leg (m)

$L_{\text{ph}}$
Length of the hot-segment of the $p$-leg (m)

$L_{\text{pc}}$
Length of the cold-segment of the $p$-leg (m)

$A_{\text{n}}$
Cross-sectional area of the $n$-leg ($\text{m}^2$)

$A_{\text{p}}$
Cross-sectional area of the $p$-leg ($\text{m}^2$)

$S_{\text{nh}}$
Ratio of the hot-segment length to the total length of the $n$-leg ($S_{\text{nh}} = L_{\text{nh}}/L$)

$S_{\text{ph}}$
Ratio of the hot-segment length to the total length of the $p$-leg ($S_{\text{ph}} = L_{\text{ph}}/L$)

$a$
Cross-sectional area ratio of the $n$-leg and the $p$-leg ($a = A_{\text{n}}/A_{\text{p}}$)

$S_{\text{nh,opt}}$
The optimal value of $S_{\text{nh}}$

$S_{\text{ph,opt}}$
The optimal value of $S_{\text{ph}}$

$a_{\text{opt}}$
The optimal value of $a$

$I$
Current flowing through the thermoelectric legs under the matched-load condition (A)

$R$
Total resistance of the STEG ($\Omega$)

$R_{\text{in}}$
Internal resistance of the STEG ($\Omega$)

$R_{\text{L}}$
Load resistance ($\Omega$)

$P_{\text{m}}$
Specific output power ($\text{W/kg}$)

$\eta$
Conversion efficiency ($\%$)

### Superscript and subscript
$i$
Element sequence number

$n$
$n$-type thermoelectric leg

$p$
$p$-type thermoelectric leg

$c$
Cold-junction of thermoelectric module

$h$
Hot-junction of thermoelectric module

$\text{nh}$
Hot-segment in the $n$-leg

$\text{nc}$
Cold-segment in the $n$-leg

$\text{ph}$
Hot-segment in the $p$-leg

$\text{pc}$
Cold-segment in the $p$-leg

$\text{opt}$
The optimal value

---

## INTRODUCTION

Thermoelectric generators (TEGs) have the ability to convert thermal energy to electrical power directly, and can be used to recovery the huge amount of low-grade waste heat. They show many practical advantages such as no moving parts, good stability, high reliability, environmental friendliness, and long operation life. Their meaning to the present energy-conscious and environment-conscious age is beyond description. However, the low conversion efficiency and high cost of TEGs have been restraining their commercial application. Therefore, much effort has been made to enhance the TEGs' conversion efficiency. An effective way is to join various materials that have high figure-of-merit in different temperature ranges together to form a segmented thermoelectric leg. Numerous findings $^{1-6}$ confirmed that, compared with non-segmented TEGs working with large temperature differences, proper design of segmented thermoelectric generators (STEGs) could significantly enhance the conversion efficiency and the output power. Studies on STEGs design usually involve two focuses.

Firstly, the proper design of STEGs involves determining the number of segments in the $n$- and $p$-leg according to the hot- and cold-junction temperatures, and selecting the appropriate materials for each segment. Highest figure-of-merit (ZT) has long been considered as the mainly criterion in determining the target segment materials. However, in 2002, Snyder et al. $^{7}$ proposed that the compatibility factor ($s$) was a further crucial criterion to evaluate the appropriate combination of segment materials. STEGs with segment materials that have higher ZT and closer $s$ can produce higher conversion efficiency. For example, segmentation of $(\text{AgSbTe}_2)_{0.15}(\text{GeTe})_{0.85}$ (TAGS) with SnTe or PbTe only produced little extra power, while with filled skutterudite it significantly increased the efficiency from $10.45\%$ to $13.56\%$. $^{8}$ Another example was an ineffective segmentation of SiGe with $\text{Bi}_2\text{Te}_3$, various skutterudites and/or TAGS which showed a marked decline in efficiency—even though SiGe has a reasonably high ZT. $^{7,8}$ In addition, other properties such as thermal and chemical stability, environmental-friendliness, low cost, and abundant supply, should also be considered in the material selection. More details about the materials selection and the performance of STEGs that segment different state-of-art thermoelectric materials together can be found in Refs. 9–11.

Another crucial issue in a segmented thermoelectric generator (STEG) design is the geometry optimization, for the geometrical parameters of a STEG also significantly affect its output power and conversion efficiency. The design task is to search for the optimal values for the geometrical parameters

Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter
and Nonlinear Optimization Method

that make a STEG produce the maximum output
power or conversion efficiency. Up to now, various
approaches have been developed for the geometry
optimization of STEGs, and they can mainly be
summarized into three categories.

The first approach is to derive the length of each
segment in the $n$- or $p$-leg by the heat transfer
analysis with known interface temperature. $^{12,13}$ In
this method, how to determine the optimal interface
temperature between the adjacent materials is a
crucial issue. Saber and El-Genk $^{14}$ found that, the
optimal interface temperatures for the maximum
efficiency or electrical power density, were close to
the cross-point temperature of the ZT curves or CP
(characteristic power) curves of the adjacent seg-
ment materials. Zhang et al. $^{15}$ further proved that
the optimal interface temperature corresponding to
the highest output power and conversion efficiency
of STEGs, were achieved at the intersection tem-
peratures of the new power factor curves and the
new efficiency factor curves, respectively. The new
power factor and the new efficiency factor were not
only relative to material properties but also to
geometrical parameters and heat transfer condi-
tions, and they were equal to the traditional power
factor and the figure-of-merit when the heat trans-
fer coefficients on the hot and cold sides were
infinitely large. But for this idea, different opinions
can be found in publications. For instance, Schilz
et al. $^{16}$ demonstrated that simply selecting the
highest ZT locally was not the right way to increase
the overall efficiency suitable for any general case,
because ZT was only a material quality, but not an
accurate criterion to evaluate a device performance.
Therefore, whether the value at the intersections of
some properties curves of thermoelectric materials
can be simply taken as the optimal interface
temperatures is still controversial.

The second approach for the geometrical opti-
mization is based on the single-parameter optimiza-
tion method, that is, the optimal value for a specific
parameter is obtained by searching the parameter
that could make the STEG reach the best perfor-
mance while keeping the other parameters
unchanged. Swanson et al. $^{17}$ applied the method
and calculated the partial derivative of conversion
efficiency with respect to the cross-sectional area
ratio to optimize the STEG performance. Picard
et al. $^{18}$ obtained an optimal segment length for the
maximum output power of STEG from the curve of
power versus the cold-side segment length, but with
the assumption that the length of the cold-side
segment was the same for both the $n$- and $p$-type
legs. Similarly, Jia et al. $^{3}$ optimized the hot segment
lengths in the $n$- and $p$-legs for maximizing the
STEG conversion efficiency. D'Angelo et al. $^{19}$
obtained the optimal junction temperatures and
the optimal cross-sectional area ratio of the $n$- and
$p$-legs for the maximum efficiency. Tian et al. $^{20}$
optimized the length ratios of the hot-segment in
the $n$- and $p$-legs of STEG with various heat and
cold source temperatures, respectively, for the max-
imum output power and conversion efficiency. How-
ever, the single-parameter optimization method
neglected the coupled effects that various parame-
ters produced on the STEG performance, thus
making the above geometrical optimizations of
STEG less accurate.

To better understand the interactions of various
design parameters, a third method that combines a
multi-parameter optimization algorithm and a TEG
analytical/numerical model has been developed.
Saber and El-Genk $^{14}$ utilized a genetic algorithm
coupled with the one-dimensional analytical TEG
model to optimize the lengths of segments in the
legs of STEG for the maximum efficiency or electric
power density. However, the area ratio of the $n$- and
$p$-legs was not optimized simultaneously, which was
independently optimized by a simple formula. $^{21}$ To
the authors' best knowledge, few studies on STEG
geometry design with the multi-parameter opti-
mization method are available in the literature.

In this paper, a new multi-parameter and nonlin-
ear optimization method based on the Improved
Powell Search Algorithm in conjunction with the
discrete numerical model (DNM), was implemented
to solve the STEG geometry optimization problem.
The DNM was used to accurately calculate the
objective optimization function that could be the
specific output power or the conversion efficiency of
STEG, as described in "Objective Function, Design
Parameters and Constraints" section. The reason
why the Improved Powell Search Algorithm was
selected as the optimization tool is shown in the
"Multi-parameter and Nonlinear Optimization
Method" section. In the "Geometry Optimization
for Maximizing Specific Output Power and Conver-
sion Efficiency" section, the geometrical parameters
including the length ratios of the hot-segment to the
whole leg for the $n$- and $p$-types and the cross-
sectional area ratio of the $n$- and $p$-legs were
optimized for maximizing the specific output power
and conversion efficiency of STEG, respectively.
Furthermore, the optimal results were analyzed
and compared with the single-parameter optimal
outcomes in the "Validation of the Optimal Results"
section. Finally, the effects of different hot- and
cold-junction temperatures on the geometrically
optimal results were investigated in the "Effect of
Hot- and Cold-Junction Temperatures on STEG
Geometry Optimization" section.

# NUMERICAL METHODS

## Segmented Thermoelectric Generator (STEG)
Based on $CoSb_3$ and $Bi_2Te_3$

A typical STEG usually consists of a number of
thermocouples with the same performance, and the
$n$- or $p$-leg of the thermocouples usually has two or
more segments made of different thermoelectric
materials that could optimally operate within dif-
ferent temperature ranges. For simplicity, only one

segmented thermocouple is analyzed in the present study. The structure of a segmented thermocouple is shown in Fig. 1. Herein, the $n$- or $p$-leg of the STEG is constructed by segmenting the medium temperature bulk material $\mathrm{CoSb}_{3}$ and the low temperature bulk material $\mathrm{Bi}_{2}\mathrm{Te}_{3}$ together. The thermoelectric properties of the $p$- and $n$-type $\mathrm{CoSb}_{3}$ and $\mathrm{Bi}_{2}\mathrm{Te}_{3}$, provided by the Shanghai Institute of Ceramics, Chinese Academy of Sciences, are presented in Fig. 2. It can be seen that the Seebeck coefficient, the electrical conductivity and the thermal conductivity of the materials all vary with temperature.

As shown in Fig. 1, the $p$- and $n$-legs have the same total length of $L$, and the segments in one leg are designed to have the same cross-sectional area, for fabrication convenience. The structure design of the STEG here is to determine the appropriate length of each segment ($L_{\mathrm{nh}}$, $L_{\mathrm{nc}}$, $L_{\mathrm{ph}}$ and $L_{\mathrm{pc}}$), and the appropriate cross-sectional area of the $n$- and $p$-legs ($A_{n}$ and $A_{p}$) so as to make the STEG produce the best performance for the maximum specific output power or conversion efficiency.

## Objective Function, Design Parameters and Constraints

### Objective Function

For the present study, the objective function should be the function to calculate the specific output power or the conversion efficiency of STEG. Firstly, an accurate numerical model for the STEG performance calculation has to be developed. Herein, the previously built and validated discrete numerical model (DNM)$^{22}$ for TEG performance estimation, which has accounted for the temperature-dependence of thermoelectric properties, is applied for the performance estimation of our segmented thermocouple. Figure 3 shows the DNM used for the STEG. The $\mathrm{CoSb}_{3}$-segment and $\mathrm{Bi}_{2}\mathrm{Te}_{3}$-segment in the $n$- and $p$-legs are individually divided into $N_{\mathrm{nh}}$, $N_{\mathrm{nc}}$, $N_{\mathrm{ph}}$, and $N_{\mathrm{pc}}$ elements as presented in Fig. 3. By controlling the values of $N_{\mathrm{nh}}$, $N_{\mathrm{nc}}$, $N_{\mathrm{ph}}$, and $N_{\mathrm{pc}}$, the temperature difference of each element could be small enough, so that the material properties of each element can be considered as constants. Then, the general steady-state heat balance equation for each element can be expressed by

$$
\begin{aligned}
& K_{\mathrm{nh}}^{i}\left(T_{\mathrm{nh}}^{i-1}-T_{\mathrm{nh}}^{i}\right)+\frac{1}{2} I^{2} R_{\mathrm{nh}}^{i}+\alpha_{\mathrm{nh}}^{i} I T_{\mathrm{nh}}^{i} \\
& \quad=K_{\mathrm{nh}}^{i+1}\left(T_{\mathrm{nh}}^{i}-T_{\mathrm{nh}}^{i+1}\right)-\frac{1}{2} I^{2} R_{\mathrm{nh}}^{i+1}+\alpha_{\mathrm{nh}}^{i+1} I T_{\mathrm{nh}}^{i}, \\
& \quad\left(i=1, \ldots, N_{n h}-1\right),
\end{aligned} \tag{1}
$$

$$
\begin{aligned}
& K_{\mathrm{nh}}^{N_{\mathrm{nh}}}\left(T_{\mathrm{nh}}^{N_{\mathrm{nh}}-1}-T_{\mathrm{nh}}^{N_{\mathrm{nh}}}\right)+\frac{1}{2} I^{2} R_{\mathrm{nh}}^{N_{\mathrm{nh}}}+\alpha_{\mathrm{nh}}^{N_{\mathrm{nh}}} I T_{\mathrm{nh}}^{N_{\mathrm{nh}}} \\
& \quad=K_{\mathrm{nc}}^{1}\left(T_{\mathrm{nc}}^{0}-T_{\mathrm{nc}}^{1}\right)-\frac{1}{2} I^{2} R_{\mathrm{nc}}^{1}+\alpha_{\mathrm{nc}}^{1} I T_{\mathrm{nc}}^{0},
\end{aligned} \tag{2}
$$

$$
\begin{aligned}
& K_{\mathrm{nc}}^{i}\left(T_{\mathrm{nc}}^{i-1}-T_{\mathrm{nc}}^{i}\right)+\frac{1}{2} I^{2} R_{\mathrm{nc}}^{i}+\alpha_{\mathrm{nc}}^{i} I T_{\mathrm{nc}}^{i} \\
& \quad=K_{\mathrm{nc}}^{i+1}\left(T_{\mathrm{nc}}^{i}-T_{\mathrm{nc}}^{i+1}\right)-\frac{1}{2} I^{2} R_{\mathrm{nc}}^{i+1}+\alpha_{\mathrm{nc}}^{i+1} I T_{\mathrm{nc}}^{i}, \\
& \quad\left(i=1, \ldots, N_{n c}-1\right),
\end{aligned} \tag{3}
$$

for the $n$-type leg, and

$$
\begin{aligned}
& K_{\mathrm{ph}}^{i}\left(T_{\mathrm{ph}}^{i-1}-T_{\mathrm{ph}}^{i}\right)+\frac{1}{2} I^{2} R_{\mathrm{ph}}^{i}+\alpha_{\mathrm{ph}}^{i} I T_{\mathrm{ph}}^{i} \\
& \quad=K_{\mathrm{ph}}^{i+1}\left(T_{\mathrm{ph}}^{i}-T_{\mathrm{ph}}^{i+1}\right)-\frac{1}{2} I^{2} R_{\mathrm{ph}}^{i+1}+\alpha_{\mathrm{ph}}^{i+1} I T_{\mathrm{ph}}^{i}, \\
& \quad\left(i=1, \ldots, N_{p h}-1\right),
\end{aligned} \tag{4}
$$

$$
\begin{aligned}
& K_{\mathrm{ph}}^{N_{\mathrm{ph}}}\left(T_{\mathrm{ph}}^{N_{\mathrm{ph}}-1}-T_{\mathrm{ph}}^{N_{\mathrm{ph}}}\right)+\frac{1}{2} I^{2} R_{\mathrm{ph}}^{N_{\mathrm{ph}}}+\alpha_{\mathrm{ph}}^{N_{\mathrm{ph}}} I T_{\mathrm{ph}}^{N_{\mathrm{ph}}} \\
& \quad=K_{\mathrm{pc}}^{1}\left(T_{\mathrm{pc}}^{0}-T_{\mathrm{pc}}^{1}\right)-\frac{1}{2} I^{2} R_{\mathrm{pc}}^{1}+\alpha_{\mathrm{pc}}^{1} I T_{\mathrm{pc}}^{0},
\end{aligned} \tag{5}
$$

$$
\begin{aligned}
& K_{\mathrm{pc}}^{i}\left(T_{\mathrm{pc}}^{i-1}-T_{\mathrm{pc}}^{i}\right)+\frac{1}{2} I^{2} R_{\mathrm{pc}}^{i}+\alpha_{\mathrm{pc}}^{i} I T_{\mathrm{pc}}^{i} \\
& \quad=K_{\mathrm{pc}}^{i+1}\left(T_{\mathrm{pc}}^{i}-T_{\mathrm{pc}}^{i+1}\right)-\frac{1}{2} I^{2} R_{\mathrm{pc}}^{i+1}+\alpha_{\mathrm{pc}}^{i+1} I T_{\mathrm{pc}}^{i}, \\
& \quad\left(i=1, \ldots, N_{p c}-1\right),
\end{aligned} \tag{6}
$$

for the $p$-type leg.

In the above equations, $T_{\mathrm{nh}}^{i}$, $T_{\mathrm{nc}}^{i}$, $T_{\mathrm{ph}}^{i}$ and $T_{\mathrm{pc}}^{i}$ stand for the temperature distribution in the thermoelectric legs, as marked in Fig. 3. The heat transfer coefficient $K_{\mathrm{nh}}^{i}, K_{\mathrm{nc}}^{i}, K_{\mathrm{ph}}^{i}, K_{\mathrm{pc}}^{i}$, the resistance $R_{\mathrm{nh}}^{i}, R_{\mathrm{nc}}^{i}, R_{\mathrm{ph}}^{i}, R_{\mathrm{pc}}^{i}$, and the Seebeck coefficient $\alpha_{\mathrm{nh}}^{i},\alpha_{\mathrm{nc}}^{i}$, $\alpha_{\mathrm{ph}}^{i}$, $\alpha_{\mathrm{pc}}^{i}$ of each element, as well as the current $I$ are derived by

![](./images/811090655899025409_1.jpg)

Fig. 1. Schematic of segmented thermoelectric generator (STEG) based on $\mathrm{CoSb}_{3}$ and $\mathrm{Bi}_{2}\mathrm{Te}_{3}$.

Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter
and Nonlinear Optimization Method

![](./images/811090655899025409_2.jpg)

![](./images/811090655899025409_3.jpg)

![](./images/811090655899025409_4.jpg)

![](./images/811090655899025409_5.jpg)

![](./images/811090655899025409_6.jpg)

Fig. 2. Thermoelectric properties of the $p$- and $n$-type $CoSb_3$ and $Bi_2Te_3$ varying with temperature: (a) Seebeck coefficient $\alpha(T)$; (b) electrical conductivity $\sigma(T)$; (c) thermal conductivity $\kappa(T)$; (d) figure-of-merit $(ZT)$; (e) characteristic power $(CP)$.

$$
K_{m}^{i}=\frac{A_{m} \cdot \frac{\kappa_{m}\left(T_{m}^{i-1}\right)+\kappa_{m}\left(T_{m}^{i}\right)}{2}}{L_{m}^{i}}
$$

$$
R_{m}^{i}=\frac{L_{m}^{i}}{A_{m} \cdot \frac{\sigma_{m}\left(T_{m}^{i-1}\right)+\sigma_{m}\left(T_{m}^{i}\right)}{2}}
$$

(m can be substituted by nh, ph, nc and pc)

$$
\alpha_{m}^{i}=\frac{\alpha_{m}\left(T_{m}^{i-1}\right)+\alpha_{m}\left(T_{m}^{i}\right)}{2}
$$

(7)

and

$$
I=\frac{\sum_{i=1}^{N_{\mathrm{nh}}} \alpha_{\mathrm{nh}}^{i}\left(T_{\mathrm{nh}}^{i-1}-T_{\mathrm{nh}}^{i}\right)+\sum_{i=1}^{N_{\mathrm{nc}}} \alpha_{\mathrm{nc}}^{i}\left(T_{\mathrm{nc}}^{i-1}-T_{\mathrm{nc}}^{i}\right)+\sum_{i=1}^{N_{\mathrm{ph}}} \alpha_{\mathrm{ph}}^{i}\left(T_{\mathrm{ph}}^{i-1}-T_{\mathrm{ph}}^{i}\right)+\sum_{i=1}^{N_{\mathrm{pc}}} \alpha_{\mathrm{pc}}^{i}\left(T_{\mathrm{pc}}^{i-1}-T_{\mathrm{pc}}^{i}\right)}{R_{\mathrm{in}}+R_{\mathrm{con}}+R_{\mathrm{L}}}. \quad (8)
$$

$$
\eta=\frac{I \cdot R_{\mathrm{L}}}{K_{\mathrm{nh}}^{1}\left(T_{\mathrm{h}}-T_{\mathrm{nh}}^{1}\right)-\frac{1}{2} I^{2} R_{\mathrm{nh}}^{1}+\alpha_{\mathrm{nh}}^{1} I T_{\mathrm{h}}+K_{\mathrm{ph}}^{1}\left(T_{\mathrm{h}}-T_{\mathrm{ph}}^{1}\right)-\frac{1}{2} I^{2} R_{\mathrm{ph}}^{1}+\alpha_{\mathrm{ph}}^{1} I T_{\mathrm{h}}} \times 100,
$$

(10)

Here, $\kappa_{m}(T_{m}^{i-1})$, $\kappa_{m}(T_{m}^{i})$, $\sigma_{m}(T_{m}^{i-1})$, $\sigma_{m}(T_{m}^{i})$, $\alpha_{m}(T_{m}^{i-1})$ and $\alpha_{m}(T_{m}^{i})$ represent the thermal conductivity, the electrical conductivity and the Seebeck coefficient corresponding to the top- and bottom-joint temperature of the $i$th element in each segment. $L_{m}^{i}$ is the length of the $i$th element in each segment that is calculated by $L_{m}^{i}=\frac{L_{m}}{N_{m}^{i}}$. $A_{m}$ represents the cross-sectional area of various segments with the assumption that $A_{\mathrm{nh}}=A_{\mathrm{nc}}=A_{\mathrm{n}}$ and $A_{\mathrm{ph}}=A_{\mathrm{pc}}=A_{\mathrm{p}}$. $R_{\mathrm{L}}$ in Eq. 8 denotes the load resistance, which takes the value by $R_{\mathrm{L}}=R_{\mathrm{in}}$ for maximizing the specific output power, and by $R_{\mathrm{L}}=\sqrt{1+Z T} R_{\mathrm{in}}$ for maximizing the conversion efficiency. $R_{\mathrm{in}}$ represents the inner resistance of the STEG, which is calculated by $R_{\mathrm{in}}=\sum_{i=1}^{N_{\mathrm{nh}}} R_{\mathrm{nh}}^{i}+\sum_{i=1}^{N_{\mathrm{nc}}} R_{\mathrm{nc}}^{i}+\sum_{i=1}^{N_{\mathrm{ph}}} R_{\mathrm{ph}}^{i}+\sum_{i=1}^{N_{\mathrm{pc}}} R_{\mathrm{pc}}^{i}$. $R_{\mathrm{con}}$ stands for the total electrical contact resistance existing in the segment-electrode interfaces and the segment-segment interfaces of a STEG.

If the operating temperature range $T_{\mathrm{h}}$ and $T_{\mathrm{c}}$, the geometric parameters $L$, $L_{\mathrm{nh}}$, $L_{\mathrm{ph}}$, $A_{\mathrm{n}}$, $A_{\mathrm{p}}$, together with the temperature dependences of each segment material properties including $\varkappa(T)$, $\kappa(T)$ and $\sigma(T)$ are given, the temperature distribution of the STEG can be obtained by solving the above heat balance equations by using a numerical iterative algorithm (cf. Ref. 22). Then, the internal resistance $R_{\mathrm{in}}$, the load resistance $R_{\mathrm{L}}$ and the current $I$ can be figured out. Finally, the specific output power $P_{\mathrm{m}}$ and conversion efficiency $\eta$ can be obtained by

$$
P_{\mathrm{m}}=\frac{I \cdot R_{\mathrm{L}}}{\rho_{\mathrm{nh}}\left(L_{\mathrm{nh}} \cdot A_{\mathrm{n}}\right)+\rho_{\mathrm{ph}}\left(L_{\mathrm{ph}} \cdot A_{\mathrm{p}}\right)+\rho_{\mathrm{nc}}\left(L_{\mathrm{nc}} \cdot A_{\mathrm{n}}\right)+\rho_{\mathrm{pc}}\left(L_{\mathrm{pc}} \cdot A_{\mathrm{p}}\right)}
$$

(9)

and

where $\rho_{\mathrm{nh}}$, $\rho_{\mathrm{ph}}$, $\rho_{\mathrm{nc}}$ and $\rho_{\mathrm{pc}}$ represent the densities of the thermoelectric materials used in each segment. In this study, $\rho_{\mathrm{nh}}=\rho_{\mathrm{ph}}=7.3 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$ for $\mathrm{CoSb}_{3}$, and $\rho_{\mathrm{nc}}=\rho_{\mathrm{pc}}=7.7 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$ for $\mathrm{Bi}_{2} \mathrm{Te}_{3}$.

### Design Variables

As is known, the geometric structure of a segmented thermocouple can be decided uniquely when the total length of thermoelectric leg $L$, the length ratios of the hot-segment to the whole leg for $n$- and $p$-type $S_{\mathrm{nh}}$ ($S_{\mathrm{nh}}=L_{\mathrm{nh}}/L$) and $S_{\mathrm{ph}}$ ($S_{\mathrm{ph}}=L_{\mathrm{ph}}/L$), the cross-sectional area of $p$-leg $A_{\mathrm{p}}$, and the area ratio $a$ ($a=A_{\mathrm{n}}/A_{\mathrm{p}}$) are determined. Figure 4 shows the effects of the single parameter $L$, $S_{\mathrm{nh}}$, $S_{\mathrm{ph}}$, $A_{\mathrm{p}}$, or $a$ on the STEG performance, where the data are calculated by the DNM. The specific output power monotonically decreases with the increasing $L$ but almost remains unchanged with the increasing $A_{\mathrm{p}}$, and but shows a rise followed by a decline with increasing $S_{\mathrm{nh}}$, $S_{\mathrm{ph}}$ and $a$. The conversion efficiency also increases at first and decreases later as $S_{\mathrm{nh}}$, $S_{\mathrm{ph}}$ and $a$ increase, but basically keeps constant when $L$

# Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter and Nonlinear Optimization Method

![](./images/811090655899025409_7.jpg)

Fig. 3. Discrete numerical model (DNM) applied on STEG.

and $A_{\mathrm{p}}$ vary. We can observe that an optimal value exists for $S_{\mathrm{nh}}, S_{\mathrm{ph}}$ or $a$ for maximizing the specific output power or the conversion efficiency. Consequently, the three parameters $S_{\mathrm{nh}}, S_{\mathrm{ph}}$ and $a$ are chosen as the design variables.

## Constraints
Before the optimization is carried out, some constraints should be considered to avoid the unphysical conditions. First, the design parameters $S_{\mathrm{nh}}, S_{\mathrm{ph}}$ and $a$ should take positive values based on the practical requirement. Second, the temperature $T^{i}$ should vary from high to low along the thermoelectric leg from the hot-junction to the cold-junction, as presented in Fig. 3. Third, the interface temperature of the segments in the $n$- and $p$-legs, $T_{\mathrm{nf}}$ and $T_{\mathrm{pf}}$, should be lower than the upper temperature limit for the thermoelectric material $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ and higher than the lower temperature limit for $\mathrm{CoSb}_{3}$, which is $563 \mathrm{~K}$ and $300 \mathrm{~K}$, respectively, as can be observed from Fig. 2. Therefore, the constraints for the optimization can be summarized as

$$
\begin{aligned}
& S_{\mathrm{nh}}>0, S_{\mathrm{ph}}>0, a>0 ; \\
& T_{\mathrm{h}}=T_{\mathrm{nh}}^{0}>T_{\mathrm{nh}}^{1}>\cdots>T_{\mathrm{nh}}^{i}>T_{\mathrm{nh}}^{i+1}>\cdots>T_{\mathrm{nh}}^{N_{\mathrm{nh}}-1}>T_{\mathrm{nh}}^{N_{\mathrm{nh}}}=T_{\mathrm{nc}}^{0}>T_{\mathrm{nc}}^{1}>\cdots>T_{\mathrm{nc}}^{i}>T_{n c}^{i+1}>\cdots>T_{\mathrm{nc}}^{N_{\mathrm{nc}}-1}>T_{\mathrm{nc}}^{N_{\mathrm{nc}}}=T_{\mathrm{c}} ; \\
& T_{\mathrm{h}}=T_{\mathrm{ph}}^{0}>T_{\mathrm{ph}}^{1}>\cdots>T_{\mathrm{ph}}^{i}>T_{\mathrm{ph}}^{i+1}>\cdots>T_{\mathrm{ph}}^{N_{\mathrm{ph}}-1}>T_{\mathrm{ph}}^{N_{\mathrm{ph}}}=T_{\mathrm{pc}}^{0}>T_{\mathrm{pc}}^{1}>\cdots>T_{\mathrm{pc}}^{i}>T_{\mathrm{pc}}^{i+1}>\cdots>T_{\mathrm{pc}}^{N_{\mathrm{pc}}-1}>T_{\mathrm{pc}}^{N_{\mathrm{pc}}}=T_{\mathrm{c}} ; \\
& 300 \mathrm{~K}<T_{\mathrm{nf}}=T_{\mathrm{nf}}^{N_{\mathrm{nf}}}<563 \mathrm{~K} ; \\
& 300 \mathrm{~K}<T_{\mathrm{pf}}=T_{\mathrm{pf}}^{N_{\mathrm{pf}}}<563 \mathrm{~K}.
\end{aligned}
\tag{11}
$$

In summary, the design variables of the geometrical optimization of STEG include the two length ratios $(S_{\mathrm{nh}}$ and $S_{\mathrm{ph}})$ and the cross-sectional area ratio $(a)$. The objective function is Eqs. 9 or 10 that can be used to accurately compute the specific output power $(P_{\mathrm{m}})$ or the conversion efficiency $(\eta)$ based on the DNM. The design task is in search of the optimal values for the three design variables, to make the objective function subject to the constraints listed in Eq. 11 achieve the maximum value.

## Multi-parameter and Nonlinear Optimization Method
The above optimization case possesses the following characteristics: (1) A non-linear relationship exists between the objective function $(P_{\mathrm{m}}$ or $\eta)$ and the design parameters $(S_{\mathrm{nh}}, S_{\mathrm{ph}}$ and $a)$; (2) The derivative of the objective function cannot be figured out because it cannot be computed by an explicit expression of design variables; and (3) All the design parameters should be optimized simultaneously because they have coupled effects on the objective function. Based on the features (1) and (3), only the multi-parameter and nonlinear optimization method can be considered. Owning to the feature (2), only direct search methods and intelligent optimization algorithms that require no derivative information can be selected. However, the intelligent optimization algorithms such as the genetic algorithm and the particle swarm optimization algorithm exhibit a distinct drawback, that is, the search speed is fast initially, but becomes slower as the number of iterations increases. Thus, large computational time may be consumed but the best solution rarely can be reached.

The Powell method $^{23}$ is a well-known direct search method for its fast ultimate convergence rate. Powell has proved that only $N$ iterations are required to yield the optimal solution for the optimization problems with a $N$-dimensional quadratic objective function, and more iterations may be required for problems with objective function of other forms. In particular, this method cannot converge to the optimal solution if the search

![](./images/811090655899025409_8.jpg)

![](./images/811090655899025409_9.jpg)

![](./images/811090655899025409_10.jpg)

![](./images/811090655899025409_11.jpg)

![](./images/811090655899025409_12.jpg)

Fig. 4. Effects of single geometric parameter on the specific output power and the conversion efficiency: (a) $P_{\mathrm{m}}$ versus $L$ & $\eta$ versus $L$; (b) $P_{\mathrm{m}}$ versus $A_{\mathrm{p}}$ & $\eta$ versus $A_{\mathrm{p}}$; (c) $P_{\mathrm{m}}$ versus $S_{\mathrm{nh}}$ & $\eta$ versus $S_{\mathrm{nh}}$; (d) $P_{\mathrm{m}}$ versus $S_{\mathrm{ph}}$ & $\eta$ versus $S_{\mathrm{ph}}$; (e) $P_{\mathrm{m}}$ versus $a$ & $\eta$ versus $a$.

directions are linearly dependent. To ensure the reasonable convergence rate, a modification has been made to the Powell method, that is, the linearly independence of the search directions has to be estimated before determining whether to replace one of the old set of linearly independent directions by the new direction. The modified Powell method has been successfully applied to solve many optimization problems whose derivatives are difficult or impossible to calculate. $^{24,25}$

However, the Powell method is only appropriate to deal with the optimization problems with no constraints.

Here, an Improved Powell Algorithm was devel- oped to solve the present optimization problem. The improvement relative to the modified Powell method is achieved by adding a judgment to esti- mate the satisfaction of the constraints during the process of STEG performance calculation. The flow chart of the Improved Powell method is presented in

![](./images/811090655899025409_13.jpg)

Fig. 5. Flow chart of the Improved Powell Algorithm.

![](./images/811090655899025409_14.jpg)

Fig. 6. Process of the geometry optimization of STEG.

<table>
<caption>Table I. Input parameters of the CoSb₃/Bi₂Te₃-based STEG geometry optimization case</caption>
<thead>
<tr>
<th>Input parameters</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Total length of the thermoelectric leg, $L$/mm</td>
<td>4</td>
</tr>
<tr>
<td>Cross-sectional area of the $p$-leg, $A_p$/mm²</td>
<td>$3\times3$</td>
</tr>
<tr>
<td>Hot-junction temperature of STEG, $T_{\text{h}}$/K</td>
<td>823</td>
</tr>
<tr>
<td>Cold-junction temperature of STEG, $T_{\text{c}}$/K</td>
<td>298</td>
</tr>
<tr>
<td>Temperature dependent thermoelectric properties of CoSb₃ and Bi₂Te₃ used in the STEG: $\alpha(T)$, $\sigma(T)$ and $\kappa(T)$</td>
<td>Presented in Fig. 2</td>
</tr>
<tr>
<td>Total electrical contact resistance, $R_{\text{con}}$/$\Omega$</td>
<td>0ᵃ</td>
</tr>
</tbody>
</table>

ᵃFor simplicity, an assumption of $R_{\text{con}}=0$ was applied, which has no effect on the accuracy validation of the multi-parameter and nonlinear optimization method proposed in the paper.

<table>
<caption>Table II. Output parameters of the CoSb₃/Bi₂Te₃-based STEG geometry optimization case</caption>
<thead>
<tr>
<th>Output parameters</th>
<th>Optimized for $P_{\text{m,max}}$</th>
<th>Optimized for $\eta_{\text{max}}$</th>
<th>Error of the output optimized for $P_{\text{m,max}}$ and $\eta_{\text{max}}$ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$S_{\text{nh,opt}}$</td>
<td>0.93</td>
<td>0.89</td>
<td>4.5</td>
</tr>
<tr>
<td>$S_{\text{ph,opt}}$</td>
<td>0.76</td>
<td>0.73</td>
<td>4.1</td>
</tr>
<tr>
<td>$a_{\text{opt}}$</td>
<td>0.56</td>
<td>0.43</td>
<td>30.2</td>
</tr>
<tr>
<td>$P_{\text{m,max}}$ ($P_{\text{m}}$)/W/kg</td>
<td>1725.33</td>
<td>1637.37</td>
<td>5.4</td>
</tr>
<tr>
<td>$\eta_{\text{max}}$ ($\eta$)/%</td>
<td>12.70</td>
<td>13.35</td>
<td>$-4.9$</td>
</tr>
</tbody>
</table>

$S_{\text{nh,opt}}$ and $S_{\text{ph,opt}}$ represent the optimal values of the length ratios of the hot-segment to the total leg for $n$- and $p$-types, respectively. $a_{\text{opt}}$ means the optimal value of the cross-sectional area ratio of the $n$- and $p$-legs. $P_{\text{m,max}}$ and $\eta_{\text{max}}$ individually indicate the maximum specific output power and conversion efficiency. $P_{\text{m}}$ in the bracket means the specific output power at $\eta_{\text{max}}$. $\eta$ in the bracket represents the conversion efficiency at $P_{\text{m,max}}$.

Fig. 5. The explanations are presented below in detail.

In Step 1, $\boldsymbol{X}$ is a vector of design variables, $\boldsymbol{P}_{0}$ represents the initial search direction set, $\boldsymbol{e}$ indicates the base vector, and $\boldsymbol{S}$ stands for the one-dimensional search direction. The variable $k$ represents the number of iterations, and $N$ indicates the dimensional of the design parameters. For this geometric optimization problem, $N=3$, $\boldsymbol{X}=\{S_{\text{nh}}, S_{\text{ph}}, a\}$, $\boldsymbol{e}^{(0)}=(1,0,0)$, $\boldsymbol{e}^{(1)}=(0,1,0)$, $\boldsymbol{e}^{(2)}=(0,0,1)$, the convergence criterion $\varepsilon=10^{-3}$, and the initial vector of design parameters $\boldsymbol{X}^{(0)}=(0.8,0.8,1)$.

In Step 2, the one-dimensional search process contains two sub steps: (1) determine an initial region containing the minimum point by the back and forth algorithm; (2) search the one-dimensional minimum of the objective function $F(\boldsymbol{X})$ by the Golden Ratio Rule method. As the Improved Powell

# Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter and Nonlinear Optimization Method

![](./images/811090655899025409_15.jpg)

Fig. 7. Single-parameter optimization results of STEG with the same input used in the Improved Powell method: (a) $P_{\mathrm{m}}$ versus $S_{\mathrm{nh}}$ ($T_{\mathrm{nf}}$ versus $S_{\mathrm{nh}}$); (b) $P_{\mathrm{m}}$ versus $S_{\mathrm{ph}}$ ($T_{\mathrm{pf}}$ versus $S_{\mathrm{ph}}$); (c) $\eta$ versus $S_{\mathrm{nh}}$ ($T_{\mathrm{nf}}$ versus $S_{\mathrm{nh}}$); (d) $\eta$ versus $S_{\mathrm{ph}}$ ($T_{\mathrm{pf}}$ versus $S_{\mathrm{ph}}$); and (e) $P_{\mathrm{m}}$ versus $a$ & $\eta$ versus $a$.

Algorithm is to search for the minimum of the objective function, the objective parameter is modified as the opposite of the specific output power or the conversion efficiency ($-P_{\mathrm{m}}$ or $-\eta$), which is calculated by the DNM described in the "Objective Function" section. The constraints are evaluated in the process of calculating the objective function.

Once the constraints cannot be satisfied, the objective function returns the value of zero. Then, a modification has to be made to the design parameters and a new search can be conducted.

In Step 3, the norm is $\|X_{k}^{(N)}-X_{k}^{(0)}\|=
\sqrt{\sum_{i=0}^{N-1}\left(x_{k,i}^{(N)}-x_{k,i}^{(0)}\right)^{2}}$ on the basis of

![](./images/811090655899025409_16.jpg)

Fig. 8. Effect of the hot-junction temperature on STEG geometric optimization for the maximum specific output power and conversion efficiency ($T_{\text{c}} = 298$ K): (a) $S_{\text{nh,opt}}$ versus $T_{\text{h}}$ ($T_{\text{nf,opt}}$ versus $T_{\text{h}}$); (b) $S_{\text{ph,opt}}$ versus $T_{\text{h}}$ ($T_{\text{pf,opt}}$ versus $T_{\text{h}}$); and (c) $a_{\text{opt}}$ versus $T_{\text{h}}$.

$$
\boldsymbol{X}_{k}^{(0)}=\left(x_{k, 0}^{(0)}, x_{k, 1}^{(0)}, \ldots, x_{k, N-2}^{(0)}, x_{k, N-1}^{(0)}\right) \quad \text { and } \quad \boldsymbol{X}_{k}^{(N)}=\left(x_{k, 0}^{(N)}, x_{k, 1}^{(N)}, \ldots, x_{k, N-2}^{(N)}, x_{k, N-1}^{(N)}\right).
$$

Other steps can be easily understood from Fig. 5. Steps 1 to 7 are repeated until the convergence conditions presented in Step 3 are satisfied. Finally, the optimal results are output, where $\boldsymbol{X}^{*}$ indicates the optimal values of the design parameters, $\boldsymbol{X}^{*}=(S_{\text{nh,opt}}, S_{\text{ph,opt}}, a_{\text{opt}})$, and $F(\boldsymbol{X}^{*})$ represents the minimum of the objective function ($-P_{\text{m}}$ or $-\eta$). Therefore, $P_{\text{m,max}}$ (or $\eta_{\text{max}}$) $=-F(\boldsymbol{X}^{*})$.

Above all, the geometry optimization process of a STEG can be summarized in Fig. 6. When the input parameters including the operating temperature range $T_{\text{h}}$ and $T_{\text{c}}$, the total length of thermoelectric leg $L$, the cross-sectional area of p-leg $A_{\text{p}}$, and the temperature-dependent thermoelectric properties ($\alpha(T)$, $\kappa(T)$ and $\sigma(T)$) of each segment material used in the STEG, are given, the optimal value for the design parameters ($S_{\text{nh,opt}}$, $S_{\text{ph,opt}}$ and $a_{\text{opt}}$) corresponding to the maximum output power or conversion efficiency can be searched by the Improved Powell method combined with the DNM.

## RESULTS AND DISCUSSION

### Geometry Optimization for Maximizing Specific Output Power and Conversion Efficiency

By using the Improved Powell method, we conducted a geometrical optimization for the $\text{CoSb}_3$/$\text{Bi}_2\text{Te}_3$-based STEG. The input and output parameters of this optimization trial are listed in Tables I and II.

Table II shows that the optimal values of the design variables for maximizing the specific output power are different from those for maximizing the conversion efficiency. For the maximum specific output power, the optimal design parameters are $S_{\text{nh,opt}} = 0.93$, $S_{\text{ph,opt}} = 0.76$ and $a_{\text{opt}} = 0.56$, while for the maximum conversion efficiency, they become

# Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter and Nonlinear Optimization Method

![](./images/811090655899025409_17.jpg)

Fig. 9. Effect of the cold-junction temperature on STEG geometric optimization for the maximum specific output power and conversion efficiency ($T_{\text{h}} = 823$ K): (a) $S_{\text{nh, opt}}$ versus $T_{\text{c}}$ ($T_{\text{nf, opt}}$ versus $T_{\text{c}}$); (b) $S_{\text{ph, opt}}$ versus $T_{\text{c}}$ ($T_{\text{pf, opt}}$ versus $T_{\text{c}}$); and (c) $a_{\text{opt}}$ versus $T_{\text{c}}$.

$S_{\text{nh, opt}} = 0.89$, $S_{\text{ph, opt}} = 0.73$ and $a_{\text{opt}} = 0.43$. The values for $S_{\text{nh, opt}}$, $S_{\text{ph, opt}}$ and $a_{\text{opt}}$ corresponding to $P_{\text{m, max}}$ are respectively 4.5, 4.1, and 30.2% higher than those corresponding to $\eta_{\text{max}}$. When optimized for $P_{\text{m, max}}$, the $\text{CoSb}_3/\text{Bi}_2\text{Te}_3$-based STEG with a temperature difference of 525 K can obtain a specific output power up to 1725.33 W/kg along with an efficiency of 12.7%. It can get a higher efficiency up to 13.35% but a lower specific output power of 1637.37 W/kg when optimized for $\eta_{\text{max}}$.

The conclusion is that the maximum specific output power and the maximum conversion efficiency cannot be obtained simultaneously with the same geometric parameters. How to design the geometrical structure of the STEG depends on the specific application. If the heat source employed is expensive, the design should be optimized to obtain the maximum conversion efficiency. However, if the heat source is inexpensive or widespread, such as in the case of waste heat or solar energy utilization, maximizing the specific output power will result in a cost reduction for STEG. Or in some other cases, it is necessary to make a trade-off between the conversion efficiency and the specific output power by a multi-objective optimization, which can be considered as a research direction for future efforts.

## Validation of the Optimal Results

To verify the accurateness of the Improved Powell method, the optimal results were compared to the single-parameter optimization results that were calculated by the DNM introduced in the "Objective Function" section. Figure 7 presents the curves of a certain design parameter acting on the specific output power or the conversion efficiency while keeping the other design parameters at the optimal values obtained by the Improved Powell method.

The $P_{\text{m}}$ versus $S_{\text{nh}}$ curve presented in Fig. 7a is generated by varying $S_{\text{nh}}$ from 0.73 to 0.99 while keeping $S_{\text{ph}} = 0.76$, $a = 0.56$, and using the same input parameters listed in Table I. For the

$P_{\mathrm{m}} \sim S_{\mathrm{nh}}$ curve, the minimum value of $S_{\mathrm{nh}}$ becomes 0.73. That is because the interfacial temperature between the hot- and cold-segment in the $n$-leg, $T_{\mathrm{nf}}$, achieves 560 K when $S_{\mathrm{nh}} = 0.73$, which can be observed from the $T_{\mathrm{nf}}$ versus $S_{\mathrm{nh}}$ curve presented in Fig. 7a. If $S_{\mathrm{nh}}$ takes values less than 0.73, $T_{\mathrm{nf}}$ will extend the temperature limit of 563 K—the highest temperature the $\mathrm{Bi}_{2}\mathrm{Te}_{3}$ material can endure. The optimal value for $S_{\mathrm{nh}}$ can be obtained by searching for it from the $P_{\mathrm{m}}$ versus $S_{\mathrm{nh}}$ curve when $P_{\mathrm{m}}$ reaches the maximum value, which is 0.93, and the corresponding $P_{\mathrm{m}}$ is 1725.32 W/kg. The result agrees well with the outcomes listed in Table II.

Similarly, the $P_{\mathrm{m}}$ versus $S_{\mathrm{ph}}$ ($T_{\mathrm{pf}}$ versus $S_{\mathrm{ph}}$), $\eta$ versus $S_{\mathrm{nh}}$ ($T_{\mathrm{nf}}$ versus $S_{\mathrm{nh}}$), $\eta$ versus $S_{\mathrm{ph}}$ ($T_{\mathrm{pf}}$ versus $S_{\mathrm{ph}}$), $P_{\mathrm{m}}$ versus $a$, and $\eta$ versus $a$ curves are individually shown in Fig. 7b-e. It can be observed that, the optimal values for each design parameter searched from the curves of performance varying with that parameter, are all in accordance with the optimal outcomes displayed in Table II. Thus, the optimal results obtained from the Improved Powell method proposed in this paper are validated.

## Effect of Hot- and Cold-Junction Temperatures on STEG Geometry Optimization

As the thermoelectric properties of segment materials of STEG vary with temperature, the geometric optimization of STEGs were carried out in different operating temperature ranges. Figures 8 and 9 individually show the effect of the hot- and cold-junction temperatures on the geometric optimization for maximizing specific output power or conversion efficiency.

As seen from Fig. 8a-c, the optimal length ratios $S_{\mathrm{nh,opt}}$ and $S_{\mathrm{ph,opt}}$ as well as the optimal area ratio $a_{\mathrm{opt}}$, for maximizing the specific output power or the conversion efficiency, all vary with the changing hot-junction temperature $T_{\mathrm{h}}$. When $T_{\mathrm{h}}$ decreases from 823 K to 463 K, $S_{\mathrm{nh,opt}}$, $S_{\mathrm{ph,opt}}$, and $a_{\mathrm{opt}}$ corresponding to the maximum specific output power, vary from 0.93 to 0.83, 0.76 to 0.07, and 0.55 to 0.61, respectively; and $S_{\mathrm{nh,opt}}$, $S_{\mathrm{ph,opt}}$, and $a_{\mathrm{opt}}$ for maximizing the conversion efficiency alter from 0.89 to 0.42, 0.73 to 0.03, and 0.43 to 0.70, respectively. The optimal length ratios all decrease with the decreasing hot-junction temperature. That means the lengths of the hot-segment in the $n$- and $p$-legs gradually become shorter as the hot-junction temperature decreases. The value of $S_{\mathrm{ph,opt}}$, for either the maximum specific output power or the maximum conversion efficiency, almost approaches zero when the hot-junction temperature is 463 K. It can be expected that it would be unnecessary to segment $\mathrm{CoSb}_{3}$ and $\mathrm{Bi}_{2}\mathrm{Te}_{3}$ together for the $p$-leg when the STEG operates with the hot-junction temperature lower than 463 K, for the $p$-leg made of single $\mathrm{Bi}_{2}\mathrm{Te}_{3}$ material may produce better performance.

Similar analysis can be made for Fig. 9a-c. $S_{\mathrm{nh,opt}}$, $S_{\mathrm{ph,opt}}$, and $a_{\mathrm{opt}}$, corresponding to the maximum specific output power or the maximum conversion efficiency, are all diversified with various cold-junction temperatures $T_{\mathrm{c}}$. When $T_{\mathrm{c}}$ increases from 298 K to 408 K, $S_{\mathrm{nh,opt}}$, $S_{\mathrm{ph,opt}}$, and $a_{\mathrm{opt}}$ corresponding to the maximum specific output power, vary from 0.93 to 0.99, 0.76 to 0.88, and 0.55 to 0.52, respectively. $S_{\mathrm{nh,opt}}$, $S_{\mathrm{ph,opt}}$, and $a_{\mathrm{opt}}$ for maximizing the conversion efficiency alter from 0.89 to 0.99, 0.73 to 0.93, and 0.43 to 0.37, respectively, when $T_{\mathrm{c}}$ varies from 298 K to 408 K. The lengths ratios of the hot-segment in the $n$- and $p$-legs gradually increase with the increasing cold-junction temperature. It should be noted that, $S_{\mathrm{nh,opt}}$ for the maximum specific output power is close to 1 when $T_{\mathrm{c}}$ increases to 408 K, and $S_{\mathrm{nh,opt}}$ corresponding to the maximum conversion efficiency approaches 1 when Tc is up to 448 K. It can be speculated that, $n$-leg based on the single $\mathrm{CoSb}_{3}$ material may produce lager specific output power than the segmented leg constructed by $\mathrm{CoSb}_{3}$ and $\mathrm{Bi}_{2}\mathrm{Te}_{3}$ when the cold-junction temperature $T_{\mathrm{c}}$ is higher than 408 K, and produce higher conversion efficiency when $T_{\mathrm{c}}$ is higher than 448 K.

In addition, the inlet figures in Figs. 8a, b, and 9a, b show that, the optimal interfacial temperature $T_{\mathrm{nf,opt}}$ and $T_{\mathrm{pf,opt}}$ corresponding to the maximum output power and the maximum conversion efficiency also vary with the changing hot- and cold-junction temperatures. Therefore, the common idea that the interface temperature for a segmented leg can be simply determined by the intersections of the ZT curves or the CP curves of the adjacent segment materials would be less accurate.

## CONCLUSIONS

A multi-parameter and nonlinear optimization method, namely, the Improved Powell Method with fast ultimate convergence and no calculating derivatives, was proposed to solve the geometric optimization problem of a STEG. The optimization results of the $\mathrm{CoSb}_{3}$/$\mathrm{Bi}_{2}\mathrm{Te}_{3}$-based STEG indicate that, the optimal geometric parameters corresponding to the maximum specific output power $P_{\mathrm{m}}$ are different from those corresponding to the maximum conversion efficiency $\eta$. For maximizing $P_{\mathrm{m}}$, the optimal values for the length ratios of the hot-segment to the whole leg for the $n$- and $p$-type $S_{\mathrm{nh}}$ and $S_{\mathrm{ph}}$, along with the cross-sectional area ratio of the $n$- and $p$-leg $a$ are: $S_{\mathrm{nh,opt}} = 0.93$, $S_{\mathrm{ph,opt}} = 0.76$, $a_{\mathrm{opt}} = 0.56$, producing a maximum $P_{\mathrm{m}}$ up to 1725.3 W/kg and a corresponding $\eta$ of 12.70%. For maximizing $\eta$, the optimal results are: $S_{\mathrm{nh,opt}} = 0.89$, $S_{\mathrm{ph,opt}} = 0.73$, $a_{\mathrm{opt}} = 0.43$, with a maximum $\eta$ reaching 13.4% and a corresponding $P_{\mathrm{m}}$ of 1637.4 W/kg.

In addition, the results obtained from the Improved Powell Method were verified by comparison with the single-parameter optimal outcomes. Furthermore, the influences of the hot- and cold-

Geometry Optimization of a Segmented Thermoelectric Generator Based on Multi-parameter and Nonlinear Optimization Method

junction temperatures on the STEG geometry opti- mization were studied in detail on the basis of the Improved Powell Method. The results show that the optimal values of the geometry parameters and the interfacial temperatures between the adjacent seg- ments, either for maximizing the specific output power or the conversion efficiency, all vary with the changing hot- and cold-junction temperatures. Con- sequently, the traditional idea that the interfacial temperature for a segmented leg can be simply determined by the intersection temperatures of the ZT curves or the CP curves of the adjacent segment materials was less accurate. The comparison between the Improved Powell method and the traditional ZT (or CP) method will be presented in a future publication.

## ACKNOWLEDGEMENTS

This work was financially supported by the Na- tional Natural Science Foundation of China (No. 51272198), the National High-tech R&D Program of China (863 Program, No. 2012AA051104), the International S&T Cooperation Program of China (2014DFA63070), and the Fundamental Research Funds for the Central Universities (WUT, Nos. 2014-VII-009 and 2014-zy-063).

## REFERENCES

1. M.S. El-Genk, H.H. Saber, and T. Caillat, *Energy Convers. Manag.* 44, 1755 (2003).
2. L.N. Vikhor and L.I. Anatychuk, *Energy Convers. Manag.* 50, 2366 (2009).
3. X. Jia and Y. Gao, *Appl. Therm. Eng.* 73, 335 (2014).
4. H.S. Kim, K. Kikuchi, T. Itoh, T. Iida, and M. Taya, *Mater. Sci. Eng. B Adv.* 185, 45 (2014).

5. X. Sun, X. Liang, G. Shu, H. Tian, H. Wei, and X. Wang, *Energy* 77, 489 (2014).
6. H. Tian, N. Jiang, Q. Jia, X. Sun, G. Shu, and X. Liang, *Energy Proced.* 75, 590 (2015).
7. T.S. Ursell and G.J. Snyder, in *Proceedings of Twenty-First International Conference on Thermoelectrics* (2002), p. 412.
8. G.J. Snyder, *Appl. Phys. Lett.* 84, 2436 (2004).
9. G.J. Snyder, *Thermoelectrics Handbook, Micro-to-Nano*, ed. D.M. Rowe (Boca Raton: CRC-Press, 2005), p. 1.
10. N. Pham Hoang, D.V. Christensen, G.J. Snyder, H. Le Thanh, S. Linderoth, N. Van Ngo, and N. Pryds, *Phys. Status Solidi A* 211, 9 (2014).
11. M. Lazard, E. Rapp, and H. Scherrer, in *5th European Conference on Thermoelectrics* (2007), p. 187.
12. J. Wang, X. Tang, H. Liu, X. Yang, and Q. Zhang, *J. Wuhan Univ. Technol.* 21, 126 (2006).
13. G. Zhang, L. Fan, Z. Niu, K. Jiao, H. Diao, Q. Du, and G. Shu, *Energy Convers. Manag.* 106, 510 (2015).
14. H.H. Saber and M.S. El-Genk, in *Proceedings of Twenty- First International Conference on Thermoelectrics* (2002), p. 404.
15. G. Zhang, K. Jiao, Z. Niu, H. Diao, Q. Du, H. Tian, and G. Shu, *Int. J. Heat Mass Transf.* 93, 1034 (2016).
16. J. Schilz, L. Helmers, W.E. Muller, and M. Niino, *J. Appl. Phys.* 83, 1150 (1998).
17. B.W. Swanson, E.V. Somers, and R.R. Heikes, *J. Heat Transf.* 83, 77 (1961).
18. M. Picard, S. Turenne, D. Vasilevskiy, and R.A. Masut, *J. Electron. Mater.* 42, 2343 (2013).
19. J. D'Angelo, E.D. Case, N. Matchanov, C. Wu, T.P. Hogan, J. Barnard, C. Cauchy, T. Hendricks, and M.G. Kanatzidis, *J. Electron. Mater.* 40, 2051 (2011).
20. H. Tian, X. Sun, Q. Jia, X. Liang, G. Shu, and X. Wang, *Energy* 84, 121 (2015).
21. M.S. El-Genk and H.H. Saber, in *Space Technology and Applications International Forum* (Staif 2002) p. 980.
22. L. Cai, P. Li, Q. Luo, W. Huang, P. Zhai, and Q. Zhang, *PI Mech Eng C-J Mec* 229, 465 (2015).
23. M.J.D. Powell, *Comput. J.* 7, 155 (1964).
24. W. Cao, J. Wu, N. Jenkins, C. Wang, and T. Green, *Appl. Energy* 165, 36 (2016).
25. S. Lazarou, V. Vita, and L. Ekonomou, *IET Sci. Meas. Technol.* 5, 77 (2011).