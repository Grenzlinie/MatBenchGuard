![](./images/812703813310873600_1.jpg)

Subscriber access provided by Uppsala universitetsbibliotek

Article

# Carbonylation of Dimethyl Ether to Methyl Acetate over SSZ-13

Marcella Lusardi, Thomas T. Chen, Matthew James Kale,
Jong Hun Kang, Matthew Neurock, and Mark E Davis

ACS Catal., Just Accepted Manuscript • DOI: 10.1021/acscatal.9b04307 • Publication Date (Web): 06 Dec 2019

Downloaded from pubs.acs.org on December 6, 2019

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Carbonylation of Dimethyl Ether to Methyl Acetate over SSZ-13

Marcella Lusardi,† Thomas T. Chen,‡ Matthew Kale, †,‡ Jong Hun Kang, † Matt Neurock,‡
Mark E. Davis†, *

†Chemical Engineering, California Institute of Technology, Pasadena, CA 91125 United States

‡Chemical Engineering and Materials Science, University of Minnesota, Minneapolis, MN 55455 United States

ABSTRACT: The small pore zeolite with the chabazite framework topology, SSZ-13, is found to be an active catalyst in the carbonylation of dimethyl ether (DME) to methyl acetate (MA). The production of MA over SSZ-13 after 24 hours on stream at 165 °C and 1 bar approaches that obtained from mordenite and is significantly higher than from ferrierite at comparable Si/Al of ca. 10. To understand the origin of the activity, SSZ-13

materials are synthesized with variable Si/Al, characterized via several techniques including multinuclear MAS NMR spectroscopy, and evaluated for their carbonylation activity. While MA production rates increase with decreasing Si/Al, the correlation is non-linear due to the effect of Si/Al on the acid site distribution within different confining environments, and the associated impact of the latter on the rate-determining transition state barrier. Enhanced MA production rates trend with acid sites located at the eight-membered ring (8MR) that are increasingly populated as framework Al content increases.

Density functional theory (DFT) analyses of transition state energies as a function of active site location support the experimental findings, where the lowest apparent barriers are associated with the methoxy groups that orient within the plane of the 8MR window.

This is due to an optimal charge stabilization of the cationic transition states with the negatively charged oxygens within the 8MR window. The effects of catalyst chemical composition, separate from framework topology, are also investigated using SAPO-34 (the silicoaluminophosphate analog of SSZ-13). Analyses of the $^1$H MAS NMR signals and carbonylation activity suggest that the higher acid site strength of SSZ-13 compared

to that of the SAPO is required for effective Brønsted acid catalysis of Koch-type carbonylation pathways.

KEYWORDS: Chabazite, carbonylation, acetic acid, confinement, small-pore zeolite

## 1 Introduction

Methanol carbonylation is an industrially important route for the production of acetic acid, an intermediate in the synthesis of various polymers, pharmaceuticals, and textiles.¹⁻⁴ The commercial process for acetic acid production is catalyzed by Rh/Ir-organometallic complexes and iodide promoters. Solid acid-mediated, Koch-type reactions provide a transition metal- and halide-free carbonylation pathway that removes significant economic and environmental drawbacks associated with the commercial catalytic system.⁵ With this mechanism, there is an induction period during which methyl groups from methanol and/or dimethyl ether (DME) adsorb at the proton site to form methoxy groups. DME is a preferred substrate to methanol since the latter generates water as a by-product, resulting in inhibition of carbonylation steps.⁶ During the steady-

state catalytic cycle, CO executes a rate-determining nucleophilic attack onto the methoxy group, yielding an acetyl intermediate. Finally, methanol and/or DME reacts with the acetyl to form methyl acetate (MA), a precursor to acetic acid, and regenerate the surface-bound methyl group.

Various solid acids have been investigated for this chemistry, including heteropolyacids,⁷⁸ Brønsted acid zeolites,⁵⁹¹⁰ and sulfated zirconia.¹¹¹² Certain zeolite topologies have shown promising MA production activity due to the positive effect of microporous confinement on the rate-determining step (RDS). Most notably, mordenite (MOR—each unique topology is given a three-letter code by the International Zeolites Association¹³) and ferrierite (FER) exhibit superior carbonylation reactivity within their 8-member rings (8MRs).¹⁴⁻¹⁶ Theoretical analyses show that the cationic linear transition state $[\text{O—C—CH}_3]^*$ is effectively stabilized by the surrounding anionic oxygens within the 8MR cage of MOR, which decreases the rate-determining activation barrier, thus resulting in enhanced MA production rates.⁹¹⁷ In contrast, carbonylation rates in the larger pores of MOR (12MR) and FER (10MR) are significantly lower, as are those from other zeolites with medium- and large-pore topologies (FAU, MFI, BEA).⁵¹⁸

Zeolites (aluminosilicate molecular sieves) and zeo-type materials have vast ranges of pore size, shape, and interconnectivity, giving rise to over 200 unique framework structures with different confining environments.¹⁹ Zeolite topologies beyond the common types mentioned above (MOR, FER) have been investigated for carbonylation activity, including ETL (EU-12), PAU (ECR-18), OFF (offretite), and CHA (chabazite).²⁰,²¹ CHA is particularly interesting because, unlike these other frameworks, it is commercially available as SSZ-13 (aluminosilicate CHA with Si/Al > 5). SSZ-13 is manufactured as a catalyst for the selective reduction of NOₓ emissions in automotive exhaust.²²,²³ It is also found as the aluminosilicate mineral chabazite (Si/Al < 5). CHA has a 3-dimensional, small-pore, cage-containing framework composed of double 6MRs (D6MRs) that interconnect to form 4-, 6-, and 8-member rings. These 8MRs (3.8 x 3.8 Å) are the sole conduit for molecular transport and provide access to the ellipsoid CHA cage (12 Å x 7 Å).²⁴ To the best of our knowledge, there is only one reference for the carbonylation activity of CHA, reported as MA yields measured at two temperatures (US Patent 7,465,822 B2).²¹ No discussion or further analysis of the activity in CHA was provided, and only a single CHA sample was evaluated (despite its promising MA yield that was

40% of that for MOR at comparable Si/Al; T = 180 °C). The carbonylation activity in CHA is particularly interesting given its starkly different structure compared to that of MOR and FER (2-dimensional, large-/medium-pore, channel structures). The significantly different topology, along with the commercial availability of SSZ-13, motivated our investigation of the behavior of CHA-type zeolite catalysts for the carbonylation of DME to MA.

In order to understand the origin of activity in CHA-type zeolites, we synthesized SSZ-13 materials with variable Si/Al. The framework Si/Al not only impacts the density of Brønsted acid sites (and, commensurately, the density of the surface-bound methyl groups that replace them during the induction period), but also the distribution of those methoxys within different confining environments.²⁵ In this way, we systematically alter the number density of the framework positions where the transition state can form during the RDS, and determine the impact on the MA production activity. These studies facilitate the identification of the most reactive methoxy group—the one located at the 8MR window—for DME carbonylation to MA in CHA-type zeolites. This result is supported by complementary DFT analyses that calculate the intrinsic activation barriers for the rate-determining nucleophilic attack by CO as a function of methoxy location in the CHA

framework. We also evaluate the reactivity of a molecular sieve with the CHA topology, but a different chemical composition (SAPO-34). This analysis decouples the effects of confinement and acid site strength to elucidate further the catalyst requirements for Koch-type carbonylation routes.

## 2 Materials and Methods

We obtained commercial mordenite (CBV 21A, Si/Al = 10) and ferrierite (CP914C, Si/Al =10) from Zeolyst for comparison to our synthesized SSZ-13 samples.

### 2.1 Synthesis of CHA-type materials

**SSZ-13s**

