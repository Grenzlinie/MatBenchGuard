# PdTe₂ Transition-Metal Dichalcogenide: Chemical Reactivity, Thermal Stability, and Device Implementation

Gianluca D'Olimpio, Cheng Guo, Chia-Nung Kuo, Raju Edla, Chin Shan Lue, Luca Ottaviano, Piero Torelli, Lin Wang, $^*$ Danil W. Boukhvalov, $^*$ and Antonio Politano$^*$

Palladium ditelluride (PdTe₂) is a novel transition-metal dichalcogenide exhibiting type-II Dirac fermions and topological superconductivity. To assess its potential in technology, its chemical and thermal stability is investigated by means of surface-science techniques, complemented by density functional theory, with successive implementation in electronics, specifically in a millimeter-wave receiver. While water adsorption is energetically unfavorable at room temperature, due to a differential Gibbs free energy of $\approx$+12 kJ mol⁻¹, the presence of Te vacancies makes PdTe₂ surfaces unstable toward surface oxidation with the emergence of a TeO₂ skin, whose thickness remains sub-nanometric even after one year in air. Correspondingly, the measured photocurrent of PdTe₂-based optoelectronic devices shows negligible changes (below 4%) in a timescale of one month, thus excluding the need of encapsulation in the nanofabrication process. Remarkably, the responsivity of a PdTe₂-based millimeter-wave receiver is 13 and 21 times higher than similar devices based on black phosphorus and graphene in the same operational conditions, respectively. It is also discovered that pristine PdTe₂ is thermally stable in a temperature range extending even above 500 K, thus paving the way toward PdTe₂-based high-temperature electronics. Finally, it is shown that the TeO₂ skin, formed upon air exposure, can be removed by thermal reduction via heating in vacuum.

## 1. Introduction
Transition-metal dichalcogenides (TMDCs) are attracting a considerable attention, $^{[1]}$ for their intriguing applications capabilities in optoelectronics, $^{[2]}$ catalysis, $^{[3]}$ gas separation, $^{[4]}$ and desalination, $^{[5]}$ arising from their peculiarities, often complementary to those of graphene. $^{[6]}$

Chemical and thermal stability represent crucial bottlenecks in the prospect of technological exploitation of materials "beyond graphene." $^{[7]}$ Definitely, chemical instability is usually associated with the chemical reactivity of the surface$^{[8]}$ and to presence of intrinsic$^{[9]}$ or extrinsic$^{[8]}$ defects. These aspects discriminate between materials with rapid surface degradation$^{[10]}$ or ambient stable.$^{[11]}$

Usually, as-cleaved surfaces of TMDCs have a surface termination constituted by an atomic layer of chalcogens. $^{[11c]}$ The lone pair electrons of chalcogen atoms play a pivotal role in surface stability. $^{[12]}$ Correspondingly, the minimized amount of chalcogen vacancies is important for surface protection from unwanted reactions with environmental species, especially surface oxidation. $^{[11c,13]}$

Thermal stability is also crucial for industrial use of TMDCs, considering that TMDC-based electronic devices will be subjected to heating caused by current flow, light absorption, etc. In particular, thermal stability is evidently essential for high-temperature electronic devices, which are present in combustion systems, air stagnation points in supersonic aircraft, vehicle brakes, nuclear reactors, and industrial processes. $^{[14]}$ Furthermore, thermal stability is mandatory for successful use in i) distillation for seawater desalination, $^{[15]}$ ii) crystallization processes, $^{[16]}$ and iii) thermoelectricity. $^{[17]}$ Nevertheless, in many cases TMDCs

---
Dr. G. D'Olimpio, Prof. L. Ottaviano, Prof. A. Politano
Department of Physical and Chemical Sciences
University of L'Aquila
via Vetoio, 67100 L'Aquila (AQ), Italy
E-mail: antonio.politano@univaq.it

Dr. C. Guo, Prof. L. Wang
State Key Laboratory of Infrared Physics
Shanghai Institute of Technical Physics
Chinese Academy of Sciences
500 Yutian Road, Shanghai 200083, China
E-mail: wanglin@mail.sitp.ac.cn

Dr. C.-N. Kuo, Dr. C. S. Lue
Department of Physics
National Cheng Kung University
1 Ta-Hsueh Road, 70101 Tainan, Taiwan
The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adfm.201906556.

DOI: 10.1002/adfm.201906556

Dr. R. Edla, Dr. P. Torelli
Consiglio Nazionale delle Ricerche (CNR)-Istituto Officina dei Materiali (IOM)
Laboratorio TASC in Area Science Park S.S. 14 km 163.5, 34149 Trieste, Italy

Prof. D. W. Boukhvalov
College of Science
Institute of Materials Physics and Chemistry
Nanjing Forestry University
Nanjing 210037, P. R. China
E-mail: danil@njfu.edu.cn

Dr. D. W. Boukhvalov
Theoretical Physics and Applied Mathematics Department
Ural Federal University
Mira Street 19, 620002 Ekaterinburg, Russia

Prof. A. Politano
CNR-IMM Istituto per la Microelettronica e Microsistemi
VIII strada 5, I-95121 Catania, Italy

---
Adv. Funct. Mater. 2019, 201906556
1906556 (1 of 12)
© 2019 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

![](./images/812711220573372416_1.jpg)

Figure 1. a) Side and b) top views of the atomic structure of PdTe₂. Blue balls denote Pd atoms, while green balls represent Te atoms. c) the LEED pattern of PdTe₂, measured with a primary electron beam energy of 68 eV. For the same surface, d) the vibrational spectrum with infrared-active optical phonons measured by HREELS with a primary electron beam energy of 4 eV is reported (after background subtraction). We adopted for phonons the nomenclature in ref. [25]. e) The XRD pattern of single crystals of PdTe₂, taken with Cu K_α. The inset shows the photo of grown single-crystal samples.

are thermally unstable with heating-induced modifications in the electron mobility,¹⁸ self-healing of vacancy defects¹⁹ or loss in stoichiometry, due to the desorption of chalcogen atoms at temperature as low as 470 K for MoS₂.²⁰

