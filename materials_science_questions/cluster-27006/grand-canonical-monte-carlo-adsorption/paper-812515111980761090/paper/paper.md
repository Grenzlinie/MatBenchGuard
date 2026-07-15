# Adsorption-Based Separation of Near-Azeotropic Mixtures—A Challenging Example for High-Throughput Development of Adsorbents

Dai Tang, Farhad Gharagheizi, and David S. Sholl*

Cite This: J. Phys. Chem. B 2021, 125, 926−936

Read Online

ACCESS | Metrics & More | Article Recommendations | Supporting Information

**ABSTRACT:** Adsorption of gas mixtures is central to adsorption-based gas separations, and the number of adsorbate mixture/adsorbent systems that exist is staggering. Because examples of machine learning (ML) models predicting single-component adsorption of arbitrary molecules in large libraries of crystalline adsorbents have been developed, it is interesting to determine whether these models can accurately predict mixture adsorption. Here, we use molecular simulations to generate mixture adsorption data with a set of 12 near-azeotropic molecules in a diverse set of MOFs. These data provide a challenging example for any method to rapidly predict mixture adsorption in MOFs. We combine a previous ML single-component isotherm model with ideal adsorbed solution theory (IAST) to make predictions that can be compared directly with molecular simulation data for these adsorbed mixtures. This combination of ML and IAST illustrates the scope that is available with these methods, but the accuracy of the resulting predictions is disappointing. By examining the same examples with IAST based on minimal molecular simulation data for single-component isotherms, we show that having an accurate description of adsorption in the dilute loading limit is critical to being able to accurately predict mixture adsorption. This observation points to a useful direction for future work developing robust ML models of adsorption isotherms for diverse collections of molecules and adsorbents.

![](./images/812515111980761090_1.jpg)

## INTRODUCTION

Adsorption-based gas separations can be an energy-efficient approach for this important class of separations.¹ Although estimates of process performance can be made with single-component adsorption data, thorough consideration of materials and processes for adsorption-based separations requires information on mixture adsorption. A key aspect of mixture adsorption is the selectivity of the adsorbent, although other metrics such as capacity and regenerability are also important.² If single-component isotherms in an adsorbent are available for the gas species of interest, then mixture adsorption can be predicted using ideal adsorbed solution theory (IAST) or other mixing theories, although it remains challenging to know a priori whether this approach will be accurate.³⁴

The number of porous materials that are potential adsorbents for gas separations is enormous. This can be illustrated by considering just one class of crystalline materials, metal−organic frameworks (MOFs). Studies considering hundreds or thousands of MOFs as potential adsorbents have been performed for a number of years,⁵⁻¹² including work on applications such as CO₂ separation from CH₄ or N₂,¹³⁻²⁰ noble gas separations,²¹ isomer separations,²²²³ and light hydrocarbon separations.²⁴⁻²⁶ Databases comprised tens of thousands of experimentally derived MOF structures are available.²⁷²⁸ A large majority of these structures have only been reported from a single synthesis experiment,²⁹ and no adsorption data are available in most of these structures. MOFs are just one class of porous materials that can be considered in these applications. In addition to other crystalline materials such as zeolites, a diverse range of disordered porous materials exist.³⁰ The availability of large libraries of MOF structures and data from molecular simulation of single-component adsorption in these structures has made implementation of machine learning (ML)-based adsorption models possible.³¹³² Impressive progress has been made in applying ML to gas adsorption in MOFs with most work to date focusing on hydrogen,³³⁻³⁵ methane,³⁶⁻³⁹ carbon dioxide,⁴⁰⁻⁴³ and a few other molecules.⁴⁴⁻⁴⁷ This list of adsorbing species is very short when

Received: December 1, 2020
Revised: December 23, 2020
Published: January 15, 2021

![](./images/812515111980761090_2.jpg)

© 2021 American Chemical Society
926
https://dx.doi.org/10.1021/acs.jpcb.0c10764
J. Phys. Chem. B 2021, 125, 926−936

**Table 1. Set of Near-Azeotropic Molecules Considered in This Study**ⁱ

<table>
  <tr>
    <td>ID</td>
    <td>Molecule</td>
    <td>ID</td>
    <td>Molecule</td>
  </tr>
  <tr>
    <td>1</td>
    <td>![](./images/812515111980761090_3.jpg)
3-butenal, C₄H₆O
$T_c$=535.1 K, $P_c$=43.47 bar, $\omega$=0.302,
$P_{vp}$ (T=300K)=0.09 bar, $T_b$=355.4 K, $T_f$=210.7 K</td>
    <td>7</td>
    <td>![](./images/812515111980761090_4.jpg)
2,4-dimethylpentane, C₇H₁₆
$T_c$=531.6 K, $P_c$=28.65 bar, $\omega$=0.291,
$P_{vp}$ (T=300K)=0.12 bar, $T_b$=354.5 K, $T_f$=150.7 K</td>
  </tr>
  <tr>
    <td>2</td>
    <td>![](./images/812515111980761090_5.jpg)
Butylamine, C₄H₁₁N
$T_c$=518.3 K, $P_c$=42.5 bar, $\omega$=0.35,
$P_{vp}$ (T=300K)=0.12 bar, $T_b$=356.1 K, $T_f$=225.6 K</td>
    <td>8</td>
    <td>![](./images/812515111980761090_6.jpg)
3,3-dimethylpentane, C₇H₁₆
$T_c$=531.5 K, $P_c$=28.99 bar, $\omega$=0.283,
$P_{vp}$ (T=300K)=0.14 bar, $T_b$=355.1 K, $T_f$=180.8 K</td>
  </tr>
  <tr>
    <td>3</td>
    <td>![](./images/812515111980761090_7.jpg)
Tert-butanol, C₄H₁₀O
$T_c$=515.1 K, $P_c$=40.95 bar, $\omega$=0.584,
$P_{vp}$ (T=300K)=0.08 bar, $T_b$=355.0 K, $T_f$=218 K</td>
    <td>9</td>
    <td>![](./images/812515111980761090_8.jpg)
Methylethylpropylamine, C₆H₁₅N
$T_c$=533 K, $P_c$=30.14 bar, $\omega$=0.38,
$P_{vp}$ (T=300K)=0.1 bar, $T_b$=355.2 K, $T_f$=198.6 K</td>
  </tr>
  <tr>
    <td>4</td>
    <td>![](./images/812515111980761090_9.jpg)
4-methyl-1-hexene, C₇H₁₄
$T_c$=528.2 K, $P_c$=29.39 bar, $\omega$=0.299,
$P_{vp}$ (T=300K)=0.12 bar, $T_b$=355.5 K, $T_f$=154.1 K</td>
    <td>10</td>
    <td>![](./images/812515111980761090_10.jpg)
Dimethylbutylamine, C₆H₁₅N
$T_c$=540 K, $P_c$=29.5 bar, $\omega$=0.359,
$P_{vp}$ (T=300K)=0.1 bar, $T_b$=355.5 K, $T_f$=201.2 K</td>
  </tr>
  <tr>
    <td>5</td>
    <td>![](./images/812515111980761090_11.jpg)
4,4-dimethyl-1-pentene, C₇H₁₄
$T_c$=524.4 K, $P_c$=29.55 bar, $\omega$=0.25,
$P_{vp}$ (T=300K)=0.16 bar, $T_b$=353.3 K, $T_f$=170 K</td>
    <td>11</td>
    <td>![](./images/812515111980761090_12.jpg)
Ethyl tert-butyl ether, C₆H₁₄O
$T_c$=513.5 K, $P_c$=30.46 bar, $\omega$=0.293,
$P_{vp}$ (T=300K)=0.17 bar, $T_b$=351.7 K, $T_f$=186.7 K</td>
  </tr>
  <tr>
    <td>6</td>
    <td>![](./images/812515111980761090_13.jpg)
