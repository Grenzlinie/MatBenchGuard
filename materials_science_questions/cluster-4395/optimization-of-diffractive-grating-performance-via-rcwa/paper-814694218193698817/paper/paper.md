# Quantitative Angle-Resolved Small-Spot Reflectance Measurements on Plasmonic Perfect Absorbers: Impedance Matching and Disorder Effects

Andreas Tittl, $^{*, \dagger}$ Moshe G. Harats, $^{\ddagger}$ Ramon Walter, $^{\dagger}$ Xinghui Yin, $^{\dagger}$ Martin Schäferling, $^{\dagger}$ Na Liu, $^{\S}$  Ronen Rapaport, $^{\ddagger}$ and Harald Giessen $^{\dagger}$

$^{\dagger}$4th Physics Institute and Research Center SCOPE, University of Stuttgart, D-70569 Stuttgart, Germany, $^{\ddagger}$The Racah Institute of Physics and the Applied Physics Department, The Hebrew University of Jerusalem, Jerusalem, Israel, and $^{\S}$Max Planck Institute for Intelligent Systems, D-70569 Stuttgart, Germany

## ABSTRACT
Plasmonic devices with absorbance close to unity have emerged as essential building blocks for a multitude of technological applications ranging from trace gas detection to infrared imaging. A crucial requirement for such elements is the angle independence of the absorptive performance. In this work, we develop theoretically and verify experimentally a quantitative model for the angular behavior of plasmonic perfect absorber structures based on an optical impedance matching picture. To achieve this, we utilize a simple and elegant $k$-space measurement technique to record quantitative angle-resolved reflectance measurements on various perfect absorber structures. Particularly, this method allows quantitative reflectance measurements on samples where only small areas have been nanostructured, for example, by electron-beam lithography. Combining these results with extensive numerical modeling, we find that matching of both the real and imaginary parts of the optical impedance is crucial to obtain perfect absorption over a large angular range. Furthermore, we successfully apply our model to the angular dispersion of perfect absorber geometries with disordered plasmonic elements as a favorable alternative to current array-based designs.

![](./images/814694218193698817_1.jpg)

## KEYWORDS:
plasmonics · perfect absorbers · angular dispersion · impedance matching

Plasmonic absorbers incorporate resonant particles above a dielectric spacer layer and metallic mirror to achieve absorbance close to unity in a variety of spectral ranges. Starting from original experiments in the gigahertz and terahertz regions, $^{1,2}$ plasmonic and metamaterial-based perfect absorbers have moved toward the near-infrared and visible spectral ranges, with applications ranging from glucose and gas sensing to spectroscopy and photovoltaic efficiency enhancement. $^{3-6}$ To extend the concept of plasmonic perfect absorption toward technological applications, optical elements with high acceptance angles are required. Such elements are able to absorb most radiation from the incidence half-space, enabling improved sensitivity and efficiency in a wide range of devices. $^{7-16}$ However, so far, detailed experimental studies on the underlying reason for the angular dispersion of plasmonic perfect absorbers at visible and near-infrared wavelengths are missing. This is associated with the fact that angle-resolved reflectance measurements with quantitative accuracy, especially in the infrared spectral range, are not easily performed, particularly in common FTIR microscopy setups. Samples where only small areas have been nanostructured, for example, by electron-beam lithography, pose further challenges.

In this paper, we use a simple and elegant $k$-space measurement approach to record large-angle and polarization-dependent reflectance measurements on different perfect absorber geometries. Combining these results with extensive numerical modeling, we develop and verify a quantitative model for the angular behavior of plasmonic absorbers.

*Address correspondence to a.tittl@pi4.uni-stuttgart.de.

Received for review August 21, 2014 and accepted September 24, 2014.

Published online 10.1021/nn504708t

© XXXX American Chemical Society

TITTL ET AL.

VOL. XXX ■ NO. XX ■ 000-000 ■ XXXX

![](./images/814694218193698817_2.jpg)
A

![](./images/814694218193698817_3.jpg)

Figure 1. System under investigation. (a) Schematic of the angle-dependent reflectance measurements discussed in this work. We can study the optical response for incident light parallel and perpendicular to the plane of incidence (p- and s-polarization). (b) Overview of the four investigated plasmonic perfect absorber structures. (c) Schematic drawing of the spectral-angular $k$-space experimental setup used to obtain quantitative large-angle reflectance measurements from our structures. The back focal plane of the lens, which is the Fourier plane of the illuminated sample, is imaged onto the entry slit of a spectrometer to obtain reflectance spectra for a large range of incident angles simultaneously.

In particular, we determine the imaginary part of the optical impedance in our plasmonic absorbers to be the key factor for angle-independent performance. One key advantage of our experimental method is the ability to measure the angular response of plasmonic samples with small structured areas, making it ideally suited for the investigation of nanoscale devices fabricated using electron-beam lithography.

