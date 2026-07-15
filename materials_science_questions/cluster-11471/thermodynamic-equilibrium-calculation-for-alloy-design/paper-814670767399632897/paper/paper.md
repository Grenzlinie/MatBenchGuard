ISSN 2075-1133, Inorganic Materials: Applied Research, 2014, Vol. 5, No. 6, pp. 587–596. © Pleiades Publishing, Ltd., 2014.
Original Russian Text © Yu.A. Dushin, A.S. Oryshchenko, Yu.A. Utkin, A.Z. Krasil'nikov, S.N. Petrov, 2013, published in Voprosy Materialovedeniya, 2013, No. 1(73), pp. 58–71.

# PHYSICAL METALLURGY.
## METALLURGY

# Prediction of the Phase Composition of the Refractory 45Cr26Ni33Si2Nb2 Alloy in the Process of Stabilization

Yu. A. Dushinⁱ, A. S. Oryshchenkoⁱ, Yu. A. Utkinⁱ, A. Z. Krasil’nikovⁱ, and S. N. Petrovⁱ

ⁱUstinov Baltic State Technical University (Voenmekh), ul. Pervaya Krasnoarmeiskaya 1, St. Petersburg, 190005 Russia
ⁱCentral Research Institute of Structural Materials PROMETEY, ul. Shpalernaya 49, St. Petersburg, 191015 Russia
e-mail: mail@crism.ru

Received September 9, 2011; in final form, January 13, 2013

Abstract—This paper is devoted to material aging in the operational temperature range of pyrolysis equipment. The EBSD analysis of the alloy phase composition after isothermal aging or stress-rupture tests at 800–1100°C for 1000–5000 h shows that the role of niobium and the two stable forms of its existence, namely, the G-phase $Nb_6Ni_{16}Si_7$ at a temperature below 900°C and carbide NbC above 1000°C, is crucial in the process of stabilization (thermodynamic equilibrium approach). The approximate dependences of the saturation concentration of carbon and the current concentration of carbides are in satisfactory agreement with numerical modeling and, at the same time, reveal the effect of temperature and doping either in a direct way (through the equilibrium constant, the specified concentrations of carbon, chromium, niobium) or via the activity coefficients of elements and their components.

Keywords: equipment of pyrolysis furnaces, refractory alloy, phase composition, EBSD analysis, aging, thermodynamic equilibrium

DOI: 10.1134/S2075113314060033

## INTRODUCTION

The 45Cr26Ni33Si2Nb2 alloy was developed as a fireproof refractory material [1, 2] designed to provide the prolonged operation of oil processing equipment. The phase composition of the alloy changes in the severe conditions of pyrolysis furnaces in the production of ethylene under the action of organic components of the process medium, and a homogeneous structure is formed along the thickness of a pyrolysis coil with a coke layer on its surface [3, 4]. These processes are combined with creep and deformation phenomena, so the resource of the material decreases [5, 6]. In [7], it is shown that the mechanical properties of pyrolysis coil materials depend directly on the operating time, and their stress-strained state is directly related to the current thickness of the carburized and coke layers. The diffusion of carbon and the formation of carbides occur simultaneously in the process of carburization and can be described by nonlinear differential equations. For this reason, it is necessary to turn to the limit variants with a “transparent” analytical result [8] or to search for a numerical solution using the diffusion-kinetic similarity criteria [9]. The study by the method of similarity theory [10, 11] seems to be the most efficient way. Such an approach in combination with experiments succeeds in a more correct prediction of carburization consequences [12, 13]. The objective of this work is to provide the procedure of prediction for the 45Cr26Ni33Si2Nb2 alloy with the data on the saturation concentration of carbon and the rate of its interaction with dopants. In essence, this is the calculation of thermal aging for the material. The elemental composition provided by the technical specifications was converted from mass fractions into atomic fractions (Table 1).

The temperature range of 800–1100°C incorporating the maximum temperature of a heat-exchange tube on the side of flue gases (1100°C) and the working surface temperature (800°C) was taken for the study. In the first place, it was necessary to ascertain what phases and concentrations of elements can be formed under such conditions and, thereupon, when a steady-

Table 1. Concentrations of elements in the alloy

<table>
  <thead>
    <tr>
      <th>Dimen- sion</th>
      <th>C</th>
      <th>Cr</th>
      <th>Ni</th>
      <th>Fe</th>
      <th>Mo</th>
      <th>Si</th>
      <th>Nb</th>
      <th>Mn</th>
      <th>Ti</th>
      <th>Y</th>
      <th>S</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wt %</td>
      <td>0.45</td>
      <td>26.9</td>
      <td>36.9</td>
      <td>29.8</td>
      <td>0.033</td>
      <td>1.56</td>
      <td>2.0</td>
      <td>0.94</td>
      <td>0.18</td>
      <td>0.013</td>
      <td>0.006</td>
      <td>0.0015</td>
    </tr>
    <tr>
      <td>At %</td>
      <td>0.021</td>
      <td>0.285</td>
      <td>0.345</td>
      <td>0.295</td>
      <td>0.001</td>
      <td>0.031</td>
      <td>0.012</td>
      <td>0.009</td>
      <td>0.002</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

<table>
<caption>Table 2. Equilibrium constants \(K_{\text{eq}}\) for reactions 1–8</caption>
<thead>
<tr>
<th>\(T\), °C</th>
<th>\(K_1\)</th>
<th>\(K_2\)</th>
<th>\(K_3\)</th>
<th>\(K_4\)</th>
<th>\(K_5\)</th>
<th>\(K_6\)</th>
<th>\(K_7\)</th>
<th>\(K_8\)</th>
</tr>
</thead>
<tbody>
<tr>
<td>800</td>
<td>1520</td>
<td>1380</td>
<td>243</td>
<td>\(4.5 \times 10^8\)</td>
<td>\(3.5 \times 10^6\)</td>
<td>1347</td>
<td>821</td>
<td>\(3.1 \times 10^8\)</td>
</tr>
<tr>
<td>1100</td>
<td>429</td>
<td>394</td>
<td>92</td>
<td>\(4.8 \times 10^6\)</td>
<td>\(1.2 \times 10^5\)</td>
<td>229</td>
<td>172</td>
<td>\(4.8 \times 10^6\)</td>
</tr>
</tbody>
</table>

state situation can be attained. Approximate analytical solutions help to reveal the individual role of the con- sidered parameters, and the validity of assumptions is verified by numerical methods and experimental data.

# THERMODYNAMIC PREREQUISITES¹

The major alloy components (C, Fe, Cr, Ni, Si, Nb, Mn, without microdopants and admixtures) can enter dozens of individual reactions. According to the recognized thermodynamic basis [14], these possibili- ties in the studied alloy are reduced by an order of magnitude and confined to eight reactions between carbon or silicon and other elements (e) by the type

$$\text{C (or Si)} + \frac{m}{n}\text{e} \rightleftharpoons \frac{1}{n}\text{C}_m\text{C (or Si)}_n:$$

