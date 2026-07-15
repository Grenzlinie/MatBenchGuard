# Computational Predictions for Effective Separation of Xenon/Krypton Gas Mixtures in the MFM Family of Metal−Organic Frameworks

Isabel Cooley, Louise Efford, and Elena Besley*

**ABSTRACT:** This study shows that a range of separation applications for the MFM family of metal−organic frameworks (MOFs) can be expanded to include effective separations of Xe/Kr binary gas mixtures. The MFM family of copper paddlewheel-based, isoreticular MOFs has shown previously an excellent performance for $CO_2/CH_4$ and $CO_2/N_2$ gas separations. The proposed new function aids the development of this MOF series into a multiuse functional material. Xe/Kr separation is a critical step in production of the noble gases from air and in revalorizing xenon isotopes produced by a nuclear reactor. A complete analysis of Xe and Kr uptake and selectivity is presented, which also includes predictions of binding affinity of the guest atoms.

![](./images/864984454534266943_1.jpg)

## INTRODUCTION

Metal organic frameworks (MOFs) are a class of material that has experienced a great deal of attention in recent years due to their tunability, porosity, and high surface area.¹⁻⁵ Many thousands of real and hypothetical MOFs have appeared in the literature; to illustrate, the Northwestern database of hypothetical MOFs contains 137,953 structures,⁶ and the Computation Ready Experimental (CoRE) MOF database contains 14,142 experimental MOFs.⁷ Networks of metal-containing nodes and organic linkers, MOFs are of widespread interest for sensing, catalysis, and gas adsorption applications. In particular, exceptional gas uptake properties and specific interactions with guests indicate potential in adsorptive separation processes including pressure swing and temperature swing adsorption (PSA and TSA) and membrane methods. These methods represent a promising alternative to energy-intensive separation methods such as cryogenic distillation.

Time and resource costs render any attempt to experimentally examine all possible MOFs for uptake of even a single gas impossible. Computational studies can be invaluable in directing experimental efforts efficiently toward promising MOFs. On a particularly large scale, the diverse chemical space occupied by MOFs makes them a prime target for high-throughput computational screenings.⁴,⁵,⁸⁻¹⁰ Large data sets of structures can be studied using relatively cheap computational methods, as in Glover and Besley's search⁸ of nearly 7,000 MOFs for biogas upgrading properties. Promising MOFs identified by computational screenings are often the subject of detailed investigations using more intensive computational methods, which remain significantly faster than experimental studies. For extremely large data sets, machine learning methods can also be used; for example, Simon et al.⁵ screened over 670,000 MOFs from the Nanoporous Materials Genome for noble gas separations.

One family of MOFs—the MFM series (MFM 126−128 and MFM 136−138)¹¹—has shown experimentally promising capabilities for gas separations and displayed impressive selectivity for $CO_2/CH_4$ and $CO_2/N_2$ separations. The series is based on adaptations made to the ligands of the copper paddlewheel MOF MFM-136.¹² These MOFs are composed of tubular channels, and alteration of the ligand and thus the characteristics of the channels enabled optimization for the selected separations. For example, for separation of a 15/85 $CO_2/N_2$ mixture at 273 K and 1 bar, selectivity values for the series range from 10.6 to 65.4.¹¹ Since open metal sites are not present, separation ability and variations therein are predominantly determined by ligand characteristics, as seen in experimental binding site analysis,¹¹ which showed interactions with various parts of the ligands. For $CO_2$ adsorption in MFM-136, for example, binding sites defined by multiple interactions with aromatic rings dominate.¹² The lack of open metal sites also indicates a likelihood for water stability above that of many copper paddlewheel MOFs, a desirable feature for practical MOF use.

Received:  April 1, 2022
Revised:  June 16, 2022
Published: July 7, 2022

![](./images/864984454534266943_2.jpg)

© 2022 The Authors. Published by
American Chemical Society
11475
https://doi.org/10.1021/acs.jpcc.2c02237
J. Phys. Chem. C 2022, 126, 11475−11486

Expanding the available capabilities of the MFM MOFs series is an attractive aim. These MOFs have already been synthesized, are known to be robust, and are likely to be relatively water stable while displaying strong separation ability for industrially and environmentally relevant gas mixtures. Such a family of materials, if found to have further separation potential and multiple uses, may allow for increased efficiency in synthesis and function of separation apparatus. The geometry of the MFM MOFs and ligand-based interactions involved are of a nature suitable to separation of challenging gas mixtures $^{4,8}$ in which gases often possess similar properties and are difficult to differentiate. The tight, tubular geometry of hosts akin to the MFM family can play an important role, allowing gases to be differentiated by guest size where other factors are less effective.

One such separation is the xenon/krypton gas mixture. The two noble gases are widely used in industrial and medical applications involving lighting, $^{13}$ anesthetics, $^{14,15}$ and lung diagnostics and therapy, $^{16}$ and their separation is both challenging and pertinent in many chemical contexts. They are present in low concentrations in air amounting to 0.086 ppmv (Xe) and 1.14 ppmv (Kr). $^{14,17}$ A 20/80 xenon/krypton stream is typically obtained as a product of cryogenic distillation of air and is separated into its constituent components by further cryogenic distillation. The process is costly and energy-intensive, particularly due to the gases' similar chemical properties. It also has associated fire risks due to ozone build-up by radiolysis. $^{9,18}$

Xenon and krypton may additionally be obtained as byproducts of nuclear fission processes. A 10:1 mixture of xenon and krypton isotopes is a component of the used nuclear fuel (UNF) generated by a conventional nuclear reactor: its separation is pertinent both for production of xenon gas and for the safe sequestration of radioactive krypton isotopes formed during fission. UNF contains both $^{85}$Kr (half-life 10.8 years) and Xe isotopes with relatively short half-lives, such as $^{127}$Xe (half-life 36.3 days). $^{9}$ They may be stored together as a single mixture, $^{14}$ but effective separation of the two components is more attractive. Once separated, storage of the lower quantity of krypton becomes easier, while a separated xenon stream of sufficient purity has industrial value. A second kind of nuclear reactor, a molten salt reactor (MSR), can also be a source of xenon and krypton isotopes. The noble gases produced by MSR may have specific applications in medicine $^{16}$ applying to the radioactive isotopes in their own right. For example, $^{135}$Xe and $^{133}$Xe may be used as imaging agents in lung diagnostics and $^{133}$Xe in lung therapy to attack suitably sized viruses using $\beta$-radiation. $^{16}$ Cryogenic distillation is again a possibility for separation of nuclear byproducts but has the same associated risks and drawbacks. Meanwhile, trace levels of radioactive Kr can be left in the Xe stream, $^{19}$ and separations to obtain MSR byproducts are further complicated by requirements relating to reactor conditions. $^{16}$

