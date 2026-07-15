# Evaluating Thermal Quenching Temperature in Eu³⁺-Substituted Oxide Phosphors via Machine Learning

Ya Zhuo, Shruti Hariyani, Edward Armijo, Zainab Abolade Lawson, and Jakoah Brgoch*

Department of Chemistry, University of Houston, Houston, Texas 77204, United States

![](./images/812699303574241281_1.jpg) Supporting Information

**ABSTRACT:** One of society's grand challenges is to reduce energy usage in ways that are cost-effective, sustainable, and environmentally benign. Replacing incandescent and compact fluorescent light bulbs with energy-efficient, solid-state white lighting is one of the easiest and most promising solutions. Eu³⁺-substituted inorganic oxide phosphors are one class of materials that can serve as the red component in these new light bulbs, allowing the creation of warm white light. Unfortunately, the emission intensity in most of these materials cannot be reliably maintained at elevated temperatures. There is therefore a need to discover entirely novel phosphor materials that are thermally robust; however, this is generally a prolonged and expensive process requiring extensive synthetic effort. In this work, we develop a machine-learning regression algorithm based on 134 experimentally measured temperature-dependent Eu³⁺ emission data points to rapidly estimate the thermal quenching temperature ($T_{50}$), which is defined as the temperature when the emission intensity is half of the initial value. The $T_{50}$ was then predicted for more than 1000 potential oxide Eu³⁺ phosphor hosts using this model. Five compounds with predicted thermal quenching temperatures >423 K were subsequently selected and synthesized for validation of this approach. The phosphors, Sr₂ScO₃F, Cs₂MgSi₅O₁₂, Ba₂P₂O₇, LiBaB₉O₁₅, and Y₃Al₅O₁₂, all exhibit good thermal stability when substituted with Eu³⁺, suggesting the success of our methodology.

**KEYWORDS:** machine learning, support vector regression, photoluminescence, inorganic phosphors, thermal quenching

![](./images/812699303574241281_2.jpg)

## 1. INTRODUCTION

The principal strategy for producing white light from an LED chip is by down-converting and broadening the nearly monochromatic emission using rare-earth-substituted inorganic phosphors, creating a so-called phosphor-converted LED ($pc$-LED).¹⁻⁴ The prototypical $pc$-LED combines a blue InGaN LED and a yellow-emitting phosphor, like cerium-substituted yttrium aluminum garnet (YAG:Ce³⁺), to generate a broad emission peak that covers nearly the entire visible spectrum, thus appearing as white light. Although functional, these devices have a low color rendering index ($R_{a}$) and high correlated color temperature (CCT), hindering extensive adoption in homes and offices, where "warmer" lighting is preferred.⁵ Adding a second, red-emitting phosphor is currently the best option to enhance color quality and reduce the CCT.

The electronic transitions that typically generate emission in the red region of the visible spectrum occur for ions such as Eu²⁺, Eu³⁺, Mn⁴⁺, Pr³⁺, or Sm³⁺ substituted in an inorganic host compound such as an oxide, nitride, or halide.⁶ Out of these possible luminescent centers, Eu²⁺ is the most common, where the 4$f^{7}$ configuration can be excited to the 4$f^{6}$5$d^{1}$ state using a blue or (near)-UV LED. The ensuing relaxation back to the ground state is highly dependent on the host lattice and can span from the blue to near-infrared spectral region as controlled by the host crystal chemistry. These Eu²⁺-based materials have high quantum yields, are chemically robust, and tend to produce a thermally stable emission. The primary limitation of Eu²⁺ phosphors is their broad emission spectrum, which decreases the luminous efficacy.⁵ Therefore, researchers are continually looking for novel, narrow, red-emitting Eu²⁺ phosphors.⁷,⁸ Research has also focused on Mn⁴⁺-substituted materials. In an octahedral crystal field, the distinct $^{2}$E → $^{4}$A₂ transition results in vibronic emission bands in the red and infrared region, depending on the host composition.⁹ For solid-state lighting, the most useful Mn⁴⁺-substituted materials are based on fluorides or oxyfluorides, producing a sharp 3$d$ ↔ 3$d$ transition in the red region of the visible spectrum. Unfortunately, these hosts tend to have limited chemical stability, precluding their use in extreme environments, and long luminescence lifetimes (~8 ms) that lead to photo-saturation effects.¹⁰,¹¹ Other red-emitting materials have also been developed, with the most notable focus on trivalent lanthanide ions, including Eu³⁺, Pr³⁺, and Sm³⁺. These phosphors are generally based on oxide hosts and have a characteristic narrow-band emission in the red region, making

---

Special Issue: Young Investigator Forum

Received: September 5, 2019

Accepted: December 9, 2019

them ideal for the red component in solid-state lighting. However, the $4f^6 \leftrightarrow 4f^6$ parity-forbidden electronic transitions of these luminescence centers exhibit weak absorption, inhibiting intense photon emission. Adding sensitizer ions to improve the excitation probability of these red-emitting activators has been demonstrated with reasonable success in systems like $\mathrm{Bi^{3+}/Eu^{3+}}$, $\mathrm{Tb^{3+}/Eu^{3+}}$, or $\mathrm{Ce^{3+}/Tb^{3+}/Eu^{3+}}^{12,13}$ The host compound must also allow a high substitution concentration of $\mathrm{Eu^{3+}}$ before concentration quenching takes place, which is necessary for a high quantum yield. Never- theless, this combination of high $\mathrm{Eu^{3+}}$ concentration and the addition of a second sensitizer ion allows these phosphors to be considered as a viable red component in $pc$-LEDs.

