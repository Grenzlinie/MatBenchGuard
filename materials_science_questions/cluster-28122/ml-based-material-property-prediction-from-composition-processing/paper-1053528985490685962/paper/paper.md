Article

# Predictive Modeling and Optimization of Layer-Cladded Ti-Al-Nb-Zr High-Entropy Alloys Using Machine Learning

Ruirui Dai $^{1,2}$, Hua Guo $^{3}$, Jianying Liu $^{4}$, Marco Alfano $^{5,6}$ , Junfeng Yuan $^{1,2}$ and Zhiqiang Zhao $^{1,7,*}$

1 Shandong Provincial Geo-Mineral Engineering Exploration Institute (801 Institute of Hydrogeology and Engineering Geology), Shandong Provincial Bureau of Geology & Mineral Resources, Jinan 250014, China; tb23050002a41ld@cumt.edu.cn (R.D.); yuanjfacademiao@outlook.com (J.Y.)
2 School of Mechatronics Engineering, China University of Mining and Technology, Xuzhou 221116, China
3 China Aero Geophysical Survey and Remote Sensing Center for Natural Resources, Beijing 100083, China; hyguohua@126.com
4 Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100094, China; liujy201787@aircas.ac.cn
5 Dipartimento di Scienze e Metodi dell'Ingegneria, Università di Modena e Reggio Emilia, Via Amendola 2, 42122 Reggio Emilia, Italy; marco.alfano@unimore.it
6 Department of Mechanical and Mechatronics Engineering, University of Waterloo, 200 University Avenue West, Waterloo, ON N2L 3G1, Canada
7 Key Laboratory of Geological Disaster Risk Prevention and Control, Emergency Management Department of Shandong Province, Jinan 250014, China
* Correspondence: dkj801xzbgs@shandong.cn; Tel.: +86-13969117324

Abstract: In this work, the influence of laser power (LP), scanning speed (SS), and powder feeding speed (PF) on the porosity, dilution, and microhardness of lightweight refractory high-entropy alloy (RHEA) coatings produced via laser cladding (LC) was investigated. Variance analysis (ANOVA) was deployed to ascertain the effect of LP, SS, and PF on performance metrics such as porosity, dilution, and microhardness. The Non-dominated Sorting Genetic Algorithm II (NSGA-II) was then applied to optimize these processing parameters to minimize porosity, achieve suitable dilution, and maximize microhardness, enhancing the mechanical properties of RHEA coatings. Finally, machine learning models-Random Forest (RF), Gradient Boosting Decision Tree (GBDT), and Genetic Algorithm-enhanced GBDT (GA-GBDT)-were developed using orthogonal experimental data, with GA-GBDT demonstrating superior predictive accuracy. The proposed approach integrates statistical analysis and advanced ML techniques, providing a better understanding into optimizing LP, SS, and PF for improved RHEA coatings performance in industrial applications, thereby advancing laser cladding technology.

Keywords: lightweight; refractory; high-entropy alloy; laser cladding; multi-objective optimization; GA-GBDT

## 1. Introduction

Refractory high-entropy alloys (RHEAs) featuring high-melting-point elements, such as Mo, Nb, Hf, Ta, Cr, W, and Zr, promise to replace the nickel-based and cobalt-based high-temperature alloys for shaft, turbine disk, turbine blades of engine in aviation aircraft, marine and gas turbine, etc. [1-3]. For example, NbMoTaW, NbMoTaWV [4], and TaNbH-fZrTi [5] possess relatively high strengths above the limiting temperature (1473 K) of the conventional nickel-based high-temperature alloys.

Nonetheless, the development of refractory high-entropy alloys has been limited owing to their high density and poor low room-temperature toughness. The addition of low-density elements (e.g., Ti, Al, Mg, and Li, etc.) and the ratio adjustment of constituent elements have been suggested to alleviate the above problems in RHEAs [6-8]. Therefore, lightweight RHEAs with densities lower than $7\ \text{g/cm}^3$, such as AlNbTiV [8],

![](./images/1053528985490685962_1.jpg)

Citation: Dai, R.; Guo, H.; Liu, J.; Alfano, M.; Yuan, J.; Zhao, Z.
Predictive Modeling and
Optimization of Layer-Cladded
Ti-Al-Nb-Zr High-Entropy Alloys
Using Machine Learning. Coatings
2024, 14, 1319. https://doi.org/
10.3390/coatings14101319

Academic Editor: Frederic Sanchette

Received: 30 August 2024
Revised: 23 September 2024
Accepted: 25 September 2024
Published: 16 October 2024

![](./images/1053528985490685962_2.jpg)

Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

Coatings 2024, 14, 1319. https://doi.org/10.3390/coatings14101319  https://www.mdpi.com/journal/coatings

AlₓNbTiVZr [9], and AlNbTiZr [10], were recently investigated in order to achieve excellent strength in high-temperature environments as well as superior room-temperature toughness.

Laser cladding (LC), i.e., an advanced manufacturing technology, has the advantages of fostering a strong metallurgical bond strength, a concentrated energy density, a high processing precision, and a wide choice of elemental materials [11,12]. As such, lightweight RHEA coatings produced by the LC can reduce the high cost of bulk alloys, overcome size and thickness limitations, and may allow the selection of many elemental materials [13,14]. It is noteworthy that RHEA coatings prepared by the LC are often affected by high dilution and porosity rates (unmelted particles), which are attributed to the high melting points of the composing elements as well as their large differences in melting points. On the one hand, the large dilution rates are generated by the overmixing of powder and matrix, which can affect coating properties, such as microhardness, abrasion resistance, and corrosion resistance [15]. On the other hand, owing to the variance in melting points among constituent elements, those with high melting points may remain unmelted, while high energy can lead to the disappearance of low-melting-point elements within the melt pool [16]. In both scenarios, the resulting mechanical properties are negatively affected. As a consequence, a current challenge lies in optimizing the LC process parameters, specifically laser power (LP), scanning speed (SS), and powder feeding speed (PF), to overcome issues of high dilution and porosity rates observed in lightweight RHEA coatings [16,17].

Usually, the optimization of process parameters commences with the design of experiments (DoE) within a matrix representing the design space, where LP, SS, and PF serve as the primary variables. The optimal design space is subsequently refined through iterative experimentation, including visual and macroscopic inspections, as well as mechanical testing. Empirical-regression modeling is then applied to derive insights from these experiments. Successful applications of statistical analysis methods, illustrating the relationships between input and output parameters and facilitating the establishment of a comprehensive process map, have been previously documented by the authors of this work [18,19] and others [16,20]. However, it is essential to note that there are limitations to their adaptability in handling complex and non-linear relationships within intricate datasets.

Machine learning (ML) methods offer a versatile approach, autonomously learning patterns and making predictions without explicit programming [21,22]. Those could serve as a complementary or alternative means of optimizing process parameters, particularly in situations where relationships are highly complex and challenging to capture solely through traditional empirical methods. In contrast to empirical-regression models, which depend on predefined mathematical relationships, ML algorithms can identify hidden patterns and non-linear correlations within the data, potentially resulting in more accurate predictions. Additionally, machine learning techniques, including supervised and unsupervised learning [23,24], enable the exploration of complex interactions among numerous variables simultaneously. Previous research efforts, such as those by Masayuki et al. [25], Xu et al. [26], and He et al. [27], showcase the successful application of machine learning algorithms, specifically Random Forest (RF), AdaBoost, Support Vector Machines (SVM), and hybrid Genetic Algorithm and Ant Colony Optimization (GA-ACO-RFR), in predicting and optimizing various material and process-related parameters. Considering these successes, there is a notable opportunity to leverage machine learning algorithms to address the challenges associated with high dilution and porosity rates in lightweight RHEA coatings produced by the LC process.

Therefore, the primary objective of this study is to formulate predictive models for the porosity, dilution, and microhardness of laser-cladded Ti-Al-Nb-Zr high-entropy alloy coatings to achieve outstanding mechanical properties. Firstly, the orthogonal experimental design is used to generate suitable output data for subsequent ML algorithms. Variance analysis (ANOVA) is used to quantify the contribution of the processing parameters (LP, SS, PF) to the porosity, dilution, and microhardness of the coatings. Subsequently, the Non-dominated Sorting Genetic Algorithm II (NSGA-II) is employed to obtain the optimal

processing parameters for achieving minimum porosity, suitable dilution, and maximum microhardness. Finally, the Random Forest (RF), Gradient Boosting Decision Tree (GBDT), and Genetic Algorithm-enhanced Gradient Boosting Decision Tree (GA-GBDT) are utilized and compared to select the most suitable model for boosting prediction accuracy. The proposed approach integrates statistical analysis and advanced ML techniques, enhancing understanding into the optimization of LP, SS, and PF for improved RHEA coating performance in industrial applications, thereby advancing laser cladding technology of lightweight RHEA coatings.

## 2. Materials and Methods
### 2.1. Laser Cladding Experiments

