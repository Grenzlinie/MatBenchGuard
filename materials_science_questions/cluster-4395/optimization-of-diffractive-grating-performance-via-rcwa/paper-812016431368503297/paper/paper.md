# Low-Loss Surface-Mode Waveguides for Terahertz Si–SiGe Quantum Cascade Lasers

Alfredo De Rossi, Mathieu Carras, and Douglas J. Paul, Senior Member, IEEE

**Abstract**—A new design of low-loss terahertz waveguide for Si–SiGe quantum-cascade lasers (QCLs) is presented. Periodic surface gratings are used to define waveguides without the requirement of cleaved or etched end facets. As Si cleaves along the (111) planes and not in the vertical direction for standard Si (100) substrates, this significantly aids the fabrication of waveguides. Losses down to $2\ \mathrm{cm}^{-1}$ with modal overlap of 0.4 can be achieved for shallow gratings with etched depths of only $0.56\ \mu\mathrm{m}$ for an active material layer thickness of $8\ \mu\mathrm{m}$. Such low loss and high modal overlap is key to any Si–SiGe QCL being realized.

**Index Terms**—Laser, SiGe, silicon, terahertz, waveguide.

## I. INTRODUCTION

THERE is enormous interest in trying to produce a Si-based laser which could leverage the low cost fabrication processes available to silicon technology thereby undercutting the inherent higher costs of III–V lasers [1]. While the indirect bandgap of silicon precludes the efficient recombination of electrons and holes across the bandgap, the unipolar quantum-cascade laser (QCL) concept [2] can be applied to Si–SiGe heterostructures where intersubband transitions are used to engineer population inversion and gain [3], [4]. QCL devices in Si–SiGe are particularly attractive below the optical phonon energy (i.e., at terahertz frequencies) due to the lack of polar optical phonon scattering. The weaker deformation potential scattering results in far weaker temperature dependence of intersubband lifetimes than III–V materials below the optical phonon energy [5], [6] and suggests that a successful laser has the potential to operate at higher temperatures. Hence, a Si–SiGe terahertz QCL could have a number of significant advantages in the emerging terahertz field which includes applications in medical [7] and security imaging [8], nondestructive testing,¹ proteomics and astronomy.

Work has already demonstrated electroluminescence at terahertz frequencies from Si–SiGe intersubband transitions [4], [9]. Due to the high effective mass ($\sim 0.93m_0$ with $m_0$ the free electron mass) of electrons in the tunnelling direction of Si valleys [10], the higher valence band discontinuities [10], and also due to dopant segregation issues with n-type dopants, all work on Si–SiGe QCLs to date has used holes rather than electrons. As Ge has a larger lattice constant that Si, SiGe layers are strained and have a critical thickness above which additional layers cannot be coherently matched to the lattice resulting in defect and dislocation formation [10]. This can be overcome if alternate layers are strain symmetrized, where tensile strained-Si barriers are grown between compressively strained SiGe quantum wells where the layers are designed so that the strain balances over a period which is smaller than the critical thickness of individual layers for the given strain component [10]. To date using strain symmetrization, Si–SiGe quantum cascade active regions with thicknesses up to about $5\mu\mathrm{m}$ have been demonstrated [11] with electroluminescence at 12 meV.

Crucial for the realization of a laser is the ability to fabricate a low-loss waveguide. In the terahertz frequency region this is particularly important as the optical mode can easily be many tens of micrometers in diameter. Surface waves exists at the interface between a dielectric (with positive permittivity $\epsilon_1$) and a metal (with $\epsilon_2 < 0$). As $\epsilon_2$ increases in modulus, the surface wave expands in the dielectric and, for an ideal conductor with infinite conductivity the field is expulsed from the metal and spreads into the dielectric, therefore the localization at the surface is lost. Surface plasmons are surface waves due to the plasmon resonance in metals, which is responsible for negative permittivity below the resonance frequency. At terahertz frequencies, the plasmon resonance is far away and the surface plasmon effect is negligible. It is well known, however, that periodically structured metal surfaces support surface waves [12]. The connection between surface waves in the long wavelength limit and surface plasmons has been established recently [13]. This result make possible the efficient confinement of radiation without the need of a cladding layer. More interestingly, the conductivity of most metals is high in the THz region, therefore propagation losses are expected to be smaller than in the visible and near-infrared spectral domain.

