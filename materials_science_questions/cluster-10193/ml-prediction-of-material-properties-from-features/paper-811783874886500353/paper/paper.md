ORIGINAL ARTICLE

# Artificial neural network methods for the prediction of framework crystal structures of zeolites from XRD data

Melkon Tatlier

Received: 15 October 2009 / Accepted: 20 May 2010 / Published online: 4 June 2010
© Springer-Verlag London Limited 2010

**Abstract** Extracting information about the structures of zeolites and other crystalline materials from X-ray dif- fraction (XRD) data simply by using statistical methods may provide an impetus for the discovery and identification of unknown materials. In this study, the possibility of using artificial neural network methods for relating framework crystal structures to XRD data reported in literature was investigated. Generalized Regression Neural Networks and Radial Basis Function-Based Neural Networks were uti- lized in the investigations. The results obtained by neural networks, using fivefold cross validation technique, were compared to the actual values as well as to those deter- mined by multilinear regression. The predictions made by these neural network methods were, in general, more reli- able than those performed by regression. The best predic- tions were achieved for the estimation of the framework densities of zeolites, which provided quite small deviations from the actual values.

**Keywords** Neural network · Zeolite · X-ray diffraction · Crystallography

## 1 Introduction

Zeolites are hydrated microporous crystalline aluminosili- cates that may be used in diverse applications related to ion exchange, catalysis, adsorption and separation [1–4]. Zeolites have developed into a large industry due to their unique and versatile properties. They may be utilized in the separation of linear and branched hydrocarbons, for cata- lytic cracking and hydrocracking or as detergent builders, to name a few, while a significant number of potential applications are waiting to emerge. Zeolites may occur naturally or be synthesized in laboratory conditions. The most significant parameters determining the type of the zeolite formed from a certain initial reaction mixture composition are the synthesis time and temperature as well as the molar ratios of the reactants. Suitable reagents that form a clear solution or a gel mixture should be used to obtain different types of zeolites. After carrying out the synthesis procedure with these reagents, the solid material formed in the solution should be separated by filtration, which is then characterized by using various techniques. X-ray diffraction (XRD) is one of the basic and essential techniques to characterize the solid material thus obtained. XRD may be used to determine the crystallographic structure, grain size and orientation of the crystals. It is commonly utilized to identify unknown substances by comparing diffraction data against a database. The relative abundance of crystalline materials in solid mixtures may also be determined by this technique. When coupled with lattice refinement techniques, it can provide structural information on unknown materials. However, the achievement of this deed is not a simple task to perform. Zeolite crystallographers have developed a number of approaches to determine framework structures. The tech- niques include informed model building, computer approaches to model generation, application of direct methods to powder data, microcrystalline diffraction and exploitation of magic angle spinning NMR and electron microscopy [5]. Usually a number of methods are com- bined to construct a framework structure model and once a reasonable model has been produced, Rietveld refinement

M. Tatlier (⊗)
Department of Chemical Engineering,
Istanbul Technical University, Maslak, 34469 Istanbul, Turkey
e-mail: tatlierm@itu.edu.tr

![](./images/811783874886500353_1.jpg)

will confirm or reject the framework proposal, also revealing further details of the structure.

Artificial neural networks (ANNs) have the ability to learn from input data and are very useful for the prediction of complex high-dimensional data. ANN methods have a broad range of applications, including research in chemical engineering. Artificial neural networks have been successfully used for dynamic modeling and control of chemical processes and fault diagnosis [6], in the catalytic modeling and design of solid catalysts [7] and for modeling the kinetics of a chemical reaction [8]. The applicability of ANN methods in emulsion liquid membranes [9] and in the prediction/estimation of the vapor-liquid equilibrium data [10] has also been investigated. It was recently shown that ANN methods could learn efficiently from available zeolite synthesis data for the Na aluminosilicate system, in the literature [11]. The type of zeolite obtained from different reaction mixtures was related to the initial compositions of the reaction mixtures by using the Generalized Regression Neural Networks (GRNN), Radial Basis Function-Based Neural Networks (RBF) and Feed Forward Back Propagation (FFBP) methods [11]. The deviations of the estimates made by using artificial neural network methods from experimental results were quite smaller than those obtained by multilinear and nonlinear regression. The best predictions of the Si molar contents (per mole of Al) of the zeolites that would be obtained from a given starting reaction mixture were made by the GRNN method. A few initial experimental verifications were also made which resulted in the syntheses of zeolites X and P from previously unknown compositions [12].