$$\text{1. } \text{C} + \frac{23}{6}\text{Cr} \rightleftharpoons \frac{1}{3}\text{Cr}_{23}\text{C}_6;$$

$$\text{2. } \text{C} + \frac{7}{3}\text{Cr} \rightleftharpoons \frac{1}{3}\text{Cr}_7\text{C}_3;$$

$$\text{3. } \text{C} + \frac{3}{2}\text{Cr} \rightleftharpoons \frac{1}{2}\text{Cr}_3\text{C}_2;$$

$$\text{4. } \text{C} + 2\text{Nb} \rightleftharpoons \text{Nb}_2\text{C};$$

$$\text{5. } \text{C} + \text{Nb} \rightleftharpoons \text{NbC};$$

$$\text{6. } \text{C} + \text{Si} \rightleftharpoons \text{SiC};$$

$$\text{7. } \text{Si} + \frac{1}{2}\text{Nb} \rightleftharpoons \frac{1}{2}\text{NbSi}_2;$$

$$\text{8. } \text{Si} + \frac{5}{3}\text{Nb} \rightleftharpoons \frac{1}{3}\text{Nb}_5\text{Si}_3.$$

Here, the basic elements are carbon (silicon) and other elements (e) in a solution at the left and their compounds in a solid state at the right. The saturation concentrations of the components obtained as a result of the reactions are related to each other by the mate- rial balance equations for each element and the equi- librium constants \(K_{\text{eq}}\). For reactions 1–5 between carbon C and the metals Me,

$$\frac{1}{\left(\gamma_{\text{Me}}[\text{Me}]_{\text{eq}}\right)^{m/n} \gamma_{\text{C}}[\text{C}]_{\text{eq}}} = K_{\text{eq}}. \tag{1}$$

¹ Here, the concentrations of components are expressed in atomic (molar) fractions and given in brackets.

Here, \([\text{Me}]_{\text{eq}}\) and \([\text{C}]_{\text{eq}}\) are the atomic concentra- tions of an element in a solid solution in an equilib- rium state, \(\gamma_{\text{Me}}\) and \(\gamma_{\text{C}}\) are the activity coefficients, and \(m/n\) is the reaction order taken with regard to the sec- ond element. The activity coefficient of carbon \(\gamma_{\text{C}}\) was calculated as for doped austenite [15], the activity coefficients of dopants were taken according to [16], and a niobium solution was assumed to be ideal (\(\gamma_{\text{Nb}} \approx 1\)). The equilibrium constants in Table 2 were calculated as in [14] at boundary temperatures of the possible operating range.

For the 45Cr26Ni33Si2Nb2 alloy, the numerical solution of the set of material balance and thermody- namic equilibrium equations for reactions 1–8 results in a binary phase composition. In the studied temper- ature range, niobium is bonded to carbide NbC (the atomic fraction of [NbC] is nearly \(1.2 \times 10^{-2}\), being two orders of magnitude higher than \([\text{Nb}_2\text{C}]\)), and chromium forms only the most carbon-lean carbide \(\text{Cr}_{23}\text{C}_6\) with a concentration of \(1.1 \times 10^{-3}\) (800°C)—\(7.1 \times 10^{-4}\) (1100°C) atomic fractions. For this reason, the material balance equation is determined by carbon according to the equation

$$
\begin{gathered}
{[\text{C}]_0 = [\text{C}]_{\text{eq}} + \frac{6}{23}} \\
\times \left\{ [\text{Cr}]_0 - [\text{Cr}]_1 \right\} + [\text{Nb}]_0 - [\text{Nb}]_5,
\end{gathered} \tag{2}
$$

where \([\text{C}]_0\) is a specified initial content of carbon in the alloy, and the equilibrium concentrations of dopants in a solution according to Eq. (1) for reactions 1 and 5 are

$$
\begin{gathered}
{[\text{Cr}]_1 = \frac{1}{\gamma_{\text{Cr}}\left(K_1 \gamma_{\text{C}}[\text{C}]_{\text{eq}}\right)^{6/23}},} \\
{[\text{Nb}]_5 = \frac{1}{\gamma_{\text{Nb}}\left(K_5 \gamma_{\text{C}}[\text{C}]_{\text{eq}}\right)}.}
\end{gathered} \tag{3}
$$

Silicon does not enter reactions 6–8 with the other elements and must be in a dissolved state. However, there are some known silicides with the open formula \(\text{A}_6\text{B}_{16}\text{Si}_7\), where position A can be occupied, in partic- ular, by Cr and Nb, and position B can be occupied by Ni and Fe [17]. Similar compounds are commonly called the G phase. This phase was revealed in a cast alloy similar to 45Cr26Ni33Si2Nb2 in its composition (the principal distinction is 0.1 wt % of C instead of 0.45 wt %) after 8 years of operation at 760°C at the

<table><caption>Table 3. Saturation concentrations of compounds and active elements in the alloy</caption>
  <thead>
    <tr>
      <th rowspan="2">Temperature, °C</th>
      <th colspan="6">Concentration of components, atomic fractions</th>
    </tr>
    <tr>
      <th>[Nb₆Ni₁₆Si₇]ₑq</th>
      <th>[NbC]ₑq</th>
      <th>[Cr₂₃C₆]ₑq</th>
      <th>[C]ₑq</th>
      <th>[Nb]ₑq</th>
      <th>[Cr]ₑq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>800</td>
      <td>2 × 10⁻³</td>
      <td>0</td>
      <td>2.77 × 10⁻³</td>
      <td>4.29 × 10⁻³</td>
      <td>0</td>
      <td>0.221</td>
    </tr>
    <tr>
      <td rowspan="3">1100</td>
      <td>0</td>
      <td>1.2 × 10⁻²</td>
      <td>1.11 × 10⁻³</td>
      <td>2.33 × 10⁻³</td>
      <td>&lt;2.75 × 10⁻⁴</td>
      <td>0.259</td>
    </tr>
    <tr>
      <td>2 × 10⁻³</td>
      <td>0</td>
      <td>2.13 × 10⁻³</td>
      <td>8.27 × 10⁻³</td>
      <td>0</td>
      <td>0.236</td>
    </tr>
    <tr>
      <td>0</td>
      <td>≅1.2 × 10⁻²</td>
      <td>7.06 × 10⁻⁴</td>
      <td>5.04 × 10⁻³</td>
      <td>2.75 × 10⁻⁴</td>
      <td>0.269</td>
    </tr>
  </tbody>
</table>

<table><caption>Table 4. Saturation concentration of carbon in the working temperature range at [G] = 0, atomic fractions</caption>
  <thead>
    <tr>
      <th>Method of estimation</th>
      <th>800°C</th>
      <th>900°C</th>
      <th>1000°C</th>
      <th>1100°C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Precise thermodynamic calculation</td>
      <td>2.33 × 10⁻³</td>
      <td>3.18 × 10⁻³</td>
      <td>4.08 × 10⁻³</td>
      <td>5.04 × 10⁻³</td>
    </tr>
    <tr>
      <td>By Eq. (4)</td>
      <td>2.44 × 10⁻³</td>
      <td>3.88 × 10⁻³</td>
      <td>5.67 × 10⁻³</td>
      <td>7.96 × 10⁻³</td>
    </tr>
  </tbody>
