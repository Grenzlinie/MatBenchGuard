# Evaluation of Thermochemical Machine Learning for Potential Energy Curves and Geometry Optimization

Dakota L. Folmsbee, David R. Koes, and Geoffrey R. Hutchison*

Cite This: J. Phys. Chem. A 2021, 125, 1987-1993

Read Online

---

ABSTRACT: While many machine learning (ML) methods, particularly deep neural networks, have been trained for density functional and quantum chemical energies and properties, the vast majority of these methods focus on single-point energies. In principle, such ML methods, once trained, offer thermochemical accuracy on par with density functional and wave function methods but at speeds comparable to traditional force fields or approximate semiempirical methods. So far, most efforts have focused on optimized equilibrium single-point energies and properties. In this work, we evaluate the accuracy of several leading ML methods across a range of bond potential energy curves and torsional potentials. The methods were trained on the existing ANI-1 training set, calculated using the $\omega$B97X/6-31G(d) single points at nonequilibrium geometries. We find that across a range of small molecules, several methods offer both qualitative accuracy (e.g., correct minima, both repulsive and attractive bond regions, anharmonic shape, and single minima) and quantitative accuracy in terms of the mean absolute percent error near the minima. At the moment, ANI-2x, FCHL, and a new libmolgrid-based convolutional neural net, the Colorful CNN, show good performance.

![](./images/812496659689766912_1.jpg)

## INTRODUCTION

Machine learning (ML) methods have been proposed as surrogates for time-consuming quantum mechanical calculations, such as density functional and first-principles methods, for their rapid prediction potential once trained. $^{1-11}$ For ML to be a successful surrogate, the methods need to be able to perform property predictions adequately for optimized geometries, capture not just the well of the potential energy curve but also the anharmonicity that force field methods fail to capture, and appropriately handle multiple conformations of the same molecule.

Numerous studies have shown the proficiency of ML methods to predict thermochemical parameters at already optimized geometries utilizing various types of representations and neural network structures. $^{2,12}$ Early representations, such as the Coulomb Matrix $^{13}$ and bag-of-features, $^{14,15}$ demonstrated success in property predictions with further iterations of representations such as FCHL $^{16,17}$ continuing to improve the property prediction at optimized geometries. These ML methods are typically trained on the QM7 $^{13,18}$ or QM9 $^{19,20}$ data sets consisting of optimized molecules with up to 7 or 9 heavy atoms, respectively, and help to demonstrate ML's potential as a surrogate.

Additional deep neural network (DNN) methods, such as ANI $^{3-5,21}$ and BAND NN, $^{22}$ used training data beyond optimized single points to better evaluate the potential surface for dynamics and geometry optimizations. These methods utilize the ANI-1 data set, $^{23}$ or the ANI-2 data set in the case of ANI-2x, for training as they contain both equilibrium and nonequilibrium structures of up to eight heavy atoms containing H, C, N, and O with the nonequilibrium structures being generated from normal-mode sampling. The training set for ANI-2x adds the additional elements of F, Cl, and S while providing additional torsion sampling data. $^{5}$ The BAND NN model uses a subset of the ANI-1 data set with only nonequilibrium geometries with energies within 30 kcal/mol of the equilibrium energy. Although these methods have been shown to perform adequately in their respective papers, the range for bond stretch applications has been limited to the harmonic portion of the potential energy curve, and the potential energy curves further from equilibrium are rarely examined.

Recent work has expanded the knowledge on ML performance for predicting and ranking thermally accessible conformations. $^{24}$ Though ML was not tasked with large bond stretches as in this work, the ability of ML methods to rank conformational energy was only comparable to that of semiempirical methods. While this is not equivalent to the accuracy of density functional (DFT) or ab initio electronic structure methods, for ML methods to be an accurate surrogate for quantum chemical methods, continued advance-

Received: November 11, 2020
Revised: February 15, 2021
Published: February 25, 2021

![](./images/812496659689766912_2.jpg)

https://dx.doi.org/10.1021/acs.jpca.0c10147
J. Phys. Chem. A 2021, 125, 1987-1993
© 2021 American Chemical Society

ments in ML models and training sets are needed to provide further performance improvements.

