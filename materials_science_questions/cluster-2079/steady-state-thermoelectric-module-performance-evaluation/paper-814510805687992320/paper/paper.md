# Critical Concentration Ratio for Solar Thermoelectric Generators

NAVEED UR REHMAN¹ and MUBASHIR ALI SIDDIQUI¹,²

1.—Solar Energy Lab, Mechanical Engineering Department, NED University of Engineering and Technology, University Road, Karachi 75270, Pakistan. 2.—e-mail: mubashir@neduet.edu.pk

A correlation for determining the critical concentration ratio (CCR) of solar concentrated thermoelectric generators (SCTEGs) has been established, and the significance of the contributing parameters is discussed in detail. For any SCTEG, higher concentration ratio leads to higher temperatures at the hot side of modules. However, the maximum value of this temperature for safe operation is limited by the material properties of the modules and should be considered as an important design constraint. Taking into account this limitation, the CCR can be defined as the maximum concentration ratio usable for a particular SCTEG. The established correlation is based on factors associated with the material and geometric properties of modules, thermal characteristics of the receiver, installation site attributes, and thermal and electrical operating conditions. To reduce the number of terms in the correlation, these factors are combined to form dimensionless groups by applying the Buckingham Pi theorem. A correlation model containing these groups is proposed and fit to a dataset obtained by simulating a thermodynamic (physical) model over sampled values acquired by applying the Latin hypercube sampling (LHS) technique over a realistic distribution of factors. The coefficient of determination and relative error are found to be 97% and ±20%, respectively. The correlation is validated by comparing the predicted results with literature values. In addition, the significance and effects of the Pi groups on the CCR are evaluated and thoroughly discussed. This study will lead to a wide range of opportunities regarding design and optimization of SCTEGs.

Key words: Solar thermoelectric generators, concentration ratio, dimensionless analysis, regression, Latin hypercube, sensitivity analysis

## INTRODUCTION

Solar thermal electricity generation relies on conversion of the thermal component of solar energy to electricity.¹,² Conversion methods employed on a large scale generally rely on a heating fluid which eventually drives a turbine or engine to produce electricity.³⁻⁵ On the other hand, application of thermoelectricity offers an alternative approach to convert solar thermal energy to electricity.⁶ The heart of these systems is a thermoelectric generator (TEG) module consisting of several thermocouples connected electrically in series and thermally in parallel. These modules offer several advantages based on their solid-state nature, including silent operation because of the absence of moving parts, reliability, and scalability.⁷ However, such systems are only suitable for microscale power generation, since they have low conversion efficiency.⁸ A thermoelectric module produces an electric potential difference proportional to the temperature difference across its two surfaces.⁹ One option to obtain such a temperature difference is to use a solar concentrated collector to concentrate solar heat flux directly onto the module. Such a system is called a solar concentrated thermoelectric generator (SCTEG) herein.

(Received March 7, 2016; accepted May 21, 2016)

Published online: 14 June 2016

![](./images/814510805687992320_1.jpg)

Typically, a SCTEG uses solar concentrating devices to focus incident solar radiation from a larger area onto one (the hot) side of the modules. $^{10}$ Simultaneously, the other (cold) side is cooled by means of convective heat transfer techniques. As an example, a parabolic trough-type SCTEG is shown in Fig. 1. Such a configuration results in a temperature difference across the two surfaces of the modules. Power can be produced on application of an electric load, and the extent of generation is proportional to the temperature difference. Higher solar heat flux yields greater temperature difference and accordingly more power. The concentration ratio is an important characteristic of any SCTEG. $^{11}$ For any type of concentrating device, the concentration ratio can be defined as

$$
C = A_{\mathrm{c}}/A_{\mathrm{r}}, \tag{1}
$$

where $A_{\mathrm{c}}$ (m²) is the aperture area of the collector where incident solar radiation is collected and $A_{\mathrm{r}}$ (m²) is the area of the receiver upon which it is focused.

For given incident solar flux, a concentrating collector with higher concentration ratio will focus more solar radiation onto the receiver. For a SCTEG, higher solar flux will lead to higher temperatures on the hot side of modules. However, hot-side temperatures for safe operation are limited by the material properties of the modules and should be considered as an important SCTEG design constraint. Taking into account this limitation, the critical concentration ratio (CCR) can be defined as the maximum concentration ratio for the collectors applied in a particular SCTEG. $^{12,13}$

The CCR depends upon several factors, including the material and geometric properties of the modules, thermal losses at the hot side, cooling method deployed at the cold side, electrical load connected, and frequent highest solar flux and ambient temperature expected at the installation site during the planned days of operation. It is obvious that, for given receiver area, increasing the concentration ratio leads to concentrating devices with larger aperture, which may increase land, manufacturing, installation, and operational costs. Therefore, efforts to understand the impact of the aforementioned factors on the CCR are always desirable.

A thermodynamic model based on the physical phenomena of SCTEG operation can provide an elementary means of connecting these factors and evaluating the CCR. However, due to the number of factors involved, any method that can reduce their count by combining them will assist in producing more comprehensible results. Dimensional analysis using the Buckingham Pi theorem is a well-known technique that has been widely used for this purpose. $^{14,15}$ Based on the principle dimensions of the response and independent variables (i.e., CCR and factors, respectively), dimensionless groups obtained by combining several factors, known as Pi terms, are derived. Also, as a Pi term containing the response variable will depend on other Pi terms, a suitable correlation between them can be established. This requires substitution of an experimentally compiled dataset (consisting of both Pi terms and the response) into a chosen correlation model. Subsequently, the suitability of this correlation model along with the relative errors between predicted and actual results must be quantified and analyzed.

