2B1.3

# STRAIN-TUNING OF PERIODIC OPTICAL DEVICES: TUNABLE GRATINGS AND PHOTONIC CRYSTALS

Chee Wei Wong, Yong Bae Jeon, George Barbastathis and Sang-Gook Kim
Massachusetts Institute of Technology, Cambridge, MA 02139

## ABSTRACT
We demonstrate strain-tuning of periodic optical devices - diffractive gratings and photonic crystals - on a deformable membrane piezoelectrically actuated with sub-nanometer resolution. In the tunable gratings implementation, period changes up to 8.3 nm (0.21% membrane strain) and diffracted order angular changes up to 486 μradians at 10 V are measured, in agreement with the theoretical model. For the strain-tunable photonic crystal microcavity, first-order perturbation theory suggests a 4.2 nm wavelength shift in resonance at C-band optical signals. The fabricated microcavity, with 130 nm minimum feature size, shows resonance at 1555.4 nm and Q of 159.

## I. INTRODUCTION
We develop a concept of strain-tuning of periodic optical devices - diffractive gratings and photonic crystals - on a deformable membrane piezoelectrically actuated with sub-nanometer resolution. In the tunable diffractive gratings implementation, we present ultra-fine control of the diffraction angle. Prior work on tunable gratings involves "digital" control of an individual grating beam or a set of beams [1,2]. Work on analog tunable gratings involves either thermal actuation [3,4], or vertical and lateral movement of two vertically stacked grating structures [4]. Compared to these tunable grating implementations, our device concept enables more precise angular resolution (on the order of micro-radians) with a smaller tuning range [5].

For photonic crystals, sub-nanometer strain is desirable because it would enable tunable low-threshold microlasers, filters and signal routers in silicon microphotonics. In silicon microphotonics devices, tuning has been accomplished by thermal actuation due to the negligible electro-optic properties in silicon. In comparison to thermal means, piezoelectric strain-tuning provides significantly faster response, lower power consumption and better localization of tunability. Effect of static strain on the periodic lattice of coupled vertical microcavity resonators has been reported [6] and a theoretical design for shear-modulated 2-dimensional photonic crystals on bulk piezoelectrics has been proposed [7]. We present here the integrated piezoelectric strain-tuning of a photonic band gap microcavity with active tuning of the resonant frequency. The microcavity design we used is based on the work first reported by Foresi [8].

The general design concept of the strain-tunable platform for microphotonics is illustrated in Figure 1. The platform is double-anchored membrane comprising of either silicon and silicon oxide or platinum, and actuated by thin-film piezoelectric actuators. The applied strain is transferred to the optical element of interest, permitting active control of its optical response.

![](./images/812353503698616321_1.jpg)

Figure 1. Design schematic of the strain-tunable platform for microphotonics. A photonic band gap microcavity [8] is built on the deformable membrane. The membrane is actuated by thin-film piezoelectric actuators.

## II. TUNABLE DIFFRACTIVE GRATINGS
### A. Design
With the applied strain on membrane, the period of a superimposed diffraction grating is correspondingly tuned. In the small angle limit, the change in the diffracted angle Δθ is related to the grating period change as

$$
\Delta \theta \cong \frac{m \lambda \Delta d}{d^{2}}, \tag{1}
$$

where $m$ is the diffracted order, $\lambda$ the wavelength, $\Delta d$ the grating period change and $d$ the grating period. The grating period change is a linear response to the applied voltage on the piezoelectric actuators (in this case, a lead zirconate titanate, PZT) due to the small strain of less than 1%. The double-anchored membrane minimizes out-of-plane displacement of the gratings, which may result from either residual stress or the actuated piezoelectric films.

The membrane in-plane displacement modeling, along the grating period axis (defined as x-axis), begins with a piezoelectric bimorph model where the deformation, $\delta_x$, is expressed as [9]

$$
\delta_{x}=\frac{d_{31} E_{p z t} A V_{a}}{t_{p z t} k_{x}}, \tag{2}
$$

where $d_{31}$ is the piezoelectric coupling coefficient, $E_i$ the $i^{th}$ material Young modulus, $A_i$ the $i^{th}$ cross-sectional area, $V_a$ the applied voltage, $t_{pzt}$ thickness of PZT layer, $k_x$ the effective axial stiffness $=\sum_i E_iA_i/L$, and $L$ the beam length along the grating period axis. Boundary conditions are

---

TRANSDUCERS '03
The 12th International Conference on Solid State Sensors, Actuators and Microsystems, Boston, June 8-12, 2003
0-7803-7731-1/03/$17.00 ©2003 IEEE

