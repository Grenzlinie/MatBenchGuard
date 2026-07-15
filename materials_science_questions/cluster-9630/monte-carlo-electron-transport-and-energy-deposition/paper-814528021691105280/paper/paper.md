# Optimization of Silicon parameters as a betavoltaic battery: Comparison of Si p-n and Ni/Si Schottky barrier

Faezeh Rahmani $^{a,*}$, Hossein Khosravinia $^{b}$

$^{a}$ Department of Physics, KN Toosi University of Technology, Tehran 1969764499, Iran
$^{b}$ Department of Radiation Application, Shahid Beheshti University, Tehran 1983963113, Iran

---

### HIGHLIGHTS

- Silicon parameters were studied in betavoltaic batteries.
- Studied betavoltaic batteries include p-n and Schottky barrier structures.
- The p-n structure has higher conversion efficiency.

---

### ARTICLE INFO

**Article history:**
Received 7 January 2015
Received in revised form
17 April 2016
Accepted 19 April 2016
Available online 21 April 2016

**Keywords:**
Betavoltaic battery
Si
$^{63}$Ni
p-n junction
Schottky barrier

---

### ABSTRACT

Theoretical studies on the optimization of Silicon (Si) parameters as the base of betavoltaic battery have been presented using Monte Carlo simulations and the state equations in semiconductor to obtain maximum power. Si with active area of $1\ \text{cm}^2$ has been considered in p-n junction and Schottky barrier structure to collect the radiation induced-charge from $10\ \text{mCi}\ \text{cm}^{-2}$ of Nickle-63 ($^{63}$Ni) Source. The results show that the betavoltaic conversion efficiency in the Si p-n structure is about 2.7 times higher than that in the Ni/Si Schottky barrier structure.

© 2016 Published by Elsevier Ltd.

---

## 1. Introduction

Betavoltaic battery due to its high energy density, long lifetime, and convenience of integration and miniaturization can be an appropriate option for low-power purposes such as the potential use in wireless networks, temperature sensors and micro-electromechanical systems (Li et al., 2012a; Ghasemi Nejad et al., 2014; Ghasemi Nejad and Rahmani, 2016).

These batteries utilize a radiation source incorporating with a semiconductor junction device to generate power. Theoretically, any kind of radiation source can be used to generate electricity, but only the pure beta-emitting radioisotopes are suitable for a long-lived semiconductor-based device (Honsberg et al., 2005). Also, semiconductor can be selected in p-n, p-i-n or Schottky barrier structures (Zuo et al., 2013; Lei et al., 2014; Guo et al., 2011; Wu et al., 2011; Lu et al., 2011; Liu et al., 2012; Li et al., 2012b; San et al., 2013).

The current paper presents a theoretical study based on the combination of Monte Carlo simulations (for beta energy spectrum) and the state equations in semiconductor for Si as a planar betavoltaic battery in p-n and Schottky barrier structures and 63Ni as a radioisotope source. Calculation of energy deposition in Si using full beta energy spectrum (instead of average energy of beta particles) was investigated in this paper. Basic parameters of Si in two structures were studied and the obtained results containing open-circuit voltage ($V_{OC}$), short-circuit current density ($J_{SC}$), conversion efficiency ($\eta$), doping concentration and thickness of regions in semiconductor are evaluated to present the optimum design of betavoltaic battery.

---

## 2. Material and methods

### 2.1. Selection of semiconductor and source

The conversion efficiency ($\eta$) of the betavoltaic batteries increases with increasing the band-gap of semiconductor ($E_g$) (Olsen, 1993), but according to the cost and availability, Si has been

---

*Corresponding author.
E-mail address: FRahmani@KNTU.ac.ir (F. Rahmani.)

http://dx.doi.org/10.1016/j.radphyschem.2016.04.012
0969-806X/© 2016 Published by Elsevier Ltd.

![](./images/814528021691105280_1.jpg)

Fig. 1. Energy spectrum of beta particles of $^{63}$Ni (Yao et al., 2012).

selected as the semiconductor material to form p-n junction and Schottky barrier in betavoltaic batteries.

