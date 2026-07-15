# Surface Coverage as an Important Parameter for Predicting Selectivity Trends in Electrochemical CO₂ Reduction
Andrew R. T. Morrison, Mahinder Ramdin, Leo J. P. van der Broeke, Wiebren de Jong, Thijs J. H. Vlugt, and Ruud Kortlever*

Cite This: *J. Phys. Chem. C* 2022, 126, 11927−11936

---

ACCESS |
Metrics & More |
Article Recommendations |
Supporting Information

## ABSTRACT:
The electrochemical CO₂ reduction reaction (CO₂RR) is important for a sustainable future. Key insights into the reaction pathways have been obtained by density functional theory (DFT) analysis, but so far, DFT has been unable to give an overall understanding of selectivity trends without important caveats. We show that an unconsidered parameter in DFT models of electrocatalysts—the surface coverage of reacting species—is crucial for understanding the CO₂RR selectivities for different surfaces. Surface coverage is a parameter that must be assumed in most DFT studies of CO₂RR electrocatalysts, but so far, only the coverage of nonreacting adsorbates has been treated. Explicitly treating the surface coverage of reacting adsorbates allows for an investigation that can more closely mimic operating conditions. Furthermore, and of more immediate importance, the use of surface coverage-dependent adsorption energies allows for the extraction of ratios of adsorption energies of CO₂RR intermediates (COOHₐds and HCOOₐds) that are shown to be predictive of selectivity and are not susceptible to systematic errors. This approach allows for categorization of the selectivity of several monometallic catalysts (Pt, Pd, Au, Ag, Zn, Cu, Rh, W, Pb, Sn, In, Cd, and Tl), even problematic ones such as Ag or Zn, and does so by only considering the adsorption energies of known intermediates. The selectivity of the further reduction of COOHₐds can now be explained by a preference for Tafel or Heyrovsky reactions, recontextualizing the nature of selectivity of some catalysts. In summary, this work resolves differences between DFT and experimental studies of the CO₂RR and underlines the importance of surface coverage.

![](./images/817368113375870981_1.jpg)

## INTRODUCTION
Transitioning away from carbon-emitting technologies and systems is a crucial part of solving global climate change, but there are several problems that must be solved. The importance of intermittent energy sources in the transition and the probable continued reliance on carbon-emitting devices are two such problems. The electrochemical CO₂ reduction reaction (CO₂RR) to commodity chemicals and fuels is can solve these problems by closing the carbon cycle and storing renewable energy in chemical bonds.¹⁻³ This reaction can synthesize several C₂₊ chemicals via multielectron reaction pathways, mainly using Cu-based catalysts.⁴⁻⁶ Moreover, the two-electron reduction products carbon monoxide and formate/formic acid are of interest as well since there are several sustainable use cases for both. The case for carbon monoxide involves the further processing to produce other chemicals,³,⁷,⁸ and the case for formate/formic acid is based on the current market for the chemical and future ideas for a bioeconomy or as a liquid reservoir of H₂ or CO.⁹⁻¹¹ With these multifaceted applications for the CO₂RR, understanding the trends in the electrocatalytic performance of different electrode materials toward the CO₂RR is crucial for catalyst development and optimization for the reaction.¹,¹² Initial experimental studies by Hori et al. mapped the activity and selectivity of many monometallic electrocatalysts for the CO₂RR.¹³ Development of density functional theory (DFT) models to resolve the observed trends and predict more selective and active catalytic materials is a logical method since selectivity is largely based on the interaction of the electrode surface and adsorbed intermediaries, which DFT is perfectly suited to analyze.¹⁴

The CO₂RR is understood to proceed through two possible adsorbed intermediates in an early stage of the reaction: COOHₐds and HCOOₐds. COOHₐds reacts to form both formate and CO, while HCOOₐds only forms formate, as evidenced by both experimental and theoretical studies.¹⁵⁻¹⁸ Along with the side production of H₂ from the hydrogen evolution reaction, these are all the two-electron reactions relevant to the CO₂RR (see eqs 123):¹³

$$\ce{CO2 (aq) + H2O (l) + 2e^- <=> HCOO^- + OH^-} \tag{1}$$

$$\ce{CO2 (aq) + H2O (l) + 2e^- <=> CO + 2OH^-} \tag{2}$$

Received: January 21, 2022
Revised: June 24, 2022
Published: July 13, 2022

![](./images/817368113375870981_2.jpg)

---

© 2022 The Authors. Published by
American Chemical Society
11927
https://doi.org/10.1021/acs.jpcc.2c00520
*J. Phys. Chem. C* 2022, 126, 11927−11936

$$\mathrm{H}_{2} \mathrm{O}(\mathrm{l})+2 \mathrm{e}^{-} \rightleftarrows \mathrm{H}_{2}+2 \mathrm{OH}^{-} \tag{3}$$

Other products, such as hydrocarbons and alcohols, are produced through further reduction of adsorbed CO.¹⁵ There are other possible adsorbed intermediates, including $\mathrm{CO}_{2}^{-}{}_{\text{ads}}$, the adsorbed products, and of course the intermediates involved in the multielectron reduction toward hydrocarbons and alcohols (e.g., $\mathrm{COH}_{\text{ads}}$).¹⁵ However, the current understanding of the selectivity for two-electron reduction products is that materials that bind $\mathrm{HCOO}_{\text{ads}}$ more strongly than $\mathrm{COOH}_{\text{ads}}$ produce formic acid, materials with the reverse tend to produce CO, and materials that bind $\mathrm{H}_{\text{ads}}$ strongly tend to have side reactions,¹⁵⁻¹⁸ making these species determining in selectivity. However, this basic understanding is yet to match model-based first-principles descriptions, so there are essential details yet to be understood.

Despite the consensus on the two-electron reaction mechanism and rules for product selectivity, designing a DFT model that is able to classify (i.e., predict the major product(s) of the catalyst based on DFT results) the electrocatalytic performance of materials for the CO₂RR in a holistic manner, across multiple materials as opposed to focusing on a single material, has proven difficult. Studies that elucidate specific mechanisms or are about specific materials are useful, but interpretation remains challenging without a better holistic understanding. Holistic approaches to classify CO₂RR catalysts have been mostly based on energies of adsorption¹⁷,¹⁹⁻²² (or quantities similar to adsorption energy, like computational hydrogen electrode potentials¹⁹). Trends across a small number of surfaces between the key adsorbates and their associated products may be observed, but this is not a proper classification.¹⁷ However, using the energies of the known intermediates leads to a misclassification of materials.¹⁹ For example, Ag is predicted to produce formate, but experimental results show a high selectivity toward CO,²³,²⁴ and Zn is predicted to produce $\mathrm{H}_{2}$ or HCOOH but mainly produces CO.²⁴,²⁵ Studies that have successfully categorized CO₂RR catalysts have done so not via the known intermediaries but by using the adsorption energies of $\mathrm{H}_{\text{ads}}$,²⁰ $\mathrm{CO}_{\text{ads}}$,²¹,²² or $\mathrm{OH}_{\text{ads}}$.²² It is not obvious why these adsorbates should primarily be predictive for CO₂RR selectivity. In summary, the more holistic DFT models that exist, while generally supporting the current understanding of the two-electron mechanism, all have specific shortcomings. Either they are not able to fully agree with the common understanding of selectivity or they do, but the model in question centers adsorbates that are not otherwise understood to be as important as the model indicates. This difference matters for studies that are trying to interpret finer points of CO₂RR since it establishes the foundation that those further explanations are based on. The difficulty of classifying CO₂RR catalysts is also one reason why this study focuses on classification rather than on a more sophisticated prediction—like partial current densities. Some studies have found quantitative relationships with partial current density and DFT models,¹⁷ but the experimental side of these studies is fragile because exact faradaic efficiencies measured in experiments are dependent on reaction conditions such as the local pH⁴,²⁶,²⁷ and cationic and anionic species²⁶,²⁸,²⁹ in the electrolyte, and the mass transfer limitations dependent on the particular cell configuration.³⁰,³¹ Therefore, we focus on accurately predicting the overall selectivity trends.

