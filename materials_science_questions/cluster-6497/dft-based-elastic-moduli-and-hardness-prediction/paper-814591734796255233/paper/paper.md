QMC and phonon study of super-hard cubic boron carbon nitride

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2015 Mater. Res. Express 2 105902

(http://iopscience.iop.org/2053-1591/2/10/105902)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 144.32.128.70
This content was downloaded on 19/02/2016 at 14:15

Please note that terms and conditions apply.

# Materials Research Express

## PAPER

### QMC and phonon study of super-hard cubic boron carbon nitride

Michael O Atambo¹, N W Makau¹, G O Amolo¹ and Ryo Maezono²

¹ Computational Material Sciences Group, University of Eldoret, Department of Physics, PO Box 1125, Eldoret, Kenya
² School of Information Science, JAIST, Asahidai 1-1, Nomi, Ishikawa 923-1292, Japan

E-mail: rmaezono@jaist.ac.jp

Keywords: superhard materials, quantum Monte Carlo, phonon calculation, ab initio electronic structure, bulk modulus

---

## Abstract
In this study, we have applied phonon and quantum Monte Carlo (QMC) calculations to c-BC₂N, which is derived from c-BN by the introduction of carbon, in search of cheaper as well as harder materials that have advantages over the traditionally known hardest material, diamond. There have been theoretical density functional theory (DFT) results of the bulk modulus, which indicate that c-BC₂N has a higher bulk modulus than c-BN. However, varied findings of experimental data for the properties of c-BC₂N reported by various groups appear to indicate a wide range of values. We found lattice structure instability at the high pressure region of c-BC₂N which has been used for theoretical estimations of bulk modulus. We also examined the widely varying predictions depending on the functionals used in previous DFT works, using QMC with a more accurate treatment of the electronic interactions. Taking the instabilities into account, the QMC energy-volume fitting is still found to support that c-BC₂N has a higher bulk modulus than c-BN, but with smaller difference than the prediction of the previous theoretical works. We also find substantial reductions in the bulk modulus due to zero point vibrational effects.

---

Cubic boron nitride (c-BN), known as ‘Borazon’, has been used as a superhard material possessing chemical stability up to around 1600 °C when it is used to machine ferrous alloys [1]. This chemical stability is not shown by diamond on the other hand although it is known to be the hardest material. The Knoop hardness value of c-BN is, however, about half of that of diamond [2, 3], and hence there are still efforts to seek such materials with higher hardness. Such efforts include the synthesis of boron carbon nitride (c-BC₂N), which can be regarded as a mixture of c-BN and diamond as well as being expected to possess both the hardness due to the diamond and the chemical stability due to c-BN. The synthesis has been reported since 1979 [4] by using the structural transition from hexagonal to cubic phase. Wedlake and Penny [4] reported the transition from h-BCN to c-BC₂N at 15 GPa under temperatures higher than 3000 °C. Badzian [5] synthesized c-BCN in similar way and identified its cubic structure by x-ray diffraction. Sasaki *et al* [6] tried to get c-BC₂N from h-BC₂N under high pressure and temperature with Co catalyst but reported that they got a mixture of c-BN and diamond. Nakano *et al* [7] tried instead without catalysts and reported obtaining c-BCN successfully which turned out to be the intermediate product to the phase separation with c-BN and diamond.

Knittle *et al* [8] synthesized c-Cₓ(BN)₁₋ₓ, $(x = 0.3-0.33, 0.5, 0.6)$ by the laser irradiation to the high pressure phase and reported the bulk modulus of c-C$_{0.33}$(BN)$_{0.67}$ as $355 \pm 19$ GPa, which is even lower than that of c-BN (369-401 GPa). Komatsu *et al* [9] using a different synthesis technique, synthesized c-BC$_{2.5}$N by explosion compression, getting its bulk modulus as $401 \pm 15$ GPa. While this supports the positive expectation that c-Cₓ(BN)₁₋ₓ could be a harder material than c-BN, Solozhenko *et al* [10] reported a lower hardness in terms of the bulk modulus of $282 \pm 15$ GPa for c-BC₂N, though its values of hardness in terms of the Vickers and Knoop criteria are reported being superior to c-BN. Restricting ourselves only to the bulk modulus, it is still unclear experimentally if c-BC₂N(c-Cₓ(BN)₁₋ₓ) could give higher modulus than c-BN. Though the ambiguity seems to come mainly from the difficulty to maintain the sample quality in the synthesis, it is worthwhile to use

---

© 2015 IOP Publishing Ltd

$ab$ initio calculations to clarify if the theoretical estimation of the bulk modulus of $c$-$BC_2$N could exceed that of $c$-BN.

There have been several density functional theory (DFT) calculations to estimate the bulk modulus of $c$-$BC_2$N ($c$-$C_x$(BN)$_{1-x}; x=0.66$), concentrating on a specific $x$ mainly because of the tractability in modeling of mixture by a super cell. All of DFT works so far support that $c$-$BC_2$N has higher bulk modulus than $c$-BN. Tateyama *et al* [11] applied local density approximation (LDA) reporting the modulus as 438 GPa. Similar LDA works by Mattesini and Matar [12] and Chen *et al* [13] also report a higher bulk modulus than that of $c$-BN. Guo *et al* [14] applied generalized gradient approximation (GGA) with Perdew–Burke–Ernzerhof (PBE) functional instead and reported the modulus at most 402.1 GPa. Gao *et al* [15] pointed out that while the DFT estimations of the bulk modulus are inconsistent with the experiment by Solozhenko [10], they could reproduce the experimental Vickers hardness by their estimation scheme coupled with GGA calculation. Šimůnek and Vackář [16] applied the same scheme with LDA instead and reported consistent results with Gao *et al*. The ideal strength at normal compression has been used to study $c$-$BC_2$N by Chen *et al* [17] as well as Wu *et al* [18], respectively, among others. Wu *et al* [18] found that the ideal strength of $c$-$BC_2$N is higher than that of $c$-BN, and also concluded that the segregation of B, C and N into layers lead to a higher strength in the material. Similarly Zhao *et al* concluded that the hardness of $c$-$BC_2$N is higher, based on the studies of the Vickers hardness [19]. From studies of the elastic properties, Chang *et al* found that the hardness of $c$-$BC_2$N is second only to that of diamond, and that the material showed evidence of brittleness, and stability up to pressures of 100 GPa [20]. Other arguments have been suggested to deal with studies on superhard materials such as electronegativity [21] and bond counting rules, employed in a rare quantum Monte Carlo(QMC) study [22].

In this work we concentrate on the bulk modulus of $c$-$BC_2$N so as to establish whether our QMC estimation supports the above DFT conclusions, namely that the modulus of $c$-$BC_2$N is superior to that of $c$-BN, being inconsistent with the experiment by Solozhenko *et al* [10]. The QMC [23] method does not depend on the exchange-correlation (XC) functionals and hence can provide more reliable reference estimation in the sense of electronic correlations, providing reliable estimations of the elastic properties with reasonably suppressed statistical errors [24–26] due to the recent increased computational power. We also applied the phonon calculation within DFT to estimate the lattice instability and the phonon corrections. We clarified the lattice instabilities of $c$-$BC_2$N at the high pressure regime, which is not taken into account in the previous studies. With the elimination of these volumes from the equation of state (EoS) fitting, our evaluations conclude that $c$-$BC_2$N gives higher bulk modulus than $c$-BN even after the lattice vibration corrections. Our diffusion Monte Carlo (DMC) studies correspond to the best possible estimation within non-relativistic, adiabatic, and fixed node approximations, as well as the available qualities of pseudo potentials. This result supports the conclusions obtained by the previous DFT studies.

The bulk modulus is estimated from the fitting of the energy–volume dependence $E(V)$ by an EoS. For compression exceeding $\sim$30% in the volume variation, Vinet EoS is known to work better [27, 28], where $V_0$ and $B_0$ denote the volume and the bulk modulus at equilibrium, respectively, and $B_0'$ is the pressure derivative of the bulk modulus. We also used Birch–Murnaghan EoS to check if our predictions have any dependence on the choice of EoS. We tried to determine the value of $B_0'$ using QMC statistical data as has been done in [25], but this was not computationally feasible for some data points, so the value of $B_0'$ was finally fixed at 4.0 as is the norm [28]. QMC data for $E(V)$ are evaluated by DMC calculations [23, 29]. It handles the many-body wave function as a function of the $N$-electron configuration, and effectively performs the projection operation starting from an initial guess $\Psi_T$ toward the exact solution as $\tau \to \infty$ [23, 29], giving the energies as a stochastic estimate with a statistical error bar. For the initial guess $\Psi_T$, working as fixed trial node for DMC, we prepared it in Slater–Jastrow form [23]. DFT-KS orbitals are used for a Slater determinant, generated by QUANTUM ESPRESSO [30], a DFT package using plain wave basis sets. We used GGA-PBE XC functional [31] and He-core pseudo potentials for B, C, and N. As norm-conserving pseudo potentials for QMC we used Trail–Needs [32, 33] potentials. We also performed DFT calculations using ultra-soft pseudo potentials [34] for comparison.

We took the zinc-blende structure for $c$-BN, and substituted some sites by C to get the unit cell for $c$-$BC_2$N. There are seven possible structures with cubic symmetry for $c$-$BC_2$N, from which we took the energetically most stable one [35]. Simulation cell sizes for $c$-BN and $c$-$BC_2$N were taken as $4 \times 4 \times 4$ (512 electrons), and $3 \times 3 \times 3$ (864 electrons), respectively, so that each system has almost the same number of electrons for reliable comparisons. These cell sizes are confirmed to give total energy convergence within the chemical accuracy with respect to the simulation size. To reduce the finite size error (FSE) the mesh was shifted in the Brillouin zone as in [24]. KS orbitals obtained by DFT in plain-wave expansions were re-expanded by the spline basis called 'blip' using the utility implemented in CASINO [36]. We used the function forms for Jastrow factor provided by CASINO [36], taking only $u$ and $\chi$ terms, each of which describes the correlation depending on electron–electron and electron–nucleus inter-particle distances. Expanding coefficients included in the functions were optimized by using the variance minimization scheme, which is known to work well for linear parameters [37],

![](./images/814591734796255233_1.jpg)

Table 1. Equilibrium volume $V_0$, bulk modulus $B_0$, and the pressure derivative of the modulus $B_0'$ at the equilibrium volume evaluated by Vinet EoS fittings. MPC corrections for FSE is applied for DMC values. Statistical errors in DMC are given in parenthesis. Lattice vibration effects are not taken into account and as such, the comparison here is not the final conclusion.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">$V_0 (\text{Bohr}^3)$</th>
<th colspan="2">$B_0 (\text{GPa})$</th>
<th colspan="2">$B_0'$</th>
</tr>
<tr>
<th>BN</th>
<th>BC₂N</th>
<th>BN</th>
<th>BC₂N</th>
<th>BN</th>
<th>BC₂N</th>
</tr>
</thead>
<tbody>
<tr>
<td>GGA</td>
<td>80.576</td>
<td>319.646</td>
<td>364.59</td>
<td>373.34</td>
<td>3.857</td>
<td>3.809</td>
</tr>
<tr>
<td>DMC</td>
<td>79.44(3)</td>
<td>318.2(4)</td>
<td>391(1)</td>
<td>395(2)</td>
<td>3.79(1)</td>
<td>3.62(8)</td>
</tr>
<tr>
<td>LDA [11]</td>
<td>76.89</td>
<td>308.8</td>
<td>366(14)</td>
<td>438(14)</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>LDA [12]</td>
<td>—</td>
<td>306.26</td>
<td>—</td>
<td>408.95</td>
<td>—</td>
<td>3.54</td>
</tr>
<tr>
<td>LDA [13]</td>
<td>78.25</td>
<td>307.7</td>
<td>392</td>
<td>421.9</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>GGA [14]</td>
<td>—</td>
<td>310.26</td>
<td>—</td>
<td>402.1</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>Exp.</td>
<td>79.7128 [42]</td>
<td>327.2 [10]</td>
<td>395(2) [42]</td>
<td>282 [10]</td>
<td>—</td>
<td>—</td>
</tr>
</tbody>
</table>

describing more than 80% of the correlation energy in DMC for all the volumes. We activated $T$-move scheme [38] to suppress the instability toward the population explosion [36, 39].

Energy–volume curves of c-BN and c-BC₂N are shown in figure 1 and EoS parameters from these raw data are shown in table 1. The results in table 1 do not take lattice vibration effects into account, which is discussed later. GGA estimations of c-BN (c-BC₂N) are obtained at the intermediate stage of the trial node generations using $4 \times 4 \times 4$ ($3 \times 3 \times 3$) mesh size for DMC. DMC data are obtained with the time step $\mathrm{d}t=0.002$ a.u. after the model periodic Coulomb (MPC) correction for FSE [40, 41]. The results here indicate that c-BC₂N has a higher bulk modulus than c-BN, supporting all the previous DFT works. As discussed later, this conclusion is maintained even after several corrections and the use of a different type of EoS. The experimental equilibrium volume in table 1 for c-BN is expected to be reliable because the quality of the samples are well controlled than for c-BC₂N, and hence can be used as a reference for theoretical estimations. On this reference,we achieved fairly good agreement with QMC estimations of the equilibrium volume, $-0.34\%$ (raw) and $+0.8\%$ (with zero point vibrations) in its relative error. Even at our GGA raw value, it is $+1.09\%$, which is an improvement when compared to previous works such as Tateyama et al [11] giving $-3.54\%$ and Chen et al [13] $-1.84\%$. Together with previous LDA, our GGA is consistent with the known fact that LDA overestimates the hardness of solids with shorter bonding lengths while GGA does the opposite. We see that DMC gives an estimation that falls in between the LDA (other works) and GGA (our calculations) values, and being closest to the experimental value of c-BN. For c-BC₂N the DMC findings are still in between the LDA and GGA but reported experimental values are off from theoretical estimations, which is presumably related to the sample quality as discussed later. Our estimations for $B_0'$ are close to 4.0, which is quite reasonable when compared to previous works shown in table 3.

MPC interaction scheme [40, 41] describes a part of two-body FSE [43] in DMC. The difference between Ewald and MPC [40, 41] estimations can be used as a quick check of FSE [43, 44]. MPC gives higher estimations in the total energies, in accordance with the general expectation [40, 41]. We confirmed that the deviations due

to the MPC correction in the estimated EoS parameters are within 0.3% at most. For one-body FSE, $k$-mesh discretization error in DFT also contribute to a part of it. The mesh used in the previous DFT works ranges from $7 \times 7 \times 7$ in Guo *et al*[14] to $8 \times 8 \times 8$ in Mattesini and Matar [12] and Chen *et al*[13] which are denser than ours of ($3 \times 3 \times 3$ and $4 \times 4 \times 4$). It is found, however, that the $k$-mesh discretization error in DFT is kept within 0.1 mHartree, which is usually expected for insulating systems. We also evaluated the time-step dependence of DMC total energies. Our final choice $\text{d}t = 0.002$ is found to give the deviation from the smaller time step $\text{d}t = 0.001$ in the total energy being 6 mHartree/primitive_cell at most for $\text{c-BC}_2\text{N}$ while that for c-BN was 3 mHartree/primitive_cell. We hence expect error cancellation in the final EoS fitting and hence took this time-step as our final choice.

For the EoS fittings including phonon contributions, we fixed $B_0'$ as 4.0 for keeping statistical errors small enough. We hence examined the influence of the fixing $B_0'$ on the estimation of EoS parameters. The hardness of $\text{c-BC}_2\text{N}$ over c-BN is proven to be unchanged regardless of fixing $B_0'$, with slight deviations mainly for $\text{c-BC}_2\text{N}$ upto 0.5% (7%) for $V_0 (B_0)$ in QMC. Detaching the constraints of fixing $B_0'$ makes c-BN hardness closer to $\text{c-BC}_2\text{N}$ but it is still softer. By fixing $B_0'$ as 4.0, we examined whether the estimations of $V_0$ and $B_0$ depends in any way on on the choice of EoS by substituting Vinet's EoS into Birch–Murnaghan's. When compared to the experimental values of c-BN, Vinet's EoS gives a better estimation to the experimental value. For $\text{c-BC}_2\text{N}$ the deviations from Vinet's estimations are found to be within 0.02% (2%) for $V_0 (B_0)$ both for DFT and QMC. Those for c-BN are 2% (15%) for $V_0 (B_0)$ with the tendency that Birch–Murnaghan gives a slightly softer estimation for c-BN, thereby confirming that $\text{c-BC}_2\text{N}$ is harder than c-BN. We also examined the dependence on the choice of pseudo potentials with the same core sizes. Ultrasoft potentials were found to give higher estimations of the bulk modulus by up to 2% when compared to those of norm-conserving ones with shortened bond lengths. For the experimental reference of c-BN, the ultrasoft pseudopotentials gave much better estimations. Though the present norm-conserving potentials overestimate $V_0$ for c-BN at DFT, it is corrected by DMC, being shifted closer to the experimental findings. Previous GGA [14] studies of $\text{c-BC}_2\text{N}$ took the same Vanderbilt ultrasoft potentials with PBE-DFT by using CASTEP [45], and hence is expected to give almost the same estimation as the present ultrasoft ones. This was however not the case, and the discrepancy may be due to the difference of the details of lattices structural parameters.

The difference of the bulk modulus for c-BN and $\text{c-BC}_2\text{N}$ is estimated to be relatively small, and hence the conclusion that $\text{c-BC}_2\text{N}$ is harder would possibly be affected by the lattice vibration effects which is not negligible at finite temperature where hard materials are normally used. Larger degrees of freedom for the vibration modes for $\text{c-BC}_2\text{N}$ bring about more possibility for softening through entropy which might compensate for the difference in the modulus estimated without considering phonons. To check if the conclusions in the previous sections are kept unchanged we examined the lattice vibration effects using phonon estimations implemented within the DFT. Phonons are treated within the quasiharmonic approximation [46, 47]. The free energy is evaluated as a function of phonon frequencies of lattice vibration mode [26]. We evaluated the frequencies from force constants obtained by QUANTUM ESPRESSO using PBE functional with $(2, 2, 2)$ $q$-mesh for phonon Brillouin zone discretization. Simulation size for the phonon estimations is carefully chosen to get $(6 \times 6 \times 6)$ as the final choice with tractability. Negative phonon dispersion corresponding to lattice instabilities are found at the high pressure regime of $\text{c-BC}_2\text{N}$, $V = 405$ and $V = 439$ Bohr$^3$, shown as cross marks in figure 1. Based on the Vinet EoS used here, the equilibrium volume is evaluated at high pressures of even more than 126 GPa where this instability might occur. Infact such pressures are now accessible as noted by the recent static high pressure experiments [24]. The instability might indicate a pressure-induced structural transition into some other structure [26]. The elimination of these two volumes from EoS fitting enlarges the error bars on $B_0$ by around five times, making the comparison between c-BN and $\text{c-BC}_2\text{N}$ impossible unless we fix $B_0'$. The elimination does not change the conclusion that $\text{c-BC}_2\text{N}$ is still harder, though it leads to the slight expansion and softening.

Adding the phonon correction, we performed the EoS fitting to get the results shown in table 2, describing thermal expansions and corresponding softenings. Zero point vibrations at $T = 0$ expands c-BN and $\text{c-BC}_2\text{N}$ by the amount of 1.18% and 1.26%, respectively. For c-BN the experimental value of $V_0$ drops to between the DMC estimation with and without phonon correction at $T = 0$ K, while for $B_0$ the correction makes the estimation to approach from below the experimental values, being around $-3.5\%$. Thermal expansions for c-BN and $\text{c-BC}_2\text{N}$ from $T = 0$ to 300 K amount to 0.05% and 0.06%, respectively, corresponding to the change in the bulk modulus as $-0.17\%$ and $-0.27\%$. The corrections turn out not to change the fact that $\text{c-BC}_2\text{N}$ is still harder in terms of the bulk modulus than c-BN. The correction for $\text{c-BC}_2\text{N}$ including zero point vibrations is about four times larger than that of c-BN, which coincides quite well with the ratio of the number of modes taken into account, i.e. six for c-BN while 24 for $\text{c-BC}_2\text{N}$.

Since the main question of the present work is to examine whether $\text{c-BC}_2\text{N}$ is indeed harder than c-BN, we have to take the same condition for fitting the EoS for both, namely fixing $B_0'$ to be 4.0. Taking only c-BN we can estimate the perfect fitting even without fixing $B_0'$ as shown in figure 1. We compare our results on BN with

<table>
<caption>Table 2. Equilibrium volumes and the bulk modulus by GGA and DMC/MPC with lattice vibration contributions being included. These were obtained by Vinet EoS with fixing $B'_0$ being fixed at 4.0 (note that only for c-BN, more liable fit without fixing $B'_0$ is given in table 3). Statistical errors are given in parenthesis.</caption>
<thead>
<tr>
<th>
</th>
<th colspan="2">
$V_0$ (Bohr3)
</th>
<th colspan="2">
$B_0$ (GPa)
</th>
</tr>
<tr>
<th>
</th>
<th>
BN
</th>
<th>
BC₂N
</th>
<th>
BN
</th>
<th>
BC₂N
</th>
</tr>
</thead>
<tbody>
<tr>
<th>
GGA/0 K
</th>
<td>
81.0969
</td>
<td>
323.6860
</td>
<td>
347.02
</td>
<td>
354.17
</td>
</tr>
<tr>
<th>
GGA/300 K
</th>
<td>
81.1419
</td>
<td>
323.8707
</td>
<td>
346.30
</td>
<td>
353.19
</td>
</tr>
<tr>
<th>
DMC/0 K
</th>
<td>
80.68(3)
</td>
<td>
322.3(5)
</td>
<td>
355.6(5)
</td>
<td>
365(4)
</td>
</tr>
<tr>
<th>
DMC/300 K
</th>
<td>
80.72(3)
</td>
<td>
322.5(5)
</td>
<td>
355.0(5)
</td>
<td>
364(4)
</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3. Elastic properties of c-BN evaluated while including the fitting of $B'_0$ ranging from 3.62 to 3.91, which is different from table 2. Statistical errors are given in parenthesis. Vinet EoS and MPC FSE corrections are used. DMC works are referenced from [48], ‘TN(64)’ means the 64 atoms simulation cell size with Trail–Needs pseudo potentials [32, 33], while ‘BFD’ means Burkatzki [49] pseudo potentials, respectively.</caption>
<thead>
<tr>
<th>
</th>
<th>
$V_0$ (Bohr3)
</th>
<th>
$B_0$ (GPa)
</th>
<th>
$B'_0$
</th>
</tr>
</thead>
<tbody>
<tr>
<th>
GGA/raw
</th>
<td>
80.58
</td>
<td>
364.59
</td>
<td>
3.86
</td>
</tr>
<tr>
<th>
GGA/0 K
</th>
<td>
81.01
</td>
<td>
357.76
</td>
<td>
3.90
</td>
</tr>
<tr>
<th>
GGA/300 K
</th>
<td>
81.05
</td>
<td>
356.42
</td>
<td>
3.91
</td>
</tr>
<tr>
<th>
DMC/raw/TN(64)
</th>
<td>
79.44(3)
</td>
<td>
391(1)
</td>
<td>
3.79(1)
</td>
</tr>
<tr>
<th>
DMC/0 K
</th>
<td>
80.35(3)
</td>
<td>
381(1)
</td>
<td>
3.80(1)
</td>
</tr>
<tr>
<th>
DMC/300 K
</th>
<td>
80.39(3)
</td>
<td>
380(1)
</td>
<td>
3.81(1)
</td>
</tr>
<tr>
<th>
LDA [13]
</th>
<td>
78.25
</td>
<td>
392
</td>
<td>
—
</td>
</tr>
<tr>
<th>
Exp. [42]
</th>
<td>
79.7128
</td>
<td>
395(2)
</td>
<td>
3.62(5)
</td>
</tr>
<tr>
<th>
DMC/300 K/TN(64) [48]
</th>
<td>
79.6(1)
</td>
<td>
381(6)
</td>
<td>
3.87(6)
</td>
</tr>
<tr>
<th>
DMC/300 K/BFD(64) [48]
</th>
<td>
79.5(1)
</td>
<td>
382(7)
</td>
<td>
3.87(7)
</td>
</tr>
<tr>
<th>
DMC/300 K/BFD(128) [48]
</th>
<td>
79.71(5)
</td>
<td>
378(3)
</td>
<td>
3.87(3)
</td>
</tr>
</tbody>
</table>