To shed light on the angular absorptive performance of our systems, we examine the angle-dependent reflectance from four different perfect absorber designs in p-polarization (Figure 1a,b). The experimental setup is depicted in Figure 1c.

The perfect absorber sample is illuminated (red beam), and the corresponding reflected beam (light red beam) is collected by the objective. The back focal plane (which constitutes the Fourier plane$^{17}$) of the objective is imaged onto the entrance slit of a spectrometer mounted with a Princeton Instruments PIXIS CCD (in the visible spectral range) or OMA V array (in the infrared). Using the spectrometer adds the ability to analyze the spectral response along with the angular response of the system.

The polar angles $\theta,\varphi$ are related to the $k$-space (Fourier plane) by the following relation:

$$
\vec{k}=k_{x} \hat{x}+k_{y} \hat{y}=\frac{2 \pi}{\lambda} \sin \theta \cos \varphi \hat{x}+\frac{2 \pi}{\lambda} \sin \theta \sin \varphi \hat{y}
$$

In this work, the measurement setup is aligned at $\varphi=0^{\circ}$, with the polarization parallel to the incident plane, as shown in Figure 1a, so only the polar angle $\theta$ is resolved. In the case of samples in the visible range, the CCD camera resolves the full spectral-angular response of the sample in one single measurement. Generally, the angular range of this measurement is only limited by the numerical aperture of the objective. In the case of samples in the NIR spectral range, the OMA V array records the spectral response only for a specific angle. Therefore, a motorized stage is used to scan the imaged Fourier plane on the spectrometer slit to resolve the full angular response of the perfect absorber.

This spectral-angular $k$-space imaging technique is easy to implement and very powerful for measuring small-area plasmonic structures efficiently and with high precision.$^{18}$ In our case, when using samples nanostructured by electron-beam lithography, only a $100\ \mu\text{m} \times 100\ \mu\text{m}$ area is measured. We note that, in most previous works, the optical response of perfect absorbers was commonly shown only for normal incidence, and no full angular characterization was demonstrated experimentally. Additionally, perfect absorbers are usually measured using a goniometric approach, which requires tilting the detectors, the samples, or both. This approach is very sensitive to alignment errors, and since each angle is measured separately, it requires very long measurement times. Also, typical goniometric reflection setups in commercial ellipsometers have minimum beam sizes in the millimeter range, making them unsuitable for measuring small-area plasmonic structures. The angular resolution is also limited by the mechanical steps of the goniometric stage. With the spectral-angular $k$-space imaging technique, we can resolve the spectral-angular response of small-area samples without any alignment errors, with high spectral and angular resolution, and with a very fast measurement.

# RESULTS AND DISCUSSION

As a first demonstration of our method, we examine a well-known near-infrared perfect absorber design consisting of an array of gold nanodisks stacked above a magnesium fluoride ($\text{MgF}_{2}$) spacer layer and a Au mirror.$^{3}$ In the original work, an absorbance of 99% was experimentally demonstrated at normal incidence. However, the angular dispersion was only investigated using numerical simulations.

The full angular dispersion of this perfect absorber design in a wide angular range from $-36$ to $36^{\circ}$ (limited by the numerical aperture of the objective) is shown in Figure 2a for a structure with a disk diameter of 330 nm, a disk height of 20 nm, a periodicity of 600 nm, a spacer height of 30 nm, and a mirror height of 200 nm.

We observe a clear reflectance dip at a wavelength of 1480 nm, with a minimum reflectance of around 2% and reflectance values below 10% over the whole angular range. Thus, we experimentally verify, for the

![](./images/814694218193698817_4.jpg)

Figure 2. (a) Spectral-angular reflectance measurements of the near-infrared Au-based perfect absorber. (b) Numerical simulation of the same system. The color bar represents the reflectance with perfect absorption corresponding to zero reflectance (blue).

first time, the near angle independence of this perfect absorber design.

To support our measurements theoretically, we perform numerical simulations using a scattering-matrix-based Fourier modal method¹⁹,²⁰ (Figure 2b; for simulation details, see the Methods section). We find an excellent agreement between simulation and experiment, with a pronounced reflectance dip again at a resonance wavelength of 1480 nm. The angle independence over the full range is also well-reproduced. Still, we find a somewhat broader spectral response of the resonance in the experiment when compared to the simulations. This is most likely due to inhomogeneous broadening as well as additional grain boundaries introduced during the nanostructuring of the Au disks.

The performance and especially the angular dispersion of perfect absorbers can be well-understood by considering an optical impedance matching picture. In general, a reflectance of zero in an optical element can be obtained by matching is optical impedance $Z$ to the value of the surrounding space. In perfect absorbers, this impedance can be tuned by varying geometric parameters such as the size of the resonant structure or the thickness of the spacer layer. Since the thick metallic mirror below the structure ensures zero transmittance, perfect impedance matching consequently results in perfect absorption at a certain design wavelength.

