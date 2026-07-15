
# Predicting aqueous and electrochemical stability of 2D materials from extended Pourbaix analyses

S. Americo \( ^{1,*} \) , I. E. Castelli \( ^{2} \) , and K.S. Thygesen \( ^{1} \) 

 \( ^{1} \) CAMD, Department of Physics, Technical University of Denmark, DK - 2800 Kongens Lyngby, Denmark

 \( ^{2} \) Department of Energy Conversion and Storage, Technical University of Denmark, DK - 2800 Kongens Lyngby, Denmark
*Email: stefano.americo@scitec.cnr.it

## Abstract

A key challenge for computational discovery of electrocatalytic materials is the reliable prediction of thermodynamic stability in aqueous environment and under different electrochemical conditions. In this work, we first evaluate the electrochemical stability of more than 3000 two-dimensional (2D) materials using conventional Pourbaix diagrams (CPDs). Due to the complete neglect of thermodynamic barriers along the (often complex) reaction pathways, the vast majority of the materials are predicted to be unstable even though some are known to be stable in practice. We then introduce an analysis based on the surface Pourbaix diagram (SPD) including 'early intermediate states' that represent the first steps of the key surface passivation and dissolution reactions. The SPD framework is applied to the 2D materials  \( MoS_{2} \) , phosphorene, and the MXene  \( Ti_{2}C \) , all of which are predicted to be unstable by the CPD. For  \( MoS_{2} \) , our approach reproduces the experimental pH-U stability window as well as the experimental desulphurization potential. For phosphorene and  \( Ti_{2}C \) , the SPD approach is used to investigate the spontaneous degradation mechanism and the potential-dependent surface termination, respectively, again yielding good agreement with experiments. The SPD-based stability analysis emerges as a versatile and quantitative method for prediction of stability and investigation of surface structures in electrochemical environments.

Introduction First-principles calculations are increasingly used for in-silico discovery of new materials with optimised properties for applications within a variety of areas including (electro)catalysis, photovoltaics, thermoelectrics, batteries, and nanoelectronics [1–16]. A basic question that any such study must address, independent of the target application, is whether the predicted materials will be stable under the relevant operating conditions. The simplest and most widely used measure of thermodynamic stability is the energy above the convex hull  \( \Delta H_{hull} \) , expressing the likelihood of a material to decompose into competing solid phases in the same compositional space. Although suitable for preliminary stability assessments, this descriptor is insufficient whenever the material under investigation is meant to be employed in setups where it can exchange chemical species with the surrounding environment. Depending on the envisioned application of the material and the specific conditions under which it should operate, it will typically be necessary to consider different processes and effects beyond the solid-state reactions covered by the convex hull analysis. In most cases, degradation processes such as corrosion and dissolution due to interactions with air or moisture, will be of relevance. In this work we shall be particularly interested in conditions applying to electrochemical setups, where undesired charge-transfer reactions with an aqueous electrolyte aided by applied electrostatic potentials often threaten the long-term stability of electrode materials. As a special case, corresponding to zero applied potential, this covers the aqueous stability, i.e., the stability towards spontaneous charge transfer reactions in contact with moisture.

The electrochemical stability issue is of paramount importance for all nanoscale structures, in particular for two-dimensional (2D) materials  \( [17–20] \) . The class of 2D materials has been under intense scrutiny for about a decade. This is not only due to the unique physical properties exhibited by many of these materials but also because of their tunability, structural flexibility, and extreme surface-to-volume ratio which makes them natural candidates as battery electrodes or (electro)catalysts  \( [21–26] \) . 2D materials are atomically thin and thus cannot be kinetically stabilised by e.g., formation of surface oxide layers as happens for many bulk materials, without significantly altering their basic properties. Methods that go beyond the 'convex hull paradigm' and allow for systematic and realistic assessment of stability under different environmental conditions, are therefore of particular relevance for this class of materials.

Traditionally, the stability of materials in electrochemical systems is analysed by means of Pourbaix diagrams [27] introduced by Marcel Pourbaix in 1966 in his study of corrosion of metals. These potential-pH phase diagrams identify the thermodynamically stable phases of a material allowed to react with water and exchange electrons with a counter electrode. Conventional Pourbaix diagrams (CPD) as introduced by Pourbaix constitute a double-edged sword when it comes to material stability predic-
 

tions. On one hand, due to the negligible computational cost of the method it is possible to rapidly generate pH-potential diagrams for thousands of materials. This allows, for instance, to screen large databases for materials that are thermodynamically stable under selected operating conditions [28–30]. On the other hand, the inherent limitations of the method, of which the most important is the complete neglect of energy barriers and reaction kinetics, can lead to erroneous conclusions regarding material stability. As a general rule, the more intermediate reaction steps are involved in a given process, i.e., the more complex the reaction is, the less likely it is to occur in practice. This is because more complex reactions involve more basic kinetic and energetic barriers separating the reactants from the products. In such situations, the system may be trapped in a metastable configuration and the entire process prevented from occurring, even if thermodynamically favorable.

In this work, we begin by performing a CPD analysis of the aqueous and electrochemical stability of more than 3000 two-dimensional (2D) materials lying on the convex hull, i.e., predicted as thermodynamically stable in the absence of other chemical species. This analysis shows that only a small fraction of the materials - the vast majority of which are oxides - are predicted to maintain stability under electrochemical conditions relevant for the hydrogen evolution (HER) and oxygen evolution reactions (OER). Surprisingly, several 2D materials that are known to be environmentally stable in practice are found to be unstable by the CPD analysis. We hypothesize that this is due to the presence of significant energy barriers associated with elementary reaction intermediates occurring along the overall reaction path. To take such barriers into account we employ an extended surface Pourbaix diagram (SPD) framework based on a concept of 'early intermediates' including relevant vacancies and adsorption configurations. A detailed stability analysis for three selected 2D materials, namely  \( MoS_{2} \) , phosphorene, and  \( Ti_{2}C \) , shows that the SPD analysis is consistent with experimental data, highlighting the necessity to go beyond the CPD for making realistic assessments of aqueous and electrochemical stability of solids in general, and for 2D materials in particular.

We stress that the employed SPD-based analysis is completely general and can be used to analyze stability of solid surfaces in general. The methods used to calculate the conventional and surface Pourbaix diagrams are available in the Atomic Simulation Environment (ASE) package [31] and the calculated CPD of thermodynamically stable 2D materials are available in the C2DB database [32,33].

## Results and discussion

## Conventional Pourbaix analysis

In order to obtain a general picture of the electrochemical stability of 2D materials according to the conventional Pourbaix diagram formulation, we first extracted from the C2DB database a set of thermodynamically stable monolayers as defined by \(\Delta H_{\mathrm{hull}} < 50 \mathrm{meV/atom}\). The ASE Pourbaix diagram implementation was then employed on the resulting 3376 materials in order to evaluate \(\Delta G_{\mathrm{pbx}}\) (see Methods) at six relevant points corresponding to the hydrogen evolution reaction (HER) an oxygen evolution reaction (OER) under acidic, neutral and alkaline conditions, respectively. As seen in Fig. 1, under HER conditions, the \(\Delta G_{\mathrm{pbx}}\) distribution is located between 0 and 2 eV/atom. On the other hand, under OER conditions, the materials are significantly less stable and the \(G_{\mathrm{pbx}}\) distribution ranges up to 8 eV/atom. This is because at these high potentials, oxidized decomposition products are stabilized (see Eq. 2). Such products, in particular bulk metal oxides and solvated oxyanions, represent the most stable competing phases for most materials. The 2D oxides, which constitute 18% of the entire data set, are characterized by generally higher electrochemical stability compared to all other 2D materials especially under OER conditions. In particular, all the materials with \(\Delta G_{\mathrm{pbx}} < 0\) are found to be oxides. In contrast, under HER conditions, the associated negative potentials promote reduction processes, which can harm the stability of 2D oxides. Still, the oxides constitute a very large fraction of all the stable materials under HER conditions as seen in Table 1. A list of all the materials found as highly stable (\(\Delta G_{\mathrm{pbx}} \leq -50 \mathrm{meV/atom}\)) under at least one of the explored conditions is reported in the supplementary material, Table 1 and 2.