CHA-type zeolites with Si/Al > 5 (SSZ-13s) were prepared from a gel with the molar composition $1\ \mathrm{SiO_2}{:}x\ \mathrm{Al_2O_3}{:}0.2\ \mathrm{SDAOH}{:}0.2\ \mathrm{NaOH}{:}40\ \mathrm{H_2O}.^{26}$ The alumina content, $x$, was varied from 0.014 to 0.062. Fumed silica (Cab-O-Sil M5, Cabot), aluminum hydroxide (Reheiss F2000), and trimethyl adamantylammonium hydroxide (25 wt.% in $\mathrm{H_2O}$, Sachem) were used as the silica source, alumina source, and structure-directing agent (SDA), respectively. In a typical synthesis, 20 wt.% sodium hydroxide solution, deionized (DI) water, and the SDA were added to a PTFE liner. The alumina source was then added

and stirred. After 30 min, the silica source was added, and the solution was stirred overnight. The gel was crystallized at 160 °C and 60 rpm for approximately 10 days.

Samples were recovered by centrifugation, washed 3 times in DI H₂O and 1 time in acetone, and dried overnight at 100 °C. The as-synthesized materials were then calcined in flowing breathing-grade air to remove the SDA by combustion at a 1 °C/min ramp to 150 °C, 3 hr hold at 150 °C, 1 °C/min ramp to 580 °C, 6 hr hold at 580 °C. The calcined SSZ-13s underwent an ammonium exchange to replace Na⁺ with NH₄⁺ as the charge- balancing cation. In this procedure, 1 g of material was stirred in 100 mL of 1 $M$NH₄NO₃ solution at 80 °C for approximately 8 hr. This was repeated 3 times, and the ammonium- exchanged sample was washed and dried following the same procedure above.

SAPO-34

The silicoaluminophosphate material with the CHA framework, SAPO-34, was synthesized from a gel with molar composition 0.08 SiO₂:0.2 Al₂O₃:0.2 P₂O5:0.4 TEAOH:9.8 H₂O.²⁷ Colloidal silica (Ludox AS-30), aluminum isopropoxide, and phosphoric acid (85 wt.%) were used as the sources for silicon, aluminum, and phosphorous, respectively. Tetraethylammonium hydroxide (TEAOH, 35 wt.%) was used

as the SDA. In this procedure, the following materials were added followed by mixing time in parentheses: SDA and 40% of the required water (0.5 hr); aluminum source (overnight); silicon source (4 hr); 60% of the required water (1 hr); phosphoric acid (overnight). The gel was then crystallized statically at 200 °C for 48 hr. The standard centrifugation, washing and drying procedure was used. The dried as-synthesized material was subjected to the same calcination program used to combust the SDA in the SSZ-13s to remove TEAOH and obtain the $H^+$-form.

### 2.2 Characterization

Powder x-ray diffraction (PXRD) patterns were obtained on a Rigaku MiniFlex II instrument using Cu Kalpha radiation ($\lambda$ = 1.54 Å) and a scan rate of 0.3°/min. All solid-state, magic-angle spinning nuclear magnetic resonance (MAS NMR) spectroscopy experiments were conducted on a Bruker 500 MHz spectrometer using a 4 mm $ZrO_2$ rotor.

$^{29}$Si MAS NMR spectra were acquired at 99.3 MHz with $^1$H decoupling and a spinning rate of 8 kHz using a 90° pulse length of 4 μs and a cycle delay time of 60 s. For the zeolites (SSZ-13s), 128 scans were collected on the $NH_4^+$-form and the spectra were deconvoluted using the DMFit software to calculate the framework Si/Al values. For

SAPO-34, 960 scans were collected on the calcined (H⁺-form) sample. ²⁷Al MAS NMR spectra were acquired on the H⁺-form samples after dehydration at 130.2 MHz, a spin rate of 10 kHz, a 90° pulse length of 0.5 μs, and a cycle delay time of 3 s for the zeolite (2000 scans) and 2 s for SAPO (128 scans) samples. Particle morphology and bulk elemental analysis were investigated using a Zeiss 1550VP field-emission scanning electron microscope (SEM) equipped with an Oxford X-Max SDD energy dispersive spectrometer (EDS).

The number of Brønsted acid sites was measured using quantitative ¹H MAS NMR spectroscopy. In a typical experiment, the freshly calcined samples (H⁺-form) were dehydrated under vacuum (10⁻² torr) at 400 °C for 12 hr in a dehydration manifold. The sample was transferred under Ar into a glove box for air- and moisture-free packing of the NMR rotor (4 mm, ZrO₂) and loaded into the Bruker 500 MHz spectrometer. Spectra were collected at 500.1 MHz and a spinning rate of 13 kHz using a 90° high power pulse length of 4 μs, a 15 s cycle delay time, and 16 scans. Signal intensities were referenced to hexamethylbenzene and normalized by the mass packed into the rotor for quantification. The spectra were deconvoluted using DMFit.

### 2.3 DME Carbonylation experiments

The DME carbonylation activity of the CHA-type zeolite catalysts was evaluated in a fixed bed reactor (8 mm ID). All reactions were conducted at 165 °C and 1 bar. The catalyst particles were sized between 150 and 600 µm and 150 mg was packed onto a bed of quartz wool. The catalyst bed was pretreated *in-situ* in flowing breathing-grade air at 2 °C/min to 550 °C, and subsequently held at 550 °C for 6 hr to convert the sample to the H⁺-form and/or remove surface adsorbates. After cooling to the reaction temperature, reagents were introduced at 75 sccm total flowrate (2% DME, 3% He with Ar (5%), 95% CO). The reactor effluent line was heated to prevent condensation of species and samples were measured by an online gas chromatograph (GC, Agilent 7890A) paired with a flame ionization detector (FID).

### 2.4 Computational methods

The adsorption, reaction, and activation energies for the different proposed elementary steps in DME carbonylation were calculated at different sites within CHA and MOR using periodic plane-wave density functional theory (DFT) calculations as implemented in the Vienna Ab initio Simulation Program (VASP). Gradient corrections were calculated using

the Perdew-Burke-Erzenhof (PBE) exchange-correlation functional²⁸ and the core electrons were described using projector augmented wave (PAW) based pseudo- potentials.²⁹ The valence electrons were represented by a plane-wave basis set with an energy cutoff of 400 eV. A (1 × 1 × 1) k-point mesh at the single Γ-point was used to sample the Brillouin zone due to the large size of the CHA unit cell and breaking of symmetry associated with Al framework substitution. The Grimme-type D3 corrections with Becke-Johnson (BJ) damping were used to account for dispersive interactions of adsorbates with the zeolite framework.³⁰,³¹

The self-consistent field (SCF) and geometry optimization calculations were converged to 10⁻⁶ eV and 0.05 eV/Å, respectively. The reaction path between the reactant and product states was calculated using the climbing image nudged elastic band (CI-NEB) method³²,³³ to a force tolerance of 0.3 eV/Å. The transition states of the different paths were subsequently refined using the dimer method to a force convergence of 0.05 eV/Å.³⁴ Stricter convergence criteria for the SCF with energies converged to 10⁻⁸ - 10⁻⁶ eV and geometry optimization with forces converged to 0.01 - 0.05 eV/Å were tested and found to change the reaction energy and the intrinsic activation energy for CO addition to CH₃

in CHA by less than 2 kJ mol⁻¹, suggesting that the original convergence criteria is sufficient for this study. Small perturbations of the transition state toward the reactant and product followed by optimization resulted in the formation of the reactant and the product, respectively, thus confirming the transition state and the reaction coordinate. Harmonic frequency calculations and partial Hessian vibrational analysis were performed to determine the zero point vibrational energies, vibrational enthalpies, and vibrational free energies that were subsequently used to calculate the enthalpies, entropies, and free energies for the reactant, product, and transition state structures. Further details regarding the computational methods are included in the SI.

