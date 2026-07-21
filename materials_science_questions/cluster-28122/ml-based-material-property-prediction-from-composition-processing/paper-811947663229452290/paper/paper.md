![](./images/811947663229452290_1.jpg)

Available online at www.sciencedirect.com

![](./images/811947663229452290_2.jpg)

Acta Materialia 56 (2008) 1094-1105

![](./images/811947663229452290_3.jpg)

# Revisiting Hume-Rothery's Rules with artificial neural networks

Y.M. Zhang, S. Yang, J.R.G. Evans*

Department of Materials, Queen Mary, University of London, Mile End Road, London E1 4NS, UK

Received 22 September 2007; accepted 3 October 2007
Available online 26 December 2007

## Abstract
Hume-Rothery's breadth of knowledge combined with a quest for generality gave him insights into the reasons for solubility in metallic systems that have become known as Hume- Rothery's Rules. Presented with solubility details from similar sets of constitutional diagrams, can one expect artificial neural networks (ANN), which are blind to the underlying metals physics, to reveal similar or better correlations? The aim is to test whether it is feasible to predict solid solubility limits using ANN with the parameters that Hume- Rothery identified. The results indicate that the correlations expected by Hume- Rothery's Rules work best for a certain range of copper or silver alloy systems. The ANN can predict a value for solubility, which is a refinement on the original qualitative duties of Hume- Rothery's Rules. The best combination of input parameters can also be evaluated by ANN.
© 2007 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Hume-Rothery's Rules; Artificial neural networks; Solubility limit of metals; Backpropagation networks; Binary alloys

## 1. Introduction
Materials science seeks to understand the causative relationships between composition, processing, structure and properties at a level that allows composition and processing parameters to be selected to provide targeted properties. Such relationships can be discerned by experiment and, in a few instances, by predictive theory. They can sometimes be obtained by molecular modelling. All molecular modelling techniques can be classified under three general categories: (1) ab initio electronic structure calculations, which are based upon quantum mechanics; (2) semi-empirical methods, which are also founded upon quantum mechanics, but which enhance computational speed by using approximations based upon experiment; (3) molecular mechanics, an empirical method based on classical physics which is computationally fast [1].

Another approach is to use correlation methods made possible by artificial neural networks (ANN), which are finding growing acceptance in many subjects for modelling complex problems [2]. They are model-free in the sense that they can process complex input-output relationships without an explicit mathematical model [3] and are becoming popular in materials science in solving problems that are not suitable for traditional statistical methods [4]. They can process large amounts of information and mimic biological systems in learning ability and capability to generalize. They can handle non-linearity, imprecise and fuzzy information and are fault and failure tolerant [5]. Importantly, they offer the materials scientist compositionally predictive power in which conventional theory is sometimes lacking because of theoretical complexity. A good example is their use in predicting dielectric constants from composition [6].

Various networks have been devised but backpropagation networks in which the data are forward-fed into the network without feedback and without same-layer neural connections are the most widely used [2,7]. The model is shown schematically in Fig. 1. In such artificial systems, learning is a process of updating an internal representation of an external system. During learning, the magnitude of the weightings or 'synapse' strengths is adjusted repetitively as the network is presented with training data.

* Corresponding author. Tel.: +44 (0)20 76794689.
E-mail address: j.r.g.evans@qmul.ac.uk (J.R.G. Evans).

1359-6454/$30.00 © 2007 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actamat.2007.10.059

![](./images/811947663229452290_4.jpg)

Fig. 1. A model of a feed-forward hierarchical artificial neural network.

In Arkadan et al.'s work [8], the location and shape of a crack were deduced from measured magnetic field val- ues as inputs. Raj et al. [9] used ANN in metalworking to predict forging load in hot upsetting, cutting forces in machining and loads in hot extrusion. Guessasma and Coddet [10] used an ANN to quantify the relation- ship between automated plasma spraying process param- eters and microstructural features of aluminium-titanium coatings.

Huang et al. [11] predicted the mechanical properties of a ceramic tool based on materials properties. Malinov and Sha [12] used ANN for correlation between processing parameters and properties in titanium alloys, such as fati- gue life and corrosion resistance. They also have been used in ceramic casting [13], to interpret ultrasonic non-destruc- tive testing (NDT) of adhesive joints [14], for modelling the cold rolling forces [15], to predict continuous-cooling trans- formation curves in steel from chemical composition [16] and to predict time-temperature transformation diagrams for titanium alloys [17].

The potential uses for prediction of properties of mat- ter are interesting for materials scientists. Homer et al. [18] used physical properties such as molecular weight, number of bonds and temperature as input factors to pre- dict the viscosity, density, heat of vaporization, boiling point and acentric factors for pure, organic, liquid hydro-carbons over a wide range of temperatures $(T_{reduced } \approx$ 0.45-0.7). A three-layer backpropagation network ANN was applied to the formulation of $BaTiO_{3}$ -based dielec trics and for analysis of the electrical properties of PZT[19,20].

Since ANN can sometimes provide significant improve- ments over linear regression analysis, there is increasing interest in their applicability to materials science where the interrelationships are not well understood and amena- ble to analytical solutions [21]. Such is the case in a survey of terminal solid solutions in several alloy systems in which Hume-Rothery devised simple and useful rules on solubil- ity limits which have become known as Hume-Rothery'sRules:
(1) The atomic size factor [22]: If the atomic diameters of the solute and solvent differ by more than $14 \%$ , the solubility is likely to be restricted because the lattice distortion is too great for substitutional solubility. A criterion of $15 \%$ , which was taken by later writers, is also tested in this work.
(2) The electrochemical factor [22]: or 'effect of the peri- ods of the solvent and solute atoms' was quantified by Cooke and Hume-Rothery [23] after the 'electro- chemical factor' introduced by Pauling [24]. Strongly electropositive components are more likely to form compounds with electronegative components than to form solid solutions, particularly in the later B sub-groups.
(3) The relative valency factor [22]: Other factors being equal, a lower valence metal is more likely to dissolve one of higher valency than vice versa, i.e., the ten- dency for two metals to form solid solutions is not necessarily reciprocal. This has been found to be valid mainly for alloys of copper, silver or gold combined with metals of higher valency.