Commercially available raw Al, Ti, and Nb spheroidal powders with particle sizes of about 75-150 $\mu$m, and Zr irregular powder with particle sizes of 50-75 $\mu$m (purity > 99.9%), were used. Powders were combined into Ti-Al-Nb-Zr (2:0.5:1:1) and then stirred using a vacuum ball mill (YXQM-2L, MITR, Changsha, China) for 2 h at 85 rev/min. The mass ratio of grinding balls to powder was 2:1. The coatings were subsequently prepared using a fiber laser system (RFL-C3000W, Raycus, Wuhan, China). The whole experimental setup is depicted in Figure 1.

![](./images/1053528985490685962_3.jpg)

Figure 1. (a) Experimental setup employed for the laser cladding experiments; (b) schematic of the laser head and the resulting deposition process.

A single-pass cladding layer was deposited under the protection of high-purity argon gas onto titanium alloy (Ti6Al4V) specimens with dimensions of $100 \times 100 \times 10$ mm³. Prior to the deposition process, the specimens were ground with sandpaper to reduce surface laser reflection, followed by cleaning with alcohol to remove residual oils and impurities. The substrate was preheated at 200 °C in order to reduce the crack sensitivity of the substrate and to improve the microstructure and mechanical properties of the coating. Based on initial experiments within a broader processing range, orthogonal experiments involving three factors and five levels (Taguchi L25 orthogonal array), as outlined in Table 1, were devised. After that, machine learning (ML) algorithms were employed for multi-response objective optimization.

<table>
<caption>Table 1. Processing variables and their levels used in factorial laser cladding experiments.</caption>
<thead>
  <tr>
    <th>Parameters</th>
    <th>Level 1</th>
    <th>Level 2</th>
    <th>Level 3</th>
    <th>Level 4</th>
    <th>Level 5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td>−2</td>
    <td>−1</td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>LP (W)</td>
    <td>1800</td>
    <td>2000</td>
    <td>2200</td>
    <td>2400</td>
    <td>2600</td>
  </tr>
  <tr>
    <td>SS (mm/s)</td>
    <td>2.5</td>
    <td>3</td>
    <td>3.5</td>
    <td>4</td>
    <td>4.5</td>
  </tr>
  <tr>
    <td>PF (g/min)</td>
    <td>0.8</td>
    <td>0.9</td>
    <td>1</td>
    <td>1.1</td>
    <td>1.2</td>
  </tr>
  <tr>
    <td>Spot diameter (mm)</td>
    <td></td>
    <td></td>
    <td>2.5</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Defocus distance (mm)</td>
    <td></td>
    <td></td>
    <td>+13</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Argon flow rate (L/min)</td>
    <td></td>
    <td></td>
    <td>5</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Preheating temperature (°C)</td>
    <td></td>
    <td></td>
    <td>200</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

### 2.2. Performance Metrics of Cladded Layers

