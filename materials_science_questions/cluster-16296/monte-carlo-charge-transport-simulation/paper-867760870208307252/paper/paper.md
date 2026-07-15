# Structurally Tunable Nonlinear Terahertz Metamaterials using Broadside Coupled Split Ring Resonators

George R. Keiser¹, a), Nicholas Karl², S. Rubaiat Ul Haque³, Igal Brener², Daniel M. Mittleman⁴, and Richard D. Averitt³

¹Department of Physics, Washington College, Chestertown, MD, USA
²Center for Integrated Nanotechnologies, Sandia National Lab. Albuquerque, NM, USA
³Department of Physics, University of California at San Diego, La Jolla, CA, USA
⁴School of Engineering, Brown University, Providence, RI, USA

We present an experimental and numerical study of a terahertz metamaterial with a nonlinear response that is controllable via the relative structural positioning of two stacked split ring resonator arrays. The first array is fabricated on an n-doped GaAs substrate and the second array is fabricated vertically above the first using a polyimide spacer layer. Due to GaAs carrier dynamics, the on-resonance terahertz transmission at 0.4 THz varies in a nonlinear manner with incident terahertz power. The second resonator layer dampens this nonlinear response. In samples where the two layers are aligned, the resonance disappears and total nonlinear modulation of the on-resonance transmission decreases. The nonlinear modulation is restored in samples where an alignment offset is imposed between the two resonator arrays. Structurally tunable MMs can therefore act as a design template for tunable nonlinear THz devices by controlling the coupling of confined electric fields to nonlinear phenomena in a complex material substrate or inclusion.

Over the past decade the field of terahertz (THz) science has grown to include the study and engineering of nonlinear optical materials.¹,² This growth in nonlinear THz science has been driven by improvements in the ability to generate high power THz pulses in the laboratory. Standard THz generation via photo-conductive antennas or optical rectification (e.g. in ZnTe) produce THz pulses limited to femto Joules of energy.³ By contrast, the newer techniques of tilted pulse front THz generation (TPFG) in LiNbO₃ and 4-wave mixing in air generate pulse energies orders of magnitude higher.⁴,⁵ In particular, TPFG methods are known to reliably produce THz pulses with micro Joules of energy, corresponding to peak electric field strengths on the order of 300-500 kV/cm, and in some instances up to 1 MV/cm.⁶

The use of high peak power THz pulses makes time resolved nonlinear experiments possible at THz frequencies. Researchers are able to study the THz nonlinear properties of materials on ultrafast timescales

a) Author to whom correspondence should be addressed. gkeiser2@washcoll.edu

$^{7}$ and design novel nonlinear optical elements for THz radiation. $^{8,9}$ Combining THz excitation with X-ray probes allows for time-resolved measurements of nonlinear structural changes in complex materials.
10

Within the field of nonlinear THz science, plasmonic metamaterials and metasurfaces (MMs) play a critical role. MMs are engineered composites with optical properties that are determined by the geometry and layout of the component sub-wavelength inclusions.¹¹ MMs have been applied across the electromagnetic spectrum and may be used to precisely control light through manipulation of phase, intensity, and polarization. ¹². This unprecedented level of control over light has led to notable MM demonstrations of left-handed materials ¹³, electromagnetic cloaking ¹⁴, and perfect absorption¹⁵, ¹⁶. Additionally, MMs are interesting from a materials science standpoint due to their enhancement of light-matter interaction $^{2,7}$. This interaction can be seen in a magnified nonlinear MM response, making MMs an ideal platform to study THz nonlinear behavior and design nonlinear devices.

