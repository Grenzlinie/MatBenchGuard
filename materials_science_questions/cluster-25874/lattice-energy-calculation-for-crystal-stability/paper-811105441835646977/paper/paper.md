![](./images/811105441835646977_1.jpg)

Subscriber access provided by University of Otago Library

# Estimation of Melting Temperature of Molecular Co-crystals using Artificial Neural Network Model

Rama Krishna Gamidi, and Åke C. Rasmuson

*Cryst. Growth Des.*, **Just Accepted Manuscript** • DOI: 10.1021/acs.cgd.6b01403 • Publication Date (Web): 29 Nov 2016

Downloaded from http://pubs.acs.org on December 1, 2016

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/811105441835646977_2.jpg)

Crystal Growth & Design is published by the American Chemical Society. 1155
Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Estimation of Melting Temperature of Molecular Co-crystals using Artificial Neural Network Model

Gamidi Rama Krishna and Åke. C. Rasmuson*

Department of Chemical and Environmental Science, Synthesis and Solid State Pharmaceutical Centre, Bernal Institute, University of Limerick, Limerick, Ireland

KEYWORDS. Database analysis, cocrystals, melting point, QSAR analysis, ANN models

ABSTRACT. A Quantitative Structure-activity Relationship (QSAR) model has been constructed by Artificial Neural Networks (ANNs) for estimation of melting temperature ($T$m) of molecular cocrystals (CCs). Based on a literature analysis using Scifinder and Cambridge Structural Database (CSD) softwares, a database has been created over CCs for four Active Pharmaceutical Ingredients (APIs), namely, *i.e.* caffeine (CAF), theophylline (THP), nicotinamide (NA) and isonicotinamide (INA). In total, of 61 CCs were included: 14-CAF, 9-THP, 29-INA and 9-NA. A good correlation was obtained with ANNs to quantify the $T$m of the CCs with respect to various coformers. The training process was completed with an average relative error of 2.38%, whereas the relative error for the validation set was 2.89%.

### Introduction

Approximately 40% of all drug molecules on the market are suffering from physico-chemical property (PCP) problems¹ such as low solubility² and dissolution rate,³ poor thermal stability⁴ and hygroscopicity,⁵ and tabletability etc.⁶ In general, the properties of drugs largely depend upon the molecular arrangement and intermolecular forces within the solid material. Therefore, control over the PCP of the drugs can be exercised through control over the interactions present within the solid form. Both academia and the pharmaceutical industry are targeting such PCP problems by employing various strategies like formation of cocrystals (CCs),⁷ salts,⁸ hydrates⁹ and solvates.¹⁰ It has been suggested that formation of CCs¹¹ is the best approach to modify the PCPs without modifying their covalent bonds of the drug molecules. Moreover, the formation of CCs is particularly useful for cases where the drug molecule suffers with PCP issues, due to the presence of non-ionisable functional groups. The number of available CC formers listed as GRAS (Generally Recognized As Safe) is very large. Even though there are many studies on CCs, little work has been done for identification of an ideal coformer for improving the desired PCP quantitatively. Development of methods for such identification would make the search for a suitable coformers to set the PCP within the target range, in a more effective way.

There are a number of approaches in the literature to guide the work of finding coformers for the formation of CCs such as supramolecular synthon approach,¹² $\Delta$pKa rule,¹³ Fabians approach,¹⁴ Hansen solubility approach,¹⁵ COSMO-RS virtual cocrystal screening through molecular electrostatic potential surfaces and lattice energy calculations.¹⁶ However, there is not much studies on prediction of PCP of molecular CCs with respect to coformer properties. In 2003, Vishweshwar et al.¹⁷ investigated the alteration of the melting temperature ($Tm$) of

cocrystals, by considering five homologous series of (diacid).(IN)₂ CCs as model components. The *Tm* of CCs is higher for even number of carbon atoms than for odd number of carbon atoms of diacid coformers. Even number carbon atoms diacids can pack themselves more densely than the odd number of carbon atoms diacids where small voids are formed. In another example, Aakeröy et al.¹⁸, ¹⁹ found that the *Tm* and aqueous solubility of the CCs of Bis(pyridinecarboxamido)alkane with aliphatic dicarboxylic acid coformers, can be predicted in cases where the CC crystal packing arrangement systematically change within a series of coformers. Thereafter, Báthori et al.²⁰ studied the *Tm* behavior and partial aqueous solubility, as a function of O⋯H and C⋯H intermolecular interaction percentage. By using a FLEXCRYST program suite, Kuleshova et al.²¹ has estimated the relative stability and the solubility of flavonoid’s CCs with respect to their pure solid forms etc. Most recently Perlovich²² developed an approach to estimate thermodynamic properties of the CCs based on a diagram method, and derived a correlation equation to relate the *Tm* of the CCs to various coformers.

There are several linear and nonlinear regression methods, which are used extensively for the prediction of properties of compounds, from molecular geometric parameters.²³, ²⁴, ²⁵, ²⁶ Artificial Neural Network approaches (ANNs) have been found to be more robust and are fast growing statistical machine learning methods²⁷ to construct a model for complex or nonlinear systems. Thus, ANN methods are preferable to solve a wide variety of tasks that are hard to solve using traditional rule-based programming, as in the field of chemical engineering for correlation of different parameters,²⁸ system control and for the prediction of properties, etc.²⁹, ³⁰ Furthermore, ANNs have been used for the prediction of *Tm* of organic compounds by quantitative structure-property relationship (QSPR) analysis.³¹, ³², ³³ Construction of a model for prediction of *Tm* of a single component is a difficult task, because, it depends upon various

parameters such as the crystal packing arrangement, molecular conformation and strength of inter/intra molecular hydrogen bonding (packing motifs) present in the crystal. Construction of a model for prediction of Tm of CCs with respect to coformer structure present in the CCs becomes even more difficult task.

In the present work, a QSAR analysis is undertaken using a robust ANNs for development of a better understanding of how the Tm of CCs of the same API depends on the properties of the different coformers. The practical advantage with ANNs is that, it is a computer modeling approach that does not require a prior knowledge of the actual process (the factors which are involved in the CC formation), but, the models are built by considering available knowledge of the components involved, and the building of an activation/transfer function would transfer the input parameters into the output parameter's of our interest (through a number of iterations to reduce the prediction error). Moreover, ANNs could give us Tm values of the CCs, quantitatively (instead of an equation or graphical representation) which is not possible by earlier proposed prediction methods.

Thus, aiming to construct a model for the prediction of Tm of the CCs using ANN methods, we have been selected and created a database of in total 61 CCs Tm of four different APIs (9-THP, 14-CAF, 29-INA and 9-NA). Lattice energies (Elatt) were calculated for all selected CCs and individual components. Using eight parameters as input neurons, we have succeeded to construct an ANN QSAR model to predict the melting point of the cocrystals.

## Methods and Calculations

Artificial Neural Network Modelling: The architecture of the constructed ANN model is composed of an input layer, a hidden layer(s), weights, a sum function, an activation function

and an output layer, as is illustrated in Figure 1. Each connection has some numeric weights that can be tuned based on trial and error, to make them adaptable to inputs and capable of learning.

