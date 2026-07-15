# A Thermodynamic Analysis of Selective Area CVD of Titanium Nitride Compound by the Alternating Cyclic Method

Q. S. Wang
Department of Physics, North Carolina State University, Raleigh, North Carolina 27695-8202

A. Reisman*
Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, North Carolina 27695-7911

D. Temple
MCNC, Electronic Technologies Division, Research Triangle Park, North Carolina 27709-2889

## ABSTRACT

As the first step in investigating the selective area chemical vapor deposition of titanium compounds, which are of considerable interest in semiconductor technology, a thermodynamic analysis has been performed for the selective area chemical vapor deposition of titanium nitride, over an extensive temperature, pressure, and composition range, using the alternating cyclic (A.C.) process. In this approach TiN deposition via the hydrogen reduction of $\text{TiCl}_4$ is followed cyclically by the etching of spurious nuclei from mask regions via an embedded disproportionation reaction. The thermodynamic calculations have been set up using a first principles analysis, and carried out via the computer program, SOLGASMIX, which is based on the minimization of the system's Gibbs free energy. The first principles constraining conditions and the equilibrium constant constraining equations have then been employed as integrity checks of the outputs of the computer program. In addition, using the first principles approach, solid-vapor solubility curves have been derived for the cases examined. These calculations have indicated that the selective deposition of TiN by this novel method is feasible and have defined the parameter space in which to conduct the selective area deposition in A.C. fashion.

Titanium compounds, such as TiN, TiC, $\text{TiB}_2$, and $\text{TiSi}_2$, have found a wide variety of technological applications due to their interesting mechanical, optical, and electrical properties. A typical property of these compounds is their chemical and thermal inertness, which makes them important protective coating materials, particularly on cutting tools. In addition, the electrical resistivities of these titanium compounds are as low or lower than the nitrides, carbides, borides, or silicides of any other metal.¹ Thus, they have been recognized as good contacts and contact barriers between interactive materials, particularly at high temperatures. Among the titanium compounds, TiN has been of most interest and has been extensively investigated in a number of earlier studies.²⁻¹⁵ In addition to these common properties, TiN has shown potential applications in semiconductor technology. As a diffusion barrier layer, in place of silicide barriers, such as PtSi, $\text{CoSi}_2$, $\text{MoSi}_2$ and $\text{TiSi}_2$, TiN thin films have become essential for reliable interconnection between overlying metal and silicon in silicon devices.⁶,⁸,¹⁴ Such films are generally deposited using sputtering techniques and are not, therefore, inherently selective, requiring, as a consequence, additional processing steps.

However, chemical vapor deposition (CVD), especially low pressure chemical vapor deposition (LPCVD), of the titanium compounds has also shown considerable promise, since it is able to provide uniform and conformal deposition which is required for forming protective coatings and barrier layers. As with the sputtering approach, LPCVD of titanium compounds has not been selective either. Metal halides, such as $\text{TiCl}_4$, $\text{TiBr}_4$, and $\text{TiI}_4$ have been used as the vapor source for LPCVD processes, due to their high vapor pressures. LPCVD of titanium nitride using $\text{TiCl}_4$ plus either nitrogen and hydrogen, or ammonia, as the source materials has been examined and shown to be applicable to device fabrication.²,⁸,¹¹,¹³,¹⁴

By examining the applications of TiN in advanced semiconductor device technology, such as filling high aspect ratio submicron contact holes in very large scale integrated (VLSI) device fabrication, it would be both desirable and a challenge to achieve selective area deposition in the LPCVD of TiN. However, none of the early work has attempted to achieve this end-result.

It has been proposed and demonstrated that the alternating cyclic (A.C.) process can be successfully used for selective tungsten deposition.¹⁶,¹⁷ Here an embedded disproportionation reaction is made dominant cyclically during sequential deposition and etching cycles which deposit the material selectively, then remove incipient or spurious nuclei grown on masks and other unwanted regions. To make the selective deposition possible, of course, an incubation period must be present in which initial deposition takes place preferentially on exposed silicon or some other desired area(s). This incubation period has been found to exist in many studies dealing with attempts at selective area deposition using more conventional approaches.¹⁸⁻²⁰

It is our goal to implement the A.C. technique for the selective deposition of TiN on silicon wafers using a reaction based on $\text{TiCl}_4 + \text{H}_2 + \text{N}_2$ or $\text{TiCl}_4 + \text{NH}_3$. The A.C. selective deposition process would involve cycling the hydrogen (or ammonia) on and off while maintaining continuous flows of $\text{TiCl}_4$ and $\text{N}_2$, if the process involves the first reaction. TiN deposition occurs when the hydrogen (or ammonia) is on, while etching of TiN would occur when hydrogen (or ammonia) is turned off. This sequence provides a potentially powerful mechanism for removing spurious nuclei of TiN in unwanted areas. The selectivity can be achieved by carrying out the two processes in an alternating cyclic, A.C., fashion. To investigate the feasibility of the selective deposition of TiN, a detailed thermodynamic analysis is essential to establish boundaries for the process, and this analysis is the focus of the present paper.

The method employed for calculating the present thermodynamic system for selective deposition of TiN was also employed to define boundaries for the selective CVD of silicon by the A.C. process.²¹ As the first step of the calculations, a set of "first principles" constraining equations for analyses both of TiN deposition in the four component Ti-H-N-Cl system, and etching of TiN in the three component Ti-N-Cl system is defined. This involves setting up general system constraints, such as total system pressure, and required input component ratios, in order to make the system univariant. Then the important species present are specified in a set of equilibrium constant constraining equa-

* Electrochemical Society Fellow.

1086
J. Electrochem. Soc., Vol. 141, No. 4, April 1994 © The Electrochemical Society, Inc.

tions, which are a function of temperature. Having estab- lished this set of constraints, a computer program, SOL- GASMIX, $^{22-24}$ was used to calculate the partial pressures of all the species in each system at given total pressures, tem- peratures, and input component ratios, based on the tech- nique of minimizing the system's Gibbs free energy. Then the constraining values in the set of equations in the first principles analysis were used as integrity checks for the computer program outputs. Finally, the first principles analysis approach was used to derive the univariant solid- vapor solubility curve-phase diagrams, in terms of the equilibrium component vapor-phase Ti/Cl ratio, as a func- tion of temperature for each set of constraining conditions using the bridge between component and vapor-phase spe- cies partial pressures. From these phase diagrams, one caneasily determine whether deposition or etching is predicted thermodynamically for a given set of system conditions. $^{25}$  Additionally, by inspection, the TiN growth and etching rate can be deduced by knowing the input gas flow rate, and assuming that the overall reaction is easily reversible. Such results provide the "control" with which to compare actual experimentally derived results.

