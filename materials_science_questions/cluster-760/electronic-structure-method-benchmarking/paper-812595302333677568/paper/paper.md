**Ab initio pseudopotential and density-functional all-electron study of ionization and excitation energies of actinide atoms**

Wenjian Liu, $^{1,2}$ Wolfgang Küchle, $^{1}$ and Michael Dolg $^{1,*}$

$^{1}$Max-Planck-Institut für Physik komplexer Systeme, Nöthnitzer Straße 38, D-01187 Dresden, Germany
$^{2}$State Key Laboratory of Rare Earth Materials Chemistry and Applications, College of Chemistry and Molecular Engineering, Peking University, Beijing 100871, People's Republic of China

(Received 8 January 1998)

Both relativistic energy-consistent small-core *ab initio* pseudopotential and fully relativistic density-functional all-electron calculations have been carried out by exploiting the presently available highest computational capability for the first to fourth ionization potentials as well as the $df$ [$\Delta_{df}=E(f^{n}d^{1}s^{2})$-$E(f^{n+1}d^{0}s^{2})$ ($n=0-13$ for Ac-No)] and $fd$ [$\Delta_{fd}=E(f^{n}d^{2}s^{2})$-$E(f^{n+1}d^{1}s^{2})$ ($n=0-13$ for Th-Lr)] excitation energies for the whole series of actinide atoms. The calculated ionization potentials might be useful to guide future experimental measurements. [S1050-2947(98)06708-0]

PACS number(s): 31.15.Ar, 31.15.Ew, 32.10.Hq

## I. INTRODUCTION

The chemistry of $f$ elements (lanthanides and actinides) has received much attention in the past three decades [1]. However, the complexity due to the possible open shells with different main quantum numbers, i.e., $(n-2)f$, $(n-1)d$, $ns$ and $np$ ($n=6$ for lanthanides and $n=7$ for actinides), poses a great challenge to theoretical work [2], e.g., the $^{2S+1}L_J$ term of the $f^n$ subshell may have a spin $S$ as large as $7/2$ and an angular momentum $L$ as large as 12. Even more extreme values may result from the coupling of the $f^n$ subshell to other partially occupied shells of $s$, $p$, or $d$ symmetry. Moreover, spin-orbit coupling leads to a large number of energetically adjacent electronic states [3,4] and further complicates both experimental measurements and their interpretation as well as theoretical investigations. For quantitative theoretical work the effects of the electron correlation and relativity have to be taken into account accurately in order to get reliable results. An ideal atomic program to achieve this is currently not available and the situation is even worse when molecules are considered. As a consequence, the present knowledge of the energy levels of free lanthanide and especially actinide atoms and ions is far from being complete.

Recently we applied two different approaches, i.e., quasirelativistic (QR) *ab initio* pseudopotential (PP) methods and fully relativistic density-functional theory (DFT), to the calculation of the first to fourth ionization potentials as well as $df$ excitation energies [$\Delta_{df}=E(f^{n}d^{1}s^{2})$-$E(f^{n+1}d^{0}s^{2})$ ($n=0-13$ for La-Yb)] of the whole series of lanthanide atoms [5]. We found that these two approaches have essentially the same accuracy and can provide quite reliable results. In fact, the accuracy of our approaches was shown to be very close to that of fully relativistic coupled-cluster all-electron calculations using large basis sets [6]. However, such a highly accurate *ab initio* approach [6] is currently feasible only for some special cases of atoms, whereas our methods are applicable to both atoms and molecules with essentially the same level of accuracy. Although the fairly accurate and complete set of experimental values in the case of the lanthanides was useful to calibrate our theoretical methods, the situation for the actinides is totally different: Only a few experimental measurements have been carried out and especially for the higher ionization potentials almost no data exist for comparison. Based on our experience for lanthanides, we believe that our results, whenever the agreement between the two approaches is good, might be useful to guide future experimental measurements. In addition, since only a few DFT studies for some cases and almost no high-level *ab initio* investigations have been performed for actinides so far, we felt that a broad study of all actinide elements using modern DFT as well as *ab initio* techniques would be timely. Therefore, we decided to apply our methods to the whole series of actinides.

Our paper is organized as follows. The applied *ab initio* PP and DFT methods are briefly outlined in Sec. II. The results are discussed and compared with available experimental data as well as previous theoretical results in Sec. III. Finally, the conclusions are presented in Sec. IV.

## II. METHODS

### A. QR PP

The relativistic energy-consistent *ab initio* PP approach was previously described elsewhere [7,8] and will be outlined here only briefly. The valence-only model Hamiltonian for an atom or ion with $n$ valence electrons is given as

$$
\mathcal{H}_v=-\frac{1}{2} \sum_{i}^{n} \Delta_{i}+\sum_{i<j}^{n} \frac{1}{r_{i j}}+V_{a v}+V_{s o}. \tag{1}
$$

Here $i$ and $j$ are electron indices. $V_{av}$ denotes a spin-orbit averaged relativistic PP in a semilocal form

$$
V_{a v}=-\sum_{i} \frac{Q}{r_{i}}+\sum_{i} \sum_{l, k} A_{l k} \exp (-a_{l k} r_{i}^{2}) P_{l}, \tag{2}
$$

*Electronic address: dolg@mpipks-dresden.mpg.de

where $P_l$ is the projection operator onto the Hilbert subspace of angular momentum $l$. The spin-orbit term $V_{so}$ may be written as

$$
V_{so}=\sum_{i} \sum_{l>0, k} \frac{2}{2 l+1} B_{l k} \exp \left(-b_{l k} r_{i}^{2}\right) P_{l} \boldsymbol{l}_{i} \mathbf{s}_{i} P_{l}. \quad (3)
$$

The free parameters $A_{l k}$, $a_{l k}$, $B_{l k}$, and $b_{l k}$ are adjusted to reproduce the valence total energies of a multitude of low-lying electronic states of the neutral atom and its ions. The necessary reference data have been taken from relativistic all-electron calculations. In the present work accurate small-core PPs for Ac to Lr have been used, e.g., the $1s$-$4f$ shells were included in the PP core, while the shells with main quantum number 5 and higher were treated explicitly. The orbitals were described by medium-sized one-particle basis sets, which are also suitable for calculations of small molecules, i.e., $(12s11p10d8f4g)/[8s7p6d4f4g]$.

All scalar-relativistic calculations were carried out with the MOLPRO ab initio program package [9]. The atomic orbitals were optimized in state-averaged complete active space multiconfiguration self-consistent field (CASSCF) calculations. Dynamic correlation was then accounted for by all single and double excitations from the CASSCF reference in averaged coupled-pair functional (ACPF) calculations [10]. The active space in the CASSCF calculations comprised all open-shell orbitals ($5f$, $6d$, and $7s$). In the ACPF calculations excitations were also allowed from the semicore orbitals ($6p$ and in some cases also $6s$ and $5d$). No excitations were allowed from the $5s$ and $5p$ shells in both the CASSCF and ACPF calculations, however; the orbitals were optimized for each state.

Spin-orbit coupling was taken into account by complete configuration-interaction calculations within all open-shell orbitals. The corresponding corrections derived from calculations with and without $V_{so}$ were then added to the scalarrelativistic ACPF results. All possible values of the total angular momentum $J$ were investigated in the intermediate coupling scheme and those giving the lowest energy were used to derive the corrections. All ACPF results reported here include spin-orbit corrections. Spin-orbit contributions were found to amount to only a few tenths of an electron volt in cases where the $f$ and $d$ occupation does not change; however, they are sometimes larger than 1 eV in other cases. Modified versions of the finite-difference programs MCHF [11] and GRASP [12] were applied. Due to the use of the state-averaging technique in calculations using MOLPRO and the exploitation of the spherical symmetry in MCHF and GRASP, all ab initio results of this work were obtained with eigenfunctions of the appropriate parity and angular momentum operators.

