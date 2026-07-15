Article

# Predicting Inorganic Photovoltaic Materials with Efficiencies >26% via Structure-Relevant Machine Learning and Density Functional Calculations

![](./images/812571283391774721_1.jpg)

Combining machine learning techniques and density functional theory calculations, Feng et al. predict four potential inorganic photovoltaic materials—$Ba_4Te_{12}Ge_4$, $Ba_8P_8Ge_4$, $Sr_8P_8Sn_4$, and $Y_4Te_4Se_2$—with power conversion efficiency exceeding 26%, comparable to the champion perovskite light-absorbing layers.

Hong-Jian Feng, Kan Wu, Zun-Yi Deng

hjfeng@nwu.edu.cn,
fenghongjian@126.com

## HIGHLIGHTS
Fast and atomic-level accuracy prediction of photovoltaic materials is proposed

The theoretical PCE exceeds 26%, comparable to the champion light-absorbing layer

Feng et al., Cell Reports Physical Science 1,
100179
September 23, 2020 © 2020 The Author(s).
https://doi.org/10.1016/j.xcrp.2020.100179

![](./images/812571283391774721_2.jpg)

# Predicting Inorganic Photovoltaic Materials with Efficiencies >26% via Structure-Relevant Machine Learning and Density Functional Calculations

Hong-Jian Feng,¹,²,* Kan Wu,¹ and Zun-Yi Deng¹

## SUMMARY
Discovering new inorganic photovoltaic materials becomes an efficient way for developing a new generation of solar cells with high efficiency and environmental stability. Using machine learning (ML) and density functional theory calculations, we report four promising inorganic photovoltaic materials—Ba₄Te₁₂Ge₄, Ba₈P₈Ge₄, Sr₈P₈Sn₄, and Y₄Te₄Se₂—demonstrating notable theoretical photovoltaic performance for use in solar cells. The symmetry-allowed optical transition probability, the large amount of density of states near the conduction band minimum (CBM) and the valence band maximum (VBM), and the strong p-p transition across the band edge contribute to the large optical absorption coefficient, leading to the outstanding theoretical power conversion efficiency (PCE). The separation of the VBM and CBM wave function distributions contribute to the fast separation of the photogenerated electrons and holes and the enhanced carrier lifetimes. Our ML model is an efficient method for fast and atomic-level accuracy prediction of photovoltaic materials with different crystal structures.

## INTRODUCTION
Discovering and screening new functional materials using the high-throughput method has become increasingly important for chemistry, materials science, medical science, and industrial applications. Due to the energy shortage and the environmental pollution caused by fossil fuels, green energy such as solar cells has drawn much attention in recent years. The new champion hybrid perovskite solar cells create a new record of 25.2% of power conversion efficiency (PCE),¹ making solar photovoltaics the focus of research again, especially in finding new, efficient light-absorbing materials. The long research cycle and waste involved in traditional photovoltaic research can be alleviated significantly by novel material discovery technologies; density functional theory (DFT) high-throughput calculations²,³ and the machine learning (ML)⁴,⁵ method have emerged in recent years, which dramatically increase the accuracy and efficiency of materials design and exploitation. Knowing the crystal structure and the atomic types, DFT calculations based on the Kohn-Sham equation⁶,⁷ can accurately predict the total energy and electronic states of the system, and thus derived quantities such as the interatomic force constant,⁸ electron and hole effective mass,⁹ carrier mobility,¹⁰ light-absorption coefficient,¹¹ optical transition probability,¹² and theoretical PCE for light-absorbing materials.¹³ The ground state property Kohn-Sham DFT calculation of a single compound usually requires several hours of processor time, and the computation time is highly demanding when the GW self-energy calculations and Heyd-Scuseria-Ernzerhof (HSE) hybrid functional are involved in the DFT calculations.

---

¹School of Physics, Northwest University, Xi'an 710127, China
²Lead Contact
*Correspondence:
hjfeng@nwu.edu.cn, fenghongjian@126.com
https://doi.org/10.1016/j.xcrp.2020.100179

![](./images/812571283391774721_3.jpg)

The ML technique is an effective approach to learn and recognize patterns and relationships between the targets and features of materials. ML can not only accelerate the discovery of new materials but it also has been successfully applied in predicting the electronic properties of materials, such as electronic density of states (DOS)¹⁴ and accelerating Kohn-Sham equation calculations.¹⁵ Therefore, ML can be a highly efficient and accurate method when combined with DFT calculations in materials discoveries. Decision tree (DT),¹⁶ neural networks (NNs),¹⁷ and deep learning (DL)¹⁸ methods have been successfully used in different areas of research, especially in the screening of photovoltaic materials. Except for the problem of overfitting, DT offers the fastest and most accurate prediction results compared with other ML algorithms. It is fortunate that the overfitting problem can be avoided by setting the number of nodes in the regression DT and limiting the depth of the model. The super-parameters can be set to limit the depth of weak learners in the gradient boosting regression (GBR)¹⁹ to avoid overfitting. The GBR algorithm is an ensemble ML algorithm, which combines several weak tree learners into a single strong learner and leads to good performance in various studies, especially photovoltaic material prediction and screening.²⁰,²¹

Features or attributes play a crucial role in the process of predicting the properties of new materials. Good features can precisely reflect the in-depth nature of the composition and the structure of the materials. They can reveal the buried relationship between the composition/structure and the target properties and render accurate ML results, hence becoming more important than the algorithm used in the ML prediction. Usually the elementary quantity or some derived physical quantities can be directly mapped into features that are able to describe the underlying physics in the target-driven prediction. Lu et al.²² selected 14 features of organic-inorganic perovskites (e.g., total number of ionic charges, $p$ orbital electrons, tolerance factors, octahedral factors) and trained the GBR model to screen the band gap of 5,158 hybrid organic-inorganic perovskites photovoltaic light-absorbing layer. Im et al.²³ selected 39 features and predicted the formation enthalpy and band gap of lead-free double perovskites. Using band gap as the dominant feature, Choudhary et al.²⁴ predicted the spectroscopic limited maximum efficiency (SLME) for 260 inorganic and organic light-absorbing materials with different structures. In addition, combining or building functions of elementary physical quantities, as well as generating new functions or matrix descriptors, can create good features and render accurate and efficient predictions of potential materials. Schütt et al.²⁵ predicted the DOS at the Fermi level of 7,264 materials from the Materials Project (MP) database by using the partial radial distribution function (PRDF), in which the distribution probability of the $eta$ particle in space around the $\alpha$ particle is defined. In addition, Faber et al.²⁶ used the Coulomb matrix (CM) to predict a band gap of 3,938 materials from the MP dataset. The shortcoming of the features used to train the model is that it is suitable only for the materials that have similar crystal structures corresponding to those trained in the ML prediction. The Voronoi tessellations method was proposed to partially solve this issue by building faces of the Voronoi polyhedral corresponding to the nearest neighbor of the atoms²⁷,²⁸ and was thus able to reflect the crystal structure and the local environment of the materials. Thanks to the Voronoi tessellations method, materials with different crystal structures can be dealt with unambiguously and predicted precisely via the ML method. To the best of our knowledge, the report on the ML prediction of inorganic solar cell materials with a wide variety of structures is very limited, although some works focused on the specific type of structures, such as hybrid perovskites and double perovskites, which have been extensively studied recently.²⁹,³⁰ It is highly desirable to predict the inorganic compounds possessing a wide variety of crystal structures and symmetries in a

