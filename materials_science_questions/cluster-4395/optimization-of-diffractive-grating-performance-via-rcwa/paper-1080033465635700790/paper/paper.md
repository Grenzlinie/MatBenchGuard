# High-efficiency, cryogenic-compatible grating couplers on an AlN-on-sapphire platform through bottom-side coupling

YIYU ZHOU¹, MOHAN SHEN¹, CHUNZHEN LI¹, LIKAI YANG¹, JIACHENG XIE¹, AND HONG X. TANG¹,*

¹ Department of Electrical Engineering, Yale University, New Haven, Connecticut 06520, USA
*hong.tang@yale.edu

Compiled December 25, 2024

Sapphire is a commonly used substrate for wide-bandgap III-nitride photonic materials. However, its relatively high refractive index results in low transmission efficiency in grating couplers. Here, we propose and demonstrate that the transmission efficiency can be significantly enhanced by bottom-side coupling. A metal reflector is deposited on the top side of the chip, and the fiber array is glued to the bottom side of the substrate. We experimentally achieve a transmission efficiency as high as 42% per coupler on an aluminum nitride (AlN) on sapphire platform at the telecom wavelength. In addition, the grating couplers show a robust performance at a cryogenic temperature as low as 3 K for both transverse-electric (TE) and transverse-magnetic (TM) modes. Our results can be useful to a wide range of sapphire-based applications that require low coupling loss and cryogenic operation.

http://dx.doi.org/10.1364/ao.XX.XXXXXX

Grating couplers play a crucial role for integrated silicon photonics as an efficient and compact interface for fiber-to-chip coupling. Thanks to the large refractive index contrast between silicon and silicon dioxide, the transmission efficiency on a silicon-on-insulator wafer has approached 50% per coupler [1], and it can be further improved to >80% per coupler by using a bottom metal reflector [2–4]. On the other hand, wide-bandgap III-nitride semiconductors, such as aluminum nitride (AlN) and gallium nitride (GaN), are emerging as integrated photonics materials due to the presence of second-order optical nonlinearity. In particular, AlN has been extensively investigated as a promising platform for a variety of nonlinear optical applications [5, 6], including electro-optic modulation [7, 8], microwave-to-optical transduction [9–15], quantum optics [16], second-harmonic generation [17], soliton and micro-comb generation [18–22], Raman lasers [23, 24], and optical frequency shifting [25]. However, for the consideration of lattice matching, high-quality single-crystalline AlN is typically deposited on the sapphire substrate. The low refractive index contrast between AlN ($n \approx 2.1$) and sapphire ($n \approx 1.7$) has thus impeded the development of efficient AlN-on-sapphire grating couplers, and the transmission efficiency is lower than 25% per coupler even in simulation [26]. Attempts have been made to enhance the transmission efficiency by applying a silicon layer on AlN, and the simulated efficiency can achieve 60% per coupler, while the experimentally measured efficiency is reported to be 28% per coupler [27]. A commonly used method to enhance the transmission efficiency in silicon photonics is to use a bottom metal reflector [2–4] by etching the entire silicon substrate via deep reactive ion etching. However, this method is not applicable to sapphire because the sapphire substrate is both chemically and physically stable and thus does not allow efficient deep etching. Metal grating couplers [28, 29] present another approach to high coupling efficiency. However, metal grating couplers are not compatible with the high-temperature annealing process, which is often used to improve the optical quality factors of AlN resonators [10]. Edge coupling is another efficient method for AlN photonics, and a coupling loss of 2.8 dB per facet has been demonstrated [30]. However, edge coupling requires a large footprint, precise position alignment, and smoothly cleaved edges that are challenging for the sapphire substrate. Therefore, high-efficiency grating couplers remain highly desirable for AlN-on-sapphire photonics.

In this work, we propose and demonstrate a bottom-side coupling technique that can significantly enhance the transmission efficiency. We deposit a metal reflector on the top side of the grating couplers such that most light is scattered downward by the grating. An apodized grating design is adopted to focus the scattered light to the fiber array that is glued underneath the 430-μm-thick sapphire substrate. The transmission efficiency is measured to be as high as 42% per coupler. The grating coupler also presents similar transmission for both TE and TM modes simultaneously. We further test the robustness of the grating coupler at cryogenic temperatures by cooling down to 3 K, and the coupling efficiency remains nearly unchanged. The compatibility with the low temperature is useful to cryogenic applications such as microwave-to-optical transducers [9–15] and superconducting electro-optic modulators [31, 32], where the photonic chip needs to be placed in a cryogenic environment to enable the operation of superconducting circuits.

