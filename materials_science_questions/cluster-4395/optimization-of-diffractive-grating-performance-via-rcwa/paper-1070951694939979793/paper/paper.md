Highly efficient, tunable, electro-optic metasurfaces
based on quasi-bound states in the continuum

Christopher Damgaard-Carstensen¹, Torgom Yezekyan², Mark L. Brongersma³,
and Sergey I. Bozhevolnyi¹

¹Centre for Nano Optics, University of Southern Denmark, Campusvej 55, DK-5230 Odense
M, Denmark
²POLIMA — Center for Polariton-driven Light–Matter Interactions, University of Southern
Denmark, Campusvej 55, DK-5230 Odense M, Denmark
³Geballe Laboratory for Advanced Materials, Stanford University, Stanford, California 94305,
United States

Abstract

Ultrafast and highly efficient dynamic optical metasurfaces enabling truly spatiotemporal control over
optical radiation are poised to revolutionize modern optics and photonics, but their practical realization
remains elusive. In this work, we demonstrate highly efficient electro-optic metasurfaces based on quasi-
bound states in the continuum (qBIC) operating in reflection that are amenable for ultrafast operation
and thereby spatiotemporal control over reflected optical fields. The material configuration consists
of a lithium niobate thin film sandwiched between an optically thick gold back-reflector and a grating
of gold nanoridges also functioning as control electrodes. Metasurfaces for optical free-space intensity
modulation are designed by utilizing the electro-optic Pockels effect in combination with an ultra-
narrow qBIC resonance, whose wavelength can be finely tuned by varying the angle of light incidence.
The fabricated electro-optic metasurfaces operate at telecom wavelengths with the modulation depth
reaching 95 % (modulating thereby 35 % of the total incident power) for a bias voltage of ±30 V
within the electrical bandwidth of 125 MHz. Leveraging the highly angle-dependent qBIC resonance
realized, we demonstrate electrically tunable phase contrast imaging using the fabricated metasurface.
Moreover, given the potential bandwidth of 39 GHz estimated for the metasurface pixel size of 22 µm,
the demonstrated electro-optic metasurfaces promise successful realization of unique optical functions,
such as harmonic beam steering and spatiotemporal shaping as well as nonreciprocal operation.

Introduction

In recent years, research into dynamic optical metasurfaces, consisting of controllable planar arrays
of subwavelength elements, has increased significantly [1–4]. The further improvement of dynamic
metasurfaces will unlock many new application areas in technologies such as spatial light modulators
(SLMs) [5–7], light detection and ranging (LIDAR) [7,8], computational imaging and sensing [9], and
virtual and augmented reality systems [10,11]. The main drawback of using metasurfaces for efficient
control of radiation is that the interaction length is severely limited by the fundamentally thin nature
of metasurfaces. This can be remedied by utilizing materials and configurations that allow for large
refractive index variations, such as structural reconfigurations [12,13], phase-change materials [14–16],
materials with large thermo-optic effects [17,18], or MEMS configurations [19–21]. The disadvantage
of all these materials and configurations is their inherently slow switching speeds. Recently reported
electrically tunable ITO-based metasurfaces, although demonstrating promising developments, were
still limited to a few MHz in bandwidth in their experimental realizations [22–24].

The linear electro-optic (Pockels) effect, which is found in several ferroelectric media without cen-
trosymmetry like electro-optic polymers [25,26], lead zirconate titanate (PZT) [27,28], and lithium
niobate (LN) [29–31], offers inherently fast electrical control of refractive index changes. LN provides
large electro-optic coefficients ($r_{33} = 31.45$ pm/V for the extraordinary polarization and $r_{13} = 10.12$
for the ordinary [32]), a high Curie temperature ($\sim 1200$ °C), a wide transparency range (0.35-4.5
µm), and great mechanical and chemical stability [33], all of which makes it an attractive platform for

![](./images/1070951694939979793_1.jpg)

Figure 1: 3D rendering of our tunable qBIC metasurface with an incident continuous beam and a modulated outgoing beam. Top plots show the experimentally applied electrical square-shaped signal (left plot) and the corresponding measured modulated optical output (right plot).

dynamic optical components [34]. The main challenge faced when implementing electro-optic meta- surfaces is that very small refractive index changes due to the Pockels effect in combination with the aforementioned severe limitations in the interaction length result in weak modulation of optical fields [35,36]. To circumvent this formidable challenge, one should exploit resonant configurations that would increase the effective interaction length either by multiple reflections across the metasurface layer in Fabry-Perot resonances [37] or by nonlocal interaction with the waveguide modes propagating along the metasurface layer [38].

Here, we make the next important step in the latter direction by adding band gap effects to the nonlocal interaction with the waveguide modes and making thereby use of quasi-bound states in the continuum (qBIC) that result in ultra-narrow qBIC resonances [39]. We investigate the occurrence of qBIC resonances in the LN electro-optic metasurface platform [37] with symmetric and asymmetric gratings of gold electrodes, being inspired by extremely high Q resonances ($>2\times10^5$) realized with all- dielectric configurations [40,41]. Through the use of numerical simulations and extensive experiments, we utilize the presence of a qBIC resonance to design, fabricate, and experimentally characterize a metasurface for free-space intensity modulation. The fabricated electro-optic metasurfaces operate at telecom wavelengths with the modulation depth reaching 95 % combined with an absolute modulation of 35 % for a bias voltage of $\pm30$ V within the electrical bandwidth of 125 MHz. Furthermore, the operation wavelength of our metasurface can be tuned by changing the angle of incidence, and we show that our device maintains a modulation depth of 30-40 % within a wavelength range of more than 30 nm by changing the angle of incidence by $1^\circ$. Leveraging the highly angle-dependent qBIC resonance realized, we demonstrate electrically tunable phase contrast imaging using the fabricated metasurface. Moreover, given the potential bandwidth of 39 GHz estimated for the metasurface pixel size of 22 $\mu$m, the demonstrated electro-optic metasurfaces promise successful realization of unique optical functions, such as harmonic beam steering and spatiotemporal shaping as well as nonreciprocal operation

