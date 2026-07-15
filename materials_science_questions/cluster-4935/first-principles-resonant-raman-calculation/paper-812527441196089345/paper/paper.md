Review

Søren Raza* and Anders Kristensen

# Raman scattering in high-refractive-index nanostructures

https://doi.org/10.1515/nanoph-2020-0539
Received September 23, 2020; accepted November 30, 2020;
published online December 16, 2020

**Abstract:** The advent of resonant dielectric nanomaterials has provided a new path for concentrating and manipulating light on the nanoscale. Such high-refractive-index materials support a diverse set of low-loss optical resonances, including Mie resonances, anapole states, and bound states in the continuum. Through these resonances, high-refractive-index materials can be used to engineer the optical near field, both inside and outside the nanostructures, which opens up new opportunities for Raman spectroscopy. In this review, we discuss the impact of high-refractive-index nano-optics on Raman spectroscopy. In particular, we consider the intrinsic Raman enhancement produced by different dielectric resonances and their theoretical description. Using the optical reciprocity theorem, we derive an expression which links the Raman enhancement to the enhancement of the stored electric energy. We also address recent results on surface-enhanced Raman spectroscopy based on high-refractive-index dielectric materials along with applications in stimulated Raman scattering and nanothermometry. Finally, we discuss the potential of Raman spectroscopy as a tool for detecting the optical near-fields produced by dielectric resonances, complementing reflection and transmission measurements.

**Keywords:** high-refractive-index nanophotonics; Mie resonances; Raman spectroscopy; surface-enhanced Raman spectroscopy

---

## 1 Introduction

Optical nanomaterials with a high refractive index are receiving high and increasing attention due to their ability to support low-loss optical resonances [1–3]. The most prominent of which are Mie-type resonances, which arise when materials with high refractive index $n$ are structured on a scale comparable to the wavelength of light inside the material $\lambda/n$, where $\lambda$ is the wavelength of light in free space. Examples of such materials include silicon, gallium arsenide, gallium phosphide, titanium dioxide, and transition metal dichalcogenides [4]. Mie resonances can be both electric or magnetic in nature [5] and enable control over different properties of light, such as polarization, amplitude and phase. In addition to Mie resonances, high-refractive-index nanostructures also host other intriguing effects, such as the anapole state [6], bound states in the continuum [7], and supercavity modes [8]. These desirable optical properties have turned high-refractive-index nanostructures into key ingredients in the design of novel nanophotonic devices, such as metasurface-based control of light [9], metalenses [10], structural color [11], Huygens' surfaces [12], lasing [13], directional control of emitters [14, 15], biosensing [16, 17], amplification of nonlinear response [18], and active control of light [19, 20].

The common denominator for resonant high-refractive-index nanostructures is that they provide strong light confinement with an accompanying enhancement of the electromagnetic near-fields. This opens up new possibilities for controlling and enhancing Raman scattering, since the Raman intensity scales dramatically with the electric near-field intensity. Raman spectroscopy measures the inelastic scattering of photons due to vibrations in molecules or phonon modes in crystalline materials. Here, we focus primarily on the latter since crystalline dielectric nanostructures show prominent phonon response, which is detectable in Raman spectroscopy. The typically weak Raman signal from phonon modes can be enhanced by engineering the dielectric nanostructure to support optical resonances, which has applications in nanoscale Raman lasers and nanothermometry. Conversely, the optical resonances may be designed to enhance the near-field outside the nanostructure for molecular Raman sensing, such as in surface-enhanced Raman spectroscopy. These applications highlight the importance of Raman spectroscopy as well as

*Corresponding author: Søren Raza, Department of Physics, Technical University of Denmark, DK-2800 Kongens Lyngby, Denmark,
E-mail: sraz@dtu.dk. https://orcid.org/0000-0002-0296-7202
Anders Kristensen, Department of Health Technology, Technical University of Denmark, DK-2800 Kongens Lyngby, Denmark

Open Access. © 2020 Søren Raza and Anders Kristensen, published by De Gruyter. This work is licensed under the Creative Commons Attribution 4.0 International License.
![](./images/812527441196089345_1.jpg)

optimizing high-refractive-index nanostructures for maximal Raman enhancement.

The aim of this review is to provide an overview of Raman scattering in optical nanomaterials with a high refractive index ($n > 2$) and discuss future directions. In Section 2, we review the state-of-the-art of intrinsic Raman enhancement due to resonant dielectric nanostructures. We find that a range of different silicon nanostructures, including nanowires, nanoparticles, and nanodisks, demonstrate resonantly enhanced Raman signal of the silicon optical phonon mode. Section 3 is devoted to the theoretical description of spontaneous Raman scattering due to phonon modes in such structures. Here, we derive an expression for the Raman intensity in the backscattering configuration using the optical reciprocity theorem and find that the Raman enhancement is linked to the enhancement of the stored electric energy. Section 4 focuses on emerging applications of Raman spectroscopy using high-refractive-index nanostructures, including surface-enhanced Raman spectroscopy, stimulated Raman scattering, nanothermometry, and near-field detection. Finally, Section 5 concludes the review.

## 2 Raman enhancement in high-index nanostructures

The ability of high-refractive-index nanostructures to resonantly confine light can lead to a dramatic enhancement in intrinsic Raman scattering. One of the first works to experimentally demonstrate this effect was performed by Murphy et al. [21], where they observed a Raman enhancement of the optical phonon mode in different silicon nanostructures. Inspired by earlier theoretical work [22], Murphy et al. showed that in particular silicon nanoparticles with diameters of approximately 100 nm produced a 100-fold enhancement in the Raman signal, when excited at 488 nm wavelength. They attributed the Raman enhancement to the excitation of the magnetic dipole resonance, which occurs at a wavelength of $\lambda_{\text{MD}} \approx nD$, where $n$ and $D$ denote the refractive index and diameter of the nanoparticle, respectively. While these initial results were exciting, the importance of Raman enhancement due to Mie resonances was not appreciated until the pioneering work by Hayashi et al. [23] Here, the authors systematically studied the Raman enhancement due to resonant gallium phosphide (GaP) nanoparticles in a broad size range. They demonstrated that Raman scattering from both the phonon modes in GaP as well as Raman signal from nearby molecules could be resonantly enhanced, opening up the possibility of performing surface-enhanced Raman spectroscopy without metals.

The results were later extended to nanowire geometries, which support polarization-dependent Mie resonances. In particular, Cao et al. [24] demonstrated a strong Raman enhancement in micrometer-long nanowires and nanocones made of silicon (Figure 1a). By measuring from the base to the tip of the nanocone, the authors tracked the Raman enhancement as a function of the local diameter of the nanocone. Here, a continuous increase in the Raman enhancement of the optical phonon line is observed as the diameter of nanowires decreases. The measurements were performed with several different excitation wavelengths as well as different polarization states of the incident light. The authors interpreted their results using Mie theory for infinite cylinders, which agreed with the continuous increase in Raman enhancement, but also showed Mie-enhanced peaks at specific diameters. However, such diameter-specific enhancements were not clearly observed in the experiments, presumably due to the finite size of the laser spot, which averages the Raman signal across a large range of local diameters. Shortly after these results, Raman scattering measurements on GaP nanowires of varying diameters were reported by Chen et al. [25]. Raman enhancement of the longitudinal optic and transverse optic phonon modes in GaP were observed at specific diameters, where the nanowires supported Mie resonances. In addition, the authors also observed Raman enhancements due to standing waves along the length of the GaP nanowires due to their few-micrometer length. Another study by Lopez et al. [26] on tapered silicon nanowires confirmed the diameter-dependent Raman enhancement due to cylindrical Mie resonances.

In recent years, there has been a shift in focus from nanowires to nanoparticles, which offer subwavelength confinement in three dimensions. Such high-refractive-index nanoparticles of different shapes, such as spherical and disks, host of variety of Mie resonances with intriguing properties. A particular enlightening geometry is that of a spherical nanostructure as it lends itself to an exact description based on analytical Mie theory. Dmitriev et al. [27] systematically studied the diameter-dependent Raman intensity of the optical phonon mode in crystalline silicon nanoparticles of spherical shape (Figure 1b). The authors experimentally observed a 140-fold enhancement of the Raman intensity due to the magnetic dipole resonance, which confines light strongly inside the silicon nanoparticle. In contrast, the electric dipole resonance confines most of the light outside the nanoparticle, leading to a modest Raman enhancement. These results were subsequently extended to polycrystalline silicon nanodisks by

