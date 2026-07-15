# Simulating the behavior of volatiles belonging to the C–O–H–S system in silicate melts under magmatic conditions with the software D-Compress

Alain Burgisser $^{a,b,*}$, Marina Alletti $^{c,d}$, Bruno Scaillet $^{c,d}$

$^{a}$ CNRS, ISTerre, F-73376 Le Bourget du Lac, France
$^{b}$ Université Savoie Mont Blanc, ISTerre, F-73376 Le Bourget du Lac, France
$^{c}$ CNRS, ISTO, F-45071 Orléans, France
$^{d}$ Université d'Orléans, ISTO, F-45071 Orléans, France

---

## ARTICLE INFO

**Article history:**
Received 14 March 2014
Received in revised form
17 February 2015
Accepted 3 March 2015
Available online 5 March 2015

**Keywords:**
Volatile
Solubility
Silicate melt
Magma
Volcanic gas
Magma degassing
Thermodynamics

---

## ABSTRACT

Modeling magmatic degassing, or how the volatile distribution between gas and melt changes at pressure varies, is a complex task that involves a large number of thermodynamical relationships and that requires dedicated software. This article presents the software D-Compress, which computes the gas and melt volatile composition of five element sets in magmatic systems (O–H, S–O–H, C–S–O–H, C–S–O–H–Fe, and C–O–H). It has been calibrated so as to simulate the volatiles coexisting with three common types of silicate melts (basalt, phonolite, and rhyolite). Operational temperatures depend on melt composition and range from 790 to 1400 °C. A specificity of D-Compress is the calculation of volatile composition as pressure varies along a (de)compression path between atmospheric and 3000 bars. This software was prepared so as to maximize versatility by proposing different sets of input parameters. In particular, whenever new solubility laws on specific melt compositions are available, the model parameters can be easily tuned to run the code on that composition. Parameter gaps were minimized by including sets of chemical species for which calibration data were available over a wide range of pressure, temperature, and melt composition. A brief description of the model rationale is followed by the presentation of the software capabilities. Examples of use are then presented with outputs comparisons between D-Compress and other currently available thermodynamical models. The compiled software and the source code are available as electronic supplementary materials.

© 2015 Published by Elsevier Ltd.

---

## 1. Introduction

Over the years, many attempts have been made to calculate how volatiles are distributed between a silicate melt and a coexisting gas phase at pressure and temperature ranges relevant to magmatic systems. These efforts include largely empirical models (e.g., Moore et al., 1998; Liu et al. 2005), semi-empirical models (e.g., Iacono-Marziano et al., 2012; Ariskin et al., 2013; Duan, 2014), and thermodynamical models using various formalisms (e.g., Dixon and Stolper 1995; Dixon et al., 1995; Papale, 1999; Moretti et al., 2003). These models have found a wide range of applications, which includes the interpretation of melt inclusion data (Papale, 2005; Moore, 2008), the interpretation of gas measurements on active volcanoes (Aiuppa et al., 2007; Oppenheimer et al., 2011), the feedback between chemistry and physics in conduit flow models (Papale and Polacci, 1999; Burgisser et al., 2008), and the assessment of the impact of volcanic gases on the atmosphere of terrestrial planets (Gaillard and Scaillet, 2009, 2014; Gaillard et al., 2011). However diverse, all these works originate from the fact that the chemistry of the fluid phase evolves as magma ascends towards the surface to feed volcanic eruptions. A complex array of factors including pressure, temperature, and magma/fluid separation control these chemical changes. Because pressure changes spans three orders of magnitude from depth to surface, the evolution of pressure profoundly affects the fluid/melt partition as magma ascends during a volcanic eruption.

Focusing on magma ascent during eruption, assuming that temperature is constant and that magma degassing during ascent is primarily driven by pressure changes removes some but not all the complexities involved. A good example of these complexities is

---

* Corresponding author at: CNRS, ISTerre, F-73376 Le Bourget du Lac, France.
Fax: +33 479 758 742.
E-mail address: alain.burgisser@univ-savoie.fr (A. Burgisser).

http://dx.doi.org/10.1016/j.cageo.2015.03.002
0098-3004/© 2015 Published by Elsevier Ltd.

![](./images/814650004370096129_1.jpg)
![](./images/814650004370096129_2.jpg)
![](./images/814650004370096129_3.jpg)

<table>
<caption>Table 1<br>Solubility constants. The $a_{\mathrm{i}}$ and $b_{\mathrm{i}}$ parameters were determined by fitting experimental solubility data of corresponding species to an empirical equation of the form $w_{\mathrm{i}}=a_{\mathrm{i}} f_{\mathrm{i}}^{\mathrm{b}_{\mathrm{i}}}$ (see Table 2 for experimental ranges). Species $\mathrm{CH}_{4}, \mathrm{CO}, \mathrm{O}_{2}$, and $\mathrm{S}_{2}$ are considered insoluble. Column 'n' indicates the number of experimental points used to calibrate the two solubility coefficients and $\mathrm{T}$ is temperature in $^{\circ} \mathrm{C}$.</caption>
<thead>
<tr>
<th>Species</th>
<th>$a_{\mathrm{i}}$</th>
<th>$b_{\mathrm{i}}$</th>
<th>n</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Rhyoliteª</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{O}$</td>
<td>$2.5973 × 10^{-8} × \mathrm{T}^{2}-4.8473 × 10^{-5} × \mathrm{T}+2.298 × 10^{-2}$</td>
<td>$-5.1482 × 10^{-6} × \mathrm{T}^{2}+9.4853 × 10^{-3} × \mathrm{T}-3.7085$</td>
<td>98</td>
</tr>
<tr>
<td>$\mathrm{H}_{2}$ b</td>
<td>$3.400 × 10^{-7}$</td>
<td>1.2800</td>
<td>12</td>
</tr>
<tr>
<td>$\mathrm{SO}_{2}$</td>
<td>$5.6322 × 10^{-8}$</td>
<td>1.2937</td>
<td>9</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{S}$</td>
<td>$2.3164 × 10^{-6}$</td>
<td>0.7338</td>
<td>33</td>
</tr>
<tr>
<td>$\mathrm{CO}_{2}$</td>
<td>$2.8895 × 10^{-9} × \mathrm{T}-1.9625 × 10^{-6}$</td>
<td>$-1.0764 × 10^{-3} × \mathrm{T}+1.9639$</td>
<td>17</td>
</tr>
<tr>
<td colspan="4">Basaltᶜ</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{O}$</td>
<td>$6.576 × 10^{-4}$</td>
<td>0.5698</td>
<td>26</td>
</tr>
<tr>
<td>$\mathrm{H}_{2}$ b</td>
<td>$3.400 × 10^{-7}$</td>
<td>1.2800</td>
<td>12</td>
</tr>
<tr>
<td>$\mathrm{SO}_{2}$</td>
<td>$2.376 × 10^{-3}$</td>
<td>0.1967</td>
<td>24ᵈ</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{S}$</td>
<td>$4.623 × 10^{-4}$</td>
<td>0.2627</td>
<td>10ᵈ</td>
</tr>
<tr>
<td>$\mathrm{CO}_{2}$</td>
<td>$1.729 × 10^{-6}$</td>
<td>0.8540</td>
<td>12</td>
</tr>
<tr>
<td colspan="4">Phonoliteᵉ</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{O}$</td>
<td>$-3.166 × 10^{-9} × \mathrm{T}^{2}+7.480 × 10^{-6} × \mathrm{T}-3.853 × 10^{-3}$</td>
<td>$2.555 × 10^{-6} × \mathrm{T}^{2}-5.827 × 10^{-3} × \mathrm{T}+3.918$</td>
<td>116</td>
</tr>
<tr>
<td>$\mathrm{H}_{2}$ b</td>
<td>$3.400 × 10^{-7}$</td>
<td>1.2800</td>
<td>12</td>
</tr>
<tr>
<td>$\mathrm{SO}_{2}$</td>
<td>$2.019 × 10^{-4}$</td>
<td>0.4366</td>
<td>15</td>
</tr>
<tr>
<td>$\mathrm{H}_{2} \mathrm{S}$</td>
<td>$4.172 × 10^{-5}$</td>
<td>0.5015</td>
<td>11</td>
</tr>
<tr>
<td>$\mathrm{CO}_{2}$</td>
<td>$4.339 × 10^{-7}$</td>
<td>0.8006</td>
<td>4</td>
</tr>
</tbody>
</table>

ª Data are from Clemente et al. (2004) for sulfur bearing species; Holtz et al. (1992, 1995), Blank et al. (1993), Mangan and Sisson (2000) for $\mathrm{H}_{2} \mathrm{O}$; Fogel and Rutherford (1990) and Blank et al. (1993) for $\mathrm{CO}_{2}$.

b Due to the lack of data of $\mathrm{H}_{2}$ solubility in melt compositions different than rhyolitic, we used the data from Gaillard et al. (2003) for all compositions.

ᶜ Data are from Beermann et al. (2011), Botcharnikov et al. (2011), Lesne et al. (In preparation) for sulfur species; Lesne et al. (2011a) for $\mathrm{H}_{2} \mathrm{O}$; Lesne et al. (2011b) for $\mathrm{CO}_{2}$.

ᵈ Detailed justification of data selection is in Appendix B.

ᵉ Data are from Moncrieff (1999) as reported in Burgisser et al. (2012) for sulfur species; Iacono-Marziano (2005) as reported in Burgisser et al. (2012) for $\mathrm{CO}_{2}$; Carroll and Blank (1997), Larsen and Gardner (2004), Iacono-Marziano et al. (2007), Schmidt and Behrens (2008), and Burgisser et al. (2012) for $\mathrm{H}_{2} \mathrm{O}$.

