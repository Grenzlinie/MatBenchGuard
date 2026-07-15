This is an open access article published under a Creative Commons Attribution (CC-BY)
License, which permits unrestricted use, distribution and reproduction in any medium,
provided the author and source are cited.

![](./images/812809320390459393_1.jpg)

# A Picture of Disorder in Hydrous Wadsleyite—Under the Combined Microscope of Solid-State NMR Spectroscopy and *Ab Initio* Random Structure Searching

David McKay, $^{\dagger,\nabla}$ Robert F. Moran, $^{\dagger,\nabla}$ Daniel M. Dawson, $^{\dagger}$ John M. Griffin, $^{\ddagger}$ Simone Sturniolo, $^{\S}$ Chris J. Pickard, $^{\parallel ,\perp}$ Andrew J. Berry, $^{\#}$ and Sharon E. Ashbrook $^{*, \dagger}$

$^{\dagger}$School of Chemistry, EaStCHEM and Centre of Magnetic Resonance, University of St Andrews, St Andrews, KY16 9ST, U.K.
$^{\ddagger}$Department of Chemistry and Materials Science Institute, Lancaster University, Lancaster, LA1 4YB, U.K.
$^{\S}$Science and Technology Facilities Council, Rutherford Appleton Laboratory, Harwell Science and Innovation Campus, Didcot, Oxfordshire OX11 0QX, U.K.
$^{\parallel }$Department of Materials Science and Metallurgy, University of Cambridge, 27 Charles Babbage Road, Cambridge, CB3 0FS, U.K.
$^{\perp}$Advanced Institute for Materials Research, Tohoku University 2-1-1 Katahira, Aoba, Sendai 980-8577, Japan
$^{\#}$Research School of Earth Sciences, Australian National University, Canberra, ACT 2601, Australia

### Supporting Information

**ABSTRACT:** The Earth's transition zone, at depths of 410–660 km, while being composed of nominally anhydrous magnesium silicate minerals, may be subject to significant hydration. Little is known about the mechanism of hydration, despite the vital role this plays in the physical and chemical properties of the mantle, leading to a need for improved structural characterization. Here we present an *ab initio* random structure searching (AIRSS) investigation of semihydrous (1.65 wt % $\text{H}_2\text{O}$) and fully hydrous (3.3 wt % $\text{H}_2\text{O}$) wadsleyite. Following the AIRSS process, $k$-means clustering was used to select sets of structures with duplicates removed, which were then subjected to further geometry optimization with tighter constraints prior to NMR calculations. Semihydrous models identify a ground-state structure (Mg3 vacancies, O1–H hydroxyls) that aligns with a number of previous experimental observations. However, predicted NMR parameters fail to reproduce low-intensity signals observed in solid-state NMR spectra. In contrast, the fully hydrous models produced by AIRSS, which enable both isolated and clustered defects, are able to explain observed NMR signals via just four low-enthalpy structures: (i) a ground state, with isolated Mg3 vacancies and O1–H hydroxyls; (ii/iii) edge-sharing Mg3 vacancies with O1–H and O3–H species; and (iv) edge-sharing Mg1 and Mg3 vacancies with O1–H, O3–H, and O4–H hydroxyls. Thus, the combination of advanced structure searching approaches and solid-state NMR spectroscopy is able to provide new and detailed insight into the structure of this important mantle mineral.

![](./images/812809320390459393_2.jpg)

## INTRODUCTION

The high-pressure silicate mineral wadsleyite, $\beta$-(Mg,Fe)$_2$SiO$_4$, is believed to be the predominant component of the Earth between depths of 410 and 520 km. At lower pressures, olivine, $\alpha$-(Mg,Fe)$_2$SiO$_4$, is stable, while, below 520 km, ringwoodite, $\gamma$-(Mg,Fe)$_2$SiO$_4$, occurs. At pressures corresponding to depths below 660 km, $\gamma$-(Mg,Fe)$_2$SiO$_4$ breaks down to (Mg,Fe)SiO$_3$, perovskite, and (Mg,Fe)O (Figure 1). Wadsleyite (shown in Figure 2a) can accommodate up to 3.3 wt % $\text{H}_2\text{O}$, $^{1-5}$ suggesting it could be acting as a vast "water" reservoir deep within the Earth, stimulating great interest from both chemists and geologists, leading to the concept of "hidden oceans" within the Earth. $^{6}$ Net hydration of wadsleyite is generally thought to be achieved via incorporation of hydrogen as $\text{H}^+$, charge balanced by loss of 6-coordinate $\text{Mg}^{2+}$ cations, where the maximum hydration level (3.3 wt % $\text{H}_2\text{O}$) corresponds to the exchange of four $\text{H}^+$ for two $\text{Mg}^{2+}$ per unit cell. However, given that wadsleyite has three crystallographically distinct $\text{Mg}^{2+}$ cations, there is some ambiguity over the specific site(s) at which vacancies are created. Additionally, since protons cannot stabilize an octahedral site, their preferred location in wadsleyite and the orientation of the hydroxyl bonds formed are challenging to determine by many experimental methods. Thus, the uncertainty regarding the positions of both $\text{H}^+$ ions and the $\text{Mg}^{2+}$ vacancies in hydrous wadsleyite introduces the potential for significant structural disorder, increasing the challenge associated with characterizing this system. Herein,

Received: October 25, 2018
Published: January 24, 2019

![](./images/812809320390459393_3.jpg)

© 2019 American Chemical Society
3024
DOI: 10.1021/jacs.8b11519
J. Am. Chem. Soc. 2019, 141, 3024−3036

![](./images/812809320390459393_4.jpg)

Figure 1. Schematic of the Earth's mantle showing its layered structure and the principal mineralogical components.

![](./images/812809320390459393_5.jpg)

Figure 2. (a) Crystal structure of anhydrous wadsleyite with the three Mg sites and four O sites labeled. (b) Detailed views of the Mg sites, the single Si site that forms a pyrosilicate unit, and their associated O sites.

we show how NMR crystallography,⁷⁻⁹ through a combination of *ab initio* structure searching, k-means clustering, first-principles calculations, and solid-state NMR spectroscopy, provides unique insight into the detailed structure of this complex and important mineral.

A number of studies, involving a range of experimental and/or theoretical techniques, have previously attempted to elucidate the structure of hydrous wadsleyite, often focusing on the Fe-free, Mg end-member, $\beta$-Mg₂SiO₄. Owing to its underbonded character (as a result of having just five Mg²⁺ nearest neighbors), the O1 site (see Figure 2) has been identified as a likely site of protonation by several theoretical investigations.²,³,¹⁰⁻¹⁴ In a study using simple ionic constraints to generate a theoretical model for hydrous $\beta$-Mg₂SiO₄ (3.3 wt % H₂O), Smyth determined that the most stable structure consists of protonated O1 sites, with the hydroxyl bonds orientated parallel to the c-axis, charge balanced locally by the removal of Mg2 cations.³ Using the single-crystal X-ray diffraction (XRD) data of Horiuchi and Sawamoto,¹⁵ Downs derived the electrostatic potential for $\beta$-Mg₂SiO₄, finding a broad minimum in the potential close to O1,¹⁶ indicating this was a promising protonation site, in agreement with the model proposed by Smyth.²,³ However, in contrast to previous literature, this study revealed even lower electrostatic-potential minima above and below the bonding plane of the O2 site, predicting protonation at both O1 and O2 sites. Similar calculations performed by Ross et al. found that potential protonation sites exist for all four oxygens, although protonation at O3 or O4 could only occur if hydrogen incorporation was accompanied by vacancies on neighboring Mg sites.¹⁷

More recently, Tsuchiya and Tsuchiya used first-principles density functional theory (DFT) calculations to investigate the possible structures of hydrous wadsleyite, determining defect structures for Mg₁.₈₇₅SiH₀.₂₅O₄ (1.65 wt % H₂O) and Mg₁.₇₅SiH₀.₅O₄ (3.3 wt % H₂O).¹⁴ In contrast to previous work, their calculations found that the lowest energy geometry optimized structures have monoclinic symmetry, Mg3 site vacancies, and O1 hydroxyls, with the OH dipoles aligned along the edges of the oxygen octahedron surrounding the formally occupied Mg3 site.²,³,¹⁶ This conclusion is, however, in agreement with several XRD investigations of hydrous wadsleyite.¹⁸⁻²¹ In an XRD study on the crystal chemistry of $\beta$-Mg₂SiO₄ at 3.3 wt % H₂O, Kudoh et al. suggested the incorporation of water occurs around an Mg3 site, with Raman and FTIR spectroscopy confirming the presence of hydroxyls and valence sum calculations implying O1 protonation.¹⁸ However, in a later publication, Kudoh and Inoue determined occupancies of less than one in the Mg2 position, which become more pronounced at higher levels of hydration.¹⁹ Fractional occupancies in Mg₁.₇₅SiH₀.₅O₄ (3.3 wt % H₂O) were found to be 100, 92, and 76% for Mg1, Mg2, and Mg3, respectively. In addition, Kudoh and Inoue reported Si vacancies, where Si was found to migrate to an interstitial "Si2" site under certain conditions. Holl et al. also saw a strong preference for protonation at O1 sites at low levels of hydration (0.005 and 1.66 wt % H₂O) but reported evidence of vacancies on Mg3 sites only.²⁰ Similarly, Ye et al. observed a significant reduction in occupancy at the Mg3 site in a wadsleyite sample with 2.8 wt % H₂O.²¹ Purevjav et al. studied hydrous $\beta$-Mg₂SiO₄ (1.36 wt % H₂O) by neutron time-of-flight single-crystal Laue diffraction,²² concluding that only the Mg3 site exhibited a decreased fractional occupancy, of 0.895(1) and 0.898(1) at 100 and 295 K, respectively. Protons were found to be located along the O1···O4 edges of vacant Mg3 octahedra, in agreement with the earlier predictions of Tsuchiya and Tsuchiya.¹⁴

In a combined FTIR spectroscopy and single-crystal XRD study, Jacobsen et al. investigated cation vacancy ordering and preferential protonation sites in a series of hydrous wadsleyite samples containing between ∼50 ppm and ∼1.06% wt H₂O.²³ XRD analysis revealed only Mg3 site occupancy decreases as protonation increases up to ∼1 wt % H₂O. Analysis of the FTIR spectra showed that all of the main bands in the hydroxyl stretching region can be explained by protonation of O1, consistent with neutron diffraction findings.²³,²⁴ Jacobsen et al. assigned the band at 3000 cm⁻¹ to hydrogen pointing along an O4···O4 edge. The systematic shortening of several hydrogen

bonded O∙∙∙O octahedral edges, attributed to reduced O∙∙∙O repulsive forces following protonation near a Mg3 vacancy, seen from the single-crystal data analysis, supports the interpretation of the FTIR spectra. A more recent study,²⁵ using FTIR spectroscopy, single-crystal XRD, and electron microprobe analysis (EMPA), largely agrees with the conclusions made by Jacobsen et al., confirming that vacancies are formed by the removal of Mg3 cations, charge balanced by preferential protonation at the O1 site. However, in their investigation, Deon et al., inferred from the electron density map that protonation occurs along the O1∙∙∙O4 and O3∙∙∙O4 edges of a vacant Mg3 octahedron. Neutron powder diffraction, in combination with single-crystal XRD and Raman spectroscopy, has also been used to investigate the structure of hydrous wadsleyite, which was deuterated during the synthesis, giving a sample containing ~1.6 wt % D₂O.²⁴ Both the neutron and XRD data showed partial occupancy at the Mg3 site.¹⁸⁻²¹ Sano-Furukawa et al.²⁴ performed diffraction studies on deuterated β-Mg₂SiO₄, finding nonunity occupancies of 0.991(3) and 0.879(2) for Mg1 and Mg3, respectively. Similarly to Kudoh and Inoue,¹⁹ an interstitial “Si2” site is reported with occupancy 0.012(2). Difference Fourier maps determined against the anhydrous structure (determined by single crystal XRD) also find the deuteron positions on the Mg3 octahedral edge lying between O1 and O4 sites with 8.2% occupancy and O1−D and D∙∙∙O4 bond lengths of 1.037(15) Å and 2.041(15) Å, respectively.

Solid-state NMR spectroscopy probes the local structure and ordering of a system, without any requirement for long-range order, and as such, it is particularly useful for identifying local environments in minerals²⁶⁻²⁸ and, more generally, rationalizing disorder in solids.⁹,²⁹,³⁰ Kohn et al. were the first to apply ¹H NMR spectroscopy (along with FTIR) to investigate hydrous wadsleyite.³¹ From the FTIR spectra, 14 of a possible 17 protonation sites¹⁸ are occupied in samples containing 0.8−1.5 wt % H₂O.³¹ The ¹H magic angle spinning (MAS) NMR spectrum of wadsleyite containing 1.5 wt % H₂O was shown to exhibit a complex line shape between 11 and 1 ppm, suggested to result from six overlapping resonances, with the majority of the intensity corresponding to a resonance at 4.2 ppm. It was thus concluded that hydrogen is associated with all four oxygen sites, with O1 being the most prominent site of protonation. More recently, Griffin et al. used multinuclear (¹H, ²H, ¹⁷O, ²⁵Mg, and ²⁹Si) solid-state NMR spectroscopy and first-principles calculations to investigate samples of wadsleyite containing ~3 wt % H₂O or D₂O.³² By comparing experimental NMR spectra to a small set of model structures, the best agreement was found for candidate structures with Mg3 vacancies. In contrast to previous work by Smyth,² structural models with Mg2 vacancies were found to be less energetically stable, with calculated NMR parameters in poor agreement with experiment. The ¹H and ²H MAS NMR spectra showed resonances corresponding to both O1 and silanol hydroxyls, with four major resonances in the ¹H spectrum at 8.6, 6.7, 3.4, and 1.1 ppm. The presence of multiple resonances suggests O1 is not the only site of protonation, a conclusion supported by ¹H−²⁹Si and ¹H−¹⁷O heteronuclear correlation experiments, which confirmed the presence of Si−OH groups. This conclusion was also supported by comparison of calculated and experimental NMR parameters, with analysis of experimental spectra suggesting that silanol defects could account for as much as 20% of total protonation.

In a recent study, we highlighted the effectiveness of using ab initio random structure searching (AIRSS³³⁻³⁵) in combination with DFT-predicted solid-state NMR parameters to investigate the structure of wadsleyite containing 1.65 wt % H₂O.³⁶ From this approach, several well-defined protonation motifs were identified, with the most enthalpically stable structure exhibiting protonation of the two O1 sites around a Mg3 vacancy, with both hydroxyl bonds lying along the O1∙∙∙ O4 octahedral edges. Structures containing a silanol, through the protonation of an O3 or O4, were found to be less stable than those with two protonated O1 sites. This work showed that the use of AIRSS as an unbiased structure-searching technique, along with the computation of solid-state NMR parameters to allow comparison with experiment, is particularly effective as a probe of interstitial disorder in solids.

Here, we present an in-depth investigation into the hydration of wadsleyite, using AIRSS, DFT computation, and NMR spectroscopy to evaluate the set of mechanistic possibilities proposed (in some cases, fairly arbitrarily) in earlier work. AIRSS is used to probe charge balancing by protonation around vacancies at all cation positions at hydration levels of 1.65 and 3.3 wt % H₂O, where the latter hydration level requires two Mg²⁺ vacancies per unit cell, allowing the effect of the intervacancy distances to be considered, albeit with the addition of further complexity. This enables the efficient generation of thousands of possible structural models without any implicit bias arising from knowledge of previous experimental results. A k-means clustering method³⁷,³⁸ is then adopted to enable the selection of unique structures from this much larger set of AIRSS-generated candidates, and, from these, compute NMR parameters to allow comparison with existing³² and new experimental solid-state NMR data. In order to match experimental measurements, we show that more than one type of vacancy must be considered (an observation that ultimately limited the conclusions made in previous work on this system). We demonstrate that it is necessary to consider two-dimensional correlation experiments, which show the spatial proximities of the spins, rather than simply the predicted chemical shifts, in order to exclude some of the lower enthalpy structural models and to confirm the local environments that are observed in the synthesized material. Finally, the inherently quantitative nature of NMR spectroscopy allows us to generate a new, and much more detailed, picture of the structure of this important deep-Earth mineral.

## METHODS
Computational Methods. The protocol for structure generation, optimization, and analysis comprised (i) ab initio random structure searching (AIRSS),³³,³⁴ (ii) DFT geometry optimization during the AIRSS process, (iii) k-means clustering, (iv) DFT optimization with increased accuracy on the selected structures, and (v) GIPAW NMR calculations.³⁹ In (i), AIRSS calculations were based on the anhydrous unit cell of Fe-free wadsleyite.¹⁵ For each hydration mechanism studied, the atoms removed were replaced with either two (for Mg²⁺) or four (for Si⁴⁺) H⁺ atoms. During the AIRSS process, a random translation vector with norm ≤3 Å was applied to the positions of the H atoms, while all other atoms and the unit cell vector were fixed, thus retaining the geometry of anhydrous wadsleyite during initial structure generation. The choice of the translation vector for H was made to allow the vacancy and the surrounding O sites to be explored while reducing the likelihood of structures with H far outside the vacancy, which were found to be high in enthalpy due to charge separation. A minimum separation of all atoms of 0.75 Å was set to


avoid structures containing molecular $H_2$. In (ii), AIRSS-generated structures were optimized at the planewave DFT level, with all atomic positions allowed to relax under quantum mechanical forces, via the CASTEP package (version 8.0). $^{40}$ The PBE exchange-correlation functional was used $^{41}$ along with ultrasoft pseudopotentials $^{42}$ and a planewave energy cutoff of 25 Ry for semihydrous structures and 40 Ry for fully hydrous models. Sampling of the first Brillouin zone was performed on a Monkhorst-Pack grid $^{43}$ with a $k$-point spacing of 0.1 $2\pi$ $\text{\AA}^{-1}$, giving two $k$ points. In step (iii), selection of structures for further study was performed using a $k$-means clustering approach, as implemented in the Soprano Python library, $^{37}$ where in-built genes were extended with system-specific genes using in-house Python scripts (a detailed overview for the $k$-means clustering process is given in section 3 of the Supporting Information). (iv) Subsequently, the chosen structures were further optimized through CASTEP. The PBE exchange-correlation functional was used along with the semi-empirical dispersion correction scheme of Tkatchenko and Scheffler. $^{44}$ Ultrasoft pseudopotentials were generated with ZORA relativistic effects, $^{45}$ and a planewave energy cutoff of 60 Ry was applied. Sampling of the first Brillouin zone was performed on a Monkhorst-Pack grid with a $k$-point spacing of 0.04 $2\pi$ $\text{\AA}^{-1}$, giving 30 $k$ points. A total energy convergence tolerance of $1 \times 10^{-10}$ eV per atom was applied to ensure a well-converged wave function. All atomic positions and the unit cell vector were relaxed under quantum mechanical forces and stresses. In (v), prediction of the relevant solid-state NMR parameters was performed via the GIPAW method, $^{39}$ as implemented in CASTEP. $^{40}$ Calculations used the same parameters as given for (iv) above. NMR parameters were extracted using in-house Python scripts extending the MagresPython library. $^{46}$ Calculations provide the absolute shielding tensor ($\boldsymbol{\sigma}$) and electric field gradient tensor (V). Diagonalization provides their respective principal components, where $\sigma_{11} \leq \sigma_{22} \leq \sigma_{33}$ and $|V_{xx}| \leq |V_{yy}| \leq |V_{zz}|$. The isotropic shielding is given by $(1/3)\text{Tr}(\boldsymbol{\sigma})$ and the predicted chemical shift, $\delta_{\text{iso}} = \sigma_{\text{ref}} - \sigma_{\text{iso}}$. The determination of $\sigma_{\text{ref}}$ is described in section 1 of the Supporting Information. The quadrupolar coupling constant, $C_Q = eQV_{ZZ}/h$, was obtained using nuclear quadrupole moments of 2.860 and $-25.58$ mb for $^2\text{H}$ and $^{17}\text{O}$, respectively. $^{47}$ Total DFT enthalpies, $H$, discussed herein are taken either from the initial geometry optimizations (carried out in step (ii) above) or from NMR calculations (step (v) above), to allow enthalpy comparison at appropriate stages of the structure generation protocol. $H$ is defined as the total electronic energy of a unit cell at zero external pressure, given $H = U + PV$, i.e., $H = U$. Relative enthalpies, $\Delta H$, are calculated as the difference in $H$ between a given structure and the most stable structure of the appropriate composition, i.e., ground-state semihydrous or fully hydrous structures represented, respectively, by motifs $\mathbf{A}$ and $\mathbf{G}$ (see the Results and Discussion). Calculations were performed at the University of St Andrews on a cluster consisting of 90 32-core Intel Broadwell nodes with FDR Infiniband interconnect and 300 TB distributed file system and on the EPSRC ARCHER National Supercomputing Service.

Experimental Methods. NMR spectra of a sample of $^{17}\text{O}$-enriched hydrous wadsleyite ($\sim 3$ wt % hydration), synthesized as described in ref 32, were acquired using a Bruker Avance III spectrometer, operating at a magnetic field strength, $B_0$, of 14.1 T, corresponding to a $^1\text{H}$ Larmor frequency of 600.1 MHz. The sample was packed in a 2.5 mm rotor and rotated at a rate of 30 kHz. $^1\text{H}$ MAS NMR spectra were acquired using a depth $^{48}$ pulse sequence to reduce background signals from the probe. Two-dimensional $^1\text{H}$ double-quantum (DQ) correlation spectra were acquired using the pulse sequence in ref 49, with between 1 and 3 loops of BABA$^{50}$ dipolar recoupling for DQ excitation and reconversion. A recycle interval of 2 s was used for all $^1\text{H}$ NMR experiments. $^1\text{H}$-$^{29}\text{Si}$ CP HETCOR experiments were performed as described in ref 32, using typical rf field strengths of 70 and 50 kHz for $^1\text{H}$ and $^{29}\text{Si}$, contact pulse durations between 1 and 5 ms, with a recycle interval of 3 s and $^1\text{H}$ TPPM decoupling during acquisition. Spectra were referenced relative to TMS using the $\text{CH}_3$ resonance of L-alanine at 1.1 ppm ($^1\text{H}$) and the single resonance of forsterite ($\text{Mg}_2\text{SiO}_4$) at $-62$ ppm ($^{29}\text{Si}$) as secondary references.

## RESULTS AND DISCUSSION

Semihydrous Wadsleyite. The structure of anhydrous wadsleyite, shown in Figure 2a, contains one, three, and four crystallographically distinct Si, Mg, and O sites, respectively. The O1 site is effectively an isolated $\text{O}^{2-}$ species, with five $\text{Mg}^{2+}$ nearest neighbors, and is the only O not bonded to Si. It is therefore considered "underbonded". The remaining oxygen sites are part of pyrosilicate ($\text{Si}_2\text{O}_7^{4-}$) units (see Figure 2b), with O2 bridging between two Si atoms and terminal O3 and O4 sites. The local coordination environments of the three Mg sites are shown in Figure 2b. On the basis of literature consensus, $^{14,23-25,32}$ our initial work focused only on hydration via a single vacancy at the Mg3 position, producing 819 hydrated model structures, with a formal hydration level of 1.65 wt % $\text{H}_2\text{O}$ (termed here semihydrous). $^{36}$ Here, we compare hydration mechanisms involving loss of Mg1 and Mg2 cations at the same hydration level.

Two series of structures with Mg1 vacancies (223 structures) and Mg2 vacancies (245 structures) were generated using AIRSS (see the Computational Methods section and section 2 of the Supporting Information) and compared to the series of 819 structures with Mg3 vacancies generated previously. $^{36}$ In each case, two H atoms were randomly positioned within a 3.0 $\text{\AA}$ radius of the chosen Mg vacancy. This radius was chosen to minimize unstable charge-separated structures that result from one or more H being located further from the vacancy, while still allowing a range of protonation sites to be explored. In lieu of using simple crystal symmetry to differentiate AIRSS-generated structures, $^{34}$ we previously relied upon differences in relative enthalpy when selecting candidates for further study. $^{36}$ In this work, an alternative selection process is presented. Here, a $k$-means clustering was employed, whereby structures were clustered using a set of "genes" that describe each structure through in-house Python scripts making use of the Soprano and ASE Python libraries. $^{37,38}$ Genes were constructed according to relative enthalpy and differentiating structural features, i.e., Mg vacancy type, type of protonated O, and a parameter quantifying the relative orientation of the two hydroxyl bond vectors (see section 3 of the Supporting Information for more detail on the clustering approach). Of the original 1287 AIRSS-generated candidates, $k$-means clustering identified a total of 88 candidate structures for further study, of which 32 have an Mg1, 7 an Mg2, and 49 an Mg3 vacancy. These 88 structures were subjected to a second, more accurate geometry optimization calculation (see the Computational Methods section), and their enthalpies, $\Delta H$, relative to the most stable candidate structure are shown in Figure 3a. Of the original 1287 AIRSS-generated candidates, $k$-means clustering identified a total of 88 candidate structures for further study, of which 32 have an Mg1, 7 an Mg2, and 49 an Mg3 vacancy. These 88 structures were subjected to a second, more accurate geometry optimization calculation (see the Computational Methods section), and their enthalpies, $\Delta H$, relative to the most stable candidate structure are shown in Figure 3a.

The arrangement of protons found in the six lowest $\Delta H$ structures (termed from here on "protonation motifs") is shown in Figure 3b. The structure with the lowest $\Delta H$, represented by protonation motif $\mathbf{A}$, is that identified in our previous work when only Mg3 vacancies were considered. $^{36}$ It consists of two protonated O1 sites with the hydrogen atoms lying along the O1$\cdots$O4 edges of the vacant octahedron, giving

![](./images/812809320390459393_6.jpg)

Figure 3. (a) Relative enthalpies of the 88 fully optimized AIRSS-generated semihydrous wadsleyite structures, with the Mg1, Mg2, and Mg3 vacant structures shown in green, red, and blue, respectively, and (b) the six lowest enthalpy protonation motifs (A−F) also colored according to Mg site vacancy. Small, dark-green spheres represent H atom positions.

two O1−H⋅⋅⋅O4 hydrogen-bonding interactions at a H−O−O−H dihedral angle of 102.7°, agreeing well with a number of previous studies.¹⁴,²³⁻²⁵,³²,³⁶ However, the next group of structures, at $\Delta H = 0.3-0.4$ eV (see Figure 3a), correspond to three different proton arrangements around a vacant Mg1 site and are represented by motifs B, C, and D in Figure 3b. Each of these three motifs exhibits two protonated Si−O oxygen sites (giving two Si−OH (silanol) groups): two O4 in C, two O3 in E, and mixed O3/O4 protonation in C, in all cases, with hydroxyl bond vectors aligned parallel to the edges of the vacant octahedra. The structure represented by motif E ($\Delta H = 0.5$ eV) has an Mg3 vacancy with adjacent protonated O1 and O3 sites, where both hydroxyl bond vectors are orientated along the edges of the vacant octahedron (here the O1⋅⋅⋅O4 and O3⋅⋅⋅O3 octahedral edges), and was identified previously as the second most stable semihydrous structure (when only Mg3 vacancies were considered).³⁶ However, motifs B, C, and D with Mg1 vacancies all now exhibit a lower $\Delta H$ than E. Motif F ($\Delta H = 0.6$ eV) represents the most stable structure with an Mg2 vacancy and contains protonated O1 and O4 sites. While the O4−H hydroxyl forms a hydrogen-bonding interaction with a second O4 site (along an edge of the vacant octahedron), the O1−H bond vector is oriented toward the center of the vacant octahedron with the closest O1−H⋅⋅⋅O4 contact at 2.07 Å at an angle of 124°, suggesting reduced hydrogen bonding, which may explain the high overall $\Delta H$ of Mg2-vacant structures. Just one example of an O2-bound H was found using AIRSS. This was found in a structure with a Mg2 vacancy, which also featured a protonated O1 site and was relatively unstable ($\Delta H \approx 1.1$ eV), suggesting O2 protonation is unlikely, in contrast to some previous work.¹⁶,¹⁷

To facilitate the comparison with existing experimental solid-state NMR data,³¹,³² NMR parameters for the 88 models were determined using GIPAW calculations.³⁹ Figure 4 shows plots of computed hydroxyl (H−O) bond lengths against predicted solid-state NMR parameters ($^1$H $\delta_{\text{iso}}$ and $^2$H $C_Q$), colored by either nearest-neighbor cation or protonated O site. Each shows a reasonably strong linear correlation with an increase in O−H distance, resulting in a downfield $^1$H shift and a decreased $^2$H $C_Q$. From parts a and b of Figure 4, it can be seen that there are relatively well-defined regions of $^1$H $\delta_{\text{iso}}$ and $^2$H $C_Q$ for "Mg−OH" (i.e., H−O1) and Si−OH (i.e., H−O2/O3/O4) hydroxyls. The picture is further clarified by displaying only those structures that fall below an enthalpy limit ($\Delta H < 1.0$ eV), which includes 58 structures (see section 4 of the Supporting Information). As a result, the $^1$H and $^2$H NMR parameters for Mg−OH and Si−OH environments become more separated, with the Mg−OH group having $^1$H $\delta_{\text{iso}} < 5$ ppm and the Si−OH group having $^1$H $\delta_{\text{iso}} > 5$ ppm. However, it is clear that, although distinguishing Mg−OH and Si−OH $^1$H environments is relatively straightforward, it is much more challenging to identify silanol types, i.e., whether an O3 or O4 (or the single example of an O2) site is protonated, due to a more significant overlap between their respective NMR parameters.

![](./images/812809320390459393_7.jpg)

Figure 4. Calculated covalent O−H bond length against (a) $^1$H $\delta_{\text{iso}}$ and (b) $^2$H $C_Q$ colored by protonation site for all 88 fully optimized AIRSS-generated semihydrous wadsleyite structures. H−O1 hydroxyls are classified as "Mg−OH" and H−O2, H−O3, and H−O4 hydroxyls as silanol groups.

It should be noted that the range in computed $^1$H $\delta_{\text{iso}}$ (ca. 1−12 ppm) is larger than that seen experimentally.³² To test

whether this is due to the inclusion of structures too high in energy to be present experimentally, the six lowest enthalpy structures (shown in Figure 3b) were considered in isolation, and $^1$H $\delta_{\text{iso}}$ are given in Table 1. Previously, $^{36}$ it was determined that the three most significant peaks in the experimental $^1$H MAS spectrum of hydrous $\beta$-Mg$_2$SiO$_4$ ($\sim$3 wt $\%$ H$_2$O)$^{32}$ at 3.4, 6.7, and 8.6 ppm likely correspond to protonation at O1, O3, and O4 sites, respectively, based on the presence of structures with only Mg3 vacancies. In the present work, motifs A, E, and B exhibit O1$-$H, O3$-$H, and O4$-$H groups with $^1$H shifts in agreement with this assignment. Notably, $^1$H $\delta_{\text{iso}}$ of the O1$-$H proton in E (2.7 ppm) exhibits an upfield shift relative to O1$-$H in motif A (3.4 ppm); this coincides with a reduction in H$-$O distance from 0.992 Å in A to 0.985 Å in E. In contrast, the structures represented by motifs C and D, despite being similar in $\Delta H$ to B, and noticeably more stable than E, exhibit relatively high O3$-$H $^1$H $\delta_{\text{iso}}$ values. Indeed, these shifts would go beyond those computed for O4$-$H protons (and also beyond the range of the experimental spectrum), in disagreement with the trend in $^1$H $\delta_{\text{iso}}$ of O1$-$H $<$ O3$-$H $<$ O4$-$H identified previously for Mg-3 vacant structures only.$^{36}$ The $\delta_{\text{iso}}$ for the O4$-$H in motif F (7.7 ppm) is also found to be in disagreement with experiment, with a lower value than expected given the previous spectral assignment.

<table>
<caption>Table 1. Calculated $^1$H $\delta_{\text{iso}}$ and $\Delta H$ values for Motifs A$-$F</caption>
<thead>
<tr>
<th>motif</th>
<th>Mg site vacancy</th>
<th>protonation site</th>
<th>$^1$H $\delta_{\text{iso}}$ (ppm)</th>
<th>$\Delta H$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>Mg3</td>
<td>O1</td>
<td>3.4</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O1</td>
<td>3.4</td>
<td></td>
</tr>
<tr>
<td>B</td>
<td>Mg1</td>
<td>O4</td>
<td>8.5</td>
<td>0.33</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O4</td>
<td>8.7</td>
<td></td>
</tr>
<tr>
<td>C</td>
<td>Mg1</td>
<td>O3</td>
<td>10.8</td>
<td>0.37</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O4</td>
<td>8.9</td>
<td></td>
</tr>
<tr>
<td>D</td>
<td>Mg1</td>
<td>O3</td>
<td>10.0</td>
<td>0.37</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O3</td>
<td>10.0</td>
<td></td>
</tr>
<tr>
<td>E</td>
<td>Mg3</td>
<td>O1</td>
<td>2.7</td>
<td>0.50</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O3</td>
<td>6.4</td>
<td></td>
</tr>
<tr>
<td>F</td>
<td>Mg2</td>
<td>O1</td>
<td>2.5</td>
<td>0.56</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O4</td>
<td>7.7</td>
</tr>
</tbody>
</table>

While motifs A, B, and E provide proton environments in good agreement with the conventional $^1$H MAS spectrum, comparison with the corresponding two-dimensional $^1$H DQ MAS spectrum$^{32}$ is not as successful. This experiment is designed to identify pairs of spins in close spatial proximity. The spectrum shows two cross peaks aligned on either side of the 2:1 diagonal for pairs of protons coupled through dipolar interactions. In the spectrum obtained previously,$^{32}$ cross peaks are in apparent agreement with chemical shift positions predicted herein for O1$-$H/O1$-$H, O1$-$H/O4$-$H, and O3$-$H/O4$-$H $^1$H correlations (at the contour levels shown). The presence of motif A is, therefore, supported by this spectrum, with the position and intensity of the O1$-$H/O1$-$H cross peaks confirming the type of $^1$H environments present and the conclusion that local environments similar to A represent the most common structural motif found in the ground-state structure of hydrous $\beta$-Mg$_2$SiO$_4$. However, the O1$-$H/O3$-$H and O4$-$H/O4$-$H correlations, suggested by motifs E and B, respectively, do not appear with any significant intensity in the previously published spectrum, at least at the contour levels shown. It is therefore clear that the semihydrous system ($\beta$-Mg$_2$SiO$_4$ at 1.65 wt $\%$ H$_2$O) considered computationally, while producing a ground-state structure in agreement with conventional and DQ MAS $^1$H NMR experiments of $\beta$-Mg$_2$SiO$_4$ at $\sim$3 wt $\%$ H$_2$O, and suggesting local environments consistent with signals in the experimental $^1$H MAS NMR spectrum, does not fully describe all of the local environments present, nor their relative spatial proximity. To this end, it is therefore necessary to consider a fully hydrous model computationally.

Fully Hydrous Wadsleyite. A hydration level of 3.3 wt $\%$ H$_2$O can be achieved by introducing four hydrogen atoms into a unit cell of wadsleyite, charge balanced by removing two Mg$^{2+}$ cations. In principle, this hydration level can also be achieved by removing one Si$^{4+}$ cation, but the resulting structures are more enthalpically unstable (see section 5 of the Supporting Information). In addition, the synthetic conditions used to prepare samples of hydrous wadsleyite contained an excess of Si (mimicking mantle conditions), further decreasing the likelihood of Si vacancies occurring experimentally. As the ground state structure for semihydrous wadsleyite contained two O1$-$H$\cdots$O4 hydroxyls, charge balanced by the removal of an Mg3 cation, more emphasis was placed on magnesium vacancy combinations that contained at least one Mg3 vacancy, although candidates consisting of two Mg1 or two Mg2 vacancies, respectively, were also considered. Table 2 gives the combinations of magnesium vacancies and intervacancy distances used in the input structures for AIRSS investigations of wadsleyite containing 3.3 wt $\%$ H$_2$O. As was the case for the semihydrous wadsleyite study, hydrogen atoms were allowed to move anywhere within a 3 Å radius of an Mg vacancy, with two hydrogen atoms arranged around each vacancy. See section 6 of the Supporting Information for detail on the choice of vacancy combinations.

<table>
<caption>Table 2. Summary of the Input Structures Created for 11 Individual AIRSS Runs, Indicating the Combination of Mg Cations Removed, the Intervacancy Distance, and the Total Number of Generated Structures</caption>
<thead>
<tr>
<th>AIRSS run</th>
<th>Mg site vacancy combination</th>
<th>intervacancy distance</th>
<th>number of AIRSS-generated structures</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Mg1/Mg1</td>
<td>7.61</td>
<td>400</td>
</tr>
<tr>
<td>2</td>
<td>Mg1/Mg3</td>
<td>2.90</td>
<td>255</td>
</tr>
<tr>
<td>3</td>
<td>Mg1/Mg3</td>
<td>4.96</td>
<td>220</td>
</tr>
<tr>
<td>4</td>
<td>Mg2/Mg2</td>
<td>7.61</td>
<td>260</td>
</tr>
<tr>
<td>5</td>
<td>Mg2/Mg3</td>
<td>3.06</td>
<td>200</td>
</tr>
<tr>
<td>6</td>
<td>Mg2/Mg3</td>
<td>4.89</td>
<td>220</td>
</tr>
<tr>
<td>7</td>
<td>Mg3/Mg3</td>
<td>2.83</td>
<td>200</td>
</tr>
<tr>
<td>8</td>
<td>Mg3/Mg3</td>
<td>2.85</td>
<td>200</td>
</tr>
<tr>
<td>9</td>
<td>Mg3/Mg3</td>
<td>4.02</td>
<td>200</td>
</tr>
<tr>
<td>10</td>
<td>Mg3/Mg3</td>
<td>5.04</td>
<td>200</td>
</tr>
<tr>
<td>11</td>
<td>Mg3/Mg3</td>
<td>7.06</td>
<td>795</td>
</tr>
</tbody>
</table>

The 11 AIRSS runs initially considered (each with a particular combination of Mg vacancies and intervacancy distance) are shown in Figure 5a. In addition, however, due to structural rearrangement via Mg migration seen in some geometry optimizations, several structures formally belonging to new series, i.e., exhibiting a combination of Mg vacancies and intervacancy distance not previously considered, were also seen. Indeed, several structures containing a Mg1/Mg2 vacancy combination, which was expected to be relatively unstable, were produced. Indeed, all of these lie well above the enthalpy cutoff ($\Delta H = 2$ eV, dashed line in Figure 5a);

![](./images/812809320390459393_8.jpg)

Figure 5. Relative enthalpies of (a) AIRSS-generated fully hydrous wadsleyite structures below $\Delta H = 4.0$ eV against the intervacancy distance, showing the enthalpy cutoff of 2.0 eV used in $k$-means clustering (dashed line) and (b) the 199 fully optimized AIRSS- generated fully hydrous wadsleyite structures, obtained after clustering, colored according to Mg site vacancy combination.

structures above this enthalpy were not considered during $k$-means clustering, as described below, or thereafter. Figure 5a shows the enthalpy and intervacancy distance of all generated structures below $\Delta H = 4$ eV. 199 structures were identified via $k$-means clustering for further calculations. Figure 5b shows the relative enthalpies of these selected structures, following more accurate geometry optimization. The global ground state, represented by motif $G$ ($\Delta H = 0.0$ eV, Figure 6), consists of two "isolated" Mg3 vacancies, $\sim$7.1 Å apart, with all four hydrogen atoms forming O1 hydroxyls, i.e., reminiscent of the semihydrous ground-state structure with a second protonation motif A within the unit cell. Motifs H, I, and J (Figure 6) show the proton arrangements found for the three next lowest enthalpy Mg vacancy combinations. The lowest enthalpy structure with Mg3/Mg3 vacancies separated by $\sim$2.9 Å, aligned with the y lattice vector, lies 0.2 eV above the ground state. The protonation arrangement, represented by motif H, shows two O1-H$\cdots$O4 and two O3-H$\cdots$O3 hydroxyls. A slightly higher enthalpy (0.3 eV) is found for two Mg3 vacancies separated by $\sim$2.9 Å but aligned parallel to the x lattice vector. As shown by motif I, two O1-H$\cdots$O4 and two O3-H$\cdots$O4 hydroxyls are found. Due to the short x lattice vector, this combination of Mg3 vacancies leads to a chain of vacant octahedra, where the local ground state features a fully protonated equatorial plane (this is illustrated in Figure 6 by the inclusion of periodic images (starred) in motif I). Motif J represents the local ground state of the next lowest vacancy combination; Mg1/Mg3 at $\sim$2.9 Å, found at $\Delta H = 0.4$ eV.

![](./images/812809320390459393_9.jpg)

Figure 6. Four lowest enthalpy protonation motifs (G−J) from Figure 5b. For G, the nearest (identical) vacancy is at a distance of 7.1 Å. In I, starred (*) atoms lie in the next adjacent unit cell. Small, dark-green spheres represent H atom positions.

Protonation produces two O1-H$\cdots$O4, one O3-H$\cdots$O3, and one O4-H$\cdots$O4 hydroxyls, where the O1−H species lie in the Mg3-vacant octahedron and the O3−H and O4−H hydroxyls are located on the octahedral edge shared by the two vacancies.

The structures represented by motifs H, I, and J, which contain silanol species, are unexpectedly stable, given that the silanol-containing semihydrous wadsleyite structures (motifs B, C, D, and E) showed relatively high enthalpies with respect to the ground state (motif A). This implies a Mg vacancy containing silanol species (i.e., O3−H species in H and I and O3−H and O4−H species in J) is stabilized when edge-sharing with a second Mg vacancy. In addition, the formation of such a cluster of two Mg vacancies, where only two O1 sites are available for protonation and four protons are added, essentially forces silanol formation, as O1 protonation outside the vacant octahedra is disfavored due to charge separation.

As shown in Figure 7, the computed $^1$H solid-state NMR parameters for the fully hydrous wadsleyite structures essentially mirror those observed for the semihydrous structures (see Figure 4), showing both $^1$H $\delta_{\text{iso}}$ and $^2$H $C_Q$ are strongly correlated with O−H bond length. The majority of protons bonded to O1 oxygens (92%) exhibit $\delta_{\text{iso}} < 5$ ppm, whereas 99% of silanol protons exhibit $\delta_{\text{iso}} > 5$ ppm, allowing the two general types of hydroxyl, Mg−OH versus Si−OH, to be separated. These two hydroxyl environment types also have reasonably well-defined $^2$H $C_Q$ ranges (see Figure 7b), with 94% of O1−$^2$H giving $C_Q > 0.2$ MHz and 86% of SiO−$^2$H giving $C_Q < 0.2$ MHz. From Figure 7a and b, it can be seen that it is reasonably facile to distinguish between Mg−OH and Si−OH hydroxyls using either the $^1$H $\delta_{\text{iso}}$ or $^2$H $C_Q$ values, as there is reasonably little overlap in the NMR parameters for the two. However, as highlighted in Figure 7c and d, it is much more challenging to confidently distinguish between the three potential types of silanols (i.e., protonated O2, O3, or O4 sites), where the chemical and structural similarity, particularly between terminal O3 and O4 sites, leads to overlapping NMR parameters (as observed for the semihydrous model system).

In an attempt to better distinguish between the different hydroxyl environments in fully hydrous wadsleyite, the

![](./images/812809320390459393_10.jpg)

Figure 7. Calculated covalent O−H bond length against (a and c) $^1$H $\delta_{\text{iso}}$ and (b and d) $^2$H $C_Q$ colored by (a and b) protonation environment (i.e., Mg−OH or Si−OH) and (c and d) protonation site for all 199 fully optimized AIRSS-generated fully hydrous wadsleyite structures.

computed $^{17}$O solid-state NMR parameters were also considered. Figure 8a shows $^1$H $\delta_{\text{iso}}$ plotted against $^{17}$O $\delta_{\text{iso}}$ of the protonated oxygen atom for all 199 structures. It can be seen that $^{17}$O1−H hydroxyls have a well-defined shift range, with, generally, $\delta_{\text{iso}} < 40$ ppm, whereas the corresponding $^{17}$O shift ($\delta_{\text{iso}}$) for silanol $^{17}$O−H is above 40 ppm, again demonstrating Mg−OH and Si−OH species are easily distinguished by their NMR parameters. However, as seen for $^1$H $\delta_{\text{iso}}$, the $^{17}$O $\delta_{\text{iso}}$ for O3−H and O4−H hydroxyl oxygens cannot be easily distinguished. The plot of $^{17}$O $C_Q$ against $^{17}$O $\delta_{\text{iso}}$ in Figure 8b shows that the NMR parameters for protonated and nonprotonated O1 oxygen species differ significantly, with protonation leading to a decrease in $\delta_{\text{iso}}$ and a noticeable increase in $C_Q$. The NMR parameters of the silanol oxygen atoms also change upon protonation (though to a lesser extent), exhibiting an increased $C_Q$ and an upfield $\delta_{\text{iso}}$. However, again, while distinguishing Mg−OH and Si−OH hydroxyl groups is possible, identifying the type of silanol protonated is not straightforward.

![](./images/812809320390459393_11.jpg)

Figure 8. (a) Calculated $^1$H/$^{17}$O $\delta_{\text{iso}}$ for all 199 fully optimized AIRSS-generated fully hydrous wadsleyite structures, denoted by the protonation site and colored according to the covalent O−H bond length. (b) Plot of calculated absolute $^{17}$O $C_Q$ correlated against $^{17}$O $\delta_{\text{iso}}$ for all 199 fully optimized AIRSS-generated fully hydrous wadsleyite structures.

Since consideration of all fully hydrous structures led to similar NMR parameters for chemically different species and under the assumption that, given a particular arrangement of Mg vacancies, protons would be most likely to adopt the lowest enthalpy arrangement and thus be most likely to contribute to experimental NMR spectra, it was decided to consider a small subset of structures, consisting of the ground state protonation arrangements for the four lowest enthalpy Mg vacancy combinations, i.e., those represented by motifs $\mathbf{G}$, $\mathbf{H}$, $\mathbf{I}$, and $\mathbf{J}$. As shown in Table 3, all 16 protons exhibit $^1$H $\delta_{\text{iso}}$ within the experimental range.$^{32}$ The ground-state structure (represented by motif $\mathbf{G}$) has $^1$H $\delta_{\text{iso}}$ of 3.3−3.5 ppm, matching well with the most intense resonance in the $^1$H MAS spectrum of fully hydrous wadsleyite.$^{32}$ Furthermore, $^1$H $\delta_{\text{iso}}$ values between 6.3 and 6.8 ppm and at 8.6 ppm, which arise from O3 and O4 protonation, in motifs $\mathbf{H}$, $\mathbf{I}$, and $\mathbf{J}$, relate to

<table>
<caption>Table 3. Mg Site Vacancy Combination, Intervacancy Distance, $^1$H $\delta_{iso}$, and $\Delta H$ Values for Structures Represented by Motifs G−J</caption>
<thead>
<tr>
<th>motif</th>
<th>vacancy combination</th>
<th>intervacancy distance (Å)</th>
<th>O−H O type</th>
<th>$^1$H $\delta_{iso}$ (ppm)</th>
<th>$\Delta H$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>G</td>
<td>Mg3/Mg3</td>
<td>7.13</td>
<td>O1</td>
<td>3.3</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>3.3</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>3.5</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>3.5</td>
<td></td>
</tr>
<tr>
<td>H</td>
<td>Mg3/Mg3</td>
<td>2.87</td>
<td>O1</td>
<td>1.9</td>
<td>0.22</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>1.9</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O3</td>
<td>6.8</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O3</td>
<td>6.8</td>
<td></td>
</tr>
<tr>
<td>I</td>
<td>Mg3/Mg3</td>
<td>2.86</td>
<td>O1</td>
<td>1.5</td>
<td>0.33</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>1.5</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O3</td>
<td>6.3</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O3</td>
<td>6.3</td>
<td></td>
</tr>
<tr>
<td>J</td>
<td>Mg1/Mg3</td>
<td>2.88</td>
<td>O1</td>
<td>2.2</td>
<td>0.37</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O1</td>
<td>3.8</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O3</td>
<td>6.8</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>O4</td>
<td>8.6</td>
<td></td>
</tr>
</tbody>
</table>

the two less intense resonances observed experimentally at ~6.7 and ~8.6 ppm. O1−H hydroxyls directly neighboring O3−H hydroxyls (as found in motifs H and I), which produce an upfield shift in $\delta_{iso}$ with respect to those in the ground state, appearing at 1.5−1.9 ppm, are potentially the source of the experimental resonance at 1.1 ppm, a feature suggested in previous work³⁶ to arise possibly from an unknown hydrous impurity or unreacted starting material.

A plot of O−H bond length against $^1$H $\delta_{iso}$ for motifs G−J is given in Figure 9a. This shows that $\delta_{iso}$ differs according to protonation site, with distinct regions observed for O1−H, O3−H, and O4−H. Indeed, the computed $\delta_{iso}$ values for the 16 $^1$H species considered fall within four regions: 1−2, 3−4, 6−7, and 8−9 ppm, mirroring the appearance of the experimental $^1$H MAS spectrum.³² A plot of $^1$H $\delta_{iso}$ against $^{17}$O $\delta_{iso}$ for motifs G−J is shown in Figure 9b. This again shows that the Mg−OH and Si−OH environments have distinct shift ranges, although $^{17}$O $\delta_{iso}$ for O3 and O4 hydroxyls are again very similar. Figure 9c provides a plot of $^1$H $\delta_{iso}$ against $^{29}$Si $\delta_{iso}$ for motifs G−J, with points colored according to protonation environment, i.e., Mg−OH or Si−OH. Colored ellipses highlight the four different types of $^1$H−$^{29}$Si correlations that are present; blue ellipses denote Mg−OH $^1$H environments coupled to Si−O (lower shift) or Si−OH (higher shift) $^{29}$Si environments, and red ellipses denote Si−OH $^1$H environments coupled to Si−O or Si−OH $^{29}$Si environments. The shift differences seen in this case allow these species to be confidently distinguished, with protonation (of O3 or O4) having a significant deshielding effect on $^{29}$Si species. The Mg−OH∙∙∙Si−O and Si−OH correlations have previously been observed in a $^1$H−$^{29}$Si CP HETCOR experiment.³² However, as the contact time is varied, signals with lower intensity can be seen at chemical shift regions that correspond to all four $^1$H−$^{29}$Si correlations identified from the predicted NMR parameters for motifs G−J (see section 8 of the Supporting Information).

![](./images/812809320390459393_12.jpg)

Figure 9. Plots of (a) calculated covalent O−H bond length against $^1$H $\delta_{iso}$ and (b) $^1$H $\delta_{iso}$ against $^{17}$O $\delta_{iso}$, colored by protonation site, for motifs G−J. (c) Plot of $^1$H $\delta_{iso}$ against $^{29}$Si $\delta_{iso}$, colored by protonation environment (i.e., Mg−OH or Si−OH), for motifs G−J.

Figure 10 compares the predicted resonance positions in a two-dimensional $^1$H DQ MAS spectrum, using the computed $^1$H $\delta_{iso}$ values (see Table 3) for the structures represented by motifs G−J, and the experimental $^1$H DQ MAS spectrum of fully hydrous wadsleyite. A $^1$H DQ MAS spectrum provides information on H∙∙∙H spatial proximities, with the increased resolution enabling the number of unique $^1$H sites present to be determined,⁵¹,⁵² and correlates $^1$H $\delta_{iso}$ ($\delta_{SQ}$) in the direct dimension with the sum of the $^1$H $\delta_{iso}$ for two $^1$H species in close spatial proximity ($\delta_{DQ}$) in the indirect dimension. Colored boxes denote predicted coherences arising from motifs G, H/I, and J, shown in blue, red, and green, respectively (where motifs H and I were combined due to their similar NMR parameters). The ground state, represented by motif G, exhibits $^1$H−$^1$H correlations of equivalent or near-equivalent protons resulting from O1−H hydroxyls, with $\delta_{DQ}$ of 6.6−6.8 ppm. Motifs H and I give predicted DQ cross peaks from O1−H/O1−H (shifted upfield with respect to O1−H protons in G), O1−H/O3−H, and O3−H/O3−H correlations, appearing at $\delta_{DQ}$ of 3.0−3.8, 7.7−8.7, and 12.6−13.7 ppm, respectively. With protonated O1, O3, and O4 sites,

![](./images/812809320390459393_13.jpg)

Figure 10. (a) Simulated $^1$H double-quantum correlation plot of $^1$H $\delta_{DQ}$ against $^1$H $\delta_{SQ}$, for structural motifs G−J, with boxes colored by motif. (b) $^1$H (14.1 T, 30 kHz) DQ MAS spectrum of wadsleyite containing $\sim 3$ wt $\%$ H$_2$O (two loops of rotor-synchronized BABA dipolar recoupling).

motif J exhibits DQ coherences from O1−H/O1−H, O1−H/O3−H, O1−H/O4−H (involving upfield- and downfield-shifted O1−H protons), and O3−H/O4−H, appearing at $\delta_{DQ}$ of 6.1, 9.1−10.7, 10.8−12.4, and 15.4 ppm, respectively. It should be noted that the spectrum in Figure 10b is similar to that shown in ref 32 but has higher sensitivity, enabling the lower intensity correlation peaks to be seen more clearly. Additional experiments with different recoupling durations did not reveal any significant differences in the cross peaks observed, only in the absolute signal intensity (see section 8 of the Supporting Information).

The good agreement between the predicted and experimental $^1$H DQ MAS spectra of fully hydrous wadsleyite combined with the predicted $^1$H $\delta_{iso}$ and $^1$H/$^{29}$Si HETCOR plots shown in Figure 9 suggest the consideration of protonation motifs G−J (as opposed to solely G) is not unreasonable and that, combined, they represent a reasonably accurate structural description of true, disordered, hydrous wadsleyite. Further to this, predicted hydroxyl band vibrational frequencies for motifs G−J are in reasonable agreement with the experimental FTIR spectrum of fully hydrous wadsleyite (shown in section 9 of the Supporting Information). If it is assumed that these four motifs alone account for the experimental $^1$H MAS NMR spectrum, the observed relative intensities of the peaks in this spectrum can be used to estimate the proportion of each defect in the sample and thus provide estimated Mg site occupancies (shown in Table 4).

<table><caption>Table 4. Estimated Structural Motif and Mg Site Vacancy Percentages for a Hydrous Wadsleyite Model</caption>
<thead>
<tr>
<th>motif</th>
<th>Mg site vacancy combination</th>
<th>protonation site</th>
<th>contribution to $^1$H MAS signal intensity (%)</th>
<th>contribution to the overall system (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>G</td>
<td>Mg3/Mg3</td>
<td>4 × O1</td>
<td>66</td>
<td>66</td>
</tr>
<tr>
<td>H</td>
<td>Mg3/Mg3</td>
<td>2 × O1</td>
<td>1.5</td>
<td>3</td>
</tr>
<tr>
<td></td>
<td></td>
<td>2 × O3</td>
<td>1.5</td>
<td></td>
</tr>
<tr>
<td>I</td>
<td>Mg3/Mg3</td>
<td>2 × O1</td>
<td>1.5</td>
<td>3</td>
</tr>
<tr>
<td></td>
<td></td>
<td>2 × O3</td>
<td>1.5</td>
<td></td>
</tr>
<tr>
<td>J</td>
<td>Mg1/Mg3</td>
<td>2 × O1</td>
<td>14</td>
<td>28</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1 × O3</td>
<td>7</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>1 × O4</td>
<td>7</td>
<td></td>
</tr>
</tbody>
</table>

The integrated intensities for $^1$H in Mg−OH and Si−OH environments were determined to be 83 and 17%, respectively, with the peaks at $\delta_{iso} = 6.7$ and 8.6 ppm attributed to protonated O3 and O4 sites, respectively, and accounting for 10 and 7% of the total spectral intensity.$^{32}$ Of the four motifs considered, only motif J contains O4−H hydroxyls. It follows, therefore, that this motif must account for 7% of the total fully hydrous wadsleyite system. As motif J consists of $2 ×$ O1−H, $1 ×$ O3−H, and $1 ×$ O4−H hydroxyls, 70% of the O3 peak intensity, which makes up 10% of the total spectral intensity, also comes from J. Therefore, motif J accounts for 28% of the total signal intensity. The remaining intensity of the O3−H hydroxyl peak must then come from either motif H or I. If it is assumed that equal amounts of both of these motifs are present experimentally (since, despite differing in enthalpy by 0.11 eV, H and I affect Mg site occupancy equally), then these motifs will account for 6% of the total spectrum. The remaining O1−H hydroxyl signal intensity then must arise from the ground state, motif G, leaving it responsible for 66% of the total signal intensity. Given motif J contains $1 ×$ Mg1 and $1 ×$ Mg3 vacancies and motifs G−I each contain $2 ×$ Mg3 vacancies, a hydrous wadsleyite model with a G:H:I:J ratio of 66:3:3:28 would exhibit Mg1, Mg2, and Mg3 site occupancies of 0.983, 1, and 0.893, respectively, in excellent agreement with the Mg site occupancies in $\beta$-Mg$_2$SiO$_4$ ($\sim 1.6$ wt $\%$ D$_2$O) derived from diffraction data (0.991(3), 1, and 0.879(2), respectively) provided by Sano-Furukawa et al.$^{24}$ It should be noted, however, that Sano-Furukawa et al. also reported displacement of Si to an interstitial position which they labeled Si2 occupancy 0.012(2); however, no such Si displacement was found in the present calculations.

### CONCLUSIONS
Combining the AIRSS approach with periodic planewave DFT calculations, we have generated candidate structural motifs for hydrous wadsleyite, an important high-pressure mineral found in the transition zone of the Earth's mantle. Our AIRSS procedure involved starting with a structural model of anhydrous wadsleyite, before creating one or two Mg$^{2+}$ vacancies per unit cell, charge balanced by the incorporation of two or four H$^+$, leading to structures termed semihydrous and fully hydrous wadsleyite, corresponding to a 1.65 and 3.3 wt $\%$ H$_2$O hydration level. In contrast to our previous investigation into the structure of semihydrous

wadsleyite, here candidates resulting from the removal of one or more of all three crystallographically unique Mg sites were considered, meaning protonation arrangements around Mg1, Mg2, and Mg3 vacancies were generated. In the case of fully hydrous wadsleyite, where two $Mg^{2+}$ cations must be removed, 11 separate AIRSS input models were created, in which different combinations of Mg vacancies and the variation of intervacancy distance was explored. The 1287 semihydrous and 3150 fully hydrous AIRSS-generated candidate structures were optimized using DFT, before $k$-means clustering was used to identify a subset of structures for more detailed analyses. The structures of the selected 88 semihydrous and 199 fully hydrous wadsleyite models were then optimized again, this time using tighter, more accurate tolerances, prior to the corresponding solid-state NMR parameters being predicted.

For the semihydrous wadsleyite system, the most stable structures, represented by motif A, consist of two protonated O1 sites arranged directly around an Mg3 vacancy, agreeing well with previous studies. $^{24,25,32}$ In this structural motif, the hydroxyls align parallel to the O1$\cdots$O4 edges of the octahedron, with a dihedral angle, $d(HOOH)$, of $102.7^\circ$ and a sum hydroxyl bond vector, $v$, of 1.02, meaning the H atoms are pointing at different O4 atoms. Higher enthalpy structures with Mg3 vacancies, such as that represented by motif B, which have $\Delta H \approx 0.50$ eV (relative to the ground state), are observed when a silanol group is formed, by the protonation of an O3 site, with the formation of two silanol hydroxyls around an Mg3 vacancy resulting in even higher enthalpy structures. In contrast, motif C, the ground state structure with an Mg1 vacancy, which has $\Delta H \approx 0.33$ eV, consists of two silanol groups, formed by the protonation of two of the O4 sites directly surrounding the vacant cation site, with metastable Mg1 vacant structures, motifs D and E, containing at least one O3 silanol. With $\Delta H \approx 0.56$ eV, the most stable example of an Mg2 vacant semihydrous wadsleyite structure, motif F, is less thermodynamically stable than the ground states with Mg1 or Mg3 vacancies and consists of an O1 and an O4 hydroxyl arranged around the octahedron that defines the Mg2 vacancy. Out of the six lowest enthalpy protonation motifs identified from the AIRSS investigation into semihydrous wadsleyite, only the predicted $^1$H solid-state NMR parameters for motifs A, B, and E agree reasonably well with previous studies, $^{32}$ with the $^1$H isotropic chemical shifts of the O3 hydroxyls in motifs C and D appearing further downfield than any significant intensity in the experimental spectrum. Further casting doubt on the predictive ability of the semihydrous wadsleyite model is the lack of a set of structures with $^1$H-$^1$H spatial proximities that fully reproduce the cross peaks seen in the experimental $^1$H DQ MAS spectrum. $^{32}$

The results of our comprehensive AIRSS investigation into the structure and protonation mechanism of semihydrous wadsleyite support assertions made in our previous work, where the ground state structure of hydrous wadsleyite containing 1.65 wt % $\ce{H_{2}O}$ was determined to consist of a Mg3 vacancy, with protonation occurring primarily at the O1 site. $^{32,36}$ However, the discrepancies between the predicted $^1$H NMR parameters and the previous experimental studies of hydrous wadsleyite containing $\sim$3.0 wt % $\ce{H_{2}O}$ (in particular the correlations observed in the experimental $^1$H DQ MAS spectra) indicate that hydration level could affect the preferred type and arrangement of Mg vacancies, the protonation arrangement, and the overall structural stability. To this end, a similar AIRSS investigation was performed on fully hydrous wadsleyite, containing 3.3 wt % $\ce{H_{2}O}$, corresponding to the addition of $4\ \text{H}^+$ per unit cell, requiring the removal of two $Mg^{2+}$ to charge balance the system. The ground state for this hydration level, motif G, was found to comprise two "isolated" Mg3 vacancies $\sim$7.1 Å apart, with four O1–H$\cdots$O4 protonation environments, split evenly over the two Mg3 vacant octahedra, essentially mirroring the semihydrous ground state and agreeing with previous literature. $^{14,24,25,32,36}$ The most likely metastable structures at this hydration level were identified as being those represented by motifs H, I, and J, the first two of which contain two Mg3 vacancies $\sim$2.9 Å apart, with the vacancies aligned parallel to the y and x unit cell vectors, respectively, and with protonation split evenly between O1 and O3 sites. In contrast, motif J has O1, O3, and O4 hydroxyl groups in a 2:1:1 ratio, spread over edge-sharing Mg1 and Mg3 vacant octahedra. The calculated $^1$H solid-state NMR parameters for these four motifs agree well with experimental spectra previously published, $^{32}$ and comparison with the $^1$H DQ MAS spectrum in particular, along with the prediction of $^{17}\text{O}$ and $^{29}\text{Si}$ NMR parameters, has helped elucidate the structure of hydrated defects in this mineral. We conclude that the fully hydrous wadsleyite phase could likely be comprised of hydration defects that resemble motifs G–J (see Figure 11), with a "background" of isolated Mg3 vacancies such as motif G making up the majority of the system (66%) and clustered vacancies from a combination of motifs H and I (6%) and motif J (28%), from which the Mg1:Mg3 vacancy ratio of 86:14 arises.

![](./images/812809320390459393_14.jpg)

Figure 11. Schematic representation of hydrous $\beta$-Mg₂SiO₄ (3.3 wt % $\ce{H_{2}O}$) showing a background array of isolated Mg3 vacancies (66% of defects, based on motif G; blue octahedra) with low-level clustering of Mg3 vacancies (6% of defects, based on motifs H and I; red octahedra) and Mg1/Mg3 vacancies (28% of defects, based on motif J; green octahedra).

This investigation, which represents a substantial expansion of our initial study of hydrous wadsleyite, $^{36}$ our first foray into the use of the AIRSS philosophy for the structural elucidation of disordered materials, highlights the effectiveness of this structure searching approach, especially when combined with both experimental multinuclear solid-state NMR spectroscopy

and DFT predictions of NMR parameters. We have used this approach to probe the structure of Fe-free wadsleyite at two different hydration levels, with our conclusions agreeing well with many previous experimental studies, explaining some of the apparent contradictions observed in previous work, as well as providing new and detailed insight into the local structure and hydration mechanism for this important high-pressure silicate mineral. It is hoped that this investigation will serve as a blueprint for approaching investigations into the structure of a wide range of inorganic materials, especially for those subject to disorder.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/jacs.8b11519.

Information on the referencing of the DFT calculations, the AIRSS-generated structural models, the procedure for $k$-means clustering, additional structural results and NMR parameters of semihydrous wadsleyite, the enthalpic stability of Si-vacant fully hydrous wadsleyite, information on the choice of Mg site combinations used in the AIRSS study of fully hydrous wadsleyite, the Smyth fully hydrous wadsleyite model, additional NMR experiments, and experimental and predicted FTIR spectra. Additional research data for this Article may be accessed at no charge and under CC-BY license at the University of St Andrews Research Portal, https://doi.org/10.17630/9d7c3c11-5d88-4c3c-9bf3-a7899499b11d.⁵³ (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*sema@st-andrews.ac.uk

### ORCID
David McKay: 0000-0003-0362-7848
Sharon E. Ashbrook: 0000-0002-4538-6782

### Author Contributions
∇D.M., R.F.M.: These authors contributed equally.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors would like to thank the ERC (EU FP7 Consolidator Grant 614290 "EXONMR") and EPSRC, the Collaborative Computational Project on NMR Crystallography (CCP-NC), via EP/M022501/1 and EP/J501542/1, and the United Kingdom Car–Parrinello Consortium (UKCP) via EP/P022596/1 for computational support. S.E.A. and C.J.P. would like to thank the Royal Society and Wolfson Foundation for merit awards.

## REFERENCES
(1) Katsura, T.; Ito, E. The system $Mg_2SiO_4$-$Fe_2SiO_4$ at high pressures and temperatures: precise determination of stabilities of olivine, modified spinel, and spinel. J. Geophys. Res. 1989, 94, 15663−15670.
(2) Smyth, J. R. $\beta$-Mg₂SiO₄A potential host for water in the mantle? Am. Mineral. 1987, 72, 1051−1055.
(3) Smyth, J. R. A crystallographic model for hydrous wadsleyite ($\beta$-Mg₂SiO₄): An ocean in the Earth’s interior? Am. Mineral. 1994, 79, 1021−1024.
(4) Huang, X.; Xu, Y.; Karato, S.-I. Water content in the transition zone from electrical conductivity of wadsleyite and ringwoodite. Nature 2005, 434, 746−749.
(5) Inoue, T.; Yurimoto, H.; Kudoh, Y. Hydrous modified spinel, Mg₁.₇₅SiH₀.₅O₄A new water reservoir in the mantle transition region. Geophys. Res. Lett. 1995, 22, 117−120.
(6) Smyth, J. R. A crystallographic model for hydrous wadsleyite ($\beta$-Mg₂SiO₄): An ocean in the Earth’s interior? Am. Mineral. 1994, 79, 1021−1024.
(7) NMR Crystallography; Harris, R. K., Wasylishen, R. E., Duer, M. J., Eds.; John Wiley & Sons: Hoboken, NJ, 2009.
(8) Martineau, C.; Senker, J.; Taulelle, F. NMR Crystallography. Annu. Rep. NMR Spectrosc. 2014, 82, 1−57.
(9) Ashbrook, S.; McKay, D. Combining solid-state NMR spectroscopy with first-principles calculations − a guide to NMR crystallography. Chem. Commun. 2016, 52, 7186−7204.
(10) Winkler, B.; Milman, V.; Hennion, B.; Payne, M. C.; Lee, M.-H.; Lin, S. J. Ab initio total energy study of brucite, diaspore and hypothetical hydrous wadsleyite. Phys. Chem. Miner. 1995, 22, 461−467.
(11) Wright, K.; Catlow, C. R. A. Calculations on the energetics of water dissolution in wadsleyite. Phys. Chem. Miner. 1996, 23, 38−41.
(12) Haiber, M.; Ballone, P.; Parrinello, M. Structure and dynamics of protonated $Mg_2SiO_4$An ab-initio molecular dynamics study. Am. Mineral. 1997, 82, 913−922.
(13) Walker, A. M.; Demouchy, S.; Wright, K. Computer modelling of the energies and vibrational properties of hydroxyl groups in $\alpha$- and $\beta$-Mg₂SiO₄. Eur. J. Mineral. 2006, 18, 529−543.
(14) Tsuchiya, J.; Tsuchiya, T. First principles investigation of the structural and elastic properties of hydrous wadsleyite under pressure. J. Geophys. Res. 2009, 114, B02206.
(15) Horiuchi, H.; Sawamoto, H. $\beta$-Mg₂SiO₄Single-crystal X-ray diffraction study. Am. Mineral. 1981, 66, 568−575.
(16) Downs, J. W. Possible sites for protonation in $\beta$-Mg₂SiO₄ from an experimentally derived electrostatic potential. Am. Mineral. 1989, 74, 1124−1129.
(17) Ross, N. L.; Gibbs, G. V.; Rosso, K. M. Potential docking sites and positions of hydrogen in high-pressure silicates. Am. Mineral. 2003, 88, 1452−1459.
(18) Kudoh, Y.; Inoue, T.; Arashi, H. Structure and crystal chemistry of hydrous wadsleyite, $Mg_{1.75}SiH_{0.5}O_4$ possible hydrous magnesium silicate in the mantle transition zone. Phys. Chem. Miner. 1996, 23, 461−469.
(19) Kudoh, Y.; Inoue, T. Mg-vacant structural modules and dilution of the symmetry of hydrous wadsleyite, $\beta$-Mg₂₋ₓSiH₂ₓO₄ with $0.00 \leq x \leq 0.25$. Phys. Chem. Miner. 1999, 26, 382−388.
(20) Holl, C. M.; Smyth, J. R.; Jacobsen, S. D.; Frost, D. J. Effects of hydration on the structure and compressibility of wadsleyite. $\beta$-(Mg₂SiO₄). Am. Mineral. 2008, 93, 598−607.
(21) Ye, Y.; Smyth, J. R.; Hushur, A.; Manghnani, M. H.; Lonappan, D.; Dera, P.; Frost, D. J. Crystal structure of hydrous wadsleyite with 2.8% $H_2O$ and compressibility to 60 GPa. Am. Mineral. 2010, 95, 1765−1772.
(22) Purevjav, N.; Okuchi, T.; Tomioka, N.; Wang, X.; Hoffmann, C. Quantitative analysis of hydrogen sites and occupancy in deep mantle hydrous wadsleyite using single crystal neutron diffraction. Sci. Rep. 2016, 6, 34988.
(23) Jacobsen, S. D.; Demouchy, S.; Frost, D. J.; Balloran, T. B.; Kung, J. A systematic study of OH in hydrous wadsleyite from polarized FTIR spectroscopy and single-crystal X-ray diffraction: Oxygen sites for hydrogen storage in Earth’s interior. Am. Mineral. 2005, 90, 61−70.
(24) Sano-Furukawa, A.; Kuribayashi, T.; Komatsu, K.; Yagi, T.; Ohtani, E. Investigation of hydrogen sites of wadsleyite: A neutron diffraction study. Phys. Earth Planet. Inter. 2011, 189, 56−62.
(25) Deon, F.; Koch-Muller, M.; Rhede, D.; Gottschalk, M.; Wirth, R.; Thomas, S.-M. Location and quantification of hydroxyl in wadsleyite: New insights. Am. Mineral. 2010, 95, 312−322.


(26) Ashbrook, S. E.; Berry, A. J.; Wimperis, S. $^{17}$O Multiple-Quantum MAS NMR Study of High-Pressure Hydrous Magnesium Silicates. J. Am. Chem. Soc. 2001, 123, 6360-6366.

(27) Ashbrook, S. E.; Berry, A. J.; Wimperis, S. $^{17}$O Multiple-Quantum MAS NMR Study of Pyroxenes. J. Phys. Chem. B 2002, 106, 773-778.

(28) Ashbrook, S. E.; Berry, A. J.; Hibberson, W. O.; Steuernagel, S.; Wimperis, S. High-Resolution $^{17}$O NMR Spectroscopy of Wadsleyite ($\beta$-Mg₂SiO₄). J. Am. Chem. Soc. 2003, 125, 11824-11825.

(29) Ashbrook, S. E.; Dawson, D. M.; Griffin, J. M. Solid-State Nuclear Magnetic Resonance Spectroscopy. In Local Structure Characterisation; Bruce, D. W., O'Hare, D., Walton, R. I., Eds.; John Wiley & Sons Ltd: 2014; pp 1-88.

(30) Moran, R. F.; Dawson, D. M.; Ashbrook, S. E. Exploiting NMR spectroscopy for the study of disorder in solids. Int. Rev. Phys. Chem. 2017, 36, 39-115.

(31) Kohn, S. C.; Brooker, R. A.; Frost, D. J.; Slesinger, A. E.; Wood, B. J. Ordering of hydroxyl defects in hydrous wadsleyite ($\beta$-Mg₂SiO₄). Am. Mineral. 2002, 87, 293-301.

(32) Griffin, J. M.; Berry, A. J.; Frost, D. J.; Wimperis, S.; Ashbrook, S. E. Water in the Earth's mantle: a solid-state NMR study of hydrous wadsleyite. Chem. Sci. 2013, 4, 1523-1538.

(33) Pickard, C. J.; Needs, R. J. High-pressure phases of silane. Phys. Rev. Lett. 2006, 97, 045504.

(34) Pickard, C. J.; Needs, R. J. Ab initio random structure searching. J. Phys.: Condens. Matter 2011, 23, 053201.

(35) Goto, Y.; Tassel, C.; Noda, Y.; Hernandez, O.; Pickard, C. J.; Green, M. A.; Sakaebe, H.; Taguchi, N.; Uchimoto, Y.; Kobayashi, Y.; Kageyama, H. Pressure-Stabilized Cubic Perovskite Oxyhydride BaScO₂H. Inorg. Chem. 2017, 56, 4840-4845.

(36) Moran, R. F.; McKay, D.; Pickard, C. J.; Berry, A. J.; Griffin, J. M.; Ashbrook, S. E. Hunting for hydrogen: random structure searching and prediction of NMR parameters of hydrous wadsleyite. Phys. Chem. Chem. Phys. 2016, 18, 10173-10181.

(37) Sturniolo, S. Soprano—a library developed by the CCP for NMR Crystallography, https://ccp-nc.github.io/soprano/.

(38) Larsen, A. H.; Mortensen, J. J.; Blomqvist, J.; Castelli, I. E.; Christensen, R.; Dulak, M.; Friis, J.; Groves, M. N.; Hammer, B.; Hargus, C.; Hermes, E. D.; Jennings, P. C.; Jensen, P. B.; Kermode, J.; Kitchin, J. R.; Kolsbjerg, E. L.; Kubal, J.; Kaasbjerg, K.; Lysgaard, S.; Maronsson, J. B.; Maxson, T.; Olsen, T.; Pastewka, L.; Peterson, A.; Rostgaard, C.; Schiøtz, J.; Schütt, O.; Strange, M.; Thygesen, K. S.; Vegge, T.; Vilhelmsen, L.; Walter, M.; Zeng, Z.; Jacobsen, K. W. The Atomic Simulation Environment—A Python library for working with atoms. J. Phys.: Condens. Matter 2017, 29, 273002.

(39) Pickard, C. J.; Mauri, F. All-electron magnetic response with pseudopotentials: NMR chemical shifts. Phys. Rev. B: Condens. Matter Mater. Phys. 2001, 63, 245101.

(40) Clark, S. J.; Segall, M. D.; Pickard, C. J.; Hasnip, P. J.; Probert, M. J.; Refson, K.; Payne, M. C. First principles methods using CASTEP. Z. Kristallogr. - Cryst. Mater. 2005, 220, 567-570.

(41) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 1996, 77, 3865-3868.

(42) Vanderbilt, D. Soft self-consistent pseudopotentials in a generalized eigenvalue formalism. Phys. Rev. B: Condens. Matter Mater. Phys. 1990, 41, 7892-7895.

(43) Monkhorst, H. J.; Pack, J. D. Special points for Brillouin-zone integrations. Phys. Rev. B 1976, 13, 5188-5192.

(44) Tkatchenko, A.; Scheffler, M. Accurate molecular van der Waals interactions from ground-state electron density and free-atom reference data. Phys. Rev. Lett. 2009, 102, 073005.

(45) Yates, J. R.; Pickard, C. J.; Payne, M. C.; Mauri, F. Relativistic nuclear magnetic resonance chemical shifts of heavy nuclei with pseudopotentials and the zeroth-order regular approximation. J. Chem. Phys. 2003, 118, 5746-5743.

(46) Sturniolo, S.; Green, T. F. G.; Hanson, R. M.; Zilka, M.; Refson, K.; Hodgkinson, P.; Brown, S. P.; Yates, J. R. Visualization and processing of computed solid-state NMR parameters: MagresView and MagresPython. Solid State Nucl. Magn. Reson. 2016, 78, 64-70.

(47) Pyykko, P. Year-2017 nuclear quadrupole moments. Mol. Phys. 2018, 116, 1328-1338.

(48) Cory, D. G.; Ritchey, W. M. Suppression of signals from the probe in Bloch decay spectra. J. Magn. Reson. 1988, 80, 128-132.

(49) Geen, H.; Titman, J. J.; Gottwald, J.; Spiess, H. W. Solid-state proton multiple-quantum NMR spectroscopy with fast magic angle spinning. Chem. Phys. Lett. 1994, 227, 79-86.

(50) Sommer, W.; Gottwald, J.; Demco, D. E.; Spiess, H. W. Dipolar heteronuclear multiple-quantum NMR spectroscopy in rotating solids. J. Magn. Reson,, Ser. A 1995, 113, 131-134.

(51) Brown, S. P.; Lesage, A.; Elena, B.; Emsley, L. Probing proton- proton proximities in the solid state: High-resolution two-dimensional ¹H-¹H double-quantum CRAMPS NMR spectroscopy. J. Am. Chem. Soc. 2004, 126, 13230-13231.

(52) Brown, S. P.; Spiess, H. P. Advanced solid-state NMR methods for the elucidation of structure and dynamics of molecular, macromolecular and supramolecular systems. Chem. Rev. 2001, 101, 4125-4156.

(53) McKay, D.; Moran, R. F.; Dawson, D. M.; Griffin, J. M.; Sturniolo, S.; Pickard, C. J.; Berry, A. J.; Ashbrook, S. E. A Picture of Disorder in Hydrous Wadsleyite - Under the Combined Microscope of Solid-State NMR Spectroscopy and Ab Initio Random Structure Searching. Dataset. University of St Andrews Research Portal. DOI: 10.17630/9d7c3c11-5d88-4c3c-9bf3-a7899499b11d, 2018.