![](./images/812527441196089345_2.jpg)

Figure 1: Enhancement of spontaneous Raman scattering in silicon nanostructures.
(A) Raman enhancement in silicon nanowires and silicon nanocones of different diameters. The Raman measurements are performed with three different excitation wavelengths and with the incident electric field polarized along the main axis of the nanowires (TM). Adapted from the study by Cao et al. [24]. (B) Raman enhancement due to Mie resonances in spherical silicon nanoparticles of different diameters D. When the ratio between the diameter and the wavelength in silicon $\lambda_{Si}$ is approximately unity, the magnetic dipole resonance is excited, which produces large internal field enhancements. Adapted from the study by Dmitriev et al. [27]. (C) Raman enhancement due to the anapole state in thin silicon nanodisk arrays. The anapole state occurs due to the destructive interference between the incident light and the toroidal and electric dipoles in the nanodisks, leading to low far-field radiation (extinction) and strong internal fields. Adapted from the study by Baranov et al. [30]. (D) Raman enhancement due to the magnetic dipole resonance in silicon nanodisk arrays. When the excitation laser wavelength matches the resonance wavelength of the magnetic dipole, a large enhancement in the Raman signal is observed. Adapted from the study by Matthiae et al. [28].

Matthiae et al. [28], who experimentally demonstrated a 100-fold enhancement of the Raman intensity due to the magnetic dipole resonance (Figure 1d). For thin nanodisks with large diameter-to-height aspect ratio, other optical effects occur beyond the fundamental Mie resonances. In such systems, the toroidal and electric dipole moments can interfere destructively in the far-field, leading to the optically dark feature known as the anapole state [6, 29]. Interestingly, the reduced far-field scattering of the anapole state is accompanied by a strong near-field enhancement. This intriguing interference effect was exploited by Baranov et al. [30] to demonstrate an 80-fold enhancement in the Raman intensity from polycrystalline silicon nanodisks (Figure 1c). In contrast to the Raman enhancement based on radiative Mie resonances (e.g., the magnetic dipole), the maximal anapole-enhanced Raman intensity coincides with a minimum in the far-field extinction. Consequentially, Raman scattering offers a route to reveal not only radiative resonances but also nonradiative states in high-refractive-index nanostructures. This insight was harnessed by Baryshnikova et al. [31] to reveal low-radiative magnetic quadrupole modes in silicon nanoparticles on glass and gold substrates. Raman enhancements have also been reported from silicon nanostructures of octahedral shape [32, 33] as well as irregular nanostructured silicon surfaces [34–37].

These recent advancements provide insight into the intrinsic Raman scattering from resonant dielectric nanostructures, which may be exploited in different applications such as those discussed in Section 4. However, several venues still remain unexplored. In particular, there have been no studies on the angular distribution of

the Raman scattering from high-refractive-index nano-
structures, and whether or not the Raman scattering may
be directed in a controllable fashion, akin to the Kerker
condition seen for elastic light scattering [38–40] and
dipole emission [14, 15]. Such directional Raman scattering
[41, 42] may boost the detected Raman signal and act in
concerto with the Raman enhancement due to near-field
enhancements. In addition, there have been limited
studies on nanostructures without in-plane symmetry,
where the polarization of the incident and Raman scattered
light is expected to play a role in the Raman signal. Indeed,
as we show in the next section, polarized Raman spec-
troscopy of dielectric nanostructures provides information
on the stored electric energy, which is strongly related to
linear and nonlinear light–matter interactions.

## 3 Theory of Raman enhancement

Raman scattering describes the inelastic scattering of
photons due to vibrational states in molecules or phonon
modes in a crystalline material. The theoretical description
of Raman scattering in the picture of classical electro-
magnetism is similar for both types of system. However, in
this section, we only outline the theoretical description of
inelastic scattering from phonon modes, as we are pri-
marily interested in the intrinsic Raman signal from
subwavelength-scale nanostructures. The Raman signal
stems from a two-step process. The first involves the exci-
tation of the phonon due to an incident electromagnetic
field $\mathbf{E}_0$ at the frequency $\omega_{\text{ex}}$. The excitation frequency and
the spatial profile of the exciting field depend on the laser
source and the optical system used to focus the illumina-
tion. This is often suitably approximated with a mono-
chromatic plane wave. The second step is the emission
of light due to the excited phonon modes occurring at the
Stokes-shifted frequency $\omega_{\text{em}} = \omega_{\text{ex}} - \Omega$, where $\Omega$ is the
phonon frequency. As the polarization induced by the
phonon modes extends only few interatomic distances, the
phonon emission is approximated by that of a point electric
dipole. This theoretical model for Raman scattering was
first described in a seminal paper by Chew et al. [22]. The
authors used Mie theory to analytically calculate the
Raman scattering from molecules embedded in spherical
particles. Notably, their results show that both the excita-
tion and emission processes depend on the electromag-
netic modes of the spherical particle (at the excitation and
emission frequencies, respectively), implying that a sig-
nificant enhancement of the Raman signal can occur under
resonant conditions.

Having outlined the general physical process, we now
take a closer look at the mathematical description of the
Raman enhancement. We consider an arbitrarily shaped
dielectric nanostructure with relative permittivity $\varepsilon$, which
is illuminated by a monochromatic plane wave with
amplitude $E_0$ and frequency $\omega_{\text{ex}}$ (Figure 2a). The nano-
structure may be placed in an inhomogeneous environ-
ment, such as on a substrate. The incident field induces a
Raman polarization in the nanostructure, which in the
point-dipole approximation can be written as

$$
\mathbf{p}\left(\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}\right)=\boldsymbol{\alpha}_{\mathrm{R}}\left(\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}\right) \mathbf{E}\left(\mathbf{r}, \omega_{\text{ex}}\right) \tag{1}
$$

Here, $\boldsymbol{\alpha}_{\mathrm{R}}\left(\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}\right)$ is the Raman polarizability tensor for a
particular phonon mode, and $\mathbf{E}\left(\mathbf{r}, \omega_{\text{ex}}\right)$ denotes the local
electric field at the dipole position $\mathbf{r}$ set up by the incident
field. It is of value to note that the local electric field can be
significantly enhanced compared to the incident field
under resonant conditions. The total Raman intensity
emanating from the dipole can be calculated by integrating
the Poynting vector over a spherical surface which en-
compasses the nanostructure. Dmitriev et al. [27] devel-
oped a Green's function approach for calculating the
Raman intensity from a spherical high-index nanoparticle,
which was subsequently generalized by Frizyuk et al. [43]
to particles of arbitrary shape. In the latter, the authors
show that the Raman intensity from a single phonon mode
can be written in an enlightening way

$$
I_{\mathrm{R}}=\frac{\omega_{\mathrm{em}}^{4}}{12 \pi \varepsilon_{0} c^{3}} \int_{V} F_{\mathrm{P}}\left(\mathbf{r}, \omega_{\mathrm{em}}\right)\left|\mathbf{p}\left(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}}\right)\right|^{2} \mathrm{d}^{3} \mathbf{r}, \tag{2}
$$

where $c$ is the speed of light in vacuum, $F_{\mathrm{P}}$ is the Purcell
factor, and the integration is performed over the volume $V$
of the nanostructure. From Eq. (2), we see that the Raman
intensity depends on both the excitation and emission
processes. The former may be enhanced through a large
local electric field, as seen from Eq. (1), while the latter is
enhanced due to the Purcell effect, namely an increase in
the optical density of states. In addition, the integral in Eq.
(2) highlights the spontaneous nature of Raman emission,
since each excited dipole contributes incoherently to the
Raman intensity emanating from the nanostructure.

The derivation of Eq. (2) assumes that the Raman
photons emitted in all directions are collected by the de-
tector (i.e., a solid angle of $4\pi$ steradians). However, such
Raman measurements are rare, and the most common
Raman setups collect Raman photons in the backscattering
(BS) configuration. In this configuration, the objective lens,
which focuses the incident light, is also used to collect
the Raman signal, akin to reflection measurements. For
comparison between BS measurements and theory,

![](./images/812527441196089345_3.jpg)

