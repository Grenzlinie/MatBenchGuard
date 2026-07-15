![](./images/812409782697721859_1.jpg)

Measurement 181 (2021) 109504

Contents lists available at ScienceDirect

# Measurement

journal homepage: www.elsevier.com/locate/measurement

![](./images/812409782697721859_2.jpg)

![](./images/812409782697721859_3.jpg)

# Temperature effects on surface plasmon resonance sensor based on side-polished D-shaped photonic crystal fiber

Wei Luo $^{a,b,1}$, Jinwei Meng $^{c,d,1}$, Xuejin Li $^{a,b,c,d,*}$, Qingli Xie $^{c,d}$, Duo Yi $^{c,d}$, Yanyong Wang $^{c,d}$, Xueming Hong $^{c,d}$

$^{a}$ The Chinese University of Hong Kong (Shenzhen), Shenzhen 518172, China
$^{b}$ University of Science and Technology of China, Hefei 231500, China
$^{c}$ Shenzhen Key Laboratory of Sensor Technology, Shenzhen 518060, China
$^{d}$ Shenzhen Engineering Laboratory for Optical Fiber Sensor and Networks, Shenzhen 518060, China

---

## ARTICLE INFO

**Keywords:**
Surface plasmon resonance sensor
Temperature effect
Side-polished D-shaped
Photonic crystal fiber
Optical fiber sensor

## ABSTRACT

A comprehensive temperature Drude theoretical mode has been established to study the temperature effects on the side-polished photonic crystal fiber (PCF) surface plasmon resonance (SPR) sensor. In the theoretical model, the temperature dependence coefficients of fiber material refractive index (RI), sensing film thickness and metal-dielectric function have been considered. The finite element method (FEM) is used to study the influence of side-polished depth, metal thickness, air hole size, and lattice constant on sensing performance with findings as following: (1) the dependence of the resonance wavelength on temperature is almost unaffected by duty ratio or lattice pitch of PCF; (2) the peak loss of the PCF SPR sensor with small lattice pitch (or increased duty ratio) is more sensitive to temperature variation; (3) for the sensor working in intensity interrogation mode, linear relationships can be found between the peak loss versus the RI and temperature. Moreover, we fabricate a side-polished D-shaped PCF SPR sensor by a wheel polishing setup, and the experimental results display a good agreement with the theoretical investigations. This study offers a detailed way to analyze the temperature effects on the sensor, and may lead to the better design and the data-progress improvement for D-shaped PCF SPR sensor.

---

## 1. Introduction

Surface plasmon resonance (SPR) is an optical-sensing technique that uses evanescent wave to sense. Due to its unique advantages of high sensitivity, real-time and label-free detection, SPR sensor has become as one of the most important methods applied in chemical, biological sensing and so on [1-3]. With photonic crystal fiber' (PCF') fiber's large flexible design of microstructures, anti-electromagnetic interference, remote sensing capability and in situ-monitoring, the PCF SPR sensor offers so many advantages over traditional SPR sensors, and has attracted immense research interest worldwide [4-6]. Since the sensing mechanism of the SPR based sensor is to couple the electromagnetic waves with free electron density oscillations on the metal-dielectric surface, parts of the PCFs' micro air holes are chosen as the sensing channel filled with analyte, and vapor metal film in the inner surface of the holes. In addition to the various theoretically designed PCF SPR sensor, the progress in experimental research has been investigated. Sazio et al. [7] and Zhang's [8] group successfully deposited the sensing layers on the inner surface of PCF cladding air holes with chemical deposition technique. Besides, the method of filling silver nanowires into the cladding holes or fiber core has been used to excite the SPR in Wong's and Lu's researches [9,10]. Because the holes of PCF are only a few microns, it is difficult to fill materials and to deposit the sensing layers inside these micron holes.

Recent studies have shown that a D-shape or exposed-core side-leakage PCFs can overcome the difficulties of metal coating. With the exposed core to be coated directly with metal film, it offers a convenient way for fabrication, and also for the phase-matching problem between core-guided mode and surface plasmon polariton (SPP) mode. In order to achieve a side-leakage PCF, Kim's group [11] fabricated the fiber in a curved V-groove and coated a photoresist long-period grating on the side-polished surface obtaining a refractive index (RI) sensor. In 2019,

---

* Corresponding author at: School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen), Shenzhen, 518172, China.
E-mail addresses: luoweivip@ustc.edu.cn (W. Luo), lixuejin@szu.edu.cn (X. Li).
$^{1}$ These authors contributed equally to this work and should be considered co-first authors.

https://doi.org/10.1016/j.measurement.2021.109504
Received 4 February 2021; Received in revised form 14 April 2021; Accepted 27 April 2021
Available online 15 May 2021
0263-2241/© 2021 Elsevier Ltd. All rights reserved.

