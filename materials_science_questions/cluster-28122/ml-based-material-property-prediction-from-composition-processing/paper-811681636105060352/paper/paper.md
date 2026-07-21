# A neural network approach for predicting steel properties characterizing cyclic Ramberg–Osgood equation

R. GHAJAR, N. NASERIFAR, H. SADATI and J. ALIZADEH K.

Material Properties Research Laboratory (MPRL), Department of Mechanical Engineering, K. N. Toosi University of Technology, No. 15, Pardis Street, MollaSadra Ave., Vanak Sq., Tehran, Iran

Received in final form 23 Nov 2010

**ABSTRACT** This paper attempts to demonstrate the applicability of artificial neural networks to the estimation of steel properties, cyclic strain-hardening exponent and cyclic strength coefficient, characterizing cyclic Ramberg–Osgood equation on the basis of monotonic tensile test properties. For this purpose, steel tensile data were extracted from the literature and two separate neural networks were constructed. One set of data was used for training the two networks and the remaining for testing purposes. Regression analysis and mean relative error calculation were used to check the accuracy of the system in the training and testing phases. Comparison of the results obtained from the neural networks and the values obtained from direct fitting of experimental data, indicated the reasonable prediction of cyclic strain-hardening exponent and cyclic strength coefficient, which are often used to characterize the cyclic deformation curve by a Ramberg–Osgood type equation.

Keywords ANN; cyclic strain hardening; fatigue properties; Ramberg–Osgood.

## NOMENCLATURE

$a_i = \text{network output value}$
$b = \text{fatigue strength exponent}$
$b_j = \text{bias term associated with neuron } j$
$BHN = \text{Brinell hardness}$
$c = \text{fatigue ductility exponent}$
$E = \text{modulus of elasticity}$
$f = \text{nonlinear activation function}$
$K' = \text{cyclic strength coefficient}$
$MRE = \text{mean relative error}$
$MSE = \text{mean square error}$
$n = \text{neuron}$
$n' = \text{cyclic strain-hardening exponent}$
$N = \text{total number of training patterns}$
$p_i = \text{input signal generated for neuron } i$
$R = \text{regression result}$
$RA\% = \text{percent reduction in area}$
$S_u = \text{ultimate tensile strength}$
$t_i = \text{target value}$
$w_{ji} = \text{weight from neuron } i \text{ to neuron } j$
$Y_j = \text{output of neuron } j$
$\Delta\varepsilon = \text{cyclic strain range}$
$\Delta\varepsilon/2 = \text{cyclic strain amplitude}$

Correspondence: R. Ghajar. E-mail: ghajar@kntu.ac.ir

$\Delta \sigma = \text{cyclic stress range}$
$\Delta \sigma/2 = \text{cyclic stress amplitude}$
$\varepsilon_a = \text{strain amplitude}$
$\varepsilon'_f = \text{fatigue ductility coefficient}$
$\sigma_a = \text{stress amplitude}$
$\sigma'_f = \text{fatigue strength coefficient}$
$\sigma_y = \text{yield stress}$

## INTRODUCTION

In many field test situations, it may be desirable to convert the measured strains to stress in order to estimate fatigue life. Stress-strain response of some steels can change significantly when subjected to inelastic strains as this may occur at notch roots due to cyclic loading. When fatigue failure occurs, particularly at low cycle fatigue, such inelastic straining is generally present. Hence, the cyclic stress-strain curve may better represent the steel's stress-strain response than the monotonic stress-strain curve. $^1$ The relationship between cyclic strain amplitude, $\Delta \varepsilon/2$, and cyclic stress amplitude, $\Delta \sigma/2$, can be expressed by a Ramberg-Osgood type equation as$^2$:

$$
\frac{\Delta \varepsilon}{2}=\frac{\Delta \sigma}{2 E}+\left(\frac{\Delta \sigma}{2 K^{\prime}}\right)^{1 / n^{\prime}}, \tag{1}
$$

where $K'$ is the cyclic strength coefficient, $n'$ is the cyclic strain-hardening exponent and $E$ is the modulus of elasticity. The two fatigue properties needed in this correlation are $K'$ and $n'$.

The cyclic strength coefficient, $K'$, and the cyclic strain-hardening exponent, $n'$, are often determined from the cyclic stress plastic strain curve. A family of stabilized hysteresis loops at different strain amplitudes can be used to obtain the cyclic stress-strain curve for a given material. The tips from the family of multiple loops are connected, as shown in Fig. 1, to form the cyclic stress-strain curve. Three methods commonly used to obtain the cyclic stress-strain curve are the companion, incremental-step and multiple-step test methods. $^2$ These test methods are time-consuming and the testing equipment is more complicated and expensive than that required for monotonic tension tests, whereas monotonic stress-strain properties are commonly available in handbooks. Therefore, it is more desirable to use approximation methods for estimating the values of $K'$ and $n'$.

An approximation of $K'$ and $n'$ can also be calculated from the low-cycle fatigue properties by using compatibility equations$^2$:

$$
K^{\prime}=\frac{\sigma_{f}^{\prime}}{\left(\varepsilon_{f}^{\prime}\right)^{b / c}}, \tag{2}
$$

$$
n^{\prime}=\frac{b}{c},
$$

where $\sigma'_f$ is the fatigue strength coefficient, $\varepsilon'_f$ is the fatigue ductility coefficient, $b$ is the fatigue strength exponent and $c$ is the fatigue ductility exponent. This estimation method has its problems and errors. It requires, in the first place, the four empirical constants that must be obtained from fatigue tests. Furthermore, estimating cyclic stress-strain curves based on fatigue properties could lead to considerable errors in certain situations. $^3$ So, it is recommended that the values of $K'$ and $n'$ obtained from direct fitting of the experimental data are used in fatigue design rather than those calculated from Eq. (2).$^2$

It is therefore useful to estimate cyclic strength coefficient and cyclic strain-hardening exponent on the basis of monotonic tensile test properties, reported in handbooks or simply obtainable from experiments. By doing so, one can covert the cyclic strain to cyclic stress only by using tensile test properties. Many researchers have attempted to develop relations between tensile and cyclic (fatigue) test properties of materials.$^{4-7}$

The method of artificial neural networks (ANN) has emerged as a powerful new computing technique, which has shown a striking performance when used to model complex nonlinear relationships. Nowadays, neural network models are used for the prediction of mechanical properties.$^{8-16}$ Mathew *et al.* predicted the low cycle fatigue life of 316LN SS by using a neural network model.$^{12}$ Genel indicated that ANN predicted strain-life fatigue properties of steels with high accuracy.$^{13}$

In this study, two separate neural networks were used to investigate the applicability of ANNs to the estimation of the steel $K'$ and $n'$ values on the basis of monotonic tensile test properties. Generalization of the ANN is verified by comprising results of neural network with data set not used in the network's the training process.

© 2011 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct **34**, 534-544

![](./images/811681636105060352_1.jpg)

Fig. 1 Stable hysteresis loops for determining the cyclic stress-strain curve and comparison with the monotonic stress-strain curve. $^{2}$

## ARTIFICIAL NEURAL NETWORK

