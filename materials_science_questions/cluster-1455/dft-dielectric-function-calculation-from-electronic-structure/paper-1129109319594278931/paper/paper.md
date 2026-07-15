
# Resonant Self-Diffraction of Femtosecond Extreme Ultraviolet Pulses in Cobalt

Alexei A. Maznev, \( ^{1,*} \)  Wonseok Lee, \( ^{2} \)  Scott K. Cushing, \( ^{2}~ \)  Dario De Angelis, \( ^{3} \)  Danny Fainozzi, \( ^{3}~ \)  Laura Foglia, \( ^{3} \)  Christian Gutt, \( ^{4} \)  Nicolas Jaouen, \( ^{5,6} \)  Fabian Kammerbauer, \( ^{7} \)  Claudio Masciovecchio, \( ^{3} \)  Riccardo Mincigrucci, \( ^{3}~ \)  Keith A. Nelson, \( ^{1}~ \)  Ettore Paltanin, \( ^{3}~ \)  Jacopo Stefano Pelli-Cresi, \( ^{3} \)  Vincent Polewczyk, \( ^{8} \)  Dmitriy Ksenzov, \( ^{4} \)  Filippo Bencivenga. \( ^{3} \) 

 \( ^{1} \) Department of Chemistry, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA  
 \( ^{2} \) Division of Chemistry and Chemical Engineering, California Institute of Technology, California 91125, USA  
 \( ^{3} \) Elettra-Sincrotrone Trieste, SS 14 km 163,5 in AREA Science Park, 34149 Trieste, Italy  
 \( ^{4} \) Department Physik, Universität Siegen, Walter-Flex-Strasse 3, 57072 Siegen, Germany  
 \( ^{5} \) Synchrotron SOLEIL, L'Orme des Merisiers, Saint-Aubin, Gif-sur-Yvette Cedex, 91192, France  
 \( ^{6} \) Department of Molecular Sciences and Nanosystems, Ca' Foscari University of Venice, 30172 Venezia, Italy  
 \( ^{7} \) Institute of Physics, Johannes Gutenberg University Mainz, 55099 Mainz, Germany  
 \( ^{8} \) Université Paris-Saclay, UVSQ, CNRS, GEMaC, 78000, Versailles, France  
 \( ^{*} \) Corresponding author: alexei.maznev@gmail.com

## Abstract

Self-diffraction is a non-collinear four-wave mixing technique well-known in optics. We explore self-diffraction in the extreme ultraviolet (EUV) range, taking advantage of intense femtosecond EUV pulses produced by a free electron laser. Two pulses are crossed in a thin cobalt film and their interference results in a spatially periodic electronic excitation. The diffraction of one of the same pulses by the associated refractive index modulation is measured as a function of the EUV wavelength. A sharp peak in the self-diffraction efficiency is observed at the  \( M_{2,3} \)  absorption edge of cobalt at 59 eV and a fine structure is found above the edge. The results are compared with a theoretical model assuming that the excitation results in an increase of the electronic temperature. EUV self-diffraction offers a potentially useful spectroscopy tool and will be instrumental in studying coherent effects in the EUV range.

The advent of free electron lasers (FELs) enabled the expansion of nonlinear optical spectroscopy methods into extreme ultraviolet (EUV) and X-ray ranges  \( [1] \) . In particular, four-wave mixing (FWM) techniques with EUV and EUV/optical fields are being actively developed  \( [2–5] \) . Self-diffraction (SD) is the simplest non-collinear FWM process, in which the interference of two coherent beams crossed in the sample results in a spatially periodic excitation acting as a diffraction grating for the same beams. It is a well-known technique  \( [6,7] \)  widely used in nonlinear optical studies  \( [8–11] \) . The SD geometry has also been used by theoreticians investigating nonlinear optical interactions in condensed matter  \( [12, 13] \) .

In the EUV range, a related FWM technique referred to as EUV transient grating (TG) spectroscopy has recently been developed at the FERMI FEL  \( [4,14] \) . In the TG technique, a time-delayed probe pulse diffracts off a spatially periodic excitation produced by two time-coincident pump pulses crossed at the sample. SD of time-coincident pulses can be thought of as a degenerate version of a TG experiment at a zero pump-probe delay, where a pump beam serves as a zero-delay probe. The SD geometry has the advantage of simplicity, which is important at short wavelengths where manipulating multiple noncollinear beams is significantly more difficult  \( [15] \)  than in a conventional optical experiment. Even more importantly, in the EUV TG experiments performed to date, the FEL wavelength could not be continuously tuned because of the narrow-band multilayer mirrors in the probe beam path. The SD approach overcomes this limitation, enabling studies in the vicinity of resonances, which has been identified by theoreticians as an especially promising application of FWM at short wavelengths  \( [16] \) .
 