</table>

boundaries of grains in the neighborhood of carbides Cr₂₃C₆ and NbC and identified as Nb₆(Ni,Fe)₁₆(Si,Cr)₇ [18]. Since there is no published information about the thermodynamic properties of complex silicides and the mechanism of their formation, we have to consider the limit situations with a negligible or maximum possible amount of the G phase of certain Nb₆Ni₁₆Si₇ composition, when it concentrates all the niobium of the alloy, and the atomic fraction [G] = [Nb]₀/6 = 2 × 10⁻³. The calculated distribution of elements between the carbides and the solid solution for such limit cases is given in Table 3.

Our attention is also engaged by a considerable decrease in the saturation concentration (the equilibrium concentration in a solid carbon solution [C]ₑq) in comparison with the initial content [C]₀. Then, if [C]ₑq ≪ [C]₀, it is possible to find the phase composition analytically and describe the key parameter [C]ₑq as

$$
[\mathrm{C}]_{\mathrm{eq}} \approx \frac{1}{K_{1} \gamma_{\mathrm{C}} \gamma_{\mathrm{Cr}}^{\frac{23}{6}}\left\{[\mathrm{Cr}]_{0}-\frac{23}{6}\left([\mathrm{C}]_{0}-[\mathrm{NbC}]_{\mathrm{eq}}\right)\right\}^{\frac{23}{6}}}. \quad (4)
$$

The obtained approximation reveals that the saturation concentration of carbon is affected by three factors: the G phase ([NbC]ₑq = 0 at a maximum G-phase concentration and [NbC]ₑq = 0.012 in the absence of the G phase), the temperature (via the equilibrium constant $K_1$ and the activity coefficients $\gamma$), and the initial composition (via [C]₀ and [Cr]₀).

As the temperature increases, the saturation concentration of carbon increases, the gap between the initial and equilibrium concentrations is reduced, and the assumption becomes less valid. According to the data of Table 4, approximate [C]ₑq calculated by Eq. (4) at 1100°C appreciably exceeds the value obtained by precise thermodynamic calculation. However, the error is reduced in the further kinetic solution predominantly owing to the fact that the saturation concentration is considered in combination with the initial concentration ([C]₀ − [C]ₑq).

## KINETIC PREREQUISITES²
Despite a variety of reactions proceeding under pyrolysis furnace conditions, the rate of each reaction $\dot{F}$ is determined by the rate of forward and backward processes ($\dot{\vec{F}}$ and $\dot{\overleftarrow{F}}$, respectively). For the precipitation of carbides [9],

$$
\dot{F}=\dot{\vec{F}}-\dot{\overleftarrow{F}}=\vec{k}(\mathrm{Me})^{\overleftarrow{\vec{n}}}(\mathrm{C})^{\overleftarrow{\vec{m}}}-\dot{\overleftarrow{F}}. \quad (5)
$$

Here, $\dot{F}$ is the mass fraction of a new phase in the material (the dot above means the derivative with respect to time τ), (C) is the mass fraction of dissolved carbon², $\vec{k}=\vec{k}_{0} \exp \left(-\frac{E_{\mathrm{f}}}{R T}\right)$ is the forward reaction rate constant, and $E_\text{f}$ is the forward reaction activation energy.

The further formation of phase composition can more conveniently be traced by the mass fraction of carbon in the alloy in different states

$$
(\mathrm{C})=(\mathrm{C})_{0}-(\mathrm{C})_{\mathrm{cb}}=(\mathrm{C})_{0}-\mathrm{v} F ; \quad (6)
$$

$$
\frac{d(\mathrm{C})}{d \tau}=-\mathrm{v} \dot{F}, \quad (7)
$$

where the subscript “0” denotes the initial level, the subscript “cb” means the presence in the composition of carbide, and $\mathrm{v}=\frac{n A_{\mathrm{C}}}{n A_{\mathrm{C}}+m A_{\mathrm{Me}}}$ is the mass fraction of carbon in carbide and depends on the atomic mass of active elements $A_\text{C}$ (carbon) and $A_\text{Me}$ (metal).

² Hereinafter, the mass concentrations of elements are given in parentheses.

---
INORGANIC MATERIALS: APPLIED RESEARCH Vol. 5 No. 6 2014

Since the resulting rate $\dot{F}=0$ at equilibrium, the backward reaction rate can be expressed through the equilibrium parameters with the subscript "eq" as
$$
\dot{\overleftarrow{F}}=\vec{k}(\mathrm{Me})_{\mathrm{eq}}^{m / n}(\mathrm{C})_{\mathrm{eq}}.
$$

Consequently,
$$
\frac{d(\mathrm{C})}{d \tau}=-v \vec{k}\left\{(\mathrm{Me})^{m / n}(\mathrm{C})-(\mathrm{Me})_{\mathrm{eq}}^{m / n}(\mathrm{C})_{\mathrm{eq}}\right\}. \quad (8)
$$

In our conditions 45Cr26Ni33Si2Nb2 alloy; temperature, $800-1100^{\circ} \mathrm{C}$, carbon is bonded to two metals, namely, chromium and niobium, by reactions 1 and 5. A great difference between the initial concentrations (26.9 against 2 wt %), the reaction orders (23/6 against 1), and the equilibrium constants according to Table 3, three orders of magnitude hampers the direct comparison of the rates of these processes. However, it is possible to estimate the intensities of the reaction with respect to the forward and backward stage rates as
$$
i=\left\{\frac{(\mathrm{Me})}{(\mathrm{Me})_{\mathrm{eq}}}\right\}^{\frac{m}{n}} \frac{(\mathrm{C})}{(\mathrm{C})_{\mathrm{eq}}},
$$
i.e.,
$$
\begin{gathered}
i_{1}=\left\{\frac{(\mathrm{Cr})}{(\mathrm{Cr})_{1}}\right\}^{\frac{23}{6}} \frac{(\mathrm{C})}{(\mathrm{C})_{\mathrm{eq}}} ; \quad i_{5}=\frac{(\mathrm{Nb})}{(\mathrm{Nb})_{5}} \frac{(\mathrm{C})}{(\mathrm{C})_{\mathrm{eq}}} ; \\
\frac{i_{5}}{i_{1}}=\frac{(\mathrm{Nb})}{(\mathrm{Cr})^{\frac{23}{6}}} \frac{(\mathrm{Cr})_{1}^{\frac{23}{6}}}{(\mathrm{Nb})_{5}}
\end{gathered}
$$
for the formation of chromium and nickel carbides.

