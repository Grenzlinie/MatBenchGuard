# Formation of core (M₇C₃)-shell (M₂₃C₆) structured carbides in white cast irons: A thermo-kinetic analysis

Kun Wang, Dongyang Li*

Department of Chemical and Materials Engineering, University of Alberta, Edmonton, Canada T6G 1H9

---

## ARTICLE INFO

**Keywords:**
Core-shell structured carbides
Phase diagrams
Mechanism
White cast irons
Composition ranges
Nucleation driving force

## ABSTRACT

Core-shell structured carbides in white cast irons help reduce interfacial stress and failure, leading to higher resistance to wear. The present study is conducted to understand the mechanism for the formation of core-shell structured carbides in white cast irons through computational thermodynamics. In particular, efforts are made to determine the compositional ranges in which the core-shell structured carbides can form. Arrays of phase diagrams in stable and metastable equilibria were calculated to determine the stable regions of M₂₃C₆, M₇C₃ and Matrix, which are the basic phase assemblage for the core-shell morphology in high-Cr cast irons (HCCIs). Scheil-Gulliver and Lever-Rule solidifications were simulated for nine alloys with compositions selected from the stable/metastable regions to investigate the phase precipitation sequence, as-cast microstructures and compositions. The contour diagrams for the nucleation driving force were mapped and used to analyze the precipitating ability of each type and the configuration of carbide in its appropriate domains in casting during heat treatment. Thorough discussion is given to the effects of parent microstructure, temperature, and overall composition on the nucleation driving force for the M₂₃C₆ shell growth in order to guide fabrication of HCCIs with desired core-shell structured carbides.

---

## 1. Introduction

High-Chromium Cast Irons (HCCIs) have received great attention due to their high resistance to wear under different conditions encountered in various industrial sectors, e.g., cement manufacturing, mineral processing and slurry pumping [1–3]. Traditionally, chromium-base cast irons are classified into three groups in terms of the chromium content and applications in different technical areas: (1) the low-Cr irons with their Cr concentrations below 12 wt%, which are used for less severe wear situations, e.g., small grinding facilities; (2) the medium-Cr irons with their Cr concentration within 18–22 wt%, which are widely used as cost-effective materials to resist wear in many industrial applications; (3) HCCIs with their Cr concentration above 25 wt %, which are developed to provide resistance to wear and corrosive wear under very harsh working conditions such as wet grinding and high-velocity slurry transport. The HCCIs widely used in the oil sands and mining industries are usually in the hypereutectic state with their carbon content in the range of 2.7 wt%C or higher. The excellent performance of HCCIs is attributed to the combination of hard carbides (e.g., M₇C₃ and M₂₃C₆) and relatively ductile ferrous matrix (martensite and/or austenite). The matrix benefits the absorption of impact energy and enhances the fracture toughness of the material, while the hard carbides play a crucial role in withstanding the wearing stress [4,5]. Although the individual phases may possess superior mechanical properties, the carbide/matrix interface strongly influences the overall performance of HCCIs. For instance, primary M₇C₃ carbides largely contribute to the high hardness of HCCIs but the lattice mismatch stress at the interface between the hard carbide and soft matrix may raise the probability of interfacial failure and thus lower the alloys' fracture toughness. It was recently noticed that core (M₇C₃)-shell (M₂₃C₆)

---

Abbreviations: CALPHAD, Computer Coupling of Phase Diagrams and Thermochemistry; HCCIs, High-Chromium Cast Irons; E, eutectic reaction; P, peritectic reaction; U, übergangsebene reaction; SEM, scanning electron microscopy; Microstructure, the solidification morphology of castings such as austenite dendrites (FCC) and eutectic austenite (partially transformed to martensite or ferrite) with interdendritic eutectic M₇C₃ carbide; Matrix, austenite (FCC)/ferrite (BCC)/martensite (BCT) that encompasses M₇C₃ in castings; The eutectic colony, the eutectic microstructure composed of Matrix and M₇C₃; MLE, Metastable Local Equilibrium characterizing the interface state of the eutectic colony; The dichotomy composition, roughly standing for the compositional gradient from the inner matrix to the matrix interface which simplifies the driving-force computations; Matrices, austenite/ferrite/martensite in various eutectic colonies (varying in composition) precipitated from the Scheil-Gulliver cooling

* Corresponding author.
E-mail address: dongyang.li@ualberta.ca (D. Li).

https://doi.org/10.1016/j.commatsci.2018.07.032
Received 9 March 2018; Received in revised form 8 June 2018; Accepted 14 July 2018
0927-0256/ © 2018 Published by Elsevier B.V.

structured carbides formed in HCCIs exhibited advantageous influence on their wear resistance. This influence is mainly contributed to the decrease in hardness from the hardest core ($M_7C_3$), through medium hard shell ($M_{23}C_6$), to the relatively softer ferrous matrix [6-12], which reduces the stress concentration at the carbide/matrix interface and consequently minimizes the risk of interfacial failure as demonstrated by an illustrative finite element analysis [7,8,13]. The effectiveness of the shell in reducing interfacial failure is affected by the shell thickness [13]. If the shell is sufficiently thick, the wear resistance would be decreased due to the decrease in hardness of the carbide as a reinforcement. It has been experimentally observed that the core-shell carbide morphology is not only limited to the combination of $M_7C_3$ (core) and $M_{23}C_6$ (shell) but also reflected by the assemblages of $M_3C$ (shell)/$M_7C_3$ (core) and $M_{23}C_6$ (shell)/$M_6C$ (core) [14,15]. Thus, it is of importance to identify the fabrication conditions to achieve suitable core-shell structures and determine their impact on the overall mechanical and tribological properties of HCCIs.

The above-mentioned studies reported in the literature show the benefits of core-shell carbides to the mechanical behavior and wear resistance of the alloys and material processing conditions, such as temperature and alloy composition, where the core-shell carbides form in the alloys [7-10,13-16]. However, to the authors' knowledge, there are no studies reported in the literature regarding the formation mechanism, which is of importance to identification and control of key process parameters for production the core-shell structured carbides during alloy processing. The main objectives of this study based on thermo-kinetic analysis are (1) to clarify the mechanism for the formation of core-shell combinations, and (2) to identify the composition range and conditions, with which the $M_7C_3$ (core)-$M_{23}C_6$ (shell) structured carbides could be produced. In this study, we also analyze the driving force, which is related to the formability of the core-shell structured carbides in a quantitative manner.