The tight confinement of the optical mode in terahertz lasers is a major problem, as the waveguided mode needs to be squeezed into the active region which is typically less than $10$–$15\ \mu\mathrm{m}$ thick, due to epitaxial growth limitations. Double-plasmon [14] or double metal cladding [15] are now widespread solutions in GaAs QCL terahertz laser technology. Demonstrated terahertz waveguides for potential Si–SiGe lasers have used a metal-like layer of $\mathrm{WSi}_2$ [11], instead of a doped semiconductor layer. The buried silicide layers are produced in a similar fashion to bond-and-etch-back silicon-on-insulator (SOI) and allow wafer scale integration and ease of processing, essential if any QCL is to be manufacturable. Standard

Manuscript received May 20, 2006; revised July 12, 2006. This work was supported in part by the EC IST Programme SHINE (IST-2001-38035).

A. De Rossi and M. Carras are with Thales Research and Technology France, F-91767 Palaiseau cedex, France (e-mail: alfredo.derossi@thalesgroup.com; mathieu.carras@thalesgroup.com).

D. J. Paul is with the Cavendish Laboratory, University of Cambridge, Cambridge CB3 0HE, U.K. (e-mail: dp109@cam.ac.uk).

Color versions of Figs. 1–6 are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/JQE.2006.883496

¹http://www.teraview.co.uk/

doped-SiGe cannot be used for plasmons due to the low mo- bility of holes in Si–SiGe quantum cascade structures, leading to strong absorption and the imaginary part of the refractive index is always lower than the real part for all frequencies. The WSi₂ layer, however, is also lossy, and calculated propagation losses of WSi₂-based waveguides are in the order of 20 cm⁻¹ [16]. This is a major problem in view of demonstrating lasing in SiGe structures, since the expected modal gain is predicted to be significantly lower than GaAs QCLs, presently around 10 cm⁻¹, due to the higher effective mass. In this paper we propose a novel design for SiGe waveguides with very low propagation losses, which would make lasing possible.

## II. MODEL

To date up to 8 μm of SiGe consisting of 5 μm of active quantum cascade Si–SiGe heterolayers have been successfully grown on a 3 μm thick virtual substrate and so this is a sensible starting point to model and determine the waveguide losses. The surface waveguide structure is a relaxed Si₀.₈Ge₀.₂ virtual substrate and spacer layer with typical thickness of around 3 μm followed by the bottom Ohmic contact layer (Si₀.₈Ge₀.₂, thickness $h_{bc} = 200$ nm, doping $N_{bc} = 5 \times 10^{19}$ cm³), the active region (~940 periods of 6.5 nm compressively strained-Si₀.₇Ge₀.₃ quantum wells and 2 nm tensile strained-Si barriers with total thickness $h_{\text{AR}} = 8$ μm) and finally the top Ohmic contact layer (Si₀.₈Ge₀.₂, thickness $h_t = 40$ nm, doping $N_t = 5 \times 10^{19}$ cm³). Silver was chosen to coat the etched grating structure as it has the highest electrical conductivity of any metal and unlike copper does not need a diffusion barrier on a Si or SiGe surface for QCL processing. While copper and aluminium are the standard metals in CMOS processing, in research silver is sometimes used as it does not easily react with or spike into silicon while providing the highest electrical con- ductivity. Any other compatible metal or even a silicide could be used but the losses are reduced for the higher conducting materials and therefore silver was used for modelling purposes.

