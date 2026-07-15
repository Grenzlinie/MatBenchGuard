# Predicting Phase Behavior of Linear Polymers in Solution Using Machine Learning

Jeffrey G. Ethier, Rohan K. Casukhela, Joshua J. Latimer, Matthew D. Jacobsen, Boris Rasin, Maneesh K. Gupta, Luke A. Baldwin, and Richard A. Vaia*

Cite This: *Macromolecules* 2022, 55, 2691−2702
Read Online

ACCESS | Metrics & More | Article Recommendations | Supporting Information

![](./images/812514987711922177_1.jpg)

ABSTRACT: The phase behavior of polymers in solution is crucial to many applications in polymer processing, synthesis, self-assembly, and purification. Quantitative prediction of polymer solubility space for an arbitrary polymer−solvent pair and across a large composition range is challenging. Qualitative agreement is provided by many current theoretical models, but only a portion of the phase space is quantitatively predicted. Here, we utilize a curated database for binary polymer solutions comprised of 21 linear polymers, 61 solvents, and 97 unique polymer−solvent combinations (6524 cloud point temperatures) to construct phase diagrams from machine learning predictions. A generalizable feature vector is developed that includes component descriptors concatenated with state variables and an experimental data descriptor (phase direction). The impact of several types of descriptors (Morgan fingerprints, molecular descriptors, and Hansen solubility parameters) to encode polymer−solvent interactions is assessed. Hansen solubility parameters are also introduced as a means to understand the general breadth of the linear polymer−solvent space as well as the density and distribution of curated data. Two common regression algorithms (XGBoost and neural networks) establish the generality of the descriptors; provide a root mean squared error (RMSE) within 3 °C for predicted cloud points in the test set; and offer excellent agreement with upper and lower critical solubility curves, isopleths, and closed-loop phase behavior by a single model. The ability to extrapolate to polymers that are very dissimilar from the curated data is poor, but with as little as 20 cloud points or a single phase boundary, RMSE error of predictions are within 5 °C. This implies that the current model captures aspects of the underlying physics and can readily exploit correlations to reduce required data for additional polymer−solvent pairs. Finally, the model and data are accessible via the Polymer Property Predictor and Database (3PDb).

## INTRODUCTION

The phase behavior of binary linear polymer−solvent solutions is critical to the success of processing, purification, self-assembly, and synthesis of polymer materials. For instance, in applications such as drug-delivery or the paint and coatings industry, polymer−solvent miscibility is determined based on the relative “distance” between solubility parameters such as the Hildebrand or Hansen solubility parameters (HSPs). $^{1−3}$ The miscible−immiscible boundary (i.e., cloud point), however, depends on many factors other than polymer−solvent chemistry, such as molecular weight, polydispersity, concentration, and pressure. It is well-known that increasing polymer molecular weight (or decreasing pressure) can shift the upper critical solubility (UCS) to higher temperatures and the lower critical solubility (LCS) to lower temperatures, decreasing the area of complete miscibility.⁴ In some cases, hourglass and closed-loop phase behavior can be found such as with polystyrene in acetone/propionitrile $^{5,6}$ (a polymer in a

Received: February 1, 2022
Revised: March 9, 2022
Published: March 24, 2022

![](./images/812514987711922177_2.jpg)

© 2022 American Chemical Society
2691
https://doi.org/10.1021/acs.macromol.2c00245
*Macromolecules* 2022, 55, 2691−2702

poor solvent) or poly(ethylene glycol) in water (a polymer in a good solvent), $^{7,8}$ respectively.

The thermodynamics behind phase separation in binary polymer solutions is generally understood $^{9}$ and depends on both entropic (polymer size) and enthalpic (monomer solvent interaction) contributions. Predictions of the polymer−solvent phase space as a function of concentration, polymer molecular weight, temperature, and pressure can be estimated using lattice models such as Flory $^{10,11}$ and Huggins $^{12,13}$ (commonly referred to as Flory−Huggins theory) or modified versions thereof. $^{14−16}$ However, these models often provide poor quantitative predictions away from the critical point in $T-\phi$ space. Additionally, the Flory−Huggins $\chi$ parameter must be measured experimentally as a function of temperature, pressure, and concentration for each polymer−solvent system. $^{17,18}$ These measurements are more complex than determining cloud point curves. Also, since $\chi$ is dependent on the polymer−solvent system, this suggests that not all of the thermodynamics are captured using such models. If a single model could estimate the temperature at which any polymer phase separates from any solvent, the formulation of synthesis, processing, and self-assembly methods would be substantially more efficient.