2,2-dimethylpentane, C₇H₁₆
$T_c$=531.5 K, $P_c$=28.99 bar, $\omega$=0.283,
$P_{vp}$ (T=300K)=0.14 bar, $T_b$=355.5 K, $T_f$=179.3 K</td>
    <td>12</td>
    <td>![](./images/812515111980761090_14.jpg)
Diisopropyl ether, C₆H₁₄O
$T_c$=506 K, $P_c$=29.63 bar, $\omega$=0.305,
$P_{vp}$ (T=300K)=0.21 bar, $T_b$=353.3 K, $T_f$=180 K</td>
  </tr>
</table>

ⁱFor each molecule, $T_c$, $P_c$, and $\omega$ (the acentric factor), $P_{vp}$ at 300 K, and $T_b$ and $T_f$ as predicted using the models of Gharagheizi et al.⁵⁶,⁶⁴⁻⁶⁶ are listed.

compared to the tens of thousands of chemicals that are of interest in the chemical industry.⁴⁸

The potential power of using ML-based methods to make predictions about mixture adsorption can be seen by considering how many mixture isotherms are needed. If we consider a collection of 10,000 adsorbent materials, smaller than the set in the CoRE MOF 2019 database,²⁸ and adsorption of the ~50,000 molecules in one list of industrial chemicals,⁴⁸ a complete description of binary adsorption at a single temperature would require more than $10^{13}$ isotherms. It would be completely infeasible to attempt to describe these isotherms in a comprehensive way using experiments or molecular simulations; only a method that gives "instant" results can be used. In previous work, we developed an ML model that predicts single-component isotherms for arbitrary molecules in arbitrary MOFs.⁴⁹ This model was trained on a collection of ~12,000 single-component isotherms we generated earlier with molecular simulations with a set of 24 molecules in 471 MOFs.⁵⁰ In this paper, we explore whether this ML model of single-component adsorption can be combined with IAST to make useful predictions about mixture adsorption. We find that the predictions of this approach have at best limited accuracy, but understanding the reasons for this outcome points to important areas for future work.

An important element of the work reported below is that we created a sizeable collection of molecular simulation results for binary mixture adsorption in MOFs that define a challenging example of mixture adsorption. Specifically, we select a group of 12 molecules that are near-azeotropic, meaning that the boiling points of all the molecules lie within 5 K of each other. We generated high-quality molecular simulation data for the complete set of binary mixtures that can be formed from this group of molecules and the associated single-component isotherms in a range of MOFs. These data allowed us to carefully test whether IAST can make accurate predictions about these adsorbed mixtures.

**Selection of Binary Mixture Systems and Simulation Methods.** In a previous study, we introduced an ML-based model that predicts single-component adsorption isotherms of arbitrary molecules in MOF materials.⁴⁹ This model is more versatile than applications of ML to adsorption in MOFs that have focused on adsorption of individual species. We previously used the saturation loadings predicted using this model to give an initial prediction about the adsorption selectivity of near-azeotropic binary mixtures of ~24,000 distinct molecules in ~4700 MOFs from the CoRE MOF 2014 database.²⁷ Two observations can be made from these results. First, an enormous number of near-azeotropic pairs of molecules exist. Second, using only the single-component saturation loadings for molecules is unlikely to lead to accurate predictions of adsorption selectivity. A key objective of this paper is to present a specific collection of near-azeotropic

![](./images/812515111980761090_15.jpg)

Figure 1. Test of IAST for 396 near-azeotropic binary mixture systems at 300 K. (a) Comparison between adsorption loadings of each component, $N_{sim+IAST}^{ads}$ and $N_{sim}^{ads}$ and their relative error (inset); (b) comparison of adsorption selectivities, $S_{sim+IAST}^{ads}$ and $S_{sim}^{ads}$ and their relative errors (inset). Results were calculated from IAST and binary mixture GCMC simulations at a total adsorption pressure of $P_{total} = 0.5 \times (P_{A, vp} + P_{B, vp})$. (c) Comparison between adsorption loadings of each component for selected mixtures in two MOFs, QATHOK and VACFUB01. The components in pairs are labeled using their molecular ID. (d) Adsorption selectivities from IAST, $S_{sim+IAST}^{ads}$ (dashed lines) and GCMC simulations $S_{sim}^{ads}$ (dots), as a function of total pressure for the same examples as in (c).

molecules that are readily amenable to molecular simulations in a diverse array of MOFs and to use simulations of this kind to test potential approaches for identifying selective adsorbents in a high-throughput way.

To maintain consistency in our molecular simulations, we restricted our attention to molecules that can be handled by the TraPPE force field (FF). $^{51-55}$ Of the $\sim$24,000 molecules considered in our earlier work, only 496 fall into this group. We refined this list by excluding molecules having different chemical names or conformations but identical structures. Details are given in the Supporting Information. We scanned the molecules' boiling temperatures as predicted by the model of Gharagheizi et al. $^{56}$ to find pairs of near-azeotropic molecules. From these pairs, we picked the set of 12 molecules listed in Table 1 for further study. These 12 molecules all have predicted boiling points between 351.7 and 356.1 K. We suggest that the task of finding suitable adsorbents for selective separations of this set of molecules is a useful challenge for computational (or experimental) methods for finding high-performance adsorbents. Below, we only consider the challenge of finding materials suitable for selective adsorption when adsorbents are in equilibrium with vapors of the molecules at 300 K.

In our molecular simulations, we modeled all 12 molecules using the TraPPE FF, with butylamine, methylethylpropyl- amine, and dimethylbutylamine described by the TraPPE- explicit hydrogen (EH) FF$^{55}$ and all other molecules modeled by the TraPPE-united atom (UA) FF. $^{51-54,57-59}$ All the molecules were modeled as having flexible internal degrees of freedom. The functional form of the potentials for dihedral interactions is different for various molecules described by TraPPE-UA/EH; details are given in the Supporting Information. Point charges were assigned for O, N, and neighboring atoms in each molecule as specified by the TraPPE FF. $^{53-55}$ FF parameters, pseudo-atom parameters, and molecular models as RASPA input files are provided in the Supporting Information. Adsorbate−adsorbate Lennard-Jones

interactions and Coulomb interactions were computed with a cutoff of 14 Å and Ewald summation, respectively.

In our molecular simulations of adsorption in MOFs, FF parameters for MOF atoms were defined by the universal FF,⁶⁰ which has been widely used in high-throughput studies of MOFs.¹⁰,¹⁴,¹⁵,¹⁸,²⁷,²⁸,⁵⁰,⁶¹ Detailed information for each simulated MOF is given in the *Supporting Information*. During adsorption simulations, all MOFs were assumed to be rigid and only nonbonded adsorbate–MOF interactions were considered. Adsorbate–MOF nonbonded interactions were defined using Lorentz–Berthelot combining rules and a tail correction with a cutoff of 14 Å, plus Coulomb interactions between point charges if the molecule has charges. We performed simulations for both single-component adsorption and binary mixture adsorption by grand canonical Monte Carlo (GCMC)⁶² using RASPA 2.0.⁶³ Simulations were performed using 10⁵ Monte Carlo cycles for equilibrium and 10⁶ Monte Carlo cycles for data collection, with each Monte Carlo cycle including translation, rotation, reinsertion, and (for mixtures) identity swap moves with equal probability. Preliminary tests indicated that these choices gave well-converged results.

As potential adsorbents, we considered 1031 materials from the CoRE MOF 2019 database²⁸ which in that library are reported as energy-minimized structures with point charges assigned to each framework atom. We defined two constraints to narrow down the number of MOFs to consider further. First, we calculated the van der Waals diameters (DvdWs) of each adsorbing molecule using the model of Zhao et al.⁶⁷ and compared them with the largest cavity diameters (LCDs) of the MOFs reported in the CoRE MOF 2019 database.²⁸ We excluded MOFs whose LCD was smaller than the DvdW of any of the molecules from further analysis. Materials that do not satisfy this condition are unlikely to allow any meaningful amount of adsorption for the molecules of interest. Second, we evaluated the inclusion of the molecule/MOF systems in the applicability domain (AD) of the ML model from our earlier work. The AD approach provides a prediction of when the results of the ML model are expected to be accurate.⁴⁹ For each MOF considered, we predicted the single-component adsorption isotherm at 300 K for each of the 12 molecules listed above with our ML model and the AD model. Only adsorbents for which the AD indicated reliable results over a significant range of vapor pressures for all 12 molecules were considered further. This procedure gave a collection of 98 MOFs that is listed in the *Supporting Information*.

