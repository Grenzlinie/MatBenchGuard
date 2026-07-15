# An exponential expression for gas heat capacity, enthalpy, and entropy

Charles Bruel *, François-Xavier Chiron $^1$, Jason R. Tavares, Gregory S. Patience *

Department of Chemical Engineering, École Polytechnique de Montréal, 2900 boul. Édouard-Montpetit, Montréal, QC H3T 1J4, Canada

---

## ARTICLE INFO

**Article history:**
Received 22 January 2016
Received in revised form 8 June 2016
Accepted 10 June 2016
Available online 11 June 2016

**Keywords:**
Heat capacity
Enthalpy
Entropy
High temperature
Adiabatic flames
Plasma

---

## ABSTRACT

Gas heat capacity, $C_P$, is a fundamental extensive thermodynamic property depending on molecular transitional, vibrational and rotational energy. Empirical four-parameter polynomials approximate the sigmoidal $C_P$ trends for temperatures up to 1500 K and adding parameters extends the range. However, the fitted parameters have no physical significance and diverge beyond their range at high temperature. Here we propose an exponential expression for $C_P$ whose fitted parameters relate to the shape of the $C_P$ versus $T$ curve and to molecular properties: $C_P = C_P^0 + C_P^\infty[1 + \ln(\underline{T})(1 + T_i/T)] \exp(-T_i/T)$. It accounts for more than 99% of the variance with a deviation of ~1% from 298 K to 6000 K for linear $C_1$–$C_7$ hydrocarbons and $N_2$, $H_2O$, $O_2$, $C_2H_4$, $H_2$, $CO$, and $CO_2$. We also provide an integrated form for enthalpy and an approximation to calculate entropy variations. This model replaces empirical polynomials with an expression whose constants are meaningful.

© 2016 Elsevier Inc. All rights reserved.

---

### 1. Introduction

Heat capacity ($C_P$) is a critical property in thermodynamics spanning diverse fields related to states and phase transitions [1,2], heat transfer [3], spin measurements [4,5] or materials characterization [6,7]. The Dulong-Petit law [8] accounts for heat capacity of metals. Neglecting vibrational and rotational energies, heat capacity for ideal monoatomic gases is related to translational kinetic energy only [9] (3 degrees of freedom) and the molar isobaric heat capacities are thus equal to 5/2 R. Theories for polyatomic gases poorly accounts for the variation of isobaric heat capacity with temperature. Textbooks [10,11] and specialized literature [12] report polynomial expressions that depend uniquely on the temperature ($T$). However, these expressions are valid over limited temperature ranges and deviate considerably for plasma applications [13] and adiabatic flames that can exceed 5000 K [14] (Fig. 1). NASA proposed a two range 5-term polynomial model [12] (200–1000 K and 1000–6000 K) to address the high temperature limitations (a total of 10 fitted parameters).

Our model characterizes $C_P$ at very high temperatures whereas standard polynomials deviate beyond the specified temperature ranges (Reid et al. [10] and Yaws et al. [11]). The NASA 5-parameter model [12] deviates much less from the experimental $C_P$ than the other polynomial models.

Models that approximate thermodynamic properties must meet several criteria [15,16]: all predicted values should be physically valid, and accurate over a wide range (~1% average absolute deviation, AAD), the function should be integratable (to calculate changes in enthalpy, $\Delta H$ and entropy, $\Delta S$), parsimonious (minimum number of parameters), and suitable for extrapolation. Among the non-polynomial models [17–19], Yuan and Mok [20] (1968) proposed a 4-parameter exponential expression:

$$
C_{P}(T)=A+B \exp \left(-\frac{C}{T^{n}}\right) \tag{1}
$$

It fits polyatomic experimental data better than 5-parameter polynomials but relies on the exponential integral (Ei) to account

---

