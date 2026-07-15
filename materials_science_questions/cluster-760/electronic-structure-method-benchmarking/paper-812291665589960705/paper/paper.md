# Oxirene: To Be or Not To Be?

George Vacek, John Morrison Galbraith, Yukio Yamaguchi, and Henry F. Schaefer, III*
Center for Computational Quantum Chemistry, University of Georgia, Athens, Georgia 30602

Ross H. Nobes
Australian National University Supercomputer Facility, Canberra, ACT 0200, Australia

Anthony P. Scott and Leo Radom*
Research School of Chemistry, Australian National University, Canberra, ACT 0200, Australia

Received: February 28, 1994; In Final Form: May 27, 1994®

The $C_{2v}$-symmetry structure of oxirene has been examined using *ab initio* molecular orbital calculations with large basis sets and a variety of methods of including electron correlation. Different qualitative conclusions regarding the nature of oxirene are reached, depending on the choice of basis set and method of electron correlation incorporation. With certain combinations of basis set and theoretical method, the symmetric oxirene structure is found to be a saddle point on the potential energy surface, while for other combinations oxirene is a local minimum. Inclusion of triple excitations in the correlation treatment has a large effect, tending to make the curvature of the surface corresponding to a ring-opening distortion of the $C_{2v}$-symmetry structure less positive (or more negative). This is counterbalanced by a basis set effect, with inclusion of f functions making the curvature more positive. At our highest level of theory, CCSD(T) with basis sets of triple-$\zeta$ quality and including multiple d shells and an f shell on C and O and multiple p shells and a d shell on H, oxirene is a genuine minimum under harmonic vibrational analysis, with a ring-opening frequency of 139-163 cm⁻¹.

## Introduction

The decomposition-rearrangement of diazoketones and diazoesters to form ketenes and nitrogen, the Wolff rearrangement (eq 1), was first documented in 1902.¹ Although almost a century

$$
\mathrm{R_1-\overset{N_2}{\underset{C}{||}}-\overset{O}{\underset{C}{||}}-R_2 \xrightarrow{h\nu, \Delta} R_1-\underset{R_2}{\overset{C}{||}}=C=O + N_2} \tag{1}
$$

has passed, the mechanism of the Wolff rearrangement is still in doubt. Numerous possibilities for the mechanism have been proposed, but to date no consensus among chemists has been reached. Meier and Zeller² have reviewed the progress made in determining the Wolff rearrangement mechanism, including the possible roles of both free and complexed carbenes, 1,3-dipoles, 1,3-diradicals, and oxirenes as intermediates or transition structures. Wolff himself believed that reaction 1 involved ketocarbenes as intermediates. More recently, the participation of symmetric intermediates, particularly oxirenes, has been proposed and supported by results from isotopic-labeling experiments,³⁴ despite the fact that earlier experimental studies failed to lend support for their existence.⁵

The history of the study of oxirenes, and to some extent ketocarbenes, is well documented in Lewar's 1983 review.⁶ At that time, experimental evidence only supported the existence of oxirenes as short-lived intermediates in photochemical and thermal Wolff rearrangements,³⁴ in the peroxyacid oxidations of acetylenes,⁷ and in ketene photolysis reactions.⁸ Since then, evidence has been presented for the observation of a substituted oxirene by laser flash photolysis during a Wolff rearrangement⁹ and for the detection by FT-IR spectroscopy of dimethyloxirene, isolated in rare-gas matrices during the photolysis of 3-diazo-2-butanone.¹⁰

Several experimental attempts have been made to isolate the parent oxirene molecule in the gas phase. Most recently, Hop, Holmes, and Terlouw¹¹ have tried to produce oxirene by the creation and subsequent vertical neutralization of oxirene radical cation, which had been predicted theoretically to be stable.¹² This attempt was unfortunately unsuccessful. Thus, no firm conclusion as to whether unsubstituted oxirenes are true minima on the potential energy surface (PES) or whether they are merely transition structures has yet been reached. Hope for the isolation of oxirene might be taken from the direct observation of the short-lived $\tilde{X}^1A_1$ vinylidene species, which was (albeit with much controversy) predicted to exist with *ab initio* theory¹³ and observed by Lineberger's group with negative ion photoelectron spectroscopy.¹⁴ Similar success by similar means was achieved for the $\tilde{X}^1A'$ state of monofluorovinylidene, which has an isomerization barrier height of only 2 kcal mol⁻¹.¹⁵,¹⁶ Unfortunately, oxirene has no stable anion, and so negative ion photoelectron spectroscopy will not be a viable technique for observing neutral oxirene.

Numerous theoretical investigations, both semiempirical¹⁷,¹⁸ and *ab initio*,¹⁹⁻²⁵ have been undertaken on the PES that includes ketene, formylmethylene, and oxirene. MINDO/3 and NDDO calculations¹⁸ find oxirene to be more stable than formylmethylene by about 20 kcal mol⁻¹. *Ab initio* results at the Hartree-Fock level,¹⁹,²²⁻²⁴ on the other hand, show formylmethylene to be more stable than oxirene by 12-17 kcal mol⁻¹. When electron correlation is included through single-point calculations on the Hartree-Fock-optimized structures,²³,²⁴ formylmethylene is still favored, but the energy difference is reduced to 1-8 kcal mol⁻¹. Moreover, such calculations have suggested that singlet formylmethylene can collapse without a barrier to ketene, the Hartree-Fock transition structure for rearrangement lying lower in energy on the correlated surface than formylmethylene itself.²³,²⁴ We note that, in the thermolysis of diazoketones, the participation of oxirene appears to be small at low temperatures where ketocarbenes are most important but increases with increasing temperature.⁴ This implies that ketocarbenes are energetically more stable than oxirenes.

Ketocarbenes have been isolated in low-temperature matrices.²⁶ These ketocarbenes were triplet ground states, however, that

---
* Abstract published in Advance ACS Abstracts, July 15, 1994.

0022-3654/94/2098-8660$04.50/0
© 1994 American Chemical Society

Oxirene: To Be or Not To Be?

should not contribute to the Wolff rearrangement which is considered to occur on the singlet surface. $^{27}$ Nevertheless, the possibility of singlet-triplet crossing cannot be discarded entirely. The interested reader is referred to an MCSCF study by Novoa, McDouall, and Robb for a discussion of this possibility. $^{28}$

Those ab initio studies $^{19-24}$ which have considered the barrier to ring opening for oxirene have all concluded that the barrier is less than $7.3\ \text{kcal}\ \text{mol}^{-1}$. The most reliable figure is perhaps that of $2\ \text{kcal}\ \text{mol}^{-1}$ as determined by Tanaka and Yoshimine by using a reaction coordinate approach. $^{23}$ The existence of a barrier at low levels of theory suggests that oxirene should be a minimum, but a more rigorous test lies in vibrational analyses at higher levels of theory. Bouma et al. $^{24}$ determined that at the HF/3-21G level of theory the $C_{2v}$-symmetry form of oxirene is a minimum with a ring-opening frequency of $524\ \text{cm}^{-1}$. More recently Vacek, Colegrove, and Schaefer $^{25}$ found a decrease (from 524 to 445 $\text{cm}^{-1}$) in the ring-deformation ($b_2$) vibrational frequency when the basis set was improved moderately (to DZP). The Vacek paper $^{25}$ also shows this particular frequency decreasing further (from 445 to $262\ \text{cm}^{-1}$) with inclusion of electron correlation. Although at their highest level of theory (CCSD/DZP) they still conclude that oxirene is a minimum, Vacek et al. $^{25}$ were not confident that the effects of still larger basis sets and improved treatments of electron correlation would not cause this particular frequency to become imaginary.

