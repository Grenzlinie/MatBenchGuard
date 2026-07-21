![](./images/813113353437184001_1.jpg)
![](./images/813113353437184001_2.jpg)

Subscriber access provided by UNIVERSITY OF THE SUNSHINE COAST

Article

# Ru-Sn/AC for the Aqueous Phase Reduction of Succinic Acid to 1,4-Butanediol under Continuous Process Conditions

Derek R. Vardon, Amy Settle, Vassili Vorotnikov, Martin Menart, Todd Eaton, Kinga A Unocic, K. Xerxes Steirer, Kevin Wood, Nicholas S Cleveland, Kathleen Moyer, William E. Michener, and Gregg T Beckham

ACS Catal., Just Accepted Manuscript • DOI: 10.1021/acscatal.7b02015 • Publication Date (Web): 01 Aug 2017

Downloaded from http://pubs.acs.org on August 1, 2017

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/813113353437184001_3.jpg)

ACS Catalysis is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Ru-Sn/AC for the Aqueous Phase Reduction of Succinic Acid to 1,4-Butanediol under Continuous Process Conditions
Derek R. Vardon$^{a,*}$ Amy E. Settle$^{a}$, Vassili Vorotnikov$^{a}$, Martin J. Menart$^{a}$, Todd R. Eaton$^{a}$, Kinga A. Unocic$^{b}$, K. Xerxes Steirer$^{c}$, Kevin N. Wood$^{c}$ Nicholas S. Cleveland$^{a}$, Kathleen E. Moyer$^{a}$, William E. Michener$^{a}$, and Gregg T. Beckham$^{a}$

$^{a}$National Bioenergy Center, National Renewable Energy Laboratory, 15013 Denver West Parkway, Golden, CO 80401
$^{b}$Materials Science and Technology Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831
$^{c}$Interfacial and Surface Science, National Renewable Energy Laboratory, 15013 Denver West Parkway, Golden, CO 80401

**ABSTRACT:** Succinic acid is a biomass-derived platform chemical that can be catalytically converted in the aqueous phase to 1,4-butanediol (BDO), a prevalent building block used in the polymer and chemical industry. Despite significant interest, limited work has been reported regarding sustained catalyst performance and stability under continuous aqueous phase process conditions. As such, this work examines Ru-Sn on activated carbon (AC) for the aqueous phase conversion of succinic acid to BDO under batch and flow reactor conditions. Initially, powder Ru-Sn catalysts were screened to determine the most effective bimetallic ratio and provide a comparison to other monometallic (Pd, Pt, Ru) and bimetallic (Pt-Sn, Pd-Re) catalysts. Batch reactor tests determined that a ~1:1 Ru-Sn metal weight ratio was effective for producing BDO in high yields, with complete conversion resulting in 82% molar yield. Characterization of the fresh Ru-Sn catalyst suggests that the sequential loading method results in Ru sites that are co-located and surface enriched with Sn. Post-batch reaction characterization confirmed stable Ru-Sn material properties; however, upon transitioning to continuous conditions, significant Ru-Sn/AC deactivation occurred due to stainless steel leaching of Ni that resulted in Ru-Sn metal crystallite restructuring to form discrete Ni-Sn sites. Computational modeling confirmed favorable energetics for Ru-Sn segregation and Ni-Sn formation at sub-monolayer Sn incorporation. To address stainless steel leaching, reactor walls were treated with an inert silica coating by chemical vapor deposition. With leaching reduced, stable Ru-Sn/AC performance was observed that resulted in a molar yield of 71% BDO and 15% tetrahydrofuran for 96 h of time-on-stream. Post reaction catalyst characterization confirmed low levels of Ni and Cr deposition, although early-stage islanding of Ni-Sn will likely be problematic for industrially relevant timescales (i.e., 1000s of h). Overall, these results (i) demonstrate the performance of Ru-Sn/AC for aqueous phase succinic acid reduction, (ii) provide insight into the Ru-Sn bimetallic structure and deactivation in the presence of leached Ni, and (iii) underscore the importance of compatible reactor metallurgy and durable catalysts.

**KEYWORDS:** biobased chemical, lignocellulose, catalyst stability, leaching, restructuring

## 1. INTRODUCTION
With the increasing pressures of climate change, renewable alternatives are needed to displace our dependence on petroleum. Succinic acid is a platform chemical that can be produced at the industrial scale from the biological conversion of refined sugars, $^{1}$ as well as through several robust, native succinic-acid producing microbes from lignocellulosic sugars. $^{2-10}$ Following biological production, succinic acid can be catalytically converted to expand its potential market applications. $^{11}$ Of note, succinic acid can be catalytically reduced to 1,4-butanediol (BDO) (Scheme 1), which has a market value of $3.50 per kg (2011 USD) and an annual demand of over 1,370,000 tonnes. $^{12}$ BDO is heavily used in the plastic industry for numerous applications including polyesters, polyurethanes, and polyethers. $^{13}$ Preliminary life cycle analysis has also shown that succinic acid-derived BDO has potential to reduce green house gas emissions when compared to petrochemical routes for BDO production. $^{14}$

Recent efforts have focused on the catalytic reduction of succinic acid to BDO using water as the reaction medium. $^{15-21}$ The use of water offers a low-cost, “green” solvent for condensed phase processing, and potentially facilitates the direct catalytic upgrading of succinic acid in purified biological culture media. Aqueous phase processing also alleviates the need for esterifying succinic acid for processing, which can reduce costs at scale. Lastly, water may play a unique chemical role by preventing the formation of ester side-products through hydrolysis reactions, $^{22,23}$ facilitating heterolytic hydrogen cleavage, $^{24}$ and influencing the mechanism of acid adsorption on the catalyst surface to improve yields. $^{25}$

Efforts to catalytically convert succinic acid to BDO in the aqueous phase have primarily focused on bimetallic catalysts containing a primary platinum group metal (PGM) and secondary promoter metal in batch reactor systems. The addition of a secondary promoter metal can serve several functions, including minimizing undesirable C-C bond cleavage reactions, preventing over reduction to mono-alcohols or alkanes, mitigating dehydration to tetrahydrofuran, and facilitating subsequent ring-opening and reduction of $\gamma$-butyrolactone (GBL) to BDO. $^{15,26}$ Significant work to date has been conducted using Pd-Re bimetallic catalysts supported on activated carbon (AC) and TiO$_2$, $^{15-21}$ with demonstrated molar selectivity to BDO as high as 83% in batch reactor experiments. $^{16}$ While Pd-Re is highly active and selective, the high cost of Pd (5-

year average of $\$22.60$ per g$)^{27}$ has motivated studies into alternative bimetallic systems.

Of note, Ru-Sn bimetallic catalysts are highly active for the aqueous phase reduction of carbonyl groups. $^{28,29}$ Under non-aqueous phase conditions, Ru-Sn catalysts have been widely applied for the selective hydrogenation of long chain fatty acids, $^{30}$ dicarboxylic acids, $^{28,31-33}$ esters, $^{34-36}$ and unsaturated aldehydes. $^{37}$ From an economic standpoint, Ru is attractive as it costs $\sim1/10^{\text{th}}$ the price of Pd on a mass basis (5-year average of $\$2.11$ per g). $^{27}$ However, to our knowledge peer-reviewed studies to date have yet to examine Ru-Sn/AC for the aqueous phase reduction of succinic acid and its sustained performance under continuous process conditions. Continuous aqueous phase processing of succinic acid is highly desirable from a scale-up and green chemistry standpoint, $^{38}$ although it introduces the challenge of catalyst stability and deactivation that is often beyond the scope of batch reactor studies. $^{39-43}$

![](./images/813113353437184001_4.jpg)

Scheme 1: Reaction scheme for the catalytic reduction of succinic acid to 1,4-butanediol (BDO).

As such, this work examines the application of Ru- Sn/AC catalysts for the aqueous phase reduction of succinic acid to BDO. Initially, batch reactor screening tests were conducted with powder AC catalysts to evaluate the most effective loading of Sn to promote Ru and provide a benchmark comparison to other bimetallic catalysts (i.e., Pd-Re, Pt-Sn). Catalysts were characterized by multiple techniques to assess the impact of secondary metal addition on material properties (e.g., support surface area and porosity, bulk structural order, metal crystallite size and elemental distribution) and physico-chemical characteristics (e.g., $\text{H}_2$ and CO affinity, temperature reduction profile, acid site density and speciation) to gain insight into the synthesized bimetallic crystallite structure and structure-function properties. The highest performing Ru-Sn formulation was then synthesized on granular AC for testing in a trickle-bed reactor to determine the activity, selectivity, and stability with time-on-stream. Lastly, due to Ru-Sn stability challenges observed from to succinic acid chelation and stainless steel leaching, computational modeling was conducted to evaluate the energetics of Ru- Sn restructuring to gain further into the stable bimetallic catalyst formulations for aqueous phase succinic acid reduction.

## 2. RESULTS

