# Experimental demonstration of second-harmonic generation in high $\chi^{2}$ metasurfaces

LÉNA SOUN, $^{1}$ BAPTISTE FIX, $^{1}$ HASNAA EL QUAZZANI, $^{1}$ SÉBASTIEN HÉRON, $^{1}$ 
NATHALIE BARDOU, $^{2}$ CHRISTOPHE DUPUIS, $^{2}$ SOPHIE DERELLE, $^{1}$ JULIEN JAECK, $^{1}$ 
RIAD HAÏDAR, $^{1,3}$ AND PATRICK BOUCHON $^{1, *}$ 

$^{1}$ ONERA, Université Paris-Saclay, F-91123 Palaiseau, France
$^{2} C 2 N$, CNRS, Université Paris-Saclay, Avenue de la Vauve, Palaiseau, France
$^{3}$ École Polytechnique, Départementement de Physique, 91128 Palaiseau, France
*Corresponding author: patrick.bouchon@onera.fr

Received 17 November 2020; revised 22 January 2021; accepted 18 February 2021; posted 19 February 2021 (Doc. ID 415257); published 15 March 2021

Metasurfaces able to concentrate light at various wavelengths are promising for enhancing nonlinear interactions. In this Letter, we experimentally demonstrate infrared second-harmonic generation (SHG) by a multi-resonant nanostructure. A 100 GaAs layer embedded in a metal-insulator-metal waveguide is shown to support various localized resonances. One resonance enhances the nonlinear polarization due to the transverse magnetic (TM)-polarized pump wavelength near $3.2\ \mu$m, while another is set near the TE-polarized generated wavelength $(1.6\ \mu$m). The measured SHG efficiency is higher than $10^{-9}\ \text{W}^{-1}$ for pump wavelengths ranging from $2.9$ to $3.3\ \mu$m, which agrees with theoretical computations. This is typically 4 orders of magnitude higher than the equivalent GaAs membrane.
©2021 Optical Society of America

https://doi.org/10.1364/OL.415257

Metasurfaces can concentrate light in subwavelength volume, exalting the electric field by several orders of magnitude [1,2]. This is particularly interesting for nonlinear optics, which depends on the powers of the pump field. Therefore, nonlinear metasurfaces have been widely studied these past years [3–7]. Actually, frequency conversion effects such as second-harmonic generation (SHG) permit the creation of new wavelengths, which can be used for spectroscopy. Different approaches have been investigated, such as enhancing the nonlinearities of metals [8–10], harnessing Mie resonances in nanostructured dielectric [11], or using photonic crystals [12]. Some dielectrics possess high $\chi^{(2)}$, making them more suitable for nonlinear effects than metals. For instance, Gallium arsenide (GaAs) has a nonlinear susceptibility of $\chi^{(2)} \simeq 150\ \text{pm/V}$ in the infrared [13]. It has been previously nanopatterned in order to enhance the SHG, for example, the nanowires of Carletti *et al.* [14] or the gratings of De Ceglia *et al.* [15]. These demonstrations have been done in the visible with typical efficiencies $\frac{P_{\text{SHG}}}{P_{\text{inc}}^{2}} \simeq 10^{-11}\ \text{W}^{-1}$. GaAs can also be included in metallic nanostructures, for creating cavities or exploiting surface plasmons. In this way, SHG has been demonstrated with devices composed of GaAs included in subwavelength metallic hole [16], or slit [17,18], or associated with metallic split-ring resonators [19]. But in these geometries, there is only a small volume of GaAs included in the metallic antenna that contributes to the generated signal, which hinders the efficiency of such systems. To improve the efficiency of nonlinear resonant nanostructures, several challenges have to be considered simultaneously. First, the enhancement and overlapping of the linear fields at the pump wavelengths have to be optimized on the largest volume possible. Then, the generated signal must be extracted.

