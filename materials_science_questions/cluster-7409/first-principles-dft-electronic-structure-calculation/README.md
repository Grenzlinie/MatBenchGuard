# First-principles DFT electronic structure calculation

A computational workflow family for studying crystalline materials using density functional theory (DFT). The core pattern involves:

1. **Model construction**: Build periodic supercells (bulk, surface slabs, doped systems, defect-containing cells) with appropriate substitutional or interstitial dopants, vacancies, etc.
2. **Electronic structure calculation**: Use DFT with plane-wave pseudopotential, FP-LAPW, tight-binding, or other methods to compute Kohn–Sham band structures, total/projected densities of states (TDOS/PDOS), magnetic moments, and formation energies.
3. **Property extraction**: Derive optical spectra (dielectric function, absorption), mechanical properties (elastic constants), energetic trends (formation energies, phase stability), and electronic descriptors (band gaps, orbital character).
4. **Verification**: Compare computed numeric values (band gaps, lattice parameters, defect levels, optical peak positions) with experimental data or established theoretical benchmarks, often applying scissor corrections to align band gaps.

Common tools/software: VASP, CASTEP, Quantum Espresso, WIEN2k, ABINIT, GPAW, Phonopy, VASPKIT, etc. Exchange-correlation functionals range from GGA-PBE, LDA, GGA+U, HSE06 to other hybrid approaches. Verification is _numeric_ – the computed quantities must match known experimental or reference values within tolerance.

Each subdirectory (`paper-<id>`) is a standalone Harbor task; its public instruction is `instruction.md` and specifies model, dataset, and tool requirements for reproducibility.

## Papers in this family

