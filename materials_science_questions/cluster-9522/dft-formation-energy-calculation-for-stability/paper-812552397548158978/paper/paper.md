# Electronic Band Engineering via $MI_3$ (M = Sb, Bi) Doping Remarkably Enhances the Air Stability of Perovskite $CsSnI_3$

Myeongjeong Lee, Byeongjun Yoo, Jino Im, Taeghwan Hyeon, and In Chung*

## ABSTRACT:
$CsSnI_3$ is a representative all-inorganic and less toxic perovskite material. However, extreme structural and chemical instability of perovskite $CsSnI_3$ makes its optoelectronic applications highly challenging. Upon exposure to air and moisture, it immediately undergoes a phase transition to a thermodynamically more stable, but optoelectronically inactive, one-dimensional polymorph near ambient temperature and ultimately deforms into $Cs_2SnI_6$. To prohibit this undesirable process, perovskite $CsSnI_3$ has to be stored and treated restrictively in an inert atmosphere and encapsulated hermitically. Here, we demonstrate an unusual strategy to markedly enhance the air stability of perovskite $CsSnI_3$. Namely, $MI_3$ (M = Sb, Bi) doping modifies the electronic band structure of perovskite $CsSnI_3$. As a result, it is remarkable that its heat of formation reduces, being lower than that of its competing polymorph. Accordingly, otherwise thermodynamically unfavorable perovskite $CsSnI_3$ becomes more stable than the latter energetically, thereby preventing the undesirable phase transition. $SbI_3$ (3 mol %)-doped $CsSnI_3$ retains 96% of its perovskite structure, whereas pristine $CsSnI_3$ retains only 12% after 12 h of exposure to air with 45−55% relative humidity. $MI_3$ doping also reduces the energy band gap of perovskite $CsSnI_3$. We employed first-principles density functional theory calculations to explain the origin of the enhanced stability and red-shifted band gaps. Our current work demonstrates that electronic band structure engineering by chemical doping can be an effective means of controlling the phase stability of polymorphs, which are otherwise difficult to stabilize or unattainable. This strategy can be widely applied to materials with low stability but high technological importance.

![](./images/812552397548158978_1.jpg)

## KEYWORDS:
halide perovskite, lead-free, tin, phase transition, air stability

---

## 1. INTRODUCTION

Metal halide compounds with a perovskite structure have been extensively studied for optoelectronic applications such as solar light harvesting and light-emitting diodes mainly due to their suitable band gaps $(E_g)$, high absorption coefficients, excellent carrier mobilities, long carrier lifetimes, and facile processability for device fabrication. $^{1−5}$ For example, solar cell devices using methylammonium lead iodide $(MAPbI_3)$ and formamidinium lead iodide $(FAPbI_3)$ as light absorbers have achieved power conversion efficiencies (PCEs) higher than 20%. $^{6−8}$ However, these materials are readily hydrolyzed in contact with moisture and leach carcinogenic $Pb^{2+}$ cations. $^{9−11}$ Accordingly, replacing Pb by less toxic elements with the preservation of many of their interesting properties has been the most difficult task. $^{12,13}$ Suggested less toxic candidates include tin(II)-$^{14−16}$ and germanium(II)-based perovskites, $^{16,17}$ double perovskites $A_2M^IM^{III}X_6$ (A and $M^I$ = formally monovalent cations; $M^{III}$ = trivalent metal ions; X = halogens), $^{18,19}$ vacancy-ordered double perovskites $A_2M^{IV}X_6$ ($M^{IV}$ = formally tetravalent metal ions), $^{20−22}$ layered perovskite derivatives $A_3M_2^{III}X_9$, $^{23−25}$ and copper-based perovskites. $^{20,26,27}$ Among them, tin(II)-based halide perovskite materials are highly promising given their similar optoelectronic properties to lead-based analogues. $^{28,29}$ Their narrower band gap $(E_g)$ and greater charge carrier mobility make them even more attractive for photovoltaics than the lead-based counterparts. Indeed, perovskite solar cells (PSCs) based on $FASnI_3$ with incorporated guanidinium cations achieved record-high PCEs of $\sim$10% for lead-free PSCs. $^{30}$

However, typical organic cationic molecules such as $MA^+$ and $FA^+$ employed in high-efficiency PSCs show inherent thermal instability, high volatility, and sensitivity to moisture and ultraviolet light, seriously degrading the overall long-term stability of their PSCs. $^{31−33}$ To address this, developing all inorganic analogues has been a sought goal in the relevant research community. $^{34−38}$ $CsSnI_3$ can be a good candidate for this purpose given its excellent photophysical properties and

---

Received: June 24, 2020
Accepted: October 8, 2020

resistance to decomposition by heat and ultraviolet irradiation. $^{29-42}$ However, electro-optic devices using $CsSnI_{3}$ have been so far underdeveloped. The main reason is the structural instability of $CsSnI_{3}$, bringing about ultimate and rapid chemical degradation in air. In fact, $CsSnI_{3}$ can be stabilized in two distinct polymorphs near ambient temperature. The black polymorph (B-$\gamma$ phase) adopts a distorted three-dimensional (3D) perovskite structure with a direct optical $E_{g}$ of 1.3 eV and strong photoluminescence (PL) at $\sim$950 nm. The yellow polymorph (Y phase) crystallizes in a one-dimensional (1D) double-chain structure consisting of edge-sharing $[SnI_{3}]$ octahedra with an indirect $E_{g}$ of 2.5 eV. $^{39}$ Note that only the B-$\gamma$ phase is suitable for applications in photovoltaics and light-emitting diodes. The evolution of this polymorphism arises from too small $Cs^{+}$ cations to stably support the perovskite framework comprising Sn and I atoms in contrast to much larger $MA^{+}$ and $FA^{+}$ cations. $^{43}$ The phase transition from the B-$\gamma$ to Y phase gives a significant 6.6% increase in density. $^{39}$ Indeed, the B-$\gamma$ phase has slightly higher formation energy than the competing Y phase, being thermodynamically less stable near ambient temperature. $^{43}$ Exposure to air or moisture prompts the metastable B-$\gamma$ phase to immediately undergo a spontaneous phase transition to the Y phase. The latter, if still pure, can be reversed to the former by heating at $\sim$150 $^{\circ}$C under an inert atmosphere. $^{39}$ Otherwise, once the Y phase forms, it irreversibly oxidizes to a discrete molecular compound $Cs_{2}Sn^{IV}I_{6}$, which is the ultimate decomposition process. $^{21,44}$ Note that $Sn^{4+}$ is thermodynamically slightly more stable than $Sn^{2+}.^{45}$ Given the degradation mechanism of the B-$\gamma$ phase, it is essential to block its transition pathway to the Y phase. $SnF_{2}$ doping has been the best-known solution for this purpose so far, but the $SnF_{2}$-doped B-$\gamma$ phase is completely decomposed in 4 h upon exposure to air. $^{44}$ On this account, it is of prime importance to improve the stability of this highly promising material for practical optoelectronic applications.