Recently, atomically thin layers of PdTe₂²¹ were proposed as thermoelectric materials with predicted ZT values as high as 1.18,²¹ comparable with values for state-of-the-art thermoelectric materials as Bi₂Te₃.²² Moreover, PdTe₂ has also attracted great interest in consideration of the presence of type-II Dirac fermions²³ and for the observation of superconductivity.²³a,24

PdTe₂ crystallize in the CdI₂-type trigonal (1T) structure with P-3m1 space group (No. 164), sketched in Figure 1a,b. Each Pd atom at the basal plane is surrounded by six Te atoms, forming PdTe₆ octahedra.

Herein, we have studied the chemical and thermal stability of PdTe₂ through density functional theory (DFT) and experiments by high-resolution electron energy loss spectroscopy (HREELS), X-ray photoelectron spectroscopy (XPS), and atomic force microscopy (AFM). We find that the as-cleaved surface has a Te termination that evolves into a TeO₂ skin in oxygen environment and in air. The thickness of the TeO₂ surface layer remains sub-nanometric even after 1 year in air. Surface tellurium-oxide phases can be thermally reduced via heating. Ambient-stable PdTe₂ was employed to fabricate millimeter-wave receivers, which show negligible changes in responsivity in a timescale of 1 month, even without encapsulation of the active channel. Moreover, PdTe₂-based millimeter-wave receivers exhibit higher performance and responsivity than similar devices based on black phosphorus and graphene.

## 2. Results and Discussion
### 2.1. Surface Chemical Reactivity and Chemical Stability

As-cleaved samples show a low-energy electron diffraction (LEED) pattern with sharp spots against a low background, indicating high crystalline quality of the as-cleaved surface (Figure 1c), which exhibits (Figure 1d) optical phonons $\Gamma_2^+$ (15 meV) and $\Gamma_2^-$ (23 meV), in agreement with the calculated phonon density of states reported in ref. [26] Crystalline quality was also assessed by X-ray diffraction (XRD, Figure 1e and Figure S1 in Supporting Information).

The analysis of core-level spectra measured with XPS is crucial in order to assess surface stability and reactivity of PdTe₂. From the analysis of Te-3d core levels (Figure 2a), at binding energies of 573.1 and 583.5 eV (Figure 2a), we infer that the as-cleaved surface is not affected by surface treatments (O₂ dosage at room temperature at doses as high as $10^5$ L, with $1\ \text{L}=10^{-6}$ Torr s). Binding energies of Te-3d core levels are consistent with the case of the parental compound PtTe₂.¹¹c Only air exposure induces the emergence of components at 576.0 (Te-3d₅/₂) and

![](./images/812711220573372416_2.jpg)

Figure 2. Panels (a) and (b) show Te-3d and Pd-3d core levels for pristine, as-cleaved surface of PdTe₂ and for its modification upon O₂ dosage (10⁵ L) and air exposure. Panels (c), (d) report the same for defected PdTe₂ (PdTe₁.₇). The photon energy is 800 eV.

586.4 eV (Te-3d₃/₂), arising from TeO₂ formation,⁽²⁷⁾ similarly to the case of PtTe₂.⁽¹¹ᶜ⁾ The spectral amplitude of TeO₂ components is higher in defected samples (PdTe₁.₇), thus pointing to a key role of Te vacancies in surface oxidation.

By means of quantitative analysis of XPS data,⁽²⁸⁾ we have estimated the thickness of the TeO₂ skin after air exposure to be i) 2.2 ± 0.4 Å after 10 min in air and ii) 8.8 ± 0.5 Å after 1 year in air. No substantial differences are found in PdTe₁.₇, except a faster oxidation kinetics. As a matter of fact, after ten minutes in air, the TeO₂ skin is already ≈5.8 Å thick.

Surface treatments do not induce any change in Pd-3d core levels. The Pd-3d doublet (Figure 2) is observed at binding energies of 336.7 (3d₅/₂) and 341.9 (3d₃/₂) eV, respectively. A core-level shift of 1.3 eV exists compared to Pd (100),⁽²⁹⁾ while similar values of the binding energy for Pd-3d were reported for Pd–S alloys⁽³⁰⁾ and for thin films of PdTe₂ grown by molecular beam epitaxy.⁽³¹⁾

Notably, we find that water does not adsorb on PdTe₂ at room temperature, as evidenced by the absence of changes in the Te-3d and Pd-3d core levels (Figure S2, Supporting Information).

Vibrational spectra represent an ideal complement to XPS studies, in consideration of the high surface sensitivity of HREELS.⁽³²⁾ The vibrational spectrum of the air-exposed surface probed by HREELS exhibits a single band with two components at 80 and 92 meV, which are ascribed to optical phonons of TeO₂ phases.⁽³³⁾ On the other hand, the PdTe₂ surface does not show any H₂O-derived vibrational mode even after prolonged H₂O dosage at room temperature (up to a total dose of 10⁶ L). Especially, the absence of O–H stretching at 410–420 and 450 meV (see ref. [34] for a review on vibrational spectroscopy of water on solid surfaces) demonstrates the absence of H₂O and OH in over-surface adsorption sites, respectively. Similarly, the absence of C–O stretching at 210–260 meV in the vibrational spectrum (Figure S5, Supporting Information) indicates that PdTe₂ is not affected by CO poisoning.

Experimental results in Figures 2 and 3 have been supplemented by a theoretical model aimed at unveiling the surface chemical reactivity of PdTe₂. Explicitly, we modeled physical adsorption (Figure 4a) and further decomposition (Figure 4b) of water, carbon monoxide, and oxygen molecules. Theoretical results (Table 1) demonstrate that, at room temperature, physical adsorption of molecular oxygen is energetically favorable (differential Gibbs free energy ΔG = −55.49 kJ mol⁻¹), while adsorption of water and carbon

![](./images/812711220573372416_3.jpg)

Figure 3. Vibrational spectrum of oxidized $PdTe_2$, obtained after air exposure of a $PdTe_2$ surface (black curve), and of $H_2O$-dosed $PdTe_2$ (red curve, taken after a water exposure of $10^6$ L at room temperature). The primary electron beam energy is 4 eV.

monoxide is energetically unfavorable ($\Delta G = +11.92$ and $+9.45$ kJ mol⁻¹ respectively).

