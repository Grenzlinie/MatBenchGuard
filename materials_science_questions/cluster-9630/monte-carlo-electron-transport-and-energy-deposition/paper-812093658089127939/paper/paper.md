Original Paper

# Quantitative X-Ray Microanalysis of Heterogeneous Materials Using Monte Carlo Simulations

Raynald Gauvin*

Department of Mining, Metals and Materials Engineering, McGill University, Montréal, Québec H3A 2B2, Canada

Received May 26, 2005; accepted October 11, 2005; published online May 4, 2006
© Springer-Verlag 2006

**Abstract.** Monte Carlo simulations are used to obtain new results of x-ray microanalysis of sample types frequently encountered in practical analytical situations such as a vertical layer embedded in a homogeneous matrix and a spherical particulate deposited on a substrate. The simulations show that a 10-nm layer of boron in a steel matrix can be imaged using backscattered electrons and detected using x-ray microanalysis with a field emission scanning electron microscope even with an electron beam energy equals to 20 keV and also that these simulations can be useful to estimate the optimum acceleration voltage to perform such analyses. For a carbon spherical particulate located on the top of a gold substrate, it is shown that x-ray emission and electron backscattering are a strong function of the diameter of the particulate and also of the electron beam energy. Finally, a new method to determine the thickness of a thin film deposited on a substrate is proposed that does not require the measurement of the beam current. That technique can also be used for a spherical particulate deposited on a substrate.

**Key words:** X-ray microanalysis; Monte Carlo; scanning electron microscopy; energy dispersive spectrometry; electron scattering.

Quantitative x-ray microanalysis was first developed to analyze flat homogeneous samples with the analytical volume containing both the x-ray source and the path of the generated x-rays to the sample surface. The schemes to convert x-ray intensity to composition for this class of samples, still in use today, are based either on the ZAF or the $\varphi(\rho z)$ methods [1]. However, these approaches do not apply to all real world samples and a great deal of attention has been and is still being given to those samples where the flat homogeneous models cannot be used. For example, quantitative schemes have been developed the determination of the composition and thickness of multilayered specimens [2, 3] and they were extended for the quantitative microanalysis of spherical inclusions embedded in a matrix [4, 5]. Monte Carlo simulations have also shown that they could be useful to improve the accuracy of quantitative x-ray microanalysis of rough surfaces [6].

It becomes obvious that Monte Carlo simulations of electron scattering in solids are the tools of choice to develop quantitative schemes to perform x-ray microanalysis of real materials, especially with the current speed of actual computers. In this paper, results obtained with the Monte Carlo free commercial software Casino [7] are presented to show how useful this software can be to perform x-ray microanalysis of boron segregation to a steel grain boundary. Results

* E-mail: raynald.gauvin@mcgill.ca

of x-ray emission and electron backscattering ob- tained with a new Monte Carlo program under devel- opment for a spherical carbon particulate deposited on a gold substrate are also presented. Finally, a new method to determine the thickness of a thin film deposited on a substrate is presented that does not require the measurement of the specimen current since it is based on the ratio of the x-rays emitted simultaneously by the thin film and the substrate. The advantage of that method is that it could be used with a cold field emission scanning electron micro- scope where current stability might be an issue when pure elements standards are used to determine specimen thickness using the classical schemes [4, 5]. Casino and the new Monte Carlo program Win X-Ray [8], that simulates the complete x-ray spec- trum of a homogeneous bulk specimen and also includes a charging model for a non conductive specimen, can be downloaded for free at http:// www.montecarlomodeling.mcgill.ca/.

The Monte Carlo simulations used in this work are based on the single scattering model and are described extensively in the papers describing Casino and Win X-Ray [7, 8]. Between elastic collisions, energy loss is computed using the continuous energy loss of Bethe that was modified for better performances below 1 keV. Elastic cross sections of Mott are used for elastic scattering. At each elastic collision, the polar and azimuthal angles of collisions are computed, the polar with the partial elastic cross sections and the azimuthal being uniformly distributed between 0 and $2\pi$. In the computation of x-rays, ionization cross sections of Casnati are used and x-ray absorption is taken into account for any geometry. Fluorescence effects are not considered in this work even if this effect might be significant near interfaces of different materials.

