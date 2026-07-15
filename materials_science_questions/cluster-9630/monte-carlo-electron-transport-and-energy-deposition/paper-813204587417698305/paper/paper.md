# Simulation of background from low-level tritium and radon emanation in the KATRIN spectrometers

B. Leiber for the KATRIN Collaboration

Institute for Nuclear Physics (IKP), Karlsruhe Institute of Technology (KIT), 76021 Karlsruhe, Germany

**Abstract.** The KArlsruhe TRItium Neutrino (KATRIN) experiment is a large-scale experiment for the model independent determination of the mass of electron anti-neutrinos with a sensitivity of 200 meV/$c^2$. It investigates the kinematics of electrons from tritium beta decay close to the endpoint of the energy spectrum at 18.6 keV. To achieve a good signal to background ratio at the endpoint, a low background rate below $10^{-2}$ counts per second is required. The KATRIN setup thus consists of a high luminosity windowless gaseous tritium source (WGTS), a magnetic electron transport system with differential and cryogenic pumping for tritium retention, and electro-static retarding spectrometers (pre-spectrometer and main spectrometer) for energy analysis, followed by a segmented detector system for counting transmitted beta-electrons.

A major source of background comes from magnetically trapped electrons in the main spectrometer (vacuum vessel: 1240 m$^3$, $10^{-11}$ mbar) produced by nuclear decays in the magnetic flux tube of the spectrometer. Major contributions are expected from short-lived radon isotopes and tritium. Primary electrons, originating from these decays, can be trapped for hours, until having lost almost all their energy through inelastic scattering on residual gas particles. Depending on the initial energy of the primary electron, up to hundreds of low energetic secondary electrons can be produced. Leaving the spectrometer, these electrons will contribute to the background rate.

This contribution describes results from simulations for the various background sources. Decays of $^{219}$Rn, emanating from the main vacuum pump, and tritium from the WGTS that reaches the spectrometers are expected to account for most of the background. As a result of the radon alpha decay, electrons are emitted through various processes, such as shake-off, internal conversion and the Auger deexcitations.

The corresponding simulations were done using the KASSIOPEIA framework, which has been developed for the KATRIN experiment for low-energy electron tracking, field calculation and detector simulation. The results of the simulations have been used to optimize the design parameters of the vacuum system with regard to radon emanation and tritium pumping, in order to reach the stringent requirements of the neutrino mass measurement.

**Keywords:** radon emanation, MAC-E filter, neutrino mass, KATRIN
**PACS:** 23.40.Bw, 14.60.Pq, 29.30.-h

# BACKGROUND ARISING FROM NUCLEAR DECAYS

Nuclear decays in the spectrometer section of the KATRIN experiment [1] can produce primary electrons from a few eV up to the multi-keV scale which are stored in the spectrometers [2, 3]. Because of the good vacuum conditions, these high-energy primaries are stored for a long time period so that they can produce low-energy secondaries through residual gas ionization that reach the detector. In the following, the basic constituents of the background production mechanism will be outlined.

## Nuclear decays as source of high-energy electrons

Tritium $\beta$-decays and $\alpha$-decays of the short lived radon isotopes $^{219,220}$Rn are a main source of keV-range electrons in the spectrometers. The KATRIN design parameters [4] require that only an exceedingly small fraction of the order of $10^{-14}$ of the tritium that is injected into the WGTS will reach the spectrometer section. However a small number of these molecules will decay inside the spectrometers before being pumped out, thereby producing electrons with a continuous energy spectrum up to 18.6 keV.

Electrons with similar and even higher energies can be produced during $\alpha$-decays of radon isotopes. Due to the presence of turbomolecular pumps offering a high pumping speed and correspondingly short pumping times (6 min), only the $\alpha$d-ecays of the short-lived radon isotopes $^{219,220}$Rn ( $t_{1/2}$ =3.96 s, 55.6 s ) will act as a source of these electrons.

The isotope $^{219}$Rn arises from the $^{235}$U actinide decay chain. It can emanate in small quantities from the non-

Low Radioactivity Techniques 2013 (LRT 2013)
AIP Conf. Proc. 1549, 243-247 (2013); doi: 10.1063/1.4818118
© 2013 AIP Publishing LLC 978-0-7354-1174-6/$30.00

![](./images/813204587417698305_1.jpg)

FIGURE 1. Energy-spectrum of electrons accompanying a $^{219}$Rn-$\alpha$-decay. For more details of the simulation see [7]

