Energy &
Environmental
Science

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: S. Kim, M. Aykol,
V. I. Hegde, Z. Lu, S. Kirklin, J. Croy, M. M. Thackeray and C. M. Wolverton, Energy Environ. Sci., 2017,
DOI: 10.1039/C7EE01782K.

![](./images/813105271441195008_1.jpg)

This is an Accepted Manuscript, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after
acceptance, before technical editing, formatting and proof reading.
Using this free service, authors can make their results available
to the community, in citable form, before we publish the edited
article. We will replace this Accepted Manuscript with the edited
and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the
author guidelines.

Please note that technical editing may introduce minor changes
to the text and/or graphics, which may alter content. The journal's
standard Terms & Conditions and the ethical guidelines, outlined
in our author and reviewer resource centre, still apply. In no
event shall the Royal Society of Chemistry be held responsible
for any errors or omissions in this Accepted Manuscript or any
consequences arising from the use of any information it contains.

![](./images/813105271441195008_2.jpg)

rsc.lí/ees

# Materials Design of High-Capacity Li-rich Layered-Oxide Electrodes:
$Li_2MnO_3$ and Beyond†

Soo Kim, $^{a \parallel}$ Muratahan Aykol, $^{az \parallel}$ Vinay I. Hegde, $^{a \parallel}$ Zhi Lu, $^{a}$ Scott Kirklin, $^{a}$
Jason R. Croy, $^{b}$ Michael M. Thackeray, $^{b}$ and Chris Wolverton*a

$^{a}$ Department of Materials Science and Engineering, Northwestern University,
2220 Campus Drive, Evanston, Illinois 60208, United States

$^{b}$ Chemical Sciences and Engineering Division, Argonne National Laboratory,
9700 South Cass Avenue, Argonne, Illinois 60439, United States

$^{z}$ Current Address: Toyota Research Institute,
4440 El Camino Real, Los Altos, California 94022, United States

*Correspondence: c-wolverton@northwestern.edu

$^{\parallel}$ These authors equally contributed to this work.

## Broader Context

Finding new battery electrode materials that can improve the current state-of-the-art Li-ion technologies will have an immediate impact on the energy industry, environment, and conservation of natural resources. Designing new high-energy Li-rich layered oxides with functionalities aiming at suppressing the structural instabilities, such as metal migration, phase transitions, and the tendency of the delithiated electrodes to lose oxygen during charge can effectively address this challenge. However, the relation between the structure and functionality of a material is very complex, and therefore experimental discovery and optimization process often consume significant time and resources. To accelerate this process, here we have carried out a multi-faceted high-throughput density functional theory screening study to narrow down the list of thousands of candidate composite electrodes to a handful

that are the most likely to be synthesized. We ultimately present our top 30 active/inactive pair cathode composite systems by exploiting the properties with respect to their operating voltage, stability against oxygen loss and metal-migration, and the formation of solid-solution and/or coherent nanocomposite.

## Abstract
Lithium-ion batteries (LIBs) have been used widely in portable electronics, hybrid-electric and all-electric vehicles for many years. However, there is a growing need to develop new cathode materials that will provide higher cell energy densities for advanced applications. Several candidates, including $Li_2MnO_3$-stabilized $LiM'O_2$ ($M' = Mn/Ni/Co$) structures, $Li_2Ru_{0.75}Sn_{0.25}O_3$ (i.e., $3Li_2RuO_3$-$Li_2SnO_3$), and disordered $Li_2MoO_3$-$LiCrO_2$ compounds can yield capacities exceeding $200$ mAh g$^{-1}$, alluding to the constructive role that $Li_2MO_3$ ($M^{4+}$) end-member compounds play in the electrochemistry of these systems. Here, we catalog the family of $Li_2MO_3$ compounds as active cathodes or inactive stabilizing agents using high-throughput density functional theory (HT-DFT). With an exhaustive search based on design rules that include phase stability, cell potential, resistance to oxygen evolution, and metal migration, we predict a number of new $Li_2M_IO_3$-$Li_2M_{II}O_3$ active/inactive electrode pairs, in which $M_I$ and $M_{II}$ are transition- or post-transition metal ions, that can be tested experimentally for high-energy-density LIBs.

## 1. Introduction
$xLi_2MnO_3$·$(1$-$x)LiM'O_2$ cathodes, in which $Li_2MnO_3$ can serve as a stabilizing agent when lithium-ion cells are charged below $4.4$ V vs. $Li/Li^+$ or as a reservoir for excess lithium when charged above $4.4$ V, can deliver substantial electrochemical capacity.$^{1}$ The exact role of the $Li_2MnO_3$-like regions has been a subject of debate,$^{1,2}$ which can be attributed to the

challenges of analyzing complex structures, quantifying oxygen activity/loss, and measuring associated metal-migration tendencies during electrochemical operation. $^{1-5}$ Even after intense scientific research on these cathode materials, $^{1-10}$ many technological challenges still remain. Problems of *i*) voltage fade on cycling, $^{5}$ *ii*) hysteresis during charge/discharge, $^{9}$ *iii*) metal-migration within the oxide structure, $^{10}$ *iv*) slow rate-capability, $^{1,3,4}$ and *v*) gas evolution $^{3}$ must still be overcome before these $Li_2MnO_3$-based cathodes become commercially-viable.

The concept of incorporating a $Li_2MnO_3$ component into a conventional layered $LiM'O_2$ structure has received substantial attention to date. $^{1,4,6-9}$ More recently, there has also been a greatly increasing interest in using high-capacity $Li_2MO_3$-type structures, apart from $Li_2MnO_3,^{11-13}$ alone as a cathode. $^{14-24}$ For example, $Li_2Ru_{1-y}M_yO_3$ ($M = Mn/Sn$) $^{14-16}$ electrodes yield a capacity exceeding 220 mAh g$^{-1}$ with significantly reduced fade of the cell voltage relative to $Li_2MnO_3$. $Li_2Ru_{0.75}Sn_{0.25}O_3$ (*i.e.*, $3Li_2RuO_3$-$Li_2SnO_3$) shows superior voltage and capacity retention compared to $Li_2RuO_3$ and $Li_2Ru_{0.75}Ti_{0.25}O_3$ (*i.e.*, $3Li_2RuO_3$-$Li_2TiO_3$), $^{15,17}$ in which $Li_2SnO_3$ and $Li_2TiO_3$ act as stabilizers, respectively, similar to structurally-integrated $Li_2MO_3$-$LiM'O_2$ materials. $^{1,25}$ In another report, $Li_2Ru_{0.75}Ti_{0.25}O_3$ facilitates better $Li^+$ diffusion, while $Li_2Ru_{0.75}Sn_{0.25}O_3$ suffers from stacking-faults that block diffusion pathways. $^{18}$ Moreover, it has been reported that disordered $Li_2MoO_3$ electrode structures can deliver high capacities. $^{19}$ Although reversible Mo migration and $Mo^{4+/6+}$ redox reactions occur in $Li_2MoO_3$, the surface of the electrode particles decomposes to $Li_2MoO_4$ and $MoO_3$ if exposed to air. $^{20,21}$ In addition, recent studies have shown that the electrochemical reactions of $Li_2IrO_3$, $Li_2Ru_{1-x}IrO_3$, and $Li_2Ir_{0.75}Sn_{0.25}O_3$ cathodes involve both cationic and anionic redox processes. $^{22-24}$

The current understanding of $Li_2MO_3$-based cathodes is that, while reversible oxygen redox reactions can contribute to additional capacity, they may also be responsible for metal-

migration within the anionic oxide array and oxygen loss, both of which are detrimental to the electrochemical performance of a $Li/Li_2MO_3$ cell. Composite $Li_2M_IO_3$-$Li_2M_{II}O_3$ cathodes, in which $M_I$ and $M_{II}$ are transition- or post-transition metal ions, and where redox activities can be tuned by the relative amounts and voltages of the active/inactive components, provide a potential pathway to mitigate such problems. The judicious design of such composite electrode pairs requires a knowledge, not only of their thermodynamic stability at various states of charge, *i.e.*, the cell voltage, but also structural instabilities, such as metal migration, phase transitions, and the tendency of the delithiated electrodes to lose oxygen during charge. Clearly, a systematic survey of these parameters that control the electrochemical performance of $Li_2MO_3$ electrodes is essential for identifying new materials with inherently superior structural and electrochemical properties. A powerful tool to carry out such a detailed survey with high-fidelity is high-throughput density functional theory (HT-DFT),$^{26-36}$ which has been successfully used to predict new battery materials such as anodes,$^{28}$ cathodes$^{29,30}$, electrolytes,$^{31}$ and coatings$^{32,36}$. Identifying new, thermodynamically-stable $Li_2MO_3$ compounds and understanding their electrochemical properties with a HT-DFT strategy can, therefore, unlock potential opportunities for advancing LIB materials technologies.