For ML to become a viable replacement for current methods, ML needs to achieve optimized geometries and predict properties without relying on force field (FF) methods. Most FFs have been refined for small molecules and biomolecules and can struggle with noncovalent and steric interactions for applications such as conjugated polymers. While these issues can be lessened with specific parametrization,²⁵,²⁶ geometries of FFs generally can be less than ideal.²⁷ ML trained on higher levels of theory ideally captures these noncovalent interactions and provides better initial optimized geometries.

With the rapid adoption of ML, there has been a growing desire to use ML in molecular dynamics (MD) applications to provide more accurate simulations than FFs at a much lower cost than time-consuming quantum mechanical calculations.²⁴ For ML to be reliable, it needs to properly predict geometric changes that occur in MD simulations from nonequilibrium bond stretching to torsional barriers. This work seeks to examine how well the current state of ML performs at these tasks, as well as to display the methods’ understanding of chemical physics to help decide key needs for ML to improve as a surrogate for computationally expensive quantum calculations.

## METHODS
### Molecules.
A mixture of small and large molecules was chosen to evaluate ML performance on potential energy surfaces for a total of 17 bond stretches and 5 dihedral scans. The molecules examined were benzene (C−C and C−H stretching), methanol, methane, CO, H₂, ethylene, water, acetylene, hydrogen cyanide, N₂, ammonia, biphenyl, aspar-tame, sucrose, dialanine, and diglycine. Bond stretches were evaluated every 0.1 Å while dihedrals were evaluated every 20° with the exception of biphenyl which was evaluated every 15°.

### Computational Methods.
The reference method, ωB97X,²⁸ was performed using Orca 4.0.1²⁹ while the force field calculations, MMFF94³⁰⁻³⁴ and GAFF,³⁵ were performed using Open Babel version 3.0.³⁶

Machine learning methods and representations included the pretrained models ANI-1x,³⁴ ANI-2x,⁵ BAND-NN,²² as well as FCHL,³⁷ Bag of Bonds (BOB),³⁸ and Extended Connectivity Fingerprints (ECFP).³⁹,⁴⁰ Scikit-learn⁴¹ was used for kernel ridge regression (KRR) and bayesian ridge regression (BRR) for BOB and random forest regression (RFR) with BOB and ECFP representations while FCHL used the custom KRR in QML.

We also trained a deep convolutional neural network (Colorful CNN), an approach that has been successfully used in protein−ligand binding affinity prediction.⁴²,⁴³ The input molecule is represented as a voxelized grid of atomic densities as generated by the libmolgrid library.⁴⁴ Our network has six modules separated by pooling operations each with seven convolutional layers and was trained on the ANI-1x data set.⁴⁵ The trained Colorful CNN model can be found at https://github.com/hutchisonlab/ml-benchmark.

Due to method scaling efficiency for memory usage, a subset of the ANI-1 data set was taken for training representations using BOB/KRR and BOB/BRR. For consistency, ECFP/RFR and BOB/RFR were additionally trained on this subset. The subset consists of five nonequilibrium geometries for every molecule with up to seven heavy atoms, as well as five nonequilibrium geometries for half of the molecules with eight heavy atoms, to create a training set consisting of 33,496 molecules and 167,480 nonequilibrium geometries. All molecules from the test set were removed from the training set. This training set was additionally used for BOB/RFR and ECFP/RFR. An additional subset of the first 5000 non-equilibrium geometries was used for FCHL/KRR. Increasing the training set for FCHL/KRR had a negative impact on prediction performance so our results are with the model trained on 1000 different molecules for a total of 5000 nonequilibrium geometries.

## RESULTS AND DISCUSSION
To illustrate the qualitative performance of potential energy surface predictions, we analyzed both small and larger

