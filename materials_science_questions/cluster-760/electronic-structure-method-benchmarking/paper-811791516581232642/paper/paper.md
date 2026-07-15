# Accurate Prediction of Enthalpies of Formation for a Large Set of Organic Compounds

CUN-XI LIU, $^{1}$ HAI-XIA WANG, $^{1}$ ZE-RONG LI, $^{1}$ CHONG-WEN ZHOU, $^{2}$ HAN-BING RAO, $^{1}$ XIANG-YUAN LI $^{2}$

$^{1}$ College of Chemistry, Sichuan University, Chengdu 610065, People's Republic of China
$^{2}$ College of Chemical Engineering, Sichuan University, Chengdu 610065,
People's Republic of China

Received 5 August 2009; Revised 21 February 2010; Accepted 25 February 2010
DOI 10.1002/jcc.21550
Published online 6 May 2010 in Wiley Online Library (wileyonlinelibrary.com).

**Abstract:** This article describes a multiparameter calibration model, which improves the accuracy of density functional theory (DFT) for the prediction of standard enthalpies of formation for a large set of organic compounds. The model applies atom based, bond based, electronic, and radical environmental correction terms to calibrate the calculated enthalpies of formation at B3LYP/6-31G(d,p) level by a least-square method. A diverse data set of 771 closed-shell compounds and radicals is used to train the model. The leave-one-out cross validation squared correlation coefficient $q^{2}$ of 0.84 and squared correlation coefficient $r^{2}$ of 0.86 for the final model are obtained. The mean absolute error in enthalpies of formation for the dataset is reduced from 4.9 kcal/mol before calibration to 2.1 kcal/mol after calibration. Five-fold cross validation is also used to estimate the performance of the calibration model and similar results are obtained.

© 2010 Wiley Periodicals, Inc. J Comput Chem 31: 2585-2592, 2010

**Key words:** enthalpy of formation; organic compounds; DFT; least-square

## Introduction

The accurate prediction of molecular thermochemical properties is one of the goals (vital tasks) in quantum chemical methods, especially the enthalpy of formation $(\Delta_{f}H_{298}^{0})$. A series of composite methods, such as Gaussian-$n$ ($n\ =\ 1\ -\ 4$) theories$^{1-8}$ and complete basis set methods (CBS) of Petersson and coworkers$^{9-12}$ (e.g., CBS-Q, CBS-QB3, and CBS-APNO), have been successfully used for the calculations of the enthalpy of formation. The $Gn$ theories employ a set of calculations with different levels of accuracy and basis sets with the goal of approaching the exact energy. In the most recent G4 scheme, $^{8}$ the mean absolute deviation (MAD) from experimental enthalpies of formation over G3/05 test set$^{7}$ (contains 270 molecules whose experimental $\Delta_{f}H_{298}^{0}$ are accurately known) is 0.80 kcal/mol within chemical accuracy, which makes a significant improvement over G3 theory (1.19 kcal/mol). In addition to the Gaussian-$n$ methods and CBS procedure, many model chemistry methods have been developed for accurate calculation of thermochemical properties of the compounds, such as the correlation consistent composite approch (ccCA) proposed by Deyonker et. al., $^{13}$ which contains no semiempirical or optimized parameters, the focal point method by Allen and coworkers, $^{14}$ the Weizmann (Wn) family of methods of Martin and coworkers, $^{15-18}$ and the High Accuracy Extrapolated $ab$ $initio$ Thermochemistry (HEAT) method by Stanton and coworkers, $^{19-21}$ the multicoefficient correlation method (MCCM) developed by Truhlar and coworkers. $^{22-24}$ Detailed discussion on the performance of these methods is beyond the scope of this article, but all these methods exhibit or exceed chamical accuracy of <1 kcal/mol. An alternative and accurate approach for calculation of thermochemical data is based on the coupled-cluster (CC) scheme with single and double excitation augmented by a perturbative treatment of triple excitations (CCSD(T))$^{25}$ and full coupled-cluster singles, doubles, and triples method ( CCSDT), $^{26}$ by employing the Dunning Correlation consistent basis sets (through aug-cc-pVDZ to aug-cc-pV5Z), $^{27}$ but, application of CC methods to larger chemical systems is limited by the rapidly increasing computational effort with growing number of electrons and basis functions. Nowadays, efficient implementations allow calculations at the CCSD(T) level of theory with up to 800 basis functions. $^{28}$ In the work of Dixon and coworkers, $^{29}$ the largest calculation performed was the CCSD(T) calculation on octane with 1468 basis

Additional Supporting Information may be found in the online version of this article.

**Correspondence to:** Z.-R. Li; e-mail: lizerong@scu.edu.cn

Contract/grant sponsor: National Natural Science Foundation of China;
contract/grant number: 20973118

© 2010 Wiley Periodicals, Inc.

functions (aug-cc-pVQZ basis set), taking 23 h on 1400 process- ors. However, all these methods are limited to small-sized mole- cules as they are very computational resource demanding and computational time consuming.

Compared with ab initio methods, DFT approaches can be applied to large molecular systems at a reasonable computa- tional cost. The computational time scales as the third power of the number of basis functions $(N^{3})$ in DFT calculations while $N^{5}$ in MP2, $N^{7}$ in QCISD(T) and CCSD(T), and $N^{8}$ in CCSDT. $^{30}$ The success of a DFT method in the prediction of electronic properties of atoms and molecules depends largely on the choice of the exchange-correlation energy functional $(E_{xc})$ . The increasing errors for large systems were observed already in previous works $^{2-4}$ and that have been attributed to an accu mulation of errors of local correlation effects. The MAD ofenthalpies of formation for B3LYP are 3.08 kcal/mol over G2/97 test sets (147) and 4.81 kcal/mol for G3/99 test sets (222). $^{4}$  Moreover, the B3LYP functional shows a particularly strong dependence on the number of electrons as its error increases dramatically from 2.25 to 3.40 and 9.01 kcal/mol for enthalpies of formation in G3/05 test set for the three subsets of mole-cules: those containing <8 pairs of valence electrons, $>8 \leq 14$  pairs of valence electrons and >14 pairs of valence electrons, respectively. $^{7}$ For these reasons, some schemes to correct the systematic errors of enthalpies of formation in the DFT methods have been recently proposed. In a series of articles of Liu et al., $^{31-33}$ a three-parameter linear regression technique was used to correct the calculated $\Delta_{f} H_{298}^{0}$ at B3LYP level with vari ous basis sets, the results are promising for some classes of compounds, such as straight-line alkanes. Another approach by combining quantum mechanical calculation and neural network(NN) correction was followed by Chen and coworkers, $^{34}$ who used a NN to calibrate the calculated standard heat of formation for 180 organic molecules at B3LYP/6-311+G(d,p) and B3LYP/6-311+G(3df,2p) levels, and the root mean square devi- ation of the calculated $\Delta_{f} H_{298}^{0}$ was reduced from 21.4 kcal / mol at B3LYP/6-311+G(d,p) level before calibration to 3.1 kcal/mol after calibration and from 12.0 kcal/mol at B3LYP/6-311+G(3df,2p) level before calibration to 3.3 kcal/ mol after calibration. Recently, Xu and coworkers $^{35}$ also combined the DFT theory with a NN correction to accurately predict the heat of formation, giving a MAD of 1.43 kcal/mol for the G3/99 setof 223 molecules and 1.48 kcal/mol for the X1/07 set of 393 molecules. Petersson et al. $^{11}$ used a least-square approach to correct the calculated $\Delta_{f} H_{298}^{0}$ values for the extended G2 neutraltest set by G2 method and various complete basis set (CBS) methods, and the errors are apparently reduced. For example, the MAD is reduced from 1.49 kcal/mol to 0.55 kcal/mol for G2 method after correction. These corrections are either atom based or bond based. Recently, an empirical localized orbital correction model providing insight into the fundamental limita- tions of DFT was reported by Friesner et al., $^{36}$ their method includes utilization of 22 optimized parameters that depend on atomic hybridization and bond types.