### 2.1. Catalyst synthesis and characterization.
To evaluate the impact of Sn on the performance of Ru and provide a benchmark to other bimetallic catalysts, a suite of materials with increasing secondary metal loading was prepared and characterized. Monometallic PGM catalysts (i.e., Pd, Pt, Ru) were initially synthesized on Darco powder activated carbon (PAC) that was sieved to $<270$ mesh ($<53$ $\mu\text{m}$ particles). The native carbon support displayed a point of zero charge of pH 7.7, which was lowered to 3.5 by nitric acid treatment. Strong electrostatic adsorption with platinum group metal (PGM) cationic precursors was used to facilitate high metal dispersion. $^{44,45}$ Chemisorption of the monometallic catalysts confirmed highly disperse PGM loadings (21-31%) (Table S1). Secondary promoter metals (i.e., Re, Sn) were loaded sequentially by incipient wetness after PGM deposition and reduction. The prepared bimetallic catalysts were then reduced and exposed to air prior to testing.

Detailed characterization was performed on the bimetallic catalysts with a nominal 1:1 weight ratio. Bulk elemental analysis by inductively coupled plasma spectroscopy (ICP-MS) showed primary-to-secondary metal mass ratios that ranged from 1.17-1.31, likely due to loss of fine support particles during the repeated loading of primary metal precursors by electrostatic static adsorption (see Supporting Information Methods). X-ray photoelectron spectroscopy (XPS) showed surface enrichment of Sn, but interestingly not for Re (Table S2). X-ray diffraction (XRD) analysis showed broad peaks in the respective loaded metal regions of interest (Figure S1), supportive of highly disperse metal crystallites. Likewise, elemental mapping by scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDS) showed evenly-distributed metals across the particles, while transmission electron microscopy (TEM) imaging confirmed crystallites $<5$ nm in diameter (Figure 1).

Chemisorption of the Pd-Re catalyst showed a significant increase in $\text{H}_2$ uptake (456 $\mu\text{mol}$ $\text{g}^{-1}$) compared to monometallic Pd (70 $\mu\text{mol}$ $\text{g}^{-1}$), highlighting the impact of Re addition on hydrogen affinity. Surprisingly, Pt-Sn and Ru-Sn catalysts displayed extremely low $\text{H}_2$ uptake ($<5$ $\mu\text{mol}$ $\text{g}^{-1}$) (Table S2) compared to their monometallic counterparts (Pt 70 $\mu\text{mol}$ $\text{g}^{-1}$; Ru 47 $\mu\text{mol}$ $\text{g}^{-1}$), highlighting the suppression of $\text{H}_2$ affinity by Sn. Further testing of Ru- Sn by CO pulse chemisorption also showed muted uptake (5.9 $\mu\text{mol}$ $\text{g}^{-1}$) (Table S2), $^{33,29}$ suggestive of a Sn-enriched surface that decreases the binding affinity for both molecules. Lastly, nitrogen physisorption confirmed comparable activated carbon support surface areas (773-888 $\text{m}^2$ $\text{g}^{-1}$), with a narrow range of pore volumes (0.43-0.51 $\text{cm}^3$ $\text{g}^{-1}$) and pore diameters (14.2-14.6 $\mathring{\text{A}}$) (Table S2). This suggests that differences in bimetallic catalyst performance are not due to variations in the underlying support structure.

![](./images/813113353437184001_5.jpg)

Figure 1. Characterization of fresh 1:1 (wt.%) bimetallic powder catalysts used in the batch reactor screening study by SEM-EDS and TEM for Pt-Sn/PAC (A-D), Pd-Re/PAC (E-H), and Ru-Sn/PAC (I-L).

Due to the focus on Ru-Sn (1:1) (vide infra), further characterization was conducted to evaluate the surface acidity and temperature dependent reducibility. Initial attempts to quantify Ru-Sn acidity by $NH_3$-temperature programmed desorption were deemed inconclusive due to off-gassing of the catalyst at high temperature, which may be due to auto-reduction or decomposition of the nitric acid-treated activated carbon support functional groups (Figure S2).$^{46}$ Qualitative acidity measurements were then attempted using pyridine adsorption diffuse reflectance Fourier-transform infrared spectroscopy (DRIFTS) after reducing the catalysts in situ (Figure S3). DRIFTS analysis revealed peaks at $1445\ \mathrm{cm}^{-1}$ and $1590\ \mathrm{cm}^{-1}$ for Ru-Sn/PAC and Sn/PAC that were present at $50^\circ\mathrm{C}$ but disappeared at $150^\circ\mathrm{C}$, indicative of pyridine adsorbed through weak hydrogen bonding with surface hydroxyl groups. However, the activated carbon support may interfere with detecting Lewis and Brønsted acid peaks due to strong incident radiation adsorption.$^{47}$ The need to identify and quantify Brønsted and Lewis acidity is notable, since acid catalyzed GBL ring opening is a critical step for converting succinic acid to BDO while avoiding excessive dehydration to THF.$^{33,48}$

Temperature-programmed reduction (TPR) profiles further highlighted the influence of Sn on catalyst behavior (Figure S4 and S5). The monometallic Ru catalyst showed a low temperature peak between $60$-$80^\circ\mathrm{C}$, suggestive of amorphous $\mathrm{RuO_2}$ reduction,$^{49}$ as well as a smaller reduction peak between $180$-$220^\circ\mathrm{C}$, suggestive of bulk $\mathrm{RuO_2}$ reduction. At temperatures above $250^\circ\mathrm{C}$, the onset of a broad peak is observed that is suggestive of auto-reduction or $\mathrm{CO}$ and $\mathrm{CO_2}$ evolution from the support, as noted above.$^{46}$ For the Ru-Sn (1:1) catalyst, a low temperature reduction peak during TPR was observed between 50-$100^\circ\mathrm{C}$, although $\mathrm{H_2}$ chemisorption showed only $9\%$ of the $\mathrm{H_2}$ uptake when compared to monometallic Ru (Table S1 and S2). In comparison to other Ru-Sn bimetallic systems, reduction peaks were not observed between $250$-$350^\circ\mathrm{C}$,$^{28,50-52}$ suggesting significant Sn surface enrichment of Ru sites that influences $\mathrm{H_2}$ uptake. At high temperatures above $400^\circ\mathrm{C}$, a broad low magnitude peak was observed (Figure S4), potentially due to the reduction of oxygenated functional groups on the support or reduction of $\mathrm{SnO_2}$.$^{53}$

![](./images/813113353437184001_6.jpg)

Figure 2. Influence of secondary metal loading ratio on the reduction of succinic acid to 1,4-BDO during 6 h screening reactions with Pd-Re/PAC (A), Pt-Sn/PAC (B), and Ru-Sn/PAC (C). Reactions were performed in duplicate, with average values reported and standard deviations typically less than 5%. Non-target products include the sum of propanol, butanol, and propionic acid. Losses were calculated based on molar closure. Batch time series experiments were then conducted with 1:1 bimetallics for 8 h (D-F). Reaction conditions were as follows: 20 mL of 2 wt.% succinic in DI water, 100 mg of catalyst, 100 bar of H₂ loaded at 24°C, stirring 800 rpm, temperature 180°C.

### 2.2. Influence of secondary promoter metal loading.
Batch reactor screening experiments were used to evaluate the activity and selectivity of the catalyst suite for succinic acid reduction to BDO, with results reported on a molar yield basis (Figure 2). As expected, monometallic catalysts performed poorly when targeting BDO. For Pd/PAC, $\gamma$-butyrolactone (GBL) was the major product (66%), consistent with past reports, with moderate amounts of BDO (17%).¹⁹ For Pt/PAC, low activity for succinic acid reduction was observed, with significant amounts of succinic acid remaining (60%). For Ru/PAC, molar losses were significant (67%), likely due to the loss of products to the gas phase from C-C bond cleavage and light product formation. Similarly, losses to methane with Ru have been observed during the reduction of succinic acid in dioxane²⁶ and the aqueous phase hydrogenolysis of polyols.⁵⁴,⁵⁵ Significant non-target products were also observed (22%), consisting of propionic acid, propanol, and butanol.

Progressive addition of oxophilic secondary metals (e.g., Re, Sn) dramatically improved catalyst performance for selectivity towards BDO, consistent with previous bimetallic catalyst batch reactor screening results summarized in Table S3. The high activity and selectivity of Pd-Re/PAC was clearly evident (Figure 2A), even at a primary-to-secondary metal mass ratio of 1:0.5, that resulted in a high yield of BDO (47%) and moderate yield of GBL (16%) and THF (15%). Increasing the Re loading to a mass ratio of 1:1 further improved the BDO yield (67%) through conversion of the intermediate GBL. With

additional Re (1:2 mass ratio), no further yield improvements were observed. This suggests no further alteration of active sites responsible for BDO loss through cracking, over-reduction, or dehydration.

In contrast, both Sn-based catalysts displayed an optimum secondary metal loading for maximum BDO yield. For Pt-Sn/PAC (Figure 2B), a mass ratio of 1:0.5 increased succinic acid reduction activity compared to monometallic Pt and resulted in a moderate yield of BDO (22%), GBL (29%), and THF (13%), with significant molar losses (21%). Increasing the mass ratio to 1:1 resulted in a high yield of BDO (51%) and moderate yield of THF (13%), although molar losses (21%) were still significant. Interestingly, at a Pt-Sn mass ratio of 1:2 the catalyst reduction activity decreased dramatically, resulting in unreacted succinic acid (85%). The drop in activity at high Sn loading suggests unfavorable bimetallic crystallite restructuring or blocking of the active promoter phase.