# Results

## Analysis of BIC and qBIC occurrence

We begin our investigation with numerical analysis of the formation of qBIC and BIC (bound states in the continuum) resonances in a planar waveguide, consisting of a thin $z$-cut LN layer (880 nm) on

an optically thick gold platform (300 nm) bonded together with a thin chromium layer (10 nm) and topped with a grating of gold ridges needed to introduce electro-optic control of waveguide modes. This waveguide configuration (without grating electrodes) is commercially available as thin-film LN wafers from NANOLN and was used in our experiments. The grating-assisted excitation of waveguide modes at telecom wavelengths for normal light incidence by using symmetric and asymmetric dielectric grating structures as well as the associated occurrence of BIC and qBIC resonances is well elucidated in our previous work [39]. Use of gold grating ridges instead of dielectric ridges along with the presence of a chromium-gold back reflector introduces (absorption) losses into an otherwise lossless configuration considered previously, influencing significantly the dynamics of resonance processes. The essential physics remains however the same: the resonant excitation of waveguide modes under normal light incidence, taking place at the first diffraction order, is intrinsically linked with the occurrence of Bragg reflection of counter-propagating waveguide modes and results thereby in the formation of a distributed Bragg resonator (DBR) along with BIC and qBIC resonances [39].

Let us first consider symmetric thin gold grating couplers on LN (Figure 1). The efficient excitation of two counter-propagating waveguide modes (excitation in the first diffraction order), means that the waveguide mode wavelength $(\lambda_{eff})$ should be equal to the grating period $(\Lambda)$: $\lambda_{eff} = \Lambda$ (Figure 2a). The condition for DBR realization, on the other hand, is $2\Lambda = m\lambda_{eff}$, where $m$ is the order of Bragg reflection. The only way to satisfy both conditions, namely the coupling in the first diffraction order and DBR, is to set $m=2$ (i.e., second order Bragg reflection). Here, we are interested in a low-loss fundamental TE mode, which in the desired telecom wavelength range $(\sim 1550$ nm) has an effective mode refractive index of 2.08 leading to a grating period of $\Lambda = 750$ nm. The dispersion curves of waveguide modes are depicted in Figure 2b, the qBIC is appearing in the lower energy side of the band gap, with the mode energy mainly concentrated beneath the gold stripe (Figure 2d). The dependence of the qBIC Q factor on the ridge width (for a fixed height) and height (for a fixed width) is presented in Figure 2c. Here one can note relatively large Q factors for very small ridge widths which is due to less absorption and weak coupling, further from some point, the increase in the ridge width is leading to an increase of the Q factor since the strength of the scattering (coupling) is again reduced. Even though the BIC itself is not accessible with a plane wave illumination, a slight shift from the normal incidence is leading to another important regime, so called "near-BIC", with characteristic high Q factors compared to qBIC [42]. Hence an introduced small angle of incidence is leading to a slight shift of the qBIC resonance position, and occurrence of a new resonance associated with the BIC (Figure 2b), where the distance between these two resonances is linked to the band gap. These features are also evident in reflection spectra of the configuration (Figure 3a and Supplementary Figure S1). Initially at the normal incidence, the qBIC resonance (reflection minima) is at 1551 nm, while with an incidence angle of $1^o$, it is shifted to 1558 nm, and the near-BIC is excited at a shorter wavelength of 1535 nm (larger energy). Further increase of the angle of incidence will lead to consequent shift of the resonances, making it tunable within certain limits.

Similar regimes can be obtained also with asymmetric grating couplers, i.e., when widths of every M$^{th}$ ridge is altered. Here we consider a structure with doubled period, i.e., every second ridge is perturbed, $\Lambda = 2\lambda_0$, where $\Lambda$ is the supercell period, and $\lambda_0$ is the period of individual ridges (Figure 2e). Here we follow the same logic for the coupling as for the symmetric case, hence $\lambda_{eff} = \Lambda$ holds, however, the DBR in this case is formed from ridges with period of $\lambda_0$, and consequently the DBR condition will be $2\lambda_0 = m\lambda_{eff}$. Again, combining the two conditions (coupling to the first diffraction order and DBR) one will get $m=1$, meaning that in the case of the asymmetric grating one deals with the first-order Bragg reflection, when considering the unperturbed grating structure. The corresponding dispersion curves for this configuration are shown in Figure 2f. Unlike the case with symmetric structure, here the qBICs are formed in the higher energy side of the band gap, which however is still consistent with previous case, since the mode energy is again concentrated beneath the gold stripes (Figure 2h). The dependence of the qBIC Q factor on the ridge perturbation (i.e., variation of every second ridge width for a fixed height) and height (for a fixed width) is presented in Figure 2g. Here one should note that the absence of any asymmetry results in resonances with large Q factors, since the mode excitation in the first order vanishes. Overall, both configurations have similar features in terms of Q factors and one can implement these structures to make use of narrow

