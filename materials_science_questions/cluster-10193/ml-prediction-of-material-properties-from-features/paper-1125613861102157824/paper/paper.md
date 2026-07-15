# RESEARCH ARTICLE

# Data Mining and Machine Learning Analysis to Find Polymers for Electronic and Photovoltaics Applications: A Goal to Achieve Higher Dielectric Constant

Bo Xiao, Nafees Ahmad,* Asif Mahmood,* and Mohamed H. Helal

The discovery of polymers with high dielectric constants is of significant interest for advanced electronic applications, such as capacitors, flexible electronics, and energy storage devices. In this study, data mining and machine learning (ML) techniques are applied to identify polymers with superior dielectric constant. Molecular descriptors are calculated. These descriptors are used to train several machine learning models, including linear regression, gradient booting regression, histgradient boosting regression, bagging regression, decision tree regression, and random forest regression. By employing cross-validation and hyperparameter tuning, best model is optimized for robust predictive performance. A database of 10k polymers is generated and their dielectric constant is predicted best ML model. Thirty polymers with higher dielectric constant values are selected. This work demonstrates the power of data-driven approaches in accelerating the discovery of high-performance polymers for electronic applications.

## 1. Introduction

The speed at which charge carriers, like electrons and holes, can flow through a substance when exposed to an electric field is known as charge carrier mobility. Higher mobility allows for faster and more efficient transport of charge, which is crucial in enhancing the performance of electronic devices like transistors, photoceptors and photovoltaic cells.[¹] Improved mobility leads to better conductivity and higher efficiency in converting electrical or solar energy.[²,³] Research has shown that too low mobility results in poor charge extraction, while too high mobility causes other losses, including field screening effects.[⁴] The ideal mobility strikes a balance between efficient charge transport and minimal recombination. This balance depends on the specific material system and device architecture. Achieving optimal mobility is a key focus in the design of organic semiconductors for improving solar cell performance.[⁵,⁶]

The dielectric constant influences charge carrier mobility by affecting the strength of electrostatic interactions between charge carriers and their environment.[⁷] By lowering the Coulombic attraction between charges and their oppositely charged counterparts, a larger dielectric constant facilitates charge separation and increases mobility.[⁸] However, very high dielectric constants can lead to increased polarization and slower charge transport, potentially hindering mobility. Therefore, the relationship between dielectric constant and charge carrier mobility is complex, with an optimal balance depending on the material and device context.

Polymers with higher dielectric constants are essential for high-performance electronic and photovoltaics because they help to reduce the Coulombic attraction between electron-hole pairs (excitons), facilitating their separation into free charge carriers.[⁹] This improved charge separation leads to enhanced charge extraction and reduces recombination losses, thereby increasing the overall efficiency of the solar cell. Higher dielectric constants also allow for better charge stabilization, enabling more efficient transport of charges to the electrodes. Additionally, these polymers can enhance the device's capacitance, leading to improved power conversion. Achieving a balance between a high dielectric constant and good charge carrier mobility is crucial for optimizing performance.

The process of examining big databases to find trends, patterns, and important information that might not be immediately obvious is known as data mining. Large volumes of experimental and computational data can be explored using data mining in materials research to find connections between performance and

---

B. Xiao
College of Chemistry and Materials Science
Sichuan Normal University
Chengdu 610068, P. R. China

N. Ahmad
College of Chemistry and Chemical Engineering
Central South University
Changsha 410083, China
E-mail: nafees@csu.edu.cn

A. Mahmood
Key Laboratory of Cluster Science of Ministry of Education
Beijing Key Laboratory of Photoelectronic/Electrophotonic Conversion Materials
School of Chemistry and Chemical Engineering
Beijing Institute of Technology
Beijing 100081, China
E-mail: 7520190006@bit.edu.cn

M. H. Helal
Center for Scientific Research and Entrepreneurship
Northern Border University
Arar 73213, Saudi Arabia

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adts.202500166

DOI: 10.1002/adts.202500166