Lastly, for Ru-Sn/PAC (Figure 2C) a low Sn loading (1:0.5 mass ratio) greatly muted cracking reactions and decreased molar losses from 67% to 18% when compared to monometallic Ru. Non-target products from over-reduction were still observed in significant quantities (30%). Increasing the Ru-Sn mass ratio to 1:1 resulted in a high yield of BDO (67%) and GBL (23%) that was on par with the high performing Pd-Re/PAC (1:1) catalyst. Further addition of Sn (1:2 mass ratio) dramatically reduced the yield of BDO (15%) and increased molar losses (26%), highlighting the performance sensitivity with the primary-to-secondary metal mass ratio. Low BDO yields ($\leq$11%) were observed when altering the Ru-Sn/PAC 1:1 synthesis procedure to either (i) sequentially load Sn first, or (ii) co-load Ru and Sn simultaneously by incipient wetness (see Figure S6). Although a detailed investigation of the resulting catalytic structures from multiple synthetic methods is beyond the scope of this study, these results indicate that BDO yield is strongly dependent on the synthetic method. The high BDO yield with strong electrostatic adsorption and the sequential loading method may be due to highly disperse Ru metal nanoparticles with significant Sn surface enrichment.

Based on the favorable bimetallic catalyst performance with a 1:1 metal ratio, batch reactor time series experiments were conducted to evaluate the progression of product selectivity to BDO, as shown in Figure 2D-F. Time series runs confirmed that Pd-Re/PAC was the most active catalyst, with near complete conversion of succinic acid after 2 h, and near equal amounts of GBL and BDO. By 4 h, maximum BDO selectivity was observed with a molar yield of 74% (Figure 2D). Due to the difficulty in quantifying bimetallic active sites, catalyst site time yields (STY) for BDO were reported on product mass per catalyst mass per unit time. For Pd-Re/PAC (1:1), the BDO STY after 4 h was $0.28\ \mathrm{g_{BDO}\ g_{cat}^{-1}\ h^{-1}}$. The high molar yield of BDO is consistent with previous reports of Pd-Re supported on AC and TiO₂ supports, although direct comparisons are difficult due to varying metal loadings and experimental conditions (see Table S3 for summary of results and conditions previously reported in peer-reviewed literature).

In comparison, the Sn bimetallic catalysts displayed a much lower activity for succinic acid reduction, although with high BDO selectivity. For Pt-Sn/PAC, 6 h were required for complete succinic acid conversion. Maximum BDO selectivity was observed at 8 h, with a molar yield of 53% and a BDO STY of $0.10\ \mathrm{g_{BDO}\ g_{cat}^{-1}\ h^{-1}}$ (Figure 2E). Ru-Sn/PAC displayed moderate activity with 6 h required for complete conversion as well. By 8 h, residual GBL was converted into BDO, resulting in a BDO molar yield of 82% and STY of $0.16\ \mathrm{g_{BDO}\ g_{cat}^{-1}\ h^{-1}}$ (Figure 2F). Previous reports have examined Ru-Sn/Al₂O₃ in dioxane (see Table S3), which resulted in 11% BDO yield and significant GBL (30%) and THF (59%) formation after 20 h.³³ This disparity may be due to differences in Ru dispersion, surface Sn enrichment, support acidity, and reaction conditions. Interestingly, the same Ru-Sn/Al₂O₃ catalyst was highly active for converting adipic acid to 1,6-hexanodiol (89%).³³ This suggests the need to tailor Ru-Sn surface reactivity for succinic acid in order to facilitate GBL ring opening, while avoiding dehydration to THF. Although in this study the BDO production rate with Ru-Sn/PAC is nearly half that of Pd-Re/PAC, the $1/12^\mathrm{th}$ material cost motivated further development. Interestingly, both Pt-Sn/PAC and Ru-Sn/PAC displayed an inhibition period during the first 4 h, similar to past reports using Ru-Sn for the batch reduction of oleic acid and unsaturated aldehydes.⁵⁰ The lag phase could potentially be attributed to several factors, including catalyst reduction after air exposure, restructuring under working conditions, oxidation of the catalyst surface when interacting with the organic substrate, or initial chelation of carboxylates with active metal sites.

Post-reaction characterization of the Ru-Sn/PAC (1:1) catalyst confirmed stable material properties after batch reactions. ICP analysis was unable detect Ru or Sn in the filtered liquid phase, confirming the stability of the catalyst against leaching. In comparison, leaching analysis of a monometallic Sn/PAC catalyst under the same conditions resulted in 13.95 ppm of Sn, suggesting Ru mitigates Sn leaching during succinic acid hydrogenation, similar to past reports for Pt-Sn with carboxylic acids⁵² and Ru-Sn with levulinic acid.²⁹ SEM-EDS mapping of the catalyst confirmed that Ru and Sn remained uniformly dispersed on the catalyst support (Figure S7A-C), while TEM imaging showed metal crystallites < 5 nm in diameter (Figure S7D). These results were consistent with the broad peaks observed by XRD for the fresh and spent catalyst (Figure S7E-F).

### 2.2. Sustained performance of Ru-Sn/AC in flow.
To evaluate the prolonged activity and stability of Ru-Sn/AC, the catalyst was synthesized on granular activated carbon (GAC) for testing in a trickle bed reactor. The granular

catalyst synthesis procedure was identical to the powder catalyst, with the exception of using Darco AC sieved to 30-50 mesh to minimize pressure drop across the reactor bed. Minimal levels of Cr, Ni, and Fe impurities were present in the fresh catalyst (Table 1). SEM-EDS mapping confirmed an even distribution of Ru and Sn across the support (Figure S8A-C), while TEM imaging showed disperse metal crystallites with a particle diameter of $1.7 \pm 0.4$ nm (Figure S8D and S8E). Chemisorption showed poor hydrogen uptake $(3.2\ \mathrm{\mu mol\ g^{-1}}$; Table S4), similar to the powder catalyst used in the batch reactor screening study (Table S2). Nitrogen physisorption determined that the granular catalyst had a lower surface area $(652\ \mathrm{m^2\ g^{-1}})$ compared to the powder $(773\ \mathrm{m^2\ g^{-1}})$ support, and a comparable pore volume $(0.45\ \mathrm{cm^3\ g^{-1}})$ and pore diameter (14.4 Å) (Table S4).

Table 1. ICP-MS elemental analysis of fresh and spent Ru-Sn/GAC catalysts to evaluate the impact of stainless steel leaching.
<table>
  <thead>
    <tr>
      <th>Elemental Composition</th>
      <th>Fresh Ru-Sn/GAC (1:1)</th>
      <th>Spent Ru-Sn/GAC Uncoated Rx</th>
      <th>Spent Ru-Sn/GAC Coated Rx</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cr (ppm)</td>
      <td>13</td>
      <td>28,000</td>
      <td>4,250</td>
    </tr>
    <tr>
      <td>Ni (ppm)</td>
      <td>18</td>
      <td>17,000</td>
      <td>5,570</td>
    </tr>
    <tr>
      <td>Fe (ppm)</td>
      <td>2080</td>
      <td>1,920</td>
      <td>2,840</td>
    </tr>
  </tbody>
</table>

To provide further evidence regarding the nature of the bimetallic active site, high-resolution STEM-EDS imaging was performed. Line scan analysis confirmed the co-location of Ru and Sn within a given metal nanoparticle for the fresh catalyst (Figure 3). This information, along with the reduced binding affinity for $\mathrm{H_2}$ and CO observed during chemisorption (Table S2 and S4), supports that the sequential loading method results in Sn surface enrichment of Ru nanoparticle sites.

![](./images/813113353437184001_7.jpg)

Figure 3. High resolution STEM-EDS analysis of the fresh Ru-Sn/GAC catalyst.

Lastly, XPS analysis evaluated the impact of air exposure and hydrogen reduction on the oxidation state of Ru and Sn. With air exposure, Ru displayed a mixed oxidation state of $\mathrm{Ru^0}$ (16%), $\mathrm{Ru^{2+}}$(40%), $\mathrm{Ru^{3+}}$(15%), and $\mathrm{Ru^{4+}}$(28%) based on lineshape analysis of the Ru $3_{p/2}$ spectra (Figure 4A).$^{56-58}$ In contrast, Sn was in a fully oxidized state of $\mathrm{Sn^{4+}}$ as determined by lineshape analysis of the Sn $3d_{3/2}$ spectra (Figure 4B).$^{59,60}$ Upon exposure to flowing $\mathrm{H_2}$ at $180^\circ\mathrm{C}$, Ru was reduced to a mixed oxidation state of predominantly $\mathrm{Ru^0}$ (68%), with residual $\mathrm{Ru^{2+}}$ (15%) and $\mathrm{Ru^{3+}}$ (17%). Similarly, Sn was reduced to a mixed oxidation state of predominantly $\mathrm{Sn^{2+}}$ (55%) with $\mathrm{Sn^{4+}}$ (32%) and $\mathrm{Sn^0}$ (13%). The higher oxidation states of Sn may provide Lewis acidity through $\mathrm{Sn^{2+}}$ or unsaturated $\mathrm{Sn^{4+}}$ cations, while Brønsted acidity may be provided surface hydroxyl group bonded through $\mathrm{Sn^{4+}}$.$^{61}$ As noted, surface acidity is critical for GBL ring opening.$^{48}$ Although trace oxygen and moisture exposure could not be completely avoided during glove box transfer, these results support a partially metallic state of Ru and Sn under reducing conditions. This transition may be responsible for the batch reaction lag phase (Figure 2). Future work will further elucidate the structure and stability of the Ru-Sn active site under working conditions.

