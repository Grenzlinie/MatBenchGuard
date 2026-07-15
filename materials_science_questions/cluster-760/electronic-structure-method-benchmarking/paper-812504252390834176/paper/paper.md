ORIGINAL PAPER

# Density functional theory for the thermodynamic gas-phase investigation of butanol biofuel and its isomers mixed with gasoline and ethanol

Marcelo Gonçalves Martins $^{1,2}$ . Tiago da Silva Arouche $^{1}$ . Abel Ferreira Gomes Neto $^{1}$ . Jorddy Neves da Cruz $^{1}$ . Fabio Luiz Paranhos da Costa $^{3}$ . Lindemberg Lima Fernandes $^{4}$ . Raul Nunes de Carvalho Junior $^{2,5}$ . José Francisco da Silva Costa $^{6}$ . Antonio Maia de Jesus Chaves Neto $^{1,2}$

Received: 30 July 2019 / Accepted: 17 January 2021 / Published online: 11 February 2021
© The Author(s), under exclusive licence to Springer-Verlag GmbH, DE part of Springer Nature 2021

## Abstract
Herein, we present the results of our study on the thermodynamic properties of the isomers of butanol ($n$-butanol, 2-butanol, i-butanol, and $t$-butanol) to evaluate their thermodynamic potential as a complementary biofuel and/or substitute for ethanol and gasoline. The Gaussian09W software was used to perform molecular geometry optimization calculations using density functional theory with the B3lyp hybrid function using the base set 6-311++g(d,p) and the compound methods G3, G4, and CBS-QB3. Calculations of the fundamental frequency of the molecules were performed to obtain the molecular vibration modes for the respective frequencies. These calculations provided thermodynamic parameters such as the entropy, enthalpy, and specific molar heat at constant pressure, all as a function of the temperature. The parameter values obtained by each method were compared to the experimental values available in the literature. The results showed good accuracy, especially those obtained at the B3lyp/6-311++g(d,p) level for $n$-butanol. The error between the theoretical and experimental values for the combustion enthalpy of $n$-butanol was less than 4% at 298.15 K; due to the good prediction of its thermodynamic properties, we used $n$-butanol as a model for the prediction of other thermodynamic properties. We started a molecular docking study of four ligands, namely, $n$-butanol, ethanol, propanol, heptane, isooctane, and methanol interacting with butanol isomers. The highest values of affinity energy found were for N-butanol. The possible formation of hydrogen bonds, associations by means of London forces, hydrogen, and alkyl interactions were analyzed. $n$-Butanol was added to ethanol–gasoline mixtures in the temperature range of 298.15 to 600 K and the results suggest that $n$-butanol has a higher calorific value than gasoline–ethanol mixtures in G30E, G40E, G50E, G60E, G70E, G80E, G90E, and E100 blends. As such, $n$-butanol releases greater amounts of heat during combustion and is thus a viable alternative to biofuels.

Keywords Biofuel · Thermodynamic properties · DFT · Heat · Combustion enthalpy · Molecular docking

## Introduction
Studies on new fuels including mixtures of biofuels with conventional fuels [1], such as ethanol–gasoline [2], butanol–petrol [3], butanol–diesel [4], diesel–biodiesel, or kerosene–bioquerosene [5], have become increasingly frequent in recent years, especially in the transport sector, covering applications in the areas of aviation [6], maritime navigation, and

---

⊗ Antonio Maia de Jesus Chaves Neto
amchaves@ufpa.br

1 Laboratory of Preparation and Computation of Nanomaterials, Federal University of Pará, C. P. 479, Belém, PA 66075-110, Brazil
2 Post-Graduation Program of Natural Resources Engineering of Amazon, Institute of Technology, State University of Pará, 2626, Belém, PA 66050-540, Brazil
3 Universidade Federal de Goiás, Campus Jatai, Jatai, GO 75801-615, Brazil
4 ITEC, Faculdade de Engenharia Sanitaria e Ambiental – FAESA, Universidade Federal do Pará, Rua Augusto Correa, s/n, Guamá, Belem, PA 66075-110, Brazil
5 Faculdade de Engenharia de Alimentos, Universidade Federal do Pará, Rua Augusto Corrêa, Guamá, Belém, PA 66075110, Brazil
6 Universidade Federal do Pará, Campus Abaetetuba, Ramal Manoel de Abreu, S/n - Mutirão, Abaetetuba, PA 68440-000, Brazil

![](./images/812504252390834176_1.jpg)

automotive [7]. The fleet of vehicles across the planet has already exceeded the mark of 1 billion cars, implying a very high fuel demand and high emission of polluting gases to the atmosphere [8]. This has encouraged the scientific community to seek alternative energy sources that are economically viable, sustainable for the planet, and capable of replacing fuels derived from non-renewable materials [9-11]. According to the 2030 agenda for sustainable development, the global objective is to ensure reliable, sustainable, modern, and affordable access to energy for all [12].

Among the existing biofuels, ethanol is a common alternative fuel that can be produced by yeast sugar fermentation [13]. Ethanol can potentially reduce the emission levels of pollutants from internal combustion engines because it contains lower levels of carbon and sulfur and more oxygen than traditional fossil fuels [14]. Like ethanol, butanol has attracted interest in the transportation sector [15]. Butanol belongs to a category of alcohols that has been recently receiving attention as a potential alternative to petroleum fuels, as it can be produced by fermentation of biomass from algae, maize, and plant feedstocks containing cellulose [16]. Figure 1 shows the structural formulae of the butanol isomers studied in the present work.

Recently, several studies have highlighted the potential of mixtures of butanol isomers with gasoline [17-20], considering their performance in terms of the brake torque engine speed, changes in thermal efficiency, specific fuel consumption of brake (BSFC), and emission of CO, $CO_2$, NO, $NO_2$ and hydrocarbons, but little has been discussed about their thermodynamic properties, as well as the thermodynamic effects of those mixtures [21-24]. This work aimed to investigate the thermodynamic properties of butanol and isomers, and mixtures of n-butanol with gasoline-ethanol. For this, we used the Gaussian 09 W software [25] and the B3lyp methods [26, 27], with the base sets 6-311 ++ g (d, p), and
6-31 + g (d), in our calculations computational, as well as G3, [28] G4, [29] and Complete Basis Set-Quadratic Becke3 (CBS-QB3) [30] and Autodock Vina 4.0.2 [31] software was used to perform the molecular docking (DOC) process, in order to validate interactions. The thermodynamic properties evaluated were enthalpy of formation, molar enthalpy (S) and Gibbs free energy (G), and enthalpy (H) of combustion. All simulations were performed varying the temperature between 100 K and 1500 K at a constant pressure of 1 atm. The enthalpy of combustion of the butanol isomers at room temperature (298.15 K) was also calculated from the enthalpy of formation.