Decomposition of the adsorbed molecule is favorable for the case of oxygen and unfavorable for water. Note that the presence of Te vacancies in the surface layer only provides slight changes in the energetics of chemisorption/decomposition of ambient gases. Additionally, we checked the energetics of the oxygenation of whole Te surface termination, finding that this process is less energetically favorable than the decomposition of the first oxygen molecule on the pristine surface, although it remains exothermic (differential enthalpy $\Delta H = -32.98$ kJ mol⁻¹). The presence of Te vacancies favors the complete oxygenation of the surface ($\Delta H = -39.11$ kJ mol⁻¹ in $PdTe_{1.88}$). Notably, the evolution of the oxygenated surface (corresponding to $TeO$) into a $TeO_2$ skin (Figure 4d) is a particularly favorable process ($\Delta H = -295.27$ kJ mol⁻¹). Note that, in contrast to the case of $PtTe_2^{[11c]}$ the presence of Te vacancies only provides a slight increase of the chemical activity, due to the minimization of the local distortion of atomic structure near the defect (see Figure 4b). To evaluate the effect of a larger concentration of vacancies, we considered two Te vacancies in the top layer ($PdTe_{1.73}$). We considered various locations of the second Te vacancy, finding that the most energetically favorable ($\approx 17$ kJ mol⁻¹) position is in the nearness of the first vacancy. The presence of double Te vacancy decreases the differential Gibbs free energy for physical adsorption of oxygen to $-58.61$ kJ mol⁻¹ with higher favorability for decomposition ($-106.42$ kJ mol⁻¹). Therefore, both defected and undefected $PdTe_2$ surfaces are subjected to oxidation, although defected surfaces are more prone to oxidation. Correspondingly, the $TeO_2$ component in Te-3d core levels is higher in air-exposed defected surface compared to air-exposed undefected $PdTe_2$ (Figure 2c).

We also extended our model to the case of the single layer of pristine $PdTe_2$, finding (see Table 1) negligible (within a few kJ mol⁻¹) changes in the chemical reactivity of $PdTe_2$.

To assess the suitability of $PdTe_2$ for catalysis, we modeled oxygen and hydrogen evolution reactions (OER and HER) over pristine and defected surfaces of bulk $PdTe_2$, before and after oxidation. Calculated values of free energies for HER (Figure 5a) evidence unsuitability of pristine $PdTe_2$ for this reaction. Surface oxidation slightly decreases the energy cost of the reaction (0.17 eV). Conversely, the presence of the defects in both pristine and oxidized surfaces significantly decreases the free energy for HER (0.33 and 0.21 eV, respectively) but the magnitude is still quite larger than for Pt(111) surface (about 0.1 eV), usually taken as standard reference. Obtained results well match with the recent reports about the poor catalytic performance of bulk $PdTe_2^{[35]}$ which however is increased after exfoliation in nanosheets, as demonstrated for the case-study example of ethanol oxidation reaction (EOR).$^{[36]}$ In the case of OER, pristine bulk $PdTe_2$ exhibits catalytic efficiency comparable to Pt (Figure 5b). Surface oxidation induces an increase of the energy cost of the last step of OER.

We have also checked the influence of the oxidation on electronic structure of $PdTe_2$ and $PdTe_{1.88}$ by analyzing the density of states (DOS, Figure 6). The presence of Te vacancies in $PdTe_{1.88}$ provides almost no changes in occupied bands, while weak features appear in unoccupied Pd-4d bands (about 3 eV above the Fermi level, see Figure 6a). Dissociative adsorption of oxygen (Figure 6b), full oxygenation (Figure 6c) and $TeO_2$ formation (Figure 6d) involve an increase of the number of states between $-4.5$ and $-1.0$ eV, although the most evident change in DOS is associated with the appearance of a band around $-18$/$-19$ eV (see Figures 6c-e and 7). These changes correspond to the formation of O-2p and O-2s bands, respectively (see partial DOS in Figure 6e). Oxidation also provides visible changes in unoccupied parts corresponding with the higher amplitude of the peak at $\approx +4$ eV, due to the contribution of Te atoms from oxidized layer (Figure 6e). Correspondingly, also Pd-derived states are changed after oxidation (Figure 6e). These findings are in qualitative agreements with experimentally observed changes in valence-band spectra (Figure 7). Especially, upon oxidation we observe the appearance of a mode at a binding energy of $\approx 18$ eV, due to O-2s states in $TeO_2$. Such a feature is observed as a weak component after a short-term exposure (10 min) to air (blue curve in Figure 7) and becomes an intense peak only in aged samples (kept in air for 1 year, green curve in Figure 7).

To evaluate the environmental stability of $PdTe_2$, the time evolution of AFM images of mechanically exfoliated flakes (Figure 8a,b) was followed on a timescale extended to 1 month. AFM results demonstrate that exposure to ambient atmosphere does not change the morphology of the flakes, as confirmed by the height profile along a specific direction remaining constant with exposure (Figure 8c).

The proven air stability of $PdTe_2$ TMDC can be exploited to devise a nanodevice without encapsulating the active channel. Especially, high-frequency tests are particularly suitable to evaluate the generation-recombination noise associated with material degradation.$^{[38]}$ Therefore, we tested the suitability of $PdTe_2$

![](./images/812711220573372416_4.jpg)

Figure 4. Optimized atomic structure of a) water physically adsorbed on pristine PdTe₂ and b) oxygen molecule decomposed in the nearness of one Te vacancy. Panel c) depicts a total uniform oxygenation of the surface Te termination, while panel d) illustrates the formation of a TeO₂-like layer on the surface. Green, blue, and red balls denote Te, Pd, and O atoms, respectively.

for high-frequency electronics and, specifically, for the buildup of the next wireless communication network at a high data rate. Explicitly, we designed and manufactured a PdTe₂-based millimeter-wave receiver, shown in the optical micrograph in Figure 9a and sketched in Figure 9b. The device was subjected to electromagnetic radiation (output power of 30 mW) at a 40 GHz carrier-wave frequency, which has been proposed by Global Mobile Supplier Association³⁹ as the hotspot for the next interconnected communication system.