The underlying physics behind perfect absorption are commonly explained in one of two ways. The first explanation assumes resonant near-field coupling between the top nanostructure and the metallic mirror below. Thus, when light impinges on the structure, particle plasmon oscillations are excited in the resonant structure on top. The corresponding charge distribution then causes the oscillation of a mirror plasmon in the thick metallic film below. By tuning the thickness of the dielectric spacer layer, the phase delay between the plasmon and the mirror plasmon oscillation can be adjusted so they oscillate in antiphase. This is assumed to lead to the formation of a circular current distribution and consequently an induced magnetic mode in the spacer layer, which enables control over the impedance, and can also be found in other plasmonic geometries.²¹,²² Additionally, impedance matching plays an important role in areas such as plasmon waveguiding.²³

Recently, it has been shown that the near-field interaction of the resonant particle and the mirror can be decoupled, and the absorptive behavior can be explained in terms of interference between the two layers.²⁴ However, we stress that, regardless of the microscopic explanation of the perfect absorption behavior, the impedance matching model for the full optical element remains valid.

The impedance of our structure can be calculated easily from the scattering parameter results of our numerical simulations, using

$$
Z = \sqrt{\frac{(1+S_{11})^{2}-S_{21}^{2}}{(1-S_{11})^{2}-S_{21}^{2}}} \tag{1}
$$

where $S_{11}$ and $S_{21}$ denote the scattering matrix coefficients of normal incidence reflection and transmission in p-polarization, respectively. Due to the presence of the thick metallic mirror, $S_{21}$ can safely be set to zero. It is important to note that $Z = Z' + i\cdot Z''$ is, in general, a complex value.

![](./images/814694218193698817_5.jpg)

Figure 3. Numerical calculation of the reflectance and optical impedance of the Au disk array perfect absorber from Figure 2 at normal incidence. Both the real and imaginary parts of the optical impedance are perfectly matched to the vacuum values of one and zero, resulting in angle-independent perfect absorption.

Figure 3 shows the simulation results for the real and imaginary parts of the optical impedance compared to the reflectance for the Au disk array-based perfect absorber. We can clearly observe that both the real and the imaginary parts are perfectly matched to the respective vacuum values of one and zero (in cgs units) at resonance, resulting in angle-independent perfect absorption.

In nanostructured plasmonic absorber arrays, the main reason for a lack of angle independence is a

coupling of the absorber resonance to the first diffrac- tion order associated with the grating periodicity of the array. For a given incident angle $\theta$, this Rayleigh anomaly appears at wavelengths given by

$$
\lambda_{\mathrm{R}}=p\left(n_{\mathrm{env}}+\sin \theta\right) \tag{2}
$$

where $p$ is the periodicity of the array and $n_{\text {env }}$ is the refractive index of the surrounding medium or the spacer layer, respectively. The presence of the Rayleigh anomaly introduces additional impedance, causing a loss of the perfect impedance matching and thus reduced absorption. $^{25-27}$ Consequently, the de sign of angle-independent perfect absorber structures requires sufficiently small periodicities to ensure ade- quate spectral separation between the particle plas- mon mode and the Rayleigh anomaly for all required incident angles $\theta$. In this way, interaction between the grating mode and the perfect absorber resonance can be suppressed, leading to angle-independent absor- bance. The spectral separation condition is neatly fulfilled in the Au absorber case. For a periodicity of $p=600 \mathrm{~nm}$, and considering the interface of the spacer layer (MgF₂, $n=1.38$), the Rayleigh anomaly is found at $\lambda_{\mathrm{R}}=830 \mathrm{~nm}$, which is well away from the perfect absorber resonance at $\lambda_{0}=1480 \mathrm{~nm}$.

However, the concept of spectral separation between Rayleigh anomaly and perfect absorber resonance does not allow to judge, in a quantitative way, whether a given perfect absorber design is angle-independent or not. In the following, we will show that perfect matching of the imaginary part of the impedance is crucial to obtain fully angle-independent perfect absorption. To prove the reliability of this model, we will now focus on the more challenging concept of a perfect absorber in the visible wavelength range. To elucidate the influence of the grating mode, we compare two palladium-based perfect absorbers with different periodicities. In both cases, the designs consist of Pd wires stacked above a dielectric spacer and a Au mirror that ensures zero transmission. $^{4}$ Figure 4a shows the spectral-angular reflectance measurements of a Pd-based perfect absor- ber with a periodicity of 450 nm, a wire width of 100 nm, a wire height of 20 nm, a MgF₂ spacer height of 65 nm, and a mirror thickness of 200 nm. Even though the absorbance reaches a maximum of 95% at a wavelength of 720 nm at normal incidence, we observe a strong angular dispersion when moving to higher incident angles. Consequently, this design can only be used up to an acceptance angle of $\theta=\pm 14^{\circ}$ while maintaining an absorbance of $A>90 \%$. This result is again well- supported by our numerical simulations (Figure 4b).

