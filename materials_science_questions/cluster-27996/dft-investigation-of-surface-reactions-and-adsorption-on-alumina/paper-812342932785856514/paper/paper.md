![](./images/812342932785856514_1.jpg)

Available online at www.sciencedirect.com

![](./images/812342932785856514_2.jpg)

Journal of Catalysis 227 (2004) 77–89

# JOURNAL OF
CATALYSIS

www.elsevier.com/locate/jcat

# Density-functional theory characterization of acid sites in chabazite

Cynthia Lo, Bernhardt L. Trout $^{*}$

Department of Chemical Engineering, Massachusetts Institute of Technology, 77 Massachusetts Avenue, Room 66-458, Cambridge, MA 02139, USA

Received 1 March 2004; revised 27 May 2004; accepted 16 June 2004
Available online 30 July 2004

## Abstract

The nature of the acid sites in zeolites and the factors contributing to enhanced catalytic activity have been the subject of much study in the literature. In particular, the issue of whether all of the acid sites in a particular zeolite are homogeneous or heterogeneous in acid strength requires the development of a systematic way to quantify acidity. To address this, we performed a detailed density-functional theory (DFT) investigation of the reactivity of the acid sites in the zeolite chabazite. We calculated energies of adsorption of bases, deprotonation energies, and vibrational frequencies on a periodic chabazite (SSZ-13) model with various loadings of acid sites per unit cell, and with various structural framework defects. We found that the four acidic oxygens at the aluminum T site all have roughly the same proton affinity, and the deprotonation energy is not correlated to the O–H bond length or vibrational stretch frequency. Furthermore, we found that the adsorption energy of various bases at each acid site oxygen is roughly the same and correlated only to the gas-phase proton affinity of the base; it does not vary significantly with acid-site concentration or framework defects near the acid site. Given the range of local chemical structure that we investigated, our results suggest that the strength of the acid sites in chabazite is not influenced significantly by chemical or structural variations in the framework near the acid site.

© 2004 Elsevier Inc. All rights reserved.

Keywords: Ab initio; Acid-site concentration; Acid-site homogeneity; Acid strength; Base adsorption; Chabazite; Density-functional theory; Periodic boundary conditions; Silanol; Zeolite

## 1. Introduction

If we had a thorough understanding of how zeolites and other solid acids catalyze reactions, we would be able to design more effective heterogeneous catalysts [1]. Unfortunately, we do not yet have even a simple measure for quantifying the acidity of the Brønsted sites in zeolites. Various measures have been proposed, including the O–H bond length and infrared (IR) frequency [2], intensities of the IR O–H stretching bands [3], deprotonation energy (proton affinity), heats of adsorption of ammonia, pyridine, and other small base probe molecules measured by microcalorimetry and thermal-programmed desorption [4], energy barriers for proton jump between neighboring oxygen atoms measured by variable temperature $^{1}$H NMR [5], and even a lumped intrinsic acidity that is defined as the quotient of the O–H bond length and the O–H vibrational frequency [6].

Furthermore, there is no adequate scale for solid acidity that is analogous to the $pK_a$ and Hammett acidity function [7] for aqueous acidity. Haw and co-workers [9,10] found that $^{19}$F and $^{15}$N NMR could be used to measure the spectroscopic changes of Hammett bases adsorbed onto zeolites. However, it was pointed out by Fărcaşiu and Ghenciu [8] that the Hammett acidity values of solid acids are not useful measures of acidity and not correlated with the catalytic activity, since the protonation of a base by a solid acid site leads to the formation of a localized tight ion pair, for which the requirement of the neutral and protonated base having identical activity coefficients is not satisfied.

In particular, the issue of whether all of the acid sites in a particular zeolite are homogeneous or heterogeneous in acid strength requires the development of a systematic way to quantify acidity. It has been hypothesized by several researchers that the acid strength is affected by physical

$^{*}$ Corresponding author.
E-mail address: trout@mit.edu (B.L. Trout).

0021-9517/$ – see front matter © 2004 Elsevier Inc. All rights reserved.
doi:10.1016/j.jcat.2004.06.018

properties of the local framework structure and constituent atoms, and the Brønsted sites are heterogeneous in acid strength. Our goal was a quantitative understanding of the factors that are responsible for differences in catalytic activ- ity and how zeolites catalyze reactions, with the objective of using this information to design catalysts more effectively. We hope that by studying structure-property relationships in zeolites, we will provide insight into whether the strength of a zeolite's catalytic activity is determined primarily by dif- ferences in acid-site strengths and geometric properties, or whether the influences are external and unrelated to the acid site. In this study, we focus on understanding the effects of local structural defects on energetic properties at the acid site of a given zeolite, and evaluating several measures to probe the acid strength of the Bronsted sites.

We use first-principle computational methods, which en- able us to study individual molecular interactions as op- posed to macroscopic averages. We use as our model zeolite chabazite (SSZ-13) (Fig. 1), which has 36 atoms in its unit cell. Chabazite contains two 8T, three 4T, and one 6T ring, where an 8T ring, for example, contains eight Si or Al atoms, and eight O atoms. Although chabazite is not as widely used in industry as ZSM-5, it has been shown to be catalytically active for the methanol-to-olefins process [18]. We choose chabazite mainly because of the small size of its unit cell, which means that the zeolite structure can be modeled as a periodic system, as opposed to using the cluster approx- imation, which treats just the atoms near the acid site and saturates the dangling bonds of the cluster with hydrogen atoms. We believe that the periodic approach is more repre- sentative of the physical system because the interactions of adsorbed molecules with the zeolite framework, not just at the acid site, are explicitly included. Also, the use of periodic models means that we can include the long-range electrosta- tic potential of the zeolite without using linking methods.

![](./images/812342932785856514_3.jpg)

Fig. 1. Perspective view down a channel of 8T rings in protonated chabazite with 1 Al/unit cell.

We study as our model system a chabazite framework that has been modified with chemical and structural defects, in order to determine if there exist intrinsic differences in acid- site strengths in the same zeolite, and whether there exists a correlation between the structural properties and the energet- ics of acid sites. We present calculations of four properties:

(1) deprotonation energies,
(2) base adsorption energies, which can be measured exper- imentally using temperature-programmed desorption,
(3) O-H vibrational frequencies, which can be probed using infrared spectroscopy, and bond lengths at the acid site, and
(4) topological visualization of the electron localization function.

In particular, base adsorption energies and O-H vibrational frequencies have been used to quantify differences in acidity between different zeolites, so we feel confident that we can use similar measures to quantify differences in acid strengths in the same zeolite.

The bases that we study are methanol, acetonitrile, am- monia, and pyridine. We choose these four bases in partic- ular because they exhibit a range of basicity and have been studied by other researchers in different contexts using dif- ferent experimental methodologies [19]. When acetonitrile adsorbs to the acid site, changes in the IR spectrum have been observed [20]. Temperature-programmed desorption of amines, such as ammonia and pyridine, is probably the most widely used method to measure heats of adsorption and the concentration of acid sites. Methanol has been extensively studied theoretically and computationally as an adsorption probe molecule for the acid sites [21-29]. We note, however, that many of the quantum calculations performed on these bases, methanol in particular, use several different zeolite models. We hope that by performing a large set of calcula- tions using the same methods on chabazite, we will be able to offer some insight into the factors affecting zeolite acidity.