Some pure beta-emitting radioisotopes are $^{90}$Sr/$^{90}$Y, $^{85}$Kr, $^{3}$H, $^{63}$Ni. $^{90}$Sr/$^{90}$Y (E$_{avg}$=196 and 935 keV) and $^{85}$Kr (E$_{avg}$=251 keV) may be thought to be appropriate for higher power applications due to their hard beta spectra, but it was shown that the threshold of radiation damage in Si is about 145 keV (Chandrashekhar, 2007) which is lower than average energy of these sources.

Tritium due to its very soft beta spectrum (E$_{avg}$=5.7 keV) is extensively used in biological applications, but its low half-life (T$_{1/2}$ ≈ 12.3 year) limits its application (Honsberg et al., 2005).

Half-life of $^{147}$Pm is low (T$_{1/2}$ ≈ 2.6 year), so this source can not be an appropriate selection for long-term application.

According to these, $^{63}$Ni has been selected for designing beta- voltaic batteries as the radioisotope source due to its soft beta spectrum (E$_{avg}$=17 keV, E$_{max}$ ≈ 67 keV) and long half-life (T$_{1/2}$ ≈ 100 year). Fig. 1 shows the beta spectrum of $^{63}$Ni.

### 2.2. Design of betavoltaic battery

#### 2.2.1. p-n structure

A cross-section of the betavoltaic battery based on p-n junction with the junction depth of $x_j$ is shown in Fig. 2.

As shown in Fig. 2, $\beta$ show the emitted beta particles from $^{63}$Ni. $L_n$ and $L_p$ are the minority carrier diffusion length in the base region ((p-Si)), and emitter (n$^+$-Si), respectively. These parameters are expressed as follows (XiaoBin et al., 2012):

$$
L_{n}=\sqrt{\frac{k T}{q}\left(232+\frac{1180}{1+\left(\frac{N_{a}}{8 E 16}\right)^{0.9}}\right) \cdot \frac{1}{3.345 E-12 N_{a}+9.5 E-32 N_{a}^{2}}}
\tag{1}
$$

$$
L_{p}=\sqrt{\frac{k T}{q}\left(130+\frac{370}{1+\left(\frac{N_{d}}{8 E 17}\right)^{1.25}}\right) \cdot \frac{1}{7.8 E-13 N_{d}+1.8 E-31 N_{d}^{2}}}
\tag{2}
$$

where, k is the Boltzmann's constant, T is the absolute temperature, and q is an electron charge. N$_D$ and N$_A$ are the doping concentration in emitter and base region, respectively. w is the width of the depletion region which is given by (Neudeck, 1989):

$$
w=\sqrt{\frac{2 K_{s} \varepsilon_{0} V_{b i}}{q} \frac{\left(N_{A}+N_{D}\right)}{N_{A} N_{D}}}
\tag{3}
$$

where, K$_s$ is dielectric constant, V$_{bi}$ is built-in voltage, and $\varepsilon_0$ is vacuum dielectric constant.

![](./images/814528021691105280_2.jpg)

Fig. 2. Schematic view of the betavoltaic battery based on the p-n junction.

#### 2.2.2. Schottky structure

A cross-section of the betavoltaic battery based on Schottky barrier diode is shown in Fig. 3.

where, $L_p$ is the minority-carrier (hole) diffusion length in the low doped n-type region (n$^-$) and w is the depletion width that is expressed as follows (Qiao et al., 2011):

$$
w=\sqrt{\frac{2 \varepsilon_{s} \varphi_{i}}{q N_{D}}}
\tag{4}
$$

where, $\varepsilon_s$ is the dielectric constant, N$_D$ is the doping concentration of the Si epi-layer, and $\varphi_i$ is the build-in potential around the depletion region and given by:

$$
\varphi_{i}=\varphi_{B}-V_{t} L n\left(\frac{N_{C}}{N_{D}}\right)
\tag{5}
$$

where, V$_t$ is the thermal voltage (0.026 V), N$_C$ is the effective density of states in the conduction band of semiconductor, and $\varphi_B$ is the barrier height, which can be expressed according to the $\varphi_M$ (work function of the Schottky metal) and $\chi$ (electron affinity of semiconductor):

$$
\varphi_{B}=\varphi_{M}-\chi
\tag{6}
$$