In this report, we describe an EUV SD experiment on a thin cobalt film, with the photon energy scanned across the  \( M_{2,3} \)  edge of Co. We observe a great enhancement of the SD efficiency at the resonant absorption edge and a fine structure above the edge. The results are compared with ab initio calculations using density functional theory (DFT) and the Bethe-Salpeter equation (BSE) based on the assumption that the electronic system is nearly thermalized within the FEL pulse duration.

The experiment was conducted at the TIMER beamline at FERMI and is schematically shown in Fig. 1(a). Two 50 fs EUV pulses are obtained by bisecting the FEL output with a grazing incidence mirror. The beams are spatially and temporally overlapped at the sample, with a crossing angle of  \( 2\theta = 18.4^{\circ} \)  (the bisector being normal to the sample surface) and a FWHM spot size of  \( 300 \mu m \) . Each of the incident beams gives rise to two first order SD beams. One of the SD beams from pump A coincides with the transmitted pump B; the other SD beam goes into a background-free direction making an angle of  \( \psi = \arcsin(3 \sin(\theta)) = 28.7^{\circ} \)  to the sample normal and is detected by a CCD camera [17]. The sample was a 20-nm-thick Co film deposited by e-beam evaporation on a 30 nm silicon nitride membrane. The measurements were performed at room temperature in high vacuum.

(a)

![](./images/1129109319594278931_1.jpg)

(b)

![](./images/1129109319594278931_2.jpg)

FIG. 1. (a) Schematic of the experiment. Dashed lines show background-free SD beams. (b) Images of the SD signal spot on the detector at photon energies corresponding to the smallest (54.6 eV) and largest (58.9 eV) SD signal. The color scale bars show CCD counts (note the substantial scale difference between the two images).

The CCD camera images obtained by averaging over 250 FEL shots show a bright spot at the expected position of the SD signal, which only appears when the two pump beams are overlapped at the sample, see representative images in Fig. 1(b). To quantify the SD signal, the CCD image is integrated within a region of interest chosen to include the entire SD spot. Figure 2(a) shows the dependence of the SD signal on the FEL photon energy (hv) in the range 54.6 – 72.1 eV (wavelengths 17.2 – 22.7 nm). For each value of hv, we obtained 3 – 8 images used to calculate the average value shown in Fig. 2(a) and the standard error shown as the error bars. The FEL pulse energy at the sample was  \( \sim \) 1  \( \mu \) J, with variations within a factor of two across the hv scan. To compensate for the variations of the FEL intensity, the signal is normalized by the cube of the FEL intensity in accordance with the expected intensity dependence of a FWM signal.

The most conspicuous feature in Fig. 2(a) is the sharp increase of the SD signal at the absorption edge. Between 54.6 eV and the peak at 58.8 eV, the increase is a factor of 500. Past the absorption edge, the SD signal decreases but remains higher than pre-edge. Furthermore, the SD spectrum above
 

the edge exhibits a fine structure involving a shoulder at ~61 eV, a dip at 62.5 eV, and a peak at 64 eV. This fine structure is not present in the EUV absorption spectrum of Co [18].

Figure. 2(b) shows the dependence of the SD signal on the FEL pulse energy at the sample at 59 eV, i.e., near the peak of the SD response, and confirms the cubic dependence mentioned above [19]. Note that the dynamic range of this measurement amounted to 4 orders of magnitude and the signal level, on the high end, exceeded 5000 photons/shot.

![](./images/1129109319594278931_3.jpg)

![](./images/1129109319594278931_4.jpg)

FIG. 2. (a) The dependence of the SD signal normalized by the cube of the FEL intensity on the photon energy (blue) and the spectrum of the imaginary part of the refractive index  \( \beta \)  adopted from Ref. [18] (green). Error bars reflect the standard error obtained from multiple measurements done at the same photon energy; where the error bars are not shown, they are smaller than the symbol size. (b) The dependence of the SD signal on the FEL intensity at the sample at  \( h\nu = 59 \, eV \)  (symbols). The dashed line shows a cubic dependence fit.

A natural question to ask is whether the observed resonant SD phenomenon is due to a coherent  \( \chi^{(3)} \)  response involving the core hole and initially excited electron [16], or whether it is caused by an incoherent population of excited electrons resulting from multi-step relaxation of the initial excitation [20]. The dephasing time of the  \( M_{2} \)  and  \( M_{3} \)  resonances in Co is estimated from the corresponding linewidths [21] as ~3 fs, which is much shorter than the FEL pulse duration. While the short dephasing time does not preclude the presence of a coherent  \( \chi^{(3)} \)  response, the latter seems inconsistent with a recently reported TG measurement with a variably delayed probe pulse on a similar sample [22] with the pump and probe photon energy 59.6 eV, i.e., close to the peak of our SD spectrum. In that experiment, the initial fast response was characterized by a short rise time comparable to the FEL pulse duration and a slower decay time of ~250 fs. Due to the short dephasing time, a coherent  \( \chi^{(3)} \)  response would only exist while the pump and probe pulses overlapped, which is incompatible with the observed slow decay. As mentioned above, our SD measurement can be considered a degenerate version of TG experiment at the zero pump-probe delay. Consequently, we believe that our
 