Herein, we report that $MI_{3}$ (M = Sb, Bi) doping in $CsSnI_{3}$ markedly enhances the structural stability of the B-$\gamma$ phase by preventing the phase transition to the technologically undesirable Y phase. It significantly modifies the electronic structure of the B-$\gamma$ phase. Hence, the heat of formation of the B-$\gamma$ phase becomes lower than that of the Y phase, thereby the former being energetically more favorable. As a result, after exposure to air with 45−55% relative humidity for 12 h, 3 mol % $SbI_{3}$- and $BiI_{3}$-doped B-$\gamma$ phases preserve 96 and 77% of their perovskite structure, respectively, while the pristine one retains only 12%. After a week, the $SbI_{3}$-doped B-$\gamma$ phase still maintains $\sim$50% of the perovskite structure. We clarified that the decomposition of the B-$\gamma$ phase is driven by moisture rather than oxygen in air according to the controlled stability test under both humid and dry air. Importantly, we show that electronic structure engineering finely controlled by chemical doping can change the intrinsic chemical stability of the materials.

## 2. EXPERIMENTAL SECTION

### 2.1. Reagents.
The following reagents were used as received unless noted otherwise: CsBr (99.999%, Alfa-Aesar), CsI (99.998%, Alfa-Aesar), MABr (MA = methylammonium) (>99%, Dyesol), $SbI_{3}$ (99.999%, Alfa-Aesar), $BiBr_{3}$ (99.999%, Alfa-Aesar), $BiI_{3}$ (99.999%, Alfa-Aesar), $PbBr_{2}$ (99.999% Alfa-Aesar), $InI_{3}$ (99.998%, Sigma-Aldrich), $I_{2}$ (99.999%, Sigma-Aldrich), and anhydrous $N,N$-dimethylformamide (DMF) (99.8%, Sigma-Aldrich). $SnI_{2}$ was prepared according to a previous report. $^{28}$ $SnBr_{2}$ (Sigma-Aldrich) and $SbBr_{3}$ (99.999%, Alfa-Aesar) were further purified by thermal recrystallization before use.

### 2.2. Synthesis.
All reagents were handled in an Ar-filled glovebox in which the levels of $H_{2}O$ and $O_{2}$ were kept at 0 and <1 ppm, respectively. To obtain phase-pure pristine and $x$ mol % $MX_{3}$-doped $CsSnX_{3}$ (M = Sb, Bi; X = Br, I), a reaction mixture of CsX, $SnX_{2}$, and $MX_{3}$ with a molar ratio of $CsX:SnX_{2}:MX_{3}$ = 1:1:0.01$x$ was loaded into an evacuated fused silica tube ($\sim$10$^{-4}$ Torr) and reacted at 450 $^{\circ}$C for 5 h, followed by natural cooling to room temperature. We also prepared the control samples doped with 4.5 mol % $I_{2}$, 3 mol % $SnI_{2}$, and 3 mol % $InI_{3}$, respectively, using a similar procedure. The reaction temperature for control pristine $MASnBr_{3}$ and its $MBr_{3}$-doped samples for comparison was 200 $^{\circ}$C.

### 2.3. Powder X-ray Diffraction (PXRD).
PXRD patterns were collected using Cu $K\alpha$ ($\lambda$ = 1.5418 Å) graphite monochromatized radiation on a SmartLab Rigaku powder X-ray diffractometer operating at 40 kV and 20 mA. The Rietveld refinement was used for obtaining lattice parameters and quantitative analysis for samples employing the HighScore Plus software suite. $^{46}$

### 2.4. Stability Tests.
The stability test under "humid air" was performed by exposing pristine and doped B-$\gamma$ $CsSnI_{3}$ powders ($\sim$0.5 g) with a relative humidity of 45−55%. Humidity was measured by a humidity temperature meter (TES-1364). The stability test under "dry air" was performed under an 80:20 (v/v) mixed flow of $N_{2}$ and $O_{2}$ with a Schlenk line. Pristine and doped B-$\gamma$ $CsSnI_{3}$ powders ($\sim$0.5 g) were individually placed in 100 mL round-bottom flasks with magnetic shaking under a $N_{2}$ and $O_{2}$ flow for 24 h. Samples were subsequently analyzed by PXRD.

### 2.5. Solid-State Optical Absorption Spectroscopy.
Optical diffuse reflectance spectra were recorded at room temperature using a Shimadzu UV-3101 PC spectrometer equipped with an integrating sphere operating in the 200−2500 nm region. $BaSO_{4}$ was used as a 100% reflectance reference. The reflectance with respect to wavelength data generated was employed to estimate $E_{g}$ of samples after converting reflectance into absorption data by the Kubelka−Munk relation $\alpha/S = (1 - R)^{2}/(2R)$, where $\alpha$ and $S$ are the absorption and scattering coefficients, respectively, and $R$ is the reflectance. $^{47-49}$

### 2.6. Optical Emission Measurements.
Pristine and doped samples were dissolved in anhydrous DMF at a concentration of 30 wt % and spin-coated onto quartz substrates at 4000 rpm for 30 s. Deposited films were annealed at 80 $^{\circ}$C for 10 min. Emission spectra were collected with a high-resolution photoluminescence spectrophotometer (LabRAM HR-800) in air, excited by a 514 nm laser diode. To collect PL signals at 100 K, samples were kept in a vacuum and cooled with a cryostat.

### 2.7. Computational Details.
First-principles electronic structure calculations were performed within the density functional theory (DFT) scheme. We utilized a plane-wave basis set with a 350 eV of cutoff energy. The cutoff energy was tested with respect to the convergence of energy difference between the black and yellow phases. We also employed the projector augmented wave method $^{50}$ implemented in the Vienna Ab initio Simulation Package. $^{51,52}$ For the exchange−correlation functional, the generalized gradient approximation was adopted within the Perdew−Burke−Ernzerhof for solids (PBEsol) formalism. $^{53}$ We employed a $2 \times 2 \times 2$ supercell accommodating 32 formula units to mimic the 3 mol % $MI_{3}$-doped $CsSnI_{3}$ ($Cs_{32}Sn_{31}M_{1}I_{97}$). To figure out the change in thermodynamic stability upon doping, we calculated the heat of formation ($\Delta H_{F}$) of both black and yellow phases, following the formula, $\Delta H_{F} = E_{total} - \sum n_{i}\mu_{i}$, where $E_{total}$, $n_{i}$, and $\mu_{i}$ are the DFT total energy of the considered system, the number of atoms of chemical element $i$, and the DFT energy of element $i$ in the reference phase. To understand the origin of the band gap shift upon $MI_{3}$ doping, we performed electronic band structure calculations for black phases. For accurate prediction of band gap, we employed a hybrid functional within the form of the Perdew−Burke−Ernzerhof hybrid functional (PBE0) $^{54}$ and spin−orbit coupling. Electronic band structures of doped $CsSnI_{3}$ were plotted within a rigid shift utilizing the calculated band gap at the $\Gamma$ point.

