LETTER

Design and investigation of a dual-layer grating coupler for efficient vertical fiber-chip coupling

To cite this article: Jiyao Yu and Hirohito Yamada 2019 Appl. Phys. Express 12 012004

View the article online for updates and enhancements.

This content was downloaded from IP address 142.132.1.147 on 12/12/2018 at 17:29

# Design and investigation of a dual-layer grating coupler for efficient vertical fiber-chip coupling

Jiyao Yu* and Hirohito Yamada

Graduate School of Engineering, Tohoku University, Aramaki Aza-Aoba 6-6-05, Sendai, 980-8579, Japan

*E-mail: yu.jiyao.q1@dc.tohoku.ac.jp

Received September 21, 2018; accepted November 14, 2018; published online December 11, 2018

A novel dual-layer grating coupler was designed for efficient vertical coupling between a single-mode fiber and silicon nanowires, with characteristics of polarization diversity and both wavelength bands of 1.3 and $1.55\ \mu\text{m}$. Theoretical analysis and two-dimensional finite-difference time-domain simulations were applied to verify the performance of the design. Optimized results show that the coupling efficiencies of a dual-port output of $41\%$ ($-3.87$ dB) for transverse-electric polarization at $1.56\ \mu\text{m}$, $32.88\%$ ($-4.83$ dB) for transverse-magnetic (TM) polarization at $1.58\ \mu\text{m}$, and $27.06\%$ ($-5.68$ dB) for TM polarization at $1.32\ \mu\text{m}$ can be achieved. Dual-layer Fabry-Perot resonance was also investigated for high coupling efficiency. © 2018 The Japan Society of Applied Physics

P hotonic integrated chips (PICs) with a submicrometer size based on a silicon-on-insulator platform attracted much attention at the beginning of this century to meet the growing demands of data rate. $^{1,2)}$ Various active and passive devices have been developed on the platform, such as optical switches, $^{3,4)}$ modulators, $^{5,6)}$ lasers, $^{7,8)}$ and polarization splitters. $^{9)}$ Integrated photonic waveguides have also been proved to be potential techniques for photonic quantum information experiments, such as entangled photon sources and buffers. $^{10,11)}$ Although high integration benefits from the small size, connecting PICs with single-mode fibers (SMFs) (approximate core size of $10\ \mu\text{m}$) is still a problem.

Generally, there are two ways to achieve data transmission between PICs and fibers: inverse tapers and grating couplers (GCs). The former group, which relies on adiabatically expanding silicon waveguide modes through a taper to match with a fiber, provides total communication; however, a perfect connection between the cross sections of the taper end and fiber is necessary. In addition, a taper length (several hundreds of micrometers) is needed to adiabatically convert fiber modes to waveguide modes. $^{12,13)}$ GC, with out-of-plane coupling, is another popular device for efficient coupling between fibers and waveguides. Considering one-dimensional (1D) gratings with high wavelength and polarization sensitivities, several kinds of 1D-GCs are demonstrated at the specific wavelength and polarization state. $^{14-18)}$ To achieve polarization diversity, two-dimensional (2D) gratings are a promising solution, studied in both theory and experiments. $^{19-22)}$ However, 2D gratings couple orthogonal polarization states of a single mode fiber to the same waveguide mode; moreover, the optimization and fabrication of 2D gratings are also a complex work.

Tilted incidence, instead of normal incidence, is a popular choice to avoid the polarization and wavelength sensitivities. With a proper design of grating parameters and fiber tilted angles, phase-matching conditions can be satisfied between the propagation modes of waveguides and fibers. Reference 23 developed a polarization separation GC for transverse-electric (TE) and transverse-magnetic (TM) polarization at $1.55\ \mu\text{m}$. Reference 24 designed a 2D bi-wavelength polarization- splitting GC. Reference 25 have recently reported a dual- band unidirectional GC for TE polarization based on a SiN platform. However, in these cases, coupling efficiency is quite sensitive to the tilted angle, which leads to extra cost of the mounting of fibers and GCs. Instead of tilted fibers, Ref. 26 reported a tilted grating. However, the fabrication complexity makes it difficult to apply in the commercial packaging. To ensure vertical coupling, gratings with asymmetric trapezoidal holes and dual-etched types have also been investigated. $^{27-30)}$ Although perfect vertical coupling, high efficiency, and broad bandwidth have been achieved, the coupling was limited at a specific wavelength and polarization. To balance the vertical coupling, polarization and wavelength diversity are still the main problems in recent research.

