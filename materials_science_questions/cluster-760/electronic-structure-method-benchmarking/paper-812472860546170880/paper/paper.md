# Atomistic Modeling of PEDOT:PSS Complexes I: DFT Benchmarking
Wesley Michaels,* Yan Zhao, and Jian Qin*

Cite This: *Macromolecules* 2021, 54, 3634−3646

ABSTRACT: Poly(3,4-ethylenedioxythiophene) polystyrene sulfonate (PEDOT:PSS) is a conductive polymer complex integral to both established and next-generation electronic devices. Density functional theory (DFT) and molecular dynamics (MD) studies are increasingly used to probe nanoscale details of this system inaccessible to experiments, but the tools used for these investigations have not yet been thoroughly validated. In Part I of this series, we conduct a benchmarking study of ground-state properties of the PEDOT:PSS system. Predictions by seventeen density functionals (DFs) of geometries, perturbative properties, complexation energies, delocalization error, exciton stability, and torsional barriers are assessed against the double-hybrid DF DSD-PBEP86. We find that the spin contamination of the open-shell PEDOT$ _3^ +$ wave function, a measure of the amount of Hartree−Fock (HF) exchange in a DF, is associated with several properties studied here. The influence of HF exchange on property predictions correlated with its tendency to enhance electron localization. DFs with reduced HF exchange generally yield better vibrational energies, molecular polarizabilities, and torsion barriers. In contrast, LC DFs were necessary to accurately obtain electron delocalization in fractional electron calculations. The use of dispersion corrections more strongly predicts performance in noncovalent complexation benchmarks than that in HF treatment. Systematic errors in exciton stability, obtained through the singlet−triplet energy, are discussed. The generalized gradient approximation (GGA) DF B97-D, hybrid DF HSE06, and LC DF $\omega$B97x-D emerge as the highest-performing functionals in the study. Based on these results, we use a combination of $\omega$B97x-D and DSD-PBEP86 calculations to train an all-atom force field for PEDOT oligomers in Part II of this work.

![](./images/812472860546170880_1.jpg)

## 1. INTRODUCTION
Conductive polymers (CPs)$^1$ are omnipresent in emerging iterations of electrical devices including thermoelectrics,$^2$ field-effect transistors,$^{3,4}$ photovoltaics,$^{5,6}$ and other optoelectronics.$^{3,7}$ In contrast to the crystalline semiconducting materials traditionally used for these applications,$^8$ CP films benefit from being lightweight, flexible, a sustainable feedstock as well as require simple processing steps and low manufacturing costs.$^9$ However, the electrical conductivity of CP films is at present prohibitively low for widespread commercial adoption. Substantial effort has been invested in addressing this concern, and CPs with prior reports of relatively high electrical conductivities are natural targets for further development. The conductive polymer complex poly(3,4-ethylenedioxythiophene) polystyrene sulfonate (PEDOT:PSS)$^{10}$ is the most widely studied CP. PEDOT:PSS devices have demonstrated high electrical conductivities ($\sigma > 4000$ S/cm),$^{11−13}$ high flexibility,$^{13,15}$ and promising ion transport,$^{16,17}$ as well recorded thermoelectric coefficients of merit $(ZT = 0.42)$.$^{14}$

Central to further performance improvements of PEDOT:PSS devices is an understanding of molecular-scale interactions during film processing. Experimental insights over the past two decades have informed the following overarching mechanistic understanding of conductivity enhancements in PEDOT:PSS:

1. Aqueous PEDOT:PSS dispersions are composed of microgels with hundreds of nanometers in size.$^{18}$ These microgels likely adopt a core−shell structure, with a hydrophilic PSS exterior and an amorphous interior of PEDOT complexed to PSS.$^{19}$
2. Pristine, drop-cast PEDOT:PSS films adopt an amorphous morphology consistent with the core−shell structure of PEDOT:PSS microgel particles.$^{20−22}$ The films are electrically insulating (electrical conductivity, $\sigma < 0.1$ S/cm) and demonstrate anisotropic conductivity reflective of their processing conditions.$^{23−25}$
3. High-performing films result from optimizing processing conditions such as film-casting technique$^{2,26−28}$ and cosolvent addition.$^{11,13,29−31}$ In addition to dramatically enhancing electrical conductivity, these modifications

Received: February 14, 2021
Revised: April 2, 2021
Published: April 16, 2021

![](./images/812472860546170880_2.jpg)

elicit qualitative changes in film morphology $^{13,16,22,32}$ and mechanism of electrical conductivity. $^{24}$

Though this understanding can heuristically aid materials design, it lacks the molecular detail to fully permit rational device engineering. Furthermore, owing to the amorphous morphology of PEDOT:PSS films (and of microgels in solution), it is difficult to obtain additional mechanistic insights from experiments. Without precise structure−function relationships, researchers must often resort to combinatorial navigation of the design space, $^{13}$ which slows down device improvements.

Facing these challenges, researchers have increasingly turned to computational techniques to interrogate the microscopic details of PEDOT:PSS. Among these techniques is DFT, $^{33}$ which has proved capable of connecting molecular-scale features to experimentally observable phenomena. For example, it is difficult to obtain the detailed morphology of PEDOT crystallites from experiments. DFT studies of $\pi-\pi$ stacking and anion intercalation in PEDOT crystallites have provided insight into the morphology, $^{34}$ band structure, $^{35}$ and ionization potentials $^{36}$ of these structures. Investigating the transport properties of PEDOT:PSS crystals with DFT calculations, Shi et al. $^{37}$ verified anisotropies in both thermal conductivity and carrier mobility. These findings supported the emerging use of nanowire morphologies in thermoelectric applications. Likewise, it is difficult to probe into the morphological features of PEDOT-poor phases in PE-DOT:PSS films experimentally; DFT has provided insight into these domains, as well. For example, Gangopadhyay et al. identified that complexation to PSS may induce curvature in the otherwise planar PEDOT backbone, explaining experimentally observed redshifting in the PEDOT UV−vis spectra taken from PEDOT:PSS films. $^{38}$

These studies have provided valuable insight into molecular details inaccessible to experiment, but their reliability is predicated on the use of an accurate DF. Benchmarking studies can inform on the DF choice by explicating the accuracy of different DFs for selected properties in related systems. In CP benchmarks, excited-state properties are a primary focus. For example, a study of polyenes, thiophene, and furan oligomers by Salzner and Aydin $^{39}$ found that the LC DFs $\omega$B97x, $^{40}$ CAM-B3LYP, $^{41}$ and $\omega$B97x-D $^{42}$ accurately modeled exciton formation. The authors advocated for the use of $\omega$B97x-D due to its faithful representation of experimental ionization potentials and electron affinities. Afzal and Hachmann $^{43}$ found that PBE0 $^{44}$ and B3LYP $^{45}$ functionals are suitable for modeling the refractive index of a large set of polymers, including polythiophene and polyacetylene. CP benchmarking studies have additionally investigated properties including molecular polarizability, $^{43,46}$ bond length alternation, $^{47}$ orbital energies, $^{48}$ and torsion potentials. $^{49}$

DFT representations of ionic liquids, components used to enhance the electrical conductivity of PEDOT:PSS films, $^{13}$ have also been benchmarked in previous studies. $^{50−53}$ More recent studies recommend the use of increasingly expensive DFs to improve accuracy. Dispersion corrections and incorporation of Hartree−Fock (HF) exchange are generally regarded as necessary for quantitative accuracy $^{50−53}$ (one exception is the reliable performance of M06-L $^{54}$), and range-separated hybrids are recommended if ionization potentials are being calculated.

Although the CP and IL benchmarking studies referenced here reach qualitatively similar conclusions regarding functional choice, we confirm that benchmarking study tailored to PEDOT, PSS, and ionic liquids may more confidently inform on the choice of DF in our system of interest. The present DFT benchmarking study examines ground-state geometries, vibrational spectra, molecular polarizabilities, delocalization error (DE), $^{55−57}$ singlet−triplet energies, torsion potentials, and exciton formation in PEDOT:PSS. This set of properties is chosen for its influence on the morphological behavior of PEDOT:PSS films, as evidenced by both experimental and computational studies. For example, identifying additives to enhance PEDOT crystallinity, and therefore electrical conductivity, in PEDOT:PSS is a key experimental goal. $^{13,22}$ In computational studies supporting this goal, $^{58,59}$ molecular complexation energies are calculated to investigate the dissociation of PEDOT from PSS, for which a reliable DF is necessary. Understanding the influence of morphology on electrical transport in PEDOT:PSS films is also of great importance for device engineering. $^{12,24,32}$ DFT studies can elucidate the energetics of key morphological motifs that influence charge transport in PEDOT, including $\pi-\pi$ stacking, $^{60}$ backbone planarity, $^{39,61}$ and charge carrier equilibria. $^{62}$ Because these property predictions vary by DF, an informed DF choice will strengthen such computational inquiries into the PEDOT:PSS system.

In Part I of this work, we seek to identify a reliable DF for the various molecular properties underlying PEDOT:PSS device function. In Part II, we use $\omega$B97x-D and DF-DSD-PBEP86/jun-cc-pV(T+d)Z to develop all-atom, nonpolarizable MD parameters for two doping states of PEDOT. The following sections comprise Part I. In Section 2, we detail our benchmarking study setup and reference method. In Section 3, we discuss the results of the DFT benchmarking study investigating the molecular geometries, interaction energies, perturbative properties, electron delocalization, exciton stability, and torsional barriers of PEDOT and related species. Our results show that the LC DF by Head-Gordon et al., $\omega$B97x-D, accurately models molecular geometries, interaction energies, and electron delocalization for the PEDOT:PSS system.

## 2. METHODOLOGY
### 2.1. Benchmarking Data.
The present study investigates the following ground-state properties of PEDOT:PSS: molecular geometries, interaction energies, vibrational spectra, molecular polarizability, DE, singlet−triplet energies, torsion potentials, and exciton formation. The compounds used to represent PEDOT:PSS are shown in Figure 1. 1-Ethyl-3-methylimidazolium bis(trifluoromethylsulfonyl)imide (EMIM⁺ TFSI⁻) is included as a candidate ionic liquid, as it is commonly added to PEDOT:PSS formulations to enhance the electrical conductivity of the resultant films. $^{63}$ Geometries, interaction energies, vibrational spectra, and molecular polarizability were tested on the molecules shown in the first row of Figure 1. The DE error was obtained only for PEDOT trimers (PEDOT₃). We used PEDOT hexamers (PEDOT₆) to evaluate torsion potentials, and both PEDOT₆ and PEDOT₁₂ to examine exciton formation. Molecules are visualized using Visualize Molecular Dynamics (VMD) software. $^{64}$ Paul Tol's color schemes $^{65}$ are used throughout.

### 2.2. Wave Function Theory Reference.
Fully ab initio approaches such as Møller−Plesset (MP) perturbation theory $^{66}$ or coupled-cluster (CC) theory $^{67}$ are widely used as

![](./images/812472860546170880_3.jpg)

Figure 1. Molecules used in this benchmarking study. Carbon, hydrogen, oxygen, sulfur, nitrogen, and fluorine atoms are represented as cyan, white, red, yellow, blue, and pink spheres, respectively. PEDOT₃ and PEDOT₆ are not shown.