![](./images/812552397548158978_2.jpg)

Figure 1. XRD patterns of $x$ mol % ($x = 1, 2, 3$) (a) SbI₃- and (b) BiI₃-doped CsSnI₃. The cell volume with respect to the doping concentration is shown in the insets of (a) and (b). (c) XRD patterns of the B-$\gamma$ phase with a higher doping concentration, showing the precipitation of the secondary phase of SnI₂ (orange asterisk) and Cs₃Sb₂I₉ (blue asterisk). Standard diffraction patterns of B-$\gamma$ CsSnI₃ and Cs₃Sb₂I₉ from the Inorganic Crystal Structure Database (ICSD) codes 262926 and 89695, respectively, and experimental pattern of synthesized SnI₂ are given for comparison. Major Bragg peaks are indexed.

![](./images/812552397548158978_3.jpg)

Figure 2. XRD patterns of (a) pristine and 3 mol % (b) SbI₃- and (c) BiI₃-doped B-$\gamma$ phase with respect to exposure time in 45−55% humid air. Standard XRD patterns of the Y phase and Cs₂SnI₆ are given for comparison from the ICSD codes 262927 and 22105, respectively. (d) Illustration of the deformation process of the B-$\gamma$ phase (black solid line) in air. MI₃ (M = Sb, Bi) doping effectively suppresses the phase transition from the B-$\gamma$ to the Y phase (orange dashed line).

### 3. RESULTS AND DISCUSSION

Pure B-$\gamma$ CsSnI₃ can be obtained by reacting a stoichiometric mixture of CsI and SnI₂ in an evacuated container at 450 °C. However, even a tiny amount of impurity present in the starting reagents tends to readily prompt the evolution of the Y phase.³⁹,⁴⁴ Especially, high-purity SnI₂ was prepared according to a previous report.²⁸ $x$ mol % MI₃-doped samples were similarly synthesized by melting a reaction mixture of CsI:SnI₂:MI₃ = 1:1:0.01$x$. All products crystallize in the orthorhombic $Pnma$ structure of B-$\gamma$ CsSnI₃ (Figures 1 and S1). The cell volume expands gradually with increasing MI₃ concentration, indicating that the added dopants of up to 3 mol % can be successfully incorporated into the perovskite lattice without a secondary phase within the detection limit of the laboratory X-ray diffractometer (Figure 1a,b and Table S1). A higher doping concentration gives rise to the precipitation of the secondary phase: SnI₂ and Cs₃Sb₂I₉ for SbI₃ doping and SnI₂ for BiI₃ doping (Figure 1c).

To investigate the effect of MI₃ doping on the stabilization of the B-$\gamma$ phase, we intentionally exposed the pristine and doped B-$\gamma$ CsSnI₃ samples to ambient air with a relative humidity of 45−55% and traced their structural changes with respect to exposure time. This condition is designated as humid air hereafter. According to the XRD patterns, the pristine B-$\gamma$ phase in humid air undergoes a two-step deformation process: (1) immediate structural transformation to the Y phase and (2) subsequent irreversible oxidization of the Y phase to discrete molecular Cs₂SnᴵⱽI₆ (Figure 2a,d), which is consistent with previous reports.³⁹,⁴⁴ Specifically, the wt % of the Y phase increases abruptly in 2 h, and three phases coexist with a wt % ratio of B-$\gamma$:Y:Cs₂SnI₆ = 50.0:34.6:15.4 (Figures 2a and 3). After 12 h, the wt % of Cs₂SnI₆ surges

![](./images/812552397548158978_4.jpg)

Figure 3. Content variation of the (a) B-$\gamma$ phase, (b) Y phase $CsSnI_3$, and (c) $Cs_2SnI_6$ in pristine and $MI_3$-doped samples with respect to the exposure time in air with 45−55% relative humidity.

while that of the Y phase only slightly increases, indicating that the transformed Y phase is continuously degraded to $Cs_2SnI_6$;
40 h later, the wt % ratio of the Y phase and $Cs_2SnI_6$ is approximately 17.0:79.9 with the negligible presence of the B-$\gamma$ phase.

In contrast, $MI_3$-doped samples show much greater resistance to the phase transition and oxidation process. Two hours after air exposure, 3 mol % $SbI_3$- and $BiI_3$-doped samples give only 1 and 5 wt % Y phase, respectively, without the oxidized form of $Cs_2SnI_6$ (Figures 2b,c and 3). This stabilization effect is surprising given that only 50% of the pristine B-$\gamma$ $CsSnI_3$ survives after 2 h in the same conditions. This result clearly shows that $MI_3$ doping effectively suppresses the unfavorable phase transition of the B-$\gamma$ to the competing Y phase. After 12 h, the $SbI_3$- and $BiI_3$-doped samples contain only 2.0 and 12.1 wt % $Cs_2SnI_6$, respectively, in contrast to 50.6 wt % in the pristine sample (Figure 3c). After 1 week, the $SbI_3$-doped sample retains the 47.7 wt % B-$\gamma$ phase (Figure S2a,c).

To confirm the unique stabilization effect of $SbI_3$ and $BiI_3$ for perovskite $CsSnI_3$, we synthesized the control samples with a dopant of 4.5 mol % $I_2$, 3 mol % $SnI_2$, and 3 mol % $InI_3$, respectively. Additional $I_2$ oxidized $Sn^{2+}$ to give $SnI_4$, a secondary phase with major B-$\gamma$ phase (Figure S3). Additional $SnI_2$ appeared to yield the pure B-$\gamma$ phase, but it rapidly transformed into the Y phase as observed for the pristine sample (Figure S4). Additional $InI_3$ could not stabilize the B-$\gamma$ phase, instead gave rise to the Y phase without exposure to air (Figure S5).