Clearly, there are many questions that remain unanswered concerning oxirene and related species that would benefit from a high-level ab initio determination of the entire oxirene $\rightarrow$ ketene potential energy hypersurface, and from calculations on related larger homologues. These include the issue of substitution effects on the stability of oxirenes, $^{29}$ an understanding of the kinetics of reactions on the $\text{C}_2\text{H}_2\text{O}$ PES, $^{30,31}$ and further probing of the mechanism for the Wolff rearrangement. $^{32}$ In the present paper, we address the particular aspect of whether or not high-level ab initio calculations indicate oxirene to be a true minimum on the surface.

### Theoretical Methods

The $C_{2v}$-symmetry structure of oxirene was studied with a variety of basis sets and methods of electron correlation. Calculations were carried out using the Gaussian 92/DFT$^{33}$ and ACES II$^{34}$ programs (at the Australian National University, ANU) and the PSI program (at the Center for Computational Quantum Chemistry, CCQC). $^{35}$

Calculations at the ANU employed the standard 6-31G(d), 6-31G(d,p), and 6-311G(d,p) basis sets$^{36}$ and the Dunning correlation-consistent basis, cc-pVTZ. $^{37}$ Additional polarization functions and diffuse functions were added to the 6-31G(d,p) and 6-311G(d,p) basis sets to form the 6-31G(df,p), 6-311G-(df,p), and 6-311+G(2df,p) sets. $^{38,39}$ Basis sets formed from 6-31G employed sets of six Cartesian d-like and ten Cartesian f-like polarization functions while those based on 6-311G and cc-pVTZ employed five pure d and seven pure f polarization functions, i.e. spherical harmonics.

The DZP basis used in the calculations performed at the CCQC was derived from the standard DZ basis by augmenting with a set of d-like functions on the heavy atoms and a set of p functions on hydrogen. $^{38,40}$ The DZP++ set was constructed by adding diffuse s and p functions to the DZP basis. $^{41,42}$ The TZ2P basis was constructed from the standard TZ basis by the addition of two sets of polarization functions on each atom. $^{38,43}$ This basis was further enhanced by the addition of f-like polarization functions on the heavy atoms and a set of d-like functions on hydrogen, $^{38,44}$ leading to the basis referred to as TZ2P(f,d) in the text. Yet another basis, TZ2P++, was formed by the addition of diffuse functions to all atoms in the TZ2P set. $^{41,45}$ The QZ3P-(f,d) basis was constructed by the addition of higher angular momentum functions to a standard QZ basis. $^{38,46}$ All the CCQC basis sets employed sets of six Cartesian d-like and ten Cartesian f-like polarization functions.

The molecular structure of oxirene was fully optimized using analytic gradient techniques for restricted Hartree-Fock (RHF),$^{47}$ Møller-Plesset perturbation theory (MP$n$),$^{48-51}$ configuration interaction (CI),$^{52,53}$ coupled-cluster (CC),$^{54,55}$ and quadratic configuration interaction (QCI)$^{56,57}$ wave functions. Density functional calculations were also performed using the local SVWN functional, $^{58}$ the gradient-corrected BLYP functional, $^{58,59}$ and the hybrid Becke3LYP functional. $^{60}$ In all cases, the default geometry optimization criteria were employed. $^{61}$ For the iterative methods, all single and double excitations (SD) from the SCF reference configuration were included (CISD, CCSD, and QCISD). For the coupled-cluster and quadratic configuration methods, the effects of connected triple excitations were included perturbatively [CCSD(T), QCISD(T)].$^{55,57}$ In most of the calculations performed at the ANU, all orbitals were correlated (full, abbreviated fu), whereas in the CCQC calculations only the valence electrons were explicitly correlated; i.e. the three lowest-lying MOs (C and O 1s-like) were held doubly occupied (frozen core, abbreviated fc).

The RHF, density functional, and MP2 quadratic force constants were evaluated via analytic second-derivative procedures. $^{62-66}$ The method of finite central differences of the analytically derived gradients was utilized to evaluate the quadratic force constants for the remaining wave functions used in this study.

### Results and Discussion

#### Structural Predictions.
Total energies and structural predictions are shown in Table 1. Perhaps the most interesting feature is the relative insensitivity of the geometrical parameters to basis set improvements for a given theoretical method. For example, with the RHF method, the C--O bond length falls within a range of $0.01\ \text{\AA}$ across the entire set of bases. This contrasts with the large change seen in going from the smaller basis set 4-31G results ($r_{\text{CO}} = 1.552\ \text{\AA}$) of Tanaka and Yoshimine to their DZ + P results ($r_{\text{CO}} = 1.465\ \text{\AA}$), where there is a change of $0.09\ \text{\AA}.^{23}$ Clearly the first set of polarization functions is very important. On the other hand, increasing the size of the sp part of the basis (from a double to a triple split of the valence functions or by adding a set of diffuse functions) has very little effect on the calculated geometry. However, the addition of f-like polarization functions does have a significant effect, especially on the C--O bond length (decreasing this length by $0.010-0.015\ \text{\AA}$ for the conventional correlated methods). It is somewhat reassuring to see the geometrical results converge so quickly with basis set. Unfortunately, as discussed below, the harmonic vibrational frequencies are not so convergent with respect to increase in basis set size.

The geometrical parameters are more sensitive to the theoretical method used than they are to basis set. However, the trends observed (namely an increase in bond lengths as one improves the electron correlation scheme$^{67,68}$) are typical for C--O, C--C, and C--H bond distances. For the correlated methods, results with all orbitals included (fu) are very close to those using the frozen-core approach (fc) in the few cases for which direct comparisons are possible. The inclusion of triple excitations in the correlation treatment [MP4SDQ $\rightarrow$ MP4, QCISD $\rightarrow$ QCISD-(T), CCSD $\rightarrow$ CCSD(T)] has a relatively large effect, tending to increase the lengths of the C--C and C--O bonds. Note also the large fluctuations in the Møller-Plesset series, with a change of $0.021\ \text{\AA}$ in the C--O length in going from MP3 to MP4, and the wide range of values for the C--O length from the density functional approaches.

Despite the relatively large changes in the C--O lengths, it appears that the predictions of geometrical structure are converging toward a single set of values with electron correlation.