database such as MP, which is generally considered to be more environmentally stable than the organic counterpart; for example, Si, GaAs, CdTe, and CIGS are always more stable than organic solar cells or hybrid perovskites. $^{30-33}$

In the present work, based on the Voronoi tessellations scheme, we adopted a training dataset that includes 2,398 inorganic light-harvesting materials possessing different crystal structures. Using the recursive feature elimination and cross-validation (RFECV) method, we performed a feature selection and retained 41 features for training. Four key features—fraction of p orbital valence, most of melting temperature, maximum of electronegativity, and mean of covalent radius—are highly relevant to the high photovoltaic performance of the candidate materials. A total of 3,587 inorganic materials with a wide variety of crystalline structures were screened based on the trained model. Four promising solar cell materials, $Y_4Te_4Se_2$, $Ba_4Te_{12}Ge_4$, $Sr_8P_8Sn_4$, and $Ba_8P_8Ge_4$, were predicted via the further DFT screening process with high atomic-level accuracy, i.e., structural stability, symmetry-induced optical transition probability, DOS analysis across the band edge, absorption coefficient, and theoretical PCE, which are considered to be the key parameters for solar cell applications.

# RESULTS AND DISCUSSION

## Prediction Strategy
Our screening framework is shown in Figure 1A. Our prediction framework consists of three consecutive parts: input dataset of high-throughput light-harvesting materials from the Computational Materials Repository (CMR), $^{34}$ the ML algorithm, and DFT calculations and screening. The suitable band gap (0.9–1.6 eV), higher thermal stability, higher absorption coefficient, and higher theoretical PCE (>20%) are the target properties for our ML prediction. The initial attributes or features were generated from the crystal structure of the input compounds. Then, the features were used to train and test the ML model. Figure 1B presents the feature engineering workflow. After the key attributes were obtained, the hyperparameters of the GBR algorithm were determined with 10-fold cross-validation procedures. K-fold cross-validation is a commonly used accuracy test method. It divides the initial data into K subsamples; a single subsample is retained as data for the verification model and the other K-1 samples are used for training. The advantage of this method is that the randomly generated subsamples are repeatedly used for training and verification, and the results are verified once each time. In our work, 10-fold cross-validation was selected to improve the prediction instability. Then, the GBR-based model was trained and evaluated. The trained model was used to predict the potential candidates from the 3,587 predictions dataset. After candidate materials were selected out from the prediction ML dataset, DFT calculations were used to determine the band gap, thermal stability, DOS, optical transition probability, absorption coefficient, and SLME, and to further unravel the in-depth origin and mechanism of the photovoltaic properties for the predicted outstanding candidates.

## Training and Prediction Dataset
The input dataset involves 2,398 photovoltaic materials. These materials come from the New Light Harvesting Materials project from the CMR database. Since these 2,398 materials have corresponding records in the MP, we can directly obtain the band gap of 2,398 materials in the MP. The band gap was obtained by high-throughput DFT calculations, $^{35}$ which can produce the same energy level with GW approximation to ensure the high accuracy of the input dataset. At the same time, we obtained the crystal structures of the 2,398 materials in the MP. The distribution of the crystalline structure in the band gap of the training dataset is demonstrated in Figure S1. To make the trained model fully structure correlated, the crystal structures

![](./images/812571283391774721_4.jpg)

![](./images/812571283391774721_5.jpg)

![](./images/812571283391774721_6.jpg)

of input materials, including binary, ternary, and quaternary compounds, are varied from cubic, tetragonal, orthorhombic, trigonal, hexagonal, and monoclinic to triclinic structures, covering all seven crystalline systems. The space group and the different crystal structures of the training dataset are shown in Figure 1C. When the GBR model is trained and evaluated, the input dataset is divided into two parts: the training set (80%) and the test set (20%).

We selected 29 potential solar materials with different crystal structures as the initial structures. The crystalline structures, space group, and compositions of the artificial materials in the prediction dataset are shown in Figure 2. We filled the sites with the same column elements in the periodic table and removed the initial 29 compounds and the well-known materials, which had already been experimentally prepared. With that, 3,587 theoretical materials were created and included in the prediction dataset.

## Features Optimization
Features should unambiguously describe the underlying relationship between the input data and the target properties. Thus, accurately building dominant features is more important than the creation of more features. Actually, the number of features must be less than the number of candidates in the input dataset because of the curse of dimensionality.³⁶ The features should be invariant with translational and rotational transformations. Based on the Voronoi tessellations, the weight of the attributes of each atom in the materials changes with the structure.²⁸ Thus, the features generated by Voronoi tessellation are able to represent the information about structure and inequivalent sites and be more accurate in describing compounds with a wider variety of crystal structures than other methods.²⁷

The feature engineering process is shown in the blue box in Figure 1B. The Voronoi tessellation method was used to generate an initial 271 features. To avoid problems of dimensionality, we used the RFECV method to eliminate redundant features that are not important.³⁷ For understanding the importance of each feature and recognizing the relationship between features and target properties, we evaluated the features via the GBR scheme, while adjusting the hyperparameters of the model. As shown in Figure 3A, 41 important features are listed and sorted by importance. It is worth noting that the fraction of the p orbital valence is a very important feature, and the feature importance percentage is 37.94%. The importance percentage of the fraction of the d orbital valence is 4.32%. In the section of DFT calculations, we notice that the both the p orbital and the d orbital are dominant in the conduction band minimum (CBM) and the valence band maximum (VBM), facilitating the strong p-p transition and the large absorption coefficient. Owing to the strong optical transition probability caused by the p-p transition, the p orbital is the prerequisite for the high-performance photovoltaic materials, while the d orbital also contributes to the optical transition and the photovoltaic performance.

