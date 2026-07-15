# Fiber-Optic Fabry-Perot Interferometer and Its Sensor Applications

TOSHIHIKO YOSHINO, KIYOSHI KUROSAWA, KATSUJI ITOH, AND TERUZI OSE

Abstract-Fiber-optic Fabry-Perot interferometers using monomode fibers are fabricated and their basic properties of finesse, polarization, and thermal response are studied. Fiber-optic Fabry-Perot inter- ferometers are applied to the sensors of temperature, mechanical vibration, acoustic wave including human voice, ac voltage, and ac and dc magnetic fields. It has been demonstrated that a fiber-optic Fabry- Perot interferometer can simplify the interferometric fiber sensor sys- tem and that high measurement sensitivity can be obtained by using a high-finesse and/or long-distance fiber Fabry-Perot interferometer.

## I. INTRODUCTION
T HE advent of monomode fibers has opened doors for the coherent use of optical fibers. As monomode fibers can carry light coherently, they can be used for arms in interferometers. Until now, two different forms of the fiber- optic interferometer using monomode fibers have been well known. One is the Mach-Zehnder form, which is used for the interferometric fiber sensor of acoustic wave [1], temperature[2], and magnetic field [3]. The other is the Sagnac form, which is used for fiber gyro [4]. Both of the interferometers utilize the two-beam interference. Recently, the Fabry- Perot form of fiber-optic interferometer, which utilizes the multiple-beam interference, has been demonstrated [5] and followed by some authors [6], [7]. The concept of using the fiber-optic Fabry-Perot interferometer for a sensor is noted in[8]. The fiber-optic Fabry-Perot interferometer (FFPI) developed by the authors consists of a single monomode fiber with dielectric-coated high-reflectance end faces, not with butt-coupled mirrors used by other authors [6], [7]. FFPI has many attractive features not only as the spectrum analyzer, but also the interferometric fiber sensor. In this paper, experimental and theoretical studies of FFPI made by the present authors are presented. In Section II, basic properties of FFPI are investigated. In Section III, thermal characteristics of FFPI are studied. In Section IV, FFPI's are applied to the sensor of temperature, vibration, acoustic wave, voltage, and magnetic field.

## II. BASIC PROPERTIES OF FFPI
A FFPI is schematically shown in Fig. 1. Two end faces of a monomode fiber are optically polished and coated with the multilayer of dielectric films by the vacuum evaporation method. The monomode fiber used consists of a $4\ \mu$m diam eter silica core and a $125\ \mu$m diameter silica cladding, covered with a 0.9 mm outer diameter nylon jacket. The optical loss of the fiber is 7.5 dB/km at a wavelength $\lambda$ of 633 nm. FFPI has a 30 mm long metal sleeve on each end part, but is equipped with no mode stripper. Fig. 2 shows the experimental setup. The light source is an internal mirror He-Ne ($\lambda = 633$ nm) laser, normally operated at two axial modes with a frequency separation of 640 MHz. The output power is 2.4 mW. The two lasing modes are linearly polarized but have orthogonal azimuths to each other. Using the polarization properties, the laser frequency is stabilized by a method described in [9]. The single mode laser light or the two-mode laser light with an arbitrary mode-intensity ratio was obtained by passing the output laser light through a suitably oriented polarizer. The laser light is passed through a 20X microscope objective and injected into FFPI. In order to avoid the undesirable optical coupling between FFPI and the laser cavity, the incident light was somewhat defocused from the end face of FFPI; thereby the laser instability caused by the optical coupling could be smaller than 1 percent. Part of FFPI, typically 5 cm lengths, was wound about a 100 mm diameter and 15 mm thick piezoelectric transducer (PZT) driven by 50 Hz sinusoidal voltages. The fiber length is then modulated, so FFPI operates as a scanning Fabry-Perot interferometer. The use of FFPI as the spectrum analyzer has also been very recently reported by [7]. A number of FFPI's are studied as parameters of fiber length $L$ of 1 cm to 100 m and end reflectance $R$ of 60-90 percent. Fig. 3(a)-(c) shows the light intensity transmitted through three different FFPI's, where the incident light is the single mode. The horizontal axis $\delta$ represents the phase delay which the fiber mode undergoes per pass through FFPI and is given by
$$\delta = kL \approx 2\pi nL/\lambda \tag{1}$$
where $k$ is the phase velocity of the fiber mode and $n$ is the refractive index of silica, equal to 1.46. Successive peaks of the transmission curves occur at $\delta = m\pi$, $m$ being integers. Fig. 4 shows the output mode patterns of some FFPI's. The output mode pattern involves more or less the speckle pattern, which stems from the cladding mode. As is seen from Fig. 4,

![](./images/812353353873883136_1.jpg)
Fig. 1. Geometry of fiber-optic Fabry-Perot interferometer (FFPI).

Manuscript received March 9, 1982; revised June 4, 1982.
T. Yoshino and T. Ose are with the Institute of Industrial Science, University of Tokyo, Roppongi, Minato-ku, Tokyo 106, Japan.
K. Kurosawa is with the Tokyo Electric Power Corporation, Ltd., Tokyo, Japan.
K. Itoh is with the Furukawa Electric Corporation, Ltd., Chiba, Japan.

0018-9197/82/1000-1624$00.75 © 1982 IEEE

![](./images/812353353873883136_2.jpg)