### B. DFT
The applied four-component Beijing density-functional program package (BDF) also has been described elsewhere [13,14]. Briefly, the one-electron Dirac-Kohn-Sham equation based on the Dirac-Coulomb Hamiltonian under the so-called no-pair approximation is solved directly, i.e.,

$$
\left[c \boldsymbol{\alpha} \cdot \mathbf{p}+(\beta-1) c^{2}+V(\mathbf{r})\right] \varphi_{j}(\mathbf{r})=\epsilon_{j} \varphi_{j}(\mathbf{r}), \quad (4)
$$

with the potential

$$
V(\mathbf{r})=V_{e x t}(\mathbf{r})+V_{c}(\mathbf{r})+V_{x c}[\rho(\mathbf{r})]. \quad (5)
$$

In Eq. (4) $\mathbf{p}=i \nabla$ is the usual momentum operator and $c$ denotes the speed of light (137.037 a.u.). $\boldsymbol{\alpha}$ and $\beta$ are the Dirac matrices

$$
\boldsymbol{\alpha}=\left(\begin{array}{cc}
0 & \boldsymbol{\sigma} \\
\boldsymbol{\sigma} & 0
\end{array}\right), \quad \beta=\left(\begin{array}{cc}
I & 0 \\
0 & -I
\end{array}\right), \quad (6)
$$

where $\boldsymbol{\sigma}$ represents the vector of the $2 \times 2$ Pauli spin matrices $(\sigma_{x}, \sigma_{y}, \sigma_{z})$ and $I$ is the $2 \times 2$ unit matrix. The external, Coulomb, and exchange-correlation potentials in Eq. (5) are, respectively,

$$
V_{e x t}(\mathbf{r})=-\sum_{A} \frac{Z_{A}}{\left|\mathbf{R}_{A}-\mathbf{r}\right|}, \quad (7)
$$

$$
V_{c}(\mathbf{r})=\int \frac{\rho\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} d \mathbf{r}^{\prime}, \quad (8)
$$

$$
V_{x c}[\rho(\mathbf{r})]=\frac{\delta E_{x c}[\rho(\mathbf{r})]}{\delta \rho}. \quad (9)
$$

The charge density reads

$$
\rho(\mathbf{r})=\sum_{j}^{o c c} n_{j} \varphi_{j}^{\dagger}(\mathbf{r}) \varphi_{j}(\mathbf{r}). \quad (10)
$$

The approximate forms for the exchange-correlation potential $V_{x c}[\rho(\mathbf{r})]$ employed in this work are the Perdew-Wang formula [15] within the local-density approximation (LDA), a self-interaction correction (SIC) according to Stoll et al. [16]. We have compared the results derived from different gradient exchange-correlation functionals [17–20] and found that they differ only marginally. So here we only report the results by gradient exchange corrections according to Becke [17] and gradient correlation corrections according to Perdew [19]. Taking uranium ($Z=92$), lawrencium ($Z=103$), and eka-merkury ($Z=112$) as examples, we noticed that relativistic corrections to the nonrelativistic density functionals [21] change the first and second ionization potentials by less than 0.1 eV and the third and fourth ionization potentials by less than $0.2\ \text{eV}\ (1\%)$. The nuclear model, finite size or a point charge, also has negligible influence on the energy differences. It is safe to directly use nonrelativistic functionals and a point nucleus model in relativistic calculations, at least, of valence-electron properties. This conclusion extends the previous discovery on the gold atom [22] to actinides and superheavy elements.

The atoms were treated in the same manner as molecules in the calculations by using the double point $D_{\infty h}^{*}$ group. The $jj$-coupling scheme was used and Kramer's degeneracy was adopted to carry out moment-polarized calculations for open shells in the same way as nonrelativistic polarization calculations. It is generally difficult for any one-determinant approach to properly describe a non-half-filled open shell. Although some recipes, e.g., the sum method of Ziegler et al. [23], can be used to calculate multiplet states correctly in

some cases, they cannot be easily applied to all the configurations involved in this work under the $jj$-coupling scheme. In addition, the presently available approximate density functionals suffer from the unphysical nondegeneracy problem [14], which leads to a biased description of multiplet states. Alternatively, however, one can assume that the intershell electron coupling is much weaker than the intrashell electron coupling and thus for a shell one can simply use equally averaged (fractional) occupancy and then construct the final state coupled by different shells. Of course, this means that such calculations are not describing the true terms of a configuration except some special cases, but it is still meaningful since only energy differences are concerned here: The lowest energies of the involved configurations have to be obtained anyway. For the configurations considered here the highest possible moment polarization was always generated. Specifically, the $5f$ shell was occupied as follows: Electrons 1-3 occupy $5f_{5/2}$ with moment up and electrons 4-7 occupy $5f_{7/2}$ with moment up; then, electrons 8-10 occupy $5f_{5/2}$ with moment down and finally electrons 11-14 occupy $5f_{7/2}$ with moment down. $6d_{3/2}$ and $7s_{1/2}$ were always occupied with moment up when occupied with a single electron. Keeping fixed the highest possible moment polarization, we then used fractional occupation numbers for all moment-polarized subshells with incomplete filling, e.g., for a $5f^1$ configuration each of the three $5f_{5/2,m_j}$ spinors with moment up was occupied by 1/3 electrons. A final remark appears to be in order here: Although our program works in the $jj$-coupling scheme, we have to account for the fact that the actinides are still closer to the nonrelativistic $LS$-coupling scheme. Therefore, instead of filling first $5f_{5/2}$ and afterward $5f_{7/2}$, we used the prescription given above, which also leads to lower total energies.

The generalized Gauss-Laguerre quadrature [24] and Lebedev quadrature [25] were employed to calculate the radial and angular integrals, respectively. The numerical accuracy of total energies can be further improved to better than 0.01 eV by the generalized transition-state method [26]. The frozen-core approximation, i.e., $[1s^2$-$5d^{10}]$, was employed for all the calculations. Although it is necessary to include $5s$, $5p$, and $5d$ shells in the valence in an accurate $ab$ $initio$ correlation treatment, the relaxation of these shells in the present DFT calculations reduces the total energies only by 0.001 a.u. and has essentially no influence on energy differences. Four-component numerical atomic spinors obtained by moment-restricted finite-difference atomic calculations were used for the cores, while the basis sets for the valence orbitals were combinations of the numerical atomic spinors and kinetically balanced double-$\zeta$ Slater-type functions. Such basis sets result in errors less than 0.05 eV.

### III. RESULTS AND DISCUSSION

The results of our calculations are listed in Tables I-IV for the first to fourth ionization potential, respectively. The results for $df$ and $fd$ excitation energies are given in Tables V and VI, respectively. Previous theoretical as well as available experimental data are also included. Due to the lack of complete sets of experimental data, the discussion is less straightforward for actinides than for lanthanides. Let us begin with the first ionization potentials (Table I), where almost all experimental values are known. The mean absolute errors of our calculations range from 0.41 eV to 0.16 eV, depending on the applied method. It is discernable that the relativistic analog to the local spin-density approximation yields very good results and further gradient corrections do not introduce significant and systematic improvements. Both relativistically and self-interaction corrected local-density functional (RLDASIC) results of Forstreuter [27] are of the same quality, i.e., the mean absolute error is 0.23 eV. However, their result for Th shows an error of 0.81 eV. An even larger error of 0.98 eV is present in the data for Th of Kotochigova $et$ $al$. [28], whereas their results for Ac, Pa, and U agree better with our than with Forstreuter's [27] values. We currently have no explanation for these findings. No experimental value exists for Lr; however, a quite reliable theoretical result has been provided by Eliav and Kaldor [6], who performed fully relativistic coupled-cluster calculations using very large one-particle basis sets. Their values for the $f^{14}s^2p_{1/2}^1$→$f^{14}s^2$ ionization process, i.e., 4.90 eV (Dirac-Coulomb-Hamiltonian) and 4.89 eV (Dirac-Coulomb-Breit-Hamiltonian), are bracketed by our DFT results (4.47 - 4.62 eV) and PP result (5.28 eV). Although the theoretical level of the calculation by Eliav and Kaldor is certainly higher than that of our methods, we want to point out that due to technical limitations (at most two electrons outside a closed shell or two holes in a closed shell) their approach cannot be used to study the whole actinide series. Moreover, at present their large one-particle basis set cannot be used for molecular calculations. Both constraints are not present for our methods.