Wang et al. proposed a D-type multimode fiber based symmetrical long range (LR) SPR sensor with quality factor (Q-F) as high as 107.52 RIU⁻¹ [12]. In 2020, a D-shaped fiber based LRSPR sensor with high Q-factor of 67.75 RIU⁻¹ and temperature self-compensation was proposed and demonstrated by his team [13]. Similarly, Chen and Luo's group presented a long-range SPR sensor based on side-polished D-shaped multimode fiber for biosensing application [14]. In 2018, Wang et al. proposed a D-shaped fiber sensor. The sensitivity can reach 44567 nm-RIU⁻¹ theoretically and 22779 nm-RIU⁻¹ experimentally for RI equals to 1.3350, respectively [15]. For the PCF, they studied the sensor property of the side-polished D-shaped PCF SPR sensor with tuning hole size, lattice pitch and fiber material RI. The experiment is taken out with the sensor fabricated by a wheel polishing setup [16]. Previously, our group have also studied the side-polished D-shaped PCF SPR sensor, theoretically and experimentally. With the sensor being used in intensity interrogation mode, a two-feature detection method is presented to improve the resolution. In addition, the effects of side-polishing length have also been studied experimentally [17,18]. For the convenient manufacture and application of the side-polished D-shaped PCF SPR sensor, the sensing may be taken out at different temperature environments. During the detection, ambient temperature fluctuation may affect the performances. This is mainly due to the temperature dependence changes of electronic components, photo-absorption effect and opto-mechanical displacements [19-21]. Therefore, it is thus of interest to investigate the temperature effects on the side-polished D-shaped PCF SPR sensor performance.

In present work, we have theoretically studied the temperature impacts on the sensing property of side-polished D-shaped PCF SPR sensor. The total internal reflection (TIR) PCF is constructed with a solid core surrounded with hexagon arranged air holes. In the theoretical model, the dispersions of fiber material have been considered in addition to the temperature dependence of sensing film thickness and metal-dielectric function. The resonance spectra and the coupling property between y-polarized fundamental core mode and SPP mode are numerically presented for different side-polished depths, meal thicknesses, duty ratios and lattice pitches. For the sensor working in intensity interrogation mode, the dependence of the peak loss of y-polarized core mode on RI and temperature has also been investigated. Furthermore, we fabricate a side-polished D-shaped PCF SPR sensor with a wheel polishing setup. A proof-of-concept experiment was carried out to have a comparative analysis with theoretical simulation.

## 2. Structure design and basic theory

The figural presentation of PCF is a simple and straightforward design. Based on the commercial PCF ESM-12 (produced by NKT Inc.), the schematic geometry of the PCF SPR sensor is depicted in Fig. 1. There are six-layer air holes arranged in a hexagon arrangement constructed the cladding. The upper side of the PCF is polished with a polishing depth of h, which is defined as the distance from the fiber core to the polished surface. The lattice pitch $\Lambda$ and air hole diameter $d$ are 7.9 μm and 3.9 μm, respectively. After the side polishing to obtain an exposed core, nanometer-thickness gold film is coated on the polished surface. Surface plasmon wave (SPW) is the resonance oscillation of conducting electrons or negative charged ions at the interface boundary of negative and positive permittivity material. One of the most important condition to generate the SPW is that the metal film is sufficiently thin. When the light travels to the polish-grinding region, the transmission mode would leak from the polished D-shaped opening surface. In this way, the evanescent wave is formed and travels through the thin metal medium, and excites SPR while satisfying the phase matching condition. Therefore, the multiple effects of temperature on the PCF SPR sensor can be transformed into the physical parameter of these constituent units, including the silica refractive index, dielectric constant of gold film and its thickness.

Since the temperature variation could cause the changes of PCF SPR sensor components, it may lead to the change of the phase-matching condition between the core-guide mode and plasmonic mode. In our design, we consider that the PCF fiber is made of fused silica, and according to the Sellmeier equation [22], the temperature dependence on the refractive index of fused silica can be calculated as:

$$
\begin{aligned}
n_{\text{silica}}^{2} &=1.31552+0.690754 × 10^{-5} T \\
+& \frac{\left(0.788404+0.235835 × 10^{-4} T\right) \lambda^{2}}{\lambda^{2}-\left(0.0110199+0.584758 × 10^{-6} T\right)} \\
+& \frac{\left(0.91316+0.548368 × 10^{-6} T\right) \lambda^{2}}{\lambda^{2}-100}
\end{aligned} \tag{1}
$$

where $\lambda$ is the wavelength of light in μm, and $T$ is the temperature in degree centigrade. The dielectric constant of the sensor gold film can be described by Drude model [23,24] as:

$$
\varepsilon(\omega)=\varepsilon_{1}+i \varepsilon_{2}=\varepsilon_{\infty}-\frac{\omega_{p}^{2}}{\omega\left(\omega+i \omega_{c}\right)} \tag{2}
$$

Here, $\varepsilon_{\infty}$ is the dielectric constant of gold at high frequency. $\omega$ is the angular frequency of the electromagnetic wave. $\omega_{\mathrm{p}}$ and $\omega_{\mathrm{c}}$ represent the plasma and collision frequency of the metallic electrons, respectively.

Due to the volumetric effects [25], the plasma frequency can be written as

$$
\omega_{p}=\omega_{p 0} \exp \left(-\frac{T-T_{0}}{2} × 3 \gamma\right) \tag{3}
$$

$\omega_{\mathrm{p} 0}$ is the plasma frequency at $T_{0}$. $r$ is the volumetric thermal expansion coefficient of gold.

The temperature dependence of collision frequency is determined by two factors: phonon-electron scattering ($\omega_{\text {ep}}$) and electron-electron scattering ($\omega_{\text {ce}}$) [26], and the combined effect of the two is

$$
\omega_{c}=\omega_{c e}+\omega_{c p} \tag{4}
$$

![](./images/812409782697721859_4.jpg)

Fig. 1. (a) Cross-section of the D-shaped PCF SPR sensor based on ESM-12. (b) Schematic diagram of mode coupling between the SPW and core-guided transmission mode.

Electron scattering can be modeled by the Lawrence's electron scattering model [27]:

$$
\omega_{c e}(T)=\frac{1}{6} \pi^{4} \frac{\Gamma \Delta}{\hbar E_{F}}\left[\left(K_{B} T\right)^{2}+\left(\frac{\hbar \omega}{4 \pi^{2}}\right)^{2}\right]
\tag{5}
$$

where h, $E_F$ and $K_B$ represent the Planck's constant, Fermi energy of the metal electrons and Boltzmann constant, respectively. Besides, according to the Holstein's phonon-electron scattering model [28,29], the phonon-electron scattering can be calculated as:

$$
\omega_{c p}(T)=\omega_{p}\left(T_{0}\right)\left[\frac{2}{5}+4\left(\frac{T}{T_{D}}\right)^{5} \int_{0}^{T_{D} / T} \frac{z^{4} d z}{e^{z}-1}\right]
\tag{6}
$$

with the $T_D$ as Debye temperature.

We also analyze the effect of temperature variation on the thickness of sensing layer. Here, $d_0$ denotes the thickness of gold film at room temperature 298 K. With a corrected thermal expansion coefficient [30], temperature dependence metal thickness is given by

$$
d_{A u}=d_{0}\left[1+\gamma \frac{1+\mu}{1-\mu}\left(T-T_{0}\right)\right]
\tag{7}
$$

$\mu$ is Poisson's number of the film material. The values of the parameters used in our calculation are listed in Table 1. Since the silver layer can also be applied as the metal layer and has the similar situation with Au film, the parameters for silver layer are also listed in the table within brackets [31].

## 3. FEM calculation and analysis

Full-vectorial finite element method (FEM) solver is used with cylindrical perfectly matched layer (PML) condition to find the complex propagation constants of the y-polarized core guided mode and SPP mode. The simulation is carried out by commercial software COMSOL Multiphysics, and the confinement loss is defined as [32]

$$
Loss(d B / c m)=8.686 \times \frac{2 \pi}{\lambda} \operatorname{Im}\left(n_{e f f}\right)
\tag{8}
$$

where $\lambda$ is the wavelength in centimeter scale.

With setting coefficients $\Lambda=7.9 \mu \mathrm{m}, d / \Lambda=0.5, h=0.5 \Lambda$, and analyte RI being 1.35, the dispersion of y-polarized fundamental core mode and SPP mode, and the confinement loss are illustrated in Fig. 2. As the blue lines show the detection situation of 270 K, the confinement loss rises first and then decreases. An intersection appears between the dispersion relationship of core guided mode and plasmonic mode, where the two modes meet the phase matching condition. Parts of the core guided energy transfer to metal surface generating the plasma oscillations. The detailed observation shows that the increase of temperature makes the dispersions of both the core mode and SPP mode moving upward, and the intersection performs a slight blue-shift in x-axis wavelength. Due to the reaction of plasma oscillations to the leakage core mode, the wavelength, where the confinement loss of y-polarized fundamental mode reaches a loss peak, exhibits a red-shift from the dispersion intersection [33]. Due to the SPR sensing principle to detect the transfer spectrum in the fiber, the wavelength corresponding to the loss peak is observed as the resonance wavelength. Therefore, with the temperature increasing, the resonance wavelength exhibits a slight increase.

When temperature increases to 370 K, the loss spectrum goes down and widens, and the peak loss decreases from 26.3 to 19.5 dB/cm. The detailed distributions of optical field of y-polarized core mode at the resonances are shown as inserted figures a and b for 270 and 370 K, respectively. The arrows represent the direction of electric field. Comparing between the inset a and b, it shows clearly that, at higher temperature, the SPP mode distribution at the boundary of the metal and analyte is much more obvious. The explanation for this phenomenon is that, the surface plasma oscillations, propagating at the boundary, is enhanced with an increase temperature.

### 3.1. Polishing depth and metal thickness effect

For the PCF SPR sensor presented in our study, polishing is the innovative approach to couple the core guided fundamental mode with SPP mode. To determine the impact of the polishing depth on the sensor's temperature dependence, we calculate the loss spectra at different polishing depths from $0.1 \Lambda$ to $0.9 \Lambda$ at intervals of $0.2 \Lambda$. For liquid analyte melting and boiling point, the temperature range is set from 270 to 320 and 370 K in the simulation.

The loss spectra of the y-polarized core guided mode for different polishing depths are illustrated in Fig. 3(a). As the figure shows, with the polishing depth decreasing from $0.7 \Lambda$ to $0.1 \Lambda$ and the polished flat surface becoming closer to the core, the coupling strength between the y-polarized core mode and SPP mode has been rapidly enhanced, and the peak loss increases significantly. At the depth of $0.9 \Lambda$ and due to the plasma oscillations supported by the polished inner surfaces of cladding air holes, the resonance wavelength performs a blue-shift [34]. When the temperature changes, the position of the resonance wavelength is almost unchanged for a certain polishing depth. However, when the temperature increases, the coupling efficiency becomes weak, and the peak loss of the y-polarized core mode decreases gradually. The detailed values of the peak loss are listed in Table 2. It shows clearly that, with the same temperature variation, the peak loss changes more at a deeper polishing depth, which implies the polished D-shaped SPR sensor, with the flat surface closer to the fiber core, is more sensitive to temperature. As a trade-off with fabrication reality, the polish depth is set to be $0.5 \Lambda$ in the following calculation.