An ANN is an information processing unit originally intended to simulate the performance and characteristics of the human brain. It is a computational technique able to learn the characteristics of the introduced data to develop a generalization property. ANN consists primarily of three basic elements: neurons, architecture of the net and a learning rule. The most common ANN with widespread use is probably the multi-layer perceptron (MLP) with the back propagation technique as proposed by Rumelhart and McClelland. $^{17}$

The back propagation neural network method is widely used in the field of computational intelligence due to its simplicity and effectiveness so that the theoretical background and various applications of the approach can be found in many volumes of the relative literature. $^{18-20}$ In general, this multi-layered neural network includes the input, hidden, and output layers as shown in Fig. 2. In the calculation process of the problem solving procedure, a specific learning rule is taken for updating the weightings of each layer in accordance with the errors from the network output. The equation for each layer may be written as

$$
Y_{j}=f\left(\sum w_{j i} p_{i}-b_{j}\right), \tag{3}
$$

where $Y_{j}$ is the output of neuron $j$, $w_{j i}$ represents the weight from neuron $i$ to neuron $j$, $p_{i}$ is the input signal generated for neuron $i$, $b_{j}$ is the bias term associated with neuron $j$ and $f$ is the nonlinear activation function. There are several functions, such as step function, sigmoid function, and hyperbolic tangent function that may be chosen as the activation function, but the last one of the form

$$
F(x)=\frac{\exp (x)-\exp (-x)}{\exp (x)+\exp (-x)} \tag{4}
$$

is usually assumed to limit the output value between $-1$ and 1. This transformation is used in this study to make the operating process continuous and differentiable. Mean squared error (MSE) is computed between desired outputs and target outputs and used as the convergence criterion. During the training process, the weights and biases in the network are adjusted to minimize the MSE error, thereby achieving a high performance in the solution. There are various training algorithms used in neural network applications. It is difficult to predict which of these training algorithms will be the fastest one for any specific problem. $^{20}$ In this study, the Levenberg-Marquardt (LM) is used as the training algorithm.

The LM method is based on approaching second-order training speeds without having the computation of second derivatives. The advantage of this training method is that it converges rapidly to the minimum values.

## ANN MODELLING

In this work, the MLP network with back propagation algorithms is used for the estimation of cyclic strain-hardening exponent, $n^{\prime}$, and the cyclic strength coefficient, $K^{\prime}$, of steels. The $K^{\prime}$ and $n^{\prime}$ are estimated by two separate networks. For these estimations, steel tensile data used as input to the ANN model, are extracted from the literature. In order to enhance training performance, both input and output variables are normalized before the network is trained. In order to investigate the

![](./images/811681636105060352_2.jpg)

Fig. 2 A typical multi-layer perceptron neural network architecture.¹⁸

influence of input parameters on the estimation of $n'$ and $K'$, several networks having different combinations of tensile data are considered. The following mean square error (MSE) between the desired output and the ANN response is used:

$$
MSE = \frac{1}{N} \sum_{i=1}^{N} (e_i)^2 = \frac{1}{N} \sum_{i=1}^{N} (t_i - a_i)^2, \tag{5}
$$

where $N$ is the total number of training patterns, $t_i$ is the target (i.e. desired) value and $a_i$ is the network output value. All analyses are performed on a personal computer with 3.4 GHz CPU using an algorithm based on MATLAB code.²¹

## RESULTS AND DISCUSSION
### Estimation of $n'$

In order to evaluate the applicability of ANN to the estimation of $n'$, the available tensile data on 82 steels reported in the literature were used (Table A1).¹,³,⁷ These data included yield stress, $\sigma_y$ (221–2034 MPa); ultimate tensile strength, $S_u$ (345–2586 MPa); Brinell hardness, $BHN$ (80–670); percent reduction in area, $RA\%$ (6–80%); modules of elasticity, $E$ (172–277 GPa); and cyclic strain-hardening exponent, $n'$ (0.05–0.36). Thus, a broad range of steels is used for modelling $n'$. One set of data consisting of 60 values was used for training the network and another consisting of 22 values was used for testing the trained network.

<table>
<caption>Table 1 Network details and architectures of $n'$</caption>
<thead>
<tr>
<th>Input sets</th>
<th>Neurons in the hidden layer</th>
<th>Regression for the training data</th>
<th>Regression for the test data</th>
<th>No. of iterations</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">$\sigma_y, S_u, BHN$</td>
<td>4</td>
<td>0.884</td>
<td>0.640</td>
<td>400</td>
</tr>
<tr>
<td>5</td>
<td>0.908</td>
<td>0.630</td>
<td>382</td>
</tr>
<tr>
<td>6</td>
<td>0.890</td>
<td>0.563</td>
<td>363</td>
</tr>
<tr>
<td>7</td>
<td>0.913</td>
<td>0.716</td>
<td>367</td>
</tr>
<tr>
<td rowspan="5">$\sigma_y, S_u, BHN, RA\%$</td>
<td>4</td>
<td>0.926</td>
<td>0.653</td>
<td>450</td>
</tr>
<tr>
<td>5</td>
<td>0.942</td>
<td>0.739</td>
<td>120</td>
</tr>
<tr>
<td>6</td>
<td>0.969</td>
<td>0.8367</td>
<td>142</td>
</tr>
<tr>
<td>7</td>
<td>0.973</td>
<td>0.726</td>
<td>550</td>
</tr>
<tr>
<td>8</td>
<td>0.967</td>
<td>0.792</td>
<td>120</td>
</tr>
<tr>
<td rowspan="6">$\sigma_y, S_u, BHN, RA\%, E$</td>
<td>9</td>
<td>0.973</td>
<td>0.865</td>
<td>112</td>
</tr>
<tr>
<td>3</td>
<td>0.904</td>
<td>0.553</td>
<td>700</td>
</tr>
<tr>
<td>4</td>
<td>0.923</td>
<td>0.496</td>
<td>700</td>
</tr>
<tr>
<td>5</td>
<td>0.913</td>
<td>0.379</td>
<td>700</td>
</tr>
<tr>
<td>6</td>
<td>0.962</td>
<td>0.706</td>
<td>700</td>
</tr>
<tr>
<td>7</td>
<td>0.910</td>
<td>0.205</td>
<td>1000</td>
</tr>
</tbody>
</table>

Preliminary examinations were performed on different combinations of $\sigma_y, S_u, RA\%, BHN$ and $E$ as input data to the ANNs in order to determine the parameters affecting the $n'$ estimation. Finally, three combinations of tensile data were selected from among them as follows: ($\sigma_y$, $S_u$

![](./images/811681636105060352_3.jpg)

Fig. 3 Regression analysis of $n'$ for the train data: (a) ($\sigma_y$, $S_u$ and $BHN$) as the ANN input (b) ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) as the ANN input (c) ($\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$) as the ANN input.

![](./images/811681636105060352_4.jpg)

Fig. 4 Regression analysis of $n'$ for test data: (a) ($\sigma_y$, $S_u$ and $BHN$) as the ANN input (b) ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) as the ANN input (c) ($\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$) as the ANN input.

© 2011 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct 34, 534–544

and $B H N),(\sigma_{y}, S_{u}, R A \%$ and $B H N)$ and $(\sigma_{y}, S_{u}, R A \%$ , $B H N$ and $E$ ).

