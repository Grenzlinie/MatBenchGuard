![](./images/885129486578745869_1.jpg)
![](./images/885129486578745869_2.jpg)

Article

# Au Single Metal Atom for Carbon Dioxide Reduction Reaction

Anna Vidal-López $^{1,2}$, Sergio Posada-Pérez $^{2,*}$![](./images/885129486578745869_3.jpg), Miquel Solà $^{2}$![](./images/885129486578745869_4.jpg) and Albert Poater $^{2,*}$![](./images/885129486578745869_5.jpg)

1.  Departament de Química, Universitat Autònoma de Barcelona, 08193 Cerdanyola del Vallès, Catalonia, Spain
2.  Institut de Química Computacional i Catalisi and Departament de Química, Universitat de Girona, c/Mª Aurèlia Capmany 69, 17003 Girona, Catalonia, Spain
*   Correspondence: sergio.posada@udg.edu (S.P.-P.); albert.poater@udg.edu (A.P.); Tel.: +34-972419403 (A.P.)

**Abstract:** $CO_2$ is the gas that contributes the most to the greenhouse effect and, therefore, to global warming. One of the greatest challenges facing humanity is the reduction of the concentration of $CO_2$ in the air. Here, we analyze the possible use of $Au_1@g$-$C_3N_4$ electrocatalyst to transform $CO_2$ into added-value products. We use density functional theory (DFT) to determine the reaction Gibbs energies for eight electron-proton transfer reaction paths of the electrochemical carbon dioxide reduction reaction (CO2RR) using a single Au atom supported on 2D carbon nitride support. Our simulations classify the $Au_1@g$-$C_3N_4$ electrocatalysts as "beyond CO" since their formation is energetically favored, although their strong binding with a Au single atom does not allow the desorption process. DFT calculations revealed that the lowest energy pathway is $CO_2$ (g) $\rightarrow COOH^* \rightarrow CO^* \rightarrow HCO^* \rightarrow HCOH^* \rightarrow CH_2OH^* \rightarrow CH_2^* \rightarrow CH_3^* \rightarrow CH_4$ (g), where the first hydrogenation of CO to HCO is predicted as the rate-limiting step of the reaction with slightly lower potential than predicted for Cu electrodes, the most effective catalysts for CO2RR. Methane is predicted to be the main reaction product after eight proton-electron transfers ($CO_2 + 8 H^+ + 8e^- \rightarrow CH_4 + 2H_2O$). The generation of formaldehyde is discarded due to the large formation energy of the adsorbed moiety and the production of methanol is slightly less favorable than methane formation. Our computational study helps to identify suitable electrocatalysts for CO2RR by reducing the amount of metal and using stable and low-cost supports.

**Keywords:** electrocatalysis; carbon dioxide reduction; Au single metal atom; carbon nitride; computational hydrogen electrode; methane production

---

## 1. Introduction

One of the most challenging and relevant problems that our society must face to improve the quality of life of future generations is climate change, with the emission of carbon dioxide ($CO_2$) considered the major contributor [1,2]. The use of renewable energy resources can drastically reduce these emissions, although nowadays approximately 80% of global energy consumption consists of fossil fuels [3]. Mitigation strategies like capture [4,5] and sequestration of $CO_2$ [6,7], or even functionalization towards other chemicals [8,9], especially cycloaddition of $CO_2$ to epoxides [10–13], have been pursued, although the conversion of $CO_2$ to valuable fuels is more promising [3,14,15]. This could promote the use of desirable waste as feedstock for added-value compounds for the industry [16–18].

From the point of view of heterogeneous catalysis, the research community is making progress in creating smaller and dispersed metal particles supported on innocent and non-innocent supports based on metal oxides [19–25] and metal carbides [26–29], with Cu as the highest active metal particle for $CO_2$ hydrogenation to methanol and Ni as the most effective metal for $CO_2$ methanation [30].

In recent years, significant progress has been made to find active and selective catalysts for electrochemical $CO_2$ reduction reaction (CO2RR) [31], where noble metals such as Pd [32], Ag [33,34], and Au [35,36], and transition metals such as Fe and Co enhance CO formation as the main product [37]. However, Cu is the rising star in this group of

![](./images/885129486578745869_6.jpg)

Citation: Vidal-López, A.;
Posada-Pérez, S.; Solà, M.; Poater, A.
Au Single Metal Atom for Carbon
Dioxide Reduction Reaction.
*Chemistry* **2023**, *5*, 1395–1406.
https://doi.org/10.3390/
chemistry5020095

Academic Editors: José
Antonio Odriozola,
Hermenegildo García and
Gianguido Ramis

Received: 4 March 2023
Revised: 7 May 2023
Accepted: 16 May 2023
Published: 5 June 2023

![](./images/885129486578745869_7.jpg)

Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

---

*Chemistry* **2023**, *5*, 1395–1406. https://doi.org/10.3390/chemistry5020095  https://www.mdpi.com/journal/chemistry

metal catalysts, since it is the only transition metal able to reduce $CO_2$ into alcohols and hydrocarbons with acceptable Faradaic efficiencies [31,38–46]. A way to drastically reduce the cost of the catalysts and at the same time increase their catalytic activity and selectivity is to use single metal atoms. Over the past decade, single-atom catalysis (SAC) has become one of the most widely researched methods for the synthesis of novel low-cost and effective catalysts [47]. It is proposed that these single metal atoms have the same principle as homogeneous catalysts, improving the selectivity with respect to metal-supported nanoparticles, although the local coordination around the single atom site plays an important role [48]. In fact, SAC can be treated as the step following supported homogeneous catalysts, since after the removal of the ligand, it is stabilized as SAC [49]. The preparation of SACs and the support choice is not trivial, since it can promote clustering [50,51] and absorption inside the catalysts [52].