Of the anomalies mentioned above, the case of Ag has attracted the most interest, likely because Ag is potentially an industrially relevant CO₂RR catalyst.³²⁻³⁴ It has been hypothesized that the predicted preferentially adsorbed $\mathrm{HCOO}_{\text{ads}}$ on Ag is actually a key component to stabilize the $\mathrm{COOH}_{\text{ads}}$ intermediary, necessary for CO production, and inhibits hydrogen adsorption.³⁵ Another study explains why Ag produces mainly CO on the basis of a difference between mono- and bidentate adsorption of $\mathrm{HCOO}_{\text{ads}}$.³⁶ An alternate approach is to consider different reaction pathways for determining the selectivity.²² Alternatively, good agreement can be had with experiments by simply assuming that Ag adsorbs mainly $\mathrm{COOH}_{\text{ads}}$ (contrary to other DFT results) and further modeling with a multiscale DFT/microkinetic model³⁷,³⁸ or with grand-canonical DFT (which allows for a potential-dependent investigation).³⁹ In principle, there is nothing stopping these investigations from considering other materials to compare with Ag and thus strengthen their conclusions. In practice, researchers choose not to allocate computational resources toward this. Explaining why non-intermediary adsorbates could be important to selectivity is the other main point of investigation into the anomalies of the holistic DFT. The approach in those studies is often modeling the coverage of nonreacting adsorbates that are thought to be important.³⁵,⁴⁰⁻⁴³ In fact, such non-intermediary adsorbate studies are the only place in the literature where surface coverage is explicitly considered. Certainly, insights on the CO₂RR process and possible effects of nonreacting adsorbates are gained, but the effect of the surface coverage on the more holistic adsorption-energy-only work (i.e., coverage of $\mathrm{COOH}_{\text{ads}}$ and $\mathrm{HCOO}_{\text{ads}}$) has never been examined for the CO₂RR to the authors’ best knowledge. The first species considered in a DFT surface coverage investigation should be the species that can determine their selectivity—the key reacting intermediates of $\mathrm{COOH}_{\text{ads}}$ and $\mathrm{HCOO}_{\text{ads}}$. This is even more apparent when one considers that $\mathrm{COOH}_{\text{ads}}$ and $\mathrm{HCOO}_{\text{ads}}$ are the species that every DFT study must assume a specific coverage of to do DFT work on the CO₂RR (typically, for fractions between 1/9 and 1/4 for studies of CO₂RR). Yet, the effect of this parameter has never been investigated. Furthermore, the configuration of adsorbates is not always optimized,³⁵,⁴¹,⁴³ which can produce errors due to the large configuration space for multiple direct adsorbates.⁴⁴

Here, we leave aside the elucidation of the exact reaction mechanisms on specific materials or in the presence of certain bystander species and focus on improving general DFT models for the CO₂RR. To improve holistic modeling, we first hypothesize that the selectivity of the CO₂RR can be predicted based on only the adsorption energies of known adsorbed intermediates. Second, to resolve the issues adsorption-energy-only approaches have had in the past, we hypothesize that the effects of the surface coverage of the known reacting intermediates must be considered. The method employed here is to model several metal surfaces at different surface coverages of $\mathrm{COOH}_{\text{ads}}$, $\mathrm{HCOO}_{\text{ads}}$, and $\mathrm{H}_{\text{ads}}$. The considered surfaces are Pt, Pd, Au, Ag, Zn, Cu, Rh, W, Pb, Sn, In, Cd, and Tl, chosen to give a good selection of different classes of CO₂RR catalysts. The considered coverages will be from low values in the typical range to high coverages (specifically: 1/6 to 4/6) while keeping the DFT cell size the same to maintain comparability. It would be interesting to examine lower coverages to determine if there is a point where long-range lateral effects fully drop off, but this presents a large

computational effort while also maintaining a consistent cell size, so these are not considered for this reason. High coverages are, of course, interesting because they are likely to exist on real catalysts due to specific catalytic effects⁶ or reactor conditions such as high current densities or applied overpotentials,⁴⁵ which will likely be required due to the target current density of 200–1000 mA/cm².²⁴⁶ They are indicated to exist by, for example, high-pressure CO₂RR experiments where a suppression of hydrogen evolution is observed⁵⁴⁷⁴⁸ and changes in CO₂RR product selectivity due to proton availability⁴⁹ and CO₂ availability.⁵⁰

High surface coverages have never been directly observed, but the primary operando techniques that are capable of observing CO₂RR intermediates struggle to quantify coverages, so this should not be surprising in itself. Ultimately, if the hypothesis is correct, the exact range of coverage studied will not be significant as long as it is wide enough to see important trends. Indeed, this work might equally be interesting if the surface coverage is much lower than generally studied, if trends continue below studied coverages.

### METHODS
Adsorption energies of $COOH_{\text{ads}}$, $HCOO_{\text{ads}}$, and $H_{\text{ads}}$ are studied for 1, 2, 3, or 4 adsorbates of the same species on $2 \times 3$ metal surfaces. Energies of adsorption correspond to the following reactions:

$$
HCOO_{\text{ads}}: \text{CO}_2(\text{g}) + \text{H}^+ + \text{e}^- \rightleftarrows HCOO_{\text{ads}}
$$

$$
COOH_{\text{ads}}: \text{CO}_2(\text{g}) + \text{H}^+ + \text{e}^- \rightleftarrows COOH_{\text{ads}}
$$

$$
H_{\text{ads}}: \text{H}^+ + \text{e}^- \rightleftarrows H_{\text{ads}}
$$

Plane-wave DFT was used to simulate the electrocatalyst surface via use of the Vienna Ab initio Simulation Package (VASP), version 5.2.⁵¹ The simulations were run via Python scripts using the atomic simulation environment (ASE) library.⁵² The configuration space for multiple adsorbates is very high, even for two adsorbates,⁴⁴ which means it is very difficult to find the configuration of adsorbates that corresponds to the energy minima. In this work, the search for the best configuration was accomplished by the minima hopping algorithm implemented in the ASE⁴⁴⁵² that preserves adsorbate identity. It was used to explore several different configurations of adsorbates. Starting configurations were set by researcher intuition, in general, by placing the adsorbates in an "on-top" position (for $HCOO_{\text{ads}}$, the two oxygen atoms were both positioned above a surface atom, if possible) and then adjusting the orientation and positions to give a large distance between the atoms of different adsorbates. The algorithm generally found a diverse selection of possible configurations, and alternate starting configurations did not find either new types or lower energies, leading to confidence that the algorithm is exploring the space well. This follows the process in other studies using the same minima hopping algorithm to search for global energy minima for multiadsorbate systems.⁴²⁵³ It should be noted that this procedure comes with the same caveat found in those studies that there is no guarantee that the minima found are the global minima (this is an unavoidable limitation of any global optimization outside of special cases). The initial temperature for the molecular dynamics portion of minima hopping was 2000 K, with an initial acceptance energy of 0.25 eV and a time step of 1 fs.⁴⁴

The ASE minimum hopping algorithm was slightly modified by extending the Hookean constraints, which act to preserve adsorbate identity to allow repulsive Hookean forces. The Hookean constraints in ASE prevent an adsorbate from breaking apart during the molecular dynamics portion of the simulation, holding it together with Hookean forces.⁴⁴ In the algorithm as implemented in the most recent version of the ASE, two atoms constrained can move freely unless the distance between them is larger than a certain threshold and then they are pulled together. In the extension implemented here, two atoms can move freely unless the distance between them is less than a threshold, in which case they are pushed apart. Thus, the extension uses the same type of spring force, but in reverse, to prevent two adsorbates from combining and therefore losing their identities in that way.

The VASP simulations handled exchange and correlation with the BEEF-vdW functionals.⁵⁴⁻⁵⁶ These have been shown to be accurate for surface adsorption calculations compared with functionals such as PW91, HSE, or RPBE and comparable to functionals, which also describe vdW interactions.⁵⁷⁻⁶⁸ BEEF-vdW has also been used in a number of studies on CO₂RR,¹⁹²⁰²²³⁵³⁸⁴³ indicating that it is a good functional for the reactions. The ionic cores were described by a plane-wave basis set employing the Vanderbilt ultrasoft pseudopotential (US-PP).⁶⁹ The Brillion zone was sampled using a $4 \times 4 \times 1$ Monkhorst−Pack grid of $k$-points.⁷⁰ A kinetic energy cutoff of 500 eV and a density energy cutoff of 5000 eV were used. The system modeled was a $2 \times 3 \times 4$ supercell with at least $16$ Å of vacuum added in the direction perpendicular to the surface. The crystal structure of the surface is FCC for Pd, Pt, Rh, Au, Cu, Ag, and Pb; HCP for Cd, Tl, and Zn; BCC for W; and tetragonal for Sn (space group 141) and In (space group 139) with optimized lattice parameters. Figure 1 shows an example of the supercell with $2\ COOH_{\text{ads}}$. The top two layers of the metal were allowed to relax and the bottom two held in place, except in minima hopping calculations the top layers were also locked (this is known to cause a minimal error and represents significant computation saving for these calculations⁴⁴). The convergence criterion for the energy optimization was a maximum force of 0.02 eV/A per atom. Energies to account for zero-point energy according to the values of Chan et al.,⁷¹ and further corrections were made to gas-phase $H_2$ and to $COOH_{\text{ads}}$, 0.09 and 0.25 eV.¹⁹⁷² These details match closely with the work of Yoo et al., which was for a similar system, and the methods here were benchmarked via values in the Supporting Information of that article.¹⁹

