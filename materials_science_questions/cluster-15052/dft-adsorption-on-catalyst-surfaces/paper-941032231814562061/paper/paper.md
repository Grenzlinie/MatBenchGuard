# Coordination Engineering in Zirconium-Nitrogen-Functionalized Materials for N₂ Reduction: A First-Principles Simulation

Jianpeng Guo, $^{a}$ Hao Luo, $^{a}$ Qinfu Zhao, $^{a, b}$ Bingbing Suo, $^{a}$ Bo Zhou, $^{a}$ Haiyan Zhu, $^{a}$ Zhiyong Zhang $^{c,**}$ and Qi Song $^{a,*}$

a. Shaanxi Key Laboratory for Theoretical Physic Frontiers, Institute of Modern Physics, Northwest University, Xi’an 710069, People’s Republic of China

b. School of Physics and Electronic Information. Yan'an University. Yan'an 716000, People's Republic of China

c. Stanford Research Computing Center, Stanford University, Stanford, CA, 94305, USA

**KEYWORDS:** Coordination engineering, NRR, Electrocatalytic, First-principles

**ABSTRACT:**

Coordination engineering was employed to optimize the coordination environment of the Zr atom anchored on the porphyrins (PP). Five promising ZrPP-A candidates as electrocatalysts for nitrogen reduction reaction (NRR) were identified through a “four-step” screening strategy. First-principles calculations were utilized to evaluate the performance of the candidate electrocatalysts for NRR. A comprehensive search for reaction pathways revealed that NRR reactions with these selected catalysts tend to follow a hybrid pathway. It is found that orbital hybridization and charge transfer between Zr and its coordination atoms, as well as between ZrPP-A and the adsorbed N₂ ensured the stability and high catalytic activity of these selected ZrPP-A. Zr plays a crucial role in coordinating charge transfer during the NRR process. Simultaneously, the coordinating atoms and the PP moiety jointly provide additional charge transfers to or from the adsorbate. An asymmetric coordination environment results in an asymmetric charge distribution of the substrate, causing the adsorbed polarized N₂ molecule oriented toward the asymmetric charge aggregation region. Our work underscores the importance of considering not only the single-atom catalyst itself but also its coordination environment for the rational design of efficient catalysts.

### 1. INTRODUCTION

Ammonia is a versatile chemical compound, harnessed for its utility in myriad applications, from the manufacture of plastics and fibers to the creation of refrigerants and explosives. It is reported that more than 185 million tons of ammonia are produced annually worldwide. [1-3] However, the Haber-Bosch (HB) process, historically used to synthesize ammonia using nitrogen and hydrogen under high pressure, produces a sizable amount of greenhouse gases. The average amount of $CO_2$ emissions produced by this method per ton of $NH_3$ produced is 2.9 tons, exacerbating the high energy consumption and high carbon emissions problems of traditional $NH_3$ production. [4, 5] The electrocatalytic synthesis of $NH_3$ is considered the most promising alternative to the HB process as it significantly reduces energy requirements and minimizes environmental impact. [6, 7]

Recently, the exceptional architectural features and electrifying metallic electrical conductivity exhibited by two-dimensional (2D) transition metal carbides and nitrides have attracted tremendous interest for their utility in catalytic applications for $CO_2$ reduction reactions ($CO_2$RR), oxygen reduction reactions (ORR), and other related processes.[8-10] Anchoring single atoms to form single-atom catalysts (SACs) in 2D materials exhibits superior catalytic activity, enhances atom utilization and catalytic activity, and significantly reduces precious metal consumption and catalytic costs.[11, 12] This makes SACs also widely used in $N_2$ reduction reaction (NRR) research.[13-15] However, a significant obstacle to electrocatalytic $N_2$ reduction arises from the conflicting hydrogen evolution reaction (HER) and NRR processes, which result in subpar Faraday efficiency of the NRR.[16] Therefore, to enable effective and sustainable ammonia synthesis, it is crucial to find NRR electrocatalysts that exhibit the best catalytic activity and selectivity.

Porphyria is a distinct type of ligand with four pyridine nitrogen atoms, which, thanks to its stable macrocyclic structure, binds well to most metal ions and converts them into metallic porphyrins.[17] A type of metal-$N_4$ coordination compounds known as metalloporphyrin (MPP) complexes are widely used in the electrocatalytic reduction of $CO_2$ and $O_2$ processes.[18-20] Researchers have focused on the utilization of 2D-PP substrates to anchor a $3d$, $4d$, or $5d$ transition-metal atom and fabricate metalloporphyrin (MPP) as NRR electrocatalysts. This strategy has proven successful and has produced a series of catalysts with exceptionally low NRR onset potential and remarkable selectivity, such as ZrPP, NbPP, HfPP, and RePP.[21] Furthermore, by modifying the coordination environment of Co atoms on the CoPP catalyst, researchers have made significant progress in the catalytic performance of $CO_2$RR.[22] These works provide us with valuable inspiration for the development of highly active catalysts for NRR.

In this work, a systematic approach was used that utilized zirconium porphyrin (ZrPP) as a

substrate while introducing different proportions of C, N, and O atoms to optimize the coordination environment of Zr. Based on this strategy, we designed 15 different catalyst candidates and through comprehensive analysis identified the optimal catalysts in terms of performance and selectivity. The most effective pathways in the catalytic process were identified and validated using density functional theory (DFT). The results can provide theoretical predictions for the experiments.

### 2. COMPUTATIONAL DETAILS
All calculations in this work were carried out using the Vienna ab initio Simulation Package (VASP) with projector-augmented wave pseudopotentials.[23] The Perdew-Burke-Ernzerhof functional (PBE) of the generalized gradient approximation (GGA) was used to treat the electron exchange-correlation interaction. [24] The plane wave cutoff energy was set to 450 eV, and the structures were optimized until the force on each atom was less than 0.01 eV/Å. A 4x4x1 Γ-centered Monkhorst-Pack K-point grid was used for Brillouin zone sampling. A vacuum layer of 15 Å along the Z axis was added to prevent interactions between periodic images.[25-27] The DFT-D3 method was used to describe van der Waals interactions.[28] To account for the strong correlation effect, a Hubbard U value of 2.0 eV was added to the $d$ electron of the Zr atom.[29, 30] Preliminary calculations showed that considering the solvation effect caused the adsorption energy of $\ce{N_{2}}$ to shift by only 0.1 eV during the adsorption process, which significantly increases the computational effort and poses significant challenges.[24] For simplicity and to focus exclusively on the electronic structure and properties of the system, the solvation effect was intentionally neglected in this work.