In this paper, we perform a multi-faceted HT-DFT screening study of single- and mixed-metal $Li_2MO_3$ and $Li_2M_IO_3$-$Li_2M_{II}O_3$ compounds, and identify promising new candidate cathodes. We begin by identifying all of the thermodynamically-stable $Li_2MO_3$ (M = Ti, V, Cr, Mn, Fe, Co, Ni, Ge, Zr, Mo, Ru, Rh, Pd, Sn, Hf, Os, Ir, Pt, and Pb) Li-rich, layered oxides. We systematically calculate the delithiation voltage windows and determine the tendencies for oxygen evolution and structural transformation for each material. Building on this information, we introduce a classification scheme that differentiates end-member $Li_2MO_3$ compounds as active cathodes and/or inactive stabilizers within integrated cathode structures.

We use our results to propose a list of end-member cathode pairs that offer structural stability at high potentials, favorable metal-mixing behavior, coherent interfaces, and high electrochemical capacity (and cell energy density). In particular, our theoretical studies predict several new active-inactive composite pairs with a higher specific capacity than $\mathrm{Li_2Ru_{1-y}MyO_3}$ (M = Mn/Sn/Ti) and $\mathrm{Li_2Ir_{1-x}Sn_xO_3;^{14-18,24}}$ and help elucidate trends and directions for designing layered-oxide electrodes for high energy LIBs.

## 2. Methods

### 2.1. Structure analysis
We perform HT-DFT calculations of $\mathrm{Li_2MO_3}$ (M = all 73 metals and metalloids in the periodic table that have PAW potentials available in the Vienna Ab initio Simulation Package$^{37-39}$) compounds in the layered $C2/m$ structure [see Electronic Supplementary Information (ESI)$\dagger$, Section S1], within the high-throughput framework of the Open Quantum Materials Database (OQMD).$^{33,34}$

(i) *Formation energy*: The formation energy of a generic $\mathrm{Li_2MO_3}$ compound, $\Delta H_f$, is defined as follows: $\Delta H_f(\mathrm{Li_2MO_3}) = E(\mathrm{Li_2MO_3}) - 2\mu_{\mathrm{Li}} - \mu_{\mathrm{M}} - 3\mu_{\mathrm{O}}$, where $E(\mathrm{Li_2MO_3})$ is the total energy of the compound calculated using DFT (Section S1$\dagger$), and $\mu_i$ ($i$ = Li, M, O) is the chemical potential of the component $i$. We use chemical potentials fitted to experimental formation energies from the SGTE substances database (SSUB)$^{40}$ in the case of elements that are gaseous or liquid, or those that exhibit solid-solid phase transformations below room temperature. We further add corrections to the reference chemical potentials of all species for which we use GGA+$U$ using the fitted elemental reference energies (FERE) method.$^{41-43}$ For all other elements, the reference chemical potentials are simply the total energies calculated

using DFT. The rationale behind, and the details of, the fitting of chemical potentials are beyond the scope of this work, and can be found elsewhere.³⁴

(ii) Thermodynamic stability: For all systems considered in our study, we plot the formation energies of all compounds in the OQMD³³,³⁴ in that phase space against their composition. The so-called convex-hull is then defined as the envelope connecting the lowest energy compounds at every composition in that phase space. The thermodynamic stability of a compound, $\Delta H_s^i$, is then given by: $\Delta H_s^i = \Delta H_f^i - E_{hull}^i$, where $\Delta H_f^i$ is the formation energy of the compound $i$, and $E_{hull}^i$ is the energy at that composition of a convex-hull constructed without the compound $i$. Therefore, "stable" compounds, by definition, lie on the convex-hull and have a stability $\Delta H_s^i \leq 0$ meV/atom (i.e., here, a stable compound would have a 'negative' convex-hull distance – evaluated excluding the Li₂MO₃ compound). We term the compounds above and close to the convex-hull ($\Delta H_s^i \leq \sim25$ meV/atom, i.e., $k_BT$ at room temperature) "nearly-stable". All other compounds further beyond the convex hull are "unstable", as they are likely to decompose into a combination of other compounds in that phase space. The OQMD³³,³⁴ contains most of the unique ordered compounds experimentally reported in the Inorganic Crystal Structure Database (ICSD) and hypothetical compounds based on decorations of commonly occurring crystal structures types, a total of more than 450,000 compounds. Although it provides one of the most extensive descriptions of the energetic landscapes of the Li-M-O systems considered in this study, the calculated thermodynamic stability of a phase depends on the completeness of the database used, and thus may change when the database grows with the addition of new structures.

(iii) Critical oxygen chemical potential: We calculate the range of oxygen chemical potential over which an Li₂MO₃ compound is competitive on the convex-hull, and thus thermodynamically-stable (at $T=0$ K) in equilibrium with O₂, with respect to all other phases

in the OQMD.⁽³³,³⁴⁾ In addition, we convert a change in the oxygen chemical potential per mole of oxygen into the more accessible temperature-scale using the following equation:

$$\Delta\mu_0(T-T_0)=\Delta H_0^{exp}(T-T_0)-T\Delta S_0^{exp}(T-T_0)+RT\ln(p_{O_2}/p_{tot})$$

where changes in enthalpy and entropy with temperature, $\Delta H_0^{exp}(T-T_0)$ and $\Delta S_0^{exp}(T-T_0)$, are obtained from JANAF experimental thermochemical tables,⁴⁴ and the partial pressure of oxygen gas at room temperature and pressure, $p_{O_2}=0.21\ p_{tot}$. The critical chemical potential window thus represents the stability of the compound in equilibrium with O₂.⁽⁴⁵,⁴⁶⁾

(iv) Cell voltage: We calculate the cell voltage, $V_{cell}$ (vs. Li⁺/Li), associated with a delithiation reaction using the equation: $V_{cell}=-\frac{\Delta G_{reaction}}{F\cdot\delta n_e}$, where $\Delta G_{reaction}$ is the molar change in the free energy for the reaction, $F$ is the Faraday constant, and $\delta n_e$ is the number of electrons removed/added in the reaction. Here, we assume that the change in entropy associated with the phases in the delithiation reaction is negligible.

(v) Oxygen vacancy formation energy: The dilute vacancy formation energy per oxygen vacancy, $\Delta E_O^{vac}$, of an Li₂₋ₓMO₃ compound is given by the equation: $\Delta E_O^{vac}(\text{Li}_{2-x}\text{MO}_3)=[E(\text{Li}_{2-x}\text{MO}_{3-\delta})+\delta\cdot\mu_0]-E(\text{Li}_{2-x}\text{MO}_3)$, where $E(\text{Li}_{2-x}\text{MO}_3)$ is the total energy of the pristine (with no oxygen vacancies) compound, $E(\text{Li}_{2-x}\text{MO}_{3-\delta})$ is the total energy of the compound with $\delta$ oxygen vacancies per formula unit, and $\mu_0$ is the reference chemical potential of oxygen. We use a $2\times1\times1$ supercell (with four Li₂₋ₓMO₃ formula units) to simulate dilute oxygen vacancy formation conditions and to mitigate the interaction between periodic images of the vacancy (see Section S1†). In addition, we have identified the lowest energy, i.e., most favorable, oxygen vacancy within the supercell. While we have only evaluated the oxygen vacancy formation in 'ideal' bulk phase in this work to avoid additional complexity and simple interpretation, it may be also possible that some defect complex or

other structure (e.g., spinel-like) having lower energy could form, being coupled with the delithiation process and metal migration.

(vi) Metal-migration tendency: We calculate the thermodynamic driving force, in a delithiated $Li_{2-x}MO_{3-\delta}$ structure (with and without oxygen vacancies), for the migration of the transition metal atom ($TM$) to a nearby Li vacancy, $\Delta E_{TM}^{mig}=E^{mms}(Li_{2-x}MO_{3-\delta})-E^{ps}(Li_{2-x}MO_{3-\delta})$, where $E^{mms}$and $E^{ps}$ refer to the total energies of the $Li_{2-x}MO_{3-\delta}$ compound after and before the $TM$ has migrated into a nearby Li vacancy. Since the migration of the $TM$ produces relatively large distortions if a single unitcell is used, we use a $2 \times 1 \times 1$ supercell, with four $Li_{2-x}MO_{3}$ formula units, so that a layered structure is largely maintained before and after the $TM$ migration (see Section S1$\dagger$).

