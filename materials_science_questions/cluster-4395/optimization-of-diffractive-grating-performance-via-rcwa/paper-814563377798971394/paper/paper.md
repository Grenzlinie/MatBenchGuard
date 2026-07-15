# Guided-mode resonance in curved grating structures

Yasuo Ohtera,* Shohei Iijima, and Hirohito Yamada

Graduate School of Engineering, Tohoku University, Sendai 980-8579 Japan

*Corresponding author: ohtera@ecei.tohoku.ac.jp

Received February 24, 2011; accepted March 21, 2011;
posted April 5, 2011 (Doc. ID 142926); published April 29, 2011

The guided-mode resonance phenomenon in curved grating structures was studied. By using finite-difference time-domain simulation in the cylindrical coordinate system, we investigated the dependence of the peak reflectivity and bandwidth of the resonance upon the curvature radius. We clarified that the reflectivity and bandwidth were similar to those of flat grating structures for a finite range of curvature. We also discussed the key factor that determines the performance of reflection. © 2011 Optical Society of America

OCIS codes: 050.1950, 130.2790, 260.5740.

Resonant coupling between leaky modes of a periodic waveguide and an external plane wave is called guided-mode resonance (GMR) and is an important and useful phenomenon for creating transmission- and reflection-type optical filters with a simple device structure [1,2]. Various light handling functions such as band rejection [3], bandpass [4], and polarization selection [5] have been proposed and demonstrated, and work has now started on developing prototype components such as high-power laser mirrors, micro-electro-mechanical-system-driven tunable mirrors [6], and arrayed filters [7].

The basic mechanism and properties of GMR are described in detail in [8,9], for example. In summary, resonant reflection occurs when the wave vector of a diffracted wave of an incident plane wave coincides with that of a leaky mode of the periodic waveguide [8]. When such a condition is satisfied, all the rays reflected back to the incident space interfere constructively, thus increasing the reflectivity. Therefore, for resonance to occur, all the unit cells of the periodic waveguide must be excited coherently. The waveguide and wavefront of the incident wave need not be flat to achieve this. If we illuminate a periodic waveguide on a curved substrate with a wavefront having the same curvature, similar resonant reflection is expected to occur. If a curved resonant grating is found to be attainable, it would open the door to another class of grating-assisted photonic elements such as parabolic mirrors, grating couplers, and beam concentrators.

Most research on GMR has dealt with periodic waveguides on a flat substrate, and so the incident light has been assumed to be plane waves. Divergence from the ideal configuration (plane wave + infinite flat grating) was found to degrade the resonance spectra [10]. The aim of this study was to confirm whether or not resonant reflection occurs for the curved grating geometry and to investigate the differences in basic resonance characteristics between flat and curved structures.

A schematic view of the sample waveguides used for the analysis is illustrated in Fig. 1. The structures are assumed to extend infinitely along the $z$ direction. For the flat structure, shallow rectangular grooves having a pitch of $\Lambda_0$ and duty ratio of $1:1$ are formed on the upper surface of the guiding layer. The refractive index of the core is 2.1, assuming high-index oxide materials ($\text{Nb}_2\text{O}_5$, etc.). The upper and lower spaces of the guiding layer are assumed to be filled with uniform media of $n = 1.0$ (air) and $n = 1.45$ (silica substrate), respectively. The full thickness of the core and the depth of the gratings were $0.45\Lambda_0$ and $0.05\Lambda_0$, respectively. For the curved structure shown in Fig. 1(b), the thickness and depth of the grooves were set to be the same as those of the flat structure. The radial position $h = 0.2125\Lambda_0$ (= half the average core thickness) from the outer surface of the guiding layer was defined as the center of the core (indicated by a dashed line in Fig. 1(b)). The curvature radius ($\rho$) was defined as the distance from the center of the curvature to the center of the core. The azimuthal angle of a unit structure, $\theta_0$, was adjusted to around $\theta_0 \simeq \Lambda_0/\rho$ for each radius so that the peak wavelength of the reflection (if found) became identical to that of the flat structure. Throughout this study, we focused on TE-mode resonance, i.e., the $E$ field normal to the plane.

