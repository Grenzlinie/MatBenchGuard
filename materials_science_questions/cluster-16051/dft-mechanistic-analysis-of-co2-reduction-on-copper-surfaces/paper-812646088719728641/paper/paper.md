![](./images/812646088719728641_1.jpg)

Subscriber access provided by BIU Pharmacie | Faculté de Pharmacie, Université Paris V

Physical Insights into Chemistry, Catalysis, and Interfaces

# Towards Engineering of Solution Microenvironments for the CO Reduction Reaction: Unraveling pH and Voltage Effects from a Combined Density-Functional–Continuum Theory

Stephen E Weitzner, Sneha A Akhade, Joel B. Varley, Brandon C. Wood, Eric B. Duoss, Sarah E Baker, and Minoru Otani

J. Phys. Chem. Lett., Just Accepted Manuscript • DOI: 10.1021/acs.jpclett.0c00957 • Publication Date (Web): 28 Apr 2020

Downloaded from pubs.acs.org on April 29, 2020

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Towards Engineering of Solution Microenvironments for the $CO_2$ Reduction Reaction: Unraveling pH and Voltage Effects from a Combined Density-Functional–Continuum Theory

Stephen E. Weitzner, $^{*, \dagger}$ Sneha A. Akhade, $^{\dagger}$ Joel B. Varley, $^{*, \dagger}$ Brandon C. Wood, $^{\dagger}$ Eric B. Duoss, $^{\dagger}$ Sarah E. Baker, $^{\dagger}$ and Minoru Otani$^{\ddagger}$

$^{\dagger}$Lawrence Livermore National Laboratory, Livermore, California 94550, United States

$^{\ddagger}$National Institute of Advanced Industrial Science and Technology (AIST), 1-1-1 Umezono, Tsukuba 305-8568, Japan

E-mail: weitzner1@llnl.gov; varley2@llnl.gov

### Abstract

Engineering the electrolyte microenvironment represents an attractive route to tuning the selectivity of electrocatalytic reactions beyond catalyst composition and morphology. However, harnessing the full potential of this approach requires understanding the interplay between voltage, electrolyte composition, and adsorbate binding within the electrical double layer, which is absent from usual theoretical approaches. In this work, we apply a recently developed density functional theory (DFT)-continuum approach based on the effective screening medium method and reference interaction site model (ESM-RISM) to explore electrolyte effects with an enhanced description of the electrochemical interface. Applying this method to the binding of CO adsorbates in potassium-containing electrolytes on copper—a problem of direct relevance to CO₂ electroreduction to value-added products—we show that the interdependence of voltage and pH leads to an unexpected change in adsorption site preference on Cu(001) terraces. Our findings highlight the often-overlooked importance of electrical double-layer structure for predicting catalyst operation.

### Graphical TOC Entry

![](./images/812646088719728641_2.jpg)

The electrochemical conversion of $CO_2$ into value-added products using liquid- or gas-fed electrolyzers is an attractive approach for the sustainable production of chemical fuels and feedstocks. Over the past several decades, an extensive search has been conducted for electrocatalysts that simultaneously exhibit both high activity and high selectivity towards desirable products such as hydrocarbons and oxygenates. $^{1,2}$ Yet despite the intensity of this search, copper-based catalysts remain the only known electocatalysts that produce alcohols and hydrocarbons at appreciable rates. Unfortunately, this class of $CO_2$ reduction catalysts generally exhibits poor selectivities, creating a significant hurdle to the deployment of industrial-scale electrochemical reactors for $CO_2$ conversion. $^{3}$

Efforts to improve the intrinsic selectivity of copper catalysts for the $CO_2$ reduction ($CO_2R$) reaction have mostly focused on engineering the copper catalyst surface, as well as the architecture and design of the electrolyzer assembly itself. However, the activity and selectivity of copper catalysts have also been shown to exhibit a remarkable sensitivity to the composition, concentration, and pH of the electrolyte solution. $^{4-8}$ Furthermore, this solution microenvironment may be controlled by leveraging the design of the electrochemical reactor itself, which can nontrivially affect mass transport to the interfacial region to influence transient local concentrations of solubilized species. $^{2,9-11}$ Therefore, properly understanding the complex interplay between the solution microenvironment and the underlying reaction mechanisms can open up new pathways for the development of optimized electrochemical reactors with high selectivity.