For this analysis, the SSZ-13 (CHA framework type) structure was constructed from the Materials Studio® structural library from Dassault Systemes with unit cell Si₁₂O₂₄ and lattice parameters a = b = c = 9.421 Å and α = β = γ = 94.200°.³⁵ The CHA topology is a high symmetry framework containing a single unique T site and four crystallographically-distinct O sites. The previously established O site nomenclature³⁶ relates to each O site's association to different rings of the framework: O1 site connects two 4MRs and one 8MR; O2 site connects one 4MR, one 6MR, and one 8MR; O3 site connects two 4MRs and one

6MR; and O4 site connects one 4MR and two 8MRs. The CHA zeolite was modeled with
a $2 \times 2 \times 2$ supercell of 288 atoms with a single Al atom substituted at the sole T site of
CHA at the 8MR windows connecting the larger cages (Si/Al = 95). The substituted Al site
was balanced by a hydrogen atom to create a Brønsted acid site.

## 3 Results and Discussion

### 3.1 Physicochemical characterizations

The PXRD patterns for the as-synthesized zeolites are illustrated in Figure 1a. All
samples show features attributed to a single, CHA phase. $^{29}$Si MAS NMR spectra (Figure
1b) for the SSZ-13s show primary resonances at -111, -105, and -101 ppm,
corresponding to Q4 $((Si-O)_4$-Si; Si(0Al)), Q3 $((Si-O)_3$-Si-(O-Al); Si(1Al)) and Q3 $((Si-O)_3$-
Si-OH; Si(0Al)) sites, respectively.$^{22}$ As the gel Si/Al decreases (i.e., increasing Al
content), the resonance at -101 ppm shifts towards -100 ppm due to increased
contributions from Q2 sites $((Si-O)_2$-Si-(O-Al)$_2$; Si(2Al)) that manifest at -99 ppm.

Deconvolution of the spectra enabled the calculation of the framework Si/Al values (Table

1).$^{37}$ An example of the deconvolution is shown in Figure S1. Bulk Si/Al values measured by SEM-EDS were within 15% of the framework Si/Al values.

![](./images/812703813310873600_2.jpg)

Figure 1. Characterizations of SSZ-13s. (a) PXRD patterns for as-synthesized SSZ-13s. (b) $^{29}$Si MAS NMR spectra for SSZ-13s (NH₄⁺-form).

Table 1. SSZ-13 characterization data.