Nonlinear MM devices have been created at microwave and terahertz frequencies through a variety of methods including incorporating nonlinear lumped circuit elements into the design $^{17-19}$, and by using the inherent nonlinear response of the subwavelength inclusions that make up the MM²⁰. Another approach used in nonlinear MMs devices makes use of resonant inclusions, such as the split ring resonator (SRR), which confine electric fields to localized regions in the unit cell. Resonant field confinement (FC) enhances the local peak electric field intensity, and may excite a nonlinear response in the MM inclusions or substrate.⁷²¹ Many demonstrations of nonlinear MMs based on FC exist, including devices that couple confined fields to charge carrier dynamics in VO₂, GaAs, and InAs ²¹,²², and devices that couple fields to superconducting phase transitions in both low and high Tc superconductors. ²³⁻²⁵

Dynamic control over the MM response dramatically extends device capability; and integration of control and tuning is an active area of study for linear and nonlinear MM devices. Two of the most commonly used methods for electrical control of MM properties are via modulation of substrate conductivity $^{26}$ and structural design or actuation, for instance via microelectrical mechanical (MEMS) based devices $^{27,28}$. We recently have shown that the nonlinear response of a THz MM can be modulated through control of substrate conductivity$^9$. Yet to date there has been no report on how the nonlinear response of MMs responds to structural manipulation of the unit cell.

In this paper, we report an experimental study outlining how the nonlinear response of a THz MM can be controlled solely through manipulation of the structural design of the MM inclusions. Our MM design is based on the common broadside-coupled SRR (BCSRR) $^{29}$ and is shown schematically in figure 1a. This design is composed of two layered SRR arrays, oriented to maximize electromagnetic interactions between the two arrays. More details on device design are discussed below. We show that by altering the lateral positions of the two component split ring resonators in the unit cell, one can control the field confinement (FC) in the capacitive gaps of the resonators and thus control the coupling of incident THz fields to the nonlinear carrier dynamics of an n-doped GaAs substrate. When the two resonator layers are aligned to overlap as shown in figure 1b, very little nonlinear behavior is seen in the device response at the design frequency of 0.4 THz. When a lateral offset is placed between the upper and lower SRR array (shown in Figure 1c) the FC in the capacitive gap of the lower resonator increases, enabling a nonlinear response from the carrier dynamics of the n-doped epilayer at a relative low incident THz power. The nonlinear carrier dynamics result in a drop in the epilayer conductivity, turning onthe lowest order SRR resonance at 0.4 THz. The resonance is thus highly dependent on incident THz power and on resonance THz transmission is modulated by approximately 3dB as the incident THz power is increased. Below, we

present nonlinear THz spectroscopy measurements to characterize device response and numerical simulations to provide insight into the physical mechanisms for device behavior.

![](./images/867760870208307252_1.jpg)

FIG 1: (a) Vertically expanded perspective and side view of metamaterial unit cell showing dimensions and direction of THz excitation. (b) and (c) Mid-fabrication photos of two samples showing a different 0 μm (b) and 48 μm (c) lateral offset between the stacked resonator arrays. The lower layer of SRRs is shown in gold, while the upper layer is shown as outlines.

The MM studied in this work consists of two stacked, planar arrays of gold SRRs as shown in Figure 1.

The lower array is fabricated directly onto a GaAs substrate with a 1 $\mu$m thick n-doped GaAs epilayer (n

$= 2\mathrm{x}10^{16}\ \mathrm{cm}^{-3}$) using standard photolithographic techniques. The SRRs of this layer are inter-connected with metallic wires for use in applying an electrical bias (not used in this study). A $2\ \mu\mathrm{m}$ thick polyimide spacer layer is then deposited on the epilayer followed by a second SRR array. The orientation of the second array is rotated by $180^\circ$ relative to the first array, which maximizes electromagnetic coupling between the two layers.$^{29}$