Overall, the number of predicted electrochemically stable 2D materials ( \( \Delta G_{pbx} < 0 \) ) is very low and never exceeds 2.1% of the total set of materials for any pH-voltage value. It is, however, interesting that several materials that are known to be electrochemically stable in practice, such as  \( MoS_{2} \)  [34],  \( NbS_{2} \)   \( [35] \) , graphene [36] and hexagonal BN [37], have  \( \Delta G_{pbx} > 0 \)  are thus predicted as unstable by the CPD analysis.

## Surface Pourbaix analysis

As mentioned in the introduction, the CPD analysis neglects energy barriers along the reaction pathway and focuses on the stability of the target material relative to the final decomposition products. For that reason it gives no information on the potential kinetic stability of the material. The inclusion of intermediate states is particularly relevant when evaluating the stability of materials containing two or more elements (other than O and H), which require to consider multiple decomposition products in order to obtain balanced chemical reactions. For instance, every considered reaction pathway of  \( MoS_{2} \)  has to include among the products both a Mo-containing species such as  \( MoO_{3} \)  and an S-containing species, e.g.

 \[ \mathrm{MoS_{2}+7H_{2}O\longrightarrow MoO_{3}+SO_{4}^{2-}+14H^{+}+12e^{-}} \quad (1) \] 

Complex processes like the one above, involving the exchange of several electrons and protons as well as significant structural rearrangements leading from the starting material ( \( MoS_{2} \) ) to its main decomposition products ( \( MoO_{3} \)  and  \( SO_{4}^{2-} \) ), can be broken down into a large number of intermediate reaction steps, as illustrated in Fig. 2a. By only considering the target material and its final
 
![](./images/1139167458217689096_1.jpg)

![](./images/1139167458217689096_2.jpg)

Figure 1: Distribution of the Pourbaix energy  \( \Delta G_{pbx} \)  calculated for 2902 2D materials with  \( E_{hull} < 50 \)  meV/atom in different conditions of pH and applied potentials vs. SHE relevant for the HER and OER processes. The dataset is split between oxides (darker color) and non-oxides (brighter color).

<table><tr><td>Conditions</td><td>U (V)</td><td>pH</td><td>% stable materials (of which oxides)</td></tr><tr><td>Acidic HER</td><td>0</td><td>0</td><td>2.1 (46.5)</td></tr><tr><td>Neutral HER</td><td>-0.41</td><td>7</td><td>1.8 (65.1)</td></tr><tr><td>Alkaline HER</td><td>-0.83</td><td>14</td><td>1.8 (78.7)</td></tr><tr><td>Acidic OER</td><td>1.23</td><td>0</td><td>1.3 (100.0)</td></tr><tr><td>Neutral OER</td><td>0.82</td><td>7</td><td>2.0 (100.0)</td></tr><tr><td>Alkaline OER</td><td>0.40</td><td>14</td><td>1.8 (100.0)</td></tr></table>

Table 1: Stable 2D materials in different conditions of pH and applied potential vs. SHE. The column “% stable materials” shows the global percentage of materials with  \( \Delta G_{pbx}=0 \)  over the total of 2902 selected materials, in each condition. Among the materials with  \( \Delta G_{pbx}=0 \) , the column “% stable oxides” shows, in percentage, how many are oxides. The numbers in parentheses show the percentage of stable oxides relative to the total number of oxides (604) in the same conditions.

decomposition products, the likely occurrence of reaction intermediates with unfavourable thermodynamics is neglected.

Given that electrochemical processes take place at the interface between the electrode material and the solution phase, the early stage of any reaction will involve the atoms at the surface (for a 2D material this could be all atoms of the material depending on its thickness). Considering the pristine surface/2D material as the initial, "non-degraded" configuration, all degradation processes are necessarily initiated by either the adsorption of species such as O, OH and H from the solution phase or by the dissolution of atoms in the first few atomic layers towards the solution phase leaving a surface vacancy [38]. We refer to such adsorption and vacancy configurations - illustrated in Fig. 2b - as "early intermediate states", and to the processes leading from the pristine surface to one of these configurations as "early degradation steps" (EDS). The Gibbs free energy change of the EDS is labeled as  \( \Delta G_{pbx}^{\dagger} \) . The EDS can be energetically costly, especially without the aid of large applied potentials and/or harsh pH conditions, leading to steep thermodynamic energy barriers that prevents the global degradation process to take place altogether. The energy diagram on the left in Fig. 2c illustrates a scenario where one or more EDSs are thermodynamically favourable, hence the target material is
 

(a)

![](./images/1139167458217689096_3.jpg)

Figure 2: a) Representative energy diagram of two different chemical reactions leading to the formation of product A and B. Product A is thermodynamically unstable with respect to the target material (black line), resulting in a negative  \( \Delta G_{pbx} \) . However, the early reaction intermediates are downhill in free energy. The reaction path leading to product B represents the opposite scenario. b) Representative energy distribution of early reaction intermediates considered in the surface Pourbaix diagram construction in the case where the target material (black line) is thermodynamically unstable ( \( \Delta G_{pbx} > 0 \) ). c) Analogous to b), this time in a scenario where the target material is stable ( \( \Delta G_{pbx} < 0 \) ).

labeled as unstable (positive  \( \Delta G_{pbx}^{\dagger} \) ). Conversely, if all the EDS are uphill in energy as in the case reported on the right, the material is considered as meta-stable (negative  \( \Delta G_{pbx}^{\dagger} \) ). Note that with this definition a meta-stable material could be globally stable (if  \( \Delta G_{pbx} < 0 \) ).

In order to include these early intermediates we construct surface Pourbaix diagrams (SPD) according to the procedure described in the Methods section. Our formulation also includes a correction scheme - described in detail in the supplemental material - to account for the surface excess or depletion of ions at the charged metal-solution interface. In the following, we apply the SPD framework to three selected 2D materials, namely  \( MoS_{2} \) , phosphorene and  \( Ti_{2}C \) . Comparisons with the CPD and experimental data highlight the great flexibility and quantitative accuracy of the SPD-based analysis for describing the behaviour of real electrochemical systems.

MoS₂ Molybdenum disulphide MoS₂ is one of the most extensively studied materials in the class of transition metal dichalcogenides (TMDs) due to its unique properties and potential applications in various fields, including electronics, optoelectronics, catalysis, and more [41–43]. A main reason for its success in several fields of application is its good stability under a wide range of experimental conditions. In particular, the use of MoS₂ as catalyst for the HER [44] and for water treatment [45] highlights the stability of the material in aqueous environments in a wide range of pH conditions and, at least, moderate potentials required for the HER.

Existing studies on  \( MoS_{2} \)  for supercapacitor applications [39,40] provide useful cyclic voltammetry (CV) profiles at pH 0 and applied potentials ranging between +0.5 V and -1.1 V against the saturated calomel electrode (SCE). No significant oxidation or reduction peaks are found within this potential window, confirming the material stability. As shown in Fig. 3a, the CPD generated herein for  \( MoS_{2} \)  predicts the material to be thermodynamically unstable across all pH conditions and potentials, in contradiction with the experimental observations. This is due to the low formation energies of molybdenum oxides such as  \( MoO_{3} \)  and  \( MoO_{2} \) , as well as sulfur oxyanions and molecular com-
 
