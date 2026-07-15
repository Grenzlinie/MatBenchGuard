Manufacturing tolerances for silver-sodium ion-exchange planar optical waveguides

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1978 J. Phys. D: Appl. Phys. 11 1567

(http://iopscience.iop.org/0022-3727/11/11/016)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.93.16.3
This content was downloaded on 06/09/2015 at 07:44

Please note that terms and conditions apply.

J. Phys. D: Appl. Phys., Vol. 11, 1978. Printed in Great Britain

# Manufacturing tolerances for silver-sodium ion-exchanged planar optical waveguides

CA Millar and RH Hutchins
Department of Electronics and Electrical Engineering, University of Glasgow,
Glasgow G12 8QQ

Received 18 November 1977, in final form 12 May 1978

Abstract. The variation of effective refractive index due to the manufacturing process is studied for silver-sodium ion-exchanged slab waveguides, and the results are related to a theoretical model which is derived from the linear refractive index profile. The consequences of the observed variability are considered for the fibre-film directional coupler and the three-dimensional silver-sodium ion-exchanged waveguide.

## Notation

| Symbol | Definition |
|--------|------------|
| $\lambda$ | wavelength of light $(=0.6328\ \mu\mathrm{m})$ |
| $n_{\mathrm{s}}$ | surface refractive index $(1.605)$ |
| $\Delta n_{\mathrm{s}}$ | change in surface refractive index $(=n_{\mathrm{s}}-n_{2})$ |
| $n_{2}$ | substrate refractive index $(=1.51625)$ |
| $n_{0}$ | superstrate refractive index $(=1.0)$ |
| $n(x)$ | refractive index profile in $x$-direction |
| $n_{\mathrm{e}}$ | effective mode index $=\beta/k$ |
| $k$ | $2\pi/\lambda$ |
| $k_{0}$ | $k(n_{\mathrm{e}}{}^{2}-n_{0}{}^{2})^{1/2}$ |
| $k_{\mathrm{s}}$ | $k(n_{\mathrm{s}}{}^{2}-n_{\mathrm{e}}{}^{2})^{1/2}$ |
| $m$ | mode order |
| $K$ | coupling coefficient for two transversely coupled optical waveguides |
| $d$ | profile depth parameter $(\mu\mathrm{m})$ |
| $d_{1}$ | waveguide depth in the linear approximation $(\mu\mathrm{m})$ |
| $t$ | diffusion time in minutes |
| $T$ | temperature (K) |
| $a$ | width of mask defining channel waveguides |

## 1. Introduction

Planar (Tien 1971) and stripe (Gallacher and De La Rue 1976) single-mode or quasi-single-mode optical waveguides are important in integrated optics for passive devices such as couplers and filters. There is considerable interest in waveguides formed by various types of diffusion processes including those formed by the migration of silver ions from a silver nitrate melt into a soda-lime glass. Silver-sodium ion-exchanged

0022-3727/78/0011-1567 $01.00 © 1978 The Institute of Physics

waveguides exhibit low optical loss of less than $1\ \text{dB}\ \text{cm}^{-1}$, and have been used to demonstrate efficient coupling between optical fibres and integrated optical circuits. A high degree of repeatability of effective refractive index is important in the batch manufacture of integrated waveguiding structures, which may have to be critically phase-matched to a predetermined figure. The ability to make small precise changes in the effective index of a given mode of the waveguide is of paramount importance when considering the velocity match to an incoming or outgoing fibre waveguide mode, or in the manufacture of narrow-band optical filters such as ring resonators and periodic grating devices.

It is the purpose of this paper to report the manufacturing tolerances required to attain a given degree of repeatability of effective refractive index for silver-sodium ion-exchanged waveguides, and the methods employed to do so.

## 2. Silver-sodium ion-exchanged waveguides

### 2.1. Refractive index profile

With a non-destructive optical technique (Stewart *et al* 1977) the refractive index profile of the silver-sodium ion-exchanged waveguide has been found to follow a quadratic variation with depth into the substrate glass as

$$
\left.
\begin{aligned}
n(x) &= n_{\mathrm{s}}-\Delta n_{\mathrm{s}}\left[\frac{x}{d}+b\left(\frac{x}{d}\right)^{2}\right] & & x<d_{1} \\
&=n_{2} & & x \geqslant d_{1}
\end{aligned}
\right\} \tag{1}
$$