In the present paper, we first show the thermodynamic analyses for the Ti-N-H-Cl and Ti-N-Cl chemical systems. Then, taken in combination, the results of these calcula- tions for the respective deposition and etching processes are employed to analyze the feasibility of the A.C. process as an approach to the selective deposition of TiN. Based on the results obtained with the Si-H-Cl and Si-H-Cl-Ar sys- tems, an inert gas such as argon can be introduced into the system to enhance attainment of equilibrium during the on-off cycles. An inert gas does not perturb the solubility curves appreciably. Thus, if $NH_{3}$ is used as a reactant, when its flow is cycled on and off, the argon flow would continue unabated.

### TiN Deposition Process in the Ti-N-H-Cl System
First principles approach.-The Ti-N-H-Cl system con- tains four components, Ti, N, H, and Cl, coexisting in two phases, solid (TiN) and a vapor phase. Eleven vapor-phase species were assumed present in the system based on the data in the JANAF tables: $^{26} TiCl_{4}, TiCl_{3}, TiCl_{2}, TiCl, NH_{3}$ , N2, H2, Cl2, HCI, H, Cl. The thermodynamic data for these species were all obtained from JANAF tables in the present analysis. Some nitrogen chlorides, such as $NCl, NCl_{2}, NCl_{3}$ , NCl, were considered, but they were left out of our cal-
$$
\begin{aligned}
\left(\frac{p_{\mathrm{Ti}}}{p_{\mathrm{Cl}}}\right)_{\text {input }} & =\frac{p_{\mathrm{TiCl}_{4}}+p_{\mathrm{TiCl}_{3}}+p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+\frac{1}{2}\left(p_{\mathrm{Cl}_{2}}-\frac{1}{2} p_{\mathrm{TiCl}_{3}}-p_{\mathrm{TiCl}_{2}}-\frac{3}{2} p_{\mathrm{TiCl}}+\frac{1}{2} p_{\mathrm{HCl}}+\frac{1}{2} p_{\mathrm{Cl}}\right)}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}+p_{\mathrm{HCl}}} \\
& =\frac{p_{\mathrm{TiCl}_{4}}+\frac{3}{4} p_{\mathrm{TiCl}_{3}}+\frac{1}{2} p_{\mathrm{TiCl}_{2}}+\frac{1}{4} p_{\mathrm{TiCl}}+\frac{1}{2} p_{\mathrm{Cl}_{2}}+\frac{1}{4} p_{\mathrm{HCl}}+\frac{1}{4} p_{\mathrm{Cl}}}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}+p_{\mathrm{HCl}}}=\frac{1}{4} \quad[13]
\end{aligned}
$$
culations because of the unavailability of thermodynamic data in the literature up to the time of the writing of the present paper.

Applying the Gibbs-phase rule, there are four degrees of freedom for this four-component, two-phase system, mak- ing it quadrivariant. The four independent variables can be chosen as the total system pressure, two different compo- nent partial pressure input gas-phase ratios, and finally, the temperature. When the total pressure, $p_{t}$ , is fixed, the system becomes trivariant. By fixing the input hypotheti- cal component partial pressure ratio, $P_{H} / P_{Cl}$ , denoted as H/Cl, and the input titanium to chlorine partial pressure ratio, $(P_{Ti} / P_{Cl})_{input }$ , denoted as $(Ti / Cl)_{input }$ , the system be comes univariant. Finally the system becomes uniquely de- fined if the temperature is specified. Such a final specifica- tion results, of course, in unique constraining value for each of the arbitrary equilibrium constants chosen to de- fine the system.

Using the $p_{t}, H / Cl$ , and $(Ti / Cl)_{input }$ constraints, each ex pressed in terms of species partial pressures of the assumed eleven vapor-phase species, eight additional constraining equations are required, which are satisfied by the eight independent chemical reactions expressed in Eq. 1-8, in terms of their equilibrium constants at given temperatures. Once a temperature is chosen, the set of eleven equations is defined uniquely
$$2 \mathrm{TiCl}_{4}(\mathrm{v})+\mathrm{N}_{2}(\mathrm{v})=2 \mathrm{TiN}(\mathrm{s})+4 \mathrm{Cl}_{2}(\mathrm{v})\qquad[1]$$

$$\mathrm{N}_{2}(\mathrm{v})+3 \mathrm{H}_{2}(\mathrm{v})=2 \mathrm{NH}_{3}(\mathrm{v})\qquad[2]$$

$$\mathrm{H}_{2}(\mathrm{v})+\mathrm{Cl}_{2}(\mathrm{v})=2 \mathrm{HCl}(\mathrm{v})\qquad[3]$$

$$2 \mathrm{TiCl}_{4}(\mathrm{v})=2 \mathrm{TiCl}_{3}(\mathrm{v})+\mathrm{Cl}_{2}(\mathrm{v})\qquad[4]$$

$$\mathrm{TiCl}_{4}(\mathrm{v})=\mathrm{TiCl}_{2}(\mathrm{v})+\mathrm{Cl}_{2}(\mathrm{v})\qquad[5]$$

$$2 \mathrm{TiCl}_{4}(\mathrm{v})=2 \mathrm{TiCl}(\mathrm{v})+3 \mathrm{Cl}_{2}(\mathrm{v})\qquad[6]$$

$$\mathrm{H}_{2}(\mathrm{v})=2 \mathrm{H}(\mathrm{v})\qquad[7]$$

$$\mathrm{Cl}_{2}(\mathrm{v})=2 \mathrm{Cl}(\mathrm{v})\qquad[8]$$

In fact, a different set of reactions could have been cho- sen to replace Eq. 1-8, provided that these reactions involve the same assumed species in the system and are indepen- dent of each other, i.e., no reaction can be expressed by an algebraic combination of two or more of the remaining ar- bitrary reactions. For example, one can assume two alter- native reactions for TiN deposition as depicted in Eq. 9 and10, representing adequate replacements for Eq. 1
$$6 \mathrm{TiCl}_{4}(\mathrm{v})+8 \mathrm{NH}_{3}(\mathrm{v})=6 \mathrm{TiN}(\mathrm{s})+24 \mathrm{HCl}(\mathrm{v})+\mathrm{N}_{2}(\mathrm{v}) \quad[9]$$

$$2 \mathrm{TiCl}_{4}(\mathrm{v})+\mathrm{N}_{2}(\mathrm{v})+4 \mathrm{H}_{2}(\mathrm{v})=2 \mathrm{TiN}(\mathrm{s})+8 \mathrm{HCl}(\mathrm{v}) \quad[10]$$

However, Eq. 9 can be obtained by an algebraic combina- tion of $3 \cdot$ [Eq. 1]-12 $\cdot$ [Eq. 3]-4 $\cdot$ [Eq. 2], and Eq. 10 can be obtained by Eq. 1-4 - [Eq. 3]. Therefore, neither of these reactions are independent of the ones described in Eq. 1-8.