<table>
<caption>Table 1. Overview of Machine Learning Performance Sorted by Median Mean Absolute Percent Error (MAPE)</caption>
<thead>
<tr>
<th>Methods</th>
<th>Median MAPEᵃ</th>
<th>r₀ᵇ</th>
<th>Repulsive Wallᶜ</th>
<th>Attractive Forcesᵈ</th>
<th>Minima after 2 Åᵉ</th>
</tr>
</thead>
<tbody>
<tr>
<td>ωB97X 6-31G(d)</td>
<td>0</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>0</td>
</tr>
<tr>
<td>ANI-2x</td>
<td>0.002</td>
<td>17</td>
<td>13</td>
<td>17</td>
<td>12</td>
</tr>
<tr>
<td>BOB/BRR</td>
<td>0.227</td>
<td>0</td>
<td>5</td>
<td>5</td>
<td>9</td>
</tr>
<tr>
<td>FCHL/KRR</td>
<td>0.255</td>
<td>10</td>
<td>16</td>
<td>15</td>
<td>13</td>
</tr>
<tr>
<td>Colorful CNN</td>
<td>0.2555</td>
<td>16</td>
<td>17</td>
<td>17</td>
<td>13</td>
</tr>
<tr>
<td>ANI-1x</td>
<td>0.265</td>
<td>16</td>
<td>11</td>
<td>17</td>
<td>5</td>
</tr>
<tr>
<td>BOB/KRR</td>
<td>0.313</td>
<td>1</td>
<td>9</td>
<td>11</td>
<td>13</td>
</tr>
<tr>
<td>BOB/RFR</td>
<td>43.881</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>8</td>
</tr>
<tr>
<td>BAND-NN</td>
<td>99.310</td>
<td>11</td>
<td>9</td>
<td>5ᶠ</td>
<td>5ᶠ</td>
</tr>
<tr>
<td>MMFF94</td>
<td>100.050</td>
<td>14</td>
<td>17</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>GAFF</td>
<td>100.133</td>
<td>13</td>
<td>17</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>ECFP/RFR</td>
<td>193.370</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

ᵃMedian mean absolute percent error over all 17 molecules from $r_0 \pm$ 0.25 Å. ᵇThe number of molecules in which the lowest predicted energy point matches DFT. ᶜThe number of times the method predicted a repulsive wall as the bond was compressed. ᵈThe number of times the method predicted anharmonic attractive forces after $r_0$. ᵉThe number of molecules predicted to have a local or global minima after 2 Å. ᶠBAND-NN regularly would not predict energies for geometries with a bond stretch of 2 Å or greater.

molecules outside of the ANI-1 data set used for training for each ML method. We wish to focus on how the methods perform not only around the bond length at the energy minima, $r_0$, but also in the attractive and repulsive regimes to gain a better understanding of how ML methods would behave if given less ideal starting geometries for a task such as geometry optimization.

Each ML method was evaluated on the criteria demon-strated in Table 1 for bond stretches. The median mean absolute percent error (MAPE) was calculated from the energy values ranging from $r_0 \pm 0.25$ Å for the molecules to determine how accurate and precise the ML predicted energies are. Since the ANI-1 training set samples harmonic displacements around the $r_0$ (e.g., Figure S1), this range corresponds mostly to interpolation. Comparisons for repulsive short-range and attractive long-range interactions−extrapolations outside the training range are compiled in Table S1. The $r_0$ evaluation criteria considered whether the method correctly predicted the DFT equilibrium bond length to be the lowest energy bond length. Additional evaluation criteria included the qualitative

![](./images/812496659689766912_3.jpg)
![](./images/812496659689766912_4.jpg)

Figure 1. $N_2$ potential energy curves for ML methods utilizing random forest regression for predictions using (a) BOB and (b) ECFP for the ML descriptors.

![](./images/812496659689766912_5.jpg)
![](./images/812496659689766912_6.jpg)
![](./images/812496659689766912_7.jpg)
![](./images/812496659689766912_8.jpg)

Figure 2. Bond stretch potential energy curves for (a) $N_2$, (b) $H_2$, (c) aspartame, and (d) dialanine using total SCF energies in kcal/mol.

<table>
<caption>Table 2. ML Prediction of $\theta_0$ and the Barrier Energy between the Lowest and Highest Energy Dihedrals for Biphenyl and Sucrose Compared to the Reference $\omega$B97X 6-31G(d) Method</caption>
<tbody>
<tr>
<td rowspan="2">Methods</td>
<td colspan="2">Biphenyl</td>
<td colspan="2">Sucrose</td>
</tr>
<tr>
<td>$\theta_0$ (deg)</td>
<td>Barrier Energy (kcal/mol)</td>
<td>$\theta_0$ (deg)</td>
<td>Barrier Energy (kcal/mol)</td>
</tr>
<tr>
<td>$\omega$B97X 6-31G(d)</td>
<td>−45</td>
<td>3.54</td>
<td>0</td>
<td>$2.45 \times 10^3$</td>
</tr>
<tr>
<td>ANI-1x</td>
<td>−45</td>
<td>3.95</td>
<td>0</td>
<td>$2.50 \times 10^3$</td>
</tr>
<tr>
<td>ANI-2x</td>
<td>−45</td>
<td>4.16</td>
<td>0</td>
<td>$1.93 \times 10^3$</td>
</tr>
<tr>
<td>Colorful CNN</td>
<td>−135</td>
<td>5.49</td>
<td>0</td>
<td>$9.46 \times 10^2$</td>
</tr>
<tr>
<td>FCHL/KRR</td>
<td>180</td>
<td>5.52</td>
<td>0</td>
<td>$9.73 \times 10^4$</td>
</tr>
</tbody>
</table>

