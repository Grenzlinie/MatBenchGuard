# Non-periodic high-index contrast gratings reflector with large-angle beam forming ability

Wenjing Fang, Yongqing Huang*, Xiaofeng Duan, Jiarui Fei, Xiaomin Ren, Min Mao

State Key Laboratory of Information Photonics and Optical Communications, Beijing University of Posts and Telecommunications, Beijing 100876, China

---

## ARTICLE INFO
**Article history:**
Received 19 August 2015
Received in revised form
31 December 2015
Accepted 9 January 2016

**Keywords:**
Gratings
Subwavelength structures
Phase shift
Reflectors

## ABSTRACT
A non-periodic high-index contrast gratings (HCGs) reflector on SOl wafer with large-angle beam forming ability has been proposed and fabricated. The proposed reflector was designed using rigorous coupled-wave analysis (RCWA) and finite-element-method (FEM). A deflection angle of $17.35^{\circ}$ and high reflectivity of $92.31\%$ are achieved under transverse magnetic (TM) polarized light in numerical simulation. Experimental results show that the reflected power peaked at $17.2^{\circ}$ under a 1550 nm incident light, which is in good accordance with the simulation results. Moreover, the reflected power spectrum was also measured. Under different incident wavelengths around 1550 nm, reflected powers all peaked at $17.2^{\circ}$. The results show that the proposed non-periodic HCGs reflector has a good reflection and beam forming ability in a wavelength range as wide as 40 nm around 1550 nm.

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction

High-index contrast gratings (HCGs) [1-3] have attracted great attention recently due to its high reflectivity over a broad bandwidth and ability to control the phase shift of the reflected or transmitted light. Owning to its simple and compact structure, HCGs have become a promising alternative to replace conventional reflectors in many optical devices, such as vertical-cavity surface-emitting lasers (VCSELs) [4,5] and reflective enhanced photodetectors [6]. In addition, with different designs, HCGs are suitable for numbers of different applications, including high efficiency transmission and reflection filters [7], optical couplers with the excitation of surface plasmons [8], and polarization-insensitive reflectors [9], etc. Another important property of HCGs is that the phase of the reflected or transmitted light can be manipulated while keeping a high reflectivity or transmittance. This property can be applied to non-periodic HCGs [10-13]. Reference [12] has shown focusing reflectors and lenses obtained by changing the phase of reflected and transmitted light from non-periodic HCGs. Reference [13] has demonstrated that reflectors can be designed by controlling the phase of transmitted light to steer the propagation direction of the transmitted light under vertical incidence condition. However, the deflection angle is small and the transmittance property is not satisfactory. So, it's necessary to study reflectors with high reflectivity and large-angle beam forming ability using non-periodic HCGs. These mirrors will be great promises for integrated optical devices due to their simple fabrication and good beam forming property.

In this paper, we study the fundamental properties of the non-periodic HCGs to design the phase front of reflected light and formulate useful design rules for realizing practical structures. Based on these rules, a non-periodic HCGs reflector with a deflection angle of $17.35^{\circ}$ and a high reflectivity of $92.31\%$ is designed and simulated using rigorous coupled-wave analysis (RCWA) [14] and finite-element-method (FEM) [15] at the designed wavelength of 1550 nm. The designed non-periodic HCGs structure can be easily fabricated with a combination process of electron beam (EB) lithography [16] and inductively coupled-plasma (ICP) etching. We experimentally demonstrate that the maximum reflected power is obtained at $17.2^{\circ}$ at 1550 nm wavelength, which is in good accordance with the simulated value. Moreover, the reflected power spectrum was also measured. Under different incident wavelengths around 1550 nm, the maximum reflected powers were all obtained at $17.2^{\circ}$. The results show a good reflection and beam forming ability at a range of 40 nm around 1550 nm for proposed non-periodic HCGs reflector.

## 2. Theoretical background

HCGs are sub-wavelength gratings comprised of high index bars fully surrounded by low index media. In sub-wavelength gratings (SWGs), the first-order diffracted mode does not correspond to freely propagating lights, but to a guided wave trapped in dielectric layers. The trapped wave is scattered into the zeroth diffracted order and interferes with the incident light to create a

---

*Corresponding author.
E-mail address: yhhuang@bupt.edu.cn (Y. Huang.)

http://dx.doi.org/10.1016/j.optcom.2016.01.025
0030-4018/© 2016 Elsevier B.V. All rights reserved.

![](./images/814563526071812097_1.jpg)
![](./images/814563526071812097_2.jpg)