The structure is defined on the $x-y$ plane and is assumed to be translation-invariant along the $z$ axis (Fig. 1). This is our 2-D model. Of corse, since channel waveguiding is desired for the end-fire QCL, the necessary lateral mode confinement in the $z$ direction is provided by etching the structure in Fig. 1 down to the Si substrate to form a mesa-like strip waveguide pointing in the $x$ direction The relevant field components are $E_x$, $E_y$, and $H_z$ with the propagation direction and periodicity defined along $x$. The study of periodic structures follows the Floquet–Bloch theorem [17]. Therefore, for each real-valued wavevector $k_x$ and for a given photonic band, we calculate a complex eigen-fre- quency $f$ and an eigenmode in the form

$$
\psi(x, y, f)=u(x, y, f) e^{i k_{x} x}. \tag{1}
$$

It is convenient to use the normalized frequency $f_n = f(\Lambda/c)$, with $\Lambda$ the grating period and $c$ the speed of light. All calcu- lations from this point are performed using normalized data, that is the wavevector and distances are expressed in units of the period $\Lambda$. The connection to the terahertz domain is made through the permittivity calculated at $\lambda = 100$ μm. The value for the metal (Silver) is $\epsilon = -1.95\ 10^5 + i2.67\ 10^5$ and was calculated with a Drude model: $\epsilon = \epsilon_\infty(1 + i\sigma/(\omega\epsilon_0))$ and $\sigma = \rho^{-1}/(1 - i\omega\tau)$. The lifetime, $\tau = 40$ fs and resistivity, $\rho = 1.51\ \Omega$cm are chosen according to [18] at room tempera- ture and $\epsilon_\infty = 1$. The complex permittivity for doped silicon was computed from data given in [16], the damping parameter 110 meV, corresponding to $\tau = 38$ fs, and the effective mass calculated using $m^*=(m_{hh}^{1.5}+m_{lh}^{1.5})/(mhh^{0.5}+m_{lh}^{0.5})$ also given in [16] which gives: $m^*=0.37m_0$. The resistivity is cal- culated using $\rho^{-1}=e^2N\tau/\epsilon_\infty m^*m_0$, with $N$ the doping. The dispersion curve (frequency versus wavevector) is calculated by a plane wave expansion method, using the Fourier factoriza- tion and the S-matrix representation as discussed in [19]–[22]. We consider a grating with a square profile since it is easy to fabricate.

![](./images/812016431368503297_1.jpg)

Fig. 1. Schematic diagram showing the Si–SiGe heterostructure layers in a QCL structure along with the grating made out of etched undoped Si₀.₈Ge₀.₂ with a coating of Ag. The period of the grating is $\Lambda$ and the grating depth is $d$. The direction pointing out of the page is $z$.

The grating depth is equal to $0.06 \times \Lambda$ with a filling factor of 50%. Calculations were performed with 100 terms to ensure a precision better than $5 \times 10^{-4}$ on the normalized frequency. Convergence of the algorithm ($f$ versus the number of terms $N$) is shown in Fig. 2. We calculate the complex eigen-frequency of the surface mode at the band edge ($k_x = \pi/\Lambda$). Convergence (i.e., relative error on losses is less then 10%) is achieved with $N > 100$. The choice of the period of 14 μm corresponds to a frequency of about 3 THz and the depth of the grating is about 0.8 μm in this case. We stress that the convergence is (almost) independent of the grating depth. This is because the method used here consists basically in matching the modes of different sections: the grating layer (which is patterned along $x$) and the others. The $x$ spatial dependency of these modes are calculated assuming invariance along $y$. The $S$-matrix algorithm [19] is used to propagate these modes through the whole structure. The convergence issue is related to the calculation of modes in the grating layer, due to the strong discontinuities (see [20]) and this is independent of the depth of the grating.

## III. DISCUSSION

The typical surface Bloch mode is represented in Fig. 3. We plot both $y$- (coupled with the active region) and $x$-components of the electric field as iso-intensity maps, relative to the root

![](./images/812016431368503297_2.jpg)