![](./images/1070951694939979793_2.jpg)

**Figure 2:** Investigation of modes in the geometry and calculation of Q factor. a-d are for the symmetric grating, and e-h are for the asymmetric grating. a,e Schematic drawing of a metasurface consisting of a a symmetric and e asymmetric gold grating on top of 880 nm of LN on a gold substrate. b,f Simulated dispersion curves. c,g Simulated Q factor vs. c ridge width (lower axis, blue curve) and ridge thickness (upper axis, red curve) and g ridge perturbation (lower axis, blue curve) and ridge thickness (upper axis, red curve) for the fundamental qBIC mode branch under normal incidence. d,h Simulated TE field profiles for the fundamental qBIC (left) and BIC (right) modes for an incident field of 1 V/m. a-d The structure parameters are $\Lambda = 750$ nm, $w = 445$ nm and $t_g = 75$ nm. e-h The structure parameters are $\Lambda = 750$ nm, $w = 25$ nm, $d = 200$ nm, and $t_g = 60$ nm

resonances.

## Design and optimization of metasurface
By connecting the gold ridges in one end, thus forming a previously used comb-like grating configuration [31,38], the gold grating and back-reflector can function as integrated metal electrodes for efficient application of bias signals. The linear electro-optic Pockels effect gives rise to a change in the refractive index of LN, when a bias voltage is applied over the thin film. The change in refractive index is given by the first-order derivation [1]:
$$
|\Delta n| \simeq \frac{1}{2} n^{3} r_{h k} \frac{V}{d} \tag{1}
$$
where $n$ is the refractive index without bias voltage, $r_{h k}$ is the relevant Pockels coefficient, $d$ is the thickness of the LN thin-film, and V is the applied bias voltage.

The design procedure follows a similar reasoning to our previous work [38]. To achieve strong and efficient modulation one should look for a sharp and deep resonance. The large Q factors of qBICs offer a sharp resonance, and by simultaneously assuring that scattering and absorption losses are equal, the resonance can be operated at critical coupling, which results in complete radiation absorption [43]. We optimize our design through numerical simulations of one unit cell using a model with periodic boundary conditions, i.e., assuming an infinite grating. As previously mentioned, the grating period was fixed based on the desired wavelength range. Afterwards, we sweep the ridge width, $w$, thickness, $t_g$, and perturbation, $d$, for the asymmetric grating to achieve critical coupling. The optimized design parameters are: $\Lambda = 750$ nm, $t_g = 75$ nm, $w = 445$ nm for the symmetric grating and $\Lambda = 750$ nm, $t_g = 60$ nm, $w = 25$ nm, $d = 200$ nm for the asymmetric grating.

Two of the primary metrics for estimating performance are the absolute modulation (i.e., the amount of total incident power that is modulated), and the modulation depth or relative modulation (i.e., the amount of reflected power that is modulated). We apply a bias voltage of $\pm 30$ V to calculate the absolute modulation $|\Delta R|$, where $R$ is reflectance, and the modulation depth, which is defined as $1-(R_{min}(\lambda)/R_{max}(\lambda))$, where $R_{min}(\lambda)$ and $R_{max}(\lambda)$ are minimum and maximum reflectance values,

![](./images/1070951694939979793_3.jpg)

Figure 3: Simulated performance of tunable qBIC metasurface. a-c represent simulations for the symmetric grating, and d-f represent simulations for the asymmetric grating. a,d Reflectance (left axis, black line) and absolute modulation (right axis, red dashed line) vs. wavelength for bias voltages of 0 V and ±30 V, respectively. b,e Zoomed in view of reflectance vs. wavelength for bias voltages of -30 V (blue line), 0 V (black line), and 30 V (red line). c,f Achievable phase difference vs. wavelength when switching from -30 V to 30 V.

respectively. The simulated spectrum and modulation plots show that critical coupling is achieved (complete radiation absorption), and as a consequence thereof the expected modulation depth of 100 % is achieved (Figure 3a,d and Supplementary Figure S2). Furthermore, our design shows an absolute modulation of 50 % and a phase modulation of up to 220º for the symmetric grating (Figure 3a,c) and an absolute modulation of 35 % and a phase modulation of 200º for the asymmetric grating (Figure 3d,f). The ability to obtain ultrafast phase modulation larger than $\pi$ opens a new avenue towards true spatiotemporal applications [44]. A zoom-in view of the reflection minima visualizes the resonance shift of 2.5 nm (Figure 3b,e), which we use to calculate a figure of merit (FOM) that was introduced in our previous work [38]: $\text{FOM} = \Delta\lambda/\text{FWHM}$, where FWHM is full width half maximum. We achieve a FOM of 0.47 and 0.30 for the symmetric and asymmetric gratings, respectively. Both values are an order of magnitude larger than our previous work (0.046), thus verifying the superior performance of this new design. Due to the better simulated performance of the symmetric grating (absolute modulation and FOM is higher) and the limitations of our fabrication facilities (not possible to fabricate structures with aspect ratios (height/width) larger than one), we continue with fabrication of the symmetric grating.