applied to reflect the double-anchored membrane structure and the solution reached iteratively. For an isotropic wide membrane, $E_{i} \rightarrow E_{i} /\left(1-v_{i}^{2}\right)$ and $d_{31} \rightarrow d_{31}\left(1+v_{i}\right)$, where $v_{i}$ is the material Poisson's ratio. With our double-anchored membrane design parameters $(d_{31}=-100$ pC/N, $E_{pzt}=90$ GPa, $t_{pzt}=0.5$ $\mu \mathrm{m}$, and $L=200 \mu \mathrm{m}$), the analytical model predicts a 187 nm x-axis membrane displacement with a single actuator at 10 V and a 5.28 nm grating period change (0.13% membrane strain). For a 632.8 nm laser on a $4 \mu \mathrm{m}$ period grating, this period change corresponds to an angular change of 209 $\mu$radians for the first diffracted order.

We used a finite-element analysis tool (CoventorWare$^{\mathrm{TM}}$) to estimate the membrane out-of-plane bow when actuated. The calculated maximum vertical deflection is $1.941 \mu \mathrm{m}$ at the center of a $232 \mu \mathrm{m}$ long membrane with an applied voltage of 10 V. This bow shape profile is added as a non-uniform phase to the grating profile. At the Fourier plane, this is observed as a spatial spreading out of the first diffracted order energy, although the first order diffraction efficiency remains approximately unvaried at 20.3%. The membrane bow also contributes to the shift in the first diffracted order and needs to be taken into account for the precision design of specific miniaturized spectrometers and other optical telecommunication devices.

### B. Device fabrication
The microfabrication process of the analog tunable grating utilizes both surface and bulk micromachining. First, a 200 nm silicon nitride layer is deposited via PECVD and then patterned to form a hard-mask for a later KOH backside etch. A 220 nm Pt/Ti layer is then evaporated on the substrate and patterned to create the bottom electrode with lift-off. Sol-gel PZT is subsequently spun-on and annealed in repeated individual steps to create a high-quality PZT layer with $0.5 \mu \mathrm{m}$ thickness. The PZT layer is patterned by wet-etching [10] and the top electrode deposited with a second 220 nm Pt/Ti evaporation and lift-off procedure. Next, the diffractive grating is separately created with a 160 nm Pt lift-off with $2 \mu \mathrm{m}$ minimal linewidths. The double-anchored membrane is then defined with a $445 \mu \mathrm{m}$ KOH etch from the backside, followed by a $5 \mu \mathrm{m}$ Si RIE to release the membrane.

The fabricated device is shown in Figure 2. The completed PZT has a predominant perovskite phase aided by good adhesion between the bottom Pt/Ti electrode and the $\mathrm{SiO}_{2}$ diffusion barrier. The average grain size of the PZT film is on the order of $0.1 \mu \mathrm{m}$. Ferroelectric characterization suggests an excellent dielectric constant of above 1200 and a dielectric loss below 0.05. The coercive field and saturation polarization are estimated at 60 kV/cm and 67 $\mu \mathrm{C} / \mathrm{cm}^{2}$ respectively. Fatigue lifecycle experiments in the film suggest operation above $10^{10}$ cycles at 5 V. The power consumption of the PZT film at 10 V actuation is gauged at 30 nW. The fabricated binary phase grating also has a measured duty cycle varying between 42 to 66%, depending on the process conditions. First and second order diffraction efficiencies were measured at 7.6% and 5.0% respectively for the fabricated grating (without actuation), although higher efficiencies could be achieved with better process control on the grating profile.

![](./images/812353503698616321_2.jpg)

Figure 2. (a) Piezoelectric-actuated tunable grating under 120X magnification, (b) SEM cross-section of fabricated PZT actuator on Pt/Ti electrodes, (c) Magnified view of Pt gratings with $4 \mu \mathrm{m}$ period.

### C. Experimental characterization
The membrane deformation by the thin-film PZT actuators is measured with a Computer Microvision instrument [11]. This instrument reconstructs three- dimensional images of microscopic targets using the optical sectioning property of a light microscope and post-processes the combined images to analyze the target motion with nanometer precision.

![](./images/812353503698616321_3.jpg)

Figure 3. Measured period change against applied voltage for two different device designs. Both results match with the analytical model for a single set of material properties and with a single fitted $d_{31}$ coefficient at -100 pC/N.

Device 1, whose PZT length is $450 \mu \mathrm{m}$, demonstrated a $229 \pm 2$ nm total membrane displacement at 9 V. From tracking the displacements of the grating beams, an average period change of 8.3 nm (0.21% membrane strain) at 9 V

---

