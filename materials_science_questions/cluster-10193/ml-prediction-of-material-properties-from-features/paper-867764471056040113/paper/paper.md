# MeltNet: Predicting alloy melting temperature by machine learning

Pin-Wen Guan$^{1, \text{a)}}$ and Venkatasubramanian Viswanathan$^{1,2,3}$

$^{1)}$Department of Mechanical Engineering, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, USA
$^{2)}$Wilton E. Scott Institute for Energy Innovation, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, USA
$^{3)}$Department of Physics, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, US

(Dated: 28 October 2020)

Thermodynamics is fundamental for understanding and synthesizing multi-component materials, while efficient and accurate prediction of it still remain urgent and challenging. As a demonstration of the "Divide and conquer" strategy decomposing a phase diagram into different learnable features, quantitative prediction of melting temperature of binary alloys is made by constructing the machine learning (ML) model "MeltNet" in the present work. The influences of model hyperparameters on the prediction accuracy is systematically studied, and the optimal hyperparameters are obtained by Bayesian optimization. A comprehensive error analysis is made on various aspects including training duration, chemistry and input features. It is found that except a few discrepancies mainly caused by less satisfactory treatment of metalloid/semimetal elements and large melting point difference with poor liquid mixing ability between constituent elements, MeltNet achieves overall success in prediction, especially capturing subtle composition-dependent features in the unseen chemical systems for the first time. The reliability, robustness and accuracy of MeltNet is further largely boosted by introducing the ensemble method with uncertainty quantification. Based on the state-of-the-art underlying techniques, MeltNet achieves a prediction mean average error (MAE) as low as about 120 K, at a minimal computational cost. We believe the present work has a general value for significant acceleration of predicting thermodynamics of complicated multi-component systems.

## I. INTRODUCTION

Thermodynamics is one of the foundations for understanding materials. It offers the knowledge about phases or structures formed under different condition variables such as composition, temperature, pressure and electric potential, from which people can optimize the conditions to obtain the structures with desirable properties. Thus, predicting thermodynamics of materials has great value in both scientific and practical aspects, although it is also a challenging task due to many variables and underlying mechanisms (lattice disorder, atomic vibration, electronic excitation, magnetic excitation, etc.) involved. So far, there have been two major approaches for this task, ab initio thermodynamic calculations and empirical/semi-empirical calculations represented by the CALPHAD (CALculation of PHAse Diagrams) method. In spite of gaining considerable success, there are still some issues for these approaches. Ab initio thermodynamic calculations are generally time-consuming and vulnerable to errors for complicated multi-component systems, and even for a simple binary metallic system, it may lead to incorrect results due to accuracy limitations$^1$. For the CALPHAD method, one of the disadvantages is that it is highly relied on critical assessment of a blend of data from different sources accomplished by human beings$^2$, which is not efficient and may be subject to lack of data, and therefore quite challenging for high-throughput modeling of high dimensional systems such as high entropy alloys (HEAs)$^3$. Therefore, it is urgent to develop a novel approach to model thermodynamics of materials with both efficiency and accuracy. A promising tool to meet this need is machine learning (ML), which has recently shown increasing potential to revolutionize physical sciences including materials science$^4$. Especially, it sheds a light in solving high dimensional problems, which are otherwise almost intractable.

There have been considerable efforts in applying ML to thermodynamics of materials, which can be classified into two categories based on the quantity learned by ML. In the first category thermochemical quantities such as formation enthalpy$^{5-8}$, Gibbs energy$^9$ and formation entropy$^{10}$ are learned, based on which the phase diagrams may be obtained$^7$. This category can be also generalized to cover the cases where a customized quantity measuring phase stability is learned, such as site likelihood$^{11}$ and entropy-forming ability$^{12}$. In the second category, the phase equilibrium is learned directly$^{13-16}$. The first category is obviously more physics-based, but thermochemical quantities are usually complicated and may be challenging to learn for multi-component non-stoichiometric phases. In addition, in both categories, temperature is usually absent in the models in practice, which is an apparent drawback from the perspective of thermodynamics.

