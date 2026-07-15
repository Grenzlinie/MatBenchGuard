# Simulation study on spectrum beam combining based on reflection volume Bragg grating

Yingyan Yi$^*$, Min Li, Changkui Hu, Fengxiang Chen,

Department of Physics science and technology, School of Science, Wuhan University of Technology, Wuhan, 430070, China

## ABSTRACT

Single fiber laser can reach kilowatt level output. Higher power output is limited by nonlinear effect inside the fiber, heat deposition and pump power. Spectral beam combining of multiple laser beams with offset wavelengths into a single near-diffraction-limited beam is an effective solution to increasing energy brightness and scaling output power of high-power lasers. The loss factors of effect on the diffraction efficiency of the gratings are discussed. Design principles and technical approach for spectral beam combining (SBC) of two channels and three channels by reflecting volume Bragg grating are investigated. Two and three channels SBC are numerically analyzed when the input beam divergence is 0.06mrad. The results show the SBC efficiencies are 98.65% and 97.57% when the spectral width is 0.1nm, and the efficiencies are 92.16% and 88.98% when the spectral width is 0.3nm, respectively.

**Keywords:** reflecting volume Bragg grating, spectral beam combining, photo-thermo-refractive glass

## 1. INTRODUCTION

High power lasers with diffraction limited beam quality are desired for many applications in defense and industry. Single fiber laser with an output power of more than 1kW are not only limited by thermal problems but also by nonlinear effects such as stimulated Brillouin scattering $^{[1]}$. Further power scaling can be achieved by combining the output beams from multiple lasers into a single beam. Many methods of beam combining have been developed last years, such as side-by-side beam combining, coherent beam combining and spectral beam combining (SBC)$^{[2-3]}$. Coherent beam combining can be realized by controlling the relative phase of beams from an array of elements that operate with the same wavelength. The highest fiber laser power that is coherently combined to date is 725W $^{[4]}$. In principle, this approach could provide efficient beam combining, but it requires extremely high precision stability of spectrum and needs stabilization of the relative phase of the source. Spectrum beam combining is an incoherent combining technique that does not require phase control of sources, allowing for a stable and robust system. The output beams from an array of lasers with several distinct wavelengths can be combined into a single diffraction-limited beam using dispersive optical elements. Cook et al. proposed an SBC setup based on a surface diffraction grating with spectral control of source using optical feedback $^{[5]}$, but the combing efficiency was affected by thermal deformation of the grating. Efimov et al. invented a photo-thermo-refractive(PTR) glass$^{[6]}$, volume Bragg gratings (VBGs) recorded in this glass have been extensively used in high-power laser systems due to their perfect thermal, optical and mechanical stability, as well as good angular and spectral selectivity in the near IR and visible spectrum. In 2002, Ciapurin et al. reported two channels

E-mail address: yingyan0410@163.com; phone 0086-027-63153727;
This work is supported by "the Fundamental Research Funds for the Central Universities"(Project number:2011-Ia-028)

Photonics and Optoelectronics Meetings (POEM) 2011: Optoelectronic Devices and Integration, edited by
Erich Kasper, Jinzhong Yu, Xun Li, Xinliang Zhang, Jinsong Xia, Junhao Chu, Zhijiang Dong, Bin Hu, Yan Shen,
Proc. of SPIE Vol. 8333, 83330O · © 2012 SPIE · CCC code: 0277-786X/12/$18 · doi: 10.1117/12.917294

Proc. of SPIE Vol. 8333 83330O-1

beam combining results⁽⁷⁾, in the latest experiment, five-channel high efficiency spectral beam combing resulted in a >750W near-diffraction-limited cw beam has been reported ⁽⁸⁾. The numerical analysis of spectral beam combining by volume Bragg grating has been reported by Pu Shi-bing et al.⁽⁹⁾, they only consider the combination beams as polychromatic planar wave and do not consider the effect of beam divergent. In this paper, in the case where a real beam is both divergent and spectrally widened, the two beams and three beams combination efficiency are numerically investigated.

## 2. DIFFRATION EFFCIENCY OF REFLECTING VOLUME BRAGG GRATINGS IN PTR GLASS