**Abbreviations:** $\Delta G$, Gibbs free energy variation (J mol⁻¹); $\Delta H$, enthalpy variation (J mol⁻¹); $\Delta S$, entropy variation (J mol⁻¹ K⁻¹); $\varepsilon$, empirical coefficient defined in Eq. (8); $a, b$, empirical coefficients defined in Eq. (3) (J mol⁻¹ K⁻¹); $A, B, C, n$, empirical coefficients defined in Eq. (1); $A_0, B_1, C_1, n_1, B_2, C_2, n_2$, empirical coefficients defined in Eq. (2); AAD, Absolute Average Deviation (%); $C_P$, heat capacity (J mol⁻¹ K⁻¹); $C_P^0$, empirical coefficient defined in Eq. (5) (J mol⁻¹ K⁻¹); $C_P^\infty$, empirical coefficient defined in Eq. (5) (J mol⁻¹ K⁻¹); $D$, deviance, sum of the squared differences between predicted and experimental values; $\text{Dev}_i$, deviation (%) between the $i$th experimental value and the $i$th predicted value; Ei, exponential integral; $f, f_i, y_i, n$, parameters defined in Eq. (7); $n_A$, number of atoms in a molecule; $R$, gas constant; $R^2$, correlation coefficient; $\text{Res}_i$, residue of the fitting for the $i$th experimental value; $S, S^*$, entropy (J mol⁻¹ K⁻¹); $S_0$, empirical coefficient defined in Eq. (11) (J mol⁻¹ K⁻¹); $S_0^*$, empirical coefficient defined in Eq. (13) (J mol⁻¹ K⁻¹); $T$, temperature (K); $\underline{T}$, dimensionless temperature expressed in Kelvin, $\underline{T}=T/(1\ \text{K})$; $T_i$, empirical coefficient linked with $T_{\text{inflection}}$ and defined in Eqs. (3)–(5) (K); $T_{\text{inflection}}$, temperature of inflection of the $C_P$ curve's model (K).

* Corresponding authors.
E-mail addresses: charles.bruel@polymtl.ca (C. Bruel), gregory-s.patience@polymtl.ca (G.S. Patience).
$^1$ Present address: Haldor Topsoe A/S, Haldor Topsoes Alle 1, DK-2800 Kgs. Lyngby, Lyngby, Denmark.

http://dx.doi.org/10.1016/j.expthermflusci.2016.06.008
0894-1777/© 2016 Elsevier Inc. All rights reserved.

![](./images/814511362364407810_1.jpg)
![](./images/814511362364407810_2.jpg)
![](./images/814511362364407810_3.jpg)

![](./images/814511362364407810_4.jpg)

Fig. 1. Experimental methane heat capacity compared to model predictions from 298 K to 6000 K.

for $\Delta H$ and $\Delta S$ as a function of the temperature. The model accounts for over 99.5% of the experimental $C_P$, even up to 6000 K (SI Table 1) but it tends toward a finite asymptote while the experimental values continue to increase. Furthermore, there is no coherent relationship between the 4 constants and molecular properties. Thinh et al. [21] expanded the exponential model to a 7-parameter group additive correlation:

$$
C_{P}^{*}(T)=A_{0}+B_{1} \exp \left(-\frac{C_{1}}{T^{n_{1}}}\right)-B_{2} \exp \left(-\frac{C_{2}}{T^{n_{2}}}\right) \tag{2}
$$

The number of parameters increases with the complexity of the molecule and can reach dozens of terms. Group additive correlations are often the most accurate [10,22] but also the most complex to handle [21,23-25]. Thinh et al. further developed additive models to calculate enthalpy, entropy and Gibbs free energy [26,27]. These correlations are accurate but cumbersome to implement because of the large number of parameters (not parsimonious). They are necessary for applications for which experimental heat capacity is nonexistent, sparse (as for polycyclic aromatic hydrocarbons) or for computed assisted engineering and modeling. (The thermodynamic package Factsage™ relies on up to 16 parameters to approximate gas $C_P$ between 298.15 K and 6000 K). Textbooks and handbooks [10,11] thus still report 4 to 5-term polynomials applicable over a narrower temperature-range that have no physical meaning.

## 2. Mathematical formulation of the $C_P$ model

To reduce the empiricism of the polynomial models and account for the increase in $C_P$ above 3000 K, we modified the Yuan and Mok model with an expression that, contrary to Thinh et al. correlations, maintains its simplicity and can be integrated to calculate $\Delta H$.