Following processing, the coatings were cut down to $15 \times 10 \times 10\ \text{mm}^3$ specimens by using a wire-EDM machine (Wire-EDM, GF, Schaffhausen, Switzerland), and their cross-sections were ground (400#–3000# sandpaper) and polished to a mirror finish. The morphology of the 25 groups of coatings was imaged using a 3D digital microscope (DSX10-SZH, OLYMPUS, Shanghai, China) and the results are illustrated in Figure 2. The porosity rate (P) and dilution rate (D), that were chosen as key geometric characteristics, were determined as:

$$
\mathrm{P} = \frac{\mathrm{A}3}{\mathrm{A}1 + \mathrm{A}2} \times 100\% \tag{1}
$$

$$
\mathrm{D} = \frac{\mathrm{A}2}{\mathrm{A}1 + \mathrm{A}2} \times 100\% \tag{2}
$$

where A1 is the area of the reinforcement (i.e., additional material that builds up on the surface of the substrate), A2 is the area of weld penetration (i.e., depth or extent to which the cladding or welding material fuses into the substrate material), and A3 is the area occupied by unmelted particles. The area A1, A2, and A3 were measured using ImageJ2 software (Version 1.54k) from cross-sectional views of the weld seam, such that reported in Figure 2a. Besides, the cross-sections of all experimental combinations are provided in Figure 2b.

![](./images/1053528985490685962_4.jpg)

Figure 2. (a) Typical appearance of the weld seam along with a cross-sectional view highlighting the areas measured to extract porosity and dilution. (b) Cross-sectional views of all specimens obtained from the orthogonal experiments. A total of 25 specimens were considered (S1–S25).

The microhardness of the coatings was determined using a microhardness tester (HVSA-1000, WHW, Shanghai, China) with a 300 g load applied for 15 s. Measurement points were selected at $200\ \mu\text{m}$ intervals from the top to the bottom of the coatings. The porosity, dilution, and microhardness for 25 sets of experiments are provided in Table 2. Additionally, the microstructure and elemental composition of the coatings were analyzed using a field emission scanning electron microscope (SEM, FEI Quanta 250, Hillsboro, OR, USA) equipped with an energy dispersive spectrometer (EDS). The phase composition of the coatings was also investigated using an X-ray diffractometer (Bruker D8 Advanced, Karlsruhe, Germany).

Table 2. Performance metrics as obtained in factorial laser cladding experiments.

<table>
<thead>
  <tr>
    <th>Sample</th>
    <th>LP<br>(W)</th>
    <th>SS<br>(mm/s)</th>
    <th>PF<br>(g/min)</th>
    <th>P<br>(%)</th>
    <th>D<br>(%)</th>
    <th>Microhardness<br>(HV<sub>0.3</sub>)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>S1</td>
    <td>1800</td>
    <td>2.5</td>
    <td>08</td>
    <td>0.86</td>
    <td>33.66</td>
    <td>523.25 $\pm$ 21.41</td>
  </tr>
  <tr>
    <td>S2</td>
    <td>1800</td>
    <td>3</td>
    <td>0.9</td>
    <td>8.09</td>
    <td>39.40</td>
    <td>475.16 $\pm$ 20.05</td>
  </tr>
  <tr>
    <td>S3</td>
    <td>1800</td>
    <td>3.5</td>
    <td>1</td>
    <td>2.49</td>
    <td>32.99</td>
    <td>547.18 $\pm$ 42.76</td>
  </tr>
  <tr>
    <td>S4</td>
    <td>1800</td>
    <td>4</td>
    <td>1.1</td>
    <td>7.64</td>
    <td>42.61</td>
    <td>431.74 $\pm$ 22.00</td>
  </tr>
  <tr>
    <td>S5</td>
    <td>1800</td>
    <td>4.5</td>
    <td>1.2</td>
    <td>6.26</td>
    <td>59.59</td>
    <td>441.79 $\pm$ 22.62</td>
  </tr>
  <tr>
    <td>S6</td>
    <td>2000</td>
    <td>2.5</td>
    <td>0.9</td>
    <td>4.72</td>
    <td>27.42</td>
    <td>518.84 $\pm$ 56.04</td>
  </tr>
  <tr>
    <td>S7</td>
    <td>2000</td>
    <td>3</td>
    <td>1</td>
    <td>4.53</td>
    <td>30.28</td>
    <td>593.94 $\pm$ 57.47</td>
  </tr>
  <tr>
    <td>S8</td>
    <td>2000</td>
    <td>3.5</td>
    <td>1.1</td>
    <td>7.16</td>
    <td>33.99</td>
    <td>448.35 $\pm$ 26.6</td>
  </tr>
  <tr>
    <td>S9</td>
    <td>2000</td>
    <td>4</td>
    <td>1.2</td>
    <td>4.48</td>
    <td>37.52</td>
    <td>537.93 $\pm$ 40.75</td>
  </tr>
  <tr>
    <td>S10</td>
    <td>2000</td>
    <td>4.5</td>
    <td>0.8</td>
    <td>1.38</td>
    <td>51.64</td>
    <td>491.24 $\pm$ 24.65</td>
  </tr>
  <tr>
    <td>S11</td>
    <td>2200</td>
    <td>2.5</td>
    <td>1</td>
    <td>5.91</td>
    <td>28.30</td>
    <td>589.04 $\pm$ 30.72</td>
  </tr>
  <tr>
    <td>S12</td>
    <td>2200</td>
    <td>3</td>
    <td>1.1</td>
    <td>6.89</td>
    <td>30.30</td>
    <td>469.61 $\pm$ 56.77</td>
  </tr>
  <tr>
    <td>S13</td>
    <td>2200</td>
    <td>3.5</td>
    <td>1.2</td>
    <td>8.83</td>
    <td>39.89</td>
    <td>516.51 $\pm$ 32.70</td>
  </tr>
  <tr>
    <td>S14</td>
    <td>2200</td>
    <td>4</td>
    <td>0.8</td>
    <td>4.21</td>
    <td>48.27</td>
    <td>436.73 $\pm$ 27.90</td>
  </tr>
  <tr>
    <td>S15</td>
    <td>2200</td>
    <td>4.5</td>
    <td>0.9</td>
    <td>8.47</td>
    <td>55.74</td>
    <td>428.51 $\pm$ 25.12</td>
  </tr>
  <tr>
    <td>S16</td>
    <td>2400</td>
    <td>2.5</td>
    <td>1.1</td>
    <td>2.45</td>
    <td>46.84</td>
    <td>563.14 $\pm$ 39.59</td>
  </tr>
  <tr>
    <td>S17</td>
    <td>2400</td>
    <td>3</td>
    <td>1.2</td>
    <td>0.86</td>
    <td>60.43</td>
    <td>400.94 $\pm$ 31.12</td>
  </tr>
  <tr>
    <td>S18</td>
    <td>2400</td>
    <td>3.5</td>
    <td>0.8</td>
    <td>1.61</td>
    <td>53.83</td>
    <td>401.86 $\pm$ 20.46</td>
  </tr>
  <tr>
    <td>S19</td>
    <td>2400</td>
    <td>4</td>
    <td>0.9</td>
    <td>2.71</td>
    <td>57.92</td>
    <td>402.17 $\pm$ 41.19</td>
  </tr>
  <tr>
    <td>S20</td>
    <td>2400</td>
    <td>4.5</td>
    <td>1</td>
    <td>2.88</td>
    <td>50.64</td>
    <td>604.1 $\pm$ 31.07</td>
  </tr>
  <tr>
    <td>S21</td>
    <td>2600</td>
    <td>2.5</td>
    <td>1.2</td>
    <td>2.87</td>
    <td>24.09</td>
    <td>603.45 $\pm$ 21.05</td>
  </tr>
  <tr>
    <td>S22</td>
    <td>2600</td>
    <td>3</td>
    <td>0.8</td>
    <td>5.19</td>
    <td>51.51</td>
    <td>476.39 $\pm$ 45.28</td>
  </tr>
  <tr>
    <td>S23</td>
    <td>2600</td>
    <td>3.5</td>
    <td>0.9</td>
    <td>3.37</td>
    <td>55.69</td>
    <td>434.73 $\pm$ 13.53</td>
  </tr>
  <tr>
    <td>S24</td>
    <td>2600</td>
    <td>4</td>
    <td>1</td>
    <td>2.77</td>
    <td>54.55</td>
    <td>430.73 $\pm$ 18.73</td>
  </tr>
  <tr>
    <td>S25</td>
    <td>2600</td>
    <td>4.5</td>
    <td>1.1</td>
    <td>3.72</td>
    <td>40.97</td>
    <td>514.16 $\pm$ 9.07</td>
  </tr>
</tbody>
</table>

### 2.3. Analysis of Variance (ANOVA)

Analysis of Variance (ANOVA) [27] is used to test the significance of differences between the means of two or more samples. It allows the analysis of the impact of different factors on data variation and identifies which factors significantly influence this variation. ANOVA was employed to quantitatively evaluate the contribution of laser cladding processing parameters to the porosity, dilution, and microhardness of the coatings [28]. Furthermore, to achieve coatings with superior mechanical properties, we employed the NSGA-II (Non-dominated Sorting Genetic Algorithm Second Generation) multi-objective optimization algorithm with targets of minimal porosity, maximum microhardness, and an appropriate dilution rate of about 25%. The basic principles of the NSGA-II algorithm are as follows:

1.  An initial population Pt of size N is randomly generated. This population undergoes non-dominated sorting, selection, crossover, and mutation to produce an offspring population Qt. The two populations are then combined to form a population Rt of size 2N.

2.  Fast non-dominated sorting is performed, and the crowding degree is calculated for each individual in the non-dominated layers. Based on non-dominated relationships

and crowding degrees, appropriate individuals are selected to form a new parent population Pt + 1.

3. A new offspring population Qt + 1 is generated through the basic operations of the genetic algorithm. Pt + 1 is merged with Qt + 1 to form a new population Rt + 1. These operations are repeated until the termination conditions are met.

### 2.4. Machine Learning Algorithms
The present investigation employed machine learning algorithms—Random Forests, Gradient Boosting Decision Trees, and a Genetic Algorithm—to predict performance metrics including dilution, porosity, and microhardness of laser-cladded coatings. The analysis aims to correlate the aforementioned metrics with key processing parameters, such as powder feed rate, laser power, and scanning speed.

#### 2.4.1. Random Forest (RF)
Random Forest (RF), initially proposed by Breiman [29], is an ensemble learning algorithm that leverages decision trees and operates under the Bagging (Bootstrap Aggregating) model [30]. The RF model constructs a multitude of decision trees by repeatedly sampling from the training dataset with a replacement, as illustrated in Figure 3. Each decision tree within the ensemble is trained on a subset of the main dataset, which comprises various combinations of processing parameters (independent variables) and corresponding performance metrics (dependent variables).

![](./images/1053528985490685962_5.jpg)

Figure 3. Illustration of the Random Forest (RF) ensemble learning process, showing the creation of multiple decision trees through Bootstrap sampling and feature randomization.

Node classification in RF is essential for its predictive power, achieved through the process of maximizing information gain. At each node of the decision tree, a subset of features (such as coating porosity, dilution, and hardness) is randomly selected to determine the best split. This randomness ensures that each tree in the ensemble captures different aspects of the data, reducing variance and enhancing the model's generalization capability across diverse datasets.

During both the training and prediction phases, RF combines predictions from multiple decision trees in its ensemble approach. For classification tasks, RF aggregates predictions through majority voting, where the predicted class is determined by the most frequent prediction among all trees. Conversely, in regression tasks, RF averages predictions across the ensemble, providing a robust estimate of the target variable (e.g., porosity, dilution, and hardness).

The ensemble nature of RF contributes significantly to its effectiveness. By leveraging the diversity among constituent trees, RF not only enhances prediction accuracy but also mitigates the risk of overfitting. Each decision tree's independence and the variability introduced through Bootstrap sampling ensure that the RF model remains robust and adaptable to different datasets and input parameters [31].

### 2.4.2. Gradient Boosting Decision Trees (GBDT)
Gradient Boosting Decision Trees (GBDT) is a powerful ensemble learning method that sequentially builds an ensemble of weak learners, typically decision trees, to minimize a predefined loss function over a training dataset. The objective is to use an iterative procedure to improve predictions by focusing on the residuals of the previous models. The algorithm begins with an initial prediction $F_0(x)$, and through iterations it adds new trees $h_m(x)$ to refine the initial prediction:

$$
\mathrm{F}_{\mathrm{m}}(\mathrm{x})=\mathrm{F}_{\mathrm{m}-1}(\mathrm{x})+\eta \mathrm{h}_{\mathrm{m}}(\mathrm{x}) \tag{3}
$$

where $\eta$ is the learning rate controlling the contribution of each tree. At each iteration, the new tree $h_m(x)$ is trained to minimize the negative gradient of the loss function with respect to the current ensemble prediction $F_{m-1}(x)$:

$$
\mathrm{h}_{\mathrm{m}}(\mathrm{x})=\underset{\mathrm{h}}{\operatorname{argmin}} \sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{L}\left(\mathrm{y}_{\mathrm{i}}, \mathrm{F}_{\mathrm{m}-1}\left(\mathrm{x}_{\mathrm{i}}\right)+\mathrm{h}\left(\mathrm{x}_{\mathrm{i}}\right)\right) \tag{4}
$$

This process involves performing gradient descent in the function space of potential weak learners h(x). The negative gradient, i.e., the derivative of the loss function L with respect to $F(x_i)$, can be expressed as:

$$
\left.\nabla_{\mathrm{F}(\mathrm{x})} \mathrm{L}\left(\mathrm{y}_{\mathrm{i}}, \mathrm{F}\left(\mathrm{x}_{\mathrm{i}}\right)\right)\right|_{\mathrm{F}(\mathrm{x})=\mathrm{F}_{\mathrm{m}-1}(\mathrm{x})}=-\left.\frac{\partial \mathrm{L}\left(\mathrm{y}_{\mathrm{i}}, \mathrm{F}\left(\mathrm{x}_{\mathrm{i}}\right)\right)}{\partial \mathrm{F}\left(\mathrm{x}_{\mathrm{i}}\right)}\right|_{\mathrm{F}(\mathrm{x})=\mathrm{F}_{\mathrm{m}-1}(\mathrm{x})} \tag{5}
$$

This gradient provides the direction and magnitude of the error that needs to be corrected by the new tree $h_m(x)$. Decision trees are employed as weak learners due to their capability to partition the feature space effectively, accommodating continuous variables inherent in many practical applications. The prediction at each stage aggregates the contributions of all previous trees scaled by $\eta$:

$$
\hat{\mathrm{y}}(\mathrm{x})=\sum_{\mathrm{m}=1}^{\mathrm{M}} \eta \mathrm{h}_{\mathrm{m}}(\mathrm{x}) \tag{6}
$$

GBDT's sequential approach ensures that each new tree corrects errors made by the ensemble up to that point, enhancing the model's predictive accuracy. A schematic flowchart is provided in Figure 4. Regularization techniques, such as limiting tree depth and adjusting the learning rate $\eta$, are crucial for preventing overfitting and improving generalization. This

methodology leverages gradient descent to optimize in an iterative manner the ensemble of decision trees, making it effective in capturing complex relationships between inputs and outputs in regression and classification tasks across various domains.

![](./images/1053528985490685962_6.jpg)

Figure 4. Schematic flowchart of the Gradient Boosting Decision Trees (GBDT) algorithm.

### 2.4.3. Decision Tree Boosting Model Based on the Genetic Algorithm (GA-GBDT)

Holland [32] introduced the Genetic Algorithm (GA) to find optimal solutions by emulating natural selection and inheritance mechanisms. Genetic Algorithms consist of five main components: encoding and decoding, population initialization, fitness function, genetic operators (including selection, crossover, and mutation), and genetic parameter settings (such as population size and the probabilities of genetic operators).

As illustrated in Figure 5, the GA process begins with the calculation of the fitness value for each individual in the initialized population, denoted as P(0). The algorithm then evaluates whether the iteration stop condition is met. If satisfied, the current optimal result is provided in output. If not, the population is updated using genetic operators, including replication, crossover, and mutation, and a new population P(gen) is thus obtained. The iterative process continues until the convergence condition is satisfied.

The GA excels in global search capability, thanks to its ability to automatically retain superior solutions and guide optimization through a probabilistic search mechanism. When high computational accuracy is needed, the GA offers several advantages: good convergence, reduced computation time, high robustness, and ease of integration with other algorithms [33]. Consequently, a decision tree boosting model based on the Genetic Algorithm (GA-GBDT) was developed.

![](./images/1053528985490685962_7.jpg)

Figure 5. Schematic diagram of the Genetic Algorithm principle.

### 2.4.4. Training of the ML Algorithms

To train the machine learning (ML) algorithms, 20 data groups each of porosity, dilution, and microhardness were randomly selected. The fivefold cross-validation method was employed, where the dataset is divided into five subsets. In each iteration, four subsets (80%) are used as the training set, and one subset (20%) is used as the validation set. This process is repeated five times, ensuring each subset is used once as the validation set. This method helps to improve the robustness and generalization of the model, as it allows for multiple rounds of training and validation.

Z-score normalization was employed to convert data with varying magnitudes—such as laser processing (LP), scanning speed (SS), powder feed rate (PF), porosity (P), dilution (D), and microhardness (MH)—into a consistent metric [34]. The normalization process is defined by the equation:

$$
Z = \frac{x - \mu}{\sigma} \tag{7}
$$

where x represents a generic variable (e.g., LP, SS, PF, P, D, or MH), $\mu$ is the mean value of the variable, and $\sigma$ is the standard deviation. This transformation ensures that all variables are scaled to have a mean of 0 and a standard deviation of 1, facilitating comparison across different scales. The normalized data is reported in Table 3.

Table 3. Z-score normalized data for porosity (P), dilution (D), and microhardness (MH) from laser cladding experiments with varied processing variables.

<table>
<thead>
  <tr>
    <th>Sample</th>
    <th>LP</th>
    <th>SS</th>
    <th>PF</th>
    <th>P</th>
    <th>D</th>
    <th>Microhardness</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>S1</td>
    <td>−1.41</td>
    <td>−1.41</td>
    <td>−1.41</td>
    <td>−1.49</td>
    <td>−0.889</td>
    <td>0.53</td>
  </tr>
  <tr>
    <td>S2</td>
    <td>−1.41</td>
    <td>−0.71</td>
    <td>−0.71</td>
    <td>1.54</td>
    <td>−0.372</td>
    <td>−0.18</td>
  </tr>
  <tr>
    <td>S3</td>
    <td>−1.41</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>−0.80</td>
    <td>−0.949</td>
    <td>0.88</td>
  </tr>
  <tr>
    <td>S4</td>
    <td>−1.41</td>
    <td>0.71</td>
    <td>0.71</td>
    <td>1.35</td>
    <td>−0.082</td>
    <td>−0.82</td>
  </tr>
  <tr>
    <td>S5</td>
    <td>−1.41</td>
    <td>1.41</td>
    <td>1.41</td>
    <td>0.77</td>
    <td>1.447</td>
    <td>−0.67</td>
  </tr>
  <tr>
    <td>S6</td>
    <td>−0.71</td>
    <td>−1.41</td>
    <td>−0.71</td>
    <td>0.12</td>
    <td>−1.451</td>
    <td>0.46</td>
  </tr>
  <tr>
    <td>S7</td>
    <td>−0.71</td>
    <td>−0.71</td>
    <td>0.00</td>
    <td>0.05</td>
    <td>−1.193</td>
    <td>1.58</td>
  </tr>
  <tr>
    <td>S8</td>
    <td>−0.71</td>
    <td>0.00</td>
    <td>0.71</td>
    <td>1.15</td>
    <td>−0.858</td>
    <td>−0.58</td>
  </tr>
  <tr>
    <td>S9</td>
    <td>−0.71</td>
    <td>0.71</td>
    <td>1.41</td>
    <td>0.02</td>
    <td>−0.541</td>
    <td>0.75</td>
  </tr>
  <tr>
    <td>S10</td>
    <td>−0.71</td>
    <td>1.41</td>
    <td>−1.41</td>
    <td>−1.27</td>
    <td>0.732</td>
    <td>0.05</td>
  </tr>
  <tr>
    <td>S11</td>
    <td>0.00</td>
    <td>−1.41</td>
    <td>0.00</td>
    <td>0.62</td>
    <td>−1.371</td>
    <td>1.51</td>
  </tr>
  <tr>
    <td>S12</td>
    <td>0.00</td>
    <td>−0.71</td>
    <td>0.71</td>
    <td>1.04</td>
    <td>−1.191</td>
    <td>−0.03</td>
  </tr>
  <tr>
    <td>S13</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>1.41</td>
    <td>1.85</td>
    <td>−0.326</td>
    <td>−1.27</td>
  </tr>
  <tr>
    <td>S14</td>
    <td>0.00</td>
    <td>0.71</td>
    <td>−1.41</td>
    <td>−0.08</td>
    <td>0.427</td>
    <td>−0.75</td>
  </tr>
  <tr>
    <td>S15</td>
    <td>0.00</td>
    <td>1.41</td>
    <td>−0.71</td>
    <td>1.70</td>
    <td>1.100</td>
    <td>−0.87</td>
  </tr>
  <tr>
    <td>S16</td>
    <td>0.71</td>
    <td>−1.41</td>
    <td>0.71</td>
    <td>−0.86</td>
    <td>0.299</td>
    <td>1.12</td>
  </tr>
  <tr>
    <td>S17</td>
    <td>0.71</td>
    <td>−0.71</td>
    <td>1.41</td>
    <td>−1.49</td>
    <td>1.523</td>
    <td>−1.28</td>
  </tr>
  <tr>
    <td>S18</td>
    <td>0.71</td>
    <td>0.00</td>
    <td>−1.41</td>
    <td>−1.17</td>
    <td>0.928</td>
    <td>−1.27</td>
  </tr>
  <tr>
    <td>S19</td>
    <td>0.71</td>
    <td>0.71</td>
    <td>−0.71</td>
    <td>−0.71</td>
    <td>1.297</td>
    <td>−1.26</td>
  </tr>
  <tr>
    <td>S20</td>
    <td>0.71</td>
    <td>1.41</td>
    <td>0.00</td>
    <td>−0.64</td>
    <td>0.641</td>
    <td>1.73</td>
  </tr>
  <tr>
    <td>S21</td>
    <td>1.41</td>
    <td>−1.41</td>
    <td>1.41</td>
    <td>−0.64</td>
    <td>−1.751</td>
    <td>1.78</td>
  </tr>
  <tr>
    <td>S22</td>
    <td>1.41</td>
    <td>−0.71</td>
    <td>−1.41</td>
    <td>0.32</td>
    <td>0.719</td>
    <td>−0.16</td>
  </tr>
  <tr>
    <td>S23</td>
    <td>1.41</td>
    <td>0.00</td>
    <td>−0.71</td>
    <td>−0.43</td>
    <td>1.095</td>
    <td>−0.78</td>
  </tr>
  <tr>
    <td>S24</td>
    <td>1.41</td>
    <td>0.71</td>
    <td>0.00</td>
    <td>−0.69</td>
    <td>0.993</td>
    <td>−0.84</td>
  </tr>
  <tr>
    <td>S25</td>
    <td>1.41</td>
    <td>1.41</td>
    <td>0.71</td>
    <td>−0.29</td>
    <td>−0.230</td>
    <td>0.39</td>
  </tr>
</tbody>
</table>

A comprehensive assessment of predictive accuracy of the various algorithms was carried out using four metrics, i.e., mean absolute error (MAE), root mean square error (RMSE), and the coefficient of determination ($R^2$). The corresponding equations are given below:

$$
\mathrm{MAE}=\frac{\sum_{\mathrm{i}=1}^{\mathrm{n}}\left|\hat{\mathrm{x}}_{\mathrm{i}}-\mathrm{x}_{\mathrm{i}}\right|}{\mathrm{n}} \tag{8}
$$

$$
\mathrm{RMSE}=\sqrt{\frac{\sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\hat{\mathrm{x}}_{\mathrm{i}}\right)^{2}}{\mathrm{n}}} \tag{9}
$$