references in benchmarking studies because they are parameter-free and therefore agnostic to the system being investigated. However, CC treatments vastly exceeded the computational resources available for this work and prelimi- nary MP2 calculations yielded high spin contamination⁶⁸ in open-shell PEDOT₃⁺, suggesting that the underlying Hartree−Fock (HF) wave function is unreliable (see Table S1 for additional details). Double-hybrid density functionals (DHDFs), which add MP2 energetic corrections to DFT- derived electron energy, present a viable alternative: because DFT suffers less from spin contamination than HF, DHDFs have provided better descriptions than MP2 or HF of systems prone to spin contamination such as homolytic bond dissociation reactions.⁶⁹,⁷⁰ Additionally, DHDFs have demon- strated accuracy for many benchmarks⁷⁰ including ionic liquid complexation energies,⁷⁰ static polarizabilities,⁷¹ bond length alternation in polymers,⁷² and torsion potentials of CP dimers.⁴⁹

In this study, we therefore used the DHDF DSD-PBEP86⁷³ (with dispersion corrections) to generate reference data for DFT benchmarking. DSD-PBEP86 has demonstrated excellent performance in modeling small-molecule organic systems, including those of ionic liquids and conjugated polymers, predicting with high accuracy the delocalization error,⁷⁰ the bond length alternation,⁷² vibrational frequencies,⁷⁴ and complexation energies.⁷⁰

Due to computational limitations, we used the Dunning correlation-corrected aug-cc-pVDZ basis set⁷⁵ to calculate DSD-PBEP86 geometries, vibrational spectra, and polar- izabilities in Gaussian 16.⁷⁶ Acknowledging that double-zeta basis sets are typically regarded as too small to guarantee the chemical accuracy required of a reference calculation in a benchmarking study, we calculated all reference single-point (SP) energies using density-fitted DF-DSD-PBEP86/jun-cc- pV(T+d)Z in Psi4.⁷⁷ Geometries for SP calculations were calculated at the DSD-PBEP86/aug-cc-pVDZ level if computa- tionally affordable. If not, we took, from all DFs tested, the geometry that yielded the lowest energy at the DF-DSD- PBEP86/jun-cc-pV(T+d)Z//{X}/jun-cc-pVDZ level. Table S3 lists the two cases in which we made this approximation.

We do not employ the Boys−Bernardi counterpoise (CP) correction⁷⁸ to correct the basis set superposition error (BSSE) in noncovalently bound complexes. In calculations with small basis sets, intrinsic basis set insufficiency has been shown to outweigh BSSE as the primary source of error with respect to complete basis set (CBS) calculations.⁷⁹ Moreover, though CP corrections were found to enhance results for calculations with triple-zeta basis sets in certain cases,⁸⁰ it was also shown that larger basis set errors in noncovalently bound dimers, as compared to those of their monomeric constituents, cause the CP correction to shift the calculated energy away from the CBS energy.⁸¹

2.3. Density Functional Theory Calculations. We benchmark in this work three classes of DFs, all used in prior computational studies of PEDOT:PSS. GGA DFs benefit from relatively low computational cost and are therefore commonly used in plane-wave DFT calculations. Hybrid DFs, which incorporate Hartree−Fock (HF) exchange into the DFT Hamiltonian, are widely used to study organic compounds. LC DFs, which can yield superior DFT results for conjugated polymers, especially for properties such as charge carrier localization³⁹ and electronic excitations.³⁹,⁸² We also examine the influence of dispersion corrections, as they are well known to improve predictions of noncovalently bound complexes.

To identify a DF that accurately represents the PEDOT:PSS system while remaining computationally affordable, we tested 17 density functionals available in Gaussian 16 with various exchange-correlation (XC) potentials and other corrections:
- GGA functionals: B97-D,⁸³ B97-D3⁸³,⁸⁴
- Meta-GGA functionals: M06-L⁸⁵
- Global-hybrid functionals: APFD,⁸⁶ B3LYP,⁴⁵ B3LYP- D3,⁴⁵,⁸⁴ HSE06,⁸⁷⁻⁸⁹ PBE0⁴⁴
- Global-hybrid meta-GGA functionals: M06-HF,⁵⁴ M06- 2X⁵⁴
- Global-hybrid meta- nonseparable gradient approxima- tion (NGA) functionals: MN15⁹⁰
- LC GGA functionals: LC-BLYP,⁴⁵,⁹¹,⁹² LC-ωPBE- D3⁸⁴,⁹³
- LC hybrid functionals: CAM-B3LYP-D3,⁴¹,⁸⁴ CAM- B3LYP,⁴¹ LC-ωHPBE,⁸⁹,⁹³ ωB97x-D⁴²

Molecular geometries, energies, vibrational spectra, torsional potentials, and polarizabilities were computed using Gaussian 16. Psi4 was used for fractional electron calculations to obtain DE. All DFT calculations used the jun-cc-pVDZ basis set.⁹⁴ We used default Gaussian 16 settings for integration grids and convergence criteria for calculations in both Gaussian 16 and Psi4.

DFT investigations of morphology changes during PE- DOT:PSS processing utilize noncovalent interaction energies of PEDOT, PSS, and ionic liquids. We define the interaction energy for DFT as
$$
\Delta E_{\mathrm{AB}}^{\mathrm{int}}=E_{\mathrm{AB}}(\mathrm{AB})-E_{\mathrm{AB}}(\mathrm{A})-E_{\mathrm{AB}}(\mathrm{B}) \tag{1}
$$
where, for molecules A and B, we calculate the energy of the molecule given in parentheses in the conformation taken from the system given as subscripts. In other words, we take geometries for both A and B from those in the AB complex.

3. BENCHMARKING RESULTS

Of the functionals tested, ωB97x-D by Head-Gordon and co- workers most accurately models the set of molecules and properties we chose to represent the PEDOT:PSS system. Table 1 shows the performance of ωB97x-D/jun-cc-pVDZ. Though it overestimates vibrational energies and under- estimates molecular polarizabilities, ωB97x-D provides reliable energetics and molecular geometries. The functional manifests

**Table 1. Summary of Benchmarking Results for the $\boldsymbol{\omega}$B97x-D Functional$^{a}$**

| $\boldsymbol{\omega}$B97x-D       | mean absolute error | overall rank | LC rank |
|------------------------------------|---------------------|--------------|---------|
| geometry                           | 0.72 pm             | 9            | 3       |
| vibrational spectrum               | 13.6 cm$^{-1}$      | 4            | 1       |
| polarizability                     | 8%                  | 12           | 3       |
| ion-exchange energy                | 1.22 kcal/mol       | 2            | 2       |
| interaction energy                 | 2.36 kcal/mol       | 6            | 3       |
| delocalization error               | 1.46 kcal/mol       | 1            | 1       |
| Torsion barrier                    | 6.47 kcal/mol       | 10           | 1       |

$^{a}$Rankings are out of 17 total functionals and six LC functionals

the lowest DE among all functionals tested, in agreement with prior reports detailing its success in modeling excited-state properties of thiophene and furan oligomers.$^{39}$ DE is a measure of the extent to which electron density is spuriously delocalized (or overlocalized) due to inadequacies in the XC formulation of a given DF. Minimizing delocalization error is related to reliable assessments of other molecular properties, including optical excitations,$^{95}$ long-range charge-transfer interactions,$^{95}$ and reaction barrier heights.$^{70}$ Given the aforementioned strengths of LC functionals in extended $\pi$-conjugated systems, $\omega$B97x-D emerges as a candidate for satisfactory modeling of the PEDOT:PSS system.

Table 2 contains the results for all tested functionals. In the following sections, we analyze in greater detail the outcomes of each property tested.

3.1. Geometry. 3.1.1. Intramolecular Geometries. Reliable molecular geometries are a prerequisite to molecular modeling. We obtain the error of a given DF by calculating the mean absolute error (MAE) of two-body internal coordinates (bonds) with respect to DSD-PBEP86/aug-cc-pVDZ values. When calculating the MAE in the geometry of a noncovalent complex, only the intermolecular interaction distance is considered. All tested DFs provide reasonably accurate intramolecular geometries. B3LYP and B3LYP-D3 perform the best with MAEs of 0.32 pm and 0.33 pm, respectively (Table S2). LC-BLYP performs the worst with an MAE of 1.29 pm. The group of functionals employing the B3LYP XC potential (B3LYP, B3LYP-D3, CAM-B3LYP (MAE, 0.56 pm), and CAM-B3LYP-D3 (MAE, 0.56 pm)) consistently performs the best. The other tested styles of XC potentials (Becke 1997 (B97), PBE, and Minnesota) remain within the range of acceptable performance. We attribute the relatively poor results from LC-BLYP to its lack of short-range HF exchange. A similar trend is found between $\omega$B97x-D and B97-D: the former, which includes a 22% short-range HF exchange, outperforms the latter with an MAE of 0.59 pm compared to 0.94 pm. As expected for small molecules, intramolecular geometries from dispersion-corrected functionals and their noncorrected counterparts are substantially similar.

3.1.2. Bond Length Alternation in PEDOT. Important to our parameterization effort is capturing the bond length alternation (BLA) in PEDOT, defined as the difference in length between the single and double bonds along the oligomer backbone. BLA in CPs is a common DF benchmark because of its impact on the electronic gap and a number of related optical properties.$^{47,96,97}$ It is connected to the electron localization,$^{47,97}$ which is in turn driven by HF contributions to the exchange potential of a given DF.$^{57}$ We choose bonds 4 and 5 in ![](./images/812472860546170880_4.jpg) as a representative measure of BLA: for all DFs studied, these two bonds have the largest disparity in the length of all carbon−carbon backbone bonds. We note that PEDOT$_3$ is symmetric about the plane perpendicular to bond 6. To extend this analysis to PEDOT$_3^+$, we examine the BLA between the same two bonds as well as $\Delta$BL, defined as the largest change in the backbone bond length between PEDOT$_3$ and PEDOT$_3^+$. This metric provides a natural way to inspect the strength of the charge-geometry coupling predicted by each DF.

**Table 2. Aggregate Performance of Density Functionals against the DSD-PBEP86/aug-cc-pVDZ Reference$^{b}$**