The angular optical response of a Pd-based perfect absorber with a smaller periodicity of 300 nm, a wire width of 85 nm, a wire height of 30 nm, an Al₂O₂ spacer height of 35 nm, and a mirror thickness of 200 nm is shown in Figure 4c. For this optimized geometry, the angular dispersion is greatly reduced. The small

![](./images/814694218193698817_6.jpg)

Figure 4. (a) Spectral-angular reflectance measurements on a Pd-based perfect absorber in the visible wavelength range. The periodicity is $p=450 \mathrm{~nm}$. (b) Numerical simula tion of the same system. (c) Spectral-angular reflectance measurements on a Pd-based perfect absorber in the visible wavelength range. The periodicity is $p=300 \mathrm{~nm}$. Note the greatly reduced angle dependence due to the smaller periodicity. (d) Numerical simulation of the same system.

periodicity design again offers very high absorbance of98% at a wavelength of 690 nm and maintains absor- bance $A>90 \%$ for acceptance angles up to $\theta=\pm 36^{\circ}$ . This constitutes an increase of the acceptance angle by close to a factor of 2.5 over the absorber with larger periodicity, which is again in excellent agreement with our simulations (Figure 4d).

The optical impedance matching model now allows quantification of the influence of grating modes on the angular behavior of the perfect absorber resonance. For the large periodicity case ( $p=450 ~nm$ , Figure $5 a$ ), only the real part of the optical impedance is perfectly matched to one, which ensures zero reflectance at normal incidence. However, there is pronounced mis- match of $\Delta Z^{\prime \prime}=-0.2$ in the imaginary part of the impedance (in cgs units). This indicates the presence of a grating mode close to the resonance, which causes the strong angular dispersion. The fact that the reflec- tance at normal incidence is near zero despite the impedance mismatch can be understood by calculating the reflectance as a function of the complex impedance $Z=Z'+i \cdot Z^{\prime \prime}$ . Assuming near-perfect matching of the real part of the impedance $(Z^{\prime}=1)$ and a small mismatch of the imaginary part $(|Z^{\prime \prime}| \ll 1)$ , this yields

$$
R=\frac{\left(Z^{\prime}-1\right)^{2}+\left(Z^{\prime \prime}\right)^{2}}{\left(Z^{\prime}+1\right)^{2}+\left(Z^{\prime \prime}\right)^{2}} \approx \frac{\left(Z^{\prime \prime}\right)^{2}}{4} \approx 0 \tag{3}
$$

Consequently, a small impedance mismatch of the imaginary part has only a negligible influence on the

![](./images/814694218193698817_7.jpg)

Figure 5. Numerical calculation of the reflectance and optical impedance of the two previously discussed Pd-based plasmonic perfect absorbers. (a) For a large periodicity of $p = 450$ nm, only the real part of the impedance is perfectly matched. The mismatch in the imaginary part indicates the presence of propagating modes and thus leads to stronger angle dependence of the absorption. (a) For a small periodicity of $p = 300$ nm, both the real and imaginary parts of the optical impedance are perfectly matched to the vacuum values, resulting in angle-independent perfect absorption.

reflectance at normal incidence. When moving to larger angles, however, this mismatch quickly increases, leading to the observed strong angular dispersion (Supporting Information Figure S1).

In contrast, for the small periodicity case ($p = 300$ nm), both the real and the imaginary parts of the impedance are perfectly matched to the respective vacuum values of one and zero, resulting in "true" angle-independent perfect absorption (Figure 5b).

To further examine the transition from small to large periodicities, we examine a continuous transition from the $p = 300$ nm to the $p = 450$ nm case. To achieve this, we consider the small periodicity design from Figure 4c and only introduce a gradual increase of the periodicity (Figure 6).

The real part of the optical impedance remains close to one for the whole periodicity range, while the imaginary part deviates strongly, reaching a maximum impedance mismatch of $\Delta Z'' = -0.6$ for the largest periodicity of 450 nm. Thus, even though the absorbance at normal incidence of this system remains very high ($A > 92\%$) for increasing periodicity, the angular behavior is strongly modified. This proves that the imaginary part of the optical impedance is a reliable design parameter and quantitative indicator for the angle independence of array-based plasmonic perfect absorber geometries. Thus, an array-based perfect absorber design which exhibits $R = 0$ at normal incidence as well as $Z'' = 0$ will not be strongly influenced by grating effects and should consequently provide the highest possible acceptance angles and, for most applications, the best performance.

![](./images/814694218193698817_8.jpg)