<table>
<caption>TABLE 1: Calculated Total Energies and Molecular Structures for the $C_{2v}$-Symmetry Structure of Oxirene$^{a}$<br>![](./images/812291665589960705_1.jpg)</caption>
<thead>
<tr>
<th>level of theory$^{b,c}$</th>
<th>source$^{d}$</th>
<th>total energy</th>
<th>$r$(C—O)</th>
<th>$r$(C$\xlongequal{}$C)</th>
<th>$r$(C—H)</th>
<th>&lt;CCH</th>
</tr>
</thead>
<tbody>
<tr>
<td>RHF/6-31G(d)</td>
<td>ANU</td>
<td>−151.583 90</td>
<td>1.467</td>
<td>1.244</td>
<td>1.062</td>
<td>162.8</td>
</tr>
<tr>
<td>RHF/DZP</td>
<td>CCQC</td>
<td>−151.617 18</td>
<td>1.466</td>
<td>1.251</td>
<td>1.066</td>
<td>162.6</td>
</tr>
<tr>
<td>RHF/DZP++</td>
<td>CCQC</td>
<td>−151.621 89</td>
<td>1.464</td>
<td>1.251</td>
<td>1.066</td>
<td>162.7</td>
</tr>
<tr>
<td>RHF/6-311G(d,p)</td>
<td>ANU</td>
<td>−151.623 65</td>
<td>1.464</td>
<td>1.243</td>
<td>1.061</td>
<td>162.8</td>
</tr>
<tr>
<td>RHF/6-311G(df,p)</td>
<td>ANU</td>
<td>−151.631 64</td>
<td>1.459</td>
<td>1.241</td>
<td>1.061</td>
<td>162.6</td>
</tr>
<tr>
<td>RHF/TZ2P</td>
<td>CCQC</td>
<td>−151.642 83</td>
<td>1.465</td>
<td>1.240</td>
<td>1.059</td>
<td>162.2</td>
</tr>
<tr>
<td>RHF/TZ2P++</td>
<td>CCQC</td>
<td>−151.643 95</td>
<td>1.464</td>
<td>1.240</td>
<td>1.059</td>
<td>162.3</td>
</tr>
<tr>
<td>RHF/cc-pVTZ$^{e}$</td>
<td>ANU</td>
<td>−151.645 36</td>
<td>1.460</td>
<td>1.240</td>
<td>1.059</td>
<td>162.5</td>
</tr>
<tr>
<td>RHF/TZ2P(f,d)</td>
<td>CCQC</td>
<td>−151.650 69</td>
<td>1.459</td>
<td>1.240</td>
<td>1.059</td>
<td>162.5</td>
</tr>
<tr>
<td>RHF/QZ3P(f,d)</td>
<td>CCQC</td>
<td>−151.656 86</td>
<td>1.457</td>
<td>1.240</td>
<td>1.059</td>
<td>162.5</td>
</tr>
<tr>
<td>SVWN/6-311G(df,p)</td>
<td>ANU</td>
<td>−151.697 02</td>
<td>1.481</td>
<td>1.265</td>
<td>1.081</td>
<td>161.8</td>
</tr>
<tr>
<td>BLYP/6-311G(d,p)</td>
<td>ANU</td>
<td>−152.478 27</td>
<td>1.530</td>
<td>1.273</td>
<td>1.076</td>
<td>161.7</td>
</tr>
<tr>
<td>BLYP/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.484 10</td>
<td>1.525</td>
<td>1.271</td>
<td>1.077</td>
<td>161.4</td>
</tr>
<tr>
<td>BLYP/6-311+G(2df,p)</td>
<td>ANU</td>
<td>−152.496 60</td>
<td>1.523</td>
<td>1.270</td>
<td>1.077</td>
<td>161.6</td>
</tr>
<tr>
<td>Becke3LYP/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.518 11</td>
<td>1.499</td>
<td>1.261</td>
<td>1.071</td>
<td>161.7</td>
</tr>
<tr>
<td>MP2-fc/6-31G(d)</td>
<td>ANU</td>
<td>−152.018 68</td>
<td>1.512</td>
<td>1.277</td>
<td>1.074</td>
<td>161.9</td>
</tr>
<tr>
<td>MP2-fc/6-311G(d,p)</td>
<td>ANU</td>
<td>−152.095 17</td>
<td>1.504</td>
<td>1.277</td>
<td>1.071</td>
<td>162.2</td>
</tr>
<tr>
<td>MP2-fc/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.146 80</td>
<td>1.492</td>
<td>1.274</td>
<td>1.073</td>
<td>161.9</td>
</tr>
<tr>
<td>MP2-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.204 18</td>
<td>1.489</td>
<td>1.272</td>
<td>1.072</td>
<td>161.8</td>
</tr>
<tr>
<td>MP2-fc/6-311+G(2df,p)</td>
<td>ANU</td>
<td>−152.185 35</td>
<td>1.500</td>
<td>1.271</td>
<td>1.071</td>
<td>162.0</td>
</tr>
<tr>
<td>MP2-fu/cc-pVTZ$^{e}$</td>
<td>ANU</td>
<td>−152.237 92</td>
<td>1.497</td>
<td>1.268</td>
<td>1.064</td>
<td>161.8</td>
</tr>
<tr>
<td>MP3-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.215 12</td>
<td>1.475</td>
<td>1.266</td>
<td>1.071</td>
<td>161.8</td>
</tr>
<tr>
<td>MP4SDQ-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.220 60</td>
<td>1.482</td>
<td>1.268</td>
<td>1.072</td>
<td>161.9</td>
</tr>
<tr>
<td>MP4-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.246 83</td>
<td>1.496</td>
<td>1.277</td>
<td>1.074</td>
<td>161.9</td>
</tr>
<tr>
<td>CISD-fc/DZP</td>
<td>CCQC</td>
<td>−152.022 66</td>
<td>1.491</td>
<td>1.272</td>
<td>1.073</td>
<td>162.0</td>
</tr>
<tr>
<td>CISD-fc/TZ2P</td>
<td>CCQC</td>
<td>−152.098 60</td>
<td>1.488</td>
<td>1.255</td>
<td>1.062</td>
<td>161.5</td>
</tr>
<tr>
<td>CISD-fc/TZ2P(f,d)</td>
<td>CCQC</td>
<td>−152.148 90</td>
<td>1.475</td>
<td>1.253</td>
<td>1.061</td>
<td>162.1</td>
</tr>
<tr>
<td>QCISD-fc/6-31G(d)</td>
<td>ANU</td>
<td>−152.036 19</td>
<td>1.506</td>
<td>1.275</td>
<td>1.075</td>
<td>162.1</td>
</tr>
<tr>
<td>QCISD-fu/6-31G(d)</td>
<td>ANU</td>
<td>−152.047 74</td>
<td>1.504</td>
<td>1.273</td>
<td>1.075</td>
<td>162.2</td>
</tr>
<tr>
<td>QCISD-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.221 52</td>
<td>1.483</td>
<td>1.269</td>
<td>1.072</td>
<td>162.0</td>
</tr>
<tr>
<td>QCISD(T)-fc/6-31G(d)</td>
<td>ANU</td>
<td>−152.053 24</td>
<td>1.514</td>
<td>1.281</td>
<td>1.077</td>
<td>162.0</td>
</tr>
<tr>
<td>QCISD(T)-fu/6-31G(d)</td>
<td>ANU</td>
<td>−152.064 94</td>
<td>1.512</td>
<td>1.280</td>
<td>1.077</td>
<td>161.9</td>
</tr>
<tr>
<td>QCISD(T)-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.245 11</td>
<td>1.490</td>
<td>1.276</td>
<td>1.074</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD-fc/DZP</td>
<td>CCQC</td>
<td>−152.073 17</td>
<td>1.506</td>
<td>1.285</td>
<td>1.078</td>
<td>161.8</td>
</tr>
<tr>
<td>CCSD-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.220 05</td>
<td>1.481</td>
<td>1.269</td>
<td>1.072</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD-fc/TZ2P</td>
<td>CCQC</td>
<td>−152.155 73</td>
<td>1.505</td>
<td>1.267</td>
<td>1.067</td>
<td>161.3</td>
</tr>
<tr>
<td>CCSD(T)-fu/6-31G(d)</td>
<td>ANU</td>
<td>−152.064 28</td>
<td>1.512</td>
<td>1.279</td>
<td>1.076</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD(T)-fu/6-31G(d,p)</td>
<td>ANU</td>
<td>−152.080 64</td>
<td>1.510</td>
<td>1.280</td>
<td>1.070</td>
<td>161.6</td>
</tr>
<tr>
<td>CCSD(T)-fu/6-31G(df,p)</td>
<td>ANU</td>
<td>−152.162 96</td>
<td>1.500</td>
<td>1.269</td>
<td>1.071</td>
<td>161.8</td>
</tr>
<tr>
<td>CCSD(T)-fc/DZP</td>
<td>CCQC</td>
<td>−152.090 85</td>
<td>1.515</td>
<td>1.292</td>
<td>1.080</td>
<td>161.7</td>
</tr>
<tr>
<td>CCSD(T)-fc/DZP++</td>
<td>CCQC</td>
<td>−152.100 26</td>
<td>1.513</td>
<td>1.291</td>
<td>1.079</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD(T)-fu/6-311G(d,p)</td>
<td>ANU</td>
<td>−152.189 37</td>
<td>1.504</td>
<td>1.280</td>
<td>1.073</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD(T)-fu/6-311G(df,p)</td>
<td>ANU</td>
<td>−152.244 39</td>
<td>1.490</td>
<td>1.276</td>
<td>1.074</td>
<td>161.8</td>
</tr>
<tr>
<td>CCSD(T)-fc/TZ2P</td>
<td>CCQC</td>
<td>−152.181 30</td>
<td>1.518</td>
<td>1.275</td>
<td>1.069</td>
<td>161.2</td>
</tr>
<tr>
<td>CCSD(T)-fc/TZ2P++</td>
<td>CCQC</td>
<td>−152.183 49</td>
<td>1.517</td>
<td>1.275</td>
<td>1.069</td>
<td>161.2</td>
</tr>
<tr>
<td>CCSD(T)-fu/cc-pVTZ$^{e}$</td>
<td>ANU</td>
<td>−152.275 86</td>
<td>1.497</td>
<td>1.270</td>
<td>1.065</td>
<td>161.9</td>
</tr>
<tr>
<td>CCSD(T)-fc/TZ2P(f,d)</td>
<td>CCQC</td>
<td>−152.239 48</td>
<td>1.503</td>
<td>1.273</td>
<td>1.069</td>
<td>161.8</td>
</tr>
</tbody>
</table>