The use of porous materials for adsorptive separation of Xe/ Kr gas mixtures is a promising alternative, pursued in a number of computational and experimental studies. Identifying a material with strong selectivity for one over the other is no straightforward task: with full valence shells, no dipole or quadrupole moments, and minimal reactivity, neither gas has strong chemical or coulomb interactions with pore walls to promote adsorption. Xenon is the larger and more polarizable of the two, with a kinetic diameter of $3.96$ Å, $^{20}$ compared to the kinetic diameter of krypton, $3.80$ Å. $^{20}$ Its higher polarizability leads to many more cases of Xe selectivity than Kr through van der Waals interactions, although krypton-selective materials have been observed under certain conditions. $^{21,22}$ Porous target materials of studies seeking Xe selectivity span from activated carbon $^{18,23,24}$ to zeolites, $^{18,19,22,25,26}$ organic cages, $^{27-29}$ and MOFs. $^{14,30}$ Over time, reachable Xe selectivity has increased, particularly with the advent of large-scale methods. Recent high-throughput screenings by, for example, Sikora et al. $^{4}$ and Simon et al., $^{5}$ facilitate highly targeted experimental and computational selectivity studies. Prior to such targeted efforts, benchmark Xe selectivity values were less than $20.^{14}$ Subsequently, SBMOF-1, identified in screenings as a top-performing structure with an incredible predicted selectivity at infinite dilution of 70.6, $^{5,9}$ was synthesized by Banerjee et al. $^{9}$ Their experimental selectivity of 16, although a large drop from the computational prediction, was the highest observed selectivity for this concentration at the time. Similarly, Li et al. $^{31}$ synthesized a squarate-based, polar hydroxyl-functionalized MOF targeted as having pores of perfect size based on guidance from previous screenings. $^{4}$ The authors refer to the MOF as MOF 1a in the dehydrated form, and as MOF 1 in the hydrated form, and we shall do the same. To our knowledge it has the best recorded experimental Xe/Kr selectivity of any MOF, of 69.7 at 1 bar as calculated from single-component isotherms.

Based on examination of the structures of the MFM MOFs in the context of previously identified promising materials and structure–function relationships, we propose adsorptive separation of Xe/Kr gas mixtures as an additional function of the family. To ascertain the usefulness of the series, as well as to determine whether and to what extent any individual MFM MOFs stand out among the rest, in this work we predict computationally xenon and krypton gas uptakes under selected industrially relevant conditions, as well as structural properties, and infinite dilution properties. We show a promising performance, particularly for MFM-138. We note that the entire family is present in common materials databases such as the Cambridge Structural Database: $^{32}$ they are likely to have formed a part of previous screenings which took their structures from available databases $^{5}$ and may also have been generated as part of screenings which created their own databases using algorithmic methods. $^{4}$ This means that initial computational data on their Xe and Kr uptake is likely to exist in some form. However, by the nature of high-throughput screening studies, isolated data on individual structures is not readily available in the literature except for those few materials picked out as the best-performing, so it is not possible to simply lift Xe/Kr uptake data for the MFM MOFs from these works. In any case, we now consider the MOFs in greater detail than the early stages of a screening. This is, of course, to say that it is known that the MFM family has not previously been identified as among the handful of top performers. We consider the series for expansion of their existing functions: we seek high Xe selectivity but do not make the requirement for it to be the highest on record.

### RESULTS AND DISCUSSION

Structural Analysis. An overwhelming common thread among Xe/Kr separation studies, $^{14,19,27}$ confirmed on a statistical scale by high-throughput screenings, $^{4,5}$ is the benefit of narrow channels within which Xe-framework interactions

![](./images/864984454534266943_3.jpg)

**Figure 1.** Top: Diagram of pore morphology showing pore limiting diameter (PLD) in red and largest cavity diameter (LCD) in blue: (a) small value of LCD/PLD ratio; (b) large value of LCD/PLD ratio. Bottom: Periodic structure of (c) SBMOF-1 which performs well for Xe/Kr separation⁹ (LCD/PLD = 1.36),⁷ and (d) LIPQIL MOF not known for good Xe/Kr separation performance (LCD/PLD = 4.4).

may be optimized. If a pore is only very slightly larger than a Xe atom (pore limiting diameter (PLD) slightly larger than 3.96 Å²⁰), Xe can experience interactions with the framework on multiple sides at once. Similarly, pore morphology, described by the largest cavity diameter/pore limiting diameter (LCD/PLD) ratio, is shown to be important.⁴ A MOF with a low LCD/PLD ratio (between 1 and 2) is mostly uniformly tubular, whereas a higher ratio indicates large cavities connected by narrow channels. This is illustrated in Figure 1, with SBMOF-1 as an example of a MOF with LCD/PLD close to 1 and an MOF from the CoRE MOF database⁷ with the identifying code LIPQIL (LCD/PLD = 4.4) as an example of a MOF with much larger LCD than PLD. The chemical groups on the pore walls are also relevant. Certain types of functionalization have been shown to be effective Xe binding sites, notably polar groups (e.g. OH), as in MOF 1a reported by Li et al.,³¹ and groups composed of aromatic rings or otherwise interacting via $\pi$ clouds,³³,³⁴ as in SBMOF-1.⁹ In any case, it is favorable for the functionality to exist along the inside of 2D channels, forming a dense wall of chemical interactions.⁵

We examine the structures of the MFM MOFs in this context.

As mentioned, the MFM family is based on the structure of MFM-136 whose ligands are composed of amide, phenyl, pyrimidine, and isophthalate functionalities. For MFM-137 and MFM-138, the amide group of MFM-136 is replaced with an alkyne and a further phenyl ring, respectively. For MFM 126–128, the ligand is shortened by removal of a phenyl ring. The pore structures are illustrated in Figure 2. It is evident that the channels are composed of walls of aromatic rings, along with other fuctional groups which may be favorable for Xe adsorption.

We calculate structural data (pore diameter, surface area, and volume) using the Zeo++ software package,³⁵ which uses purely geometrical probes to sample a structure's Voronoi network. The PLD and LCD are calculated if we define the acronyms earlier, along with the ratio LCD/PLD (Figure 3, and Supporting Information). We observe low PLD, with LCD/PLD ratio which is fairly low, but not below 2: the series contains MOFs which possess some very narrow channels, where Xe adsorption may be achieved very effectively. Other parts of the channels are not as strictly narrow, potentially allowing adsorption of krypton to compete in some areas of the MOF pores.

We note that four MOFs, MFM-126, MFM-128, MFM-137, and MFM-138, possess PLD smaller than the kinetic diameter of Xe. This does not prevent simulation of adsorption as long as at least part of the pore is large enough to admit the guest (as is the case here) since the GCMC simulations take no account of a guest's journey to an adsorption site. This also does not preclude Xe or Kr adsorption experimentally if we assume that the MOFs display some flexibility to allow guests into the pores. All of the MOFs have previously been shown experimentally to adsorb CO₂ and CH₄,¹¹ which are also larger than some of the smaller values of PLD. A similar effect has previously been observed and explained using MOF flexibility by Chen et al.²⁷ for Xe in the organic cage CC3. In this case, the authors used molecular dynamics simulations of the framework to define a pore-limiting envelope which took into account vibrational motion of the cage and was large enough to admit the relevant gases with windows “open” for only a small fraction of the time.

Surface areas are calculated using Monte Carlo sampling of a probe of set radius inside the framework's Voronoi network and are compared to published experimental Brunauer–Emmett–Teller (BET)³⁶ surface areas.¹¹ Experimental BET surface areas are, in this case and commonly, measured using N₂ adsorption isotherms, so a probe of the kinetic diameter of N₂ (3.64 Å)³⁷ is used to facilitate the comparison. Both accessible surface area (ASA) and nonaccessible surface area (NASA) are initially calculated. Since we consider the MOFs to be able to admit molecules some degree larger than their PLD, the pertinent value here is the total surface area, the sum of the ASA and NASA, which is plotted against experimental BET surface area¹¹ in Figure 4. Individual ASA and NASA

![](./images/864984454534266943_4.jpg)

Figure 2. Structure of the pores and ligands of the MFM MOFs family.