(vii) Mixing energy: We estimate the tendency of two single layered cathode materials, $Li_{2}M'O_{3}$ and $Li_{2}M''O_{3}$, to "mix" to form a layered $Li_{2}M'_{0.5}M''_{0.5}O_{3}$ structure (all belonging to the $C2/m$ space group), by calculating the mixing energy, $\Delta E^{mix}(M',M'')$, with the following equation: $\Delta E^{mix}(M',M'')=E(Li_{2}M'_{0.5}M''_{0.5}O_{3})-\frac{1}{2}[E(Li_{2}M'O_{3})+E(Li_{2}M''O_{3})]$, where $E(Li_{2}M'_{0.5}M''_{0.5}O_{3})$ and $E(Li_{2}MO_{3}),(M=M',M'')$ are the energies of the $C2/m$ structure with the two symmetrically identical $TM$ sites in the unitcell occupied by two different metal atoms M' and M'', and completely by either M' alone or M'' alone, respectively (see Section S1$\dagger$). Depending on $\Delta E^{mix}(M',M'')$, we can estimate the metal order/disorder nature within the layered oxide. Please note that the mixing enthalpy is calculated with fixed $Li_{2}MO_{3}$ $(M^{4+})$ symmetry in this work; and therefore, it may overestimate $\Delta E^{mix}$ as some of the cation mixtures may form a different ordering or oxidation state (e.g., $Mo^{4+} \rightarrow Mo^{6+}$, if coupled with $Ni^{4+} \rightarrow Ni^{2+}$).


### 2.2. Cathode classification

We have carefully considered several properties calculated from the abovementioned procedures that govern the feasibility of a compound to be used either as an active cathode or an inactive stabilizer material in a battery.

(i) **Active $Li_2MO_3$ cathode**: An active $Li_2MO_3$ cathode is expected to possess a wide voltage window and to be resistant against oxygen evolution and metal migration.

(ii) **Inactive $Li_2MO_3$ stabilizer**: All remaining $Li_2MO_3$ compounds are categorized as an inactive $Li_2MO_3$ stabilizer. Preferably, these $Li_2MO_3$ compounds behave as a structural stabilizer by remaining inactive until very high voltages. It is crucial that the inactive $Li_2MO_3$ component is not charged too high to avoid severe phase transformations. Inactive $Li_2MO_3$ that can tolerate oxygen evolution and metal migration may be further activated. Here, we use the lowest voltage of delithiation in the inactive $Li_2MO_3$ stabilizer as the voltage cutoff for the active/inactive composite cathode system (i.e., we rely on the redox capacity from the active $Li_2MO_3$ component and will not activate the inactive component).

(iii) **Both active/inactive $Li_2MO_3$**: Depending on the characteristic of the other $Li_2MO_3$ component (i.e., voltage window), a few $Li_2MO_3$ compound can act as either an active cathode or an inactive stabilizer.

(iv) **Cathode pair assignment**: A favorable metal mixing (<25 meV/site) and a small lattice mismatch (<0.5 Å) are obligatory for both active/active and active/inactive cathode pairs. We also evaluate whether the pair cathode materials are thermodynamically stable or nearly-stable *vs.* quaternary Li-Mᵢ-Mᵢᵢ-O chemical space within the OQMD³³ˡ³⁴ (i.e., on or close to the convex-hull; $\Delta H_s^i \leq \sim$25 meV/atom). The active/active pairs must share a voltage overlap. An inactive $Li_2MO_3$ can be chosen to be a structural stabilizer for an active $Li_2MO_3$ component to be categorized as the active/inactive composite pairs.

(v) Choosing the top 30 $Li_2M_I O_3$-$Li_2M_{II}O_3$ active/inactive pair cathode candidates: We evaluate the gravimetric energy density of all $Li_2M_I O_3$-$Li_2M_{II}O_3$ active/inactive pairs (ESI$\dagger$).

We exclude ordered $Li_4M_I M_{II}O_6$ compounds from the final evaluations. Here, we define the gravimetric energy density as the product of average voltage and capacity of the $Li_2M_I O_3$-
$Li_2M_{II}O_3$ active/inactive composite system. For further discussions, see Section S3 (ESI$\dagger$).

## 3. Results and Discussion
### 3.1. Stability and Synthesis Conditions for $Li_2MO_3$ Compounds
We first execute a HT-search for thermodynamically-stable, Li-rich, layered $Li_2MO_3$ compounds that are isostructural with layered $Li_2MnO_3$ ($C2/m$) by substituting all possible elements in the periodic table for M within the Open Quantum Materials Database (OQMD) framework. $^{33,34}$ By evaluating the stabilities of these compounds against all other materials that currently exist in the OQMD (>450,000), $^{33,34}$ we find 15 of them to be stable (on the convex-hull) and 4 of them to be nearly-stable (within ~25 meV/atom of the convex-hull; see Fig. 1a and Table S1$\dagger$).

In our best of our knowledge, a total of 15 $Li_2MO_3$ (M = Ti, V, Mn, Fe, Ni, Ge, Zr, Mo, Ru, Rh, Pd, Sn, Ir, Pt, and Pb) compounds have been observed experimentally over the years. In all fifteen cases (*i.e.*, with zero "errors" in the screening strategy), our DFT stability metric correctly identifies these compounds as stable or within ~25 meV/atom (roughly $kT$ at 300 K) of the stable convex hull. Here, we recover *all* of the $Li_2MO_3$ materials that have been examined as a cathode or a stabilizer for LIB applications, including $Li_2TiO_3$, $Li_2VO_3$, $Li_2MnO_3$, $Li_2GeO_3$, $Li_2ZrO_3$, $Li_2MoO_3$, $Li_2RuO_3$, $Li_2SnO_3$, $Li_2IrO_3$, and $Li_2PtO_3$. $^{1-25,47-49}$ In addition, we find several stable and nearly-stable $Li_2MO_3$ materials that have not been exploited for battery applications, such as $Li_2CrO_3$, $Li_2FeO_3$, $^{50-53}$ $Li_2CoO_3$, $Li_2NiO_3$, $^{54}$ $Li_2RhO_3$, $^{55}$ $Li_2PdO_3$, $^{56}$ $Li_2HfO_3$, $Li_2OsO_3$, and $Li_2PbO_3$, $^{57}$ which might have varying degrees

of practical vs. purely scientific interest, primarily because of cost or toxicity reasons. We have marked the experimentally-known $C2/m$ or $C2/c$ $Li_2MO_3$ compounds, observed polymorphs (i.e., $Li_2VO_3$, $Li_2GeO_3$, and $Li_2ZrO_3$)²⁵,⁴⁷,⁴⁸, and $Li_2MO_3$ without reported crystal structure (i.e., $Li_2FeO_3$)⁵⁰⁻⁵³ in Fig. 1a, as well as the newly-discovered compounds in this work (see Section S2 in ESI† for further discussion).

To ascertain whether oxidizing or reducing conditions (high or low oxygen chemical potential, respectively) are favorable for synthesizing a given compound, we present the oxygen chemical potential windows for stable and nearly-stable $Li_2MO_3$ compounds (Fig. 1b and Fig. S1†). Outside these critical oxygen chemical potential windows indicated by the blue region in Fig. 1b, $Li_2MO_3$ becomes unstable relative to other Li-M-O compositions and structures (in equilibrium with $O_2$). The temperature-scale in Fig. 1b, which relates to atmospheric-air conditions ($p_{O_2}=0.21$ atm), shows the optimal heat-treatment temperatures for the synthesis of $Li_2MO_3$ compounds. For example, the synthesis of $Li_2NiO_3$ is predicted to require lower temperatures and more strongly oxidizing conditions (i.e., completely consistent with Ref. 54), than those required to synthesize $Li_2CrO_3$. We also observe that $Li_2CrO_3$, $Li_2FeO_3$, $Li_2NiO_3$, and $Li_2OsO_3$ have relatively narrow temperature windows (Fig. 1b), and consequently, may be more extremely tough to stabilize than $Li_2MO_3$ compounds with wider windows (see Fig. S1†). Interestingly, $C2/m$ $Li_2FeO_3$ was found to be a stable compound ($T=0$ K), consistent with the stability of tetravalent iron in organometallic complexes⁵⁸,⁵⁹ and in charged $Li_{4-x}FeSbO_6$⁶⁰,⁶¹ and $Li_{5-x}FeO_4$ electrodes⁶²,⁶³. Teixeira et al.⁵⁰,⁵¹ have previously detected the presence of $Li_2FeO_3$ phase, while Kokarovtseva et al.⁵² reported that $Li_2FeO_3$ was synthesized but decomposed in water with the contact with $O_2$. We identify $Li_2VO_3$, $Li_2GeO_3$, $Li_2ZrO_3$, and $Li_2MoO_3$ as nearly-stable compounds. Further details about

competing phase mixtures and critical oxygen chemical potential windows for the above mentioned compounds are provided in Table S1† and Fig. S1†.

### 3.2. Classification and Performance of Li₂MO₃ Compounds
The functionality expected from each of the 19 stable/nearly-stable Li₂MO₃ materials in Fig. 1a (active vs. inactive) depends on the characteristics of the second Li₂MO₃ component in a structurally-integrated Li₂MᵢO₃-Li₂MᵢᵢO₃ cathode system. While the kinetics of Li⁺ diffusion or particle morphology can influence the electrochemical activity/inactivity of a battery cathode, thermodynamics provides the principal basis that allows redox reactions to occur or not. Therefore, we use the operating voltage range as the primary guide to categorize a Li₂MO₃ material as active or inactive in an integrated Li₂MᵢO₃-Li₂MᵢᵢO₃ system. The second key factor in designing Li₂MO₃ cathodes is their stability upon delithiation. For example, the Li₂MO₃ structure might undergo a phase transformation or structural change by migration of the M cations into the Li-layers or by irreversibly losing oxygen. Our HT-design strategy considers all these factors as described below.

Active vs. inactive Li₂MO₃: The voltage stability windows for the 19 Li₂MO₃ compounds identified in this work are provided in Fig. 2 (and Fig. S2†). In thermodynamic terms, an inactive Li₂MO₃ component serves as a structural stabilizer for a redox-active counterpart and remains electrochemically-inactive unless activated by lithium extraction at an elevated voltage. Previously-explored Li₂TiO₃, Li₂MnO₃, Li₂ZrO₃, and Li₂SnO₃ stabilizers¹⁻¹⁸,²⁵ in Fig. 2 are good examples of inactive Li₂MO₃ materials because the transition metal ions are not electrochemically oxidized below ~4 V. On the other hand, good examples of active Li₂MO₃ cathode materials are Li₂RuO₃ and Li₂IrO₃ because they are capable of carrying out redox reactions in a wide voltage window.¹⁴⁻¹⁸,²²⁻²⁴

Stability against decomposition to other phases upon delithiation: Delithiation reactions can destabilize $Li_{2-x}MO_3$ structures; therefore, we further evaluate their thermodynamic stabilities upon delithiation within the OQMD. In particular, we find that $Li_{2-x}MO_3$ materials for M = Ru, Rh, Os, Ir, and Pt are resistant to phase transformations to relatively high values of $x \geq 1$ (see Table S2$\dagger$).

Stability against oxygen release upon delithiation: To classify a $Li_2MO_3$ compound as active or inactive, we need to know how far it can be charged prior to O-release. Oxygen has already been reported to play a role in the redox activity of $LiCoO_2;^{64}$ furthermore, recent studies have indicated that electron holes on the oxygen ions contribute to redox activity in Li-rich metal oxide cathode materials. $^{65,66}$ The thermodynamic measure of whether participation of O-holes in redox reactions would lead to irreversible oxygen loss in a material is its oxygen vacancy formation energy ($\Delta E_{vac,O}$). We use $\Delta E_{vac,O}$ as the primary guideline to determine the stability of $Li_2MO_3$, $Li_{2-\delta}MO_3$, and $MO_3$ compounds to oxygen loss ($\delta$ = dilute limit concentration; see Fig. 3a and Table S3$\dagger$). A negative $\Delta E_{vac,O}$ indicates a strong thermodynamic tendency to release oxygen from the host structure. We confirm that $\Delta E_{vac,O}$ is positive for all the fully-lithiated stable/nearly-stable $Li_2MO_3$ compounds of this study. Nevertheless, $Li_2FeO_3$ and $Li_2NiO_3$ have very small $\Delta E_{vac,O}$ values, which support our calculated data in Fig. 1a that these compounds would decompose with relatively small changes in oxygen chemical potential and also hint at relatively unstable $Fe^{4+}$ and $Ni^{4+}$ oxidation states, respectively. We find that several partially-delithiated $Li_{1.5}MO_3$ and completely-delithiated $MO_3$ compounds are resistant to oxygen evolution. If $\Delta E_{vac,O}$ is observed to be positive for all stages of delithiation, we consider that compound to be an excellent candidate either as an active or inactive $Li_2MO_3$ material. However, if $\Delta E_{vac,O}$ is negative for any delithiated species, the compound will release oxygen during the charge

process, thereby excluding it as a good active cathode (Fig. S3†). Nevertheless, such materials may still be used as an inactive stabilizer as long as the cell is not charged beyond the voltage at which oxygen is released.

Stability against metal-migration: The voltage fade observed in $Li_2MnO_3$-stabilized $LiM'O_2$ results from the accumulated effects of local defects (e.g., dumbbells, spinel-like configurations, vacancies), where Mn migration facilitated by oxygen vacancies is critical to the overall degradation process. $^{8,10,67,68}$ Here, we calculate the thermodynamic driving-force for metal-migration by comparing the formation energy of the metal-migrated-structure (MMS) and the pristine-structure (PS) (Fig. 3b and Table S4†). Based on the Brønsted–Evans–Polanyi principle, the metal migration energy in systems considered here is expected to be linearly correlated with the thermodynamic energy difference between these initial and final states. $^{69-72}$ Since many $Li_{2-x}MO_3$ compounds release oxygen during the charging process (Fig. 3a), we assess the migration tendency of M in $Li_{1.5}MO_3$, $Li_{1.5}MO_{3-\delta}$, $MO_3$, and $MO_{3-\delta}$ materials. We find that the thermodynamic driving-force for migration is radically-altered by the presence of an O-vacancy; e.g., Mn migration is facilitated in an O-deficient $MnO_{3-\delta}$ structure, consistent with previous reports $^{1,3,5,9,67,68}$. We therefore indicate the migration energies that are relevant when simultaneously considering stability against oxygen loss with a black-edged box in Fig. 3b. We consider the compounds that are resistant to metal-migration to be excellent active or inactive $Li_2MO_3$ candidates, and those with metal-migration tendencies to be candidates only as inactive stabilizers, provided that the $Li_2MO_3$ stabilizers are not electrochemically-activated above a prescribed voltage.

Overall classification as active/inactive $Li_2MO_3$: We have considered the voltage window, oxygen stability, and metal-migration tendency to classify each $Li_2MO_3$ compound as an electrochemically active or inactive material (Table S5†). The ideal active $Li_2MO_3$ cathode

should have a wide voltage window and stability to oxygen evolution and metal migration.

The other $Li_2MO_3$ compounds are classified as inactive stabilizers, which do not undergo redox until high voltages (i.e., at higher voltages, these materials also need to avoid oxygen loss and metal migration). Some $Li_2MO_3$ species can function either as an active cathode or an inactive stabilizer depending on the characteristics of the other $Li_2MO_3$ component, and/or the operation of the battery, as presented in Table S5†.

Using the above classification scheme, we categorize $Li_2RuO_3$ as an active cathode, consistent with previous experimental reports. $^{14,15}$ It was shown that while substitution of $Ru^{4+}$ for $Mn^{4+}$ in $Li_{1.2}Mn_{0.6-x}Ru_xNi_{0.2}O_2$ reduced oxygen loss, a concomitant drop in the overall voltage also occurred; $^{73}$ therefore, according to our classification, $Li_2RuO_3$ is not acting as a stabilizer. $Li_2MnO_3$ appears to be one of the best stabilizers because delithiation only starts to occur (with oxygen loss) at 4.5 V. We find that $Li_2GeO_3$ is stable up to an even higher potential than $Li_2MnO_3$, and is highly resistant to oxygen loss and metalloid-migration upon charging. $Li_2MO_3$ ($M = Ti/Mn/Ni/Ge/Zr/Sn/Pb$) materials that are stable at high-potentials can serve as structural stabilizers for either an active $Li_2MO_3$ or other common layered-cathodes (e.g., $R\overline{3}m$-type $LiM'O_2$) and will increase the overall energy density in the integrated cathode system.

### 3.3. Active-active and Active-inactive $Li_2M_I O_3$-$Li_2M_{II}O_3$ Cathode Pairs

Pair classification based on voltage profiles: For mixed metal $Li_2M_IO_3$-$Li_2M_{II}O_3$ systems, we first begin by defining the types of pairs of cathode materials that arise. (i) Active/active pair
– $M_I$ and $M_{II}$ in $Li_2M_IO_3$-$Li_2M_{II}O_3$ can both contribute to the redox activity, as schematically shown in Fig. 4. An ideal example of this type of pairing is the $Li_2RuO_3$-$Li_2IrO_3$ system, the electrochemical behavior of which has been recently reported. $^{22}$ This cathode system displays a significant overlap in voltage between the two $Li_2MO_3$ end-members (Fig. 2). Here, we do

not classify the pairs that have a voltage gap (i.e., pairs with no voltage overlap between two Li₂MO₃ compounds) as an active/active pair; but, categorize them as an active/inactive pair.

(ii) Active/inactive pair – this battery cathode material would be mainly operated within the voltage window of the active component, as illustrated in Fig. 4. The high-voltage component remains inactive and stabilizes the integrated-structure. An example of this type of pairing is Li₂RuO₃-Li₂SnO₃.¹⁵

Thermodynamic mixing tendencies of pairs: When two C2/m materials (Li₂MᵢO₃/Li₂MᵢᵢO₃) are paired to form active/active or active/inactive cathodes, the tendency of Mᵢ and Mᵢᵢ to mix on the same sublattice will control the final morphology of the electrode particles (short-/long-range ordering). Previous experimental observations¹,²,4,5-9,14-22,24,25,60,61,67,68,73,74 suggest that for improved electrochemical performance, Mᵢ and Mᵢᵢ should either form a solid-solution or a closely-integrated nanocomposite. To reveal such tendencies, we estimate the mixing enthalpy $E_{\text{mix}}$ in a HT-fashion for all possible combinations of Mᵢ and Mᵢᵢ in a Li₄MᵢMᵢᵢO₆ supercell (Fig. 5 and Table S6†). Formally, a negative mixing enthalpy favors an ordered state. Therefore, a significantly negative $E_{\text{mix}}$ (<-25 meV/site, dark-blue-colored-boxes) ultimately suggests a tendency to form an ordered-compound, possibly leading to slower Li diffusion or undesired phase transformations¹⁹,⁶⁰,⁶¹. However, sufficient data is not currently available to completely exclude these ordered-compounds from future studies for LIB applications. A slightly negative $E_{\text{mix}}$ (-25 to 0 meV/site, light-blue-colored-boxes in Fig. 5) indicates a ‘weak’ tendency for metal ordering, and the system may form a solid solution, e.g., Li₂RuₓIr₁₋ₓO₃. A slightly positive $E_{\text{mix}}$ (0 to 25 meV/site, yellow- and orange-colored-boxes) represents a weak phase-separating tendency and would still lead to a solid-solution at low temperatures (e.g., Li₂RuₓSn₁₋ₓO₃)¹⁷ or weak phase-separating nanocomposite system (e.g., Li₂IrₓSn₁₋ₓO₃ after extended cycling)²⁴ depending on entropic contributions. Therefore,

we suggest the actual ordering of these $Li_2M_I O_3/Li_2M_{II}O_3$ pairs in yellow- and orange-colored-boxes (with a slightly positive $E_{\text{mix}}$) may depend on the synthesis conditions. Conversely, pairs with a considerably positive $E_{\text{mix}}$ (>25 meV/site, brown-colored-boxes) are likely to form a two-phase mixture. Based on these thermodynamic arguments, mixing tendencies to form ideal active/active or active/inactive $Li_2M_I O_3$-$Li_2M_{II}O_3$ pairs are largely promising for the 19 stable/nearly-stable compounds (see Fig. 5 – all favorable except the brown-colored-boxes). We have provided additional stable and nearly-stable III-V and II-VI pairs in Tables S7–S8†. Our results predict $Li_4FeSbO_6$ and $Li_4NiTeO_6$ cathodes to be stable compounds, consistent with previous reports$^{60,61,74}$, while revealing, for the first time, many other yet-undiscovered III-V and II-VI pairs.

Lattice mismatch: We provide the calculated lattice parameters for the $Li_2MO_3$ compounds in Table S9† and Fig. S4†. For convenience, we refine their lattice parameters using $R\overline{3}m$ structure$^{75,76}$ to compare them with other, well-defined, cathode structures such as $LiNi_{0.5}Co_{0.2}Mn_{0.3}O_2$ and $LiCoO_2$. For coupled cathodes, we only consider combinations with mismatch less than 0.5 Å (z-direction) to increase the likelihood of forming a coherent interface between the components, as applicable (see Fig. S4† for further discussions).

### 3.4. Designing High-Performance $Li_2MO_3$ Electrodes
There is increasing evidence that a systematic HT-DFT approach with comprehensive thermodynamic information can help understand and design new class of materials of importance,$^{26-36,77-79}$ that can be quickly confirmed by the subsequent experimental study. From the above information, we have established a general principle to design high-performance, layered $Li_2MO_3$ cathodes. When two stable/nearly-stable active $Li_2MO_3$ materials have an overlapping voltage, favorable metal mixing, and a small lattice parameter mismatch, we classify these electrodes as active-active pairs (Table S10†). Likewise, we

![](./images/813105271441195008_3.jpg)

provide the list of active-inactive pairs in Table S11†, where a higher voltage, inactive
$Li_2MO_3$ stabilizes a lower-voltage, active $Li_2MO_3$ component that is mainly responsible for
the redox processes. The compounds provided in Tables S10–12† are also screened for their
thermodynamic stability vs. quaternary Li-M₁-M₁₁-O chemical space within the OQMD³³,³⁴
(i.e., stable/nearly-stable materials that can be synthesized experimentally). Two other
important factors in designing high-energy layered oxide cathodes would be the electronic
and ionic conductivities; however, as the diffusion kinetic calculations are computationally
expensive to be added as a screening/attribute for ranking materials, it was not considered in
our current study.

Our HT-design strategy is validated as we note that it successfully reproduces previously-
examined active/inactive pairs, $Li_2RuO_3$-$Li_2MnO_3$, $Li_2RuO_3$-$Li_2SnO_3$, $Li_2RuO_3$-$Li_2TiO_3$, and
$Li_2IrO_3$-$Li_2SnO_3$ systems¹⁵⁻¹⁸,²⁴, and an active/active pair, $Li_2Ru_xIr_{1-x}O_3$²² (see Tables S10–
S11†). But, we go beyond reproducing existing materials and predict several other interesting
cases. We predict that several noble metal-containing $Li_2MO_3$ (M = Ru/Rh/Os/Ir/Pt) will
perform well as active components.¹⁴⁻¹⁸,²⁴ Depending on the other $Li_2MO_3$ component and the
operation voltage, we find that $Li_2CrO_3$, $Li_2CoO_3$, $Li_2PdO_3$, and $Li_2PtO_3$ can be used either as
an active or an inactive component (Tables S10–S11†).

The top 30 active/inactive pair candidates identified by our HT-design strategy, ranked by
gravimetric energy density are shown in the voltage vs. capacity chart in Fig. 6 and Table I.
Among the currently known systems, $Li_4RuMO_6$ (M = Mn/Sn/Ti) systems¹⁴⁻¹⁸ are found to be
in our top-30 list, whereas $Li_4IrSnO_6$²⁴ is not, because of its relatively low gravimetric energy
density (437 Wh/kgₒₓᵢdₑ). More importantly, we reveal at least a dozen new Li-rich cathode
pairs with higher gravimetric energy densities compared to recently-discovered materials,¹⁴⁻
¹⁸,²⁴ that are predicted to be synthesizable experimentally. In Fig. 6, we present a variety of

materials that use $Li_2TiO_3$ or $Li_2MnO_3$ as an inactive stabilizer with active counterparts such as $Li_2PdO_3$, $Li_2RhO_3$, and $Li_2PtO_3$ that can provide a very high energy density.

Our calculations provide new insights into the design of cathode materials for LIBs. As for $Li_2MnO_3$, $^{1-10}$ we expect an interplay of complex chemistry in the newly-predicted systems. It was previously asserted that the voltage decay in $Li_2Ru_xTi_{1-x}O_3$ electrodes is more severe compared to $Li_2Ru_xSn_{1-x}O_3$ due to the smaller Ti atoms migrating more easily than the bigger Sn atoms. $^{17}$ This assertion was contradicted in a subsequent study that found the opposite trend, attributing the superior performance of $Li_2Ru_xTi_{1-x}O_3$ to its greater structural stability. $^{18}$ While the variation in the experimental synthesis condition may lead to the observed differences in the electrochemical properties in these two studies, $^{17,18}$ our thermodynamic calculations demonstrate that titanium migration in O-depleted $TiO_{3-\delta}$ is energetically less favorable than tin migration in $SnO_{3-\delta}$ (Fig. 3b). $^{69-72}$ Further, our calculations show that delithiated $Li_2SnO_3$ becomes unstable above $\sim$4.41 V, leading to oxygen loss and subsequent metal-migration. Lastly, $Li_2TiO_3$ is predicted to be more resilient at higher voltages to titanium-migration. These observations stress that metal migration is not necessarily proportional to the ionic radius only, $^{17}$ and that other factors, such as the voltage window, oxygen redox activity and/or the release of oxygen gas, as well as the kinetics, influence the complex electrochemical reactions that occur in these layered-oxide electrode systems.

### 4. Conclusion
In summary, we offer a classification scheme and use it to guide the discovery and design of novel layered cathode materials, considering the advantages and disadvantages of structurally integrated, lithium-rich $Li_2MO_3$ cathode pairs. A comparison with known $Li_2MO_3$ compounds connects our DFT calculations and the experimental realization (*i.e.*, synthesizability). A total of 15 $Li_2MO_3$ compounds have been experimentally observed over the years, and our DFT

stability metrics correctly identify these compounds (i.e., with zero errors in the screening strategy) as stable or within ~25 meV/atom (roughly $kT$ at 300 K) of the stable convex hull.
This serves as strong validation that our computational DFT stability metric is highly effective strategy for screening experimentally observable, synthesizable compounds.
Prospects for these cathode systems with respect to their operating voltage, stability against oxygen loss and metal-migration, and the formation of solid-solution and/or coherent nanocomposite structures have been explored and exploited in our design strategy. Finally, we recommend the top 30 active/inactive $Li_2MO_3$ pair candidates that satisfy our HT-design strategy, ranked by gravimetric energy density, in calling for experimental testing. In particular, we propose that $Li_4CrTiO_6$ and $Li_4CrMnO_6$, in which $Cr^{6+}$ oxidation is accessible during lithium extraction, are candidates worthy of electrochemical evaluation (however, please note that $Cr^{6+}$ is a health hazard and such experiments would have to be conducted with caution). Active $Li_2MO_3$ cathodes containing precious metals (M = Pd, Rh, and Pt) and an inactive $Li_2GeO_3$ stabilizing component are of interest for providing a further fundamental understanding of $Li_2MO_3$ materials derived from our high-throughput computational search.

### Conflicts of Interest
There are no conflicts of interest to declare.

### Acknowledgements
S.Kim was supported by Northwestern-Argonne Institution of Science and Engineering (NAISE). M.A. and Z.L. were supported by the Dow Chemical Company. S.Kirklin and C.W. were supported as part of the Center for Electrochemical Energy Science (CEES), an Energy Frontier Research Center (EFRC) funded by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences (Award No. DE-AC02-06CH11357). V.I.H. was

supported by National Scientific Foundation (NSF, DMR-1309957). Support from the Advanced Batteries Materials Research (BMR) Program, in particular David Howell and Tien Duong, of the U.S. Department of Energy, Office of Energy Efficiency and Renewable Energy, is gratefully acknowledged by J.R.C. and M.M.T. This research used resources of the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231. S.Kim, M.A., V.I.H., and C.W. initially proposed the concept of performing HT-DFT calculations of $Li_2MO_3$ cathode structures and their related properties. V.I.H. and S.Kirklin helped setting up the calculations within the OQMD framework. S.Kim, M.A., and V.I.H. initially prepared the manuscript and figures with input from Z.L., J.R.C., M.M.T., and C.W. All authors contributed to the discussions and revision of the manuscript.

## Notes and References
1 M. M. Thackeray, S.-H. Kang, C. S. Johnson, J. T. Vaughey, R. Benedek and S. Hackney, *J. Mater. Chem.*, 2007, **17**, 3112-3125.

2 C. Genevois, H. Koga, L. Croguennec, M. Ménétrier, C. Delmas and F. Weill, *J. Phys. Chem. C.*, 2014, **119**, 75-83.

3 D. Y. W. Denis, K. Yanagida, Y. Kato and H. Nakamura, *J. Electrochem. Soc.*, 2009, **156**, A417-A424.

4 S.-H. Kang, C. Johnson, J. Vaughey, K. Amine and M. M. Thackeray, *J. Electrochem. Soc.*, 2006, **153**, A1186-A1192.

5 B. Song, Z. Liu, M. O. Lai and L. Lu, *Phys. Chem. Chem. Phys.*, 2012, **14**, 12875-12883.

6 J. R. Croy, J. S. Park, F. Dogan, C. S. Johnson, B. Key and M. Balasubramanian, *Chem. Mater.*, 2014, **26**, 7091-7098.


7 J. R. Croy, H. Iddir, K. Gallagher, C. S. Johnson, R. Benedek and M. Balasubramanian, Phys. Chem. Chem. Phys., 2015, 17, 24382-24391.

8 J. R. Croy, M. Balasubramanian, K. G. Gallagher and A. K. Burrell, Acc. Chem. Res., 2015, 48, 2813-2821.

9 J. R. Croy, K. G. Gallagher, M. Balasubramanian, Z. Chen, Y. Ren, D. Kim, S.-H. Kang, D. W. Dees and M. M. Thackeray, J. Phys. Chem. C., 2013, 117, 6525-6536.

10 E. Lee and K. A. Persson, Adv. Energy Mater., 2014, 4, 1400498.

11 M. Rossouw, D. Liles and M. M. Thackeray, J. Solid State Chem., 1993, 104, 464-466.

12 P. Kalyani, S. Chitra, T. Mohan and S. Gopukumar, J. Power Sources, 1999, 80, 103-106.

13 A. D. Robertson and P. G. Bruce, Chem. Mater., 2003, 15, 1984-1992.

14 M. Sathiya, K. Ramesha, G. Rousse, D. Foix, D. Gonbeau, A. Prakash, M. Doublet, K. Hemalatha and J.-M. Tarascon, Chem. Mater., 2013, 25, 1121-1131.

15 M. Sathiya, G. Rousse, K. Ramesha, C. P. Laisa, H. Vezin, M. T. Sougrati, M. L. Doublet, D. Foix, D. Gonbeau, W. Walker, A. S. Prakash, M. Ben Hassine, L. Dupont and J.-M. Tarascon, Nat. Mater., 2013, 12, 827-835.

16 E. Salager, V. Sarou-Kanian, M. Sathiya, M. Tang, J.-B. Leriche, P. Melin, Z. Wang, H. Vezin, C. Bessada and M. Deschamps, Chem. Mater., 2014, 26, 7009-7019.

17 M. Sathiya, A. M. Abakumov, D. Foix, G. Rousse, K. Ramesha, M. Saubanère, M. Doublet, H. Vezin, C. Laisa and A. Prakash, Nat. Mater., 2015, 14, 230-238.

18 A. K. Kalathil, P. Arunkumar, D. H. Kim, J.-W. Lee and W. B. Im, ACS Appl. Mater. Interfaces, 2015, 7, 7118-7128.

19 J. Lee, A. Urban, X. Li, D. Su, G. Hautier and G. Ceder, Science, 2014, 343, 519-522.

20 J. Ma, Y.-N. Zhou, Y. Gao, X. Yu, Q. Kong, L. Gu, Z. Wang, X.-Q. Yang and L. Chen, Chem. Mater., 2014, 26, 3256-3262.

21 J. Ma, Y. Gao, Z. Wang and L. Chen, J. Power Sources, 2014, 258, 314-320. DOI: 10.1039/C7EE01782K

22 S. Sarkar, P. Mahale and S. Mitra, J. Electrochem. Soc., 2014, 161, A934-A942.

23 Y. Chen, M. Huo, L. Song and Z. Sun, RSC Adv., 2014, 4, 42462-42466.

24 E. McCalla, A. M. Abakumov, M. Saubanère, D. Foix, E. J. Berg, G. Rousse, M.-L.
Doublet, D. Gonbeau, P. Novák and G. Van Tendeloo, Science, 2015, 350, 1516-1521.

25 J.-S. Kim, C. S. Johnson, J. T. Vaughey, M. M. Thackeray, S. A. Hackney, W. Yoon, and
C. P. Grey, Chem. Mater., 2004, 16, 1996-2006.

26 S. Curtarolo, G. L. Hart, M. B. Nardelli, N. Mingo, S. Sanvito and O. Levy, Nat. Mater.,
2013, 12, 191-201.

27 M. M. Thackeray, C. Wolverton and E. D. Isaacs, Energy Environ. Sci., 2012, 5, 7854-
7863.

28 S. Kirklin, B. Meredig and C. Wolverton, Adv. Energy. Mater., 2013, 3, 252-262.

29 M. Liu, Z. Rong, R. Malik, P. Canepa, A. Jain, G. Ceder, and K. A. Persson, Energy
Environ. Sci., 2015, 8, 964-974.

30 A. Urban, I. Matts, A. Abdellahi and G. Ceder, Adv. Energy. Mater., 2016, 6, 1600488.

31 Y. Wang, W. D. Richards, S. P. Ong, L. J. Miara, J. C. Kim, Y. Mo and G. Ceder, Nat.
Mater:, 2015, 14, 1026-1031.

32 M. Aykol, S. Kirklin and C. Wolverton, Adv. Energy. Mater., 2014, 4, 1400690.

33 J. E. Saal, S. Kirklin, M. Aykol, B. Meredig and C. Wolverton, JOM, 2013, 65, 1501-
1509.

34 S. Kirklin, J. E. Saal, B. Meredig, A. Thompson, J. W. Doak, M. Aykol, S. Rühl and C.
Wolverton, npj Computational Materials, 2015, 1, 15010.

35 A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter,
D. Skinner and G. Ceder, APL Materials, 2013, 1, 011002.

36 M. Aykol, S. Kim, V. I. Hegde, D. Snydacker, Z. Lu, S. Hao, S. Kirklin, D. Morgan and C. Wolverton, *Nat. Commun.*, 2016, **7**, 13779.

37 G. Kresse and J. Hafner, *Phys. Rev. B*, 1993, **47**, 558-561.

38 G. Kresse and J. Furthmüller, *Comput. Mater. Sci.*, 1996, **6**, 15-50.

39 G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 1758-1775.

40 SGTE substance database, Thermodynamic Properties of Inorganic Materials, Landolt- Börnstein Group IV (Physical Chemistry), **19**, Pub. Springer Berlin / Heidelberg.

41 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

42 S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys and A. P. Sutton, *Phys. Rev. B*, 1998, **57**, 1505-1509.

43 V. Stevanović, S. Lany, X. Zhang and A. Zunger, *Phys. Rev. B*, 2012, **85**, 115104.

44 M.W. Chase, J.R. Downey, D.J. Frurip, R.A. McDonald and A.N. Syverud, *J. Phys. Chem. Ref. Data, Suppl.*, 1985, **14**, 1.

45 S. Kim, M. Aykol and C. Wolverton, *Phys. Rev. B*, 2015, **92**, 115411.

46 M. Aykol and C. Wolverton, *Phys. Rev. B*, 2014, **90**, 115105.

47 R. Chen, S. Ren, M. Yavuz, A. A. Guda, V. Shapovalov, R. Witter, M. Fichtner and H. Hahn, *Phys. Chem. Chem. Phys.*, 2015, **17**, 17288-17295.

48 M. M. Rahman, I. Sultana, T. Yang, Z. Chen, N. Sharma, A. M. Glushenkov and Y. Chen, *Angew. Chem. Int. Ed.*, 2016, **55**, 16059-16063.

49 K. Asakura, S. Okada, H. Arai, S. Tobishima and Y. Sakurai, *J. Power Sources*, 1999, **81-82**, 388-392.

50 S. Soreto Teixeira, M.P.F. Graça and L.C. Costa, *J. Non-Cryst. Solids*, 2012, **358**, 1924-1929.

51 S. Soreto Teixeira, M.P.F. Grac, L.C. Costa and M.A. Valente, *Mater. Sci. Eng. B*, 2014, 186, 83-88.

52 I. G. Kokarovtseva, I. N. Belyaev and L. V. Semenyakova, *Russ. Chem. Rev.*, 1972, 41, 929-937.

53 M. Tabuchi, A. Nakashima, H. Shigemura, K. Ado, H. Kobayashi, H. Sakaebe, H. Kageyama, T. Nakamura, M. Kohzaki, A. Hirano and R. Kanno, *J. Electrochem. Soc.*, 2002, 149, A509-A524.

54 E. Shinova, E. Zhecheva, R. Stoyanova and G. D. Bromiley, *J. Solid State Chem.*, 2005, 178, 1661-1669.

55 V. Todorova and M. Jansen, *Z. anorg. allg. Chem.*, 2011, 637, 37-40.

56 Y. Laligant, P. Lacorre and J. Rodríquez-Carvajal, *Materials Science Forum*, 2001, 378-381, 632-637.

57 B. Brazel and R. Hoppe, *Zeitschrift für Naturforschung B*, 1982, 37, 1369-1374.

58 J.-U. Rohde, J.-H. In, M. H. Lim, W. W. Brennessel, M. R. Bukowski, A. Stubna, E. Münck, W. Nam and L. Que, *Science*, 2003, 299, 1037-1039.

59 K. M. Van Heuvelen, A. T. Fiedler, X. Shan, R. F. De Hont, K. K. Meier, E. L. Bominaar, E. Münck and L. Que, *Proc. Natl. Acad. Sci.*, 2012, 109, 11933-11938.

60 E. McCalla, A. Abakumov, G. Rousse, M. Reynaud, M. T. Sougrati, B. Budic, A. Mahmoud, R. Dominko, G. Van Tendeloo and R. P. Hermann, *Chem. Mater.*, 2015, 27, 1699-1708.

61 E. McCalla, M. T. Sougrati, G. Rousse, E. J. Berg, A. Abakumov, N. Recham, K. Ramesha, M. Sathiya, R. Dominko and G. Van Tendeloo, *J. Am. Chem. Soc.*, 2015, 137, 4804-4814.

62 N. Imanishi, Y. Inoue, A. Hirano, M. Ueda, Y. Takeda, H. Sakaebe and M. Tabuchi,
Power Sources, 2005, 146, 21-26.

63 T. Okumura, M. Shikano and H. Kobayashi, J. Mater. Chem. A, 2014, 2, 11847-11856.

64 C. Wolverton and A. Zunger, Phys. Rev. Lett., 1998, 81, 606-609.

65 K. Luo, M. R. Roberts, R. Hao, N. Guerrini, D. M. Pickup, Y.-S. Liu, K. Edström, J.
Guo, A. V. Chadwick and L. C. Duda, Nat. Chem., 2016, 8, 684-691.

66 D.-H. Seo, J. Lee, A. Urban, R. Malik, S. Kang and G. Ceder, Nat. Chem., 2016, 8, 692-697.

67 Y. Li, J. Bareño, M. Bettge and D. P. Abraham, J. Electrochem. Soc., 2015, 162, A155-A161.

68 M. Gu, I. Belharouak, J. Zheng, H. Wu, J. Xiao, A. Genc, K. Amine, S. Thevuthasan, D.
R. Baer and J.-G. Zhang, ACS Nano, 2013, 7, 760-767.

69 J. Brønsted, Chem. Rev., 1928, 5, 231-338.

70 J. K. Nørskov, T. Bligaard, A. Logadottir, S. Bahn, L. B. Hansen, M. Bollinger, H.
Bengaard, B. Hammer, Z. Sljivancanin and M. Mavrikakis, J. Catal., 2002, 209, 275-278.

71 T. Bligaard, J. Nørskov, S. Dahl, J. Matthiesen, C. Christensen and J. Sehested, J. Catal.,
2004, 224, 206-217.

72 A. Logadottir, T. H. Rod, J. K. Nørskov, B. Hammer, S. Dahl and C. Jacobsen, J. Catal.,
2001, 197, 229-231.

73 J. C. Knight, P. Nandakumar, W. H. Kan and A. Manthiram, J. Mater. Chem. A, 2015, 3,
2006-2011.

74 M. Sathiya, K. Ramesha, G. Rousse, D. Foix, D. Gonbeau, K. Guruprakash, A. Prakash,
M. Doublet and J.-M. Tarascon, Chem. Comm., 2013, 49, 11376-11378.

75 S. Kim, C. Kim, J.-K. Noh, S. Yu, S.-J. Kim, W. Chang, W. C. Choi, K. Y. Chung and B.-W. Cho, *J. Power Sources*, 2012, **220**, 422-429.

76 S. Kim, C. Kim, Y.-I. Jhon, J.-K. Noh, S. H. Vemuri, R. Smith, K. Y. Chung, M. S. Jhon and B.-W. Cho, *J. Mater. Chem.*, 2012, **22**, 25418-25426.

77 X. Wan, A. M. Turner, A. Vishwanath and S. Y. Savrasov, *Phys. Rev. B.*, 2011, 83, 205101.

78 H. Weng, C. Fang, Z. Fang, B. A. Bernevig and X. Dai, *Phys. Rev. X*, 2015, **5**, 011029.

79 S. -M. Huang, S. -Y. Xu, I. Belopolski, C. -C. Lee, G. Chang, B. Wang, N. Alidoust, G. Bian, M. Neupane, C. Zhang, S. Jia, A. Bansil, H. Lin and M. Z. Hasan, *Nat. Commun.*, 2015, **6**, 7373.

Electronic Supplementary information (ESI)

† Electronic supplementary information (ESI) available: See DOI: 10.1039/c7eexxxxxx

Figures, Table, & Captions

![](./images/813105271441195008_4.jpg)

Figure 1. Stability of new $Li_2MO_3$ compounds calculated within the OQMD framework:³³,³⁴
a) $Li_2MO_3$ compounds that are thermodynamically stable/nearly-stable (on or within ~25 meV/atom of the convex-hull) with respect to all other phases in the OQMD³³,³⁴. The data points denoted by ‘+’ are the experimentally known $C2/m$ or $C2/c$ $Li_2MO_3$ compounds. There are other experimentally observed polymorphs and $Li_2MO_3$ reported without crystal structure (denoted by ‘*’). b) Oxygen chemical potential windows for stable $Li_2MO_3$ compounds found in Fig. 1a. The blue regions correspond to the region of stability for the $Li_2MO_3$ phase (see Fig. S1†). We assume that the change in entropy of solid phases is negligible relative to that of oxygen gas and a partial pressure of oxygen = 0.21 atm. $Li_2MO_3$ is not in equilibrium with $O_2$ gas outside of this window. The temperature-scale on the right is a guide for choosing optimum heat-treatment conditions during experimental synthesis.