The thermo-kinetic analysis in this study was conducted within the framework of the CALPHAD method, in which thermodynamics and phase diagrams are combined to deal with multicomponent alloy systems. This research area has been very active over past 30 years and received increasing attention for applications in computational material processing, development of structure-property relationships, prediction of material properties, and material design [17]. The CALPHAD method requires not only computational skills but also extensive thermodynamic database and versatile solution models, such as the compound energy formalism [18,19]. In this work, the Pandat thermodynamic software developed by Chen [20-23] is employed, which can handle various types of phase equilibria and thermodynamic calculations involving stable/metastable phase diagrams, liquidus projections, solidification paths and contour properties. The Fe-Cr-C ternary system is constructed on the thermodynamic database with the optimized parameters reported by Khvan [24]. With the established Fe-Cr-C model system, thermo-kinetic analysis can be conducted to investigate the formation of the core-shell structured carbides in HCCIs that may contain minor impurities such as Si, Mn, Al and P etc. (less than 2 wt%). As long as the impurities have their concentration less than 2 wt%, the influence of the impurities on phase equilibria and thermodynamic properties is negligible.

This article reports results of our computational analysis on the formation of core-shell structured carbides in terms of the formation mechanism and conditions. The results would help guide determining the adequate composition ranges and processing conditions in order to obtain core-shell structured carbides in fabricated HCCIs. The article has five parts, among which the Sections 2-4 present or report equilibrium phase diagrams, solidification-path analysis and post heat treatments. The stable/metastable phase diagrams manifest possible regions with two variables, temperature and composition, for the formation of core-shell structured carbides. In the solidification-path analysis, the solidification processes were simulated under rapid cooling and Lever-Rule cooling conditions using Scheil-Gulliver and Lever-Rule methods, respectively. Both of the methods may provide valuable information on the as-cast microstructures and corresponding microstructural composition distributions for the driving force calculation in post heat treatments. Post heat treatments for carbide precipitation are studied through analyzing driving forces for carbide nucleation in the inner matrix and at the eutectic $M_7C_3$/Matrix interface; the former generates secondary carbides while the latter creates the core-shell structure. Background information is provided in Section 1. Conclusions are drawn and given in Section 5.

![](./images/813011534031618049_1.jpg)

Fig. 1. The calculated stable phase diagrams for HCCIs in (a) 45%Cr; (b) 40%Cr; (c) 35%Cr; (d) 30%Cr; (e) 25%Cr; (f) 20%Cr; (g) 15%Cr; (h) 10%Cr; (i) 3D diagram; (j) enlarged 3D diagram for the ternary Matrix + $M_7C_3$ + $M_{23}C_6$ region. In figures (a)-(h), the regions in which $M_7C_3$, $M_{23}C_6$ and Matrix co-exist are highlighted in yellow. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/813011534031618049_2.jpg)

![](./images/813011534031618049_3.jpg)

![](./images/813011534031618049_4.jpg)

![](./images/813011534031618049_5.jpg)

![](./images/813011534031618049_6.jpg)

![](./images/813011534031618049_7.jpg)

**Fig. 1. (continued)**

### 2. Equilibrium phase diagrams

A serial of isopleth sections with the chromium contents varying from 10 wt% to 45 wt% and corresponding 3D diagrams for the ternary Fe-Cr-C system in both stable and metastable states were calculated and are illustrated in Figs. 1 and 2. These diagrams depict three-phase regions consisting of the matrix (Austenite/Martensite), $M_7C_3$ and $M_{23}C_6$ (marked in yellow) carbides. In these three-phase regions, alloys have the compositions suitable for the formation of the core-shell structured carbides. This is the compositional prerequisite for fabricating HCCIs containing core-shell structured carbides based on phase-equilibria thermodynamics. Figs. 1(a)-1(h) clearly manifest that the three-phase region shifts towards the high-C side as the Cr-content increases. More intuitively, as shown in the 3D diagrams (Figs. 1(i) and 1(j)), when the Cr content is fixed, the carbon amount is tolerant between $\%(C)_{\text{max}} = 0.1$ wt (Cr)% and $\text{wt}\%(C)_{\text{min}} = 0.06$ wt (Cr)% within the three-phase regions.

All HCCIs which may have core-shell structured carbides comply with these relationships except the three alloys having their respective compositions at Fe-10 wt%Cr-5 wt%C [25], Fe-25 wt%Cr-0.8 wt%C [16] and Fe-29 wt%Cr-0.3 wt%C [27], which are beyond the defined

![](./images/813011534031618049_8.jpg)

**Fig. 1. (continued)**

![](./images/813011534031618049_9.jpg)

![](./images/813011534031618049_10.jpg)

![](./images/813011534031618049_11.jpg)

Fig. 2. The calculated metastable phase diagrams for HCCIs given suppressing the cementite and graphite in (a) 10%Cr; (b) 15%Cr; (c) 3D diagram; (d) enlarged 3D diagram for the ternary Matrix + M₇C₃ + M₂₃C₆ region. In figures (a) and (b), the regions in which M₇C₃, M₂₃C₆ and Matrix co-exist are highlighted in yellow. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/813011534031618049_12.jpg)

Fig. 3. Core-shell structured carbides in HCCIs (see Ref. [25]).

