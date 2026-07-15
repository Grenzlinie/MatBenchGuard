OPEN
# Enhancing topological index of calcium chloride network through feature selection methods exploration

Sana Javed¹, Shabbir Ahmad¹, Noor Sehar¹, Sadia Khalid¹, Muhammad Kamran Siddiqui¹ & Brima Gegbe²⊠

With the chemical formula $CaCl_2$, calcium chloride is a salt as well as an inorganic material. At room temperature, it has the consistency of a white, crystalline solid and is very water-soluble. It can be created by neutralizing calcium hydroxide with hydrochloric acid. Calcium chloride is a solution with a large enthalpy change. It is extensively utilized in research facilities, manufacturing facilities, and pharmaceuticals, including all types of food-graded applications, the treatment of acute illnesses, packaging for drying tubes, dust controllers, and de-icing, among other uses. In this paper, firstly we compute the topological indices, coindices, and reverse indices of $CaCl_2$. Further, we employ machine learning strategies to capture the best suitable set of indices for the proximity of the prediction of distinct physio-chemical properties of $CaCl_2$. To strengthen the results, different regression techniques are implemented to predict HOF of $CaCl_2$ based on our features, and the most influential features were detected to verify our results.

Keywords Topological indices, Calcium chloride, Inorganic compound, Feature selection, Regression methods, MATLAB, Python

Many applications in other science disciplines utilize graph theoretical tools (see¹⁻²). In chemistry, these tools introduce a specific branch of graph theory based on topological indices, known as chemical graph theory³. These indices or descriptors are considered to study the graphical structure of different chemical or molecular elements⁴. It provides a way to illustrate any structure or compound in a graphical form which helps to study the interrelated behavior of chemical components. It provides a deep insight into how the chemical components or molecules are related and influence each other⁵. Chemical compounds are composed of various chemical elements; in a chemical graph, such elements are represented by nodes or vertices while their bonding is considered as an edge between two elements. Several studies have been conducted in recent years to analyze different chemical substances in the form of chemical graphs using graphical or topological descriptors⁶.

Graphical and topological descriptors are the values that usually define the topology of the corresponding structure. This topology might be defined based on distances between the vertices or degrees of the vertices. Comprehension of the topology of the graph, under consideration, helps us to study different chemical properties or activities interrelated with the graph structure. Any two isomorphic graphs share the same topological indices while the converse is not true⁷. Many thermodynamical measures including heat of formation, entropy or boiling point can be studied based on these descriptors⁸. Such measurable physical properties can be easily understood in the form of such connectivity indices which are directly computed using the graphical structure of the chemical compound under consideration.

Calcium chloride is a salt that is an inorganic material. At room temperature, it has the consistency of a white, crystalline solid and is very water-soluble. It might be manufactured by neutralizing calcium hydroxide with hydrochloric acid. Calcium chloride is a solution with a large enthalpy change. It is extensively utilized in research facilities, manufacturing facilities, and pharmaceuticals, including all types of food-graded applications, the treatment of acute illnesses, packaging for drying tubes, dust controllers, and de-icing, among other uses. Given the widespread use of $CaCl_2$, it is important to research this chemical compound in depth. Figure 1 represents the chemical structure of calcium chloride.

¹Department of Mathematics, COMSATS University Islamabad, Lahore Campus, Lahore, Pakistan. ²Department of Mathematics and Statistics, Njala University, Freetown, Sierra Leone. ⊠email: bgegbe@njala.edu.sl

![](./images/1064023331520380987_1.jpg)

Fig. 1. Calcium Chloride

Let $\mathcal{Q}$ be a graph with $\mathcal{V}(\mathcal{Q})$ and $\mathcal{E}(\mathcal{Q})$ representing the vertex and edge set of $\mathrm{CaCl}_{2}$, respectively. Suppose $|\mathcal{V}(\mathcal{Q})|=x$, $|\mathcal{E}(\mathcal{Q})|=y$ and $\xi(x)$ denotes the degree of $x$. The Randić index presented by Milan Randić⁹, was the first index based on the basis of the degree of vertices of graphs. The general Randić index⁹ is defined in (1).

$$
\Re_{\beta}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})}\left(\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)\right)^{\beta}, \quad \text { where } \quad \beta \in\left\{1,-1, \frac{1}{2},-\frac{1}{2}\right\} \tag{1}
$$

Estrada et al¹⁰ presented a graph descriptor, named as atom bond connectivity index and denoted as $\mathcal{ABC}$ (2).

$$
\mathcal{ABC}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})} \sqrt{\frac{\xi\left(x_{1}\right)+\xi\left(x_{2}\right)-2}{\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)}} \tag{2}
$$

Geometric arithmetic index $\mathcal{G}\mathcal{A}$ given in (3) was introduced by Vukicevic et al¹¹.

$$
\mathcal{G}\mathcal{A}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})} \frac{2 \sqrt{\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)}}{\xi\left(x_{1}\right)+\xi\left(x_{1}\right)} \tag{3}
$$

The forgotten index is used to describe the branching properties of a molecule. It is calculated by counting the number of forgotten vertices in a graph, which are not part of a cycle. The forgotten index invented by Furtula et al¹² is given in (4).

$$
F(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})}\left[\xi\left(x_{2}\right)^{2}+\xi\left(x_{2}\right)^{2}\right] \tag{4}
$$

Another index developed in¹³ is augmented Zagreb index, represented by $\mathcal{A}\mathcal{Z}\mathcal{I}$, which is provided in (5).

$$
\mathcal{A}\mathcal{Z}\mathcal{I}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})}\left(\frac{\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)}{\xi\left(x_{1}\right)+\xi\left(x_{2}\right)-2}\right)^{3} \tag{5}
$$

The two most common indices are the first and second Zagreb indices (see¹⁴ and¹⁵) that are used to predict the strength of a material. These are defined in (6) and (7), respectively.

$$
\mathcal{M}_{1}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})}\left[\xi\left(x_{1}\right)+\xi\left(x_{2}\right)\right] \tag{6}
$$

$$
\mathcal{M}_{2}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})}\left[\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)\right] \tag{7}
$$

All Zagreb indices were modified by Ranjini et al⁷ and are referred as redefined Zagreb indices given in (8)-(10).

$$
\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{1}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})} \frac{\xi\left(x_{1}\right)+\xi\left(x_{2}\right)}{\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)} \tag{8}
$$

$$
\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{2}(\mathcal{Q})=\sum_{x_{1} x_{2} \in \mathcal{E}(\mathcal{Q})} \frac{\xi\left(x_{1}\right) \times \xi\left(x_{2}\right)}{\xi\left(x_{1}\right)+\xi\left(x_{2}\right)} \tag{9}
$$

$$
\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}(\mathcal{Q}) = \sum_{x_{1}x_{2} \in \mathcal{E}(\mathcal{Q})} \left(\xi(x_{1}) \times \xi(x_{2})\right)\left(\xi(x_{1}) + \xi(x_{2})\right)
\tag{10}
$$

The idea of co-index was provided in¹⁶. The co-index of a graph $\mathcal{Q}$ might be derived by considering its complement graph as given in Theorem 1.

**Theorem 1** Let $\overline{\mathcal{Q}}$ be the complement graph of $\mathcal{Q} = (\mathcal{V}, \mathcal{E})$ with vertex set $\mathcal{V}$ and edge set $\overline{\mathcal{E}}$. Let $\mathcal{T}$ represent any degree-based topological index $\mathcal{Q}$. Then the co-index $\overline{\mathcal{T}}$ of $\mathcal{Q}$ is as follows:
$$
\mathcal{C}\mathcal{T}(\mathcal{Q}) = \mathcal{T}(\overline{\mathcal{Q}})
$$

Kulli first proposed the idea of the reverse degree of a vertex in¹⁷, it is based on $\bigtriangleup(\mathcal{Q})$ where $\bigtriangleup(\mathcal{Q}) = \max\{\xi(x_{1}); x_{1} \in \mathcal{V}(\mathcal{Q})\}$, and is defined as follows for a vertex $x_{1}$.
$$
\eta[\xi(x_{1})] = \bigtriangleup(\mathcal{Q}) - \xi(x_{1}) + 1
$$

The reverse Randic index is defined as follows (11). All remaining reverse indices might be defined in a similar way.
$$
\mathcal{R}_{\beta}(\mathcal{Q}) = \sum_{x_{1}x_{2} \in \mathcal{E}(\mathcal{Q})} \left(\eta[\xi(x_{1})] \times \eta[\xi(x_{1})]\right)^{\beta}, \text{ where } \quad \beta \in \left\{1, -1, \frac{1}{2}, -\frac{1}{2}\right\}
\tag{11}
$$

Machine learning is a subfield of artificial intelligence that emphasizes on emergence of algorithms and processes trained on data having the ability to forecast or make decisions. Statistical approaches along with computational algorithms are employed to investigate and infer large datasets, gaining valuable knowledge and patterns. At present, machine learning is playing a vital role in many disciplines including finance, health care, marketing, and robotics where it might be used to program tasks, optimize procedures, and increase overall efficiency.