values are given in the Supporting Information. The geo- metrical surface areas are very close to the experimental values, validating the choice of method. This is with the exception of MFM-126, whose experimental surface area is much lower than that predicted computationally. It is also much lower than the other surface areas in the series, and we suggest that there may have been some structural collapse or other defects acting to reduce the available area in the experimental sample used for the BET measurements. The high surface area of a MOF is a celebrated property, which can be instrumental in maximizing uptake capacities. Increasing the surface area up to an optimal point $(2500-3000\ \text{m}^2\ \text{g}^{-1}$ for methane$)^6$ maximizes storage capacity before the capacity begins to reduce as surface area increases further. For separation applications, the total storage

![](./images/864984454534266943_5.jpg)

Figure 3. Bar charts showing the pore diameters of the MFM MOFs. Left: Pore-limiting diameter (blue) and largest cavity diameter (orange), along with horizontal lines showing the kinetic diameters of Xe and Kr.²⁰ Right: LCD/PLD ratio (green).

![](./images/864984454534266943_6.jpg)

Figure 4. Plot of computational total surface areas (this work) against experimental BET surface areas¹¹ for the MFM MOFs. Also displayed is the line $y = x$ (black).

capacity offered by high surface area is far from the only consideration. Indeed, high capacity can be accompanied by reduced separation ability, although high capacity coexisting with selectivity is clearly beneficial.

High volume in a MOF can allow high uptake at high pressure, although at low pressure it can go hand in hand with larger pores and reduced surface interactions, reducing uptake. The larger pores often associated with high volume can also be detrimental to selectivity, although the effect on behavior of the interplay between structural properties is case dependent. Geometric accessible volumes, calculated using Monte Carlo sampling of a probe on a Voronoi network, are shown in Figure 5. A zero radius probe is used, so all of the volume is accessible. The volume is larger for those MOFs in the series which contain longer ligands. Of particular note is the volume of MFM-137, the highest in the series.

Figure 5 also shows total probe-occupiable helium void fraction for the series. Void fraction, determined by multiplication of pore volume by a framework's density, is a necessary quantity for conversion of absolute gas uptakes measured computationally to experiment-equivalent excess uptakes.³⁸ Void fraction has commonly been calculated using Widom insertion³⁹ and force-field methods with a He probe. An assessment of void fraction calculation methods by Ongari et al.⁴⁰ concluded that better agreement with experiment is given by accessible probe-occupiable volume calculated using a geometric method with a N₂ probe and considering the volume accessible to the whole of the probe (hence accessible probe-occupiable). Since the method is geometric, it is not reliant on force-field parameters or dependent on temperature. The conclusions drawn by Ongari et al. are not fully applicable here. As we have made the assumption that the MOFs can

![](./images/864984454534266943_7.jpg)

Figure 5. Bar charts showing volume of the MFM MOFs. Left: Accessible volume calculated using a zero-radius probe (blue). Right: Total probe-occupiable void fraction calculated using a helium-radius probe.

![](./images/864984454534266943_8.jpg)

Figure 6. Xe and Kr adsorption isotherms of the MFM MOFs calculated up to 10 bar pressure at 273 K (left) and 298 K (right). Top: Single-component adsorption isotherms.Center: 50/50 mixture adsorption isotherms. Bottom: 20/80 mixture adsorption isotherms. Xe uptake: closed circles, solid lines. Kr uptake: open circles, dashed lines.

adsorb gases larger than their PLD, accessible pore volume alone with a probe of comparable size to the gases in question is clearly insufficient to model the situation. Here, the geometry-based PO volume is used, but total volume, accessible plus nonaccessible, is considered instead of accessible only. A He probe is used, both because the smaller probe may capture more of the supposedly inaccessible volume than $N_2$, and because He is a common choice for void fraction calculations. This was compared to force-field based void fraction methods and yielded negligible differences in calculated uptake.

Xe and Kr Uptake, Selectivity, and Binding Affinity.
Adsorption isotherms, heats of adsorption, and Henry constants are calculated for the MFM family of MOFs using the Grand Canonical Monte Carlo (GCMC) and Widom insertion$^{39}$ methods available in the RASPA software package.$^{38}$ Frameworks are assumed to be rigid, which is judged to be appropriate to a useful degree of accuracy, as adsorption simulations are produced at 273 and 298 K. The rigid approximation is common in isotherm modeling,$^{41}$ although rigid frameworks are unlikely to be appropriate at elevated temperatures, and even at room temperature some structures experience appreciable flexibility.$^{42}$ This approximation, however, drastically reduces computational and development cost.

![](./images/864984454534266943_9.jpg)
![](./images/864984454534266943_10.jpg)

Figure 7. Xe selectivity of MFM-138 (red) and average Xe selectivity of the remaining MFM MOFs (black) calculated up to 10 bar pressure at 273 K (left) and 298 K (right) Dashed line: 20/80 mixture. Solid line: 50/50 mixture. Error bars for MFM-138 selectivity are given.

<table>
<caption>Table 1. Highest and the Lowest Values of Selectivity in the MFM MOFs Series</caption>
<tbody>
<tr>
<td rowspan="2">
</td>
<td colspan="4">50/50 mixture</td>
<td colspan="4">20/80 mixture</td>
</tr>
<tr>
<td colspan="2">0.01 bar</td>
<td colspan="2">10 bar</td>
<td colspan="2">0.01 bar</td>
<td colspan="2">10 bar</td>
</tr>
<tr>
<td>
</td>
<td>$S_{ij}$</td>
<td>MOF</td>
<td>$S_{ij}$</td>
<td>MOF</td>
<td>$S_{ij}$</td>
<td>MOF</td>
<td>$S_{ij}$</td>
<td>MOF</td>
</tr>
<tr>
<td>$T = 273$ K</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>highest $S_{ij}$</td>
<td>51.98 $\pm$ 6</td>
<td>MFM-127</td>
<td>9.22 $\pm$ 0.2</td>
<td>MFM-137</td>
<td>27.26 $\pm$ 2</td>
<td>MFM-127</td>
<td>10.12 $\pm$ 0.2</td>
<td>MFM-138</td>
</tr>
<tr>
<td>lowest $S_{ij}$</td>
<td>30.39 $\pm$ 3</td>
<td>MFM-128</td>
<td>4.14 $\pm$ 0.1</td>
<td>MFM-126</td>
<td>19.56 $\pm$ 2</td>
<td>MFM-137</td>
<td>5.01 $\pm$ 0.08</td>
<td>MFM-126</td>
</tr>
<tr>
<td>$T = 298$ K</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>highest $S_{ij}$</td>
<td>52.16 $\pm$ 10</td>
<td>MFM-127</td>
<td>8.37 $\pm$ 0.08</td>
<td>MFM-138</td>
<td>23.33 $\pm$ 3</td>
<td>MFM-138</td>
<td>8.93 $\pm$ 0.1</td>
<td>MFM-138</td>
</tr>
<tr>
<td>lowest $S_{ij}$</td>
<td>35.29 $\pm$ 4</td>
<td>MFM-128</td>
<td>3.99 $\pm$ 0.07</td>
<td>MFM-126</td>
<td>15.24 $\pm$ 3</td>
<td>MFM-137</td>
<td>4.85 $\pm$ 0.06</td>
<td>MFM-126</td>
</tr>
</tbody>
</table>

Classical force fields are used considering only non-bonded interactions (Coulomb and van der Waals), with truncated potentials and a van der Waals cutoff of 12.0 Å; guest−guest and guest−host interactions are included, with no host−host interactions required. For framework atoms, van der Waals interactions are described using Lennard-Jones parameters from the Dreiding force field,⁴³ except in the case of copper, for which Dreiding force field parameters are unavailable and parameters from the universal force field (UFF)⁴⁴ are used instead. Similar combination of UFF and Dreiding parameters has previously been used to good effect in terms of reproducing experimental data,³⁰,⁴⁵ and in tests on MFM-136 this approach performed slightly better overall than purely UFF parameters. Guest atoms are described using parameters taken from Hirschfelder et al. (Xe)⁴⁶ and from Talu and Myers (Kr).⁴⁷ The computational method of calculating gas uptake is verified for all MFM MOFs against the existing experimental data¹¹ for CO₂ and CH₄. It is additionally verified for the guests Xe and Kr against experimental data⁴⁸⁻⁵¹ for MOF-505 and IRMOF-1 (see the Supporting Information). Since there is no current experimental data for adsorption of Xe and Kr in the MFM series, it is not yet possible to verify the method directly for the systems in question.

