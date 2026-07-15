Optics and Laser Technology 122 (2020) 105836

Contents lists available at ScienceDirect

![](./images/812730961866260481_1.jpg)

# Optics and Laser Technology

journal homepage: www.elsevier.com/locate/optlastec

![](./images/812730961866260481_2.jpg)

Full length article

# Thermal gradients sensing using LPGs with a spatially varying effective refractive index difference

![](./images/812730961866260481_3.jpg)

T.A. Eftimov*, N'G. Koffi, F.J. Lesage, P. Mikulic, W.J. Bock

Centre de recherche en photonique, Département d'informatique et d'ingénierie, Université du Québec en Outaouais, Gatineau, QC J8X3X7, Canada

## HIGHLIGHTS

- A matrix model of LPGs with asymmetric $\Delta n_{\text{eff}}$ along the structure is presented.
- Spectral responses of LPGs with temperature differences $\Delta$T are simulated.
- Experiments have been performed to corroborate the simulation results.
- It has been shown that uniform LPGs sense only the absolute value $|\Delta$T|.
- It has been shown that non-uniform LPGs can sense the value and the sign of $\Delta$T.

## ARTICLE INFO

**Keywords:**
Long period gratings (LPG)
Photosensitive fibers
Thermal gradients
Temperature sensors

## ABSTRACT

In this work we present the theoretical modeling and experimental results from thermal gradient measurements using long-period gratings (LPG) with a spatially varying effective refractive index difference along the structure. It has been shown theoretically and confirmed experimentally that by introducing a spatial dependence of the effective refractive index difference $\Delta n_{\text{eff}}$ along the LPG, it can sense not only the magnitude but the direction of the thermal gradient. Thermal gradients in LPG fabricated in boron doped photosensitive fibers are shown to cause depth changes of the minimum $\Delta I_{\text{m}}$ and sensitivities as high as 0.33 dB/°C were observed for a fiber with temperature sensitivity of 2.3 nm/°C. Since average temperature causes wavelength shifts, thermal gradients and average temperature can thus be simultaneously measured by a single LPG.

## 1. Introduction

Temperature sensing using fiber Bragg gratings (FBG) is a mature technology with a variety of multiplexed networks [1]. Because of their small size and narrow spectral width an arrangement of several FBGs can be used to measure temperature distribution and thermal gradients. However, measuring thermal gradient is impossible using a single FBG of a constant period. Measurement of thermal gradients by a single fiber sensor has been proposed for biomedical applications by making use of chirped glass [2–5] or polymer [6] fiber Bragg gratings. However, the sensitivity reported is quite low for satisfactory measurement. Another way of measuring thermal gradients is in the time domain, using longer chirped FBGs [7]. Standard glass fiber LPGs have a far greater thermal sensitivity [8] compared to FBGs and thus present an interest for thermal gradient measurements. Also, recently LPGs written in polymer PMMA fibers with a temperature sensitivity of 276 pm/°C were reported [9]. We have recently proposed [10,11] to use regular arc-induced and UV written LPGs for the measurement of thermal gra- dients. We showed that when a thermal gradient is imposed upon an LPG, its depth $I_{\text{m}}$ changes as a function of the introduced temperature difference $\Delta T$. This permits a far better sensitivity compared to chirped FBGs, which can allow a number of applications. On the other hand, a change of the average temperature causes shifts of the resonance wa- velength. The transmission spectrum sensitivity with respect to tem- perature difference was found [11] to be as high as $d(\Delta I_{\text{m}})/d$ ($\Delta T$) ≈ 0.211 dB/deg and the sensitivity of the centre wavelength ($\lambda_{\text{c}}$) to temperature was $d\lambda_{\text{c}}/dT = 0.431$ nm/deg.

This means that simultaneous temperature and thermal gradient measurements can be performed using a single LPG. The problem that arises, however, is the type of response of the depth change $\Delta I$ vs. $\Delta T$ which is of the type $\Delta I \sim |\Delta T|$ with certain shifts about the zero.

As shown in [11], the possible cause for the temperature shifts of the response is the presence of a gradient of the effective refractive index difference $\Delta n_{\text{eff}}$ along the grating, which ultimately leads to the

