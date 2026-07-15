# Holographic edge-illuminated polymer Bragg gratings for dense wavelength division optical filters at 1550 nm

Atsushi Sato$^\text{a}$, Miodrag Scepanovic$^\text{b}$, Raymond K. Kostuk$^\text{b}$

$^\text{a}$Toppan Printing Co., Ltd. , Japan
$^\text{b}$ECE & Optical Science Center, University of Arizona, Tucson, AZ 85721

## ABSTRACT

To meet the requirements of DWDM spectral filters at 1550nm, we suggest a new design for holographic Bragg gratings in photopolymers. The design is based on an edge-illuminated hologram configuration. Using this configuration, it is not difficult to make a very long grating and to apply apodization to the grating profile. A larger range of filter functions can be realized by cascading several gratings with different properties or by combining the gratings with other planar optical elements. Here, we show both simulated and experimental results using this arrangement. Rouard's method is used to examine the properties of apodized grating, and the results indicate the potential for narrow spectral bandwidths and high side lobe suppression. Experimental results with two types of photopolymer, Aprilis ULSH-500-7A and Phenanthrenequinone-doped PMMA, provide evidence of the effectiveness of this arrangement.

Keywords: Optical communication, DWDM, Bragg grating, photopolymer

## 1. INTRODUCTION

Dense wavelength division multiplexing (DWDM) systems require the control of narrowly spaced spectral bands within the fiber transmission window. Various types of optical filters have been developed for this purpose. The important requirements for DWDM spectral filters include narrow spectral line-widths (=0.2 nm for 25GHz separation), low loss (<0.1 dB), high side lobe suppression (<-30 dB), and minimal polarization dependent loss (PDL < 0.2 dB).$^{1,2}$ Other filter operations are also required for the DWDM system tasks such as gain equalization and dispersion compensation. At the present time dielectric thin film reflection stacks, arrayed waveguide gratings (AWGs),$^3$ and fiber Bragg gratings (FBGs)$^4$ are the primary forms of narrow band spectral filters used in fiber optic communications systems. Although these device types are important for modern fiber optic systems, other approaches$^{5,6}$ of implementing spectral filters are sought to provide more design options and to reduce manufacturing costs.

In this paper, we present a new design for holographic Bragg gratings in photosensitive polymers to realize DWDM narrow band spectral filters. The design is based on an edge-illuminated hologram configuration. Using this arrangement, it is not difficult to make very long gratings and to apply apodization to the grating profile. Also, a larger range of filter functions can be realized by cascading several gratings with different properties or by combining the gratings with other planar optical elements. The design is analyzed using coupled wave and dielectric layer analytical techniques, and supporting experimental data is provided. Both Aprilis ULSH-500-7A$^{7,8,9}$ photopolymer and Phenanthrenequinone-doped Polymethyl methacrylate (PQ/PMMA) material$^{10,11}$ are used for the experiments.

## 2. DESIGN OF THE EDGE-ILLUMINATED POLYMER BRAGG GRATING

Fig.1 shows the basic concept of the holographic edge-illuminated polymer Bragg grating. The grating is recorded by the interference pattern of two beams coming from the one side of the material (as shown in Fig.1). Therefore, it is recorded as an unslanted transmission grating, and it is used as a reflection grating with edge illumination. The micro lenses and optical surfaces are used to couple the light into the grating. The lens waveguide overlaps with the edge-illuminated grating. Only light that satisfies the Bragg condition will be diffracted (reflected) by the grating.

At first, we will discuss the required length, L, of the grating. For a constant index profile grating, the diffraction efficiency, $\eta$, of an unslanted reflection grating can be determined using the approximate coupled wave expression$^{12}$


$$
L_{\eta}=\frac{\lambda_{B}}{\pi \Delta n} \tanh ^{-1}(\sqrt{\eta})
\tag{1}
$$

where $L_{\eta}$ is the grating length required to obtain a diffraction efficiency of $\eta$, $\Delta n$ is the index modulation, and $\lambda_{B}$ is the Bragg wavelength of the grating. The length of the grating $L_{s}$ required to obtain a specific filter spectral bandwidth $\Delta \lambda$ is given as $^{13}$

$$
L_{S}=\frac{\lambda_{B}^{2}}{\left[(n \Delta \lambda)^{2}-\left(\Delta n \lambda_{B}\right)^{2}\right]^{1 / 2}}
\tag{2}
$$

with n equal to the average refractive index of the photopolymer. In the case of $\Delta n<<\lambda_{B} / L_{S}$, equation (2) can be simplified as