**Applicability of IAST for Binary Mixture Adsorption of Near-Azeotropic Molecules.** To give some baseline information on adsorption of the 12 near-azeotropic molecules listed above, we performed molecular simulations for 6 MOFs that were picked to give variation in their metal centers, linkers, and pore shapes. We first simulated single-component isotherms at 300 K for each of the 12 molecules in these 6 MOFs. We predicted the vapor pressure, $P_{\text{vp}}$, of each molecule as described in *Table 1* and predicted isotherms for pressures up to $50 \times P_{\text{vp}}$. The lowest pressure for each isotherm was chosen such that the loading was $<10^{-4}$ times the loading obtained at the highest pressure. This protocol ensures that we have data from the Henry's law region of the isotherm to the isotherm's saturation loading. We also performed GCMC simulations in each MOF of binary mixture adsorption for each of the 66 binary mixtures possible with the set of 12 molecules. For these simulations, the bulk phase was assumed to be equimolar at a total pressure of $P_{\text{total}} = 0.5 \times (P_{\text{A,vp}} + P_{\text{B,vp}})$, where $P_{\text{A,vp}}$ and $P_{\text{B,vp}}$ are the predicted vapor pressure of each component. We also performed equimolar binary mixture GCMC simulations as a function of total pressure for a smaller number of examples.

The results from our molecular simulations allow us to test whether IAST³,⁴ makes reliable predictions of mixture adsorption for these near-azeotropic molecules. We made predictions with IAST based on our detailed single-component isotherms using the pyIAST package.⁶⁸ These calculations predict the adsorption loadings of each component in the adsorbed phase of the binary mixture, $N_{\text{A}}^{\text{ads}}$ and $N_{\text{B}}^{\text{ads}}$, and the associated adsorption selectivity $S_{\text{A/B}}^{\text{ads}}$, defined using the bulk phase mole fractions, $y_{\text{A}}$ and $y_{\text{B}}$, as⁶⁹

$$
S_{\text{A/B}}^{\text{ads}} = \frac{N_{\text{A}}^{\text{ads}}/N_{\text{B}}^{\text{ads}}}{y_{\text{A}}/y_{\text{B}}}
\tag{1}
$$

To test the accuracy of IAST for near-azeotropic binary mixtures, we first compared the adsorption loadings of each component in all 396 test systems at 300 K and different pressures. *Figure 1a* shows the simulated adsorption loadings at relatively high loadings and the equivalent predictions from IAST. We defined the relative error as the absolute difference between the simulated and IAST results divided by the value from direct binary mixture simulations. *Figure 1a* shows that 44% of the examples we considered have relative errors <0.1 and 88% have relative errors <0.5. Only 1.2% of the cases have a relative error >1.0, including several examples in MOF VACFUB01: 3-butenal in 3-butenal/2,4-dimethylpentane with a relative error of 1.1, *tert*-butanol in *tert*-butanol/4,4-dimethyl-1-pentene with a relative error of 9.5, and *tert*-butanol in *tert*-butanol/3,3-dimethylpentane with a relative error of 12.2.

The adsorption selectivity of the test systems is shown in *Figure 1b*. The systematic errors in the predictions of each component's loading from IAST do not typically cancel, so the relative errors in the IAST predictions of selectivity are larger than for the predictions of component-wise uptake. 17% of the adsorbing pairs have relative error for selectivity <0.1 and 69% have a relative error <0.5. 20% of the pairs have a relative error for selectivity >1.0, including dimethylbutylamine/ethyl *tert*-butyl ether in BEPMIU with a relative error of 2.4, 4-methyl-1-hexene/3,3-dimethylpentane in FUNCAT with a relative error of 1.8, and butylamine/4,4-dimethyl-1-pentene in QATHOK with a relative error of 2.0. Interestingly, IAST appears to be less accurate on average for examples with higher selectivities; the mean relative error in selectivity for examples where $S_{\text{sim}}^{\text{ads}} \leq$ 5 is 0.92 while for the examples with $S_{\text{sim}}^{\text{ads}} > 5$, the mean relative error is 1.61.

We picked four near-azeotropic binary mixtures at random to test IAST as a function of total pressure, with six data points uniformly spaced in range $[P_{\text{total,low}}, P_{\text{total}}]$, where $P_{\text{total,low}} = 0.1 \times \min(P_{\text{A,vp}}, P_{\text{B,vp}})$. Specifically, we simulated binary adsorption of equimolar bulk mixtures for 3-butenal (ID = 1)/tert-butanol (ID = 3), 3-butenal (ID = 1)/4-methyl-1-hexene (ID = 4), 4-methyl-1-hexene (ID = 4)/2,2-dimethylpentane (ID = 6), and 4-methyl-1-hexene (ID = 4)/2,4-dimethylpentane (ID = 7), in two MOFs, QATHOK and VACFUB01. *Figure 1c* shows that the relative error for adsorption loadings of both components is all <0.16, except for 3-butenal in 3-butenal/tert-butanol in QATHOK (average relative error of 0.59) and 3-butenal in 3-butenal/4-methyl-1-hexene in VACFUB01 (average relative error of 1.42). The adsorption selectivities (*Figure 1d*) vary weakly with the overall pressure, an observation that supports

![](./images/812515111980761090_16.jpg)

Figure 2. Array plots of scaled adsorption selectivities from applying IAST to single-component ML isotherms of all 66 near-azeotropic pairs. (a) The largest and smallest scaled selectivities among the MOFs considered, $s_{AB,max}$ and $s_{AB,min}$, are shown in the upper right triangle and lower left triangle, respectively. The order of molecule IDs is consistent with that listed in Table 1. (b) Rankings of MOFs BEPMIU (upper right) and HIHGOW (lower left) in terms of scaled selectivity for each near-azeotropic pair, where the highest ranking is 1 and the lowest ranking is 98.

the idea of examining a larger number of examples based on just one or two bulk pressures.

As suggested by its name, IAST assumes that the adsorbed phase forms an ideal mixture in which all adsorbates access the same volumes in the adsorbent. $^{4}$ Deviations can occur if target systems disobey the basic assumptions held by IAST. $^{3,4,70,71}$ Inaccuracies in IAST predictions can also occur because of imprecision or extrapolation in defining the single-component data that IAST relies on. $^{72}$ Because the largest deviations associated with IAST in Figure 1b are associated with materials that are predicted to be highly selective, it is of interest to understand the source of these deviations. IAST overestimates selectivity for the majority of systems having a relative error for selectivity >1.0, which includes 20% of all pairs in our data. Among those systems, more than 72% (54%) of them have high selectivity, that is, $S_{sim+IAST}^{ads} \geq 5(10)$. A key factor that leads to the tendency for inaccurate IAST predictions on those systems is that the bulk phase mixtures are nonideal mixtures. For example, we found inaccurate IAST predictions for butylamine (ID = 2)/4,4-dimethyl-1-pentene (ID = 5), dimethylbutylamine (ID = 10)/diisopropyl ether (ID = 12), and tert-butanol (ID = 3)/4-dimethyl-1-pentene (ID = 5) in at least 3 MOFs investigated. Although our data set includes a small number of examples where IAST has poor accuracy, the success of IAST for the majority of the examples we considered indicates that using IAST as a basis for screening a large number of materials for separations of near-azeotropic molecules seems reasonable, especially if such a screening exercise is then coupled with more detailed examination of promising systems.