$^{a}$ Energies in hartrees, bond lengths in angströms, bond angles in degrees. $^{b}$ The notation "fu" (full) indicates that all orbitals were included in the correlation treatment while "fc" (frozen-core) indicates that the core orbitals were held frozen. $^{c}$ Calculations based on the 6-31G or CCQC basis sets used 6d and/or 10f, while calculations based on 6-311G or cc-pVTZ used 5d and/or 7f. $^{d}$ ANU: Australian National University, Canberra. CCQC: Center for Computational Quantum Chemistry, Athens. $^{e}$ [4s3p2d1f].

The largest part of the change in geometry occurs between the SCF and either the MP2 or the CISD methods of electron correlation. More sophisticated inclusion of electron correlation has a much smaller effect.

Frequency Predictions. Predictions of the harmonic vibrational frequencies appear in Table 2. Of particular interest is the ring-deformation normal vibrational mode. *It can be seen that the nature of the oxirene stationary point changes, depending on choice of basis set and theoretical procedure!* If one were to use only SCF calculations, the clear conclusion would be that oxirene is a minimum on the surface. Conversely, all of the density functional based approaches indicate that oxirene is a saddle point. For the conventional correlated procedures, one sees a mixture of real and imaginary values for the ring-deformation vibrational mode.

We note initially that the effect of freezing the core in the correlated calculations is very small. For example, the mean absolute difference between the QCISD-fc/6-31G(d) and QCISD-fu/6-31G(d) frequencies is just $3\ \text{cm}^{-1}$, with a largest difference of $13\ \text{cm}^{-1}$.

The drop in the ring-opening harmonic vibrational frequency from RHF/DZP ($445\ \text{cm}^{-1}$) to CISD/DZP ($338\ \text{cm}^{-1}$) to CCSD/DZP ($262\ \text{cm}^{-1}$) has already been noted by Vacek et al.$^{25}$ Inclusion of triple excitations in the correlation treatment has a large effect, further flattening the surface at the $C_{2v}$-symmetry stationary point. For example, for the DZP basis set, there is another drop (to $119\ \text{cm}^{-1}$) in going to the CCSD(T) method of electron correlation. Furthermore, when rather typical basis set improvements [such as from DZP to TZ2P or 6-31G(d,p) to 6-311G(d,p)] are made, we again see a lowering of this vibrational

Oxirene: To Be or Not To Be?
The Journal of Physical Chemistry, Vol. 98, No. 35, 1994 8663

