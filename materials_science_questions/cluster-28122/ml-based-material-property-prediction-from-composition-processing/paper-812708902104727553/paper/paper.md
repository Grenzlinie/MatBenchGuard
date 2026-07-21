IOP Conference Series: Materials Science and Engineering

PAPER • OPEN ACCESS

# Study on the Forecasting of the Hot Corrosion Resistance of Typical Superalloys for Aeroengines

To cite this article: Guo Bingxiu *et al* 2019 *IOP Conf. Ser.: Mater. Sci. Eng.* **685** 012025

View the [article online](article online) for updates and enhancements.

This content was downloaded from IP address 193.202.81.178 on 22/04/2020 at 16:58

# Study on the Forecasting of the Hot Corrosion Resistance of Typical Superalloys for Aeroengines

Bingxiu Guo, Xiaohui Wang*, Yanyan Wang and Yue Shao

School of Reliability and Systems Engineering, Beihang University, Beijing, P. R.China

*Email: xiaohuiw@buaa.edu.cn

**Abstract.** The high-temperature components of aeroengines are in contact with gas flow for a long time, making them susceptible to hot corrosion, which can affect the reliability and lifespan of aeroengines. In this study, five types of superalloys commonly used in the high-temperature components of Aeroengines are selected for gas-based hot corrosion tests, and the corrosion rates are calculated using the weight loss method. Gradient Boosting Regression Tree (GBRT) machine learning algorithm is utilized to establish a corrosion rate forecasting model. The evaluation results show the predictability of this method. The effect of input parameters, including main alloy chemical composition and corrosion time, on the corrosion rate was discussed using GBRT and critical factors are obtained. These results provide a reference for the protection of aeroengines from hot corrosion.

## 1. Introduction
The hot-end components of aeroengines, including combustion chambers, gas turbines, power turbines and exhaust systems, are directly exposed to high-temperature gas for a long time. Sulfates accumulated on the surface after combustion will cause accelerated oxidation, resulting in serious thermal corrosion[1]. As materials with multiphase structure and complex components, superalloys have good impact resistance and oxidation resistance, making them widely used in the hot-end parts of aeroengines[2-4].

Scholars have studied the hot corrosion resistance of different types of superalloys under various preparation processes in complex environments. The literature has established that the research methods for the hot corrosion resistance of superalloys to mostly focus on the performance test and corrosion products analysis after the test. However, the hot corrosion test has certain limitations in studying many corrosion influencing factors and corrosion laws of alloy, due to the complex reacting process, long cycle and high cost of test data sets. Corrosion prediction technology, which analyzes, models, verifies and analyzes corrosion test data, can obtain information from the existing experimental data through the establishment of dynamic model and statistical model. Further, it provides a new framework for further research and real-world application. At present, the corrosion prediction statistical model of poor information system, including Cellular Automata, Principal Component Analysis, and Grey System Theory, has been applied in aviation materials, reinforced concrete structures, and other fields.

A rapidly growing field, machine learning has been largely employed by many scholars in recent years to solve corrosion problems. For example, Fang et al.[5] proposed a genetic algorithm (GA) and support vector regression (SVR) combined method and can successfully predict atmospheric corrosion