Predicting phase diagrams of complicated multi-component systems directly by ML is also challenging. To reduce the difficulty, the old wisdom "Divide and conquer" may be a viable strategy, i.e., decomposing a phase diagram into different features learned by different ML models respectively. As a first attempt to realize this strategy, quantitative prediction of melting temperature of binary alloys is made by constructing a ML model termed "MeltNet" in the present work. Melting temperature is an important phase equilibrium feature defining the boundary between two fundamental states of condense matter, as well as a critical parameter in many important applications such as solder materials, metallic glass$^{17}$ and room-temperature liquid metal electrodes (LME) for rechargeable batteries$^{18}$. It is noted that there have been a few works on predicting melting points of binary compounds by ML$^{15,16}$, but they have very strict constraints on the stoichiometry, and there-

$^{\text{a)}}$Electronic mail: pinweng@andrew.cmu.edu

![](./images/867764471056040113_1.jpg)

FIG. 1. Distribution of elements in the systems studied in the present work. The number under the name of each element represents the times of that element appearing in the studied systems, which is also indicated by the color. The elements with grey color are not involved in the present work.

fore lacks generalizability in arbitrary chemical compositions present in the MeltNet.

## II. COMPUTATIONAL METHODS

### A. Data generation
For alloy systems, the melting temperature is generally an interval bounded by the liquidus and the solidus instead of a single value. To simplify the problem, the treatment by Chelikowsky and Anderson¹⁹ is adopted in the present study, i.e., defining the liquidus as the melting temperature. The tdb files are retrieved from NIMS Computational Phase Diagram Database (https://cpddb.nims.go.jp/en/), from which the liquidus of each binary system is calculated using pycalphad²⁰. There are 287 different binary alloy systems collected in total, involving 57 elements with distribution shown in fig. 1. The non-metal elements are absent except B and Si, but the methodology described in the present work should be also applicable to them. The composition is sampled in a step of 0.01 from 0 to 1 with the endmembers excluded, resulting 99 samples per system. However, a tiny portion of calculations are abnormal and therefore removed. Finally, a total of 28148 data was generated, which consist of a large database for the subsequent study.

### B. ML model
The deep neural network (DNN) is employed as the ML model and termed MeltNet in the present work, and is implemented in PyTorch²¹. Seven descriptors are used as the inputs for MeltNet, including the valence electron concentration VEC, electronegativity difference $\Delta \chi$, atomic radius difference $\delta$, ideal mixing entropy $\Delta S_{mix}$, formation enthalpy $\Delta H_f$, average fusion entropy $S^{fus}$, fusion entropy weighted average melting point $\tilde{T}$. Among them, VEC, $\Delta \chi$, $\delta$ and $\Delta S_{mix}$ adopt the definitions in the reference¹⁴, while $\Delta H_f$ is taken from the Materials Project database²². The following definitions are used for a n-component system:

$$
S^{f u s}=\sum_{i=1}^{n} c_{i} S_{i}^{f u s}
$$

$$
\tilde{T}=\frac{\sum_{i=1}^{n} c_{i} S_{i}^{f u s} T_{i}}{S^{f u s}}
$$

where $c_i$, $S_i^{fus}$ and $T_i$ are the concentration, fusion entropy and melting point of the element i, respectively. Some rationales can be given for selecting the above descriptors. VEC, $\Delta \chi$, $\delta$ and $\Delta H_f$ are all relevant to stability of the solid phases. $\Delta S_{mix}$ is related to stability of both solid and liquid solutions. $S^{fus}$ describes the basic part of fusion entropy contributed by the linear mixing between elements. $\tilde{T}$ would be the true melting temperature if both fusion entropy and fusion enthalpy contain only the contribution from the linear mixing between elements. It is noted that the definitions of all the descriptors are general for any multi-component system without restriction on the number of components, although only binary systems are studied in this work. In addition, for convenience in later discussions, the average melting point based on the Vegard's law is defined by

$$
\bar{T}=\sum_{i=1}^{n} c_{i} T_{i}
$$

and the excess melting point, i.e., the deviation of the true melting point $T$ from $\bar{T}$ is defined by

$$
\Delta T=T-\bar{T}
$$

which is the object variable to be learned by MeltNet. The error or the loss function is defined as the L1-norm loss, i.e.,

$$
\varepsilon=\sum_{i=1}^{m} \frac{\left|\widehat{\Delta T}_{i}-\Delta T_{i}\right|}{m}
$$

where m is the number of data in the dataset, and $\widehat{\Delta T}_{i}$ is an estimation for $\Delta T_{i}$.

### C. Bayesian optimization of hyperparameters
There are multiple hyperparameters in MeltNet and its training process, with the important ones including: (1) number of hidden layers, (2) number of nodes in each layer, (3) momentum, (4) batch size, (5) learning rate, and 6) weight of decay. These hyperparameters form a high-dimension space, for which the optimization is quite challenging. To accomplish this task, a very useful black-box global optimization technique, the Bayesian optimization method was employed by using the Dragonfly package²³. In the Bayesian optimization, every evaluation of the objective function (the test error as a function of hyperparameters here) at some point is used to update the posterior distribution over the objective function, from which an acquisition function is constructed to determine the next point