evaporative getter (NEG) material that is used to pump the KATRIN spectrometers [5, 6]. The $^{220}$Rn isotope is created in the $^{232}$Th decay chain. It emanates from the stainless steel inner surfaces of the spectrometers as well as from components like ceramic insulators, glass windows, vacuum gauges and thermocouples.

There exist several processes following the $\alpha$-decays of $^{219,220}$Rn that generate electrons [2, 7, 8]:

**inner conversion** $^{219,220}$Rn decays into excited $^{215,216}$Po* levels will result in the emission of $\gamma$-rays or a conversion electron with energies up to 450 keV.

**shake-off** The emitted $\alpha$-particles can directly knock out electrons from the atomic shells. These electrons can have energies up to 80 keV .

**shell reorganization** The emission of an $\alpha$-particle results in a sudden change of nuclear potential. This leads to the emission of low-energy shell reorganization electrons from the outer shells. They usually share an energy of about 250 eV.

**Auger electrons** Shake-off and conversion processes both leave vacancies in the electron shell. This leads to a cascade of relaxations, releasing multiple Auger electrons with energies up to 20 keV.

These processes result in rather complex energy spectra and high multiplicity values of electrons accompanying the $\alpha$-decays. An example of a simulated spectrum for $^{219}$Rn is shown in figure 1. The simulated electron multiplicities are in good agreement with measurements from an independent work.

## Magnetic mirror trap created by MAC-E filters

Due to the MAC-E filter concept used in KATRIN to scan the $\beta$-spectrum, an electron created in the center of a spectrometer (where the magnetic field is relatively low) will be trapped in the magnetic bottle formed by the regions of high magnetic field at its ends. As a result, the longitudinal (axial) energy of the electron $E$ is transformed into transversal (gyration) energy $E_{\perp}$. Depending on the starting polar angle of the electron to the magnetic field (or energy of the electron), the kinetic energy can be completely transformed into transversal energy, so that the electron is magnetically trapped.

## Background production of stored electrons

A primary high-energy electron which is trapped inside the magnetic bottle of the spectrometer will slowly cool down via ionization and electronic excitation collisions off residual gas molecules. Energy loss through elastic scattering and emission of synchrotron radiation play a minor role for electrons in the keV-range in low magnetic

fields (<1mT). Due to the ultra high vacuum (UHV, p=$10^{-11}$ mbar) conditions inside the KATRIN main spectrometer, collisions are rare, allowing a single electron to be stored for hours. In this timespan, hundreds of low-energy secondary electrons can be created by ionization collisions. These secondaries can leave the spectrometer on a rather short timescale of minutes. They are accelerated towards the detector by the retarding potential and thus produce background in the narrow energy region-of-interest of the signal-$\beta$-decay electrons.

# SIMULATION OF STORED ELECTRONS

In order to quantify the expected background caused by nuclear decays and to optimize the vacuum setup with respect to this background, extensive calculations were performed. These include the emanation rates of different materials, primary and secondary electron spectra and Monte-Carlo tracking of stored electrons taking into account synchrotron radiation and scattering off residual gas molecules.

## MC simulations

To better understand the process of background creation through stored electrons and its implications, extensive simulations were carried out using the KASSIOPEIA software package. The main parameters investigated in these simulation were the storage time $t_s$ of a primary particle and the number of created secondary particles $N_{sec}$, as a function of the primary's start energy $E_{prim}$. For a realistic calculation, effects like synchrotron radiation, elastic and inelastic scattering and non-adiabatic effects had to be taken into account. The simulations reveal a correlation of both background parameters with $E_{prim}$. A higher $E_{prim}$ implies a longer storage time ( up to 10 h) and higher multiplicity of secondary electrons. For example, a 10 keV primary electron will be stored for 3 h. In this timespan it produces ~300 secondaries, corresponding to a background rate of about $3{\cdot}10^{-2}$ cps.

## Activity calculations

