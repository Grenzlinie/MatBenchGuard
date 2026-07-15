# CH₃O Radical Binding on Hexagonal Water Ice and Amorphous Solid Water

W. M. C. Sameera,* Bethmini Senevirathne, Stefan Andersson, Muhsen Al-Ibadi, Hiroshi Hidaka, Akira Kouchi, Gunnar Nyman, and Naoki Watanabe

Cite This: J. Phys. Chem. A 2021, 125, 387−393

ABSTRACT: Binding energies of the $CH_3O$ radical on hexagonal water ice ($I_h$) and amorphous solid water (ASW) were calculated using the ONIOM(QM:MM) method. A range of binding energies is found (0.10−0.50 eV), and the average binding energy is 0.32 eV. The $CH_3O$ radical binding on the ASW surfaces is stronger than on the $I_h$ surfaces. The computed binding energies from the ONIOM(wB97X-D/def2-TZVP:AMBER) and wB97X-D/def2-TZVP methods agree quite well. Therefore, the ONIOM(QM:MM) method is expected to give accurate binding energies at a low computational cost. Binding energies from the ONIOM(wB97X-D/def2-TZVP:AMBER) and ONIOM(wB97X-D/def2-TZVP:AMOEBA09) methods differ noticeably, indicating that the choice of force field matters. According to the energy decomposition analysis, the electrostatic interactions and Pauli repulsions between the $CH_3O$ radical and ice play a crucial role in the binding energy. This study gives quantitative insights into the $CH_3O$ radical binding on interstellar ices.

![](./images/812523446993944576_1.jpg)

## INTRODUCTION

Complex organic molecules (COMs) have been detected in the interstellar medium (ISM).¹⁻⁵ Mechanistic details of their formation are, however, still not fully understood, but radicals may play a key role. Radical species in the ISM can be formed through surface reactions or photodissociation of molecules, such as $H_2O$, $CO$, $CH_3OH$, $CO_2$, $NH_3$, $CH_4$, and $H_2CO$, in the icy mantles of interstellar grains.⁶⁷ The radicals can serve as precursors for the formation of COMs.⁶,⁸,⁹ Radical species on interstellar ices may diffuse and react with molecules or other radicals, giving rise to large molecular or radical species. Quantifying the details of radical binding, diffusion, and reactions on the interstellar ices is crucial for rationalizing the chemical evolution in space. Experimental determination of radical binding energies on ice, their probability of desorption, and surface mobility is highly challenging. In this regard, quantum chemistry plays a vital role in the quantitative determination of the radical processes on the interstellar ices.¹⁰

In our previous study,¹¹ binding energies between $OH$, $HCO$, and $CH_3$ radicals on crystalline water ice ($I_h$) were calculated using the two-layer our own N-layered integrated molecular orbital molecular mechanics (ONIOM) method.¹² In that computational study, the electronically important part of the molecular system, particularly the binding site, was described by density functional theory (DFT), while the remaining part of the molecular system was described by the AMOEBA09¹³⁻¹⁵ polarizable force field. ONIOM(DFT:AMOEBA09) calculations suggested that the binding energies of the radicals on $I_h$ are sensitive to the number of dangling hydrogen ($dH$) and dangling oxygen ($dO$) at the binding sites. A range of binding energies was found ($OH$: 0.67−0.20 eV, $HCO$: 0.42−0.12 eV, and $CH_3$: 0.26−0.11 eV). The computed average binding energies follow the order $OH$ (0.43 eV) > $HCO$ (0.26 eV) > $CH_3$ (0.16 eV). In the present study, we focus on the $CH_3O$ radial binding on both $I_h$ and amorphous solid water (ASW) in order to acquire a quantitative picture of the $CH_3O$ radical binding on the interstellar ices.

The $CH_3O$ radical was discovered in the cold and dense core Barnard-1b.¹⁶ The $CH_3O$ radical was proposed as an intermediate for the formation of $CH_3OH$ through hydrogenation of $CO$ on icy grain surfaces at around 10 K.¹⁷⁻²⁰ As a significant amount of solid $CH_3OH$ is formed on icy grains, $CH_3OH$ desorption from ice may be an important source of gaseous $CH_3OH$ in molecular clouds.²¹ This phenomenon was studied experimentally in the successive hydrogenation of $CO$,²²,²³ where the desorption of $CH_3OH$ may be induced by the hydrogenation of the $CH_3O$ radical. An experimental study by Qasim et al. suggested that the reactions between the $CH_3O$ radical and hydrocarbon radicals give rise to methoxyethene, methoxyethane, allyl alcohol, and 1-propanol in the ISM.²⁴ Another experimental study proposed that the $CH_3O$ radical is essential for the formation of methyl formate, glycolaldehyde, and ethylene glycol in the ISM.⁸ However, under realistic interstellar conditions, the reactions between a $CH_3O$ radical and other radical species may compete with surface diffusion and