* Corresponding author.
E-mail address: tinko.eftimov@uqo.ca (T.A. Eftimov).

https://doi.org/10.1016/j.optlastec.2019.105836
Received 28 July 2019; Received in revised form 7 September 2019; Accepted 11 September 2019
Available online 26 September 2019
0030-3992/ © 2019 Published by Elsevier Ltd.

![](./images/812730961866260481_4.jpg)

Fig. 1. An LPG subdivided into two parts at different temperatures $T_1$ and $T_2$,
and containing $N_1$ and $N_2$ periods.

inequality $\Delta n_{eff,1}^0 \neq \Delta n_{eff,2}^0$ on each half of the grating. Since such a shift
of the response leads to a monotonous dependence of $\Delta I$ vs. $\Delta T$ that
would permit the measurement of both the temperature difference and
its sign. This in turn would allow to determine the value and direction
of a thermal flux.

In this work we present the theoretical study with simulations as
well as experimental confirmation on the performance of LPGs with
thermal gradients in the presence of spatially varying effective re-
fractive index and discuss the implications for simultaneous measure-
ment of average temperature, temperature differences and the thermal
flux direction using a single LPG.

## 2. Theoretical analysis

### 2.1. Matrix formulation

We consider an LPG containing $N$ periodic modulations of nominal
pitch $\Lambda$ and a total length $L = N\Lambda$ at a temperature $T$ as shown in Fig. 1.

If half of the grating is at one temperature $T_1$ and the other is at $T_2$, a
temperature difference $\Delta T = T_2 - T_1$ appears over a distance $\Delta x$
thereby generating a gradient $\Delta T/\Delta x$. Due to thermal expansions and
contractions, the two parts at temperatures $T_1$ and $T_2$, covering corre-
spondingly $N_1$ and $N_2$ pitches will be characterized by periods $\Lambda_1$ and $\Lambda_2$
and hence the total lengths $L_1$ lengths and $L_2$ of the two sections are:

$$
L_i(T)=N_i\Lambda_i(T)\quad i=1,2 \tag{1a}
$$

$$
N_1 + N_2 = N \tag{1b}
$$

The performance of the LPG is theoretically described using the
matrix method described in [11] according to which the input vector
$\boldsymbol{A}^0 = (A_{core}^0, A_{cl}^0)$ of the electric field of the core and the cladding mode is
transformed into an output vector $\boldsymbol{A} = (A_{core}, A_{cl})$ as:

$$
\boldsymbol{A} = \boldsymbol{M}_2 \cdot \boldsymbol{M}_1 \boldsymbol{A}^0 \tag{2}
$$

In (2) the matrices $\mathbf{M}_i$ ($i = 1,2$) are of the type [12]:

$$
\boldsymbol{M}_i = \begin{bmatrix} C_i + j\Delta_i \cdot S_i & j\mathrm{K}_{i} \cdot S_i \\ j\mathrm{K}_{i} \cdot S_i & C_i - j\Delta_i \cdot S_i \end{bmatrix} \quad (i=1,2) \tag{3a}
$$

$$
C_i = \cos(\delta\beta_i L_i),\ S_i = \sin(\delta\beta_i L_i),\ \delta\beta_i = 2\sqrt{\delta_i^2 + \kappa_i^2} \tag{3b}
$$

$$
\Delta_i = 2\delta_i/\delta\beta_i,\ \mathrm{K}_i = 2\kappa_i/\delta\beta_i \text{ with } \Delta_i^2 + K_i^2 = 1 \tag{3c}
$$

In (3) $\delta_i = \delta(T_i)$ and $\kappa_i = \kappa(T_i)$ are the detuning and coupling
parameters defined through the temperature dependent effective re-
fractive indices $\Delta n_{eff,i} = \Delta n_{eff}\ (T_i)$ and periods $\Lambda_i =\Lambda\ (T_i)$ [12] as:

$$
\delta\left(T_{i}\right)=\pi\left[\frac{\Delta n_{eff}\left(T_{i}\right)}{\lambda}-\frac{1}{\Lambda\left(T_{i}\right)}\right] \text{ and } \kappa\left(T_{i}\right)=\frac{\Delta \lambda_{0}}{\lambda^{2}} \Delta n_{eff}\left(T_{i}\right) \tag{4}
$$

of center wavelength $\lambda_c$ and bandwidth $\Delta\lambda_0$. At the fibre input only the
core mode is excited i.e. $\boldsymbol{A}^0 = (1, 0)$ and since the cladding mode is
lossy, only the core mode is detected at the output of the LPG. We then
have for $A_{core}$ and for the normalized intensity $I = |A_{core}|^2$ the wave-
length dependent expressions [11]:

$$
A_{core}=C_{1}C_{2}-(\Delta_{1}\Delta_{2}+\mathrm{K}_{1}\mathrm{K}_{2}).\ S_{1}S_{2}+j(\Delta_{1}S_{1}C_{2}+\Delta_{2}C_{1}S_{2}) \tag{5a}
$$

$$
I=[C_{1}C_{2}-(\Delta_{1}\Delta_{2}+\mathrm{K}_{1}\mathrm{K}_{2}).\ S_{1}S_{2}]^{2}+(\Delta_{1}S_{1}C_{2}+\Delta_{2}C_{1}S_{2})^{2} \tag{5b}
$$

Using Eq. (5b) we can simulate the thermal performance of an LPG
and its response to thermal gradients as a function of the wavelength.

### 2.2. Theoretical Simulations for LPGs with uniform $\Delta n_{eff}$.

To simulate the dependence of spectral responses on the tempera-
ture changes $\Delta T$ we develop $\Lambda(T)$ and $\Delta n_{eff}(T)$ in series and limit our-
selves to the linear first order corrections:

$$
\Lambda_{i}(T)=\Lambda_{i}^{0}+S_{\Lambda,i}'\Delta T_{i} \tag{6a}
$$

$$
\Delta n_{eff,i}(T)=\Delta n_{eff,i}^{0}+S_{\Delta n,i}'\Delta T_{i} \tag{6b}
$$

where

$$
\Delta T_{i}=T_{i}-T_{0} \tag{6c}
$$

$$
S_{\Lambda,i}'=d\Lambda_{i}(T)/dT,\ S_{\Delta n,i}'=d\left[\Delta n_{eff,i}(T)\right]/dT \tag{6d}
$$

it the temperature $T_i$ at the $i$-th part with respect to the initial tem-
perature $T_0$. In our simulations we limit ourselves to:

$$
\Lambda_{i}(T)=\Lambda_{i}^{0}+S_{\Lambda,i}'\Delta T_{i},\ \Delta n_{eff,i}(T)=\Delta n_{eff,i}^{0}+S_{\Delta n,i}'\Delta T_{i} \tag{7}
$$

In the above expressions $\Lambda_i^0$ and $\Delta n_{eff,i}^0$ are the periods and effective
refractive index differences of the two halves at the initial temperature
$T_0$, $S_{\Lambda,i}'$ and $S_{\Delta n,i}'$ are the thermal expansion coefficients and the tem-
perature sensitivities of the efficient refractive index differences $\Delta n_{eff,i}$.
While $S_{\Lambda,i}'$ is strictly positive, $S_{\Delta n,i}'$ can change sign. If both halves of the
LPG are identical $\Lambda_1^0 = \Lambda_2^0$, $\Delta n_{eff,1}^0 = \Delta n_{eff,2}^0 = \Delta n_{eff}^0$ and written in the
same fiber then $S_{\Lambda,1}' = S_{\Lambda,2}'$ and $S_{\Delta n,1}' = S_{\Delta n,2}'$.

In our simulations we seek to outline the types of responses that can
be expected for varying signs and values of sensitivities so we represent
the temperature difference as:

$$
\Delta T_{i}=T_{i}-T_{0}=m\delta T_{i}\quad m=0,\pm1,\pm2,\pm3,.... \tag{8}
$$

and then for $\delta T_i = \delta T = const$

$$
S_{\Lambda,i}'\Delta T_{i}=m.\ S_{\Lambda,i}'\delta T=m.\ \sigma_{\Lambda,T}^{i}\quad m=0,\pm1,\pm2,\pm3,.... \tag{9a}
$$