Figure 2: Simulated Raman enhancements.
(A) Schematic of inelastic Raman scattering in dielectric nanostructures. The incident field with frequency $\omega_{\text{ex}}$ excites the phonon mode, which subsequently emits light at the Stokes-shifted frequency $\omega_{\text{em}}$. (B-D) Simulated Raman enhancement as a function of excitation wavelength in different silicon nanostructures. The insets show the field profiles of the Raman-enhancing resonances supported by the nanostructures. The particle sizes are $R = 110$ nm, $(R, h) = (110, 200)$ nm, and $(R, h) = (170, 50)$ nm, respectively. (E) Raman and stored electric energy enhancements in silicon nanospheres of varying diameter at a fixed excitation wavelength.

we now derive an expression for the Raman intensity in the BS configuration. We neglect the effect of the numerical aperture of the objective lens, and assume that the excitation light impinges at normal incidence along the $z$-axis. Likewise, the Raman signal is collected along the direction of the $z$-axis. The intensity of light emitted in a given direction from a Raman dipole is given by radial component of the Poynting vector, which in the BS configuration simplifies to $\mathbf{S} \cdot \hat{\mathbf{z}}$. The objective lens, which collects the emitted signal, is typically placed many wavelengths away from the nanostructure. This allows us to consider the Poynting vector in the far-field $\mathbf{S}^{\text{ff}}$, where the electric field is transverse and has only $x$ and $y$ components. With these considerations in mind, we may write the Raman intensity in the BS configuration from a single Raman dipole $I_{\text{dp}}$ as

$$
I_{\text{dp}} = \mathbf{S}^{\text{ff}} \cdot \hat{\mathbf{z}} = \frac{1}{2} \varepsilon_{0} c \left( \left| E_{\text{x}}^{\text{ff}} \right|^{2} + \left| E_{\text{y}}^{\text{ff}} \right|^{2} \right). \tag{3}
$$

Consequently, the Raman intensity from a single Raman dipole is now reduced to determining the electric far-field components, $E_{\text{x}}^{\text{ff}}$ and $E_{\text{y}}^{\text{ff}}$. These can be expressed in terms of the electric field at the position of the dipole $\mathbf{r}$ by using the optical reciprocity theorem [44]. The reciprocity theorem states that the electric far-field emitted by the Raman dipole at position $\mathbf{r}$ is related to the electric field at position $\mathbf{r}$ produced by a dipole located in the far-field. In other words, the position of the emitter and detector can be interchanged. The radiation created by a dipole in the far-field at the position of the nanostructure reduces to that of a plane wave polarized along the dipole axis, and we may write [44]

$$
E_{\text{x}}^{\text{ff}} = \frac{\omega_{\text{em}}^{2}}{4 \pi \varepsilon_{0} c^{2} \left| E_{0} \right|} \mathbf{p} (\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}) \cdot \mathbf{E}^{X} (\mathbf{r}, \omega_{\text{em}}), \tag{4}
$$

$$
E_{\text{y}}^{\text{ff}} = \frac{\omega_{\text{em}}^{2}}{4 \pi \varepsilon_{0} c^{2} \left| E_{0} \right|} \mathbf{p} (\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}) \cdot \mathbf{E}^{Y} (\mathbf{r}, \omega_{\text{em}}). \tag{5}
$$

Here, $\mathbf{E}^{X} (\mathbf{E}^{Y})$ denotes the local electric field at the Raman dipole position $\mathbf{r}$ set up by an incident plane wave polarized along the $x$-axis ($y$-axis). From Eqs. (4) and (5), we notice that the problem of calculating the electric far-field from the Raman dipole reduces to calculating the local electric field produced by a plane wave source at the emission frequency. For an isotropic Raman tensor, $\mathbf{p} (\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}) = \alpha_{\text{R}} (\omega_{\text{ex}}, \omega_{\text{em}}) \mathbf{E} (\mathbf{r}, \omega_{\text{ex}})$, the intensity from a single Raman dipole becomes

$$
I_{\text{dp}} = \frac{\omega_{\text{em}}^{4} \left| \alpha_{\text{R}} E_{0} \right|^{2}}{32 \pi^{2} \varepsilon_{0} c^{3}} M (\mathbf{r}, \omega_{\text{ex}}, \omega_{\text{em}}), \tag{6}
$$

where we have introduced the enhancement factor

$$
\begin{aligned}
M\left(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}}\right)=& \frac{\left|\mathbf{E}\left(\mathbf{r}, \omega_{\mathrm{ex}}\right) \cdot \mathbf{E}^{X}\left(\mathbf{r}, \omega_{\mathrm{em}}\right)\right|^{2}}{\left|E_{0}\right|^{4}} \\
&+\frac{\left|\mathbf{E}\left(\mathbf{r}, \omega_{\mathrm{ex}}\right) \cdot \mathbf{E}^{Y}\left(\mathbf{r}, \omega_{\mathrm{em}}\right)\right|^{2}}{\left|E_{0}\right|^{4}}.
\end{aligned} \quad(7)
$$

Since each Raman dipole contributes incoherently to the Raman intensity, the total Raman signal emanating from a single phonon mode in the dielectric nanostructure becomes

$$
I_{\mathrm{R}}^{\mathrm{BS}}=\frac{\omega_{\mathrm{em}}^{4}\left|\alpha_{\mathrm{R}} E_{0}\right|^{2}}{32 \pi^{2} \varepsilon_{0} C^{3}} \int_{V} M\left(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}}\right) \mathrm{d}^{3} \mathbf{r}
$$

Eq. (8) is our main result and provides an approach for calculating the intrinsic Raman signal from dielectric nanostructures in the BS configuration. Although the enhancement factor $M$ requires two independent planewave calculations with different polarizations (along $x$ and $y$), such calculations are typically computationally inex-pensive compared to those involving a dipole emitter.

An interesting special case of Eq. (8) is that of polarized detection parallel to the excitation polarization. Here, the enhancement factor simplifies to a single plane-wave calculation at two different frequencies

$$
M_{\mathrm{pol}}\left(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}}\right)=\frac{\left|\mathbf{E}\left(\mathbf{r}, \omega_{\mathrm{ex}}\right) \cdot \mathbf{E}\left(\mathbf{r}, \omega_{\mathrm{em}}\right)\right|^{2}}{\left|E_{0}\right|^{4}}.
$$

For polarized measurements, the Raman intensity is closely related to the enhancement of the stored electric energy density, $W=u_{\mathrm{E}} / u_{0}=\varepsilon|\mathbf{E}|^{2} /\left|E_{0}\right|^{2}$, where $u_{\mathrm{E}}$ and $u_{0}$ denote the electric energy density in the nanostructure and free space, respectively. Dielectric nanostructures for Raman applications are therefore more suitably optimized with respect to the stored electric energy rather than far-field quantities, such as the scattering cross section.

Figure 2b–d shows simulation results of the Raman enhancement in individual silicon nanostructures of different shapes, when tuning the excitation wavelength. The simulations are performed in COMSOL Multiphysics (ver. 5.5), which numerically solves Maxwell’s equations using the finite-element method. We obtain the Raman enhancement by numerically evaluating Eqs. (8) and (9) and normalizing it to the BS Raman intensity from the same volume of bulk silicon, given by $I_{\mathrm{R} 0}^{\mathrm{BS}}=\left(\omega_{\mathrm{em}}^{4}\left|\alpha_{\mathrm{R}} E_{0}\right|^{2} \sqrt{\varepsilon} V\right) /\left(32 \pi^{2} \varepsilon_{0} C^{3}\right)$. With this normalization procedure, the Raman enhancement $R E$ becomes

$$
R E=\frac{I_{\mathrm{R}}^{\mathrm{BS}}}{I_{\mathrm{R} 0}^{\mathrm{BS}}}=\frac{1}{\sqrt{\varepsilon} V} \int_{V} M\left(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}}\right) \mathrm{d}^{3} \mathbf{r}.
$$