In this Letter, we experimentally demonstrate SHG in 100 GaAs embedded in a metal-insulator-metal (MIM) configuration with mid-infrared pump wavelength. This MIM resonator supports various kind of resonances in each polarization, from which we take advantage so as to increase the SHG efficiency by having field enhancement in the GaAs layer at both the pump and the generated wavelengths. SHG is measured thanks to an optical parametric oscillator (OPO), whose mid-infrared idler is used as pump wavelength, and an InGaAs camera. We demonstrate resonant SHG with efficiency higher than $10^{-9}\ \text{W}^{-1}$ for pump wavelengths ranging from $2.9$ to $3.3\ \mu$m, which is typically 4 orders of magnitude higher than the equivalent GaAs membrane.

The structure studied here is a waveguide resonator, which is depicted on the top of Fig. 1(a). The waveguide structure is composed of a layer of gallium arsenide (thickness $h$) encapsulated between a continuous gold layer, which is thick enough to be optically opaque and is considered as a semi-infinite layer, and a gold grating (period $d$, thickness $t$, and width of the gold ribbons $w$). The model of gold used here is a Drude model in agreement with experimental data in the infrared range: $\epsilon_{Au}(\lambda) = 1 - 1/(\lambda_{p}/\lambda(\lambda_{p}/\lambda + i\gamma))$ with $\lambda_{p} = 159\ \text{nm}$ and $\gamma = 0.0075$ [20]. The gallium arsenide layer has a second-order nonlinear susceptibility $\chi_{xyz}^{(2)}$, only these $xyz$ coefficients are nonzero due to its crystal symmetries (zinc blende type, $\overline{4}3m$ class). The nonlinear properties of gold are not considered in the following, as the nonlinear susceptibility of gold is far smaller than for gallium arsenide [21]. The structure has been optimized for SHG, with a transverse magnetic (TM)-polarized

![](./images/812499380014678018_1.jpg)

Fig. 1. (a) Scheme of the structure made of a stack of a gold mirror, a GaAs layer of thickness $h = 152$ nm, and a top grating of gold ribbons of width $w = 235$ nm, thickness $t = 60$ nm, and period $d = 544$ nm. The incoming wave at $\omega$ is TM-polarized and focused with a $15^\circ$ half-angle. (b) Scanning electron microscope image of the grating. (c) Computed SHG efficiency as a function of the pump wavelength for the waveguide resonator (green curve) and for a GaAs membrane of same thickness $h$ with and without a back gold mirror (orange and blue curves).

pump near $3.2\ \mu$m and a transverse electric (TE)-polarized signal near $1.6\ \mu$m.

The simulations have been realized thanks to a B-spline modal method (BMM) [22,23]. The SHG efficiency is calculated as follows:

$$
\Pi = \frac{P_{\text{SHG}}}{P_{\text{inc}}^2}\ \text{W}^{-1}, \tag{1}
$$

where $P_{\text{SHG}}$ is the signal power and $P_{\text{inc}}$ is the incident power. Figure 1(c) shows the simulated efficiency spectra as a function of the pump wavelength for the metasurface (green curve) and two references, one without the top grating layer (orange curve), and the other with only the GaAs layer (blue curve). The thickness $h$ of the GaAs layer is the same in the three cases. The first reference is far more efficient than the second, thanks to the mirror that creates a cavity. Moreover, the waveguide resonator is even more efficient with a peak of efficiency at $0.8 \times 10^{-8}\ \text{W}^{-1}$. Even if the references are optimized in order to have their peak of efficiency around $3.2\ \mu$m, their efficiencies remain smaller.

The metasurface was fabricated following the process detailed hereafter. First, an epitaxial layer of 152 nm GaAs layer with an AlAs barrier layer of 30 nm was grown on a (100) GaAs substrate. Then, a Ti/Au/Ti/Al stack with thicknesses 5/200/20/200 nm was deposited. After an anodic bonding to a Pyrex substrate, the GaAs substrate was removed by a mechanical polishing and then a chemical etching with a Piranha etching solution $(2\text{H}_2\text{SO}_4 + \text{H}_2\text{O}_2)$. The optical reflectivity of the GaAs layer on gold was characterized with a Fourier transform infrared (FTIR) spectrometer. In order to have a good agreement with theoretical computations, a 10 nm aluminum oxide layer has to be included on top of the GaAs layer, whose thickness is reduced to 142 nm. Then, an electron beam lithography was performed with a subsequent lift-off of 40 nm of gold with 2 nm of titanium serving as an adhesion layer. A scanning electron microscope image of the grating is shown in Fig. 1(b).