<table><thead><tr><th>TABLE 2: Calculated Harmonic Vibrational Frequencies for the $C_{2v}$-Symmetry Structure of Oxirene$^a$</th><th></th><th>CH symm. stretch ($a_1$)</th><th>CC stretch ($a_1$)</th><th>CO symm. stretch ($a_1$)</th><th>CH symm. rock ($a_1$)</th><th>CH asymm. wag ($a_2$)</th><th>CH symm. wag ($b_1$)</th><th>CH asymm. stretch ($b_2$)</th><th>CH asymm. rock ($b_2$)</th><th>ring deform. ($b_2$)</th></tr><tr><th>level of theory$^{b,c}$</th><th>source$^d$</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>RHF/6-31G(d)</td><td>ANU</td><td>3618</td><td>2004</td><td>1180</td><td>998</td><td>795</td><td>693</td><td>3537</td><td>1095</td><td>440</td></tr><tr><td>RHF/DZP</td><td>CCQC</td><td>3581</td><td>1971</td><td>1170</td><td>994</td><td>786</td><td>673</td><td>3502</td><td>1087</td><td>445</td></tr><tr><td>RHF/DZP++</td><td>CCQC</td><td>3584</td><td>1971</td><td>1171</td><td>995</td><td>789</td><td>675</td><td>3500</td><td>1087</td><td>457</td></tr><tr><td>RHF/6-311G(d,p)</td><td>ANU</td><td>3576</td><td>1978</td><td>1167</td><td>999</td><td>821</td><td>692</td><td>3492</td><td>1096</td><td>441</td></tr><tr><td>RHF/6-311G(df,p)</td><td>ANU</td><td>3575</td><td>1979</td><td>1182</td><td>1002</td><td>826</td><td>693</td><td>3493</td><td>1105</td><td>459</td></tr><tr><td>RHF/TZ2P</td><td>CCQC</td><td>3575</td><td>1969</td><td>1160</td><td>982</td><td>785</td><td>677</td><td>3492</td><td>1094</td><td>416</td></tr><tr><td>RHF/TZ2P++</td><td>CCQC</td><td>3575</td><td>1968</td><td>1159</td><td>982</td><td>781</td><td>674</td><td>3492</td><td>1094</td><td>422</td></tr><tr><td>RHF/cc-pVTZ$^e$</td><td>ANU</td><td>3570</td><td>1976</td><td>1173</td><td>998</td><td>823</td><td>689</td><td>3485</td><td>1106</td><td>446</td></tr><tr><td>RHF/TZ2P(f,d)</td><td>CCQC</td><td>3570</td><td>1975</td><td>1169</td><td>996</td><td>833</td><td>695</td><td>3488</td><td>1105</td><td>446</td></tr><tr><td>RHF/QZ3P(f,d)</td><td>CCQC</td><td>3568</td><td>1976</td><td>1174</td><td>1000</td><td>832</td><td>692</td><td>3487</td><td>1111</td><td>456</td></tr><tr><td>SVWN/6-311G(df,p)</td><td>ANU</td><td>3320</td><td>1810</td><td>1084</td><td>870</td><td>585</td><td>478</td><td>3243</td><td>919</td><td>354$i$</td></tr><tr><td>BLYP/6-311G(d,p)</td><td>ANU</td><td>3315</td><td>1764</td><td>1011</td><td>836</td><td>558</td><td>500</td><td>3244</td><td>903</td><td>394$i$</td></tr><tr><td>BLYP/6-311G(df,p)</td><td>ANU</td><td>3312</td><td>1770</td><td>1022</td><td>840</td><td>569</td><td>499</td><td>3241</td><td>914</td><td>374$i$</td></tr><tr><td>BLYP/6-311+G(2df,p)</td><td>ANU</td><td>3310</td><td>1765</td><td>1009</td><td>837</td><td>604</td><td>513</td><td>3241</td><td>915</td><td>310$i$</td></tr><tr><td>Becke3LYP/6-311G(df,p)</td><td>ANU</td><td>3397</td><td>1833</td><td>1072</td><td>889</td><td>647</td><td>546</td><td>3323</td><td>966</td><td>183$i$</td></tr><tr><td>MP2-fc/6-31G(d)</td><td>ANU</td><td>3458</td><td>1800</td><td>1107</td><td>889</td><td>481</td><td>467</td><td>3390</td><td>950</td><td>42$i$</td></tr><tr><td>MP2-fc/6-311G(d,p)</td><td>ANU</td><td>3445</td><td>1768</td><td>1098</td><td>894</td><td>581</td><td>510</td><td>3375</td><td>955</td><td>128$i$</td></tr><tr><td>MP2-fc/6-311G(df,p)</td><td>ANU</td><td>3442</td><td>1781</td><td>1124</td><td>903</td><td>556</td><td>475</td><td>3372</td><td>970</td><td>129</td></tr><tr><td>MP2-fu/6-311G(df,p)</td><td>ANU</td><td>3454</td><td>1787</td><td>1126</td><td>905</td><td>573</td><td>482</td><td>3384</td><td>974</td><td>135</td></tr><tr><td>MP2-fc/6-311+G(2df,p)</td><td>ANU</td><td>3426</td><td>1775</td><td>1082</td><td>884</td><td>628</td><td>517</td><td>3358</td><td>958</td><td>158</td></tr><tr><td>MP2-fu/cc-pVTZ$^e$</td><td>ANU</td><td>3455</td><td>1785</td><td>1098</td><td>895</td><td>614</td><td>516</td><td>3370</td><td>972</td><td>135</td></tr><tr><td>MP3-fu/6-311G(df,p)</td><td>ANU</td><td>3474</td><td>1843</td><td>1161</td><td>931</td><td>608</td><td>511</td><td>3403</td><td>999</td><td>400</td></tr><tr><td>MP4SDQ-fu/6-311G(df,p)</td><td>ANU</td><td>3455</td><td>1820</td><td>1137</td><td>917</td><td>583</td><td>505</td><td>3383</td><td>988</td><td>227</td></tr><tr><td>MP4-fu/6-311G(df,p)</td><td>ANU</td><td>3425</td><td>1760</td><td>1103</td><td>887</td><td>509</td><td>457</td><td>3356</td><td>958</td><td>207$i$</td></tr><tr><td>CISD-fc/DZP</td><td>CCQC</td><td>3500</td><td>1866</td><td>1134</td><td>932</td><td>652</td><td>561</td><td>3427</td><td>1009</td><td>336</td></tr><tr><td>CISD-fc/TZ2P</td><td>CCQC</td><td>3500</td><td>1873</td><td>1119</td><td>924</td><td>608</td><td>581</td><td>3417</td><td>1011</td><td>310</td></tr><tr><td>CISD-fc/TZ2P(f,d)</td><td>CCQC</td><td>3514</td><td>1894</td><td>1135</td><td>946</td><td>733</td><td>616</td><td>3436</td><td>1032</td><td>364</td></tr><tr><td>QCISD-fc/6-31G(d)</td><td>ANU</td><td>3433</td><td>1818</td><td>1095</td><td>889</td><td>494</td><td>461</td><td>3365</td><td>948</td><td>119</td></tr><tr><td>QCISD-fu/6-31G(d)</td><td>ANU</td><td>3435</td><td>1821</td><td>1097</td><td>891</td><td>499</td><td>474</td><td>3366</td><td>950</td><td>121</td></tr><tr><td>QCISD-fu/6-311G(df,p)</td><td>ANU</td><td>3448</td><td>1815</td><td>1128</td><td>913</td><td>573</td><td>503</td><td>3377</td><td>985</td><td>207</td></tr><tr><td>QCISD(T)-fu/6-31G(d)</td><td>ANU</td><td>3409</td><td>1777</td><td>1079</td><td>868</td><td>448</td><td>389</td><td>3342</td><td>929</td><td>90$i$</td></tr><tr><td>QCISD(T)-fu/6-311G(df,p)</td><td>ANU</td><td>3422</td><td>1769</td><td>1109</td><td>890</td><td>499</td><td>451</td><td>3354</td><td>962</td><td>82</td></tr><tr><td>CCSD-fc/DZP</td><td>CCQC</td><td>3429</td><td>1784</td><td>1099</td><td>890</td><td>552</td><td>487</td><td>3361</td><td>969</td><td>263</td></tr><tr><td>CCSD-fu/6-311G(df,p)</td><td>ANU</td><td>3450</td><td>1821</td><td>1136</td><td>917</td><td>582</td><td>506</td><td>3379</td><td>989</td><td>285</td></tr><tr><td>CCSD-fc/TZ2P</td><td>CCQC</td><td>3420</td><td>1791</td><td>1081</td><td>878</td><td>517</td><td>495</td><td>3341</td><td>965</td><td>228</td></tr><tr><td>CCSD(T)-fu/6-31G(d)</td><td>ANU</td><td>3410</td><td>1781</td><td>1081</td><td>870</td><td>451</td><td>396</td><td>3343</td><td>931</td><td>21</td></tr><tr><td>CCSD(T)-fu/6-31G(d,p)</td><td>ANU</td><td>3449</td><td>1780</td><td>1092</td><td>875</td><td>448</td><td>426</td><td>3381</td><td>948</td><td>48</td></tr><tr><td>CCSD(T)-fu/6-31G(df,p)</td><td>ANU</td><td>3435</td><td>1788</td><td>1105</td><td>895</td><td>522</td><td>493</td><td>3368</td><td>977</td><td>218</td></tr><tr><td>CCSD(T)-fc/DZP</td><td>CCQC</td><td>3405</td><td>1739</td><td>1076</td><td>865</td><td>488</td><td>439</td><td>3339</td><td>947</td><td>119</td></tr><tr><td>CCSD(T)-fc/DZP++</td><td>CCQC</td><td>3410</td><td>1741</td><td>1074</td><td>865</td><td>489</td><td>464</td><td>3336</td><td>945</td><td>165</td></tr><tr><td>CCSD(T)-fc/6-311G(d,p)</td><td>ANU</td><td>3415</td><td>1751</td><td>1080</td><td>878</td><td>518</td><td>481</td><td>3347</td><td>941</td><td>122$i$</td></tr><tr><td>CCSD(T)-fu/6-311G(df,p)</td><td>ANU</td><td>3422</td><td>1772</td><td>1111</td><td>892</td><td>502</td><td>453</td><td>3355</td><td>964</td><td>137</td></tr><tr><td>CCSD(T)-fc/TZ2P</td><td>CCQC</td><td>3392</td><td>1739</td><td>1055</td><td>846</td><td>476</td><td>418</td><td>3314</td><td>936</td><td>85$i$</td></tr><tr><td>CCSD(T)-fc/TZ2P++</td><td>CCQC</td><td>3391</td><td>1738</td><td>1053</td><td>846</td><td></td><td></td><td>3313</td><td>937</td><td>13$i$</td></tr><tr><td>CCSD(T)-fu/cc-pVTZ$^e$</td><td>ANU</td><td>3425</td><td>1775</td><td>1084</td><td>884</td><td>567</td><td>500</td><td>3339</td><td>966</td><td>139</td></tr><tr><td>CCSD(T)-fc/TZ2P(f,d)</td><td>CCQC</td><td>3407</td><td>1763</td><td>1067</td><td>873</td><td>591</td><td>514</td><td>3338</td><td>960</td><td>163</td></tr></tbody></table>

