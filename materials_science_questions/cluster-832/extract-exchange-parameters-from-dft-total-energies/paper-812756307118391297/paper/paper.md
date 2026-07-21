# Electronic and magnetic structure of $KNiF_{3}$ perovskite

J. M. Ricart
Department of Chemistry, Universitat Rovira i Virgili, Plaza Imperial Tarraco 1, 43005 Tarragona, Spain

R. Dovesi and C. Roetti
Department of Inorganic, Physical and Materials Chemistry, University of Torino, via P. Giuria 5, I-10125 Torino, Italy

V. R. Saunders
CLRC Daresbury Laboratory, Daresbury, Warrington WA4 4AD, United Kingdom

(Received 9 November 1994)

The ground-state electronic structure of the ferromagnetic and antiferromagnetic phases of $KNiF_{3}$ has been investigated using the $ab$ initio periodic Hartree-Fock approach. The system is a wide-gap insulator. The antiferromagnetic phase is correctly predicted to be more stable than the ferromagnetic phase (0.031 eV per Ni pair at the experimental geometry). The energy difference between these phases is shown to obey a $d^{-12}$ ($d$ is the shortest Ni-Ni distance) power law, as suggested in the literature. The superexchange interaction turns out to be additive with respect to the number of Ni-Ni neighbors, as assumed in model spin Hamiltonians. Elastic properties, charge, and spin-density maps, and density of states plots are reported.

## I. INTRODUCTION

In the past ten years $ab$ initio or first-principle quantum-mechanical methods have become reliable tools for the investigation of the electronic and structural properties of important classes of crystalline compounds, such as semiconductors, ceramics, and silicates. Properties related to the total energy of the system or to its derivatives, such as the formation energy, the equilibrium geometry, and the elastic constants can now be obtained from standard computer programs easily available to the scientific community. $^{1,2}$ The quality of the results is reasonably good; the error with respect to experiment is of the order of 5%, 1%, 10% for the formation energy, linear geometrical parameters, and elastic properties, $^{1,3,4}$ respectively.

For other classes of compounds and/or other properties, the situation is less favorable. A typical area where $ab$ initio methods seem to produce less accurate results is that of ionic insulators containing transition-metal (TM) atoms, in particular, with reference to their magnetic properties. Prototypes in this family are the simple TM oxides $XO$; the family is very large and extremely important in various fields (from materials science to geology) and includes complex oxides ($Fe_{2}O_{3}$, for example), halides, sulfides, and silicates. Nearly all the $ab$ initio periodic investigations of these systems have been based on the density-functional scheme, mostly in the local approximation (LDA); $^{5-13}$ in many cases, the system turns out to be metallic at the experimental geometry, or to present a very small gap $^{6,7}$ that disappears under small deformation $^{7}$ or compression of the unit cell, in contradiction with experimental evidence. As a consequence, very important properties of the system, such as the relative stabilities of the ferromagnetic (FM), antiferromagnetic (AFM), and nonmagnetic (NM) states, obtained from LDA calculations, are incorrect. Considerable effort has been devoted recently to modifications of the LDA scheme [SIC-LSD; $^{8}$ LDA+U (Refs. 9 and 10)] able to produce a gap in the band structure, as a preliminary and necessary step for obtaining correct ground-state magnetic properties.

The local nature of the superexchange interaction, and the ionic nature of the systems here considered, suggested the use of a cluster approach in the study of their electronic and magnetic properties. $^{14-21}$ The cluster contains very few atoms, in general one or two TM atoms, and is embedded in the electrostatic field created by a set of point charges simulating the rest of the crystal. The advantages of such a scheme are related to the possibility of using sophisticated many-body techniques, able to take into account most of the correlation effects; usually they are based on the Hartree-Fock Hamiltonian, and, therefore, describe correctly the exchange interaction; pure eigenstates of the spin operators are obtained. The fundamental limit of such an approach, in particular, when used to describe bulk (rather than atomiclike, such as the $d$-$d$ spectrum $^{18,19}$) properties, is related to the finite cluster size; results obtained with clusters of different size and shape $^{14-16}$ seem to indicate that border effects have a crucial influence on the results.

A third strategy is used in the present study, based on the periodic Hartree-Fock (HF) scheme as implemented in the CRYSTAL code. $^{1,22,23}$ In the periodic scheme border effects are absent, and the HF Hamiltonian correctly describes the exchange interactions that are largely re-