Fig. 3(b) depicts the loss spectra at the temperature of 270, 320 and 370 K with different gold layer thicknesses. When the thickness increases from 35 to 55 nm, the resonance moves to a longer wavelength. This is mainly due to the increase of surface gap between the polished plane and plasma oscillation surface, which leads to the core light not easy to couple with the SPP mode and alters the phase matching condition to a long wavelength range. It also reveals that, with a thinner gold film, the resonance spectrum has a narrower bandwidth and higher confinement loss. In general, it also enables the sensor with higher sensing resolution and better signal-to-noise-ratio. Moreover, with the same temperature increase, the sensor with thinner metal film performs an enhanced decrease in the peak loss. Herein, we set the metal film to be 35 nm in the following simulation to have a better show of temperature influence.

### 3.2. Duty ratio and lattice pitch variation

With the lattice pitch $\Lambda$ of the PCF set to be $7.9 \mu \mathrm{m}$, polishing depth h being $0.5 \Lambda$ and analyte RI fixed at 1.35, the resonance wavelength and the peak loss of the spectrum for different duty ratios are shown in Fig. 4(a). With the increase of duty ratio, the peak loss rises rapidly. Simultaneously, the variation of the resonance wavelength is insignificant, which indicates that the relationship governing the resonance variation versus temperature change is approximately independent of the duty ratio (without considering the extreme ratio situation of 0.2). Moreover, for the no-linear rising of peak loss lines and observing the increasing space between these curves, it reveals that the peak loss of PCF SPR

<table>
<caption>Table 1<br>Parameters of gold and silver layer used in the number calculation.</caption>
<thead>
<tr>
<th>Parameters</th>
<th>Value</th>
<th>Parameters</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Delta$</td>
<td>0.77 (0.73)</td>
<td>$T_D$</td>
<td>185 (215) K</td>
</tr>
<tr>
<td>$\Gamma$</td>
<td>0.55</td>
<td>$E_F$</td>
<td>5.51 (5.48) eV</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>$1.42\ (1.89)\times10^{-5}\ \text{K}^{-1}$</td>
<td>$M$</td>
<td>0.44 (0.37)</td>
</tr>
<tr>
<td>$K_B$</td>
<td>$1.38\times10^{-23}\ \text{J/K}$</td>
<td></td>
<td>$6.626\times10^{-34}\ \text{Js}$</td>
</tr>
</tbody>
</table>


![](./images/812409782697721859_5.jpg)

Fig. 2. Dispersion relations and resonance loss spectra for temperatures of 270 K (blue lines) and 370 K (red lines). Dashed lines represent the two SPP modes. Inserted figure a and b show the optical field distributions at the resonance for 270 and 370 K, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/812409782697721859_6.jpg)

Fig. 3. $\Lambda = 7.9\ \mu$m, $d/\Lambda = 0.5$, $n_a = 1.35$ RIU. (a) Loss spectra of the D-shaped PCF SPR sensor at different temperatures of 270, 320 and 370 K with polish depth of $0.1\Lambda$, $0.3\Lambda$, $0.7\Lambda$ and $0.9\Lambda$. (b) Loss spectra at different temperatures with gold layer thickness of 35, 45 and 55 nm.

Table 2
The peak loss value of y-polarized core mode at different temperatures and polish depths.

<table>
<thead>
<tr>
<th>Temperature</th>
<th colspan="5">Polish depth</th>
</tr>
<tr>
<th></th>
<th>$0.1\Lambda$</th>
<th>$0.3\Lambda$</th>
<th>$0.5\Lambda$</th>
<th>$0.7\Lambda$</th>
<th>$0.9\Lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td>270 K</td>
<td>72.6805</td>
<td>41.3107</td>
<td>26.3632</td>
<td>12.6451</td>
<td>12.1851</td>
</tr>
<tr>
<td>320 K</td>
<td>61.9577</td>
<td>35.0635</td>
<td>22.4136</td>
<td>11.2969</td>
<td>10.6984</td>
</tr>
<tr>
<td>370 K</td>
<td>54.2544</td>
<td>30.5332</td>
<td>19.5412</td>
<td>10.2629</td>
<td>9.5611</td>
</tr>
</tbody>
</table>

sensor with a higher duty ratio has an enhanced sensitivity to temper-ature. Therefore, increasing the duty ratio can improve the coupling efficiency between core guided mode and SPP mode.

Fig. 4(b) depicts the resonance wavelength and the peak loss of fundamental core mode for different lattice pitches, with the duty ratio set to be 0.5, polishing depth as $0.5\Lambda$ and analyte $n_a = 1.35$. The results show that the dependence of the resonance on temperature is almost unaffected by the lattice pitch. However, with the lattice pitch increasing from $4\ \mu$m to $10\ \mu$m, the coupling strength between the core guided mode and SPP mode reduces. It leads a reduction in the peak loss correspondingly. Simultaneously, the observation of the decreasing space between these pairs of curves implies the dependence of the peak loss on temperature can be enhanced with small lattice pitch.

### 3.3. Dependence of the loss peak intensity on RI and temperature

As analyzed above, the duty ratio and lattice pitch have little influ-ence on the resonance wavelength, but the peak loss of the y-polarized fundamental core mode can be tuned by these coefficients. The peak loss of the SPR sensor, with smaller lattice pitch or larger duty ratio, is more

![](./images/812409782697721859_7.jpg)

Fig. 4. $h=0.5\Lambda$, $n_a=1.35$ RIU, gold metal thickness: 35 nm. (a) The resonance wavelength and the peak loss of the loss spectra for different duty ratios, $\Lambda=7.9\ \mu$m; (b) The resonance and the peak loss at different lattice pitches, $d/\Lambda=0.5$.

sensitive to temperature variation. Since the D-shaped PCF fiber SPR sensor can be used in intensity interrogation mode [17,18], we also study the dependence of the peak loss intensity on temperature and RI in detail.

