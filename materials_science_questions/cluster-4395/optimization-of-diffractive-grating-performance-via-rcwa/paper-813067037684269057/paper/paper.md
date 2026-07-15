# A Thickness-varying Sub-wavelength Grating Focusing Lens for TE Polarization Light

Min Zhang, Yongqing Huang, Wenjing Fang, Huize Fan, Xiaofeng Duan, Kai Liu, Xiaomin Ren
State Key Laboratory of Information Photonics and Optical Communications, Beijing University of Posts and Telecommunications
No 10, Xitucheng Road, Haidian District, Beijing, 100876, China yqhuang@bupt.edu.cn

**Abstract:** A focusing lens for TE polarization light based on silicon sub-wavelength gratings using two different thicknesses is proposed. The properties are numerically studied with Finite Element Method (FEM). Total transmissivity is 72% and the full-width-half-maximum (FWHM) at focal plane is 0.8µm at a wavelength of 1550nm.

## 1. Introduction
With the rapid development of micro-nano machining technology, the miniaturization of integrated optical devices is becoming more and more obvious. The high-contrast sub-wavelength gratings (HCGs), whose grating period is smaller than the wavelength of the incident light and which have only zero order diffraction at normal incidence, have received wide attention [1]. Novel types of high-reflectivity HCG mirrors have recently been proposed and have become a promising alternative to distributed Bragg reflection dielectric stacks for broadband, high-reflectivity filtering applications [1-4]. However, few articles have previously discussed HCG focusing lenses or reflectors for TE (the electric field vector parallel to the grating bars) polarization light.

In this paper, we present a novel method to design gratings with double thickness for normal incidence of TE polarization light. With the method of Rigorous Coupled Wave Analysis (RCWA), we can obtain a total phase shift of $2\pi$ rad continuously [4] by changing the period, duty cycle and thickness of each grating bar simultaneously. We proposed a new type of focusing lens for TE polarization light based on HCGs at normal incidence. Total transmissivity is 72% and the FWHM at focal plane is 0.8µm at a wavelength of 1550nm.

## 2. Theory and structure
The proposed flat focusing sub-wavelength grating lens is consisted of one-layer non-periodic silicon grating bars with two different thicknesses (shown in Fig.1). Every grating bar is surrounded by air. As is shown in Fig.1, $n_1$ and $n_2$ are the refractive indices of the air and the silicon grating bars, respectively. The parameters of this one-layer HCG are period ($\Lambda$), bar width ($\omega$), and thickness ($t_g$). The duty cycle $\tau$ is defined as the ratio of bar width to period, $\tau$=$\omega$/$\Lambda$. The parameters $\Lambda$, $\omega$ and $t_g$ are changing with the x-coordinate. For this structure, the focusing feature depends on the phase manipulation of transmitted beams. The transmittance and the phase shift of HCGs depend only on the local geometry, so we can study the distribution of the grating phase shift by geometry theory. By choosing sets of parameters (period, duty cycle and thickness) of the silicon bars, we can obtain a total phase shift of $2\pi$ rad continuously at normal incidence of TE polarization light.

![](./images/813067037684269057_1.jpg)

Fig. 1. Schematic of proposed sub-wavelength gratings

In order to design the grating structure to achieve the focusing effect at normal incidence, the phase shift of the diffraction light $\Phi$(x) must satisfy Eq. (2) [4] when the silicon bars are distributed along x axis.

$$
\Phi(\mathrm{x})=\frac{2 \pi}{\lambda}\left(\sqrt{\mathrm{x}^{2}+\mathrm{f}^{2}}-\mathrm{f}\right)+\Phi_{0} \tag{2}
$$

In Eq. (2), x is the coordinate of the center for the silicon bar and $\Phi_0$ is the initial phase. When the phase shift $\Phi$(x) is more than $2\pi$, it can be mapped to an equivalent value between 0 and $2\pi$.

## 3. Design process
This focusing lens for TE polarization light is one-layer non-periodic HCGs with $n_1$=1 and $n_2$=3.48. In order to design this structure, we calculate the transmittivity and phase shift at the transmission plane as a function of ($\Lambda$, $\tau$) of periodic HCG using RCWA shown in Fig. 2. Fig.2 (a) and (b) are the results at $t_g$=1.3µm and (c) and (d) at $t_g$=1.2µm. The period and duty cycle of each silicon bar vary from 0.4µm to 1.2µm and 0.2 to 0.9, respectively.

![](./images/813067037684269057_2.jpg)

Fig. 2. (a) and (b) are the transmittivity and phase shift of periodic HCG at $t_g$=1.3µm, respectively; (c) and (d) are the transmittivity and phase shift of periodic HCG at $t_g$=1.2µm, respectively.


