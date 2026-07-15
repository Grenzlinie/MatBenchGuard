# Experimental Study and Simulation of the Spectral Characteristics of LED Heterostructures with an InAs Active Region

A. A. Semakova$^{a,b,*}$, S. N. Lipnitskaya$^{b}$, K. D. Mynbaev$^{a}$, N. L. Bazhenov$^{a}$,
S. S. Kizhaev$^{c}$, A. V. Chernyaev$^{a,c,d}$, N. D. Stoyanov$^{c}$, and H. Lipsanen$^{b,e}$

$^{a}$ Ioffe Physical Technical Institute, Russian Academy of Sciences, St. Petersburg, 194021 Russia
$^{b}$ St. Petersburg University of Information Technologies, Mechanics, and Optics (ITMO University),
St. Petersburg, 197101 Russia
$^{c}$ Microsensor Technology, St. Petersburg, 194223 Russia
$^{d}$ S.M. Budyonny Military Academy of the Signal Corps, St. Petersburg, 194064 Russia
$^{e}$ Aalto University, FI-00076 Aalto, Finland

*e-mail: antonina.semakova@itmo.ru

Received July 18, 2019; revised July 18, 2019; accepted November 8, 2019

Abstract—The spectral parameters of midinfrared LED heterostructures with an InAs active region were studied experimentally, calculated using MATLAB, and simulated in COMSOL Multiphysics. The obtained data were compared to reveal the mechanism of formation of the emission spectra of these heterostructures. The results confirm that simulation is a promising design tool for LED structures.

Keywords: LED heterostructures, indium arsenide, electroluminescence.

DOI: 10.1134/S1063785020020121

The midinfrared range (3–5 $\mu$m) is used in gas and molecule spectroscopy, systems for detecting explo- sives, medical systems, and environmental monitor- ing. The rapid development of optoelectronic instru- ments operating in this range [1–4] is fueling interest in heterostructures (HSs) based on narrow-gap A$^{\text{III}}$B$^{\text{V}}$ semiconductors, which serve as the basis for such devices. We have recently reported the results of exper- imental studies of the electroluminescence (EL) of LED HSs with an active layer made of an InAsSb solid solution [5]. The aim of the present study was to deter- mine spectral characteristics of HSs with an InAs active layer experimentally and compare the obtained results with calculated and simulated data.

HSs were grown by metal-organic chemical vapour deposition at Microsensor Technology (Russia). The growth procedure was similar to that detailed in [6]. An intentionally undoped 2.5-$\mu$m-thick InAs active layer with an electron density of $\sim$10$^{16}$ cm$^{-3}$ was grown on an $n$-type InAs substrate (doped with sulfur). The HS growth was finalized by forming a wide-gap barrier layer doped with an acceptor impu- rity (zinc) to a density of $2 \times 10^{18}$ cm$^{-3}$. This barrier layer had the following chemical compositions: InAs$_{0.15}$Sb$_{0.31}$P$_{0.54}$ (structure no. 1), InAs$_{0.31}$Sb$_{0.23}$P$_{0.46}$ (no. 2), In$_{0.76}$Ga$_{0.24}$As$_{0.80}$Sb$_{0.20}$ (no. 3), and InAs$_{0.25}$Sb$_{0.25}$P$_{0.50}$ (no. 4). A solid contact was formed on the epitaxial HS side, and an annular contact with a width of 35 $\mu$m and an inner diameter of 200 $\mu$m was formed on the substrate. Radiation was extracted through the substrate.

LED chips $0.38 \times 0.38$ mm in size were fabricated by standart photolithography and wet chemical etch- ing. A contact system based on a multilayer Cr–Au– Ni–Au composition was used. The samples were placed on TO-18 holders.

EL spectra at temperature $T = 300$ K were recorded under pulsed excitation with a pulse rate of 1 kHz and a pulse duration of 1 $\mu$s. The signal was detected by a cooled InSb photodiode. The spectra were recorded with an MDR-23 monochromator.

Figure 1a shows the normalized EL spectra of the studied HSs obtained at $T = 300$ K and a pump current of 2 A. It can be seen that the spectra of HSs nos. 1 and 2 are symmetrical with a maximum corresponding to an energy of ~0.36 eV. The spectra of HSs nos. 3 and 4 are broader, and their maxima are shifted to 0.37 eV. This is attributable to the difference in substrate dop- ing levels: structures nos. 1 and 2 were grown on sub- strates doped to electron density $n \approx 2 \times 10^{18}$ cm$^{-3}$, while structures nos. 3 and 4 were grown on substrates doped to $n \approx 5 \times 10^{18}$ cm$^{-3}$. The optical transmission spectra of these two types of substrates at $T = 300$ K are presented in Fig. 1b. It is evident that the substrate for HSs nos. 1 and 2 (spectrum 1) absorbs the short- wavelength part of the EL spectrum, forming a sym-