### RESULTS AND DISCUSSION
In Figure 2, the total energies of adsorption for $n\ COOH_{\text{ads}}$ and $n\ HCOO_{\text{ads}}$ are plotted against each other for all $n$ less than or equal to the number of adsorbates that fit in a $2 \times 3$ surface cell of Au, Ag, and Pb (the surface can become too packed to easily add adsorbates—see Figure 2 inset).

These three materials are representative of materials studied here (see Section S2 in the Supporting Information). The parameters of the fits for all the considered metals can be seen in Table 1 for $COOH_{\text{ads}}$ vs $HCOO_{\text{ads}}$, Table 2 for $COOH_{\text{ads}}$ vs $H_{\text{ads}}$, and Table S1 in the Supporting Information for $HCOO_{\text{ads}}$ vs $H_{\text{ads}}$ (and all summarized in Figure 3). The total energy of adsorption increases as $n$ increases, which is expected as doubling $n$ will require approximately twice the adsorption energy, disregarding other effects. As can be seen in Figure 2, the energies of adsorption increase proportionally by

![](./images/817368113375870981_3.jpg)

Figure 1. Ag $2 \times 3$ cell with $2\ \text{COOH}_{\text{ads}}$ repeated once in both planar directions viewed from the (a) top and (b) side.

![](./images/817368113375870981_4.jpg)

Figure 2. Typical plots of $E_{\text{ads}}\ \text{COOH}_{\text{ads}}$ vs $E_{\text{ads}}\ \text{HCOO}_{\text{ads}}$ for 1−4 adsorbates of the same species in a $2 \times 3$ section of a Ag (green), Au (red), and Pb (blue) surface. Each point is labeled with the number of adsorbates on a $2 \times 3$ surface cell it represents. The lines are plotted from linear regressions of at least 3 of the points—discounting the 4th point if the surface with 4 adsorbates was too packed. Inset shows 1− $4\ \text{COOH}_{\text{ads}}$ in a $2 \times 3$ Au cell repeated twice in each direction as an example. See Section S2 in the Supporting Information for this type of plot for other metals.

the same amount for both $\text{HCOO}_{\text{ads}}$ and $\text{COOH}_{\text{ads}}$, up to 3 or 4 adsorbates (this is surface-dependent, see Section S2 in the Supporting Information). The uneven spacing of points along the lines indicates that there are adsorbate−adsorbate interactions, but the linear relationship in this space indicates that these interactions are approximately the same for $\text{COOH}_{\text{ads}}$ as for $\text{HCOO}_{\text{ads}}$ since if interadsorbate interactions differed between the two, the data would not be linear but would curve toward the adsorbate more stabilized by higher coverages (or less destabilized). This is interesting partially because for $\text{COOH}_{\text{ads}}$, hydrogen bonding could be expected to stabilize the adsorbates at high surface coverage, whereas that is not possible for $\text{HCOO}_{\text{ads}}$. Indeed, in several of the optimized geometries, the hydrogen atom in $\text{COOH}_{\text{ads}}$ takes up a position to the side of the oxygen atom rather than on top, indicating hydrogen bonding. Whether an adsorbed structure displays hydrogen bonding does depend on surface coverage (see Section S4 in the Supporting Information). However, the greatest number of hydrogen-bonded structures is actually found at medium surface coverages. A likely explanation for this is that the stabilizing effect of hydrogen bonding competes with the destabilizing effect of an increase in the footprint of the molecule on the surface, which the H bonding configuration requires. The larger footprint will make it more difficult to fit all the $\text{COOH}_{\text{ads}}$ in their optimum positions and also create more repulsion for nearby adsorbates not participating in the bond. This explains why the presence of hydrogen-bonded $\text{COOH}_{\text{ads}}$ does not curve the plots in Figure 2.

Of course, a line has two properties commonly called the slope and the intercept. The meaning of these two properties for the linear regressions and how they can explain/predict the $\text{CO}_2\text{RR}$ selectivity of materials is discussed here.

As can be seen in Figure 2, the fit for Ag has a significant nonzero intercept, and for Pb, it may be slightly out as well. In fact, this is typical of the linear regressions for this data. The intercepts of these fits should all be 0, since at 0 adsorbates, there should be 0 adsorption energy for both species. A nonzero intercept indicates that there is a systematic bias (i.e., the same size of effect regardless of the number of adsorbates) that influences calculated adsorption energies. The nonzero intercepts begin to show the value of this technique since it is a bias that would be present in normal DFT calculations, but there would be no way to see it since only a single point is calculated for each surface. The fact that for some of the surfaces the magnitude is tens of millielectronvolt means that the systematic bias would be enough to influence predictions, if they were based on a single point. The possible sources of the nonzero intercepts can be divided into three categories: biases to do with the surface energy, to do with the adsorbate-surface energy, or to do with the lateral interaction of adsorbates. The first possibility can be eliminated because if it were from the surface energy, all three fits (two in Tables 1 and 2 and the third in Section S2 of the Supporting Information) for a given material would have the same nonzero intercepts, which is not the case. The second can likely be eliminated since this would not be systematic since it would be multiplied by the number of adsorbates. Thus, these nonzero intercepts must arise from adsorbate−adsorbate interactions. This should also scale with the number of adsorbates but not necessarily linearly like with surface-adsorbate energies. Within lateral interactions, either there is an error in the DFT code or configuration arising from or dealing with lateral interactions (even effecting cells with one adsorbate because of the periodic boundary conditions) or there are long-range lateral interactions that fall away at very

**Table 1.** Parameters of the Linear Fit for Plots of the Total Energy of Adsorption for the HCOO and COOH Intermediaries Plotted against Each Other for 1−4 Adsorbates of the Same Type of Adsorbate in a $2 \times 3$ Section of the Surface as Calculated by DFT alongside the Main Products Seen in Experimental Investigation in the Literature for That Surface$^{a}$

<table>
<thead>
<tr>
<th>surface</th>
<th>slope ($\text{HCOO}_{\text{ads}}:\text{COOH}_{\text{ads}}$ $E_{\text{ads}}$ ratio)</th>
<th>intercept/ eV</th>
<th>main experimental products $(5\ \text{mA·cm}^{-2})^{24}$</th>
<th>main experimental products $(200\ \text{mA·cm}^{-2})^{73}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pd (111)</td>
<td>0.65</td>
<td>−0.39</td>
<td>$\text{H}_2$, CO</td>
<td>$\text{HCOOH}$, CO, $\text{H}_2$</td>
</tr>
<tr>
<td>Pt (111)</td>
<td>0.69</td>
<td>−0.10</td>
<td>$\text{H}_2$</td>
<td>$\text{H}_2$, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Rh (111)</td>
<td>0.74</td>
<td>−0.60</td>
<td>no data</td>
<td>CO, $\text{HCOOH}$, $\text{H}_2$</td>
</tr>
<tr>
<td>Au (111)</td>
<td>1.04</td>
<td>−0.04</td>
<td>CO</td>
<td>CO</td>
</tr>
<tr>
<td>W (110)</td>
<td>1.43</td>
<td>0.95</td>
<td>no data</td>
<td>$\text{H}_2$, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Cu (111)</td>
<td>1.52</td>
<td>0.00</td>
<td>CO, C2, and up</td>
<td>CO, C2, and up</td>
</tr>
<tr>
<td>Ag (111)</td>
<td>1.60</td>
<td>−0.30</td>
<td>CO</td>
<td>CO</td>
</tr>
<tr>
<td>Zn (0001)</td>
<td>1.64</td>
<td>0.68</td>
<td>CO</td>
<td>CO, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Sn (100)</td>
<td>1.69</td>
<td>0.02</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
<tr>
<td>Cd (0001)</td>
<td>2.06</td>
<td>−0.13</td>
<td>$\text{HCOOH}$</td>
<td>no data</td>
</tr>
<tr>
<td>In (001)</td>
<td>2.22</td>
<td>0.12</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
<tr>
<td>Pb (111)</td>
<td>2.38</td>
<td>0.09</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
<tr>
<td>Tl (0001)</td>
<td>2.57</td>
<td>0.15</td>
<td>$\text{HCOOH}$</td>
<td>no data</td>
</tr>
</tbody>
</table>