$$
S_{\Delta n,i}'\Delta T_{i}=m.\ S_{\Delta n,i}'\delta T=m.\ \sigma_{\Delta n,T}^{i}\quad m=0,\pm1,\pm2,\pm3,... \tag{9b}
$$

so by varying the temperature difference parameter $m$ by value and sign
we simulate a step-wise increase of the temperature difference, which is
$\Delta T > 0$ for one side $\Delta T < 0$ for the other. I.e. $\Delta T_1 = -\Delta T_2$.

For a uniform fiber and grating we calculate the detuning $\delta$ and the
coupling $\kappa$ parameters for each wavelength from (4) for both halves
using the following values: $\lambda_c = 1550$ nm, $\Lambda_0 = 250$ $\mu$m and hence
$\Delta n_{eff}^0 = 0.0062$. Also we assume $\Delta\lambda = 39.6$ nm, $N_1 = N_2 = 100$ and
$\sigma_{\Lambda,T}^i = 0.01$ $\mu$m $\sigma_{\Delta n,T}^i$ was varied between $-2\cdot10^{-6}$ and $2\cdot10^{-6}$ riu.
The values were substituted into (5)-(9) for each half of the grating
with $\Delta T_2 = -\Delta T_i$. Using (5b) we calculate

$$
I_{dB}(\lambda)=10\log I(\lambda) \tag{10}
$$

Fig. 2(a) show theoretical spectral responses of the model LPG for
$m = 0$ to $\pm 10$ from which we see that on increasing the temperature
difference $\Delta T = \Delta T_2 - \Delta T_1$ between the two parts of the LPG, the depth
of the minimum changes and the dependence is shown in Fig. 2(b). The
depth change $\Delta I_m$ is symmetric with respect to $\Delta T$ and the sign of the
gradient cannot be determined.

## 3. Experiments and results

### 3.1. Experimental set-up

Fig. 3 shows the experimental set up used to measure the response
to temperature differences $\Delta T$ imposed on an LPG as shown in Fig. 4 in
which the broadband source is an Agilent 83437A in the range from
1150 nm to 1700 nm and the optical spectrum analyzer is an Agilent
86142B.

Several LPGs were fabricated using a KrF excimer UV laser and a
splicer. The excimer laser is a PulseMaster 860/880 series
(LightMachinery), emitting up to 700 mJ at 248 nm. Pulse durations are

![](./images/812730961866260481_5.jpg)

Fig. 2. Theoretical simulations and experimental observations of spectral responses of LPGs to thermal gradients in the case of $\Delta n_{eff,1}^{0} = \Delta n_{eff,2}^{0} = \Delta n_{eff}^{0}$ and $\sigma_{\Delta n,T}=+1 \cdot 10^{-6}$ riu: (a) change of spectral distribution; (b) Depth change $\Delta I$ versus $\Delta T$.

![](./images/812730961866260481_6.jpg)

Fig. 3. Experimental set-up or the measurement of spectral responses of LPGs for induced thermal gradients.

![](./images/812730961866260481_7.jpg)

Fig. 4. Experimental arrangement for the creation of abrupt thermal gradients along an LPG with a nominally constant period.

12-20 ns. The laser beam having 8x12 mm dimensions at laser output were expanded and collimated to a dimension of 8x50 mm using cylindrical lenses. The beam was next directed to an amplitude mask placed above the fiber. The splicer used was a Fitel. All gratings were written in a Fibercore 1250/1550 photosensitive (PS) B-doped optical fibre. The UV-written PS LPGs are noted as PS-368 $(\Lambda_{0}=368 \mu m)$ and PS-358 $(\Lambda_{0}=358 \mu m)$ while the arc-fused tapered LPGs as PS-252 $(\Lambda_{0}=252 \mu m)$, PS-220 $(\Lambda_{0}=220 \mu m)$ and PS-194 $(\Lambda_{0}=194 \mu m)$ all with lengths of $L \approx 50$ mm.