The binding energy $(E_b)$ of anchoring the Zr atom to the 15 designed PP-A (A = $\ce{C_{4}}$, $\ce{C_{3}O}$, $\ce{C_{2}O_{2}-o}$, $\ce{C_{2}O_{2}-n}$, $\ce{CO_{3}}$, $\ce{O_{4}}$, $\ce{NC_{3}}$, $\ce{N_{2}C_{2}-o}$, $\ce{N_{2}C_{2}-n}$, $\ce{N_{3}C}$, $\ce{N_{4}}$, $\ce{ON_{3}}$, $\ce{O_{2}N_{2}-o}$, $\ce{O_{2}N_{2}-n}$, and $\ce{O_{3}N}$) substrate in a 2D PP monolayer was calculated using the following equation (1):
$$
E_{b}=E_{M P P}-E_{P P}-E_{M} \tag{1}
$$
where $E_{MPP}$, $E_{PP}$ and $E_M$ represent the energy of the MPP unit, the PP substrate and the M atom, respectively. $\ce{X_{2}Y_{2}-o}$, and $\ce{X_{2}Y_{2}-n}$ were use to denote the structure in which the same atoms occupy opposite and neighboring coordinations, respectively.

The cohesive energy $(E_c)$ was calculated using the following equation (2):
$$
E_{c}=\left(n \times E_{M(single)}-E_{M(bulk)}\right) / n \tag{2}
$$
where $\mathrm{E}_{M \text { (single) }}$, $\mathrm{E}_{M \text { (bulk) }}$, and $n$ represent the energy of an M atom in vacuum, the energy of the bulk metal crystal, and the number of M atoms in the bulk metal crystal, respectively.

The Gibbs free energy calculations involving electron/proton transfer were performed using the Computational Hydrogen Electrode (CHE) model, which was first introduced by Nørskov et al. [31] in the following equation (3):
$$
G=E_{\mathrm{DFT}}+E_{\mathrm{ZPE}}-T S \tag{3}
$$

Where $E_{DFT}$, $E_{ZPE}$, and $TS$ are the ground-state energy, the zero-point energies, and the entropy terms, respectively, with the latter two obtained from vibration frequencies from DFT calculations. Here $T$ stands for the thermodynamic temperature (298.15 K)

The overpotential ($\eta$) of the entire reduction process is calculated by $\eta = U_{eq} - U_{lim}$. In this formula, $U_{eq}$ is the equilibrium potential of NRR (approximately 0.17 V),[32] and $U_{lim}$ is the limit potential, obtained by $U_{lim} = -\Delta G_{max}/e$, with $\Delta G_{max}$ being the most positive $\Delta G$ in NRR.

## 3 RESULTS AND DISCUSSION
The detailed structural information of the 15 optimized ZrPP-A monolayers (including the top view of the crystal structure, space group, bond lengths, and bond angles) is depicted in Figure 1. In ZrPP-A, the Zr center binds to four coordination atoms and forms a five-membered ring. The different coordination structures of Zr can result in different $d$-electron configurations, which can be revealed through projected density of states (PDOS) analysis, and will be discussed later in detail. The binding energies that can be used to evaluate the binding strength between Zr atoms and these 15 substrates are calculated and presented in Table 1. To estimate the extent of charge transfer between Zr atoms and ligands, Bader charge calculations were performed. Figure 2 shows the relationship between the collective values of $E_b$+$E_c$ and the gain and loss of charges of Zr atoms in different ZrPP-A catalysts. There is a consistent trend between the value of $E_b$+$E_c$ and charge transfer. The more charges the Zr atom accumulates, the easier it is to bind to the ligand and form a more stable catalyst. For A=$CO_3$, $NO_3$, and $O_4$, $E_b$+$E_c$ > 0, indicating that Zr atoms tend to cluster in these coordination environments. Therefore, these 3 candidates should be excluded from the designed 15 candidate configurations.

The paper is organized as follows: In Section 3.1, a "four-step" screening strategy is performed to screen potential ZrPP-A candidates as NRR electrocatalysts. This was followed by a comprehensive investigation of all potential NRR reaction pathways on the screened catalysts in Section 3.2. Section 3.3 describes the use of the spin polarization DFT method to calculate the electronic structures of these candidates and allows us to delve deeper into the intricate details of the orbital hybridization and electron transfer of the $N_2$-ZrPP-A catalyst. Finally, *ab initio* molecular dynamics simulation (AIMD) is performed to evaluate the thermodynamic stability of the screened ZrPP-A monolayer.

### 3.1 Four-step screening.
The spontaneous adsorption of $N_2$ on the catalyst surface is a necessary prerequisite for NRR. Two types of adsorption geometries were considered for $N_2$ binding, including end-on and side-on adsorption morphologies. The optimized adsorption morphologies are shown in Figure 3.

The participation of both the first and the last proton-electron pairs in the NRR reaction is crucial, as this typically requires much more energy input than the intermediate steps. We set the Gibbs free energy difference before and after adsorption of proton-electron pairs to 0.8 eV. Finally, by comparing the competitive relationship between $N_2$ molecules and $H^+$ at the adsorption site, a group of more promising NRR catalysts is selected. Associated ZPE and TS data were calculated and listed in Table 2. The specific process is as follows:

Step 1: Catalysts with changes in the Gibbs free energy of $N_2$ adsorbed on the ZrPP-A catalyst of less than 0 eV are selected. The adsorption of $N_2$ on these candidates occurred in two different configurations, as shown in Figure 4(a) for "end-on" and Figure 4(b) for "side-on", respectively. It is worth noting that $N_2$ adsorbed in a side-on configuration on ZrPP-$C_4$, ZrPP-$NC_3$ and ZrPP-$N_2C_2$-$o$ catalysts transitions to the end-on configuration during structure optimization. The $N\equiv N$ bond length of the adsorbed $N_2$ on ZrPP-A catalysts is calculated and compared in Figure 4(c) and Figure 4(d). Specific values are listed in Table 3. All adsorption Gibbs free energies are negative and the $N\equiv N$ bond length adsorbed on the catalyst increases, indicating that $N_2$ can adsorb spontaneously on all ZrPP-A and that the $N\equiv N$ bond was activated by these candidates. All 12 designed candidates qualified for this step.