After design optimization, a grating consisting of $N = 50$ periods was fabricated using electron- beam lithography and the spectrum was measured (Supplementary Figure S3). The measured spectrum shows a very broad and shallow resonance that does not match the simulated spectrum. We conduct a numerical investigation of the connection between the grating size, i.e., the number of unit cell periods, and the resonance shape through numerical simulations of a finite grating with sizes ranging from $N = 40$ to $N = 140$ unit cell periods. It is clearly seen that a larger grating gives a deeper and narrower resonance (Supplementary Figure S3). Therefore, we conduct thorough simulations for a finite model with $N = 120$ unit cell periods. Switching from the infinite to the finite model influences the reflection minimum that is now less deep, meaning the resonant excitation is shifted away from critical coupling (Supplementary Figure S4).

## Fabrication and static characterization of metasurface

The fabrication process starts by evaporation of large macroscopic electrodes through a shadow-mask (Figure 4a). Afterwards, the gratings are formed based on the design described in Figure 3a,c using the standard nanofabrication technology of electron-beam lithography and lift-off. During this process, the grating is aligned and interfaced with the macroscopic electrode for later application of bias voltages.

![](./images/1070951694939979793_4.jpg)

Figure 4: Fabrication and static characterization of qBIC metasurface. a Optical images of a macroscopic electrode and metasurface. b SEM images of the entire grating ($N=120$) and a zoom-in view of the fabricated gold ridges. Scale bars represent 10 $\mu$m (left) and 1 $\mu$m (right). c Measured (black line) and simulated (red dashed line) reflection spectra from the metasurface. Error bars are on the order of the line width.

Scanning electron microscopy images after lift-off show straight evenly-spaced gold ridges with very few defects (Figure 4b). For optical characterization of the static performance, a collimated beam from a supercontinuum source is linearly polarized and inbound on the grating. The reflected light is separated from the incident by a beam splitter, collected by a 20X objective, spatially filtered by a pinhole and collected by a camera or spectrometer (Supplementary Figure S5). The measured and simulated reflection spectra show very similar wavelength dependence in the large wavelength range from 1000-1700 nm for four pronounced reflection minima (Figure 4c). The two deepest and widest reflection minima ($\sim$1120 nm and $\sim$1460 nm) are Fabry-Perot modes, whereas the two narrow but less deep reflection minima ($\sim$1320 nm and $\sim$1550 nm) are excitation of guided modes. In this work, we designed around the right-most minimum at 1554 nm, which corresponds to the qBIC resonance discussed in the previous section.

Ultrafast and ultrathin spatial light modulators are a very desirable ideal application prospect for efficient free-space light modulators. The lateral miniaturization of such devices is directly related to the achievable resolution and device footprint. Under the assumption of the modulator functioning at critical coupling, we calculate the minimal achievable pixel size from the estimated decay length of the optical mode [31,45]. The loaded Q-factor of our device is $\sim$180, which corresponds to an unloaded Q-factor of $Q_U=2Q_L\approx360$ at critical coupling, where absorption and scattering losses are equal. The loss per unit length is estimated from the unloaded Q-factor:

$$
\alpha=\frac{4\pi}{Q_U\lambda_{eff}}\approx0.045\ \mu\mathrm{m}^{-1} \tag{2}
$$

where $\lambda_{eff}$ is the effective mode wavelength, and we assume an effective mode refractive index of 2. From the loss per unit length, the propagation length is derived as the inverse: $L_p\approx1/0.045\ \mu\mathrm{m}^{-1}=22\ \mu\mathrm{m}$. We note that the pixel size of an SLM configuration can be considerably reduced without risking crosstalk due to guided modes.

## Dynamic characterization of metasurface

To measure efficient modulator operation, we supply bias voltages to the sample using a function generator and detect reflected signals using a photodetector. By applying a bias voltage of $\pm30$ V, we measure an absolute modulation of up to 35 % in the wavelength range of 1540 to 1570 nm (Figure 5a). The absolute modulation is larger on the longer wavelength side of the reflection minimum, because the slope of the spectrum is larger. We note that the large spacing between the measurement points of the spectrum are due to the limited resolution of the spectrometer. In addition, a near-perfect modulation depth reaching 95 % is measured (Figure 5b), which corresponds very well with the simulations (Supplementary Figure S2b). The large contrast between the on- and off-state is visualized in the Supplementary Video S1. As discussed in the previous section, the location of reflection minima can be controlled by changing the angle of incidence of the laser. This effect is investigated in simulations and verified in measurements (Supplementary Figure S1), where we measure the spectrum and the modulation depth for an angle of incidence of $1^\circ$. As expected, the reflection minima are

![](./images/1070951694939979793_5.jpg)

Figure 5: Dynamic characterization of the fabricated tunable qBIC metasurface. a Measured reflection intensity (left axis, black dots and line) and absolute modulation (right axis, red dots and line) vs. wavelength for bias voltages of 0 V and ±30 V, respectively. Measurements are performed using a 1 kHz sinusoidal signal. A moving average of three points has been applied to the absolute modulation data points. b Measured modulation depth vs. wavelength of incident light for bias voltage of ±30 V. c Measured modulation vs. electrical frequency of the applied signal at 1556 nm. The dashed line represents -3 dB. a-c Dots are measurement points and lines are spline approximations to guide the eye. Error bars are on the order of data point sizes.

less pronounced and therefore the measured modulation depth is also reduced to the range of 30-40 %. This proves that our metasurface modulator is tunable within a range of more than 30 nm, while maintaining a decent modulation depth. However, the presence of a bandgap in the dispersion relation results in a range of unachievable wavelengths just below the wavelength of the reflection minimum for normal incidence.