equilibria zones, as observed in previous experiments. The first alloy has a low content of Cr while the other two alloys are short of carbon. For the first alloy, a SEM image of microstructure (Fig. 3) presented in reference [25] illustrates distinguishable core-shell structured carbides. In view of the composition and related stable phase assemblage as Fig. 1(h) shows, the above-mentioned exceptional case is in the phase region containing cementite or graphite, and does not satisfy the phase requirements to form the core-shell structure. However, when the two phases of cementite and graphite were suppressed to calculate the metastable phase diagram (Fig. 2), the three-phase zone of Matrix + M₇C₃ + M₂₃C₆ would appear in another branch located in the high-C and low-Cr region. The two triangular prisms in Figs. 2(c) and 2(d) can distinctly represent the three-phase zones in different composition regions. This indicates that the required phase constituents for the core-shell morphology can be reached in the alloy of Fe-10 wt%Cr-5 wt%C, given that the precipitation of cementite and graphite is inhibited during the practical fabrication. This inhibition can be realized by adding trace alloying elements such as Si [28], Al [29] and Cu, Mn, Ni and Mo [30,31] or using larger cooling rate for fine precipitation. The former may vary the carbide/matrix interfacial energy for certain carbides, leading to the variation in the precipitation sequence. While the latter affects the driving force for carbide nucleation. Details about suppressing the formation of cementite are not included in this paper, since they are complex and need more analysis for clarification, which will be investigated in the follow-up studies. For the other two alloys with higher wt%Cr, core-shell structured carbides were also experimentally observed [16,27], but the mechanism for their core-shell structured carbide formation is different from that for the first alloy. When the alloy contains sufficient Cr while less C, Matrix and M₂₃C₆ are the stable phases within a wide temperature range. Matrix-M₇C₃(core)-M₂₃C₆(shell) configuration could be temporally formed after annealing the castings. Due to limited amount of M₇C₃ formed during solidification, the Matrix + M₇C₃ M₂₃C₆ reaction will continue to consume all M₇C₃ leading to disappearance of the core. It should be noted here that all these exceptional alloys having core-shell structured configuration are not suitable for industrial applications due to their metastable characteristics.

However, fabricating alloys with reference to the phase diagrams does not guarantee that the core-shell structure can be generated in the three-phase region. This uncertainty is ascribed to the following two key facts: (1) phases displayed in the equilibrium diagrams are those ideally created under the thermodynamic limits without consideration of kinetic factors; (2) the carbide M₂₃C₆ may be precipitated in the

matrix to form the secondary carbide rather than that formed at the eutectic $M_7C_3$/Matrix interface to yield the shell configuration. The required conditions where $M_{23}C_6$ could be formed in different locations of as-cast irons have been discussed in detail in the following sections.

The equilibrium diagrams also help select appropriate heat-treat- ment temperatures for as-cast alloys with specific compositions. The typical heat-treatment process for HCCIs may involve destabilization, sometimes austenitizing, and quenching [32]. One may see in Fig. 1j that there exists phase transition from ferrite to austenite at about 815 °C. When the heat treatment is performed for austenitizing, the temperature should be set above the transition temperature, and quenching for martensitizing. This could be the fine tuning for HCCIs before practical applications.

### 3. Solidification-path analysis

One of the main objectives of this study is to understand the for- mation of the core-shell structured carbides during microstructural evolution in HCCIs. Microstructural characteristics of cast irons such as carbide's shape and distribution as well as the ferrous matrix micro- structure are dependent on the chemical composition, casting process, e.g. cooling condition, and post heat treatments [33,34]. In the afore- mentioned section, the effect of overall chemical composition on mi- crostructure is discussed with regard to how the alloy is driven into the three-phase region of Matrix $+M_{7}C_{3}+M_{23}C_{6}$, which is a prerequisite in phase constituent for the formation of core-shell structured carbides. In this section, the impact of cooling condition on the solidification behavior is analyzed and evaluated through comparative simulations using the Scheil-Gulliver and Lever-Rule methods. These simulations provide useful information on the microstructure evolution during cooling and post heat-treatments. In Section 4, the emphasis of study is put on variations in microstructure with specific compositions during the heat-treatment process in order to understand the mechanism for the formation of the core-shell configuration in HCCIs.

As above-mentioned, two kinds of solidification simulations, namely Scheil-Gulliver and Lever-Rule, are employed to analyze possible crys- tallization routes and microstructure evolution in the nine alloys with their nominal compositions listed in Table 1. It is noticeable that each composition is located in the three-phase region of Ma- trix $+M_{7}C_{3}+M_{23}C_{6}$. As a matter of fact, the true solidification process proceeds between the two paths but is closer to the one described by the Scheil-Gulliver model.

For Scheil-Gulliver cooling, it is assumed that (1) no diffusion occurs in solid phases once they are formed, (2) the liquid phase remains homogenous with infinitely fast diffusion, and (3) the liquid/solid in- terface keeps in local equilibrium. Such solidification seems to be close to the practical casting process with high cooling rates. With regard to the Lever-Rule cooling, assumptions include (1) solidification of an alloy from its liquid state is in complete thermodynamic equilibrium or metastable equilibrium, (2) all solid phases remain homogeneous through internal diffusion, and (3) all peritectic reactions proceed to completion. Such condition is achievable only when the cooling rate is extremely slow, which is thus beyond the practical situation, but can have the solidification behavior considered under the global or local equilibrium limits.

The solidification paths under the Scheil-Gulliver and Lever-Rule cooling conditions were simulated and then imposed on the corre- sponding liquidus projections, as shown in Figs. 4(a) and 4(b), re- spectively. Results of simulations under the condition of suppressing the graphite and cementite are also illustrated in Fig. 5. Table 1 provides detailed information on solidification microstructures of individual al- loys obtained from the two kinds of simulations during each cooling period. The precipitated microstructure that attracts the most attention is the eutectic Matrix (Fcc/Bcc) $+M_{7}C_{3}$ colony, since the $M_{23}C_{6}$ carbide, once nucleates and grows at the Matrix $+M_{7}C_{3}$ interface, can probably form the shell configuration [10,11]. Or in other words, without the eutectic Matrix $+M_{7}C_{3}$ colony, the $M_{23}C_{6}$ shell configuration is almost impossible to form. Figs. 4 and 5 and Table 1 show that the Scheil- Gulliver solidification provides all as-cast alloys with the eutectic colony, while under the Lever-Rule solidification condition the alloy Fe-10Cr-0.75C does not have the eutectic matrix but the austenite (FCC) one. The figures and table also show that the molten alloys with the Cr level above 30 wt% terminate their solidification at the eutectic point (E1) no matter what the cooling condition is. Usually, the eutectic precipitation has the largest volume over the entire solidification pro- cess under the Scheil-Gulliver condition. It can be unscrambled that all selected alloys except Fe-10Cr-0.75C under the lever-rule solidification condition have the potential to form the $M_{23}C_{6}$ shell at the interface between the eutectic Matrix and Primary $M_{7}C_{3}$ no matter what is the cooling condition. However, whether the predicted shell formation could be achieved during the post heat treatment is critically dependent on the composition of the eutectic matrix at the interface with $M_{7}C_{3}$, which should provide sufficiently large driving force for $M_{23}C_{6}$ nu- cleation at the interface. This issue has been analyzed in detail and illustrated in the following section.