SD signal is more likely to be produced by an incoherent population of excited electrons than by a coherent  \( \chi^{(3)} \)  response.

The simplest way to model the formation of the SD signal due to an incoherent electronic excitation is to assume that the electrons get thermalized faster than the FEL pulse duration. It was reported that electronic thermalization following optical excitation of Co occurs within 2 fs [23]. While thermalization of the excitation produced by  \( \sim60 \)  eV EUV photons may take longer, we believe that assuming a thermalized electronic sub-system is a reasonable first step towards developing the theory of the observed phenomenon.

We calculate the variation of the complex refractive index at the EUV wavelength caused by an electronic temperature change using DFT and BSE  \( [24–27] \) . The electronic temperature is implemented in the BSE Hamiltonian  \( H^{BSE} \)  by modifying the fractional occupation numbers  \( [28–30] \) 

 \[ H_{i j}^{B S E}=\epsilon_{i}\delta_{i j}+\sqrt{\tilde{f}_{i}}[V_{X}-W]\sqrt{\tilde{f}_{j}}. \quad (1) \] 

In Eq. (1), the notation  \( i = \{vck\} \)  represents the electron-hole pair indexes for each valence and conduction bands ( \( \nu \)  and c) and k-points (k). The Hamiltonian includes the bare energies  \( \epsilon_{i} \) , the occupation number difference between the nominal electron ( \( f_{ei} \) ) and hole ( \( f_{hi} \) ) states  \( \widetilde{f}_{i} = |f_{ei} - f_{hi}| \) , and the two electron-hole interaction terms, the direct W and exchange  \( V_{X} \) . While the electron-hole correlation function in the BSE can be expanded into an infinite series, the first-order electron-hole interaction terms are only considered here. Additionally, the Tamm-Dancoff approximation is employed to simplify the calculations and make them computationally more efficient, while still providing reasonably accurate results for calculating the complex dielectric function [31]. The individual occupation numbers are given by the Fermi-Dirac distribution function  \( (E, \mu(T_{e}), T_{e}) = \{\exp[(E - \mu(T_{e}))/(k_{B}T_{e})] + 1\}^{-1} \)  where  \( \mu \)  is the chemical potential,  \( k_{B} \)  is the Boltzmann constant, and  \( T_{e} \)  indicates the electron temperature. The chemical potential is determined using the electronic density of states in Co obtained from DFT [32]. By solving the BSE via the Haydock recursion method, the complex dielectric function is derived from the photon operator  \( \hat{T} \)  acting on the ground state  \( |\Phi_{0}\rangle \)  and two-particle Green's function at energy  \( \omega \)  defined as  \( G_{2}(\omega) = (\omega - H^{BSE} + i\eta)^{-1} \)  with the BSE Hamiltonian and broadening parameter  \( \eta \) ,

 \[ \epsilon(\omega)=1-\frac{4\pi}{\Omega_{\mathrm{V}}q^{2}}\Big\langle\Phi_{0}\Big|\hat{T}^{+}\frac{1}{\omega-H^{B S E}+i\eta}\hat{T}\Big|\Phi_{0}\Big\rangle, \quad (2) \] 

where  \( \Omega_{V} \)  is the unit cell volume and q denotes the magnitude of the photon momentum [26, 33]. The dielectric function is then converted into the complex refractive index:  \( \tilde{n} = 1 - \delta + i\beta \) .

The diffraction efficiency of a refractive index grating in a weakly absorbing material is proportional to  \( (\Delta\delta)^{2} + (\Delta\beta)^{2} \) , where  \( \Delta\delta \)  and  \( \Delta\beta \)  are the amplitudes of the modulation of the real and imaginary parts of the refractive index, respectively [34]. In our case, the material is strongly absorbing at the EUV wavelength, which leads to a more complicated expression for the diffraction efficiency [22]. Representing the refractive index variation as  \( (\Delta\delta)^{2} + (\Delta\beta)^{2} = A(h\nu)\rho^{2} \) , where  \( A(h\nu) \)  is a function of the photon energy and  \( \rho \)  is the absorbed energy density and using Eq. (5) from Ref. [22], we obtain the following expression for the normalized SD signal,

 \[ \frac{l_{SD}}{l_{0}^{3}}\propto A(h\nu)\frac{e^{-\frac{d}{L\cos\psi}}}{L^{2}}\frac{e^{-\frac{d}{\tilde{L}^{*}}}-2e^{-\frac{d}{2\tilde{L}^{*}}\cos(\Delta Q_{Z}d)+1}}{\Delta Q_{Z}^{2}+\frac{1}{4L^{*2}}}, \quad (3) \]
 