In this work, a dual-layer GC consisting of two 1D gratings was proposed for perfect vertical fiber-chip coupling with both wavelength and polarization diversities. The first grating was designed with a long period and deep-etch depth to function as a beam splitter, which could efficiently convert vertical incident fiber waves into tilted diffracted waves. The second grating was designed with a short period and shallow- etch depth to diffract the tilted waves a second time. By properly designing the parameters of two gratings and silicon waveguides, phase-matching conditions for normal incident waves and waveguide modes can be satisfied. A dual-layer grating equation accompanied by finite-difference time-do- main (FDTD) simulations was applied to verify the correct- ness of the design. The settings of FDTD simulation are introduced as follows. First, the two gratings were set with enough periods (15 and 30 for the top and bottom grating, respectively) making the overall length of two gratings slightly larger than the core diameter of the SMF ($10\ \mu\text{m}$). Then, the computational domain of a uniform orthogonal 2D mesh was used. The ends of the domain were terminated by perfectly matched layers. The grid size was $10\ \text{nm}$ for both directions for high calculation resolution. Results show that for TM-polarized waves at $1.55\ \mu\text{m}$, both TE- and TM- polarized waves at approximately $1.55\ \mu\text{m}$ were effectively coupled from a SMF to waveguides through vertical inci- dence. To the best of the authors' knowledge, this research is the first report of a vertical incidence GC with characteristics of polarization and wavelength diversities.

Figure 1 shows the schematic of the proposed dual-layer GC for vertical coupling with a SMF. The first top-grating, which functions as a beam splitter, was designed with a long period and deep-etch depth. Low index difference materials of $\text{Si}_3\text{N}_4$ ($n_{\text{Si}_3\text{N}_4}=2$) and $\text{SiO}_2$ ($n_{\text{SiO}_2}=1.45$) are applied in this grating for minimizing the effect of polarization and back-reflection. The pitch period and etch depth of the grating are represented by $\Lambda_r$ and $d_r$, respectively. The second bottom-grating was designed with a short period and

![](./images/812820489402580995_1.jpg)

Fig. 1. (Color online) Schematic of a dual-layer grating coupler for vertical coupling with a single-mode fiber and silicon slab waveguides.

shallow-etch depth for splitting the beam again. This is done to satisfy the phase-matching conditions of silicon waveguides (with a height of $d_{\text{Si}}$). The pitch period and etch depth of the grating are represented by $\Lambda_{c}$ and $d_{c}$, respectively. The two gratings are separated by a $\text{SiO}_{2}$ gap layer with a height of $d_{\text{gap}}$. For simplification, both gratings were designed with duty cycles of 0.5. $\text{Si}_{3}\text{N}_{4}$ and $\text{SiO}_{2}$ were used as the top and bottom cladding layers. The whole device was established on a silicon substrate.

The working principle of the dual-layer GC is shown as follows. Incident beams with TE (electric field lies strictly along the $y$ direction) and TM (magnetic field lies strictly along the $y$ direction) polarization states from a SMF are diffracted in directions after they pass through the first grating. Then, when those tilted waves pass through the second grating, they are diffracted again to satisfy the propagation modes of silicon waveguides. Equations (1) and (2) represent the diffraction equations for the first and second grating, respectively

$$
k_{0} * N_{\text{eff}\_t}=k_{0} * n_{\text{Si}_{3}\text{N}_{4}} * \sin(\theta)-(\pm i)\frac{2\pi}{\Lambda_{t}}, \tag{1}
$$

$$
k_{0} * N_{\text{eff}\_c}=k_{0} * N_{\text{eff}\_t}-(\pm i)\frac{2\pi}{\Lambda_{c}}, \tag{2}
$$