several previous works as shown in table 3. For c-BN, there is another DMC work by Esler et al [48] where Vinet EoS is used. Taking the experiment by Datchi et al [42] as a reference, we see that our DMC projection corrects the volume around the experimental value, from $-0.3\%$ without phonon to $+0.8\%$ with phonon corrections while the GGA (used to generate the nodal surface) always gives overestimations around $+1.5\%$. The ‘DMC/TN(64)’ studies by Esler et al [48] employs the same pseudo potentials and the same simulation size as our present work, but with additional work done to correct for pseudo potential errors by calibrating all electron calculations. The larger error bars, which are an order of magnitude larger than the present work, might be due to the additive errors when the energies are added/subtracted to compose the sophisticated corrections. They used rougher corrections for phonons, taking Debye approximation using Debye temperature, giving the closer coincidence. It implies that their phonon correction would underestimate the thermal expansion than the present work because our result passes across the experimental values from $-0.3\%$ to $+0.8\%$ by including phonon corrections. For the bulk modulus, all the theoretical estimations underestimate it. However, our DMC studies give a better approximation of $-3.8\%$, while GGA gives $-9.8\%$. Previous LDA results [13] give the closest value of $-0.8\%$ though it underestimates the equilibrium volume. Relying on the size dependence observed by Esler’s work, BFT(64) to BFD(128), we expect that the FSE corrections would lead further softening, thereby deviating from experimental values table 3 also suggests a substantial reduction in the bulk modulus of BN due to zero point vibrational effects, when we compare the raw result and that for 0 K. This is also the case for BC₂N when we compare table 1 (raw) and table 2 (0 K). Previous results by DFT would be regarded as overestimations due to this effect.