In this article, we proposed a linear regression correction method to calibrate the raw $\Delta_{f} H_{298}^{0}$ calculated by B3LYP method, based on a new dataset (771) covering a wide range of chemical structures. Hybrid feature selection method $^{37}$ was employed for effective descriptor or variable selection, and the parameters were determined by least-square regression method. A remarkable improvement in the MAD for prediction of enthal- pies of formation is observed, as well as a qualitative reduction in the number of outliers and size of the deviations from experi- ment of those outliers. Both the Leave-One-Out (LOO) method and leave-20%-out method (i.e., five-fold crossvalidation method) $^{37}$ are employed for the validation of the model.

## Computational Methods
All quantum chemical calculations were carried out with the Gaussian 03 program. $^{38}$ Geometry optimization for all the com pounds were carried out at B3LYP/6-31G(d,p) level of theory. Analytical harmonic vibration frequencies were computed at the same level to verify the character of the stationary point located(all real frequencies for a minimum) and give the zero-point energies (ZPE) and thermal corrections. In a second step, single point energy was calculated at the same level basing on the B3LYP/6-31G(d,p) optimized geometries. All calculations used the spin-restricted formalism for closed-shell systems and the spin-unrestricted formalism for open-shell systems.

DFT is the most well-suited ab initio technique for studies on large compounds and is chosen as the method to get the raw enthalpies of formation to be calibrated in this study. B3LYP/6-31 G(d, p) was chosen because B3LYP $^{39}$ was the most accurate of the hybrid-GGA class for calculating vibrational frequen- cies, $^{40}$ and was reported to yield accurate geometries and reason able energies. $^{41,42}$ Petersson et al. $^{11}$ recommended the use of B3LYP for geometrical optimization and frequency calculation in several of his CBS calculation methods. Recently, Jorgensen and coworkers $^{43}$ carried out a comparison of the effect of the choice of basis sets on the calculation of heats of formation for622 closed-shell organic compounds with B3LYP and they con- cluded that the quality of the B3LYP-based results was not very sensitive to the choice of basis set, and furthermore, the best results were obtained with 6-31G(d,p).

Standard enthalpies of formation are obtained using the atomization energy scheme. The detail process was fully dis- cussed in our previous study. $^{44} \Delta_{f} H_{298}^{0}$ of a compound is equal to enthalpies of formation of the gaseous atoms that constitute the compound minus the atomization enthalpy of the com- pound, see eq. (1). Only the lowest-energy conformer for a molecule is considered in the calculation of the enthalpy of formation.

$$
\begin{aligned}
\Delta_{\mathrm{f}} H_{298}^{\circ}\left(A_{n_{\mathrm{A}}} B_{n_{\mathrm{B}}} C_{n_{\mathrm{c}}} \cdots\right) & =n_{\mathrm{A}} \Delta_{\mathrm{f}} H_{298, \text { gas }}^{\circ}(A)+n_{\mathrm{B}} \Delta_{\mathrm{f}} H_{298, \text { gas }}^{\circ}(B) \\
& +n_{\mathrm{C}} \Delta_{\mathrm{f}} H_{298, \text { gas }}^{\circ}(C)+\cdots-\Delta_{\mathrm{a}} H_{298}^{\circ}\left(A_{n_{\mathrm{A}}} B_{n_{\mathrm{B}}} C_{n_{\mathrm{c}}} \cdots\right) \quad(1)
\end{aligned}
$$

The experimental enthalpies of formation of gaseous atoms are taken from NIST-JANAF Thermochemical Tables FourthEdition $^{45}$ with $\Delta_{f} H_{298, gas }^{\circ}(C)=171.3 kcal / mol, \Delta_{f} H_{298, gas }^{\circ}(H)=$ 52.1 kcal/mol, Δ_f H_298,gas^∘(O) = 59.6 kcal/mol, Δ_f H_298,gas^∘(N)=113.0 kcal/mol, Δ_f H_298,gas^∘(S) = 66.2 kcal/mol, Δ_f H_298,gas^∘(F)=19.0 kcal/mol, Δ_f H_298,gas^∘(Cl) = 29.0 kcal/mol, Δ_f H_298,gas^∘(Br)=26.7 kcal/mol.

### Data Sets

A number of test sets have been proposed to benchmark quantum chemistry methods. The $Gn$ test sets (G2/97,² G3/99,⁴ G3/05⁷) have been widely used for these purposes. The G3/05 test set, as an expansion of the G3/99 test set, includes 236 neutral molecules and 34 radicals for which the experimental enthalpies of formation are accurately known. Xu and coworkers³⁵ compiled the X1/07 data set (393) by adding 170 neutral molecules to the G3/99 set. Recently, Jorgensen and coworkers⁴³ accessed the performance of B3LYP density functional methods on a large dataset of 622 neutral, closed-shell compounds containing the elements C, H, N, and O. However, only small and middle-sized molecules were concerned in these datasets. In this work, we compiled a data set of 771 diverse molecules including 740 neutral closed-shell compounds and 31 radicals, up to 32 heavy atoms. The experimental enthalpies of formation for these compounds were obtained mainly from NIST-JANAF Thermochemical Tables Fourth Edition,⁴⁵ thermochemical tables of Pedley,⁴⁶ and NIST Chemistry WebBook⁴⁷ and literatures.²⁻⁴,⁴³,⁴⁸⁻⁵⁶ The dataset includes neutral compounds and radicals spanning the typical classes of organic compounds: alkanes, alkenes, alkynes, alcohols, acids, aldehydes, ketones, esters, ethers, diols, amino compounds, nitro compounds, nitroso compounds, cyanides, thiols, sulfides, sulfones, sulfoxides, and cyclic compounds, which are composed of elements C, H, O, N, S, F, Cl, and Br. Hence our data set is diverse in chemical structure and the developed model can be used for the calculation of thermochemical properties for a wide variety of molecular systems.