the modeling of degassing in the Erebus magmatic system in Antarctica (Oppenheimer et al., 2011). In this comprehensive attempt to bring melt inclusion data, petrologic observations, and gas chemistry measurements of the emission of an active lava lake, the equilibrium saturation model of Moretti et al. (2003) was combined with a regular mixture approach for $\mathrm{H}_{2} \mathrm{O}$ and $\mathrm{CO}_{2}$ (Papale et al., 2006), a polymeric treatment of silicate melts for S-related computations (Moretti and Ottonello, 2005; Moretti and Papale, 2004), a thermodynamical model for iron (Ottonello et al., 2001) and its interaction with S (Moretti and Baker, 2008), and non-ideal equations of state for gas species (Belonoshko and Saxena, 1992). Owing to such complexity, not all of these models have been released to the volcanological community in a user-friendly format. Notable exceptions are the models VolatilCalc (Newman and Lowenstern, 2002), PELE (Boudreau, 1999), and SolEx (Witham et al., 2012), and the models of Papale et al. (2006), Iacono-Marziano et al. (2012), Ariskin et al. (2013), and Duan (2014). Altogether, these models cover a wide range of situations of geological interest, but each of them handles a specific range of intensive parameters and volatile and melt compositions. Because magmatic systems involve varying magmatic compositions, temperatures and pressures of interest, studies have to rely on a combination of these models, which raises issues of inter-model consistency and gaps in parameter ranges.

Here we describe a software, D-Compress, that computes the fluid and melt volatile composition of five volatile-dominated systems (O–H, S–O–H, C–S–O–H, C–S–O–H–Fe, and C–O–H). This software is intended primarily to address the chemical evolution of the fluid phase emanating from magmas where $\mathrm{H}_{2} \mathrm{O}$ is present in significant abundance, and for moderately reduced conditions. We caution against its application on strongly reduced magmas (i.e., $f_{\mathrm{O} 2}<$ NNO-3, where NNO is the Ni–NiO solid buffer) because the solubility laws of some species, in particular sulfur, would depart from the formalism adopted here (Gaillard and Scaillet, 2009). The chemical systems considered are composed of at most nine volatile species ($\mathrm{H}_{2} \mathrm{O}, \mathrm{H}_{2}, \mathrm{O}_{2}, \mathrm{SO}_{2}, \mathrm{H}_{2} \mathrm{S}, \mathrm{S}_{2}, \mathrm{CO}_{2}, \mathrm{CO}$, and $\mathrm{CH}_{4}$), which constitute $>99$ mol% of the volatiles commonly measured in arc volcanoes (Delmelle and Stix, 2000). Originally built to deal with relatively volatile-rich rhyolitic melts (Burgisser and Scaillet, 2007; Burgisser et al., 2008), its application to phonolite has been presented in Burgisser et al. (2012). The version presented herein has been calibrated so as to simulate the volatiles coexisting with three common types of silicate melts (basalt, phonolite, and rhyolite). Operational temperatures depend on melt composition and range from 790 to $1400^{\circ} \mathrm{C}$. A specificity of D-Compress is the calculation of volatile composition as pressure varies along a (de)compression path between atmospheric pressure and 3000 bars. This feature is intended to simulate consequences of isothermal magma ascent. The software was prepared so as to maximize versatility by proposing different sets of input parameters. Parameter gaps were minimized by including sets of chemical species for which calibration data were available over a wide range of pressure, temperature, and melt composition. In the next sections, a brief description of the model rationale is followed by the presentation of the software capabilities. Examples of use are presented with output comparisons between D-Compress and other models. The compiled software and the source code are available as Supplementary material (Appendix A).

## 2. Summary of the chemical model

Processes controlling gas chemistry variations in response to pressure changes occur on widely different timescales (to keep nomenclature simple and consistent with volcanic gas literature, we refer to the fluid phase as gas regardless of whether it is sub- or supercritical). Because of the high temperatures involved, the fastest process is chemical reactions within the gas phase itself

<table><caption>Table 2 Parameter ranges of the experiments used to calibrate the chemical model.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>H₂S</th>
<th>SO₂</th>
<th>H₂O</th>
<th>CO₂</th>
<th>H₂</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Rhyoliteᵃ</td>
</tr>
<tr>
<td>ΔNNO</td>
<td>−2.3 − +1.1</td>
<td>+1.3 − +3.0</td>
<td>&gt; 0</td>
<td>~ +1</td>
<td>n.a.</td>
</tr>
<tr>
<td>P (bar)</td>
<td>1970–2500</td>
<td>1990–2070</td>
<td>250–2000</td>
<td>500–3530</td>
<td>220–265</td>
</tr>
<tr>
<td>fᵢ (bar)</td>
<td>422–2620</td>
<td>638–1770</td>
<td>50–1740</td>
<td>45–10000</td>
<td>0.02–70</td>
</tr>
<tr>
<td>T (°C)</td>
<td>785–1000</td>
<td>930–1000</td>
<td>800–1000</td>
<td>850–1050</td>
<td>700–1000</td>
</tr>
<tr>
<td>H₂Oᵐᵉˡᵗ (wt%) ᵇ</td>
<td>1.80–4.82</td>
<td>1.80–4.82</td>
<td>0.51–6.49</td>
<td>0.51–3.34</td>
<td>n.a.</td>
</tr>
<tr>
<td>FeO* (wt%) ᶜ</td>
<td>1.06–6.99</td>
<td>1.06–6.99</td>
<td>0–0.94</td>
<td>0.38–1</td>
<td>0.08–1.6</td>
</tr>
<tr>
<td>MgO (wt%) ᶜ</td>
<td>0.02–0.32</td>
<td>0.02–0.32</td>
<td>0–0.03</td>
<td>0.05–0.06</td>
<td>0.08</td>
</tr>
<tr>
<td>CaO (wt%) ᶜ</td>
<td>1.31–2.58</td>
<td>1.31–2.58</td>
<td>0–0.54</td>
<td>0.25–0.52</td>
<td>0.75</td>
</tr>
<tr>
<td>Na₂O (wt%) ᶜ</td>
<td>3.29–4.14</td>
<td>3.29–4.14</td>
<td>1.21–6.71</td>
<td>4.08–4.21</td>
<td>4.15</td>
</tr>
<tr>
<td>K₂O (wt%) ᶜ</td>
<td>1.84–2.85</td>
<td>1.84–2.85</td>
<td>0.89–9.24</td>
<td>4.19–4.78</td>
<td>5.64</td>
</tr>
<tr>
<td>SiO₂ (wt%) ᶜ</td>
<td>72.06–78.29</td>
<td>72.06–78.29</td>
<td>75.64–77.70</td>
<td>76.45–77.70</td>
<td>74.51</td>
</tr>
<tr>
<td colspan="6">Basaltᵃ</td>
</tr>
<tr>
<td>ΔNNO</td>
<td>−1 to −0.3</td>
<td>+2</td>
<td>+2</td>
<td>+3</td>
<td>n.a.</td>
</tr>
<tr>
<td>P (bar)</td>
<td>1000–20000</td>
<td>250–2000</td>
<td>163–3948</td>
<td>269–2059</td>
<td>220–265</td>
</tr>
<tr>
<td>fᵢ (bar)</td>
<td>28–1159</td>
<td>54–2975</td>
<td>120–5240</td>
<td>152–3111</td>
<td>0.02–70</td>
</tr>
<tr>
<td>T (°C)</td>
<td>1050–1250</td>
<td>1050–1200</td>
<td>1200</td>
<td>1200</td>
<td>700–1000</td>
</tr>
<tr>
<td>H₂Oᵐᵉˡᵗ (wt%) ᵇ</td>
<td>1.70–4.84</td>
<td>0.52–3.58</td>
<td>0.98–6.18</td>
<td>0.71–1.58</td>
<td>n.a.</td>
</tr>
<tr>
<td>FeO* (wt%) ᶜ</td>
<td>7.62–10.46</td>
<td>7.62–10.46</td>
<td>7.62–10.24</td>
<td>7.62–10.24</td>
<td>0.08–1.6</td>
</tr>
<tr>
<td>MgO (wt%) ᶜ</td>
<td>5.76–8.07</td>
<td>5.76–8.07</td>
<td>5.76–8.07</td>
<td>5.76–8.07</td>
<td>0.08</td>
</tr>
<tr>
<td>CaO (wt%) ᶜ</td>
<td>10.81–12.94</td>
<td>10.81–12.94</td>
<td>10.93–12.94</td>
<td>10.93–12.94</td>
<td>0.75</td>
</tr>
<tr>
<td>Na₂O (wt%) ᶜ</td>
<td>1.80–3.45</td>
<td>1.80–3.45</td>
<td>1.80–3.42</td>
<td>1.80–3.42</td>
<td>4.15</td>
</tr>
<tr>
<td>K₂O (wt%) ᶜ</td>
<td>1.90–5.55</td>
<td>1.90–5.55</td>
<td>1.90–5.55</td>
<td>1.90–5.55</td>
<td>5.64</td>
</tr>
<tr>
<td>SiO₂ (wt%) ᶜ</td>
<td>47.41–49.40</td>
<td>47.41–49.40</td>
<td>47.59–49.40</td>
<td>47.95–49.82</td>
<td>74.51</td>
</tr>
<tr>
<td colspan="6">Phonoliteᵃ</td>
</tr>
<tr>
<td>ΔNNO</td>
<td>−1.5 to −1</td>
<td>+2.2 − +8.0</td>
<td>−1.0 − +1.3</td>
<td>+1.3</td>
<td>n.a.</td>
</tr>
<tr>
<td>P (bar)</td>
<td>2020</td>
<td>1500–2010</td>
<td>100–3950</td>
<td>1000–2000</td>
<td>220–265</td>
</tr>
<tr>
<td>fᵢ (bar)</td>
<td>0.65–1148</td>
<td>1.48–1778</td>
<td>98–4686</td>
<td>681–1678</td>
<td>0.02–70</td>
</tr>
<tr>
<td>T (°C)</td>
<td>930</td>
<td>930</td>
<td>825–1200</td>
<td>1100</td>
<td>700–1000</td>
</tr>
<tr>
<td>H₂Oᵐᵉˡᵗ (wt%) ᵇ</td>
<td>2.48–9.29</td>
<td>2.68–6.29</td>
<td>0.75–10.02</td>
<td>2.08–2.64</td>
<td>n.a.</td>
</tr>
<tr>
<td>FeO* (wt%) ᶜ</td>
<td>3.49</td>
<td>3.49</td>
<td>1.39–5.74</td>
<td>2.61</td>
<td>0.08–1.6</td>
</tr>
<tr>
<td>MgO (wt%) ᶜ</td>
<td>0.33</td>
<td>0.33</td>
<td>0.07–1.04</td>
<td>0.43</td>
<td>0.08</td>
</tr>
<tr>
<td>CaO (wt%) ᶜ</td>
<td>0.79</td>
<td>0.79</td>
<td>0.38–3.63</td>
<td>3.24</td>
<td>0.75</td>
</tr>
<tr>
<td>Na₂O (wt%) ᶜ</td>
<td>10.1</td>
<td>10.1</td>
<td>2.03–11.21</td>
<td>5.07</td>
<td>4.15</td>
</tr>
<tr>
<td>K₂O (wt%)ᶜ</td>
<td>5.53</td>
<td>5.53</td>
<td>3.09–12.25</td>
<td>9.35</td>
<td>5.64</td>
</tr>
<tr>
<td>SiO₂ (wt%) ᶜ</td>
<td>59.87</td>
<td>59.87</td>
<td>53.64–59.87</td>
<td>57.15</td>
<td>74.51</td>
</tr>
</tbody>
</table>