Grating coupler design. The design of the grating coupler is shown in Fig. 1(a). The AlN film thickness is 1 μm, and the grating etching depth is 400 nm. The sapphire substrate is double side polished and has a thickness of 430 μm. A 270-nm-thick SiO₂ layer is deposited at the bottom side as an anti-reflection coating. We use 2.7-μm-thick SiO₂ as the cladding, and 100 nm niobium (Nb) is deposited on the grating as a metal reflector. An angled fiber array is glued at the bottom side of the wafer. The light in the fiber is reflected towards the grating at the fiber tip due to the total internal reflection at the fiber-air interface. To illustrate the effect of the metal reflector, we launch the TM0 mode

![](./images/1080033465635700790_1.jpg)

Fig. 1. (a) The schematic of the AlN-on-sapphire grating coupler. The monitor plane is placed 3 μm under the AlN film in the simulation program. (b) The simulated normalized downward power ratio as a function of wavelength. (c) The simulated field amplitude distribution of the scattered field and the Gaussian fiber mode at the monitor plane. (d) The normalized transmission per coupler as a function of position misalignment.

in the on-chip waveguide and numerically calculate the downward scattering power ratio with and without the metal reflector using a commercial software (Ansys Lumerical FDTD) in a two-dimensional (2D) configuration. The normalized downward scattering power ratio is presented in Fig. 1(b). In the absence of a metal reflector, only ~40% of the light is directed to the fiber. By contrast, when a metal reflector is present, the downward scattering power ratio increases to as high as 95%, which validates the use of metal reflector. We note that we design the grating coupler for TM0 mode because we experimentally observed that the TM0 mode has higher quality factor compared to the TE0 mode.

We next investigate the design of grating structure. Each grating tooth can be viewed as a scatterer that directs a small amount of light to the fiber [33]. The scattering strength depends on several parameters such as the index contrast, the duty cycle, and the etching depth. In general, a high scattering strength is desirable because it allows a smaller scattered field size to match the fiber mode diameter. We simulate different etching depths for AlN on sapphire and eventually choose an etching depth of 400 nm, because a larger etching depth does not further enhance the scattering strength significantly. It is worth noting that the scattering strength of the grating can be appreciably tuned by adjusting the grating duty cycle in silicon photonics, thanks to the high refractive index contrast. Hence, by spatially varying the duty cycle, an apodized grating coupler can be designed to generate a Gaussian-like scattered field profile to match the fiber mode [33]. However, for AlN-on-sapphire platforms, we find that the scattering strength does not show significant dependence on the grating duty cycle as a consequence of the low index contrast, and thus the scattered field always shows a negative exponential distribution. The maximum coupling efficiency is therefore upper bonded to 80%, which is determined by the overlap between a Gaussian distribution and an exponential distribution [33]. To match the fiber Gaussian mode size to the scattered field size, we place the fiber array 320 μm underneath the sapphire bottom side. The fiber is polished at an angle of 41°, and thus the reflected fiber mode propagates at an angle of 12° with respect to the z axis in air. The diffraction angle of the grating is hence chosen to be 12° to match the angled fiber as shown in Fig. 1(a).

![](./images/1080033465635700790_2.jpg)

Fig. 2. (a) Design parameter of the grating coupler. (b) The optical micrograph and the scanning electron microscope (SEM) image of a grating coupler. The images are taken before the PECVD SiO₂ cladding is deposited. (c) The grating coupler measurement setup.

In the numerical simulation, we design the grating coupler for TM polarization and we launch the TM0 mode in the waveguide as the input mode. A monitor plane is placed 3 μm under the grating coupler. The scattered field profile is shown in Fig. 1(c). It can be seen that the scattered field size is significantly larger than the fiber mode field diameter of 10.6 μm. Therefore, we place the fiber 320 μm underneath the sapphire substrate. After propagation in air gap and sapphire substrate, the fiber mode field diameter at the monitor plane becomes as large as 110 μm as a consequence of divergence and thus matches the scattered field size. The fill factor and grating period are tuned to determine the diffraction angle $\theta$, and the relation can be