The dimensions of the component SRRs are chosen to maximize coupling between the two resonator layers and to place the device resonance near the peak of the TPFG THz signal at ~0.4 THz. The key dimensions of each resonator are marked on the upper SRR in figure 1a. These are the side length, L, the capacitive gap width, g, the linewidth, w, and the square array periodicity, P. Below, the dimensions for the lower SRR array are written with a subscript 1, while dimensions for the upper array are written with a subscript 2. In the lower array, $\mathrm{L_1} = 28\ \mu\mathrm{m}$, linewidth $\mathrm{w_1} = 6\ \mu\mathrm{m}$, and $\mathrm{g_1} = 2\ \mu\mathrm{m}$. In the upper array, $\mathrm{L_2} = 48\ \mu\mathrm{m}$, $\mathrm{w_2=}6\ \mu\mathrm{m}$, and $\mathrm{g_2} = 2\ \mu\mathrm{m}$. The unit cell periodicity is the same for both arrays and is $\mathrm{P=}96\ \mu\mathrm{m}$. Two samples are fabricated each with a varying lateral shift, $\mathrm{L_{shift}}$, between the centers of the two SRRs, as shown in the side view of figure 1a. Photographs of the two fabricated samples are shown in figure 1b and 1c. In sample 1 (figure 1b), the two SRR arrays are directly aligned with $\mathrm{L_{shift}} = 0\ \mu\mathrm{m}$. In sample 2 (figure 1c), the two arrays are laterally offset by half of the unit cell periodicity ($\mathrm{L_{shift}} = 48\ \mu\mathrm{m}$).

To characterize the nonlinear response of the two samples, THz pulses with field strengths between 50 and 400 kV/cm were generated using TPFG in $\mathrm{LiNO_3}$ and focused onto the MM at normal incidence with the THz electric field polarized perpendicular to the SRR capacitive gaps, as shown in figure 1a. The transmitted pulses are then measured using electro-optic sampling in ZnTe in a standard THz time-domain spectroscopy (THz-TDS) configuration. The transmission spectra are obtained through Fourier transform and normalized to a THz-TDS reference measurement of a bare GaAs substrate with a $1\ \mu\mathrm{m}$ n-doped epilayer.

![](./images/867760870208307252_2.jpg)

FIG 2: THz-TDS data for samples with (a) $L_{shift} =0\ \mu$m and (b) $L_{shift}=48\ \mu$m. Insets show photographs of the relative positioning for the two SRR layers for the data shown in the plot. On each plot, the dashed vertical lines mark the position of the resonance of the broadside coupled SRR system.

Experimental transmission spectra as a function of field strength for both samples are shown in figure 2.

For the sample with $L_{shift}=0\ \mu$m (fig. 2a) only a small nonlinear response can be seen in the data. As the THz field strength is increased from 50 - 400 kV/cm, the overall transmission through the sample slightly increases, but no clear resonance is seen, regardless of incident field strength. Figure 2b shows noticeably different behavior exhibited by the structure in which the SRRs are offset. The MM now exhibits a strong resonance near approximately 0.4 THz with a larger nonlinear modulation. As the THz field strength is increased from 50 - 400 kV/cm, the on-resonance transmission is modulated by approximately 3dB.

Thus, the presence of a strong nonlinear modulation in the MM resonance can be controlled solely by structural positioning of the two MM layers. As another comparison of the stark difference in modulation range, figure 3 plots the transmission at 0.4THz for both samples as a function of incident THz field

strength. Not only is the modulation range noticeably increased in the case for $\mathrm{L_{shift}} = 48\ \mathrm{\mu m}$, the direction of modulation is also reversed compared to the unshifted structure.

![](./images/867760870208307252_3.jpg)

FIG 3: Modulation of the transmission minimum at 0.4THz vs. applied THz field strength for both shifted and unshifted BC-
SRR samples. Cross markers on lines signify measured data points.

Using numerical simulations, we investigate the physical origins of the nonlinear response of the BC-SRR
MM discussed above. In order to show the mode structure of the MM, we simulate the THz transmission
spectra of the BC-SRR structure for $\mathrm{L_{shift}} = 0$ and $48\ \mathrm{\mu m}$ using commercial solvers based on finite
difference time domain techniques. $^{30}$ The SRR gold patterning is modeled as a lossy metal, while the
GaAs substrate is modeled with a $1\ \mathrm{\mu m}$ lossy semiconductor epilayer on a loss-free semi-insulating GaAs
substrate. These simulated spectra are shown together in Figure 4a. Due to the limited frequency resolution
in the tilted pulse front THz-TDS system, the resonances in simulation are narrower than in the
experimental results.