Figure 6. Impedance at resonance and at normal incidence of a Pd-based perfect absorber for increasing periodicity. The real part of the impedance remains mostly constant, while the imaginary part moves away from the vacuum value of zero for larger periodicities.

One intriguing alternative approach for obtaining angle-independent perfect absorbers is a system where the plasmonic resonators are placed on the spacer layer in a disordered fashion rather than in an array. However, the numerical design and optimization of such structures is challenging due to the very large computational domains associated with disordered systems. Consequently, we start our numerical design process with an array-based sample and optimize the geometry to obtain perfect absorption at the desired resonance wavelength. A disordered geometry with a similar surface coverage is then realized experimentally using colloidal nanofabrication. For such disordered samples, our measurement method enables high-throughput characterization of the angular response of such structures at a wide range of operating wavelengths.

Figure 7a shows spectral-angular reflectance measurement of a disordered Au-based perfect absorber with a disk diameter of 160 nm, a disk height of 20 nm, a $MgF_2$ spacer height of 40 nm, and a mirror thickness of 120 nm. Importantly, this Au-based absorber works in the red part of the visible spectral range, where the design of angle-independent perfect absorbers is challenging. The disordered Au nanodisks were produced using colloidal etching lithography (see SEM image in Figure 7b; fabrication details can be found in the Methods section).

In this system, we observe a high absorbance of $A = 92\%$ at a wavelength of 780 nm for normal incidence, which remains above 90% for acceptance angles up to

![](./images/814694218193698817_9.jpg)

Figure 7. (a) Spectral-angular reflectance measurements on a disordered Au-based perfect absorber in the 800 nm wavelength range. (b) SEM image of the disordered absorber structure. (c) Simulated reflectance and optical impedance of an individual Au disk perfect absorber element. Both the real and the imaginary parts of the optical impedance are perfectly matched to the vacuum values of one and zero. (d) Histogram of the median interparticle distances extracted from the SEM image in b. We find a median distance of around 345 nm with a standard deviation of 140 nm. Due to the disorder and the spread of available periodicities, grating effects are effectively suppressed.

$\theta = \pm36^\circ$. The performance of the disordered design can be understood in terms of our impedance matching model by considering two determining factors: the local impedance matching of individual absorber elements and the suppression of interparticle coupling and grating effects via their spatial arrangement.

To first examine the local impedance matching, we calculate the optical impedance of an individual perfect absorber element consisting of one Au nanodisk stacked above a $MgF_2$ spacer layer and a Au mirror. This simulation is carried out using a FDTD approach (calculation details are provided in the Methods section). The results of this simulation are shown in Figure 7c. We find a distinct reflectance minimum close to the experimental resonance position, as well as perfect matching of the real and imaginary parts of the optical impedance to vacuum values of one and zero. Thus, when considered separate from possible grating contributions, our design should exhibit excellent angle-independent performance.

Regarding the spatial arrangement of the individual absorber elements, there are two crucial requirements for angle independence: The interparticle distance needs to be large enough to prevent near-field coupling of adjacent resonators, and the spatial arrangement of the particles needs to deviate sufficiently from an exact array to suppress the formation of grating modes. In our sample, the Au nanodisks form a disordered structure with a surface coverage of approximately 25%, which corresponds to a half-pitch grating in the array case.

To further quantify the particle distribution in our sample, we extract the locations of all nanodisks from the SEM image and find a median interparticle distance of around 345 nm with a standard deviation of 140 nm (Figure 7d). Considering the strong decay of plasmonic near-fields on the order of several tens of nanometers, this yields mostly uncoupled single plasmonic absorber structures.⁸,²⁹ Together with the fabrication-induced disorder, the significant spread of interparticle distances (which constitute different available periodicities) in the system leads to an effective suppression of grating effects.³⁰ Thus, the perfect impedance matching of individual perfect absorber elements combined with a suppression of the grating contribution yields fully angle-independent performance.

## CONCLUSION
We have developed and verified a quantitative model for the angular behavior of plasmonic perfect absorber structures based on the optical impedance picture. Using high-throughput angle-resolved reflectance measurements and numerical simulations, we have found that it is crucial to match both the real and imaginary parts of the optical impedance to vacuum values to obtain "true" angle-independent perfect absorption. We identified the imaginary part of the impedance as a reliable design parameter and quantitative indicator for the angle independence of plasmonic perfect absorber geometries. Our model was successfully verified for both array-based and

disordered perfect absorber geometries in the visible and near-infrared spectral ranges and can be easily extended toward other resonance wavelengths. The insights gained from our impedance model enable the rapid design of angle-independent plasmonic perfect absorber geometries and will lead to a multitude of applications of absorbing elements with high accep- tance angles in the future.