![](./images/1080033465635700790_3.jpg)

Fig. 3. The simulated and experimentally measured transmission per coupler for (a) TM mode and (b) TE mode at room temperature T=293 K. (c) The experimentally measured transmission per coupler for TE and TM modes at cryogenic temperature T=3 K. (d) The normalized transmission per coupler for position misalignment in the x dimension.

written as [34]
$$
\Lambda=\frac{\lambda}{n_{\mathrm{eff}}+\sin \theta},
\tag{1}
$$

$$
n_{\mathrm{eff}}=n_{\mathrm{wg}} \cdot F+n_{\mathrm{e}} \cdot(1-F),
$$
where $\lambda$ is the vacuum wavelength, $\Lambda$ is the grating period, $n_{\mathrm{eff}}$ is the effective index of a period, $F$ is the fill factor, $n_{\mathrm{wg}}=1.99$ is the eigenmode effective index in the unetched waveguide, and $n_{\mathrm{e}}=1.90$ is the eigenmode effective index of the etched waveguide. Due to the birefringence of single-crystalline AlN, the refractive index of AlN used in the simulation is $n_{\mathrm{TM}}=2.050$ and $n_{\mathrm{TE}}=2.016$ for TM and TE polarization, respectively. In our design, we use $\theta=12^{\circ}$ to match the beam deflection angle of the angled fiber as shown in Fig. 1(a), and the fill factor starts from 0.85 at $x=0$ and linearly decreases to 0.70 at $x=30 \mu \mathrm{m}$, then remains at 0.70 for $x>30 \mu \mathrm{m}$. Here $x=0$ is defined as the position of the first grating unit cell. To focus the scattered field to the fiber, we use an apodized design [33] based on spatially varying grating period. For a focusing Gaussian mode centered at $x_{c}$, its phase distribution can be written as $\phi(x)=-2 \pi\left(x-x_{c}\right)^{2} /\left(2 R_{z} \lambda\right)$, where $x_{c}$ is the center of the fiber Gaussian mode at the grating plane, $R_{z}$ is the radius of curvature of the wavefront at the grating plane and is determined by $R_{z}=l+\left(z_{R}^{2} / l\right), z_{R}=\pi \omega_{0}^{2} / \lambda$ is the fiber mode Rayleigh range, $\omega_{0}=5.2 \mu \mathrm{m}$ is the fiber beam waist radius, $l=\left(t_{\mathrm{sa}} / n_{\mathrm{sa}}\right)+t_{\mathrm{air}}$ is the equivalent path length in air between the fiber and the grating coupler, $n_{\mathrm{sa}}=1.74$ is the sapphire substrate refractive index, $t_{\mathrm{sa}}=430 \mu \mathrm{m}$ is the sapphire substrate thickness, and $t_{\text {air }}=320 \mu \mathrm{m}$ is the air gap thickness. The value of $x_{c}$ needs to be numerically optimized, and we use $x_{c}=43 \mu \mathrm{m}$ in our simulation. To imprint this phase distribution to the scattered field, we add a small length change $\Delta L$ to each grating period, which follows [33]

$$
\Delta L_{i}=\frac{\lambda}{2 \pi\left(n_{\mathrm{wg}}+\sin \theta\right)}\left(\phi_{i}-\phi_{i-1}\right),
\tag{2}
$$

where $\Delta L_{i}$ is the length change in the $i$-th unit cell, $\phi_{i}=\phi\left(x_{i}\right)$ is the phase at the position of the $i$-th unit cell $x_{i}$. Therefore, the total period of the $i$-th unit cell is $\Lambda+\Delta L_{i}$, and the length of the etched part is $L_{i}=\Lambda(1-F)$, as depicted in Fig. 2(a).