Most theoretical studies of the $CO_2R$ reaction have focused on understanding the energy landscape using model planar electrodes and adsorbates under vacuum conditions. In particular, planewave density functional theory (DFT) calculations have been routinely employed to compute theoretical descriptors such as the binding energy of key $CO_2R$ reaction intermediates on copper surfaces as well as the energy barriers of elementary steps in the reaction pathway. $^{2,12,13}$ The choice of vacuum conditions is for computational convenience due to the high cost of planewave DFT calculations, yet it lacks the ability to properly de-

scribe the electrical double layer. In some cases, small amounts of explicit water molecules and ions have been included along with sawtooth potentials to capture some effects of the electrical double layer;⁷,¹⁴⁻¹⁶ however, these methods are insufficient for realizing a full range of possible solution environments.

Recently, embedded DFT-continuum approaches have emerged as a promising alternative that incorporates an implicit description of the electrolyte with modest additional computational expense. Such methods have been used to examine the effects of the electrochemical environment on CO₂R,¹⁷⁻¹⁹ and can go beyond vacuum calculations to account for interface polarization and the charge-voltage response of the electrode-solution interface.¹⁷,²⁰⁻²² Nevertheless, while a variety of prescriptive computational schemes have been proposed to model environmental effects on CO₂R, the rigorous ability to simultaneously describe electrolyte composition effects and polarization response to applied voltage within planewave DFT has remained an ongoing challenge.

In this Letter, we demonstrate the use of a recently implemented DFT-continuum approach based on the effective screening medium method and the reference interaction site model (ESM-RISM) to model electrolyte composition effects on CO adsorption free energies, a key performance descriptor in CO₂R.²,²³,²⁴ Unlike conventional embedded approaches that rely on the definition of a dielectric cavity and the use of corrective schemes to contend with the periodic boundary conditions of planewave DFT, ESM-RISM instead relies upon a classical description of the liquid environment and employs Green’s function techniques to directly model electrified interfaces within open boundary conditions.²⁵⁻²⁷ As shown in Fig. 1a, this formalism enables the determination of spatial distributions of fluid components under constant electrochemical boundary conditions, rendering a detailed statistical description of the electrical double layer structure as a function of voltage and solution composition. Moreover, as shown in Fig. 1b, the approach can describe the spatial variation of the electrostatic potential within the electrical double layer, addressing some of the recently reported limitations of embedded DFT-continuum approaches for catalysis applications.²⁸

![](./images/812646088719728641_3.jpg)

Figure 1: (a) The average concentration of $K^+$ (blue) and $Cl^-$ (orange) near the Cu(100) surface in 0.1 M KCl at potentials of $-0.4$ V/RHE (solid) and $-0.8$ V/RHE (dashed). The Debye length $L_D = 9.6$ Å estimated from the ionic strength of the solution is drawn in gray. (b) The electrostatic potential within the composite DFT-RISM cell at $-0.8$ V/RHE. The oscillation in the potential beginning near 3 Å is due to the classical charge density of the polarized electrolyte.

In what follows, we employ this new capability to examine how the binding energy of CO on the copper (100), (211), and (321) surfaces varies as a function of pH and applied voltage in potassium-containing electrolytes. These representative surface models allow us to evaluate the influence of the electrochemical environment on CO adsorption on terrace, step-edge, and kink sites on the Cu surface under typical $CO_2R$ operating conditions. As we will show, explicit inclusion of the solution microenvironment critically alters the site binding preferences, which change qualitatively as a function of solution composition and operating

conditions as the electrolyte restructures in response to interface polarization.

In order to assess the effects of pH and voltage on the binding energy of CO, we consider several commonly used electrolytes that are summarized in Table 1 spanning a pH range of 1–13 while maintaining a constant concentration of 0.1 M $K^+$. We note that all solutions

Table 1: Solutions modeled in this study along with their pH, molar ionic strength $I$, and estimated Debye length $L_D$.