Fig. 2. Experimental setup for FFPI.

![](./images/812353353873883136_3.jpg)

Fig. 3. Output light intensity $I$ of scanning FFPI. $\delta$ represents the phase delay due to single pass through FFPI.

![](./images/812353353873883136_4.jpg)

(a) L=24cm, R=60% (b) L=1m, R=80% (c) L=100m, R=70%

Fig. 4. Output pattern of FFPI.

the speckle pattern component is generally larger for shorter FFPI. The speckle component involved in the output light intensity gives a bias in the transmission curve. In order to represent the transmission characteristics of FFPI without being affected by such spurious bias levels, we introduce an effective finesse $\mathfrak{F}_{e}$, defined as

$$
\mathfrak{F}_{e}=\pi / \Delta \delta \tag{2}
$$

where $\Delta \delta$ represents the full-width of $\delta$ yielding half the peak-to-peak transmittance (not half the maximum transmittance in the conventional definition [10]), as shown in Fig. 5. Theoretically, the transmittance of FFPI is given by

$$
\tau=1 /\left(1+F \sin ^{2} \delta\right) \tag{3}
$$

in accordance with the conventional etalon [10]. Here

$$
F=4 R /(1-R)^{2}. \tag{4}
$$

Considering that $\tau_{\max }=1$ and $\tau_{\min }=1 /(1+F)$, it can be shown that

$$
\mathfrak{F}_{e}=(\pi / 2) / \sin ^{-1}(1 / \sqrt{F+2}). \tag{5}
$$

![](./images/812353353873883136_5.jpg)

Fig. 5. Relationship for representing effective finesse $\mathfrak{F}_{e}$ of FFPI.

The free-spectral range of FFPI is, from (1), given by

$$
\Omega_{f} \approx c /(2 n L), \tag{6}
$$

$c$ being the light velocity in vacuum. Since the linewidth of the single mode of the He-Ne laser is as small as 2 kHz [11], the transmission curves as shown in Fig. 3 may be considered as those for a perfectly monochromatic light. From the transmission curves as shown in Fig. 3, the effective finesse $\mathfrak{F}_{e}$ was determined for various FFPI's. Some of the measured results are listed in Table I, together with the theoretical values. Comparing the experimental and theoretical values of $\mathfrak{F}_{e}$, both are generally in fairly good agreement. In some of the fabricated FFPI's, however, the experimental values are a few times smaller than the theoretical ones. The most probable cause for this is that the end faces of such FFPI's are tilted to the fiber axis. In that case, the fiber mode which is internally reflected on the end face of the fiber, cannot perfectly couple with the fiber mode. Letting the tilt angle be $\theta$, the internal coupling efficiency, from the result for tilt losses in connecting fibers [12], is calculated to be

$$
\eta=1-K_{\theta}(2 n \theta / \sqrt{2 \Delta})^{2} \tag{7}
$$

where $\Delta=0.002$, which is the relative refractive index difference between the core and the cladding, and $K_{\theta}=1.8$, which is the angular loss coefficient. If the coupling efficiency is $\eta$, the end reflectance of the fiber effectively becomes $\eta R$. In order to achieve $\eta=0.9$, it is required from (7) that the tilt angle $\theta$ should be smaller than $0.29^{\circ}$, the fulfillment of which is not technically difficult. It should be noted that, in the present experiment, no particularly exact polishing was conducted so as to make the tilt angle as small as possible. The effective values of end reflectance $R_{e}$ were also calculated by corresponding the measured $\mathfrak{F}_{e}$ values to the theoretical ones given by (5) and the results are also shown in Table I for comparison. In general, in the conventional Fabry-Perot interferometer or etalon, the tilt of the reflection surface causes the light beam to walk off the interferometer during the multiple passes through the interferometer, thereby causing the walk-off loss of light power. This walk-off loss is a very serious problem in the conventional form of Fabry-Perot interferometer. The walk-off loss increases with an increase in the interferometer length, so that long-distance Fabry-Perot interferometers, say longer than several meters, are hardly possible to construct. On the contrary, in FFPI, owing to the light trapping capability of optical fibers, there exists no walk-off loss; the presence of the tilt of the reflection surfaces simply reduces the effective end reflectance. As a consequence, it is much easier to fabricate FFPI than to construct the conventional form of Fabry-Perot interferometer. The spectral resolution of FFPI is given by $\Omega_{f} / \mathfrak{F}_{e}$ and increases with increasing $\Omega_{f}$ if $\mathfrak{F}_{e}$ is constant. For the 100 m

<table>
<caption>TABLE I Characteristics of FFPI</caption>
<thead>
<tr>
<th>FFPI<br>length L</th>
<th>Surface<br>reflectance R</th>
<th colspan="2">Effective<br>finesse $\mathcal{F}_e$</th>
<th>Effective<br>reflectance Re</th>
<th>Free-spectral<br>range $\Omega_f$</th>
</tr>
<tr>
<th></th>
<th></th>
<th>Exp.</th>
<th>Theo.</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>0.01m</td>
<td>90%</td>
<td>20</td>
<td>29</td>
<td>85%</td>
<td>1GHz</td>
</tr>
<tr>
<td>0.24m</td>
<td>80%</td>
<td>10</td>
<td>14</td>
<td>71%</td>
<td>0.43GHz</td>
</tr>
<tr>
<td>1.0m</td>
<td>80%</td>
<td>13</td>
<td>14</td>
<td>77%</td>
<td>103MHz</td>
</tr>
<tr>
<td>10m</td>
<td>80%</td>
<td>6</td>
<td>14</td>
<td>54%</td>
<td>10MHz</td>
</tr>
<tr>
<td>100m</td>
<td>70%(59%)</td>
<td>3</td>
<td>9(6.3)</td>
<td>28%</td>
<td>1MHz</td>
</tr>
</tbody>
</table>