![](./images/1125613861102157824_1.jpg)

Figure 1. Correlation between dielectric constant and selected descriptors.

material attributes. $^{[10,11]}$ Researchers can forecast the behavior of novel materials and find viable candidates for particular applications, like effective solar cell materials, by utilizing machine learning techniques. $^{[12]}$ By identifying relationships between elements like structure, composition, and functionality, data mining makes it possible to optimize material qualities. This speeds up the process of finding and creating effective materials without depending entirely on laborious experimental techniques. $^{[13,14]}$

Thanks to machine learning (ML), computers can learn from data and forecast new data. $^{[15,16]}$ To find trends, forecast out-

![](./images/1125613861102157824_2.jpg)

Figure 2. Comparison of ML models based on test set accuracy ($R^2$ value).

![](./images/1125613861102157824_3.jpg)

Figure 3. Comparison of ML models based on the test set's RMSE.

![](./images/1125613861102157824_4.jpg)

Figure 4. Distribution of predicted dielectric constant values.

comes, and adjust in response to fresh information, it employs algorithms. The three main categories of machine learning are reinforcement learning (learning through rewards and penalties), unsupervised learning (finding hidden patterns in unlabeled data), and supervised learning (using labeled data). ML is widely applied in various fields, including healthcare, finance, and autonomous systems. As it evolves, ML continues to drive advancements in automation, data-driven decision-making, and intelligent technologies.

In present study, data mining is used to find polymers with higher dielectric constant. Machine learning (ML) is also used for this purpose. Easily synthesizable polymers are selected from a polymer database. An ML model is used to estimate their dielectric constant values. Higher dielectric constant polymers are chosen and examined.

## 2. Computational Methods
### 2.1. Machine Learning Analysis

The data of dielectric constant is extracted from a published article.[17] Data contains more than 380 points. Mordred software is a tool used to calculate molecular descriptors, which are quantitative representations of molecular properties.[18] It has generated 1800 descriptors, capturing various chemical and structural attributes of the molecules. Python-based tools such as Scikit-learn, Matplotlib, Seaborn, Pandas, Numpy, and Scipy provide a comprehensive ecosystem for data analysis and visualization. Scikit-learn offers machine learning algorithms, while Pandas and Numpy handle data manipulation and numerical computations efficiently. Matplotlib and Seaborn allow for customizable data visualizations, and Scipy complements the toolkit with advanced statistical and scientific computing functions. The dataset was stored in a comma-separated (.CSV) format, ensuring easy access and compatibility with various Python-based tools.

### 2.2. Screening of Monomers and Similarity Analysis

Designing monomers with specific properties based on similarity can be challenging, but data mining techniques offer a viable solution. From the PI1M database,[19] 200 000 monomers with synthetic accessibility (SA) score less than 4 were selected, and their dielectric constant was predicted using a pre-trained machine learning model. Synthetic accessibility (SA) score less than 6 indicates easy synthesis. A portion of the selected database was visualized and analyzed using t-distributed Stochastic Neighbor Embedding (t-SNE) and Structure-Activity Landscape Index (SALI) methods to explore relationships in the data. Additionally, a cluster plot was employed to evaluate the chemical similarity among 30 selected monomers, providing insights into their structural patterns.

## 3. Results and Discussion
### 3.1. Molecular Descriptors

Molecular descriptors are like numerical "fingerprints" that describe the key characteristics of a molecule. These descriptors are fed into machine learning models, which then use them to predict which polymers are likely to have high dielectric constants. By analyzing the most important descriptors, scientists can understand what makes a polymer good at storing electric energy and use that information to design new, better-performing materials. In the present study, molecular descriptors were calculated using Mordred software, a tool known for its comprehensive feature set in molecular characterization. Mordred can generate hundreds of descriptors covering various chemical properties, including topological, geometric, and electronic attributes. These descriptors are crucial for quantifying molecular features that are used in cheminformatics and drug discovery studies.[20,21] By utilizing Mordred, the study aims to establish a more detailed and accurate understanding of the molecular structures under