## Materials and methods

The molecular structures of butanol and its isomers (Fig. 1) were designed, and a conformational analysis was performed for each molecule individually with HyperChem Software 7.5 [32]. After, with the Gaussian 09 W software, each molecule was optimized using the functional B3lyp with sets of bases 6-311 ++ g (d, p) and 6-31 + g (d), G3, G4 and CBS- QB3 methods that present good precision [30, 33] with standard enthalpy of hydrocarbon formation, the data calculated by G3 and G4 (G3 / G4) for hydrocarbons are reasonably accurate when compared to experimental values. Calculations of vibrational frequency confirmed the global minimum points of the respective potential energy surfaces of the molecules, that is, the absence of imaginary frequencies [34].

The simulations carried out in this study describe the gas-phase thermochemical properties of the four butanol isomers: n-butanol, i-butanol, 2-butanol, and t-butanol. The pressure and temperature conditions in which the calculations were performed are similar to those of the fuel injection stage in internal combustion engines, which are generally pressures of

Fig. 1 Structural formulae of butanol and its isomers: a butanol, b n-butanol, c 2-butanol, d i- butanol, and e t-butanol
![](./images/812504252390834176_2.jpg)

approximately 1 atm and temperatures in the range of 298.15 to 600 K. The fuels at this stage are normally in chemical equilibrium [35, 36]. After optimization of the molecular geometries, the vibrational frequencies were calculated for each chemical compound, from which the molar enthalpy ($H$) and molar entropy ($S$) were estimated. These properties were calculated for different temperatures in the range of 100 to 1500 K, using each of the functional and base assemblies already mentioned. We also evaluated the best method to describe the thermodynamic properties of the mixtures by comparing our results with experimental values available in the literature. In addition to the highlighted properties, it was possible to calculate the specific molar heat at constant pressure ($C_\text{P}$) by means of a numerical differentiation of the enthalpy in relation to the absolute temperature, as shown in Eq. (1).

$$
C_{\mathrm{p}}=\left(\frac{\partial \mathrm{H}}{\partial \mathrm{T}}\right)_{\mathrm{p}} \tag{1}
$$

This property has great relevance, since it influences the description of fuel heating, as well as being related to mechanical properties such as the ratio of specific heats (or Poisson coefficient), which has many applications in the study of fuels, especially on their storage and driving performance. In addition to these properties, we obtained the enthalpy of combustion for each isomer, using the enthalpy of formation calculated by the presented methodologies at 298.15 K and the experimental values for the enthalpy of formation available in the literature [37] for the molecules of $\mathrm{O}_{2}$, $\mathrm{CO}_{2}$, and $\mathrm{H}_{2} \mathrm{O}$. To obtain the enthalpy of combustion ($\Delta H_\text{c}$), the difference between the enthalpy of the reaction products and the enthalpy of the reactants was calculated. For this, we used the complete combustion reaction (Eq. (2)):

$$
\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{OH}_{(\mathrm{g})}+6 \mathrm{O}_{2(\mathrm{g})} \rightarrow 4 \mathrm{CO}_{2(\mathrm{g})}+5 \mathrm{H}_{2} 0_{(\mathrm{l})}+\Delta \mathrm{H}_{\mathrm{C}} \tag{2}
$$

Although air contains molecular nitrogen ($\mathrm{N}_{2}$), this component was neglected in the combustion reaction (Eq. (2)) because it does not significantly influence the results obtained as $\mathrm{N}_{2}$ is an inert gas in fuel combustion reactions. For water condensation, the following condensation enthalpy ($\Delta H_\text{c}$) was used:$\Delta H_\text{c}=-40.66$ kJ/mol [38, 39]. To predict the thermodynamic properties of gasoline, the choice of molecules was based on the work by Burri *et al* [40, 41], where the main elements of regular gasoline used in the USA were found, as can be seen in Table 1. For this same composition, Neto et al. [38] carried out a study on the use of DFT for the prediction of the thermodynamic properties of gasoline–ethanol mixtures.

Finally, thermodynamic predictions were made on the following mixtures: *n*-butanol–gasoline, *n*-butanol–ethanol, and *n*-butanol–gasoline–ethanol, by analyzing the behavior of the enthalpy change in these mixtures in the temperature range of 298.15–600 K at pressure of 1 atm, which are the typical operating conditions of the combustion chamber. Thus, with $X$ being a thermodynamic potential at 1 atm:

$$
\Delta X=X_{(600\ K)}-X_{(298.15\ K)} \tag{3}
$$

where $\Delta X$ is the change in fuel properties due to the increasing temperature during injection in the combustion chamber.

DOC methods have the main objective of predicting the affinity mode of small molecules, and the method must be able to distinguish between molecules that are unlikely to bind to the receptor and to classify compounds with greater affinity. Among the basic tools for docking, the methods are the conformational search algorithm and the scoring function [42]. The search algorithms exploit the free energy profile to find the best way of linking (positioning) the ligand within according to the interaction, while the scoring functions assess the quality of the connection mode and select the most relevant conformations. Currently, there are several methodologies and software packages available for automated docking that provide forecasts combined with good performance and speed with low computational cost [43]. The Autodock Vina 4.0 package was used to predict the energy affinity (AE) binding modes between small ligands, and the software uses a grid method to research the available conformational space for