prediction of a repulsive wall, anharmonic long-range interactions, and if there were incidences of additional minima past 2 Å.

While methods such as BOB/BRR and BOB/KRR had the second- and fifth-lowest median MAPE, their ability to predict the geometry with the lowest energy, a repulsive wall, and attractive forces was quite poor compared to the other top methods based on MAPE. Other methods utilizing RFR also performed poorly, often predicting the stepwise energy surfaces seen in Figure 1 and thus being incapable of consistently predicting $r_0$ or attractive or repulsive forces. This is seen in Figure 1b when the bond breaking causes the only change in the ECFP representation and leads to the higher energy. Other ML methods such as ANI-1x, ANI-2x, FCHL, and Colorful CNN were able to accurately predict energies while also predicting the repulsive and attractive forces of the molecule. In short, while random forest methods may have accuracy at single-point properties, they prove inherently inaccurate for potential energy and should be avoided.

A possible advantage for the ANI-1x and ANI-2x models is that some molecules in our test evaluation are found in the ANI-1x training set. In the training of the other methods, molecules in our test set were purposefully left out of the training set but may be present in the ANI-1x and ANI-2x model. For that reason, we will focus the remainder of our discussion on molecules outside of the ANI-1 training set, examining the best overall performers, ANI-1x, ANI-2x, FCHL, and Colorful CNN from Table 1. The performance of all methods is included in the Supporting Information.

![](./images/812496659689766912_9.jpg)

Figure 3. Dihedral energy predictions for (a) biphenyl and (b) sucrose in kcal/mol.

### Dialanine

![](./images/812496659689766912_10.jpg)

Figure 4. 2D torsion scans of dialanine in kcal/mol unless otherwise stated. Methods were tested at the geometries obtained with $\omega$B97X 6-31G(d) from the torsion scan. Note that the color schemes differ, due to large differences in energy scales.

Figure 2a displays the performance of ANI-1x, ANI-2x, Colorful CNN, and FCHL on the N−N bond stretch of $N_2$. While each of these ML methods predicts the correct $r_0$, there are issues in the prediction of the potential energy curve. ANI-1x, ANI-2x, and Colorful CNN fail to accurately depict the repulsive region with ANI-2x lowering in energy as the bond was compressed to 0.6 Å. FCHL depicts the repulsive wall but inaccurately predicts the energy as the bond is compressed. All four methods accurately determined the attractive forces to be about 2 Å with ANI-2x matching $\omega$B97X to 2.25 Å.

The H−H stretch of $H_2$ in Figure 2b indicates one possible issue for ML. All four methods performed poorly with ANI-2x being the only method to obtain the correct $r_0$. This performance is likely due to the absence of H−H bonding data within the training set. $H_2$, while a unique bond,

Diglycine

![](./images/812496659689766912_11.jpg)

Figure 5. 2D torsion scans of diglycine in kcal/mol unless otherwise stated. Methods were tested at the geometries obtained with ωB97X 6-31G(d) from the torsion scan. Note that the color schemes differ, due to large differences in energy scales.

<table>
 <thead>
  <tr>
   <th colspan="3">Table 3. Mean Absolute Error (MAE) in kcal/mol of 2D Torsion Scans for the Top Performing Methods</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>Methods</th>
   <td>Dialanine MAE ΔEnergy (kcal/mol)</td>
   <td>Diglycine MAE ΔEnergy (kcal/mol)</td>
  </tr>
  <tr>
   <th>ANI-2x</th>
   <td>1.89</td>
   <td>1.71</td>
  </tr>
  <tr>
   <th>ANI-1x</th>
   <td>3.01</td>
   <td>2.52</td>
  </tr>
  <tr>
   <th>Colorful CNN</th>
   <td>7.10</td>
   <td>6.07</td>
  </tr>
  <tr>
   <th>FCHL/KRR</th>
   <td>252.17</td>
   <td>200.86</td>
  </tr>
 </tbody>