One standing challenge is improving the thermal stability of the emission intensity of $\mathrm{Eu^{3+}}$-substituted phosphors. Phos- phors suffer a decrease in light output with increasing temperature due to thermal quenching. $^{14}$ These adverse effects are the result of elevated LED device operating temperature due to more compact packaging and the use of high-power LED chips. Yet, the knowledge of crystal chemistry that governs a phosphor's thermal quenching behavior remains unclear. Fortunately, merging data science and materials science has become a promising tool to guide the discovery of new materials with desired properties. For example, researchers have created models to predict the electronic properties of materials such as band gap, dielectric constant, electron affinity, and formation energy. $^{15-18}$ Moreover, it is possible to predict materials' intrinsic mechanical properties including elastic moduli, heat capacity, and Debye temperature and extrinsic, bulk properties such as microstructure, fatigue strength in steels, and cracks in road surface. $^{19-23}$

Here, we apply supervised machine learning based on support vector regression (SVR) to predict the thermal response of $\mathrm{Eu^{3+}}$-substituted phosphors. Our training set employs 134 experimentally reported thermal quenching temperatures $(T_{50})$, which is the temperature that the photoluminescence emission intensity degrades to 50% of the room temperature value. These data were obtained by mining peer-reviewed literature. The initial feature set employed for machine learning is limited to compositional features, two space group features, and the rare-earth substitution concentration because most quenching temper- atures obtained from the literature are not accompanied by sufficient crystallographic data. The final feature set was then reduced to only 51 features after applying feature elimination. The advantage of using a training set derived from experimentally measured $T_{50}$ values and a composition-based feature set is that the resulting machine-learning algorithm can rapidly and accurately predict the $T_{50}$ for any given composition. Using this training set, we constructed a regression model that was finally applied to predict the $T_{50}$ of more than 1000 oxides. $\mathrm{Sr_2ScO_3F}$, $\mathrm{Cs_2MgSi_3O_{12}}$, $\mathrm{Ba_2P_2O_7}$, $\mathrm{LiBaB_9O_{15}}$, and $\mathrm{Y_3Al_5O_{12}}$ were suggested to have high $T_{50}$ values from these predictions and were thus prepared using high-temperature solid-state synthesis with 5% $\mathrm{Eu^{3+}}$ sub- stitution. The ensuing optical properties including temper- ature-dependent luminescence were studied. All compounds selected had their experimentally measured $T_{50}$ confirmed to be well above LED device operating temperatures and also close to our model prediction, suggesting their potential application in $pc$-LEDs and display devices as well as the accuracy of our regression model. Moreover, these results show the power of data science in material discovery even in the situation where training data is sparse.

## 2. MATERIALS AND METHODS
The regression model was trained on experimental data extracted from the literature using the support vector regression (SVR) method implemented with a linear kernel and evaluated with leave-one-out (LOO) cross-validation. $^{24,25}$ The initial feature set used to construct the model is provided in Table S1. A recursive feature elimination (RFE) scheme was then employed for feature reduction. Hyper- parameter settings were adjusted with a grid search method, which exhaustively evaluates all parameter combinations. The searching space was defined as cost values ranging in [0.3, 1, 3, 10, 30, 100] and epsilon values in [0.001, 0.01, 0.1, 1] where cost is the penalty parameter of the error term and epsilon specifies the tube within which no penalty is associated in the training loss function with points predicted within a distance epsilon from the actual value. The SCIKIT-LEARN python implementations of these learning algo- rithms were used. $^{26}$

Selected phosphors were prepared via solid-state reactions in alumina crucibles starting from $\mathrm{SrCO_3}$ (Alfa Aesar, 99%), $\mathrm{Sc_2O_3}$ (Materion Advanced Chemicals, 99.9%), $\mathrm{SrF_2}$ (Alfa Aesar, 99%), $\mathrm{BaCO_3}$ (Johnson Matthey, 98%), $\mathrm{Li_2CO_3}$ (Alfa Aesar, 99.998%), $\mathrm{H_3BO_3}$ (Sigma-Aldrich, 99.999%), $\mathrm{NH_4H_2PO_4}$ (Acros Organics, 99.9%), MgO (Sigma-Aldrich, 99.995%), $\mathrm{Y_2O_3}$ (Alfa Aesar, 99.9%), $\mathrm{Al_2O_3}$ (Sigma-Aldrich, 99.99%), $\mathrm{Cs_2CO_3}$ (Alfa Aesar, 99%), $\mathrm{SiO_2}$ (Sigma-Aldrich, 99.5%), and $\mathrm{Eu_2O_3}$ (Materion Chemicals, 99.9%). The starting materials for each compound were loaded in the requisite stoichiometric ratios and then thoroughly ground using an agate mortar and pestle. $\mathrm{Sr_2ScO_3F:Eu^{3+}}$ was reacted at 1050 °C for 8 h, ground, and heated again using the same reaction profile. To make $\mathrm{Cs_2MgSi_3O_{12}:Eu^{3+}}$, we combined starting reagents and ground in an acetone medium. Pellets of the sample were pressed and laid on a bed of sacrificial powder to avoid reaction with crucible. The reaction was then carried out at 1000 °C for 12 h. For $\mathrm{Ba_2P_2O_3:Eu^{3+}}$ and $\mathrm{LiBaB_9O_{15}:Eu^{3+}}$, starting powders were first decomposed under 500 °C for 6 h and 600 °C for 2 h, respectively and then reground before reacting at 1100 °C for 4 h and 800 °C for 22 h, respectively. All reactions mentioned above were carried out in air with furnace heating and cooling rates of 3 °C/min. $\mathrm{Y_3Al_5O_{12}:5\%Eu^{3+}}$ was made with a microwave-assisted solid-state reaction. The starting powder was mixed with 1 wt % $\mathrm{NH_4Cl}$ and 5 wt % $\mathrm{BaF_2}$ as flux. The mixture was reacted at ~1200 W for 10 min and then ~960 W for 8 min.