A detailed theoretical investigation of the rather complex and high-dimensional relationship between the XRD peaks and the crystallographic properties of various zeolites (as well as other crystalline materials) may be very useful to provide a more common use of the XRD technique in the prediction of the framework crystal structures of unknown materials. In this study, ANN methods and the cross validation technique were utilized to perform this investigation. Some past studies have not revealed significant advantage of using relatively high k values in k-fold cross validation [13]. Fivefold cross validation was utilized in this study. The results obtained were compared to actual zeolite properties reported in the literature, as well as to estimations made by using multilinear regression.

## 2 Theory

### 2.1 X-Ray diffraction technique

Crystals are regular arrays of atoms, and X-rays can be considered as waves of electromagnetic radiation. Atoms scatter X-ray waves, primarily through their electrons. An X-ray striking an electron produces secondary spherical waves emanating from the electron, which is known as elastic scattering. Although these waves cancel one another out in most directions through destructive interference, they add constructively in a few specific directions, determined by Bragg's law,

$$2d\sin\theta = n\lambda \tag{1}$$

where $d$ is the spacing between diffracting planes in $\mathring{A}$, $\theta$ is the incident angle in degrees, $n$ is any integer, and $\lambda$ is the wavelength of the beam in $\mathring{A}$. These specific directions appear as spots on the diffraction pattern. It should be mentioned that X-rays have wavelengths on the order of a few angstroms, the same as typical interatomic distances in crystalline solids. This means that X-rays can be diffracted from minerals which, by definition, are crystalline and have regularly repeating atomic structures. In the XRD technique, the X-ray intensity is recorded and reported as a function of the $2\theta$ angle.

### 2.2 Artificial neural networks

Artificial neural networks are black box models that can perform an estimation using limited input and output data patterns. They can model nonlinear statistical data by simulating the structure and/or functional aspects of biological neural networks. In most cases, ANNs are adaptive systems that change structure depending on external or internal information that flows through the network during the learning phase. In this study, the Generalized Regression Neural Networks (GRNN) and Radial Basis Function-Based Neural Networks (RBF) methods were used to relate the XRD data to the framework properties of zeolites.

The basics of the GRNN can be found in the literature [14, 15]. The GRNN method does not require an iterative training procedure but instead estimates any arbitrary function between input and output vectors, drawing the function estimate directly from the training data. The GRNN is based on a standard statistical technique called kernel regression. By definition, the regression of a dependent variable $y$ on an independent $x$ estimates the most probable value for $y$, given $x$ and a training set. The regression method will produce the estimated value of $y$, which minimizes the mean-squared error. The GRNN consists of four layers: input layer, pattern layer, summation layer, and output layer. The first layer is fully connected to the second, pattern layer, where each unit represents a training pattern and its output is a measure of the distance of the input from the stored patterns. Each pattern layer unit is connected to the two neurons in the summation layer: S-summation neuron and D-summation neuron. The S-summation neuron computes the sum of the

![](./images/811783874886500353_2.jpg)

