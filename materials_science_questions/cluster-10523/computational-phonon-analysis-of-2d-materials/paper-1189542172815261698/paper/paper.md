
# Strain-induced structural change and nearly-commensurate diffuse scattering in the model high-temperature superconductor HgBa_{2}CuO_{4+\delta}

Mai Ye, \( ^{1,*} \)  Wenshan Hong, \( ^{2,3} \)  Tom Laurin Lacmann, \( ^{1,\dagger} \)  Mehdi Frachet, \( ^{1,\ddagger} \)  Igor

Vinograd, \( ^{1,\S} \)  Gaston Garbarino, \( ^{4} \)  Sofia-Michaela Souliou, \( ^{1} \)  Michael Merz, \( ^{1,5} \) 

Rolf Heid, \( ^{1} \)  Amir-Abbas Haghighirad, \( ^{1}Yuan Li,^{2,3} \)  and Matthieu Le Tacon \( ^{1} \) 

 \( ^{1} \) Institute for Quantum Materials and Technologies,

Karlsruhe Institute of Technology, Kaiserstr. 12, 76131 Karlsruhe, Germany

 \( ^{2} \) International Center for Quantum Materials, School of Physics, Peking University, 100871 Beijing, China

 \( ^{3} \) Beijing National Laboratory for Condensed Matter Physics,

Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China

 \( ^{4} \) European Synchrotron Radiation Facility, BP 220, F-38043 Grenoble Cedex, France

 \( ^{5} \)  Karlsruhe Nano Micro Facility (KNMFi), Karlsruhe Institute of Technology, Kaiserstr. 12, 76131 Karlsruhe, Germany (Dated: October 27, 2025)

We investigate the strain response of underdoped  \( HgBa_{2}CuO_{4+\delta} \)  (Hg1201), by synchrotron X-ray diffraction and corresponding simulations of thermal diffuse scattering. The compression in the crystallographic a direction leads to relatively small expansion in the b and c directions, with Poisson ratios  \( \nu_{ba}=0.16 \)  and  \( \nu_{ca}=0.11 \) , respectively. However, the Cu-O distance in the c direction exhibits a notable 0.9% increase at 1.1% a-axis compression. We further find strain-induced diffuse scattering which corresponds to a new type of two-dimensional charge correlation. Interestingly, this signal is insensitive to the onset of superconductivity and instead corresponds to a short-range, nearly commensurate modulation with a wave vector close to  \( (0.5, 0, 0) \)  and a correlation length of approximately four unit cells. It closely resembles the charge order theoretically predicted in the phase diagram of the spin-liquid model with resonating valence bonds on a square lattice.

## I. INTRODUCTION

Strain tuning has emerged as a powerful tool for manipulating competing electronic orders and revealing new quantum phases in correlated systems: by modifying lattice symmetries, bond angles, and interatomic distances, strain can significantly alter the delicate balance between spin, charge, and superconducting orders, offering a controllable parameter to probe intertwined phenomena in the phase diagram  \( [1-13] \) . Notably, uniaxial pressure has been shown to influence superconducting transition temperatures  \( [1-4, 7] \)  and stabilize charge-density-wave (CDW) phases that are otherwise suppressed under strain-free conditions  \( [5, 6, 11] \) .

A striking example is the emergence of long-range three-dimensional (3D) charge-density-wave (CDW) order in the double copper–oxygen-layer compound  \( YBa_{2}Cu_{3}O_{y} \)  (YBCO). This order was first revealed under high magnetic fields [14, 15], and was later shown to be induced by suppressing the superconducting transition via uniaxial compression along the a-axis [5]. The observation of this otherwise hidden phase highlights a competing — or possibly intertwined — electronic order that coexists with, and is suppressed by, high-temperature superconductivity.

However, it remains an open question whether such strain-induced electronic ordering phenomena are universal across cuprate families or are limited to specific structural and electronic contexts. The special structure of YBCO, with its orthorhombic symmetry, CuO chains, and bilayer  \( CuO_{2} \)  planes, introduces unique interlayer couplings and charge reservoirs that may influence the CDW formation under strain [11, 16]. Thus, extending the investigation to structurally simpler cuprates is crucial for disentangling intrinsic effects from sample-specific characteristics.

A natural choice for such exploration is the cuprate system  \( HgBa_{2}CuO_{4+\delta} \)  (Hg1201), which has tetragonal symmetry, a single copper-oxygen layer, and minimal disorder [17]. The crystal structure of Hg1201, whose space group is  \( P4/mmm \)  (No.123), is shown in Fig. 1 (a). The absence of structural anisotropy due to its tetragonal symmetry implies that the response of Hg1201 to directional strain may differ fundamentally from that of orthorhombic YBCO. Strain-induced symmetry breaking which lifts the four-fold electronic degeneracies could, in principle, stabilize new ordering patterns. Moreover, the absence of bilayer splitting and chain contributions makes Hg1201 an ideal platform for studying the intrinsic properties of the  \( CuO_{2} \)  plane. Previous X-ray scattering studies have identified short-range 2D CDW order with a wavevector  \( H = 0.27 \, r.l.u. \)  in samples with  \( T_{c} = 79 \, K \)  [18]. As the doping level is reduced and superconductivity
 

(a)

![](./images/1189542172815261698_1.jpg)

(b)

![](./images/1189542172815261698_2.jpg)

FIG. 1. (a) Crystal structure of  \( HgBa_{2}CuO_{4+\delta} \) . The doped oxygen atoms stay in the Hg layers. (b) The Razorbill CS200T strain cell used to apply strain to the sample.