Exploring Promising MOFs for Near-Azeotropic Binary Mixture Separation. The results mentioned above indicate that applying IAST to the adsorption of the near-azeotropic molecules in Table 1 is sufficiently accurate that IAST-based predictions should be useful in the initial stages of high-throughput screening of adsorbents for these molecules. This motivated us to use predictions from our previous ML-based adsorption model in combination with IAST to consider separations of this challenging set of molecules in a high-throughput manner.

The 12 molecules and 98 MOFs we considered define 6468 near-azeotropic binary mixture systems. We predicted the single-component adsorption isotherms for each example using the ML model discussed above (more details are provided in the Supporting Information). The data were then used as inputs in IAST calculations to predict the adsorption selectivity of the equimolar bulk mixture of each system at 300 K and $P_{total} = 0.5 \times (P_{A,vp} + P_{B,vp})$. We used pyIAST with linear interpolation between single-component isotherm points predicted using our ML model. $^{68}$ pyIAST will report an "extrapolation warning" message if the spreading pressure of at least one component as predicted by IAST is beyond the single-component isotherm data. We initially predicted the single-component isotherms up to the vapor pressures of molecules at 300 K. While performing the IAST calculations, pyIAST frequently extrapolated to define single isotherm data. To avoid this approximation, we reapplied our ML model to extend the single-component isotherms up to a much higher pressure than the vapor pressure of the molecules. This led to extrapolation-free IAST calculations. When characterizing a single-component isotherm, widely spaced data points can lead to inaccurate interpolation. Using an ML model, we are able to generate closely spaced points with little computational cost, so each single-component isotherm included at least 1000 data points. These calculations for adsorbed mixtures require negligible computational time and resources, in strong contrast to similar results based on molecular simulations.

To clarify the separation effect of 98 MOFs on each molecular pair, we defined the scaled adsorption selectivities by $s_{A/B} = S_{A/B}^{-1}$ if $S_{A/B} > 1$, otherwise $s_{A/B} = S_{A/B}$. The range of scaled adsorption selectivities is $s_{A/B} \in (0,1]$, where $s_{A/B} \to 1$ means that the pair is poorly separated and $s_{A/B} \to 0$ means that the pair is strongly separated. Below, we discuss this scaled selectivity unless specified otherwise. Figure 2a shows the largest and smallest predicted selectivities among the 98 MOFs for all 66 molecular pairs. The results predict that many but not all of the molecular pairs can be strongly separated by one or more of the 98 MOFs. Some pairs of molecules have similar predicted selectivities in every MOF considered. Two examples of this type are 4-methyl-1-hexene (ID = 4)/3,3-dimethylpentane (ID = 8), with $s_{AB,max} = 0.95$ and $s_{AB,min} = 0.93$, and 2,2-

![](./images/812515111980761090_17.jpg)

Figure 3. Test of the ML + IAST method for 396 near-azeotropic binary mixture systems at 300 K. (a) Comparison of adsorption loadings of each component, $N_{\text{ML+IAST}}^{\text{ads}}$ and $N_{\text{sim}}^{\text{ads}}$; (b) comparison of adsorption selectivities of each binary mixture, $S_{\text{ML+IAST}}^{\text{ads}}$ and $S_{\text{sim}}^{\text{ads}}$. Results were calculated from IAST and binary mixture GCMC simulations at a total adsorption pressure $P_{\text{total}} = 0.5 \times (P_{\text{A,vp}} + P_{\text{B,vp}})$.

![](./images/812515111980761090_18.jpg)

Figure 4. Tests of IAST for six representative near-azeotropic binary mixture separations at 300 K. Each panel shows the single-component isotherms of each component as generated from GCMC simulations (symbols) and our ML model, with solid lines for AD = 1 and dashed lines for AD = 0. $P_{\text{vp}}$ is the vapor pressure of the adsorbate estimated at 300 K. Adsorbing species are identified with the molecular IDs from Table 1. $S_{\text{sim}}^{\text{ads}}$, $S_{\text{sim+IAST}}^{\text{ads}}$, and $S_{\text{ML+IAST}}^{\text{ads}}$ are the adsorption selectivities calculated from binary mixture GCMC simulations, IAST using single-component isotherms fitted to GCMC simulation data, and our ML + IAST model, respectively, at 300 K and a total pressure $P_{\text{total}} = 0.5 \times (P_{\text{A,vp}} + P_{\text{B,vp}})$.

dimethylpentane (ID = 6)/2,4-dimethylpentane (ID = 7), with $s_{\text{AB,max}} = 0.99$ and $s_{\text{AB,min}} = 0.91$. It is not surprising that pairs of molecules that are less chemically similar are predicted to be easier to separate and that these pairs show more variation among MOFs. Two examples are butylamine (ID = 2)/tert-butanol (ID = 3), with $s_{\text{AB,max}} = 0.61$ and $s_{\text{AB,min}} = 0.002$, and methylethylpropylamine (ID = 9)/ethyl tert-butyl ether (ID = 11), with $s_{\text{AB,max}} = 0.62$ and $s_{\text{AB,min}} = 0.02$.

It is interesting to use the data from Figure 2 to ask if there are individual MOFs that are predicted to be particularly versatile for separating the mixtures from our test set of molecules. We ranked the MOFs for each molecular pair separately in terms of their scaled selectivity, with the MOFs whose scaled selectivity closest to zero ranked most highly. Two MOFs, BEPMIU and HIHGOW, were chosen as examples to illustrate how different the MOFs' selective separation could be for near-azeotropic pairs. It can be seen in Figure 2b that using our ML isotherms in conjunction with IAST predicts that BEPMIU is selective for many more mixtures (i.e., its ranking is much lower for most pairs) than HIHGOW.

Figure 2 gives a glimpse of how a combination of ML isotherms and IAST might be used to rapidly consider large numbers of adsorbed mixtures, but this approach is only useful

![](./images/812515111980761090_19.jpg)

Figure 5. Prediction of separation for 396 near-azeotropic binary mixture systems at 300 K under the assumption of the Langmuir model. (a) Distribution of relative error of loadings in single-component isotherms, between the Langmuir model and simulation. The top/bottom panel is the distribution results of full adsorption isotherms and that when $P/P_{vp} \geq 10^{-2}$ (pink) and $P/P_{vp} < 10^{-2}$ (green). (b) Comparison of adsorption loadings of each component, $N_{Langmuir+IAST}^{ads}$ and $N_{sim}^{ads}$; (c) comparison of adsorption selectivities of each binary mixture, $S_{Langmuir+IAST}^{ads}$ and $S_{sim}^{ads}$. The upper/lower boundary of error bars indicates the largest/smallest $S_{Langmuir+IAST}^{ads}$ when considering numerical uncertainty of simulated Henry's law constant and saturation loadings. The purple dots represent systems in which IAST is not applicable identified in the previous section. (d) Distribution of relative error of adsorption loadings (top panel) and selectivities (bottom panel) by the ML + IAST method (gray) and Langmuir + IAST method (orange).

if this ML + IAST approach is sufficiently accurate. Figure 3 directly compares the predictions of the ML + IAST method with the mixture GCMC simulations we discussed above. Unfortunately, the accuracy of the ML + IAST predictions is poor; only about 15% of the adsorption loadings have a relative error <0.3 and 13% have a relative error >1.0 (Figure 3a). For the adsorption selectivities, the ML + IAST prediction method has a relative error <0.3 for only 11% of pairs and 64% of the pairs have a relative error >1.0 (Figure 3b). The inaccuracy of the ML + IAST method is particularly acute for the examples that it predicts to have the highest selectivities; our ML + IAST calculations predict a selectivity >10 or smaller than 0.1 for 42% of adsorbed pairs, but our molecular simulation data identify only 11% of the examples as having this property. Among the 23 (18) examples found in our simulations to have selectivity <0.1 (>10), only 0 (10) are predicted by our ML + IAST calculations to lie in this category of highly selective cases.