Firstly, select proper grating parameters $(\Lambda, \tau)$ whose transmittivity is more than 90% from Fig.2 (a) ($\text{t}_\text{g}$=1.3$\mu$m) and Fig.2 (c) ($\text{t}_\text{g}$=1.2$\mu$m). Then sort the phase shift, as shown in Fig.3 (a) and (b), whose parameters $(\Lambda, \tau)$ are chosen from the first step.

![](./images/813067037684269057_3.jpg)

Fig.3. (a) sorted phase shift with $\text{t}_\text{g}$=1.3$\mu$m, (b) sorted phase shift with $\text{t}_\text{g}$=1.2$\mu$m and (c) sorted transmittance phase shift after combination (the front phase shift data are taken from $\text{t}_\text{g}$=1.3$\mu$m, and the following phase shift data are taken from $\text{t}_\text{g}$=1.2$\mu$m).

In Fig.3 (a), ranging from 3 rad to $2\pi$ rad at thickness of 1.3$\mu$m, there are some phase shift points with large differences, and that's why we don't use a single thickness. Meanwhile in Fig.3 (b), at thickness of 1.2$\mu$m, the phase shift points with large differences appears in range from 0 rad to 3 rad. So, we take these two kinds of thicknesses into consideration simultaneously. The final phase shift design results are shown in Fig.3(c).

Finally, we calculate the phase shift $\Phi(\text{x})$ according to the Eq. (2). The focal length (f) designed in this paper is 7$\mu$m. Select the first point in Fig.3 (c) as $\Phi_0$. According to the design process, we design a focusing sub-wavelength grating lens. The parameters (period, duty cycle and thickness) and the corresponding discrete phase shift distribution of the designed gratings are shown in Fig.4 [5]. The total size is 26$\mu$m.

![](./images/813067037684269057_4.jpg)

Fig. 4. The detailed grating parameters of period (red dot), duty cycle (blue triangle), thickness (pink triangle) and the phase shift (black square) of the designed structure.

### 4. Numerical simulation and discussions
The performance of the designed focusing grating lens is numerically studied using FEM as shown in Fig.5. The TE polarization light is vertical to the plane of the grating bars and focuses to the other side shown in Fig. 5 (a). The focal length from the bottom of Si bars is f=7.2$\mu$m which is very close to the theoretical value 7$\mu$m. The FWHM at focal plane is 0.8$\mu$m and the total transmittance is 72% by calculation.

![](./images/813067037684269057_5.jpg)

Fig. 5. Intensity distribution of E-field for TE polarization light.

### 5. Conclusions
In this paper, we have proposed and demonstrated a focusing thickness-varying sub-wavelength grating lens for TE polarization light. We choose two different thicknesses to obtain a total phase shift of $2\pi$ rad continuously. The design method and the design process are given in detail. The proposed sub-wavelength grating structure is obtained by the method of RCWA. And the properties are numerically studied using FEM. Total transmissivity is 72% and the FWHM at focal plane is 0.8$\mu$m at a wavelength of 1550nm.

### Acknowledgments
This work was supported by the National Natural Science Foundation of China (Grant No. 61574019, 61674018 and 61674020), the Specialized Research Fund for the Doctoral Program of Higher Education of China (Grant No. 20130005130001), the Beijing Municipality Natural Science Foundation (Grant No. 4132069).

### References
[1] C. J. Chang-Hasnain and Weijian Yang, "High-contrast gratings for integrated optoelectronics", Optics and Photonics **4**, 379–440 (2012).

[2] V. Karagodsky, F. G. Sedgwick, and C. J. Chang-Hasnain, "Theoretical analysis of subwavelength high contrast grating reflectors," Opt. Express **18(16)**, 16973-16988 (2010).

[3] Y. Zhou, M. C. Y. Huang, C. Chase, V. Karagodsky, M. Moewe, B. Pesala, F. G. Sedgwick and C. J. Chang-Hasnain, "High-Index-Contrast Grating (HCG) and Its Applications in Optoelectronic Devices," IEEE J. Sel. Top. Quantum Electron. **15(5)**, 1485–1499 (2009).

[4] F. Lu, F. G. Sedgwick, V. Karagodsky, C. Chase and Connie J. Chang-Hasnain, "Planar high-numerical-aperture low-loss focusing reflectors and lenses using subwavelength high contrast gratings," Opt Express **18(12)**, 12606-12614 (2010).

[5] Changlian Ma, Yongqing Huang, Xiaofeng Duan, and Xiaomin Ren, "High-transmittivity non-periodic sub-wavelength high-contrast grating with large-angle beam-steering ability," Chin. Opt. Lett., **12(12)**, 120501-1 – 120501-4 (2014).