$^{a}$ Harmonic vibrational frequencies in $cm^{-1}$. $^{b}$ The notation "fu" (full) indicates that all orbitals were included in the correlation treatment while "fc" (frozen-core) indicates that the core orbitals were held frozen. $^{c}$ Calculations based on the 6-31G or CCQC basis sets used 6d and/or 10f, while calculations based on 6-311G or cc-pVTZ used 5d and/or 7f. $^{d}$ ANU: Australian National University, Canberra. CCQC: Center for Computational Quantum Chemistry, Athens. $^{e}$ [4s3p2d1f].

frequency. This effect is somewhat additive, and as a result, it can be seen that at the CCSD(T) level with large spd basis sets the surface actually has negative curvature; i.e. oxirene is a saddle point at these levels of theory!

However, all other basis set improvements seem to stabilize oxirene with respect to ring deformation. The addition of diffuse functions to the DZP and TZ2P bases slightly decreases the C-O bond length and stabilizes the mode in question by 12 and $6cm^{-1}$, respectively, on the RHF surfaces and by 56 and $72cm^{-1}$ on the CCSD(T) surfaces. Note also that, although the initial valence and polarization improvement from DZP and TZ2P was destabilizing, an additional improvement from TZ2P(f,d) to QZ3P(f,d) is stabilizing, at least on the RHF surface.

The stabilization of oxirene by higher angular momentum functions is even greater than that by diffuse functions. For example, with the CCSD(T) method, the addition of an f shell to the 6-311G(d,p) basis or f (on C and O) and d (on H) shells to the TZ2P basis has a large effect, restoring positive curvature to the potential surface. With our best theoretical levels, CCSD-(T)-fc/TZ2P(f,d) and CCSD(T)-fu/cc-pVTZ, oxirene is a local minimum on the potential surface with ring-opening frequencies of 163 and $139cm^{-1}$, respectively.

The poor performance of Møller-Plesset perturbation theory for this problem should be noted. One can see rather large fluctuations in the $b_2$ vibrational frequency along the series RHF $\rightarrow$ MP2 $\rightarrow$ MP3 $\rightarrow$ MP4 ($459\rightarrow135\rightarrow400\rightarrow207i cm^{-1}$) for the 6-311G(df,p) basis. The importance of a balanced treatment of triple substitutions is also nicely illustrated by results with the 6-311G(df,p) basis set. MP4 without the triples (MP4SDQ) has a ring-opening frequency of $227cm^{-1}$. This changes dramatically to $207i cm^{-1}$ when triples are included (MP4). MP4 is, however, known$^{69,70}$ to overestimate the importance of the triple substitutions. A more complete treatment of the triples is provided by QCISD(T) for which the ring-opening frequency becomes real ($82cm^{-1}$). CCSD(T) results in a further improvement in the treatment of the triple effects,$^{70}$ and at the CCSD(T)/6-311G-(df,p) level the $b_2$ frequency increases to $137cm^{-1}$. The effect of the inclusion of quadruple excitations$^{71}$ on the geometry and the ring-opening frequency of oxirene would certainly be of interest!

A brief aside should be made concerning the possible importance of a multireference wave function. For all three CISD wave functions constructed in this study, the coefficient of the reference configuration is 0.94. The coefficients for the second most

important configuration (a double excitation from the $2b_1$ $\pi_{CC}$- bonding MO to the $1a_2$ $\pi^*_{CC}$-antibonding MO) are -0.06, -0.05, and -0.04 for increasing-size basis sets. Such contributions from the second configuration imply that single-reference CISD may not be entirely suitable. However, analysis of the coupled-cluster wave functions reveal $T_1$ diagnostic values of 0.014 for all cases. This is less than the suggested threshold of $0.02,^{72}$ implying that most of the dynamical correlation energy is being recovered by the coupled-cluster wave functions. Thus, while CISD results are suggested to be insufficient, coupled-cluster wave functions should be adequate to resolve the problem without resorting to multireference techniques. This last conclusion, of course, only pertains to the oxirene stationary point and does not necessarily apply to the entire isomerization hypersurface.

## Concluding Remarks
The present study has examined the $C_{2v}$-symmetry structure of oxirene with a variety of basis sets and theoretical procedures. The results at the various levels show qualitative differences, specifically with regard to the nature of the stationary point. Density functional methods, fourth-order Møller-Plesset perturbation theory, and CCSD(T) methods with large spd basis sets all show the symmetric structure to be a transition structure along the ring-opening normal coordinate, while other methods show it to be a true minimum. At our highest level of theory, CCSD(T) with basis sets of triple-$\zeta$ quality and including multiple d shells and an f shell on C and O and multiple p shells and a d shell on H, oxirene is a true minimum with a ring-opening frequency of $139-163\ \text{cm}^{-1}$.

The large basis set CCSD(T) calculations may prove prohibitively costly for studying the low-symmetry structures in the oxirene $\rightarrow$ ketene isomerization. A compromise in terms of computational efficiency and accuracy may be provided by the CCSD(T)/6-311G(df,p) level of theory, which predicts a geometry and a ring-opening frequency satisfactorily close to those given by the CCSD(T)/cc-pVTZ and CCSD(T)/TZ2P(f,d) methods.

Acknowledgment. This research was supported by the U.S. Department of Energy, Office of Basic Energy Sciences, Grant No. DE-FG09-87ER13811. G.V. is supported under a U.S. Department of Defense Graduate Fellowship. G.V., J.M.G., Y.Y., and H.F.S. thank Dan Gezelter and William H. Miller for interesting discussions. A.P.S., R.H.N., and L.R. thank the Australian National University Supercomputer Facility for a generous allocation of time on the Fujitsu VP2200.