Traditionally, phase diagrams were determined by(often tedious) experimentation, which nevertheless suf- fered from the difficulty of reaching equilibrium at low temperatures (typically $<0.5 T_{m}$ ) in reasonable timescales[25]. Hume-Rothery's quest for generality was thus well founded but has, to an extent, been superseded by compu- tational calculation of phase diagrams following pioneering work by Kaufman and Bernstein [26] and Hillert [27] and others in the 1970s giving rise to such tools as CALPHAD, which has been widely used, e.g., Refs. [28-33].
After the significant work done by Hume-Rothery et al. on the prediction of solid solubility in alloys, Dar- ken and Gurry [34], Chelikowsky [35], Alonso and Simo- zar [36], Alonso et al. [37] and Zhang and Liao [38] all contributed in different ways to the prediction of solid sol- ubility in terms of a soluble/insoluble criterion.
The authors' aim is to stand at the place where Hume- Rothery stood, with the added advantage of the ANN and, based on a large number of constitutional diagrams and physical parameters of metals provided by handbooks[39,40], to simulate the process that Hume-Rothery used to derive his rules. Hume-Rothery considered 60 systems, and so one faces the problem of limited data. Nevertheless, there are many situations where materials scientists would like to benefit from ANN in situations where the data set has inherent limitations. It has been proved that ANN methods provide an efficient tool for experimental data analysis even when the database size is small [41]. Further- more, this study attempts to predict the solubility quantita-tively rather than produce a classification of soluble/ insoluble. Thereafter, it is attempted to extend the method to a wider range of silver and copper alloys based on binary systems and including different structures.
One interesting question is whether the parameters Hume-Rothery used are sufficient to determine the solu- bility. Hume-Rothery amended the rules by introducing the structural parameter 14 years after the first presenta- tion of the rules [42]. In this paper, ANN have been used to determine the relative importance by deliberately omit- ting one or two parameters. Another aim is to explore the effects of the format of the input parameters. The combi-

nations of these different parameters are tested in this
paper.

## 2. Types of ANN
There are some more frequently used ANN from which
to select. They have their own characteristics and special
applications [2]:

1.  *Backpropagation artificial neural networks (BPANN)*.
    This type of network is versatile and can be used in
    many fields such as data modelling, classification, fore-
    casting, control, data and image compression and pat-
    tern recognition [43].
2.  *Hopfield networks*. These are two-layer recurrent net-
    works, which are ideal for solving optimization prob-
    lems [44,45].
3.  *Adaptive resonance theory (ART) networks*. These are
    made up of a layer that receives inputs and a layer that
    consists of output neurons and can, like Hopfield net-
    works, be used for pattern recognition, completion
    and classification [2].
4.  *Kohonen networks*. These are two-layer networks, which
    convert multidimensional input patterns into lower-
    order data [46]. In addition to pattern recognition and
    classification, Kohonen networks also can be used for
    data compression, i.e., high-dimensional data can be
    mapped into lower-dimensional space without losing
    content [47].
5.  *Counterpropagation networks*. These networks, which
    are developed by Hecht-Nielsen [48,49], are trained by
    supervised and unsupervised learning to create a self-
    organizing database and can be used for function
    approximation and classification [50].
6.  *Radial basis function (RBF) networks*. These are a type
    of a multi-layer feed-forward error-backpropagation
    networks with three-layers [51]. The selection of RBF
    or BPANN depends on the type of problem [52]. RBF
    networks train faster than BPANN but are less versatile
    and are somewhat slower [53].

The reason for selecting the proposed ANN is now
explained. As Basheer and Hajmeer [2] mentioned, the
decision depends strictly on the problem logistics. The
Kohonen network is required by a clustering problem,
BP or RBF networks can model mapping problems, but
Hopfield networks can only solve some optimization prob-
lems. ANN selection also depends on the type of input
(Boolean, continuous or a mixture of these) and the speed
of the network once it is trained. The initial problem, which
simulates the process that Hume-Rothery used to derive his
rules has ‘soluble/insoluble’ as output and is a type of clas-
sification problem, so a probabilistic neural network [54,55]
is designed for use. This is a type of radial basis network
suitable for classification problems. In subsequent work,
the problems are all mapping problems, so BPANN are
used.

## 3. Data collection
The silver and copper alloy solid solubility limits (at.%)
are recorded from Massalski et al. [39], Moffatt [56] and
*ASM Handbook*, vol. 3, *Alloy Phase Diagrams* [57]. The
physical parameters, radii, valences and electrochemical
factors (electronegativity) of solvent and solute atoms are
taken from Stark and Wallace [40] and from Aylward
and Findlay [58]. The valences of elements, which were
mentioned by Hume-Rothery in 1934, follow his represen-
tation. Radii of Al, Ga, and $\alpha$-Fe also followed Hume-
Rothery's representations [59]. The structure parameter is
taken from Ref. [57].

The whole data set is used in two ways: (1) the 60-alloy
systems, which were first mentioned by Hume-Rothery in
1934, are used for training the neural network and testing
whether the Hume-Rothery's Rules work in this range of
alloy systems; (2) all the 408 silver and copper alloy systems
collected are used to repeat the process.

## 4. Configuration of the neural network
The ANN are constructed, trained and simulated by
MATLAB software, run under the Microsoft Windows
XP operating system on ThinkPad (IBM ThinkPad T40
Model 2373-12H: Intel Pentium M1.3 G, 256 MB, 30
GB, 14.1 in. TFT), Java VM Version: Java 1.4.2 with
Sun Microsystems Inc. Java HotSpot™ Client VM.

### 4.1. Number of neural network layers
A two-hidden-layer sigmoid/linear network can repre-
sent any functional relationship between inputs and
outputs if the sigmoid layer has enough neurons [60]. A
two-hidden-layer network, with a tan-sigmoid transfer
function in the first hidden layer and a linear transfer func-
tion in the second hidden layer, is thus adopted. The num-
ber of neurons in the second hidden layer is constrained by
the number of outputs required by the problem. The out-
put in this work is solubility, so there is one neuron in
the second hidden layer.

### 4.2. Number of neurons in the first hidden layer
The choice of number of neurons in the first hidden
layer is up to the designer. The optimum number of neu-
rons in the first hidden layers may be a function of (1)
input/output vector size, (2) size of training and testing
sub-sets and, more importantly, (3) the problem of non-lin-
earity [2]. The optimum number is found by trial and error
by placing a different number of neurons in the first hidden
layer for the same data set.

### 4.3. Improving generalization
Overfitting occurs during network training if the error
associated with the training set becomes low, but the error

becomes large when new data are presented to the network. This means that the network has learned the training examples but is unable to generalize to new situations. There are two common methods for improving generalization: Bayesian Regularization and Early Stopping [60]. Bayesian Regularization tends to provide better generalization performance than Early Stopping in training function approximation networks. As a result, Bayesian Regularization is used for improving generalization. This involves setting the sum of squares of the network errors on the training set to give the best generalization.

### 4.4. Partitioning of the database