High-dimensional data might be an obstacle due to the existence of extraneous, deceptive, or unnecessary attributes. It might create issues in processing the data and learning process. To address this matter, the feature subset selection technique is utilized to detect the best valuable attributes for model building. This procedure is expedited by various feature selection algorithms, which are centered on an explicit definition of relevance. Usually, feature selection is recognized as a hunt for the best attributes based on specific evaluation standards. Feature selection includes selecting a particular set of attributes from a data set to train machine learning algorithms. It doesn't modify the original features but rather chooses a subgroup of them. The central aims of feature selection are to improve the performance of machine learning models, develop quicker and more economical algorithms, and make it easier to comprehend the predictions made by the models.

Over the years, numerous techniques have been created to select features, catering to different data and model requirements. Feature selection algorithms can be categorized into three groups based on how they generate and assess feature subsets: filter methods, wrapper methods, and embedded methods (see Fig. 2).

Zaman et al¹⁸ emphasize the importance of topological indices, particularly coindices, in identifying correlations between molecular structures and their therapeutic efficacy. Nadeem et al¹⁹ analyze MOFs using underlying molecular networks, which allows them to extract and examine the topological properties of these complex structures. The study highlights the utility of topological indices in understanding the connectivity, stability, and function of MOFs. Ahmed et al²⁰ focus on applying supervised machine learning algorithms to predict the physicochemical properties of anti-HIV drugs based on topological descriptors. Danish et al²¹ delve into predictive modeling and regression analysis to study the bioactivity of sulfonamide compounds used in cancer therapy. Koam et al²² conduct a comparative study focusing on valency-based topological descriptors

![](./images/1064023331520380987_2.jpg)

Fig. 2. Methods of feature selection

<table>
 <thead>
  <tr>
   <th>
    $\xi{(x_{1})}$
   </th>
   <th>
    Frequencies
   </th>
   <th>
    No of Vertices
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    1
   </td>
   <td>
    8
   </td>
   <td>
    $\mathcal{V}_{1}$
   </td>
  </tr>
  <tr>
   <td>
    2
   </td>
   <td>
    ${4mn} - {4m} + {4n} + 8$
   </td>
   <td>
    $\mathcal{V}_{2}$
   </td>
  </tr>
  <tr>
   <td>
    3
   </td>
   <td>
    $2mn$
   </td>
   <td>
    $\mathcal{V}_{3}$
   </td>
  </tr>
  <tr>
   <td>
    4
   </td>
   <td>
    ${2mn} - {2m} - {2n} + 2$
   </td>
   <td>
    $\mathcal{V}_{4}$
   </td>
  </tr>
  <tr>
   <td>
    6
   </td>
   <td>
    $2mn$
   </td>
   <td>
    $\mathcal{V}_{5}$
   </td>
  </tr>
 </tbody>
</table>

Table 1. Vertex Partition of CaCl₂

<table>
 <thead>
  <tr>
   <th>
    $(\xi{(x_{1})},\xi{(x_{2})})$
   </th>
   <th>
    Frequencies
   </th>
   <th>
    No of Edges
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    (1, 2)
   </td>
   <td>
    4
   </td>
   <td>
    $\mathcal{E}_{1}$
   </td>
  </tr>
  <tr>
   <td>
    (1, 3)
   </td>
   <td>
    4
   </td>
   <td>
    $\mathcal{E}_{2}$
   </td>
  </tr>
  <tr>
   <td>
    (2, 2)
   </td>
   <td>
    ${4m} + {4n} - 8$
   </td>
   <td>
    $\mathcal{E}_{3}$
   </td>
  </tr>
  <tr>
   <td>
    (2, 3)
   </td>
   <td>
    ${4m} + {4n} - 8$
   </td>
   <td>
    $\mathcal{E}_{4}$
   </td>
  </tr>
  <tr>
   <td>
    (2, 4)
   </td>
   <td>
    ${4mn} - {4m} - {4n} + 4$
   </td>
   <td>
    $\mathcal{E}_{5}$
   </td>
  </tr>
  <tr>
   <td>
    (2, 6)
   </td>
   <td>
    $4mn$
   </td>
   <td>
    $\mathcal{E}_{6}$
   </td>
  </tr>
  <tr>
   <td>
    (3, 4)
   </td>
   <td>
    ${4mn} - {4m} - {4n} + 4$
   </td>
   <td>
    $\mathcal{E}_{7}$
   </td>
  </tr>
  <tr>
   <td>
    (3, 6)
   </td>
   <td>
    $2mn$
   </td>
   <td>
    $\mathcal{E}_{8}$
   </td>
  </tr>
 </tbody>
</table>

Table 2. Edge Partition of CaCl₂

for the Hexagon Star Network, a structure of interest in nanomaterials and molecular networks. Masmali et al²⁰ focus on the graph-theoretical parameters of anticancer drugs, exploring how these parameters can inform the structural and functional properties of these compounds.

### Degree based topological indices/Coindices/Reverse indices
Randic index, atom bond connectivity index, geometric arithmetic index, forgotten index, augmented Zagreb index, first and second Zagreb indices, and redefined Zagreb indices of CaCl₂ are included in this section along with their corresponding coindices and reverse indices. Tables 1 and 2 provide the vertex partition and edge partition of CaCl₂, respectively.

In Theorem 2, the degree based indices defined in Eqs. (1)–(10) are computed for the $m \times n$ unit cell of chemical graph of calcium chloride.

**Theorem 2** Consider the chemical graph $\mathcal{Q}$ of CaCl₂. The indices $\mathcal{R}_{\alpha};{\alpha \in {\{1,{- 1},\frac{1}{2},{- \frac{1}{2}}\}}}$, $\mathcal{ABC}$, $\mathcal{GA}$, $\mathcal{F}$, $\mathcal{AZI}$, $\mathcal{M}_{1}$, $\mathcal{M}_{2}$, $\mathcal{ReZG}_{1}$, $\mathcal{ReZG}_{2}$ and $\mathcal{ReZG}_{3}$ for $\mathcal{Q}$ are as follows:

$$\mathcal{R}1{(\mathcal{Q})} = {164mn} - {40m} - {40n} + 20$$

$$\mathcal{R}_{- 1}{(\mathcal{Q})} = {1.2778mn} + {0.8333m} + {0.8333n} + 2.1667$$

$$\mathcal{R}_{\frac{1}{2}}{(\mathcal{Q})} = {47.5118mn} - {7.3722m} - {7.3722n} + 2.1593$$

$$\mathcal{R}_{- \frac{1}{2}}{(\mathcal{Q})} = {4.1950mn} + {1.0641m} + {1.0641n} + 0.4408$$

$$\mathcal{ABC}{(\mathcal{Q})} = {9.4860mn} + {0.2464m} + {0.2464n} + 0.1911$$

$$\mathcal{GA}{(\mathcal{Q})} = {13.07998mn} + {0.1890m} + {0.1890n} - 0.8728$$

$$\mathcal{F}{(\mathcal{Q})} = {430mn} - {96m} - {96n} + 72$$

$$\mathcal{AZI}{(\mathcal{Q})} = {153.3818mn} - {23.296m} - {23.296n} + 4.796$$

$$\mathcal{M}_{1}{(\mathcal{Q})} = {102mn} - {16m} - {16n} + 8$$

$$\mathcal{M}_{2}{(\mathcal{Q})} = {164mn} - {40m} - {40n} + 20$$

$$\mathcal{ReZG}_{1}{(\mathcal{Q})} = {11.6667mn} + {2m} + {2n} + 2$$

$$\mathcal{ReZG}_{2}{(\mathcal{Q})} = {22.1905mn} - {3.3905m} - {3.3905n} + 0.2571$$

$$\mathcal{ReZG}_{3}{(\mathcal{Q})} = {1236mn} - {344m} - {344n} + 232$$

Table 3 provides the numerical values for the indices for ${m \times n};{m,n \in {\{1,2,3,\ldots,100\}}}$ unit cells of $\mathcal{Q}$ computed in Theorem 2. Figure 3 illustrate these indices graphically.

Table 4 provides the edge partitions of the complement graph of CaCl₂ by using Theorem 1.

**Theorem 3** Consider the chemical graph $\mathcal{Q}$ of CaCl₂. The degree based coindices $\mathcal{CR}_{\beta}{(\mathcal{Q})}$; $\beta \in \{ 1, - 1,\frac{1}{2}, - \frac{1}{2}\}$, $\mathcal{CABC}{(\mathcal{Q})}$, $\mathcal{CF}{(\mathcal{Q})}$, $\mathcal{CGA}{(\mathcal{Q})}$, $\mathcal{CAZI}{(\mathcal{Q})}$, $\mathcal{CM}_{1}{(\mathcal{Q})}$, $\mathcal{CM}_{2}{(\mathcal{Q})}$, $\mathcal{CReZG}_{1}{(\mathcal{Q})}$, $\mathcal{CReZG}_{2}{(\mathcal{Q})}$ and $\mathcal{CReZG}_{3}{(\mathcal{Q})}$ are computed for the $m \times n$ unit cell of chemical graph of calcium chloride as follows.