weakens (e.g.,  \( T_{c} = 55 K \) ), the CDW wavevector increases to  \( H = 0.29 r.l.u. \)  [18, 19], suggesting a close interplay between charge order and carrier concentration. Nevertheless, the CDW correlation length in Hg1201 remains very short: typically no more than a few lattice spacings—and no evidence for any long-range 3D CDW order has been reported to date. Whether an in-plane strain field can reinforce this fragile CDW order, modify its wavevector, or even induce a qualitatively new electronic phase, such as 3D CDW or electronic nematicity [20], is an unresolved theoretical and experimental issue.

In this work, we investigate the structural changes and diffuse scattering features induced by a-axis compressive strain in  \( HgBa_{2}CuO_{4+\delta} \)  with  \( T_{c}=78K \) . Our results reveal that the strain dependence of the lattice parameters in Hg1201 deviates significantly from that observed in YBCO, reflecting the different crystallographic and bonding environment of the Hg-based cuprate. Strikingly, we observe a strain-induced diffuse scattering signal with a wavevector near H=0.5 r.l.u., which is not only distinct from the weak 2D CDW signal typically seen in Hg1201 but also suggests a new form of structural or electronic modulation. This diffuse scattering exhibits saturation at 0.2% strain and shows little temperature dependence, hinting at a strain-stabilized, potentially static order.

## II. EXPERIMENTAL AND COMPUTATIONAL DETAILS

## A. Sample preparation

Single crystals of  \( HgBa_{2}CuO_{4+\delta} \)  were grown using a self-flux method [21]. These crystals were annealed after growth over extended periods of time in air at  \( 650^{\circ}C \)  to achieve homogeneous doping. Sample quality was examined by X-ray single-crystal diffraction using a Rigaku MiniFlex 600 system and Laue diffraction by Photonic Science system. The superconducting transition temperature  \( T_{c} \)  is determined to be  \( 78\pm2K \)  by the measurement of magnetic susceptibility using Quantum Design MPMS VSM equipment. In the following, the notation  \( T_{c} \)  always means the transition temperature under zero uniaxial pressure.

The samples were cut using a wire saw and polished into a thin bar with dimensions 1.2 mm along the a axis, 0.2 mm along the c axis, and  \( 75 \mu m \)  along the b axis. The polished samples were mounted to the Razorbill CS200T strain cell by Loctite Stycast 2850FT epoxy with CAT 24LV as the epoxy catalyst [Fig. 1 (b)]. We verified that the mounting process does not introduce additional strain by comparing the Raman spectra of unmounted and mounted samples.

## B. X-ray diffraction and thermal diffuse scattering

The X-ray diffraction experiments were performed at the European Synchrotron Radiation Facility (ESRF) ID15B beamline. The incident beam with photon energy of 30.0 keV was focused to a spot of  \( 4 \mu m \)  diameter, and the diffracted beam was detected with a DECTRIS EIGER2 X 9M CdTe flat panel detector. Each diffraction image was recorded with an angular range of  \( \pm35 \)  degrees and an angular step of 0.5 degrees. Low-flux data were taken for structure refinement, and high-flux data were taken to better observe the diffuse scattering. The measured XRD data are available from the ESRF Data Portal [22].

The software CrysAlisPro by Rigaku Oxford Diffraction was used for cell refinement and data reduction. The programs SHELXL  \( [23] \)  and JANA  \( [24] \)  were used to solve the crystal structure and perform relevant refinements  \( [25] \) . For each refinement, around 500 Bragg peaks were used. The data were corrected for Lorentz, polarization, extinction, and absorption effects. The automatic unit cell finding rendered a primitive tetragonal lattice when the strain was zero, and a primitive orthorhombic lattice when the sample was compressed. The data reduction results were inspected by the corresponding scale factor vs. frame plot. The strain values reported in this work are the real strain determined from the measured lattice parameters.

## C. Raman scattering

The Raman measurements were performed with a Horiba LabRAM HR Evolution spectrometer. A He-Ne laser (632.8 nm) with less than 1 mW power was focused to a spot of  \( 5 \mu m \)  diameter with a  \( x_{50} \)  magnification objective. The spectra were collected with  \( 1800 mm^{-1} \)  ( \( 0.6 cm^{-1} \)  spectral resolution) gratings and a liquid-nitrogen-cooled CCD detector. All the spectra were corrected for the instrumental spectral response and Bose factor. We used the aa polarization configuration in which the incident light polarization is along the crystallographic a direction, and the scattered one is also along
 

the a direction.

## D. First-Principles Lattice-Dynamics Calculations

In order to interpret the X-ray scattering intensity between the Bragg reflections, simulations of the diffuse scattering induced by the thermal population of phonons were performed in first-order approximation assuming the validity of both harmonic and adiabatic approximations. The details of the formalism can be found in Ref. [26].

The relevant dynamical matrices, necessary for the calculation of the thermal diffuse scattering, were calculated using the linear response of density-functional perturbation theory as implemented in the mixed-basis pseudopotential method  \( [27, 28] \) . In this approach valence states are expanded in a basis set consisting of a combination of plane waves and local functions, which allows an efficient description of more localized valence states. We used norm-conserving pseudopotentials including semicore states Hg-5p, Hg-5d, Ba-5s, Ba-5p, Cu-3s, Cu-3p, and O-2s. The kinetic energy cutoff for the plane waves was 24 Ry, augmented by local functions of s,p,d type at the Ba and Cu sites, of p and d type at the Hg sites, and of s and p type at the O sites. Brillouin zone integrations were performed with a  \( 8 \times 8 \times 4 \)  tetragonal k-point grid using a Gaussian smearing of 0.2 eV. We employed the PBESOL variant of the generalized gradient approximation for the exchange-correlation functional  \( [29] \) . Dynamical matrices were calculated on a  \( 4 \times 4 \times 2 \)  momentum grid for both unstrained and strained  \( HgBa_{2}CuO_{4} \)  using the experimental lattice constants  \( [25] \)  and relaxing the internal structural parameters until the forces on the atoms were smaller than  \( 2.6 \times 10^{-2} \)  eV/ \( \AA \) .