## References and Notes
(1) (a) Wolff, L. *Justus Liebigs Ann. Chem.* 1902, 325, 129. (b) *Ibid.* 1912, 394, 23.
(2) Meier, H.; Zeller, K.-P. *Angew. Chem. Int. Ed. Engl.* 1975, 14, 32.
(3) (a) Csizmadia, I. G.; Font, J.; Strausz, O. P. *J. Am. Chem. Soc.* 1968, 90, 7360. (b) Thornton, D. E.; Gosavi, R. K.; Strausz, O. P. *J. Am. Chem. Soc.* 1970, 92, 1768.
(4) (a) Matlin, S. A.; Sammes, P. G. *J. Chem. Soc., Chem. Commun.* 1972, 11. (b) Matlin, S. A.; Sammes, P. G. *J. Chem. Soc., Perkin Trans. 1* 1972, 2623. (c) *Ibid.* 1973, 2851.
(5) (a) Huggett, C.; Arnold, R. T.; Taylor, T. I. *J. Am. Chem. Soc.* 1942, 64, 3043. (b) Franzen, V. *Annalen* 1958, 614, 31.
(6) Lewars, E. G. *Chem. Rev.* 1983, 83, 519.
(7) (a) McDonald, R. N.; Schwab, P. A. *J. Am. Chem. Soc.* 1964, 86, 4866. (b) Stille, J. K.; Whitehurst, D. D. *J. Am. Chem. Soc.* 1964, 86, 4871.
(8) Russell, R. L.; Rowland, F. S. *J. Am. Chem. Soc.* 1970, 92, 7508.
(9) Tanigaki, K.; Ebbesen, T. W. *J. Am. Chem. Soc.* 1987, 109, 5883.
(10) (a) Debu, F.; Monnier, M.; Verlaque, P.; Davidovics, G.; Pourcin, J.; Bodot, H.; Aycard, J.-P. *C. R. Acad. Sci. Paris, Ser. 2* 1986, 303, 897. (b) Bachmann, C.; N'Guessan, T. Y.; Debu, F.; Monnier, M.; Pourcin, J.; Aycard, J.-P.; Bodot, H. *J. Am. Chem. Soc.* 1990, 112, 7488.
(11) Hop, C. E. C. A.; Holmes, J. L.; Terlouw, J. K. *J. Am. Chem. Soc.* 1989, 111, 441.
(12) Bouma, W. J.; Gill, P. M. W.; Radom, L. *Org. Mass Spectrom.* 1984, 19, 610.
(13) (a) Dykstra, C. E.; Schaefer, H. F. *J. Am. Chem. Soc.* 1978, 100, 1378. (b) Gallo, M. M.; Hamilton, T. P.; Schaefer, H. F. *J. Am. Chem. Soc.* 1990, 112, 8714. (c) Smith, B. J.; Smernik, R.; Radom, L. *Chem. Phys. Lett.* 1992, 188, 589.
(14) Ervin, K. M.; Ho, J.; Lineberger, W. C. *J. Chem. Phys.* 1989, 91, 5974.
(15) Gilles, M. K.; Lineberger, W. C.; Ervin, K. M. *J. Am. Chem. Soc.* 1993, 115, 1031.
(16) DeLeeuw, B. J.; Fermann, J. T.; Xie, Y.; Schaefer, H. F. *J. Am. Chem. Soc.* 1993, 115, 1039.
(17) Csizmadia, I. G.; Gunning, H. E.; Gosavi, R. K.; Strausz, O. P. *J. Am. Chem. Soc.* 1973, 95, 133.
(18) Dewar, M. J. S.; Ramsden, C. A. *J. Chem. Soc., Chem. Commun.* 1973, 688.
(19) (a) Strausz, O. P.; Gosavi, R. K.; Gunning, H. E. *J. Chem. Phys.* 1977, 67, 3057. (b) Strausz, O. P.; Gosavi, R. K.; Gunning, H. E. *Chem. Phys. Lett.* 1978, 54, 510.
(20) Dykstra, C. E. *J. Chem. Phys.* 1978, 68, 4244.
(21) Baird, N. C.; Taylor, K. F. *J. Am. Chem. Soc.* 1978, 100, 1333.
(22) Strausz, O. P.; Gosavi, R. K.; Denes, A. S.; Csizmadia, I. G. *J. Am. Chem. Soc.* 1976, 98, 4784.
(23) Tanaka, K.; Yoshimine, M. *J. Am. Chem. Soc.* 1980, 102, 7655.
(24) Bouma, W. J.; Nobes, R. H.; Radom, L.; Woodward, C. E. *J. Org. Chem.* 1982, 47, 1869.
(25) Vacek, G.; Colegrove, B. T.; Schaefer, H. F. *Chem. Phys. Lett.* 1991, 177, 468.
(26) (a) Trozzolo, A. M. *Acc. Chem. Res.* 1968, 1, 329. (b) Hutton, R. S.; Manion, M. L.; Roth, H. D.; Wasserman, E. *J. Am. Chem. Soc.* 1974, 96, 4680. (c) Hutton, R. S.; Roth, H. D. *J. Am. Chem. Soc.* 1978, 100, 4324.
(27) (a) Padwa, A.; Layton, R. *Tetrahedron Lett.* 1965, 2167. (b) Jones, M.; Ando, W. *J. Am. Chem. Soc.* 1968, 90, 2200. (c) DoMinh, T.; Strausz, O. P. *J. Am. Chem. Soc.* 1970, 92, 1766.
(28) (a) Novoa, J. J.; McDouall, J. J. W.; Robb, M. A. *J. Chem. Soc., Faraday Trans. 2* 1987, 83, 1629. (b) See also: Gosavi, R. K.; Torres, M.; Strausz, O. P. *Can. J. Chem.* 1991, 69, 1630.
(29) Fowler, J. E.; Vacek, G.; Galbraith, J. M.; Schaefer, H. F. In progress.
(30) (a) Lovejoy, E. R.; Kim, S. K.; Alvarez, R. A.; Moore, C. B. *J. Chem. Phys.* 1991, 95, 4081. (b) Lovejoy, E. R.; Kim, S. K.; Moore, C. B. *Science* 1992, 256, 1541. (c) Lovejoy, E. R.; Moore, C. B. *J. Chem. Phys.* 1993, 98, 7846.
(31) Gezelter, D.; Miller, W. H.; Vacek, G.; Schaefer, H. F. In progress.
(32) Scott, A. P.; Nobes, R. H.; Schaefer, H. F.; Radom, L. *J. Am. Chem. Soc.*, in press.
(33) Gaussian 92/DFT, Revision F.3. Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Gill, P. M. W.; Johnson, B. G.; Wong, M. W.; Foresman, J. B.; Robb, M. A.; Head-Gordon, M.; Replogle, E. S.; Gomperts, R.; Andres, J. L.; Raghavachari, K.; Binkley, J. S.; Gonzales, G.; Martin, R. L.; Fox, D. J.; DeFrees, D. J.; Baker, J.; Stewart, J. J. P.; Pople, J. A. Gaussian Inc., Pittsburgh, PA, 1993.
(34) (a) ACES II, Version 0.2. Stanton, J. F.; Gauss, J.; Watts, J. D.; Lauderdale, W. J.; Bartlett, R. J. Quantum Theory Project, University of Florida, 1992. (b) Stanton, J. F.; Gauss, J.; Watts, J. D.; Lauderdale, W. J.; Bartlett, R. J. *Int. J. Quantum. Chem. Symp.* 1992, 26, 879.
(35) PSI 2.0, Version 8. Seidl, E. T.; Janssen, C. L.; Vacek, G.; Yamaguchi, Y.; Scuseria, G. E.; Lee, T. J.; Allen, W. D.; Remington, R. B.; Scheiner, A. C.; Crawford, T. D.; Sherrill, C. D.; Hamilton, T. P.; Pitzer, R. M.; Xie, Y.; Schaefer, H. F. PSITECH Inc., Watkinsville, GA, 1993.
(36) (a) Hariharan, P. C.; Pople, J. A. *Theor. Chim. Acta* 1973, 28, 213. (b) Krishnan, R.; Binkley, J. S.; Seeger, R.; Pople, J. A. *J. Chem. Phys.* 1980, 72, 650.
(37) (10s5p2d1f)/[4s3p2d1f]: Dunning, T. H. *J. Chem. Phys.* 1989, 90, 1007.
(38) Frisch, M. J.; Pople, J. A.; Binkley, J. S. *J. Chem. Phys.* 1984, 80, 3265.
(39) $\alpha_{\mathrm{f}}(\mathrm{C})=0.8$ and $\alpha_{\mathrm{f}}(\mathrm{O})=1.4$.
(40) (9s5p)/[4s2p], $\alpha_{\mathrm{d}}(\mathrm{C})=0.75$, $\alpha_{\mathrm{d}}(\mathrm{O})=0.85$. (4s)/[2s], $\alpha_{\mathrm{p}}(\mathrm{H})=$ 0.75: Dunning, T. H. *J. Chem. Phys.* 1970, 53, 2823.
(41) Lee, T. J.; Schaefer, H. F. *J. Chem. Phys.* 1985, 83, 1784.
(42) $\alpha_{\mathrm{s}}(\mathrm{C})=0.031$ 069, $\alpha_{\mathrm{p}}(\mathrm{C})=0.036$ 290, $\alpha_{\mathrm{s}}(\mathrm{O})=0.057$ 122, $\alpha_{\mathrm{p}}(\mathrm{O})=$ 0.065 082, and $\alpha_{\mathrm{s}}(\mathrm{H})=0.044$ 150.
(43) (10s6p)/[5s3p], $\alpha_{\mathrm{d}}(\mathrm{C})=1.50$, 0.375, $\alpha_{\mathrm{d}}(\mathrm{O})=1.70$, 0.425. (5s)/[3s], $\alpha_{\mathrm{p}}(\mathrm{H})=1.50$, 0.375: Dunning, T. H. *J. Chem. Phys.* 1971, 55, 716.
(44) $\alpha_{\mathrm{f}}(\mathrm{C})=0.8$, $\alpha_{\mathrm{f}}(\mathrm{O})=1.4$, and $\alpha_{\mathrm{d}}(\mathrm{H})=1.0$.
(45) $\alpha_{\mathrm{s}}(\mathrm{C})=0.048$ 116, $\alpha_{\mathrm{p}}(\mathrm{C})=0.033$ 886, $\alpha_{\mathrm{s}}(\mathrm{O})=0.089$ 929, $\alpha_{\mathrm{p}}(\mathrm{O})=$ 0.058 397, and $\alpha_{\mathrm{s}}(\mathrm{H})=0.030$ 158.
(46) (11s7p)/[6s4p], $\alpha_{\mathrm{d}}(\mathrm{C})=3.0$, 0.75, 0.1875, $\alpha_{\mathrm{d}}(\mathrm{O})=3.4$, 0.85, 0.2125, and $\alpha_{\mathrm{p}}(\mathrm{H})=3.0$, 0.75, 0.1875: Van Duijneveldt, F. B. IBM Report 945, Tables A2 and A34.
(47) Pulay, P. *Adv. Chem. Phys.* 1987, 69, 241.
(48) Pople, J. A.; Krishnan, R.; Schlegel, H. B.; Binkley, J. S. *Int. J. Quantum Chem. Symp.* 1979, 13, 225.
(49) (a) Frisch, M. J.; Head-Gordon, M.; Pople, J. A. *Chem. Phys. Lett.* 1990, 166, 275. (b) *Ibid.* 1990, 166, 281.
(50) Fitzgerald, G.; Harrison, R.; Laidig, W. D.; Bartlett, R. J. *J. Chem. Phys.* 1985, 82, 4375.
(51) (a) Gauss, J.; Cremer, D. *Chem. Phys. Lett.* 1987, 138, 131. (b) *Ibid.* 1988, 153, 303.
(52) Brooks, B. R.; Laidig, W. D.; Saxe, P.; Goddard, J. D.; Yamaguchi, Y.; Schaefer, H. F. *J. Chem. Phys.* 1980, 72, 4652.
(53) Rice, J. E.; Amos, R. D.; Handy, N. C.; Lee, T. J.; Schaefer, H. F. *J. Chem. Phys.* 1986, 85, 963.