We studied the response characteristics of PdTe₂-based devices with a direct comparison with similar devices fabricated with black phosphorus and graphene (Figure 9c,d). It is also worth noticing that other TMDCs, including MoS₂ and WS₂, effectively work at frequency lower than 10 GHz, because of their low mobility achieved in experimental studies (few tens of cm² V⁻¹ s⁻¹⁴⁰), which represents a serious hurdle for their usage in high-frequency electronics.⁴¹ Notably, PdTe₂-based millimeter-wave detectors are more sensitive than similar devices based on black phosphorus and graphene (Figure 9c,d). Specifically, photocurrent values are higher in PdTe₂ by even an order of magnitude

Table 1. Differential enthalpy ΔH and differential Gibbs free energy ΔG (at room temperature) for physical adsorption and differential enthalpy of decomposition (all in kJ mol⁻¹) of molecular oxygen and water on PdTe₂ and PdTe₁.₈₈ surfaces. In the case of oxygen decomposition, we also report, in parenthesis, the differential enthalpy for the formation of i) an oxygenated surface and ii) a TeO₂-like layer.

<table>
<thead>
<tr>
<th>Surface</th>
<th>Chemical species</th>
<th colspan="2">Physisorption</th>
<th>Decomposition</th>
</tr>
<tr>
<th></th>
<th></th>
<th>ΔH [kJ mol⁻¹]</th>
<th>ΔG [kJ mol⁻¹]</th>
<th>ΔH [kJ mol⁻¹]</th>
</tr>
</thead>
<tbody>
<tr>
<td>PdTe₂</td>
<td>O₂</td>
<td>−66.79</td>
<td>−55.49</td>
<td>−94.40(−32.98/−295.27)</td>
</tr>
<tr>
<td></td>
<td>H₂O</td>
<td>−19.38</td>
<td>+11.92</td>
<td>+131.49</td>
</tr>
<tr>
<td></td>
<td>CO</td>
<td>−9.90</td>
<td>+9.45</td>
<td>—</td>
</tr>
<tr>
<td>PdTe₁.₈₈</td>
<td>O₂</td>
<td>−53.74</td>
<td>−52.44</td>
<td>−92.28(−39.11/−336.44)</td>
</tr>
<tr>
<td></td>
<td>H₂O</td>
<td>−20.25</td>
<td>+11.05</td>
<td>+167.68</td>
</tr>
<tr>
<td></td>
<td>CO</td>
<td>−9.41</td>
<td>+9.94</td>
<td>—</td>
</tr>
<tr>
<td>PdTe₂ monolayer</td>
<td>O₂</td>
<td>−66.91</td>
<td>−55.61</td>
<td>−85.25(−27.31/−298.41)</td>
</tr>
<tr>
<td></td>
<td>H₂O</td>
<td>−22.34</td>
<td>+8.96</td>
<td>+158.99</td>
</tr>
<tr>
<td></td>
<td>CO</td>
<td>−7.48</td>
<td>+11.87</td>
<td>—</td>
</tr>
</tbody>
</table>

![](./images/812711220573372416_5.jpg)

Figure 5. Free energy diagrams for a) HER and b) OER on various surfaces of PdTe₂. Values for Pt (111) are from ref. [37]. The symbol "*" corresponds to the substrate.

compared to black phosphorus and graphene, as it can be inferred from the behavior of the power-dependent photo-current (Figure 9c). By comparing the behavior of the photo-current as a function of the bias voltage (Figure 9d), it is also evident that the PdTe₂-based device possesses larger dynamic regime than black phosphorus- and graphene-based devices for carrier-frequency conversion. Specifically, the dynamic regime, defined as the ratio between the photocurrent at 100 and 0 mV, i.e., $20\log(I_{ph\_100\ \text{mV}}/I_{ph\_0\ \text{mV}})$, is 35 dB for PdTe₂, 12 dB for graphene and 6 dB for black phosphorus. Explic-itly, under the same operational conditions ($f = 40$ GHz; $V_{\text{sd}} = 100$ mV, $P = 30$ mW), the responsivity of the PdTe₂-based millimeter-wave receiver (6.4 A W⁻¹) is 21 and 13 times greater than that of similar devices based on graphene and black phosphorus, respectively.

Furthermore, PdTe₂-based devices also exhibit excellent air stability. As shown in Figure 9e, the variation in photo-signal for PdTe₂-based devices within 1 month air exposure is below $\approx$4%, thus supporting PdTe₂ as a promising candidate for micro- and nanoelectronics. The output of the fabricated device shows good repetition ability with sharp rise/fall times, closely following the coded digital signal (Figure 9f). The signal exhibits especially good repeatability without decay even after a 1 month exposure to the ambient environment, thus elucidating the superb stability of a PdTe₂ device working at a frequency above the cutoff frequency (12 GHz) of a transistor with a micrometer-long channel.[42] Therefore, PdTe₂ could be an ideal platform for engineering devices for next-generation communication and optoelectronic applications.

![](./images/812711220573372416_6.jpg)

Figure 6. Total densities of states (DOS) for PdTe₂ (red curve) and PdTe₁.₈₈ (blue curve): a) pristine surfaces; b) after decomposition of a single oxygen molecule (see Figure 4b); c) after oxygenation of whole Te surface layer (see Figure 4c); d) after formation of a TeO₂-like surface layer (see Figure 4d). On panel e), partial DOS for oxygen (green curve), tellurium bound with oxygen (black curve), and palladium atoms (magenta curve) for the totally oxidized layer is shown. Fermi energy is set as zero.

![](./images/812711220573372416_7.jpg)

Figure 7. Valence-band spectra for the as-cleaved PdTe₂ surface (black curve) and for its modification upon O₂ dosage (10⁵ L at room temperature, red curve), air exposure for 10 min (blue curve) and aging of 1 year in air (green curve), respectively. The photon energy is 400 eV.

![](./images/812711220573372416_8.jpg)

Figure 8. Time evolution of AFM images of a ≈100 nm thick flake of PdTe₂. Panel a) shows the flake immediately after exfoliation, while panel b) displays the same flake after 1 month in air. The dotted white lines in panels (a) and (b) indicate the path of the height profile reported in panel (c).

### 2.2. Thermal Stability