## III. RESULTS AND DISCUSSION

## A. Structural properties

In Fig. 2 (a) we illustrate how the applied compressive strain leads to a structural change by presenting the shift of three Bragg reflections. Because the structural change mainly happens along the a axis, the shift is mostly dependent on the H value of the Bragg reflections: the  \( 2\theta \)  value of both (611) and (-601) reflections increases with strain, whereas that of the (001) reflection exhibits no shift instead. Another feature is that the linewidth of the Bragg reflections broadens with strain, probably due to strain-induced disorder or inhomogeneity. The strain-induced structural change in the b and c directions is shown in Fig. 2 (b). Noticeably, the change of the lattice parameters along the b and c axes stays within 0.2% up to 1.2% strain, showing that these two lattice parameters respond weakly to the compression along the a axis. By doing a linear fit to the relative change of the lattice parameters, the Poisson ratios are estimated to

![](./images/1189542172815261698_3.jpg)

![](./images/1189542172815261698_4.jpg)

FIG. 2. The strain-induced structural change in  \( HgBa_{2}CuO_{4+\delta} \)  at  \( T_{c}=78K \) . (a) The shift of three representative Bragg reflections as a function of the a-axis compressive strain. The red, green, and blue colors represent 0.0%, 0.5%, and 1.1% strain, respectively. The dashed black lines track the shift of each Bragg reflection under strain. The intensity of the Bragg peaks is normalized with respect to the (00-1) Bragg peak at zero strain. (b) The magnitude of expansive strain in the  \( b\left(\epsilon_{bb}\right) \)  and  \( c\left(\epsilon_{cc}\right) \)  directions as a function of the magnitude of compressive strain in the a direction  \( \left(-\epsilon_{aa}\right) \) . The strain values are determined from lattice parameters. The dashed lines are linear fits.

be  \( \nu_{ba}=0.16 \)  and  \( \nu_{ca}=0.11 \) , which are reasonable values for ceramics [30]. For comparison, the Poisson ratios in YBCO are  \( \nu_{ba}\sim0.4 \)  and  \( \nu_{ca}\sim0.15 \)  [11].

The Cu-O distances are a crucial factor influencing the superconducting transition temperature  \( [31, 32] \) . In both a and b directions, the Cu-O bond length and the lattice parameter have the same percentage changes  \( [25] \) , because of the structural simplicity of the Cu-O plane. However, the out-of-plane Cu-O distance increases by 0.86% whereas the c-axis lattice parameter increases only by 0.12% under 1.1% strain  \( [25] \) . For comparison, in-plane uniaxial compression leads to almost no change of the apical oxygen position with respect to the  \( CuO_{2} \)  plane in YBCO  \( [11] \) . Our structural analysis, therefore, reveals that in-plane uniaxial compression brings the apical oxygen away from the  \( CuO_{2} \)  planes, a behavior typically associated with an increase in the superconducting tran-
 
![](./images/1189542172815261698_5.jpg)

FIG. 3. The experimental X-ray diffraction patterns measured at  \( T_{c}=78K \)  (shown in the right side of each panel, Exp.) compared with the calculated thermal diffuse scattering (shown in the left side of each panel, Calc.) for  \( HgBa_{2}CuO_{4+\delta} \) . The three rows from top to bottom show the results at zero strain, 1.1% strain, and their difference, respectively. The three panels to the left are in the  \( (H\ 0\ L) \)  plane, whereas the three panels to the right are in the  \( (H\ K\ 2) \)  plane. The strain-induced diffuse scattering, which has strip shape in panel (e) and dot shape in panel (f), is labeled by blue arrows. The bow-tie-shaped lobes along the L direction is labeled by a green arrow and enlarged at bottom-right corner in panel (a).

sition temperature [31, 32].

## B. Diffuse scattering

In Fig. 3 we present a comprehensive survey of the strain-dependence of the experimentally measured X-ray scattering intensity across selected reciprocal space planes at the superconducting transition temperature  \( T_{c} \) . This temperature was chosen based on prior studies of YBCO, which reported the most pronounced strain effects occurring in the vicinity of  \( T_{c} \)  [5, 11]. Our analysis primarily focuses on the diffuse scattering intensity between the main structural Bragg reflections, where weak signatures of short-range CDW modulations are expected.

The X-ray scattering intensity in the reciprocal  \( (H\ 0\ L) \)  and  \( (H\ K\ 2) \)  planes in the absence of applied strain is shown in Fig. 3 (a) and (b), respectively. The Bragg reflections are resolution-limited and intense compared to the diffuse background. The broad base of Bragg reflections, especially in Fig. 3 (a), appears elongated along specific high-symmetry directions. This broadening arises from the thermal diffuse scattering of acoustical phonons, and can be well captured by the calculated diffuse scattering.

Moreover, the experimental results show broad, bow-tie-shaped lobes existing along L direction from some Bragg reflections with large L values [Fig. 3 (a), identified by the green arrow and enlarged at bottom-right corner]. These features have previously been reported and associated with nanoscale correlations of atomic displacements perpendicular to the  \( CuO_{2} \)  planes [33, 34], but cannot be easily reproduced by our calculations.

The experimentally accessible reciprocal space in the  \( (HK2) \)  plane [Fig. 3 (b)] is more limited due to the scattering geometry. Because of the structure factors, reflections at  \( H+K=2n \)  are much weaker than those at  \( H+K-2n+1 \) . The reflection at  \( (102) \)  appears sharper than other reflections with larger  \( H+K=2n+1 \)  values [for example,  \( (412) \) ], consistent with the calculation results.