<table><thead><tr><th>Index/Cell</th><th>$1×1$</th><th>$2×2$</th><th>$3×3$</th><th>...</th><th>$98×98$</th><th>$99×99$</th><th>$100×100$</th></tr></thead><tbody><tr><td>$\mathcal{R}_{1}(Q)$</td><td>104</td><td>516</td><td>1256</td><td>...</td><td>1567236</td><td>1599464</td><td>1632020</td></tr><tr><td>$\mathcal{R}_{-1}(Q)$</td><td>5.1111</td><td>10.6111</td><td>18.6667</td><td>...</td><td>12437.4847</td><td>12690.8779</td><td>12946.8267</td></tr><tr><td>$\mathcal{R}_{\frac{1}{2}}(Q)$</td><td>34.9267</td><td>162.7177</td><td>385.5323</td><td>...</td><td>454860.5353</td><td>464205.6155</td><td>473645.7193</td></tr><tr><td>$\mathcal{R}_{-\frac{1}{2}}(Q)$</td><td>6.764</td><td>21.4772</td><td>44.5804</td><td>...</td><td>40497.7844</td><td>41326.3276</td><td>42163.2608</td></tr><tr><td>$\mathcal{ABC}(Q)$</td><td>10.1699</td><td>39.1207</td><td>87.0435</td><td>...</td><td>91152.0295</td><td>93021.2643</td><td>94909.4711</td></tr><tr><td>$\mathcal{GA}(Q)$</td><td>12.58518</td><td>52.20312</td><td>117.98102</td><td>...</td><td>125656.2991</td><td>128233.4332</td><td>130836.7272</td></tr><tr><td>$\mathcal{F}(Q)$</td><td>310</td><td>1408</td><td>3366</td><td>...</td><td>4110976</td><td>4195494</td><td>4280872</td></tr><tr><td>$\mathcal{AZI}(Q)$</td><td>111.5858</td><td>525.1392</td><td>1245.4562</td><td>...</td><td>1468517.587</td><td>1498687.21</td><td>1529163.596</td></tr><tr><td>$\mathcal{M}_{1}(Q)$</td><td>78</td><td>352</td><td>830</td><td>...</td><td>976480</td><td>996542</td><td>1016808</td></tr><tr><td>$\mathcal{M}_{2}(Q)$</td><td>104</td><td>516</td><td>1256</td><td>...</td><td>1567236</td><td>1599464</td><td>1632020</td></tr><tr><td>$\mathcal{ReZG}_{1}(Q)$</td><td>17.667</td><td>56.668</td><td>119.003</td><td>...</td><td>112443.868</td><td>114746.267</td><td>117072</td></tr><tr><td>$\mathcal{ReZG}_{2}(Q)$</td><td>15.6666</td><td>75.4571</td><td>179.6286</td><td>...</td><td>212453.2811</td><td>216818.0286</td><td>221227.1571</td></tr><tr><td>$\mathcal{ReZG}_{3}(Q)$</td><td>780</td><td>3800</td><td>9292</td><td>...</td><td>11803352</td><td>12046156</td><td>12291432</td></tr></tbody></table>

Table 3. Indices Values for $m×n$ Unit Cell of $CaCl_2$; $m,n\in\{1,2,...,100\}$

![](./images/1064023331520380987_3.jpg)

![](./images/1064023331520380987_4.jpg)

![](./images/1064023331520380987_5.jpg)

![](./images/1064023331520380987_6.jpg)

Fig. 3. Graphical illustration of $\mathcal{R}_{\alpha};\alpha\in\{1,-1,\frac{1}{2},-\frac{1}{2}\},\mathcal{ABC},\mathcal{GA},\mathcal{F},\mathcal{AZI},\mathcal{M}_1,\mathcal{M}_2,\mathcal{ReZG}_1,\mathcal{ReZG}_2$ and $\mathcal{ReZG}_3$ for $Q$

$$\mathcal{CR}1(\mathcal{Q})=358m^{2}n^{2}-384m^{2}n+10mn^{2}+564mn+8m^{2}-8n^{2}-320m+176n+124$$

$$\begin{aligned}
\mathcal{CR}_{-1}(\mathcal{Q})=& 5.556m^{2}n^{2}-7.6667m^{2}n+5.6667mn^{2}+31.611mn+m^{2}-n^{2}-26.333m \\
& +22.6667n+35.8333
\end{aligned}$$

$$\begin{aligned}
\mathcal{CR}_{\frac{1}{2}}(\mathcal{Q})=& 116.7631m^{2}n^{2}+16.0897m^{2}n+65.4523mn^{2}+241.1257mn \\
& +22.6274m^{2}-22.6274n^{2}-157.7649m-22.0004n+105.7230
\end{aligned}$$

$$\begin{aligned}
\mathcal{CR}_{-\frac{1}{2}}(\mathcal{Q})=& 14.5013m^{2}n^{2}-20.3869m^{2}n+12.4207mn^{2}+56.8750mn+2.8284m^{2} \\
& -2.8284n^{2}-45.1768m+38.0554n+56.6045
\end{aligned}$$

$$\begin{aligned}
\mathcal{CABC}(\mathcal{Q})=& 27.708m^{2}n^{2}+31.3591m^{2}n+20.0454mn^{2}+81.1132mn+5.6569m^{2} \\
& -5.6569n^{2}-58.2292m+40.7658n+53.5490
\end{aligned}$$

$$\begin{aligned}
\mathcal{CGA}(\mathcal{Q})=& 38.0393m^{2}n^{2}-49.8105m^{2}n+26.8076mn^{2}+104.8371mn \\
& +7.5425m^{2}-7.5425n^{2}-78.9863m+56n+73.6701
\end{aligned}$$

$$\mathcal{CF}(\mathcal{Q})=928m^{2}n^{2}-972m^{2}n+452mn^{2}+790mn+16m^{2}-16n^{2}-752m+368n+248$$

$$\begin{aligned}
\mathcal{CAZI}(\mathcal{Q})=& 379.3077m^{2}n^{2}-881m^{2}n+200.704mn^{2}+1803.9942mn+64m^{2}-64n^{2} \\
& -632.704m+486.816n+603.204
\end{aligned}$$

$$\mathcal{CM}_{1}(\mathcal{Q})=248m^{2}n^{2}-292m^{2}n+140mn^{2}+518mn+48m^{2}-48n^{2}-328m+200n+360$$

$$\mathcal{CM}_{2}(\mathcal{Q})=358m^{2}n^{2}-384m^{2}n+160mn^{2}+564mn+8m^{2}-8n^{2}-320m+176n+124$$

$$\begin{aligned}
\mathcal{CReZG}_{1}(\mathcal{Q})=& 35.6667m^{2}n^{2}-47.6667m^{2}n+31mn^{2}+129.6667mn+6m^{2}-6n^{2} \\
& -67m+74n+100
\end{aligned}$$

$$\begin{aligned}
\mathcal{CReZG}_{2}(\mathcal{Q})=& 49.123om^{2}n^{2}-65.7908m^{2}n+30.7429mn^{2}+112.533mn+10.6667m^{2} \\
& -10.6667n^{2}-82.6095m+48.0571n+67.7429
\end{aligned}$$

$$\begin{aligned}
\mathcal{CReZG}_{3}(\mathcal{Q})=& 2504m^{2}n^{2}-2368m^{2}n+928mn^{2}+3068mn+389m^{2}-389n^{2} \\
& -1410m+696n+1240
\end{aligned}$$

Table 5 provides the numerical values for the indices for $m \times n; m, n \in \{1,2,3,...,100\}$ unit cells of $\mathcal{Q}$ computed in Theorem 3. Figure 4 illustrate these indices graphically.

By using equations (11), the vertex and edge partition of $\mathcal{Q}$ are given in Tables 6 and 7, respectively.

Theorem 4 Consider the chemical graph $\mathcal{Q}$ of $CaCl_{2}$. The reverse indices $\mathcal{RR}_{\beta}(\mathcal{Q}); \beta \in \{1, -1, \frac{1}{2}, -\frac{1}{2}\}$, $\mathcal{RABC}(\mathcal{Q})$, $\mathcal{RF}(\mathcal{Q})$, $\mathcal{RGA}(\mathcal{Q})$, $\mathcal{RAZI}(\mathcal{Q})$, $\mathcal{RM}_{1}(\mathcal{Q})$, $\mathcal{RM}_{2}(\mathcal{Q})$, $\mathcal{RReZG}_{1}(\mathcal{Q})$, $\mathcal{RReZG}_{2}(\mathcal{Q})$, and $\mathcal{RReZG}_{3}(\mathcal{Q})$ are computed for $m \times n$ unit cell of chemical graph of calcium chloride are as follows:

<table><thead><tr><th>Index/Cell</th><th>$1 × 1$</th><th>$2 × 2$</th><th>$3 × 3$</th><th>...</th><th>$98 × 98$</th><th>$99 × 99$</th><th>$100 × 100$</th></tr></thead><tbody><tr><td>$\mathcal{CR}_{1}(\mathcal{Q})$</td><td>528</td><td>4828</td><td>23668</td><td>...</td><td>32674176988</td><td>34031958964</td><td>35431625724</td></tr><tr><td>$\mathcal{CR}_{-1}(\mathcal{Q})$</td><td>67.334</td><td>227.8407</td><td>705.3694</td><td>...</td><td>510888634.3</td><td>532076037.4</td><td>553915779.2</td></tr><tr><td>$\mathcal{CR}_{\frac{1}{2}}(\mathcal{Q})$</td><td>365.3885</td><td>3231.2408</td><td>13396.0035</td><td>...</td><td>10848901508</td><td>11297682501</td><td>11760245386</td></tr><tr><td>$\mathcal{CR}_{-\frac{1}{2}}(\mathcal{Q})$</td><td>112.8932</td><td>438.1529</td><td>1506.6332</td><td>...</td><td>1330601602</td><td>1385816280</td><td>1442731894</td></tr><tr><td>$\mathcal{CABC}(\mathcal{Q})$</td><td>196.3113</td><td>1197.639</td><td>4363.4471</td><td>...</td><td>2604856555</td><td>2712290475</td><td>2823013939</td></tr><tr><td>$\mathcal{CGA}(\mathcal{Q})$</td><td>170.56</td><td>871.6569</td><td>3408.3582</td><td>...</td><td>3487978446</td><td>3632745596</td><td>3781973246</td></tr><tr><td>$\mathcal{CF}(\mathcal{Q})$</td><td>1062</td><td>13328</td><td>67334</td><td>...</td><td>85113895184</td><td>88646459270</td><td>92287861848</td></tr><tr><td>$\mathcal{CAZI}(\mathcal{Q})$</td><td>1960.3219</td><td>8153.96</td><td>28757.4195</td><td>...</td><td>34363157246</td><td>35793722897</td><td>37268499956</td></tr><tr><td>$\mathcal{CM}_{1}(\mathcal{Q})$</td><td>846</td><td>4928</td><td>20622</td><td>...</td><td>22736631872</td><td>23680360206</td><td>24653167560</td></tr><tr><td>$\mathcal{CM}_{2}(\mathcal{Q})$</td><td>678</td><td>6028</td><td>27718</td><td>...</td><td>32815355788</td><td>34177503814</td><td>35581625724</td></tr><tr><td>$\mathcal{CReZ}_{1}(\mathcal{Q})$</td><td>255.6667</td><td>1070.0004</td><td>3727.0021</td><td>...</td><td>3275342386</td><td>3411228945</td><td>3551300767</td></tr><tr><td>$\mathcal{CReZ}_{2}(\mathcal{Q})$</td><td>159.7986</td><td>954.3549</td><td>4009.5524</td><td>...</td><td>4499039758</td><td>4685828421</td><td>4878374043</td></tr><tr><td>$\mathcal{CReZ}_{3}(\mathcal{Q})$</td><td>4658</td><td>40628</td><td>190654</td><td>...</td><td>$2.29635 × 10^{11}$</td><td>$2.39166 × 10^{11}$</td><td>$2.48991 × 10^{11}$</td></tr></tbody></table>

Table 5. Coindices Values for $m \times n$ Unit Cell of $CaCl_{2}, m, n \in \{1,2,...,100\}$

![](./images/1064023331520380987_7.jpg)

(a) $\mathcal{CR}_{\beta}(\mathcal{Q});\ \beta\in\{1,-1,\frac{1}{2},-\frac{1}{2}\}$

![](./images/1064023331520380987_8.jpg)

(b) $\mathcal{CABC}(\mathcal{Q}),\ \mathcal{CF}(\mathcal{Q}),\ \mathcal{CGA}(\mathcal{Q}),\ \mathcal{CAZI}(\mathcal{Q})$

![](./images/1064023331520380987_9.jpg)

(c) $\mathcal{CM}_{1}(\mathcal{Q}),\ \mathcal{CM}_{2}(\mathcal{Q})$

![](./images/1064023331520380987_10.jpg)

(d) $\mathcal{CReZG}_{1}(\mathcal{Q}),\ \mathcal{CReZG}_{2}(\mathcal{Q}),\ \mathcal{CReZG}_{3}(\mathcal{Q})$

Fig. 4. Graphical Illustration of $\mathcal{CR}_{\beta}(\mathcal{Q});\ \beta\in\{1,-1,\frac{1}{2},-\frac{1}{2}\},\mathcal{CABC}(\mathcal{Q}),\mathcal{CF}(\mathcal{Q}),\mathcal{CGA}(\mathcal{Q}),\mathcal{CAZI}(\mathcal{Q}),$
$\mathcal{CM}_{1}(\mathcal{Q}),\mathcal{CM}_{2}(\mathcal{Q}),\mathcal{CReZG}_{1}(\mathcal{Q}),\mathcal{CReZG}_{2}(\mathcal{Q}),$ and $\mathcal{CReZG}_{3}(\mathcal{Q})$

<table>
<thead>
  <tr>
    <th>$\xi(x_1)$</th>
    <th>Frequencies</th>
    <th>No of Vertices</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>6</td>
    <td>8</td>
    <td>$\mathcal{V}_1$</td>
  </tr>
  <tr>
    <td>5</td>
    <td>$4mn-4m+4n+8$</td>
    <td>$\mathcal{V}_2$</td>
  </tr>
  <tr>
    <td>4</td>
    <td>$2mn$</td>
    <td>$\mathcal{V}_3$</td>
  </tr>
  <tr>
    <td>3</td>
    <td>$2mn-2m-2n+2$</td>
    <td>$\mathcal{V}_4$</td>
  </tr>
  <tr>
    <td>1</td>
    <td>$2mn$</td>
    <td>$\mathcal{V}_5$</td>
  </tr>
</tbody>
</table>

Table 6. Vertex Partition of ${\text{CaCl}}_{2}$

<table>
<thead>
  <tr>
    <th>$(\xi(x_1),\ \xi(x_2))$</th>
    <th>Frequencies</th>
    <th>No of Edges</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>(5, 6)</td>
    <td>4</td>
    <td>$\mathcal{E}_1$</td>
  </tr>
  <tr>
    <td>(4, 6)</td>
    <td>4</td>
    <td>$\mathcal{E}_2$</td>
  </tr>
  <tr>
    <td>(5, 5)</td>
    <td>$4m+4n-8$</td>
    <td>$\mathcal{E}_3$</td>
  </tr>
  <tr>
    <td>(4, 5)</td>
    <td>$4m+4n-8$</td>
    <td>$\mathcal{E}_4$</td>
  </tr>
  <tr>
    <td>(3, 5)</td>
    <td>$4mn-4m-4n+4$</td>
    <td>$\mathcal{E}_5$</td>
  </tr>
  <tr>
    <td>(1, 5)</td>
    <td>$4mn$</td>
    <td>$\mathcal{E}_6$</td>
  </tr>
  <tr>
    <td>(3, 4)</td>
    <td>$4mn-4m-4n+4$</td>
    <td>$\mathcal{E}_7$</td>
  </tr>
  <tr>
    <td>(1, 4)</td>
    <td>$2mn$</td>
    <td>$\mathcal{E}_8$</td>
  </tr>
</tbody>
</table>

Table 7. Edge Partition of ${\text{CaCl}}_{2}$

$$\mathcal{RR}_{1}(\mathcal{Q}) = 136mn + 72m + 72n - 36$$

$$\mathcal{RR}_{-1}(\mathcal{Q}) = 1.9mn - 0.24m - 0.24n + 0.18$$

$$\mathcal{RR}_{\frac{1}{2}}(\mathcal{Q}) = 42.2926mn + 8.5402m + 8.5402n - 4.9239$$

$$\mathcal{RR}_{-\frac{1}{2}}(\mathcal{Q}) = 4.9764mn - 0.4931m - 0.4931n + 0.3954$$

$$\mathcal{RABC}(\mathcal{Q}) = 10.4216mn + 0.4957m + 0.4957n - 2.5028$$

$$\mathcal{RGA}(\mathcal{Q}) = 12.4134mn + 0.1433m + 0.1433n - 0.2159$$

$$\mathcal{RF}(\mathcal{Q}) = 374mn + 128m + 128n - 40$$

$$\mathcal{RAZI}(\mathcal{Q}) = 130.3493mn + 9.7612m + 9.7612n + 118.8296$$

$$\mathcal{RM}_{1}(\mathcal{Q}) = 90mn + 16m + 16n - 8$$

$$\mathcal{RM}_{2}(\mathcal{Q}) = 136mn + 72m + 72n + 144$$

$$\mathcal{RReZG}_{1}(\mathcal{Q}) = 11.7667mn + 0.2m + 0.2n + 0.8$$

$$\mathcal{RReZG}_{2}(\mathcal{Q}) = 15.5405mn + 6.7540m + 6.7540n - 2.9115$$

$$\mathcal{RReZG}_{3}(\mathcal{Q}) = 976mn + 904m + 904n - 344$$

Table 8 provides the numerical values for the reverse indices for $m \times n; m, n \in \{1, 2, 3, \dots, 100\}$ unit cells of $\mathcal{Q}$ computed in Theorem 4. Figure 5 illustrate these indices graphically.

### Correlation analysis
A heat map is a great tool to visualize the relationship between the features of a data set. The intensity of color depicts the strength of the relation among the variables. The coefficient of correlation is used to capture such relation. A heat map of indices, coincices and reverse indices found in Theorems 2, 3 and 4 is shown in Fig. 6. It might be seen clearly from the heat map that several indices are highly correlated with each other which shows the occurrence of multicollinearity. Multicollinearity yields to unstable and untrustworthy coefficient assessments in model fitting. Feature selection is highly recommended approach to handle this issue. In this paper, we have used an exhaustive feature selector for the evaluation of the possible feature combinations.