The blue curve in figure 4a shows the spectra for the sample with Lₛₕᵢբₜ = 0 μm. The incident THz electric field polarized perpendicular to the capacitive gap of the SRRs excites two modes. The resonance at 0.73THz (resonance A) corresponds to the electrically active coupled mode of the BC-SRR. ³¹ The frequency position and oscillator strength of mode A has been shown in previous work to be highly dependent on the electromagnetic coupling between the two component SRRs. The frequency position of mode A can be approximately described using an LC oscillator model:

$$
f_{A} \sim \frac{1}{2 \pi}\left(\frac{1}{\sqrt{L C}}\right) \tag{1}
$$

where L is the BC-SRR total inductance, and C the BC-SRR total capacitance. ³²,³³.

The red curve in figure 4a shows the transmission spectrum for the sample with Lₛₕᵢբₜ = 48 μm. The lateral offset of the two SRRs alters the mutual capacitance and inductance of the structure, red-shifting resonance A from 0.73 THz to 0.47 THz. The mode at 0.66 THz (resonance B) is a surface lattice mode, common in periodic MM structures ³⁴. The frequency position of mode B is largely independent of the mutual interactions between the two SRRs, as expected for a surface lattice resonance.

Figures 4b and 4c show simulations of the nonlinear response of the Lₛₕᵢբₜ = 0 μm and Lₛₕᵢբₜ = 48 μm samples, respectively. Here, the GaAs response is modeled using Drude model with a carrier mobility that can vary between 100 cm²/Vs and 1000 cm²/Vs. The nonlinear response arises from terahertz field induced intervalley scattering of charge carriers in the 1 μm n-GaAs epilayer. The resulting decrease in mobility reduces the conductivity of the epilayer, resulting in a terahertz field dependent increase in resonance depth for resonances A and B for both Lₛₕᵢբₜ = 0 μm and Lₛₕᵢբₜ = 48 μm.

![](./images/867760870208307252_4.jpg)

FIG 4: (a) Simulated transmission spectra for the $L_{\text{shift}} = 0$ µm and 48 µm samples assuming no loss in the GaAs substrate. Letters A and B denote resonances discussed in the main text. (b) Simulated nonlinear response for $L_{\text{shift}} = 0$ µm (c) Simulated nonlinear response for $L_{\text{shift}} = 48$ µm.

In experiment, the overall loss in the n-doped epilayer broadens all resonances. The resolution limit of the THz-TDS system also artificially broadens the observed resonances. For $L_{\text{shift}} = 0$ µm, neither resonance is seen in experiment (fig. 2a) for any value of incident THz field strength, due to the above-mentioned broadening effects. However, the net decrease in carrier mobility is still seen in the data as a broadband increase in transmission.

For $L_{\text{shift}} = 48$ µm (fig 2b), resonance A is clearly visible in the experimental results since the overall oscillator strength, and thus resonance depth, of resonance A is now much greater. Here, the decrease in

carrier mobility decreases the on-resonance loss of the BC-SRR structure, leading to a stronger resonance and explaining the difference in modulation direction discussed above in figure 3.

The lateral positioning of the two SRR layers allows for tuning of the oscillator strength by controlling the local FC within the MM unit cell. For mode A, the FC within the capacitive gap region is directly proportional to the oscillator strength of mode A. In addition to the LC resonance model, mode A can be thought of as a resonance of a folded half-wave dipole antenna, where the length, d, of the dipole is the circumference of the SRR. As such, the current distribution in the a BC-SRR resonator can be approximately modeled as a cosine distribution:

$$
j = j_o \cos\left(\frac{\pi s}{d}\right) e^{-i\omega t} \tag{2}
$$

where $j_o$ is the peak current density on resonance, s is the position along the SRR circumference, and $\omega$ is the frequency of incident THz excitation. The current in the upper SRR, oscillates out of phase with the current in the lower SRR. This results in a charge buildup along the gaps of both SRRs, $90^\circ$ out of phase with the resonant current. Specifically, the charge is:

$$
Q = Q_o \sin\left(\frac{\pi s}{L}\right) e^{-i\omega t} \tag{3}
$$

where $Q_o$ is the peak charge across the SRR capacitive gap. With no lateral offset, the out of phase electric fields from the two resonators superimpose and distructively interfere, leading to a low net electric field strength in the unit cell of the MM. As the two resonators are laterally offset, the resonant electric fields of the two SRRs no longer superimpose spatially, leading to less destructive interference and a higher net electric field strength inside the MM unit cell. The end result is an increase in the strength of the local

electric fields in the lower SRR gap region. This results in a stronger resonance for the sample with $L_{\text{shift}}$ = 48 μm and a larger nonlinear modulation of the resonance as the incident THz field strength is increased.

We can confirm this explanation of tunable local FC by performing simulations of the local electric field distributions within the MM unit cell. Figure 5 shows the time domain electric field strength maximum in the plane of the lower SRR for the $L_{\text{shift}} = 0$ μm (fig. 5a) and $L_{\text{shift}} = 48$ μm (fig. 5b) samples. The local electric fields are higher by close to a factor of 4 in the $L_{\text{shift}} = 48$ μm sample. As the local electric field amplification increases, especially in the vicinity of the SRR capacitive gap, so will the overall oscillator strength and resonance depth of the BC-SRR resonance.

![](./images/867760870208307252_5.jpg)

FIG 5: Local electric field distribution in lower SRR during THz excitation for (a)Lshift = 0 μm (b)Lshift =48 μm. White dashed square outlines position of upper SRR layer.

Figure 6a and 6b show simulations of the increase in resonance depth, and thus oscillator strength, of resonance A, for varying values of $L_{\text{shift}}$. As $L_{\text{shift}}$ is increased from 0 to 48 μm, the depth of resonance A increases by 80%, corresponding to an 80% increase to oscillator strength. Consequentially, resonance A and its nonlinear behavior is visible in the experimental spectra for $L_{\text{shift}} = 48$ μm, but not for $L_{\text{shift}} = 0$ μm.

![](./images/867760870208307252_6.jpg)

FIG 6: (a) Simulated transmission spectra for BC-SRR samples with varying values of $L_{\text{shift}}$. (b) Change in the on-resonance transmission minimum vs. $L_{\text{shift}}$. Crosses mark measured data points.

In conclusion, we presented a proof-of-principle study showing how a nonlinear metamaterial response can be tuned in magnitude via the relative lateral positioning of the stacked resonator arrays inside a broadside coupled split ring resonator metamaterial. The metamaterial was patterned on an n-doped GaAs substrate. We investigated the behavior of the metamaterial experimentally via terahertz time domain spectroscopy and use numerical simulations to provide physical insight into the device response. In samples where the two resonator arrays were aligned, the device showed only a small nonlinear response in experiment. In samples where the component split ring resonator arrays were laterally shifted by 48 $\mu$m, a resonance appeared at $\sim$ 0.41 THz. Due to the charge carrier dynamics of the n-doped GaAs and on-resonance field confinement in the SRR capacitive gaps, the on-resonance THz transmission was strongly nonlinear, decreasing by approximately 3 dB as the incident terahertz power increases from 50 to 400 kV/cm. This result is, to the best of our knowledge, the first example illustrating the control of the nonlinear response of a THz MM device solely through the structural positioning of the component inclusions.

### Acknowledgements