Fabrication and measurement. The $1-\mu$ m-thick AlN film is grown on double-side polished sapphire substrate with a thickness of $430 \mu \mathrm{m}$ using metal-organic chemical vapor deposition (MOCVD). To fabricate the grating, we deposit $175 \mathrm{~nm} \mathrm{SiO}_{2}$ on AlN as a hard mask by plasmaenhanced chemical vapor deposition (PECVD). Electron beam resist (CSAR 62) is then spin coated onto the $\mathrm{SiO}_{2}$ layer, and $10 \mathrm{~nm}$ gold is sputtered subsequently as a charge dissipation layer [35]. The resist is exposed by a $100 \mathrm{kV}$ electron beam pattern generator (EBPG 5200,Raith). We remove the gold layer by dipping in gold etchant for 2 minutes and then develop the resist by dipping in xylene for 45 seconds. We etch the $\mathrm{SiO}_{2}$ hard mask by $\mathrm{CHF}_{3} / \mathrm{O}_{2}$, and then etch the AlN layer by $\mathrm{Cl}_{2} / \mathrm{BCl}_{3} / \mathrm{Ar}$ in an Oxford 100 etcher [36]. The remaining $\mathrm{SiO}_{2}$ hard mask is removed by buffered oxide etch. The waveguides and microring resonators are fabricated in a separate step with an etching depth of $600 \mathrm{~nm}$. We note that the micro-ring resonators are used to inspect the waveguide propagation loss and polarization state on chip. The resonators have no effect on the performance of grating couplers and thus we do not further discuss their designs. $2.7 \mu \mathrm{m} \mathrm{SiO}_{2}$ is deposited on the grating by PECVD as the cladding. $100 \mathrm{~nm} \mathrm{Nb}$ is deposited on the grating areas by electron beam evaporation, and the pattern of $\mathrm{Nb}$ is defined by a photolithography lift-off process. A layer of $270 \mathrm{~nm}$ PECVD $\mathrm{SiO}_{2}$ is deposited at the bottom side of the sapphire substrate as an anti-reflection coating for telecom wavelengths. We note that the $\mathrm{Nb}$ reflector can be readily replaced by other commonly used metals such as gold and aluminum. The micrographs of the fabricated grating couplers are presented in Fig. 2(b). The fiber array is attached to the bottom side following a recipe similar to [32]. The device chip is first glued on a copper plate. A hole is drilled at the edge of the copper plate to make the chip bottom side accessible. The fiber array is aligned to the grating couplers and then glued to the chip bottom side using an ultraviolet-curable epoxy.

The measurement setup to characterize the grating couplers is shown in Fig. 2(c). We use a wavelength-tunable laser (TSL-710,Santec) as the light source to characterize the spectral response of the grating couplers. A three-paddle fiber polarization controller (FPC560,Thorlabs) is used to tune the polarization state of light, and a telecom fiber-coupled detector (2053-FC, New Focus) is used to measure the optical power. For room-temperature measurement, we first short connect the fibers to bypass the chip and measure the optical power $P_{0}$. We then connect fibers to the chip and measure its spectral response $P_{r t}(\lambda)$ by sweeping the laser wavelength $\lambda$. We then place the chip in a cryostat and measure the cryogenic response $P_{c}(\lambda)$. Each device on the chip has two grating couplers, one as input port and the other as output port. We assume that two grating couplers are identical, and thus the transmission per coupler can be computed as $\sqrt{P_{r t}(\lambda) / P_{0}}$ and $\sqrt{P_{c}(\lambda) / P_{0}}$, respectively. The simulated as well as the experimentally measured transmission results for at room temperature are presented in Fig. 3(a) for TM mode and Fig. 3(b) for TE mode. Resonance dips are visible in the measured spectrum due to the presence of micro-ring resonators. These resonances are useful for distinguishing the polarization states and have no effect on the coupling efficiency measurement. The simulation shows a maximum transmission of $70 \%$ (78%) per coupler, while the measured transmission is $42 \%$ (41%) per coupler