### Data normalization
Data normalization is used to scale the features to a common range to handle the influence of a particular feature on the estimation of model. It aids in improving model's performance and convergence. It is also helpful in manipulating the outliers in the data. Existence of outliers might produce wrong predictions and can affect the performance of model. Outliers can sometimes indicate unusual or extreme values in the data set, and they can have a significant impact on statistical analysis and interpretation. It is important to consider the implications of displaying outliers before normalizing the data. Without normalization, the outliers may appear more extreme or influential than they actually are, which can impact the overall analysis and decision-making process. To ensure a more accurate and reliable interpretation of the data, it is recommended to normalize the data before further analysis. Before conducting any analysis on the data it is important to visualize the data and detect any outliers.

Box plots are particularly useful to display the spread and skewness of the selected features in a concise and informative manner. By examining the box plot, one can quickly identify the central tendency, variability,

<table>
  <thead>
    <tr>
      <th>Index/Cell</th>
      <th>$1 \times 1$</th>
      <th>$2 \times 2$</th>
      <th>$3 \times 3$</th>
      <th>...</th>
      <th>$98 \times 98$</th>
      <th>$99 \times 99$</th>
      <th>$100 \times 100$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathcal{RR}_{1}(\mathcal{Q})$</td>
      <td>244</td>
      <td>796</td>
      <td>1620</td>
      <td>...</td>
      <td>1320220</td>
      <td>1347156</td>
      <td>1374364</td>
    </tr>
    <tr>
      <td>$\mathcal{RR}_{-1}(\mathcal{Q})$</td>
      <td>1.6</td>
      <td>6.82</td>
      <td>15.84</td>
      <td>...</td>
      <td>18200.74</td>
      <td>18574.56</td>
      <td>18952.18</td>
    </tr>
    <tr>
      <td>$\mathcal{RR}_{\frac{1}{2}}(\mathcal{Q})$</td>
      <td>54.4491</td>
      <td>198.4073</td>
      <td>426.9507</td>
      <td>...</td>
      <td>407847.1</td>
      <td>416195.8</td>
      <td>424629.1</td>
    </tr>
    <tr>
      <td>$\mathcal{RR}_{-\frac{1}{2}}(\mathcal{Q})$</td>
      <td>4.3856</td>
      <td>18.3286</td>
      <td>42.2244</td>
      <td>...</td>
      <td>47697.09</td>
      <td>48676.46</td>
      <td>49665.78</td>
    </tr>
    <tr>
      <td>$\mathcal{RABC}(\mathcal{Q})$</td>
      <td>8.9102</td>
      <td>41.1664</td>
      <td>94.2658</td>
      <td>...</td>
      <td>100183.7</td>
      <td>102237.7</td>
      <td>104312.6</td>
    </tr>
    <tr>
      <td>$\mathcal{RGA}(\mathcal{Q})$</td>
      <td>12.4841</td>
      <td>50.0109</td>
      <td>112.3645</td>
      <td>...</td>
      <td>119246.2</td>
      <td>121691.9</td>
      <td>124162.4</td>
    </tr>
    <tr>
      <td>$\mathcal{RF}(\mathcal{Q})$</td>
      <td>590</td>
      <td>1968</td>
      <td>4094</td>
      <td>...</td>
      <td>3616944</td>
      <td>3690878</td>
      <td>3765560</td>
    </tr>
    <tr>
      <td>$\mathcal{RAZI}(\mathcal{Q})$</td>
      <td>268.7013</td>
      <td>679.2716</td>
      <td>1350.541</td>
      <td>...</td>
      <td>1253907</td>
      <td>1279605</td>
      <td>1305564</td>
    </tr>
    <tr>
      <td>$\mathcal{RM}_{1}(\mathcal{Q})$</td>
      <td>114</td>
      <td>416</td>
      <td>898</td>
      <td>...</td>
      <td>867488</td>
      <td>885250</td>
      <td>903192</td>
    </tr>
    <tr>
      <td>$\mathcal{RM}_{2}(\mathcal{Q})$</td>
      <td>424</td>
      <td>976</td>
      <td>1800</td>
      <td>...</td>
      <td>1320400</td>
      <td>1347336</td>
      <td>1374544</td>
    </tr>
    <tr>
      <td>$\mathcal{RReZG}_{1}(\mathcal{Q})$</td>
      <td>12.9667</td>
      <td>48.6668</td>
      <td>107.9003</td>
      <td>...</td>
      <td>113047.4</td>
      <td>115365.8</td>
      <td>117707.8</td>
    </tr>
    <tr>
      <td>$\mathcal{RReZG}_{2}(\mathcal{Q})$</td>
      <td>26.137</td>
      <td>86.2665</td>
      <td>177.477</td>
      <td>...</td>
      <td>150571.8</td>
      <td>15365.8</td>
      <td>156752.9</td>
    </tr>
    <tr>
      <td>$\mathcal{RReZG}_{3}(\mathcal{Q})$</td>
      <td>2440</td>
      <td>7176</td>
      <td>13864</td>
      <td>...</td>
      <td>9550344</td>
      <td>9744424</td>
      <td>9940456</td>
    </tr>
  </tbody>
</table>

Table 8. Reverse Indices Values for $m \times n$ Unit Cell of $CaCl_{2}; m, n \in \{1, 2, \dots, 100\}$

![](./images/1064023331520380987_11.jpg)

(a) $\mathcal{RR}_\beta(Q);\ \beta \in \{1, -1, \frac{1}{2}, -\frac{1}{2}\}$

![](./images/1064023331520380987_12.jpg)

(b) $\mathcal{RABC}(Q), \mathcal{RR}(Q), \mathcal{RGA}(Q), \mathcal{RAZI}(Q)$

![](./images/1064023331520380987_13.jpg)

(c) $\mathcal{RM}_1(Q), \mathcal{RM}_2(Q)$

![](./images/1064023331520380987_14.jpg)

(d) $\mathcal{RReZG}_1(Q), \mathcal{RReZG}_2(Q), \mathcal{RReZG}_3(Q)$

Fig. 5. Graphical Illustration of $\mathcal{RR}_\beta(Q);\ \beta \in \{1, -1, \frac{1}{2}, -\frac{1}{2}\},\mathcal{RABC}(Q),\mathcal{RF}(Q),\mathcal{RGA}(Q),\mathcal{RAZI}(Q), \mathcal{RM}_1(Q),\mathcal{RM}_2(Q),\mathcal{RReZG}_1(Q),\mathcal{RReZG}_2(Q)$ and $\mathcal{RReZG}_3(Q)$

![](./images/1064023331520380987_15.jpg)

Fig. 6. Heat Map of indices, coindices and reverse indices

and presence of outliers in the data. The length of the box indicates the spread of the data, with a longer box indicating a larger range. The position of the median within the box gives an idea of the symmetry or skewness of the distribution. The whiskers provide information about the range of the data, while the outliers give insights into any unusual or extreme values.

We have generated a box plot that displays the distribution of accuracy scores for each set of selected features. The box plot displays a set of data points, and within this plot, there are a few outliers that stand out of a selected portion. These outliers are data points that deviate significantly from the rest of the data. They can be identified as individual points that are located far away from the main cluster of data points in the box plot.

Figures 7 and 8 represent the box plots of the features without normalization and with normalization, respectively. The absence of the outliers can be clearly seen from Fig. 8. In Figs. 7 and 8, CRN1, CR12, CRN12, CABC, CGA, CF, CM1, CM2, CReZ1, CReZ2 and CReZ3 represent the indices $\mathcal{CR}_1, \mathcal{CR}_{\frac{1}{2}}, \mathcal{CR}_{-\frac{1}{2}}, \mathcal{CABC}, \mathcal{CGA}, \mathcal{CF}, \mathcal{CM}_1, \mathcal{CM}_2, \mathcal{CReZG}_1, \mathcal{CReZG}_2$ and $\mathcal{CReZG}_3$, respectively.

![](./images/1064023331520380987_16.jpg)

Fig. 7. Box plot before normalization

![](./images/1064023331520380987_17.jpg)

Fig. 8. Box plot after normalization

## Feature selection of topological indices
The Exhaustive Feature Selector (EFS) class from mlxtend.feature_selection is used to detect the important set of features in our data set that is based on indices, coindices, reverse indices found in "Degree based topological indices/Coindices/Reverse indices" section. This EFS algorithm is a wrapper approach to systematically generate and test the subsets of features; the optimal selection is made by optimizing an indicated evaluation metric subject to an vagarious regressor or classifier.

Following are key steps of EFS algorithm after importing important libraries, data manipulation, and initializing model like linear regression:

- Choose an estimator to assess feature combinations
- Set the range of the size of feature subset
- Pick a metric for evaluation
- Select cross validation fold
- Fix number of analogous procedures, if necessary.

Table 9 provides the results by initializing linear regression model from scikit-learn, setting maximum number of features equal to 1, using 5-fold cross validation and $R^2$ as scoring metric. The indices $\mathcal{GA}$, $\mathcal{RGA}$, $\mathcal{RABC}$, $\mathcal{RR}_{-\frac{1}{2}}$, $\mathcal{RReZG}_1$, $\mathcal{ABC}$, $\mathcal{CF}$, $\mathcal{RR}_{-1}$, $\mathcal{CReZG}_3$, and $\mathcal{CM}_2$ are lying on the top 10 positions among all indices based on the defined metric. This result helps to determine the subset of features, inclusion of which in any model estimation might produce robust results.