The generalizing ability of the network depends on the training database size [2]. Although ANN can be obtained from a training database of any size, like other empirical models, generalization of these models outside the model domain is adversely affected. Since ANN are required to generalize for the unseen data, data used for training should be large enough to cover the possible known variation in the problem domain.

The development of an ANN based on Bayesian Regularization requires partitioning of the parent database into two sub-sets: training and testing. Currently, there are no definitive rules for determining the required sizes of the data sub-sets. Rules of thumb derived from experience and analogy between ANN and statistical regression exist [2]. Following the method suggested by Matlab [60], the sets are picked as equally spaced points throughout the original data. Ratios between 2:1 and 5:1 are tested and, based on regression coefficient for the testing set, the ratio 4:1 is selected, i.e., partitioning the whole data set into five groups, four groups being used for training, while one group is used for testing. The size of the training set and testing set are thus determined, but the choice of testing set still plays a crucial role, because the training set should include all the data belonging to the problem domain. In this work, the problem domain is not clear, so, referring to Malinov and Sha's work [4], a loop program was used to redistribute the database in order to make the training set cover the problem domain. The distribution was selected on the basis of regression coefficient $R$ ($R=1$ corresponds to perfect correlation), for the testing set. However, where $M$, the slope of the linear regression line, is smaller than 0.9, the regression coefficient provides an unreliable criterion, and so the selection was based on $\varphi = |M-1|+(1-R)+\left|\frac{B}{B_{\max}}\right|$, where $B$ was the intercept on the $A$-axis, and $B_{\max}$ is the maximum solubility. The ideal value of this parameter is zero.

### 4.5. Data normalization

The data should be normalized within a uniform range (e.g., $[0,1]$ or $[-1,1]$) in order to prevent larger numbers from overriding smaller ones and to prevent premature saturation of the neurons of hidden layers, which would impede the learning process [2]. There are two functions for scaling the inputs and targets of networks that have been implemented in the Matlab Neural Network Toolbox: PREMNMX, which is used to scale inputs and targets so that they fall in the range $[-1,1]$; and PRESTD, which normalizes the inputs and targets so that they will have zero mean and unity standard deviation. As the transfer functions employed here are tan-sigmoid transfer function and linear function, PREMNMX is adopted.

Because the size of the database in this work is small, it is crucial to make the training set cover the problem boundary. As in Malinov and Sha's work [4], a looped program is used in order to find the best combination of database distribution and number of neurons in the first hidden layer. The criteria used to find the best combination are discussed below.

## 5. Determination of input parameters

The network input parameters are the physical parameters including (1) atomic size parameter, (2) valence parameter, (3) electrochemical parameter, i.e., electronegativity, and (4) structure parameter of solvent and solute atoms, which were not mentioned in 1934, but were introduced in 1948 [42] concerning the detailed examination of Vegard's law [61] in the case of metallic solid solutions.

Three different expressions of these parameters are used:

1. The raw data that Hume-Rothery used. Details are discussed below.
2. The original collected values for each parameter of solvent and solute atoms.
3. The original collected parameters are converted into functionalized values before putting them into the networks:
    (a) *For the size factor.* The difference between the atomic diameters of solvent and solute atoms divided by the diameter of the solvent atoms is used.
    (b) *For the valence factor.* These are integers and the original values are used, leaving the neural network to decide the relations between valence of solvents and solutes.
    (c) *For the electrochemical factor.* The difference between that of the solvent and solute atoms is used.
    (d) *For the structure parameter.* The expressions of the structures can be put in terms of numbers 1–14 for the Bravais lattices, but this revealed little effect of the structures. They can also be expressed in three sets of numbers representing primitive cell dimensions, angles and systems. This allows some similarities to be explored. The three sets are (1) unit cell length ($a=b=c;a=b\neq c;a\neq b\neq c$), (2) axes angles ($\alpha=\beta=\gamma=90^{\circ};\ \alpha=\beta=90^{\circ},\ \gamma=120^{\circ}$;

$$\alpha=\beta=\gamma\neq90^{\circ};\ \alpha=\gamma=90^{\circ}\neq\beta;\ \alpha\neq\beta\neq\gamma\neq90^{\circ})$$
and (3) crystal system (simple; base-centred; face-centred; body-centred).

## 6. Determination of the output parameters

In Hume-Rothery's Rules, a soluble/insoluble criterion is described. However, it would be more advantageous to attempt to predict the original value of the solubility. The output parameters, which are the solubility limits of each alloy system, are therefore expressed in two ways:

(1) Follow the specialized criterion: if the solubility of solute metal in solvent metal exceeds 5 at.% [38,62], it is said that this solute metal is soluble in the solvent metal.
(2) Use the original maximum solubility limits of each alloy system.

## 7. Results

The data are used in two ways: (1) the first 60-alloy systems mentioned by Hume-Rothery in 1934 are used as a start; (2) the whole 408-alloy systems are then used to test whether Hume-Rothery's Rules work for copper and silver alloy systems in general.

### 7.1. Testing Hume-Rothery's rules within 60-alloy systems

Of the four parameters, the size factor, the electrochemical factor and the relative valency factor were those used by Hume-Rothery in 1934, so these are used in initial tests for predicting solubility using the following criteria:

1. If the atomic diameters differ by more than 14%, it means that the size factor is 'unfavourable', and the input number for this parameter is zero, or it is one.
2. If the valency of solvent atom is lower than that of solute atom, the input number for this parameter is one, or else the number is zero.
3. If the difference of the electronegativity of solvent and solute atom is more than 0.4, mentioned by Darken and Gurry [34] and Zhang and Liao [38], the input number for this parameter is zero, or else it is one.
4. If the solubility of solute metal in solvent metal exceed 5 at.%, the output number is one, or else it is zero.

In this case, the problem to be solved is a classification problem, so a probabilistic neural network [54,55] is designed for use. This is a radial basis network suitable for classification problems. The modified criterion of 15% for the diameter difference mentioned by Darken and Gurry [34] is used in the next trial, also with soluble/insoluble as output, and both results are listed in Table 1 in terms of the percentage of all the 60 predictions that are wrong. Comparing these results, a slight difference is found: the percentage error of the predicted results based

<table><caption>Table 1 Testing Hume-Rothery's Rules with 60-alloy systems using his criterion (14% variation), the later suggestion of 15% and the 15% criterion with structural identity (same or not)</caption>
<thead>
  <tr>
    <th>Choice (%)</th>
    <th colspan="2">Error of prediction (%)</th>
  </tr>
  <tr>
    <th></th>
    <th>Testing</th>
    <th>Whole data</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>14</td>
    <td>8.3</td>
    <td>15</td>
  </tr>
  <tr>
    <td>15</td>
    <td>8.3</td>
    <td>13</td>
  </tr>
  <tr>
    <td>Structure parameter</td>
    <td>8.3</td>
    <td>13</td>
  </tr>