where $k_{0}=2\pi/\lambda$ is the free space wave number, $N_{\text{eff}\_t}$ and $N_{\text{eff}\_c}$ are the effective refractive indices of the diffracted waves by the first and second-layer grating, respectively, $n_{\text{Si}_{3}\text{N}_{4}}$ is the refractive index of silicon nitrite, $\theta$ is the incident angle of the SMF ($\theta=0$ for vertical incidence), $i$ is the integer of diffraction order (usually $i=1$), and $\Lambda_{t}$ and $\Lambda_{c}$ are grating periods of the first- and second-layer grating, respectively. By substituting $\theta=0$, $i=1$, eliminating $k_{0}$ and medium variable $N_{\text{eff}\_t}$, Eq. (3) is obtained for representing the dual-layer grating equation

$$
N_{\text{eff}\_c}=(\pm 1)\frac{\lambda}{\Lambda_{t}}+(\pm 1)\frac{\lambda}{\Lambda_{c}}. \tag{3}
$$

To perform effective coupling with diffracted waves and waveguides, $N_{\text{eff}\_c}$ from Eq. (3) should be satisfied with the propagation modes of waveguides. In a typical silicon slab waveguide, shown in Fig. 1, guiding conditions are only determined by waveguide height $d_{\text{Si}}$. Thus, a proper design of a group of $[\Lambda_{t}\ \Lambda_{c}\ d_{\text{Si}}]$ is key. In addition, to achieve high coupling efficiencies, high diffraction efficiencies of two gratings are necessary. However, compared with the second shallow-etched grating, the first deep-etched grating shows more space for manipulation. Thus, before the results of the phase-matching conditions are presented, the characteristics of the first grating (beam splitter) are explained.

![](./images/812820489402580995_2.jpg)

Fig. 2. (Color online) Calculated normalized efficiencies of the first-order diffracted waves of the top grating as functions of $\Lambda_{t}$ and $d_{t}$: (a) for TE at 1.3 $\mu$m, (b) for TM at 1.3 $\mu$m, (c) for TE at 1.55 $\mu$m, and (d) for TM at 1.55 $\mu$m. The maximum efficiency is limited by 50%.

Because diffraction occurs equally on two directions with central mirror symmetry, it is enough to consider only a single side of the first grating. Figures 2(a)-2(d) represent the 2D-FDTD results of the normalized efficiency of the first-order diffracted waves of a single side (maximum efficiency is limited by 50%) as functions of $\Lambda_{t}$ and $d_{t}$ for TE and TM polarization at 1.3 and 1.55 $\mu$m, which are the most used optical bands. From those figures, it is clear that diffraction efficiency varies greatly with $d_{t}$ and slightly with $\Lambda_{t}$. The diffraction behaves the same for TE and TM polarization at the same wavelength. Peak efficiency larger than 35% appeared at $d_{t}=1.23$ and $d_{t}=1.48\ \mu$m for wavelengths at 1.3 and 1.55 $\mu$m, respectively. Although several higher-order diffracted waves appear with the increase of $\Lambda_{t}$, the principle of high efficiency can still be roughly explained as the minimum of the 0th transmitted waves, leading to the enhancement of first-order diffracted waves. When the phase delay difference of the 0th-order waves passing through the $\text{SiO}_{2}$ and $\text{Si}_{3}\text{N}_{4}$ equals a half wavelength, the deconstructed interference condition is satisfied, leading to the minimum of 0th-order waves. Equation (4) is used for the calculation of the condition of deconstructed interference.

$$
n_{\text{Si}_{3}\text{N}_{4}}*d_{t}-n_{\text{SiO}_{2}}*d_{t}=n*\frac{\lambda}{2} \tag{4}
$$

where $n$ is an integer, and $n_{\text{Si}_{3}\text{N}_{4}}$ and $n_{\text{SiO}_{2}}$ are the refractive indices of $\text{Si}_{3}\text{N}_{4}$ and $\text{SiO}_{2}$, respectively. The results from Eq. (4) represent $d_{t}=1.185$ and $1.41\ \mu$m for wavelengths of 1.3 and 1.55 $\mu$m, respectively, which are approximately the values shown in Fig. 2. However, $d_{t}$ must be considered a fixed value in the realistic design, indicating a trade-off for high efficiencies at 1.3 and 1.55 $\mu$m. Next, the diffracted

