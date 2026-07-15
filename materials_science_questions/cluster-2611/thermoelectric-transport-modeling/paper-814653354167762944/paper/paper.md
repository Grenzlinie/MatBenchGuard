![](./images/814653354167762944_1.jpg)

Current Applied Physics 15 (2015) 608-616

Contents lists available at ScienceDirect

Current Applied Physics

journal homepage: www.elsevier.com/locate/cap

![](./images/814653354167762944_2.jpg)

# Theoretical investigation of electronic structure and optical response in relation to the transport properties of $\mathbf{Ga_{1-x}In_xN}$ ($\boldsymbol{x=0, 0.25}$, 0.50, 0.75)

![](./images/814653354167762944_3.jpg)

Fahad Ali Shah $^{a}$, Saleem Ayaz Khan $^{b}$, Suneela Arif $^{e}$, Sikander Azam $^{b}$, R. Khenata $^{c,*}$, S. Bin Omran $^{d}$

$^{a}$ Faculty of Basic \& Applied Sciences, Department of Physics, International Islamic University Islamabad, Pakistan
$^{b}$ New Technologies - Research Center, University of West Bohemia, Univerzitni 8, 306 14 Pilsen, Czech Republic
$^{c}$ Laboratoire de Physique Quantique et de Modélisation Mathématique, Université de Mascara, 29000, Algeria
$^{d}$ Department of Physics and Astronomy, College of Science, King Saud University, P.O. Box 2455, Riyadh 11451, Saudi Arabia
$^{e}$ Materials Modeling Lab, Department of Physics, Hazara University, Mansehra, Pakistan

---

## ARTICLE INFO

**Article history:**
Received 14 October 2014
Received in revised form
17 January 2015
Accepted 16 February 2015
Available online 20 February 2015

**Keywords:**
Electronic structure
Optical properties
Thermoelectric properties

## ABSTRACT

The state-of-the-art all-electron FLPAW method and the BoltzTrap software package based on semi-classical theory were adopted to explore the electronic structure and the optical and thermoelectric properties of $\text{Ga}_{1-\text{x}}\text{In}_{\text{x}}\text{N}$. $\text{Ga}_{1-\text{x}}\text{In}_{\text{x}}\text{N}$ is predicted to be a direct band gap material for all values of $x$. Moreover, the band gap varies between 2.99 eV and 1.95 eV as $x$ changes. Optical parameters such as the dielectric constant, absorption coefficient, reflectivity and refractive index are calculated and discussed in detail. The doping of In plays an important role in the modulation of the optical constants. The static dielectric constant $\varepsilon(0)$ of $\text{Ga}_{1-\text{x}}\text{In}_{\text{x}}\text{N}$ was calculated as 3.95, 3.99, 3.99 and 4.03 at $x=0.00, 0.25, 0.50$ and 0.75, respectively. The static refractive index is 2.0 for pure $\text{Ga}_{1-\text{x}}\text{In}_{\text{x}}\text{N}$ at $x=0.00$. The thermal properties varied greatly as $x$ fluctuated. The ternary alloy has large values for the Seebeck coefficient and figure of merit at high temperatures and is thus suitable for thermoelectric applications. Pure $\text{Ga}_{1-\text{x}}\text{In}_{\text{x}}\text{N}$ at $x=0$ exhibited $ZT=0.80$ at room temperature, and at higher temperatures, the thermal conductivity decreased with increased In doping.

© 2015 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Semiconductor electronics and spintronics are emerging fields in science and technology. Numerous efficient and active materials with technological applications have received interest from material scientists worldwide. Among alloys, Group III-V semiconductors are of special interest due to their potential role in photonic and optoelectronic devices. Because of their wide band gap near the $\Gamma$ symmetry point, III-V nitrites are considered to have the most potential for maximizing the efficiency of optoelectronic devices [1,2].

Heterojunction devices may play a potential role in optoelectronics. Dissimilar semiconductors with unequal band gaps give rise to heterojunctions. Among the most important optoelectronic heterostructures, laser diodes and photodetectors are of particular interest. Heterojunction devices are frequently used in high-speed optoelectronics and have substantially improved the performance of optical detectors [3]. High-speed heterojunction transistors are fabricated from GaN, InN and AlN [4]. Group III nitrides are effectively used in high-power lasers as well as in high-temperature and high-frequency electronic devices [5]. These materials are also used in manufacturing highly efficient low-cost solar cells [6], visible light-emitting diodes (LEDs) [7,8] and laser diodes [9-12] in the visible (amber, green and blue) to ultraviolet (UV) region. Recent developments in solid-state lighting have been driven by the modification of ternary nitrides such as $\text{In}_{\text{x}}\text{Ga}_{1-\text{x}}\text{N}$ and $\text{In}_{\text{x}}\text{Al}_{1-\text{x}}\text{N}$ alloys. The calculated fundamental energy band gaps of these materials are approximately 0.7 eV for InN [13,14] and 3.5 eV for GaN [15], and the absorption and emission edges of these semiconductor alloys lie in the infrared (IR) to ultraviolet (UV) region of the electromagnetic spectrum.