For the second (Table II), third (Table III), and fourth (Table IV) ionization potentials the present DFT and PP results show similar trends along the series. The agreement between our results and those of Forstreuter [27] is not as good as for the first ionization potentials, but the trends are rather similar. The differences between our DFT and $ab$ $initio$ results tends to be larger for the second half than for the first half of the series. It is remarkable that in the second half of the series the DFT values are always larger than the PP values. We attribute the possibly too low $ab$ $initio$ values to an incomplete accounting for differential electron correlation effects, especially for the third and fourth ionization potentials. In the ionization process for systems with more than seven $f$ electrons an electron pair in the $f$ shell is broken up. Since the correlation treatment is not perfect, e.g., due to the neglect of higher angular momentum basis functions as well as higher excitations in the wave function, the final state is treated slightly better than the initial state and the energy difference turns out to be a bit too low. On the other hand, our experience from the lanthanide atoms [5] indicates that the DFT values might be slightly too high. In fact, there we found that for the second to fourth ionization potentials our DFT and $ab$ $initio$ results either quite accurately reproduce or at least bracket the experimental values. Actually, the average of our DFT and $ab$ $initio$ results for the third and fourth ionization potentials of the lanthanides are even closer to the experimental data, e.g., the mean absolute error being 0.21 and 0.27 eV, the largest relative error being 1.6% and 1.8%, respectively. We believe that, if the tendency found for the lanthanides also holds for the actinides, the present values for the second to fourth ionization potentials, or empirically

<table><caption>TABLE I. First ionization potential (in eV) for the the actinide atoms from the present fully relativistic density-functional calculations (BDF [13,14]) [LDASIC: local-density approximation [15] (LDA) with a self-interaction correction (SIC) [16]; $B$, Becke gradient exchange correction [17]; BP, Becke gradient exchange [17] and Perdew gradient correlation [19] correction] and quasirelativistic (QR) $ab$ initio pseudopotential (PP) calculations [8] (ACPF: averaged coupled-pair functional [10] with spin-orbit coupling corrections) in comparison to other theoretical results (RLDA: relativistically corrected LDA [28]; RLDASIC: relativistically corrected LDA with SIC [27]) and experimental data (Expt. [4]). The mean absolute error (MAE) and the largest relative error (LRE) are also given.</caption>
<table>
<thead>
<tr>
<th rowspan="2">Atom</th>
<th rowspan="2">Configurations</th>
<th colspan="3">BDF</th>
<th colspan="3">Other DFT</th>
<th colspan="2">QR PP</th>
<th rowspan="2">Expt.</th>
</tr>
<th>LDASIC</th>
<th>$B$</th>
<th>BP</th>
<th>RLDASIC</th>
<th>RLDA</th>
<th>ACPF</th>
<th>$+6s$ d</th>
<th>$+5d$ e</th>
</tr>
</thead>
<tbody>
<tr>
<td>89Ac</td>
<td>$f^{0}d^{1}s^{2}\rightarrow f^{0}d^{0}s^{2}$</td>
<td>5.08</td>
<td>5.14</td>
<td>5.07</td>
<td>5.72</td>
<td>5.29</td>
<td>5.04</td>
<td>5.06</td>
<td>4.97</td>
<td>$5.17\pm 0.12$</td>
</tr>
<tr>
<td>90Th</td>
<td>$f^{0}d^{2}s^{2}\rightarrow f^{0}d^{2}s^{1}$</td>
<td>6.07</td>
<td>6.15</td>
<td>5.91</td>
<td>6.89</td>
<td>7.06</td>
<td>6.06</td>
<td>6.05</td>
<td>6.06</td>
<td>$6.08\pm 0.12$</td>
</tr>
<tr>
<td>91Pa</td>
<td>$f^{2}d^{1}s^{2}\rightarrow f^{2}d^{0}s^{2}$</td>
<td>5.53</td>
<td>5.58</td>
<td>5.52</td>
<td>6.13</td>
<td>5.58</td>
<td>5.66</td>
<td></td>
<td></td>
<td>$5.89\pm 0.12$</td>
</tr>
<tr>
<td>92U</td>
<td>$f^{3}d^{1}s^{2}\rightarrow f^{3}d^{0}s^{2}$</td>
<td>5.62</td>
<td>5.66</td>
<td>5.61</td>
<td>6.22</td>
<td>5.61</td>
<td>5.91</td>
<td></td>
<td></td>
<td>6.19</td>
</tr>
<tr>
<td rowspan="2">93Np</td>
<td>$f^{4}d^{1}s^{2}\rightarrow f^{4}d^{1}s^{1}$ a</td>
<td>6.00</td>
<td>6.10</td>
<td>5.85</td>
<td>6.27</td>
<td></td>
<td>5.73</td>
<td></td>
<td></td>
<td>6.26</td>
</tr>
<tr>
<td>$f^{5}d^{0}s^{2}\rightarrow f^{5}d^{0}s^{1}$ b</td>
<td>5.65</td>
<td>5.75</td>
<td>5.52</td>
<td></td>
<td></td>
<td>5.53</td>
<td>5.53</td>
</tr>
<tr>
<td>94Pu</td>
<td>$f^{6}d^{0}s^{2}\rightarrow f^{6}d^{0}s^{1}$</td>
<td>5.69</td>
<td>5.78</td>
<td>5.55</td>
<td>6.01</td>
<td></td>
<td>5.76</td>
<td>5.77</td>
</tr>
<tr>
<td>95Am</td>
<td>$f^{7}d^{0}s^{2}\rightarrow f^{7}d^{0}s^{1}$</td>
<td>5.72</td>
<td>5.82</td>
<td>5.58</td>
<td>6.07</td>
<td></td>
<td>5.74</td>
<td>5.75</td>
</tr>
<tr>
<td rowspan="2">96Cm</td>
<td>$f^{7}d^{1}s^{2}\rightarrow f^{7}d^{0}s^{2}$ a</td>
<td>5.71</td>
<td>5.73</td>
<td>5.67</td>
<td>6.29</td>
<td></td>
<td>5.47</td>
<td></td>
<td></td>
<td>6.02</td>
</tr>
<tr>
<td>$f^{8}d^{0}s^{2}\rightarrow f^{8}d^{0}s^{1}$ b</td>
<td>5.87</td>
<td>5.96</td>
<td>5.72</td>
<td></td>
<td></td>
<td>5.74</td>
<td>5.75</td>
</tr>
<tr>
<td>97Bk</td>
<td>$f^{9}d^{0}s^{2}\rightarrow f^{9}d^{0}s^{1}$</td>
<td>6.00</td>
<td>6.09</td>
<td>5.86</td>
<td>6.36</td>
</tr>
<tr>
<td>98Cf</td>
<td>$f^{10}d^{0}s^{2}\rightarrow f^{10}d^{0}s^{1}$</td>
<td>6.11</td>
<td>6.20</td>
<td>5.97</td>
<td>6.48</td>
</tr>
<tr>
<td>99Es</td>
<td>$f^{11}d^{0}s^{2}\rightarrow f^{11}d^{0}s^{1}$</td>
<td>6.24</td>
<td>6.33</td>
<td>6.10</td>
<td>6.60</td>
</tr>
<tr>
<td>100Fm</td>
<td>$f^{12}d^{0}s^{2}\rightarrow f^{12}d^{0}s^{1}$</td>
<td>6.36</td>
<td>6.44</td>
<td>6.22</td>
<td>6.70</td>
</tr>
<tr>
<td>101Md</td>
<td>$f^{13}d^{0}s^{2}\rightarrow f^{13}d^{0}s^{1}$</td>
<td>6.47</td>
<td>6.55</td>
<td>6.33</td>
<td>6.80</td>
</tr>
<tr>
<td>102No</td>
<td>$f^{14}d^{0}s^{2}\rightarrow f^{14}d^{0}s^{1}$</td>
<td>6.54</td>
<td>6.62</td>
<td>6.40</td>
<td>6.92</td>
</tr>
<tr>
<td rowspan="2">103Lr</td>
<td>$f^{14}d^{1}s^{2}\rightarrow f^{14}d^{0}s^{2}$ b,c</td>
<td>4.70</td>
<td>4.73</td>
<td>4.61</td>
<td>5.37</td>
</tr>
<tr>
<td>$f^{14}d^{0}s^{2}p^{1}\rightarrow f^{14}d^{0}s^{2}$ c</td>
<td>4.54</td>
<td>4.62</td>
<td>4.55</td>
<td></td>
</tr>
<tr>
<td></td>
<td>MAE (eV)</td>
<td>0.23</td>
<td>0.16</td>
<td>0.34</td>
<td>0.23</td>
<td></td>
<td>0.34</td>
<td></td>
</tr>
<tr>
<td></td>
<td>LRE (%)</td>
<td>9.2</td>
<td>8.6</td>
<td>9.4</td>
<td>13.3</td>
</tr>
</tbody>
</table>
</table>