The reflection characteristics of this curved grating were calculated using a cylindrical coordinate version of the finite-difference time-domain (FDTD) method [11]. The analytical space is shown in Fig. 2. The inner and outer bounds in the radial direction were terminated by perfectly matched layers (PMLs), while the azimuthal ($\theta$) extent of the space was truncated by $\theta_0$ with periodic boundary conditions. We placed an arc-shaped $E_z$ distribution in the middle of the inner space, indicated by "A" in Fig. 2 at $t = 0$, and released it to propagate freely.

![](./images/814563377798971394_1.jpg)

Fig. 1. (Color online) Schematic view of the sample resonant gratings. (a) Flat structure, (b) Curved structure. Dotted lines indicate wavefronts.

![](./images/814563377798971394_2.jpg)

Fig. 2. Schematic of the analytical space for the cylindrical FDTD calculation.

Some portion of the diverging wave is reflected by the grating and returns back to the center, while the remainder escapes to the outer space. The average axial component of the $E$ field $(E_{z})$ and the azimuthal component of the $H$ field $(H_{\theta})$ were monitored at the outer surface of the grating (indicated by "B" in Fig. 2). After the time-domain loop, they were Fourier transformed and multiplied to yield the radial component of the Poynting vector. The same procedure was repeated for the uniform space to obtain the spectrum of the launched power. The former was converted to the transmittance, $T(\lambda)$, by normalizing it by the latter. Reflectivity was then calculated by $R(\lambda)=1-T(\lambda)$.

An example of the reflection spectra for various curvatures is plotted in Fig. 3. We focused on the wavelength range where the lowest-order GMR peak for the flat grating appeared. Resonance peaks were clearly observed for finite curvatures, and they maintained $>99\%$ peak reflectivity for $\rho>8\Lambda_{0}$. The relation between the curvature and peak reflectivity is plotted in Fig. 4 together with the bandwidth (FWHM). Note that the range of both wavelength and the acceptance angle of incidence are expected to increase as the refractive index modulation of the grating becomes higher. This will enable wide band or wide incidence angle reflectors. On the other hand, if the curved grating is illuminated with a nonconcentric wave, the reflection spectra will be degraded, with a drop in peak reflectivity and broadening of the bandwidth. This situation is similar to the illumination of flat gratings with a Gaussian beam.

This result confirms that the reflection performance remains high at small curvature, but begins to drop at about $\Lambda_{0}/\rho\sim0.15$. The mechanism of this characteristic can be roughly explained as follows: a resonant grating can be regarded as a cavity system as well as a leaky-mode waveguide. A part of its guided power, confined in the core, is always radiating into the claddings. The ratio of the average power leakage to the stored modal energy determines the quality factor $(Q)$ as a resonant cavity. If the structure is flat, there are only two paths for the leakage (radiation into both claddings). On the other hand, if the grating is curved, a bending loss is added as a new leakage path. The quality factor of the resonance will remain similar to that of the flat grating, as long as the bending loss is small compared to the original radiation. However, once it exceeds the radiation loss, the $Q$ factor starts to decrease, causing the peak reflectivity to drop and the bandwidth to increase.

![](./images/814563377798971394_3.jpg)

Fig. 3. (Color online) Reflection spectra of TE modes $(E_{z},H_{\theta}$, and $H_{r})$ for various curvatures.

![](./images/814563377798971394_4.jpg)

Fig. 4. Dependence of reflection characteristics on the curvature. Solid lines are peak reflectivity and bandwidth (FWHM). Dotted line denotes the propagation distance of the leaky mode.

We also plotted the propagation distance of the leaky mode where its amplitude is attenuated by $1/e$, as shown in Fig. 4 by a dotted line. There is a clear correlation

![](./images/814563377798971394_5.jpg)