| Solution composition               | pH | $I$ [M] | $L_D$ [Å] |
|:-----------------------------------|:---|:--------|:----------|
| 0.1 M KCl + 0.1 M HCl              | 1  | 0.2     | 6.8       |
| 0.1 M KCl + $10^{-4}$ M HCl        | 4  | 0.1     | 9.6       |
| 0.1 M KCl                          | 7  | 0.1     | 9.6       |
| 0.1 M KCl + $10^{-4}$ M KOH        | 10 | 0.1     | 9.6       |
| 0.1 M KOH                          | 13 | 0.1     | 9.6       |

have an ionic strength of 0.1 M, save for the pH 1 solution composed of 0.1 M KCl and 0.1 M HCl, which has an ionic strength of 0.2 M. The estimated Debye length of the pH 1 solution is 2.8 Å shorter compared to the other solutions, leading to an increase in the surface charge at certain potentials. We then consider the adsorption of CO at the copper surface ($CO^*$) in each solution at a fixed voltage $\Phi$

$$
\mathrm{CO(aq)} + * \stackrel{\Phi}{\longrightarrow} \mathrm{CO^*,} \tag{1}
$$

where the CO molecule is initially dissolved in the same solution. The binding free energy is computed as a difference of electrochemical Gibbs free energies

$$
\Delta G_b(\Phi) = G_{\mathrm{CO^*}}(\Phi) - G_*(\Phi) - G_{\mathrm{CO}}, \tag{2}
$$

where $G_{\mathrm{CO^*}}(\Phi) = \Omega_{\mathrm{CO^*}}(\Phi) + E_{\mathrm{ZPE}} + \int C_v dT - TS$, $\Omega_{\mathrm{CO^*}}(\Phi)$ is the electronic grand potential of the CO-covered surface, $G_*(\Phi) = \Omega_*(\Phi)$ is the electronic grand potential of the clean copper surface, and $G_{\mathrm{CO}} = A_{\mathrm{CO}} + \int C_p dT + E_{\mathrm{ZPE}} - TS$, where $A_{\mathrm{CO}}$ is the free energy of the solvated CO molecule. We note that while CO adsorption at transition metal surfaces is well-known as being challenging to treat within conventional Kohn-Sham DFT (c.f., the

"CO/Pt(111) Puzzle" introduced by Feibelman and co-workers nearly two decades ago²⁹), the introduction of long range interactions through the use of van der Waals functionals often provides both qualitative and quantitative improvements in both the adsorption site preference and binding energy of CO in these systems.³⁰,³¹ In this work, we have used the BEEF-vdw exchange-correlation functional³² as it provides an affordable balance of accuracy and efficiency, while providing a similar predictive accuracy as more expensive hybrid PBE0 and HSE03 functionals for the copper surface.³³ For a full accounting of the numerical DFT and RISM parameters used in this work, see Section S1 of the Supporting Information. The entropy of dissolved CO contains vibrational, rotational, and translational contributions, while the entropy of the adsorbed CO contains only vibrational contributions as detailed in Section S2 of the Supporting Information.

While CO binding is traditionally considered to be a non-electrochemical step in the reduction of CO or CO₂, we expect the binding energy to exhibit some voltage dependence due to variations in the surface properties from electrocapillary effects and the interfacial electric field associated with an applied electrode potential. This field effect is modulated by the local concentration of cations near the negatively charged electrode surface, as depicted in Fig. 2, which shows the spatial distributions of potassium cations near the CO covered Cu(100) surface at several different voltages in 0.1 M KCl. The potential of zero charge of the configuration shown in Fig. 2 in 0.1 M KCl is $-0.18$ V/RHE ($-0.59$ V/SHE). As anticipated, we observe that as the electrode potential is made more negative relative to the potential of zero charge, the local concentration of potassium ions builds up in response, thereby increasing the magnitude of the local interfacial electric field.

In Fig. 3, we show that voltage significantly affects the binding free energy (Eq. 2) of CO on the Cu(100) terrace, and that the degree of the effect depends on the solution considered. Perhaps more importantly, the specific interplay between solution composition and voltage depends on the adsorption site. Here we observe that at potentials close to 0 V/RHE, CO exhibits a similar binding free energy across each adsorption site, but exhibits a site

![](./images/812646088719728641_4.jpg)

Figure 2: Iso-concentration levels of $K^+$ over the polarized Cu(100) surface in contact with a 0.1 M KCl solution at voltages ranging between $-0.2$ and $-1.4$ V/RHE. Molar $K^+$ concentrations are shown to highlight the complex evolution of the electrical double layer structure at the polarized interface. CO* is shown bound within a hollow site.