Fig. 2. Convergence of the numerical method for the calculation of the surface mode at $k_x = 0$. The normalized frequency $f_n$ versus the number of terms used in the plane wave expansion. The grating structure is the following: period $\Lambda$, filling factor $\phi = 0.5$, grating depth is $0.06 \times \Lambda$. With $\Lambda = 14\ \mu$m, the frequency is $f_n \times 21.5$ THz.

![](./images/812016431368503297_3.jpg)

Fig. 3. Electric field distribution corresponding to a surface mode at $k_x = 0$. The filling factor is $\phi = 0.5$ and grating depth is $0.2 \times \Lambda$. $|E_y|$ and $|E_x|$ field component are represented as iso-intensity plots. The normalized frequency is $f = 0.1304$, the quality factor $Q$ is 227, equivalent propagation loss is $9\ \text{cm}^{-1}$ and the modal overlap is $62\%$. The dotted horizontal line at a depth of $-0.75/\Lambda$ represent the location of the 200 nm p-SiGe ohmic layer.

mean square (rms) field. It is apparent that the field is is mainly $y$-polarized in an TM-like mode and is concentrated below the lower interface of the grating. The $x$-polarized field is located between the grating holes. This mode correspond to the point $k = K$ of the dispersion curve. This mode is stationary, that is with zero propagation velocity. Clearly, other modes, with non vanishing propagation speed exist at lower frequency and form a photonic band of available modes. Thus, the frequency that we will refer to represents the higher bound of this photonic band.

An important issue is the properties of the surface modes dependent on the relative depth of the grating. From this point all calculations refer to the special case of the structure described above, however we report results in terms of normalized units so that calculations can be scaled up to other frequencies (within some limits). We will calculate mode frequency, losses and mode confinement as a function of the grating depth.

The definition of propagation loss $\alpha$ for slow waves is not simple in periodic structures. Let us consider two structures, such that the attenuation per unit length is the same, but the group velocity is not. Clearly, the structure supporting slower waves would be preferable for applications such as amplification or lasing, as the interaction time is longer and, therefore, the gain is higher. Thus, expressing the loss in terms of $\text{cm}^{-1}$ is not appropriate. Instead, the suitable measure is the photon lifetime $\tau_{\text{ph}}$ defined as

$$
\tau_{\text{ph}}^{-1} = 2\Im(\omega) \tag{2}
$$

where $\omega$ is the complex eigen-frequency associated to the mode and $\Im$ is the imaginary part which in terms of the normalized frequency is

$$
\tau_{\text{ph}}^{-1} = \frac{4\pi c}{\Lambda\Im(f_n)}. \tag{3}
$$

The lasing condition, i.e., gain equal to losses, would imply the definition of gain in terms of inverse time, that is $g_t$. The relationship between gain in terms of inverse distance is thus $g = g_t/v_g$. The gain per unit length depends on the group velocity of the mode, which is not a constant in strongly dispersive structures. Thus, the gain defined in this way is well defined only in "fast" structures, such that the group velocity is very close to the phase velocity; in this case $g = n_{\text{eff}}g_t/c$, with $n_{\text{eff}}$ the effective index of the mode.

In order to allow comparison with values in the literature, where propagating modes are characterized in terms of $\text{cm}^{-1}$, we can still define "equivalent" propagation loss, such that the group velocity is replaced by the phase velocity

$$
\alpha = \frac{4\pi n_{\text{eff}}}{\Lambda\Im(f_n)}. \tag{4}
$$

This corresponds to comparing the photon lifetime with the gain expressed in terms of inverse time. We also define the quality factor

$$
Q = \frac{1}{2} \frac{\Re(f_n)}{\Im(f_n)} \tag{5}
$$

where $\Re$ is the real part of the complex term.

Fig. 4 shows propagation losses and overlap of the mode to the active region vs the depth of the grating. The overlap is defined as the 2-D integral with the numerator integrated over the active region (AR) and the denominator over the total structure

$$
\Gamma = \frac{\iint_{\text{AR}} dxdy|E_y|^2}{\iint dxdy\left(|E_y|^2+|E_x|^2\right)}. \tag{6}
$$