Received: October 7, 2020
Revised: December 10, 2020
Published: December 28, 2020

![](./images/812523446993944576_2.jpg)

© 2020 American Chemical Society
387
https://dx.doi.org/10.1021/acs.jpca.0c09111
J. Phys. Chem. A 2021, 125, 387−393

![](./images/812523446993944576_3.jpg)

Figure 1. QM/MM ice cluster models of $I_h$ and ASW. The "ball and stick" representations are for the QM regions, and the "wireframe" representations show the MM regions.

desorption. These phenomena have not been examined quantitatively, where the nature of the binding sites on ice surfaces may play a role. $^{25,26}$ Kinetic models of the surface chemistry of interstellar grains have indicated that $CH_{3}O$ is important for the formation of methyl formate, $^{27}$ and also that $CH_{3}O$ might aid both the formation and removal of the amino acid glycine. $^{28}$ The validity of these models relies on implementing realistic parameters for reaction rates, surface diffusion, and binding energies. Previous estimates of the $CH_{3}O$ binding energy in models of interstellar ices have varied between2500 and $5080 ~K(0.22-0.44 eV).^{6,27,29}$ An estimate based onsimple quantum chemistry calculations on a $H_{2}O-CH_{3}O$ molecular complex gave a binding energy of $4400 ~K(0.38 eV).^{30}$  Hence, a clear understanding of binding energies between CH,O and the various binding sites of the ice surface is critical for constructing more accurate astrochemical models.

## COMPUTATIONAL METHODS
Structure optimizations of the ice systems were performed usingthe two-layer ONIOM $^{12}$ method in the Gaussian16 program, $^{31}$  where the high-level computations were performed using the quantum mechanical (QM) method, while the low-level computations were carried out using the molecular mechanics(MM) method. The total energy $(E)$ , gradient $(G)$ , and Hessian $(H)$ of an ONIOM(QM:MM) calculation can be defined as $^{12,32}$ 

$$
\begin{aligned}
& E_{\text {ONIOM }}(\mathrm{QM}: \mathrm{MM}) \\
& \quad=E_{\mathrm{QM}}(\mathrm{QM})+E_{\mathrm{MM}}(\mathrm{QM}: \mathrm{MM})-E_{\mathrm{MM}}(\mathrm{QM})
\end{aligned}
$$

$$
\begin{aligned}
& G_{\text {ONIOM }}(\mathrm{QM}: \mathrm{MM}) \\
& \quad=G_{\mathrm{QM}}(\mathrm{QM}) \times J+G_{\mathrm{MM}}(\mathrm{QM}: \mathrm{MM}) \\
& \quad-G_{\mathrm{MM}}(\mathrm{QM}) \times J
\end{aligned}
$$

$$
\begin{aligned}
& H_{\text {ONIOM }}(\mathrm{QM}: \mathrm{MM}) \\
& \quad=J^{T} \times H_{\mathrm{QM}}(\mathrm{QM}) \times J+H_{\mathrm{MM}}(\mathrm{QM}: \mathrm{MM}) \\
& \quad-J^{T} \times H_{\mathrm{MM}}(\mathrm{QM}) \times J
\end{aligned}
$$

Here, the labels in parentheses denote the region of the molecular system, the labels in the subscript indicate the computational method, and $J=\frac{\delta( real coord. )}{\delta( model coord. )}$ . For the ONIOM high-layer computations, the wB97X-D $^{33}$ functional and the def2-TZVP $^{34}$ basis sets were employed. The ONIOM low-layerwas described by the AMBER $^{35}$ force field or the AMOEB09 polarizable force field. The SICTWO interface $^{32}$ was used for the ONIOM(wB97X-D:AMOEBA09) calculations. Mechanical embedding was used for all ONIOM(QM:MM) calculations, where the interactions between the QM and MM regions were calculated using MM. Vibrational frequency calculations were performed to confirm that the optimized structures were local minima (i.e., no imaginary frequency) and to calculate harmonic zero-point energies.

Ice cluster models were prepared using the $I_{h}$ and ASW structural models by Andersson et al. $^{36}$ For $I_{h}$ , two types of ice cluster models were used (Figure 1). In the $I_{h}$ cluster models, three water layers were included. The $I_{h}$ models A1-A5 consistof $162 H_{2}O$ molecules (48 molecules in the QM region and 114 $H_{2}O$ in the MM region). The $I_{h}$ models A6-A8 hold $156 H_{2}O$  molecules ( $44 H_{2}O$ in the QM region and $112 H_{2}O$ in the MM region). In the case of the $I_{h}$ cluster models A9-A16, each has a vacancy obtained by removing an $H_{2}O$ molecule from the top H,O layer of the Al cluster model. The ASW cluster models, $B 1-B 10$ , consist of $162 H_{2}O$ molecules, where $49 H_{2}O$  molecules are in the QM region and 113 in the MM region(Figure 1). All $I_{h}$ and ASW cluster model systems were fully optimized. To avoid structural deformations at the binding site and to save computational cost, $H_{2}O$ molecules in the MM region were frozen during the structure optimization, where the positions of the atoms in the MM region were kept as in the structural models by Andersson et al. $^{36}$ If we allow the MM region to relax, the structure of the QM region will deform, and the binding sites in the resulting structures will not mimic the binding sites in the periodic ice structures. Binding energies were calculated using the following formula