weighted outputs of the pattern layer while the D-sum- mation neuron calculates the unweighted outputs of the pattern neurons. The connection weight between the $i$th neuron in the pattern layer and the S-summation neuron is $y_i$, the target output value corresponding to the $i$th input pattern. For D-summation neuron, the connection weight is unity. The output layer merely divides the output of each S-summation neuron by that of each D-summation neuron. In this method, the spread $\sigma$ is a smoothing parameter, the optimal value of which is often determined experimentally [16]. When the spread parameter $\sigma$ is made large, the estimated density is forced to be smooth and in the limit becomes a multivariate Gaussian with covariance $\sigma^{2} I$. On the other hand, a smaller value of $\sigma$ allows the estimated density to assume non-Gaussian shapes, but with the haz- ard that wild points may have too great an effect on the estimate.

Radial Basis Functions are powerful techniques for interpolation in multidimensional space. RBF networks were introduced into the neural network literature as a model motivated by the locally tuned response observed in biological neurons [17]. Neurons with a locally tuned response characteristic can be found in several parts of the nervous system, for example, cells in the visual cortex sensitive to bars oriented in a certain direction or other visual features within a small region of the visual field [18]. These locally tuned neurons show response characteristics bounded to a small range of the input space. The theoretical basis of the RBF approach lies in the field of interpolation of multivariate functions.

The interpretation of the RBF method as an artificial neural network consists of three layers: a layer of input neurons feeding the feature vectors into the network; a hidden layer of RBF neurons, calculating the outcome of the basis functions; and a layer of output neurons, calcu- lating a linear combination of the basis functions [19]. The input layer sends copies of the input variables to each node in the hidden layer. The nodes in the hidden layer are each specified by a transfer function, which transforms the incoming signals. The network output is given by a linear weighted summation of the hidden node responses at each node in the output layer. The choice of the RBF in the hidden layer is not crucial to the network performance as long as localized activations are near the center and func- tion decays rapidly as it takes values away from the center. In this study, the most common RBF function, i.e., the Gaussian, was employed.

### 2.3 Method

Zeolites are hydrated microporous crystalline materials. The zeolite framework consists of an assemblage of $SiO_{4}$ and $AlO_{4}$ tetrahedra, joined together in various regular arrangements through shared oxygen atoms, to form an open crystal lattice. The micropore structure is determined by the crystal lattice, which contains pores of molecular dimensions into which guest molecules can penetrate. The cations (e.g., Na) are placed in special positions near the Al atoms. The pore size varies for different zeolites, depend- ing on the arrangement of the atoms forming the zeolite crystal structure. The crystal structure of a material or the arrangement of atoms in a crystal structure can be descri- bed in terms of its unit cell. The unit cell is a tiny box with one or more spatial arrangements of atoms. The unit cells stacked in three-dimensional space describe the bulk arrangement of atoms of the crystal. The crystal structure has a three-dimensional shape. The unit cell may be rep- resented by its lattice parameters, including the length of the cell edges and the angles between them.

In this study, data obtained from the literature, describing the XRD patterns of different zeolites, were used in the estimations carried out by the GRNN and RBF methods. The components of the input vector were the $2 \theta$ angles of eight XRD peaks with the highest intensity, pertaining to different zeolites, while the components of the output vector were the minimum and maximum dimensions of the largest pores of zeolites $(r_{1}$ and $r_{2})$, their framework densities (fd) and the lengths of their unit cell edges (a, b and c). The framework density may be defined as the number of T (Si or Al) atoms per $1,000 \AA^{3}$. The pores of some zeolites are not uniform in size, and some others may have pore channels of different lengths. In this study, the largest and smallest dimensions of the most prominent pore opening in these materials were taken into consideration.

The application of the ANNs to data consisted of two steps. The first step was the training of the neural networks, which comprised the presentation of training data describing the input and output to the network and obtaining the inter-connection weights. The input and output data were normalized between 0 and 1 prior to the training. Once the training stage was completed, the ANNs were applied to the testing data. Fivefold cross validation was performed. Accordingly, the total of 131 XRD data [20, 21] utilized in this study was partitioned into five disjoint sets. Four sets were used for training the network and the omitted set (testing set) was used to compute the prediction error. Four of the datasets contained 26 data while one dataset consisted of 27 data. The network was trained five times, each time leaving out one of the data sets. In this study, different spreads, varied in a regular interval, were tried to find the best one that gave the minimum difference between predicted and experimental values for the utilization of the GRNN and RBF methods. The average of the spreads providing the smallest errors for the use of the five different testing datasets was then