A number of neural network architectures with different number of neurons in the hidden layer (2-10 neurons) were also investigated to select the best one. A summary of the results is presented in Table 1. The results indicate that the best architecture involves seven neurons for the first combination $(\sigma_{y}, S_{u}$ and $B H N)$ , nine neurons for the second $(\sigma_{y}, S_{u}, R A \%$ and $B H N)$ and six neurons for the last $(\sigma_{y}, S_{u}, R A \%, B H N$ and $E)$ .

As mentioned earlier, the performance of the networks was evaluated by calculating MSE errors. In order to assess the validity of the networks and their accuracy, it is often useful to perform regression analysis between the net- work response and the corresponding target. Obviously, the closer these two data are, the better the performance of the network is. Figures 3 and 4 show the regression anal- yses for the three sets of input for the test and training data. The regression results of the training data illustrate that the networks were trained with a high accuracy of0.913 for the first set of input, 0.973 for the second set and 0.962 for the third set. Furthermore, comparison of the regression results of the test data indicates that the set of inputs $(\sigma_{y}, S_{u}, R A \%$ and $B H N)$ provided the best pre diction, $R=0.866$ , followed by the set $(\sigma_{y}, S_{u}$ and $B H N)$ . The difference in accuracy observed among the different input sets shows the importance of input parameters for predicting $n^{\prime}$ . It may be concluded that $\sigma_{y}, S_{u}, R A \%$ and BHN have relatively established effects on the prediction of $n^{\prime}$ while the effect of $E$ is not only immaterial, but also confusing.

In addition, the test data were used for a new prediction based on Eq. (2) to evaluate the ANN test results. Figure5 shows the results of this estimation. By comparing ANN and Eq. (2) results (Figs 4 and 5), it may be concluded that the ANN estimations were more accurate than those of Eq.(2). Therefore, such estimations seem desirable, es- pecially considering the time and effort that are required to obtain the fatigue properties used in the approxima- tions by Eq.(2) as compared with the monotonic tensile properties used in ANN predictions.

In addition, the performance accuracies of ANNs pre- dictions and those of Eq. (2) were investigated by an anal- ysis of the relative errors. Mean relative error (MRE) of ANNs and Eq. (2) predictions were calculated as follows

$$
M R E(\%)=\frac{1}{N} \sum_{i=1}^{N}\left|\frac{t_{i}-a_{i}}{t_{i}}\right| × 100,\qquad(6)
$$

where $N$ is the total number of test data, $t_{i}$ is the target(i.e. desired) value and $a_{i}$ is the network or Eq. (2) output value. The results of this analysis are provided in Fig. 6. Itis observed that the ANN with $(\sigma_{y}, S_{u}, R A \%$ and $B H N)$  as the input set yielded the minimum MRE.

![](./images/811681636105060352_5.jpg)

Fig. 5 Regression analysis of approximated $n^{\prime}$ based on Eq. (2) for the test data.

![](./images/811681636105060352_6.jpg)

Fig. 6 Comparison of MREs of the networks and the approximation method used for the $n^{\prime}$ prediction.

Finally, based on the regression and MRE analysis re- sults, it is safe to claim that the ANN with the input set $(\sigma_{y}$ , $S_{u}, R A \%$ and $B H N$ ) is a useful method for the prediction of cyclic strain-hardening exponent.

### Estimation of $K^{\prime}$ 
Prediction of $K^{\prime}$ by the ANN was investigated. For $K^{\prime}$  estimation, the properties of 48 steels reported in theliterature were used, which are provided in Table A1. $^{1,3,7}$ These data included $\sigma_{y}$ (228-2000 MPa), $S_{u}$ (345-2360MPa), BHN (80-536), RA% (14-80%), E (193-277 GPa) and $K^{\prime}$ (462-3538 MPa). Thus, analogous to the case of n', a broad range of steels were used for the modelling of

<table>
<caption>Table 2 Network details and architectures of $K'$</caption>
<thead>
<tr>
<th>Input sets</th>
<th>Neurons in the hidden layer</th>
<th>Regression for the training data</th>
<th>Regression for the test data</th>
<th>No. of iterations</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">$\sigma_y, S_u, BHN$</td>
<td>3</td>
<td>0.987</td>
<td>0.816</td>
<td>215</td>
</tr>
<tr>
<td>4</td>
<td>0.986</td>
<td>0.854</td>
<td>1000</td>
</tr>
<tr>
<td>5</td>
<td>0.994</td>
<td>0.872</td>
<td>168</td>
</tr>
<tr>
<td>6</td>
<td>0.998</td>
<td>0.901</td>
<td>320</td>
</tr>
<tr>
<td>7</td>
<td>0.995</td>
<td>0.896</td>
<td>200</td>
</tr>
<tr>
<td rowspan="5">$\sigma_y, S_u, BHN,$<br>$RA\%$</td>
<td>3</td>
<td>0.975</td>
<td>0.722</td>
<td>200</td>
</tr>
<tr>
<td>4</td>
<td>0.994</td>
<td>0.825</td>
<td>200</td>
</tr>
<tr>
<td>5</td>
<td>0.996</td>
<td>0.886</td>
<td>117</td>
</tr>
<tr>
<td>6</td>
<td>0.999</td>
<td>0.926</td>
<td>229</td>
</tr>
<tr>
<td>7</td>
<td>0.994</td>
<td>0.931</td>
<td>87</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td>0.996</td>
<td>0.953</td>
<td>100</td>
</tr>
<tr>
<td rowspan="5">$\sigma_y, S_u, BHN,$<br>$RA\%, E$</td>
<td>4</td>
<td>0.993</td>
<td>0.863</td>
<td>260</td>
</tr>
<tr>
<td>5</td>
<td>0.995</td>
<td>0.910</td>
<td>113</td>
</tr>
<tr>
<td>6</td>
<td>0.999</td>
<td>0.913</td>
<td>166</td>
</tr>
<tr>
<td>7</td>
<td>0.999</td>
<td>0.925</td>
<td>185</td>
</tr>
<tr>
<td>8</td>
<td>0.999</td>
<td>0.853</td>
<td>200</td>
</tr>
</tbody>
</table>

$K'$. Out of the whole range of data, 36 values were used for training the network and the others consisting of 12 data values were used for testing the trained network.

Three combinations of tensile data consisting of $\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$ were used to determine the parameters affecting the $K'$ estimation in the same manner as in the case of $n'$.

A number of neural network architectures with different number of neurons in the hidden layer (2–10 neurons) were also investigated to select the best one. The summary of the results are provided in Table 2. Clearly, the best architecture is associated with six neurons for the combination ($\sigma_y$, $S_u$ and $BHN$), eight neurons for ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) and seven neurons for ($\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$).

As mentioned previously, the performance of the networks was evaluated by calculating the MSE errors. In order to assess the validity of the networks and their accuracies, the regression analysis was performed between the network response and the corresponding target. Figures 7 and 8 indicate the regression analysis for the three sets of input for the test and training data. The regression result of the training data was 0.998 for the first input set, 0.996 for the second and 0.999 for the third. It may be seen from this figure that the value of $K'$ obtained from the trained network is in close agreement with its experimental value. Moreover, the regression results of the test data illustrate that amongst the input sets, the set ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) set of inputs yielded the best prediction, $R=0.953$, followed by the set ($\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$). Similar to the case of $n'$ estimation, it can be concluded that $\sigma_y$, $S_u$, $RA\%$ and $BHN$ have relatively established ef-