Comparing this to the usual definition for modes of translation-invariant waveguides needs some care: the surface mode is indeed a stationary mode, basically resulting from the coupling of counter propagating modes. Thus, in the case of a translation

![](./images/812016431368503297_4.jpg)

Fig. 4. Effective propagation loss $\alpha$ (left axis) and modal overlap $\Gamma$ (right axis) as a function of the grating depth. Calculations are made with 100 terms in the plane wave expansion.

![](./images/812016431368503297_5.jpg)

Fig. 5. Normalized frequency (left axis) and quality factor $Q$ (right axis) as a function of the grating depth. Calculations are made with 100 terms in the plane wave expansion.

invariant waveguide and after having dropped the $|E_x|^2$, which is about $0.1|E_y|^2$, our definition reduces to the usual

$$
\Gamma \approx \frac{\int_{\mathrm{AR}} d y\left|E_{y}(y)\right|^{2} \int_{0}^{\Lambda} d x \cos ^{2}\left(\frac{\pi}{\Lambda} x\right)}{\int d y\left|E_{y}(y)\right|^{2} \int_{0}^{\Lambda} d x \cos ^{2}\left(\frac{\pi}{\Lambda} x\right)} \tag{7}
$$

that is

$$
\Gamma=\frac{\int_{\mathrm{AR}} d y\left|E_{y}(y)\right|^{2}}{\int d y\left|E_{y}(y)\right|^{2}}. \tag{8}
$$

The volume of the active area $V_{\mathrm{AR}}$ divided by $\Gamma$ can be interpreted as the mode volume. In Fig. 5 we show the normalized frequency and the factor of quality as a function of the grating depth. For a structure with period of $14~\mu$m and with active region of $8~\mu$m, the depth varies between 0.7 and $2.8~\mu$m. The frequency of the photonic band edge decreases from 3.14 to 2.8 THz.

Both confinement in the active region and propagation losses increase with the grating depth. The increase of losses is mainly related to an increase of the overlap of the surface wave with the metal, which is directly related to the decay length. Residual absorption in the contact layer is negligible, unless the grating depth becomes very small ($<0.01$). The photon lifetime decreases significantly as the losses are increased due to the increase of the overlap of the mode with the metal. Indeed, the quality factor $Q$ is reduced from 1600 to less than 300.

To make easier the comparison with the literature, Fig. 4 shows the equivalent propagation losses $\alpha$. $\alpha$ scales almost linearly with the grating depth $d$. It is worth in noting that in the case of double metal clad structures, $\alpha$ scales linearly as one over the waveguide thickness which, in this case, is directly related to the mode volume, as $\Gamma \sim 1$ [16]. Thus, this result is not surprising, as the volume of the surface mode decreases as the grating thickness increases. In other words, in both case the increase of losses is associated to a stronger confinement of the mode. The overlap $\Gamma$, defined in (6), is also shown. It saturates at $\sim 60\%$ as the grating depth approaches ($\sim 0.1$, i.e., $\sim 1.4~\mu$m).

In designing waveguides for lasers, the relevant figure of merit is the ratio $\chi = \Gamma/\alpha$. For instance, the figure of merit is $\sim 0.12$ cm (Fig. 4) when the grating depth is $t \sim 0.1$ ($\sim 1.4~\mu$m). This correspond to $\Gamma = 0.5$ and $\alpha = 4~\mathrm{cm}^{-1}$. This values can be compared with the typical value for the demonstrated silicide-based waveguide, which is $\chi = 0.58/25~\mathrm{cm}^{-1} = 0.0232$ cm.