$$
\mathrm{R}^{2}=1-\frac{\sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\hat{\mathrm{x}}_{\mathrm{i}}\right)^{2}}{\sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\overline{\hat{\mathrm{x}}}_{\mathrm{i}}\right)^{2}} \tag{10}
$$

In these equations, $x_i$ represents the experimental value, $\hat{x}$ is the model predicted value, $\hat{x}$ is the average of the predicted values, and n is the number of specimens (20). The MAE measures the average magnitude of the errors between predicted and actual values; therefore, lower MAE indicates that the predictions are closer to the actual values, providing a straightforward interpretation of prediction accuracy. RMSE penalizes larger errors more than MAE, giving a higher weight to larger deviations and providing a more sensitive measure of prediction accuracy. Thus, lower RMSE indicates better predictive accuracy, with fewer large errors. Relative error ($\delta$) expresses the prediction error as a percentage, offering a normalized view of error magnitude relative to the actual values. Finally, $R^2$ indicates the proportion of variance in the dependent variable that is predictable

from the independent variables, with values closer to 1 meaning better model performance.
The value ranges from 0 to 1, where 1 indicates perfect prediction.

## 3. Results and Discussion
### 3.1. Optimization of the Laser Cladding Process
#### 3.1.1. ANOVA Results and Coating Optimization Using the NSGA-II Algorithm