![](./images/813105271441195008_5.jpg)

**Figure 2.** Calculated voltage of Li₂MO₃ compounds: We consider the following delithiation reactions: Li₄M₂O₆ → Li₃M₂O₆ → Li₂M₂O₆ → M₂O₆ and identify all intermediate reaction products (shown in the legend) that are stable with respect to the end-members. The calculated voltage for each step corresponds to the removal of Li atom that is energetically most favorable. Typical operating voltage windows of common cathode materials are also provided. "NCM" denotes LiNiₓCoᵧMn_zO₂ and "Layered-Layered" denotes xLi₂MnO₃·(1-x)NCM.

![](./images/813105271441195008_6.jpg)

Figure 3. Oxygen stabilities and metal-migration tendencies: a) We calculate the oxygen vacancy formation energy of Li₂MO₃, Li₁.₅MO₃, and MO₃ compounds to predict the tendency of O₂ gas evolution at various stages of the charging process. The oxygen chemical potential corresponding to room temperature (300 K) was subtracted from the final $\Delta E_{vac,O}$ values (~0.3 eV). b) We have examined the metal-migration tendency in Li₂-δMO₃, Li₂-δMO₃-δ, MO₃, and MO₃-δ compounds. The transition metal atom in the metal-layer of a pristine-structure (PS) is moved to the energetically most favorable empty Li-site to generate a metal-migrated-structure (MMS). We have identified the thermodynamically-likely structures at each step using $\Delta E_{vac,O}$ from Fig. 3a (black-edged-boxes). The voltage fade in Li₂MO₃ has been directly linked to the phase transformation caused by the above-mentioned metal-migration.