### 4. Heat treatments for driving the core-shell structure development

The as-cast microstructures of HCCIs consist of primary austenite dendrites (FCC) and eutectic austenite (partially transformed to mar- tensite) with interdendritic eutectic $M_{7}C_{3}$ carbide, as shown in Figs. 3 and 4 and Table 1. In general, thermal treatments are exerted on the as- cast irons to modify the microstructure for improved service perfor- mance with, e.g., higher fracture toughness and crack propagation re- sistance [2,35-38]. The treatments may also assist castings to grow the secondary carbides in the matrix and shell carbide at the primary car- bides-matrix interface, respectively. These heat treatments are con- ventionally held at 950-1050 °C, followed by air cooling and tem- pering. The holding period is called "destabilization" since it drives carbon and chromium in the austenite matrix out of the solution, forming the precipitates of carbides [9].

Studies on the formation of secondary carbides [14,39-44] de- monstrate that the secondary carbides never nucleate and grow on the eutectic carbides but form separately within the original dendritic re- gions [39-41]. The secondary carbides in cast irons containing 15-20%Cr have been identified as $M_{7}C_{3}$ and as $M_{23}C_{6}$ in those with 25-30%Cr [3,41-43], respectively. Destabilization treatments do not show significant influence on the configuration of the eutectic carbides in HCCIs with the overall Cr content below 28 wt%. However, when the Cr content is above 30 wt%, the destabilization treatment affects the eutectic $M_{7}C_{3}$ carbide, causing its partial transformation to $M_{23}C_{6}$ and thus yielding the $M_{23}C_{6}$ shell encompassing the $M_{7}C_{3}$ core. Although the previous experiments showed that the formation of the secondary carbides and the core-shell configuration largely depended on the overall Cr level in HCCIs, it is unclear how the different Cr levels play distinct roles in generating carbides having different configurations and shapes. Clarification of the mechanisms for the above-mentioned puzzle is of significance to fundamental understanding and development of guidelines for controlling the core-shell structured carbide growth.

Thermodynamic calculations were conducted in this work to ana- lyze the nucleation driving force of the $M_{23}C_{6}$ shell and secondary carbides in order to investigate the probability of precipitating each type of carbide according to the classical nucleation theory [45]. In order to simplify the computations, several assumptions are made as follows: (1) the temperature of simulated heat treatments is 1000 °C; (2) the composition of the eutectic matrix is nonuniform and roughly di- vided into the inner one and the interfacial one; (3) the inner compo- sition is momentarily kept as that precipitated from the solidification; (4) the eutectic matrix and carbide immediately match the Metastable Local Equilibrium (MLE) at the interface and the interfacial composi- tion is thus equilibrated by the eutectic carbide $(M_{7}C_{3})$ during the

<table><caption>Table 1 Calculated steps during Scheil-Gulliver and Lever-Rule cooling from the liquid state to final disappearance of the liquid at several compositions.</caption>
<thead>
<tr>
<th>Initial composition</th>
<th>Scheil-Gulliver cooling</th>
<th>Lever-Rule cooling</th>
</tr>
</thead>
<tbody>
<tr>
<td>45Cr-4.0C</td>
<td>Liquid cooling (2000–1393 °C)
Liquid → M₇C₃ (1393–1319.7 °C)
Liquid → M₂₃C₆ (1319.7–1297.9 °C)
Liquid → Bcc + M₂₃C₆ (1297.9–1289.1 °C)
Liquid → Bcc + M₇C₃ (1289.1–1283.8 °C)
Liquid → Fcc + Bcc + M₇C₃ (1283.8 °C)</td>
<td>Liquid cooling (2000–1393 °C)
Liquid → M₇C₃ (1393–1319.4 °C)
Liquid → M₂₃C₆ + M₇C₃ (1319.4–1289.1 °C)
Liquid + M₂₃C₆ → Bcc + M₇C₃ (1289.1 °C)</td>
</tr>
<tr>
<td>40Cr-3.5C</td>
<td>Liquid cooling (2000–1352 °C)
Liquid → M₇C₃ (1352–1300 °C)
Liquid → M₂₃C₆ (1300–1292.2 °C)
Liquid → M₂₃C₆ + Bcc(1292.2–1289.1 °C)
Liquid → M₇C₃ + Bcc(1289.1–1283.8 °C)
Liquid → M₇C₃ + Bcc + Fcc (1283.8 °C)</td>
<td>Liquid cooling (2000–1352 °C)
Liquid → M₇C₃ (1352–1300 °C)
Liquid → M₇C₃ + M₂₃C₆ (1300–1289.1 °C)
Liquid → M₇C₃ + Bcc (1289.1–1286.9 °C)</td>
</tr>
<tr>
<td>35Cr-3.0C</td>
<td>Liquid cooling (2000–1312 °C)
Liquid → M₇C₃ (1312–1287.2 °C)
Liquid → M₇C₃ + Bcc (1287.2–1283.8 °C)
Liquid → M₇C₃ + Bcc + Fcc (1283.8 °C)</td>
<td>Liquid cooling (2000–1312 °C)
Liquid → M₇C₃ (1312–1287.2 °C)
Liquid → M₇C₃ + Bcc (1287.2–1283.8 °C)
Liquid → M₇C₃ + Bcc + Fcc (1283.8 °C)</td>
</tr>
<tr>
<td>30Cr-2.3C</td>
<td>Liquid cooling (2000–1318.6 °C)
Liquid → Bcc (1300.2–1284.0 °C)
Liquid → Bcc + M₇C₃ (1284.0–1283.8 °C)
Liquid → Fcc + Bcc + M₇C₃ (1283.8 °C)</td>
<td>Liquid cooling (2000–1318.6 °C)
Liquid → Bcc (1318.6–1284.1 °C)
Liquid → Bcc + M₇C₃ (1284.1–1283.8 °C)
Liquid → Fcc + M₇C₃ (1283.8 °C)</td>
</tr>
<tr>
<td>25Cr-2.0C</td>
<td>Liquid cooling (2000–1342.3 °C)
Liquid → Bcc (1342.3–1342 °C)
Liquid → Fcc (1342–1285.4 °C)
Liquid → Fcc + M₇C₃ (1285.4–1283.8 °C)
Liquid → Fcc + M₇C₃ + Bcc (1283.8 °C)</td>
<td>Liquid cooling (2000–1342.3 °C)
Liquid → Bcc (1342.3–1342 °C)
Liquid → Fcc + Bcc(1342–1341.8 °C)
Liquid → Fcc (1341.8–1285.4 °C)
Liquid → Fcc + M₇C₃ (1285.4–1284.9 °C)</td>
</tr>
<tr>
<td>20Cr-1.5C</td>
<td>Liquid cooling (2000–1383.8 °C)
Liquid → Bcc (1383.8–1381.6)
Liquid → Fcc (1381.6–1286.2 °C)
Liquid → Fcc + M₇C₃ (1286.2–1284.8 °C)</td>
<td>Liquid cooling (2000–1383.8 °C)
Liquid → Bcc (1383.8–1381.6 °C)
Liquid → Fcc + Bcc (1381.6–1380.2 °C)
Liquid → Fcc (1380.2–1286.2 °C)
Liquid → Fcc + M₇C₃ (1286.2–1286.1 °C)</td>
</tr>
<tr>
<td>15Cr-1C</td>
<td>Liquid cooling (2000–1429.8 °C)
Liquid → Bcc (1429.8–1417.3 °C)
Liquid → Fcc (1429.8–1285.3 °C)
Liquid → Fcc + M₇C₃ (1285.3–1265.2 °C)</td>
<td>Liquid cooling (2000–1429.8 °C)
Liquid → Bcc (1429.8–1417.3 °C)
Liquid → Bcc + Fcc (1417.3–1411.9 °C)
Liquid → Fcc (1411.9–1285.6 °C)
Liquid → Fcc + M₇C₃ (1285.6 °C)</td>
</tr>
<tr>
<td>10Cr-0.75C</td>
<td>Liquid cooling (2000–1480.1 °C)
Liquid → Bcc (1480.1–1449.1 °C)
Liquid → Fcc (1449.1–1277.1 °C)
Liquid → Fcc + M₇C₃ (1277.1–1185.0 °C)</td>
<td>Liquid cooling (2000–1480.1 °C)
Liquid → Bcc (1480.1–1449.3 °C)
Liquid → Fcc + Bcc (1449.3–1441.1 °C)
Liquid → Fcc (1441.1–1416.7 °C)</td>
</tr>
<tr>
<td>10Cr-5C</td>
<td>Liquid cooling (2000–1242.4 °C)
Liquid → M₇C₃ (1242.4–1170.3 °C)
Liquid → Fcc + M₇C₃ (1170.3–1114.7 °C)
Liquid → Fcc + M₂₃C₆ (1114.7–1098.2 °C)</td>
<td>Liquid cooling (2000–1242.4 °C)
Liquid → M₇C₃ (1242.4–1172.2 °C)
Liquid → Fcc + M₇C₃ (1172.2–1135.7 °C)</td>
</tr>
</tbody>
</table>