The analysis of variance (ANOVA) was used to analyze the significance of the processing parameters (LP, SS, PF) on the coatings' porosity, dilution, and microhardness. By identifying the most influential parameters, we aim to fine-tune the laser cladding process to achieve coatings with enhanced performance. The p-value was used, whereas a value less than 0.05 indicates a significant effect [35]. This threshold is commonly accepted in statistical analyses, and when the p-value is below this cutoff, the results are considered statistically significant, implying a high level of confidence in the observed relationships.

The results are summarized in Table 4 and indicate that LP, SS, and PF contributed 61.42%, 8.37%, and 30.21% to coating porosity, respectively, with LP having the most significant impact. This suggests that the LP is the dominant factor influencing the porosity of the coating. In contrast, SS and PF have relatively minor contributions, indicating that adjustments in these parameters would have a less pronounced effect on porosity. For coating dilution, SS was the primary factor at 47.05%, followed by LP at 37.89% and PF at 15.05%. This distribution shows that SS plays a crucial role in determining the extent of coating dilution, which is important for achieving the desired thickness. LP also significantly affects dilution, albeit to a lesser extent than SS, while the impact of PF appears to be minimal, thereby suggesting that fine-tuning SS and LP is more effective for controlling dilution. In terms of coating microhardness, LP, SS, and PF contributed 7.47%, 49.69%, and 42.84%, respectively, with SS having the greatest influence. The high contribution of SS suggests that it is the most critical factor in determining the hardness, which is essential for ensuring the durability and wear resistance of the coated material. PF also has a substantial impact, implying that both SS and PF need to be optimized to enhance the microhardness, whereas LP plays a relatively minor role in this regard.

<table>
<caption>Table 4. Analysis of variance (ANOVA) results for the selected coating's performance metrics (P, D, MH).</caption>
<thead>
<tr>
<th>Objective</th>
<th>Factor</th>
<th>Adj-SS</th>
<th>Adj-MS</th>
<th>F-Value</th>
<th><i>p</i>-Value</th>
<th>Contribution</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">P</td>
<td>LP</td>
<td>62.35</td>
<td>15.58</td>
<td>4.63</td>
<td>0.01</td>
<td>61.42%</td>
</tr>
<tr>
<td>SS</td>
<td>8.49</td>
<td>2.12</td>
<td>0.63</td>
<td>0.65</td>
<td>8.37%</td>
</tr>
<tr>
<td>PF</td>
<td>30.65</td>
<td>7.66</td>
<td>2.28</td>
<td>0.12</td>
<td>30.21%</td>
</tr>
<tr>
<td rowspan="3">D</td>
<td>LP</td>
<td>892.10</td>
<td>223.02</td>
<td>3.68</td>
<td>0.03</td>
<td>37.90%</td>
</tr>
<tr>
<td>SS</td>
<td>1107.60</td>
<td>276.90</td>
<td>4.56</td>
<td>0.01</td>
<td>47.05%</td>
</tr>
<tr>
<td>PF</td>
<td>354.30</td>
<td>88.57</td>
<td>1.46</td>
<td>0.27</td>
<td>15.05%</td>
</tr>
<tr>
<td rowspan="3">MH</td>
<td>LP</td>
<td>5334.00</td>
<td>1334</td>
<td>0.47</td>
<td>0.75</td>
<td>7.47%</td>
</tr>
<tr>
<td>SS</td>
<td>35,485.00</td>
<td>8871</td>
<td>3.12</td>
<td>0.05</td>
<td>49.69%</td>
</tr>
<tr>
<td>PF</td>
<td>30,593.00</td>
<td>7648</td>
<td>2.69</td>
<td>0.08</td>
<td>42.84%</td>
</tr>
</tbody>
</table>

In particular, the present study targets the achievement of coatings with superior mechanical properties by focusing on minimal porosity, maximum microhardness, and an appropriate dilution rate (D = 25%) [36]. Minimal porosity is critical for improving the coating's resistance to environmental degradation and mechanical stress. Maximum microhardness ensures the coating's durability and resistance to wear and abrasion, which are vital for extending the life span of the coated material. An appropriate dilution rate of 25% is aimed at achieving a balance between coating adhesion and integrity, ensuring that the coating is sufficiently thick and uniform without compromising its mechanical properties. The optimization process employed the Non-dominated Sorting Genetic Algorithm II (NSGA-II) described earlier [27,35]. The NSGA-II is known for its excellent performance in

handling problems with multiple conflicting objective functions [37]. Here, the objective functions and the processing parameter range are defined as:

$$
\begin{cases}
\min \mathrm{f}_{\mathrm{P}}(\mathrm{LP}, \mathrm{SS}, \mathrm{PF}) \\
\min |\mathrm{f}_{\mathrm{D}}(\mathrm{LP}, \mathrm{SS}, \mathrm{PF})-25 \%| \\
\max \mathrm{f}_{\mathrm{HV}}(\mathrm{LP}, \mathrm{SS}, \mathrm{PF})
\end{cases}
\tag{11}
$$

Subjected to:

$$
\begin{cases}
1800 \mathrm{~W} \leq \mathrm{LP} \leq 2600 \mathrm{~W} \\
2.5 \mathrm{~mm} / \mathrm{s} \leq \mathrm{SS} \leq 4.5 \mathrm{~mm} / \mathrm{s} \\
0.8 \mathrm{~g} / \mathrm{min} \leq \mathrm{PF} \leq 1.2 \mathrm{~g} / \mathrm{min}
\end{cases}
\tag{12}
$$

The multi-objective optimization problem involves finding a set of optimal solutions (i.e., Pareto optimal solution set) representing a suitable trade-off between conflicting objectives. The Pareto set is illustrated in Figure 6, from which we concluded that the optimal processing parameters are as follows: LP = 2384 W, SS = 2.52 mm/s, PF = 1.10 g/min. This involved considering the minimum porosity, maximum microhardness, and appropriate dilution, as summarized in Table 5. Predictions for the porosity, dilution, and microhardness of the coatings were made, resulting in values of 2.76%, 45.27%, and 553.32 HV₀.₃, respectively. Furthermore, the algorithm's optimized parameters closely approximate the experimental data, with errors of 13.11%, 3.35%, and 1.74% for porosity, dilution, and microhardness of the coatings, respectively.

![](./images/1053528985490685962_8.jpg)

Figure 6. The optimized Pareto front of NSGA-II, the Pareto optimal solution selected, and projection of optimal solution to porosity rate and dilution rate.

Table 5. Comparison between predicted and experimental optimal values of processing parameters and performance metrics.

<table>
<thead>
<tr>
<th></th>
<th>LP</th>
<th>SS</th>
<th>PF</th>
<th>P (%)</th>
<th>δₚ</th>
<th>D (%)</th>
<th>δₚ</th>
<th>HV</th>
<th>δₚ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pre-value</td>
<td>2384.78</td>
<td>2.52</td>
<td>1.10</td>
<td>2.76</td>
<td rowspan="2">13.11%</td>
<td>45.27</td>
<td rowspan="2">3.35%</td>
<td>553.32</td>
<td rowspan="2">1.74%</td>
</tr>
<tr>
<td>Exp-value</td>
<td>2400</td>
<td>2.50</td>
<td>1.10</td>
<td>2.44</td>
<td>46.84</td>
<td>563.14</td>
</tr>
</tbody>
</table>