Step 2: Catalysts with a Gibbs free energy change of the first proton transfer to ZrPP-A*$N_2$ of less than 0.8 eV are selected to ensure a lower onset potential. All possible configurations are shown in Figure 5(a) for end-on and Figure 5(b) for side-on, respectively. The Gibbs free energy change of the first and last proton-electron pair transfer steps on the ZrPP-A is listed in Table 4. The Gibbs free energy changes of both absorption configurations are larger than 0.8 eV, which is a sufficient condition for the unqualified catalysts. The ZrPP-A catalyst (A=$C_4$, $NC_3$, and $N_2C_2$-$o$) should be excluded in this step.

Step 3: Catalysts with a Gibbs free energy change of the last proton transfer step on the ZrPP-A of less than 0.8 eV are selected. As shown in Figure 5(c), ZrPP-$ON_3$, ZrPP-$O_2N_2$-$o$, and ZrPP-$O_2N_2$-$n$ were excluded in this step.

Step 4: Catalysts that can promote the adsorption and activation of $N_2$ while inhibiting the competing HER were selected. Because HER and NRR have comparable reaction potentials, and HER often has a lower potential than NRR under acidic and alkaline conditions. The molecular dynamics approach was used to simulate the adsorption process of $N_2$ and $H^+$ on the catalyst surface at room temperature, as shown in Figure 6 and Figure S1 in ESM. Through trajectory and radial distribution function analysis, it was found that only the ZrPP-$N_3C$ catalyst had comprehensive coverage of the adsorption sites by $H^+$. The remaining catalysts showed mixed absorption of *$N_2$ and *$H^+$, with $N_2$ adsorption equal to or exceeding the amount of $H^+$. It is worth noting that *$N_2$ coverage of almost all adsorption sites on the ZrPP-$C_3$O. ZrPP-$N_3C$ was excluded in this step.

### 3.2 Reaction pathway of NRR.

Only 5 candidates successfully passed the four-step selection criteria: ZrPP-C₃O, ZrPP-N₄, ZrPP-N₂C₂-o, ZrPP-C₂O₂-o, and ZrPP-C₂O₂-n. We comprehensively investigated the complete NRR pathways of these selected candidates, including four direct pathways: Distal (D-pathway), Alternating (A-pathway), Consecutive (C-pathway), and Enzymatic (E-pathway), as well as some other hybrid pathways such as Distal-Alternating (DA-path), Distal-Alternating-Distal (DAD-path), Consecutive-Enzymatic (CE-path), Consecutive-Enzymatic-Consecutive paths (CEC-path), and so on, as shown in Figure 7. The path with the smallest change in Gibbs free energy was selected as the optimal reaction path for the potential determining step (PDS).

The limit step with the smallest change in the Gibbs free energy is depicted in Figure 8 using the example of the ZrPP-C₃O catalyst. The Gibbs free energy diagrams of NRR for the remaining four candidates can be found in Figure S2. Reaction path diagrams illustrating the nonminimal Gibbs free energy changes in the rate-limiting steps for these five catalysts can be found in Figure S3, while the unique structure marked in red are shown in Figure S4.

The Gibbs free energy diagram of the EC-path for NRR on ZrPP-C₃O catalyst is illustrated in Figure 8(a). Initially, N₂ adsorbs on the ZrPP-C₃O catalyst in the side-on configuration, resulting in a Gibbs free energy change of -2.06 eV. Alternating attacks of three proton-electron pairs ($\text{H}^{+} + \text{e}^{-}$) on two N atoms produce *N-*NH (distant) or *NH (proximal)-*N, *NH-*NH, and *NH-*NH₂ (distant) species with Gibbs free energy changes of 0.32 or 0.45, -0.35, and -0.47 eV, respectively. *NH-*NH₂ (distant) reacts with a following $\text{H}^{+} + \text{e}^{-}$ pair to produce the first NH₃ molecule with a Gibbs free energy change of 0.47 eV. The remaining *NH continues to react with the following two $\text{H}^{+} + \text{e}^{-}$ pairs, sequentially forming *NH₂ and *NH₃, with Gibbs free energy changes of -2.07 and 0.31 eV, respectively. As shown in Figure 8(b), the PDS of the EC-path is $\text{*NH-*NH}_{2}\text{ (distant)} + \text{H}^{+} + \text{e}^{-} \rightarrow \text{*NH} + \text{NH}_{3}\text{(g)}$, with the onset potential of -0.47 V. The Gibbs free energy change for the second NH₃ molecule from *NH₃ is 3.03 eV. N₂ adsorption on ZrPP-C₃O catalyst in a side-on configuration results in a change in Gibbs free energy of -2.06 eV as shown in Figure 8(c), indicating that a reaction pathway made up of CEC-path is favored. Two proton-electron pairs ($\text{H}^{+} + \text{e}^{-}$) continuously attack the distant N to form *N-*NH (distant) and *N-*NH₂ (distant) sequentially, and the third proton-electron pair attacks the proximal N form *NH-*NH₂ (distant), with Gibbs free energy changes of 0.32, 0.30, and -1.24 eV, respectively. The subsequent reaction path and changes in Gibbs free energy are the same as in the last part of Figure 8(a). The spontaneous adsorption of N₂ and the energy released during the hydrogenation process can promote the rapid desorption of NH₃ molecules at room temperature.[21] The onset potential of the hybrid pathway is lower than that of the four direct pathways, suggesting that the ZrPP-C₃O-catalyzed NRR is preferable to the hybrid pathway.

In summary, numerous reaction pathways for NRR were discovered and investigated on the five selected ZrPP-A catalysts, which exhibit low onset potential, indicating high catalytic

activity.

### 3.3 Origin of high activity for NRR.