In Figure 3A, we notice that the importance percentages of the maximum of electronegativity and the mean of electronegativity are 5.27% and 2.18%, respectively. Furthermore, the correlation coefficient between the maximum of electronegativity

### Figure 1. Architecture of the Optimized Workflow Used in This Study
(A) Process framework of finding promising light-harvesting materials with PCE > 20%. The black boxes denote the ML process. The DFT calculations are shown in the green box.
(B) ML flowchart. The blue box presents the feature engineering process, and the black box indicates the process of model training and evaluation.
(C) The space group and the wide variety of crystal structures for inorganic compounds being used in training the GBR model.

![](./images/812571283391774721_7.jpg)

<table><tbody><tr><td>1</td><td>SrO₂</td><td>I4/mmm</td><td>9</td><td>MgNa₂C₂O₆</td><td>R-3</td><td>16</td><td>Mo₈Rb₂S₆</td><td>P63/m</td><td>23</td><td>Hg₂P₂S₆</td><td>P-1</td></tr><tr><td>2</td><td>NaTiO₂</td><td>R-3m</td><td>10</td><td>Al₂YB₄O₁₂</td><td>R32</td><td>17</td><td>Ca₂Pd₃F₈</td><td>I4/mcm</td><td>24</td><td>Mg₄V₂O₁₁</td><td>P-1</td></tr><tr><td>3</td><td>Sr₂O₈Se₂</td><td>P121/m1</td><td>11</td><td>Ca₂LaB₂O₁₀</td><td>Cm</td><td>18</td><td>Ba₉As₅Ge₄</td><td>P21/c</td><td>25</td><td>Ag₂Cr₄O₁₂</td><td>P-1</td></tr><tr><td>4</td><td>KMgF₃</td><td>Pm-3m</td><td>12</td><td>Al₂Ca₂Li₃F₁₂</td><td>P-31c</td><td>19</td><td>Cs₂Pd₅Rb₂F₁₈</td><td>P4/mbm</td><td>26</td><td>Mg₂Rb₄Cl₁₂</td><td>P6₃/mmc</td></tr><tr><td>5</td><td>Ga₄Li₄S₆</td><td>Pna21</td><td>13</td><td>Ag₂Cu₂O₄</td><td>C2/m</td><td>20</td><td>Al₂Ba₂S₁₄</td><td>Pmn21</td><td>27</td><td>C₄Br₂I₅</td><td>Pnma</td></tr><tr><td>6</td><td>Cu₂K₂Ta₂Se₈</td><td>Anna2</td><td>14</td><td>Sc₄O₄S₂</td><td>P63/mmc</td><td>21</td><td>K₂PdBr₄</td><td>P4/mmm</td><td>28</td><td>Au₂I₂Te₄</td><td>P21/c</td></tr><tr><td>7</td><td>Nb₂Sr₂Y₂O₁₂</td><td>P121/n1</td><td>15</td><td>Ba₄O₁₂Si₄</td><td>P222</td><td>22</td><td>Be₈P₆</td><td>C2/c</td><td>29</td><td>Ga₂La₂Mn₂S₁₄</td><td>P63</td></tr><tr><td>8</td><td>SnTl₂As₂S₆</td><td>P-3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

**Figure 2. Materials Used in the Prediction Dataset**
The crystalline structure, space group, different sites occupied by the elements in the periodic table, and compositions for the 3,587 compounds in the prediction dataset.

and the band gap is 0.78, and that between the mean of electronegativity and the
band gap is 0.71, indicating the dominant role of these two features. The element
with high electronegativity in the compound influences more in the band gap than

![](./images/812571283391774721_8.jpg)

Figure 3. The Key Features and the Evaluation of the GBR Model
(A) The feature importance percentage.
(B) Heatmap of the correlation between each feature.
(C) Evaluation of the trained model.
(D) Layout of training set and test set.
(E) Comparison of the GBR with other methods in terms of accuracy and detection speed.

other elements. The relationship of the maximum of electronegativity and the band gap is almost positively correlated. From our analysis, whether or not a low electro-negativity atom exists in the compounds, the band gap becomes larger as long as a high electronegativity atom exists in the materials. For example, the fluorine atom rarely appears in high-performance photovoltaic materials.²⁴ Therefore, high elec-tronegativity elements were not considered in our prediction dataset due to the pos-itive correlation with the band gap. In Figure 3B, the correlation coefficients between pairs of features are shown as a heatmap. Most of the correlation coefficients are ~0, which indicates that redundant features are successfully removed. With that, the per-formance of the ML model can be greatly improved. In Figure 3D, we can see two

curves with almost the same trend. We arrange the input dataset from small to large and select them randomly by percentage. It can be seen that the training set and the test set have the same trend, indicating the randomness of the test set and the accuracy of the model. In Figure 3E, we used the same training set to train the rotation forest (RF), the kernel ridge regression (KRR),³⁸ the support vector regression (SVR), and the extreme tree regressor (ETR) method, and compared them with the GBR model to prove the feasibility of the model. By comparing the GBR with the training effects of the above four models, we can clearly find that GBR has the highest accuracy. Although the time taken by KRR, SVR, and ETR is relatively short, the accuracy is much lower than that of the GBR. Although the accuracy of the RF is close to that of the GBR, it takes a longer time, so GBR is a good choice.

## Model Analysis
There are multiple algorithms involved in the ML algorithm, such as support vector machines (SVMs),³⁹ NNs,⁴⁰ KRR, DT classifier (DTC),⁴⁰ and GBR. Because the overfitting can be alleviated by ensemble methods, we chose the GBR algorithm to predict the band gap in the prediction set. In this work, the Pearson correlation coefficient (r) and the coefficient of determinations ($R^{2}$) were calculated to estimate the prediction errors. The evaluation of the GBR model is shown in Figure 3C. The black line represents the reference line of perfect prediction. The blue dots from the test set surround the black line, indicating the accuracy of the trained model.

Finding the buried relationship between the features and the target properties is the main goal of the ML process. The distribution of band gap as a function of the four important features is shown in Figure 4. The underlying trend between the key features and the band gap can provide clues about the pattern that can be obtained or estimated from the trained model. One important parameter is the range of the key attributes that can be deduced from the pattern in the target-feature relationship. The band gap of predicted solar cell materials is between 0.9 and 1.6 eV, which permits the photons in the whole visible-light spectrum to be absorbed and tends to create the best PCE for photovoltaic cells where the open circuit voltage and short circuit current can be balanced at the premium value. This ideal band gap range can be used to estimate the corresponding data interval of the key features. For example, the fraction of the p orbital valence ranges from 0.01 to 0.56 in the black box in Figure 4A. The main distribution of this feature is shown by the green box. Thus, the best range of the fraction of the p orbital is between 0.06 and 0.33. Based on the same analysis, the corresponding value for most of the melting temperature, the maximum of electronegativity, and the mean of the covalent radius are illustrated in Figures 4B–4D, respectively. These criteria have been used as screening conditions in the prediction dataset. The other features do not show a clear pattern and provide the appropriate range used for prediction (the 37 feature-target correlations are shown in Figure S2).