In the following, the linear and nonlinear properties of the grating (period $d = 544$ nm and width $w = 235$ nm) are experimentally investigated. The reflectivity spectra for both polarizations are obtained thanks to a microscope Bruker Hyperion 2000 coupled to a FTIR spectrometer Bruker vertex 70. The polarized light is focused on the grating with a Cassegrain objective ($\text{NA} = 0.4$) with a central occultation such that in practice only angles of incidence from $12^\circ$ to $24^\circ$ are incoming on the sample. The measured reflectivity spectra are plotted in Fig. 2 for the TM polarization (red dotted curve) and the TE polarization (green dotted curve). There is a nearly total absorption resonance in TE polarization at $\lambda = 1.6\ \mu$m, which is attributed to a vertical Fabry–Perot resonance [24]. In TM polarization, there are two resonances, respectively, at $\lambda = 1.75\ \mu$m, due to a guided modes resonance [25], and at $\lambda = 2.85\ \mu$m, which is due to a horizontal Fabry–Perot resonance in the MIM cavity [26]. The computed reflectivity spectra have also been computed for the incoming focused beam for both polarizations, and they are in good agreement with measurements.

The SHG from $3.2\ \mu$m to $1.6\ \mu$m benefits from both the broad TM resonance close to $\lambda = 2.85\ \mu$m (pump wavelength) and the narrower TE resonance at $\lambda = 1.6\ \mu$m (signal).

The TM resonance at the pump wavelength is a Fabry–Perot resonance in a horizontal cavity below the gold ribbons, created by surface plasmons propagating at the metal/dielectric

![](./images/812499380014678018_2.jpg)

Fig. 2. Study of the efficiency of the resonator in the linear regime. Reflectivity spectra of the waveguide resonator in TM polarization (red curve) and in TE polarization (green curve). The parameters of the grating are $d = 544$ nm, $w = 235$ nm, $t = 40$ nm, $h = 152$ nm. In the insets, map of the normalized nonlinear polarization $\mathcal{P}_{\text{norm}}^{(2)}$ generated at $\lambda_{\text{TM}} = 2.85\ \mu$m in one period, and map of the normalized electric field intensity at $\lambda = 1.6\ \mu$m in TE polarization. In both cases, gold is represented in gray.

interfaces. The resonance wavelength depends on the size the cavity, here the width of the gold ribbons. This broad resonance permits the exaltation of the pump fields—$\mathcal{E}_x$ and $\mathcal{E}_z$—used for the generation of the nonlinear polarization. Besides, this resonance offers a good angular tolerance, convenient for the experiment. The red inset in Fig. 2 represents an $xz$ map of the normalized nonlinear polarization produced in one period. This polarization is generated along the $y$ direction thanks to the multiplication of the pump fields along $x$ and $z$ directions:

$$
\mathcal{P}_{y_{\text{norm}}}^{(2)}=\left|\frac{\mathcal{E}_{x 1} \mathcal{E}_{z 1}}{\mathcal{E}_{\text {inc }}^{2}}\right|. \tag{2}
$$

The TE resonance at the signal wavelength is also a Fabry–Perot resonance, but with a vertical cavity in the GaAs layer. Here the resonance wavelength depends on the thickness of the GaAs layer. The green inset in Fig. 2 represents the linear field $\mathcal{E}_y$ at the signal wavelength. Actually, at the generated wavelength, the most important feature in order to reach the highest nonlinear efficiency possible is a good extraction ratio. The latter is closely linked to the resonance inside the nonlinear layer and, thus, to the reflectivity ratio (see Supplement 1). The more resonant the structure will be, the more it will be able to absorb an important fraction for a monochromatic excitation, and in parallel to extract a signal that would be generated within the structure. On the other hand, the quality factor of the resonance will provide information on the level of losses suffered by the generated wave, as well as on the tolerance to manufacturing errors.