To further understand the deformation process, we examined the structural transition of the pristine and 3 mol % $MI_3$-doped B-$\gamma$ phase under dry air (Figure S6). Namely, samples were stored under an 80:20 (v/v) mixed stream of $N_2$ and $O_2$ gases in the absence of moisture (see Section 1 for details). This condition is designated as dry air hereafter. All samples show a much slower rate of phase transitions in dry air than in typical humid air with moisture (Figures S6 and S7). In 24 h, the pristine sample under dry air shows a wt % ratio of B-$\gamma$:Y:$Cs_2SnI_6$ = 36.2:60.8:3.0 in contrast to 5.9:22.7:71.4 under humid air. In the same duration under dry air, both the Y phase and $Cs_2SnI_6$ are not observed in the $SbI_3$-doped sample, and only a small fraction of Y phase (5 wt %) is formed without $Cs_2SnI_6$ in the $BiI_3$-doped sample. The phase distribution (wt % ratio) of B-$\gamma$:Y:$Cs_2SnI_6$ under humid air in 24 h is 93.3:2.2:4.5 and 56.5:20.1:23.4 for $SbI_3$- and $BiI_3$-doped samples, respectively. These observations clearly indicate that moisture in air mainly activates both the phase transition of the B-$\gamma$ to Y phase and the subsequent oxidation process. This result can be understood in light of highly ionic characteristics of the $Cs^+[SnI_3]^-$ compound.

The solid-state optical absorption spectra of $MI_3$-doped $CsSnI_3$ samples reveal a large red shift in absorption edges from 1.24 eV of the pristine sample, implying a substantial alteration in their electronic band structures (Figure 4a). $SbI_3$ doping gradually reduces the optical band gap $(E_g)$ from 1.17 to 1.14 eV with increasing doping rate from 1 to 3 mol %. $BiI_3$ induces a greater reduction in $E_g$ of $CsSnI_3$ than $SbI_3$. All $BiI_3$-doped samples with a doping rate from 1 to 3 mol % show nearly the same $E_g$ at 0.80 eV. Importantly, we found that the addition of $MX_3$ (X = halogens) to other tin-based halide perovskite compounds similarly tunes $E_g$ values. We introduced $SbX_3$ and $BiX_3$ with the same X atom as that in the host perovskite framework to eliminate possible influence from anions. We carefully controlled the doping concentration to avoid precipitation of the secondary phase (Figures S8 and S9). For example, addition of 2 mol % $BiBr_3$ considerably decreases the $E_g$ of $CsSnBr_3$ and $MASnBr_3$ from 1.75 to 1.16 eV and 2.05 to 1.41 eV, respectively (Figure S10). Similar to the observation in $CsSnI_3$, the $E_g$ reduction by 2 mol % $SbBr_3$ doping is relatively small: from 1.75 to 1.62 eV for $CsSnBr_3$ and 2.05 to 1.93 eV for $MASnBr_3$. However, these dopants

![](./images/812552397548158978_5.jpg)

Figure 4. (a) Normalized optical absorption spectra of the $MI_3$-doped B-$\gamma$ phase. Dotted lines are a guide to show absorption edges of samples. (b) Variation in the calculated heat of formation $(\Delta H_F)$ of the B-$\gamma$ and Y phases by 3 mol % $SbI_3$ and $BiI_3$ doping, respectively. The reversed phase stability for B-$\gamma$ and Y polymorphs by $MI_3$ doping is clearly seen.

have much less solubility in lead-based perovskite compounds. For example, addition of only 1 mol % either $SbBr_3$ or $BiBr_3$ addition to $CsPbBr_3$ generates a $CsPb_2Br_5$ precipitate (Figure S11). Thus, their $E_g$ tuning effect is unclear. The product for the former has the same $E_g$ as the pristine sample at 2.25 eV, and that for the latter shows a decreased $E_g$ at 2.00 eV (Figure S12). In the case of replacing Pb by Sb or Bi, the $MAPb_{0.99}Sb_{0.01}I_3$ film shows a slightly increased $E_g$ of 1.58 from 1.55 eV, and $CsPb_{0.975}Bi_{0.025}Br_3$ single crystals exhibit a decreased $E_g$ of 1.77 from 2.21 eV according to previous reports. $^{55-57}$

Despite the reduced $E_g$, $MI_3$-doped B-$\gamma$ phases exhibit maximum PL intensity at nearly the same wavelength ($\lambda_{max}$) as the pristine sample. Pristine B-$\gamma$ $CsSnI_3$ exhibits a strong PL ($\lambda_{max} = 935$ nm) at room temperature (RT) (Figure S13a). However, the PL intensity of $MI_3$-doped B-$\gamma$ phases decreases significantly with higher doping concentration; 0.1 mol % $SbI_3$- and $BiI_3$-doped samples exhibit considerably suppressed PL signals at $\lambda_{max}$ of 933 and 930 nm (Figure S13a), respectively, and those with 3 mol % dopants emit almost negligible PL. To observe the PL signal of $MI_3$-doped B-$\gamma$ phases by eliminating the thermal quenching effect, $^{58}$ the measurement temperature was lowered to 100 K. The 3 mol % $SbI_3$- and $BiI_3$-doped samples exhibit a weak PL at $\lambda_{max}$ of 955 and 953 nm, respectively, at 100 K, which is slightly red-shifted from those at RT (Figure S13b). This difference is attributed to the temperature-dependent emission behavior of B-$\gamma$ $CsSnI_3$ as reported previously. $^{59}$ The nearly invariant $\lambda_{max}$ by $MI_3$ doping implies that their emission mechanism is similar to that of the pristine sample, arising from the defects formed by Sn vacancies. $^{28,39}$

To elucidate the unusual effects of $MI_3$ doping on perovskite $CsSnI_3$ for phase stability and optical properties, we performed first-principles calculations for total energies per formula unit (f.u.) and electronic band structures within the DFT formalism. We employed a $2 \times 2 \times 2$ supercell for the 3 mol % $MI_3$-doped $CsSnI_3$ ($Cs_{32}Sn_{31}M_1I_{97}$). M atoms are supposed to be located at the Sn site given the ionic size $^{60,61}$ and Sn and the intrinsically high concentration of Sn vacancies in $CsSnI_3$. $^{39}$ Additional I atoms are located at the interstitial sites for charge neutrality given the formal charge of $Sn^{2+}$ and $M^{3+}$. For pristine $CsSnI_3$, the Y phase has a slightly lower calculated heat of formation ($\Delta H_F$) ($-4.7229$ eV/f.u.) than the B-$\gamma$ phase ($-4.7134$ eV/f.u.) (Figure 4b), consistent with previous theoretical calculations and experimental observations for the phase transition. $^{43,44}$ It is remarkable that the $\Delta H_F$ trend between the B-$\gamma$ and Y phases is reversed by $MI_3$ doping. For the $BiI_3$-doped $CsSnI_3$, the calculated $\Delta H_F$ is $-4.6960$ and $-4.6840$ eV/f.u. for the B-$\gamma$ and Y phases, respectively. For the $SbI_3$-doped $CsSnI_3$, the difference in $\Delta H_F$ is even greater: $-4.6867$ and $-4.6682$ eV/f.u. for the B-$\gamma$ and Y phases, respectively. Namely, $SbI_3$ better stabilizes the B-$\gamma$ phase than $BiI_3$. As a consequence, the B-$\gamma$ phase becomes more thermodynamically favorable than the Y phase by this chemical doping. These results are consistent with the experimental observations for the phase transition and deformation processes of B-$\gamma$ $CsSnI_3$.