![](./images/1139167458217689096_4.jpg)

![](./images/1139167458217689096_5.jpg)

![](./images/1139167458217689096_6.jpg)

![](./images/1139167458217689096_7.jpg)

Figure 3: a) Conventional Pourbaix diagram of  \( MoS_{2} \) , with SCE as the counter-electrode. The color map shows the Pourbaix energy per atom. b) Surface Pourbaix diagram of  \( MoS_{2} \)  with SCE as the counter-electrode. The color map shows the Pourbaix energy per unit formula. An inset covering the darkened region is shown at the top right in order to better highlight the phases associated with narrow stability domains. The dashed green line represents the HER equilibrium vs. SCE. The concentration of  \( SO_{4}^{2-} \)  ions has been set to the experimental bulk value of  \( 1.0\ mol\ l^{-1} \)  and then corrected for the surface excess (see supplemental material) in order to compare with the CV data in refs. 39 and 40. c) Surface pourbaix diagram obtained from a  \( MoS_{2} \)  surface with a Mo vacancy. The darkened region represents the new, reduced stability window of  \( MoS_{2} \)  due to the stabilization of S vacancies around the Mo defect. The dashed lines show the stability window of pristine  \( MoS_{2} \) , as in panel b. d) Slice at pH=0.3 of the SPD of  \( MoS_{2} \)  vs. RHE. The colored lines describe the energy profile of the dissolution EDS producing sulphur-containing species. The vertical dashed line at -0.84 V marks the predicted onset of the overall desulphurization process. The vertical line at -1.06 V marks the onset of  \( H_{2}S \)  evolution.

pounds such as  \( SO_{4}^{2-} \)  and  \( H_{2}S \) .

Note that all the  \( MoS_{2} \)  decomposition pathways defining the stability domains in Fig. 3a (such as the oxidation to  \( MoO_{3} \)  and parallel dissolution into  \( SO_{4}^{2-} \) ) imply complex transformations of the initial structure, and are poorly described by a single thermodynamic step. Shifting our focus to the EDSs instead, we generate the SPD shown in Fig. 3b. A large stability domain is now found, spanning both positive and negative potentials around the HER equilibrium potential (dashed green line) across the entire pH range. The newfound stability of  \( MoS_{2} \)  towards dissolution processes is due to the positive and high vacancy formation energies which, at a vacancy density of  \( 0.012\ \AA^{-2} \)  (one vacancy every nine unit cells) and relative to the vacant elements in their standard states, amounts to  \( 2.97\ eV \)  (S vacancies) and  \( 7.74\ eV \)  (Mo vacancies). The stability towards surface passivation is due to  \( MoS_{2} \)  the low basal plane reactivity [46–48] leading to positive adsorption energies of O, OH and H adsorbates (0.72, 1.80 and 2.20 eV, respectively).

The SPD diagram in Fig. 3b shows excellent agreement with the aforementioned CV scans, identifying a stability window at pH 0 between +0.3 and -1.1 V. Above 0.3 V, surface passivation with atomic oxygen is predicted to be favorable. In comparison, the experiments find the material to be stable up to at least 0.5 V. Nevertheless,
 

both cited papers [39, 40], as well as a study by Chia et al. [49], report the onset of an anodic peak already at 0.3 V, suggesting the occurrence of a reversible oxidative process already in the 0.3-0.5 V region. By comparison with Fig. 3b, this process can be attributed to the adsorption of low coverage atomic oxygen.

The diagram in Fig. 3b discussed so far describes early steps of degradation processes affecting a pristine  \( MoS_{2} \)  reference structure. In principle, however, the pristine structure is an idealization and any real material will contain defects, e.g., vacancies or other types of point defects, even if they are thermodynamically unstable. Such defects may act as nucleation centers for extended defects such as vacancy pairs, clusters, or line defects, which could eventually lead to the degradation of the material. This means that the pristine crystal structure/surface may not be a realistic reference structure for the SPD analysis. In Fig. 3c, we investigate the role of native defects on the stability of  \( MoS_{2} \)  towards dissolution by using a surface with a pre-existing Mo vacancy as the reference state and defining dissolution processes that produce a second neighboring Mo or S vacancy. We find that Mo defects greatly stabilize nearby S vacancies, whose formation energy is decreased from 2.97 eV on the pristine surface to 0.91 eV. As a consequence, the dissolution into sulfur-containing ions and molecules becomes accessible at more moderate potentials, significantly reducing in size the stability domain of  \( MoS_{2} \)  and making the presence of Mo vacancies in the as-synthesized material undesirable. With that said, we highlight that given their really high formation energy, a large concentration of Mo vacancies is unlikely to occur experimentally. The same cooperative effect is not seen for other combinations of defect pairs. For instance, forming an S vacancy next to a pre-existing S vacancy yields practically the same formation energy (2.96 eV) as creating the first S vacancy on the pristine surface. Our results suggest that the nucleation of extended defects on  \( MoS_{2} \)  is unlikely: after the S atoms around a pre-existing Mo vacancy are preferentially dissolved, subsequent dissolution steps do not gain a significant advantage from the newly formed S vacancies and an eventual radial expansion of the defect is prevented.

Finally, a study by Tsai et al. investigates the effect of electrochemically induced sulphur vacancies at the basal plane of  \( MoS_{2} \)  on the HER catalytic activity [50]. The experimental onset of the desulphurization process is observed around -0.5 V vs. RHE. The S vacancy concentration reaches an equilibrium value at about -1.0 V, where  \( H_{2}S \)  formation is predicted theoretically to be favourable. These observations are in good agreement with the results presented in fig. 3d, showing the energy profile as a function of the electrode potential of different dissolution processes involving the formation of S vacancies, after imposing the experimental pH value of 0.3. At -0.84 V vs. RHE,  \( MoS_{2} \)  dissolves favourably into  \( HS^{-} \) ions, which can be related to the experimental onset of the desulphurization process. At -1.06 V  \( H_{2}S \)  formation becomes favourable as well, in perfect agreement with the theoretical results in the cited work.
Phosphorene Phosphorene is the 2D counterpart of black phosphorus, which has a layered structure in bulk phase and can be mechanically exfoliated. Due to its high hole mobility and tunable band gap, phosphorene has been identified as a promising candidate for applications in field-effect transistors and photodetectors [51–53]. One of the main practical limitations towards the use of phosphorene in opto-electronic devices is its poor stability in presence of oxygen and moisture, making its encapsulation in more stable materials a necessary precaution [54–56].

As expected, the CPD in Fig. 4a predicts phosphorene to be unstable under ambient conditions, represented by the dashed line at U=0 V. This is mainly due to the wide range of stable oxidation states of phosphor and, accordingly, of solvated oxyanions  \( H_{x}P_{y}O_{n}^{2-} \)  with low formation energies. From a microscopic point of view, the phosphorene surface is rather reactive: oxygen adsorption is exothermic under standard conditions (-56.1 meV at 25% coverage) and the P vacancy formation energy is only 1.70 eV. Accordingly, some of the available dissolution and passivation pathways have negative  \( \Delta G \)  in absence of an applied potential and, similarly to the CPD, the SPD in Fig. 4b predicts the material to be unstable in ambient conditions.