where $b=0.64$, $x$ is the direction perpendicular to the surface of the glass, and $d$ is a constant which depends on the time and diffusion temperature. The graph of $n(x)$

![](./images/812686734440529921_1.jpg)

Figure 1. Second-order polynomial refractive index profile plotted against normalised depth.

against $x/d$ is shown in figure 1. The depth $d_1$ is defined by the condition

$$
\left[\frac{x}{d}+b\left(\frac{x}{d}\right)^{2}\right]_{x=d_{1}}=1 \tag{2}
$$

or

$$
d_{1}=0 \cdot 69273 d. \tag{3}
$$

The constant $d$ (in $\mu \mathrm{m}$) depends on the diffusion time $t$ (in min) and the melt temperature $T$ (in K) and is given by

$$
d=1 \cdot 19 \times 10^{4} t^{1 / 2} \exp \left(-1 \cdot 02 \times 10^{4} / 2 T\right). \tag{4}
$$

Equations (1) and (4) determine the refractive index profile $n(x)$ for any set of fabrication parameters $t$ and $T$. Equations (2) and (3) similarly determine the effective depth $d_1$.

### 2.2. Mode propagation
The general form of the eigenvalue equation for a monotonically decreasing refractive index profile is

$$
k \int_{0}^{a}\left(n^{2}(x)-n_{\mathrm{e}}^{2}\right)^{1 / 2} \mathrm{~d} x=\left(m+\frac{1}{4}\right) \pi+\tan ^{-1} \xi \frac{k_{0}}{k_{\mathrm{s}}} \tag{5}
$$

where

$$
\left.
\begin{array}{ll}
\xi=1 & \text { for TE modes } \\
\xi=\left(\frac{n_{\mathrm{s}}}{n_{0}}\right)^{2} & \text { for TM modes }
\end{array}
\right\}. \tag{6}
$$

The depth $a_{\mathrm{e}}$ is the WKB turning point defined by

$$
n\left(a_{\mathrm{e}}\right)=n_{\mathrm{e}}. \tag{7}
$$

From equation (1), since $\Delta n_{\mathrm{s}} / n_{\mathrm{s}}$ is small,

$$
n^{2}(x)=n_{\mathrm{s}}{ }^{2}-2 n_{\mathrm{s}} \Delta n_{\mathrm{s}}\left[\frac{x}{d}+b\left(\frac{x}{d}\right)^{2}\right]. \tag{8}
$$

Furthermore, it may be seen from figure 1 that a linear approximation

$$
n^{2}(x)=n_{\mathrm{s}}{ }^{2}-2 n_{\mathrm{s}} \Delta n_{\mathrm{s}} \frac{x}{d_{1}} \tag{9}
$$

is valid, where

$$
d_{1}=0.69273 d=8.243 \times 10^{3} t^{1 / 2} \exp \left(-1.02 \times 10^{4} / 2 T\right). \tag{10}
$$

Substituting equation (9) into equation (5) and integrating reveals the eigenvalue equation for the waveguide modes given by

$$
\frac{d_{1} k_{\mathrm{s}}{ }^{3}}{3 k^{2} n_{\mathrm{s}} \Delta n_{\mathrm{s}}}=\left(m+\frac{1}{4}\right) \pi+\tan ^{-1} \xi \frac{k_{0}}{k_{\mathrm{s}}}. \tag{11}
$$

## 3. Theoretical description of the temperature and time dependences of the effective refractive index