of evaluation. The posterior distribution over the objective function is calculated based on the Gaussian process. The optimization is implemented in two stages. In stage 1, the six hyperparameters listed above are optimized simultaneously, assuming the number of nodes in each layer is a constant. In stage 2, all the hyperparameters are fixed at the optimized values obtained from stage 1, except that the number of nodes in each layer can be changed independently and treated as optimization variables. The architecture of MeltNet with Bayesian optimization of hyperparameters used in the present work is illustrated in fig. 2.

### D. Uncertainty quantification
The ML model can be largely influenced by the choice of samples for training. To quantify the uncertainty associated with such choice, the ensemble approach was employed here, which has been applied successfully in other fields of computational materials science, e.g., the Bayesian Error Estimation Functional (BEEF) where an ensemble of density functionals are used to estimate the exchange-correlation errors²⁴. Especially, the ensemble approach has been applied in thermochemical properties²⁵ and phase diagrams²⁶,²⁷. In the present work, the training dataset was sampled randomly for 100 times forming 100 subsets, and each subset contains 75% of the total training data. Each subset was used for training a set of MeltNet parameters. As a result, an ensemble of 100 sets of MeltNet parameters can be obtained, providing an ensemble of 100 predictions. The average and standard deviation of the prediction ensemble can then be calculated, with the latter taken as the uncertainty of the prediction.

## III. RESULTS AND DISCUSSION
### A. Baseline prediction and trends in melting temperatures
The simplest prediction one can imagine is probably the average melting point based on the Vegard's law $\bar{T}$, which is considered as the baseline in this work. fig. 3 shows the relationship between $\bar{T}$ and the true melting point $T$. Due to the large amount of the total data, only the data with equal molar composition is shown. The MAE of the Vegard's prediction on the whole dataset is 218 K, which is quite significant. It is noted that the deviation of $\bar{T}$ from $T$ is not symmetric, and $\bar{T}$ has a larger tendency to be an underestimation of $T$ due to the physical constraint that $T$ is always above 0 K while it has no apparent upper limit.

Before the ML prediction, it is beneficial to have a rough overview about the relation between the melting point and each individual feature (fig. 4). Due to the large amount of the total data, only the data with equal molar composition is shown, and the mixing entropy $\Delta S_{mix}$ is therefore absent from the shown features. It is found that the excess melting point $\Delta T$ has weak one-to-one correlation with $\Delta \chi$, $\delta$ and $S^{fus}$, which is somewhat against intuition, since at least $\Delta \chi$ and $\delta$ are considered as important factors affecting stability of compounds and alloys and therefore the melting point. On the other hand, lack of one-to-one correlation does not necessarily mean lack of correlation, which may be via complicated synergy with other features. For the three features, VEC, $\Delta H_f$ and $\bar{T}$, negative one-to-one correlation with $\Delta T$ can be observed, though not highly significant. An intuitive explanation is that, high-VEC elements, e.g., transition metals, usually have high melting points, making the baseline $\bar{T}$ high, therefore the "chance" to have more negative $\Delta T$ is higher. The effect of $\bar{T}$ can be also understood in a similar way. The effect of $\Delta H_f$ is more obvious: a more negative $\Delta H_f$ means stronger stability of the solid at the corresponding composition, and therefore more positive $\Delta T$. A previous work attempted to correlate binary alloy melting points with chemical coordinates consisting of 10 properties such as atomic radii and bulk moduli (VEC was not included), but only poor correlation was found except for cohesive energies and elemental melting points¹⁹, which is in consistence with the present observations.