For the spherical and nanodisk particles (Figure 2b,c), we find that the magnetic dipole and quadrupole resonances provide the most prominent Raman enhancements. Indeed, the magnetic-type resonances provide stronger light localization inside the dielectric material than electric-type resonances. Interestingly, the magnetic quadrupole produces two peaks in the Raman spectrum due to the high quality factor of the mode, as also seen in the study by Frizyuk et al. [43]. The short-wavelength peak occurs when the emission wavelength matches the magnetic quadrupole resonance wavelength, while the long-wavelength peak is due to the enhancement of the excitation process. The low quality factor of the magnetic dipole mode masks this effect, leading to a single peak in the Raman enhancement. As for the thin nanodisk in Figure 2d, the Raman enhancement occurs due to the formation of an anapole state. As discussed in relation to Figure 1d, the anapole is a specific state occurring due to far-field destructive interference of the incident and scattered fields. Consequentially, it depends on the incident field and is therefore not an eigenmode of the system [45]. Nonetheless, the anapole state enhances the stored electric energy in the nanodisk and thereby also the Raman signal.

As an additional demonstration of the usefulness of Eqs. (8) and (9), we simulate the Raman enhancement of a silicon nanosphere of varying diameter $D$ at a fixed excitation wavelength of 633 nm (Figure 2e). We purposely choose to represent the Raman enhancement in terms of a dimensionless diameter $D / \lambda_{\mathrm{Si}}$ for direct comparison with the experimental measurements in Figure 1b. Here, $\lambda_{\mathrm{Si}}$ denotes the wavelength of light in silicon. We find excellent agreement between our theoretical model and the experimental results, despite not including the substrate in the simulations. The maximum value of the Raman enhancement differs, which is due to a difference in the normalization procedure. We also calculate the enhancement of the stored electric energy, which shows a similar profile to the Raman enhancement. The stored electric energy peaks at a different particle diameter, since it is only evaluated at the excitation wavelength, while the Raman enhancement has both the excitation and emission wavelengths as inputs. Nonetheless, the enhancement of the stored electric energy provides an excellent figure-of-merit for predicting the Raman enhancement of different optical resonances.

These results highlight that high-refractive-index nanostructures display a variety of different optical resonances, which are attractive for enhancing Raman scattering. In addition to the aforementioned Mie resonances, properly designed dielectric nanostructures can support Fano resonances [46], bound states in the continuum [7], as well as supercavity modes [8], which may offer unprecedented Raman enhancements due to their high quality

factors. In addition, new nanoscale design tools for tailoring the near-field have recently emerged [47, 48], which enable a more deterministic approach to dielectric Raman enhancements. Eq. (8) provides a straight-forward tool to evaluate the potential of these novel optical reso- nances. Our theoretical description of Raman scattering can be extended to include anisotropic Raman tensors as well as including the finite size of the numerical aperture of the objective lens [44]. The former can be achieved by defining a Raman tensor according to a suitable coordinate system, which ultimately leads to a modified expression for the enhancement factor $M(\mathbf{r}, \omega_{\mathrm{ex}}, \omega_{\mathrm{em}})$ in Eqs (6) and (8). These additional considerations may be important for ac- curate representation of certain experimental setups and anisotropic crystalline high-refractive-index materials, such as $MoS_{2}$ [49]. Nevertheless, based on our theoretical analysis, we expect the enhancement of the stored electric energy to provide an easy-to-use measure for designing Raman-enhancing dielectric nanostructures.

## 4 Applications

Controlling Raman scattering with high-refractive-index nanostructures has a number of attractive applications. In this section, we review recent advances in four different areas: surface-enhanced Raman spectroscopy (SERS), stimulated Raman scattering, nanothermometry, and the potential of detecting near-field enhancements using Raman scattering. We highlight the state-of-the-art in these areas of application and discuss possible future directions.

### 4.1 Surface-enhanced Raman spectroscopy

SERS is a vibrant and burgeoning field, which exploits enhanced Raman scattering from nanostructured surfaces for ultrasensitive sensing and related analytical techniques [50–52]. The unique Raman spectra of individual molecules provide a fingerprint-like identification method for their presence. However, Raman scattering from molecules is a weak process, and has therefore lead to the development of predominantly nanostructured metal surfaces, which provide dramatic enhancements of the local electric field due to plasmonic light confinement. For a comprehensive overview of the field, we refer the reader to the recent reviews by Alessandri and Lombardi and Langer et al. [53, 54]. Here, we highlight selected results using Mie resonances and related optical phenomena in high-refractive-index dielectric and semiconductor nanostructures.

The first observation of Mie-enhanced SERS can be traced to the work of Hayashi et al., where the authors demonstrated a 700-fold enhancement of the Raman scat- tering from molecules due to resonant GaP nanoparticles [23], see Figure 3a. The authors compared their experimentalresults with the near-field enhancement efficiency $Q_{NF}$  derived by Messinger et al. [55]. The near-field efficiency is strictly applicable only to spherical nanostructures and is obtained by integrating the scattered field at the sphere surface. Although the GaP nanoparticles tended to be more ellipsoidal in shape, the authors found qualitative agree- ment between theory and experiments, highlighting the electromagnetic contribution to the Raman enhancement.

In more recent years, an increasing number of different semiconductor materials have shown potential as SERS substrates due to a synergy of contributions to the Raman enhancements [53, 58]. As in metal-based SERS substrates, the electromagnetic enhancement plays a key role in enhancing the Raman signal from nearby molecules, which can be described within the theoretical framework developed in Section 3. In particular, Eqs. (6) and (7) describe the in- tensity from a single Raman dipole, which, in the context of SERS, is due to vibrational states of the molecule. The elec- tromagnetic Raman enhancement now stems from the enhanced fields outside the high-refractive-index nano- structure, which spatially overlap with the nearby molecules. Besides the electromagnetic part, contributions from the valence-band plasmon resonances, exciton resonances, and charge-transfer resonances between the molecule and the semiconductor turn out to play prominent roles in the Raman enhancement [59]. Combined with the high chemical sta- bility and tunable photoelectrical properties, semiconductor materials are becoming attractive for use in SERS. Tailoring the electromagnetic contribution using high-refractive-index optical phenomena may lead to unforeseen Raman en- hancements comparable to plasmonic-based SERS.

Alessandri [60] demonstrated the potential of high-refractive-index materials by using titanium dioxide $(TiO_{2})$  core-shell resonators, which support whispering-gallery- mode resonances [61], even in nanometer-thin shells. The author exploited the electromagnetically enhanced Raman signal to detect and monitor the photodegradation of low concentrations of methylene blue molecular aggregates. In another study, Rodriguez et al. [62] used Mie resonances in individual silicon nanoparticles to enhance the Raman signal from nearby molecules and found, quite surprisingly, that silicon nanoparticles may outperform gold nanoparticles in Raman enhancement. Caldarola et al. [63] capitalized on the large field enhancement occurring in the gap of a silicon nanodisk dimer [64,65] to demonstrate a $10^{3}$ enhancement in the Raman signal from an encapsulating polymer film. The

![](./images/812527441196089345_4.jpg)

Figure 3: Surface-enhanced Raman spectroscopy.
(A) Surface-enhanced Raman signal using high-refractive-index gallium phosphide nanoparticles of varying particle size. Adapted from the study by Hayashi et al. [23]. (B) Comparison of Raman signal from graphene from different surface architectures. The large electromagnetic fields produced by the coupling between the silicon nanoparticle and metal substrate outperform the other surfaces. Adapted from the study by Tseng et al. [56] (C) Surface-enhanced Raman signal using a silicon nitride photonic crystal (PhC), which supports a bound state in the continuum (BIC). Adapted from the study by Romano et al. [57].

authors also demonstrated a similar enhancement in the fluorescence signal from an assembly of emitters in the gap, which was later extended to the single-molecule limit by Regmi et al. [66]. Another promising approach to realizing large near-field enhancements is by placing high-refractive-index nanoparticles on a metal substrate [67]. Tseng et al. [56] exploited this architecture to amplify the Raman signal from graphene, which was placed in between silicon nanoparticles and a copper substrate (Figure 3b). The authors convincingly demonstrate that silicon nanoparticles on a copper substrate outperform other common architectures for surface-enhanced Raman spectroscopy. Related studies on similar hybrid dielectric-plasmon surfaces also demonstrated large enhancements of the Raman signal [68, 69].