preference order of atop $>$ bridge $>$ hollow based on the relative energetics between these systems. This trend is equivalent to what one would find in vacuum both with and without an externally applied electric field, as shown in Fig. S6 of the Supporting Information. However, as the voltage on the electrode becomes more cathodic and the surface charge becomes more negative, the site preference for CO switches from atop to bridge and then from bridge to hollow, ultimately exhibiting a site preference order of hollow $>$ bridge $>$ atop as the potential approaches $-1.5$ V/RHE. The potentials at which these transitions occur shifts towards more positive potentials with increasing pH on the RHE scale, and we note that atop adsorption is predicted to become increasingly unfavorable at all potentials with increasing solution alkalinity. Moreover, Fig. 3 demonstrates that the binding free energy of CO adsorbed at bridge and hollow sites are close in energy throughout the sampled voltage range, indicating

![](./images/812646088719728641_5.jpg)

Figure 3: Voltage-dependent CO binding free energies at the atop (blue), bridge (red), and hollow (green) sites of the Cu(100) surface across a pH range of 1-13. Voltages are reported on the RHE scale. Colored regions indicate the most stable site geometry within each voltage range.

that when CO adsorbs on a copper (100) terrace under cathodic conditions, it exhibits a general preference to adsorb at multicoordinated sites. This finding is consistent with recent spectroscopic work by Gunathunge *et al.*, who observed the presence of an electrochemically inert population of CO adsorbed at bridge and hollow sites on polycrystalline copper surfaces in alkaline electrolytes.¹⁶ Notably, our methodology provides a physical explanation for this observation, which can be traced to voltage-induced restructuring of the electrolyte solution that destabilizes the atop site to reveal competition between multicoordinated sites.

The voltage-induced switching of site preference may have additional practical consequences for tuning electrochemical selectivity via the solution microenvironment. In particular, the preferential formation of bridge-bound CO* is attractive for formation of C₂ products, as these sites have shown favorable reaction barriers for coupling to form CO dimers, which are precursors for ethylene and multi-carbon oxygenates.²,³⁴,³⁵ Furthermore,

![](./images/812646088719728641_6.jpg)

Figure 4: CO adsorption at atop sites on the Cu(100), Cu(211), and Cu(321) surfaces. The lines connecting markers are present as a guide to highlight the effect of pH on the binding free energy of CO at $-1$ V/RHE.

the observation in Fig. 3 that multi-coordinated sites become increasingly favored in more alkaline environments and under more reductive potentials, thereby making CO-CO coupling more amenable, is consistent with the highly alkaline conditions adopted in recent $CO_2R$ experiments reporting high $C_2$-selectivities.$^{36,37}$

In addition to planar (001) terraces, we investigated CO adsorption at highly under-coordinated sites, represented by step edge and kink sites on the Cu(211) and Cu(321) surfaces, respectively. As expected and as shown in Fig. 4, we also observe that CO binds more strongly to the copper surface as the coordination environment of the adsorption site decreases in the order kink $>$ step edge $>$ terrace.$^{13,38}$ By comparing to the results obtained for the Cu(100) surface (Fig. 3), Fig. 4 indicates that the solution pH has an even stronger effect on relative stability when CO is adsorbed on low-coordination step edges or kink sites. In particular, we observe that variations in the solution pH modify the binding free energy of CO at a given potential on the RHE scale, as can be seen in the highlighted

variations on each surface at a fixed potential of $\Phi = -1$ V/RHE within Fig. 4. While the energy variations at a fixed voltage span less than 0.1 eV, we note that the ability to detect such energetic shifts under a particular set of electrochemical conditions could enable accurate activity descriptors for engineering $\text{CO}_2\text{R}$ catalysts that are sensitive to electrolyte composition and solution microenvironment effects. $^{39}$ Perhaps more importantly, accurate calculation of solution-mediated reaction free energies of elementary steps and transition states in the $\text{CO}_2\text{R}$ reaction pathway would enable electrolyte-sensitive catalyst selectivity descriptors. Because selectivity tends to be especially sensitive to fine differences in relative reaction energetics, this is a particularly promising gateway for solution microenvironment optimization.