For optimization, understanding the impact of each of the dimensionless groups on the SCTEG design is of utmost importance. This can be accomplished by means of sensitivity analysis. For this

![](./images/814510805687992320_2.jpg)

Fig. 1. Example SCTEG using a parabolic trough-type concentrating collector. Solar radiation is collected over a large collector aperture and focused onto one side of the modules by a reflecting concentrator. The other side of the modules is cooled with the help of a coolant (e.g., water) flowing through channels. Selective coatings may also be applied to reduce radiation loss.

Critical Concentration Ratio for Solar Thermoelectric Generators

purpose, a correlation model is fit to a statistically standardized dataset to obtain a standardized correlation. The resulting numerical values of the model exponents express the impact of the corresponding Pi terms on the response.¹⁶ A positive exponent indicates that an increase in the corresponding Pi term will increase the response, and vice versa, whereas a negative exponent indicates that an increase in the corresponding Pi term will decrease the response. The absolute value of each exponent describes the significance of the corresponding Pi term in the correlation model.

In addition to laboratory experiments, numerical experiments can also be carried out to establish such correlations and perform sensitivity analysis.¹⁷⁻¹⁹ Such experiments require a dataset consisting of a number of samples. Each sample contains a set of values, comprising one value for each independent factor in a desired range of interest. Several strategies are available to generate reliable datasets, such as random sampling and Latin hypercube sampling (LHS).²⁰ Among these, LHS is famous for use with models with high computational demands.²¹,²² The thermodynamic model is solved for the desired response for each sample, and a dataset consisting of the prior dataset and the response is compiled.

Herein, we present a numerically derived correlation for estimating the CCR of any SCTEG. The established correlation is based on meaningful dimensionless groups, representing different material, geometrical, natural, and operational factors associated with the SCTEG design. The Buckingham Pi theorem is applied to derive these groups. The dataset required for the numerical experiments was generated by the LHS technique. A thermodynamic model is also presented to understand the physical phenomena involved in SCTEG operation. Results obtained from the correlation are compared with results from literature studies. The physical interpretation of each group is discussed, and its numerical significance investigated for sensitivity analysis. The results of this study will enable designers and researchers to optimize SCTEGs for various applications.

## METHODOLOGY

An overview of the steps performed to establish the CCR correlation is illustrated in Fig. 2, as discussed in the subsections below.

### Thermodynamic Model

This section presents a steady-state one-dimensional thermodynamic model of an SCTEG based on energy balance. The flow of heat energy through an SCTEG occurs in the order: (i) accumulation, (ii) conversion, and (iii) liberation, as illustrated in Fig. 3.

In accumulation, solar radiation falling on the collector aperture is concentrated onto the hot side of the module. Subject to the thermal properties of the receiving surface, only a fraction of the heat energy in this radiation is absorbed. These properties may, however, be improved if desired by applying a suitable selective coating.²³,²⁴ Also, thermal convective effects may further reduce this accumulation of heat energy, resulting in a loss. Assuming that there are no optical losses in the concentrator device, the energy accumulated at the hot side of the module ($Q_{\text{h}}$, watts) can be formulated as

$$
Q_{\text{h}} = A_{\text{r}} \left[ G C \alpha_{\text{r}} - \varepsilon_{\text{r}} \sigma (T_{\text{h}}^{4} - T_{\text{a}}^{4}) - h_{\text{h}} (T_{\text{h}} - T_{\text{a}}) \right], \quad (2)
$$

where $A_{\text{r}}$ (m²), $\alpha_{\text{r}}$, $\varepsilon_{\text{r}}$, and $T_{\text{h}}$ (K) are, respectively, the area, absorptivity, emissivity, and temperature of the module surface (or selective coating, if applied) receiving the concentrated solar radiation, $G$ (W/m²) is the magnitude of the solar flux incident on the collector aperture, $C$ is the concentration ratio, $h_{\text{h}}$(W/m²-K) is the hot-side heat transfer convection coefficient, $T_{\text{a}}$ (K) is the ambient temperature, and $\sigma$ ($5.67 \times 10^{-8}$ W/m²-K⁴) is the Stefan-Boltzmann constant.

The accumulated heat energy flows through the module. Transport of this heat energy is attributed not only to thermal conduction, but also to the Seebeck effect and Joule heating. Assuming that the material properties are independent of temperature,²⁵ this rate of heat transfer can be written as²⁶:

$$
Q_{\text{h}} = S T_{\text{h}} I + K (T_{\text{h}} - T_{\text{c}}) - \frac{1}{2} I^{2} R, \quad (3)
$$

where $S$ (V/K), $K$ (W/K), and $R$ ($\Omega$) are the Seebeck coefficient, thermal conductance, and electric resistance of the module, respectively, $I$ (A) is the electric current flowing through the module, and $T_{\text{c}}$ (K) is the cold-side temperature of the module.

A module consists of several thermocouples, and its properties can be stated in terms of the intrinsic (material and geometric) properties of the thermocouples as

$$
S = n \alpha, \quad (4)
$$

$$
K = n \lambda G_{\text{f}}, \quad (5)
$$

$$
R = n \rho / G_{\text{f}}, \quad (6)
$$

where $n$ is the number of thermocouples in the module, $\alpha$ (V/K), $\lambda$ (W/m-K), and $\rho$ ($\Omega$ m) are the Seebeck coefficient, thermal conductivity, and electric resistivity of combined $p$- and $n$-type thermopiles (two legs of a thermocouple), respectively, and $G_{\text{f}}$ (m) is a geometric factor defined as the ratio of the cross-sectional area to length of the thermopiles. Another important term related to these material properties is the figure of merit denoted by $Z$ (K⁻¹), where