## Simulation of Boron Segregation in 1080 Steel

CASINO was used to simulate the variation of the BSE coefficient, $\eta$, and of the boron $K_{\alpha}$ line on a line scan for a 1080 steel specimen (simulated here with 0.8 wt% C and balance Fe) having a 10 nm vertical layer of boron that simulates grain boundary segrega- tion. These simulations were performed for various electron beam energy $(E_{0})$ with a beam diameter of 10 nm and 5000 electron trajectories were computed for each of the 50 beam locations of a 100 nm line scan. Fig. 1a shows the variation of $\eta$ with the beam position. Clearly, the boron layer should be visible at all $E_{0}$ when imaged with the compositional mode with backscattered electrons using a field emission scan- ning electron microscope. With the minimum and maximum values of the backscattering coefficient of a line scan, $\eta_{min}$ and $\eta_{max}$, the contrast in % can be computed with this equation:

$$
C(\%)=\frac{\eta_{\max }-\eta_{\min }}{\eta_{\max }+\eta_{\min }} \tag{1}
$$

![](./images/812093658089127939_1.jpg)

Fig. 1. (a) Variation of the electron backscattering coefficient, $\eta$, with the electron beam position for a 10 nm boron vertical layer embedded in a 1080 steel (0.8 wt% C, balance Fe) for various incident electron energies. The beam diameter was set to 10 nm. (b) Variation of the contrast of the electron backscattered images versus the electron beam energy; $E_{0}$ computed using Eq. (1) and the data shown in (a)

Figure 1b shows the computed contrast as a function of $E_{0}$ using Eq. (1) and the line scans of Fig. 1a. The contrast decreases with $E_{0}$ owing to the increase of the interaction volume with the incident electron beam energy. However, a contrast of 30% is predicted at 20 keV, which is pretty high and should allow the visibility of such a small layer. Figure 2a shows the variation of the intensity of the boron $K_{\alpha}$ line with the beam position. The intensity given in this figure and all the following figures are in counts. Clearly, even with beam energy of 20 keV, a 10 nm boron layer can be detected with a beam diameter of 10 nm. Figure 2b shows the variation of the intensity of the boron $K_{\alpha}$ line when the beam is located at the center of the boron layer as a function of $E_{0}$ for two cases, same beam current, which is the results obtained with

![](./images/812093658089127939_2.jpg)

Fig. 2. (a) Variation of the net intensity of the boron $K_{\alpha}$ line with the electron beam position for a 10 nm boron vertical layer embedded in a 1080 steel (0.8 wt% C, balance Fe) for various incident electron energies. The beam diameter was set to 10 nm. (b) Variation of the intensity of the B $K_{\alpha}$ line when the beam is located at the center of the boron layer as a function of $E_{0}$ computed with the data shown in (a)

the same number of simulated electrons in the simulations, and the real situation that accounts for the linear variation of the gun brightness with $E_{0}$ [1]. This latter curve was obtained by scaling the curve having the same current by the factor $E_{0}/20$. In order to obtain the real variation of the boron intensity with $E_{0}$, we have to scale to this factor because the beam diameter was kept constant in the simulations. Therefore, 20 keV would be the condition that would maximize the B $K_{\alpha}$ line count rate.

It is quite impressive that these simulations predicts that even at 20 keV, a 10 nm boron layer should be seen in these conditions, considering that the electron range is about $1.3\ \mu$m for a 1080 steel. Figure 3 shows the electrons trajectories simulated at 1 and 20 keV using Casino when the electron beam is located at the center of the boron layer. At 1 keV, the small electron range (about 20 nm) and the beam diameter of 10 nm easily explain the boron detectability. At 20 keV, it is clear that even for a quite larger electron range, a beam diameter of the same size as the layer is sufficient to give a detectability for boron because being a light element, its mean free path between elastic collisions is larger than iron and also its elastic angle of collision is smaller, then the electron trajectories in boron are almost straight lines and they travel significantly in that layer. Therefore, there is a kind of electron channeling in the boron layer that explain its detectability at 20 keV and it is clear that Monte Carlo simulations are very useful to understand the electron scattering for these specimen geometries.