n.a.: not applicable.

ᵃ For references, see Table 1.
ᵇ Range of H₂O solubility in the experimental melts.
ᶜ Compositional range of starting material.

<table><caption>Table 3 Equation list of the O–H system (variable solved for is $m_{O2}$).</caption>
<tbody>
<tr>
<td>
$$
\begin{aligned}
& \frac{w_{TH}}{2M_{H}(1 - m_{O2})} - \frac{w_{TO}}{M_{O}(m_{H2O} + 2m_{O2})} \\
& \quad = \frac{1}{1 - m_{O2}} \beta_{H2} m_{H2}^{b_{H2}} + \left( \frac{1}{1 - m_{O2}} - \frac{1}{m_{H2O} + 2m_{O2}} \right) \beta_{H2O} m_{H2O}^{b_{H2O}} \\
& m_{H2O} = (1 - m_{O2}) \left( 1 + n_{1} m_{O2}^{- 0.5} \right)^{- 1} \\
& m_{H2} = 1 - m_{O2} - m_{H2O} \\
& w_{gT} = \left( w_{TO}/M_{O} - \beta_{H2O} m_{H2O}^{b_{H2O}} \right) (m_{H2O} + 2m_{O2})^{- 1}
\end{aligned}
$$
</td>
<td>
$$
\begin{aligned}
& \beta_{i} = a_{i} (\gamma_{i} P)^{b_{i}} M_{i}^{- 1} \\
& n_{1} = \gamma_{H2O} K_{1}^{- 1} \gamma_{H2}^{- 1} \gamma_{O2}^{- 0.5} P^{- 0.5}
\end{aligned}
$$
</td>
</tr>
</tbody>
</table>

that dictate exsolved species proportions (Symonds et al., 1994; Burgisser et al., 2012). Processes involving the silicate liquid are slower (Baker et al., 2005, and references therein) and they are controlled by the diffusion of dissolved species within the melt, which sets rates of chemical reactions occurring between gaseous and dissolved species and those occurring between dissolved species (see Pichavant et al., 2013, for an example of kinetically controlled degassing). The speed at which gas and magma can physically separate from each other, either by buoyant rise of gas bubbles, or by gas flow through an interconnected bubble network, is arguably the lesser known of these rates, but its higher end is broadly comparable to volatile diffusion in melt. Finally, precipitation of solid phases is among the slowest processes directly controlling gas/melt partition.

With these general processes in mind, our approach assumes that, during magma ascent, gaseous species are in equilibrium with each other and with their dissolved counterparts. Crystallization kinetics, conversely, are neglected, which means that our model cannot be applied to magma compositions able to precipitate S- and Fe-bearing solids while pressure changes (Burgisser et al., 2012). The physical separation of gas and magma is either considered as instantaneous (pure gas and open-system degassing), or impossible (closed-system degassing).

The model formulation summarized here is based on that of Clemente et al. (2004), Burgisser and Scaillet (2007), and Burgisser et al. (2008). Its core tenet is that for any volatile species dissolved

**Table 4**
Equation list of the S-O-H system (variables solved for are $m_{O2}$, $m_{S2}$).

$$
\frac{w_{TO}}{M_O} = R_B(2m_{O2} + 2m_{SO2} + m_{H2O}) + \beta_{H2O}m_{H2O}^{b_{H2O}} + \beta_{SO2}m_{SO2}^{b_{SO2}}
$$

$$
\frac{w_{TH}}{2M_H} = R_B(m_{H2} + m_{H2S} + m_{H2O}) + \beta_{H2}m_{H2}^{b_{H2}} + \beta_{H2S}m_{H2S}^{b_{H2S}} + \beta_{H2O}m_{H2O}^{b_{H2O}}
$$

$$
m_{H2O} = n_4 m_{S2}^{-0.25} m_{H2}^{-1} m_{SO2}^{0.5}
$$

$$
m_{H2} = n_2 m_{H2S} n_1^{-1} m_{S2}^{-0.5}
$$

$$
m_{SO2} = n_1 n_5 m_{O2} m_{S2}^{0.5}
$$

$$
m_{H2S} = \frac{1 - m_{O2} - m_{S2} - m_{SO2}}{1 + n_2 n_1^{-1} m_{S2}^{-0.5} + n_3 m_{O2}^{0.5} m_{S2}^{-0.5}}
$$

$$
\beta_i = a_i(\gamma_i P)^{b_i} M_i^{-1}
$$

$$
R_B = \left( \frac{w_{TS}}{M_S} - \beta_{SO2} m_{SO2}^{b_{SO2}} - \beta_{H2S} m_{H2S}^{b_{H2S}} \right) (m_{S2} + m_{SO2} + m_{H2S})^{-1}
$$

$$
n_1 = \sqrt{\gamma_{S2} P}
$$

$$
n_2 = \gamma_{H2S} K_1^{-1} K_3^{-1} \gamma_{H2}^{-1}
$$

$$
n_3 = \gamma_{H2S} \gamma_{O2}^{0.5} K_3^{-1} \gamma_{H2O}^{-1} \gamma_{S2}^{0.5}
$$

$$
n_4 = K_1 K_2^{0.5} \gamma_{H2} P^{0.25} \gamma_{H2O}^{-1} \gamma_{S2}^{-0.25} \gamma_{SO2}^{-0.5}
$$

$$
n_5 = K_2 \gamma_{O2} \gamma_{SO2}^{-1}
$$

$$
w_{gT} = R_B \sum_i m_i M_i
$$

---

**Table 5**
Equation list of the C-S-O-H-Fe system (variables solved for are $m_{CO}$, $m_{CO2}$, $m_{CH4}$).

$$
\frac{w_{TO}}{M_O} = R_C(m_{CO} + 2m_{CO2} + 2m_{O2} + m_{H2O} + 2m_{SO2}) + 2\beta_{SO2}m_{SO2}^{b_{SO2}} + \beta_{H2O}m_{H2O}^{b_{H2O}}
$$

$$
+ 2\beta_{CO2}m_{CO2}^{b_{CO2}} + \frac{m_{Fe}}{\sum_i m_i M_i} \frac{1+3F}{1+2F}
$$

$$
\frac{w_{TH}}{2M_H} = R_C(m_{H2O} + m_{H2} + m_{H2S} + 2m_{CH4}) + \beta_{H2}m_{H2}^{b_{H2}} + \beta_{H2O}m_{H2O}^{b_{H2O}} + \beta_{H2S}m_{H2S}^{b_{H2S}}
$$

$$
\frac{w_{TS}}{M_S} = R_C(m_{SO2} + m_{H2S} + 2m_{S2}) + \beta_{SO2}m_{SO2}^{b_{SO2}} + \beta_{H2S}m_{H2S}^{b_{H2S}}
$$

$$
m_{H2O} = n_6 m_{CO2}^{1.5} m_{CH4}^{0.5} m_{CO}^{-2}
$$

$$
m_{O2} = n_4^2 m_{CO2}^2 m_{CO}^2
$$

$$
m_{H2} = n_7 m_{CO2}^{0.5} m_{CH4}^{0.5} m_{CO}^{-1}
$$

$$
m_{SO2} = - 0.5 c_2 c_1^{-1} + \left(0.25 c_2^2 c_1^{-2} + c_3 c_1^{-1}\right)^{0.5}
$$

$$
m_{H2S} = n_9 m_{CO} m_{CH4}^{0.5} m_{SO2} m_{CO2}^{-1.5}
$$

$$
m_{S2} = n_8 m_{SO2}^2 m_{CO}^4 m_{CO2}^{-4}
$$

$$
R_C = \left( \frac{w_{TC}}{M_C} - \beta_{CO2} m_{CO2}^{b_{CO2}} \right) (m_{CO} + m_{CO2} + m_{CH4})^{-1}
$$

$$
\beta_i = a_i(\gamma_i P)^{b_i} M_i^{-1}
$$

$$
c_1 = n_3^2 m_{O2}^{-2}
$$

$$
c_2 = 1 + n_3 m_{H2O} n_2^{-1} m_{O2}^{-1.5}
$$

$$
c_3 = 1 - m_{H2O} - m_{O2} - m_{H2} - m_{CO} - m_{CO2} - m_{CH4}
$$