In summary, we have used the recently developed ESM-RISM DFT-continuum approach to assess the influence of pH and voltage effects on the binding free energies of CO on model copper surfaces at terrace, step edge, and kink sites in common potassium-containing electrolytes. Our results indicate that CO binding on Cu(100) terraces is preferentially tuned towards multicoordinated bridge or hollow sites under cathodic conditions due to restructur- ing of the solution environment, providing a physical basis for recent in situ spectroscopic observations in alkaline media. $^{16}$ This preference is also shifted to smaller reducing potentials with increased alkalinity. On the other hand, the relative energetic ordering of the latter surface sites is preserved, generally favoring under-coordinated sites and demonstrating that the interplay between solution composition and applied voltage depends strongly on the nature of the surface morphology. These results highlight the influence that solution pH and applied voltage can have in tuning energetics even for steps that may be perceived to be non-electrochemical in nature. Exploiting the complex interplay within the solution mi- croenvironment to tune reaction energetics, such as site-dependent CO-CO coupling barriers for the increased formation of $\text{C}_2$ products in electrochemical $\text{CO}_2\text{R}$, is promoted as a key next step in engineering selectivity control in electrochemical reactions.

## Acknowledgement

This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344 and was supported with Laboratory Directed Research and Development funding under project numbers 19-SI-005 and 18-FS-019 and a cooperative research and development agreement with TOTAL American Services, Inc. under project number TC02307.

## Supporting Information Available

The Supporting Information is available free of charge:

Computational methods and ESM-RISM parameterization for copper (Section S1); Electrochemical modeling (Section S2).

## References

(1) Zhao, G.; Huang, X.; Wang, X.; Wang, X. Progress in catalyst exploration for heterogeneous CO 2 reduction and utilization: a critical review. *Journal of Materials Chemistry A* **2017**, *5*, 21625–21649.

(2) Nitopi, S.; Bertheussen, E.; Scott, S. B.; Liu, X.; Engstfeld, A. K.; Horch, S.; Seger, B.; Stephens, I. E.; Chan, K.; Hahn, C. et al. Progress and perspectives of electrochemical CO2 reduction on copper in aqueous electrolyte. *Chemical reviews* **2019**, *119*, 7610–7672.

(3) Kuhl, K. P.; Cave, E. R.; Abram, D. N.; Jaramillo, T. F. New insights into the electrochemical reduction of carbon dioxide on metallic copper surfaces. *Energy & Environmental Science* **2012**, *5*, 7050–7059.

(4) Hori, Y.; Takahashi, R.; Yoshinami, Y.; Murata, A. Electrochemical reduction of CO at a copper electrode. *The Journal of Physical Chemistry B* **1997**, *101*, 7075–7081.

(5) Wang, L.; Nitopi, S. A.; Bertheussen, E.; Orazov, M.; Morales-Guio, C. G.; Liu, X.; Higgins, D. C.; Chan, K.; Nørskov, J. K.; Hahn, C. et al. Electrochemical carbon monoxide reduction on polycrystalline copper: Effects of potential, pressure, and pH on selectivity toward multicarbon and oxygenated products. *ACS Catalysis* **2018**, *8*, 7445–7454.

(6) Hori, Y.; Murata, A.; Takahashi, R.; Suzuki, S. Enhanced formation of ethylene and alcohols at ambient temperature and pressure in electrochemical reduction of carbon dioxide at a copper electrode. *Journal of the Chemical Society, Chemical Communications* **1988**, 17–19.

(7) Resasco, J.; Chen, L. D.; Clark, E.; Tsai, C.; Hahn, C.; Jaramillo, T. F.; Chan, K.; Bell, A. T. Promoter effects of alkali metal cations on the electrochemical reduction of carbon dioxide. *Journal of the American Chemical Society* **2017**, *139*, 11277–11287.

(8) Resasco, J.; Lum, Y.; Clark, E.; Zeledon, J. Z.; Bell, A. T. Effects of anion identity and concentration on electrochemical reduction of CO2. *ChemElectroChem* **2018**, *5*, 1064–1072.

(9) Raciti, D.; Mao, M.; Wang, C. Mass transport modelling for the electroreduction of CO2 on Cu nanowires. *Nanotechnology* **2017**, *29*, 044001.