![](./images/812820489402580995_3.jpg)

Fig. 3. (Color online) Calculated angles (degree) of the first-order diffracted waves of the top grating as functions of $\Lambda_t$ and $d_t$: (a) for TE at 1.3 $\mu$m, (b) for TM at 1.3 $\mu$m, (c) for TE at 1.55 $\mu$m, and (d) for TM at 1.55 $\mu$m.

![](./images/812820489402580995_4.jpg)

Fig. 4. (Color online) Possible phase-matching conditions of the diffracted waves by the bottom grating and propagation modes of silicon slab waveguides: (a) for one side input and (b) for one port output. ($\text{TE}_1$ mode is not taken into consideration in the phase match condition.)

angle of the first-order diffracted waves is shown in Fig. 3. Again, for simplification, only a single side is considered. It is clear from the figures that diffracted angles only vary with $\Lambda_t$. The diffracted angles also behave the same for different polarization states at the same wavelength. Equation (1) could be used to calculate the angles for verification. Little diversities may come from the calculation roughness. A high-efficiency transmission grating has now been successfully designed with controllable angles.

To determine the phase-matching conditions, defined by a group of $[\Lambda_t, \Lambda_c, d_{\text{Si}}]$, is the key work in this study. Figure 4(a) shows one possible configuration of a polarization separation design for one-side input (only the $-1$st-order diffracted waves generated by the first grating are considered). The waves diffracted by the second grating originally expect to be designed with the matching of waveguide modes of $\text{TM}_0$ and $\text{TE}_1$ at 1.3, and $\text{TE}_0$ and $\text{TM}_0$ at 1.55 $\mu$m. However, in further calculations, all conditions could not be satisfied simultaneously. Thus, the phase-matching condition of $\text{TE}_1$ at 1.3 $\mu$m is not taken into consideration in later work, because fundamental modes show more meanings. In addition, symmetric diffracted waves ($+1$st by the first grating) appeared on the other side. Figure 4(b) shows the output characteristics for two sides' input and one port output. It is clear that $\text{TM}_0$ at 1.3 and $\text{TE}_0$ and $\text{TM}_0$ at 1.55 $\mu$m should output at one port. Meanwhile, the opposite port shows the same behaviors.

According to the above analysis, the optimized values of $\Lambda_t$, $\Lambda_c$, and $d_{\text{Si}}$ are set to 4.1, 0.63, and 0.26 $\mu$m. $d_t$ is optimized to 1.3 $\mu$m to balance the efficiency of the first grating at both wavelengths. $d_c$ is set to 0.06 $\mu$m for a proper value. $^{24)}$ $d_{\text{gap}}$ and $d_{\text{box}}$ are both optimized with a value of 1.75 $\mu$m, as explained later. Figure 5(a) shows the results of the phase-matching conditions described by Fig. 4(a). The results are calculated by Eq. (3) and dispersion relations of silicon slab waveguides with parameters mentioned above. In Fig. 5(a), real lines represent the effective refractive indices of $\text{TE}_{0,1}$ and $\text{TM}_{0,1}$ modes for a silicon slab waveguide. Dashed lines represent the effective refractive indices of the twice-diffracted waves shown in Fig. 4(a), where $-1$ and $+1$ represent the orders of $-1$st and $+1$st diffracted waves. The cross points represent the phase-matching conditions, marked by symbols A–D. Because point A does not match the design demand, only B–D are considered. Symbol B can be described as the matching of the $-1$st-order waves diffracted the second time with the $\text{TM}_0$ guided mode at approximately 1.3 $\mu$m. The same explanation can be applied to symbols C and D. Then, to verify the effectiveness of the design, a 2D-FDTD simulation is shown in Fig. 5(b). Four peaks can be observed, and they are marked in order of A–D. Each peak represents a corresponding cross-point in Fig. 5(a). Again, Peak A is not taken into consideration. Comparison of Fig. 5(a) and 5(b) shows that the design works as desired. Peak B represents the output of the $\text{TM}_0$ mode at 1.3223 $\mu$m with a normalized efficiency of 13.53% (27.06% for two ports) and a 3 dB bandwidth of 47 nm. Peaks C and D represent the output of the $\text{TE}_0$ and $\text{TM}_0$ modes at 1.5826 and 1.5625 $\mu$m with normalized efficiencies of 20.51% (41%) and 16.44% (32.88%), and 3 dB bandwidths of 49 and 34 nm, respectively. The distortion of the calculated wavelength and desired wavelength comes from the slight shift of phase-matching conditions (currently three) in the optimization, which would become unacceptable for four. The above results show a successful design of a dual-layer GC for the first time, giving characteristics of polarization diversity and a dual-wavelength response. The electric field for TE polarization and magnitude field for TM polarization give a Gaussian-field profile, indicating the fundamental modes, which are not shown here. We should also note that the total efficiencies of peaks B–D depend on the depth of the gap layer ($d_{\text{gap}}$) and box layer ($d_{\text{box}}$). A kind of two-layer Fabry–Perot (FP) interference is predicted at the two layers. High efficiency demands on the effective design of the depth of the two layers. Figure 6 shows the calculated results of coupling efficiency for two ports (single port $\times 2$) for TE polarization at 1.55 $\mu$m as an example, where coupling efficiencies