The samples were checked for phase purity using powder X-ray diffraction on a PANalytical Empyrean powder diffractometer equipped with Cu $K\alpha$ radiation ($\lambda = 1.54183$ Å). Additionally, the lattice parameters were refined based on the Le Bail method using the GSAS package with a shifted Chebyshev function employed to model the background. $^{27,28}$

The samples were then mixed into an optically transparent silicone resin (GE Silicones, RTV615) and deposited on a quartz substrate (Chemglass). Steady-state photoluminescent spectra were collected at room temperature on a Photon Technology International fluores- cence spectrophotometer with a 75 W xenon arc lamp for excitation. The temperature-dependent emission spectra were collected from 300 to 600 K in 20 K increments using a $\lambda_{ex} = 395$ nm with the temperature controlled using a Janis liquid nitrogen cryostat (VPF- 100). The (internal) photoluminescence quantum yield (PLQY) was measured three times for each compound prepared with 5% $\mathrm{Eu^{3+}}$ using the method of de Mello et al. inside a Spetralon-coated integrating sphere (150 mm diameter, Labsphere) and exciting at 395 nm. $^{29}$

## 3. RESULTS AND DISCUSSION
### 3.1. Data Extraction and Feature Development.
The development of the machine-learning model to predict the thermal quenching temperature first involves extracting 269 experimentally reported host compositions and the associated


![](./images/812699303574241281_3.jpg)

Figure 1. (a) Coefficient of determination ($r^2$) as a function of the number of features. The red dot is showing the best $r^2$. (b) Weight assigned to each feature. (c) Plot of parameter optimization for cost and epsilon. The optimized cost and epsilon are highlighted by the red box.

$T_{50}$ values from the literature. Prior to model construction, data sanitization was conducted to ensure consistency within the machine-learning training set. Two primary criteria were considered for data retention. First, the $T_{50}$ must be reached within the measurement window; extrapolated data were not included. The second criterion is that the initial emission measurements must start at room temperature, i.e., the first data point is at $\sim$300 K. The final training set was reduced accordingly to 134 compounds composed of 130 oxides (including oxyhalides), 3 nitrides, and 1 fluoride. Despite the reduction in size, the training set still contained a range of $T_{50}$ values from thermally unstable phosphors such as $Ca_{2.91}Eu_{0.06}Ba_2N_4$ ($T_{50} = 330$ K)$^{30}$ and $Lu_{1.9}Eu_{0.1}MoO_6$ ($T_{50}$ = 353 K)$^{31}$ to thermally robust phosphors like $La_{0.97}Eu_{0.03}BO_3$ ($T_{50} = 750$ K)$^{32}$ and $Y_{1.99}Eu_{0.01}O_3$ ($T_{50} = 810$ K).$^{33}$ The full training labels are provided in Table S2. Given the large imbalance in the data toward oxide-based phosphors, the ensuing model construction was focused on $Eu^{3+}$-substituted oxide phosphors.

Our choice of features was dictated by gathering a large number of features and performing dimensionality reduction to down-select a few features. Compounds considered by the machine-learning algorithm were first described by a set of 35 distinct compositional variables along with five mathematical expressions including the weighted average, the difference, the maximum value, the minimum value, and the standard deviation, where the weights are the stoichiometric number of the chemical constituents in a given composition. These compositional variables are related to the relative position of atoms on the periodic table, the electronic structure, and their physical properties.$^{34}$ For example, atomic number, atomic weight, Mendeleev's number, and covalent radius are included to account for the relative size, weight effects, and chemical similarity across different atoms. Electron affinity provides relevant energy scales for electronic excitations, whereas electronegativity is used to model relative chemical trends in the valence and conduction band edges across a range of chemistries. Atomic polarization is relevant to the determination of the centroid shift. Additionally, specific heat and heat of vaporization account for the impact on the energy change as temperature varies. Because polymorphs are contained within the training set and the reported $Eu^{3+}$ substitution concentration values from literature vary from 0.5 to 100%, additional features beyond compositional variables were also extracted from the literature, including host crystal system, host space group, and $Eu^{3+}$ substitution concentration. The combination of these variables resulted in an initial total of 178 features for the model. The full list of features is provided in Table S1.