(10) Singh, M. R.; Clark, E. L.; Bell, A. T. Effects of electrolyte, catalyst, and membrane composition and operating conditions on the performance of solar-driven electrochemical reduction of carbon dioxide. *Physical Chemistry Chemical Physics* **2015**, *17*, 18924–18936.

(11) Zheng, Y.; Vasileff, A.; Zhou, X.; Jiao, Y.; Jaroniec, M.; Qiao, S.-Z. Understanding the roadmap for electrochemical reduction of CO2 to multi-carbon oxygenates and

hydrocarbons on copper-based catalysts. *Journal of the American Chemical Society* **2019**, *141*, 7646–7659.

(12) Birdja, Y. Y.; Pérez-Gallent, E.; Figueiredo, M. C.; Göttle, A. J.; Calle-Vallejo, F.; Koper, M. T. Advances and challenges in understanding the electrocatalytic conversion of carbon dioxide to fuels. *Nature Energy* **2019**, *4*, 732–745.

(13) Bagger, A.; Ju, W.; Varela, A. S.; Strasser, P.; Rossmeisl, J. Electrochemical CO2 Reduction: Classifying Cu Facets. *Acs Catalysis* **2019**, *9*, 7894–7899.

(14) Montoya, J. H.; Shi, C.; Chan, K.; Nørskov, J. K. Theoretical insights into a CO dimerization mechanism in CO2 electroreduction. *The journal of physical chemistry letters* **2015**, *6*, 2032–2037.

(15) Chen, L. D.; Urushihara, M.; Chan, K.; Nørskov, J. K. Electric field effects in electrochemical CO2 reduction. *ACS Catalysis* **2016**, *6*, 7133–7139.

(16) Gunathunge, C. M.; Ovalle, V. J.; Li, Y.; Janik, M. J.; Waegele, M. M. Existence of an electrochemically inert CO population on Cu electrodes in alkaline pH. *ACS Catalysis* **2018**, *8*, 7507–7516.

(17) Xiao, H.; Cheng, T.; Goddard III, W. A.; Sundararaman, R. Mechanistic explanation of the pH dependence and onset potentials for hydrocarbon products from electrochemical reduction of CO on Cu (111). *Journal of the American Chemical Society* **2016**, *138*, 483–486.

(18) Gauthier, J. A.; Dickens, C. F.; Ringe, S.; Chan, K. Practical Considerations for Continuum Models Applied to Surface Electrochemistry. *ChemPhysChem* **2019**, *20*, 3074–3080.

(19) Gauthier, J. A.; Dickens, C. F.; Heenen, H. H.; Vijay, S.; Ringe, S.; Chan, K. Uni-

fied approach to implicit and explicit solvent simulations of electrochemical reaction energetics. *Journal of chemical theory and computation* **2019**, *15*, 6895–6906.

(20) Sundararaman, R.; Goddard III, W. A.; Arias, T. A. Grand canonical electronic density-functional theory: Algorithms and applications to electrochemistry. *The Journal of chemical physics* **2017**, *146*, 114104.

(21) Melander, M. M.; Kuisma, M. J.; Christensen, T. E. K.; Honkala, K. Grand-canonical approach to density functional theory of electrocatalytic systems: Thermodynamics of solid-liquid interfaces at constant ion and electrode potentials. *The Journal of chemical physics* **2019**, *150*, 041706.

(22) Hörmann, N. G.; Andreussi, O.; Marzari, N. Grand canonical simulations of electrochemical interfaces in implicit solvation models. *The Journal of chemical physics* **2019**, *150*, 041730.

(23) Peterson, A. A.; Abild-Pedersen, F.; Studt, F.; Rossmeisl, J.; Nørskov, J. K. How copper catalyzes the electroreduction of carbon dioxide into hydrocarbon fuels. *Energy & Environmental Science* **2010**, *3*, 1311–1315.

(24) Kuhl, K. P.; Hatsukade, T.; Cave, E. R.; Abram, D. N.; Kibsgaard, J.; Jaramillo, T. F. Electrocatalytic conversion of carbon dioxide to methane and methanol on transition metal surfaces. *Journal of the American Chemical Society* **2014**, *136*, 14107–14113.