$$
Z = S^{2} / R K = \alpha^{2} / \rho \lambda. \quad (7)
$$

High figure of merit corresponds to an efficient module consisting of thermocouples with high

![](./images/814510805687992320_3.jpg)

Fig. 2. Flowchart describing steps involved in establishing CCR correlation: (1) building thermodynamic model, (2) choosing independent factors, (3) performing dimensional analysis, (4) proposing a suitable correlation model, (5) assigning statistical distributions to factors, (6) deploying sampling (LHS) technique to yield dataset, (7) solving thermodynamic model using samples in dataset, (8) generating response column and compiling dataset, (9) fitting correlation model to compiled dataset, (10) establishing CCR correlation (coefficient, exponents, and statistics), (11) standardizing compiled dataset, (12) establishing standardized CCR correlation (exponents) for sensitivity analysis.

![](./images/814510805687992320_4.jpg)

Fig. 3. Schematic diagram of typical SCTEG showing different devices and energy flows.

Seebeck coefficient and low electrical resistance and thermal conductance.

As per the working principle of thermoelectric generation, part of the transported heat energy is converted to electric work. For given module properties, the conversion depends on the temperature difference between the hot and cold sides of the module and the connected electric load to which power is delivered. A conventional way to describe the electric load in terms of the dimensionless ratio

Critical Concentration Ratio for Solar Thermoelectric Generators

of resistances, hereinafter called the matching load,
is considered as
$$
M=R_{\mathrm{L}} / R, \tag{8}
$$
where $R_{\mathrm{L}}$ ($\Omega$) is the connected electric load.

The electric power output ($P$, watts) and the
current flowing through the load can be written as
$$
P=\frac{\left[S\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)\right]^{2}}{R} \frac{M}{(M+1)^{2}}, \tag{9}
$$

$$
I=\frac{S\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)}{R(M+1)}. \tag{10}
$$

The remaining, unconverted part of the trans-
ported heat energy ($Q_{\mathrm{c}}$, $\mathrm{W/m^2}$) can be quantified as
$$
Q_{\mathrm{c}}=Q_{\mathrm{h}}-P. \tag{11}
$$

Note that this heat energy has to be removed from
the cold side of the module, or it will increase the
cold-side temperature and eventually reduce the
power output. This liberation of heat energy is
generally assisted by convective heat transfer. The
amount of heat energy removed at the cold side of
the modules can be represented as
$$
Q_{\mathrm{c}}=h_{\mathrm{c}} A_{\mathrm{r}}\left(T_{\mathrm{c}}-T_{\mathrm{a}}\right), \tag{12}
$$
where $h_{\mathrm{c}}$ ($\mathrm{W/m^2}$-K) is the cold-side heat transfer
convection coefficient.

If the modules are square in shape with side $L$
(m), the area of a module can be written as
$$
A_{\mathrm{r}}=L^{2}. \tag{13}
$$

To evaluate the CCR, the highest expected solar
flux during SCTEG operation ($G_{\mathrm{max}}$, $\mathrm{W/m^2}$) and the
maximum bearable hot-side temperature of a mod-
ule ($T_{\mathrm{max}}$, K) should be taken into account, such that
$$
C=\mathrm{CCR}, \tag{14}
$$

$$
G=G_{\mathrm{max}} \tag{15}
$$

$$
T_{\mathrm{h}}=T_{\mathrm{max}}. \tag{16}
$$

When evaluating the CCR, the material proper-
ties, ambient temperature, hot- and cold-side heat
transfer convection coefficients, and matching load
represent the design, natural, and operational
parameters of the SCTEG, respectively.

### Independent Factors

To describe the considered problem adequately,
14 independent factors were chosen from the ther-
modynamic model as follows:
$$
\begin{aligned}
\mathrm{CCR}=f(\alpha, \rho, \lambda, G_{\mathrm{f}}, n, L, T_{\mathrm{max}}, \varepsilon_{\mathrm{r}}, \alpha_{\mathrm{r}}, T_{\mathrm{a}}, G_{\mathrm{max}}, h_{\mathrm{h}}, h_{\mathrm{c}}, M),
\tag{17}
\end{aligned}
$$
where $\alpha$, $\rho$, $\lambda$, $G_{\mathrm{f}}$, $n$, $L$, and $T_{\mathrm{max}}$ represent module
material and geometrical properties, $\varepsilon_{\mathrm{r}}$ and $\alpha_{\mathrm{r}}$
characterize hot-side (or selective coating) thermal
properties, $T_{\mathrm{a}}$ and $G_{\mathrm{max}}$ are site attributes, while
$h_{\mathrm{h}}$, $h_{\mathrm{c}}$, and $M$ depend on the thermal and electric
operating conditions. The SI units of these factors
are listed in Table I.

### Dimensional Analysis

The Buckingham Pi theorem was applied on the
chosen independent factors to establish dimension-
less groups, which will serve as important charac-
teristic parameters for investigating the CCR of any
SCTEG. While performing dimensional analysis,
the number of principle dimensions was minimized
to four by assuming $\Psi = \mathrm{M\ T^{-3}}$ in $\mathrm{M\ L\ t\ \theta\ A}$, yield-
ing a reduced system of dimensions of $\Psi\ \mathrm{L\ \theta\ A}$,
where M stands for mass, L for length, t for time, $\theta$
for temperature, and A for current. The reduced
dimensions of all the factors are listed in Table I.