Fig. 5 shows the experimental results for two LPGs made from photosensitive fibres. Fig. 5(a) shows the spectral changes for the PS-359 LPG, while Fig. 5(b) the changes $\Delta I_{m}$ of the depth minimum vs. the temperature difference $\Delta T$. The responses as a whole behave as expected from the theoretical simulation in Fig. 2(b) except for the shifts to positive $\Delta T$ for PS-359 and to negative for PS-358.

![](./images/812730961866260481_8.jpg)

Fig. 5. Theoretical simulation of the spectral response of an LPG grating to temperature differences $\Delta T$ of the two halves of the grating: (a) simulated spectra changes for $\sigma_{\Delta n,T}=+1 \cdot 10^{-6}$ riu and $m$ varying from -10 to +10; (b) Changes of the depth of the LPG at different temperature parameters $m$ for three values of $\sigma_{\Delta n,T}$: 0 and $\pm 1 \cdot 10^{-6}$ riu°C.

As commented in [11] these shifts suggest that the effective refractive index difference $\Delta n_{eff.}$ of the LPG is not uniform along the grating.

### 3.2. Simulation and experimental verification

#### 3.2.1. LPGs with a gradient in the effective refractive index

We now assume that there exists a certain gradient of the effective refractive index distribution along the grating i.e. $\Delta n_{eff}^{0}(x)$. In such a case the average effective index differences of both halves are different: $\bar{\Delta} n_{eff,1}^{0} \neq \bar{\Delta} n_{eff,2}^{0}$. We therefore simulate the LPG performance for different initial values of $\bar{\Delta} n_{eff,1}^{0}$ and $\bar{\Delta} n_{eff,2}^{0}$

$$
\Delta n_{eff,1}^{0}=\Delta n_{eff}^{0}-dn, \Delta n_{eff,2}^{0}=\Delta n_{eff}^{0}+dn \tag{11}
$$

With $dn$ varying from $dn=-3 \cdot 10^{-6}$-$1 \cdot 10^{-6}$ we simulate the spectral changes and plot the dependences of $\Delta I_{m}(\Delta T)$ which we plot in Fig. 6. As is seen, the shift of the responses is related and proportional to the step-index gradient. And the response for $dn=-1 \cdot 10^{-5}$ is symmetric to that of $dn=1 \cdot 10^{-5}$. Theses simulations explain the experimental observations shown in Fig. 5(b).

We next measured the responses of a double resonance (DR) LPG and we found that the sensitivity to thermal gradient was extremely high, however the dependences of $\Delta I_{m}$ on $\Delta T$ are different and correspond to a high value of $dn$ and at the higher wavelength, the response exhibits a greater shift so that the LPG can sense the direction of the gradient.

It is clearly seen that the grating in Fig. 7(a) almost vanishes as simulated in Fig. 2(a) but unlike the $\Delta I$ vs. $\Delta T$ response from Fig. 2(b) which does not discern the sign of the thermal gradient, the DR LPG exhibits a shifted response and within the limits of $\Delta T$ from -30C to +30C will sense the gradient sign for the minimum at higher wavelengths.

In a previous paper [9] we have shown that when placed in water the responses of $\Delta I$ to $\Delta T$ exhibit certain shifts. Therefore, we perform

![](./images/812730961866260481_9.jpg)

Fig. 6. Theoretical responses to temperature differences $\Delta T$ in a fiber with step-change in the effective refractive index along the grating for different values of $dn$.

![](./images/812730961866260481_10.jpg)

Fig. 7. Responses to thermal gradients of a fused taper double resonance LPG made from photosensitive fiber: (a) changes of the spectrum; (b) response curves to temperature differences.

the measurements in air and in water for one of the gratings – PS-268 whose spectral changes in air are shown in Fig. 8(a) while the $\Delta I(\Delta T)$ plots for air and water are in Fig. 8(b). A closer inspection of the two

![](./images/812730961866260481_11.jpg)

Fig. 8. LPG responses to temperature difference $\Delta T$: (a) spectral changes; (b) Response curves to thermal gradients.