![](./images/811681636105060352_7.jpg)

Fig. 7 Regression analysis of $K'$ for the train data: (a) ($\sigma_y$, $S_u$ and $BHN$) as the ANN input (b) ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) as the ANN input (c) ($\sigma_y$, $S_u$, $RA\%$, $BHN$ and $E$) as the ANN input.

![](./images/811681636105060352_8.jpg)

Fig. 8 Regression analysis of $K'$ for the test data: (a) $(\sigma_y, S_u$ and $BHN)$ as the ANN input (b) $(\sigma_y, S_u, RA\%$ and $BHN)$ as the ANN input (c) $(\sigma_y, S_u, RA\%, BHN$ and $E)$ as the ANN input.

![](./images/811681636105060352_9.jpg)

Fig. 9 Regression analysis of approximated $K'$ based on Eq. (2) for the test data.

![](./images/811681636105060352_10.jpg)

Fig. 10 Comparison of MREs of the networks and approximation method used for the $K'$ prediction.

fects on the prediction of $K'$ while the effect of $E$ is not only immaterial, but also confusing.

In addition, the test data were used for a new prediction based on Eq. (2). A comparison of the results of this estimation and experimental values for $K'$ is depicted in Fig. 9. There is a poor agreement between the experimental values of $K'$ and the predictions obtained from Eq. (2). From Figs 7 and 9, it can be concluded that the ANN estimations are more accurate than those of Eq. (2). Therefore, the ANN method is preferred, especially by considering that it only requires monotonic tensile properties.

The results of MRE analysis of $K'$ are summarized in Fig. 10. As shown, the ANN with $(\sigma_y, S_u, RA\%$ and $BHN)$ as