Both Wood (1976) and Stewart *et al* (1977) have shown that the refractive index profile of planar silver-ion exchanged waveguides in soda-lime glass microscope slides takes the form of a second-order polynomial distribution which is consistent with a model of the

process in which interdiffusion of silver and sodium ions takes place. This refractive index profile is the dominant factor determining the effective mode index, and the para- meters affecting the exchange process are, primarily, the composition of the host glass and the temperature and time of diffusion. The temperature and time dependencies of the effective refractive index may be found using Stewart's linear approximation to the characteristic equation governing propagation in the fundamental mode of a silver-sodium ion-exchanged waveguide:

$$
\frac{d_{1} k_{\mathrm{s}}{ }^{3}}{3 k^{2} n_{\mathrm{s}} \Delta n_{\mathrm{s}}}=\frac{\pi}{4}+\tan ^{-1}\left(\xi \frac{k_{0}}{k_{\mathrm{s}}}\right). \tag{12}
$$

Differentiating both sides of equation (12) gives

$$
\frac{\delta n_{\mathrm{e}}}{\delta d_{1}}=\frac{k_{\mathrm{s}}{ }^{4}}{3 k^{4} n_{\mathrm{s}} \Delta n_{\mathrm{s}}\left\{\left(n_{\mathrm{e}} / k_{0}\right) \xi\left[1+\left(k_{0} / k_{\mathrm{s}}\right)^{2}\right]\left[1+\left(\xi k_{0} / k_{\mathrm{s}}\right)^{2}\right]^{-1}+3 / k_{\mathrm{s}}\right\}}. \tag{13}
$$

Using equation (10) we obtain

$$
\delta n_{\mathrm{e}}(t)=\frac{\alpha}{t} \delta t \tag{14}
$$

$$
\delta n_{\mathrm{e}}(T)=\frac{1 \cdot 02 \times 10^{4} \alpha}{T^{2}} \delta T \tag{15}
$$

where

$$
\alpha=\frac{k_{\mathrm{s}}{ }^{4} d_{1}}{6 k^{4} n_{\mathrm{s}} \Delta n_{\mathrm{s}}\left\{\left(n_{\mathrm{e}} / k_{0}\right) \xi\left[1+\left(k_{0} / k_{\mathrm{s}}\right)^{2}\right]\left[1+\left(\xi k_{0} / k_{\mathrm{s}}\right)^{2}\right]^{-1}+3 / k_{\mathrm{s}}\right\}}. \tag{16}
$$

The functions $\delta n_{\mathrm{e}}(t) / \delta t$ and $\delta n_{\mathrm{e}}(T) / \delta T$ are plotted against $n_{\mathrm{e}}$ in figure 2, and are for the $\mathrm{TE}_{0}$ mode in waveguides manufactured at process temperatures, $217\ ^{\circ}\mathrm{C}$, $250\ ^{\circ}\mathrm{C}$ and $300\ ^{\circ}\mathrm{C}$. This range of temperature covers most of the working spectrum of the process. Clearly the effect on $n_{\mathrm{e}}$ of variations of operating temperature between samples is not very

![](./images/812686734440529921_2.jpg)

Figure 2. The functions $\delta n_{\mathrm{e}}(t) / \delta t$ and $\delta n_{\mathrm{e}}(T) / \delta T$ plotted against effective index (TE₀ mode), for $T=217\ ^{\circ}\mathrm{C}, 250\ ^{\circ}\mathrm{C}, 310\ ^{\circ}\mathrm{C}$.

dependent on the operating temperature as $\delta n_{\mathrm{e}}(T) / \delta T$ only varies between $1 \times 10^{-3}$ and $3 \times 10^{-3}$ over the entire range of effective mode index. It can be seen from figure 2 that if the maximum temperature error in $n_{\mathrm{e}}$ is limited, for example, to $3 \times 10^{-4}$ a temperature control of $\pm 0 \cdot 1{ }^{\circ} \mathrm{C}$ is imposed.