The main advantage of making dynamic metasurfaces utilizing the electro-optic Pockels effect is the inherently fast modulation, which it supports. The electrical bandwidth of our device is measured in the range of 10-250 MHz, and we determine a -3 dB cutoff of 125 MHz (Figure 5c). The limiting factor of the achievable modulation speed is the electrical circuit, and herein primarily the size of the macroscopic electrode, which forms a capacitor with the continuous bottom gold electrode. We verify this by testing another electrode configuration, which is fabricated simultaneously with the grating by the use of electron beam lithography (Supplementary Figure S6). This way, the electrode can be more compact and consequently have a smaller surface area. A -3 dB cutoff frequency of 350 MHz is measured. Further limiting the size of the top electrode or limiting the bottom electrode to only span an area below the patterned grating would allow our metasurface modulator to reach electrical bandwidths of up to 39 GHz estimated for the metasurface pixel size of 22 $\mu$m, which is easily supported by the Pockels effect.

One possible application for high Q factor tunable metasurfaces, is to implement it for switchable phase contrast imaging. The large Q factor in combination with the highly angle-dependent spectral position of the minimum, leads to our metasurface attenuating paraxial rays at wavelengths close to resonance, while not influencing rays incoming at larger angles [46]. We demonstrate a proof-of-concept of switchable phase contrast imaging of a transparent Poly(methyl methacrylate) (PMMA) stripe, where the edge of the phase object is clearly emphasized at resonance and the contrast is decreased when the metasurface is shifted off resonance by tuning of the applied bias voltage (Supplementary Note 6).

## Discussion

To summarize, we have presented an investigation of the occurrence of BIC and qBIC modes in a material configuration consisting of a LN thin-film sandwiched between an optically thick gold back- reflector and a grating of gold nanoridges also functioning as control electrodes. Furthermore, we utilize the findings of this investigation to design, fabricate and experimentally characterize a meta- surface for tunable optical free-space intensity modulation. The fabricated electro-optic metasurfaces operate at telecom wavelengths with the modulation depth reaching 95 % combined with an absolute modulation of 35 % for a bias voltage of ±30 V within the electrical bandwidth of 125 MHz. In recent years, several free-space intensity modulators utilizing various active materials have been demonstrated (Supplementary Table S1). We believe that the electro-optic LN metasurface configuration presented

here is attractive due to its highly efficient performance combined with inherently ultrafast responses, making it superior to those based on phase-change materials or MEMS components, while its exceptional environmental stability contrasts starkly to those based on electro-optic polymers with low glass temperatures.

Furthermore, highly angle-dependent qBIC resonances realized with this platform open exciting possibilities for ultrafast, electrically tunable phase contrast imaging that allows one to realize electrically tunable phase contrast imaging and, for example, dynamically adjust edge enhancement effects in imaging applications. The estimated pixel size of 22 um is small enough for implementing sophisticated spatial and temporal modulation of radiation at telecom wavelengths similar to what has been demonstrated with the state-of-the-art ITO-based electrically tunable metasurfaces, but with much larger bandwidths [24]. Finally, given the potential bandwidth of 39 GHz estimated for and in combination with the metasurface pixel size of $22\ \mathrm{\mu m}$, the demonstrated electro-optic metasurfaces promise successful realization of unique optical functions, such as harmonic beam steering and spatiotemporal shaping as well as nonreciprocal operation. Overall, we believe that the demonstrated electro-optic LN metasurfaces based on qBIC resonances open new avenues towards the development of ultrafast, highly efficient and ultrathin flat-optics components for advanced applications involving spatiotemporal control of optical fields.

## Methods
### Simulation
Simulations are performed in the commercially available finite element software COMSOL Multiphysics, ver. 6.2. Given that the grating design is constant (semi-infinite) in the $y$-direction, all simulations are performed for 2D models. Due to the significant thickness of the chromium adhesion layer (10 nm), and our inability to alter it, we include it in the optical simulations, even though adhesion layers are typically not modelled. Interpolated values are used for the permittivity of chromium [47], LN [48], and gold [49]. For the infinite model simulations we simply calculate one period of the grating with one nanoridge (or two nanoridges for the asymmetric grating) and add periodic boundary conditions to the sidewalls of the model domain. For the finite model, we model the whole grating and truncate the domain with perfectly matched layers to eliminate reflection from boundaries. Wave excitation and measuring is done using ports. An electro-optic simulation is performed in two steps: First, the electric field distribution from an applied DC voltage is determined in an electrostatic simulation. Second, the change of refractive index is calculated from the electric field distribution and the Pockels coefficients of Jazbinšek et al. [32] (considering only the largest diagonal terms, i.e., $\Delta n_{i}=-\frac{1}{2}n_{i}^{3}r_{iiz}E_{z}$, with $r_{x x z}=r_{y y z}=10.12\ \mathrm{pm/V}$ and $r_{z z z}=31.45\ \mathrm{pm/V}$), after which the optical simulation is conducted with the updated refractive index. For calculation of the dispersion relation and Q factor, we employ the eigenfrequency solver of COMSOL Multiphysics.