![](./images/812820489402580995_5.jpg)

Fig. 5. (Color online) Calculated phase-matching conditions as a function of wavelength described by Fig. 4(a): (a) theoretical results by Eq. (3) and dispersion relations of silicon waveguides with $[\Lambda, \Lambda_{c}, d_{Si}]=[4.1, 0.63, 0.26\ \mu m]$ and (b) FDTD results.

![](./images/812820489402580995_6.jpg)

Fig. 6. (Color online) Example of coupling efficiency (two ports) of a dual-layer Fabry–Perot resonance as functions of $d_{gap}$ and $d_{box}$ for TE polarization at $1.55\ \mu m$.

periodically vary with the increasing of $d_{gap}$ and $d_{box}$. Because the FP interference of light depends on wavelength, there is another trade-off to get high efficiency at 1.3 and $1.55\ \mu m$. In addition, the choice of large value of $d_{gap}$ can effectively avoid the evanescent coupling between two gratings, indicating that there is no need for $x$-direction alignment of two gratings.

In conclusion, a dual-layer GC was designed and calculated for perfect vertical coupling between a SMF and silicon nanowires. This is the first report of such a dual-layer design, which functions as polarization diversity and both wavelength bands of 1.3 and $1.55\ \mu m$. First, a long-period and deep-etched grating (functioning as a beam splitter) was designed with a high diffraction efficiency and proposed angle. Next, a short-period and shallow-etched grating was designed for effective matching with silicon nanowires. The principle of phase-matching conditions was introduced by utilizing a dual-layer grating equation. The coupling efficiency and bandwidth were calculated by 2D-FDTD simulations. The optimized results exhibited a two-port output of $41\%$ ($-3.87$ dB) for $TE_{0}$ at $1.5625\ \mu m$, $32.88\%$ ($-4.83$ dB) for $TM_{0}$ at $1.5826\ \mu m$, and $27.06\%$ ($-5.68$ dB) for $TM_{0}$ at $1.3223\ \mu m$ with 3 dB bandwidths of 49, 47, and 34 nm, respectively. Two-layer FP resonance was also investigated for realistic fabrication guidance. The efficiency could be further increased with the assembling of either top or bottom anti-reflection layers. The current two-port output can be varied to a single-port output by inserting distributed Bragg reflectors at an arbitrary location for each port. However, the designs of both broadband anti-reflection layers and distributed Bragg reflectors are difficult.