![](./images/814528021691105280_3.jpg)

Fig. 3. Schematic view of the betavoltaic battery based on Schottky diode.

![](./images/814528021691105280_4.jpg)

Fig. 4. Carrier generation within silicon under irradiation of ⁶³Ni with activity of of 10 mCi for p-n structure.

### 2.3. The calculation of electron-hole generation

#### 2.3.1. P-n structure

High energy beta particles lose their energy through ionization and excitation processes (Knoll, 2000). Energy loss is given by the Bethe formula (Cheng et al., 2010):

$$
\frac{dE}{ds} = -\frac{78500}{E} \frac{Z\rho}{A} \ln\left( \frac{1.66E}{\varepsilon} \right) \tag{7}
$$

where, Z is the atomic number, A is the atomic weight, $\rho$ is the mass density, s is the distance from the entrance of the electron trajectory, E is the electron energy, $\varepsilon$ is the average energy for an EHP generation which is given by Eq. (8) (Klein, 1968).

$$
\varepsilon = 2.8E_g + 0.5 \tag{8}
$$

Eq. (7) is defined for mono-energy electrons, so for beta spectrum, MCNP4C as a general purpose three dimensional Monte Carlo code has been used for calculating the generation rate of electron hole pair (EHP) within the Si (Ghasemi Nejad et al., 2014).

By calculating the deposited energy within Si ($E_{dep}$) using

![](./images/814528021691105280_5.jpg)

Fig. 6. Short circuit current density ($J_{sc}$) versus doping concentration ($N_A$ and $N_D$).

![](./images/814528021691105280_6.jpg)

Fig. 5. a) Depletion region width (w) and b) minority carrier diffusion length ($L_p$ and $L_n$) versus doping concentration ($N_A$ and $N_D$).

![](./images/814528021691105280_7.jpg)

Fig. 7. Leakage current density ($J_0$) versus doping concentration ($N_A$ and $N_D$).

tally for electrons, the generation rate of EHPs based on p-n junction (in Fig. 2) has been obtained using Eq. (9):

$$
G(x)=\frac{E_{d e p}}{\varepsilon} \exp (-\alpha x)=G_{0} \exp (-\alpha x)
\tag{9}
$$

where, $G_0$ and $\alpha$ are the fitting parameters for generation rate derived from MCNP4C results. x is the distance from the entrance of the beta particle, and $\varepsilon$ was introduced in Eq. (8).

### 2.3.2. Schottky structure
For betavoltaic battery based on Schottky barrier diode (Fig. 3), the number of EHPs within Si under irradiation of $^{63}$Ni can be calculated by:

$$
N_{e-h}=\frac{E_{d e p}}{\varepsilon}
\tag{10}
$$

## 2.4. The calculation of short-circuit current density ($J_{SC}$) and leakage current density ($J_0$)

### 2.4.1. p-n structure
The analytical expression of $J_{SC}$ for a betavoltaic battery based on p-n diode can be obtained by solving the minority carrier diffusion equation in the emitter and base region. According to Fig. 2, the radiation-induced current densities in the emitter, base and depletion regions are given by (Sze and Ng, 2007):

$$
\begin{aligned}
J_{E}=-\left.q D_{p} \frac{d p_{n}}{d x}\right|_{x=x_{j}} & =\frac{G_{0} L_{p}}{a^{2} L_{p}^{2}-1} \\
& \times\left(\frac{\frac{S_{p} L_{p}}{D_{p}}+\alpha L_{p}-\exp \left(-\alpha x_{j}\right)\left[\frac{S_{p} L_{p}}{D_{p}} \cosh \left(\frac{x_{j}}{L_{p}}\right)+\sinh \left(\frac{x_{j}}{L_{p}}\right)\right]}{\left[\frac{S_{p} L_{p}}{D_{p}} \sinh \left(\frac{x_{j}}{L_{p}}\right)+\cosh \left(\frac{x_{j}}{L_{p}}\right)\right]}\right. \\
& \left.-\alpha L_{p} \exp \left(-\alpha x_{j}\right)\right)
\end{aligned}
\tag{11}
$$

![](./images/814528021691105280_8.jpg)