The number in the parentheses represents the theoretical value taking into consideration the optical transmission loss in fiber.

FFPI shown in Table I, $\Omega_f = 1$ MHz and $\mathcal{F}_e = 3.3$, so that the spectral resolution is as high as about 300 kHz. Such a high spectral resolution is mainly owing to the very small free-spectral range of the FFPI. Fig. 6(a) and (b) shows the transmission curves in the cases that the input light involves two axial modes $f_1$ and $f_2$ $(f_1 - f_2 = 640$ MHz) with different intensity ratios. The transmission curve is given by the two independent transmission curves corresponding to each mode $f_1,f_2$.

The polarization properties are also studied. Generally, a monomode fiber, when placed in a coil form without twisting, has linear birefringence. Therefore, a coiled FFPI has the eigenstate of polarization consisting of orthogonal linear polarizations; their azimuths of polarization are either parallel or orthogonal to the plane where the fiber is placed. Each polarization mode has different phase velocity. Fig. 7 shows the light intensity transmitted through the 1 m FFPI ($R =$ 80 percent) when two polarization modes $s$ and $p$ are simul-taneously excited. It was achieved by passing the input light through a $45^\circ$ polarizer. The input light is the single mode in Fig. 7(a) but is the two modes in Fig. 7(b). In the latter case, the transmission curve is given by the superposition of four dif-ferent curves corresponding to the four combinations of two polarization modes $s$ and $p$ and two frequency modes $f_1$ and $f_2$. Naturally, such polarization-related complexity of the transmission characteristics of FFPI can be eliminated by using the polarization-maintaining fiber for the etalon fiber.

From the above study, it has been verified that 1) FFPI can have high finesse, 2) FFPI makes it possible to achieve very long distance Fabry-Perot interferometer, thereby achiev-ing very high spectral resolution, 3) FFPI requires much less precision for the tilt angle of the reflection surface than the conventional form of Fabry-Perot interferometer or etalon, and 4) FFPI is particularly well suited for a scanning Fabry-Perot interferometer because the optical path length in fiber can be readily modulated by appropriate external perturba-tions such as mechanical forces or temperature.

![](./images/812353353873883136_6.jpg)

Fig. 6. Output light intensity $I$ of scanning FFPI in the case that input light involves two modes $f_1$ and $f_2$ $(f_1 - f_2 = 640$ MHz).

![](./images/812353353873883136_7.jpg)

Fig. 7. Output light intensity $I$ of scanning 1 m FFPI ($R = 80$ percent) in cases where input light involves single frequency but two polariza-tion modes $s$ and $p$, (a), and two frequencies $f_1$ and $f_2$ and two polarization modes $s$ and $p$, (b).

### III. THERMAL CHARACTERISTICS OF FFPI

The temperature characteristics of FFPI are important for the practical use of it. The temperature induced phase shift in FFPI was measured with an FFPI of $L = 24$ cm ($R = 60$ percent). In order to prevent the undesirable effect of mechanical vibrations, the FFPI was inserted into a hollow glass tube of 19 cm length and 3 mm inner diameter. The glass tube was slowly heated or cooled by blowing hot or cool air on it. The output light intensity from the FFPI then changed with time as shown in Fig. 8(a); the input laser light is the single mode. One interference fringe or pulse cor-responds to the change of $\lambda/2$ in the optical path length of FFPI. When the FFPI was cooled from 65 to $30^\circ$C, the number of pulses was counted as a function of the fiber tem-perature change $\Delta T$, which was monitored by a thermistor

![](./images/812353353873883136_8.jpg)

Fig. 8. Output light intensity $I$ of 24 cm FFPI ($R = 60$ percent) when it was heated or cooled; input light is (a) single mode and (b) two modes.

![](./images/812353353873883136_9.jpg)

Fig. 9. Number of light pulses counted as a function of temperature change of 19 cm lengths of FFPI.

probe placed inside the glass tube. Fig. 9 shows the measured results, together with the experimental scheme. From Fig. 9, the average temperature sensitivity of the FFPI is obtained as $S_{jacket}(\text{pulse})=100/^\circ\text{C}\cdot\text{m}$, which yields the temperature sensitivity in the relative phase shift as $S_{jacket}(\text{phase})=\Delta\phi/(\phi\Delta T)=2.2\times10^{-5}/^\circ\text{C}$, where $\phi=nL$. Similar experiments were done in the case that the FFPI was unjacketed. The measured temperature sensitivity is $S_{unjacket}(\text{pulse})=36/^\circ\text{C}\cdot\text{m}$, yielding $S_{unjacket}(\text{phase})=7.9\times10^{-6}/^\circ\text{C}$. Thus, the temperature sensitivity for jacketed fibers is by a factor of 2.8 larger than that for unjacketed ones. Similar results have been recently reported [13], [14].