Carbon-based materials such as graphene have high surface areas and superior electrical conductivity and are normally employed as SAC supports to boost oxygen reduction reaction [53], oxygen evolution reaction [54], hydrogen evolution reaction [55], and CO2RR [56], among others, improving electrochemical activities. Graphitic carbon nitride (g-$C_3N_4$), with a graphene-like framework, contains periodic heptazine units connected via tertiary amines. The presence of nitrogen atoms in this graphene structure provides rich electron lone pairs to capture metal ions in the ligands. In fact, these electron pairs promote layer corrugation due to their electronic repulsions, although the corrugation phenomena enhance the generation of active sites for metal deposition [57]. 2D g-$C_3N_4$ is an excellent candidate for electrocatalytic $CO_2$ reduction, acting as a non-innocent support for single metal atom catalysts—mainly Cu, Pd, and Pt [58–60]. Experimental studies using $Cu_1@g$-$C_3N_4$ as a catalyst for CO2RR proved the stability of Cu single atom since the formation of Cu nanoparticles was not observed [59]. Moreover, it was found that formic acid and $H_2$ were the main products. From a theoretical point of view, the CO2RR has been studied using Cu and Au atoms supported on polymeric carbon nitride (CN) [61] and several transition metal atoms embedded on $C_2N$ [62]. Focusing on polymeric CN, authors [61] highlighted the selectivity of Cu single atom to produce $CH_4$; however, neither the competitive hydrogen evolution reaction (HER) nor the poor selectivity of Au single atom was addressed. On the other hand, the recent work by Dobrota et al. reported, by means of density functional simulations, the stability of several single metal atoms on similar carbon nitride supports, showing that Cu, Ag, and Au are stable but have lower stability compared with other transition metals [63]. Despite this, $Cu_1@g$-$C_3N_4$ and $Au_1@g$-$C_3N_4$ have been synthesized [64].

In this work, we want to explore the capability of a single Au atom supported on g-$C_3N_4$ for CO2RR. The single Au atom deposition on g-$C_3N_4$ was experimentally confirmed [64] but its catalytic activity has not been elucidated. This paper explores the reaction mechanism of the eight electron–proton transfer processes by means of periodic density functional calculations (DFT) applying the computational hydrogen electrode approach (CHE) [65].

## 2. Results

First, it is important to clarify the relevance of the monolayer corrugation. Initially, the optimized monolayer with and without the single metal atom has a flat structure. The deposition of Au single atom did not modify the planarity of the monolayer. However, the adsorption of all the moieties involved in the different pathways of CO2RR and HER process promoted surface corrugation (see Figure 1). This corrugation process is not unexpected and has been previously observed for g-$C_3N_4$ slab [52] and g-$C_3N_4$ monolayers [66,67]. According to Azofra et al. [57], corrugation minimizes the electronic repulsion of the nitrogen lone pairs located in their structural holes. From an energy point of view, the corrugated surface is around 1.2–2 eV lower in energy than the planar, including or not the transition metal single atom. Therefore, the global minimum and the reference of the monolayer's energy is the corrugated structure, while the planar is a metastable structure

that becomes corrugated after the adsorption of reactants. With respect to single-atom deposition, Au anchoring is favored by 1.91 eV. This result, together with the experimental characterization of $Au_1@g$-$C_3N_4$ [58], highlights its stability.

![](./images/885129486578745869_8.jpg)

Figure 1. Sketches of the top (up) and lateral (down) corrugated $Au_1/g$-$C_3N_4$ monolayer.

Figure 2 shows the Gibbs energy profile, considering the lowest energy pathways, while Figure 3 illustrates the sketches of all the adsorbed species of CO2RR reaction on $Au_1@g$-$C_3N_4$ and their relative Gibbs energies with respect to $CO_2$ and the $C_3N_4$ surface in the gas phase. In a previous study, we elucidated the interaction and activation of $CO_2$ molecules on $Au_1@g$-$C_3N_4$, obtaining a binding energy of $-0.22$ eV, and maintaining the linear conformation of the molecule [61]. This was in contrast to other studies where $CO_2$ was not bonded to Au single atom on 2D-carbon nitrides structure [68]. $CO_2$ bending facilitates the proton-coupled electron transfer, although Cu single atom on $g$-$C_3N_4$ was found to be active both experimentally [59] and computationally [61] for the two proton-coupled electron transfers maintaining the (almost) linear structure. Going into detail about each proton-electron transfer, the first proton-coupled electron transfer is energetically favored, independent of the formed species, with COOH (2a, see Figure 3 for labels) being slightly lower in energy than HCOO (2b) by 0.33 eV. The second proton-electron transfer has two competitive pathways involving the ejection of one water molecule and the formation of adsorbed CO on top of the Au single atom or the generation of formic acid. Our simulations predict that the formation of adsorbed CO is favored by 0.83 eV, clearly ruling out the formation of HCOOH. However, our predictions show that CO would not be detected as a product since its desorption energy is very large (1.58 eV). Therefore, the $Au_1@g$-$C_3N_4$ system can be classified into the "beyond CO" group of catalysts. The third proton-electron transfer, which implies the hydrogenation of CO, is the most energetically demanding step of the reaction since it has the largest thermodynamic barrier. This predicted barrier, at 0 V, gives the limiting potential value. It coincides with the reaction mechanism explored with Cu [38,43], where a limiting potential of $-0.74$ V is required. For the $Au_1@g$-$C_3N_4$ system, the limiting potential is $-0.69$ eV, slightly lower than the most efficient catalyst for CO2RR. It is important to mention that $CO^*$ hydrogenates toward $HCO^*$ species (4b) because the formation of $COH^*$ is 2.00 eV higher in energy (4a). The $HCO^*$ is hydrogenated to $HCOH^*$ moiety (5b) during the fourth proton-electron transfer. The thermodynamic energy barrier for this step is only 0.08 eV, whereas the formation of the $CH_2O$ moiety (5c) comes with an energetic cost of 1.15 eV. The possible formation and desorption of one water molecule (5a)