$^{a}$Experimentally measured lowest configurations.

$^{b}$DFT calculated lowest configurations.

$^{c}$The relativistic all-electron coupled-cluster calculations of Lr with an uncontracted $(34s25p21d15f10g6h)$ basis set predicted that the $f^{14}d^{0}s^{2}p_{1/2}^{1}$ configuration is lower than $f^{14}d_{3/2}^{1}s^{2}$ by 0.16 eV. The first ionization potential is 4.90 eV (Dirac-Coulomb Hamiltonian), or 4.89 eV (Dirac-Coulomb-Breit Hamiltonian), taking $f^{14}d^{0}s^{2}p_{1/2}^{1}$ as the ground state, whereas it is 4.73 eV with respect to $f^{14}d_{3/2}^{1}s^{2}$ [6].

$^{d}$6s orbitals were also correlated.

$^{e}$5d orbitals were also correlated.

the average of the corresponding DFT and $ab$ initio results, also should be close to the yet unknown experimental values. This speculation is further supported by the quite good agreement of the present results for the first ionization potentials as well as $df$ and $fd$ excitation energies with experimental data.

A further result for uranium, the most extensively studied element among the actinides, can be discussed. Besides the first to fourth ionization potentials, our DFT and $ab$ initio results for the fifth ionization potential of U [47.38, 47.47, and 47.25 eV for the LDA SIC, Becke ($B$), and Becke-Perdew (BP) results, respectively, by BDF and 47.26 eV by ACPF including excitations from $5d$, $5f$, $6s$, and $6p$] are also in good agreement with each other as well as with Eliav and Kaldor's relativistic coupled-cluster calculation (47.28 eV) [29]. However, the experimental values for the second to fourth ionization potentials were not decisively determined and several values for each ionization potential exist (cf. Tables II–IV). The present calculations do not coincide well with all these values and therefore more accurate experimental measurements need to be performed.

For the lighter actinides experimental data exist also for $df$ and $fd$ excitation energies and allows us to calibrate the accuracy of our methods. For both series our DFT and $ab$ initio results are quite close to the available experimental values and often bracket them (Tables V and VI). Our results are in considerably better agreement with each other and also with experiment than previous discrete-variational $X\alpha$ calculations of Fricke <i>et al.</i> [30]. Although the agreement is relatively good at the beginning of the series, their $X\alpha$ values increase much faster than our values along the series. For No the discrepancies amount to 6 eV and 10 eV for the $df$ and $fd$ excitation energies, respectively. In order to find the possible reason for this disagreement we performed $X\alpha$ calculations (without self-interaction correction) for Es and No. The results, 2.42 (4.71) eV for the $df$ excitation and 6.52 (8.30) eV for the $fd$ excitation, agree within 0.3 eV with our LDA data for Es (No). The value for the $df$ excitation of Es