Fig. 8. a) Open-circuit voltage ($V_{OC}$) and b) Filling factor (FF) versus doping concentration ($N_A$ and $N_D$).

![](./images/814528021691105280_9.jpg)

Fig. 9. Conversion efficiency ($\eta$) versus doping concentration ($N_A$ and $N_D$).

<table>
<caption>Table 1<br>Specification of some common Schottky metals (Zhao et al., 2005; Qiao et al., 2011).</caption>
<thead>
<tr>
<th>Schottky metal</th>
<th>Ag</th>
<th>Al</th>
<th>Mo</th>
<th>Au</th>
<th>Ni</th>
</tr>
</thead>
<tbody>
<tr>
<td>Work function (eV)</td>
<td>4.25</td>
<td>4.28</td>
<td>4.6</td>
<td>5.1</td>
<td>5.15</td>
</tr>
<tr>
<td>Density (g cm⁻³)</td>
<td>10.5</td>
<td>2.7</td>
<td>2.10</td>
<td>19.3</td>
<td>8.9</td>
</tr>
</tbody>
</table>

![](./images/814528021691105280_10.jpg)

Fig. 10. Normalized flux as a function of Schottky metal thickness.

![](./images/814528021691105280_11.jpg)

Fig. 11. EHPs generation within silicon under illumination of 63Ni for Ni/Si Schottky barrier structure.

![](./images/814528021691105280_12.jpg)

Fig. 12. a) Hole diffusion length (Lp) and b) Depletion region width (w) versus epi-layer doping concentration (ND).

<table>
<caption>Table 2
Calculated parameters of the betavoltaic battery based on Ni/Si Schottky barrier diode.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>φ (mCi/cm²)</td>
<td>10</td>
<td>–</td>
</tr>
<tr>
<td>S (cm²)</td>
<td>1</td>
<td>–</td>
</tr>
<tr>
<td>A*(A cm⁻² K⁻²)</td>
<td>110</td>
<td>(Lutz, 2007)</td>
</tr>
<tr>
<td>n</td>
<td>1</td>
<td>–</td>
</tr>
<tr>
<td>Nc (#/cm³)</td>
<td>2.8e19</td>
<td>(Lutz, 2007)</td>
</tr>
<tr>
<td>ε (eV)</td>
<td>3.64</td>
<td>(XiaoBin et al., 2012)</td>
</tr>
<tr>
<td>εₛ</td>
<td>11.8</td>
<td>(Neudeck, 1989)</td>
</tr>
<tr>
<td>L (μm)</td>
<td>11</td>
<td>–</td>
</tr>
<tr>
<td>φₘ (eV)</td>
<td>5.15</td>
<td>(Qiao et al., 2011)</td>
</tr>
<tr>
<td>χ (eV)</td>
<td>4.05</td>
<td>–</td>
</tr>
</tbody>
</table>

$$
\begin{aligned}
J_{B}=\left.q D_{n} \frac{d n_{p}}{d x}\right|_{x=x_{j}+w} &=\frac{G_{0} L_{n}}{a^{2} L_{n}^{2}-1} \exp \left(-\alpha\left(x_{j}+w\right)\right) \\
& \times\left(a L_{n}-\frac{\frac{S n L_{n}}{D_{n}}\left[\cosh \left(\frac{h}{L_{n}}\right)-\exp (-\alpha h)\right]+\sinh \left(\frac{h}{L_{n}}\right)+a L_{n} \exp (-\alpha h)}{\left[\frac{S n L_{n}}{D_{n}} \sinh \left(\frac{h}{L_{n}}\right)+\cosh \left(\frac{h}{L_{n}}\right)\right]}\right)
\end{aligned} \tag{12}
$$

$$
J_{D}=q \int_{x_{j}}^{x_{j}+w} G(x) d x=\frac{G_{0}}{\alpha} e^{-\alpha x_{j}}\left(1-e^{-\alpha w}\right) \tag{13}
$$

where, D is the carrier diffusion coefficient and S is the surface recombination velocity of the carriers.

Thus, $J_{SC}$ can be calculated from the sum of $J_E$, $J_B$, and $J_D$:

$$
J_{S C}=J_{E}+J_{B}+J_{D} \tag{14}
$$

Also, $J_0$ is expressed as follows (Wu et al., 2011):

$$
\begin{aligned}
J_{0}=& q \frac{n_{i}^{2}}{N_{D}} \frac{D_{p}}{L_{p}}\left(\frac{\frac{D_{p}}{L_{p}} \sinh \left(\frac{x_{j}}{L_{p}}\right)+S_{p} \cosh \left(\frac{x_{j}}{L_{p}}\right)}{\frac{D_{p}}{L_{p}} \cosh \left(\frac{x_{j}}{L_{p}}\right)+S_{p} \sinh \left(\frac{x_{j}}{L_{p}}\right)}\right) \\
&+q \frac{S n_{i}^{2}}{N_{A}} \frac{D_{n}}{L_{n}}\left(\frac{\frac{D_{n}}{L_{n}} \sinh \left(\frac{h}{L_{n}}\right)+S_{n} \cosh \left(\frac{h}{L_{n}}\right)}{\frac{D_{n}}{L_{n}} \cosh \left(\frac{h}{L_{n}}\right)+S_{n} \sinh \left(\frac{h}{L_{n}}\right)}\right)
\end{aligned} \tag{15}
$$

where, $n_i$ is the intrinsic carrier concentration which is obtained from the following equation according to the effective density of the valence band of semiconductor ($N_v$):

![](./images/814528021691105280_13.jpg)

Fig. 13. a) Short-circuit current density (Jsc), b) Open-circuit voltage (Voc), c) Filling. factor (FF), and d) Conversion efficiency (η) versus epi-layer doping concentration (ND).