Changes in $n_{\mathrm{e}}$ due to variations of process time $\delta t$ are more dependent on the diffusion temperature to a few degrees above the melting point of the $\mathrm{AgNO}_{3}$. At $217^{\circ} \mathrm{C}$, a time control of $\pm 2 \mathrm{~s}$ is a necessary requirement to reduce the variation in $n_{\mathrm{e}}$ to $2 \times 10^{-4}$ for a single mode propagating near to optical cut-off. However, for well-guided single-mode or quasi-single-mode waveguides manufactured at temperatures slightly above the melting point, process time errors of the order of a few seconds may be considered negligible.

## 4. Batch manufacture of silver-sodium ion-exchanged waveguides

Silver-sodium ion-exchanged waveguides are manufactured by immersing the substrate material in a container of molten $\mathrm{AgNO}_{3}$ (commercial grade). The 18 in long horizontal tubular electrical furnace and silver nitrate container sketched in figure 3 were designed

![](./images/812686734440529921_3.jpg)

Figure 3. The design of the melt container, and the apparatus.

to minimise temperature gradients, and allow the substrate to reach equilibrium temperature with the silver nitrate bath prior to insertion in the melt. The temperature variations measured along the length of the bath was less than $0 \cdot 1{ }^{\circ} \mathrm{C}$, a figure supported by the observations that the waveguide mode indices were constant, within the measuring errors, along the length of the slide. The slide (Fisher glass, mean refractive index $=1 \cdot 51625$, at $\lambda=0.633 \mu \mathrm{m}$ ) was supported by two silica arms projecting from a silica rod, angular rotation of which inserted the hot slide into the bath (figure 3). The cleaning procedure for each slide consisted of a standard detergent wash, ultrasonic clean and alcohol

degrease. The slides were then air-dried in a dust-free atmosphere. Matched and cali- brated Chromel-Alumel thermocouples were used, one for the temperature control and the other for the monitoring system. Both were led to cold junctions at ice point, there- after by thick copper leads to the measuring instruments. The control voltage was com- pared to the set point voltage on a Wheatstone bridge (2 $\mu$V resolution, unaffected by ambient temperature drift), and the error signal was fed into the error input of a West three-term controller set to give optimum control conditions. A slide which had reached equilibrium temperature (the time to do so was about 10 min) was inserted into the melt and the temperature was controlled to within $\pm 0 \cdot 1$ °C over the entire process time. Samples were then withdrawn completely from the furnace and allowed to cool at room temperature, the time for the silver nitrate remaining on the sample surface to crystallise being approximately 3 s.

The control specification was independently verified by the monitoring thermocouple, which was connected to a high-input impedance digital voltmeter (Dana model 5370) reading to 1 $\mu$V. Recordings of the melt temperature fluctuations for each sample were made by extracting an analogue voltage from the digital voltmeter which was then fed into a DC amplifier and offset circuit to allow small variations of thermocouple voltage (of order $1\ \mu\text{V} \equiv 0.02\ ^\circ\text{C}$) to be displayed on a chart recorder.

## 5. Results

With the melt controlled to $\pm 0 \cdot 1$ °C at $217\ ^\circ\text{C}$ waveguides were manufactured in batches of 6, the process time varying between 5 and 140 min, in 15 min intervals. The system was then shut down, thoroughly recleaned, and the series of diffusions repeated in arbitrary time sequence. The mode angles were then measured and the effective refractive indices were calculated. The mean and sample standard deviation were calculated for each batch, and figure 4 shows the measured standard deviation plotted against the mean effective refractive index.

![](./images/812686734440529921_4.jpg)

Figure 4. The measured ($\bigcirc$) and expected ($-$) deviations for $T=217\ ^\circ\text{C}$. $\delta t=\pm 2$ s, $\delta T=\pm 0 \cdot 1$ °C.