$$
n_1 = K_1 \gamma_{H2} \gamma_{O2}^{0.5} P^{0.5} \gamma_{H2O}^{-1}
$$

$$
n_2 = K_2 \gamma_{H2S} \gamma_{O2}^{0.5} \gamma_{H2O}^{-1} \gamma_{S2}^{-1}
$$

$$
n_3 = K_3 \gamma_{SO2} \gamma_{O2} \gamma_{S2}^{-1} \gamma_{SO2}^{-0.5} P^{-0.5}
$$

$$
n_4 = K_4 \gamma_{CO2} \gamma_{CO}^{-1} \gamma_{O2}^{-0.5} P^{-0.5}
$$

$$
n_5 = K_5 \gamma_{CO2} \gamma_{H2O}^{-1} \gamma_{CH4}^{-1} \gamma_{O2}^{-2}
$$

$$
n_6 = n_4^2 n_5^{-0.5}
$$

$$
n_7 = n_6 n_1^{-1} n_4^{-1}
$$

$$
n_8 = n_3^2 n_4^{-4}
$$

$$
n_9 = n_6 n_8^{0.5} n_2^{-1} n_4^{-1}
$$

$$
w_{gT} = R_C \sum_i m_i M_i
$$

---

in a fluid-saturated silicate melt, equilibrium conditions impose that the fugacity $f_i$ of species $i$ in the gas phase equals that in the melt (e.g., Scaillet and Pichavant, 2005). In order to establish these fugacities, we combine mass balances and the equilibrium constants of the reactions occurring in the gas phase (Holloway, 1987; Iacono-Marziano et al., 2012; Gaillard and Scaillet, 2014). The dissolved amounts of the soluble species are, on the other hand, determined by using solubility laws that are a function of the corresponding species fugacities.

The reactions that govern the redox state of the gas phase all involve molecular oxygen:

$$
H_2O = H_2 + 1/2O_2 \tag{1}
$$

$$
1/2S_2 + H_2O = H_2S + 1/2O_2 \tag{2}
$$

$$
1/2S_2 + O_2 = SO_2 \tag{3}
$$

$$
CO + 1/2O_2 = CO_2 \tag{4}
$$

$$
CH_4 + 2O_2 = CO_2 + 2H_2O \tag{5}
$$

The equilibrium constants of these reactions, $K_1$-$K_5$, as well as the reaction $C+O_2=CO_2$ that yields graphite activity are calculated following Ohmoto and Kerrick (1977). The gas is thus composed of 9 species ($H_2O$, $H_2$, $O_2$, $SO_2$, $H_2S$, $S_2$, $CO_2$, $CO$, and $CH_4$), which have each a molar fraction $m_i$:

$$
\sum_{i=1}^9 m_i = 1 \tag{6}
$$

An additional reaction, $OCS+H_2O=CO_2+H_2S$, is only used in the software for gas species calculations at atmospheric pressure (its equilibrium constant is given by Symonds and Reed, 1993). We assume ideal mixing in the gas phase, which yields the following expression for species fugacities (e.g., Ohmoto and Kerrick, 1977; Shi and Saxena, 1992; Larsen, 1993; Huizenga, 2005).

$$
f_i = \gamma_i m_i P \tag{7}
$$

where $P$ is total pressure and $\gamma_i$ are species fugacity coefficients that are calculated using the Lewis and Randall rule, which states that the fugacity coefficient of species $i$ in the gas mixture equals that of the pure species at the same pressure and temperature (the 1 bar standard state at the temperature of interest is adopted). The coefficient $\gamma_{H2O}$ is from Holland and Powell (1991), $\gamma_{H2}$ is from

![](./images/814650004370096129_4.jpg)

Fig. 1. User interface of D-Compress. (A). Main window. (B) Window used to modify the melt composition and the parameters controlling the numerical resolutions.

Shaw and Wones (1964), and the other coefficients are from Shi and Saxena, (1992). The gas is thus considered as an ideal mixture of real pure gases.

Solubility is usually defined as the maximum concentration of a volatile species coexisting with a pure fluid ($H_2O$ with $H_2O$-only fluid, etc.) but, in our multicomponent volatile system, we define solubility as the maximum amount of a given volatile species that remains in solution at the corresponding pure species fugacity. We assume that the dissolved amount of species $i$ is related to that species fugacity, $f_i$, by a power law. Chemical equilibrium implying equalities of species fugacities in both phases, we use the $f_i$ established for the gas Eq. (7) to calculate the dissolved amount of species $i$. The total weight fraction of each species $(w_{Ti})$ is thus the sum of its exsolved part and its dissolved part (Burgisser et al., 2008)

$$
w_{Ti} = w_{gT}x_{i} + a_{i}(f_{i})^{b_{i}} \tag{8}
$$

where $w_{gT}$ is the total gas weight fraction, the second term on the right-hand side is the solubility law and, and $a_i$ and $b_i$ are experimentally-determined constants that depend, when relevant,

![](./images/814650004370096129_5.jpg)

Fig. 2. TAS diagram of the melt compositions used to calibrate the solubility laws. Circles, triangles, and squares represent "basaltic", "phonolitic", and "rhyolitic" compositions, respectively. The diamond represents the unique melt composition used to calibrate the H₂ solubility law. Selected oxides proportions are given in Table 2 and full melt compositions are given in the user manual (Appendix A).

![](./images/814650004370096129_6.jpg)

Fig. 3. Schematic representation of the three modes of compression/decompression. (A) Closed-system behavior assumes that gas and melt are moving together. (B) Open-system behavior assumes that the gas is separated away from the moving melt. (C) Gas-only behavior assumes that the gas is moving independently from the melt, which remains stagnant. The situation where the melt is chemical equilibrium with the flowing gas is simulated by calculating melt volatile contents after the gas compression/decompression so that the mass balance between gas and melt is not enforced ("Equilibrium a posteriori").

on melt composition and temperature (Tables 1 and 2). Appendix B shows how $a_{H2S}$, $b_{H2S}$, $a_{SO2}$, and $b_{SO2}$ were calibrated for basalts and how to build a new solubility law for H₂O in phonolite. Conversion between molar fraction, $m_i$, and weight fraction, $x_i$, is carried out using

$$
x_{i}=\frac{m_{i} M_{i}}{\sum_{j} m_{j} M_{j}} \tag{9}
$$

where $M_i$ are molecular weights of each species.

Since our modeling focuses on magma ascent, pressure changes are assumed faster than crystallization dynamics, but slow enough to allow equilibration of gases and liquids, which includes dissolved oxides and immiscible liquid phases. In sulfur-bearing systems, immiscible sulfide liquid may occur, which sequesters part of the S present in the system (Scaillet et al., 1998). This is not simulated in our model so calculations are stopped automatically if the temperature is above the melting temperature of FeS (Moretti and Baker, 2008) and $f_{S2}$ is larger than that at FeS saturation (Liu et al., 2007). Conversely, if FeS is saturated as pyrrhotite, no error is generated because it is a solid phase. In iron-bearing systems, the model takes into account the way that the iron dissolved in the silicate liquid affects the redox state of the magma by exchanging oxygen with the gas phase:

$$
\mathrm{FeO}_{(\text{melt})}+1 / 2 \mathrm{O}_{2}=\mathrm{Fe}_{2} \mathrm{O}_{3(\text{melt})} \tag{10}
$$

This reaction is not calculated through equilibrium constant but thanks to the ratio of the molar fractions of Fe₂O₃ and FeO, $F = m_{Fe2O3}/m_{FeO}$ (Kress and Carmichael, 1991).

Mass balances are enforced by keeping the total weight percents of atomic oxygen ($w_{TO}$), atomic hydrogen ($w_{TH}$), atomic sulfur ($w_{TS}$), and atomic carbon ($w_{TC}$) constant

$$
\begin{aligned}
\frac{w_{T O}}{M_{O}}=& \frac{w_{T H 2 O}}{M_{H 2 O}}+2 \frac{w_{T O 2}}{M_{O 2}}+2 \frac{w_{T S O 2}}{M_{S O 2}}+2 \frac{w_{T C O 2}}{M_{C O 2}}+\frac{w_{T C O}}{M_{C O}} \\
&+\frac{w_{T F e}}{M_{F e}} \frac{1+3 F}{1+2 F}
\end{aligned} \tag{11}
$$

$$
\frac{w_{T H}}{2 M_{H}}=\frac{w_{T H 2 O}}{M_{H 2 O}}+\frac{w_{T H 2}}{M_{H 2}}+\frac{w_{T H 2 S}}{M_{H 2 S}}+2 \frac{w_{T C H 4}}{M_{C H 4}} \tag{12}
$$

$$
\frac{w_{T S}}{M_{S}}=2 \frac{w_{T S 2}}{M_{S 2}}+\frac{w_{T H 2 S}}{M_{H 2 S}}+\frac{w_{T S O 2}}{M_{S O 2}} \tag{13}
$$

$$
\frac{w_{T C}}{M_{C}}=\frac{w_{T C O}}{M_{C O}}+\frac{w_{T C O 2}}{M_{C O 2}}+\frac{w_{T C H 4}}{M_{C H 4}} \tag{14}
$$

The gas volume fraction, $\alpha$, is calculated according to

$$
\alpha=\left[1+\frac{M P\left(1-w_{g l}\right)}{R T \rho_{l} w_{g l}}\right]^{-1} \tag{15}
$$

where $R$ is the universal gas constant (8.3144 J/mol K), $\rho_l$ is the magma density ($\mathrm{kg/m^3}$), which is a function of melt composition (Spera, 2000), and $M$ is the average molar mass of the gas phase

$$
M=\sum_{i=1}^{9} x_{i} M_{i} \tag{16}
$$

## 3. Numerical resolution