We fit Eq. (1) to the $C_P$ of linear hydrocarbons ($C_1$-$C_7$), $O_2$, $H_2O$, $H_2$, $CO_2$, $CO$, $N_2$, and ethylene (gas). All data we retrieved from the literature [28-30] and are either purely experimental [28,30] or interpolated [29]. With an exponential value of $n=1$, we accounted for more than 99.6% of the variance in the data, which is as good as the fitting reported by Yuan and Mok [20]. Consequently, we integrated these expressions numerically to generate enthalpy as a function of temperature and fit the enthalpy with

$$
H^{*}(T)=a\ T+b\ T \ln(\underline{T}) \exp(-T_i/T) \tag{3}
$$

This expression accounts for more than 99% of the variance in the integrated $C_P$ where $a$, $b$ and $T_i$ are fitted parameters. Differentiating $H^*(T)$ gives:

$$
C_{P}(T)=\frac{\mathrm{d} H^{*}}{\mathrm{~d} T}=a+b\left[1+\ln(\underline{T})\left(1+\frac{T_{i}}{T}\right)\right] \exp \left(-\frac{T_{i}}{T}\right) \tag{4}
$$

where the upper and lower bounds are $\lim_{T \to 0K} C_P(T)=a=C_P^0$ and $\lim_{T \to \infty K} C_P(T)=\lim_{T \to \infty K} b\ln(\underline{T})=\lim_{T \to \infty K} C_P^\infty \ln(\underline{T})=+\infty$. Physically, the parameters $C_P^0$ (= a) and $C_P^\infty$ (= b), both in $\mathrm{J} \mathrm{mol}^{-1} \mathrm{~K}^{-1}$, are thus respectively the limit of $C_P$ at low temperature and the growing rate of $C_P$ at high temperature, while $T_i$, in K, is a temperature related with the inflection point of the sigmoid and thus with the transition between low and high $C_P$ values. The inflection of a curve is mathematically defined as the point where the second derivative is null while its third derivative is different than zero. It happens for the $C_P$ model in $T_{\text{inflection}}=T_i\ (0.353+0.234/T_i^{0.384})$ where $T_{\text{inflection}}$ and $T_i$ are both in K ($R^2$ 0.999). This expression comes from the resolution of the non-linear equation $(d^2C_P/dT^2)$= 0 (Fig. 2).

Replacing $a$ and $b$ with these limiting factors gives:

$$
C_{P}(T)=C_{P}^{0}+C_{P}^{\infty}\left[1+\ln(\underline{T})\left(1+\frac{T_{i}}{T}\right)\right] \exp \left(-\frac{T_{i}}{T}\right) \tag{5}
$$

$$
\Delta H_{T_{1} \rightarrow T_{2}}=\left[C_{P}^{0} T+C_{P}^{\infty} T \ln(\underline{T}) \exp \left(-\frac{T_{i}}{T}\right)\right]_{T_{1}}^{T_{2}} \tag{6}
$$

## 3. Methods

Models were fitted to experimental data based on a Marquardt-Levenberg algorithm [31] to minimize the sum of the squared differences (deviance D) between the experimental data and the predicted values:

$$
D=\sum_{i=1}^{n}\left(f_{i}-y_{i}\right)^{2} \tag{7}
$$

where $n$ and $y_i$ are the number and the values of experimental data and $f_i$ values predicted by the model.

$$
\operatorname{Res}_{i}=f_{i}-y_{i} \tag{8}
$$

The deviation $\operatorname{Dev}_{i}$ between a prediction and an experimental value, in %, is calculated from the residues $\operatorname{Res}_{i}$:

$$
\operatorname{Dev}_{i}=100 \operatorname{Res}_{i} / y_{i}=100\left(f_{i}-y_{i}\right) / y_{i} \tag{9}
$$

The average absolute deviation, AAD, is the average of the absolute values of $\operatorname{Dev}_{i}$, it is a measure of the average deviation a user can expect from the fitted expression:

![](./images/814511362364407810_5.jpg)