We also assessed the thermal stability in vacuum of the PdTe₂ surface, with a particular care to the possible influence of surface TeO₂ phases. **Figure 10** shows the evolution upon heating of Pd-3d and Te-3d core levels measured for (panels a,b) the as-cleaved, undefected PdTe₂ surface and (panels c,d) in the presence of the surface TeO₂ phase, respectively. We focused on the evolution of Te-3d core levels upon annealing for the case of the oxidized surface, as compared to spectra acquired for pristine PdTe₂. The temperature increase induces notable changes in the intensity of the oxide component of the Te-3d core-level spectra. Specifically, the relative weight of the oxide component in Te-3d core levels decreases with increasing heating temperature. We attribute the modification of the core-level spectra to the thermal reduction of surface TeO₂ phases. The reduction process also continues during the cooling procedure, with a final reduction of the oxide component to 62% with respect to the initial value, after thermalization at room temperature.

Conversely, no change is found for Pd-3d core levels for both i) pristine, undefected PdTe₂ and ii) the oxidized surface after the heating/cooling process.

The analysis of the valence band could provide further insights on the influence of TeO₂ phases and their thermal reduction on the electronic properties. In **Figure 11**, the valence band of the pristine and oxidized PdTe₂ is reported for different heating temperatures with subsequent cooling. Valence band for as-cleaved pristine surface is unmodified by the annealing treatment, confirming that the pristine surface is thermally stable. Contrariwise, the valence band of oxidized PdTe₂ displays a different behaviour. Specifically, the broad peak at 6–7 eV (associated to O-2p states, according to partial DOS in Figure 6e) decreases its intensity when temperature increases from 300 up to 540 K. During the cooling procedure, the intensity of this feature remains constant.

The thermal stability of PdTe₂ is further verified by the thermal gravimetric analysis (TGA). The weight change is negligible in the TGA curve up to 680 K (**Figure 12**) and, correspondingly, the differential thermal gravimetry (DTG) curve in inert atmosphere is flat (see Figure S6, Supporting Information, for the case of a reactive atmosphere). These evidences

![](./images/812711220573372416_9.jpg)

Figure 9. a) Optical micrograph of the PdTe₂-based device; b) architecture of PdTe₂ millimeter-wave receiver; c) power dependence of PdTe₂-(black curve), black phosphorus-(green curve) and graphene-based (red curve) devices; d) bias dependence of PdTe₂-(black curve), black phosphorus- (green curve) and graphene-based (red curve) devices; e) photosignal of the as-fabricated PdTe₂ device (black squares) and after 1 month in air (blue squares); f) time-resolved response of the as-prepared PdTe₂ millimeter-wave receiver (black curve) and after 1 month in air (blue curve).

point to a nearly zero thermal expansion coefficient for PdTe₂, as previously reported for other layered materials.⁽⁴³⁾

## 3. Conclusions
We have demonstrated that the oxidation of PdTe₂ proceeds via the formation of a surface TeO₂ skin, whose thickness remains sub-nanometric even after 1 year in air. On the other hand, no reactivity toward water at room temperature is found. We have also shown that undefected PdTe₂ is thermally stable in the temperature range usually employed for most applications (even above 500 K). Conversely, surface TeO₂ phases are thermally unstable, due to temperature-induced reduction, which also implies changes in the electronic properties. The thermal reduction of surface TeO₂ phase should be kept into account when analyzing any temperature-dependent effects in Te-terminated TMDC.

The catalytic activity of bulk PdTe₂ is rather limited, although exfoliation in nanosheets increases the number of active sites.

Correspondingly, devices with PdTe₂-based active channels exhibit good air stability even without encapsulation. We devised a PdTe₂-based millimeter-wave receiver, exhibiting both fast response data rate at 40 GHz, high sensitivity (responsivity of ≈6.4 A W⁻¹) and dynamic regime of 35 dB, with negligible changes in its performances (below 4%) after air exposure for 1 month. The high-frequency receiver is able to detect carrier frequencies higher than cut-off frequency of other van der Waals semiconductors, thus paving the way for the use of PdTe₂ for future communication or imaging systems.

## 4. Experimental Section
*Experimental Methods:* Single crystals of PdTe₂ were prepared by the slow cooling method. High-purity Pd (99.9%) sheet and Te powder

![](./images/812711220573372416_10.jpg)

Figure 10. Pd-3d and Te-3d core levels taken for (a, b) the pristine PdTe₂ surface and (c, d) oxidized PdTe₂, respectively. Core-level spectra were acquired at different heating/cooling temperatures. The photon energy is 800 eV.

![](./images/812711220573372416_11.jpg)

Figure 11. Valence-band spectra normalized to the Fermi edge for a) as-cleaved and b) oxidized PdTe₂. The photon energy is 400 eV.

![](./images/812711220573372416_12.jpg)

Figure 12. TGA (blue) and DTG (red) curves for PdTe₂ in the 300–680 K range, measured in an inert atmosphere (N₂).

(99.9999%) were mixed in the ratio of 1:2 and sealed under vacuum in a cone-shaped quartz tube. The quartz tube was heated to 900 °C, dwelled for 24 h, and slowly cooled at a rate of 3–5 °C h⁻¹ to 450 °C. The resulting crystals, with typical dimensions of 10 × 10 × 3 mm³ (Figure 1e) with the c-axis perpendicular to the plates, can be easily cleaved and show superb flatness.

The structure of the grown crystals was examined by X-ray diffraction (Bruker D2 PHASER) using Cu Kα radiation and Laue diffraction (Photonic Science) at room temperature. The sharp lines in the XRD pattern and clear spots in the Laue pattern suggest high crystalline quality (Figure 1e). Samples were exfoliated in situ by adhesive tape. In Figure S1 (Supporting Information), the XRD pattern of powdered single crystals was also reported.

XPS experiments were performed at the high-energy branch of the advanced photoelectric experiments beamline (APE-HE) of the Elettra Synchrotron, Trieste, Italy. XPS spectra were acquired with an Omicron EA125 hemispherical electron energy analyzer, with the sample at room temperature and in normal emission condition. The linearly polarized light impinged on the sample forming an angle of 45° with respect to the normal to the surface. Energy resolution was 0.1 eV. No beam-induced damage was observed even after long-time exposure to synchrotron light.

HREELS experiments were carried out with a Delta 0.5 spectrometer by Specs GmbH, Germany. The impinging energy was 4 eV. Spectra were recorded in specular direction, with an incidence angle of 55° with respect to the sample normal.

AFM experiments were performed by means of Dimension ICON microscope from Bruker, USA.