$$
L_{S}=\frac{\lambda_{B}^{2}}{n \Delta \lambda}
\tag{3}
$$

Using these expressions, an average refractive index of 1.5, a Bragg wavelength of 1550nm, a grating length of 8.0 mm, and a refractive index modulation of $1.5 \mathrm{x} 10^{-4}$ satisfy the requirements of $\Delta \lambda=0.2 \mathrm{nm}$ and $\eta=97 \%(0.1 \mathrm{~dB}$ loss). It is difficult to achieve a grating thickness of 8.0mm. Light absorption during the recording of the grating may result in inhomogeneous grating strength along the thickness of the material. On the other hand, an 8.0mm long grating is easy to record when the plane of incidence is normal to the substrate surface. The refractive index modulation of $1.5 \mathrm{x} 10^{-4}$ is relatively easy to achieve with most of holographic materials.

![](./images/812380255800000513_1.jpg)

Fig. 1 The schematics of the edge-illuminated polymer Bragg grating

Next, we will consider the required thickness of the material. To minimize the optical power loss in the grating, the lens waveguide should confine the optical beam within the thickness of the polymer. The overlap can be improved by placing the grating in the region of minimum beam waist. In our design, we will restrict the length of the grating to the Rayleigh range of the Gaussian beam. $^{14}$ The divergence angle $\theta$ (half angle) of the Gaussian beam is given by the relation

$$
\theta=\frac{\lambda}{\pi n \omega}
\tag{4}
$$

where $\omega$ is the radius of the beam at the $1 / \exp ^{2}$ power points. The Rayleigh range for a Gaussian beam is given by

$$
Z_{R}=\frac{2 \omega}{\theta}
\tag{5}
$$

The corresponding thickness of the grating layer T should be

Proc. of SPIE Vol. 5005 423

$$
T \geq \sqrt{2}(2 \omega)=\sqrt{2}\left(\theta Z_{R}\right)=2\left(\frac{\lambda L}{\pi n}\right)^{1 / 2} \tag{6}
$$

where the Rayleigh range $Z_R$ is replaced with the length of the grating L, which meets both the diffraction efficiency and the spectral selectivity requirements. For our system operating at 1.55 mm, with a refractive index near 1.5, and a grating length of 8.0 mm, the thickness of the photopolymer should be approximately 100µm. The material thickness of 100µm is available in some commercialized photopolymers like Aprilis USLH series.

Apodization of the grating profile may be used to suppress the sideband peaks. It is well known that in the case of constant index profile grating, there are many sideband peaks in the spectral response. A sinc function grating profile is ideal not only to suppress sidebands but also to achieve the flat top filter response. A Gaussian or one of several other profiles⁴ may also be used for apodization. It must be taken into account that the apodization of the grating profile results in shorter effective length than the constant index profile grating. Therefore we need a longer grating than equations (1) and (3) suggest, and we also need a thicker material than equation (6) shows.

In the case of a Gaussian apodization profile, Gaussian function can be expressed

$$
A(x)=\exp \left[-\varepsilon\left(\frac{x}{L}\right)^{2}\right] \tag{7}
$$

The parameter $\varepsilon$ determines how rapidly the profile changes and x specifies the position along the length of the grating L. Smaller values of $\varepsilon$ produce longer effective grating lengths. The corresponding refractive index profile for a grating modulated in the x-direction is given by

$$
\begin{aligned}
&n(x)=n_{\text {д }}+\Delta n(x) \cos (\underline{K} \cdot \underline{x}) \\
&\Delta n(x)=A(x) \Delta n_{\text {max }}
\end{aligned} \tag{8}
$$

where n is the average refractive index of the holographic material, $\Delta n_{max}$ is the peak index modulation, and $\underline{K}$ is the grating vector. Using equation (7), the effective grating length $L_{eff}$ can be expressed

$$
L_{e f f}=\int_{-L / 2}^{L / 2} A(x) d x=e r f\left(\frac{\sqrt{\varepsilon}}{2}\right) \frac{\sqrt{\pi} L}{\sqrt{\varepsilon}} \tag{9}
$$

Here, erf(t) is the error function, which is defined as

$$
\operatorname{erf}(t)=\frac{2}{\sqrt{\pi}} \int_{0}^{t} \exp \left(-s^{2}\right) d s \tag{10}
$$

Fig.2 shows the value of $L_{eff}$ /L versus $\varepsilon$. For example, in the case of $\varepsilon$ = 9.0, the grating length, L, is 14.0 mm ($L_{eff}$ is about 57% of L), $\Delta n_{max}$=1.5x10⁻⁴, and thickness, T, is about 136 µm. Fig.3 shows the grating profile that has these parameters.