To derive the Pi terms, $\alpha$, $\rho$, $\lambda$, and $G_{\mathrm{f}}$ were chosen
as repeating variables. These variables have dis-
tinct dimensions and are independent of each other.
Eventually, 11 Pi terms were derived. One may note
that these factors represent intrinsic module mate-
rial and geometric properties. To obtain overall
higher SCTEG efficiency, it is obvious that a
designer must select a module with appropriate
material properties. Commercial availability and
cost may also be constraints on module choice.
However, this selection can easily be performed in
the earlier stages of system design.

### Correlation Model

Each of the derived Pi groups has a unique impact
on the CCR. The following model was proposed to
estimate the CCR based on the derived Pi terms:
$$
\begin{aligned}
\mathrm{CCR}=\pi_{1}=a \cdot \pi_{2}^{b} \cdot \pi_{3}^{c} \cdot \pi_{4}^{d} \cdot \pi_{5}^{e} \cdot \pi_{6}^{f} \cdot \pi_{7}^{g} \cdot \pi_{8}^{h} \cdot \pi_{9}^{i} \cdot \pi_{10}^{j} \cdot \pi_{11}^{k},
\tag{18}
\end{aligned}
$$
where $\pi$ represents a Pi term (or dimensionless
group). Values of $a$ through $k$, i.e., the coefficient
and exponents, can be calculated by fitting this
model to an experimentally obtained dataset.

### Statistical Distributions

Sampling techniques generally require statistical
distributions of factors to generate the desired
samples. A uniform distribution was assigned to
each factor to give the same weight to each value of
the factors/variables. Realistic ranges of the factors
were chosen, as listed in Table I. Most of these

<table>
<caption>Table I. Factors (with SI units and reduced dimensions) chosen from the thermodynamic model for the analysis</caption>
<thead>
<tr>
<th>Factor</th>
<th>Symbol</th>
<th>Units</th>
<th>Dimensions</th>
<th>Chosen range</th>
</tr>
</thead>
<tbody>
<tr>
<td>Critical concentration ratio</td>
<td>CCR</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Seebeck coefficient of thermocouple</td>
<td>$\alpha$</td>
<td>$\mu$V/K</td>
<td>$\Psi$ L$^2$ A$^{-1}$ $\Theta^{-1}$</td>
<td>200–300</td>
</tr>
<tr>
<td>Electrical resistance of thermocouple</td>
<td>$\rho$</td>
<td>$\Omega$ cm</td>
<td>$\Psi$ L$^3$ A$^{-2}$</td>
<td>$0.5 \times 10^{-3}$–$1.5 \times 10^{-3}$</td>
</tr>
<tr>
<td>Thermal conductance of thermocouple</td>
<td>$\lambda$</td>
<td>W/cm-K</td>
<td>$\Psi$ L $\Theta^{-1}$</td>
<td>$0.5 \times 10^{-2}$–$1.5 \times 10^{-2}$</td>
</tr>
<tr>
<td>Geometric factor of thermocouple</td>
<td>$G_{\text{f}}$</td>
<td>cm</td>
<td>L</td>
<td>0.04–0.4</td>
</tr>
<tr>
<td>Number of thermocouples in module</td>
<td>$n$</td>
<td>–</td>
<td>–</td>
<td>90–300</td>
</tr>
<tr>
<td>Length of module</td>
<td>$L$</td>
<td>mm</td>
<td>L</td>
<td>30–60</td>
</tr>
<tr>
<td>Temperature of hot side of module</td>
<td>$T_{\text{max}}$</td>
<td>K</td>
<td>$\Theta$</td>
<td>373–873</td>
</tr>
<tr>
<td>Emissivity of hot side of module (or selective coating)</td>
<td>$\varepsilon_{\text{r}}$</td>
<td>–</td>
<td>–</td>
<td>0.01–0.3</td>
</tr>
<tr>
<td>Absorptivity of hot side of module (or selective coating)</td>
<td>$\alpha_{\text{r}}$</td>
<td>–</td>
<td>–</td>
<td>0.7–1.0</td>
</tr>
<tr>
<td>Ambient temperature</td>
<td>$T_{\text{a}}$</td>
<td>K</td>
<td>$\Theta$</td>
<td>298–323</td>
</tr>
<tr>
<td>Maximum expected solar flux incident on collector</td>
<td>$G_{\text{max}}$</td>
<td>W/m$^2$</td>
<td>$\Psi$</td>
<td>300–1000</td>
</tr>
<tr>
<td>Convection coefficient at hot side of module</td>
<td>$h_{\text{h}}$</td>
<td>W/m$^2$-K</td>
<td>$\Psi$ $\Theta^{-1}$</td>
<td>5–50</td>
</tr>
<tr>
<td>Convection coefficient at cold side of module</td>
<td>$h_{\text{c}}$</td>
<td>W/m$^2$-K</td>
<td>$\Psi$ $\Theta^{-1}$</td>
<td>500–1500</td>
</tr>
<tr>
<td>Ratio of external to internal electrical resistance</td>
<td>$M$</td>
<td>–</td>
<td>–</td>
<td>0.5–1.5</td>
</tr>
</tbody>
</table>

The range of each factor chosen for numerical experiments is also given.

ranges were taken from information available in literature and/or engineering judgment. $^{13,24,27}$

### Latin Hypercube Sampling Technique

This technique utilizes efficient stratification of a given distribution to generate the desired dataset consisting of as many samples as desired. The following steps are performed in LHS:

1.  Divide the range for each factor into equal-probability intervals (called bins).
2.  Pick one value randomly from each interval of a factor.
3.  Randomly rearrange the values for each factor.
4.  Develop the final samples by picking values for each factor, one by one, and pairing them with other factors.