An alternative class of optical resonances, which are promising for SERS, are the so-called bound states in the continuum (BICs). Originally an old idea from quantum mechanics [70], BICs have in recent years been revealed in nanophotonics [7]. BICs are an unusual type of wave resonance, which due to their radiationless nature can trap light for a long time—in principle, forever. This unique property of BIC modes leads to strong light–matter interaction and has been realized in different architectures, such as dielectric photonic crystal membranes [71–73] and dielectric metasurfaces [16, 17]. Romano et al. [57] applied BICs to SERS detection of crystal violet probe molecules (Figure 3c). The BIC mode is realized using a silicon nitride photonic crystal membrane. The authors find that the BIC-enhanced amplification of the Raman signal leads to a clear spectral signature of the probe molecules, which is absent when the Raman signal is collected outside the structure. The Raman enhancement factor exceeds $10^3$ and demonstrates that BICs can be used to strongly amplify the Raman signal in purely dielectric nanostructures.

The rich diversity of optical resonances supported by dielectric nanostructures, such as the discussed Mie resonances and BICs, provide new opportunities to design all-dielectric SERS substrates. Judiciously designed dielectric and semiconductor substrates enable large electromagnetic enhancements along with the aforementioned desirable chemical properties. High-refractive-index nanostructures may therefore usher a new era of SERS substrates, which can be independent on plasmonic hot-spots generated by noble metal nanostructures.

### 4.2 Stimulated Raman scattering

Stimulated Raman scattering (SRS) is essentially a light amplification process similar to stimulated emission, and

consequently the precursor to achieving Raman laser emission [74, 75]. In SRS, two optical fields are present in the Raman scattering material, one at the excitation frequency and the second at the Stokes-shifted emission frequency. This can be achieved by illuminating the material with two different lasers with suitable frequencies, or by using a single excitation laser and generating the Stokes-shifted light through spontaneous Raman scattering. In the latter situation, the Raman-shifted light can be trapped in a resonant cavity and thereby stimulate the generation of Raman photons. This process leads to the formation of a coherent beam at the Stokes-shifted frequency. The net result is that the energy of the excitation laser is transferred to the weaker Stokes beam, which experiences a dramatic amplification. SRS therefore leads to orders of magnitude larger intensities than spontaneous Raman scattering.

The SRS amplification is a third-order nonlinear process, which is characterized by the Raman gain coefficient of the material. Silicon has a relatively large bulk Raman gain [74], which has been exploited to realize Raman lasers, first on the centimeter-scale [76–78] and later shrunken to the micrometer-scale using a photonic crystal design [79]. Raman lasers have important applications in realizing compact light sources, especially for silicon photonics, where the indirect band gap of silicon hampers the development of lasers based on conventional stimulated emission. Shrinking the footprint of Raman lasers to the nanoscale is therefore desirable for dense integration into photonic circuits and for reducing the Raman lasing threshold power. This miniaturization can be achieved by manipulating the electromagnetic landscape through nanostructuring, which effectively tailors the quality factor and mode volume of the optical cavity. Wu et al. [80] exploited the Mie resonances in short GaP nanowires to demonstrate SRS with two orders of magnitude smaller threshold power than that reported using silicon photonic crystals. This was extended to silicon nanowires by Agarwal et al. [81], who demonstrated Mie-enhanced SRS with a $10^6$ increase in the net effective Raman gain compared to bulk silicon. Recently, Zograf et al. [82] observed SRS from subwavelength silicon nanodisks supporting higher-order Mie resonances (Figure 4a). The onset of SRS is marked by a deviation from the expected linear trend of spontaneous Raman scattering with increasing pump intensity. The authors optimized the SRS conditions by designing the nanodisk to support Mie resonances at both the excitation and emission wavelengths. In addition, they used a sapphire substrate as a thermal sink to mitigate the optically induced heating of the nanoparticle, which would otherwise have been detrimental for SRS.

![](./images/812527441196089345_5.jpg)

**Figure 4:** Applications of Raman spectroscopy.
(A) Stimulated Raman scattering from a silicon nanodisk for different laser pump intensities. The blue line corresponds to the expected trend of spontaneous Raman scattering. Adapted from the study by Zograf et al. [82]. (B) Raman scattering from a silicon nanoparticle for different laser pump intensities. The optical phonon mode broadens and redshifts due to nanoparticle heating. The insets show scanning electron microscope and thermal images. Adapted from the study by Zograf et al. [83]. (C) Tunable-excitation Raman spectroscopy of a silicon thin film and silicon nanodisk array, which support Fabry–Pérot and magnetic dipole resonances, respectively. Adapted from the study by Matthiae et al. [28].

These initial reports are promising demonstrations of nanoscale SRS empowered by optical resonances in high-refractive-index nanostructures. However, Raman laser emission in these systems has yet to be reported. This may be in part due to optically induced heating of the nanostructures, which shifts the phonon energy (details in Section 4.3), as well as the need for optical resonances with larger quality factors. The former was effectively mitigated by Zograf et al. [82] using a sapphire substrate, while the latter may be addressed using supercavity modes [8]. Supercavity modes are based on the physics of BICs and offer high quality factors with small mode volumes. Conventional lasing using BICs has been demonstrated [13,73], which underpins the promising potential of these modes for SRS and Raman lasing.

## 4.3 Nanothermometry

The phonon modes in a variety of crystalline materials are sensitive to temperature due to anharmonic effects in the vibrational potential energy [84]. In particular, the optical phonon mode of crystalline silicon shows high thermal sensitivity [85]. Such temperature dependence is marked by a shift and linewidth broadening of the optical phonon mode, which is detectable in the Raman spectrum. Zograf et al. [83] demonstrated that optically induced heating of crystalline silicon nanoparticles can be tracked using Raman spectroscopy (Figure 4b). By comparison with theory, the thermal-induced shift of the optical phonon peak can be converted to an absolute temperature, enabling nanoscale thermometry (inset of Figure 4b). The authors exploited the magnetic quadrupolar resonance in the silicon nanoparticle to demonstrate a fourfold enhancement of the light-to-heat conversion compared to a similar gold nanoparticle, which is often used in thermoplasmonics. As such, resonant silicon nanoparticles provide efficient optical heating despite their low optical losses and, importantly, their temperature can be directly monitored using Raman spectroscopy. These desirable properties have been exploited to track the temperature of silicon nanostructures during laser reshaping [86] and laser crystallization [87, 88], real-time observations of protein unfold in a hybrid plasmon-dielectric nanocavity [89], and, recently, for controllable drug release with high-refractive-index iron oxide nanoparticles [90]. These results demonstrate that Raman spectroscopy of high-refractive-index nanostructures offer emerging opportunities in biological applications, such as photothermal therapy, drug release, and nanosurgery.

## 4.4 Detecting near-field enhancements

The enhancement of spontaneous Raman scattering in dielectric nanostructures is linked to the enhancement of the internal near-field (cf. Eq. (8) and Figure 1). Thus, Raman spectroscopy offers a unique opportunity to measure the electric near-field inside dielectric nanostructures, which is challenging with existing measurement techniques. While existing near-field instruments, such as near-field scanning optical microscopy (NSOM) and cathodoluminescence (CL), have successfully probed the near-field distribution of Mie resonances on a deep subwavelength scale [65,91-94], they do not provide quantitative information on the enhancement. Quantitative measurements of the near-field are important for optimizing both linear and nonlinear light-matter interactions in the design of efficient optical nanodevices. In addition, the aforementioned techniques have drawbacks ranging from the perturbing tip in NSOM to specific sample requirements in CL. Given that Raman spectroscopy is a far-field technique, it cannot compete with SNOM and CL on spatial resolution, but instead inherits the benefits of far-field optical microscopy, which include versatility and noninvasiveness.

A current technical limitation of Raman spectroscopy for near-field-enhancement measurements is the fixed excitation wavelength set by the Raman laser. The fixed excitation wavelength entails that resonances can only be detected by fabricating multiple samples, which gradually shift the resonance wavelength across the Raman excitation wavelength (as seen in Figure 1). It is important from both a practical and scientific point-of-view to be able to measure the Raman signal in a broad range of wavelengths from individual samples. State-of-the-art tunable lasers offer a solution to this problem, as they cover most of the visible spectrum and have linewidths suitable for Raman spectroscopy [28, 95, 96]. Matthiae et al. [28] recently provided a proof-of-principle for tunable Raman spectroscopy of dielectric nanostructures. Using a tunable near-infrared laser, the authors demonstrated that both the Fabry-Pérot and the magnetic dipole resonance can be identified in the Raman signal from thin silicon films and silicon nanodisk arrays, respectively (Figure 4c). Interestingly, the Raman intensity peaks at a slightly shorter wavelength than the Fabry-Pérot resonance of the thin film. It turns out that this provides the best conditions for amplifying both the excitation and emission processes. On the other hand, the magnetic dipole resonance wavelength coincides with the Raman intensity peak. These initial results show the potential of tunable-excitation Raman spectroscopy for measuring the internal field enhancements due to Mie resonances and can be extended to other nanostructure