Compared with the previous datasets, large molecules containing up to 10 or more heavy atoms are included in our dataset, such as some species involved in the combustion reactions of large alkanes. Furthermore, some propellants and explosive compounds are included in our dataset, which have never been included in the previous datasets, such as G2/97, G3/99, and G3/05 test sets.

### Least-Square Calibration Model and Assessment

In this work, a multiparameter calibrating equation is used to predict the enthalpy of formation.

$$
\Delta_{\mathrm{f}} H_{\mathrm{ls}}^{0}=\Delta_{\mathrm{f}} H_{\mathrm{DFT}}^{0}+A+\sum_{i} c_{i} x_{i} \tag{2}
$$

In eq. (2), $\Delta_{\mathrm{f}} H_{\mathrm{DFT}}^{0}$ is the calculated enthalpy of formation by DFT method and $\Delta_{\mathrm{f}} H_{\mathrm{ls}}^{0}$ is the calibrated enthalpy of formation. $A$ is a constant in the calibration model. $x_{i}$ is the value of descriptor $i$ and $c_{i}$ is the corresponding coefficient of the descriptor. The coefficients in the calibration model are determined by the ordinary linear regression method.

First, a leave-one-out (LOO) cross validation procedure is used for the descriptor selection. Crossvalidation is a resampling technique that is used for assessment of the statistics models. In LOO, all data with the exception of one compound are used to train the model. The model built in this way is used to predict the property of compound that is not in the training set. The process is repeated for every compound in the dataset and the averaged predicted results are reported. The outcome from this procedure is a cross-validated squared correlation coefficient $q^{2}$, which is calculated according to the formula⁵⁷

$$
q^{2}=1-\frac{\sum\left(\Delta_{f} H_{\mathrm{LS}, i}-\Delta_{f} H_{\mathrm{exp}, i}\right)^{2}}{\sum\left(\Delta_{f} H_{\mathrm{exp}, i}-\Delta_{\mathrm{f}} \bar{H}_{\mathrm{exp}}\right)^{2}} \tag{3}
$$

where $\Delta_{\mathrm{f}} \bar{H}_{\text {exp }}$ is the averaged $\Delta_{\mathrm{f}} H_{\text {exp }}$(over the entire dataset) and the summations in eq. (3) are performed over all compounds in the dataset.

Then, a final model is built from the full dataset by a leastsquare procedure and squared correlation coefficient $r^{2}$ is defined as⁵⁷

$$
r^{2}=\frac{\left(\sum\left(\Delta_{\mathrm{f}} H_{\mathrm{LS}, i}-\Delta_{\mathrm{f}} \bar{H}_{\mathrm{LS}}\right)\left(\Delta_{\mathrm{f}} H_{\mathrm{expt}, i}-\Delta_{\mathrm{f}} \bar{H}_{\text {expt }}\right)\right)^{2}}{\sum\left(\Delta_{\mathrm{f}} H_{\mathrm{LS}, i}-\Delta_{\mathrm{f}} \bar{H}_{\mathrm{LS}}\right)^{2} \sum\left(\Delta_{\mathrm{f}} H_{\mathrm{expt}, i}-\Delta_{\mathrm{f}} \bar{H}_{\text {expt }}\right)^{2}} \tag{4}
$$

### Descriptors Construction and Selection

The key point to these statistical correction methods is the selection of the descriptors to encode the molecular structures. The most widely used calibration method is the atom additivity method, where the descriptors are the number of atoms in each atom types.³¹⁻³³,⁵⁸ Another calibration scheme is based on the bond additivity model developed by Petersson et al.,¹¹ where the descriptors are the numbers of bonds in each bond types. In other studies, other descriptors have been used to improve the accuracy of calibration models for prediction of thermochemical properties. In the NN scheme of Chen and coworkers,³⁴,⁵⁹ the total number of atoms, zero-point energy, number of double bonds, and number of hydrogen atoms are selected. Fan and coworkers⁶⁰ choose the number of lone pair electrons, the number of bonding electrons, the number of inner layer electrons and the number of unpaired electrons as descriptors. In addition to that, the number of $\beta$ and $\alpha$ valence electrons are selected as descriptors for the high level correction (HLC) in $Gn$ families.¹⁻⁸ The G3-like higher level correction parameters based on number of unpaired and lone pair/pi electrons in the atoms or molecules is included in modified KMLYP functional of Kang and Musgrave.⁶¹ The main differences between these works are the datasets and descriptors. In this study, the first class of descriptors are the number of atoms for C, H, O, N, S, F, Cl, Br ($N_{\mathrm{C}}$, $N_{\mathrm{H}}$, $N_{\mathrm{O}}$, $N_{\mathrm{N}}$, $N_{\mathrm{S}}$, $N_{\mathrm{F}}$, $N_{\mathrm{Cl}}$, and $N_{\mathrm{Br}}$). Knoll and coworkers³⁶ showed that nondynamical correlation in every chemical bond type is quite similar and Melius and coworkers⁶² successfully applied the bond additivity correction (BAC) procedures for the calibration of calculated thermochemical properties by G3-based methods. Therefore the second class of descriptors used in this study is the number of bond types. Because it is difficult to distinguish between $\mathrm{N-O}$ and $\mathrm{N=O}$ bond in $-\mathrm{NO}_{2}$, the number of $\mathrm{NO}_{2}$ is also used as a descriptor in this class. The third class of descriptors used in this study is the ring-based descriptors: number of three member rings and four member rings, number of rings with size larger than four and number of aromatic rings. The forth class of descriptors is lone electron based descriptors.

**Table 1. Full List of Descriptors and the Regression Coefficients for the Selected Descriptors.**