$$\text { Binding energy }=\left|E_{(\text {ice }- \text { radical })}-E_{\text {ice }}-E_{\text {radical }}\right|$$

where $E_{(ice - radical) }$ is the total energy of an optimized $CH_{3}O$  radical-bound ice structure, $E_{ice }$ is the total energy of an optimized ice cluster model, and $E_{radical }$ is the total energy of an optimized $CH_{3}O$ radical.

## RESULTS AND DISCUSSION
Optimized structures of the $CH_{3}O$ radical-bound ice structures are shown in Figure 2. The wB97XD/def2-TZVP-optimized doublet ground state of the $CH_{3}O$ radical has an $O-C$ bond distance of $1.36 \AA$ and a $C-H$ bond distance of $1.10 \AA$ . The

![](./images/812523446993944576_4.jpg)

Figure 2. ONIOM(wB97X-D/Def2-TZVP:AMBER) optimized structures of the $CH_3O$ radical bound to the $I_h$ (A1−A16) and to the ASW (B1−B10). Calculated binding energies are in eV. For simplicity, only the binding pocket of the QM region is shown. Bond lengths are in Å.

calculated spin density on O is 0.90, suggesting that the unpaired electron is localized on O. After absorption of the $CH_3O$ radical on various binding sites, its structure is nearly preserved and the spin density remains localized on the O atom of the $CH_3O$ radical (Table S1).

The calculated binding energies are shown in Figure 3. A range of binding energies, 0.10−0.50 eV (ZPE accounted for harmonically), was observed. When we take all binding sites into account, the computed average binding energy is 0.32 eV, which is slightly lower than that obtained without accounting for ZPE (0.37 eV). Thus, the ZPE plays a minor role in the binding energy. In the case of $I_h$ without a vacancy (i.e., A1−A8), the computed average binding energy is 0.28 eV. In the presence of a vacancy on the $I_h$ surface (i.e., A9−A16), the calculated average binding energy becomes 0.36 eV. Therefore, the $CH_3O$ radical binding is stronger if a vacancy is present on $I_h$.

For the ASW models (i.e., B1−B10), the computed average binding energy is 0.31 eV, which is slightly higher than that of $I_h$

![](./images/812523446993944576_5.jpg)

Figure 3. Computed binding energies (without and with zero-point energy (ZPE)) of a $CH_3O$ radical on $I_h$ (A1−A16) and ASW (B1−B10) according to ONIOM(wB97X-D/Def2-TZVP:AMBER) calculations. The binding energies are summarized in Table S2.

![](./images/812523446993944576_6.jpg)

Figure 4. Distribution of the binding energies of the $CH_3O$ radical on ice from ONIOM(wB97X-D/Def2-TZVP:AMBER) calculations.

(0.28 eV). Compared to the spread in binding energies between individual sites, this difference is rather small. The B4 system has the weakest binding energy (0.10 eV) as in this case, the radical interacts with the surface water molecules through relatively weak $OC(H_2)H-OH_2$ interactions. Due to the weak binding energy at the B4 site, the $CH_3O$ radical may thermally desorb or diffuse to a binding site with a larger binding energy. On the other hand, relatively strong binding energies were found when the $CH_3O$ radical binds to the surface water molecules through $H_3CO-HOH$ interactions (e.g., at B2 (0.42 eV)), and therefore, the $CH_3O$ radical may not desorb or diffuse thermally from such sites. The distribution of the binding energies of the $CH_3O$ radical on ice is shown in Figure 4. Binding energies in the 0.20−0.40 eV range dominate.

To check whether the size of the QM region affects the calculated binding energies, binding energies (without ZPE) from the ONIOM(wB97X-D/Def2-TZVP:AMBER) and wB97X-D/Def2-TZVP methods were compared (Figure S1). In general, the computed binding energies from the two methods are in reasonable agreement, suggesting that the electronic effects of the $H_2O$ molecules in the ONIOM low-layer computations play a minor role in the calculated binding energies. The maximum discrepancy of 0.10 eV was found for the A1, A13, and B3 binding sites, while the average unsigned difference of all sites is 0.04 eV. Thus, the QM region is most important and the MM region matters less, indicating that the size of the QM region in our ONIOM(QM:MM) calculations gives reliable binding energies of the $CH_3O$ radical on the ice cluster models.