for TM (TE) mode. We attribute the slightly higher simulated efficiency of TE mode to its stronger grating scattering strength observed in the simulation, and the different peak wavelength is attributed to the different effective mode index and material birefringence. Regarding the discrepancy in efficiency between simulation and experiment, there are several possible reasons. First, the simulation is performed in a simplified 2D configuration along the radial dimension for time-efficient computations. We expect a three-dimensional (3D) simulation to produce a lower coupling efficiency due to the mode mismatch along the angular dimension. Second, we control the AlN etching depth by measuring the AlN thickness using an ellipsometer. However, an ellipsometer can only measure the thickness of a uniform film. The plasma etching process generally shows an aspect ratio dependence, and we expect the etching depth at the grating area to be smaller than the value measured by an ellipsometer [37]. In addition, the PECVD cladding is known to produce air voids at grating gaps [38], which can change the grating scattering strength unpredictably. The etching depth and air voids can potentially be characterized by inspecting the cleaved side of a chip using SEM, which we leave for future study. We also characterize the performance of six different grating couplers, and the average efficiency is 41.4% with a standard deviation of 1.6%, which validates the reproducibility of the structure. The tolerance to the fiber position misalignment is also estimated numerically. Based on the simulated scattered field distribution $E_s(x)$ and the fiber Gaussian mode $E_f(x)$ at the monitor plane (see Fig. 1(c)), the transmission under misalignment can be computed as $\left|\int E_{s}^{*}(x) E_{f}(x-\delta x) d x\right|^{2}$, where $\delta x$ is the position misalignment in the $x$ dimension. The results show a 3 dB tolerance of $8\ \mu\text{m}$ (see Fig. 3(d)).

To test the robustness of grating couplers at low temperatures, We put the chip in a cryostat which allows to cool down to T=3 K within 8 hours. The peak transmission is nearly unchanged, and the peak wavelength shows a slight shift of 3 nm as demonstrated in Fig. 3(b). We attribute the peak wavelength shift to the thermal contraction of the sapphire substrate during the cool down process. The 3 dB bandwidth of the coupler is measured to be 11 nm for TM mode and 13 nm for TE mode, which agrees well with the simulation result. The limited bandwidth stems from the large distance between the fiber and the grating coupler [34], which fundamentally is a result of the low index contrast between AlN and sapphire. We note that this bandwidth is sufficient for microwave-to-optical transducers, and it could potentially be improved by using silicon overlay layer [27] to enhance the index contrast. Although the grating coupler is designed for TM polarization, we notice that the a similar peak transmission of 41% can be achieved for TE polarization at T=3 K, which can be useful to applications that require both polarizations.

Conclusions. In summary, we experimentally demonstrate high-efficiency grating couplers on an AlN-on-sapphire platform via bottom-side coupling. The low index contrast between AlN and sapphire necessitates the large distance between the fiber and the grating for mode size matching. To enhance the scattering directionality, a metal layer is deposited on the top side of the grating coupler as a reflector, and the fiber array is hence attached to the bottom side of the double-side-polished substrate. An apodized design with spatially varying grating periods is adopted to focus the scattered field to the fiber. We experimentally achieved a peak transmission as high as 42% per coupler for TM polarization, both at room temperature T=293 K and cryogenic temperature T=3 K, which allows for compatibility with superconducting quantum circuits [9–15]. In addition, the grating coupler simultaneously support the transmission of both TE and TM polarizations with similar peak transmission and bandwidth. We believe that our design is not only useful to AlN-on-sapphire platform, but also can benefit other low-index-contrast sapphire-based platform such as silicon nitride on sapphire [39] and lithium niobate on sapphire [14, 40] substrates.

Funding. Co-design Center for Quantum Advantage (DE-SC0012704); Army Research Office (W911NF2410029).

Acknowledgment. The authors thank Dr. Yong Sun, Dr. Michael Rooks, Dr. Lauren McCabe, Dr. Yeongjae Shin, and Kelly Woods for assistance in device fabrication. The authors acknowledge the support from Yale Quantum Institute, Yale University Cleanroom, and Yale Institute for Nanoscience and Quantum Engineering.

Disclosures. The authors declare no conflicts of interest.

Data availability. Data underlying the results presented in this paper are not publicly available at this time but may be obtained from the authors upon reasonable request.