1) R. Soref, IEEE J. Sel. Top. Quantum 12, 1678 (2006).
2) H. Subbaraman, X. Xu, A. Hosseini, X. Zhang, Y. Zhang, D. Kwong, and R. T. Chen, Opt. Express 23, 2487 (2015).
3) T. Chu, H. Yamada, S. Ishida, and Y. Arakawa, Opt. Express 13, 10109 (2005).
4) T. Volz, A. Reinhard, M. Winger, A. Badolato, K. J. Hennessy, E. L. Hu, and A. Imamoglu, Nat. Photonics 6, 605 (2012).
5) A. Liu, R. Jones, L. Liao, D. S. Rubio, D. Rubin, O. Cohen, R. Nicolaescu, and M. Paniccia, Nature 427, 615 (2004).
6) G. T. Reed, G. Mashanovich, F. Y. Gardes, and D. J. Thomson, Nat. Photonics 4, 518 (2010).
7) T. Kita, N. Yamamoto, T. Kawanishi, and H. Yamada, Appl. Phys. Express 8, 062701 (2015).
8) T. Kita, N. Yamamoto, A. Matsumoto, T. Kawanishi, and H. Yamada, Jpn. J. Appl. Phys. 55, 04EH11 (2016).
9) D. Dai and J. E. Bowers, Opt. Express 19, 10940 (2011).
10) N. Matsuda, H. Nishi, P. Karkus, T. Tsuchizawa, K. Yamada, W. J. Munro, K. Shimizu, and H. Takesue, J. Opt. 19, 124005 (2017).
11) H. Takesue, N. Matsuda, E. Kuramochi, W. J. Munro, and M. Notomi, Nat. Commun. 4, 2725 (2013).
12) H. Park, S. Kim, J. Park, J. Joo, and G. Kim, Opt. Express 21, 29313 (2013).
13) B. B. Bakir, A. V. D. Gyves, R. Orobtchouk, P. Lyan, C. Porzier, A. Roman, and J. M. Fedeli, IEEE Photonics Technol. Lett. 22, 739 (2010).
14) H. Yamada, M. Nozawa, M. Kinoshita, and K. Ohashi, Opt. Express 19, 698 (2011).
15) D. Taillaert, W. Bogaerts, P. Bienstman, T. F. Krauss, P. V. Daele, I. Moerman, S. Verstuyft, K. D. Mesel, and R. Baets, IEEE J. Quantum Electron. 38, 949 (2002).
16) D. Taillaert, F. V. Laere, M. Ayre, W. Bogaerts, D. V. Thourhout, P. Bienstman, and R. Baets, Jpn. J. Appl. Phys. 45, 6071 (2006).
17) J. Unshida, M. Tokushima, Y. Sobu, D. Shimura, K. Yashiki, S. Takahashi, and K. Kurata, Jpn. J. Appl. Phys. 57, 052502 (2018).
18) J. H. Song and X. Rottenberg, IEEE Photonics Technol. Lett. 29, 389 (2017).
19) X. Chen, C. Li, and H. K. Tsang, Opt. Commun. 283, 2146 (2010).
20) D. Taillaert, H. Chong, P. I. Borel, L. H. Frandsen, R. M. D. L. Rue, and R. Baets, IEEE Photonics Technol. Lett. 15, 1249 (2003).
21) T. Katayama, J. Ito, and H. Kawaguchi, Appl. Phys. Express 9, 072703 (2016).
22) X. Chen and H. K. Tsang, Opt. Lett. 36, 796 (2011).
23) Y. Tang, D. Dai, and S. He, IEEE Photonics Technol. Lett. 21, 242 (2009).

012004-4

© 2018 The Japan Society of Applied Physics

24) M. Streshinsky, R. Shi, A. Novack, R. T. P. Cher, A. E. J. Lim, P. G. Q. Lo, T. B. Jones, and M. Hochberg, Opt. Express 21, 31019 (2013).

25) S. Nambiar, M. Hemalatha, T. Sharma, and S. K. Selvaraja, CLEO/Europe- EQEC, 2017.

26) S. Wang, Y. Hong, Y. Zhu, J. Chen, S. Gao, X. Cai, Y. Shi, and L. Liu, Opt. Express 25, 22032 (2017).

27) A. Mizutani, Y. Eto, and H. Kikuta, Appl. Phys. Express 10, 122501 (2017).

28) A. Michaels and E. Yablonovitch, Opt. Express 26, 4766 (2018).

29) M. Dai, L. Ma, Y. Xu, M. Lu, X. Liu, and Y. Chen, Opt. Express 23, 1691 (2015).

30) T. Watanabe, M. Ayata, U. Koch, Y. Fedoryshyn, and J. Leuthold, J. Lightwave Technol. 35, 4663 (2017).