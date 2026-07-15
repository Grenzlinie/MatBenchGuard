# Temperature dependence analysis of the parameters in double clad hollow core fibers.

Hanna Stawska*, Elżbieta Bereś-Pawlik,

Radiocommunication and Teleinformatics Department, Wrocław University of Technology,
Wybrzeże Wyspiańskiego 27, 50-370 Wrocław, Poland;

## ABSTRACT

A double-clad photonic bandgap fiber (DCPBGF) can be used to transmit femtosecond signals. This fiber is supposed to be applied in endoscopy in vivo. In the environment of human body, temperature is higher than ambient temperature. For this reason one should consider influence of temperature rise on properties of ultrafast impulse propagation.

Keywords: double-clad photonic bandgap fiber, femtosecond signal, endoscopy

## 1. INTRODUCTION

The introduction of femtosecond lasers into microscopy was a milestone in the development of non-linear imaging techniques such as two-photon microscopy or two-photon fluorescence lifetime imaging. Currently, researchers work on allowing to use these techniques in clinical imaging in vivo[1-2]. The most commonly used endoscopic probe design involves the use of double clad fibers. In this case, the core of the fiber is used to provide the excitation signal, while the inner clad is used to collect the fluorescence signal. Unfortunately, all the fibers used in these structures are characterized by a large dispersion approx. 100 [ps/ nm km], and currently designed endoscopes are equipped with dispersion compensation systems which are very uncomfortable for physicians. Therefore, it is important to design the fiber which allows efficient delivery of ultrafast excitation signal to the tested tissue without pulse broadening. One should face with obstacles pertaining to physical properties of fiber. The following properties of fiber should be considered during research: dispersion, losses, temperature influence on remaining properties [4-5] because this design should be applied in human body. Our aim is to build a fiber and accompanying coupler whose purpose is to eliminate previously mentioned parts of traditional system. Traditional endoscopy systems consist of many additional parts, besides a fiber itself: bulb optics, dispersion compensation systems, micromechanical systems for calibration of response signal. In the new approach we would like to optimize the construction in order to make it more compact and consequently more convenient for physicians (Figure 1).

![](./images/813224325510332417_1.jpg)

Figure 1. New construction of endoscopy system without bulb optics.

*hanna.stawska@pwr.wroc.pl

Fifth European Workshop on Optical Fibre Sensors, edited by Leszek R. Jaroszewicz, Proc. of SPIE Vol. 8794,
87942F · © 2013 SPIE · CCC code: 0277-786X/13/$18 · doi: 10.1117/12.2026616

Proc. of SPIE Vol. 8794 87942F-1

## 2. FIBER CONSTRUCTION

In [6-7] we proposed two new constructions of double clad fibers and we simulated their dispersion properties. Preliminary simulations of these fibers showed up that by matching geometric parameters of these fibers one can obtain dispersion characteristics which allow ultrafast pulse operating at a wavelength of 800nm propagated in the core of the fiber practically without becoming distorted. Designs described [6-7] were elaborated with assumption that temperature is invariant. In this paper we will consider influence of temperature on propagation properties. The cross section and geometrical parameters of the simulated DCPBGF are shown in Figure 2. The background material is silica, and the holes are filled with air. To define the structure of this fiber the following parameters are required: pitch $\Lambda$, air filling fraction f, core radius R, radius of holey region $r_1$, radius of the outmost ring $r_2$.

![](./images/813224325510332417_2.jpg)

<table>
  <tr>
    <th>pitch $\Lambda$</th>
    <td>2.4$\mu$m</td>
  </tr>
  <tr>
    <th>core radius R</th>
    <td>3.8$\mu$m</td>
  </tr>
  <tr>
    <th>radius of holey region $r_1$</th>
    <td>19$\mu$m</td>
  </tr>
  <tr>
    <th>radius of outmost ring $r_2$</th>
    <td>45$\mu$m</td>
  </tr>
  <tr>
    <th>air filling fraction f</th>
    <td>0.92</td>
  </tr>
</table>

Figure 2. Cross section and geometrical parameters of simulated DCPBGF.

## 3. THE TEMPERATURE DEPENDENCE OF THE REFRACTIVE INDEXES

The method used in this paper has been introduced by Matsuoka [3]. The refractive index data of silica glass are fitted with three-term Sellmeier dispersion equation which is derived from Lorentz oscillator model. This equation gives the refractive index with good approximation in UV, Visible and near-IR regions. Matsuoka discussed the temperature dependence of the refractive index in terms of the temperature dependence of each parameter in this equation. The Sellmeier equation expressed the refractive index as a function of photon energy and is expressed by formula:

$$
n^{2}-1=\sum_{i=1}^{3} \frac{a_{i}}{b_{i}^{2}-E^{2}} \tag{1}
$$

Where n is the absolute refractive index, E is the photon energy in electron volts, $a_i$ is a parameter given by the product of oscillator strength and number of oscillators per unit volume, and $b_i$ is the resonance energy of the oscillators. To include the temperature dependence of the refractive index in this equation Matsuoka expressed $a_i$ and $b_i$ as a quadratic functions of temperature as

$$
a_{i}=a_{i 1}+a_{i 2} T+a_{i 3} T^{2} \tag{2}
$$

$$
b_{i}=b_{i 1}+b_{i 2} T+b_{i 3} T^{2} \tag{3}
$$

Where T is the temperature in degrees Celsius.

Parameters in equations (2) and (3) were calculated by Matsuoka by the least square method and are listed in Table 1.