$^{a}$Examples of these plots can be seen in Figure 2. The table is sorted by a slope, with the main products noted for $5\ \text{mA·cm}^{-224}$ and $200\ \text{mA·cm}^{-273}$ (categorized according to the experimental study from the literature). See the Supporting Information material classification (Section S1) and further plots (Section S2).

**Table 2.** Parameters of the Linear Fit of Total Energy of Adsorption for the $\text{H}_{\text{ads}}$ and $\text{COOH}_{\text{ads}}$ Intermediaries vs Each Other for 1−4 Adsorbates of the Same Type of Adsorbate in a $2 \times 3$ Section of the Surface as Calculated by DFT$^{a}$

<table>
<thead>
<tr>
<th>surface</th>
<th>slope ($\text{H}_{\text{ads}}:\text{COOH}_{\text{ads}}$ $E_{\text{ads}}$ ratio)</th>
<th>intercept/eV</th>
<th>main experimental products $(5\ \text{mA·cm}^{-2})^{24}$</th>
<th>main experimental products $(200\ \text{mA·cm}^{-2})^{73}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>W (110)</td>
<td>0.26</td>
<td>0.08</td>
<td>no data</td>
<td>$\text{H}_2$, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Pd (111)</td>
<td>0.21</td>
<td>0.03</td>
<td>CO, $\text{H}_2$</td>
<td>$\text{HCOOH}$, CO, $\text{H}_2$</td>
</tr>
<tr>
<td>Rh (111)</td>
<td>0.15</td>
<td>0.01</td>
<td>no data</td>
<td>CO, $\text{HCOOH}$, $\text{H}_2$</td>
</tr>
<tr>
<td>Pt (111)</td>
<td>0.13</td>
<td>0.02</td>
<td>$\text{H}_2$</td>
<td>$\text{H}_2$, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Cu (111)</td>
<td>−0.04</td>
<td>−0.02</td>
<td>CO, $\text{C}_2$, and up</td>
<td>CO, $\text{C}_2$, and up</td>
</tr>
<tr>
<td>Ag (111)</td>
<td>−0.50</td>
<td>−0.01</td>
<td>CO</td>
<td>CO</td>
</tr>
<tr>
<td>Sn (100)</td>
<td>−0.68</td>
<td>−0.20</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
<tr>
<td>Au (111)</td>
<td>−0.75</td>
<td>−0.21</td>
<td>CO</td>
<td>CO</td>
</tr>
<tr>
<td>In (001)</td>
<td>−0.98</td>
<td>−0.15</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
<tr>
<td>Zn (0001)</td>
<td>−1.04</td>
<td>0.04</td>
<td>CO</td>
<td>CO, $\text{HCOOH}$</td>
</tr>
<tr>
<td>Tl (0001)</td>
<td>−1.27</td>
<td>−0.23</td>
<td>$\text{HCOOH}$</td>
<td>no data</td>
</tr>
<tr>
<td>Cd (0001)</td>
<td>−1.33</td>
<td>−0.01</td>
<td>$\text{HCOOH}$</td>
<td>no data</td>
</tr>
<tr>
<td>Pb (111)</td>
<td>−1.47</td>
<td>−0.25</td>
<td>$\text{HCOOH}$</td>
<td>$\text{HCOOH}$</td>
</tr>
</tbody>
</table>

$^{a}$The table is sorted by a slope, with the main products noted for $5\ \text{mA·cm}^{-2}$ and $200\ \text{mA·cm}^{-2}$. See the Supporting Information material classification (S1) and further plots (S2).

![](./images/817368113375870981_5.jpg)

**Figure 3.** Summary of the data in Tables 1, 2, and S1 (Supporting Information). The ratio between the adsorption energy of $\text{H}_{\text{ads}}$ and the most stable $\text{CO}_2\text{RR}$ intermediate (Tables 2 and S1) is plotted vs the ratio between the energy of adsorption of $\text{HCOO}_{\text{ads}}$ and $\text{COOH}_{\text{ads}}$ (Table 1). It is clearly seen here how the different classes of $\text{CO}_2\text{RR}$ catalysts group themselves.

low surface coverages. As has already been mentioned, studying very low coverages is computationally intensive and is not done in the present study. Whichever way it is, these nonzero intercepts show that studying coverage-dependent adsorption energies is important. Furthermore, a solution to the effect of nonzero intercepts is contained in the other parameter of the linear regressions of the DFT data: the slope.

The slope is actually where the linear relationship between the $\text{HCOO}_{\text{ads}}$ and $\text{COOH}_{\text{ads}}$ adsorption energies has utility because the slope is necessarily the ratio of the two adsorption energies (see Section S3 in the Supporting Information for more details). The ratio is an interesting quantity since it is a single number that can be used to compare the relative preference of a surface between two adsorbates. In this case, a higher ratio indicates that $\text{HCOO}_{\text{ads}}$ is more strongly adsorbed than $\text{COOH}_{\text{ads}}$ and vice versa for a lower ratio. Calculating the ratio from the linear regression of coverage-dependent adsorption energies rather than from adsorption energies at a single coverage is superior because it eliminates the effects of the nonzero intercepts described above while secondarily reducing random errors. The slopes of coverage-dependent adsorption energy can thus be examined as a descriptor to predict if the surface mainly produces CO or $\text{HCOOH}$. In Table 1, the slopes and intercepts of fits for several different

metal surfaces are shown, and the main product(s) observed during experimental studies are listed. The data in Table 1 shows that the slope can be used to sort the materials with a single primary product by their selectivities. All surfaces with a fitted slope larger than 1.65 primarily produce formic acid/ formate (HCOOH), and surfaces with a fitted slope less than 1.65 will primarily produce CO. This is consistent with the understanding of the two intermediates. Surfaces where $HCOO_{ads}$ is more strongly adsorbed (high slope) produce mainly $HCOOH$ since $HCOO_{ads}$ reduces only to $HCOOH$, while surfaces where the slope is low adsorb more $COOH_{ads}$ that reduces to either CO or HCOOH. The sorting of Cu as a CO-producing material by the $HCOO_{ads}:COOH_{ads}$ ratio is consistent with the understanding that hydrocarbon products typically produced on Cu surfaces are known to result from the further reduction of adsorbed CO.¹⁵ It is especially of note that this method can place Ag and Zn on the CO-producing side of the divide. Also, Zn being at the boundary is consistent with work, showing that its main product is flexible.⁷⁴,⁷⁵ Another interesting point is Sn, being near the boundary on the HCOOH side. This is consistent with several studies that have shown that Sn can be modified or added to synthesize a catalyst that either produces CO⁷⁶⁻⁷⁹ or HCOOH.⁷⁸⁻⁸⁰

Another important distinction for two-electron products of the $CO_{2}RR$ is the difference between surfaces that predominantly produce a single product versus those that produce multiple products. As can be seen in Table 1, the multiple product surfaces tend to adsorb $COOH_{ads}$ more preferentially than the CO-selective surfaces, with $HCOO_{ads}:COOH_{ads}$ ratios below 1.5 being multiproduct surfaces. However, Au, a catalyst that is selective for CO, shows that this cannot be the whole story.

To determine the properties of a multiproduct $CO_{2}RR$ catalyst, the $COOH_{ads}:H_{ads}$ ratio will be used instead of the $HCOO_{ads}:COOH_{ads}$ adsorption energy ratio (see Table 2). The data in Table 2 is based on the same type of fits as seen in Figure 2, but with $H_{ads}$ adsorption energy substituted for $HCOO_{ads}$ (see Section S2 in the Supporting Information). In Table 2, higher slopes should tend to adsorb $H_{ads}$ more strongly than $COOH_{ads}$ based on the same reasoning as the $HCOO_{ads}:COOH_{ads}$ ratio for the difference between CO and HCOOH. As can be seen in Table 2, surfaces that have a higher slope (surfaces that more strongly adsorb hydrogen) do correspond to multiple product materials and those that produce predominately a single product all have a lower slope. Thus, the relative availability of adsorbed hydrogen determines whether surfaces that tend to adsorb $COOH_{ads}$ produce mostly CO or produce multiple products. Finally, the position of Cu, at the boundary between single product and multiple product materials, is consistent with this hypothesis since it reflects the need for a balance of adsorbed hydrogen and $CO_{2}$ reduction intermediaries to produce $C_{2}$ and higher products.⁸¹

To further put Table 1 and Table 2 in context and offer insights into the underlying mechanisms, some information about the electronic structure and the low coverage adsorption energies can be found in Table S2 in the Supporting Information. The energies of adsorption at low coverage underscore the used technique presented here showing no clear-cut delimitation of the different categories of the catalyst. There is an association between metals with a low d-band center (or the p-block metals) and the overall efficiency at the $CO_{2}RR$; however, the association between that parameter and which $CO_{2}RR$ intermediatory they tend to adsorb is much less clear. Another interesting potential association can be seen with the density of surface atoms, also found in Table S2.