The relationship between the peak loss and RI at different temperatures is plotted in Fig. 5(a). It is obvious that the peak loss varies quite linearly with RI at each temperature level. The linear fitting and correlations are also shown in the figure. With the RI range of 1.33-1.36 RIU, the peak loss of y-polarized fundamental core mode rises from 45.2 to 68.3 dB/cm, from 38.1 to 56.9 dB/cm, and from 32.9 to 48.9 dB/cm at the temperatures of 270, 320 and 370 K, corresponding to linear coefficients of 767.4502, 625.8965 and 530.8129 dB/(cm·RIU), respectively. The reduced slope implies the peak loss is more sensitive to RI version at a lower temperature. Moreover, with the increase of RI, the spacing between these curves becomes larger, which indicates the peak loss is more sensitive to temperature at increased RI range. Fig. 5(b) depicts the resonance peak loss performs a linear negative response to temperature increase. This is consistent with the fact that the increased temperature will reduce the mode coupling efficiency. When RI varies from 1.33 to 1.36 RIU, the linear sensitivity decreases from -0.1211 to -0.1913 dB/(cm·K). The absolute values imply, for the D-shaped PCF SPR sensor working in intensity interrogation mode, the peak loss is more sensitive to temperature at increased analyte RI range. This is the same with the analysis in Fig. 5(a).

### 4. Experiment and discussion

An all-glass ESM-12 (NKT Inc.) PCF is chosen to produce the SPR sensor for it is strong enough to avoid tensile failure during the polishing process. We use a wheel-polishing system (Wanrun LTD., Wuxi, china.) to achieve the side polishment, and the setup is shown in Fig. 6(a). A 30-mm-long PCF is spliced between two single-mode fibers (SMFs, core diameter: $9\ \mu$m, outer diameter: $125\ \mu$m). The ESM-12 PCF has a standard $125\ \mu$m outer diameter and is compatible with common SMF, forming an SMF-PCF-SMF sensing structure. The spliced fiber is fixed by a pair of fiber holders and the small weight is used to straighten the fiber to provide suitable tension for polishing. In order to monitor the polishing depth during the progress, one end of the spliced fiber is connected to a laser source (Maxphotonics Inc.), and the other end is connected with an optical power meter (Thorlabes Inc.) to measure the transmission loss. The micrographs of PCF cross sections before and after polishing are shown in figure (b) and (c), respectively. It can be seen that the air holes in the cladding retain their original shapes. After polishing, a 45-nm-thickness gold film is deposited on the side-polished D-shaped PCF with JGP450A magnetron sputtering device (SKY Technology Development Inc.).

The schematic diagram of experiment setup is shown in Fig. 7. White light (DH-2000-BAL, Ocean Optics Inc.) transmits into the D-shaped PCF SPR sensor region through the SMF, and the modulated spectrum is detected by a miniature spectrometer (USB 4000, Ocean Optics Inc.). Temperature of testing analyte is changed by a hot plate. Filtering the detected data with Gaussian method, normalized resonance spectra can be obtained.

Pure water was used as the detecting analyte, and the measured spectra at different temperatures are shown in Fig. 8(a). The normalized transmission spectrum is calculated according to the ratio of the

![](./images/812409782697721859_8.jpg)

Fig. 5. $d/\Lambda=0.5$, $h=0.5\Lambda$, $\Lambda=7.9\ \mu$m (a) Loss peak value shift versus RI at the temperatures of 270, 320 and 370 K. (b) Relationship between the loss peak and temperature at different RIs.

![](./images/812409782697721859_9.jpg)

Fig. 6. (a) Wheel polishing system. (b) Micrographs of ESM-12 PCF fiber cross section. (c) Image of the cross section of side-polished D-shaped PCF. (d) SEM image of the metal film.

![](./images/812409782697721859_10.jpg)

Fig. 7. SPR experiment setup based on side-polished D-shaped PCF.

![](./images/812409782697721859_11.jpg)

Fig. 8. (a) Experimentally measured transmission spectra for the D-shaped PCF SPR sensor at different temperatures. (b) Theoretically calculated transmittance. $h = 0.5\Lambda$, dAu = 48 nm.

transmittance when the sensor is immersed in liquid compared to the transmittance of the sensor exposed in the air. Obviously, the resonance is observed at about 600 nm. Theoretical calculation has also been carried out to have a comparative analysis with the detected spectra.
The RI of water can be presented as a function of wavelength, density and temperature at the temperature range of 0–100 °C:

$$
\frac{n^{2}-1}{n^{2}+2}(1 / \bar{\rho})=a_{0}+a_{1} \bar{\rho}+a_{2} \bar{T}+a_{3} \bar{\lambda}^{2} \bar{T}+\frac{a_{4}}{\bar{\lambda}^{2}}+\frac{a_{5}}{\bar{\lambda}^{2}-\bar{\lambda}_{U V}^{2}}+\frac{a_{6}}{\bar{\lambda}^{2}-\bar{\lambda}_{I R}^{2}}+\mathrm{a}_{7} \bar{\rho}^{2}
\tag{9}
$$

where the terms $\bar{\rho}$, $\bar{\lambda}$ and $\bar{T}$ are dimensionless variables and a₀ to a₇, $\bar{\lambda}_{U V}$ and $\bar{\lambda}_{I R}$ are constants [35,36]. The transmittance can be given as:

$$
T = exp\left(-\frac{4\pi}{\lambda_0} imag(n_{eff}) L\right)
\tag{10}
$$