![](./images/812552397548158978_6.jpg)

Figure 5. Local atomic structure of (a) $SbI_3$- and (b) $BiI_3$-doped B-$\gamma$ and (c) $SbI_3$- and (d) $BiI_3$-doped Y phases according to the DFT results.

![](./images/812552397548158978_7.jpg)

Figure 6. Calculated electronic band structures and projected density of states (PDOS) of 3 mol % (a) $SbI_3$- and (b) $BiI_3$-doped B-$\gamma$ phase. The red arrow in the electronic band structures indicates the new band induced by doping.

The origin of the reversed $\Delta H_F$ can be attributed to the geometric difference of an additional I atom, introduced by $MI_3$ doping, near a Bi or Sb atom in the B-$\gamma$ and Y phases. According to the DFT calculation, the additional I atom forms a bridging bond between Bi (or Sb) and the nearest Sn atoms in the B-$\gamma$ phase (Figure 5a,b), whereas it only bonds with Bi (or Sb) as a terminal atom in the Y phase (Figure 5c,d). Because a single-bonded terminal atom is less stable than a bridging atom, the $MI_3$-doped $CsSnI_3$ B-$\gamma$ phase is more stable than the corresponding Y phase. The additional I atom at the terminal position in the Y phase induces a highly localized state inside the band gap.

A previous first-principles DFT calculation for the pristine B-$\gamma$ phase shows that both the valence band maximum (VBM) and the conduction band minimum (CBM) occur at the $\Gamma$

point, and their p-p mixing gives rise to a direct $E_{g}^{39}$
Surprisingly, both $SbI_{3}$ and $BiI_{3}$ doping develops new intermediate bands below the conduction band (CB) of the B-$\gamma$ phase, and these bands are mainly contributed by the 6p-orbital of Sb and Bi (Figure 6). New bands in the $BiI_{3}$-doped B-$\gamma$ phase are isolated from the original CB. On the other hand, those in the $SbI_{3}$-doped one are located in the higher energy level, consequently overlapping with the original CB. The deviation in the energy level of the new bands developed by doping is attributed to the electron affinity difference of Sb and Bi. These modulations in electronic band structures by doping explain our experimental observations for their reduced $E_{g}$. Because the red-shifted absorption onset can be related to the optical transition from the VBM to the new bands, a shift in absorption edge is much greater by $BiI_{3}$ than $SbI_{3}$ doping. The calculated electronic band structures also help understand quenched PL by $MI_{3}$ doping. Excited electrons may be relaxed to the new bands by doping, possibly decreasing the PL intensity. The doped B-$\gamma$ phase maintains the direct $E_{g}$ nature at the $\Gamma$ point, which is essential for many optoelectronic applications.

## 4. CONCLUSIONS
We synthesized $MI_{3}$ (M = Sb, Bi)-doped $CsSnI_{3}$ perovskite materials and compared their air stability with pristine under air and moisture. We surprisingly found that $MI_{3}$ chemical doping stabilizes the perovskite structure of $CsSnI_{3}$ significantly by inhibiting the undesirable phase transition to its competing one-dimensional polymorph near ambient temperature. For example, the 3 mol % $SbI_{3}$-doped $CsSnI_{3}$ perovskite phase retains 96% of its structure, whereas pristine does merely 12% upon exposure to air with 45−55% relative humidity for 12 h. Indeed, it is essential to block the phase transition to the one-dimensional polymorph given that it leads to ultimate decomposition to the oxidized phase of $Cs_{2}SnI_{6}$. However, effective solutions have been elusive before this work.

Our theoretical calculations within the density functional theory regime show that $MI_{3}$ doping alters the electronic structure of perovskite $CsSnI_{3}$. This unexpectedly causes to decrease its heat of formation lower than that of the competing one-dimensional polymorph. As a consequence, the perovskite phase of the doped $CsSnI_{3}$ becomes thermodynamically more stable than the latter in contrast to the opposite trend in pristine $CsSnI_{3}$, thereby displaying substantially enhanced air stability.

It is remarkable that the extremely unstable $CsSnI_{3}$ perovskite phase can be markedly stabilized by engineering the electronic band structure by a few mol % chemical doping despite the intrinsic structural disadvantage. Consequently, this can improve its processability for practical device fabrication processes. This achievement definitely calls for an extensive study of the generation of new bands by a wide range of dopants, possibly enhancing the structural stability and optoelectronic performance simultaneously.

## ■ ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge at
https://pubs.acs.org/doi/10.1021/acsaem.0c01484.

Lattice parameters of pristine and doped $CsSnI_{3}$; powder XRD pattern of pristine $CsSnI_{3}$; $MI_{3}$-doped $CsSnI_{3}$ upon prolonged exposure to humid air and dry air; powder
XRD patterns of $I_{2^{-}}$, $SnI_{2^{-}}$, and $InI_{3}$-doped $CsSnI_{3}$; powder XRD patterns and absorption spectra of pristine and $MBr_{3}$-doped $CsSnBr_{3}$, $MASnBr_{3}$, and $CsPbBr_{3}$; and PL spectra of pristine and doped $CsSnI_{3}$ (PDF)

## ■ AUTHOR INFORMATION
### Corresponding Author
In Chung − Center for Nanoparticle Research, Institute for Basic Science (IBS), Seoul 08826, Republic of Korea; School of Chemical and Biological Engineering, and Institute of Chemical Processes, Seoul National University, Seoul 08826, Republic of Korea; orcid.org/0000-0001-6274-3369;
Email: inchung@snu.ac.kr

### Authors
Myeongjeong Lee − School of Chemical and Biological Engineering, and Institute of Chemical Processes, Seoul National University, Seoul 08826, Republic of Korea; orcid.org/0000-0002-4873-544X

Byeongjun Yoo − Center for Nanoparticle Research, Institute for Basic Science (IBS), Seoul 08826, Republic of Korea; School of Chemical and Biological Engineering, and Institute of Chemical Processes, Seoul National University, Seoul 08826, Republic of Korea

Jino Im − Chemical Data-Driven Research Center, Korea Research Institute of Chemical Technology, Daejeon 34114, Republic of Korea

Taeghwan Hyeon − Center for Nanoparticle Research, Institute for Basic Science (IBS), Seoul 08826, Republic of Korea; School of Chemical and Biological Engineering, and Institute of Chemical Processes, Seoul National University, Seoul 08826, Republic of Korea; orcid.org/0000-0001-5959-6257