## 2. Computational methodology

In order to calculate properties of the various chabazite structures and electronic energies, we use density-functional theory [30-32] (DFT). This method allows us to compute en- ergetic and spectroscopic properties with as much accuracy as possible for a large and complex chemical system. The exchange-correlation energy used is the generalized gradi- ent approximation (GGA) of Perdew and Wang [33]. Norm- conserving Troullier-Martins pseudopotentials [34] were used to reduce the computational cost relative to all-electron calculations, while maintaining an accurate net charge den- sity for the nuclei and core electrons.

In general, DFT can predict structural properties within 0.05 Å and 1–2°, overall adsorption and reaction energies within 20–30 kJ/mol, and spectroscopic data within a few percent of experiment [35]. It is generally considered that relative errors are less than absolute ones, and we take 10 kJ/mol as the relative error on energies. The PW91 functional was chosen because it includes interactions between adsorbates and the zeolite framework and gives accurate bond lengths and other structural properties. While dispersive interactions are not included physically, it has been shown that PW91 accurately models van der Waals interactions, for example, in Ar–Ar [36] and N₂–N₂ [37] interactions.

All calculations were performed using the Car-Parrinello Molecular Dynamics (CPMD) code, version 3.3 [38]. This code employs a plane-wave basis set with periodic boundary conditions, in order to model chabazite as an infinite crystalline system. A plane-wave cutoff of 55 Ry was chosen to match the cutoffs used by Payne and co-workers [24,39], and also because it is quite accurate, as will be seen in Section 3.3. We sampled only the $\Gamma$ point in the Brillouin zone.

During the geometry optimizations, all atoms, including those in the zeolite framework, were free to move; however, the lattice vectors of the unit cell are fixed. Govind et al. [40] calculated the difference in total energy of faujasite, using a fixed unit cell and a fully optimized cell, to be only 0.2 kJ/mol, so our use of fixed lattice parameters is accurate while reducing the computational cost. Chabazite (SSZ-13) has a trigonal unit cell ($a = b = c = 9.281$ Å, $\alpha = \beta = \gamma = 94.275^\circ$), and we used the structural parameters determined by Smith et al. [11] using neutron diffraction. Our main model system contained 1 aluminum T site per unit cell, for a Si/Al ratio of 11. The presence of only one aluminum substituent, itself a chemical defect, per unit cell allowed us to consider just the interaction between the probe molecule and the acid site and siliceous framework. We later employed chabazite models with 2 Al atoms per unit cell, both in the 8T ring, and incorporated a silanol defect into the chabazite framework.

## 3. Results and discussion

### 3.1. Proton position on acid-site oxygens

First, we wanted to determine whether there are one or two possible proton positions per acid site. Cook et al. [41] performed calculations on a cluster model of the T12 acid site of H-ZSM-5 and found only one stable proton position forming a $10^\circ$ angle with the Al–O–Si plane. Smith et al. [11], however, performed neutron diffraction experiments on chabazite that showed a single proton position situated at an out-of-plane angle of either 45 or $19^\circ$, depending on the acid site considered. The results of deuterium NMR experiments on HZSM-5 by Kobe et al. [42] suggested a proton out-of-plane angle of $55^\circ$. Their results implied that two proton positions per oxygen are possible.

Kobe et al. [42] proposed a model involving motional averaging, whereby the Brønsted acid deuteron can jump between lobes on the $\text{sp}^3$-hybridized oxygen. The justification for this model, as opposed to one where an $\text{sp}^2$-hybridized oxygen is in a planar Al–OH–Si structure, is that the latter model cannot produce certain peaks visible in the NMR spectrum of ZSM-5. Although the observed Al–OH–Si angles in chabazite (around $130^\circ$) are not close to either $120^\circ$ ($\text{sp}^2$) or $109.5^\circ$ ($\text{sp}^3$), we can attribute this discrepancy to the distortions in the zeolite lattice when Al is substituted for Si. In order to maximize proton overlap with the oxygen lone pairs, the H atom is restricted to the plane bisecting the Al–O–Si angle.

We used two methods to evaluate the characteristics of protons in various positions: a topological analysis and a constrained geometry optimization. For the topological analysis, we computed the electron localization function [43,44] (ELF), as presented in Eq. (1). The ELF is normalized between 0 and 1 and describes the probability of finding an electron near another electron with the same spin.

$$
\text{ELF} = \frac{1}{1 + \chi^2}, \tag{1}
$$

$$
\chi = \frac{\sum_i |\nabla \psi_i|^2 - (1/4)(\nabla \rho)^2/\rho}{C\rho^{5/3}}. \tag{2}
$$

The ELF isosurfaces for chabazite with one active site per unit cell are shown in Fig. 2; $\chi = 0.87$ was chosen for

![](./images/812342932785856514_4.jpg)

Fig. 2. ELF isosurfaces ($\chi = 0.87$) for chabazite with one active site per unit cell. (a) Corresponds to out-of-plane angle $= 35.7^\circ$ and (b) corresponds to out-of-plane $= -39.5^\circ$, where the proton is situated out of the Al–O–Si plane.

ease of visualization of the lobe features. There is one large lobe corresponding to the most stable proton position, and a much smaller U-shaped lobe corresponding to a possible metastable proton position. This suggests that there may be two possible proton positions.

We then performed geometry optimizations on the chab- azite structure, constraining the proton position at various out-of-plane angles relative to the Al-O-Si plane. The to- tal energy of chabazite as a function of out-of-plane angle is shown in Fig. 3, with the reference zero energy correspond- ing to the optimized structure without constraints. There are two minima: a deeper minimum at an out-of-plane angle of $35.7^{\circ}$ corresponding to the optimized structure, and a shal lower minimum, approximately 6.30 kJ/mol less stable, at an out-of-plane angle of $-39.5^{\circ}$ , as indicated by the ELF isosurfaces. The magnitude of the out-of-plane angle of the more stable position is consistent with the results of Smith et al. [11], but higher than the calculated $13.7^{\circ}$ out-of-plane angle of Jeanvoine et al. [45] for the O3 site. We note that the out-of-plane angles corresponding to the two minima are similar in magnitude, and thus are further evidence support- ing the $sp^{3}$ -hybridized model for oxygen, with its lone pairs symmetric across the Al-O-Si plane.

We performed a similar study of the O2 acid site and found the most stable proton position to form a $8.68^{\circ}$ angle with the Al-O-Si plane; this value compares more favor-ably to the $11.6^{\circ}$ angle calculated by Jeanvoine et al. [45]for the O2 site, and the $10^{\circ}$ angle found by Cook et al. [41]for ZSM-5. We again also found a second, much less stable, proton position for the O2 site. In conclusion, it is likely that there are two minima for a proton position at each acid site, though one of these proton positions is more energetically stable than the other.

### 3.2. Deprotonation energy and stability of acid sites