Properties of reflecting and transmitting VBGs have been described in great detail ⁽¹⁰⁻¹¹⁾. In this paper, we will focus on spectral properties of narrow-band reflecting VBGs used for SBC. For a plane wave incident on an unslanted reflecting Bragg grating with sinusoidal variation of refractive index, diffraction efficiency can be expressed with basic grating parameters ⁽¹¹⁾:

$$
\eta(\Delta \lambda)=\left\{1+\frac{1-\left(\lambda_{0} f^{2} \Delta \lambda / 2 n_{a v} \delta n\right)^{2}}{\sinh ^{2}\left[\left(2 \pi n_{a v} t \delta n / \lambda_{0}^{2} f\right)^{2}-\left(\pi f t \Delta \lambda / \lambda_{0}\right)^{2}\right]^{1 / 2}}\right\}^{-1} \tag{1}
$$

where $t$ is grating thickness, $n_{\text{av}}$ is an average refractive index of a medium $n_{\text{av}}$ at free-space wavelength $\lambda_0$, $\delta$n is an amplitude of refractive index modulation, and $f$ is spatial frequency of grating. The plane wave is incident on the grating at an angle that satisfies the Bragg condition for a wavelength $\lambda_0$, and $\Delta\lambda$ represents spectral offset from $\lambda_0$. For beams with finite spectral width, diffraction efficiency can be calculated as a convolution of the diffraction efficiency for monochromatic wave of the grating and the spectral distribution ⁽¹¹⁾.

### 2.1 The effect of absorption of medium on diffraction efficiency

The diffraction efficiency that we obtained in reference [11] is the case of lossless dielectric grating, and the absorption has always existed for a real volume grating. For Bragg incident and unslanted VBG, we can be obtained the diffraction efficiency formula ⁽¹²⁾:

$$
\eta=\frac{\kappa^{2}}{\left[\alpha+\left(\kappa^{2}+\alpha^{2}\right)^{1 / 2} \cdot \operatorname{coth} \frac{t}{\cos \theta}\left(\kappa^{2}+\alpha^{2}\right)^{1 / 2}\right]^{2}} \tag{2}
$$

where $\alpha$ is average absorption constant, $\kappa=\pi \delta n / \lambda$ is coupling constant and $\theta$ the angle of incidence. It is assumed that the angle of incidence $\theta=10^{\circ}$, refractive index modulation $\delta$n=0.0015 and the incident wavelength $\lambda_0$=1064nm, the dependence of diffraction efficiency on grating thickness for different absorption constant $\alpha$ is shown in Fig.1. It can be seen that the diffraction efficiency decreases with the increase of absorption constant $\alpha$ when the thickness of grating are given. For certain grating thickness t, the diffraction efficiency $\eta$ deceases with the increase of $\alpha$. It also shows that the diffraction efficiency increases rapidly with the grating thickness increasing when the grating thickness is below 0.8mm, then the diffraction efficiency almost doesn't change as the grating thickness is larger than 0.8mm, and the effect of absorption on diffraction efficiency is also smaller, the diffraction efficiency decreases about 1% when the absorption constant varies from $0.01\ \text{cm}^{-1}$ to $0.1\ \text{cm}^{-1}$. The new VBGs with an absorption constant $\alpha$=$1×10^{-4}\ \text{cm}^{-1}$ was reported by OptiGrate corporation in the year of 2010, the effect of absorption on combining efficiency can be neglected when using this VBGs for beam combining.

![](./images/813333938108891137_1.jpg)

Fig.1 Dependence of diffraction efficiency on grating thickness

### 2.2 The effect of polarization of incident beam on diffraction efficiency

In addition to absorption, the diffraction efficiency has influence by polarization of incident beam. We assume that the beam incident on the VBGs includes s-polarization and p-polarization which also incidence at an angle $\theta_1$, the angle of diffraction is $\theta_2$. The diffraction efficiency of s-polarization and p-polarization represent by $\eta_s$ and $\eta_p$, respectively. Based on the Kogelnik coupled-wave theory, when the beam incidences on the unslanted VBGs at Bragg angle, the diffraction efficiency can be given as

$$
\eta_{s, p}=\tanh ^{2} \Phi_{s, p} \tag{3}
$$

where $\Phi_{\mathrm{s}}=\frac{\pi \delta \mathrm{nt}}{\lambda\left(\cos \theta_{1} \cos \theta_{2}\right)^{1 / 2}}$ and $\Phi_{\mathrm{p}}=\Phi_{\mathrm{s}} \cos \left(\theta_{2}-\theta_{1}\right)$ are the phase incursion of s-polarization and p-polarization, respectively.