## METHODS
Angle-Dependent Numerical Simulations. Numerical simula- tions for the four perfect absorber geometries were performedusing a scattering-matrix-based Fourier modal method. $^{19,20}$  All structures were defined on a glass substrate (n = 1.5). The array-based Au perfect absorber consisted of Au nanodisks(diameter = 320 nm, periodicity = 600 nm, height = 20 nm)placed above a $MgF_{2}$ spacer layer (thickness $=30 nm, n=1.38$ ) and a Au mirror (thickness = 200 nm). Optical constants for Au were taken from the literature. $^{31}$ The palladium-based perfect absorber design with large periodicity consisted of a Pd wiregrating (wire width = 125 nm, periodicity = 450 nm, wire height =20 nm ) placed above a $MgF_{2}$ spacer layer (thickness =50 nm ) and a Au mirror (thickness = 200 nm). Optical constants for Pd were again taken from the literature. $^{32}$ The palladium-based perfect absorber with small periodicity consisted of a Pd wiregrating (wire width = 85 nm, periodicity = 300 nm, wire height =30 nm ) placed above a $Al_{2} O_{3}$ spacer layer (thickness =35 nm, n = 1.75) and a Au mirror (thickness = 200 nm).

Impedance Calculation for Individual Absorber Elements. The im- pedances for the randomly arranged perfect absorber were calculated in Lumerical FDTD solutions. To this end, a single particle calculation employing a cubic 450 nm total-field-scat- tered field source containing the complete absorber geometry(120 nm Au mirror, $40 nm MgF_{2}$ spacer, and one Au disk with a diameter of 160 nm and a height of 20 nm) was carried out. The entire FDTD simulation domain spanned a $5 \mu m$ side length cube bounded by perfectly matched layers. The boundaries of the scattered-field region, which coincided with the boundaries of the simulation domain, were chosen such that the fields at the Au mirror were already sufficiently decayed to ensure the convergence of the simulation. This isolated the absorptive performance of a single absorber element. The impedance ex- tracted from this simulation was equivalent to the impedance of a surface covered with noninteracting absorber elements of an average density of at least $1 /(450 nm)^{2}$ , effectively excluding grating effects. The amplitude and phase of a normal incidence backward-scattered wave were extracted. In order to obtain the scattering matrix parameter $S_{11}$ from this, we corrected for the propagation phase from the source to the absorber and back to the monitor. The impedance was then calculated according to $Z=[(1+S_{11})^{2} /(1-S_{11})^{2}]^{1 / 2}$ .

Fabrication of the Perfect Absorber Samples. The array-based perfect absorber designs were fabricated as described pre- viously. $^{3,4}$ The disordered Au-based perfect absorber design was fabricated using a colloidal method. Starting from a cleaned borosilicate substrate, all necessary materials were evaporated using electron-beam-assisted deposition. The deposited materi- al system consisted of a 5 nm titanium adhesion layer, a 120 nm Au mirror, a $50 nm MgF_{2}$ spacer layer, followed by another 20 nm of Au and a 40 nm Ni sacrificial layer.

The Ni surface was treated in an $O_{2}$ plasma for 18 s, and a solution of PDDA was drop-coated. Next, the sample was rinsed with demineralized water and dried with $N_{2}$ . Directly after this step, PS nanospheres (160 nm diameter, nonfunctionalized,0.2 wt % in water, ultrasonicated for about 40 min) were drop- coated on the surface, rinsed after 1 min with demineralized water, and immersed in hot water $(98^{\circ} C)$ for about 3 min. After this, the sample was dried with $N_{2}$ . To produce the nanodisks, the sample was then dry etched with an Ar ion beam for 300 s. The PS nanospheres were removed by putting the sample in acetone for about 12 h, followed by treatment in $O_{2}$ plasma for 30 min. The sample was put in diluted (1:9) sulfuric acid for 2 min, rinsed afterward with demineralized water, and dried with $N_{2}$ .

Calculation of Interparticle Distances in the Disordered Perfect Absor- ber. Statistics on the interparticle distances in the disordered perfect absorber geometry were calculated using a custom MATLAB script. First, the locations of the individual nanodisks were extracted from the SEM image in Figure 7b using MA- TLAB's image processing toolbox. To add a neighbor relation- ship to the data set, a Delaunay triangulation was created for the array of nanodisk positions. The interparticle distance was then defined as the average distance of each nanodisk from its neighbors in the triangulation. This definition is a good repre- sentation of the effective particle separation and thus useful for the estimation of grating contributions in our impedance model.

Conflict of Interest: The authors declare no competing financial interest.