<table>
  <thead>
    <tr>
      <th>No.</th>
      <th>Abbreviation</th>
      <th>Description</th>
      <th>Coefficient</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>$N_{C}$</td>
      <td>The number of carbon atoms</td>
      <td>−2.50</td>
    </tr>
    <tr>
      <td>2</td>
      <td>$N_{O}$</td>
      <td>The number of oxygen atoms</td>
      <td>−0.55</td>
    </tr>
    <tr>
      <td>3</td>
      <td>$N_{S}$</td>
      <td>The number of sulfur atoms</td>
      <td>−6.09</td>
    </tr>
    <tr>
      <td>4</td>
      <td>$N_{F}$</td>
      <td>The number of fluorine atoms</td>
      <td>3.30</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$N_{Cl}$</td>
      <td>The number of chlorine atoms</td>
      <td>−5.06</td>
    </tr>
    <tr>
      <td>6</td>
      <td>$N_{Br}$</td>
      <td>The number of bromine atoms</td>
      <td>3.36</td>
    </tr>
    <tr>
      <td>7</td>
      <td>$N_{CCD}$</td>
      <td>The number of C=C double bond</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>8</td>
      <td>$N_{NH}$</td>
      <td>The number of N−H single bond</td>
      <td>−1.33</td>
    </tr>
    <tr>
      <td>9</td>
      <td>$N_{OH}$</td>
      <td>The number of O−H single bond</td>
      <td>−3.57</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$N_{COS}$</td>
      <td>The number of C−O single bond</td>
      <td>−0.61</td>
    </tr>
    <tr>
      <td>11</td>
      <td>$N_{CND}$</td>
      <td>The number of C=N double bond</td>
      <td>1.12</td>
    </tr>
    <tr>
      <td>12</td>
      <td>$N_{NND}$</td>
      <td>The number of N=N double bond</td>
      <td>−4.30</td>
    </tr>
    <tr>
      <td>13</td>
      <td>$N_{SOD}$</td>
      <td>The number of S=O double bond</td>
      <td>−17.68</td>
    </tr>
    <tr>
      <td>14</td>
      <td>$N_{5,6,7,8\ ring}$</td>
      <td>The number of rings with size larger than 4</td>
      <td>−3.14</td>
    </tr>
    <tr>
      <td>15</td>
      <td>$N_{RA}$</td>
      <td>The number of heavy atoms bonded to the radical atom</td>
      <td>2.21</td>
    </tr>
    <tr>
      <td>16</td>
      <td>$I_{RT}$</td>
      <td>Indicator for a radical on a triple bond (1 if a molecule has a radical resides on a atom that is part of a triple bond, 0 otherwise)</td>
      <td>−15.91</td>
    </tr>
    <tr>
      <td>17</td>
      <td>ZPE</td>
      <td>zero-point energy of molecule (in kcal/mol)</td>
      <td>0.03</td>
    </tr>
  </tbody>
</table>

This class of descriptors includes the number of unpaired electrons and the number of lone pairs. As the extent of the delocalization of the lone electrons on O, N, and S, the number of lone pair on O, N, S are used separately. However, any O atoms have two lone pairs, the number of O atoms and the number of lone pairs on O atoms are completely correlated. Therefore, the number of lone pair on O atoms is not considered as a descriptor. The fifth class of descriptors is the radical environmental correction terms: the number of H atoms bonded to the radical atom, the number of heavy atoms bonded to the radical atom, indicator for a radical on a double bond (1 if a molecule has a radical residing on a atom that is part of a double bond, 0 otherwise), indicator for a radical on a triple bond (1 if a molecule has a radical residing on a atom that is part of a triple bond, 0 otherwise). The final class of descriptors contains only one descriptor: zero-point energy. A full list of theses descriptors is given in Table S2 in the supporting information.

Because some of the descriptors listed in Table S2 in supporting information are redundant, a key problem in our calibration model is to remove these redundant descriptors and select the descriptors relevant to the calibration model in eq. (2).

The first step of feature selection is the feature preprocessing: one of any pair of descriptors with the absolute value of Pearson correlation coefficient above 0.90 is removed.⁶³ Secondly, Metropolis Monte Carlo simulated annealing procedure is further applied to find the optimal subset of 39 molecular descriptors. Here, the fitniess function $Q$ is the cross-validated squared correlation coefficient $q^{2}$ defined in eq. (3) and the algorithm is as follows: Step (1): Set the initial parameter $T$, which is analogous to simulation temperature, reasonably large; Step (2):Generate a trial solution to the underlying optimization problem, i.e., a feature subset $S_{0}$ based on a random selection of descriptors; Step (3): Calculate the value of the fitness function $Q_{0}$ for $S_{0}$; Step (4): Perturb the trial solution to obtain a new trial solution, i.e., a new feature subset $S$; Step (5): Calculate the value of the fitness function $Q$ for $S$; Step (6): Apply the optimization criteria: If $Q_{0} \leq Q$, the new solution $S$ is accepted; if $Q_{0} > Q$, the new solution is accepted only if the Metropolis criterion, i.e.

$$
rnd < e^{-(Q_{0}-Q)/T} \tag{5}
$$

is satisfied, where $rnd$ is a random number uniformly distributed between 0 and 1; Step (7): Set $S$ as $S_{0}$ and $Q$ as $Q_{0}$ if the new solution is accepted and repeat step 4–6 until a predefined umber of equilibrium steps at this temperature are obtained; Step (8): Lower the parameter $T$ and repeat step 2–7 until the temperature approaches zero or the solution is converged.

## Results and Discussion

### Feature Selection

In the first step of feature selection, i.e., the preprocessing step, eight descriptors are eliminated and the number of the descriptors is reduced from 47 to 39, descriptors that are removed in preprocessing step can be seen in supporting information.

In the second step of feature selection, Monte Carlo simulated annealing method described above is used to find the optimal subset of descriptors from the 39 descriptors. In this process, the fitness function is the leave-one-out cross validation $q^{2}$ and the leave-one-out is performed for the full data set. Finally, an optimal subset with 17 descriptors is obtained and $q^{2}$ is 0.84, indicating that the model using this set of descriptors has very good prediction ability. These descriptors selected and their corresponding coefficients are listed in Table 1. It is worthy of note that the contribution of each descriptor to the calibration can not be simply meseured by its magnitude of the regression coefficient, because standardization is not applied to the descriptors and the range of the values of the descriptors may be very different. For example, in Table 1, descriptor 17 scales the zero-point energy by a factor of 0.03. Although this coefficient is very small, the unit used for this descriptor is kcal/mol and its magnitude is very large compared with other descriptors, hence it is not allowed to be removed from the descriptor list.