</tbody>
</table>

on the experimental results for the whole data set using the 15% criterion is slightly lower than that for 14%. This result shows the consistency with the modified criterion of size factor, although Hume-Rothery stated in his later work [63]: 'the 14% difference does give a better correlation with solubility data than the commonly accepted 15%'.

Using the same approach and including the 15% criterion, the structure parameter is introduced next in terms of whether the structures of solvents and solutes are the same (i.e., 1 same, 0 not same). The results are listed in the last row of Table 1. Comparing these results with the previous one, there is no improvement in correlation. This indicates that the structure parameters do not play a very important role in solubility when the 5 at.% solubility limit is selected as the threshold. Zhang and Liao [38] commented that taking the 5 at.% threshold at any temperature is not precise enough, and solubility limits are not accurately predicted when the rules are deployed in this way.

In the next trial, the original values of input parameters and of output solubilities are used and the structure parameter is incorporated using an integer for each of the 14 Bravais lattices. From this trial to the end, all the problems modelled are mapping problems, so BPANN are adopted throughout. The separate results for training sets and testing sets are shown in Table 2. For the training set, the regression coefficient $R$ is 0.996, and slope $M$ is 0.984. However, the prediction for the testing data from the trained network in this case is very poor ($M$ is 0.193, and $R$ is 0.383), and this clearly indicates that, although the network trains satisfactorily on the actual values of input data, it is unable to use these for prediction.

In the next trial, input variables are based on functionalized values, the structure parameter is omitted, and the results are shown in Fig. 2, in which the training set (a) is distinguished from the testing set (b). The values of $M$, $B$ and $R$ for the training set are 0.977, 0.23 and 0.993, respectively, and for the testing set they are 0.962, $-1.19$ and 0.992, respectively. This demonstrates reasonable correlation (the ideal values are $M=1$, $B=0$ and $R=1$).

<table><caption>Table 2 Testing Hume-Rothery's Rules using original parameter values</caption>
<thead>
  <tr>
    <th colspan="2">$M$</th>
    <th colspan="2">$B$</th>
    <th colspan="2">$R$</th>
  </tr>
  <tr>
    <th>Training</th>
    <th>Testing</th>
    <th>Training</th>
    <th>Testing</th>
    <th>Training</th>
    <th>Testing</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.984</td>
    <td>0.193</td>
    <td>0.158</td>
    <td>$-2.75$</td>
    <td>0.996</td>
    <td>0.383</td>
  </tr>
</tbody>
</table>

![](./images/811947663229452290_5.jpg)

Fig. 2. Prediction of solubility using three functionalized parameters for the 60-alloy system data set: atomic size, valency and electronegativity. (a) Training set; (b) testing set; (c) whole set.

The functionalized structural parameter described above is then incorporated in place of the Bravais lattice number, and the results are shown in Fig. 3. Comparing this with Fig. 2, the difference is not great, nor can it be said that one is superior to the other. This could imply that the structure parameter does not play a very important role and, indeed, Hume-Rothery did not include it in 1934.

There are several ways to evaluate the performance of neural network predictions. The first and simplest is based on the value of the linear regression coefficient $R$ for the plot of predicted vs experimental output. A problem occurs when $R$ is low ($<0.9$), and the slope $M$ is close to unity or vice versa. Under these circumstances, slope $M$, intercept $B$, and $R$ can be combined to give one parameter $\varphi$ as defined above, which should be as close as possible to zero. This has the advantage of providing a single value that can be used as a criterion for parameter selection in a looped optimization program. However, in this composite parameter, the contribution of each of $M$, $B$ and $R$ is treated as equal, whereas a weighting might be preferable. An alternative method is to consider the mean error of the predicted value from the experimental value. There are three ways in which this error can be calculated: (1) the mean true error having the same unit as target values; (2) the mean modulus of error again having the same unit as target; and (3) the percentage error (as modulus) based on the experimental value. The problem of (1) is that a zero mean error can be obtained from very large deviations from the line, and the problem with (3) is that, when many experimental values are zero or close to zero, the percentage is infinite or very high, respectively. Thus (2) provides the best criterion and, furthermore, the standard deviation of this modulus of error gives a measure of spread and, hence, if large, indicates that the error is not systematic. So in assessing the correlation, two parameters are used: the correlation coefficient $R$ and the average absolute deviation between theory and prediction (mean modulus of error). The two are plotted in Fig. 4 for all data sets and show a good correlation at high $R$: at $R=1$, the mean modulus of error is zero.

These criteria are compared in the first two data rows of Table 3 for the testing set and whole set of the 60-alloy system from plots of predicted solubility against experimental solubility. The first thing to notice about this table is that the four ways of assessing the accuracy of prediction (testing set) concur. As the linear regression coefficient decreases, parameter $\varphi$ increases much more dramatically and can be regarded as a more sensitive indicator for this reason. Also, a simple calculation of the mean deviation of the predicted values from the best fit line (mean modulus of error) gives an estimate of the accuracy of prediction. This follows the trend of increasing $\varphi$ and reduced $R$.

![](./images/811947663229452290_6.jpg)

Fig. 3. Prediction of solubility using four functionalized parameters for the 60-alloy systems: atomic size, valence, electronegativity and structure. (a) Training set; (b) testing set; (c) whole set.

![](./images/811947663229452290_7.jpg)

Fig. 4. The correlation between R-values and mean modulus of error.

The standard deviation for this error is an indicator that the error is random rather than systematic and, if so, the standard deviation is expected to increase with the mean, as it does, in fact. The ratio of standard deviation of error to mean error is, in all but one case, greater than unity. These trends in the assessment criteria are consistent for both the testing set and the whole set.

The best predictive results for the network are obtained using the functionalized values of atomic size, valence and electronegativity to predict the original values of solubility for the 60-alloy data set used by Hume-Rothery himself, and the data are plotted in Fig. 2. Inclusion of the structural factor using the parameter described above weakens the predictive power of the network (Fig. 3). The reason for this slightly counter-intuitive finding is that crystallographic compatibility is likely to become more important at higher solubility levels, being essential for continuous solubility. However, the majority of data are at the low solubility end, where substitutional atoms are at a low coordination number. Another reason is that the number used to represent structure actually conceals crystallographic similarities, as discussed in more detail below, and there is not enough training data for the network to establish these similarities by itself. The structure parameter is used to assess the criterion for solubility that 'the same crystal structure for the two elements favours a wide solubility range' [64]. This makes it a type of classification problem, not completely the same as a mapping problem, and it could be argued that including it in this type of network is inappropriate.