To better understand the reasons for the shortcomings of our ML + IAST model, six representative systems were chosen for more detailed investigation. Figure 4 shows the single- component isotherms from GCMC simulations and our ML model of each system and associated selectivities calculated with various methods. The example in Figure 4a has comparable selectivities for $S_{sim}^{ads}$ and $S_{ML+IAST}^{ads}$, indicating that IAST is appropriate for this system. It also gives an example in which the ML + IAST method makes a relatively accurate prediction for adsorption selectivity. For the examples in Figure 4b−f, IAST is also seen to be applicable since $S_{sim}^{ads}$ and $S_{ML+IAST}^{ads}$ are similar in each case. Large differences exist, however, between the selectivity from the ML + IAST approach, $S_{ML+IAST}^{ads}$, and the mixture GCMC data. It is notable in each example that the ML model does not make accurate predictions about the single-component isotherm in the regime of moderate and low loadings. We emphasize that this is something that is quantified directly in our ML model by its

use of the AD. The AD is a binary variable that predicts whether the pointwise isotherm from our ML model is expected to be accurate or not.⁴⁹ The regions where the ML isotherm is expected on this basis to be inaccurate are shown as dashed lines in Figure 4. In each case, the ML isotherm is expected to become inaccurate at low loadings, and our GCMC simulations agree with this expectation. This situation would not be problematic if we were only interested in single- component loadings at high loadings. Unfortunately, applying IAST requires computing integrals of the single-component isotherms over loadings that extend to zero,³⁴⁶⁸ so using isotherms that are inaccurate in the low pressure limit creates difficulties for using IAST at any bulk pressure and composition.

To explore the role of having accurate single-component data at low loadings on making reliable IAST predictions, we tested an alternative to our ML-based isotherms. In earlier work, we showed that reasonable predictions for single- component adsorption isotherms for a range of molecules in a wide range of MOFs could be made using a simple Langmuir form.⁵⁰ The Langmuir isotherm is fully specified once the saturation loading and Henry's constant are known. Here, we obtained Langmuir isotherms by obtaining these two parameters directly from molecular simulations. Specifically, we obtained Henry's constants using the Widom insertion method and set the saturation loadings equal to the simulated loadings from GCMC at 10 times the adsorbate vapor pressure. These calculations were performed for the 12 molecules in 6 MOFs that were considered above in Figure 1. Figure 5a shows the average absolute relative error for each example. Although by construction this Langmuir fit correctly describes each isotherm in the limit of zero loading and saturation loading, the results at intermediate loadings clearly show that the actual isotherms are not completely Langmuir in form. The Langmuir model predicts the single-component isotherm of only 68% of systems with an average absolute relative error ≤1. In all of the examples we chose the adsorption loading rise rapidly at low relative pressures. This can be seen in Figure 5a where the average relative error for data points with $P/P_{vp} > 10^{-2}$ is far smaller than the analogous result for lower relative pressures. Another way to say this is that most of the low relative pressure points used in the comparison in Figure 5a lie outside the Henry's regime.

To make IAST predictions with the fitted Langmuir isotherms, we generated 2000 data points for each isotherm uniformly spaced in log pressure in the range $[10^{-10}, 50] \times P/ P_{vp}$ for each molecule−MOF system. This range was chosen to ensure the data included both the Henry's regime and loadings reaching saturation loading. These data were used in pyIAST in the same way as the calculations described above for our ML-based isotherms. Figure 5b compares the Langmuir + IAST predictions with binary GCMC data for all state points at which we have GCMC data. The contrast with Figure 3a is striking; the predictions of IAST based on our Langmuir isotherms are considerably more accurate than the results from our ML-based isotherms.

It is useful to estimate how much of the deviation between our Langmuir + IAST results and direct binary GCMC simulations is due to uncertainties in fitting single-component isotherms. For each single-component isotherm, numerical uncertainties for the Henry's constant and saturation loading were obtained by block averaging our molecular simulation data. For each molecule−MOF system, adding/subtracting the relevant uncertainty to the Henry's constant and saturation loading gave 4 possible isotherms. For each binary mixture, this approach gave 17 combinations of single-component iso- therms, including the one using actual values of the Henry's constant and saturation loading. Uncertainties in IAST predictions were estimated by separately applying pyIAST to each of these 17 examples. Figure 5c compares the selectivities from the Langmuir + IAST method (including uncertainties) and direct binary mixture simulations. We can identify the examples for which the Langmuir + IAST method makes reasonable predictions as those satisfying $S_{Langmuir+IAST,min}^{ads} \leq S_{sim}^{ads} \leq S_{Langmuir+IAST,max}^{ads}$. 54% of the examples in Figure 5c satisfy this criterion.

Figure 5d compares the relative errors of IAST predictions made with the Langmuir model and the ML-based isotherms. The Langmuir + IAST method predicts the loadings of 75% of state points with a relative error ≤0.5, while only 41% of the ML-based predictions have the same accuracy. For selectivities, the Langmuir + IAST (ML-based) method gave a relative error ≤0.5 for 47% (19%) of state points. 53% of the state points have relative errors for selectivity >1.0 when using the Langmuir + IAST method, where the much higher relative error cases (purple dots in Figure 5c) point to the same ~20% of pairs for which IAST is not applicable as we observed in Figure 1b.

The improved accuracy of the Langmuir + IAST approach relative to our ML isotherms comes at significantly increased computational cost since molecular simulations must be performed at dilute and saturated loadings for each adsorbate−adsorbent pair of interest. We showed above that our ML isotherms have limited accuracy in the Henry's regime. Conceptually, it is not surprising that including an accurate description of the Henry's regime improves predictions of binary mixtures; in the dilute limit, the selectivity of adsorbed mixtures is given without approximation by the ratio(s) of Henry's constants⁴ and selectivity often varies only weakly with loading (see Figure 1d). These observations suggest that future efforts to use ML approaches to predict mixture adsorption should place special focus on accurately predicting single- component Henry's constants. Using isotherm models that capture the deviations from simple functional forms such as the Langmuir isotherm at intermediate loadings evident in Figure 5a will also improve the prediction of mixture adsorption, but our results hint that correctly describing the Henry's regime is likely to have a larger impact.

## CONCLUSIONS

We have explored several aspects of the challenging task of making accurate predictions about adsorption of diverse molecular mixtures in large numbers of crystalline adsorbents. A key outcome from our work is molecular simulation data for mixtures of 66 pairs of near-azeotropic molecules in 6 MOFs. This information illustrates many aspects of the general problem of predicting mixture adsorption and we suggest that it will be a useful test set for future efforts to tackle this problem. Our analysis showed that many but not all of the binary mixture/adsorbent pairs could be described with reasonable accuracy using IAST.

Generating molecular simulation data such as the test set we have reported is time-consuming. We illustrated the potential of methods based on ML to rapidly make predictions about mixture adsorption by combining an ML model for single- component adsorption of arbitrary adsorbates from our earlier

work⁴⁹ with IAST. This approach was used to make predictions about 66 binary mixtures of near-azeotropic molecules in 98 MOFs, and it readily could have been extended to far larger collections of adsorbing molecules and MOFs. We found by comparison with molecular simulation data, however, that this ML + IAST model made predictions of low quality.

An unusual feature of our earlier ML model is that in addition to predicting single-component isotherms it also predicted the expected accuracy of the loading at each state point using an AD approach.⁴⁹ The AD approach correctly predicted that in each example we studied the single-component isotherms from our ML model that were inaccurate in the low loading regime. This means that the ML approach could not be expected to give accurate adsorption selectivities in the dilute regime, where these selectivities are exactly the ratio of the single-component Henry's constants. Just as importantly, this situation means that IAST, which involves integrals over a range of loadings including the low loading regime, is unlikely to make successful predictions based on these approximate single-component isotherms.

To demonstrate the importance of including accurate low loading data in IAST calculations, we tested an alternative approach in which molecular simulations were used to directly obtain the single-component Henry's constants and saturation loadings for each adsorbate/adsorbent pair of interest. Using these simulation data, the complete single-component isotherm could readily be approximated as a Langmuir isotherm and predictions of mixture adsorption were made by applying IAST to these Langmuir isotherms. Even though comparisons with single-component GCMC data showed that many examples deviated considerably from the Langmuir form at intermediate loadings, this Langmuir + IAST approach gave considerably more reliable predictions about adsorption of binary mixtures than our ML + IAST method. This approach cannot be easily extended to the task of describing the enormous diversity of mixtures that can be formed by hundreds or thousands of molecules because a limited number of molecular simulations must be performed for each adsorbent in each adsorbate of interest.