#### 3.1.2. Microstructural Analysis of the Optimized Coating

Detailed microstructural and compositional analyses were carried out to explore the microstructure of the coatings prepared using optimized parameters. SEM cross-sectional views, which are reported in Figure 7, reveal a dense composition with partially unmelted Nb powder (melting point: 2468 K), minimal voids and defects, which suggests

enhanced coating mechanical strength and durability. Besides, Figure 7b highlights coarse equiaxed crystals in the upper region of the molten pool, whereas the middle and bottom regions of the coating exhibit columnar crystals that grow from the bottom upwards. This phenomenon is attributed to the crystal growth direction of the $Al_{0.5}Ti_{2}NbZr$ coating, which is influenced by varying solidification rates and temperature gradients in the melt pool [38,39]. It is also noted that the supercooling degree of the dendrite tip increases in the direction of grain solidification and growth due to the additional melted powder consuming significant energy in the melt pool. Simultaneously, a broader supercooling zone is formed due to Marangoni convection and sedimentation dispersion in the mixing zone generated by the powder under the influence of gravity, leading to the non-uniform nucleation of equiaxial crystals [40]. Conversely, the dendrite tips at the bonding interface exhibit a low supercooling degree, resulting in the formation of columnar crystals. Effective solidification dynamics, influenced by supercooling effects and Marangoni convection, promote a fine-grained microstructure, consistent coating quality, and can ensure uniform mechanical properties and strong adhesion. Finally, line element scanning reveals an even distribution of elements in the coating, with small amounts of Zr and Nb present in the matrix due to matrix dilution. Additionally, the line element scanning indicates an even distribution of elements, crucial for maintaining uniform properties and preventing localized weaknesses.

![](./images/1053528985490685962_9.jpg)

Figure 7. (a) SEM image showing the coating and substrate, with regions selected for higher-magnification imaging presented in (b-d). (e) EDS line spectra of the coating and substrate taken along the dashed line indicated in (a).

Figure 8 displays the high-magnification SEM and EDS images of the coating. The presence of subtle microscopic segregation in the coatings is evident through elemental maps and point elemental analysis reported in Figure 8a,b. This microscopic segregation, attributed to melting point differences, has been previously demonstrated in research [41]. Additionally, the dendritic region (DR), characterized by the higher melting points of Nb and Zr (2468 K, 2125 K), solidified initially to form dendritic branches within the melt pool, as indicated by the EDS point analysis in Figure 8b. In contrast, the intergranular region (IR) exhibited lower melting points, primarily Ti and Al (1930 K, 933.4 K). Overall, the microscopic segregation observed in high-magnification SEM and EDS images, with distinct dendritic and intergranular regions, reflects a structured and orderly solidification process typical of well-prepared coatings.

![](./images/1053528985490685962_10.jpg)

Figure 8. (a) SEM image showing the coating, with regions selected for higher-magnification imaging presented in (a1). (b) Elemental distribution maps. (c,d) Elemental content of the points.

### 3.2. Comparative Assessment of the Developed ML Algorithms

To enhance the robustness and effectiveness of the optimization process, AI-based predictive models were integrated into the framework. These models provide a powerful tool for forecasting the effects of varying processing parameters and that can capture complex, non-linear relationships between the parameters and the coating properties. This integration aims to offer improved predictions, which traditional statistical methods alone may not reveal. Therefore, building on the initial analysis presented above, we implemented three machine learning algorithms: Random Forest, Gradient Boosting Decision Tree (GBDT), and Genetic Algorithm-enhanced Gradient Boosting Decision Tree (GA-GBDT). The orthogonal dataset previously used for ANOVA was utilized to train and compare these models. In particular, Figure 9 shows the comparison between the measured values of porosity, dilution, and microhardness and those predicted by developed ML algorithms. The overall analysis of the results suggests a good agreement between prediction and experiments. However, the GA-GBDT demonstrates the closest alignment with experimental values. The genetic optimization algorithm significantly enhances the accuracy of GBDT, particularly for predicting dilution and microhardness. However, the improvement in predicting porosity is less pronounced.

To determine the best-performing model, we compared the evaluation metrics for each performance indicator of coating quality. The comparative data is summarized in Table 6. Overall, the GA-GBDT is the most accurate for predicting porosity. For dilution and microhardness, GA-GBDT outperforms both RF and GBDT across all metrics. Therefore, we concluded that GA-GBDT is the best-performing model, as it consistently achieves lower MAE and RMSE values and higher $R^2$ values, indicating superior accuracy and predictive performance. Consequently, the GA-GBDT algorithm was selected as the optimal prediction model for the porosity, dilution, and microhardness data of the single-pass $Al_{0.5}Ti_2NbZr$ lightweight RHEA coatings. This choice is further supported by the enhanced generalization and robustness of GBDT [37] and the capability of the GA to address complex problems and search for the global optimum [42].

![](./images/1053528985490685962_11.jpg)

Figure 9. Schematic Scatter plot of predicted vs. experimental values of coating porosity, dilution and microhardness values by the RF, GBDT and GA-GBDT.

<table>
<thead>
<tr><th rowspan="2">Model</th><th colspan="3">P</th><th colspan="3">D</th><th colspan="3">Microhardness</th></tr>
<tr><th>MAE</th><th>RMSE</th><th>R²</th><th>MAE</th><th>RMSE</th><th>R²</th><th>MAE</th><th>RMSE</th><th>R²</th></tr>
</thead>
<tbody>
<tr><td>RF</td><td>0.32</td><td>0.39</td><td>0.84</td><td>0.29</td><td>0.34</td><td>0.83</td><td>0.29</td><td>0.34</td><td>0.86</td></tr>
<tr><td>GBDT</td><td>0.31</td><td>0.39</td><td>0.85</td><td>0.21</td><td>0.24</td><td>0.92</td><td>0.31</td><td>0.33</td><td>0.92</td></tr>
<tr><td>GA-GBDT</td><td>0.30</td><td>0.32</td><td>0.88</td><td>0.20</td><td>0.23</td><td>0.93</td><td>0.19</td><td>0.24</td><td>0.94</td></tr>
</tbody>
</table>

### 3.3. Evaluating the Predictive Performance of the GA-GBDT ML Algorithm

To assess the predictive capabilities of GA-GBDT, five distinct sets of experimental data, not duplicated in the training data, were considered. The corresponding experimental parameters are detailed in Table 7, while the comparison between the predicted and measured values of coating porosity, dilution, and microhardness by GA-GBDT is illustrated in Figure 10. The trained GA-GBDT machine learning algorithm utilized the pre-processed inputs from the five sets of experimental data to generate the corresponding predicted values. Additionally, Table 8 presents the relative error ($\delta$) of such predicted performance metrics:

$$
\delta = \frac{\mathrm{x_i} - \hat{\mathrm{x_i}}}{\mathrm{x_i}} \times 100\% \tag{13}
$$

The analysis shows that while the predicted values for dilution and microhardness closely match the experimental data, the porosity predictions have larger discrepancies. This lower accuracy in predicting porosity may be attributed to its complex and non-linear nature, insufficient and potentially noisy data, and inadequate feature selection. Additionally, the current model may not be sophisticated enough to capture all the factors affecting porosity, including operational variability. To improve porosity predictions, it may be necessary to enhance data quality and quantity, perform advanced feature engineering,

or use more complex models, including variability factors in the dataset. By applying the previously optimized processing parameters, we predicted the porosity, dilution, and microhardness of the coatings. As shown in Table 8, the predicted values were 2.76% for porosity, 45.27% for dilution, and 553.32 HV₀.₃ for microhardness. These predictions closely matched the experimental data, with corresponding errors of 13.11% for porosity, 3.35% for dilution, and 1.74% for microhardness.

Table 7. Experimental data set employed to investigate the predictive capabilities of the GA-GBDT algorithm.

<table>
<thead>
  <tr>
    <th>Sample</th>
    <th>LP (W)</th>
    <th>SS (mm/s)</th>
    <th>PF (g/min)</th>
    <th>P (%)</th>
    <th>D (%)</th>
    <th>Microhardness (HV₀.₃)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1 (S17)</td>
    <td>2400</td>
    <td>3</td>
    <td>1.2</td>
    <td>0.86</td>
    <td>60.43</td>
    <td>400.94 ± 31.12</td>
  </tr>
  <tr>
    <td>2 (S7)</td>
    <td>2000</td>
    <td>3</td>
    <td>1</td>
    <td>4.53</td>
    <td>30.28</td>
    <td>593.94 ± 57.47</td>
  </tr>
  <tr>
    <td>3 (S15)</td>
    <td>2200</td>
    <td>4.5</td>
    <td>0.9</td>
    <td>8.47</td>
    <td>55.74</td>
    <td>428.51 ± 25.12</td>
  </tr>
  <tr>
    <td>4 (S24)</td>
    <td>2600</td>
    <td>4</td>
    <td>1</td>
    <td>2.76</td>
    <td>54.55</td>
    <td>430.73 ± 18.73</td>
  </tr>
  <tr>
    <td>5 (S4)</td>
    <td>1800</td>
    <td>4</td>
    <td>1.1</td>
    <td>7.64</td>
    <td>42.61</td>
    <td>431.74 ± 22.00</td>
  </tr>