Considering the number of features is greater than the number of training labels, which often deteriorates the predictive power of the model as a result of overfitting, recursive feature elimination (RFE) was conducted to decrease the overall number of features employed by the model. First, the 178 features were rescaled to have zero mean and unit variance. The estimator was then trained on the transformed 178 features, and the importance of each feature was obtained through a coefficient attribute, specifically, the weights assigned to the features by a linear kernel embedded in support vector regression (SVR). The least five important features were then pruned from the set of features. This procedure was recursively repeated on each pruned set until the assigned number of features was eventually reached. Tuning the number of features selected from RFE can find the optimal number of features, which gives the best accuracy in terms of coefficient of determination ($r^2$). Figure 1a shows the model performance as a function of the number of features, evaluated by $r^2$, indicating the model accuracy. This analysis scheme was obtained from leave-one-out cross-validation, and the model performance was examined using a range of 25−175 features in increments of 25 features. Two local maxima appear at 50 features and 100 features, with an $r^2$ of 0.69 and 0.65, respectively. The model with 50 features outperforms 100 features; therefore, the model examination was further done using 51 and 52 features, respectively. As shown in Figure 1a, with 51 features, the model performance reaches the best value of $r^2 = 0.71$. Further increasing the number of features to 52 results in $r^2$ decreasing. Interestingly, all three noncompositional features were pruned from the initial feature set, which is beneficial in prediction as the $T_{50}$ can be readily predicted for any given composition. It is also interesting to note that $Eu^{3+}$ concentration was removed from the feature set suggestion that it has minimal influence on the $T_{50}$ values. The final reduced feature set is composed of 51 compositional features selected from RFE. The numbers of features selected from each mathematical expression are

equally distributed, except for the maximum scenario where only five features remained after feature selection. The weight, which is also called the coefficient, assigned to each feature is provide in Figure 1b. Twenty-four features have positive weights, whereas 27 features have negative weights. The absolute weight varies from 11.47 for the standard deviation of Pauling electronegativity to 70.19 for the standard deviation of the Martynov–Batsanov electronegativity. Finally, the 51 selected features were scaled back to their original representations before the learning.

3.2. Model Construction. Our approach to learning from the experimental thermal quenching data was to establish how $T_{50}$ varies with the input features by using regression methods and then predicting the $T_{50}$ of unexplored oxide phosphors. A support vector regression (SVR) algorithm using a linear kernel was used to construct the model due to its efficiency when dealing with small training sets. Our model was cross-validated with the leave-one-out (LOO) method. Before learning, the training data were standardized to have a mean of 0 and variance of 1, and the validation data were unseen. The same scaling was then applied to the validation data. Because SVR is highly sensitive to hyper-parameter settings, the cost ($C$), which is the penalty parameter of the error term, and epsilon ($\varepsilon$), which is a free parameter that serves as a threshold where all predictions have to be within a $\pm\varepsilon$ range of the true predictions, were tuned using an exhaustive grid search. Figure 1c shows the model performance with different $C$ and $\varepsilon$ combinations in terms of $r^{2}$. When $\varepsilon = 0.01$, $r^{2}$ varies from 0.33 to 0.71 as changing $C$ with an optimal $C = 30$. On the other hand, different values of $\varepsilon$ do not influence the model performance as significantly as $C$. When $C = 30$ and $\varepsilon = 0.01$, the model has the maximal $r^{2}$ of 0.71. Further decreasing $\varepsilon$ did not enhance the model accuracy further.

The validation results for the optimized model are plotted in Figure 2. The coefficient of determination had an $r^{2} = 0.71$ with a mean absolute error (MAE) of 31 K, demonstrating reasonable prediction power of our machine-learning model even for this small training set. The histograms at the top and right show that the training and validation sets contain a good spread of data across the entire $T_{50}$ range with standard deviations of 87 and 69 K, respectively. There is a slight underestimation for the high $T_{50}$ phosphors, which is most likely due to a limited number of compounds reported with these high experimental $T_{50}$ values as well as difficulties measuring optical properties at such extreme temperatures.

![](./images/812699303574241281_4.jpg)

Figure 2. Predicted $T_{50}$ from the cross-validation of 134 training data versus experimental $T_{50}$. The ideal line is shown as the solid gray line. The histograms at the top and right show that the training and validation sets contain a good spread of data across the entire $T_{50}$ range of interest.

3.3. Experimental Validation through Novel Material Synthesis. Once the model was constructed, it was used to estimate the $T_{50}$ for 1337 oxide compounds compiled in Pearson's Crystal Data (PCD).$^{35}$ Oxides containing transition metals from groups 7–11 and group 18 as well as Cd, Hg, Tl, Pb, and hydrogen-containing compounds were removed from our prediction set because they are rarely reported to be suitable inorganic phosphor hosts. The final prediction set is provided in Table S3.