We note that the sharp diffuse lines observed in optimally doped  \( Hg_{1201} \)  [35] and associated with the formation of dopant O-chains are not seen in our diffraction patterns, as expected for underdoped materials. Moreover, we do not observe here the weak signature of 2D CDW order that has been reported at in-plane wavevector  \( H = 0.27 \, r.l.u. \)  in a series of resonant scattering experiments [18, 19, 36, 37].

Applying compressive 1.1% strain along the crystallographic a direction leads to additional diffuse scattering intensity between the reflections. In the  \( (H\ 0\ L) \)  plane, this strain-induced diffuse scattering forms strips at half-H values along the L direction [Fig. 3 (c)], showing that the corresponding modulation is in-plane confined. In the  \( (H\ K\ 2) \)  plane, the same diffuse-scattering features manifest themselves as broad peaks at the two sides of Bragg peaks along the H direction [Fig. 3 (d)]. To better emphasize the strain-induced contribution to the diffuse scattering, we subtract the zero-strain diffraction patterns [Fig. 3 (a) and (b)] from the 1.1%-strain diffraction patterns [Fig. 3 (c) and (d)]. Fig. 3 (e) and (f) unambiguously indicate that the strain-induced diffuse scattering has a rod-like structure along the L direction and is centered in-plane around wavevectors with  \( H = 0.5\ r.l.u \) . Most interestingly, this experimentally observed strain-induced change cannot be simply explained by the change of the calculated phonon dispersion. As seen in Fig. 3 (e)
 

and (f), the impact of strain on the calculated thermal diffuse scattering is strictly limited to regions close to the Bragg reflections and relates to the directional stiffening of the lattice under uniaxial compression.

Next, to gain more insights regarding the nature of the strain-induced signal, we examine in Fig. 4 its strain and temperature dependence. To achieve this, cuts are made across these features along the reciprocal H direction. These cuts reveal that the signal already appears with minimal compression of 0.05% and rapidly saturates for in-plane strain as low as 0.2% [Fig. 4 (a)]. Furthermore, at 1.1% compressive strain, there is no significant impact of temperature on these features. Moreover, we do not observe any particular loss of intensity in the superconducting state (at 30 K) or the normal state (at 101 K) [Fig. 4 (b)].

Finally, we analyse quantitatively the lineshape of the strain-induced features by fitting them to a Lorentzian profile in the H direction:  \( I(q) \propto 1/[(q - q_{0})^{2} + \kappa^{2}] \) , in which  \( q_{0} \)  is the center position and  \( \kappa \)  is the decay factor. The Lorentzian lineshape corresponds in real space to a short-range order whose correlation function follows exponential decay:  \( G(x) \propto e^{-x/\xi} \) , in which the correlation length  \( \xi = 1/\kappa \) . By fitting the strain-induced diffuse scattering, we find the correlation length to be around 4 lattice constants. The spectral linewidth and, in turn, the correlation length show little temperature or strain dependence. The  \( q_{0} \)  values for the two strain-induced features shown in Fig. 4 (b) are very close to half integer values, 3.53(4) and 4.48(2) r.l.u., respectively, consistent with a nearly-commensurate nature.

## C. Raman scattering

To determine whether the strain-induced signal may be related to strain-induced changes in short-range oxygen dopant structures, we performed a Raman scattering study. We show in Fig. 5 the Raman spectra measured in the aa polarization geometry at 30 K. The compound  \( HgBa_{2}CuO_{4+\delta} \)  has four Raman-active phonon modes:  \( 2A_{1g} \)  and  \( 2E_{g} \)  which have previously been investigated [38, 39]. According to Raman selection rules [40], Raman signal with  \( A_{1g} \)  and  \( B_{1g} \) , symmetry is probed in the aa polarization geometry. In Fig. 5, the modes at 161 and  \( 592 cm^{-1} \)  correspond to the  \( A_{1g} \)  phonon derived from Ba and O atoms, respectively [38]; the other relatively weak modes have been assigned to defects arising from oxygen dopants [37–39]. Fig. 5 shows that a-axis compressive strain has only moderate impact on the zone center phonons of Hg1201. When the strain is increased to 1.1%, the frequency shift for the  \( 161 cm^{-1} \)  and  \( 592 cm^{-1} \)   \( A_{1g} \) -symmetry phonons is around  \( 1 cm^{-1} \)  and  \( 4 cm^{-1} \) , respectively. The corresponding Grüneisen parameters,  \( \gamma_{i} = -(\Delta\omega_{i}/\omega_{i})/(\Delta V/V) \) , for these two phonons at 30 K are 0.8 (the  \( 161 cm^{-1} \)  mode) and 0.6 (the  \( 592 cm^{-1} \)  mode), respectively. For a comparison, the Grüneisen parameter for the  \( 592 cm^{-1} \)   \( A_{1g} \) -symmetry

![](./images/1189542172815261698_6.jpg)

![](./images/1189542172815261698_7.jpg)

FIG. 4. The line cuts along H direction across the (412) Bragg peak. (a) The strain dependence of the diffuse scattering at  \( T_{c}=78K \) . (b) The temperature dependence of the diffuse scattering under 1.1% strain. The dashed red curve shows the fit to the 78K spectrum. The (412) Bragg peak and the diffuse scattering associated with it are labeled by an red rectangle in the diffraction pattern shown at bottom-left corner.

phonon derived from measurements under hydrostatic pressure is 0.52 [41] or 0.61 [42, 43] (We note that the Grüneisen parameters obtained from uniaxial compression and hydrostatic pressure experiments do not need to be the same.) Moreover, we do not observe any significant strain-induced change in the defect modes, nor do we detect the appearance of any new features, confirming the absence of noticeable strain-induced structural distortions.