![](./images/1125613861102157824_5.jpg)

![](./images/1125613861102157824_6.jpg)

![](./images/1125613861102157824_7.jpg)

Figure 7. Structures of selected monomers 1-15.

investigation. Mordred software has generated 1800 molecular descriptors, providing a wide range of features for detailed molecular analysis. However, using such a large number of descriptors can increase the risk of overfitting, where the model becomes too complex and learns the noise in the data rather than general patterns.[¹⁶] Overfitting reduces the model's ability to perform well on new, unseen data, leading to poor generalization. Descriptors with high correlation to the target property (dielectric constant) are chosen for feature selection to improve model performance. These selected descriptors capture key molecular characteristics that influence the dielectric constant. By reducing irrelevant or weakly correlated features, the machine learning model can achieve better accuracy and generalization. Six descriptors are chosen (Figure 1). This figure is a heatmap showing the correlation between the dielectric constant and various molecular descriptors. The color scale on the right indicates the correlation values, where positive correlations are in green and negative correlations are in brown. The highest positive correlation (0.64) is observed with TopoPSA, while the strongest negative correlation (−0.55) is with HybRatio. The other descriptors, such as nS, SIC4, MIC2, and ATSC0Z, show moderate positive correlations ranging from 0.52 to 0.63 with the dielectric constant. The selected descriptors are then used as input variables to train predictive models for dielectric constant estimation.

### 3.2. Machine Learning
Multiple machine learning models were tested to identify the best-performing one for predicting the desired outcomes based

![](./images/1125613861102157824_8.jpg)

Figure 8. Structures of selected monomers 16-30.

on molecular descriptors. $^{[15]}$ Each model was trained and evaluated on a dataset to determine its ability to generalize well and avoid overfitting. Techniques such as cross-validation were employed to ensure robust comparisons between models. Performance metrics like R-squared, or mean squared error were used to rank the models. The best model was selected based on its balance of predictive power and generalizability to unseen data. Six ML models are tried. Accurcy (R-squared values) of tested models is depicted in Figure 2. HistGradient boosting regressor is best model. It is a ML model that builds an ensemble of decision trees to improve predictive accuracy, using histogram-based techniques for faster and more efficient training. It is particularly effective for large datasets and handles continuous data well, making it suitable for regression tasks where high performance is required (Figure 3).

### 3.3. Screening of Polymers
Data mining helps to identify efficient materials by uncovering patterns and relationships within large datasets, enabling the discovery of novel materials with desired properties. $^{[22,23]}$ By analyzing historical data, it can predict how different material combinations will behave, reducing the need for expensive and time-consuming experimental trials. $^{[24-26]}$ Machine learning models, trained on existing material properties, can make accurate predictions for new compounds or structures. This accelerates the materials discovery process, guiding researchers toward the most promising candidates for specific applications.
A selection of 200 000 monomers was made from the PIIM database, a comprehensive resource for polymeric materials. These monomers were chosen to investigate specific proper-

Table 1. The predicted dielectric constant values of 30 searched polymers.