$$
n_{i}=\sqrt{N_{C} N_{V}} \exp \left(\frac{-E_{g}}{k T}\right)
$$

(16)

### 2.4.2. Schottky structure
For Schottky barrier structure (Fig. 3), the radiation-induced current densities in the depletion and n-type regions are given by (Qiao et al., 2011):

$$
J_{D}=\varphi q N_{e-h}\left(1-\exp \left(-w / L_{a}\right)\right)
$$

(17)

$$
\begin{aligned}
J_{N}= & \varphi q N_{e-h}\left(\frac{L_{p} L_{a}}{L_{a}{ }^{2}-L_{p}{ }^{2}} ×\left[\operatorname{coth}\left(\frac{L-w}{L_{p}}\right)-\frac{L_{p}}{L_{a}}\right] × \exp \left(-w / L_{a}\right)\right. \\
& \left.-\frac{\exp \left(-L / L_{a}\right)}{\sinh \left(\frac{L-w}{L_{p}}\right)}\right)
\end{aligned}
$$

(18)

where, $\varphi$ is the activity of isotope, $L_{a}$ is the stopping range of the beta particle, and L is the thickness of active region.

Thus, $J_{S C}$ can be approximated as:

$$
J_{S C}=J_{N}+J_{D}
$$

(19)

Also, $J_{0}$ is expressed as follows (Li et al., 2011):

$$
J_{0}=A^{*} T^{2} \exp \left(-\frac{q \varphi_{B}}{n k T}\right)
$$

(20)

<table>
<caption>Table 3 Optimized parameters of betavoltaic batteries based on Si p-n structure and Ni/Si Schottky barrier structure.</caption>
<tbody>
<tr>
<td rowspan="4">p-n structure</td>
<td>Doping concentration in emitter region ($N_D$)</td>
<td>1e19 #/cm³</td>
</tr>
<tr>
<td>Doping concentration in base region ($N_A$)</td>
<td>1e17 #/cm³</td>
</tr>
<tr>
<td>Junction depth ($x_j$)</td>
<td>0.1 μm</td>
</tr>
<tr>
<td>Thickness of p-type region ( ≈ h)</td>
<td>400 μm</td>
</tr>
<tr>
<td rowspan="5">Schottky structure</td>
<td>Thickness of Schottky metal (Ni)</td>
<td>0.1 μm</td>
</tr>
<tr>
<td>Doping concentration in N-type epi-layer ($N_D$)</td>
<td>1e13 #/cm³</td>
</tr>
<tr>
<td>Thickness of N-type epi-layer (L)</td>
<td>11 μm</td>
</tr>
<tr>
<td>Substrate</td>
<td>400 μm</td>
</tr>
</tbody>
</table>