Complete contact information is available at:
https://pubs.acs.org/10.1021/acsaem.0c01484

### Notes
The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS
This research was supported by the Institute for Basic Science (IBS-R006-D1) and Technology Development Program to Solve Climate Changes (NRF-2015M1A2A2058362 and NRF-2015M1A2A2058130) through NRF (National Research Foundation of Korea) funded by the Ministry of Science and ICT.

## ■ REFERENCES
(1) Gao, L.; Quan, L. N.; García de Arquer, F. P.; Zhao, Y.; Munir, R.; Proppe, A.; Quintero-Bermudez, R.; Zou, C.; Yang, Z.; Saidaminov, M. I.; Voznyy, O.; Kinge, S.; Lu, Z.; Kelley, S. O.; Amassian, A.; Tang, J.; Sargent, E. H. Efficient near-infrared light-emitting diodes based on quantum dots in layered perovskite. Nat. Photonics 2020, 14, 227−233.

(2) Becker, M. A.; Vaxenburg, R.; Nedelcu, G.; Sercel, P. C.; Shabaev, A.; Mehl, M. J.; Michopoulos, J. G.; Lambrakos, S. G.; Bernstein, N.; Lyons, J. L.; Stöferle, T.; Mahrt, R. F.; Kovalenko, M. V.; Norris, D. J.; Rainò, G.; Efros, A. L. Bright triplet excitons in caesium lead halide perovskites. Nature 2018, 553, 189−193.

(3) Lim, J. W.; Kwon, H.; Kim, S. H.; You, Y.-J.; Goo, J. S.; Ko, D.-H.; Lee, H. J.; Kim, D.; Chung, I.; Kim, T. G.; Kim, D. H.; Shim, J. W. Unprecedentedly high indoor performance (efficiency >34%) of perovskite photovoltaics with controlled bromine doping. Nano Energy 2020, 75, No. 104984.

(4) Said, A. A.; Xie, J.; Zhang, Q. Recent progress in organic electron transport materials in inverted perovskite solar cells. *Small* **2019**, *15*, No. 1900854.

(5) Gu, P.-Y.; Wang, N.; Wu, A.; Wang, Z.; Tian, M.; Fu, Z.; Sun, X. W.; Zhang, Q. An azaacene derivative as promising electron-transport layer for inverted perovskite solar cells. *Chem. − Asian J.* **2016**, *11*, 2135−2138.

(6) National Renewable Energy Laboratory. Best Research-Cell Efficiency Chart. https://www.nrel.gov/pv/cell-efficiency.html ( accessed May 22 , 2020 ).

(7) Min, H.; Kim, M.; Lee, S.-U.; Kim, H.; Kim, G.; Choi, K.; Lee, J. H.; Seok, S. I. Efficient, stable solar cells by using inherent bandgap of $\alpha$-phase formamidinium lead iodide. *Science* **2019**, *366*, 749−753.

(8) Bai, S.; Da, P.; Li, C.; Wang, Z.; Yuan, Z.; Fu, F.; Kawecki, M.; Liu, X.; Sakai, N.; Wang, J. T.-W.; Huettner, S.; Buecheler, S.; Fahlman, M.; Gao, F.; Snaith, H. J. Planar perovskite solar cells with long-term stability using ionic liquid additives. *Nature* **2019**, *571*, 245−250.

(9) Li, J.; Cao, H.-L.; Jiao, W.-B.; Wang, Q.; Wei, M.; Cantone, I.; Lü, J.; Abate, A. Biological impact of lead from halide perovskites reveals the risk of introducing a safe threshold. *Nat. Commun.* **2020**, *11*, No. 310.

(10) Ju, M.-G.; Chen, M.; Zhou, Y.; Dai, J.; Ma, L.; Padture, N. P.; Zeng, X. C. Toward eco-friendly and stable perovskite materials for photovoltaics. *Joule* **2018**, *2*, 1231−1241.

(11) Wang, R.; Mujahid, M.; Duan, Y.; Wang, Z.-K.; Xue, J.; Yang, Y. A Review of perovskites solar cell stability. *Adv. Funct. Mater.* **2019**, *29*, No. 1808843.

(12) Ke, W.; Kanatzidis, M. G. Prospects for low-toxicity lead-free perovskite solar cells. *Nat. Commun.* **2019**, *10*, No. 965.

(13) Lee, M.; Kim, D.; Lee, Y. K.; Koo, H.; Lee, K. T.; Chung, I. Indene-$C_{60}$ bisadduct electron-transporting material with the high LUMO level enhances open-circuit voltage and efficiency of tin-based perovskite solar cells. *ACS Appl. Energy Mater.* **2020**, *3*, 5581−5588.

(14) Ke, W.; Stoumpos, C. C.; Kanatzidis, M. G. "Unleaded" perovskites: status quo and future prospects of tin-based perovskite solar cells. *Adv. Mater.* **2019**, *31*, No. 1803230.

(15) Chung, I.; Lee, B.; He, J.; Chang, R. P. H.; Kanatzidis, M. G. All-solid-state dye-sensitized solar cells with high efficiency. *Nature* **2012**, *485*, 486−489.

(16) Chen, M.; Ju, M.-G.; Garces, H. F.; Carl, A. D.; Ono, L. K.; Hawash, Z.; Zhang, Y.; Shen, T.; Qi, Y.; Grimm, R. L.; Pacifici, D.; Zeng, X. C.; Zhou, Y.; Padture, N. P. Highly stable and efficient all- inorganic lead-free perovskite solar cells with native-oxide passivation. *Nat. Commun.* **2019**, *10*, No. 16.

(17) Stoumpos, C. C.; Frazer, L.; Clark, D. J.; Kim, Y. S.; Rhim, S. H.; Freeman, A. J.; Ketterson, J. B.; Jang, J. I.; Kanatzidis, M. G. Hybrid germanium iodide perovskite semiconductors: active lone pairs, structural distortions, direct and indirect energy gaps, and strong nonlinear optical properties. *J. Am. Chem. Soc.* **2015**, *137*, 6804−6819.

(18) Du, K.-z.; Meng, W.; Wang, X.; Yan, Y.; Mitzi, D. B. Bandgap engineering of lead-free double perovskite $Cs_{2}AgBiBr_{6}$ through trivalent metal alloying. *Angew. Chem., Int. Ed.* **2017**, *56*, 8158−8162.