![](./images/813113353437184001_8.jpg)

Figure 4. XPS of the fresh Ru-Sn/GAC catalyst. The air-exposed catalyst was analyzed following synthesis and storage under ambient conditions. The 'air-free' catalyst was reduced in a reactor tube at $180^\circ\mathrm{C}$ under $\mathrm{H_2}$ flowing prior to transfer into a glovebox integrated XPS system for mounting and analysis. The glovebox was maintained at $<10$ ppm moisture and $\mathrm{O_2}$.

Initial trickle bed reactor experiments were performed with the Ru-Sn/GAC catalyst using an uncoated 316 stainless steel reactor tube. Partial conversion runs showed a steady decline in catalyst activity over 100 h prior to steady state (Figure S9). Post-reaction characterization of the catalyst confirmed that significant compositional and structural changes had occurred. SEM-EDS imaging of the catalyst (Figure S10) revealed the deposition of Cr and Ni on the surface that leached from the stainless steel reactor tube. Elemental mapping showed that Ru, Cr, and Fe remained evenly distributed, while discrete Ni-Sn crystallites had formed at the micron scale. The restructuring of Ru-Sn to form Ni-Sn suggests preferential alloying. Previous efforts have shown Ni-Sn to be active for hydrogenation of glucose,⁶² although the large metal crystallite size makes it questionable that these particles would show significant activity. TEM imaging of the spent catalyst confirmed a heterogeneous distribution of dispersed and sintered metal crystallites (Figure S11). Regions of non-sintered metal crystallites (< 3 nm diameter) were present throughout the spent catalyst (Figure S11A), which is likely responsible for the continued hydrogenation activity with succinic acid. ICP analysis of the spent catalyst confirmed significant levels of Cr (2.8%) and Ni (1.7%) relative to the fresh catalyst (Cr 13 ppm; Ni 18 ppm), and comparable levels of Fe (2080 ppm fresh; 1920 ppm spent) native to the AC support (Table 1). Control experiments with blank activated carbon in an uncoated reactor tube showed no catalytic activity for succinic acid reduction with over 65 h of time-on-stream (Figure S12), supporting that residual Ru-Sn crystallites are likely responsible for the remaining catalyst activity.

2.3. Impact of metallurgy on catalyst stability. To reduce stainless steel leaching and mitigate Ru-Sn restructuring, the trickle bed reactor tube was coated with silica by chemical vapor deposition (CVD) to form an inert barrier to the aqueous acid feed. The use of silica surface coatings to inhibit stainless steel corrosion in aqueous acidic environments has been well documented in the literature.⁶³⁻⁶⁵ Using the silica-coated reactor tube, stable catalyst activity was observed for 84 h under partial conversion conditions (Table S6). Analysis of the reactor effluent showed no detectable leaching of Ru or Sn, and analysis of spent catalysts showed significantly decreased levels of Cr, Ni, and Fe compared to the uncoated reactor tube (Table 1). SEM-EDS elemental mapping of the spent catalyst confirmed highly disperse Ru and Sn sites throughout the support (Figure S13).

With stable catalyst performance achieved, further experiments were conducted to examine the apparent activation energy and prolonged stability under complete conversion conditions. Under partial conversion conditions (<25% molar conversion, 5 wt.% succinic acid, liquid flow rate 0.25 mL min⁻¹, temperature 180°C, H₂ 200 sccm at 124 bar, catalyst loading 200 mg), an apparent activation energy of 62.2 kJ mol⁻¹ was measured for succinic acid reduction, as shown in Figure 5A. Subsequent experiments under complete conversion conditions (5 wt.% succinic acid in water, liquid flow rate 0.1 mL min⁻¹, temperature 170°C, H₂ 200 sccm at 124 bar, catalyst loading 5 g) confirmed stable catalyst performance for 96 h of time-on-stream, with an average molar yield of 71% BDO, 15% THF, 3% GBL, and 2% butanol (Figure 5B). Trace propanol was also present at below 0.5% molar yield, resulting in an average liquid product molar closure of 91%. A low weight hour space velocity (WHSV) of 0.06 h⁻¹ was required to convert both succinic acid and the intermediate GBL to produce BDO as the primary product.

Characterization of the spent catalyst from the 96-h complete conversion run in the coated reactor tube showed minor material property changes compared to the catalysts used in the uncoated reactor tube. Bulk elemental analysis of the spent catalyst by ICP-MS revealed significantly lower levels of Cr (4250 ppm) and Ni (5570 ppm) compared to runs in the uncoated reactor tube (Cr 28,000 ppm; Ni 17,000 ppm), suggesting silica CVD coating dramatically reduces stainless steel leaching (Table 1). Ru and Sn metal loadings were comparable to the fresh catalyst; however, XPS elemental analysis revealed a lower ratio of Ru to Sn, indicating enrichment of Sn on the surface of the catalyst under operating conditions (Table S4). Enrichment of surface Sn may be due to prolonged exposure to operating conditions or Ni leaching, with further work needed to decouple the effects of both phenomena. Nitrogen physisorption analysis of the activated carbon support showed 9% reduction in surface area to 595 m² g⁻¹, 9% increase in pore volume to 0.49 cm₃ g⁻¹, and 36% reduction in pore diameter to 9.8 Å (Table S4). This suggests a reduction in the carbon support average pore size with prolonged exposure to reaction conditions, potentially due to support restructuring or oligomer fouling in larger pore diameters.

STEM elemental mapping of the fresh (Figure 6A) and spent (Figure 6B) Ru-Sn/GAC catalyst revealed that with time-on-stream in the coated reactor tube, small patches of agglomerated metal particles still resulted (see Figure S14 for TEM results). In the spent catalyst, Ni was observed uniformly across the support, consistent with elemental analysis by ICP (Table 1). The early onset of discrete ~100-nm Ni-Sn sites was also evident, which is much smaller compared to the micron-scale Ni-Sn metal crystallites observed in the uncoated reactor tube (Figure S10). Although chemical and material stability of the Ru-Sn/GAC catalyst was greatly improved through reactor CVD coating, further efforts are needed when considering industrially relevant time scales for catalyst performance (i.e., 1000s of h), tradeoffs with using more expensive reactor metallurgy, and potential for alternative catalyst formulations.

![](./images/813113353437184001_9.jpg)

Figure 5. Apparent activation energy for succinic acid reduction under partial conversion conditions (<25% molar) with Ru-Sn/GAC (1:1) in the silica CVD coated trickle bed reactor tube (A). Complete conversion of succinic acid resulted in molar yields of 71% BDO and 15% THF (B). Reaction conditions for both experiments are listed in the figure insets.

![](./images/813113353437184001_10.jpg)

Figure 6. Characterization by STEM-EDS of the fresh (A) and spent (B) Ru-Sn/GAC catalyst used in the CVD coated trickle bed reactor tube for 96 h of time-on-stream. On the spent catalyst, increased levels of Ni were observed, as well as the formation of Ni-Sn “hot spots” (triangle symbols) that were consistent with bulk elemental analysis by ICP-MS shown in Table 1.

### 2.4. Energetics of bimetallic catalyst restructuring.
To provide further insight into the nature of Ru-Sn restructuring when exposed to stainless steel leaching, periodic density functional theory calculations were performed to assess the energetics of bimetallic surface formation and subsurface-to-surface segregation. Ru-Sn, Pt-Sn, and Ni-Sn were chosen as model bimetallic systems, with Ru-Sn and Pt-Sn representing native bimetallic hydrogenation catalysts and Ni-Sn representing undesired metal crystallites formed during stainless steel leaching.

To assess the surface formation energy for a bimetallic M-Sn system, where M equals Ru, Pt, or Ni (Figure 7A), the bimetallic formation was modeled as a reaction between the constituent species:

$$
\mathbf{M}_a^{surf} + b\mathbf{Sn}^{bulk} \rightarrow \mathbf{M}_{a-b}\mathbf{Sn}_b^{surf} + b\mathbf{M}^{bulk}
$$

where $\mathbf{M}_a^{surf}$ is a slab of metal $\mathbf{M}$ consisting of $a$ atoms, $\mathbf{M}_{a-b}\mathbf{Sn}_b^{surf}$ is the same slab with $b$ Sn atoms incorporated into the top layer replacing the same number of $\mathbf{M}$ atoms, and bulk referring to the single-component $\mathbf{M}$ or $\mathbf{Sn}$ phase. The average formation energy is then defined as the energy of this reaction:

$$
\Delta E_f = \left(E_{\mathbf{M}_{a-b}\mathbf{Sn}_b^{surf}} + bE_{\mathbf{M}^{bulk}} - E_{\mathbf{M}_a^{surf}} - bE_{\mathbf{Sn}^{bulk}}\right)/b
$$

where all quantities refer to zero-K DFT energies.

To assess the subsurface-to-surface segregation energy for a bimetallic M-Sn system, the reaction was evaluated as:

$$
\mathbf{M}_c\mathbf{Sn}_d^{subsurf} \rightarrow \mathbf{M}_c\mathbf{Sn}_d^{surf}
$$