Xe and Kr uptake isotherms up to 10 bar at 273 and 298 K are shown in Figure 6. Isotherms obtained from single component simulations are displayed, along with those from binary mixture simulations with Xe/Kr ratios of both 50/50 and 20/80. In each case a total of 25,000 initialization cycles and 25,000 production cycles are used. A representative input file for the simulations is included in the Supporting Information. The 20/80 ratio is selected for its relevance to industrial separations, and the 50/50 ratio for ease of comparison to other selectivity measures. Further gas ratios could also be instructive to consider, such as the 10:1 Kr:Xe ratio of UNF, but the 50/50 and 20/80 ratios are judged to be sufficiently representative. Xenon is adsorbed more readily than krypton for the whole series, and when guests are allowed to compete for binding sites a higher uptake of Xe than Kr is observed at all pressures considered. This remains the case even with significantly more Kr than Xe in the gas mixture. The single component isotherms show Kr adsorption overtaking Xe at sufficiently high pressure and low temperature. Here, saturation is approached and the limitations of volume become relevant, the smaller size of Kr allowing higher molar quantities to be adsorbed. The difference in behavior between the two temperatures considered is familiar, capacity increasing as guest atoms lose kinetic energy and interactions with pore walls dominate.

Using binary mixture isotherms, preferential adsorption can be quantified by the metric selectivity, $S_{i/j}$, calculated as⁵²,⁵³

$$
S_{i/j} = \frac{q_i y_j}{q_j y_i} \tag{1}
$$

where $q_i$ is the quantity of component $i$ in the adsorbed phase and $y_i$ is the mole fraction of component $i$ in the gas phase. Xenon selectivity for each MFM MOF is calculated using the 20/80 and the 50/50 Xe/Kr mixture. In each case, MFM-138 displays the highest or very close to the highest Xe selectivity over the full pressure range, while MFM-137 is its closest contender, with very similar or slightly higher selectivity at high

pressure. At 273 and 298 K, the Xe selectivity of MFM-138 in equilibrium with both gas mixtures is plotted against pressure in Figure 7. Figure 7 also includes the average selectivity of the other five MFM MOFs. Individual selectivity plots for the whole series are given in the Supporting Information. All structures display higher selectivity at very low pressure, dropping rapidly before 1 bar is reached, and leveling off as pressure further increases. MFM-137 and MFM-138 experience a selectivity local minimum at pressures between 0 and 1 bar in some cases.

To illustrate the range of selectivity values observed, the two extreme pressure points, 0.01 and 10 bar, are highlighted in Table 1 for each combination of temperature and gas mixture. The highest and the lowest selectivity displayed by an individual MOF in the series in each case are given. These values do not compete with the best literature benchmarks $^{9,31}$ for the highest observed or predicted Xe/Kr selectivity of a material. However, they show high selectivity at low pressure for the whole series, and appreciable and practical behavior at higher pressures. This may be added to the already established separation applications of the family. $^{11}$ In particular, MFM-138 stands out for the best Xe-selective behavior predicted, while MFM-126 has low Xe uptake compared to the rest of the series, translating to low selectivity, with MFM-126 being the least selective MOF at 10 bar for every case.

In addition to selectivity, it is instructive to consider the magnitude of guest uptake. Although this metric is not as important for separation applications as for storage, it can be decisive in determining the efficiency of a separation and whether use of a given framework is practically viable. Total Xe uptake in the MFM series is predicted to compare well with many previously identified promising materials. From singlecomponent simulations (Figure 6), Xe uptake at saturation is predicted to be between 7.56 and $9.01 \mathrm{mmol} \mathrm{g}^{-1}$ at $273 \mathrm{~K}$ and between 6.96 and $8.32 \mathrm{mmol} \mathrm{g}^{-1}$ at $298 \mathrm{~K}$. This competes well with previous relevant Xe uptakes, including those recently identified as having exceptional selectivities. $^{9,31}$ Of the two MOFs with published selectivity values close to 70, the first, SBMOF-1, has an experimental Xe uptake around $1.4 \mathrm{mmol}$ $\mathrm{g}^{-1}$ at $298 \mathrm{~K}$ and 1 bar, approaching saturation. $^{9}$ Under the same conditions, the second, the squarate-based MOF 1a published by Li et al. $^{31}$ has a reported Xe uptake of $66.1 \mathrm{~cm}^{3}$ $\mathrm{cm}^{-3}$, which is equivalent to $1.35 \mathrm{mmol} \mathrm{g}^{-1}$. In general, high literature Xe uptakes $^{14}$ are between 4 and $6 \mathrm{mmol} \mathrm{g}^{-1}$. We note that computational values may be often behave as an upper bound for experimental performance and that our predicted binary mixture uptakes are reduced compared to the given single component values. Although in practical separation applications Xe uptake is likely to be lower, the MFM MOF series competes very well with leading structures for total Xe uptake.

Examining both single-component and binary-mixture data, insight is available into the usefulness of single component isotherms as a cheaper approximation for MOF/gas mixture behavior. The single-component approximation is particularly pertinent for experimental studies, where mixture isotherms are less accessible. The single component isotherms calculated here accurately predict higher xenon than krypton uptake at low to medium pressures and thus that the MOFs are xenonselective. They additionally prove to be a good qualitative approximation for uptake of xenon, the dominant guest, in a 50/50 mixture. For Xe, the single component and the 50/50 isotherms follow a very similar shape, and the singlecomponent isotherms overestimate total Xe uptake by only around $1 \mathrm{mmol} \mathrm{g}^{-1}$. From the $50 / 50$ mixture simulations, it is apparent that a large amount of krypton adsorption that would occur in equilibrium with pure krypton gas is blocked by the presence of xenon. Krypton adsorption in the 50/50 mixture fails to exceed $1.5 \mathrm{mmol} \mathrm{g}^{-1}$, and single-component krypton adsorption overpredicts this by $3-5$ times. The unequal $20 / 80$ mixture isotherms can be less directly compared to singlecomponent results, though for both gases they too follow a broadly similar shape to the single-component isotherms. Both mixture isotherms predict markedly lower total uptake than the simple sum of xenon and krypton single-component uptake, particularly the $20 / 80$ mixture in which the less readily adsorbed krypton is the more prevalent element in the gas phase. This is a natural consequence of the competition of the two species for the same adsorption sites but could not be quantified from single component isotherms. The single component approximations are thus demonstrated to have qualitative predictive power for binary mixture calculations for these two gases before saturation is reached, but their quantitative predictions are limited.