Theoretical considerations of the temperature sensitivity are done on a simple model. The fiber is composed of the core and the cladding with typically similar properties of silica, the cushion layer made of silicone, and the nylon jacket. The parameters of each component are listed in Table II. When the fiber system undergoes a temperature change of $\Delta T$, the following relative phase shift is induced in the core

$$
S(\text{phase})=\frac{\Delta\phi}{\phi\Delta T}=\frac{1}{n}\frac{\partial n}{\partial T}+\frac{(\Delta n)_{\text{strain}}}{n}+\frac{\Delta L}{L}
\tag{8}
$$

where $\Delta L$ is the net expansion of the fiber length. The quantity $(\Delta n)_{\text{strain}}$ represents the strain induced change in the refractive index of the core, which is, by an ordinary photoelastic calculation, shown to be

$$
(\Delta n)_{\text{strain}}=\frac{n^3}{2}\left[(p_{11}+p_{12})\nu-p_{12}\right]\sigma_1/E_1
\tag{9}
$$

where $p_{11}$ and $p_{12}$ are the photoelastic constants of silica and $\nu$ is Poisson's ratio; $\sigma_i$ and $E_i(i=1,2,3)$ are, respectively, the axial stress and Young's modulus of each fiber component numbered in Table II. Assuming that all the fiber components are uniformly deformed without slip at the boundaries, it follows that

$$
\Delta L/L=\alpha_i+\sigma_i/E_i\quad(i=1,2,3)
\tag{10}
$$

under

$$
\sum_{i=1}^{3}\sigma_iS_i=0
\tag{11}
$$

where $\alpha_i$ and $S_i$ are the linear expansion coefficient and cross-sectional area of each fiber component, respectively. Using (10), (11),

$$
\sigma_1=(\beta-\alpha_1)E_1
$$

where

$$
\beta=\frac{\Delta L}{L}=\sum_{i=1}^{3}(\alpha_iE_iS_i)\bigg/\sum_{i=1}^{3}(E_iS_i).
\tag{12}
$$

Hence, (8) becomes

$$
\begin{aligned}
S(\text{phase})=\frac{1}{n}\frac{\partial n}{\partial T}+\frac{n^2}{2}\left[(p_{11}+p_{12})\nu-p_{12}\right](\beta-\alpha_1)+\beta
\\
\tag{13}
\end{aligned}
$$

which is in substantial accordance with the result in [14], neglecting tensor relations among the stresses and strains.

The numerical values of $E_iS_i$ and $\alpha_iS_iE_i$ are also shown in Table II. The numerical calculation of (12) gives

$$
\begin{aligned}
S_{jacket}(\text{phase})&=[(0.076)+(-0.014)+(0.24)]\times10^{-4}/^\circ\text{C}
\\
\tag{14a}
\\
&=3.0\times10^{-5}/^\circ\text{C}.
\\
\tag{14b}
\end{aligned}
$$

Each parenthesis in (14a) corresponds to each term in (8). It is seen from (12) and (13) that $S$ depends on the parameters of the silicone layer and nylon jacket through $\beta$, which depends on $E_iS_i$ and $\alpha_iE_iS_i$. As is seen in Table II, $E_1S_1$ and $E_3S_3$ have comparable magnitudes to each other, but are much larger than $E_2S_2$; in addition, $\alpha_2E_2S_2\ll\alpha_1E_1S_1$ or $\alpha_3E_3S_3$. Consequently, the effect of the silicon cushion layer on $S$ is negligibly small. The calculated value of $S_{jacket}(\text{phase})$ of $3.0\times10^{-5}/^\circ\text{C}$ agrees fairly well with the measured result of $2.2\times10^{-5}/^\circ\text{C}$. The calculated value of $S_{unjacket}(\text{phase})$ is $8.0\times10^{-6}/^\circ\text{C}$, which agrees well with the measured value of $7.9\times10^{-6}/^\circ\text{C}$.

## IV. APPLICATION OF FFPI TO FIBER SENSORS

### A. Temperature

The temperature change can be measured by counting the number of pulses as shown in Fig. 8(a), where one pulse corresponds to the temperature change of $0.04^\circ\text{C}$. For the practical temperature sensor, it must be distinguished whether temperature is rising or falling. In order to supply this ability for FFPI, the two-mode laser light was used as the input light. Fig. 8(b) shows the output light signal in that case. The output signal involves two peaks, in one period, corresponding to the two mode input whose intensity ratio is $5:1$ in this case.

<table><thead><tr><th></th><th>Diameter d (mm)</th><th>Young's Modulus E ($10^{8}$N/$m^{2}$)</th><th>Cross-section S ($mm^{2}$)</th><th>Linear expansion coeff. $\alpha$ ($10^{-4}$/$^\circ$C)</th><th>ES ($10^{2}$N)</th><td>$\alpha$ES ($10^{-2}$N/$^\circ$C)</td></tr></thead><tbody><tr><td>1. Core and cladding (Silica)</td><td>0.125</td><td>730</td><td>0.012</td><td>0.004</td><td>8.8</td><td>0.035</td></tr><tr><td>2. Cushion layer (Silicone)</td><td>0.4</td><td>0.01</td><td>0.11</td><td>2.5</td><td>0.0011</td><td>0.0028</td></tr><tr><td>3. Jacket (Nylon)</td><td>0.9</td><td>5.5</td><td>0.52</td><td>1</td><td>2.8</td><td>2.8</td></tr></tbody></table>