---

* Corresponding author. LPQ3M-Laboratory, Faculty of Science and Technology, Mascara University, 29000 Mascara, Algeria.
E-mail address: khenata_rabah@yahoo.fr (R. Khenata).

http://dx.doi.org/10.1016/j.cap.2015.02.014
1567-1739/© 2015 Elsevier B.V. All rights reserved.

With the development of science and technology, researchers have sought for new applications of GaN alloys. III-V semiconductor alloys can be obtained by a simple, commonly used method, doping, performed by replacing a small amount of the anion species in GaN with other impurities such as In. The use of a sapphire substrate for nitride thin films increases the lattice mismatch and the difference in thermal expansion coefficient between the substrate and the epilayer. This effect increases the dislocation density and piezoelectric field in the heterostructure [16]. Dislocation can be decreased by using techniques such as epitaxial lateral overgrowth (ELO) and pendeo-epitaxy. Yoon et al. [17] observed that the dislocation density decreased when an epitaxial layer of $\text{In}_x\text{Ga}_{1-x}\text{N}$ was successfully grown on a sapphire substrate. During the annealing process, InN precipitation has been observed in the $\text{Ga}_{1-x}\text{In}_x\text{N}$ alloy; thus, the wurtzite phase of $\text{Ga}_{1-x}\text{In}_x\text{N}$ is thermodynamically unstable [18]. Theoretical studies addressing calculations of the $\text{Ga}_{1-x}\text{In}_x\text{N}$ phase diagram have demonstrated that a zinc-blende modification provides a thermodynamically stable phase of $\text{Ga}_{1-x}\text{In}_x\text{N}$ [19-24].

Experimental and theoretical studies have demonstrated that the band gap value of $\text{Ga}_{1-x}\text{In}_x\text{N}$ and $\text{Ga}_{1-x}\text{Al}_x\text{N}$ varies with the concentration of the minor component. For increasing In concentration, the band gap decreases; however, the band gap increases with increasing Al concentration [25,26]. The impurity concentration strongly controls the electrical conductivity of semiconductor materials. The doping process may be complicated; however, in designing electronic devices, both n-type (electron carrier) and p-type (hole carrier) doping are necessary. Native defects such as vacancies and interstitials may hinder the doping process, and the optical properties of materials are greatly affected by these defects. Most compound semiconductors from group III-V are doped with an element of the same group (either from group III or group V) to produce an alloy with desirable properties such as energy band gaps fit for producing light at specified wavelengths. One such alloy is gallium indium nitride (GaInN), which is the focus of this work. Ternary compounds play an important role in achieving properties that are difficult to obtain with binary compounds. This ternary alloy has been intensively investigated both experimentally and theoretically in its wurtzite crystal phase [27,28]; however, investigations of the zinc-blende phase of $\text{Ga}_{1-x}\text{In}_x\text{N}$ are more pertinent owing to its large optical gain and lower threshold current density [29]. Thus, it is worthwhile to explore the electronic, optical and thermal properties of the zinc-blende $\text{Ga}_{1-x}\text{In}_x\text{N}$ alloy due to a lack of available information on the cubic phase. The main goal of this study is to investigate the dependence of the band gap, dielectric constant and thermoelectric properties on the Ga and In concentrations in the zinc-blende structure of the $\text{Ga}_{1-x}\text{In}_x\text{N}$ alloy.

### 2. Method of calculations

The core/inner shell electrons in Ga ($1s^2 2s^2 2p^6 3s^2 3p^6$), In ($1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^2 4p^6$) and N ($1s^2$) are distinguished from the valence shell electrons of Ga ($3d^{10} 4s^2 4p^1$), In ($4d^{10} 5s^2 5p^1$), and N ($2s^2 2p^3$) in this calculation. GaN and InN compounds usually crystallize in the wurtzite and zinc-blende structures, respectively. Calculations were performed on the zinc-blende phase of $\text{Ga}_{1-x}\text{In}_x\text{N}$ for various values of x, using the ab-initio all-electron full potential linearized augmented plane wave (FP-LAPW) method based on density functional theory (DFT), as implemented in the WIEN2K software package [30]. We obtained the most accurate results using FP-LAPW with the modified Becke-Johnson potential (mBJ) [31]. The mBJ potential yields better band splitting and is considered to have an accuracy similar to that of the more computationally intensive and well-known GW method, where 'G' stands for Green's function and 'W' is the screened Coulomb interaction, for obtaining energy band gap values. FP-LAPW has been reported as the most accurate and reliable method for addressing solid materials [32,33]. In this method, Kohn-Sham orbitals are expanded in the form of atomic-like orbitals inside muffin-tin (MT) spheres and as a plane wave in the interstitial regions. The local density approximation (LDA) and generalized gradient approximation (GGA) in Ceperley and Alder [34] and Perdew-Burke and Ernzerhof [35] parameterization have been avoided because these approximations do not properly account for the exchange correlation potential and its charge derivatives, which results in an underestimation of the most important electronic property, i.e., the energy band gap of the material. Hence, the mBJ scheme was used to treat the exchange correlation potential by solving the Kohn-Sham equations. A plane wave cutoff parameter of $\text{R}_{\text{MT}}\text{K}_{\text{max}}=7.0$ was used in the plane wave expansion, where $\text{R}_{\text{MT}}$ and $\text{K}_{\text{max}}$ are the minimum-radius muffin-tin sphere and the magnitude of the largest k vector in the plane wave expansion, respectively. To ensure that the atomic spheres do not overlap, the atomic sphere radii of the atoms were taken to be as large as possible. The spherical harmonic behavior of the wave function inside the muffin-tin sphere was expanded up to $\text{l}_{\text{max}}=10$. The self-consistent calculations were considered to have converged when the total energy of the systems was stable within $10^{-4}$ Ryd for successive steps.