metric spectrum with its maximum at ~0.36 eV. The substrates for HSs nos. 3 and 4 (spectrum 2) transmit a greater part of the EL spectrum, although they alter its shape at energies above ~0.45 eV.

Figure 2a shows the calculated optical absorption spectra of the studied substrates. The absorption coefficient was calculated using MATLAB and the formulas from [7]. The material parameters and the mathematical expressions for their calculation were taken from [8]. Absorption coefficient $\alpha$ was determined from the expression for permittivity $\chi''$:

$$
\chi'' = \frac{c\sqrt{\chi_{\infty}}}{\omega}\alpha(\omega),
$$

where $\chi_{\infty}$ is the high-frequency permittivity, $c$ is the speed of light, and $\omega$ is the frequency. The permittivity itself was defined as follows:

$$
\begin{aligned}
\chi''(\omega, 0) &= \frac{e^{2}\sqrt{m_{e}}}{\eta^{2}\omega\sqrt{E_{g}}}\bigg\{\sqrt{2}\sqrt{\eta\omega(\eta\omega - E_{g})}[1 - f_{n}^{(h)}] \\
&+ \frac{1}{6\sqrt{2}}\sqrt{(\eta^{2}\omega^{2} - E_{g}^{2})}\bigg(\frac{2E_{g}^{2}}{\eta^{2}\omega^{2}} + 1\bigg)[1 - f_{n}^{(l)}]\bigg\},
\end{aligned}
$$

where the first and the second terms in curly brackets characterize transitions involving a heavy hole and a light one, respectively. The dependences of the hole energy on the wave vector were taken to be parabolic and nonparabolic for heavy and light holes, respectively:

$$
\begin{aligned}
f_{n}^{(h)} &= \left(1 + \exp\left(\frac{\eta\omega - E_{g}}{k_{\text{B}}T}\left(1 - \frac{m_{e}}{m_{h}}\frac{\eta\omega}{E_{g}}\right) - \frac{\varepsilon_{c}}{k_{\text{B}}T}\right)\right)^{-1}, \\
f_{n}^{(l)} &= \left(\exp\left(\frac{\eta\omega - E_{g}}{2k_{\text{B}}T} - \frac{\varepsilon_{c}}{k_{\text{B}}T}\right) + 1\right)^{-1}.
\end{aligned}
$$

Here, $\varepsilon_{c}$ is the energy of the Fermi quasi-level for electrons, $k_{\text{B}}$ is the Boltzmann constant, $m_{e}$ is the electron mass, and $m_{h}$ is the mass of heavy holes. In order to verify the accuracy of calculations, the results were compared to experimental data on the absorption coefficient of InAs from [9]. With the electron densities being equal and $\alpha = 10^{2}\ \text{cm}^{-1}$, the calculated data differed from the experimental ones by several millielectronvolts. This suggests that the calculations were correct. The qualitative agreement between the experimentally measured substrate transmission spectra (Fig. 1b) and the calculated InAs absorption spectra (Fig. 2a) with carrier density $n \approx 2 \times 10^{18}$ and $5 \times 10^{18}\ \text{cm}^{-3}$ also confirms the validity of calculations.

Figure 2b presents the normalized EL spectra (the experimental spectrum, the emission spectrum of InAs calculated using MATLAB, and the emission spectrum of the active HS layer simulated in COMSOL Multiphysics) of structure no. 4. Calculations were performed in the approximation of a nonparabolic dependence of the energy of electrons and light holes on the wave vector in accordance with the procedure outlined in [7]. The nonequilibrium carrier density was set to $4 \times 10^{16}\ \text{cm}^{-3}$ in accordance with the data obtained earlier under similar injection conditions in structures with an InAsSb active layer [5]. The finite-volume method was used in modeling to solve the electrostatic Poisson equation together with the electron and hole transport equations in the stationary formulation and in the approximation of a parabolic dependence of the energy on the wave vector. Only the interband recombination mechanisms and spontaneous emission were taken into account. Elements of the transition matrix were defined in terms of the radiative recombination lifetime. The entire HS was simulated (the insulation boundary condition was set at the HS sides, and the continuity/heterojunction condition was set at the layer boundaries using the thermionic emission model). The thicknesses of the substrate, the active region, and the barrier layer were set

![](./images/812645713602150401_1.jpg)

Fig. 1. (a) Normalized EL spectra of heterostructures nos. 1–4 (see numbers next to curves) recorded at 300 K and a pump current of 2 A. (b) Optical transmission spectra of InAs substrates with an electron density of (1) $2 \times 10^{18}$ and (2) $5 \times 10^{18}\ \text{cm}^{-3}$ shown next to (3) the EL spectrum of structure no. 4. The features at ~0.29 eV are associated with the absorption band of carbon dioxide in the atmosphere.