## REFERENCES
1. D. S. Zemtsov, D. M. Zhigunov, S. S. Kosolobov, *et al.*, Opt. Lett. **47**, 3339 (2022).
2. W. S. Zaoui, A. Kunze, W. Vogel, *et al.*, Opt. Express **22**, 1277 (2014).
3. Y. Ding, C. Peucheret, H. Ou, and K. Yvind, Opt. Lett. **39**, 5348 (2014).
4. N. Hoppe, W. S. Zaoui, L. Rathgeber, *et al.*, IEEE J. Sel. Top. Quantum Electron. **26**, 1 (2019).
5. X. Liu, A. W. Bruch, and H. X. Tang, Adv. Opt. Photon. **15**, 236 (2023).
6. N. Li, C. P. Ho, S. Zhu, *et al.*, Nanophotonics **10**, 2347 (2021).
7. C. Xiong, W. H. Pernice, and H. X. Tang, Nano Lett. **12**, 3562 (2012).
8. S. Zhu and G.-Q. Lo, Opt. Express **24**, 12501 (2016).
9. M. Mirhosseini, A. Sipahigil, M. Kalaee, and O. Painter, Nature **588**, 599 (2020).
10. L. Fan, C.-L. Zou, R. Cheng, *et al.*, Sci. Adv. **4**, eaar4994 (2018).
11. F. Lecocq, F. Quinlan, K. Cicak, *et al.*, Nature **591**, 575 (2021).
12. W. Fu, M. Xu, X. Liu, *et al.*, Phys. Rev. A **103**, 053504 (2021).
13. J. Holzgrafe, N. Sinclair, D. Zhu, *et al.*, Optica **7**, 1714 (2020).
14. T. P. McKenna, J. D. Witmer, R. N. Patel, *et al.*, Optica **7**, 1737 (2020).
15. A. Rueda, F. Sedlmeir, M. C. Collodo, *et al.*, Optica **3**, 597 (2016).
16. X. Guo, C.-I. Zou, C. Schuck, *et al.*, Light Sci. Appl. **6**, e16249 (2017).
17. A. W. Bruch, X. Liu, X. Guo, *et al.*, Appl. Phys. Lett. **113** (2018).
18. S. Yao, K. Liu, and C. Yang, Opt. Express **29**, 8312 (2021).
19. K. Liu, S. Yao, and C. Yang, Opt. Lett. **46**, 993 (2021).
20. A. W. Bruch, X. Liu, Z. Gong, *et al.*, Nat. Photon. **15**, 21 (2021).
21. J. Liu, H. Weng, A. A. Afridi, *et al.*, Opt. Express **28**, 19270 (2020).
22. A. A. Afridi, H. Weng, J. Li, *et al.*, Opt. Continuum **1**, 42 (2022).
23. K. Liu, S. Yao, Y. Ding, *et al.*, Opt. Lett. **47**, 4295 (2022).
24. X. Liu, C. Sun, B. Xiong, *et al.*, Optica **4**, 893 (2017).
25. L. Fan, C.-L. Zou, M. Poot, *et al.*, Nat. Photon. **10**, 766 (2016).
26. T.-J. Lu, M. Fanto, H. Choi, *et al.*, Opt. Express **26**, 11147 (2018).
27. S. KP, S. Raghavan, and S. K. Selvaraja, "High-efficiency overlay grating fiber-chip couplers for aluminum nitride-on-sapphire waveguide platform," in *2022 Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR)*, (2022), pp. 1–2.
28. J. A. Smith, J. Monroy-Ruz, P. Jiang, *et al.*, Opt. Lett. **47**, 3868 (2022).
29. Z. Ruan, J. Hu, Y. Xue, *et al.*, Opt. Express **28**, 35615 (2020).
30. X. Liu, C. Sun, B. Xiong, *et al.*, Opt. express **25**, 587 (2017).
31. A. Youssefi, I. Shomroni, Y. J. Joshi, *et al.*, Nat. Electron. **4**, 326 (2021).
32. M. Shen, J. Xie, Y. Xu, *et al.*, Nat. Photon. **18**, 371 (2024).
33. Z. Zhao and S. Fan, J. Light. Technol. **38**, 4435 (2020).
34. E. Lomonte, F. Lenzini, and W. H. Pernice, Opt. Express **29**, 20205 (2021).
35. Y. Wang, Y. Guo, Y. Zhou, *et al.*, Opt. Express **32**, 20146 (2024).
36. X. Liu, C. Sun, B. Xiong, *et al.*, Vacuum **116**, 158 (2015).
37. J. Yeom, Y. Wu, J. C. Selby, and M. A. Shannon, J. Vac. Sci. Technol., B: Microelectron. Process. Phenom. **23**, 2319 (2005).
38. Y. Sun, W. Shin, D. A. Laleyan, *et al.*, Opt. Lett. **44**, 5679 (2019).
39. S. Martinussen, E. Berenschot, D. Bonneville, *et al.*, Opt. Express **32**, 36835 (2024).
40. J. Mishra, T. P. McKenna, E. Ng, *et al.*, Optica **8**, 921 (2021).