where  \( I_{5D} \)  is the SD signal,  \( I_{0} \)  is the pump pulse energy, d is the sample thickness, L is the absorption length at the EUV wavelength,  \( L^{*} = L(3/\cos\theta - 1/\cos\psi)^{-1} \) , and  \( \Delta Q_{z} = k(\cos\theta - \cos\psi) \) , where k is the EUV wave vector. (We only retained the terms dependent on the photon energy.) We calculate  \( A(h\nu) \)  by computing  \( (\Delta\delta)^{2} + (\Delta\beta)^{2} \)  at a fixed electronic temperature rise of 100 K above a background temperature of 300 K [32] and take  \( L(h\nu) \)  from Ref. [18]. (As one can see from the supplemental Fig. S4 [20], the variations of  \( \delta \)  and  \( \beta \)  are comparable in magnitude.)

![](./images/1129109319594278931_5.jpg)

FIG. 3. Calculated SD spectrum (solid curve) based on the assumption that the EUV excitation modulates the complex refractive index via electronic temperature vs experimental data (dots). Both the theoretical curve and experimental data are normalized to unity at their maxima.

Figure 3 shows the calculated SD spectrum alongside the experimental data. The calculated SD spectrum reproduces a sharp peak at the Co  \( M_{2,3} \)  edge and exhibits smaller peaks above the edge, qualitatively agreeing with experiment. At the Co  \( M_{2,3} \)  edge, EUV photons excite core 3p electrons to unoccupied states near the Fermi level in the conduction band formed by 3d states. Changes in the electron temperature alter the electronic population near the Fermi level, as described by Fermi-Dirac statistics. When the final state of the transition lies at the Fermi level, the refractive index becomes highly sensitive to variations in the electronic temperature, which explains the intense SD peak. The interactions between electrons involved in the transition and screening processes lead to collective excitations above the Co  \( M_{2,3} \)  edge [35]. This many-body effect is captured by using the screened Coulomb potential in the direct term (W) of the BSE Hamiltonian in Eq. (1). The transition probability is modified due to the changes in the electronic population and spectral changes resulting from the state-filling effect are therefore observed beyond the absorption edge. The fine structure above the edge is less accurately reproduced by our calculations, because the model used here is primarily designed for calculating the spectrum near an absorption edge and may not be as suitable for simulating the extended SD spectrum.

While the present experiment provides a proof-of-principle for resonant EUV SD, further developments can be anticipated. Firstly, the fact that the M-edge resonance is much more prominent in the SD spectrum than in the absorption spectrum indicates the potential of the SD technique as a spectroscopy tool. We expect the fine structure in the SD spectrum to be specific to a particular chemical compound, which may lead to a nonlinear near-edge EUV spectroscopy technique based on SD. One can also envision looking for signatures of coherent FWM effects: for example, a photon echo can be detected in SD by introducing a delay between the two pulses  \( [36, 37] \) . Even though we believe that the coherent  \( \chi^{(3)} \)  response is unlikely to tangibly contribute to the SD signal in the present experiment, one can use absorption edges of lighter elements with longer dephasing time  \( [5] \)  and shorter EUV pulses. Experiments with gas phase samples, where hundreds-fs dephasing times have been reported  \( [38] \)  may prove especially promising. Whereas the present experiment was conducted
 

at an FEL facility, the simplicity of the SD setup and large signal levels may enable “table-top” EUV FWM experiments with high-harmonic generation sources [39].

In summary, we have demonstrated femtosecond SD in the EUV range. By scanning the photons energy across the  \( M_{2,3} \)  edge of Co, we obtain an SD spectrum revealing a resonant peak at the absorption edge, and a fine structure above the edge. The SD spectrum is much more structured than the EUV absorption spectrum, which may yield a useful nonlinear EUV spectroscopy tool. While a model based on an incoherent mechanism in which the SD signal is produced by a modulation of the electronic temperature yields a reasonable agreement with the experiment, it is anticipated that SD can be used to study coherent FWM effects in the EUV and possibly X-ray ranges.

## Acknowledgments

A.A.M. and K.A.N. received support from the Department of Energy, Office of Science, Office of Basic Energy Sciences, under Award Number DE-SC0019126. W.L. and S.K.C. were supported as part of Ensembles of Photosynthetic Nanoreactors (EPN), an Energy Frontiers Research Center funded by the U.S. DOE, Office of Science under Award No. DE-SC0023431. W.L. acknowledges support from the Korea Foundation for Advanced Studies. D.K. and C.G. acknowledge funding by the Deutsche Forschungsgemeinschaft (DFG) projects GU 535/9-1 and KS 62/3-1. C.G. acknowledges funding from BMBF(05K24PSA) and DFG (NFDI 40/1). F.K. acknowledges funding by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) TRR 173/2 Spin+X (Project A01 and B02). The calculations presented here were conducted in the Resnick High Performance Computing Center, a facility supported by Resnick Sustainability Institute at the California Institute of Technology.

## References

[1] M. Chergui, M. Beye, S. Mukamel, C. Svetina, and C. Masciovecchio, Progress and prospects in nonlinear extreme-ultraviolet and X-ray optics and spectroscopy, Nat. Rev. 5, 578 (2023).