It remains for us to convert the mass fractions $(\mathrm{Cr})_{1}$ and $(\mathrm{Nb})_{5}$ into the atomic fractions $[\mathrm{Cr}]$ and $[\mathrm{Nb}]$, to use Eq. (3), and to substitute the equilibrium constants $K_{1}$ and $K_{5}$ from Table 2 to finally obtain
$$
\frac{i_{5}}{i_{1}}>11 \frac{(\mathrm{Nb})}{(\mathrm{Cr})^{\frac{23}{6}}}.
$$

At first, the current concentration of metals in a solution is still close to the initial concentration, so
$$
\frac{i_{50}}{i_{10}}>11 \frac{(\mathrm{Nb})_{0}}{(\mathrm{Cr})_{0}^{\frac{23}{6}}}=11 \frac{0.02}{(0.269)^{\frac{23}{6}}}=34.
$$

This means that niobium carbide is formed much faster than chromium carbide. The difference gradually decreases, but the apparent advantage is retained by niobium even at the approaches to equilibrium.

Under such circumstances, it is admissible to describe the decomposition of a solid solution by only Eq. (8) for reaction 1
$$
\frac{d(\mathrm{C})}{d \tau}=v \vec{k}\left\{(\mathrm{Cr})^{\frac{m}{n}}(\mathrm{C})-(\mathrm{Cr})_{\mathrm{eq}}^{\frac{m}{n}}(\mathrm{C})_{\mathrm{eq}}\right\}, \quad (9)
$$
with the constants $m=23, n=6$, and $v=0.057$ and to determine the content of the phase which has precipitated by the moment $\tau$ as
$$
F=-\vec{k} \int_{0}^{\tau}\left\{(\mathrm{Cr})^{\frac{m}{n}}(\mathrm{C})-(\mathrm{Cr})_{\mathrm{eq}}^{\frac{m}{n}}\left(\mathrm{C}_{\mathrm{eq}}\right)\right\} d \tau. \quad (10)
$$

The concentrations of elements are additionally related to each other via the equilibrium constants and the material balance conditions as in Eqs. (3) and (4). Such a set can be solved analytically only at $m / n=1$, so it is necessary to turn to numerical methods.

However, the concentration of chromium in a solution (Cr) for high-chromium alloys can be considered to be constant and even equal to the initial concentration $(\mathrm{Cr})_{0}$ throughout the entire path up to an equilibrium value. Then integration gives
$$
F=\frac{1}{v}\left\{(\mathrm{C})_{0}-(\mathrm{C})_{\mathrm{eq}}\right\}\{1-\exp (-\tilde{k} \tau)\}, \quad (11)
$$
where $\tilde{k}$ is the reduced rate constant, $\tilde{k}=v(\mathrm{Cr})_{0}^{\frac{m}{n}} \vec{k}$.

Equation (11) reveals an ambiguous effect of the temperature $T$ on the phase composition of the alloy. Both the saturation concentration $(\mathrm{C})_{\text {eq }}$ and the reduced rate constant $\tilde{k}$ are temperature-dependent: the former, according to Eq. (4), through the equilibrium constant $K_{1}$ and the activity coefficients of elements $\gamma$ and the latter, by definition, through the forward reaction rate constant $\vec{k}$. All these characteristics must satisfy "strong" exponential functions $\exp \left(-\frac{E}{R T}\right)$, [19], which quickly grow with increasing temperature, but have an opposite effect on the calculated concentration of precipitations. To describe the consequences, it is first necessary to solve the inverse problem: to determine the carburization rate constants $\tilde{k}(\vec{k})$ from the calculated saturation concentration of carbon $(\mathrm{C})_{\text {eq }}$ and experimental current phase composition data by Eq. (10) or (11).

## EXPERIMENTAL RESULTS AND ASSUMPTIONS

To verify the proposed model and assumptions for adequacy, we used the experimental data [20] obtained for the phase composition and volumetric fraction of disperse precipitations by electron backscattered diffraction (EBSD). These data for different structural states of the 45Cr26Ni33Si2Nb2 alloy experiment nos. 0-6 are listed in Table 5.

<table><thead><tr><td rowspan="2"><b>Experiment no.</b></td><td rowspan="2"><b>State</b></td><td colspan="4"><b>Concentration of precipitations, vol %</b></td></tr><tr><td><b>$Nb_{6}Ni_{16}Si_{7}$</b></td><td><b>NbC</b></td><td><b>$Cr_{23}C_{6}$</b></td><td><b>$Cr_{7}C_{3}$</b></td></tr></thead><tbody><tr><td><b>$0^{*}$</b></td><td><b>Initial</b></td><td><b>0</b></td><td><b>2.3</b></td><td><b>0</b></td><td><b>1.8</b></td></tr><tr><td><b>1</b></td><td><b>After aging $800^{\circ }C,10^{3}h$</b></td><td><b>2.9</b></td><td><b>1.5</b></td><td><b>2.6</b></td><td><b>1.4</b></td></tr><tr><td><b>2</b></td><td><b>$900^{\circ }C,10^{3}h$</b></td><td><b>3.0</b></td><td><b>0.3</b></td><td><b>4.6</b></td><td><b>0.2</b></td></tr><tr><td><b>3</b></td><td><b>$1000^{\circ }C,10^{3}h$</b></td><td><b>2.7</b></td><td><b>0.8</b></td><td><b>5.9</b></td><td><b>0.3</b></td></tr><tr><td><b>4</b></td><td><b>$1100^{\circ }C,10^{3}h$</b></td><td><b>0.1</b></td><td><b>1.7</b></td><td><b>5.9</b></td><td><b>0.2</b></td></tr><tr><td><b>5</b></td><td><b>After experiments $900^{\circ }C,10^{3}h+900^{\circ }C,4.3×10^{-3}h,40MPa$</b></td><td><b>4.7</b></td><td><b>0</b></td><td><b>6.9</b></td><td><b>0</b></td></tr><tr><td><b>6</b></td><td><b>$1000^{\circ }C,10^{3}h+1000^{\circ }C,2.2×10^{-3}h,40MPa$</b></td><td><b>0.3</b></td><td><b>2.1</b></td><td><b>7.1</b></td><td><b>0</b></td></tr></tbody></table>

The volumetric fraction of phases was calculated from one or another phase area fraction in the phase map plotted by EBSD data for a selected region under the assumption of the absence of an appreciable shape anisotropy and orientation of disperse phases. The experience of structural studies, both electron-micro- scopic and metallographic, shows that two opposite trends affect the precision of the quantitatively esti- mated fraction of the area occupied by highly dis- persed phases in coarsely grained structures like cast austenite. The necessity of a detailed analysis of parti- cle shapes for precise area estimates requires high-res- olution studies; on the other hand, a fairly representa- tive region adequately reflecting the ratio of compo- nents must contain 50-100 structural elements(grains). At an average element size of $70-100 \mu m$  typical of cast austenite, the size of such a region is $500 ×500 \mu m$ . The field of such a size is difficult to study at a high resolution. The certified technique for the measurement of the volumetric fraction of disperse precipitations in fireproof steels and alloys by scanning electron microscopy [21] estimates the measurement error at a level of $10 \%$ .