$\partial n/\partial T$=$1.1$$\times$$10^{-5}$/$^\circ$C, $p_{11}$=0.121 , $p_{12}$=0.270, $\nu$=0.17

![](./images/812353353873883136_10.jpg)

It is manifested in Fig. 8(b) that the order in which the two peaks appear is reversed between whether the temperature is rising or falling, i.e., the optical path length of FFPI is increas- ing or decreasing. Using this phenomenon, the direction of temperature change can be discriminated.

Since the nylon-jacketed FFPI with a length $L(m)$ has the temperature sensitivity-in-pulse-number of $100\ L/^\circ$C as shown in Section III, very high temperature sensitivities can be ob- tained with long FFPI. This was demonstrated by some experiments. Fig. 10(a) shows the output light signal when a human came near a 10 m long FFPI ($R$ = 70 percent), which was coiled in 10 turns; the input light is the two-mode. The fiber temperature was then changed by the termal radiation from the human body and convection. Fig. 10(b) shows the output light signal in the case where a human hand was made close to the FFPI; in this case, the fiber was most dominantly heated by the thermal radiation. It is clearly seen in both figures that small temperature changes caused by the human body were very sensitively and quickly detected by the FFPI. The pulse height reduction seen in Fig. 10 is only apparent, stemming from the relatively slow response of the pen recorder. Fig. 11 shows the output light signal in the case where a human hand was made near the 100 m FFPI coiled in 100 turns. The output signal was recorded with a memory scope. In the FFPI, if the temperature change is uniform over the entire length of it, one pulse of the light signal corresponds to a temperature change as small as $0.1\ m\cdot^\circ$C. Such a high temperature sensitivity is an attractive feature of a long FFPI and would find interesting applications.

![](./images/812353353873883136_11.jpg)

Fig. 10. Output light intensity $I$ of 10 m FFPI ($R$ = 70 percent) subject to temperature changes (pen recorder output); input light is two modes.

![](./images/812353353873883136_12.jpg)

Fig. 11. Output light intensity $I$ of 100 m FFPI ($R$ = 70 percent) subject to temperature change (oscilloscope trace); input light is single mode.

The thermal response time of FFPI is one important factor for the temperature sensor. The thermal response time of a cylinder structure, defined by the time required for attaining to $1/e$ of the initial temperature difference, is given by $\tau_{h} = 0.12a^{2}\rho C/K$ [15], where $a$, $\rho$, $C$, and $K$ are the radius, density, specific heat, and thermal conductivity of the cylinder, respec- tively. For a silica cylinder with $2a = 125\ \mu$m, as $\rho = 2.22\ g/$ cm$^{3}$, $C = 0.20\ cal/g\cdot^\circ$C, and $K = 3.5\times 10^{-3}\ cal/cm\cdot s\cdot^\circ$C, $\tau_{h}$ is calculated to be 0.6 ms, which is very small. The re- sponse time of the jacketed fiber can be reasonably approxi- mated by that of a nylon cylinder of $2a = 0.9$ mm. As for nylon, $\rho = 1.12\ g/cm^{3}$, $C = 0.46\ cal/g\cdot^\circ$C, and $K = 5.2\times 10^{-4}$ $cal/cm\cdot s\cdot^\circ$C, $\tau_{h}$ is calculated to be 0.2 s, which is also suf-

ficiently small for most practical use for a temperature sensor.
Since the optical path length in fiber is sensitive to mechanical
vibration, FFPI as a temperature sensor has to be sufficiently
well isolated from the ambient mechanical vibration.

### B. Mechanical Vibration
Because FFPI has no reference arm in itself, FFPI can be not
only a simple, but also a reliable, fiber sensor for vibrations.
The 10 m FFPI ($R = 70$ percent) was placed in a coil on an
optical bench. An impact was given to the bench. Fig. 12
shows the output light signal. In this case, the impact was so
strong that phase modulation of several $\pi$ was induced in the
fiber. Fig. 12(a) and (b) corresponds to the cases that the
input light is the single mode and two modes with an intensity
ratio of $5:1$, respectively. In the latter case, the output signal
has an asymmetrical structure consisting of two peaks with
different heights as shown in Fig. 12(b). From the order in
which the two peaks appear, it can be discriminated whether
the fiber is expanding or contracting. The change in the
ambient temperature drifts the point of operation of FFPI.
This is, however, not a significant problem if the vibration
amplitude is large enough to cause the phase modulation
larger than $\pi$, which is the case in most practical measurements
of vibration.

![](./images/812353353873883136_13.jpg)

Fig. 12. Output light intensity $I$ of 10 m FFPI ($R = 70$ percent) subject
to mechanical vibrations in cases that input light is (a) single mode
and (b) two mode.

### C. Acoustic Wave
The acoustic sensitivity of FFPI is proportional to the fiber
length. The 100 m FFPI was placed on a metal plate in a
coil of 30 cm diameter. Acoustic waves of different fre-
quencies of $f_A = 1$ kHz, 5 kHz, and 10 kHz, were radiated on
the metal plate. Fig. 13(a)-(c) shows the corresponding
output signals; the input light is the single mode. The opera-
tion point was located near the middle between the maximum
and minimum transmittance of the FFPI. The incident
acoustic pressure was 0.1 Pa in amplitude. The phase modu-
lation induced in the fiber was about $\pi/8$ in amplitude. The
corresponding sensitivity was about 4 rad/Pa. This sensi-
tivity is one to two orders of magnitude greater than that
by the free jacketed fiber [16], [17]. This is because the
fiber was placed on the metal plate, which acted as a resonator
and enhanced the acoustic vibration of the fiber. The opera-
tion point of the FFPI, however, drifted naturally. The stabili-
zation of the operation point required a suitable feedback
system as mentioned below. Fig. 14(a) and (b) shows the out-
put signals in the cases that two human hands were clapped
at distances of 1 m and 10 m from the FFPI, respectively. It
is demonstrated that the FFPI can detect acoustic signals
with high sensitivity.