To check whether the chosen force field affects the calculated binding energies, binding energies (without considering ZPE) from the ONIOM(wB97X-D/Def2-TZVP:AMBER) and ONIOM(wB97XD/Def2-TZVP:AMOEBA09) methods were compared. The average binding energy from the ONIOM(wB97X-D/Def2-TZVP:AMBER) method is 0.37 eV, which is close to the average binding energy from the ONIOM(wB97X-D/Def2-TZVP:AMOEBA09) method, 0.38 eV. Yet, the maximum discrepancies between the two methods are as large as 0.14 eV (A16) and 0.11 eV (A14 and A11). The average difference in the binding energy between the two methods is 0.06 eV for the A sites and 0.03 eV for the B sites. This indicates that the choice of the force field noticeably affects the results, albeit not dramatically. We also notice here that the average deviation between the ONIOM(wB97X-D/Def2-TZVP:AMOEBA09) and wB97X-D/Def2-TZVP calculations are 0.07 eV for the A sites and 0.07 eV for the B sites. These differences are larger than the corresponding differences (0.04 and 0.05 eV, respectively) between the ONIOM(wB97X-D/Def2-

TZVP:AMBER) and wB97X-D/Def2-TZVP calculations. The ONIOM(wB97X-D/Def2-TZVP:MM) binding energies versus wB97X-D/Def2-TZVP binding energies are shown in Figure S3a. In the case of ONIOM(wB97X-D/Def2-TZVP:AMOE-BA09), the spread of energies around $y = x$ is relatively larger than that of the ONIOM(wB97X-D/Def2-TZVP:AMBER) method (Figure S3b). Thus, we have used the ONIOM(wB97X-D/Def2-TZVP:AMBER) method to report the binding energies.

Energy Decomposition Analysis. To acquire more insight into the reasons for the stronger and weaker binding energies obtained for various sites, an EDA was performed. $^{37-39}$ The EDA was performed using the ASW models B1-B10 as they are most relevant for the interstellar conditions. For EDA, the QM region of the $CH_{3}O$-bound ice clusters (XY) was used and divided into two fragments: ice (X) and the $CH_{3}O$ radical (Y) (see Figure 5).

![](./images/812523446993944576_7.jpg)

Figure 5. Dividing the $CH_{3}O$ radical-bound ice structure (XY) into ice (X) and a $CH_{3}O$ radical (Y) for energy decomposition analysis (EDA). The binding energy is decomposed into interaction energy ($\Delta E_{INT}$) and deformation energy ($\Delta E_{DEF}$). The $\Delta E_{INT}$ term was divided into electrostatic attraction ($\Delta V_{elstat}$), Pauli repulsion ($\Delta E_{Pauli}$), and orbital interactions ($\Delta E_{oi}$).

Using EDA, the binding energy between the $CH_{3}O$ radical and ice can be decomposed into interaction energy and deformation energy. In this way, some insights into the possible reasons for strong or weak binding energies can be obtained. The energy difference between the optimized ice-radical complex and the isolated ice structure and the isolated $CH_{3}O$ radical, with internal geometries unchanged, is defined as the interaction energy ($\Delta E_{INT}$). The deformation energy ($\Delta E_{DEF}$) is defined as the energy difference of the ice structure and the $CH_{3}O$ radical obtained when changing the geometry to that optimal for the two isolated structures (denoted as $X_{0}$ and $Y_{0}$). The $\Delta E_{INT}$ term was divided into electrostatic attraction ($\Delta V_{elstat}$), Pauli repulsion ($\Delta E_{Pauli}$), and orbital interactions ($\Delta E_{oi}$). The Coulomb interaction ($\Delta V_{elstat}$) is the interaction between the frozen charge densities of the two fragments, A and B. The exchange (Pauli) repulsion, $\Delta E_{Pauli}$, is the energy difference obtained using the normalized wave function of the product (AB) that violates the Pauli principle and the antisymmetrized and renormalized wave function. The orbital interactions ($\Delta E_{oi}$) describes the orbital mixing and charge transfer between the A and B fragments when they form the product, AB. The EDA was performed using the ADF program (Version 2019.103),$^{40,41}$ employing the wB97X functional and the TZP basis sets. $^{41-44}$