Two types of solutions can be searched for with D-Compress. The first is finding the equilibrium conditions of all species when only a subset of variables is known. These initial variables are $f_{H2}$, $f_{H2O}$, $f_{CO2}$, $w_{gT}$, $P$, $T$, and total iron FeO*. When a H₂O or CO₂ melt content is given instead of $f_{H2O}$ and $f_{CO2}$, the respective fugacities are found using the solubility laws. When a redox state is supplied instead of $f_{H2}$, equilibrium (1) and $f_{H2O}$ are used to retrieve $f_{H2}$. The three fugacities, $P$, $T$, and reactions (1–6) are then used algebraically to find all $m_i$ and $f_i$. When the molar ratios CO₂/CO, CO₂/SO₂, CO₂/H₂O, either of H₂S/SO₂ or SO₂/OCS, and either of $P$ or $T$ are set initially, no algebraic solution exists to retrieve the other species molar fractions. Instead, either $P$ or $T$ is considered as unknown and a globally convergent Newton algorithm ensures that Eq. (6) is satisfied. In other words, the user sets four species ratios and either sets the pressure to find the equilibrium gas temperature, or sets the temperature to find the equilibrium pressure. For any

![](./images/814650004370096129_7.jpg)

Fig. 4. Isobaric calculations of H₂O and CO₂ melt contents by four models (D-Compress, VolatilCalc, Iacono-Marziano et al., 2012, and Papale et al., 2006). Melt compositions are those proposed by default in D-Compress. In the Papale et al. (2006) model, quantities of Fe₂O₃ and FeO were adjusted using the FeO* value and the corresponding molar ratio given by D-Compress. Gray areas indicate uncertainty ranges for D-Compress. (A) Basaltic melt at 1000 °C and NNO+1. (B) Rhyolitic melt at 850 °C and NNO+1. Data from Blank et al. (1993) are at 750 bar and the 12% correction on melt CO₂ content proposed by Botcharnikov et al. (2005) is of a size similar to that of the symbols. Uncertainties of the D-Compress 750 isobar are omitted for clarity. (C) Phonolitic melt at 1000 °C and NNO-1.

given P or T, a combination of equilibrium constants is used to retrieve the missing fugacities and the fugacity coefficients are used to find the molar fractions involved in Eq. (6).

Once all molar fractions are calculated, the atomic composition of the exsolved volatiles (i.e. amounts of S, O, H, and C, Eqs. 11-14) is computed. If melt is involved in the calculation, the total atomic composition is found by adding the dissolved volatiles (Eq. 7) to the gas. The amount of oxygen fixed by FeO* is found by using F and $f_{O2}$. The other four subsets of the full system (O-H, S-O-H, C-S-O-H, and C-O-H) are treated in a similar way.

The second type of resolution is to change pressure by compression or decompression while assuming mass conservation of the atomic elements. This mass conservation is applied either to the gas only, or to both melt and gas. This second step is available for 4 combinations (O-H, S-O-H, C-S-O-H, and C-S-O-H-Fe) of the full system presented above. Mass conservation (6) and (11-14), chemical equilibrium (1-6), and solubility laws (8) are used jointly to algebraically reduce the system to the smallest possible number of equations (Tables 3-5). The full system, for instance, can be so reduced to three conservation equations on $w_{TO}$, $w_{TS}$, and $w_{TH}$ (Table 5). D-Compress uses a globally convergent Newton algorithm with numerically-determined Jacobian matrix (Press et al., 2006) such that these three quantities are conserved to a user-defined precision. The variables solved for are $m_{CO2}$, $m_{CO}$, $m_{CH4}$. From one iteration to the next, the changes in these molar fractions should be at least the value of the "Tolerance on stalling" parameter and at most the value of the "Tolerance on change" parameter. The algorithm takes the user-defined initial step (typically 1/1000 of the initial pressure) and varies it between a maximum (typically 1/100 of the maximum pressure reached during the run) and a minimum (typically 1 Pa) value. Every 5 successful iterations, the pressure step increases by 20%, whereas

![](./images/814650004370096129_8.jpg)

Fig. 5. Isobaric calculations (500, 1000, 2000, and 3000 bars) of S and CO₂ melt contents with varying H₂O melt content in the C-O-H-S-Fe basaltic system. The melt composition is that proposed by default in D-Compress. Melt inclusion data for Etna are from Spilliaert et al. (2006).

every failed iteration causes the step to decrease by 20%.

Mass conservation of the gaseous species (Eq. 6), which involves adding exactly $m_{H2O} (\sim 10^{-1})$ and $m_{O2} (\sim 10^{-15})$, is beyond standard machine precision (about 16 significant digits for IEEE 754 binary64 standard). To keep sufficient precision, we used a specific number coding called Binary Coded Decimal (BCD), which allows for 26 significant digits but markedly slows down the numerical resolution. This level of precision is necessary to maintain an accuracy $< 10^{-4}$ on the conserved quantities $w_{TO}$, $w_{TS}$, and $w_{TH}$, which is a typical maximal value ensuring numerical stability (Burgisser et al., 2008). The code is written in Turbo Delphi 2006 with the BCD library Systools from TurboPower. It is compiled for Windows® OS (XP, Vista, 7).

## 4. Fixed pressure calculations and input parameters

D-Compress enables the user to calculate the gas and melt volatile composition of 5 systems: O-H, S-O-H, C-S-O-H, C-S-O-H-Fe, and C-O-H. These are selected in the panel labeled "Chemical system" in the upper left of the main window (Fig. 1A). For all systems, at least three input parameters are needed to establish the gas and melt volatile compositions: gas weight fraction, pressure, and temperature. Depending on which system is selected, there are up to three additional parameters that need to be set. There are three ways to input these parameters. The user can choose between entering the fugacities of $H_2$, $H_2O$, and $CO_2$, entering the redox state and the fugacities of $H_2O$ and $CO_2$, entering the redox state and the melt content of $H_2O$ and $CO_2$, and entering a combination of ratios of gas species fugacities (or molar proportions) of $CO_2$, $CO$, $SO_2$, $H_2O$, $H_2S$, and OCS. The button "Compute initial conditions" calculates all the other relevant parameters of the system selected, which are then displayed in four separate lists ("Melt", "Total", "Miscellaneous", and "Gas", Fig. 1A).

The type of melt is selected through the "Advanced parameter" window (Fig. 1B). There are three pre-defined melt compositions: basaltic, rhyolitic, or phonolitic (Fig. 2). This affects the solubility laws, which are given in Table 1. For all melts, changing the proportions of the major oxides affects the relationship between $m_{Fe2O3}/m_{FeO}$ and $f_{O2}$. Such changes are thus only apparent in compression/decompression runs. When rhyolitic melt is selected, the user has the choice between fixed and temperature-dependent solubilities. In the latter case, the software enforces the temperature range over which these relationships are valid (790-1010 °C). When a basaltic melt is selected, the user has the choice between fixed solubility coefficients and coefficients for $H_2O$ and $CO_2$ that vary according to temperature (1000-1400 °C) and composition (Iacono-Marziano et al. 2012; more details in the user manual, Appendix A). Phonolitic melts have fixed solubility coefficients that were determined at ~1000 °C (Table 2), except for $H_2O$ where temperature-dependent solubilities (825-1200 °C) can be selected. Importantly, entering a user-defined melt composition and/or solubility law is possible. This allows users to easily adapt the software to new solubility laws for other melt compositions than the three default ones without changing the compiled code (more details in Appendix B).

Isobar calculations are possible when initial conditions are set so that melt volatile contents are used as input (tab "melt", Fig. 1A). To start such a calculation, the user must select which of redox, $H_2O$, and $CO_2$ will be varied over how many steps, as well as between which bounds the linear variation will take place. Isobar output parameters are the melt amounts of the soluble species, the pressure, the temperature, the redox state, and the gas composition in molar fraction.

## 5. Compression/decompression calculations

The parameters controlling the compression or decompression calculation are the final pressure and which type of run will be performed: "Closed system", "Gas only", or "Open system". Closed-system runs assume that the gas is in equilibrium with the surrounding melt (Fig. 3). There is no physical segregation between gas and melt, like in the case of a magma where gas bubbles and the surrounding melt rise at the same speed. This situation can correspond to a high-viscosity magma containing large numbers of small bubbles, or to a large gas bubble rising with its thin melt shell in low-viscosity magma (see Burgisser et al., 2012 for more details).

Gas-only runs ignore volatile contribution from the melt (Fig. 3). They are carried out by setting all solubility coefficients to zero and fixing the gas content to 100 wt%. The output file, however, includes melt volatile contents that are recalculated a posteriori using the fugacities given by the pure gas compression/decompression. These melt volatile contents can either be disregarded or considered to represent a stagnant melt through which the gas is passing; as the gas rises independently, it only encounters melt that is in equilibrium with it. The physical situation can be viewed either as a melt column undergoing steady degassing, i.e. the gas is rising from any point within the column, or as a melt column that has been flushed to equilibrium by a deeper gas source. One option of the gas-only type run is to reach the target pressure in an isentropic fashion, which causes the temperature to change at each pressure step.

Open-system runs in D-Compress are easier to explain in the case of a decompression. Like all run types, these runs are carried out by decompressing melt and gas to lower pressure in small increments. In the conventional sense, the gas composition of an open-system decompression should be fully discarded after each increment before the next step is performed (Fig. 3). Since D-Compress is based on the presence of gas, however, resetting the gas content to zero is not possible. Instead, an aliquot of gas is removed so that the small but finite value of gas fixed in the initial conditions (typically $10^{-6}$ wt%) remains for the next step. This

![](./images/814650004370096129_9.jpg)

Fig. 6. Evolution of volatile melt content and redox state with decreasing pressure for up to three degassing behaviors (closed system, open system, and gas only) by two models (D-Compress and SolEx). The melt is basaltic at 1153 °C with 5.8 wt% FeO* and either at NNO + 1.8, or at NNO-3.14. The D-Compress solubility coefficients for H₂O and CO₂ are those of Iacono-Marziano et al. (2012), the starting pressure is 3000 bars (curve extremities with the highest melt volatile content) and the end pressure is close to atmospheric (curve extremities with the lowest melt volatile content). (A) H₂O vs. CO₂ melt contents. (B) S vs. CO₂ melt contents. (C) Redox state.