![](./images/812353353873883136_14.jpg)

Fig. 13. Output light intensity $I$ of 100 m FFPI ($R = 70$ percent)
subject to acoustic waves of various frequencies.

![](./images/812353353873883136_15.jpg)

Fig. 14. Output light intensity $I$ of 100 m FFPI ($R = 70$ percent)
subject to sounds generated by clapping.

An attractive use of FFPI is to exploit its high finesse, i.e.,
its sharp transmission characteristics. In general, the sensi-
tivity of the Fabry-Perot interferometer is proportional to
$d\tau/d\delta$. It can be derived from (3) that if $F \gg 1$, the sensi-
tivity takes its maximum value of $0.65\sqrt{F}$ at $\delta = \pm 1/\sqrt{3F}$
(mod. $\pi$), i.e., at the point of $\tau = 75$ percent. This maximum
sensitivity is by a factor of about $1.3\sqrt{F}$ larger than the sensi-
tivity with a two-beam interferometer such as the Mach-
Zehnder interferometer. A fiber-optic microphone system
using FFPI was constructed as shown in Fig. 15(a). The 1
m FFPI ($R = 80$ percent) of Fig. 3(a) was employed for the
sensor. In order to set the operation point at the steepest
slope of the transmission curve, the following servo system was
employed. The output light intensity of the FFPI was passed
through a low-pass filter $LF$ and compared, in a differential
amplifier DA, with a constant voltage $V_o$ corresponding to the
point to which operation point should be stabilized [see Fig.
15(b)]. The differential signal was then fed, through a power
amplifier $PA$, to the voice coil for driving a speaker cone. A
part of the FFPI was attached on the cone so that the fiber
length could be modulated by the displacement of the cone.
By this servo system, the temperature-induced phase shift in

![](./images/812353353873883136_16.jpg)

![](./images/812353353873883136_17.jpg)

![](./images/812353353873883136_18.jpg)

![](./images/812353353873883136_19.jpg)

![](./images/812353353873883136_20.jpg)

Fig. 15. Optical microphone system using FFPI: (a) entire system, (b) operation scheme (I output light signal), (c) stabil-
ized result, (d) output light signal for the incidence of sinusoidal acoustic waves, (e) output signal for the incidence of
vowels.

the fiber was compensated so that the operation point was stabilized to the steepest slope of the transmission curve of Fig. 15(b). Fig. 15(c) shows the typical result of stabilization. Somewhat intensity fluctuation involved in the stabilized re- sult is attributed to the ambient acoustic noise. In order to increase the acoustic sensitivity, the acoustic wave was inci- dent on the speaker cone, on which the FFPI was attached. Fig. 15(d) shows the output light signal of the FFPI for the incidence of sinusoidal acoustic waves with different fre- quencies. The modulation depth of the output light signal was about 20 percent of the peak-to-peak transmittance of the FFPI. Good linearity is obtained between the input acoustic wave and the output light signal. Fig. 15(e) shows the output light intensity of the FFPI for the incidence of the vowels generated by a man. The modulation depth of the output light was typically 20 percent. The frequency spec- trum of each vowel pattern shown in Fig. 15(e) accords well with the well-known formant. By means of this microphone system, human voice would be well regenerated through a loud speaker LS. In this FFPI, since $R_e=77$ percent (see Table I), the sensitivity enhancement factor of $1.3\sqrt{F}$ is 9.9. The minimum detectable phase shift by using the FFPI scheme

is proportional to the above sensitivity enhancement factor but also depends on the light transmittance [6]. Concerning this, more detailed experimental study is demanded. One great advantage of using FFPI as an acoustic sensor is that it requires no reference arm and so it is free from any spurious signals associated with the reference arm.

### D. Voltage
By the pulse counting method, ac electric voltages were measured. The measurement scheme is substantially the same as shown in Fig. 2. A part of FFPI was attached on PZT's as illustrated in Fig. 17(a) and (b). Fig. 16 shows the typical output signal when 50 Hz voltages were applied to the PZT of Fig. 17(a). Many light pulses were generated even for relatively low voltages. The pulse number was counted with an electronic counter. Fig. 17(a) and (b) shows the counted pulse number $N$ as a function of the applied 50 Hz voltage $V_{\text{ac}}$. By using these $V_{\text{ac}}$ - $N$ curves, the ac electric voltages can be optically measured. In the case of Fig. 17(b) in particular, $N$ is proportional to $V_{\text{ac}}$, which is favorable for voltmeter. The frequency characteristic of this voltmeter is directly related to that of PZT. The PZT's used in Fig. 17(a) and (b) have the resonance frequencies of 1 kHz and 92 kHz, respectively. The measurement sensitivity of the voltmeter increases around the resonance frequency.