designs and spectral ranges. This insight is important for controlling near-field-based processes, such as spontaneous emission, strong coupling, and nonlinear interactions, and complements far-field transmission and reflection measurements.

It is also worth noting that the connection between the Raman signal and the near field has been exploited in plasmonic nanocavities [97, 98]. Here, judiciously positioned molecules act as Raman probes for the near-field in few-nanometer-sized gaps, enabling Ångstrom spatial mapping of the local electric field. These Raman measurements provide insight to the limit of plasmonic field enhancement as well as the field distribution in nanocavities, which would otherwise only be accessible using simulations. We anticipate that similar experimental insight into the internal field of dielectric nanostructures (using the material itself as the Raman probe) may propel the understanding and engineering of their optical response.

## 5 Conclusion
In conclusion, we have provided an overview of Raman scattering in high-refractive-index nanostructures. In particular, we have shown that the Raman intensity is linked to the enhancement of the stored electric energy, which can be significantly amplified through optical resonances in dielectric nanostructures. We have discussed emerging applications of enhanced Raman spectroscopy and discussed potential future directions for maximizing the Raman signal. We hope that the background provided here will drive future research into new designs of dielectric resonators with exciting Raman-based applications.

Author contribution: All the authors have accepted responsibility for the entire content of this submitted manuscript and approved submission.

Research funding: S. R. acknowledges support by the Independent Research Funding Denmark (7026-00117B).

Conflict of interest statement: The authors declare no conflicts of interest regarding this article.

## References
[1] A. I. Kuznetsov, A. E. Miroshnichenko, M. L. Brongersma, Y. S. Kivshar, and B. Luk'yanchuk, "Optically resonant dielectric nanostructures," *Science*, vol. 354, p. aag2472, 2016.

[2] S. Jahani and Z. Jacob, "All-dielectric metamaterials," *Nat. Nanotechnol.*, vol. 11, pp. 23–36, 2016.

[3] I. Staude and J. Schilling, "Metamaterial-inspired silicon nanophotonics," *Nat. Photonics*, vol. 11, pp. 274–284, 2017.

[4] R. Verre, D. G. Baranov, B. Munkhbat, J. Cuadra, M. Käll, and T. Shegai, "Transition metal dichalcogenide nanodisks as high-index dielectric Mie nanoresonators," *Nat. Nanotechnol.*, vol. 14, pp. 679–683, 2019.

[5] A. I. Kuznetsov, A. E. Miroshnichenko, Y. H. Fu, J. Zhang, and B. Lukyanchukl, "Magnetic light," *Sci. Rep.*, vol. 2, p. 492, 2012.

[6] K. V. Baryshnikova, D. A. Smirnova, B. S. Luk'yanchuk, and Y. S. Kivshar, "Optical anapoles: concepts and applications," *Adv. Opt. Mater.*, vol. 7, p. 1801350, 2019.

[7] C. W. Hsu, B. Zhen, A. D. Stone, J. D. Joannopoulos, and M. Soljacic, "Bound states in the continuum," *Nat. Rev. Mater.*, vol. 1, p. 16048, 2016.

[8] M. V. Rybin, K. L. Koshelev, Z. F. Sadrieva, et al., "High-Q supercavity modes in subwavelength dielectric resonators," *Phys. Rev. Lett.*, vol. 119, pp. 1–5, 2017.

[9] A. Arbabi, Y. Horie, M. Bagheri, and A. Faraon, "Dielectric metasurfaces for complete control of phase and polarization with subwavelength spatial resolution and high transmission," *Nat. Nanotechnol.*, vol. 10, pp. 937–943, 2015.

[10] M. Khorasaninejad, W. T. Chen, R. C. Devlin, J. Oh, A. Y. Zhu, and F. Capasso, "Metalenses at visible wavelengths: diffraction-limited focusing and subwavelength resolution imaging," *Science*, vol. 352, pp. 1190–1194, 2016.

[11] A. Kristensen, J. K. Yang, S. I. Bozhevolnyi, et al., "Plasmonic colour generation," *Nat. Rev. Mater.*, vol. 2, p. 16088, 2016.

[12] M. Decker, I. Staude, M. Falkner, et al., "High-efficiency dielectric Huygens' surfaces," *Adv. Opt. Mater.*, vol. 3, pp. 813–820, 2015.

[13] S. T. Ha, Y. H. Fu, N. K. Emani, et al., "Directional lasing in resonant semiconductor nanoantenna arrays," *Nat. Nanotechnol.*, vol. 13, pp. 1042–1047, 2018.

[14] A. F. Cihan, A. G. Curto, S. Raza, P. G. Kik, and M. L. Brongersma, "Silicon Mie resonators for highly directional light emission from monolayer MoS₂," *Nat. Photonics*, vol. 12, pp. 284–290, 2018.

[15] A. Vaskin, J. Bohn, K. E. Chong, et al., "Directional and spectral shaping of light emission with Mie-resonant silicon nanoantenna arrays," *ACS Photonics*, vol. 5, pp. 1359–1364, 2018.

[16] A. Tittl, A. Leitis, M. Liu, et al., "Imaging-based molecular barcoding with pixelated dielectric metasurfaces," *Science*, vol. 360, pp. 1105–1109, 2018.

[17] F. Yesilkoy, E. R. Arvelo, Y. Jahani, et al., "Ultrasensitive hyperspectral imaging and biodetection enabled by dielectric metasurfaces," *Nat. Photonics*, vol. 13, pp. 390–396, 2019.

[18] K. Koshelev, S. Kruk, E. Melik-Gaykazyan, et al., "Subwavelength dielectric resonators for nonlinear nanophotonics," *Science*, vol. 367, pp. 288–292, 2020.

[19] A. L. Holsteen, S. Raza, P. Fan, P. G. Kik, and M. L. Brongersma, "Purcell effect for active tuning of light scattering from semiconductor optical antennas," *Science*, vol. 358, pp. 1407–1410, 2017.

[20] A. L. Holsteen, A. F. Cihan, and M. L. Brongersma, "Temporal color mixing and dynamic beam shaping with silicon metasurfaces," *Science*, vol. 365, pp. 257–260, 2019.

[21] D. V. Murphy and S. R. J. Brueck, "Enhanced Raman scattering from silicon microstructures," *Opt. Lett.*, vol. 8, pp. 494–496, 1983.

[22] H. Chew, P. J. McNulty, and M. Kerker, "Model for Raman and fluorescent scattering by molecules embedded in small particles," *Phys. Rev. A*, vol. 13, pp. 396–404, 1976.

[23] S. Hayashi, R. Koh, Y. Ichiyama, and K. Yamamoto, "Evidence for surface-enhanced Raman scattering on nonmetallic surfaces: copper phthalocyanine molecules on GaP small particles," *Phys. Rev. Lett.*, vol. 60, pp. 1085–1088, 1988.

[24] L. Cao, B. Nabet, and J. E. Spanier, "Enhanced Raman scattering from individual semiconductor nanocones and nanowires," Phys. Rev. Lett., vol. 96, p. 157402, 2006.

[25] G. Chen, J. Wu, Q. Lu, et al., "Optical antenna effect in semiconducting nanowires," Nano Lett., vol. 8, pp. 1341-1346, 2008.

[26] F. J. Lopez, J. K. Hyun, U. Givan, I. S. Kim, A. L. Holsteen, and L. J. Lauhon, "Diameter and polarization-dependent Raman scattering intensities of semiconductor nanowires," Nano Lett., vol. 12, pp. 2266-2271, 2012.

[27] P. A. Dmitriev, D. G. Baranov, V. A. Milichko, et al., "Resonant Raman scattering from silicon nanoparticles enhanced by magnetic response," Nanoscale, vol. 8, pp. 9721-9726, 2016.