This work was supported by the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering and performed, in part, at the Center for Integrated Nanotechnologies, an Office of Science User Facility operated for the U.S. Department of Energy (DOE) Office of Science. Sandia National Laboratories is a multi-mission laboratory managed and operated by National Technology and Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honeywell International, Inc., for the U.S. Department of Energy's National Nuclear Security Administration under contract DE-NA0003525. Work at UCSD was supported by the DARPA DRINQS program (Grant No. D18AC00014). G.R.K. thanks the Washington College Faculty Enhancement Program for travel and equipment funding throughout the duration of this project.

This paper describes objective technical results and analysis. Any subjective views or opinions that might be expressed in the paper do not necessarily represent the views of the U.S. Department of Energy or the United States Government.

### Data Availability

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# References

1.  F. Blanchard, L. Razzari, F. H. Su, G. Sharma, R. Morandotti, T. Ozaki, M. Reid and F. A. Hegmann, in *Nonlinear Photonics and Novel Optical Phenomena*, edited by Z. Chen and R. Morandotti (Springer New York, 2012), Vol. 170, pp. 297-323.
2.  G. R. Keiser and P. Klarskov, Photonics **6** (1), 22 (2019).
3.  D. M. Mittleman, Journal of Applied Physics **122** (23), 230901 (2017).
4.  J. A. Fülöp, L. Pálfalvi, S. Klingebiel, G. Almási, F. Krausz, S. Karsch and J. Hebling, Optics Letters **37** (4), 557-559 (2012).
5.  D. J. Cook and R. M. Hochstrasser, Optics Letters **25** (16), 1210-1212 (2000).
6.  H. Hirori, A. Doi, F. Blanchard and K. Tanaka, Applied Physics Letters **98** (9), 091106 (2011).
7.  M. Liu, H. Y. Hwang, H. Tao, A. C. Strikwerda, K. Fan, G. R. Keiser, A. J. Sternbach, K. G. West, S. Kittiwatanakul, J. Lu, S. A. Wolf, F. G. Omenetto, X. Zhang, K. A. Nelson and R. D. Averitt, Nature **487** (7407), 345-348 (2012).
8.  G. R. Keiser, J. Zhang, X. Zhao, X. Zhang and R. D. Averitt, J. Opt. Soc. Am. B **33** (12), 2649-2655 (2016).
9.  G. R. Keiser, N. Karl, P. Q. Liu, C. Tulloss, H.-T. Chen, A. J. Taylor, I. Brener, J. L. Reno and D. M. Mittleman, Applied Physics Letters **111** (12), 121101 (2017).
10. A. X. Gray, M. C. Hoffmann, J. Jeong, N. P. Aetukuri, D. Zhu, H. Y. Hwang, N. C. Brandt, H. Wen, A. J. Sternbach, S. Bonetti, A. H. Reid, R. Kukreja, C. Graves, T. Wang, P. Granitzka, Z. Chen, D. J. Higley, T. Chase, E. Jal, E. Abreu, M. K. Liu, T. C. Weng, D. Sokaras, D. Nordlund, M. Chollet, R. Alonso-Mori, H. Lemke, J. M. Glownia, M. Trigo, Y. Zhu, H. Ohldag, J. W. Freeland, M. G. Samant, J. Berakdar, R. D. Averitt, K. A. Nelson, S. S. P. Parkin and H. A. Dürr, Physical Review B **98** (4), 045104 (2018).
11. J. B. Pendry, A. J. Holden, D. J. Robbins and W. J. Stewart, Microwave Theory and Techniques, IEEE Transactions on **47** (11), 2075-2084 (1999).
12. J. Y. Ou, E. Plum, L. Jiang and N. I. Zheludev, Nano Letters **11** (5), 2142-2144 (2011).
13. R. A. Shelby, D. R. Smith and S. Schultz, Science **292** (5514), 77-79 (2001).
14. D. Schurig, J. J. Mock, B. J. Justice, S. A. Cummer, J. B. Pendry, A. F. Starr and D. R. Smith, Science **314** (5801), 977-980 (2006).
15. N. I. Landy, S. Sajuyigbe, J. J. Mock, D. R. Smith and W. J. Padilla, Physical Review Letters **100** (20), 207402 (2008).
16. H. Tao, C. M. Bingham, A. C. Strikwerda, D. Pilon, D. Shrekenhamer, N. I. Landy, K. Fan, X. Zhang, W. J. Padilla and R. D. Averitt, Physical Review B **78** (24), 241103 (2008).
17. A. Rose, D. A. Powell, I. V. Shadrivov, D. R. Smith and Y. S. Kivshar, Physical Review B **88** (19), 195148 (2013).
18. A. Rose, D. Huang and D. R. Smith, Physical Review Letters **107** (6), 063902 (2011).
19. I. Gil, J. Garcia-Garcia, J. Bonache, F. Martin, M. Sorolla and R. Marques, Electronics Letters **40** (21), 1347-1348 (2004).
20. B. Wang, J. Zhou, T. Koschny and C. M. Soukoulis, Opt. Express **16** (20), 16058-16063 (2008).
21. J. Zhang, X. Zhao, K. Fan, X. Wang, G.-F. Zhang, K. Geng, X. Zhang and R. D. Averitt, Applied Physics Letters **107** (23), 231101 (2015).
22. H. R. Seren, J. Zhang, G. R. Keiser, S. J. Maddox, X. Zhao, K. Fan, S. R. Bank, X. Zhang and R. D. Averitt, Light Sci Appl. **5**, e16078 (2016).
23. D. Zhang, M. Trepanier, O. Mukhanov and S. M. Anlage, Physical Review X **5** (4), 041045 (2015).
24. C. Zhang, B. Jin, J. Han, I. Kawayama, H. Murakami, X. Jia, L. Liang, L. Kang, J. Chen, P. Wu and M. Tonouchi, New Journal of Physics **15** (5), 055017 (2013).
25. K. G. Nathaniel, G. P. Bradford, Jr., Y. H. Harold, C. B. Nathaniel, T. Darius, S. Ranjan, Y. Li, T. Daniel, A. T. Stuart, Q. X. Jia, J. T. Antoinette, A. N. Keith and C. Hou-Tong, New Journal of Physics **15** (10), 105016 (2013).
26. W. L. Chan, H.-T. Chen, A. J. Taylor, I. Brener, M. J. Cich and D. M. Mittleman, Applied Physics Letters **94** (21), 213511 (2009).
27. Y. H. Fu, A. Q. Liu, W. M. Zhu, X. M. Zhang, D. P. Tsai, J. B. Zhang, T. Mei, J. F. Tao, H. C. Guo, X. H. Zhang, J. H. Teng, N. I. Zheludev, G. Q. Lo and D. L. Kwong, Advanced Functional Materials **21** (18), 3589-3594 (2011).
28. X. Zhao, J. Zhang, K. Fan, G. Duan, J. Schalch, G. R. Keiser, R. D. Averitt and X. Zhang, Physical Review B **99** (24), 245111 (2019).
29. R. Marques, F. Mesa, J. Martel and F. Medina, Antennas and Propagation, IEEE Transactions on **51** (10), 2572-2581 (2003).
30. K. S. Kunz and R. J. Luebbers, *The finite difference time domain method for electromagnetics*. (CRC press, 1993).
31. H. Haus and W. P. Huang, Proceedings of the IEEE **79** (10), 1505-1518 (1991).
32. E. Ekmekci, A. C. Strikwerda, K. Fan, G. Keiser, X. Zhang, G. Turhan-Sayan and R. D. Averitt, Physical Review B **83** (19), 193103 (2011).
33. D. A. Powell, M. Lapine, M. V. Gorkunov, I. V. Shadrivov and Y. S. Kivshar, Physical Review B **82** (15), 155128 (2010).
34. T. C. Tan, E. Plum and R. Singh, Photonics **6** (3), 75 (2019).