The $p_{t}, H / Cl$ , and $(Ti / Cl)_{input }$ constraints can be defined in terms of species partial pressures as shown in Eq. 11-13. The remaining variable, temperature, is constrained in terms of appropriate equilibrium constants for Eq. 1-8, which will be described subsequently
$$\begin{aligned}
p_{\mathrm{t}}=p_{\mathrm{TiCl}_{4}} & +p_{\mathrm{TiCl}_{3}}+p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}} \\
& +p_{\mathrm{NH}_{3}}+p_{\mathrm{N}_{2}}+p_{\mathrm{H}_{2}}+p_{\mathrm{Cl}_{2}}+p_{\mathrm{HCl}}+p_{\mathrm{H}}+p_{\mathrm{Cl}} \quad[11]
\end{aligned}$$

$$\frac{p_{\mathrm{H}}}{p_{\mathrm{Cl}}}=\frac{3 p_{\mathrm{NH}_{3}}+2 p_{\mathrm{H}_{2}}+p_{\mathrm{HCl}}+p_{\mathrm{H}}}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}+p_{\mathrm{HCl}}} \quad[12]$$

Equation 11 conserves the total system pressure (assum- ing, as is done throughout, that all species behave ideally in the vapor phase).

Equation 12 represents the component input conserva- tion equation for H and Cl, in terms of their derived species. Notice that these two components are always confined to the vapor phase, so that this ratio can be deduced by inspection.

Equation 13 gives the corresponding expression for the conservation of the input Ti/Cl ratio. Notice that in the present instance, since $TiCl_{4}$ is the titanium source, this input ratio is 1/4. However, unlike the input component ratio H/Cl, which remains constant in the vapor phase ev- erywhere in the system, the component Ti is not confined to the vapor phase, since some fraction of it may precipitate as TiN. To conserve this input component Ti/Cl ratio, a "marker" is, therefore, needed to account for precipitated Ti. From Eq. 1 we see that for each two molecules of the vapor phase species $TiCl_{4}$ consumed, four molecules of the vapor-phase species, $Cl_{2}$ , are generated, along with two molecules of the solid species, TiN. To conserve the input

component Ti/Cl ratio, therefore, the generated Cl₂ can be used as a marker representing the TiCl₄ consumed, which is no longer in the vapor phase. Since the species ratio, TiCl₄/Cl₂, in Eq. 1 is 1/2, i.e., \(p_{\text{TiCl}_4} = p_{\text{Cl}_2}/2\), if no other complications exist, the input Ti/Cl component ratio would be conserved as shown in Eq. 14

$$
(\mathrm{Ti} / \mathrm{Cl})_{\text {input }}=\frac{p_{\mathrm{TiCl}_{4}}+p_{\mathrm{TiCl}_{3}}+p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+\frac{1}{2} p_{\mathrm{Cl}_{2}}}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}+p_{\mathrm{HCl}}}
$$

[14]

Notice, however, that from Eq. 4-6, Cl₂ is also generated via the dissociation of TiCl₄, forming its subchlorides TiCl₃, TiCl₂, and TiCl, plus additional Cl₂ in the process. The partial pressures of these subchlorides can serve as markers for the excess Cl₂ generated during the TiCl₄ dissociative process. This excess Cl₂, defined in terms of the markers TiCl₃, TiCl₂, and TiCl, must be subtracted from the term \(p_{\text{Cl}_2}/2\) in Eq. 14, since only that Cl₂, which represents precipitated Ti, can appear in the conservation equation for the input Ti/Cl component ratio. As an example, notice in Eq. 4 that the TiCl₃/Cl₂ species ratio is 2/1, then the \(p_{\text{Cl}_2}\) derived is equal to \(p_{\text{TiCl}_3}/2\). Similarly, we conclude from Eq. 5 and 6 that \(p_{\text{Cl}_2}=p_{\text{TiCl}_2}\) and \(p_{\text{Cl}_2}=3p_{\text{TiCl}}/2\). This leads to the intermediate corrected equation, Eq. 15

$$
\left(\frac{P_{\mathrm{Ti}}}{P_{\mathrm{Cl}}}\right)_{\text {input }}=\frac{p_{\mathrm{TiCl}_{4}}+p_{\mathrm{TiCl}_{3}}+p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+\frac{1}{2}\left(p_{\mathrm{Cl}_{2}}-\frac{1}{2} p_{\mathrm{TiCl}_{3}}-p_{\mathrm{TiCl}_{2}}-\frac{3}{2} p_{\mathrm{TiCl}}\right)}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}+p_{\mathrm{HCl}}}
$$

[15]

Furthermore, Eq. 3 and 8 each consumes Cl₂, generating the species of HCl and Cl, respectively. Here the HCl and Cl can serve as markers for the consumed Cl₂, which must be added to the \(p_{\text{Cl}_2}/2\) term in Eq. 15. From Eq. 3 we see that \(p_{\text{Cl}_2}=p_{\text{HCl}}/2\), and from Eq. 8 that \(p_{\text{Cl}_2}=p_{\text{Cl}}/2\). Taking all of these into account, yields the required equation, Eq. 13.

The equilibrium constants for the eight chemical reactions, Eq. 1-8, need also to be expressed in terms of the partial pressures of the species present in the system

$$
K_{1}=p_{\mathrm{Cl}_{2}}^{4} /\left(p_{\mathrm{TiCl}_{4}}^{2} \cdot p_{\mathrm{N}_{2}}\right)
$$

[16]

$$
K_{2}=p_{\mathrm{NH}_{3}}^{2} /\left(p_{\mathrm{N}_{2}} \cdot p_{\mathrm{H}_{2}}^{3}\right)
$$

[17]

$$
K_{3}=p_{\mathrm{HCl}}^{2} /\left(p_{\mathrm{H}_{2}} \cdot p_{\mathrm{Cl}_{2}}\right)
$$

[18]

$$
K_{4}=\left(p_{\mathrm{TiCl}_{3}}^{2} \cdot p_{\mathrm{Cl}_{2}}\right) / p_{\mathrm{TiCl}_{4}}^{2}
$$

[19]

$$
K_{5}=\left(p_{\mathrm{TiCl}_{2}} \cdot p_{\mathrm{Cl}_{2}}\right) / p_{\mathrm{TiCl}_{4}}
$$

[20]

$$
K_{6}=\left(p_{\mathrm{TiCl}}^{2} \cdot p_{\mathrm{Cl}_{2}}^{3}\right) / p_{\mathrm{TiCl}_{4}}^{2}
$$

[21]

$$
K_{7}=p_{\mathrm{H}}^{2} / p_{\mathrm{H}_{2}}
$$

[22]

$$
K_{8}=p_{\mathrm{Cl}}^{2} / p_{\mathrm{Cl}_{2}}
$$

[23]

The equilibrium constants for each reaction, \(K_i\), at temperature \(T(^\circ\text{K})\) is a function of the standard Gibbs free energy of the reaction, \(\Delta G_{\mathrm{i}}^{\circ}\), given in the following form