Heat of adsorption, $Q_{s t}$, is a useful measure of strength of binding between host and guest. In the limit of infinite dilution, heat of adsorption can be determined using Widom insertion $^{39}$ and is done here using 100,000 Monte Carlo cycles. Infinite dilution $Q_{s t}$ values (Table 2) for both Xe and $\mathrm{Kr}$ are similar across the MFM series, with the highest heat of adsorption for xenon being $28.40 \pm 0.1 \mathrm{~kJ} \mathrm{~mol}^{-1}$ for MFM138. This fits in favorably with typical literature values of the heat of adsorption for $\mathrm{Xe}$, although values above $30 \mathrm{~kJ} \mathrm{~mol}^{-1}$ have been observed for materials with particular Xe affinity. ${ }^{14,31,54}$ It is thus clear that the MOFs in the series contain favorable binding sites for xenon. Heat of adsorption values for $\mathrm{Kr}$ are markedly lower, in line with the observed lowpressure selectivity. Although comparatively low, these remain fairly high in absolute terms, showing that the adsorption sites in the series also possess appreciable affinity toward krypton.

<table>
 <thead>
  <tr>
   <th colspan="3">Table 2. Heat of Adsorption, $Q_{st}$, at Infinite Dilution for Xe and Kr at 298 K</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    MOF
   </td>
   <td>
    $Q_{st}$(Xe) (kJ mol-1)
   </td>
   <td>
    $Q_{st}$(Kr) (kJ mol-1)
   </td>
  </tr>
  <tr>
   <td>
    MFM-126
   </td>
   <td>
    26.31 ± 0.06
   </td>
   <td>
    18.95 ± 0.02
   </td>
  </tr>
  <tr>
   <td>
    MFM-127
   </td>
   <td>
    25.29 ± 0.02
   </td>
   <td>
    18.22 ± 0.2
   </td>
  </tr>
  <tr>
   <td>
    MFM-128
   </td>
   <td>
    26.44 ± 0.01
   </td>
   <td>
    19.03 ± 0.04
   </td>
  </tr>
  <tr>
   <td>
    MFM-136
   </td>
   <td>
    25.74 ± 0.1
   </td>
   <td>
    18.62 ± 0.1
   </td>
  </tr>
  <tr>
   <td>
    MFM-137
   </td>
   <td>
    25.08 ± 0.01
   </td>
   <td>
    18.54 ± 0.1
   </td>
  </tr>
  <tr>
   <td>
    MFM-138
   </td>
   <td>
    28.40 ± 0.1
   </td>
   <td>
    20.34 ± 0.01
   </td>
  </tr>
 </tbody>
</table>

A second measure of binding affinity, the Henry constant for a host/guest system, is equal to the gradient of the adsorption isotherm at infinite dilution, as shown by eq 2, where $X$ is the gas uptake, $P$ is the pressure, and $K_{H}$ is the Henry constant:

$$
X=K_{\mathrm{H}} P \tag{2}
$$

For two gases $i$ and $j$, the ratio of the Henry constants $K_{\mathrm{H}}(i)$ $/ K_{\mathrm{H}}(j)$ can be used as a somewhat limited measure of selectivity for gas $i$. Henry constant and selectivity at infinite dilution were calculated for each MOF using Widom insertion methods at $298 \mathrm{~K}$ (Table 3). The selectivity values may be compared to those obtained using binary mixture isotherms, which are also displayed for $298 \mathrm{~K}$ in Table 3. At low loading, a generally similar trend is followed between Henry and 20/80

Table 3. Henry Constant and Xe Selectivity at Infinite Dilution at 298 K; Selectivity for 50/50 and 20/80 Binary Mixture at 0.01 bar and at 10 bar at the Same Temperature

<table>
<thead>
<tr>
<th rowspan="2">MOF</th>
<th rowspan="2">$K_{H}(Xe)$<br>$(mol\ kg^{-1}Pa^{-1}×10^{-5})$</th>
<th rowspan="2">$K_{H}(Kr)$<br>$(mol\ kg^{-1}Pa^{-1}×10^{-5})$</th>
<th rowspan="2">$K_{H}(Xe)/K_{H}(Kr)$</th>
<th colspan="4">$S_{Xe/Kr}$</th>
</tr>
<tr>
<th colspan="2">50/50</th>
<th colspan="2">20/80</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>0.01 bar</th>
<th>10 bar</th>
<th>0.01 bar</th>
<th>10 bar</th>
</tr>
</thead>
<tbody>
<tr>
<td>MFM-126</td>
<td>22.2 ± 0.1</td>
<td>2.23 ± 0.009</td>
<td>9.96 ± 0.0008</td>
<td>51.65±9</td>
<td>3.99±0.07</td>
<td>19.15±3</td>
<td>4.85±0.06</td>
</tr>
<tr>
<td>MFM-127</td>
<td>20.8 ± 0.04</td>
<td>2.08 ± 0.006</td>
<td>9.98 ± 0.0003</td>
<td>52.16 ± 10</td>
<td>5.73 ± 0.1</td>
<td>20.36 ± 2</td>
<td>6.57 ± 0.06</td>
</tr>
<tr>
<td>MFM-128</td>
<td>24.2 ± 0.1</td>
<td>2.27 ± 0.005</td>
<td>10.66 ± 0.0005</td>
<td>35.29 ± 4</td>
<td>4.96 ± 0.05</td>
<td>19.01 ± 0.9</td>
<td>6.35 ± 0.05</td>
</tr>
<tr>
<td>MFM-136</td>
<td>19.9 ± 0.1</td>
<td>2.15 ± 0.01</td>
<td>9.34 ± 0.001</td>
<td>46.21 ± 7</td>
<td>5.19 ± 0.08</td>
<td>18.34 ± 3</td>
<td>6.19 ± 0.03</td>
</tr>
<tr>
<td>MFM-137</td>
<td>16.5 ± 0.1</td>
<td>1.95 ± 0.01</td>
<td>8.46 ± 0.002</td>
<td>40.64 ± 2</td>
<td>7.96 ± 0.1</td>
<td>15.24 ± 3</td>
<td>8.37 ± 0.09</td>
</tr>
<tr>
<td>MFM-138</td>
<td>36.0 ± 0.1</td>
<td>3.08 ± 0.02</td>
<td>11.68 ± 0.0008</td>
<td>45.91 ± 5</td>
<td>8.37 ± 0.08</td>
<td>23.33 ± 3</td>
<td>8.93 ± 0.1</td>
</tr>
</tbody>
</table>

mixture selectivities, with MFM-138 standing out as having notably the largest selectivity in both cases. The remaining MOFs display only small variation, reducing in Henry selectivity in the order MFM-128, MFM-127 MFM-126, MFM-136, and MFM-137, and reducing in 20/80 mixture selectivity in the order MFM-127, MFM-126, MFM-128, MFM-136, and MFM-137. The values of Henry selectivity underestimate those of 20/80 mixture selectivity but reproduce the trends well, having only a small discrepancy in the order of the MOFs, which is unsurprising over such a narrow range. At 0.01 bar, both Henry selectivity and 20/80 mixture selectivity are significantly lower than 50/50 mixture selectivity. For a 50/50 gas mixture at very low pressure, the amount of krypton adsorbed is very low, which drives selectivity up. A different order is also observed, being MFM-127, MFM-126, MFM-136, MFM-138, MFM-137, and MFM-128. We note that the very low krypton uptakes observed lead to high errors in selectivity for the 50/50 mixture at 0.01 bar. However, even if the selectivity values were the lowest allowed within their errors, 50/50 low pressure selectivities would be notably higher than infinite dilution Henry selectivities and indeed 20/80 low pressure selectivities.

As pressure increases, the effect causing unusually high selectivity for a 50/50 mixture is no longer seen. Table 3 shows this result for both compositions of binary mixture at 10 bar, with MFM-138 having the highest selectivity. For the remaining MOFs at 10 bar, the order of selectivity values is altered compared to low-pressure selectivity for both 50/50 and 20/80 mixtures. The resulting order of selectivity, however, is very similar for the two gas mixtures. Most notably, in both cases MFM-137 goes from being the least or almost the least selective MOF at low pressure to the second most selective at higher pressure. At higher pressure, available volume becomes more important, and MFM-137, with the highest available volume, becomes relatively more selective.