<table>
  <thead>
    <tr>
      <th>LC</th>
      <th>functional</th>
      <th>$\Delta|Z_{i}|$</th>
      <th>$|\Delta\lambda_{i}|$</th>
      <th>$\Delta|\alpha_{i}|$ (%)</th>
      <th>$\Delta E_{ion}$</th>
      <th>$|\Delta E_{int}|$</th>
      <th>$\Delta E_{DE}^{a}$</th>
      <th>$\Delta E_{tor}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>no LC</td>
      <td>APFD</td>
      <td>0.97</td>
      <td>13.52</td>
      <td>5.9</td>
      <td>0.41</td>
      <td>−2.00</td>
      <td>−</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td></td>
      <td>B3LYP</td>
      <td>0.60</td>
      <td>22.41</td>
      <td>3.5</td>
      <td>−0.68</td>
      <td>10.30</td>
      <td>−7.52</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td></td>
      <td>B3LYP-D3</td>
      <td>0.44</td>
      <td>23.13</td>
      <td>3.6</td>
      <td>−1.98</td>
      <td>1.79</td>
      <td>−7.49</td>
      <td>1.60</td>
    </tr>
    <tr>
      <td></td>
      <td>B97-D</td>
      <td>1.33</td>
      <td>16.94</td>
      <td>1.1</td>
      <td>0.41</td>
      <td>−1.18</td>
      <td>−10.09</td>
      <td>−3.18</td>
    </tr>
    <tr>
      <td></td>
      <td>B97-D3</td>
      <td>0.67</td>
      <td>16.69</td>
      <td>0.7</td>
      <td>1.07</td>
      <td>−0.52</td>
      <td>−10.10</td>
      <td>−2.57</td>
    </tr>
    <tr>
      <td></td>
      <td>HSE06</td>
      <td>0.71</td>
      <td>10.54</td>
      <td>5.7</td>
      <td>0.55</td>
      <td>−1.04</td>
      <td>−8.63</td>
      <td>1.01</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-2X</td>
      <td>0.53</td>
      <td>17.01</td>
      <td>8.3</td>
      <td>−1.72</td>
      <td>1.88</td>
      <td>−3.12</td>
      <td>6.25</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-HF</td>
      <td>2.97</td>
      <td>27.83</td>
      <td>9.6</td>
      <td>1.22</td>
      <td>3.99</td>
      <td>3.49</td>
      <td>10.4</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-L</td>
      <td>1.42</td>
      <td>18.02</td>
      <td>6.8</td>
      <td>−2.06</td>
      <td>3.09</td>
      <td>−9.87</td>
      <td>−0.53</td>
    </tr>
    <tr>
      <td></td>
      <td>MN15</td>
      <td>0.58</td>
      <td>20.91</td>
      <td>6.9</td>
      <td>0.39</td>
      <td>−1.98</td>
      <td>−4.38</td>
      <td>4.64</td>
    </tr>
    <tr>
      <td></td>
      <td>PBE0</td>
      <td>0.72</td>
      <td>12.22</td>
      <td>6.1</td>
      <td>0.50</td>
      <td>−1.09</td>
      <td>−6.65</td>
      <td>1.81</td>
    </tr>
    <tr>
      <td>LC</td>
      <td>CAM-B3LYP</td>
      <td>0.62</td>
      <td>32.47</td>
      <td>7.2</td>
      <td>−0.64</td>
      <td>6.92</td>
      <td>−1.48</td>
      <td>6.53</td>
    </tr>
    <tr>
      <td></td>
      <td>CAM-B3LYP-D3</td>
      <td>0.70</td>
      <td>32.92</td>
      <td>7.2</td>
      <td>−1.95</td>
      <td>2.15</td>
      <td>−1.51</td>
      <td>7.31</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-BLYP</td>
      <td>1.88</td>
      <td>100.66</td>
      <td>11.3</td>
      <td>−0.95</td>
      <td>3.78</td>
      <td>−</td>
      <td>12.8</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-$\omega$HPBE</td>
      <td>0.89</td>
      <td>32.49</td>
      <td>8.4</td>
      <td>−0.17</td>
      <td>7.68</td>
      <td>1.46</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-$\omega$PBE-D3</td>
      <td>0.99</td>
      <td>32.46</td>
      <td>10.8</td>
      <td>−1.34</td>
      <td>1.55</td>
      <td>−</td>
      <td>11.6</td>
    </tr>
    <tr>
      <td></td>
      <td>$\omega$B97x-D</td>
      <td>0.72</td>
      <td>13.55</td>
      <td>7.7</td>
      <td>−0.37</td>
      <td>2.37</td>
      <td>1.46</td>
      <td>6.47</td>
    </tr>
  </tbody>
</table>

$^{a}$Extremal DE (maximum deviation from ideal behavior) is reported. $^{b}$Columns correspond to the functional tested and the two-body internal coordinate value, MAE (Å); vibrational spectrum energy, MAE (cm$^{-1}$); polarizability tensor eigenvalues, MAE (Bohr$^3$/Bohr$^3$); ion-exchange energy signed error (kcal/mol); interaction energy, MAE (kcal/mol); PEDOT$_3$ DE (kcal/mol); and PEDOT$_6^{2+}$ torsion barrier signed error (kcal/mol), respectively. Exciton stability results are omitted (see the main text). Not all functionals tested were available in Psi4; dashes represent DE values that were not calculated. Table S2 delineates intramolecular and intermolecular geometric measures.

![](./images/812472860546170880_5.jpg)

Figure 2. Effect of HF exchange on BLA in PEDOT₃ and PEDOT₃⁺. (a) BLA in PEDOT₃ (blue) and ΔBL (red) versus $S_{\text{polaron}}^2$. (b) Ball-and-stick model of PEDOT with backbone bonds enumerated. BLA measures the difference in lengths between bonds 4 and 5. (c) ΔBL for bonds shown in (b).

![](./images/812472860546170880_6.jpg)

Figure 3. Geometric measures and energetic measures of EDOT···EDOT interaction. (a) (Left) CAM-B3LYP geometry shown in a head-on orientation, (right) ωB97x-D geometry shown in a top-down orientation. $d_{\text{h}}$, $d_{\text{v}}$, $\theta_{\text{ip}}$, and $\theta_{\text{r}}$ denote the horizontal displacement, vertical displacement, interplanar angle, and rotational angle, respectively. The total displacement, $d_{\text{t}} = \sqrt{d_{\text{h}}^2 + d_{\text{v}}^2}$, is not shown. Displacements are defined between the geometric centers of each thiophene ring. (b) $\Delta E$ versus $d_{\text{v}}$ for DFs without dispersion corrections (filled blue circles), DFs with dispersion corrections (open blue diamonds), and DSD-PBEP86 (filled black circle). B3LYP is not included, as it did not yield stable $\pi-\pi$ stacking (see Table S4). (c) Schematic of head-on TOS-H···TOS-H interaction.

We compare DFs on the basis of their total wave function spin, $S^2$, of PEDOT₃⁺. Though the use of $S^2$ is a posteriori, it facilitates comparison of LC and non-LC DFs because it qualitatively captures the total amount of HF exchange used, which is the primary source of spin contamination in hybrid and LC DFT. We note that (1) using the value of $S^2$ after spin-contaminant annihilation⁹⁸ does not alter the conclusions we draw here, and (2) spin contamination is negligible in all DFs tested after the annihilation of the first spin contaminant (see Table S1). The HF/jun-cc-pVDZ and MP2/jun-cc-pVDZ BLA values for PEDOT₃ are upper and lower bounds for the DFs in this study (Figure 2), including DSD-PBEP86. This result indicates that, as with many similar CP systems,⁸²,⁹⁹ HF overlocalizes electrons due to the lack of dynamic correlation,¹⁰⁰⁻¹⁰² whereas the MP2 contribution may overcorrect this problem.

The association between $S^2$ (before spin-contaminant annihilation) and BLA in PEDOT₃ is presented in Figure 2. We find that increasing the HF exchange, whether through a global hybrid or LC contribution, increases BLA in PEDOT₃. Similar trends have been identified in polyacetylene by Körzdörfer, Bredás, and co-workers.¹⁰³,¹⁰⁴ Among the DFs studied, B97-D3 ($S^2 = 0.76$) gives the smallest BLA of 0.048 Å, whereas LC-BLYP ($S^2 = 0.88$) gives the largest BLA of 0.089 Å. Despite having a higher $S^2$ (0.98), DSD-PBEP86 finds a BLA of 0.055 Å, underscoring the impact of MP2 correlation on BLA. HSE06 most closely matches this value (0.057 Å), perhaps due to its underlying similarities with DSD-PBEP86. A similar trend is found for BLA in PEDOT₃⁺: increasing total spin is associated with a more quinoid-like conformation (Figure S1). The magnitude of BLA in PEDOT₃⁺ for all DFs is smaller than in PEDOT₃, indicating that the highest-occupied molecular orbital (HOMO) electrons delocalize across the entire molecule as opposed to assuming a fully quinoid structure. Interestingly, B97-D3 ($S^2 = 0.76$, BLA = $-4.5$ pm) is a clear outlier, whereas B97-D ($S^2 = 0.76$, BLA = $-0.1$ pm) more closely adheres to the trend. Driven by changes in BLA for PEDOT₃ and PEDOT₃⁺, ΔBL (Figure 2) increases with increasing $S^2$, suggesting that a greater HF contribution strengthens charge-geometry coupling in PEDOT trimers.

3.1.3. Intermolecular Interaction. Because full geometry optimizations of EDOT···EDOT and Tos-H···Tos-H complexes were computationally affordable with DSD-PBEP86/aug-cc-pVDZ, we also benchmarked noncovalent interaction distances.

Two competing EDOT···EDOT configurations are examined for all methods: one with fully antiparallel EDOT monomers and another with partially skewed monomers (the right panel of Figure 3a depicts the latter). Optimizations initialized with a parallel structure result in a skewed

**Table 3. Results for Molecular Interaction Energy**

