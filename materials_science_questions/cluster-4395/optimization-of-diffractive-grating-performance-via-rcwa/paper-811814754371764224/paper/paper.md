# Resonant surface roughness interactions in planar superlenses

Mikkel Schøler *, Richard J. Blaikie

MacDiarmid Institute for Advanced Materials and Nanotechnology, Department of Electrical and Computer Engineering, University of Canterbury, Christchurch, New Zealand

---

## A R T I C L E  I N F O

**Article history:**
Received 14 September 2009
Received in revised form 7 December 2009
Accepted 8 December 2009
Available online 16 December 2009

**Keywords:**
Planar lens
Super lens
Near-field lithography
Super-resolution
Imaging
Surface roughness
Thin-film
Finite element method
Simulation

## A B S T R A C T

Simulations were performed to investigate how various spatial frequencies of surface roughness, in planar superlenses, affect superlens performance. Resonant behaviour was observed and increases between 110% and 267%, in image line-edge roughness (LER), were observed at the peaks relative to the average image LER observed outside these resonant frequencies. This investigation suggests that the position of these resonance peaks is dependent upon the periodic character of the object being imaged, implying that a resonant coupling between shadow mask features and surface roughness takes place. These results present additional considerations for future studies within the field of superlensing.

© 2009 Elsevier B.V. All rights reserved.

---

### 1. Introduction

The concept of using a 'superlens' made from negative-index or plasmonic materials for deep sub-wavelength imaging has attracted a great deal of attention since Pendry's proposal in 2000 [1], and the debate that ensued in the literature [2–5]. Experimentally, the principle of superlens enhanced evanescent near-field optical lithography (ENFOL) has been demonstrated using silver-dielectric superlenses [6–8], showing that such systems are able to project sub-diffraction information contained in the evanescent near-field significantly further than the conventional decay length for non-propagating radiation. However, results to date fall short of providing the performance of theoretical predictions [1]. One widely recognised, but poorly understood, variable in this equation is how surface roughness on the superlens interfaces impacts upon the imaging characteristics of such systems.

The superlens phenomenon, in metallo-dielectric stacks, is mediated by surface–plasmon polariton couplings, near the plasma frequency, and consequent cascading from interface to interface, a mechanism which is sensitive to the presence of surface roughness at the interfaces [9]. Hence the added versatility of superlens lithography comes with the price of increased vulnerability to noise, such as line-edge roughness (LER), in the resultant images, and careful control of the surface quality is required to mitigate this effect. In this paper it will be shown that, not only does the amplitude of the surface roughness affect superlens imaging performance [10], but that the spatial frequencies of the surface roughness profiles also have a considerable impact upon image LER due to resonance effects. This implies that grain-size control during the deposition of superlens layers is important.

### 2. Background

Using conventional physical vapour deposition (PVD) techniques it is possible to achieve surface roughness values, for silver thin-films, in the range of 0.7–1.0 nm root-mean-square (RMS) with relative ease. Strict control of all process parameters is necessary to maintain consistency in such depositions. As a consequence precise and consistent control of the surface roughness magnitude between depositions is not an easy task. Thus, performing consecutive superlens lithography experiments while varying the surface roughness, in a controlled manner, becomes difficult.

Finite element method (FEM) modelling provides an opportunity for analysing how surface roughness impacts upon superlens imaging performance by solving Maxwell's equations for the complex geometries involved in superlens imaging systems with realistic surface roughness profiles at the metallo-dielectric interfaces.

Initial investigations [10], performed through FEM simulations, showed a positive linear relationship between RMS surface roughness and line-edge roughness (LER $=3\sigma$) in the resulting images of

---

* Corresponding author. Tel.: +64 21 0243 6146.
E-mail addresses: msc113@student.canterbury.ac.nz (M. Schøler), blaikie@elec.canterbury.ac.nz (R.J. Blaikie).

0167-9317/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.mee.2009.12.027