Fig. 2. Methane model parameters deduced from experimental data: $C_P^0 \sim 8/2$ R, $C_P^\infty$ accounts for the growing rate of $C_P$ at high temperature, and $T_i$ relates to the inflection point of the curve $T_{\text{inflection}}$.

![](./images/814511362364407810_6.jpg)
![](./images/814511362364407810_7.jpg)

Fig. 3. Model predictions compared to the experimental $C_{P}$: a and b, the model accounts for 99% of the variance in the for linear hydrocarbons (C₁-C₇) and common gases (O₂, H₂O, CO₂, N₂, CO, H₂).

$$
A A D=\sum_{i=1}^{n}\left|\frac{D e v_{i}}{n}\right|=\frac{100}{n} \sum_{i=1}^{n} \frac{\left|f_{i}-y_{i}\right|}{\left|y_{i}\right|} \tag{10}
$$

## 4. Results and discussion
The model (Eq. (5)) fits common gases (methane, dioxygen, nitrogen) from 298 K to 6000 K with a correlation coefficient $R^{2}>0.99$ (Fig. 3a & b and SI Table 2). It fits C₃-C₇ linear hydrocarbons between 298 K and 1500 K and up to 3000 K for ethane equally well. Our model accounts for the experimental data equally as well as the 5-parameter polynomial model - AAD is mostly below 1% (SI Table 1, Fig. 4 and SI Figure 7 & 8). The Yuan and Mok [20] model accounts for the variance in the data slightly better than our exponential model but it has an additional fitted parameter. Moreover, its fitted parameters are not related to any molecular properties, whereas in Eq. (5) they can be linked with the number of atoms in the molecule, $n_{A}$, and with its number of freedom degrees. Indeed, the coefficient $C_{P}{ }^{\infty}$ increases linearly with $n_{A}$: $C_{P}{ }^{\infty}=-2.78+2.22 \quad n_{A}\left(R^{2}=0.999\right)$ (Fig. 5a). For noble gases (monoatomic gases, $n_{A}=1$ ), $T_{i}$ is infinite, thus $C_{P}{ }^{0} \approx C_{P}{ }^{\infty}$ remains constant with $T$, which is the expected result for monoatomic gases. Similarly, $C_{P}{ }^{0}$ and $T_{i}$ vary linearly with $n_{A}$ for linear hydrocarbons (C₂-C₇): $C_{P}{ }^{0}=0.33+5.18 \quad n_{A}\left(R^{2}=0.993\right)$ and $T_{i}=1132.2-7.3 \quad n_{A}$ (R²=0.965) (Fig. 5a & b).

![](./images/814511362364407810_8.jpg)

Fig. 4. Average AAD for CH₄, O₂, H₂O, CO, CO₂, N₂, H₂ and C₂H₄ between 298 K and 6000 K for the exponential models (Eq. (5) and Yuan and Mok [20]), and polynomial models. Vertical bars represent the standard deviation of the AAD. Our model is significantly better than 4-parameter polynomials and is equivalent to the 5-parameter polynomial model.

The coefficients $C_{P}{ }^{0}$ and $T_{i}$ of methane are closer to the other common gases, which is reasonable since its physico-chemical properties are distinct from the linear hydrocarbons. Furthermore, the best fit values of $C_{P}{ }^{0}$ for diatomic gases - O₂, N₂, CO and H₂ - are within 2% of the theoretical value for ideal diatomic gases [9] 7/2 R (29.1 J mol⁻¹ K⁻¹ or R/2 per degree of freedom in the molecule). In

![](./images/814511362364407810_9.jpg)

Fig. 5. Model coefficients related to number of atoms, $n_{A}$: In a, coefficients $C_{P}{ }^{0}$ and $C_{P}{ }^{\infty}$ are regressed based on the number of atoms in the molecule $n_{A}: C_{P}{ }^{\infty}=-2.78+$ $2.22 n_{A}\left(R^{2}=0.999\right)$ for all gases. Restricting linear hydrocarbons $C_{P}{ }^{0}$ to C₂-C₇ hydrocarbons gives: $C_{P}{ }^{0}=0.33+5.18 n_{A}\left(R^{2}=0.993\right)$. In b, the same restriction was applied for $T_{i}: T_{i}=1132.2-7.3 n_{A}\left(R^{2}=0.965\right)$.