[28] M. Matthiae, K. E. S. Nielsen, A. Larroche, C. Zhou, A. Kristensen, and S. Raza, "Probing optical resonances of silicon nanostructures using tunable-excitation Raman spectroscopy," Opt. Express, vol. 27, pp. 38479-38492, 2019.

[29] A. E. Miroshnichenko, A. B. Evlyukhin, Y. F. Yu, et al., "Nonradiating anapole modes in dielectric nanoparticles," Nat. Commun., vol. 6, p. 8069, 2015.

[30] D. G. Baranov, R. Verre, P. Karpinski, and M. Käll, "Anapole- enhanced intrinsic Raman scattering from silicon nanodisks," ACS Photonics, vol. 5, pp. 2730-2736, 2018.

[31] K. V. Baryshnikova, K. Frizyuk, G. Zograf, et al., "Revealing low- radiative modes of nanoresonators with internal Raman scattering," JETP Lett., vol. 110, pp. 25-30, 2019.

[32] G. Mannino, A. Alberti, R. Ruggeri, S. Libertino, A. R. Pennisi, and G. Faraci, "Octahedral faceted Si nanoparticles as optical traps with enormous yield amplification," Sci. Rep., vol. 5, p. 8354, 2015.

[33] G. Faraci, M. Italia, R. Ruggeri, G. Litrico, and G. Mannino, "Strong Raman yield enhancement in large Si nanocrystals from ultraviolet to infrared: density and shape dependence," J. Raman Spectrosc., vol. 50, pp. 674-683, 2019.

[34] M. C. Lee, C. R. Huang, Y. S. Chang, and Y. F. Chao, "Double- resonance-enhanced Raman scattering in laser-recrystallized amorphous silicon film," Phys. Rev. B, vol. 40, pp. 10420-10424, 1989.

[35] F. M. Liu, B. Ren, J. H. Wu, et al., "Enhanced-Raman scattering from silicon nanoparticle substrates," Chem. Phys. Lett., vol. 382, pp. 502-507, 2003.

[36] K. Kitahara and A. Ishizaki, "Raman microscopy of silicon for electronic displays and solar cells: enhanced Raman scattering observed for microstructured surface," J. Appl. Phys., vol. 112, p. 123524, 2012.

[37] N. Bontempi, M. Salmistraro, M. Ferroni, L. E. Depero, and I. Alessandri, "Probing the spatial extension of light trapping- induced enhanced Raman scattering in high-density Si nanowire arrays," Nanotechnology, vol. 25, p. 465705, 2014.

[38] I. Staude, A. E. Miroshnichenko, M. Decker, et al., "Tailoring directional scattering through magnetic and electric resonances in subwavelength silicon nanodisks," ACS Nano, vol. 7, pp. 7824-7832, 2013.

[39] Y. H. Fu, A. I. Kuznetsov, A. E. Miroshnichenko, Y. F. Yu, and B. Luk'yanchuk, "Directional visible light scattering by silicon nanoparticles," Nat. Commun., vol. 4, p. 1527, 2013.

[40] S. Person, M. Jain, Z. Lapin, J. J. Sáenz, G. Wicks, and L. Novotny, "Demonstration of zero optical backscattering from single nanoparticles," Nano Lett., vol. 13, pp. 1806-1809, 2013.

[41] W. Zhu, D. Wang, and K. B. Crozier, "Direct observation of beamed Raman scattering," Nano Lett., vol. 12, pp. 6235-6243, 2012.

[42] D. Wang, W. Zhu, Y. Chu, and K. B. Crozier, "High directivity optical antenna substrates for surface enhanced Raman scattering," Adv. Mater., vol. 24, pp. 4376-4380, 2012.

[43] K. Frizyuk, M. Hasan, A. Krasnok, A. Alú, and M. Petrov, "Enhancement of Raman scattering in dielectric nanostructures with electric and magnetic Mie resonances," Phys. Rev. B, vol. 97, p. 085414, 2018.

[44] E. C. Le Ru and P. G. Etchegoin, "Rigorous justification of the |E| 4 enhancement factor in surface enhanced Raman spectroscopy," Chem. Phys. Lett., vol. 423, pp. 63-66, 2006.

[45] F. Monticone, D. Sounas, A. Krasnok, and A. Alù, "Can a nonradiating mode be externally excited? Nonscattering states versus embedded eigenstates," ACS Photonics, vol. 6, pp. 3108-3114, 2019.

[46] M. F. Limonov, M. V. Rybin, A. N. Poddubny, and Y. S. Kivshar, "Fano resonances in photonics," Nat. Photonics, vol. 11, pp. 543-554, 2017.

[47] S. Mignuzzi, S. Vezzoli, S. A. Horsley, W. L. Barnes, S. A. Maier, and R. Sapienza, "Nanoscale design of the local density of optical states," Nano Lett., vol. 19, pp. 1613-1617, 2019.

[48] V. Ginis, M. Piccardo, M. Tamagnone, et al., "Remote structuring of near-field landscapes," Science, vol. 369, pp. 436-440, 2020.

[49] T. D. Green, D. G. Baranov, B. Munkhbat, R. Verre, T. Shegai, and M. Käll, "Optical material anisotropy in high-index transition metal dichalcogenide Mie nanoresonators," Optica, vol. 7, pp. 680-686, 2020.

[50] M. Moskovits, "Surface-enhanced Raman spectroscopy: a brief retrospective," J. Raman Spectrosc., vol. 36, pp. 485-496, 2005.

[51] E. C. Le Ru, E. Blackie, M. Meyer, and P. G. Etchegoint, "Surface enhanced Raman scattering enhancement factors: a comprehensive study," J. Phys. Chem. C, vol. 111, pp. 13794-13803, 2007.

[52] P. L. Stiles, J. A. Dieringer, N. C. Shah, and R. P. Van Duyne, "Surface-enhanced Raman spectroscopy," Ann. Rev. Anal. Chem., vol. 1, pp. 601-626, 2008.

[53] I. Alessandri and J. R. Lombardi, "Enhanced Raman scattering with dielectrics," Chem. Rev., vol. 116, pp. 14921-14981, 2016.

[54] J. Langer, D. J. de Aberasturi, J. Aizpurua, et al., "Present and future of surface-enhanced Raman scattering," ACS Nano, vol. 14, pp. 28-117, 2020.

[55] B. J. Messinger, K. U. Von Raben, R. K. Chang, and P. W. Barber, "Local fields at the surface of noble-metal microspheres," Phys. Rev. B, vol. 24, pp. 649-657, 1981.

[56] Y. C. Tseng, T. Y. Lin, Y. C. Lee, C. K. Ku, C. W. Chen, and H. L. Chen, "Magnetic dipole resonance and coupling effects directly enhance the Raman signals of as-grown graphene on copper foil by over one hundredfold," Chem. Mater., vol. 30, pp. 1472-1483, 2018.

[57] S. Romano, G. Zito, S. Managò, et al., "Surface-enhanced Raman and fluorescence spectroscopy with an all-dielectric metasurface," J. Phys. Chem. C, vol. 122, pp. 19738-19745, 2018.

[58] W. Ji, B. Zhao, and Y. Ozaki, "Semiconductor materials in analytical applications of surface-enhanced Raman scattering," J. Raman Spectrosc., vol. 47, pp. 51-58, 2016.

[59] J. R. Lombardi and R. L. Birke, "Theory of surface-enhanced Raman scattering in semiconductors," J. Phys. Chem. C, vol. 118, pp. 11120-11130, 2014.

[60] I. Alessandri, "Enhancing Raman scattering without plasmons: unprecedented sensitivity achieved by TiO₂ shell- based resonators," J. Am. Chem. Soc., vol. 135, pp. 5541-5544, 2013.

[61] L. K. Ausman and G. C. Schatz, "Whispering-gallery mode resonators: surface enhanced Raman scattering without plasmons," *J. Chem. Phys.*, vol. 129, p. 054704, 2008.

[62] I. Rodriguez, L. Shi, X. Lu, B. A. Korgel, R. A. Alvarez-Puebla, and F. Meseguer, "Silicon nanoparticles as Raman scattering enhancers," *Nanoscale*, vol. 6, pp. 5666–5670, 2014.