## Screening Process
The trained GBR ML model was adopted to screen the potential candidates from the 3,587 inorganic materials in the prediction dataset (the screening process is shown in Figure S3). The band gap ranging from 0.9 to 1.6 eV was chosen as the first screening criterion because of the higher probability of PCE in the corresponding band gap interval. Therefore, 285 materials were screened out from the prediction dataset. To select candidate compounds that are stable and easy to synthesize and fabricate into photovoltaic devices, the formation enthalpy $\Delta H$ was chosen as the second screening parameter. The $\Delta H$ of the 285 materials (see full list in Table S1) were obtained from the Open Quantum Materials Database (OQMD).⁴¹ From previous statistics, the majority of the theoretical candidates considered to be potential photovoltaic materials have formation

![](./images/812571283391774721_9.jpg)

Figure 4. Data Visualization of the Training Set and the Test Set as Variation with the Band Gap
The green boxes represent the rational range for (A) fraction of the p orbital valence, (B) most of the melting temperature, (C) the maximum of electronegativity, and (D) the mean of covalent radius, respectively, in terms of the appropriate band gap.

enthalpy smaller than $-0.76$ eV/atom; the minority ($\Delta H > -0.76$ eV/atom) do not possess the appropriate band gap for solar cells. $^{23}$ Thus, adopting the criterion of $\Delta H < -0.76$ eV/atom, 63 materials were screened out further. The price of the materials and the ease of fabrication were taken as the third factor for further screening. Due to the expense of the compounds with some elements and the difficult synthesized conditions that are not suitable for solar cell fabrication, the compounds containing scandium, lanthanum, and tantalum are not considered in the following screening process. Therefore, six materials that met all of the above-mentioned requirements were finally selected out for DFT evaluation. Meanwhile, we also used SLME $> 20\%$ as the screening parameter to confirm the result in this step, $^{42}$ and the DFT calculations agree well with the ML prediction, indicating that our prediction method is at high atomic-level accuracy. Considering the SLME screened result, we took the six candidates as the input for the DFT evaluation.

It only takes a few seconds to screen out target materials via our GBR ML model. With the fast prediction speed and atomic-level accuracy achieved, our trained GBR model is more efficient than the DFT high-throughput calculations. Thus, this ML scheme is a convenient and low-cost route for discovering new light-harvesting inorganic materials with different crystal structures.

DFT Electronic and Photovoltaic Calculations
According to the crystal space group, we classified the six screened candidate materials into three groups: (1) $P21/c$ (no. 14), including $Ca_8As_8Sn_4$, $Sr_8P_8Sn_4$,

![](./images/812571283391774721_10.jpg)

![](./images/812571283391774721_11.jpg)

Figure 5. Variation of Free Energies from the Ab Initio Molecular Dynamics Simulation at 300 K
Variation of the free energies for (A) Ba₄Te₁₂Ge₄, (B) Ba₈P₈Ge₄, (C) Sr₈P₈Sn₄, and (D) Y₄Te₄Se₂. The insets show the corresponding structural evolution.

Sr₈As₈Sn₄, and Ba₈P₈Ge₄; (2) P63/mmc (no. 194), including Y₄Te₄Se₂; and (3) P222 (no. 16), including Ba₄Te₁₂Ge₄. Based on the DFT, we implemented ab initio molecular dynamics (AIMD) to screen their thermal stability. The results suggested that Ca₈As₈Sn₄ and Sr₈As₈Sn₄ are not capable of maintaining the original crystal structure (see Figures S4 and S5) and thus were excluded from the prediction and evaluation process. Therefore, only four materials—Ba₄Te₁₂Ge₄, Ba₈P₈Ge₄, Sr₈P₈Sn₄, and Y₄Te₄Se₂—were screened out, and the corresponding AIMD results are given in Figure 5. It can be seen that with constant-pressure Nosé-Hoover dynamics (NPT) calculation at 300 K, the total energies of four selected materials swing within a very narrow range. We also note that the Bravais lattice systems of three candidates (Ba₄Te₁₂Ge₄, Ba₈P₈Ge₄, and Y₄Te₄Se₂) are stable. Only that of Sr₈P₈Sn₄ (Figure 5C) slightly tilts after 2,000 fs. That indicates that the four candidates are roughly thermodynamically stable at room temperature. Furthermore, we demonstrate the electronic and photovoltaic properties, including the DOS, electronic band structure, and SLME in the following discussions.

All of the calculations of electronic and optical properties for the six selected materials were performed with the HSE06 + GGA exchange-correlation functional⁴³,⁴⁴ and projector-augmented wave (PAW) scheme.⁴⁵ Figure 6 shows the DOS of four thermodynamically stable materials (Ba₄Te₁₂Ge₄, Ba₈P₈Ge₄, Sr₈P₈Sn₄, and Y₄Te₄Se₂). The VBM and CBM of Ba₄Te₁₂Ge₄ are mainly contributed by the p orbital of Te, but these Te atoms are inequivalent (Figure 6A). For Ba₈P₈Ge₄, the VBM is contributed by the d orbital of Ba and the p orbital of P and Ge, while the CBM is dominated by the p orbital of P and Ge atoms (Figure 6B). Specifically, the large DOS at the band edge indicates that the more photoinduced electrons can be generated and transformed between the edge bands. The VBM of Sr₈P₈Sn₄ is mainly contributed by the p orbitals of P and Sn, while the CBM is dominated by the p orbital of P and the d orbital of Sr (Figure 6C). The electronic structure of Y₄Te₄Se₂ is shown in Figure 6D, the VBM is contributed by the p orbital of Te, and the CBM is dominated by the d orbital of Y. (The DOS of the two predicted unstable materials are shown as Figures S6 and S7.)

![](./images/812571283391774721_12.jpg)

Figure 6. DOS for the Four Predicted Materials
DOS of (A) $Ba_4Te_{12}Ge_4$, (B) $Ba_8P_8Ge_4$, (C) $Sr_8P_8Sn_4$, and (D) $Y_4Te_4Se_2$. The insets show the corresponding wave function distribution for the VBM and CBM.