isothermal heat treatment, as illustrated in Fig. 6; (5) the matrix is purely austenite after the austenitizing treatment. The MLE refers to the state which occurs only at the phase interface, where a new phase may be precipitated during prolonged heat treatments. The matrix composition in a dichotomy (inner and interface) has possible influences on various configurations of carbides, as schematically illustrated in Fig. 7. The compositional gradient from the inner to interface matrix controls the precipitation of carbides in distinct configurations and shapes. The interfacial composition determines the M₂₃C₆ shell formation, while the inner composition dominates the precipitation of the secondary carbides. The dichotomy assumption is reasonably made with regard to the tough diffusion kinetics of elements in the matrix, temporally resulting in compositional variations from inner to interface. Correspondingly, it usually takes a long period to achieve the compositional homogeneity in view of the slow mobility of atoms and their long-range interdiffusion in the matrix lattice during thermal treatments. Although carbon diffuses much faster than Fe and Cr and may rapidly reach uniform over the entire matrix during the thermal treatment, it has negligible influence on the present calculation using the dichotomy compositions since there is no abrupt change (less than 0.2%) of the C level between the inner and the interface matrix, as shown in Fig. 6.

The driving force for nucleation is portrayed by the two-dimensional Gibbs energy curves (Fig. 8) instead of a complex three-dimensional Gibbs energy surfaces for simplicity. The common tangent line in Fig. 8 is accordingly in lieu of the actual common tangent plane. These can be imagined as a vertical plane (a fixed ratio of Fe to Cr in this plane) intersecting the 3D energy surface and the common tangent plane to form. In a ternary system, there must be one and only one common plane tangent to the three Gibbs energy surfaces but more to those for the two phases. Therefore, at the fixed composition and temperature, the common tangent plane for M₇C₃, M₂₃C₆ and Matrix are mostly different from that for the MLE M₇C₃ and Matrix, leading to the nonzero driving force of M₂₃C₆ nucleated from the interface between M₇C₃ and Matrix. Owing to the verifying ratios of Fe to Cr in the two carbides, the largest driving force for nucleating M₂₃C₆ is adopted and calculated using the parallel tangent method [26] with the tangent plane determined by the chemical potentials of Fe, Cr and C in the MLE Matrix and M₇C₃. The initial composition of the M₂₃C₆ embryo is thus determined using the parallel tangent plane to intersect the energy curve of M₂₃C₆. According to Fig. 8, the nucleation driving force of M₂₃C₆ at the two-phase interface can also be defined by the equilibrium composition of Matrix since the contact fronts between M₇C₃ and Matrix are in MLE as mentioned by the above-fourth assumption. Based on this inference, we could merge the driving forces of carbides

![](./images/813011534031618049_13.jpg)

Fig. 4. Calculated liquidus projection of the Fe-Cr-C system with the solidification paths during: (a) Scheil-Gulliver cooling; (b) Lever-Rule cooling for the 8 alloys compositions.

precipitated from various matrix domains in a contour diagram by only tracking the domain compositions.