curves reveals that the effect of water is to shift the response to the right compared to that in air. The response in water now is such that the direction of the thermal gradient can be identified. The response in air for PS-268 from Fig. 8(b) is similar to the simulation for $dn=-3\cdot10^{-6}$ while the response for water to that for $dn=-4\cdot10^{-6}$ which means it has been shifted. The thermal gradient response now is such that the direction of the gradient can be determined.

### 3.2.2. LPGs with a deliberate step-index gradient in the effective refractive index

The above experiments suggest that if we could deliberately introduce a change in the effective refractive index difference in each half of the LPG i.e. $\Delta n_{eff,1}^{0}\neq\Delta n_{eff,2}^{0}$, we can off-set the thermal gradient sensitivity curve. In the arrangement shown in Fig. 9 each half of the grating is placed in a separate U-shaped groove that can be independently filled with water we can realize four combinations: air/air (A/A), air/water (A/W), water/air (W/A) and water/water (W/W) denoted by the sequence of the halves - first/second.

Fig. 10 shows the results of controlled effective refractive index difference for the single resonance fused tapered LPG in a photosensitive fiber PS-220. When in air (A/A), the thermal gradient response exhibits a certain off-set $(\Delta T_{off}\approx+10^{\circ}C)$ as indicated in Fig. 10(b). Inserting the grating's right half in water (A/W) the off-set is compensated and we observe the response shifting left, while for the opposite case (W/A) the response shifts right and the off-set is increased to approximately $\Delta T_{off}\approx+17^{\circ}C$. This is exactly what we would expect from the simulations in Fig. 6. A closer inspection reveals that apart from the

![](./images/812730961866260481_12.jpg)

Fig. 9. Experimental arrangement for deliberate external introduction of a step-change in the effective refractive index difference between the two halves of the grating.

![](./images/812730961866260481_13.jpg)

![](./images/812730961866260481_14.jpg)

Fig. 10. Responses to temperature difference $\Delta T$ of single resonance LPG PS-220: (a) spectral changes; (b) Responses to thermal gradients with externally imposed step gradients.

![](./images/812730961866260481_15.jpg)

![](./images/812730961866260481_16.jpg)

Fig. 11. Responses to temperature difference $\Delta T$ of single resonance LPG PS-194: (a) spectral changes; (b) Responses to thermal gradients with externally imposed step gradients.

observed sensitivity shifts, the slopes of the responses also change and the W/A response is more sensitive than A/A which in turn is more sensitive than the A/W. This means that the effective sensitivities $S_{\Delta n}'$ become different for water immersion.

We next studied the thermal gradient response for DR LPGs away from turning point. The results for the lower resonance wavelength ($\lambda_1 = 1422$ nm) are presented in Fig. 11. As seen from Fig. 11(a) the grating is practically erased at $\Delta T = -40$ °C. This is also observed with step-like imposed gradients in $\Delta n_{eff}^0$. In Fig. 11(b) we see that in air (A/A) the off-set temperature difference is $\Delta T_{AA} \approx 7$ °C. Imposing water on the left side (W/A) shifts the symmetry line to an off-set $\Delta T_{A/ \Omega} \approx -16$ °C while with water on the right side (A/W) the symmetry line is shifted to $\Delta T_{W/A} \approx +30$ °C and within the interval of $\Delta T = [-30$ °C, $+30$ °C] the thermal response is symmetric about $\Delta T = 0$ °C and both the value and the direction of the gradient can be measured. As can be verified $\Delta T_{AA} \approx (\Delta T_{A/W} + \Delta T_{A/W})/2$.

The W/A curve from Fig. 11(b) shows that temperature differences in the range between $\Delta T = -30$ °C to $\Delta T = +30$ °C can be sensed over an LPG length of 50 mm by measuring the depth of the grating which varied by 6 dB. This yields on the average sensitivity $d(\Delta I_m)/d$ $(\Delta T) = 0.1$ dB/°C for the PS-194 DR LPG. Since power level and losses can be measured with a 0.02 dB accuracy this means gradients caused by temperature differences as low as 0.2 °C are measurable with this grating. However, from Figs. 9(b) and 7(b) it can be estimated that grating PS-268 exhibited an intensity change of 9.3 dB over $\Delta T = \pm$ 25 °C which yields a sensitivity of $d(\Delta I_m)/d(\Delta T) = 0.186$ dB/°C while PS-252 had a change of 20 dB for $\Delta T = \pm 30$ °C which translates into a sensitivity of $d(\Delta I_m)/d(\Delta T) = 0.33$ dB/°C. The temperature sensitivity of this LPG was about 2.3 nm/°C. This is the highest sensitivity measured with tapered DR LPG made from photosensitive fibers.