Therefore, it can be concluded that for these materials, the VBM and CBM are mainly contributed by $p$ orbital electrons, suggesting that the abundant $p$-$p$ transitions arise between the edge bands. The analogous phenomenon is also observed in the perovskite $ABX_3$ (X = Cl, Br, I) system, $^{46-48}$ where the CBM is contributed by the $p$ orbital of the B site atom, and the VBM is mainly dominated by the $p$ orbital of the X site atom and partly dominated by the $s$ orbital of the B site atom. Moreover, the CBM- and VBM-associated charge densities distribute throughout the whole crystal, which suggests high electronic dimensionality. This offers the smooth carrier flowing pathway, $^{49}$ enhancing the carrier's separation and providing the opportunity for high photovoltaic performance. It is worth noting that the separation of CBM and VBM wave function demonstrates the fast decoherence of the states, and thus the efficient charge separation and enhancement of the carrier lifetime in the system.

Figure 7 shows the electronic band structure and transition probabilities. The transition peak of $P^2$ appears at the high symmetry point corresponding to the VBM or CBM and can reflect the parity-allowed optical transition probability and the light absorption intensity. For $Ba_4Te_{12}Ge_4$, the band opens a direct gap at $T$ point, where the $P^2$ is relatively large, suggesting that the large electronic transition appears between the CBM and VBM (Figure 7A). A similar phenomenon is observed in the case of $Y_4Te_4Se_2$, where the VBM and CBM is at $\Gamma$ point, and simultaneously the electronic transition is allowed near the $\Gamma$ point. In contrast, $Ba_8P_8Ge_4$ and $Sr_8P_8Sn_4$ are indirect band gap materials. For $Ba_8P_8Ge_4$, the peak of $P^2$ is at $\Gamma$ point, but the CBM is at another point, resulting in the electronic transition from VBM to CBM through electron relaxation in the direction of the red arrow shown in Figure 7B. During the relaxation, part of the energy (~0.21 eV) is dissipated as heat. For $Sr_8P_8Sn_4$, there also exists an indirect transition (see Figure 7C). However, a peak

![](./images/812571283391774721_13.jpg)

Figure 7. Band Structures, Transition Probabilities $P^{2}$ at Each K Point, and the Corresponding Crystal Structures
Band structures, $P^{2}$, and crystal structures for (A) $Ba_{4}Te_{12}Ge_{4}$, (B) $Ba_{8}P_{8}Ge_{4}$, (C) $Sr_{8}P_{8}Sn_{4}$, and (D) $Y_{4}Te_{4}Se_{2}$.

of $P^{2}$ appears at Figure 7B point Figure 7. An energy of 0.15 eV dissipates as heat during the electron excitation, which is smaller than that of $Ba_{8}P_{8}Ge_{4}$. Therefore, we speculate that $Ba_{4}Te_{12}Ge_{4}$ and $Y_{4}Te_{4}Se_{2}$ are more suitable as candidates for photovoltaic conversion materials, which can be confirmed in the following theoretical PCE calculation. (The electronic band structure and transition probabilities of the two predicted unstable materials are shown as Figures S8 and S9.)

As is known, $MAPbI_{3}$, with excellent and outstanding photovoltaic performance, is a champion material for solar cells. Figure 8A shows the calculated photon absorption spectra of four candidates, with the spectra of $MAPbI_{3}$ as a comparison. The four candidates exhibit excellent light-absorption characteristics in the visible light, meanwhile possessing the same order of magnitude at $10^{5}\ cm^{-1}$ as that of $MAPbI_{3}$. The theoretical PCE of four candidates are larger, at 23%, and $Ba_{4}Te_{12}Ge_{4}$, $Sr_{8}P_{8}Sn_{4}$, and $Y_{4}Te_{4}Se_{2}$ possess PCE exceeding 26%, which is approaching the champion perovskite solar materials. In addition, there exist sharp increments in the SLME curves with increases in film thickness, and the PCE approximately reaches the saturation value as the film thickness exceeds 500 nm (Figure 8B). The SLMEs for $Ba_{4}Te_{12}Ge_{4}$, $Sr_{8}P_{8}Sn_{4}$, and $Y_{4}Te_{4}Se_{2}$, with film thicknesses exceeding 500 nm, are beyond 26%, as shown in Table S2, which possibly results from their band gap being closer to the band gap value identified by the Shockley-Queisser limit (1.34 eV); this causes these materials to have the ability to capture more photons in the visible light spectrum.⁵⁰ Therefore, the three candidates ($Ba_{4}Te_{12}Ge_{4}$, $Sr_{8}P_{8}Sn_{4}$, and $Y_{4}Te_{4}Se_{2}$), especially the two direct band gap candidates, which have the higher optical transition probability and the optimal band gap, have been predicted with promising photovoltaic performance for solar cells.

In summary, combining the ML technique and the DFT calculation, using 3,587 materials with different crystalline structures in the prediction dataset, we successfully predicted four potential materials ($Ba_{4}Te_{12}Ge_{4}$, $Ba_{8}P_{8}Ge_{4}$, $Sr_{8}P_{8}Sn_{4}$, and

![](./images/812571283391774721_14.jpg)

Figure 8. Photon Absorption Spectra and SLME.
(A) Photon absorption spectra for $Ba_4Te_{12}Ge_4$, $Ba_8P_8Ge_4$, $Sr_8P_8Sn_4$, and $Y_4Te_4Se_2$.
(B) SLME at 300 K and within the Shockley-Queisser model for $Ba_4Te_{12}Ge_4$, $Ba_8P_8Ge_4$, $Sr_8P_8Sn_4$, and $Y_4Te_4Se_2$.

$Y_4Te_4Se_2$) that possess higher PCEs exceeding 26%, which is comparable to the champion perovskite light-absorbing layer. The Voronoi tessellation method has been implemented to extract structure-relevant features or descriptors for our GBR-based ML model. The trained GBR model is capable of providing high atomic-level-accuracy prediction results, which is comparable to the DFT calculations. It is worth noting that the prediction time is only a few seconds, dramatically faster than the traditional DFT high-throughput calculations. The excellent photovoltaic performance is deeply related to the large amount of DOS in the band edge, the strong $p$-$p$ transitions allowed by the symmetry, the efficient separation of photogenerated electrons and holes, and the longer carrier lifetime, and thus the excellent theoretical PCE confirmed by the DFT calculations.

## EXPERIMENTAL PROCEDURES

### Resource Availability

#### Lead Contact
Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Prof. Hong-Jian Feng (hjfeng@nwu.edu.cn; fenghongjian@126.com).

#### Materials Availability
This study did not generate new unique reagents.