![](./images/813333938108891137_2.jpg)

Fig.2 Diffraction efficiency as a function of grating thickness with different polarization

![](./images/813333938108891137_3.jpg)

Fig.3 Diffraction efficiency as a function of incident angle with different polarization

Fig. 2 shows the diffraction efficiency as a function of grating thickness with different polarization with an incident angle of $20^{\circ}$, the other parameters described in Section 2.1. It can be seen that different polarization beam has different

diffraction efficiency when the grating thickness is small, the diffraction efficiency almost keeps constant 100% when grating thickness is larger than 0.8mm, we can neglect the effect of polarization on diffraction efficiency. Fig.3 gives the diffraction efficiency against the incident angle with different polarization. We can see that the diffraction efficiency of s-polarization beam tends to one when the incident angle varies from 0° to 30°, but the diffraction efficiency of p-polarization beam drops from 100% to 97.5%. In general, when the incident angle is smaller than 10° in combining system using reflecting VBGs, the loss induced by the polarization can be neglected.

## 3. DESIGN OF REFLECTING VBGS FOR SPECTRUM BEAM COMBINING

Design of volume Bragg grating for spectrum beam combining of real beams is a produce of optimizing grating parameters such as grating period, thickness and refractive index modulation based on the combining geometry, parameters of individual lasers such as beam divergence, spectral width et al. and the desired channel separation. Our goal of the optimizing procedure is to maximize the combining efficiency by minimizing diffraction losses in the SBC system.

Design procedure for reflecting VBGs used for spectral beam combining consists of the following steps:

(1) Grating frequency is determined by desired Bragg angle, which is selected based on system geometry considerations. If polarization insensitivity is desired, Bragg angle should be kept below 10-15° as discussed in Section 2.2.

(2) Grating thickness is determined by the required spectral separation of channels, it can be calculated using
$$
t=\frac{\lambda_{0}\left[\left(\operatorname{atanh} \sqrt{\eta_{0}}\right)^{2}+\pi^{2}\right]^{1 / 2}}{\pi f \delta \lambda^{H W F Z}}
$$
, where $\eta_{0}$ is usually set larger than $99 \%, \delta \lambda^{H W F Z}$ is the spectral selectivity of reflecting VBGs.

(3) Refractive index modulation can be obtained based on given diffraction efficiency $\eta_{0}$:
$$
\delta n=\frac{\lambda_{0}\left|\cos \theta_{m}^{*}\right| \operatorname{atanh} \sqrt{\eta_{0}}}{\pi t}.
$$

## 4. THEORY MODEL OF VOLUME BRAGG GRATING FOR SPECTRAL BEAM COMBINING

### 4.1 Modeling of two channels spectral beam combining

SBC by means of volume Bragg gratings utilizes unique spectral response of VBGs: diffraction efficiency is close to unity when the Bragg condition is satisfied and is close to zero at multiple points corresponding to particular wavelengths offsets from Bragg condition. Two beams with shifted wavelengths incident on a grating at conjugate angles emerge overlapped and collinear (Fig.4) if the wavelength of one $(\lambda_{1})$ matches the Bragg condition (the beam is diffracted) and the wavelength of the other $(\lambda_{2})$ is offset to match one of the zeros (the beam is transmitted).

In general, the real beam is both divergent and spectrally widened, the losses induced by absorption and reflection occurs when the incident beam propagations through the VBGs. It is assumed that the losses induced by absorption and reflection are represented by $\eta_{a}$. The diffraction efficiency for the beam $\lambda_{1}$ is $\eta_{D}$, and the transmitting efficiency of the beam $\lambda_{2}$ is $\eta_{T}$, and the output powers are $P_{1}$ and $P_{2}$, respectively. Then the combining efficiency $\eta$ can be written as:

$$
\eta=\frac{P_{1} \eta_{D}+P_{2}\left(1-\eta_{\alpha}\right) \eta_{T}}{P_{1}+P_{2}} \tag{4}
$$

Further suppose that the output powers are equal for two combining lasers, the combining efficiency can be rewritten as:

$$
\eta==\frac{\eta_{T}\left(1-\eta_{\alpha}\right)+\eta_{D}}{2} \tag{5}
$$