![](./images/812380255800000513_2.jpg)

Fig. 2 The change of the effective length $L_{\text{eff}}$ of the Gaussian apodized grating by the parameter $\varepsilon$

![](./images/812380255800000513_3.jpg)

Fig. 3 Refractive index modulation of a grating with the Gaussian profile. The grating length L = 14.0 mm, grating pitch $\Lambda$ = 517nm (enlarged in the graph), average refractive index n =1.5, peak refractive index modulation $\Delta\text{n}_{\text{max}}$ = $1.5\text{x}10^{-4}$ and Gaussian profile parameter $\varepsilon$ = 9.0.

### 3. SIMULATION OF THE APODIZED GRATING

Rouard's method$^{15,16,17}$ was used to simulate the spectral response of the apodized Bragg grating. Fig.4 shows the results for a grating pitch $\Lambda$ of 517 nm, which is required to select wavelengths in the 1550 nm region, a grating length L of 14.0 mm, average refractive index n of 1.5, $\Delta\text{n}_{\text{max}}$ of $1.5\text{x}10^{-4}$, and a Gaussian apodization parameter $\varepsilon$ of 9.0 corresponding to the grating shown in Fig.3. The solid curve shows the reflectance when the beam is normally incident on the grating and the dashed curve shows reflectance when the beam is incident at an angle of 0.39 degrees with TE polarization. This angle corresponds to the divergence angle for the 14.0 mm Rayleigh range of a Gaussian mode at a wavelength of 1550 nm. In this case, the peak reflectance is 97%, full width half maximum (FWHM) is 0.17 nm, and the side lobe peaks are less than -30 dB. The difference in Bragg wavelength due to the divergence angle is only 0.02

Proc. of SPIE Vol. 5005 425

nm. Additionally, at the incidence angle of 0.39 degrees, the variation in peak reflectance is less than –30dB for TE and TM polarization. This simulation result satisfies the DWDM filter requirements.

![](./images/812380255800000513_4.jpg)

Fig. 4 Simulated spectral reflectance of the grating, which is illustrated in Figure 3. The solid line shows the reflectance when incident light angle is 0 degrees, and the dotted line shows it at 0.39 degrees. The peak reflectance at Bragg condition is -0.1dB (97%), FWHM = 0.17nm, all sideband peaks are less than –30dB. The difference between two Bragg wavelengths is 0.02nm.

Fig.5 shows the spectral reflectance when the absorption of the material is included. To get the diffraction efficiency $\eta > 97\%$, required peak refractive index modulation, $\Delta n_{\text{max}}$, is $1.9\text{x}10^{-4}$, the acceptable value of the absorption coefficient is 0.03 /cm at 1550nm for a 14.0mm long grating. This requirement might be critical for the photopolymer materials. Larger absorption results in a wider bandwidth, and the balance between grating length, bandwidth, and absorption loss must be considered when designing the grating.

![](./images/812380255800000513_5.jpg)

Fig. 5 Simulated spectral reflectance of the grating with an absorption coefficient of 0.03 /cm.

### 4. EXPERIMENTS

The basic properties of the edge-illuminated holographic Bragg filter were evaluated using both Aprilis ULSH 500-7A photopolymer and PQ/PMMA material.

### 4-1 TEST USING APRILIS MATERIAL

A prism coupler was used to measure the refractive index of the material. ULSH500-7A photopolymer material was found to have a refractive index of 1.4956 at 1550nm after fixing. The intensity absorption coefficient of the material was calculated from the transmittance at 1550nm. After compensation for reflection loss and absorption loss in the substrate, the absorption coefficient was found to be 1.9 /cm at 1550nm. The edge-illuminated hologram was recorded using 2 beam inference with exposure conditions chosen to optimize the grating pitch and refractive index modulation. The inter beam angle was 59.5 degrees and the recording wavelength was 514.5nm.

We estimated the peak refractive index modulation using the theoretical model to curve fit the experimental data. Kubota's analysis¹⁸ was used as a theoretical model, which is the two-wave coupled wave theory¹² combined with an attenuated index modulation profile as a function of grating depth. The angular dependence of the diffraction efficiency of the grating, when used as an unslanted transmission grating with reconstruction wavelength of 632.8nm, was measured using the geometry shown in Fig. 6. The estimated value of maximum refractive index modulation is 0.01 for ULSH500-7A for a grating recorded with an exposure of 50mJ/cm².