</tbody>
</table>

![](./images/1053528985490685962_12.jpg)

Figure 10. Comparison of predicted and experimental values for coating porosity, dilution, and microhardness.

Table 8. Relative errors between model predictions (GA-GBDT) and experiments concerning coating porosity, dilution, and microhardness. Exp.: experimental; Pred.: predictions.

<table>
<thead>
  <tr>
    <th rowspan="2">Number</th>
    <th colspan="3">P</th>
    <th colspan="3">D</th>
    <th colspan="3">Microhardness</th>
  </tr>
  <tr>
    <th>Exp.</th>
    <th>Pred.</th>
    <th>δ (%)</th>
    <th>Exp.</th>
    <th>Pred.</th>
    <th>δ (%)</th>
    <th>Exp.</th>
    <th>Pred.</th>
    <th>δ (%)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>0.05</td>
    <td>0.13</td>
    <td>158.82</td>
    <td>1.53</td>
    <td>1.32</td>
    <td>−13.13</td>
    <td>−1.39</td>
    <td>−1.99</td>
    <td>43.38</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1.70</td>
    <td>1.51</td>
    <td>−10.94</td>
    <td>−1.19</td>
    <td>−1.03</td>
    <td>−13.92</td>
    <td>1.58</td>
    <td>1.78</td>
    <td>12.59</td>
  </tr>
  <tr>
    <td>3</td>
    <td>1.36</td>
    <td>0.77</td>
    <td>−43.03</td>
    <td>1.10</td>
    <td>0.90</td>
    <td>−18.09</td>
    <td>−0.97</td>
    <td>−1.16</td>
    <td>19.67</td>
  </tr>
  <tr>
    <td>4</td>
    <td>−1.49</td>
    <td>−0.83</td>
    <td>−44.56</td>
    <td>0.99</td>
    <td>1.19</td>
    <td>20.24</td>
    <td>−0.93</td>
    <td>−1.03</td>
    <td>10.50</td>
  </tr>
  <tr>
    <td>5</td>
    <td>−0.69</td>
    <td>−0.44</td>
    <td>−36.85</td>
    <td>−0.08</td>
    <td>−0.10</td>
    <td>24.39</td>
    <td>−0.92</td>
    <td>−0.61</td>
    <td>−33.08</td>
  </tr>
</tbody>
</table>

## 4. Conclusions

In this study, a machine learning-based predictive model was developed to assess the porosity, dilution, and microhardness of $Al_{0.5}Ti_2NbZr$ coatings prepared via laser cladding. Initially, ANOVA was used to analyze how processing parameters—LP, SS, and PF—affect these coating properties. Subsequently, the NSGA-II algorithm optimized these parameters to achieve coatings with superior mechanical properties, aiming for minimal porosity, maximum microhardness, and a maintained dilution rate of 25%. ANOVA results revealed direct effects of LP, SS, and PF on porosity, dilution, and microhardness, with significant interactions among these parameters. LP contributed 61.42%, SS contributed 47.05%, and PF contributed 49.69% to the variations in these properties, respectively. From the Pareto front's optimal solutions identified by NSGA-II, we selected the following processing parameters: LP = 2.384 kW, SS = 2.52 mm/s, and PF = 1.10 g/min.

To enhance the robustness and effectiveness of the optimization process, AI-based predictive models were integrated into the framework. These models provide a powerful

tool for forecasting the effects of varying processing parameters and capturing complex, non-linear relationships between the parameters and the coating properties. Therefore, building on the initial analysis presented above, we implemented Random Forest, Gradi- ent Boosting Decision Tree (GBDT), and Genetic Algorithm-enhanced Gradient Boosting Decision Tree (GA-GBDT). The orthogonal dataset previously used for ANOVA was uti- lized to train and compare these models. Comparison of RF, GBDT, and GA-GBDT using experimental data demonstrated the superior predictive capability of GA-GBDT. Incor- porating the genetic optimization algorithm significantly enhanced GBDT's prediction accuracy, yielding $R^{2}$ values of 0.88,0.93, and 0.94 for porosity, dilution, and microhardness, respectively-outperforming RF and standard GBDT models.

Applying the optimized processing parameters in the GA-GBDT algorithm, we accu- rately predicted the porosity $(2.76 \%)$, dilution $(45.27 \%)$, and microhardness $(553.32 HV_{0.3})$ of the coatings, with relative errors $(\delta)$ of $13.11 \%, 3.35 \%$, and $1.74 \%$ compared to the experimental data.

Overall, this study employed a novel approach to enhance the understanding and optimization of laser-cladded coatings. By sequentially integrating ANOVA for rigor- ous statistical analysis, NSGA-II for precise multi-objective optimization, and advanced machine learning models for accurate predictive modeling, we demonstrated a robust methodology for validating factors, optimizing processing parameters, and predicting coating performance.

Author Contributions: R.D.: Methodology, Formal analysis, Writing-original draft. H.G.: Formal analysis, Funding acquisition. J.L.: Resources, Formal analysis. M.A.: Writing-review and edit- ing, Formal analysis, Funding acquisition. J.Y.: Supervision, Resources, Funding acquisition, Z.Z.: Resources, Funding acquisition. All authors have read and agreed to the published version of the manuscript.

Funding: The work was financially supported by the Open Fund for the Key Laboratory of Geological Disaster Risk Prevention and Control, Emer-gency Management Department of Shandong Province (801KF2024-DZ01), National Science Fund for Excellent Young Scholars (Oversea), China Postdoctoral Science Foundation Funded Project (Project No. 2021M693415), Jiangsu Provincial Postdoctoral Science Foundation Funded Project (Project No. 2020C340), Jiangsu Provincial Double-Innovation Doctor Program (Project No. 202031063), China Postdoctoral International Exchange Program (Project No. PC2022061), and M.A. acknowledges Faculty Support (Starter Grant) funding from the University of Waterloo.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Data are contained within the article.

Conflicts of Interest: The authors declare no conflict of interest.

### References
1. Senkov, O.N.; Wilks, G.B.; Miracle, D.B.; Chuang, C.P.; Liaw, P.K. Refractory high-entropy alloys. *Intermetallics* **2010**, *18*, 1758–1765. [CrossRef]
2. Perepezko, J.H. The Hotter the Engine, the Better. *Science* **2009**, *326*, 1068–1069. [CrossRef] [PubMed]
3. Pollock, T.M. Alloy design for aircraft engines. *Nat. Mater.* **2016**, *15*, 809–815. [CrossRef] [PubMed]
4. Senkov, O.N.; Wilks, G.B.; Scott, J.M.; Miracle, D.B. Mechanical properties of $Nb_{25}Mo_{25}Ta_{25}W_{25}$ and $V_{20}Nb_{20}Mo_{20}Ta_{20}W_{20}$ refractory high entropy alloys. *Intermetallics* **2011**, *19*, 698–706. [CrossRef]
5. Senkov, O.N.; Scott, J.M.; Senkova, S.V.; Miracle, D.B.; Woodward, C.F. Microstructure and room temperature properties of a high-entropy TaNbHfZrTi alloy. *J. Alloys Compd.* **2011**, *509*, 6043–6048. [CrossRef]
6. Senkov, O.N.; Senkova, S.V.; Woodward, C. Effect of aluminum on the microstructure and properties of two refractory high- entropy alloys. *Acta Mater.* **2014**, *68*, 214–228. [CrossRef]
7. Yang, X.; Zhang, Y.; Liaw, P. Microstructure and Compressive Properties of NbTiVTaAlx High Entropy Alloys. *Procedia Eng.* **2012**, *36*, 292–298. [CrossRef]
8. Stepanov, N.D.; Shaysultanov, D.G.; Salishchev, G.A.; Tikhonovsky, M.A. Structure and mechanical properties of a light-weight AlNbTiV high entropy alloy. *Mater. Lett.* **2015**, *142*, 153–155. [CrossRef]

9. Stepanov, N.D.; Yurchenko, N.Y.; Shaysultanov, D.; Salishchev, G.; Tikhonovsky, M.A. Effect of Al on structure and mechanical properties of AlₓNbTiVZr (x = 0, 0.5, 1, 1.5) high entropy alloys. *Mater. Sci. Technol.* 2015, 31, 1184–1193. [CrossRef]

10. Chen, W.; Tang, Q.H.; Wang, H.; Xie, Y.C.; Yan, X.H.; Dai, P.Q. Microstructure and mechanical properties of a novel refractory AlNbTiZr high-entropy alloy. *Mater. Sci. Technol.* 2018, 34, 1309–1315. [CrossRef]