To elaborate on this further, consider an example with three factors, say, A, B, and C, uniformly distributed in the different ranges of 0 to 10, 0.0 to 1.0, and 100 to 1000, respectively. If we are to generate four samples, the ranges of each factor are divided into four (25%) equal-probability intervals, as presented in Table II.

Now, a value of each factor is picked randomly from each interval to form a data column. These values are randomly rearranged within their respective columns and placed adjacently to yield a dataset, as presented in Table III.

This procedure was applied to generate a dataset consisting of factors for the problem considered herein.

### Numerical Experiments

The effects on and significance for the CCR of each Pi term greatly depend on the arithmetic sign and absolute value of the corresponding exponent. To evaluate these values, numerical experiments were carried out in this study. After having generated the dataset, the numerical experiments involved: (i) solving the model against each sample in the input dataset, (ii) fitting the correlation model over the actual and/or standardized dataset, and (ii) quantifying the adequacy of samples, the suitability of the correlation model, and the relative errors.

A standardized dataset can be obtained by subtracting the column mean and dividing by the column standard deviation for each value in that column. This procedure was applied for each column (and hence each factor) of the compiled dataset. Mathematically,
$$
x' = \frac{x - \overline{x}}{\sigma}, \tag{19}
$$
where $x',x,\overline{x}$, and $\sigma$ are the standardized value, actual value, column mean, and column standard deviation, respectively.

The adequacy of the number of samples can be verified by converging values of the cumulative average of the response (CCR) with the number of runs, as illustrated in Fig. 5.

The suitability of the chosen correlation model can be quantitatively expressed in terms of the coefficient of determination, $R^2$, calculated as $^{28}$ It can be expressed as:

Critical Concentration Ratio for Solar Thermoelectric Generators

**Table II. Illustrating LHS: factors, ranges, and equal-probability intervals**

| Factor | Range   | 25% equal-probability intervals (Bins) |
|--------|---------|----------------------------------------|
|        |         | 0–2.5       | 2.5–5        | 5–7.5        | 7.5–10       |
| A      | 0–10    | 0–0.25      | 0.25–0.50    | 0.50–0.75    | 0.75–1.0     |
| B      | 0.0–1.0 | 100–125     | 125–150      | 150–175      | 175–200      |
| C      | 100–200 |             |              |              |              |

**Table III. Illustrating LHS: forming columns and dataset**

<table>
  <thead>
    <tr>
      <th rowspan="2">Interval no.</th>
      <th colspan="3">Data columns</th>
      <th rowspan="2">Sample no.</th>
      <th colspan="3">Dataset</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0.23</td>
      <td>112</td>
      <td>1</td>
      <td>4</td>
      <td>0.62</td>
      <td>168</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>0.48</td>
      <td>145</td>
      <td>2</td>
      <td>1</td>
      <td>0.48</td>
      <td>112</td>
    </tr>
    <tr>
      <td>3</td>
      <td>6</td>
      <td>0.62</td>
      <td>168</td>
      <td>3</td>
      <td>9</td>
      <td>0.78</td>
      <td>192</td>
    </tr>
    <tr>
      <td>4</td>
      <td>9</td>
      <td>0.78</td>
      <td>192</td>
      <td>4</td>
      <td>6</td>
      <td>0.23</td>
      <td>145</td>
    </tr>
  </tbody>
</table>

$$
R^{2}=\frac{\sum\left(\mathrm{CCR}_{\mathrm{c}}-\overline{\mathrm{CCR}_{\mathrm{t}}}\right)^{2}}{\sum\left(\mathrm{CCR}_{\mathrm{t}}-\overline{\mathrm{CCR}_{\mathrm{t}}}\right)^{2}},\tag{20}
$$

where $\mathrm{CCR_c}$ and $\mathrm{CCR_t}$ are the critical concentration ratios obtained by the correlation and thermodynamic model, respectively. $\overline{\mathrm{CCR_t}}$ is the average value of all responses obtained by the thermodynamic solutions.

In addition, the relative error $(\xi)$ indicates the accuracy of prediction, i.e., how close the correlation is to predicting the actual result.¹⁵ In this study, the relative error can be obtained mathematically as

$$
\xi=\frac{\mathrm{CCR}_{\mathrm{t}}-\mathrm{CCR}_{\mathrm{c}}}{\mathrm{CCR}_{\mathrm{c}}}.\tag{21}
$$

## RESULTS AND DISCUSSION

### Dimensionless Groups

Eleven Pi terms (one containing the response and the remaining ten pertaining to each factor) were derived, as listed in Table IV. Each of these terms is associated with important and distinct physical phenomena or system attributes, based on either the nonrepeating variables in a Pi term or by the Pi term as a whole. $\pi_1$ is the response Pi term which explicitly contains the CCR variable. The Pi terms $\pi_2$ through $\pi_4$ represent module properties. $\pi_5$ and $\pi_6$ dictate the surface optical characteristics at the receiving side of the module (or selective coating). $\pi_7$ and $\pi_8$ represent natural characteristics of the installation site. The remaining Pi terms, $\pi_9$ through $\pi_{11}$, represent thermal and electrical operating conditions of the SCTEG. Note that $\lambda/G_{\mathrm{f}}$ is denoted as $Y$ (W/m²K) in $\pi_8$ through $\pi_{10}$, representing another combination of intrinsic properties of the thermocouples.

### Sampling and Numerical Experiments

A dataset comprising 500 samples was generated using LHS, and the distribution of each factor confirmed from the respective histograms. As an example, the histogram for solar radiation is shown in Fig. 4.