![](./images/814511362364407810_10.jpg)

Fig. 6. Entropy model predictions compared to the experimental data from 298 K to 6000 K. The model (Eq. (12)) deviates on average less than 1% for all the compounds.

fact, substituting the 7/2 R rather than fitting the value only drops the $R^{2}$ from 99.4% to 99.3% for $N_{2}$ in the range of 100-6000 K. For $CO_{2}$, $C_{P}^{0}$ is also approximately equal to 7/2 R, whereas it is about 8/2 R for $H_{2}O$, $CH_{4}$ and $C_{2}H_{4}$. Thus, the experimental coefficients of our model are directly linked to some molecular characteristics and may be related to previous theories on ideal mono and diatomic gases. Associating physico-chemical properties to the parameters reduces the empiricism of previous models.

Besides $\Delta H$, $\Delta S$ is the other critical thermodynamic properties that depends on $C_{P}$. Integrating $C_{P}/T$ (the Eq. (5)) leads to an Ei. Here, we propose a good approximation to it based on the same parameters we derived for $C_{P}$ (SI Table 2):

$$
\Delta S_{T_{1} \rightarrow T_{2}} \approx\left[C_{p}^{0} \ln (\underline{T})+C_{p}^{\infty} \ln (\underline{T})\left[\left(1+\frac{5}{3} \frac{T}{T_{i}}\right) /\left(1+\frac{2}{3} \frac{T}{T_{i}}\right)\right] \exp \left(-\frac{T_{i}}{T}\right)\right]_{T_{1}}^{T_{2}}
\tag{11}
$$

$$
S(T) \approx C_{p}^{0} \ln (\underline{T})+C_{p}^{\infty} \ln (\underline{T})\left[\left(1+\frac{5}{3} \frac{T}{T_{i}}\right) /\left(1+\frac{2}{3} \frac{T}{T_{i}}\right)\right] \exp \left(-\frac{T_{i}}{T}\right)+S_{0}
\tag{12}
$$

where $C_{P}^{0}$, $C_{P}^{\infty}$ and $T_{i}$ are the same as the values for $C_{P}$. This equation fits the experimental $S$ [28,29] (SI Table 3, Fig. 6). The absolute deviation between the model and experimental data is less than 2% up to 6000 K for all compounds except ethylene (4%) (SI Figure 9). With the same coefficients that we derived for $C_{P}$, the model accounts for 99% of the variance in the data with an average absolute deviations, AAD, of 1% over the whole temperature range. Introducing a fitted parameter $\varepsilon$ to replace the coefficients, 2/3 and 5/3, reduces that average deviation by factor of two (SI Table 3 and SI Figure 9):

$$
\begin{aligned}
S^{*}(T) \approx & C_{p}^{0} \ln (\underline{T})+C_{p}^{\infty} \ln (\underline{T})\left[\left(1+(1+\varepsilon) \frac{T}{T_{i}}\right) /\left(1+\varepsilon \frac{T}{T_{i}}\right)\right] \\
& \exp \left(-\frac{T_{i}}{T}\right)+S_{0}^{*}
\end{aligned}
\tag{13}
$$

## 5. Conclusions

The heat capacity of light gases and linear hydrocarbons ($C_{2}$ to $C_{7}$) varies as a function of temperature following an Arrhenius type dependency (Eq. (5)). The expression we derived to approximate $C_{P}$ and the integrated forms to give $\Delta H$ (Eq. (6)) and $\Delta S$ (Eq. (11)) are valid from 298 K up to 6000 K. These expressions account for 99% of the variance in the data with only three fitted parameters. The parameters reflect the characteristics of $C_{P}$ vs $T$ curve-origin ($C_{P}^{0}$), inflection point ($T_{i}$) and growing rate ($C_{P}^{\infty}$). The fitted parameter $C_{P}^{0}$ is within a couple percent of the theoretical value of heat capacity tending toward 0 K. (For a diatomic gas $C_{P}=7/2$ R). The other two terms vary with the number of atoms in the molecule. It applies to all thermodynamic and thermochemical processes from heat transfer or adiabatic flame temperatures to Gibbs free energy calculations ($\Delta G=\Delta H-T \Delta S$) to determine the direction and equilibrium of chemical reactions. Adding a fitted parameter increases the accuracy in entropy calculations (Eq. (12)). The model may apply to a larger variety of compounds and replace previous empirical polynomial expressions in handbooks and textbooks: the expression has fewer parameters, a wider temperature range, and equivalent accuracy.