<table><caption>Table 3 Comparison of criteria for predicting solubility using different combinations of parameter groups</caption>
<thead>
<tr>
<th>Conditions¹</th>
<th colspan="4">Test set</th>
<th colspan="4">Whole set</th>
</tr>
<tr>
<th></th>
<th>R</th>
<th>φ</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
<th>R</th>
<th>φ</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Size, valence, electronegativity (60 alloys)</td>
<td>0.992</td>
<td>0.0579</td>
<td>2.46</td>
<td>3.21</td>
<td>0.992</td>
<td>0.0422</td>
<td>1.65</td>
<td>1.94</td>
</tr>
<tr>
<td>Size, valence, electronegativity, structure (60 alloys)</td>
<td>0.976</td>
<td>0.168</td>
<td>6.98</td>
<td>4.58</td>
<td>0.975</td>
<td>0.0851</td>
<td>3.21</td>
<td>3.21</td>
</tr>
<tr>
<td>Size, valence, electronegativity (408 alloys)</td>
<td>0.695</td>
<td>0.662</td>
<td>7.01</td>
<td>14.1</td>
<td>0.768</td>
<td>0.631</td>
<td>6.30</td>
<td>12.7</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">¹ Using functionalized parameters.</td>
</tr>
</tfoot>
</table>

### 7.2. Testing Hume-Rothery's rules with the 408-alloy systems

From the results for the 60-alloy systems, it is clear that using the three functionalized values of parameters provides better results, so the same approach is adopted for testing the 408-alloy systems. This represents a nearly exhaustive set of known silver and copper alloys. The results, shown in the last row of Table 3 and plotted in Fig. 5, use the same format of inputs as those used for the 60-alloys set. When this method (omitting structural parameter) is applied to the larger 408-alloys data set, the regression coefficient is low (<0.9), and the comparison between different regression coefficient values has less meaning. Calculation of the mean modulus of error gives a less ambiguous estimate of the accuracy of prediction. The mean error of the prediction (testing set) increases by a factor of 3, and the linear regression coefficient drops well below 0.9. The mean error for the testing set and the whole set becomes closer, showing that this set does not train well, whereas for the 60-alloy set, the whole-set errors are much lower than the testing-set errors. It is an inevitable conclusion that the wider application of the rules introduces difficulties, some of which are discussed below.

### 7.3. Relative importance of the rules

It is interesting to enquire which of the four parameters, i.e., atomic size, valence, structure and electronegativity, is the most influential parameter, assuming that they are

![](./images/811947663229452290_8.jpg)

Fig. 5. Prediction of solubility using three functionalized parameters for the 408-alloy systems: atomic size, valency and electronegativity: (a) Training set, (b) testing set, (c) whole set.

independent of each other. The importance of the structural parameter has been tested and found not to play a very important overall role, although of course it does influence the possibility of continuous solubility.

The relative importance of size factor, valence and electronegativity is compared in Table 4. Using the same procedure (functionalized parameters including structure), the network is run with one parameter omitted at a time on the set of 60 systems.

In general, mean error (data columns 3 and 7) varies inversely with regression coefficient (data columns 1 and 5), and the standard deviation of error is between 1.1 and 1.8 times higher than the mean error. Using the mean error of the testing set as our main criterion for accuracy of prediction, the parameters atomic size, valence and electronegativity provide the strongest prediction of solubility and, of these, atomic size has the strongest effect because, when it is omitted, the error is highest (data row 2). Electronegativity appears to have a stronger influence than valence (data rows 3 and 4). In fact, these parameters are not wholly independent of each other. As mentioned by Hume-Rothery, they are related, and their interplay makes the determination of solubility very difficult [22]. As a result, determining the relative importance of each parameter is not easy; it can only be said descriptively that the atomic size and electronegativity play more important roles than the valence and structural parameters.

In the next stage, pairs of parameters are selected to predict solubility: (1) atomic size and valence factors; (2) atomic size and electronegativity factors; (3) atomic size and structural factors; (4) valence and electronegativity factors; (5) valence and structural factors; and (6) structure and electronegativity factors. They are shown in Table 5. The first thing to notice is that most of the mean errors are increased compared with the three-input tests reported in Table 4. The correlation coefficient for the testing set is generally higher than that for the whole set, because the partitioning procedure described above selects minimum $\varphi$ for the testing set as criteria rather than for the training set. An ideal procedure would be to find the correlation for both sets for each partition and select the distribution that gives the closest and highest $R$-values, as described by Malinov and Sha [4]. When the correlation is poor, however, as for the effects of valence and structure, the value of $R$ has little meaning. Table 5 confirms the deductions from the three-parameter tests that atomic size has the strongest effect on solubility, and the structural parameter the least effect. However, some ambiguity attends the relative roles of electronegativity and valence, which are reversed in this assessment of ranking. Pearson [65] states that when one

Table 4
Comparison of criteria for predicting solubility using different combinations of three parameters

<table>
<thead>
<tr>
<th>Conditions¹</th>
<th colspan="4">Test set</th>
<th colspan="4">Whole set</th>
</tr>
<tr>
<th></th>
<th>$R$</th>
<th>$\varphi$</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
<th>$R$</th>
<th>$\varphi$</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Size, valence, electronegativity (60 alloys)</td>
<td>0.992</td>
<td>0.0579</td>
<td>2.46</td>
<td>3.21</td>
<td>0.992</td>
<td>0.0422</td>
<td>1.65</td>
<td>1.94</td>
</tr>
<tr>
<td>Valence, electronegativity, structure (60 alloys)</td>
<td>0.867</td>
<td>0.308</td>
<td>8.19</td>
<td>11.7</td>
<td>0.924</td>
<td>0.197</td>
<td>4.20</td>
<td>6.34</td>
</tr>
<tr>
<td>Size, structure, electronegativity (60 alloys)</td>
<td>0.93</td>
<td>0.365</td>
<td>3.17</td>
<td>4.19</td>
<td>0.968</td>
<td>0.142</td>
<td>3.46</td>
<td>3.66</td>
</tr>
<tr>
<td>Size, valence, structure (60 alloys)</td>
<td>0.569</td>
<td>0.477</td>
<td>7.73</td>
<td>13.8</td>
<td>0.761</td>
<td>0.613</td>
<td>7.07</td>
<td>11.0</td>
</tr>
</tbody>
</table>
¹ Using functionalized parameters.

Table 5
Comparison of criteria for predicting solubility using different combinations of two parameters