The contour diagram is very useful for illustration of how a property changes with respect to more than one variable, such as energy and liquidus surfaces in ternary systems, which is actually the projection of a three-dimensional surface into a two-dimensional plane. This method has been implemented by Chen [23] in the Pandat software. Fig. 9 illustrates the calculated driving forces for $M_7C_3$ and $M_{23}C_6$ to nucleate from austenite (based on the fifth assumption), which helps investigate the mechanism for the formation of secondary carbides inside the eutectic matrix. The inner compositions of all the eutectic matrices in the nine castings were calculated using both the Scheil-Gulliver and Lever-Rule simulations, which are superimposed on the contour diagram. One may see from Fig. 9 that the driving forces for the nucleation of the secondary carbides, $M_7C_3$ and $M_{23}C_6$, from the inner matrix in the Fe-15Cr-1C casting are respectively 3000-3500 J/mol and 1500-2400 J/mol; and in the Fe-20Cr-1.5C they are 3500-3600 J/mol and 2500-2800 J/mol, respectively. The results indicate that the nucleation rate of $M_7C_3$ is much higher than that of $M_{23}C_6$ in the inner matrix. The situation is similar for castings having their Cr content less than 25 wt %. However, at the Cr level of 30 wt%, $M_7C_3$ and $M_{23}C_6$ have their nucleation driving forces around 1500-1600 J/mol and 2000-2100 J/mol, respectively, implying that $M_{23}C_6$ is more facile than $M_7C_3$ to be precipitated in the inner matrix. The same situation is also for the castings with their Cr level above 30 wt%. The calculated results agree well with experimental observations on the formation of secondary carbides [3,41-43].

Regarding the formation of the core-shell structured carbides, the carbide $M_{23}C_6$ should be precipitated at the $M_7C_3$-matrix interface. It is thus of primary interest to determine the driving force contour for nucleation of $M_{23}C_6$ from $M_7C_3$ and Matrix. As already elucidated above, the nucleation driving force of $M_{23}C_6$ at the $M_7C_3$-matrix interface can be calculated using the interfacial composition of Matrix (Fig. 8) instead of the overall composition of the eutectic colony. This would help make direct comparison between Figs. 9 and 10 to see the difference between $M_{23}C_6$ nucleation from the inner matrix and that at

![](./images/813011534031618049_14.jpg)

Fig. 5. Calculated liquidus projection of the Fe-Cr-C system with the solidification paths during: (a) Scheil-Gulliver cooling; (b) Lever-Rule cooling for the Fe-10Cr-5C alloy under the condition of suppressing graphite and cementite.

![](./images/813011534031618049_15.jpg)

Fig. 6. Calculated elements' partitions in the eutectic matrix subjected to heat treatments.

IC: Interface Composition
ic: inner composition

![](./images/813011534031618049_16.jpg)

Fig. 7. The schematic diagram for the formation of the core-shell structured carbides: (a) the as cast single-phase M₇C₃ carbide; (b) formation of core-shell structured carbide by thermal treatment.

![](./images/813011534031618049_17.jpg)

Fig. 8. The schematic diagram on the driving force for nucleating $M_{23}C_{6}$ from the Matrix and $M_{7}C_{3}$ interface.

![](./images/813011534031618049_18.jpg)

Fig. 9. Calculated nucleation driving force of $M_{23}C_{6}$ and $M_{7}C_{3}$ from the inner matrix composition.

![](./images/813011534031618049_19.jpg)

Fig. 10. Calculated nucleation driving force of $M_{23}C_{6}$ from the interface matrix composition.

the matrix interface. The interfacial compositions of all eutectic matrices in the nine castings can be obtained by initially tracking the overall compositions of the eutectic colonies during the solidification process and then using them to calculate the equilibrium compositions of the eutectic matrices at the isothermal heat treatment (1000 °C in the present case). All interfacial compositions of Matrices are later superimposed on the contour diagram (the same red¹ lines as presented in Fig. 9) as Fig. 10 shows. According to Figs. 9 and 10, the carbide $M_{23}C_{6}$ prefers to nucleate from the inner matrix, since the nucleation driving force is much larger than that for nucleation at the interface. Fig. 10 also shows that at the Cr level larger than 30 wt%, the driving force of $M_{23}C_{6}$ nucleating from the interface reaches more than 300 J/mol, which is perhaps the benchmark value to counteract the energy barrier to precipitation at the interface. The results of the calculations are consistent with experimentally observed formation of core-shell structured carbides [7-11]. Fe-10Cr-5C casting is an exception, in which the core-shell structured carbides were observed [25], since the driving force of $M_{23}C_{6}$ nucleation at the interface is below 100 J/mol which is not sufficiently larger for $M_{23}C_{6}$ nucleation at the interface. However, as discussed in Section 2, the three-phase region can occur if the cementite and graphite are suppressed by adding alloying elements or introducing extremely rapid and fine precipitation during solidification processes. The addition of alloying elements may increase the cementite-matrix interfacial energy, and meanwhile reduce that of $M_{23}C_{6}$-matrix interface, thus promoting the nucleation of $M_{23}C_{6}$ in both the inner matrix and the interfacial zone. The latter finally evolve in the core-shell structured carbide. It should be noted that the precipitation compositions imposed in Figs. 9 and 10 are only tracked from the Scheil-Gulliver solidification but they indeed cover those from the Lever-Rule cooling process. This does not affect the analysis of the calculation results but could avoid the data overlap in the two figures. With the above-presented figures, tables and discussions, the mechanisms for the formation of the core-shell structured and secondary

![](./images/813011534031618049_20.jpg)

Fig. 11. Calculated driving force for nucleating $M_{23}C_{6}$ at the $M_{7}C_{3}$ and Matrix interface on the as-cast eutectic colony.

![](./images/813011534031618049_21.jpg)

Fig. 12. The effect of the Matrix microstructure and temperature on the driving force of $M_{23}C_{6}$ precipitated from the $M_{7}C_{3}$ and Matrix interface on the as-cast eutectic colony.

¹ For interpretation of color in Fig. 9, the reader is referred to the web version

(footnote continued)
of this article.

carbides are reasonably explained based on relevant dependence on the non-uniform composition of the eutectic matrix that determines the driving force of carbide nucleation in different zones.