Indeed, one might expect, when extrapolating the figure of merit in Fig. 4 to the case flat gratings, that there is no need to pattern the metal surface, as losses decrease faster than overlap with decreasing depth. This limit case needs to be considered carefully, as when losses become very low and confinement is reduced, the model used here is no more complete. Indeed, when the metal surface is flat, the mode extends deeply into the substrate, which is typically doped, therefore lossy. Second, realistic devices entail a metal stripe, that is a finite trasverse dimension for the structure. This results in general into a much stronger reduction of the confinement, thus of the modal gain, than predicted by our 2-D model. Third, when the modal gain and internal loss are small, mirror loss become important, unless the device length is increased considerably. For these practical reasons, the extrapolation to flat surfaces should not be considered to be valid in our case.

We remark that the bandgap is not defined in the usual way, as the upper band mode is not bounded. It follows that the usual analysis of DFB lasers is not straightforward, as the effective coupling constant cannot be defined easily. We think that the analysis of lasing in such deeply modulated periodic surfaces, which is our case, should explicitely take into account Floquet modes, as periodiciy here cannot be treated as a pertubation of well-defined waveguide modes.

Fig. 6 shows the dispersion curve ($f$ versus $k_x$) corresponding to this surface wave, along with losses and overlap. This surface modes exist for $f \leq f_v$. As $f$ decreases, both the overlap and losses are reduced, as the localization is weaker. As $f$ approaches $f_v$, the group velocity decreases and the gain, in terms of inverse distance, increases. Because of the strong feedback, associated to this deep grating, an optical cavity is formed as soon as the grating is terminated. In other words, it is not necessary to add further feedback by cleaving the end facets. This is particularly attractive for silicon-based QCLs as Si (100) preferentially cleaves on the (111) facets at an angle and therefore requires a deep etch to produce laser facets for a cavity. Moreover, if the grating is patterned such that an additional period,

![](./images/812016431368503297_6.jpg)

Fig. 6. Normalized frequency $f_n$ versus wavevector $k_x$ for grating filling factor $\phi=0.5$ and depth $0.1\times\Lambda$. The corresponding frequency, when considering a $14-\mu$m period, is also marked on the right-hand axis. The equivalent output angle, in the substrate, is given in the top axis, assuming this mode is coupled to radiation using a second grating with period $2\Lambda$.

$\Lambda_1=2\Lambda$, appears, the waveguide mode is coupled to a plane wave with angle almost close to normal incidence. The exact angle is related to the wavevector, therefore the frequency, as also shown in Fig. 6.

A final remark concerns the choice of Drude parameters (resistivity and lifetime) for silver: we have chosen the room temperature values as they correspond to a conservative estimate of the losses. Therefore, we expect the propagation loss to be reduced to lower values below room temperature.

## IV. CONCLUSIONS

In conclusion, we suggest an alternative waveguide approach for terahertz QCLs and provide modelling results for the Si-SiGe system. The advantage of the proposed system is that no buried or double metal fabrication route is required, only the far simpler surface processing. The relevant figure of merit of the modal overlap divided by the waveguide losses is 0.2 cm for $8\,\mu$m of active cascade material which compares favourably to demonstrated terahertz waveguides in the Si-SiGe system.

## REFERENCES

[1] L. Pavesi, S. Gaponenko, and L. Dal Negro, Towards the First Silicon Laser, ser. NATO Science. Dordrecht, Germany: Kluwer, 2003.

[2] J. Faist, F. Capasso, C. Sirtori, D. L. Sivco, A. L. Hutchinson, and A. Y. Cho, "Quantum cascade laser," Science, vol. 264, no. 5158, pp. 553-556, Apr. 1994.

[3] G. Dehlinger, L. Diehl, U. Gennser, H. Sigg, J. Faist, K. Ensslin, D. Grtzmacher, and E. Müller, "Intersubband electroluminescence from silicon-based quantum cascade structures," Science, vol. 290, no. 5500, pp. 2277-2280, Dec. 2000.

[4] S. A. Lynch, R. Bates, D. J. Paul, D. J. Norris, A. G. Cullis, Z. Ikonic, R. W. Kelsall, P. Harrison, D. D. Arnone, and C. R. Pidgeon, "Intersub- band electroluminescence from Si-SiGe cascade emitters at terahertz frequencies," Appl. Phys. Lett., vol. 81, no. 9, pp. 1543-1545, Aug. 2002.