$$
K_{i}(T)=\exp \left[-\Delta G_{\mathrm{i}}^{\circ} / R T\right]
$$

[24]

where the free energy of each reaction is the difference between the sum of the free energies of formation of the products and the reactants. Applying Eq. 24 to Eq. 16-23, at unique temperatures, which make the system invariant, in conjunction with the specification of the system constraining equations, Eq. 11-13, enables solution for the partial pressures of the eleven vapor-phase species. Therefore, Eq. 11-13 and 16-23 form a set of nonlinear equations for solving the chemical system in question.

Instead of developing a computer program to solve this set of equations, we employed an existing computer program, SOLGASMIX, based on the free energy minimization method. The set of the first principles constraining equations and the equilibrium constant equations were then used as integrity checks of the SOLGASMIX outputs, as is described below. Any other suitable existing computer program could have been used along with the first principles integrity check.

SOLGASMIX program approach.—The SOLGASMIX computer program²² was developed by Eriksson²³,²⁴ for calculating multiphase chemical systems. It determines the equilibrium state of the system by minimizing its total Gibbs free energy. It, of course, assumes the employed data are accurate. SOLGASMIX has a direct interface to a thermodynamic database, the JANAF tables,²⁶ which contain tabulated data for various thermodynamic functions for a large number of chemical species.

The input data list to SOLGASMIX program consists of the chemical components present in the system, and the chemical species assumed to be derivable from these components. In addition, one needs to specify the total system pressure and temperature at which the equilibrium is assumed to obtain, and the temperature at which the reactants are introduced, as well as the relative molar amounts of the input chemicals.

For the Ti-N-H-Cl system, the calculations were conducted at total system pressures of 100 Torr, 500 mTorr, and 10 mTorr, within the temperature range of 273 to 1500 K. The four components were introduced in the form of the chemicals having the stoichiometries TiCl₄(v) and NH₃(v). The input ratios of TiCl₄/NH₃ were chosen as 1/2 and 1/ which correspond to the component N/Cl ratios of 1/2 and 5/4, at fixed input component N/H ratio of 1/3 and a fixed component input ratio (Ti/Cl)input of 1/4. It is noteworthy that, for simplicity, the components N and H were introduced as NH₃, and the components Ti and Cl were introduced as TiCl₄. In an easily reversible reaction this is equivalent to introducing H₂(v) and N₂(v) along with TiCl₄ in the appropriate ratios.

The outputs of the SOLGASMIX program include the Gibbs free energy, \(G(T)\), and the enthalpy change functions, \(H(T) - H(298)\), with their coefficients in power law form for each species in the system. The errors in the curve fits of these two functions (the difference between the original data and the values obtained via the use of the power law curves) are also among the outputs in the percentage form. The most important portion of the outputs, for our purpose, is the list of the equilibrium partial pressures at each temperature of interest. From this data, we can construct univariant solid-vapor solubility curve-phase diagrams, specified in terms of component ratios as a function of temperature with constrained pressure and input component ratio values. This approach is described below.

Integrity check.—To ensure that no mistake was made during the SOLGASMIX analyses, an internal consistency check was performed for each set of system conditions. It was found that a proper setup of the SOLGASMIX program enables reconstructing the first principles constraining values by inserting the program outputs, in terms of the species partial pressures, into the constraining and equilibrium equations. The accuracy of the derived data, of course, depends upon the accuracy of the data employed. As an integrity check for the present calculations, the SOLGASMIX partial pressure outputs were introduced into the set of the first principles constraining equations, Eq. 11-13, and the equilibrium constant equations, Eq. 16-23. As noted, if the SOLGASMIX analysis is correct, then the input values should be reproduced, i.e., Eq. 11 should give the input value of the total system pressure, Eq. 12 and 13 should give the input component ratios of H/Cl and (Ti/Cl)input, respectively, and Eq. 16-23 should reproduce the numerical values of the equilibrium constants obtained by applying Eq. 24 to the corresponding chemical reactions using the available thermodynamic data.

A detailed analysis of the boundary conditions for TiN deposition/etching processes requires a knowledge of the

solid-vapor solubility-phase diagrams, which can best be defined in terms of the output component partial pressure ratio, $(p_{\text{Ti}}/p_{\text{Cl}})_{\text{output}}$, or denoted as $(\text{Ti}/\text{Cl})_{\text{output}}$, as a function of temperature, as shown in Eq. 25

$$
\left(\frac{P_{\text{Ti}}}{P_{\text{Cl}}}\right)_{\text{output}} = \frac{p_{\text{TiCl}_4} + p_{\text{TiCl}_3} + p_{\text{TiCl}_2} + p_{\text{TiCl}}}{4p_{\text{TiCl}_4} + 3p_{\text{TiCl}_3} + 2p_{\text{TiCl}_2} + p_{\text{TiCl}} + p_{\text{HCl}} + 2p_{\text{Cl}_2} + p_{\text{Cl}}}
$$

[25]

The choice of this component ratio, as an indicator, is based on the consideration that in the present chemical system, the titanium can be either deposited or etched, while the chlorine always remains in the vapor phase. Therefore, it provides a simple way of assessing the deposition and/or etching behavior. Thus, if the solid-vapor solubility curves are available, when the Ti/Cl ratio increases from its input value of 0.25, titanium is being etched; when this ratio decreases, titanium is being deposited. In addition, by knowing the "mass" flow rate of the input component Cl, which can be derived from the $\text{TiCl}_4$ input flow, and knowing the $(\text{Ti}/\text{Cl})_{\text{output}}$ ratio as a function of temperature, the deposition/etching rate, in terms of moles per unit time, can be deduced, assuming, of course, the overall reactions are reversible in the temperature range of interest.

In the present analysis, the equilibrium $(\text{Ti}/\text{Cl})_{\text{output}}$ ratio was calculated for different $\text{TiCl}_4/\text{NH}_3$ ratios (1/2 and 1/5) for three total system pressures (100 Torr, 500 mTorr, and 10 mTorr). The 500 mTorr value probably is most applicable to an experimental CVD system. At each pressure, there exists two solid-vapor solubility curves, i.e., for $\text{TiCl}_4/\text{NH}_3$ input ratios of 1/2 and 1/5, from which titanium deposition/etching efficiencies can be deduced.