According to previous research, the high catalytic performance of these selected ZrPP-A catalysts can be evaluated from two perspectives: orbital hybridization and electron transfer. Spin-polarized density functional theory (DFT) calculations were employed to determine the electronic structure of these 5 selected ZrPP-A catalysts. The projected density of states (PDOS) before and after N₂ adsorption on ZrPP-C₃O catalyst are depicted in Figure 9, and the PDOS of the other four candidates can be found in Figure S5. From Figure 9 and Figure S5, the primary contribution of the valence-band maximum (VBM) comes from the hybridization between the Zr-4*d* orbitals and the 2*p* orbital of the surrounding coordination atoms, but the conduction-band minimum (CBM) is contributed by the unoccupied *d* orbitals of Zr marked. PDOS analysis shows how different coordination atoms can alter the *d* electron configuration of Zr. Figure 9 shows that a square-planar coordinated crystal field divides degenerate *d* orbitals of Zr into four groups: doubly degenerate $d_{xz}$ and $d_{yz}$ orbitals, and nondegenerate $d_{x^2-y^2}$, $d_{z^2}$, and $d_{xy}$ orbitals. Apparent $\pi$ bonds are induced by the strong coupling between 2*p* orbitals of coordination atoms and 4*d* orbitals of the central Zr atom, as shown in Figure 9. And it is clear that asymmetric coordination environments result in differences in coupling modes between atoms. No significant bond can be found between the central Zr and coordinating O atoms. This is attributed to the strong coupling between O and its adjacent C. Zr and coordination atoms can easily undergo electron transfer, which efficiently contributes to the stabilization of the Zr atom, and promotes electrocatalysis, as shown Figure 10. The oxidation state of Zr is higher in ZrPP-N₄ than in ZrPP-C₄ and ZrPP-O₄, which is due to the higher electronegativity of pyridine N compared to the coordination of C and O, with O gaining sufficient electrons from neighboring C with lower electronegativity. A significant decrease in charge transfer between Zr and the coordinating O atom indicates a much weaker interaction between Zr and the coordinating O atoms. The charge originally surrounding the Zr atom is redistributed among the coordinating atoms, indicating that the central Zr atom is positively charged. This not only ensures that N₂ is easily absorbed, but also prevents H⁺ from approaching Zr and forming *H, effectively inhibiting HER.

Significant charge transfer was also observed when N₂ was anchored to the ZrPP-C₃O catalyst, suggesting strong interaction between N₂ molecules and Zr. The electron density accumulation regions are mainly concentrated in the Zr-N bond, indicating that the Zr-N bond is strengthened by electron transfer. This strong interaction between N₂ and Zr is desirable in catalytic processes that require N₂ activation and functionalization. As shown in Figure 10, the unoccupied *d* orbitals of the Zr atom accept the lone pairs of electrons from the $\sigma_{\text{g}}$ orbitals of the N₂ molecules, during N₂ adsorption on the ZrPP-A catalysts. Simultaneously, the occupied

$d$ orbitals of the Zr atoms contribute electrons to the unoccupied $\pi^{*}$ anti-bonding orbital of $N_{2}$, facilitating efficient electron transfer. The charge density difference of the remining 4 candidates before and after $N_{2}$ adsorption in two different configurations are shown in Figure S6. Noteworthy in this context are the accepting-donating mechanism and the strong orbital interactions between the Zr atom and the adsorbed $N_{2}$: the Zr atom has partially filled $d$ orbitals, while the $N_{2}$ molecule occupies $\sigma_{g}$ orbitals and vacant $\pi^{*}$ anti-bonding orbitals. An asymmetric coordination environment leads to an asymmetric charge distribution of the substrate, resulting in the adsorbed $N_{2}$ molecule being oriented toward the C coordination atom.

For further analysis, the charge changes of the intermediates in the optimal NRR path on the five catalysts were calculated, where the charge change refers to the difference between consecutive steps of each intermediate, as shown in Figure 11 and Figure S7. Here each intermediate is divided into three parts: part 1 (PP substrate without Zr-A), part 2 (Zr-A), and part 3 (adsorbed $N_{2}$). During the NRR process, significant charge transfer occurred between the adsorbent and the substrate, while the charge on the Zr atom barely changed, which means that Zr plays a role of coordinating the charge transfer process, with the coordinating atoms and the PP moiety acting as electron donor or acceptor reservoirs. Together they supply the adsorbate with additional charges or accept excess charges.

In addition to the broad application of adsorption energy and active site vacancy formation energy, Norskov *et al.* extended the $d$-band center theory to predict the catalytic activity of NRR. The $d$-band center $(\varepsilon_{d})$ of Zr before and after $N_{2}$ adsorption is calculated and shown in Figure 9 and Figure S5. The results show that the $d$-band center of Zr moves toward the Fermi level after $N_{2}$ adsorption, which means that the anti-bonding orbital of the adsorbed $N_{2}$ is induced to a higher level, thereby enhancing the interaction between the adsorption surface and the $N_{2}$ reinforces and promotes the charge transfer between the Zr atom and $N_{2}$.

Overall, the optimal coordination environment has a significant impact on charge transfer and overall catalytic performance. Therefore, when developing catalysts, it is crucial to consider not only the single-atom catalyst itself but also its coordination environment.

### 3.4 Thermodynamic stability of ZrPP-A.

To evaluate the thermodynamic stability of these selected ZrPP-A catalysts, *ab initio* molecular dynamics simulations (AIMD) were performed. These simulations were performed with $4{\times}4{\times}1$ supercells at 500 K for 10 ps with a time step of 1 fs. As shown in Figure 12 and Figure S8, the overall surface morphology of these candidates remained unchanged throughout the simulation. The Zr atoms protruded only slightly from the surface but remained tightly coupled to the surrounding ligands, indicating their thermodynamic stability in thermal equilibrium. Due to their high stability at 500 K demonstrated by AIMD simulations, it is stated that these selected ZrPP-A catalysts could be used as efficient and long-lasting NRR

catalysts under reaction conditions.