### E. Magnetic Field
Both ac and dc magnetic fields were measured by the pulse counting method. Fig. 18 shows the measurement system. The 10 m FFPI was wound about a magnetostrictive cylinder of ferrite, which has a hollow form of 4 cm inner diameter, 5.5 cm outer diameter, and 8 cm length. The magnetic fields were generated by a coil placed in front of the magnetostrictive cylinder, and was applied to the cylinder in its axial direction. Fig. 19 shows the typical output light signal when 50 Hz magnetic fields were applied to the cylinder; the input light was the single mode. It is observed in Fig. 19 that the modulation of the output light intensity becomes small around the zero levels of applied fields. This corresponds to the fact that the magnetostriction is an even function of the applied magnetic field. The number of the light pulses generated was measured as a function of the amplitude of the applied 50 Hz magnetic field $H_{\text{ac}}$ and is shown in Fig. 20 by the circles. The pulse number was changed by the additional application of dc magnetic fields. The dependence of the pulse number $N$ on dc magnetic field $H_{\text{dc}}$ was measured as a parameter of the amplitude of the 50 Hz magnetic field $H_{\text{ac}}$. The measured results are shown in Fig. 21 by the circles.

In Fig. 20 it is found that $N$ increases with an increase in $H_{\text{ac}}$, depending on its square. In Fig. 20, the solid line represents the calculated curve of $N = 1.6H_{\text{ac}}^{2}$. Good agreement is shown between the calculated and measured results. This indicates that, in the present case, the magnetostriction of the used magnetostrictive cylinder is proportional to the square of the applied magnetic field. Consequently, in the presence of both ac and dc magnetic fields, the magnetostriction is proportional to $(H_{\text{ac}} + H_{\text{dc}})^{2}$, and hence, for the modulation term in particular, to $H_{\text{ac}} \cdot H_{\text{dc}}$, if $H_{\text{dc}} \gg H_{\text{ac}}$. In Fig. 21, the solid lines represent the calculated curve of $N = 0.8\ H_{\text{ac}} \cdot H_{\text{dc}}$. Good agreement is obtained between the cal-

![](./images/812353353873883136_21.jpg)

Fig. 16. Output light intensity $I$ of 1 m FFPI ($R = 80$ percent) attached on PZT subject to 50 Hz voltage $V$.

![](./images/812353353873883136_22.jpg)

Fig. 17. Measured dependence of pulse number $N$ on PZT 50 Hz voltage $V_{\text{ac}}$.

![](./images/812353353873883136_23.jpg)

Fig. 18. Magnetic field measurement system using FFPI.

![](./images/812353353873883136_24.jpg)

Fig. 19. Output light intensity $I$ of 10 m FFPI wound about magnetostrictive cylinder subject to 50 Hz magnetic field $H$.

![](./images/812353353873883136_25.jpg)

Fig. 20. Measured and calculated dependence of pulse number $N$ on amplitude of 50 Hz magnetic field applied to the magnetostrictive cylinder $H_{\mathrm{ac}}$.

![](./images/812353353873883136_26.jpg)

Fig. 21. Measured and calculated dependence of pulse number $N$ on dc magnetic field applied to the magnetostrictive cylinder $H_{\mathrm{dc}}$ as a parameter of amplitude of 50 Hz magnetic field $H_{\mathrm{ac}}$.

culated and measured results except the region where $H_{\mathrm{dc}}$ is near $H_{\mathrm{ac}}$; in this region, the present calculation is invalid. The experimental results as shown in Fig. 21 make it possible to measure dc magnetic fields, which is generally difficult by the optical method.

In general, a digital sensing scheme undergoes the measurement error due to the quantization of a signal. The quantization error is significant for small signals because it increases in inverse proportionality to the number of generated pulses. Obviously, such quantization error can be decreased by increasing that part of FFPI which is attached on a PZT or a magnetostrictive material. Another useful approach to decreasing the quantization error is to scan the operation point across one or multiple periods of the pulse in such a way that one or multiple scans are involved in the measurement time but that the scanning speed is sufficiently slower than the modulation frequency of the signal. In the present measuring scheme using FFPI, such scanning action is actually, although not perfectly, performed by the naturally occuring temperature drift of the optical phase in fiber. The measurement error was typically ±3 percent or less in both the measurements of electric and magnetic fields.

## V. CONCLUDING REMARKS

The fiber-optic Fabry-Perot interferometer (FFPI) has been developed for the first time. It has been shown that FFPI can have high finesse. It has been shown that, unlike the conventional Fabry-Perot interferometer, FFPI is flexible, can be very long, requires relatively low precision of fabrication, and moreover, it can be readily scanned. The polarization and thermal characteristics of FFPI are investigated. It is shown both experimentally and theoretically that the temperature sensitivity of jacketed FFPI is about three times larger than the unjacketed one. FFPI has been applied to the sensors of temperatures, mechanical vibrations, acoustic waves, ac voltages, and ac and dc magnetic fields. The fiber-optic microphone system using FFPI is also constructed. The analog or digital sensing scheme has been applied for these purposes. It has been demonstrated that FFPI can achieve high sensing sensitivity by using its high finesse and/or by making its fiber length very long. Unlike the conventional fiber-sensor scheme using the Mach-Zehnder interferometer, FFPI has a very simple form, can easily produce the interferometric signal, and is free from the false signal due to the reference arm. Consequently, FFPI can be a very attractive interferometer not only as the spectrum analyzer but also as the interferometric fiber sensor.