The PdTe₂-based millimeter-wave detector was fabricated by electron beam lithography and electron beam evaporation. Photocurrent experiments were performed by using a lock-in amplifier (LIA) after a low-noise voltage preamplifier. The radiation frequency and the power were 40 GHz and 30 mW, respectively. The current–voltage characteristics were measured by using B2912A Semiconductor Analyzer.

TGA analysis was carried out with a NETZSCH STA 449 F3 instrument in N₂ atmosphere. Around 23 mg of powders was gradually heated from 300 to 673 K at a heating rate of 5 K min⁻¹.

Theoretical Methods: The atomic structure and energetics of various configurations of various gases on PdTe₂ were studied by DFT using the QUANTUM-ESPRESSO code⁽⁴⁴⁾ and the GGA-PBE + van der Waals (vdW) approximation, feasible for the description of the adsorption of molecules on surfaces.⁽⁴⁵⁾ Energy cutoffs of 25 and 400 Ry for the plane-wave expansion of the wave functions and the charge density, respectively, and the 4 × 4 × 3 Monkhorst-Pack k-point grid for the Brillouin sampling were used.⁽⁴⁶⁾ For the modeling of the surface of PdTe₂, a slab of three layers was used (Figure 4). The presence of the Te vacancies in the top layer was also considered. The formation of the single vacancy corresponds to PdTe₁.₈₈ for the outermost surface layer.

Physisorption enthalpies were calculated by the standard formula

$$
\Delta H_{\text{phys}} = \left[ E_{\text{host+mol}} - \left( E_{\text{host}} + E_{\text{mol}} \right) \right] \tag{1}
$$

where $E_{\text{host}}$ is the total energy of pristine surface, and $E_{\text{mol}}$ is the energy of the single molecules of selected species in empty box. In the case of water adsorption, the gaseous phase was only considered. Chemisorption energy is defined as the difference between the total energy of the system with adsorbed molecule and the total energy of same system after decomposition of the same molecule on the surface. For the case of physisorption, differential Gibbs free energy was also evaluated by the formula

$$
\Delta G = \Delta H - T\Delta S \tag{2}
$$

where $T$ is the temperature and $\Delta S$ is the change of entropy of adsorbed molecule, which was estimated considering the gas→liquid transition by the standard formula

$$
\Delta S = \Delta H_{\text{vaporization}} / T \tag{3}
$$

where $\Delta H_{\text{vaporization}}$ is the measured enthalpy of vaporization. All formulas and technical details for the calculations of HER and OER are the same used for modelling these reactions over Pt(111) substrate.⁽³⁷⁾ The value of overpotential $U = 1.23$ eV was used.

### Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

### Acknowledgements
G.D.O., C.G., C.N.K. contributed equally to this work. This work was partly performed in the framework of the nanoscience foundry and fine analysis (NFFA-MIUR Italy, Progetti Internazionali) facility.

### Conflict of Interest
The authors declare no conflict of interest.

### Keywords
DFT calculations, palladium ditelluride, surface science, transition-metal dichalcogenides, XPS

Received: August 10, 2019
Revised: October 15, 2019
Published online:

[1] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, M. S. Strano, Nat. Nanotechnol. 2012, 7, 699.
[2] a) Z. Guo, A. Wei, Y. Zhao, L. Tao, Y. Yang, Z. Zheng, D. Luo, J. Liu, J. Li, Appl. Phys. Lett. 2019, 114, 153102; b) L. H. Zeng, D. Wu, S. H. Lin, C. Xie, H. Y. Yuan, W. Lu, S. P. Lau, Y. Chai, L. B. Luo, Z. J. Li, Y. H. Tsang, Adv. Funct. Mater. 2019, 29, 1806878; c) S. Witomska, T. Leydecker, A. Ciesielski, P. Samorì, Adv. Funct. Mater. 2019, 29, 1901126; d) M. Long, P. Wang,

---
Adv. Funct. Mater. 2019, 1906556
1906556 (10 of 12)
© 2019 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

H. Fang, W. Hu, *Adv. Funct. Mater.* 2019, 29, 1803807; e) L. B. Luo, D. Wang, C. Xie, J. G. Hu, X. Y. Zhao, F. X. Liang, *Adv. Funct. Mater.* 2019, 29, 1900849; f) U. N. Noumbé, C. Gréboval, C. Livache, T. Brule, B. Doudin, A. Ouerghi, E. Lhuillier, J. F. Dayen, *Adv. Funct.* Mater. 2019, 29, 1902723; g) J. K. Qin, G. Qiu, W. He, J. Jian, M. W. Si, Y. Q. Duan, A. Charnas, D. Y. Zemlyanov, H. Y. Wang, W. Z. Shao, L. Zhen, C. Y. Xu, P. D. Ye, *Adv. Funct. Mater.* 2018, 28, 1806254; h) B. Sun, Z. Wang, Z. Liu, X. Tan, X. Liu, T. Shi, J. Zhou, G. Liao, *Adv. Funct. Mater.* 2019, 29, 1900541; i) L. H. Zeng, D. Wu, S. H. Lin, C. Xie, H. Y. Yuan, W. Lu, S. P. Lau, Y. Chai, L. B. Luo, Z. J. Li, Y. H. Tsang, *Adv. Funct. Mater.* 2019, 29, 1806878.

[3] a) X. Chia, M. Pumera, *Chem. Soc. Rev.* 2018, 47, 5602;
b) P. Zhuang, Y. Sun, P. Dong, W. Smith, Z. Sun, Y. Ge, Y. Pei, Z. Cao, P. M. Ajayan, J. Shen, M. Ye, *Adv. Funct. Mater.* 2019, 29, 1901290.

[4] a) S. Kim, H. Wang, Y. M. Lee, *Angew. Chem.* 2019, https://doi.org/10.1002/anie.201814349; b) J. Shen, G. Liu, Y. Ji, Q. Liu, L. Cheng, K. Guan, M. Zhang, G. Liu, J. Xiong, J. Yang, W. Jin, *Adv. Funct. Mater.* 2018, 28, 1801511.

[5] W. Li, Y. Yang, J. K. Weber, G. Zhang, R. Zhou, *ACS Nano* 2016, 10, 1829.