Our DMC findings were able to describe the bulk modulus of c-BN reasonably well compared with experiments. This supports the justification of the approximations applied to the present DMC, namely the adiabatic, non-relativistic, fixed-node [23, 29], and the locality [23, 29] approximations. Note that Trail–Needs pseudo potentials [32, 33] used here include some relativistic effects, so the present calculations are regarded as partially relativistic, in a more precise sense. Compared with previous DFT studies [11–14], the present DMC findings support their conclusions that c-BC₂N gives a bulk modulus exceeding that of c-BN. On the other hand,

many experiments [8, 10] on c-$C_x$(BN)$_{1-x}$ except Komatsu *et al* [9] could not reproduce a bulk modulus exceeding c-BN, being inconsistent with the above theoretical estimations. Their (Solozenko *et al*) sample was reported, however, to have a larger lattice constant of 3.642(2)Å for c-$BC_2$N, than those of c-BN (3.6158 Å) and carbon-diamond (3.5667 Å), based on which they related it to a new structural phase identified as $B_{0.4\pm0.1}C_{1.1\pm0.1}N_{0.5\pm0.1}$. Another possibility was pointed out [50] relating to the difficulty to extract the exact bulk modulus of such an anisotropic sample.

In summary, we have considered a careful analysis of c-BN and c-$BC_2$N with the aim of accurately analyzing their bulk properties. The properties were studied with respect to the dependence on the EoS, finite size effects, pseudopotential choice and structural stability. All the results obtained in this work suggest that c-$BC_2$N has a higher bulk modulus than that of c-BN. A check of structural stability from phonon calculations upon elimination of lattice instabilities and finite temperature investigations using both GGA and DMC approaches also demonstrated a higher value of the bulk modulus for c-$BC_2$N. The diverse reported experimental findings of the bulk modulus are an indication of the difficulty existing in the synthesis of a homogeneous c-$BC_2$N matrix. From a theoretical point of view the isotropic form of c-$BC_2$N would have a higher bulk modulus than that of c-BN.