![](./images/813105271441195008_7.jpg)

Figure 4. Schematic of active/active and active/inactive cathode pair: In an active/active cathode pair, both $Li_2MO_3$ compounds are capable of carrying out the redox process. This is in contrast with an active/inactive cathode pair wherein only one active $Li_2MO_3$ cathode material is mostly responsible for redox during charge/discharge, while the other high-voltage $Li_2MO_3$ stabilizer remains mostly inactive.

![](./images/813105271441195008_8.jpg)

Figure 5. Mixing enthalpy ($E_{mix}$) in $Li_4M_IM_{II}O_6$ compounds: Entropy of mixing, $S_{mix}$, will favor the mixing of $M_I$ and $M_{II}$ on the M sublattice at finite temperatures by lowering the free energy of mixing as in $G_{mix} \cong E_{mix}-TS_{mix}$, and in the simplest case of ideal mixing, by -17 meV/site at room temperature ($2RT \times 0.5\ln(0.5)$). Thus, a negative mixing enthalpy ($E_{mix} < 0$) tends to yield a solid-solution ($Li_4M_IM_{II}O_6$) [blue-colored-boxes]. On the other hand, a weakly positive mixing enthalpy ($0 < E_{mix} < 25$ meV) may yield a nanocomposite structure ($Li_2M_IO_3$-$Li_2M_{II}O_3$) at low temperatures [yellow- and orange-colored boxes]. However, $E_{mix}$ <25 meV is small enough that the ideal mixing entropy ($S_{mix}$) at room temperature can induce mixing and result in a solid-solution. Therefore, for the $Li_2MO_3$ considered above, metal mixing tendencies are mostly favorable, except for those indicated by brown-colored-boxes.