We have considered here adsorption at commonly studied temperatures applicable to the majority of relevant use cases. Under select circumstances, it may be desired to pursue gas separations under extreme conditions, an example being to make a process amenable to the high operating temperatures of an MSR, which can reach 600−800 °C.¹⁶ Such an aim is not without significant challenges,⁵⁵ not least that the stability, uptake, and often selectivity of MOFs degrade with temperature. The idea is impossible in the case of TSA, as operation at elevated temperatures is antithetical to the basis of the process. However, PSA and membrane separations, and related methods, may be carried out at high temperature using the correct materials.⁵⁶⁻⁵⁹ No MOF has been discovered with thermal stability reaching 800 °C, but the usefulness of the MFM MOFs at some intermediate temperature is not inconceivable. For the interested reader, we provide an initial approximate quantification based on Henry constants of selectivity trends of the MFM MOFs as temperature increases in the Supporting Information.

The locations of adsorption within a MOF framework can give information on the nature of binding and site affinity for guests. Such information can determine whether binding behavior follows similar trends to those previously observed in well-performing structures. To this end, the probability density of the guests within the framework over the entire duration of the Monte Carlo simulations may be calculated using kernel density estimation. This is done for MFM-126 as an example. For the case of a 20/80 Xe/Kr mixture at 10 bar and 298 K, probability density distributions for Xe and Kr are plotted alongside framework atom positions and shown in Figure 8. Viewed from the z-direction and looking into the pores, both gases appear to display adsorption primarily in pore centers, in line with literature findings of noble gas adsorption involving interaction with all sides of the pore.⁴,⁵ Viewed from the x-direction and toward the side of the pores, it is clear that there are particular preferential adsorption sites. These do not all fall directly in the center, but many appear to facilitate interaction with multiple parts of the framework at once. The probability density distributions of Kr and Xe are very similar: the two gases adsorb in the same sites, so it is only the strength of this adsorption that causes the preferential binding of Xe observed in uptake magnitudes. Also in Figure 8 is a snapshot of uptake in MFM-126 at one Monte Carlo simulation step for the 20/80 mixture at 10 bar and 298 K. Here, both Xe (green) and Kr (purple) are observed throughout the pores.

### CONCLUSIONS
The MFM series of six robust, experimentally synthesized Cu-based MOFs has been computationally assessed for its Xe/Kr uptake and separation properties. These MOFs have already been synthesized and shown to have uses for other separations, so finding additional applications for them as multiuse materials is desirable. The MOFs have all been shown to display fairly substantial selectivity for Xe over Kr. Their particularly impressive combination of selectivity and high total uptakes makes them promising separation candidates. Comparison to literature has allowed the MFM MOFs series as a whole to be established within currently observed trends for Xe/Kr separation. It has been possible to identify MFM-138 MOF as the most promising structure. The best-performing MOF of the series possesses the longest, thinnest pores, decorated with the most aromatic rings, in line with similar previous observations of other structures. Additionally,

![](./images/864984454534266943_11.jpg)

Figure 8. Visualization of Xe and Kr binding for a 20/80 Xe/Kr mixture in MFM-126 at 10 bar and 298 K. Top: Probability density distributions of Kr (purple) and Xe (green), viewed along the z-direction (left) and x-direction (right), with axis dimensions in Å. Bottom: Snapshot of loading of Kr (purple) and Xe (green) at one Monte Carlo step during the simulation.

visualization of the locations of guest adsorption has shown appreciable Xe and Kr adsorption at the centers of pores and interactions on many sides with the frameworks.

Further experimental study is required to establish the Xe/ Kr separation properties of the MFM MOFs. Computational uptake predictions are likely to be a theoretical upper bound for experimentally observed behavior. Although experimental behavior has been demonstrated for other separations, their experimental Xe/Kr separation behavior remains to be seen.

## ASSOCIATED CONTENT

### Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.2c02237.

Numerical structural data, validation of methodology, individual selectivity plots, discussion of temperature effects, and a representative input file (PDF)

### AUTHOR INFORMATION

#### Corresponding Author
Elena Besley – School of Chemistry, University of Nottingham, Nottingham NG7 2RD, U.K.; orcid.org/0000-0002-9910-7603; Email: elena.besley@nottingham.ac.uk

#### Authors
Isabel Cooley – School of Chemistry, University of Nottingham, Nottingham NG7 2RD, U.K.
Louise Efford – School of Chemistry, University of Nottingham, Nottingham NG7 2RD, U.K.

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.2c02237

### Notes
The authors declare no competing financial interest.

### ACKNOWLEDGMENTS
E.B. acknowledges the awards of a Royal Society Wolfson Fellowship and a Royal Society Leverhulme Trust Senior Research Fellowship for financial support.