### Acknowledgments

The authors acknowledge Mr Kentaro Hayaschi for his intensive computational contributions. The authors also acknowledge the support by the Computational Materials Science Initiative (CMSI/Japan) for the computational resources, SR16000 (Center for Computational Materials Science of the Institute for Materials Research, Tohoku University/Japan) and K-computer (Riken/Japan). R M is grateful for financial support from KAKENHI grants 26287063, 25600156, 23104714, and that from the Asahi glass Foundation. The Computational Materials Science Group in Eldoret would like to acknowledge the National Commission for Science, Technology and Innovation (NACOSTI, Kenya Government) for support through a grant, NCST/003/4 Call/050.

### References

[1] Vel L, Demazeau G and Etourneau J 1991 *Mater. Sci. Eng. B* **10** 149
[2] Solozhenko V L, Kurakevych O O, Andrault D, le Godec Y and Mezouar M 2009 *Phys. Rev. Lett.* **102** 015506
[3] Qin J *et al* 2008 *Adv. Mater.* **20** 4780
[4] Wedlake R J and Penny A L 1979 *Chem. Abstr.* **90** 42865Z
[5] Badzian A R 1981 *Mater. Res. Bull.* **16** 1385
[6] Sasaki T, Akaishi M, Yamaoka S, Fujiki Y and Oikawa T 1993 *Chem. Mater.* **5** 695
[7] Nakano S, Akaishi M, Sasaki T and Yamaoka S 1994 *Chem. Mater.* **6** 2246
[8] Knittle E, Kaner R B, Jeanloz R and Cohen M L 1995 *Phys. Rev. B* **51** 12149
[9] Komatsu T, Nomura M, Kakudate Y and Fujiwara S 1996 *J. Mater. Chem.* **6** 1799
[10] Solozhenko V L, Andrault D, Fiquet G, Mezouar M and Rubie D C 2001 *Appl. Phys. Lett.* **78** 1385
[11] Tateyama Y, Ogitsu T, Kusakabe K, Tsuneyuki S and Itoh S 1997 *Phys. Rev. B* **55** R10161
[12] Mattesini M and Matar S 2001 *Int. J. Inorg. Mater.* **3** 943
[13] Chen S, Gong X G and Wei S H 2007 *Phys. Rev. Lett.* **98** 015502
[14] Guo X *et al* 2007 *Diam. Relat. Mater.* **16** 526
[15] Gao F *et al* 2003 *Phys. Rev. Lett.* **91** 015502
[16] Šimůnek A and Vackář J 2006 *Phys. Rev. Lett.* **96** 085501
[17] Chen S, Gong X G and Wei S-H 2009 *Phys. Status Solidi* **246** 589
[18] Wu B-R, Huang Z-Q, Su W-S, Hsieh Y-Y and Chuang F-C 2010 *Diam. Relat. Mater.* **19** 1341
[19] Zhao J, Zhuang C and Jiang X 2010 *Diam. Relat. Mater.* **19** 1419
[20] Chang J, Chen X-R, Wei D-Q and Yuan X-L 2010 *Phys.:Condens. Matter* **405** 3751
[21] Li K, Wang X, Zhang F and Xue D 2008 *Phys. Rev. Lett.* **100** 235504
[22] Yuge K 2009 *J. Phys.: Condens. Matter* **21** 415403
[23] Foulkes W M C, Mitas L, Needs R J and Rajagopal G 2001 *Rev. Mod. Phys.* **73** 33
[24] Maezono R, Ma A, Towler M D and Needs R J 2007 *Phys. Rev. Lett.* **98** 025701
[25] Maezono R, Drummond N D, Ma A and Needs R J 2010 *Phys. Rev. B* **82** 184108
[26] Ouma C N M, Mapelu M Z, Makau N W, Amolo G O and Maezono R 2012 *Phys. Rev. B* **86** 104115
[27] Cohen R E, Gülseren O and Hemley R J 2000 *Am. Mineral.* **85** 338
[28] Anderson D L 1989 *Theory of the Earth* (Oxford: Blackwell Scientific Publications)
[29] Hammond B L, Lester W A and Reynolds P J 1994 *Monte Carlo Methods in Ab initio Quantum Chemistry* (Singapore: World Scientific)
[30] Giannozzi P *et al* 2009 *J. Phys.: Condens. Matter* **21** 395502
[31] Perdew J, Burke K and Ernzerhof M 1996 *Phys. Rev. Lett.* **77** 3865
[32] Trail J R and Needs R J 2005 *J. Chem. Phys.* **122** 174109
[33] Trail J R and Needs R J 2005 *J. Chem. Phys.* **122** 014112
[34] Vanderbilt D 1990 *Phys. Rev. B* **41** 7892
[35] Sun H, Jhi S, Roundy D, Cohen M and Louie S 2001 *Phys. Rev. B* **64** 094108
[36] Needs R, Towler M, Drummond N and Rios P L 2010 *J. Phys.: Condens. Matter* **22** 023201