<table>
  <thead>
    <tr>
      <th rowspan="2">LC</th>
      <th rowspan="2">functional</th>
      <th colspan="6">molecular interaction energy (kcal/mol)</th>
      <th colspan="3">errors (kcal/mol)</th>
    </tr>
    <tr>
      <th>PD₃⁺···Tos⁻</th>
      <th>EMIM⁺···TFSI⁻</th>
      <th>PD₃⁺···TFSI⁻</th>
      <th>EMIM⁺···Tos⁻</th>
      <th>PD₁···PD₁</th>
      <th>Tos-H···Tos-H</th>
      <th>MAE</th>
      <th>MSE</th>
      <th>ΔE<sub>ion</sub></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No LC</td>
      <td>DSD-PBEP86-D3BJ</td>
      <td>−98.05</td>
      <td>−83.68</td>
      <td>−86.47</td>
      <td>−86.58</td>
      <td>−11.02</td>
      <td>−23.36</td>
      <td>−</td>
      <td>−</td>
      <td>−</td>
    </tr>
    <tr>
      <td></td>
      <td>APFD</td>
      <td>−100.65</td>
      <td>−87.54</td>
      <td>−89.17</td>
      <td>−88.34</td>
      <td>−12.16</td>
      <td>−27.11</td>
      <td>3.31</td>
      <td>−3.31</td>
      <td>2.00</td>
    </tr>
    <tr>
      <td></td>
      <td>B3LYP</td>
      <td>−90.55</td>
      <td>−64.85</td>
      <td>-71.71</td>
      <td>−74.33</td>
      <td>−2.31</td>
      <td>−19.56</td>
      <td>10.30</td>
      <td>10.30</td>
      <td>0.68</td>
    </tr>
    <tr>
      <td></td>
      <td>B3LYP-D3</td>
      <td>−98.70</td>
      <td>−82.08</td>
      <td>-84.10</td>
      <td>−86.02</td>
      <td>−9.13</td>
      <td>−23.80</td>
      <td>1.74</td>
      <td>0.21</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td></td>
      <td>B97-D</td>
      <td>−94.72</td>
      <td>−75.25</td>
      <td>−78.15</td>
      <td>−81.97</td>
      <td>−8.92</td>
      <td>−19.37</td>
      <td>4.46</td>
      <td>4.46</td>
      <td>1.18</td>
    </tr>
    <tr>
      <td></td>
      <td>B97-D3</td>
      <td>−95.89</td>
      <td>−78.68</td>
      <td>−81.67</td>
      <td>−83.69</td>
      <td>−9.41</td>
      <td>−22.15</td>
      <td>2.65</td>
      <td>2.27</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td></td>
      <td>HSE06</td>
      <td>−93.57</td>
      <td>−68.91</td>
      <td>−74.95</td>
      <td>−77.82</td>
      <td>−3.57</td>
      <td>−22.57</td>
      <td>7.29</td>
      <td>7.29</td>
      <td>1.04</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-2X</td>
      <td>−99.79</td>
      <td>−81.06</td>
      <td>−84.77</td>
      <td>−85.67</td>
      <td>−8.92</td>
      <td>−23.39</td>
      <td>1.88</td>
      <td>0.25</td>
      <td>1.72</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-HF</td>
      <td>−100.13</td>
      <td>−80.87</td>
      <td>−88.96</td>
      <td>−84.57</td>
      <td>−9.52</td>
      <td>−36.39</td>
      <td>3.99</td>
      <td>−2.55</td>
      <td>1.22</td>
    </tr>
    <tr>
      <td></td>
      <td>M06-L</td>
      <td>−97.61</td>
      <td>−78.89</td>
      <td>−81.99</td>
      <td>−83.77</td>
      <td>−7.67</td>
      <td>−19.11</td>
      <td>3.09</td>
      <td>2.68</td>
      <td>2.06</td>
    </tr>
    <tr>
      <td></td>
      <td>MN15</td>
      <td>−99.65</td>
      <td>−81.21</td>
      <td>−84.61</td>
      <td>−85.60</td>
      <td>−9.39</td>
      <td>−23.19</td>
      <td>1.80</td>
      <td>0.25</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td></td>
      <td>PBE0</td>
      <td>−93.21</td>
      <td>−68.81</td>
      <td>−74.65</td>
      <td>−77.60</td>
      <td>−3.52</td>
      <td>−22.16</td>
      <td>7.53</td>
      <td>7.53</td>
      <td>1.09</td>
    </tr>
    <tr>
      <td>LC</td>
      <td>CAM-B3LYP</td>
      <td>−93.72</td>
      <td>−69.55</td>
      <td>−76.11</td>
      <td>−77.83</td>
      <td>−3.31</td>
      <td>−23.09</td>
      <td>6.92</td>
      <td>6.92</td>
      <td>0.64</td>
    </tr>
    <tr>
      <td></td>
      <td>CAM-B3LYP-D3</td>
      <td>−99.72</td>
      <td>−82.52</td>
      <td>−85.45</td>
      <td>−86.16</td>
      <td>−8.62</td>
      <td>−26.18</td>
      <td>2.11</td>
      <td>−0.59</td>
      <td>1.95</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-BLYP</td>
      <td>−98.21</td>
      <td>−76.54</td>
      <td>−82.42</td>
      <td>−82.69</td>
      <td>−5.09</td>
      <td>−28.52</td>
      <td>3.76</td>
      <td>1.94</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-wHPBE</td>
      <td>−92.86</td>
      <td>−69.07</td>
      <td>−75.91</td>
      <td>−77.17</td>
      <td>−3.02</td>
      <td>−21.56</td>
      <td>7.59</td>
      <td>7.59</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td></td>
      <td>LC-wPBE-D3</td>
      <td>−99.66</td>
      <td>−83.05</td>
      <td>−86.29</td>
      <td>−86.40</td>
      <td>−9.60</td>
      <td>−24.94</td>
      <td>1.55</td>
      <td>−0.80</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td></td>
      <td>ωB97x-D</td>
      <td>−96.88</td>
      <td>−78.58</td>
      <td>−82.57</td>
      <td>−83.83</td>
      <td>−9.13</td>
      <td>−22.50</td>
      <td>2.37</td>
      <td>1.94</td>
      <td>0.37</td>
    </tr>
  </tbody>
</table>

*Columns correspond to the functional name and interaction energies (eq 1) for various molecular pairs, and three definitions of the error with respect to DF-DSD-PBEP86/jun-cc-pV(T+d)Z//DSD-PBEP86/aug-cc-pVDZ: MAE, MSE, and Δ mean signed error (MSE), and error in the ion-exchange energy (eq 2). PD<sub>n</sub> is used as shorthand for PEDOT<sub>n</sub>.

configuration. The tested DFs predict that these structures vary in energy by up to 3.1 kcal/mol (APFD, in favor of the skewed configuration) and 1.1 kcal/mol (B97-D, in favor of the antiparallel configuration). Figure 3 demonstrates that both structures can be characterized by two displacements (vertical and horizontal, $d_\text{v}$ and $d_\text{h}$) and two angles (interplanar and rotational, $\theta_\text{ip}$ and $\theta_\text{r}$). DSD-PBEP86 favors the skewed structure by 2.6 kcal/mol, probably because it gives greater $\pi-\pi$ stacking, and that structure has the following parameters: $d_\text{h} = 0.86$ Å, $d_\text{v} = 3.38$ Å, $\theta_\text{ip} = 179^\circ$, and $\theta_\text{r} = 69^\circ$.

Dispersion corrections improve EDOT···EDOT interaction geometries and energies. All functionals tested produce qualitatively similar geometries for the skewed configuration with the exception of B3LYP and CAM-B3LYP, which give unphysically large horizontal displacements of 7.77 and 4.47 Å, respectively. In contrast, B3LYP-D3 and CAM-B3LYP-D3 both give $d_\text{h} = 0.86$ Å, indicating that dispersion corrections are necessary for accurate descriptions of interactions with the B3LYP XC treatment. Table S4 further shows the details of the reported EDOT···EDOT geometric measures. As expected, stronger EDOT···EDOT interaction, as measured by eq 1, is associated with a shorter vertical displacement in $\pi-\pi$ stacking for all tested DFs and DSD-PBEP86. Compared to DFs without dispersion corrections, dispersion-corrected DFs tend to give closer interaction distances and tighter binding.

Geometries of Tos-H···Tos-H complexes are largely similar across all DFs studied, with the exception of intermolecular hydrogen-bonding distances (Figure 3c). The fact that Tos-H···Tos-H is bound by two hydrogen bonds constrains the orientational degrees of freedom in the complex: all DFs predict a "head-on" geometry of the two monomers with minimal variations in the intermolecular angle. DSD-PBEP86 gives an interaction distance of 1.65 Å. Three DFs have less than 1% absolute error with respect to this value, and the best-performing of which are M06-2X, MN15, and B97-D with MAEs of 0.2, 0.2, and 0.3%, respectively. No DFs significantly underbind the complex compared to the reference. Only M06-HF significantly overbinds the complex, with an interaction distance of 1.45 Å.

### 3.2. Interaction Energy.
Table 3 shows the interaction energies for EDOT···EDOT, Tos-H···Tos-H, PEDOT₃⁺···TOS⁻, EMIM⁺···TFSI⁻, EMIM⁺···TOS⁻, and PEDOT₃⁺···TFSI⁻. LC-$\omega$PBE-D3 performs the best in this benchmark, with MAE of 1.5 kcal/mol and MSE of −0.8 kcal/mol with respect to the DF-DSD-PBEP86/jun-cc-pV(T+d)Z//DSD-PBEP86/aug-cc-pVDZ reference. Functionals with dispersion corrections give significantly better results (average MAE of 2.5 kcal/mol) than those without it (average MAE of 6.4 kcal/mol). Although 9 of the 17 DFs tested consistently underbind the complexes, with MSE/MAE > 80%, high-performing DFs have more balanced results. Of the five highest-ranking DFs, four have MSE/MAE < 30%, indicating a low systematic error with respect to the reference.

We additionally determine the "ion-exchange" energy ($\Delta E_\text{ion}$) between PEDOT₃⁺···Tos⁻ and EMIM⁺···TFSI⁻, defined by

$$
\begin{aligned}
\Delta E_\text{ion} &= \left(E_{\text{EMIM}^+ \cdots \text{Tos}^-} + E_{\text{PEDOT}_3^+ \cdots \text{TFSI}^-}\right) \\
&\quad - \left(E_{\text{PEDOT}_3^+ \cdots \text{Tos}^-} + E_{\text{EMIM}^+ \cdots \text{TFSI}^-}\right)
\tag{2}
\end{aligned}
$$

By the DSD-PBEP86 calculation, $\Delta E_\text{ion} = -8.68$ kcal/mol. The average MAE of all DFs with respect to this value is low (1.23 kcal/mol), and we find no meaningful relationship between the interaction energy MAE and $\Delta E_\text{ion}$ for the DFs studied. Nonetheless, the seemingly good performance of many DFs in this benchmark with poor MAE values suggests that cancellation of errors takes place. For example, B3LYP yielded an MAE of 10.3 kcal/mol with respect to individual interaction energies, yet has a $\Delta E_\text{ion}$ of 0.68 kcal/mol. In fact, 15 of the 17 DFs studied have MAE < $\Delta E_\text{ion}$. Given the organic, ionic nature of the species in this example, dispersion interactions

![](./images/812472860546170880_7.jpg)

and dynamic electron correlation are natural sources of error that may fortuitously cancel in a computation, such as eq 2.

### 3.3. Perturbative Properties.
We additionally examine the vibrational spectra and molecular polarizabilities of the small molecules in our benchmarking set. The MAE in vibrational wavenumber, $|\Delta\lambda|$ ($\text{cm}^{-1}$), and the mean percent error in eigenvalues of the polarizability tensor, $\Delta|\alpha|$ (Bohr/ Bohr), are used to obtain each DF. We benchmarked DF performance on all small molecules in the present study, except for $\text{PEDOT}_3^+$ because calculating its second derivatives with DSD-PBEP86 exceeded our computational capabilities. All values in this section are obtained using the jun-cc-pVDZ basis set.

Figure 4a shows the association between $S^2$ in $\text{PEDOT}_3^+$ and $|\Delta\lambda|$ for all molecules tested. The HSE06 and PBE0 DFs give the most accurate vibrational spectra, with the wavenumber MAEs of 10.5 and $12.2\ \text{cm}^{-1}$, respectively. Though this result is in part attributable to the similarities between those DFs and DSD-PBEP86, we note that LC functionals employing PBE exchange perform relatively poorly in this benchmark: the MAEs of LC-$\omega$HPBE and LC-$\omega$PBE-D3 are 32.46 and $32.49\ \text{cm}^{-1}$, respectively. In fact, with the exception of $\omega$B97x-D, which yields a competitive MAE of $13.6\ \text{cm}^{-1}$, the remaining five LC functionals consistently overestimate vibrational energies and are the worst performers of the DFs tested (MAE $>32\ \text{cm}^{-1}$, MSE $>24\ \text{cm}^{-1}$). LC-BLYP is a clear outlier with an MAE of $101\ \text{cm}^{-1}$. Appropriate incorporation of HF exchange appears to dictate accurate prediction of the backbone vibrational modes in $\text{PEDOT}_3^+$ ($1200\ \text{cm}^{-1}<\lambda<1700\ \text{cm}^{-1}$), as evidenced in Figure 4b by the association between $S^2$ and the average energy of those wavemodes for each DF tested.

We found analogous associations between $S^2$ and molecular polarizability, though different DFs (B97-D, B97-D3, and B3LYP) perform better and $\omega$B97x-D does not match the reference closely. In this case, LC functionals systematically underestimate molecular polarizabilities compared to DFs without LC. We attribute this result to the tendency of HF to overestimate electron localization, which results in a larger Coulombic repulsion and more energetically expensive perturbations than the ground state. Polarizability tensor eigenvalues for the molecules studied are shown in Table S5.