procedure approaches the conventional Rayleigh distillation, i.e. the decompression of a magma batch, the gas of which is freely leaking out. Such runs yield the evolution of melt volatile content as a function of pressure. Gas composition is also given, but physical arguments show that only the gas composition at the last step of the decompression is meaningful when studying volcanic gas emissions (Burgisser et al., 2012). Compression runs in open system suffer from that limitation because they directly involve the gas aliquots discarded at each step, the composition of which is unknown during a compression. The algorithm simply assumes that these aliquots have the same composition as the remaining gas at that pressure step when it increases the gas content back to the constant, initial value.

## 6. Examples of model outputs

Example outputs of each of the software capability are compared whenever possible to a selection of outputs from other models or to experimental data that were used to calibrate D-Compress. Uncertainties intrinsic to D-Compress (i.e. due to the scatter of the calibration data) are given for typical run conditions.

![](./images/814650004370096129_10.jpg)

The largest source of error is linked to the quantification of dissolved species (see below). In the gas phase, D-Compress is able to calculate the equilibrium temperature of natural volcanic gases at atmospheric pressure to $\pm 5\ ^{\circ}\text{C}$ from their gas composition (Burgisser et al., 2012). At higher pressure, where non-ideal effects are larger, the assumption of ideal mixing needs to be tested. Relative differences between measured (Jakobsson and Oskarsson, 1990) and calculated C-O-H gas compositions at 5000 bar are similar between a model assuming non-ideal mixture of real gases (GFluid, Zhang and Duan, 2010) and D-Compress. Using D-Compress at $900\ ^{\circ}\text{C}$, these differences in molar fractions are of 7%, 41%, 8%, 35%, and 91% for $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{CH}_4$, $\text{H}_2$, and CO, respectively. At $1000\ ^{\circ}\text{C}$, these respective differences become 6%, 94%, 4%, 21%, and 43%. By comparison, the real mixture model GFluid reproduces measured molar fractions within 27%, 33%, 16%, 82%, and 49% at $900\ ^{\circ}\text{C}$ and 21%, 118%, 14%, 31%, and 32% at $1000\ ^{\circ}\text{C}$. For both models, the least precise estimates are for $\text{CO}_2$ and CO. Since the test pressure is well above our calibration limit of 3000 bars, these errors are maxima.

### 6.1. Fixed pressure runs

Fig. 4 shows isobars of $\text{H}_2\text{O}$ vs. $\text{CO}_2$ melt contents for basaltic, phonolitic and rhyolitic melts produced by D-Compress, VolatilCalc (Newman and Lowenstern, 2002), and the models of Iacono-Marziano et al. (2012) and Papale et al. (2006). VolatilCalc considers an ideal mixture of two real gases ($\text{H}_2\text{O}$ and $\text{CO}_2$), Iacono-Marziano et al. (2012) consider an ideal mixture of two ideal gases, and Papale et al. (2006) consider a real mixture of two real gases. Runs made by D-Compress were done using the solubility laws by default (Table 1) in the C-O-H system, which comprises $\text{H}_2\text{O}$, $\text{O}_2$, $\text{H}_2$, CO, $\text{CO}_2$, and $\text{CH}_4$. D-Compress outputs are close to those of VolatilCalc up to 2000 bar. In the case of rhyolite, it reflects the common dataset used to calibrate both models, as shown by the nice fit with the data from Blank et al. (1993) at 750 bar (Fig. 4B). The difference between D-Compress and the Papale et al. (2006) model outputs is more marked, partly because the different sets of calibration data (Table 1). In particular, the low $\text{CO}_2$ concentrations predicted by Papale et al. (2006) at low pressure for basalts are a known consequence of the database used for its calibration (Shishkina et al., 2010). The model of Iacono-Marziano et al. (2012) can be selected in D-Compress instead of the solubility law of Table 1. It should be used preferentially because it is calibrated for a large range of melt composition, except for alkali-rich basalts where it tends to under-estimate melt water content (Fig. 4A).

Uncertainties in melt species contents in D-Compress can be quantified using the scatter inherent to the calibration experimental data (Appendix B3). The gray areas in Fig. 4 surrounding the D-Compress outputs were calculated by using two extreme fittings; one being based only on the experimental melt volatile contents higher than the globally fitted curve, and the other being based only on the data points lower than the globally fitted curve. These two fittings were done for each species, which yielded four

![](./images/814650004370096129_11.jpg)

Fig. 8. Evolution of gas quantity and composition with decreasing pressure for a basalt at 1000 °C and degassing in closed system. Runs are done with D-Compress (bold curves) and PELE 7.04 (thin curves). (A) Gas composition. S₂ is not shown because it is not calculated by PELE and CH₄ is not shown because both models predict CH₄ molar amounts ≪10⁻⁵. (B) Gas weight fraction (left vertical axis) and redox state (right vertical axis) as a function of pressure.

solubility coefficients ($a_i$ and $b_i$) for H₂O and CO₂. Four isobars were then calculated by changing one set of coefficients at a time. The external envelope of these four isobars defines the gray areas of Fig. 4. The same procedure was applied for SO₂ and H₂S data so as to obtain typical errors for S melt content. At 2000 bars, these are +50% and −40% for rhyolite, +20% and −30% for basalt, and +20% and −20% for phonolite. Considering the outcome of the inter-model comparison on Fig. 4, it is safe to consider these un- certainties as minimum values.

Moving to the full system introduces more degrees of freedom. Fig. 5 shows isobars of S vs. CO₂ melt contents for basaltic melts. The redox state is constant at NNO+1 and isobars of two kinds are shown. The first type of isobars has amounts of water that fit data from melt inclusions hosted in olivine from Etna (Spilliaert et al., 2006): 1 wt% H₂O for ~250 ppm CO₂ (500 isobar), 2 wt% H₂O for 500–2000 ppm CO₂ (1000 and 2000 isobars), and 3 wt% H₂O for >2000 ppm CO₂ (3000 isobar). The pressure range given by these isobars on the S–CO₂ plot of Fig. 5 is very similar to the one found by ignoring S and using the C–O–H system (500–3000 bar). If, however, various degrees of H₂O loss from the inclusions are suspected, the pressures given by the C–O–H system are minimum pressures. In other words, it is possible to fit the whole range of S and CO₂ contents measured in the melt inclusions by the second type of isobars, which are all at 3000 bars but have H₂O contents ranging from 3 to 7.5 wt%.

### 6.2. Decompression runs

We carried out two sets of three decompression runs from 3000 bars down to atmospheric pressure to illustrate this feature of the software. In each set, one run was degassing melt in closed system, another was degassing melt in open system, and the last run was decompressing pure gas. The initial conditions of the two sets are such that a comparison with the SolEx model (Witham et al., 2012) can be carried out. This means that the starting pressure, basaltic melt composition, and melt H₂O and CO₂ con- tents are similar between the two models. Starting melt S content, however, is lower for SolEx (~3300 ppm) than for D-Compress (~5200 ppm) at identical redox conditions (NNO+1.8). The first set of runs from D-Compress is thus carried out at NNO+1.8 in- itially and the second set is carried out at NNO-3.14 so that initial S melt contents are similar for both models (~3300 ppm). This difference can be explained by an internal inconsistency of the dataset used to calibrate SolEx (see Appendix B).

Fig. 6 shows one of the many ways to display D-Compress outputs by focusing on the redox state and the melt contents of H₂O, CO₂, and S. For H₂O and CO₂, D-Compress and SolEx runs follow similar paths in both open and closed system (Fig. 6A). Melt H₂O and CO₂ contents of the gas-only runs are quite distinct from the other runs because pure-gas volatile contents are calculated after (de)compression controlled by mass balance (see Section 4 and Fig. 3). The models show contrasting S degassing paths, which is partly due to the different starting S melt contents. Overall, SolEx predicts a sharp decrease of S content at low pressure (~500 bars) in closed system and a quasi-constant S content in open-system degassing (Fig. 6B). D-Compress, however, predicts a smoother decrease in S with decreasing pressure regardless of degassing style. Unlike SolEx, D-Compress predicts changes in the redox state with decreasing pressure, regardless of degassing style or starting redox conditions (Fig. 6C).

Fig. 7 focuses on gas molar composition of the same eight runs (2 SolEx and 6 D-Compress). Here also, D-Compress and SolEx runs follow similar degassing paths for H₂O/CO₂ and contrasting S/CO₂ degassing paths because of the different starting S contents. Both models predict that the two ratios rapidly increase as pres- sure reaches ~1500 bar in open-system degassing. This is due to the fact that degassing at low pressure releases mostly H₂O, which dominates gas composition and causes other species to be present in very small quantities. Gas-only runs from D-Compress show no evolution of either species ratios with decompression.

Fig. 8A shows the evolution of gas composition with decreasing pressure calculated with D-Compress and PELE (Boudreau, 1999). Both runs represent the closed-system degassing of Etnean basalt at 1000 °C (Table 2). The agreement between the respective molar quantities of CO, CO₂, CH₄, and H₂O calculated by both models is satisfactory, but large discrepancies can be noted between H₂S and SO₂. The sulfur-bearing species have similar trends with decreas- ing pressure but one to two orders of magnitude difference in absolute molar fractions. The probable origin of this difference is that PELE calculates $f_{S2}$ thanks to the FeS buffer of Wallace and Carmichael (1992), which yields a $f_{S2}$ of 10¹.⁸⁴ bar at a total pres- sure of 1000 bar, instead of the C–O–H–S gas buffer used in D-Compress, which yields a $f_{S2}$ of 10⁻⁵.⁴³ bar. This interpretation is supported by the fact that values of $f_{O2}$ at the same total pressure are similar for both models (Fig. 8B). These differences in gas composition have a small effect on the evolution of gas content