[37] Drummond N D and Needs R J 2005 *Phys. Rev.* B **72** 085124

[38] Casula M 2006 *Phys. Rev.* B **74** 161102

[39] Umrigar C J, Nightingale M P and Runge K J 1993 *J. Chem. Phys.* **99** 2865

[40] Fraser L M *et al* 1996 *Phys. Rev.* B **53** 1814

[41] Williamson A J *et al* 1997 *Phys. Rev.* B **55** R4851

[42] Datchi F, Dewaele A, Godec Y and Loubeyre P 2007 *Phys. Rev.* B **75** 214104

[43] Hongo K, Watson M, Iitaka T, Aspuru-Guzik A and Maezono R 2015 *J. Chem. Theor. Comput.* **11** 907

[44] Drummond N D, Needs R J, Sorouri A and Foulkes W M C 2008 *Phys. Rev.* B **78** 125106

[45] Clark S J *et al* 2005 *Z. Kristallogr.* **220** 567

[46] Mounet N and Marzari N 2005 *Phys. Rev.* B **71** 205214

[47] Abbasnejad M, Shojaee E, Mohammadizadeh M R, Alaei M and Maezono R 2012 *Appl. Phys. Lett.* **100** 261902

[48] Esler K *et al* 2010 *Phys. Rev. Lett.* **104** 185702

[49] Burkatzki M, Filippi C and Dolg M 2007 *J. Chem. Phys.* **126** 234105

[50] Zhang Y, Sun H and Chen C 2004 *Phys. Rev. Lett.* **93** 195504