100 nm half-pitch lines at a wavelength of 365 nm, with approximately 20 nm of LER per nanometre of RMS surface roughness on the superlens interfaces. Additionally, these simulations suggest that the performance witnessed in superlens experiments to date is inferior to what should ideally be achievable using silver thin-films with similar surface roughness values ($\approx 1$ nm RMS). These simulations were performed in two dimensions using idealised material parameters and real surface roughness profiles extracted using atomic force microscopy (AFM). Here we extend this FEM analysis to study the spatial-frequency dependence of the surface roughness effects.

## 3. Spatial frequency analysis
In order to investigate how different spatial frequencies, contained within a typical surface roughness profile, affect the LER, FEM simulations were performed for a single layer plasmonic superlens system, consisting of a 30-nm thick silver film sandwiched between two 15-nm thick spacer layers, illuminated at 365 nm, with sinusoidal surface roughness profiles introduced on both silver-dielectric interfaces, as shown in Fig. 1. A four-slit, 100 nm half-pitch grating made from a representative high-conductivity mask material ($\sigma = 3.774 \times 10^7$ S/m and $\epsilon_r = \mu_r = 1$) was used as the test object. Intensity profiles at the image plane, 60 nm beyond the object plane, were used to determine image quality. The superlens layer ($\epsilon_r = -1 - 0.2j$ and $\mu_r = 1$) was positioned symmetrically between the object and image planes. The spacer layers were given electromagnetic properties identical to free space ($\epsilon_r = \mu_r = 1$).

![](./images/811814754371764224_1.jpg)

Fig. 1. A schematic of the modelling domain, illustrating the position of the various elements and the unit axes for both the frame of reference and polarisation vectors. The modelling domain is $1.2\ \mu$m by $1.0\ \mu$m.

The details of the FEM simulation method, used in this investigation, have been described elsewhere [10]. Typically $\approx 350,000$ elements were used across the $1\ \mu$m $\times 1.2\ \mu$m modelling domain. Convergence tests were performed to ensure that this did not affect the accuracy of the results obtained. Perfectly matched layers (PMLs) were employed at the $x$-axis boundaries to ensure that end reflections did not affect the results either.

The period, $\Lambda$, of the sinusoidal roughness profiles was varied from 10 nm to $1\ \mu$m throughout the simulations while the amplitude, $A$, was fixed at $\sqrt{2}$ nm (equalling 1 nm RMS). A set of 15 simulations was performed at each period of the surface roughness, with the phase, $\theta$, picked at random for each individual interface. The LER was estimated for each constant-period ensemble, and Fig. 2 shows LER as a function of the spatial frequency of the roughness, $k_y = 2\pi/\Lambda$, the error bars indicate the 95% confidence interval as per the $\chi^2$-distribution. Also shown in Fig. 2, by the dashed line, is a typical power spectral density plot for the roughness of a thermally-evaporated silver film, obtained from atomic-force microscopy (AFM) analysis.

The simulation data indicates resonant behaviour with three resonance peaks inside the range of typical spatial frequencies present in silver thin-film surface roughness. These are centred at spatial frequencies of 51, 93 and $165\ \mu$m$^{-1}$($\pm < 5\%$) and their full width at half maximum (FWHM) is 14, 28 and $19\ \mu$m$^{-1}$, respectively. Compared to the non-resonant baseline the LER magnitude is increased by 110%, 267% and 172% for the respective peaks. This implies that across the spatial frequency band, where the resonant behaviour is observed, approximately one third of

![](./images/811814754371764224_2.jpg)

Fig. 2. Line-edge roughness, $3\sigma$, (solid line and symbols) as a function of the surface roughness wave vector, $k_y$. The error bars represent the 95% confidence interval as per the $\chi^2$-distribution. Three resonance peaks are present inside the central interval of the plot. The dashed line represents the power spectral density (PSD) for a typical silver thin-film.

![](./images/811814754371764224_3.jpg)

Fig. 3. Position of the central resonance peak as a function of grating period, p. The trendline represents a directly proportional fit with a correlation coefficient of 0.64 nm/nm with a coefficient of determination, $R^{2}$, of 0.96.

