### Assessing conformer energies using electronic structure and machine learning methods

Dakota Folmsbee | Geoffrey Hutchison

Department of Chemistry, University of
Pittsburgh, Pittsburgh, Pennsylvania

Correspondence
Geoffrey Hutchison, Department of
Chemistry, University of Pittsburgh, PA 15260.
Email: geoffh@pitt.edu

Funding information
National Science Foundation, Grant/Award
Number: CHE-1800435

#### Abstract
We have performed a large-scale evaluation of current computational methods, including conventional small-molecule force fields; semiempirical, density functional, ab initio electronic structure methods; and current machine learning (ML) techniques to evaluate relative single-point energies. Using up to 10 local minima geometries across $\sim$700 molecules, each optimized by B3LYP-D3BJ with single-point DLPNO-CCSD(T) triple-zeta energies, we consider over 6500 single points to compare the correlation between different methods for both relative energies and ordered rankings of minima. We find that the current ML methods have potential and recommend methods at each tier of the accuracy-time tradeoff, particularly the recent GFN2 semiempirical method, the B97-3c density functional approximation, and RI-MP2 for accurate conformer energies. The ANI family of ML methods shows promise, particularly the ANI-1ccx variant trained in part on coupled-cluster energies. Multiple methods suggest continued improvements should be expected in both performance and accuracy.

#### KEYWORDS
conformers, coupled-cluster, density functional, DFTB, machine learning, semiempirical, thermochemistry

---

## 1 | INTRODUCTION

For almost all molecules, multiple geometrically distinct conformers exist. Understanding and predicting thermodynamically accessible ensembles of molecular conformers is a key task underlying much of computational chemistry.$^{[1-3]}$ In principle, for each rotatable bond, the number of possible minima increases exponentially. Consequently, most conformer sampling methods$^{[4]}$ use classical small-molecule force fields to evaluate energies because of their fast performance, despite potentially poor correlation with quantum mechanical methods.$^{[5]}$

Multiple efforts have evaluated the success of wavefunction and density functional first-principles methods to compare the energetics of different conformers.$^{[6-12]}$ While experimental crystal structures and bioactive docked conformers are not always the lowest energy conformer, recent efforts have demonstrated only small energy differences when using quantum chemical methods instead of force fields.$^{[13,14]}$

Even for simple molecules such as 1,1'-biphenyl, use of large basis set coupled-cluster methods are needed to accurately place the dihedral angle and barrier.$^{[15]}$ Other works have documented the need for accurate treatment of noncovalent interactions to model conformers in $\pi$-conjugated oligomers.$^{[16]}$

---

Referee reports and author responses are made public under through the "Open Peer-Review Details" section.

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.
© 2020 The Authors. *International Journal of Quantum Chemistry* published by Wiley Periodicals LLC.

Int J Quantum Chem. 2020;e26381.
https://doi.org/10.1002/qua.26381
http://q-chem.org | 1 of 15

One common assumption is the presumed balance between increasing desired thermochemical accuracy and increased computational time. That is, more computationally intensive methods produce more accurate geometries and thermochemical properties. For example, the rise of composite ab initio thermochemical recipes such as G3, $^{[17]}$ G4, $^{[18]}$ and W1 $^{[19,20]}$ to W4 $^{[21]}$ seeks to provide highly accurate thermochemical predictions by separate estimates of basis set extrapolation and electron correlation. Still, such methods are largely limited to small molecules due to the high computational cost. $^{[22]}$ As mentioned above, efforts for conformer sampling have often focused on classical force fields or multilevel approaches using semiempirical methods. $^{[4,23,24]}$

In our previous paper, $^{[5]}$ we considered both the single-point energies and geometry optimizations of a range of common computational chemistry methods, including classical force fields, semiempirical quantum chemistry, and dispersion-corrected density functional methods. In general, due to the large differences in the potential energy surfaces predicted by force fields and quantum methods, we found poor correlation between both single-point energies at the same geometry and optimized geometries using different methods.

In this work, in order to expand our range of computational methods, we only consider the relative single-point energies from the same set of density functional-optimized geometries, comparing multiple current methods to a high-quality coupled-cluster baseline. We consider the mean absolute relative errors (MARE) in energies, as well as the correlation of relative energies, reflected in the $R^2$ coefficient of determination, and the ranking of single-point energies reflected in the Spearman $\rho$ correlation. The use of correlation coefficients and the Spearman correlation is intended to consider whether methods exhibit systematic errors that may not affect linear correlation or ranking of energetic stabilities.

While we find that increased accuracy typically still requires exponential increases in computational time, several methods stand out as widely useful methods for ranking conformer energies. Future improvements in standard computational methods and machine learning surrogates suggest that both increased accuracy and efficiency are expected from further method development.

## 2 | COMPUTATIONAL METHODS

Calculations were performed using Open Babel version 3.0 $^{[25]}$ for all force field calculations (MMFF94 $^{[26-30]}$ and UFF $^{[31,32]}$ ); OpenMOPAC for PM7 $^{[33]}$; xtb version 6.2 $^{[34]}$ for GFN0, $^{[35]}$ GFN1, $^{[36]}$ and GFN2 calculations $^{[37]}$; and Orca 4.0.1 $^{[38]}$ for all density functional and ab initio calculations, unless otherwise indicated. For density functional methods, the D3(BJ) $^{[39-42]}$ dispersion correction scheme was used as indicated, except for $\omega$B97X-D3, $^{[43]}$ which uses a similar approach. For ab initio methods, Orca 4.0.1 was used for MP2 $^{[44]}$ and DLPNO-CCSD(T), $^{[45,46]}$ with "TightPNO" using the cc-pVTZ basis set. $^{[47,48]}$ Energies are read from all output files using the cclib $^{[49]}$ version 1.6.2 and pybel version 3.0. $^{[50]}$

Machine learning methods included "bag-of-features" representations and ANI-1x $^{[51]}$, ANI-1ccx $^{[52]}$, and ANI-2x $^{[53]}$ models. The Bag-of-Features representations chosen were Bag of Bonds $^{[54]}$(BOB), Bond Angle Torsion $^{[55]}$(BAT), and Bond Angle Torsion Typed (BATTY). BOB represents atoms and pairwise interactions into sorted bags, with BAT being a many-body expansion to include angles and torsions. Both of these representations were implemented using chemreps. $^{[56]}$ The BATTY representation takes inspiration from BAT in order to include minimal atom typing in all bond, angle, and torsion bags while excluding nonbonding interaction and nuclear charge bags in the final representation, as discussed below. Scikit-learn $^{[57]}$ was used for kernel ridge regression of Bag-of-Features representations.

For this work, all timings are single-core CPU times using a 2.60 GHz Intel Skylake CPU (Intel Xeon Gold 6126) with 192GB RAM per node, through the University Pittsburgh Center for Research Computing.

Python scripts and Jupyter notebooks were used to compile all data into pandas $^{[58]}$ data frames, using numpy $^{[59]}$ and scipy $^{[60]}$ functions for analysis. 3DMol.js was used for interactive molecular visualization of conformers. $^{[61]}$ Plotly was used for interactive plots. $^{[62]}$