Moreover, the experimental volumetric fractions required for the verification of the proposed model for adequacy cannot precisely be converted into the mass fractions required for kinetic calculations. Passing from one to the other, we adhere to the idealized notions: particles of the same size and shape are uni- formly distributed over the region of observation, and the mass concentrations are approximately, but sim- ply, related to the volumetric concentrations (unlike the atomic and mass concentrations, the volumetricconcentrations are isolated with angular brackets <>):
$$(\mathrm{C}) \approx\langle\mathrm{C}\rangle \frac{\rho_{\mathrm{cb}}}{\rho},\qquad(12)$$
 where $\rho_{cb}$ is the density of carbides, which is taken from the commonly known values for carbides and cal- culated for the G phase from the crystal lattice charac- teristics (face-centered cubic lattice; a = 1.18 nm) as equal to $6.57 ×10^{3} kg / m^{3}$ , and $\rho$ is the alloy density(approximately $8 ×10^{3} kg / m^{3}$ ).

According to X-ray diffraction data, the austenite matrix has a lattice of the same type with a = 0.365 nm(i.e., the alloy represents doped austenite), and the activity coefficients of components can be calculated by the dependences established for austenite steels with correction for the parity content of iron and nickel in the material.

The iron-nickel base of the 45Cr26Ni33Si2Nb2 alloy has an effect on the role of the third essential component, i.e., chromium, and is exhibited in its rel- ative activity coefficient with respect to carbon $f_{C}^{Cr}$ . Inour experiments, $f_{C}^{Cr}=\exp \{(10-21900 K / T)[Cr]\}$  corresponds to the middle level between the values obtained by extrapolating the dependences for the Fe-Cr-C and Ni-Cr-C systems.

Naturally, the induced errors associated with both measurements and assumptions have an effect on the precision of calculations; i.e., they are exhibited as a widening of the confidence interval.

## ANALYSIS OF EXPERIMENTAL DATA
The mechanism of phase conversions under the indicated conditions of tests is detailed in [20]. The phase composition given in Table 5 was expressed in the mass fraction taken for further kinetic calcula- tions. In Table 6, this composition is compared with the results of thermodynamic calculations for two pos- sible situations: with a maximum equilibrium content of the G phase $Nb_{6} Ni_{16} Si_{7}(0.061$ mass fractions) at800-900°C and its complete absence at 1000-1100°C. The main objective is to ascertain whether the alloy tends to the composition with predominance of the G phase $Nb_{6} Ni_{16} Si_{7}$ or niobium carbide NbC and what the role of temperature is in this case.

The initial composition is formed during the cool- ing of a billet, when the temperature quickly changes

<table>
<caption>Table 6. Composition of precipitations depending on the alloy state</caption>
<thead>
<tr>
<th rowspan="2">Alloy state,<br>experiment no.</th>
<th rowspan="2">$T$, °C</th>
<th rowspan="2">Aging time, h</th>
<th colspan="4">Concentration of precipitations, wt %</th>
</tr>
<tr>
<th>$\text{Nb}_6\text{Ni}_{16}\text{Si}_7$</th>
<th>NbC</th>
<th>$\text{Cr}_{23}\text{C}_6$</th>
<th>$\text{Cr}_7\text{C}_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Initial</td>
<td>20</td>
<td>—</td>
<td>0</td>
<td>0.021</td>
<td>0</td>
<td>0.015</td>
</tr>
<tr>
<td rowspan="2">Equilibrium</td>
<td rowspan="2">800</td>
<td>1000</td>
<td>0.023</td>
<td>0.014</td>
<td>0.022</td>
<td>0.012</td>
</tr>
<tr>
<td>$\gg$1000</td>
<td>≈0.061</td>
<td>≈0</td>
<td>0.064–0.025</td>
<td>0</td>
</tr>
<tr>
<td>2</td>
<td rowspan="4">900</td>
<td>1000</td>
<td>0.024</td>
<td>0.030</td>
<td>0.039</td>
<td>0.062</td>
</tr>
<tr>
<td>5</td>
<td>5300</td>
<td>0.038</td>
<td>0</td>
<td>0.059</td>
<td>0</td>
</tr>
<tr>
<td>6</td>
<td>5300</td>
<td>0.034</td>
<td>0</td>
<td>0.051</td>
<td>0</td>
</tr>
<tr>
<td>Equilibrium</td>
<td>$\gg$5300</td>
<td>≈0.061</td>
<td>≈0</td>
<td>0.059–0.022</td>
<td>0</td>
</tr>
<tr>
<td>3</td>
<td rowspan="2">1000</td>
<td>1000</td>
<td>0.021</td>
<td>0.007</td>
<td>0.050</td>
<td>0.003</td>
</tr>
<tr>
<td>Equilibrium</td>
<td>$\gg$3200</td>
<td>≈ 0</td>
<td>≈0.023</td>
<td>0.054–0.019</td>
<td>0</td>
</tr>
<tr>
<td>4</td>
<td rowspan="2">1100</td>
<td>1000</td>
<td>0.01</td>
<td>0.015</td>
<td>0.050</td>
<td>0.02</td>
</tr>
<tr>
<td>Equilibrium</td>
<td>$\gg$1000</td>
<td>≈0</td>
<td>≈0.023</td>
<td>0.049–0.016</td>
<td>0</td>
</tr>
</tbody>
</table>

along the wall thickness. The hypothesized aggressiv-ity of niobium looks all the more convincing: during this period, it completely comes from the solution and captures as much carbon as required for the formation of the most stable carbide. When there is no free nio-bium, carbide $\text{Cr}_7\text{C}_3$ precipitates instead of $\text{Cr}_{23}\text{C}_6$, and the G phase is absent.

The first high-temperature aging (1) reveals the general trend in the formation of a prestable structure. It is likely that the formation of $\text{Nb}_6\text{Ni}_{16}\text{Si}_7$ begins, and its attendant processes, such as the decomposition of NbC, the transitions of niobium into a new phase, and of carbon into carbide $\text{Cr}_{23}\text{C}_6$, are started.

Experimental regimes 2, 5, and 6 with a higher temperature and more prolonged aging draw the alloy nearer to equilibrium, and the revealed trend is real-ized as nearly limit concentrations of the G phase, the elimination of NbC, and an adequate increment in the content of $\text{Cr}_{23}\text{C}_6$. At a level of $1000^\circ\text{C}$ (regime 3), attention is drawn to the radical turn of the vector of development; there is the trend toward the other equi-librium state without the G phase with the saturation concentration of carbide NbC. At $1100^\circ\text{C}$, a composi-tion close to such a limit is attained even under short-term aging for 1000 h (regime 4).

The described sequence of events agrees with the preliminary thermodynamic finding and the conclu-sions [20] and confirms the conclusion about the cru-cial role of niobium and the form of its existence in the alloy: this is predominantly the G phase $\text{Nb}_6\text{Ni}_{16}\text{Si}_7$ at a temperature of $900^\circ\text{C}$ and lower and carbide NbC at $1000^\circ\text{C}$ and higher.