where $\mathbf{M}_c\mathbf{Sn}_d^{subsurf}$ represents $d$ Sn atoms incorporated into the subsurface of the metal slab and $\mathbf{M}_c\mathbf{Sn}_d^{surf}$ represents the corresponding surface with $d$ Sn atoms in the top layer. The average segregation energy, $\Delta E_{seg}$, is the difference between the two states:

$$
\Delta E_{seg} = \left(E_{\mathbf{M}_c\mathbf{Sn}_d^{surf}} - E_{\mathbf{M}_c\mathbf{Sn}_d^{subsurf}}\right)/d
$$

This definition of segregation energy is similar to one used by Nørskov and co-workers,⁶⁶,⁶⁷ but it is referenced to subsurface configurations rather than bulk structures to maintain stoichiometry.

Using the above equations, the M-Sn formation and segregation energies were computed as a function of Sn incorporation into the top surface layer of M. The average bimetallic surface formation energy with Sn follows the trend of Ru >Ni >Pt at coverage below 0.5 monolayer (ML), with smaller differences in formation energy below 0.25 ML (Figure 7B). This suggests that the driving force for the surface formation of Ni-Sn is greater than that for Ru-Sn in this range of surface coverage. The driving force for Sn subsurface-to-surface segregation follows the same trend of Ru >Ni >Pt (Figure 7C). For Ru, the segregation energy is very negative (about -2.5 eV), suggesting facile Sn migration to the surface. Meanwhile, the segregation energy for Ni is less exothermic (even more so for Pt), suggesting a weaker driving force for Sn migration. These results may explain the tendency of Sn to transfer from Ru-Sn to Ni-Sn under stainless steel leaching conditions. Furthermore, the results with Pt-Sn highlight the potential for enhanced stability against restructuring in the presence of Ni through bimetallic elemental selection, although at the potential expense of desired activity and selectivity for succinic acid reduction.

![](./images/813113353437184001_11.jpg)

**Figure 7.** Computational results, including model M-Sn bimetallic surfaces for M = Ru, Ni, Pt (A), formation energies of M-Sn surfaces with increasing Sn incorporation in the top monolayer, with lower values indicating a greater driving force for M-Sn formation relative to surface M and bulk Sn (B), and M-Sn subsurface-to-surface segregation energy with increasing Sn incorporation, with lower values indicating a greater driving force for subsurface-to-surface Sn segregation (C).

## DISCUSSION

### 3.1. Ru-Sn/PAC for improved BDO selectivity.
As shown in this work, monometallic Ru/PAC is highly active for converting succinic acid to THF, non-targets (butanol, propanol, propionic acid), and gas phase products, but poorly selective to BDO. Ru alone resulted in complete conversion and significant cracking via hydrogenolysis of succinic acid under batch screening conditions employed in this work $(180^{\circ} C, 100$ bar $H_{2})$ (Figure 2). $^{68}$ As noted above, excessive C-C bond cleavage has been previously observed with $Ru$ during the reduction of succinic acid $^{26}$ and hydrogenolysis of polyols. $^{54,55}$ Previous efforts have shown that under milder conditions $(150^{\circ} C, 35$ bar $H_{2}), Ru$ can be highly active and selective for the partial reduction of succinic acid to GBL $(\geq 90 \%),^{68}$ although BDO is not produced in significant quantities. $Ru$ is highly active for monocarboxylic acid reduction, as been shown for acetic, $^{69,70}$ lactic, $^{71-73}$ and propionic acid, $^{73-75}$ with theimproved performance linked to its greater oxophilicity $^{25}$  and ability to interact with water. $^{69}$ However, to target BDO the addition of a secondary promoter metals is needed to facilitate ring opening and the subsequent reduction of GBL.

The addition of $Sn$ to $Ru$ resulted in highly uniform small metal crystallites (Figure 1, Figure S8), which dramatically improved the selectivity for BDO and muted hydrogenolysis activity (Figure 2). The sequential preparation method to load $Sn$ on top of $Ru$ resulted in surface enrichment of $Sn$ by XPS, muted $H_{2}$ and $CO$ binding affinity, and no discernable bimetallic reduction peaks by TPR (Table S2, Figure S4). Further, STEM-EDS line scan analysis (Figure 3) supports the co-location of $Ru$ and $Sn$ and suggests that enhanced performance is due to their chemical interaction, as opposed to a physical mixture of isolated $Ru$ and $Sn$ sites. Previous efforts to characterize the interaction of $Ru$ and $Sn$ have shown that $Sn$ incorporation can suppress both $H_{2}$ and $CO$ binding affinity, $^{29,33}$ consistent with this work. Sn-mediated suppression of $H_{2}$ binding affinity may correlate with the muted cracking activity observed for Ru-Sn/PAC, when compared to monometallic Ru/PAC (Figure 2). C-C bond cleavage is typically preceded by C-H bond cleavage, $^{76}$ with the latter affected by $H_{2}$ binding affinity. $^{77}$ Similar cracking suppression effects with $Sn$ incorporation have been proposed for Pt-Sncatalysts. $^{78-80}$

The oxophilic promoter effects of adding $Sn$ to $Ru$ for succinic acid reduction have also been observed when adding Co to $Ru,^{26}$ as well when adding Re to Pd. $^{15}$ It has been proposed that the use of oxophilic secondary metals may enhance the coordination of carboxylic groups due to Lewis acidity, as well as facilitate GBL ring opening forsubsequent hydrogenation. $^{15}$ For $Sn$ , Brønsted and Lewis acidity requires an oxidized state as opposed to metallic, $^{61,81}$  consistent with the XPS results shown here (Figure 4). It should be noted that bimetallic crystallite structures are highly influenced by the elemental composition, synthetic method, and reaction conditions, affording possibilities for tuning the surface reactivity. The influence of water on surface reactivity should also not be ruled out, as recent computational studies have shown interesting co-adsorptionbehavior over monometallic Ru surfaces. $^{82}$

### 3.2. Ru-Sn/GAC continuous-flow performance.
The importance of compatible reactor metallurgy was evident when processing succinic acid continuously in a trickle bed reactor. The Ru-Sn crystallites significantly restructured to form Ni-Sn crystallites with the uncoated stainless reactor tube (Figure S10), which resulted in a steady decline in catalyst performance (Figure S9). Previous work with Ru-Sn/AC has shown stable performance for the aqueous phase reduction of levulinic acid to $\gamma$ -valerolactone in stainless steel reactors, $^{29}$ which suggests that the chelating properties of succinic acid and other diacids may be uniquely problematic and impact bimetallic catalystdesign. $^{83}$

Coating the stainless steel reactor tube with silica byCVD greatly retarded the deposition of $Ni$ and $Cr$ (Table 1) and minimized restructuring of $Ru-Sn$ for the course of the96-h reaction (Figure 5 and 6). Neither $Ru$ nor $Sn$ were detected in the reactor effluent, which supports that the metal crystallites remain strongly anchored on the activated carbon support under acidic conditions. $^{42} AC$ supports have been shown to be very stable in subcritical water, in contrast to $Al_{2} O_{3}$ and $SiO_{2}$ which are subject to hydrolysis reactionsthat result in dramatic pore collapse and deactivation. $^{84}$  STEM-EDS analysis confirmed the early onset of Ni deposition and Ru-Sn restructuring (Figure 6). The distribution of agglomerated regions was highly non- uniform across and between catalyst particles (Figure S14), which may be due to early-stage leaching of $Ni$ from the reactor walls that promotes restructuring or metal site mobility that leads to sintering. Sintering was observed as a prominent deactivation mode for monometallic $Ru$ during the aqueous phase hydrogenation of levulinic acid on both carbon and oxide supports. $^{85}$ For succinic acid, further study is needed to understand the role of bimetallic metal-support interactions to influence sintering during aqueous phase processing.

With regards to mitigating Ru-Sn restructuring, several techniques have emerged to enhance metal crystallite stability, including atomic layer overcoatings, support surface chemical modification, and post-synthesis treatmentto promote strong metal-support interactions. $^{40,86,87}$  Likewise, alternative reactor metallurgies may be considered for processing aqueous acid streams, such as Hastelloy or titanium. $^{88}$ However, due to the resulting increase in reactor material expenses, the impact on capital costs and process economics must be considered.

With stable flow reactor performance in the coated reactor tube, partial and complete conversion conditions were established with Ru-Sn/GAC by varying the WHSV(Figure 5). Under partial conversion conditions $(<25 \%$  molar conversion) at a WHSV of $4.0 ~h^{-1}$ , the Ru-Sn/GAC

catalyst displayed an apparent activation energy (62.2 kJ
mol⁻¹) that was in line with past reports for monocarboxylic
acid hydrogenation over Ru for acetic acid (53 kJ mol⁻¹) and
propionic acid (68 kJ mol⁻¹).⁸⁹ In order to achieve complete
conversion with BDO as the primary product (71% molar
yield), a significantly reduced WHSV of 0.06 h⁻¹ was
required. Although this space velocity is quite low, similar
retention times have been reported for the complete
reduction of lactic acid to propanediol.⁹⁰ Improved
understanding of the bimetallic active site may allow for
utilizing synthetic approaches that maximize metal
utilization and increase reactivity on a catalyst mass basis. In
addition to BDO, a significant amount of THF (15% molar
yield) was produced under these reaction conditions.
Although THF was not the target product, it has value with
numerous downstream applications for biobased solvents,
polymers, and textiles.⁹¹ Further work is needed to
determine the optimum preferred product distribution of
BDO, GBL, and THF based on economic and environmental
considerations for informed catalyst and process design.¹⁴,⁹²