So far, we have shown that our method can distinguish between catalysts that will produce mainly formate and mainly CO and between surfaces that produce mainly a single product (CO or formate) and those that have a more even distribution of products. The product distribution in the multiproduct surfaces does remain unpredictable, and the prime question here is why these surfaces that, according to the model presented, tend to strongly adsorb $COOH_{ads}$ can produce significant amounts of $HCOOH$ when $COOH_{ads}$ does not react to $HCOOH$ in CO-selective surfaces (e.g., Pd can produce a large amount of HCOOH and Au makes mainly CO, but both tend to prefer the $COOH_{ads}$ intermediate). According to the reasoning until now, multiproduct surfaces should make CO if they are reducing $CO_{2}$ at all, since they all tend to adsorb $COOH_{ads}$. A hypothesis to resolve this will be proposed. If a surface has a large amount of $H_{ads}$ and fewer $COOH_{ads}$ (the conditions for multiproduct surfaces), this condition will favor a Tafel mechanism for further reduction of $COOH_{ads}$. Surfaces that have less adsorbed $H_{ads}$ and more $COOH_{ads}$ (the likely condition of primarily CO-producing surfaces) will favor a Heyrovsky mechanism, which is through a reaction with an aqueous H, for further reduction. The Heyrovsky mechanism will naturally lead to production of CO rather than HCOOH because the upward positioned oxygen atom and hydroxyl group will screen the carbon from the incoming hydrogen. If the hydrogen reacts with the hydroxyl group, it will produce CO. Alternatively, if the reacting hydrogen is adsorbed to the catalyst, it can readily react with either the carbon of the $COOH_{ads}$ or its hydroxyl group. Thus, $COOH_{ads}$ reacting via the Tafel mechanism can readily form either CO or HCOOH. This is in line with the experimental evidence that HCOOH is selected for when $H_{ads}$ is made more available than aqueous H.⁸²⁻⁸⁴ A schematic representation of this explanation can be seen in Figure 4a along with a summary

![](./images/817368113375870981_6.jpg)

Figure 4. (a) Schematic of the proposed tendency of Heyrovsky vs Tafel mechanism for the $CO_{2}RR$. In the Heyrovsky mechanism, CO is the more likely product because the carbon atom is screened from reacting. In the Tafel mechanism, the angle of reaction is from the side, so either the carbon or OH group is open for the reaction. (b) Schematic of the deciding factors for the different types of the $CO_{2}RR$ catalyst.

of a guide to the selectivity of catalysts in Figure 4b. Thus, the selectivity of the multiproduct surfaces should be found by analyzing the further reduction of $COOH_{ads}$, rather than focusing on the adsorption energy of the initial intermediates. This is relevant for Pd selectivity, which can be made to favor either CO or HCOOH, even with catalysts that are entirely or mostly Pd. $^{85-92}$ Some analyses suggest that this can be explained by the difference between the adsorption energy of $COOH_{ads}$ and $HCOO_{ads}^{85-87}$ However, as seen here, the approach of focusing on the adsorption energy of $CO^{88-91}$ and/or the production of HCOOH through the COOH path $^{92}$ should yield more insights since they deal with the further reduction of the $COOH_{ads}$ intermediate, which is more significant.

## CONCLUSIONS
We have demonstrated that surface coverage effects are essential for predicting the selectivity of metal catalysts for the $CO_{2}RR$. Specifically, taking coverage-dependent adsorption energies as a descriptor of $CO_{2}RR$ catalyst selectivity is necessary to categorize catalysts by which two-electron products they tend to make. This success is due to the ability of surface coverage-dependent adsorption energies to eliminate systematic effects likely associated with adsorbate−adsorbate interactions. Importantly, this method successfully categorizes all the considered metals correctly, including previously problematic ones, and it does this through only adsorbates that are known to participate in the reaction. This combination of results has not been achieved in a previous study, so it is an important result in itself.

Our model supports the story told to explain two-electron product selectivity. That is to say, the difference between HCOOH and CO-producing surfaces is seen to lie in the relative energies of adsorption of $COOH_{ads}$ and $HCOO_{ads}$. The difference between electrodes that produce CO and multipleproduct surfaces (both categories tending to adsorb $COOH_{ads}$) is the relative energy of adsorption of $H_{ads}$ to $COOH_{ads}$. Furthermore, the reason that surfaces that tend to adsorb $COOH_{ads}$ are able to produce HCOOH in the case of multiproduct surfaces, but this ability is limited in CO-selective surfaces, is proposed to be a difference in Heyrovsky vs Tafel reaction mechanisms for further reduction of the $COOH_{ads}$ intermediate. This overall scheme can be seen in Figure 4b, which highlights how the possibility of $COOH_{ads}$ reducing to HCOOH is significant. In fact, this study supports the twoelectron selectivity story more so than other studies. This result is important in more than its own right because it indicates that less special explanations of certain surfaces or mechanisms may be needed than previously thought. Concretely, it can change interpretation of previous results. For example, this can already help to explain the selectivity of materials like Ag or Zn, and it recontextualizes the nature of Pd-based materials. It also indicates how the ability to tune Zn- or Sn-based catalysts for CO and HCOOH, as has been already seen in the literature can be understood. Furthermore, more confidence can be placed on the use of a DFT model that takes surface coverage into account to (re)examine the selectivity of (new) electrocatalytic materials for the $CO_{2}RR$.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.2c00520.

Material classification vs activity, further data and plots, elimination of systematic errors, and hydrogen bonding in $COOH_{ads}$ (PDF)

## AUTHOR INFORMATION
### Corresponding Author
Ruud Kortlever − Large-Scale Energy Storage, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands; orcid.org/0000-0001-9412-7480; Email: r.kortlever@tudelft.nl

### Authors
Andrew R. T. Morrison − Large-Scale Energy Storage, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands; Present Address: A.R.T.M.: Electrochemical Innovation Lab, University College London, London, UK WC1E 7JE & The Faraday Institution, Didcot, OX11 0RA, U.K

Mahinder Ramdin − Large-Scale Energy Storage, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering and Engineering Thermodynamics, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands; orcid.org/0000-0002-8476-7035

Leo J. P. van der Broeke − Engineering Thermodynamics, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands

Wiebren de Jong − Large-Scale Energy Storage, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands

Thijs J. H. Vlugt − Engineering Thermodynamics, Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, 2628 CB Delft, The Netherlands; orcid.org/0000-0003-3059-8712

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.2c00520

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This work was supported by RVO and TKI New Gas under project numbers TEEI116076, TCCU118009, and TKI-2019-CCUS-SUPER HIPE and by NWO (Netherlands Organization for Scientific Research, NWO). TJHV acknowledges NWO-CW for a VICI grant. This work was sponsored by NWO Domain Science for the use of supercomputer facilities.

## REFERENCES
(1) De Luna, P.; Hahn, C.; Higgins, D.; Jaffer, S. A.; Jaramillo, T. F.; Sargent, E. H. What Would It Take for Renewably Powered Electrosynthesis to Displace Petrochemical Processes? Science 2019, 364, No. eaav3506.

(2) Jouny, M.; Luc, W.; Jiao, F. General Techno-Economic Analysis of $CO_{2}$ Electrolysis Systems. Ind. Eng. Chem. Res. 2018, 57, 2165−2177.

(3) Foit, S. R.; Vinke, I. C.; de Haart, L. G. J.; Eichel, R.-A. Power-to-Syngas: An Enabling Technology for the Transition of the Energy System? *Angew. Chem., Int. Ed.* **2017**, *56*, 5402−5411.

(4) Kas, R.; Kortlever, R.; Yılmaz, H.; Koper, M. T. M.; Mul, G. Manipulating the Hydrocarbon Selectivity of Copper Nanoparticles in CO₂ Electroreduction by Process Conditions. *ChemElectroChem* **2015**, *2*, 354−358.

(5) Li, J.; et al. Electroreduction of CO₂ to Formate on a Copper-Based Electrocatalyst at High Pressures with High Energy Conversion Efficiency. *J. Am. Chem. Soc.* **2020**, *142*, 7276−7282.

(6) Kuhl, K. P.; Cave, E. R.; Abram, D. N.; Jaramillo, T. F. New Insights into the Electrochemical Reduction of Carbon Dioxide on Metallic Copper Surfaces. *Energy Environ. Sci.* **2012**, *5*, 7050−7059.

(7) Ramdin, M.; et al. Electroreduction of CO₂/CO to C₂ Products: Process Modeling, Downstream Separation, System Integration, and Economic Analysis. *Ind. Eng. Chem. Res.* **2021**, *60*, 17862−17880.