## Associated content

Supporting Information Available: SI Fig. 7 and 8 & 9 related to deviation analysis and models comparison. SI Table 1, 2 & 3 providing experimentally fitted parameters for Eqs. (5), (6), (11) and (13) and models average absolute deviation AAD and correlation coefficients $R^{2}$. This material is available free of charge via the Internet at http://www.sciencedirect.com/.

## Author contributions

G.S.P conceived the project, C.B. and F.-X.C. did the literature review and collected the data. C.B. developed the model with assistance from G.S.P. The manuscript was written through contributions from C.B., F.-X.C., J.R.T and G.S.P. All authors have given approval to the final version of the manuscript.

## Funding

This work was supported by the Fond de Recherche du Québec - Nature et Technologie (FRQNT).

## Acknowledgment

We acknowledge the contribution of G. Lemieux and N. Amane as well as the FRQNT for its financial support.

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.expthermflusci.2016.06.008.

## References

[1] E.B. Moore, V. Molinero, Structural transformation in supercooled water controls the crystallization rate of ice, Nature 479 (2011) 506-509.
[2] C.A. Angell, Insights into phases of liquid water from study of its unusual glass-forming properties, Science 319 (2008) 582-587.
[3] M.W. Graham, S.-F. Shi, D.C. Ralph, J. Park, P.L. McEuen, Photocurrent measurement of supercollision cooling in graphene, Nat. Phys. 9 (2013) 103-108.
[4] S. Yamashita, T. Yamamoto, Y. Nakazawa, M. Tamura, R. Kato, Gapless spin liquid of an organic triangular compound evidenced by thermodynamic measurements, Nat. Commun. 2 (2010) 275.
[5] T. Liang, S.M. Koohpayeh, J.W. Krizan, T.M. McQueen, R.J. Cava, N.P. Ong, Heat capacity peak at the quantum critical point of the transverse Ising magnet CoNb2O6, Nat. Commun. 6 (2015) 7611.
[6] A.C. Jacko, J.O. Fjærestad, B.J.A. Powell, A unified explanation of the Kadowaki-Woods ratio in strongly correlated metals, Nat. Phys. 5 (2009) 422-425.
[7] M.H. Khademi, A.Z. Hezave, A. Jahanmiri, J. Fathikaljahi, An expression for ratio of critical temperature to critical pressure with the heat capacity for low to medium molecular weight compounds, J. Chem. Eng. Data 54 (2009) 690-700.

[8] A.T. Petit, P.L. Dulong, Recherches sur quelques points importants de la théorie de la chaleur, Annal. Chim. Phys. 10 (1819) 395-413.

[9] R. Fitzpatrick, Thermodynamics and Statistical Mechanics: An Intermediate Level Course, Lulu Marketplace, 2006. http://farside.ph.utexas.edu/teaching/sm1/statmech.pdf (accessed Jun. 06, 2016).

[10] R.C. Reid, J.M. Prausnitz, T.K. Sherwood, The Properties of Gases and Liquids, third ed., McGraw-Hill, New York, 1977.

[11] C.L. Yaws, X. Lin, L. Bu, S. Nijhawan, D.R. Balundgi, S. Tripathi, Chemical Properties Handbook: Physical, Thermodynamic, Environmental, Transport, Safety, and Health Related Properties for Organic and Inorganic Chemicals, McGraw-Hill, New York, 1999.

[12] B.J. McBride, S. Gordon, M.A. Reno, Coefficients for calculating thermodynamic and transport properties of individual species, Technical Report for NASA, TM-4513, 1993.

[13] A.G. Whittaker, P.L. Kintner, L.S. Nelson, N. Richardson, Carbon vapor pressure in the range 3450 to 4500 K and evidence for melting at approximately 3800 K, Technical Report for DTIC, SD-TR-81-60, 1981.