![](./images/813333938108891137_4.jpg)

Fig.4 Spectral beam combining of two beams with offset wavelengths using a reflecting volume Bragg grating

![](./images/813333938108891137_5.jpg)

Fig.5 Spectral selectivity of a reflecting VBG used for SBC with 0.64nm channel spacing around 1064nm

The numerical analysis results are shown based on the physics model for two beams combining. In order to simplified analysis, the spectral distribution of the combining lasers is approximated by a Gaussian function $^{[11]}$. The optimized grating has the following parameters: $n_{av}$=1.485 , t=2.5mm , $\Lambda$=0.36$\mu$m , $\delta$n=550ppm and $\lambda_{0}$=1064nm when angle of incidence is $\sim$5°. The spectral selectivity of a reflecting VBG optimized for combining of beams with 0.6mrad divergence with 0.64nm channel separation at 5° angle of incidence is shown in Fig.5. This grating provides diffraction efficiency of 99.9% at Bragg condition and diffraction loss is about 0.9% for the beam with and divergence ~ 0.6mrad wavelength ~ 1063.36nm, corresponding to the $4^{\text{th}}$ minimum. The losses induced by polarization can be neglected when

the incident angle is small. We suppose that the losses $\eta_{\alpha}$ induced by the absorption and the reflection of the grating are 1.5%, and the output powers of two combining lasers are equal. The diffraction efficiency of the beam which matches the Bragg condition, the transmission efficiency of the beam offset from Bragg condition and the total combining efficiency with different spectrum width are given in Table 1. The results show the SBC efficiencies are 98.65% and 92.16% when the spectral width is 0.1nm and 0.3nm, respectively. Moreover, the diffraction efficiency of the beam $\lambda_1$ which matches the Bragg condition decreases with the increase of the spectral width, the transmission efficiency of the beam $\lambda_2$ also decreases, too. It can be explained that the minima of the diffraction efficiency curve will become larger with the increase of the spectral width, so the diffraction loss becomes larger.

Table 1 diffraction efficiency and the combining efficiency $\eta$ with different beam spectral width $w$

<table>
  <thead>
    <tr>
      <th>$w$/nm</th>
      <th>$\eta_{\text{T}}$(1063.36nm)/%</th>
      <th>$\eta_{\text{D}}$(1064nm)/%</th>
      <th>$\eta$/%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>99.1</td>
      <td>99.9</td>
      <td>98.76</td>
    </tr>
    <tr>
      <td>0.02</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>98.71</td>
    </tr>
    <tr>
      <td>0.04</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>98.71</td>
    </tr>
    <tr>
      <td>0.06</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>98.71</td>
    </tr>
    <tr>
      <td>0.08</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>98.71</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>99.0</td>
      <td>99.7</td>
      <td>98.65</td>
    </tr>
    <tr>
      <td>0.15</td>
      <td>98.9</td>
      <td>99.4</td>
      <td>98.41</td>
    </tr>
    <tr>
      <td>0.2</td>
      <td>98.4</td>
      <td>97.5</td>
      <td>97.22</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>97.7</td>
      <td>93.9</td>
      <td>95.08</td>
    </tr>
    <tr>
      <td>0.3</td>
      <td>96.8</td>
      <td>89.0</td>
      <td>92.16</td>
    </tr>
  </tbody>
</table>

![](./images/813333938108891137_6.jpg)

Fig. 6 The combining efficiency as a function of spectrum width

Fig.6 shows the dependence of total combining efficiency on the spectrum width of the combining lasers. We can see that the combining efficiency almost remains the same when the spectral width of the combining beams is smaller than the spectral selectivity of the grating, and the combining efficiency decreases rapidly when the spectral width of the combining beams are larger than the spectral selectivity of the grating. So, the angular selectivity, the spectral selectivity and the diffraction efficiency of the beam that matches the Bragg condition should be overall consideration when we design the reflecting VBGs.

### 4.2 Modeling of three channels beam spectral combining
The physics models of SBC setup with three distinct laser sources by two identical reflecting VBGs cascaded is shown in fig.7. By setting the $VBG_1$ to be highly transmissive at wavelength $\lambda_0$ and highly reflective at $\lambda_1$, so the two beams can be combining by $VBG_1$, the principle was discussed in Section 4.1. However, by setting the $VBG_2$ to be highly transmissive at wavelength $\lambda_0$ and $\lambda_1$, at the same time highly reflective at wavelength $\lambda_2$。So the diffraction beam $\lambda_2$ and transmissive beams $\lambda_0$ and $\lambda_1$ are realized spectral beam combining by two cascaded VBGs.