[6] a) H. Zhang, H. M. Cheng, P. Ye, *Chem. Soc. Rev.* 2018, 47, 6009;
b) N. Sethulakshmi, A. Mishra, P. M. Ajayan, Y. Kawazoe, A. K. Roy, A. K. Singh, C. S. Tiwary, *Mater. Today* 2019, 27, 107; c) S. Deng, A. V. Sumant, V. Berry, *Nano Today* 2018, 22, 14; d) Y. Liu, X. Duan, Y. Huang, X. Duan, *Chem. Soc. Rev.* 2018, 47, 6388; e) Z. Zeng, X. Sun, D. Zhang, W. Zheng, X. Fan, M. He, T. Xu, L. Sun, X. Wang, A. Pan, *Adv. Funct. Mater.* 2019, 29, 1806874; f) X. Zang, J. N. Hohman, K. Yao, P. Ci, A. Yan, M. Wei, T. Hayasaka, A. Zettl, P. J. Schuck, J. Wu, L. Lin, *Adv. Funct. Mater.* 2019, 29, 1807612;
g) A. Zafar, Z. Zafar, W. Zhao, J. Jiang, Y. Zhang, Y. Chen, J. Lu, Z. Ni, *Adv. Funct. Mater.* 2019, 29, 1809261; h) X. Sang, X. Li, A. A. Puretzky, D. B. Geohegan, K. Xiao, R. R. Unocic, *Adv. Funct. Mater.* 2019, 1902149; i) X. Jing, Y. Illarionov, E. Yalon, P. Zhou, T. Grasser, Y. Shi, M. Lanza, *Adv. Funct. Mater.* 2019, 1901971;
j) H. Jin, Z. Hu, T. Li, L. Huang, J. Wan, G. Xue, J. Zhou, *Adv. Funct. Mater.* 2019, 29, 1900649; k) T. M. Higgins, S. Finn, M. Matthiesen, S. Grieger, K. Synnatschke, M. Brohmann, M. Rother, C. Backes, J. Zaumseil, *Adv. Funct. Mater.* 2019, 29, 1804387; l) H. Feng, Z. Xu, J. Zhuang, L. Wang, Y. Liu, X. Xu, L. Song, W. Hao, Y. Du, *Adv. Funct. Mater.* 2019, 29, 1900367; m) F. Wang, Z. Wang, L. Yin, R. Cheng, J. Wang, Y. Wen, T. A. Shifa, F. Wang, Y. Zhang, X. Zhan, J. He, *Chem. Soc. Rev.* 2018, 47, 6296.

[7] a) R. Thakur, A. VahidMohammadi, J. Moncada, W. R. Adams, M. Chi, B. Tatcharku, M. Beidaghi, C. A. Carrero, *Nanoscale* 2019, 11, 10716; b) X. Liu, J. D. Wood, K.-S. Chen, E. Cho, M. C. Hersam, *J. Phys. Chem. Lett.* 2015, 6, 773; c) M. Seredych, C. E. Shuck, D. Pinto, M. Alhabeb, E. Precetti, G. Deysher, B. Anasori, N. Kurra, Y. Gogotsi, *Chem. Mater.* 2019, 31, 3324.

[8] A. Politano, M. S. Vitiello, L. Viti, D. W. Boukhvalov, G. Chiarello, *FlatChem* 2017, 1, 60.

[9] W. Zhou, X. Zou, S. Najmaei, Z. Liu, Y. Shi, J. Kong, J. Lou, P. M. Ajayan, B. I. Yakobson, J.-C. Idrobo, *Nano Lett.* 2013, 13, 2615.

[10] a) J. O. Island, G. A. Steele, H. S. J. van der Zant, A. Castellanos-Gomez, *2D Mater.* 2015, 2, 011002; b) X. Han, J. Han, C. Liu, J. Sun, *Adv. Funct. Mater.* 2018, 28, 1803471.

[11] a) R. C. Longo, R. Addou, S. Kc, J.-Y. Noh, C. M. Smyth, D. Barrera, C. Zhang, J. W. P. Hsu, R. M. Wallace, K. Cho, *2D Mater.* 2017, 4, 025050; b) J. Gao, A. Cupolillo, S. Nappini, F. Bondino, R. Edla, V. Fabio, R. Sankar, Y. W. Zhang, G. Chiarello, A. Politano, *Adv. Funct. Mater.* 2019, 29, 1900965; c) A. Politano, G. Chiarello, C.-N. Kuo, C. S. Lue, R. Edla, P. Torelli, V. Pellegrini, D. W. Boukhvalov, *Adv. Funct. Mater.* 2018, 28, 1706504; d) W. Tang, A. Politano, C. Guo, W. Guo, C. Liu, L. Wang, X. Chen, W. Lu, *Adv. Funct. Mater.* 2018, 28, 1801786.

[12] M. Chhowalla, H. S. Shin, G. Eda, L.-J. Li, K. P. Loh, H. Zhang, *Nat. Chem.* 2013, 5, 263.

[13] a) Q. Yao, L. Zhang, P. Bampoulis, H. J. Zandvliet, *J. Phys. Chem. C* 2018, 122, 25498; b) S. R. Das, K. Wakabayashi, M. Yamamoto, K. Tsukagoshi, S. Dutta, *J. Phys. Chem. C* 2018, 122, 17001;
c) P. Afanasiev, C. Lorentz, *J. Phys. Chem. C* 2019, 123, 7486;
d) P. Zhou, Q. Xu, H. Li, Y. Wang, B. Yan, Y. Zhou, J. Chen, J. Zhang, K. Wang, *Angew. Chem., Int. Ed.* 2015, 54, 15226; e) H. Liu, N. Han, J. Zhao, *RSC Adv.* 2015, 5, 17572; f) Z. Li, S. Yang, R. Dhall, E. Kosmowska, H. Shi, I. Chatzakis, S. B. Cronin, *ACS Nano* 2016, 10, 6836; g) M. Yamamoto, S. Dutta, S. Aikawa, S. Nakaharai, K. Wakabayashi, M. S. Fuhrer, K. Ueno, K. Tsukagoshi, *Nano Lett.* 2015, 15, 2067.

[14] P. Dreike, D. Fleetwood, D. King, D. Sprauer, T. Zipperian, *IEEE Trans Compon, Packag., Manuf. Technol.: Part A* 1994, 17, 594.