## D. Discussion

We have demonstrated that the application of uniaxial pressure along the crystallographic a-axis of underdoped  \( HgBa_{2}CuO_{4+\delta} \)  induces a previously unreported modulation characterized by several intriguing features.

First, the strain-induced modulation manifests as a pronounced rod-like structure in the  \( (H\ 0\ L) \)  plane, clearly indicative of the absence of correlations along the c-axis and reinforcing the two-dimensional nature
 
![](./images/1189542172815261698_8.jpg)

FIG. 5. Strain dependence of Raman spectra measured in the aa polarization geometry at 30 K. The inset shows the shift of the  \( A_{1g} \) -symmetry phonon at  \( 592\,cm^{-1} \) .

of this phenomenon. Within the  \( CuO_{2} \)  plane, satellite peaks exclusively appear along the H direction, suggesting an underlying unidirectional structure. Furthermore, the strain-induced signal saturates already at relatively modest strain levels (0.2%) and, notably, is only detected along the direction parallel to the applied strain.

Second, the observed modulation emerges at a nearly-commensurate wave vector corresponding to a doubling of the unit cell. This behavior sharply contrasts with previous observations in underdoped cuprates, where charge density waves typically manifest at incommensurate wave vectors associated with periodicities spanning approximately 3 to 4 unit cells  \( [44] \) . Remarkably, Hg1201 is thus far the only known cuprate exhibiting commensurate low-energy magnetic fluctuations, as previously reported in Refs.  \( [45–48] \) . Moreover, the observed modulation displays an in-plane correlation length similar to these magnetic fluctuations, suggesting a potentially unique and intimate interplay between charge and spin correlations specific to this compound.

Third, the absence of a significant temperature dependence of the strain-induced signal indicates insensitivity to the onset of superconductivity, consistent with earlier reports of charge ordering phenomena in this family of materials  \( [18, 19, 36] \) . However, further studies will be necessary to clarify this relationship, along with investigations into the effect of uniaxial pressure on the superconducting properties of Hg1201, which remain largely unexplored.

We conclude this discussion by emphasizing that although this particular type of nearly-commensurate charge correlation has yet to be observed in other cuprate families, it bears a striking resemblance to degenerate site-charge density wave stripes characterized by wave vectors  \( (\pi,0) \)  and  \( (0,\pi) \) . Interestingly, these stripe configurations emerge naturally within the mean-field phase diagram derived from the  \( \pi \) -flux state employing fermionic spinon approaches to the resonating valence bond spin-liquid model on the square lattice [49–51]. This analogy is particularly compelling given that Hg1201 is among the very few cuprates possessing a simple tetragonal crystal structure and minimal doping-induced disorder. These unique attributes establish Hg1201 as an ideal candidate for unraveling the intrinsic electronic properties inherent to doped  \( CuO_{2} \)  planes.

## IV. CONCLUSION

We use synchrotron X-ray diffraction to study the structural change and diffuse scattering induced by a-axis compressive strain in  \( HgBa_{2}CuO_{4+\delta} \)  with  \( T_{c}=78K \) . The lattice parameters in the b and c directions respond weakly to the compression in the a direction, which leads to relatively small Poisson ratios of  \( \nu_{ba}=0.16 \)  and  \( \nu_{ca}=0.11 \) . Regarding the Cu-O distances, although the c-axis lattice parameter increases by only 0.1% at 1.1% a-axis strain, the Cu-O distance along the c axis increases by 0.9%. By comparing the experimental diffraction patterns with the simulation of thermal diffuse scattering, we identify strain-induced diffuse scattering with a wavevector near  \( (0.5\ 00) \)  and a correlation length of around 4 unit cells along the a direction. The diffuse-scattering features saturate at 0.2% strain and exhibit little change on cooling below  \( T_{c} \) . We suggest that such diffuse scattering corresponds to a new 2D charge correlation which does not compete with the superconductivity. The nearly-commensurate wavevector of this new charge modulation bears a resemblance to the magnetic fluctuations in this system, and such order was found to emerge in the mean-field phase diagram derived from the  \( \pi \) -flux state employing fermionic spinon approaches to the resonating valence bond spin-liquid model on the square lattice. Our findings provide new insights into the coupling between strain and charge order in structurally simple cuprates and open new directions for engineering electronic phases in high- \( T_{c} \)  superconductors via lattice perturbations.

## ACKNOWLEDGMENTS

We acknowledge Steve Kivelson and Subir Sachdev for fruitful discussion. The work at Karlsruhe Institute for Technology was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - TRR 288 - 422213477 (project B03), and Projektnummer 449386310. The work at Peking University was supported by the National Natural Science Foundation of China (Grant No. 12061131004) and by the National Basic Research Program of China (Grant No. 2021YFA1401901). M. F. acknowledges funding from the Alexander von Humboldt foundation, and the YIG preparation program of the Karlsruhe Institute of Technology. R.H. acknowledges support by the state of Baden-Württemberg through bwHPC.
 

[1] F. Hardy, N. J. Hillier, C. Meingast, D. Colson, Y. Li, N. Barišić, G. Yu, X. Zhao, M. Greven, and J. S. Schilling, Enhancement of the Critical Temperature of  \( HgBa_{2}CuO_{4+\delta} \)  by Applying Uniaxial and Hydrostatic Pressure: Implications for a Universal Trend in Cuprate Superconductors, Phys. Rev. Lett. 105, 167002 (2010).

[2] C. W. Hicks, D. O. Brodsky, E. A. Yelland, A. S. Gibbs, J. A. N. Bruin, M. E. Barber, S. D. Edkins, K. Nishimura, S. Yonezawa, Y. Maeno, and A. P. Mackenzie, Strong Increase of  \( T_{c} \)  of  \( Sr_{2}RuO_{4} \)  Under Both Tensile and Compressive Strain, Science 344, 283 (2014).