<table>
<caption>Table 3 Calculated stress ranges</caption>
<thead>
<tr>
<th>Steel ID</th>
<th>$\Delta\sigma_{Actual}$ (MPa)</th>
<th>$\Delta\sigma_{ANN\ based}$ (MPa)</th>
<th>$\Delta\sigma_{Eq.\ 2based}$ (MPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>S45C</td>
<td>978.8</td>
<td>905.6</td>
<td>1103.8</td>
</tr>
<tr>
<td>1045</td>
<td>974.5</td>
<td>1074.6</td>
<td>1078.6</td>
</tr>
<tr>
<td>RQC-100</td>
<td>1007.2</td>
<td>943.7</td>
<td>1414.8</td>
</tr>
<tr>
<td>SAE</td>
<td>975.5</td>
<td>915.9</td>
<td>642.5</td>
</tr>
<tr>
<td>105(M)D1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$MRE\ (\%)$</td>
<td>7.5</td>
<td>24.5</td>
</tr>
</tbody>
</table>

the input set has the minimum MRE. Finally, similar to the case of $n'$, based on the results from the regression and MRE analysis, it is safe to claim that the ANN with the input set ($\sigma_y$, $S_u$, $RA\%$ and $BHN$) is a useful method for the prediction of cyclic strength coefficient.

## ILLUSTRATIVE EXAMPLE

The purpose of this section is to illustrate the role of $n'$ and $K'$ errors on stress calculation. Consider the problem of calculating the stress range for a given strain range, $\Delta\varepsilon=0.012$, by using Eq. (1). Four steels consisting of S45C, 1045, RQC-100 and SAE 105(M)D1 were selected randomly for this calculation. ANN and Eq. (2) were used initially to determine $n'$ and $K'$. Then, $n'$ and $K'$ were used for the calculation of the stress range and MRE (%). The results are summarized in Table 3. It can be seen that the value $7.5\%$ for the MRE (%) of $\Delta\sigma_{ANNbased}$ is less than that of $24.5\%$ for $\Delta\sigma_{Eq.\ 2based}$.

## CONCLUSION

ANN was applied to develop a model for predicting cyclic strain-hardening exponent and cyclic strength coefficient of steels on the basis of monotonic tensile test properties. A number of neural networks with different number of input neurons were trained and amongst the input sets, the four-parameter input set, namely ($\sigma_y$, $S_u$, $RA\%$ and $BHN$), was found to yield the best predictions. Cyclic strain-hardening exponent and cyclic strength coefficient of steels, characterizing the stable curves of true stress amplitude versus true plastic strain amplitude, were predicted by ANN with high levels of accuracy, 0.865 and 0.953 respectively, while the accuracy of estimations based on approximate relations [Eq. (2)] were 0.693 and 0.726, in that order.

The MREs of the predictions by the ANN and approximate relations [Eq. (2)] were calculated. Using ANN, the value for the MRE (%) of Eq. (2) estimations decreased from 27.43 to $18.53\%$ for $n'$, and from 20.56 to $11.43\%$ for $K'$. Finally, stress ranges for four steels were calculated for a given strain range based on Eq. (2) and ANN. It was observed that the MRE (%) of calculated stress ranges decreased from 24.5 to $7.5\%$.

As input to the network, this approximation simply uses the monotonic tensile properties for the $n'$ and $K'$ approximation. These data are commonly available in the pertinent literature, or easily measurable.

It was concluded that the stable cyclic true stress-strain curve properties predicted by the trained neural network were more accurate compared with those by the approximate relations based on the low-cycle fatigue properties.

## REFERENCES

1 SAE Standards (2002) Technical report on low cycle fatigue properties: ferrous and nonferrous materials. Report Number: J1099, SAE, Warren dale, PA.

2 Stephens, R. I., Fatemi, A., Stephens, R. R. and Fuchs, H. O. (2001) *Metal Fatigue in Engineering*. John Wiley & Sons, Canada.

3 Kim, K. S., Chen, X., Han, C. and Lee, H. W. (2001) Estimation methods for fatigue properties of steels under axial and torsional loading. *Int. J. Fatigue* **24**, 783–793.

4 Manson, S. S. (1965) A complex subject– some simple approximations. *Exp. Mech.* **5**, 193–226.

5 Ong, J. (1993) An improved technique for the prediction of axial fatigue life from tensile data. *Int. J. Fatigue* **15**, 213–219.

6 Baumel, J. A. and Seeger, T. (1987) *Materials Data for Cyclic Loading*. Elsevier, New York.

7 Roessle, M. L. and Fatemi, A. (2000) Strain-controlled fatigue properties of steels and some simple approximations. *Int. J. Fatigue* **22**, 495–511.

8 Malinov, S., Sha, W. and McKeown, J. J. (2001) Modeling the correlation between processing parameters and properties in titanium alloys using artificial neural network. *Comp. Mater. Sci.* **21**, 375–394.

9 Venkatessh, V. and Rack, H. J. (1999) A neural network approach to elevated temperature creep-fatigue life prediction. *Int. J. Fatigue* **21**, 225–234.

10 Bucar, T., Nagode, M. and Fajdiga, M. (2006) A neural network approach to describing the scatter of S–N curves. *Int. J. Fatigue* **28**, 311–323.

11 Srinivasan, V. S., Valsan, M., Roa, K. B. S., Mannan, S. L. and Raj, B. (2003) Low cycle fatigue and creep-fatigue interaction behavior of 316L(N) stainless steel and life prediction by artificial neural network approach. *Int. J. Fatigue* **28**, 1327–1338.

12 Mathew, M. D., Kim, D. W. and Ryu, W. S. (2007) A neural network model to predict low cycle fatigue life of nitrogen-alloyed 316L stainless steel. *Mater. Sci. Eng.* **474**, 247–253.

13 Genel, K. (2004) Application of artificial neural network for predicting strain-life fatigue properties of steels on the basis of tensile data. *Int. J. Fatigue* **26**, 1027–1035.

14 Sinan Koksal, N. (2009) Prediction of mechanical properties in magnesia based refractory materials using ANN. *Comp. Mater. Sci.* **47**, 86–92.

© 2011 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct **34**, 534–544

15 Dini, G., Najafizadeh, A., Monir-Vaghefi, S. M. and Ebnonnasir, A. (2009) Predicting of mechanical properties of Fe-Mn-(Al, Si) TRIP/TWIP steels using neural network modeling. *Comp. Mater. Sci.* **45**, 959-965.

16 Monajati, H., Asefi, D., Parsapour, A. and Abbasi, Sh. (2010) Analysis of the effects of processing parameters on mechanical properties and formability of cold rolled low carbon steel sheets using neural networks. *Comput. Mater. Sci.* **49**, 876-881.

17 Rumelhart, D. E. and McClelland, J. L. (1986) *Parallel Distributed Processing*. MIT Press, Cambridge, MA.

18 Arslan, A. and Ince, R. (1996) Neural network-based design of edge supported reinforced concrete slabs. *Struct. Eng. Rev.* **8**, 329-335.

19 Hagan, M. T., Demuth, H. B. and Beale, M. (1995) *Neural Network Design*. PWS Publishing Company, Boston, USA.

20 Charpentier, E. and Laurin, J.,(1997). Sectorial direction finding antenna array with a MLP beam former. In: *Proceedings of the IEEE International Symposium on Antennas and Propagation*, Montreal, Canada, Vol. 4, 2270-2273.

21 Demuth, H. and Beale, M. (2005) *Neural Network Toolbox*. USA.

## APPENDIX

See Table A1.

Table A1 Data for the properties of steels used in this study

<table>
  <thead>
    <tr>
      <th>Steel (ID)</th>
      <th>BHN<br>(kgf/mm²)</th>
      <th>$S_u$<br>(MPa)</th>
      <th>$\sigma_y$<br>(MPa)</th>
      <th>$RA$ (%)</th>
      <th>$E$ (GPa)</th>
      <th>$K'$<br>(MPa)</th>
      <th>$n'$</th>
      <th>$\sigma'_f$<br>(MPa)</th>
      <th>$\varepsilon'_f$</th>
      <th>$b$</th>
      <th>$c$</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1005-1009</td>
      <td>90</td>
      <td>345</td>
      <td>262</td>
      <td>80</td>
      <td>200</td>
      <td>462</td>
      <td>0.12</td>
      <td>641</td>
      <td>0.1</td>
      <td>−0.109</td>
      <td>−0.39</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1005-1009</td>
      <td>125</td>
      <td>414</td>
      <td>400</td>
      <td>64</td>
      <td>200</td>
      <td>490</td>
      <td>0.11</td>
      <td>538</td>
      <td>0.11</td>
      <td>−0.073</td>
      <td>−0.41</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1005-1009</td>
      <td>90</td>
      <td>359</td>
      <td>269</td>
      <td>73</td>
      <td>207</td>
      <td>490</td>
      <td>0.12</td>
      <td>579</td>
      <td>0.15</td>
      <td>−0.09</td>
      <td>−0.43</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1005-1009</td>
      <td>125</td>
      <td>469</td>
      <td>448</td>
      <td>66</td>
      <td>207</td>
      <td>572</td>
      <td>0.11</td>
      <td>517</td>
      <td>0.3</td>
      <td>−0.059</td>
      <td>−0.51</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>108</td>
      <td>441</td>
      <td>262</td>
      <td>62</td>
      <td>203</td>
      <td>772</td>
      <td>0.18</td>
      <td>896</td>
      <td>0.41</td>
      <td>−0.12</td>
      <td>−0.51</td>
      <td>1</td>
    </tr>
    <tr>
      <td>950X</td>
      <td>150</td>
      <td>441</td>
      <td>345</td>
      <td>65</td>
      <td>207</td>
      <td>793</td>
      <td>0.134</td>
      <td>627</td>
      <td>0.35</td>
      <td>−0.075</td>
      <td>−0.54</td>
      <td>1</td>
    </tr>
    <tr>
      <td>950X</td>
      <td>156</td>
      <td>531</td>
      <td>331</td>
      <td>72</td>
      <td>203</td>
      <td>924</td>
      <td>0.114</td>
      <td>1007</td>
      <td>0.85</td>
      <td>−0.1</td>
      <td>−0.61</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1015</td>
      <td>80</td>
      <td>414</td>
      <td>228</td>
      <td>68</td>
      <td>207</td>
      <td>945</td>
      <td>0.22</td>
      <td>827</td>
      <td>0.95</td>
      <td>−0.11</td>
      <td>−0.64</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1541 (C2)</td>
      <td>195</td>
      <td>906</td>
      <td>475</td>
      <td>42</td>
      <td>205</td>
      <td>950</td>
      <td>0.114</td>
      <td>1044</td>
      <td>0.513</td>
      <td>−0.083</td>
      <td>−0.557</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SNCM439</td>
      <td>323</td>
      <td>1050</td>
      <td>950</td>
      <td>37</td>
      <td>208</td>
      <td>1000</td>
      <td>0.066</td>
      <td>1380</td>
      <td>1.89</td>
      <td>−0.0722</td>
      <td>−0.801</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SCM440</td>
      <td>319</td>
      <td>1000</td>
      <td>846</td>
      <td>36</td>
      <td>204</td>
      <td>1040</td>
      <td>0.094</td>
      <td>1400</td>
      <td>0.675</td>
      <td>−0.0879</td>
      <td>−0.65</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SNCM630</td>
      <td>327</td>
      <td>1100</td>
      <td>951</td>
      <td>49</td>
      <td>196</td>
      <td>1060</td>
      <td>0.054</td>
      <td>1270</td>
      <td>1.54</td>
      <td>−0.0732</td>
      <td>−0.823</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SCM435</td>
      <td>300</td>
      <td>951</td>
      <td>795</td>
      <td>66</td>
      <td>210</td>
      <td>1070</td>
      <td>0.089</td>
      <td>1100</td>
      <td>0.996</td>
      <td>−0.067</td>
      <td>−0.708</td>
      <td>3</td>
    </tr>
    <tr>
      <td>S25C</td>
      <td>153</td>
      <td>508</td>
      <td>280</td>
      <td>52</td>
      <td>209</td>
      <td>1140</td>
      <td>0.21</td>
      <td>821</td>
      <td>0.216</td>
      <td>−0.0961</td>
      <td>−0.458</td>
      <td>3</td>
    </tr>
    <tr>
      <td>S45C</td>
      <td>234</td>
      <td>798</td>
      <td>590</td>
      <td>39</td>
      <td>206</td>
      <td>1150</td>
      <td>0.152</td>
      <td>1400</td>
      <td>0.449</td>
      <td>−0.107</td>
      <td>−0.564</td>
      <td>3</td>
    </tr>
    <tr>
      <td>980X</td>
      <td>225</td>
      <td>696</td>
      <td>565</td>
      <td>68</td>
      <td>194</td>
      <td>1248</td>
      <td>0.134</td>
      <td>1055</td>
      <td>0.21</td>
      <td>−0.08</td>
      <td>−0.53</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1141 (A4)</td>
      <td>241</td>
      <td>802</td>
      <td>602</td>
      <td>54</td>
      <td>217</td>
      <td>1254</td>
      <td>0.154</td>
      <td>1080</td>
      <td>0.361</td>
      <td>−0.079</td>
      <td>−0.508</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1141 (A6)</td>
      <td>252</td>
      <td>797</td>
      <td>610</td>
      <td>58</td>
      <td>215</td>
      <td>1270</td>
      <td>0.154</td>
      <td>1162</td>
      <td>0.534</td>
      <td>−0.086</td>
      <td>−0.555</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1141 (A2)</td>
      <td>277</td>
      <td>925</td>
      <td>814</td>
      <td>59</td>
      <td>277</td>
      <td>1277</td>
      <td>0.124</td>
      <td>1127</td>
      <td>0.309</td>
      <td>−0.066</td>
      <td>−0.514</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1050 (D2)</td>
      <td>220</td>
      <td>829</td>
      <td>460</td>
      <td>34</td>
      <td>203</td>
      <td>1292</td>
      <td>0.146</td>
      <td>1094</td>
      <td>0.309</td>
      <td>−0.075</td>
      <td>−0.502</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SFNCM85S</td>
      <td>241</td>
      <td>825</td>
      <td>565</td>
      <td>66</td>
      <td>201</td>
      <td>1320</td>
      <td>0.18</td>
      <td>1040</td>
      <td>0.316</td>
      <td>−0.0924</td>
      <td>−0.522</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SAE 1038 (B3)</td>
      <td>195</td>
      <td>649</td>
      <td>410</td>
      <td>67</td>
      <td>219</td>
      <td>1330</td>
      <td>0.208</td>
      <td>1009</td>
      <td>0.225</td>
      <td>−0.097</td>
      <td>−0.46</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1038 (B1)</td>
      <td>163</td>
      <td>582</td>
      <td>331</td>
      <td>54</td>
      <td>201</td>
      <td>1340</td>
      <td>0.22</td>
      <td>1043</td>
      <td>0.309</td>
      <td>−0.107</td>
      <td>−0.481</td>
      <td>7</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>225</td>
      <td>724</td>
      <td>634</td>
      <td>65</td>
      <td>200</td>
      <td>1344</td>
      <td>0.18</td>
      <td>1227</td>
      <td>1</td>
      <td>−0.095</td>
      <td>−0.66</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SF60</td>
      <td>167</td>
      <td>820</td>
      <td>580</td>
      <td>53</td>
      <td>208</td>
      <td>1350</td>
      <td>0.186</td>
      <td>978</td>
      <td>0.187</td>
      <td>−0.082</td>
      <td>−0.439</td>
      <td>3</td>
    </tr>
    <tr>
      <td>9262</td>
      <td>280</td>
      <td>1000</td>
      <td>786</td>
      <td>33</td>
      <td>193</td>
      <td>1358</td>
      <td>0.12</td>
      <td>1220</td>
      <td>0.41</td>
      <td>−0.073</td>
      <td>−0.6</td>
      <td>1</td>
    </tr>
    <tr>
      <td>9262</td>
      <td>260</td>
      <td>924</td>
      <td>455</td>
      <td>14</td>
      <td>207</td>
      <td>1379</td>
      <td>0.15</td>
      <td>1041</td>
      <td>0.16</td>
      <td>−0.071</td>
      <td>−0.47</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1541 (C1)</td>
      <td>180</td>
      <td>783</td>
      <td>475</td>
      <td>55</td>
      <td>205</td>
      <td>1416</td>
      <td>0.194</td>
      <td>1622</td>
      <td>0.515</td>
      <td>−0.135</td>
      <td>−0.548</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1038 (B2)</td>
      <td>185</td>
      <td>652</td>
      <td>359</td>
      <td>53</td>
      <td>219</td>
      <td>1420</td>
      <td>0.222</td>
      <td>1004</td>
      <td>0.202</td>
      <td>−0.098</td>
      <td>−0.44</td>
      <td>7</td>
    </tr>
    <tr>
      <td>RQC-100</td>
      <td>290</td>
      <td>931</td>
      <td>883</td>
      <td>67</td>
      <td>207</td>
      <td>1434</td>
      <td>0.14</td>
      <td>1241</td>
      <td>0.66</td>
      <td>−0.07</td>
      <td>−0.69</td>
      <td>1</td>
    </tr>
    <tr>
      <td>RQC-100</td>
      <td>290</td>
      <td>938</td>
      <td>896</td>
      <td>43</td>
      <td>207</td>
      <td>1434</td>
      <td>0.14</td>
      <td>1241</td>
      <td>0.66</td>
      <td>−0.07</td>
      <td>−0.69</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1141 (A7)</td>
      <td>229</td>
      <td>789</td>
      <td>493</td>
      <td>47</td>
      <td>220</td>
      <td>1441</td>
      <td>0.177</td>
      <td>1326</td>
      <td>0.602</td>
      <td>−0.103</td>
      <td>−0.581</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1141 (A3)</td>
      <td>199</td>
      <td>695</td>
      <td>418</td>
      <td>53</td>
      <td>220</td>
      <td>1448</td>
      <td>0.205</td>
      <td>1117</td>
      <td>0.264</td>
      <td>−0.096</td>
      <td>−0.462</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1141 (A5)</td>
      <td>217</td>
      <td>725</td>
      <td>450</td>
      <td>49</td>
      <td>214</td>
      <td>1467</td>
      <td>0.191</td>
      <td>1255</td>
      <td>0.43</td>
      <td>−0.102</td>
      <td>−0.529</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1141 (A1)</td>
      <td>223</td>
      <td>771</td>
      <td>457</td>
      <td>57</td>
      <td>216</td>
      <td>1515</td>
      <td>0.205</td>
      <td>1168</td>
      <td>0.257</td>
      <td>−0.097</td>
      <td>−0.464</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1090 (E1)</td>
      <td>259</td>
      <td>1090</td>
      <td>735</td>
      <td>14</td>
      <td>203</td>
      <td>1611</td>
      <td>0.174</td>
      <td>1310</td>
      <td>0.25</td>
      <td>−0.091</td>
      <td>−0.496</td>
      <td>7</td>
    </tr>
  </tbody>
</table>

(Continued)

© 2011 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct **34**, 534-544

Table A1 (Continued)

<table>
  <thead>
    <tr>
      <th>Steel (ID)</th>
      <th>BHN<br>(kgf/mm²)</th>
      <th>Su<br>(MPa)</th>
      <th>σy<br>(MPa)</th>
      <th>RA (%)</th>
      <th>E (GPa)</th>
      <th>K'<br>(MPa)</th>
      <th>n'</th>
      <th>σ¹f<br>(MPa)</th>
      <th>ε¹f</th>
      <th>b</th>
      <th>c</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1541F</td>
      <td>260</td>
      <td>889</td>
      <td>786</td>
      <td>60</td>
      <td>206</td>
      <td>1620</td>
      <td>0.16</td>
      <td>1276</td>
      <td>0.93</td>
      <td>−0.071</td>
      <td>−0.65</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1090 (E5)</td>
      <td>272</td>
      <td>1124</td>
      <td>765</td>
      <td>38</td>
      <td>203</td>
      <td>1653</td>
      <td>0.159</td>
      <td>1547</td>
      <td>1.57</td>
      <td>−0.093</td>
      <td>−0.683</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1090 (E2)</td>
      <td>357</td>
      <td>1388</td>
      <td>950</td>
      <td>25</td>
      <td>203</td>
      <td>1663</td>
      <td>0.133</td>
      <td>1954</td>
      <td>2.58</td>
      <td>−0.106</td>
      <td>−0.777</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1050 (D1)</td>
      <td>205</td>
      <td>821</td>
      <td>465</td>
      <td>50</td>
      <td>211</td>
      <td>1673</td>
      <td>0.22</td>
      <td>989</td>
      <td>0.433</td>
      <td>−0.126</td>
      <td>−0.512</td>
      <td>7</td>
    </tr>
    <tr>
      <td>1541F</td>
      <td>290</td>
      <td>951</td>
      <td>889</td>
      <td>49</td>
      <td>206</td>
      <td>1758</td>
      <td>0.17</td>
      <td>1276</td>
      <td>0.68</td>
      <td>−0.076</td>
      <td>−0.65</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1090 (E4)</td>
      <td>279</td>
      <td>1251</td>
      <td>760</td>
      <td>14</td>
      <td>203</td>
      <td>1835</td>
      <td>0.168</td>
      <td>1928</td>
      <td>0.734</td>
      <td>−0.12</td>
      <td>−0.642</td>
      <td>7</td>
    </tr>
    <tr>
      <td>SAE 1090 (E3)</td>
      <td>309</td>
      <td>1147</td>
      <td>650</td>
      <td>22</td>
      <td>217</td>
      <td>1873</td>
      <td>0.176</td>
      <td>1878</td>
      <td>0.7</td>
      <td>−0.12</td>
      <td>−0.6</td>
      <td>7</td>
    </tr>
    <tr>
      <td>9262</td>
      <td>410</td>
      <td>1565</td>
      <td>1379</td>
      <td>32</td>
      <td>200</td>
      <td>2013</td>
      <td>0.089</td>
      <td>1855</td>
      <td>0.38</td>
      <td>−0.057</td>
      <td>−0.65</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10B62</td>
      <td>430</td>
      <td>1641</td>
      <td>1510</td>
      <td>38</td>
      <td>193</td>
      <td>2130</td>
      <td>0.16</td>
      <td>1779</td>
      <td>0.32</td>
      <td>−0.067</td>
      <td>−0.56</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>410</td>
      <td>1448</td>
      <td>1365</td>
      <td>51</td>
      <td>200</td>
      <td>2310</td>
      <td>0.146</td>
      <td>1862</td>
      <td>0.6</td>
      <td>−0.073</td>
      <td>−0.7</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5160</td>
      <td>430</td>
      <td>1669</td>
      <td>1531</td>
      <td>42</td>
      <td>193</td>
      <td>2310</td>
      <td>0.15</td>
      <td>1931</td>
      <td>0.4</td>
      <td>−0.071</td>
      <td>−0.57</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SAE 1050 (D3)</td>
      <td>536</td>
      <td>2360</td>
      <td>2000</td>
      <td>15</td>
      <td>203</td>
      <td>3538</td>
      <td>0.109</td>
      <td>3492</td>
      <td>1.87</td>
      <td>−0.109</td>
      <td>−1.04</td>
      <td>7</td>
    </tr>
    <tr>
      <td>1040</td>
      <td>225</td>
      <td>621</td>
      <td>345</td>
      <td>60</td>
      <td>200</td>
      <td></td>
      <td>0.18</td>
      <td>1538</td>
      <td>0.61</td>
      <td>−0.14</td>
      <td>−0.57</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>500</td>
      <td>1827</td>
      <td>1689</td>
      <td>51</td>
      <td>207</td>
      <td></td>
      <td>0.12</td>
      <td>2275</td>
      <td>0.25</td>
      <td>−0.08</td>
      <td>−0.68</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>595</td>
      <td>2241</td>
      <td>1862</td>
      <td>41</td>
      <td>207</td>
      <td></td>
      <td>0.13</td>
      <td>2723</td>
      <td>0.07</td>
      <td>−0.081</td>
      <td>−0.6</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>450</td>
      <td>1586</td>
      <td>1517</td>
      <td>55</td>
      <td>207</td>
      <td></td>
      <td>0.15</td>
      <td>1793</td>
      <td>0.35</td>
      <td>−0.07</td>
      <td>−0.69</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>390</td>
      <td>1344</td>
      <td>1276</td>
      <td>59</td>
      <td>207</td>
      <td></td>
      <td>0.17</td>
      <td>1586</td>
      <td>0.45</td>
      <td>−0.074</td>
      <td>−0.68</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1144</td>
      <td>265</td>
      <td>931</td>
      <td>717</td>
      <td>33</td>
      <td>197</td>
      <td></td>
      <td>0.15</td>
      <td>1000</td>
      <td>0.32</td>
      <td>−0.08</td>
      <td>−0.58</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1144</td>
      <td>305</td>
      <td>1034</td>
      <td>1020</td>
      <td>25</td>
      <td>199</td>
      <td></td>
      <td>0.18</td>
      <td>1586</td>
      <td>0.27</td>
      <td>−0.09</td>
      <td>−0.53</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4130</td>
      <td>365</td>
      <td>1427</td>
      <td>1358</td>
      <td>55</td>
      <td>200</td>
      <td></td>
      <td>0.12</td>
      <td>1696</td>
      <td>0.89</td>
      <td>−0.081</td>
      <td>−0.69</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4130</td>
      <td>258</td>
      <td>896</td>
      <td>779</td>
      <td>67</td>
      <td>221</td>
      <td></td>
      <td>0.13</td>
      <td>1276</td>
      <td>0.92</td>
      <td>−0.083</td>
      <td>−0.63</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4140</td>
      <td>310</td>
      <td>1076</td>
      <td>965</td>
      <td>60</td>
      <td>201</td>
      <td></td>
      <td>0.14</td>
      <td>1827</td>
      <td>1.2</td>
      <td>−0.08</td>
      <td>−0.59</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>670</td>
      <td>2448</td>
      <td>1620</td>
      <td>6</td>
      <td>200</td>
      <td></td>
      <td>0.05</td>
      <td>2586</td>
      <td></td>
      <td>−0.075</td>
      <td></td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>560</td>
      <td>2241</td>
      <td>1689</td>
      <td>27</td>
      <td>207</td>
      <td></td>
      <td>0.12</td>
      <td>2654</td>
      <td>0.07</td>
      <td>−0.089</td>
      <td>−0.76</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>475</td>
      <td>1931</td>
      <td>1724</td>
      <td>35</td>
      <td>207</td>
      <td></td>
      <td>0.13</td>
      <td>2172</td>
      <td>0.09</td>
      <td>−0.081</td>
      <td>−0.61</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>335</td>
      <td>1248</td>
      <td>1234</td>
      <td>28</td>
      <td>199</td>
      <td></td>
      <td>0.14</td>
      <td>1248</td>
      <td>0.06</td>
      <td>−0.08</td>
      <td>−0.62</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>475</td>
      <td>2034</td>
      <td>1896</td>
      <td>20</td>
      <td>200</td>
      <td></td>
      <td>0.15</td>
      <td>2068</td>
      <td>0.2</td>
      <td>−0.082</td>
      <td>−0.77</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>400</td>
      <td>1551</td>
      <td>1448</td>
      <td>47</td>
      <td>200</td>
      <td></td>
      <td>0.16</td>
      <td>1896</td>
      <td>0.5</td>
      <td>−0.09</td>
      <td>−0.75</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>450</td>
      <td>1931</td>
      <td>1862</td>
      <td>37</td>
      <td>200</td>
      <td></td>
      <td>0.16</td>
      <td>2103</td>
      <td>0.6</td>
      <td>−0.09</td>
      <td>−0.76</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>380</td>
      <td>1413</td>
      <td>1379</td>
      <td>48</td>
      <td>207</td>
      <td></td>
      <td>0.17</td>
      <td>1827</td>
      <td>0.45</td>
      <td>−0.08</td>
      <td>−0.75</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>310</td>
      <td>1062</td>
      <td>1048</td>
      <td>29</td>
      <td>200</td>
      <td></td>
      <td>0.18</td>
      <td>1448</td>
      <td>0.22</td>
      <td>−0.1</td>
      <td>−0.51</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4142</td>
      <td>450</td>
      <td>1758</td>
      <td>1586</td>
      <td>42</td>
      <td>207</td>
      <td></td>
      <td>0.15</td>
      <td>1999</td>
      <td>0.4</td>
      <td>−0.08</td>
      <td>−0.73</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4340</td>
      <td>350</td>
      <td>1241</td>
      <td>1172</td>
      <td>57</td>
      <td>193</td>
      <td></td>
      <td>0.14</td>
      <td>1655</td>
      <td>0.73</td>
      <td>−0.076</td>
      <td>−0.62</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4340</td>
      <td>409</td>
      <td>1469</td>
      <td>1372</td>
      <td>38</td>
      <td>200</td>
      <td></td>
      <td>0.15</td>
      <td>1999</td>
      <td>0.48</td>
      <td>−0.091</td>
      <td>−0.6</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4340</td>
      <td>243</td>
      <td>827</td>
      <td>634</td>
      <td>43</td>
      <td>193</td>
      <td></td>
      <td>0.18</td>
      <td>1200</td>
      <td>0.45</td>
      <td>−0.095</td>
      <td>−0.54</td>
      <td>1</td>
    </tr>
    <tr>
      <td>30304</td>
      <td>327</td>
      <td>951</td>
      <td>745</td>
      <td>69</td>
      <td>172</td>
      <td></td>
      <td>0.17</td>
      <td>2275</td>
      <td>0.89</td>
      <td>−0.12</td>
      <td>−0.77</td>
      <td>1</td>
    </tr>
    <tr>
      <td>30304</td>
      <td>160</td>
      <td>745</td>
      <td>255</td>
      <td>74</td>
      <td>186</td>
      <td></td>
      <td>0.36</td>
      <td>2413</td>
      <td>1.02</td>
      <td>−0.15</td>
      <td>−0.69</td>
      <td>1</td>
    </tr>
    <tr>
      <td>30310</td>
      <td>145</td>
      <td>641</td>
      <td>221</td>
      <td>64</td>
      <td>193</td>
      <td></td>
      <td>0.26</td>
      <td>1655</td>
      <td>0.6</td>
      <td>−0.15</td>
      <td>−0.57</td>
      <td>1</td>
    </tr>
    <tr>
      <td>52100</td>
      <td>518</td>
      <td>2013</td>
      <td>1924</td>
      <td>11</td>
      <td>207</td>
      <td></td>
      <td>0.16</td>
      <td>2586</td>
      <td>0.18</td>
      <td>−0.09</td>
      <td>−0.56</td>
      <td>1</td>
    </tr>
    <tr>
      <td>A-538-A</td>
      <td>405</td>
      <td>1517</td>
      <td>1482</td>
      <td>67</td>
      <td>186</td>
      <td></td>
      <td>0.09</td>
      <td>1655</td>
      <td>0.3</td>
      <td>−0.065</td>
      <td>−0.62</td>
      <td>1</td>
    </tr>
    <tr>
      <td>950C</td>
      <td>159</td>
      <td>565</td>
      <td>317</td>
      <td>64</td>
      <td>204</td>
      <td></td>
      <td>0.15</td>
      <td>1172</td>
      <td>0.95</td>
      <td>−0.12</td>
      <td>−0.61</td>
      <td>1</td>
    </tr>
    <tr>
      <td>950C</td>
      <td>150</td>
      <td>565</td>
      <td>324</td>
      <td>69</td>
      <td>207</td>
      <td></td>
      <td>0.185</td>
      <td>972</td>
      <td>0.85</td>
      <td>−0.11</td>
      <td>−0.59</td>
      <td>1</td>
    </tr>
    <tr>
      <td>A-538-B</td>
      <td>460</td>
      <td>1862</td>
      <td>1793</td>
      <td>56</td>
      <td>186</td>
      <td></td>
      <td>0.075</td>
      <td>2137</td>
      <td>0.8</td>
      <td>−0.071</td>
      <td>−0.71</td>
      <td>1</td>
    </tr>
    <tr>
      <td>A-538-C</td>
      <td>480</td>
      <td>1999</td>
      <td>1931</td>
      <td>55</td>
      <td>179</td>
      <td></td>
      <td>0.08</td>
      <td>2241</td>
      <td>0.6</td>
      <td>−0.07</td>
      <td>−0.75</td>
      <td>1</td>
    </tr>
    <tr>
      <td>AM-350</td>
      <td>496</td>
      <td>1903</td>
      <td>1862</td>
      <td>20</td>
      <td>179</td>
      <td></td>
      <td>0.21</td>
      <td>2689</td>
      <td>0.1</td>
      <td>−0.102</td>
      <td>−0.42</td>
      <td>1</td>
    </tr>
    <tr>
      <td>H-11</td>
      <td>660</td>
      <td>2586</td>
      <td>2034</td>
      <td>33</td>
      <td>207</td>
      <td></td>
      <td>0.07</td>
      <td>3172</td>
      <td>0.08</td>
      <td>−0.077</td>
      <td>−0.74</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

© 2011 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct 34, 534–544