During tritium-measurements non-vanishing amounts of tritiated molecules (HT) will reach the spectrometer sec- tion. If the tritium $\beta$-decay happens in the spectrometers, the decay electron will be trapped and also produce up to hundreds of secondary electrons that reach the detector. To mitigate this, the KATRIN pumping setup features 3000 m of NEG strips in the main spectrometer and up to 1000 m of NEG strips in the pre-spectrometer. The strips dra- matically increase the pumping speed for hydrogen which results in a much lower tritium partial pressure and thereby reduces the tritium-$\beta$-activity by three orders of magnitude.
Measurements at the KATRIN pre-spectrometer [5] have shown that the NEG strips themselves will introduce a sub- stantial background as they are emanating the short-lived radon isotope $^{219}$Rn. There is also a non-negligible emanation of $^{219}$Rn and $^{220}$Rn from the inner surfaces of the spectrometers [2].
Calculations were done for different UHV-setups in order to minimize the activity of primary electrons and to optimize the trade-off between tritium pumping and radon emanation. As a result of these calculations the optimal setup was found to be 70 m of additional NEG strips in the pre-spectrometer and for the main spectrometer the radon will be shielded from the tank-volume by adding liquid-Nitrogen-cooled baffles to the pump-ports.

# IMPACT ON THE KATRIN EXPERIMENT

As simulations show, the radon emanation from the inner walls of the spectrometers and other structural materials used may easily exceed the reference background level by a factor of three, and potentially, in case of larger than expected emanation rates, the background level would be correspondingly larger. In addition, background caused by nuclear decays has a non-Poissonian nature, meaning that the fluctuations of the background-rate are determined by the number of stored primary electrons, which is small compared to the number of secondaries reaching the detector. Therefore the count-rate at the detector will show large fluctuations that are not Poisson-distributed. As a consequence, the variance is determined by the variance of the number of stored primaries arising from nuclear decays.
In order to investigate the impact of the background arising from stored electrons, a detailed model describing the

![](./images/813204587417698305_2.jpg)

FIGURE 2. Statistical neutrino mass sensitivity as a function of background rate for Poisson distributed background and for the background model including nuclear decays. The dashed lines indicate the statistical sensitivity reached with a Poisson-distributed background of 10 mHz (as stated in [4]) and with the estimated background level of 30 mHz arising from nuclear decays.

background as a function of time over the full three years measurement time of KATRIN was implemented. The model is based on the full MC simulations described in the section above. Figure 2 shows the statistical neutrino mass sensitivity at 90% confidence level as a function of the overall background rate (leaving all other contributions at their reference values). Here we compare a Poisson-distributed background (as used in the KATRIN design report [4]) to the new background model introduced in [2] including nuclear decays. It is evident that the statistical error increases significantly in case of a non-Poissonian background. This particular feature of nuclear decays necessitates the development of active background countermeasures to realize the full physics potential of KATRIN.

## CONCLUSION
Due to their inherent electromagnetic design features, the KATRIN spectrometers act as magnetic bottles for light charged particles. A primary electron in the multi-keV regime produced by a nuclear decay can thus be magnetically trapped over a time period of several hours during which it can produce several hundred secondary electrons.
In order to reduce the background due to nuclear decays, $LN_2$ cooled baffles have been put in front of the pump port, where the NEG strips are located. Further, some active background reduction techniques that include electric dipole fields, magnetic pulsing and stochastic heating through ECR [9] will be implemented in the experiment.

## ACKNOWLEDGMENTS
This work has been supported by the Bundesministerium für Bildung und Forschung (BMBF) with project number 05A08VK2 and the Deutsche Forschungsgemeinschaft (DFG) via Transregio 27 "Neutrinos and beyond".

## REFERENCES
1. G. Drexlin, V. Hannen, S. Mertens, and C. Weinheimer, *Advances in High Energy Physics* **2013**, 39 (2013).
2. S. Mertens, et al., *Astroparticle Physics* **41**, 52-62 (2013), ISSN 0927-6505.
3. F. Fränkle, *Background Investigations of the KATRIN Pre-Spectrometer*, Ph.D. thesis, Karlsruhe Institute of Technology (KIT) (2010).
4. KATRIN Design Report (FZKA Report 7090), Tech. rep., KIT (2004).
5. F. Fränkle, et al., *Astroparticle Physics* **35**, 128-134 (2011).

6. S. Görhardt, *Reduktion der durch Radon induzierten Untergrundprozesse in den KATRIN Spektrometern*, Master's thesis, Karlsruhe Institute of Technology (KIT) (2011).

7. N. Wandkowsky, et al. (2012), arXiv:1304.1379.

8. N. Wandkowsky, et al. (2013), arXiv:1304.1375.

9. S. Mertens, et al., *Journal of Instrumentation* 7, P08025 (2012).

Copyright of AIP Conference Proceedings is the property of American Institute of Physics and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.