is not competitive since it implies an energy barrier larger than 3.5 eV. DFT simulations show that two moieties are close in energy for the fifth proton-coupled electron transfer. The hydrogenation of HCOH (5b) to CH₂OH (6b) and CH₃O (6c) is energetically favored, being that the formation of CH₂OH is lower in energy by 0.23 eV. A priori, this small difference makes both hydrogenation processes feasible, although one should consider that the generation of CH₃O from HCOH would involve, apart from the formation of the new C-H bond, cleavage of the O-H bond, which difficult its generation staring from HCOH species. With respect to water molecule formation (6a), this step is endergonic by more than 2 eV. The sixth proton-electron transfer is one of the most relevant steps because it may involve the generation of methanol and methane. According to our simulations, the hydrogenation of CH₂OH (6b) and/or CH₃O (6c) to CH₄ (g) is endergonic by more than 1.4 eV in the best cases (7c and 7d). Thus, the conversion of CO₂ with six protons to CH₄ is not energetically feasible. In this case, the ejection of one water molecule and the formation of CH₂* moiety (7a) is predicted as the lowest energy step with an energy barrier of 0.65 eV, followed by the production of methanol, which is 0.19 eV higher in energy (this will be discussed later). Following the lowest energy route, the next step involves the hydrogenation of CH₂* (7a) to CH₃* (8a). This process is exergonic and the previous step of CH₄ formation at the eighth electron-proton transfer. The last step is endergonic by 0.66 eV, very close to the rate-limiting step. Thus, according to our simulations, methane is the main product of CO2RR when using Au₁@g-C₃N₄ as a catalyst and applying a limiting voltage of −0.69 V that corresponds to CO hydrogenation to HCO. CO formation is predicted to be exergonic, i.e., without the requirement of a potential, although its strong binding with the Au atom is detrimental to its desorption. It is important to mention that CH₄ production is possible after eight electron-proton transfers. The same product can be generated after six electron-proton transfers starting from CH₂OH species, although our results show that the formation of one water molecule and its corresponding desorption is a much more favored process (by 1.00 eV).

![](./images/885129486578745869_9.jpg)

Figure 2. The lowest energy profile of CO2RR calculated using periodic DFT simulations using Au₁/g-C₃N₄ at 0V and a limiting potential of −0.69 V corresponding to the energy barrier of CO hydrogenation to HCO.

![](./images/885129486578745869_10.jpg)

Figure 3. Full CO2RR reaction scheme using Au₁/g-C₃N₄ at 0V. The Gibbs energy values in parentheses (eV) correspond to the relative reaction energies with respect to CO₂ (g) and the Au₁/g-C₃N₄ surface. Energies in bold and black arrows mark the lowest energy path.

A limit potential of −0.84 V is predicted for methanol production (Figure 4a). As illustrated in Figure 4, the hydrogenation of the CH₂OH moiety (6b) to methanol (7b) is possible when the limiting potential is increased, making it the rate limiting step in the reaction. This process is competitive with respect to the ejection of one water molecule. However, the process would be feasible if CH₃O (6c) is formed during the fifth proton-electron transfer. This moiety is only 0.25 eV larger in energy than CH₂OH and its generation can promote methanol production with a limit potential of −0.69 V, the same value required to hydrogenate CO to HCO* (Figure 4b). Nevertheless, as has been mentioned before, the precursor of both moieties is HCOH (5b), which is clearly the lowest energy product of the fourth hydrogenation process. Thus, the formation of CH₃O is not only a simple hydrogenation process but involves cleavage of the O-H bond and subsequent migration of the proton to the C atom. Furthermore, increasing the limiting potential will still favor ejection of the water molecule and formation of CH₂* species (7a) bonded to Au single atom. For these reasons, the generation of methanol using Au₁@g-C₃N₄ as an electrocatalyst is difficult, even if the limiting potential is increased. With respect to the formation of CH₂O (g) (5c*),

this process is endergonic and 0.55 eV higher than the formation of HCOH (5b). In this case,
the major difficulty is the generation of the adsorbed $CH_2O^*$ species that implies an energy
cost larger than 1 eV, despite the fact that its desorption is favored in energy. Therefore, the
generation of formaldehyde is excluded.

![](./images/885129486578745869_11.jpg)

Figure 4. Reaction scheme of methanol as a product of CO2RR using $Au_1/g$-$C_3N_4$ (a) considering
$CH_2OH$ intermediate and (b) considering $CH_3O$ intermediate.

Finally, it is important to compare these results with the competitive reaction, the
proton evolution to $H_2$. In this case, the binding energy of H to the Au atom is $-0.92$ eV [63].
Therefore, a very large overpotential is required for $H_2$ production, which favors the CO2RR
on $Au_1@$g-$C_3N_4$. Nevertheless, the large H-Au interaction can poison the catalytic active
site, although the binding energy of COOH/HCOO moieties, the products of the first
electron-proton transfer, and CO have higher binding energies than H. Moreover, Au
is not the preferred site for H adsorption since the interaction with monolayer carbon
atoms is higher. Thus, the monolayer would be covered by protons before binding to Au
single atom.

### 3. Conclusions
In this work, DFT simulations have been carried out to explore the capability of single
Au atom supported on g-$C_3N_4$ for CO2RR using the CHE approach. The lowest energy
pathway is $CO_2$ (g) $\rightarrow COOH^* \rightarrow CO^* \rightarrow HCO^* \rightarrow HCOH^* \rightarrow CH_2OH^* \rightarrow CH_2^* \rightarrow CH_3^*$
$\rightarrow CH_4$ (g), where the step that marks the limiting potential is the CO hydrogenation to
HCO, the third electron-proton transfer. A limiting potential of $-0.69$ V is required to over-
come this thermodynamic barrier; this is lower than the potential required for Cu metal, the

most efficient electrocatalyst for CO2RR. Our simulations predict $CH_4$ generation, where eight proton-electron transfers are required ($CO_2 + 8H^+ + 8e^- \rightarrow CH_4 + 2H_2O$). The formation of $CH_4$ using six protons ($CO_2 + 6H^+ + 6e^- \rightarrow CH_4 + H_2O + O^*$) is not feasible since the ejection of a second water molecule is preferred ($CH_2OH^* + H^+ + e^- \rightarrow CH_2^* + H_2O$). In fact, this is the key step of the catalyst's selectivity, since this water generation is slightly favored over methanol production by 0.18 eV. The high stability of the $CH_2OH^*$ moiety with respect to $CH_3O^*$ is detrimental to methanol production, where a limiting potential of $-0.84$ V is required.

In summary, applying the CHE approach, $Au_1@g$-$C_3N_4$ is predicted as a promising electrocatalyst for CO2RR, avoiding $H_2$ production due to the large overpotential required. This work encourages research on single metal atom properties for catalysis as well as the role of density functional simulations in order to shed light on the adsorption mode, coordination environment, and stability of single atom catalysts.