Our results point to several fruitful directions for future work. In particular, it is clear that if a computationally efficient model for single-component adsorption of diverse molecules in a set of materials is available that makes accurate predictions for the low loading regime and other conditions, then such a model can be combined with IAST in a simple way to make useful predictions about mixture adsorption. No ML model with these properties is currently available, but it seems plausible that such models can be developed. We strongly advocate for the use of an AD or similar approach in developing ML models of this kind so that an assessment of expected prediction accuracy is possible even in the absence of detailed molecular simulation data. Our molecular simulation data and the specific test set of near-azeotropic molecules we have analyzed also include some examples for which IAST is fundamentally inaccurate, so this data set will be useful in efforts to test or develop mixing theories that go beyond IAST. The molecular simulations that underpin the ML model we used here, and most ML models for predicting adsorption in porous materials, rely on a series of assumptions such as their choice of FFs and use of rigid structures. In addition to expanding the scope of these simulations using ML methods, efforts that systematically test these assumptions and point to areas where improvements in simulation methods are needed remain important.⁷³⁻⁷⁸

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at
https://pubs.acs.org/doi/10.1021/acs.jpcb.0c10764.

Conversion test of binary mixture GCMC simulations using RASPA and single-component isotherms fitted by interpolation using pyIAST (PDF)

Lists of molecules that could be described by TraPPE FF, list of 12 molecules and their predicted properties, list of 98 MOFs, single-component isotherms predicted by ML model/GCMC simulations/Langmuir model, adsorption loadings and selectivities predicted by binary mixture GCMC simulations/ML + IAST method/ Langmuir + IAST method, and simulated Henry's law constants for 12 molecules in 6 MOFs that are considered in simulations (ZIP)

## AUTHOR INFORMATION

### Corresponding Author
David S. Sholl − School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332-0100, United States; orcid.org/0000-0002-2771-9168; Email: david.sholl@chbe.gatech.edu

### Authors
Dai Tang − School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332-0100, United States

Farhad Gharagheizi − School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332-0100, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcb.0c10764

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
F.G. and D.S.S. received funding from the U.S. Department of Energy's Office of Energy Efficiency and Renewable Energy (EERE) under the Advanced Manufacturing Office Award Number DE-EE0007888. D.T. and D.S.S. received funding from the Nanoporous Materials Genome Center, funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, under Award #DEFG02-17ER16362.

## REFERENCES
(1) Sholl, D. S.; Lively, R. P. Seven Chemical Separations to Change the World. *Nature* **2016**, 532, 435−437.
(2) Park, J.; Rubiera Landa, H. O.; Kawajiri, Y.; Realff, M. J.; Lively, R. P.; Sholl, D. S. How Well Do Approximate Models of Adsorption-Based CO₂ Capture Processes Predict Results of Detailed Process Models? *Ind. Eng. Chem. Res.* **2020**, 59, 7097−7108.
(3) Myers, A. L.; Prausnitz, J. M. Thermodynamics of Mixed-Gas Adsorption. *AIChE J.* **1965**, 11, 121−127.
(4) Walton, K. S.; Sholl, D. S. Predicting Multicomponent Adsorption: 50 Years of the Ideal Adsorbed Solution Theory. *AIChE J.* **2015**, 61, 2757−2762.

(5) Chen, B.; Liang, C.; Yang, J.; Contreras, D. S.; Clancy, Y. L.; Lobkovsky, E. B.; Yaghi, O. M.; Dai, S. A microporous metal-organic framework for gas-chromatographic separation of alkanes. *Angew. Chem., Int. Ed.* **2006**, 45, 1390−1393.

(6) Li, H.; Eddaoudi, M.; Groy, T. L.; Yaghi, O. M. Establishing microporosity in open metal-organic frameworks: Gas sorption isotherms for Zn(BDC) (BDC = 1,4-benzenedicarboxylate). *J. Am. Chem. Soc.* **1998**, 120, 8571−8572.

(7) Chui, S. S.; Lo, S. M. F.; Charmant, J. P. H.; Orpen, A. G.; Willians, I. D. A Chemically Functionalizable Nanoporous Material [Cu₃(TMA)₂(H₂O)₃]ₙ. *Science* **1999**, 283, 1148−1150.

(8) Challa, S. R.; Sholl, D. S.; Johnson, J. K. Adsorption and Separation of Hydrogen Isotopes in Carbon Nanotubes: Multi- component Grand Canonical Monte Carlo Simulations. *J. Chem. Phys.* **2002**, 116, 814−824.

(9) Watanabe, T.; Sholl, D. S. Accelerating applications of metal- organic frameworks for gas adsorption and separation by computa- tional screening of materials. *Langmuir* **2012**, 28, 14114−14128.

(10) Yazaydin, A. O.; et al. Screening of Metal-Organic Frameworks for Carbon Dioxide Capture from Flue Gas Using a Combined Experimental and Modeling Approach. *J. Am. Chem. Soc.* **2009**, 131, 18198−18199.

(11) Wilmer, C. E.; Leaf, M.; Lee, C. Y.; Farha, O. K.; Hauser, B. G.; Hupp, J. T.; Snurr, R. Q. Large-scale screening of hypothetical metal- organic frameworks. *Nat. Chem.* **2012**, 4, 83−89.

(12) Bernales, V.; League, A. B.; Li, Z.; Schweitzer, N. M.; Peters, A. W.; Carlson, R. K.; Hupp, J. T.; Cramer, C. J.; Farha, O. K.; Gagliardi, L. Computationally guided discovery of a catalytic cobalt-decorated metal−organic framework for ethylene dimerization. *J. Phys. Chem. C* **2016**, 120, 23576−23583.

(13) Chung, Y. G.; et al. In silico discovery of metal-organic frameworks for precombustion CO₂ capture using a genetic algorithm. *Sci. Adv.* **2016**, 2, No. e1600909.

(14) Park, J.; Lively, R. P.; Sholl, D. S. Establishing upper bounds on CO₂ swing capacity in sub-ambient pressure swing adsorption via molecular simulation of metal−organic frameworks. *J. Mater. Chem. A* **2017**, 5, 12258−12265.

(15) Qiao, Z.; Zhang, K.; Jiang, J. In silico screening of 4764 computation-ready, experimental metal−organic frameworks for CO₂ separation. *J. Mater. Chem. A* **2016**, 4, 2105−2114.

(16) Watanabe, T.; Keskin, S.; Nair, S.; Sholl, D. S. Computational identification of a metal organic framework for high selectivity membrane-based CO₂/CH₄ separations: Cu(hfpbb)(H₂hfpbb)₀.₅. *Phys. Chem. Chem. Phys.* **2009**, 11, 11389−11394.

(17) Keskin, S.; van Heest, T. M.; Sholl, D. S. Can metal-organic framework materials play a useful role in large-scale carbon dioxide separations? *ChemSusChem* **2010**, 3, 879−891.

(18) Haldoupis, E.; Nair, S.; Sholl, D. S. Finding MOFs for highly selective CO₂/N₂ adsorption using materials screening based on efficient assignment of atomic point charges. *J. Am. Chem. Soc.* **2012**, 134, 4313−4323.

(19) Ding, M.; Flaig, R. W.; Jiang, H.-L.; Yaghi, O. M. Carbon capture and conversion using metal-organic frameworks and MOF- based materials. *Chem. Soc. Rev.* **2019**, 48, 2783−2828.

(20) Babarao, R.; Jiang, J. Molecular screening of metal-organic frameworks for CO₂ storage. *Langmuir* **2008**, 24, 6270−6278.