### Calibration Model

A calibration model is build from the full dataset using the selected 17 descriptors by ordinary linear regression method. The Coefficients $(c_{i})$ in eq. (2) are listed in Table 1. The constant $A$ in eq. (2) is 2.33 kcal/mol and the squared correlation coefficient $(r^{2})$ for the model is 0.86. The units of coefficients for descriptor #1–16 in Table 1 are kcal/mol and unit of coefficient for descriptor #17 in Table 1 is dimensionless. A full tabulation of predicted results and experimental enthalpies of formation is presented in Table S1 of the supporting information.

**Table 2.** Mean Absolute Errors (MAE) and Max Absolute Error (AE) in Calculated Enthalpies of Formation for Molecules in this Work (kcal/mol).

| Class$^{\text{a}}$ | N$^{\text{b}}$ | B3LYP       |             | Calibration Model |             |
|---------------------|----------------|-------------|-------------|-------------------|-------------|
|                     |                | MAE         | Max AE      | MAE               | Max AE      |
| Full dataset        | 771            | 4.9         | ---         | 2.1               | ---         |
| CH                  | 230            | 3.6         | 32.2        | 1.7               | 12.8        |
| CHO                 | 210            | 3.6         | 19.8        | 2.3               | 12.2        |
| CHN                 | 134            | 3.3         | 14.6        | 2.3               | 8.8         |
| CHS                 | 87             | 12.4        | 53.9        | 2.1               | 8.8         |

$^{\text{a}}$CH are compounds composed of only C, H atoms, including alkanes, alkenes, alkynes, aromatic hydrocarbon compounds, and cyclic hydrocarbon compounds; CHO are compounds composed of only C, H, O atoms, including alcohols, acids, aldehydes, ketones, esters, ethers, diols and O-heterocyclic compounds; CHN are compounds composed of at least C, H, N, including amino compounds, nitro compounds, nitroso compounds, cyanide compounds and N-heterocyclic compounds; CHS are compounds composed of at least C, H, S, including thiols, sulfides, sulfones, sulfoxides and S-heterocyclic compounds.
$^{\text{b}}$The number of compounds in the data set.

The compounds in the dataset are divided into four classes. The mean absolute errors (MAE) for the full dataset and each class are given in Table 2. As shown in Table 2, the MAE of the calculated enthalpies of formation at B3LYP level is reduced from 4.9 to 2.1 kcal/mol after calibration for the full dataset molecules. The results are comparable to the performance of the model of Jorgensen and coworkers,⁴³ who implemented empirical dispersion correction terms within DFT to calculate enthalpy of formation of 622 neutral compounds and the MAEs are 2.6 kcal/mol for B3LYP/6-31G(d,p) and 2.7 kcal/mol for B3LYP/6-31G+(d,p). Recently, Hehre and coworkers⁶⁴ developed an efficient model for calculating heats of formation by taking atom counts, mulliken bond orders, and HF/6-31G* and RI-MP2 energies in linear regression model. The model reproduces experimental heats of formation for a set of 1805 diverse organic molecules from NIST thermochemical database with MAE of 8.5 kJ/mol (2.0 kcal/mol). Considering the diversity of our dataset, such accuracy for our model in prediction of enthalpy of formation is encouraging.

For molecules with absolute errors of $\Delta_{\text{f}}H_{298}^{0}$ larger than 40 kcal/mol at B3LYYP level, an apparent improvement in accuracy is obtained and the results are listed in Table 3. A point need to be emphasized is that each of the molecules in Table 3 contain at least two sulfur-oxygen double bonds (S$\text{=}$O), therefore, the descriptor of number 35 was solely needed to correct these molecules containing S$\text{=}$O bonds. There are nine molecules in Table 3 and they are sulfuric compounds, indicating that the performance of B3LYP functional in calculations of enthalpy of formation for sulfuric compounds is not as well as for other compounds. For sulfuryl chloride (Cl₂O₂S), the calculated $\Delta_{\text{f}}H_{298}^{0}$ at B3LYP level has the maximum absolute error 53.9 kcal/mol among the full dataset. After calibration, an apparent improvement in accuracy is obtained, the deviation being reduced to 5.9 kcal/mol. However, the calibration model does not improve calculated results of enthalpies of formation at B3LYP/6-31G(d,p) level obviously for some of the compounds in the dataset. For example, the absolute errors for 2,3,3,4-tetramethylpentane (C₉H₂₀), trans-4-methylcyclohexanol (C₇H₁₄O), 3,5,7,9-tetraoxaundecane (C₇H₁₆O₄), and n-butyl trichloroacetate (C₆H₉Cl₃O₂) are 11.9, 19.9, 15.6, 28.5 kcal/mol before calibration and 12.8, 12.2, 10.6, 10.1 kcal/mol after calibration. The absolute errors are still larger than 10 kcal/mol after calibration. The reason for the large errors may be two fold: (1) Not all of the errors of the enthalpies of formation calculated at B3LYP level are systematic error and hence this part of error can not be canceled after calibration. (2) The constructed descriptors can not capture all the structural features of the studied compounds.

A number distribution histogram of species for errors in calculated enthalpies of formation (experiment minus theory) is

**Table 3.** Improvements in Accuracy for Molecules with Absolute Error Larger than 40 kcal/mol (kcal/mol).

| No. | species                    | $\Delta_{\text{f}}H_{\text{exp}}^{0}(298\text{K})^{\text{a}}$ | Error$^{\text{b}}$ |             | Improvement$^{\text{c}}$ |
|-----|----------------------------|---------------------------------------------------------------|---------------------|-------------|--------------------------|
|     |                            |                                                               | B3LYP               | LS          |                          |
| 1   | *tert*-Butyl methyl sulphone | $-113.2^{\text{d}}$                                           | $-42.8$             | $-4.0$      | 38.8                     |
| 2   | Allyl methyl sulfone       | $-73.0^{\text{d}}$                                            | $-44.4$             | $-5.1$      | 39.3                     |
| 3   | Di-*tert*-Butyl sulfone    | $-130.6^{\text{d}}$                                           | $-46.8$             | $-7.1$      | 39.7                     |
| 4   | 3-(Ethylsulphonyl)-1-propene | $-77.0^{\text{d}}$                                            | $-41.7$             | $-2.1$      | 39.6                     |
| 5   | Sulfur trioxide            | $-94.6^{\text{e}}$                                            | $-47.4$             | $8.7$       | 38.7                     |
| 6   | Sulfuryl chloride          | $-84.8^{\text{e}}$                                            | $-53.9$             | $-5.9$      | 48.0                     |
| 7   | Diisobutyl sulfone         | $-128.0^{\text{d}}$                                           | $-47.5$             | $-8.0$      | 39.5                     |
| 8   | *tert*-Butyl ethyl sulfone | $-117.5^{\text{d}}$                                           | $-41.3$             | $-2.2$      | 39.1                     |
| 9   | Butyl methyl sulfone       | $-109.9^{\text{d}}$                                           | $-41.7$             | $-3.0$      | 38.7                     |