[2] F. Bencivenga, R. Cucini, F. Capotondi, A. Battistoni, R. Mincigrucci, E. Giangrisostomi, A. Gessini, M. Manfredda, I. P. Nikolov, E. Pedersoli et al., Four-wave mixing experiments with extreme ultraviolet transient gratings, Nature 520, 205 (2015).

[3] L. Foglia, F. Capotondi, R. Mincigrucci, D. Naumenko, E. Pedersoli, A. Simoncig, G. Kurdi, A. Calvi, M. Manfredda et al., First Evidence of Purely Extreme-Ultraviolet Four-Wave Mixing, Phys. Rev. Lett. 120, 263901 (2018).

[4] F. Bencivenga, R. Mincigrucci, F. Capotondi, L. Foglia, D. Naumenko, A. A. Maznev, E. Pedersoli, A. Simoncig, F. Caporaletti, V. Chiloyan et al., Nanoscale transient gratings excited and probed by extreme ultraviolet femtosecond pulses, Sci Adv. 5, eaaw5805 (2019).

[5] H. Rottke, R. Y. Engel, D. Schick, J. O. Schunck, P. S. Miedema, M. C. Borchert, M. Kuhlmann, N. Ekanayake, S. Dziarzhytski, G. Brenner et al., Probing electron and hole colocalization by resonant four-wave mixing spectroscopy in the extreme ultraviolet, Sci Adv. 8, eabn5127 (2022).

[6] R. L. Carman, R. Y. Chiao, and P. L. Kelley, Observation of Degenerate Stimulated Four-Photon Interaction and Four-Wave Parametric Amplification, Phys. Rev. Lett. 17, 1281 (1966).

[7] V. L. Vinetskii, N. V. Kukhtarev, S. G. Odulov and M. S. Soskin, Dynamic self-diffraction of coherent light beams, Sov. Phys. Usp. 22, 742 (1979).

[8] E. O. Göbel, K. Leo, T. C. Damen, J. Shah, S. Schmitt-Rink, W. Schäfer, J. F. Müller, and K. Köhler, Quantum beats of excitons in quantum wells, Phys. Rev. Lett. 64, 1801 (1990).
 

[9] P. Kner, W. Schäfer, R. Lövenich, and D.S. Chemla, Coherence of four-particle correlations in semiconductors, Phys. Rev. Lett. 81, 5386 (1998).

[10] D. J. Kane and R. Trebino, Characterization of arbitrary femtosecond pulses using frequency-resolved optical gating, IEEE J. Quant. Electron. 29, 571 (1993).

[11] T. Rappen, U. Peter, M. Wegener, and W. Schäfer, Coherent dynamics of continuum and exciton states studied by spectrally resolved fs four-wave mixing, Phys. Rev. B 48, 4879 (1993).

[12] A. I. Lvovsky and S. R. Hartmann, Superradiant self-diffraction, Phys. Rev. A 59, 4052 (1999).

[13] T. Meier, V. Chernyak, and S. Mukamel, Femtosecond photon echoes in molecular aggregates, J. Chem. Phys. 107, 8759 (1997).

[14] F. Bencivenga, F. Capotondi, L. Foglia, R. Mincigrucci, and C. Masciovecchio, Extreme ultraviolet transient gratings, Adv. Phys. X 8, 2220363 (2023).

[15] R. Mincigrucci, L. Foglia, D. Naumenko, E. Pedersoli, A. Simoncig, R. Cucini, A. Gessini, M.P. Kiskinova, G. Kurdi, N. Mahne et al., Advances in instrumentation for FEL-based four-wave mixing experiments, Nucl. Instrum. Methods Phys. Res. Sect. A 907, 132 (2018).

[16] S. Tanaka and S. Mukamel, X-ray four-wave mixing in molecules, J. Chem. Phys. 116, 1877 (2002).

[17] Note that for the background-free SD, the Bragg diffraction condition is not satisfied. However, the Bragg condition is relaxed for thin gratings. Based on the expression for TG diffraction efficiency in transmission in Ref. [22], we find that in our geometry the signal reduction due to the deviation from the Bragg condition is less than 4%.

[18] Q. Saadeh, P. Naujok, D. Thakare, M. Wu, V. Philipsen, F. Scholze, C. Buchholz, Z. Salami, Y. Abdulhadi, D. O. García et al., On the optical constants of cobalt in the M-absorption edge region, Optik 273, 170455 (2023).

[19] At the high end of the intensity range, we had to use just a few FEL shots per image to avoid overloading of the detector, and the shutter did not provide sufficient accuracy for counting the number of shots, which explains the deviation of the data taken at high intensities from the cubic trend.

[20] N. Medvedev, U. Zastrau, E. Förster, D. O. Gericke, and B. Rethfeld, Short-Time Electron Dynamics in Aluminum Excited by Femtosecond Extreme Ultraviolet Radiation, Phys. Rev. Lett. 107, 165003 (2011).

[21] J. L. Campbell and T. Papp, Width of the atomic K-N7 levels, Atomic Data and Nuclear Data Tables 77, 1 (2001).