Considering the real beam is both divergent and spectrally widened, and losses induced by the absorption and reflection always exist, so the diffraction and transmission efficiencies for the diffraction beam and transmission beam can not reach 100%. We assume that the diffraction efficiency of the beam with wavelength $\lambda_1$ is $\eta_{1D}$ for the $VBG_1$ , the transmission efficiency of the beam with wavelength $\lambda_0$ is $\eta_{1T}$ for the $VBG_1$ , the diffraction efficiency of the beam with wavelength $\lambda_2$ is $\eta_{2D}$ for the $VBG_2$ , the transmission efficiency of the beams with wavelength $\lambda_0$ and $\lambda_1$ are $\eta_{1T}'$ and $\eta_{2T}'$ for the $VBG_2$, the losses of the $VBG_1$ and $VBG_1$ are $\eta_{1\alpha}$ and $\eta_{2\alpha}$ , respectively. In order to simplified analysis, we consider the three laser beams have the same power, so we can obtain the total combining efficiency formula :

$$
\eta=\frac{\left[\eta_{2 D}+\eta_{1 D}\left(1-\eta_{2 \alpha}\right) \eta_{2 T}^{\prime}+\eta_{1 T}\left(1-\eta_{1 \alpha}\right)\left(1-\eta_{2 \alpha}\right) \eta_{1 T}^{\prime}\right]}{3} \tag{6}
$$

![](./images/813333938108891137_7.jpg)

Fig.7 Schematic of three beams combining by two reflecting volume grating

The grating parameters are the same as Section 4.1. The Bragg condition of $VBG_1$ is satisfied for $\lambda_1$=1064nm when angle of incidence is $5^\circ$ , the wavelength of the other laser beam is $\lambda_0$=1063.36nm. For the $VBG_2$, the centre wavelength

$\lambda_2$=1064.64nm which satisfied the Bragg condition when the angle of incidence is 4.4°. The results of three beams combining by two cascaded reflecting VBGs are shown in Table 2. It can be seen that the SBC efficiencies are 97.5% and 89% when the spectral width is 0.1nm and 0.3nm, respectively. The diffraction efficiency is almost free from the spectral width of combining beams as they are much less than the spectral selectivity of the VBGs, higher combining efficiency can be obtained, and the combining efficiency dramatically drops when spectral width of combining beams are close to the spectral selectivity of the VBGs, these results are consistent with the results of two channels combining system. The results of two beams and three beams spectral combining are all obtained with 0.6mard beam divergence of combining beams. When the other condition are maintained, the combining efficiency will obviously decrease with the increase of the divergence of the combining beams, the reason is that the larger diffraction loss will occur at the $4^{th}$ minimum.

Table.2 Results of three beams combining by reflecting volume Bragg grating