<table><thead><tr><th>Indices</th><th>Score</th></tr></thead><tbody><tr><td>$\mathcal{G}\mathcal{A}$</td><td>0.999999</td></tr><tr><td>$\mathcal{R}\mathcal{G}\mathcal{A}$</td><td>0.999997</td></tr><tr><td>$\mathcal{R}\mathcal{A}\mathcal{B}\mathcal{C}$</td><td>0.999997</td></tr><tr><td>$\mathcal{R}\mathcal{R}_{-\frac{1}{2}}$</td><td>0.999988</td></tr><tr><td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td><td>0.999985</td></tr><tr><td>$\mathcal{A}\mathcal{B}\mathcal{C}$</td><td>0.999985</td></tr><tr><td>$\mathcal{C}\mathcal{F}$</td><td>0.999975</td></tr><tr><td>$\mathcal{R}\mathcal{R}_{-1}$</td><td>0.999960</td></tr><tr><td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td><td>0.999958</td></tr><tr><td>$\mathcal{C}\mathcal{M}_{2}$</td><td>0.999954</td></tr><tr><td>$\mathcal{C}\mathcal{R}_{1}$</td><td>0.999911</td></tr><tr><td>$\mathcal{R}\mathcal{M}_{1}$</td><td>0.999898</td></tr><tr><td>$\mathcal{M}_{1}$</td><td>0.999887</td></tr><tr><td>$\mathcal{R}_{\frac{1}{2}}$</td><td>0.999879</td></tr><tr><td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td><td>0.999878</td></tr><tr><td>$\mathcal{R}\mathcal{R}_{\frac{1}{2}}$</td><td>0.999871</td></tr><tr><td>$\mathcal{A}\mathcal{Z}\mathcal{I}$</td><td>0.999869</td></tr><tr><td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td><td>0.999848</td></tr><tr><td>$\mathcal{C}\mathcal{M}_{1}$</td><td>0.999838</td></tr><tr><td>$\mathcal{F}$</td><td>0.999795</td></tr><tr><td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td><td>0.999785</td></tr><tr><td>$\mathcal{C}\mathcal{G}\mathcal{A}$</td><td>0.999730</td></tr><tr><td>$\mathcal{R}_{1}$</td><td>0.999700</td></tr><tr><td>$\mathcal{M}_{2}$</td><td>0.999700</td></tr><tr><td>$\mathcal{C}\mathcal{R}_{\frac{1}{2}}$</td><td>0.999654</td></tr><tr><td>$\mathcal{R}\mathcal{A}\mathcal{Z}\mathcal{I}$</td><td>0.999643</td></tr><tr><td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td><td>0.999643</td></tr><tr><td>$\mathcal{R}\mathcal{F}$</td><td>0.999630</td></tr><tr><td>$\mathcal{R}_{-\frac{1}{2}}$</td><td>0.999592</td></tr><tr><td>$\mathcal{C}\mathcal{A}\mathcal{Z}\mathcal{I}$</td><td>0.999586</td></tr><tr><td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td><td>0.999445</td></tr><tr><td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td><td>0.999429</td></tr><tr><td>$\mathcal{C}\mathcal{R}_{-\frac{1}{2}}$</td><td>0.999401</td></tr><tr><td>$\mathcal{R}\mathcal{R}_{1}$</td><td>0.999260</td></tr><tr><td>$\mathcal{C}\mathcal{R}_{-1}$</td><td>0.998925</td></tr><tr><td>$\mathcal{C}\mathcal{A}\mathcal{B}\mathcal{C}$</td><td>0.998801</td></tr><tr><td>$\mathcal{R}\mathcal{M}_{2}$</td><td>0.998405</td></tr><tr><td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td><td>0.998052</td></tr><tr><td>$\mathcal{R}_{-1}$</td><td>0.996981</td></tr></tbody></table>

Table 9. Score Wise Features Obtained through EFS

From Table 9, we can see the index $\mathcal{G}\mathcal{A}$, possesses the highest average score while $\mathcal{R}\mathcal{G}\mathcal{A}$ lies on the second number which yields the decision of considering these attributes as good indicators for the prediction of distinct physio-chemical properties of $CaCl_2$. This result is further strengthened by considering a heap map that showcases a collection of chosen features through a visually appealing representation. This graphical depiction allows for a quick and intuitive understanding of the distribution and significance of these features. Each feature is assigned a specific color, which corresponds to its value or intensity. By observing the heat map, one can easily identify clusters or patterns within the selected features, as areas with similar colors indicate similarities in their values. This enables researchers or analysts to gain valuable insights into the relationships and interactions between these features, aiding in decision-making or further analysis. The heat map graph of our selected features is given in Fig. 9.

From Fig. 9, we can easily see that $\mathcal{G}\mathcal{A}$ and $\mathcal{R}\mathcal{G}\mathcal{A}$ are highly related with all the other indices except $\mathcal{R}\mathcal{R}_{-1}$, $\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$, $\mathcal{C}\mathcal{M}_{2}$ which are in turn distinctly linked with $\mathcal{A}\mathcal{B}\mathcal{C}$. Also, $\mathcal{A}\mathcal{B}\mathcal{C}$ is highly correlated with $\mathcal{G}\mathcal{A}$ and

![](./images/1064023331520380987_18.jpg)

Fig. 9. Heat map of selected features

![](./images/1064023331520380987_19.jpg)

Fig. 10. Cluster map of selected features

$\mathcal{RGA}$. So, we can consider either $\mathcal{GA}$ and $\mathcal{CGA}$ as the most potential candidate for the further explanation of the chemical structure and linked properties of $\text{CaCl}_2$.

The cluster map offers a holistic view of the selected features, enabling a deeper understanding of their relationships. It helps to uncover hidden structures and relationships that may not be immediately apparent when examining the features individually. By utilizing the cluster map, researchers can make informed decisions and draw meaningful conclusions based on the collective behavior and characteristics of the selected features. The cluster map of our selected features is given below. Cluster map in Fig. 10 exhibits the similar findings as above since we can see from the clusters and positions of indices the distances between them. We can see from the cluster map that the set of indices $\mathcal{RGA}, \mathcal{GA}$ possesses the last two positions while the set of indices $\mathcal{CM}_2$, $\mathcal{RR}_{-1},\mathcal{CReZG}_3$ constitutes the first three positions showing largest distance between both set of indices while $\mathcal{ABC}$ lies next to $\mathcal{GA}$ depicting high correlation between them. This finding supports our results obtained above.

### Heat of formation of $\text{CaCl}_2$
This section includes the values of heat of formation $HOF$ for $m \times n; m,n \in \{1,2,\cdots,100\}$ unit cell of $\text{CaCl}_2$. The values for $m \times n$ unit cells have been computed by using the standard value of $HOF$ that is $\Delta H_f^o=-795.4\,\text{kJ/mol}$, and the following formula:

$$
HOF(m,n)=\frac{(m+n)^2 \times (-795.8)}{60.22}\text{kJ/mol}.
$$

Table 10 represents the values of $HOF$ for $m \times n \in \{1,2,\dots,100\}$ unit cells of $\text{CaCl}_2$.

### Reliance of heat formation on selected indices
To re-evaluate our findings in previous section we have used different regression techniques. Total five regression techniques namely adaptive boosting (A-Boost), extra-tree regression (ET), random forest (RF), F-Regression (F), gradient boosting (GB), Lasso-CV (L-CV), Ridge-CV (R-CV), multi-linear regression(ML) have been

<table>
<thead>
<tr>
<th>Cell</th>
<th>$1 × 1$</th>
<th>$2 × 2$</th>
<th>$3 × 3$</th>
<th>...</th>
<th>$98 × 98$</th>
<th>$99 × 99$</th>
<th>$100 × 100$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$HOF$</td>
<td>− 52.85951511</td>
<td>− 211.4380604</td>
<td>− 475.735636</td>
<td>...</td>
<td>− 507662.7831</td>
<td>− 518076.1076</td>
<td>− 528595.1511</td>
</tr>
</tbody>
</table>

Table 10. Heat of Formation for $m × n$ Unit Cell of CaCl₂; $m × n \in \{1,2,\dots,100\}$