### Fabrication
The device is fabricated using a combination of nanostenciling and electron beam lithography. 5 nm of titanium and 100 nm of gold is deposited by thermal evaporation through a shadow mask to form macroscopic electrodes. A $\sim 200\ \mathrm{nm}$ layer of PMMA 950K A4 resist is spin-coated, and the modulator is manually aligned to the macroscopic electrode and exposed using electron beam lithography at 30 kV. The resist is developed, and the modulator is formed by evaporation of 3 nm of titanium and 75 nm of gold followed by liftoff in acetone. The grating array consists of 120 periods, and it measures $90\ \mathrm{\mu m}\times60\ \mathrm{\mu m}$.

### Electro-optic characterization

The sample was mounted on a homemade sample holder, with an attached commercial probe (GGB, Model 40A-GSG-750, working range: DC - 40 GHz) used for connection to the upper electrode (the grating), while to connect to the bottom electrode a conductive paste is applied to the edge of the sample. The sample holder was mounted on a 3D stage. For characterization of the passive device, a collimated supercontinuum laser beam (NKT Photonics SuperK Extreme) is used in combination with a spectrometer to get the full spectral response, whereas for the characterization of the active device, a collimated low-power continuous-wave laser beam from a tunable telecom laser (New Focus Venturi) is used. The polarization of the incident light is controlled by a Glan-Thompson polarizer, and a beam splitter is used for the sample illumination, placed between the sample and the objective in the collection part, to maximally resemble the plane wave incidence. The reflected light is collected by a 20X objective, spatially filtered with a pinhole to reduce the background noise and further carried to the photodetector or spectrometer. The measurements of the modulation depth are performed at relatively low frequencies ($\sim 200$ kHz), with the modulating signals supplied by a homemade function generator and measured with an oscilloscope (bandwidth of 200 MHz). Electrical bandwidth is determined using a high-speed photodetector and RF spectrum analyzer with high sensitivity.

**Research funding:** C.D.-C. and S.I.B. acknowledge financial support from Villum Fonden (Award in Technical and Natural Sciences 2019). T.Y. acknowledges the support from the Center for Polariton-driven Light-Matter Interactions (POLIMA) funded by the Danish National Research Foundation (Project No. DNRF165).

**Conflict of interest statement:** The authors declare no conflicts of interest.

### References

[1] M. Thomaschewski and S. I. Bozhevolnyi, “Pockels modulation in integrated nanophotonics,” *Applied Physics Reviews*, vol. 9, p. 021311, June 2022.

[2] G. Sinatkas, T. Christopoulos, O. Tsilipakos, and E. E. Kriezis, “Electro-optic modulation in integrated photonics,” *Journal of Applied Physics*, vol. 130, p. 010901, July 2021.

[3] M. Y. Shalaginov, S. D. Campbell, S. An, Y. Zhang, C. Ríos, E. B. Whiting, Y. Wu, L. Kang, B. Zheng, C. Fowler, H. Zhang, D. H. Werner, J. Hu, and T. Gu, “Design for quality: reconfigurable flat optics based on active metasurfaces,” *Nanophotonics*, vol. 9, pp. 3505–3534, July 2020.

[4] Y. Che, X. Wang, Q. Song, Y. Zhu, and S. Xiao, “Tunable optical metasurfaces enabled by multiple modulation mechanisms,” *Nanophotonics*, vol. 9, pp. 4407–4431, Oct. 2020.

[5] A. Smolyaninov, A. E. Amili, F. Vallini, S. Pappert, and Y. Fainman, “Programmable plasmonic phase modulation of free-space wavefronts at gigahertz rates,” *Nat. Photonics*, vol. 13, pp. 431–435, Feb. 2019.

[6] I.-C. Benea-Chelmus, M. L. Meretska, D. L. Elder, M. Tamagnone, L. R. Dalton, and F. Capasso, “Electro-optic spatial light modulator from an engineered organic layer,” *Nature Communications*, vol. 12, p. 5928, Oct 2021.

[7] J. Park, B. G. Jeong, S. I. Kim, D. Lee, J. Kim, C. Shin, C. B. Lee, T. Otsuka, J. Kyoung, S. Kim, K.-Y. Yang, Y.-Y. Park, J. Lee, I. Hwang, J. Jang, S. H. Song, M. L. Brongersma, K. Ha, S.-W. Hwang, H. Choo, and B. L. Choi, “All-solid-state spatial light modulator with independent phase and amplitude control for three-dimensional LiDAR applications,” *Nature Nanotechnology*, vol. 16, pp. 69–76, Oct. 2020.

[8] B. Schwarz, “Mapping the world in 3d,” *Nat. Photonics*, vol. 4, pp. 429–430, July 2010.

[9] I. W. Jung, D. Lopez, Z. Qiu, and W. Piyawattanametha, "2-d MEMS scanner for handheld multispectral dual-axis confocal microscopes," *J. Microelectromech. Syst.*, vol. 27, pp. 605-612, Aug. 2018.

[10] M. Gopakumar, G.-Y. Lee, S. Choi, B. Chao, Y. Peng, J. Kim, and G. Wetzstein, "Full- colour 3d holographic augmented-reality displays with metasurface waveguides," *Nature*, vol. 629, p. 791-797, May 2024.

[11] W.-J. Joo and M. L. Brongersma, "Creating the ultimate virtual reality display," *Science*, vol. 377, no. 6613, pp. 1376-1378, 2022.