<table>
  <thead>
    <tr>
      <th rowspan="2">w/nm</th>
      <th colspan="2">η(1064)/%</th>
      <th colspan="2">η(1063.36)/%</th>
      <th>η(1064.64)/%</th>
      <th rowspan="2">η/%</th>
    </tr>
    <tr>
      <td>VBG₁(η₁ᴰ)</td>
      <td>VBG₂($\eta_{2T}'$)</td>
      <td>VBG₁(η₁ᵀ)</td>
      <td>VBG₂($\eta_{1T}'$)</td>
      <td>VBG₂(η₂ᴰ)</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>99.9</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.9</td>
      <td>97.57</td>
    </tr>
    <tr>
      <td>0.02</td>
      <td>99.8</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>97.50</td>
    </tr>
    <tr>
      <td>0.04</td>
      <td>99.8</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>97.50</td>
    </tr>
    <tr>
      <td>0.06</td>
      <td>99.8</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>97.50</td>
    </tr>
    <tr>
      <td>0.08</td>
      <td>99.8</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.1</td>
      <td>99.8</td>
      <td>97.50</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>99.7</td>
      <td>99.0</td>
      <td>99.0</td>
      <td>99.1</td>
      <td>99.7</td>
      <td>97.37</td>
    </tr>
    <tr>
      <td>0.2</td>
      <td>97.5</td>
      <td>98.4</td>
      <td>98.4</td>
      <td>99.1</td>
      <td>97.5</td>
      <td>95.54</td>
    </tr>
    <tr>
      <td>0.3</td>
      <td>89.0</td>
      <td>96.8</td>
      <td>96.8</td>
      <td>99.1</td>
      <td>89.0</td>
      <td>88.98</td>
    </tr>
  </tbody>
</table>

The special cases with two and three channels beam combining systems are discussed above, in order to scale the output power, we can cascade series of gratings by setting all individual VBGs to be high transmissive at wavelength $\lambda_1, \lambda_2, ..., \lambda_{N-1}$, and highly reflective only at $\lambda_i$. The total combining efficiency is significantly affected by the transmission losses for the transmission loss affects the throughput multiple times. But the total combining efficiency does not suffer much from the loss in diffraction.

## 5. CONCLUSIONS

The effects of absorption and polarization on the diffraction efficiency of the gratings are studied in this paper. The results show that the effect on diffraction efficiency can be ignored when the absorption is smaller than $0.01cm^{-1}$, when the incident angle is smaller than $10^{\circ}$ in combining system using reflecting VBGs, the loss induced by the polarization also can be neglected. The physical model and the combining efficiency of spectral beam combining for two and three channels by reflecting VBGs are investigated based on the spectral selectivity of the grating, also the design procedure for reflecting VBGs used for spectral beam combining are presented. Two and three channels SBC are numerically analyzed when the input beam divergence is 0.06mrad. The results show the SBC efficiencies are 98.65% and 97.57% when the spectral width is 0.1nm, and the efficiencies are 92.16% and

88.98% when the spectral width is 0.3nm, respectively. Particularly, the cross-talk and material losses, being the main contributing loss factors to the overall system efficiency, should be carefully addressed in the multiple channels SBC design $^{[8]}$.

REFERENCES

[1] Timothy H. Russell and Won B. R., “Incoherent beam combining using stimulated Brillouin scattering in multimode fibers,”. Opt. Expr, 8(2), 246-254(2001)

[2] T.Y. Fan, A. Sanchez, “Coherent (phased array) and wavelength (spectral) beam combining compared,” Proc of SPIE, 5709, 157-164(2005)

[3] T. Y. Fan, “Laser beam combining for high-power, high-radiance source,” IEEE J. Sel. Top. Quantum Electron, 11 (3): 567-577(2005)

[4] T. M. Shay, J. T. Baker, A. D. Sanchez, et al., “Electronic Phasing of High Power Fiber Amplifier Arrays,” LEOS, 783-784(2008)

[5] C C Cook, T. Y. FAN, M M Fejer et al., “Spectral beam combining of Yb-doped fiber lasers in an external cavity,” OSA Trends in Optics and Photonics, 26, 163-166(1999)

[6] Efimov, O., Glebov, L. and Smirnov, V., “High efficiency volume diffractive elements in photo-thermo-refractive glass,” United States Patent 6,673,497 (2004).

[7] I. Ciapurin, L. Glebova, C. Stichley., “High-power incoherent beam combining with Bragg grating in photosensitive glasses,” Proceedings of Solid State and Diode Lasers Technical Review, HPFIB4(2002)

[8] Armen Sevian, Oleksiy Andrusyas, Igor Ciapurin et al., “Efficient power scaling of laser radiation by spectral beam combining,” Opt. Lett., 33(4), 384-38(2008)

[9] Pu Shi-ping, Jiang Zong-fu and Xu Xiao-jun, “Numercical analysis of spectral beam combining by volume Bragg grating,” High power laser and particle beams, 20(5),721-724 (2008)

[10] Ciapurin. I., Glebov L., and Smirnov V., “Modeling of phase volume diffractive gratings, part 1: transmitting sinusoidal uniform gratings”, Opt. Eng. 45(1) 015802 (2006)

[11]Yingyan Yi, Deming Liu, “Modeling of reflecting sinusoidal uniform phase volune diffraction gratings,” Proc.of SPIE, 7516, 75160D (2009)

[12] Kogelnik, H., “Coupled wave theory for thick hologram gratings”, Bell Syst. Tech. J.48, 2909-2945(1969)