(8) Artz, J.; Müller, T. E.; Thenert, K.; Kleinekorte, J.; Meys, R.; Sternberg, A.; Bardow, A.; Leitner, W. Sustainable Conversion of Carbon Dioxide: An Integrated Review of Catalysis and Life Cycle Assessment. *Chem. Rev.* **2018**, *118*, 434−504.

(9) Yishai, O.; Lindner, S. N.; Gonzalez de la Cruz, J.; Tenenboim, H.; Bar-Even, A. The Formate Bio-Economy. *Curr. Opin. Chem. Biol.* **2016**, *35*, 1−9.

(10) Singh, A. K.; Singh, S.; Kumar, A. Hydrogen Energy Future with Formic Acid: A Renewable Chemical Hydrogen Storage System. *Catal. Sci. Technol.* **2016**, *6*, 12−40.

(11) Jens, C. M.; Nowakowski, K.; Scheffczyk, J.; Leonhard, K.; Bardow, A. CO from CO₂ and Fluctuating Renewable Energy Via Formic-Acid Derivatives. *Green Chem.* **2016**, *18*, 5621−5629.

(12) Garg, S.; Li, M.; Weber, A. Z.; Ge, L.; Li, L.; Rudolph, V.; Wang, G.; Rufford, T. E. Advances and Challenges in Electrochemical CO₂ Reduction Processes: An Engineering and Design Perspective Looking Beyond New Catalyst Materials. *J. Mater. Chem. A* **2020**, *8*, 1511−1544.

(13) Hori, Y. Electrochemical Co₂ Reduction on Metal Electrodes. In *Modern Aspects of Electrochemistry*, Vayenas, C. G.; White, R. E.; Gamboa-Aldeco, M. E., Eds.; Springer New York: New York, NY, 2008; pp 89−189.

(14) Maheshwari, S.; Li, Y.; Agrawal, N.; Janik, M. J. Chapter Three - Density Functional Theory Models for Electrocatalytic Reactions. In *Advances in Catalysis*, Song, C., Ed. Academic Press, 2018, Vol 63; pp 117−167.

(15) Kortlever, R.; Shen, J.; Schouten, K. J. P.; Calle-Vallejo, F.; Koper, M. T. M. Catalysts and Reaction Pathways for the Electrochemical Reduction of Carbon Dioxide. *J. Phys. Chem. Lett.* **2015**, *6*, 4073−4082.

(16) Hatsukade, T.; Kuhl, K. P.; Cave, E. R.; Abram, D. N.; Jaramillo, T. F. Insights into the Electrocatalytic Reduction of Co₂ on Metallic Silver Surfaces. *Phys. Chem. Chem. Phys.* **2014**, *16*, 13814−13819.

(17) Feaster, J. T.; Shi, C.; Cave, E. R.; Hatsukade, T.; Abram, D. N.; Kuhl, K. P.; Hahn, C.; Nørskov, J. K.; Jaramillo, T. F. Understanding Selectivity for the Electrochemical Reduction of Carbon Dioxide to Formic Acid and Carbon Monoxide on Metal Electrodes. *ACS Catal.* **2017**, *7*, 4822−4827.

(18) Zhu, M.; Tian, P.; Li, J.; Chen, J.; Xu, J.; Han, Y.-F. Structure-Tunable Copper−Indium Catalysts for Highly Selective Co₂ Electroreduction to Co or Hcooh. *ChemSusChem* **2019**, *12*, 3955−3959.

(19) Yoo, J. S.; Christensen, R.; Vegge, T.; Nørskov, J. K.; Studt, F. Theoretical Insight into the Trends That Guide the Electrochemical Reduction of Carbon Dioxide to Formic Acid. *ChemSusChem* **2016**, *9*, 358−363.

(20) Bagger, A.; Ju, W.; Varela, A. S.; Strasser, P.; Rossmeisl, J. Electrochemical CO₂ Reduction: A Classification Problem. *ChemPhysChem* **2017**, *18*, 3266−3273.

(21) Hussain, J.; Jónsson, H.; Skúlason, E. Calculations of Product Selectivity in Electrochemical Co₂ Reduction. *ACS Catal.* **2018**, *8*, 5240−5249.

(22) Tang, M. T.; Peng, H.; Lamoureux, P. S.; Bajdich, M.; Abild-Pedersen, F. From Electricity to Fuels: Descriptors for C1 Selectivity in Electrochemical Co₂ Reduction. *Appl. Catal., B* **2020**, No. 119384.

(23) Firet, N. J.; Smith, W. A. Probing the Reaction Mechanism of Co₂ Electroreduction over Ag Films Via Operando Infrared Spectroscopy. *ACS Catal.* **2017**, *7*, 606−612.

(24) Hori, Y.; Wakebe, H.; Tsukamoto, T.; Koga, O. Electrocatalytic Process of CO Selectivity in Electrochemical Reduction of CO₂ at Metal Electrodes in Aqueous Media. *Electrochim. Acta* **1994**, *39*, 1833−1839.

(25) Won, D. H.; Shin, H.; Koh, J.; Chung, J.; Lee, H. S.; Kim, H.; Woo, S. I. Highly Efficient, Selective, and Stable Co₂ Electroreduction on a Hexagonal Zn Catalyst. *Angew. Chem., Int. Ed.* **2016**, *55*, 9297−9300.

(26) de Salles, M.; Pupo, M.; Kortlever, R. Electrolyte Effects on the Electrochemical Reduction of CO₂. *ChemPhysChem* **2019**, *20*, 2926−2935.

(27) Gupta, N.; Gattrell, M.; MacDougall, B. Calculation for the Cathode Surface Concentrations in the Electrochemical Reduction of CO₂ in KHCO₃ Solutions. *J. Appl. Electrochem.* **2006**, *36*, 161−172.

(28) Resasco, J.; Chen, L. D.; Clark, E.; Tsai, C.; Hahn, C.; Jaramillo, T. F.; Chan, K.; Bell, A. T. Promoter Effects of Alkali Metal Cations on the Electrochemical Reduction of Carbon Dioxide. *J. Am. Chem. Soc.* **2017**, *139*, 11277−11287.

(29) Huang, Y.; Ong, C. W.; Yeo, B. S. Effects of Electrolyte Anions on the Reduction of Carbon Dioxide to Ethylene and Ethanol on Copper (100) and (111) Surfaces. *ChemSusChem* **2018**, *11*, 3299−3306.

(30) Lim, C. F. C.; Harrington, D. A.; Marshall, A. T. Effects of Mass Transfer on the Electrocatalytic Co2 Reduction on Cu. *Electrochim. Acta* **2017**, *238*, 56−63.

(31) Morrison, A. R. T.; van Beusekom, V.; Ramdin, M.; van den Broeke, L. J. P.; Vlugt, T. J. H.; de Jong, W. Modeling the Electrochemical Conversion of Carbon Dioxide to Formic Acid or Formate at Elevated Pressures. *J. Electrochem. Soc.* **2019**, *166*, E77−E86.

(32) Endrődi, B.; Kecsenovity, E.; Samu, A.; Halmágyi, T.; Rojas-Carbonell, S.; Wang, L.; Yan, Y.; Janáky, C. High Carbonate Ion Conductance of a Robust Piperion Membrane Allows Industrial Current Density and Conversion in a Zero-Gap Carbon Dioxide Electrolyzer Cell. *Energy Environ. Sci.* **2020**, *13*, 4098−4105.

(33) Ma, S.; Luo, R.; Gold, J. I.; Yu, A. Z.; Kim, B.; Kenis, P. J. A. Carbon Nanotube Containing Ag Catalyst Layers for Efficient and Selective Reduction of Carbon Dioxide. *J. Mater. Chem. A* **2016**, *4*, 8573−8578.

(34) Bhargava, S. S.; Proietto, F.; Azmoodeh, D.; Cofell, E. R.; Henckel, D. A.; Verma, S.; Brooks, C. J.; Gewirth, A. A.; Kenis, P. J. A. System Design Rules for Intensifying the Electrochemical Reduction of Co₂ to Co on Ag Nanoparticles. *ChemElectroChem* **2020**, *7*, 2001−2011.

(35) Bohra, D.; Ledezma-Yanez, I.; Li, G.; de Jong, W.; Pidko, E. A.; Smith, W. A. Lateral Adsorbate Interactions Inhibit Hcoo⁻ While Promoting CO Selectivity for CO₂ Electrocatalysis on Silver. *Angew. Chem., Int. Ed.* **2019**, *58*, 1345−1349.