[3] A. Steppke, L. Zhao, M. E. Barber, T. Scaffidi, F. Jerzembeck, H. Rosner, A. S. Gibbs, Y. Maeno, S. H. Simon, A. P. Mackenzie, and C. W. Hicks, Strong peak in  \( T_{c} \)  of  \( Sr_{2}RuO_{4} \)  under uniaxial pressure, Science 355, 148 (2017).

[4] M. Mito, K. Ogata, H. Goto, K. Tsuruta, K. Nakamura, H. Deguchi, T. Horide, K. Matsumoto, T. Tajiri, H. Hara, T. Ozaki, H. Takeya, and Y. Takano, Uniaxial strain effects on the superconducting transition in re-doped  \( hg-1223 \)  cuprate superconductors, Phys. Rev. B 95, 064503 (2017).

[5] H.-H. Kim, S. M. Souliou, M. E. Barber, E. Lefrançois, M. Minola, M. Tortora, R. Heid, N. Nandi, R. A. Borzi, G. Garbarino, A. Bosak, J. Porras, T. Loew, M. König, P. J. W. Moll, A. P. Mackenzie, B. Keimer, C. W. Hicks, and M. L. Tacon, Uniaxial pressure control of competing orders in a high-temperature superconductor, Science 362, 1040 (2018).

[6] H.-H. Kim, E. Lefrançois, K. Kummer, R. Fumagalli, N. B. Brookes, D. Betto, S. Nakata, M. Tortora, J. Porras, T. Loew, M. E. Barber, L. Braicovich, A. P. Mackenzie, C. W. Hicks, B. Keimer, M. Minola, and M. Le Tacon, Charge Density Waves in  \( YBa_{2}Cu_{3}O_{6.67} \)  Probed by Resonant X-Ray Scattering under Uniaxial Compression, Phys. Rev. Lett. 126, 037002 (2021).

[7] M. E. Barber, H.-h. Kim, T. Loew, M. Le Tacon, M. Minola, M. Konczykowski, B. Keimer, A. P. Mackenzie, and C. W. Hicks, Dependence of  \( T_{c} \)  of  \( YBa_{2}Cu_{3}O_{6.67} \)  on in-plane uniaxial stress, Phys. Rev. B 106, 184516 (2022).

[8] T. J. Boyle, M. Walker, A. Ruiz, E. Schierle, Z. Zhao, F. Boschini, R. Sutarto, T. D. Boyko, W. Moore, N. Tanuma, F. He, E. Weschke, A. Gozar, W. Peng, A. C. Komarek, A. Damascelli, C. Schüßler-Langeheine, A. Frano, E. H. da Silva Neto, and S. Blanco-Canosa, Large response of charge stripes to uniaxial stress in  \( La_{1.475}Nd_{0.4}Sr_{0.125}CuO_{4} \) , Phys. Rev. Res. 3, L022004 (2021).

[9] A. Najev, S. Hameed, D. Gautreau, Z. Wang, J. Joe, M. Pożek, T. Birol, R. M. Fernandes, M. Greven, and D. Pelc, Uniaxial strain control of bulk ferromagnetism in rare-earth titanates, Phys. Rev. Lett. 128, 167201 (2022).

[10] H.-H. Kim, K. Ueda, S. Nakata, P. Wochner, A. Mackenzie, C. Hicks, G. Khaliullin, H. Liu, B. Keimer, and M. Minola, Giant stress response of terahertz magnons in a spin-orbit mossbauer, Nature Communications 13, 6674 (2022).

[11] I. Vinograd, S. M. Souliou, A. A. Haghighirad, T. Lacmann, Y. Caplan, M. Frachet, M. Merz, G. Garbarino, Y. Liu, S. Nakata, K. Ishida, H. M. L. Noad, M. Minola, B. Keimer, D. Orgad, C. W. Hicks, and M. Le Tacon,

Using strain to uncover the interplay between two- and three-dimensional charge density waves in high-temperature superconducting  \( YBa_{2}Cu_{3}O_{y} \) , Nature Communications 15, 3277 (2024).

[12] C. Lin, A. Consiglio, O. K. Forslund, J. Küspert, M. M. Denner, H. Lei, A. Louat, M. D. Watson, T. K. Kim, C. Cacho, D. Carbone, M. Leandersson, C. Polley, T. Balasubramanian, D. D. Sante, R. Thomale, Z. Guguchia, G. Sangiovanni, T. Neupert, and J. Chang, Uniaxial strain tuning of charge modulation and singularity in a kagome superconductor, Nature Communications 15, 10466 (2024).

[13] J. Küspert, I. Bialo, R. Frison, A. Morawietz, L. Martinelli, J. Choi, D. Bucher, O. Ivashko, M. v Zimmermann, N. B. Christensen, D. G. Mazzone, G. Simutis, A. A. Turrini, L. Thomarat, D. W. Tam, M. Janoschek, T. Kurosawa, N. Momono, M. Oda, Q. Wang, and J. Chang, Engineering phase competition between stripe order and superconductivity in  \( La_{1.88}Sr_{0.12}CuO_{4} \) , Communications Physics 7, 225 (2024).

[14] T. Wu, H. Mayaffre, S. Krämer, M. Horvatić, C. Berthier, W. N. Hardy, R. Liang, D. A. Bonn, and M.-H. Julien, Magnetic-field-induced charge-stripe order in the high-temperature superconductor  \( YBa_{2}Cu_{3}O_{y} \) , Nature 477, 191 (2011).