where $\lambda_0$ refers to the wavelength of light source, and $L$ represents the length of the sensing region [37]. The resonance spectra are calculated and shown in Fig. 8(b). With the temperature increase, it is obtained that, in both experimental and theoretical data, the dip of the transmission spectrum appears blue-shift and the resonance depth is reduced.

For more detailed scenarios, the theoretical and experimental dependencies of the resonance wavelength and the transmission intensity on temperature are presented in Fig. 9. Fig. 9(a) illustrates the non-linear relation between the resonance wavelength and the temperature. As the temperature varies from room temperature (22 °C) to 90 °C with a step of 10 °C, the resonance wavelength changes from 602.6 to 586.8 nm in FEM simulation, and changes from 602.26 to 589.37 nm in the detected spectra. This is mainly due to the negative dependence of analyte RI on temperature, and a blue-shift appears in the resonance. The fitting lines show that the experimental data has a good agreement with theoretical values in the changing trends. Note that the spacing between theoretical and experimental fitting lines increases at the high temperature range, and this is mainly due to the non-uniform heat transfer. Therefore, the reduction of analyte RI is less than the theoretical value, and the measured resonance wavelength performs a small red-shift.

Fig. 9(b) shows that, with temperature increase, the normalized transmission intensity of the resonance dip varies from 63.32% to 71.32% theoretically, and varies from 63.3% to 79.73% experimentally. It is obtained that, both for theoretical and experimental data, the values have linear response versus the temperature increase, and the fitting lines are also displayed in the figure with the slopes of 2.21838%/10 °C and 1.17681%/10 °C, respectively. Because of the uneven heat transfer, the real value of analyte RI is less reduced, and higher than the value set in the simulation. With the analysis in part 3.3, the dependence of the peak loss on temperature is more sensitive at higher RI range, and this is the main reason for the increasing spacing, between the two linear fitting curves, at high temperature range. As the SPR sensor can work in wavelength and intensity interrogation mode separately or simultaneously, the temperature effects on both the wavelength and loss intensity have been studied in detail. Therefore, the results of present study may have potential applications in different situations [38,39].

## 5. Conclusion

In conclusion, the temperature effects on the sensing characteristics of the SPR sensor based on side-polished D-shaped PCF are investigated in this paper. The temperature dependences of both SPR sensor transmission (i.e., D-shaped PCF and sensing metal layer) and detecting analyte are considered in the study. With the FEM method, the coefficients of side-polishing depth, metal thickness, air hole size and lattice pitch have been studied to show their influences on the sensing performance. Theoretical calculation shows that the peak loss of the polished PCF SPR sensor with small lattice pitch or increased duty ratio exhibits an improved sensitivity to temperature. For the sensor working in intensity interrogation mode, the peak loss shows linear responses to both RI and temperature variation. Furthermore, with a wheel-polishing setup to fabricate the PCF, the proof experiment is carried out, and normalized resonance spectra are obtained. The analysis shows the experimental data has good agreement with theoretical values. Comparing with other relative work studying the temperature effects on the SPR sensor, the highlight of this work can be concluded as: (1) both the theoretical and experimental dependences of the resonance wavelength and intensity on temperature have been investigated, and the detailed analysis of the similarities and differences has been taken out. (2) this work establishes a theoretical mode to explain how temperature affects signal output, including the side-polished depth, metal thickness, air hole size, and lattice constant. (3) the fabrication method, used in the experiment, can be applied to fabricate other type D-shaped SPR sensor. Therefore, this study may lead to a better microstructure design and data processing for the D-shaped PCF SPR sensor to deal with temperature interference.

## Funding

National Natural Science Foundation of China (NSFC) (No. 61775149); Shenzhen Science and Technology Project (No. JCYJ20160226192754225, No. JCYJ20160307145209361, No. JCYJ20160307111047701); Guangdong Natural Science Foundation (2016A030313059); and Science and Technology plan project of Guangdong (2017A010101018).

## CRediT authorship contribution statement

Wei Luo: Conceptualization, Methodology, Software, Investigation, Writing - original draft. Jinwei Meng: Supervision, Data curation. Xuejin Li: Validation, Formal analysis, Visualization, Writing - review & editing. Qingli Xie: Resources, Writing - review & editing. Duo Yi: Resources, Writing - review & editing. Yanyong Wang: Resources, Writing - review & editing. Xueming Hong: Supervision, Data curation.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

![](./images/812409782697721859_12.jpg)

Fig. 9. (a) Theoretical and experimental resonance wavelength versus temperature and the corresponding fitting curves for each of them. (b) Normalized transmission intensity at the resonance and the fitting lines.

the work reported in this paper.

## Acknowledgments
The authors acknowledge the facilities, and the scientific and technical assistance, of Shenzhen Key Laboratory of Sensor Technology and Shenzhen Engineering Laboratory for Optical Fiber Sensor and Networks.

## References
[1] Y. Zeng, R. Hu, L. Wang, D. Gu, J. He, S.Y. Wu, H.P. Ho, X. Li, J. Qu, B.Z. Gao, Y. Shao, Recent advances in surface plasmon resonance imaging: detection speed, sensitivity, and portability, Nanophotonics 6 (5) (2017) 1017–1030.

[2] Z. Mai, J. Zhang, Y. Chen, J. Wang, X. Hong, Q. Su, X. Li, A disposable fiber optic SPR probe for immunoassay, Biosens. Bioelectron. 144 (2019), 111621.

[3] A. Smolyaninov, A.E. Amili, F. Vallini, S. Pappert, Y. Fainman, Programmable plasmonic phase modulation of free-space wavefronts at gigahertz rates, Nat. Photonics 13 (2019) 431–435.