[22] L. Foglia, R. Mincigrucci, A.A. Maznev, G. Baldi, F. Capotondi, F. Caporaletti, R. Comin, D. De Angelis, R.A. Duncan, D. Fainozzi et al., Extreme ultraviolet transient gratings: A tool for nanoscale photoacoustics, Photoacoustics 29, 100453 (2023).

[23] B. R. de Roulet, L. Drescher, S. A. Sato, and S. R. Leone, Initial electron thermalization in metals measured by attosecond transient absorption spectroscopy, Phys. Rev. B 110, 174301 (2024).

[24] P. Giannozzi et al., Advanced capabilities for materials modelling with Quantum ESPRESSO, J. Phys.: Condens. Matter 29, 465901 (2017).

[25] P. Giannozzi et al., QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter 21, 395502 (2009).

[26] J. Vinson, Advances in the OCEAN-3 spectroscopy package, Phys. Chem. Chem. Phys. 24, 12787 (2022).
 

[27] J. Vinson, J. J. Rehr, J. J. Kas, and E. L. Shirley, Bethe-Salpeter equation calculations of core excitation spectra, Phys. Rev. B 83, 115106 (2011).

[28] A. Schleife, C. Rödl, F. Fuchs, K. Hannewald, and F. Bechstedt, Optical absorption in degenerately doped semiconductors: Mott transition or Mahan excitons? Phys. Rev. Lett. 107, 236405 (2011).

[29] D. Sangalli, S. Dal Conte, C. Manzoni, G. Cerullo, and A. Marini, Nonequilibrium optical properties in semiconductors from first principles: A combined theoretical and experimental study of bulk silicon, Phys. Rev. B 93, 195205 (2016).

[30] I. M. Klein, A. Krotz, W. Lee, J. M. Michelsen, and S. K. Cushing, Ab initio calculations of XUV ground and excited states for first-row transition metal oxides, J. Phys. Chem. C 127, 1077 (2023).

[31] L. X. Benedict, E. L. Shirley, and R. B. Bohn, Optical absorption of insulators and the Electron-Hole Interaction: An Ab Initio Calculation, Phys. Rev. Lett. 80, 4514 (1998).

[32] See Supplemental Material for details on the calculations of the electronic density of states, chemical potential, and complex refractive index for hcp cobalt.

[33] L. X. Benedict and E. L. Shirley, Ab initio calculation of  \( \varepsilon_{2}(\omega) \)  including the electron-hole interaction: Application to GaN and  \( CaF_{2} \) , Phys. Rev. B 59, 5441 (1999).

[34] K. A. Nelson, R. Casalegno, R. J. D. Miller, and M. D. Fayer, Laser-induced excited state and ultrasonic wave gratings: Amplitude and phase grating contributions to diffraction, J. Chem. Phys. 77, 1144 (1982).

[35] J. P. Connerade, Controlled Collapse and the Profiles of ‘Giant Resonances,’ in Giant Resonances in Atoms, Molecules, and Solids, edited by J. P. Connerade, J. M. Esteva, and R. C. Karnatak (Springer US, Boston, MA, 1987), pp. 3–23.

[36] I. D. Abella, N. A. Kurnit, and S. R. Hartmann, Photon echoes, Phys. Rev. 141, 391 (1966).

[37] D. Bennhardt, P. Thomas, R. Eccleston, E. J. Mayer, and J. Kuhl, Polarization dependence of four-wave-mixing signals in quantum wells, Phys. Rev. B 47, 13485 (1993).

[38] A. Wituschek, L. Bruder, E. Allaria, U. Bangert, M. Binz, R. Borghes, C. Callegari, G. Cerullo, P. Cinquegrana, L. Giannessi et al., Tracking attosecond electronic coherences using phase-manipulated extreme ultraviolet pulses, Nature Commun. 11, 883 (2020).

[39] I. Makos, I. Orfanos, A. Nayak, J. Peschel, B. Major, I. Liontos, E. Skantzakis, N. Papadakis, C. Kalpouzos, M. Dumergue et al., A 10-gigawatt attosecond source for non-linear XUV optics and XUV-pump-XUV-probe studies, Sci. Rep. 10, 3759 (2020).
 

# Resonant Self-Diffraction of Femtosecond Extreme Ultraviolet Pulses in Cobalt

Supplemental Material