![](./images/813105271441195008_9.jpg)

Figure 6. Voltage vs. capacity chart of the top 30 cathode pair candidates, ranked by gravimetric energy density: We use the average voltage and composite capacity to calculate the gravimetric energy density of all active/inactive $Li_2M_IO_3$-$Li_2M_{II}O_3$ cathode pairs suggested in Table S11† (for further discussions, see methods and Table I). An element M inside a box indicates the active component $Li_2M_IO_3$, and the inactive stabilizers are shown in the legends (i.e., $Li_2M_{II}O_3$, $M_{II} =$ Ge, Mn, Ti, Ni, Sn, Zr, Co, and Cr). We expect the active/inactive cathode pairs to either form a solid-solution ($Li_4M_IM_{II}O_6$) or a nanocomposite ($Li_2M_IO_3$-$Li_2M_{II}O_3$) based on the corresponding mixing energetics. "NCM", "LFP", and "LCO" denote $LiNi_xCo_yMn_zO_2$, $LiFePO_4$, and $LiCoO_2$, respectively. We note that 4.35 V LCO is also commercially-available, which would place LCO at ~650 Wh/kg in this plot.

Table I. Properties of the top-30 active/inactive Li₂MᵢO₃-Li₂MᵢᵢO₃ pair candidates, ranked by gravimetric energy density: We analyze all active/inactive cathode pair candidates in Table S11† by calculating average voltage, composite capacity, and gravimetric energy density of Li₂MᵢO₃-Li₂MᵢᵢO₃ pairs (see ESI†, Section S3 for further discussions).