Acknowledgment. We are grateful to D. Dregely and R. Taubert for providing the Pd-based perfect absorber samples investigated in this study. We thank T. Weiss for help with the numerical simulations. A.T., X.Y., R.W., M.S., and H.G. were financially supported by the Deutsche Forschungsgemeinschaft(SPP1391, FOR730, GI 269/11-1), the Bundesministerium für Bildung und Forschung (13N9048 and 13N10146), the ERC Advanced Grant COMPLEXPLAS, the Baden-Württemberg Stif- tung (Spitzenforschung II), and the Ministerium für Wissenschaft, Forschung und Kunst Baden-Württemberg (Az: 7533-7-11.6-8). X.Y. additionally acknowledges support by the Carl-Zeiss- Stiftung. M.H. and R.R. acknowledge financial support by the FIRST Program of the Israel Science Foundation (Grant No.1046/10). Financial support by the European Cooperation in Science and Technology through COST Action MP1302 Nano- spectroscopy is gratefully acknowledged. We acknowledge funding through the German-Israel Foundation (GIF) and the Alexander-von-Humboldt Foundation.

Supporting Information Available: Numerical simulations of the angle-dependent optical impedance, Figure S1. This material is available free of charge via the Internet at http://pubs.acs.org.

## REFERENCES AND NOTES
1. Landy, N.; Sajuyigbe, S.; Mock, J.; Smith, D. R.; Padilla, W. J. Perfect Metamaterial Absorber. Phys. Rev. Lett. 2008, 100,207402.
2. Tao, H.; Bingham, C.; Strikwerda, A.; Pilon, D.; Shrekenhamer, D. B.; Landy, N.; Fan, K.; Zhang, X.; Padilla, W. J.; Averitt, R. D. Highly Flexible Wide Angle of Incidence Terahertz Meta- material Absorber: Design, Fabrication, and Characterization. Phys. Rev. B 2008, 78, 241103.
3. Liu, N.; Mesch, M.; Weiss, T.; Hentschel, M.; Giessen, H. Infrared Perfect Absorber and Its Application as Plasmonic Sensor. Nano Lett. 2010, 10, 2342-2348.
4. Tittl, A.; Mai, P.; Taubert, R.; Dregely, D.; Liu, N.; Giessen, H. Palladium-Based Plasmonic Perfect Absorber in the Visible Wavelength Range and Its Application to Hydrogen Sensing. Nano Lett. 2011, 11, 4366-4369.
5. Chen, K.; Adato, R.; Altug, H. Dual-Band Perfect Absorber for Multispectral Plasmon-Enhanced Infrared Spectroscopy. ACS Nano 2012, 6, 7998-8006.
6. Vora, A.; Gwamuri, J.; Pala, N.; Kulkarni, A.; Pearce, J. M.; Güney, D. O. Exchanging Ohmic Losses in Metamaterial Absorbers with Useful Optical Absorption for Photovoltaics. Sci. Rep. 2014, 4, 4901.
7. Moreau, A.; Ciraci, C.; Mock, J. J.; Hill, R. T.; Wang, Q.; Wiley, B. J.; Chilkoti, A.; Smith, D. R. Controlled-Reflectance