$^{\text{a}}$Experimental enthalpy of formation at 298 K.
$^{\text{b}}$Error = $\Delta_{\text{f}}H_{\text{exp}}^{0} - \Delta_{\text{f}}H_{\text{calc.}}^{0}$. The left column is $\Delta_{\text{f}}H_{298}^{0}$ calculated by B3LYP/6-31G(d,p) method, and the right coumn is $\Delta_{\text{f}}H_{298}^{0}$ after least-square calibration.
$^{\text{c}}$The absolute error of B3LYP/6-31G(d,p) results minus that of least-square results.
$^{\text{d}}$Experimental value from ref. 33.
$^{\text{e}}$Experimental value from NIST Chemistry WebBook.³⁴

![](./images/811791516581232642_1.jpg)

Figure 1. Distribution of species in different error (experiment minus theory) range for B3LYP enthalpies of formation before and after calibration. The number of molecules with MAE larger than 12 kcal/mol are added together.

shown in Figure 1. The number distribution histogram of species for errors demonstrates that the multiparameter calibration model has substantially removed the systematic component of error. After calibration, 60% (468/771) compounds in the dataset have deviations within the range from -2 to 2 kcal/mol, while only 39% compounds fall in this range before calibration. And 86% (662/771) compounds in the dataset have deviations within -4 to 4 kcal/mol after calibration, while 63% compounds in the dataset have deviations within -4 to 4 kcal/mol before calibration. Therefore, the calibration has a substantial improvement over the $\Delta_{\mathrm{f}} H_{298}^{0}$ by B3LYP method.

A lot of attempts have been made to decrease the systematic errors of DFT method for calculations of the enthalpies of formation of hydrocarbons by using statistical calibration methods. In 1996, Mole et al. $^{65}$ used an atom equivalent method in conjunction with six DFT methods and the root mean square deviations between the calculated and experimental $\Delta_{\mathrm{f}} H^{0}$ for 23 hydrocarbons ranged from 1 to 6 kcal/mol. In 1998, Labanowski et al. $^{66}$ used bond and group equivalents to calibrate the calculated results at B3LYP/6-31G* and the accuracy is 0.36 kcal/ mol. In 2003, Saeys et al. $^{67}$ adapted a systematic correction of -1.29 kJ/mol per C atom and -0.28 kJ/mol per H atom for a set of 58 hydrocarbons ranging from $C_{1}$ and $C_{10}$ and the MAEs for the atomic energies were reduced from 7.44 to 2.19 kcal/mol for B3LYP/6-31G(d) and from 11.97 to 3.09 kcal/mol for B3LYP/6-311G(d,p). In 2006, Liu et al. $^{33}$ used a three-parameter (number of C atoms, number of H atoms, and constant term) modification equation to accurately predict enthalpy of formation for a set of 65 hydrocarbons and a MAE ranging from 1.3-1.6 kcal/mol was obtained. In our work, the dataset contains 230 hydrocarbon compounds up to 32 C atoms, consisting of alkanes, alkenes, alkynes, polycyclic aromatic hydrocarbon compounds, and cyclic hydrocarbon compounds. The MAE of our calibrated results for hydrocarbon compounds is 1.7 kcal/mol, which is comparable to the best literature-reported results, however, our dataset for hydrocarbon compounds is much larger and more structurally diverse.

For the enthalpies of formation of C-H-O composite compounds, in 2005, Liu et al. $^{32}$ adopted three parameteric (number of C atoms, number of H atoms, and constant term) modification equation to accurately predict enthalpy of formation for $C_{1}-C_{10}$ straight-chain aldehydes, alcohols, and alkoxides and a MAE of 0.5 kcal/mol was obtained. In this study, the C-H-O composite compounds in our dataset include alcohols, acids, aldehydes, ketones, esters, ethers, diols, and O-heterocyclic compounds. After calibration, the MAE of enthalpies of formation of 210 compounds is reduced from 3.6 to 2.3 kcal/mol.

For the enthalpies of formation of nitrogen-containing compounds, extensive efforts have been made. In 1999, Rice et al. $^{68}$ used the B3LYP/6-31G(d) method and atomic corrections to predict enthalpies of formation of energetic materials. The calculated gas-phase enthalpies of formation had a root mean square deviation of 3.1 kcal/mol from 35 experimental values. In 2000, Wilcox et al. $^{69}$ developed an similar approach combining B3LYP model and seven-parameter atom/group additivity scheme, which reduces the MAE from 3.1 to 1.1 kcal/mol for 18 singlet species and from 5.1 to 1.3 kcal/mol for12 free radicals. In this study, the dataset has 134 nitrogen-containing compounds comprised of various nitrogen-containing functional groups, such as nitro, nitrate, cyanide, amino groups, and N-heterocycles. The MAE for these compounds is 2.3 kcal/mol after calibration.

There is no report to develop the calibration model for prediction of enthalpies of formation of sulfur-containing compounds. In this study, the MAE of enthalpies of formation of 87

Table 4. Performance of the Calibration Model Estimated by Five-Fold cross validation.