<table>
<caption>Table 1 Experimental values of combustion enthalpy ($\Delta \text{H}_\text{c}$) and entropy (S) (T = 289.15 K and $P = 1$ atm)</caption>
<thead>
<tr>
<th>Major components of regular gasoline</th>
<th>Percentage fractions (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2-Metilbutano</td>
<td>7.88</td>
</tr>
<tr>
<td>M-xileno</td>
<td>....</td>
</tr>
<tr>
<td>2,2,4-Trimetilpentano</td>
<td>....</td>
</tr>
<tr>
<td>Tolueno</td>
<td>5.92</td>
</tr>
<tr>
<td>2-Metipentano</td>
<td>....</td>
</tr>
<tr>
<td>N-butano</td>
<td>3.85</td>
</tr>
<tr>
<td>1,2,4-Trunetilbenzeno</td>
<td>2.83</td>
</tr>
<tr>
<td>N-pentano</td>
<td>7.27</td>
</tr>
<tr>
<td>2,3,4-Trimetilpentano</td>
<td>....</td>
</tr>
<tr>
<td>2,2,3-Trimetilpentano</td>
<td>....</td>
</tr>
<tr>
<td>3-Metilpentano</td>
<td>....</td>
</tr>
<tr>
<td>O-xileno</td>
<td>....</td>
</tr>
<tr>
<td>Etilbenzeno</td>
<td>2.70</td>
</tr>
<tr>
<td>Benzeno</td>
<td>1.35</td>
</tr>
<tr>
<td>P-xyleno</td>
<td>....</td>
</tr>
<tr>
<td>2,3-Dementilbutano</td>
<td>....</td>
</tr>
<tr>
<td>N- hexano</td>
<td>3.50</td>
</tr>
<tr>
<td>1-Metil-3-Etilbenzeno</td>
<td>1.84</td>
</tr>
<tr>
<td>1-Metil-4-Etilbenzeno</td>
<td>....</td>
</tr>
<tr>
<td>3-Metilhexano</td>
<td>....</td>
</tr>
<tr>
<td>2-Metilhexano</td>
<td>1.25</td>
</tr>
</tbody>
</table>

![](./images/812504252390834176_3.jpg)

the ligand next to a receiver, which allows an effective energy assessment of connection between the conformations [44]. In this method, the connection energy between the ligand and the receiver is calculated and the value is stored in a score. This AE score can then be used on a reference table during the DOC process. The main method for conformational search in this package is Lamarckiana genetics [45]. The "Lamarckian" aspect is an additional feature that allows indi- vidual conformations to search for their local conformational space, finding the minimums, and then passing this informa- tion on to future generations [46].

## Results and discussion

First, the thermodynamic properties of the isomers of butanol as a function of the temperature obtained through simulations are discussed. However, in order to verify which DFT method (among those chosen from the literature) is more suitable for the thermodynamic prediction of these isomers, the $C_{P}$ values were calculated at various temperatures. These theoretical values were compared to the respective experimental data available in the National Institute of Standards and Technology (NIST) database [47].

## Comparison of theoretical and experimental $C_{P}$ values

The $C_{P}$ values were obtained by the numerical derivative of the enthalpy as a function of the absolute temperature, as de- scribed in Eq. (1). This resource was used with the B3lyp functional (with the base sets 6-311++g(d,p) and 6-31+ g(d)) for the G3, G4, and CBS-QB3 methods. The results obtained for each functional were compared to the experimen- tal values available in the literature, as shown in Fig. 2 for the four butanol isomers. Based on Fig. 2, good agreement exists between the theoretical $C_{P}$ values and those available at the NIST. So as to evaluate the best methodology to estimate the $C_{P}$ values in the temperature range of 298.15-600 K, the rel- ative error between the theoretical and experimental results was calculated. It should be noted that this temperature range corresponds approximately to that of the fuel injection stage in the combustion chamber, as well as the temperatures at which fuels such as regular gasoline (G100) and ethanol (E100) [38,48,49].

![](./images/812504252390834176_4.jpg)
![](./images/812504252390834176_5.jpg)

Fig. 2 Theoretical $C_{P}$ and their respective experimental values for butanol isomers: a n-butanol, b i-butanol, c 2-butanol, and d t-butanol. The values were set as a function of the temperature and calculated with B3lyp/6-311++g(d, p), B3lyp/6-31+g(d), CBS-QB3, G3, G4, and average G3/G4 methods. The results have also been compared to the experimental data available in the NIST database

![](./images/812504252390834176_6.jpg)

![](./images/812504252390834176_7.jpg)

![](./images/812504252390834176_8.jpg)

Fig. 3 Relative errors of $C_P$ values when compared to the respective values for the butanol isomers: a $n$-butanol, b $i$-butanol, c 2-butanol, and d $t$-butanol. The values were set as a function of the temperature and calculated with the B3lyp/6-311++g(d,p), B3lyp/6-31+g(d), CBS- QB3, G3, G4, and average G3/G4 methods

Based on the results shown in Fig. 3, all methods present a percentage error of less than 10% in this temperature range. The theory level B3lyp/6–311++g(d,p) provides the smallest error among all the methodologies used to estimate $C_P$. For $n$- butanol, the maximum error was 4% at 298.15 K. Thus, this method and this isomer were chosen to represent the butanol isomers in further predictions and comparisons of the thermo- dynamic properties. As such, the best theoretical level was determined and the most appropriate functional for the predic- tion of the thermodynamic properties of the butanol isomers was determined. Figure 4 summarizes the behavior of $C_P$ as a function of the temperature for all butanol isomers. As can be seen, all isomers present very similar values at each tempera- ture. Thus, $n$-butanol was selected as it provides a simpler chemical route for its production, making it more economical- ly attractive without affecting the fuel characteristics [45].

Entropy of butanol isomers as a function of the temperature

We chose the B3lyp functional with the set of bases 6–311++ g(d,p) for the calculation of the thermodynamic properties of each butanol isomer because it provided the smallest error upon comparison of the theoretical and experimental values. We calculated the entropy values by varying the temperature from 100 to 1500 K. However, comparison of the theoretical and experimental values was only performed at 298.15 K as

![](./images/812504252390834176_9.jpg)

Fig. 4 $C_P$ values as a function of the temperature obtained at the B3lyp/6- 311++g(d,p) level

![](./images/812504252390834176_10.jpg)

<table><thead><tr><th>Butanol Isomers</th><th>Functional/ Basis Set</th><th>$S_{Theo}$ (J/mol.K)</th><th>$S_{Exp}$ (J/mol.K)</th><th>RE (%)</th></tr></thead><tbody><tr><td>n-Butanol</td><td>B3lyp/6-311++g(d,p)</td><td>335.85</td><td>361.98</td><td>7.22</td></tr><tr><td>i-Butanol</td><td>B3lyp/6-311++g(d,p)</td><td>329.49</td><td>350</td><td>5.86</td></tr><tr><td>2-Butanol</td><td>B3lyp/6-311++g(d,p)</td><td>329.31</td><td>355.57</td><td>7.38</td></tr><tr><td>t-Butanol</td><td>B3lyp/6-311++g(d,p)</td><td>323.64</td><td>–</td><td>–</td></tr></tbody></table>

the corresponding experimental values are only available at this temperature (Fig. 5) [43]. Table 2 describes the margin of error with respect to the experimental values [43]. It can be observed that the four isomers also show little differences in their entropy values at different temperatures, again indicating that $n$-butanol may be a more suitable fuel than the other isomers. The relative percentage error at room temperature was between 5.86% and 7.38%, showing the smallest devia- tion at the B3lyp/6-311++g(d,p) level for i-butanol. Moreover, the entropy increased directly proportional to the vibrational degree of freedom of these molecules: $S_{n-butanol} > S_{i-butanol} > S_{2-butanol} > S_{t-butanol}$.

### Enthalpy of combustion of butanol isomers
The enthalpy of combustion $(\Delta H_{c})$ was obtained from the difference between the enthalpy of the products and the reac- tants at 298.15 K, according to Eq. (2). The values for $\Delta H_{c}$ were obtained from the calculations performed with the B3lyp/6-311++g(d,p), B3lyp/6-31+g(d), G3, G4, and CBS- QB3 methods (Fig. 6). The six methods display good preci- sion in the prediction of the enthalpy of combustion for the four isomers, since the percentage errors are between 1.20% and 3.58%. Thus, for this property, one can employ any of the six methods. However, the best results for the $n$-butanol and i- butanol isomers were obtained with the G3 method, whereas B3lyp/6-311++g(d,p) afforded the best predictions for 2- butanol and $t$-butanol. Table 3 presents the $\Delta H_{c}$ experimental values for the butanol isomers [43, 50, 51] used to obtain the $\Delta H_{c}$ relative errors, as shown in Table 4.

![](./images/812504252390834176_11.jpg)

Fig. 5 Entropy ($S$) of butanol isomers as a function of the temperature

### Variation of molar enthalpy
The enthalpy change is related to the heat released or absorbed in a physical or chemical process. In this section, a combina- tion of the weighted average values of the enthalpy change for $n$-butanol in mixtures with ethanol and/or regular gasoline between 298.15 and 600 K, as given by Eq. (3), is discussed. This parameter was calculated under similar conditions to those at the stage of direct fuel injection in the combustion chamber [52]. In our study, we have considered gaseous mix- tures of $n$-butanol [49] with ethanol-gasoline in different pro- portions at a constant pressure of 1 atm. In addition to the above observations for G100 and E100, we also used G10E (mixture with 90% gas + 10% ethanol), G20E (mixture with 80% gas + 20% ethanol), and G30E (30% ethanol) mixtures. We thus evaluated the enthalpy change of fuels G100, E100, G10E, G20E, G30E, G40E, G50E, G60E, G70E, G80E, and G90E on the basis of the addition of $n$-butanol. The results are shown in Fig. 7(a) and (b).

Figure 7(a) and (b) shows that $n$-butanol without blending exhibits a higher enthalpy change than the E100, G90E, G80E, G70E, G60E, G50E, G40E, and G30E fuels. This re- sult makes $n$-butanol very attractive from the energetic and environmental points of view as a renewable and low pollut- ant fuel. For G100, G10E, and G20E fuels without the addi- tion of n-butanol, the percentage of $\Delta$H is higher than that of n-butanol in 13.8%, 8.5%, and 3.1%, respectively. It is impor- tant to note that when mixing G10E with 60% n-butanol, the change in enthalpy observed was very close to that of G20E

<table><thead><tr><th>Fuel</th><th>$\Delta_{c}$H (kJ/mol)</th><th>S(J/mol.K)</th></tr></thead><tbody><tr><td>n-Butanol</td><td>−2676.1</td><td>361.98</td></tr><tr><td>i-Butanol</td><td>−2669.68</td><td>350</td></tr><tr><td>2- Butanol</td><td>−2660.6</td><td>355.57</td></tr><tr><td>t- Butanol</td><td>−2644</td><td>–</td></tr></tbody></table>

Table 3 Relation between the values calculated by DFT methods and the experimental values set in Table 1 for n-butanol, i-butanol, 2-butanol, and t-butanol

<table><thead><tr><th colspan="6">Table 4 Errors relative to the experimental values for the combustion enthalpy of the butanol isomers obtained by DFT calculations</th></tr><tr><th colspan="2">n-Butanol</th><th colspan="2">i-Butanol</th><th colspan="2">2-Butanol</th><th colspan="2">t-Butanol</th></tr><tr><th>DFT method</th><th>RE (%)</th><th>DFT method</th><th>RE (%)</th><th>DFT method</th><th>RE (%)</th><th>DFT method</th><th>RE (%)</th></tr></thead><tbody><tr><td>G4</td><td>1.97</td><td>G4</td><td>2.24</td><td>B3lyp/6-311++g(d,p)</td><td>1.92</td><td>B3lyp/6-311++g(d,p)</td><td>1.2</td></tr><tr><td>B3lyp/6-311++g(d,p)</td><td>2.57</td><td>B3lyp/6-311++g(d,p)</td><td>2.25</td><td>B3lyp/6-311+g(d)</td><td>1.92</td><td>CBS-QB3</td><td>1.21</td></tr><tr><td>CBS-QB3</td><td>2.57</td><td>CBS-QB3</td><td>2.26</td><td>CBS-QBS</td><td>1.93</td><td>G4</td><td>1.22</td></tr><tr><td>B3lyp/6-311)g(d)</td><td>2.63</td><td>B3lyp/6-311++g(d,p)</td><td>2.32</td><td>G4</td><td>1.94</td><td>B3lyp/6-311+g(d)</td><td>1.29</td></tr><tr><td>G3/G4</td><td>2.78</td><td>G3/G4</td><td>2.75</td><td>G3/G$</td><td>2.44</td><td>G3/G4</td><td>1.72</td></tr><tr><td>G3</td><td>3.58</td><td>G3</td><td>3.27</td><td>G3</td><td>2.9</td><td>G3</td><td>2.22</td></tr></tbody></table>