(21) Simon, C. M.; Mercado, R.; Schnell, S. K.; Smit, B.; Haranczyk, M. What Are the Best Materials To Separate a Xenon/Krypton Mixture? *Chem. Mater.* **2015**, 27, 4459−4475.

(22) Gee, J. A.; Zhang, K.; Bhattacharyya, S.; Bentley, J.; Rungta, M.; Abichandani, J. S.; Sholl, D. S.; Nair, S. Computational Identification and Experimental Evaluation of Metal−Organic Frameworks for Xylene Enrichment. *J. Phys. Chem. C* **2016**, 120, 12075−12082.

(23) Chung, Y. G.; et al. Computational Screening of Nanoporous Materials for Hexane and Heptane Isomer Separation. *Chem. Mater.* **2017**, 29, 6315−6328.

(24) Altintas, C.; Keskin, S. Computational screening of MOFs for C₂H₆/C₂H₄ and C₂H₆/CH₄ separations. *Chem. Eng. Sci.* **2016**, 139, 49−60.

(25) Kulkarni, A. R.; Sholl, D. S. Screening of copper open metal site MOFs for olefin/paraffin separations using DFT-derived force fields. *J. Phys. Chem. C* **2016**, 120, 23044−23054.

(26) Bae, Y.-S.; Lee, C. Y.; Kim, K. C.; Farha, O. K.; Nickias, P.; Hupp, J. T.; Nguyen, S. T.; Snurr, R. Q. High propene/propane selectivity in isostructural metal-organic frameworks with high densities of open metal sites. *Angew. Chem., Int. Ed. Engl.* **2012**, 51, 1857−1860.

(27) Chung, Y. G.; Camp, J.; Haranczyk, M.; Sikora, B. J.; Bury, W.; Krungleviciute, V.; Yildirim, T.; Farha, O. K.; Sholl, D. S.; Snurr, R. Q. Computation-ready, experimental metal−organic frameworks: a tool to enable high-throughput screening of nanoporous crystals. *Chem. Mater.* **2014**, 26, 6185−6192.

(28) Chung, Y. G.; et al. Advances, Updates, and Analytics for the Computation-Ready, Experimental Metal-Organic Framework Data- base: CoRE MOF 2019. *J. Chem. Eng. Data* **2019**, 64, 5985−5998.

(29) Agrawal, M.; Han, R.; Herath, D.; Sholl, D. S. Does repeat synthesis in materials chemistry obey a power law? *Proc. Natl. Acad. Sci. U. S. A.* **2020**, 117, 877−882.

(30) Thyagarajan, R.; Sholl, D. S. A Database of Porous Rigid Amorphous Materials. *Chem. Mater.* **2020**, 32, 8020−8033.

(31) Butler, K. T.; Davies, D. W.; Cartwright, H.; Isayev, O.; Walsh, A. Machine learning for molecular and materials science. *Nature* **2018**, 559, 547−555.

(32) Boyd, P. G.; et al. Data-driven design of metal-organic frameworks for wet flue gas CO₂ capture. *Nature* **2019**, 576, 253−256.

(33) Bobbitt, N. S.; Snurr, R. Q. Molecular modelling and machine learning for high-throughput screening of metal-organic frameworks for hydrogen storage. *Mol. Simul.* **2019**, 45, 1069−1081.

(34) Bucior, B. J.; Bobbitt, N. S.; Islamoglu, T.; Goswami, S.; Gopalan, A.; Yildirim, T.; Farha, O. K.; Bagheri, N.; Snurr, R. Q. Energy-based descriptors to rapidly predict hydrogen storage in metal-organic frameworks. *Mol. Syst. Des. Eng.* **2019**, 4, 162−174.

(35) Anderson, G.; Schweitzer, B.; Anderson, R.; Gómez-Gualdrón, D. A. Attainable Volumetric Targets for Adsorption-Based Hydrogen Storage in Porous Crystals: Molecular Simulation and Machine Learning. *J. Phys. Chem. C* **2019**, 123, 120−130.

(36) Ohno, H.; Mukae, Y. Machine learning approach for prediction and search: application to methane storage in a metal-organic framework. *J. Phys. Chem. C* **2016**, 120, 23963−23968.

(37) Pardakhti, M.; Moharrer, E.; Wanik, D.; Suib, S. L.; Srivastava, R. Machine Learning Using Combined Structural and Chemical Descriptors for Prediction of Methane Adsorption Performance of Metal Organic Frameworks (MOFs). *ACS Comb. Sci.* **2017**, 19, 640−645.

(38) Wu, X.; Xiang, S.; Su, J.; Cai, W. Understanding Quantitative Relationship between Methane Storage Capacities and Characteristic Properties of Metal-Organic Frameworks Based on Machine Learning. *J. Phys. Chem. C* **2019**, 123, 8550−8559.

(39) Tsamardinos, I.; Fanourgakis, G. S.; Greasidou, E.; Klontzas, E.; Gkagkas, K.; Froudakis, G. E. An Automated Machine Learning architecture for the accelerated prediction of Metal-Organic Frame- works performance in energy and environmental applications. *Microporous Mesoporous Mater.* **2020**, 300, 110160.

(40) Dureckova, H.; Krykunov, M.; Ahaji, M. Z.; Woo, T. K. Robust Machine Learning Models for Predicting High CO₂ Working Capacity and CO₂/H₂ Selectivity of Gas Adsorption in Metal Organic Frameworks for Precombustion Carbon Capture. *J. Phys. Chem. C* **2019**, 123, 4133−4139.

(41) Burns, T. D.; Pai, K. N.; Subraveti, S. G.; Collins, S. P.; Krykunov, M.; Rajendran, A.; Woo, T. K. Prediction of MOF Performance in Vacuum Swing Adsorption Systems for Postcombus- tion CO₂ Capture Based on Integrated Molecular Simulations, Process Optimizations, and Machine Learning Models. *Environ. Sci. Technol.* **2020**, 54, 4536−4544.

(42) Deng, X.; Yang, W.; Li, S.; Liang, H.; Shi, Z.; Qiao, Z. Large- Scale Screening and Machine Learning to Predict the Computation-

Ready, Experimental Metal-Organic Frameworks for $CO_2$ Capture from Air. Appl. Sci. 2020, 10, 569.

(43) Anderson, R.; Rodgers, J.; Argueta, E.; Biong, A.; Gómez-Gualdrón, D. A. Role of Pore Chemistry and Topology in the $CO_2$ Capture Capabilities of MOFs: From Molecular Simulation to Machine Learning. Chem. Mater. 2018, 30, 6325−6337.

(44) Shi, Z.; Liang, H.; Yang, W.; Liu, J.; Liu, Z.; Qiao, Z. Machine learning and in silico discovery of metal-organic frameworks: Methanol as a working fluid in adsorption-driven heat pumps and chillers. Chem. Eng. Sci. 2020, 214, 115430.

(45) Liang, H.; Yang, W.; Peng, F.; Liu, Z.; Liu, J.; Qiao, Z. Combining large-scale screening and machine learning to predict the metal-organic frameworks for organosulfurs removal from high-sour natural gas. APL Mater. 2019, 7, 091101.

(46) Anderson, R.; Biong, A.; Gómez-Gualdrón, D. A. Adsorption Isotherm Predictions for Multiple Molecules in MOFs Using the Same Deep Learning Model. J. Chem. Theory Comput. 2020, 16, 1271−1283.

(47) Sun, Y.; DeJaco, R. F.; Siepmann, J. I. Deep neural network learning of complex binary sorption equilibria from molecular simulation data. Chem. Sci. 2019, 10, 4377−4388.

(48) Yaws, C. L. The Yaws Handbook of Physical Properties forHydrocarbons and Chemicals : Physical Properties for more than 54,000Organic and Inorganic Chemical Compounds, Coverage for C1 to C100 Organics and Ac to Zr Inorganics, 2nd ed.; Elsevier: Oxford, U.K.,2015; p vii, 823 pages.

(49) Gharagheizi, F.; Tang, D.; Sholl, D. S. Selecting Adsorbents to Separate Diverse Near-Azeotropic Chemicals. J. Phys. Chem. C 2020,124, 3664−3670.