The dashed lines in figure 4 represent the theoretical predictions of equations (14) and (15) with $\delta t_{\text{max}}=2$ s and $\delta T_{\text{max}}=0.1$ °C. The solid curve is constructed from the addition in quadrature of $\delta n_{\text{e}}(t_{\text{max}})$, $\delta n_{\text{e}}(T_{\text{max}})$ and $\delta n_{\text{e}}(\text{e})$, the latter being the combination of the estimated measurement error of $\pm 1.5'$ arc in angular measurement $(\pm 1.5\times 10^{-4}$ in $n_{\text{e}})$ and the standard deviation about the mean substrate refractive index. Changes in bulk refractive index between different manufacturing batches of substrate material may override the small changes in the index profile resulting from the time/temperature perturbations, therefore a single batch of Fisher glass slides was used throughout. The slides were measured on an Abbé refractometer and the standard deviation was found to be $\pm 1.1\times 10^{-4}$. The maximum resultant expected deviation $\delta n_{\text{e}}(\text{TOT})$ is given by

$$
\left[\delta n_{\text{e}}(\text{TOT})\right]^{2}=\left[\delta n_{\text{e}}(T_{\text{max}})\right]^{2}+\left[\delta n_{\text{e}}(t_{\text{max}})\right]^{2}+3.46\times 10^{-8}. \tag{17}
$$

For comparison, figure 4 also shows the measured standard deviations from the mean values of $n_{\text{e}}$ against the mean $n_{\text{e}}$. The measured values have deviations in the vicinity of the expected maxima. The observed variations can be attributed to known factors and it would appear that, within the bounds of experimental error and the known variation of the substrate glass, the waveguides are being manufactured to the best possible tolerances. It is thought that further efforts to control the time and temperature variability would result in little or no improvement in the repeatability of the guided mode index.

### 6. Effect of batch variability on the coupled-wave device

Since the variation of $n_{\text{e}}$ from one film to the next can be a source of a significant error in the manufacture of coupled-wave structures it is important to relate the batch variability to the efficiency of some passive devices. We shall consider, as an example, phase-matched directional coupling to an optical fibre.

In some circumstances a direct phase match between an incoming fibre mode and the integrated waveguide mode is required to achieve efficient and reciprocal coupling between the two, and where the fibre parameters are fixed, the match is normally introduced by altering the $n_{\text{e}}$ value of the ion-exchanged guide at the manufacturing stage (Millar and Laybourn 1976). The desired $n_{\text{e}}$ value is subject to the variation introduced by the ion-exchange process and therefore velocity matching is only accurate within the bounds of batch variability. If an optical directional coupler, designed with $Kz=\pi/2$ develops an error $\delta n_{\text{e}}$ during fabrication, then the efficiency of the power transfer from the initially-excited guide to the coupled guide is (Miller 1954)

$$
\eta=\frac{K^{2}}{\rho^{2}} \sin ^{2} \rho z \tag{18}
$$

where

$$
\rho=K\left[1+\left(\frac{k \delta n_{\text{e}}}{2 K}\right)^{2}\right]^{1 / 2}. \tag{19}
$$

It is clear from figure 4 that

$$
\delta n_{\text{e}}=f\left(n_{\text{e}}, \frac{\delta T}{T}, \frac{\delta t}{t}\right). \tag{20}
$$

The coupling coefficient $K$ can be plotted as a function of the maximum transfer efficiency

$$
\hat{\eta}=\left[1+\left(\frac{k \delta n_{\mathrm{e}}}{2 K}\right)^{2}\right]^{-1}
\tag{21}
$$

over the range of $n_{\mathrm{e}}$ for any set of fabrication conditions, and such a graph is shown in figure 5 for $\delta T / T$ and $\delta t / t$ as in figure 4. It is seen that the maximum transfer efficiency is greater than $3 \mathrm{~dB}$ for values of $K$ greater than $10^{4} \mathrm{~m}^{-1}$ over a significant range of $n_{\mathrm{e}}$,