[4] B. Shuai, L. Xia, D. Liu, Coexistence of positive and negative refractive index sensitivity in the liquid-core photonic crystal fiber based plasmonic sensor, Opt. Express 20 (23) (2012) 25858–25866.

[5] Y. Zhao, Z.Q. Deng, J. Li, Photonic crystal fiber based surface plasmon resonance chemical sensor, Sens. Actuators B 202 (2014) 557–567.

[6] A.A. Rifat, R. Ahmed, A.K. Yetisen, H. Butt, A. Sabouri, G.A. Mahdiraji, S.H. Yun, F. R.M. Adik, Photonic crystal fiber based plasmonic sensors, Sens. Actuators B 243 (2017) 311–325.

[7] P.J.A. Sazio, A. Amezcua-Correa, C.E. Finlayson, Microstructured optical fibers as high-pressure microfluidic reactors, Science 311 (2006) 1583–1586.

[8] X. Zhang, R. Wang, F.M. Cox, B.T. Kulhulme, M.C.J. Large, Selective coating of holes in microstructured optical fiber and its application to in-fiber absorptive polarizers, Opt. Express 15 (24) (2007) 16270–16278.

[9] W.C. Wong, C.C. Chan, J.L. Boo, Z.Y. Teo, Z.Q. Tou, H.B. Yang, C.M. Li, K.C. Leong, Photonic crystal fiber surface plasmon resonance biosensor based on protein G immobilization, IEEE J. Sel. Top. Quantum Electron. 19 (2013) 468–473.

[10] Y. Lu, X.C. Yang, M.T. Wang, J.Q. Yao, Surface plasmon resonance sensor based on hollow-core PCFs filled with silver nanowires, Electron. Lett. 51 (2015) 1675–1677.

[11] H.J. Kim, O.J. Kwon, Y.G. Han, M.K. Lee, S.B. Lee, Surface long-period fiber gratings inscribed in photonic crystal fibers, J. Korean Phys. Soc. 57 (2010) 1956–1959.

[12] J.Y. Qing, S.Y. Li, X.Z. Wang, Q. Zhu, F.L. Meng, Q. Wang, A D-type fiber based symmetrical long-range surface plasmon resonance sensor with high quality factor, Measurement 140 (2019) 395–406.

[13] Q. Wang, J.Y. Jing, X.Z. Wang, L.Y. Niu, W.M. Zhao, A D-shaped Fiber Long-range Surface Plasmon Resonance Sensor with High Q-factor and Temperature Self-compensation, IEEE T. Instrum. Meas. 69 (5) (2020) 2218–2224.

[14] Z. Hui, Y. Chen, X. Feng, X. Xiong, S. Hu, Z. Jiang, J. Dong, W. Zhu, W. Qiu, H. Guan, H. Lu, J. Yu, Y. Zhong, J. Zhang, M. He, Y. Luo, Z. Chen, Long-range surface plasmon resonance sensor based on side-polished fiber for biosensing applications, IEEE J. Sel. Top. Quant. 25 (2) (2018), 710909.

[15] S. Cao, Y. Shao, Y. Wang, T. Wu, L. Zhang, Y. Huang, F. Zhang, C. Liao, J. He, Y. Wang, Highly sensitive surface plasmon resonance biosensor based on a low-index polymer optical fiber, Opt. Express 26 (4) (2018) 3988–3994.

[16] T. Wu, Y. Shao, Y. Wang, S. Cao, W. Cao, F. Zhang, C. Liao, J. He, Y. Huang, M. Hou, Y. Wang, Surface plasmon resonance biosensor based on gold-coated side-polished hexagonal structure photonic crystal fiber, Opt. Express 25 (17) (2017) 20313–20322.

[17] Q.L. Xie, Y.Z. Chen, X.J. Li, Z. Yin, L.L. Wang, Y.F. Geng, X.M. Hong, Characteristics of D-shaped photonic crystal fiber surface plasmon resonance sensors with different side-polished lengths, Appl. Opt. 56 (5) (2017) 1550–1554.

[18] Y.Z. Chen, Q.L. Xie, X.J. Li, H.S. Zhou, X.M. Hong, Y.F. Geng, Experimental realization of D-shaped photonic crystal fiber SPR sensor, J. Phys. D Appl. Phys. 50 (2) (2017), 025101.

[19] X. Chen, L. Xia, C. Li, Surface plasmon resonance sensor based on a novel D-shaped Photonic Crystal Fiber for low refractive index detection, IEEE Photonics J. 10 (1) (2018) 6800709.

[20] W. Luo, R. Wang, H. Li, J. Kou, X. Zeng, H. Huang, X. Hu, W. Huang, Simultaneous measurement of refractive index and temperature for prism-based surface plasmon resonance sesnors, Opt. Express 27 (2) (2019) 576–589.

[21] P. Zhang, B. Lu, Y. Sun, H. Yu, K. Xu, D. Li, Side-polished flexible SPR sensor modified by graphene with in situ temperature self-compensation, Biomed. Opt. Express 10 (1) (2019) 215–225.

[22] G. Ghosh, M. Endo, T. Iwasalu, Temperature-dependent Sellmeier coefficients and chromatic dispersions for some optical fiber glasses, J. Lightwave Technol. 12 (1994) 1338–1342.

[23] A. Vial, A. Grimault, D. Macías, D. Barchiesi, M.L. Chapelle, Improved analytical fit of gold dispersion: Application to the modeling of extinction spectra with a finite-difference time-domain method, Phys. Rev. B 71 (2005), 085416.