[14] A.D. Kirshenbaum, A. Grosse, The combustion of carbon subnitride, C4N2, and a chemical method for the production of continuous temperatures in the range of 5000-6000 K, J. Am. Chem. Soc. 78 (1956) 2020.

[15] V.A. Bychinskii, A.A. Tupitsyn, A.V. Mukhetdinova, K.V. Chudnenko, S.V. Fomichev, V.A. Krenev, Method of approximation of dependence of isobaric heat capacity on temperature, Russ. J. Inorg. Chem+ 58 (2013) 1511-1517.

[16] G.V. Belov, Thermodynamic Modeling: Methods, Algorithm, Programs, Nauchnyi Mir, Moscow, 2002.

[17] S.W. Benson, Thermochemical Kinetics: Methods for the Estimation of Thermochemical Data and Rate Parameters, second ed., Wiley, New York, 1976.

[18] P.E. Liley, G.H. Thomson, D.G. Friend, T.E. Daubert, E. Buck, Perry's Chemical Engineers' Handbook, seventh ed., McGraw-Hill, New York, 1997.

[19] N. Cohen, S.W. Benson, Estimation of heats of formation of organic compounds by additivity, Chem. Rev. 93 (1993) 2419-2438.

[20] S.C. Yuan, Y.I. Mok, New look at heat capacity prediction, Hydrocarb. Process. 47 (1968) 133.

[21] T.P. Thinh, J. Duran, R.S. Ramalho, Estimation of ideal gas heat capacities of hydrocarbons from group contribution techniques, Ind. Eng. Chem. Process Des. Dev. 10 (1971) 576.

[22] S.O. Colgate, C.F. Sona, K.R. Reed, A. Sivaraman, Experimental ideal gas reference state heat capacities of gases and vapors, J. Chem. Eng. Data 35 (1990) 1-5.

[23] D.W. Scott, Correlation of the chemical thermodynamic properties of alkane hydrocarbons, J. Chem. Phys. 8 (1974) 3144-3165.

[24] S.W. Benson, F.R. Cruickshank, D.M. Golden, G.R. Haugen, H.E. O'Neal, A.S. Rodgers, R. Shaw, R. Walsh, Additivity rules for the estimation of thermochemical properties, Chem. Rev. 69 (1969) 279-324.

[25] T.A. Albahri, Accurate prediction of the standard net heat of combustion from molecular structure, J. Loss. Prevent. Proc. 32 (2014) 377-386.

[26] T.P. Thinh, T.K. Trong, Estimation of standard heats of formation, standard entropies of formation, standard free energies of formation and absolute entropies of hydrocarbons from group contributions: an accurate approach, Can. J. Chem. Eng. 54 (1976) 344.

[27] R. Van de Vivjer, N.M. Vandewiele, P.L. Bhoorasingh, B.L. Slakman, F. Seyedzadeh Khanshan, H.-H. Carstensen, M.-F. Reyniers, G.B. Marin, R.H. West, K.M. Van Geem, Automatic Mechanism and Kinetic Model Generation for Gas- and Solution-Phase Processes: A Perspective on Best Practices, Recent Advances, and Future Challenges, Int. J. Chem. Kinet. 47 (2015) 199-231.

[28] B.J. McBride, S. Heimel, J.G. Ehlers, S. Gordon, Thermodynamic properties to 6000 K for 210 substances involving the first 18 elements, Technical Report for NASA, SP-3001, 1963.

[29] D.W. Scott, Chemical thermodynamic properties of hydrocarbons and related substances. Properties of the alkane hydrocarbons, C1 through C10 in the ideal gas state from 0 to 1500K, Bulletin for US Bureau of Mines, 666, 1974.

[30] L.V. Gurvich, I.V. Veyts, C.B. Alcock, Thermodynamic Properties of Individual Substances, Hemisphere, New York, 1989.

[31] D.W. Marquardt, An algorithm for least-squares estimation of nonlinear parameters, J. Soc. Ind. Appl. Math. 11 (1963) 11.