![](./images/812380255800000513_6.jpg)

Fig. 6 The geometry to measure the angular dependence of the diffraction efficiency of the edge-illuminated grating used as an unslanted transmission grating.

Although the absorption of the Aprilis ULSH-500-7A photopolymer was high, we were able to determine the basic spectral filtering properties of the edge-illuminated hologram using the experimental set-up shown in Fig. 7.

![](./images/812380255800000513_7.jpg)

Fig. 7 The geometry used to measure the spectral transmittance using two prisms.

Proc. of SPIE Vol. 5005 427

Here, the wavelength tunable semiconductor laser was used as the light source. Two 45-90-45 degrees prisms are index matched to the glass substrates surrounding the photopolymer and serve as a coupling interface to the material. Changing the angle of incidence of the beam relative to the prism surface allows us to change the effective propagation length within the grating. Fig. 8 shows the spectral transmittance of an edge-illuminated holographic filter with the probe beam passing through a 1.3 mm length of the grating. Also shown is the calculated transmittance based on Rouard's method. The measured transmittance dip was 7.8dB and FWHM of the transmittance spectrum is 0.6 nm and agrees well with the theoretical transmittance for this grating.

![](./images/812380255800000513_8.jpg)

Fig. 8 The measured spectral transmittance of the grating with Aprilis USLH500-7A.

The edge-illuminated hologram allows the formation of apodized refractive index grating profiles. To demonstrate this property, a hologram was exposed with the near Gaussian intensity profile of an expanded laser beam to create an apodized unslanted transmission grating. After exposing and fixing the material, the diffraction efficiency across the aperture of the apodized grating was measured with a 632.8 nm probe beam as a function of position along the aperture As shown in Fig. 9, nearly perfect Gaussian profile of the grating could be obtained.

![](./images/812380255800000513_9.jpg)

Fig. 9 The measured grating profile (o) and the fitted Gaussian (solid line).

### 4-2 TEST USING PQ/PMMA MATERIAL

The PQ/PMMA material has some unique features, such are 1) low shrinkage, 2) low absorption and scattering loss, and 3) a variety of possible geometries can be formed by molding the material. It has relatively low sensitivity and low maximum refractive index modulation. We prepared 2.2mm thick samples of this material, using bulk polymerization method following the references. $^{10,11}$

The PQ/PMMA has a refractive index of 1.4781 at 1550nm, which was measured with a prism coupler. The absorption coefficient, calculated from a transmittance, was 0.21 /cm at 1550nm. As in the test using Aprilis material, the edge-illuminated hologram was recorded by 2 beam inference. In this case, the inter beam angle was 55.5 degrees with a recording wavelength of 488nm.

The estimated peak refractive index modulation was $1.5x10^{-4}$ at the exposure level of $900mJ/cm^{2}$.

The spectral response of the edge-illuminated holographic Bragg filter configuration (as shown in Fig.1) was measured by wavelength tunable semiconductor laser. In the measurement, an objective lens instead of a micro lens was used to couple light from the fiber into the grating. Fig.10 shows the spectral transmittance of a 5.0 mm long grating. The measured transmittance dip was 2.4dB and FWHM was about 0.7 nm. Although the grating length is much longer than that of the grating recorded in Aprilis photopolymer, the results show a lower transmittance dip and a wider bandwidth. This result may be due to the chirping of the grating pitch, which could have occurred during post-exposure bake. This area of research is currently being investigated.

![](./images/812380255800000513_10.jpg)

Fig. 10 The spectral transmittance of the grating with PQ/PMMA material. The grating length is 5.0 mm.

### 5. CONCLUSION

We suggested an edge-illuminated polymer Bragg filter configuration. The advantages of this configuration include: 1) the ability to implement gratings with large interaction lengths in relatively thin photopolymer samples (100-200 mm), 2) easy formation of apodized gratings to suppress spectral sidebands, 3) the ability to form cascaded grating systems to implement different filter functions, and 4) the ability to form reflection gratings using a transmission interference pattern.

We showed the design method of a Bragg grating filter including apodization using coupled wave analysis. We also showed simulated results using Rouard's method. These investigations indicated: 1) a 14mm grating length is needed to get 0.2 nm spectral bandwidth with Gaussian apodization, 2) a refractive index modulation of 0.00015 is needed to achieve 97% diffraction efficiency, and 3) an absorption coefficient of 0.03 /cm or less is needed for acceptable light intensity loss.

Proc. of SPIE Vol. 5005 429