## 4. CONCLUSIONS
In this work, ZrPP is selected as a substrate and the coordination environment of Zr is altered through coordination engineering, aiming to select efficient electrocatalysts for NRR. Five promising catalysts were identified through a four-step screening process, with ZrPP-$C_3$O showing the highest stability and activity for $N_2$ adsorption. The Gibbs free energy diagram revealed that the hybrid path has lower onset potentials than the four direct paths in the NRR. The electronic structure, Bader charge, and $d$-band center analysis of these selected catalysts were calculated and analyzed. The results indicate significant orbital hybridization between the coordinating atoms and the Zr atom, which contributed to the stability of Zr within the substrate. This work highlights the importance of considering the coordination environment of metal atoms when designing single-atom catalysts. Analysis of the electronic structures of catalysts has also revealed the sources of their catalytic activity. These results provide valuable insights and a foundation for the development of similar catalysts in future research efforts.

### Acknowledgments
This work was supported by Natural Science Basic Research Plan in Shaanxi Province of China(No. S2020-JC-QN-0623), the Natural Science Foundation of Shaanxi Province of China (No. 2020JQ-568), and the Double First-class University Construction Project of Northwest University.

### Electronic Supplementary Material

### References
1.  Du Feng, et al., *Recent progress in electrochemical synthesis of carbon-free hydrogen carrier ammonia and ammonia fuel cells: A review.* Materials Reports: Energy, 2022. **2**(4).
2.  Kyriakou, V., et al., *An Electrochemical Haber-Bosch Process.* Joule, 2020. **4**(1): p. 142-158.
3.  van Langevelde, P.H., I. Katsounaros, and M.T.M. Koper, *Electrocatalytic Nitrate Reduction for Sustainable Ammonia Production.* Joule, 2021. **5**(2): p. 290-294.
4.  Erisman, J.W., et al., *How a century of ammonia synthesis changed the world.* Nature Geoscience, 2008. **1**(10): p. 636-639.
5.  Wang, M., et al., *Can sustainable ammonia synthesis pathways compete with fossil-fuel based Haber-Bosch processes?* Energy & Environmental Science, 2021. **14**(5): p. 2535-2548.
6.  Chen, Q., et al., *An Overview on Noble Metal (Group VIII)-based Heterogeneous Electrocatalysts for Nitrogen Reduction Reaction.* Chem Asian J, 2020. **15**(24): p. 4131-4152.
7.  Feng, J. and H. Pan, *Electronic state optimization for electrochemical N2 reduction reaction in aqueous solution.* Journal of Materials Chemistry A, 2020. **8**(28): p. 13896-13915.
8.  Deng, Q., et al., *2D transition metal-TCNQ sheets as bifunctional single-atom catalysts for oxygen reduction and evolution reaction (ORR/OER).* Journal of Catalysis, 2019. **370**: p. 378-384.
9.  Lin, Z.Z., et al., *Electrochemical CO2 reduction in confined space: Enhanced activity of metal catalysts by graphene overlayer.* J International Journal of Energy Research, 2019. **44**: p. 784 - 794.
10. Zhu, X. and Y. Li, *Advances in two dimensional electrochemical catalysts for ammonia synthesis.* Chinese Science Bulletin, 2020. **66**(6): p. 625-639.

11. Gao, Y., et al., *A theoretical study of electrocatalytic ammonia synthesis on single metal atom/MXene.* Chinese Journal of Catalysis, 2019. **40**(2): p. 152-159.

12. Zheng, S., et al., *Electrochemical Nitrogen Reduction Reaction Performance of Single-Boron Catalysts Tuned by MXene Substrates.* J Phys Chem Lett, 2019. **10**(22): p. 6984-6989.

13. Chen, Y., et al., *Single-Atom Catalysts: Synthetic Strategies and Electrochemical Applications.* Joule, 2018. **2**(7): p. 1242-1264.

14. Pan, Y., et al., *Structural Regulation with Atomic-Level Precision: From Single-Atomic Site to Diatomic and Atomic Interface Catalysis.* Matter, 2020. **2**(1): p. 78-110.

15. Xu, L., L.M. Yang, and E. Ganz, *Electrocatalytic Reduction of N(2) Using Metal-Doped Borophene.* ACS Appl Mater Interfaces, 2021. **13**(12): p. 14091-14101.

16. Fu, C., et al., *Theoretical Exploration of the Thermodynamic Process Competition between NRR and HER on Transition-Metal-Doped CoP (101) Facets.* The Journal of Physical Chemistry C, 2021. **125**(31): p. 17051-17057.

17. Strianese, M., et al., *The contribution of metalloporphyrin complexes in molecular sensing and in sustainable polymerization processes: a new and unique perspective.* 2021.

18. Amanullah, S., et al., *Tuning the thermodynamic onset potential of electrocatalytic O2 reduction reaction by synthetic iron-porphyrin complexes.* Chem Commun (Camb), 2015. **51**(49): p. 10010-3.

19. Li, R., et al., *Bioinspired Mo tape-porphyrin as an efficient and selective electrocatalyst for ammonia synthesis.* Applied Surface Science, 2020. **520**.

20. Liu, J.-H., L.-M. Yang, and E. Ganz, *Electrocatalytic reduction of CO2 by two-dimensional transition metal porphyrin sheets.* Journal of Materials Chemistry A, 2019. **7**(19): p. 11944-11952.

21. Huang, C.-X., et al., *Single-atom catalysts based on two-dimensional metalloporphyrin monolayers for ammonia synthesis under ambient conditions.* Nano Research, 2022. **15**(5): p. 4039-4047.

22. Zhou, H., et al., *Coordination Engineering in Cobalt-Nitrogen-Functionalized Materials for CO(2) Reduction.* J Phys Chem Lett, 2019. **10**(21): p. 6551-6557.

23. Hafner, J., *Ab-initio simulations of materials using VASP: Density-functional theory and beyond.* J Comput Chem, 2008. **29**(13): p. 2044-78.

24. Perdew, J.P., K. Burke, and M. Ernzerhof, *Generalized Gradient Approximation Made Simple.* Phys Rev Lett, 1996. **77**(18): p. 3865-3868.

25. Henkelman, G., A. Arnaldsson, and H. Jónsson, *A fast and robust algorithm for Bader decomposition of charge density.* Computational Materials Science, 2006. **36**(3): p. 354-360.

26. Sanville, E., et al., *Improved grid-based algorithm for Bader charge allocation.* J Comput Chem, 2007. **28**(5): p. 899-908.

27. Tang, W., E. Sanville, and G. Henkelman, *A grid-based Bader analysis algorithm without lattice bias.* J Phys Condens Matter, 2009. **21**(8): p. 084204.