### REFERENCES
(1) Yaghi, O. M.; Li, G.; Li, H. Selective Binding and Removal of Guests in a Microporous Metal-Organic Framework. *Nature* 1995, 378, 703−706.
(2) Düren, T.; Sarkisov, L.; Yaghi, O. M.; Snurr, R. Q. Design of New Materials for Methane Storage. *Langmuir* 2004, 20, 2683−2689.
(3) Chen, B.; Ockwig, N. W.; Millward, A. R.; Contreras, D. S.; Yaghi, O. M. High H2 Adsorption in a Microporous Metal-Organic Framework with Open Metal Sites. *Ang. Chem. Int. Ed.* 2005, 44, 4745−4749.
(4) Sikora, B. J.; Wilmer, C. E.; Greenfield, M. L.; Snurr, R. Q. Thermodynamic Analysis of Xe/Kr Selectivity in over 137,000 Hypothetical Metal-Organic Frameworks. *Chem. Sci.* 2012, 3, 2217−2223.
(5) Simon, C. M.; Mercado, R.; Schnell, S. K.; Smit, B.; Haranczyk, M. What Are the Best Materials To Separate a Xenon/Krypton Mixture? *Chem. Mater.* 2015, 27, 4459−4475.
(6) Wilmer, C. E.; Leaf, M.; Lee, C. Y.; Farha, O. K.; Hauser, B. G.; Hupp, J. T.; Snurr, R. Q. Large-Scale Screening of Hypothetical Metal-Organic Frameworks. *Nat. Chem.* 2012, 4, 83−89.
(7) Chung, Y. G.; Haldoupis, E.; Bucior, B. J.; Haranczyk, M.; Lee, S.; Zhang, H.; Vogiatzis, K. D.; Milisavljevic, M.; Ling, S.; Camp, J. S.; et al. Advances, Updates, and Analytics for the Computation Ready, Experimental Metal Organic Framework Database: CoRE MOF 2019. *J. Chem. Eng. Data* 2019, 64, 5985−5998.
(8) Glover, J.; Besley, E. A High-Throughput Screening of Metal-Organic Framework Based Membranes for Biogas Upgrading. *Faraday Discuss.* 2021, 231, 235−257.
(9) Banerjee, D.; Simon, C. M.; Plonka, A. M.; Motkuri, R. K.; Liu, J.; Chen, X.; Smit, B.; Parise, J. B.; Haranczyk, M.; Thallapally, P. K. Metal-Organic Framework with Optimally Selective Xenon Adsorption and Separation. *Nat. Commun.* 2016, 7, 11831.
(10) Ren, E.; Coudert, F.-X. Thermodynamic Exploration of Xenon/Krypton Separation Based on a High-Throughput Screening. *Faraday Discuss.* 2021, 231, 201−223.
(11) Humby, J. D.; Benson, O.; Smith, G. L.; Argent, S. P.; Da Silva, I.; Cheng, Y.; Rudić, S.; Manuel, P.; Frogley, M. D.; Cinque, G.; et al. Host-Guest Selectivity in a Series of Isoreticular Metal-Organic Frameworks: Observation of Acetylene-to-Alkyne and Carbon Dioxide-to-Amide Interactions. *Chem. Sci.* 2019, 10, 1098−1106.
(12) Benson, O.; da Silva, I.; Argent, S. P.; Cabot, R.; Savage, M.; Godfrey, H. G.; Yan, Y.; Parker, S. F.; Manuel, P.; Lennox, M. J.; et al. Amides Do Not Always Work: Observation of Guest Binding in an Amide-Functionalized Porous Metal-Organic Framework. *J. Am. Chem. Soc.* 2016, 138, 14828−14831.
(13) Marshall, J.; Bird, A. C. A Comparative Histopathological Study of Argon and Krypton Laser Irradiations of the Human Retina. *Br. J. Opthamol.* 1979, 63, 657−668.
(14) Banerjee, D.; Simon, C. M.; Elsaid, S. K.; Haranczyk, M.; Thallapally, P. K. Xenon Gas Separation and Storage Using Metal-Organic Frameworks. *Chem.* 2018, 4, 466−494.
(15) Sanders, R. D.; Ma, D.; Maze, M. Xenon: Elemental Anaesthesia in Clinical Practice. *Br. Med. Bul.* 2005, 71, 115−135.
(16) Degueldre, C.; Dawson, R.; Cooley, I.; Besley, E. Fission Gas Released from Molten Salt Reactor Fuel: the Case of Noble Gas Short Life Radioisotopes for Radiopharmaceutical Application. *Med. Novel Technol. Devices* 2021, 10, 100057.
(17) Kerry, F. G. *Industrial Gas Handbook: Gas Separation and Purification*, 1st ed.;CRC Press: Boca Raton, FL, 2007; p 129.
(18) Ianovski, D.; Munakata, K.; Kanjo, S.; Yokoyama, Y.; Koga, A.; Yamatsuki, S.; Tanaka, K.; Fukumatsu, T.; Nishikawa, M.; Igarashi, Y. Adsorption of Noble Gases on H-Mordenite. *J. Nucl. Sci. Technol.* 2002, 39, 1213−1218.
(19) Feng, X.; Zong, Z.; Elsaid, S. K.; Jasinski, J. B.; Krishna, R.; Thallapally, P. K.; Carreon, M. A. Kr/Xe Separation over a Chabazite Zeolite Membrane. *J. Am. Chem. Soc.* 2016, 138, 9791−9794.
(20) Breck, D. W. *Zeolite Molecular Sieves: Structure, Chemistry and Use*; R.E. Krieger: Malabar, FL, 1984.
(21) Fernandez, C. A.; Liu, J.; Thallapally, P. K.; Strachan, D. M. Switching Kr/Xe Selectivity with Temperature in a Metal-Organic Framework. *J. Am. Chem. Soc.* 2012, 134, 9046−9049.
(22) Wu, T.; Feng, X.; Elsaid, S. K.; Thallapally, P. K.; Carreon, M. A. Zeolitic Imidazolate Framework-8 (ZIF-8) Membranes for Kr/Xe Separation. *Ind. Eng. Chem. Res.* 2017, 56, 1682−1686.
(23) Castellani, F. F.; Curzio, G. G.; Gentil, A. F. Krypton Diffusion in Granular Charcoal. *Anal. Chem.* 1976, 48, 599−600.
(24) Thallapally, P. K.; Grate, J. W.; Motkuri, R. K. Facile Xenon Capture and Release at Room Temperature using a Metal-Organic Framework: a Comparison with Activated Charcoal. *Chem. Commun.* 2012, 48, 347−349.
(25) Jameson, C. J.; Jameson, A. K.; Lim, H.-M. Competitive Adsorption of Xenon and Krypton in Zeolite NaA: 129Xe Nuclear Magnetic Resonance Studies and Grand Canonical Monte Carlo Simulations. *J. Chem. Phys.* 1996, 104, 1709.
(26) Kuznicki, S. M.; Ansón, A.; Koenig, A.; Kuznicki, T. M.; Haastrup, T.; Eyring, E. M.; Hunter, D. Xenon Adsorption on Modified ETS-10. *J. Phys. Chem. C* 2007, 111, 1560−1562.
(27) Chen, L.; Reiss, P. S.; Chong, S. Y.; Holden, D.; Jelfs, K. E.; Hasell, T.; Little, M. A.; Kewley, A.; Briggs, M. E.; Stephenson, A.; et al. Separation of Rare Gases and Chiral Molecules by Selective Binding in Porous Organic Cages. *Nat. Mater.* 2014, 13, 954−960.
(28) Patil, R. S.; Banerjee, D.; Simon, C. M.; Atwood, J. L.; Thallapally, P. K. Noria: A Highly Xe-Selective Nanoporous Organic Solid. *Chem.—Eur. J.* 2016, 22, 12618−12623.
(29) Subrahmanyam, K. S.; Spanopoulos, I.; Chun, J.; Riley, B. J.; Thallapally, P. K.; Trikalitis, P. N.; Kanzatzidis, M. G. Chalcogenide Aerogels as Sorbents for Noble Gases (Xe, Kr). *ACS Appl. Mater. Interfaces* 2017, 9, 33389−33394.
(30) Ryan, P.; Farha, O. K.; Broadbelt, L. J.; Snurr, R. Q. Computational screening of metal-organic frameworks for xenon/krypton separation. *AIChE J.* 2011, 57, 1759−1766.
(31) Li, L.; Guo, L.; Zhang, Z.; Yang, Q.; Yang, Y.; Bao, Z.; Ren, Q.; Li, J.; Robust Square-Based Metal-Organic, A. Framework Demonstrates Record-High Affinity and Selectivity for Xenon over Krypton. *J. Am. Chem. Soc.* 2019, 141, 9358−9364.
(32) Groom, C. R.; Bruno, I. J.; Lightfoot, M. P.; Ward, S. C. The Cambridge Structural Database. *Acta. Crystallogr., Sect. B: Struct. Sci.* 2016, 72, 171−179.
(33) Lawler, K. V.; Hulvey, Z.; Forster, P. M. Nanoporous Metal Formates for Krypton/Xenon Separation. *Chem. Commun.* 2013, 49, 10959−10961.


(34) Banerjee, D.; Cairns, A. J.; Liu, J.; Motkuri, R. K.; Nune, S. K.; Fernandez, C. A.; Krishna, R.; Strachan, D. M.; Thallapally, P. K. Potential of Metal-Organic Frameworks for Separation of Xenon and Krypton. *Acc. Chem. Res.* **2015**, *48*, 211–219.

(35) Willems, T. F.; Rycroft, C. H.; Kazi, M.; Meza, J. C.; Haranczyk, M. Algorithms and Tools for High-Throughput Geometry-Based Analysis of Crystalline Porous Materials. *Microporous Mesoporous Mater.* **2012**, *149*, 134–141.

(36) Brunauer, S.; Emmett, P. H.; Teller, E. Adsorption of Gases in Multimolecular Layers. *J. Am. Chem. Soc.* **1938**, *60*, 309–319.

(37) Yampolskii, Y.; Pinnau, I.; Freeman, B. D. *Materials Science of Membranes for Gas and Vapor Sepatation*; John Wiley and Sons, Ltd: Chichester, UK, 2006.