# FULL REFERENCES

1.  D. S. Zemtsov, D. M. Zhigunov, S. S. Kosolobov, *et al.*, "Broadband silicon grating couplers with high efficiency and a robust design," Opt. Lett. **47**, 3339–3342 (2022).

2.  W. S. Zaoui, A. Kunze, W. Vogel, *et al.*, "Bridging the gap between optical fibers and silicon photonic integrated circuits," Opt. Express **22**, 1277–1286 (2014).

3.  Y. Ding, C. Peucheret, H. Ou, and K. Yvind, "Fully etched apodized grating coupler on the SOI platform with -0.58 db coupling efficiency," Opt. Lett. **39**, 5348–5350 (2014).

4.  N. Hoppe, W. S. Zaoui, L. Rathgeber, *et al.*, "Ultra-efficient silicon-on- insulator grating couplers with backside metal mirrors," IEEE J. Sel. Top. Quantum Electron. **26**, 1–6 (2019).

5.  X. Liu, A. W. Bruch, and H. X. Tang, "Aluminum nitride photonic in- tegrated circuits: from piezo-optomechanics to nonlinear optics," Adv. Opt. Photon. **15**, 236–317 (2023).

6.  N. Li, C. P. Ho, S. Zhu, *et al.*, "Aluminium nitride integrated photonics: a review," Nanophotonics **10**, 2347–2387 (2021).

7.  C. Xiong, W. H. Pernice, and H. X. Tang, "Low-loss, silicon integrated, aluminum nitride photonic circuits and their use for electro-optic signal processing," Nano Lett. **12**, 3562–3568 (2012).

8.  S. Zhu and G.-Q. Lo, "Aluminum nitride electro-optic phase shifter for backend integration on silicon," Opt. Express **24**, 12501–12506 (2016).

9.  M. Mirhosseini, A. Sipahigil, M. Kalaee, and O. Painter, "Supercon- ducting qubit to optical photon transduction," Nature **588**, 599–603 (2020).

10. L. Fan, C.-L. Zou, R. Cheng, *et al.*, "Superconducting cavity electro- optics: a platform for coherent photon conversion between supercon- ducting and photonic circuits," Sci. Adv. **4**, eaar4994 (2018).

11. F. Lecocq, F. Quinlan, K. Cicak, *et al.*, "Control and readout of a superconducting qubit using a photonic link," Nature **591**, 575–579 (2021).

12. W. Fu, M. Xu, X. Liu, *et al.*, "Cavity electro-optic circuit for microwave- to-optical conversion in the quantum ground state," Phys. Rev. A **103**, 053504 (2021).

13. J. Holzgrafe, N. Sinclair, D. Zhu, *et al.*, "Cavity electro-optics in thin-film lithium niobate for efficient microwave-to-optical transduction," Optica **7**, 1714–1720 (2020).

14. T. P. McKenna, J. D. Witmer, R. N. Patel, *et al.*, "Cryogenic microwave-to-optical conversion using a triply resonant lithium-niobate- on-sapphire transducer," Optica **7**, 1737–1745 (2020).

15. A. Rueda, F. Sedlmeir, M. C. Collodo, *et al.*, "Efficient microwave to optical photon conversion: an electro-optical realization," Optica **3**, 597–604 (2016).

16. X. Guo, C.-I. Zou, C. Schuck, *et al.*, "Parametric down-conversion photon-pair source on a nanophotonic chip," Light Sci. Appl. **6**, e16249– e16249 (2017).

17. A. W. Bruch, X. Liu, X. Guo, *et al.*, "17 000%/W second-harmonic conversion efficiency in single-crystalline aluminum nitride microres- onators," Appl. Phys. Lett. **113** (2018).

18. S. Yao, K. Liu, and C. Yang, "Pure quartic solitons in dispersion- engineered aluminum nitride micro-cavities," Opt. Express **29**, 8312– 8322 (2021).

19. K. Liu, S. Yao, and C. Yang, "Raman pure quartic solitons in Kerr microresonators," Opt. Lett. **46**, 993–996 (2021).