[24] B. Han, Y. Zhang, S. E, X. Wang, D. Yang, T. Wang, K. Lu, F. Wang, Simultaneous measurement of temperature and strain based on dual SPR effect in PCF, Opt. Laser Technol. 113 (2019) 46–51.

[25] K. Lin, Y. Lu, Z. Luo, R. Zheng, P. Wang, H. Ming, Numerical and experimental investigation of temperature effects on the surface plasmon resonance sensor, Chin. Opt. Lett. 7 (5) (2009) 428–431.

[26] R. Beach, R. Christy, Electron-electron scattering in the intraband optical conductivity of Cu, Ag, and Au, Phys. Rev. B 16 (1977) 5277.

[27] W.E. Lawrence, Electron-electron scattering in the low temperature resistivity of the noble metals, Phys. Rev. B 13 (1976) 5316–5319.

[28] T. Holstein, Optical and infrared volume absorptivity of metals, Phys. Rev. 96 (2) (1954) 535–536.

[29] S.K. Ozdemir, G. Turhan-Sayan, Temperature effects on surface plasmon resonance: design considerations for an optical temperature sensor, J. Lightwave Technol. 21 (3) (2003) 805–814.

[30] C. Liu, F. Wang, J. Lv, T. Sun, Q. Liu, C. Fu, H. Mu, P.K. Chu, A highly temperature-sensitive photonic crystal fiber based on surface plasmon resonance, Opt. Commun. 359 (2016) 378–382.

[31] Y. Peng, J. Hou, Z. Huang, Q. Lu, Temperature sensor based on surface plasmon resonance within selectively coated photonic crystal fiber, Appl. Opt. 51 (26) (2012) 6361–6367.

[32] X. Yang, Y. Lu, B. Liu, J. Yao, Simultaneous measurement of refractive index and temperature based on SPR in D-shaped MOF, Appl. Opt. 56 (15) (2017) 4369–4374.

[33] Z. Tan, X. Hao, Y. Shao, Y. Chen, X. Li, P. Fan, Phase modulation and structural effects in a D-shaped all-solid photonic crystal fiber surface plasmon resonance sensor, Opt. Express 22 (12) (2014) 15049–15063.

[34] W. Luo, X. Li, J. Meng, Y. Wang, X. Hong, Surface plasmon resonance sensor based on side-polished D-shaped photonic crystal fiber with splitting cladding air holes, IEEE T. Instrum. Meas. (2021), https://doi.org/10.1109/TIM.2021.3054003.

[35] A.H. Harvey, J.S. Gallagher, J.M.H.L. Sengers, Revised formulation for the refractive index of water and steam as a function of wavelength, temperature and density, J. Phys. Chem. Ref. Data 27 (1998) 761–774.

[36] C.S. Moreira, A.M.N. Lima, H. Neff, C. Thirstrup, Temperature-dependent sensitivity of surface plasmon resonance sensors at the gold-water interface, Sens. Actuators B 134 (2008) 854–862.

[37] X. Zhao, X. Zhang, X. Zhu, Y. Shi, Long-range surface plasmon resonance sensor based on the GK570/Ag coated hollow fiber with an asymmetric layer structure, Opt. Express 27 (7) (2019) 9550–9560.

[38] Y. Zhao, Q. Wu, Y. Zhang, Simultaneous measurement of salinity, temperature and pressure in seawater using optical fiber SPR sensor, Measurement 148 (2019), 106792.

[39] Y. Liu, S. Li, H. Chen, J. Li, W. Zhang, M. Wang, Surface plasmon resonance induced high sensitivity temperature and refractive index sensor based on evanescent field enhanced photonic crystal fiber, J. Lightwave Technol. 38 (4) (2020) 919–928.

Wei Luo is a postdoctoral scholarship in Chinese University of Hong Kong (Shenzhen). He received Ph.D. degree from University of SciBioence and Technology of China in 2018. His current research interests are prism-based and fiber-based surface plasmon resonance sensors.

Jinwei Meng is pursuing master degree in College of Physics and Opto-electronic Engineering at Shenzhen University. His research interests focus on liquid-core fiber and surface plasmon resonance sensors.

Professor Xuejin Li, Associate Vice President of the Chinese University of Hong Kong (Shenzhen), is also Director of the Research Administration Office. He graduated from Tianjin University with a Doctoral degree in 2005. He was an outstanding scholar and leader of sensor discipline in Shenzhen University, the director of Shenzhen Key Laboratory of Sensor Technology, the director of Shenzhen Engineering Laboratory for Optical Fiber Sensors And Networks and the doctoral supervisor. Prof. Li has published more than 150 papers, and he has long been engaged in the study of fiber optic sensors and nonlinear optics.

Qingli Xie is pursuing master degree in College of Physics and Opto-electronic Engineering at Shenzhen University. His research interests focus on side-polished D-shaped fiber-based surface plasmon resonance sensor.

Duo Yi is associate professor in the college of Physics and Opto-electronic Engineering at Shenzhen University. He received Ph.D. degree from Université de Tchnologie de Belfort et Montbéliard. His current research interests are fiber based optic sensors.

Yanyong Wang is the researcher in the college of Physics and Opto-electronic Engineering at Shenzhen University. He received Ph.D. degree from Tianjin University. His current research interests are fiber-optic communications technology and fiber-optic amplifiers.

Hong Xue ming is an engineer at the Optical Fiber Sensor Network Engineering Laboratory, college of Physics and Opto-electronic Engineering, Shenzhen University.