Once the resonance behavior has been verified, the sample has been characterized on a nonlinear setup depicted in Fig. 3. The pump is generated by an OPO with a pulse frequency of 20 kHz and a pulse duration of 1.5 ns. The complementary (idler) of the OPO is used, which generates at wavelengths between 2 and 4.1 μm, with an average power of 10 mW, giving a peak power of about 300W. The setup is composed of two perpendicular arms: one of injection of the incident beam at 3.2 μm at normal incidence and one of collection of the signal generated at 1.6 μm in the same direction, on a photodetector. The two arms meet on a dichroic mirror that differentiates the two wavelengths at stake: it is transparent for the pump wavelength and reflective for the signal wavelength. An untreated germanium window is used for this, which transmits 90% above 2 μm. This window also blocks any signal residue from the OPO. The incident beam is focused on the sample with $\text{CaF}_2$ lens with 4 cm focal length (incident angles on the sample between $-15^\circ$ and $15^\circ$). The power density on the sample is around $50\ \text{MW/cm}^2$. The fabricated sample contains several gratings with different $w$ and $d$ parameters. It is on a support with micrometric translation plates in $xyz$. To visualize the gratings, we use a FLIR SC7000 camera (InSb, sensitive between 1.5 and 5.4 μm), which allows us to distinguish the grating as well as the spot of the focused pump (as depicted in Fig. 3). The signal is detected by a camera Xenics Xeva 1.7-320 (InGaAs), which has been calibrated thanks to a monochromator that injects light into an integrating sphere and is subsequently acquired by the Xenics camera (see Supplement 1). The signal power is calculated by integration on the signal spot on the camera. Then it is normalized by the incident power squared to find an efficiency respecting Eq. (1). It has been verified that this signal is indeed a second-harmonic (SH) signal. First, it is maximized for a TM-polarized pump and extinguished for a TE-polarized pump. Besides, the emitted signal is, as predicted, TE-polarized, and the output power has a quadratic dependence on the pump power. Finally, when the pump wavelength is set at $\lambda=3.2\ \mu\text{m}$, a filter centered at $\lambda=1.6\ \mu\text{m}$ was placed on the signal path that confirms the SH generation at this wavelength.

![](./images/812499380014678018_3.jpg)

Fig. 3. Experimental setup for second-harmonic generation: the TE-polarized pump beam (near 3.2 μm) is generated by a nanosecond OPO idler, and its polarization is rotated to TM thanks to a half-wave blade. It passes through the germanium window and is focused on the sample through a $\text{CaF}_2$ lens (focal length of 4 cm). The second-harmonic signal (near 1.6 μm), materialized in blue, is reflected by the germanium window and is detected on an InGaAs Xenics camera. The FLIR SC7000 infrared camera allows us to visualize the pump spot focused on the sample grating, as illustrated on the schematic.

Figure 4 shows the measurement of the reflected SHG spectrum (red dots with errorbars) as a function of the pump wavelength. The resonant SHG efficiency is higher than $10^{-9}\ \text{W}^{-1}$ for pump wavelengths ranging from 2.9 to 3.3 μm, and a peak efficiency of $8\times 10^{-9}\ \text{W}^{-1}$ is obtained for a pump wavelength of 3.17 μm. For the sake of comparison, the computed SHG spectrum is also plotted (blue curve), and there is a fair agreement with the experiment. SHG measurements on the metallized membrane without patterning have been done, but the signal-to-noise ratio was lower than 1.

Figure 5 shows measured efficiency spectra for two other gratings GaAs on Au stack of layers. Therefore, the widths of

![](./images/812499380014678018_4.jpg)