The sample size was set after several trials, by gradually increasing the number of samples from 100 in steps of 50, and observing when the cumulative average of the response (CCR) became smooth. For each new sample size, a unique dataset was generated by picking values from new bins. The thermodynamic model was also solved each time for all samples (using equation solver software²⁹).

Figure 5 depicts that, when the number of samples reached 150, the cumulative average of the response became less fluctuating and hence converged. However, to ensure adequacy, 500 samples were taken.

### CCR Correlation and Validation

The correlation model was fit to the dataset, and the coefficient and exponents were determined to obtain a correlation consisting of 10 Pi groups, as presented in Table V. The coefficient of determination ($R^2$) was found to be 97%. Also, by plotting the histogram of relative errors $(\xi)$ as shown in Fig. 6, it was found that most of these errors were in the range of ±20%.

<table>
<caption>Table IV. Pi terms with their definition and interpretation as derived by dimensional analysis using the Buckingham Pi theorem</caption>
<thead>
<tr>
<th>Group</th>
<th>Definition</th>
<th>Interpretation</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\pi_1$</td>
<td>CCR</td>
<td>Output</td>
</tr>
<tr>
<td>$\pi_2$</td>
<td>$n$</td>
<td>Module material and geometrical characteristics</td>
</tr>
<tr>
<td>$\pi_3$</td>
<td>$L^* = L/G_{\text{f}}$</td>
<td></td>
</tr>
<tr>
<td>$\pi_4$</td>
<td>$T_{\text{max}}^* = ZT_{\text{max}}$</td>
<td></td>
</tr>
<tr>
<td>$\pi_5$</td>
<td>$\varepsilon_{\text{r}}$</td>
<td>Thermal characteristics of receiver (hot side of module or selective absorber)</td>
</tr>
<tr>
<td>$\pi_6$</td>
<td>$\alpha_{\text{r}}$</td>
<td></td>
</tr>
<tr>
<td>$\pi_7$</td>
<td>$T_{\text{a}}^* = ZT_{\text{a}}$</td>
<td>Site characteristics</td>
</tr>
<tr>
<td>$\pi_8$</td>
<td>$G^* = ZG_{\text{max}}/Y$</td>
<td></td>
</tr>
<tr>
<td>$\pi_9$</td>
<td>$h_{\text{h}}^* = h_{\text{h}}/Y$</td>
<td>Thermal and electrical operating conditions</td>
</tr>
<tr>
<td>$\pi_{10}$</td>
<td>$h_{\text{c}}^* = h_{\text{c}}/Y$</td>
<td></td>
</tr>
<tr>
<td>$\pi_{11}$</td>
<td>$M$</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/814510805687992320_5.jpg)

Fig. 4. Histogram of samples generated for solar radiation (G, W/$\text{m}^2$) as an example to confirm that the distribution is similar to that chosen.

![](./images/814510805687992320_6.jpg)

Fig. 5. Cumulative average of CCR versus number of runs. The graph gradually becomes smooth after 150 runs.

The established correlation was validated by comparing its predictions with literature results. Work performed by Atik¹² and Li et al.¹³ on CCR evaluation was taken as reference. The simulation parameters chosen in their studies were transformed to form Pi terms as discussed herein; For example, $\pi_3$ was obtained by dividing the module length ($L$) by the geometric factor $G_{\text{f}}$, being 10 cm and 0.77 cm, respectively, in the work of Atik.¹² These values yield 129.9 for $\pi_3$. In Li et al.,¹³ the module length and geometric factor are 29 mm and 0.43 mm (1.3 mm × 1.3 mm/3.9 mm), respectively, yielding 66.97 for $\pi_3$. The established correlation was solved using these Pi terms, and the results compared as presented in Table VI. It can be seen that, in both cases, the prediction by the correlation agrees well with the published results; For instance, the CCR is 17.01 as per our thermo-dynamic model and 17.76 as per our correlation, comparable to the value of 17.0 obtained by Atik.¹² Hence, the proposed correlation can be used in SCTEG design with a good level of confidence.

### Sensitivity Analysis
Sensitivity analysis was performed to assess the impact of individual Pi terms on the CCR, for which the dataset was statistically normalized and the model fit to the dataset to obtain the exponents, as presented in Table V. Note that the coefficient $a$ disappears in the standardized correlations.

In Fig. 7, the Pi terms are sorted according to their impact on the CCR. Among them, $T_{\text{max}}^*$ shows the greatest impact on the CCR. This is because a module that can bear higher temperatures can tolerate greater concentration values, for given material properties. This may also be interpreted as saying that, for a particular value of maximum hot-side temperature, a module with good figure of merit will have higher CCR. In both cases, any effort to raise the CCR will increase the power output.

The next two highest impacting terms are $G^*$ and $T_{\text{a}}^*$, which represent installation site characteristics. Their negative effects limit the upper bound on the CCR. This is because higher solar flux and ambient temperature will increase the hot-side temperature of the module even for a smaller concentration ratio of the SCTEG. This also dictates that sites with

Critical Concentration Ratio for Solar Thermoelectric Generators

Table V. Model coefficient and exponents, and standardized exponents determined by fitting the correlation model to regular and normalized datasets, respectively