</table>

demonstrates the need to be careful when applying ML to molecules or chemistry completely outside the scope of the training set.

Figure 2c and 2d demonstrate the prediction capability of these ML methods on bond stretches for molecules larger than the training set. FCHL was only able to accurately capture the shape of the potential energy curve for dialanine, failing to capture the well of the potential energy curve for aspartame, perhaps from the difficulties training the entire ANI-1 set. ANI-1x, ANI-2x, and Colorful CNN retain both repulsive and attractive information while having accurate energies to that of ωB97X for both aspartame and dialanine. These methods do continue to exhibit difficulty in accurately predicting bond compression under $1\ \mathring{A}$ as well as bond stretching after $2\ \mathring{A}$.

For bond stretches, ANI-1x, ANI-2x, Colorful CNN, and FCHL models show promise with initial training indicating these methods can accurately predict the bottom of the potential energy well. While force fields such as MMFF94 or GAFF can be used to obtain optimized geometries near this regime, ultimately ML methods should exhibit accuracy not only at single-point energy evaluation tasks but also at qualitatively and quantitatively accurate potential energy curves. Further training on long-range attractive forces might enable ML models to evaluate noncovalent interactions.

As an example, further evaluations were carried out on energy predictions from frozen-rotor dihedral angle scans performed with ωB97X 6-31G(d) for biphenyl and sucrose. Table 2 compiles the predicted lowest energy angle for these molecules as well as the barrier energies from $-45^\circ$ to $0^\circ$ for biphenyl and $0^\circ$ to $-60^\circ$ for sucrose.

ANI-1x and ANI-2x properly predict the lowest energy angle for biphenyl while Colorful CNN predicts $-45^\circ$ to be a local, but not global, minimum. FCHL improperly predicts rotation energies as seen in Figure 3a, predicting $0^\circ$, $180^\circ$, and $-180^\circ$

to be the lowest energy dihedrals. All of the methods overpredicted the height of the energy barrier for biphenyl.

For sucrose, all four methods correctly predicted the lowest energy angle. ANI-1x best captures the energy of the dihedral angles, seen in Figure 3b, with ANI-2x and Colorful CNN underpredicting the energy for most angles. Unlike with biphenyl, FCHL captures the shape of the torsion scan for sucrose but vastly overpredicts the energies at each angle.

Dihedral scans demonstrate how small conformational changes in the molecule can affect the potential energy surface. The 2D torsion scans in Figures 4 and 5 compare ML performance to that of $\omega$B97X and the FFs MMFF94 and GAFF. ANI-1x, ANI-2x, and Colorful CNN retain the resolution of some of the higher energy $\phi$ and $\psi$ between $-100^\circ$ to $100^\circ$ while FCHL predicts these to be lower energy conformations similar to both FF methods. In lower energy conformations both BAND and BOB/KRR methods overestimate these energy differences.

The additional torsion training in ANI-2x provided a beneficial reduction in the MAE for both dialanine and diglycine, seen in Table 3, by roughly 35% from ANI-1x. Additional torsion sampling for the methods Colorful CNN and FCHL should also provide a decrease in MAE for predicting dihedral angle energies. This could improve accuracy for the Colorful CNN method that is already qualitatively adequate.

As an example, the ANI-2x training includes additional torsion sampling, and the method shows improved accuracy over ANI-1x. Providing additional torsion sampling training sets should improve the ML method accuracy across multiple methods.

A prevailing pitfall of ML methods stems from the training set. At the end of the day, the machine learning method is only as good as the training set. As seen with H₂, models struggle with chemical motifs outside of the training set. Current ML training sets largely consist of a subset of the molecules generated in the GDB-17²⁰ set, typically containing at least H, C, O, and N. While these training sets are a noble starting point for covering small organic molecules, they lack a diversity of atom species needed for applications such as protein binding and DNA sequencing. Additional data sets such as PubChemQC⁴⁶ could help to further expand the snapshot of chemical space that ML methods are trained on.

## CONCLUSIONS