As observed by Wood et al., phosphorene samples in ambient conditions degrade in few days. As the process is monitored, an XPS peak attributed to oxidized phosphor species ( \( PO_{x} \) ) appears with concurrent formation of bubbles on the sample surface [57]. These are clear signs of a spontaneous reaction resulting in the oxidation of the surface P atoms and the concurrent evolution of a gaseous species. Fig. 4c shows the energy profile of different spontaneous degradation pathways of phosphorene in ambient conditions, described by the U=0 dashed line in fig. 4b. The EDS found along the latter (1.0 ML O passivation, dissolution into  \( HPO_{4}^{2-}/PO_{4}^{3-} \) ) - as well as several other dissolution and passivation processes not shown here - are all thermodynamically favorable over the whole pH range and can take place simultaneously without the aid of an applied potential. These oxidative processes are paralleled by the catalytic conversion of solvated protons into  \( H_{2} \) , as shown by the atomic models at the top of Fig. 4d. Mixed surface processes (see the two models at the bottom of Fig. 4d) form the pink band (H adsorption + dissolution) and blue band (O adsorption + H adsorption) in Fig. 4c. Since these are mildly endoergonic over the entire pH range, they are not expected to contribute to the material degradation. Our analysis suggests that, after a prolonged exposure to the atmospheric moisture, phosphorene releases a variety of phosphor oxoanions while adsorbing oxygen, leaving a partially dissolved, partially passivated surface. The XPS peaks observed in the cited study can be attributed to oxoanions such as  \( HPO_{4}^{2-} \)  and  \( PO_{4}^{3-} \) , which can remain adsorbed on the surface, as well as the P atoms in contact with the adsorbed oxygen. All of these degradation processes are paralleled by hydrogen evolution, the most logical origin of the bubbles observed experimentally.

Ti_{2}C MXene MXenes are a class of 2D materials that belong to the family of transition metal carbides, nitrides, and carbonitrides (M: transition metal; X: carbon and/or
 
![](./images/1139167458217689096_8.jpg)

Aqueous stability of phosphorene

![](./images/1139167458217689096_9.jpg)

(d)

![](./images/1139167458217689096_10.jpg)

![](./images/1139167458217689096_11.jpg)

Figure 4: a) Conventional Pourbaix diagram of phosphorene, with Pt as the reference electrode. b) Surface Pourbaix diagram of phosphorene, with Pt as the reference electrode. The dashed black line at U=0V vs. Pt highlights the relevant region for stability predictions about spontaneous processes. c) Slice of the diagram in panel b along the dashed line at U=0V, obtained by including mixed surface states. The light blue lines forming a band at positive free energies represent all the mixed adsorption-adsorption states. The pink band contains all the mixed adsorption-dissolution states. The three colored lines at negative free energies represent the free energy profile of the most stable phases found along the 0 V line in panel b. Vertical dashed lines highlight the pH corresponding to the phase boundaries. d) Atomic models illustrating the four different types of processes present in panel (c).

nitrogen). Often characterized by exceptional electronic, mechanical, and thermal properties, these materials are highly versatile for a range of applications including batteries [58], gas sensing [59] and photocatalysis [60]. Titanium carbide  \( Ti_{x}C_{y} \)  is among the most studied MXenes. It is characterized by a rich surface chemistry which poses challenges towards its use in electrochemical applications. For instance,  \( Ti_{x}C_{y} \)  electrodes have been recently tested as HER catalysts, showing only modest performance which tends to further decrease over several cycles [26]. As observed by Zhang et al., colloidal suspensions of  \( Ti_{3}C_{2} \)  can decompose to  \( TiO_{2} \)  and amorphous carbon over several days in solution [61]. It has also been found that the material tends to form passivation layers [62, 63] and to decompose in aqueous environments.

The general instability of  \( Ti_{x}C_{y} \)  in an aqueous environment together with its rich surface chemistry makes this system a perfect case study for our SPD framework. We choose as our model surface the thinnest possible form of titanium carbide, namely  \( Ti_{2}C \) . The CPD of  \( Ti_{2}O \)  shown in Fig. S1 predicts the material to be unstable in agreement with the experimental evidence, but provides no information about its surface state. In order to cover a wider range of surface terminations, we model the adsorption of O, OH and H at various coverages (0.1ML, 0.33ML, 0.66ML, 1.0ML) and we include mixed coverage states. The SPD, shown in Fig. 5a, highlights the remarkable surface reactivity of  \( Ti_{2}C \) , which favors the coverage by a full monolayer of adsorbates in the whole spanned U-pH region. As expected, the overall oxidation state of the adsorbate layer progressively increases when moving from negative to positive applied potentials, going from a ML of adsorbed hydrogen up to a ML of oxygen. Mixed coverage states are found stable at intermediate poten-
 
![](./images/1139167458217689096_12.jpg)

![](./images/1139167458217689096_13.jpg)

Aqueous stability of Ti₂C

![](./images/1139167458217689096_14.jpg)

(d)

![](./images/1139167458217689096_15.jpg)

![](./images/1139167458217689096_16.jpg)

![](./images/1139167458217689096_17.jpg)