Fig. 4. Measured SHG efficiency spectrum: the red dots are the mean value of five measurements at each wavelength, and the errorbars give their standard deviation for each wavelength. The computed SHG efficiency spectrum is also plotted (blue curve). The grating parameters are $w=235\ \text{nm}$, $d=544\ \mu\text{m}$, $h=152\ \text{nm}$.

![](./images/812499380014678018_5.jpg)

Fig. 5. Measured SHG spectra of different arrays (same GaAs thickness $h=152$ nm, but different period $d$ and ribbons width $w$) as a function of the pump wavelength. The grating shown in purple has the following parameters: $w=265$ nm and $d=500$ nm, and the grating shown in green has the following parameters: $w=235$ nm and $d=500$ nm.

the ribbons $w$ and the period $d$ are different, but the thickness $h$ of the GaAs layer remains the same. The grating represented in green has maximum efficiency at $\lambda=3234$ nm, whereas the grating represented in purple has maximum efficiency at $\lambda=3270$ nm. This is explained by the fact that the purple grating has a larger ribbons width (265 nm compared to 235 nm), while their period is the same ($d=500$ nm). Actually, the ribbon width $w$ affects the pump resonance wavelength (horizontal Fabry–Perot resonance), increasing it with higher $w$ (see Supplement 1). The purple grating is also more selective, with a FWHM of 68 nm, against 237 nm for the green grating (and 226 nm for the red grating shown in Fig. 4).

In conclusion, we have theoretically and experimentally studied a MIM structure including a crystalline GaAs layer. It supports both horizontal and vertical Fabry–Perot resonances, as well as a guided mode resonance, and the linear optical characterization is in good agreement with the theoretical predictions. We have experimentally demonstrated resonant SHG with an efficiency of $0.8 \times 10^{-8}\ \text{W}^{-1}$ at $\lambda=3.2\ \mu\text{m}$. Such multi-resonant structures are also promising to enhance difference-frequency generation, as was recently theoretically predicted [27], and to achieve generated wavelengths spanning the infrared and terahertz ranges. As a prospect, 111 GaAs could be used to improve even further the nonlinear polarization generation, and to avoid any dependency to the polarization of the pump wavelength [28]. Another interesting lead is to include multiple quantum wells (MQWs) in the place of the GaAs layer. Recent studies proved that use of MQWs can significantly improve the effective $\chi^{(2)}$ and, thus, the efficiency [29].

Acknowledgment. The authors acknowledge Benjamin Vest for fruitful discussions.

Disclosures. The authors declare no conflicts of interest.

Supplemental document. See Supplement 1 for supporting content.