Fig. 1. (a) Schematic diagram of the investigated non-periodic HCGs with linear phase response. (b) Cross-section diagram of the non-periodic HCGs structure.

![](./images/814563526071812097_3.jpg)
![](./images/814563526071812097_4.jpg)

Fig. 2. Contour map of the reflection and phase properties (a) reflectivity and (b) the matching phase shift of periodic HCGs versus grating period (Λ) and bar width (s) for TM-polarized light at 1550 nm wavelength.

pronounced modulation of transmission and reflection. The guided waves in a HCG are rapidly scattered and do not propagate very far laterally. In this case, it is appropriate to think of the grating as a coupled resonator system. High reflection and transmission features can be achieved since the elimination of non-zero diffraction orders increases the coupling efficiency. When a periodic HCG was illuminated by a wave, phase variations will be developed by the varying structural parameters, such as the gratings period (Λ) and bar width (s). The phase is spatially dependent on these grating structural parameters. The beam forming of reflection light can be realized by properly choosing the phase distribution to form a linear phase shift of the reflected light at the reflect plane.

Fig. 1(a) shows the schematic of the investigated non-periodic HCGs. The electric field of the reflected light is a power envelop with the expression of $E(x,z)=E_{0}(x,z)\exp(jk_{0}(x\sin\theta+z\sin\theta))$, where $k_{0}=2\pi/\lambda$ is the wave number at the wavelength $\lambda$, and $\theta$ is the angle between the reflected light wave vector and the negative z-axis. For a fixed z coordinate, the phase of the reflected light can be written as

$$
\Phi(x)=k_{0}x\sin\theta+c \tag{1}
$$

where $c$ is a constant. Since the phase profile is linear, Eq. (1) can be written as $\Phi(x)=\alpha x$, $\alpha=k_{0}\sin\theta$, where $\alpha$ is a proportional factor which depends on the phase difference $\Delta\Phi$ determined by width $d$ of the non-periodic HCGs as shown in Fig. 1(b). The proportional factor is $\alpha=\frac{\Delta\Phi}{d}$, then the deflecting angle $\theta$ is obtained by

$$
\theta=\arcsin^{-1}\left(\frac{\Delta\Phi}{dk_{0}}\right) \tag{2}
$$

The deflected angle $\theta$ is determined by the designed parameters $\Delta\Phi$, grating width $d$ and wavelength $\lambda$. At a certain wavelength and the gratings width, larger deflected angle can be obtained by increasing the total phase shift. Therefore, with the structure size d is determined by the requirements, the only way to achieve a bigger tilting angle is to feature a larger phase difference $\Delta\Phi$.

### 3. Design and simulations

For design of a non-periodic HCGs with beam forming ability, the most important part is the selection of a set of proper grating period and bar width calculated from Eq. (1) to realize a linear phase profile. The next step is to find out a one-one correspondence between the HCG's reflection and dimensions. In this work, the non-periodic HCGs was designed as a reflector with a deflecting angle of $20^{\circ}$. The structure is implemented on a SOI wafer consisting of a 500 nm silicon layer $(t_{g})$ and a 500 nm buried oxide layer $(t_{l})$ as depicted in Fig. 1(a). The refractive indexes of Si and buried $SiO_{2}$ are 3.47 and 1.47, respectively. For a certain grating layer thickness, the periodic HCGs' reflection properties, as of reflectivity and phase shift, are investigated using RCWA simulation method under TM polarized illumination. In this approach, the structure's periodicity is exploited to solve Maxwell's equations. A linear system of equations is built from the boundary conditions. The system solution yields the field distribution, as well as the reflection characteristics. This result serves as a look-up table to find a set of grating parameters which can provide the targeted phase and reflectivity.

Shown in Fig. 2, the reflectivity and phase shift property of the periodic HCGs are simulated using RCWA method for TM polarization at 1550 nm. The thickness of the grating is kept constant at 500 nm, while the period varies from $0.3\ \mu\text{m}$ to $1.2\ \mu\text{m}$, and the bar width of grating varies from $0.2\ \mu\text{m}$ to $0.7\ \mu\text{m}$. Fig. 2(a) shows the reflectivity of periodic HCGs. Fig. 2(b) shows the phase shift of reflected light which cover a full $2\pi$ shifting within the high reflectivity region. Realizing a full $2\pi$ phase shift in the high reflectivity region is very important due to the need of arbitrary phase front control. According to the look-up tables, a set of useful discrete data, $(\Lambda_{n},s_{n})$, corresponding to the maximum reflectivity $R_{max}(\Lambda_{n},s_{n})$ for phase covering a full $2\pi$ shifts, can be chosen to