## Proposal of a New Method for Thickness Determination of a Thin Film on a Substrate

The determination of the thickness of a thin film deposited on the substrate is based on the measurement of the classical K ratio of the element of the coating that is given by this equation [1]:
$$
\mathrm{K}=\frac{\mathrm{I}_{\mathrm{f}}}{\mathrm{I}_{\mathrm{s}}} \tag{2}
$$
where $I_{f}$ is the intensity emitted by the element of the thin film on the substrate and $I_{s}$ is the intensity emitted by the same element on a standard of known composition, generally a bulk specimen of that pure element. Here the case of a single element thin film is considered. This method can be generalized for the cases of this films having more than one element [2] and also for the case of complex multilayers structures made of several alloys [3]. The simplest case is therefore the case of a thin film having a single element that is deposited on a substrate and Monte Carlo simulations are the technique of choice for computing a calibration curve relating the K ratio of the element of the thin film as a function of its thickness for a specific beam energy.

As an example of this technique, Fig. 4a shows the net intensity of the carbon $K_{\alpha}$ line as a function of the thickness of a carbon thin film, t, deposited on a gold substrate for $E_{0}$ equal to 4, 5 and 6 keV. Figure 4b shows the corresponding net intensity of the gold $M_{\alpha}$ line as a function of the thickness of a carbon thin film. These simulations were performed with Casino using 10 000 electron trajectories. For the carbon $K_{\alpha}$ line, the intensity increases with the thickness of the film until it saturates to a constant value above the electron range for that beam energy. As $E_{0}$ increases, the thickness where the intensity saturates increases as

![](./images/812093658089127939_3.jpg)

![](./images/812093658089127939_4.jpg)

Fig. 3. Plot of electron trajectories simulated at 1 and 20 keV using Casino when the electron beam is located at the center of the boron layer.
(a) 1 keV and (b) 20 keV

well since the electron range increases with the electron beam energy. Of course, the reverse is seen for the gold $M_\alpha$ line as a function of the thickness of a carbon thin film since, as the thickness of the carbon film increases, the electrons travel less in gold and the emitted intensity decreases. Above a certain thickness, equals to the electron range in carbon, the gold intensity equals zero and that critical thickness, which is the same seen in Fig. 4a, increases with $E_0$. Figure 5a shows the K ratio of the carbon $K_\alpha$ line as a function

![](./images/812093658089127939_5.jpg)

Fig. 4. (a) Net intensity of the carbon $K_{\alpha}$ line as a function of the thickness of a carbon thin film, t, deposited on a gold substrate for $E_{0}$ equal to 4, 5 and 6keV. (b) Net intensity of the gold $M_{\alpha}$ line as function of t in the same conditions used in (a)

![](./images/812093658089127939_6.jpg)

Fig. 5. (a) K ratio of the carbon $K_{\alpha}$ line as a function of the thickness of a carbon thin film, t, deposited on a gold substrate for $E_{0}$ equal to 4, 5 and 6keV. (b) R ratio given by $ICK_{\alpha}/(ICK_{\alpha}+IAuM_{\alpha})$ as a function of t in the same conditions used in (a)

of the thickness of a carbon thin film computed with the data of Figs. 7 and 8 and also with Monte Carlo simulation of a bulk specimen of graphite for the same $E_{0}$ (4, 5 and 6keV). These curves are the calibration curves that can be used to determine the thickness of the carbon coating from the measurement of the carbon K ratio at a given beam energy.