We next determined the deprotonation energies of each of the four possible acid sites corresponding to the single aluminum substituent, as shown in Fig. 4 and numbered O1-O4 according to the chabazite topology labeling [46]. In our labeling scheme, sites O2 and O3 are part of the large 8T ring, while sites O1 and O4 are part of the smaller6T ring. There have been several published studies aimed at understanding the properties of the zeolite acid sites and quantifying differences between the four oxygen acid sites[11,24,26,29,45,47-49].

![](./images/812342932785856514_5.jpg)

Fig. 3. Total energy (kJ/mol) vs constrained proton out-of-plane angle for chabazite with proton at O3.

Selected geometric parameters, including the O-H bond length and the Al-O-Si bond angle at each of the protonated acid sites, and energetic parameters, including proton affini- ties and O-H vibrational stretching frequencies, are shown in Table 1. We calculated all vibrational frequencies using the harmonic approximation from finite differences of first derivatives. Although it has been shown by Mihaleva et al. that anharmonic effects must be included for the most ac- curate comparison to experimental stretching frequencies, the relative ordering of the harmonic and anharmonic fun- damentals between the four acid sites is not changed [13]. The experimental O-H stretching frequencies on chabazite are 3603 and $3579 ~cm^{-1}$ at the O1 and O3 sites, respec tively [11]. A comparison of our calculated relative energies to other published studies is shown in Table 2.

![](./images/812342932785856514_6.jpg)

Fig. 4. Four nonequivalent oxygen acidic sites in chabazite.

Table 1 Selected geometric and energetic parameters at the four tetrahedral acid sites in chabazite (1 Al/unit cell)
| Acid site | Al-O-Si Bond angle (deg) | O-H bond length (Å) | Deprotonation energy (kJ/mol) | O-H vibrational frequency (cm⁻¹) |
|-----------|--------------------------|----------------------|--------------------------------|-----------------------------------|
| O1        | 129.8                    | 0.977                | 1178.7                         | 3578                              |
| O2        | 133.5                    | 0.979                | 1180.9                         | 3541                              |
| O3        | 130.9                    | 0.980                | 1174.6                         | 3514                              |
| O4        | 134.6                    | 0.980                | 1179.1                         | 3532                              |


<table>
<caption>Table 2 Comparison of relative deprotonation energies between different acid sites in chabazite (1 Al/unit cell), calculated by us and various researchers</caption>
<thead>
<tr>
<th></th>
<th colspan="4">Relative energies (kJ/mol) of acid sites</th>
</tr>
<tr>
<th></th>
<th>O1</th>
<th>O2</th>
<th>O3</th>
<th>O4</th>
</tr>
</thead>
<tbody>
<tr>
<td>This work</td>
<td>2.2</td>
<td>0</td>
<td>6.3</td>
<td>1.8</td>
</tr>
<tr>
<td>Shah et al. [24] (periodic)</td>
<td>0</td>
<td>6.8</td>
<td>3.9</td>
<td>8.6</td>
</tr>
<tr>
<td>Shah et al. [47] (periodic)</td>
<td>0</td>
<td>7.7</td>
<td>4.8</td>
<td>13.5</td>
</tr>
<tr>
<td>Haase et al. [26] (periodic)</td>
<td>0</td>
<td></td>
<td>9.5</td>
<td></td>
</tr>
<tr>
<td>Jeanvoine et al. [45] (periodic)</td>
<td>0</td>
<td>8.8</td>
<td>5.2</td>
<td>5.0</td>
</tr>
<tr>
<td>Brändle et al. [48] (embedded cluster)</td>
<td>0</td>
<td>17.0</td>
<td>12.9</td>
<td>12.5</td>
</tr>
<tr>
<td>Mihaleva et al. [29] (cluster, Gaussian98)</td>
<td>1.5</td>
<td>5.0</td>
<td>5.7</td>
<td>0</td>
</tr>
<tr>
<td>Mihaleva et al. [29] (cluster, DGauss)</td>
<td>0</td>
<td>1.7</td>
<td>2.8</td>
<td>0.8</td>
</tr>
<tr>
<td>Treesukol et al. [49] (embedded cluster)</td>
<td>0</td>
<td>15.8</td>
<td>16.7</td>
<td>15.9</td>
</tr>
<tr>
<td>Smith et al. [11] (exp)</td>
<td>*</td>
<td></td>
<td>*</td>
<td></td>
</tr>
</tbody>
</table>

The neutron diffraction results of Smith et al. [11] suggest that protons are observed only on O1 and O3. Although most of the other researchers find that the O1 site is the most stable, we found that the O2 site is the most stable. The difference between our results and those of other researchers is likely due to slight differences in methodology. We note that the difference in deprotonation energy between the O2 and O1 sites is only about 2 kJ/mol. Also, when we compare our results to those of the other researchers, we see no distinct trends in the stability of the other acid sites. Therefore, we take this result to imply that the four acid sites have approximately the same stability, within the accuracy of the calculations.

Also, we attribute the small differences in the magnitude and the order of the deprotonation energies among the results in Table 2 to differences in models and methodology. We note that the range of relative energies of the four acid sites is around 6–10 kJ/mol, which corresponds to an energy difference of $2k_{\text{B}}T$ at $400\,^{\circ}\text{C}$. We are using functional approximations to the exchange and correlation energies, and since the absolute accuracy of the energies calculated with DFT has been shown to be about 20–30 kJ/mol [35], we take 10 kJ/mol as a good estimate of the relative accuracy of the energies among the four acid sites. Other small sources of inaccuracy in the calculations may include the use of fixed unit cell lattice parameters instead of letting the system volume relax as well, and the incomplete basis sets used. Also, we note that the energy surface is likely to be highly corrugated so that there are many local minima. Current, state of the art geometry optimization methods (i.e., direct inversion of the iterative subspace, steepest descent, and preconditioned conjugate gradients) can only guarantee convergence to a local minimum. We showed in Section 3.1 that the difference in relative total energies between the local and the global minima is around 6.3 kJ/mol. Perhaps some of the differences in acid-site energies can be attributed to not fully optimizing the zeolite framework structures, especially if the PW91 functional is unable to adequately treat the negative charge of the chabazite anion in the calculation of the deprotonation energies.

We note that by just considering deprotonation of each unit cell, we are actually introducing a divergent Coulomb term in the lattice energy, which is an unphysical. This can be rectified by adding a uniform positive background charge to the deprotonated unit cell. Both Eichler et al. [50] and we compared the deprotonation energy for the removal of a single proton from a single unit cell and a double $(2\times1\times1)$ supercell, where only one active site is protonated per cell. The deprotonation energy changes by only 1.6 kJ/mol. There are also small errors introduced by the different structural relaxation when one or two acid sites are deprotonated in the $2\times1\times1$ supercell, but these should not affect our results appreciably.

We note that although it has been shown in the studies of both Smith et al. [11] and Vitale et al. [51] that the O1 and O3 sites are the only protonated sites in chabazite, based on our energetic studies the O2 and O4 sites seem to be the most stable. We cannot explain why only the O1 and O3 protons are observed experimentally, and we believe that factors outside of the scope of our calculations must be involved.

We conclude that the most likely explanation is that all four acid sites at a given aluminum substituent in chabazite have approximately the same deprotonation energy, and therefore are roughly homogeneous in acid strength.

### 3.3. Adsorption of bases