without n-butanol. Similar results were obtained for G100 fuel mixed with 40% n-butanol, in which case the same change in enthalpy was obtained for G10E without the addition of n- butanol. This demonstrates that the addition of $n$-butanol in gasoline-ethanol mixtures makes this fuel cleaner by reducing the percentage of fossil fuel and consequently decreasing the emission of toxic gases to the environment.

From the conduct of DOC simulations, 10 conformations were obtained for each ligand, the value of the respective AE of the ligands with the receptors and their average distances, as can be seen in Table 5. The selected conformation was the one that presented interaction energy value more favorable (near to zero) and lower RMSD value, with these data it is possible to analyze the level of reliability of the predictions of the chosen method, where RMSD values less than 2.0 are consid- ered adequate. The conventional hydrogen bonds are repre- sented by lines and are green and the alkyl type bonds are purple in color as seen in Figs. 8, 9, and 10. The hydrogen bond is formed when an electronegative atom accepting the bond approaches a hydrogen atom attached to another donor electronegative atom. Different parameters can clarify the different aspects of the nature of the H bonds established for a given system. The interaction energy is the best indicator of the strength of the H bond. The geometry of the H bond complex and, in particular, the distance and angle around the H bond also provide a very good indication of this interaction, with the docking process we obtain two types of hydrogen interaction, conventional and alkyl type, with carbon. When a hydrogen bond is formed, the distance between the H atoms and the acceptor must be less than the sum of the correspond- ing van der Waals rays, the presence of this kind of bond in the docking process indicates strong interaction. Since the bonds are very close, they therefore cannot clearly enable and relate that the structural modifications contributed to the formation of better associations, exploring the differences in electroneg- ativity between the atoms. The AE analysis occurred with the strongest n-butanol among the tested positions, the best bind- ing energies, probably also the positions assumed in the com- bustion reaction.