sponsible for the higher stability of the AFM with respect to the FM phase, as experimentally observed in many of these materials at low temperature. The unrestricted Hartree-Fock (UHF) scheme, which allows the investiga- tion of open shell structures, has been recently imple- mented in the CRYSTAL code. $^{24,25}$ Previous applications to MnO and NiO (Refs. 24, 26, and 27) and $Fe_{2} O_{3}$ (Ref.28) provided encouraging results: the systems are found to be large gap insulators both in the FM and AFMstates; the AFM solution is more stable than the FM one; for MnO and NiO the ratio between the FM-AFM ener- gy differences for the two systems is very close to the ra- tio between the corresponding Néel temperatures; also, such a delicate quantity as the magnetostriction effect, that is the deviation from the ideal cubic angle of thedouble AFM cell, was correctly reproduced $(0.5^{\circ}$ and $0.1^{\circ}$ for MnO and NiO, respectively, to be compared with $0.6^{\circ}$  and $0.1^{\circ}$ from experiment). It must be remembered that the UHF solutions are eigenfunctions of the $S_{z}$ operator, not of $S^{2}$ . The results for $NiO, MnO$ , and $Fe_{2} O_{3}$ suggest that the spin contamination in the $S=S_{ max }$ (FM) and S=0 (AFM) states is not very large, or largely cancels in the energy differences, and that correlation effects, that are disregarded at the HF level, do not play a crucial role in determining the FM-AFM energy difference.
In the present paper, we apply the periodic UHF scheme to another magnetic insulator: $KNiF_{3}. KNiF_{3}$ is a prototype system with a $180^{\circ}$ cation-anion-cation superexchange path. It has been the object of many experi- mental $^{29-33}$ and theoretical $^{5,15-17,34-36}$ investigations. Of particular importance are the review by de Jongh and Miedema $^{35}$ and the paper by de Jongh and Block $^{36}$ devoted to the $180^{\circ}$ superexchange interaction in the $XMF_{3}$  and $X_{2} MF_{4}$ compounds $(X=K, Rb, Tl$ and $M=Mn, Co$ , Ni), where the available experimental data for the mag- netic coupling constants $J$ of the Heisenberg and Ising models, are collected and discussed. The aim of the present paper is to investigate the structural, electronic, and magnetic properties of $KNiF_{3}$ . In particular, with reference to the magnetic properties, we explore the rela- tive stability of the NM, FM, and AFM phases; we dis- cuss the additivity of the superexchange interaction and compare the calculated and experimental $^{35,36}$ magnetic coupling constant $J$ ; we investigate its variation with the Ni-Ni distance and compare with the power law pro-posed by de Jongh and Block. $^{36}$
The structure of $KNiF_{3}$ perovskite is a simple cubic ar ray of $NiF_{6}$ octahedra (see Fig. 1). The $K^{+}$ ions fill the empty space (dodecahedra) between the octahedra. The FM unit cell is shown in Fig. 1, on the left. The Ni-F dis- tance is $a / 2$ . There are six second-nearest-neighbor $Ni$ atoms of the central $Ni$ atoms; the $Ni-Ni$ distance is $a$ . At low temperature $KNiF_{3}$ is antiferromagnetic; the AFM structure consists of (111) sheets of $Ni$ atoms of common spin, the spin alternating between the sheets (see Fig. 1 at the center); as a consequence, each $Ni$ atom with a given spin is surrounded by six $Ni$ atoms with opposite spin. The Néel temperature is between 246 (Ref. 36) and253 K.31
## II. COMPUTATIONAL DETAILS
The implementation of the $a b$ initio self-consistent field (SCF) Hartree-Fock linear combination of atomic orbitals computational scheme for periodic systems within the CRYSTAL code $^{1}$ has been described in previous papers. $^{22,23}$ For comparison of AFM and FM energies, whose difference range between $10^{-3}$ and $10^{-4}$ hartree per double cell as a function of the lattice parameter, high numerical accuracy is required. Therefore, values of7, 7, 7, 7, and 14 have been used for the parameters con- trolling the direct space summations for the Coulomb and exchange series (see Refs. 1, 22, and 23 for more de- tails); the reciprocal space integration was performed by sampling the Brillouin zone at a regular set of points defined by a shrinking factor, IS, of 8 ( $29 k$ points); the energy difference with respect to a calculation performed with IS $=12$ is less than $10^{-7}$ hartree/cell. The energy difference between the FM state evaluated with the single and the double cell (the latter is necessary for the AFM calculations) is less than $10^{-7}$ hartree/cell.
Extended Gaussian basis sets composed of 27, 17, and13 atomic orbitals, reported in Table I have been used for $Ni, K$ , and $F$ , respectively, where each orbital is a linear combination (contraction) of Gaussian-type functions. The basis set has been optimized (exponents andcoefficients) in previous studies (see Refs. 27, 37, and 38 for $Ni, K$ , and $F$ , respectively). The outer $s p$ Gaussian of the three ions, and the outer $d$ Gaussian for $Ni$ have been reoptimized by minimizing the bulk energy at the experi- mental volume; the total-energy gain was, however, quite small (about 1 millihartree/atom), and we preferred to maintain unaltered the original basis set in the optimiza- tion of the geometry. However, in order to check the influence of basis set improvements on the very small FM-AFM energy difference, calculations have been per-
![](./images/812756307118391297_1.jpg)
FIG. 1. The cubic unit cell of KNiF3. The ferromagnetic (FM, left) and two possible antiferro- magnetic (AFM, center, and AFM', right) structures are shown. In the central figure, the dashed lines connect $Ni$ atomswith the same spin in the (111) plane.

<table><caption>TABLE I. Exponents and coefficients of the contracted Gaussian-type basis functions used for the present work. Coefficients multiply individually normalized basis functions.</caption>
<tbody><tr><th rowspan="2">Shell<br>type</th><th colspan="3">Ni</th><th colspan="3">K</th><th colspan="3">F</th></tr><tr><th>Exponent</th><th colspan="2">Coefficient<br>s(d) p</th><th>Exponent</th><th colspan="2">Coefficient<br>s p</th><th>Exponent</th><th colspan="2">Coefficient<br>s p</th></tr><tr><td rowspan="9">s</td><td>36 7916.</td><td>0.000 227</td><td></td><td>172 500.</td><td>0.000 22</td><td></td><td>13770.</td><td>0.000 877</td><td></td></tr><tr><td>52 493.9</td><td>0.001 929</td><td></td><td>24320.</td><td>0.001 92</td><td></td><td>1590.</td><td>0.009 15</td><td></td></tr><tr><td>11 175.8</td><td>0.0111</td><td></td><td>5140.</td><td>0.011 09</td><td></td><td>326.5</td><td>0.0486</td><td></td></tr><tr><td>2925.4</td><td>0.05</td><td></td><td>1343.9</td><td>0.049 92</td><td></td><td>91.66</td><td>0.1691</td><td></td></tr><tr><td>882.875</td><td>0.1703</td><td></td><td>404.5</td><td>0.1702</td><td></td><td>30.46</td><td>0.3708</td><td></td></tr><tr><td>305.538</td><td>0.369</td><td></td><td>139.4</td><td>0.3679</td><td></td><td>11.50</td><td>0.41649</td><td></td></tr><tr><td>119.551</td><td>0.4035</td><td></td><td>54.39</td><td>0.4036</td><td></td><td>4.76</td><td>0.1306</td><td></td></tr><tr><td>49.9247</td><td>0.1426</td><td></td><td>22.71</td><td>0.1459</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">sp</td><td>924.525</td><td>−0.0052</td><td>0.0086</td><td>402.0</td><td>−0.006 03</td><td>0.008 41</td><td>19</td><td>−0.1094</td><td>0.1244</td></tr><tr><td>223.044</td><td>−0.0679</td><td>0.0609</td><td>93.5</td><td>−0.0805</td><td>0.0602</td><td>4.53</td><td>−0.1289</td><td>0.5323</td></tr><tr><td></td><td>74.4211</td><td>−0.1319</td><td>0.2135</td><td>30.75</td><td>−0.1094</td><td>0.2117</td><td></td><td></td><td></td></tr><tr><td></td><td>29.6211</td><td>0.2576</td><td>0.3944</td><td>11.92</td><td>0.258</td><td>0.3726</td><td></td><td></td><td></td></tr><tr><td></td><td>12.4721</td><td>0.6357</td><td>0.3973</td><td>5.167</td><td>0.684</td><td>0.4022</td><td></td><td></td><td></td></tr><tr><td></td><td>4.2461</td><td>0.2838</td><td>0.2586</td><td>1.582</td><td>0.399</td><td>0.186</td><td></td><td></td><td></td></tr><tr><td rowspan="4">sp</td><td>56.6581</td><td>0.0124</td><td>−0.018</td><td>17.35</td><td>−0.0074</td><td>−0.0321</td><td>1.387</td><td>1.0</td><td>1.0</td></tr><tr><td>21.2063</td><td>−0.2218</td><td>−0.08</td><td>7.55</td><td>−0.129</td><td>−0.062</td><td></td><td></td><td></td></tr><tr><td>8.4914</td><td>−0.8713</td><td>0.2089</td><td>2.939</td><td>−0.6834</td><td>0.1691</td><td></td><td></td><td></td></tr><tr><td>3.6152</td><td>1.0285</td><td>1.255</td><td>1.19</td><td>1.08</td><td>1.500</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>0.674</td><td>1.03</td><td>1.060</td><td></td><td></td><td></td></tr><tr><td>sp</td><td>1.5145</td><td>1.0</td><td>1.0</td><td>0.389</td><td>1.0</td><td>1.0</td><td>0.44</td><td>1.0</td><td>1.0</td></tr><tr><td>sp</td><td>0.6144</td><td>1.0</td><td>1.0</td><td>0.216</td><td>1.0</td><td>1.0</td><td>0.179</td><td>1.0</td><td>1.0</td></tr><tr><td rowspan="3">d</td><td>41.08</td><td>0.0405</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11.413</td><td>0.2022</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.8561</td><td>0.4338</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1.3302</td><td>0.4897</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>d</td><td>0.411</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

formed at the experimental geometry by (i) adding $d$ orbitals on F and K; (ii) using the optimized exponent for the most diffuse $sp$ shell for F; (iii) adding a diffuse $sp$ shell on Ni; (iv) using a 5-1 G $d$ basis for Ni, instead of the 4-1 G contraction given in Table I. The results, reported in Table II show that the FM-AFM energy difference is totally insensitive to basis sets improvements, which on the other hand lower the total energy of the system by non-negligible amounts. It should be noticed that in the case of the 5-1G contraction for the nickel $d$ shell the energy lowering is largely due to the improvement of the inner part of the shell, not to the outer part involved in the bond, as shown by the corresponding isolated atom energy lowering, which is about 95% of that for the bulk.

## III. RESULTS AND DISCUSSION

### A. The structural data

The calculated and experimental lattice parameter, bulk modulus, and elastic constants are given in Table

<table><caption>TABLE II. Effect of basis set modifications on the total energy (in hartree) of the ferromagnetic and antiferromagnetic states, and on their difference $\Delta E$. DE is the energy difference with respect to the first row energy (Case 1). Indications such as $2 + d(\text{F}) = 0.7$ mean that the basis set specified for Case 2, plus a $d$ shell on F with exponent 0.7 bohr$^{-2}$ has been used. Case 5 refers to a calculation in which a 5-1G basis has been used for the $d$ electrons on Ni, instead of the 4-1G basis reported in Table I. DE and $\Delta E$ in eV.</caption>
<tbody><tr><th rowspan="2">Case</th><th rowspan="2">Basis set</th><th colspan="2">Total energy<br>$2 \times$ FM</th><th colspan="2">Total energy<br>AFM</th><th rowspan="2">$\Delta E$</th></tr><tr><th></th><th>DE</th><th></th><th>DE</th></tr><tr><td>1</td><td>as in Table I</td><td>−4809.226 005</td><td></td><td>−4809.227 141</td><td></td><td>0.031</td></tr><tr><td>2</td><td>1 with $sp(\text{F}) = 0.149$</td><td>−4809.228 728</td><td>0.074</td><td>−4809.229 870</td><td>0.074</td><td>0.031</td></tr><tr><td>3</td><td>$2 + d(\text{F}) = 0.7$</td><td>−4809.236 750</td><td>0.293</td><td>−4809.237 893</td><td>0.293</td><td>0.031</td></tr><tr><td>4</td><td>$3 + d(\text{K}) = 0.4$</td><td>−4809.238 018</td><td>0.327</td><td>−4809.239 196</td><td>0.328</td><td>0.032</td></tr><tr><td>5</td><td>$2 + d(\text{Ni}) = 0.235$</td><td>−4809.275 270</td><td>1.341</td><td>−4809.276 389</td><td>1.340</td><td>0.030</td></tr><tr><td>6</td><td>$2 + sp(\text{Ni}) = 0.25$</td><td>−4809.236 752</td><td>0.293</td><td>4809.237 893</td><td>0.293</td><td>0.031</td></tr></tbody></table>

<table>
<caption>TABLE III. Calculated and experimental equilibrium lattice parameter ($a_0$), bulk modulus ($B$), and elastic constants ($C_{ij}$).</caption>
<tbody><tr><th></th><td>Calculated</td><td>Experimental</td></tr>
<tr><th>$a_0$ (Å)</th><td>4.10</td><td>4.01ª</td></tr>
<tr><th>$B$ (GPa)</th><td>79</td><td>85</td></tr>
<tr><th>$C_{11}$ (GPa)</th><td>168</td><td>158ᵇ</td></tr>
<tr><th>$C_{12}$ (GPa)</th><td>60</td><td>48.5ᵇ</td></tr>
<tr><th>$C_{44}$ (GPa)</th><td>46</td><td>40.3ᵇ</td></tr>
</tbody>
</table>
ªReference 20.
ᵇReference 33.

III. The lattice parameter is overestimated by about 2%, in line with the results for MnO and NiO (Refs. 26 and 27), CaO,³ K₂O.³⁷ The bulk modulus and the elastic constants, evaluated at the calculated equilibrium geometry, are in satisfactory agreement with the experimental room-temperature results. ³³

### B. The magnetic properties
In Table IV the total energy of the NM, FM, and AFM states, evaluated at the experimental geometry, are reported. The AFM solution is more stable than the FM solution by 0.03 eV per Ni pair, whereas the NM solutions are less stable by many eV. The FM and the AFM solutions are characterized by large energy gaps (see later on), whereas one of the NM solutions is metallic. The stability order remains unaltered when the crystal is subjected to large geometry modifications (tetragonal and trigonal unit-cell deformations; isotropic compression and expansion), although obviously the energy differences change as a function of these modifications. Metallic states, that often in LDA calculations are the most stable ones,¹² or have energies very close to those of the AFM insulating states, in the present approach are far less stable than the AFM, and also the FM solution.

The energy difference $\Delta E$ can be related to experimental data obtained with various techniques. The experimental results are usually expressed in terms of the magnetic coupling constants $J$ of a model (Heisenberg or Ising) spin Hamiltonian; the $-J/k_B$ values ($k_B$ is Boltzman's constant) collected by de Jongh and Block,³⁶ range from 44 (Ref. 34) to 51 K.³⁰

If we refer to the Ising model, the following relation holds between $J$ and $\Delta E$:
$$
\Delta E=2zS^{2}|J|,
$$
where $z$ is the number of Ni second neighbors with opposite spin (6 in AFM and 2 in AFM') and $S$ is the total spin moment ($S=1$ in the present case). The resulting calculated $J$ value is 29.8 K, that is something between 58 and 68% of the experimental value. The discrepancy can, in principle, be attributed to many factors: (i) inadequacy of the model adopted in going from the calculated $\Delta E$ to $J$ through the Ising model and (ii) from the experimental data to $J$; inadequacy of the present scheme because (iii) the UHF solutions are eigenfunctions of $S_z$, not of $\mathbf{S}^2$; and (iv) correlation effects are disregarded at the HF level. As regards point (iv), the correlation energy of the FM and AFM states has been evaluated with a correlation-only density functional scheme, by applying the gradient corrected formula proposed by Perdew et al.³⁹ to the HF electron density. It turns out that the AFM-FM energy difference is increased by about 10% (0.003 eV). At the moment we are unable to estimate the importance of the other factors listed above. The data of Table II exclude any basis set influence on $\Delta E$.

The data in Table IV can be used to check the hypothesis of additivity of the superexchange interaction, which is implicit in the Ising (factor $z$ in the equation above), as well as in the Heisenberg models. In this table, the energies of two AFM states (AFM and AFM') are reported. The spin ordering is shown in Fig. 1: in AFM, each Ni atom is surrounded by six Ni atoms with opposite spin; in AFM' four neighbors have the same spin and two have opposite spin. The ratio between the two $\Delta E$ values is 2.97, very close to the theoretical $\frac{6}{2}$ value resulting from additivity. We can go a bit further, and assuming the additivity of the superexchange interaction, we can evaluate from the data of Table IV the value of $J_2$, the next-nearest neighbors (NNN) Ni-Ni interaction. In AFM, the NNN have the same spin as the central atom, so that in this case $\Delta E$ is simply six times the single first-neighbors Ni-Ni interaction; on the other hand, there are four NNN with parallel and eight with opposite spin; disregarding longer-range contributions, we obtain from these data 0.005 15 and 0.000 015 eV for a single first neighbor and NNN interaction (they have the same sign). The resulting $J_2/J_1$ ratio is 0.29%, in reasonable agreement with the experimental estimate of 0.5% of Yamaguchi and Sakamoto.³²

de Jongh and Block,³⁶ on the basis of the experimental $J$ values for a set of $X\mathrm{NiF}_{3}$ and $X_{2}\mathrm{NiF}_{4}$ compounds

<table>
<caption>TABLE IV. Total energy per two formula units (in hartree) at the experimental geometry. NM, FM, and AFM indicate nonmagnetic, ferromagnetic, and antiferromagnetic solutions, respectively. $\Delta E$ is the energy difference (in eV) with respect to the FM case. $\sigma=2S_z$/cell.</caption>
<tbody><tr><th>State</th><th>$\sigma$</th><th>Total energy</th><th>$\Delta E$</th></tr>
<tr><td>FM $t_{2g}^{6}e_{g}^{2}$</td><td>2</td><td>−4809.226 005</td><td></td></tr>
<tr><td>NM $t_{2g}^{6}e_{g}^{2}$</td><td>0</td><td>−4808.316 716</td><td>+24.74</td></tr>
<tr><td>NM closed shell</td><td>0</td><td>−4808.330 32</td><td>+25.18</td></tr>
<tr><td>AFM $t_{2g}^{6}e_{g}^{2}$</td><td>0</td><td>−4809.227 141</td><td>−0.030 91</td></tr>
<tr><td>AFM' $t_{2g}^{6}e_{g}^{2}$</td><td>0</td><td>−4809.226 388</td><td>−0.010 42</td></tr>
</tbody>
</table>

![](./images/812756307118391297_2.jpg)

FIG. 2. Energy difference per two molecular units between the ferromagnetic and the antiferromagnetic phases as a function of the lattice parameter. Three interpolating functions are shown. Note that the energy scale in the figure is in millihartree, while the coefficients in the interpolating formulas are in hartree.

$(X=\mathrm{K}, \mathrm{Rb}, \mathrm{Tl})$ with the same Ni-F coordination and electronic structure, but different Ni-F distances, suggested a $d^{-12}$ power-law dependence of $J$ on the Ni-Ni distance $d$. In Fig. 2, the calculated $\Delta E$ points are reported, together with three interpolating functions. It is shown that in the case of the power law the exponent, 12.2, is very close to that suggested by de Jongh and Block; however, at short distances (much shorter than these taken into account in Ref. 36), the calculated $\Delta E$ values deviate from the $d^{-12}$ law.

In the recent literature, we were able to find only one $a b$ initio study of the magnetic coupling constant $J$ of $\mathrm{KNiF}_{3}$. Illas et al., in a series of papers, $^{14-17}$ investigated the energy differences between several spin states in the $\left(\mathrm{Ni}_{2} \mathrm{~F}\right)^{3+}$ and $\left(\mathrm{Ni}_{2} \mathrm{~F}_{11}\right)^{7-}$ clusters and related them to the magnetic coupling constant $J$. They used various basis sets and adopted different strategies of increasing complexity (and cost) for the treatment of the interelectronic correlation. Test calculations were performed also with the $\left(\mathrm{Ni}_{4} \mathrm{~F}_{4}\right)^{8+}$ cluster. The clusters were embedded in a lattice of total ion potentials and point charges simulating the Madelung potential. The results were very stable with respect to the basis set, whereas changes as large as $100 \%$ were observed in going from the cluster with a single fluorine atom to the one $\left(\mathrm{Ni}_{2} \mathrm{~F}_{11}\right)$ in which all the first neighbors of the $\mathrm{Ni}$ atoms were treated quantum mechanically, or when the more expensive SCI(CAS) correlation scheme was used instead of the cheaper CASCI (See Ref. 15 for the meaning of the acronyms). The best $J$ value (obtained with the $\mathrm{Ni}_{2} \mathrm{~F}_{11}$ cluster and with the most sophisticated treatment of correlation) is about $50 \%$ of the experimental value. The authors suggests that collective effects (synergy of the Ni-Ni interactions) might play a crucial role in determining the experimental $J$ value. Unfortunately they did not perform cluster calculations at the same level as the present ones, $^{40}$ that is with a SCF-UHF scheme, that would allow us to draw conclusions on the relative importance of the crystalline effects, taken fully into account in the present study and approximated in the cluster calculations (through the point-charge embedding technique), and of electronic

TABLE V. Mulliken charges and bond population data (in electrons) for the ferromagnetic (FM) and the antiferromagnetic (AFM) solutions. $Q$ is the atomic net charge; $q(3 d)$ is the electron population of the $d$ orbitals; $\delta n_{s}$ and $\delta n_{s}(3 d)$ are the corresponding spin quantities. In the AFM case, data for only one spin type of atoms are reported.

|          |          FM           |          |          AFM           |          |
| :------- | :-------------------: | :------: | :-------------------: | :------: |
|          |          Ni           |    K     |          Ni           |    K     |
| $Q$      |        $+1.87$        | $+1.00$  |        $+1.87$        | $+1.00$  |
| $q(3 d)$ |         $8.09$        |          |         $8.09$        |          |
| $\delta n_{s}$ |         $1.95$        |  $0.00$  |         $1.95$        |  $0.00$  |
| $\delta n_{s}(3 d)$ |         $1.95$        |          |         $1.95$        |          |
|          |           F           |          |           F           |          |
| $Q$      |        $-0.96$        |          |        $-0.96$        |          |
| $q(3 d)$ |                       |          |                       |          |
| $\delta n_{s}$ |        $-0.02$        |          |         $0.00$        |          |
| $\delta n_{s}(3 d)$ |                       |          |                       |          |

![](./images/812756307118391297_3.jpg)

FIG. 3. Total charge-density map in a (001) plane (left) through the Ni and F atoms, and in a (110) plane (right) through the three type of atoms. The separation between contiguous isodensity curves is $0.01 e / \mathrm{bohr}^{3}$; the innermost curves in the atomic region correspond to $0.15 e / \mathrm{bohr}$ (Ref. 3).

![](./images/812756307118391297_4.jpg)

FIG. 4. Difference charge-density maps. Sections as in previous figure. The difference between the bulk density and the density obtained as a superposition of ions is reported. The ionic solutions have been obtained with the same basis sets used for the periodic calculations. The separation between contiguous isodensity curves is $0.005\ e/$bohr$^3$. The function is truncated in the core regions at $\pm0.05\ e/$bohr$^3$. Continuous, dashed, and dot-dashed lines correspond to positive, negative, and zero values, respectively.

correlation, that has been taken into account in a very approximate way in the present study by the $a$ posteriori density-functional estimate, and which appears from the results of Illas et al. to play an important role in determining the magnitude of the FM-AFM energy difference.

### C. The electronic structure
$KNiF_3$ is a nearly fully ionic insulator. The net charges, evaluated according to a Mulliken scheme and reported in Table V, are very close to the formal ones ($Ni^{2+}$, $K^+$, and $F^-$). The Ni $d$ population is very close to eight, the excess being due to overlap terms with neighboring atoms; the population of each $t_{2g}d$ orbital is exactly 2; that of each $e_g d$ orbital is slightly larger than 1.

The fully ionic structure is confirmed by the Mulliken bond populations data: 0.001, 0.000, and $-0.003$ electrons for Ni-F, Ni-K, and K-F, respectively (we recall that covalent and ionic bonds are characterized by large and very small/null bond populations, respectively, and

![](./images/812756307118391297_5.jpg)

FIG. 5. Spin-density maps for the ferromagnetic solution; sections, symbols, and scale as in previous figure.

![](./images/812756307118391297_6.jpg)

FIG. 6. Spin-density maps for the antiferromagnetic solution; sections, symbols, and scale as in Fig. 4.

that short-range repulsion gives rise to small negative terms).

This picture is confirmed by the charge-density maps shown in Figs. 3 and 4. In particular the difference maps (bulk minus superposition of ionic charge distributions) show (a) for $Ni^{2+}$, depletion of charge (dotted lines) along the principal axes, and build up of charge along the diag- onals [direction of $d_{x y}, d_{x z}$ , and $d_{y z}$ , particularly evident in the (110) section]; (b) for $F^{-}$ , depletion along the Ni F-Ni line, and transfer of this charge in the orthogonal direction; (c) for $K^{+}$ , a very small spherical contraction[the zone between $F^{-}$ and $K^{+}$ in the (110) section is neg ative, and the zone within the $K^{+}$ sphere is positive, al though the values of the density difference is smaller than the first isodensity line].

The $Ni$ atomic spin is close to two (see Table $V$ and Fig. 5) and is entirely due to $d$ orbitals; a small net spin is located on the $F$ atoms, probably through overlap terms with the $Ni d$ orbitals. The $K^{+}$ ions appear not to be spin polarized, as clearly shown in Fig. 5. The FM and AFM solutions are very similar; the net charges and bond populations coincide to within 0.001 electrons. The same is true for the spin density in the $Ni$ and $K$ regions (see Fig. 6); in the $F$ region, on the contrary, there is an im

![](./images/812756307118391297_7.jpg)

FIG. 7. Valence (left) and conduction (right) bands projected density of states of the ferromagnetic phase. In the two figures, different energy and DOS scales are used.

![](./images/812756307118391297_8.jpg)

FIG. 8. Same as previous figure, for the antiferromagnetic solution.

portant difference: the spin density along the Ni-F-Ni path, which is present in the FM solution and has mainly antibonding character, as results from the comparison of Figs. 4 and 5, is absent (very small) in the AFM map (Fig. 6), because the exchange repulsion has been removed by allowing the two Ni atoms to have opposite spin; as a consequence, the AFM total energy is slightly lower than the FM one.

The valence (left) and conduction (right) density of states (DOS) is shown in Figs. 7 and 8 for the FM and the AFM solutions, respectively. The highest valence band and the lowest conduction band are mainly F in character, with contributions from the Ni $t_{2g}$ (top valence) states and Ni $e_g$ (bottom conduction) states. The $e_g$ band is located at lower energy than the $t_{2g}\alpha$ (majority) states, which in turn (in the FM solution) have lower energy than the $t_{2g}\beta$ states. The DOS for the two magnetic states are similar, apart obviously from the symmetric situation between the $\alpha$ and $\beta$ states in the AFM case. The $t_{2g}\beta$ states show a large dispersion and an extended overlap with F states. The $d$ band width is not negligible even in this very ionic situation. The band gap is about 20 eV. The general features of the DOS referring to the Ni $d$ levels are very similar to those found for NiO with the same HF approach;$^{27}$ we refer then to this study for a more extensive discussion on these aspects.

## IV. CONCLUSIONS

The Hartree-Fock method qualitatively describes correctly the ground-state electronic properties of $KNiF_3$. The system is a large gap insulator, both in the FM and AFM state. The AFM solution is more stable than the FM one by 0.031 eV per Ni couple. The additivity of the superexchange interaction has been verified by comparing two different AFM structures with six and two Ni-Ni nearest neighbors with opposite spin: the ratio between the two $\Delta E$ values (difference between the FM and AFM total energies) is 2.97, to be compared with 3 from a complete independent interaction model. The calculated $\Delta E$ dependence on $d$, the Ni-Ni distance, is well fitted by a $d^{-x}$ power with $x=12.3$, in excellent agreement with the value estimated by de Jongh and Block$^{36}$ from experimental $J$ values for systems with similar geometry but different Ni-Ni distances. The next-nearest neighbors magnetic coupling constant $J_2$ is 0.3% of $J_1$, the nearest-neighbors constant.

## ACKNOWLEDGMENTS

R.D. wishes to thank the Universitat Rovira i Virgili (Tarragona) for a two-month grant. The work was supported by the Human Capital & Mobility Programme of the European Community under Contract No. CHRX-CT93-0155, by the CICYT Project No. PB92-0766-C02-01 of the Spanish Ministerio de Educacion y Ciencia and the CIRIT Project No. GRQ93-7.003 of the Generalitad de Catalunya.

$^{1}$R. Dovesi, C. Pisani, C. Roetti, M. Causà, and V. R. Saunders, CRYSTAL88, QCPE, N.577, Quantum Chemistry Program Exchange, Indiana University, Bloomington, Indiana, 1989; R. Dovesi, V. R. Saunders, and C. Roetti, CRYSTAL92 User's Manual, Universitá di Torino, Torino, 1992.
$^{2}$P. Blaha, K. Schwarz, P. I. Sorantin, and S. B. Trickey, Comput. Phys. Commun. 59, 399 (1990).
$^{3}$R. Dovesi, C. Roetti, C. Freyria Fava, E. Aprá, V. R. Saunders, and N. M. Harrison, Philos. Trans. R. Soc. London, Ser. A 341 (1992).
$^{4}$M. Causà, R. Dovesi, and C. Roetti, Phys. Rev. B 43, 11937 (1991).
$^{5}$K. Brooemfield and P. M. A. Sherwood, J. Chem. Soc. Faraday Trans. 2 79, 799 (1983).
$^{6}$S. Hatta, R. V. Kasowski, and W. Y. Hsu, J. Appl. Phys. 72, 4480 (1992).
$^{7}$V. Eyert and K. H. Hock, J. Phys. Condens. Matter 5, 2987 (1993).
$^{8}$A. Svane and O. Gunnarsson, Phys. Rev. Lett. 65, 1148 (1990).
$^{9}$V. I. Anisimov, M. A. Korotin, and E. Z. Kurmaev, J. Phys. Condens. Matter 2, 3973 (1990).
$^{10}$V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B 44, 943 (1991).
$^{11}$P. Dufek, K. Schwarz, and P.Blaha, Phys. Rev. B 48, 12672 (1993).
$^{12}$W. E. Pickett, Rev. Mod. Phys. 61, 433 (1989), and references therein.
$^{13}$H. Winter, Z. Szotek, and W. M. Temmerman, Z. Phys. B 79, 241 (1990).
$^{14}$F. Illas, J. Casanovas, M. A. Garcia-Bach, R. Caballol, and O. Castell, Phys. Rev. Lett. 71, 549 (1993).
$^{15}$J. Casanovas and F. Illas, J. Chem. Phys. 100, 8257 (1994).
$^{16}$J. Casanovas, J. Rubio, and F. Illas, in New Challenges in Computational Quantum Chemistry, edited by R. Broer, P. J. C. Aerts, and P. S. Bagus (University of Groningen, Groningen, 1994), pp. 214-226.
$^{17}$J. Casanovas and F. Illas, Phys. Rev. B 50, 3789 (1994).
$^{18}$V. Luaña, M. Bermejo, M. Flórez, J. M. Recio, and L. Pueyo, J. Chem. Phys. 90, 6409 (1989).
$^{19}$S. Y. Shashkin and W. A. Goddard III, Phys. Rev. B 33, 1353 (1986).
$^{20}$A. C. Lewandowski and T. M. Wilson, Phys. Rev. B 50, 2780 (1994).
$^{21}$A. B. van Oosten, R. Broer, and W. C. Nieupoort, Int. J. Quantum Chem. (to be published).
$^{22}$C. Pisani, R. Dovesi, and C. Roetti, Hartree-Fock ab initio Treatment of Crystalline Systems, Lecture Notes in Chemistry Vol. 48 (Springer, Heidelberg, 1988).
$^{23}$V. R. Saunders, C. Freyria-Fava, R. Dovesi, L. Salasco, and C. Roetti, Mol. Phys. 77, 629 (1992).
$^{24}$E. Aprá, Ph.D. thesis, Universitá di Torino, 1993.
$^{25}$V. R. Saunders, E. Aprá, and R. Dovesi (unpublished).
$^{26}$W. C. Mackrodt, N. M. Harrison, V. R. Saunders, N. L. Allan, M. D. Towler, E. Aprá, and R. Dovesi, Philos. Mag A

68, 653 (1993).

27M. D. Towler, N. L. Allan, N. M. Harrison, V. R. Saunders, W. C. Mackrodt, and E. Aprá, Phys. Rev. B 50, 5041 (1994).

28M. Catti, G. Valerio, and R. Dovesi, Phys. Rev. B 51, 7441 (1995).

29A. Okazaki and Y. Suemune, J. Phys. Soc. Jpn. 16, 671 (1961).

30S. R. Chinn, H. J. Zeiger, and J. R. O'Connor, Phys. Rev. B 3, 1709 (1971).

31K. Hirakawa, K. Hirakawa, and T. Hashimoto, J. Phys. Soc. Jpn. 15, 2063 (1960).

32Y. Yamaguchi and N. Sakamoto, J. Phys. Soc. Jpn. 27, 1444 (1969).

33M. Rousseau, J.Nouet, and A. Zarembovitch, J. Phys. Chem. Solids 35, 921 (1974).

34M. E. Lines, Phys. Rev. 164, 736 (1967).

35L. J. de Jongh and A. R. Miedema, Adv. Phys. 23, 1 (1974).

36L. J. de Jongh and R. Block, Physica 79B, 568 (1975).

37R. Dovesi, C. Roetti, C. Freyria-Fava, M. Prencipe, and V. R. Saunders, Chem. Phys. 156, 11 (1991).

38M. Catti, R. Dovesi, A. Pavese, and V. R. Saunders, J. Phys. Condens. Matter 3, 4151 (1991).

39J. P. Perdew, Phys. Rev. B 33, 8822 (1986); 34, 7406(E) (1986); J. R. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B 46, 6671 (1992).

40Within the cluster model it has been impossible to obtain an UHF self-consistent solution for the lower spin state [F. Illas (private communication)].