All scripts and data, including molecular geometries, are provided through GitHub (https://github.com/ghutchis/conformer-benchmark) with the intent that additional computational methods can be added to these benchmark comparisons.

## 3 | TEST SET SELECTION

As in our previous work, $^{[5]}$ a dataset consisting of experimental crystal structures of 700 small molecules capable of multiple conformer geometries was provided to us by Ebejer $^{[63]}$ and were derived from the work of Hawkins et al $^{[23]}$ along with ligands from the Astex Diverse Set. $^{[64]}$ These compounds have been repeatedly used to evaluate the quality of conformer generation. $^{[23,63]}$ Approximately half (320 molecules) consist solely of carbon, hydrogen, nitrogen, and oxygen (CHON) atoms, while the remainder are more complex drug-like compounds and ligands from the Protein Data Bank (PDB). $^{[23]}$ A list of Simplified Molecular Input Line Entry Specification (SMILES) $^{[65]}$ for all 700 molecules can be found in the Supporting Information.

For ab initio calculations using the cc-pVTZ basis sets, relativistic effective core potentials were not available for molecules containing iodine. Thus, for comparisons with DLPNO-CCSD(T) and RI-MP2 methods, such species were omitted. Similarly, the ANI-1x and ANI-1cxx methods only support molecules containing CHON atoms, and evaluations were only performed on the subset of molecules supported. The ANI-2x method supports additional elements, but not bromine or iodine, and thus, evaluations were similarly only performed on the supported subset for that method.

For bag-of-feature ML testing, the training set was five conformers of each molecule, with the remaining conformers as a test/validation. Any molecule with fewer than five conformers had the conformers added to the training set and was omitted from the test set.

## 4 | RESULTS

In this work, we focus on the evaluation of single-point atomization energy calculations on a subset of ~700 organic molecules. Conformers were initially created from a set of 250 diverse poses with maximal heavy-atom root mean squared deviation (RMSD) using Open Babel, and at most, 10 poses were selected based on the lowest heat of formation calculated by PM7, followed by full geometry optimization using B3LYP-D3BJ with the def2-SVP basis set. $^{[5]}$

Using this set of DFT-optimized minima, in this work, single-point atomization energies were computed using the DLPNO-CCSD(T)$^{[45,46]}$ method using the cc-pVTZ basis set. This approach has been found to be a highly accurate method for calculating thermochemical properties and with a significantly lower computational cost for medium-to-large organic molecules, compared to canonical CCSD(T) methods.$^{[45,66,67]}$ Using only the set of molecules for which all standard (ie, not machine-learning based) methods were used leaves 6511 entries. Of those, 9 molecules (out of 690) had two or fewer poses and were also removed, leaving 681 unique molecules and ~ 6500 entries for comparison.

To our knowledge, this is the most extensive computational validation set in terms of the number of compounds, geometries, and computational methods for studying low-energy molecular conformers. We provide all data and analysis scripts as open data and open source to allow future reuse via a GitHub repository.

As illustrated in Figure 1, each method is correlated with DLPNO-CCSD(T)/cc-pVTZ energies for each molecule (eg, astex_1hwi in Figure 1). As each molecule has several conformers, three metrics are compiled: the mean absolute relative energy (MARE) compared to the DLPNO-CCSD (T) atomization energies, the Pearson $R^2$ correlation, and the Spearman correlation $\rho$. The MARE metric gives an absolute measure of the energetic errors, but as different methods use different energy scales (eg, heats of formation for PM7 and force fields), the statistical correlations use linear regression ($R^2$) and relative ordering (Spearman $\rho$) to remove sources of systematic energy differences. For each metric across each method, the median value was compiled as illustrated in Figure 1 to represent the overall quality of a given method.

As the metrics are unlikely to reflect normal distributions (eg, Figure 1 shows highly non-Gaussian distributions), determining confidence intervals cannot be established from analytical formulas. Consequently, we used bootstrap sampling to establish 95% confidence values for the medians, as reported below. For ease of discussion, we have given the confidence ranges in all tables and figures but indicate ± errors using the average of the upper and lower bounds. In general, the asymmetry between upper and lower bounds are small.

By considering a large number of diverse organic molecules with many poses per molecule, we seek to sample a wide variety of conformer energy preferences (eg, intramolecular hydrogen and halogen bonding, $\pi$ - $\pi$ stacking, electrostatic interactions, etc.). While using optimized low-energy conformers may underestimate the accuracy of methods for high-energy structures, $^{[7]}$ we believe the current work is a challenging but useful comparison. In general, such high-energy geometries reflect steric repulsion more than the diverse types of interactions driving low-energy geometries.

Moreover, many computational predictions rely on Boltzmann-weighted averages of multiple thermally accessible conformers, including NMR prediction, $^{[1,2]}$ reactions, and even understanding the effects of dipole moments on solvent viscosity. $^{[68]}$ Consequently, deriving accurate relative energies of molecular conformers is a crucial task, as discussed below.

### 4.1 | Comparison of single points vs DLPNO-CCSD(T)

For comparison, we considered a wide variety of currently available computational methods:

- Common classical organic force fields: MMFF94, $^{[26-30]}$ UFF, $^{[31]}$ GAFF$^{[69]}$
- Semiempirical wavefunction: PM7$^{[33]}$
- Density functional tight binding: GFN0, $^{[35]}$ GFN1, $^{[36]}$ GFN2$^{[37]}$
- Low-cost density functional approximations: PBEh-3c, $^{[70]}$ B97-3c$^{[71]}$
- Dispersion-corrected density functionals: B3LYP, $^{[72-75]}$ PBE$^{[76,77]}$, ωB97X-D$^{[43]}$ with dispersion correction (using def2-TZVP basis set$^{[78,79]}$)
- Møller-Plesset RI-MP2$^{[44]}$ with the cc-pVTZ basis set$^{[47,48]}$

In the case of B3LYP and PBE dispersion-corrected functionals, we also considered both the commonly used double-zeta def2-SVP and triple-zeta def2-TZVP basis sets to understand the effects of basis set size. For B3LYP, PBE, and ωB97X, we also considered the accuracy with and without dispersion correction.

![](./images/812592469769191426_1.jpg)

![](./images/812592469769191426_2.jpg)

**FIGURE 1** Example analysis of ωB97X-D3 and GFN2 methods, starting with (A) correlation between ωB97X-D3 and DLPNO-CCSD (T) energies for a single molecule, (B) histogram of $R^2$ correlations across all molecules, (C) correlation between GFN2 and DLPNO-CCSD (T) energies, and (D) corresponding histogram of $R^2$ correlations across all molecules

## 4.2 | Basis set effects

For the frequently used B3LYP-D3BJ and PBE-D3BJ density functional methods, we considered both the def2-SVP and def2-TZVP basis sets. In both cases, the triple-zeta basis set significantly improved correlation with the DLPNO-CCSD(T)/cc-pVTZ baseline, for example, the median $R^2$ scores improved from $0.868 \pm 0.064$ to $0.920 \pm 0.025$ for B3LYP-D3BJ and from $0.835 \pm 0.025$ to $0.885 \pm 0.018$ for PBE-D3BJ. There were comparable improvements in median Spearman rank correlation and reduced mean absolute relative errors, all statistically significant (ie, P-values far below 0.001). The increased basis sets also roughly doubled the CPU time required.

While the PBE method is still significantly faster than B3LYP, the newer B97-3c proves to be faster than either, with comparable accuracy (ie, roughly intermediate to the TZ results for B3LYP-D3BJ and PBE-D3BJ). In addition, the time required for B3LYP-D3BJ/def2-TZVP calculations is only slightly less than RI-MP2/cc-pVTZ results, which exhibit significantly improved accuracy relative to DLPNO-CCSD(T)/cc-pVTZ (ie, median $R^2 = 0.964 \pm 0.006$ and median MARE of $0.115 \pm 0.011$ kcal/mol for RI-MP2).

Thus, increasing the basis set size for these density functional methods, at least from double zeta to triple zeta, does improve accuracy, albeit at a significant computational cost. In general, the B97-3c method provides accuracy comparable to popular dispersion-corrected density functional theory (DFT) methods such as B3LYP-D3BJ with faster performance, and RI-MP2 provides greater accuracy at a very similar speed.

## 4.3 | Dispersion corrections

As the bonding is consistent across multiple conformers, the ranking of small energy differences is known to be dominated by nonbonding interactions. $^{[80,81]}$ Density functional methods are known to incorrectly account for dispersion interactions, which has led to a variety of empirical

corrections. $^{[39-42,82-85]}$ Comparing uncorrected PBE, B3LYP, and ωB97X single-point energies to DLPNO-CCSD(T) illustrates a significant effect. The uncorrected median $R^2$ values drop by ~0.12, and the median Spearman correlations drop by ~0.08. For example, the median $R^2$ of B3LYP/TZ drops from $0.920 \pm 0.012$ to $0.706 \pm 0.050$ without the D3BJ dispersion correction.

On the time scale of a density functional calculation, these empirical dispersion corrections require only a minuscule time yet significantly improve the accuracy of the relative energies. Thus, even though this work is concerned with intramolecular interactions in conformers, dispersion-corrected density functional calculations should always be used. Continued efforts, such as the improved D3 methods$^{[86]}$ or the new D4 method,$^{[82,83]}$ will hopefully improve their accuracy further.

## 4.4 | Comparison of timing

As discussed above, a frequent concern for conformer screening is the relative computational performance. In general, classical molecular force field methods have been preferred as they allow the generation of hundreds of conformers per compound in seconds. While traditional high-level *ab initio* methods are considered a "gold standard" for thermochemical energies, the time required for a single-point energy evaluation may be high. For this work, all timings are single-core CPU times using a 2.60 GHz Intel Skylake CPU (Intel Xeon Gold 6126) with 192GB RAM per node.

As indicated in Figure 2, hybrid density functional methods such as B3LYP-D3BJ require significant single-computational time for single-point energies of medium-sized organic molecules (median $26 \pm 0.3$ minutes) compared to GGA methods, such as PBE, or approximate density functional tight binding methods, such as GFN1/GFN2 (median $2.6 \pm 0.06$ second yields ~600× speedup). Conventional density functional methods, nevertheless, represent a meaningful mid-point relative to the DLPNO-CCSD(T) method, which may be faster than traditional coupled-cluster methods but is still 5 to 10 times slower than B3LYP (ie, hours per single-point energy).

Consequently, an important consideration is also the typical tradeoff in computational chemistry between thermochemical accuracy and computational time. As traditional MP2 and coupled-cluster methods exhibit high computational complexity, much research ignored them for medium to large organic molecules due to the time required. Particularly in computational screening and conformer generation, fast molecular force fields such as MMFF94 and UFF, as well as semiempirical quantum chemical methods such as AM1,$^{[87]}$ PM3,$^{[88]}$ PM6,$^{[89]}$ and PM7,$^{[33]}$ were considered "good enough" to generate structures for further refinement with density functional and other methods. More recent methods, particularly the ANI machine learning methods and the GFN family of density functional tight binding, appear to significantly improve accuracy, with only modest increases in the time required.

We find that, consistent with common assumptions, even recent methods roughly adhere to the requirement of significant increases in computational (time) cost to gain increased thermochemical accuracy, as illustrated in Figure 3 with $R^2$. Similar trends are found for MARE and Spearman $\rho$ metrics. As multiple studies have demonstrated the need for accurate treatment of noncovalent interactions, including intramolecular electrostatic and dispersion effects for understanding conformer relative energies, it is not surprising that this benchmark illustrates the significant accuracy advantage of modern dispersion-corrected density functional and wavefunction methods.

## 4.5 | Use of machine learning methods as surrogates: ANI and bag-of-features

One possible solution to the tradeoff between accuracy and computational cost would be the growing use of machine learning (ML) methods in chemistry, particularly as a surrogate for thermochemical parameters such as atomization energies.$^{[90-92]}$ Typically, these ML methods use deep neural networks (DNNs) and have been trained for density functional calculations, particularly hybrid B3LYP or ωB97X atomization energies,$^{[93,94]}$ although recent efforts have included training on coupled-cluster quality data as well.$^{[52]}$

In principle, as the evaluation of the DNN is fast, the time required for the prediction of an ML method is dominated by the time to generate the input descriptors—still only a small fraction of that required for a quantum calculation. Therefore, if an ML method could reproduce density functional or coupled-cluster energies at semiempirical or force field computational cost, it would dramatically change the conventional accuracy/time tradeoff.

While evaluation of DNN methods would be significantly faster on graphics processing units (GPUs), and may not be optimized for CPU evaluation, we note that many quantum chemistry methods are also accelerated on GPUs. Thus, we retain the single-core CPU timings in Table 1 and Figure 3 but note that the actual speed of ML methods such as ANI would be faster when evaluated on a modern GPU.

## 4.6 | ANI methods

Table 1 and Figure 3 show the ANI family ML methods, ANI-1x, ANI-1ccx, and ANI-2x, performing similarly to GFN tight binding semiempirical methods in both accuracy and speed. ANI-1cxx outperforms the ANI-1x model that does not contain dispersion corrections while performing

![](./images/812592469769191426_3.jpg)

**FIGURE 2** Histograms of relative timings for key methods considered, normalized to B3LYP-D3BJ single points on the same molecule, using ORCA 4.0.1. Median relative times and median wall clock times for single-core runs are included for reference

![](./images/812592469769191426_4.jpg)

**FIGURE 3** Comparison of single-core computational time required for energy evaluation (in log scale) to median $R^2$ found when compared to DLPNO-CCSD(T) energies. Error bars indicate 95% confidence intervals of time and median $R^2$ from bootstrap sampling. Dashed line indicates approximate "best current method" threshold defined from force fields through RI-MP2 methods

slightly better than the ANI-2 model. The inclusion of dispersion correction for DFT methods is clearly beneficial as they improve upon their nondispersion-corrected counterparts, as seen in Table 2.

In principal, it is possible to perform post hoc addition of a D3 dispersion correction to both ANI-1x and ANI-2x. Table 3 shows potentially improved performance over their nondispersion-corrected counterparts, although the differences are not statistically significant. Moreover, as the D3 dispersion correction for ωB97X-D3 cannot be calculated by standard tools, applying such a post hoc correction is challenging. For our set,

<table><caption>TABLE 1 Overall statistics across all molecules studied and all methods</caption>
<tbody><tr><td>Method</td><td colspan="2">MARE</td><td colspan="2">R²</td><td colspan="2">Spearman ρ</td><td colspan="2">CPU time</td></tr>
<tr><td>DLPNO-CCSD(T)</td><td>0</td><td></td><td>1</td><td></td><td>1</td><td></td><td>2.19e+04</td><td>±2.77e+02</td></tr>
<tr><td>RI-MP2</td><td>0.115</td><td>[0.105-0.127]</td><td>0.964</td><td>[0.960-0.970]</td><td>0.952</td><td>[0.952-0.964]</td><td>2.12e+03</td><td>±4.23e+01</td></tr>
<tr><td>ωB97X-D3</td><td>0.160</td><td>[0.150-0.172]</td><td>0.929</td><td>[0.914-0.939]</td><td>0.915</td><td>[0.903-0.927]</td><td>2.52e+03</td><td>±3.57e+01</td></tr>
<tr><td>B3LYP (TZ)</td><td>0.168</td><td>[0.151-0.185]</td><td>0.920</td><td>[0.909-0.933]</td><td>0.915</td><td>[0.903-0.927]</td><td>1.67e+03</td><td>±2.07e+01</td></tr>
<tr><td>B97-3c</td><td>0.198</td><td>[0.180-0.224]</td><td>0.902</td><td>[0.888-0.915]</td><td>0.903</td><td>[0.881-0.915]</td><td>1.37e+02</td><td>±2.16e+00</td></tr>
<tr><td>PBE (TZ)</td><td>0.208</td><td>[0.190-0.227]</td><td>0.885</td><td>[0.868-0.904]</td><td>0.891</td><td>[0.879-0.903]</td><td>3.59e+02</td><td>±6.94e+00</td></tr>
<tr><td>PBEh-3c</td><td>0.207</td><td>[0.179-0.230]</td><td>0.879</td><td>[0.858-0.895]</td><td>0.879</td><td>[0.867-0.903]</td><td>4.53e+02</td><td>±9.46e+00</td></tr>
<tr><td>B3LYP (SVP)</td><td>0.228</td><td>[0.211-0.264]</td><td>0.868</td><td>[0.843-0.893]</td><td>0.879</td><td>[0.867-0.891]</td><td>3.31e+02</td><td>±4.35e+00</td></tr>
<tr><td>PBE (SVP)</td><td>0.265</td><td>[0.242-0.298]</td><td>0.835</td><td>[0.814-0.864]</td><td>0.855</td><td>[0.842-0.879]</td><td>1.49e+02</td><td>±2.24e+00</td></tr>
<tr><td>ANI-1ccx</td><td>0.439</td><td>[0.355-0.522]</td><td>0.638</td><td>[0.566-0.708]</td><td>0.713</td><td>[0.636-0.771]</td><td>1.45e+00</td><td>±3.40e-03</td></tr>
<tr><td>GFN2</td><td>0.389</td><td>[0.334-0.430]</td><td>0.637</td><td>[0.589-0.679]</td><td>0.717</td><td>[0.681-0.745]</td><td>2.60e+00</td><td>±6.50e-02</td></tr>
<tr><td>GFN1</td><td>0.350</td><td>[0.313-0.406]</td><td>0.622</td><td>[0.575-0.659]</td><td>0.697</td><td>[0.661-0.733]</td><td>2.66e+00</td><td>±5.00e-02</td></tr>
<tr><td>ANI-2x</td><td>0.410</td><td>[0.361-0.482]</td><td>0.620</td><td>[0.561-0.685]</td><td>0.685</td><td>[0.648-0.715]</td><td>3.45e+00</td><td>±5.71e-03</td></tr>
<tr><td>ANI-1x</td><td>0.449</td><td>[0.376-0.536]</td><td>0.594</td><td>[0.523-0.662]</td><td>0.654</td><td>[0.569-0.718]</td><td>1.46e+00</td><td>±4.14e-03</td></tr>
<tr><td>BATTY/n</td><td>0.415</td><td>[0.375-0.479]</td><td>0.467</td><td>[0.410-0.539]</td><td>0.500</td><td>[0.400-0.600]</td><td>1.45e-01</td><td>±2.16e-05</td></tr>
<tr><td>GFN0</td><td>0.439</td><td>[0.394-0.486]</td><td>0.405</td><td>[0.349-0.477]</td><td>0.527</td><td>[0.455-0.564]</td><td>6.50e-02</td><td>±5.00e-04</td></tr>
<tr><td>GAFF</td><td>1.638</td><td>[1.415-1.827]</td><td>0.348</td><td>[0.289-0.407]</td><td>0.479</td><td>[0.442-0.539]</td><td>5.28e-02</td><td>±5.73e-05</td></tr>
<tr><td>MMFF94</td><td>0.704</td><td>[0.581-0.845]</td><td>0.332</td><td>[0.286-0.382]</td><td>0.467</td><td>[0.430-0.515]</td><td>3.58e-03</td><td>±4.40e-05</td></tr>
<tr><td>BOB</td><td>1.922</td><td>[1.723-2.162]</td><td>0.319</td><td>[0.279-0.388]</td><td>0.100</td><td>[0.000-0.200]</td><td>1.41e-01</td><td>±3.92e-05</td></tr>
<tr><td>PM7</td><td>0.617</td><td>[0.555-0.712]</td><td>0.315</td><td>[0.265-0.357]</td><td>0.333</td><td>[0.273-0.406]</td><td>5.50e-02</td><td>±4.00e-03</td></tr>
<tr><td>BAT</td><td>1.177</td><td>[1.032-1.297]</td><td>0.314</td><td>[0.280-0.379]</td><td>0.200</td><td>[0.100-0.300]</td><td>1.79e-01</td><td>±1.32e-05</td></tr>
<tr><td>UFF</td><td>5.026</td><td>[4.396-5.614]</td><td>0.290</td><td>[0.240-0.338]</td><td>0.321</td><td>[0.238-0.406]</td><td>9.45e-04</td><td>±8.61e-06</td></tr>
</tbody></table>

Note: Columns indicate median mean absolute relative error (MARE in kcal/mol), median $R^2$ correlation, median Spearman correlation, and median single-core CPU time in seconds. MARE, $R^2$, and Spearman correlation are relative to the DLPNO-CCSD(T)/cc-pVTZ baseline. Ranges indicate 95% confidence intervals for the median metrics established by bootstrap sampling.

<table><caption>TABLE 2 Effect of dispersion correction for DFT methods</caption>
<tbody><tr><td rowspan="2">Method</td><td colspan="2">Median R²</td><td colspan="2">No dispersion</td><td colspan="2">Median Spearman ρ</td><td colspan="2">No dispersion</td></tr>
<tr><td></td><td>Dispersion</td><td></td><td></td><td></td><td>Dispersion</td><td></td><td></td></tr>
<tr><td>DLPNO-CCSD(T)</td><td>1</td><td></td><td>—</td><td></td><td>1</td><td></td><td>—</td><td></td></tr>
<tr><td>ωB97X</td><td>0.929</td><td>[0.914-0.939]</td><td>0.881</td><td>[0.862-0.901]</td><td>0.915</td><td>[0.903-0.927]</td><td>0.891</td><td>[0.873-0.903]</td></tr>
<tr><td>B3LYP (TZ)</td><td>0.920</td><td>[0.909-0.933]</td><td>0.706</td><td>[0.658-0.758]</td><td>0.915</td><td>[0.903-0.927]</td><td>0.782</td><td>[0.745-0.806]</td></tr>
<tr><td>PBE (TZ)</td><td>0.885</td><td>[0.868-0.904]</td><td>0.746</td><td>[0.707-0.788]</td><td>0.891</td><td>[0.879-0.903]</td><td>0.806</td><td>[0.770-0.830]</td></tr>
<tr><td>B3LYP (SVP)</td><td>0.868</td><td>[0.843-0.893]</td><td>0.731</td><td>[0.673-0.762]</td><td>0.879</td><td>[0.867-0.891]</td><td>0.782</td><td>[0.758-0.806]</td></tr>
<tr><td>PBE (SVP)</td><td>0.835</td><td>[0.814-0.864]</td><td>0.751</td><td>[0.702-0.788]</td><td>0.855</td><td>[0.842-0.879]</td><td>0.806</td><td>[0.770-0.830]</td></tr>
</tbody></table>

Note: Values in brackets indicate 95% confidence intervals from bootstrap sampling.

one could calculate the dispersion correction from the ωB97X-D3 calculations performed on the same molecule, but without such density functional calculations, applying dispersion correction would be impossible.

While the newer D4 correction$^{[82,83]}$ can be calculated using the DFTD4 program,$^{[95]}$ we find that adding D4 corrections worsens the median $R^2$ and Spearman metrics, although again, the differences are not statistically significant. The variance of applying D3 and D4 corrections to the ANI models illustrates the challenge in current ML methods. As they inherently add some error on top of the underlying data used for training the model, use of coupled-cluster or other highly accurate dispersion-corrected training is needed.

<table><caption>TABLE 3 Comparison of post hoc dispersion correction for ANI machine learning methods</caption>
<thead>
<tr>
<th>Method</th>
<th colspan="3">Median $R^2$</th>
<th colspan="3">Median Spearman $\rho$</th>
</tr>
<tr>
<th></th>
<th>No dispersion</th>
<th>D3</th>
<th>D4</th>
<th>No dispersion</th>
<th>D3</th>
<th>D4</th>
</tr>
</thead>
<tbody>
<tr>
<td>ANI-1ccx</td>
<td>0.638 [0.571-0.704]</td>
<td>– [0.571-0.708]</td>
<td>–</td>
<td>0.713</td>
<td>– [0.636-0.773]</td>
<td>–</td>
</tr>
<tr>
<td>ANI-1x</td>
<td>0.594 [0.517-0.664]</td>
<td>0.630 [0.574-0.719]</td>
<td>0.574 [0.480-0.665]</td>
<td>0.654</td>
<td>0.709 [0.648-0.745]</td>
<td>0.624 [0.558-0.709]</td>
</tr>
<tr>
<td>ANI-2x</td>
<td>0.620 [0.561-0.679]</td>
<td>0.655 [0.609-0.704]</td>
<td>0.596 [0.541-0.659]</td>
<td>0.685</td>
<td>0.705 [0.667-0.733]</td>
<td>0.661 [0.624-0.697]</td>
</tr>
</tbody>
</table>

Note: Values in brackets indicate 95% confidence intervals from bootstrap sampling.

## 4.7 | Bag-of-feature methods

The performance of the bag-of-features models, while faster than the ANI symmetry function models, were more comparable to the accuracy of force field methods. The inclusion of additional information to the descriptor, such as three- and four-body interactions and atom typing, was beneficial to the bag-of-features models, and the accuracy pales in comparison to the ANI symmetry function models.

Standard bag-of-features have, at minimum, a bag of nuclear charges and a bag of two-body interactions as seen in BOB, and further bags are added that contain additional information such as angles and torsions with BAT. This approach was taken for the BATTY representation with the modification of using minimal atom typing (ie, sp, sp², sp³ hybridization) to sort bags. Unlike other bag-of-features representations, the performance of BATTY was increased by removing the bags of nuclear charges and excluding the nonbonding interactions from the two-body interactions bag to create a bag of simple bonds. As relative conformer energies are strongly dominated by nonbonded interactions, this finding is surprising, although perhaps separating bonding and two-body nonbonded interactions facilitate ML training. A recent example, BAND-NN, took the approach of separating the bonding and nonbonding information similarly to classical force fields and finds an improvement in performance.[⁹⁶]

ML commonly uses techniques to normalize the data, improving the model's training.[⁹⁷,⁹⁸] In this work, we used physically motivated normalization techniques for the bag-of-features representations. Four molecular properties, the number of atoms, bonds, electrons, and the molecular mass, were chosen for normalizing the atomization energy (Table 4).

**TABLE 4** Effects of normalization descriptors on machine learning methods (eg, BATTY/n refers to BATTY with number of atom normalization)

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Normalization</th>
      <th colspan="2">MARE</th>
      <th colspan="2">R²</th>
      <th colspan="2">Spearman ρ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BOB</td>
      <td>—</td>
      <td>1.922</td>
      <td>[1.726-2.162]</td>
      <td>0.319</td>
      <td>[0.272-0.393]</td>
      <td>0.10</td>
      <td>[0.00-0.20]</td>
    </tr>
    <tr>
      <td>BOB</td>
      <td>Atoms</td>
      <td>1.944</td>
      <td>[1.763-2.174]</td>
      <td>0.358</td>
      <td>[0.317-0.422]</td>
      <td>0.10</td>
      <td>[0.00-0.20]</td>
    </tr>
    <tr>
      <td>BOB</td>
      <td>Mass</td>
      <td>2.202</td>
      <td>[1.933-2.410]</td>
      <td>0.323</td>
      <td>[0.267-0.371]</td>
      <td>0.10</td>
      <td>[−0.10 to 01.0]</td>
    </tr>
    <tr>
      <td>BOB</td>
      <td>Electrons</td>
      <td>2.058</td>
      <td>[1.750-2.283]</td>
      <td>0.316</td>
      <td>[0.276-0.372]</td>
      <td>0.00</td>
      <td>[−0.10 to 01.0]</td>
    </tr>
    <tr>
      <td>BOB</td>
      <td>Bonds</td>
      <td>5.092</td>
      <td>[4.460-5.775]</td>
      <td>0.272</td>
      <td>[0.239-0.320]</td>
      <td>0.00</td>
      <td>[−0.10 to 01.0]</td>
    </tr>
    <tr>
      <td>BAT</td>
      <td>—</td>
      <td>1.177</td>
      <td>[1.053-1.298]</td>
      <td>0.314</td>
      <td>[0.280-0.374]</td>
      <td>0.20</td>
      <td>[0.10-0.30]</td>
    </tr>
    <tr>
      <td>BAT</td>
      <td>Atoms</td>
      <td>1.356</td>
      <td>[1.191-1.493]</td>
      <td>0.343</td>
      <td>[0.279-0.402]</td>
      <td>0.10</td>
      <td>[0.10-0.30]</td>
    </tr>
    <tr>
      <td>BAT</td>
      <td>Mass</td>
      <td>1.403</td>
      <td>[1.272-1.549]</td>
      <td>0.310</td>
      <td>[0.271-0.365]</td>
      <td>0.20</td>
      <td>[0.10-0.30]</td>
    </tr>
    <tr>
      <td>BAT</td>
      <td>Electrons</td>
      <td>1.275</td>
      <td>[1.157-1.454]</td>
      <td>0.325</td>
      <td>[0.279-0.376]</td>
      <td>0.15</td>
      <td>[0.10-0.30]</td>
    </tr>
    <tr>
      <td>BAT</td>
      <td>Bonds</td>
      <td>1.617</td>
      <td>[1.451-1.807]</td>
      <td>0.352</td>
      <td>[0.304-0.399]</td>
      <td>0.10</td>
      <td>[0.00-0.20]</td>
    </tr>
    <tr>
      <td>BATTY</td>
      <td>—</td>
      <td>0.510</td>
      <td>[0.470-0.601]</td>
      <td>0.396</td>
      <td>[0.341-0.442]</td>
      <td>0.40</td>
      <td>[0.30-0.50]</td>
    </tr>
    <tr>
      <td>BATTY</td>
      <td>Atoms</td>
      <td>0.415</td>
      <td>[0.375-0.479]</td>
      <td>0.467</td>
      <td>[0.403-0.540]</td>
      <td>0.50</td>
      <td>[0.40-0.60]</td>
    </tr>
    <tr>
      <td>BATTY</td>
      <td>Mass</td>
      <td>0.691</td>
      <td>[0.606-0.749]</td>
      <td>0.411</td>
      <td>[0.352-0.475]</td>
      <td>0.40</td>
      <td>[0.30-0.50]</td>
    </tr>
    <tr>
      <td>BATTY</td>
      <td>Electrons</td>
      <td>0.628</td>
      <td>[0.545-0.714]</td>
      <td>0.417</td>
      <td>[0.351-0.477]</td>
      <td>0.40</td>
      <td>[0.30-0.50]</td>
    </tr>
    <tr>
      <td>BATTY</td>
      <td>Bonds</td>
      <td>0.423</td>
      <td>[0.370-0.499]</td>
      <td>0.479</td>
      <td>[0.407-0.543]</td>
      <td>0.50</td>
      <td>[0.40-0.60]</td>
    </tr>
  </tbody>
</table>

Note: Numbers in brackets indicate 95% confidence intervals for the median MARE, R², and Spearman ρ metrics.

**FIGURE 4** Histogram of relative DLPNO-CCSD(T) energy ranges across multiple conformers

![](./images/812592469769191426_5.jpg)

BATTY saw improvements in performance when normalizing by the number of atoms (ie, BATTY/n) and the number of bonds (BATTY/b) across Spearman, $R^2$, and MARE. The other bag-of-feature representations experienced a slight improvement in $R^2$ when normalizing by the number of atoms but not an improvement in the MARE. Normalizing the atomization energy for bag-of-features methods does provide minor improvements, but not enough to compete with the ANI-1 and ANI-2 methods.

ML methods, despite training on density functional and coupled-cluster energies, are still not as accurate as conventional quantum methods for predicting conformer energies. At present, the ANI family is comparable to the semiempirical GFN methods for accuracy on this task.

## 5 | DISCUSSION

### 5.1 | Effects of conformer energy ranges on accuracy metrics

Previous work has suggested that the poor correlations found between force field and semiempirical methods are derived from the small number of low-energy conformers considered in this benchmark.$^{[7]}$ Certainly, one might imagine that when considering multiple geometries with only small differences in energies, random errors are magnified. Figure 4 illustrates a histogram of the ranges in DLPNO-CCSD(T) energies across the molecules considered. Despite the small ranges in energies, there is little correlation between the energy range of a molecule and the accuracy metrics of a particular method. This suggests no bias from the small energy windows used in this benchmark set.

Figure 5 indicates that there is no correlation between $R^2$ and the energy window of the conformers. The ML methods have a relatively even distribution of $R^2$ across the energy window, indicating that random errors in the model may have more of an impact on performance than the size of the energy window.

![](./images/812592469769191426_6.jpg)

**FIGURE 5** Examples of the relation of energy windows to $R^2$ for the ML methods: A, ANI-1x, B, ANI-1ccx, C, BOB, and D, BATTY/# atoms

## 5.2 | Connection between accuracy metrics: MARE, R2, Spearman

In principle, the mean absolute relative errors in energies (MARE) consider both random and systematic errors of a method, while the $R^2$ and Spearman correlation metrics remove systematic errors through linear correlation ($R^2$) or ranking (Spearman $\rho$). However, for the comparisons here, there is a strong connection between all three metrics, as illustrated in Figure 6. Methods with a smaller MARE have almost a linear correlation with increased median $R^2$. The three classical force field methods have essentially the same median $R^2$ metric despite differences in MARE, likely due to systematic errors in the methods. Similarly, while increasing the data in the bag-of-features descriptors from BOB to BAT decreases the median MARE from 1.92 kcal/mol to 1.18 kcal/mol, the accuracy as judged by the median $R^2$ remains essentially constant (0.31 and 0.32, respectively) (Figure 6).

![](./images/812592469769191426_7.jpg)

FIGURE 6 Correlation between mean absolute relative energies (MARE) and median $R^2$ correlation. As the $R^2$ metric minimizes systematic errors, the high degree of correlation between the two metrics indicate most methods exhibit relatively random/nonsystematic errors. Error bars indicate 95% confidence intervals from bootstrap sampling

![](./images/812592469769191426_8.jpg)

FIGURE 7 Histogram of the range of B3LYP-computed dipole moments in Debye across the conformers considered in this work. While most molecules show only small differences in polarity across conformers, many have over 3 to 4 Debye ranges

![](./images/812592469769191426_9.jpg)

FIGURE 8 Example of conformational diversity in dipole moment in the molecule omegacsd_CNBPCT reflecting antiparallel carbonyl (left–rmsd45) or parallel carbonyl groups (right–rmsd92), with B3LYP-D3BJ def2-TZVP computed dipole moments ranging from 1.41D to 9.78D. The two geometries differ by only 1.3 kcal/mol at the B3LYP-D3BJ def2-TZVP level, with the more polar conformer (right) stabilized by an intramolecular hydrogen bond. Using DLPNO-CCSD(T) cc-pVTZ, the less polar conformer (left) is more stable by 0.3 kcal/mol

<table>
<thead>
<tr>
<th>Method</th>
<th colspan="2">Median time</th>
<th colspan="2">Median batch time</th>
<th>Speedup</th>
</tr>
</thead>
<tbody>
<tr>
<td>MMFF94</td>
<td>3.58e-03</td>
<td>±4.40e-05</td>
<td>5.05e-05</td>
<td>±6.02e-07</td>
<td>70.9</td>
</tr>
<tr>
<td>GAFF</td>
<td>5.28e-03</td>
<td>±5.73e-05</td>
<td>3.29e-05</td>
<td>±4.49e-07</td>
<td>160.6</td>
</tr>
<tr>
<td>UFF</td>
<td>9.45e-04</td>
<td>±8.61e-06</td>
<td>4.32e-05</td>
<td>±4.46e-07</td>
<td>21.9</td>
</tr>
<tr>
<td>ANI-1x</td>
<td>1.46</td>
<td>±4.14e-03</td>
<td>1.29e-02</td>
<td>±1.06e-04</td>
<td>113.2</td>
</tr>
<tr>
<td>ANI-1ccx</td>
<td>1.45</td>
<td>±3.40e-03</td>
<td>1.30e-02</td>
<td>±1.03e-04</td>
<td>111.5</td>
</tr>
<tr>
<td>ANI-2x</td>
<td>3.45</td>
<td>±5.71e-03</td>
<td>2.00e-02</td>
<td>±9.7e-05</td>
<td>172.4</td>
</tr>
</tbody>
</table>

**TABLE 5** Comparison of single-core median sequential time to median batch time (in seconds) and relative speedups for batch evaluation

## 5.3 | Dipole moment ranges

As we generally find very small energy differences between the conformers considered in this work, one might wonder whether such differences have meaningful consequences. Due to Boltzmann statistics, many properties are dominated by the lowest energy geometry, even with small energy windows to other geometries. One recent example comes from understanding the effects of dipole moments on solvent viscosity.⁶⁸ Finding all conformers with proper weighting is thus crucial to predicting the dipole moment of an ensemble of different conformers.

We find that, across the set of molecules considered, over 140 molecules have a range of 3 Debye or more, and 75 molecules have a range of 4 Debye or above across multiple conformers in the study (Figure 7).

Figure 8 illustrates the example of omegacsd_CNBPCT, with two conformers that are close in energy yet span dramatically different dipole moments. Using B3LYP-D3BJ (TZ), the computed dipole moments range from 1.41D to 9.78D. The molecule contains two carbonyl bonds, either parallel (high dipole moment) or antiparallel (low dipole moment) depending on the rotation of several bonds, and the more polar conformer is predicted to be more stable by B3LYP-D3BJ, possibly due to an intramolecular hydrogen bond. On the other hand, using DLPNO-CCSD(T) cc-pVTZ, the conformers differ by only 0.3 kcal/mol, with the antiparallel, less polar conformer more stable than the other.

Such polarity differences are examples in which small differences in conformer energies can have significant effects on molecular properties. As experimental properties reflect a Boltzmann-weighted average of multiple thermally accessible conformers, even small differences in conformer energies have large effects on populations involved in property prediction, as recently discussed with conformer and polarity effects on solvent viscosity.⁶⁸

## 5.4 | Machine learning batch evaluation

An advantage of ML and force field predictions is the ability to batch evaluate by loading all conformers of a molecule at once and evaluating them as a batch opposed to evaluating one at a time, as with conventional quantum chemistry methods. Table 5 indicates the median sequential times from Table 1 and median time per single point in batch evaluation. Speedups range ~70 to 170 times faster for both force field and ANI methods. We note that, while the ANI methods improve performance in batch evaluation, traditional force field methods do as well, with similar speedups.

## 6 | CONCLUSIONS

The current work extends previous efforts to consider the accuracy of modern computational chemistry methods to rank the energies of drug-like conformers. As such energy differences are small, this poses a challenging benchmark even for density functional methods. Use of dispersion corrections for density functionals are required—the less time required is offset with dramatically increased accuracy. While triple-zeta and larger basis sets also provide higher accuracy, likely because of better treatment of noncovalent interactions, the large number of possible conformers forces tradeoffs in accuracy and computational time required.

Current ML methods show great promise, particularly the ANI-1ccx method trained in part on coupled-cluster energies,⁵² as they provide accuracy comparable to the semiempirical GFN2 method and can be performed in batch and accelerated on GPUs. Despite claims of reaching and exceeding DFT accuracy, we do not find that these methods yet meet the accuracy of modern dispersion-corrected methods. Nevertheless, we expect these methods will provide increased accuracy in the future. An important caveat is the need to train on accurate data, such as dispersion-corrected density functional, MP2, or coupled-cluster calculations.

We expect continued improvement from other methods, particularly multiple efforts to improve classical force fields,⁹⁹⁻¹⁰² inclusion of polarizable atomic charges,¹⁰³⁻¹¹⁰ novel force fields from experimental data, density functional and other quantum methods,¹¹¹⁻¹¹⁶ and continued development of approximate semiempirical quantum methods.³⁷

Currently, we can highly recommend methods at each tier of the accuracy-time tradeoff, particularly the recent GFN2 semiempirical method, the B97-3c density functional approximation, and RI-MP2 for accurate conformer energies. Previous efforts to use a hierarchy of methods are still

useful, for example, the use of GFN2 methods to refine initial conformer ensembles, followed by refinement of a smaller set of low-energy geometries with more accurate methods. Batch evaluation with ANI methods are also efficient, although they do not yet span the range of elements supported by semiempirical methods such as GFN2 or density functional methods.

The current benchmark reflects conformational preferences in a vacuum as judged by enthalpy differences alone. As free energy differences drive experimental conformers, introducing entropic considerations will be needed for further work. $^{[15]}$ Moreover, much chemistry is performed in solution; thus, work on understanding conformer energies in solvation is also critical. $^{[117,118]}$

## ACKNOWLEDGMENTS
GRH and DLF acknowledge the National Science Foundation (CHE-1800435) for support and the University of Pittsburgh Center for Research Computing through the computational resources provided. The authors thank Olexandr Isayev and Justin Smith for access to the ANI-2x model.

## AUTHOR CONTRIBUTIONS
Geoffrey Hutchison: Conceptualization; funding acquisition; investigation; methodology; resources; supervision; validation; writing-original draft; writing-review and editing. Dakota Folmsbee: Investigation; methodology; validation; visualization; writing-original draft; writing-review and editing.

## SUPPORTING INFORMATION
Additional supporting information may be found at the GitHub repository for this article: https://github.com/ghutchis/conformer-benchmark.

## PEER REVIEW DETAILS
Open Peer Reviewer Details for this article are openly available here:

- Peer Reviewer Report #1 DOI: 10.22541/au.159189857.79976995.
- Peer Reviewer Report #2 DOI: 10.22541/au.159189857.70478172.
- Author Response DOI: 10.22541/au.159189985.55415173.

## ORCID
Geoffrey Hutchison https://orcid.org/0000-0002-1757-1980

## REFERENCES
[1] S. Grimme, *Reviews in Computational Chemistry*, John Wiley & Sons Inc, Hoboken, NJ 2004, pp. 153-218.
[2] M. W. Lodewyk, M. R. Siebert, D. J. Tantillo, *Chem. Rev.* 2011, 112, 1839.
[3] N. E. Jackson, B. M. Savoie, K. L. Kohlstedt, T. J. Marks, L. X. Chen, M. A. Ratner, *Macromolecules* 2014, 47, 987.
[4] P. C. D. Hawkins, *J. Chem. Info. Model.* 2017, 57, 1747.
[5] I. Y. Kanal, J. A. Keith, G. R. Hutchison, *Int. J. Quantum Chem.* 2017, 118, e25512.
[6] M. Habgood, T. James, A. Heifetz, *Conformational Searching with Quantum Mechanics*, Springer US, New York, NY 2020.
[7] D. I. Sharapa, A. Genaev, L. Cavallo, Y. Minenkov, *ChemPhysChem* 2019, 20, 92.
[8] M. K. Kesharwani, A. M. L. Martin, *J. Chem. Theory Comput.* 2015, 12, 444.
[9] J. Řezáč, D. Bím, O. Gutten, L. Rulíšek, *J. Chem. Theory. Comput.* 2018, 14, 1254.
[10] V. K. Prasad, A. Otero-de-la-Roza, G. A. DiLabio, *Sci. Data* 2019, 6, 180310. https://doi.org/10.1038/sdata.2018.310.
[11] Y. K. Kang, H. S. Park, *Chem. Phys. Lett.* 2018, 702, 69.
[12] Y. Yuan, M. J. L. Mills, P. L. A. Popelier, F. Jensen, *J. Phys. Chem. A* 2014, 118, 7876.
[13] B. K. Rai, V. Sresht, Q. Yang, R. Unwalla, M. Tu, A. M. Mathiowetz, G. A. Bakken, *J. Chem. Info. Model.* 2019, 59, 4195.
[14] N. Foloppe, I.-J. Chen, *Future Med. Chem.* 2019, 11, 97.
[15] M. P. Johansson, J. Olsen, *J. Chem. Theory Comput.* 2008, 4, 1460.
[16] N. E. Jackson, B. M. Savoie, K. L. Kohlstedt, M. O. de la Cruz, G. C. Schatz, L. X. Chen, M. A. Ratner, *J. Am. Chem. Soc.* 2013, 135, 10475.
[17] L. A. Curtiss, K. Raghavachari, P. C. Redfern, V. Rassolov, J. A. Pople, *J. Chem. Phys.* 1998, 109, 7764.
[18] L. A. Curtiss, P. C. Redfern, K. Raghavachari, *J. Chem. Phys.* 2007, 126, 084108.
[19] J. M. L. Martin, G. de Oliveira, *J. Chem. Phys.* 1999, 111, 1843.
[20] S. Parthiban, J. M. L. Martin, *J. Chem. Phys.* 2001, 114, 6014.
[21] A. Karton, E. Rabinovich, J. M. L. Martin, B. Ruscic, *J. Chem. Phys.* 2006, 125, 144108.
[22] M. G. Ghahremanpour, P. J. van Maaren, J. C. Ditz, R. Lindh, D. van der Spoel, *J. Chem. Phys.* 2016, 145, 114305.
[23] P. C. Hawkins, A. G. Skillman, G. L. Warren, B. A. Ellingson, M. T. Stahl, *J Chem Inf Model* 2010, 50, 572.
[24] J. Juárez-Jiménez, X. Barril, M. Orozco, R. Pouplana, F. J. Luque, *J. Phys. Chem. B* 2014, 119, 1164.
[25] N. M. O'Boyle, M. Banck, C. A. James, C. Morley, T. Vandermeersch, G. R. Hutchison, *J Cheminform* 2011, 3, 33.
[26] T. A. Halgren, *J. Comput. Chem.* 1996, 17, 490.
[27] T. A. Halgren, *J. Comput. Chem.* 1996, 17, 520.
[28] T. A. Halgren, *J. Comput. Chem.* 1996, 17, 553.

[29] T. A. Halgren, R. B. Nachbar, J. Comput. Chem. 1996, 17, 587.

[30] T. A. Halgren, J. Comput. Chem. 1996, 17, 616.

[31] A. K. Rappe, C. J. Casewit, K. S. Colwell, W. A. Goddard, W. M. Skiff, J. Am. Chem. Soc. 1992, 114, 10024.

[32] C. J. Casewit, K. S. Colwell, A. K. Rappe, J. Am. Chem. Soc. 1992, 114, 10035.

[33] J. J. P. Stewart, J. Mol. Model. 2012, 19, 1.

[34] grimme-lab/xtb. https://github.com/grimme-lab/xtb.

[35] P. Pracht, E. Caldeweyher, S. Ehlert, S. Grimme, 2019, https://doi.org/10.26434/chemrxiv.8326202.v1.

[36] S. Grimme, C. Bannwarth, P. Shushkov, J Chem Theory Comput 2017, 13, 1989.

[37] C. Bannwarth, S. Ehlert, S. Grimme, 2018, https://doi.org/10.26434/chemrxiv.7246238.v2.

[38] F. Neese, The ORCA program system Wiley Interdisciplinary Reviews: Computational Molecular Science, 2012, 2, 73, https://doi.org/10.1002/wcms.81.

[39] S. Grimme, S. Ehrlich, L. Goerigk, J. Comput. Chem. 2011, 32, 1456.

[40] A. D. Becke, E. R. Johnson, J. Chem. Phys. 2005, 123, 154101.

[41] E. R. Johnson, A. D. Becke, J. Chem. Phys. 2005, 123, 024101.

[42] E. R. Johnson, A. D. Becke, J. Chem. Phys. 2006, 124, 174104.

[43] J.-D. Chai, M. Head-Gordon, Phys. Chem. Chem. Phys. 2008, 10, 6615.

[44] S. Kossmann, F. Neese, J. Chem. Theory Comput. 2010, 6, 2325.

[45] D. G. Liakos, F. Neese, J. Chem. Theory Comput. 2015, 11, 4054.

[46] Y. Guo, C. Riplinger, U. Becker, D. G. Liakos, Y. Minenkov, L. Cavallo, F. Neese, J. Chem. Phys. 2018, 148, 011101.

[47] T. H. Dunning, J. Chem. Phys. 1989, 90, 1007.

[48] R. A. Kendall, T. H. Dunning, R. J. Harrison, J. Chem. Phys. 1992, 96, 6796.

[49] N. M. Oboyle, A. L. Tenderholt, K. M. Langner, J. Comput. Chem. 2008, 29, 839.

[50] N. M. OBoyle, C. Morley, G. R. Hutchison, Chem. Cent. J. 2008, 2, 5.

[51] J. S. Smith, B. Nebgen, N. Lubbers, O. Isayev, A. E. Roitberg, J. Chem. Phys. 2018, 148, 241733.

[52] J. S. Smith, B. T. Nebgen, R. Zubatyuk, N. Lubbers, C. Devereux, K. Barros, S. Tretiak, O. Isayev, A. Roitberg, 2019, https://doi.org/10.26434/chemrxiv.6744440.v2.

[53] C. Devereux, J. Smith, K. Davis, K. Barros, R. Zubatyuk, O. Isayev, A. Roitberg, J. Chem. Theory Comput. 2020. https://doi.org/10.1021/acs.jctc.0c00121.

[54] K. Hansen, F. Biegler, R. Ramakrishnan, W. Pronobis, O. A. von Lilienfeld, K.-R. Müller, A. Tkatchenko, J. Phys. Chem. Lett. 2015, 6, 2326.

[55] B. Huang, O. A. von Lilienfeld, J. Chem. Phys. 2016, 145, 161102.

[56] D. Folmsbee, S. Upadhyay, A. Dumi, D. Hiener, D. Mulvey, 2019, https://doi.org/10.5281/zenodo.3333856.

[57] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, É. Duchesnay, J. Mach. Learn. Res. 2011, 12, 2825.

[58] W. McKinney, Proceedings of the 9th Python in Science Conference, Austin, Texas 2010, p. 51.

[59] S. van der Walt, S. C. Colbert, G. Varoquaux, Comput. Sci. Eng. 2011, 13, 22.

[60] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, İ. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, Nat. Met. 2020, 17, 261.

[61] N. Rego, D. Koes, Bioinformatics 2014, 31, 1322.

[62] Plotly Technologies Inc. Collaborative data science, 2020, https://plot.ly/.

[63] J. P. Ebejer, G. M. Morris, C. M. Deane, J Chem Inf Model 2012, 52, 1146.

[64] M. J. Hartshorn, M. L. Verdonk, G. Chessari, S. C. Brewerton, W. T. Mooij, P. N. Mortenson, C. W. Murray, J Med Chem 2007, 50, 726.

[65] D. Weininger, J. Chem. Info. Model. 1988, 28, 31.

[66] E. Paulechka, A. Kazakov, J. Phys. Chem. A 2017, 121, 4379.

[67] D. G. Liakos, Y. Guo, F. Neese, J. Phys. Chem. A 2019, 124, 90.

[68] M. N. Vo, M. Call, C. Kowall, J. K. Johnson, Indus. Eng. Chem. Res. 2019, 58, 19263.

[69] J. Wang, R. M. Wolf, J. W. Caldwell, P. A. Kollman, D. A. Case, J. Comput. Chem. 2004, 25, 1157.

[70] S. Grimme, J. G. Brandenburg, C. Bannwarth, A. Hansen, J. Chem. Phys. 2015, 143, 054107.

[71] J. G. Brandenburg, C. Bannwarth, A. Hansen, S. Grimme, J. Chem. Phys. 2018, 148, 064104.

[72] C. Lee, W. Yang, R. G. Parr, Phys. Rev. B 1988, 37, 785.

[73] A. D. Becke, Phys. Rev. A 1988, 38, 3098.

[74] P. J. Stephens, F. J. Devlin, C. F. Chabalowski, M. J. Frisch, J. Phys. Chem. 1994, 98, 11623.

[75] S. H. Vosko, L. Wilk, M. Nusair, Canadian J. Phys. 1980, 58, 1200.

[76] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1997, 78, 1396.

[77] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1996, 77, 3865.

[78] F. Weigend, R. Ahlrichs, Phys. Chem. Chem. Phys. 2005, 7, 3297.

[79] F. Weigend, Phys. Chem. Chem. Phys. 2006, 8, 1057.

[80] J. M. L. Martin, J. Phys. Chem. A 2013, 117, 3118.

[81] D. Gruzman, A. Karton, J. M. L. Martin, J. Phys. Chem. A 2009, 113, 11974.

[82] E. Caldeweyher, C. Bannwarth, S. Grimme, J. Chem. Phys. 2017, 147, 034112.

[83] E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, S. Grimme, J. Chem. Phys. 2019, 150, 154122.

[84] S. Grimme, Density functional theory with London dispersion corrections. Wiley Interdisciplinary Reviews: Computational Molecular Science, 2011, 1, p. 211.https://doi.org/10.1002/wcms.30.

[85] E. R. Johnson, I. D. Mackie, G. A. DiLabio, J. Phys. Org. Chem. 2009, 22, 1127.

[86] J. Witte, N. Mardirossian, J. B. Neaton, M. Head-Gordon, J. Chem. Theory Comput. 2017, 13, 2043.

[87] M. J. S. Dewar, E. G. Zoebisch, E. F. Healy, J. J. P. Stewart, J. Am. Chem. Soc. 1985, 107, 3902.

[88] J. J. P. Stewart, J. Comput. Chem. 1989, 10, 209.

[89] J. J. P. Stewart, J. Mol. Model. 2007, 13, 1173.

[90] M. Rupp, A. Tkatchenko, K.-R. Müller, O. A. von Lilienfeld, Phys. Rev. Lett. 2012, 108, 058301.

[91] K. Hansen, G. Montavon, F. Biegler, S. Fazli, M. Rupp, M. Scheffler, O. A. von Lilienfeld, A. Tkatchenko, K.-R. Müller, J. Chem. Theory Comput. 2013, 9, 3404.

[92] F. A. Faber, L. Hutchison, B. Huang, J. Gilmer, S. S. Schoenholz, G. E. Dahl, O. Vinyals, S. Kearnes, P. F. Riley, O. A. von Lilienfeld, J. Chem. Theory Comput. 2017, 13, 5255.

[93] R. Ramakrishnan, P. O. Dral, M. Rupp, O. A. von Lilienfeld, Sci. Data 2014, 1, 1.

[94] J. S. Smith, O. Isayev, A. E. Roitberg, Chem. Sci. 2017, 8, 3192.

[95] dftd4/dftd4. https://github.com/dftd4/dftd4.

[96] S. Laghuvarapu, Y. Pathak, U. D. Priyakumar, J. Comput. Chem. 2019, 41, 790.

[97] S. Ioffe, C. Szegedy, arXiv 2015 abs/1502.03167.

[98] G. Klambauer, T. Unterthiner, A. Mayr, S. Hochreiter, Advances in Neural Information Processing Systems 30, Curran Associates Inc., Long Beach, CA 2017, p. 971.

[99] J. Wahl, J. Freyss, M. von Korff, T. Sander, J. Cheminformat. 2019, 11, 53.

[100] D. van der Spoel, M. M. Ghahremanpour, J. A. Lemkul, J. Phys. Chem. A 2018, 122, 8982.

[101] K. Roos, C. Wu, W. Damm, M. Reboul, J. M. Stevenson, C. Lu, M. K. Dahlgren, S. Mondal, W. Chen, L. Wang, R. Abel, R. A. Friesner, E. D. Harder, J. Chem. Theory Comput. 2019, 15, 1863.

[102] E. Harder, W. Damm, J. Maple, C. Wu, M. Reboul, J. Y. Xiang, L. Wang, D. Lupyan, M. K. Dahlgren, J. L. Knight, J. W. Kaus, D. S. Cerutti, G. Krilov, W. L. Jorgensen, R. Abel, R. A. Friesner, J. Chem. Theory Comput. 2016, 12, 281.

[103] F.-Y. Lin, A. D. MacKerell, Biomolecular Simulations: Methods and Protocols, Springer New York, New York, NY 2019, p. 21.

[104] V. S. S. Inakollu, D. P. Geerke, C. N. Rowley, H. Yu, Curr. Opinion Struct. Biol. 2020, 61, 182.

[105] A. Warshel, M. Kato, A. V. Pisliakov, J. Chem. Theory Comput. 2007, 3, 2034.

[106] Z. Jing, C. Liu, S. Y. Cheng, R. Qi, B. D. Walker, J.-P. Piquemal, P. Ren, Ann. Rev. Biophys. 2019, 48, 371.

[107] C. Zhang, C. Lu, Z. Jing, C. Wu, J.-P. Piquemal, J. W. Ponder, P. Ren, J. Chem. Theory Comput. 2018, 14, 2084.

[108] J. A. Rackers, Q. Wang, C. Liu, J.-P. Piquemal, P. Ren, J. W. Ponder, Phys. Chem. Chem. Phys. 2017, 19, 276.

[109] J. W. Ponder, C. Wu, P. Ren, V. S. Pande, J. D. Chodera, M. J. Schnieders, I. Haque, D. L. Mobley, D. S. Lambrecht, R. A. DiStasio, M. Head-Gordon, G. N. I. Clark, M. E. Johnson, T. Head-Gordon, J. Phys. Chem. 2010, 114, 2549.

[110] C. Liu, J.-P. Piquemal, P. Ren, J. Chem. Theory Comput. 2019, 15, 4122.

[111] The Open Force Field 1.0 small molecule force field, our first optimized force field (codename Parsley). https://openforcefield.org/news/introducing-openforcefield-1.0/.

[112] K. A. Beauchamp, J. M. Behr, A. S. Rustenburg, C. I. Bayly, K. Kroenlein, J. D. Chodera, J. Phys. Chem. B 2015, 119, 12912.

[113] C. Zanette, C. C. Bannan, C. I. Bayly, J. Fass, M. K. Gilson, M. R. Shirts, J. D. Chodera, D. L. Mobley, J. Chem. Theory Comput. 2018, 15, 402.

[114] B. Waldher, J. Kuta, S. Chen, N. Henson, A. E. Clark, J. Comput. Chem. 2010, 31, 2307.

[115] F. Zahariev, N. D. Silva, M. S. Gordon, T. L. Windus, M. Dick-Perez, J. Chem. Info. Model. 2017, 57, 391.

[116] S. Grimme, J. Chem. Theory Comput. 2014, 10, 4497.

[117] Y. Basdogan, A. M. Maldonado, J. A. Keith, WIREs Comput. Mol. Sci. 2020, 10, e1446.

[118] Y. Basdogan, J. A. Keith, Chem. Sci. 2018, 9, 5341.

How to cite this article: D Folmsbee, G Hutchison. Assessing conformer energies using electronic structure and machine learning methods. Int J Quantum Chem. 2020;e26381. https://doi.org/10.1002/qua.26381