We then calculated the adsorption energies on chabazite for four bases: acetonitrile, methanol, ammonia, and pyridine. The weak bases acetonitrile and methanol were chosen because they are commonly used in hydrogenation reactions involving zeolites. Ammonia and pyridine were chosen because they are commonly used as base probes in temperature-programmed desorption, a widely used experimental method for characterizing zeolite acidity. We have illustrated the adsorption of these bases on O3-protonated chabazite in Fig. 5.

The gas-phase proton affinities of the four bases are given in Table 3. Ammonia and pyridine have much higher proton affinities than acetonitrile and methanol, and ammonia and pyridine are able to induce proton transfer from the chabazite framework.

The adsorption energies of bases on chabazite are given in Table 4, and a comparison of our results to the ranges reported in the literature from both calculated and experimental results is shown in Table 5 for methanol and ammonia adsorption. The adsorption energies of ammonia and pyridine are about 60 kJ/mol higher than those of acetonitrile and methanol; this suggests that higher gas-phase base proton affinities, and the corresponding proton-transfer reactions, result in more strongly bonded zeolite–base complexes. This trend was also seen by Biaglow et al. [4], who showed that the heats of adsorption of amines in H-ZSM-5 scaled with their gas-phase gas-phase affinities.

![](./images/812342932785856514_7.jpg)

Fig. 5. (a) Acetonitrile, (b) methanol, (c) ammonia, (d) pyridine adsorbed to chabazite with proton on O3.

Table 3
Calculated and literature values for proton affinities (kJ/mol) of base adsor-
bates used in this study

<table>
<thead>
<tr>
<th rowspan="2">Base</th>
<th colspan="3">Proton affinities (kJ/mol) of base adsorbate</th>
</tr>
<tr>
<th>This work</th>
<th>Aue and Bowers [65] (exp)</th>
<th>Error</th>
</tr>
</thead>
<tbody>
<tr>
<td>Acetonitrile</td>
<td>805.3</td>
<td>798.7</td>
<td>6.6 (0.8%)</td>
</tr>
<tr>
<td>Methanol</td>
<td>757.1</td>
<td>773.6</td>
<td>−16.5 (2.1%)</td>
</tr>
<tr>
<td>Ammonia</td>
<td>877.3</td>
<td>857.7</td>
<td>19.6 (2.3%)</td>
</tr>
<tr>
<td>Pyridine</td>
<td>957.8</td>
<td>922.2</td>
<td>35.6 (3.9%)</td>
</tr>
</tbody>
</table>

Table 4
Adsorption energies (kJ/mol) of bases on chabazite (1 Al/unit cell)

<table>
<thead>
<tr>
<th rowspan="2">Acid site</th>
<th colspan="4">Adsorption energies of bases (kJ/mol)</th>
</tr>
<tr>
<th>Acetonitrile</th>
<th>Methanol</th>
<th>Ammonia</th>
<th>Pyridine</th>
</tr>
</thead>
<tbody>
<tr>
<td>O1</td>
<td>82.7</td>
<td>94.0</td>
<td>149.3</td>
<td>153.6</td>
</tr>
<tr>
<td>O2</td>
<td>83.6</td>
<td>91.6</td>
<td>142.9</td>
<td>161.2</td>
</tr>
<tr>
<td>O3</td>
<td>69.7</td>
<td>91.7</td>
<td>144.5</td>
<td>153.5</td>
</tr>
<tr>
<td>O4</td>
<td>79.4</td>
<td>90.9</td>
<td>135.7</td>
<td>162.6</td>
</tr>
</tbody>
</table>