| Paper ID | Title | Key computational focus |
|----------|-------|------------------------|
| 1050293411485057031 | Boosting the transparency of metallic SrNbO3 through Ti doping | Band structure & pDOS of Ti-substituted SrNbO3 using VASP (PBE, PAW) |
| 1112351269814534149 | THz carrier dynamics in SrTiO3/LaTiO3 interface two-dimensional electron gases | DFT effective masses, two-temperature model linking DFT to THz transients |
| 319069982623268864 | Influence of cation impurities and both cation and anion nonstoichiometry on aluminum oxide energy gap width | CPA-TB-LMTO-ASA for disordered Al2O3 doped with Zr/Nb/Mo, metallic DOS |
| 811037902279540736 | The first-principles study for the novel optical properties of LiTi2O4, Li4Ti5O12, Li2Ti2O4 and Li7Ti5O12 | GGA-PBE band structures, TDOS/PDOS, band gaps, formal oxidation states |
| 811058774054797314 | The photocatalytic mechanism of BiOI with oxygen vacancy and iodine self-doping | PBE+U (CASTEP) defect formation energies, dopant site preference |
| 811087996131475458 | Formation mechanism of conduction path in titanium dioxide with Ti-interstitials-doped: Car–Parrinello molecular dynamics | CPMD (PBE, 70 Ry) + Dmol³ analysis of O-aggregation and electron localization |
| 811098107415625729 | Influence of titanium doping on the Raman spectra of nanocrystalline ZnAl2O4 | GPAW meta‑GGA band structure, direct gap of pure and Ti‑doped ZnAl2O4 |
| 811105615102345217 | Atomic and electronic structure of Ti substitution in Ca3Co4O9 | PBE+U (U=4 eV) defect formation energies for Ti substitution at Co and Ca sites |
| 811153994503159808 | The first principles calculation and temperature-sensitive luminescence behavior of optimized red phosphor Mg2Al4Si5O18: Eu3+ | Configurational‑coordinate model from DFT, energy barriers for ET and quenching |
| 811260287939248129 | First-principles study of the cubic CaHfO3 (001) surface | GGA (PBE) slab band structures, termination‑dependent band gaps, PDOS |
| 811607250471747586 | Surface energy and excess charge in (1×2)-reconstructed rutile TiO2(110) from DFT+U calculations | PBE+U (U=5 eV) surface free energies via symmetric slab model |
| 811623877745573890 | New layered semiconductors for efficient photoelectrochemical hydrogen and oxygen generation | DFT‑derived band structures and optical gaps of nitrogen‑doped tantalates |
| 811634819036348418 | Presence of excited electronic state in CaWO4 crystals provoked by a tetrahedral distortion | Excited‑state DFT relaxation and mechanistic model for PL in CaWO4 |
| 811668980933591040 | First-principles study of the electronic structure of Pb(ZrTiNb)O3 (PZTN) systems | LDA/FLAPW DOS showing Nb electron donation and metallic gap states |
| 811675285916221441 | Configuration interaction study of the ground and excited states of TiO2 ring structures | RHF/CI on (TiO2)₂ₙ rings, localization vs delocalization of excitons |
| 811782464233013249 | Band-Engineered Bismuth Titanate Pyrochlores for Visible Light Photocatalysis | GGA‑PBE substitutional 3d‑TM‑doping in Bi2Ti2O7, midgap states |
| 811793111956062209 | Formation of Ce3+ at the cerium dioxide (110) surface by doping | PBE+U (U=5 eV) & HSE06 comparison for Ce3+ localization by Ta/Nb |
| 811800172756467713 | (Hyper)polarizabilities and optical absorption spectra of MSi12 clusters (M=Sc–Zn): A theoretical study | B3LYP/6‑311+G(2d) geometry search, optical properties of doped Si clusters |
| 811850816104169472 | Structural, electronic properties and stability of the (1×1) PbTiO3 (111) polar surfaces by first-principles calculations | GGA/PAW slab relaxations, interlayer contraction, rumpling |
| 811853206215720961 | Electronic structure of the Sr2MgSi2O7:Eu2+ persistent luminescence material | GGA+U (U=4.35–7.62 eV) Eu2+ 4f ground state in host gap |
| 811861213951557635 | First-principles calculation of nitrogen-tungsten codoping effects on the band structure of anatase-titania | GGA formation energies for N, W, and N/W codoped anatase |
| 811887387004108801 | Anion photoelectron spectroscopy of transition metal- and lanthanide metal-silicon clusters: MSin− (n=6–20) | Reactivity minima linked to geometric encapsulation of dopant atoms |
| 811936871801159681 | First-principles study of the electronic structures and magnetic properties of 3d transition metal-doped anatase TiO2 | Band coupling model (D₂d) explaining FM/AFM trends in 3d‑TM:TiO₂ |
| 811986197457928192 | First principle prediction of vacancy-induced magnetism in non-magnetic perovskite SrTiO3 | FP-LAPW (GGA) spin‑polarized DOS, magnetic moment from O vacancy |
| 812010485313437697 | Quantification of antisite disorder via combined Mössbauer and NMR | Mössbauer/NMR analysis complemented by DFT formation energies |
| 812016309599469569 | Electronic defects in LaAlO3 | Screened exchange (sX) oxygen vacancy A₁ level, AlLa antisite |
| 812131706961133569 | First-principles investigation of SnO2 at high pressure | FP-LAPW (LDA/GGA) structural optimization, equilibrium parameters for rutile, CaCl₂‑type, cubic |
| 812142564164501504 | The electronic structure of vanadium antimonate | Extended Hückel 3D band structure, orbital‑resolved DOS near EF |
| 812275805806657537 | First-principles study on the electronic structures and absorption spectra for the PbWO4 crystal with lead vacancy | CASTEP GGA absorption spectrum with scissors shift, defect peaks |
| 812300606965284865 | Performance Analysis of Perovskite Solar Cells Using DFT-Extracted Parameters of Metal-Doped TiO2 Electron Transport Layer | DFT+U band gaps for Sn‑doped rutile TiO₂, concentration trends |
| 812309561389088769 | Electronic Structure and Chemical Bonding of Zr Substitution of Ti Site on Pb(Zr1−xTix)O3 Using DV‑Xα Method | DV‑Xα HOMO‑LUMO gap analysis, link to fatigue |
| 812312827636219904 | Tuning fermi level and band gap in Li4Ti5O12 by doping and vacancy for ultrafast Li+ insertion/extraction | Multitechnique (XAS, EPR, DFT) mechanism for enhanced conductivity |
| 812333617266032642 | Electronic structures of InTaO4, a promising photocatalyst | GGA‑PW91 oxygen‑vacancy induced gap states, visible‑light transitions |
| 812364123147862017 | Optical properties of strontium titanate by ab initio calculation within density functional theory | FP-LAPW (GGA) optical spectra with scissor shift, ε₂, ε₁ |
| 812447320497979393 | Electronic structure of 3d transition metal perovskites, LaMO3 from band structure calculations | LMTO‑ASA band structure/DOS feature labeling for LaNiO₃ |
| 812451150115635201 | First-Principles Study of Titanium Dioxide: Rutile and Anatase | Pseudopotential LDA (ABINIT) equilibrium structure for rutile |
| 812568752620044288 | Influence of Rb doping in optical and thermoelectric properties of KCl – A DFT approach | FP-LAPW (GGA) direct band gaps for KCl and K₀.₅Rb₀.₅Cl |
| 812589850950631425 | Boosted photoelectrochemical performance of In2O3 nanowires via modulating oxygen vacancies on crystal facets | One‑step CVD growth and DFT‑assisted defect characterization |
| 812595145995190272 | Long-term heat-storage ceramics absorbing thermal energy from hot water | DFT supercell formation energies + phonon Gibbs free‑energy crossover |
| 812668327036977152 | Interplay between Gd and oxygen vacancy on the electronic properties and defect chemistry of Gd‑doped CeO2: A DFT+U study | Spin‑polarized PBE+U (U=5 eV) Gd‑induced gap states and magnetic moment |
| 812695508710588418 | Tuning optical properties of TiO2 by dimension reduction: from 3D bulk to 2D sheets along {001} and {101} plane | PBE PDOS and 2D sheet band gaps of anatase (101) |
| 812743838190796901 | (title mismatch: “Application of Neural Network to GNSS-R Wind Speed Retrieval” – but reasoning describes Ti/Zr nitride) | DFT‑GGA (PBE) structural parameters for Ti‑substituted ZrN (treat as Ti‑Zr‑N series) |
| 812754245873827840 | Electronic structure of ideal TiO2(110), TiO2(001), and TiO2(100) surfaces | Tight‑binding + scattering‑theoretic method for surface Green's functions |
| 812761398550462465 | First-principles study of Hf/Nb/Zr-doped MAX phases Ti3AlC2 and Ti3SiC2 | DFT (VASP) bonding analysis explaining mechanical property contrast |
| 812777955833937920 | Effects of Oxygen Vacancy on the Magnetic Properties of Ni‑Doped SnO2 Nanoparticles | Experimental RT‑FM and DFT (PBE) confirmation of vacancy effect on magnetism |
| 812816053364064257 | First principles investigation of electronic properties and high refractive index of rutile TiO2 for photovoltaic applications | Quantum Espresso (LDA/GGA) optical properties, ε₁, ε₂, high‑frequency dielectric constants |
| 812841153790476291 | Determination of the structure and properties of an edge dislocation in rutile TiO2 | Multilevel global optimization (SMTBQ → DFT → DFT+U) for dislocation cores |
| 812844949409103873 | Efficient near ultraviolet to near infrared downconversion photoluminescence of La2GeO5: Bi3+, Nd3+ phosphor for silicon-based solar cells | Rietveld refinement + DFT‑assisted site occupancy and phase purity |
| 813067426458501120 | Tuning the pure monoclinic phase of WO3 and WO3‑Ag nanostructures for non-enzymatic glucose sensing application with theoretical insight from electronic structure simulations | Hydrothermal synthesis tuned by DFT‑based electronic structure simulation |
| 813109842506940418 | Electronic structure and optical properties of ALa9‑xEux(GeO4)6O2 (A = Li, Na, K, Rb, Cs, La1/3; x = 0, 0.07) | Photoluminescence excitation/emission assignment, DFT conduction‑band character |
| 813126563963863041 | DFT study of Mg2TiO4 and Ni doped Mg1.5Ni0.5TiO4 as electrode material for Mg ion battery application | PBE projected DOS and magnetic moments to identify Ni redox activity |
| 813130597177229313 | Hydrogen anion and subgap states in amorphous In–Ga–Zn–O thin films for TFT applications | PBE+U (U=7,8,8 eV) IR‑active hydride vibrational modes |
| 813176071523401728 | Solvothermal synthesis and photocatalytic performance of Mg2+-doped anatase nanocrystals with exposed {001} facets | Combined XPS/DFT interpretation of Mg substitution and charge transfer |
| 813185959079182337 | An Experimental and Theoretical Study on the Effect of Silver Nanoparticles Concentration on the Structural, Morphological, Optical, and Electronic Properties of TiO2 Nanocrystals | HSE06 band structure, acceptor‑type gap states from Ag doping |
| 813202329019875329 | Structural and electrochemical properties of hydrogen titanium oxides | Rietveld against neutron diffraction, single‑phase H₂Ti₆O₁₃ synthesis |
| 813224018755715072 | A Large Manganese‑doped Polyoxotitanate Nanocluster: Ti14MnO14(OH)2(OEt)28 | Single‑crystal XRD solution, Keggin‑type core with DFT‑aided band‑gap interpretation |
| 813266449018650625 | Considerations for further scaling of metal–insulator–metal DRAM capacitors | Extraction of tunneling effective mass from TAT model, DFT imaginary band structure |
| 813273446535397377 | Anti‑ferrodistortive‑Like Oxygen‑Octahedron Rotation Induced by the Oxygen Vacancy in Cubic SrTiO3 | HSE06/320‑atom supercell, local AFD rotation around O vacancy |
| 813286145902247938 | Electronic band structure, optical absorption and photocatalytic activity of anatase doped with bismuth or carbon | PAW‑GGA+U (U‑J=3.2,7.2 eV) identification of Bi‑6s/O‑2p‑derived impurity bands |
| 813286512148873216 | Emergence of ferromagnetism at a vacancy on a non‑magnetic ferroelectric PbTiO3 surface: A first‑principles study | Spin‑polarized GGA defect formation energies and magnetic moments |
| 813306062718369792 | First‑principle study of electronic structure of Sn‑doped amorphous In2O3 and the role of O‑deficiency | IPR analysis of a‑ITO with oxygen vacancy, band gap reduction |
| 813327056560455681 | The Influence of Defects on Mo‑Doped TiO2 by First‑Principles Studies | GGA‑WC supercell, band gap narrowing with Mo concentration and defect influence |
| 813329434646937600 | Determination of the electronic band structure of the rutile polymorph of TiO2: a quantum chemical approach | B3LYP surface energy formulation, slab termination stability |
| 813345549376815104 | Effects of Zn impurities on the electronic properties of Pr doped CaTiO3 | GGA+U (VASP) band‑gap defect states, assignment of 614 nm and 380 nm transitions |
| 814510904254136322 | Influence of carbon and phosphorus doping on electronic properties of ZnO | GGA+U C 2p impurity states ~0.4 eV above O 2p VBM, acceptor‑like |
| 814516914867929088 | A computational study of magnetic exchange interactions of 3d and 4f electrons in Ti‑Ce co‑doped AlN | GGA‑PBE formation energies, nearest‑neighbor preference, lattice expansion |
| 814541142585507841 | An Efficient Strategy for Controlled Band Gap Engineering of KTaO3 | HSE06 formation energies for N/halogen codoping, thermodynamic preference |
| 814550228232306691 | Investigating Orientational Defects in Energetic Material RDX Using First‑Principles Calculations | Dispersion‑corrected DFT+CI‑NEB for defect formation and annealing barriers |
| 814565748688027648 | Organic Pollutant Photodecomposition by Ag/KNbO3 Nanocomposites: A Combined Experimental and Theoretical Study | PBE surface adsorption energies, coverage‑dependent Ag/KNbO₃ |
| 814586091171479553 | Simultaneous enhancements in photon absorption and charge transport of bismuth vanadate photoanodes for solar water splitting | Characterization of mild N₂ nitridation with DFT support |
| 814621755220951040 | Selective catalytic reduction of NO with NH3 over V2O5 supported on TiO2 and Al2O3: A comparative study | DFT‑based support‑induced electron transfer mechanism for SCR |
| 814638976592773121 | Improving the photocatalytic activity of TiO2 through reduction | DFT+U (U=5.5 eV) band‑edge shifts due to O‑vac, O‑H, Ti‑int |
| 814751191882792960 | Behaviour of hydrogen in wide band gap oxides | HSE06 negative‑U behaviour of interstitial H in SiO₂ |
| 867745725423812911 | A Two‑Dimensional Carbon Semiconductor | DFT‑predicted planar allotrope Octite SC, lattice parameters and relative energy |
| 867746469661114508 | Electronic Structure and Optical Properties of the Co‑doped Anatase TiO2 Studied from First Principles | LSDA+U optical conductivity, vacancy‑sensitive absorption edge |
| 867752637657776526 | Magnetic orders of LaTiO3 under epitaxial strain: a first‑principles study | LDA+U (U−J=2.3 eV) G‑AFM ground state, band gap 0.45 eV |
| 867757216361349873 | Interplay between strain and oxygen vacancies in lanthanum aluminate | GGA+U (U=10.32 eV) La‑4f shift and octahedral rotation optimization |
| 867761367157833833 | The crystal structure of Rb2Ti2O5 | GGA relaxation confirming C2/m stability, formation enthalpy, band gap |
| 966876699536916489 | Enhanced Charge Separation in Single Atom Cobalt Based Graphitic Carbon Nitride: Time Domain Ab Initio Analysis | PBE+U (U=3.0 eV) Co‑doped GCN mid‑gap states, hole trap analysis |

---

All tasks follow the same family pattern: **DFT‑based electronic structure analysis** with numeric verification against experiment or known benchmarks.