## 4. Computational Details and Models
The geometry of the bare monolayer, gas phase species, and the combination of both have been obtained from total energy minimization with the energy obtained from periodic DFT-based calculations carried out using the Vienna Ab initio Simulation Package (VASP) [69]. Exchange-correlation effects have been accounted for using generalized gradient approximation employing the Perdew-Burke-Ernzerhof (PBE) exchange-correlation potential [70], including the semi-empirical method of Grimme (D3) to describe the dispersion effects [71]. The valence electron wavefunctions were expanded onto a plane-wave basis set. The effect of the core electrons is considered through the projector augmented wave (PAW) method of Blöchl [72] as implemented by Kresse and Joubert [73]. The Brillouin zone was sampled by a $5 \times 5 \times 1$ grid of k-points within the Monkhorst-Pack scheme [74]. The atomic positions were relaxed until the forces were smaller than $0.01$ eV $\AA^{-1}$. The threshold for electronic relaxation was less than $10^{-5}$ eV.

The (001) monolayer of g-$C_3N_4$ is used as model ($Cmcm$ space group), the most favorable available on materials project database [75]. The monolayer contains 24 C and 32 N atoms since the cell is expanded two times in the x and y axes. The Au deposition occurs between the Nitrogen atoms, which stabilize the system. The corrugation of the surface monolayer occurs after adsorption of the reactants [64]. Thus, to obtain the minimum energy value of the surface, the corrugated monolayers were computed without reactants, obtaining almost identical corrugated geometries degenerate in energy. The binding energy of single metal atom was calculated following Equation (1),

$$
\mathrm{E}_{\mathrm{ads}}=\mathrm{E}_{\mathrm{Au} @ \mathrm{C}_{3} \mathrm{N}_{4}}-\left(\mathrm{E}_{\mathrm{C}_{3} \mathrm{N}_{4}}+\mathrm{E}_{\mathrm{Au}}\right) \tag{1}
$$

where $\mathrm{E}_{\mathrm{Au} @ \mathrm{C}_{3} \mathrm{N}_{4}}$ is the DFT energy of the monolayer including the anchored Au atom, $\mathrm{E}_{\mathrm{C}_{3} \mathrm{N}_{4}}$ is the energy of the corrugated g-$C_3N_4$ monolayer, and $\mathrm{E}_{\mathrm{Au}}$ is the energy of one Au atom in its ground state.

In this work, we have evaluated the eight possible electron-proton transfer processes, considering all the possible reaction pathways:

$$
\mathrm{CO}_{2}(\mathrm{g})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{COOH}^{*} \tag{R2a}
$$

$$
\mathrm{CO}_{2}(\mathrm{g})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{HCOO}^{*} \tag{R2b}
$$

$$
\mathrm{COOH}^{*} / \mathrm{HCOO}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{CO}^{*}+\mathrm{H}_{2} \mathrm{O}(\mathrm{g}) \tag{R3a}
$$

$$
\mathrm{CO}^{*} \rightarrow \mathrm{CO}(\mathrm{g})+^{*} \tag{R3a*}
$$

$$\mathrm{COOH^*/HCOO^* + H^+ + e^- \rightarrow HCOOH\ (g)} \tag{R3b}$$

$$\mathrm{CO^* + H^+ + e^- \rightarrow COH^*} \tag{R4a}$$

$$\mathrm{CO^* + H^+ + e^- \rightarrow HCO^*} \tag{R4b}$$

$$\mathrm{HCO^*/COH^* + H^+ + e^- \rightarrow C^* + H_2O\ (g)} \tag{R5a}$$

$$\mathrm{HCO^*/COH^* + H^+ + e^- \rightarrow HCOH^*} \tag{R5b}$$

$$\mathrm{HCO^*/COH^* + H^+ + e^- \rightarrow CH_2O^*} \tag{R5c}$$

$$\mathrm{CH_2O^* \rightarrow CH_2O\ (g)} \tag{R5c*}$$

$$\mathrm{C^+ + H^+ + e^- \rightarrow CH^*} \tag{R6a}$$

$$\mathrm{HCOH^*/CH_2O^* + H^+ + e^- \rightarrow CH^* + H_2O\ (g)} \tag{R6a*}$$

$$\mathrm{HCOH^*/CH_2O^* + H^+ + e^- \rightarrow CH_2OH^*} \tag{R6b}$$

$$\mathrm{HCOH^*/CH_2O^* + H^+ + e^- \rightarrow CH_3O^*} \tag{R6c}$$

$$\mathrm{CH^* + H^+ + e^- \rightarrow CH_2^*} \tag{R7a}$$

$$\mathrm{CH_2OH^*/CH_3O^* + H^+ + e^- \rightarrow CH_2^* + H_2O\ (g)} \tag{R7a*}$$

$$\mathrm{CH_2OH^*/CH_3O^* + H^+ + e^- \rightarrow CH_3OH\ (g)} \tag{R7b}$$

$$\mathrm{CH_2OH^*/CH_3O^* + H^+ + e^- \rightarrow CH_4\ (g) + O^*} \tag{R7cd}$$

$$\mathrm{CH_2^* + H^+ + e^- \rightarrow CH_3^*} \tag{R8a}$$

$$\mathrm{O^* + H^+ + e^- \rightarrow OH^*} \tag{R8b}$$

$$\mathrm{CH_3^* + H^+ + e^- \rightarrow CH_4\ (g)} \tag{R9a}$$

$$\mathrm{OH^* + H^+ + e^- \rightarrow H_2O\ (g)} \tag{R9b}$$

To compute the reaction energy, we have employed the computational hydrogen electrode (CHE) approach proposed by Norskov and coworkers [65]. In this protocol, the energy of $\mathrm{H^+ + e^-}$ can be computed as half of the Gibbs energy of the $\mathrm{H_2}$ molecule at 0 V vs. SHE. Therefore, the reaction energy of each step can be calculated by computing the binding energies of adsorbed moieties and the initial and final products ($\mathrm{CO_2, CO, CH_2O}$, $\mathrm{CH_3OH}$, and $\mathrm{CH_4}$) in gas phase. The vibrational frequencies have also been determined through the construction and diagonalization of the Hessian matrix, constructed by inde-

pendent displacements of atoms by $0.03\ \mathring{A}$, and it has been used to compute the zero-point energy and the entropic effects considering adsorbate moieties. Accounting for the DFT energy, entropy, and ZPE, one can evaluate the Gibbs energies of the species involved in the reaction network. The Gibbs energies can be directly related to the electrode potential by following Equation (2) as an example case for reaction 4b:

$$
\Delta \mathrm{G}_{4 \mathrm{~b}}=\Delta \mathrm{G}_{\mathrm{HCO}^{*}}-1 / 2 \Delta \mathrm{G}_{\mathrm{H} 2}-\Delta \mathrm{G}_{\mathrm{CO}^{*}}+\mathrm{eU}_{\mathrm{SHE}} \tag{2}
$$

where e is the charge of the transferred electron and U is the voltage. The limiting potential required is the electrode potential at which all the reaction steps are exergonic, without thermodynamic barrier. On the other hand, solvation effects may be relevant to stabilize some reaction intermediates owing to the H-bonding effect of water molecules [62,76], although in our previous calculations, including solvents had no remarkable differences (0.01–0.05 eV) [66] and thus all the calculations in the present study are performed without including solvent effects.

Author Contributions: Investigation, A.V.-L. and S.P.-P.; writing, review and editing, S.P.-P., M.S. and A.P. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Spanish Ministerio de Ciencia e Innovación (projects PID2021-127423NB-I00 to A.P. and PID2020-113711GB-I00 to M.S.) and the Generalitat de Catalunya (project 2021SGR0623 and ICREA Academia prize 2019 to A.P.). A.V.-L. is grateful for funding from the pre-doctoral fellowship (PRE2019-089647). S.P.-P. appreciates the economic support of the Marie Curie fellowship (H2020-MSCA-IF-2020-101020330).

Data Availability Statement: Data are deposited in the Universitat de Girona repository.

Acknowledgments: A.P. is a Serra Húnter Fellow and thanks the ICREA Academia Prize 2019. The article is in honor of Avelino Corma for the excellent contributions in the field of heterogeneous catalysis.

Conflicts of Interest: There are no conflict of interest to declare.

## References

1. Lim, L. How to make the most of carbon dioxide. *Nature* **2015**, *526*, 628–630. [CrossRef] [PubMed]
2. Intergovernmental Panel on Climate Change. *Climate Change 2013—The Physical Science Basis*, 1st ed.; Cambridge University Press: Cambridge, UK, 2014.
3. Luque-Urrutia, J.A.; Ortiz-García, T.; Solà, M.; Poater, A. Green Energy by Hydrogen Production from Water Splitting, Water Oxidation Catalysis and Acceptorless Dehydrogenative Coupling. *Inorganics* **2023**, *11*, 88. [CrossRef]
4. Poater, J.; Gimferrer, M.; Poater, A. Covalent and Ionic Capacity of MOFs To Sorb Small Gas Molecules. *Inorg. Chem.* **2018**, *57*, 6981–6990. [CrossRef] [PubMed]
5. Rajjak Shaikh, A.; Posada-Pérez, S.; Brotons-Rufes, A.; Pajski, J.J.; Kumar, G.; Mateen, A.; Poater, A.; Solà, M.; Chawla, M.; Cavallo, L. Selective absorption of $\mathrm{H}_{2} \mathrm{~S}$ and $\mathrm{CO}_{2}$ by azole based protic ionic liquids: A combined Density Functional Theory and Molecular Dynamics study. *J. Mol. Liq.* **2022**, *367*, 120558. [CrossRef]
6. Arayachukiat, S.; Yingcharoen, P.; Vummaleti, S.V.C.; Cavallo, L.; Poater, A.; D'Elia, V. Cycloaddition of $\mathrm{CO}_{2}$ to challenging N-tosyl aziridines using a halogen-free niobium complex: Catalytic activity and mechanistic insights. *Mol. Catal.* **2017**, *443*, 280–285. [CrossRef]
7. Vummaleti, S.V.C.; Nolan, S.P.; Cavallo, L.; Talarico, G.; Poater, A. Mechanism of $\mathrm{CO}_{2}$ fixation by Ir–X Bonds (X = OH, OR, N, C). *Eur. J. Inorg. Chem.* **2015**, *2015*, 4653–4657. [CrossRef]
8. Coufourier, S.; Gaignard-Gaillard, Q.; Lohier, J.-F.; Poater, A.; Gaillard, S.; Renaud, J.-L. Hydrogenation of $\mathrm{CO}_{2}$, Hydrogenocarbonate, and Carbonate to Formate in Water using Phosphine Free Bifunctional Iron Complexes. *ACS Catal.* **2020**, *10*, 2108–2116. [CrossRef]
9. Darensbourg, D.J.; Holtcamp, M.W. Catalysts for the reactions of epoxides and carbon dioxide. *Coord. Chem. Rev.* **1996**, *27*, 155–174. [CrossRef]
10. Vidal-López, A.; Posada-Pérez, S.; Solà, M.; D'Elia, V.; Poater, A. The Importance of the Bite Angle of Metal(III) Salen Catalysts in the Sequestration of CO2 with Epoxides in Mild Conditions. *Green Chem. Eng.* **2022**, *3*, 180–187. [CrossRef]
11. Aomchad, V.; Del Gobbo, S.; Yingcharoen, P.; Poater, A.; D'Elia, V. Exploring the potential of Group III salen complexes for the conversion of $\mathrm{CO}_{2}$ under ambient conditions. *Catal. Today* **2021**, *375*, 324–334. [CrossRef]
12. Natongchai, W.; Luque-Urrutia, J.A.; Phungpanya, C.; Solà, M.; D'Elia, V.; Poater, A.; Zipse, H. Cycloaddition of $\mathrm{CO}_{2}$ to epoxides by highly nucleophilic 4-aminopyridines: Establishing a relationship between carbon basicity and catalytic performance by experimental and DFT investigations. *Org. Chem. Front.* **2021**, *8*, 613–627. [CrossRef]

13. Sodpiban, O.; Del Gobbo, S.; Barman, S.; Aomchad, V.; Kidkhunthod, P.; Ould-Chikh, S.; Poater, A.; D'Elia, V.; Basset, J.-M. Synthesis of Well-defined Yttrium-based Lewis Acids by Capture of a Reaction Intermediate and Catalytic Application for cycloaddition of $CO_2$ to Epoxides Under Atmospheric Pressure. *Catal. Sci. Technol.* **2019**, 9, 6152–6165. [CrossRef]