[12] A. She, S. Zhang, S. Shian, D. R. Clarke, and F. Capasso, "Adaptive metalenses with simulta- neous electrical control of focal length, astigmatism, and shift," *Science Advances*, vol. 4, no. 2, p. eaap9957, 2018.

[13] X. Li, L. Wei, R. H. Poelma, S. Vollebregt, J. Wei, H. P. Urbach, P. M. Sarro, and G. Q. Zhang, "Stretchable binary fresnel lens for focus tuning," *Scientific Reports*, vol. 6, p. 25348, May 2016.

[14] Y. Wang, P. Landreman, D. Schoen, K. Okabe, A. Marshall, U. Celano, H.-S. P. Wong, J. Park, and M. L. Brongersma, "Electrical tuning of phase-change antennas and metasurfaces," *Nature Nanotechnology*, vol. 16, pp. 667-672, Apr. 2021.

[15] Y. Zhang, C. Fowler, J. Liang, B. Azhar, M. Y. Shalaginov, S. Deckoff-Jones, S. An, J. B. Chou, C. M. Roberts, V. Liberman, M. Kang, C. Ríos, K. A. Richardson, C. Rivero-Baleine, T. Gu, H. Zhang, and J. Hu, "Electrically reconfigurable non-volatile metasurface using low-loss optical phase-change material," *Nature Nanotechnology*, vol. 16, pp. 661-666, Apr. 2021.

[16] S. Abdollahramezani, O. Hemmatyar, M. Taghinejad, H. Taghinejad, A. Krasnok, A. A. Eftekhar, C. Teichrib, S. Deshmukh, M. A. El-Sayed, E. Pop, M. Wuttig, A. Alù, W. Cai, and A. Adibi, "Electrically driven reprogrammable phase-change metasurface reaching 80% efficiency," *Nature Communications*, vol. 13, p. 1696, Mar. 2022.

[17] N. Sharma, J. Bar-David, N. Mazurski, and U. Levy, "Metasurfaces for enhancing light absorption in thermoelectric photodetectors," *ACS Photonics*, vol. 7, pp. 2468-2473, July 2020.

[18] M. Rahmani, L. Xu, A. E. Miroshnichenko, A. Komar, R. Camacho-Morales, H. Chen, Y. Zárate, S. Kruk, G. Zhang, D. N. Neshev, and Y. S. Kivshar, "Reversible thermal tuning of all-dielectric metasurfaces," *Advanced Functional Materials*, vol. 27, p. 1700580, July 2017.

[19] C. Meng, P. C. V. Thrane, F. Ding, J. Gjessing, M. Thomaschewski, C. Wu, C. Dirdal, and S. I. Bozhevolnyi, "Dynamic piezoelectric mems-based optical metasurfaces," *Science Advances*, vol. 7, no. 26, p. eabg5639, 2021.

[20] C. Meng, P. C. V. Thrane, F. Ding, and S. I. Bozhevolnyi, "Full-range birefringence control with piezoelectric mems-based metasurfaces," *Nature Communications*, vol. 13, p. 2071, Apr 2022.

[21] E. Arbabi, A. Arbabi, S. M. Kamali, Y. Horie, M. Faraji-Dana, and A. Faraon, "Mems-tunable dielectric metasurface lens," *Nature Communications*, vol. 9, p. 812, Feb 2018.

[22] G. K. Shirmanesh, R. Sokhoyan, P. C. Wu, and H. A. Atwater, "Electro-optically tunable multi- functional metasurfaces," *ACS Nano*, vol. 14, pp. 6912-6920, Apr. 2020.

[23] J. Park, J.-H. Kang, X. Liu, and M. L. Brongersma, "Electrically tunable epsilon-near-zero (enz) metafilm absorbers," *Scientific Reports*, vol. 5, Nov. 2015.

[24] J. Sisler, P. Thureja, M. Y. Grajower, R. Sokhoyan, I. Huang, and H. A. Atwater, "Electrically tunable space-time metasurfaces at optical frequencies," *Nature Nanotechnology*, July 2024.

[25] I.-C. Benea-Chelmus, S. Mason, M. L. Meretska, D. L. Elder, D. Kazakov, A. Shams-Ansari, L. R. Dalton, and F. Capasso, "Gigahertz free-space electro-optic modulators based on mie resonances," *Nature Communications*, vol. 13, p. 3170, June 2022.

[26] J. Zhang, Y. Kosugi, M. Ogasawara, K. Ariu, A. Otomo, T. Yamada, Y. Nakano, and T. Tanemura, "High-speed metasurface modulator using perfectly absorptive bimodal plasmonic resonance," *APL Photonics*, vol. 8, Dec. 2023.

[27] K. Alexander, J. P. George, J. Verbist, K. Neyts, B. Kuyken, D. Van Thourhout, and J. Beeckman, "Nanophotonic pockels modulators on a silicon nitride platform," *Nature Communications*, vol. 9, p. 3444, Aug 2018.

[28] T. Yezekyan, M. Thomaschewski, P. C. V. Thrane, and S. I. Bozhevolnyi, "Plasmonic electro-optic modulators on lead zirconate titanate platform," *Nanophotonics*, vol. 0, Mar. 2024.

[29] M. Thomaschewski, V. A. Zenin, C. Wolff, and S. I. Bozhevolnyi, "Plasmonic monolithic lithium niobate directional coupler switches," *Nat. Commun.*, vol. 11, p. 748, Feb 2020.