<table>
  <thead>
    <tr>
      <th>Polymer</th>
      <th>Dielectric constant</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>7.18</td>
    </tr>
    <tr>
      <td>2</td>
      <td>6.62</td>
    </tr>
    <tr>
      <td>3</td>
      <td>6.53</td>
    </tr>
    <tr>
      <td>4</td>
      <td>6.38</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6.37</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6.36</td>
    </tr>
    <tr>
      <td>7</td>
      <td>6.35</td>
    </tr>
    <tr>
      <td>8</td>
      <td>6.34</td>
    </tr>
    <tr>
      <td>9</td>
      <td>6.31</td>
    </tr>
    <tr>
      <td>10</td>
      <td>6.25</td>
    </tr>
    <tr>
      <td>11</td>
      <td>6.21</td>
    </tr>
    <tr>
      <td>12</td>
      <td>6.2</td>
    </tr>
    <tr>
      <td>13</td>
      <td>6.2</td>
    </tr>
    <tr>
      <td>14</td>
      <td>6.17</td>
    </tr>
    <tr>
      <td>15</td>
      <td>6.17</td>
    </tr>
    <tr>
      <td>16</td>
      <td>6.15</td>
    </tr>
    <tr>
      <td>17</td>
      <td>6.14</td>
    </tr>
    <tr>
      <td>18</td>
      <td>6.14</td>
    </tr>
    <tr>
      <td>19</td>
      <td>6.11</td>
    </tr>
    <tr>
      <td>20</td>
      <td>6.11</td>
    </tr>
    <tr>
      <td>21</td>
      <td>6.11</td>
    </tr>
    <tr>
      <td>22</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>23</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>24</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>25</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>26</td>
      <td>6.09</td>
    </tr>
    <tr>
      <td>27</td>
      <td>6.09</td>
    </tr>
    <tr>
      <td>28</td>
      <td>6.03</td>
    </tr>
    <tr>
      <td>29</td>
      <td>6</td>
    </tr>
    <tr>
      <td>30</td>
      <td>5.98</td>
    </tr>
  </tbody>
</table>

ties, such as their dielectric constant. The selection allows for large-scale analysis using machine learning models, which pre- dict how these monomers might behave under certain condi- tions. This dataset forms the basis for further computational analysis, including visualization and chemical similarity assess- ments. The dielectric constant of monomers is predicted using best ML model. The distribution of predicted dielectric constant values for 200 000 is given in Figure 4. Majority of polymers are showing values less than 5.10 k monomers with higher di- electric constant values are selected for visualization analysis. Figure 5 is showing t-SNE plot, space is full of monomers with values near to 5. Higher values than 5 are hidden behind red circles.

The Structure Activity Landscape Index (SALI) is a metric used to quantify and analyze activity cliffs in structure-activity relation- ship (SAR) studies. Activity cliffs occur when small changes in molecular structure led to disproportionately large changes in target property. By using SALI, researchers can systematically assess the steepness of these cliffs, helping to identify critical regions in chemical space where structural modifications have significant impacts on activity. The index is calculated as the ratio of the activity difference between two compounds to the structural difference, providing insights into the relationship be- tween molecular changes and target property. This quantitative tool aids in understanding SARs, facilitating more rational drug design and optimization. SALI plot is given in Figure 6. Polymers are divided into small colonies that are well-separated from oth- ers. There is minor change in dielectric constant on structural changes.

We selected 30 monomers with the highest predicted dielectric constants to enhance electronic and photovoltaic performance. Monomers with high dielectric constants reduce Coulombic at- traction between electron-hole pairs (excitons), promoting their dissociation into free charge carriers. This property is crucial for improving charge transport and efficiency in electronic and photovoltaic applications. By minimizing exciton binding en- ergy, these materials enable better charge separation, reduc- ing energy losses. Therefore, our selection focuses on optimiz- ing dielectric properties to enhance device performance. Chem- ical structures of selected monomers are given in Figures 7 and 8 (Table 1).

### 3.4. Analysis of Chemical Similarity

Chemical similarity in polymers helps to identify how closely related different polymers are in terms of their chemical struc- ture and properties. $^{[27,28]}$ By analyzing their molecular compo sition, functional groups, and repeating units, one can pre- dict behaviors like solubility, thermal stability, and mechanical strength. $^{[29,30]}$ It also aids in understanding how slight variations in polymer structure can affect performance in specific applica- tions, such as in packaging, medicine, or electronics. $^{[31,32]}$ Addi tionally, chemical similarity allows for the prediction of poten- tial interactions between polymers and other materials, which is crucial in material design and development. Chemical similar- ity is studied using RDkit. Chemical similarity is studied using fingerprints. RDkit compares chemical structures and the quan- tifies the similarity between molecules, Tanimoto similarity in- dex is used for this purpose. In the present study, a heatmap is used to display the chemical similarity analysis's findings, where each cell represents the similarity score between pairs of polymers. The color gradient in the heatmap indicates vary- ing degrees of similarity, with darker or lighter shades corre- sponding to higher or lower similarity, respectively. This graph- ical representation provides an intuitive way to identify clusters of chemically similar polymers and discern structural relation- ships across the dataset. Heatmap is given in Figure 9. There is clear structural diversity in selected polymers. It means higher dielectric constant can be achieved from any specific structural features.