<table>
  <thead>
    <tr>
      <th>Sample</th>
      <th>$x$ Al₂O₃$^{\text{a}}$<br>(mol/mol SiO₂)</th>
      <th>Framework Si/Al$^{\text{b}}$</th>
      <th>Bulk Si/Al$^{\text{c}}$</th>
      <th>Brønsted acid site density (mmol g⁻¹)$^{\text{d}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SSZ-13 (9)</td>
      <td>0.062</td>
      <td>9.2</td>
      <td>9.8</td>
      <td>1.55</td>
    </tr>
    <tr>
      <td>SSZ-13 (13)</td>
      <td>0.042</td>
      <td>12.9</td>
      <td>11.6</td>
      <td>1.08</td>
    </tr>
  </tbody>
</table>

<table>
  <tr>
    <td>SSZ-13
(15)</td>
    <td>0.035</td>
    <td>14.9</td>
    <td>13.9</td>
    <td>0.95</td>
  </tr>
  <tr>
    <td>SSZ-13
(19)</td>
    <td>0.026</td>
    <td>18.8</td>
    <td>17.0</td>
    <td>0.73</td>
  </tr>
  <tr>
    <td>SSZ-13
(22)</td>
    <td>0.025</td>
    <td>21.5</td>
    <td>18.7</td>
    <td>0.52</td>
  </tr>
  <tr>
    <td>SSZ-13
(30)</td>
    <td>0.016</td>
    <td>29.9</td>
    <td>29.3</td>
    <td>n. q.</td>
  </tr>
  <tr>
    <td>SSZ-13
(35)</td>
    <td>0.014</td>
    <td>35.3</td>
    <td>33.3</td>
    <td>n. q.</td>
  </tr>
</table>

ᵃcontent in synthesis gel

ᵇmeasured by ²⁹Si MAS NMR spectroscopy

ᶜmeasured by SEM-EDS

ᵈmeasured by ¹H MAS NMR spectroscopy and referenced to hexamethylbenzene

n.q.: not quantified since 4 ppm signal intensities for these samples are too low for accurate quantification

![](./images/812703813310873600_3.jpg)

Figure 2. $^{27}$Al MAS NMR spectra for SSZ-13s (dehydrated H⁺-form).

$^{27}$Al NMR spectra on selected SSZ-13 samples (Figure 2) show a strong resonance centered at 58 ppm corresponding to tetrahedrally-coordinated Al in the zeolite framework and a weaker peak near 0 ppm, indicative of extraframework Al. SEM images of the zeolites show particles with a cube-like morphology (Figure S2) typical of chabazite and diameters between 2 and 5 μm (Table S1).

3.2 Bronsted acid site characterization: $^1$H MAS NMR spectroscopy

The $^1$H MAS NMR spectra measured on the dehydrated SSZ-13s are reported in Figure 3a. An example deconvolution through DMFit is presented in Figure S3. The spectra show a resonance near 1.8 ppm that corresponds to protons in silanols (Si-OH).$^{38,39}$ Resonances for protons in aluminum-rich (e.g., extraframework Al) environments arise between 2 and 3.5 ppm.$^{39}$ Near 4 ppm, the signal manifests from bridging hydroxyl groups that form from Al incorporation into the framework.$^{39,40}$ The integration of this resonance gives the total Brønsted acid site density (Table 1), which linearly scales with framework Al content (Figure 3b). Since the signals at 4 ppm for samples SSZ-13 (30) and SSZ-13 (35) are very weak (Figure 3a), accurately fitting these spectra is difficult. As a result, Brønsted acid site densities for these samples are not reported.

![](./images/812703813310873600_4.jpg)

![](./images/812703813310873600_5.jpg)

Figure 3. Brønsted acid site characterizations. (a) ¹H MAS NMR spectra for dehydrated SSZ-13s (H⁺-form). (b) Total Brønsted acid site density measured as a function of framework Si/Al for the SSZ-13s.

3.3 DME carbonylation activity in CHA-type zeolites

### 3.3.1 MOR, FER, CHA comparison

The DME carbonylation activity for MOR, FER, and CHA frameworks at similar Si/Al (~10) is reported in Figure 4a. MOR is the most active at early time on stream, but the MA production rate decays by more than a factor of 2 over time. The activity loss in MOR is attributed to deactivation—while the 8MRs are extremely selective (>99%) to MA, hydrocarbon formation mechanisms within the 12MRs of MOR are more kinetically favored compared to carbonylation routes, thus allowing the formation of carbonaceous deposits that restrict transport and cause the catalyst to deactivate.⁹,¹⁰,¹⁴ This result is consistent with the weight loss in the TGA profiles for the spent catalysts between 300 and 650 °C (Figure S4) that shows that MOR produces more coke-like deposits (2 to 3x, Table S2) than the other frameworks. The relatively smaller 10MR channels in FER inhibit excessive formation of these deposits, resulting in a stable MA production rate over time on stream for this catalyst (Figure 4a).¹⁰,⁴¹ However, the maximum rate of MA production over FER is an order of magnitude less than that over MOR, despite the fact that the carbonylation activity in both topologies is attributed to their 8MRs. The enhanced rate in

MOR is attributed to the specific dimensions of its 8MRs, specific sites within the 8MR, and the preferred orientation of the linear transition state within the small pores and side pockets.¹⁷ Interestingly, the carbonylation reactivity over CHA ranks intermediate between that of MOR and FER, thereby surpassing FER as the second-most active zeolite framework for carbonylation reported in the literature.⁵,⁹,¹⁵,¹⁸,⁴² After 24 hr on stream, the total MA produced over CHA is within 12% of that produced over MOR (Figure 4b).

![](./images/812703813310873600_6.jpg)

![](./images/812703813310873600_7.jpg)

Figure 4. DME carbonylation results. (a) Methyl acetate production rates measured over time for MOR (open triangles), FER (open circles), and CHA (filled squares) frameworks.

(b) Total methyl acetate produced after 24 hr on stream over each framework.

The carbonylation activity in the CHA-type framework is interesting, particularly because its framework is so different from those of the other zeolite carbonylation catalysts (MOR,

FER). Given its slower deactivation rate compared to MOR, and its commercial availability, CHA-type zeolites (SSZ-13s) merit further investigation.

### 3.3.2 CHA: activity vs Si/Al

The kinetics of MA production in MOR (and to a smaller degree, FER) have been extensively investigated, and the locations of the Brønsted acid sites that give rise to the very high selectivity within the framework have been specifically identified.5,9,14,15,17,42–44

To elucidate the origin of activity in the CHA topology, we investigated the MA production rates in SSZ-13s at varied Si/Al ($9 \leq \text{Si/Al} \leq 35$). The activities of these materials are summarized in Figure 5.

![](./images/812703813310873600_8.jpg)

Figure 5. MA production rates as a function of time for the SSZ-13s. Samples with overlapping activity correspond to SSZ-13 (19)/SSZ-13 (22); and SSZ-13(30)/SSZ-13(35).

On a per gram basis, the MA production rates increase with decreasing Si/Al. This general trend is expected given that the surface coverage of methyl groups has shown to reach saturation ($\text{DME}_{\text{adsorbed}} / \text{Al}_{\text{framework}} = 0.5$) for various topologies.$^{5}$ Thus, decreasing Si/Al (i.e., increasing Brønsted acid site density) would result in larger methoxy surface coverages, enhancing the probability of nucleophilic attack by CO. We prepared a sample with low Si/Al (2.6) using a recipe previously reported in our group$^{45}$ to investigate the activity at low Si/Al. However, we were not able to maintain structural integrity of the sample at reaction conditions. This is a common challenge with Al-rich zeolites in their acid forms.

If all Brønsted acid sites are equally reactive for carbonylation, the MA production would increase linearly with decreasing framework Si/Al (increasing Brønsted acid site density—see Figure 3b). However, we find this not to be the case. Figure 6 shows the non-linear

correlation between the maximum rates of MA production and framework Si/Al. These rates plotted as a function of total Brønsted acid site density are reported below.

![](./images/812703813310873600_9.jpg)

Figure 6. Maximum rates of MA production measured over the SSZ-13s as a function of Si/Al.

Framework Si/Al, among other factors (e.g., the presence or absence of Na⁺ during the synthesis)²²,⁴⁶ strongly influences the distribution (i.e., siting, density) of cations required to compensate the negative charge in the lattice generated by Al³⁺/Si⁴⁺ substitution.²⁵,⁴⁷⁻⁴⁹ Monovalent cation distribution, in turn, dictates the distribution of methoxy groups in the framework. We postulate that the non-linearity in these rates as a function of Si/Al

originates from the sensitive relationship between MA rates and methoxy location, as evidenced by prior experimental and computational work in MOR. $^{6,9,17,43}$ This relationship arises from the stabilization (or lack thereof) via confinement of the transition state formed by CO attack on the methoxy group, which decreases (or increases) the activation barrier of the RDS. There are three primary positions for monovalent, extraframework cations to site in SSZ-13 (Figure 7) associated with the crystallographically-distinct O atoms. $^{25,47,49}$ Cations in site SI nest in the D6MR, in site SII sit above the plane of the 6MR, and in site SIII' orient at the 8MR. While small cations (e.g., $H^{+}$) can fit in the D6MR, it is not considered an active center because it is inaccessible by the gas-phase reactants involved in the carbonylation reaction. This leaves sites SII and SIII' as candidates for methoxy positions in the SSZ-13 catalysts.

![](./images/812703813310873600_10.jpg)

Figure 7. Monovalent cation locations in CHA: site SI (sphere, in D6MR); site SII (cube, above 6MR into cage); site SIII' (triangular prism, at 8MR).

Prior work²⁵ using ²³Na multiple quantum MAS NMR spectroscopy and DFT calculations has shown that site SII is preferentially occupied at higher Si/Al in SSZ-13 materials. As framework Al content increases, site SIII' becomes increasingly populated as more than one Al per cage cannot be avoided. As Al content increases further, occupation in Site SI becomes apparent. These trends in the site distribution when considered in conjunction with measured MA production rates as a function of Si/Al are suggestive that active sites located at SII are less kinetically favorable for DME carbonylation than those at SIII'. This, in turn, would lead to the fact that CO attack on a methoxy group at the 8MR (window or cage) gives a lower transition state barrier compared to those at the 6MR (cage).

3.3.3 DFT analysis of rate-determining transition state barriers in SSZ-13

The activation enthalpies, activation free energies, and the overall reaction energies for the different elementary steps in the carbonylation of DME to methyl acetate at the four crystallographically-distinct O sites (Figure 8) in SSZ-13 were calculated using DFT.

![](./images/812703813310873600_11.jpg)

Figure 8. $2 \times 2 \times 2$ supercell of zeolite CHA with Al substituted at the sole T site to form a Brønsted acid site. Close-up viewpoint of the Brønsted acid site depicts the four crystallographically-distinct O sites. Atom colors: Al (purple), Si (yellow), O (red), and H (white).

The carbonylation of DME to MA is thought to proceed by the elementary steps listed in Scheme 1.

(1) $\ce{CH3OCH3 (gas) + H^{+}-Zeolite <=> CH3OCH3--H^{+}-Zeolite}$
(DME adsorption)

(2) $\ce{CH3OCH3--H^{+}-Zeolite <=> CH3OH + H3C^{+}-Zeolite}$
(DME hydrogenolysis)

(3) $\ce{CO(gas) + H3C^{+}-Zeolite <=> CO--H3C^{+}-Zeolite}$
(CO adsorption)

(4) $\ce{CO-- H3C^{+}-Zeolite <=> CH3CO^{+}-Zeolite}$
(CO addition)

(5) $\ce{CH3OCH3 (gas) + CH3CO^{+}-Zeolite <=> CH3OCH3--CH3CO^{+}-Zeolite}$
(DME adsorption)

(6) $\ce{CH3OCH3--CH3CO^{+}-Zeolite <=> CH3COOCH3--H3C^{+}-Zeolite}$
(Acetyl esterification)

(7) $\ce{CH3COOCH3--H3C^{+}-Zeolite <=> CH3COOCH3 (gas) + H3C^{+}-Zeolite}$
(MA desorption)

Scheme 1. Elementary steps involved in the carbonylation of DME to MA over zeolites

Previous experimental results have shown that DME readily adsorbs in different framework topologies⁵,⁶,¹⁸ but undergoes a slow induction period where adsorbed DME intermediates react with the Brønsted acid sites to form persistent surface methoxy intermediates along with gas phase methanol. As such, we assume herein that the

Brønsted acid sites are fully converted to methoxy intermediates at steady-state conditions. DFT-calculated activation enthalpies and free energies for elementary steps (3)-(7) at the O2 site within SSZ-13 are shown in Figures S5 and S6, respectively. This site, as discussed below, was found to be the most active. The resultant enthalpy and free energy pathways in SSZ-13 presented in Figures S5 and S6 are consistent with previous literature for DME carbonylation steps in MOR⁴³ where the largest barrier and rate limiting step involves the addition of CO to the bound methoxy species to form an acetyl intermediate (step 4: $\Delta \text{H}_\text{A} = 102.6$ kJ mol⁻¹; $\Delta \text{G}_\text{A} = 129.5$ kJ mol⁻¹). The bound acetyl can subsequently react with a second DME molecule to form MA that desorbs and a surface methoxy intermediate (step 6: $\Delta \text{H}_\text{A} = 47.8$ kJ mol⁻¹; $\Delta \text{G}_\text{A} = 91.9$ kJ mol⁻¹), thus regenerating the active methoxy site. Based on these results, the energetic analyses at the remaining O sites within SSZ-13 focus solely on steps (3) and (4) (CO adsorption and addition) that are thought to control the rates of carbonylation.

Figure 9 shows the transition states structures for the rate-determining CO addition to a bound $\text{CH}_3$ at each of the four distinct O sites. The transition states can lie in the plane of the 8MR window (sites O1 and O2, Figure 9a and b), or orient into the cage from the

6MR (site O3, Figure 9c) or the 8MR (site O4, Figure 9d). Regardless of the originating O site, the transition states for CO addition to the bound methoxy species appear to have very similar geometries, with $H_3C$--$O_{zeolite}$ distances between 2.01 and 2.05 Å and $O≡C$--$CH_3$ distances between 1.95 and 1.98 Å. Furthermore, the $O≡C$--$CH_3$ bond angles varied by only a few degrees (between 168° and 174°) for the four O sites. The reaction energies, intrinsic activation energies, and apparent activation energies for the CO addition transition state at each of the O sites are shown in Table 2. Although the geometries of the different transition states are nearly identical, the calculated intrinsic enthalpic and free energy barriers at the O1 ($\Delta H_A$ = 101.5 kJ mol⁻¹; $\Delta G_A$ = 126.7 kJ mol⁻¹) and O2 ($\Delta H_A$ = 102.6 kJ mol⁻¹; $\Delta G_A$ = 129.5 kJ mol⁻¹) sites are similar and markedly lower in energy than those over the O3 ($\Delta H_A$ = 114.0 kJ mol⁻¹; $\Delta G_A$ = 137.3 kJ mol⁻¹) and O4 ($\Delta H_A$ = 112.0 kJ mol⁻¹; $\Delta G_A$ = 136.5 kJ mol⁻¹) sites.

![](./images/812703813310873600_12.jpg)

Figure 9. Transition states for CO addition to $CH_3^+$ originating from the four O sites: (a)
O1 site, (b) O2 site, (c) O3 site, and (d) O4 site. The dotted green lines indicate close
contact interactions (< 3.50 Å) between the $CH_3^+$ or $(C)≡O$ of the transition state and the
oxygens of the SSZ-13 framework. Atom colors: Al (purple), Si (yellow), O (red), C (grey),
and H (white).

Table 2. DFT-calculated overall reaction enthalpies and intrinsic and apparent activation
energies for CO addition to methoxy in CHA at different O sites (P = 1 bar, T = 165 °C)

<table>
  <thead>
    <tr>
      <th rowspan="2">O Site</th>
      <th rowspan="2">Cationi c positio n</th>
      <th>Reaction Enthalpy</th>
      <th colspan="3">Intrinsic Barrier</th>
      <th colspan="2">Apparent Barrier</th>
    </tr>
    <tr>
      <th>$\Delta H_{rxn}$</th>
      <th>$\Delta H_A$</th>
      <th>$-T\Delta S_A$</th>
      <th>$\Delta G_A$</th>
      <th>$\Delta H_{app}$</th>
      <th>$\Delta G_{app}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O1</td>
      <td>SIII'</td>
      <td>-38.6</td>
      <td>101.5</td>
      <td>25.2</td>
      <td>126.7</td>
      <td>71.3</td>
      <td>127.1</td>
    </tr>
    <tr>
      <td>O2</td>
      <td>SIII'</td>
      <td>-46.6</td>
      <td>102.6</td>
      <td>26.9</td>
      <td>129.5</td>
      <td>69.1</td>
      <td>125.7</td>
    </tr>
    <tr>
      <td>O3</td>
      <td>SII</td>
      <td>-23.5</td>
      <td>114.0</td>
      <td>23.3</td>
      <td>137.3</td>
      <td>83.6</td>
      <td>135.6</td>
    </tr>
    <tr>
      <td>O4</td>
      <td></td>
      <td>-29.5</td>
      <td>112.0</td>
      <td>24.5</td>
      <td>136.5</td>
      <td>86.2</td>
      <td>141.3</td>
    </tr>
  </tbody>
</table>

$^{a}$Apparent enthalpy barriers are calculated with the assumption that the surface is saturated by CH₃.

The transition state for CO addition is linear in nature as a result of the CO backside attack on the CH₃ and shown by the angles of 168° to 174°. The reaction proceeds via a concerted increase in the H₃C-O<sub>zeolite</sub> bond and decrease in O≡C--CH₃ distance. The positively charged CH₃ carbenium that forms is stabilized via its interactions with the negatively charged O of the zeolite to which it was initially bound and by its interaction with the C of the attacking CO. The H₃C-O<sub>zeolite</sub> bond length is essentially the same for the 4 different O sites for carbonylation that were examined. As such, the stabilization that results from the single O<sub>zeolite</sub> alone would be very similar for all 4 sites. The other framework oxygens in the local zeolite cage or ring, however, can interact and stabilize

the carbenium ion that forms in the transition state. The $CH_3^+$ of the transition states at the O1, O2, O3, and O4 sites are distinctly different with 3, 4, 4, and 2 close contact interactions (< 3.5 Å, dotted green lines in Figure 9) between $CH_3^+$ and other zeolite oxygens, respectively. The positively charged $CH_3$-$C≡O$ transition state can be further stabilized by the interactions of its carbonyl C with the negatively charged oxygens in the zeolite framework. CO addition to methyl groups at the O1 and O2 sites, which orient within the 8MR window, results in 3 close contact interactions between the C of CO in the $O≡C$-$CH_3$ transition state and the O atoms in the zeolite framework. This is in contrast to CO addition to the methyl groups bound to the O3 or O4 sites, which orient into the cage from the 6MR or 8MR, respectively, where the CO in these transition states show little interaction with the zeolite framework. Thus, the total number of close contacts, i.e., stabilizing interactions between the transition state and zeolite framework, appear to be indicative of the propensity for CO addition at each of the O sites. The O1 and O2 sites have the greatest number of stabilizing interactions with 6 and 7 total close contacts, respectively. The lack of stabilization of the CO in the O3 and O4 transition states leads to the higher intrinsic activation enthalpies relative to the O1 and O2 sites, with differences

of ~12 kJ mol⁻¹. Thus, the lowest intrinsic barriers are obtained for the linear transition states formed at O1 and O2, which correspond to the SIII' site in the plane of the 8MR.

The increased stabilization of the positively charged $O\equiv C--CH_3$ transition state at the framework oxygens at the O1 and O2 sites in the CHA framework results in greater entropic penalties at the O1 and O2 sites compared to the O3 and O4 sites. The difference in entropic penalties between the O1 and O2 sites and the O3 and O4 sites, however, are only 2 to 3 kJ mol⁻¹. In contrast, the O1 and O2 sites show enthalpic stabilization of ~12 kJ mol⁻¹, where the enthalpic contributions tend to greatly outweigh entropic penalties for this carbonylation reaction. As such, the intrinsic free energy barriers are the smallest for the O1 and O2 sites. In addition to the intrinsic barriers, the apparent enthalpy and free energy barriers, which account for the adsorption of CO into SSZ-13, were also calculated. They show the same trends with lower apparent barriers for the O1 and O2 sites. The computational results and analyses discussed here suggest that the highest MA production rates would be obtained for methyl groups at the O1 and O2 sites corresponding to the SIII' position within the plane of the 8MR window due to the stabilizing effect of zeolite confinement on the linear transition state. The results are also

consistent with the experimentally observed trends of nonlinearly increasing MA production rates with decreasing Si/Al and subsequently increasing site SIII' occupation.

3.4 DME carbonylation activity of SAPO-34

The experimental and computational results for the DME carbonylation in SSZ-13s are consistent with prior findings in MOR and FER in that confinement is a critical parameter for catalytic activity. To determine the sensitivity of this reaction to the local strength of the acid site, we investigated the activity of SAPO-34. SAPO-34 is the silicoaluminophosphate analogue of SSZ-13. In SAPO-34, $Si^{4+}$ substitutes for $P^{5+}$ in the aluminophosphate (ALPO) framework with the CHA topology, generating a negative charge in the lattice that requires a charge-compensating cation (similar to $Al^{3+}/Si^{4+}$ substitution in zeolites). In the $H^+$-form, these catalysts exhibit Brønsted acidity that is reported to be weaker than that for zeolites (e.g., SSZ-13).$^{26,50}$ Further, both confining environments (at the 6MR in the cage and at the 8MR) are represented by protons at this Si content (9 at.%) in SAPO-34.$^{51}$ Thus, the impact of acid site strength can be evaluated

independently from confinement effects. PXRD, MAS NMR ($^{29}$Si, $^{27}$Al) and SEM-EDS analyses of the SAPO-34 material are presented in Figures S7-S10.

The DME carbonylation activity of the SAPO-34 sample compared to activities of the SSZ-13s are shown in Figure 10 as a function of the total Brønsted acid site density. The time-dependent rates are presented in Figure S11. The activity of this sample is very low, despite its large density of acid sites. The Brønsted acid signal in the $^{1}$H MAS NMR spectrum for SAPO-34 (Figure 11) shows two contributions. The shoulder that spans from the dominant signal at 3.7 ppm towards 4 ppm is attributed to zeolite-like domains that can form in SAPO when two Si⁴⁺ atoms replace Al³⁺ and P⁵⁺, creating SiO₂ domains or "islands".²⁶,⁵² Al³⁺ bound to the edges of SiO₂ domains are zeolite (aluminosilicate)-like, which gives rise to zeolite acidity at these SiO₂ island edges.⁵¹,⁵³ The dominant resonance at 3.7 ppm corresponds to Brønsted acid sites in silicoaluminophosphate domains (i.e., a single Si⁴⁺/P⁵⁺ substitution), which is shifted upfield relative to that for the SSZ-13s (4 ppm).³⁷,⁵⁴ Upfield chemical shifts are consistent with shielding effects due to higher electron densities that give rise to weaker acid sites.²⁶,⁵⁰ Decreased acid site strength can restrict the DME carbonylation pathway in two primary ways:

(i) The first step in this reaction involves an induction period, during which the Brønsted acid sites interact with the oxygen in DME. This results in a concerted proton transfer to the oxygen of DME, the elimination of methanol, and the formation of a bound methyl to the oxygen of the zeolitic framework.⁴³ If the strength of that interaction is insufficient, the formation of methoxy groups is inhibited, resulting in low surface coverage of critical intermediates.

(ii) Even if the surface is completely saturated, the surface methoxy groups that replace the protons likely bear higher electron densities, as well. Consequently, they would be poorer candidates for nucleophilic attack by CO.

Evidence of the high surface coverage of methoxy groups over SAPO-34 even at mild temperatures has been shown extensively during studies of this material as a catalyst in the methanol-to-olefins reaction.⁵⁵⁻⁵⁹ This would suggest that weaker electrophilicity of the methoxys (ii) is the primary cause of the low activity of this material. This is supported by the higher barriers calculated for the rate-determining CO addition step at the four crystallographically-distinct O sites in SAPO-34 for a methoxy-saturated surface (Table S3). Similar close contact interactions between the transition state and the framework

and minor differences in the $HC_3$-$O_{zeolite}$ bond distances (Figure S12) indicate that the confining environments and the geometries of the transition states are similar regardless of framework chemical composition. Yet, the intrinsic enthalpic barriers, particularly for the most active O1 (SSZ-13: $\Delta H_{A,O1}$ = 101.5 kJ mol⁻¹; SAPO-34: $\Delta H_{A,O1}$ = 111.8 kJ mol⁻¹) and O2 (SSZ-13: $\Delta H_{A,O2}$ = 102.6 kJ mol⁻¹; SAPO-34: $\Delta H_{A,O2}$ = 111.2 kJ mol⁻¹) sites, are ~ 10 kJ mol⁻¹ larger in SAPO-34 than in SSZ-13. The larger barriers for the rate-determining step might explain the lower MA production activity of SAPO-34 compared to SSZ-13. These results suggest that the acid strength afforded in zeolites is required for effective catalysis in the DME carbonylation reaction through the Koch-type mechanism.

![](./images/812703813310873600_13.jpg)

Figure 10. Maximum rate of MA production as a function of Brønsted acid site density

(measured by $^1$H MAS NMR) for CHA materials: SSZ-13s (solid squares) and SAPO-34
(open star).

![](./images/812703813310873600_14.jpg)

Figure 11. $^1$H MAS NMR spectra for dehydrated SSZ-13s (fine black curves) and SAPO-34 (thick green curve).

## 4 Conclusion

CHA-type zeolites (SSZ-13s) are active catalysts for the carbonylation of dimethyl ether to methyl acetate, an industrially important reaction for acetic acid production. At comparable Si/Al, the total MA produced after 24 hr over CHA is within 12% of that produced over MOR and is over 6x more than FER. To develop an understanding of the reactivity of the CHA framework, SSZ-13 materials with a wide range of Si/Al were synthesized and characterized through various physicochemical techniques and reactivity experiments. Results from this investigation suggest that methoxy groups that give the highest MA production rates in CHA are located at the 8MR, while those that give lower rates reside in the CHA cage above the 6MR. DFT results support the experimental findings, calculating the lowest activation barrier for the RDS of nucleophilic attack by CO at the methoxy group oriented within the plane of the 8MR window. These results further emphasize the critical role that confinement plays on this reaction mechanism, particularly

in the context of the positively-charged transition state stabilized by close proximity to the negatively charge zeolitic framework. Lastly, through a comparison of SAPO-34 and SSZ-13 reactivities, we demonstrated that a "zeolitic" acid site strength is required for this reaction to effectively proceed, even in similar confining environments.

ASSOCIATED CONTENT

AUTHOR INFORMATION

Corresponding Author

*Mark E. Davis, mdavis@cheme.caltech.edu.

Author Contributions

The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

Funding Sources

The authors thank Chevron for supporting the experimental work and the University of Minnesota for the computational efforts.

Supporting Information. Experimental and model fit MAS NMR spectra, SEM images, energetics vs reaction coordinate diagrams, SAPO-34 characterizations. This information is available free of charge on the ACS Publications website.

ACKNOWLEDGMENT

The authors gratefully acknowledge Dr. Sonjong Hwang and Dr. Stacey Zones for their helpful insight on the synthesis and characterization of the materials used in this investigation. The authors also acknowledge the computing resources provided by the Minnesota Supercomputing Institute (MSI) at the University of Minnesota that contributed to the calculations reported in this study.

REFERENCES

(1) Sunley, G. J.; Watson, D. J. High Productivity Methanol Carbonylation Catalysis Using Iridium The Cativa TM Process for the Manufacture of Acetic Acid. 2000, 58, 293–307.

(2) Tomas, R. A. F.; Bordado, J. C. M.; Gomes, J. F. P. P-Xylene Oxidation to Terephthalic Acid : A Literature Review Oriented toward Process Optimization and Development. *Chem. Rev.* **2013**, *113*, 7421–7469.

(3) Bejblova, M.; Prochazkova, D.; Cejka, J. Acylation Reactions over Zeolites and Mesoporous Catalysts. **2009**, *23*, 486–499.

(4) Koh, J.; Kim, H. J.; Lee, B. S.; Kim, S. D. Effect of Acid Donors on the Dyeing of Nylon Fiber with Acid Milling Dyes. **2018**, *19*, 2533–2540.

(5) Cheung, P.; Bhan, A.; Sunley, G. J.; Law, D. J.; Iglesia, E. Site Requirements and Elementary Steps in Dimethyl Ether Carbonylation Catalyzed by Acidic Zeolites. *J. Catal.* **2007**, *245*, 110–123.

(6) Bhan, A.; Allian, A. D.; Sunley, G. J.; Law, D. J.; Iglesia, E. Specificity of Sites within Eight-Membered Ring Zeolite Channels for Carbonylation of Methyls to Acetyls. *J. Am. Chem. Soc.* **2007**, *129*, 4919–4924.

(7) Kazantsev, M. S.; Luzgin, M. V; Stepanov, A. G. Carbonylation of Dimethyl Ether with CO on Solid 12-Tungstophosphoric Acid : In Situ Magic Angle Spinning NMR Monitoring of the Reaction Kinetics. *J. Phys. Chem. C* **2013**, *117*, 11168–11175.

(8) Shen, H.; Li, Y.; Huang, S.; Cai, K.; Cheng, Z.; Lv, J.; Ma, X. The Carbonylation of Dimethyl Ether Catalyzed by Supported Heteropoly Acids : The Role of Brønsted Acid Properties. *Catal. Today* **2019**, *330*, 117–123.

(9) Boronat, M.; Martínez-Sánchez, C.; Law, D.; Corma, A. Enzyme-like Specificity in Zeolites: A Unique Site Position in Mordenite for Selective Carbonylation of Methanol and Dimethyl Ether with CO. *J. Am. Chem. Soc.* **2008**, *130*, 16316–16323.

(10) Liu, J.; Xue, H.; Huang, X. Dimethyl Ether Carbonylation to Methyl Acetate over HZSM-35. **2010**, *139*, 33–37.

(11) Mori, H.; Wada, A.; Xu, Q.; Souma, Y. Novel Application of a Solid Super Acid, Sulfated Zirconia, as a Catalyst for Koch Carbonylation Reaction. *Chem. Lett.* **2000**, *29*, 136–137.

(12) Luzgin, M. V; Rogov, V. A.; Kotsarenko, N. S.; Shmachkova, V. P.; Stepanov, A. G. Methane Carbonylation with CO on Sulfated Zirconia : Evidence from Solid-State NMR for the Selective Formation of Acetic Acid. *J. Phys. Chem. C* **2007**, *111*, 10624–10629.

(13) International Zeolite Association: Structure Commission. Database of Zeolite Structures http://www.iza-structure.org/.

(14) Bhan, A.; Allian, A. D.; Sunley, G. J.; Law, D. J.; Iglesia, E. Specificity of Sites within Eight-Membered Ring Zeolite Channels for Carbonylation of Methyls to Acetyls. *J. Am. Chem. Soc.* **2007**, *129*, 4919–4924.

(15) Kim, J.; Ham, H.; Jung, H. S.; Wang, Y.; He, Y.; Tsubaki, N.; Cho, S. J.; Han, G. Y.; Bae, J. W. Dimethyl Ether Carbonylation to Methyl Acetate over Highly Crystalline Zeolite Seed-Derived Ferrierite. *Catal. Sci. Technol.* **2018**, *8*, 3060–3072.

(16) Román-Leshkov, Y.; Moliner, M.; Davis, M. E. Impact of Controlling the Site Distribution of Al Atoms on Catalytic Properties in Ferrierite-Type Zeolites. *J. Phys. Chem. C* **2011**, *115*, 1096–1102.

(17) Neurock, M. Engineering Molecular Transformations for Sustainable Energy Conversion. *Ind. Eng. Chem. Res.* **2010**, *49*, 10183–10199.

(18) Cheung, P.; Bhan, A.; Sunley, G. J.; Iglesia, E. Selective Carbonylation of Dimethyl Ether to Methyl Acetate Catalyzed by Acidic Zeolites. *Angew. Chemie - Int. Ed.* **2006**, *45*, 1617–1620.

(19) Dusselier, M.; Davis, M. E. Small-Pore Zeolites : Synthesis and Catalysis. *Chem. Rev.* **2018**, *118*, 5265–5329.

(20) Feng, X.; Yao, J.; Li, H.; Fang, Y.; Yoneyama, Y.; Yang, G.; Tsubaki, N. A Brand New Zeolite Catalyst for Carbonylation Reaction. *Chem. Commun.* **2019**, *55*, 1048–1051.

(21) Cheung, P.; Iglesia, E.; Sunley, J. G.; Law, D. J.; Bhan, A. United States Patent 7,465,822 B2, 2008.

(22) Di Iorio, J. R.; Gounder, R. Controlling the Isolation and Pairing of Aluminum in Chabazite Zeolites Using Mixtures of Organic and Inorganic Structure-Directing Agents. *Chem. Mater.* **2016**, *28*, 2236–2247.

(23) Song, J.; Wang, Y.; Walter, E. D.; Washton, N. M.; Mei, D.; Kovarik, L.; Engelhard, M. H.; Prodinger, S.; Wang, Y.; Peden, C. H. F.; Gao, F. Toward Rational Design of Cu / SSZ-13 Selective Catalytic Reduction Catalysts : Implications from Atomic-Level Understanding of Hydrothermal Stability. *ACS Catal.* **2017**, *7*, 8214–8227.

(24) Di Iorio, J. R.; Nimlos, C. T.; Gounder, R. Introducing Catalytic Diversity into Single-Site Chabazite Zeolites of Fixed Composition via Synthetic Control of Active Site

Proximity. *ACS Catal.* 2017, 7, 6663−6674.

(25) Zhao, Z.; Xing, Y.; Li, S.; Meng, X.; Xiao, F. S.; McGuire, R.; Parvulescu, A. N.; Müller, U.; Zhang, W. Mapping Al Distributions in SSZ-13 Zeolites from $^{23}$Na Solid-State NMR Spectroscopy and DFT Calculations. *J. Phys. Chem. C* 2018, 122, 9973−9979.

(26) Deimund, M. A.; Harrison, L.; Lunn, J. D.; Liu, Y.; Malek, A.; Shayib, R.; Davis, M. E. Effect of Heteroatom Concentration in SSZ-13 on the Methanol-to-Olefins Reaction. *ACS Catal.* 2016, 6, 542−550.

(27) Inui, T.; Kang, M. Reliable Procedure for the Synthesis of Ni-SAPO-34 as a Highly Selective Catalyst for Methanol to Ethylene Conversion. *Appl. Catal. A Gen.* 1997, 164, 211−223.

(28) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* 1996, 77, 3865−3868.

(29) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* 1994, 50, 17953−17979.

(30) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate Ab Initio

Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. *J. Chem. Phys.* **2010**, *132*, 154104.

(31) Grimme, S.; Ehrlich, S.; Goerigk, L. Effect of the Damping Function in Dispersion Corrected Density Functional Theory. *J. Comput. Chem.* **2011**, *32*, 1456–1465.

(32) Henkelman, G.; Uberuaga, B. P.; Jónsson, H. A Climbing Image Nudged Elastic Band Method for Finding Saddle Points and Minimum Energy Paths. *J. Chem. Phys.* **2000**, *113*, 9901–9904.

(33) Henkelman, G.; Jónsson, H. Improved Tangent Estimate in the Nudged Elastic Band Method for Finding Minimum Energy Paths and Saddle Points. *J. Chem. Phys.* **2000**, *113*, 9978–9985.

(34) Csicsery, S. M. Dehydrocyclodimerization: IV. The Reactions of Butenes. *J. Catal.* **1970**, *17*, 323–330.

(35) Materials Studio (Accelrys Inc.), Database of Structures. *Materials Studio (Accelrys Inc.), Database of Structures.* Accelrys Software Inc.

(36) Jeanvoine, Y.; Ángyán, J. G.; Kresse, G.; Hafner, J. Brønsted Acid Sites in HSAPO-34 and Chabazite: An Ab Initio Structural Study. *J. Phys. Chem. B* **1998**, *102*, 5573–

5580.

(37) Nagy, J. B.; Derouane, E. G. *Perspectives in Molecular Sieve Science: NMR Spectroscopy and Zeolite Chemistry*, 1988.

(38) Gounder, R.; Davis, M. E. Beyond Shape Selective Catalysis with Zeolites: Hydrophobic Void Spaces in Zeolites Enable Catalysis in Liquid Water. *AICHE J.* 2013, 59, 3349−3358.

(39) Zhu, X.; Kosinov, N.; Hofmann, J. P.; Mezari, B.; Qian, Q.; Rohling, R.; Weckhuysen, B. M.; Ruiz-Martínez, J.; Hensen, E. J. M. Fluoride-Assisted Synthesis of Bimodal Microporous SSZ-13 Zeolite. *Chem. Commun.* 2016, 52, 3227−3230.

(40) Hunger, M.; Ernst, S.; Steuernagel, S.; Weitkamp, J. High-Field 1H MAS NMR Investigations of Acidic and Non-Acidic Hydroxyl Groups in Zeolites H-Beta, H-ZSM-5, H-ZSM-58 and H-MCM-22. *Microporous Mater.* 1996, 6, 349−353.

(41) Park, S. Y.; Shin, C.-H.; Bae, J. W. Selective Carbonylation of Dimethyl Ether to Methyl Acetate on Ferrierite. *Catal. Commun.* 2016, 75, 28−31.

(42) Feng, P.; Zhang, G.; Chen, X.; Zang, K.; Li, X.; Xu, L. Specific Zone within 8-

Membered Ring Channel as Catalytic Center for Carbonylation of Dimethyl Ether and Methanol over FER Zeolite. *Appl. Catal. A, Gen.* **2018**, *557*, 119–124.

(43) Rasmussen, D. B.; Christensen, J. M.; Temel, B.; Studt, F.; Moses, P. G.; Rossmeisl, J.; Riisager, A.; Jensen, A. D. Reaction Mechanism of Dimethyl Ether Carbonylation to Methyl Acetate over Mordenite-a Combined DFT/Experimental Study. *Catal. Sci. Technol.* **2017**, *7*, 1141–1152.

(44) Li, B.; Xu, J.; Han, B.; Wang, X.; Qi, G.; Zhang, Z.; Wang, C.; Deng, F. Insight into Dimethyl Ether Carbonylation Reaction over Mordenite Zeolite from In-Situ Solid- State NMR Spectroscopy. *J. Phys. Chem. C* **2013**, *117*, 5840–5847.

(45) Ji, Y.; Deimund, M. A.; Bhawe, Y.; Davis, M. E. Organic-Free Synthesis of CHA- Type Zeolite Catalysts for the Methanol-to-Olefins Reaction. *ACS Catal.* **2015**, *5*, 4456–4465.

(46) Gallego, E. M.; Li, C.; Paris, C.; Martín, N.; Martínez-Triguero, J.; Boronat, M.; Moliner, M.; Corma, A. Making Nanosized CHA Zeolites with Controlled Al Distribution for Optimizing Methanol-to-Olefin Performance. *Chem. - A Eur. J.* **2018**, *24*, 14631–14635.

(47) Smith, L. J.; Eckert, H.; Cheetham, A. K. Site Preferences in the Mixed Cation Zeolite, Li,Na-Chabazite: A Combined Solid-State NMR and Neutron Diffraction Study. *J. Am. Chem. Soc.* **2000**, *122*, 1700–1708.

(48) Smith, L. J.; Eckert, H.; Cheetham, A. K. Potassium Cation Effects on Site Preferences in the Mixed Cation Zeolite Li, Na-Chabazite. *Chem. Mater.* **2001**, *13*, 385–391.

(49) Civalleri, B.; Ferrari, A. M.; Llunell, M.; Orlando, R.; Mérawa, M.; Ugliengo, P. Cation Selectivity in Alkali-Exchanged Chabazite: An Ab Initio Periodic Study. *Chem. Mater.* **2003**, *15*, 3996–4004.

(50) Bleken, F.; Bjørgen, M.; Palumbo, L.; Bordiga, S.; Svelle, S.; Lillerud, K. P.; Olsbye, U. The Effect of Acid Strength on the Conversion of Methanol to Olefins over Acidic Microporous Catalysts with the CHA Topology. *Top. Catal.* **2009**, *52*, 218–228.

(51) Martins, G. A. V.; Berlier, G.; Coluccia, S.; Pastore, H. O.; Superti, G. B.; Gatti, G.; Marchese, L. Revisiting the Nature of the Acidity in Chabazite-Related Silicoaluminophosphates: Combined FTIR And29Si MAS NMR Study. *J. Phys. Chem. C* **2007**, *111*, 330–339.

(52) Sastre, G.; Lewis, D. W.; Catlow, C. R. A. Modeling of Silicon Substitution in SAPO-5 and SAPO-34 Molecular Sieves. *J. Phys. Chem. B* **1997**, *101*, 5249–5262.

(53) Zokaie, M.; Olsbye, U.; Lillerud, K. P.; Swang, O. Stabilization of Silicon Islands in Silicoaluminophosphates by Proton Redistribution. *J. Phys. Chem. C* **2012**, *116*, 7255–7259.

(54) Zibrowius, B.; Löffler, E.; Hunger, M. Multinuclear MAS n.m.r. and i.r. Spectroscopic Study of Silicon Incorporation into SAPO-5, SAPO-31, and SAPO-34 Molecular Sieves. *Zeolites* **1992**, *12*, 167–174.

(55) Wang, W.; Buchholz, A.; Seiler, M.; Hunger, M. Evidence for an Initiation of the Methanol-to-Olefin Process by Reactive Surface Methoxy Groups on Acidic Zeolite Catalysts. *J. Am. Chem. Soc.* **2003**, *125*, 15260–15267.

(56) Wang, W.; Jiang, Y.; Hunger, M. Mechanistic Investigations of the Methanol-to-Olefin (MTO) Process on Acidic Zeolite Catalysts by in Situ Solid-State NMR Spectroscopy. *Catal. Today* **2006**, *113*, 102–114.

(57) Salehirad, F.; Anderson, M. W. Solid-State NMR Studies of Adsorption Complexes and Surface Methoxy Groups on Methanol-Sorbed Microporous Materials. *J. Catal.*

1998, 177, 189-207.

(58) Philippou, A.; Salehirad, F.; Luigi, D. P.; Anderson, M. W. Investigation of Surface Methoxy Groups on SAPO-34: A Combined Magic-Angle Turning NMR Experimental Approach with Theoretical Studies. *J. Chem. Soc. - Faraday Trans.* 1998, 94, 2851-2856.

(59) Chen, D.; Grønvold, A.; Moljord, K.; Holmen, A. Methanol Conversion to Light Olefins over SAPO-34: Reaction Network and Deactivation Kinetics. *Ind. Eng. Chem. Res.* 2007, 46, 4116-4123.

For Table of Contents only

![](./images/812703813310873600_15.jpg)