(36) Zhang, X.-G.; Jin, X.; Wu, D.-Y.; Tian, Z.-Q. Selective Electrocatalytic Mechanism of Co₂ Reduction Reaction to Co on Silver Electrodes: A Unique Reaction Intermediate. *J. Phys. Chem. C* **2018**, *122*, 25447−25455.

(37) Singh, M. R.; Goodpaster, J. D.; Weber, A. Z.; Head-Gordon, M.; Bell, A. T. Mechanistic Insights into Electrochemical Reduction of Co₂ over Ag Using Density Functional Theory and Transport Models. *Proc. Natl. Acad. Sci. U. S. A.* **2017**, *114*, E8812−E8821.

(38) Chen, L. D.; Urushihara, M.; Chan, K.; Nørskov, J. K. Electric Field Effects in Electrochemical Co₂ Reduction. *ACS Catal.* **2016**, *6*, 7133−7139.

(39) Alsunni, Y. A.; Alherz, A. W.; Musgrave, C. B. Electrocatalytic Reduction of CO₂ to CO over Ag(110) and Cu(211) Modeled by Grand-Canonical Density Functional Theory. *J. Phys. Chem. C* **2021**, *125*, 23773−23783.


(40) Huang, Y.; Handoko, A. D.; Hirunsit, P.; Yeo, B. S. Electrochemical Reduction of $CO_2$ Using Copper Single-Crystal Surfaces: Effects of CO* Coverage on the Selective Formation of Ethylene. ACS Catal. 2017, 7, 1749-1756.

(41) Shi, C.; Hansen, H. A.; Lausche, A. C.; Nørskov, J. K. Trends in Electrochemical $CO_2$ Reduction Activity for Open and Close-Packed Metal Surfaces. Phys. Chem. Chem. Phys. 2014, 16, 4720-4727.

(42) Zhang, Y.-J.; Sethuraman, V.; Michalsky, R.; Peterson, A. A. Competition between $CO_2$ Reduction and $H_2$ Evolution on Transition-Metal Electrocatalysts. ACS Catal. 2014, 4, 3742-3748.

(43) Liu, H.; Liu, J.; Yang, B. Modeling the Effect of Surface Co Coverage on the Electrocatalytic Reduction of $CO_2$ to CO on Pd Surfaces. Phys. Chem. Chem. Phys. 2019, 21, 9876-9882.

(44) Peterson, A. A. Global Optimization of Adsorbate-Surface Structures While Preserving Molecular Identity. Top. Catal. 2014, 57, 40-53.

(45) Gileadi, E.; Conway, B. E. Kinetic Theory of Adsorption of Intermediates in Electrochemical Catalysis. J. Chem. Phys. 1963, 39, 3420-3430.

(46) Verma, S.; Kim, B.; Jhong, H.-R. M.; Ma, S.; Kenis, P. J. A. A Gross-Margin Model for Defining Technoeconomic Benchmarks in the Electroreduction of $CO_2$. ChemSusChem 2016, 9, 1972-1979.

(47) Kudo, A.; Nakagawa, S.; Tsuneto, A.; Sakata, T. Electro- chemical Reduction of High Pressure $CO_2$ on Ni Electrodes. J. Electrochem. Soc. 1993, 140, 1541-1545.

(48) Hirota, K.; Tryk, D. A.; Yamamoto, T.; Hashimoto, K.; Okawa, M.; Fujishima, A. Photoelectrochemical Reduction of $CO_2$ in a High- Pressure $CO_2$ + Methanol Medium at P-Type Semiconductor Electrodes. J. Phys. Chem. B 1998, 102, 9834-9843.

(49) Tomita, Y.; Teruya, S.; Koga, O.; Hori, Y. Electrochemical Reduction of Carbon Dioxide at a Platinum Electrode in Acetonitrile- Water Mixtures. J. Electrochem. Soc. 2000, 147, 4164.

(50) Wang, X.; et al. Efficient Methane Electrosynthesis Enabled by Tuning Local $CO_2$ Availability. J. Am. Chem. Soc. 2020, 142, 3525-3531.

(51) Kresse, G.; Hafner, J. Ab Initio Molecular-Dynamics Simulation of the Liquid-Metal-Amorphous-Semiconductor Transition in Germanium. Phys. Rev. B 1994, 49, 14251-14269.

(52) Ask Hjorth, L.; et al. The Atomic Simulation Environment-a Python Library for Working with Atoms. J. Phys.: Condens. Matter 2017, 29, 273002.

(53) Zhang, Y.-J.; Peterson, A. A. Oxygen-Induced Changes to Selectivity-Determining Steps in Electrocatalytic $Co_2$ Reduction. Phys. Chem. Chem. Phys. 2015, 17, 4505-4515.

(54) Wellendorff, J.; Lundgaard, K. T.; Mogelhøj, A.; Petzold, V.; Landis, D. D.; Nørskov, J. K.; Bligaard, T.; Jacobsen, K. W. Density Functionals for Surface Science: Exchange-Correlation Model Development with Bayesian Error Estimation. Phys. Rev. B 2012, 85, No. 235149.

(55) Klimeš, J.; Bowler, D. R.; Michaelides, A. A Critical Assessment of Theoretical Methods for Finding Reaction Pathways and Transition States of Surface Processes. J. Phys.: Condens. Matter 2010, 22, No. 074203.

(56) Klimeš, J.; Bowler, D. R.; Michaelides, A. Van der Waals Density Functionals Applied to Solids. Phys. Rev. B 2011, 83, No. 195131.

(57) Yuan, D.; Zhang, Y.; Ho, W.; Wu, R. Effects of Van Der Waals Dispersion Interactions in Density Functional Studies of Adsorption, Catalysis, and Tribology on Metals. J. Phys. Chem. C 2020, 124, 16926-16942.

(58) Yuan, D.; Liao, H.; Hu, W. Assessment of Van Der Waals Inclusive Density Functional Theory Methods for Adsorption and Selective Dehydrogenation of Formic Acid on Pt(111) Surface. Phys. Chem. Chem. Phys. 2019, 21, 21049-21056.

(59) Wellendorff, J.; Silbaugh, T. L.; Garcia-Pintos, D.; Nørskov, J. K.; Bligaard, T.; Studt, F.; Campbell, C. T. A Benchmark Database for Adsorption Bond Energies to Transition Metal Surfaces and Comparison to Selected Dft Functionals. Surf. Sci. 2015, 640, 36-44.

(60) Tayyebi, E.; Hussain, J.; Abghoui, Y.; Skúlason, E. Trends of Electrochemical Co2 Reduction Reaction on Transition Metal Oxide Catalysts. J. Phys. Chem. C 2018, 122, 10078-10087.

(61) Tameh, M. S.; Dearden, A. K.; Huang, C. Accuracy of Density Functional Theory for Predicting Kinetics of Methanol Synthesis from CO and $CO_2$ Hydrogenation on Copper. J. Phys. Chem. C 2018, 122, 17942-17953.

(62) Studt, F.; Abild-Pedersen, F.; Varley, J. B.; Nørskov, J. K. Co and Co2 Hydrogenation to Methanol Calculated Using the Beef-Vdw Functional. Catal. Lett. 2013, 143, 71-73.

(63) Mallikarjun Sharada, S.; Karlsson, R. K. B.; Maimaiti, Y.; Voss, J.; Bligaard, T. Adsorption on Transition Metal Surfaces: Trans- ferability and Accuracy of Dft Using the Ads41 Dataset. Phys. Rev. B 2019, 100, No. 035439.

(64) Mallikarjun Sharada, S.; Bligaard, T.; Luntz, A. C.; Kroes, G.-J.; Nørskov, J. K. Sbh10: A Benchmark Database of Barrier Heights on Transition Metal Surfaces. J. Phys. Chem. C 2017, 121, 19807-19815.

(65) Horvatits, C.; Li, D.; Dupuis, M.; Kyriakidou, E. A.; Walker, E. A. Ethylene and Water Co-Adsorption on Ag/Ssz-13 Zeolites: A Theoretical Study. J. Phys. Chem. C 2020, 124, 7295-7306.

(66) Gautier, S.; Steinmann, S. N.; Michel, C.; Fleurat-Lessard, P.; Sautet, P. Molecular Adsorption at Pt(111). How Accurate Are Dft Functionals? Phys. Chem. Chem. Phys. 2015, 17, 28921-28930.

(67) Duanmu, K.; Truhlar, D. G. Validation of Density Functionals for Adsorption Energies on Transition Metal Surfaces. J. Chem. Theory Comput. 2017, 13, 835-842.

(68) Bajdich, M.; Nørskov, J. K.; Vojvodic, A. Surface Energetics of Alkaline-Earth Metal Oxides: Trends in Stability and Adsorption of Small Molecules. Phys. Rev. B 2015, 91, No. 155401.