### 4. Conclusion

In this study, data mining and machine learning techniques are successfully employed to identify polymers with higher dielectric constants. Six machine learning models are tried and HistGradi- ent boosting regressor is best model. Polymers that are easily syn- thesizable are selected from polymer database. The best model is

![](./images/1125613861102157824_9.jpg)

Figure 9. Clustering of monomers on basis of similarity.

used to predict their dielectric constant values. Thirty polymers with greater dielectric constants are chosen. A clear structural di- versity is found in selected polymers.

### Acknowledgements
The authors extend their appreciation to the Deanship of Scientific Re- search at Northern Border University, Arar, KSA for funding this research work through the project number "NBU-FFR-2025-540-03".

### Conflict of Interest
The authors declare no conflict of interest.

### Data Availability Statement
The data that support the findings of this study are available from the cor- responding author upon reasonable request.

### Keywords
dielectric constant, machine learning, polymers, synthetic accessibility

Received: January 28, 2025
Revised: April 1, 2025
Published online: May 3, 2025

[1] A. A. Mohapatra, Y. Dong, P. Boregowda, A. Mohanty, A. Sadhanala, X. Jiao, A. Narayan, C. R. McNeill, J. R. Durrant, S. Patil, *J. Phys. Chem. C* **2021**, 125, 6886.

[2] P. Fan, G.-J. Chen, S. Chen, Z.-H. Zheng, M. Azam, N. Ahmad, Z.-H. Su, G.-X. Liang, X.-H. Zhang, Z.-G. Chen, *ACS Appl. Mater. Interfaces* **2021**, 13, 46671.

[3] G. Wu, T. Yang, X. Li, N. Ahmad, X. Zhang, S. Yue, J. Zhou, Y. Li, H. Wang, X. Shi, S. Liu, K. Zhao, H. Zhou, Y. Zhang, *Matter* **2021**, 4, 582.

[4] P. Guo, J. Liang, J. He, S. Guan, Q. Wang, F. Shi, Y. Zhou, C. Wang, Y. Xia, *Opt. Mater.* **2024**, 150, 115119.

[5] G. Wu, N. Ahmad, Y. Zhang, *J. Mater. Chem. C* **2021**, 9, 9851.

[6] K. Li, S. Yue, X. Li, N. Ahmad, Q. Cheng, B. Wang, X. Zhang, S. Li, Y. Li, G. Huang, H. Kang, T. Yue, S. U. Zafar, H. Zhou, L. Zhu, Y. Zhang, *Adv. Funct. Mater.* **2022**, 32, 2200024.

[7] S. M. R. Billah, in *Functional Polymers* (Eds: M. A. Jafar Mazumder, H. Sheardown, A. Al-Ahmed), Springer International Publishing, Cham, **2019**, pp. 241-288.

[8] B. Chen, F. Zheng, Q. Wang, P. Guo, Q. Liang, Y. Zhang, C. Wang, Y. Xia, H. Wu, *Sol. Energy* **2022**, 236, 206.

[9] J. Brebels, E. Douvogianni, D. Devisscher, R. Thiruvallur Eachambadi, J. Manca, L. Lutsen, D. Vanderzande, J. C. Hummelen, W. Maes, *J. Mater. Chem. C* **2018**, 6, 500.

[10] A. Mahmood, A. Irfan, J.-L. Wang, *Chem. - Eur. J.* **2022**, 28, 202103712.

[11] A. Mahmood, J.-L. Wang, *J. Mater. Chem. A* **2021**, 9, 15684.