Results and discussion.—Figure 1 presents the solid-vapor solubility curve families in terms of the equilibrium output component vapor-phase ratio, $(\text{Ti}/\text{Cl})_{\text{output}}$, at the three pressures studied as a function of temperature. The two curves in each figure correspond to the input $\text{TiCl}_4/\text{NH}_3$ ratios of 1/2 and 1/5, which translates into input Cl/H component ratios of 2/3 and 4/15. Since the input titanium to chlorine ratio, $(\text{Ti}/\text{Cl})_{\text{output}}$, is 0.25, assuming that equilibrium obtains, when the equilibrium vapor-phase component ratio, $(\text{Ti}/\text{Cl})_{\text{output}}$, is greater than 0.25, this indicates that solid TiN is being etched, if it is less than 0.25, this indicates that TiN is being deposited, and when it is equal to 0.25, this indicates that neither deposition nor etching is taking place. From Fig. 1 one sees that TiN deposition should occur from 273 K up at all three system pressures and both input Cl/H ratios. It is seen that at a given total system pressure, the lower the input Cl/H ratio is, the greater is the expected deposition efficiency. For a fixed input $\text{TiCl}_4/\text{NH}_3$ or Cl/H ratio, the deposition efficiency increases with increasing temperature up to about 1273 K at the total pressure of 100 Torr, to about 1073 K at a total pressure of 500 mTorr, and about 973 K at a total pressure of 10 mTorr. At temperatures higher than these, the expected deposition efficiency decreases with temperature. By comparing Fig. 1a, b, and c, it can also be concluded that for a given Cl/H ratio, TiN deposition would be more efficient at the lower total system pressures, assuming constant mass input rates.

Figure 2 shows two graphs of equilibrium partial pressures of the eleven chemical species assumed present in the Ti-N-H-Cl system as a function of temperature at a total system pressure of 100 Torr. As in Fig. 1, Fig. 2a and b represent the two input $\text{TiCl}_4/\text{NH}_3$ ratios examined.

Similarly, Fig. 3a and b present equilibrium partial pressures at a total system pressure of 500 mTorr, and Fig. 4a and b depict the situation at 10 mTorr.

### TiN Etching Process in the Ti-N-Cl System

The study of the Ti-N-Cl system is aimed at analyzing the embedded disproportionation reaction for etching TiN spurious nuclei. This reaction is made dominant when the $\text{H}_2$ (or $\text{NH}_3$) flow is turned off during the A.C. cycle (or when this flow is reduced significantly). The analyses were conducted using the same approach as employed for the Ti-N-H-Cl system.

First principles approach.—The Ti-N-Cl system consists of three components, Ti, N, Cl, in two phases, solid and vapor. Seven vapor-phase species are assumed present in this system: $\text{TiCl}_4$, $\text{TiCl}_3$, $\text{TiCl}_2$, $\text{TiCl}$, $\text{N}_2$, $\text{Cl}_2$, and Cl. Again the nitrogen chlorides ($\text{NCl}$, $\text{NCl}_2$, $\text{NCl}_3$, and $\text{NCl}_5$) are neglected.

Using the Gibbs-phase rule, this system is seen to be trivariant. By fixing the total system pressure, $p_{\text{t}}$, and the input titanium to chlorine component ratio, $(\text{Ti}/\text{Cl})_{\text{input}}$, the system becomes univariant. When temperature is specified, the system is uniquely defined.

To solve for the partial pressures of the seven chemical species in the system, five additional equations representing five chemical equilibria are needed, which were chosen as Eq. 26-30

$$2\text{TiN(s)} + 6\text{TiCl}_4(\text{v}) = 8\text{TiCl}_3(\text{v}) + \text{N}_2(\text{v}) \tag{26}$$

$$2\text{TiCl}_4(\text{v}) = 2\text{TiCl}_3(\text{v}) + \text{Cl}_2(\text{v}) \tag{27}$$

$$2\text{TiCl}_3(\text{v}) = 2\text{TiCl}_2(\text{v}) + \text{Cl}_2(\text{v}) \tag{28}$$

$$2\text{TiCl}_2(\text{v}) = 2\text{TiCl}(\text{v}) + \text{Cl}_2(\text{v}) \tag{29}$$

$$\text{Cl}_2(\text{v}) = 2\text{Cl(v)} \tag{30}$$

Equation 26, obviously, represents the disproportionation reaction, from which it is seen that no additional reactant is required to etch the spurious TiN nuclei. This reaction is made dominant when either the hydrogen (in the hydrogen-nitrogen implementation), or ammonia flow is interrupted, leaving only a $\text{TiCl}_4$ (and $\text{N}_2$ in the hydrogen-nitrogen implementation) flow to cause TiN etching. It should be recognized that in practice one might not want to turn the flow off completely, but rather reduce this flow sufficiently so as to move the system into the etching regime. For the purposes of the present discussion, hydrogen flow, either in terms of stopping it completely, or stopping the $\text{NH}_3$ flow completely, were the boundary cases examined.

The two system constraints, i.e., the total system pressure and the input titanium to chlorine ratio are given in Eq. 31 and 32, respectively, in terms of the equilibrium partial pressures of the species in the system

$$p_{\text{t}} = p_{\text{TiCl}_4} + p_{\text{TiCl}_3} + p_{\text{TiCl}_2} + p_{\text{TiCl}} + p_{\text{N}_2} + p_{\text{Cl}_2} + p_{\text{Cl}} \tag{31}$$

$$\left(\frac{P_{\text{Ti}}}{P_{\text{Cl}}}\right) = \frac{p_{\text{TiCl}_4} + p_{\text{TiCl}_3} + p_{\text{TiCl}_2} + p_{\text{TiCl}} - 2p_{\text{N}_2}}{4p_{\text{TiCl}_4} + 3p_{\text{TiCl}_3} + 2p_{\text{TiCl}_2} + p_{\text{TiCl}} + 2p_{\text{Cl}_2} + p_{\text{Cl}}} = \frac{1}{4} \tag{32}$$

Equation 32, again, shows the conservation of the input titanium to chlorine ratio. This equation is obtained as follows. From Eq. 26, it is seen that if the solid-phase species, TiN, is etched, it contributes to the component Ti in vapor phase. For the experiment where deposition is affected using the $\text{TiCl}_4(\text{v}) + \text{NH}_3(\text{v})$ reaction, during the etching portion of the cycle when the ammonia is turned off, the vapor-phase species, $\text{N}_2$, serves as a good marker for etched TiN, since this species can be generated only via the etching of the solid TiN. From Eq. 26, it is seen that as the species ratio, $\text{TiN(s)}/\text{N}_2(\text{v}) = 2/1$, i.e., $\text{TiN} = 2\text{N}_2$, hence, $2p_{\text{N}_2}$ must be subtracted from the $\sum p_{\text{Ti}_x\text{Cl}_y}$ to conserve the input ratio $(p_{\text{Ti}}/p_{\text{Cl}})_{\text{input}} = 0.25$.

The equilibrium constants of the chemical reactions, given in Eq. 26-30, can be derived in terms of the partial pressures of the chemical species involved, and are presented in Eq. 33-37

$$K_1 = (p_{\text{TiCl}_3}^8 \cdot p_{\text{N}_2})/p_{\text{TiCl}_4}^6 \tag{33}$$

$$K_2 = (p_{\text{TiCl}_3}^2 \cdot p_{\text{Cl}_2})/p_{\text{TiCl}_4}^2 \tag{34}$$