![](./images/811783874886500353_3.jpg)

estimated. After this step, the ANN estimations were per- formed again for the five distinct cases mentioned above by using the average spread value to obtain new results. Finally, the average value of these five new predictions was calculated. This procedure was repeated for all six parameters (a, b, c, $r_1$, $r_2$, fd) investigated in this study. The ANN methods were used to predict only one component of the output vector at a time.

For the estimations carried out by RBF, initially, dif- ferent numbers of hidden layer neurons were tried. The hidden layer neuron number that gave the minimum dif- ference between predicted and experimental values was determined not to vary significantly for the utilization of different data and parameters investigated in this study. Thus, the hidden layer neuron number was taken to be equal to 15 for all the cases investigated.

An additional investigation was also carried out to determine the effect of the number of data used for training the neural networks, on the prediction performance of the networks. In this case, the training data used in the first set of investigations mentioned above were separated into two, for each of the five different combinations of training/ testing data. These two different datasets, in each data combination, were utilized for training the neural networks separately, such that the number of data in each set used for training was reduced from 104 (or 105) to 52 (or 53) while the number of testing data was kept constant as before. The procedure described above for the first approach was fol- lowed, first, by taking the average of the spread values providing the smallest errors in the ten different estima- tions performed. Then, the average spread value was uti- lized for performing ten new estimations and, finally, the average of these new predictions were determined for all the parameters investigated.

The results obtained by using the GRNN and RBF methods were compared to the actual values [20, 21] as well as to those values estimated by using multilinear regression. In regression, relationships between the $2\theta$ angles of eight XRD peaks and the minimum, maximum pore dimensions, framework densities and lengths of the unit cell edges of zeolites were determined by using exactly the same five (training) datasets used in neural network predictions. The information obtained was used in the estimation of the minimum, maximum dimensions of the pores, framework densities and lengths of the unit cell edges of the zeolites utilized in the testing stages of the ANN predictions. The average of the errors obtained for the five distinct datasets (testing data for the ANNs) was finally reported for all the parameters investigated. Since a similar theoretical attempt, for determining such a rela- tionship has not been performed before, the comparison of the results obtained from ANN methods to those deter- mined by multilinear regression may be a reasonable first approach. Some nonlinear equation types were also tested, but their predictive power was not sufficient for our purpose.

The regression model of simple linear form utilized in this study is given below. $R$ might represent the minimum pore size, maximum pore size, framework density or the length of one of the unit cell edges of zeolites.

$$
\begin{aligned}
R= & a_{0}+a_{1}\left(2 \theta_{1}\right)+a_{2}\left(2 \theta_{2}\right)+a_{3}\left(2 \theta_{3}\right)+a_{4}\left(2 \theta_{4}\right) \\
& +a_{5}\left(2 \theta_{5}\right)+a_{6}\left(2 \theta_{6}\right)+a_{7}\left(2 \theta_{7}\right)+a_{8}\left(2 \theta_{8}\right)
\end{aligned} \tag{2}
$$

The coefficients in (2) were determined by using the Marquardt-Levenberg algorithm.

The relative error ($d$) was used to monitor the success of the ANN methods and regression used in the prediction of zeolite crystal properties from the $2\theta$ angles of the X-ray diffraction patterns. $d$ was determined by taking into con- sideration the deviation (%) of the pore sizes, framework densities or lengths of the unit cell edges of zeolites, cal- culated by using the ANN methods or regression ($c_{\text{calc}}$), from the corresponding actual values ($c_{\text{act}}$).

$$
d=\left|c_{\text{act}}-c_{\text{calc}}\right| / c_{\text{act}} \times 100 \tag{3}
$$