# VERIFICATION OF KINETIC PREREQUISITES

The processing of an array of experimental points is preceded by the verification of the computational model. First, using the chromium carbide $\text{Cr}_{23}\text{C}_6$ concentrations $F$ obtained on a limited base of experi-ments 1–3 (1000 h of aging at 800, 900, and $1000^\circ\text{C}$) and Eq. (10) or (11), we find the reaction rate constants
$$
\vec{k} = \vec{k}_0\exp\left(-\frac{E_{\text{f}}}{RT}\right);
$$
$$
\tilde{k} = v(\text{Cr})_0^{\frac{23}{6}}\vec{k} = 0.057 \times (0.269)^{\frac{23}{6}}\vec{k} = 3.72 \times 10^{-4}\vec{k}.
$$

Then we separate the components, such as the frequency multiplier $\vec{k}_0$ and the activation energy $E_{\text{f}}$. At the following stage, we solve the inverse problems; i.e., we calculate the concentrations $F$ under new condi-tions of experiments with other combinations of tem-perature and time values ($900^\circ\text{C}$, 5300 h; $1000^\circ\text{C}$, 3200 h; $1100^\circ\text{C}$, 1000 h). In this case, the revealed transition of niobium from the G phase into NbC has an indirect effect on the results, i.e., via the saturation concentration of carbon $(\text{C})_{\text{eq}}$ in Eqs. (10) and (11), and, for this reason, does not produce any appreciable effect on the values of $\tilde{k}(\vec{k})$.

The experimental points (Tables 5 and 6) are plot-ted in Fig. 1 in combination with the curves of numer-ical integration (10). Experiments 1, 2, and 3 taken as a basis (dark points) enable the estimation of the stabi-lization constants $E_n$ for the further calculation of the current state of carbides; regimes 4 and 5 (light points) are used to check the calculations at a different tem-perature (4) and aging time (5); repeated experiments 6,


7, etc. (squares) are performed to enlarge the statistical base.

The calculated curves pass within the range of measured concentrations $F$, but the experimental points of repeated measurements on the same specimen differ from each other by 10–15%. The main reason for such deviations is the nonuniform distribution of carbon over the cast metal. It turns out that the difference between the physical and calculated concentrations for the cast alloy cannot be avoided, but it is necessary to turn to the methods of statistics for confident conclusions.

## GENERALIZATION AND RELIABILITY OF OBTAINED CHARACTERISTICS

The standard processing of experimental data is confined to the calculation of average values in the confidence range determined at a specified probability (usually of 0.95). Here, it is assumed that random deviations are not limited in their value, are symmetric with respect to the average, and satisfy the normal distribution law. In this case, however, the phase concentration $F$ is limited by the initial content of elements, on one hand, and the thermodynamic equilibrium condition, on the other hand, and the distribution differs from normal, so the standard approach is not applicable here.

At the same time, as can be seen from Eq. (10) or (11) and the content of the rate constants $(\vec{k}$ or $\tilde{k})$, the function $F(T, \tau)$ is directly related to the temperature and the time via the constants $E_{n}$ and $k_{0}$ and, in the long run, can be written as $\exp(y + z/T)$. The parameters $y$ and $z$ appear in the form of a linear combination, have no limitations, and are perceived as normally distributed random values, and their confidence range may be situated symmetrically around the line of the mathematical expectation estimate (average value).

Since two independently determined characteristics are considered, multiple (in this case, two-dimensional) regression analysis [22] should be applied. From the normal law of distribution for each constant, we numerically determine the confidence ranges and true (within the framework of the accepted hypotheses) $y$ and $z$ for these constants in a standard way to arrive at the average parameters

$$
k_{0}=6.74 \times 10^{4} \mathrm{~h}^{-1} ; \quad E_{n}=9.28 \times 10^{4} \mathrm{~J} / \mathrm{mol} \quad(13)
$$

and the related functions

$$
\vec{k}=6.74 \times 10^{4} \exp\left(\frac{-9.28 \times 10^{4}}{R T}\right) \mathrm{h}^{-1} ;
$$

$$
\tilde{k}=3.72 \times 10^{-4} \vec{k} \approx 25 \exp\left(-\frac{11200 \mathrm{~K}}{T}\right) \mathrm{h}^{-1},
$$

and further arrive at integral (10) or Eq. (11) for the average carbide concentration $F$ via these functions and at the boundaries of the confident range of $F$ via the extremal values.

![](./images/814670767399632897_1.jpg)

Fig. 1. Concentration of chromium carbide $\mathrm{Cr}_{23} \mathrm{C}_{6}$ versus temperature and aging time $\tau$.

![](./images/814670767399632897_2.jpg)

Fig. 2. Concentration of $\mathrm{Cr}_{23} \mathrm{C}_{6}$ versus aging time at $900^{\circ} \mathrm{C}$ in the confidence range at $k_{0}=6.74 \times 10^{4} \mathrm{~h}^{-1}$ and $E_{n}=$ $9.28 \times 10^{4} \mathrm{~J} / \mathrm{mol}$: (—) numerical integration by Eq. (10), (-----) approximate dependence (11), (—·—·—) range boundaries with a probability of 0.95.

The results for the most studied temperature of $900^{\circ} \mathrm{C}$ are plotted in Fig. 2. The curve $F(\tau)$ inside its confidence range approaches the upper boundary with time for average (from the viewpoint of mathematical expectation) $F$. The experimental points lie almost on the boundary of the confidence range or deep inside it, and such a location indicates a quite acceptable precision of the obtained statistical estimates.

The curves calculated from statistically substantiated $k_{0}$ and $E_{n}$ (13) are similar to the values which were preliminarily obtained on the basis of the first experiments 1–3 (Fig. 1), but are distinguished by a more abrupt initial region; i.e., the phase composition changes more quickly than previously suspected. For approximate analytical dependence (11), the concentration $F$ is always higher than in the case of numerical integration. Such a proportion is explained by the assumption that the content of chromium in a solid solution changes slightly, and $(\mathrm{Cr})=(\mathrm{Cr})_{0}$. For this reason, the originally inappreciable error grows with time, but gradually decreases to zero in the region of equilibrium, when $(-\tilde{k} \tau) \ll 1$.

As the rate of phase conversions increases, the period of stabilization is reduced. Strictly speaking,

![](./images/814670767399632897_3.jpg)

Fig. 3. Stabilization time versus temperature for (a) (—) the numerical solution by integral (10) at constants (13) and (----) the approximate solution by Eq. (11) and (b) the calculation by the similarity criterion at (----) $E_{\max}=10^{5}$ J/mol and (---) $E_{\min}=8.5\times10^{4}$ J/mol.