Different methods can be used to introduce a deliberate permanent spatial variation of the effective refractive index difference so as to enable the measurement of the magnitude and the direction of the thermal gradient and they will be considered elsewhere.

While in our study we have used highly temperature sensitive PS fibers for temperature changes at higher and lower average temperatures, for some applications as in medicine where it may be undesirable to introduce glass fiber, polymer fiber LPGs [6,9] may be more appropriate since the average temperature is around 37 °C and PMMA withstands up to 100 °C. Also, temperature sensitivities will depend on the particular period that defines the higher order mode and the resonance wavelength.

### 4. Conclusions

The theoretical and experimental analysis performed in this paper allows the following conclusions:

First, it is shown that if an LPG possesses a gradient of the effective refractive index along its structure $\Delta n_{eff}^0(x)$, then its response to thermal gradient exhibits shifts and an off-set from the $\Delta T = 0$ position.

Second, we have experimentally confirmed this effect in both single- and double resonance LPGs.

Third, we have shown that by deliberately introducing a simple step change of $\Delta n_{eff}^0(x)$ along an LPG we can shift the thermal gradient response in a way that the grating simultaneously detects both the temperature difference and the direction of the gradient.

### Funding

This work was supported by the Natural Sciences and Engineering Research Council of Canada (NSERC) under Industrial Research Chair program.

### References

[1] Eric Udd, William B. Spillman (Eds.), Fiber Optic Sensors: An Introduction for

Engineers and Scientists, John Wiley and Sons Inc., 2011.

[2] D. Tosi, E. Macchi, M. Gallati, G. Braschi, A. Cigada, S. Rossi, G. Leen, E. Lewis, Fiber-optic chirped FBG for distributed thermal monitoring of ex-vivo radio- frequency ablation of liver, Biomed. Opt. Exp. 5 (2014) 1799-1811.

[3] G. Palumboa, A. Iadiciccoa, D. Tosi, P. Verzec, N. Carlomagnoc, V. Tammaroc, J. Ippolitoc, S. Campopiano, Fiber Bragg Grating for temperature monitoring during medical radiofrequency treatments, 30th Eurosensors Conf., Eurosensors 2016, Procedia Engineering, vol. 168, Elsevier, 2016, pp. 1308-1311.

[4] Giovanna Palumbo, Daniele Tosi, Agostino Iadicicco, Stefania Campopiano, Analysis and design of chirped fiber Bragg Grating for temperature sensing for possible biomedical applications, IEEE Photo. J. 10 (3) (2018) 1-15 https:// ieeexplore.ieee.org/document/8345713/https://doi.org/10.1109/JPHOT.2018. 2829623.

[5] S. Korganbayev, Y. Orazayev, S. Sovetov, A. Bazyl, E. Schena, C. Massaroni, R. Gassino, A. Vallan, G. Perrone, P. Saccomandi, M.A. Caponero, G. Palumbo, S. Campopiano, A. Iadicicco, D. Tosi, Detection of thermal gradients through fiber- optic Chirped Fiber Bragg Grating (CFBG): medical thermal ablation scenario, Opt. Fiber Technol. 41 (2018) 48-55.

[6] S. Korganbayev, R. Min, M. Jelbudina, X. Hu, C. Caucheteur, O. Bang, B. Ortega, C. Marques, D. Tosi, Thermal profile detection through high-sensitivity fiber optic chirped Bragg grating on microstructured PMMA fiber, J. Lightw. Techn. 36 (2018) 4723-4729.

[7] A.L. Ricchiuti, D. Barrera, K. Nonaka, S. Sales, Temperature gradient sensor based on a long-fiber Bragg grating and time-frequency analysis, Opt. Lett. 39 (2014) 5729-5731.