<table>
<thead>
<tr>
<th>Index</th>
<th>A-Boost</th>
<th>ET</th>
<th>RF</th>
<th>F</th>
<th>GB</th>
<th>L-CV</th>
<th>R-CV</th>
<th>ML</th>
<th>Average</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mathcal{G}\mathcal{A}$</td>
<td>0.034</td>
<td>0.012</td>
<td>0.049</td>
<td>6,970,226,364.351</td>
<td>0.003</td>
<td>0</td>
<td>0.011</td>
<td>0.087</td>
<td>871,278,295.568</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{G}\mathcal{A}$</td>
<td>0.036</td>
<td>0.025</td>
<td>0.047</td>
<td>1,981,349,743.241</td>
<td>0.002</td>
<td>0</td>
<td>0.011</td>
<td>0.094</td>
<td>247,668,717.932</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.036</td>
<td>0.029</td>
<td>0.022</td>
<td>1,586,080,823.792</td>
<td>0.015</td>
<td>0</td>
<td>0.011</td>
<td>0.126</td>
<td>198,260,103.004</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.018</td>
<td>0.036</td>
<td>0.040</td>
<td>390,329,782.897</td>
<td>0.035</td>
<td>0</td>
<td>0.010</td>
<td>0.062</td>
<td>48,791,222.887</td>
</tr>
<tr>
<td>$\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.024</td>
<td>0.028</td>
<td>0.027</td>
<td>378,929,723.989</td>
<td>0.016</td>
<td>0</td>
<td>0.009</td>
<td>0.042</td>
<td>47,366,215.517</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.020</td>
<td>0.045</td>
<td>0.029</td>
<td>357,699,192.453</td>
<td>0.001</td>
<td>0</td>
<td>0.007</td>
<td>0.058</td>
<td>44,712,399.077</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{F}$</td>
<td>0.035</td>
<td>0.021</td>
<td>0.006</td>
<td>172,018,055.077</td>
<td>0.004</td>
<td>0</td>
<td>0.028</td>
<td>0.046</td>
<td>21,502,256.902</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.021</td>
<td>0.019</td>
<td>0.033</td>
<td>121,960,584.700</td>
<td>0.023</td>
<td>0</td>
<td>0.025</td>
<td>0.018</td>
<td>15,245,073.103</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{-1}$</td>
<td>0.042</td>
<td>0.030</td>
<td>0.031</td>
<td>117,543,584.133</td>
<td>0.006</td>
<td>0</td>
<td>0.004</td>
<td>0.018</td>
<td>14,692,948.033</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{M}_{2}$</td>
<td>0.022</td>
<td>0.014</td>
<td>0.027</td>
<td>86,261,688.482</td>
<td>0.018</td>
<td>0</td>
<td>0.016</td>
<td>0.058</td>
<td>10,782,711.080</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{M}_{1}$</td>
<td>0.026</td>
<td>0.025</td>
<td>0.058</td>
<td>49,473,447.905</td>
<td>0.153</td>
<td>0</td>
<td>0.021</td>
<td>0.125</td>
<td>6,184,181.039</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{1}$</td>
<td>0.020</td>
<td>0.014</td>
<td>0.040</td>
<td>47,138,251.495</td>
<td>0.003</td>
<td>0</td>
<td>0.018</td>
<td>0.030</td>
<td>5,892,281.453</td>
</tr>
<tr>
<td>$\mathcal{M}_{1}$</td>
<td>0.049</td>
<td>0.036</td>
<td>0.015</td>
<td>45,616,746.409</td>
<td>0.001</td>
<td>0</td>
<td>0.027</td>
<td>0.084</td>
<td>5,702,093.328</td>
</tr>
<tr>
<td>$\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.020</td>
<td>0.028</td>
<td>0.022</td>
<td>43,033,929.174</td>
<td>0.012</td>
<td>0</td>
<td>0.021</td>
<td>0.068</td>
<td>5,379,241.168</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.033</td>
<td>0.025</td>
<td>0.009</td>
<td>42,939,496.740</td>
<td>0.010</td>
<td>0</td>
<td>0.016</td>
<td>0.043</td>
<td>5,367,437.109</td>
</tr>
<tr>
<td>$\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.025</td>
<td>0.020</td>
<td>0.017</td>
<td>40,442,780.560</td>
<td>0.027</td>
<td>0</td>
<td>0.032</td>
<td>0.157</td>
<td>5,055,347.605</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.031</td>
<td>0.026</td>
<td>0.054</td>
<td>39,139,447.734</td>
<td>0.065</td>
<td>0</td>
<td>0.016</td>
<td>0.081</td>
<td>4,892,431.001</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{M}_{1}$</td>
<td>0.024</td>
<td>0.015</td>
<td>0.024</td>
<td>30,725,288.732</td>
<td>0.002</td>
<td>0</td>
<td>0.009</td>
<td>0.003</td>
<td>3,840,661.101</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.011</td>
<td>0.012</td>
<td>0.016</td>
<td>30,070,222.565</td>
<td>0.104</td>
<td>0</td>
<td>0.007</td>
<td>0.005</td>
<td>3,758,777.840</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.020</td>
<td>0.012</td>
<td>0.011</td>
<td>24,788,961.061</td>
<td>0.004</td>
<td>0</td>
<td>0.008</td>
<td>0.014</td>
<td>3,098,620.141</td>
</tr>
<tr>
<td>$\mathcal{F}$</td>
<td>0.015</td>
<td>0.029</td>
<td>0.029</td>
<td>24,466,104.773</td>
<td>0.049</td>
<td>0.262</td>
<td>0.045</td>
<td>0.024</td>
<td>3,058,263.153</td>
</tr>
<tr>
<td>$\mathcal{M}_{2}$</td>
<td>0.039</td>
<td>0.025</td>
<td>0.031</td>
<td>17,202,228.824</td>
<td>0.026</td>
<td>0</td>
<td>0.034</td>
<td>0.069</td>
<td>2,150,278.631</td>
</tr>
<tr>
<td>$\mathcal{R}_{1}$</td>
<td>0.027</td>
<td>0.044</td>
<td>0.021</td>
<td>17,202,228.824</td>
<td>0.004</td>
<td>0</td>
<td>0.034</td>
<td>0.058</td>
<td>2,150,278.626</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{G}\mathcal{A}$</td>
<td>0.023</td>
<td>0.025</td>
<td>0.003</td>
<td>16,146,047.351</td>
<td>0.025</td>
<td>0</td>
<td>0.003</td>
<td>0.011</td>
<td>2,018,255.930</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.017</td>
<td>0.023</td>
<td>0.022</td>
<td>14,226,994.703</td>
<td>0.008</td>
<td>0.149</td>
<td>0.070</td>
<td>0.106</td>
<td>1,778,374.387</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.016</td>
<td>0.035</td>
<td>0.015</td>
<td>14,200,078.865</td>
<td>0.002</td>
<td>0</td>
<td>0.015</td>
<td>0.021</td>
<td>1,775,009.871</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.032</td>
<td>0.029</td>
<td>0.019</td>
<td>14,140,804.918</td>
<td>0.059</td>
<td>0</td>
<td>0.010</td>
<td>0.066</td>
<td>1,767,600.642</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{F}$</td>
<td>0.031</td>
<td>0.020</td>
<td>0.005</td>
<td>13,782,234.848</td>
<td>0.076</td>
<td>0</td>
<td>0.031</td>
<td>0.053</td>
<td>1,722,779.383</td>
</tr>
<tr>
<td>$\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.028</td>
<td>0.028</td>
<td>0.032</td>
<td>12,916,288.155</td>
<td>0.007</td>
<td>0</td>
<td>0.005</td>
<td>0.006</td>
<td>1,614,536.033</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.035</td>
<td>0.043</td>
<td>0.048</td>
<td>8,947,132.601</td>
<td>0.125</td>
<td>0</td>
<td>0.009</td>
<td>0.005</td>
<td>1,118,391.608</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.006</td>
<td>0.017</td>
<td>0.022</td>
<td>7,057,180.085</td>
<td>0.003</td>
<td>0</td>
<td>0.001</td>
<td>0.010</td>
<td>882,147.518</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{1}$</td>
<td>0.013</td>
<td>0.014</td>
<td>0.016</td>
<td>6,845,671.118</td>
<td>0.026</td>
<td>0</td>
<td>0.021</td>
<td>0.063</td>
<td>855,708.909</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.027</td>
<td>0.036</td>
<td>0.025</td>
<td>6,629,300.910</td>
<td>0.003</td>
<td>0</td>
<td>0.002</td>
<td>0.036</td>
<td>828,662.630</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.050</td>
<td>0.032</td>
<td>0.032</td>
<td>6,289,935.625</td>
<td>0.011</td>
<td>0</td>
<td>0.010</td>
<td>0.000</td>
<td>786,241.970</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.030</td>
<td>0.018</td>
<td>0.023</td>
<td>4,388,040.669</td>
<td>0.002</td>
<td>0</td>
<td>0.008</td>
<td>0.013</td>
<td>548,505.095</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{-1}$</td>
<td>0.023</td>
<td>0.028</td>
<td>0.008</td>
<td>3,501,920.426</td>
<td>0.026</td>
<td>0</td>
<td>0.004</td>
<td>0.009</td>
<td>437,740.065</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{M}_{2}$</td>
<td>0.013</td>
<td>0.033</td>
<td>0.036</td>
<td>3,196,468.004</td>
<td>0.007</td>
<td>0</td>
<td>0.007</td>
<td>0.026</td>
<td>399,558.516</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}\mathcal{e}\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.020</td>
<td>0.023</td>
<td>0.028</td>
<td>2,618,596.773</td>
<td>0.011</td>
<td>0</td>
<td>0.037</td>
<td>0.005</td>
<td>327,324.612</td>
</tr>
<tr>
<td>$\mathcal{R}_{-1}$</td>
<td>0.011</td>
<td>0.027</td>
<td>0.005</td>
<td>1,597,673.219</td>
<td>0.030</td>
<td>0</td>
<td>0.001</td>
<td>0.003</td>
<td>199,709.162</td>
</tr>
</tbody>
</table>

Table 11. Score-wise ranking of indices based on average of 5 regression techniques

implemented on the data sets including all the indices, coindices and reverse indices obtained previously as independent features and $HOF$ as dependent variable. From each regression technique absolute value of weight of each index is noted depicting its importance in predicting $HOF$. Further, the average scores of indices from each model was computed and ranked. We can easily see from the Table 11 that the top 10 indices namely $\mathcal{G}\mathcal{A}$,

![](./images/1064023331520380987_20.jpg)

Fig. 11. Average scores of indices based on different regression techniques