the time required for the transition of the alloy into a stable (time-invariant) state is infinite. For this reason, the process can be considered as almost completed when the degree of stabilization, i.e., the ratio of the current concentration of a phase to its equilibrium level $\Theta=C/C_{\text{eq}}$, approaches unity and attains the specified value $\Theta^{*}=0.99$. The stabilization time $\tau^{*}$ calculated by this criterion (Fig. 3a) is from $10^{3}$ (1100°C) to $1.6\times10^{4}$ h (800°C). The analytical curve accumulates the errors of assumptions, passes much lower than the calculated curve, and corresponds to the value of $\tau^{*}$, which is nearly one and a half times lower.

However, it is clear that the true destination of the approximate dependences is not to compete with numerical methods, but to reveal the role of individual factors in the general state of the material and to help in understanding the formal numerical conclusions. This important function is clearly manifested during the consideration of the main dependence $F(T,\ \tau)$ plotted in Figs. 1 and 4 in two variants, in which one of the two variables—the temperature or the aging time—is constant.

Comparing the comultipliers in approximate expression (11), we can see that they contain the characteristics of different (thermodynamic and kinetic) origination and react to the change in temperature in opposite fashions. For this reason, the temperature range with a maximum content of carbides is formed on the $F-T$ curves (Fig. 4).

A nonmonotonic character of the temperature dependence affects the mechanical properties of the alloy. For the relative elongation at rupture $\delta_{20}$, which is the parameter most sensitive to material aging, the $\delta_{20}-T$ temperature dependence in the case of isothermal aging for $10^{3}$ h [3] represents almost the mirror reflection of the lower $F-T$ curve.

The longer the aging time $\tau$, the greater the role of the kinetics, and the carbide maximum shifts toward lower temperatures. Such a trend can easily be traced on the $F-\tau$ and $F-T$ plots (Figs. 1 and 4, respectively): in the case of aging for 1000 h, the content of carbides at 1100°C is much higher than at 800°C. However, the advantage goes to the temperature of 800°C after 9000–10 000 h despite a low process rate. The physical nature of these events is the approach of the alloy to an equilibrium state (the upper curve in Fig. 4): the lower the temperature, the smaller the solubility of carbon and the higher the content of carbides.

In all the calculations of this part, the constants were taken with respect to average level (13), but they can differ from each other with a probability of 0.95: slightly with respect to the activation energy and by almost an order of magnitude with respect to the frequency multiplier of a reaction, i.e.,

$$
2.4\times10^{4}<k_{0}<1.9\times10^{5}\ \text{h}^{-1};
$$

$$
8.3\times10^{4}<E_{n}<10^{5}\text{J/mol}.
$$

![](./images/814670767399632897_4.jpg)

Fig. 4. Concentration of carbide $\text{Cr}_{23}\text{C}_{6}$ versus temperature at different aging times; the numbers at the curves stand for the aging times.

What then is observed in the limit cases? The curves $F(\tau)$ for the concentration of precipitations with the confidence range boundaries as in Fig. 2 do not pro-

vide a clear understanding of possible deviations from calculations by average $k_0$ and $E_n$. Therefore, it makes sense to show the deviation from average on an individual plot. Moreover, it is reasonable to reject the absolute concentrations and to prefer the degree of stabilization $\Theta$ to arrive at the conclusions general for different temperatures, as the curves written in the form of $\Delta\Theta/\Theta$ hardly depend on the temperature (Fig. 5).

Probable deviations form a closed asymmetrically situated region. Large deviations make "for plus" and small deviations make "for minus" at the beginning of phase conversions, the inverse ratio takes place at the end, the difference between extremes is nearly constant at the main stage, and the maximum deviation with a probability $P=0.95$ amounts to almost $0.6\Theta$. In other words, the actual concentration of chromium carbide may prove to be $60\%$ higher or lower than its calculated value. This results from the unavoidable spread of experimental data in the EBSD analysis of the cast material with a nonuniform distribution of carbon.

The existing situation does not yet revoke the principal conclusion about the existence of a relation of carburization rate (10) to the temperature and the initial, current, and equilibrium concentration of carbon. It is sufficient to use the similarity techniques in which a specified state is not experimentally reproduced by the absolute values of temperature, time, wall thickness, and medium parameters, but modeled by the combinations of these characteristics in the form of physicochemical similarity criteria which eliminate "laborious" parameters at the expense of the other parameters [10, 11].

For the particular case of thermal aging, such an equivalent approach is confined to the condition of retaining the product $\vec{k}\tau$ unchangeable. Then, the stabilization time at a specified temperature $T$ is
$$
\tau^{*}=\tau_{\mathrm{e}} \exp \frac{k_{\mathrm{e}}}{k_{*}}=\tau_{\mathrm{e}} \exp \left[-\frac{E_{n}}{R}\left(\frac{1}{T_{\mathrm{e}}}-\frac{1}{T}\right)\right],\qquad(14)
$$
where the subscript "e" stands for an experimental value taken as a base.

In our conditions, stabilization can be considered complete after $1000\ \text{h}$ in the temperature range of $1000-1100^\circ\text{C}$, when the concentration of $\text{Cr}_{23}\text{C}_6$ does not change (regimes 3 and 4, Tables 5 and 6). The curves (7) calculated by Eq. (14) on the basis of $T_{\mathrm{e}}=1000^\circ\text{C}$ from the maximum and minimum activation energies are shown in Fig. 3b. Similar results for $1100^\circ\text{C}$ are slightly lower. On the whole, the stabilization time is from 1000 to $1200\ \text{h}$ at $1100^\circ\text{C}$ and from 7600 to $13000\ \text{h}$ at $800^\circ\text{C}$ with a probability of 0.95. Hence, the demonstrated combination of the methods of similarity theory and statistics seems to be quite promising.

This result once again confirms the fact known in statistics: the addition of a new fundamental relationship for experimental data to the already available relationships (e.g., the mass or energy conservations laws) increases the precision of obtained estimates owing to narrowing of the admissible spread area. The criterial relationships are classified as fundamental, since new still unknown relations may exist between the dimensionless parameters.

![](./images/814670767399632897_5.jpg)

Fig. 5. Utmost deviations from the calculated (most probable) degree of stabilization $\Delta\Theta$ in the current value function $\Theta\ (P=0.95)$ for (---) 800 and (----) $1100^\circ\text{C}$.

## CONCLUSIONS

(1) Equations (10) and (11) were proposed for the description of phase conversions in the process of stabilization (approach to equilibrium). From these equations and the thermodynamic relationships, it follows that niobium reacts with carbon an order of magnitude faster than chromium, and the stabilization rate is controlled by the formation of carbide $\text{Cr}_{23}\text{C}_6$.

(2) Kinetic stabilization constants (13) and the possible deviations (with a probability of 0.95) were calculated from the data of the EBSD analysis of specimens after experiments at $800-1100^\circ\text{C}$ for 1000– $5000\ \text{h}$. The saturation concentrations calculated for chromium carbides on this basis can differ from average values by almost $60\%$.