### B. Optimization, training and factors affecting errors
In stage 1 of Bayesian optimization of hyperparameters of the DNN model where the number of nodes in each hidden layer is equal, the optimization was run for 100 iterations. The searching space is 20-50 for the number of nodes per hidden layer, 3-6 for the number of hidden layers, 0.1-0.9 for the momentum, $2^n$ (n=5,6,7,8,9) for the mini-batch size, 0.01-0.2 for the learning rate, and $10^{-4}-10^{-3}$ for the weight-decay factor. Based on the data generated in the optimization, the relation between the test error and the hyperparameters is visualized in the parallel coordinates diagram (fig. 5). It should be noted that the space of hyperparameters is not homogeneously sampled. Instead, the space region with higher probability to minimize the test error is more likely sampled due to the algorithm of Bayesian optimization²³. Interestingly, though the depth of a DNN is generally considered as one of its important advantages, it is found that the test error is not sensitive to the number of hidden layers in the present case. In contrast, the number of nodes per hidden layer has very significant influences on the test error. To minimize the test error, a relatively large number of nodes per hidden layer is preferred. A small enough mini-batch size and a low learning rate are also preferred, while the momentum and the weight-decay factor does not matter too much. Finally, a 3-hidden-layer DNN with 48 nodes per hidden layer trained with 32 of the mini-batch size, 0.01 of the learning rate, 0.5 of the momentum and $6*10^{-4}$ of the weight-decay factor is found to be optimal in the search. In stage 2, the numbers of nodes of different hidden layers were allowed different, but no further decrease of the test error was detected. Therefore, the optimal DNN from stage 1 is adopted as the working model of MeltNet in the present study.

To avoid bias introduced by the partition of the training/test sets, the cross validation method was employed, where the total 287 binary systems were randomly partitioned into five subsets, leading to five training-test dataset pairs, in each of which one subset was used as the test set and the other four subsets formed the training set together. fig. 7 shows the evolution of training and test errors in the training process for the five training-test dataset pairs. It can be seen that the test errors have modest variation be-

![](./images/867764471056040113_2.jpg)

FIG. 2. Architecture of MeltNet with Bayesian optimization of hyperparameters. The input features are described in the main text.

![](./images/867764471056040113_3.jpg)

FIG. 3. Parity plot between the true melting point and the prediction based on Vegard's law. The shown data points are those with equal molar composition.

tween the dataset pairs, but the training errors are very similar. After rapid decrease in the initial tens of epochs, the training errors continue to decrease slowly, but the test errors almost stop decreasing, and some dataset pairs even exhibit overfitting behavior.

To further clarify how the test errors depend on the underlying chemistry, the system-resolved test MAE is calculated for all the 287 systems and ranked within the test set of the corresponding dataset pairs (fig. 6). The MeltNet predictions for the majority of the studied systems have a test MAE within about 200 K, indicating an improvement on the baseline average MAE, 218 K, which demonstrates the success of MeltNet in predicting the unseen chemistry. However, the MeltNet predictions are still not satisfactory for some systems, with five systems B-Mg, B-Nd, Ce-Cr, Mg-Zr and B-Ga being the most problematic. Interestingly, three out of these five systems contain the element boron, a metalloid with properties between those of metals and non-metals. It is worth noting that for the B-Nd system, there are considerable discrepancies between different sources in the literature. The true value adopted in the present study is calculated based on the work by Hallemans et al.²⁸, where the liquidus line in the intermediate and Nd-rich compositions is higher than that in a work²⁹ published later by several hundreds of kelvin. In other words, more experimental and theoretical efforts are needed to clarify the origin of the large prediction error for the B-Nd system. The Mg-Zr system and the Ce-Cr system both consist of a low-melting-point element and a high-melting-point element, as well as have weak liquid mixing ability characterized by the liquid miscibility gap. The present model fails to capture such scenario, which will be subject to future study and improvement.