(54) (a) Scheiner, A. C.; Scuseria, G. E.; Rice, J. E.; Lee, T. J.; Schaefer, H. F. J. Chem. Phys. 1987, 87, 5361. (b) Scuseria, G. E.; Janssen, C. L.; Schaefer, H. F. J. Chem. Phys. 1988, 89, 7383. (c) Gauss, J.; Stanton, J. F.; Bartlett, R. J. J. Chem. Phys. 1991, 95, 2623. (d) Rendell, A. P.; Lee, T. J. J. Chem. Phys. 1991, 94, 6219.

(55) (a) Scuseria, G. J. Chem. Phys. 1991, 94, 442. (b) Salter, E. A.; Trucks, G. W.; Bartlett, R. J. J. Chem. Phys. 1989, 90, 1752. (c) Lee, T. J.; Rendell, A. J. Chem. Phys. 1991, 94, 6229.

(56) Gauss, J.; Cremer, D. Chem. Phys. Lett. 1988, 150, 280.

(57) Gauss, J.; Cremer, D. Chem. Phys. Lett. 1989, 163, 549.

(58) Johnson, B. G.; Gill, P. M. W.; Pople, J. A. J. Chem. Phys. 1992, 97, 7846.

(59) Gill, P. M. W.; Johnson, B. G.; Pople, J. A.; Frisch, M. J. Chem. Phys. Lett. 1992, 197, 499.

(60) Becke, A. D. To be published.

(61) For the DFT calculations, the default SG-1 grid was used: Gill, P. M. W.; Johnson, B. G.; Pople, J. A. Chem. Phys. Lett. 1993, 209, 506.

(62) Saxe, P.; Fox, D. J.; Schaefer, H. F.; Handy, N. C. J. Chem. Phys. 1982, 77, 5584.

(63) (a) Johnson, B. G.; Frisch, M. J. Chem. Phys. Lett. 1993, 216, 133. (b) See also: Handy, N. C.; Tozer, D. J.; Laming, G. J.; Murray, C. W.; Amos, R. D. Isr. J. Chem. 1993, 33, 331.

(64) Osamura, Y.; Yamaguchi, Y.; Saxe, P.; Vincent, M. A.; Schaefer, H. F. Chem. Phys. 1982, 72, 131.

(65) Osamura, Y.; Yamaguchi, Y.; Saxe, P.; Fox, D. J.; Vincent, M. A.; Schaefer, H. F. J. Mol. Struct. 1983, 103, 183.

(66) Schlegel, H. B.; Binkley, J. S.; Pople, J. A. J. Chem. Phys. 1984, 80, 1976.

(67) Hehre, W. J.; Radom, L.; Schleyer, P. v. R.; Pople, J. A. Ab Initio Molecular Orbital Theory; Wiley: New York, 1986.

(68) (a) Thomas, J. R.; DeLeeuw, B. J.; Vacek, G.; Schaefer, H. F. J. Chem. Phys. 1993, 98, 1336. (b) Thomas, J. R.; DeLeeuw, B. J.; Vacek, G.; Crawford, T. D.; Yamaguchi, Y.; Schaefer, H. F. J. Chem. Phys. 1993, 99, 403. (c) DeLeeuw, B. J.; Thomas, J. R.; Vacek, G.; Yamaguchi, Y.; Schaefer, H. F. To be published.

(69) Pople, J. A.; Head-Gordon, M.; Raghavachari, K. Int. J. Quantum Chem. Symp. 1988, 22, 377.

(70) See for example: (a) He, Z.; Cremer, D. Int. J. Quantum Chem. Symp. 1991, 25, 43. (b) He, Z.; Cremer, D. Theor. Chim. Acta 1993, 85, 305.

(71) Raghavachari, K.; Pople, J. A.; Replogle, E. S.; Head-Gordon, M. J. Phys. Chem. 1993, 94, 5579.

(72) Lee, T. J.; Taylor, P. R. Int. J. Quantum Chem. Symp. 1989, 23, 199.