(3) Such an error is mainly produced by a selective character of EBSD measurements and a nonuniform distribution of carbon over the cast material. It is reasonable to combine the methods of statistics and similarity theory in the process of study. Thus, the predicted stabilization time is from 1000 to $1200\ \text{h}$ at $1100^\circ\text{C}$ and from 7600 to $13000\ \text{h}$ at $800^\circ\text{C}$.

(4) The approximate formulas for the saturation concentration of carbon (Eq. (4)) and the current concentration of carbides (Eq. (11)) can be used for the operation with physicochemical similarity criteria. The analytical dependences are in satisfactory agreement with numerical modeling and, at the same time, reveal the role of temperature and doping either in a direct fashion (via the equilibrium constant $K_1$ and the specified concentrations of carbon, chromium, and niobium) or through the activity coefficients of elements $\gamma$ and their components.

## ACKNOWLEDGMENTS

The studies were performed on the equipment of the Center of Shared Access Composition, Structure, and Properties of Structural and Functional Materials of the Central Research Institute of Structural Materials PROMETEY and financially supported by the Ministry of Education and Science of the Russian Federation.

## REFERENCES

1. Ignatov, V.A., Belov, V.P., Rybin, V.B., Mikerin, B.I., Vinokurov, V.F., Utkin, Yu.A., Odintsov, N.B., Rago-syan, I.V., and Starikov, V.G., RF Patent 2026401, 2008.

2. Oryshchenko, A.S., Utkin, Yu.A., and Odintsov, N.B., RF Patent 2350674, 2009.

3. Oryshchenko, A.S. and Utkin, Yu.A., Influence of change of microstructure at temperatures $800-1100^\circ\text{C}$ on characteristics of high-temperature strength of alloy 45X26H33C2Б2, *Vopr. Materialoved.*, 2009, no. 3, pp. 17–25.

4. D’yakov, V.G., Levtonova, N.M., and Medvedev, Yu.S., *Ekspluatatsiya materialov v uglevodorodnykh sredakh pechei piroliza (tematicheskii obzor)* (Exploitation of Materials in Carbon-Hydrogen Media of Phyrolisis Furnaces (Thematical Review)), Moscow: TsNIIT-Eneftekhim, 1983.

5. Oryshchenko, A.S., Development of high-temperature alloys for elements of construction of the radiant part of the coils of the high-temperature installations for oil synthesis, *Vopr. Materialoved.*, 2006, No. 1, pp. 147–159.

6. Polonskii, Ya.A. and Vatnik, L.E., Study of safety exploita-tion factors of reaction furnace tubes from NK-4 type steel, in *Nauchn.-Inform. Sbornik TsNIITEneftekhim* (Collection of Sci.-Inform. Papers of "TsNIITEneftekhim,") Moscow: TsNIITEneftekhim, 1995, pp. 31–34.

7. Chirkova, A.G., Hierarchiac system of estimation of safety exploitation of equipment for oil remaking, *Doctoral (Eng.) Dissertation*, Ufa, 2005.

8. Lukin, O.A., Kinetics of diffusion phase transforma-tions in non-stationary conditions, *Candidate Sci. (Eng.) Dissertation*, Voronezh, 2000.

9. Dushin, Yu.A., Longterm carburization of chromium-nickel steels and alloys, *Fiziko-Khim. Mekh. Mater.*, 1991, No. 3, pp. 34–39.

10. Dushin, Yu.A., Similar parameters of diffusion alloying of metallic articles, *Izv. Akad. Nauk SSSR. Metally*, 1979, No. 6, pp. 162–167.

11. Dushin, Yu.A., Influence of mass and heat transfer on the corrosion embrittlement of metals in a gaseous medium, *Sov. Mater. Sci.*, 1981, vol. 17, pp. 491–494.

12. Volodin, S.I., Dushin, Yu.A., Kunilovskii, V.V., and Novikova, I.E., Cracking and mechanical-property forecasting for carburized materials in high-tempera-ture equipment, *Mater. Sci.*, 1992, vol. 28, pp. 371–374.

13. Dushin, Yu.A., Ivanov, A.V., Kunilovsky, V.V., and Medvedev, N.A., Structure-stable weldable HN55MVC (ChS57) alloy for large-scale equipment operating at temperatures of up to $950^\circ\text{C}$ during a service life of up to 50000 h., *Materials Science and Engineering, A: Struct. Mat.: Prop., Microstruct., Proc.*, 1993, vol. 168, pp. 29–33.

14. Barin, I., *Thermochemical Data of Pure Substances*, Weinheim: VCH Verlagsgesellshaft, 1995.

15. Surovtsev, A.P., Tomilin, I.A., and Golovanenko, S.A., On thermodynamical activity of carbon in high-alloyed austenite, *Izv. Akad. Nauk SSSR: Metally*, 1975, No. 6, pp. 53–58.

16. Dushin, Yu.A., Peretyagin, Yu.V., Komissarchik, G.A., and Nemets, A.M., Thermodynamical characteristics of austenite steels and nickel alloys, *Izv. Akad. Nauk SSSR. Metally*, 1981, No. 3, pp. 141–145.

17. Lo, K.H., Shek, C.H., and Lai, L.J.R., Recent devel-opments in stainless steels, *Mater. Sci. Eng.*, 2009, vol. 65, pp. 39–104.

18. Chen, Q.Z., Thomas, C.W., and Knowles, D.M., Characterization of 20Cr32Ni1Nb alloys in as-cast and ex-service conditions by SEM, TEM and SDX, *Mater. Sci. Eng., A: Struct. Mat.: Prop., Microstruct., Proc.*, 2004, vol. 374, pp. 398–408.

19. Shtiller, V., *Arrenius Equation and Non-Equilibrium Kinetics*, Leipzig: Teubner, 1989; Moscow: Mir, 2000.

20. Oryshchenko, A.S., Utkin, Yu.A., Petrov, S.N., Neste-rova, E.N., and Mikhailov-Smol’nyakov, M.S., Investi-gation of transformation of structure, phase composi-tion and mechanical properties of 45Cr26Ni33Si2Nb2 alloy during high-temperature test for long-term strength of metal of a centrifugal casting pipe, *Inorg. Mater: Appl. Res.*, 2013, vol. 4, pp. 494–501.

21. *MVI "Metodika izmereniya ob"emnoi doli dispersnykh vydelenii v zharoprochnykh stalyakh i splavakh metodami rastrovoi elektronnoi mikroskopii"* (Methodology of Measurement Execution "Methodology of Measurement of Bulk Part of Dispersed Segregations in Refractory Steels and Alloys by Methods of Raster Electron Microscopy), FR No. 1.27.2011.10215 according to Federal Raster of Methodology of Measurement Execution.

22. Draper, N. and Smith, G., *Applied Regresion Analysis*, New York: Wiley, 1998, 3rd ed.; Moscow: Dialektika, 2007.

Translated by E. Glushachenkova

---

INORGANIC MATERIALS: APPLIED RESEARCH Vol. 5 No. 6 2014