<table>
<caption>TABLE II. Second ionization potential (in eV). For other explanations see Table I.</caption>
<thead>
<tr>
<th rowspan="2">Atom</th>
<th rowspan="2">Configurations</th>
<th colspan="3">BDF</th>
<th colspan="2">Other DFT</th>
<th colspan="2">QR PP</th>
<th rowspan="2">Expt.</th>
</tr>
<tr>
<td>LDASIC</td>
<td>$B$</td>
<td>BP</td>
<td>RLDASIC</td>
<td>ACPF</td>
<td>$+6s$ c</td>
<td>$+5d$ d</td>
</tr>
</thead>
<tbody>
<tr>
<td>89Ac</td>
<td>$f^{0}d^{0}s^{2}\rightarrow f^{0}d^{0}s^{1}$</td>
<td>11.56</td>
<td>11.63</td>
<td>11.45</td>
<td>11.93</td>
<td>11.49</td>
<td>11.50</td>
<td>11.54</td>
<td>11.78$\pm 0.19$</td>
</tr>
<tr>
<td>90Th</td>
<td>$f^{0}d^{2}s^{1}\rightarrow f^{1}d^{1}s^{0}$</td>
<td>11.93</td>
<td>11.96</td>
<td>11.98</td>
<td>11.08</td>
<td>12.87</td>
<td>12.82</td>
<td>12.43</td>
<td></td>
</tr>
<tr>
<td>91Pa</td>
<td>$f^{2}d^{0}s^{2}\rightarrow f^{2}d^{1}s^{0}$</td>
<td>12.27</td>
<td>12.32</td>
<td>12.07</td>
<td>12.39</td>
<td>12.85</td>
<td>12.75</td>
<td></td>
<td></td>
</tr>
<tr>
<td>92U</td>
<td>$f^{3}d^{0}s^{2}\rightarrow f^{4}d^{0}s^{0}$</td>
<td>12.12</td>
<td>12.15</td>
<td>11.89</td>
<td>12.58</td>
<td>12.00</td>
<td>12.02</td>
<td></td>
<td>11.07 or 11.45 or 11.59$\pm 0.37$</td>
</tr>
<tr>
<td>93Np</td>
<td>$f^{4}d^{1}s^{1}\rightarrow f^{5}d^{0}s^{0}$ a</td>
<td>11.05</td>
<td>11.01</td>
<td>10.93</td>
<td>12.77</td>
<td>12.38</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$f^{5}d^{0}s^{1}\rightarrow f^{5}d^{0}s^{0}$ b</td>
<td>11.67</td>
<td>11.69</td>
<td>11.55</td>
<td></td>
<td>11.36</td>
<td>11.35</td>
<td></td>
<td></td>
</tr>
<tr>
<td>94Pu</td>
<td>$f^{6}d^{0}s^{1}\rightarrow f^{6}d^{0}s^{0}$</td>
<td>11.85</td>
<td>11.87</td>
<td>11.72</td>
<td>12.14</td>
<td>11.45</td>
<td>11.44</td>
<td></td>
<td></td>
</tr>
<tr>
<td>95Am</td>
<td>$f^{7}d^{0}s^{1}\rightarrow f^{7}d^{0}s^{0}$</td>
<td>12.02</td>
<td>12.04</td>
<td>11.89</td>
<td>12.32</td>
<td>11.74</td>
<td>11.73</td>
<td></td>
<td></td>
</tr>
<tr>
<td>96Cm</td>
<td>$f^{7}d^{0}s^{2}\rightarrow f^{8}d^{0}s^{0}$ a</td>
<td>11.44</td>
<td>11.55</td>
<td>11.39</td>
<td>13.26</td>
<td>12.33</td>
<td>12.18</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$f^{8}d^{0}s^{1}\rightarrow f^{8}d^{0}s^{0}$ b</td>
<td>12.15</td>
<td>12.18</td>
<td>12.01</td>
<td></td>
<td>11.92</td>
<td>11.91</td>
<td></td>
<td></td>
</tr>
<tr>
<td>97Bk</td>
<td>$f^{9}d^{0}s^{1}\rightarrow f^{9}d^{0}s^{0}$</td>
<td>12.28</td>
<td>12.31</td>
<td>12.13</td>
<td>12.58</td>
<td>11.97</td>
<td>11.95</td>
<td></td>
<td></td>
</tr>
<tr>
<td>98Cf</td>
<td>$f^{10}d^{0}s^{1}\rightarrow f^{10}d^{0}s^{0}$</td>
<td>12.40</td>
<td>12.44</td>
<td>12.25</td>
<td>12.72</td>
<td>12.06</td>
<td>12.05</td>
<td></td>
<td></td>
</tr>
<tr>
<td>99Es</td>
<td>$f^{11}d^{0}s^{1}\rightarrow f^{11}d^{0}s^{0}$</td>
<td>12.53</td>
<td>12.57</td>
<td>12.37</td>
<td>12.85</td>
<td>12.20</td>
<td>12.18</td>
<td></td>
<td></td>
</tr>
<tr>
<td>100Fm</td>
<td>$f^{12}d^{0}s^{1}\rightarrow f^{12}d^{0}s^{0}$</td>
<td>12.66</td>
<td>12.70</td>
<td>12.49</td>
<td>12.99</td>
<td>12.42</td>
<td>12.41</td>
<td></td>
<td></td>
</tr>
<tr>
<td>101Md</td>
<td>$f^{13}d^{0}s^{1}\rightarrow f^{13}d^{0}s^{0}$</td>
<td>12.79</td>
<td>12.84</td>
<td>12.61</td>
<td>13.13</td>
<td>12.42</td>
<td>12.40</td>
<td></td>
<td></td>
</tr>
<tr>
<td>102No</td>
<td>$f^{14}d^{0}s^{1}\rightarrow f^{14}d^{0}s^{0}$</td>
<td>12.92</td>
<td>12.97</td>
<td>12.73</td>
<td>13.27</td>
<td>12.52</td>
<td>12.51</td>
<td></td>
<td></td>
</tr>
<tr>
<td>103Lr</td>
<td>$f^{14}d^{0}s^{2}\rightarrow f^{14}d^{0}s^{1}$</td>
<td>14.46</td>
<td>14.53</td>
<td>14.26</td>
<td>14.87</td>
<td>14.22</td>
<td>14.21</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

aExperimentally measured lowest configurations.
bDFT calculated lowest configurations.
c$6s$ orbitals were also correlated.
d$5d$ orbitals were also correlated.

almost coincides with the experimental result of 2.40 eV. This clearly shows that the differences between our results and those of Fricke *et al.* [30] are not related to the use of different density functionals.

Finally, we want to make some additional comments on the methods applied here. The *ab initio* approaches appear to suffer from the too slow convergence of the configuration-interaction expansion of the wave function. States with higher $f$ occupation are less well described than states with a lower $f$ occupation, i.e., differential correlation effects are not sufficiently accounted for, leading to slightly biased ionization or excitation energies. Moreover, at present the spin-orbit interaction cannot be treated together with the electron correlation, but instead the corresponding corrections have to be taken from limited configuration-interaction calculations in the intermediate coupling scheme and then added to the highly correlated scalar-relativistic results. The DFT calculations presented here do not suffer from these problems; however, they have the disadvantage that they cannot be improved in a systematic way. Moreover, DFT mainly accounts

<table>
<caption>TABLE III. Third ionization potential (in eV). For other explanations see Table I.</caption>
<thead>
<tr>
<th rowspan="2">Atom</th>
<th rowspan="2">Configurations</th>
<th colspan="3">BDF</th>
<th rowspan="2">ACPF</th>
<th colspan="2">QR PP</th>
<th rowspan="2">Expt.</th>
</tr>
<tr>
<td>LDASIC</td>
<td>$B$</td>
<td>BP</td>
<td>$+6s$ a</td>
<td>$+5d$ b</td>
</tr>
</thead>
<tbody>
<tr>
<td>89Ac</td>
<td>$f^{0}d^{0}s^{1}\rightarrow f^{0}d^{0}s^{0}$</td>
<td>17.43</td>
<td>17.48</td>
<td>17.28</td>
<td>16.93</td>
<td>17.24</td>
<td>17.29</td>
<td></td>
</tr>
<tr>
<td>90Th</td>
<td>$f^{1}d^{1}s^{0}\rightarrow f^{1}d^{0}s^{0}$</td>
<td>17.70</td>
<td>17.77</td>
<td>17.61</td>
<td>17.90</td>
<td>17.94</td>
<td></td>
<td>18.33</td>
</tr>
<tr>
<td>91Pa</td>
<td>$f^{2}d^{1}s^{0}\rightarrow f^{2}d^{0}s^{0}$</td>
<td>18.15</td>
<td>18.20</td>
<td>18.05</td>
<td>17.61</td>
<td>17.67</td>
<td></td>
<td></td>
</tr>
<tr>
<td>92U</td>
<td>$f^{4}d^{0}s^{0}\rightarrow f^{3}d^{0}s^{0}$</td>
<td>18.86</td>
<td>18.94</td>
<td>18.77</td>
<td>18.62</td>
<td>18.74</td>
<td>18.61</td>
<td>17.73 or 17.92 or 19.80$\pm 0.31$</td>
</tr>
<tr>
<td>93Np</td>
<td>$f^{5}d^{0}s^{0}\rightarrow f^{4}d^{0}s^{0}$</td>
<td>20.16</td>
<td>20.25</td>
<td>20.09</td>
<td>19.38</td>
<td>19.52</td>
<td>19.37</td>
<td></td>
</tr>
<tr>
<td>94Pu</td>
<td>$f^{6}d^{0}s^{0}\rightarrow f^{5}d^{0}s^{0}$</td>
<td>21.39</td>
<td>21.47</td>
<td>21.31</td>
<td>21.15</td>
<td>21.27</td>
<td>21.10</td>
<td></td>
</tr>
<tr>
<td>95Am</td>
<td>$f^{7}d^{0}s^{0}\rightarrow f^{6}d^{0}s^{0}$</td>
<td>22.74</td>
<td>22.84</td>
<td>22.70</td>
<td>21.90</td>
<td>21.99</td>
<td>21.74</td>
<td></td>
</tr>
<tr>
<td>96Cm</td>
<td>$f^{8}d^{0}s^{0}\rightarrow f^{7}d^{0}s^{0}$</td>
<td>21.53</td>
<td>21.52</td>
<td>21.19</td>
<td>20.55</td>
<td>20.55</td>
<td>20.31</td>
<td></td>
</tr>
<tr>
<td>97Bk</td>
<td>$f^{9}d^{0}s^{0}\rightarrow f^{8}d^{0}s^{0}$</td>
<td>22.85</td>
<td>22.85</td>
<td>22.54</td>
<td>21.75</td>
<td>21.87</td>
<td>21.71</td>
<td></td>
</tr>
<tr>
<td>98Cf</td>
<td>$f^{10}d^{0}s^{0}\rightarrow f^{9}d^{0}s^{0}$</td>
<td>24.09</td>
<td>24.12</td>
<td>23.81</td>
<td>22.81</td>
<td>22.90</td>
<td>22.62</td>
<td></td>
</tr>
<tr>
<td>99Es</td>
<td>$f^{11}d^{0}s^{0}\rightarrow f^{10}d^{0}s^{0}$</td>
<td>23.52</td>
<td>23.56</td>
<td>23.27</td>
<td>22.12</td>
<td>22.23</td>
<td>21.93</td>
<td></td>
</tr>
<tr>
<td>100Fm</td>
<td>$f^{12}d^{0}s^{0}\rightarrow f^{11}d^{0}s^{0}$</td>
<td>24.60</td>
<td>24.65</td>
<td>24.37</td>
<td>22.75</td>
<td>22.87</td>
<td>22.56</td>
<td></td>
</tr>
<tr>
<td>101Md</td>
<td>$f^{13}d^{0}s^{0}\rightarrow f^{12}d^{0}s^{0}$</td>
<td>25.62</td>
<td>25.69</td>
<td>25.41</td>
<td>23.77</td>
<td>23.86</td>
<td>23.43</td>
<td></td>
</tr>
<tr>
<td>102No</td>
<td>$f^{14}d^{0}s^{0}\rightarrow f^{13}d^{0}s^{0}$</td>
<td>26.60</td>
<td>26.68</td>
<td>26.41</td>
<td>25.29</td>
<td>25.34</td>
<td>24.83</td>
<td></td>
</tr>
<tr>
<td>103Lr</td>
<td>$f^{14}d^{0}s^{1}\rightarrow f^{14}d^{0}s^{0}$</td>
<td>21.85</td>
<td>21.90</td>
<td>21.60</td>
<td>21.50</td>
<td>21.49</td>
<td>21.18</td>
<td></td>
</tr>
</tbody>
</table>