[8] S.W. James, R.P. Tatam, Optical fibre long-period grating sensors: characteristics and application, Measur. Sci. Technol. 14 (2003) R49-R61.

[9] R. Min, C. Marques, K. Nielsen, O. Bang, B. Ortega, Fast inscription of long period gratings in microstructured polymer optical fibers, IEEE Sens. J. 18 (2018) 1919-1923.

[10] M. Koffi, T. Eftimov, F. Lesage, P. Mikulic, W.J. Bock, Measurement of thermal gradients using long period gratings at different levels of ambient refractive indices, TuE69, OFS-26, Lausanne, (2018).

[11] M. Koffi, T. Eftimov, F.J. Lesage, P. Mikulic, W.J. Bock, Measurement of thermal gradients using long period gratings at different levels of ambient refractive indices, Special issue of J. Lightw Technol. (2019) (May 20).

[12] T. Erdogan, Fiber grating spectra, J. Lightw. Techn. 5 (1997) 1277-1294.

Tinko A. Eftimov received his M.S. degree in Engineering Physics from the Sofia University, Bulgaria in 1982 and Ph.D. degree from the Technical University, Sofia in 1989 in the field of optical fibers. He has worked for the Technical University in Sofia, the Helsinki University of Technology, Finland, JDSUniphase Corp., the Université du Québec en Outaouais, Canada and the Plovdiv University, Bulgaria. His interests were in the field of polarization in optical fibers, fiber sensors, intermodal interference, WDM components, FBG reliability testing, fluorescence, and senor networks. His recent interests are LPG based, core-cladding intermodal sensors and micro in-line Mach-Zehnder Interferometers. He is the author and co-author of more than 120 papers, a monography and three patents.

N'Guessan G.M. Koffi was born in Tiassalé, Ivory Coast, in 1979. He received the B.Ing. degree in mechanic and M. Ing. degree in renewable energy from "École Polytechnique de Montréal", Montréal, Canada, in 2015 and 2017, respectively. In September 2017, he joined the research team of CRP as Ph.D. degree in Photonic engineering at UQO uni- versity, Québec, Canada. His current research interest is in the application of fiber grating technology for thermal flux measurement and thermal sensing. Over the past 16 months, he has been working on temperature gradient sensitivity to build a new LPG architecture. His latest activities are focused on fiber optics sensors for thermal gradient detection.

Frédéric J. Lesage received his M.Sc. in Complex Analysis from the University of Montreal and his PhD in Mechanical Engineering from McMaster University, Hamilton Canada. He is currently an Associate Professor with the Département d'informatique et d'ingénierie, Université du Québec en Outaouais in Gatineau QC Canada.

Predrag Miculic received an Associate of Science Degree as a Telecommunication Engineering Technologist at the University of Sarajevo, Yugoslavia in 1989. He has over 20 years of professional high-tech experience in the industry. His major interests are thin- film deposition, excimer lasers, photonic devices, fiber sensors, and procedures for spli- cing dissimilar fibers including photonic crystal fibers.

Wojtek J. Bock received his M.Sc. in Electrical Engineering and his Ph.D. in Solid State Physics from the Warsaw University of Technology, Poland, in 1971 and 1980, respec- tively. Since 1989 he has been a Full Professor of Electrical Engineering at the Université du Québec en Outaouais (UQO), Canada. Dr. Bock has been Director of the Photonics Research Center at UQO since 2003. He has recently been awarded an SPI-NSERC Senior Industrial Research Chair in Photonic Sensing Technologies for Safety and Security Monitoring. His current research program centers around developing novel fiber-optic device solutions and photonic sensing techniques for application in sectors of national importance to Canada. He has authored and co-authored more than 400 scientific papers, patents and conference papers in the fields of fiber optics and metrology which have been cited about 3500 times. Dr. Bock is a Life Fellow of IEEE, and served as Associate Editor of IEEE/OSA Journal of Lightwave Technology and International Journal of Sensors. He was also Chairman of the International Optical Fiber Sensor Conference (OFS21) held in Ottawa in May 2011.