![](./images/812686734440529921_5.jpg)

Figure 5. The maximum transfer efficiency of a directional coupler against system coupling coefficient for the effective indices and variations shown in figure 4.

the implication being that the probability of making an efficient film/fibre coupler is much reduced if the coupling coefficient is less than $10^{4} \mathrm{~m}^{-1}$. However, it has been shown that a well-guided single-mode coupling system can be made with a coupling coefficient of this order of magnitude, and indeed measured maximum transfers of $96 \%$ have been reported (Millar and Laybourn 1976), using silver ion exchange films which were manufactured in a batch process where the temperature and time controls were $\pm 0 \cdot 1{ }^{\circ} \mathrm{C}$ and $\pm 2 \mathrm{~s}$ respectively.

### 7. Tolerances for three-dimensional silver-sodium ion-exchanged waveguides

Extension of the results for two-dimensional (slab) waveguides to three-dimensional (channel) waveguides is difficult. However, it is known that effective indices, $n_{\mathrm{e}}(x)$ and $n_{\mathrm{e},}(y)$ can be associated with each of the two orthogonal transverse directions $x$ and $y$, which are related to the axial propagation constant $n_{\mathrm{e}}(z)$ by

$$
\left[n_{\mathrm{e}}(z)\right]^{2}=\left[n_{\mathrm{e}}(x)\right]^{2}+\left[n_{\mathrm{e}}(y)\right]^{2}-\left[n\left(n_{\mathrm{e}}(x), n_{\mathrm{e}}(y)\right)\right]^{2}
\tag{22}
$$

where $n$ will be a function of the channel waveguide refractive index profile defined by the aperture $a$ and the diffusion coefficients of the silver and sodium ions in the glass. Error terms $\delta n_{\mathrm{e}}(x)$ and $\delta n_{\mathrm{e}}(y)$ appear in the three components on the right of the equation and thus a realistic estimate of the term $\delta n_{\mathrm{e}}(z)$ is the addition in quadrature of the error terms on the right. Thus

$$
\left[\delta n_{\mathrm{e}}(z)\right]^{2}=\left[\delta n_{\mathrm{e}}(x)\right]^{2}+\left[\delta n_{\mathrm{e}}(y)\right]^{2}+\delta n^{2}.
\tag{23}
$$

Manufacturing tolerances for planar optical waveguides

Let us assume that, for a guide where $a$ and $d$ are of the same order of magnitude,

$$\delta n_{\mathrm{e}}(x) \sim \delta n_{\mathrm{e}}(y) \sim \delta n.\tag{24}$$

Thus

$$\delta n_{\mathrm{e}}(z) \sim \sqrt{ } 3 \delta n_{\mathrm{e}}(x).\tag{25}$$

A deviation from a set value of the axial propagation constant in a three-dimensional guide is approximately $\sqrt{ } 3$ times that of a two-dimensional guide of the same effective index. Hence we may predict that the average standard deviation which would result from the fabrication of single-mode stripe optical waveguides at the same temperature and time with equivalent tolerances used in section 4 would be about $7 \times 10^{-4}$. This simplistic analysis does not take into account any systematic uncertainties associated with the manufacture of three-dimensional guides, and it is prudent to allow an experimental standard deviation of $1 \times 10^{-3}$ in $n_{\mathrm{e}}$ for these stripe waveguides. Gallacher and De La Rue (1976) have shown that single-mode stripe waveguides can be manu- factured using silver-sodium ion exchange. The total available effective index change for the single $\mathrm{E}_{11}$ mode is between its optical cut-off (substrate bulk index) and the value of $n_{\mathrm{e}}$ at the cut-off of the next higher-order transverse mode, and has a value of approximately $3 \times 10^{-3}$. The manufacturing error within the control specification $\pm 0 \cdot 1{ }^{\circ} \mathrm{C}, \pm 2 \mathrm{~s}$, is approximately $1 \times 10^{-3}$, which is a significant proportion of this total range of $n_{\mathrm{e}}$ available for single-mode operation. We therefore predict that the increased fabrication error and the decrease in the effective index band for single-mode operation makes repeatable fabrication of the three-dimensional structures more difficult, unless a method of retarding the exchange process is found, for example by dilution of the silver ion in the melt. $\dagger$