a$6s$ orbitals were also correlated.
b$5d$ orbitals were also correlated.

<table>
<caption>TABLE IV. Fourth ionization potential (in eV). For other explanations see Table I.</caption>
<tbody>
<tr>
<td rowspan="2">Atom</td>
<td rowspan="2">Configurations</td>
<td rowspan="2">LDASIC</td>
<td colspan="3">BDF</td>
<td colspan="2">QR PP</td>
<td rowspan="2">Expt.</td>
</tr>
<tr>
<td>$B$</td>
<td>BP</td>
<td>ACPF</td>
<td>$+6s$ a</td>
<td>$+5d$ b</td>
</tr>
<tr>
<td>89Ac</td>
<td>$5s^{2}5p^{6}\rightarrow5s^{2}5p^{5}$</td>
<td>44.10</td>
<td>44.17</td>
<td>43.96</td>
<td>44.15</td>
<td>43.64</td>
<td>43.78</td>
<td></td>
</tr>
<tr>
<td>90Th</td>
<td>$f^{1}d^{0}s^{0}\rightarrow f^{0}d^{0}s^{0}$</td>
<td>28.97</td>
<td>29.04</td>
<td>28.83</td>
<td>27.93</td>
<td>28.06</td>
<td>27.78</td>
<td>28.65</td>
</tr>
<tr>
<td>91Pa</td>
<td>$f^{2}d^{0}s^{0}\rightarrow f^{1}d^{0}s^{0}$</td>
<td>30.95</td>
<td>31.03</td>
<td>30.83</td>
<td>32.26</td>
<td>32.37</td>
<td>32.12</td>
<td></td>
</tr>
<tr>
<td>92U</td>
<td>$f^{3}d^{0}s^{0}\rightarrow f^{2}d^{0}s^{0}$</td>
<td>32.78</td>
<td>32.87</td>
<td>32.68</td>
<td>32.56</td>
<td>32.65</td>
<td>32.36</td>
<td>30.33 or 31.12 or 36.70±0.99</td>
</tr>
<tr>
<td>93Np</td>
<td>$f^{4}d^{0}s^{0}\rightarrow f^{3}d^{0}s^{0}$</td>
<td>33.54</td>
<td>33.63</td>
<td>33.45</td>
<td>33.68</td>
<td>33.77</td>
<td>33.51</td>
<td></td>
</tr>
<tr>
<td>94Pu</td>
<td>$f^{5}d^{0}s^{0}\rightarrow f^{4}d^{0}s^{0}$</td>
<td>35.14</td>
<td>35.24</td>
<td>35.07</td>
<td>34.90</td>
<td>35.04</td>
<td>34.86</td>
<td></td>
</tr>
<tr>
<td>95Am</td>
<td>$f^{6}d^{0}s^{0}\rightarrow f^{5}d^{0}s^{0}$</td>
<td>36.59</td>
<td>36.69</td>
<td>36.53</td>
<td>36.82</td>
<td>36.94</td>
<td>36.68</td>
<td></td>
</tr>
<tr>
<td>96Cm</td>
<td>$f^{7}d^{0}s^{0}\rightarrow f^{6}d^{0}s^{0}$</td>
<td>38.14</td>
<td>38.25</td>
<td>38.08</td>
<td>36.93</td>
<td>37.01</td>
<td>36.78</td>
<td></td>
</tr>
<tr>
<td>97Bk</td>
<td>$f^{8}d^{0}s^{0}\rightarrow f^{7}d^{0}s^{0}$</td>
<td>37.37</td>
<td>37.36</td>
<td>37.02</td>
<td>36.29</td>
<td>36.45</td>
<td>36.28</td>
<td></td>
</tr>
<tr>
<td>98Cf</td>
<td>$f^{9}d^{0}s^{0}\rightarrow f^{8}d^{0}s^{0}$</td>
<td>38.97</td>
<td>38.98</td>
<td>38.66</td>
<td>37.47</td>
<td>37.58</td>
<td>37.27</td>
<td></td>
</tr>
<tr>
<td>99Es</td>
<td>$f^{10}d^{0}s^{0}\rightarrow f^{9}d^{0}s^{0}$</td>
<td>40.51</td>
<td>40.54</td>
<td>40.22</td>
<td>38.69</td>
<td>38.77</td>
<td>38.41</td>
<td></td>
</tr>
<tr>
<td>100Fm</td>
<td>$f^{11}d^{0}s^{0}\rightarrow f^{10}d^{0}s^{0}$</td>
<td>39.92</td>
<td>39.97</td>
<td>39.67</td>
<td>39.09</td>
<td>39.20</td>
<td>38.79</td>
<td></td>
</tr>
<tr>
<td>101Md</td>
<td>$f^{12}d^{0}s^{0}\rightarrow f^{11}d^{0}s^{0}$</td>
<td>41.27</td>
<td>41.34</td>
<td>41.04</td>
<td>39.49</td>
<td>39.60</td>
<td>39.14</td>
<td></td>
</tr>
<tr>
<td>102No</td>
<td>$f^{13}d^{0}s^{0}\rightarrow f^{12}d^{0}s^{0}$</td>
<td>42.57</td>
<td>42.64</td>
<td>42.36</td>
<td>40.94</td>
<td>41.03</td>
<td>40.50</td>
<td></td>
</tr>
<tr>
<td>103Lr</td>
<td>$f^{14}d^{0}s^{0}\rightarrow f^{13}d^{0}s^{0}$</td>
<td>43.82</td>
<td>43.90</td>
<td>43.62</td>
<td>42.98</td>
<td>43.02</td>
<td>42.40</td>
<td></td>
</tr>
</tbody>
</table>