$d_m$ was defined as the arithmetic mean of the relative errors obtained for the different data used in prediction.

## 3 Results and discussion

### 3.1 Criteria assuring best performance for the GRNN and RBF methods

As mentioned before, the predictions of the minimum and maximum dimensions of the pores ($r_1$, $r_2$), framework densities (fd) and lengths of the unit cell edges of zeolites (a, b, c) were performed by fivefold cross validation using GRNN and RBF methods. The network structure pro- viding the best result was determined according to the success of the predictions performed by employing the testing data. It was also established that the conditions providing the best results in the testing stage could allow the ANN method to exhibit quite high performances in the training stage.

For the GRNN method, spread factors in the range 0.16–0.36 were the conditions determined to give the best results. The average spread factor was determined to be equal to 0.16, 0.20, 0.31, 0.36, 0.31 and 0.23 for $r_1$, $r_2$, fd, a, b and c, respectively, by using the testing data. For the RBF method, spreads in the range 0.14–0.28 and 15 neu- rons, as explained before, were the conditions determined to give the best results. The average spread was determined to be equal to 0.23, 0.27, 0.28, 0.14, 0.15 and 0.27 for $r_1$, $r_2$, fd, a, b and c, respectively, by using the testing data. When the optimization was performed by using training data,

![](./images/811783874886500353_4.jpg)

without taking into consideration testing data, the $d_m$ values, representing the deviation of the predicted values from actual values, were less than 10% for all the cases investigated.

### 3.2 Evaluation of the predictions made by the GRNN and RBF methods

The results are depicted in Figs. 1, 2, 3, 4, 5, and 6 and Tables 1 and 2. Figures 1, 2, 3, 4, 5, and 6 show the proximity of the values estimated by the ANNs to the actual values of $r_1$, $r_2$, fd, a, b, and c, respectively, when the average spread values and one of the testing datasets were utilized. It may be observed from the figures that the GRNN and RBF methods provided fairly good fits to the actual results for most of the data, though there were some discrepancies. The deviation from actual values was relatively high for some extreme values of the parameters investigated.

The average deviations of the results obtained by using the ANN methods from the actual values may be observed more clearly from Table 1. The performance exhibited by multilinear regression may also be seen therein. It may be observed from Table 1 that when fivefold cross validation was used, the GRNN method provided better fits than the RBF method and multilinear regression for the minimum pore size ($r_1$), maximum pore size ($r_2$) and the length of the unit cell edge (c). RBF method provided better fits than the other methods investigated for the framework density (fd) and the lengths of the unit cell edges of zeolites (a, b) estimations. The agreement between the estimate made by RBF and the actual framework density was especially significant. In general, the discrepancies obtained for the lengths of unit cell edges, a, b and c, were higher. The results obtained for regression given in Table 1 should also be taken into consideration before arriving at a conclusion about the success of the ANN methods in the prediction of the zeolite framework properties. When multilinear regression was utilized, the average deviation from the

![](./images/811783874886500353_5.jpg)

Fig. 1 Zeolite pore size ($r_1$) predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

![](./images/811783874886500353_6.jpg)

Fig. 2 Zeolite pore size ($r_2$) predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

![](./images/811783874886500353_7.jpg)

Fig. 3 Framework density, fd, predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

![](./images/811783874886500353_8.jpg)

Fig. 4 Unit cell length, a, predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

![](./images/811783874886500353_9.jpg)

Fig. 5 Unit cell length, b, predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

![](./images/811783874886500353_10.jpg)

Fig. 6 Unit cell length, c, predictions by (times) GRNN and (open triangle) RBF in comparison with (open square) actual values