(25) Otani, M.; Sugino, O. First-principles calculations of charged surfaces and interfaces: A plane-wave nonrepeated slab approach. *Physical Review B* **2006**, *73*, 115407.

(26) Nishihara, S.; Otani, M. Hybrid solvation models for bulk, interface, and membrane: Reference interaction site methods coupled with density functional theory. *Physical Review B* **2017**, *96*, 115429.

(27) Haruyama, J.; Ikeshoji, T.; Otani, M. Electrode potential from density functional theory calculations combined with implicit solvation theory. *Physical Review Materials* **2018**, *2*, 095801.

(28) Gauthier, J. A.; Ringe, S.; Dickens, C. F.; Garza, A. J.; Bell, A. T.; Head-Gordon, M.; Nørskov, J. K.; Chan, K. Challenges in Modeling Electrochemical Reaction Energetics with Polarizable Continuum Models. *ACS Catalysis* **2018**, *9*, 920−931.

(29) Feibelman, P. J.; Hammer, B.; Nørskov, J. K.; Wagner, F.; Scheffler, M.; Stumpf, R.; Watwe, R.; Dumesic, J. The CO/Pt (111) Puzzle. *The Journal of Physical Chemistry B* **2001**, *105*, 4018−4025.

(30) Janthon, P.; Vines, F.; Sirijaraensre, J.; Limtrakul, J.; Illas, F. Adding pieces to the CO/Pt (111) puzzle: the role of dispersion. *The Journal of Physical Chemistry C* **2017**, *121*, 3970−3977.

(31) Duanmu, K.; Truhlar, D. G. Validation of density functionals for adsorption energies on transition metal surfaces. *Journal of chemical theory and computation* **2017**, *13*, 835−842.

(32) Wellendorff, J.; Lundgaard, K. T.; Møgelhøj, A.; Petzold, V.; Landis, D. D.; Nørskov, J. K.; Bligaard, T.; Jacobsen, K. W. Density functionals for surface science: Exchange-correlation model development with Bayesian error estimation. *Physical Review B* **2012**, *85*, 235149.

(33) Stroppa, A.; Termentzidis, K.; Paier, J.; Kresse, G.; Hafner, J. CO adsorption on metal surfaces: A hybrid functional study with plane-wave basis set. *Physical Review B* **2007**, *76*, 195440.

(34) Jiang, K.; Sandberg, R. B.; Akey, A. J.; Liu, X.; Bell, D. C.; Nørskov, J. K.; Chan, K.; Wang, H. Metal ion cycling of Cu foil for selective C−C coupling in electrochemical CO 2 reduction. *Nature Catalysis* **2018**, *1*, 111−119.

(35) Li, F.; Thevenon, A.; Rosas-Hernández, A.; Wang, Z.; Li, Y.; Gabardo, C. M.; Oz- den, A.; Dinh, C. T.; Li, J.; Wang, Y. et al. Molecular tuning of CO 2-to-ethylene conversion. *Nature* **2020**, *577*, 509–513.

(36) Dinh, C.-T.; Burdyny, T.; Kibria, M. G.; Seifitokaldani, A.; Gabardo, C. M.; De Ar- quer, F. P. G.; Kiani, A.; Edwards, J. P.; De Luna, P.; Bushuyev, O. S. et al. CO2 electroreduction to ethylene via hydroxide-mediated copper catalysis at an abrupt in- terface. *Science* **2018**, *360*, 783–787.

(37) Liu, X.; Schlexer, P.; Xiao, J.; Ji, Y.; Wang, L.; Sandberg, R. B.; Tang, M.; Brown, K. S.; Peng, H.; Ringe, S. et al. pH effects on the electrochemical reduction of CO (2) towards C 2 products on stepped copper. *Nature communications* **2019**, *10*, 1–10.

(38) Durand, W. J.; Peterson, A. A.; Studt, F.; Abild-Pedersen, F.; Nørskov, J. K. Structure effects on the energetics of the electrochemical reduction of CO2 by copper surfaces. *Surface Science* **2011**, *605*, 1354–1359.

(39) Nørskov, J. K.; Abild-Pedersen, F.; Studt, F.; Bligaard, T. Density functional theory in surface chemistry and catalysis. *Proceedings of the National Academy of Sciences* **2011**, *108*, 937–943.