TRANSDUCERS '03
The 12th International Conference on Solid State Sensors, Actuators and Microsystems, Boston, June 8-12, 2003

actuation is observed. This corresponds to a theoretical diffracted angle change of 328 µradians for our fabricated device parameters. Device 2, with 200 µm PZT length, shows a 4.9 nm period change at 10 V (corresponding to 0.12% membrane strain and a theoretical 194 µradians diffracted angle change). The period change at 1 V for both devices is approximately 0.6 nm, calculated from total membrane displacement. Displacements below 1V are limited by noise in the measurement instrument. As summarized in Figure 3, both experimental device measurements are in good agreement (correlation coefficient $\rho \sim 0.9$) with the analytical formulation for a single fitted $d_{3j}$ coefficient of $-100 \pm 15$ pC/N. The material properties used in the analytical model are consistent in both plots and fall within the range reported in the literature. The membrane strain uniformity is estimated at 16% [5]. Comparison between released and unreleased membranes with respect to ambient vibration effects shows no discernable differences up to the first modal resonance, as measured with a laser vibrometer. In addition, a direct characterization of the $d_{33}$ coefficient [12] gives a value of 275.4 pC/N of the thin-film actuators, concurring with the estimated $d_{31}$ coefficient.

Measurement of the diffraction angular change was performed by imaging the first diffracted order onto a CCD camera. A 632.8 nm HeNe laser was utilized as the illumination source and the diffracted order image centroid was analyzed for various actuation voltages. At 10 V, the angular change is estimated at 486 µradians for a device with 450 µm PZT length when corrected for tilt in membrane. A device with 200 µm PZT length shows a correspondingly scaled diffracted angular change of 154 µradians at 10 V. Comparisons between the optical image centroid processing, mechanical membrane deformation measurements, and theoretical predictions show agreement within 15%, limited by uncertainty in membrane tilt and the strong dependence of the membrane actuation on the $d_{31}$ coefficient. Future work involves multi-cycle experiments with the possibility of feedback control to compensate for piezoelectric relaxation and aging.

## III. TUNABLE PHOTONIC CRYSTALS

### A. Design

The conceptual design of the strain-tunable photonic band gap microcavity is illustrated in Figure 1. The microcavity is defined through a defect in a set of periodic holes embedded in a dielectric waveguide. The optical resonant response can be thought of as analogous to a Fabry-Perot cavity (or a double potential barrier) such that resonance is dependent on defect length. The thin-film piezoelectric actuators apply strain along the waveguide, resulting in active control of the defect length of the microcavity. Thus, the resonant response is tuned by up to 0.3%. The waveguide channels light into and out of the microcavity through index-guiding in the plane normal to the direction of periodicity.

We employ first-order perturbation theory to obtain a semi-analytical result for the strain-induced shift in the microcavity resonance. Such methods ease the study of small modulations such as the 0.1% strain considered here. First, a closed-form solution for the hole boundary displacements is derived following classical mechanics [13]. The material boundary displacements are then numerically meshed and employed in a perturbation-theory formulation [14], which involves surface integrals of the unperturbed fields (obtained by finite-difference time-domain computation) with the perturbed material boundaries. The full 3D computation predicts a 0.3% shift in resonant wavelength (4.2 nm in the C-band centered at 1552 nm wavelength) for a 0.1% mechanical strain from a full 3D computation. Effects such as photoelasticity and waveguide out-of-plane bending were found to be secondary. Figure 4 illustrates the perturbed transmission shift, in addition to an unperturbed finite-difference time-domain transmission of the microcavity. The transmission is normalized to the intensity at the band edges, while a non-dimensional frequency is used given the scale-invariance of Maxwell's equations [15] in our length scales of interest.

![](./images/812353503698616321_4.jpg)

Figure 4. Computed transmission shift through perturbation theory [14] and finite-difference time-domain in photonic band gap of the microcavity. The frequency is non-dimensionalized with lattice constant $a$ and speed of light $c$.

### B. Device fabrication

Figure 4 also suggests the device length scales for operation at desired wavelengths: for resonance at optical telecommunications wavelengths of 1.55 µm, the photonic crystal lattice constant, $a$, is 420 nm. This requires minimum feature sizes at 130 nm between the waveguide and hole edges. X-ray lithography is employed to transfer the pattern from the mask to a PMMA resist. The mask is a $SiN_x$ membrane (3 µm thick) with 200 nm Au features written with electron-beam lithography. The resist image is then transferred to 50 nm of Cr hard mask with lift-off, and etched into a 212 nm single-crystal Si layer to form the

---
TRANSDUCERS '03
The 12th International Conference on Solid State Sensors, Actuators and Microsystems, Boston, June 8-12, 2003