Much work has focused on the use of machine learning methods as surrogates for computationally intensive density functional and quantum chemical methods. Often such efforts train and test on single-point energies of optimized structures. An important step is to evaluate ML methods across potential energy curves and surfaces for tasks such as geometry optimization.

ML methods such as ANI-2x, Colorful CNN, and FCHL perform decently near the well of the potential energy curve while struggling to properly predict repulsive regions and particularly long-range attractive forces. While this poor performance outside the domain of the training set is expected, these methods show promise with further improvements through the addition of stretched bonds in training data helping to improve model performance in this area. Increased torsion sampling for training ANI-2x improved the model's performance over ANI-1x and should provide improvements for models such as Colorful CNN and FCHL.

In general, there is still the issue of applying ML to the prediction of molecules too far outside the scope of the training set. The inclusion of additional elements and an increase in diversity of molecules in the training set from diverse data sets such as PubchemQC should alleviate some of these challenges.

## ASSOCIATED CONTENT

### Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpca.0c10147.

Figures of all bond stretch potential energy curves and dihedral potential energy scans for all molecules and methods considered (PDF)

## AUTHOR INFORMATION

### Corresponding Author

Geoffrey R. Hutchison − Department of Chemistry, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, United States; Department of Chemical and Petroleum Engineering, University of Pittsburgh, Pittsburgh, Pennsylvania 15261, United States; <https://orcid.org/0000-0002-1757-1980>; Email: geoffh@pitt.edu

### Authors

Dakota L. Folmsbee − Department of Chemistry, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, United States

David R. Koes − Department of Computational & Systems Biology, School of Medicine, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, United States; <https://orcid.org/0000-0002-6892-6614>

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpca.0c10147

### Notes

The authors declare no competing financial interest.
All raw data, Python notebooks, and the trained Colorful CNN model can be found at https://github.com/hutchisonlab/ml-benchmark.

## ACKNOWLEDGMENTS

We acknowledge the National Science Foundation (CHE-1800435) for support and the University of Pittsburgh Center for Research Computing for the computational resources provided.

## REFERENCES

(1) Behler, J.; Parrinello, M. Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces. Phys. Rev. Lett. 2007, 98, DOI: 10.1103/PhysRevLett.98.146401

(2) Faber, F. A.; Hutchison, L.; Huang, B.; Gilmer, J.; Schoenholz, S. S.; Dahl, G. E.; Vinyals, O.; Kearnes, S.; Riley, P. F.; von Lilienfeld, O. A. Prediction Errors of Molecular Machine Learning Models Lower than Hybrid DFT Error. J. Chem. Theory Comput. 2017, 13, 5255−5264.

(3) Smith, J. S.; Isayev, O.; Roitberg, A. E. ANI-1: an extensible neural network potential with DFT accuracy at force field computational cost. Chemical Science 2017, 8, 3192−3203.

(4) Smith, J. S.; Nebgen, B.; Lubbers, N.; Isayev, O.; Roitberg, A. E. Less is more: Sampling chemical space with active learning. J. Chem. Phys. 2018, 148, 241733.

(5) Devereux, C.; Smith, J. S.; Davis, K. K.; Barros, K.; Zubatyuk, R.; Isayev, O.; Roitberg, A. E. Extending the Applicability of the ANI

Deep Learning Molecular Potential to Sulfur and Halogens. *J. Chem. Theory Comput.* **2020**, *16*, 4192–4202.

(6) von Lilienfeld, O. A.; Burke, K. Retrospective on a decade of machine learning for chemical discovery. *Nat. Commun.* **2020**, *11*, DOI: 10.1038/s41467-020-18556-9

(7) Dral, P. O. Quantum Chemistry in the Age of Machine Learning. *J. Phys. Chem. Lett.* **2020**, *11*, 2336–2347.

(8) Qiao, Z.; Welborn, M.; Anandkumar, A.; Manby, F. R.; Miller, T. F. OrbNet: Deep learning for quantum chemistry using symmetry-adapted atomic-orbital features. *J. Chem. Phys.* **2020**, *153*, 124111.

(9) Sinitskiy, A. V.; Pande, V. S. Deep Neural Network Computes Electron Densities and Energies of a Large Set of Organic Molecules Faster than Density Functional Theory (DFT); 2018.