[5] P. Murzyn, C. R. Pidgeon, J.-P. R. Wells, I. V. Bradley, Z. Ikonic, R. W. Kelsall, P. Harrison, S. A. Lynch, D. J. Paul, D. D. Arnone, D. J. Robbins, D. J. Norris, and A. G. Cullis, "Picosecond intersubband dynamics in p-Si-SiGe quantum-well emitter structures," Appl. Phys. Lett., vol. 80, no. 8, pp. 1456-1458, Feb. 2002.

[6] R. W. Kelsall, Z. Ikonic, P. Murzyn, C. R. Pidgeon, P. J. Phillips, D. Carder, P. Harrison, S. A. Lynch, P. Townsend, D. J. Paul, S. L. Liew, D. J. Norris, and A. G. Cullis, "Intersubband lifetimes in p-Si-SiGe terahertz quantum cascade heterostructures," Phys. Rev. B, vol. 71, no. 11, pp. 1-10, Mar. 2005.

[7] R. M. Woodward, B. E. Cole, V. P. Wallace, R. J. Pye, D. D. Arnone, E. H. Linfield, and M. Pepper, "Terahertz pulse imaging in reflection geometry of human skin cancer and skin tissue," Phys. Med. Biol., vol. 47, no. 21, pp. 3853-3863, Nov. 2002.

[8] Y. C. Shen, T. Lo, P. F. Taday, B. E. Cole, W. R. Tribe, and M. C. Kemp, "Detection and identification of explosives using terahertz pulsed spec- troscopic imaging," Appl. Phys. Lett., vol. 86, no. 24, pp. 1-3, Jun. 2005, Article no. 241116.

[9] R. Bates, S. A. Lynch, D. J. Paul, Z. Ikonic, R. W. Kelsall, P. Harrison, S. L. Liew, D. J. Norris, A. G. Cullis, W. R. Tribe, and D. D. Arnone, "Interwell intersubband electroluminescence from Si-SiGe quantum cascade emitters," Appl. Phys. Lett., vol. 83, no. 20, pp. 4092-4094, Nov. 2003.

[10] D. J. Paul, "Si-SiGe heterostructures: from material and physics to devices and circuits," Semicond. Sci. Technol., vol. 19, no. 10, pp. R75-R108, Oct. 2004.

[11] D. J. Paul, P. Townsend, S. A. Lynch, R. W. Kelsall, Z. Ikonic, P. Har- rison, D. J. Norris, S. L. Liew, A. G. Cullis, X. Li, J. Zhang, M. Bain, and H. S. Gamble, "In search of a Si-SiGe THz quantum cascade laser," in Proc. Dig. Papers Top. Meeting Silicon Monolithic Intergr. Circuits RF Syst., Sep. 2004, pp. 143-146.

[12] R. E. Collins, Field Theory of Guided Waves, ser. Electromagnetic Wave Theory, D. G. Dudley, Ed., 2nd ed. New York: IEEE Press, 1991.

[13] J. B. Pendry, L. Martin-Moreno, and F. J. Garcia-Vidal, "Mimicking surface plasmons with structured surfaces," Science, vol. 305, no. 5685, pp. 847-848, Aug. 2004.

[14] R. Köhler, A. Tredicucci, F. Beltram, H. E. Beere, E. H. Linfield, A. G. Davies, D. A. Ritchie, R. C. Iotti, and F. Rossi, "Terahertz semicon- ductor-heterostructure laser," Nature, vol. 417, no. 6885, pp. 156-159, May 2002.

[15] B. S. Williams, S. Kumar, H. Callebaut, Q. Hu, and J. L. Reno, "Ter- ahertz quantum-cascade laser operating at 137 K," Appl. Phys. Lett., vol. 83, no. 11, pp. 2124-2126, Sep. 2003.