#### Data and Code Availability
The authors declare that data supporting the findings of this study are available within the article and the Supplemental Information. All other data are available from the Lead Contact upon reasonable request.

### Gradient-Boosted Regression
GBR,¹⁹ an ensemble ML algorithm, used gradient boosting in the scikit-learn package,³⁶ combining several weak tree learners into a strong learner. Within the GBR algorithm, the model will be trained M times, and the weak learner $T$ will be produced each time. The final algorithm is obtained by a weighted sum from several weak tree learners:

$$
F_M(x) = \sum_{m=1}^M T(x, \theta_m), \qquad \text{(Equation 1)}
$$


where m is the number of weak learners, x is the training data, and $\theta_m$ is the distribution weight vector.

Loss function is calculated as

$$
\hat{\theta}_{m}=\arg _{\theta_{m}} \min \sum_{i=1}^{N} L\left(y_{i}, F_{m-1}\left(x_{i}\right)+T\left(x_{i}, \theta_{m}\right)\right),
$$

(Equation 2)

Where $F_{m-1}$ $(x_i)$ corresponds to the current model. By minimizing the empirical risk, GBR adjusts parameters, which are applied to the next weak tree learner to improve the accuracy of the final model.

### Voronoi Tessellation
The Voronoi tessellation method can split the crystal into small cages, which are similar to Wigner-Seitz cells, and the shape of these small cages is relevant to the nearest-neighbor atoms. The tessellation depends only on the crystal structure, but is not much affected by the unit cell used. The faces of the Voronoi polyhedron are relevant to the nearest-neighbor atoms, where they are formed. Thus, the Voronoi tessellation method provides a clear definition for describing the local crystalline structure of materials and can recognize the differences in structural change for the materials with a wide variety of crystal structures. Structural attributes, such as effective coordination number, structural heterogeneity, chemical ordering, maximum packing efficiency, local environment, and compositional attributes, are involved in the Voronoi tessellation method to fully describe the structure and composition of the materials. $^{27,28}$

### DFT Calculations
All first-principles calculations were carried out using the PAW method $^{45}$ with the generalized gradient approximation (GGA), $^{51}$ implemented in the PWmat package. $^{52}$ The electronic properties were computed using one unit cell with periodic boundary conditions. The cutoff energy for the plane-wave basis was set at 400 eV. The structure was optimized until an energy-convergence threshold of $10^{-5}$ eV was reached using a $2 \times 2 \times 2$ M-P mesh and atomic force $<0.01$ eV/Å. To confirm dynamic stability, we performed AIMD simulations in 5,000 fs, with the step of 1 fs for the $2 \times 2 \times 2$ supercell. The temperature was controlled at 300 K by using the constant-pressure NPT method.

### Absorption Coefficient
To obtain more precise results, the optical properties were calculated by setting three times as many empty conduction bands as occupied valence bands. The imaginary part is calculated by $^{24}$:

$$
\begin{aligned}
\varepsilon_{\alpha \beta}^{(2)}(E) &=\frac{4 \pi^{2} e^{2}}{\Omega^{2}} \lim _{q \rightarrow 0} \frac{1}{q^{2}} \sum_{c, v, \vec{K}} 2 \omega \rightarrow \delta\left(\zeta_{c \vec{K}}-\zeta_{v \vec{K}}-E\right) \\
& \times\left\langle\Psi_{c \vec{K}+\vec{e}_{\alpha q}}\left|\Psi_{v \vec{K}}\right\rangle\left\langle\Psi_{v \vec{K}}\right| \Psi_{c \vec{K}+\vec{e}_{\beta q}}\right\rangle^{*},
\end{aligned}
$$

(Equation 3)

The matrix elements on the right side of Equation 3 capture the transitions allowed by structural symmetry and selection rules. The real part of dielectric tensor $\varepsilon_{\alpha \beta}^{(1)}$ is obtained by the usual Kramers-Kronig transformation $^{24}$,

$$
\varepsilon_{\alpha \beta}^{(1)}(E)=1+\frac{2}{\pi} P \int_{0}^{\infty} \frac{\varepsilon_{\alpha \beta}^{(2)}\left(E^{\prime}\right) E^{\prime}}{\left(E^{\prime}\right)^{2}-E^{2}+i \eta} d E^{\prime},
$$

(Equation 4)

where $\eta$ is the complex shift parameter. We use the crystallographic average of the dielectric function $(\varepsilon^{(1)}$ and $\varepsilon^{(2)})$ by diagonalizing the dielectric tensor for each energy and averaging the diagonal elements. That is, using $\varepsilon^{(1)}$ and $\varepsilon^{(2)}$, the absorption coefficient $\alpha(E)$ is defined as

$$
\alpha(E)=\frac{2 E}{\hbar c} \sqrt{\frac{\sqrt{\left(\varepsilon^{(1)}(E)\right)^{2}+\left(\varepsilon^{(2)}(E)\right)^{2}}-\left(\varepsilon^{(1)}(E)\right)}{2}},
$$

(Equation 5)

where $c$ is the speed of light.

### SLME
To maximize the power density, the SLME $\eta$ is defined as $^{24}$:

$$
\eta=\frac{P_{\max }}{P_{i n}}=\frac{\max \left\{\left(J_{s c}-J_{0}\left(e^{e V / k T}-1\right)\right) V\right\}_{V}}{\int_{0}^{\infty} E I_{s u n}(E) d E},
$$

(Equation 6)

Therefore, $\eta$ is the ratio of the maximum output power density $P_{max}$ and the total incident solar energy density $P_{in}$. We assume that the solar cell is illuminated under the photo flux $I_{sun}$ and can be approximated as an ideal diode; that is, the temperature $T$, current density $J$, and voltage $V$ follow

$$
J=J_{s c}-J_{0}\left(e^{e V / k T}-1\right),
$$

(Equation 7)

where $J_{sc}$ is the short-circuit current density, and

$$
J_{s c}=e \int_{0}^{\infty} a(E) I_{s u m}(E) d E,
$$

(Equation 8)

Where $a(E)$ is the calculated photon absorptivity, $e$ is the elementary charge, and $I_{sun}$ is the AM 1.5 G solar spectrum. $^{53}$

The reverse saturation current $J_0$ includes the radiative current $J_0^r$ and nonradiative current $J_0^{nr}$,

$$
J_{0}=J_{0}^{r}+J_{0}^{n r}=\frac{J_{0}^{r}}{f_{r}},
$$

(Equation 9)

where

$$
J_{0}^{r}=e \pi \int_{0}^{\infty} a(E) I_{b b}(E, T) d E,
$$

(Equation 10)