From the point view of fabrication, it is of significance to investigate the effects of temperature and overall composition on the nucleation driving force of forming the $M_{23}C_6$ shell configuration. Fig. 11 shows that point A possesses the largest nucleation driving force within the upper three-phase region, while point A' is in a similar situation within the lower one. When the overall carbon content is fixed, the driving force is increased with increasing the overall Cr level within the upper zone (Fig. 11) and the situation is reversed within the lower zone. When the overall Cr content is fixed, the driving force is reduced with increasing the overall carbon content in the upper zone, while the situation becomes opposite in the lower zone. From Fig. 12 one may draw the following conclusions: the lower the temperature of heat treatments, the larger is the driving force of the $M_{23}C_6$ shell; keeping the matrix in the austenite state would help enlarge the driving force of the $M_{23}C_6$ shell. However, it is worthwhile to note that the heat-treatment temperature should not be too much lower in order to immediately reach MLE at the matrix-carbide $(M_7C_3)$ interface by avoiding extremely sluggish reaction kinetics.

## 5. Conclusions

The compositional range and relevant mechanism for the formation of core $(M_7C_3)$-shell $(M_{23}C_6)$ structured carbides in HCCIs were investigated through thermo-kinetic analysis. The thermodynamic database and Calphad method were used to calculate a serial of equilibrium diagrams with the isopleth Cr concentration ranging from 10 wt% to 45 wt% to ascertain the stable region of $M_7C_3 + M_{23}C_6 +$ Matrix. The as-cast microstructures formed under both the Scheil-Gulliver and Lever-Rule cooling conditions were analyzed to determine the prerequisite microstructure of the eutectic colony $(M_7C_3$ and Matrix) for the formation of the core-shell configuration. The nucleation driving force for the carbide formation, influenced by the matrix composition during solidifications was also investigated, and the contour diagrams of the nucleation driving force were obtained for different configurations and types of carbides within the eutectic matrix. The dichotomy compositions for the inner matrix and matrix interface were designed to treat the non-uniform composition within the matrix, in which the former kept unchanged as it precipitated while the latter matched the instantaneous MLE (metastable local equilibrium) with the eutectic carbide $(M_7C_3)$ during heat treatments. All results of the calculations demonstrate that the non-uniform composition within the eutectic matrix governs the nucleation and precipitation of various types and configurations of carbides. The driving force of 300 J/mol is determined as the benchmark to counteract the energy barrier to the nucleation of $M_{23}C_6$ at the eutectic interface between the matrix and $M_7C_3$, leading to the final formation of the core-shell structured carbide. The effects of parent microstructure, temperature, and overall composition on the nucleation driving force are fully discussed in order to help optimize the external conditions to fabricate HCCIs with the desired core-shell structured carbides.

## Acknowledgments

The authors are grateful for funding support from the Natural Science and Engineering Research Council of Canada, Camber Technology Corporation, Suncor Energy, Shell Canada Ltd., Magna International Inc. and Volant Products Inc. The authors would also like to thank Dr. Shuanglin Chen for helpful discussions in this work and Computherm LLC for the permitted usage of the Pandat thermodynamic software.

## References

[1] R.W. Durman, Progress in abrasion-resistant materials for use in comminution processes, Int. J. Miner. Process. 22 (1988) 381-399.

[2] J.T.H. Pearce, Abrasive wear behavior of alloy cast irons, Br. Foundryman 78 (1985) 13-23.

[3] J.T.H. Pearce, High chromium cast irons to resist abrasive wear, Foundryman 95 (2002) 156-166.

[4] Ö. Doğan, J. Hawk, G. LairdII, Solidification structure and abrasion resistance of high chromium white irons, Metall. Mater. Trans. A. 28 (1997) 1315-1328.

[5] C.-M. Chang, Y.-C. Chen, W. Wu, Microstructural and abrasive characteristics of high carbon Fe-Cr-C hardfacing alloy, Tribol. Int. 43 (2010) 929-934.

[6] C.-M. Lin, C.-M. Chang, J.-H. Chen, W. Wu, Hardness, toughness and cracking systems of primary $(Cr, Fe)_{23}C_6$ and $(Cr, Fe)_7C_3$ carbides in high-carbon Cr-based alloys by indentation, Mater. Sci. Eng. A. 527 (2010) 5038-5043.

[7] X.H. Tang, Lei Li, B. Hinckley, K. Dolman, D.Y. Li, L. Parent, Beneficial effects of the core-shell structure of primary carbides in high-Cr (45 wt%) white cast irons on their mechanical behavior and wear resistance, Tribol. Lett. 58 (44) (2015) 1-10.

[8] X.H. Tang, R. Chung, C.J. Pang, D.Y. Li, B. Hinckley, K. Dolman, Microstructure of high (45 wt.%) chromium cast irons and their resistances to wear and corrosion, Wear 271 (2011) 1426-1431.

[9] A. Wiengmoon, T. Chairuangsri, J.T.H. Pearce, A microstructural study of destabilized 30wt%Cr-2.3wt%C high chromium cast iron, ISIJ. Int. 44 (2004) 396-403.

[10] A. Wiengmoon, T. Chairuangsri, A. Brown, R. Brydson, D.V. Edmonds, J.T.H. Pearce, Microstructural and crystallographical study of carbides in 30wt.%Cr cast irons, Acta. Mater. 53 (2005) 4143-4154.

[11] J. Pearce, D.W. Elwell, Duplex nature of eutectic carbides in heat-treated 30% chromium cast iron, J. Mater. Sci. Lett. 5 (1986) 1063-1064.

[12] D. Kopyciński, E. Guzik, D. Siekaniec, A. Szczęsny, Analysis of the high chromium cast iron microstructure after the heat treatment, Arch. Found. Eng. 14 (2014) 43-46.

[13] J. Cui, H. Guo, J.W. Li, D.Y. Li, L. Parent, H. Tian, A computational study on the benefit of core-shell structured carbides to the erosion resistance of high-Cr cast irons, Tribol. Int. 103 (2016) 432-439.

[14] A. Inoue, T. Masumoto, Carbide reactions $(M_3C \rightarrow M_7C_3 \rightarrow M_{23}C_6 \rightarrow M_6C)$ during tempering of rapidly solidified high carbon chromium-tungsten and chromium-molybdenum steels, Metall. Trans. A. 11A (1980) 739-747.

[15] C.P. Tabrett, Microstructure-property Relationships in High Chromium White Irons, University of South Australia, 1997.