Alexei A. Maznev, \( ^{1,*} \)  Wonseok Lee, \( ^{2} \)  Scott K. Cushing, \( ^{2}~ \)  Dario De Angelis, \( ^{3} \)  Danny Fainozzi, \( ^{3}~ \)  Laura Foglia, \( ^{3} \)  Christian Gutt, \( ^{4} \)  Nicolas Jaouen, \( ^{5,6} \)  Fabian Kammerbauer, \( ^{7} \)  Claudio Masciovecchio, \( ^{3} \)  Riccardo Mincigrucci, \( ^{3}~ \)  Keith A. Nelson, \( ^{1}~ \)  Ettore Paltanin, \( ^{3}~ \)  Jacopo Stefano Pelli-Cresi, \( ^{3} \)  Vincent Polewczyk, \( ^{8} \)  Dmitriy Ksenzov, \( ^{4} \)  Filippo Bencivenga. \( ^{3} \) 

 \( ^{1} \) Department of Chemistry, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA  
 \( ^{2} \) Division of Chemistry and Chemical Engineering, California Institute of Technology, California 91125, USA  
 \( ^{3} \) Elettra-Sincrotrone Trieste, SS 14 km 163,5 in AREA Science Park, 34149 Trieste, Italy  
 \( ^{4} \) Department Physik, Universität Siegen, Walter-Flex-Strasse 3, 57072 Siegen, Germany  
 \( ^{5} \) Synchrotron SOLEIL, L'Orme des Merisiers, Saint-Aubin, Gif-sur-Yvette Cedex, 91192, France  
 \( ^{6} \) Department of Molecular Sciences and Nanosystems, Ca' Foscari University of Venice, 30172 Venezia, Italy  
 \( ^{7} \) Institute of Physics, Johannes Gutenberg University Mainz, 55099 Mainz, Germany  
 \( ^{8} \) Université Paris-Saclay, UVSQ, CNRS, GEMaC, 78000, Versailles, France  
 \( ^{*} \) Corresponding author: alexei.maznev@gmail.com

## CONTENTS

S1. Electronic structure calculations for hcp cobalt 1
S2. Chemical potential calculations 2
S3. Complex refractive index at varying  \( T_{e} \)  3

## S1. Electronic structure calculations for hcp cobalt

The electronic density of states (DOS) of cobalt (Co) is calculated within density functional theory (DFT) using Quantum ESPRESSO version 7.0 [1, 2]. Co adopts a hcp structure at ambient conditions with lattice constants of  \( a = 4.736 \)  Bohr and  \( c = 7.693 \)  Bohr [3]. A kinetic energy cutoff of 100 Ry is applied for the plane-wave expansion of the Kohn-Sham wavefunctions. The calculations use a norm-conserving Troullier-Martins pseudopotential [4] with the Perdew-Burke-Ernzerhof generalized gradient approximation exchange-correlation functional [5]. The integration of the Brillouin zone is performed using a  \( 12 \times 12 \times 6 \)  Monkhorst-Pack (MP) k-point grid [6], and Gaussian smearing is employed to accelerate self-consistent field convergence. The electronic DOS is computed with a 0.1 eV energy grid step. As shown in Fig. S1, the spin-up DOS is below the Fermi level  \( E_{F} \) , with the d-band electrons being occupied, while the spin-down DOS cuts through  \( E_{F} \) . These results are consistent with previous computational studies on hcp Co [7, 8].
 
![](./images/1129109319594278931_6.jpg)

FIG. S1. Spin-polarized electronic DOS of hcp Co.

## S2. Chemical potential calculations

Given that the total number of valence electrons N is conserved at any electronic temperature  \( T_{e} \) , the chemical potential  \( \mu(T_{e}) \)  is determined by integrating the product of the Fermi-Dirac distribution function,  \( f(E, \mu(T_{e}), T_{e}) = \{\exp[(E - \mu(T_{e}))/(k_{B}T_{e})] + 1\}^{-1} \)  with Boltzmann constant  \( k_{B} \) , and the total electronic DOS of Co,  \( g(E) \) , over all energies [9, 10]:

 \[ N=\int_{-\infty}^{\infty}f(E,E_{F},T_{e}=0\mathrm{~K})g(E)d E=\int_{-\infty}^{\infty}f(E,\mu(T_{e}),T_{e})g(E)d E. \quad (1) \] 

Co has  \( 3d^{7}4s^{2} \)  valence electrons and exhibits a high electronic DOS near the Fermi level, as illustrated in Fig. S1. This high DOS allows the excitation of d-band electrons at the energy levels around the Fermi energy, which results in an increase in the chemical potential as  \( T_{e} \)  increases, as shown in Fig. S2.
 
![](./images/1129109319594278931_7.jpg)

FIG. S2. Chemical potential of Co as a function of the electronic temperature.

## S3. Complex refractive index at varying  \( T_{e} \) 

