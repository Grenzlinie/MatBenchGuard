# Ab initio tensile tests of grain boundaries in the fcc crystals of Ni and Co with segregated $sp$-impurities

M. Černý $^{a,b,c,*}$, P. Šesták $^{a,b}$, P. Řehák $^{a,b,c,d}$, M. Všianská $^{d,a}$, M. Šob $^{d,a,e}$

$^{a}$ Institute of Physics of Materials, Academy of Sciences of the Czech Republic, Žižkova 22, CZ-616 62 Brno, Czech Republic
$^{b}$ Central European Institute of Technology, Brno University of Technology, Technická 10, CZ-616 69 Brno, Czech Republic
$^{c}$ Faculty of Mechanical Engineering, Brno University of Technology, Technická 2, CZ-616 69 Brno, Czech Republic
$^{d}$ Central European Institute of Technology, Masaryk University, Kamenice 5, CZ-625 00 Brno, Czech Republic
$^{e}$ Department of Chemistry, Faculty of Science, Masaryk University, Kotlářská 2, CZ-611 37 Brno, Czech Republic

---

## ARTICLE INFO

**Article history:**
Received 27 January 2016
Received in revised form
19 May 2016
Accepted 20 May 2016
Available online 24 May 2016

**Keywords:**
Theoretical strength
Computational tensile test
Grain boundary embrittlement
Ab initio calculations

---

## ABSTRACT

Models of $\Sigma5(210)$ grain boundaries in crystals of fcc Ni and fcc Co with segregated $sp$-impurities (Al, Si, P, S, Ga, Ge, As, Se, In, Sn, Sb, and Te) have been subjected to ab initio computational tensile tests. Two models of deformation (rigid grain shift and uniaxial loading) have been considered and their results have been compared. The results reveal striking differences in predictions from the models. Poisson contraction included in the model of uniaxial loading remarkably reduces the computed strength values but, unlike the rigid grain shift, predicts an enhancement of the grain boundary strength due to the presence of impurities (particularly those segregated in interstitial positions). These different predictions are discussed in terms of the effect of transverse stresses on the computed strength values.

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Mechanical properties of materials are predominantly governed by defects they contain. Since majority of engineering materials are polycrystals, grain boundaries (GBs) belong to the most important defects affecting their macroscopic mechanical characteristics. As it has been observed in many materials, impurity atoms tend to segregate at GBs due to an excess volume in the GB region and a large variety of available sites. Their presence at GB can considerably enhance or reduce GB cohesion. For this reason, remarkable attention (experimental as well as theoretical) has been paid to this effect in the past. In magnetic materials, segregated impurities can also change the magnetic moment of atoms in the vicinity of GB plane, which can even increase the impact on mechanical stability of the system. Many theoretical studies have been devoted to GBs in bcc Fe and fcc Ni [1–6]. On the other hand, less attention has been paid to GBs in Co [7].

Simulated tensile tests are widely used for investigation of cleavage properties of GBs. Former studies [1,8] often employed a model of GB cleavage by increasing distance of rigid grains (blocks of atoms) at defined cleavage plane (at GB). In such a model of GB fracture, the tensile strain is localized between two atomic planes that represent two new surfaces created by the cleavage. This is the computationally simplest model which, however, can supply useful information on the fracture characteristics and often is referred to as rigid grain displacement or rigid grain shift [9]. In order to optimize the structure, at least partially, some studies [5,6] included optimization of atomic positions. Relaxation of the transverse stresses (i.e. allowing for the Poisson contraction) has mostly been disregarded due to related computational difficulties (high computational demands and problematic convergence [2]). Only few computational tensile tests controlling also the stress tensor have been performed. Namely, the Car-Parrinello molecular dynamics was employed by Tomar et al. for calculations of strength of GBs in tungsten [10] and SiC [11]. These studies, however, did not deal directly with the effect of constrained optimization and restricted transverse contractions. Nevertheless, it was reported in other studies that neglecting the Poisson contraction can significantly affect results of simulated tensile tests on single crystals [12] as well as on GBs [2].

The aim of this paper is to compare the effect of impurities segregated at grain boundaries in fcc Ni and Co on the GB cohesion for a series of $sp$-elements. The effect is studied by computational tensile tests using two distinct models of GB deformation (with and without the Poisson contraction). Ground-state structure of a bulk cobalt (at 0 K) is hcp. It has been known for a long time, however, that, at elevated temperatures (well below the Curie temperature), its structure depends on the grain size [13]. When the grain size is sufficiently small, the fcc structure can also be observed. It was experimentally confirmed [14] that ball milling

---

*Corresponding author.
E-mail address: cerny.m@fme.vutbr.cz (M. Černý).

http://dx.doi.org/10.1016/j.msea.2016.05.083
0921-5093/© 2016 Elsevier B.V. All rights reserved.

![](./images/814520262555860993_1.jpg)
![](./images/814520262555860993_2.jpg)
![](./images/814520262555860993_3.jpg)