and the fraction of radiative recombination current $f_r$ is given by

$$
f_{r}=e^{\left(E_{g}-E_{g}^{d a} / k T\right)},
$$

(Equation 11)

where $E_g$ is the electronic band gap, $E_g^{da}$ is the direct-allowed optical band gap, and $I_{bb}$ is the black-body spectrum at temperature T.

### SUPPLEMENTAL INFORMATION
Supplemental Information can be found online at https://doi.org/10.1016/j.xcrp.2020.100179.

### ACKNOWLEDGMENTS
H.-J.F. was financially supported by the National Natural Science Foundation of China (NSFC) under grant nos. 51972266, 51672214, 11304248, and 11247230;

the Natural Science Basic Research Plan in Shaanxi Province of China (program no.
2014JM1014); the Scientific Research Program Funded by Shaanxi Provincial Educa-
tion Department (program no. 2013JK0624); the Fund Program for the Scientific Ac-
tivities of Selected Returned Overseas Professionals in Shaanxi Province of China;
and the Youth Bai-Ren Project in Shaanxi Province of China. We thank Ping Ma
and Shanshan Lu for useful discussions during the revision of the manuscript.

## AUTHOR CONTRIBUTIONS
H.-J.F. conceived the idea and proposed the theoretical design. H.-J.F. wrote the
manuscript. H.-J.F. and K.W. performed the ML and DFT calculations and analyzed
the results. Z.-Y.D. analyzed part of the DFT calculation results.

## DECLARATION OF INTERESTS
The authors declare no competing interests.

Received: May 12, 2020
Revised: July 13, 2020
Accepted: July 30, 2020
Published: September 2, 2020; Corrected online September 30, 2020

## REFERENCES
1. National Renewable Energy Laboratory. Best Research-Cell Efficiency Chart. https://www. nrel.gov/pv/cell-efficiency.html.

2. Sun, W., Zheng, Y., Yang, K., Zhang, Q., Shah, A.A., Wu, Z., Sun, Y., Feng, L., Chen, D., Xiao, Z., et al. (2019). Machine learning-assisted molecular design and efficiency prediction for high-performance organic photovoltaic materials. Sci. Adv. 5, eaay4275.

3. Hieulle, J., Wang, X., Stecker, C., Son, D.Y., Qiu, L., Ohmann, R., Ono, L.K., Mugarza, A., Yan, Y., and Qi, Y. (2019). Unraveling the impact of halide mixing on perovskite stability. J. Am. Chem. Soc. 141, 3515-3523.

4. Chang, S., Cohen, T., and Ostdiek, B. (2018). What is the machine learning? Phys. Rev. D 97, 056009.

5. Legrain, F., Carrete, J., van Roekeghem, A., Madsen, G.K.H., and Mingo, N. (2018). Materials screening for the discovery of new Half-Heuslers: machine learning versus ab initio methods. J. Phys. Chem. B 122, 625-632.

6. Kresse, G., and Furthmüller, J. (1996). Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 6, 15-50.

7. Kresse, G., and Furthmüller, J. (1996). Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B Condens. Matter 54, 11169-11186.

8. Urcelay, F., Toro-Labbé, A., and Gutiérrez- Oliva, S. (2020). Spectral decomposition of the reaction force constant. J. Phys. Chem. A 124, 2372-2379.

9. Sasaki, A. (1984). Effective-mass superlattice. Phys. Rev. B Condens. Matter 30, 7016-7020.

10. Hunter, L.P. (1953). Current carrier mobility ratio in semiconductors. Phys. Rev. 91, 579-581.

11. Zhao, X.-G., Yang, D., Sun, Y., Li, T., Zhang, L., Yu, L., and Zunger, A. (2017). Cu-In halide perovskite solar absorbers. J. Am. Chem. Soc. 139, 6718-6725.

12. Meng, W., Wang, X., Xiao, Z., Wang, J., Mitzi, D.B., and Yan, Y. (2017). Parity-forbidden transitions and their impact on the optical absorption properties of lead-free metal halide perovskites and double perovskites. J. Phys. Chem. Lett. 8, 2999-3007.

13. Yu, L., and Zunger, A. (2012). Identification of potential photovoltaic absorbers based on first-principles spectroscopic screening of materials. Phys. Rev. Lett. 108, 068701.

14. Mosconi, E., Grancini, G., Roldán-Carmona, C., Gratia, P., Zimmermann, I., Nazeeruddin, M.K., and Angelis, F.D. (2016). Enhanced TiO₂/ MAPbI₃ electronic coupling by interface modification with PbI₂. Chem. Mater. 28, 3612-3615.

15. Brockherde, F., Vogt, L., Li, L., Tuckerman, M.E., Burke, K., and Müller, K.R. (2017). Bypassing the Kohn-Sham equations with machine learning. Nat. Commun. 8, 872-881.

16. Gu, G.H., Noh, J., Kim, I., and Jung, Y. (2019). Machine learning for renewable energy materials. J. Mater. Chem. A Mater. Energy Sustain. 7, 17069.

17. Montavon, G., Samek, W., and Müller, K.R. (2018). Methods for interpreting and understanding deep neural network. Digit. Signal Process. 73, 1-15.

18. LeCun, Y., Bengio, Y., and Hinton, G. (2015). Deep learning. Nature 521, 436-444.

19. Truccolo, W., and Donoghue, J.P. (2007). Nonparametric modeling of neural point processes via stochastic gradient boosting regression. Neural Comput. 19, 672-705.

20. Scherbela, M., Hörmann, L., Jeindl, A., Obersteiner, V., and Hofmann, O.T. (2018). Charting the energy landscape of metal/ organic interfaces via machine learning. Phys. Rev. M 2, 043803.

21. Xu, Q., Li, Z., Liu, M., and Yin, W.-J. (2018). Rationalizing perovskite data for machine learning and materials design. J. Phys. Chem. Lett. 9, 6948-6954.

22. Lu, S., Zhou, Q., Ouyang, Y., Guo, Y., Li, Q., and Wang, J. (2018). Accelerated discovery of stable lead-free hybrid organic-inorganic perovskites via machine learning. Nat. Commun. 9, 3405-3412.

23. Im, J., Lee, S., Ko, T.W., Kim, H.W., Hyon, Y.K., and Chang, H. (2019). Identifying Pb-free perovskites for solar cells by machine learning. npj Comput Mater. 5, 37-44.

24. Choudhary, K., Bercx, M., Jiang, J., Pachter, R., Lamoen, D., and Tavazza, F. (2019). Accelerated discovery of efficient solar-cell materials using quantum and machine-learning methods. Chem. Mater. 31, 5900-5908.