![](./images/814650004370096129_12.jpg)

Fig. 9. Relative errors induced by extreme solubility laws on four dissolved species ($H_2O$, $CO_2$, S, and $H_2$) in the C-S-O-H-Fe system. All runs start from 2000 bars and have 0.1 wt% initial gas content. (A) Basaltic melt. Initial conditions for the standard basalt run are: $1200\ ^\circ C$, $f_{H2}$=1.3 bar, $f_{H2O}$=190 bar, and $f_{CO2}$=2800 bar. (B) Rhyolitic melt. Initial conditions for the standard rhyolite run are: $850\ ^\circ C$, $f_{H2}$=1 bar, $f_{H2O}$=200 bar, and $f_{CO2}$=2000 bar. (C) Phonolitic melt. Initial conditions for the standard phonolite run are: $1000\ ^\circ C$, $f_{H2}$=1.3 bar, $f_{H2O}$=190 bar, and $f_{CO2}$=2960 bar.

during decompression (Fig. 8B).

Uncertainties intrinsic to D-Compress that are associated with decompression can be estimated by error propagation. For gas-only runs, taking a gas composition and varying the equilibration temperature by $\pm5\ ^\circ C$ yields relative errors of $\pm7\%$, $\pm1\%$, $<\pm0.003\%$, and $\pm2\%$ on the gas molar ratio of $SO_2/OCS$, $CO_2/CO$, $CO_2/H_2O$, and $CO_2/SO_2$, respectively (Burgisser et al., 2012). For runs involving melt, uncertainties for each dissolved species are estimated by the extreme laws as in Fig. 4. For each of the three melt compositions and each of the five soluble species ($H_2O$, $CO_2$, $SO_2$, $H_2S$, and $H_2$), we carried out closed-system decompressions starting from the same respective initial conditions but using the maximum and minimum solubility laws of each species, respectively. Counting the three standard runs (one for each melt composition) with the average solubility laws, this yielded 33 runs. Runs with different $H_2S$ and $SO_2$ solubility laws were combined so as to give the total S melt content, which brought the total number of runs down to 27. Taking the average laws as a reference, Fig. 9 presents the relative errors that were induced by the extreme laws on the dissolved species, and Fig. 10 presents the relative errors on the gas species. Overall, errors on melt species content are on the order of a few tens of percent at the beginning of the decompression and increase up to 100% at atmospheric pressure. Errors on gas species content are on the order of a few percent at the beginning of the decompression and reach 20-50% at atmospheric pressure. In compression runs, Burgisser et al. (2012) presents a similar error analysis for phonolitic melts and find maximum errors in gas molar ratios at 1000 bars to be $\pm50\%$, $\pm10\%$, $\pm40\%$, and $\pm20\%$ for $SO_2/OCS$, $CO_2/CO$, $CO_2/H_2O$, and $CO_2/SO_2$, respectively.

### 7. Concluding remarks

The user interface of D-Compress has voluntarily been left quite flexible to maximize versatility. As a result, although unphysical

![](./images/814650004370096129_13.jpg)

Fig. 10. Relative errors induced by extreme solubility laws on four gas species (H₂O, CO₂, SO₂, and H₂S). Runs are the same as in Fig. 9. (A) Basaltic melt. (B) Rhyolitic melt. H₂ errors are not shown because are <0.03%. (C) Phonolitic melt.

inputs and outputs are generally signaled to the user (e.g., negative fugacity), inconsistencies in the input parameters are possible (e.g., selecting rhyolitic solubility laws while specifying basaltic composition). Use of D-Compress beyond the parameter ranges it has been calibrated with (Table 2) may sometimes indicate meaningful trends but surely yields incorrect absolute values.

## Acknowledgments

We would like to thank P. Lesne for helping to establish the solubility laws in basaltic melts, G. Iacono-Marziano for discussions on the strengths and limitations of experimental data, and C. Bouvet de Maisonneuve for being the perfect software user. An anonymous review and constructive reviews from A. Boudreau and R. Botcharnikov were appreciated. This project was partially funded by Grant 202844 from the European Research Council under the European FP7 and Grant FP7 MED-SUV.

## Appendix A. Suplementary information

Supplementary data associated with this article can be found in the online version at http://dx.doi.org/10.1016/j.cageo.2015.03.002.

## References

Aiuppa, A., Moretti, R., Federico, C., Giudice, G., Gurrieri, S., Liuzzo, M., Papale, P., Shinohara, H., Valenza, M., 2007. Forecasting Etna eruptions by real-time observation of volcanic gas composition. Geology 35, 1115-1118.

Ariskin, A.A., Danyushevsky, L.V., Bychkov, K.A., McNeill, A.W., Barmina, G.S., Nikolaev, G.S., 2013. Modeling solubility of Fe-Ni sulfides in basaltic magmas: the effect of nickel. Econ. Geol. 108, 1983-2003.

Baker, D.R., Freda, C., Brooker, R.A., Scarlato, P., 2005. Volatile diffusion in silicate melts and its effects on melt inclusions. Ann. Geophys. 48, 699-717.

Beermann, O., Botcharnikov, R.E., Holtz, F., Diedrich, O., Nowak, M., 2011. Temperature dependence of sulfide and sulfate solubility in olivine-saturated basaltic magmas. Geochim. Cosmochim. Acta 75, 7612-7631.

Belonoshko, A., Saxena, S.K., 1992. A molecular dynamics study of pressure-volume-temperature properties of super-critical fluids: 1. H₂O. Geochim. Cosmochim. Acta 55, 381-387.

Blank, J.G., Stolper, E.M., Carroll, M.R., 1993. Solubilities of carbon dioxide and water in rhyolitic melt at 850 °C and 750 bar. Earth Planet. Sci. Lett. 119, 27-36.

Botcharnikov, R., Freise, M., Holtz, F., Behrens, H., 2005. Solubility of C-O-H

mixtures in natural melts: new experimental data and application range of recent models. Ann. Geophys. 48, 633-646.

Botcharnikov, R.E., Linnen, R.L., Wilke, M., Holtz, F., Jugo, P.J., Berndt, J., 2011. High gold concentrations in sulphide-bearing magma under oxidizing conditions. Nat. Geosci. 4, 112-115. http://dx.doi.org/10.1038/ngeo1042.

Boudreau, A.E., 1999. PELE-a version of the MELTS software program for the PC platform. Comput. Geosci. 25, 201-203.

Burgisser, A., Scaillet, B., 2007. Redox evolution of a degassing magma rising to the surface. Nature 445, 194-197.

Burgisser, A., Scaillet, B., Harshvardhan, 2008. Chemical patterns of erupting silicic magmas and their influence on the amount of degassing during ascent. J. Geophys. Res. 113, B12204. http://dx.doi.org/10.1029/2008JB005680.

Burgisser, A., Oppenheimer, C., Alletti, M., Kyle, P.R., Scaillet, B., Carroll, M.R., 2012. Backward tracking of gas chemistry measurements at Erebus volcano. Geo- chem. Geophys. Geosyst. 13, Q1101. http://dx.doi.org/10.1029/2012GC004243.

Carroll, M.R., Blank, J.G., 1997. The solubility of $H_2O$ in phonolitic melts. Am. Miner. 82, 549-556.

Clemente, B., Scaillet, B., Pichavant, M., 2004. The solubility of sulfur in hydrous rhyolitic melts. J. Petrol. 45, 2171-2196.

Delmelle, P., Stix, J., 2000. Volcanic Gases In: Sigurdsson, H. (Ed.), Encyclopedia of Volcanoes. Academic Press, San Diego, pp. 803-815.

Dixon, J.E., Stolper, E.M., Holloway, J.R., 1995. An experimental study of water and carbon dioxide solubilities in mid-ocean ridge basaltic liquids. Part I: calibra- tion and solubility models. J. Petrol. 36 (6), 1607-1631.

Dixon, J.E., Stolper, E.M., 1995. An experimental study of water and carbon dioxide solubilities in mid-ocean ridge basaltic liquids. Part II: applications to degas- sing. J. Petrol. 36 (6), 1633-1646.

Duan, X., 2014. A general model for predicting the solubility behavior of $H_2O$-$CO_2$ fluids in silicate melts over a wide range of pressure, temperature and com- positions. Geochim. Cosmochim. Acta 125, 582-609.

Fogel, R.A., Rutherford, M.J., 1990. The solubility of carbon dioxide in rhyolitic melts: a quantitative FTIR study. Am. Miner. 75, 1311-1326.

Gaillard, F., Scaillet, B., 2009. The sulfur content of volcanic gases on Mars. Earth and Planet. Sci. Lett. 279 (1), 34-43.

Gaillard, F., Scaillet, B., Arndt, N.T., 2011. Atmospheric oxygenation caused by a change in volcanic degassing pressure. Nature 478 (7368), 229-232.

Gaillard, F., Scaillet, B., 2014. A theoretical framework for volcanic degassing chemistry in a comparative planetology perspective and implications for pla- netary atmospheres. Earth Planet. Sci. Lett. 403, 307-316.

Gaillard, F., Schmidt, B., Mackwell, S., McCammon, C., 2003. Rate of hydrogen-iron redox exchange in silicate melts and glasses. Geochim. Cosmochim. Acta 67, 2427-2441.

Holland, T., Powell, R., 1991. A Compensated-Redlich-Kwong (CORK) equation for volumes and fugacities of $CO_2$ and $H_2O$ in the range 1 bar to 50 kbar and 100- $1600^{\circ}$ C. Contrib. Miner. Petrol. 109, 265-273.

Holloway, J.R., 1987. Igneous fluids. Rev. Mineral. Geochem. 17, 211-233.

Holtz, F., Beherens, H., Dingwell, D.B., Taylor, R.P., 1992. $H_2O$ solubility in alumi- nosilicate melts of haplogranite composition at 2 kbar. Chem. Geol. 96, 289-302.