can produce Co stable in the fcc structure at room temperature. Considering both metals in their fcc phases gives us the opportunity to compare the effect of impurities at the same GBs in two crystals with different electronic structures (and magnetic moments of different magnitudes).

## 2. Computational details
The computational supercell used for the present calculations is illustrated in Fig. 1. The displayed arrangement of atoms corresponds to a model of the $\Sigma5(210)$ GB in fcc crystal with impurity atoms segregated in interstitial (Fig. 1 (a,c) and substitutional (Fig.1(b)) positions at GB. Geometry and the optimized parameters of the cell for Ni (corresponding to the ground state) are same as those used by Všianská and Šob in their calculations of structure and magnetism at the GB [3,4]. The ground-state geometries for fcc Co supercells were similarly determined in Ref. [7]. In the present simulated tensile tests we consider only the geometries that correspond to the predicted preferential segregation sites (i.e., Al, Ga, In, Sn, Sb, and Te are in substitutional positions, Si, P, S, Ge, As, and Se are in interstitial positions).

Tensile test is performed along an axis perpendicular to the GB plane. First considered model of tensile test conforms to the rigid grain shift (RGS). According to this model, vertical coordinates of all atoms in the upper half of the supercell in Fig. 1 are increased by the same magnitude of displacement without any relaxations of stresses or forces acting on individual atoms.

The other model considered in this work is optimized uniaxial loading (OUL). In this case, we consider also Poisson contraction of the supercell and each increment of axial strain is followed by an optimization loop consisting of repeated optimization of transverse cell dimensions (relaxation of lateral stresses) and subsequent relaxation of forces acting on individual atoms within the cell.

In order to follow a standard engineering definition, the strain is defined using the length $c$ of the supercell measured along the loading axis

$$
\varepsilon = \frac{c}{c_0} - 1
$$

with $c_0$ being the equilibrium length that corresponds to the optimized supercell which was determined individually for each GB model.

For the electronic structure calculations, we employed the first-principles code VASP [15,16] with the projector-augmented waves (PAW) potentials as supplied with the code [17]. The energy cut-off for plane waves was set to 450 eV. Sampling of the Brillouin zone was done using the $\Gamma$-centered mesh with $6 \times 2 \times 14$ $k$-points. The total energy was converged to lower its differences in two subsequent steps of self-consistent cycle below $1 \times 10^{-7}$ eV. Optimization of atomic positions within the supercell (OUL model) was performed using the internal VASP procedure and was finished when all the residual forces were lower than $9$ meV/Å. For optimization of the cell shape we used our own external procedure that cooperated with the VASP code via reading its output files and writing new structure files. The transverse stresses were relaxed below 0.10 GPa. In all present calculations, ferromagnetic ordering in Ni and Co was included via spin polarization.

## 3. Results
### 3.1. Bulk crystals and clean GBs
In the case of a bulk crystal, the OUL model must yield same results for simulation cells equivalent to both the primitive cells and the supercells of a size comparable to those described in Fig. 1. Therefore, in order to save computational resources, we simulated the uniaxial loading using the primitive fcc cells. For the RGS model, however, we constructed and fully optimized a computational supercell containing ten $\{012\}$ planes of fcc lattice. The obtained equilibrium lattice parameter of $3.517$ Å for fcc Ni agrees well with the value of $3.52$ Å obtained in previous calculations

![](./images/814520262555860993_4.jpg)

Fig. 1. Computational setup for the calculation of the $\Sigma5(210)$ GB with (a) interstitially and (b) substitutionally segregated impurities. (c) Top view of the computational cell with impurities in interstitial positions. The cell dimensions are approximately $7.8 \times 24 \times 3.5$ Å.

![](./images/814520262555860993_5.jpg)

Fig. 2. The stress-strain curves computed using rigid grain shift (RGS) and optimized uniaxial loading (OUL) for bulk fcc crystals (solid symbols) of Ni and Co compared with results calculated for clean $\Sigma 5(210)$ GB (open symbols) in both crystals.

using a primitive cell [18] and also measured experimentally [19]. The magnetic moment per atom of $0.64\,\mu_{\text{B}}$ is slightly higher than the values $0.62\,\mu_{\text{B}}$ and $0.606\,\mu_{\text{B}}$ from previous calculations [18] and from experiments [19], respectively. The values of $3.515\,\text{\AA}$ and $1.65\,\mu_{\text{B}}$ for fcc Co also agree well with those of $3.52\,\text{\AA}$ and $1.64\,\mu_{\text{B}}$ obtained in former calculations [20].

Results of the simulated tensile tests obtained using both considered models for bulk Ni and Co as well as for clean GBs are displayed in Fig. 2 as the stress-strain curves. The stress maxima $\sigma_{\text{max}}$ exhibited by these curves are considered to be the theoretical tensile strengths (or, more correctly, the cleavage stresses). Due to the localization of strain between two atomic planes, the critical strains related to the stress maxima in RGS model are lower than those obtained within the OUL model. This is particularly apparent for the results of calculated tensile tests on cells containing GB. The $\sigma_{\text{max}}$ values calculated using RGS are evidently higher than those from OUL. This clearly shows the effect of structure optimization (particularly relaxation of the transverse stresses) on the calculated cleavage stress in atomistic simulations. As it has been reported formerly for a series of fcc and bcc crystals [21], omitting the Poisson contraction induces tensile transverse stresses that usually increase the tensile strength. Therefore, the present results seem to be consistent with those former findings.

Regardless of the computational model, the $\sigma_{\text{max}}$ values computed for the clean $\Sigma 5(210)$ GB are lower than those computed for bulk crystals which is in agreement with the expected effect of such a plane defect in the crystal lattice. The values calculated for bulk and clean GB in fcc Ni using RGS (29.3 GPa and 25.3 GPa, respectively) seem to be in a reasonable agreement with the values of about 30 GPa and 26 GPa formerly computed by Yamaguchi et al. [1] with neglecting magnetism in Ni. Although the present result for a clean GB was computed for ferromagnetic ordering of spins, it agrees better with the nonmagnetic results of Yamaguchi et al. [1] than with those computed by Schusteritsch and Kaxiras [5] (20.9 GPa) or Liu et al. [6] (20.3 GPa) who considered magnetism but optimized atomic positions in their computational supercells. This demonstrates that the choice of a computational model has a more significant effect than considering or neglecting magnetism in Ni.

![](./images/814520262555860993_6.jpg)

Fig. 3. The maximum tensile stress values $\sigma_{\text{max}}$ calculated using the rigid grain shift (RGS) for $\Sigma 5(210)$ GB in fcc Ni (upper panel) and Co (lower panel) with segregated impurities. The empty and full symbols correspond to substitutionally and interstitially segregated impurities, respectively. The dotted horizontal lines mark the $\sigma_{\text{max}}$ values computed for clean GBs. (For interpretation of the references to color in this figure, the reader is referred to the web version of this article.)

### 3.2. Effect of impurities

#### 3.2.1. Results from the RGS model

Optimized computational supercells for impurity segregated GBs in fcc Ni and Co were first subjected to a simulated tensile test that conforms to the RGS model. The results are displayed in Fig. 3 in terms of the maximum values $\sigma_{\text{max}}$ of axial stress. Elements from the same group are denoted by the same symbols (circles for 13th, squares for 14th, diamonds for 15th and triangles for 16th group in Periodic Table), periods are distinguished by colors (red for 3rd, blue for 4th and green for 5th period) and, in order to distinguish the segregation preference, we systematically plot interstitially segregated impurities by solid symbols and those segregated substitutionally by open symbols. The maximum tensile stresses computed for a clean GB (25.3 GPa for Ni and 27.4 GPa for Co) are displayed in Fig. 3 by the dotted horizontal lines. It is obvious that the effect of impurities segregated at GBs predicted by the RGS model is very similar for both studied metals. Strength enhancement is predicted only for GBs with interstitially segregated Si and P. In the case of GB in fcc Ni, results for these two elements are in agreement with predictions based on calculations of strengthening/embrittling energy [4]. One can note only one inconsistent prediction: Slightly strengthening effect predicted for

substitutionally segregated Al is not confirmed by the present RGS calculations that report a slight strength reduction instead. The other elements are predicted to reduce the strength, again in agreement with the energy arguments [4]. In the case of GB in fcc Co, only Si was previously found [7] to be a strength enhancer while the other elements were consistently (except for P) predicted to reduce the strength of GB in fcc Co. Phosphorus was, contrary to the present results, reported to slightly reduce the GB cohesion. There are two major reasons for the differences in predictions mentioned above: First, the predictions based on strengthening/embrittling energy [4,7] considered fully relaxed structure of both the GB and a free surface. The RGS model started from fully relaxed GB as well but the fracture surfaces were not relaxed. The other reason is that (as will be mentioned later in the text) the maximum tensile stress is not necessarily directly proportional to the cleavage energy (which is proportional to the strengthening/embrittling energy).

The strength values in Fig. 3 exhibit certain periodicity: GB with elements from the 14th group exhibit the highest strength within the studied elements of the same period. Mean values for each period then exhibit a decreasing trend with increasing atomic number. Some of the $\sigma_{\text{max}}$ values can be compared with results of former calculations. For example, the values of 20.4 GPa and 29.2 GPa computed for interstitially segregated S and P, respectively, agree well with the values of 22 GPa and 31 GPa reported by Yamaguchi et al. [1]. Models which incorporate optimization of atomic positions usually report values that are somewhat lower than those from the RGS model. For example, strength of GB in fcc Ni with segregated S atoms (of the equivalent GB coverage) computed by Schusteritsch and Kaxiras [5] (17.7 GPa) was lower than their result for a clean GB (20.9 GPa). The reported reduction of strength caused by sulphur is in agreement with our results. Similarly, our prediction for phosphorus is qualitatively consistent with calculations by Liu et al. [6] who predicted a slight strength enhancement by a presence of segregated P.

Although we calculated the tensile stress from finite differences of the total energy (using sufficiently small strain increments), we also fitted our computed energies (for an extended range of strains) to the well known universal binding energy relationship (UBER) formulated by Rose et al. [22];

$$
E_{\mathrm{b}}=W_{\mathrm{s}}\left[1-\left(1+\frac{x}{L}\right) \exp (-x / L)\right], \tag{1}
$$

where $W_{\mathrm{s}}$ is the work of separation (or cleavage energy), $L$ is a critical length and $x$ is the displacement of the two rigid grains. Validity of the relationship (1) for a description of an energy-displacement dependence in RGS model was verified in several papers (see, e.g., Lazar and Podloucky [23] and Janisch et al. [9]) and we also successfully fitted all our computed data to the UBER curve. Table 1 contains the obtained values of the UBER parameter $W_{\mathrm{s}}$. One can note a correlation between the $W_{\mathrm{s}}$ values and the $\sigma_{\text{max}}$ values in Fig. 3. This correlation is not a coincidence since the critical length values for all the elements are scattered within the relatively narrow range of 0.5–0.6 Å (on average, the $L$ values of GBs with interstitial impurities are close to 0.52 and and those of GBs with substitutional impurities are close to 0.57). Thus the predictions based simply on the cleavage energy are in agreement with $\sigma_{\text{max}}$ values in most cases. For example, presence of Si atoms at a GB enhances its cleavage energy in both the Ni and Co crystals. On the other hand, the strength enhancement by P atoms predicted from $\sigma_{\text{max}}$ values is not confirmed by the computed cleavage energy. Although the $W_{\mathrm{s}}$ values for phosphorus at GB are the second highest among all (in Ni as well as in Co), comparing them with the corresponding values for clean GBs shows that $W_{\mathrm{s}}$ computed for P in Ni is same and that computed in Co is slightly lower.

All the above mentioned RGS calculations were performed for a standard choice of a cleavage plane which is the plane located between the GB plane and the first neighboring plane in a bulk. Some of the previous computational tensile tests considering optimizations of atomic positions at each strain increment confirmed justifiability of this choice (e.g. for S at GB in Ni [2]). On the other hand, some impurities can draw charge from the neighboring metal atoms onto themselves which can result in weakening the bonds between metal atoms. Consequently, there can be relatively strong bonding between atoms in the GB plane and the first neighboring planes (particularly between the impurity and metal atoms), strength of which can exceed that between some pair of neighboring planes with the weakened metallic bonds. Such an effect of the impurity atoms was reported, e.g., for phosphorus in fcc Ni [6] or for an interface between Ti and a-C:H [24]. In order to verify the preferred cleavage plane, we computed tensile tests using the RGS model for cleavage planes located between the first and the second and between the second and third atomic planes in the Ni bulk. These tensile test were performed for all interstitially segregated impurities. Since all the substitutionally segregated elements are predicted to reduce the GB cohesion, we ran the same computation only for Al (with the lowest reduction of GB strength). The results confirmed validity of the standard choice of the cleavage plane in most cases. Only in the cases of Si and P, the strength calculated for a cleavage plane located between the first and the second Ni plane in the bulk was lower than that for the cleavage plane between the GB and the Ni first plane. For Si we obtained the strength of 26.3 GPa that is by about 3.2 GPa lower than the value plotted in Fig. 3 and for P we got a reduction by 3.7 GPa to the value of 25.5 GPa which is just a little bit greater than the strength of the clean GB. This reduction of $\sigma_{\text{max}}$ was, however, not reflected by changes of the cleavage energy $W_{\mathrm{s}}$ which had, in both cases, higher values than those in Table 1.

### 3.2.2. Results from the OUL model

Strength values computed for impurity segregated GBs using the OUL model are displayed in Fig. 4. The maximum tensile stresses computed for the clean GBs (7.7 GPa for Ni and 8.4 GPa for Co) are again displayed by the dotted horizontal lines. From a comparison of the data one can see that the $\sigma_{\text{max}}$ values obtained from OUL also for all impurity decorated GBs are remarkably lower than those obtained using RGS. On the other hand, they are mostly higher than the strengths of the clean GBs in both studied metals, thus predicting a cohesion enhancement by a presence of almost all the impurities at GB. Only the atoms of Ga are predicted to have no effect on the cohesion of GB in fcc Ni and slightly weakening effect at GB in fcc Co. Atoms of Al are predicted to slightly increase the strength of GB in Ni but decrease the strength in Co.

One can also note that interstitially segregated elements are predicted to enhance the tensile strength of GB on average more than those segregated substitutionally. This suggests that the strength enhancement might be, at least partially, caused by the GB geometry and the related deformation mechanism. In order to

Table 1.
Computed values of the cleavage energy $W_{\mathrm{s}}$ in $\mathrm{J} / \mathrm{m}^{2}$ for the $\Sigma 5(210)$ grain boundaries in fcc Ni and fcc Co decorated by the studied impurities. The values of $W_{\mathrm{s}}$ for the clean GBs in Ni and Co are $3.94 \mathrm{~J} / \mathrm{m}^{2}$ and $4.42 \mathrm{~J} / \mathrm{m}^{2}$, respectively.

<table>
<thead>
<tr>
<th>Substitutional<br>GB</th>
<th>in Ni</th>
<th>in Co</th>
<th>Interstitial<br>GB</th>
<th>in Ni</th>
<th>in Co</th>
</tr>
</thead>
<tbody>
<tr>
<td>+Al</td>
<td>3.91</td>
<td>3.93</td>
<td>+Si</td>
<td>4.34</td>
<td>4.68</td>
</tr>
<tr>
<td>+Ga</td>
<td>3.27</td>
<td>3.34</td>
<td>+P</td>
<td>3.94</td>
<td>4.24</td>
</tr>
<tr>
<td>+In</td>
<td>2.89</td>
<td>2.83</td>
<td>+S</td>
<td>2.68</td>
<td>3.02</td>
</tr>
<tr>
<td>+Sn</td>
<td>2.85</td>
<td>2.76</td>
<td>+Ge</td>
<td>3.56</td>
<td>3.90</td>
</tr>
<tr>
<td>+Sb</td>
<td>2.47</td>
<td>2.40</td>
<td>+As</td>
<td>3.16</td>
<td>3.44</td>
</tr>
<tr>
<td>+Te</td>
<td>1.93</td>
<td>1.81</td>
<td>+Se</td>
<td>2.21</td>
<td>2.51</td>
</tr>
</tbody>
</table>

![](./images/814520262555860993_7.jpg)

Fig. 4. The maximum tensile stress values $\sigma_{\text{max}}$ calculated using optimized uniaxial loading (OUL) for $\Sigma 5(210)$ GB in fcc Ni and Co with segregated impurities.

explore the structural changes in our model, we substantially ex- tended the range of tensile strains for selected cases. Since the OUL model is computationally very demanding, we limited our atten- tion to the clean GB in Ni and to the same GB with substitutionally segregated Al and Te and interstitially segregated Si. Reason for including two substitutionally segregated elements was that, while the GB with Te exhibits the highest strength value in OUL model and the lowest value in the RGS model, response of the GB with Al to both loading models is almost opposite from this point of view.

Fig. 5 displays computed values of the total energy $E_{\text{tot}}$ as functions of the tensile strain for the four selected systems. Zero level was set to the energies of the optimized unstrained struc- tures individually for each system. The energy profile for the clean GB exhibits two additional minima besides that at the zero strain. The energy minimum at the strain of 0.20 is only 0.2 eV above that of the optimized ground state. Similar local energy minimum seems to exist (at the strain of 0.18) on the energy profile of the GB with Si and we verified that the data point corresponds to a stress- free state. In both cases, the local minima are surrounded by rapid changes of the energy (accompanied by similarly sharp changes of the structural parameters). On the other hand, both GBs with substitutionally segregated Al and Te have continuous energy profiles exhibiting only one energy minimum at nonzero strain each.

The energy minimum computed for the clean GB at the strain of 0.32 is about 3.2 eV below that at the zero strain which suggests that optimizations during the tensile loading drew the structure to energetically more favorable state. The structure of the clean GB is illustrated in Fig. 6 at strains corresponding to all the three energy minima. Only half of the supercell (the Ni bulk limited by two GB planes) is shown there. Fig. 6(a) shows the ground state of the $\Sigma 5(210)$ GB and the blue square highlights a (001) plane of the fcc unit cell. The structure at the strain of 0.32 that corresponds to the state of the lowest energy is displayed in Fig. 6(c). After a closer inspection we successfully identified the structure with the $\Sigma 11(311)$ GB in the fcc Ni and the blue rectangle displays the (110) plane in a single fcc unit cell. On the other hand, we did not succeed in identifying the structure in Fig. 6(b) that corresponds to the local energy minimum with any structure of a higher symmetry.

![](./images/814520262555860993_8.jpg)

Fig. 5. The total energy $E_{\text{tot}}$ profiles in an extended range of tensile strains cal- culated using optimized uniaxial loading (OUL) for the clean and three impurity segregated GBs in fcc Ni.

The global energy minimum calculated in the model of GB with segregated Al corresponds to almost the same structure as we described for the clean GB. Although the energy profile for GB with segregated Te exhibits only a shallow local minimum (at a strain of about 0.25) 4.6 eV above the equilibrium, the structure is again very similar to that of the fcc Ni with the $\Sigma 11(311)$ GB. The energy profile for interstitially segregated Si at the GB is discontinuous and there is no evident second energy minimum. The data point at the strain of 0.29, however, corresponds to another stress-free state (according to the computed stress tensor) and the structure in the Ni bulk is again very similar to that in Fig. 6(c). It seems that the structural transition changing the type of GB is suppressed by addition of an element segregated at the GB, which increases the GB energy for the $\Sigma 11(311)$ configuration. Consequently, the maximum tensile stress computed using the fully relaxed (OUL) model is increased by most of the segregated elements.

Although the above described mechanism offers an explanation for the strength enhancement predicted by the OUL model, it is unlikely to occur in reality. The quasi-static calculations can often find an optimized structure after an onset of instability in the lattice. Real systems can, however, deviate from the simulated deformation path not only at the strains related to the dis- continuities in energy profiles (in Fig. 5) but even at lower strains related to occurrence of soft phonons (that was not tested in present simulations) or instability of other kind (e.g. related to unstable propagation of defects in real lattice). If such instabilities were not present in the lattice prior reaching critical strains (of about 0.10) related to $\sigma_{\text{max}}$ values, these values of stress would equal to the theoretical strength, regardless of the likely

![](./images/814520262555860993_9.jpg)

Fig. 6. The upper half of the computational supercell for a clean GB in Ni at (a) the zero strain, (b) the strain of 0.20 and (c) the strain of 0.32. Orientations of a single fcc unit cell are marked as blue rectangles. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

occurrence of instabilities at higher strains.

## 4. Discussion

The striking difference between predictions of the methods presented in this paper deserves a closer inspection. As was mentioned in Section 3.1, differences in magnitudes of the tensile strength might be explained by the effect of transverse stresses occuring in simulations that neglect Poisson contraction (such as the RGS method as well as methods that comprise optimization of atomic positions). In order to estimate level of such transverse stresses, we applied uniaxial deformation along the [210] direction to a single crystal of Ni. During this tensile test, the Ni crystal was uniformly strained along the loading axis while the transverse strains were zero. The transverse stresses that were computed using this model are plotted in Fig. 7 as functions of the axial stress. Their crystallographic orientation (consistent with directions in Fig. 1) is indicated by the subscripts. The maximum axial stress of about 30.6 GPa is close to the value computed using the RGS model (see Fig. 2). The results also clearly show that both stresses are tensile (as usual, positive values correspond to tension) and almost linearly increasing with increasing axial stress (except for the values close to the maximum). Thus, omitting the

![](./images/814520262555860993_10.jpg)

Fig. 7. Transverse stresses computed as functions of the axial stress in a single crystal of fcc Ni under uniaxial deformation.

Poisson contraction during the [210] tension of fcc Ni induces triaxial stress state with the ratio the transverse stresses $\sigma_{[001]}/\sigma_{[1\overline{2}0]}$ approximately equal to 1.4. Results of former calculations [21] of tensile strength of fcc and bcc crystals under superimposed isotropic transverse stresses revealed that tensile transverse stresses mostly increase the tensile strength values. From the low-index directions studied therein, [110] is the one crystallographically closest to orientation of the loading axis in the present study. Also the [110] strength value of 9.5 GPa reported for fcc Ni [21] is close to the present OUL value for bulk Ni of 10.4 GPa. Therefore, one can also expect similar effect of the transverse stresses that was predicted to be strength-enhancing: The tensile strength was increased by about 80% of the superimposed transverse stresses. Similar effect was formerly obtained by Zhang et al. [25] who employed molecular dynamics simulations with semiempirical interatomic potentials for tensile tests on a set of $\Sigma 5$ GBs in fcc Cu. Considering different boundary conditions they obtained remarkably higher strength values in models of constrained tension than in those considering the Poisson contraction.

In order to bring a direct proof of the aforementioned effect of transverse stresses, we performed additional tensile tests on GBs using the procedure that was employed for the OUL model with modified settings. During these tensile tests, the transverse stresses were not relaxed; they were converged to constant values keeping $\sigma_{[001]} = 1.4\sigma_{[1\overline{2}0]}$ for each axial strain increment instead. Besides the clean GB in Ni, we studied the effect of transverse stresses also for four more GBs with impurities. We considered the same three examples of GBs as in the previous section (Al, Si and Te) and GB with Se, since this system (among the interstitially segregated GBs) exhibits the greatest strength reduction in the RGS model whereas the OUL model predicts a nonnegligible strength enhancement. The maximum axial stress values $\sigma_{\text{max}}$ obtained from these calculations are displayed in Fig. 8 for several constant values of $\sigma_{[1\overline{2}0]}$. These data points clearly demonstrate that the transverse stresses raise the predicted strength values remarkably. This can explain the quantitative differences between strength values calculated by means of both considered models. Moreover, different sensitivity of individual GBs to transverse stresses caused by a presence of the impurity atoms brings another explanation (another point of view to that presented in previous section in terms of the structural transformation) of the qualitatively different predictions of these models. The values for $\sigma_{[1\overline{2}0]} = 0$ are results of the OUL model for Ni (displayed also in Fig. 4). Shifting from left to right in Fig. 8 one can cross from the predictions of the OUL model closer to those of the RGS model or

![](./images/814520262555860993_11.jpg)

Fig. 8. The maximum axial stress values $\sigma_{\max}$ computed for five levels of the transverse stresses keeping their ratio $\sigma_{[001]} / \sigma_{[1 \overline{2} 0]}=1.4$. Slopes of the connecting lines correspond to sensitivity of $\sigma_{\max }$ values to transverse stresses. Intersections of lines for segregated GBs with that for a clean GB mean the qualitative changes in predictions of strengthening or embrittlement caused by the impurity.

other models neglecting the Poisson contraction (including the already mentioned models with optimized atomic positions [5,6]). The sensitivities of $\sigma_{\max }$ to $\sigma_{[1 \overline{2} 0]}$ for individual GBs are proportional to slopes of the lines connecting the corresponding data points.

Despite the fact that the estimate of transverse stresses was simply based on calculations for a bulk Ni, the trends displayed by the lines are mostly consistent with our results. The data for GB with interstitially segregated Si exhibit only slightly lower sensi- tivity than the clean GB which, along with sufficient difference in $\sigma_{\max }$ for $\sigma_{[1 \overline{2} 0]}=0$, ensures consistent predictions from both com putational models. On the other hand, Se and Te reduce the sen- sitivity of GB to transverse stresses which results in opposite predictions of their effect on the GB cohesion for lower and higher transverse stresses. This might also explain the difference in pre- dictions of the OUL and RGS models. Sensitivity of the GB with substitutionally segregated Al is very similar to that of the clean GB and Fig. 8 predicts only slight strength enhancement in the whole studied range of transverse stresses. The slight strength reduction predicted by the RGS model thus cannot be explained by the effect of transverse stresses alone. In this case, the strain lo- calization and keeping the atomic positions fixed (without re- laxation) can play more important role than in the cases men- tioned above.

Naturally, a question that arises from the analysis is: "Which of the two sets of predictions is closer to reality? " There is no simple answer to this question since it depends on the local stress state in the GB region in a real polycrystal. Owing to geometrical restric- tions in polycrystalline materials, the grains cannot fully relax the transverse stresses. On the other hand, the grains can, at least partially, contract perpendicularly to the loading direction. Thus, neither the OUL nor the RGS model (nor any other atomistic model available in literature) describes the deformation entirely correctly. This, however, does not mean that atomistic approaches cannot give correct predictions, it only advices the researchers to interpret their data cautiously. Our study considered twelve elements as possible impurities. Making a thorough analysis for each of them (to predict their effect on GB cohesion) is a very demanding task. Thus we can just summarize that Si and P are expected to enhance the cohesion of both GBs, Al has rather negligible effect and per- haps Ga has likely slightly embrittling effect. Predictions for other elements can be made employing data such as those in Fig. 8: The higher transverse stresses correspond to the intersection of lines corresponding to the clean and segregated GB, the more likely the element has strength enhancing effect.

It should be noted, however, that the present results corre- spond to one particular GB and one particular (in a sense "geo- metrically optimal") concentration of impurities at the GB, i.e., the segregated atoms fill all available interstitial positions at the GB or, in the case of substitutional segregation, replace all Ni atoms at the GB plane (see Fig. 1). The effect of segregated impurities on GB cohesion can substantially differ for other concentrations which can be illustrated on the example of sulphur at GB in Ni. According to experiments [26], intergranular embrittlement is observed in Ni polycrystals after the S concentration reaches a critical level. Analysis by Yamaguchi et al. [1] demonstrated that the critical concentration is higher than that considered in the present study. This means that the experiment suggests that effect of the studied S content should not be embrittling.

## 5. Conclusions

Computational tensile tests of impurity-decorated $\Sigma 5(210)$ grain boundaries in crystals of fcc Ni and fcc Co were performed considering two deformation models. On average, the model of displacement of rigid grains yields approximately two times greater values of tensile strength than the model of fully optimized uniaxial loading. While the strength values calculated using a rigid grain shift predict a strength enhancement only for segregated Si and P, the model of fully optimized uniaxial loading exhibits the strengthening effect for all the 12 studied elements (with rather negligible effect of Ga and Al). These qualitatively different re- sponses are explained in terms of the effect of transverse stresses that are not relaxed in the model with rigid grains. Our optimized model of a tensile test on clean GB in fcc Ni predicted a structural transformation from the $\Sigma 5(210)$ GB to a $\Sigma 11(311)$ GB with lower energy.

## Acknowledgements

This research was supported by the Czech Science Foundation (Projects No. GAP108/12/0311 and GA16-24711S), by the Ministry of Education, Youth and Sports of the Czech Republic under the Project CEITEC 2020 (Project No. LQ1601) and by the Academy of Sciences of the Czech Republic (Institutional Project No. RVO:68081723). Computational resources were provided by the Ministry of Education, Youth and Sports of the Czech Republic under the Project IT4Innovations National Supercomputer Center (Project No. LM2015070) within the program Projects of Large Research, Development and Innovations Infrastructures.

## References

[1] M. Yamaguchi, M. Shiga, H. Kaburaki, Grain boundary decohesion by impurity segregation in a nickel-sulfur system, Science 307 (5708) (2005) 393-397.
[2] Z.X. Tian, J.X. Yan, W. Xiao, W.T. Geng, Effect of lateral contraction and mag- netism on the energy release upon fracture in metals: first-principles com- putational tensile tests, Phys. Rev. B 79 (2009) 144114.
[3] M. Všianská, M. Šob, Magnetically dead layers at $sp$-impurity-decorated grain boundaries and surfaces in nickel, Phys. Rev. B 84 (2011) 014418.
[4] M. Všianská, M. Šob, The effect of segregated $sp$-impurities on grain-boundary and surface structure, magnetism and embrittlement in nickel, Prog. Mater. Sci. 56 (2011) 817-840.
[5] G. Schusteritsch, E. Kaxiras, Sulfur-induced embrittlement of nickel: a first- principles study, Modell. Simul. Mater. Sci. Eng. 20 (6) (2012) 065007.
[6] W. Liu, C. Ren, H. Han, J. Tan, Y. Zou, X. Zhou, P. Huai, H. Xu, First-principles study of the effect of phosphorus on nickel grain boundary, J. Appl. Phys. 115 (4) (2014) 043706.

[7] M. Všianská, H. Vémolová, M. Šob, Segregation of sp-impurities at grain boundaries and surfaces: comparison of fcc cobalt and nickel, in preparation.

[8] S. Sanyal, U.V. Waghmare, P.R. Subramanian, M.F.X. Gigliotti, Effect of dopants on grain boundary decohesion of ni: a first-principles study, Appl. Phys. Lett. 93 (22) (2008) 223113.

[9] R. Janisch, N. Ahmed, A. Hartmaier, Ab initio tensile tests of al bulk crystals and grain boundaries: Universality of mechanical behavior, Phys. Rev. B 81 (2010) 184108.

[10] H. Lee, V. Tomar, Understanding the influence of grain boundary thickness variation on the mechanical strength of a nickel-doped tungsten grain boundary, Int. J. Plast. 53 (2014) 135-147.

[11] Y.S. Han, V. Tomar, An ab-initio investigation of the effect of graphene on the strength-electron density correlation in SiC grain boundaries, Comput. Mater. Sci. 92 (2014) 422-430.

[12] F. Milstein, H.E. Fang, J. Marschall, Mechanics and energetics of the Bain transformation, Philos. Mag. A 70 (4) (1994) 621-639.

[13] E.A. Owen, D.M. Jones, Effect of grain size on the crystal structure of cobalt, Proc. Phys. Soc. Lond., Sect. B 67 (6) (1954) 456.

[14] J. Huang, Y. Wu, H. Ye, Allotropic transformation of cobalt induced by ball milling, Acta Mater. 44 (3) (1996) 1201-1209.

[15] G. Kresse, J. Hafner, Norm-conserving and ultrasoft pseudopotentials for first- row and transition elements, J. Phys.: Condens. Matter 6 (40) (1994) 8245-8257.

[16] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (16) (1996) 11169-11186.

[17] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector aug- mented-wave method, Phys. Rev. B 59 (3) (1999) 1758-1775.

[18] M. Černý, Elastic stability of magnetic crystals under isotropic compression and tension, Mater. Sci. Eng. A 462 (2007) 432-435.

[19] C. Kittel, Introduction to Solid State Physics, 8th edition, John Wiley & Sons, 2005.

[20] M. Zelený, D. Legut, M. Šob, Ab initio study of Co and Ni under uniaxial and biaxial loading and in epitaxial overlayers, Phys. Rev. B 78 (2008) 224105.

[21] M. Černý, J. Pokluda, Ideal tensile strength of cubic crystals under super- imposed transverse biaxial stresses from first principles, Phys. Rev. B 82 (17) (2010) 174106.

[22] J.H. Rose, J.R. Smith, J. Ferrante, Universal features of bonding in metals, Phys. Rev. B 28 (1983) 1835-1845.

[23] P. Lazar, R. Podloucky, Cleavage fracture of a crystal: density functional theory calculations based on a model which includes structural relaxations, Phys. Rev. B 78 (2008) 104114.

[24] M. Mrověc, D.D. Stefano, C. Elsässer, S. Rajagopalan, P.A. Stevens, Theoretical study of interfaces between transition metals and a-C:H (2016), in preparation.

[25] L. Zhang, C. Lu, K. Tieu, Atomistic simulation of tensile deformation behavior of $\Sigma 5$ tilt grain boundaries in copper bicrystal, Sci. Rep. 4 (2014) 5919.

[26] J. Heuer, P. Okamoto, N. Lam, J. Stubbins, Disorder-induced melting in nickel: implication to intergranular sulfur embrittlement, J. Nucl. Mater. 301 (2-3) (2002) 129-141.