3.3. Stable bimetallic catalyst design. Computational
modeling provided insights into the stability of Ru-Sn metal
crystallites in the presence of Ni from stainless steel
leaching (Figure 7). The preferential formation energies for
Ni-Sn over Ru-Sn suggest that alternative bimetallic
combinations should be evaluated if Ni deposition is
ongoing, as Sn will not stay associated with Ru over time.
Likewise, subsurface-to-surface segregation energies can be
used as an additional computational tool to screen potential
bimetallic systems that would resist intraparticle migration
over time. For validation, such computational approaches
can be combined with highly controlled bimetallic synthetic
strategies and operando studies to provide a clearer picture
of the active site and its stability under working conditions,
as well as the potential for deactivation and restructuring in
the presence of chelating organics and non-target impurities.

It should be noted that reactor sidewall leaching is not
the only possible avenue for the introduction of inorganic
impurities that can cause catalyst restructuring with succinic
acid. Significant carryover of inorganic impurities (e.g., Al,
Ca, Cl, K, Fe, Mg, Mn, Na, P, S) can result when processing
biomass feedstocks, whether from the plant matter itself or
during its deconstruction and pretreatment.⁹³ Similarly,
upstream biological conversion processes can introduce
unique impurities form the presence of residual amino acids,
growth media, and pH buffering salts. Limited studies have
investigated the impact of biogenic impurities on catalyst
performance and material structure over time.⁴³,⁹⁴⁻⁹⁶ Moving
forward, further work is needed to gain first principles
insights and establish fundamentally driven approaches to
stable and robust catalyst design for harsh biomass
conversion environments.

## 4. CONCLUSION

As demonstrated in this work, bimetallic Ru-Sn/GAC
can facilitate the continuous aqueous phase reduction of
succinic acid to BDO in high yields for prolonged time-on-
stream. The addition of Sn to Ru dramatically impacts the
catalyst affinity for H₂ and CO, resulting in negligible
uptake by chemisorption. TPR suggested the lack of a
surface Ru-Sn alloy, while high resolution STEM-EDS
confirmed the co-location of Ru and Sn. XPS analysis
following reduction confirmed the presence of partially
oxidized Ru-Sn, which may be responsible for surface
acidity that promotes GBL ring opening. Although, further
work is needed to understand the nature of the active site
after synthesis and under operando conditions that will be
addressed in future studies. With prolonged exposure to
reaction conditions in a trickle bed reactor, leaching of
stainless steel resulted in catalyst metal crystallite
restructuring to form Ni-Sn species. Computational
modeling confirmed favorable energetics for Ru-Sn
segregation and Ni-Sn formation at sub-monolayer Sn
incorporation, highlighting potential driving forces for Sn
migration from Ru-Sn to Ni particles. To address leaching,
the reactor tube was coated with an inert silica layer by
CVD. After silica coating, stainless steel leaching was
greatly reduced and the Ru-Sn catalyst displayed stable
performance with an activation energy of 62.2 MJ kg⁻¹
under partial conversion conditions (WHSV of 4 h⁻¹).
Reducing the WHSV to 0.06 h⁻¹ resulted in complete
conversion of succinic acid and a major molar product
distribution of 71% BDO and 15% THF. These results
highlight the potential of Ru-Sn/AC as a bimetallic catalyst
for converting succinic acid to BDO, while underscoring the
need for chemically compatible reactor metallurgy and
catalyst active site design for continuous processing.

## 5. MATERIALS AND METHODS

### 5.1. Catalyst Synthesis and Characterization.
Catalysts
were prepared on nitric acid treated AC powder and
granular supports using strong electrostatic adsorption for
primary metals and incipient wetness for secondary metals.
Catalysts were dried and reduced in pure H2 following
loading, and stored under ambient conditions with air
exposure unless otherwise indicated. Further details on
catalyst synthesis are provided in the Supporting
Information. Catalysts were characterized to determine
their fresh and post reaction material properties. Details for
XRD, N₂ physisorption, and SEM-EDX are described
elsewhere.⁹⁷ Further detail on TEM, STEM, chemisorption,
TPR, ammonia TPD, and pyridine DRIFTS are provide in
the Supporting Information.

### 5.3. Catalytic Testing and Chemical Analysis.
Batch
reactor screening experiments were performed in a Parr
multi-batch reactor system (Parr Instrument Company).
Trickle bed reactor experiments were performed in a Parr
tubular reactor system (Parr Instrument Company). For
experiments to address stainless steel leaching, the reactor
tube was CVD coated with a silica Dursan® coating
provided by SilcoTek Coating Company. Further details on
both systems are provided in the Supporting Information.

For batch and trickle bed reactor runs, molar conversion was reported as moles of substrate reacted divided by the moles of substrate introduced to the reactor. Molar selectivity was reported as moles of target product divided by moles of substrate reacted. Molar yield is defined as molar conversion multiplied by molar selectivity. Concentrations of liquid substrate and products were determined by high performance liquid chromatography and gas chromatography mass spectroscopy, with further details provided in the Supporting Information.

5.5. Computational Modeling. Periodic density functional theory (DFT) calculations were carried out using Vienna Ab Initio Simulation Package (VASP), version 5.4.1.98-101 The ion-electron interactions were described using the projected augmented wave (PAW) potentials.102,103 The electron-electron exchange and correlation energies were computed using Perdew, Burke, and Ernzerhof (PBE) functional.104 The van der Waals (vdW) forces were calculated using the method of Tkatchenko and Scheffler (TS) as implemented in VASP.105 A 13×13×13, 15×15×15, and 19×19×13 Γ-centered k-meshes were used for bulk α-Sn, Ni and Pt, and Ru calculations, respectively. The Murnaghan-Birch equation of state was used to estimate bulk parameters, which were also confirmed to within 0.001 Å with single-point energy calculations.106,107 The resulting lattice parameters are in excellent agreement with previous experimental estimates (see Table S7).

A five-layer 4×4 surface was used to represent Ru(0001), Ni(111) and Pt(111) close-packed surfaces. The bottom two layers were frozen in the corresponding bulk-optimized positions while the top three layers were allowed to relax. The vacuum layer between slabs was set to 30 Å. A 400 eV cutoff energy and a 5×5×1 k-mesh were chosen for all calculations. The relaxation was performed until all forces were lower than 0.02 eV Å⁻¹ using a conjugate-gradient algorithm. Dipole corrections were included in all calculations.108,109 These parameters resulted in relative energy errors of less than 0.01 eV.

## AUTHOR INFORMATION
### Corresponding Author
*E-mail: [derek.vardon@nrel.gov](mailto:derek.vardon@nrel.gov)

### Notes
The authors declare no competing financial interest.

## ASSOCIATED CONTENT
### Supporting Information
XRD spectra, NH₃-TPD profiles, pyridine DRIFTS, TPR profiles, batch reactor Ru-Sn screening results based on bimetallic catalyst synthesis method, SEM-EDS and TEM images, particle size distributions, trickle-bed reactor molar yield data, ICP and XPS metal loadings, CO and H₂ chemisorption, nitrogen physisorption analysis, summary of peer-reviewed literature for bimetallic catalysts tested for succinic acid conversion to BDO, XPS peak fitting parameters, calculated lattice parameters

## ACKNOWLEDGEMENTS
We would like to thank the US Department of Energy Bioenergy Technologies Office for funding this work via Contract No. DE-AC36-08GO28308 at the National Renewable Energy Laboratory. Also, this work was performed in collaboration with the Chemical Catalysis for Bioenergy Consortium (ChemCatBio), a member of the Energy Materials Network (EMN) and was supported by the DOE Bioenergy Technology Office under Contract no DE-AC05-00OR22725 with ORNL and Contract no. DE-AC36-08-GO28308 with NREL. S/TEM experiments were performed using instrumentation (FEI Talos F200X STEM) provided by the Department of Energy, Office of Nuclear Energy, Fuel Cycle R&D Program and the Nuclear Science User Facilities. The computational work was supported in part by the Consortium for Computational Physics and Chemistry funded by the U.S. Department of Energy's Bioenergy Technologies Office (DE-AC36-08GO28308). The authors are grateful for supercomputer time on Stampede provided by the Texas Advanced Computing Center (TACC) under the National Science Foundation Extreme Science and Engineering Discovery Grant MCB09159, and the NREL Computational Sciences Center, which is supported by the DOE Office of EERE under Contract No. DE-AC36- 08GO28308. Support for KXS was provided by proceeds from NREL's intellectual property licensing program. We would also like to thank Glenn Teeter at NREL for his assistance with XPS analysis. The U.S. Government retains and the publisher, by accepting the article for publication, acknowledges that the U.S. Government retains a nonexclusive, paid up, irrevocable, worldwide license to publish or reproduce the published form of this work, or allow others to do so, for U.S. Government purposes.