Holtz, F., Beherens, H., Dingwell, D.B., Johannes, W., 1995. $H_2O$ solubility in haplo- granitic melts: compositional, pressure and temperature dependence. Am. Miner. 80, 94-108.

Huizenga, J.M., 2005. COH, an Excel spreadsheet for composition calculations in the C-O-H fluid system. Comput. Geosci. 31, 797-800.

Iacono-Marziano, G., 2005. Equilibrium and Disequilibrium Degassing of a Phono- litic Melt Simulated by Decompression Experiments. Univ. Palermo, Palermo, Italy, Ph.D. Disseration.

Iacono-Marziano, G., Schmidt, B.C., Dolfi, D., 2007. Equilibrium and disequilibrium degassing of a phonolitic melt (Vesuvius AD 79 "white pumice") simulated by decompression experiments. J. Volcanol. Geotherm. Res. 161, 151-164.

Iacono-Marziano, G., Morizet, Y., Le Trong, E., Gaillard, F., 2012. New experimental data and semi-empirical parameterization of $H_2O$-$CO_2$ solubility in mafic melts. Geochim. Cosmochim. Acta 97, 1-23.

Jakobsson, S., Oskarsson, N., 1990. Experimental determination of fluid composi- tions in the system C-O-H at high P and T and low fO2. Geochim. Cosmochim. Acta 54, 355-362.

Kress, V.C., Carmichael, I.S.E., 1991. The compressibility of silicate liquids containing $Fe_2O_3$ and the effect of composition, temperature, oxygen fugacity and pressure on their redox states. Contrib. Mineral. Petrol. 108, 82-92.

Larsen, J.F., Gardner, J.E., 2004. Experimental study of water degassing from pho- nolite melts: implications for volatile oversaturation during magma ascent. J. Volcanol. Geotherm. Res. 134, 109-124.

Larsen, R.B., 1993. "Geofluids": a Fortran 77 program to compute chemical prop- erties of gas species in C-O-H fluids. Comput. Geosci. 19, 1295-1320.

Lesne, P., Scaillet, B., Pichavant, M., Iacono-Marziano, G., Beny, J.M., 2011a. The $H_2O$ solubility of alkali basaltic melts: an experimental study. Contrib. Mineral. Petrol. 162, 133-151.

Lesne, P., Scaillet, B., Pichavant, M., Beny, J.M., 2011b. The carbon dioxide solubility of alkali basalts: an experimental study. Contrib. Mineral. Petrol. 162, 153-168.

Lesne, P., Scaillet, B., Pichavant, M., 2015. The solubility of sulfur in hydrous basaltic melts. Chem. Geol., In preparation.

Liu, Y., Zhang, Y., Behrens, H., 2005. Solubility of $H_2O$ in rhyolitic melts at low pressures and a new empirical model for mixed $H_2O$-$CO_2$ solubility in rhyolitic melts. J. of Volcanol. Geotherm. Res. 143, 219-235.

Liu, Y., Samaha, N.-T., Baker, D.R., 2007. Sulfur concentration at sulfide saturation (SCSS) in magmatic silicate melts. Geochim. Cosmochim. Acta 71, 1783-1799.

Mangan, M., Sisson, T., 2000. Delayed, disequilibrium degassing in rhyolite magma: decompression experiments and implications for explosive volcanism. Earth Planet. Sci. Lett. 183, 441-455.

Moncrieff, D.H.S., 1999. Sulphur Solubility Behaviour in Evolved Magmas: An Ex- perimental Study. University of Bristol, Bristol, U.K., Ph.D. Dissertation.

Moore, G., 2008. Interpreting $H_2O$ and $CO_2$ contents in melt inclusions: constraints from solubility experiments and modeling. Rev. Mineral. Geochem. 69, 33-361.

Moore, G., Vennemann, T., Carmichael, I.S.E., 1998. An empirical model for the so- lubility of $H_2O$ in magmas to 3 kilobars. Am. Mineral. 83, 36-42.

Moretti, R., Papale, P., 2004. On the oxidation state and volatile behavior in mul- ticomponent gas-melt equilibria. Chem. Geol. 213, 265-280.

Moretti, R., Ottonello, G., 2005. Solubility and speciation of sulfur in silicate melts: the Conjugated Toop-Samis-Flood-Grjotheim (CTSFG) model. Geochim. Cos- mochim. Acta 69, 801-823.

Moretti, R., Baker, D.R., 2008. Modeling the interplay of f $O_2$ and f $S_2$ along the FeS- silicate melt equilibrium. Chem. Geol. 256, 286-298.

Moretti, R., Papale, P., Ottonello, G., 2003. A Model for the Saturation of C-O-H-S Fluids in Silicate Melts In: Oppenheimer, C., Pyle, D.M., Barclay, J. (Eds.), Vol- canic Degassing. Geological Society Special Publication 213, London, pp. 81-101.

Newman, S., Lowenstern, J.B., 2002. VolatileCalc: a silicate melt-$H_2O$-$CO_2$ solution model written in visual basic for excel. Comput. Geosci. 28, 597-604.

Ohmoto, H., Kerrick, D., 1977. Devolatilization equilibria in graphitic systems. Am. J. Sci. 277, 1013-1044.

Oppenheimer, C., Moretti, R., Kyle, P.R., Eschenbacher, A., Lowenstern, J.B., Hervig, R. L., Dunbar, N.W., 2011. Mantle to surface degassing of alkalic magmas at Erebus volcano, Antarctica. Earth Planet. Sci. Lett. 306, 261-271.

Ottonello, G., Moretti, R., Marini, L., Vetuschi Zuccolini, M., 2001. Oxidation state of iron in silicate glasses and melts: a thermochemical model. Chem. Geol. 174, 157-159.

Papale, P., 1999. Modeling of the solubility of a two-component $H_2O$+$CO_2$ fluid in silicate liquids. Am. Mineral. 84, 477-492.

Papale, P., 2005. Determination of total $H_2O$ and $CO_2$ budgets in evolving magmas from melt inclusion data. J. Geophys. Res. 110, B03208. http://dx.doi.org/10.1029/2004JB003033.

Papale, P., Polacci, M., 1999. Role of carbon dioxide in the dynamics of magma as- cent in explosive eruptions. Bull. Volcanol. 60, 583-594.

Papale, P., Moretti, R., Barbato, D., 2006. The compositional dependence of the sa- turation surface of H2O+CO2 fluids in silicate melts. Chem. Geol. 229, 78-95.

Pichavant, M., Di Carlo, I., Rotolo, S.G., Scaillet, B., Burgisser, A., Le Gall, N., Martel, C., 2013. Generation of CO2-rich melts during basalt magma ascent and degassing. Contrib. Mineral. Petrol. 166 (2), 545-561.

Press, W.H., Teukolsky, S.A., Vetterling, W.T., Flannery, B.P., 2006. Numerical Recipes in Fortran 77: The Art of Scientific Computing, Second Edition Cambridge University Press, New York, p. 934.

Scaillet, B., Pichavant, M., 2005. A model of sulphur solubility for hydrous mafic melts: application to the determination of magmatic fluid compositions of Italian volcanoes. Ann. Geophys. 48, 671-698.

Scaillet, B., Clemente, B., Evans, B.W., Pichavant, M., 1998. Redox control of sulfur degassing in silicic magmas. J. Geophys. Res. 103 (B10), 23937-23949.

Schmidt, B., Behrens, H., 2008. Water solubility in phonolite melts: influence of melt composition and temperature. Chem. Geol. 256, 259-268.

Shaw, H.R., Wones, D.R., 1964. Fugacity coefficients for hydrogen gas between $0^{\circ}$ and $1000^{\circ}$ C, for pressures to 3000 ATM. Am. J. Sci. 262, 918-929.

Shi, P., Saxena, S.K., 1992. Thermodynamic modeling of the C-H-O-S fluid system. Am. Miner. 77, 1038-1049.

Shishkina, T.A., Botcharnikov, R.E., Holtz, F., Almeev, R.R., Portnyagin, M.V., 2010. Solubility of $H_2O$- and $CO_2$-bearing fluids in tholeiitic basalts at pressures up to 500 MPa. Chem. Geol. 277, 115-125.

Spera, F.J., 2000. Physical Properties of Magma In: Sigurdsson, H. (Ed.), Encyclopedia of Volcanoes. Academic Press, San Diego, pp. 171-190.

Spilliaert, N., Allard, P., Métrich, N., Sobolev, A.V., 2006. Melt inclusion record of the conditions of ascent, degassing, and extrusion of volatile-rich alkali basalt during the powerful 2002 flank eruption of Mount Etna (Italy). J. Geophys. Res. 111, B04203. http://dx.doi.org/10.1029/2005JB003934.

Symonds, R.B., Reed, M.H., 1993. Calculations of multicomponent chemical equili- bria in gas-solid-liquid systems: calculation methods, thermochemical data, and applications to studies of high-temperature volcanic gases with example of Mount St. Helens. Am. J. Sci. 293, 758-864.

Symonds, R.B., Rose, W.I., Bluth, G.J.S., Gerlach, T.M., 1994. Volcanic-gas studies: methods, results, and applications. Rev. Mineral. 30, 1-66.

Wallace, P., Carmichael, I.S.E., 1992. Sulfur in basaltic magmas. Geochim. Cosmo- chim. Acta 56, 1863-1874.

Witham, F., Blundy, J., Kohn, S.C., Lesne, P., Dixon, J., Chruakov, S.V., Botcharnikov, R., 2012. SolEx: a model for mixed COHSCI-volatile solubilities and exsolved gas compositions in basalt. Comput. Geosci. 45, 87-97.

Zhang, C., Duan, Z., 2010. GFluid: an Excel spreadsheet for investigating C-O-H fluid composition under high temperatures and pressures. Comput. Geosci. 36, 569-572.