[30] J. Liu, L. Qu, W. Wu, C. Jin, Z. Chen, Z. Gu, W. Liu, C. Wang, D. Zheng, H. Liu, W. Cai, M. Ren, and J. Xu, "Lithium niobate thin film electro-optic modulator," *Nanophotonics*, vol. 13, p. 1503-1508, Feb. 2024.

[31] C. Damgaard-Carstensen, M. Thomaschewski, and S. I. Bozhevolnyi, "Electro-optic metasurface- based free-space modulators," *Nanoscale*, vol. 14, no. 31, pp. 11407-11414, 2022.

[32] M. Jazbinšek and M. Zgonik, "Material tensor parameters of ${\rm LiNbO_3}$ relevant for electro- and elasto-optics," *Appl. Phys. B: Lasers Opt.*, vol. 74, pp. 407-414, Apr. 2002.

[33] R. S. Weis and T. K. Gaylord, "Lithium niobate: Summary of physical properties and crystal structure," *Appl. Phys. A: Solids Surf.*, vol. 37, pp. 191-203, Aug. 1985.

[34] M. Zhang, C. Wang, P. Kharel, D. Zhu, and M. Lončar, "Integrated lithium niobate electro-optic modulators: when performance meets scalability," *Optica*, vol. 8, p. 652, May 2021.

[35] B. Gao, M. Ren, W. Wu, W. Cai, and J. Xu, "Electro-optic lithium niobate metasurfaces," *Sci. China: Phys., Mech. Astron.*, vol. 64, p. 240362, Feb 2021.

[36] H. Weigand, V. V. Vogler-Neuling, M. R. Escalé, D. Pohl, F. U. Richter, A. Karvounis, F. Timpu, and R. Grange, "Enhanced electro-optic modulation in resonant metasurfaces of lithium niobate," *ACS Photonics*, vol. 8, pp. 3004-3009, Sept. 2021.

[37] C. Damgaard-Carstensen, M. Thomaschewski, F. Ding, and S. I. Bozhevolnyi, "Electrical tuning of fresnel lens in reflection," *ACS Photonics*, vol. 8, pp. 1576-1581, June 2021.

[38] C. Damgaard-Carstensen and S. I. Bozhevolnyi, "Nonlocal electro-optic metasurfaces for free-space light modulation," *Nanophotonics*, vol. 12, p. 2953-2962, Apr. 2023.

[39] T. Yezekyan, S. Boroviks, O. J. F. Martin, and S. I. Bozhevolnyi, "Engineering quasi-bound states in the continuum in asymmetric waveguide gratings," *New Journal of Physics*, vol. 26, p. 093027, Sept. 2024.

[40] M. Cotrufo, A. Cordaro, D. L. Sounas, A. Polman, and A. Alù, "Passive bias-free non-reciprocal metasurfaces based on thermally nonlinear quasi-bound states in the continuum," *Nature Photon- ics*, vol. 18, pp. 81-90, Jan 2024.

[41] L. Huang, R. Jin, C. Zhou, G. Li, L. Xu, A. Overvig, F. Deng, X. Chen, W. Lu, A. Alù, and A. E. Miroshnichenko, "Ultrahigh-q guided mode resonances in an all-dielectric metasurface," *Nature Communications*, vol. 14, June 2023.

[42] S. I. Azzam, V. M. Shalaev, A. Boltasseva, and A. V. Kildishev, "Formation of bound states in the continuum in hybrid plasmonic-photonic systems," *Physical Review Letters*, vol. 121, Dec. 2018.

[43] C. Wu, B. Neuner, G. Shvets, J. John, A. Milder, B. Zollars, and S. Savoy, "Large-area wide-angle spectrally selective plasmonic absorber," *Physical Review B*, vol. 84, p. 075102, Aug. 2011.

[44] A. M. Shaltout, V. M. Shalaev, and M. L. Brongersma, "Spatiotemporal light control with active metasurfaces," *Science*, vol. 364, no. 6441, p. eaat3100, 2019.

[45] A. Weiss, C. Frydendahl, J. Bar-David, R. Zektzer, E. Edrei, J. Engelberg, N. Mazurski, B. Desi- atov, and U. Levy, "Tunable metasurface using thin-film lithium niobate in the telecom regime," *ACS Photonics*, vol. 9, pp. 605-612, Jan. 2022.

[46] A. Ji, J.-H. Song, Q. Li, F. Xu, C.-T. Tsai, R. C. Tiberio, B. Cui, P. Lalanne, P. G. Kik, D. A. B. Miller, and M. L. Brongersma, "Quantitative phase contrast imaging with a nonlocal angle-selective metasurface," *Nature Communications*, vol. 13, Dec. 2022.

[47] P. Johnson and R. Christy, "Optical constants of transition metals: Ti, v, cr, mn, fe, co, ni, and pd," *Phys. Rev. B*, vol. 9, pp. 5056-5070, June 1974.

[48] D. E. Zelmon, D. L. Small, and D. Jundt, "Infrared corrected sellmeier coefficients for congruently grown lithium niobate and 5 mol% magnesium oxide -doped lithium niobate," *J. Opt. Soc. Am. B*, vol. 14, p. 3319, Dec. 1997.

[49] A. D. Rakić, A. B. Djurišić, J. M. Elazar, and M. L. Majewski, "Optical properties of metallic films for vertical-cavity optoelectronic devices," *Appl. Opt.*, vol. 37, pp. 5271-5283, Aug 1998.