### 3.4. Delocalization Error.
Figure 5a shows the full fractional electron curves for selected functionals, where the relative energy $E$ is plotted against the fractional electron occupancy in the highest occupied molecular orbital $N$. The limits $N=-1$ and 0 correspond to the oxidatively doped and neutral forms of $\text{PEDOT}_3$, respectively. Each curve is referenced to the ground-state energy of $\text{PEDOT}_3$ calculated with the corresponding DF. The deviation from ideal, linear behavior with respect to fractional electron occupancy, $\Delta E(N)$ $= E(N) - N\ (E(0) - E(-1))$, is a measure of the delocalization error. $^{57}$ We note that different values of $E(-1)$ by each DF result in different slopes for their corresponding ideal lines.

![](./images/812472860546170880_8.jpg)

Figure 5b shows the residual, $\Delta E$, for $\text{PEDOT}_3$ from selected DFs. Results for all DFs are shown in Figure S2. For simplicity, we henceforth refer to the extremum of each curve in Figure 5b as the DE of the corresponding DF. DFs with no HF contribution exhibit the largest DE: B97-D3 and M06-L deviate from the linear behavior by about $-10\ \text{kcal/mol}$. All the tested global hybrid functionals exhibit excess electron delocalization but vary in performance. For example, the DE of HSE06 is $-8.63\ \text{kcal/mol}$, whereas M06-2X yields a DE of $-2.35\ \text{kcal/mol}$. LC functionals uniformly exhibit the lowest DE of the functionals studied: $\omega$B97x-D and LC-$\omega$PBE-h both overlocalize electrons with a DE of $1.46\ \text{kcal/mol}$. Taken together with the relationship between $S^2$ and BLA discussed in Section 3.1.1, our results highlight that in LC DFs, the correct treatment of DE does not guarantee the correct treatment of BLA (or vice versa). $^{103}$

Because PEDOT oxidation is accompanied by deformation of the polymer backbone, we additionally performed calculations where $\text{PEDOT}_3$ was fully relaxed for each fractional electron occupancy (Figure S2). Although geometric relaxation affects the DE values, the qualitative trends remain identical between DFs, and $\omega$B97x-D still exhibits the lowest DE of all functionals studied.

In principle, DE can be reduced through an "IP-tuning" procedure¹⁰⁵ which modulates the rate at which HF exchange is incorporated in LC functionals. However, it has been shown that increasing the polymer length only gradually changes the optimal IP-tuning,¹⁰⁶ confirming that ωB97x-D maintains a relatively consistent description of electron delocalization for long PEDOT oligomers. Furthermore, because we do not train our force field against any data involving excited-state calculations in Part II of this work, and because tuning may impact the property predictions of ωB97x-D in other benchmarks, we forego any IP-tuning of ωB97x-D in this study.

### 3.5. Exciton Stability.
As PEDOT is expected to be present as long oligomers in commercial formulations,¹⁶ benchmarking the properties of such oligomers is desirable. The type of charge carrier that predominates in PEDOT:PSS films, either polarons or bipolarons, affects the electrical transport and optoelectronic properties of PEDOT:PSS films.¹⁰⁷ We quantify this tendency with the energy gap between the lowest triplet and lowest singlet (T1-S0), defined as $\Delta E_{\text{ST}} = E_{\text{singlet}} - E_{\text{triplet}}$, in fully doped PEDOT₆²⁺: the singlet state is bipolaronic and the triplet state is pair-polaronic.

To confirm that our benchmark method, DSD-PBEP86, can reliably determine $\Delta E_{\text{ST}}$ for small molecules, we recapitulate a subset of $\Delta E_{\text{ST}}$ calculations for substituted vinyl cations by Winter and Falvey performed at the CASPT2/pVTZ// CASSCF/cc-pVTZ level.¹⁰⁸ In the study, $\Delta E_{\text{ST}}$ ranged from $-53.2$ to 14.1 kcal/mol depending on the substituent. For the subset of structures we tested, the authors found that B3LYP/ 6-31G(d,p) captures this wide range of $\Delta E_{\text{ST}}$ values with an MAE of 2.5 kcal/mol. Using their optimized CASSCF/cc- pVTZ geometries, the MAE of our DF-DSD-PBEP86/jun-cc-col pV(T+d)Z//CASSCF/cc-pVTZ calculations was 1.9 kcal/mol (Table S6). The low errors for DF-DSD-PBEP86/jun-cc-pV(T +d)Z and B3LYP/jun-cc-pVDZ//CASSCF/cc-pVTZ (MAE of 2.1 kcal/mol) demonstrate that both methods can reliably estimate $\Delta E_{\text{ST}}$ for small organic molecules. Given that DSD- PBEP86 also accurately models BLA in CPs⁷² and MESIE in a variety of benchmarks,⁷⁰ we conclude that it provides a reliable benchmark for $\Delta E_{\text{ST}}$ of PEDOT oligomers.

SP energies of bipolaronic PEDOT₆²⁺ (spin multiplicity, $m =$ 1) and pair-polaronic PEDOT₆²⁺ ($m = 3$) were calculated at the DF-DSD-PBEP86/jun-cc-pV(T+d)Z//PBE0/jun-cc- pVDZ level of theory because PBE0 geometries yielded the lowest energies, on average, for DF-DSD-PBEP86/jun-cc- pV(T+d)Z SP calculations in PEDOT₆ (see Table S7). Our DF-DSD-PBEP86/jun-cc-pV(T+d)Z calculation gives $\Delta E_{\text{ST}} =$ $-19.6$ kcal/mol, indicating a highly favorable singlet state for PEDOT₆²⁺. The $\Delta E_{\text{ST}}$ values obtained by B97-D3 and LC- ωHPBE are the lowest and highest at $-10.3$ and 2.2 kcal/mol, respectively. We find a strong association between $S^2$ and $\Delta E_{\text{ST}}$, which suggests that increasing HF exchange favors more localized but less energetically favorable bipolarons. The reference $\Delta E_{\text{ST}}$ value is significantly lower than all other DFs tested, suggesting that the DFs underestimate bipolaron favorability in PEDOT₆²⁺. The favorability of bipolarons in highly doped environments has been corroborated exper- imentally,¹⁰⁷ though the dispersity of PEDOT in the films is not known.

Though the calculations of PEDOT₁₂ with DSD-PBEP86 exceeded the computational resources available in this study, we calculate $\Delta E_{\text{ST}}$ and the singlet−quintet energy, $\Delta E_{\text{SQ}} =$ $E_{\text{singlet}} - E_{\text{quintet}}$, in PEDOT₁₂ with the remaining DFs to obtain their predicted favorability of polaron combination. Figure 6 emphasizes that the trends for PEDOT₆²⁺ persist in long

![](./images/812472860546170880_9.jpg)

Figure 6. Exciton combination energies in doped PEDOT oligomers. (a) Singlet−triplet energy for PEDOT₆²⁺. Reference $\Delta E_{\text{ST}}$ (at DF- DSD-PBEP86/jun-cc-pV(T+d)Z level of theory) is shown by the dashed line. (b) Various exciton energies for PEDOT₁₂: $\Delta E_{\text{ST}}$ for $q =$ 2 (doping level = 17%, blue), $\Delta E_{\text{ST}}$ for $q = 4$ (doping level = 33%, red), and $\Delta E_{\text{SQ}}$ for $q = 4$ (doping level = 33%, green). Open diamonds indicate DFs that employ LC corrections, whereas filled circles indicate DFs that do not use LC corrections.

PEDOT oligomers. Almost all DFs predict PEDOT₁₂²⁺ to exist in the triplet state, suggesting that confinement effects are not significant enough to overcome the Coulombic repulsion between electrons and holes in each polaron. However, as the doping level increases, the polaron combination into bipolarons becomes more favorable. With the exceptions of LC-ωHPBE and LC-ωPBE-D3, which find triplet states to be the most favorable in PEDOT₁₂²⁺, all DFs predict that singlet states are more favorable than triplet states, which in turn are more favorable than quintet states. The trends in Figure 6 highlight that quantitatively different predictions of polaron− bipolaron equilibrium result from differing HF treatments in a DF. Similar behavior was observed in Fe(II) transition-metal complexes, where modulating the amount of pure HF exchange in hybrid DFs linearly affected the quintet−singlet energy gap.¹⁰⁹ In light of the reference results for PEDOT₆²⁺, we recommend that DHDFs be used for calculations of relative exciton stability in PEDOT.

### 3.6. Torsional Barriers.
The energetic cost of rotating a CP about an intermonomer bond along its backbone affects its stiffness and conformational properties, its crystallization,¹⁰⁷ and its electrical transport properties.¹¹⁰ We performed relaxed torsion scans about the bond connecting monomers 3 and 4 of PEDOT₆²⁺, in both $m = 1$ (bipolaronic, BP) and $m = 3$ (pair- polaronic, PP) states. Reference energies were calculated at the DF-DSD-PBEP86/jun-cc-pV(T+d)Z//PBE0/jun-cc-pVDZ level of theory. The trans configuration (an S-C-C-S dihedral angle of $\phi = 180^\circ$) was found to be the energetic minimum for BP PEDOT₆²⁺ by all DFs, with an energetic maximum at $\phi =$ $90^\circ$, a local minimum at $\phi \approx 30^\circ$, and a local maximum at the cis configuration of $\phi = 0^\circ$. A similar trend is found for the PP torsion profile, although some functionals with large amounts of HF exchange predict that $\Delta E_{\phi=180^\circ} > \Delta E_{\phi=90^\circ}$. We find that torsional barriers for BP PEDOT₆²⁺ vary widely (from 16.5 to 32.4 kcal/mol) and are positively associated with $S^2$ in PEDOT₃. M06-L and B3LYP barriers most closely match the reference value of 19.7 kcal/mol with errors of 0.5 and $-0.7$ kcal/mol, respectively. Table 2 highlights that LC functionals almost uniformly overestimate the BP torsional barrier compared to non-LC functionals, with the exception of M06-HF. Torsional barriers for PP PEDOT₆²⁺ are lower for all

![](./images/812472860546170880_10.jpg)

Figure 7. Overview of torsional profile results. (a) Profiles of BP PEDOT$_{6}^{2+}$ from selected DFs and DSD-PBEP86, progressing from the trans configuration ($\phi = 180^\circ$) to the cis configuration ($\phi = 0^\circ$). (b) Torsional barriers (at $\phi = 90^\circ$) for BP (blue) and PP (red) PEDOT$_{6}^{2+}$ for all DFs tested. (c) Evolution of $\phi_c$ with increasing $S^2$. B97-D3 is not shown (see the main text). In both (b) and (c), non-LC and LC DFs are shown as filled circles and open diamonds, respectively.

DFs studied: all functionals yield a barrier between 2.1 and 8.4 kcal/mol.