For better understanding of the origins of the errors, the data with equal molar composition is plotted in the pair plot of the features, with the test error represented by the color of the data point. There is no significant correlation between the test error and the features, except that it is quite evident that a higher fusion entropy averaged from the constituent elements by their compositions, $S^{fus}$, tends to lead to larger test errors. According to Fig. S1 (see Supplementary material), the elements with high fusion entropy can be roughly classified into two large classes, metalloids/semimetals (e.g., Bi, Sn, Ge, Si, Ga, B, Sb) and refractory metals (e.g., Os, Ru, Ir, Mo, W). The cases where large test errors occur usually belong to the first class. Obviously, the chemical nature of the systems containing metalloids/semimetals are quite different from that of the systems containing metals exclusively, making the predictions more challenging.

![](./images/867764471056040113_4.jpg)

FIG. 4. Relation between the excess melting temperature and the input features. The shown data points are those with equal molar composition.

![](./images/867764471056040113_5.jpg)

FIG. 5. Relation between the test errors (in K) and the hyperparameters of MeltNet.

### C. Predictions by MeltNet

The predicted melting points of selected systems are presented in fig. 9 as examples, with the true melting points adopted in the present work also shown. These selected systems are sampled from the test set of the first training-test dataset pair ranked in alphabetical order with the equal sampling interval to reduce possible bias. In the single prediction, the whole training set was used to train a single DNN model resulting in a single prediction, while in the ensemble prediction, the whole training set was sampled to generate multiple subsets to train an ensemble of DNN models resulting in an ensemble of predictions. The ensemble standard deviation is used to quantify the uncertainty associated with the training data, which is represented by the red shadow area. It can be seen that for most systems, both types of predictions achieve general agreement with the true values, at least semi-quantitatively. Especially, the kinks in the melting point curve are usually well captured by the predictions, which is quite non-trivial and encouraging, provided these test systems are unseen for MeltNet. To the best of our knowledge, successful ML prediction of such subtle composition-dependent features of thermodynamic equilibrium is unprecedented. It is also worth noting that although the present dataset is quite large, the number ( 230) of systems used for training is still a small portion ( 14%) compared with the number (1596) of all the binary systems that can be formed from the studied 57 elements, implying good generalizability of MeltNet. Admittedly, some quantitative discrepancies still

![](./images/867764471056040113_6.jpg)

FIG. 6. Test errors for each system in the five training-test dataset pairs, in each of which one subset was used as the test set and the other four subsets formed the training set together.

![](./images/867764471056040113_7.jpg)

FIG. 7. Evolution of errors during training for the five training-test dataset pairs.

exist. For example, in the Ag-Nd system, the "valley" in the Nd-rich side and the "twin peaks" in the intermediate compositions and Ag-rich side are all captured by the predictions and the depth of the "valley" is also well predicted, but the height of the "twin peaks" is underestimated. In addition, the predicted positions of the kinks sometimes have minor shift compared with the true values. The most unsatisfactory performance of the present model is for the Cr-Sn and Si-Sn systems, both of which are combinations of a low-melting-point element and a high-melting-point element with weak liquid mixing ability and therefore cannot be well reproduced by the present predictions as discussed above.

In terms of the two types of predictions, it is found that the ensemble prediction is obviously superior to the single prediction. The ensemble prediction provides uncertainty guiding the decision that how much confidence should be given to the prediction. For example, in the Au-In system, there are considerable errors in the prediction of the "bump" in the In-rich side, but the large uncertainty reminds one to prudently assess the prediction, while the small uncertainty in the Au-rich side is in line with the high accuracy of the prediction. However, it should be pointed out that the uncertainty here is only associated with the training data, which does not cover all the sources of uncertainty such like the model itself. Thus, it is not guaranteed that the true values can be always bounded by the uncertainty of the present ensemble prediction, as shown by the Cr-Sn and Si-Sn systems. Another significant advantage of the ensemble prediction is that it is more robust and less noisy, as evident by the smooth behavior of the ensemble average compared with the spurious behavior of the single prediction. In fact, as shown in Table 1, the ensemble average has considerably smaller test MAE (122.5 K) than the single prediction (133.1 K) in overall and performs invariantly better in each test in the five-fold cross validation. The average uncertainty of the ensemble prediction is 74.7 K in overall and does not change too much across the tests in the cross validation. Based on these observations, it is implied that the ensemble approach should be routinely employed in the ML prediction of thermodynamics. Compared with the test MAE by the baseline prediction based on the Vegard's law (218.0 K), MeltNet significantly improves the prediction accuracy, at expense of little increase in computational costs, which is vital important for complicated multi-component systems.