[16] Z. Ikonic, R. W. Kelsall, and P. Harrison, "Waveguide design for mid and far-infrared p-Si-SiGe quantum cascade lasers," Semicond. Sci. Technol., vol. 19, no. 1, pp. 76-81, Jan. 2004.

[17] J. D. Joannopoulos, R. D. Meade, and J. N. Winn, Photonic Crystals: Molding the Flow of Light. Princeton, NJ: Princeton Univ. Press, 1995.

[18] N. W. Ashcroft and N. D. Mermin, Solid State Physics. Philadelphia, PA: Saunders College Press, 1976.

[19] L. F. Li, "Formulation and comparison of two recursive matrix algo- rithms for modelling layered diffraction gratings," J. Opt. Soc. Amer. A, vol. 13, no. 5, pp. 1024-1035, May 1996.

[20] ——, "Use of Fourier series in the analysis of discontinuous periodic structures," J. Opt. Soc. Amer. A, vol. 13, no. 9, pp. 1870-1876, Sep. 1996.

[21] G. Granet and B. Guizal, "Efficient implementation of the coupled- wave method for metallic lamellar gratings in TM polarization," J. Opt. Soc. Amer. A, vol. 13, no. 5, pp. 1019-1023, May 1996.

[22] P. Lalanne and G. M. Morris, "Highly improved convergence of the coupled-wave method for TM polarization," J. Opt. Soc. Amer. A, vol. 13, no. 4, pp. 779-784, Apr. 1996.

![](./images/812016431368503297_7.jpg)

Alfredo De Rossi was born in Rome, Italy, in 1971. He received the MS degree in electrical engineering from de University of Rome "La Sapienza," Rome, Italy, in 1997 and the Ph.D. degree from University of Rome III, Rome, Italy, in 2002.

Since 2000 he has been a Research Engineer in Thales Research and Technology, Palaiseau cedex, France, formerly "Laboratoire Centrale de Recherche" of Thomson CSF. He is in charge of electromagnetic modeling. His interests cover non- linear optics (nonlinear propagation, second-order processes in semiconductors, entangled photon generation), electromagnetic design of infrared photonic devices, and photonic crystals. He is author and coauthor of more than 30 papers and holds 5 patents.

![](./images/812016431368503297_8.jpg)

Mathieu Carras received the M.S. degree from Ecole Centrale de Paris, Paris, Germany, in 2002 and is currently working toward the Ph.D. degree at Thales Research And Technology (TRT), Palaiseau cedex, France, with a thesis on quantum-well in- frared photodetectors.

Since January 2006, he has been a Research En- gineer at TRT France. His research interests include optical modelling of metallic nanostructures, physics of intersubband transitions, and the vertical transport in semiconductors, design and characterization of in- frared devices, including quantum-cascade lasers.

![](./images/812016431368503297_9.jpg)

Douglas J. Paul (M'00-SM'05) was born in Greenock, U.K., in 1969. He received the B.A. degree in physics/theoretical physics and the M.A. and Ph.D. degress from the University of Cambridge, Cambridge U.K. in 1990 and 1994, respectively.

Since 1994, he has worked in the Semicon- ductor Physics Group at the Cavendish Laboratory, Cambridge, University of Cambridge, U.K., and is presently responsible for all the Si and SiGe research. His research interests include the physics of short-channel CMOS devices, heterostructure and strained-Si CMOS, SiGe MODFETs, SiGe resonant tunnelling diodes and quantum devices, SiGe quantum-cascade lasers and quantum information processing. He has published over 50 journal publications, made over 80 presentations at conferences, and holds one patent. He was one of the Editors of the first Technology Roadmap of European Nanoelectronics which is now incorporated into the ITRS Roadmap. He is the U.K.s representative to the NATO Science for Peace CBP panel, sits on a U.K. Home Office advisory board and sits on a number of U.K. and international programme and scientific committees for many international conferences.

Dr. Paul is a Fellow of St Edmund's, College, Cambridge, a member of the Institute of Physics and a chartered physicists.