| Model coefficient and exponents | Corresponding dimensionless group | Model coefficient and exponent values | Standardized model exponent values |
|----------------------------------|------------------------------------|---------------------------------------|------------------------------------|
| $a$                              | —                                  | 0.170                                 | —                                  |
| $b$                              | $n$                                | 0.464                                 | 0.180                              |
| $c$                              | $L^*$                              | $-0.916$                              | $-0.640$                           |
| $d$                              | $T_{\text{max}}^*$                 | 2.640                                 | 1.670                              |
| $e$                              | $\varepsilon_{\text{r}}$           | $-0.002$                              | $-0.002$                           |
| $f$                              | $\alpha_{\text{r}}$                | $-1.040$                              | $-0.123$                           |
| $g$                              | $T_{\text{a}}^*$                   | $-1.360$                              | $-0.812$                           |
| $h$                              | $G^*$                              | $-1.000$                              | $-1.170$                           |
| $i$                              | $h_{\text{h}}^*$                   | 0.075                                 | 0.079                              |
| $j$                              | $h_{\text{c}}^*$                   | 0.502                                 | 0.421                              |
| $k$                              | $M$                                | $-0.076$                              | $-0.027$                           |

![](./images/814510805687992320_7.jpg)

Fig. 6. Histogram showing that relative error values were most frequently within $\pm 20\%$.

![](./images/814510805687992320_8.jpg)

Fig. 7. Quantified impact of different Pi terms on CCR.

Table VI. Comparison between values predicted by established correlation and literature results

| Pi Terms                  | Atik¹²       | Li et al.¹³   |
|---------------------------|--------------|--------------|
| $\pi_2$                   | 127          | 98           |
| $\pi_3$                   | 129.9        | 66.97        |
| $\pi_4$                   | 1.111        | 1.96         |
| $\pi_5$                   | 0.02         | 0.08         |
| $\pi_6$                   | 0.8          | 0.9          |
| $\pi_7$                   | 0.6624       | 1.114        |
| $\pi_8$                   | 0.001104     | 0.001376     |
| $\pi_9$                   | 0.0004968    | 0.002406     |
| $\pi_{10}$                | 0.4968       | 0.4811       |
| $\pi_{11}$                | 1            | 1            |
| CCR (reference)           | 17           | 51           |
| CCR (thermodynamic model) | 17.01        | 50.95        |
| CCR (correlation)         | 17.76        | 55.60        |

good solar potential will require lower concentration ratio compared with sites having poor solar potential.

$L^*$ is next, having a substantial negative impact on the CCR and consisting of module and intrinsic geometrical properties. Modules with large surface area (Eq. 13) will accumulate more energy and hence result in higher temperatures, due to which the CCR must be lowered. $G_{\text{f}}$, an intrinsic property pertaining to the thermocouple, affects the CCR in such a way that thin thermocouples, having lower values of $G_{\text{f}}$, result in lower $K$ (Eq. 6) and higher $R$ (Eq. 6), which will lead to lower energy transport from the hot to cold side of the module (Eq. 3), giving rise to higher temperatures and thus leading to lower CCR values.

$h_{\text{c}}^*$ is the second term after $T_{\text{max}}^*$ to affect CCR proportionally. Dedicated cooling methods will not only result in higher CCR but also increase the power output. Adequate convection will contribute towards heat removal from the cold side, preventing heat accumulation at the hot side and resulting in the use of a higher concentration ratio. This is an effective Pi term that can be controlled operationally.

![](./images/814510805687992320_9.jpg)

Critical Concentration Ratio for Solar Thermoelectric Generators

![](./images/814510805687992320_10.jpg)

$n$ also shows proportionality with the value of CCR. This is because a module with more thermocouples will transport more accumulated energy, resulting in lower hot-side temperature. This ultimately contributes to increase the CCR of the SCTEG.

A selective coating with high $\alpha_{\mathrm{r}}$ is always desirable, as this increases the solar energy accumulation. However, such a value will limit the upper bound on the CCR, because of high hot-side temperatures. Thus, this has a negative effect on the CCR. On the other hand, high $h_{\mathrm{h}}$ is never desirable, as this reduces the solar energy accumulation and hence the power output. However, any loss in heat accumulation will increase the potential for raising the CCR. Therefore, the terms $\alpha_{\mathrm{r}}$ and $h_{\mathrm{h}}^{*}$ are directly associated with solar energy accumulation at the hot side and hence should be interpreted as increasing the power output. The remaining terms, $M$ and $\varepsilon_{\mathrm{r}}$, when selected within the chosen ranges, contribute almost negligibly to determining the CCR.

Figure 8 illustrates insights based on the sensitivity analysis. Each Pi term is normalized on the basis of its minimum and maximum values (considering Table I) and the CCR determined for the whole range, while keeping the other Pi terms constant at their mean value. The trend for $n$ is approximately linear and proportional. Within its range, the CCR changes from 60 to 100. The variation of the CCR is inversely proportional to $L^{*}$, being quite steep in the first half of its range, where the CCR drops from 700 to about 80, while thereafter the change is not very significant. The trend for $T_{\max }^{*}$ is also directly proportional, rising gradually for the first half of its values but sharply later. The CCR is essentially insensitive to $\varepsilon_{\mathrm{r}}$, only changing from 84.5 to 85.5. However, $\alpha_{\mathrm{r}}$ has an effective and decreasing effect on the CCR, decreasing the response from approximately 100 to 70. The trend for $T_{\mathrm{a}}^{*}$ and $G^{*}$ is strong in the first quarter of their values. The CCR drops from above 2000 to about less than 500. Both end up at a CCR value below 50. The CCR tends to vary directly with $h_{\mathrm{h}}^{*}$ and $h_{\mathrm{c}}^{*}$, although somewhat sharply with the former in the first half of its values. $M$ has little effect on the CCR, which only varies from 83 to 90.

## CONCLUSIONS