![](./images/867764471056040113_8.jpg)

FIG. 8. Relation between the test errors and the combination of any two input features. The shown data points are those with equal molar composition.

## IV. CONCLUSIONS

To make complicate phase equilibria of multi-component systems learnable, the "Divide and conquer" strategy is proposed in the present work, where the whole phase diagram is decomposed into different phase equilibria features which are relatively easy to learn by ML. As one of the most important phase equilibria features, the melting point is chosen as the first example to demonstrate the state-of-the-art methodology for such kind of problems. MeltNet, a DNN model with seven input features is constructed, with the optimal hyperparameters obtained from Bayesian optimization. The number of nodes per hidden layer, mini-batch size and learning rate are found crucial for the model performance. Five-fold cross validation is employed to reduce bias related to training-test dataset partition. A thorough analysis is made for the dependence of the prediction errors on various aspects including hyperparameters, training duration, chemistry and input features. It is found that large prediction errors mainly originate from less satisfactory treatment of metalloid/semimetal elements and large melting point difference with poor liquid mixing ability between constituent elements. Despite a minority of failures and some quantitative discrepancies, MeltNet offers satisfactory predictions in general, especially capable of capturing subtle composition-dependent features successfully for the first time. It is also found that the ensemble prediction is more reliable, robust and accurate with uncertainty quantification. The prediction MAE by MeltNet is as low as about 120 K, at a negligible computational cost compared with other methods. We believe the present work sets a solid cornerstone for ML of thermodynamics of complicated multi-component systems.

## V. SUPPLEMENTARY MATERIAL

See Supplementary Material for detailed descriptions of data used in this work, and the results not covered in the main text.

## VI. ACKNOWLEDGEMENT

This work was partially supported by the Assistant Secretary for Energy Efficiency and Renewable Energy, Office of Vehicle Technologies of the U.S. Department of Energy (DOE) through the Advanced Battery Materials Research (BMR) Program under Contract No. DE-EE0007810. Acknowledgment is also made to the Extreme Science and Engineering Discovery Environment (XSEDE) for pro-

![](./images/867764471056040113_9.jpg)

FIG. 9. Predicted vs true melting point for nine sample systems. The red shadow area represents uncertainty associated with the choice of training data in the ensemble prediction.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Test 1</th>
      <th>Test 2</th>
      <th>Test 3</th>
      <th>Test 4</th>
      <th>Test 5</th>
      <th>Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Size</td>
      <td>5683</td>
      <td>5672</td>
      <td>5599</td>
      <td>5604</td>
      <td>5590</td>
      <td>28148</td>
    </tr>
    <tr>
      <td>$\varepsilon_{baseline}$ (K)</td>
      <td>225.2</td>
      <td>254.5</td>
      <td>195.5</td>
      <td>179.5</td>
      <td>235.0</td>
      <td>218.0</td>
    </tr>
    <tr>
      <td>$\varepsilon_{MeltNet}^{single}$ (K)</td>
      <td>130.8</td>
      <td>143.3</td>
      <td>125.8</td>
      <td>116.6</td>
      <td>148.9</td>
      <td>133.1</td>
    </tr>
    <tr>
      <td>$\varepsilon_{MeltNet}^{ensemble}$ (K)</td>
      <td>123.8</td>
      <td>133.3</td>
      <td>109.6</td>
      <td>104.2</td>
      <td>141.7</td>
      <td>122.5</td>
    </tr>
    <tr>
      <td>$\sigma_{MeltNet}^{ensemble}$ (K)</td>
      <td>70.1</td>
      <td>75.5</td>
      <td>75.7</td>
      <td>77.8</td>
      <td>74.4</td>
      <td>74.7</td>
    </tr>
  </tbody>
</table>