$$K_3 = (p_{\text{TiCl}_2}^2 \cdot p_{\text{Cl}_2})/p_{\text{TiCl}_3}^2 \tag{35}$$

$$K_4 = (p_{\text{TiCl}}^2 \cdot p_{\text{Cl}_2})/p_{\text{TiCl}_2}^2 \tag{36}$$

$$K_5 = p_{\text{Cl}}^2/p_{\text{Cl}_2} \tag{37}$$

Thus, a new set of nonlinear equations is formed, including Eq. 33-37 and Eq. 31-32, with the equilibrium partial pressures for the seven species as unknowns. The SOL-GASMIX computer program was used to perform the calculations based on the free energy minimization algorithm as before.

# Ti/Cl Component Gas Phase Ratios As a Function of Temperature for the Reaction of TiCl₄ with NH₃

![](./images/812079858753470464_1.jpg)

## Species Gas Phase Partial Pressures in the Ti-H-N-Cl System at 100torr for Different TiCl₄/NH₃ Input Ratios

![](./images/812079858753470464_2.jpg)

SOLGASMIX program approach.—The SOLGASMIX program, which has been described in section on TiN Deposition Process in the Ti-N-H-Cl System, was employed for the analysis of the Ti-N-Cl system at total system pressures of 100 Torr, 500 mTorr, and 10 mTorr, and in the temperature range, 500 to 1500 K. The lower temperature boundary chosen was slightly higher than that for the Ti-N-H-Cl system, because nothing much happens below 500 K in the etching system.

Based on the disproportionation reaction, depicted by Eq. 26, the input reactants to the SOLGASMIX program are TiCl₄ and solid TiN. The ratios of the molar amounts of these two chemicals were chosen as 3/1 and 3/3, such that TiN cannot be totally consumed during the etching process by the input amount of TiCl₄. It turns out that, as could have been anticipated, if all other conditions are identical,

# Species Gas Phase Partial Pressures in the Ti-H-N-Cl System at 500mtorr for Different $\text{TiCl}_4$/$\text{NH}_3$ Input Ratios

![](./images/812079858753470464_3.jpg)

**Fig. 3. Equilibrium partial pressures of vapor phase species vs. temperature for TiN deposition from $\text{TiCl}_4$ at a total system pressure of 500 mTorr with input molar ratios of (a, left) $\text{TiCl}_4$/$\text{NH}_3 = 1/2$; (b, right) $\text{TiCl}_4$/$\text{NH}_3 = 1/5$.**

# Species Gas Phase Partial Pressures in the Ti-H-N-Cl System at 10mtorr for Different $\text{TiCl}_4$/$\text{NH}_3$ Input Ratios

![](./images/812079858753470464_4.jpg)

**Fig. 4. Equilibrium partial pressures of vapor phase species vs. temperature for TiN deposition from $\text{TiCl}_4$ at a total system pressure of 10 mTorr with input molar ratios of (a, left) $\text{TiCl}_4$/$\text{NH}_3 = 1/2$; (b, right) $\text{TiCl}_4$/$\text{NH}_3 = 1/5$.**

these two ratios gave the same outputs of the SOLGASMIX program, which will be presented below.

Integrity check.—With the outputs of the SOLGASMIX program as the input data to the first principles constraining equations, an integrity check was conducted. Thus, using the species partial pressures given by the SOLGASMIX program, the input values for the total system pressure and the titanium to chlorine ratio were reproduced by Eq. 31 and 32, respectively, and the equilibrium constants for the five reactions involved were regenerated by Eq. 33-37.

In a similar fashion to the analysis for the TiN deposition process in the Ti-N-H-Cl system, solid-vapor solubility curves, in the form of titanium to chlorine component output partial pressures ratios given in Eq. 38, were calculated

and plotted as a function of temperature for the present system

$$
\left(\frac{P_{\mathrm{Ti}}}{P_{\mathrm{Cl}}}\right)_{\text {output }}=\frac{p_{\mathrm{TiCl}_{4}}+p_{\mathrm{TiCl}_{3}}+p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}}{4 p_{\mathrm{TiCl}_{4}}+3 p_{\mathrm{TiCl}_{3}}+2 p_{\mathrm{TiCl}_{2}}+p_{\mathrm{TiCl}}+2 p_{\mathrm{Cl}_{2}}+p_{\mathrm{Cl}}} \quad[38]
$$

The titanium to chlorine ratio would exceed its input value of 0.25, if etching of TiN occurs. For a given total system pressure, there exists only one solubility curve, instead of a family of curves, since the system is univariant if the total pressure and $(\mathrm{Ti} / \mathrm{Cl})_{\text {input }}$ are specified. From the solubility curve, the TiN etching rate can be evaluated for a given $\mathrm{TiCl}_{4}$ flow rate at the temperature of interest.

Results and discussion.-Three etching curves are presented in Fig. 5 representing the solid-vapor solubility curves as a function of temperature at total system pressures of 100 Torr, 500 mTorr, and 10 mTorr, respectively. In each case, the two input ratios of the molar amount of solid TiN to the amount of $\mathrm{TiCl}_{4}, 3 / 3$ and $1 / 3$, gave identical solubility curves in the isobarically, isoplethally constrained system. For such cases where excess TiN is assumed present, its quantity has no effect on the calculation results. As shown in Fig. 5, the component vapor-phase ratio, $(\mathrm{Ti} / \mathrm{Cl})_{\text {output }}$, exceeds its starting value of 0.25 above $900 \mathrm{~K}$ at a total system pressure of 100 Torr, above $800 \mathrm{~K}$ at $500 \mathrm{mTorr}$, and above $700 \mathrm{~K}$ at $10 \mathrm{mTorr}$. This indicates that TiN etching would occur in these temperature ranges. The curves in Fig. 5a, b, and c indicate that the etching efficiency increases with increasing temperature, and at a given temperature, lower total system pressure favors the etching process.

Figure 6 presents the equilibrium partial pressures of the seven vapor-phase species in the Ti-N-Cl system as a function of temperature at total system pressures of 100 Torr, $500 \mathrm{mTorr}$, and $10 \mathrm{mTorr}$, respectively. Again, the different amounts of input solid TiN have no effect on the species partial pressures.

## The Alternating Cycle Process for Selective Deposition of TiN