[15] S. Gerber, H. Jang, H. Nojiri, S. Matsuzawa, H. Yasumura, D. A. Bonn, R. Liang, W. N. Hardy, Z. Islam, A. Mehta, S. Song, M. Sikorski, D. Stefanescu, Y. Feng, S. A. Kivelson, T. P. Devereaux, Z.-X. Shen, C.-C. Kao, W.-S. Lee, D. Zhu, and J.-S. Lee, Three-dimensional charge density wave order in  \( YBa_{2}Cu_{3}O_{6.67} \)  at high magnetic fields, Science 350, 949 (2015).

[16] Y. Caplan and D. Orgad, Dimensional crossover of charge-density wave correlations in the cuprates, Phys. Rev. Lett. 119, 107002 (2017).

[17] N. Barišić, Y. Li, X. Zhao, Y.-C. Cho, G. Chabot-Couture, G. Yu, and M. Greven, Demonstrating the model nature of the high-temperature superconductor  \( HgBa_{2}CuO_{4+\delta} \) , Phys. Rev. B 78, 054518 (2008).

[18] W. Tabis, B. Yu, I. Bialo, M. Bluschke, T. Kolodziej, A. Kozlowski, E. Blackburn, K. Sen, E. M. Forgan, M. v. Zimmermann, Y. Tang, E. Weschke, B. Vignolle, M. Hepping, H. Gretarsson, R. Sutarto, F. He, M. Le Tacon, N. Barišić, G. Yu, and M. Greven, Synchrotron x-ray scattering study of charge-density-wave order in  \( HgBa_{2}CuO_{4+\delta} \) , Phys. Rev. B 96, 134510 (2017).

[19] B. Yu, W. Tabis, I. Bialo, F. Yakhou, N. B. Brookes, Z. Anderson, Y. Tang, G. Yu, and M. Greven, Unusual Dynamic Charge Correlations in Simple-Tetragonal  \( HgBa_{2}CuO_{4+\delta} \) , Physical Review X 10, 021059 (2020).

[20] H. Murayama, Y. Sato, R. Kurihara, S. Kasahara, Y. Mizukami, Y. Kasahara, H. Uchiyama, A. Yamamoto, E. G. Moon, J. Cai, J. Freyermuth, M. Greven, T. Shibauchi, and Y. Matsuda, Diagonal nematicity in the pseudogap phase of  \( HgBa_{2}CuO_{4+\delta} \) , Nature Communications 10, 3282 (2019).

[21] X. Zhao, G. Yu, Y.-C. Cho, G. Chabot-Couture, N. Barišić, P. Bourges, N. Kaneko, Y. Li, L. Lu, E. M. Motoyama, O. P. Vajk, and M. Greven, Crystal Growth and Characterization of the Model High-Temperature Superconductor  \( HgBa_{2}CuO_{4+\delta} \) , Advanced Materials 18, 3243
 

(2006).

[22] M. Ye, T. Lacmann, M. Frachet, I. Vinograd, G. Garbarino, and A.-A. Haghighirad, Stress-induced structural changes and diffuse scattering in high-temperature superconductor hbco (version 1) [dataset], 10.15151/ESRF-DC-1511962937 (2024), European Synchrotron Radiation Facility.

[23] G. M. Sheldrick, Crystal structure refinement with SHELXL, Acta Cryst. C 71, 3 (2015).

[24] V. Petříček, M. Dušek, and L. Palatinus, Crystallographic computing system jana2006: General features, Z. Kristallogr. 229, 345 (2014).

[25] The Supplemental Material contains representative refinements of the synchrotron x-ray diffraction data.

[26] B. Wehinger, A. Bosak, and P. T. Jochym, Soft phonon modes in rutile  \( TiO_{2} \) , Phys. Rev. B 93, 014303 (2016).

[27] B. Meyer, C. Elsässer, F. Lechermann, and M. Fähne, Fortran90 program for mixed-basis pseudopotential calculations for crystals, Max-Planck-Institut für Metallforschung, Stuttgart (unpublished).

[28] R. Heid and K. P. Bohnen, Linear response in a density-functional mixed-basis approach, Phys. Rev. B 60, R3709 (1999).

[29] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Restoring the density-gradient expansion for exchange in solids and surfaces, Phys. Rev. Lett. 100, 136406 (2008).

[30] G. N. Greaves, A. L. Greer, R. S. Lakes, and T. Rouxel, Poisson's ratio and modern materials, Nature Materials 10, 823 (2011).

[31] E. Pavarini, I. Dasgupta, T. Saha-Dasgupta, O. Jepsen, and O. K. Andersen, Band-Structure Trend in Hole-Doped Cuprates and Correlation with  \( T_{c}^{max} \) , Physical Review Letters 87, 047003 (2001).

[32] Y. Y. Peng, G. Dellea, M. Minola, M. Conni, A. Amorese, D. Di Castro, G. M. De Luca, K. Kummer, M. Salluzzo, X. Sun, X. J. Zhou, G. Balestrino, M. Le Tacon, B. Keimer, L. Braicovich, N. B. Brookes, and G. Ghiringhelli, Influence of apical oxygen on the extent of in-plane exchange interaction in cuprate superconductors, Nature Physics 13, 1201 (2017).

[33] Z. W. Anderson, M. Spaie, N. Biniskos, L. Thompson, B. Yu, J. Zwettler, Y. Liu, F. Ye, G. E. Granroth, M. Krogstad, R. Osborn, D. Pelc, and M. Greven, Nanoscale structural correlations in a model cuprate superconductor, Phys. Rev. B 110, 214519 (2024).

[34] R. Osborn, D. Pelc, M. J. Krogstad, S. Rosenkranz, and M. Greven, Diffuse scattering from correlated electron systems, Science Advances 11, eadt7770 (2025).