Calculations of optical properties provide a true understanding of the structure of a material. The dielectric function is the fundamental property required to investigate the optical nature of a solid material. This function describes the linear response of the system to electromagnetic radiation and is also related to the electron-photon interactions. This function behaves as a bridge by connecting the physical process of interband transitions with the electronic structure. Energy eigenvalues and electron wave functions are required parameters for calculating the frequency-dependent dielectric function and are the natural output obtained from calculating the band structure. The imaginary part of the dielectric constant $\varepsilon_2(\omega)$ primarily describes the transition of electrons from occupied to unoccupied states. The optical response function in the linear response range can be described by the complex quantity $\varepsilon(\omega)=\varepsilon_1(\omega)+i\varepsilon_2(\omega)$. For the cubic crystal symmetry of $\text{Ga}_{1-x}\text{In}_x\text{N}$, a single non-zero dielectric tensor component fully describes the linear optical properties. The imaginary part can be calculated using the following expression [36]:

$$
\begin{aligned}
\varepsilon_{2}^{i j}=& \frac{4 \pi^{2} e^{2}}{V m^{2} \omega^{2}} \times \sum_{n n^{\prime} \sigma}\left\langle k n \sigma\left|p_{i}\right| k n^{\prime} \sigma\right\rangle\left\langle k n^{\prime} \sigma\left|p_{j}\right| k n \sigma\right\rangle \\
& \times f_{k n}\left(1-f_{k n^{\prime}}\right) \delta\left(E_{k n^{\prime}}-E_{k n}-\hbar \omega\right).
\end{aligned}
$$