<table>
<thead>
<tr>
<th rowspan="2">Cross validation sets</th>
<th colspan="3">Training set</th>
<th colspan="3">Test set</th>
</tr>
<tr>
<th>Number of Species</th>
<th>$r^{2a}$</th>
<th>MAE (kcal/mol)</th>
<th>Number of Species</th>
<th>$r^{2a}$</th>
<th>MAE (kcal/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>616</td>
<td>0.84</td>
<td>2.1</td>
<td>155</td>
<td>0.89</td>
<td>2.2</td>
</tr>
<tr>
<td>2</td>
<td>617</td>
<td>0.87</td>
<td>2.1</td>
<td>154</td>
<td>0.78</td>
<td>2.2</td>
</tr>
<tr>
<td>3</td>
<td>617</td>
<td>0.87</td>
<td>2.1</td>
<td>154</td>
<td>0.78</td>
<td>2.2</td>
</tr>
<tr>
<td>4</td>
<td>617</td>
<td>0.87</td>
<td>2.0</td>
<td>154</td>
<td>0.79</td>
<td>2.3</td>
</tr>
<tr>
<td>5</td>
<td>617</td>
<td>0.85</td>
<td>2.1</td>
<td>154</td>
<td>0.87</td>
<td>2.1</td>
</tr>
</tbody>
</table>

$^{a}$Squared correlation coefficient.

sulfur-containing compounds is reduced from 12.4 kcal/mol before calibration to 2.1 kcal/mol after calibration. Hence, the calibration model of our work is effective in prediction of enthalpies of formation for sulfur-containing compounds.

In this work, five-fold cross validation method is also used to validate the prediction ability of the calibration model. During five-fold cross validation, the dataset is divided into five subsets of approximately equal size, where each compound in the training set appears only once. One subset of the compounds is withheld for testing while the remaining subsets are used for training. This process is repeated five times for all five subsets, respectively, to provide predictions of all compounds in the dataset when they are not included in the training set. Following five times of training and testing, five results are produced. The performance of the calibration model is given in Table 4. The results of five-fold cross validation are at the same level with the results of leave-one-out procedure, with MAE of 2.1 kcal/ mol for training set and 2.2 kcal/mol for test set.

In summary, a calibrated model is developed for a wide diverse set of organic compounds and the predicted accuracies for each class of compounds are comparable to the models developed individually by other groups.

## Conclusion

In this article, a multiparameter calibration model has been devel- oped, to improve the accuracy of DFT methods for prediction of enthalpies of formation $\Delta_{f}H^{0}$ at 298K for 771 organic molecules with diverse chemical structures. The calibration model combines the DFT energy at the level of B3LYP/6-31G(d,p)//B3LYP/6-31G(d,p) with linear correction parameters obtained by a least- square procedure. The multiparameter calibration model effec- tively reduces the MAE from experiment in enthalpy of formation from 4.9 to 2.1 kcal/mol. The results reveal that B3LYP/6-31G(d,p) in combination with least-square calibration can be used to the accurate prediction of $\Delta_{f}H^{0}$, significantly eliminating sys tematic errors, which increase with molecular size.

This work indicates that errors in electronic energies obtained from *ab initio* calculations due to the finite size of the basis sets and the limited level of correction for the electron correlation are systematic and additive and hence the errors can be reduced by a systematic calibration model. In this way, the enthalpies of formation of compounds can be calculated by B3LYP method and accurate results can be obtained by calibration, making B3LYP method a very viable method for prediction of enthal- pies of formation of molecules, especially for larger molecules, for which the G-*n* method, CBS method, CCSD(T) method are computationally expensive, and sometimes are prohibitive. Fur- ther work that calculates the reaction activation energy by multi- parameter model will be done.

## References

1. Curtiss, L. A.; Raghavachari, K.; Pople, J. A. J Chem Phys 1993, 98, 1293.
2. Curtiss, L. A.; Raghavachari, K.; Redfern, P. C.; Pople, J. A. J Chem Phys 1997, 106, 1063.
3. Redfern, P. C.; Zapol, P.; Curtiss, L. A.; Raghavchari, K. J Chem Phys 2000, 112, 5850.
4. Curtiss, L. A.; Raghavachari, K.; Redfern, P. C.; Pople, J. A. J Chem Phys 2000, 112, 7374.
5. Curtiss, L. A.; Redfern, P. C.; Raghavachari, K.; Pople, J. A. J Chem Phys 2001, 114, 108.
6. Curtiss, L. A.; Redfern, P. C.; Raghavachari, K.; Pople, J. A. Chem Phys Lett 2002, 359, 390.
7. Curtiss, L. A.; Redfern, P. C.; Raghavachari, K. J Chem Phys 2005, 123, 124107.
8. Curtiss, L. A.; Redfern, P. C.; Raghavachari, K. J Chem Phys 2007, 126, 084108.
9. Montgomery, J. A.; Ochterski, J. W.; Perterson, G. A. J Chem Phys 1994, 101, 5900.
10. Ochterski, J. W.; Petersson, G. A.; Montgomery, J. A. J Chem Phys 1995, 104, 2598.
11. Petersson, G. A.; Malick, D. K.; Wilson, W. G.; Ochterski, J. W.; Montgomery, J. A.; Frisch, M. J. J Chem Phys 1998, 109, 10570.
12. Montgomery, J. A.; Frisch, M. J.; Ochterski, J. W.; Perterson, G. A. J Chem Phys 2000, 112, 6532.
13. Deyonker, N. J.; Cundari, T. R.; Wilson, A. K. J Chem Phys 2006, 124, 114104.
14. Schuurman, M. S.; Muir, R. S.; Allen, W. D.; Schaefer, H. F. J Chem phys 2004, 120, 11586.
15. Martin, J. M. L.; Oliveira, G.de. J Chem Phys 1999, 111, 1843.
16. Parthiban, S.; Martin, J. M. L. J Chem Phys 2001, 114, 6014.
17. Boese, A. D.; Oren, M.; Atasoylu, O.; Martin, J. M. L.; Kállay, M.; Gauss, J. J Chem Phys 2004, 120, 4129.
18. Karton, A.; Rabinovich, E.; Martin, J. M. L.; Ruscic, B. J Chem Phys 2006, 125, 144108.
19. Tajti, A.; Szalay, P. G.; Császár, A. G.; Kállay, M.; Gauss, J.; Valeev, E. F.; Flowers, B. A.; Vázquez, J.; Stanton, J. F. J Chem Phys 2004, 121, 11599.
20. Bomble, Y. J.; Vázquez, J.; Kállay, M.; Michauk, C.; Szalay, P. G.; Császár, A. G.; Gauss, J.; Stanton, J. F. J Chem Phys 2006, 125, 064108.
21. Harding, M. E.; Vázquez, J.; Ruscic, B.; Wilson, A. K.; Gauss, J.; Stanton, J. F. J Chem Phys 2008, 128, 114111.
22. Zhao, Y.; Lynch, B. J.; Truhlar, D. G. Phys Chem Chem Phys 2005, 7,43.
23. Lynch, B. J.; Truhlar, D. G. J Phys Chem A 2003, 107, 3898.
24. Fast, P. L.; Truhlar, D. G. J Phys Chem A 2000, 104, 6111.
25. Raghavachari, K.; Turcks, G. W.; Pople, J. A.; Head-Gordon, M. Chem Phys Lett 1989, 157, 479.
26. Noga, J.; Bartlett, R. J. J Chem Phys 1987, 86, 7041.
27. Kendall, R. A.; Dunning, T. H., Jr.; Harrison, R. J. J Chem Phys 1992, 96, 6976.
28. Harding, M. E.; Metzroth, T.; Gauss, J.; Auer, A. A. J Chem Theory Comput 2008, 4, 64.
29. Pollack, L.; Windus, T. L.; de Jong, W. A.; Dixon, D. A. J Phys Chem A 2005, 109, 6934.
30. Sousa, S. F.; Fernandes, P. A.; Ramos, M. J. J Phys Chem A 2007, 111, 10439.
31. Liu, M. H.; Chen, C.; Liu, C. W.; Hong, Y. S. J Phys Chem A 2004, 108, 6784.
32. Liu, M. H.; Chen, C.; Hong, Y. S. J Chem Phys 2005, 122, 064312.
33. Liu, M. H.; Chen, C. J Comput Chem 2006, 27, 537.
34. Hu, L. H.; Wang, X. J.; Wong, L. H.; Chen, G. H. J Chem Phys 2003, 119, 11501.
35. Wu, J. M.; Xu, X. J Chem Phys 2007, 127, 214105.
36. Friesner, R. A.; Knoll, E. H.; Cao, Y. X. J Chem Phys 2006, 125, 124107.
37. Yang, C. S.; Chuang, L. Y.; Ke, C. H.; Yang, C. H. IAENG Int J Comput Sci 2008, 35, 05.

---

Journal of Computational Chemistry DOI 10.1002/jcc

38. Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Gill, P. M. W.; John- son, B. G.; Robb, M. A.; Cheeseman, J. R.; Keith, T.; Petersson, G. A.; Montgomery, J. A.; Raghavachari, K.; Al-Laham, M. A.; Zakr- zewski, V. G.; Ortiz, J. V.; Foresman, J. B.; Cioslowski, J.; Stefa- nov, B. B.; Nanayakkara, A.; Challacombe, M.; Peng, C. Y.; Ayala, P. Y.; Chen, W.; Wong, M. W.; Andres, J. L.; Replogle, E. S.; Gomperts, R.; Martin, R. L.; Fox, D. J.; Binkley, J. S.; Defrees, D. J.; Baker, J.; Stewart, J. P.; Head-Gordon, M.; Gonzalez, C.; Pople, J. A. Gaussian 03; Gaussian, Inc.: Pittsburgh, PA, 2003.

39. Stephens, P. J.; Devlin, F. J.; Chabalowski, C. F.; Frisch, M. J. J Phys Chem 1994, 98, 11623.

40. Riley, K. E.; Op't Holt, B. T.; Merz, K. M. Jr. J Chem Theory Comput 2007, 3, 407.

41. Durant, J. L. Chem Phys Lett 1996, 256, 595.

42. Bauschlicher, C. W., Jr. Chem Phys Lett 1995, 246, 40.

43. Tirado-Rives, J.; Jorgensen, W. J Chem Theory Comput 2008, 4, 297.

44. Liu, C. X.; Li, Z. R.; Zhou, C. W.; Li, X. Y. J Comput Chem 2009, 30, 1007.

45. Chase, M. W., Jr. J Phys Chem Ref Data Monograph 1998, 9, 1.

46. Pedley, J. B.; Naylor, R. D.; Kirby, S. P. In Thermochemical Data of Organic Compounds, 2nd ed.; Chapman and Hall: New York, 1986.

47. Afeefy, H. Y.; Liebman, J. F.; Stein, S. E. In NIST Chemistry WebBook, NIST Standard Reference Database Number 69; Linstrom, P. J.; Mallard, W. G., Eds.; National Institute of Standards and Technology: Gaithers- burg MD, 2005; p. 20899. Available at http://webbook.nist.gov.

48. Osmont, A.; Catoire, L.; Gökalp, I.; Yang, V. Combust Flame 2007, 15, 262.

49. Burcat, A. J Propul Power 2000, 16, 105.

50. Leal, J. P. J Phys Chem Ref Data 2006, 35, 55.

51. Allinger, N. L.; Schmitz, L. R.; Motoc, I.; Bender, C.; Labanowski, J. K. J Comput Chem 1992, 13, 838.

52. Chen, K.-H.; Allinger, N. L. J Comput Chem 1993, 14, 755.

53. Goldstein, E.; Ma, B. Y.; Lii, J. H.; Allinger, N. L. J Phys Org Chem 1996, 9, 191.

54. Voityuk, A. A. Chem Phys Lett 2006, 433, 216.

55. Liu, R. F.; Allinger, N. L. J Phys Org Chem 1993, 6, 551.

56. Blanksby, S. J.; Ramond, T. M.; Davico, G. E.; Nimlos, M. R.; Kato, S.; Bierbaum, V. M.; Lineberger, W. C.; Ellison, G. B.; Oku- mura, M. J Am Chem Soc 2001, 123, 9585.

57. Golbraikh, A.; Tropsha, A. J Mol Graphics Modell 2002, 20, 269.

58. Winget, P.; Clark, T. J Comput Chem 2004, 25, 725.

59. Wang, X. J.; Wong, L. H.; Hu, L. H.; Chan, C. Y.; Su, Z. M.; Chen, G. H. J Phys Chem A 2004, 108, 8514.

60. Duan, X. M.; Song, G. L.; Li, Z. H.; Wang, X. J.; Chen, G. H.; Fan, K. N. J Chem Phys 2004, 121, 7086.

61. Kang, J. K.; Musgrave, C. B. J Chem Phys 2001, 115, 11040.

62. Anantharaman, B.; Melius, C. F. J Phys Chem A 2005, 109, 1734.

63. Todeschini, R.; Consonni, V. Handbook of Molecular Descriptors; WILEY-VCH Verlag GmbH: Weinheim, 2000; p. 465.

64. Ohlinger, W. S.; Klunzinger, P. E.; Deppmeier, B. J.; Hehre, W. J. J Phys Chem A 2009, 113, 2165.

65. Mole, S. J.; Zhou, X. F.; Liu, R. F. J Phys Chem 1996, 100, 14665.

66. Labanowski, J.; Schmitz, L.; Chen, K. H.; Allinger, N. L. J Comput Chem 1998, 19, 1421.

67. Saeys, M.; Reyniers, M.-F.; Marin, G. B.; Speybroeck, V. V.; Waro- quier, M. J Phys Chem A 2003, 107, 9147.

68. Rice, B. M.; Pai, S. V.; Hare, J. Combust Flame 1999, 118, 445.

69. Wilcox, C. F.; Zhang, Y. X.; Bauer, S. H. J Mol Struct (THEO- CHEM) 2000, 528, 95.