20. A. W. Bruch, X. Liu, Z. Gong, *et al.*, "Pockels soliton microcomb," Nat. Photon. **15**, 21–27 (2021).

21. J. Liu, H. Weng, A. A. Afridi, *et al.*, "Photolithography allows high-Q AlN microresonators for near octave-spanning frequency comb and harmonic generation," Opt. Express **28**, 19270–19280 (2020).

22. A. A. Afridi, H. Weng, J. Li, *et al.*, "Breather solitons in AlN microres- onators," Opt. Continuum **1**, 42–50 (2022).

23. K. Liu, S. Yao, Y. Ding, *et al.*, "Fundamental linewidth of an aln micro- cavity raman laser," Opt. Lett. **47**, 4295–4298 (2022).

24. X. Liu, C. Sun, B. Xiong, *et al.*, "Integrated continuous-wave aluminum nitride raman laser," Optica **4**, 893–896 (2017).

25. L. Fan, C.-L. Zou, M. Poot, *et al.*, "Integrated optomechanical single- photon frequency shifter," Nat. Photon. **10**, 766–770 (2016).

26. T.-J. Lu, M. Fanto, H. Choi, *et al.*, "Aluminum nitride integrated pho- tonics platform for the ultraviolet to visible spectrum," Opt. Express **26**, 11147–11160 (2018).

27. S. KP, S. Raghavan, and S. K. Selvaraja, "High-efficiency overlay grating fiber-chip couplers for aluminum nitride-on-sapphire waveguide platform," in *2022 Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR)*, (2022), pp. 1–2.

28. J. A. Smith, J. Monroy-Ruz, P. Jiang, *et al.*, "Toward compact high- efficiency grating couplers for visible wavelength photonics," Opt. Lett. **47**, 3868–3871 (2022).

29. Z. Ruan, J. Hu, Y. Xue, *et al.*, "Metal based grating coupler on a thin-film lithium niobate waveguide," Opt. Express **28**, 35615–35621 (2020).

30. X. Liu, C. Sun, B. Xiong, *et al.*, "Aluminum nitride-on-sapphire plat- form for integrated high-q microresonators," Opt. express **25**, 587–594 (2017).

31. A. Youssefi, I. Shomroni, Y. J. Joshi, *et al.*, "A cryogenic electro-optic interconnect for superconducting devices," Nat. Electron. **4**, 326–332 (2021).

32. M. Shen, J. Xie, Y. Xu, *et al.*, "Photonic link from single-flux-quantum circuits to room temperature," Nat. Photon. **18**, 371–378 (2024).

33. Z. Zhao and S. Fan, "Design principles of apodized grating couplers," J. Light. Technol. **38**, 4435–4446 (2020).

34. E. Lomonte, F. Lenzini, and W. H. Pernice, "Efficient self-imaging grating couplers on a lithium-niobate-on-insulator platform at near- visible and telecom wavelengths," Opt. Express **29**, 20205–20216 (2021).

35. Y. Wang, Y. Guo, Y. Zhou, *et al.*, "Heterogeneous sapphire-supported low-loss photonic platform," Opt. Express **32**, 20146–20152 (2024).

36. X. Liu, C. Sun, B. Xiong, *et al.*, "Smooth etching of epitaxially grown AlN film by Cl2/BCl3/Ar-based inductively coupled plasma," Vacuum **116**, 158–162 (2015).

37. J. Yeom, Y. Wu, J. C. Selby, and M. A. Shannon, "Maximum achievable aspect ratio in deep reactive ion etching of silicon due to aspect ratio dependent transport and the microloading effect," J. Vac. Sci. Technol., B: Microelectron. Process. Phenom. **23**, 2319–2329 (2005).

38. Y. Sun, W. Shin, D. A. Laleyan, *et al.*, "Ultrahigh Q microring resonators using a single-crystal aluminum-nitride-on-sapphire platform," Opt. Lett. **44**, 5679–5682 (2019).

39. S. Martinussen, E. Berenschot, D. Bonneville, *et al.*, "Thick waveguides of low-stress stoichiometric silicon nitride on sapphire (sinos)," Opt. Express **32**, 36835–36847 (2024).

40. J. Mishra, T. P. McKenna, E. Ng, *et al.*, "Mid-infrared nonlinear optics in thin-film lithium niobate on sapphire," Optica **8**, 921–924 (2021).