(10) Sinitskiy, A. V.; Pande, V. S. *Physical machine learning outperforms "human learning" in Quantum Chemistry*; 2020.

(11) Schütt, K. T.; Sauceda, H. E.; Kindermans, P.-J.; Tkatchenko, A.; Müller, K.-R. SchNet − A deep learning architecture for molecules and materials. *J. Chem. Phys.* **2018**, *148*, 241722.

(12) Wu, Z.; Ramsundar, B.; Feinberg, E.; Gomes, J.; Geniesse, C.; Pappu, A. S.; Leswing, K.; Pande, V. MoleculeNet: a benchmark for molecular machine learning. *Chem. Sci.* **2018**, *9*, 513–530.

(13) Rupp, M.; Tkatchenko, A.; Müller, K.-R.; von Lilienfeld, O. A. Fast and Accurate Modeling of Molecular Atomization Energies with Machine Learning. *Phys. Rev. Lett.* **2012**, *108*, 058301.

(14) Hansen, K.; Biegler, F.; Ramakrishnan, R.; Pronobis, W.; von Lilienfeld, O. A.; Müller, K.-R.; Tkatchenko, A. Machine Learning Predictions of Molecular Properties: Accurate Many-Body Potentials and Nonlocality in Chemical Space. *J. Phys. Chem. Lett.* **2015**, *6*, 2326–2331.

(15) Huang, B.; von Lilienfeld, O. A. Communication: Understanding molecular representations in machine learning: The role of uniqueness and target similarity. *J. Chem. Phys.* **2016**, *145*, 161102.

(16) Faber, F. A.; Christensen, A. S.; Huang, B.; von Lilienfeld, O. A. Alchemical and structural distribution based representation for universal quantum machine learning. *J. Chem. Phys.* **2018**, *148*, 241717.

(17) Christensen, A. S.; Bratholm, L. A.; Faber, F. A.; von Lilienfeld, O. A. FCHL revisited: Faster and more accurate quantum machine learning. *J. Chem. Phys.* **2020**, *152*, 044107.

(18) Blum, L. C.; Reymond, J.-L. 970 Million Druglike Small Molecules for Virtual Screening in the Chemical Universe Database GDB-13. *J. Am. Chem. Soc.* **2009**, *131*, 8732.

(19) Ramakrishnan, R.; Dral, P. O.; Rupp, M.; von Lilienfeld, O. A. Quantum chemistry structures and properties of 134 kilo molecules. *Sci. Data* **2014**, *1*, DOI: 10.1038/sdata.2014.22

(20) Ruddigkeit, L.; van Deursen, R.; Blum, L. C.; Reymond, J.-L. Enumeration of 166 Billion Organic Small Molecules in the Chemical Universe Database GDB-17. *J. Chem. Inf. Model.* **2012**, *52*, 2864–2875.

(21) Smith, J. S.; Nebgen, B. T.; Zubatyuk, R.; Lubbers, N.; Devereux, C.; Barros, K.; Tretiak, S.; Isayev, O.; Roitberg, A. Approaching coupled cluster accuracy with a general-purpose neural network potential through transfer learning; 2019.

(22) Laghuvarapu, S.; Pathak, Y.; Priyakumar, U. D. BAND NN: A Deep Learning Framework for Energy Prediction and Geometry Optimization of Organic Small Molecules. *J. Comput. Chem.* **2020**, *41*, 790–799.

(23) Smith, J. S.; Isayev, O.; Roitberg, A. E. ANI-1, A data set of 20 million calculated off-equilibrium conformations for organic molecules. *Sci. Data* **2017**, *4*, 170193.

(24) Folmsbee, D.; Hutchison, G. Assessing conformer energies using electronic structure and machine learning methods. *Int. J. Quantum Chem.* **2021**, *121*, e26381.

(25) DuBay, K. H.; Hall, M. L.; Hughes, T. F.; Wu, C.; Reichman, D. R.; Friesner, R. A. Accurate Force Field Development for Modeling Conjugated Polymers. *J. Chem. Theory Comput.* **2012**, *8*, 4556–4569.

(26) Wildman, J.; Repišćák, P.; Paterson, M. J.; Galbraith, I. General Force-Field Parametrization Scheme for Molecular Dynamics Simulations of Conjugated Materials in Solution. *J. Chem. Theory Comput.* **2016**, *12*, 3813–3824.