### REFERENCES

[1] J. A. Bucaro, H. D. Darty, and E. F. Caron, "Optical fiber acoustic sensor," *Appl. Opt.*, vol. 16, no. 7, pp. 1761-1762, 1977.

[2] G. B. Hocker, "Fiber-optic sensing of pressure and temperature," *Appl. Opt.*, vol. 18, no. 9, pp. 1445-1448, 1979.

[3] A. Dandridge, A. B. Treven, G. H. Sigel, Jr., E. J. West, and T. G. Giallorenzi, "Optical fiber magnetic field sensors," *Electron. Lett.*, vol. 16, no. 11, pp. 408-409, 1980.

[4] A. Vali and R. W. Shorthill, "Fiber ring interferometer," *Appl. Opt.*, vol. 15, no. 5, pp. 1445-1448, 1979.

[5] T. Yoshino, "Fiber Fabry-Perot interferometers," in *Proc. 3rd Int. Conf. on Integrated Optics and Optical Fiber Commun.*, San Francisco, CA, Apr. 1981, paper WL2.

[6] S. J. Petuchowski, T. G. Giallorenzi, and S. K. Sheem, "A sensitive fiber-optic Fabry-Perot interferometer," *IEEE J. Quantum Electron.*, vol. QE-17, pp. 2168-2170, Nov. 1981.

[7] D. L. Franzen and E. M. Kim, "Long optical fiber Fabry-Perot interferometer," *Appl. Opt.*, vol. 20, no. 23, pp. 3991-3992, 1981.

[8] P. G. Cielo, "Fiber-optic hydrophone: improved strain and environmental noise protection," *Appl. Opt.*, vol. 18, no. 18, pp. 2933-2937, 1979.

[9] T. Yoshino, "Frequency stabilization of internal-mirror He-Ne ($\lambda = 633$ nm) lasers using the polarization properties," *Japan. J. Appl. Phys.*, vol. 19, no. 11, pp. 2181-2185, 1980.

[10] M. Born and E. Wolf, *Principles of Optics*, 2nd ed. Oxford: Pergamon, 1964, p. 327.

[11] P. J. Nagill and T. Young, "Measurement of He-Ne laser linewidth utilizing the Doppler effect," *Appl. Phys. Lett.*, vol. 5, no. 1, pp. 13-15, 1964.

[12] Y. Murakami, I. Hatakeyama, and H. Tsuchiya, "Normalized frequency dependence of splice losses in single-mode optical fibers," *Electron. Lett.*, vol. 18, no. 9, pp. 277-278, 1978.

[13] M. Tateda, S. Tanaka, and Y. Sugiyama, "Thermal characteristics of phase shift in jacketed optical fibers," *Appl. Opt.*, vol. 19, no. 5, pp. 770-773, 1980.

[14] N. Lagakos, J. A. Bucaro, and J. Jarzynski, "Temperature-induced optical phase shifts in fibers," *Appl. Opt.*, vol. 20, no. 13, pp. 2305-2308, 1981.

[15] H. S. Carslaw and J. C. Jager, *Conduction of Heat in Solids*, 2nd ed. Oxford: Clarendon, 1959, p. 230.

[16] G. B. Hocker, "Fiber-optic acoustic sensors with composite structures: An analysis," *Appl. Opt.*, vol. 18, no. 21, pp. 3674-3683, 1979.

[17] B. Budiansky, D. C. Drucker, G. S. Kino, and J. R. Rice, "Pressure sensitivity of a clad optical fiber," *Appl. Opt.*, vol. 18, no. 24, pp. 4085-4088, 1979.

![](./images/812353353873883136_27.jpg)
Toshihiko Yoshino was born in Tokyo, Japan, on April 27, 1939. He received the B.S., M.S., and Ph.D. degrees in applied physics from Tokyo University, Tokyo, Japan, in 1963, 1965, and 1968, respectively.

Since 1968 he has been with the Institute of Industrial Science, Tokyo University, where he has been engaged in research and education on optics. From 1971 to 1973 he was a Guest Researcher with the Technical University, Hannover, West Germany, where he worked on laser spectroscopy.

Dr. Yoshino is a member of the Japan Society of Applied Physics.

![](./images/812353353873883136_28.jpg)
Kiyoshi Kurosawa was born in Nagano Prefecture, Japan, on September 6, 1952. He received the B.E. degree in electrical engineering from Nihon University, Tokyo, Japan, in 1978 and graduated from the Department of Technology, University Course, Tokyo Electric Power Institute, Tokyo, Japan, in 1980.

Since 1971 he has been with the Tokyo Electric Power Corporation, Ltd., Tokyo, Japan, where he has been engaged in research and development in application of optics in electric power systems.

![](./images/812353353873883136_29.jpg)
Katsuji Itoh was born in Tokyo, Japan, on February 15, 1942. He received the B.S. and the M.S. degrees in electrical engineering from the Yokohama National University, Yokohama, Japan, in 1966 and 1968, respectively.

Since 1968 he has been with the Furukawa Electric Corporation, Ltd., Chiba, Japan, where he has been engaged in research and development in distribution and application of optics to high voltage.

Mr. Itoh is a member of the Institute of Electrical Engineers of Japan and the Japan Society of Applied Physics.

Teruzi Ose, photograph and biography not available at the time of publication.