the band is affected by the resonant LER increase to significant degree.

In order to identify the causes of the resonant coupling, that the peaks in Fig. 2 imply, additional simulations were performed while varying either the wavelength of the incident radiation, $\lambda$, or the period of the apertures in the shadow mask, $p$, each by $\pm 20 \%$ around their nominal values ($\lambda = 365$ nm, $p = 100$ nm). The impact of changing the wavelength, $\lambda$, to 292 and 438 nm respectively, was negligible and neither was a measurable shift in resonant peak position nor a significant change in peak height observed. Simulations with the aperture period, $p$, set to 80 and 120 nm, respectively, caused a considerable and apparently linear shift in the position of the central resonance peak as is illustrated in Fig. 3, with no discernable change in peak amplitude. This shows a linear variation of the peak position (surface roughness period at which the LER was greatest) with regards to $p$, with the peak position occurring at approximately 65% of the grating period. The reason for this non-unity scaling factor is not known at present, but it could be related to the finite domain size in which these simulations were performed.

## 4. Potential implications in superlens imaging

This resonant interaction constitutes an additional consideration in regards to superlens enhanced ENFOL. For exposure patterns with features inside a narrow spatial frequency bandwidth it is potentially possible to tailor the metallo-dielectric interfaces to minimise LER in the image. This would necessitate excellent control of deposition characteristics such as grain size, and consequently surface roughness spatial frequency, distribution. Conversely, patterns comprised of features with a wide spatial frequency distribution will experience inhomogeneous LERs. In this case minimising the surface roughness magnitude would become even more important in order to achieve homogeneous imaging characteristics across the entirety of the exposure pattern.

An analysis of superlens images presented in relation to successful superlens lithography experiments yields a LER figure of more than 100 nm for lines approximately 225 nm wide. This figure is about five times larger than the figure of $\approx 20$ nm predicted by the FEM simulations for a single layer superlens with interfacial surface roughness of around 1 nm RMS. This implies that the contributions to LER from other factors, such as the resist and LER in the mask being imaged, are also of importance. Until these factors can be controlled, a systematic experimental study of the resonant surface roughness interactions presented here is not warranted.

## 5. Conclusions

The results presented here show that there are resonant interactions between superlens surface roughness and LER when imaging grating-like objects. The resonance peaks, observed for a 100 nm period half-pitch grating, are situated in the surface roughness period range of 30-150 nm, which, unfortunately, falls well within the PSD distribution for a typical thermally deposited silver thin-film. Control of grain size during film deposition (whilst maintaining low RMS roughness amplitude) is one possible avenue to mitigating these effects by ensuring that the features being imaged do not strongly resonate with the dominant film roughness interaction modes. Experimental verification of these roughness resonances will only be possible once precise control of surface roughness parameters, in silver thin-film deposition, has been achieved.

## References

[1] J.B. Pendry, Phys. Rev. Lett. 85 (2000) 3966.
[2] N. Garcia, M. Nieto-Vesperinas, Phys. Rev. Lett. 88 (2002).
[3] P.M. Valanju, R.M. Walser, A.P. Valanju, Phys. Rev. Lett. 88 (2002).
[4] D.R. Smith, D. Schurig, J.B. Pendry, App. Phys. Lett. 81 (2002) 2713.
[5] J.B. Pendry, D.R. Smith, Phys. Rev. Lett. 90 (2003).
[6] D.O.S. Melville, R.J. Blaikie, C.R. Wolf, Appl. Phys. Lett. 84 (2004) 4403.
[7] D.O. S Melville, R.J. Blaikie, Opt. Express 13 (2005) 2127.
[8] N. Fang, H. Lee, C. Sun, X. Zhang, Science 308 (2005) 534.
[9] Z. Liu, N. Fang, T. Yen, X. Zhang, Appl. Phys. Lett. 83 (2003) 5184.
[10] M. Schøler, R.J. Blaikie, J. Opt. A: Pure Appl. Opt. 11 (2009) 105503.