14. Bobadilla, L.F.; Azancot, L.; Luque-Álvarez, L.A.; Torres-Sempere, G.; González-Castaño, M.; Pastor-Pérez, L.; Yu, J.; Ramírez- Reina, T.; Ivanova, S.; Centeno, M.A.; et al. Development of Power-to-X Catalytic Processes for $CO_2$ Valorisation: From the Molecular Level to the Reactor Architecture. *Chemistry* **2022**, 4, 1250–1280. [CrossRef]

15. Schäppi, R.; Rutz, D.; Dähler, F.; Muroyama, A.; Haueter, P.; Lilliestam, J.; Patt, A.; Furler, P.; Aomchad, V.; Del Gobbo, S.; et al. Drop-in fuels from sunlight and air. *Nature* **2022**, 601, 63–68. [CrossRef]

16. Preti, D.; Resta, C.; Squarcialupi, S.; Fachinetti, G. Carbon dioxide hydrogenation to formic acid by using a heterogeneous gold catalyst. *Angew. Chem. Int. Ed.* **2011**, 50, 12551–12554. [CrossRef]

17. Wang, Y.; Darensbourg, D.J. Carbon dioxide-based functional polycarbonates: Metal catalyzed copolymerization of $CO_2$ and epoxides. *Coord. Chem. Rev.* **2018**, 372, 85–100. [CrossRef]

18. Pomelli, C.S.; Tomasi, J.; Solà, M. Theoretical Study on the Thermodynamics of the Elimination of Formic Acid in the Last Step of the Hydrogenation of $CO_2$ Catalyzed by Rhodium Complexes in the Gas Phase and Supercritical $CO_2$. *Organometallics* **1998**, 17, 3164–3168. [CrossRef]

19. Italiano, C.; Llorca, J.; Pino, L.; Ferraro, M.; Antonucci, V.; Vita, A. CO and $CO_2$ methanation over Ni catalysts supported on $CeO_2$, $Al_2O_3$ and $Y_2O_3$ oxides. *Appl. Catal. B Environ.* **2020**, 264, 118494. [CrossRef]

20. Lam, E.; Noh, G.; Larmier, K.; Safonova, O.V.; Copéret, C. $CO_2$ Hydrogenation on Cu-Catalysts Generated from $Zn^{II}$ Single-Sites: Enhanced $CH_3OH$ Selectivity Compared to $Cu/ZnO/Al_2O_3$. *J. Catal.* **2021**, 394, 266–272. [CrossRef]

21. Song, X.; Yang, C.; Li, X.; Wang, Z.; Pei, C.; Zhao, Z.J.; Gong, J. On the Role of Hydroxyl Groups on $Cu/Al_2O_3$ in $CO_2$ Hydrogenation. *ACS Catal.* **2022**, 12, 14162–14172. [CrossRef]

22. Falbo, L.; Visconti, C.G.; Lietti, L.; Szanyi, J. The effect of CO on $CO_2$ methanation over $Ru/Al_2O_3$ catalysts: A combined steady-state reactivity and transient DRIFT spectroscopy study. *Appl. Catal. B Environ.* **2019**, 256, 117791. [CrossRef]

23. Yan, Y.; Wong, R.J.; Ma, Z.; Donat, F.; Xi, S.; Saqline, S.; Fan, Q.; Du, Y.; Borgna, A.; He, Q.; et al. $CO_2$ hydrogenation to methanol on tungsten-doped $Cu/CeO_2$ catalysts. *Appl. Catal. B Environ.* **2022**, 306, 121098. [CrossRef]

24. Ye, R.-P.; Liao, L.; Reina, T.R.; Liu, J.; Chevella, D.; Jin, Y.; Fan, M.; Liu, J. Engineering $Ni/SiO_2$ catalysts for enhanced $CO_2$ methanation. *Fuel* **2021**, 285, 119151. [CrossRef]

25. Gonell, F.; Puga, A.V.; Julián-López, B.; García, H.; Corma, A. Copper-doped titania photocatalysts for simultaneous reduction of $CO_2$ and production of $H_2$ from aqueous sulfide. *Appl. Catal. B Environ.* **2016**, 180, 263–270. [CrossRef]

26. Posada-Pérez, S.; Ramirez, P.J.; Gutierrez, R.A.; Stacchiola, D.J.; Viñes, F.; Liu, P.; Illas, F.; Rodriguez, J.A. The conversion of $CO_2$ to methanol on orthorhombic $\beta$-$Mo_2C$ and $Cu/\beta$-$Mo_2C$ catalysts: Mechanism for admetal induced change in the selectivity and activity. *Catal. Sci. Technol.* **2016**, 6, 6766–6777. [CrossRef]

27. Dixit, M.; Peng, X.; Porosoff, M.D.; Willauer, H.D.; Mpourmpakis, G. Elucidating the role of oxygen coverage in $CO_2$ reduction on $Mo_2C$. *Catal. Sci. Technol.* **2017**, 7, 5521–5529. [CrossRef]

28. Posada-Pérez, S.; Ramírez, P.J.; Evans, J.; Viñes, F.; Liu, P.; Illas, F.; Rodriguez, J.A. Highly active $Au/\delta$-MoC and $Cu/\delta$-MoC catalysts for the conversion of $CO_2$: The metal/C ratio as a key factor defining activity, selectivity, and stability. *J. Am. Chem. Soc.* **2016**, 138, 8269–8278. [CrossRef]

29. Rodriguez, J.A.; Ramírez, P.J.; Gutierrez, R.A. Highly Active Pt/MoC and Pt/TiC Catalysts for the Low-Temperature Water-Gas Shift Reaction: Effects of the Carbide Metal/Carbon Ratio on the Catalyst Performance. *Catal. Today* **2017**, 289, 47–52. [CrossRef]

30. Posada-Pérez, S.; Solà, M.; Poater, A. Carbon dioxide conversion on supported metal nanoparticles: A brief review. *Catalysts* **2023**, 13, 305. [CrossRef]

31. Todorova, T.K.; Schreiber, M.W.; Fontcave, M. Mechanistic understanding of $CO_2$ reduction reaction (CO2RR) toward multicarbon products by heterogeneous copper-based catalysts. *ACS Catal.* **2020**, 10, 1754–1768. [CrossRef]

32. Jiang, T.-W.; Zhou, Y.-W.; Ma, X.-Y.; Qin, X.; Li, H.; Ding, C.; Jiang, B.; Jiang, K.; Cai, W.-B. Spectrometric study of electrochemical $CO_2$ reduction on Pd and Pd-B electrodes. *ACS Catal.* **2021**, 11, 840–848. [CrossRef]