a6s orbitals were also correlated.
b5d orbitals were also correlated.

for dynamical correlation within the one-determinant formulation and sometimes fails to reproduce the correct ordering of near-degenerate configurations, e.g., for Np/Np⁺, Cm/ Cm⁺, and (possibly) Lr (cf. Tables I and II). The sources of errors occurring in $sp$ and $sd$ excitation energies of first-row and $3d$ atoms due to the local-density approximation for the exchange interaction have been analyzed in detail by Gunnarsson and Jones [31]. Their findings will also hold for the cases considered here. A possible way to further improve the present DFT calculations might be a more accurate treatment of the exchange; however, it is well known that a simple addition of Hartree-Fock (or Dirac-Hartree-Fock) exchange and DFT correlation does not yield satisfactory results. A promising but computationally more demanding approach is the coupling between multi-configurational wave-function-based methods, e.g., CASSCF, and DFT, which takes care of nondynamical and dynamical correlations, respectively [32]. Although some progress has been made with such hybrid schemes for small systems with main-group elements, their application to lanthanides and actinides appears to be out of reach at present.

### IV. CONCLUSIONS

Ab initio PP and DFT all-electron calculations have been performed for the whole series of actinide atoms. The results

<table>
<caption>TABLE V. $df$ excitation energies (eV) defined as $\Delta_{df}=E(f^{n}d^{1}s^{2})$-$E(f^{n+1}d^{0}s^{2})$ ($n=0-13$ for Ac-No). DV-$X\alpha$ (discrete variational) is from [30]. For other explanations see Table I.</caption>
<tbody>
<tr>
<td rowspan="2">Atom</td>
<td rowspan="2">LDASIC</td>
<td colspan="2">BDF</td>
<td>Other DFT</td>
<td>QR PP</td>
<td rowspan="2">Expt.</td>
</tr>
<tr>
<td>$B$</td>
<td>BP</td>
<td>DV-$X\alpha$</td>
<td>ACPF</td>
</tr>
<tr>
<td>89Ac</td>
<td>−3.10</td>
<td>−3.08</td>
<td>−3.14</td>
<td>−5.33</td>
<td></td>
<td>−3.72±0.37</td>
</tr>
<tr>
<td>90Th</td>
<td>−2.06</td>
<td>−2.04</td>
<td>−2.09</td>
<td>−3.59</td>
<td>−2.96</td>
<td>−2.44</td>
</tr>
<tr>
<td>91Pa</td>
<td>−1.10</td>
<td>−1.07</td>
<td>−1.12</td>
<td>−1.96</td>
<td>−1.94</td>
<td>−1.61</td>
</tr>
<tr>
<td>92U</td>
<td>−0.90</td>
<td>−0.84</td>
<td>−0.89</td>
<td>−0.41</td>
<td>−1.32</td>
<td>−0.87</td>
</tr>
<tr>
<td>93Np</td>
<td>0.27</td>
<td>0.32</td>
<td>0.29</td>
<td>1.28</td>
<td>−0.79</td>
<td>−0.35</td>
</tr>
<tr>
<td>94Pu</td>
<td>1.17</td>
<td>1.24</td>
<td>1.21</td>
<td>2.80</td>
<td>1.31</td>
<td>0.78</td>
</tr>
<tr>
<td>95Am</td>
<td>2.06</td>
<td>2.13</td>
<td>2.11</td>
<td>2.15</td>
<td>1.26</td>
<td>1.32</td>
</tr>
<tr>
<td>96Cm</td>
<td>0.87</td>
<td>0.86</td>
<td>0.67</td>
<td>3.62</td>
<td>−0.15</td>
<td>−0.15</td>
</tr>
<tr>
<td>97Bk</td>
<td>2.07</td>
<td>2.07</td>
<td>1.91</td>
<td>4.90</td>
<td>0.60</td>
<td>1.13</td>
</tr>
<tr>
<td>98Cf</td>
<td>3.21</td>
<td>3.24</td>
<td>3.10</td>
<td>6.34</td>
<td>1.58</td>
<td>2.10</td>
</tr>
<tr>
<td>99Es</td>
<td>2.58</td>
<td>2.61</td>
<td>2.49</td>
<td>7.51 a</td>
<td>2.20</td>
<td>2.40</td>
</tr>
<tr>
<td>100Fm</td>
<td>3.56</td>
<td>3.61</td>
<td>3.51</td>
<td>8.79</td>
<td>2.04</td>
<td>2.48±0.37</td>
</tr>
<tr>
<td>101Md</td>
<td>4.50</td>
<td>4.56</td>
<td>4.48</td>
<td>9.93</td>
<td>2.69</td>
<td></td>
</tr>
<tr>
<td>102No</td>
<td>4.60</td>
<td>4.73</td>
<td>4.65</td>
<td>11.27 b</td>
<td>4.61</td>
<td></td>
</tr>
<tr>
<td>MAE (eV)</td>
<td>0.64</td>
<td>0.67</td>
<td>0.59</td>
<td>2.60</td>
<td>0.37</td>
<td></td>
</tr>
</tbody>
</table>

aThe DV-$X\alpha$ result by BDF is 2.42 eV.
bThe DV-$X\alpha$ result by BDF is 4.71 eV.

TABLE VI. $fd$ excitation energies (eV) defined as $\Delta_{fd}=E(f^{n}d^{2}s^{2})$-$E(f^{n+1}d^{1}s^{2})$ ($n=0-13$ for Th-Lr). DV-$X\alpha$ is from [30]. For other explanations see Table I.