Calculations of the complex refractive indices near the Co  \( M_{2,3} \)  edge at varying  \( T_{e} \)  are performed using the Obtaining Core Excitations from the Ab initio electronic structure and the NIST Bethe-Salpeter equation (BSE) solver (OCEAN) version 3.0.3 [11, 12]. The code first calculates the ground-state electronic structure of Co within plane-wave DFT framework using Quantum ESPRESSO and subsequently computes the complex dielectric function within the BSE approach to account for excitonic effects. For consistency, the same pseudopotential, kinetic energy cutoff, and lattice constants are used in both the DFT and BSE calculations. The MP k-point grids employed are  \( 10 \times 10 \times 1 \)  for the ground state,  \( 16 \times 16 \times 1 \)  for the final state, and  \( 4 \times 4 \times 1 \)  for screening calculations. The number of bands for the final-state and screening wavefunctions is set to 100, and a scaling factor of 0.8 is used for the Slater integrals, which is typical for 3d transition metals [13]. The electron-hole occupation number differences in the BSE Hamiltonian are determined by the Fermi-Dirac distribution function, with chemical potentials dependent on  \( T_{e} \) . The resulting dielectric functions are broadened using a convolution of a Lorentzian function with a FWHM of 0.3 eV. Finally, the complex dielectric function  \( \epsilon = \epsilon_{1} + i\epsilon_{2} \)  is converted into the complex refractive index  \( \tilde{n} = 1 - \delta + i\beta \)  by using  \( 1 - \delta = \left\{\left[(\epsilon_{1}^{2} + \epsilon_{2}^{2})^{1/2} + \epsilon_1\right]/2\right\}^{1/2} \)  and  \( \beta = \left\{\left[(\epsilon_{1}^{2} + \epsilon_{2}^{2})^{1/2} - \epsilon_1\right]/2\right\}^{1/2} \) . Figure S3 illustrates the experimental and calculated complex refractive indices of Co. While the calculations do not as accurately reproduce the experimental complex refractive index, the spectral differences due to photoexcitation is accurately reproduced as proven in previous studies [14, 15]. Figure S4 demonstrates that the differences in  \( \delta \)  and  \( \beta \)  resulting from a 100 K increase in  \( T_{e} \)  are most pronounced near the Co  \( M_{2,3} \)  edge, where they contribute to the most intense signal in the self-diffraction spectrum.
 
![](./images/1129109319594278931_8.jpg)

![](./images/1129109319594278931_9.jpg)

FIG. S3. (a) Real and (b) imaginary parts of the complex refractive index of Co, as obtained from [16] (blue) and from calculations (black).

![](./images/1129109319594278931_10.jpg)

FIG. S4.  \( \Delta\delta \)  (red) and  \( \Delta\beta \)  (blue) at an electronic temperature rise of 100 K from 300 K to 400 K.

## References

[1] P. Giannozzi et al., Advanced capabilities for materials modelling with Quantum ESPRESSO, J. Phys.: Condens. Matter 29, 465901 (2017).

[2] P. Giannozzi et al., QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter 21, 395502 (2009).

[3] L. J. E. Hofer and W. C. Peebles, Preparation and X-Ray Diffraction Studies of a New Cobalt Carbide, J. Am. Chem. Soc. 69, 893 (1947).
 

[4] N. Troullier and J. L. Martins, Efficient pseudopotentials for plane-wave calculations, Phys. Rev. B 43, 1993 (1991).

[5] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[6] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13, 5188 (1976).

[7] S. F. Matar, A. Houari, and M. A. Belkhir, Ab initio studies of magnetic properties of cobalt and tetracobalt nitride  \( Co_{4}N \) , Phys. Rev. B 75, 245109 (2007).

[8] J. P. Rueff, R. M. Galéra, Ch. Giorgetti, E. Dartyge, Ch. Brouder, and M. Alouani, Rare-earth contributions to the x-ray magnetic circular dichroism at the Co K edge in rare-earth–cobalt compounds investigated by multiple-scattering calculations, Phys. Rev. B 58, 12271 (1998).

[9] N. W. Ashcroft and N. D. Mermin, Solid State Physics (Holt, Rinehart, and Winston, New York, 1976).

[10] Z. Lin, L. V. Zhigilei, and V. Celli, Electron-phonon coupling and electron heat capacity of metals under conditions of strong electron-phonon nonequilibrium, Phys. Rev. B 77, 075133 (2008).

[11] J. Vinson, Advances in the OCEAN-3 spectroscopy package, Phys. Chem. Chem. Phys. 24, 12787 (2022).

[12] J. Vinson, J. J. Rehr, J. J. Kas, and E. L. Shirley, Bethe-Salpeter equation calculations of core excitation spectra, Phys. Rev. B 83, 115106 (2011).

[13] F. de Groot and A. Kotani, Core Level Spectroscopy of Solids, Advances in Condensed Matter Science (Taylor & Francis Group, London, 2008).

[14] I. M. Klein, A. Krotz, W. Lee, J. M. Michelsen, and S. K. Cushing, Ab initio calculations of XUV ground and excited states for first-row transition metal oxides, J. Phys. Chem. C 127, 1077 (2023).

[15] H. Liu, J. M. Michelsen, J. L. Mendes, I. M. Klein, S. R. Bauers, J. M. Evans, A. Zakutayev, and S. K. Cushing, Measuring Photoexcited Electron and Hole Dynamics in ZnTe and Modeling Excited State Core-Valence Effects in Transient Extreme Ultraviolet Reflection Spectroscopy, J. Phys. Chem. Lett. 14, 2106 (2023).

[16] Q. Saadeh et al., On the optical constants of cobalt in the M-absorption edge region, Optik 273, 170455 (2023).
 