Fig. 5. (Color online) Instantaneous field pattern of the gratings at the resonance wavelength. (a) Amplitude of $E_{z}$ (Media 1), (b) $H_{r}\cdot W_{0}$ where $W_{0}=\sqrt{\mu_{0}\varepsilon_{0}}$ is the impedance in vacuum (Media 2). (c) $E_{z}$ (Media 3). (a) and (b) are for $\rho=8\Lambda_{0}$, and (c) is for $\rho=2.9\Lambda_{0}$.

between the peak reflectivity and the length. This result indicates that the drop in reflectivity could be changed if we can tailor the spatial decay constant of the leaky mode by designing the refractive index profile.

We also calculated the electromagnetic field pattern at the resonant wavelength. The complex field pattern, $F(r,\theta,\lambda)$, is first extracted by specifying the resonant wavelength, and its instantaneous amplitudes are calculated by $F(r,\theta,t) = \mathrm{Re}\{e^{i\omega t}F(r,\theta,\lambda)\}$. Field patterns of the TE mode for $\rho = 8\Lambda_0$, which is about the lower limit of the curvature radius for the mirror performance to be maintained, are displayed in Figs. 5(a) and 5(b), respectively. The outer PML is out of the drawing range. The fields are drawn in the same color scale. The concentric pattern of $E_z$ implies that the main direction of radiation is radial. The whole diameter of the grating "ring" is about $20\Lambda_0$. This result indicates that a huge curvature radius is not needed in order to construct elements such as beam concentrators and cylindrical cavities using this geometry in future. Figure 5(b) shows the nonzero radial $H$ field far outside the grating. Its pattern can be regarded as a superposition of two radiated fields having curved wavefronts; they propagate obliquely with respect to the azimuthal direction. In the flat structure, such an $H$ field (perpendicular to the waveguide) has no amplitude except for the near field of the grating, so it is obvious that the curved field was created by the bending of the waveguide. This result provides evidence for the hypothesis of the curvature versus reflectivity relation described above. We also displayed $E_z$ for a small radius structure ($\rho = 2.9\Lambda_0$) in Fig. 5(c). Strong variation in the azimuthal direction outside the ring represents the radiated field due to the large bending loss of the leaky mode.

From these results, we conclude that the GMR phenomenon still takes place in grating waveguides with curved geometry when illuminated by an appropriate diverging wave. If a ring-shaped grating is excited by a circular or point source, a concentric convergent wave is returned back toward the center of the curvature. Numerical simulation also clarified that a similar electromagnetic field pattern, except for the radiation due to the waveguide bending, was formed at resonance frequencies, the same as for ordinary flat grating waveguides.

### References

1. S. S. Wang and R. Magnusson, Appl. Opt. **32**, 2606 (1993).
2. Y. Ding and R. Magnusson, Opt. Express **12**, 5661 (2004).
3. S. S. Wang and R. Magnusson, Opt. Lett. **19**, 919 (1994).
4. R. Magnusson and S. S. Wang, Appl. Opt. **34**, 8106 (1995).
5. A. Lehmuskero, I. Vartiainen, T. Saastamoinen, T. Alasaarela, and M. Kuittinen, Opt. Express **18**, 27270 (2010).
6. K. Hane, T. Kobayashi, F.-R. Hu, and Y. Kanamori, Appl. Phys. Lett. **88**, 141109 (2006).
7. D. W. Peters, R. R. Boye, J. R. Wendt, R. A. Kellogg, S. A. Kemme, T. R. Carter, and S. Samora, Opt. Lett. **35**, 3201 (2010).
8. D. Rosenblatt, A. Sharon, and A. A. Friesem, IEEE J. Quantum Electron. **33**, 2038 (1997).
9. S. Fan and J. D. Joannopoulos, Phys. Rev. B **65**, 235112 (2002).
10. D. W. Peters, S. A. Kemme, and G. R. Hadley, J. Opt. Soc. Am. A **21**, 981 (2004).
11. A. Taflove, *Computational Electrodynamics: The Finite-Difference Time-Domain Method* (Artech, 1995).