A selection of five different phosphor hosts were then chosen for experimental investigation to not only verify our model's accuracy but also to potentially discover new thermally stable Eu$^{3+}$ phosphors. The selection of the target materials was intended to be diverse in terms of both composition and structure. Moreover, all of the compounds chosen had a predicted $T_{50}$ above 423 K, which is the peak operating temperature of current lighting devices.$^{36}$ Finally, only the compounds that could be synthesized under ambient pressure and are stable at room temperature were considered. Eventually, $Sr_{2}ScO_{3}F$, $Cs_{2}MgSi_{5}O_{12}$, $Ba_{2}P_{2}O_{7}$, $LiBaB_{9}O_{15}$, and $Y_{3}Al_{5}O_{12}$, were found to be of interest for experimental analysis.$^{37-41}$ Their predicted $T_{50}$ values were 479, 553, 575, 643, and 681 K, respectively. All five compounds, illustrated in Figure 3, were synthesized via high-temperature solid-state reaction with 5% Eu$^{3+}$ substituted in the systems. The phase purity was confirmed with Le Bail refinements based on laboratory (Cu $K\alpha$) powder X-ray diffraction patterns, shown in Figure 4. Refinement results and unit cell parameters are provided in Table S4.

![](./images/812699303574241281_5.jpg)

Figure 3. Phosphor hosts considered in the experimental verifications are (a) $Sc_{2}ScO_{3}F$, (b) $LiBaB_{9}O_{15}$, (c) $Ba_{2}P_{2}O_{7}$, (d) $Y_{3}Al_{5}O_{12}$, and (e) $Cs_{2}MgSi_{5}O_{15}$. Sc, B, P, Al, and Si(Mg) occupy the center of the polyhedra. Sr, Li, Ba, and Cs are colored in different shades of gray. F is in green, Y is in pink, and O is in orange.

The photoluminescent excitation spectrum of each phosphor was measured and is plotted Figure 5a. The compounds can all be excited between $\sim$350 to $\sim$450 nm as monitored under the corresponding monitoring wavelength provided in Figure 5b. All five samples exhibit similar excitation spectra

![](./images/812699303574241281_6.jpg)

Figure 4. Le Bail refinements of (a) $Sr_{2}ScO_{3}F$, (b) $Cs_{2}MgSi_{5}O_{15}$, (c) $Ba_{2}P_{2}O_{7}$, (d) $LiBaB_{9}O_{15}$, and (e) $Y_{3}Al_{5}O_{12}$ using X-ray powder diffraction data. The measured data are shown in black, the fit by the red line, and the difference between the data and the fit by the blue line.

![](./images/812699303574241281_7.jpg)

Figure 5. (a) Excitation and (b) emission spectra of all prepared $Eu^{3+}$ substituted phosphors. The emission data for all compounds are collected using $\lambda_{ex}=395$ nm.

with three main peaks below 400 nm and one small peak centered beyond 400 nm. The sequence of sharp excitation lines was ascribed to the $4f\leftrightarrow4f$ transition of $Eu^{3+}$ ions. The strongest absorption line is located at approximately 395 nm, which indicates the potential application in pc-LEDs. Upon 395 nm excitation, the emission spectra were collected and are plotted in Figure 5b. $Y_{3}Al_{5}O_{12}:Eu^{3+}$ shows two main peaks at 591 and 710 nm, respectively. The spectrum of $LiBaB_{9}O_{15}:Eu^{3+}$ is dominated by a strong red emission with a center at $\sim$610 nm, whereas $Ba_{2}P_{2}O_{7}:Eu^{3+}$ exhibits a series of sharp, intense peaks ranging from 589 to 700 nm. $Cs_{2}MgSi_{5}O_{12}$ possesses only one peak around 614 nm, which could be attributed to several peaks overlapping with one another. Finally, $Sr_{2}ScO_{3}F:5\%Eu^{3+}$ shows one intense peak at 610 nm with a shoulder peak at around 625 nm. The corresponding photoluminescence quantum yield (PLQY) of each sample upon 395 nm excitation is provided in Table S5.

The thermal stability of these phosphors is the central focus of this research because the junction temperature of typical LEDs can be as high as $423$ K.$^{36}$ Therefore, temperature- dependent emission spectra were collected from 300 to 600 K in 20 K steps for all five phosphors upon excitation at 395 nm. The emission peak that was monitored was the most intense peak generally centered around 600 nm. Contour plots based on the raw emission data as a function of temperature are provided in Figure S1. The quenching temperature, $T_{50}$, which is regarded as the temperature at which the emission intensity is 50% of its original value, was then obtained by normalizing the intensity of the peak at $\sim$600 nm, shown in Figure 6. The

![](./images/812699303574241281_8.jpg)

Figure 6. Normalized peak intensity is plotted against temperature. The dashed gray line indicates the 50% normalized peak intensity ($T_{50}$).

emission intensity slowly decreased with increasing temper- ature for $Y_{3}Al_{5}O_{12}:Eu^{3+}$ and $LiBaB_{9}O_{15}:Eu^{3+}$, indicating a $T_{50}$ of 760 and 650 K, respectively, obtained by extrapolating the data. The excellent thermal stability of both is similar to their respective predictions, although $Y_{3}Al_{5}O_{12}:5\%Eu^{3+}$ shows some discrepancy to its prediction (680 K). $Cs_{2}MgSi_{5}O_{12}:5\%Eu^{3+}$ thermally quenched faster than the two phosphors mentioned above, at 540 K. Interestingly, the intensity stays unchanged between the 500 and 600 K measuring window. This phenomenon was not only observed in this silicate phosphor but also in $GdAlO_{3}:4\%Eu^{3+}$ and $KY_{0.97}Eu_{0.03}P_{2}O_{7}$.$^{42,43}$ Further increasing the temperature causes the intensity to decrease again, as expected. The phosphate and oxyfluoride phosphor, $Ba_{2}P_{2}O_{7}:5\%Eu^{3+}$ and $Sr_{2}ScO_{3}F:5\%Eu^{3+}$, are the least thermally stable phosphors among the five selected candidates. Although their thermal responses are not as outstanding as the rest, their respective $T_{50}$ values (475 K for $Ba_{2}P_{2}O_{7}$ and 450 K for $Sr_{2}ScO_{3}F$) are still well above the 423 K threshold. For easy comparison, the predicted and experimental results are listed in Table 1. Considering a majority of the predictions were close to our experimental value, it proves that our machine-learning model has reliable predictive capability, which will allow this approach to at least act as a top-level screening in the search for new thermally robust $Eu^{3+}$-based phosphors.