In order to perform experimentally such a measurement, all the experimental conditions must be similar and constant when the x-ray intensities are measured for the thin film as well as from the standard and the beam current must be determined using a Faraday cup. In the case of cold field emission scanning electron microscopes, the beam current fluctuate during time [1], making the precise requirement of a constant beam current difficult. Since these microscopes have the best resolution below 5keV owing to a smaller chromatic aberration due to the smaller energy spread of incident electrons, it is obvious that the development of a new method to determine the specimen thickness without measuring the beam current would be advantageous.

In that regards, a calibration curve should be constructed with a new ratio method that was developed for quantitative x-ray microanalysis of materials in the cold field emission electron microscope [9]. This ratio is obtained from the measured spectrum of the thin film deposited on the substrate:

$$
\mathrm{R}=\frac{\mathrm{I}_{\mathrm{f}}}{\mathrm{I}_{\mathrm{f}}+\mathrm{I}_{\mathrm{sb}}} \tag{3}
$$

where $\mathrm{I}_{\mathrm{f}}$ is, as before, the intensity emitted by the element of the thin film and $\mathrm{I}_{\mathrm{sb}}$ is the intensity emitted by the substrate. The great advantage on the ratio given by Eq. (3) is that the specimen current does not need to be known since it is the same for both intensities. The drawback is that to compute the x-ray intensities, accurate knowledge of the fundamental parameters, like the ionization cross sections and the fluorescence yields, to name a few, and also the detec-

tor efficiency must be known since they do not cancel out with this ratio, which is the case with the K ratio defined in Eq. (2) since the same element is present in the numerator and the denominator. However, it is possible to find a homogeneous material having these two elements and to determine the corresponding cor- rection factor. If a homogeneous alloy can not be obtained, the thickness of the thin film could be deter- mined using another technique (the electron micro- probe is certainly one of these) in order to determine the calibration factor. Once the calibration factor is known, several coatings of the same system could then be analyzed using a cold field emission scanning electron microscope. It may be argued why to use a cold field emission scanning electron microscope when the electron microprobe can be used. The answer it that a cold field emission scanning electron gives the best image resolution below $5\,\text{keV}$ and therefore, with that technique high resolution imaging and high spatial resolution microanalysis can be per- formed which is not the case for the electron micro- probe yet. Of course, that ratio method can be applied to any kind of scanning electron microscopes. Figure 5b shows the calibration curves of R versus the thick- ness of a carbon film deposited on a gold substrate at4, 5 and $6\,\text{keV}$ that were computed with the data of Fig. 4. Clearly, similar curves as these shown in Fig. 5a are obtained and the proposed method based on the R ratio should work with the knowledge of the proper calibration factor.

## Simulation of X-Ray Emission and Electron Backscattering from a Spherical Particulate on a Substrate

A new Monte Carlo program is under development to simulate x-ray emission and electron backscattering from a spherical particulate on a substrate. The Monte Carlo modeling is similar to that used in the Casino and Win X-Ray programs [7, 8]. Figure 6 shows the geometry used to simulate a spherical particulate on a substrate where $D$ is the sphere diameter. Simulations

![](./images/812093658089127939_7.jpg)

Fig. 6. Geometry used to simulate a spherical particulate on a substrate. $D$ is the sphere diameter

![](./images/812093658089127939_8.jpg)

Fig. 7. (a) Variation of the electron backscattering coefficient, $\eta$, as a function of $D$ for a carbon spherical particulate deposited on a gold substrate for $E_0$ equal to 1, 2, 5, 10 and $20\,\text{keV}$. (b) Net intensity of the carbon $K_\alpha$ line as a function of $D$ in the same conditions used in (a)

were performed for a carbon particulate deposited on a gold substrate. 10 000 electron trajectories were simu- lated and the beam diameter was fixed to $10\,\text{nm}$. Simulations were performed for $D$ ranging from 1 to $1000\,\text{nm}$ and for $E_0$ between 1 and $20\,\text{keV}$. In these simulations, the detector was located normal to the particulate shown in Fig. 6 with a take off angle of $40^\circ$. The electron beam was always located at the top of the particulate.