### References
(1) Cok, B.; Tsiropoulos, I.; Roes, A. L.; Patel, M. K. *Biofuels Bioprod. Biorefining* **2014**, 8, 16–29.
(2) Guettler, M. V.; Rumler, D.; Jain, M. K. *Int. J. Syst. Bacteriol.* **1999**, 49, 207–216.
(3) Lee, P. C.; Lee, S. Y.; Hong, S. H.; Chang, H. N. *Appl Microbiol Biotechnol* **2002**, 58, 663–668.
(4) Kim, D. Y.; Yim, S. C.; Lee, P. C.; Lee, W. G.; Lee, S. Y.; Chang, H. N. *Enzyme Microb. Technol.* **2004**, 35, 648–653.
(5) Li, J.; Zheng, X.-Y.; Fang, X.-J.; Liu, S.-W.; Chen, K.-Q.; Jiang, M.; Wei, P.; Ouyang, P.-K. *Bioresour. Technol.* **2011**, 102, 6147–6152.
(6) Heerden, C.; Nicol, W. *Biochem Eng J* **2013**, 73, 5-11.
(7) Akhtar, J.; Idris, A.; Abd. Aziz, R. *Appl. Microbiol. Biotechnol.* **2014**, 98, 987–1000.
(8) Choi, S.; Song, H.; Lim, S. W.; Kim, T. Y.; Ahn, J. H.; Lee, J. W.; Lee, M.-H.; Lee, S. Y. *Biotechnol. Bioeng.* **2016**, 113, 2168–2177.
(9) Salvachúa, D.; Mohagheghi, A.; Smith, H.; Bradfield, M. F. A.; Nicol, W.; Black, A. B.; Biddy, M. J.; Dowe, N.; Beckham, G. T. *Biotechnol. Biofuels* **2016**, 9, 1–15.
(10) Salvachúa, D.; Smith, H.; John, P. C. S.; Mohagheghi, A.; Peterson, D. J.; Black, B. A.; Dowe, N.; Beckham, G. T. *Bioresour. Technol.* **2016**, 214, 558–566.
(11) Delhomme, C.; Weuster-Botz, D.; Kühn, F. E. *Green Chem.* **2009**, 11, 13–26.
(12) Davis, R.; Tao, L.; Biddy, M. J.; Beckham, G. T.; Scarlata, C.; Jacobson, J.; Cafferty, K.; Ross, J.; Lukas, J.; Knorr, D.; Schoen, P. *NREL Tech. Rep.* **2013**, 88–101.
(13) Haas, T.; Jaeger, B.; Weber, R.; Mitchell, S. F.; King, C. F. *Appl. Catal. Gen.* **2005**, 280, 83–88.
(14) Adom, F.; Dunn, J. B.; Han, J.; Sather, N. *Environ. Sci. Technol.* **2014**, 48, 14624–14631.
(15) Ly, B. K.; Tapin, B.; Aouine, M.; Delichere, P.; Epron, F.; Pinel, C.; Especel, C.; Besson, M. *ChemCatChem* **2015**, 7, 2161–2178.
(16) Ly, B. K.; Minh, D. P.; Pinel, C.; Besson, M.; Tapin, B.; Epron, F.; Especel, C. *Top. Catal.* **2012**, 55, 466–473.
(17) Minh, D. P.; Besson, M.; Pinel, C.; Fuertes, P.; Petitjean, C. *Top. Catal.* **2010**, 53, 1270–1273.
(18) Tapin, B.; Epron, F.; Especel, C.; Ly, B. K.; Pinel, C.; Besson, M. *Catal. Today* **2014**, 235, 127-133.
(19) Tapin, B.; Epron, F.; Especel, C.; Ly, B. K.; Pinel, C.; Besson, M. *ACS Catal.* **2013**, 3, 2327–2335.
(20) Takeda, Y.; Tamura, M.; Nakagawa, Y.; Okumura, K.; Tomishige, K. *Catal. Sci. Technol.* **2016**, 6, 5668–5683.
(21) Corbel-Demailly, L.; Ly, B.-K.; Minh, D.-P.; Tapin, B.; Especel, C.; Epron, F.; Cabiac, A.; Guillon, E.; Besson, M.; Pinel, C. *ChemSusChem* **2013**, 6, 2388–2395.
(22) Krammer, P.; Vogel, H. J. *Supercrit. Fluids* **2000**, 16, 189–206.
(23) Wan, H.; Chaudhari, R. V.; Subramaniam, B. *Energy Fuels* **2013**, 27, 487–493.
(24) Pritchard, J.; Filonenko, G. A.; Putten, R. van; Hensen, E. J. M.; Pidko, E. A. *Chem. Soc. Rev.* **2015**, 44, 3808–3833.
(25) Michel, C.; Gallezot, P. *ACS Catal.* **2015**, 5, 4130–4132.
(26) Deshpande, R. .; Buwa, V. .; Rode, C. .; Chaudhari, R. .; Mills, P. . *Catal. Commun.* **2002**, 3, 269–274.
(27) BASF. Metal Price History Charts http://apps.catalysts.basf.com/apps/eibprices/mp/DPCharts.aspx (accessed Mar 8, 2017).
(28) Zhu, Z.; Lu, Z.; Li, B.; Guo, S. *Appl. Catal. Gen.* **2006**, 302, 208–214.
(29) Wettstein, S. G.; Bond, J. Q.; Alonso, D. M.; Pham, H. N.; Datye, A. K.; Dumesic, J. A. *Appl. Catal. B Environ.* **2012**, 117–118, 321–329.
(30) Cheah, K.; Tang, T.; Mizukami, F.; Niwa, S.; Toba, M.; Choo, Y. *J. Am. Oil Chem. Soc.* **1992**, 69, 410–416.
(31) Tahara, K.; Tsuji, H.; Kimura, H.; Okazaki, T.; Itoi, Y.; Nishiyama, S.; Tsuruya, S.; Masai, M. *Catal. Today* **1996**, 28, 267–272.
(32) Tahara, K.; Nagahara, E.; Itoi, Y.; Nishiyama, S.; Tsuruya, S.; Masai, M. *Appl. Catal. Gen.* **1997**, 154, 75–86.
(33) Toba, M.; Tanaka, S.; Niwa, S.; Mizukami, F.; Koppány, Z.; Guczi, L.; Cheah, K.-Y.; Tang, T.-S. *Appl. Catal. Gen.* **1999**, 189, 243–250.
(34) Fontana, J.; Vignado, C.; Jordao, E.; Figueiredo, F. C. A.; Carvalho, W. A. *Catal. Today* **2011**, 172, 27–33.
(35) Silva, A. M.; Morales, M. A.; Baggio-Saitovitch, E. M.; Jordão, E.; Fraga, M. A. *Appl. Catal. Gen.* **2009**, 353, 101–106.
(36) Jiang, H.-B.; Jiang, H.-J.; Su, K.; Zhu, D.-M.; Zheng, X.-L.; Fu, H.-Y.; Chen, H.; Li, R.-X. *Appl. Catal. Gen.* **2012**, 447–448, 164–170.
(37) Silva, A. M.; Santos, O. A. A.; Mendes, M. J.; Jordão, E.; Fraga, M. A. *Appl. Catal. Gen.* **2003**, 241, 155–165.
(38) Wiles, C.; Watts, P. *Green Chem.* **2014**, 16, 55–62.
(39) Besson, M.; Gallezot, P. *Catal. Today* **2003**, 81, 547–559.
(40) Héroguel, F.; Rozmysłowicz, B.; Luterbacher, J. S. *Chim. Int. J. Chem.* **2015**, 69, 582–591.


(41) Moulijn, J. A.; van Diepen, A. E.; Kapteijn, F. *Appl. Catal. Gen.* **2001**, *212*, 3–16.

(42) Sádaba, I.; Granados, M. L.; Riisager, A.; Taarning, E. *Green Chem.* **2015**, *17*, 4133–4145.

(43) Schwartz, T. J.; O’Neill, B. J.; Shanks, B. H.; Dumesic, J. A. *ACS Catal.* **2014**, *4* (6), 2060–2069.

(44) Hao, X.; Quach, L.; Korah, J.; Spieker, W. A.; Regalbuto, J. R. *J. Mol. Catal. Chem.* **2004**, *219* (1), 97–107.

(45) Jiao, L.; Zha, Y.; Hao, X.; Regalbuto, J. R. In *Studies in Surface Science and Catalysis*; E.M. Gaigneaux, M. D., D. E.De Vos, S.Hermans, P. A.Jacobs, J. A.Martens and P.Ruiz, Ed.; Scientific Bases for the Preparation of Heterogeneous Catalysts; Elsevier, 2006; Vol. 162, pp 211–218.

(46) Dandekar, A.; Baker, R. T. K.; Vannice, M. A. *Carbon* **1998**, *36*, 1821–1831.

(47) Lennon, D.; Lundie, D. T.; Jackson, S. D.; Kelly, G. J.; Parker, S. F. *Langmuir* **2002**, *18*, 4667–4673.

(48) Gupta, S.; Arora, R.; Sinha, N.; Imteyaz Alam, M.; Ali Haider, M. *RSC Adv.* **2016**, *6*, 12932–12942.

(49) Huang, S.-Y.; Chang, S.-M.; Yeh, C. *J. Phys. Chem. B* **2006**, *110*, 234–239.

(50) Mendes, M. .; Santos, O. A. .; Jordão, E.; Silva, A. . *Appl. Catal. Gen.* **2001**, *217*, 253–262.