The thermodynamic analyses for the Ti-N-H-Cl and Ti$\mathrm{N}-\mathrm{Cl}$ systems in the preceding sections show that using a $\mathrm{TiCl}_{4}$ source with the addition of a reducing gas, $\mathrm{H}_{2}$ (in the presence of $\mathrm{N}_{2}$ ), or $\mathrm{NH}_{3}$, solid TiN can be deposited at reasonable temperatures, while when the $\mathrm{TiCl}_{4}$ alone is passed over solid TiN, the latter is etched. Taken in combination, these two results indicate that it is possible to use $\mathrm{TiCl}_{4}$ as a source for both deposition and etching of TiN, which indicates that an A.C. process for the selective deposition of TiN is feasible. The way to implement the A.C. process is to interrupt the $\mathrm{H}_{2}$ (or $\mathrm{NH}_{3}$ ) flow in a cyclic fashion. When $\mathrm{H}_{2}$ (or $\mathrm{NH}_{3}$ ) flow is on, the hydrogen reduction reaction becomes dominant, and TiN is deposited; when $\mathrm{H}_{2}$ (or $\mathrm{NH}_{3}$ ) is turned off, the embedded disproportionation reaction dominates, resulting in TiN etching. Thus, if experimental conditions are properly chosen, by pulsing the hydrogen (or ammonia) on and off while maintaining a continuous flow of $\mathrm{TiCl}_{4}$, the hydrogen reduction reaction and the disproportionation reaction are made dominant alternatively. In the etching part of the cycle, spurious nuclei of TiN should be etched preferentially from the unwanted areas due to their higher surface energy and larger degree of exposure to the etching vapor, when compared with continuous films in the desired areas.

As an example, Fig. 7 depicts a combination of the deposition and etching processes for a complete cycle in the A.C. sequence involving $\mathrm{TiCl}_{4}$ and $\mathrm{NH}_{3}$. Figure 7 presents the $\mathrm{Ti} / \mathrm{Cl}$ vapor-phase ratio as a function of temperature at a total system pressure of $10 \mathrm{mTorr}$. The bottom curve represents deposition of TiN for a $\mathrm{TiCl}_{4} / \mathrm{NH}_{3}$ input ratio of $1 / 5$. The top curve represents etching of TiN when $\mathrm{NH}_{3}$ is turned off. The dotted horizontal line depicts the input $\mathrm{Ti} / \mathrm{Cl}$ ratio of 0.25, which divides the graphs into two regions, etching and deposition. Neglecting kinetic or mass transport limitations, the deposition/etching rate, in grams per unit time, can be calculated from these curves. For example, assuming a $\mathrm{TiCl}_{4}$ flow rate, $F R_{\mathrm{TiCl}_{4}}$, of $100 \mathrm{sccm}$, and an $\mathrm{NH}_{3}$ flow rate of $500 \mathrm{sccm}$ for deposition, and of zero for etching, at a temperature of $973 \mathrm{~K}$, the equilibrium $\mathrm{Ti} / \mathrm{Cl}$ ratios at points A and B in Fig. 7, 0.259 and 0.003, determine the etching and deposition rates, $D R_{\text {etch }}$ and $D R_{\text {dep }}$, as calculated in Eq. 39 and 40, respectively