$\mathcal{RGA}$, $\mathcal{RABC}$, $\mathcal{RReZG}_{1}$, $\mathcal{ABC}$, $\mathcal{RR}_{-1}$, $\mathcal{CF}$, $\mathcal{CReZG}_{3}$, $\mathcal{RR}_{-1}$, $\mathcal{CM}_{2}$ are exactly the same as we detected in "Reliance of heat of formation on selected indices" section. Figure 11 illustrate our findings graphically.

In addition, we can see that the top two indices are $\mathcal{GA}$ and $\mathcal{RGA}$ which are the same indices we have recommended in "Reliance of heat of formation on selected indices" section as the most influential indices in the estimation of heat of formation. This result is further strengthened by analyzing the relationship of the indices, coindices and reverse indices via linear regression. Linear regression models between each index, coindex and reverse index vs $HOF$ was fitted and their corresponding root mean squared errors ($RMSE$) were noted. Table 12 provides the $RMSE$ score of linear fit between each index and $HOF$. Again, $\mathcal{GA}$ and $\mathcal{RGA}$ are taking the first two rankings verifying our results of the paper.

## Conclusion
This paper is focused on finding the best appropriate feature among topological indices, coindices, and reverse indices which might be used to exhibit various physio-chemical properties of $CaCl_2$. Firstly, different degree based topological indices, coindices, and reverse indices of the chemical graph of $CaCl_2$ were computed. Each computed index, coindex, and reverse index was regarded as a feature. Further, correlation among the features was depicted using heat map which clearly depicted the existence of multicollinearity in the data. To find the best appropriate features subset for the prediction of different physicochemical property was detected through Exhaustive Feature Selector. Top 10 indices were selected based on $R^2$-score. To make the features subset narrower, more analysis was conducted and $\mathcal{GA}$ and $\mathcal{RGA}$ were found to be the possible most influential features. The results were verified by implementing different regression techniques to predict heat of formation of $CaCl_2$ for $m \times n$ unit cells.

<table>
<thead>
<tr>
<th>Indices</th>
<th>RMSE</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mathcal{G}\mathcal{A}$</td>
<td>0.01115</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{G}\mathcal{A}$</td>
<td>0.042566</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.072088</td>
</tr>
<tr>
<td>$\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.097289</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.097605</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.106202</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{F}$</td>
<td>0.115678025</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{M}_{1}$</td>
<td>0.132918548</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.148270583</td>
</tr>
<tr>
<td>$\mathcal{M}_{1}$</td>
<td>0.15631424</td>
</tr>
<tr>
<td>$\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.1702674</td>
</tr>
<tr>
<td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.17441887</td>
</tr>
<tr>
<td>$\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.188241101</td>
</tr>
<tr>
<td>$\mathcal{F}$</td>
<td>0.195219407</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{F}$</td>
<td>0.260250195</td>
</tr>
<tr>
<td>$\mathcal{R}_{1}$</td>
<td>0.261644196</td>
</tr>
<tr>
<td>$\mathcal{M}_{2}$</td>
<td>0.261644196</td>
</tr>
<tr>
<td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.268918621</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{1}$</td>
<td>0.277996689</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{-1}$</td>
<td>0.27840745</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.289943873</td>
</tr>
<tr>
<td>$\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.291193762</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{M}_{2}$</td>
<td>0.295450878</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.321036794</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}_{1}$</td>
<td>0.339990036</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{\frac{1}{2}}$</td>
<td>0.369882248</td>
</tr>
<tr>
<td>$\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.386731572</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{2}$</td>
<td>0.528294106</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.532463053</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{M}_{1}$</td>
<td>0.53689769</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{R}e\mathcal{Z}\mathcal{G}_{3}$</td>
<td>0.540839723</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{A}\mathcal{B}\mathcal{C}$</td>
<td>0.642560314</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{G}\mathcal{A}$</td>
<td>0.650032145</td>
</tr>
<tr>
<td>$\mathcal{R}\mathcal{M}_{2}$</td>
<td>0.769856091</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}e\mathcal{Z}\mathcal{G}_{1}$</td>
<td>0.842935812</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{A}\mathcal{Z}\mathcal{I}$</td>
<td>0.849839949</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{-\frac{1}{2}}$</td>
<td>0.894442183</td>
</tr>
<tr>
<td>$\mathcal{C}\mathcal{R}_{-1}$</td>
<td>1.084791514</td>
</tr>
</tbody>
</table>

Table 12. RMSE of linear regression fits between indices and $HOF$

## Data availability
The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 11 July 2024; Accepted: 5 November 2024
Published online: 12 November 2024

## References
1.  Amić D., Bešlo, D., Lucić, B., Nikolić, S. & Trinajstić, N. The vertex-connectivity index revisited. *J. Chem. Inf. Comput. Sci.* **38(5)**, 819–822 (1998).
2.  Bollobás, B. & Erdos, P. Graphs of extremal weights. *Ars combinatoria* **50**, 225–233 (1998).
3.  Caporossi, G., Gutman, I., Hansen, P. & Pavlović, L. Graphs with maximum connectivity index. *J. Comput. Biol. Chem.* **27(1)**, 85–90 (2003).
4.  Gutman, I. et al. Graph theory and molecular orbitals. XII. Acyclic polyenes. *J. Chem. Phys.* **62(9)**, 3399–3405 (1975).

5. Gutman, I. & Trinajstić, N. Graph theory and molecular orbitals. Total electron energy of alternant hydrocarbons. *Chem. Phys. Lett.* **17(4)**, 535–538 (1972).
6. Kwun, Y. C., Munir, M., Nazeer, W., Rafique, S. & Kang, S. M. M-Polynomials and topological indices of V-Phenylenic Nanotubes and Nanotori. *Sci. Rep.* **7(1)**, 1–9 (2017).
7. Ranjini, P. S., Lokesha, V. & Usha, A. Relation between phenylene and hexagonal squeeze using harmonic index. *Int. J. Graph Theory* **1(4)**, 116–121 (2013).
8. Iqbal, Z., Ishaq, M., Aslam, A. & Gao, W. On eccentricity-based topological descriptors of water-soluble dendrimers. *Zeitschrift für Naturforschung C* **74(1–2)**, 25–33 (2019).
9. Li, X., Gutman, I. & Randić, M. *Mathematical aspects of Randić-type molecular structure descriptors* (University, Faculty of Science, 2006).
10. Estrada, E., Torres, L., Rodriguez, L. & Gutman, I. An atom-bond connectivity index: modelling the enthalpy of formation of alkanes. *Indian J. Chem.* **37A**, 849–855 (1998).
11. Vukičević, D. & Furtula, B. Topological index based on the ratios of geometrical and arithmetical means of end-vertex degrees of edges. *J. Math. Chem.* **46(4)**, 1369–1376 (2009).
12. Furtula, B. & Gutman, I. A forgotten topological index. *J. Math. Chem.* **53(4)**, 1184–1190 (2015).
13. Wang, D., Huang, Y. & Liu, B. Bounds on augmented zagreb index, MATCH. *Commun. Math. Comput. Chem.* **68**, 209–216 (2011).
14. Das, K. C. & Gutman, I. Some properties of the second Zagreb index. *MATCH Commun. Math. Comput. Chem* **52(1)**, 3–1 (2004).
15. Furtula, B., Gutman, I. & Ediz, S. On difference of Zagreb indices. *Discret. Appl. Math.* **178**, 83–88 (2014).
16. Gutman, I., Furtula, B., Vukicevic, Z. K. & Popivoda, G. On Zagreb indices and coindices. *MATCH Commun. Math. Comput. Chem* **74(1)**, 5–16 (2015).
17. Kulli, V. R. Reverse Zagreb and reverse hyper-Zagreb indices and their polynomials of rhombus silicate networks. *Annals Pure Appl. Math.* **16(1)**, 47–51 (2018).
18. Zaman, S., Rasheed, S. & Alamer, A. A quadratic regression model to quantify certain latest corona treatment drug molecules based on coindices of M-polynomial. *J. Supercomput.* 1–26 (2024).
19. Nadeem, M. F. et al. Topological aspects of metal-organic structure with the help of underlying networks. *Arab. J. Chem.* **14(6)**, 103–123 (2021).
20. Masmali, I., Azeem, M., Kamran Jamil, M., Ahmad, A. & Koam, A. N. Study of some graph theoretical parameters for the structures of anticancer drugs. *Sci. Rep.* **14(1)**, 13301 (2024).
21. Danish, M., Liaquat, T., Ashraf, F. & Zaman, S. Predictive modeling and regression analysis of diverse sulfonamide compounds employed in cancer therapy. *Front. Chem.* **12(1413850)**, 1–19 (2024).
22. Koam, A. N., Ahmad, A. & Nadeem, M. F. Comparative study of valency-based topological descriptor for hexagon star network. *Comput. Syst. Sci. Eng.* **36(2)**, 293–306 (2021).

## Author contributions
S.J. contributed to the supervision, conceptualization, and project administration. S.A. contributed to the data analysis, computation, methodology, and wrote the initial draft of the paper. N.S. investigated and analyzed the data curation. S.K. and M.K.S. critically analyzed the paper. B.G. contributed as a proof reader, formal analyzer and funder. All authors read and approved the final manuscript.

## Declarations

### Competing interests
The authors declare no competing interests.

### Additional information
Correspondence and requests for materials should be addressed to B.G.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2024