11. Kusinski, J.; Kac, S.; Kopia, A.; Radziszewska, A.; Rozmus-Górnikowska, M.; Major, B.; Major, L.; Marczak, J.; Lisiecki, A. Laser modification of the materials surface layer—A review paper. *Bull. Pol. Acad. Sci. Tech. Sci.* 2012, 60, 711–728. [CrossRef]

12. Gao, Z.; Wang, L.; Wang, Y.; Lyu, F.; Zhan, X. Crack defects and formation mechanism of FeCoCrNi high entropy alloy coating on TC4 titanium alloy prepared by laser cladding. *J. Alloys Compd.* 2022, 903, 163905. [CrossRef]

13. Lou, L.-Y.; Liu, K.-C.; Jia, Y.-J.; Ji, G.; Wang, W.; Li, C.-J.; Li, C.-X. Microstructure and properties of lightweight Al₀.₂CrNbTiV refractory high entropy alloy coating with different dilutions deposited by high speed laser cladding. *Surf. Coat. Technol.* 2022, 447, 128873. [CrossRef]

14. Lou, L.-Y.; Chen, S.-N.; Liu, Y.; Ji, G.; Chen, H.-D.; Jia, Y.-J.; Li, C.-J.; Li, C.-X. Microstructure and mechanical properties of lightweight Al CrNbTiV(x = 0.2, 0.5, 0.8) refractory high entropy alloys. *Int. J. Refract. Met. Hard Mater.* 2022, 104, 105784. [CrossRef]

15. Hemmati, I.; Ocelík, V.; De Hosson, J. Dilution effects in laser cladding of ni–cr–b–si–c hard facing alloys. *Mater. Lett.* 2012, 84, 69–72. [CrossRef]

16. Gao, Q.; Liu, H.; Chen, P.; Liu, X.; Yang, H.; Hao, J. Multi-objective optimization for laser cladding refractory MoNbTiZr high-entropy alloy coating on Ti6Al4V. *Opt. Laser Technol.* 2023, 161, 109220. [CrossRef]

17. Emamian, A.; Corbin, S.F.; Khajepour, A. The influence of combined laser parameters on in-situ formed TiC morphology during laser cladding. *Surf. Coat. Technol.* 2011, 206, 124–131. [CrossRef]

18. Xu, Z.; Yuan, J.; Wu, M.; Arif, A.F.M.; Li, L.; Kong, D.; Zhou, Q. Laser cladding of in situ synthesized tib reinforced ti-based composite coating on t6al4v alloy. *J. Alloys Compd.* 2015, 649, 240–247. [CrossRef]

19. Peng, H.; Chen, W.; Wang, Y.; Lin, J.; Chen, W.; Zhang, Q. Laser cladding of ni ti alloy on t6al4v substrate. *Opt. Laser Technol.* 2014, 57, 44–51. [CrossRef]

20. Sun, W.; Yan, H.; Liu, Z.; Huang, X.; Xiao, L.; Li, H.; Liu, B.; Sun, X. Laser cladding of ni-based alloy and composite coatings: A review. *Int. J. Precis. Eng. Man.-GT* 2021, 8, 367–398.

21. Gao, J.; Wang, C.; Hao, Y.; Wang, X.; Zhao, K.; Ding, X. Prediction of molten pool temperature and processing quality in laser metal deposition based on back propagation neural network algorithm. *Opt. Laser Technol.* 2022, 155, 108363. [CrossRef]

22. Hao, J.; Yang, S.; Le, X.; Królczyk, G.; Sulowicz, M.; Glowacz, A.; Li, Z. Bead morphology prediction of coaxial laser cladding on inclined substrate using machine learning. *J. Manuf. Process.* 2023, 98, 159–172. [CrossRef]

23. Ai, L.; Muggleton, S.H.; Hocquette, C.; Gromowski, M.; Schmid, U. Beneficial and harmful explanatory machine learning. *Mach. Learn.* 2021, 110, 695–721. [CrossRef]

24. Jordan, M.I.; Mitchell, T.M. Machine learning: Trends, perspectives, and prospects. *Science* 2015, 349, 255–260. [CrossRef]

25. Kishino, M.; Matsumoto, K.; Kobayashi, Y.; Taguchi, R.; Akamatsu, N.; Shishido, A. Fatigue life prediction of bending polymer films using random forest. *Int. J. Fatigue* 2023, 166, 107230. [CrossRef]

26. Xu, D.; Wang, Y.; Huang, J.; Liu, S.; Xu, S.; Zhou, K. Prediction of geology condition for slurry pressure balanced shield tunnel with super-large diameter by machine learning algorithms. *Tunn. Undergr. Space Technol.* 2023, 131, 104852. [CrossRef]

27. He, G.; Du, Y.; Liang, Q.; Zhou, Z.; Shu, L. Modeling and Optimization Method of Laser Cladding Based on GA-ACO-RFR and GNSGA-II. *Int. J. Precis. Eng. Manuf. Technol.* 2023, 10, 1207–1222. [CrossRef]

28. St»Hle, L.; Wold, S. Analysis of variance (ANOVA). *Chemom. Intell. Lab. Syst.* 1989, 6, 259–272. [CrossRef]

29. Breiman, L. Random forests. *Mach. Learn.* 2001, 45, 5–32. [CrossRef]

30. Joharestani, M.Z.; Cao, C.; Ni, X.; Bashir, B.; Talebiesfandarani, S. PM₂.₅ Prediction Based on Random Forest, XGBoost, and Deep Learning Using Multisource Remote Sensing Data. *Atmosphere* 2019, 10, 373. [CrossRef]

31. Shaikhina, T.; Lowe, D.; Daga, S.; Briggs, D.; Higgins, R.; Khovanova, N. Decision tree and random forest models for outcome prediction in antibody incompatible kidney transplantation. *Biomed. Signal Process. Control* 2019, 52, 456–462. [CrossRef]

32. Holland, J.H. Genetic algorithms. *Sci. Am.* 1992, 267, 66–73. Available online: https://www.jstor.org/stable/24939139 (accessed on 29 August 2024). [CrossRef]

33. Qu, Y.; Lin, Z.; Li, H.; Zhang, X. Feature Recognition of Urban Road Traffic Accidents Based on GA-XGBoost in the Context of Big Data. *IEEE Access* 2019, 7, 170106–170115. [CrossRef]

34. Cochran, J.M.; Leproux, A.; Busch, D.R.; O’Sullivan, T.D.; Yang, W.; Mehta, R.S.; Police, A.M.; Tromberg, B.J.; Yodh, A.G. Breast cancer differential diagnosis using diffuse optical spectroscopic imaging and regression with z-score normalized data. *J. Biomed. Opt.* 2021, 26, 026004. [CrossRef]

35. Peng, S.; Li, T.; Zhao, J.; Lv, S.; Tan, G.Z.; Dong, M.; Zhang, H. Towards energy and material efficient laser cladding process: Modeling and optimization using a hybrid TS-GEP algorithm and the NSGA-II. *J. Clean. Prod.* 2019, 227, 58–69. [CrossRef]

36. Wu, S.; Liu, Z.; Huang, X.; Wu, Y.; Gong, Y. Process parameter optimization and EBSD analysis of Ni60A-25% WC laser cladding. *Int. J. Refract. Met. Hard Mater.* 2021, 101, 105675. [CrossRef]

37. Cheng, J.; Li, G.; Chen, X. Research on Travel Time Prediction Model of Freeway Based on Gradient Boosting Decision Tree. *IEEE Access* 2018, 7, 7466–7480. [CrossRef]

38. Huang, Y.; Zeng, X.; Hu, Q.; Zhou, S. Microstructure and interface interaction in laser induction hybrid cladding of Ni-based coating. *Appl. Surf. Sci.* 2009, 255, 3940–3945. [CrossRef]

39. Huang, Y.; Ansari, M.; Asgari, H.; Farshidianfar, M.H.; Sarker, D.; Khamesee, M.B.; Toyserkani, E. Rapid prediction of real-time thermal characteristics, solidification parameters and microstructure in laser directed energy deposition (powder-fed additive manufacturing). *J. Mater. Process. Technol.* 2019, 274, 116286. [CrossRef]

40. Chen, C.; Meiping, W.; Rui, H.; Yuling, G.; Xiaojin, M. Understanding Stellite-6 coating prepared by laser cladding: Convection and columnar-to-equiaxed transition. *Opt. Laser Technol.* 2022, 149, 107885. [CrossRef]

41. Wang, T.; Jiang, W.; Wang, X.; Jiang, B.; Rong, C.; Wang, Y.; Yang, J.; Zhu, D. Microstructure and properties of $Al_{0.5}NbTi_3V_xZr_2$ refractory high entropy alloys combined with high strength and ductility. *J. Mater. Res. Technol.* 2023, 24, 1733–1743. [CrossRef]

42. Katoch, S.; Chauhan, S.S.; Kumar, V. A review on genetic algorithm: Past, present, and future. *Multimed. Tools Appl.* 2021, 80, 8091–8126. [CrossRef] [PubMed]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.