![](./images/812645713602150401_2.jpg)

Fig. 2. (a) Calculated optical absorption spectra of InAs with an electron density of (1) $2 \times 10^{18}$ and (2) $5 \times$ $10^{18}$ cm$^{-3}$. (b) Normalized EL spectra of structure no. 4 for $T = 300$ K: (1) experimental spectrum, (2) spectrum calculated using MATLAB for InAs with an injected carrier density of $4 \times 10^{16}$ cm$^{-3}$, and spectra simulated in COMSOL Multiphysics for a constant pump current of (3) 3.8 and (4) 150 mA.

to 250, 2.5, and 1.2 $\mu$m, respectively. The material parameters and the mathematical expressions for their calculation were also taken from [8]. It can be seen that the experimental results agree well with the calculated and simulated data in the case when a constant current of 3.8 mA passing through the structure was simulated. The maximum of the spectrum obtained in the simulation with a current of 150 mA is shifted considerably toward higher energies. This is attributable to the fact that the Fermi quasi-level for electrons shifts upwards as the density of injected carriers increases. The similarity of curves 2 and 3 in Fig. 2b suggests that, as expected, the nonparabolicity of the dependence of the energy of electrons and light holes on the wave vector does not manifest itself at low carrier densities.

![](./images/812645713602150401_3.jpg)

Fig. 3. Calculated temperature dependence of bandgap $E_g$ of nondegenerate InAs (curve) and $E_g$ values determined for structures nos. (1) 4 and (2) 3 based on the EL spectra in accordance with the procedure detailed in [5].

Figure 3 presents the temperature dependences of $E_g$ determined based on the experimental EL spectra for HSs nos. 3 and 4 in accordance with the algorithm outlined in [5] (an excitation current of 800 mA was used in the present case). The calculated values of $E_g$ for nondegenerate InAs are also shown in Fig. 3. Just as the structures with an InAsSb active region [5], the studied HSs emitted stimulated radiation under excitation at temperatures below 75 K. These data are not shown and will be discussed in subsequent publications. The calculated and experimental data agree fairly well at 75 < $T$ < 300 K, thus providing additional evidence of emission from the active layer. The FWHM of the emission line increased smoothly from 20–25 meV at $T = 77$ K to 50–60 meV at 300 K, which is typical of LEDs of this design [10–12].

Thus, the comparison of experimental data and the results of calculations and simulation of the spectral characteristics of InAs/(Ga)InAsSb(P) LED HSs grown on InAs substrates revealed the mechanism of formation of the emission spectra of these HSs. It was demonstrated that the simulation results agree with the experimental data and the data calculated for the material of the HS active region. The obtained results confirm that simulation is a promising design tool for LED heterostructures.

## CONFLICT OF INTEREST

The authors declare that they have no conflict of interest.


### REFERENCES

1. D. Jung, S. Bank, M. L. Lee, and D. Wasserman, J. Opt. **19**, 123001 (2017).

2. C. L. Tan and H. Mohseni, Nanophotonics 7, 169 (2018).

3. S. A. Karandashev, B. A. Matveev, and M. A. Remennyi, Semiconductors **53**, 139 (2019).

4. M. P. Mikhailova, K. D. Moiseev, and Yu. P. Yakovlev, Semiconductors **53**, 273 (2019).

5. K. D. Mynbaev, N. L. Bazhenov, A. A. Semakova, A. V. Chernyaev, S. S. Kizhaev, N. D. Stoyanov, V. E. Bougrov, H. Lipsanen, and Kh. M. Salikhov, Infrared Phys. Technol. **85**, 246 (2017).

6. M. Sopanen, T. Koljonen, H. Lipsanen, and T. Tuomi, J. Cryst. Growth **145**, 492 (1994).

7. N. L. Bazhenov, K. D. Mynbaev, and G. G. Zegrya, Semiconductors **49**, 1170 (2015).

8. I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, J. Appl. Phys. **89**, 5815 (2001).

9. J. R. Dixon and J. M. Ellis, Phys. Rev. **123**, 1560 (1961).

10. E. A. Grebenshchikova, N. V. Zotova, S. S. Kizhaev, S. S. Molchanov, and Yu. P. Yakovlev, Tech. Phys. **46**, 1125 (2001).

11. N. V. Zotova, N. D. Il’inskaya, S. A. Karandashev, B. A. Matveev, M. A. Remennyi, N. M. Stus’, V. V. Shus-tov, and N. G. Tarakanova, Semiconductors **40**, 977 (2006).

12. B. Matveev, N. Zotova, N. Il’inskaya, S. Karandashev, M. Remennyi, N. Stus’, A. P. Kovchavtsev, G. L. Kuryshev, V. G. Polovinkin, and N. Tarakanova, MRS Proc. **891**, 0891-EE01-04 (2005).

*Translated by D. Safin*