![](./images/812708902104727553_1.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Published under licence by IOP Publishing Ltd

of metallic materials such as zinc and steel. Chou et al.[6] applied a single model and a set model for machine learning prediction to predict the pitting corrosion risk of reinforced concrete and the rate of marine corrosion of carbon steel. Mousavifard et al.[7] used the artificial neural network (ANN) and adaptive neuro-fuzzy inference systems (ANFIS) to model the corrosion rate as a function of pH, zirconium concentration, temperature, and immersion time for a hot dip galvanized steel.

In this paper, five typical superalloys used in aeroengines were selected as test objects for the gas hot-corrosion test, and the corrosion rate was calculated by the weight loss method. Gradient Boosting Regression Tree (GBRT) was applied to model the corrosion rate with corrosion time and main chemical composition for five types of superalloys after test. The influence of the main chemical composition in the superalloy on the corrosion rate was explored using GBRT. The effects of important alloy constituents such as Ni, Al, Ti, Mn, Mo and Co on the corrosion rate were obtained. The results contributed to better understand hot corrosion protection and provided a reference for the selection of aeroengines.

## 2. Materials and Methods

### 2.1. Test materials
Table 1 describes the five test materials selected in this paper. Table 2 gives the chemical composition of the materials.

Table 1. Test materials
<table>
  <tr>
    <td>Name</td>
    <td>Attribute</td>
    <td>Use</td>
  </tr>
  <tr>
    <td>GH3625</td>
    <td>Cr-Mo-Nb solid solution strengthened nickel-base superalloy</td>
    <td>Engine combustion chamber, exhaust system, tool</td>
  </tr>
  <tr>
    <td>GH2132</td>
    <td>Fe-25Ni-15Cr base superalloy</td>
    <td>Engine turbine disk, compressor disk, etc.</td>
  </tr>
  <tr>
    <td>GH605</td>
    <td>20Cr-15W solid solution strengthened cobalt-based superalloy</td>
    <td>Engine blades, combustion chambers, etc.</td>
  </tr>
  <tr>
    <td>GH3536</td>
    <td>Cr-Mo solid solution strengthened nickel-base superalloy</td>
    <td>Engine combustion chamber</td>
  </tr>
  <tr>
    <td>GH4738</td>
    <td>Ni-Cr-Co-based superalloy</td>
    <td>Engine gas turbine</td>
  </tr>
</table>

Table 2. superalloy chemical compositions
<table>
  <tr>
    <td>Name</td>
    <td colspan="14">(wt,%)</td>
  </tr>
  <tr>
    <td>GH3625</td>
    <td>Ni</td>
    <td>Cr</td>
    <td>Mo</td>
    <td>Nb</td>
    <td>Fe</td>
    <td>Co</td>
    <td>Si</td>
    <td>Mn</td>
    <td>Ti</td>
    <td>Al</td>
    <td>C</td>
    <td>Cu</td>
    <td>P, S</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>61.85</td>
    <td>21.50</td>
    <td>9</td>
    <td>3.65</td>
    <td>2.50</td>
    <td>0.50</td>
    <td>0.25</td>
    <td>0.25</td>
    <td>0.20</td>
    <td>0.20</td>
    <td>0.05</td>
    <td>0.04</td>
    <td>0.01</td>
    <td></td>
  </tr>
  <tr>
    <td>GH2132</td>
    <td>Fe</td>
    <td>Ni</td>
    <td>Cr</td>
    <td>Ti</td>
    <td>Mo</td>
    <td>Mn</td>
    <td>Si</td>
    <td>Al</td>
    <td>C</td>
    <td>V</td>
    <td>P, S</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>54.16</td>
    <td>25.50</td>
    <td>15</td>
    <td>2.025</td>
    <td>1.25</td>
    <td>1</td>
    <td>0.50</td>
    <td>0.20</td>
    <td>0.04</td>
    <td>0.03</td>
    <td>0.025</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>GH605</td>
    <td>Co</td>
    <td>Cr</td>
    <td>W</td>
    <td>Ni</td>
    <td>Mn</td>
    <td>Fe</td>
    <td>Si</td>
    <td>C</td>
    <td>P, S</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>51.67</td>
    <td>20</td>
    <td>15</td>
    <td>10</td>
    <td>1.50</td>
    <td>1.50</td>
    <td>0.20</td>
    <td>0.10</td>
    <td>0.04</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>GH3536</td>
    <td>Ni</td>
    <td>Cr</td>
    <td>Fe</td>
    <td>Mo</td>
    <td>Co</td>
    <td>W</td>
    <td>Mn</td>
    <td>Si</td>
    <td>Cu</td>
    <td>C</td>
    <td>Ti</td>
    <td>Al</td>
    <td>P, S</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>46.96</td>
    <td>21.75</td>
    <td>18.50</td>
    <td>9</td>
    <td>1.50</td>
    <td>0.60</td>
    <td>0.50</td>
    <td>0.50</td>
    <td>0.25</td>
    <td>0.10</td>
    <td>0.25</td>
    <td>0.08</td>
    <td>0.02</td>
    <td></td>
  </tr>
  <tr>
    <td>GH4738</td>
    <td>Ni</td>
    <td>Cr</td>
    <td>Co</td>
    <td>Mo</td>
    <td>Ti</td>
    <td>Al</td>
    <td>Fe</td>
    <td>Si</td>
    <td>C</td>
    <td>Cu</td>
    <td>Mn</td>
    <td>P,S,B</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>57.04</td>
    <td>19.50</td>
    <td>13.50</td>
    <td>4.25</td>
    <td>3</td>
    <td>1.40</td>
    <td>1</td>
    <td>0.08</td>
    <td>0.07</td>
    <td>0.05</td>
    <td>0.05</td>
    <td>0.07</td>
    <td></td>
    <td></td>
  </tr>
</table>

### 2.2. Experimental
The gas hot-corrosion test in this study is a cold-heat alternating cycle test of the sample in a gas formed under the conditions of a specified temperature, a fuel flow rate, an oil-gas ratio and sea salt content. This method can simulate the working environment of an aeroengine and evaluate the hot

corrosion resistance of materials and has been widely used[8,9]. The conditions under which the gas is formed in this study are as follows:

Test Temperature (℃): 900;
Gas-oil ratio: 1/45;
Fuel flow (L/h): 0.2;
Seawater discharge: 0.2;
Air flow rate (L/h): 9;
Seawater concentration ($\times 10$-6): 20.

Each material consists of three samples. All samples have no surface treatment. The samples were placed in the prescribed gas environment for 100h, heat preservation 55 min and cooling 5 min per hour, every 25 hours take out and weigh the samples.

### 2.3. Calculation of the corrosion rate
In this study, the corrosion rate was selected to evaluate the corrosion resistance of the materials. The weight loss method is a method for determining the corrosion rate of a sample before and after corrosion. Generally, the metal is made into the shape and size of the test piece and placed in a corrosive environment. After a certain period of time, the weight change is measured, and the corrosion rate v can be calculated.

$$
v=\frac{m_{0}-m_{t}}{S t} \tag{1}
$$

where $v$ represents the corrosion rate, $m_{0}$ represents the precorrosion weight, $m_{t}$ represents the weight after the test, $t$ represents the corrosion time, $S$ represents the surface area of a sample.

### 2.4. Gradient boosting regression tree (GBRT)
Gradient boosting regression tree (GBRT) is a combinatorial algorithm that uses the decision tree (CART) (as the basic learning device) and gradient boosting (to train several times)[10]. Each decision tree is used to evaluate the residuals of all previous trees. The results of each tree are added up to obtain the final prediction value. GBRT is regarded as one of the best algorithms for prediction. Its good reputation for its capacity to sort and analyze the importance of the input of the model,as well as to express complex laws.

## 3. Result and Discussion

### 3.1. Description of the test results
Table 3 shows the corrosion rate of 15 items. Negative values in Table 3 indicates that the weight of the corrosion product exceeds the corrosion loss. Combined with the corrosion rate data, it obtained that GH605 exhibits the most serious corrosion 100h after the test, while GH3625 and GH2132 have some slight corrosion. GH3536 and GH4738 have almost no corrosion.

**Table 3. corrosion rate data set**

<table>
  <thead>
    <tr>
      <th rowspan="2">Materals</th>
      <th rowspan="2">Number</th>
      <th colspan="4">Corrosion rate(g/(m²*h))</th>
    </tr>
    <tr>
      <th>Time 25/h</th>
      <th>Time 50/h</th>
      <th>Time 75/h</th>
      <th>Time 100/h</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">GH3625</td>
      <td>1</td>
      <td>0.5775</td>
      <td>0.3108</td>
      <td>0.2355</td>
      <td>0.1834</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.5911</td>
      <td>0.3227</td>
      <td>0.2582</td>
      <td>0.1987</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.5741</td>
      <td>0.3125</td>
      <td>0.2514</td>
      <td>0.1546</td>
    </tr>
    <tr>
      <td rowspan="3">GH2132</td>
      <td>4</td>
      <td>0.1732</td>
      <td>0.0934</td>
      <td>0.1268</td>
      <td>0.2217</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.1529</td>
      <td>0.0798</td>
      <td>0.1008</td>
      <td>0.2285</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.2955</td>
      <td>0.1189</td>
      <td>0.1042</td>
      <td>0.1512</td>
    </tr>
    <tr>
      <td>GH605</td>
      <td>7</td>
      <td>0.9262</td>
      <td>5.3206</td>
      <td>6.751</td>
      <td>8.0735</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td rowspan="2">
      </td>
      <td>8</td>
      <td>0.6849</td>
      <td>5.6546</td>
      <td>6.8339</td>
      <td>7.7944</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1.6882</td>
      <td>3.8241</td>
      <td>6.4715</td>
      <td>8.0446</td>
    </tr>
    <tr>
      <td rowspan="3">GH3536</td>
      <td>10</td>
      <td>-0.0815</td>
      <td>-0.0815</td>
      <td>-0.0566</td>
      <td>-0.0391</td>
    </tr>
    <tr>
      <td>11</td>
      <td>-0.0951</td>
      <td>-0.073</td>
      <td>-0.06</td>
      <td>-0.0433</td>
    </tr>
    <tr>
      <td>12</td>
      <td>-0.1461</td>
      <td>-0.09</td>
      <td>-0.0566</td>
      <td>-0.0467</td>
    </tr>
    <tr>
      <td rowspan="3">GH4738</td>
      <td>13</td>
      <td>-0.1393</td>
      <td>-0.0883</td>
      <td>-0.0396</td>
      <td>-0.028</td>
    </tr>
    <tr>
      <td>14</td>
      <td>-0.1155</td>
      <td>-0.0764</td>
      <td>-0.0328</td>
      <td>-0.0238</td>
    </tr>
    <tr>
      <td>15</td>
      <td>-0.1393</td>
      <td>-0.0985</td>
      <td>-0.0442</td>
      <td>-0.0314</td>
    </tr>
  </tbody>
</table>

### 3.2. Corrosion rate forecasting model

#### 3.2.1. Model establishment.
Scikit-learn is a machine learning library based on python, which can facilitate the implementation of machine learning algorithms. In this research, the 11 components of the superalloys and the corrosion time were selected as features in GBRT. The corrosion rate was used as objective value. 90% and 10% of total experimental data (60 data) were used as training and testing data set randomly. The process was repeated 10 times. Ten different training processes and test sets were used to get the average performance of GBRT. A 8-fold cross-validation was used to train data to improve the generalization of the model, which means the training data set was randomly divided into eight parts and each of parts taken turns as the validation data set.

#### 3.2.2. Model parameter selection.
Combining the characteristics of the experimental data, this study selected the main parameters of each model by using GridsearchCV in Scikit-learn to adjust the parameters of the models in the Python environment. The specific description of the main parameters is as follows:

The maximum depth of the decision tree depends on the interaction between the input variables. The number of decision trees represents the number of gradient enhancements, which has strong robustness to overfitting of the model. Figure 1 shows the relationship between the number of decision trees (Boosting Iterations) and the mean square error (MSE) in GBRT. This study determined that the number of decision trees is 500 and the maximum depth is 3. Other parameters were set as the default parameters in sklearn.

![](./images/812708902104727553_2.jpg)

Figure 1. Relationship between Boosting Iterations and MSE in GBRT

#### 3.2.3. Evaluation of predictive effects.
The mean square error (MSE) and the determination coefficient (R2 score) are selected as the evaluation indicators of the model forecasting effect. It was calculated MSE=0.0451,R2=0.9922 in the training set, MSE=0.0477,R2=0.9696 in the testing set.It can be seen that the GBRT could predict the corrosion rate with a good reliability for the training set and the testing set.

### 3.3. GBRT model

#### 3.3.1. Evaluation of feature importance.
Feature_importance in Scikit-learn is used to output the importance ranking and score for each feature. Figure 2 shows the importance of 11 features. In GBRT, time is the factor that affects the maximum corrosion rate. Among chemical composition of superalloys, Mn, Co, Al, Ni, Ti, and Mo have the greatest influence on the corrosion rate, and the remaining components have less influence.

![](./images/812708902104727553_3.jpg)

**Figure 2.** Importance order of corrosion factors

#### 3.3.2. Effect of influencing factors on the corrosion rate.
The "partial_dependence" function in GBRT shows the independence between the target correspondence and a set of features, excluding all other features. Partial_dependence can be interpreted as expected target responses, and function of target characteristics.

A one-dimensional partially dependent as a function to study the relationship between corrosion rate and the chemical compositions for Mn, Co, Ti, Ni, Mo and Al, is calculated by partial_dependence. Figure 3 shows the following:

-   Increasing the content of Ti, Al and Mo with a certain specific gravity could reduce the corrosion rate very effectively. After a certain proportion, the increase of Al and Mo would not affect the corrosion rate, the effect of Ti would also be greatly reduced.
-   When the content of Ni fell within the range of $10\% \sim 25\%$, the corrosion of superalloys could be inhibited, but the corrosion rate was not affected when the content was more than $30\%$.
-   Corrosion would be aggravated when the content of Co exceeds $20\%$, so the content of Co should not be large in the design. In combination with Figure 2 and Figure 3, a small amount of Mn would also aggravate the corrosion to a great extent. Therefore, the content of Mn should be strictly controlled in superalloy design not to exceed $1\%$.

A two-dimensional partial dependence function to calculate the relationship between corrosion rate and four sets of feature combinations. Figure 4 shows the effect of time-Al, time-Ni, time-Co, Ni-Co on corrosion rate. The color in the figure represents an increase in corrosion rate from dark to light. In Figure 4(a), 4(b), inclined trend lines indicate the correlation between the Al, Ni content in a certain range and the corrosion time. With the increase of corrosion time, the inclined degree of trend line is greater, which indicates that the suppression effect of Al, Ni element on corrosion was more obvious with the process of corrosion. The corrosion rate line in Figure 4(c) becomes more dense with the increase of Co content. The increasing trend of corrosion rate is also faster. Figure 4(d) shows the combined effect of Ni and Co on corrosion rate of superalloys. The composition combination of Ni-Co in purple region could effectively inhibit the corrosion.

![](./images/812708902104727553_4.jpg)

Figure 3. One-dimensional partial dependence function of corrosion factors and corrosion rate
(a)Al (b)Mo (c)Ti (d)Ni (e)Co (f)Mn

![](./images/812708902104727553_5.jpg)

Figure 4. Two-dimensional partial dependence function of corrosion factors and corrosion rate(a)time
and Al (b)time and Ni (c)time and Co (d)Ni and Co

## 4. Conclusion
In this study, gas hot-corrosion tests of GH3625, GH2132, GH605, GH3536, and GH4738 were carried out, and the corrosion rates at 25h, 50h, 75h, and 100h were calculated by the weight loss method.

Gradient boosting regression tree was used to analyze the relationship between the chemical compositions and corrosion rates. From the analysis of the predicted value and the real value, the evaluation of predictive effects was obtained. GBRT results led to a good understanding of the effect of each factor on the corrosion rate. The significance of superalloy elements was evaluated using feature importance function. The separate effects and co-effects on the important factors was calculated by partial dependent function. The elements of Mn, Co had a great negative influence on the corrosion rate of superalloys in this study while Al, Ni, Ti and Mo were shown to have a positive effect.

This study provides a reference for the selection and protection of aeroengine superalloys. However, it should be noted that this part of the analysis only for the five superalloys under the experimental conditions in this paper, different test conditions could affect the alloy composition of the thermal corrosion resistance. Therefore, more empirical data are needed for future research to explain. Due to the lack of corrosion process data in the test, further research is needed. The conclusions of this paper need to be proved through verification experiments in the future research.

## Acknowledgments
Thanks for the technical guidance provided by School of Reliability and Systems Engineering in Beihang University and experimental guidance by Engineer ShaoYue.

## References
[1] [Dong J X, Li L H, Li H Y,Zhang M C and Yao Z H 2015 Effect of extent of homogenization on the hot deformation recrystallization of superalloy ingot in cogging process. *Mater. Lett.* **51** 1207-1218

[2] Zhou C, Zhang Q and Yao L I 2013 Thermal shock behavior of nanostructured and microstructured thermal barrier coatings on a Fe-based alloy *Acta Metall. Sinica.* **217** 70 - 75

[3] Yang H, Dong L, Zhu X, Yang Y, Wang J and Wang H 2018 Effect of rolling passes on thermal parameters and microstructure evolution via ring-rolling process of GH4738 superalloy *Surf. Coat. Technol.* **1** 1-10

[4] Deb D, Iyer S R and Radhakrishnan V M 1996 A comparative study of oxidation and hot corrosion of a cast nickel base superalloy in different corrosive environments *Mater. Lett.* **29** 19-23

[5] Fang S F, Wang M P, Qi W H and Zheng F 2009 Hybrid genetic algorithms and support vector regression in forecasting atmospheric corrosion of metallic materials *Comput. Mater. Sci.* **44** 647-655

[6] Chou J S, Ngo N T and Chong W K 2017 The use of artificial intelligence combiners for modeling steel pitting risk and corrosion rate *Eng. Appl. Artif. Intell.* **65** 471-483

[7] Vafakhah M 2012 Application of artificial neural networks and adaptive neuro-fuzzy inference system models to short-term streamflow forecasting *Can. J. Civ. Eng.* **39** 402-414

[8] Warnes B M, Pettit F S and Meier G H 2002 Hot-corrosion resistance of Ni-Cr-Al-Y and Ni-18% Si alloys in sulfate eutectic and sulfate plus vanadate melts at 973K *Oxid. Met.* **58** 487-498.

[9] Raffaitin A, Crabos F, Andrieu E and Monceau D 2006 Advanced burner-rig test for oxidation-corrosion resistance\udevaluation of mcrally/superalloys systems *Surf. Coat. Technol.* **201** 3829-3835.

[10] Friedman J H 2001 Greedy function approximation: a gradient boosting machine *Ann. Stat.* **29** 1189-1232.