In the above expression, $e$ and $m$ represent the charge and mass of an electron, while $\omega$ is the frequency of the electromagnetic radiation striking the crystal. The volume of the unit cell is represented by $V$, and $p$, given in bracket notation, is the momentum operator. The quantity $|kn\sigma\rangle$ represents the crystal wave function, where $k$ is the crystal momentum and $\sigma$ is the spin. The counting of transitions from occupied to unoccupied states is ensured by $f_{kn}$, the Fermi distribution function. The last term, $\delta(E_{kn'}-E_{kn}-\hbar\omega)$, is the condition for the conservation of total energy. The electron dipole transition between the valence and conduction band is attributed to the peaks arising in the optical response.

In this work, the $\text{Ga}_{1-x}\text{In}_x\text{N}$ alloy (zinc-blende structure) was modeled with varying elemental compositions, i.e., x = 0, 0.25, 0.50 and 0.75, as shown in Fig. 1. A supercell containing eight atoms and exhibiting cubic symmetry was adopted. We calculated the fundamental physical properties, such as the total energy and energy band gap, for each configuration.

![](./images/814653354167762944_4.jpg)

Fig. 1. Unit cell structure of the $Ga_{1-x}In_xN$ alloy.

## 3. Results and discussion

### 3.1. Band structure and density of states

The electronic band structure of zinc-blende $Ga_{1-x}In_xN$ was calculated for various compositions (x = 0, 0.25, 0.50 and 0.75) using the mBJ scheme. Fig. 2a-d show that the calculated band gap varies with x. For increasing In (x = 0, 0.25, 0.50 and 0.75), the nature of the band gap of $Ga_{1-x}In_xN$ is direct $(E_g^{\Gamma-\Gamma})$. The band gap value decreases with increasing values of x. We obtained a direct band gap of 2.99 eV for pure $Ga_{1-x}In_xN$ (at x = 0). Our calculated band gap values for $Ga_{1-x}In_xN$ are in close agreement with the experimental results (3.25 eV) reported in ref [37] and more closely agree with the theoretical findings (1.93 eV) of Kanoun et al. [38] and the reported values of (1.28-1.9 eV) [39-46]. The variation in the band gap of $Ga_{1-x}In_xN$ covers a broad spectral range from visible to ultraviolet (UV). Based on specific requirements, applications can be fulfilled by achieving a band gap between 2.99 eV and 1.95 eV. Hence, optoelectronic devices operating at different wavelengths can be fabricated by simply controlling the In concentration in $Ga_{1-x}In_xN$. The improved results in this case are due to the effectiveness of the mBJ scheme. The variation in the energy band gap occurs due to the difference in the density of states (DOS) [47]. As other theoretical studies [48-50] have reported, the DOS strongly affects the band gap of a compound. Differences in the DOS lead to a wider band gap in $Ga_{1-x}In_xN$ (at x = 0.00) compared with $Ga_{1-x}In_xN$ (at x = 1.00). The DOS changes as some of the Ga atoms are replaced with In in the $Ga_{1-x}In_xN$ crystals. At a higher Ga concentration, the distribution of the Ga DOS is dominant, at which point, the band gap is observed to be similar to that of pure $Ga_{1-x}In_xN$ at x = 0.00. Likewise, a higher In concentration alters the band gap of $Ga_{1-x}In_xN$ such that it is similar to that of pure $Ga_{1-x}In_xN$ at x = 1.00. The total density of states (TDOS) together with the partial density of states (PDOS) for the s, p and d orbitals of Ga and In and the s and p orbitals of N are presented for $Ga_{1-x}In_xN$ in Fig. 3a-d. In $Ga_{1-x}In_xN$ at x = 0.00, N-p substantially contributes to the valence band maximum (VBM); all lower-energy states are considered to be part of the core and are identified as Ga-d and N-s states. Upon the formation of a ternary alloy, the lower part of the valence band is primarily occupied by Ga-d and In-d states. The main peaks of Ga-d and In-d are positioned near -11.5 eV for all values of x, but their contributions vary. The intensity of these strongly localized states is much larger than that of the N-s/p states. Furthermore, we conclude that strong hybridization occurs between the Ga-d and In-d states in the lower energies, which results in the covalent nature of the bond between these two atoms.

### 3.2. Optical properties

The calculated imaginary part $\varepsilon_2(\omega)$ of the dielectric function of $Ga_{1-x}In_xN$ is shown in Fig. 4a for x = 0.00, 0.25, 0.50 and 0.75. The fundamental absorption edge of $Ga_{1-x}In_xN$ occurs at approximately 3.12 eV, 2.80 eV, 2.55 eV and 2.10 eV for x = 0, 0.25, 0.50 and 0.75, respectively. These critical points are attributed to the threshold of the direct optical transition that occurs at 2.99 eV, 2.67 eV, 2.31 eV and 1.95 eV, respectively. One broad peak located at approximately 7.9 eV and two sharp peaks situated at 10.8 eV and 12.8 eV represent electron transitions from the valence band to the conduction band in the $\varepsilon_2(\omega)$ graph. The imaginary part $\varepsilon_2(\omega)$ behaves in a similar fashion for all In concentrations except for minor differences in terms of the peak height.

The Kramers-Kronig transformation [51] is a useful approach for obtaining the real part $\varepsilon_1(\omega)$ of the dielectric function from the imaginary part:

$$
\varepsilon_{1}(\omega)=1+\frac{2}{\pi} p \int_{0}^{\infty} \frac{\omega^{\prime} \varepsilon_{2}\left(\omega^{\prime}\right)}{\omega^{\prime 2}-\omega^{2}} d \omega^{\prime}
$$

where p is the principle value of the integral. Fig. 4b shows the calculated real part of the dielectric function. The real component of the dielectric function increases with photon energy and reaches a maximum value of approximately 7.1 eV for all compositions. The zero-frequency limit or static dielectric constant $\varepsilon(0)$, which is strongly dependent on the band gap, was also calculated. The calculated static dielectric constant of $Ga_{1-x}In_xN$ is 3.959, 3.990, 3.993 and 4.037 for x = 0, 0.25, 0.50 and 0.75, respectively. The corresponding band gap values are 2.99 eV, 2.67 eV, 2.31 eV and 1.95 eV, respectively. It has been observed that a smaller band gap value results in a larger static dielectric constant $\varepsilon(0)$. The inverse relation between $\varepsilon(0)$ and the band gap can be defined using the Penn model [52]:

$$
\varepsilon(0) \approx 1+\left(\hbar \omega_{p} / E_{g}\right)^{2}.
$$

Utilizing values of $\varepsilon(0)$ and plasma energy, we can calculate Eg using the above relation. From the graph, we observe that the value of $\varepsilon_1(\omega)$ drops below zero at 11 eV for pure Ga₁₋xInxN (when x = 0.00) and at 12.8 eV for x = 0.25, 0.50 and 0.75. In these energy regions, the incident light is completely reflected from the material, and thus, the material exhibits metallic behavior. Furthermore, the negative value of $\varepsilon_1(\omega)$ corresponds to local maxima in the reflectivity spectra.

The refractive index $n(\omega)$ of $Ga_{1-x}In_xN$ was calculated and is presented in Fig. 4c. We obtained a broad spectrum of refractive index $n(\omega)$ values over a wide energy range up to 14 eV. The behavior of $n(\omega)$ and $\varepsilon_1(\omega)$ is similar. The main peak of the refractive index occurs at approximately 7 eV for all values of x.

The refractive index starts to decline when the photon energy exceeds 12.5 eV. The static refractive index $n(0)$ of pure $Ga_{1-x}In_xN$ at x = 0.00 is found to be 2, which is in close agreement with the theoretical findings of Amin et al. [53]. The clear sharp peaks of

![](./images/814653354167762944_5.jpg)

Fig. 2. Calculated electronic band structure of the Ga₁₋ₓInₓN alloy.

Ga₁₋ₓInₓN at x=0.00 transform into broad peaks (hump-like structures) with increasing In concentration. Fig. 4c also clearly demonstrates that the refractive index of Ga1-xInxN falls below unity at 13.2 eV for x=0, 0.25, 0.50 and 0.75. A refractive index below unity indicates that the group velocity ($v_g = c/n$) of the incident light is greater than c, implying that the group velocity has shifted to the negative domain and that the nature of the material has changed from linear to nonlinear. Thus, the material becomes superluminal for higher-energy photons [54,55].

The absorption coefficient $I(\omega)$ determines the range of light that passes through the materials before being absorbed. The absorption spectrum of Ga₁₋ₓInₓN is presented in Fig. 4d. The absorption coefficient of Ga₁₋ₓInₓN varies as the In concentration increases.

The absorption coefficient of pure Ga₁₋ₓInₓN at zero doping dominates at intermediate energy values. The maximum value of $I(\omega)$ increases from $326 \times 104\ \mathrm{cm}^{-1}$ for Ga₁₋ₓInₓN (x = 0.00) to $338 \times 104\ \mathrm{cm}^{-1}$ for high In concentrations. Two major peaks at approximately 9 eV and 11.1 eV in the absorption coefficient represent the absorption of light at two different wavelengths. The maximum value of $I(\omega)$ is approximately 13.5 eV for all values of x.

The reflectivity $R(\omega)$ of Ga₁₋ₓInₓN as a function of photon energy is displayed in Fig. 4e. From the reflectivity plot, we determined that each concentration has a corresponding maximum reflectivity value. At approximately 11.3 eV, pure Ga₁₋ₓInₓN (at x=0.00) has a value of 0.44 compared with 0.46 at 13 eV [53]. A sharp increase in the reflectivity spectrum occurs above 12 eV and reaches maximum

![](./images/814653354167762944_6.jpg)

Fig. 3. Calculated TDOS and PDOS of the In-doped GaN alloy.

values of 0.74, 0.67, 0.71 and 0.69 for $x=0.00,0.25,0.50$ and 0.75 at
13.5 eV, respectively. The maxima arise from inter-band transitions,
while the reflectivity minimum in the energy range of 9-10 eV
results from collective plasma resonance. The incorporation of
different In concentrations yields various reflectivity values for
Ga$_{1-x}$In$_x$N, indicating that this material is suitable for Bragg
reflection at various wavelengths [56,57].

### 3.3. Thermoelectric properties

Based on the electronic band structure, the transport properties
were calculated using semi-classical Boltzmann theory with the
constant scattering approximation, as implemented in the Boltz-
Trap program [58,59]. Transport parameters, such as the Seebeck
coefficient, electrical conductivity, figure of merit, thermal con-
ductivity and power factor, of the ternary alloy Ga$_{1-x}$In$_x$N were
calculated using the BoltzTrap code under the generalized
relaxation-time approximation. In this package, the relaxation time
is considered to be both temperature- and energy-dependent and
satisfies the power-law approximate relation $\tau(E,T)=\tau_0(E/k_BT)^s$
[60]. $\tau_0$ is a parameter and $s=1/2$ for semiconductors, while $E$ is
measured from the valence band top or conduction band bottom.
We calculated the electrical conductivity $\sigma$ of Ga$_{1-x}$In$_x$N for various
values of $x$ ($x=0,0.25,0.50$ and 0.75), as shown in Fig. 5a. The
electric conductivity of the ternary alloy increases smoothly with
temperature for $x=0,0.25,0.50$ and 0.75. With the incorporation
of In, we see that $\sigma$ increases compared with pure Ga$_{1-x}$In$_x$N
($x=0.00$) until reaching 500 K. For pure Ga$_{1-0}$In$_0$N and
Ga$_{0.75}$In$_{0.25}$N, a maximum value of $14.1\times10^{18}\ (\Omega\mathrm{ms})^{-1}$ is obtained
at 850 K. At higher temperatures, Ga$_{1-0}$In$_0$N and Ga$_{0.75}$In$_{0.25}$N
exhibit greater $\sigma$ values than the highly doped In alloy. The Seebeck
coefficient $S$ determines the efficiency of thermocouples, as elec-
trons are a means of both heat and charge transport. In the case of a
temperature gradient, electrons move from a higher-temperature
region toward a lower-temperature region because of the poten-
tial difference setup, which is known as the Seebeck voltage. We

![](./images/814653354167762944_7.jpg)

Fig. 4. Calculated optical constants of the Ga₁₋ₓInₓN alloy: (a) imaginary part of the dielectric constant, (b) real part of the dielectric constant, (c) refractive index, (d) absorption coefficient and (e) reflectivity.

![](./images/814653354167762944_8.jpg)

Fig. 5. Calculated thermoelectric properties of the $Ga_{1-x}In_xN$ alloy: (a) electrical conductivity, (b) Seebeck coefficient, (c) thermal conductivity, (d) power factor and (e) figure of merit.

calculated the Seebeck coefficient of pure Ga₁₋ₓInₓN (x = 0.00) and In-doped GaN over a temperature range of 100–900 K. Fig. 5b clearly depicts the Seebeck coefficient of the ternary alloy Ga₁₋ₓInₓN for various values of x. From the Seebeck curve, it is evident that Ga₁₋ₓInₓN has the largest Seebeck coefficient for x = 0.00 over the entire temperature range. Pure Ga₁₋ₓInₓN at x = 0.00 exhibits a maximum value of 288 μV/K at 150 K; the value then decreases and reaches a minimum value of 247 μV/K at approximately 850 K. At 100 K, Ga1–xInxN exhibits values of 269 μV/K, 218 μV/K, 120 μV/K and 154 μV/K for x = 0.00, 0.25, 0.50 and 0.75, respectively. The Seebeck coefficient S increases with temperature for In-doped Ga₁₋ₓInₓN and reaches a maximum value of 239 μV/K (x = 0.25 and 0.50) at 850 K and 232 μV/K (x = 0.75) at 849 K. It is apparent from the graph that S decreases to a greater extent with the addition of In in the Ga₁₋ₓInₓN alloy.

Thermal conductivity refers to the ability of a material to conduct heat, and both electrons and lattice vibrations contribute to this ability. Unlike metals, in semiconductors, the conduction of heat occurs primarily by phonons (lattice vibrations) [61]. Fig. 5c displays the thermal conductivity k of the ternary alloy Ga₁₋ₓInₓN for x = 0.00, 0.25, 0.50 and 0.75. The minimum value of Ga₁₋ₓInₓN occurs at 100 K and increases exponentially, reaching maximum values of 9.5 × 10¹⁴ (W/mK²s)⁻¹(x = 0), 8.3 × 10¹⁴ (W/mK²s)⁻¹(x = 0.50), 8.9 × 10¹⁴ (W/mK²s)⁻¹(x = 0.25), and 7.9 × 10¹⁴ (W/mK²s)⁻¹(x = 0.75) at 850 K, 859 K and 845 K, respectively. The thermal conductivity remains constant at lower temperatures and decreases with In doping in the high-temperature region. The power factor ($P^{IV}=S^{2}\sigma$) is another transport parameter that provides information regarding the thermoelectric behavior of a material. The power factor of Ga₁₋ₓInₓN is shown in Fig. 5d for several values of x. The minimum power factor was recorded at 100 K for pure Ga₁₋ₓInₓN (x = 0.00) and In-doped Ga₁₋ₓInₓN. The power factor increased linearly with temperature and reached a maximum value of 8.5 × 10¹¹ (W/mK²s) for pure Ga₁₋ₓInₓN (x = 0.00) at 850 K. For Ga₀.₇₅In₀.₂₅N and Ga₀.₅₀In₀.₅₀N, these values were 7.9 × 10¹¹ (W/mK²s) and 7.2 × 10¹¹ (W/mK²s), respectively, at 850 K. For high In concentrations, the value decreases to 7.0 × 10¹¹ (W/mK²s) at 825 K. From the overall curve, we can see that the power factor of Ga₁₋ₓInₓN decreases with increasing In concentration.

The figure of merit (ZT) is a dimensionless quantity used to predict the performance of a thermoelectric material. The figure of merit is directly proportional to the Seebeck coefficient and the electric conductivity and is inversely proportional to the thermal conductivity according to the following expression:

$$
ZT=\frac{S^{2}\sigma_{e}T}{k_{e}+k_{p}}.
$$

Here, $k_e$ and $k_p$ are the thermal contributions from electrons and phonons, respectively. Good thermoelectric materials are considered to have ZT values approximately equal to or greater than unity [62]. The phonon subsystem also offers a crucial contribution; however, in the present calculation, the phonon thermal conductivity is ignored, and only the electron thermal conductivity is considered. The calculated ZT values of Ga₁₋ₓInₓN for x = 0, 0.25, 0.50 and 0.75 are presented in Fig. 5e. At room temperature, pure Ga₁₋ₓInₓN (x = 0.00) has a maximum ZT value of 0.80. With the addition of In, ZT decreases and reaches a maximum value of approximately 0.75 at 850 K. In Fig. 5e, the ZT of Ga₁₋ₓInₓN is compared with that of the clathrate compound from the work of Li Wang et al. [63].

## 4. Conclusions

In summary, we have investigated the electronic structure and optical properties of Ga₁₋ₓInₓN by tuning the In concentration using the FPLAPW method based on DFT. The thermoelectric properties were calculated with the assistance of the BoltzTrap program. The band structure calculations demonstrated that the energy band gap decreases with increasing In concentration. Because of this flexibility, band gap devices can be constructed for various applications within the range of 2.99 eV−1.95 eV. Optical constants such as the dielectric function, reflectivity, absorption coefficient and refractive index also vary strongly with the In concentration. A smaller band gap results in a larger static dielectric constant. Thus, the material may act as a wavelength filter and a Bragg reflector at certain wavelengths. The transport tensor of the ternary alloy (Ga₁₋ₓInₓN) was also calculated for the first time in this work. Pure Ga₁₋ₓInₓN (at x = 0.00) was observed to exhibit a larger Seebeck coefficient and figure of merit compared with the In-doped alloy, and the thermal conductivity decreased with the addition of In. The overall thermoelectric properties revealed that Ga₁₋ₓInₓN is a good thermoelectric candidate and can be utilized in manufacturing alternative energy sources.

## Acknowledgments

These results were developed within the CENTEM project, reg. no. CZ.1.05/2.1.00/03.0088, which was co-funded by the ERDF as part of the Ministry of Education, Youth and Sports OP RDI program, MetaCentrum (LM2010005) and CERIT-SC under the program Centre CERIT Scientific Cloud, reg. no. CZ.1.05/3.2.00/08.0144. The authors (R.K. and S.B.O.) acknowledge support provided by the National Plan for Science, Technology and Innovation under research project no. #ADV-1498.

## References

[1] Y.S. Park, J. Korean Phys. Soc. 34 (1999) S199.
[2] M. Razeghi, P. Kung, D. Walker, E. Monroy, M. Hamilton, P. Sandvik, J. Korean Phys. Soc. 34 (1999) S234.
[3] H. Kressel, J.K. Butler, Semiconductor Lasers and Heterojunction LEDs, Academic, New York, 1977, p. 608.
[4] S.N. Mohammad, H. Morkoc, Prog. Quantum Electron. 20 (1996) 361.
[5] J. Wu, J. Appl. Phys. 106 (2009) 011101.
[6] A. Yamamoto, M. Tsujino, M. Ohkubo, A. Hashimoto, Sol. Energy Mater. Sol. Cells 35 (1994) 53.
[7] S. Nakamura, G. Fasol, The Blue Laser Diodes, Springer, Berlin, 1997.
[8] A. Dagar, J. Christen, T. Riemann, S. Richler, J. Blassing, A. Diez, A. Krost, A. Alam, M. Heuken, Appl.Phys.. Lett. 78 (2001) 2211.
[9] I. Vurgaftman, J.R. Meyer, L. Ram-Mohan, J. Appl. Phys. 89 (2001) 5815.
[10] C.G. Van de Walle, Wide band gap semiconductors, in: Proceeding of the Seventh Trieste Semicon-ductors Symposium, 1992. North Holland, Amsterdam 1993.
[11] J.F. Kaeding, Y. Wu, T. Fujii, R. Sharma, P.T. Fini, J.S. Speck, S. Nakamura, J. Cryst. Growth. 272 (2004) 257.
[12] T. Kawashima, A. Miyazaki, H. Kasugai, S. Mishima, A. Honshio, Y. Miyake, M. Iwaya, S. Kamiyama, H. Amano, I. Akasaki, J. Cryst. Growth 272 (2004) 270.
[13] V. Davydov, A. Klochikhin, R. Seisyan, V. Emtsev, S. Ivanov, F. Bechstedt, J. Furthmüller, H. Harima, A. Mudryi, A. Aderhold, O. Semchinova, J. Graul, Phys. Status Solidi B 229 (2002) R1.
[14] J. Wu, W. Walukiewicz, K.M. Yu, J.W. Ager III, E.E. Haller, H. Lu, W.J. Schaff, Y. Saito, Y. Nanishi, Appl. Phys. Lett. 80 (2002) 3967.
[15] I. Vurgaftman, J.R. Meyer, J. Appl. Phys. 94 (2003) 3675.
[16] J.S. Im, H. Kollmer, J. O, A. Sohmer, F. Scholz, A. Hangleiter, Phys. Rev. B 57 (1998) R9435.
[17] H.S. Yoon, R.J. Choi, C.S. Kim, Y.B. Hahn, C.H. Hong, E.-K. Suh, H.J. Lee, J. Korean Phys. Soc. 42 (2003) S438-S440.
[18] M.D. McCluskey, L.T. Romano, B.S. Krusor, D.P. Bour, N.M. Johnson, S. Brennan, Appl. Phys. Lett. 72 (1998) 1730.
[19] G.B. Stringfellow, J. Cryst. Growth 58 (1982) 194.
[20] J.L. Martins, A. Zunger, Phys. Rev. B 30 (1984) 6217.
[21] I.H. Ho, G.B. Stringfellow, Appl. Phys. Lett. 69 (1996) 2701.
[22] T. Matsuoka, Appl. Phys. Lett. 71 (1997) 105.
[23] A. Wakahara, T. Tokuda, X.-Z. Dang, S. Noda, A. Sasaki, Appl. Phys. Lett. 71 (1997) 906.
[24] L.K. Teles, J. Furthmüller, L.M.R. Scolfaro, J.R. Leite, F. Bechstedt, Phys. Rev. B 62 (2000) 2475.
[25] M.D. McCluskey, et al., Appl. Phys. Lett. 72 (1998) 2725.
[26] L. Bellaiche, et al., Appl. Phys. Lett. 74 (1999) 1842.

[27] M.G. Ganchenkova, V.A. Borodin, K. Laaksonen, R.M. Nieminen, Phys. Rev. B 77 (2008) 075207.

[28] K. Laaksonen, M.G. Ganchenkova, R.M. Nieminen, Phys. B 376 (2006) 502.

[29] S.H. Park, S.L. Chuang, J. Appl. Phys. 87 (2000) 353.

[30] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, WEIN2K, an Augmented Plane Wave p Local Orbitals Program for Calculating Crystal Properties, Technische Universitat, Wein, Vienna, Austria., 2001.

[31] F. Tran, P. Blaha, Phys. Rev. Lett. 102 (2009) 226401.

[32] S. Gao, Comput. Phys. Commun. 153 (2003) 190.

[33] K. Schwarz, J. Solid State Chem. 176 (2003) 319.

[34] D.M. Ceperley, B.I. Alder, Phys. Rev. Lett. 45 (1980) 566.

[35] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[36] A. Delin, P. Ravindran, O. Eriksson, J.M. Wills, Int. J. Quantum Chem. 69 (1998) 349.

[37] A. Trampert, O. Brandt, K.H. Ploog, in: J.I. Pankove, T.D. Moustakas (Eds.), Crystal Structure of Group III-nitrides, Semiconductors and Semimetals, Vol. 50, Academic, San Diego,, 1998.

[38] M.B. Kanoun, S. Goumri-Said, A.E. Merad, H. Mariette, J. Appl. Phys. 98 (2005) 063710.

[39] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.

[40] F.D. Murnaghan, Proc. Natl. Acad. Sci. U. S. A. 30 (1944) 244.

[41] K. Kim, W.R.L. Lambrecht, B. Segall, Phys. Rev. B 53 (1996) 16310.

[42] N.E. Christensen, I. Gorczyca, Phys. Rev. B 50 (1994) 4397.

[43] A.F. Wright, J. Appl. Phys. 82 (1997) 2833.

[44] K. Karch, J.M. Wagner, F. Bechstedt, Phys. Rev. B 57 (1998) 7043.

[45] M.B. Nardelli, K. Rapcewicz, J. Bernholc, Phys. Rev. B 55 (1997) R7323.

[46] S.K. Pugh, D.J. Dugdale, S. Brand, R.A. Abram, Semicond. Sci. Technol. 14 (1999) 23.

[47] B. Amin, I. Ahmad, M. Maqbool, 26 (2009) 2180.

[48] L.C. Duda, C.B. Stagarescu, J. Downes, K.E. Smith, D. Korakakis, T.D. Moustakus, J. Guo, J. Nordgren, Phys. Rev. B 58 (1928).

[49] T.H. Gfroerer, L.P. Priestley, F.E. Weindruch, M.W. Wanless, Appl. Phys. Lett. 80 (2002) 4570.

[50] M.L. Benkhedir, M.S. Aida, A. Stesmans, G.J. Adriaenssens, J. Optoelectron. Adv. Mater. 7 (2005) 329.

[51] H. Tributsch, Naturforsch. A 32A (1977) 972.

[52] D. Penn, Phys. Rev. 128 (1962) 2093.

[53] B. Amin, Iftikhar Ahmad, M. Maqbool, S. Goumri-Said, R. Ahmad, J. Appl. Phys. 109 (2011) 023109.

[54] L.J. Wang, A. Kuzmich, A. Dogariu, Nat. Lond. 406 (2000) 277.

[55] D. Mugnai, A. Ranfagni, R. Ruggeri, Phys. Rev. Lett. 84 (2000) 4830.

[56] A. Bhattacharyya, S. Lyer, E. Iliopoulos, A.V. Sampath, J. Cabalu, I. Friel, J. Vac. Sci. Technol. B 20 (2002) 1229.

[57] T. Someya, Y. Arakawa, Appl. Phys. Lett. 73 (1998) 3653.

[58] G.K.H. Madsen, K. Schwarz, P. Blaha, D.J. Singh, Phys. Rev. B 68 (2003) 125212.

[59] G.K.H. Madsen, D.J. Singh, Comput. Phys. Commun. 175 (2006) 67.

[60] M. Lundstrom, Fundamentals of Carrier Transport, second ed., Cambridge University Press, Cambridge, 2000.

[61] O. Rabin, L. Yu-Ming, M.S. Dresselhaus, Appl. Phys. Lett. 79 (2001) 81.

[62] T. Takeuchi, Mater. Trans. 50 (2009) 2359.

[63] Li Wang, Li-Dong Chen, Xi-Hong Chen, Wen-Bin Zhang, J. Phys. D Appl. Phys. 42 (2009) 045113.