<table>
  <thead>
    <tr>
      <th rowspan="2">Atom</th>
      <th></th>
      <th colspan="2">BDF</th>
      <th>Other DFT</th>
      <th>QR PP</th>
      <th rowspan="2">Expt.</th>
    </tr>
    <tr>
      <th>LDASIC</th>
      <th>$B$</th>
      <th>BP</th>
      <th>DV-$X\alpha$</th>
      <th>ACPF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$^{90}$Th</td>
      <td>$-0.55$</td>
      <td>$-0.55$</td>
      <td>$-0.63$</td>
      <td>$-1.17$</td>
      <td>$-1.57$</td>
      <td>$-0.97$</td>
    </tr>
    <tr>
      <td>$^{91}$Pa</td>
      <td>$0.73$</td>
      <td>$0.75$</td>
      <td>$0.68$</td>
      <td>$1.20$</td>
      <td>$0.35$</td>
      <td>$0.25$</td>
    </tr>
    <tr>
      <td>$^{92}$U</td>
      <td>$1.96$</td>
      <td>$1.99$</td>
      <td>$1.93$</td>
      <td>$3.48$</td>
      <td>$1.22$</td>
      <td>$1.43$</td>
    </tr>
    <tr>
      <td>$^{93}$Np</td>
      <td>$2.20$</td>
      <td>$2.24$</td>
      <td>$2.19$</td>
      <td>$5.47$</td>
      <td>$1.73$</td>
      <td>$2.49$</td>
    </tr>
    <tr>
      <td>$^{94}$Pu</td>
      <td>$3.29$</td>
      <td>$3.36$</td>
      <td>$3.31$</td>
      <td>$7.48$</td>
      <td>$3.47$</td>
      <td>$3.69$</td>
    </tr>
    <tr>
      <td>$^{95}$Am</td>
      <td>$4.37$</td>
      <td>$4.45$</td>
      <td>$4.40$</td>
      <td>$9.42$</td>
      <td>$3.93$</td>
      <td>$5.60\pm0.62$</td>
    </tr>
    <tr>
      <td>$^{96}$Cm</td>
      <td>$5.39$</td>
      <td>$5.49$</td>
      <td>$5.45$</td>
      <td>$8.60$</td>
      <td>$3.59$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{97}$Bk</td>
      <td>$4.18$</td>
      <td>$4.18$</td>
      <td>$3.97$</td>
      <td>$10.31$</td>
      <td>$2.58$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{98}$Cf</td>
      <td>$5.52$</td>
      <td>$5.55$</td>
      <td>$5.36$</td>
      <td>$11.92$</td>
      <td>$4.73$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{99}$Es</td>
      <td>$6.83$</td>
      <td>$6.88$</td>
      <td>$6.71$</td>
      <td>$13.55$ $^{a}$</td>
      <td>$7.28$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{100}$Fm</td>
      <td>$6.06$</td>
      <td>$6.13$</td>
      <td>$5.98$</td>
      <td>$15.10$</td>
      <td>$4.68$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{101}$Md</td>
      <td>$7.21$</td>
      <td>$7.29$</td>
      <td>$7.15$</td>
      <td>$16.68$</td>
      <td>$5.57$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{102}$No</td>
      <td>$8.32$</td>
      <td>$8.41$</td>
      <td>$8.29$</td>
      <td>$18.20$ $^{b}$</td>
      <td>$6.12$</td>
      <td></td>
    </tr>
    <tr>
      <td>$^{103}$Lr</td>
      <td>$9.38$</td>
      <td>$9.49$</td>
      <td>$9.39$</td>
      <td></td>
      <td>$7.54$</td>
      <td></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="7">$^{a}$The DV-$X\alpha$ result by BDF is 6.52 eV.</td>
    </tr>
    <tr>
      <td colspan="7">$^{b}$The DV-$X\alpha$ result by BDF is 8.30 eV.</td>
    </tr>
  </tfoot>
</table>

for the first to fourth ionization potentials as well as the $df$ and $fd$ excitation energies of the neutral atoms show that the applied two approaches have a similar accuracy. In the case of the first ionization potential an almost complete set of reliable experimental data exists and the mean absolute error of our theoretical results is 0.35 eV or less. For higher ion- ization potentials as well as $df$ and $fd$ excitation energies the results of both approaches show the same qualitative trends along the series, although quantitatively, especially for the heavier elements, differences up to 5% are present. Never- theless, since the agreement of our independent calculations with the few available experimental values is better than the case of previous DFT studies, we believe that our data might be useful to guide further experimental work and that, in particular, the average of our DFT and $ab$ initio results for higher ionization potentials might be very close to the yet unknown experimental values.

## ACKNOWLEDGMENTS

The authors thank H. Eschrig and M. Richter for valuable discussions.

[1] *Handbook on the Physics and Chemistry of Rare Earths* (Elsevier, Amsterdam, 1978–1996), Vols. 1–22.

[2] M. Dolg and H. Stoll, in *Handbook on the Physics and Chem- istry of Rare Earths*, edited by K. A. Gschneidner, Jr. and L. Eyring (Elsevier, Amsterdam, 1996), Vol. 22, p. 607.

[3] W. C. Martin, R. Zalubas, and L. Hagan, *Atomic Energy Levels—The Rare Earth Elements*, Natl. Bur. Stand. Ref. Data Ser., Natl. Bur. Stand. (U.S.) Circ. No. 60 (U.S. GPO, Wash- ington, DC, 1978).

[4] J. Blaise and J.-F. Wyart, *Energy Levels and Atomic Spectra of Actinides*, in *International Tables of Selected Constants 20* (CNRS, Paris, 1992).

[5] W. Liu and M. Dolg, Phys. Rev. A **57**, 1721 (1998).

[6] E. Eliav and U. Kaldor, Phys. Rev. A **52**, 291 (1995).

[7] M. Dolg, H. Stoll, and H. Preuß, J. Chem. Phys. **90**, 1730 (1989).

[8] W. Küchle, M. Dolg, H. Stoll, and H. Preuß, J. Chem. Phys. **100**, 7535 (1994).

[9] Program system MOLPRO: P. J. Knowles and H.-J. Werner, Chem. Phys. Lett. **115**, 5053 (1985); H.-J. Werner and P. J. Knowles, J. Chem. Phys. **89**, 5803 (1988); P. J. Knowles and H.-J. Werner, Chem. Phys. Lett. **145**, 514 (1988); P. J. Knowles and H.-J. Werner, Theor. Chim. Acta **84**, 95 (1992).

[10] R. J. Gdanitz and R. Ahlrichs, Chem. Phys. Lett. **143**, 413 (1988).

[11] Atomic structure code MCHF: C. Froese Fischer, *The Hartree- Fock Method for Atoms—A Numerical Approach* (Wiley, New York, 1976).

[12] Atomic structure code GRASP: K. G. Dyall, I. P. Grant, C. T. Johnson, F. A. Parpia, and E. P. Plummer, Comput. Phys. Commun. **55**, 425 (1989).

[13] W. Liu, G. Hong, D. Dai, L. Li, and M. Dolg, Theor. Chem. Acc. **96**, 75 (1997).

[14] W. Liu, M. Dolg, and L. Li, J. Chem. Phys. **108**, 2886 (1998).

[15] J. P. Perdew and Y. Wang, Phys. Rev. B **45**, 13 244 (1992).

[16] H. Stoll, C. M. E. Pavlidou, and H. Preuss, Theor. Chim. Acta **49**, 143 (1978); H. Stoll, E. Golka, and H. Preuss, *ibid.* **55**, 29 (1980).

[17] A. D. Becke, Phys. Rev. A **38**, 3098 (1988).

[18] J. P. Perdew, K. Burke, and E. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1997).

[19] J. P. Perdew, Phys. Rev. B **33**, 8822 (1986); **34**, 7406(E) (1986).

[20] C. Lee, W. Yang, and R. G. Parr, Phys. Rev. B **37**, 785 (1988).

[21] A. H. MacDonald and S. H. Vosko, J. Phys. C **12**, 2977 (1979); A. H. MacDonald, *ibid.* **16**, 3869 (1983).

[22] M. Mayer, O. D. Häberlen, and N. Rösch, Phys. Rev. A **54**, 4775 (1996).

[23] T. Ziegler, A. Rauk, and E. J. Baerends, Theor. Chim. Acta **43**, 261 (1977).

[24] W. Yang, J. Chem. Phys. **94**, 1208 (1991).

[25] V. I. Lebedev, Zh. Vychisl. Mat. Mat. Fiz. **15**, 48 (1975); **16**, 293 (1976); V. I. Lebedev, Sib. Mat. Zh. **18**, 32 (1977).

[26] T. Ziegler and A. Rauk, Theor. Chim. Acta **46**, 1 (1977).

[27] J. Forstreuter, Ph.D. thesis, Technische Universität, Dresden, 1997 (unpublished).

[28] S. Kotochigova, Z. Levine, E. Shirley, M. Stiles, and C. Clark, website: http://math.nist.gov/DFTdata/

[29] E. Eliav, U. Kaldor, and Y. Ishikawa, Phys. Rev. A **51**, 225 (1995).

[30] B. Fricke, W. Greiner, and J. T. Waber, Theor. Chim. Acta **21**, 235 (1971).

[31] O. Gunnarsson and R. O. Jones, Phys. Rev. B **31**, 7588 (1985).

[32] A. Savin, Int. J. Quantum Chem., Symp. **22**, 59 (1988); B. Miehhlich, H. Stoll, A. Savin, Mol. Phys. **91**, 527 (1997).