28. Grimme, S., et al., *A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu.* Journal of Chemical Physics, 2010. **132**(15).

29. Schulz, H.J., *Correlation exponents and the metal-insulator transition in the one-dimensional Hubbard model.* Phys Rev Lett, 1990. **64**(23): p. 2831-2834.

30. Zhang, Y., V. Ji, and K.-W. Xu, *The detailed geometrical and electronic structures of monoclinic zirconia.* Journal of Physics and Chemistry of Solids, 2013. **74**(3): p. 518-523.

31. Nørskov, J.K., et al., *Origin of the Overpotential for Oxygen Reduction at a Fuel-Cell Cathode.* The Journal of Physical Chemistry B, 2004. **108**(46): p. 17886-17892.

32. Li, L., J.M.P. Martirez, and E.A. Carter, *Prediction of Highly Selective Electrocatalytic Nitrogen Reduction at Low Overpotential on a Mo-Doped g-GaN Monolayer.* ACS Catalysis, 2020. **10**(21): p. 12841-12857.

Figure 1. The optimized equilibrium structures of the 15 designed ZrPP-A catalyst candidates.

![](./images/941032231814562061_1.jpg)

Figure 2. The sum of $E_b$+$E_c$ (in red balls) and the gain and loss charges of Zr atoms (in blue balls) in different ZrPP-A catalyst candidates, where $E_b$ is the binding energy and $E_c$ is the cohesion energy.

![](./images/941032231814562061_2.jpg)

Figure 3. Front view and top view of $N_2$ adsorption on the ZrPP-A. (a) end-on adsorption configuration, (b) side-on adsorption configuration.

![](./images/941032231814562061_3.jpg)

Figure 4. Gibbs free energy change of $N_2$ adsorbed on ZrPP-A, (a) $N_2$ adsorbed in an end-on configuration, (b) $N_2$ adsorbed in a side-on configuration, with $ZrPP-C_4$, $ZrPP-NC_3$, and $ZrPP-N_2C_2$-o catalysts that transition to the end-on configuration during structure optimization. The length of the $N\equiv N$ bond after $N_2$ adsorption in the end-on adsorption configuration (c) and in the side-on adsorption configuration (d).

![](./images/941032231814562061_4.jpg)

Figure 5. Gibbs free energy change of the first proton-electron pairs $(H^+ + e^-)$ on $N_2$ adsorbed on ZrPP-A in an end-on configuration (a), and in a side-on configuration (b). And the Gibbs free energy change of the last proton-electron pairs $(H^+ + e^-)$ attacks $^*NH_2$ adsorbed on ZrPP-A.

![](./images/941032231814562061_5.jpg)

Figure 6. The distribution function of the N atom centered in the Zr atom (blue curve) and the distribution function of the H atom centered in the Zr atom (green curve). The initial and thermal equilibrium structures of the molecular dynamic simulation are shown on the right.

![](./images/941032231814562061_6.jpg)

Figure 7. Part I shows that C, N, and O atoms are exchanged in pairs to form a ZrPP-A catalyst. Part II shows two configurations of N₂ adsorption. Part III shows four direct reaction paths of NRR on the ZrPP-A catalyst: Distal, Alternating, Consecutive, and Enzymatic, as well as partial hybrid paths such as Distal-Alternating, Distal-Alternating-Distal, Consecutive-Enzymatic, Consecutive-Enzymatic-Consecutive and so on.

![](./images/941032231814562061_7.jpg)

Figure 8. Gibbs free energy diagrams of the NRR on the ZrPP-C₃O catalyst experiencing the Enzymatic-consecutive (a), (b), and Consecutive-enzymatic-consecutive (c) hybrid pathway at zero potential and onset potential. The two Gibbs free energy values of the PDS are marked in red.

![](./images/941032231814562061_8.jpg)

Figure 9. Energy band structure and PDOS of ZrPP-C₃O before N₂ adsorption (a), and after N₂ adsorption (b). A Pink area represents the Zr-4d orbital, the blue lines represent the 2p orbitals of the coordination atoms around Zr, and the green line represents the N₂-2p orbital.

![](./images/941032231814562061_9.jpg)

Figure 10. The charge density difference of ZrPP-C₃O (a), side view (b) and corresponding top view (c) of the charge density difference after N₂ adsorption in side-on configuration. Yellow and blue colors refer to electron accumulation and depletion regions, respectively.

![](./images/941032231814562061_10.jpg)

Figure 11. (a) Definition of the three parts of NₓHᵧ-ZrPP-A system: (1) PP substrate without Zr-A, (2) Zr-A, A = C₃O, N₄, N₂C₂-n, C₂O₂-n, and C₂O₂-o, and (3) adsorbed NₓHᵧ. (b)-(d) Bader charge variation of the NRR on the ZrPP-C₃O catalyst via three optimal paths.

![](./images/941032231814562061_11.jpg)

Figure 12. Energy and temperature fluctuations versus the AIMD simulation time for ZrPP-
C₃O. The insets show the corresponding geometry configurations for ZrPP-C₃O after AIMD
simulations.

![](./images/941032231814562061_12.jpg)

**Table 1.** The binding energy ($E_b$), $E_b + E_c$ of the ZrPP-A catalysts, and the Bader charge of the Zr atom, the cohesion energy $E_c$=6.57eV for all candidates.