According to EDA (Table 1 and Figure 6), the interaction energy is the dominant contributor to the binding energy. The deformation energies of the ice and $CH_{3}O$ radicals are almost zero in all cases except B3, suggesting essentially no geometric or electronic preparation of the two fragments during the radical absorption on ice. In B3, the $CH_{3}O$ radical breaks a hydrogen bond between two $H_{2}O$ molecules at the binding site. As a result, the deformation of the B3 ice structure costs 0.15 eV. The electrostatic interactions are stronger than the orbital interactions in most cases. For $CH_{3}O$ radical binding, the electrostatic interactions and orbital interactions must exceed the Pauli repulsion. A strong binding energy, for instance B2 (0.50 eV), is observed in the presence of strong electrostatic attractions and strong Pauli repulsion. On the other hand, a weak binding energy, for instance B4 (0.17 eV), is observed for relatively weak electrostatic attractions and weak Pauli repulsion.

<table><thead><tr><th></th><th colspan="3">$\Delta E_{INT}$</th><th colspan="2">$\Delta E_{DEF}$</th><th rowspan="2">binding energy ($\Delta E_{INT} + \Delta E_{DEF}$)</th></tr><tr><th></th><th>$\Delta V_{elstat}$</th><th>$\Delta E_{Pauli}$</th><th>$\Delta E_{oi}$</th><th>$\Delta E_{DEF,X}$</th><th>$\Delta E_{DEF,Y}$</th></tr></thead><tbody><tr><td>B1</td><td>−0.46 (−0.56, 0.36, −0.26)</td><td></td><td></td><td>0.02 (0.02, 0.00)</td><td></td><td>−0.44</td></tr><tr><td>B2</td><td>−0.56 (−0.74, 0.54, −0.36)</td><td></td><td></td><td>0.06 (0.05, 0.01)</td><td></td><td>−0.50</td></tr><tr><td>B3</td><td>−0.45 (−0.55, 0.39, −0.30)</td><td></td><td></td><td>0.15 (0.15, 0.00)</td><td></td><td>−0.30</td></tr><tr><td>B4</td><td>−0.17 (−0.22, 0.12, −0.08)</td><td></td><td></td><td>0.01 (0.00, 0.01)</td><td></td><td>−0.16</td></tr><tr><td>B5</td><td>−0.46 (−0.56, 0.36, −0.26)</td><td></td><td></td><td>0.03 (0.03, 0.00)</td><td></td><td>−0.43</td></tr><tr><td>B6</td><td>−0.29 (−0.27, 0.11, −0.12)</td><td></td><td></td><td>0.01 (0.01, 0.00)</td><td></td><td>−0.28</td></tr><tr><td>B7</td><td>−0.34 (−0.41, 0.26, −0.19)</td><td></td><td></td><td>0.05 (0.05, 0.00)</td><td></td><td>−0.29</td></tr><tr><td>B8</td><td>−0.23 (−0.16, 0.06, −0.13)</td><td></td><td></td><td>0.00 (0.00, 0.00)</td><td></td><td>−0.23</td></tr><tr><td>B9</td><td>−0.49 (−0.57, 0.35, −0.27)</td><td></td><td></td><td>0.01 (0.00, 0.01)</td><td></td><td>−0.48</td></tr><tr><td>B10</td><td>−0.46 (−0.56, 0.37, −0.26)</td><td></td><td></td><td>0.03 (0.03, 0.00)</td><td></td><td>−0.43</td></tr></tbody></table>

$^{a}$Subscript X refers to the ice model and subscript Y refers to the radical.

## CONCLUSIONS
Binding energies of the $CH_{3}O$ radicals on model structures of $I_{h}$ and ASW were calculated using the ONIOM(QM:MM) method. Our findings give some insights into the behavior of the $CH_{3}O$ radical on interstellar ices. Combining the $I_{h}$ and ASW models, a range of binding energies, 0.10−0.50 eV, was obtained. Previous estimates$^{6,27,29,30}$ are within this range. Still, our calculations provide a broader range of binding energies. The calculated average binding energy of our ASW model is 0.31 eV, which is higher than that of $I_{h}$ (0.28 eV), but lower when there is a vacancy on the $I_{h}$ surface (0.36 eV). When all 26 binding sites are taken into account, the calculated average binding energy from the ONIOM(QM:MM) computations is 0.32 eV, which is slightly lower than the reported binding energy of a $H_{2}O-CH_{3}O$ molecular complex (0.38 eV).$^{30}$ In common practice, the astrochemistry community uses a single number of binding energy for developing astrochemical models. Considering the broad range of our calculated $CH_{3}O$ radical binding energies on ices, we propose that a more realistic astrochemical model could be achieved by considering a distribution of binding energies instead of a single value.

Our calculations show that the $CH_{3}O$ radical binding on the ASW surfaces is slightly stronger than on the $I_{h}$ surfaces.

![](./images/812523446993944576_8.jpg)

Figure 6. Calculated interaction energy ($\Delta E_{\text{INT}}$), electrostatic attraction ($\Delta V_{\text{elstat}}$), Pauli repulsion ($\Delta E_{\text{Pauli}}$), and orbital interactions ($\Delta E_{\text{oi}}$) of the ASW models B1−B10.