A multi-layer feed-forward ANN model was used, where back-propagation of error algorithm (supervised learning) is employed to calculate ANN weights, because, multi-layers of neurons with nonlinear transfer (activation) function allow the network to efficiently learn (non)linear relationships between input and output vectors. To train the model, eight input parameters used are assumed to be those more influential on the Tm of CCs. These parameters are: the lattice energy of the CCs (CC$_{Elatt}$), ratio of the electrostatic interaction percentage of the CC *vs* the vdWs interaction percentage (CC$_{Eel/Evdw}$) (see Table S1), the total molecular weight of the CCs (CC$_{MW}$) (see Table S1), the ratio of molecular weight of API *vs* the molecular weight of the coformer (API$_{MW}$/CF$_{MW}$) (see Table S1), $\Delta$pKa values ($\Delta$pKa values for the 61CC complexes were calculated (base/acid), where $\Delta$pKa = pKa (base) - pKa (acid) based on pKa values.$^{13}$ For complexes involving two acids, the pKa of the more basic compound (with more basic substituent's) is taken as pKa (base)) of the CC (CC$_{\Delta\text{pKa}}$), crystal packing density of the CC (CC$_{CPD}$) (see Table S1), melting temperature of the API (API$_{Tm}$), and melting temperature of the coformer (CF$_{Tm}$). Moreover, to set an ANN QSAR model of 61 CCs with a good generalization capability, the data points were divided into two sets i) 55 data points for the training set and ii) 6 data points for the validation set (one system from each of THP, CAF and NA (Saccharin (SA), 4-Fluoro-3-nitro aniline (4F3NAN) and Glutaric acid (GTA) respectively); three from INA (Adipic acid (ADP), 4-hydroxy benzoic acid (4HBA) and Glutaric acid (GTA))).

In the training of the model, weight parameters were adjusted iteratively to minimize the criterion function. The attributes which are present in the input/output vectors were normalized between 0 and 1 (within the limits of the sigmoid transfer function *i.e.*, logsig). The neurons

present in the input layer (eight parameters) fed-in through connections with some weights used from -0.5 to +0.5, here, the value's 0.3 is used as for the learning parameters and 0.5 for the momentum. The total weight of the input layer is nothing but the weighted sum of the inputs from all the eight input parameters. Each neuron in the input layer is connected to all neurons in the hidden layer, thereafter, the neurons present in the hidden layer will transfer the information to output layer property, i.e., Tm of the CCs through transfer/activation function. The choice of hidden layer(s) and the number of network parameters used here was largely attained by a trail-and-error process. However, we succeeded to get the best results with one hidden layer which contains 8 neurons, the same number of neurons as present in the input variables (eight). Kolmogotov theorem states that < 2 hidden layers are sufficient to build a model for any problem.³⁴ Because, the higher number of hidden layers (more than two) causes to increase the number of weight parameters which leads to over-fitting and poor generalization capability of the model. For avoiding such issues, eight neurons were used for the generation of a hidden layer.

To set the global minimum of an objective function after completion of fully converged iterations, the momentum parameter value varied from 0.3 to 0.2. Thus, the back propagation algorithm modifies network weight parameters to minimize the mean squared error between the desired and the actual outputs of the network. To avoid the over-fitting of the model, the root-mean-square error, correlation coefficient, and average absolute error was calculated for each trial on the training set and validation set. For processing the neurons present in the different layers within the network, the sigmoid transfer function was used as an activation function (has smooth and easily differentiable feature). To build and train the ANNs model, both, Neural network software³⁵ package and MATLAB (R2015b, MathWorks) were employed.

![](./images/811105441835646977_3.jpg)

Figure 1. The architecture of constructed ANN models, consists of three main layers, input, hidden and output layer. The input layer is used to introduce the input variables to the network and output layer represents predictions of the response variables calculated by ANN.

## Database Creation

A database over cocrystals of four different APIs, namely, caffeine (CAF), theophylline (THP), nicotinamide (NA) and isonicotinamide (INA) has been created by using the Scifinder and the Cambridge Structural Database softwares (CSD version 5.37, update 1 (Nov 2015). Initial search on Scifinder identified various cocrystals of each system which were then searched for in the CSD to find the structural features of each system. The data available at both Scifinder and CSD were considered to be more reliable. We have found several cocrystal reports in the literature on these four APIs, from which, Tm of the CCs and individual components were extracted. The Tm values used are onset values, and were determined by Differential Scanning Calorimetry. Among

all the different cocrystals reported on these four APIs, we have been selected 61 CCs based on the reliability of data. Priority has been given to the systems where both single crystal X-Ray diffraction data (SC-XRD) and DSC data are available. Accordingly, cocrystals where only PXRD data are available were not included. On the other hand, we did not make the restriction to consider the different stoichiometric ratio's and CC polymorphs of the same pair of components.

![](./images/811105441835646977_4.jpg)

Scheme 1. (a) Schematic representation of methodology (b) Chemical structures of the four APIs included.

Lattice energy calculations

Lattice energies (Elatt) for all 61 CCs were calculated by using the COMPASS II forcefield as implemented in the Forcite module of the Material Studio (Accerlys Inc.) software. In that, both electrostatic and vdWs interactions are calculated by the atom based method. Initially, crystallographic information files (cif) for CCs were extracted from the CSD software (Refcodes are provided in the Table 1), and were used as such for Elatt calculations. Energies were calculated in fully relaxed geometries using the periodic boundary conditions in all directions.

Table 1. The 61CCs used in this study, respective CSD refcodes, stoichiometric ratios, $\Delta pKa$ and Elatt.

<table>
  <thead>
    <tr>
      <th>Name of the Component</th>
      <th>Code</th>
      <th>pKa</th>
      <th>Cocrystal</th>
      <th>$\Delta pKa$</th>
      <th>$E_{latt}$ of CCs<br>(Kcal/mol)</th>
      <th>Ratio</th>
      <th>Cocrystal Refcode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Caffeine</td>
      <td>CAF</td>
      <td>0.7 (cb)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Theophylline</td>
      <td>THP</td>
      <td>1.7 (cb)<br>8.77 (ca)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Isonicotinamide</td>
      <td>INA</td>
      <td>3.61<br>10.61</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Nicotinamide</td>
      <td>NA</td>
      <td>3.35</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>DL-Malic acid</td>
      <td>DLMA</td>
      <td>3.40<br>5.11</td>
      <td>THP:DLMA</td>
      <td>-1.7<br>-3.66</td>
      <td>-67.876</td>
      <td>1:1</td>
      <td>CIZTAH</td>
    </tr>
    <tr>
      <td>D-Malic acid</td>
      <td>DMA</td>
      <td>3.40<br>5.11</td>
      <td>THP:DMA</td>
      <td>-1.7<br>-3.66</td>
      <td>-67.197</td>
      <td>1:1</td>
      <td>CODCOO</td>
    </tr>
    <tr>
      <td>Glutaric acid</td>
      <td>GTA</td>
      <td>4.31<br>5.41</td>
      <td>THP:GTA</td>
      <td>-2.6<br>-3.36</td>
      <td>-60.167</td>
      <td>1:1</td>
      <td>XEJXIU</td>
    </tr>
    <tr>
      <td>Gentisic acid</td>
      <td>GNA</td>
      <td>2.97</td>
      <td>THP:GNA</td>
      <td>-1.27</td>
      <td>-63.764</td>
      <td>1:1</td>
      <td>DUCROJ</td>
    </tr>
    <tr>
      <td>Salicylic acid</td>
      <td>SA</td>
      <td>2.97<br>13.82</td>
      <td>THP:SA</td>
      <td>-1.27<br>-12.12</td>
      <td>-55.419</td>
      <td>1:1</td>
      <td>KIGLES</td>
    </tr>
    <tr>
      <td>p-coumaric acid-I</td>
      <td>PCA-I</td>
      <td>4<br>9.51 *M</td>
      <td>THP:PCA-I</td>
      <td>-2.3<br>-7.81</td>
      <td>-64.651</td>
      <td>1:1</td>
      <td>IJIBEI</td>
    </tr>
    <tr>
      <td>p-coumaric acid-II</td>
      <td>PCA-II</td>
      <td>"</td>
      <td>THP:PCA-II</td>
      <td>"</td>
      <td>-63.937</td>
      <td>1:1</td>
      <td>IJIBEI01</td>
    </tr>
    <tr>
      <td>Saccharin</td>
      <td>SAC</td>
      <td>11.68</td>
      <td>THP:SAC</td>
      <td>-9.98</td>
      <td>-59.602</td>
      <td>1:1</td>
      <td>XOBCUN</td>
    </tr>
    <tr>
      <td>Urea</td>
      <td>URE</td>
      <td>0.10</td>
      <td>THP:URE</td>
      <td>1.60</td>
      <td>-52.728</td>
      <td>1:1</td>
      <td>DUXZAX</td>
    </tr>
    <tr>
      <td>Glutaric acid</td>
      <td>GTA-I</td>
      <td>4.31<br>5.41</td>
      <td>CAF:GTA-I</td>
      <td>-3.61<br>-4.71</td>
      <td>-59.068</td>
      <td>1:1</td>
      <td>EXUQUJ01</td>
    </tr>
    <tr>
      <td>Glutaric acid</td>
      <td>GTA-II</td>
      <td>"</td>
      <td>CAF:GTA-II</td>
      <td>"</td>
      <td>-59.512</td>
      <td>1:1</td>
      <td>EXUQUJ</td>
    </tr>
    <tr>
      <td>p-coumaric acid</td>
      <td>PCA</td>
      <td>4<br>9.51 *M</td>
      <td>CAF:PCA</td>
      <td>-2.3<br>-7.81</td>
      <td>-63.746</td>
      <td>1:1</td>
      <td>IJEZUT</td>
    </tr>
    <tr>
      <td>4-nitroaniline</td>
      <td>4NAN</td>
      <td>1</td>
      <td>CAF:4NAN</td>
      <td>-0.3</td>
      <td>-53.417</td>
      <td>1:1</td>
      <td>LATGUK</td>
    </tr>
  </tbody>
</table>

<table>
<tbody>
<tr>
<td>
2-iodo-4-nitroaniline
</td>
<td>
2I4NAN
</td>
<td>
0.46 *M
</td>
<td>
CAF:2I4NAN
</td>
<td>
0.24
</td>
<td>
-49.364
</td>
<td>
1:1
</td>
<td>
LATFUJ
</td>
</tr>
<tr>
<td>
2-fluoro-5-nitroaniline
</td>
<td>
2F5NAN
</td>
<td>
0.52 *M
</td>
<td>
CAF:2F5NAN
</td>
<td>
0.18
</td>
<td>
-52.866
</td>
<td>
1:1
</td>
<td>
LATHEV
</td>
</tr>
<tr>
<td>
4-fluoro-3-nitroaniline
</td>
<td>
4F3NAN
</td>
<td>
1.42 *M
</td>
<td>
CAF:4F3NAN
</td>
<td>
-0.72
</td>
<td>
-52.236
</td>
<td>
1:1
</td>
<td>
LATGIY
</td>
</tr>
<tr>
<td>
4-chloro-3-nitroaniline
</td>
<td>
4C3NAN
</td>
<td>
1.90
</td>
<td>
CAF:4C3NAN
</td>
<td>
-1.2
</td>
<td>
-57.170
</td>
<td>
1:1
</td>
<td>
LATGEU
</td>
</tr>
<tr>
<td>
2-chloro-5-nitroaniline
</td>
<td>
2C5NAN
</td>
<td>
0.40 *M
</td>
<td>
CAF:2C5NAN
</td>
<td>
0.3
</td>
<td>
-53.369
</td>
<td>
1:1
</td>
<td>
LATGOE
</td>
</tr>
<tr>
<td>
4-iodo-3-nitroaniline
</td>
<td>
4I3NAN
</td>
<td>
1.28 *M
</td>
<td>
CAF:4I3NAN
</td>
<td>
-0.58
</td>
<td>
-55.371
</td>
<td>
1:1
</td>
<td>
LATGAQ
</td>
</tr>
<tr>
<td>
2,4-dinitrobenzoic acid
</td>
<td>
24DNBA
</td>
<td>
1.43
</td>
<td>
CAF:24DNBA
</td>
<td>
-0.73
</td>
<td>
-61.841
</td>
<td>
1:1
</td>
<td>
LATHAR
</td>
</tr>
<tr>
<td>
2-fluoro-5-nitrobenzoic acid
</td>
<td>
2F5NBA
</td>
<td>
2.69 *M
</td>
<td>
CAF:2F5NBA
</td>
<td>
-1.99
</td>
<td>
-57.534
</td>
<td>
1:1
</td>
<td>
LATHIZ
</td>
</tr>
<tr>
<td>
Salicylic acid
</td>
<td>
SA
</td>
<td>
2.98
</td>
<td>
CAF:SA
</td>
<td>
-2.28
</td>
<td>
-54.979
</td>
<td>
1:1
</td>
<td>
XOBCAT
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
13.82
</td>
<td>
</td>
<td>
-13.12
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Salicylic acid_I
</td>
<td>
SA-I
</td>
<td>
"
</td>
<td>
CAF:SA-I
</td>
<td>
"
</td>
<td>
-54.990
</td>
<td>
1:1
</td>
<td>
XOBCAT01
</td>
</tr>
<tr>
<td>
Oxalic acid
</td>
<td>
OXA
</td>
<td>
1.23
</td>
<td>
INA:OXA
</td>
<td>
2.38
</td>
<td>
-84.971
</td>
<td>
2:1
</td>
<td>
ULAWAF
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
4.19
</td>
<td>
</td>
<td>
-0.58
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Malonic acid
</td>
<td>
MLA
</td>
<td>
2.83
</td>
<td>
INA:MLA
</td>
<td>
0.78
</td>
<td>
-126.336
</td>
<td>
2:1
</td>
<td>
ULAWEJ
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.69
</td>
<td>
</td>
<td>
-2.08
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Succinic acid
</td>
<td>
SCA
</td>
<td>
4.16
</td>
<td>
INA:SCA
</td>
<td>
-0.55
</td>
<td>
-85.669
</td>
<td>
2:1
</td>
<td>
LUNNUD
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.61
</td>
<td>
</td>
<td>
-2
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Glutaric acid
</td>
<td>
GTA
</td>
<td>
4.31
</td>
<td>
INA:GTA
</td>
<td>
-0.7
</td>
<td>
-56.894
</td>
<td>
1:1
</td>
<td>
ULAXAG
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.41
</td>
<td>
</td>
<td>
-1.8
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Adipic acid
</td>
<td>
ADA
</td>
<td>
4.43
</td>
<td>
INA:ADA
</td>
<td>
-0.82
</td>
<td>
-57.713
</td>
<td>
1:1
</td>
<td>
ULAXEK
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.41
</td>
<td>
</td>
<td>
-1.8
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Pimelic acid
</td>
<td>
PIA
</td>
<td>
4.71
</td>
<td>
INA:PIA
</td>
<td>
-1.1
</td>
<td>
-58.609
</td>
<td>
1:1
</td>
<td>
ISIJEA
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.58
</td>
<td>
</td>
<td>
-1.97
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Suberic acid
</td>
<td>
SUA
</td>
<td>
4.52
</td>
<td>
INA:SUA
</td>
<td>
-0.91
</td>
<td>
-62.187
</td>
<td>
1:1
</td>
<td>
ISIJIE
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.49
</td>
<td>
</td>
<td>
-1.88
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Azelaic acid
</td>
<td>
AZA
</td>
<td>
4.550
</td>
<td>
INA:AZA
</td>
<td>
-0.94
</td>
<td>
-61.805
</td>
<td>
1:1
</td>
<td>
ISIJAW
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
5.498
</td>
<td>
</td>
<td>
-1.88
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Fumaric acid
</td>
<td>
FUA
</td>
<td>
3.03
</td>
<td>
INA:FUA
</td>
<td>
0.58
</td>
<td>
-84.215
</td>
<td>
2:1
</td>
<td>
LUNNOX
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
4.44
</td>
<td>
</td>
<td>
-0.83
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
4-ketopimelic acid
</td>
<td>
4KPIA
</td>
<td>
3.68 *M
</td>
<td>
INA:4KPA
</td>
<td>
-0.07
</td>
<td>
-91.711
</td>
<td>
2:1
</td>
<td>
LUNNIR
</td>
</tr>
</tbody>
</table>

<table>
  <tr>
    <td></td>
    <td></td>
    <td>4.42 *M</td>
    <td></td>
    <td>-0.81</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>12-bromododecanoic acid</td>
    <td>12BDA</td>
    <td>4.95 *M</td>
    <td>INA:12BDA</td>
    <td>-1.34</td>
    <td>-62.859</td>
    <td>1:1</td>
    <td>LUNMUC</td>
  </tr>
  <tr>
    <td>Salicylic acid</td>
    <td>SA</td>
    <td>2.98</td>
    <td>INA:SA</td>
    <td>0.63</td>
    <td>-50.890</td>
    <td>1:1</td>
    <td>XAQQEM</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>13.82</td>
    <td></td>
    <td>-10.21</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3-hydroxybenzoic acid</td>
    <td>3HBA</td>
    <td>4.06</td>
    <td>INA:3HBA</td>
    <td>-0.45</td>
    <td>-53.994</td>
    <td>1:1</td>
    <td>LUNMEM</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>9.92</td>
    <td></td>
    <td>-6.31</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4-hydroxybenzoic acid</td>
    <td>4HBA</td>
    <td>4.48</td>
    <td>INA:4HBA</td>
    <td>-0.87</td>
    <td>-55.167</td>
    <td>1:1</td>
    <td>VAKTOR</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>9.32</td>
    <td></td>
    <td>-5.71</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4-fluorobenzoic acid</td>
    <td>4FBA</td>
    <td>4.15</td>
    <td>INA:4FBA</td>
    <td>-0.54</td>
    <td>-49.167</td>
    <td>1:1</td>
    <td>ASA XUN01</td>
  </tr>
  <tr>
    <td>3-nitrobenzoic acid</td>
    <td>3NBA</td>
    <td>3.47</td>
    <td>INA:3NBA</td>
    <td>0.14</td>
    <td>-54.057</td>
    <td>1:1</td>
    <td>ASA XOH</td>
  </tr>
  <tr>
    <td>2-hexeneoic acid</td>
    <td>2HEA</td>
    <td>5.13 *M</td>
    <td>INA:2HEA</td>
    <td>-1.52</td>
    <td>-48.183</td>
    <td>1:1</td>
    <td>AJAKAX</td>
  </tr>
  <tr>
    <td>Cinnamic acid</td>
    <td>CIA</td>
    <td>3.89 (cis)</td>
    <td>INA:CIA</td>
    <td>-0.28</td>
    <td>-52.787</td>
    <td>1:1</td>
    <td>LUNMAI</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>4.44 (trans)</td>
    <td></td>
    <td>-0.83</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Chloroacetic acid</td>
    <td>CAA</td>
    <td>2.85</td>
    <td>INA:CAA</td>
    <td>0.76</td>
    <td>-44.004</td>
    <td>1:1</td>
    <td>LUNNAJ</td>
  </tr>
  <tr>
    <td>(RS)-2-phenylpropionic acid</td>
    <td>2PPARS</td>
    <td>4.34</td>
    <td>INA:2PPARS</td>
    <td>-0.73</td>
    <td>-48.773</td>
    <td>1:1</td>
    <td>ROLFOO</td>
  </tr>
  <tr>
    <td>(R)-2-phenylpropionic acid</td>
    <td>2PPAR</td>
    <td>4.34</td>
    <td>INA:2PPAR</td>
    <td>-0.73</td>
    <td>-48.469</td>
    <td>1:1</td>
    <td>RONDAA</td>
  </tr>
  <tr>
    <td>dl-mandelic acid</td>
    <td>DLMDA</td>
    <td>3.85</td>
    <td>INA:DLMDA</td>
    <td>-0.24</td>
    <td>-56.255</td>
    <td>1:1</td>
    <td>LUNPAL</td>
  </tr>
  <tr>
    <td>Clofibridic acid</td>
    <td>CFA</td>
    <td>3.0</td>
    <td>INA:CFA</td>
    <td>0.61</td>
    <td>-54.279</td>
    <td>1:1</td>
    <td>UMUYUX</td>
  </tr>
  <tr>
    <td>Resorcinol</td>
    <td>REOL</td>
    <td>9.32</td>
    <td>INA:REOL</td>
    <td>-5.71</td>
    <td>-77.890</td>
    <td>2:1</td>
    <td>VAKTUX</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>11.1</td>
    <td></td>
    <td>-7.49</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hydroquinone</td>
    <td>HQ</td>
    <td>9.85</td>
    <td>INA:HQ</td>
    <td>-6.24</td>
    <td>-76.792</td>
    <td>2:1</td>
    <td>VAKVIN</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>11.4</td>
    <td></td>
    <td>-7.79</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3-(N,N-dimethylamino)benzoic acid</td>
    <td>3NNDMABA</td>
    <td>3.76 *M</td>
    <td>INA:3NNDMABA</td>
    <td>-0.15</td>
    <td>-51.969</td>
    <td>1:1</td>
    <td>LUNMIQ</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>4.92 *M</td>
    <td></td>
    <td>-1.31</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3,5-bis(trifluoromethyl)benzoic acid</td>
    <td>35TFMBA</td>
    <td>3.81 *M</td>
    <td>INA:35TFMBA</td>
    <td>-0.2</td>
    <td>-51.324</td>
    <td>1:1</td>
    <td>LUNMOW</td>
  </tr>
  <tr>
    <td>Meclofenamic acid</td>
    <td>MEFA</td>
    <td>3.79</td>
    <td>INA:MEFA</td>
    <td>-0.18</td>
    <td>-62.583</td>
    <td>1:1</td>
    <td>SAXPAK</td>
  </tr>
  <tr>
    <td>Fumaric acid monoethyl ester</td>
    <td>FAMEE</td>
    <td>3.48 *M</td>
    <td>INA:FAMEE</td>
    <td>0.13</td>
    <td>-51.755</td>
    <td>1:1</td>
    <td>LUNNEN</td>
  </tr>
  <tr>
    <td>Fumaric acid</td>
    <td>FUA</td>
    <td>3.03</td>
    <td>NA:FUA</td>
    <td>0.32</td>
    <td>-54.457</td>
    <td>1:1</td>
    <td>NUKYAU</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>4.44</td>
    <td></td>
    <td>-1.09</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

<table>
<tbody>
<tr>
<td>Glutaric acid</td>
<td>GTA</td>
<td>4.31</td>
<td>NA:GTA</td>
<td>-0.96</td>
<td>-57.708</td>
<td>1:1</td>
<td>NUKYEY</td>
</tr>
<tr>
<td></td>
<td></td>
<td>5.41</td>
<td></td>
<td>-2.06</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>4-hydroxybenzoic acid</td>
<td>4HBAII</td>
<td>4.48</td>
<td>NA:4HBAII</td>
<td>-1.13</td>
<td>-53.731</td>
<td>1:1</td>
<td>RUYHEZ01</td>
</tr>
<tr>
<td></td>
<td></td>
<td>9.32</td>
<td></td>
<td>-5.97</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ethyl paraben</td>
<td>EPB</td>
<td>8.34</td>
<td>NA:EPB</td>
<td>-4.99</td>
<td>-51.664</td>
<td>1:1</td>
<td>GOGQID</td>
</tr>
<tr>
<td>2-chloro-4-nitrobenzoic acid</td>
<td>2C4NBA</td>
<td>0.94</td>
<td>NA:2C4NBA</td>
<td>2.41</td>
<td>-54.546</td>
<td>1:1</td>
<td>SUTTUX</td>
</tr>
<tr>
<td>Tolfenamic acid</td>
<td>TOFA</td>
<td>3.88</td>
<td>NA:TOFA</td>
<td>-0.53</td>
<td>-87.578</td>
<td>2:1</td>
<td>EXAQIE</td>
</tr>
<tr>
<td>Mefenamic acid</td>
<td>MEFA</td>
<td>3.79</td>
<td>NA:MEFA</td>
<td>-0.44</td>
<td>-85.931</td>
<td>2:1</td>
<td>EXAQOK</td>
</tr>
<tr>
<td>Niflumic acid</td>
<td>NIFA</td>
<td>1.88</td>
<td>NA:NIFA</td>
<td>1.47</td>
<td>-62.731</td>
<td>1:1</td>
<td>EXAQEA</td>
</tr>
<tr>
<td>Furosemide</td>
<td>FURA</td>
<td>4.25</td>
<td>NA:FURA</td>
<td>-0.9</td>
<td>-76.015</td>
<td>1:1</td>
<td>YASGOQ</td>
</tr>
</tbody>
</table>

Note-¹ It is noteworthy to mention that some of the pKa values which we used were extracted from the literature and the compounds which does not have the pKa values were calculated by using the Marvin software (which are marked as *M in the table). These 61CCs systems cover a wide range of $\Delta$pKa from -9.98 to +2.41, between the acceptor and donor functional groups.

²ca-conjugate acid value, whereas cb-conjugate base value

## Results and Discussion

### Data collection and database creation

For the four APIs,189 entries on CAF were found, 114 entries on THP, 449 entries on NA and 351 entries on INA, belonging to various classes of components, Table 2. Organic binary (two-component) systems such as anhydrous CCs are our main interest. In this category, as listed in the Table 2, 80 entries on CAF, 38 on THP, 85 on NA, and 113 entries on INA system, are available in the CSD software, in total, 316 binary CCs entries. In the second step a literature survey on properties of the CCs and the pure drug molecules allowed us to create a database for Tm of the CCs and their individual coformers and APIs. In the material we find

several cases where the properties of the CCs have improved over those of the pure API, e.g. hygroscopicity, physical stability, thermal stability, nonlinear optical property, solubility, dissolution rate and bioavailability, and tabletability, etc. For creation of the database 61 CCs were selected out of the 316 to maintain high data reliability. Such as where the cocrystals systems which were characterized by both SC-XRD as well as by DSC experiments, has given the highest priority.²² The selected number on each system and stoichiometric ratio's were as follows: CAF-14 (1:1 ratio), THP-9 (1:1 ratio), NA-9 ((1:1) ratio-7; (2:1) ratio-02) and INA-29 ((1:1) ratio-22; (2:1) ratio-07). As a whole, 85% of the CCs have a (1:1) stoichiometric ratio, and the rest have a (2:1) stoichiometric ratio.

Table 2. Information about the CSD analysis (CSD version 5.37, update 1 (Nov 2015) on CAF, THP, NA and INA.

<table>
<thead>
<tr>
<th>Name of the category</th>
<th colspan="3">CAF</th>
<th colspan="3">THP</th>
<th colspan="4">NA</th>
<th colspan="3">INA</th>
</tr>
</thead>
<tbody>
<tr>
<td>Total no. of entries</td>
<td colspan="3">189</td>
<td colspan="3">114</td>
<td colspan="4">449</td>
<td colspan="3">351</td>
</tr>
<tr>
<td>Organic</td>
<td colspan="3">156</td>
<td colspan="3">87</td>
<td colspan="4">180</td>
<td colspan="3">184</td>
</tr>
<tr>
<td>Other entries</td>
<td colspan="3">33</td>
<td colspan="3">27</td>
<td colspan="4">269</td>
<td colspan="3">167</td>
</tr>
<tr>
<td>Polymorphs</td>
<td colspan="3">06</td>
<td colspan="3">07</td>
<td colspan="4">07</td>
<td colspan="3">06</td>
</tr>
<tr>
<td>Solvates</td>
<td colspan="3">06</td>
<td colspan="3">01</td>
<td colspan="4">02</td>
<td colspan="3">03</td>
</tr>
<tr>
<td>Hydrates</td>
<td colspan="3">02</td>
<td colspan="3">05</td>
<td colspan="4">-</td>
<td colspan="3">03</td>
</tr>
<tr>
<td>Salts</td>
<td colspan="3">02</td>
<td colspan="3">03</td>
<td colspan="4">18</td>
<td colspan="3">19</td>
</tr>
<tr>
<td>Total no. of anhy. CCs</td>
<td colspan="3">80</td>
<td colspan="3">41</td>
<td colspan="4">92</td>
<td colspan="3">119</td>
</tr>
<tr>
<td></td>
<td>Binary</td>
<td colspan="2">Ternary</td>
<td>Binary</td>
<td colspan="2">Ternary</td>
<td>Binary</td>
<td colspan="3">Ternary</td>
<td>Binary</td>
<td colspan="2">Ternary</td>
</tr>
<tr>
<td></td>
<td>80</td>
<td colspan="2">-</td>
<td>38</td>
<td colspan="2">03</td>
<td>85</td>
<td colspan="3">06</td>
<td>113</td>
<td colspan="2">06</td>
</tr>
<tr>
<td>Ratio of binary CCs</td>
<td>1:1</td>
<td>1:2</td>
<td>2:1</td>
<td>1:1</td>
<td>1:2</td>
<td>2:1</td>
<td>1:1</td>
<td>1:2</td>
<td>2:1</td>
<td>4:1</td>
<td>1:1</td>
<td>1:2</td>
<td>2:1</td>
</tr>
<tr>
<td></td>
<td>64</td>
<td>02</td>
<td>14</td>
<td>33</td>
<td>01</td>
<td>04</td>
<td>66</td>
<td>06</td>
<td>12</td>
<td>01</td>
<td>84</td>
<td>05</td>
<td>24</td>
</tr>
<tr>
<td>No. of CCs used for PCP studies</td>
<td colspan="3">39</td>
<td colspan="3">19</td>
<td colspan="4">40</td>
<td colspan="3">44</td>
</tr>
<tr>
<td>No. of CCs used for structural features of CCs</td>
<td colspan="3">41</td>
<td colspan="3">19</td>
<td colspan="4">45</td>
<td colspan="3">69</td>
</tr>
</tbody>
</table>

<table>
  <tr>
    <td>Combinations (salts, hydrates, CC, solvates and hydrates etc)</td>
    <td>60</td>
    <td>30</td>
    <td>62</td>
    <td>34</td>
  </tr>
</table>

Among the selected 61 cocrystals 57.5% have $Tm$ in-between the $Tm$ of the individual components (category I), 26% of the CCs have the $Tm$ lower than those of both API and conformer (category II) and remaining 16.5% of the CCs have the $Tm$ higher than those of the both API and individual components (category III), as given in Table 3 and illustrated in Figure 1. The classification and the percentages have matched previous studies.$^{22}$

![](./images/811105441835646977_5.jpg)

Figure 2. Information about the different categories and their relative percentages of the $Tm$ of the 61 CCs of four APIs.

Table 3. Information about each category, respective percentage and regarded CCs systems of the four APIs.

<table>
  <tr>
    <th>Category I</th>
    <th>Category II</th>
    <th>Category III</th>
  </tr>
  <tr>
    <td>THP:DLMA</td>
    <td>CAF:GTA</td>
    <td>NA:GTA</td>
  </tr>
  <tr>
    <td>THP:DMA</td>
    <td>CAF:PCA</td>
    <td>NA:2C4NBA</td>
  </tr>
  <tr>
    <td>THP:GTA</td>
    <td>CAF:24DNBA</td>
    <td>INA:OXA</td>
  </tr>
  <tr>
    <td>THP:GNA</td>
    <td>CAF:SA</td>
    <td>INA:MLA</td>
  </tr>
</table>

<table>
<thead>
<tr>
<th>THP:PCA-I</th>
<th>THP:PCA-II</th>
<th>INA:SCA</th>
</tr>
</thead>
<tbody>
<tr>
<td>THP:SA</td>
<td>THP:SAC</td>
<td>INA:ADA</td>
</tr>
<tr>
<td>THP:URE</td>
<td>NA:EPB</td>
<td>INA:SUA</td>
</tr>
<tr>
<td>CAF:GTA-II</td>
<td>NA:MEFA</td>
<td>INA:3NBA</td>
</tr>
<tr>
<td>CAF:4NAN</td>
<td>INA:FUA</td>
<td>INA:DLMDA</td>
</tr>
<tr>
<td>CAF:2I4NAN</td>
<td>INA:4KPIA</td>
<td>INA:35TFMBA</td>
</tr>
<tr>
<td>CAF:2F5NAN</td>
<td>INA:SA</td>
<td></td>
</tr>
<tr>
<td>CAF:4C3NAN</td>
<td>INA:3HBA</td>
<td></td>
</tr>
<tr>
<td>CAF:2C5NAN</td>
<td>INA:4FBA</td>
<td></td>
</tr>
<tr>
<td>CAF:4I3NAN</td>
<td>INA:CFA</td>
<td></td>
</tr>
<tr>
<td>CAF:4F3NAN</td>
<td>INA:HQ</td>
<td></td>
</tr>
<tr>
<td>CAF:2F5NBA</td>
<td>INA:3NNDMABA</td>
<td></td>
</tr>
<tr>
<td>CAF:SA-I</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:PIA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:AZA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:GTA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:12BDA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:4HBA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:2HEA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:CIA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:CAA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:2PPARS</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:2PPAR</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:REOL</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:MEFA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>INA:FAMEE</td>
<td></td>
<td></td>
</tr>
<tr>
<td>NA:FUA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>NA:4HBA-II</td>
<td></td>
<td></td>
</tr>
<tr>
<td>NA:TOFA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>NA:NIFA</td>
<td></td>
<td></td>
</tr>
<tr>
<td>NA:FURA</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# QSAR analysis for Estimation of Tm of the Cocrystals using ANNs

The constructed ANN QSAR model consists of eight neurons, which were the most influential parameters on the outcome of output parameter *i.e.* melting point of the cocrystals. They were selected on the basis of empiricism, during which we initially trained the model using five input neurons ($CC_{MW}$, $CC_{CPD}$, $CC_{Elatt}$, $API_{Tm}$ and $CF_{Tm}$) and ended with an average relative error of 8.56 % for the training set whereas 10.23 % for the validation set. To improve on this outcome we examined the inclusion of two other parameters as input neurons, such are $API_{MW}$/$CF_{MW}$ ratio and $CC_{Eel}$/$E_{vdW}$, either to replace any of the original five parameters (1) or added as additional parameters to the model (2). Among all these attempts, the best results (not optimal) were obtained (compared to previous), when we consider the seven neurons (altogether) as input parameters, leading to: 7.57 % error for the training set and 6.81 % for the validation set. To further reduce the average relative error, we introduced one more input parameter, *i.e.* the $\Delta$pKa value of the CC and repeated the training process as mentioned earlier. This improved the results by lowering the prediction error of 2.38 % for the training set, and 2.89 % for the validation set.

The capability of the final model is illustrated in Figure 2, where the *Tm* value obtained from ANNs models is plotted against the experimental *Tm* of the CCs, for the training set in diagram a) and for the validation set in diagram b). The overall capability of the model which describes the training set is quite good, the scatter in the validation diagram suggests that for particular system improvements are required. In Table 4 the values are examined in detail. The best results for each API in the training set were obtained for THP:GTA, CAF:4C3NAN, INA:2PPAR and NA:FUA, which are marked as green color in the Table 4. Whereas, the largest errors are obtained for THP:GNA, CAF:2C5NAN, INA:SA and NA:TOFA, which are marked as

red in the Table 4. Among the training series, the lowest prediction error value 0.3 % (in Kelvin scale) was obtained for NA, with fumaric acid coformer; highest prediction error 29.5 % (in Kelvin scale) was obtained for salicylic acid (SA) coformer in the INA series. On the other hand, the lowest prediction error value in the validation series is obtained for the CAF:4F3NAN whereas the highest prediction error obtained for the INA:4HBA, which were marked as purple in the Table 4. The melting points of the model exhibit both positive and negative deviation from the experimental $Tm$ values. As an average, 0.4 % of positive deviation (in Kelvin scale) obtained for THP cocrystals, +1.4 % deviation for CAF cocrystals, -1.6 % deviation for INA cocrystals and -0.5 % of negative deviation for the NA cocrystals. Therefore, among the four APIs, least deviation value obtained for the THP, whereas the highest deviation value obtained for the INA cocrystals. Using the ANN QSAR model, we have analyzed whether a direct relationship can be found between any of the input variables and the output CCs melting point. No such relationship can be found, but each parameter has some significant influence to lower down the average relative error to estimate the melting point of the CCs.

![](./images/811105441835646977_6.jpg)

Figure 3. Ability of neural network QSAR model for prediction of Tm of CCs (a) Experimental versus predicted Tm values (K) for the training set, whereas (b) for validation set for the set of four API molecules.

Table 4. Information about the Tm of the 61 CCs of CAF, THP, NA and INA drug molecules, which are obtained from both experimental and ANN models.

<table>
  <thead>
    <tr>
      <th>Name of the CC</th>
      <th>API (Tm) (K)</th>
      <th>COF (Tm) (K)</th>
      <th>Tm of the CC (exp) (K)</th>
      <th>Tm of the CC (pre) (K)</th>
      <th>Tm (pre)- Tm (exp) (K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>THP: DLMA</td>
      <td>544.2</td>
      <td>403.2</td>
      <td>443.2</td>
      <td>460.1</td>
      <td>16.9</td>
    </tr>
    <tr>
      <td>THP: DMA</td>
      <td>544.2</td>
      <td>371.7</td>
      <td>408.2</td>
      <td>401.0</td>
      <td>-7.2</td>
    </tr>
    <tr>
      <td>THP:GTA</td>
      <td>544.2</td>
      <td>369.7</td>
      <td>391.2</td>
      <td>390.5</td>
      <td>-0.7</td>
    </tr>
    <tr>
      <td>THP:GNA</td>
      <td>544.2</td>
      <td>475.7</td>
      <td>513.2</td>
      <td>494.2</td>
      <td>-19.0</td>
    </tr>
    <tr>
      <td>THP:PCA-I</td>
      <td>544.2</td>
      <td>484.7</td>
      <td>492.8</td>
      <td>486.1</td>
      <td>-6.7</td>
    </tr>
    <tr>
      <td>THP:PCA-II</td>
      <td>544.2</td>
      <td>484.7</td>
      <td>476.8</td>
      <td>488.1</td>
      <td>11.3</td>
    </tr>
    <tr>
      <td>THP:SAC</td>
      <td>544.2</td>
      <td>502.0</td>
      <td>480.2</td>
      <td>474.9</td>
      <td>-5.3</td>
    </tr>
    <tr>
      <td>THP:URE</td>
      <td>544.2</td>
      <td>406.2</td>
      <td>478.2</td>
      <td>475.2</td>
      <td>-3.0</td>
    </tr>
    <tr>
      <td>THP:SA</td>
      <td>544.2</td>
      <td>432.2</td>
      <td>462.2</td>
      <td>479.2</td>
      <td>17.0</td>
    </tr>
    <tr>
      <td>CAF:GTA_I</td>
      <td>509.7</td>
      <td>369.7</td>
      <td>398.2</td>
      <td>387.6</td>
      <td>-10.6</td>
    </tr>
    <tr>
      <td>CAF:GTA_II</td>
      <td>509.7</td>
      <td>369.7</td>
      <td>369.2</td>
      <td>388.5</td>
      <td>19.3</td>
    </tr>
    <tr>
      <td>CAF: PCA</td>
      <td>509.7</td>
      <td>484.7</td>
      <td>452.6</td>
      <td>461.5</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>CAF:4NAN</td>
      <td>509.7</td>
      <td>420.7</td>
      <td>436.9</td>
      <td>433.1</td>
      <td>-3.8</td>
    </tr>
  </tbody>
</table>

<table>
<tbody>
<tr>
<td>CAF:2I4NAN</td>
<td>509.7</td>
<td>380.2</td>
<td>430.2</td>
<td>422.5</td>
<td>-7.7</td>
</tr>
<tr>
<td>CAF:2F5NAN</td>
<td>509.7</td>
<td>371.7</td>
<td>413.7</td>
<td>395.6</td>
<td>-18.1</td>
</tr>
<tr>
<td>CAF:4C3NAN</td>
<td>509.7</td>
<td>373.2</td>
<td>420.7</td>
<td>418.5</td>
<td>-2.2</td>
</tr>
<tr>
<td>CAF:2C5NAN</td>
<td>509.7</td>
<td>394.2</td>
<td>379.7</td>
<td>403.0</td>
<td>23.3</td>
</tr>
<tr>
<td>CAF:4I3NAN</td>
<td>509.7</td>
<td>415.2</td>
<td>438.2</td>
<td>446.2</td>
<td>8.0</td>
</tr>
<tr>
<td>CAF:24DNBA</td>
<td>509.7</td>
<td>454.2</td>
<td>432.4</td>
<td>430.1</td>
<td>-2.3</td>
</tr>
<tr>
<td>CAF:2F5NBA</td>
<td>509.7</td>
<td>416.2</td>
<td>457.2</td>
<td>452.7</td>
<td>-4.5</td>
</tr>
<tr>
<td>CAF:SA</td>
<td>509.7</td>
<td>432.2</td>
<td>416.0</td>
<td>431.9</td>
<td>15.9</td>
</tr>
<tr>
<td>CAF:SA_I</td>
<td>509.7</td>
<td>432.2</td>
<td>433.2</td>
<td>423.5</td>
<td>-9.7</td>
</tr>
<tr>
<td>CAF:4F3NAN</td>
<td>509.7</td>
<td>368.2</td>
<td>401.7</td>
<td>404.2</td>
<td>2.5</td>
</tr>
<tr>
<td>INA:OXA</td>
<td>429.2</td>
<td>375.7</td>
<td>517.0</td>
<td>505.4</td>
<td>-11.6</td>
</tr>
<tr>
<td>INA:MLA</td>
<td>429.2</td>
<td>409.2</td>
<td>443.2</td>
<td>443.9</td>
<td>0.7</td>
</tr>
<tr>
<td>INA:SCA</td>
<td>429.2</td>
<td>457.2</td>
<td>479.2</td>
<td>472.4</td>
<td>-6.8</td>
</tr>
<tr>
<td>INA:GTA</td>
<td>429.2</td>
<td>369.7</td>
<td>409.0</td>
<td>431.3</td>
<td>22.3</td>
</tr>
<tr>
<td>INA:ADA</td>
<td>429.2</td>
<td>425.3</td>
<td>439.0</td>
<td>427.4</td>
<td>-11.6</td>
</tr>
<tr>
<td>INA:PIA</td>
<td>429.2</td>
<td>377.2</td>
<td>385.2</td>
<td>408.7</td>
<td>23.5</td>
</tr>
<tr>
<td>INA:SUA</td>
<td>429.2</td>
<td>415.7</td>
<td>438.2</td>
<td>422.9</td>
<td>-15.3</td>
</tr>
<tr>
<td>INA:AZA</td>
<td>429.2</td>
<td>382.2</td>
<td>415.2</td>
<td>395.1</td>
<td>-20.1</td>
</tr>
<tr>
<td>INA:FUA</td>
<td>429.2</td>
<td>560.2</td>
<td>420.2</td>
<td>415.1</td>
<td>-5.1</td>
</tr>
<tr>
<td>INA:4KPA</td>
<td>429.2</td>
<td>416.2</td>
<td>385.7</td>
<td>392.5</td>
<td>6.8</td>
</tr>
<tr>
<td>INA:12BDA</td>
<td>429.2</td>
<td>326.7</td>
<td>362.2</td>
<td>364.7</td>
<td>2.5</td>
</tr>
<tr>
<td>INA:SA</td>
<td>429.2</td>
<td>431.8</td>
<td>393.2</td>
<td>422.7</td>
<td>29.5</td>
</tr>
<tr>
<td>INA:3HBA</td>
<td>429.2</td>
<td>472.2</td>
<td>418.2</td>
<td>431.7</td>
<td>13.5</td>
</tr>
<tr>
<td>INA:4HBA</td>
<td>429.2</td>
<td>487.7</td>
<td>468.2</td>
<td>430.8</td>
<td>-37.4</td>
</tr>
<tr>
<td>INA:4FBA</td>
<td>429.2</td>
<td>457.2</td>
<td>427.2</td>
<td>426.3</td>
<td>-0.9</td>
</tr>
<tr>
<td>INA:3NBA</td>
<td>429.2</td>
<td>413.2</td>
<td>434.2</td>
<td>439.3</td>
<td>5.1</td>
</tr>
<tr>
<td>INA:2HEA</td>
<td>429.2</td>
<td>307.2</td>
<td>384.2</td>
<td>361.0</td>
<td>-23.2</td>
</tr>
<tr>
<td>INA:CIA</td>
<td>429.2</td>
<td>406.2</td>
<td>420.2</td>
<td>407.5</td>
<td>-12.7</td>
</tr>
<tr>
<td>INA:CAA</td>
<td>429.2</td>
<td>336.2</td>
<td>369.7</td>
<td>363.8</td>
<td>-5.9</td>
</tr>
<tr>
<td>INA:2PPARS</td>
<td>429.2</td>
<td>302.7</td>
<td>365.0</td>
<td>361.1</td>
<td>-3.9</td>
</tr>
<tr>
<td>INA:2PPAR</td>
<td>429.2</td>
<td>302.7</td>
<td>361.0</td>
<td>361.4</td>
<td>0.4</td>
</tr>
</tbody>
</table>

<table>
  <tr>
    <td>INA:DLMDA</td>
    <td>429.2</td>
    <td>403.2</td>
    <td>442.2</td>
    <td>421.1</td>
    <td>-21.1</td>
  </tr>
  <tr>
    <td>INA:CFA</td>
    <td>429.2</td>
    <td>393.7</td>
    <td>362.7</td>
    <td>388.0</td>
    <td>25.3</td>
  </tr>
  <tr>
    <td>INA:REOL</td>
    <td>429.2</td>
    <td>383.2</td>
    <td>428.2</td>
    <td>427.6</td>
    <td>-0.6</td>
  </tr>
  <tr>
    <td>INA:HQ</td>
    <td>429.2</td>
    <td>445.2</td>
    <td>429.0</td>
    <td>434.3</td>
    <td>5.3</td>
  </tr>
  <tr>
    <td>INA:<br>3NNDMABA</td>
    <td>429.2</td>
    <td>423.7</td>
    <td>412.2</td>
    <td>414.8</td>
    <td>2.6</td>
  </tr>
  <tr>
    <td>INA:35TFMBA</td>
    <td>429.2</td>
    <td>415.2</td>
    <td>434.7</td>
    <td>431.3</td>
    <td>-3.4</td>
  </tr>
  <tr>
    <td>INA:MEFA</td>
    <td>429.2</td>
    <td>522.2</td>
    <td>450.0</td>
    <td>443.0</td>
    <td>-7.0</td>
  </tr>
  <tr>
    <td>INA:FAMEE</td>
    <td>429.2</td>
    <td>337.7</td>
    <td>367.5</td>
    <td>370.0</td>
    <td>2.5</td>
  </tr>
  <tr>
    <td>NA:FUA</td>
    <td>401.2</td>
    <td>560.2</td>
    <td>449.2</td>
    <td>449.4</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>NA:GTA</td>
    <td>401.2</td>
    <td>369.7</td>
    <td>423.0</td>
    <td>431.4</td>
    <td>8.4</td>
  </tr>
  <tr>
    <td>NA:4HBAII</td>
    <td>401.2</td>
    <td>487.7</td>
    <td>458.2</td>
    <td>448.6</td>
    <td>-9.6</td>
  </tr>
  <tr>
    <td>NA:EPB</td>
    <td>401.2</td>
    <td>389.7</td>
    <td>381.0</td>
    <td>374.8</td>
    <td>-6.2</td>
  </tr>
  <tr>
    <td>NA:2C4NBA</td>
    <td>401.2</td>
    <td>412.7</td>
    <td>432.8</td>
    <td>423.6</td>
    <td>-9.2</td>
  </tr>
  <tr>
    <td>NA:TOFA</td>
    <td>401.2</td>
    <td>480.2</td>
    <td>427.0</td>
    <td>403.7</td>
    <td>-23.3</td>
  </tr>
  <tr>
    <td>NA:MEFA</td>
    <td>401.2</td>
    <td>503.7</td>
    <td>400.0</td>
    <td>421.7</td>
    <td>21.7</td>
  </tr>
  <tr>
    <td>NA:NIFA</td>
    <td>401.2</td>
    <td>477.2</td>
    <td>414.0</td>
    <td>425.7</td>
    <td>11.7</td>
  </tr>
  <tr>
    <td>NA:FURA</td>
    <td>401.2</td>
    <td>493.2</td>
    <td>423.2</td>
    <td>424.7</td>
    <td>1.5</td>
  </tr>
</table>

## Conclusions

In the present study, a machine learning Artifial Neural Network (ANN) model has been applied to the correlation/prediction of the melting temperature of cocrystals. A successful Quantitative Structure-Activity Relationship (QSAR) model has been constructed based on 61 cocrystals for four Active Pharmaceutical Ingredient (API) molecules with the optimum model giving an average relative deviation of 2.38 % for the training set of 55 cocrystals, and a corresponding deviation of 2.89 % for the validation set of 6 cocrystals. However, the best predictive value (compared to experimental value) is obtained in the training set is for the

glutaric acid (GTA) coformer in the theophylline (THP) series: with about –0.7 % (K) error, 4-Chloro-3-nitro aniline (4C3NAN) coformer in the CAF series: about –2.2 % (K) error, (R)-2-phenylpropionic acid (2PPAR) coformer in the INA series: about 0.4 % (K) error and with fumaric acid (FUA) coformer in the NA cocrystals series: about 0.2 % (K) error. On the other hand, large deviation is observed in series of each APIs: -19 % (K) deviation obtained for the gentisic acid (GNA) coformer in the theophylline (THP) series: +23.3 % (K) deviation obtained for 2-Chloro-5-nitro aniline (2C5NAN) in the CAF series: 29.5 % (K) positive deviation obtained for salicylic acid (SA) in the INA series and -23.3 % (K) deviation obtained with tolfenamic acid coformer in the NA series. Whereas, the best predictive value in the validation set is obtained for 4-Fluoro-3-nitro aniline coformer with caffeine about +2.5 % error, and the highest deviation obtained for 4-hydroxybenzoic acid coformer with isonicotinamide with about -37.4 % error. The biggest deviation observed among the 61 cocrystal systems is for 4-hydroxybenzoic acid (4HBA) of isonicotinamide cocrystals (INA:4HBA) about -37.4 % (K), whereas least deviation is observed for fumaric acid coformer of nicotinamide cocrystals about 0.2 % (K).

ASSOCIATED CONTENT

Crystal packing density, molecular weight of all the APIs, coformers and their respective ratio, electrostatic interaction percentages, van der Waals interaction percentages and the ratio of electrostatic interactions *vs* van der Waals interactions of all the cocrystals are available free of charge via the Internet at http://pubs.acs.org.

AUTHOR INFORMATION

Corresponding Author

*E-mail: Ake.Rasmuson@ul.ie

## ACKNOWLEDGMENT

The authors acknowledge financial support from the Science Foundation Ireland, Grant number: 12/RC/2275. The authors thank Dr. Marko Ukrainczyk and Dr. Jacek Zeglinski for their valuable scientific discussions and suggestions.

## REFERENCES

(1) Schultheiss, N.; Newman, A. *Cryst. Growth. Des.* **2009**, 9, 2950–2967.

(2) Dhore, P. W.; Dave, V. S.; Saoji, S. D.; Bobde, Y. S.; Mack, C.; Raut, N. A. *Pharm. Dev. Technol.* **2016**, http://dx.doi.org/10.1080/10837450.2016.1193193.

(3) Sonoda, R.; Horibe, M.; Oshima, T.; Iwasaki, T.; Watano, S. *Chem. Pharm. Bull.* **2008**, 56, 1243-1247.

(4) Liu, X.; Lu, M.; Guo, Z.; Huang, L.; Feng, X. Wu, C. *Pharm. Res.* **2012**, 29, 806-817.

(5) McNamara, D. P.; Childs, S. L.; Giordano, J.; Iarriccio, A.; Cassidy, J.; Shet, M. S.; Mannion, R.; Donnell, E.; Park, A. *Pharm. Res.* **2006**, 23, 1888-1897.

(6) Krishna, G. R.; Shi, L.; Bag, P. P.; Sun, C. C.; Reddy, C. M. *Cryst. Growth Des.* **2015**, 15, 1827–1832.

(7) Duggirala, N. K.; Perry, M. L.; Almarsson, Ö.; Zaworotko, M. J. *Chem. Commun.* **2016**, 52, 640-655.

(8) Rahman, Z.; Zidan, A. S.; Samy, R.; Sayeed, V. A.; Khan, M. A. *AAPS PharmSciTech.* **2012**, 13, 793-801.

(9) Zhao, X. S.; Siepmann, J. I.; Xu, W.; Kiang, Y–H.; Sheth, A. R.; Karaborni, S. *J. Phys. Chem. B* **2009**, 113, 5929–5937.

(10) Chadha, R.; Kuhad, A.; Arora, P.; Kishor, S. *Chem. Cent. J.* **2012**, 6, 114.

(11) Friščić, T.; Jones, W. *J. Pharm. Pharmacol.* **2010**, 62, 1547–1559.

(12) Thakur, T. S.; Desiraju, G. R. *Cryst. Growth Des.* **2008**, 8, 4031–4044.

(13) Bhogala, B. R.; Basavoju, S.; Nangia, A. *CrystEngComm.* **2005**, 7, 551−562.

(14) Fábián, L. *Cryst. Growth Des.* **2009**, 9, 1436−1443.

(15) Mohammada, M. A.; Alhalaweha, A.; Velaga, S. P. *Int. J. Pharm.* **2011**, 407, 63−71.

(16) Cysewski, P.; Przybyłek, M.; Ziółkowska, D.; Mroczyńska, K. *J Mol Model.* **2016**, 22, 103.

(17) Vishweshwar, P.; Nangia, A.; Lynch, V. M. *Cryst. Growth Des.* **2003**, 3, 783-790.

(18) Aakeräy, C. B.; Panikkattu, S.; DeHaven, B.; Desper, J. *CrystEngComm.* **2013**, 15, 463−470.

(19) Aakeröy, C. B.; Forbes, S.; Desper, J. *CrystEngComm.* **2014**, 16, 5870−5877.

(20) Batisai, E.; Ayamine, A.; Kilinkissa, O. E. Y.; Báthori, N. B. *CrystEngComm.* **2014**, 16, 9992−9998.

(21) Kuleshova, L. N.; Hofmann, D. W. M.; Boese, R. *Chem. Phys. Lett.* **2013**, 564, 26−32.

(22) Perlovich, G. L. *CrystEngComm.* **2015**, 17, 7019−7028.

(23) Godavarthy, S. S.; Jr, R. L. R.; Gasem, K. A. M. *Ind. Eng. Chem. Res.* **2006**, 45, 5117-5126.

(24) Palmer, D. S.; Llinàs, A.; Morao, I.; Day, G. M.; Goodman, J. M.; Glen, R. C.; Mitchell, J. B. O. *Mol. Pharm.* **2008**, 5, 266−279.

(25) Harding, A. P.; Wedge, D. C.; Popelier, P. L. A. *J. Chem. Inf. Model.* **2009**, 49, 1914−1924.

(26) Mitchell, J. B. O. *Comput Mol Sci.* **2014**, 4, 468−481.

(27) Bhat, A. U.; Merchant, S. S.; Bhagwat, S. S. *Ind. Eng. Chem. Res.* **2008**, 47, 920−925.

(28) Ukrainczyk, N.; Ukrainczyk, V. *Mag Concrete Res.* **2008**, 60, 475−486.

(29) Karthikeyan, M. *J. Chem. Inf. Model.* **2005**, 45, 581−590.

(30) Torrecilla, J. S.; Rodríguez, F.; Bravo, J. L.; Rothenberg, G.; Seddond, K. R.; López-Martin, I. *Phys. Chem. Chem. Phys.* **2008**, 10, 5826−5831.

(31) Le, T.; Epa, V. C.; Burden, F. R.; Winkler, D. A. *Chem. Rev.* **2012**, 112, 2889−2919.

(32) Gharagheizi, F.; Salehi, G. R. *Thermochim Acta.* **2011**, 521, 37−40.

(33) Jain, A.; Yang, G.; Yalkowsky, S. H. *Ind. Eng. Chem. Res.* **2004**, 43, 4376-4379.

(34) Kůrková, V. *Neural Netw.* **1992**, 5, 501−506.

(35) Saha, A. Neural Network Models in Excel for Prediction and Classification. Available online from https://www.sites.google.com/site/sayhello2angshu/dminexcel.

For Table of Contents Use Only

Estimation of Melting Temperature of Molecular Co-crystals using Artificial Neural Network Model

Gamidi Rama Krishna and Åke. C. Rasmuson*

Department of Chemical and Environmental Science, Synthesis and Solid State Pharmaceutical Centre, Bernal Institute, University of Limerick, Limerick, Ireland

![](./images/811105441835646977_7.jpg)

Synopsis: Based on a literature analysis using Scifinder and Cambridge Structural Database softwares, a database has been created over 61 cocrystals for four APIs, namely, *i.e.* caffeine, theophylline, nicotinamide and isonicotinamide. And an estimation of melting point of the co-crystals are made possible by performing a Quantitative Structure Activity Relationship using the Artificial Neural Network programs as a main tool.

![](./images/811105441835646977_8.jpg)

Prediction of melting point of the cocrystals

88x34mm (300 x 300 DPI)