microcavity waveguide. Figure 5 shows the scanning electron micrograph of the fabricated structure. The device is integrated on the thin-film piezoelectric actuator membrane, released through a combination of bulk KOH wet etching and $XeF_2$ dry etching.

![](./images/812353503698616321_5.jpg)

Figure 5. SEM of microcavity waveguide.

### C. Experimental characterization
A fiber lens assembly is used to couple 1430 to 1610 nm tunable laser diode sources, with transverse electric polarization and lock-in amplification, into the prepared input/output waveguide facets. A piezo-controlled stage with 10 nm resolution is used to couple the beam into the approximately 200 nm by 400 nm waveguide facets. The measured resonance is found at 1555.4 nm with a measured quality factor $Q$ of 159 for a static microcavity waveguide. Figure 6 shows the resonance within the photonic band gap. Experimental measurements of the tunable microcavity resonance are currently underway.

![](./images/812353503698616321_6.jpg)

Figure 6. Measured microcavity resonance within photonic band gap. Inset: top view of waveguide in transmission.

### IV. CONCLUSIONS
We have designed and fabricated tunable optical elements - photonic bandgap microcavity waveguides and diffractive gratings - using the concept of a strain-tunable membrane platform. Thin-film piezoelectric actuators not only provide sufficient force for actuation at low voltages (and low power consumption), but also allow for controlling tunability within fraction of a nanometer. Significant advantages over current thermo-optics methods include a faster response time and better localization for discrete tunability of individual microphotonic devices on high-density optical integrated circuits. The demonstration of the tunable diffractive grating shows tuning of the first diffracted order angle up to 486 $\mu$radians at 10 V, with minimum observable grating period displacements at approximately 0.6 nm at 1 V. The theoretical design and fabrication of the photonic band gap microcavity, involving various integrated micro- and nanofabrication techniques such as thin-film piezoelectric processing, bulk micromachining and X-ray nanolithography, suggest feasibility for tunable integrated silicon optics.

### V. ACKNOWLEDGEMENTS
The authors thank Steven Johnson, Peter Rakich, Minghao Qi, Juan Ferrara, James Daley, Erich Ippen, Henry Smith and Lionel Kimerling for their invaluable assistance towards the tunable photonic crystal work. The contributions by Salil Desai, Dennis Freeman, Dong-Guk Kim, Wei-Chuan Shih, Arnab Sinha, Kurt Broderick, Gregory Nielson and Carlos Hidrovo towards the tunable diffractive gratings work are also deeply appreciated.

### VI. REFERENCES
1. B. Apte et. al., *Solid State Sensors and Actuators Workshop*, Hilton Head, SC, pp.1-6, 1994.
2. G.B. Hocker et. al., *Solid State Sensors and Actuators Workshop*, Hilton Head, SC, pp.89-92, 2000.
3. X.M. Zhang and A.Q. Liu, *Optical MEMS 2000 IEEE/LEOS International Conference*, Kauai, HI, pp.25-26, 2000.
4. D.E. Sene et. al., *Proc. of IEEE MEMS Workshop*, San Diego, CA, pp.222-227, 1996.
5. C.W. Wong et., *Applied Optics* **42** (4), pp.621-626, 2003.
6. H. Pier et. al., *Nature* **407**, pp.880-883, 2000.
7. S.W. Kim and V. Gopalan, *Appl. Phys. Lett.* **78**, pp.3015-3017, 2001.
8. J.S. Foresi et. al., *Nature* **390**, pp.143-145, 1997.
9. M.S. Weinberg, *Jour. of Microelectromechanical Systems* **8** (4), pp.529-533, 1999.
10. W. Liu et. al., *Thin Solid Films* **371** (1-2), pp.254-258, 2000.
11. D.M. Freeman et. al., *Solid State Sensors and Actuators Workshop*, Hilton Head, SC, pp.150-155, 1998.
12. D.-G. Kim and H.-G. Kim, *Integrated Ferroelectrics* **24**, pp.107-119, 1999.
13. S.P. Timoshenko and J.N. Goodier, *Theory of Elasticity*, McGraw-Hill, New York, $2^{nd}$ edition, 1970.
14. S.G. Johnson et. al., *Phys. Rev. E* **65**, 066611, 2002.
15. J.D. Joannopoulos et. al., *Photonic Crystals: Molding the Flow of Light*, Princeton University Press, New Jersey, $1^{st}$ edition, 1995.

---
TRANSDUCERS '03
The 12th International Conference on Solid State Sensors, Actuators and Microsystems, Boston, June 8-12, 2003

205