![](./images/814563526071812097_5.jpg)

Fig. 3. (a) Phase distribution, red line denotes the ideal phase profile, and blue points denote the designed phase distribution of the reflector. (b) Maps of period and grating bar of designed reflector, blue triangles represent the period of gratings, and green five-pointed stars represent the width of grating bars.

![](./images/814563526071812097_6.jpg)

Fig. 4. Simulation results of designed non-periodic HCGs for beamforming. (a) E-field intensity distribution of reflected light. (b) E-field intensity profile at different distances.

design the required reflector. The subscript is an integer corre- sponding to each point of the map. Each period and bar width are found, in the one by one optimization process, corresponding to the target phase distribution obtained from Eq. (1).

While keeping the reflectivity within the required range, the maximum phase shift obtained from Fig. 3(b) is approximately $\Delta \phi=13.4$ rad. The total width of the non-periodic HCG is $9.66 \mu m$. And the deflecting angle of the final structure, estimated using Eq. (2), is $\theta=20^{\circ}$.

Fig. 3 shows the phase distribution and the useful structural parameters for designing a non-periodic HCGs reflector with beam forming ability. As illustrated in Fig. 3(a), the red line represents the ideal phase distribution for a non-periodic HCGs reflector calculated by Eq. (1) with a deflecting angle $20^{\circ}$, and the blue points represent the designed discrete phase shifts corresponding to $(\Lambda_{n}, s_{n})$. The dimensions of the periods and the grating bars selected to design a non-periodic HCGs reflector are well visible in Fig. 3(b). The blue triangles represent the width of the periods, and the green stars represent the width of the grating bars. The bar width varies from $0.2 \mu m$ to $0.7 \mu m$, and the period varies from $0.6 \mu m$ to $0.9 \mu m$. These points specify the widths and positions of each bar in the HCGs.

As mentioned previously, this design process creates a final structure that is no longer periodic. The commercial software COMSOL implementing FEM method is used to analyze the non- periodic HCGs structure instead of RCWA. The light source is a TM polarized light wave with a Gaussian power envelope and the wavelength is 1550 nm. In order to avoid the reflection inter- ference, perfectly matched layer (PML) and scattering boundary condition are used. In the FEM simulation, we include 14 Si bars of those phase profiles are given in Fig. 3(a). The total phase variation of 13.4 rad is required to design the non-periodic HCGs reflector with a width of $9.66 \mu m$ and a deflecting angle of $20^{\circ}$. The simu lation results shown in Fig. 4 confirm the beamforming ability of a non-periodic HCG reflector working at 1550 nm wavelength with TM polarization. Fig. 4(a) shows the distributions of the E-field intensity of the reflected lights. A deflected reflected beam can be gained owning to the linear phase modulation. Fig. 4(b) shows the E-field intensity profile at distances of $18 \mu m, 20 \mu m, 22 \mu m$, and24 um from the reflected plane, respectively. The peak of E-field intensity profile clearly moves toward the negative x-axis direction.

![](./images/814563526071812097_7.jpg)

Fig. 5. E-filed intensity distribution of reflected light at $z=18 \mu m$ with the variation of the incident wavelength.

With the distance from the reflection plane moving from 18 to $24 \mu m$, the electric field intensity profile peak moves $1.875 \mu m$ toward lower x coordinates. The obtained deflecting angle in the

![](./images/814563526071812097_8.jpg)

Fig. 6. Optical microscope picture of a fabricated non-periodic HCGs reflector. The groove width in different locations is shown in SEM images in the insets.

![](./images/814563526071812097_9.jpg)

Fig. 7. Experimental setup for measurement of reflected light at TM polarization incident light.

simulation is $\theta = \tan^{-1}(1.876/6) = 17.35^\circ$, which is very close to the targeted value $20^\circ$. The total reflectivity for the non-periodic HCGs reflector is $92.31\%$ by calculation. This small deviation can be attributed to the discrete phases in the center of the non-periodic HCG rather than the continuous phases as Eq. (1) indicate.

The designed non-periodic HCGs reflector not only has a high reflectivity for incident light at 1550 nm wavelength but also shows a 40 nm wavelength range of high reflection around 1550 nm. While the incident light wavelength varies from 1530 nm to 1570 nm with an interval of about 5 nm, the corresponding E-filed intensity distributions of the reflected lights at $z=18\ \mu$m are calculated and shown in Fig. 5. The line forms are almost consistent. The peaks of each line have no drift along $x$-axis, but there is some small changes in the peak intensity. Therefore, within this spectral range, the wavelength has no

![](./images/814563526071812097_10.jpg)