### 4. CONCLUSIONS
A predictive model based on the thermal quenching temper- ature was developed by constructing machine-learning algorithms using training data extracted from the literature.

<table>
<thead>
<tr>
<th colspan="5">Table 1. Comparison of Predicted (pred.) $T_{50}$ and the Experimental (exp.) $T_{50}$ with the Percent Difference (% diff.) is Provided</th>
</tr>
<tr>
<th>composition</th>
<th>space group</th>
<th>pred. $T_{50}$ (K)</th>
<th>exp. $T_{50}$ (K)</th>
<th>% diff.</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Sr_2ScO_3F$:$Eu^{3+}$</td>
<td>$I4/mmm$</td>
<td>479</td>
<td>450</td>
<td>6</td>
</tr>
<tr>
<td>$Cs_2MgSi_5O_{12}$:$Eu^{3+}$</td>
<td>$Ia\overline{3}d$</td>
<td>553</td>
<td>540</td>
<td>2</td>
</tr>
<tr>
<td>$Ba_2P_2O_7$:$Eu^{3+}$</td>
<td>$P\overline{6}2m$</td>
<td>575</td>
<td>475</td>
<td>21</td>
</tr>
<tr>
<td>$BaLiB_9O_{15}$:$Eu^{3+}$</td>
<td>$R\overline{3}c$</td>
<td>643</td>
<td>650</td>
<td>−1</td>
</tr>
<tr>
<td>$Y_3Al_5O_{12}$:$Eu^{3+}$</td>
<td>$Ia\overline{3}d$</td>
<td>681</td>
<td>760</td>
<td>−10</td>
</tr>
</tbody>
</table>

This data-driven approach allowed the rapid prediction of the thermal quenching temperature for $Eu^{3+}$-substituted oxide phosphors prior to experimental efforts. Selected compounds from the prediction, $Sr_2ScO_3F$, $Cs_2MgSi_5O_{12}$, $Ba_2P_2O_7$, $LiBaB_9O_{15}$, and $Y_3Al_5O_{12}$, were synthesized with 5% $Eu^{3+}$ substitution followed by optical characterization. The excitation spectra show that these phosphors can be effectively excited by near-UV light, which adequately matches the emission wavelength of commercial near-UV LED chips. All five phosphors possess an experimentally measured $T_{50}$ well above LED device operating temperature, as desired, suggesting their potential application in pc-LEDs and display devices. Moreover, the observed experimental $T_{50}$ also agrees well with our model prediction, indicating the accuracy of our model. These results highlight the power of using data science to advance materials discovery even for situations where only small training data sets are available.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsami.9b16065.