$$
\begin{aligned}
& D R_{\text {etch }}=\left[(\mathrm{Ti} / \mathrm{Cl})_{\text {output }}-(\mathrm{Ti} / \mathrm{Cl})_{\text {input }_{\text {etch }}} \cdot M W_{\mathrm{TiN}}\right. \\
& \cdot 4 F R_{\mathrm{TiCl}_{4}} /\left(22,400 \mathrm{~cm}^{3} / \mathrm{mol}\right)=(0.259-0.25) \cdot(61.89 \mathrm{~g} / \mathrm{mol}) \\
& \times 4\left(100 \mathrm{~cm}^{3} / \mathrm{min}\right) /\left(22,400 \mathrm{~cm}^{3} / \mathrm{mol}\right)=0.00995 \mathrm{~g} / \mathrm{min} \quad[39] \\
& D R_{\text {dep }}=\left[(\mathrm{Ti} / \mathrm{Cl})_{\text {input }}-(\mathrm{Ti} / \mathrm{Cl})_{\text {output }_{\text {dep }}} \cdot M W_{\mathrm{TiN}}\right. \\
& \cdot 4 F R_{\mathrm{TiCl}_{4}} /\left(22,400 \mathrm{~cm}^{3} / \mathrm{mol}\right)=(0.25-0.003) \cdot(61.89 \mathrm{~g} / \mathrm{mol}) \\
& \cdot 4\left(100 \mathrm{~cm}^{3} / \mathrm{min}\right) /\left(22,400 \mathrm{~cm}^{3} / \mathrm{mol}\right)=0.273 \mathrm{~g} / \mathrm{min} \quad[40]
\end{aligned}
$$

where $(\mathrm{Ti} / \mathrm{Cl})_{\text {output }}$ can be read directly from the equilibrium diagram, Fig. 7, the molecular weight of TiN, $M W_{\mathrm{TiN}}$, is $61.89 \mathrm{~g} / \mathrm{mol}$, and the factor 4 is used to convert the input $\mathrm{TiCl}_{4}$ flow rate into the units of the volume of the component $\mathrm{Cl}$ introduced per unit time.

Similarly, the etching and deposition rates at $1173 \mathrm{~K}$, represented by points $\mathrm{C}$ and $\mathrm{D}$, can be calculated to be $0.271 \mathrm{~g} / \mathrm{min}$ and $0.0508 \mathrm{~g} / \mathrm{min}$, respectively. The growth rate in thickness per unit time can also be determined by assuming a uniform deposition over a specific area.

It can be seen from Fig. 7 that the transition between etching and deposition occurs by merely turning on and off the input flow of $\mathrm{NH}_{3}$. At $973 \mathrm{~K}\left(700^{\circ} \mathrm{C}\right)$, the A.C. process requires alternating between point A (etching $0.01 \mathrm{~g} / \mathrm{min}$ ) when $\mathrm{NH}_{3}$ is off, and B (depositing $0.27 \mathrm{~g} / \mathrm{min}$ ) when $\mathrm{NH}_{3}$ is on. Alternating between $\mathrm{C}$ and $\mathrm{D}$ at $1173 \mathrm{~K}\left(900^{\circ} \mathrm{C}\right)$, obviously will increase the amount of TiN removed $(0.05 \mathrm{~g} / \mathrm{min}$ at $\mathrm{C}$ ) during each cycle, which would be advantageous when more etching is required to maintain selectivity. It is left for experimental work to precisely determine the amount of TiN that can be deposited and/or etched during each A.C. cycle, and the time duration of each portion of a cycle.

Figure 8 depicts the A.C. process for selective deposition of TiN at a total system pressure of $500 \mathrm{mTorr}$, which as indicated is a likely CVD pressure, for a range of input $\mathrm{H} / \mathrm{Cl}$ ratios. The etching portion of the A.C. cycle is represented by the top solid-vapor solubility curve, which corresponds to the case when the $\mathrm{NH}_{3}$ flow is interrupted. Notice also that in the $\mathrm{H} / \mathrm{Cl}=0.075$ curve, an etching region also exists, so that one need not completely turn off a hydrogen or ammonia flow to achieve etching, if the experiment is implemented using either the $\mathrm{TiCl}_{4}+\mathrm{H}_{2}+\mathrm{N}_{2}$, or the $\mathrm{TiCl}_{4}+$ $\mathrm{NH}_{3}$ reaction. The deposition portion of the cycle, is shown by five curves, each of them corresponding to a different input $\mathrm{NH}_{3} / \mathrm{TiCl}_{4}$ value. It is obvious that at a given total system pressure and temperature, if the $\mathrm{TiCl}_{4}$ flow is kept constant, the higher the $\mathrm{NH}_{3}$ flow is, the greater is the deposition efficiency.

## Conclusions

Thermodynamic calculations for the selective area CVD of titanium nitride via an A.C. process have been conducted using both a first principles approach and a SOLGASMIX computer program approach. The former gives an entire analysis of the appropriate species, variables, and chemical reactions involved in the system at each equilibrium condition of interest; the latter directly determines the equilibrium composition by minimizing the system's free energy. The integrity of the SOLGASMIX analysis was verified by checking the consistency of the two approaches. The results of the calculations have been depicted in the form of solid-vapor solubility curves plotted as a function of temperature. The thermodynamic feasibility of the A.C. technique for the selective deposition of titanium nitride has been analyzed, and it has been shown to be thermodynamically possible to remove spurious nuclei of TiN by employing an embedded disproportionation chemistry. The removal of spurious nuclei in unwanted areas can be realized by cyclically interrupting hydrogen or ammonia gas flow during the sequential deposition process. This A.C. approach is expected to be general and applicable to deposition of a wide variety of other materials in semiconductor processes.

# Ti/Cl Component Gas Phase Ratios As a Function of Temperature
for the Etching of TiN by $TiCl_4$

![](./images/812079858753470464_5.jpg)

Fig. 5. Equilibrium solid-vapor solubility curves for TiN etching by $TiCl_4$ at total system pressures of (a, left) 100 Torr, (b, center) 500 mTorr, (c, right) 10 mTorr.

# Species Gas Phase Partial Pressures in the Ti-N-Cl System
at Different System Total Pressures

![](./images/812079858753470464_6.jpg)

Fig. 6. Equilibrium partial pressures of vapor phase species vs. temperature for TiN etching by $TiCl_4$ at total system pressures of (a, left) 100 Torr, (b, center) 500 mTorr, (c, right) 10 mTorr.

AC Process for the Selective Deposition of TiN

![](./images/812079858753470464_7.jpg)

Fig. 7. Equilibrium solid-vapor solubility curves for the A.C. process of the selective deposition of TiN at a total system pressure of 10 mTorr.

AC Process for the Selective Deposition of TIN from TICI4
(Ptot=500mtorr)

![](./images/812079858753470464_8.jpg)

Fig. 8. Equilibrium solid-vapor solubility curve families for the A.C. process of the selective deposition of TiN at a total system pressure of 500 mTorr for different input $\mathrm{NH}_{3} / \mathrm{TiCl}_{4}$ ratios.

### Acknowledgments

Manuscript submitted Aug. 23, 1993; revised manuscript received Nov. 22, 1993.

MCNC assisted in meeting the publication costs of this article.

### REFERENCES

1. S. M. Sze, *VLSI Technology*, 2nd ed., McGraw-Hill, New York (1988).
2. T. Takahashi and H. Itoh, *This Journal*, **124**, 797 (1977).
3. T. C. Jung, D. Y. Sheng, and M. H. Fang, in *Chemical Vapor Deposition (CVD-10)*, G. W. Cullen, Editor in Chief, p. 81, The Electrochemical Society Proceedings Series, Pennington, NJ (1987).
4. F. Pintchovski, T. White, E. Travis, P. T. Tobin, and J. B. Price, in *Tungsten and Other Refractory Materials for VLSI Applications-IV*, R. S. Blewer and C. M. McConica, Editors, pp. 275-282, Material Research Society, Pittsburgh, PA (1989).
5. A. Sherman, *ibid.*, pp. 323-329.
6. N. Yokoyama, K. Hinode, and Y. Homma, *This Journal*, **136**, 882 (1989).
7. N. Nakanishi, S. Mori, and E. Kato, *ibid.*, **137**, 322 (1990).
8. A. Sherman, *ibid.*, **137**, 1892 (1990).
9. A. Sherman and I. J. Raaijmakers, in *Chemical Vapor Deposition-1990 (CVD-11)*, K. E. Spear and G. W. Cullen, Editors, The Electrochemical Society Proceedings Series, Pennington, NJ (1990).
10. D. G. Bhat, *ibid.*, p. 648.
11. M. S. You, N. Nakanishi, and E. Kato, *ibid.*, p. 670.
12. E. O. Travis, W. M. Paulson, F. Pintchovski, B. Boeck, L. C. Parrillo, M. L. Kottke, K. Y. Fu, M. J. Rice, J. B. Price, and E. C. Eichman, *IEDM Tech. Dig.*, p. 47 (1990).
13. M. J. Buiting and A. H. Reader, *Mater. Res. Soc. Symp. Proc.*, **168**, 199 (1990).
14. N. Yokoyama, K. Hinode, and Y. Homma, *This Journal*, **138**, 190 (1991).
15. M. J. Buiting, A. F. Otterloo, and A. H. Montree, *ibid.*, **138**, 500 (1991).
16. A. Reisman, D. R. Shin, and G. W. Jones, *ibid.*, **137**, 722 (1990).
17. A. Reisman, A. Kepton, G. W. Jones, and R. Hogle, in *Tungsten and Other Refractory Metals for ULSI Applications-VI*, G. C. Smith and R. Blumenthal, Editors, p. 105, Materials Research Society, Pittsburgh, PA (1991).
18. J. Murota, N. Nakamura, M. Kato, and N. Mikoshiba, *Appl. Phys. Lett.*, **54**, 1007 (1989).
19. M. Kato, M-L. Cheng, C. Iwasaki, J. Murota, N. Mikoshiba, and S. Ono, Abstract 554, p. 796, The Electrochemical Society Extended Abstracts, Vol. 90-2, Seattle, WA, Meeting, Oct. 14-19, 1990.
20. G. J. Parker, J. M. Bonar, and C. M. Starbuck, *Electron. Lett.*, **27**, 1595 (1991).
21. Q. S. Wang, A. Reisman, and D. Temple, *This Journal*, **141**, 593 (1994).
22. J. A. Peters, The Pennsylvania State University Technical Report, No. TR88-008 (1988).
23. G. Eriksson, *Chem. Scripta*, **8**, 100 (1975).
24. G. Eriksson, *ACTA Chem. Scand.*, **25**, 2651 (1971).
25. A. Reisman and S. A. Alyanakyan, *This Journal*, **111**, 1154 (1964).
26. JANAF Thermochemical Tables, 3 ed., National Bureau of Standards, Washington, DC (1985); *J. Phys. Chem. Ref. Data*, **14**, Suppl. 1 (1985).