[15] E. Drioli, A. Ali, F. Macedonio, *Desalination* 2015, 356, 56.

[16] F. Macedonio, A. Politano, E. Drioli, A. Gugliuzza, *Mater. Horiz.* 2018, 5, 912.

[17] C. Gayner, K. K. Kar, *Prog. Mater. Sci.* 2016, 83, 330.

[18] P. Han, E. R. Adler, Y. Liu, L. St Marie, A. El Fatimy, S. Melis, E. Van Keuren, P. Barbara, *Nanotechnology* 2019, 30, 284004.

[19] V. O. Özçelik, H. H. Gurel, S. Ciraci, *Phys. Rev. B* 2013, 88, 045440.

[20] M. Donarelli, F. Bisti, F. Perrozzi, L. Ottaviano, *Chem. Phys. Lett.* 2013, 588, 198.

[21] Y.-S. Lan, X.-R. Chen, C.-E. Hu, Y. Cheng, Q.-F. Chen, *J. Mater. Chem. A* 2019, 7, 11134.

[22] H. Goldsmid, *Materials* 2014, 7, 2577.

[23] a) O. J. Clark, M. J. Neat, K. Okawa, L. Bawden, I. Marković, F. Mazzola, J. Feng, V. Sunko, J. M. Riley, W. Meevasana, J. Fujii, I. Vobornik, T. K. Kim, M. Hoesch, T. Sasagawa, P. Wahl, M. S. Bahramy, P. D. C. King, *Phys. Rev. Lett.* 2018, 120, 156401;
b) M. S. Bahramy, O. J. Clark, B. J. Yang, J. Feng, L. Bawden, J. M. Riley, I. Marković, F. Mazzola, V. Sunko, D. Biswas, S. P. Cooil, M. Jorge, J. W. Wells, M. Leandersson, T. Balasubramanian, J. Fujii, I. Vobornik, J. E. Rault, T. K. Kim, M. Hoesch, K. Okawa, M. Asakawa, T. Sasagawa, T. Eknapakul, W. Meevasana, P. D. C. King, *Nat. Mater.* 2018, 17, 21.

[24] a) H.-J. Noh, J. Jeong, E.-J. Cho, K. Kim, B. Min, B.-G. Park, *Phys. Rev. Lett.* 2017, 119, 016401; b) J. A. Voerman, J. C. de Boer, T. Hashimoto, Y. Huang, C. Li, A. Brinkman, *Phys. Rev. B* 2019, 99, 014510; c) A. Kjekshus, W. Pearson, *Can. J. Phys.* 1965, 43, 438.

[25] T. Finlayson, W. Reichardt, H. Smith, *Phys. Rev. B* 1986, 33, 2473.

[26] K. Kim, S. Kim, J. S. Kim, H. Kim, J. H. Park, B. I. Min, *Phys. Rev. B* 2018, 97, 165102.

[27] S. Yang, H. Cai, B. Chen, C. Ko, V. O. Ozcelik, D. F. Ogletree, C. E. White, Y. Shen, S. Tongay, *Nanoscale* 2017, 9, 12288.

[28] A. Cimino, D. Gazzoli, M. Valigi, *J. Electron Spectrosc. Relat. Phenom.* 1999, 104, 1.

[29] M. Brun, A. Berthet, J. Bertolini, *J. Electron Spectrosc. Relat. Phenom.* 1999, 104, 55.

[30] R. Bhatt, S. Bhattacharya, R. Basu, A. Singh, U. Deshpande, C. Surger, S. Basu, D. Aswal, S. Gupta, *Thin Solid Films* 2013, 539, 41.

[31] E. Li, R.-Z. Zhang, H. Li, C. Liu, G. Li, J.-O. Wang, T. Qian, H. Ding, Y.-Y. Zhang, S.-X. Du, *Chin. Phys. B* 2018, 27, 086804.

[32] H. Ibach, D. L. Mills, *Electron Energy Loss Spectroscopy and Surface Vibrations*, Academic Press, San Francisco, CA 1982.

[33] M. Ceriotti, F. Pietrucci, M. Bernasconi, *Phys. Rev. B* 2006, 73, 104304.

[34] M. A. Henderson, *Surf. Sci. Rep.* 2002, 46, 1.

[35] X. Chia, Z. Sofer, J. Luxa, M. Pumera, *ACS Appl. Mater. Interfaces* 2017, 9, 25587.

[36] Y. He, D. Yan, S. Wang, L. Shi, X. Zhang, K. Yan, H. Luo, *Energy Technol.* 7, 1900663.

[37] a) J. Greeley, T. F. Jaramillo, J. Bonde, I. Chorkendorff, J. K. Nørskov, Nat. Mater. 2006, 5, 909; b) Y. Tang, B. L. Allen, D. R. Kauffman, A. Star, J. Am. Chem. Soc. 2009, 131, 13200.

[38] Y. Fang, A. Armin, P. Meredith, J. Huang, Nat. Photonics 2019, 13, 1.

[39] Spectrum for Terrestrial 5G Networks: Licensing Developments, Global Mobile Supplier Association, 2018, https://gsacom.com/paper/spectrum-for-5g-jan-2019/.

[40] G. Fiori, F. Bonaccorso, G. Iannaccone, T. Palacios, D. Neumaier, A. Seabaugh, S. K. Banerjee, L. Colombo, Nat. Nanotechnol. 2014, 9, 768.

[41] D. Krasnozhon, D. Lembke, C. Nyffeler, Y. Leblebici, A. Kis, Nano Lett. 2014, 14, 5905.

[42] H. Wang, X. Wang, F. Xia, L. Wang, H. Jiang, Q. Xia, M. L. Chin, M. Dubey, S.-J. Han, Nano Lett. 2014, 14, 6424.

[43] G. Anemone, A. Al Taleb, A. Castellanos-Gomez, D. Farías, 2D Mater. 2018, 5, 035015.

[44] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, L. Michele, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzcovitch, J. Phys.: Condens. Matter 2009, 21, 395502.

[45] a) J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1996, 77, 3865; b) V. Barone, M. Casarin, D. Forrer, M. Pavone, M. Sambi, A. Vittadini, J. Comput. Chem. 2009, 30, 934.

[46] H. J. Monkhorst, J. D. Pack, Phys. Rev. B 1976, 13, 5188.