25. Schütt, K.T., Glawe, H., Brockherde, F., Sanna, A., Müller, K.R., and Gross, K.U. (2014). How to represent crystal structures for machine learning: towards fast prediction of electronic properties. Phys. Rev. B Condens. Matter Mater. Phys. 89, 205118.

26. Faber, F., Lindmaa, A., Lilienfeld, O.A., and Armiento, R. (2015). Crystal structure representations for machine learning models of formation energies. Int. J. Quantum Chem. 115, 1094-1101.

27. Ward, L., Agrawal, A., Choudhary, A., and Wolverton, C. (2016). A general-purpose machine learning framework for predicting properties of inorganic materials. npj Comput Mater. 2, 16028-16034.

28. Ward, L., Liu, R., Krishna, A., Hegde, V.I., Agrawal, A., Choudhary, A., and Wolverton, C. (2017). Including crystal structure attributes in machine learning models of formation energies via Voronoi tessellations. Phys. Rev. B 96, 024104.

29. Castelli, I.E., Thygesen, K.S., and Jacobsen, K.W. (2015). Calculated optical absorption of different perovskite phases. J. Mater. Chem. A Mater. Energy Sustain. 3, 12343–12349.

30. Nguyen, B.-M., Swartzentruber, B., Ro, Y.G., and Dayeh, S.A. (2015). Facet-selective nucleation and conformal epitaxy of Ge shells on Si nanowires. Nano Lett. 15, 7258–7264.

31. Yan, L., and You, W. (2013). Real function of semiconducting polymer in GaAs/polymer planar heterojunction solar cells. ACS Nano 7, 6619–6626.

32. Bang, J.H., and Kamat, P.V. (2009). Quantum dot sensitized solar cells. A tale of two semiconductor nanocrystals: CdSe and CdTe. ACS Nano 3, 1467–1476.

33. Singh, A., Coughlan, C., Laffir, F., and Ryan, K.M. (2012). Assembly of CuIn(1-x)Ga(x)S2 nanorods into highly ordered 2D and 3D superstructures. ACS Nano 6, 6977–6983.

34. Computational Materials Repository. https://cmr.fysik.dtu.dk.

35. Castelli, I.E., Hüser, F., Pandey, M., Li, H., Thygesen, K.S., Seger, B., Jain, A., Persson, K.A., Ceder, G., and Jacobsen, K.W. (2014). New light-harvesting materials using accurate and efficient bandgap calculations. Adv. Energy Mater. 5, 1400915–1400921.

36. Bishop, C.M., and Nasrabadi, N.M. (2016). Pattern Recognition and Machine LearningVolume 14 (Springer).

37. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., et al. (2011). Scikit-learn: Machine Learning in Python. J. Mach. Learn. Res. 12, 2825–2830.

38. Zhuo, Y., Mansouri Tehrani, A., and Brgoch, J. (2018). Predicting the band gaps of inorganic solids by machine learning. J. Phys. Chem. Lett. 9, 1668–1673.

39. Mammone, A., Turchi, M., and Cristianini, N. (2009). Support vector machines. Wiley Interdiscip. Rev. Comput. Stat. 1, 83–289.

40. Fanourgakis, G.S., Gkagkas, K., Tylianakis, E., and Froudakis, G.E. (2020). A universal machine learning algorithm for large-scale screening of materials. J. Am. Chem. Soc. 142, 3814–3822.

41. Kirklin, S., Saal, J.E., Meredig, B., Thompson, A., Doak, J.W., Aykol, M., Ruhl, S., and Wolverton, C. (2015). The open quantum materials database (OQMD): assessing the accuracy of DFT formation energies. npj Comput. Mater. 1, 15010.

42. Li, S.X., Li, C.Z., Shi, M.M., and Chen, H.Z. (2020). New phase for organic solar cell research: emergence of Y-Series electron acceptors and their perspectives. ACS Energy Lett. 5, 1554–1567.

43. Schlipf, M., Betzinger, M., Friedrich, C., Ležaić, M., and Blügel, S. (2011). HSE hybrid functional within the FLAPW method and its application to GdN. Phys. Rev. B Condens. Matter Mater. Phys. 84, 125142.

44. Deák, P., Aradi, B., Frauenheim, T., Janzén, E., and Gali, A. (2010). Accurate defect levels obtained from the HSE06 range-separated hybrid functional. Phys. Rev. B Condens. Matter Mater. Phys. 81, 153203.

45. Blöchl, P.E. (1994). Projector augmented-wave method. Phys. Rev. B Condens. Matter 50, 17953–17979.

46. Pazoki, M., Jacobsson, T.J., Kullgren, J., Johansson, E.M., Hagfeldt, A., Boschloo, G., and Edvinsson, T. (2017). Photoinduced stark effects and mechanism of Ion displacement in perovskite solar cell materials. ACS Nano 11, 2823–2834.

47. Fu, Y., Zhu, H., Stoumpos, C.C., Ding, Q., Wang, J., Kanatzidis, M.G., Zhu, X., and Jin, S. (2016). Broad wavelength tunable robust lasing from single-crystal nanowires of cesium lead halide perovskites (CsPbX₃, X = Cl, Br, I). ACS Nano 10, 7963–7972.

48. Mao, X., Sun, L., Wu, T., Chu, T.-S., Deng, W.-Q., and Han, K.-L. (2018). First-principles screening of all-inorganic lead-free ABX₃ perovskites. J. Phys. Chem. C 122, 7670–7675.

49. Xiao, Z.-W., Meng, W.-W., Wang, J.-B., Mitzi, D.B., and Yan, Y.-F. (2017). Searching for promising new perovskite-based photovoltaic absorbers: the importance of electronic dimensionality. Mater. Horiz. 4, 206–216.

50. Shockley, W., and Queisser, H.J. (1961). Detailed balance limit of efficiency of p-n junction solar cells. J. Appl. Physiol. 32, 510–519.

51. Perdew, J.P., Burke, K., and Ernzerhof, M. (1996). Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865–3868.

52. Jia, W., Fu, J., Cao, Z., Wang, L., Chi, X., Gao, W., and Wang, L.W. (2013). The analysis of a plane wave pseudopotential density functional theory code on a GPU machine. Comput. Phys. Commun. 184, 9–18.

53. Collins, D.G., Blättner, W.G., Wells, M.B., and Horak, H.G. (1972). Backward monte carlo calculations of the polarization characteristics of the radiation emerging from spherical-shell atmospheres. Appl. Opt. 11, 2684–2696.

Cell Reports Physical Science 1, 100179, September 23, 2020 17