(19) Locardi, F.; Cirignano, M.; Baranov, D.; Dang, Z.; Prato, M.; Drago, F.; Ferretti, M.; Pinchetti, V.; Fanciulli, M.; Brovelli, S.; De Trizio, L.; Manna, L. Colloidal synthesis of double perovskite $Cs_{2}AgInCl_{6}$ and Mn-doped $Cs_{2}AgInCl_{6}$ nanocrystals. *J. Am. Chem. Soc.* **2018**, *140*, 12989−12995.

(20) Lee, B.; Stoumpos, C. C.; Zhou, N.; Hao, F.; Malliakas, C.; Yeh, C.-Y.; Marks, T. J.; Kanatzidis, M. G.; Chang, R. P. H. Air-stable molecular semiconducting iodosalts for solar cell applications: $Cs_{2}SnI_{6}$ as a hole conductor. *J. Am. Chem. Soc.* **2014**, *136*, 15379−15385.

(21) Qiu, X.; Cao, B.; Yuan, S.; Chen, X.; Qiu, Z.; Jiang, Y.; Ye, Q.; Wang, H.; Zeng, H.; Liu, J.; Kanatzidis, M. G. From unstable $CsSnI_{3}$ to air-stable $Cs_{2}SnI_{6}$: a lead-free perovskite solar light absorber with bandgap of 1.48eV and high absorption coefficient. *Sol. Energy Mater. Sol. Cells* **2017**, *159*, 227−234.

(22) Chen, M.; Ju, M.-G.; Carl, A. D.; Zong, Y.; Grimm, R. L.; Gu, J.; Zeng, X. C.; Zhou, Y.; Padture, N. P. Cesium titanium(IV) bromide thin films based stable lead-free perovskite solar Cells. *Joule* **2018**, *2*, 558−570.

(23) Saparov, B.; Hong, F.; Sun, J.-P.; Duan, H.-S.; Meng, W.; Cameron, S.; Hill, I. G.; Yan, Y.; Mitzi, D. B. Thin-film preparation and characterization of $Cs_{3}Sb_{2}I_{9}$: a lead-free layered perovskite semiconductor. *Chem. Mater.* **2015**, *27*, 5622−5632.

(24) McCall, K. M.; Stoumpos, C. C.; Kontsevoi, O. Y.; Alexander, G. C. B.; Wessels, B. W.; Kanatzidis, M. G. From 0D $Cs_{3}Bi_{2}I_{9}$ to 2D $Cs_{3}Bi_{2}I_{6}Cl_{3}$: dimensional expansion induces a direct band gap but enhances electron−phonon coupling. *Chem. Mater.* **2019**, *31*, 2644−2650.

(25) Kundu, K.; Acharyya, P.; Maji, K.; Sasmal, R.; Agasti, S. S.; Biswas, K. Synthesis and localized photoluminescence blinking of lead-free 2D nanostructures of $Cs_{3}Bi_{2}I_{6}Cl_{3}$ perovskite. *Angew. Chem., Int. Ed.* **2020**, *59*, 13093.

(26) Cortecchia, D.; Dewi, H. A.; Yin, J.; Bruno, A.; Chen, S.; Baikie, T.; Boix, P. P.; Grätzel, M.; Mhaisalkar, S.; Soci, C.; Mathews, N. Lead-free $MA_{2}CuCl_{x}Br_{4−x}$ hybrid perovskites. *Inorg. Chem.* **2016**, *55*, 1044−1052.

(27) Jun, T.; Sim, K.; Iimura, S.; Sasase, M.; Kamioka, H.; Kim, J.; Hosono, H. Lead-free highly efficient blue-emitting $Cs_{3}Cu_{2}I_{5}$ with 0D electronic structure. *Adv. Mater.* **2018**, *30*, No. 1804547.

(28) Stoumpos, C. C.; Malliakas, C. D.; Kanatzidis, M. G. Semiconducting tin and lead iodide perovskites with organic cations: phase transitions, high mobilities, and near-infrared photoluminescent properties. *Inorg. Chem.* **2013**, *52*, 9019−9038.

(29) Meng, X.; Lin, J.; Liu, X.; He, X.; Wang, Y.; Noda, T.; Wu, T.; Yang, X.; Han, L. Highly stable and efficient FASnI₃-based perovskite solar cells by introducing hydrogen bonding. *Adv. Mater.* **2019**, *31*, No. 1903721.

(30) Jokar, E.; Chien, C.-H.; Tsai, C.-M.; Fathi, A.; Diau, E. W.-G. Robust tin-based perovskite solar cells with hybrid organic cations to attain efficiency approaching 10%. *Adv. Mater.* **2019**, *31*, No. 1804835.

(31) Yang, S.; Wang, Y.; Liu, P.; Cheng, Y.-B.; Zhao, H. J.; Yang, H. G. Functionalization of perovskite thin films with moisture-tolerant molecules. *Nat. Energy* **2016**, *1*, No. 15016.

(32) Yang, S.; Chen, S.; Mosconi, E.; Fang, Y.; Xiao, X.; Wang, C.; Zhou, Y.; Yu, Z.; Zhao, J.; Gao, Y.; De Angelis, F.; Huang, J. Stabilizing halide perovskite surfaces for solar cell operation with wide-bandgap lead oxysalts. *Science* **2019**, *365*, 473−478.

(33) Kim, B.; Seok, S. I. Molecular aspects of organic cations affecting the humidity stability of perovskites. *Energy Environ. Sci.* **2020**, *13*, 805−820.

(34) Tian, J.; Xue, Q.; Yao, Q.; Li, N.; Brabec, C. J.; Yip, H.-L. Inorganic halide perovskite solar cells: progress and challenges. *Adv. Energy Mater.* **2020**, *10*, No. 2000183.

(35) Wang, Y.; Dar, M. I.; Ono, L. K.; Zhang, T.; Kan, M.; Li, Y.; Zhang, L.; Wang, X.; Yang, Y.; Gao, X.; Qi, Y.; Grätzel, M.; Zhao, Y. Thermodynamically stabilized $\beta$-CsPbI₃-based perovskite solar cells with efficiencies >18%. *Science* **2019**, *365*, 591−595.

(36) Acharyya, P.; Maji, K.; Kundu, K.; Biswas, K. 2D Nanoplates and scaled-up bulk polycrystals of ruddlesden−popper $Cs_{2}PbI_{2}Cl_{2}$ for optoelectronic applications. *ACS Appl. Nano Mater.* **2020**, *3*, 877−886.

(37) Wang, N.; Liu, W.; Zhang, Q. Perovskite-based nanocrystals: synthesis and applications beyond solar cells. *Small Methods* **2018**, *2*, No. 1700380.

(38) Fang, Z.; Shang, M.; Zheng, Y.; Zhang, T.; Du, Z.; Wang, G.; Duan, X.; Chou, K.-C.; Lin, C.-H.; Yang, W.; Hou, X.; Wu, T. Organic intercalation engineering of quasi-2D Dion−Jacobson $\alpha$-CsPbI₃ perovskites. *Mater. Horiz.* **2020**, *7*, 1042−1050.