(50) Tang, D.; Wu, Y.; Verploeggh, R. J.; Sholl, D. S. Efficiently Exploring Adsorption Space to Identify Privileged Adsorbents for Chemical Separations of a Diverse Set of Molecules. ChemSusChem2018, 11, 1567−1575.

(51) Martin, M. G.; Siepmann, J. I. Transferable Potentials for Phase Equilibria. 1. United-Atom Description of n-Alkanes. J. Phys. Chem. B1998, 102, 2569−2577.

(52) Martin, M. G.; Siepmann, J. I. Novel configurational-bias Monte Carlo method for branched molecules. transferable potentials for phase equilibria. 2. united-atom description of branched alkanes. J. Phys. Chem. B 1999, 103, 4508−4517.

(53) Chen, B.; Potoff, J. J.; Siepmann, J. I. Monte Carlo Calculations for Alcohols and Their Mixtures with Alkanes. Transferable Potentials for Phase Equilibria. 5. United-Atom Description of Primary, Secondary, and Tertiary Alcohols. J. Phys. Chem. B 2001, 105,3093−3104.

(54) Stubbs, J. M.; Potoff, J. J.; Siepmann, J. I. Transferable Potentials for Phase Equilibria. 6. United-Atom Description for Ethers, Glycols, Ketones, and Aldehydes. J. Phys. Chem. B 2004, 108,17596−17605.

(55) Wick, C. D.; Stubbs, J. M.; Rai, N.; Siepmann, J. I. Transferable Potentials for Phase Equilibria. 7. Primary, Secondary, and Tertiary Amines, Nitroalkanes and Nitrobenzene, Nitriles, Amides, Pyridine, and Pyrimidine. J. Phys. Chem. B 2005, 109, 18974−18982.

(56) Gharagheizi, F.; Mirkhani, S. A.; Ilani-Kashkouli, P.; Mohammadi, A. H.; Ramjugernath, D.; Richon, D. Determination of the normal boiling point of chemical compounds using a quantitative structure-property relationship strategy: Application to a very large dataset. Fluid Phase Equilib. 2013, 354, 250−258.

(57) Maerzke, K. A.; Schultz, N. E.; Ross, R. B.; Siepmann, J. I. TraPPE-UA Force Field for Acrylates and Monte Carlo Simulations for Their Mixtures with Alkanes and Alcohols. J. Phys. Chem. B 2009,113, 6415−6425.

(58) Zhang, L.; Siepmann, J. I. Pressure Dependence of the Vapor-Liquid-Liquid Phase Behavior in Ternary Mixtures Consisting of n-Alkanes, n-Perfluoroalkanes, and Carbon Dioxide. J. Phys. Chem. B2005, 109, 2911−2919.

(59) Wick, C. D.; Martin, M. G.; Siepmann, J. I. Transferable Potentials for Phase Equilibria. 4. United-Atom Description of Linear and Branched Alkenes and Alkylbenzenes. J. Phys. Chem. B 2000, 104,8008−8016.

(60) Rappe, A. K.; Casewit, C. J.; Colwell, K. S.; Goddard, W. A.; Skiff, W. M. UFF, a Full Periodic Table Force Field for Molecular Mechanics and Molecular Dynamics Simulations. J. Am. Chem. Soc.1992, 114, 10024−10035.

(61) Yu, J.; Xie, L.-H.; Li, J.-R.; Ma, Y.; Seminario, J. M.; Balbuena, P. B. $CO_2$ Capture and Separations Using MOFs: Computational and Experimental Studies. Chem. Rev. 2017, 117, 9674−9754.

(62) Frenkel, D.; Smit, B. Understanding Molecular Simulations: FromAlgorithms to Applications, 2nd ed.; Academic Press: San Diego, 2002; Vol. 1.

(63) Dubbeldam, D.; Calero, S.; Ellis, D. E.; Snurr, R. Q. RASPA: Molecular Simulation Software for Adsorption and Diffusion in Flexible Nanoporous Materials. Mol. Simul. 2016, 42, 81−101.

(64) Gharagheizi, F.; Eslamimanesh, A.; Mohammadi, A. H.; Richon, D. Determination of Critical Properties and Acentric Factors of Pure Compounds Using the Artificial Neural Network Group Contribution Algorithm. J. Chem. Eng. Data 2011, 56, 2460−2476.

(65) Gharagheizi, F.; Eslamimanesh, A.; Ilani-Kashkouli, P.; Mohammadi, A. H.; Richon, D. Determination of vapor pressure of chemical compounds: A group contribution model for an extremely large database. Ind. Eng. Chem. Res. 2012, 51, 7119−7125.

(66) Gharagheizi, F.; Ilani-Kashkouli, P.; Kamari, A.; Mohammadi, A. H.; Ramjugernath, D. A group contribution model for the prediction of the freezing point of organic compounds. Fluid Phase Equilib. 2014, 382, 21−30.

(67) Zhao, Y. H.; Abraham, M. H.; Zissimos, A. M. Fast calculation of van der Waals volume as a sum of atomic and bond contributions and its application to drug compounds. J. Org. Chem. 2003, 68, 7368−7373.

(68) Simon, C. M.; Smit, B.; Haranczyk, M. pyIAST: Ideal adsorbed solution theory (IAST) Python package. Comput. Phys. Commun.2016, 200, 364−380.

(69) Bae, Y.-S.; Snurr, R. Q. Development and Evaluation of Porous Materials for Carbon Dioxide Separation and Capture. Angew. Chem.,Int. Ed. 2011, 50, 11586−11596.

(70) Mason, J. A.; McDonald, T. M.; Bae, T.-H.; Bachman, J. E.; Sumida, K.; Dutton, J. J.; Kaye, S. S.; Long, J. R. Application of a high-throughput analyzer in evaluating solid adsorbents for post-combustion carbon capture via multicomponent adsorption of $CO_2$, $N_2$, and $H_2O$. J. Am. Chem. Soc. 2015, 137, 4787−4803.

(71) Coudert, F.-X. Responsive Metal−Organic Frameworks and Framework Materials: Under Pressure, Taking the Heat, in the Spotlight, with Friends. Chem. Mater. 2015, 27, 1905−1916.

(72) Chen, H.; Sholl, D. S. Examining the accuracy of ideal adsorbed solution theory without curve-fitting using transition matrix Monte Carlo simulations. Langmuir 2007, 23, 6431−6437.

(73) Agrawal, M.; Sholl, D. S. Effects of Intrinsic Flexibility on Adsorption Properties of Metal-Organic Frameworks at Dilute and Nondilute Loadings. ACS Appl. Mater. Interfaces 2019, 11, 31060−31068.

(74) Witman, M.; Ling, S.; Jawahery, S.; Boyd, P. G.; Haranczyk, M.; Slater, B.; Smit, B. The influence of intrinsic framework flexibility on adsorption in nanoporous materials. J. Am. Chem. Soc. 2017, 139,5547−5557.

(75) Gladysiak, A.; et al. Biporous Metal-Organic Framework with Tunable $CO_2/CH_4$ Separation Performance Facilitated by Intrinsic Flexibility. ACS Appl. Mater. Interfaces 2018, 10, 36144−36156.

(76) Witman, M.; Wright, B.; Smit, B. Simulating Enhanced Methane Deliverable Capacity of Guest Responsive Pores in Intrinsically Flexible MOFs. J. Phys. Chem. Lett. 2019, 10, 5929−5934.

(77) Park, J.; Howe, J. D.; Sholl, D. S. How Reproducible Are Isotherm Measurements In Metal-Organic Frameworks? Chem. Mater.2017, 29, 10487−10495.

(78) Bingel, L. W.; Chen, A.; Agrawal, M.; Sholl, D. S. Experimentally Verified Alcohol Adsorption Isotherms in Nanoporous Materials from Literature Meta-Analysis. J. Chem. Eng. Data 2020, 65,4970−4979.