(38) Dubbeldam, D.; Calero, S.; Ellis, D. E.; Snurr, R. Q. RASPA: Molecular Simulation Software for Adsorption and Diffusion in Flexible Nanoporous Materials. *Mol. Simul* **2016**, *42*, 81–101.

(39) Widom, B. Some Topics in the Theory of Fluids. *J. Chem. Phys.* **1963**, *39*, 2808–2812.

(40) Ongari, D.; Boyd, P. G.; Barthel, S.; Witman, M.; Haranczyk, M.; Smit, B. Accurate Characterization of the Pore Volume in Microporous Crystalline Materials. *Langmuir* **2017**, *33*, 14529–14538.

(41) Glover, J.; Besley, E. In *Computer Simulation of Porous Materials: Current Approaches and Future Opportunities*; Jelfs, K., Ed.; Royal Society of Chemistry: London, 2022 Chapter 4, pp 122–214.

(42) Schneemann, A.; Bon, V.; Schwedler, I.; Senkovska, I.; Kaskel, S.; Fischer, R. A. Flexible Metal-Organic Frameworks. *Chem. Soc. Rev.* **2014**, *43*, 6062–6096.

(43) Mayo, S. L.; Olafson, B. D.; Goddard, W. A., III DREIDING: A Generic Force Field for Molecular Simulations. *J. Phys. Chem.* **1990**, *94*, 8897–8909.

(44) Rappe, A. K.; Casewit, C. J.; Colwell, K. S.; Goddard, W., III; Skiff, A. W. M. UFF, a Full Periodic Table Force Field for Molecular Mechanics and Molecular Dynamics Simulations. *J. Am. Chem. Soc.* **1992**, *114*, 10024–10035.

(45) Rana, M. K.; Koh, H. S.; Zuberi, H.; Siegel, D. J. Methane Storage in Metal-Substituted Metal-Organic Frameworks: Thermodynamics, Usable Capacity, and the impact of Enhanced Binding Sites. *J. Phys. Chem.C* **2014**, *118*, 2929–2942.

(46) Hirschfelder, J. O.; Curtiss, C. F.; Bird, R. B. *The Molecular Theory of Gases and Liquids*, 2nd ed.; Wiley: New York, 1964.

(47) Talu, O.; Myers, A. L. Reference Potentials for Adsorption of Helium, Argon, Methane, and Krypton in High-Silica Zeolites. *Colloids Surf*, A **2001**, *187–188*, 83–93.

(48) Bae, Y. S.; Hauser, B. G.; Colón, Y. J.; Hupp, J. T.; Farha, O. K.; Snurr, R. Q. High Xenon/Krypton Selectivity in a Metal-Organic Framework with Small Pores and Strong Adsorption Sites. *Microporous Mesoporous Mater.* **2013**, *169*, 176–179.

(49) Pawsey, S.; Moudrakovski, I.; Ripmeester, J.; Wang, L.-Q.; Exarhos, G. J.; Rowsell, J. L. C.; Yaghi, O. M. Hyperpolarized 129 Xe Nuclear Magnetic Resonance Studies of Isoreticular Metal-Organic Frameworks. *J. Phys. Chem. C* **2007**, *111*, 6060–6067.

(50) Mueller, U.; Schubert, M.; Teich, F.; Puetter, H.; Schierle-Arndt, K.; Pastré, J. Metal-Organic FrameworksProspective Industrial Applications. *J. Mater. Chem.* **2006**, *16*, 626–636.

(51) Greathouse, J. A.; Kinnibrugh, T. L.; Allendorf, M. D. Adsorption and Separation of Noble Gases by IRMOF-1: Grand Canonical Monte Carlo Simulations. *Ind. Eng. Chem. Res.* **2009**, *48*, 3425–3431.

(52) Rahimi, M.; Singh, J. K.; Müller-Plathe, F. Adsorption and Separation of Binary and Ternary Mixtures of SO2, CO2 and N2 by Ordered Carbon Nanotube Arrays: Grand-Canonical Monte Carlo Simulations. *Phys. Chem. Chem. Phys.* **2016**, *18*, 4112–4120.

(53) Solanki, V. A.; Borah, B. Exploring the Potentials of Metal-Organic Frameworks as Adsorbents and Membranes for Separation of Hexane Isomers. *J. Phys. Chem. C* **2019**, *123*, 17808–17822.

(54) Mohamed, M. H.; Elsaidi, S. K.; Pham, T.; Forrest, K. A.; Schaef, H. T.; Hogan, A.; Wojtas, L.; Xu, W.; Space, B.; Zaworotko, M. J.; et al. Hybrid Ultra-Microporous Materials for Selective Xenon Adsorption and Separation. *Angew. Chem., Int. Ed.* **2016**, *55*, 8285–8289.

(55) Wieme, J.; Vandenbrande, S.; Lamaire, A.; Kapil, V.; Vanduyfhuys, L.; Speybroeck, V. V. Thermal Engineering of Metal-Organic Frameworks for Adsorption Applications: A Molecular Simulation Perspective. *ACS Appl. Mater. Interfaces* **2019**, *11*, 38697–38707.

(56) Riboldi, L.; Bolland, O. Overview on Pressure Swing Adsorption (PSA) as CO2 Capture Technology: State-of-the-Art, Limits and Potentials. *Energy Procedia* **2017**, *114*, 2390–2400.

(57) Sánchez-Laínez, J.; Paseta, L.; Navarro, M.; Zornoza, B.; Téllez, C.; Coronas, J. Ultrapermeable Thin Film ZIF-8/Polyamide Membrane for H2/CO2 Separation at High Temperature without Using Sweep Gas. *Adv. Mater. Interfaces* **2018**, *5*, 1800647.

(58) Van Selow, E. R.; Cobden, P. D.; Verbraeken, P. A.; Hufton, J. R.; Van Den Brink, R. W. Carbon Capture by Sorption-Enhanced Water-Gas Shift Reaction Process using Hydrotalcite-Based Material. *Ind. Eng. Chem. Res.* **2009**, *48*, 4184–4193.

(59) Ban, Y.; Cao, N.; Yang, W. Metal-Organic Framework Membranes and Membrane Reactors: Versatile Separations and Intensified Processes. *Research* **2020**, *2020*, 1–13.

### Recommended by ACS

#### Identifying High-Performance Metal-Organic Frameworks for Low-Temperature Oxygen Recovery from Helium by Computational Screening
Shubham Jamdade, David S. Sholl, *et al.*
JANUARY 18, 2023
INDUSTRIAL & ENGINEERING CHEMISTRY RESEARCH
READ $\boxed{⧉}$

#### First-Principles Perspective on Gas Adsorption by $[Fe_4S_4]$-Based Metal-Organic Frameworks
Fatemeh Keshavarz, Bernardo Barbiellini, *et al.*
DECEMBER 29, 2022
LANGMUIR
READ $\boxed{⧉}$

#### Model-Based Analysis of a Highly Efficient CO₂ Separation Process Using Flexible Metal-Organic Frameworks with Isotherm Hysteresis
Yuya Takakura, Yoshiaki Kawajiri, *et al.*
NOVEMBER 02, 2022
ACS SUSTAINABLE CHEMISTRY & ENGINEERING
READ $\boxed{⧉}$

#### Computational Screening of Metal-Organic Frameworks for Ammonia Capture from H₂/N₂/NH₃ Mixtures
Zhaofan Zhu, Jianren Fan, *et al.*
OCTOBER 10, 2022
ACS OMEGA
READ $\boxed{⧉}$

**Get More Suggestions >**

---

11486

https://doi.org/10.1021/acs.jpcc.2c02237
*J. Phys. Chem. C* **2022**, *126*, 11475−11486