The Aprilis ULSH-500-7A photopolymer and PQ/PMMA materials were tested for this application. Although the material absorption was high in both materials, we were able to demonstrate narrow band filter operation ($\approx$0.6 nm FWHM) and the ability to apodize edge-illuminated holograms. Some optimization of the material preparation and/or post-exposure procedure may reduce the absorption loss. If the absorption can be reduced, holographic photopolymers may prove a viable alternative to fiber Bragg gratings for implementing a wide range of spectral filters for optical communication.

# REFERENCE

1.  G. Castanon, O. Vassilieva, S. Choudhary, and T. Hoshida, "Requirement of filter characteristics for 40 Gbit/s-based DWDM systems," in Proc. 27th Eur. Conf. on Opt. Comm. (ECOC'01- Amsterdam), pp.60-61, IEEE , NY, 2001.
2.  N. Makeda, A. AL- Hamdan, T.H. Chong, and D.G. Dout, "Polarizatio independent, linear- tuned interference filter with constant transmission characteristics over 1530- 1570-nm tuning range," IEEE Photon. Technol. Lett. **9**, 783-784, 1997.
3.  R. Ramaswami and K. N. Sivarajan, *Optical Networks*, A Practical Perspective, 2nd Ed., Ch. 3, Morgan Kaufmann Publishers, San Francisco, 2002.
4.  R.Kashyap, *Fiber Bragg Gratings*, Academic press, San Diego, 1999.
5.  J. Qiao, F. Zhao, J. Liu, and R. T. Chen, "Dispersion enhanced volume hologram for dense wavelength division demultiplexer," IEEE Photonics Tech. Lett. **12**, 1070-1072, 2000.
6.  P. Boffi, M. C. Ubaldi, D. Piccinin, C. Frascolla, and M. Martinelli, "1550 nm volume holography for optical communication devices," IEEE Photonics Tech. Lett. **12**, 1355-1357, 2000.
7.  D.A.Waldman, R.T.Ingwall, P.K.Dhal, M.G.Horner, E.S.Kolb, H.-Y.S.Li, R.A.Minns, and H.G.Schild, "Cationic ring-opening photopolymerization methods for volume hologram recording", in Diffractive and Holographic Optics Technology III , I Cindrich and S H Lee, eds., Proc. SPIE 2689, 127-141, 1996.
8.  D.A.Waldman and H.-Y.S.Li , "Determination of low-transverse shrinkage in slant fringe gratings of a cationic ring-opening volume hologram recording material", in Diffractive and Holographic Device Technologies and Applications IV, I Cindrich and S H Lee, eds., Proc. SPIE 3010, 354-372, 1997.
9.  D.A.Waldman, H.-Y.S.Li, and E.Cetin, "Holographic recording properties in thick films of ULSH-500 photopolymer" in Diffractive and Holographic Device Technologies and Applications V, I Cindrich and S H Lee, eds., Proc. SPIE 3291, 89-103, 1998.
10. G.J.Steckman, I.Solomatine, G.Zhou and D.Psaltis, "Characterization of phenanthrenequinone-doped poly(methyl methacrylate) for holographic memory", Optics Letters, **23**, 1310-1312, 1998.
11. S.H.Lin, K.Y.Hsu, W.Z.Chen and W.T.Whang, "Phenanthrenequinone-doped poly(methyl methacrylate) photopolymer bulk for volume holographic data storage", Optics Letters, **25**, 451-453, 2000.
12. H.Kogelnik, "Coupled wave theory for thick hologram grating", Bell Sys. Tech. J. 48, 2909-2946, 1969.
13. T. Erdogan, ``Fiber grating spectra,'' J. of Lightwave Tech. **15**, 1277-1294, 1997.
14. D. C. O'Shea, *Elements of Modern Optical Design*, Wiley Series in Pure and Applied Optics Wiley-Interscience, New York, 1985, pp.232-234.
15. M. P. Rouard, "Etudes des propertietes optiques des lames metal-liques tres minces," Ann. Phys. (Paris) ser. II 7, 291-384, 1937.
16. L.A.Weller-Brophy and D.G.Hall, "Analysis of waveguide gratings: application of Rouard's method", J.Opt.Soc.Am.A **2**, 863-871, 1985.
17. L.A.Weller-Brophy and D.G.Hall, "Analysis of waveguide gratings: a comparison of the results of Rouard's method and coupled-wave theory", J.Opt.Soc.Am.A **4**, 60-65, 1987.
18. T.Kubota, "Characteristics of thick hologram grating recorded in absorptive medium", Optica Acta 25, 1035-1053, 1978.