Fig. 8. Experimental results. (a) Power spectrum with the incident wavelength of 1550 nm at different angle $\theta$. (b) Received power at different angle.

![](./images/814563526071812097_11.jpg)
![](./images/814563526071812097_12.jpg)

Fig. 9. (a) The power of reflected light under different wavelength at 17.2°, (b) The profile of incident light and reflected light at 1550 nm.

impact on the deflection angle of reflected beam, but only has some small effect on the E-field intensity of the reflected beam.

## 4. Experimental measurements

The above designed non-periodic HCG structure was then fabricated. An EB resist (ZEP520) was spin-coated on a SOI wafer which consists of a 500-nm-thick silicon layer and a 500 nm-thick buried oxide layer. The grating patterns were defined by electron-beam lithography. Then, using the EB resist as a mask, the silicon grooves were formed by inductively coupled-plasma (ICP) etching by using C4F8 and SF6 as etchants. The etching depth was controlled by etching time. The etching rate of the silicon was 21 nm/ min. Finally, the residual EB resist was removed with a 1:1 solution of $H_2SO_4$ and $H_2O_2$.The fabricated device has grating periods ranging from $d_{min}$=634 nm to $d_{max}$=894 nm, covering a square of $500\ \mu m \times 500\ \mu m$ and containing 632 periods. An optical microscope image of the fabricated non-periodic HCGs reflector is shown in Fig. 6, together with scanning electron microscope images of the silicon grooves at different locations.

The experimental setup used for the characterization experiments performed to proof the beam forming ability of the designed non-periodic HCGs is depicted in Fig. 7. A continuously tunable laser with output power of 1mw is used as the light source and the input power of 0.97 mw is obtained by the large-area photodetector. The laser output is coupled to a polarization controller to form a TM polarized light. The light was then collected by a polarization-maintaining photonic crystal fiber (PM-PCF) with a mode diameter of $10.5\pm1.0\ \mu m$ to maintain the TM polarization while the light propagates though the fiber. An aspheric lens is used to collimate the incident light at the grating position with a waist of $100\ \mu m$. The overall grating structure has a total width of $500\ \mu m$, the waist of the reflected beam should be around 200- $300\ \mu m$. Both PM-PCF and the tapered fiber are mounted on two five-axis displacement stages which include three translation and two rotation. The PM-PCF and aspheric lens have to be aligned to each other in order to form a maximum input power. The reflected light beam was picked by a tapered fiber with a mode dimension of 4-5 $\mu m$ at a distance of $300\ \mu m$ in front of the grating. The tapered fiber have to be adjusted to the same plane with the PM-PCF by adjusting the translation stages in order to obtain a maximum coupling efficiency and, at the same time, optimal angle is measured by an angle measuring instrument with a precision of $\pm0.2^{\circ}$. Then, the translation stage was adjusted toward both sides of the optimized angle to obtain the reflected optical powers at different angles. The reflected light was recorded by an optical spectrum analyzer.

The experimental results are shown in Fig. 8. The power of reflected light is measured at different angles from $16.4^{\circ}$ to $17.4^{\circ}$. Fig. 8(a) shows the received power spectrum of the reflected light with a wavelength of 1550 nm at different angle $\theta$. The received power of the reflected light at different angle from $16.4^{\circ}$ to $17.4^{\circ}$ is shown in Fig. 8(b). The peak power of the reflected light appears at $17.2^{\circ}$, which is in excellent agreement with the theoretical value of $17.35^{\circ}$ for the designed grating. The power spectrums at different angles have little changes in shape and no drift with each other. The result shows good deflected ability of reflected beam. The reflectance measured is lower than 92.31% due to proximity effects in the electron-beam lithography step and the deviations in the measurement process.

The powers of the reflected light are measured at wavelengths around 1550 nm, of which intervals are about 5 nm. The powers are measured at $17.2^{\circ}$. The results are shown in Fig. 9(a). As shown, the received powers at different wavelengths didn't change a lot, which agree with the simulation results shown in Fig. 5. Fig. 9 (b) shows the normalized intensity profile of the incident light and the reflected light of the reflector at 1550 nm wavelength. It shown a good agreement in spectrum profile. So the reflector has a property of broadband wavelength response, which originates from the broadband nature and wavelength scalability of HCGs. The results demonstrates the wide spectrum operation ability of the designed non-periodic HCGs.

## 5. Conclusions