<table>
<caption>Table 1 Average relative errors obtained for the predictions made by different methods</caption>
<thead>
<tr>
<th>Method</th>
<th colspan="6">$d_m$ (%)</th>
</tr>
<tr>
<th></th>
<th>$r_1$</th>
<th>$r_2$</th>
<th>fd</th>
<th>a</th>
<th>b</th>
<th>c</th>
</tr>
</thead>
<tbody>
<tr>
<td>GRNN</td>
<td>16.3</td>
<td>11.8</td>
<td>8.2</td>
<td>20.8</td>
<td>22.8</td>
<td>23.7</td>
</tr>
<tr>
<td>RBF</td>
<td>18.6</td>
<td>14.4</td>
<td>7.6</td>
<td>19.6</td>
<td>22.1</td>
<td>25.8</td>
</tr>
<tr>
<td>Regression</td>
<td>28.9</td>
<td>25.7</td>
<td>10.0</td>
<td>34.8</td>
<td>34.7</td>
<td>55.3</td>
</tr>
</tbody>
</table>

actual values was higher than those provided by the ANN methods tested. The largest amount of error was observed for the estimations carried out by multilinear regression to predict the length of unit cell edge, c. This parameter represented the most problematic case for prediction by regression and the improvement provided by the ANNs seemed to be quite significant.

As mentioned before, an additional investigation was also performed, in order to observe the effect of using a smaller number of data on the prediction performance. Accordingly, one half of the training data used in the first approach was employed in this case. The results obtained are depicted in Table 2. It may be observed from the table that the performance of the ANN models decreased, to some extent, when the number of training data used was reduced. More noteworthy differences were observed in the estimation of fd, $r_1$ and $r_2$ by using the RBF method. These results indicate that there is still some room for improvement, which may possibly be achieved by providing additional suitable data for training.

<table>
<caption>Table 2 Average relative errors obtained for the predictions made by ANNs when the number of training data was halved</caption>
<thead>
<tr>
<th>Method</th>
<th colspan="6">$d_m$ (%)</th>
</tr>
<tr>
<th></th>
<th>$r_1$</th>
<th>$r_2$</th>
<th>fd</th>
<th>a</th>
<th>b</th>
<th>c</th>
</tr>
</thead>
<tbody>
<tr>
<td>GRNN</td>
<td>18.3</td>
<td>12.3</td>
<td>8.7</td>
<td>21.3</td>
<td>23.7</td>
<td>24.7</td>
</tr>
<tr>
<td>RBF</td>
<td>21.3</td>
<td>17.5</td>
<td>8.8</td>
<td>20.2</td>
<td>22.8</td>
<td>26.9</td>
</tr>
</tbody>
</table>

ANN methods were utilized quite successfully, especially, to predict the framework densities and maximum pore sizes of zeolites from XRD data. The average relative errors in the best cases were equal to 7.6% and 11.8% for the former and latter parameters, respectively, when ANN methods were utilized. The zeolite framework density, which is related to porosity, is a significant parameter describing zeolitic structure. The success of the prediction of the framework density from XRD data by ANNs was not very surprising since regression also seemed to predict this parameter fairly well. The maximum pore size is another important parameter related to zeolites, and its successful prediction by ANNs might be very useful. The lengths of the unit cell edges, a, b and c as well as the minimum pore size, $r_1$, were predicted fairly well by ANNs with the smallest average relative errors amounting to 19.6, 22.1, 23.7 and 16.3%, respectively.

## 4 Conclusions
It was shown that information might be gained about the framework crystal structures of zeolites from XRD data by using artificial neural network methods. ANN methods generally provided quite better predictions than multilinear regression for this purpose. RBF had higher predictive power for some of the parameters while GRNN exhibited better performance for others. The best prediction was made for the framework densities of zeolites, with a quite small difference between the actual and estimated values. For especially the prediction of the framework densities and pore sizes of zeolites, RBF neural networks learned better from XRD data when a

higher number of training data was utilized in this study. The superiority of the ANNs over conventional methods for the prediction of complex and high-dimensional relationships, such as the one investigated in this study, might be attributed to the capability of the ANNs to capture the nonlinear features and generalize the structure of the whole data set.