### 8. Conclusions
The manufacturing tolerances required to obtain a high repeatability of effective refractive index for silver-sodium ion-exchanged waveguides have been investigated, and it has been found that the repeatability is best where the fabrication temperature is close to the melting point of the silver nitrate and is continuously within $\pm 0 \cdot 1{ }^{\circ} \mathrm{C}$ of the set value. At low temperatures, time errors of a few seconds are negligible except for guided mode velocities close to optical cut-off. The linear profile approximation provides a theoretical basis for the experimental results, and when the measurement and other errors are taken into account, it is seen that the theory and the experiment are in good agreement. The measured values of $n_{\mathrm{e}}$ have deviations in the vicinity of the expected maxima and show a deviation of about $4 \times 10^{-4}$ over a significant range of $n_{\mathrm{e}}$. Improvement in this figure of the measured standard deviation is thought unlikely using pure silver nitrate as the melt. The batch variability of coupled wave devices using silver-sodium ion-exchanged waveguides and external waveguides effectively imposes a restriction on the design of

$\dagger$ Stewart and Laybourn (1978) have found that dilution of the silver nitrate melt with sodium nitrate increases the melting point of the mixture and lowers the surface refractive index of the waveguide. To a first approximation the expression for $d_{1}$ (equation 10) and the profile shape remains the same, and therefore the theory outlined in section 2 is still applicable to the dilute melt situation. For example, we find that $\delta n_{\mathrm{e}}(T) / \delta T$ is more than an order of magnitude smaller for $n_{\mathrm{s}}=1 \cdot 526$ and $T=315^{\circ} \mathrm{C}$, than $\delta n_{\mathrm{e}}(T) / \delta T$ for the pure melt where $n_{\mathrm{s}}=1 \cdot 605$ and $T=215^{\circ} \mathrm{C}$. This prediction has been independently vrified by Stewart who reports excellent single-mode effective index repeatability with dilute silver nitrate melts, even with temperature variations greater than $\pm 1{ }^{\circ} \mathrm{C}$.

the coupling system since there is a minimum value of the coupling coefficient which permits efficient power transfer for every sample.

Extension of the results to three-dimensional waveguides shows that the increased manufacturing error and decreased effective index band for single mode operation combine to further lower the probability of obtaining a desired value of guided mode index.

One method which should significantly reduce the manufacturing tolerances reported here is the reduction of the concentration of silver ions in the melt, and for this dilute melt situation the theory predicts a virtual elimination of the error in effective mode index due to the manufacturing process.

## Acknowledgments

The authors would like to thank G Stewart and C D W Wilkinson for helpful discussions, and acknowledge the financial support of the UK Ministry of Defence, ASWE.

## References

Gallacher J G and De La Rue R M 1976 *Electron. Lett.* **12** 397

Gedeon A 1974 *Opt Commun.* **12** 329

Millar C A and Laybourn P J R 1976 *Opt. Commun.* **18** 80

Miller S E 1954 *Bell. Syst. Tech. J.* **33** 661

Stewart G and Laybourn P J R 1978 *IEEE J. Quantum Electron.* to be published

Stewart G, Millar C A, Laybourn P J R, Wilkinson C D W and De La Rue R M 1977 *IEEE J. Quantum Electron.* QE-13 192

Tien P K 1971 *Appl. Optics* **10** 2395

Wood V E 1976 *J. appl. Phys.* **47** 337