A correlation for determining the CCR of SCTEGs has been established based on several factors associated with material and geometric module characteristics, receiver (module hot side or selective absorber) thermal characteristics, site characteristics, and thermal and electrical operating conditions. To reduce the number of terms in the model, these factors were combined to form dimensionless groups called Pi terms using the Buckingham Pi theorem. A correlation model containing these Pi terms was proposed and fit to a dataset obtained by simulating the thermodynamic model over samples obtained by the LHS technique. The coefficient of determination and relative error of the correlation compared with the thermodynamic solution were found to be 97% and ±20%, respectively. The model was validated by comparing its predictions with literature results. In addition, the significance of the Pi groups is also discussed based on the model exponents determined from a statistically standardized dataset. These exponents describe the effect of and significance for the CCR of the corresponding Pi terms. As expected, it was found that the maximum temperature that a module could bear had the greatest impact on the CCR, followed by the site characteristics including solar flux and ambient temperature. These terms limit the upper bound on the CCR. The cooling method was found to be the only effective term that could be controlled operationally. This study will enable a wide range of opportunities for SCTEG design and optimization.

## REFERENCES

1. D. Mills, *Sol. Energy* (2004). doi:10.1016/S0038-092X(03)00102-6.
2. S.P. Sukhatme, *Indian Academy of Sciences Chemical Sciences Proceedings* (1997), pp. 521–531.
3. E. Zarza, L. Valenzuela, J. Leon, K. Hennecke, M. Eck, H.D. Weyers, and M. Eickoff, *Energy* (2004). doi:10.1016/S0360-5442(03)00172-5.
4. J. Schlaich, *The Solar Chimney: Electricity from the Sun* (Stuttgart: Edition Axel Menges, 1996), p. 12.
5. P.L. Geok, R. Affandi, A. Ghani, M. Ruddin, C.K. Gan, and J. Zanariah, *Appl. Mech. Mater.* (2015). doi:10.4028/www.scientific.net/AMM.785.576.
6. H. Xi, L. Luo, and G. Fraisse, *Renew. Sustain. Energy Rev.* (2007). doi:10.1016/j.rser.2005.06.008.
7. S. Priya and D.J. Inman, *Energy Harvesting Technologies* (New York: Springer, 2009), pp. 323–336.
8. R. Amatya and R.J. Ram, *J. Electron. Mater.* (2010). doi:10.1007/s11664-010-1190-8.
9. D.K.C. MacDonald, *Thermoelectricity: An Introduction to the Principles* (New York: Dover, 2006), pp. 1–4.
10. A.I. Novikov, *J. Eng. Phys. Thermophys.* (2001). doi:10.1023/A:1016667129697.
11. Y. Cai, J. Xiao, W. Zhao, X. Tang, and Q. Zhang, *J. Electron. Mater.* (2011). doi:10.1007/s11664-011-1616-y.
12. K. Atik, *Energy Sources Part A* (2011). doi:10.1080/15567030903261873.
13. P. Li, L. Cai, P. Zhai, X. Tang, Q. Zhang, and M. Niino, *J. Electron. Mater.* (2010). doi:10.1007/s11664-010-1279-0.
14. B.R. Munson, D.F. Young, and T.H. Okiishi, *Fundamentals of Fluid Mechanics*, 1st ed. (New York: Wiley, 1990), pp. 388–393.

Rehman and Siddiqui

15. J.H. Lin, C.Y. Huang, and C.C. Su, *Int. Commun. Heat Mass Transf.* (2007). doi:10.1016/j.icheatmasstransfer.2006.12.002.

16. C.K. Ho, S.S. Khalsa, and G.J. Kolb, *Sol. Energy* (2011). doi:10.1016/j.solener.2010.05.004.

17. K.P. Bowman, J. Sacks, and Y.F. Chang, *J. Atmos. Sci.* (1993). 50(9), 1267–1278. .

18. K. Yamada, A. Yamaguchi, T. Takata, in *8th Japan Korea Symposium on Nuclear Thermal Hydraulics and Safety* (2012) Paper no.: N8P1091.

19. P.J. Marti and J.M. Pinazom, *Int. J. Therm. Sci.* (2003). doi:10.1016/S1290-0729(02)00038-8.

20. M.D. McKay, R.J. Beckman, and W.J. Conover, *Techno- metrics* (1979). doi:10.1080/00401706.1979.10489755.

21. J.C. Helton, J.D. Johnson, C.J. Sallaberry, and C.B. Stor- lie, *Reliab. Eng. Syst. Saf.* (2006). doi:10.1016/j. ress.2005.11.017.

22. J.C. Helton and F.J. Davis, *Reliab. Eng. Syst. Saf.* (2003). doi:10.1016/S0951-8320(03)00058-9.

23. J.A. Duffie and W.A. Beckman, *Solar Engineering of Thermal Processes*, 3rd ed. (New York: Wiley, 2006), p. 189.

24. R. Forristall, Report No. NREL/TP-550-34169, National Renewable Energy Laboratory, Colorado, October 2003.

25. D.M. Rowe, *Thermoelectrics Handbook* (Boca Raton: CRC Press, 2006), pp. 1–4.

26. C.T. Hsu, G.Y. Huang, H.S. Chu, B. Yu, and D.J. Yao, *Appl. Energy* (2011). doi:10.1016/j.apenergy.2011.07.033.

27. T.M. Tritt and M.A. Subramanian, *MRS Bull.* (2006). doi:10.1557/mrs2006.44.

28. R.E. Walpole, R.H. Myers, S.L. Myers, and K. Ye, *Proba- bility and Statistics for Engineers and Scientists*, 9th ed. (New York: Pearson, 2012), p. 407.

29. S.A. Klein, F.L. Alvarado. Engineering Equation Solver, http://www.fchart.com/ees/. Accessed 12 December 2015.