[35] M. Izquierdo, S. Megtert, D. Colson, V. Honkimäki, A. Forget, H. Raffy, and R. Comès, One dimensional ordering of doping oxygen in  \( HgBa_{2}CuO_{4+\delta} \)  superconductors evidenced by X-ray diffuse scattering, Journal of Physics and Chemistry of Solids 72, 545 (2011).

[36] W. Tabis, Y. Li, M. Le Tacon, L. Braicovich, A. Kreyssig, M. Minola, G. Dellea, E. Weschke, M. J. Veit, M. Ramazanoglu, A. I. Goldman, T. Schmitt, G. Ghiringhelli, N. Barišić, M. K. Chan, C. J. Dorow, G. Yu, X. Zhao, B. Keimer, and M. Greven, Charge order and its connection with fermi-liquid charge transport in a pristine high-tc cuprate, Nature Communications 5, 5875 (2014).

[37] L. Wang, B. Yu, R. Jing, X. Luo, J. Zeng, J. Li, I. Bialo, M. Bluschke, Y. Tang, J. Freyermuth, G. Yu, R. Sutarto, F. He, E. Weschke, W. Tabis, M. Greven, and Y. Li,

Doping-dependent phonon anomaly and charge-order phenomena in the  \( HgBa_{2}CuO_{4+\delta} \)  and  \( HgBa_{2}CaCu_{2}O_{6+\delta} \)  superconductors, Phys. Rev. B 101, 220509 (2020).

[38] X. Zhou, M. Cardona, C. Chu, Q. Lin, S. Loureiro, and M. Marezio, Raman study of  \( HgBa_{2}Ca_{n-1}Cu_{n}O_{2n+2+\delta} \)  (n=1,2,3,4 and 5) superconductors, Physica C: Superconductivity 270, 193 (1996).

[39] X. Zhou, M. Cardona, C. W. Chu, Q. M. Lin, S. M. Loureiro, and M. Marezio, Raman spectra of hg-based superconductors: Effect of oxygen defects, Phys. Rev. B 54, 6137 (1996).

[40] W. Hayes and R. Loudon, Scattering of Light by Crystals (John Wiley and Sons, New York, 1978).

[41] I.-S. Yang, H.-S. Shin, H.-G. Lee, S.-J. Jeon, H.-S. Ahn, J. Yu, S. Lee, S.-I. Lee, and N. H. Hur, Micro-raman study of the role of pressure in mercury-based superconductors, Phys. Rev. B 51, 644 (1995).

[42] N. Auvray, B. Loret, S. Chibani, R. Grasset, Y. Guar-nelli, P. Parisiades, A. Forget, D. Colson, M. Cazayous, Y. Gallais, and A. Sacuto, Exploration of hg-based cuprate superconductors by raman spectroscopy under hydrostatic pressure, Phys. Rev. B 103, 195130 (2021).

[43] S. Wang, J. Zhang, J. Yan, X.-J. Chen, V. Struzhkin, W. Tabis, N. Barišić, M. K. Chan, C. Dorow, X. Zhao, M. Greven, W. L. Mao, and T. Geballe, Strain derivatives of  \( T_{c} \)  in  \( HgBa_{2}CuO_{4+\delta} \) : The  \( CuO_{2} \)  plane alone is not enough, Phys. Rev. B 89, 024515 (2014).

[44] R. Comin and A. Damascelli, Resonant x-ray scattering studies of charge order in cuprates, Annual Review of Condensed Matter Physics 7, 369 (2016).

[45] Y. Li, V. Balédent, G. Yu, N. Barišić, K. Hradil, R. A. Mole, Y. Sidis, P. Steffens, X. Zhao, P. Bourges, and M. Greven, Hidden magnetic excitation in the pseudogap phase of a high-tc superconductor, Nature 468, 283 (2010).

[46] G. Yu, Y. Li, E. M. Motoyama, X. Zhao, N. Barišić, Y. Cho, P. Bourges, K. Hradil, R. A. Mole, and M. Greven, Magnetic resonance in the model high-temperature superconductor  \( HgBa_{2}CuO_{4+\delta} \) , Phys. Rev. B 81, 064518 (2010).

[47] M. K. Chan, Y. Tang, C. J. Dorow, J. Jeong, L. Mangin-Thro, M. J. Veit, Y. Ge, D. L. Abernathy, Y. Sidis, P. Bourges, and M. Greven, Hourglass Dispersion and Resonance of Magnetic Excitations in the Superconducting State of the Single-Layer Cuprate  \( HgBa_{2}CuO_{4+\delta} \)  Near Optimal Doping, Phys. Rev. Lett. 117, 277002 (2016).

[48] M. K. Chan, C. J. Dorow, L. Mangin-Thro, Y. Tang, Y. Ge, M. J. Veit, G. Yu, X. Zhao, A. D. Christianson, J. T. Park, Y. Sidis, P. Steffens, D. L. Abernathy, P. Bourges, and M. Greven, Commensurate antiferromagnetic excitations as a signature of the pseudogap in the tetragonal high-Tc cuprate  \( HgBa_{2}CuO_{4+\delta} \) , Nature Communications 7, 10819 (2016).

[49] S. Sachdev, Colloquium: Order and quantum phase transitions in the cuprate superconductors, Rev. Mod. Phys. 75, 913 (2003).

[50] M. Christos, Z.-X. Luo, H. Shackleton, Y.-H. Zhang, M. S. Scheurer, and S. Sachdev, A model of d-wave superconductivity, antiferromagnetism, and charge order on the square lattice, Proceedings of the National Academy of Sciences 120, e2302701120 (2023).

[51] S. Sachdev, The foot, the fan, and the cuprate phase diagram: Fermi-volume-changing quantum phase transi-
 

tions, Physica C: Superconductivity and its Applications 633, 1354707 (2025).
 