Figure 5: a) Surface Pourbaix diagram of  \( Ti_{2}C \)  with SHE as the reference electrode, including mixed adsorption states. The color map shows the Pourbaix energy per unit formula. For better visualization, the reference system chosen for defining the pourbaix energy scale is the 2/3ML O*, 1/3ML OH* mixed adsorption state. An inset covering the darkened region is shown at the top right in order to better highlight the phases associated with narrow stability domains. b) Surface pourbaix diagram of  \( Ti_{2}C \)  obtained by considering only the dissolution processes, i.e., adsorption configurations are omitted during the diagram construction. An analogous diagram, obtained by using the surface with a pre-existing Ti vacancy as the reference state, is overlaid (dashed lines). c) Slice of the diagram in panel (a) along the dashed line at U=0V. Mixed surface reactions are included. The light blue lines forming a band at positive free energies represent all the mixed adsorption reactions. The pink band contains all the mixed adsorption-dissolution reactions. The dark blue lines represent adsorption processes paralleled by hydrogen evolution. The three dark red lines represent the most stable dissolved phases of  \( Ti_{2}C \)  ( \( Ti^{3+} \) ,  \( TiO^{2+} \) ,  $ HT

tials. These results agree well with the surface Pourbaix diagram obtained by Gao et al. [63], with the difference that in our SPD we include hydrogen adsorption, which becomes stable at negative potentials.

We note that surface vacancies are not found to be energetically favorable under any voltage or pH conditions. Nevertheless, several of the dissolution processes have negative  \( \Delta G \)  in extended regions of the diagram, as seen in the SPD in Fig. 5b, obtained by masking all the adsorption configurations and thus showing only vacancy EDS. Similar to the case of  \( MoS_{2} \) , pre-existing Ti vacancies are found to stabilize neighboring ones, although to a smaller extent: their formation is reduced from 2.89 eV on the pristine surface to 2.34 eV on a defective one. This causes some of the dissolved phases (especially  \( Ti^{2+} \)  and  \( HTiO_{3}^{-} \) to extend their stability domain by a small, but significant amount (see the dashed lines).

In order to investigate spontaneous degradation processes, we report in Fig. 5c a slice of the SPD against the Pt electrode at U = 0. Despite passivation processes being the most favourable ones from a thermodynamic standpoint, at least one of the "pure" dissolution EDS (red lines) is exoergonic in any pH conditions, supporting the observations by Xia et al. regarding the role of Ti vacancies in  \( Ti_{2}C \)  degradation [64]. Furthermore, all the mixed adsorption-dissolution reactions (pink band) are spontaneous across the entire pH range. This suggests a cooperative role of passivation and Ti dissolution in compromising the material stability, compatibly with the observations by Ibragimova et al. [65].

Overall, these results confirm the natural tendency of bare titanium carbide surfaces to form stable passivation
 

layers, whose composition depends on the applied potential and pH conditions. The dissolution of Ti surface atoms, enhanced in presence of native Ti vacancies, is confirmed to contribute to the material degradation.

## Conclusions

In this work we employ both a conventional Pourbaix diagram (CPD) and a surface Pourbaix diagram (SPD) methodology in order to investigate the electrochemical stability of solid state materials, with a focus on two-dimensional (2D) materials. Our updated CPD description implemented in the ASE python package, used as a backbone for the SPD implementation, is proven suitable for rapidly finding qualitative trends on large material datasets. With that said, we find the CPD to severely underestimate the electrochemical stability in general, as highlighted by the very low number of 2D materials found stable in HER and OER conditions. We attribute this to the neglect of early degradation steps (EDS) with unfavorable thermodynamics that can prevent degradation processes to take place.

The EDS are captured by our comprehensive SPD framework, employed on  \( MoS_{2} \) , phosphorene and  \( Ti_{2}C \)  as three separate case studies. The SPD grants mechanistic insight, great flexibility and predictive power when comparing to experimental results, at the expense of a higher computational cost. Using the SPD, we quantitatively reproduce the experimental desulphurization potential and stability window of  \( MoS_{2} \) , incorrectly described by the CPD. Our results also suggest that  \( MoS_{2} \)  samples with a significant concentration of Mo vacancies are more prone to dissolution compared to samples with low defectivity. As for phosphorene and  \( Ti_{2}C \) , the SPD provides additional mechanistic insight on their spontaneous degradation and surface state as a function of the pH and applied potential, supporting experimental and theoretical results in good agreement.

We stress that including vacancy configurations in the SPD is fundamental in order to cover dissolution processes, thus obtaining a complete picture of the electrochemical stability of materials in general. The accuracy of SPD results can be improved by operating on the ab initio modeling of the surface configurations. For instance, including solvation effects or investigating different vacancy concentrations can further reduce the gap between theoretical predictions and experiments. Overall, we discourage the use of CPD results as conclusive data on the electrochemical stability of materials. We recommend instead the SPD whenever a detailed comprehension of electrochemical degradation processes is required.

As a final remark, we point out that performance and stability are tightly connected. With the focus in the materials science literature often being on materials properties rather than on stability, obtaining accurate models for the latter is complicated by the lack of reliable data. Advancing our understanding of (electrochemical) stability of materials can be only reached only by combining high quality experimental data with accurate computational modeling. We believe that more efforts have to be dedicated in both the experimental and computational communities to understanding fundamental degradation mechanisms and elucidating the surface structure and stability of materials.

## Methods

Conventional Pourbaix diagrams An efficient utility to calculate conventional Pourbaix diagrams was implemented in the Atomic Simulation Environment (ASE) package [31]. The method initially defines a list of electrochemical reactions describing every possible decomposition pathway of the target material into competing solid and solvated phases. We retrieve the relevant solid phases from the OQMD database [66], and the solvated phases from the ASE phase diagram utility. The reaction free energy  \( \Delta G \)  of each electrochemical process at temperature T is determined by writing the Gibbs free energy in terms of the pH of the solution and the potential U applied between the working electrode (represented by the target material) and a reference electrode of choice:

 \[ \Delta G=\Delta G^{0}+k_{B}T\ln Q^{\prime}-n_{\mathrm{H}}\alpha\mathrm{pH}-n_{e}U \quad (2) \] 

With  \( \alpha = k_{B}T \ln 10 \) .  \( n_{H} \)  and  \( n_{e} \)  are the number of protons and electrons, respectively, exchanged in the semi-reaction at the working electrode. Their values are positive for reactants and negative for products. Electrons are among the products in oxidation processes, and among the reactants in reduction processes.

The standard reaction free energy is written as

 \[ \Delta G^{0}=\sum_{r}\mu_{r}^{0}n_{r}-\sum_{p}\mu_{p}^{0}n_{p} \quad (3) \] 

where  \( n_{r} \)  and  \( n_{p} \)  denote the stoichiometric coefficients of reactants and products, respectively. The standard chemical potentials  \( \mu^{0} \)  of all the solid species are represented by their formation energies with respect to the elements in their standard state. For species containing hydrogen and/or oxygen, we correct the standard state energies following Persson et al. [67]. The  \( \mu_{0} \)  of solvated species are obtained from thermodynamic tables [27,68].  \( Q' = \prod_{i \neq H^{+}} a_{i}^{n_{i}} \)  gathers the activities of the ionic species (except for  \( H^{+} \) ) as determined by their concentration which we set to the fixed value of  \( 10^{-6} \)  mol  \( L^{-1} \) . The contribution from protons is considered separately in the pH term.

The code supports the use of five different reference electrodes, which are modeled by applying a zero-point shift of  \( -n_{e}U_{ref}^{0} \)  to eq. 2 and including an additional contribution to the pH term when needed. The Standard Hydrogen Electrode (SHE) sets the zero of the potential scale, hence  \( U_{ref}^{0}=0V \) , and carries no pH dependence. For the Ag/AgCl and Saturated Calomel Electrode (SCE)  \( U_{ref}^{0} \)  amounts to 0.222V and 0.244V, respectively, with no pH dependence. For the Reversible Hydrogen Electrode (RHE),  \( U_{ref}^{0}=0V \)  and a pH-dependent contribution of  \( n_{e}\alpha pH \)  is included in eq. 2. We include the Pt electrode as well, which conceptually represents any inert metallic electrode able to perform the hydrogen evolution reaction (HER) and the oxygen evolution reaction (OER).
 

catalytically. For all oxidation processes \((n_{e} > 0)\), the Pt electrode behaves exactly as the RHE, hence the same \(U_{\mathrm{ref}}^{0}\) and pH correction apply. However, since a Pt electrode cannot reverse the HER or the OER as it is not supplied by \(\mathrm{H}_{2}\) or \(\mathrm{O}_{2}\), all the reduction processes \((n_{e} < 0)\) are raised in energy by \(n_{e} U_{\mathrm{O}_{2}/\mathrm{H}_{2}\mathrm{O}}^{0}\), where \(U_{\mathrm{O}_{2}/\mathrm{H}_{2}\mathrm{O}}^{0} = 1.23\mathrm{V}\) is the standard electrode potential of the oxygen evolution reaction (OER) - and maintain the pH dependence. The potential profile as a function of the pH of the implemented reference electrodes is shown in Fig. S2.

When generating Pourbaix diagrams, an expression of the form of Eq. 2 is pre-computed for each of the considered reaction pathways, and then evaluated as a function of the pH and applied potential U. This allows to simultaneously determine the energy  \( \Delta G_{pbx} \)  of the target material relative to the most stable competing phase and the identity of the latter:

 \[ \Delta G_{pbx}(pH,U)=-\min_{react}\Delta G(pH,U) \quad (4) \] 

where all considered reaction pathways are included on the right hand side. If  \( \Delta G_{pbx} \)  is negative in a given pH-U window, the target material is labeled as stable.

Surface Pourbaix diagrams The same ASE framework was employed (partially) to generate surface Pourbaix diagrams. Density functional theory as implemented in GPAW [69] is used to obtain the relaxed geometry and ground state energy of the reference surface and early intermediate states. We employ the PBE exchange-correlation functional [70] and include Grimme D3 corrections [71] in order to capture van der Waals interactions. A 3x3x1 supercell is utilized for all surface configurations except when considering pre-existing vacancies where 4x4x1 supercells are employed. The chemical potentials of the pristine surface and early intermediates are represented by their formation energies obtained from the D3-corrected total energies. The early degradation steps represent all the considered electrochemical processes. These are laid out by combining the reference surface configuration with each of the early intermediates and balancing out with  \( H_{2}O \) ,  \( H^{+} \) , electrons, and ionic species. e.g.:

 \[ \mathrm{MoS_{2}+H_{2}O\longrightarrow MoS_{2}(OH)+H^{+}+e^{-}} \quad (5) \] 

 \[ \mathrm{MoS_{2}+4H_{2}O\longrightarrow MoS_{2}(VS)+SO_{4}^{2-}+8H^{+}+6e^{-}} \quad (6) \] 

In the above reactions  \( \mathrm{MoS_{2}(OH)} \)  and  \( \mathrm{MeS_{2}(VS)} \)  represent  \( \mathrm{MoS_{2}} \)  with an adsorbed OH and with a S vacancy, respectively. The construction of the surface Pourbaix diagram proceeds analogous to the one described for conventional Pourbaix diagrams. Pourbaix energies are normalized with respect to the number of formula units in the supercell. A comprehensive view of all the EDS considered by the SPD framework is shown in the supplemental material, Fig. S1.

Since the modeled electrochemical processes take place in proximity of a charged surface, it is a crude approximation to set the concentration of all charged species to the same arbitrary value as routinely done in the CPD analysis. We employ a simple correction scheme in our SPD formulation, to account for the surface excess or depletion of ionic species as a function of the applied electrode potential. The theoretical background behind the implementation of the correction scheme is described in the Supporting Material.

Aqueous stability in ambient conditions When a material is in contact with an aqueous solution without an external circuit driving electrons from or towards a counter electrode, spontaneous electrochemical degradation may still take place. In this case the material acts as both the cathode and the anode, hence the global electron transfer reaction takes place at one electrode-solution interface. Since the electrons involved in oxidation and reduction are taken/delivered at the same potential (the Fermi level of the material surface), the  \( n_{e}U \)  contribution to the reaction energetics in eq. 2 is zero. On the other hand, the pH of the solution still influences the reaction energetics. Three scenarios are possible in such conditions: (i) The electrode material gets oxidized, e.g. by adsorbing oxygen, releasing electrons into another region of the surface where  \( H_{2} \)  is catalytically evolved from  \( H^{+} \) . (ii) The electrode material gets reduced, e.g. by adsorbing hydrogen with the necessary electrons obtained from the catalytic oxidation of  \( H_{2}O \)  into  \( O_{2} \)  in a nearby surface region. (iii) Both the oxidation and reduction semi-reactions affect the surface structure of the material through adsorption or dissolution. Scenarios i) and ii) are practically reproduced by slicing along the U = 0 line the SPD of the target material against the Pt electrode. In order to reproduce scenario iii), we include in the same slice a set of reactions obtained by combining oxidation and reduction EDS's with each other, e.g:

 \[  A)MoS_{2}+H_{2}O\longrightarrow MoS_{2}(OH)+H^{+}+e^{-} \quad (7) \] 

 \[  B)MoS_{2}+H^{+}+e^{-}\longrightarrow MoS_{2}(H) \quad (8) \] 

 \[  A+B)2MoS_{2}+H_{2}O\longrightarrow MoS_{2}(H)+MoS_{2}(OH) \quad (9) \] 