<table>
<thead>
<tr>
<th>Conditions¹</th>
<th colspan="4">Test set</th>
<th colspan="4">Whole set</th>
</tr>
<tr>
<th></th>
<th>$R$</th>
<th>$\varphi$</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
<th>$R$</th>
<th>$\varphi$</th>
<th>Mean modulus of error (at.%)</th>
<th>SD of modulus of error (at.%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Size, valence (60 alloys)</td>
<td>0.852</td>
<td>0.470</td>
<td>4.47</td>
<td>2.50</td>
<td>0.496</td>
<td>1.36</td>
<td>9.52</td>
<td>14.3</td>
</tr>
<tr>
<td>Size, electronegativity (60 alloys)</td>
<td>0.679</td>
<td>0.860</td>
<td>6.99</td>
<td>4.83</td>
<td>0.495</td>
<td>1.36</td>
<td>10.3</td>
<td>13.8</td>
</tr>
<tr>
<td>Size, structure (60 alloys)</td>
<td>0.675</td>
<td>0.889</td>
<td>10.2</td>
<td>6.42</td>
<td>0.441</td>
<td>1.50</td>
<td>10.7</td>
<td>14.4</td>
</tr>
<tr>
<td>Valence, electronegativity (60 alloys)</td>
<td>0.91</td>
<td>0.153</td>
<td>7.31</td>
<td>10.1</td>
<td>0.925</td>
<td>0.184</td>
<td>4.54</td>
<td>6.06</td>
</tr>
<tr>
<td>Valence, structure (60 alloys)</td>
<td>0.459</td>
<td>1.02</td>
<td>12.4</td>
<td>11.9</td>
<td>0.662</td>
<td>0.886</td>
<td>9.82</td>
<td>11.3</td>
</tr>
<tr>
<td>Structure, electronegativity (60 alloys)</td>
<td>0.607</td>
<td>1.30</td>
<td>11.3</td>
<td>21.1</td>
<td>0.524</td>
<td>1.35</td>
<td>9.00</td>
<td>14.5</td>
</tr>
</tbody>
</table>
¹ Using functionalized parameters.

component in a binary alloy is very electropositive relative to the other, there is a strong tendency for them to form compounds of considerable stability in which valence rules are satisfied. Such alloys are said to exhibit a strong elec- trochemical factor and this is the strongest effect in deter- mining the constitution of alloys, and one which dominates all other effects such as energy band or geometrical factors.

## 8. Discussion
It is important to recognize that there are four factors that limit the predictive capability of the networks: (1) imperfections in the network configuration, which the authors have attempted to minimize through design; (2) paucity of learning data, which has been discussed above; (3) the generality of Hume-Rothery's Rules which were conceived as guidelines; and (4) the fact, recognized by Hume-Rothery and co-authors, that the available data are subject to inexactitudes.

### 8.1. The validity of ANN models
It can be seen that, if the parameters are selected appro- priately, as shown in Figs. 2 and 3, the prediction of the solid solubility limit by the ANN is reasonably consistent with Hume-Rothery's Rules. The ANN, as a method, can be treated as feasible, although it cannot be relied on defin- itively, and others have reiterated this. It may be regarded as a useful tool for cautious use in materials science, but the choice of right ANN plays a critical role in its success, espe- cially when the data set is restricted, as is often the case in materials science.

### 8.2. The effect of number of layers
Basheer and Hajmeer [2] indicate that the choice of the number of hidden layers and the number of neurons in the hidden layers are among the most important choices in ANN design. It is often claimed that, in most function approximation problems, one hidden layer is sufficient to approximate continuous functions [48,66]; two hidden lay- ers must generally be necessary for learning functions with discontinuities [67]. In this work, the type of function is not clear. Also the neural network user's guide [60] suggested that a two-hidden-layer sigmoid/linear network can repre- sent any function of input/output relationship. On these bases and looking at the results produced from this work, it can be seen that the choice of two-hidden layer network is a sensible one.

### 8.3. The effect of size of layer
The choice of size of the first hidden layer is critical in the ANN design. There are several rules of thumb available in the literature relating hidden layer size to the number of nodes in input $(N_{INP})$ and output $(N_{OUT})$ layers [48,67-71].
As Basheer and Hajmeer [2] suggested, the most popular way to find the optimal number of hidden nodes is by trial and error with one of those rules as a starting point. How- ever, facing exotic problems with high non-linearity and hysteresis such as are shown in Basheer's work [66,72], these 'rules of thumb' may need to be abandoned. There is some value in beginning with a small number of hidden nodes and building up iteratively to attain the accuracy required. This method is adopted in this work through implementation of the program.

### 8.4. The reliability of input parameters
Hume-Rothery et al. [22] themselves made it clear that the exact 'atomic diameter' of an element is always difficult to define. Their definition of atomic diameter, as given by the nearest-neighbour distance in a crystal of the pure metal, was used here but the 'radius' of an atom is probably affected by coordination number. Except for the heavy ele- ments, elements of the $B$ sub-groups tend to crystallize with coordination number $8-N$, where $N$ is the group to which the element belongs. This is due to the partly covalent nat- ure of the forces in these crystals and, except in Group IV B(diamond structure), results in the atoms having two sets of neighbours at different distances in the crystal. Cottrell [73] suggests that the concept of a characteristic size, which sug- gests hard spheres butted together, is doubtful. Allocating a single atomic diameter for each element, independent of its environment, and valences of solvent and solute is too sim- plistic an approach [62]. Furthermore, within the 408-alloy systems, the metallic radius of some elements could not be found, and the covalent radius was used instead. These fac- tors contribute to the errors for the prediction of solid sol- ubility limit and are to be distinguished from the intrinsic weaknesses of the ANN.

An early discovery by Hume-Rothery was that a metal of lower valence is more likely to dissolve one of higher valence than vice versa. However, more detailed examina- tion has not confirmed this. For example, silver dissolves about $20 \%$ aluminium, but aluminium dissolves about24% silver. For high valence, covalently bonded compo- nents, the relative valence factor applies. For example, copper dissolves about $11 \%$ of silicon, which behaves as a four-valent metal in forming $Cu-Si$ electron phase alloys, but the solubility of copper in covalently bonded silicon is negligible [73]. As a result, although Hume- Rothery [62] accepted that it is still a general principle that the solubility in the element of lower valency is of greater extent when dealing with alloys of univalent met- als copper, silver and gold with metals of higher valency, in its general form, this principle must be treated with caution.

The valencies of transition metals are variable and com-plex and have been analysed by Hume-Rothery et al. [74] and Cockayne and Raynor [75]. As suggested by Cottrell[73], due to the valency complication caused by partly filled d shells, the transition metal alloys generally do not follow

the rule. Gschneider [76] modified the relative valence rule so that the solubility is low when a metal in which $d$ orbitals strongly influence the valence behaviour is alloyed with a simple 'sp metal', but that the solubility is likely to be better in the $d$ metal than the reverse.

The electronegativity rule needs a scale, such as that given by Mullikan, based on the equation $\chi=\frac{1}{2}(I+A)$, where $I$ is the ionization energy, $A$ is electron affinity, and $\chi$ is Mullikan electronegativity. When divided by 2.8, this scale matches the empirical scale of Pauling reasonably well. In the case of transition metals, as emphasized by Watson and Bennett [77], the partly filled $d$ states of transition metals at energies near the Fermi energy influence electronegativity. Watson and Bennett presented an electronegativity scale for transition metals that matched Pauling's scale, and could be scaled by 2.8 to bring it to Mullikan's scale of $\chi$ values. Most importantly, Li and Xue [78] have mentioned that the 'although electronegativity is often treated as an invariant property of an atom, as in Pauling's scale, it actually depends on the chemical environment of the atom, e.g. valence state and coordination number'. The electronegativity values adopted in this project are based on Pauling's work, so the above effects are not entirely taken into account.

The method adopted for expressing structure parameter has some limitations. First, the expressions used to distinguish different crystal structures can conceal similarities. For unit cell length, $a=b=c$ and $a=b \neq c$ are distinguished but can have considerable similarity. Secondly, from this expression, the face centred cubic (fcc) and the hexagonal close packed (hcp) systems are expressed as quite distinct sets, but there are some similarities between these two structures. They are both close packed systems, and stacking faults can blur the difference. Indeed, the $\mathrm{Cu}$ and $\mathrm{Zn}$ systems demonstrate high solubility, even though one component, $\mathrm{Zn}$, is hcp and the $\mathrm{Cu}$ is fcc. The $\mathrm{Ag}$ and $\alpha$-Li system is a similar case. Thirdly, there are several complex structural systems that cannot be distinguished from other systems by using this expression, such as $\alpha$-Mn, whose structure is cI58, and $\beta$ $\mathrm{Mn}$, whose structure is cP20. These all affect the ability of the structure parameter to contribute to predicting the solubility.

### 8.5. The generality of Hume-Rothery's rules

Hume-Rothery and co-workers state: 'In general, the solubility limit is mainly determined by these factors, and it is their interplay that makes the results so complex' [22]. For the 60-alloy systems mentioned by Hume-Rothery in 1934, and using some of the parameter values that can be found in Hume-Rothery's paper or his book and others that follow his representations, the results for prediction of the solid solubility limit are satisfactory.

However, from theory as analysed by others in later work [38,73,79], and also from attempts to predict the solid solubility limit of the 408-alloy systems, it can be said that Hume-Rothery's Rules work properly in a certain range of alloy systems, but cannot be treated as general principles. Also, it needs to be said that, despite using Hume-Rothery's Rules, one cannot predict the solid solubility limits accurately. However, these rules are still useful guidelines for judging the solubility of alloy systems.

## 9. Conclusions

ANN offer materials scientists a relatively new tool for examining their data with the intention of making predictions while theory is still too opaque to be predictive. It is often the case in materials science that data sets are limited, either inherently, because of the limits imposed by the number of elements, or extrinsically, because of the high cost of experimentation. This study has taken one of the cornerstones of physical metallurgy and adopted ANN for predicting the solid solubility limit of alloy systems based on Hume-Rothery's Rules. Application of a two-hidden-layer backpropagation network with functionalized input parameter values for different classes and numbers of alloy systems, indicates that: (1) ANN is a useful tool for dealing with forecasting problems or mapping problems in materials science; (2) Hume-Rothery's general principles work well in several alloy systems, such that the ANN can be used to estimate solid solubility. When the 60-alloy systems used by Hume-Rothery are tested, the rules work very well, as demonstrated by the ANN correlation. The wider application of the rules to a set of 408 silver and copper alloys is less successful, but this is consistent with the inherent simplification of the rules which are already documented.

## References

[1] Dorsett H, White A. Overview of molecular modeling and ab initio molecular orbital methods suitable for use with energetic materials. Salisbury: Aeronautical and Maritime Research Laboratory; 2000. p. 3.

[2] Basheer IA, Hajmeer M. J Microbiol Methods 2000;43:3.

[3] Fausett LV. Fundamentals of neural networks: Architectures, algorithms and applications. Englewood Cliffs, NJ: Prentice-Hall; 1994.

[4] Malinov S, Sha W. Comput Mater Sci 2003;28:179.

[5] Jain AK, Mao JC, Mohiuddin KM. Computer 1996;29:31.

[6] Scott DJ, Coveney PV, Kilner JA, Rossiny JCH, Alford NMcN. J Eur Ceram Soc 2007;27:4425.

[7] Rumelhart DE, Hinton GE, Williams RJ. Learning internal representation by error propagation. In: Rumelhart DE, Mcclelland JL, editors. Parallel distributed processing: Exploration in the microstructure of cognition, vol. 1. Cambridge, MA: MIT Press; 1986.

[8] Arkadan AA, Chen Y, Subramaniam S, Hoole SRH. IEEE Trans Magn 1995;31:1984.

[9] Raj KH, Sharma RS, Srivastava S, Patvardhan C. Int J Mach Tools Manufact 2000;40:851.

[10] Guessasma S, Coddet C. Acta Mater 2004;52:5157.

[11] Huang CZ, Zhang L, He L, Sun J, Fang B, Zou B, et al. J Mater Process Technol 2002;129:399.

[12] Malinov S, Sha W. Mater Sci Eng A 2004;365:202.

[13] Martinez SE, Smith AE, Bidanda B. J Intell Manuf 1994;5:277.

[14] Bork U, Challis RE. Meas Sci Technol 1995;6:72.

[15] Larkiola J, Myllykoski P, Nylander J, Korhonen AS. J Mater Process Technol 1996;60:381.

[16] Gavard L, Bhadeshia H, MacKay DJC, Suzuki S. Mater Sci Technol 1996;12:453.

[17] Malinov S, Sha W, Guo Z. Mater Sci Eng A 2000;283:1.

[18] Homer J, Generalis SC, Robson JH. Phys Chem Chem Phys 1999;1:4075.

[19] Guo D, Wang YL, Nan C, Li LT, Xia JT. Sens Actuators A 2002;102:93.

[20] Cai K, Xia JT, Li LT, Gui ZL. Comput Mater Sci 2005;34:166.

[21] Schooling JM, Brown M, Reed PAS. Mater Sci Eng A 1999;260:222.

[22] Hume-Rothery W, Mabbott GW, Channel-Evans KM. Philos Trans Soc A 1934;233:1.

[23] Cooke CJ, Hume-Rothery W. J Less Common Met 1966;10:52.

[24] Pauling L. The nature of the chemical bond and the structure of molecules and crystals: An introduction to modern structural chemistry. Ithaca, NY: Cornell University Press; 1960. p. 88-95.

[25] Ohtani H, Ishida K. Thermochim Acta 1998;314:69.

[26] Kaufman L, Bernstein H. Computer calculation of phase diagrams: with special reference to refractory metals. New York: Academic Press; 1970.

[27] Hillert M. Calculations of phase equilibria. In: ASM, editor. American Society for Metals Seminar on Phase Transforma- tions. Metals Park (OH): ASM International; 1968. p. 181-218.

[28] Lim SS, Rossiter PL, Tibballs JE. Calphad 1995;19:131.

[29] Yang J, Silk NJ, Watson A, Bryant AW, Chart TG, Argent BB. Calphad 1995;19:415.

[30] Fries SG, Ansara I, Lukas HL. J Alloys Compd 2001;320:228.

[31] Ohnuma I, Fujita Y, Mitsui H, Ishikawa K, Kainuma R, Ishida K. Acta Mater 2000;48:3113.

[32] Du Z, Yang H, Li C. J Alloys Compd 2000;297:185.

[33] Liu ZK, Zhong Y, Schlom DG, Xi XX, Li Q. Calphad 2001;25:299.

[34] Darken LS, Gurry RW. Physical chemistry of metals. New York: McGraw-Hill; 1953.

[35] Chelikowsky JR. Phys Rev B 1979;19:686.

[36] Alonso JA, Simozar S. Phys Rev B 1980;22:5583.

[37] Alonso JA, Lopez JM, Simozar S, Girifalco LA. Acta Metall 1982;30:105.

[38] Zhang BW, Liao SZ. Shanghai Met 1999;21:3.

[39] Massalski TB, Murray JL, Bennett LH, Baker H, editors. Binary alloy phase diagrams. Metals Park (OH): American Society for Metals; 1986. p. 1-87. pp. 908-82.

[40] Stark JG, Wallace HG, editors. Chemistry data book. London: Mur- ray; 1982. p. 24. pp. 27-9.

[41] Guessasma S, Montavon G, Coddet C. Neural Networks, design of experiments and other optimizations methodologies to quantify parameter dependence of atmospheric plasma spraying. In: Marple R, Moreau C, editors. Proceedings of the Thermal Spray 2003: Advancing the science and applying the technology. Materials Park (OH): ASM International; 2003. p. 39.

[42] Axon HJ, Hume-Rothery W. Proc Roy Soc A 1948;193:1.

[43] Hassoun MH. Fundamentals of artificial neural networks. Cam- bridge, MA: MIT Press; 1995.

[44] Hopfield JJ. Proc Natl Acad Sci USA-Biol Sci 1984;81:3088.

[45] Hopfield JJ, Tank DW. Science 1986;233:625.

[46] Kohonen T. Self-organization and associative memory. Ber- lin: Springer; 1989.

[47] Zupan J, Gasteiger J. Anal Chim Acta 1991;248:1.

[48] Hecht-Nielsen R. Neurocomputing. Reading, MA: Addison-Wesley;1990.

[49] Hecht-Nielsen R. Neural Networks 1988;1:131.

[50] Zupan J, Gasteiger J. Neural networks for chemists: An introduc- tion. New York: VCH-Weinheim; 1993.

[51] Schalkoff RJ. Artificial neural networks. London: McGraw-Hill;1997.

[52] Pal SK, Srimani PK. Computer 1996;29:24.

[53] Attoh-Okine NO, Basheer IA, Chen D-H. Use of artificial neural networks in geomechanical and pavement systems. Washing- ton: Transportation Research Board, National Research Council;1999. p. 5.

[54] Specht DF. Neural Networks 1990;3:109.

[55] Vicino F. Substance Use Misuse 1998;33:335.

[56] Moffatt WG, editor. The handbook of binary phase diagrams. Sche- nectady (NY): General Electric Co.; 1977. Sections Ag-Al to Ag-Zr, Cu-Al to Cu-Zr.

[57] ASM handbook, vol. 3, Alloy phase diagrams. Metals Park (OH): ASM International; 1992.

[58] Aylward GH, Findlay T, editors. SI chemical data. New York: Wiley;1998. p. 6-13.

[59] Hume-Rothery W. Elements of structural metallurgy. London: Insti- tute of Metals; 1961. p. 107-10.

[60] Matlab. http://www.mathworks.com/access/helpdesk/help/pdf_doc/nnet/nnet.pdf/.

[61] Vegard L. Z Phys 1921;5:17.

[62] Hume-Rothery W, Smallman RE, Haworth CW. The structure of metals and alloys. London: Metals and Metallurgy Trust of the Institute of Metals and the Institution of Metallurgists; 1969.

[63] Hume-Rothery W. Acta Metall 1966;14:17.

[64] Wyatt OH, Dew-Hughes D. Metals, ceramics and polymers: An introduction to the structure and properties of engineering materi- als. London: Cambridge University Press; 1974. p. 42.

[65] Pearson WB. The crystal chemistry and physics of metals and alloys. New York: Wiley-Interscience; 1972. p. 68.

[66] Basheer IA. Comput Aided Civil Infrastruct Eng 2000;15:440.

[67] Masters T. Practical neural network recipes in C++. Boston: Aca- demic Press; 1993.

[68] Widrow B, Lehr MA. Proc IEEE 1990;78:1415.

[69] Upadhaya B, Eryureka E. Neural Technol 1992;97:170.

[70] Lachtermacher G, Fuller JD. J Forecast 1995;14:381.

[71] Jadid MN, Fairbairn DR. Eng Appl Artif Intell 1996;9:309.

[72] Basheer IA. Neuromechanistic-based modeling and simulation of constitutive behavior of fine-grained soils. PhD thesis, Kansas State University, Manhattan; 1998. 435p.

[73] Cottrell A. Concepts in the electron theory of alloys. London: IOM Communications; 1998. p. 56-7. pp. 72, 92.

[74] Hume-Rothery W, Irving HM, Williams RJP. Proc Roy Soc A 1951;208:431.

[75] Cockayne B, Raynor GV. Proc Roy Soc A 1961;261:175.

[76] Gschneider KA. L.S. Darken's contributions to the theory of alloy formation and where we are today. In: Bennett LH, editor. Theory of alloy phase formation. Warrendale: The Metallurgical Society of AIME; 1980. p. 1-34.

[77] Watson RE, Bennett LH. Phys Rev B 1978;18:6439.

[78] Li KY, Xue DF. J Phys Chem A 2006;110:11332.

[79] Miedema AR. J Less Common Met 1973;32:117.