In this paper, a non-periodic HCGs reflector with large-angle beam forming ability on SOI wafer is presented, which is designed by phase front manipulation of reflected beam. By FEM numerical simulation, a deflected angle of $17.35^{\circ}$ and a high reflectivity of 92.31% are obtained for TM polarization at 1550 nm. Then the non-periodic HCGs reflector is fabricated. We have experimentally demonstrated that the maximum reflected power appears at $17.2^{\circ}$, which is in excellent agreement with the simulation results. The deflecting angle of $17.2^{\circ}$ is stable under different wavelength. It shows the good reflection and beam forming ability of the non-periodic HCGs reflector. And a deflected reflected beam spectrum range of 40 nm around 1550 nm is obtained experimentally. Moreover, the approach proposed in this paper can be used to obtain arbitrary-angle beam forming ability HCGs reflector, and thus broadens a series of possible applications in integrated optoelectronic devices.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant nos. 61274044, 61077049), the National Basic Research Program of China (Grant no. 2010CB327600),

the Specialized Research Fund for the Doctoral Program of China (Grant no. 20130005130001), and the Natural Science Foundation of Beijing, China (Grant no. 4132069).

## References

[1] C.J. Chang-Hasnain, W. Yang, High-contrast gratings for integrated optoelectronics, Adv. Opt. Photonics 4 (2012) 379-440.

[2] V. Karagodsky, F.G. Sedgwick, C.J. Chang-Hasnain, Theoretical analysis of subwavelength high contrast grating reflectors, Opt. Express 18 (2010) 16973-16988.

[3] V. Karagodsky, C.J. Chang-Hasnain, Physics of near-wavelength high contrast gratings, Opt. Express 20 (2012) 10888-10895.

[4] Y. Zhou, M.C.Y. Huang, C.J. Chang-Hasnain, Large fabrication tolerance for VCSELs using high contrast grating, IEEE Photonics Technol. Lett. 20 (2008) 434-436.

[5] C. Chase, Y. Rao, W. Hofmann, C.J. Chang-Hasnain, 1550 nm high contrast grating VCSEL, Opt. Express 18 (2010) 15461-15466.

[6] X. Duan, Y. Huang, X. Ren, Y. Shang, X. Fan, F. Hu, High-efficiency InGaAs/In-Pphotodetector incorporating SOI-based concentric circular subwavelength gratings, IEEE Photonics Technol. Lett. 24 (2012) 863-865.

[7] S. Tibuleac, R. Magnusson, Reflection and transmission guided-mode resonance filters, J. Opt. Soc. Am. A 14 (1997) 1617-1626.

[8] H.F. Ghaemi, T. Thio, D.E. Grupp, T.W. Ebbesen, H. Jezec, Surface plasmons enhance optical transmission through subwavelength holes, Phys. Rev. B 58 (1998) 6779-6782.

[9] R. Zhang, Y.F. Wang, Y.J. Zhang, Z.G. Feng, F. Qi, L. Liu, W.H. Zheng, Broadband and polarization-insensitive subwavelength grating reflector for the near-infrared region, Chin. Opt. Lett. 12 (2014) 020502-1-020502-3.

[10] Changlian Ma, Yongqing Huang, Xiaofeng Duan, et al., High-transmittivity non-periodic sub - wavelength high - contrast grating with large - angle beam - steering ability, Chin. Opt. Lett. 12 (2014) 120501-1-120501-4.

[11] Xiaodong Ting Ma, Weimin Yuan, Wei Ye, Shiqiao Xu, Qin, Zhihong Zhu, High focusing grating reflectors with TE-polarized normal incidence, Chin. Opt. Lett. 12 (2014) 020501-1-020501-5.

[12] D. Fattal, J. Li, Z. Peng, M. Fiorentino, R.G. Beausoleil, Flat dielectric grating reflectors with focusing abilities, Nat. Photonics 4 (2010) 466-470.

[13] L. Carletti, R. Malureanu, J. Mrk, I.S. Chung, High-index-contrast grating reflector with steering ability for the transmitted beam, Opt. Express 19 (2011) 23567-23572.

[14] M.G. Moharam, E.B. Grann, D.A. Pommet, T.K. Gaylord, Formulation for stable and efficient implementation of the rigorous coupled-wave analysis of binary gratings, J. Opt. Soc. Am. A 12 (1995) 1068-1076.

[15] O.C. Zienkiewicz, R.L. Taylor, The Finite Element Method: Basic Formulation and Linear Problems, McGrow-Hill, 6th ed., 2005, ISBN 0-7506-6320-0.

[16] T. Fujita, H. Nishihara, J. Koyama, Blazed gratings and Fresnel lenses fabricated by electron-beam lithography, Opt. Lett. 7 (1982) 578-580.