(27) Kanal, I. Y.; Keith, J. A.; Hutchison, G. R. A sobering assessment of small-molecule force field methods for low energy conformer predictions. *Int. J. Quantum Chem.* **2018**, *118*, No. e25512.

(28) Chai, J.-D.; Head-Gordon, M. Systematic optimization of long-range corrected hybrid density functionals. *J. Chem. Phys.* **2008**, *128*, 084106.

(29) Neese, F. The ORCA program system. *Wiley Interdiscip. Rev.: Comput. Mol. Sci.* **2012**, *2*, 73–78.

(30) Halgren, T. A. Merck molecular force field. I. Basis, form, scope, parameterization, and performance of MMFF94. *J. Comput. Chem.* **1996**, *17*, 490–519.

(31) Halgren, T. A. Merck molecular force field. II. MMFF94 van der Waals and electrostatic parameters for intermolecular interactions. *J. Comput. Chem.* **1996**, *17*, 520–552.

(32) Halgren, T. A. Merck molecular force field. III. Molecular geometries and vibrational frequencies for MMFF94. *J. Comput. Chem.* **1996**, *17*, 553–586.

(33) Halgren, T. A.; Nachbar, R. B. Merck molecular force field. IV. conformational energies and geometries for MMFF94. *J. Comput. Chem.* **1996**, *17*, 587–615.

(34) Halgren, T. A. Merck molecular force field. V. Extension of MMFF94 using experimental data, additional computational data, and empirical rules. *J. Comput. Chem.* **1996**, *17*, 616–641.

(35) Wang, J.; Wolf, R. M.; Caldwell, J. W.; Kollman, P. A.; Case, D. A. Development and testing of a general amber force field. *J. Comput. Chem.* **2004**, *25*, 1157–1174.

(36) O'Boyle, N. M.; Banck, M.; James, C. A.; Morley, C.; Vandermeersch, T.; Hutchison, G. R. Open Babel: An open chemical toolbox. *J. Cheminf.* **2011**, *3*, 33.

(37) Christensen, A.; Faber, F.; Huang, B.; Bratholm, L.; Tkatchenko, A.; Müller, K.; von Lilienfeld, QML, O. *A Python Toolkit for Quantum Machine Learning*; 2017; https://github.com/qmlcode/qml.

(38) Folmsbee, D.; Upadhyay, S.; Dumi, A.; Hiener, D.; Mulvey, D. chemreps/chemreps: Molecular Machine Learning Representations; 2019; DOI: 10.5281/zenodo.3333856.

(39) Rogers, D.; Hahn, M. Extended-Connectivity Fingerprints. *J. Chem. Inf. Model.* **2010**, *50*, 742–754.

(40) Wójcikowski, M.; Zielenkiewicz, P.; Siedlecki, P. Open Drug Discovery Toolkit (ODDT): a new open-source player in the drug discovery field. *J. Cheminf.* **2015**, *7*, 26.

(41) Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; et al. Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research* **2011**, *12*, 2825–2830.

(42) Ragoza, M.; Hochuli, J.; Idrobo, E.; Sunseri, J.; Koes, D. R. Protein–ligand scoring with convolutional neural networks. *J. Chem. Inf. Model.* **2017**, *57*, 942–957.

(43) Jiménez, J.; Skalic, M.; Martinez-Rosell, G.; De Fabritiis, G. K. deep: Protein–ligand absolute binding affinity prediction via 3d-convolutional neural networks. *J. Chem. Inf. Model.* **2018**, *58*, 287–296.

(44) Sunseri, J.; Koes, D. R. libmolgrid: Graphics Processing Unit Accelerated Molecular Gridding for Deep Learning Applications. *J. Chem. Inf. Model.* **2020**, *60*, 1079–1084.

(45) Smith, J. S.; Zubatyuk, R.; Nebgen, B.; Lubbers, N.; Barros, K.; Roitberg, A. E.; Isayev, O.; Tretiak, S. The ANI-1ccx and ANI-1x data sets, coupled-cluster and density functional theory properties for molecules. *Sci. Data* **2020**, *7*, 1–10.

(46) Nakata, M.; Shimazaki, T. PubChemQC Project: A Large-Scale First-Principles Electronic Structure Database for Data-Driven Chemistry. *J. Chem. Inf. Model.* **2017**, *57*, 1300–1308.