## REFERENCES
1. J. A. Schuller, E. S. Barnard, W. Cai, Y. C. Jun, J. S. White, and M. L. Brongersma, *Nat. Mater.* **9**, 193 (2010).
2. P. Bouchon, F. Pardo, B. Portier, L. Ferlazzo, P. Ghenuche, G. Dagher, C. Dupuis, N. Bardou, R. Haïdar, and J.-L. Pelouard, *Appl. Phys. Lett.* **98**, 191109 (2011).
3. S. Xiao, Q. He, X. Huang, S. Tang, and L. Zhou, *Phys. Rev. B* **85**, 085125 (2012).
4. M. Kauranen and A. V. Zayats, *Nat. Photonics* **6**, 737 (2012).
5. S. Keren-Zur, L. Michaeli, H. Suchowski, and T. Ellenbogen, *Adv. Opt. Photon.* **10**, 309 (2018).
6. N. C. Panoiu, W. E. Sha, D. Y. Lei, and G.-C. Li, *J. Opt.* **20**, 083001 (2018).
7. A. Krasnok, M. Tymchenko, and A. Alu, *Mater. Today* **21**, 8 (2018).
8. V. K. Valev, N. Smisdom, A. V. Silhanek, B. De Clercq, W. Gillijns, M. Ameloot, V. Moshchalkov, and T. Verbiest, *Nano Lett.* **9**, 3945 (2009).
9. H. Husu, R. Siikanen, J. Makitalo, J. Lehtolahti, J. Laukkanen, M. Kuittinen, and M. Kauranen, *Nano Lett.* **12**, 673 (2012).
10. M. Celebrano, X. Wu, M. Baselli, S. Großmann, P. Biagioni, A. Locatelli, C. De Angelis, G. Cerullo, R. Osellame, B. Hecht, L. Duò, F. Ciccacci, and M. Finazzi, *Nat. Nanotechnol.* **10**, 412 (2015).
11. P. P. Vabishchevich, S. Liu, M. B. Sinclair, G. A. Keeler, G. M. Peake, and I. Brener, *ACS Photon.* **5**, 1685 (2018).
12. N. Segal, S. Keren-Zur, N. Hendler, and T. Ellenbogen, *Nat. Photonics* **9**, 180 (2015).
13. T. Skauli, K. L. Vodopyanov, T. J. Pinguet, A. Schober, O. Levi, L. A. Eyres, M. M. Fejer, J. S. Harris, B. Gerard, L. Becouarn, E. Lallier, and G. Arisholm, *Opt. Lett.* **27**, 628 (2012).
14. L. Carletti, D. de Ceglia, M. Vincenti, and C. De Angelis, *Opt. Express* **27**, 32480 (2019).
15. D. De Ceglia, G. D'Aguanno, N. Mattiucci, M. A. Vincenti, and D. M. Scalora, *Opt. Lett.* **36**, 704 (2011).
16. W. Fan, S. Zhang, K. J. Malloy, S. Brueck, N. C. Panoiu, and R. M. Osgood, *Opt. Express* **14**, 9570 (2006).
17. M. Scalora, M. A. Vincenti, D. De Ceglia, V. Roppo, M. Centini, N. Akozbek, and M. J. Bloemer, *Phys. Rev. A* **82**, 043828 (2010).
18. S. Héron, P. Bouchon, and R. Haïdar, *Phys. Rev. A* **94**, 033831 (2016).
19. F. Niesler, N. Feth, S. Linden, J. Niegemann, J. Gieseler, K. Busch, and M. Wegener, *Opt. Lett.* **34**, 1997 (2009).
20. E. D. Palik, *Handbook of Optical Constants of Solids* (Academic, 1998), Vol. 3.
21. F. X. Wang, F. J. Rodriguez, W. M. Albers, R. Ahorinta, J. Sipe, and M. Kauranen, *Phys. Rev. B* **80**, 233402 (2009).
22. P. Bouchon, F. Pardo, R. Haïdar, and J.-L. Pelouard, *J. Opt. Soc. Am. A* **27**, 696 (2010).
23. S. Héron, F. Pardo, P. Bouchon, J.-L. Pelouard, and R. Haïdar, *J. Opt. Soc. Am. B* **32**, 275 (2015).
24. M. Makhsiyan, “Nano-émetteurs thermiques multi-spectraux,” Ph.D. thesis (Paris-Saclay, 2017).
25. C. Wei, S. Liu, D. Deng, J. Shen, J. Shao, and Z. Fan, *Opt. Lett.* **31**, 1223 (2006).
26. C. Koechlin, P. Bouchon, F. Pardo, J. Jaeck, X. Lafosse, J.-L. Pelouard, and R. Haïdar, *Appl. Phys. Lett.* **99**, 241104 (2011).
27. L. Soun, S. Héron, H. El Ouazzani, B. Fix, R. Haïdar, and P. Bouchon, *Opt. Express* **28**, 27210 (2020).
28. J. D. Sautter, L. Xu, A. E. Miroshnichenko, M. Lysevych, I. Volkovskaya, D. A. Smirnova, R. Camacho-Morales, K. Z. Kamali, F. Karouta, K. Vora, H. H. Tan, M. Kauranen, I. Staude, C. Jagadish, D. N. Neshev, and M. Rahmani, *Nano Lett.* **19**, 3905 (2019).
29. S. Campione, A. Benz, M. B. Sinclair, F. Capolino, and I. Brener, *Appl. Phys. Lett.* **104**, 131104 (2014).