<table>
  <thead>
    <tr>
      <th>Li₂MᵢO₃
-Li₂MᵢᵢO₃</th>
      <th>Energy
density
[Wh/kgₒₓᵢ𝒹ₑ]</th>
      <th>Redox
window
[V]</th>
      <th>Average
voltage
[V]</th>
      <th>Composite
capacity
[mAh/g]</th>
      <th>Active
Li₂MᵢO₃
reaction</th>
      <th>Stability
within OQMD
[meV/atom]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pd/Ti</td>
      <td>807</td>
      <td>3.84 – 4.52</td>
      <td>4.18</td>
      <td>192.8</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Pd/Mn</td>
      <td>787</td>
      <td>3.84 – 4.53</td>
      <td>4.19</td>
      <td>188.0</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Rh/Ti</td>
      <td>783</td>
      <td>3.49 – 4.52</td>
      <td>4.01</td>
      <td>195.2</td>
      <td>Li₂RhO₃→RhO₃</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Pd/Ni</td>
      <td>776</td>
      <td>3.84 – 4.52</td>
      <td>4.18</td>
      <td>185.6</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Cr/Ti</td>
      <td>767</td>
      <td>4.02 – 4.52</td>
      <td>4.27</td>
      <td>179.8</td>
      <td>Li₂CrO₃→Li₀.₅CrO₃</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Rh/Mn</td>
      <td>763</td>
      <td>3.49 – 4.53</td>
      <td>4.01</td>
      <td>190.3</td>
      <td>Li₂RhO₃→RhO₃</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Rh/Ni</td>
      <td>752</td>
      <td>3.49 – 4.52</td>
      <td>4.00</td>
      <td>187.8</td>
      <td>Li₂RhO₃→RhO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Pd/Ge</td>
      <td>748</td>
      <td>3.84 – 4.61</td>
      <td>4.23</td>
      <td>177.0</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Pd/Cr</td>
      <td>746</td>
      <td>3.84 – 4.01</td>
      <td>3.93</td>
      <td>190.0</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Co/Ti</td>
      <td>747</td>
      <td>4.05 – 4.52</td>
      <td>4.29</td>
      <td>174.4</td>
      <td>Li₂CoO₃→Li₀.₅CoO₃</td>
      <td>13</td>
    </tr>
    <tr>
      <td>Cr/Mn</td>
      <td>744</td>
      <td>4.02 – 4.53</td>
      <td>4.27</td>
      <td>174.3</td>
      <td>Li₂CrO₃→Li₀.₅CrO₃</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Pd/Co</td>
      <td>732</td>
      <td>3.84 – 4.05</td>
      <td>3.95</td>
      <td>185.4</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Rh/Ge</td>
      <td>726</td>
      <td>3.49 – 4.61</td>
      <td>4.05</td>
      <td>179.1</td>
      <td>Li₂RhO₃→RhO₃</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Co/Mn</td>
      <td>725</td>
      <td>4.05 – 4.53</td>
      <td>4.29</td>
      <td>169.2</td>
      <td>Li₂CoO₃→Li₀.₅CoO₃</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Co/Ni</td>
      <td>713</td>
      <td>4.05 – 4.52</td>
      <td>4.28</td>
      <td>166.6</td>
      <td>Li₂CoO₃→Li₀.₅CoO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Ru/Ti</td>
      <td>712</td>
      <td>2.72 – 4.52</td>
      <td>3.62</td>
      <td>196.6</td>
      <td>Li₂RuO₃→RuO₃</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Cr/Ge</td>
      <td>698</td>
      <td>4.02 – 4.61</td>
      <td>4.31</td>
      <td>161.8</td>
      <td>Li₂CrO₃→Li₀.₅CrO₃</td>
      <td>26</td>
    </tr>
    <tr>
      <td>Ru/Mn</td>
      <td>694</td>
      <td>2.72 – 4.53</td>
      <td>3.62</td>
      <td>191.6</td>
      <td>Li₂RuO₃→RuO₃</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Co/Ge</td>
      <td>682</td>
      <td>4.05 – 4.61</td>
      <td>4.33</td>
      <td>157.5</td>
      <td>Li₂CoO₃→Li₀.₅CoO₃</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Pd/Zr</td>
      <td>670</td>
      <td>3.84 – 4.18</td>
      <td>4.01</td>
      <td>166.8</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>23</td>
    </tr>
    <tr>
      <td>Ru/Ge</td>
      <td>660</td>
      <td>2.72 – 4.61</td>
      <td>3.67</td>
      <td>180.2</td>
      <td>Li₂RuO₃→RuO₃</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Pd/Sn</td>
      <td>634</td>
      <td>3.84 – 4.41</td>
      <td>4.13</td>
      <td>153.6</td>
      <td>Li₂PdO₃→PdO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Rh/Sn</td>
      <td>613</td>
      <td>3.49 – 4.41</td>
      <td>3.95</td>
      <td>155.2</td>
      <td>Li₂RhO₃→RhO₃</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Pt/Ti</td>
      <td>595</td>
      <td>3.61 – 4.52</td>
      <td>4.07</td>
      <td>146.2</td>
      <td>Li₂PtO₃→PtO₃</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Pt/Mn</td>
      <td>584</td>
      <td>3.61 – 4.53</td>
      <td>4.07</td>
      <td>143.4</td>
      <td>Li₂PtO₃→PtO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Pt/Ni</td>
      <td>577</td>
      <td>3.61 – 4.52</td>
      <td>4.06</td>
      <td>142.0</td>
      <td>Li₂PtO₃→PtO₃</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Pt/Ge</td>
      <td>563</td>
      <td>3.61 – 4.61</td>
      <td>4.11</td>
      <td>136.9</td>
      <td>Li₂PtO₃→PtO₃</td>
      <td>On Hull</td>
    </tr>
    <tr>
      <td>Ru/Sn</td>
      <td>556</td>
      <td>2.72 – 4.41</td>
      <td>3.56</td>
      <td>156.0</td>
      <td>Li₂RuO₃→RuO₃</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Ir/Ti</td>
      <td>531</td>
      <td>2.69 – 4.52</td>
      <td>3.60</td>
      <td>147.3</td>
      <td>Li₂IrO₃→IrO₃</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Ir/Mn</td>
      <td>521</td>
      <td>2.69 – 4.53</td>
      <td>3.61</td>
      <td>144.5</td>
      <td>Li₂IrO₃→IrO₃</td>
      <td>11</td>
    </tr>
  </tbody>
</table>

For a table of contents entry (8 cm × 4 cm)

![](./images/813105271441195008_10.jpg)

Materials Design of new Li-rich $Li_2(M_\text{I},M_\text{II})O_3$ layered oxides for high-energy-density lithium-ion batteries *via* a multi-faceted high-throughput density function theory calculation.