---
TITTL ET AL.
VOL. XXX ■ NO. XX ■ 000-000 ■ XXXX
![ACSNANO](https://pubs.acs.org/na101/home/literatum/publisher/achs/journals/content/ancac3/2024/ancac3.2024.xxx.issue-xx/acs.nanolett.XXXXXXX/20240101/images/medium/nn-2024-XXXXXXX_0009.gif)
www.acsnano.org
G

Surfaces with Film-Coupled Colloidal Nanoantennas.
Nature 2013, 492, 86-89.

8. Alaee, R.; Menzel, C.; Rockstuhl, C. Perfect Absorbers on
Curved Surfaces and Their Potential Applications. Opt.
Express 2012, 20, 18370-18376.

9. Fang, Z.; Zhen, Y.-R.; Fan, L.; Zhu, X.; Nordlander, P. Tunable
Wide-Angle Plasmonic Perfect Absorber at Visible Fre-
quencies. Phys. Rev. B 2012, 85, 245401.

10. Wu, C.; Neuner, B.; Shvets, G.; John, J.; Milder, A.; Zollars, B.;
Savoy, S. Large-Area Wide-Angle Spectrally Selective Plas-
monic Absorber. Phys. Rev. B 2011, 84, 075102.

11. Hao, J.; Zhou, L.; Qiu, M. Nearly Total Absorption of Light
and Heat Generation by Plasmonic Metamaterials. Phys.
Rev. B 2011, 83, 165107.

12. Chriki, R.; Yanai, A.; Shappir, J.; Levy, U. Enhanced Efficiency
of Thin Film Solar Cells Using a Shifted Dual Grating
Plasmonic Structure. Opt. Express 2013, 21, A382-A391.

13. Yanai, A.; Orenstein, M.; Levy, U. Giant Resonance Absorp-
tion in Ultra-thin Metamaterial Periodic Structures. Opt.
Express 2012, 20, 3693-3702.

14. Esfandyarpour, M.; Garnett, E. C.; Cui, Y.; McGehee, M. D.;
Brongersma, M. L. Metamaterial Mirrors in Optoelectronic
Devices. Nat. Nanotechnol. 2014, 9, 542-547.

15. Pala, R. A.; Liu, J. S. Q.; Barnard, E. S.; Askarov, D.; Garnett,
E. C.; Fan, S.; Brongersma, M. L. Optimization of Non-
periodic Plasmonic Light-Trapping Layers for Thin-Film
Solar Cells. Nat. Commun. 2013, 4, 2095.

16. Huebner, U.; Pshenay-Severin, E.; Alaee, R.; Menzel, C.;
Ziegler, M.; Rockstuhl, C.; Lederer, F.; Pertsch, T.; Meyer,
H.-G.; Popp, J. Exploiting Extreme Coupling To Realize a
Metamaterial Perfect Absorber. Microelectron. Eng. 2013,
111,110-113.

17. Goodman, J. W. Introduction to Fourier Optics; Roberts &
Company Publishers: Greenwood Village, CO, 2005.

18. Harats, M. G.; Livneh, N.; Zaiats, G.; Yochelis, S.; Paltiel, Y.;
Lifshitz, E.; Rapaport, R. Full Spectral and Angular Char-
acterization of Highly Directional Emission From Nano-
crystal Quantum Dots Positioned on Circular Plasmonic
Lenses. Nano Lett. 2014, 10.1021/nl502652k.

19. Weiss, T.; Granet, G.; Gippius, N. A.; Tikhodeev, S.; Giessen,
H. Matched Coordinates and Adaptive Spatial Resolution
in the Fourier Modal Method. Opt. Express 2009, 17, 8051-
8061.

20. Weiss, T.; Gippius, N. A.; Tikhodeev, S.; Granet, G.; Giessen,
H. Efficient Calculation of the Optical Properties of Stacked
Metamaterials with a Fourier Modal Method. J. Opt. A: Pure
Appl. Opt. 2009, 11, 114019.

21. Dolling, G.; Wegener, M.; Soukoulis, C. M.; Linden, S. Negative-
Index Metamaterial at 780 nm Wavelength. Opt. Lett. 2007,
32,53-55.

22. Linden, S.; Enkrich, C.; Wegener, M.; Zhou, J.; Koschny, T.;
Soukoulis, C. M. Magnetic Response of Metamaterials at
100 Terahertz. Science 2004, 306, 1351-1353.

23. Fang, Z.; Fan, L.; Lin, C.; Zhang, D.; Meixner, A. J.; Zhu, X.
Plasmonic Coupling of Bow Tie Antennas with Ag Nano-
wire. Nano Lett. 2011, 11, 1676-1680.

24. Chen, H.-T. Interference Theory of Metamaterial Perfect
Absorbers. Opt. Express 2012, 20, 7165-7172.

25. Polyakov, A.; Zolotorev, M.; Schuck, P. J.; Padmore, H. A.
Collective Behavior of Impedance Matched Plasmonic
Nanocavities. Opt. Express 2012, 20, 7685-7693.

26. Falco, F.; Tamir, T.; Leung, K. M. Grating Diffraction and
Wood's Anomalies at Two-Dimensionally Periodic Impe-
dance Surfaces. J. Opt. Soc. Am. A 2004, 21, 1621-1634.

27. Oliner, A. H. A. A. A New Theory of Wood's Anomalies on
Optical Gratings. Appl. Opt. 1965, 4, 1275-1297.

28. Su, K. H.; Wei, Q. H.; Zhang, X.; Mock, J. J.; Smith, D. R.;
Schultz, S. Interparticle Coupling Effects on Plasmon Re-
sonances of Nanogold Particles. Nano Lett. 2003, 3, 1087-
1090.

29. Quinten, M.; Kreibig, U. Absorption and Elastic Scattering
of Light by Particle Aggregates. Appl. Opt. 1993, 32, 6173-
6182.

30. Nau, D.; Schönhardt, A.; Bauer, C.; Christ, A.; Zentgraf, T.;
Kuhl, J.; Klein, M.; Giessen, H. Correlation Effects in
Disordered Metallic Photonic Crystal Slabs. Phys. Rev. Lett.
2007,98,133902.

31. Johnson, P. B.; Christy, R. W. Optical-Constants of Noble-
Metals. Phys. Rev. B 1972, 6, 4370-4379.

32. Vargas, W. E.; Rojas, I.; Azofeifa, D. E.; Clark, N. Optical
and Electrical Properties of Hydrided Palladium Thin Films
Studied by an Inversion Approach from Transmittance
Measurements. Thin Solid Films 2006, 496, 189-196.

---

TITTL ET AL.

VOL. XXX • NO. XX • 000-000 • XXXX
![](./images/814694218193698817_11.jpg)
H