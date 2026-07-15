# In operando investigation of GaN PIN device characteristics under electron irradiation energies comparable to Pm-147 source for betavoltaic application

Cite as: AIP Advances 10, 085110 (2020); https://doi.org/10.1063/5.0015517
Submitted: 28 May 2020 . Accepted: 14 July 2020 . Published Online: 04 August 2020

Kasey Hogan, Miguel Rodriguez, Emma Rocco, Vincent Meyers, Benjamin McEwen, and F. Shadi Shahedipour-Sandvik

![](./images/812581368419581953_1.jpg)

![](./images/812581368419581953_2.jpg)
![](./images/812581368419581953_3.jpg)
![](./images/812581368419581953_4.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

Numerical investigation of the patterns of the flow past nine cylinders at low Reynolds number
AIP Advances 10, 085107 (2020); https://doi.org/10.1063/5.0015541

Multiphysics analysis for unusual heat convection in microwave heating liquid
AIP Advances 10, 085201 (2020); https://doi.org/10.1063/5.0013295

Multi-modal surface analysis of porous films under operando conditions
AIP Advances 10, 085109 (2020); https://doi.org/10.1063/5.0006220

![](./images/812581368419581953_5.jpg)

AIP Advances 10, 085110 (2020); https://doi.org/10.1063/5.0015517
© 2020 Author(s).

10, 085110

# In operando investigation of GaN PIN device characteristics under electron irradiation energies comparable to Pm-147 source for betavoltaic application

Cite as: AIP Advances 10, 085110 (2020); doi: 10.1063/5.0015517
Submitted: 28 May 2000 • Accepted: 14 July 2020 •
Published Online: 4 August 2020

![](./images/812581368419581953_6.jpg) ![](./images/812581368419581953_7.jpg) ![](./images/812581368419581953_8.jpg)

Kasey Hogan,ª Miguel Rodriguez, Emma Rocco, Vincent Meyers, Benjamin McEwen, and F. Shadi Shahedipour-Sandvik

## AFFILIATIONS
College of Nanoscale Science and Engineering, SUNY Polytechnic Institute, Albany, New York 12203, USA

ªAuthor to whom correspondence should be addressed: khogan@sunypoly.edu

## ABSTRACT
Here, we report on the application of an electron source with high accelerating voltage (62 kV–200 kV) to simulate betavoltaic power generation capabilities of a planar GaN PIN ($p$-GaN/$i$-GaN/$n$-GaN) device. The *in situ* electrical characterization reported here enables detailed performance comparison of new device designs to conventional device configurations. *In operando* investigation of a GaN PIN device under irradiation by a modified transmission electron microscope is being reported here. A large-area planar GaN PIN ($0.04\ \text{cm}^2$, $17.8\ \text{nA/cm}^2$ at 5 V reverse bias) device was irradiated with an electron beam of approximately equivalent spot size. At an approximate input current density of $5\ \text{nA/cm}^2$, the maximum power produced (MPP) decreases from $2.45\ \mu\text{W/cm}^2$ to $0.45\ \mu\text{W/cm}^2$ with an increase in the beam voltage from 62 kV to 200 kV. This reduction in power corresponds to reduced electron–hole pair generation and capture within the active region of the device. The inverse relation of MPP to beam voltage is modeled by CASINO2 Monte Carlo simulations of energy absorption and is found to be in good agreement with the experimental measurement. At a constant 62 kV beam voltage, MPP is shown to increase with beam current density up to $48.2\ \mu\text{W/cm}^2$ at $177\ \text{nA/cm}^2$. Repeated device dark current measurements following the irradiation indicate no degradation of the device. An irradiation dose of $\sim10^{16}\ \text{cm}^{-2}$, equivalent to exposure from a 10 mCi radioisotope source for 1 yr, was performed at an energy of 200 kV, with no appreciable deterioration in device performance.

© 2020 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0015517

## I. INTRODUCTION
Betavoltaic (BV) micro-batteries characteristically have high energy density, relatively low mass, and long lifetime. Direct charge-conversion devices, such as PN-junction and Schottky diodes, are the focus of most current research in the field. The use of wide bandgap (WBG) materials such as (Al)GaN, SiC, and diamond shows promise due to their radiation hardness, high theoretical conversion efficiencies, and continuous improvement in material quality and cost. Recent reports show improvement of WBG-based betavoltaic device performance and propose advanced device designs. $^{1–10}$ Wide bandgap oxides such as $\text{TiO}_2$ and $\text{ZnO}$ show promise by implementing 3D nanostructures in the device design. $^{11–13}$ An important consideration for performance of BV devices is the effective source activity incident to the device. A higher effective surface activity can be achieved by minimizing the self-absorption of energy within the isotope and by utilizing a 3D geometry to increase the surface area contact between the isotope and the device for a given wafer footprint. In this regard, the development of liquid-form isotopes will lower self-absorption due to reduced material density (compared to conventional metal-based sources) and enables conformal coverage of 3D structures for increased source–semiconductor surface area. $^{14,15}$

The (Al)GaN material system shows particular promise for BV application due to its desirable properties, including wide and tunable direct bandgap, radiation hardness, chemical inertness, and physical hardness. Current state-of-the-art GaN-based devices suffer from low conversion efficiency (<1%) due to limited minority carrier diffusion length and limited output power from limited surface contact of the isotope for a given wafer footprint when using a 2D planar configuration. To improve device performance, it is necessary to optimize device design for maximum electron-hole pair (EHP) collection efficiency by employing a higher surface area and to select appropriate higher energy emitting sources such as $^{147}$Pm (62 keV avg. energy).$^{14}$ Common methods for investigating device characteristics of direct conversion devices under irradiation for use in a BV configuration include *in situ* testing under an electron flood gun or using a scanning electron microscope (SEM).$^{16}$ The achievable electron accelerating voltages in these settings are typically limited to <30 kV. Bao *et al.* reported using a linear accelerator as the electron source to achieve high beam currents and voltages for the investigation of a radiation hardened-Si solar cell as a BV converter.$^{17}$ These methods of testing differ from the emission of a radioisotope source in which the electrons incident on the device are monoenergetic, whereas with a real isotope source, a spectrum of electron energies is emitted at all angles. Although the common low-energy radioisotope sources ($^{3}$H and $^{63}$Ni) are statistically favored to emit electron energies <62 keV, $^{147}$Pm and $^{90}$Sr emit a greater proportion of beta electrons above this level. As such, it is important to understand and quantify device characteristics under irradiation by these higher energies over a period of time. High energy electrons can produce point defects in GaN in the form of Ga and N vacancies, negatively impacting its electrical characteristics by the introduction of trap states.$^{18}$ Early experimental results for the probability of defect creation utilizing the Rutherford cross-section model indicated that atomic displacement of the Ga atom by electron bombardment occurs at a threshold energy of 440 keV in AlGaN/GaN light emitting diodes (LEDs), which corresponds to a displacement energy of $E_d = 19 \pm 2$ eV.$^{19}$ More recent molecular dynamics simulations indicate that the displacement energy is likely much higher for both Ga and N at $E_d$ = 73.2 eV and $E_d$ = 32.4 eV, respectively.$^{20}$ The value for displacement energy is also highly dependent on the plane-orientation of the GaN film.$^{20}$ It is known that dose, energy, dislocation density, impurity concentration, and carrier concentration will all have some effect on the characteristics of GaN in response to radiation.$^{21}$ In order to select the best design for the next-generation of GaN-based betavoltaic devices, it is important to experimentally demonstrate device response under the full energy and activity range of common isotope sources.

Here, we report on *in operando* investigation of the characteristics of a low leakage planar GaN PIN device under the application of an electron beam with the accelerating voltage in the range of 62 kV–200 kV and a variable beam current. *In situ* measurement of the electrical characteristics of the device detailed here will enable future investigation into new device designs and materials closely relevant to BV application. To carry out the study, a transmission electron microscope (TEM) that allows for fast, repeatable, and variable current measurements of devices has been modified. Such a characterization system is an ideal proxy for investigation of novel device designs, as well as the effect of radiation on material quality and device characteristics without the challenges associated with higher-energy radioactive isotope sources.

## II. EXPERIMENTAL
### A. Irradiation system modifications
A JEOL 2010 TEM system with a tungsten (W) filament was used in this study. The standard specimen stage was bypassed within the TEM column, and the beam was brought to focus within the viewing chamber. A custom flange fitting was engineered to hold the packaged device in place while enabling vacuum feedthroughs into the viewing chamber for *in situ* electrical characterization of the device under irradiation. A Keithley 6430 sub-fA remote source meter paired with a Model 6430 Remote Preamp is used to measure the current–voltage (IV) characteristics of a given device. A Python script was used for remote-control of the source meter and automation of the data capture and storage (https://github.com/khoga2/keithley_control).

A phosphor screen is used for visualizing the focus and sizing of the beam above the device surface. Measurement of the beam current magnitude incident on the device is made via an ammeter in contact with the phosphor screen. A reference circle of 500 $\mu$m diameter at the center of the screen allows for an estimation of the beam area.

### B. Experimental parameters
A GaN PIN planar film was grown by the metalorganic chemical vapor deposition (MOCVD) technique using a Veeco D180 vertical reactor. The material layers consist of 80 nm $p$-GaN, 500 nm $i$-GaN, and 3.6 $\mu$m $n$-GaN grown on a physical vapor deposition nanocolumn (PVDNC) AlN buffer layer deposited on a sapphire substrate. Devices were fabricated by standard optical lithography with mesa isolation formed by inductively coupled plasma (ICP) reactive ion etching (RIE). A 20% potassium hydroxide (KOH) chemical etch was employed to reduce the damage induced by the dry etch. A transparent current-spreading contact was deposited on the $p$-GaN mesa surface consisting of 3 nm Ni/3 nm Au, with a thicker ring-eye contact, and 50 nm Ni/50 nm Au, along the outer edge of the device, as shown in Fig. 1. Selected devices were placed in a custom $1^2$ in. package with Au-bond pads. The device under test (DUT) for this study has an area of 0.04 cm$^2$ with 17.8 nA/cm$^2$ leakage current density ($J_L$) at 5 V reverse bias.

Dark current ($J_d$) measurements were performed *in situ* and prior to irradiation to confirm that the performance of the device was not affected by the packaging and mounting. A systematic study of irradiation conditions was performed with a beam of approximately equal area to the device area of 0.04 cm$^2$ for all of the tests, unless otherwise noted. Under each of the conditions described hereafter, the IV characteristics of the DUT were captured using the methods described in Sec. III A. The beam accelerating voltage was increased from 62 kV to 200 kV in increments of 20 kV. At each voltage setpoint, the focus and position of the beam were adjusted over the DUT, and an example of beam repositioning is shown in Fig. 1. Following the first cross-over of the electron beam, the condenser lens can be altered to select an appropriate spot size which determines the overall diameter and current of the beam.

---

AIP Advances 10, 085110 (2020); doi: 10.1063/5.0015517
© Author(s) 2020

10, 085110-2

![](./images/812581368419581953_9.jpg)

FIG. 1. (left) Image of a dummy device under test (DUT) illuminated by 10 mA injection current (blue), which sits adjacent to the 62-kV electron beam irradiating the GaN surface (green); this allows for locating the device to adjust the beam position and (right) the device and the electron beam superimposed after making use of the electron beam XY control; the sample remains fixed within a custom holder.

In addition, a selection of the physical aperture within the column can modulate the beam current incident to the sample. For this series of irradiations, the input beam current density was held constant at $\sim 5\ \text{nA/cm}^2$ by tuning the condenser lens aperture and filament emission current appropriately at each accelerating voltage. A series of irradiations with varying beam input current density were also performed, ranging from $\sim 4\ \text{nA/cm}^2$ to $500\ \text{nA/cm}^2$. The beam voltage was held constant at either 62 kV or 200 kV. An extended duration irradiation was performed at $200\ \text{kV}$, $500\ \text{nA/cm}^2$ for 1 h, leading to a target total dose of $\sim 1 \times 10^{16}\ \text{cm}^{-2}$. This dose is equivalent to irradiation using a 10 mCi radioisotope source for a duration of 1 yr. The IV characteristics of the DUT were obtained at 10 min intervals to observe possible degradation of the device characteristics as the irradiation proceeded, specifically degradation in power generation.

In addition, Monte Carlo simulations using CASINO2 software were performed to simulate the energy deposition profile within the material layers as a function of beam voltage. This allows for an estimation of the energy absorbed within the active region of the device compared to the nonactive layers, where the active region is defined as the distance from the surface through the depletion width within the i-region of the PIN. The simulated value for the energy absorbed can be used to estimate the relative change in produced power, for a given electron beam energy. For these simulations, the material is considered ideal and free from impurities and defects which would alter the electron trajectory. For calculation of the energy absorbed along the depth of the simulated structure, a voltage-dependent value for the number of equally spaced in-plane sections ($\Delta x$) was used to maintain near 10 nm resolution along the depth of the sample, with $1 \times 10^6$ electrons being simulated at each beam voltage.

### III. RESULTS AND DISCUSSION

The experimental maximum power produced (MPP) as a function of the beam accelerating voltage is shown in Fig. 2. The power output of the device is calculated by the product of measured device current and voltage during irradiation in the $0\ \text{V}$-$V_{\text{oc}}\ \text{V}$ voltage range. $^{22}$ The maximum value in this range is the MPP. The fill factor (FF) of the device is calculated by

$$
FF = \frac{MPP}{I_{sc}V_{oc}}. \tag{1}
$$

![](./images/812581368419581953_10.jpg)

FIG. 2. Measured MPP as a function of beam accelerating voltage. The slight increase in MPP more than 140 kV is attributed to the variation in the beam current, beam area, and instability under high voltage/low current operation.

Here, $I_{sc}$ is the short-circuit current, and $V_{oc}$ is the open-circuit voltage. In addition, the $FF$ was calculated at each of the beam voltage setpoints, leading to an average $FF_{avg} = 0.56 \pm 0.1$. The MPP is maximum at a beam voltage of $62\ \text{kV}$, with a value of $2.45\ \mu\text{W/cm}^2$. This MPP continuously lowers as the beam accelerating voltage is increased up to $140\ \text{kV}$, where a slight increase in the MPP occurs, which again lowers at $200\ \text{kV}$ to a minimum density of $0.45\ \mu\text{W/cm}^2$, as shown in Fig. 2. The slight increase in MPP may be associated with variation in the beam size and current as the beam energy is altered and possible increased backscattering under the new beam condition. For voltages beyond $140\ \text{kV}$, maintaining the $5\ \text{nA/cm}^2$ current density setting was shown to be challenging due to un-optimal operation of the electron source filament for lower emission currents. Dark current measurements after each irradiation energy show no degradation in the electrical characteristics. The measured decrease in MPP with increasing beam voltage is consistent with the results of the CASINO2 Monte Carlo simulations, performed under the conditions described previously. Table I shows the percentage of energy absorbed within the active region of the device relative to the total energy absorbed for each beam energy simulated. In order to deduce the change in produced power based on the change in the percentage of energy absorbed in the active region, % energy absorbed in the $80\ \text{kV}$-$180\ \text{kV}$ range was weighted against the lowest beam energy at $62\ \text{kV}$. From this, the simulated MPP was calculated from the simulated change in energy absorbed. The experimental MPP was calculated between each beam energy and the $62\ \text{kV}$ baseline. The experimental MPP and the simulated MPP are plotted in Fig. 3. The simulated MPP trends closely with the measured values for beam voltages below $140\ \text{kV}$. The difference in their values is likely derived from the assumption of ideal material in the simulation. Such an assumption omits any interaction between incoming electrons and traps or impurities within the GaN layers and thereby leads to a larger simulated interaction volume than the volume that exists in the real device. This may contribute to the overall lower MPP for the

<table><caption>TABLE I. CASINO2 simulation results and calculating MPP based on energy absorbed in the active region.</caption>
<thead>
<tr>
<th>Energy (kV)</th>
<th>% total energy absorbed in the active layer</th>
<th>Experimental MPP (nW)</th>
<th>Simulated MPP (nW)</th>
</tr>
</thead>
<tbody>
<tr>
<td>62</td>
<td>6.1</td>
<td>97.8</td>
<td>97.8</td>
</tr>
<tr>
<td>80</td>
<td>3.2</td>
<td>62.8</td>
<td>50.9</td>
</tr>
<tr>
<td>100</td>
<td>1.8</td>
<td>47.3</td>
<td>29.2</td>
</tr>
<tr>
<td>120</td>
<td>1.2</td>
<td>37.6</td>
<td>19.5</td>
</tr>
<tr>
<td>140</td>
<td>0.9</td>
<td>21.3</td>
<td>14.4</td>
</tr>
<tr>
<td>160</td>
<td>0.7</td>
<td>23.6</td>
<td>11.2</td>
</tr>
<tr>
<td>180</td>
<td>0.6</td>
<td>25.1</td>
<td>9.3</td>
</tr>
</tbody>
</table>

simulation results than the experimental results at any given beam energy.

The MPP as a function of beam current is shown in Fig. 4. A lin- ear increase in the power as a function of input beam current density ($J_{in}$) is observed for both the 62 kV and 200 kV accelerating voltage setpoints, with a different rate of increase for each of the voltages. The MPP is shown to increase up to $48.2\ \mu\text{W/cm}^2$ with increased beam current density to $177\ \text{nA/cm}^2$ at 62 kV accelerating voltage. The MPP for the 62 kV beam voltage is higher for all input beam current values than the 200 kV beam voltage. The difference in the slope for the two cases is related to the efficiency of energy conver- sion. The energy conversion rate is markedly higher for the 62 kV electrons, which dissipate proportionally more energy in the active layers than a 200 kV electron. For irradiation by 200 kV electrons, EHPs are generated and lost well below the active layers, even into the sapphire substrate, resulting in a low conversion efficiency and limited power output. $I_{sc}$ and $V_{oc}$ are plotted against one another in Fig. 5 and fitted using the following relationship:

$$
V_{o c}=\frac{n k T}{q} \ln \left(\frac{I_{s c}}{I_{o}}\right). \tag{2}
$$

![](./images/812581368419581953_11.jpg)

FIG. 3. Comparison of the change in MPP ($\Delta$MPP) for the experimental data and the CASINO Monte Carlo simulation of energy absorbed. The value for MPP at 62 kV is used as the baseline to normalize the simulated data.

![](./images/812581368419581953_12.jpg)

FIG. 4. Input beam current density dependence on measured MPP for 62 kV and 200 kV accelerating voltages. The y-intercept is fixed at MPP ($x=0$) = $J_{in}$ ($x=0$) = 0 for both of the linear fits.

Here, $I_o$ is the saturation current of the device and is calculated as a fitting parameter for $I_{sc} \gg I_o$, and $T$ is 300 K. Using these val- ues, the ideality factor of the device is measured to be $n=2.97$ $\pm$ 0.12. This value is in good agreement with previous reports for high performance GaN PIN devices on the sapphire substrate.

In order to simulate the long-term radiation response of the GaN PIN device, an irradiation dose test was performed. For this measurement, the electron source was set to 200 kV with a target input current density of $500\ \text{nA/cm}^2$ for 1 h. This current density leads to a target dose of $10^{16}\ \text{cm}^{-2}$, which is equivalent to expo- sure to a 10 mCi source for a period of 1 yr. The selected electron energy of 200 keV is near the maximum for a $^{147}$Pm source (225 keV). Table II shows the values for $I_{sc}$, $V_{oc}$, and MPP at selected time steps throughout the irradiation. $I_{sc}$, $V_{oc}$, and MPP each show a downward trend as time proceeds from t = 0 to t = 60 min, with $I_{sc}$ decreasing from $3.75 \times 10^{-7}$ A to $2.22 \times 10^{-7}$ A, $V_{oc}$ from 2.16 V to 2.09 V, and MPP from $4.96 \times 10^{-7}$ W to $2.78 \times 10^{-7}$ W. MPP is plotted as a function of time in Fig. 6. The decrease appears to

![](./images/812581368419581953_13.jpg)

FIG. 5. Relationship between $V_{oc}$ and $I_{sc}$ for the beam currents tested at 62 kV.

<table>
<caption>TABLE II. Device characteristics during the dose test at 200 kV.</caption>
<thead>
<tr>
<th>Time (min)</th>
<th>I<sub>sc</sub> (A)</th>
<th>V<sub>oc</sub> (V)</th>
<th>MPP (W)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>−3.75 × 10<sup>−7</sup></td>
<td>2.16</td>
<td>4.96 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>5</td>
<td>−3.16 × 10<sup>−7</sup></td>
<td>2.14</td>
<td>4.10 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>10</td>
<td>−2.82 × 10<sup>−7</sup></td>
<td>2.12</td>
<td>3.52 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>20</td>
<td>−2.30 × 10<sup>−7</sup></td>
<td>2.10</td>
<td>2.93 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>30</td>
<td>−2.56 × 10<sup>−7</sup></td>
<td>2.11</td>
<td>3.26 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>40</td>
<td>−2.01 × 10<sup>−7</sup></td>
<td>2.08</td>
<td>2.50 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>50</td>
<td>−3.40 × 10<sup>−7</sup></td>
<td>2.15</td>
<td>4.47 × 10<sup>−7</sup></td>
</tr>
<tr>
<td>60</td>
<td>−2.22 × 10<sup>−7</sup></td>
<td>2.09</td>
<td>2.78 × 10<sup>−7</sup></td>
</tr>
</tbody>
</table>

![](./images/812581368419581953_14.jpg)

FIG. 6. Experimental MPP measured during the irradiation dose test. The decrease observed in MPP throughout the experiment is attributed to the filament emission current variability described above. The dark current measurement after irradiation indicated no change in the electrical characteristics of the device from electron bombardment.

be due to a slight decrease in the input beam current throughout the irradiation and not a change in device performance. To confirm this, dark current measurement was made after 1 h of irradiation, which shows negligible change in leakage characteristics and forward resistance. As such, the irradiation conditions appear to be below the threshold for significant lattice defect generation, consistent with previous reports. Other degradation mechanisms such as contact damage and Al wire-bond damage are also not expected to have occurred, given the sustained dark current characteristics and inspection under SEM.

## IV. CONCLUSION

In operando characterization of a direct conversion GaN PIN device for BV application using a high energy (62 kV–200 kV) electron source has been demonstrated in this report. The large-area planar GaN PIN (0.04 cm², 17.8 nA/cm² at −5 V) device shows a decrease in maximum power produced (MPP) from 2.45 μW/cm² to 0.45 μW/cm² at an approximate input current density of 5 nA/cm² for increasing beam voltages from 62 kV to 200 kV. In addition, the MPP shows enhancement with increased beam current density up to 48.2 μW/cm² at 177 nA/cm² at 62 kV voltage set point. A dose test was performed to a target of 10¹⁶ cm⁻², which led to no observable change in the dark current characteristics of the device, indicating no observable radiation induced degradation of the device. This unique characterization capability allows for non-destructive sample preparation and fast evaluation of new device designs and structures for the next generation of BV devices coupled with high energy sources.

## ACKNOWLEDGMENTS

The work presented here was supported by the Army Research Office under Award No. W911NF-18-2-0215 under the direction of Dr. Michael Gerhold. The authors would like to thank Brian Taylor and the CNSE Academic Engineering Group for assistance with the design and fabrication of the custom hardware and Dr. Bradley Thiel for sharing his insight into electron optics. The authors are thankful to Dr. Marc Litz and Dr. Randy Tompkins of the Army Research Laboratory for many insightful discussions.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

¹K. Hogan, M. Litz, and F. Shahedipour-Sandvik, Appl. Radiat. Isot. 145, 154 (2019).
²R. Zheng, J. Lu, Y. Liu, X. Li, X. Xu, R. He, Z. Tao, and Y. Gao, Radiat. Phys. Chem. 168, 108595 (2020).
³M. Litz, W. Ray, J. Russo, S. Kelley, and J. Smith, U.S. Army, ARL-TR-7801 (September 2015).
⁴T. R. Alam, M. G. Spencer, M. A. Prelas, and M. A. Pierson, Int. J. Energy Res. 42, 2564 (2018).
⁵C. Thomas, S. Portnoff, and M. G. Spencer, Appl. Phys. Lett. 108, 013505 (2016).
⁶L. Zhang, H. L. Cheng, X. C. Hu, and X. B. Xu, Superlattices Microstruct. 123, 60–70 (2018).
⁷V. S. Bormashov, S. Y. Troschiev, S. A. Tarelkin, A. P. Volkov, D. V. Teteruk, A. V. Golovanov, M. S. Kuznetsov, N. V. Kornilov, S. A. Terentiev, and V. D. Blank, Diamond Relat. Mater. 84, 41 (2018).
⁸C. Delfaure, M. Pomorski, J. De Sanoit, P. Bergonzo, and S. Saada, Appl. Phys. Lett. 108, 252105 (2016).
⁹S. Tarelkin, V. Bormashov, E. Korostylev, S. Troschiev, D. Teteruk, A. Golovanov, A. Volkov, N. Kornilov, M. Kuznetsov, D. Prikhodko, and S. Buga, Phys. Status Solidi A 213, 2492 (2016).
¹⁰J. W. Murphy, L. F. Voss, C. D. Frye, Q. Shao, K. Kazkaz, M. A. Stoyer, R. A. Henderson, and R. J. Nikolic, AIP Adv. 9, 065208 (2019).
¹¹Q. Zhang, R. Chen, H. San, G. Liu, and K. Wang, J. Power Sources 282, 529 (2015).
¹²Q. Zhang, N. Wang, P. Zhou, C. Chen, H. San, K. Wang, and X. Chen, in Proceedings of IEEE International Conference on Micro Electro Mechanical Systems, February 2016 (IEEE, 2016), p. 1177.
¹³M. Wu, S. Wang, Y. Ou, and W. Wang, Appl. Radiat. Isot. 142, 22 (2018).
¹⁴J. Russo, H. Berk, and D. Bigio, U.S. Army, ARL-TR-8599 (December 2018).

$^{15}$J. Russo, M. Litz, W. Ray, G. M. Rosen, D. I. Bigio, and R. Fazio, *Appl. Radiat. Isot.* **125**, 66 (2017).

$^{16}$M. R. Khan, J. R. Smith, R. P. Tompkins, S. Kelley, M. Litz, J. Russo, J. Leather- sich, F. Shahedipour-Sandvik, K. A. Jones, and A. Iliadis, *Solid-State Electron.* **136**, 24 (2017).

$^{17}$R. Bao, P. J. Brand, and D. B. Chrisey, *IEEE Trans. Electron Devices* **59**, 1286 (2012).

$^{18}$A. Y. Polyakov, S. J. Pearton, P. Frenzer, F. Ren, L. Liu, and J. Kim, *J. Mater. Chem. C* **1**, 877 (2013).

$^{19}$A. Ionascut-Nedelcescu, C. Carlone, A. Houdayer, H. J. Von Bardeleben, J.-L. Cantin, and S. Raymond, *IEEE Trans. Nucl. Sci.* **49**, 2733 (2002).

$^{20}$H. Y. Xiao, F. Gao, X. T. Zu, and W. J. Weber, *J. Appl. Phys.* **105**, 123527 (2009).

$^{21}$S. J. Pearton, F. Ren, E. Patrick, M. E. Law, and A. Y. Polyakov, *ECS J. Solid State Sci. Technol.* **5**, Q35 (2016).

$^{22}$K. E. Bower, Y. A. Barbanel, Y. G. Shreter, and G. W. Bohnert, *Polymers, Phos- phors, and Voltaics for Radioisotope Batteries* (CRC Press, Boca Raton, 2002), Chap. 1.2.3.

---

AIP Advances **10**, 085110 (2020); doi: 10.1063/5.0015517
© Author(s) 2020

10, 085110-6