[63] M. Caldarola, P. Albella, E. Cortés, et al., "Non-plasmonic nanoantennas for surface enhanced spectroscopies with ultra- low heat conversion," *Nat. Commun.*, vol. 6, p. 7915, 2015.

[64] P. Albella, M. A. Poyli, M. K. Schmidt, et al., "Low-loss electric and magnetic field-enhanced spectroscopy with subwavelength silicon dimers," *J. Phys. Chem. C*, vol. 117, pp. 13573–13584, 2013.

[65] R. M. Bakker, D. Permyakov, Y. F. Yu, et al., "Magnetic and electric hotspots with silicon nanodimers," *Nano Lett.*, vol. 15, pp. 2137–2142, 2015.

[66] R. Regmi, J. Berthelot, P. M. Winkler, et al., "All-dielectric silicon nanogap antennas to enhance the fluorescence of single molecules," *Nano Lett.*, vol. 16, pp. 5143–5151, 2016.

[67] Y. Yang, O. D. Miller, T. Christensen, J. D. Joannopoulos, and M. Soljačić, "Low-loss plasmonic dielectric nanoresonators," *Nano Lett.*, vol. 17, pp. 3238–3245, 2017.

[68] Z. Huang, J. Wang, Z. Liu, et al., "Strong-field-enhanced spectroscopy in silicon nanoparticle electric and magnetic dipole resonance near a metal surface," *J. Phys. Chem. C*, vol. 119, pp. 28127–28135, 2015.

[69] A. Maimaiti, P. P. Patra, S. Jones, and T. J. Antosiewicz, "Low-loss hybrid high-index dielectric particles on a mirror for extreme light confinement," *Adv. Opt. Mater.*, vol. 8, p. 1901820, 2020.

[70] J. von Neumann and E. Wigner, "Über merkwürdige diskrete Eigenwerte," *Phys. Z.*, vol. 30, pp. 465–467, 1929.

[71] C. W. Hsu, B. Zhen, J. Lee, et al., "Observation of trapped light within the radiation continuum," *Nature*, vol. 499, pp. 188–191, 2013.

[72] R. Gansch, S. Kalchmair, P. Genevet, et al., "Measurement of bound states in the continuum by a detector embedded in a photonic crystal," *Light Sci. Appl.*, vol. 5, p. e16147, 2016.

[73] A. Kodigala, T. Lepetit, Q. Gu, B. Bahari, Y. Fainman, and B. Kanté, "Lasing action from photonic bound states in continuum," *Nature*, vol. 541, pp. 196–199, 2017.

[74] L. Sirleto, A. Vergara, and M. Antonietta Ferrara, "Advances in stimulated Raman scattering in nanostructures," *Adv. Opt. Photonics*, vol. 9, pp. 169–217, 2017.

[75] R. C. Prince, R. R. Frontiera, and E. O. Potma, "Stimulated Raman scattering: from bulk to nano," *Chem. Rev.*, vol. 117, pp. 5070–5094, 2017.

[76] O. Boyraz and B. Jalali, "Demonstration of a silicon Raman laser," *Opt. Express*, vol. 12, p. 5269, 2004.

[77] H. Rong, R. Jones, A. Liu, et al., "A continuous-wave Raman silicon laser," *Nature*, vol. 433, pp. 725–728, 2005.

[78] H. Rong, A. Liu, R. Jones, O. Cohen, and D. Hak, "An all-silicon Raman laser," *Nature*, vol. 433, pp. 292–294, 2005.

[79] Y. Takahashi, Y. Inui, M. Chihara, T. Asano, R. Terawaki, and S. Noda, "A micrometre-scale Raman silicon laser with a microwatt threshold," *Nature*, vol. 498, pp. 470–474, 2013.

[80] J. Wu, A. K. Gupta, H. R. Gutierrez, and P. C. Eklund, "Cavity- enhanced stimulated Raman scattering from short GaP nanowires," *Nano Lett.*, vol. 9, pp. 3252–3257, 2009.

[81] D. Agarwal, M. L. Ren, J. S. Berger, J. Yoo, A. Pan, and R. Agarwal, "Nanocavity-enhanced giant stimulated Raman scattering in Si nanowires in the visible light region," *Nano Lett.*, vol. 19, pp. 1204–1209, 2019.

[82] G. P. Zograf, D. Ryabov, V. Rutckaia, et al., "Stimulated Raman scattering from Mie-resonant subwavelength nanoparticles," *Nano Lett.*, vol. 20, pp. 5786–5791, 2020.

[83] G. P. Zograf, M. I. Petrov, D. A. Zuev, et al., "Resonant nonplasmonic nanoparticles for efficient temperature-feedback optical heating," *Nano Lett.*, vol. 17, pp. 2945–2952, 2017.

[84] I. P. Ipatova, A. A. Maradudin, and R. F. Wallis, "Temperature dependence of the width of the fundamental lattice-vibration absorption peak in ionic crystals. II. Approximate numerical results," *Phys. Rev.*, vol. 155, pp. 882–895, 1967.

[85] M. Balkanski, R. F. Wallis, and E. Haro, "Anharmonic effects in light scattering due to optical phonons in silicon," *Phys. Rev. B*, vol. 28, pp. 1928–1934, 1983.

[86] M. Aouassa, E. Mitsai, S. Syubaev, et al., "Temperature-feedback direct laser reshaping of silicon nanostructures," *Appl. Phys. Lett.*, vol. 111, 2017, https://doi.org/10.1063/1.5007277.

[87] G. P. Zograf, Y. F. Yu, K. V. Baryshnikova, A. I. Kuznetsov, and S. V. Makarov, "Local crystallization of a resonant amorphous silicon nanoparticle for the implementation of optical nanothermometry," *JETP Lett.*, vol. 107, pp. 699–704, 2018.

[88] J. Berzinš, S. Indrišiūnas, S. Fasold, et al., "Laser-induced spatially-selective tailoring of high-index dielectric metasurfaces," *Opt. Express*, vol. 28, pp. 1539–1553, 2020.

[89] V. A. Milichko, D. A. Zuev, D. G. Baranov, et al., "Metal-dielectric nanocavity for real-time tracing molecular events with temperature feedback," *Laser Photonics Rev.*, vol. 12, p. 1700227, 2018.

[90] G. P. Zograf, A. S. Timin, A. R. Muslimov, et al., "All-optical nanoscale heating and thermometry with resonant dielectric nanoparticles for controllable drug release in living cells," *Laser Photonics Rev.*, vol. 14, p. 1900082, 2020.

[91] D. Permyakov, I. Sinev, D. Markovich, et al., "Probing magnetic and electric optical responses of silicon nanoparticles," *Appl. Phys. Lett.*, vol. 106, p. 171110, 2015.

[92] C. P. McPolin, G. Marino, A. V. Krasavin, et al., "Imaging electric and magnetic modes and their hybridization in single and dimer AlGaAs nanoantennas," *Adv. Opt. Mater.*, vol. 6, pp. 1–6, 2018.

[93] T. Coenen, J. Van De Groep, and A. Polman, "Resonant modes of single silicon nanocavities excited by electron irradiation," *ACS Nano*, vol. 7, pp. 1689–1698, 2013.

[94] J. van de Groep, T. Coenen, S. A. Mann, and A. Polman, "Direct imaging of hybridized eigenmodes in coupled silicon nanoparticles," *Optica*, vol. 3, pp. 93–99, 2016.

[95] A. D. McFarland, M. A. Young, J. A. Dieringer, and R. P. Van Duyne, "Wavelength-scanned surface-enhanced Raman excitation spectroscopy," *J. Phys. Chem. B*, vol. 109, pp. 11279–11285, 2005.

[96] N. S. Mueller, S. Juergensen, K. Höflich, S. Reich, and P. Kusch, "Excitation-tunable tip-enhanced Raman spectroscopy," *J. Phys. Chem. C*, vol. 122, pp. 28273–28279, 2018.

[97] W. Zhu and K. B. Crozier, "Quantum mechanical limit to plasmonic enhancement as observed by surface-enhanced Raman scattering," *Nat. Commun.*, vol. 5, p. 5228, 2014.

[98] C. Y. Li, S. Duan, B. Y. Wen, et al., "Observation of inhomogeneous plasmonic field distribution in a nanocavity," *Nat. Nanotechnol.*, 2020.