TABLE I. Comparison between different methods in predicting melting temperatures for the five training-test dataset pairs, listing test errors by baseline prediction based on the Vegard's law $\varepsilon_{baseline}$, single prediction by MeltNet $\varepsilon_{MeltNet}^{single}$, and ensemble average prediction by MeltNet $\varepsilon_{MeltNet}^{ensemble}$. The size of each test dataset and the uncertainty associated with the choice of training data in the ensemble prediction $\sigma_{MeltNet}^{ensemble}$ are also listed.

viding computational resources through Award No. TG-CTS180061.

$^{1}$E. Decolvenaere, M. J. Gordon, and A. Van der Ven, "Testing pre- dictions from density functional theory at finite temperatures: $\beta 2$-like ground states in Co-Pt," Physical Review B 92, 085119 (2015).

$^{2}$H. L. Lukas, S. G. Fries, and B. Sundman, Computational thermody- namics: the CALPHAD method, Vol. 131 (Cambridge University Press, Cambridge, 2007) p. 324.

$^{3}$D. Miracle, "High entropy alloys as a bold step forward in alloy devel- opment," Nature communications 10, 1-3 (2019).

$^{4}$J. Schmidt, M. R. Marques, S. Botti, and M. A. Marques, "Recent advances and applications of machine learning in solid-state materials science," npj Computational Materials 5, 1-36 (2019).

$^{5}$J. Schmidt, J. Shi, P. Borlido, L. Chen, S. Botti, and M. A. Marques, "Predicting the thermodynamic stability of solids combining density functional theory and machine learning," Chemistry of Materials 29, 5090-5103 (2017).

$^{6}$W. Ye, C. Chen, Z. Wang, I.-H. Chu, and S. P. Ong, "Deep neural networks for accurate predictions of crystal stability," Nature commu- nications 9, 1-6 (2018).

$^{7}$D. Jha, L. Ward, A. Paul, W.-k. Liao, A. Choudhary, C. Wolverton, and A. Agrawal, "Elemnet: Deep learning the chemistry of materials from only elemental composition," Scientific reports 8, 1-13 (2018).

$^{8}$S. Ubaru, A. Miedlar, Y. Saad, and J. R. Chelikowsky, "Formation enthalpies for transition metal alloys using machine learning," Physical Review B 95, 214102 (2017).

$^{9}$G. H. Teichert, A. Natarajan, A. Van der Ven, and K. Garikipati, "Ma- chine learning materials physics: Integrable deep neural networks en- able scale bridging by learning free energy functions," Computer Meth- ods in Applied Mechanics and Engineering 353, 201-216 (2019).

$^{10}$C. Lapointe, T. D. Swinburne, L. Thiry, S. Mallat, L. Proville, C. S. Becquart, and M.-C. Marinica, "Machine learning surrogate models for prediction of point defect vibrational entropy," Physical Review Mate- rials 4, 063802 (2020).

$^{11}$K. Ryan, J. Lengyel, and M. Shatruk, "Crystal structure prediction via deep learning," Journal of the American Chemical Society 140, 10158-10168 (2018).

$^{12}$K. Kaufmann, D. Maryanovsky, W. M. Mellor, C. Zhu, A. S. Rosen- garten, T. J. Harrington, C. Oses, C. Toher, S. Curtarolo, and K. S. Vecchio, "Discovery of high-entropy ceramics via machine learning," Npj Computational Materials 6, 1-9 (2020).

$^{13}$Y. Zhang, C. Wen, C. Wang, S. Antonov, D. Xue, Y. Bai, and Y. Su, "Phase prediction in high entropy alloys with a rational selection of materials descriptors and machine learning models," Acta Materialia 185, 528-539 (2020).

$^{14}$W. Huang, P. Martin, and H. L. Zhuang, "Machine-learning phase pre- diction of high-entropy alloys," Acta Materialia 169, 225-236 (2019).

$^{15}$G. Pilania, J. E. Gubernatis, and T. Lookman, "Structure classifica- tion and melting temperature prediction in octet ab solids via machine learning," Physical Review B 91, 214302 (2015).