Therefore, we propose that the $\text{CH}_3\text{O}$ radical diffusion on ASW is likely to be slower than on $I_h$, albeit this primarily hinges on diffusion barrier heights. According to the EDA, the interactions between the $\text{CH}_3\text{O}$ radical and ice (i.e., electrostatic attraction, Pauli repulsion, and orbital interactions) control the strength of the binding energy, with only minor contributions from the deformation energies of ice and $\text{CH}_3\text{O}$. In our ONIOM-(QM:MM) calculations, a relatively large QM region was used, and therefore, binding energies could be calculated accurately. The chosen force field for the ONIOM low-level computations plays a minor role in the computed average binding energy.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpca.0c09111.

Calculated spin densities, calculated binding energies, and cartesian coordinates of the optimized structures (PDF)

## AUTHOR INFORMATION
### Corresponding Author
W. M. C. Sameera − Institute of Low Temperature Science, Hokkaido University, Sapporo 060-0819, Japan;
orcid.org/0000-0003-0213-0688; Phone: +81-11-706-7449; Email: wmcsameera@lowtemp.hokudai.ac.jp; Fax: +81-11-706-7142

### Authors
Bethmini Senevirathne − Department of Chemistry and Molecular Biology, University of Gothenburg, SE-412 96 Gothenburg, Sweden

Stefan Andersson − Department of Chemistry and Molecular Biology, University of Gothenburg, SE-412 96 Gothenburg, Sweden; SINTEF Industry, NO-7465 Trondheim, Norway

Muhsen Al-Ibadi − Department of Chemistry, College of Science, University of Kufa, P.O 21 Najaf, Iraq

Hiroshi Hidaka − Institute of Low Temperature Science, Hokkaido University, Sapporo 060-0819, Japan

Akira Kouchi − Institute of Low Temperature Science, Hokkaido University, Sapporo 060-0819, Japan

Gunnar Nyman − Department of Chemistry and Molecular Biology, University of Gothenburg, SE-412 96 Gothenburg, Sweden; orcid.org/0000-0002-9527-3890

Naoki Watanabe − Institute of Low Temperature Science, Hokkaido University, Sapporo 060-0819, Japan;
orcid.org/0000-0001-8408-2872

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpca.0c09111

### Author Contributions
Calculations were performed by W.M.C.S., B.S., and M.A. The manuscript was written by W.M.C.S. in collaboration with all authors. All authors have given approval to the final version of the manuscript.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
W.M.C.S. acknowledges the Grant-in Aid for Scientific Research (C) grant (No. 19K03940). N.W. acknowledges the Grant-in-Aid for Specially Promoted Research grant (No. JP17H06087). W.M.C.S., B.S., S.A., and G.N. acknowledge the MC-ITN (LASSIE) grant. G.N. acknowledges support from the Swedish Research Council Grant (No. 2016-03275). Super computing resources at the Institute for Molecular Science (IMS) in Japan, the Institute for Information Management and Communication at Kyoto University in Japan, and Chalmers Centre for Computational Science and Engineering (C3SE) in Sweden are also acknowledged.

## REFERENCES
(1) Herbst, E.; van Dishoeck, E. F. Complex Organic Interstellar Molecules. Annu. Rev. Astron. Astrophys. 2009, 47, 427−480.

(2) Bottinelli, S.; Ceccarelli, C.; Williams, J. P.; Lefloch, B. Hot Corinos in NGC 1333-IRAS4B and IRAS2A. Astron. Astrophys. 2007, 463, 601−610.

(3) Hollis, J. M.; Remijan, A. J.; Jewell, P. R.; Lovas, F. J. Cyclopropenone ($c$-H₂C₃O): A New Interstellar Ring Molecule. Astrophys. J. 2006, 642, 933−939.

(4) Bacmann, A.; Taquet, V.; Faure, A.; Kahane, C.; Ceccarelli, C. Detection of Complex Organic Molecules in a Prestellar Core: A New Challenge for Astrochemical Models. Astron. Astrophys. 2012, 541, L12.

(5) Vastel, C.; Ceccarelli, C.; Lefloch, B.; Bachiller, R. The Origin of Complex Organic Molecules in Prestellar Cores. Astrophys. J. Lett. 2014, 795, L2.

(6) Garrod, R. T.; Weaver, S. L. W.; Herbst, E. Complex Chemistry in Star-forming Regions: An Expanded Gas-Grain Warm-up Chemical Model. Astrophys. J. 2008, 682, 283−302.

(7) Öberg, K. I.; van Dishoeck, E. F.; Linnartz, H.; Andersson, S. The Effect of H₂O on Ice Photochemistry. Astrophys. J. 2010, 718, 832−840.