Table 1. Parameters for Sellmeier equation dependent on temperature.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>i=1</th>
      <th>i=2</th>
      <th>i=3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>aᵢ₀ (eV²)</td>
      <td>228.7018</td>
      <td>46.40806</td>
      <td>0.014173</td>
    </tr>
    <tr>
      <td>aᵢ₁ (eV² C⁻¹)</td>
      <td>4.93*10⁻⁵</td>
      <td>-3.27*10⁻⁵</td>
      <td>-1.704*10⁻⁶</td>
    </tr>
    <tr>
      <td>aᵢ₂ (eV² C⁻²)</td>
      <td>1.10*10⁻⁷</td>
      <td>-3.78*10⁻⁸</td>
      <td>-2.14*10⁻⁹</td>
    </tr>
    <tr>
      <td>bᵢ₁ (eV²)</td>
      <td>18.111630</td>
      <td>10.671082</td>
      <td>0.125</td>
    </tr>
    <tr>
      <td>bᵢ₂ (eV² C⁻¹)</td>
      <td>9.15*10⁻⁵</td>
      <td>-2.9913*10⁻⁴</td>
      <td>&lt;10⁻⁵</td>
    </tr>
    <tr>
      <td>bᵢ₃ (eV² C⁻²)</td>
      <td>7.478*10⁻⁵</td>
      <td>-4.8074*10⁻⁸</td>
      <td>&lt;10⁻⁸</td>
    </tr>
  </tbody>
</table>

## 4. RESULTS AND DISCUSSION

The temperature dependence on refractive index at 808nm was simulated using parameters calculated by Matsuoka and is presented in Figure 3.

![](./images/813224325510332417_3.jpg)

Figure 3. The temperature dependence on refractive index at 808nm.

Because human body temperature is different from ambient temperature, parameters of Sellemier equation were determined for two temperatures T=20C and T=40C. The obtained results are presented in Table 3. Additionally we have simulated dispersion and losses for this double clad fiber Figure 4. Regarding calculated losses and dispersion, the temperature has significant impact on wavelength below 795nm. Simulation in the research were carried out by means of commercial application Lumerical Mode Solution.

Table 3. Parameters for temperature dependent Sellmeier equation.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>T=20⁰C</th>
      <th>T=40⁰C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>a₁</td>
      <td>228.703</td>
      <td>228.704</td>
    </tr>
    <tr>
      <td>a₂</td>
      <td>46.4074</td>
      <td>46.4067</td>
    </tr>
    <tr>
      <td>a₃</td>
      <td>0.0141381</td>
      <td>0.0141014</td>
    </tr>
    <tr>
      <td>b₁</td>
      <td>18.1118</td>
      <td>18.1121</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>T=20⁰C</th>
      <th>T=40⁰C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>b₂</td>
      <td>10.6649</td>
      <td>10.6583</td>
    </tr>
    <tr>
      <td>b₃</td>
      <td>0.125104</td>
      <td>0.125216</td>
    </tr>
  </tbody>
</table>

![](./images/813224325510332417_4.jpg)

Figure 4. Losses and dispersion for double clad hollow core fiber vs wavelength for two temperatures.

## 5. CONCLUSION

We have proven that temperature influence on properties of tested fibers is to be neglected in measured temperature range. Usage of this fiber in vivo does not require additional compensation methods. Thus we can conclude that this fiber is suitable to medical applications. Due to ultrashort pulses used in two photon fluorescence endoscopy fiber, thermal effect is not observed.

## 6. ACKNOWLEDGMENT

This work is co-financed by the European Union as part of the European Social Fund. Calculations have been carried out in Wrocław Centre for Networking and Supercomputing (http://www.wcss.wroc.pl), Grant No. 184. This work is also co-financed by Grant No. S20089.

## REFERENCES

[1] Bereś-Pawlik Elżbieta, Dybała Filip, Michalski Wojciech, Duś Danuta "Application of the fluorescent fiber sensor for tumor cells quantification", Opt. Appl., vol. 34 nr 1, pp. 87-92, 2004.
[2] Bereś-Pawlik E., Gąsiorek K., Kulas Z., Rząca M., "Optical Fiber Sensors for Point Investigation of Cancer Tissues", Acta Physica Polonica A, vol 116, pp. 254-256, 2009.
[3] J. Matsuoka, N. Kitamura, S. Fujinaga, T. Kitaoka, H. Yamashita "Temperature dependence of refractive index of SiO2 glass," Journal of Non-Crystalline Solids, vol. 135, issue 1, pp. 86-89.
[4] C. Engelbrecht, R. Johnston, E. Seibel, and F. Helmchen, "Ultra-compact fiber-optic two-photon microscope for functional fluorescence imaging in vivo," Opt. Express 16, 5556-5564 (2008).
[5] D. Bird and M. Gu, "Two-photon fluorescence endoscopy with a micro-optic scanning head," Opt. Lett. 28, 1552-1554 (2003).
[6] H. Stawska, E. Bereś-Pawlik, Construction of double cladding small dispersion photonic crystal fiber to guide ultrashort pulse at 800 nm., Acta Physica Polonica. A. 2012, vol. 122, nr 5, s. 896-899.
[7] H. Stawska , E. Bereś-Pawlik, Dispersion properties of double-clad hollow-core photonic bandgap fibers based on a circular lattice cladding., 22nd International Conference on Optical Fiber Sensors, OFS-22, Beijing, China, 15-19 October 2012 / [ed. by Yanbiao Liao i in.]. Bellingham, Wash. : SPIE, cop. 2012. s. 84217F-1 - 84217F-4.