(51) Pouilloux, Y.; Autin, F.; Guimon, C.; Barrault, J. *J. Catal.* **1998**, *176*, 215–224.

(52) Hara, Y.; Endou, K. *Appl. Catal. Gen.* **2003**, *239*, 181–195.

(53) de Miguel, S. R.; Román-Martínez, M. C.; Jablonski, E. L.; Fierro, J. L. G.; Cazorla-Amorós, D.; Scelza, O. A. *J. Catal.* **1999**, *184*, 514–525.

(54) Maris, E. P.; Davis, R. J. *J. Catal.* **2007**, *249*, 328–337.

(55) Montassier, C.; Ménézo, J. C.; Hoang, L. C.; Renaud, C.; Barbier, J. *J. Mol. Catal.* **1991**, *70*, 99–110.

(56) Ernst, M. A.; Sloof, W. G. *Surf. Interface Anal.* **2008**, *40* (3), 334–337.

(57) Armenise, S.; Roldán, L.; Marco, Y.; Monzón, A.; García-Bordejé, E. *J. Phys. Chem. C* **2012**, *116*, 26385–26395.

(58) Morgan, D. J. *Surf. Interface Anal.* **2015**, *47*, 1072–1079.

(59) Beran, J.; Hishita, S.; Mašek, K.; Matolín, V.; Haneda, H. *Ceram. Int.* **2014**, *40*, 323–329.

(60) Liu, J.; Wang, C.; Yang, Q.; Gao, Y.; Zhou, X.; Liang, X.; Sun, P.; Lu, G. *Sens. Actuators B Chem.* **2016**, *224*, 128–133.

(61) Xu, G.; Zhang, J.; Wang, S.; Zhao, Y.; Ma, X. *RSC Adv.* **2016**, *6*, 51005–51013.

(62) Gallezot, P.; Cerino, P. J.; Blanc, B.; Flèche, G.; Fuertes, P. *J. Catal.* **1994**, *146*, 93–102.

(63) Wang, D.; Bierwagen, G. P. *Prog. Org. Coat.* **2009**, *64*, 327–338.

(64) L. Zheludkevich, M.; Miranda Salvado, I.; S. Ferreira, M. G. *J. Mater. Chem.* **2005**, *15*, 5099–5111.

(65) Vasconcelos, D. C. L.; Carvalho, J. A. N.; Mantel, M.; Vasconcelos, W. L. *J. Non-Cryst. Solids* **2000**, *273*, 135–139.

(66) Ruban, A. V.; Skriver, H. L.; Nørskov, J. K. *Phys. Rev. B* **1999**, *59*, 15990–16000.

(67) Greeley, J.; Nørskov, J. K. *Electrochimica Acta* **2007**, *52*, 5829–5836.

(68) Primo, A.; Concepción, P.; Corma, A. *Chem. Commun.* **2011**, *47*, 3613–3615.

(69) Olcay, H.; Xu, Y.; Huber, G. W. *Green Chem.* **2014**, *16*, 911–924.

(70) Olcay, H.; Xu, L.; Xu, Y.; Huber, G. W. *ChemCatChem* **2010**, *2*, 1420–1424.

(71) Zhang, Z.; Jackson, J. E.; Miller, D. J. *Appl. Catal. Gen.* **2001**, *219*, 89–98.

(72) Zhang, Z.; Jackson, J. E.; Miller, D. J. *Ind. Eng. Chem. Res.* **2002**, *41*, 691–696.

(73) Chen, Y.; Miller, D. J.; Jackson, J. E. *Ind. Eng. Chem. Res.* **2007**, *46*, 3334–3340.

(74) Chen, L.; Zhu, Y.; Zheng, H.; Zhang, C.; Li, Y. *Appl. Catal. Gen.* **2012**, *411–412*, 95–104.

(75) Chen, L.; Zhu, Y.; Zheng, H.; Zhang, C.; Zhang, B.; Li, Y. *J. Mol. Catal. Chem.* **2011**, *351*, 217–227.

(76) Chiu, C.; Genest, A.; Rösch, N. *Top. Catal.* **2013**, *56*, 874–884.

(77) Zhao, Z.-J.; Chiu, C.; Gong, J. *Chem. Sci.* **2015**, *6*, 4403–4425.

(78) Alcala, R.; Shabaker, J. W.; Huber, G. W.; Sanchez-Castillo, M. A.; Dumesic, J. A. *J. Phys. Chem. B* **2005**, *109*, 2074–2085.

(79) Hook, A.; Massa, J. D.; Celik, F. E. *J. Phys. Chem. C* **2016**, *120*, 27307–27318.

(80) Yang, M.-L.; Zhu, Y.-A.; Zhou, X.-G.; Sui, Z.-J.; Chen, D. *ACS Catal.* **2012**, *2*, 1247–1258.

(81) Corma, A.; Nemeth, L. T.; Renz, M.; Valencia, S. *Nature* **2001**, *412*, 423–425.

(82) Michel, C.; Zaffran, J.; Ruppert, A. M.; Matras-Michalska, J.; Jędrzejczyk, M.; Grams, J.; Sautet, P. *Chem. Commun.* **2014**, *50*, 12450–12453.

(83) Li, L.; Qu, W.; Zhang, X.; Lu, J.; Chen, R.; Wu, F.; Amine, K. *J. Power Sources* **2015**, *282*, 544–551.

(84) Xiong, H.; Pham, H. N.; Datye, A. K. *Green Chem.* **2014**, *16*, 4627–4643.

(85) Abdelrahman, O. A.; Luo, H. Y.; Heyden, A.; Román-Leshkov, Y.; Bond, J. Q. *J. Catal.* **2015**, *329*, 10–21.

(86) Lu, J.; Elam, J. W.; Stair, P. C. *Surf. Sci. Rep.* **2016**, *71*, 410–472.

(87) Munnik, P.; de Jongh, P. E.; de Jong, K. P. *Chem. Rev.* **2015**, *115*, 6687–6718.

(88) Dunn, J. B.; Savage, P. E. *Green Chem.* **2003**, *5*, 649–655.

(89) Shih, Y.-S.; Lee, C.-K. *J. Chin. Chem. Soc.* **1985**, *32*, 29–34.

(90) Cortright, R. D.; Sanchez-Castillo, M.; Dumesic, J. A. *Appl. Catal. B Environ.* **2002**, *39*, 353–359.

(91) Choi, S.; Song, C. W.; Shin, J. H.; Lee, S. Y. *Metab. Eng.* **2015**, *28*, 223–239.

(92) Biddy, M. J.; Davis, R.; Humbird, D.; Tao, L.; Dowe, N.; Guarnieri, M. T.; Linger, J. G.; Karp, E. M.; Salvachúa, D.; Vardon, D. R.; Beckham, G. T. *ACS Sustain. Chem. Eng.* **2016**, *4*, 3196-3211.

(93) Vassilev, S. V.; Baxter, D.; Andersen, L. K.; Vassileva, C. G.; Morgan, T. J. *Fuel* **2012**, *94*, 1–33.

(94) Schwartz, T. J.; Johnson, R. L.; Cardenas, J.; Okerlund, A.; Da Silva, N. A.; Schmidt-Rohr, K.; Dumesic, J. A. *Angew. Chem. Int. Ed.* **2014**, *53*, 12718–12722.

(95) Zhang, Z.; Jackson, J. E.; Miller, D. J. *Bioresour. Technol.* **2008**, *99*, 5873–5880.

(96) Schwartz, T. J.; Brentzel, Z. J.; Dumesic, J. A. *Catal. Lett.* **2014**, *145*, 15–22.

(97) Vardon, D. R.; Sharma, B. K.; Humberto Jaramillo; Kim, Dongwook; Choe, Jong Kwon; Ciesielski, Peter; Strathmann, Timothy J. *Green Chem.* **2014**, *16*, 1507–1520.

(98) Kresse, G.; Furthmüller, J. *Phys. Rev. B* **1996**, *54*, 11169–11186.

(99) Kresse, G.; Furthmüller, J. *Comput. Mater. Sci.* **1996**, *6*, 15–50.

(100) Kresse, G.; Hafner, J. *Phys. Rev. B* **1993**, *47*, 558–561.

(101) Kresse, G.; Hafner, J. *Phys. Rev. B* **1994**, *49*, 14251–14269.

(102) Blöchl, P. E. *Phys. Rev. B* **1994**, *50*, 17953–17979.

(103) Kresse, G.; Joubert, D. *Phys. Rev. B* **1999**, *59*, 1758.

(104) Perdew, J. P.; Burke, K.; Ernzerhof, M. *Phys. Rev. Lett.* **1996**, *77*, 3865–3868.

(105) Tkatchenko, A.; Scheffler, M. *Phys. Rev. Lett.* **2009**, *102*, 73005.

(106) Murnaghan, F. D. *Proc. Natl. Acad. Sci.* **1944**, *30*, 244–247.

(107) Birch, F. *Phys. Rev.* **1947**, *71*, 809–824.

(108) Makov, G.; Payne, M. C. *Phys. Rev. B* **1995**, *51*, 4014–4022.

(109) Neugebauer, J.; Scheffler, M. *Phys. Rev. B* **1992**, *46*, 16067–16080.

TOC Image:

![](./images/813113353437184001_12.jpg)