<table>
  <thead>
    <tr>
      <th>Coordinated environment</th>
      <th>$E_b$ (eV)</th>
      <th>$E_b + E_c$ (eV)</th>
      <th>Change in Bader charge for Zr ($e$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zr-CO₃</td>
      <td>-5.30</td>
      <td>1.27</td>
      <td>-1.65</td>
    </tr>
    <tr>
      <td>Zr -C₂O₂-n</td>
      <td>-8.18</td>
      <td>-1.61</td>
      <td>-2.08</td>
    </tr>
    <tr>
      <td>Zr -C₂O₂-o</td>
      <td>-8.25</td>
      <td>-1.68</td>
      <td>-2.09</td>
    </tr>
    <tr>
      <td>Zr -C₃O</td>
      <td>-9.13</td>
      <td>-2.56</td>
      <td>-2.10</td>
    </tr>
    <tr>
      <td>Zr -C₄</td>
      <td>-10.07</td>
      <td>-3.50</td>
      <td>-2.23</td>
    </tr>
    <tr>
      <td>Zr -NC₃</td>
      <td>-10.07</td>
      <td>-3.50</td>
      <td>-2.19</td>
    </tr>
    <tr>
      <td>Zr -N₂C₂-o</td>
      <td>-10.29</td>
      <td>-3.72</td>
      <td>-2.22</td>
    </tr>
    <tr>
      <td>Zr -N₂C₂-n</td>
      <td>-10.70</td>
      <td>-4.13</td>
      <td>-2.27</td>
    </tr>
    <tr>
      <td>Zr -N₃C</td>
      <td>-10.78</td>
      <td>-4.21</td>
      <td>-2.27</td>
    </tr>
    <tr>
      <td>Zr -N₄</td>
      <td>-11.64</td>
      <td>-5.07</td>
      <td>-2.33</td>
    </tr>
    <tr>
      <td>Zr -ON₃</td>
      <td>-9.72</td>
      <td>-3.15</td>
      <td>-1.85</td>
    </tr>
    <tr>
      <td>Zr -O₂N₂-o</td>
      <td>-7.10</td>
      <td>-0.53</td>
      <td>-1.67</td>
    </tr>
    <tr>
      <td>Zr -O₂N₂-n</td>
      <td>-6.93</td>
      <td>-0.36</td>
      <td>-1.65</td>
    </tr>
    <tr>
      <td>Zr -O₃N</td>
      <td>-4.38</td>
      <td>2.19</td>
      <td>-1.51</td>
    </tr>
    <tr>
      <td>Zr -O₄</td>
      <td>-1.53</td>
      <td>5.04</td>
      <td>-1.35</td>
    </tr>
  </tbody>
</table>

**Table 2.** Thermal corrections of different adsorbed substances: zero-point energy (ZPE) and entropy correction (TS). *N-N and *N-*N represent the end-on and side-on adsorption configurations, respectively. Where "▲" indicates that the structure does not exist after structural optimization.

<table>
  <thead>
    <tr>
      <th rowspan="2">adsorbed species</th>
      <th colspan="6">ZrPP-A catalysts: E<sub>ZPE</sub>/TS (eV)</th>
    </tr>
    <tr>
      <th>C₃O</th>
      <th>N₄</th>
      <th>N₃C</th>
      <th>N₂C₂-n</th>
      <th>C₂O₂-o</th>
      <th>C₂O₂-n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>*N-N</td>
      <td>0.18/0.20</td>
      <td>0.19/0.19</td>
      <td>0.19/0.19</td>
      <td>0.18/0.20</td>
      <td>0.18/0.20</td>
      <td>0.19/0.18</td>
    </tr>
    <tr>
      <td>*N-NH</td>
      <td>0.45/0.20</td>
      <td>0.43/0.24</td>
      <td>0.43/0.22</td>
      <td>0.43/0.23</td>
      <td>0.46/0.19</td>
      <td>0.44/0.21</td>
    </tr>
    <tr>
      <td>*N-NH₂</td>
      <td>0.76/0.26</td>
      <td>0.76/0.27</td>
      <td>0.78/0.16</td>
      <td>0.76/0.27</td>
      <td>0.76/0.26</td>
      <td>0.79/0.21</td>
    </tr>
    <tr>
      <td>*N</td>
      <td>0.03/0.12</td>
      <td>0.04/0.10</td>
      <td>0.04/0.10</td>
      <td>0.04/0.11</td>
      <td>0.04/0.11</td>
      <td>0.05/0.11</td>
    </tr>
    <tr>
      <td>*NH</td>
      <td>0.32/0.12</td>
      <td>0.33/0.11</td>
      <td>0.33/0.11</td>
      <td>0.32/0.12</td>
      <td>0.33/0.12</td>
      <td>0.34/0.11</td>
    </tr>
    <tr>
      <td>*NH₂</td>
      <td>0.64/0.15</td>
      <td>0.63/0.18</td>
      <td>0.64/0.16</td>
      <td>0.62/0.13</td>
      <td>0.65/0.13</td>
      <td>0.63/0.16</td>
    </tr>
    <tr>
      <td>*NH₂</td>
      <td>1.01/0.19</td>
      <td>1.01/0.16</td>
      <td>1.00/0.15</td>
      <td>1.00/0.16</td>
      <td>1.01/0.18</td>
      <td>1.01/0.19</td>
    </tr>
    <tr>
      <td>*NH-NH</td>
      <td>0.78/0.23</td>
      <td>0.78/0.23</td>
      <td>0.79/0.23</td>
      <td>0.78/0.24</td>
      <td>▲</td>
      <td>0.79/0.22</td>
    </tr>
    <tr>
      <td>*NH-NH₂</td>
      <td>1.11/0.25</td>
      <td>▲</td>
      <td>▲</td>
      <td>▲</td>
      <td>1.11/0.25</td>
      <td>▲</td>
    </tr>
    <tr>
      <td>*NH₂-NH₂</td>
      <td>1.47/0.27</td>
      <td>▲</td>
      <td>▲</td>
      <td>▲</td>
      <td>▲</td>
      <td>1.48/0.24</td>
    </tr>
    <tr>
      <td>*N-*N</td>
      <td>0.17/0.21</td>
      <td>0.17/0.21</td>
      <td>0.18/0.19</td>
      <td>0.17/0.20</td>
      <td>0.18/0.19</td>
      <td>0.18/0.19</td>
    </tr>
    <tr>
      <td>*N-*NH</td>
      <td>0.47/0.20(far)<br>0.47/0.14(near)</td>
      <td>0.48/0.18</td>
      <td>0.47/0.14(far)<br>0.48/0.17(near)</td>
      <td>0.48/0.17(CC)<br>0.48/0.18(NN)</td>
      <td>0.48/0.17</td>
      <td>0.48/0.17(CC)<br>0.47/0.18(OO)</td>
    </tr>
    <tr>
      <td>*N-*NH₂</td>
      <td>0.78/0.15(far)<br>▲(near)</td>
      <td>▲</td>
      <td>▲(far)<br>0.81/0.18(near)</td>
      <td>0.77/0.23(CC)<br>▲(NN)</td>
      <td>0.80/0.19</td>
      <td>0.81/0.13(CC)<br>0.81/0.17(OO)</td>
    </tr>
    <tr>
      <td>*NH-*NH</td>
      <td>0.75/0.23</td>
      <td>0.76/0.22</td>
      <td>0.75/0.24</td>
      <td>0.74/0.20</td>
      <td>0.76/0.21</td>
      <td>0.74/0.25</td>
    </tr>
    <tr>
      <td>*NH-*NH₂</td>
      <td>1.12/0.22(far)<br>1.12/0.22(far)</td>
      <td>1.13/0.22</td>
      <td>1.13/0.22(far)<br>1.12/0.15(near)</td>
      <td>1.12/0.22(CC)<br>1.13/0.22(NN)</td>
      <td>1.12/0.17</td>
      <td>1.12/0.16(CC)<br>1.13/0.21(OO)</td>
    </tr>
    <tr>
      <td>*NH₂-*NH₂</td>
      <td>1.47/0.20</td>
      <td>1.47/0.22</td>
      <td>▲</td>
      <td>▲</td>
      <td>▲</td>
      <td>▲</td>
    </tr>
  </tbody>
</table>

Table 3. Changes in the Gibbs free energy of $N_2$ adsorbed on the ZrPP-A catalysts and activated
$N\equiv N$ bond length of $N_2$ adsorption on ZrPP-A catalyst

<table>
  <thead>
    <tr>
      <th rowspan="2">Coordinated environment</th>
      <th colspan="2">$\Delta G^{*}N_2$(eV)</th>
      <th colspan="2">$N\equiv N$ bond length of $^*N_2$($\mathring{A}$)</th>
    </tr>
    <tr>
      <th>end-on</th>
      <th>side-on</th>
      <th>end-on</th>
      <th>side-on</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$N_4$</td>
      <td>-0.61</td>
      <td>-0.29</td>
      <td>1.134</td>
      <td>1.165</td>
    </tr>
    <tr>
      <td>$ON_3$</td>
      <td>-0.54</td>
      <td>-0.46</td>
      <td>1.148</td>
      <td>1.174</td>
    </tr>
    <tr>
      <td>$O_2N_2$-$o$</td>
      <td>-1.11</td>
      <td>-1.24</td>
      <td>1.152</td>
      <td>1.190</td>
    </tr>
    <tr>
      <td>$O_2N_2$-$n$</td>
      <td>-1.04</td>
      <td>-1.14</td>
      <td>1.153</td>
      <td>1.208</td>
    </tr>
    <tr>
      <td>$N_3C$</td>
      <td>-1.44</td>
      <td>-1.24</td>
      <td>1.133</td>
      <td>1.155</td>
    </tr>
    <tr>
      <td>$C_3O$</td>
      <td>-2.27</td>
      <td>-2.06</td>
      <td>1.131</td>
      <td>1.150</td>
    </tr>
    <tr>
      <td>$C_2O_2$-$o$</td>
      <td>-1.54</td>
      <td>-1.49</td>
      <td>1.143</td>
      <td>1.171</td>
    </tr>
    <tr>
      <td>$C_2O_2$-$n$</td>
      <td>-1.68</td>
      <td>-1.38</td>
      <td>1.136</td>
      <td>1.160</td>
    </tr>
    <tr>
      <td>$N_2C_2$-$n$</td>
      <td>-1.90</td>
      <td>-1.66</td>
      <td>1.132</td>
      <td>1.154</td>
    </tr>
    <tr>
      <td>$N_2C_2$-$o$</td>
      <td>-2.03</td>
      <td>$\leftarrow$</td>
      <td>1.130</td>
      <td>$\leftarrow$</td>
    </tr>
    <tr>
      <td>$NC_3$</td>
      <td>-2.48</td>
      <td>$\leftarrow$</td>
      <td>1.128</td>
      <td>$\leftarrow$</td>
    </tr>
    <tr>
      <td>$C_4$</td>
      <td>-3.02</td>
      <td>$\leftarrow$</td>
      <td>1.126</td>
      <td>$\leftarrow$</td>
    </tr>
  </tbody>
</table>

Table 4. Gibbs free energy change of the first and last proton-electron pair transfer steps on the
ZrPP-A

<table>
  <thead>
    <tr>
      <th rowspan="2">Coordinated environment</th>
      <th colspan="2">$\Delta G^{*_{N2}\rightarrow*_{N2H}}$(eV)</th>
      <th rowspan="2">$\Delta G^{*_{NH2}\rightarrow*_{NH3}}$(eV)</th>
    </tr>
    <tr>
      <th>end-on</th>
      <th>side-on</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$N_4$</td>
      <td>0.95</td>
      <td>0.36</td>
      <td>0.49</td>
    </tr>
    <tr>
      <td>$ON_3$</td>
      <td>0.58</td>
      <td>0.20</td>
      <td>1.30</td>
    </tr>
    <tr>
      <td>$O_2N_2$-$o$</td>
      <td>0.41</td>
      <td>-0.11</td>
      <td>1.29</td>
    </tr>
    <tr>
      <td>$O_2N_2$-$p$</td>
      <td>0.14</td>
      <td>0.04</td>
      <td>1.30</td>
    </tr>
    <tr>
      <td>$N_3C$</td>
      <td>1.06</td>
      <td>0.60</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>$C_3O$</td>
      <td>0.84</td>
      <td>0.32</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>$C_2O_2$-$o$</td>
      <td>0.67</td>
      <td>0.27</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td>$C_2O_2$-$n$</td>
      <td>0.88</td>
      <td>0.55</td>
      <td>0.41</td>
    </tr>
    <tr>
      <td>$N_2C_2$-$n$</td>
      <td>1.05</td>
      <td>0.31</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>$N_2C_2$-$o$</td>
      <td>0.91</td>
      <td>$\leftarrow$</td>
      <td></td>
    </tr>
    <tr>
      <td>$NC_3$</td>
      <td>1.09</td>
      <td>$\leftarrow$</td>
      <td></td>
    </tr>
    <tr>
      <td>$C_4$</td>
      <td>1.29</td>
      <td>$\leftarrow$</td>
      <td></td>
    </tr>
  </tbody>
</table>