Because of the dependence of both $\Delta E_{ST}$ (see Section 3.5) and torsion barrier heights on $S^2$, the BP spin state is more favorable in the trans configuration and eventually evolves into a PP state at some "critical" $\phi_c$ (Figure S3c, Table S8). The functionals exhibiting stronger electron localization generally predict larger values of $\phi_c$. The wide range of $\phi_c$ values shown demonstrates how this crossover behavior can significantly impact the shape of the minimum potential energy surface. For example, the $\Delta E_c$ values from $\omega$B97x-D and B3LYP are 3.7 and 13.8 kcal/mol, respectively. LC-$\omega$HPBE, LC-$\omega$PBE-D3, and LC-BLYP give $\phi_c = 180^\circ$, signifying that the PP state is more stable for all $\phi$. In contrast, DSD-PBEP86 indicates that the BP state is more stable for all $\phi$. Interestingly, only B97-D3, one of the two GGA functionals tested in this study, exhibits the same. Because the value of $\phi_c$ by B97-D3 is undefined, it is not shown in Figure 7 ($\phi_c = 88^\circ$ by B97-D, constituting a very similar prediction). Thus, although a small amount of HF exchange generally leads to a closer agreement with the DSD-PBEP86 BP PEDOT$_{6}^{2+}$ torsional profile, a pure DF provides a more faithful representation of the PES from this qualitative perspective.

## 4. CONCLUSIONS
In this work, we conducted a DFT benchmarking study of the PEDOT:PSS system, investigating the ground-state geometries, vibrational spectra, molecular polarizabilities, delocalization error, singlet−triplet energies, exciton formation, and torsion potentials. We found the spin contamination $S^2$ of the PEDOT$_{3}^{+}$ wave function, a measure of the amount of HF exchange in a DF, to be strongly associated with the DF performance in many benchmarks (Figures 2, 4, 6 and 7). The impact of HF exchange on these results is readily understood through the increased electron localization HF obtained compared to pure DFT, suggesting that this finding is applicable to other CPs beyond PEDOT.

The fact that no one value of HF exchange was able to match the reference values for all benchmarks highlights the importance of property-specific DF choice for this system. For example, HF exchange is not a good predictor of performance in noncovalently bound systems; perhaps, unsurprisingly, dispersion corrections were found to more uniformly improve interaction geometries and energies. In contrast, DFs with a tendency toward greater electron localization, including LC DFs, generally overestimate vibrational energies and underestimate molecular polarizabilities.

The exciton stability and torsional profile benchmarks strongly suggest that DFT calculations of relative exciton stability in CPs, especially those performed with LC functionals, should be analyzed carefully. LC DFs deviated most significantly from the reference due to their tendency to more strongly localize electrons; LC-BLYP, LC-$\omega$-HPBE, and LC-$\omega$PBE-D3 predict PP to be the stable electronic state for PEDOT$_{6}^{2+}$, qualitatively deviating from the DSD-PBEP86 prediction of a more stable BP PEDOT$_{6}^{2+}$. Only B97-D3, one of the two GGA functionals tested in this study, matches the DSD-PBEP86 prediction that the BP state is more stable than the PP state throughout the entire torsional profile. As increasingly intricate devices dynamically alter the doping state of PEDOT$^{107}$ to, for example, modulate electrical current in electrochemical transistors, $^{17}$ a precise understanding of the charge carrier equilibrium remains an important target of future work.

From our findings, we make the following recommendations regarding the functional choice for systems containing PEDOT:
- GGA and meta-GGA DFs: B97-D, for noncovalent interaction and ground-state intramolecular properties.
- Hybrid DFs: HSE06, for ground-state intramolecular properties.
- LC DFs: $\omega$B97x-D, for general use. Good for noncovalent interaction, ground-state intramolecular properties, and properties directly influenced by DE.

In Part II of this study, we develop an all-atom, nonpolarizable force field for PEDOT in undoped and highly doped charge states. From the results shown here, we elect to use a mix of $\omega$B97x-D and DSD-PBEP86 calculations as training data. Despite the general trends regarding LC DFs, $\omega$B97x-D has the second-highest average ranking in the study (6.4), behind only B97-D3 (6.1) (Table S9). $\omega$B97x-D falls short from B97-D3 primarily in predictions of molecular polarizability and torsional barriers but predicts DE significantly more accurately. Because $\omega$B97x-D also provides accurate excited-state properties for PEDOT, $^{39}$ this choice also maximizes compatibility with any future DFT/MM investigations that rely on MD for sampling.

### ASSOCIATED CONTENT
#### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.macromol.1c00351.

Full results for DE, EDOT$\cdots$EDOT complexation, BLA, and torsional profile benchmarks; and full rankings of DF performance in benchmarks (PDF)

### AUTHOR INFORMATION

#### Corresponding Authors
Wesley Michaels — Department of Chemical Engineering, Stanford University, Stanford, California 94305, United States; Email: wpm216@stanford.edu

Jian Qin — Department of Chemical Engineering, Stanford University, Stanford, California 94305, United States; orcid.org/0000-0001-6271-068X; Email: jianq@stanford.edu

#### Author
Yan Zhao — State Key Laboratory of Silicate Materials for Architectures, Wuhan University of Technology, Wuhan 430070, China; orcid.org/0000-0002-1234-4455

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.macromol.1c00351

### Notes
The authors declare no competing financial interest.

### ACKNOWLEDGMENTS
W.M. and J.Q. thank Zhenan Bao, Tom Markland, Todd Martínez, Claudio Melis, Michael Beckinghausen, Vivian Feig, and Scott Keene for helpful conversations. This work was supported by the Stanford Precourt Institute for Energy, the National Science Foundation Graduate Research Fellowship Program (Grant No. DGE-1656518), and the David G. Mason Fellowship from the Stanford University Department of Chemical Engineering.

### REFERENCES
(1) Swager, T. M. 50th Anniversary Perspective: Conducting/Semiconducting Conjugated Polymers. A Personal Perspective on the Past and the Future. *Macromolecules* 2017, 50, 4867−4886.

(2) Culebras, M.; Gómez, C. M.; Cantarero, A. Review on Polymers for Thermoelectric Applications. *Materials* 2014, 7, 6701−6732.

(3) Geoghegan, M.; Hadziioannou, G. *Polymer Electronics*, Oxford Master Series in Physics; Oxford University Press: Oxford, New York, 2013.

(4) Wang, D.; Noël, V.; Piro, B. Electrolytic Gated Organic Field-Effect Transistors for Application in Biosensors—A Review. *Electronics* 2016, 5, 9.

(5) Li, G.; Zhu, R.; Yang, Y. Polymer solar cells. *Nat. Photonics* 2012, 6, 153−161.

(6) Kippelen, B.; Brédas, J.-L. Organic photovoltaics. *Energy Environ. Sci.* 2009, 2, 251−261.

(7) Zhan, C.; Yu, G.; Lu, Y.; Wang, L.; Wujcik, E.; Wei, S. Conductive polymer nanocomposites: a critical review of modern advanced devices. *J. Mater. Chem. C* 2017, 5, 1569−1585.

(8) Lee, T. D.; Ebong, A. U. A review of thin film solar cell technologies and challenges. *Renewable Sustainable Energy Rev.* 2017, 70, 1286−1297.

(9) Husain, A. A. F.; Hasan, W. Z. W.; Shafie, S.; Hamidon, M. N.; Pandey, S. S. A review of transparent solar photovoltaic technologies. *Renewable Sustainable Energy Rev.* 2018, 94, 779−791.

(10) Kayser, L. V.; Lipomi, D. J. Stretchable Conductive Polymers and Composites Based on PEDOT and PEDOT:PSS. *Adv. Mater.* 2019, 31, 1806133.

(11) Kim, N.; Kee, S.; Lee, S. H.; Lee, B. H.; Kahng, Y. H.; Jo, Y.-R.; Kim, B.-J.; Lee, K. Highly Conductive PEDOT:PSS Nanofibrils Induced by Solution-Processed Crystallization. *Adv. Mater.* 2014, 26, 2268−2272.

(12) Worfolk, B. J.; Andrews, S. C.; Park, S.; Reinspach, J.; Liu, N.; Toney, M. F.; Mannsfeld, S. C. B.; Bao, Z. Ultrahigh electrical conductivity in solution-sheared polymeric transparent films. *Proc. Natl. Acad. Sci. U.S.A.* 2015, 112, 14138−14143.

(13) Wang, Y.; Zhu, C.; Pfattner, R.; Yan, H.; Jin, L.; Chen, S.; Molina-Lopez, F.; Lissel, F.; Liu, J.; Rabiah, N. I.; Chen, Z.; Chung, J. W.; Linder, C.; Toney, M. F.; Murmann, B.; Bao, Z. A highly stretchable, transparent, and conductive polymer. *Sci. Adv.* 2017, 3, No. e1602076.

(14) Kim, G.-H.; Shao, L.; Zhang, K.; Pipe, K. P. Engineered doping of organic semiconductors for enhanced thermoelectric efficiency. *Nat. Mater.* 2013, 12, 719−723.

(15) Feig, V. R.; Tran, H.; Lee, M.; Liu, K.; Huang, Z.; Beker, L.; Mackanic, D. G.; Bao, Z. An Electrochemical Gelation Method for Patterning Conductive PEDOT:PSS Hydrogels. *Adv. Mater.* 2019, 31, No. 1902869.

(16) Rivnay, J.; Inal, S.; Collins, B. A.; Sessolo, M.; Stavrinidou, E.; Strakosas, X.; Tassone, C.; Delongchamp, D. M.; Malliaras, G. G. Structural control of mixed ionic and electronic transport in conducting polymers. *Nat. Commun.* 2016, 7, No. 11287.

(17) Spyropoulos, G. D.; Gelinas, J. N.; Khodagholy, D. Internal ion-gated organic electrochemical transistor: A building block for integrated bioelectronics. *Sci. Adv.* 2019, 5, No. eaau7378.

(18) Murphy, R. J.; Weigandt, K. M.; Uhrig, D.; Alsayed, A.; Badre, C.; Hough, L.; Muthukumar, M. Scattering Studies on Poly(3,4-ethylenedioxythiophene)-Polystyrenesulfonate in the Presence of Ionic Liquids. *Macromolecules* 2015, 48, 8989−8997.

(19) Leaf, M. A.; Muthukumar, M. Electrostatic Effect on the Solution Structure and Dynamics of PEDOT:PSS. *Macromolecules* 2016, 49, 4286−4294.

(20) Greczynski, G.; Kugler, T.; Keil, M.; Osikowicz, W.; Fahlman, M.; Salaneck, W. Photoelectron spectroscopy of thin films of PEDOT−PSS conjugated polymer blend: a mini-review and some new results. *J. Electron Spectrosc. Relat. Phenom.* 2001, 121, 1−17.

(21) Lang, U.; Müller, E.; Naujoks, N.; Dual, J. Microscopical Investigations of PEDOT:PSS Thin Films. *Adv. Funct. Mater.* 2009, 19, 1215−1220.

(22) Takano, T.; Masunaga, H.; Fujiwara, A.; Okuzaki, H.; Sasaki, T. PEDOT Nanocrystal in Highly Conductive PEDOT:PSS Polymer Films. *Macromolecules* 2012, 45, 3859−3865.

(23) Nardes, A. M.; Kemerink, M.; Janssen, R. A. J. Anisotropic hopping conduction in spin-coated PEDOT:PSS thin films. *Phys. Rev. B: Condens. Matter Mater. Phys.* 2007, 76, No. 085208.

(24) Nardes, A. M.; Janssen, R. A. J.; Kemerink, M. A Morphological Model for the Solvent-Enhanced Conductivity of PEDOT:PSS Thin Films. *Adv. Funct. Mater.* 2008, 18, 865−871.

(25) Ihnatsenka, S. Activated hopping transport in anisotropic systems at low temperatures. *Phys. Rev. B: Condens. Matter Mater. Phys.* 2016, 94, No. 195202.