[16] K. Wieczerzak, P. Bala, R. Dziurka, T. Tokarski, G. Cios, T. Koziel, L. Gondek, The effect of temperature on the evolution of eutectic carbides and $M_7C_3$→$M_{23}C_6$ carbide reaction in the rapidly solidified Fe-Cr-C alloy, J. Alloy. Compd. 698 (2017) 673-684.

[17] Z.K. Liu, First-principles calculations and CALPHAD modeling of thermodynamics, Jpedav 30 (2009) 517-534.

[18] M. Hillert, The compound energy formalism, J. Alloys Compd. 320 (2001) 161-176.

[19] M. Hillert, L. Kjellqvist, H. Mao, M. Selleby, B. Sundman, Parameters in the compound energy formalism for ionic systems, Calphad. 33 (2009) 227-232.

[20] S.L. Chen, S. Daniel, F. Zhang, Y.A. Chang, X.Y. Yan, F.Y. Xie, R. Schmid-Fetzer, W.A. Oates, The PANDAT software packages and its applications, Calphad. 26 (2002) 175-188.

[21] S.L. Chen, F. Zhang, S. Daniel, F.Y. Xie, X.Y. Yan, Y.A. Chang, R. Schmid-Fetzer, W.A. Oates, Calculating phase diagrams using PANDAT and PanEngine, JOM 55 (2003) 48-51.

[22] W. Cao, S.L. Chen, F. Zhang, K. Wu, Y. Yang, Y.A. Chang, R. Schmid-Fetzer, W.A. Oates, PANDAT software with PanEngine, PanOptimizer and PanPrecipitation for multi-component phase diagram calculation and materials property simulation, Calphad 33 (2009) 328-342.

[23] S.L. Chen, W. Cao, C. Zhang, J. Zhu, F. Zhang, Q. Li, J. Zhang, Calculation of property contour diagrams, Calphad 55 (2016) 63-68.

[24] A.V. Khvan, B. Hallstedt, C. Broeckmann, A thermodynamic evaluation of the Fe-Cr-C system, Calphad 46 (2014) 24-33.

[25] J. Cui, L. Guo, H. Lu, D.Y. Li, Understanding effects of Cr content on the slurry erosion behavior of high-Cr cast irons through local property mapping and computational analysis, Wear 376-377 (2017) 587-594.

[26] M. vardavoulias, G. Papadimitriou, D. Pantelis, Effect of $M_7C_3$→$M_{23}C_6$ transformation on fracture behaviour of cast ferritic stainless steels, Mater. Sci. Technol. 9 (1993) 711-717.

[27] L. Li, H. Jiang, Application of thermodynamics in designing of advanced automotive steels, Adv. Manuf. 4 (2016) 340-347.

[28] D. Delagnes, F. Pettinari-Sturmel, M.H. Mathon, R. Danoix, F. Danoix, C. Bellot, P. Lamesle, A. Grellier, Cementite-free martensitic steels: a new route to develop high strength/high toughness grades by modifying the conventional precipitation sequence during tempering, Acta. Mater. 60 (2012) 5877-5888.

[29] B.T. Lu, J.L. Luo, S. Chiovelli, Corrosion and wear resistance of chrome white irons- A correlation to their composition and microstructure, Metall. Mater. Trans. A 37A (2006) 3029-3038.

[30] R.S. Jackson, Austenite liquidus surface and constitutional diagram for the iron-chromium-carbon metastable system, J. Iron Steel Inst. 208 (1970) 163-167.

[31] I.F. Pariente, F.J. Belzunce, C.R.Y.J. Riba, Mechanical strength and fracture toughness of high chromium white cast irons, Mater. Sci. Tech-Lond. 24 (2008) 981-985.

[32] R. Ghasemi, L. Elmquist, H. Svensson, M. König, A. Jarfors, Mechanical properties of solid solution-strengthened CGI, Int J. Cast. Metal. Res. 29 (2016) 97-104.

[33] L. Collini, G. Nicoletto, R. Konečná, Microstructure and mechanical properties of

pearlitic gray cast iron, Mater. Sci. Eng. A. 488 (2008) 529–539.

[34] M. Fiset, K. Peev, M. Radulovic, The influence of niobium on fracture toughness and abrasion resistance in high-chromium white cast irons, J. Mater. Sci. Lett. 12 (1993) 615–617.

[35] M. Radulovic, M. Fiset, K. Peev, The influence of vanadium on fracture toughness and abrasion resistance in high chromium white cast irons, J. Mater. Sci. 29 (1994) 5085–5094.

[36] C.P. Tabrett, Microstructure-property relationships in high chromium white iron alloys, Int. Mater. Rev. 41 (1996) 59–82.

[37] S.K. Hann, J.D. Gates, A transformation toughening white cast iron, J. Mater. Sci. 32 (1997) 1249–1259.

[38] G.L.F. Powell, G. Laird, Structure, nucleation, growth and morphology of secondary carbides in high chromium and Cr-Ni white cast irons, J. Mater. Sci. 27 (1992) 29–35.

[39] J.T.H. Pearce, D.W.J. Elwell, Proc. Best Practices in the Production, Processing and Thermal Treatment of Castings, Raffles City Convention Centre, Singapore, 1995, pp. 26-1.

[40] J.T.H. Pearce, in: B.K. Dhindaw, B.S. Murty, S. Sen (Eds.), Proc. of Solidification Science and Processing: Outlook for the 21st Century, Bangalore, India, Oxford & IBH Publishing, New Delhi, 2001, pp. 241.

[41] K.A. Kibble, J.T.H. Pearce, Influence of heat treatment on the microstructure and hardness of 19% high-chromium cast irons, Cast Met. 6 (1993) 9–15.

[42] K.A. Kibble, J.T.H. Pearce, An examination of the effects of annealing heat treat- ment on secondary carbide formation in 25% Cr high chromium irons, Cast Met. 8 (1995) 123–127.

[43] J.D.B. Demello, M.D. Charr, S.H. Thibault, Solidification and solid state transfor- mations during cooling of chromium-molybdenum white cast irons, Metall. Trans. A. 14A (1983) 1793–1801.

[44] P.M. Chaikin, T.C. Lubensky, Principles of Condensed Matter Physics, Cambridge University Press, Cambridge, 1995.

[45] J.W. Christian, Theory of Transformations in Metals and Alloys. Part 1, Pergamon Press, Oxford, 1975.