33. Mistry, H.; Choi, Y.W.; Bagger, A.; Scholten, F.; Bonifacio, C.S.; Sinev, I.; Divins, N.J.; Zegkinoglou, I.; Jeon, H.S.; Kisslinger, K.; et al. Enhanced carbon dioxide electroreduction to carbon monoxide over defect-reach plasma-activated silver catalysts. *Angew. Chem. Int. Ed.* **2017**, 56, 11394–11398. [CrossRef]

34. Clark, E.L.; Ringe, S.; Tang, M.; Walton, A.; Hahn, C.; Jaramillo, T.F.; Chan, K.; Bell, A.T. Influence of atomic surface structure on the activity of Ag for the electrochemical reduction of $CO_2$ to CO. *ACS Catal.* **2019**, 9, 4006–4014. [CrossRef]

35. Chen, Y.; Li, C.W.; Kanan, M.W. Aqueous $CO_2$ reduction at very low overpotential on oxide-derived Au nanoparticles. *J. Am. Chem. Soc.* **2012**, 134, 19969–19972. [CrossRef]

36. Mistry, H.; Reske, R.; Zeng, Z.; Zhao, Z.-J.; Greeley, J.; Strasser, P.; Roldan-Cuenya, B. Exceptional size-dependent activity enhancement in the electroreduction of $CO_2$ over Au nanoparticles. *J. Am. Chem. Soc.* **2014**, 136, 16473–16476. [CrossRef]

37. Bonin, J.; Maurin, A.; Robert, M. Molecular catalysis of the electrochemical and photochemical reduction of $CO_2$ with Fe and Co metal based complexes. Recent advances. *Coord. Chem. Rev.* **2017**, 334, 184–198. [CrossRef]

38. Rendón-Calle, A.; Builes, S.; Calle-Vallejo, F. How symmetry factors cause potential- and facet-dependent pathway shifts during $CO_2$ reduction to $CH_4$ on Cu electrodes. *Curr. Opin. Electrochem.* **2018**, 9, 158–165. [CrossRef]

39. Diaz-Morales, O.; Ledezma-Yanez, I.; Koper, M.T.M.; Calle-Vallejo, F. Guidelines for the Rational Design of Ni-Based Double Hydroxide Electrocatalysts for the Oxygen Evolution Reaction. *ACS Catal.* 2015, 9, 5380-5387. [CrossRef]

40. Rendón-Calle, A.; Low, Q.H.; Hong, S.H.L.; Builes, S.; Yao, B.S.; Calle-Vallejo, F. A brief review of the computational modeling of CO₂ electroreduction on Cu electrodes. *Appl. Catal.* 2021, 285, 119776. [CrossRef]

41. Reske, R.; Mistry, H.; Behafarid, F.; Roldan-Cuenya, B.; Strasser, P. Particle size effects in the catalytic electroreduction of CO₂ on Cu nanoparticles. *J. Am. Chem. Soc.* 2014, 136, 6978-6986. [CrossRef]

42. Woldu, A.R.; Huang, Z.; Zhao, P.; Hu, L.; Astruc, D. Electrochemical CO₂ reduction (CO₂RR) to multi-carbon products over copper-based catalysts. *Coord. Chem. Rev.* 2022, 454, 214340. [CrossRef]

43. Peterson, A.A.; Abild-Pedersen, F.; Studt, F.; Rossmeisl, J.; Nørskov, J.K. How copper catalyzes the electroreduction of carbon dioxide into hydrocarbon fuels. *Energy Environ. Sci.* 2010, 3, 1311-1315. [CrossRef]

44. Nie, X.; Luo, W.; Janik, M.J.; Asthagiri, A. Reaction mechanisms of CO₂ electrochemical reduction on Cu(1 1 1) determined with density functional theory. *J. Catal.* 2014, 312, 108-122. [CrossRef]

45. Kuhl, K.P.; Cave, E.R.; Abram, D.N.; Jaramillo, T.F. New insights into the electrochemical reduction of carbon dioxide on metallic copper surfaces. *Energy Environ. Sci.* 2012, 5, 7050-7059. [CrossRef]

46. Goodpaster, J.D.; Bell, A.T.; Head-Gordon, M. Identification of Possible Pathways for C-C Bond Formation during Electrochemical Reduction of CO₂: New Theoretical Insights from an Improved Electrochemical Model. *J. Phys. Chem. Lett.* 2016, 7, 1471-1477. [CrossRef]

47. Datye, A.K.; Guo, H. Single atom catalysis poised to transition from an academic curiosity to an industrially relevant technology. *Nat. Commun.* 2021, 12, 895. [CrossRef]

48. Liu, L.; Corma, A. Metal catalysts for heterogeneous catalysis: From single atoms to nanoclusters and nanoparticles. *Chem. Rev.* 2018, 118, 4981-5079. [CrossRef]

49. Basset, J.M.; Baudouin, A.; Bayard, F.; Candy, J.-P.; Copéret, C.; De Mallmann, A.; Godard, G.; Kuntz, E.; Lefebvre, F.; Lucas, C.; et al. *Modern Surface Organometallic Chemistry*; Wiley-VCH Verlag GmbH & Co. KGaA: Weinheim, Germany, 2009; pp. 23-73.

50. Rivera-Cárcamo, C.; Serp, P. Single atom catalysts on carbon-based materials. *ChemCatChem* 2018, 10, 5058-5091. [CrossRef]

51. Xu, Y.-T.; Xie, M.-Y.; Zhong, H.; Cao, Y. In situ clustering of single-atom copper precatalysts in a metal-organic framework for efficient electrocatalytic nitrate-to-ammonia reduction. *ACS Catal.* 2022, 12, 8698-8706. [CrossRef]

52. Jurado, L.; Esvan, J.; Luque-Álvarez, L.A.; Bobadilla, L.F.; Odriozola, J.A.; Posada-Pérez, S.; Poater, A.; Comas-Vives, A.; Axet, M.R. Highly dispersed Rh single atoms over graphitic carbon nitride as a robust catalyst for the hydroformylation reaction. *Catal. Sci. Technol.* 2023, 13, 1425-1436. [CrossRef]