(26) Zhang, J.; Seyedin, S.; Qin, S.; A. Lynch, P.; Wang, Z.; Yang, W.; Wang, X.; M. Razal, J. Fast and scalable wet-spinning of highly conductive PEDOT:PSS fibers enables versatile applications. *J. Mater. Chem. A* 2019, 7, 6401−6410.

(27) Greco, F.; Zucca, A.; Taccola, S.; Menciassi, A.; Fujie, T.; Haniuda, H.; Takeoka, S.; Dario, P.; Mattoli, V. Ultra-thin conductive free-standing PEDOT/PSS nanofilms. *Soft Matter* 2011, 7, 10642.

(28) Gholampour, N.; Brian, D.; Eslamian, M. Tailoring Characteristics of PEDOT:PSS Coated on Glass and Plastics by Ultrasonic Substrate Vibration Post Treatment. *Coatings* 2018, 8, 337.

(29) Itoh, K.; Kato, Y.; Honma, Y.; Masunaga, H.; Fujiwara, A.; Iguchi, S.; Sasaki, T. Structural Alternation Correlated to the Conductivity Enhancement of PEDOT:PSS Films by Secondary Doping. *J. Phys. Chem. C* 2019, 123, 13467−13471.

(30) Massonnet, N.; Carella, A.; Geyer, Ad.; Faure-Vincent, J.; Simonato, J.-P. Metallic behaviour of acid doped highly conductive polymers. *Chem. Sci.* 2015, 6, 412−417.

(31) Yu, Z.; Xia, Y.; Du, D.; Ouyang, J. PEDOT:PSSFilms with Metallic Conductivity through a Treatment with Common Organic Solutions of Organic Salts and Their Application as a Transparent Electrode of Polymer Solar Cells. *ACS Appl. Mater. Interfaces* 2016, 8, 11629−11638.


(32) Palumbiny, C. M.; Liu, F.; Russell, T. P.; Hexemer, A.; Wang, C.; Müller-Buschbaum, P. The Crystallization of PEDOT:PSS Polymeric Electrodes Probed In Situ during Printing. Adv. Mater. 2015, 27, 3391−3397.

(33) Jones, R. Density functional theory: Its origins, rise to prominence, and future. Rev. Mod. Phys. 2015, 87, 897−923.

(34) Dkhissi, A.; Beljonne, D.; Lazzaroni, R.; Louwet, F.; Groenendaal, B. Modeling of the solid-state packing of charged chains (PEDOT) in the presence of the counterions (TSA) and the solvent (DEG). Theor. Chem. Acc. 2008, 119, 305−312.

(35) Lenz, A.; Kariis, H.; Pohl, A.; Persson, P.; Ojamäe, L. The electronic structure and reflectivity of PEDOT:PSS from density functional theory. Chem. Phys. 2011, 384, 44−51.

(36) Casanovas, J.; Zanuy, D.; Alemán, C. Distribution of dopant ions around poly(3,4-ethylenedioxythiophene) chains: a theoretical study. Phys. Chem. Chem. Phys. 2017, 19, 9889−9899.

(37) Shi, W.; Zhao, T.; Xi, J.; Wang, D.; Shuai, Z. Unravelling Doping Effects on PEDOT at the Molecular Level: From Geometry to Thermoelectric Transport Properties. J. Am. Chem. Soc. 2015, 137, 12929−12938.

(38) Gangopadhyay, R.; Das, B.; Molla, M. R. How does PEDOT combine with PSS? Insights from structural studies. RSC Adv. 2014, 4, 43912−43920.

(39) Salzner, U.; Aydin, A. Improved Prediction of Properties of $\pi$-Conjugated Oligomers with Range-Separated Hybrid Density Functionals. J. Chem. Theory Comput. 2011, 7, 2568−2583.

(40) Chai, J.-D.; Head-Gordon, M. Systematic optimization of long-range corrected hybrid density functionals. J. Chem. Phys. 2008, 128, No. 084106.

(41) Yanai, T.; Tew, D. P.; Handy, N. C. A new hybrid exchange−correlation functional using the Coulomb-attenuating method (CAM-B3LYP). Chem. Phys. Lett. 2004, 393, 51−57.

(42) Chai, J.-D.; Head-Gordon, M. Long-range corrected hybrid density functionals with damped atom−atom dispersion corrections. Phys. Chem. Chem. Phys. 2008, 10, 6615−6620.

(43) Afzal, M. A. F.; Hachmann, J. Benchmarking DFT approaches for the calculation of polarizability inputs for refractive index predictions in organic polymers. Phys. Chem. Chem. Phys. 2019, 21, 4452−4460.

(44) Adamo, C.; Barone, V. Toward reliable density functional methods without adjustable parameters: The PBE0 model. J. Chem. Phys. 1999, 110, 6158−6170.

(45) Becke, A. D. Density-functional exchange-energy approximation with correct asymptotic behavior. Phys. A 1988, 38, 3098−3100.

(46) Oviedo, M. B.; Ilawe, N. V.; Wong, B. M. Polarizabilities of $\pi$-Conjugated Chains Revisited: Improved Results from Broken-Symmetry Range-Separated DFT and New CCSD(T) Benchmarks. J. Chem. Theory Comput. 2016, 12, 3593−3602.

(47) Jacquemin, D.; Adamo, C. Bond Length Alternation of Conjugated Oligomers: Wave Function and DFT Benchmarks. J. Chem. Theory Comput. 2011, 7, 369−376.

(48) McCormick, T. M.; Bridges, C. R.; Carrera, E. I.; DiCarmine, P. M.; Gibson, G. L.; Hollinger, J.; Kozycz, L. M.; Seferos, D. S. Conjugated Polymers: Evaluating DFT Methods for More Accurate Orbital Energy Modeling. Macromolecules 2013, 46, 3879−3886.

(49) Bloom, J. W. G.; Wheeler, S. E. Benchmark Torsional Potentials of Building Blocks for Conjugated Materials: Bifuran, Bithiophene, and Biselenophene. J. Chem. Theory Comput. 2014, 10, 3647−3655.

(50) Izgorodina, E. I.; Bernard, U. L.; MacFarlane, D. R. Ion-Pair Binding Energies of Ionic Liquids: Can DFT Compete with Ab Initio-Based Methods? J. Phys. Chem. A 2009, 113, 7064−7072.

(51) Grimme, S.; Hujo, W.; Kirchner, B. Performance of dispersion-corrected density functional theory for the interactions in ionic liquids. Phys. Chem. Chem. Phys. 2012, 14, 4875−4883.

(52) Zahn, S.; MacFarlane, D. R.; Izgorodina, E. I. Assessment of Kohn-Sham density functional theory and Møller-Plesset perturbation theory for ionic liquids. Phys. Chem. Chem. Phys. 2013, 15, 13664−13675.

(53) Lage-Estebanez, I.; Del Olmo, L.; López, R.; Garcia de la Vega, J. M. The role of errors related to DFT methods in calculations involving ion pairs of ionic liquids. J. Comput. Chem. 2017, 38, 530−540.

(54) Zhao, Y.; Truhlar, D. G. The M06 suite of density functionals for main group thermochemistry, thermochemical kinetics, noncovalent interactions, excited states, and transition elements: two new functionals and systematic testing of four M06-class functionals and 12 other functionals. Theor. Chem. Acc. 2008, 120, 215−241.

(55) Perdew, J. P.; Zunger, A. Self-interaction correction to density-functional approximations for many-electron systems. Phys. Rev. B: Condens. Matter Mater. Phys. 1981, 23, 5048−5079.

(56) Cohen, A. J.; Mori-Sánchez, P.; Yang, W. Insights into Current Limitations of Density Functional Theory. Science 2008, 321, 792−794. Publisher: American Association for the Advancement of Science Section: Special Perspectives.

(57) Hait, D.; Head-Gordon, M. Delocalization Errors in Density Functional Theory Are Essentially Quadratic in Fractional Occupation Number. J. Phys. Chem. Lett. 2018, 9, 6280−6288.

(58) Yildirim, E.; Wu, G.; Yong, X.; Tan, T. L.; Zhu, Q.; Xu, J.; Ouyang, J.; Wang, J.-S.; Yang, S.-W. A theoretical mechanistic study on electrical conductivity enhancement of DMSO treated PE-DOT:PSS. J. Mater. Chem. C 2018, 6, 5122−5131.

(59) de Izarra, A.; Park, S.; Lee, J.; Lansac, Y.; Jang, Y. H. Ionic Liquid Designed for PEDOT:PSS Conductivity Enhancement. J. Am. Chem. Soc. 2018, 140, 5375−5384.

(60) Scherlis, D. A.; Marzari, N. $\pi$-Stacking in Charged Thiophene Oligomers. J. Phys. Chem. B 2004, 108, 17791−17795.

(61) Sutton, C.; Körzdörfer, T.; Gray, M. T.; Brunsfeld, M.; Parrish, R. M.; Sherrill, C. D.; Sears, J. S.; Brédas, J.-L. Accurate description of torsion potentials in conjugated polymers using density functionals with reduced self-interaction error. J. Chem. Phys. 2014, 140, No. 054310.

(62) Zozoulenko, I.; Singh, A.; Singh, S. K.; Gueskine, V.; Crispin, X.; Berggren, M. Polarons, Bipolarons, And Absorption Spectroscopy of PEDOT. ACS Appl. Polym. Mater. 2019, 1, 83−94.

(63) Mazaheripour, A.; Majumdar, S.; Hanemann-Rawlings, D.; Thomas, E. M.; McGuiness, C.; d'Alencon, L.; Chabinyc, M. L.; Segalman, R. A. Tailoring the Seebeck Coefficient of PEDOT:PSS by Controlling Ion Stoichiometry in Ionic Liquid Additives. Chem. Mater. 2018, 30, 4816−4822.

(64) Humphrey, W.; Dalke, A.; Schulten, K. VMD: Visual molecular dynamics. J. Mol. Graphics 1996, 14, 33−38.

(65) Tol, P. Colour Schemes. SRON Technical Note, Doc. no SRON/EPS/TN/09-002, https://personal.sron.nl/~pault/data/col-ourschemes.pdf, 2018.

(66) Møller, C.; Plesset, M. S. Note on an Approximation Treatment for Many-Electron Systems. Phys. Rev. 1934, 46, 618−622.

(67) Kümmel, H. G. A biography of the coupled cluster method. Int. J. Mod. Phys. B 2003, 17, 5311−5325.

(68) Baker, J.; Scheiner, A.; Andzelm, J. Spin contamination in density functional theory. Chem. Phys. Lett. 1993, 216, 380−388.

(69) Menon, A. S.; Radom, L. Consequences of Spin Contamination in Unrestricted Calculations on Open-Shell Species: Effect of Hartree-Fock and Møller-Plesset Contributions in Hybrid and Double-Hybrid Density Functional Theory Approaches. J. Phys. Chem. A 2008, 112, 13225−13230.

(70) Goerigk, L.; Hansen, A.; Bauer, C.; Ehrlich, S.; Najibi, A.; Grimme, S. A look at the density functional theory zoo with the advanced GMTKN55 database for general main group thermochemistry, kinetics and noncovalent interactions. Phys. Chem. Chem. Phys. 2017, 19, 32184−32215.