Table S1, feature set; Table S2, training labels; Table S3, predicted $T_{50}$; Table S4: Le Bail refinement results; Table S5, photoluminescence quantum yield of samples; Figure S1, ontour plots of the normalized emission spectra (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*Email: jbrgoch@central.uh.edu (J.B.).

### ORCID
Ya Zhuo: 0000-0003-2554-498X
Shruti Hariyani: 0000-0002-4707-8863
Jakoah Brgoch: 0000-0002-1406-1352

### Funding
This research was funded by National Science Foundation, Grant DMR 18-47701 and CER 19-11311; Welch Foundation, Grant E-1981; and Seed Funding for Advanced Computing (SeFAC) at the University of Houston.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
Z.A. acknowledges the ACS Project SEED program for supporting her research. Y.Z. and J.B. thank Dr. Mike Krames and Dr. Marie Anne van de Haar for many fruitful discussions.

## REFERENCES
(1) Lin, C. C.; Liu, R.-S. Advances in Phosphors for Light-Emitting Diodes. J. Phys. Chem. Lett. 2011, 2, 1268−1277.

(2) Qin, X.; Liu, X.; Huang, W.; Bettinelli, M.; Liu, X. Lanthanide- Activated Phosphors Based on 4f-5d Optical Transitions: Theoretical and Experimental Aspects. Chem. Rev. 2017, 117, 4488−4527.

(3) Pimputkar, S.; Speck, S. J.; DenBaars, P. S.; Nakamura, S. Prospects for LED Lighting. Nat. Photonics 2009, 3, 180−182.

(4) George, N. C.; Denault, K. A.; Seshadri, R. Phosphors for Solid- State White Lighting. Annu. Rev. Mater. Res. 2013, 43, 481−501.

(5) McKittrick, J.; Shea-Rohwer, L. E. Review: Down Conversion Materials for Solid-State Lighting. J. Am. Ceram. Soc. 2014, 97, 1327−1352.

(6) Li, J.; Yan, J.; Wen, D.; Khan, W. U.; Shi, J.; Wu, M.; Su, Q.; Tanner, P. A. Advanced Red Phosphors for White Light-Emitting Diodes. J. Mater. Chem. C 2016, 4, 8611−8623.

(7) Zeuner, M.; Hintze, F.; Schnick, W. Low Temperature Precursor Route for Highly Efficient Spherically Shaped LED-Phosphors $M_2Si_5N8$:$Eu^{2+}$ (M = Eu, Sr, Ba). Chem. Mater. 2009, 21, 336−342.

(8) Qiao, J.; Ning, L.; Molokeev, M. S.; Chuang, Y.; Zhang, Q.; Poeppelmeier, K. R.; Xia, Z. Site-selective Occupancy of $Eu^{2+}$ toward Blue-light-excited Red Emission in a $Rb_3YSi_5O_7$:Eu Phosphor. Angew. Chem. 2019, 131, 11645−11650.

(9) Setlur, A. A.; Lyons, R. J.; Murphy, J. E.; Prasanth Kumar, N.; Satya Kishore, M. Blue Light-Emitting Diode Phosphors Based upon Oxide, Oxyhalide, and Halide Hosts. ECS J. Solid State Sci. Technol. 2013, 2, R3059−R3070.

(10) Sijbom, H. F.; Joos, J. J.; Martin, L. I. D. J.; Van den Eeckhout, K.; Poelman, D.; Smet, P. F. Luminescent Behavior of the $K_2SiF_6$:$Mn^{4+}$ Red Phosphor at High Fluxes and at the Microscopic Level. ECS J. Solid State Sci. Technol. 2016, 5, R3040−R3048.

(11) Verstraete, R.; Sijbom, H. F.; Joos, J. J.; Korthout, K.; Poelman, D.; Detavernier, C.; Smet, P. F. Red $Mn^{4+}$-Doped Fluoride Phosphors: Why Purity Matters. ACS Appl. Mater. Interfaces 2018, 10, 18845−18856.

(12) Maciel, G. S.; Rakov, N. Photon Conversion in Lanthanide- Doped Powder Phosphors: Concepts and Applications. RSC Adv. 2015, 5, 17283−17295.

(13) van de Haar, M. A.; Werner, J.; Kratz, N.; Hilgerink, T.; Tachikirt, M.; Honold, J.; Krames, M. R. Increasing the Effective Absorption of $Eu^{3+}$-Doped Luminescent Materials towards Practical Light Emitting Diodes for Illumination Applications. Appl. Phys. Lett. 2018, 112, 132101.

(14) Blasse, G.; Sabbatini, N. The Quenching of Rare-Earth Ion Luminescence in Molecular and Non-Molecular Solids. Mater. Chem. Phys. 1987, 16, 237−252.

(15) Zhuo, Y.; Mansouri Tehrani, A.; Brgoch, J. Predicting the Band Gaps of Inorganic Solids by Machine Learning. J. Phys. Chem. Lett. 2018, 9, 1668−1673.

(16) Mannodi-Kanakkithodi, A.; Pilania, G.; Huan, T. D.; Lookman, T.; Ramprasad, R. Machine Learning Strategy for Accelerated Design of Polymer Dielectrics. Sci. Rep. 2016, 6, 20952.

(17) Pilania, G.; Wang, C.; Jiang, X.; Rajasekaran, S.; Ramprasad, R. Accelerating Materials Property Predictions Using Machine Learning. Sci. Rep. 2013, 3, 2810.

(18) Ramprasad, R.; Batra, R.; Pilania, G.; Mannodi-Kanakkithodi, A.; Kim, C. Machine Learning in Materials Informatics: Recent Applications and Prospects. npj Comput. Mater. 2017, 3, 54.

(19) Agrawal, A.; Deshpande, P. D.; Cecen, A.; Basavarsu, G. P.; Choudhary, A. N.; Kalidindi, S. R. Exploration of Data Science Techniques to Predict Fatigue Strength of Steel from Composition and Processing Parameters. Integr. Mater. Manuf. Innov. 2014, 3, 90−108.

(20) Liu, R.; Kumar, A.; Chen, Z.; Agrawal, A.; Sundararaghavan, V.; Choudhary, A. A Predictive Machine Learning Approach for Microstructure Optimization and Materials Design. Sci. Rep. 2015, 5, 11551.

(21) Mansouri Tehrani, A.; Oliynyk, A. O.; Parry, M.; Rizvi, Z.; Couper, S.; Lin, F.; Miyagi, L.; Sparks, T. D.; Brgoch, J. Machine

Learning Directed Search for Ultraincompressible, Superhard Materials. *J. Am. Chem. Soc.* **2018**, *140*, 9844−9853.

(22) Zhuo, Y.; Mansouri Tehrani, A.; Brgoch, J. Predicting the Band Gaps of Inorganic Solids by Machine Learning. *J. Phys. Chem. Lett.* **2018**, *9*, 1668−1673.

(23) Zhang, L.; Yang, F.; Daniel Zhang, Y.; Zhu, Y. J. Road Crack Detection Using Deep Convolutional Neural Network. *In 2016 IEEE International Conference on Image Processing (ICIP)*; IEEE, 2016; 3708−3712.

(24) Chang, C. C.; Lin, C. J. LIBSVM: A Library for Support Vector Machines. *ACM Trans. Intell. Syst. Technol.* **2011**, *2*, 27.

(25) Drucker, H.; Burges, C. J. C.; Kaufman, L.; Smola, A.; Vapnik, V. Support Vector Regression Machines. *Adv. Neural Inf. Process. Syst.* **1996**, *1*, 155−161.

(26) Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; Vanderplas, J.; Passos, A.; Cournapeau, D.; Brucher, M.; Perrot, M.; Duchesnay, É. Scikit-Learn: Machine Learning in Python. *J. Mach. Learn. Res.* **2011**, *12*, 2825−2830.

(27) Larson, A. C.; Von Dreele, R. B. *General Structure Analysis System (GSAS)*; Los Alamos National Laboratory: Los Alamos, NM, 1987.

(28) Toby, B. H. EXPGUI, A Graphical User Interface for GSAS. *J. Appl. Crystallogr.* **2001**, *34*, 210−213.

(29) Leyre, S.; Coutino-Gonzalez, E.; Joos, J. J.; Ryckaert, J.; Meuret, Y.; Poelman, D.; Smet, P. F.; Durinck, G.; Hofkens, J.; Deconinck, G.; Hanselaer, P. Absolute Determination of Photoluminescence Quantum Efficiency Using an Integrating Sphere Setup. *Rev. Sci. Instrum.* **2014**, *85*, 123115.

(30) Ding, J.; Wu, Q.; Li, Y.; Long, Q.; Wang, Y.; Ma, X.; Wang, Y. $\alpha$-M₃B₂N₄ (M = Ca, Sr):Eu³⁺: A Nitride-Based Red Phosphor with a Sharp Emission Line and Broad Excitation Band Used for WLED. *J. Phys. Chem. C* **2017**, *121*, 10102−10111.

(31) Li, L.; Yang, P.; Chang, W.; Tang, X.; Li, C.; Zeng, Z.; Jiang, S.; Zhou, X. Multifunctional Broad-Band Excited Eu³⁺-Activated Fluorescent Materials for Potential Warm White Light-Emitting Diodes (w-LEDs) and Temperature Sensor Applications. *Adv. Powder Technol.* **2018**, *29*, 43−49.

(32) Blasse, G.; de Vries, J. On the Eu³⁺ Fluorescence of Mixed Metal Oxides. *J. Electrochem. Soc.* **1967**, *114*, 875−877.

(33) Bosze, E. J.; Hirata, G. A.; McKittrick, J. An Analysis of Y₂O₃:Eu³⁺ Thin Films for Thermographic Phosphor Applications. *J. Lumin.* **2011**, *131*, 41−48.

(34) Ward, L.; Agrawal, A.; Choudhary, A.; Wolverton, C. A General-Purpose Machine Learning Framework for Predicting Properties of Inorganic Materials. *npj Comput. Mater.* **2016**, *2*, 16028.

(35) Villars, O.; Cenzual, K. *Pearson's Crystal Data: Crystal Structure Database for Inorganic Compounds*; ASM International: Cleveland, OH, 2007.

(36) U.S. Department of Energy. *Solid-State Lighting 2017 Suggested Research Topics*; Washington, DC, 2017.

(37) Wang, Y.; Tang, K.; Zhu, B.; Wang, D.; Hao, Q.; Wang, Y. Synthesis and Structure of a New Layered Oxyfluoride Sr₂ScO₃F with Photocatalytic Property. *Mater. Res. Bull.* **2015**, *65*, 42−46.

(38) Wu, H.-Q.; Ju, P.; He, H.; Yang, B.-F.; Yang, G.-Y. Three New Mixed-Alkali-and Alkaline-Earth-Metal Borates: From 1D Chain to 2D Layer to 3D Framework. *Inorg. Chem.* **2013**, *52*, 10566−10570.

(39) ElBelghitti, A. A.; Elmarzouki, A.; Boukhari, A.; Holt, E. M. $\sigma$-Dibarium Pyrophosphate. *Acta Crystallogr., Sect. C: Cryst. Struct. Commun.* **1995**, *51*, 1478−1480.

(40) Emiraliev, A.; Kocharov, A. G.; Bakradze, R. V.; Karimov, U.; Ahmetzhanov, Z. I. The Neutron Diffraction Redefinition of the Coordinates of the Atoms of Oxygen in Yttrio-Aluminium Garnet. *Kristallografiya* **1976**, *21*, 211−213.

(41) Yanase, I.; Kobayashi, H.; Mitamura, T. Thermal Property and Phase Transition of the Synthesized New Cubic Leucite-Type Compounds. *J. Therm. Anal. Calorim.* **1999**, *57*, 695−705.

(42) Pązik, R.; Watras, A.; Macalik, L.; Dereń, P. J. One Step Urea Assisted Synthesis of Polycrystalline Eu³⁺ Doped KYP₂O₇ − Luminescence and Emission Thermal Quenching Properties. *New J. Chem.* **2014**, *38*, 1129.

(43) Lojpur, V.; Čulubrk, S.; Medić, M.; Dramicanin, M. Luminescence Thermometry with Eu³⁺ Doped GdAlO₃. *J. Lumin.* **2016**, *170*, 467−471.