(8) Chuang, K.-J.; Fedoseev, G.; Iopporo, S.; van Dishoeck, E. F.; Linnartz, H. H-atom Addition and Abstraction Reactions in Mixed CO, H₂CO and CH₃OH Ices-an Extended View on Complex Organic Molecule Formation. Mon. Not. R. Astron. Soc. 2016, 455, 1702−1712.

(9) Enrique-Romero, J.; Rimola, A.; Ceccarelli, C.; Ugliengo, P.; Balucani, N.; Skouteris, D. Formation of Acetaldehyde on CO-Rich Ices. ACS Earth Space Chem. 2019, 3, 2158−2170.

(10) Zamirri, L.; Ugliengo, P.; Ceccarelli, C.; Rimola, A. Quantum Mechanical Investigations on the Formation of Complex Organic Molecules on Interstellar Ice Mantles. Review and Perspectives. ACS Earth Space Chem. 2019, 3, 1499−1523.

(11) Sameera, W. M. C.; Senevirathne, B.; Andersson, S.; Maseras, F.; Nyman, G. ONIOM(QM:AMOEBA09) Study on Binding Energies and Binding Preference of OH, HCO, and CH₃ Radicals on Hexagonal Water Ice (Iₕ). J. Phys. Chem. C 2017, 121, 15223−15232.

(12) Chung, L. W.; Sameera, W. M. C.; Ramozzi, R.; Page, A. J.; Hatanaka, M.; Petrova, G. P.; Harris, T. V.; Li, X.; Ke, Z.; Lui, F.; Li, H.-B.; Ding, L.; Morokuma, K. The ONIOM Method and its Applications. Chem. Rev. 2015, 115, 5678−5796.

(13) Ponder, J. W.; Case, D. A. Force Fields for Protein Simulations. Adv. Protein Chem. 2003, 66, 27−85.

(14) Ren, P. Y.; Ponder, J. W. J. Polarizable Atomic Multipole Water Model for Molecular Mechanics Simulation. Phys. Chem. B 2003, 107, 5933−5947.

(15) Ren, P. Y.; Ponder, J. W. Consistent Treatment of Inter- and Intramolecular Polarization in Molecular Mechanics Calculations. J. Comput. Chem. 2002, 23, 1497−1506.

(16) Cernicharo, J.; Marcelino, N.; Roueff, E.; Gerin, M.; Jiménez-Escobar, A.; Caro, G. M. Discovery of the Methoxy Radical, CH₃O, Toward B1: Dust Grain and Gas-phase Chemistry in Cold Dark Clouds. Astrophys. J. Lett. 2012, 759, L43.

(17) Ehrenfreund, P.; Charnley, S. B. Organic Molecules in the Interstellar Medium, Comets, and Meteorites: A Voyage from Dark Clouds to the Early Earth. Annu. Rev. Astron. Astrophys. 2000, 38, 427−483.

(18) Song, L.; Kästner, J. Tunneling Rate Constants for H₂CO + H on Amorphous Solid Water Surfaces. Astrophys. J. 2017, 850, 118.

(19) Woon, D. E. Modeling Gas Grain Chemistry with Quantum Chemical Cluster Calculations. I. Heterogeneous Hydrogenation of CO and H₂CO on Icy Grain Mantles. Astrophys. J. 2002, 569, 541−548.

(20) Rimola, A.; Taquet, V.; Ugliengo, P.; Balucani, N.; Ceccarelli, C. Combined Quantum Chemical and Modeling Study of CO Hydro- genation on Water Ice. A&A 2014, 572, A70.

(21) Garrod, T.; Wakelam, V.; Herbst, E. Non-thermal Desorption from Interstellar Dust Grains via Exothermic Surface Reactions. Astron. Astrophys. 2007, 467, 1103−1115.

(22) Hidaka, H.; Watanabe, N.; Shiraki, T.; Kouchi, A. Conversion of H₂CO to CH₃OH by Reactions of Cold Atomic Hydrogen on Ice Surfaces below 20 K. Astrophys. J. 2004, 614, 1124−1131.

(23) Chuang, K. -J.; Fedoseev, G.; Qasim, D.; Ioppolo, S.; van Dishoeck, E. F.; Linnartz, H. Reactive Desorption of CO Hydro- genation Products under Cold Pre-stellar Core Conditions. Astrophys. J. 2018, 853, 102.

(24) Qasim, D.; Fedoseev, G.; Chuang, K.-J.; Taquet, V.; Lamberts, T.; He, J.; Ioppolo, S.; van Dishoeck, E. F.; Linnartz, H. Formation of Interstellar Propanal and 1-propanol Ice: A Pathway Involving Solid- state CO Hydrogenation. Astron. Astrophys. 2019, 627, A1.

(25) Watanabe, N.; Kimura, Y.; Kouchi, A.; Chigai, T.; Hama, T.; Pirronello, V. Direct Measurements of Hydrogen Atom Diffusion and the Spin Temperature of Nascent H₂ Molecule on Amorphous Solid Water. Astrophys. J. Lett. 2010, 714, L233.