[12] N. Ahmad, Y. Zhao, F. Ye, J. Zhao, S. Chen, Z. Zheng, P. Fan, C. Yan, Y. Li, Z. Su, X. Zhang, G. Liang, *Adv. Sci.* **2023**, 10, 2302869.

*Adv. Theory Simul.* **2025**, 8, 2500166
2500166 (9 of 10)
© 2025 Wiley-VCH GmbH

[13] T. Yue, K. Li, X. Li, N. Ahmad, H. Kang, Q. Cheng, Y. Zhang, Y. Yue, Y. Jing, B. Wang, S. Li, J. Chen, G. Huang, Y. Li, Z. Fu, T. Wu, S. U. Zafar, L. Zhu, H. Zhou, Y. Zhang, ACS Nano 2023, 17, 14632.

[14] X. Chen, Y. Zhao, N. Ahmad, J. Zhao, Z. Zheng, Z. Su, X. Peng, X. Li, X. Zhang, P. Fan, G. Liang, S. Chen, Nano Energy 2024, 124, 109448.

[15] A. Mahmood, Y. Sandali, J.-L. Wang, Phys. Chem. Chem. Phys. 2023, 25, 10417.

[16] A. Mahmood, A. Irfan, J.-L. Wang, Chin. J. Polym. Sci. 2022, 40, 870.

[17] C. Kuenneth, A. C. Rajan, H. Tran, L. Chen, C. Kim, R. Ramprasad, Patterns 2021, 2, 100238.

[18] H. Moriwaki, Y.-S. Tian, N. Kawashita, T. Takagi, J. Cheminformatics 2018, 10, 4.

[19] R. Ma, T. Luo, J. Chem. Inf. Model. 2020, 60, 4684.

[20] N. Ahmad, A. Kausar, B. Muhammad, J. Plast. Film Sheeting 2015, 32, 419.

[21] N. Ahmad, A. Kausar, B. Muhammad, Fuller. Nanotub. 2016, 24, 75.

[22] Y. Tian, Y. Cai, Y. Chen, M. Jia, H. Hu, W. Xie, D. Li, H. Song, S. Guo, X. Zhang, Adv. Funct. Mater. 2024, 34, 2316342.

[23] R.-M. Hao, L. Zhu, T.-F. Shang, Z.-B. Xu, Q.-P. Wu, Chem. Eng. J. 2024, 497, 154979.

[24] M. I. Abdullah, M. R. S. A. Janjua, M. F. Nazar, A. Mahmood, Bull. Chem. Soc. Jpn. 2013, 86, 1272.

[25] A. Irfan, A. Mahmood, J. Mex. Chem. Soc. 2017, 61, 309.

[26] T. Zhang, W. Zhao, Q. He, J. Xu, Sustainability 2025, 17, 648.

[27] M. R. S. A. Janjua, A. Irfan, M. Hussien, M. Ali, M. Saqib, M. Sulaman, Energy Technol. 2022, 10, 2200019.

[28] A. Mahmood, S. Naeem, A. Javed, Z. Shafiq, M. A. El-Sheikh, H. O. Elansary, M. R. Saeed, Ashraf Janjua, Mater. Today Commun. 2024, 38, 108403.

[29] F. Chen, Y. Yang, M. Zhou, X. Huang, Y. Gao, K. Li, Z. Chen, C. Zhou, Z. Zhou, C. Zheng, X. Gao, Chem. Eng. J. 2025, 510, 161651.

[30] L. Gao, M. Cao, C. Zhang, J. Li, X. Zhu, X. Guo, Z. Toktarbay, Adv. Compos. Hybrid Mater. 2024, 7, 144.

[31] F. Ahmad, A. Mahmood, I. H. El Azab, N. Ahmad, M. H. H. Mahmoud, Z. M. El-Bahy, J. Photochem. Photobiol. A 2024, 453, 115670.

[32] X. Li, S. Xiong, G. Li, S. Xiao, C. Zhang, Y. Ma, Mater. Lett. 2023, 346, 134481.