The use of machine learning (ML) in polymer science is increasing exponentially. $^{19−21}$ Data extraction and access to polymer databases are becoming more widespread, allowing the use of ML to assist in the design of new polymer materials. For instance, predicting glass transition temperature, $^{22−24}$ thermal conductivity, $^{25}$ and mechanical properties $^{26}$ has recently been of interest. It has also been demonstrated that ML models can assist in the design of new polymers with targeted properties. $^{27,28}$ To ensure reliable ML models, the quality of data and the set of descriptors used to structure the input to the model should be appropriately considered. This was recently demonstrated with glass transition temperature predictions, where a comprehensive study showed that the choice of polymer structure representation affected model performance. $^{24}$ Hence, clarifying the most important descriptors in the feature vector can help curate the data set and accelerate additional data collection. For example, encoding a molecule structure into a topological fingerprint (which encodes the arrangement of atoms in a molecule's structure) may suffice for screening a large selection of molecule candidates by similarity $^{29}$ but requires the curation of larger data sets to reveal chemical and intermolecular factors important for property predictions. To address this, chemical descriptors encoding the chemical information on a molecule (e.g., long- and short-range interactions, polarity, etc.) may reduce the amount of data required for accurate predictions in such cases. Thus, the structure of the feature vector is a means to capture prior knowledge into a specific ML model.

In our previous work, we demonstrated that cloud point data for polystyrene (PS) can be used to train a neural network and Gaussian process regression model to predict both upper and lower critical solubility curves. $^{30}$ The input feature vector contained information on the solvent−PS chemistry, PS characteristics (size, dispersity, etc.), and state descriptors. Herein, we extend the previous data set to include cloud point temperatures for 21 polymers and 61 solvents (97 unique polymer−solvent systems) to ascertain the necessary data density and feature vector architecture to predict general linear polymer−solvent phase behavior. The feature vector is generalized to include any number of components, and the impact of several types of descriptors (Morgan fingerprints, molecular descriptors, Hansen solubility parameters) to encode polymer−solvent interactions is assessed. Two common regression models are tested, including gradient boosted decision trees and neural networks to establish the generality of the descriptors with respect to the ML algorithm chosen. Lastly, we discuss the challenges in extrapolating to new polymer−solvent systems, estimate the minimum set of additional data necessary to enable prediction of its $T-\phi$ solvent phase behavior, and introduce HSPs as a means to understand the general breadth of linear polymer−solvent space as well as the density and distribution of curated data.

## COMPUTATIONAL DETAILS
Data Set. The curated data set of 6524 total cloud points is composed of 21 polymers, 61 solvents, and 97 unique polymer−solvent systems. The data are a subset of the data reported in the section Liquid−Liquid Equilibrium Data of Binary Polymer Solutions from the CRC Handbook of Liquid−Liquid Equilibrium Data of Polymer Solutions. $^{31}$ The handbook only includes published data between the years 1940 and 2006. Additionally, the CRC Handbook is not a comprehensive list of cloud points in the literature as there are many publications without a tabulated format, with only a graphical representation of the cloud points reported (see Section 2.3 of ref 31). Hence, we digitize plots from publications listed in this section of the CRC Handbook for select polymers noted in Table S1. The number of digitized cloud points is 689 which is included in the 6524 total reported above. To obtain the tabulated cloud points, a PDF copy of the book was first parsed into a JSON file using Python. Only data labeled as "cloud points", "coexistence data", "binodal data", or "critical point data" in the CRC Handbook are processed. Specifically, we do not include "spinodal data", as the cloud point is often associated with the binodal curve in polymer phase separation. Lastly, each entry in our data set is a single cloud point from the CRC Handbook or digitized from the cited literature in Section 2.3 of ref 31.

During the data curation process, entries with missing values for the weight-average molecular weight $(M_{w})$ or number-average molecular weight $(M_{n})$ are removed. Furthermore, the polydispersity index (PDI) values are calculated (PDI = $M_{w}/$$M_{n}$), and values less than 6 are processed into the curated data set. The cutoff was selected to minimize the number of data removed and eliminate extreme polydispersity values (e.g., PDI > 10). To keep the reported concentrations consistent, we convert all mass fractions to volume fractions using densities at 20 °C (or 25 °C, if 20 °C data are unavailable). Polymer and solvent densities used are listed in Tables S1 and S2 for easy conversion back to mass fraction. All entries that do not report either a mass fraction or volume fraction (such as mass or mole concentrations) are removed. Lastly, we discard any polymer−solvent combination with less than 2 reported cloud points to ensure that a stratified split is obtainable (see the Model Training subsection). The remaining binary data are for other polymer architectures (block copolymers, star polymers, etc.), contain missing information, or do not report a cloud point temperature (e.g., cloud point pressure).

We note that experimental uncertainty (e.g., quality of data) could not be rigorously assessed, which results in an inherent uncertainty for each cloud point estimated to be about 3−5 °C on average due to the variability in cloud point measurement techniques. For example, visual observation and light scattering

measurements can lead to differences of up to 10 °C for the measured cloud point. $^{32,33}$ Therefore, several literature sources with noticeably large discrepancies or outliers were discarded from the data set. With enough data, ML models will typically predict the mean value, capturing the variability in the reported measurements. In some cases, the median value of several measurements can be implemented as demonstrated with predictions of polymer glass transition temperature. $^{22}$ The number of cloud points for each polymer that meet the curation standards is listed in Table S1. In total, roughly 70% of the tabulated cloud points reported in the CRC Handbook comprise the final curated data set for training and testing, with an additional 689 cloud points digitized from the literature. The final data set can be found on the Polymer Property Predictor and Database (3PDb) website (pppdb.uchicago. edu).

Feature Vector. The feature vector used to predict the cloud point temperature is a combined set of component (polymer or solvent), state (concentration, pressure, temper- ature, etc.), and experimental (phase direction) descriptors, which is generalizable to multicomponent solutions and blends. Each molecule in the feature vector is represented using Simplified Molecular Input Line Entry System (SMILES) strings containing the molecular structure and atomic arrangement of each component. For linear homopol- ymers, the chemical structure representation can be reduced to the repeat unit, with additional descriptors to represent the weight-average and distribution of the polymer size ($M_w$ and PDI). For example, we represent the polystyrene repeat unit as "*C(C*)c1ccccc1", whereas the styrene monomer SMILES is "C=Cc1ccccc1" (see example structures drawn in Figure S1). The repeat unit chemistry is used to represent the polymer structure because several polymers have different monomer structures but the same repeat unit structure. For example, poly(ethylene glycol) and poly(ethylene oxide) have the same polymer structure but are polymerized from different monomers. If the monomer structures are encoded, this will lead to very different descriptor values for the same polymer chemistry. Thus, to ensure that these polymers have the same encoded values, we use the repeat unit SMILES. In this work, only binary solutions are considered, and thus, the component portion of the feature vector reduces further to the solvent chemical descriptors and the polymer repeat unit chemical, chain $M_w$, and chain PDI descriptors.

As previously mentioned, the choice of descriptors to represent the chemistry of component $N$ is crucial for accurate model prediction. In order for the ML model to distinguish between various chemistries, the SMILES notation of the molecule structure is encoded into a set of descriptors using RDKit cheminformatics software. $^{34}$ In this work, we compare the use of 3 different component feature representations. (1) The topological "Morgan" fingerprint (MFP) examines multiple substructures of the molecule and encodes them into a bit vector, creating a very sparse feature vector. The radius parameter is set to 3, which is akin to the Extended Connectivity Fingerprint (ECFP6) algorithm, $^{29}$ and a reduced fingerprint size of 64 bits per component is used. Typical fingerprint sizes range between 64 and 2048 bits depending on the data set, and we find that 64 bits minimizes the number of descriptors containing the same value for all components and reduces sparsity. (2) Molecular descriptors (as provided by RDKit) contain a combination of connectivity, MOE-type, constitutional, molecular property, and other 1- and 2- dimensional descriptors often used in QSAR/QSPR models (e.g., number of hydrogen bond donors, partial charges, number of rings, lipophilicity, etc.). Due to the limited number of polymers and solvents, some descriptors have the same value for all molecules (similar to the fingerprint feature set) or contain "NaN" and infinite values. Since the model will not find any relationships between these descriptors, they are removed. Of the 196 molecular descriptors provided by RDKit, 96 polymer and 120 solvent descriptors are included in the reduced feature set. The specific descriptors used for the polymer and solvent are listed in Table S5.

Lastly, with the understanding that polymer−solvent compatibility is often described by their HSPs, we test a highly reduced feature vector by (3) using HSP descriptors (3 HSP values per component). However, these values are not readily available for many polymers and even some solvents. Thus, we estimate HSPs for each component using gradient boosting decision tree models (via XGBoost software $^{35}$) trained separately to predict each solubility parameter. Specifically, these models are trained on a data set containing 10 255 molecules with known HSP values collected from Hansen Solubility Parameters in Practice (HSPiP) software and the literature. $^{3}$ Each molecule in the data set is first encoded into 196 molecular descriptors from their SMILES notation (using RDKit) before training and optimizing the model hyperparameters. Hence, we are essentially using the molecular descriptors in component feature representation 2 to reduce the component descriptor set to a 3-dimensional space (via their HSP values). This also helps with visualization of the polymer−solvent space, which is impractical using the full molecular or MFP component descriptor sets. The details of model training and predictive performance of the HSPs can be found in Section S2 of the Supporting Information. To summarize, the 5-fold cross-validation results show that predictions for $\delta_D$, $\delta_P$, and $\delta_H$ have a mean absolute error (MAE) of 0.25 ± 0.01, 0.74 ± 0.03, and 0.62 ± 0.03, respectively, with $R^2$ ∼ 0.9 or greater. HSPs for polymer repeat unit and solvent in the cloud point data set are predicted using the model trained on all 10 255 molecules. The highlighted predictions in the parity plots of Figure S3 show that the estimated values for solvent molecules in the cloud point data set (with known HSPs) lie along the diagonal and are highly accurate. Thus, we expect that the estimated HSP values for the repeat unit chemistry listed in Table S1 are similarly accurate.

The above construct for a binary solution feature vector contains $2n$ component descriptors, $n$ being the number of descriptor values per component (polymer/solvent), con- catenated with state descriptors and an experimental descriptor. The state descriptors include concentration (polymer volume fraction), pressure, and temperature (our target or "label" feature). The experimental descriptor is required to distinguish the different cloud points and miscibility regions in $T−\phi$ space, which was first introduced in our previous work with polystyrene. $^{30}$ Hence, the temper ature region of complete miscibility for a particular cloud point is encoded into this descriptor. This descriptor is called the "one-phase direction" in which "positive" or "negative" is assigned to each cloud point and is relative to temperature. In other words, the one-phase (miscible) region can be found with increasing (positive $T$ direction) or decreasing (negative $T$ direction) temperature. This descriptor can be expanded to other state variables (e.g., pressure) but is not explored here

![](./images/812514987711922177_3.jpg)

Figure 1. Representation of polymer repeat unit and solvent chemistry via component Hansen solubility parameters ($\delta_{\rm D}$, $\delta_{\rm P}$, $\delta_{\rm H}$): colored points show (a) polymer HSP and (b) solvent HSP in the cloud point data set. The gray points represent the 10 255 molecules in the training set for HSP predictions (details available in Section S2 of the Supporting Information). The left column (a) provides a view of the directional intermolecular nature of the polymer [polar and hydrogen bonding character, ($\delta_{\rm P}$, $\delta_{\rm H}$)] with respect to the dispersive character of the polymer ($\delta_{\rm D}$). The right column (b) provides a complementary view based on the dispersive character of the solvent. The colors represent the number of training data $n$ within the curated cloud point data set.

due to lack of data. A schematic of the feature vector, where we compare different chemical descriptors (MFP, molecular descriptors, or HSP), can be found in the Supporting Information.

Model Training. Two different regression models are compared in this work: a gradient boosted decision tree model using the extreme gradient boosting algorithm, XGBoost,³⁵ and a feed-forward artificial neural network (ANN) model using the Keras backend in Tensorflow.³⁶ This compares the use of an ensemble model (decision trees) to that of neural networks. Both are known to be excellent supervised learning models, with the XGBoost algorithm being one of the most commonly employed on the Kaggle competition platform.³⁵ The XGBoost model is a highly efficient algorithm that uses the gradient boosting method where base decision tree estimators are built sequentially, and each subsequent decision tree added is trained to reduce the previous decision tree’s residual errors. To minimize overfitting, early stopping is implemented with a patience set to 10 rounds and stops training if the validation root mean squared error (RMSE) does not decrease any further from the last 10 RMSE values.

For the artificial neural network, a sequential model is built with several hidden layers and an output layer consisting of a single unit. The number of hidden layers and units per layer are tuned using Hyperopt (see the Hyperparameter Tuning subsection). The Adam optimizer is used for training the ANN with a learning rate of 0.001. Additionally, a batch size of 128 was used for training efficiency. For each layer, the “ReLU” activation function is applied to each neuron’s output. To help minimize overfitting, “L2” regularization is used with default values. The last layer uses a “linear” activation function, which is simply the output value of the unit. Each layer’s weights are initialized using “He” initialization values and trained for a maximum of 2000 epochs. Similar to the XGBoost model, early stopping is implemented during training with a patience set to 100 epochs.

An 80:10:10 split ratio is applied to the data set for the train, validation, and test data sets, respectively. Since the number of cloud points for each polymer is significantly skewed toward polystyrene (Table S1), a random train/test split may lead to a biased test set toward PS. Therefore, we implement a stratified split based on the number of cloud points for each unique polymer–solvent combination to ensure that our test set represents the distribution of cloud points in our curated data set. The validation set is used to tune the hyperparameters and prevent overfitting (see the Hyperparameter Tuning sub- section) but does not train the model parameters. Before training each ML model, the train and validation data sets are subjected to a preprocessing pipeline where the continuous variables are standardized (HSPs, molecular descriptors, log $M_w$, log $P$, $\sqrt{\phi}$, and PDI) to have a mean of 0 and standard deviation of 1. Note that the XGBoost model does not require standardization, whereas the ANN does, and therefore, we standardize all variables for consistency. The “one-phase direction” is a categorical feature containing “positive” or “negative” which is converted to a 0 or 1, respectively. The statistics for standardizing are then saved and used to transform the test set before analyzing model performance.

Hyperparameter Tuning. Model hyperparameters are tuned using the Hyperopt software.³⁷ This software, based on Bayesian optimization methods, allows automation of the search for an optimized set of hyperparameters in a defined space. For each model, we search the hyperparameter space for 100 iterations and use the RMSE of the validation set for the performance metrics. The Tree of Parzen Estimators (TPE) algorithm is used for selecting the subsequent set of hyperparameters at each iteration. The span of hyperparameter values that were searched along with the optimized hyper-

![](./images/812514987711922177_4.jpg)

Figure 2. Predicted vs observed cloud point temperatures using the XGBoost (left) and ANN (right) models for each feature set: 64-bit Morgan fingerprints (top), molecular descriptors (middle), or Hansen solubility parameters (bottom). Training and validation data sets (gray) are combined for the RMSE calculation. Train and test RMSE values are reported in each plot. Model hyperparameter values can be found in the Supporting Information.

parameters for each model can be found in Tables S6 and S7 in
the Supporting Information.

## RESULTS AND DISCUSSION

Polymer−Solvent Solubility Space. We first visualize
the cloud point data to examine the span of polymer−solvent
solubility space. To visualize polymer and solvent solubility,
HSPs predicted from the trained XGBoost models are plotted
(see Section S2 of the Supporting Information for HSP model
details). Additionally, visualization is important in machine
learning to identify key areas of missing data, outliers, or other
artifacts of the data set. If the dimensionality of the feature
space is large, dimensionality reduction tools are used such as
principal component analysis (PCA) or t-distributed Stochastic
Neighbor Embedding (t-SNE) to visualize the feature space in
2 or 3 dimensions. Given that the HSP XGBoost models use
molecular descriptors of the polymer repeat unit and solvent to
predict an HSP value, these models are essentially reducing the
molecular descriptors to a 3-dimensional space tailored to
polymer and solvent solubility.

Figure 1 summarizes HSP values $(\delta_{\mathrm{D}},\ \delta_{\mathrm{P}},\ \delta_{\mathrm{H}})$ for polymer
repeat unit (Figure 1a) and solvent molecules (Figure 1b) in
the cloud point data set compared to the 10 255 molecules in
the training set. The 21 polymers and 61 solvents are also
highlighted in order of number of training data. This provides a
simple representation of the chemical space in terms of HSPs
and highlights the span of polymer and solvent chemistries in
our data set. For instance, with 21 polymers in the data set, the
vast majority of polymers have $\delta_{\mathrm{D}}$ values in the range 13−17
with $\delta_{\mathrm{P}}$ and $\delta_{\mathrm{H}}$ less than 10. Only the poly(vinyl alcohol)
repeat unit (14.6, 10.6, 21.2) has a large $\delta_{\mathrm{H}}$ of $\sim$21 (see also
Table S1). Similarly, solvents in our data set are limited to $\delta_{\mathrm{D}}$
between 12.5 and 18 but show a much larger range of $\delta_{\mathrm{P}}$ and
$\delta_{\mathrm{H}}$ values. Additionally, the vast majority of solvents have $\delta_{\mathrm{P}} <$
10 and $\delta_{\mathrm{H}} < 20$. The density of cloud points in the polymer−
solvent chemistry space is also portrayed in Figure 1, with the
color corresponding to the amount of cloud points in the
training set. Polystyrene (18.3, 3.6, 3.0) and polyethylene
(13.7, 3.5, 2.6) both have more than 500 observed cloud points
that span the minimum and maximum of $\delta_{\mathrm{D}}$, while roughly half
of the polymers in the data set contain more than 100 cloud
points.

To further examine the sparsity of the data set, the
distributions of polymer molecular weight, polydispersity,
volume fraction, pressure, and temperature are plotted in
Figure S2 in the Supporting Information. The distributions for
$\log M_{\mathrm{w}}$, $\log P$, PDI, and $\sqrt{\phi}$ before standardizing the data are
shown. Since FH theory implies that polymer size and
concentration will affect phase behavior similarly among all
polymers, the data density for these features is much greater

![](./images/812514987711922177_5.jpg)

Figure 3. Predicted temperature vs observed temperature for (a) polystyrene, (b) polyethylene, (c) poly(methyl methacrylate), (d) polydimethylsiloxane, (e) poly(ethylene glycol), and (f) poly(vinyl alcohol). The ANN model with the HSP feature set is used for the predictions. Prediction error (RMSE) on the training and validation (gray) and test (red) data sets are reported in each plot.

than the enthalpic contribution, which depends on the specific polymer−solvent interaction, temperature, and pressure. For instance, both $\log M_{\mathrm{w}}$ and $\sqrt{\phi}$ show good coverage over the range of values. A large portion of temperatures are between 0 and 75 °C, with a broader distribution at higher temperatures. The distribution of PDI also shows that there are mostly monodisperse molecular weights in the data set. For instance, many molecular weights have a PDI of $\sim$1.05, with significantly less data for PDI > 3. Effects of polydispersity can be found to broaden the binodal curve, and therefore, keeping polydispersity in the set of descriptors will allow the model to account for this change in solubility curve shape. Similar to the PDI distribution, many cloud points are observed at atmospheric pressure ($P = 0.1$ MPa). However, similar to molecular weight, varying pressure will shift the miscibility regions in $T−\phi$ space. Therefore, it is important for the models to capture these pressure effects.

Model Performance. A comparison of all optimized regression models can be found in Figure 2, where we plot the predicted vs observed cloud point temperatures for a single stratified train/test split. Both XGBoost and ANN models predict the test data over the entire temperature range (−25 to 300 °C) with an average RMSE of 4 °C or less. Of the three component descriptor sets, the molecular descriptors (RDKit) appear to have the lowest test prediction error of less than 3 °C. Additionally, the Morgan fingerprint feature set shows the highest prediction error, confirming that, for this data set, chemical features (HSP/molecular descriptors) require less data to capture the underlying thermodynamics than a low-resolution fingerprint approach. For model comparison, the average test RMSE from 5-fold cross-validation (CV) was measured between the different feature sets and models in Figure S5. We note that, with cross-validation, each fold is split at random and not using a stratified technique (see the Supporting Information). Therefore, the CV results show slightly larger RMSE values on average due to less control over the polymer/solvent distributions in the training/validation set. Regardless, the CV results are consistent with the results in Figure 2, confirming that molecular and HSP descriptors provide the necessary information for predicting polymer solubility with mean absolute errors (MAEs) less than 2 °C between the ANN and XGBoost models. This is consistent with our previous work³⁰ and confirms that HSPs are good solubility descriptors for multiple polymer−solvent systems while also providing a 3-dimensional space for data visualization. Below, we discuss the predictions and performance of the models for select polymers to examine the ability to construct cloud point curves for a variety of polymer chemistries. Results are reported using the ANN model (as it predicts smoother cloud point curves) with the HSP descriptor set to demonstrate the usefulness of using a reduced feature set that is tailored to solubility. Similar plots for other feature sets/models can be found in the Supporting Information.

The parity plots for several common polymers are shown in Figure 3 for the ANN model. The remaining plots for other polymers can be found in the Supporting Information (Figures S6−S8). Overall, the predictive performance is excellent for most polymers. This suggests that our ML models are able to capture the unique behaviors ranging from simple polyolefins to silicon-based organic polymers and aromatic polymers. In most cases, neural networks are applied when data sets contain $10^{4}−10^{5}$ training instances or more. Our results suggest that the amount of polymer−solvent data is sufficient for capturing the phase behavior of linear-polymer solvent systems, likely due to the similarities in the entropic effects (e.g., polymer size, concentration, etc.) among these systems. Note that these predictions are for cloud points similar to the training set (e.g., same solvent, molecular weight, PDI, etc.) and are interpolating within a cloud point curve. Extrapolation to

![](./images/812514987711922177_6.jpg)

Figure 4. Cloud point predictions for various polymer−solvent systems demonstrating the predictive performance of (a) upper critical solubility (UCS) of PS in cyclohexane, (b) lower critical solubility (LCS) of PS in cyclohexane, (c) isopleths at varying concentrations of PE (52 kDa) in n-hexane, and (d) closed-loop behavior of PEG in water. Experimental data are reported from various literature sources cited in the CRC Handbook.

![](./images/812514987711922177_7.jpg)

Figure 5. Average increase in the predicted MSE on the test data set after shuffled permutation of each descriptor's values using the XGBoost (left) and ANN (right) models. The permutation was applied 10 times to calculate the average (red bar) and standard deviation (error bars). Plots show subsequent feature importance with the one-phase direction descriptor removed for clarity (see the Supporting Information for one-phase direction importance). Notation for specific molecular descriptors and model hyperparameter values can be found in the Supporting Information.

other molecular weights (curves) is discussed in the Extrapolation to New Chemistries subsection below. Several polymers have less than 20 recorded cloud point temperatures, such as poly(vinyl alcohol), or PVA, shown in Figure 4f. Predictions for these polymers in the data set are quite good, indicating that even small amounts of training data can lead to accurate predictions for a polymer−solvent system.

Binodal Predictions. The predictive performance of the ANN model with HSP descriptors is shown in Figure 4 (similar figures for the molecular descriptors/XGBoost models can be found in the Supporting Information). We plot 4 common phase behaviors found in the literature: upper critical and lower critical solubility (Figure 4a,b), isopleths (Figure 4c), and closed-loop (Figure 4d). The polymer−solvent system and polymer molecular weights are listed in the figure caption. Interestingly, all 4 curve types are captured for various polymer−solvent chemistries, contrary to current theoretical models. For instance, the shape of the UCS and LCS curve for

polystyrene in cyclohexane over a wide range of molecular weights is excellent and agrees with experimental observations. Even the closed-loop curve shapes agree with those found in the literature and previous models. $^{8,38,39}$ This demonstrates that ML can be used to predict all types of phase behaviors found in varying polymer-solvent systems with a single model. We also show predictions from the XGBoost model and predictions using the molecular feature set (see Figures S10-S12). For the XGBoost model, the predicted curve shape is quite noisy due to its underlying decision tree estimators, but overall predictions agree with expected thermodynamic behavior.

In most cases, the predicted curves agree with known thermodynamic phase behavior even when extrapolating outside the range of experimental concentrations shown in Figure 4. Of course, the accuracy of the curve shape at the boundaries of the binodal such as that found at low concentration regimes will largely depend on the number of training data. For instance, the predicted LCS curves for PS (37 kDa) in cyclohexane and LCS for PEG (2.5 kDa) in water deviate from their qualitative shape when extrapolating to low concentrations (see Figure S9 of the Supporting Information). Thus, extrapolation out to concentrations away from the critical point requires additional data, especially at these low concentrations where the binodal appears asymptotic (infinitely increasing or decreasing) at the concentration boundary. The vast majority of concentration values in our data set are close to the critical point range (between 0.1 and 0.5 as seen in Figure S2). Regardless, many of the predicted boundaries are akin to known phase behavior, and the agreement with the observed data is excellent, even for other systems such as the LCS-type binodal of PEG in water (Figures S13 and S14 in the Supporting Information).

In Figure 4c,d, we plot the predictions for isopleths ($T$ vs $P$) at several concentrations for the PE (52 kDa) in $n$-hexane and closed-loop behavior in $T-\phi$ space for the PEG-water system at several molecular weights. The agreement for closed-loop behavior is exceptionally good compared to previous models (such as FH theory) where agreement at lower molecular weights can be poor. While the models do not capture the complete "loop" at high concentration, predictions using the HSP and molecular descriptors show overlap at low concentrations (see also Figures S9-S11). Thus, our models are able to estimate not only the two demixing regions for systems such as polystyrene-cyclohexane but also pressure effects of polyethylene and the closed-loop behavior of poly(ethylene glycol)-water.

Permutation Importance. With deep learning models such as neural networks, interpretability of the model is mostly nonexistent. In some cases, "feature importance" can be extracted from the model to give insight into how important each descriptor is for a particular model. In Figure 5, we analyze the feature importance of the XGBoost and ANN model using permutation feature importance with the molecular and HSP feature sets. Permutation feature importance is calculated as implemented by scikit-learn software in Python, where a single descriptor is chosen, and the values are randomly shuffled before calculating the change in MSE on the test set. By shuffling the values, the relationship between the descriptor and output is no longer valid and therefore indicates how important that particular descriptor is to a particular model's accuracy. Additionally, using the test set for measuring feature importance indicates how critical a particular descriptor is in generalizing to new cloud points. Thus, the increase in MSE is calculated compared to the original order of descriptor values. This is repeated 10 times for each descriptor, where the average MSE increase is reported.

For both models and feature sets, the "one-phase direction" descriptor is found to be substantially more critical than the other descriptors (see Figure S15 in the Supporting Information), and hence, we only plot the subsequent 10 important descriptors in Figure 5. The one-phase direction descriptor is intended to provide information on concavity and distinguish between UCS- or LCS-type phase behavior. Additionally, it provides a key indication of the temperature region where a cloud point resides, since most UCS and LCS cloud points are well separated in $T-\phi$ space as seen in Figure 4a,b. Therefore, shuffling the "one-phase direction" values will lead to the largest increase in prediction error. Examining the subsequent 10 most important descriptors (Figure 5), we find that polymer molecular weight and pressure are the next most important descriptors for the ANN model using molecular component descriptors. This is also observed in the permutation importance for the XGBoost model (left plots in Figure 5). We know from experimental data that these descriptors are what shift the cloud point curves up or down in $T-\phi$ space. Overall, it is found that the most important descriptors are derived from prior knowledge of binary solution thermodynamics (the molecule size, pressure, concentration, etc.). Thus, insight into the ANN and XGBoost model confirms that these known physical parameters are crucial to predicting an accurate cloud point temperature. Lastly, using a reduced feature set with HSP component descriptors shows that shuffling each one increases the MSE by over 200, but solvent choice (solvent HSPs) appears to be most important for the ANN model (all 3 solvent HSP values are in the top 4 important descriptors).

Figure 5 also lists the permutation importance for the XGBoost model, where the polymer MolLogP descriptor is critical for generalizing to new cloud points in the test set. This descriptor is known as the octanol-water partition coefficient and describes the lipophilicity of the molecule. $^{40}$ Thus, aside from molecular weight, pressure, and concentration, the XGBoost model finds that the water-soluble and hydrogen bonding characteristics of the polymer and solvent can severely affect prediction accuracy in the test set as evidenced by the large increase in MSE for the MolLogP and $\delta_{\text{H}}$ descriptors. Removal of the water-soluble polymer data removes these descriptors from the feature importance which suggests that the XGBoost model is sensitive to the categorical imbalance of the polymer-solvent data in the training and test set (see additional analysis in Section S4 in the Supporting Information). Note that the XGBoost model can also calculate the feature importance using a built-in algorithm that measures the "total gain" in performance by splitting the feature in the base decision tree estimators. We find that this feature importance is consistent with the results in Figure 5 (see Figure S18 in the Supporting Information).

Extrapolation to New Chemistries. The above predictions show excellent predictive performance for constructing phase behavior of polymers and solvents within the data set, but they do not demonstrate the predictive performance of new polymer-solvent systems. In this regard, we demonstrate the ability to extrapolate to new polymers and solvents using the polymers with small amounts of data in the current data

set. To do this, a variation of the leave-one-out method is implemented where a single polymer is left out before training the model on the entire data set. The test RMSE of the new polymer is calculated, and the leave-one-out method is repeated for each polymer. We use the XGBoost model and HSP feature set due to its excellent efficiency in model training which provides an ideal tool for online learning. Due to similar prediction errors for both ML models, the extrapolation behavior is expected to be similar for the ANN model.

The XGBoost model is first tested with the ability to predict a new polymer with no prior information (Figure 6).

![](./images/812514987711922177_8.jpg)

Figure 6. RMSE of predictions on a test set consisting of a single polymer using a leave-one-out method. The XGBoost model with HSP descriptors is used for training and testing. From left to right, polymers are listed in order of increasing number of cloud points. The leave-one-out method is repeated 10 times for every polymer, each time randomly shuffling the training data to predict the cloud point temperature of the new polymer. Error bars show one standard deviation from the mean.

Predictions for polymers such as poly(vinyl acetate), poly(vinyl methyl ether), polypropylene, polyisobutylene, and poly(vinyl alcohol) show very large prediction errors, with RMSE values greater than 50 °C. The "best" predictions are still quite poor, between 10 and 20 °C. These poor extrapolated predictions are likely due to the dissimilarity in feature space when removed from the training set, as can be understood by the distribution of data portrayed in Figure 1 and Figure S2. For instance, observed temperatures for PVME are between 35 and 45 °C, which is very low for a "negative" one-phase direction (or LCS type behavior). Similarly for poly(vinyl acetate), observed UCS temperatures are higher than 150 °C, outside the typical range of cloud point temperatures for the "positive" one-phase direction (or UCS-type behavior). Thus, because the "one-phase" direction is so critical, more data are needed for these polymers that have phase behaviors outside of the typical cloud point ranges. Furthermore, extrapolation to polymers with significantly different HSP values results in large prediction errors, as seen by the predictions for poly(vinyl alcohol) ($\delta_{\text{H}} = 21$).

The effects of introducing new polymers to the training set are determined by shuffling in data to the training set at random for each polymer. This is repeated 10 times, shuffling in a new random sequence each time for the test polymer. In Figure 7, we show the average reduction in RMSE on the remaining test polymer data as a function of increasing number of cloud points added. Overall, we find that predictions of the new polymer−solvent system can reach below 5 °C with roughly 20 cloud points. For some polymers, this is close to the total amount of cloud points in our data set. In some instances, more than 20 cloud points are required, as apparent with the larger prediction RMSE in polyisobutylene and poly(2,6-dimethyl-1,4-phenylene oxide). Nevertheless, predictions for new cloud points are significantly reduced when a small number of cloud points are added to the training set, compared to extrapolating from no prior information (Figure 6). This is an indication that the large amount of data for polystyrene captures the entropic contributions to solubility such as molecular weight, pressure, and concentration. Hence, the model only requires a small amount of data for polymer−solvent chemistry to make accurate predictions of cloud points. This is likely a result of the amount of data available to date. Increasing the number of polymer−solvent systems will reduce the interpolation (or extrapolation) distance of a new polymer−solvent system, thereby reducing the number of cloud points required for a reasonable estimate.

While the above results show that little information is required for new polymer−solvent chemistries, the new cloud point predictions can be for any concentration and molecular weight. In practice, however, one might want to estimate the entire binodal curve for several molecular weights of a new polymer and solvent instead of estimating a single cloud point. Therefore, we next demonstrate that entire demixing regions (binodal curves) can be predicted with information for only one constructed curve in $T−\phi$ space. Specifically, we predict cloud point curves in $T−\phi$ space at a

![](./images/812514987711922177_9.jpg)

Figure 7. RMSE as a function of the number of data added to the training set for each polymer. The addition of data to the training set is repeated 10 times for each polymer with a new random order. The RMSE at 0 is equivalent to Figure 6. The XGBoost model with HSP descriptors is trained and used for predictions (see the Supporting Information for specific hyperparameter values). (inset) Same plot on a reduced scale; shaded regions show one standard deviation from the mean.

specific polymer $M_\mathrm{w}$ when the model is given cloud points for a different $M_\mathrm{w}$. The results in Figure 8 depict this for polyisoprene in 1,4-dioxane and poly(2-ethyl-2-oxazoline) in water. With the addition of 20 kDa poly(2-ethyl-2-oxazoline), the predictions for 50, 128, and 500 kDa curves have an average RMSE of $\sim5$ °C. Similarly for polyisoprene, we see that, with the addition of one cloud point curve, the prediction for a new $M_\mathrm{w}$ is within 5 °C. The predicted cloud point curves for these new $M_\mathrm{w}$ values seen in Figure S19 in the Supporting Information show excellent agreement between the predicted value and observed cloud points. Thus, the molecular weight (entropic) behavior in $T-\phi$ space is well captured by our data, likely because the model captures the effect of molecular weight (e.g., the inherent variance in the data set) from one or two polymers with a complete set of cloud points such as the large data set of polystyrene and polyethylene. Hence, extrapolating to molecular weights for new polymer−solvent systems requires less data.

![](./images/812514987711922177_10.jpg)

Figure 8. Average RMSE of predictions for a test $M_\mathrm{w}$ for (a) polyisoprene in 1,4-dioxane and (b) poly(2-ethyl-2-oxazoline) in water. The $M_\mathrm{w}$ values added to the training set are listed in each figure with units of kDa. The XGBoost model with HSP component descriptors is used for predictions. Error bars show one standard deviation from the mean. Predicted cloud point curves can be found in the Supporting Information.

## CONCLUSION

In this work, we demonstrated that a curated cloud point data set consisting of 21 polymers, 61 solvents, and 97 unique polymer−solvent pairs can be used to construct phase diagrams for binary polymer solutions from machine learning models. Overall, the predictive performance of the XGBoost and artificial neural network models showed excellent agreement with experimentally observed phase behavior including UCS, LCS, and closed-loop behavior with an average prediction RMSE of less than 3 °C on the test data set. Of the three component descriptors examined, we confirmed that a significantly reduced feature set consisting of ML-predicted Hansen solubility parameters captures the importance of polymer−solvent interactions as well as helps understand the general scope and density of data in polymer−solvent space. A permutation feature importance showed that, in addition to the one-phase descriptor, the most significant descriptors included those derived from prior knowledge on polymer phase behavior such as polymer chain size, pressure, and concentration. Additionally, we demonstrated that the RMSE of predictions for polymer−solvent pairs excluded from the curated data set can be reduced to 5 °C with as little as 20 cloud points or a single binodal curve. Hence, the current model captures aspects of the polymer phase behavior by training on the current data set and requires less data to construct cloud point curves for additional polymer−solvent pairs. This is critical for estimating phase behavior of polymer−solvent systems moving forward, as the ability to accurately estimate the miscibility regions of polymers will enable more efficient processing of polymer materials.

To further improve the generality of the models established in this work, additional polymer and solvent chemistries are required and will be a focus for future data collection. Given the common impact of structure for polymer−solvent phase boundaries, our models indicate that an additional 20 cloud points and two molecular weights at minimum are required for each polymer−solvent system. As more data are added, this will decrease due to the model learning more examples of polymer−solvent interaction. For large PDIs or low concentrations, additional data for these descriptors would broaden the distribution and allow more accurate cloud point curve estimates. Finally, given the broad polymer and solvent chemistry space, more systems in areas such as intermediate polymer $\delta_\mathrm{H}$ ($10 < \delta_\mathrm{H} < 20$) and large solvent $\delta_\mathrm{D}$ (>18) will further enhance generality as seen in Figure 1. Future work will also aim to reduce the required training data further by implementing theory-informed machine learning methods, such as incorporating estimates for the Flory−Huggins interaction parameter $\chi$. This will become increasingly important as we explore the capabilities of training models to predict the phase behavior of other macromolecular systems, such as block copolymer and various polymer architectures (e.g., branched polymers), or ternary phase behavior where cloud point data are significantly less abundant.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.macromol.2c00245.

Curated data set details; schematic of feature vector and polymer/solvent molecular descriptors; HSP model details and prediction performance; XGBoost and ANN model hyperparameters; 5-fold cross-validation, and other predictions; and additional permutation and extrapolation results (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Richard A. Vaia − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force

Base, Ohio 45433, United States; orcid.org/0000-0003-4589-3423; Email: richard.vaia@us.af.mil

# Authors
Jeffrey G. Ethier − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States; UES, Inc., Dayton, Ohio 45431, United States; orcid.org/0000-0001-7987-4058

Rohan K. Casukhela − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States; UES, Inc., Dayton, Ohio 45431, United States

Joshua J. Latimer − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States; UES, Inc., Dayton, Ohio 45431, United States

Matthew D. Jacobsen − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States

Boris Rasin − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States

Maneesh K. Gupta − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States

Luke A. Baldwin − Materials and Manufacturing Directorate, Air Force Research Laboratory, Wright-Patterson Air Force Base, Ohio 45433, United States; orcid.org/0000-0002-7787-238X

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.macromol.2c00245

# Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors acknowledge the Air Force Office of Scientific Research (AFOSR) and the Air Force Research Laboratory's Materials and Manufacturing Directorate for their financial support. The authors also thank Dr. Steven Abbott for providing the HSPiP data set and Dr. Debra Audus for assisting with model deployment on 3PDb.

## REFERENCES
(1) Hansen, C. M. *The Three Dimensional Solubility Parameter*; Danish Technical Press: Copenhagen, 1967.

(2) Hansen, C. M. *Hansen Solubility Parameters: A User's Handbook*; CRC Press, 2007.

(3) Abbott, S.; Hansen, C. M. *Hansen Solubility Parameters in Practice*; Hansen-Solubility, 2008.

(4) Imre, A.; Van Hook, W. A. Liquid−Liquid Demixing from Solutions of Polystyrene. 1. A Review. 2. Improved Correlation with Solvent Properties. *J. Phys. Chem. Ref. Data* 1996, 25 (2), 637−661.

(5) Siow, K. S.; Delmas, G.; Patterson, D. Cloud-Point Curves in Polymer Solutions with Adjacent Upper and Lower Critical Solution Temperatures. *Macromolecules* 1972, 5 (1), 29−34.

(6) Luszczyk, M.; Van Hook, W. A. Isotope and Pressure Dependence of Liquid- Liquid Equilibria in Polymer Solutions. 7. Solute and Solvent H/D Isotope Effects in Polystyrene- Propionitrile Solutions. *Macromolecules* 1996, 29 (20), 6612−6620.

(7) Bae, Y. C.; Lambert, S. M.; Soane, D. S.; Prausnitz, J. M. Cloud-Point Curves of Polymer Solutions from Thermooptical Measurements. *Macromolecules* 1991, 24 (15), 4403−4407.

(8) Oh, S. Y.; Bae, Y. C. Closed Miscibility Loop Phase Behavior of Polymer Solutions. *Polymer (Guildf)* 2008, 49 (20), 4469−4474.

(9) Knychala, P.; Timachova, K.; Banaszak, M.l; Balsara, N. P. 50th Anniversary Perspective: Phase Behavior of Polymer Solutions and Blends. *Macromolecules* 2017, 50 (8), 3051−3065.

(10) Flory, P. J. Thermodynamics of High Polymer Solutions. *J. Chem. Phys.* 1941, 9 (8), 660.

(11) Flory, P. J. Thermodynamics of High Polymer Solutions. *J. Chem. Phys.* 1942, 10 (1), 51−61.

(12) Huggins, M. L. Solutions of Long Chain Compounds. *J. Chem. Phys.* 1941, 9 (5), 440.

(13) Huggins, M. L. Some Properties of Solutions of Long-Chain Compounds. *J. Phys. Chem.* 1942, 46 (1), 151−158.

(14) Bae, Y. C.; Shim, J. J.; Soane, D. S.; Prausnitz, J. M. Representation of Vapor−Liquid and Liquid−Liquid Equilibria for Binary Systems Containing Polymers: Applicability of an Extended Flory−Huggins Equation. *J. Appl. Polym. Sci.* 1993, 47 (7), 1193−1206.

(15) Bae, Y. C. Applicability of the Extended Flory-Huggins Equation for Molecular Weight Dependence of Liquid-Liquid Equilibria in Binary Polymer Solutions. *J. Ind. Eng. Chem.* 1995, 1 (1), 18−27.

(16) Jung, J. G.; Bae, Y. C. Liquid−Liquid Equilibria of Polymer Solutions: Flory-Huggins with Specific Interaction. *J. Polym. Sci., Part B: Polym. Phys.* 2010, 48 (2), 162−167.

(17) Schuld, N.; Wolf, B. A. Solvent Quality as Reflected in Concentration-and Temperature-Dependent Flory−Huggins Interaction Parameters. *J. Polym. Sci., Part B: Polym. Phys.* 2001, 39 (6), 651−662.

(18) Janssen, S.; Schwahn, D.; Mortensen, K.; Springer, T. Pressure Dependence of the Flory-Huggins Interaction Parameter in Polymer Blends: A SANS Study and a Comparison to the Flory-Orwoll-Vrij Equation of State. *Macromolecules* 1993, 26 (21), 5587−5591.

(19) Audus, D. J.; De Pablo, J. J. Polymer Informatics: Opportunities and Challenges. *ACS Macro Lett.* 2017, 6 (10), 1078−1082.

(20) Gormley, A. J.; Webb, M. A. Machine Learning in Combinatorial Polymer Chemistry. *Nat. Rev. Mater.* 2021, 6, 642−644.

(21) Kumar, J. N.; Li, Q.; Jun, Y. Challenges and Opportunities of Polymer Design with Machine Learning and High Throughput Experimentation. *MRS Commun.* 2019, 9 (2), 537−544.

(22) Jha, A.; Chandrasekaran, A.; Kim, C.; Ramprasad, R. Impact of Dataset Uncertainties on Machine Learning Model Predictions: The Example of Polymer Glass Transition Temperatures. *Model. Simul. Mater. Sci. Eng.* 2019, 27 (2), 24002.

(23) Alcobaca, E.; Mastelini, S. M.; Botari, T.; Pimentel, B. A.; Cassar, D. R.; de Leon Ferreira, A. C. P.; Zanotto, E. D. Explainable Machine Learning Algorithms for Predicting Glass Transition Temperatures. *Acta Mater.* 2020, 188, 92−100.

(24) Tao, L.; Varshney, V.; Li, Y. Benchmarking Machine Learning Models for Polymer Informatics: An Example of Glass Transition Temperature. *J. Chem. Inf. Model* 2021, 61 (11), 5395−5413.

(25) Wu, S.; Kondo, Y.; Kakimoto, M.; Yang, B.; Yamada, H.; Kuwajima, I.; Lambard, G.; Hongo, K.; Xu, Y.; Shiomi, J.; et al. Machine-Learning-Assisted Discovery of Polymers with High Thermal Conductivity Using a Molecular Design Algorithm. *Npj Comput. Mater.* 2019, 5 (1), 1−11.

(26) Jordan, B.; Gorji, M. B.; Mohr, D. Neural Network Model Describing the Temperature-and Rate-Dependent Stress-Strain Response of Polypropylene. *Int. J. Plast* 2020, 135, 102811.

(27) Batra, R.; Dai, H.; Huan, T. D.; Chen, L.; Kim, C.; Gutekunst, W. R.; Song, L.; Ramprasad, R. Polymers for Extreme Conditions Designed Using Syntax-Directed Variational Autoencoders. *Chem. Mater.* 2020, 32 (24), 10489−10500.

(28) Kumar, J. N.; Li, Q.; Tang, K. Y. T.; Buonassisi, T.; Gonzalez-Oyarce, A. L.; Ye, J. Machine Learning Enables Polymer Cloud-Point Engineering via Inverse Design. *npj Comput. Mater.* 2019, 5 (1), 1−6.

(29) Rogers, D.; Hahn, M. Extended-Connectivity Fingerprints. *J. Chem. Inf. Model* 2010, 50 (5), 742−754.

(30) Ethier, J. G.; Casukhela, R. K.; Latimer, J. J.; Jacobsen, M. D.; Shantz, A. B.; Vaia, R. A. Deep Learning of Binary Solution Phase Behavior of Polystyrene. ACS Macro Lett. 2021, 10, 749−754.

(31) Wohlfarth, C. CRC Handbook of Liquid-Liquid Equilibrium Data of Polymer Solutions; CRC Press, 2007.

(32) Szydlowski, J.; Van Hook, W. A. Isotope and Pressure Effects on Liquid-Liquid Equilibria in Polymer Solutions: H/D Solvent Isotope Effects in Acetone-Polystyrene Solutions. Macromolecules 1991, 24 (17), 4883−4891.

(33) Szydlowski, J.; Rebelo, L. P.; Van Hook, W. A. A New Apparatus for the Detection of Phase Equilibria in Polymer Solvent Systems by Light Scattering. Rev. Sci. Instrum. 1992, 63 (2), 1717−1725.

(34) RDKit: Open-Source Cheminformatics Software. http://www.rdkit.org.

(35) Chen, T.; Guestrin, C. Xgboost: A Scalable Tree Boosting System. Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining 2016, 785−794.

(36) Abadi, M.; Agarwal, A.; Barham, P.; Brevdo, E.; Chen, Z.; Citro, C.; Corrado, G. S.; Davis, A.; Dean, J.; Devin, M. Tensorflow: Large-Scale Machine Learning on Heterogeneous Distributed Systems. arXiv, arXiv1603.04467, 2016. https://arxiv.org/abs/1603.04467.

(37) Bergstra, J.; Yamins, D.; Cox, D. In Making a Science of Model Search: Hyperparameter Optimization in Hundreds of Dimensions for Vision Architectures, International Conference on Machine Learning; 2013; pp 115−123.

(38) Hino, T.; Lambert, S. M.; Soane, D. S.; Prausnitz, J. M. Lattice Thermodynamics for Binary Closed-Loop Equilibria: Ordinary and Polymer Systems. AIChE J. 1993, 39 (5), 837−845.

(39) Clark, G. N. I.; Galindo, A.; Jackson, G.; Rogers, S.; Burgess, A. N. Modeling and Understanding Closed-Loop Liquid- Liquid Immiscibility in Aqueous Solutions of Poly (Ethylene Glycol) Using the SAFT-VR Approach with Transferable Parameters. Macromolecules 2008, 41 (17), 6582−6595.

(40) Wildman, S. A.; Crippen, G. M. Prediction of Physicochemical Parameters by Atomic Contributions. J. Chem. Inf. Comput. Sci. 1999, 39 (5), 868−873.

██ Recommended by ACS

### Representing Polymers as Periodic Graphs with Learned Descriptors for Accurate Polymer Property Predictions
Evan R. Antoniuk, Anna M. Hiszpanski, et al.
OCTOBER 31, 2022
JOURNAL OF CHEMICAL INFORMATION AND MODELING
READ ⧉

### A Self-Consistent Field Theory Formalism for Sequence-Defined Polymers
Oliver Xie and Bradley D. Olsen
JULY 21, 2022
MACROMOLECULES
READ ⧉

### Validation and Refinement of Unified Analytic Model for Flexible and Semiflexible Polymer Melt Entanglement
Joseph D. Dietz, Robert S. Hoy, et al.
APRIL 20, 2022
MACROMOLECULES
READ ⧉

### Compatibilization Efficiency of Graft Copolymers in Incompatible Polymer Blends: Dissipative Particle Dynamics Simulations Combined with Machine Learning
Tianhang Zhou, Florian Müller-Plathe, et al.
SEPTEMBER 01, 2022
MACROMOLECULES
READ ⧉

Get More Suggestions >