(69) Vanderbilt, D. Soft Self-Consistent Pseudopotentials in a Generalized Eigenvalue Formalism. Phys. Rev. B 1990, 41, 7892-7895.

(70) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. Phys. Rev. B 1996, 54, 11169-11186.

(71) Chan, K.; Tsai, C.; Hansen, H. A.; Nørskov, J. K. Molybdenum Sulfides and Selenides as Possible Electrocatalysts for $Co_2$ Reduction. ChemCatChem 2014, 6, 1899-1905.

(72) Christensen, R.; Hansen, H. A.; Vegge, T. Identifying Systematic Dft Errors in Catalytic Reactions. Catal. Sci. Technol. 2015, 5, 4946-4949.

(73) Hara, K.; Kudo, A.; Sakata, T. Electrochemical Reduction of Carbon Dioxide under High Pressure on Various Electrodes in an Aqueous Electrolyte. J. Electroanal. Chem. 1995, 391, 141-147.

(74) Zhang, T.; Qiu, Y.; Yao, P.; Li, X.; Zhang, H. Bi-Modified Zn Catalyst for Efficient $CO_2$ Electrochemical Reduction to Formate. ACS Sustainable Chem. Eng. 2019, 7, 15190-15196.

(75) Li, Q.; et al. Tuning Sn-Catalysis for Electrochemical Reduction of $CO_2$ to CO Via the Core/Shell $Cu/Sno_2$ Structure. J. Am. Chem. Soc. 2017, 139, 4290-4293.

(76) Zhao, Y.; Su, D.; Dong, W.; Xu, X.; Zhang, X.; Hu, Y. High Crystallinity Sn Crystals on Ni Foam: An Ideal Bimetallic Catalyst for the Electroreduction of Carbon Dioxide to Syngas. RSC Adv. 2020, 10, 39026-39032.

(77) Yoo, C. J.; Dong, W. J.; Park, J. Y.; Lim, J. W.; Kim, S.; Choi, K. S.; Odongo Ngome, F. O.; Choi, S.-Y.; Lee, J.-L. Compositional and Geometrical Effects of Bimetallic Cu-Sn Catalysts on Selective Electrochemical $CO_2$ Reduction to CO. ACS Appl. Energy Mater. 2020, 3, 4466-4473.

(78) Lee, M.-Y.; Ringe, S.; Kim, H.; Kang, S.; Kwon, Y. Electric Field Mediated Selectivity Switching of Electrochemical $CO_2$ Reduction from Formate to CO on Carbon Supported Sn. ACS Energy Lett. 2020, 5, 2987-2994.

(79) Chandrashekar, S.; Nesbitt, N. T.; Smith, W. A. Electro- chemical $Co_2$ Reduction over Bimetallic Au-Sn Thin Films: Comparing Activity and Selectivity against Morphological, Composi- tional, and Electronic Differences. J. Phys. Chem. C 2020, 124, 14573-14580.

(80) Ye, K.; Cao, A.; Shao, J.; Wang, G.; Si, R.; Ta, N.; Xiao, J.; Wang, G. Synergy Effects on Sn-Cu Alloy Catalyst for Efficient CO₂ Electroreduction to Formate with High Mass Activity. *Sci. Bull.* **2020**, 65, 711−719.

(81) Vasileff, A.; Xu, C.; Jiao, Y.; Zheng, Y.; Qiao, S.-Z. Surface and Interface Engineering in Copper-Based Bimetallic Materials for Selective CO₂ Electroreduction. *Chem* **2018**, 4, 1809−1831.

(82) Gabardo, C. M.; Seifitokaldani, A.; Edwards, J. P.; Dinh, C.-T.; Burdyny, T.; Kibria, M. G.; O’Brien, C. P.; Sargent, E. H.; Sinton, D. Combined High Alkalinity and Pressurization Enable Efficient CO₂ Electroreduction to Co. *Energy Environ. Sci.* **2018**, 11, 2531−2539.

(83) Seifitokaldani, A.; Gabardo, C. M.; Burdyny, T.; Dinh, C.-T.; Edwards, J. P.; Kibria, M. G.; Bushuyev, O. S.; Kelley, S. O.; Sinton, D.; Sargent, E. H. Hydronium-Induced Switching between CO₂ Electroreduction Pathways. *J. Am. Chem. Soc.* **2018**, 140, 3833−3837.

(84) Rosen, B. A.; Zhu, W.; Kaul, G.; Salehi-Khojin, A.; Masel, R. I. Water Enhancement of Co₂ Conversion on Silver in 1-Ethyl-3-Methylimidazolium Tetrafluoroborate. *J. Electrochem. Soc.* **2012**, 160, H138−H141.

(85) Wang, J.; Kattel, S.; Hawxhurst, C. J.; Lee, J. H.; Tackett, B. M.; Chang, K.; Rui, N.; Liu, C.-J.; Chen, J. G. Enhancing Activity and Reducing Cost for Electrochemical Reduction of Co₂ by Supporting Palladium on Metal Carbides. *Angew. Chem., Int. Ed.* **2019**, 58, 6271−6275.

(86) Jiang, B.; Zhang, X.-G.; Jiang, K.; Wu, D.-Y.; Cai, W.-B. Boosting Formate Production in Electrocatalytic CO₂ Reduction over Wide Potential Window on Pd Surfaces. *J. Am. Chem. Soc.* **2018**, 140, 2880−2889.

(87) Gao, D.; et al. Switchable CO₂ Electroreduction Via Engineering Active Phases of Pd Nanoparticles. *Nano Res.* **2017**, 10, 2181−2191.

(88) Zhu, W.; Kattel, S.; Jiao, F.; Chen, J. G. Shape-Controlled CO₂ Electrochemical Reduction on Nanosized Pd Hydride Cubes and Octahedra. *Adv. Energy Mater.* **2019**, 9, No. 1802840.

(89) Zhu, W.; Zhang, L.; Yang, P.; Hu, C.; Luo, Z.; Chang, X.; Zhao, Z.-J.; Gong, J. Low-Coordinated Edge Sites on Ultrathin Palladium Nanosheets Boost Carbon Dioxide Electroreduction Performance. *Angew. Chem., Int. Ed.* **2018**, 57, 11544−11548.

(90) Dong, H.; Zhang, L.; Yang, P.; Chang, X.; Zhu, W.; Ren, X.; Zhao, Z.-J.; Gong, J. Facet Design Promotes Electroreduction of Carbon Dioxide to Carbon Monoxide on Palladium Nanocrystals. *Chem. Eng. Sci.* **2019**, 194, 29−35.

(91) Huang, H.; Jia, H.; Liu, Z.; Gao, P.; Zhao, J.; Luo, Z.; Yang, J.; Zeng, J. Understanding of Strain Effects in the Electrochemical Reduction of CO₂: Using Pd Nanostructures as an Ideal Platform. *Angew. Chem., Int. Ed.* **2017**, 56, 3594−3598.

(92) Klinkova, A.; De Luna, P.; Dinh, C.-T.; Voznyy, O.; Larin, E. M.; Kumacheva, E.; Sargent, E. H. Rational Design of Efficient Palladium Catalysts for Electroreduction of Carbon Dioxide to Formate. *ACS Catal.* **2016**, 6, 8115−8120.

---

### Recommended by ACS

**Kinetic Understanding of Catalytic Selectivity and Product Distribution of Electrochemical Carbon Dioxide Reduction Reaction**
Dai-Jian Su, Zhong-Qun Tian, *et al.*
MARCH 02, 2023
JACS AU
READ ➔

**Understanding the Activity and Design Principle of Dual-Atom Catalysts Supported on C₂N for Oxygen Reduction and Evolution Reactions: From Homonuclear to Heteronu...**
Mengjie Huang, Xiong-Xiong Xue, *et al.*
FEBRUARY 09, 2023
THE JOURNAL OF PHYSICAL CHEMISTRY LETTERS
READ ➔

**Potential-Dependent Free Energy Relationship in Interpreting the Electrochemical Performance of CO₂ Reduction on Single Atom Catalysts**
Hao Cao, Yang-Gang Wang, *et al.*
MAY 19, 2022
ACS CATALYSIS
READ ➔

**Catalytic CO₂/CO Reduction: Gas, Aqueous, and Aprotic Phases**
Alexander Bagger, Jan Rossmeisl, *et al.*
FEBRUARY 04, 2022
ACS CATALYSIS
READ ➔

Get More Suggestions >
---

11936

https://doi.org/10.1021/acs.jpcc.2c00520
*J. Phys. Chem. C* **2022**, 126, 11927−11936