The interactions of most ligands with their binding sites can be characterized in terms of a binding affinity. In general, the binding of the high affinity ligand results from a greater

Fig. 6 Comparison of the combustion enthalpy values of the butanol isomers obtained by different methods
![](./images/812504252390834176_12.jpg)

![](./images/812504252390834176_13.jpg)

Fig. 7 a Variation of the molar enthalpy for blends of gasoline, ethanol, and gasoline-ethanol as a function of the n-butanol content; b Variation of the molar enthalpy percentage for blends of gasoline, ethanol, and gasoline-ethanol as a function of the n-butanol content

intermolecular force between the ligand and its receptor, while the binding of the low affinity ligand involves less intermolecular force between the ligand and its receptor. Low affinity binding implies that a relatively high concentra- tion of a ligand is required before the binding site is fully occupied and the maximum physiological response to the li- gand is achieved. Empirical methods, such as docking, gener- ally use the scoring function to measure the likelihood that the ligand will bind to the target molecule.

<table><caption>Table 5 DOC interactions between selected target and ligand</caption>
<thead>
<tr>
<th>Ligand</th>
<th>2-Butanol</th>
<th></th>
</tr>
<tr>
<th></th>
<th>Affinity energy (kcal/mol)</th>
<th>Distance (nm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>n-Butanol</td>
<td>−0.9</td>
<td>2.55</td>
</tr>
<tr>
<td>Ethanol</td>
<td>−0.7</td>
<td>2.03</td>
</tr>
<tr>
<td>Heptane</td>
<td>−1.0</td>
<td>2.15</td>
</tr>
<tr>
<td>Isooctane</td>
<td>−1.1</td>
<td>3.13</td>
</tr>
<tr>
<td>Methanol</td>
<td>−0.5</td>
<td>1.17</td>
</tr>
<tr>
<td>Propanol</td>
<td>−0.8</td>
<td>3.65</td>
</tr>
<tr>
<td></td>
<td>I-Butanol</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Affinity energy (kcal/mol)</td>
<td>Distance (nm)</td>
</tr>
<tr>
<td>n-Butanol</td>
<td>−0.9</td>
<td>1.75</td>
</tr>
<tr>
<td>Ethanol</td>
<td>−0.7</td>
<td>0.96</td>
</tr>
<tr>
<td>Heptane</td>
<td>−1.0</td>
<td>2.25</td>
</tr>
<tr>
<td>Isooctane</td>
<td>−1.0</td>
<td>3.26</td>
</tr>
<tr>
<td>Methanol</td>
<td>−0.6</td>
<td>2.44</td>
</tr>
<tr>
<td>Propanol</td>
<td>−0.9</td>
<td>2.31</td>
</tr>
<tr>
<td></td>
<td>N-butanol</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Affinity energy (kcal/mol)</td>
<td>Distance (nm)</td>
</tr>
<tr>
<td>n-Butanol</td>
<td>−0.9</td>
<td>2.03</td>
</tr>
<tr>
<td>Ethanol</td>
<td>−0.6</td>
<td>1.99</td>
</tr>
<tr>
<td>Heptane</td>
<td>−0.9</td>
<td>1.68</td>
</tr>
<tr>
<td>Isooctane</td>
<td>−1.0</td>
<td>1.45</td>
</tr>
<tr>
<td>Methanol</td>
<td>−1.5</td>
<td>1.27</td>
</tr>
<tr>
<td>Propanol</td>
<td>−1.2</td>
<td>1.88</td>
</tr>
<tr>
<td></td>
<td>T-butanol</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Affinity energy (kcal/mol)</td>
<td>Distance (nm)</td>
</tr>
<tr>
<td>n-Butanol</td>
<td>−0.7</td>
<td>2.09</td>
</tr>
<tr>
<td>Ethanol</td>
<td>−0.6</td>
<td>2.26</td>
</tr>
<tr>
<td>Heptane</td>
<td>−0.9</td>
<td>2.21</td>
</tr>
<tr>
<td>Isooctane</td>
<td>−1.0</td>
<td>2.67</td>
</tr>
<tr>
<td>Methanol</td>
<td>−0.5</td>
<td>1.77</td>
</tr>
<tr>
<td>Propanol</td>
<td>−0.7</td>
<td>2.83</td>
</tr>
</tbody>
</table>

![](./images/812504252390834176_14.jpg)

Fig. 8 Interaction between n-butanol with a n-butanol and b propanol

Among the DOC processes, the simulation with n-butanol was selected for presenting better results of AE. These results highlight the potential of n-butanol. The lower binding energies of the binders result in the higher binding affinities. The lowest binding affinities detected for this simulation were −1.5 Kcal/mol and −1.2 Kcal/mol for methanol and propanol.

In the DOC process, we use the position parameters specified in the input file for the adjustment method, which is acceptable and capable of recovering the structure and interactions of a known complex. In this way, this computational process engages in the original position of the ligand in the first simulation of the complex, in an induced way, to assess whether the positions and adjustment parameters obtained by the various programs are capable of recovering the structure and interactions of a known complex and also your active connection site. With the information obtained by DOC, the interactions that obtained the best results were with n-butanol, and these six ligands were selected and widely used for the previous automated reaction coupling.

From the ADV, the interaction between n-butanol-n-butanol and n-butanol-propanol. Figure 8 has the binding affinities of −0.9 and −1.2 Kcal/mol, respectively. AE high compared to other selected compounds, a conventional hydrogen bond and an alkyl bond. From these results, it was observed that the binding affinity is slightly different, while the interaction residues are the same. Based on these results, we performed the virtual coupling and through this method it was proven that these fuels can form hydrogen bonds with other residues, in theory, they are capable of bonding to them.

The interaction of n-butanol with methanol and ethanol can be seen in Fig. 9, and these are the smallest molecules in the group of fuels we analyzed; the distances ranged from 1.99 to 1.27 Å, as shown in Table 5. Both obtained a bond of hydrogen with n-butanol. The highest affinity energy value for the interaction with n-butanol was methanol. The AE conformation and variations for the molecular adjustment between small molecules were shown in Fig. 10. It was observed that heptane and isooctane obtained AE of −1.0 and −0.9 Kcal/mol were the lowest AE values when compared to the others molecules used in the experiment. It was evident that heptane and isooctane obtained alkyl-type bonds when interacting with n-butanol.

DOC results were verified considering some of the main conformations, and AE for the best punctuated conformation, Fig. 11a shows the result of the interaction and the connection distances between the studied molecules n-butanol, ethanol, heptane, isooctane and 11b of n-butanol, methanol, heptane, isooctane. The fitting results demonstrate interaction between these molecules smaller than 3 Å indicating their mode of interaction in the combustion stage.

![](./images/812504252390834176_15.jpg)

Fig. 9 Interaction between n-butanol with a ethanol and b methanol

![](./images/812504252390834176_16.jpg)

Fig. 10 Interaction between n-butanol with a heptane and b isooctane

![](./images/812504252390834176_17.jpg)

![](./images/812504252390834176_18.jpg)

Fig. 11 Interactions between n-butanol with a heptane, ethane, isooctane,
and b heptane, isooctane, methanol

## Conclusions

Based on the results, the $C_P$ values were successfully calculated with all proposed methodologies (B3lyp/6-311++g(d,p), B3lyp/6-311+g(d), CBS-QB3, G3, G4, and G3/G4), but the level of theory B3lyp/6-311++g(d,p) was the one that provided results closer to the experimental values. Therefore, we used this level of theory to obtain the other thermodynamic properties presented. The molar entropy of each isomer was calculated at the B3lyp/6-311++g(d,p) level in the temperature range of 100 to 1500 K. We established a comparison with the available experimental values for the temperature at 298.15 K. The error obtained was 7.22% for $n$-butanol, 5.86% for i-butanol, and 7.86% for 2-butanol. To obtain the enthalpy of combustion of the isomers, we used B3lyp/6-311++g(d,p), B3lyp/6-311+g(d), CBS-QB3, G3, G4, and the arithmetic mean of G3 and G4 (G3/G4). The B3lyp/6-311++g(d,p) method provided an error relative to the experimental values of 2.57% for $n$-butanol, 2.25% for i-butanol, 1.92% for 2-butanol, and 1.2% for $t$-butanol. We chose $n$-butanol as the model compound which, in addition to exhibiting a $C_P$ value similar to that of the other isomers, involves a simpler synthesis route and is economically more viable than the other isomers [53]. $n$-Butanol was added to ethanol-gasoline mixtures in the temperature range of an internal combustion chamber (298.15-600 K) and pressure of 1 atm. It is noteworthy that, by mixing 60% $n$-butanol with G10E, we obtained an enthalpy change very close to that of the G20E blend without $n$-butanol. Similar results were obtained for G100 blended with 40% $n$-butanol, in which case we practically obtained the enthalpy change of G10E without $n$-butanol. It can thus be concluded that butanol is a better biofuel than ethanol because it is more energetic, as well as affording cleaner combustion when compared to fossil fuels [54].

Docking was able to classify the ligands based on an accurate prediction of posture and the ability of the ligand to interact. The applied methodology allowed to identify interactions, between the targets found, these have a strong influence on the development and evolution of the combustion mechanisms and can be used later as a parameter for experimental studies. The ligands showed stable conformations and little affinity energy, indicating spontaneous reaction. Because they are very close links and with high interactivity, they, therefore, can enable and clearly relate that chemical reactions occur and contribute to the formation of better associations. The higher the AE values, the stronger the interactions that occur between the ligand molecules and the receptors. Among the tested positions, the best binding energies are likely to also be the positions assumed in the biological environment. The analysis made it possible to identify a strong interaction and reaction in combustion, as it presents itself as a starting point to improve the knowledge that involves interactions with propanols.

Acknowledgements Abel F. G. Neto and Antonio M. J. C. Neto thank CNPq and CAPES for their support.

Author contribution All authors designed and developed the study. All authors read and approved the final version of the manuscript.

Funding This study was partially funded by: CNPq (Process: 312824/2017-3).

Data availability The data used to support the findings of this study are included within the article. The authors authorize the use of figures, tables, or text passages that will be published in the journal.

## Declarations

Ethics approval The researchers conducted their research, from the research proposal to publication, in accordance with the best practices and codes of conduct of relevant professional bodies and national and international regulatory bodies.

Conflict of interest The authors declare that they have no conflict of interest.

![](./images/812504252390834176_19.jpg)

## References

1. Goodger EM, Vere R (1985) *Aviation Fuels Technology*. Macmillan, London

2. Carpio LGT, Simone de Souza F (2017) Optimal allocation of sugarcane bagasse for producing bioelectricity and second- generation ethanol in Brazil: scenarios of cost reductions. *Renew. Energy* 111:771–780

3. Xu Y, Avedisian CT (2015) Combustion of *n*-butanol, gasoline, and *n*-butanol/gasoline mixture droplets. *Energy & Fuels* 29(5): 3467–3475

4. Das AK, Hong P-D (2011) Solute–solvent friction kernels and so- lution properties of methyl oxazoline–phenyl oxazoline (MeOx– PhOx) copolymers in binary ethanol–water mixtures. *Phys. Chem. Chem. Phys.* 13(25):11892

5. Mustafa KF, Abdullah S, Abdullah MZ, Sopian K, Ismail AK (2015) Experimental investigation of the performance of a liquid fuel-fired porous burner operating on kerosene-vegetable cooking oil (VCO) blends for micro-cogeneration of thermoelectric power. *Renew. Energy* 74:505–516

6. *Chevron Global Aviation Aviation Fuels Technical Review*; 2006

7. Hassan MH, Kalam MA (2013) An overview of biofuel as a renew- able energy source: development and challenges. *Procedia Eng.* 56: 39–53

8. Perera, F. Pollution from fossil-fuel combustion is the leading en- vironmental threat to global pediatric health and equity: solutionsexist. *Int. J. Environ. Res. Public Health* 2017, 15 (1)

9. Petrou EC, Pappis CP (2009) Biofuels: a survey on pros and cons.*Energy & Fuels* 23(2):1055–1066

10. Neto AFG, Marques FC, Amador AT, Ferreira ADS, Neto AMJC (2019) DFT and canonical ensemble investigations on the thermo- dynamic properties of syngas and natural gas/syngas mixtures.*Renew. Energy* 130:495–509

11. Owusu, P. A.; Asumadu-Sarkodie, S. A review of renewable ener- gy sources, sustainability issues and climate change mitigation.*Cogent Eng.* 2016, 3 (1)

12. Nations, U. *Transforming Our World: The 2030 Agenda for Sustainable Development Transforming Our World: The 2030Agenda for Sustainable Development Preamble*; 2030

13. Zhang S, Maréchal F, Gassner M, Périn-Levasseur Z, Qi W, Ren Z, Yan Y, Favrat D (2009) Process modeling and integration of fuel ethanol production from lignocellulosic biomass based on double acid hydrolysis. *Energy & Fuels* 23(3):1759–1765

14. Karavalakis G, Durbin TD, Shrivastava M, Zheng Z, Villela M, Jung H (2012) Impacts of ethanol fuel level on emissions of regu- lated and unregulated pollutants from a fleet of gasoline light-dutyvehicles. *Fuel* 93:549–558

15. Harvey BG, Meylemans HA (2011) The role of butanol in the development of sustainable fuel technologies. *J. Chem. Technol.Biotechnol.* 86(1):2–9

16. Karimi K, Tabatabaei M, Sárvári Horváth I, Kumar R (2015) Recent trends in acetone, butanol, and ethanol (ABE) production.*Biofuel Res. J.* 2(4):301–308

17. Dernotte J, Mounaim-Rousselle C, Halter F, Seers P (2010) Evaluation of butanol-gasoline blends in a port fuel-injection, spark-ignition engine. *Oil Gas Sci. Technol. – Rev. l'InstitutFrançais du Pétrole* 65(2):345–351

18. Singh SB, Dhar A, Agarwal AK (2015) Technical feasibility study of butanol–gasoline blends for powering medium-duty transporta-tion spark ignition engine. *Renew. Energy* 76:706–716

19. Hergueta C, Bogarra M, Tsolakis A, Essa K, Herreros JM (2017) Butanol-gasoline blend and exhaust gas recirculation, impact onGDI engine emissions. *Fuel* 208:662–672

20. Merola S, Tornatore C, Marchitto L, Valentino G, Corcione F (2012) Experimental investigations of butanol-gasoline blends effects on the combustion process in a SI engine. *Int. J. EnergyEnviron. Eng.* 3(1):6

21. Puli D, Ravi Kumar P (2015) Performance and emission character- istics of tertiary butyl alcohol gasoline blends on a spark ignitionengine. *Biofuels* 6(1–2):71–78

22. Gu X, Huang Z, Cai J, Gong J, Wu X, Lee C (2012) Emission characteristics of a spark-ignition engine fuelled with gasoline-n-butanol blends in combination with EGR. *Fuel* 93:611–617

23. Mack JH, Schuler D, Butt RH, Dibble RW (2016) Experimental investigation of butanol isomer combustion in homogeneous chargecompression ignition (HCCI) engines. *Appl. Energy* 165:612–626

24. Wigg, B.; Coverdill, R.; Lee, C.-F.; Kyritsis, D. Emissions charac- teristics of neat butanol fuel using a port fuel-injected, spark-ignition engine; 2011

25. Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Mennucci, B.; Petersson, G. A.; et al. Gaussian 09, Revision B.01. *Gaussian 09, Revision B.01, Gaussian, Inc., Wallingford CT*. Wallingford CT2009

26. Becke A, Density-functional D (1993) thermochemistry. III. TheRole of Exact Exchange. *J. Chem. Phys.* 98(7):5648–5652

27. Lee, Yang, Parr (1988) Development of the Colle-Salvetti correla- tion-energy formula into a functional of the electron density. *Phys.Rev. B. Condens. Matter* 37(2):785–789

28. Curtiss LA, Raghavachari K, Redfern PC, Rassolov V, Pople JA (1998) Gaussian-3 (G3) Theory for molecules containing first andsecond-row atoms. *J. Chem. Phys.* 109(18):7764

29. Curtiss LA, Redfern PC, Raghavachari K (2007) Gaussian-4Theory. *J. Chem. Phys.* 126(8):084108

30. Simmie JM, Somers KP (2015) Benchmarking compound methods (CBS-QB3, CBS-APNO, G3, G4, W1BD) against the active ther- mochemical tables: a litmus test for cost-effective molecular forma-tion enthalpies. *J. Phys. Chem. A* 119(28):7235–7246

31. Trott O, Olson AJ (2010) Autodock Vina: Improving the speed and accuracy of docking with a new scoring function, efficient optimi- zation, and multithreading. Journal of Computational Chemistry.31(2):455–461

32. Froimowitz M (1993) HyperChem: A software package for com-putational chemistry and molecular modeling. *Biotechniques* 14(6):1010–1013

33. Simmie JM (2015) A database of formation enthalpies of nitrogen species by compound methods (CBS-QB3, CBS-APNO, G3, G4).*J. Phys. Chem. A* 119(42):10511–10526

34. Neese F (2009) Prediction of molecular properties and molecular spectroscopy with density functional theory: from fundamental the-ory to exchange-coupling. *Coord. Chem. Rev.* 253(5–6, 526):–563

35. Poroikov VV, Filimonov DA, Ihlenfeldt W-DD, Gloriozova TA, Lagunin AA, Borodina YV, Stepanchikova AV, Nicklaus MC, Poroikov VV, Filimonov DA et al (2003) PASS biological activity spectrum predictions in the enhanced open NCI database browser.*J. Chem. Inf. Comput. Sci.* 43(1):228–236

36. Kim, Y.; Hoon Sohn, C.; Hong, M.; Lee, S. Y. An analysis of fuel- oxidizer mixing and combustion induced by swirl coaxial jet injec- tor with a model of gas-gas injection. *Aerosp. Sci. Technol.* 2014,37

37. Cox JD, Wagman DD, Medvedev VA, Vadim A (1989) *CODATA Key Values for Thermodynamics*. Hemisphere Pub Corp, NewYork

38. Neto AFG, Lopes FS, Carvalho EV, Huda MN, Neto AMJC, Machado NT (2015) Thermodynamic analysis of fuels in gas phase: ethanol, gasoline and ethanol — gasoline predicted byDFT method. *J. Mol. Model.* 21(10):267

39. Neto AFG, Huda MN, Marques FC, Borges RS, Neto AMJC (2017) Thermodynamic DFT analysis of natural gas. *J. Mol.Model.* 23(8):224

![](./images/812504252390834176_20.jpg)

40. Ndaba B, Chiyanzu I, Marx S (2015) N-butanol derived from bio- chemical and chemical routes: a review. *Biotechnol. Reports* 8:1–9

41. Venugopal T, Ramesh A (2014) Performance, Combustion and emission characteristics of a spark-ignition engine with simulta- neous injection of n-butanol and gasoline in comparison to blended butanol and gasoline. *Int. J. Energy Res.* 38(8):1060–1074

42. Yang Z, Liu Y, Chen Z, Xu Z, Shi J, Chen K, Zhu W (2015) A quantum mechanics-based halogen bonding scoring function for protein-ligand interactions. Journal of Molecular Modeling. 21(6): 1–21

43. Heck GS, Pintro VO, Pereira RR, Ávila MB, Levin NMB, Azevedo WF (2017) Supervised machine learning methods applied to predict ligand- binding affinity. Current Medicinal Chemistry. 24(23): 2459–2470

44. Monteagudo MC, Díaz HG, Chapín GA, Santana L, Borges F, Dominguez ER, Podda G, Uriarte E (2007) Computational chem- istry development of a unified free energy Markov model for the distribution of 1300 chemicals to 38 different environmental or biological systems. Journal of Computational Chemistry. 2811: 1909–1923

45. Therrien E, Englebienne P, Arrowsmith AG, Sanchez RM, Corbeil VR, Weill N, Slater VC, Moitessier N (2011) Integrating medicinal chemistry, organic/combinatorial chemistry, and computational chemistry for the discovery of selective estrogen receptor modula- tors with forecaster, a novel platform for drug discovery. Journal of Chemical Information and Modeling. 521:210–224

46. Korlach J, Baird DW, Heikal AA, Gee KR, Hoffman GR, Webb WW (2004) Spontaneous nucleotide exchange in low molecular weight GTPases by fluorescently labeled -phosphate-linked GTP analogs. Proceedings of the National Academy of Sciences. 101(9):2800–2805

47. NIST Chemistry WebBook, NIST Standard Reference Database Number 69; Linstrom, P. J., Mallard, W. G., Eds.; National Institute of Standards and Technology: Gaithersburg MD, 20899, 2005

48. Yusri IM, Mamat R, Najafi G, Razman A, Awad OI, Azmi WH, Ishak WFW, Shaiful AIM (2017) Alcohol based automotive fuels from first four alcohol family in compression and spark ignition engine: a review on engine performance and exhaust emissions. *Renew. Sustain. Energy Rev.* 77:169–181

49. Hirshfeld DS, Kolb JA, Anderson JE, Studzinski W, Frusti J (2014) Refining economics of U.S. Gasoline: octane ratings and ethanol content. *Environ. Sci. Technol.* 48(19):11064–11071

50. Burri J, Crockett R, Hany R, Rentsch D (2004) Gasoline Composition Determined by 1H NMR Spectroscopy. *Fuel* 83(2): 187–193

51. Liu H, Lee C, Huo M, Yao M (2011) Comparison of ethanol and butanol as additives in soybean biodiesel using a constant volume combustion chamber. *Energy & Fuels* 25(4):1837–1846

52. Westbrook CK (2013) Biofuels combustion. *Annu. Rev. Phys. Chem.* 64(1):201–219

53. Xin H, Kyle EN, Kyle BB, Chih-Jen S (2017) Reduced chemistry for butanol isomers at engine-relevant conditions. *Energy & Fuels* 31(1):867–881

54. Yuhao X (2015) C. Thomas A. Combustion of n-butanol, gasoline, and n-butanol/gasoline mixture droplets. *Energy & Fuels* 29(5): 3467–3475

Publisher's note Springer Nature remains neutral with regard to jurisdic- tional claims in published maps and institutional affiliations.

![](./images/812504252390834176_21.jpg)