$^{16}$A. Seko, T. Maekawa, K. Tsuda, and I. Tanaka, "Machine learning with systematic density-functional theory calculations: Application to melting temperatures of single-and binary-component solids," Physical Review B 89, 054303 (2014).

$^{17}$A. Dasgupta, S. R. Broderick, C. Mack, B. U. Kota, R. Subramanian, S. Setlur, V. Govindaraju, and K. Rajan, "Probabilistic assessment of glass forming ability rules for metallic glasses aided by automated anal- ysis of phase diagrams," Scientific reports 9, 1-12 (2019).

$^{18}$X. Guo, L. Zhang, Y. Ding, J. B. Goodenough, and G. Yu, "Room- temperature liquid metal and alloy systems for energy storage applica- tions," Energy & Environmental Science 12, 2605-2619 (2019).

$^{19}$J. R. Chelikowsky and K. E. Anderson, "Melting point trends in inter- metallic alloys," Journal of Physics and Chemistry of Solids 48, 197-205 (1987).

$^{20}$R. Otis and Z.-K. Liu, "pycalphad: CALPHAD-based Computational Thermodynamics in Python," Journal of Open Research Software 5, 1(2017).

$^{21}$A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. D. Facebook, A. I. Research, Z. Lin, A. Desmaison, L. Antiga, O. Srl, and A. Lerer, "Automatic differentiation in PyTorch," NIPS-W (2017).

$^{22}$A. Jain, S. Ong, G. Hautier, W. Chen, W. Richards, S. Dacek, S. Cho- lia, D. Gunter, D. Skinner, and G. Ceder, "The Materials Project: A materials genome approach to accelerating materials innovation," Apl Materials 1, 11002 (2013).

$^{23}$K. Kandasamy, K. R. Vysyaraju, W. Neiswanger, C. R. Collins, J. Schneider, and E. P. Xing, "Tuning Hyperparameters without Grad Students: Scalable and Robust Bayesian Optimisation with Dragonfly," Tech. Rep. (2020).

$^{24}$J. Wellendorff, K. T. Lundgaard, A. Møgelhøj, V. Petzold, D. D. Lan- dis, J. K. Nørskov, T. Bligaard, and K. W. Jacobsen, "Density function- als for surface science: Exchange-correlation model development with bayesian error estimation," Phys. Rev. B 85, 235149 (2012).

$^{25}$P. W. Guan, G. Houchins, and V. Viswanathan, "Uncertainty quantifi- cation of DFT-predicted finite temperature thermodynamic properties within the Debye model," Journal of Chemical Physics 151, 244702(2019), arXiv:1910.07891.

$^{26}$Y. Yuan, G. Houchins, P.-W. Guan, and V. Viswanathan, "Uncertainty quantification of first principles computational phase diagram predic- tions of li-si system via bayesian sampling," (2020), arXiv:2003.13393[cond-mat.mtrl-sci].

$^{27}$P.-W. Guan, R. J. Hemley, and V. Viswanathan, " $\mathscr{P}^{2}$ : Combining pressure and electrochemistry to synthesize superhydrides," (2020), arXiv:2007.15613 [cond-mat.mtrl-sci].

$^{28}$B. Hallemans, P. Wollants, and J. R. Roos, "Thermodynamic assess- ment of the Fe-Nd-B phase diagram," Journal of Phase Equilibria 16,137-149 (1995).

$^{29}$P. K. Liao, K. E. Spear, and M. E. Schlesinger, "The B-Nd (Boron- Neodymium) system," (1996).

Supporting Information For

MeltNet: Predicting alloy melting temperature by machine learning

Pin-Wen Guan$^{1, \text{a)}}$ and Venkatasubramanian Viswanathan$^{1,2,3}$

$^{1)}$Department of Mechanical Engineering, Carnegie Mellon University, Pittsburgh,
Pennsylvania 15213, USA

$^{2)}$Wilton E. Scott Institute for Energy Innovation, Carnegie Mellon University, Pittsburgh,
Pennsylvania 15213, USA

$^{3)}$Department of Physics, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213,
US

(Dated: 27 October 2020)

$\text{a)}$Electronic mail: pinweng@andrew.cmu.edu

![](./images/867764471056040113_10.jpg)

FIG. S1. Fusion entropy of elements involved in the present study.