where, $A^{*}$ is the effective Richardson constant.

### 2.5. Open-circuit voltage ($V_{OC}$) and conversion efficiency ($\eta$)
For a betavoltaic battery $V_{OC}$ and $\eta$ are given by following equations:

$$
V_{o c}=\frac{n k T}{q} \ln \left(1+\frac{J_{s c}}{J_{0}}\right)
$$

(21)

$$
\eta(\%)=\frac{F F × V_{o c} × I_{s c}}{P_{i n}} × 100
$$

(22)

where, n is an ideal factor, $P_{in}$ refers to the incident power density of radioisotope source, and FF is the fill factor calculated by (XiaoBin et al., 2012):

$$
FF = \frac{\left(\frac{q}{nkT}V_{oc}\right) - Ln\left(\frac{q}{nkT}V_{oc} + 0.72\right)}{\frac{q}{nkT}V_{oc} + 1}
\tag{23}
$$

## 3. Results and discussion

### 3.1. Betavoltaic battery based on Si p-n junction

The performance of the betavoltaic battery based on p-n junction (according to Eqs. (11)-(13) affected by the generation rate of EHPs within Si (G(x)), junction depth ($x_j$), depletion region width (w), and minority carrier diffusion length in the emitter and base regions ($L_p$ and $L_n$), so to achieve higher conversion efficiency, these parameters should be optimized.

Fig. 4 shows the generation rate of EHPs within Si under irradiation of 10 mCi of $^{63}$Ni. According to the results of energy deposition in Si, $G_0$ and $\alpha$ (in Eqs. (11)-(13) have been calculated equal to $3.7 \times 10^{15}\#\ \text{cm}^{-3}\text{ s}$ and $3697\ \text{cm}^{-1}$, respectively.

Due to internal field of the p-n junction, probability of electron-hole collection for carriers generated inside the depletion region is about 100% (XiaoBin et al., 2012). As shown in Fig. 4, by increasing the depth, deposited energy in the device will be decreased, so it is desirable to reduce the junction depth as much as possible. So the maximum conversion efficiency can be obtained with the junction depth of $0.1\ \mu\text{m}$.

Also, the doping concentrations in the emitter and base regions ($N_D$ and $N_A$) should be optimized to obtain high conversion efficiency, because these parameters have direct influence on the depletion region width and minority carrier diffusion length. The dependence of these parameters on $N_A$ and $N_D$ is shown in Fig. 5. According to Fig. 5, the depletion region width and minority carrier diffusion lengths decrease with increasing in $N_D$ and $N_A$. Thus, $J_{SC}$ decreases with increasing in $N_A$ and $N_D$.

Also, Fig. 6 shows the result for $J_{SC}$ versus doping concentrations at 300 K with a junction depth of $0.1\ \mu\text{m}$ and a base thickness of $400\ \mu\text{m}$. As seen in Fig. 6 the maximum obtainable value of $J_{SC}$ is about $160\ \text{nA cm}^{-2}$.

According to Eq. (21), $V_{OC}$ is determined by $J_{SC}$ and $J_0$. The dependence of $J_0$ on $N_A$ and $N_D$ can be determined according to Eq. (15), which is shown in Fig. 7. It can be seen that $J_0$ decreases by increasing the $N_A$ and $N_D$.

Fig. 8 shows the dependence of $V_{OC}$ and FF on $N_A$ and $N_D$ which increases with decreasing $J_0$. Also, the maximum obtainable value of $V_{OC}$ is about 0.38 V.

Ultimately, the conversion efficiency of the betavoltaic battery based on p-n junction is shown in Fig. 9. It can be seen that under irradiation of $^{63}$Ni with activity of 10 mCi, the maximum efficiency (3.17%) will be achieved when $N_A \approx 1 \times 10^{17}\ \#\ \text{cm}^{-3}$ and $N_D \approx 1 \times 10^{19}\ \#\ \text{cm}^{-3}$ and the related values for $J_{SC}$, $V_{OC}$ and FF can be obtained $157\ \text{nA cm}^{-2}$, 0.35 V and 0.75, respectively.

### 3.2. Betavoltaic battery based on Ni/Si Schottky barrier structure

According to Eq. (17) and (18), the performance of the Schottky barrier based betavoltaic battery is affected by the Schottky metal, number of generated EHPs ($N_{e-h}$), stopping range of the beta particles ($L_a$), depletion width (w), and minority carrier diffusion length in the n-type epi-layer ($L_p$). So, higher conversion efficiency can be obtained by optimization of these parameters.

According to Section 2, $V_{OC}$ is strongly depends on the work function of the Schottky metal. Therefore metals with large work functions should be selected as the Schottky metal. Table 1 shows some common Schottky metals. It is obvious that Ni and Au due to their higher work functions are the good options for this purpose.

But as shown in Fig. 10, Au due to its high atomic number as well as high density attenuates large number of beta particles. So Ni was chosen to form the schottky junction. On the other hand, due to self-absorption of beta particles in the Schottky metal, the thickness of Ni should be as small as possible. Thus, Ni with thickness of 100 nm has been selected as the Schottky metal.

Calculation of the number of generated EHPs and stopping range of beta particle within Si ($L_a$) have been determined using the energy deposition of the beta particles in Si. Fig. 11 shows the number of generated EHPs within Si.

As shown in Fig. 11, the number of generated EHPs by one beta particle within Si is about 2200. Also, more than 95% of the total energy of beta particle is deposited in the region with depth less than $9.5\ \mu\text{m}$, so this thickness has been considered as the stopping range of beta particle from $^{63}$Ni within Si.

Fig. 12 shows the dependence of depletion region width and minority carrier diffusion length on $N_D$. It can be seen that $L_p$ and w decrease with increasing the $N_D$. It should be mentioned that w is about $9.5\ \mu\text{m}$, when $N_D$ is about $1 \times 10^{13}\ \#\ \text{cm}^{-3}$.

Table 2 shows the specification of Ni/Si Schottky barrier structure and Fig. 13 shows the electrical performance of the betavoltaic battery under irradiation of $^{63}$Ni (with activity of 10 mCi per $\text{cm}^2$).

According to Fig. 13, the performance of battery decreased with increasing the $N_D$. On the other hand, the highest efficiency of betavoltaic conversion will be achieved with depletion width equal the stopping range of beta particles within Si, because the electron-hole collection probability is equal 100% for carriers generated inside the depletion region. For the depletion width equal to $9.5\ \mu\text{m}$ (equivalent to $N_D \approx 1 \times 10^{13}\ \#\ \text{cm}^{-3}$), $J_{SC}$, $V_{OC}$, FF, and $\eta$ have been calculated $86.6\ \text{nA cm}^{-2}$, 0.26 V, 0.69, and 1.18%, respectively.

Ultimately, Table 3 shows the comparison of optimized parameters in Si p-n junction and Ni/Si Schottky barrier diode as a betavoltaic battery.

## 4. Conclusion

In this paper, two types of betavoltaic batteries based on p-n and Schottky structures were studied. These batteries were designed using Si and $^{63}$Ni as the semiconductor material and radiation source, respectively. Some parameters with more effect on efficiency have been optimized.

In Si p-n junction type, the maximum efficiency equal to 3.17% will be achieved when $N_A \approx 1 \times 10^{17}\ \#\ \text{cm}^{-3}$ and $N_D \approx 1\text{×}10^{19}\ \#\ \text{cm}^{-3}$. The related values of $J_{SC}$, $V_{OC}$ and FF can be obtained $157\ \text{nA cm}^{-2}$, 0.35 V and 0.75, respectively.

In Ni/Si Schottky barrier type, for the depletion width equal to $9.5\ \mu\text{m}$ ($N_D \approx 1 \times 10^{13}\#\ \text{cm}^{-3}$), $J_{SC}$, $V_{OC}$, FF, and $\eta$ have been calculated $86.6\ \text{nA cm}^{-2}$, 0.26 V, 0.69, and 1.18%, respectively.

The results show that the performance of the batteries strongly depends on the doping concentration and betavoltaic battery based on Si p-n structure has better performance (about 2.7 times higher) than Ni/Si Schottky barrier structure.

## References

Chandrashekhar, M.V.S., 2007. Demonstration of a 4H SiC Betavoltaic Cell. 25. Cornell University.

Cheng Z., et al., 2010. The design optimization for GaN-based betavoltaic micro-battery. In: Proceedings of the 5th IEEE International Conference on Nano/Micro Engineered and Molecular System, pp. 582-586.

Ghasemi Nejad, G.R., et al., 2014. Design and optimization of beta-cell temperature sensor based on 63Ni-Si. J. Appl. Radiat. Isot. 86, 46-51.

Ghasemi Nejad, G.R., Rahmani, F., 2016. Design and simulation of betavoltaic angle sensor based on 63Ni-Si. J. Appl. Radiat. Isot. 107, 346-352.

Guo, H., et al., 2011. Fabrication of SiC p-i-n betavoltaic cell with 63Ni irradiation source. In: Proceedings of the International Conference of Electron Devices and Solid-State. IEEE, Tianjin.

Honsberg C., et al., 2005. GaN betavoltaic energy converters. In Proceedings of the 31st IEEE Photovoltaics Specialist Conference, pp. 3–7.

Klein, C.A., 1968. Bandgap dependence and related features of radiation ionization energies in semiconductors. J. Appl. Phys. 39 (4), 2029–2038.

Knoll, G.F., 2000. Radiation Detection and Measurement, 3rd ed. John Wiley & Sons, p. 44.

Lei, Y., et al., 2014. The radiation damage of crystalline silicon PN diode in tritium beta-voltaic battery. J. Appl. Radiat. Isot. 90, 165–169.

Li, D.-R., et al., 2012. Betavoltaic battery conversion efficiency improvement based on interlayer structures. J. Chin. Phys. Lett. 29 (7), 0781021–0781024.

Li, H., et al., 2012. Simulations about self-absorption of tritium in titanium tritide and the energy deposition in a silicon Schottky barrier diode. J. Appl. Radiat. Isot. 70, 2559–2563.

Li, X.-Y., et al., 2011. 63Ni schottky barrier nuclear battery of 4H–SiC. J. Radioanal. Nucl. Chem. 287, 173–176.

Liu, Y., et al., 2012. Investigation on a radiation tolerant betavoltaic battery based on Schottky barrier diode. J. Appl. Radiat. Isot. 70, 438–441.

Lu, M., et al., 2011. Gallium nitride schottky betavoltaic nuclear batteries. J. Energy Convers. Manag. 52, 1955–1958.

Lutz, G., 2007. Semiconductor Radiation Detectors. 1999. Springer-Verlag,. Berlin Heidelberg, pp. 59–80.

Neudeck, G.W., 1989. The PN Junction Diode. Addison-Wesley, p. 34.

Olsen L.C., 1993. Review of betavoltaic energy conversion. In: Proceedings of the NASA Conference Publication, NASA.

Qiao, D.-Y., et al., 2011. A micro nuclear battery based on SiC schottky barrier diode. J. Microelectromech. Syst. 20 (3), 685–690.

San, H., et al., 2013. Design and simulation of GaN based schottky betavoltaic nuclear micro-battery. J. Appl. Radiat. Isot. 80, 17–22.

Sze, S., Ng, M.K., 2007. Physics of Semiconductor Devices, 3rd ed. John Wiley & Sons, pp. 720–727.

Wu K., et al., 2011. A theoretical study on silicon betavoltaics using Ni-63. In: Proceedings of the 6th IEEE International Conference on Nano/Micro Engineered and Molecular Systems, pp. 724–727.

XiaoBin, T., et al., 2012. Optimization design and analysis of Si-⁶³Ni betavoltaic battery. J. Sci. China Technol. Sci. 55 (4), 990–996.

Yao, S., et al., 2012. Design and simulation of betavoltaic battery using large-grain polysilicon. J. Appl. Radiat. Isot. 70, 2388–2394.

Zhao, J.H., 2005. Silicon carbide schottky barrier diode. J. High Speed Electron. Syst.

ZUO, G., et al., 2013. A simple theoretical model for 63Ni betavoltaic battery. J. Appl. Radiat. Isot. 82, 119–125.