Table 5
Comparison of our calculated adsorption energies of methanol and ammo-
nia on chabazite (1 Al/unit cell) to those calculated or measured experimen-
tally by other researchers

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">Adsorption energy of bases (kJ/mol)</th>
</tr>
<tr>
<th>Methanol</th>
<th>Ammonia (kJ/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>This work</td>
<td>90.9–94.0</td>
<td>135.7–149.3</td>
</tr>
<tr>
<td>Gale et al. [21] (cluster)</td>
<td>63.5–79.8</td>
<td></td>
</tr>
<tr>
<td>Shah et al. [24] (periodic)</td>
<td>82</td>
<td></td>
</tr>
<tr>
<td>Haase et al. [26] (periodic)</td>
<td>93.6–94.1</td>
<td></td>
</tr>
<tr>
<td>Mihaleva et al. [29] (cluster)</td>
<td>96–105</td>
<td></td>
</tr>
<tr>
<td>Sauer and co-workers [17,48] (embedded cluster)</td>
<td></td>
<td>100–109</td>
</tr>
<tr>
<td>Truong and co-workers [66] (embedded cluster)</td>
<td></td>
<td>166–190</td>
</tr>
<tr>
<td>Messow et al. [67] (HZSM-5, exp)</td>
<td>63</td>
<td></td>
</tr>
<tr>
<td>Haase et al. [23] (HZSM-5, exp)</td>
<td>120</td>
<td></td>
</tr>
<tr>
<td>Dumesic and co-workers [15] (HZSM-5, exp)</td>
<td></td>
<td>150</td>
</tr>
<tr>
<td>Gorte and co-workers [16] (HZSM-5, exp)</td>
<td></td>
<td>150</td>
</tr>
<tr>
<td>Derouane and Chang [68] (HZSM-5, exp)</td>
<td></td>
<td>145</td>
</tr>
<tr>
<td>Joly and Perrard [69] (HY, exp)</td>
<td></td>
<td>125</td>
</tr>
</tbody>
</table>

The stability trend, in order from most stable to least stable, of the zeolite–base complexes is shown in the following:

acetonitrile, O2 > O1 > O4 > O3;

methanol, O1 > O3 > O2 > O4;

ammonia, O1 > O3 > O2 > O4;

pyridine, O4 > O2 > O1 > O3.
(3)

This suggests that geometric factors are important; the smaller bases, ammonia and methanol, are slightly more stable when situated in smaller channels and hence adsorbed to the O1 site, whereas the larger bases, acetonitrile and pyridine, prefer to be situated in the 8T ring and thus adsorbed to the O2 site. Derouane and co-workers [14] also proposed in a model for confinement effects that bases prefer to adsorb in the smallest pores that can accommodate them, in order to maximize their van der Waals interactions with the zeolite framework, and we do see a slight size dependence in our results. However, we do not see a similar trend among bases of similar strengths but different sizes, for example, acetonitrile and methanol. It is also important to note that the relative stabilities differ only by 10 kJ/mol, which is within the accuracy of the DFT calculations so most likely any trends are not significant (see Section 3.2) and the bases do not actually prefer one acid site over another, as demonstrated by ammonia TPD experiments [15,16].

We conclude that there is a definite correlation between base adsorption energies and gas-phase proton affinities, and there may be a correlation between base size and the preferred zeolite acid site for adsorption. We stress, however, that for a given base, the difference in adsorption energies between the four acid sites is very low.

### 3.4. Concentration of framework substituents

We now describe our studies of base adsorption on different chabazite models. The ratio of Si/Al in industrial chabazite is about 4.5 [18]. In our model system described previously, there is only one Al site per unit cell, giving a Si/Al ratio of 11. We want to determine how the base adsorption energy varies as a function of the concentration of Al substituents in the silicate framework. We therefore constructed three models with 2 Al/unit cell. The two aluminum atoms cannot be separated by only one oxygen atom by Loewenstein's rule [52], so there are three possible configurations for the two aluminum substituents around the 8T ring, as shown in Fig. 6; only the 8T ring was chosen for the location of the additional aluminum substituent in order to isolate the effect of the extra electronic charge from any steric effects. We designate these structures as "ortho," "meta," and "para," analogous to the nomenclature used for aromatic compounds. In all three cases, the O3 proton from Section 3.2 was chosen to be protonated to match that given in the original chabazite coordinates of Smith et al. [11], in order to have our 2 Al/unit cell models start from the same base structure as for the 1 Al/unit cell models and not propagate any errors in our geometry optimizations. We anticipate that the deprotonation energies on chabazite with 2 Al/unit

![](./images/812342932785856514_8.jpg)

Fig. 6. Chabazite with 2 Al/unit cell, with protons on: (a) O3 and O1 ("ortho"), (b) O3 and O2 ("meta"), and (c) O3 and O3 ("para").

<table>
<caption>Table 6 Deprotonation energies and O–H vibrational frequencies at the two acid sites in chabazite (2 Al/unit cell)</caption>
<thead>
<tr>
<th>2 Al configuration</th>
<th>Deprotonation energy (kJ/mol)</th>
<th>O–H vibrational frequency (cm⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>O3 and O1 (“ortho”)</td>
<td>1190.4 (O3)</td>
<td>3557</td>
</tr>
<tr>
<td></td>
<td>1176.0 (O1)</td>
<td>3542</td>
</tr>
<tr>
<td>O3 and O2 (“meta”)</td>
<td>1167.5 (O3)</td>
<td>3544</td>
</tr>
<tr>
<td></td>
<td>1153.5 (O2)</td>
<td>3581</td>
</tr>
<tr>
<td>O3 and O3 (“para”)</td>
<td>1188.5 (O3)</td>
<td>3576</td>
</tr>
<tr>
<td></td>
<td>1191.7 (O3)</td>
<td>3588</td>
</tr>
<tr>
<td>O3 only</td>
<td>1175</td>
<td>3514</td>
</tr>
</tbody>
</table>

cell and O1 as the protonated site should not be vastly different from those with O3 as the protonated site, since it seems that the acid sites in chabazite have roughly similar deprotonation energies, as seen in Section 3.2. The proton affinities and O–H vibrational frequencies for all three structures are shown in Table 6. We found that the ortho and para configurations, with their perfectly symmetric distribution of Al substituents around the 8T ring, are more stable than the meta configuration. Barbosa and van Santen also found that the ortho and para structures, with a $[ZnOZn]^{2+}$ cluster instead of two protons as the charge neutralizers, were more stable than the corresponding meta structure [53].

The adsorption energies of acetonitrile, methanol, ammonia, and pyridine on these three structures, as illustrated in Fig. 6, are shown in Table 7, and compared to the analogous base adsorption energies on chabazite with 1 Al/unit cell with the proton on O3 (henceforth referred to as “CHA”). For methanol, as shown in Fig. 7, we see a slight increase in adsorption energy when comparing ortho to meta to para; there does not seem to be a similar trend in the adsorption energies for acetonitrile. There may be small geometrical or steric factors that affect the methanol adsorption energy. We note that the methanol C–O bond does not lie in the plane of the two chabazite protons in ortho, but does lie in the plane in meta and para. In ortho, since the chabazite protons are only $3.29\ \text{Å}$ apart and in close proximity to the methanol proton, there may be some repulsive interactions that slightly destabilize the chabazite–methanol complex. By comparison, the chabazite protons are more than $4.0\ \text{Å}$ apart in the meta and para structures. We note that the two framework protons in ortho and para are roughly equidistant to the framework oxygen closest to the O–H and N–H groups of methanol and ammonia, respectively, so the symmetric structural topology and corresponding electronic density may help to stabilize the base. However, the extra strain in the ortho structural framework that arises from the Al atoms being in close proximity may work to slightly destabilize the base.

The adsorption energies of ammonia and pyridine on ortho and meta are similar in magnitude to the adsorption energies of ammonia and pyridine on our structure with 1 Al/unit cell, with ortho being slightly lower due to steric effects. This was also seen by Meusinger and Corma [54], who observed that acid strength, as measured by proton-transfer

![](./images/812342932785856514_9.jpg)

Fig. 7. Methanol adsorbed on chabazite with 2 Al/unit cell, with protons on: (a) O3 and O1 (“ortho”), (b) O3 and O2 (“meta”), and (c) O3 and O3 (“para”).

### Table 7
Adsorption energies of bases on chabazite with 1 Al/unit cell and 2 Al/unit cell

<table>
  <thead>
    <tr>
      <th rowspan="2">2 Al configuration</th>
      <th colspan="4">Base adsorption energy (kJ/mol)</th>
    </tr>
    <tr>
      <th>Acetonitrile</th>
      <th>Methanol</th>
      <th>Ammonia</th>
      <th>Pyridine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O3 and O1 ("ortho")</td>
      <td>72.3</td>
      <td>80.1</td>
      <td>140.9</td>
      <td>150.4</td>
    </tr>
    <tr>
      <td>O3 and O2 ("meta")</td>
      <td>64.0</td>
      <td>88.0</td>
      <td>144.1</td>
      <td>152.2</td>
    </tr>
    <tr>
      <td>O3 and O3 ("para")</td>
      <td>69.1</td>
      <td>97.5</td>
      <td>125.6</td>
      <td>147.4</td>
    </tr>
    <tr>
      <td>O3 only</td>
      <td>69.7</td>
      <td>91.7</td>
      <td>144.5</td>
      <td>153.5</td>
    </tr>
  </tbody>
</table>

### Table 8
Nonacidic chabazite proton out-of-plane angle with and without ammonia adsorbed to chabazite framework

<table>
  <thead>
    <tr>
      <th rowspan="2">2 Al configuration</th>
      <th colspan="2">Out-of-plane angle (deg)</th>
    </tr>
    <tr>
      <th>CHA only</th>
      <th>CHA-NH₃</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O3 and O1 ("ortho")</td>
      <td>28.7</td>
      <td>−52.0</td>
    </tr>
    <tr>
      <td>O3 and O2 ("meta")</td>
      <td>23.3</td>
      <td>−49.8</td>
    </tr>
    <tr>
      <td>O3 and O3 ("para")</td>
      <td>−11.9</td>
      <td>−43.1</td>
    </tr>
  </tbody>
</table>

reactions, decreased for zeolites with two $AlO_4$ tetrahedra separated by only one $SiO_4$ tetrahedra, which is similar to our ortho case. Also, for both these bases, the adsorption energy on para is slightly lower. As shown in Fig. 8 and Table 8, the optimized nonacidic proton positions are almost identical for the three structures, with out-of-plane angles ranging from $-43.1$ to $-52.0^\circ$. During the process of ammonia adsorption, the nonacidic proton distorts to minimize the Coulombic repulsion with the ammonium ion. Hence the optimized structures of the acid site containing the nonacidic proton are roughly identical for all three structures, yet when the base is present, the framework distortion leads to some variation in the base adsorption energies.

We also note that the range of adsorption energies in Table 7 is below 10 kJ/mol for both large-sized bases acetonitrile and pyridine, whereas the range of adsorption energies is between 15 and 20 kJ/mol for the smaller bases methanol and ammonia. In Section 3.3, we saw that confinement effects are important, so the smaller bases may be affected by the positioning of the acid site protons around the 8T ring, and thus the strength of the hydrogen bonds stabilizing the zeolite–base complex.

We then performed an ELF visualization of the optimized ortho, meta, and para structures with ammonia. In Fig. 9, the ELF lobe on the acidic oxygen is smaller in para than in either ortho or meta. This indicates a slightly reduced acid strength for para that could explain the slightly lower ammonia adsorption energy.

Experimentally, it has been shown that in high silica zeolites (Si/Al > 10) such as ZSM-5, catalytic activity, as measured by the rate of hexane cracking, increases linearly with Al content [55]; in essence, the catalytic activity per acid site remains constant. Even for low silica zeolites such as faujasite (Si/Al > 4.5), the activity per Al atom is constant [56]. Only for very low silica zeolites does the specific activity increase with decreasing aluminum content. In our

![](./images/812342932785856514_10.jpg)

Fig. 8. Ammonia adsorbed on chabazite with 2 Al/unit cell, with protons on: (a) O3 and O1 ("ortho"), (b) O3 and O2 ("meta"), and (c) O3 and O3 ("para").

![](./images/812342932785856514_11.jpg)

Fig. 9. ELF isosurfaces ($\chi=0.87$) on O3 proton of chabazite with 2 Al/unit cell, with protons on: (a) O3 and O1 ("ortho"), (b) O3 and O2 ("meta"), and (c) O3 and O3 ("para").

model chabazite systems, we considered Si/Al ratios of 11 and 5. We used methanol and ammonia to probe only one acid site, although there were two acid sites in the framework. Although our results suggest that the strength of the acid sites in chabazite, as measured by the energies of adsorption of small bases, is also constant amidst changes in Al content in the framework, we stress that acidity is not necessarily a measure of catalytic activity.

We conclude that although there are some variations, roughly 5–17 kJ/mol, in the adsorption energies on ortho, meta, and para, for all bases, there are no consistent trends that seem to be universally applicable, and that the presence of additional aluminum substituents does not significantly affect the strength of any individual acid site.

### 3.5. Framework defects

Finally, we were interested in how the presence of zeolite framework defects would affect the strength of acid sites. Both the natural and synthetic environments of chabazite contain significant amounts of water, which is either physisorbed or chemisorbed to the framework [57]. During the synthesis of chabazite, two nonbridging siloxy ($\equiv$Si–O–) species associated with the adamantane templates [18] can undergo calcination and acid treatment to form a vicinal hydroxyl group pair ($\equiv$Si–OH$\cdots$HO–Si$\equiv$). Upon thermal decomposition and ion exchange, the vicinal silanols are dehydrated to form an Si–O–Si linkage. The reverse can also happen, whereby the Si–O–Si linkage is hydrolyzed to form two vicinal silanol groups [58].

We performed geometry optimization calculations on chabazite with a vicinal silanol defect near the acid site, as shown in Fig. 10. In setting up the silanol defect model, we replaced an $\equiv$Si–O–Si$\equiv$ linkage with an $\equiv$Si–OH$\cdots$HO–Si$\equiv$ unit, essentially hydrolyzing an Si–O bond. The hydrolysis reaction is important because zeolites are commonly used as molecular sieves, so it is not unreasonable to assume that water molecules are present. We note that there are several possible configurations for the silanol defect, but we chose this one because the energy of formation was only 5.78 kJ/mol, making it likely to occur in a zeolite system. The heat of formation, which we calculated with the PW91 functional, is comparable to the value of 8 kJ/mol calculated using the B3-LYP functional [59], although Pascale et al. did

![](./images/812342932785856514_12.jpg)

Fig. 10. Chabazite with silanol framework defect near acid site.

<table>
<caption>Table 9 Deprotonation energies and O–H vibrational frequencies at the acid site</caption>
<thead>
<tr>
<th>CHA with</th>
<th>Deprotonation energy (kJ/mol)</th>
<th>O–H vibrational frequency (cm<sup>−1</sup>)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silanol defect</td>
<td>1186.8</td>
<td>3522</td>
</tr>
<tr>
<td>No defect</td>
<td>1180.9</td>
<td>3514</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 10 Methanol and ammonia adsorption energies (kJ/mol) on chabazite (1 Al/unit cell) with and without silanol defect</caption>
<thead>
<tr>
<th rowspan="2">CHA with</th>
<th colspan="2">Base adsorption energy (kJ/mol)</th>
</tr>
<tr>
<th>Methanol</th>
<th>Ammonia</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silanol defect</td>
<td>88.2</td>
<td>129.0</td>
</tr>
<tr>
<td>No defect</td>
<td>91.7</td>
<td>144.5</td>
</tr>
</tbody>
</table>

not have an Al substituent in their chabazite unit cell. For comparison, the heat of formation for a hydrogarnet defect, where four hydrogen atoms bonded to four oxygen atoms substitute for a tetrahedral Si atom, is about 54 kJ/mol [59]. Both Pascale et al. and we note that the BLYP functional tends to give Si–O and O–H bonds that are too long, which is why we chose to use the PW91 functional in all of our calculations for this study.

The proton affinities and O–H vibrational frequencies at the acid site of chabazite with and without a silanol defect are shown in Table 9; the adsorption energies of methanol and ammonia at the acid site are shown in Table 10. It seems that the presence of the silanol defect results in slight de- creases in both the methanol and the ammonia adsorption en- ergies. The chabazite O–H bond is not weakened much in the presence of the silanol defect; the O–H vibrational frequen- cies (3522 cm<sup>−1</sup> with the silanol defect versus 3514 cm<sup>−1</sup> with no defect) and bond lengths (0.980 Å in both cases) are roughly the same.

The ELF isosurfaces shed some light on what is happen- ing at the acid site. In Fig. 11, the ELF lobe at the acid site oxygen is smaller for chabazite with the silanol defect than for the defect-free chabazite. A possible explanation is that the substitution of H for Si at the silanol defect site results in a greater partial positive charge at the defect site. Some electron density is then shifted in the direction of the charge gradient, away from the acid site to the defect site. We con- clude that the presence of a vicinal silanol framework defect does not affect appreciably the frequency of vibration of the O–H group, nor the heat of adsorption of small bases at the acid site.

### 3.6. Implications for solid acidity scale

Based on our results, the four Brønsted sites corre- sponding to the Al substituent have roughly the same acid strength. It is difficult, given our results, to determine which of the characterization methods employed—base adsorp- tion energies, acid-site deprotonation energies, or structural parameters—is the best to characterize acid-site strength.

![](./images/812342932785856514_13.jpg)

Fig. 11. ELF isosurfaces ($\chi = 0.87$) for chabazite (a) with silanol defect, (b) without silanol defect.

However, the deprotonation energy is widely thought to be the best [12]. Our results also suggest that small bases have similar adsorption energies on chabazite with 1 Al/unit cell and 2 Al/unit cell, and with a vicinal silanol framework de- fect. Therefore, neither the number of Al substituents in the zeolite unit cell nor the presence of structural defects near the acid site significantly affect the strength of the individual acid sites in chabazite.

We emphasize that our results do not imply that the O–H groups on different zeolites have the same strength, since we only considered chabazite in this study. For example, Freude et al. [60] found that the enhanced catalytic activity of mordenite relative to zeolite Y is due to the higher acid strength of the O–H groups. They did note that the acidity should be constant for zeolites with Si/Al ratios greater than 10. Sharma et al. [15] found that the enthalpies of adsorp- tion of ammonia and pyridine on mordenite are higher than the corresponding enthalpies on ZSM-5. Mosqueda-Jiménez et al. [61] found that both the strength of the acid sites in Ni-ZSM-5, Ni-MOR, and Ni-MCM-22, as measured by the shift of the O–H vibrational frequency upon adsorption of benzene, and the concentration of the acid sites were directly correlated to the conversion of NO with propane.

It is also important to note that enhanced “activity” is not necessarily correlated to enhanced “acidity.” For exam- ple, there is no proven correlation between enhanced cat-

<table>
<caption>Table 11
Intrinsic acidity [6] for the four acid sites in chabazite (1 Al/unit cell)</caption>
<thead>
<tr>
<th>Acid site</th>
<th>O–H bond length (Å)</th>
<th>O–H vibrational frequency (cm⁻¹)</th>
<th>Intrinsic acidity</th>
</tr>
</thead>
<tbody>
<tr>
<td>O1</td>
<td>0.977</td>
<td>3578</td>
<td>$2.73×10^{-12}$</td>
</tr>
<tr>
<td>O2</td>
<td>0.979</td>
<td>3541</td>
<td>$2.77×10^{-12}$</td>
</tr>
<tr>
<td>O3</td>
<td>0.980</td>
<td>3514</td>
<td>$2.79×10^{-12}$</td>
</tr>
<tr>
<td>O4</td>
<td>0.980</td>
<td>3532</td>
<td>$2.77×10^{-12}$</td>
</tr>
</tbody>
</table>

alytic activity and decreased proton affinity or changes in the equilibrium constant for proton donation to a base [19]. Several experimental studies seem to support this statement. Brunner et al. [62] showed that the magnitude of $^1$H NMR chemical shifts and vibrational frequencies of bridging hy- droxyl groups do not change upon hydrothermal treatment, even though enhanced activity of $n$-hexane cracking was ob- served. Biaglow et al. [63] found that the decomposition temperature of isopropylamine is the same on SAPO-5 and H-ZSM-5, and does not appear to be sensitive to the strengthof the acid sites, since the strength of the sites in SAPO-5 is assumed to be intermediate between H-[Fe]-ZSM-5 and H-[Al]-ZSM-5 as measured by the materials' ability to pro- tonate propene. Parrillo and Gorte [16] showed that the rate of proton transfer is not correlated to the rate of alkane crack- ing since they occur at significantly different temperatures. Babitz et al. [64] performed solid-state NMR experiments showing that either the activation energy for hexane crack- ing is insensitive to differences in acid site strength or there are no differences in acid strength among ZSM-5, morden- ite, and Y zeolites.

Soscún et al. [6] recently defined a possible acidity scale in terms of a quantity described as the "intrinsic acidity" of the O–H groups. The intrinsic acidity is defined as the ratio between the O–H distance and the frequency of the O– H vibration mode. Soscún et al. showed that there exists a linear correlation between the intrinsic acidity and the total charge; however, all of the calculations were performed on cluster models of zeolites. We calculated the intrinsic acidity on our periodic models, as shown in Table 11. We find that the intrinsic acidity does not correlate with our calculated adsorption energies, but the small differences in magnitudebetween the calculated intrinsic acidities (roughly 1.66%) shows that all four acid sites do have approximately the same acidity. Of course, the validity and usefulness of the intrinsic acidity factor need to be further investigated.

## 4. Conclusions

We have performed a characterization via DFT and a topological visualization of the acid sites in chabazite with varying framework defects, including multiple Al sub- stituents in the 8T ring and a vicinal silanol defect near the acid site. We confirmed, using both ELF visualization and constrained geometry optimizations, that there are two min- ima for proton positions on the oxygens at the acid site.

Our results also show that the four acidic oxygens at the aluminum T site all have roughly the same deprotonation en- ergy, which is not strictly correlated to the O–H bond length or stretch vibrational frequency. Furthermore, we found that the adsorption energy of various bases at each acid-site oxy- gen is roughly the same and correlates well only with the gas-phase proton affinity of the base. These results reinforce the conclusion that the construction of a universal scale for quantifying zeolite acidity is likely to be problematic. Also, the deprotonation energies and base adsorption energies are not significantly changed with the presence of additional aluminum substituents in the zeolite framework, nor with silanol framework defects near the acid site.

## Acknowledgments

We thank the National Science Foundation for financial support in the form of a Graduate Research Fellowship and Grant CTS-9984301, and the National Center for Supercom- puting Applications for computing time.

## References

[1] R.J. Gorte, Catal. Lett. 62 (1999) 1.
[2] S. Damoun, W. Langenaeker, P. Geerlings, J. Phys. Chem. A 101(1997) 6951.
[3] V.B. Kazansky, A.I. Serykh, V. Semmer-Herledan, J. Fraissard, Phys. Chem. Chem. Phys. 5 (2003) 966.
[4] A.I. Biaglow, R.J. Gorte, G.T. Kokotailo, D. White, J. Catal. 148(1994) 779.
[5] M. Sierka, J. Sauer, J. Phys. Chem. B 105 (2001) 1603.
[6] H. Soscún, O. Castellano, J. Hernández, A. Hinchliffe, Int. J. Quant. Chem. 82 (2001) 143.
[7] L.P. Hammett, A.J. Deyrup, J. Am. Chem. Soc. 54 (1932) 2721.
[8] D. Fărcașiu, A. Ghenciu, Prog. Nucl. Magn. Reson. Spectrosc. 29(1996) 129.
[9] J.B. Nicholas, J.F. Haw, L.W. Beck, T.R. Krawietz, D.B. Ferguson, J. Am. Chem. Soc. 117 (1995) 12350.
[10] J.F. Haw, Phys. Chem. Chem. Phys. 4 (2002) 5431.
[11] L.J. Smith, A. Davidson, A.K. Cheetham, Catal. Lett. 49 (1997) 143.
[12] M. Sierka, U. Eichler, J. Datka, J. Sauer, J. Phys. Chem. B 102 (1998)6397.
[13] V.V. Mihaleva, R.A. van Santen, A.P.J. Jansen, J. Chem. Phys. 119(2003) 13,053.
[14] E.G. Derouane, in: D. Barthomeuf, E.G. Derouane, W. Hölderich(Eds.), Guidelines for Mastering the Properties of Molecular Sieves, vol. 221, Plenum, New York, 1990, pp. 225–239.
[15] S.B. Sharma, B. Meyeres, D. Chen, J. Miller, J.A. Dumesic, Appl. Catal. A 102 (1993) 253.
[16] D.J. Parrillo, R.J. Gorte, J. Phys. Chem. 97 (1993) 8786.
[17] M. Brändle, J. Sauer, J. Am. Chem. Soc. 120 (1998) 1556.
[18] L.-T. Yuen, S.I. Zones, T.V. Harris, E.J. Gallegos, A. Auroux, Micro- por. Mater. 2 (1994) 105.
[19] W.E. Farneth, R.J. Gorte, Chem. Rev. 95 (1995) 615.
[20] E.L. Meijer, R.A. van Santen, A.P.J. Jansen, J. Phys. Chem. 100 (1996)9282.
[21] J.D. Gale, C.R.A. Catlow, J.R. Carruthers, Chem. Phys. Lett. 216(1993) 155.
[22] F. Haase, J. Sauer, J. Phys. Chem. 98 (1994) 3083.
[23] F. Haase, J. Sauer, J. Am. Chem. Soc. 117 (1995) 3780.

[24] R. Shah, M.C. Payne, J.D. Gale, J. Phys. Chem. 100 (1996) 11,688.

[25] S.R. Blaszkowski, R.A. van Santen, Stud. Surf. Sci. Catal. 105 (1997) 1707-1714.

[26] F. Haase, J. Sauer, J. Hutter, Chem. Phys. Lett. 266 (1997) 397.

[27] P.E. Sinclair, C.R.A. Catlow, J. Chem. Soc., Faraday Trans. 93 (1997) 333.

[28] R.A. van Santen, Catal. Today 38 (1997) 377.

[29] V.V. Mihaleva, R.A. van Santen, A.P.J. Jansen, J. Phys. Chem. B 105 (2001) 6874.

[30] P. Hohenberg, W. Kohn, Phys. Rev. B 136 (1964) B864.

[31] W. Kohn, L.J. Sham, Phys. Rev. A 140 (1965) A1133.

[32] R.G. Parr, W. Yang, Density Functional Theory of Atoms and Mole- cules, Oxford Univ. Press, New York, 1989.

[33] J.P. Perdew, in: P. Ziesche, H. Eschrig (Eds.), Electronic Structure of Solids '91, Akademie Verlag, Berlin, 1991, pp. 11-20.

[34] N. Troullier, J.L. Martins, Phys. Rev. B 43 (1991) 1993.

[35] M. Neurock, J. Catal. 216 (2003) 73.

[36] S. Tsuzuki, H.P. Lüthi, J. Chem. Phys. 114 (2001) 3949.

[37] O. Couronne, Y. Ellinger, Chem. Phys. Lett. 306 (1999) 71.

[38] J. Hutter, A. Alavi, T. Deutsch, M. Bernasconi, S. Goedecker, D. Marx, M. Tuckerman, M. Parrinello, CPMD Version 3.3 (1995-1999), Max- Planck-Institut für Festkörperforschung and IBM Zurich Research Laboratory.

[39] R. Shah, M.C. Payne, M.-H. Lee, J.D. Gale, Science 271 (1996) 1395.

[40] N. Govind, J. Andzelm, K. Reindel, G. Fitzgerald, Int. J. Mol. Sci. 3 (2002) 423.

[41] S.J. Cook, A.K. Chakraborty, A.T. Bell, D.N. Theodorou, J. Phys. Chem. 97 (1993) 6679.

[42] J.M. Kobe, T.J. Gluszak, J.A. Dumesic, T.W. Root, J. Phys. Chem. 99 (1995) 5485.

[43] A.D. Becke, K.E. Edgecombe, J. Chem. Phys. 92 (1990) 5397.

[44] B.L. Trout, M. Parrinello, J. Phys. Chem. B 103 (1999) 7340.

[45] Y. Jeanvoine, J.G. Àngyán, G. Kresse, J. Hafner, J. Phys. Chem. B 102 (1998) 5573.

[46] M. Calligaris, G. Nardin, L. Randaccio, P.C. Chiaramonti, Acta Crys- tallogr. B 38 (1982) 602.

[47] R. Shah, M.C. Payne, J.D. Gale, Int. J. Quant. Chem. 61 (1997) 393.

[48] M. Brändle, J. Sauer, R. Dovesi, N.M. Harrison, J. Chem. Phys. 109 (1998) 10,379.

[49] P. Treesukol, J.P. Lewis, J. Limtrakul, T.N. Truong, Chem. Phys. Lett. 350 (2001) 128.

[50] U. Eichler, M. Brändle, J. Sauer, J. Phys. Chem. B 101 (1997) 10,035.

[51] G. Vitale, L.M. Bull, B.M. Powell, A.K. Cheetham, J. Chem. Soc., Chem. Commun. 22 (1995) 2253.

[52] W. Loewenstein, Am. Miner. 39 (1954) 92.

[53] L.A.M.M. Barbosa, R.A. van Santen, J. Phys. Chem. B 107 (2003) 4532.

[54] J. Meusinger, A. Corma, J. Catal. 159 (1996) 353.

[55] W.O. Haag, N.Y. Chen, in: L.L. Hegedus (Ed.), Catalyst Design: Progress and Perspectives, Wiley, New York, 1987, pp. 163-212.

[56] S.J. DeCanio, J.R. Sohn, P.O. Fritz, J.H. Lunsford, J. Catal. 101 (1986) 132.

[57] A.A. Sokol, C.R.A. Catlow, J.M. Garcés, A. Kuperman, J. Phys. Chem. B 106 (2002) 6163.

[58] H. Koller, R.F. Lobo, S.L. Burkett, M.E. Davis, J. Phys. Chem. 99 (1995) 12,588.

[59] F. Pascale, P. Ugliengo, B. Civalleri, R. Orlando, P. D'Arco, R. Dovesi, J. Chem. Phys. 117 (2002) 5337.

[60] D. Freude, M. Hunger, H. Pfeifer, W. Schwieger, Chem. Phys. Lett. 128 (1986) 62.

[61] B.I. Mosqueda-Jiménez, A. Jentys, K. Seshan, J.A. Lercher, J. Ca- tal. 218 (2003) 348.

[62] E. Brunner, H. Ernst, D. Freude, T. Fröhlich, M. Hunger, H. Pfeifer, J. Catal. 127 (1991) 34.

[63] A.I. Biaglow, A.T. Adamo, G.T. Kokotailo, R.J. Gorte, J. Catal. 131 (1991) 252.

[64] S.M. Babitz, B.A. Williams, J.T. Miller, R.Q. Snurr, W.O. Haag, H.H. Kung, Appl. Catal. A 179 (1999) 71.

[65] D.H. Aue, M.T. Bowers, in: M.T. Bowers (Ed.), Gas Phase Ion Chem- istry, vol. 2, Academic Press, New York, 1979, pp. 2-52, chap. 9.

[66] J.M. Vollmer, E.V. Stefanovich, T.N. Truong, J. Phys. Chem. B 103 (1999) 9415.

[67] U. Messow, K. Quitzsch, H. Herden, Zeolites 4 (1984) 255.

[68] E.G. Derouane, C.D. Chang, Micropor. Mesopor. Mater. 35-36 (2000) 425.

[69] J.-P. Joly, A. Perrard, Langmuir 17 (2001) 1538.