53. Wang, Y.; Li, Q.; Zhang, L.c.; Wu, Y.; Chen, H.; Li, T.; Xu, M.; Bao, S.-J. A gel-limiting strategy for large-scale fabrication of Fe-N-C single-atom ORR catalysts. *J. Mater. Chem. A* 2021, 9, 7137-7142. [CrossRef]

54. Ying, Y.; Fan, K.; Luo, X.; Qiao, J.; Huang, H. Unravelling the origin of bifunctional OER/ORR activity for single-atom catalysts supported on C₂N by DFT and machine learning. *J. Mater. Chem. A* 2021, 9, 16860-16867. [CrossRef]

55. Zeng, L.; Dai, C.; Liu, B.; Xue, C. Oxygen-assisted stabilization of single-atom Au during photocatalytic hydrogen evolution. *J. Mater. Chem. A* 2019, 7, 24217-24221. [CrossRef]

56. Li, M.; Wang, H.; Luo, W.; Sherrell, P.C.; Chen, J.; Yang, J. Heterogeneous single-atom catalysts for electrochemical CO₂ reduction reaction. *Adv. Mater.* 2020, 32, e2001848. [CrossRef]

57. Azofra, L.M.; MacFarlane, D.R.; Sun, C. A DFT study of planar vs. corrugated graphene-like carbon nitride (g-C₃N₄) and its role in the catalytic performance of CO₂ conversion. *Phys. Chem. Chem. Phys.* 2016, 18, 18507-18514. [CrossRef]

58. Gao, G.; Jiao, Y.; Waclawik, E.; Du, A. Single Atom (Pd/Pt) Supported on Graphitic Carbon Nitride as an Efficient Photocatalyst for Visible-Light Reduction of Carbon Dioxide. *J. Am. Chem. Soc.* 2016, 138, 6292-6297. [CrossRef]

59. Cometto, C.; Ugolotti, A.; Grazietti, E.; Moretto, A.; Bottaro, G.; Armelao, L.; Di Valentin, C.; Calvillo, L.; Granozzi, G. Copper single-atoms embedded in 2D graphitic carbon nitride for the CO₂ reduction. *npj 2D Mater. Appl.* 2021, 5, 63. [CrossRef]

60. Peng, Y.; Lu, B.; Chen, S. Carbon-Supported Single Atom Catalysts for Electrochemical Energy Conversion and Storage. *Adv. Mater.* 2018, 30, 1801995. [CrossRef]

61. Li, J.; Yan, O.; Li, K.; You, J.; Wang, H.; Cui, W.; Cen, W.; Chu, Y.; Dong, F. Cu supported on polymeric carbon nitride for selective CO₂ reduction into CH₄: A combined kinetic and thermodynamics investigation. *J. Mater. Chem. A* 2019, 7, 17014-17021. [CrossRef]

62. Liu, H.; Huang, Q.; An, W.; Wang, Y.; Men, Y.; Liu, S. Dual-atom active sites embedded in two-dimensional C₂N for efficient CO₂ electroreduction: A computational study. *J. Energy Chem.* 2021, 61, 507-516. [CrossRef]

63. Dbrota, A.S.; Skorodumova, N.V.; Mentus, S.V.; Pašti, I.A. Surface Pourbaix plots of M@N4-graphene single-atom electrocatalysts from density functional theory thermodynamic modeling. *Electrochim. Acta* 2022, 412, 140155. [CrossRef]

64. Yu, J.; Chen, C.; Zhang, Q.; Lin, J.; Yang, X.; Gu, L.; Zhang, H.; Liu, Z.; Wang, Y.; Zhang, S.; et al. Au Atoms Anchored on Amorphous C₃N₄ for Single-Site Raman Enhancement. *J. Am. Chem. Soc.* 2022, 144, 21908-21915. [CrossRef] [PubMed]

65. Nørskov, J.K.; Rossmeisl, J.; Logadottir, A.; Lindqvist, L.; Kitchin, J.R.; Bligaard, T.; Jónsson, H. Origin of the Overpotential for Oxygen Reduction at a Fuel-Cell Cathode. *J. Phys. Chem. B* 2004, 108, 17886-17892. [CrossRef]

66. Posada-Pérez, S.; Vidal-López, A.; Solà, M.; Poater, A. 2D carbon nitride as a support with single Cu, Ag, and Au atoms for carbon dioxide reduction reaction. *Phys. Chem. Chem. Phys.* 2023, 25, 8574-8582. [CrossRef]

67. Zhao, X.; Wang, L.; Pei, Y. Single metal atom catalysts supported on g-C₃N₄ for formic acid dehydrogenation: A combining density functional theory and machine learning study. J. Phys. Chem. C 2021, 125, 22513-22521. [CrossRef]

68. Cui, X.; An, W.; Liu, X.; Wang, H.; Men, Y.; Wang, J. C₂N-graphene supported single-atom catalysts for CO₂ electrochemical reduction reaction: Mechanistic insight and catalysts screening. Nanoscale 2018, 10, 15262-15272. [CrossRef]

69. Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. Phys. Rev. B Condens. Matter Mater. Phys. 1996, 54, 11169-11186. [CrossRef]

70. Perdew, J.P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865-3868. [CrossRef]

71. Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate ab Initio Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. J. Chem. Phys. 2010, 132, 154104-154119. [CrossRef]

72. Blöchl, P.E. Projector Augmented-Wave Method. Phys. Rev. B 1994, 50, 17953-17979. [CrossRef]

73. Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. Phys. Rev. B 1999, 59, 1758-1775. [CrossRef]

74. Wisesa, P.; McGill, K.; Mueller, T. Efficient generation of generalized Monkhorst-Pack grids through the use of informatics. Phys. Rev. B 2016, 93, 155109. [CrossRef]

75. Jain, A.; Ong, S.P.; Hautier, G.; Chen, W.; Richards, W.D.; Dacek, S.; Cholia, S.; Gunter, D.; Skinner, D.; Ceder, G.; et al. Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. APL Mater. 2013, 1, 011002. [CrossRef]

76. Feng, Y.; An, W.; Wang, Z.; Wang, Y.; Men, Y.; Du, Y. Electrochemical CO₂ reduction reaction on M@Cu(211) bimetallic single-atom surface alloys: Mechanism, kinetics, and catalyst screening. ACS Sustain. Chem. Eng. 2020, 8, 210-222. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.