Figure 7a shows the variation of the electron back- scattering coefficient, $\eta$, as a function of $D$ for $E_0$ equal to 1, 2, 5, 10 and $20\,\text{keV}$. Clearly, for a given energy smaller than $10\,\text{keV}$, the variation of $D$ has a strong effect on the backscattering coefficient. As a result, two carbon particulate with a different $D$ will give a different contrast that is not chemical but topo- graphical. Care must therefore be taken to interpret the contrast of small particulates of different sizes observed in the backscattered electron mode. The value of $\eta$ versus $D$ is almost constant for $E_0$ equals

![](./images/812093658089127939_9.jpg)

Fig. 8. R ratio given by $ICK_{\alpha}/(ICK_{\alpha} + IAuM_{\alpha})$ as a function of $D$ for a carbon spherical particulate deposited on a gold substrate for $E_0$ equal to 4, 5 and 6 keV

to 10 and 20 keV, the spheres are too small to affect significantly the value of $\eta$ that is mainly dominated by gold. For smaller electron beam energies, the value of $\eta$ increases with $D$, goes to a maximum value and then decay to the value of pure carbon when $D$ is significantly greater that the electron range in bulk carbon. The corresponding value of $D$ associated with the maximum value of $\eta$ increases with $E_0$, consistently with the increase of the electron range with beam energy.

Figure 7b shows the net intensity of the carbon $K_{\alpha}$ line as a function of $D$ for $E_0$ equal to 1, 2, 5, 10 and 20 keV. The carbon intensity increases with $D$, goes to a maximum and then decays to a constant value equals to that of bulk carbon at a given $E_0$. Clearly, the behavior is different to that of a thin film of C deposited on gold, as shown in Fig. 4a where a monotonic increase, up to a plateau, of carbon x-ray intensity with specimen thickness is observed. Figure 8 shows the R ratio as a function of $D$ for a carbon spherical particulate deposited on a gold substrate for $E_0$ equal to 4, 5 and 6 keV. Clearly, despite the differences of x-ray variation with $D$ for a particulate instead of a thin film deposited on gold, a monotonic increase is observed and this indicates that the R ratio could be used to determine the diameter of a spherical particulate deposited on a substrate.

## Conclusions

This paper has shown how useful are Monte Carlo simulations of electron scattering in heterogeneous materials in order to understand electron backscattering and x-ray emission. This allows figuring out the contrast of BSE images as a function of geometrical parameters, to find experimental conditions to optimize the characterization of these materials and to perform quantitative x-ray microanalysis. A new method to determine the thickness of thin film deposited on a substrate was also proposed. That method is based on the ratio of intensities of elements of the thin film and the substrate obtained from the same x-ray spectrum, eliminating the measurement of the specimen current. This is a great advantage for cold field scanning electron microscopes that do have specimen current fluctuations. However, an experimental calibration using a reference standard can be needed. This new method should also work for the determination of the diameter of a spherical particulate deposited on a substrate.

## References

[1] Goldstein J I, Newbury D E, Echlin P, Joy D C, Romig A D, Lyman C E, Fiori C, Lifshin E (1992) Scanning electron microscopy and microanalysis. Plenum Press, New York
[2] Kyser D F, Murata K (1974) IBM J Res Develop 18: 352
[3] Pouchou J-L (2002) Microchim Acta 138: 133
[4] Gauvin R, L'Espérance G, St-Laurent S (1992) Scanning 14: 37
[5] Gauvin R, Hovington P, Drouin D (1995) Scanning 17: 202
[6] Gauvin R, Lifshin E (2004) Microchim Acta 145: 41
[7] Hovington P, Drouin D, Gauvin R (1997) Scanning 19: 1
[8] Gauvin R, Lifshin E, Demers H, Horny P, Campbell H (2006) Microsc Microanal 12: 49
[9] Horny P, Gauvin R, Lifshin E (2005) A new method for quantitative microanalysis with a scanning electron microscope (these proceedings)