The use of artificial neural network methods together with X-ray diffraction patterns can provide a quick and very simple means for establishing a preliminary opinion about the framework structures of unknown materials. This can ease and support the discovery of novel crystalline materials. It should also be remembered that in case additional training data may be used with ANN models to make the predictions, the relative success of prediction may still improve. Different ANN methods may also be tested for possible improvements in the prediction of framework crystal structures from XRD data.

### References
1. Weitkamp J (2000) Zeolites and catalysis. Solid State Ionics 131(1–2):175–188
2. Caro J, Noack M, Kolsch P, Schafer R (2000) Zeolite membranes-state of their development and perspective. Micropor Mesopor Mat 38(11):3–24
3. Ruthven DM (1988) Zeolites as selective adsorbents. Chem Eng Prog 84:42–50
4. Mintova S, Bein T (2001) Nanosized zeolite films for vapor-sensing applications. Micropor Mesopor Mat 50(2–3):159–166
5. McCusker LB (1991) Zeolite crystallography. Structure determination in the absence of conventional single-crystal data. Acta Cryst A47:297–313
6. Hussain MA (1999) Review of the applications of neural networks in chemical process control-simulation and online implementation. Artif Intel Eng 13(1):55–68

7. Huang K, Chen F, Lu D (2001) Artificial neural network-aided design of a multi-component catalyst for methane oxidative coupling. Appl Catal A 219(1–2):61–68
8. Serra JM, Corma A, Chica A, Argente E, Botti V (2003) Can artificial neural networks help the experimentation in catalysis? Catal Today 81(3):393–403
9. Chakraborty M, Bhattacharya C, Dutta S (2003) Studies on the applicability of artificial neural network (ANN) in emulsion liquid membranes. J Membrane Sci 220(1–2):155–164
10. Sharma R, Singhal D, Ghosh R, Dwivedi A (1999) Potential applications of artificial neural networks to thermodynamics: vapor-liquid equilibrium predictions. Comput Chem Eng 23(3):385–390
11. Tatlier M, Cigizoglu HK, Erdem-Şenatalar A (2005) Artificial neural network methods for the estimation of zeolite molar compositions that form from different reaction mixtures. Comput Chem Eng 30(1):137–146
12. Tatlier M, Cigizoglu KB, Cigizoglu HK, Erdem-Şenatalar A (2008) Low-silica zeolite coatings prepared by using predictions from an artificial neural network method. J Porous Mat 15(4):389–395
13. Feng C-XJ, Yu Z-G, Kingi U, Baig MP (2005) Threefold vs. fivefold cross validation in one-hidden-layer and two-hidden-layer predictive neural network modeling of machining surface roughness data. J Manuf Syst 24(2):93–107
14. Specht DF (1991) A general regression neural network. IEEE T Neural Networ 2(6):568–576
15. Tsoukalas LH, Uhrig RE (1997) Fuzzy and neural approaches in engineering. Wiley, New York
16. Kim B, Kim S, Kim K (2003) Modeling of plasma etching using a generalized regression neural network. Vacuum 71(4):497–503
17. Broomhead D, Lowe D (1988) Multivariable functional interpolation and adaptive networks. Complex Syst 2:321–355
18. Poggio T, Girosi F (1990) Regularization algorithms for learning that are equivalent to multilayer networks. Science 247(4945):978–982
19. Taurino AM, Distante C, Siciliano P, Vasanelli L (2003) Quantitative and qualitative analysis of VOCs mixtures by means of a microsensors array and different evaluation methods. Sensor Actuat B 93(1–3):117–125
20. Baerlocher Ch, Meier WM, Olson DH (2001) Atlas of zeolite framework types. Elsevier, Amsterdam
21. Treacy MMJ, Higgins JB (2001) Collection of simulated XRD powder patterns for zeolites. Elsevier, Amsterdam

![](./images/811783874886500353_11.jpg)