## 1 Supporting Information

List of the 72 materials found as highly stable under the CPD, CPD of the  \( Ti_{2}C \)  MXene, Implemented reference electrodes and their pH-dependent potentials, illustrations of electrochemical processes modeled by the SPD, surface excess correction scheme (PDF).

The complete list of 3376 materials used for the CPD analysis (Fig. 1 and Table 1), as well as the code used for generating the SPD and acquies stability diagrams are available at https://github.com/surfpbx/surfpbx.

## 2 Acknowledgements

S.A. and K.S.T. acknowledge funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program Grant No. 773122 (LIMA) and the Villum Investigator Grant No. 37789 supported by VILLUM FONDEN. I.E.C. acknowledge support from the Independent Research Fund Denmark (Research Project 1, project “Rational Design of High-Entropy
 

Oxides for Protonic Ceramic Fuel Cells (HERCULES)", grant No 1032-00269B).
 

## References

[1] Jeff Greeley, Thomas F Jaramillo, Jacob Bonde, IB Chorkendorff, and Jens K Nørskov. Computational high-throughput screening of electrocatalytic materials for hydrogen evolution. Nature Materials, 5(11):909–913, 2006.

[2] Georg KH Madsen. Automated search for new thermoelectric materials: the case of liznsb. Journal of the American Chemical Society, 128(37):12140–12146, 2006.

[3] Stefano Curtarolo et al. The high-throughput highway to computational materials design. Nature Materials, 12(3):191–201, 2013.

[4] Scott Kirklin, Bryce Meredig, and Chris Wolverton. High-throughput computational screening of new lithium battery anode materials. Advanced Energy Materials, 3(2):252–262, 2013.

[5] Kristian B Ørnø, Juan M Garcia-Lastra, and Kristian S Thygesen. Computational screening of functionalized zinc porphyrins for dye sensitized solar cells. Physical Chemistry Chemical Physics, 15(44):19478–19486, 2013.

[6] Zihe Zhang et al. Computational screening of layered materials for multivalent ion batteries. ACS Omega, 4(4):7822–7828, 2019.

[7] Wei Chen et al. Understanding thermoelectric properties from high-throughput calculations: trends, insights, and comparisons with experiment. J. Mater. Chem. C, 4(20):4414–4426, 2016.

[8] Johannes Hachmann, Roberto Olivares-Amaya, Sule Atahan-Evrenk, Carlos Amador-Bedolla, Roel S Sánchez-Carrera, Aryeh Gold-Parker, Leslie Vogt, Anna M Brockway, and Alán Aspuru-Guzik. The harvard clean energy project: large-scale computational screening and design of organic photovoltaics on the world community grid. The Journal of Physical Chemistry Letters, 2(17):2241–2251, 2011.

[9] Sandip Bhattacharya and Georg KH Madsen. High-throughput exploration of alloying as design strategy for thermoelectrics. Physical Review B, 92(8):085205, 2015.

[10] Ivano E Castelli et al. Computational screening of perovskite metal oxides for optimal solar light capture. Energy and Environmental Sciences, 5(2):5814–5819, 2012.

[11] Geoffroy Hautier, Anna Miglio, Gerbrand Ceder, Gian-Marco Rignanese, and Xavier Gonze. Identification and design principles of low hole effective mass p-type transparent conducting oxides. Nature Communications, 4(1):1–7, 2013.

[12] Liping Yu and Alex Zunger. Identification of potential photovoltaic absorbers based on first-principles spectroscopic screening of materials. Physical Review Letters, 108(6):068701, 2012.

[13] Korina Kuhar, Mohnish Pandey, Kristian S Thygesen, and Karsten W Jacobsen. High-throughput computational assessment of previously synthesized semiconductors for photovoltaic and photoelectrochemical devices. ACS Energy Letters, 3(2):436–446, 2018.

[14] Muratahan Aykol, Soo Kim, Vinay I Hegde, David Snydacker, Zhi Lu, Shiqiang Hao, Scott Kirklin, Dane Morgan, and Christopher Wolverton. High-throughput computational design of cathode coatings for li-ion batteries. Nature communications, 7(1):1–12, 2016.

[15] Nicolas Mounet, Marco Gibertini, Philippe Schwaller, Davide Campi, Andrius Merkys, Antimo Marrazzo, Thibault Sohier, Ivano Eligio Castelli, Andrea Cepellotti, Giovanni Pizzi, and Nicola Marzari. Two-dimensional materials from high-throughput computational exfoliation of experimentally known compounds. Nature Nanotechnology, 13(3):246–252, 2018.

[16] Long-Qing Chen, Li-Dong Chen, Sergei V Kalinin, Gerhard Klimeck, Sanat K Kumar, Jörg Neugebauer, and Ichiro Terasaki. Design and discovery of materials guided by theory and computation. npj Computational Materials, 1(1):1–2, 2015.

[17] Qing Hua Wang, Kourosh Kalantar-Zadeh, Andras Kis, Jonathan N Coleman, and Michael S Strano. Electronics and optoelectronics of two-dimensional transition metal dichalcogenides. Nature Nanotechnology, 7(11):699–712, 2012.

[18] Sajedeh Manzeli, Dmitry Ovchinnikov, Diego Pasquier, Oleg V Yazyev, and Andras Kis. 2d transition metal dichalcogenides. Nature Reviews Materials, 2(8):1–15, 2017.

[19] Vigneshwaran Shanmugam, Rhoda Afriyie Mensah, Karthik Babu, Sidique Gawusu, Avishek Chanda, Yongming Tu, Rasoul Esmaeely Neisiany, Michael Försth, Gabriel Sas, and Oisik Das. A review of the synthesis, properties, and applications of 2d materials. Particle & Particle Systems Characterization, 39(6):2200031, 2022.

[20] Andrea C Ferrari, Francesco Bonaccorso, Vladimir Fal'Ko, Konstantin S Novoselov, Stephan Roche, Peter Bøggild, Stefano Borini, Frank HL Koppens, Vincenzo Palermo, Nicola Pugno, et al. Science and technology roadmap for graphene, related two-dimensional crystals, and hybrid systems. Nanoscale, 7(11):4598–4810, 2015.

[21] Yury Gogotsi and Babak Anasori. The rise of mxenes, 2019.

[22] Le Shi and Tianshou Zhao. Recent advances in inorganic 2d materials and their applications in lithium and sodium batteries. Journal of Materials Chemistry A, 5(8):3735–3758, 2017.
 

[23] Mohnish Pandey and Kristian S Thygesen. Two-dimensional mxenes as catalysts for electrochemical hydrogen evolution: A computational screening study. The Journal of Physical Chemistry C, 121(25):13593–13598, 2017.

[24] Mohnish Pandey, Aleksandra Vojvodic, Kristian S Thygesen, and Karsten W Jacobsen. Two-dimensional metal dichalcogenides and oxides for hydrogen evolution: a computational screening approach. The Journal of Physical Chemistry Letters, 6(9):1577–1585, 2015.

[25] Jakob Kibsgaard, Zhebo Chen, Benjamin N Reinecke, and Thomas F Jaramillo. Engineering the surface structure of mos2 to preferentially expose active edge sites for electrocatalysis. Nature materials, 11(11):963–969, 2012.

[26] Zhi Wei Seh, Kurt D Fredrickson, Babak Anasori, Jakob Kibsgaard, Alaina L Strickler, Maria R Lukatskaya, Yury Gogotsi, Thomas F Jaramillo, and Aleksandra Vojvodic. Two-dimensional molybdenum carbide (mxene) as an efficient electrocatalyst for hydrogen evolution. ACS Energy Letters, 1(3):589–594, 2016.

[27] Marcel Pourbaix. Atlas of electrochemical equilibria in aqueous solutions. NACE, 1966.

[28] Ivano E Castelli, Kristian S Thygesen, and Karsten W Jacobsen. Calculated pourbaix diagrams of cubic perovskites for water splitting: stability against corrosion. Topics in Catalysis, 57:265–272, 2014.

[29] Aniketa Shinde, Santosh K Suram, Qimin Yan, Lan Zhou, Arunima K Singh, Jie Yu, Kristin A Persson, Jeffrey B Neaton, and John M Gregoire. Discovery of manganese-based solar fuel photoanodes via integration of electronic structure calculations, pourbaix stability modeling, and high-throughput experiments. ACS Energy Letters, 2(10):2307–2312, 2017.

[30] Seoin Back, Kevin Tran, and Zachary W Ulissi. Discovery of acid-stable oxygen evolution catalysts: high-throughput computational screening of equimolar bimetallic oxides. ACS applied materials & interfaces, 12(34):38256–38265, 2020.

[31] Ask Hjorth Larsen, Jens Jørgen Mortensen, Jakob Blomqvist, Ivano E Castelli, Rune Christensen, Marcin Dulak, Jesper Friis, Michael N Groves, Bjørk Hammer, Cory Hargus, et al. The atomic simulation environment—a python library for working with atoms. Journal of Physics: Condensed Matter, 29(27):273002, 2017.

[32] Sten Haastrup, Mikkel Strange, Mohnish Pandey, Thorsten Deilmann, Per S Schmidt, Nicki F Hinsche, Morten N Gjerding, Daniele Torelli, Peter M Larsen, Anders C Riis-Jensen, et al. The computational 2d materials database: high-throughput modeling and discovery of atomically thin crystals. 2D Materials, 5(4):042002, 2018.

[33] MN Gjerding, A Taghizadeh, A Rasmussen, S Ali, F Bertoldo, T Deilmann, UP Holguin, NR Knøsgaard, M Kruse, S Manti, et al. Recent progress of the computational 2d materials database (c2db). arXiv:2102.03029, 2021.

[34] Sha Li, Shanshan Wang, Matteo M Salamone, Alex W Robertson, Simantini Nayak, Heeyeon Kim, SC Edman Tsang, Mauro Pasta, and Jamie H Warner. Edge-enriched 2d mos2 thin films grown by chemical vapor deposition for enhanced catalytic performance. ACS Catalysis, 7(1):877–886, 2017.

[35] Jieun Yang, Abdul Rahman Mohmad, Yan Wang, Raymond Fullon, Xiuju Song, Fang Zhao, Ibrahim Bozkurt, Mathias Augustin, Elton JG Santos, Hyeon Suk Shin, et al. Ultrahigh-current-density niobium disulfide catalysts for hydrogen evolution. Nature materials, 18(12):1309–1314, 2019.

[36] Jiao Deng, Pengju Ren, Dehui Deng, and Xinhe Bao. Enhanced electron penetration through an ultrathin graphene layer for highly efficient catalysis of the hydrogen evolution reaction. Angewandte Chemie International Edition, 54(7):2100–2104, 2015.

[37] Sehmus Ozden, Sumit Bawari, Soumya Vinod, Ulises Martinez, Sandhya Susarla, Claudia Narvaez, Jarin Joyner, Chandra Sekhar Tiwary, Tharangattu N Narayanan, and Pulickel M Ajayan. Interface and defect engineering of hybrid nanostructures toward an efficient her catalyst. Nanoscale, 11(26):12489–12496, 2019.

[38] Xi Rong and Alexie M Kolpak. Ab initio approach for prediction of oxide surface structure, stoichiometry, and electrocatalytic activity in aqueous solution. The journal of physical chemistry letters, 6(9):1785–1789, 2015.

[39] Karthikeyan Krishnamoorthy, Ganesh Kumar Veerasubramani, Sivaprakasam Radhakrishnan, and Sang Jae Kim. Supercapacitive properties of hydrothermally synthesized sphere like mos \( ^{2} \)  nanostructures. Materials Research Bulletin, 50:499–502, 2014.

[40] RB Pujari, AC Lokhande, AR Shelke, JH Kim, and CD Lokhande. Chemically deposited nano grain composed mos \( ^{2} \)  thin films for supercapacitor application. Journal of colloid and interface science, 496:1–7, 2017.

[41] Xiao Li and Hongwei Zhu. Two-dimensional mos2: Properties, preparation, and applications. Journal of Materiomics, 1(1):33–44, 2015.

[42] Min Sup Choi, Deshun Qu, Daeyeong Lee, Xiaochi Liu, Kenji Watanabe, Takashi Taniguchi, and Won Jong Yoo. Lateral mos2 p-n junction formed by chemical doping for use in high-performance optoelectronics. ACS nano, 8(9):9332–9340, 2014.
 

[43] Mark A Lukowski, Andrew S Daniel, Fei Meng, Audrey Forticaux, Linsen Li, and Song Jin. Enhanced hydrogen evolution catalysis from chemically exfoliated metallic mos \( _{2} \)  nanosheets. Journal of the American Chemical Society, 135(28):10274–10277, 2013.

[44] Yang Cao. Roadmap and direction toward high-performance mos \( _{2} \)  hydrogen evolution catalysts. ACS nano, 15(7):11014–11039, 2021.

[45] Yang Liu, Yingcan Zhao, Xinbo Zhang, Xuanlin Huang, Wenchao Liao, and Yintong Zhao. Mos2-based membranes in water treatment and purification. Chemical Engineering Journal, 422:130082, 2021.

[46] Hong Li, Charlie Tsai, Ai Leen Koh, Lili Cai, Alex W Contryman, Alex H Fragapane, Jiheng Zhao, Hyun Soo Han, Hari C Manoharan, Frank Abild-Pedersen, et al. Activating and optimizing mos \( ^{2} \)  basal planes for hydrogen evolution through the formation of strained sulphur vacancies. Nature materials, 15(1):48–53, 2016.

[47] Wenzhuo Wu, Chunyao Niu, Cong Wei, Yu Jia, Chong Li, and Qun Xu. Activation of mos2 basal planes for hydrogen evolution by zinc. Angewandte Chemie International Edition, 58(7):2029–2033, 2019.

[48] Xiaolei Huang, Mei Leng, Wen Xiao, Meng Li, Jun Ding, Teck Leong Tan, Wee Siang Vincent Lee, and Junmin Xue. Activating basal planes and s-terminated edges of mos2 toward more efficient hydrogen evolution. Advanced functional materials, 27(6):1604943, 2017.

[49] Xinyi Chia, Adriano Ambrosi, Zdenek Sofer, Jan Luxa, and Martin Pumera. Catalytic and charge transfer properties of transition metal dichalcogenides arising from electrochemical pretreatment. ACS nano, 9(5):5164–5179, 2015.

[50] Charlie Tsai, Hong Li, Sangwook Park, Joonsuk Park, Hyun Soo Han, Jens K Nørskov, Xiaolin Zheng, and Frank Abild-Pedersen. Electrochemical generation of sulfur vacancies in the basal plane of mos2 for hydrogen evolution. Nature communications, 8(1):15113, 2017.

[51] Han Liu, Adam T Neal, Zhen Zhu, Zhe Luo, Xianfan Xu, David Tománek, and Peide D Ye. Phosphorene: an unexplored 2d semiconductor with a high hole mobility. ACS nano, 8(4):4033–4041, 2014.

[52] Alexandra Carvalho, Min Wang, Xi Zhu, Aleksandr S Rodin, Haibin Su, and Antonio H Castro Neto. Phosphorene: from theory to applications. Nature Reviews Materials, 1(11):1–16, 2016.

[53] Varrla Eswaraiah, Qingsheng Zeng, Yi Long, and Zheng Liu. Black phosphorus nanosheets: synthesis, characterization and applications. Small, 12(26):3480–3502, 2016.

[54] David K Sang, Huide Wang, Zhinan Guo, Ni Xie, and Han Zhang. Recent developments in stability and passivation techniques of phosphorene toward next-generation device applications. Advanced Functional Materials, 29(45):1903419, 2019.

[55] Angelo Ziletti, A Carvalho, David K Campbell, David F Coker, and Antonio Helio Castro Neto. Oxygen defects in phosphorene. Physical review letters, 114(4):046801, 2015.

[56] Mohammad Ziaur Rahman, Chi Wai Kwong, Kenneth Davey, and Shi Zhang Qiao. 2d phosphorene as a water splitting photocatalyst: fundamentals to applications. Energy & Environmental Science, 9(3):709–728, 2016.

[57] Joshua D Wood, Spencer A Wells, Deep Jariwala, Kan-Sheng Chen, EunKyung Cho, Vinod K Sangwan, Xiaolong Liu, Lincoln J Lauhon, Tobin J Marks, and Mark C Hersam. Effective passivation of exfoliated black phosphorus transistors against ambient degradation. Nano letters, 14(12):6964–6970, 2014.

[58] Fangwang Ming, Hanfeng Liang, Gang Huang, Zahra Bayhan, and Husam N Alshareef. MXenes for rechargeable batteries beyond the lithium-ion. Advanced Materials, 33(1):2004039, 2021.

[59] Eunji Lee, Armin VahidMohammadi, Barton C Prorok, Young Soo Yoon, Majid Beidaghi, and Dong-Joo Kim. Room temperature gas sensing of two-dimensional titanium carbide (mxene). ACS applied materials & interfaces, 9(42):37184–37190, 2017.

[60] Qian Zhong, Yuan Li, and Gaoke Zhang. Two-dimensional mxene-based and mxene-derived photocatalysts: Recent developments and perspectives. Chemical Engineering Journal, 409:128099, 2021.

[61] Chuanfang John Zhang, Sergio Pinilla, Niall McEvoy, Conor P Cullen, Babak Anasori, Edmund Long, Sang-Hoon Park, Andrés Seral-Ascaso, Aleksey Shmeliov, Dileep Krishnan, et al. Oxidation stability of colloidal two-dimensional titanium carbides (mxenes). Chemistry of Materials, 29(11):4848–4856, 2017.

[62] Kurt D Fredrickson, Babak Anasori, Zhi Wei Seh, Yury Gogotsi, and Aleksandra Vojvodic. Effects of applied potential and water intercalation on the surface chemistry of ti2c and mo2c mxenes. The Journal of Physical Chemistry C, 120(50):28432–28440, 2016.

[63] Guoping Gao, Anthony P O'Mullane, and Aijun Du. 2d mxenes: a new family of promising catalysts for the hydrogen evolution reaction. Acs Catalysis, 7(1):494–500, 2017.

[64] Fanjie Xia, Junchao Lao, Ruohan Yu, Xiahang Sang, Jiayan Luo, Yu Li, and Jinsong Wu. Ambient oxidation of ti 3 c 2 mxene initialized by atomic defects. Nanoscale, 11(48):23330–23337, 2019.
 

[65] Rina Ibragimova, Patrick Rinke, and Hannu-Pekka Komsa. Native vacancy defects in mxenes at etching conditions. Chemistry of Materials, 34(7):2896–2906, 2022.

[66] James E Saal, Scott Kirklin, Muratahan Aykol, Bryce Meredig, and Christopher Wolverton. Materials design and discovery with high-throughput density functional theory: the open quantum materials database (oqmd). Jom, 65:1501–1509, 2013.

[67] Kristin A Persson, Bryn Waldwick, Predrag Lazic, and Gerbrand Ceder. Prediction of solid-aqueous equilibria: Scheme to combine first-principles calculations of solids with experimental aqueous states. Physical Review B—Condensed Matter and Materials Physics, 85(23):235438, 2012.

[68] James W Johnson, Eric H Oelkers, and Harold C Helgeson. Suprct92: A software package for calculating the standard molal thermodynamic properties of minerals, gases, aqueous species, and reactions from 1 to 5000 bar and 0 to 1000 c. Computers & Geosciences, 18(7):899–947, 1992.

[69] Jens Jørgen Mortensen, Ask Hjorth Larsen, Mikael Kuisma, Aleksei V Ivanov, Alireza Taghizadeh, Andrew Peterson, Anubhab Haldar, Asmus Ougaard Dohn, Christian Schäfer, Elvar Örn Jónsson, et al. Gpaw: An open python package for electronic structure calculations. The Journal of Chemical Physics, 160(9), 2024.

[70] John P Perdew, Kieron Burke, and Matthias Ernzerhof. Generalized gradient approximation made simple. Physical review letters, 77(18):3865, 1996.

[71] Stefan Grimme, Jens Antony, Stephan Ehrlich, and Helge Krieg. A consistent and accurate ab initio parametrization of density functional dispersion correction (dft-d) for the 94 elements h-pu. The Journal of chemical physics, 132(15), 2010.
 