(26) Senevirathne, B.; Andersson, S.; Dulieu, F.; Nyman, G. Hydrogen Atom Mobility, Kinetic Isotope Effects and Tunneling on Interstellar Ices (Iₕ and ASW). Mol. Astrophys. 2017, 6, 59−69.

(27) Garrod, R. T. A. Three-Phase Chemical Model of Hot Cores: The Formation of Glycine. Astrophys. J. 2013, 765, 60.

(28) Suzuki, T.; Majumdar, L.; Ohishi, M.; Saito, M.; Hirota, T.; Wakelam, V. An Expanded Gas-Grain Model for Interstellar Glycine. Astrophys J. 2018, 863, 51.

(29) Garrod, R. T.; Herbst, E. Formation of Methyl Formate and Other Organic Species in the Warm-up Phase of Hot Molecular Cores. Astron. Astrophys. 2006, 457, 927−936.

(30) Wakelam, V.; Loison, J.-C.; Mereau, R.; Ruaud, M. Binding energies: New Values and Impact on the Efficiency of Chemical Desorption. Mol. Astrophys. 2017, 6, 22−35.

(31) Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Petersson, G. A.; Nakatsuji, H.et al. Gaussian 16, Revision C.01; Gaussian, Inc.: Wallingford CT, 2016.

(32) Sameera, W. M. C.; Maseras, F. Expanding the Range of Force Fields Available for ONIOM Calculations: The SICTWO Interface. J. Chem. Inf. Model. 2018, 58, 1828−1835.

(33) Chai, J.-D.; Head-Gordon, M. Long-range Corrected Hybrid Density Functionals with Damped Atom−atom Dispersion Correc- tions. Phys. Chem. Chem. Phys. 2008, 10, 6615−6620.

(34) Weigend, F.; Ahlrichs, R. Balanced Basis Sets of Split Valence,Triple Zeta Valence and Quadruple Zeta Valence Quality for H to Rn: Design and Assessment of Accuracy. Phys. Chem. Chem. Phys. 2005, 7, 3297−3305.

(35) Cornell, W. D.; Cieplak, P.; Bayly, C. I.; Gould, I. R.; Merz, K. M.,Jr.; Ferguson, D. M.; Spellmeyer, D. C.; Fox, T.; Caldwell, J. W.; Kollman, J. W. A. Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules. J. Am. Chem. Soc. 1995, 117, 5179−5197.

(36) Andersson, S.; Al-Halabi, A.; Kroes, G. J.; van Dishoeck, E. F. Molecular Dynamics Study of Photodissociation of Water in Crystalline and Amorphous Ices. J. Chem. Phys. 2006, 124, No. 064715.

(37) Ziegler, T.; Rauk, A. On the Calculation of Bonding Energies by the Hartree Fock Slater Method. Theor. Chim. Acta 1977, 46, 1−10.

(38) Zhao, L.; von Hopffgarten, M.; Andrada, D. M.; Frenking, G. Energy Decomposition Analysis. Wiley Interdiscip. Rev.: Comput. Mol. Sci. 2018, 8, e1345.

(39) Andrés, J.; Ayers, P. W.; Boto, R. A.; Carbó-Dorca, R.; Chermette, H.; Cioslowski, J.; Contreras-García, J.; Cooper, D. L.; Frenking, G.; Gatti, C.; et al. J. Comput. Chem. 2019, 40, 2248−2283.

(40) Bickelhaupt, F. M.; Baerends, E. J. Kohn-Sham Density Functional Theory: Predicting and Understanding Chemistry, Rev. Comput. Chem.; Lipkowitz, K. B.; Boyd, D. B. Eds.; Wiley-VCH: New York, 2000, 1, 1−86.

(41) te Velde, G.; Bickelhaupt, F. M.; Baerends, E. J.; Guerra, C. F.; van Gisbergen, S. J. A.; Snijders, J. G.; Ziegler, T. Chemistry With ADF. J. Comput. Chem. 2001, 22, 931−967.

(42) van Lenthe, E.; Baerends, E. J. Optimized Slater-type Basis Sets for the Elements 1-118. J. Comput. Chem. 2003, 24, 1142−1156.

(43) Chong, D. P.; van Lenthe, E.; van Gisbergen, S. J. A.; Baerends, E. J. Even-tempered Slater-Type Orbitals Revisited: From Hydrogen to Krypton. J. Comput. Chem. 2004, 25, 1030−1036.

(44) Chong, D. P. Augmenting Basis Set for Time-dependent Density Functional Theory Calculation of Excitation Energies: Slater-type Orbitals for Hydrogen to Krypton. Mol. Phys. 2005, 103, 749−761.