(71) Hait, D.; Head-Gordon, M. How accurate are static polarizability predictions from density functional theory? An assessment over 132 species at equilibrium geometry. Phys. Chem. Chem. Phys. 2018, 20, 19800−19810. Publisher: The Royal Society of Chemistry.

(72) Wykes, M.; Su, N. Q.; Xu, X.; Adamo, C.; Sancho-García, J.-C. Double Hybrid Functionals and the $\pi$-System Bond Length

Alternation Challenge: Rivaling Accuracy of Post-HF Methods. J. Chem. Theory Comput. 2015, 11, 832−838.

(73) Kozuch, S.; Martin, J. M. L. DSD-PBEP86: in search of the best double-hybrid DFT with spin-component scaled MP2 and dispersion corrections. Phys. Chem. Chem. Phys. 2011, 13, 20104−20107.

(74) Kesharwani, M. K.; Brauer, B.; Martin, J. M. L. Frequency and Zero-Point Vibrational Energy Scale Factors for Double-Hybrid Density Functionals (and Other Selected Methods): Can Anharmonic Force Fields Be Avoided? J. Phys. Chem. A 2015, 119, 1701−1714.

(75) Kendall, R. A.; Dunning, T. H.; Harrison, R. J. Electron affinities of the first-row atoms revisited Systematic basis sets and wave functions. J. Chem. Phys. 1992, 96, 6796−6806.

(76) Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Petersson, G. A.; Nakatsuji, H.; Li, X.; Caricato, M.; Marenich, A. V.; Bloino, J.; Janesko, B. G.; Gomperts, R.; Mennucci, B.; Hratchian, H. P.; Ortiz, J. V.; Izmaylov, A. F.; Sonnenberg, J. L.; Williams-Young, D.; Ding, F.; Lipparini, F.; Egidi, F.; Goings, J.; Peng, B.; Petrone, A.; Henderson, T.; Ranasinghe, D.; Zakrzewski, V. G.; Gao, J.; Rega, N.; Zheng, G.; Liang, W.; Hada, M.; Ehara, M.; Toyota, K.; Fukuda, R.; Hasegawa, J.; Ishida, M.; Nakajima, T.; Honda, Y.; Kitao, O.; Nakai, H.; Vreven, T.; Throssell, K.; Montgomery, J. A., Jr.; Peralta, J. E.; Ogliaro, F.; Bearpark, M. J.; Heyd, J. J.; Brothers, E. N.; Kudin, K. N.; Staroverov, V. N.; Keith, T. A.; Kobayashi, R.; Normand, J.; Raghavachari, K.; Rendell, A. P.; Burant, J. C.; Iyengar, S. S.; Tomasi, J.; Cossi, M.; Millam, J. M.; Klene, M.; Adamo, C.; Cammi, R.; Ochterski, J. W.; Martin, R. L.; Morokuma, K.; Farkas, O.; Foresman, J. B.; Fox, D. J. Gaussian 16, Revision C.01; Gaussian Inc.: Wallingford CT, 2016.

(77) Parrish, R. M.; Burns, L. A.; Smith, D. G. A.; Simonett, A. C.; DePrince, A. E.; Hohenstein, E. G.; Bozkaya, U.; Sokolov, A. Y.; DiRemigio, R.; Richard, R. M.; Gonthier, J. F.; James, A. M.; McAlexander, H. R.; Kumar, A.; Saitow, M.; Wang, X.; Pritchard, B. P.; Verma, P.; Schaefer, H. F.; Patkowski, K.; King, R. A.; Valeev, E. F.; Evangelista, F. A.; Turney, J. M.; Crawford, T. D.; Sherrill, C. D. Psi4 1.1: An Open-Source Electronic Structure Program Emphasizing Automation, Advanced Libraries, and Interoperability. J. Chem. Theory Comput. 2017, 13, 3185−3197.

(78) Boys, S. F.; Bernardi, F. The calculation of small molecular interactions by the differences of separate total energies. Some procedures with reduced errors. Mol. Phys. 1970, 19, 553−566. Publisher: Taylor & Francis _eprint: https://doi.org/10.1080/00268977000101561.

(79) Brauer, B.; Kesharwani, M. K.; Martin, J. M. L. Some Observations on Counterpoise Corrections for Explicitly Correlated Calculations on Noncovalent Interactions. J. Chem. Theory Comput. 2014, 10, 3791−3799.

(80) Sherrill, C. D.; Takatani, T.; Hohenstein, E. G. An Assessment of Theoretical Methods for Nonbonded Interactions: Comparison to Complete Basis Set Limit Coupled-Cluster Potential Energy Curves for the Benzene Dimer, the Methane Dimer, Benzene-Methane, and Benzene-H2S. J. Phys. Chem. A 2009, 113, 10146−10159.

(81) Mentel, L. M.; Baerends, E. J. Can the Counterpoise Correction for Basis Set Superposition Effect Be Justified? J. Chem. Theory Comput. 2014, 10, 252−267.

(82) Sun, H.; Autschbach, J. Electronic Energy Gaps for $\pi$-Conjugated Oligomers and Polymers Calculated with Density Functional Theory. J. Chem. Theory Comput. 2014, 10, 1035−1047.

(83) Becke, A. D. Density-functional thermochemistry. V. Systematic optimization of exchange-correlation functionals. J. Chem. Phys. 1997, 107, 8554−8560.

(84) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J. Chem. Phys. 2010, 132, No. 154104.

(85) Zhao, Y.; Truhlar, D. G. A new local density functional for main-group thermochemistry, transition metal bonding, thermochemical kinetics, and noncovalent interactions. J. Chem. Phys. 2006, 125, No. 194101.

(86) Austin, A.; Petersson, G. A.; Frisch, M. J.; Dobek, F. J.; Scalmani, G.; Throssell, K. A Density Functional with Spherical Atom Dispersion Terms. J. Chem. Theory Comput. 2012, 8, 4989−5007.

(87) Heyd, J.; Scuseria, G. E. Efficient hybrid density functional calculations in solids: Assessment of the Heyd−Scuseria−Ernzerhof screened Coulomb hybrid functional. J. Chem. Phys. 2004, 121, 1187−1192.

(88) Krukau, A. V.; Vydrov, O. A.; Izmaylov, A. F.; Scuseria, G. E. Influence of the exchange screening parameter on the performance of screened hybrid functionals. J. Chem. Phys. 2006, 125, No. 224106.

(89) Henderson, T. M.; Izmaylov, A. F.; Scalmani, G.; Scuseria, G. E. Can short-range hybrids describe long-range-dependent properties? J. Chem. Phys. 2009, 131, No. 044108.

(90) Yu, H. S.; He, X.; Li, S. L.; Truhlar, D. G. MN15: A Kohn−Sham global-hybrid exchange−correlation density functional with broad accuracy for multi-reference and single-reference systems and noncovalent interactions. Chem. Sci. 2016, 7, 5032−5051.

(91) Lee, C.; Yang, W.; Parr, R. G. Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. Phys. Rev. B: Condens. Matter Mater. Phys. 1988, 37, 785−789.

(92) Iikura, H.; Tsuneda, T.; Yanai, T.; Hirao, K. A long-range correction scheme for generalized-gradient-approximation exchange functionals. J. Chem. Phys. 2001, 115, 3540−3544.

(93) Vydrov, O. A.; Scuseria, G. E. Assessment of a long-range corrected hybrid functional. J. Chem. Phys. 2006, 125, No. 234109.

(94) Papajak, E.; Zheng, J.; Xu, X.; Leverentz, H. R.; Truhlar, D. G. Perspectives on Basis Sets Beautiful: Seasonal Plantings of Diffuse Basis Functions. J. Chem. Theory Comput. 2011, 7, 3027−3034.

(95) Autschbach, J.; Srebro, M. Delocalization Error and "Functional Tuning" in Kohn-Sham Calculations of Molecular Properties. Acc. Chem. Res. 2014, 47, 2592−2602.

(96) Brédas, J. L. Relationship between band gap and bond length alternation in organic conjugated polymers. J. Chem. Phys. 1985, 82, 3808−3811.

(97) Yang, S.; Kertesz, M. Bond Length Alternation and Energy Band Gap of Polyyne. J. Phys. Chem. A 2006, 110, 9771−9774.

(98) Löwdin, P.-O. Quantum Theory of Many-Particle Systems. III. Extension of the Hartree-Fock Scheme to Include Degenerate Systems and Correlation Effects. Phys. Rev. 1955, 97, 1509−1520.

(99) Shao, N.; Wu, Q. Charge self-localization in $\pi$-conjugated polymers by long range corrected hybrid functionals. Phys. Chem. Chem. Phys. 2014, 16, 6700−6708.

(100) Cremer, D. Density functional theory: coverage of dynamic and non-dynamic electron correlation effects. Mol. Phys. 2001, 99, 1899−1940. Publisher: Taylor & Francis _eprint: https://doi.org/10.1080/00268970110083564.

(101) Jankowski, K.; Nowakowski, K.; Grabowski, I.; Wasilewski, J. Coverage of dynamic correlation effects by density functional theory functionals: Density-based analysis for neon. J. Chem. Phys. 2009, 130, No. 164102.

(102) Li, C.; Yang, W. On the piecewise convex or concave nature of ground state energy as a function of fractional number of electrons for approximate density functionals. J. Chem. Phys. 2017, 146, No. 074107. Publisher: American Institute of Physics.

(103) Körzdörfer, T.; Parrish, R. M.; Sears, J. S.; Sherrill, C. D.; Brédas, J.-L. On the relationship between bond-length alternation and many-electron self-interaction error. J. Chem. Phys. 2012, 137, No. 124305.

(104) Körzdörfer, T.; Brédas, J.-L. Organic Electronic Materials: Recent Advances in the DFT Description of the Ground and Excited States Using Tuned Range-Separated Hybrid Functionals. Acc. Chem. Res. 2014, 47, 3284−3291.

(105) Kronik, L.; Stein, T.; Refaely-Abramson, S.; Baer, R. Excitation Gaps of Finite-Sized Systems from Optimally Tuned Range-Separated Hybrid Functionals. J. Chem. Theory Comput. 2012, 8, 1515−1531.

(106) Körzdörfer, T.; Sears, J. S.; Sutton, C.; Brédas, J.-L. Long-range corrected hybrid functionals for $\pi$-conjugated systems: Dependence of the range-separation parameter on conjugation length. J. Chem. Phys. 2011, 135, No. 204107.

(107) Paulsen, B. D.; Wu, R.; Takacs, C. J.; Steinrück, H.-G.; Strzalka, J.; Zhang, Q.; Toney, M. F.; Rivnay, J. Time-Resolved Structural Kinetics of an Organic Mixed Ionic-Electronic Conductor. Adv. Mater. 2020, 32, No. 2003404.

(108) Winter, A. H.; Falvey, D. E. Vinyl Cations Substituted with $\beta \pi$-Donors Have Triplet Ground States. J. Am. Chem. Soc. 2010, 132, 215−222.

(109) Reiher, M.; Salomon, O.; Artur Hess, B. Reparameterization of hybrid functionals based on energy differences of states of different multiplicity. Theor. Chem. Acc. 2001, 107, 48−S5.

(110) Bombile, J. H.; Janik, M. J.; Milner, S. T. Polaron formation mechanisms in conjugated polymers. Phys. Chem. Chem. Phys. 2018, 20, 317−331.