(39) Chung, I.; Song, J.-H.; Im, J.; Androulakis, J.; Malliakas, C. D.; Li, H.; Freeman, A. J.; Kenney, J. T.; Kanatzidis, M. G. $CsSnI_{3}$: semiconductor or metal? high electrical conductivity and strong near- infrared photoluminescence from a single material. High hole mobility and phase-transitions. *J. Am. Chem. Soc.* **2012**, *134*, 8579−8587.

(40) Marshall, K. P.; Walker, M.; Walton, R. I.; Hatton, R. A. Enhanced stability and efficiency in hole-transport-layer-free $CsSnI_3$ perovskite photovoltaics. *Nat. Energy* **2016**, *1*, No. 16178.

(41) Zheng, Y.; Fang, Z.; Shang, M.-H.; Du, Z.; Yang, Z.; Chou, K.-C.; Yang, W.; Wei, S.; Hou, X. Enhancing the stability of orthorhombic $CsSnI_3$ perovskite via oriented $\pi$-conjugated ligand passivation. *ACS Appl. Mater. Interfaces* **2020**, *12*, 34462−34469.

(42) Heo, J. H.; Kim, J.; Kim, H.; Moon, S. H.; Im, S. H.; Hong, K.-H. Roles of $SnX_2$ ($X = F$, Cl, Br) additives in tin-based halide perovskites toward highly efficient and stable lead-free perovskite solar cells. *J. Phys. Chem. Lett.* **2018**, *9*, 6024−6031.

(43) da Silva, E. L.; Skelton, J. M.; Parker, S. C.; Walsh, A. Phase stability and transformations in the halide perovskite $CsSnI_3$. *Phys. Rev. B* **2015**, *91*, No. 144107.

(44) Kontos, A. G.; Kaltzoglou, A.; Siranidi, E.; Palles, D.; Angeli, G. K.; Arfanis, M. K.; Psycharis, V.; Raptis, Y. S.; Kamitsos, E. I.; Trikalitis, P. N.; Stoumpos, C. C.; Kanatzidis, M. G.; Falaras, P. Structural stability, vibrational properties, and photoluminescence in $CsSnI_3$ perovskite upon the addition of $SnF_2$. *Inorg. Chem.* **2017**, *56*, 84−91.

(45) Donaldson, J. D.; Grimes, S. M. The Inorganic Chemistry of Tin. In *Chemistry of Tin*; Smith, P. J., Ed.; Springer Netherlands: Dordrecht, 1998; pp 62−94.

(46) Degen, T.; Sadki, M.; Bron, E.; König, U.; Nénert, G. The HighScore suite. *Powder Diffr.* **2014**, *29*, S13−S18.

(47) Wendlandt, W. W.; Hecht, H. G. *Reflectance Spectroscopy*; Interscience: New York, 1966.

(48) Kortüm, G. *Reflectance Spectroscopy: Principles, Methods, Applications*; Springer: Berlin, 1969.

(49) Chung, D.-Y.; Choi, K.-S.; Iordanidis, L.; Schindler, J. L.; Brazis, P. W.; Kannewurf, C. R.; Chen, B.; Hu, S.; Uher, C.; Kanatzidis, M. G. High thermopower and low thermal conductivity in semiconducting ternary K−Bi−Se compounds. Synthesis and properties of $\beta$-K₂Bi₈Se₁₃ and K₂.₅Bi₈.₅Se₁₄ and their Sb analogues. *Chem. Mater.* **1997**, *9*, 3060−3071.

(50) Blöchl, P. E. Projector augmented-wave method. *Phys. Rev. B* **1994**, *50*, No. 17953.

(51) Kresse, G.; Hafner, J. Norm-conserving and ultrasoft pseudopotentials for first-row and transition elements. *J. Phys.: Condens. Matter* **1994**, *6*, 8245−8257.

(52) Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B* **1996**, *54*, No. 11169.

(53) Perdew, J. P.; Ruzsinszky, A.; Csonka, G. I.; Vydrov, O. A.; Scuseria, G. E.; Constantin, L. A.; Zhou, X.; Burke, K. Restoring the density-gradient expansion for exchange in solids and surfaces. *Phys. Rev. Lett.* **2008**, *100*, No. 136406.

(54) Perdew, J. P.; Ernzerhof, M.; Burke, K. Rationale for mixing exact exchange with density functional approximations. *J. Chem. Phys.* **1996**, *105*, 9982−9985.

(55) Miao, X.; Qiu, T.; Zhang, S.; Ma, H.; Hu, Y.; Bai, F.; Wu, Z. Air-stable $CsPb_{1-x}Bi_xBr_3$ ($0 \leq x \ll 1$) perovskite crystals: optoelectronic and photostriction properties. *J. Mater. Chem. C* **2017**, *5*, 4931−4939.

(56) Chatterjee, S.; Dasgupta, U.; Pal, A. J. Sequentially deposited antimony-doped $CH_3NH_3PbI_3$ films in inverted planar heterojunction solar cells with a high open-circuit voltage. *J. Phys. Chem. C* **2017**, *121*, 20177−20187.

(57) Zhang, J.; Shang, M.-h.; Wang, P.; Huang, X.; Xu, J.; Hu, Z.; Zhu, Y.; Han, L. n-type doping and energy states tuning in $CH_3NH_3Pb_{1-x}Sb_{2x/3}I_3$ perovskite solar cells. *ACS Energy Lett.* **2016**, *1*, 535−541.

(58) Liu, Z.; Huang, Y.; Yi, X.; Fu, B.; Yuan, G.; Wang, J.; Li, J.; Zhang, Y. Analysis of photoluminescence thermal quenching: guidance for the design of highly effective p-type doping of nitrides. *Sci. Rep.* **2016**, *6*, No. 32033.

(59) Xing, G.; Kumar, M. H.; Chong, W. K.; Liu, X.; Cai, Y.; Ding, H.; Asta, M.; Grätzel, M.; Mhaisalkar, S.; Mathews, N.; Sum, T. C. Solution-processed tin-based perovskite for near-infrared lasing. *Adv. Mater.* **2016**, *28*, 8191−8196.

(60) Kieslich, G.; Sun, S.; Cheetham, A. K. An extended tolerance factor approach for organic−inorganic perovskites. *Chem. Sci.* **2015**, *6*, 3430−3433.

(61) Shannon, R. D. Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides. *Acta Crystallogr., Sect. A* **1976**, *32*, 751−767.
<br>
H
https://dx.doi.org/10.1021/acsaem.0c01484
ACS Appl. Energy Mater. XXXX, XXX, XXX−XXX