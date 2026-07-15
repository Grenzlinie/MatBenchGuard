# Computational study of stacking faults in sapphire using total energy methods

M. H. Jhon,* A. M. Glaeser, and D. C. Chrzan†

Department of Materials Science and Engineering, University of California at Berkeley and Materials Sciences Division,
Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA

(Received 26 February 2005; published 8 June 2005)

The structures and energetics of stacking faults on the prism planes in sapphire are studied computationally using total energy methods. Both first principles methods and empirical potentials are used to study four competing stacking fault structures on $\{1\overline{1}00\}$ and one structure on $\{11\overline{2}0\}$. Estimates for the vibrational contribution to the fault energy are obtained using empirical shell-model potentials. The calculated stacking fault energies are combined with anisotropic elasticity theory to predict the structure of low-angle symmetric tilt boundaries.

DOI: 10.1103/PhysRevB.71.214101
PACS number(s): 61.72.Nn, 61.72.Mm, 68.35.Ct

## I. INTRODUCTION

Perfect dislocations in sapphire ($\alpha$-Al₂O₃) have relatively large Burgers vectors and have been observed to separate into partial dislocations connected by a stacking fault. Describing the nature of this dissociation reaction is important for the understanding of plasticity. Experimental observations have identified two important dislocation dissociations that appear during deformation. First, under deformation by basal slip (0001) $\langle11\overline{2}0\rangle$, the reaction

$$
\frac{1}{3}\langle11\overline{2}0\rangle \to \frac{1}{3}\langle10\overline{1}0\rangle + \text{stacking fault} + \frac{1}{3}\langle01\overline{1}0\rangle \tag{1}
$$

has been observed to occur due to dislocation climb.¹⁻³ A second dislocation reaction can be found during deformation by prismatic slip $\{11\overline{2}0\}\langle1\overline{1}00\rangle$ due to both glide⁴ and climb⁵ processes:

$$
\langle1\overline{1}00\rangle \to \frac{1}{3}\langle1\overline{1}00\rangle + \frac{1}{3}\langle1\overline{1}00\rangle + \frac{1}{3}\langle1\overline{1}00\rangle + \text{stacking fault}. \tag{2}
$$

The extended dislocations described by Eqs. (1) and (2) can also be formed during other processes, such as in spontaneous crack healing⁶ or grain boundary formation. Weak-beam transmission electron microscopy (WB-TEM) studies of polycrystalline Al₂O₃ have found that low-angle grain boundaries contain dissociated dislocations.⁷,⁸ Recent high-resolution electron microscopy (HREM) studies of near-$\{1\overline{1}00\}$ (Refs. 9 and 10) and near-$\{11\overline{2}0\}$ (Refs. 11–13) symmetric tilt boundaries have demonstrated that they are constructed of well-ordered arrays of extended dislocations. The equilibrium structure of these boundaries is clearly a function of the stacking fault energy (SFE). The observed dislocation structure of the near-$\{11\overline{2}0\}$ boundary is represented in Fig. 1.

The stacking faults created in these dissociation reactions have been observed to form primarily on the $\{11\overline{2}0\}$ and $\{1\overline{1}00\}$ prism planes. Although stacking faults on the basal plane have been proposed,¹⁴ both calculations from semiempirical shell model¹⁵ and first principles¹⁶ methods have suggested that these are high energy defects, with energies on the order of $3\ \text{J/m}^2$. The shell-model calculations have found the prism plane faults to be much lower in energy. However, experimental measurements of SFE on the prism planes obtained by analyzing isolated dislocation dipoles have yielded inconsistent results, varying by more than a factor of $2.^{2,3}$ These differences have been attributed to differences in material purity and temperature effects.²

The temperature dependence of SFEs in sapphire has not been studied in great detail. While metallic systems have been studied theoretically,¹⁷,¹⁸ there have been few such studies performed on ceramics. It has been suggested¹⁵ that the temperature dependence of the SFE in sapphire should be on the order of $1.1 \times 10^{-4}\ \text{J m}^{-2}\text{K}^{-1}$, by comparison to free energy minimization studies of NiO grain boundaries.¹⁹ It has been experimentally measured for faults on $\{11\overline{2}0\}$, that

![](./images/812275805139763201_1.jpg)

FIG. 1. Schematic array of near-$\{11\overline{2}0\}$ low-angle tilt boundary. Panel (a) corresponds to a perfect boundary, and panel (b) corresponds to the dissociated boundary. The dashed lines indicate the presence of a stacking fault.


the difference between SFE at 1450 and 1700 °C is negligible.⁵ Experiments have also been performed on electron-irradiated sapphire at 800 °C.²⁰ The measured SFE was much higher than previous studies, and was attributed to the lower processing temperature.

In the present study, density-functional theory (DFT) is used to compute SFEs for the stacking faults appearing in Eqs. (1) and (2). Shell-model calculations are used to help test convergence of the more expensive DFT calculations, and to study the temperature dependence of SFEs. Finally, the calculated SFE is discussed with respect to observed low-angle boundary configurations.

## II. STACKING FAULT STRUCTURE

Sapphire has the corundrum structure, in which the anions lie in a nearly hexagonal close packing. The anions are arranged in layers which have a stacking sequence …ABAB… along [0001]. The cations sit on 2/3 of the octahedral interstitial sites, forming layers with an …abcabc… stacking sequence. The nonprimitive hexagonal unit cell can be described by alternating anion and cation layers in the sequence AaBbAcBaAbBc. The fault vector $1/3\langle 1\overline{1}00\rangle$ is a perfect lattice translation in the anion sublattice but not in the cation sublattice. This fault will therefore only appear on the cation sublattice. In the basal plane, the cations have a $…\alpha\beta\gamma\alpha\beta\gamma…$ stacking sequence in the $\langle 1\overline{1}00\rangle$ directions. This allows both interstitial and vacancy faults to be present. In the $\langle 11\overline{2}0\rangle$ directions, there is a simpler …1212… stacking. It can be shown that on this plane, the interstitial and vacancy faults are identical.¹

Four structures of stacking faults on the $\{11\overline{2}0\}$ and $\{1\overline{1}00\}$ planes have been proposed previously³ˡ¹⁵ and are shown in Fig. 2. One structure (a) corresponds to the fault in the $(11\overline{2}0)$ plane, with a fault vector in the $[1\overline{1}00]$ direction. Three types of faults with fault vector $(1/3)\langle 10\overline{1}0\rangle$ have been proposed that lie on the $\{1\overline{1}00\}$ planes: (b) a vacancy fault, (c) an interstitial fault with $…\alpha\beta\gamma\alpha\alpha\beta\gamma…$ stacking, and (d) an interstitial fault with $…\alpha\beta\gamma\beta\alpha\beta\gamma…$ stacking. The present study also considers a third possible interstitial fault (e) which is generated by alternating $…\alpha\beta\gamma\alpha\alpha\beta\gamma…$ stacking with $…\alpha\beta\gamma\gamma\alpha\beta\gamma…$ stacking in the $\langle 11\overline{2}0\rangle$ direction. This structure has not been previously considered.

These five structures may be visualized by separately examining the cation layers in the basal plane. Because of the stacking of the cations in [0001], three cation layers are shown in Fig. 2. The relative energies of the stacking faults structure on the prism planes have been considered on the basis of electrostatics, which suggests that fault (d) would have a higher energy than (c) due to the configuration of holes.¹ Earlier shell-model calculations¹⁵ as well as the present study have confirmed this, finding that (d) is measurably higher energy independent of the potential used.

![](./images/812275805139763201_2.jpg)

FIG. 2. Schematic of studied stacking fault structures projected onto (0001), after Ref. 3. The cation sublattice is depicted for the five fault structures considered. Fault (a) is the structure of the fault on $(11\overline{2}0)$, and faults (b)–(e) represent possible structures of faults on $(1\overline{1}00)$. Filled circles represent octahedral sites occupied by Al ions, while empty circles represent empty sites. The three unique layers in [0001] are represented separately, labeled a, b, and c.

## III. METHOD OF COMPUTATION

The stacking faults are studied computationally using total energy methods, applying a supercell approximation. The studied configuration corresponds to an infinite one-dimensional array of faults separated from their neighbors by regions of perfect crystal. In order to ensure that the stacking faults are spaced sufficiently far apart such that they do not interact, a study using semiempirical shell-model potentials was undertaken. The General Utility Lattice Program (GULP) was used to perform the shell-model calculations.²¹ Two sets of potentials were used for the shell-model calculations, both utilizing the Buckingham potential.²²ˡ²³ The rationalized function optimization (RFO) algorithm was used to minimize the energy at constant volume, then at constant pressure. The SFE was first calculated as a function of supercell size. Using the potentials optimized by Minervini et al.,²³ the SFE of the smallest supercells were found to be within 5 mJ/m² of the fully converged SFE. We note that the Gale and Henson²² potential parameters found somewhat more interaction for faults (b) and (d). Even so, the minimal supercell found a SFE within 10 mJ/m² of the converged SFE. This suggests that the elastic interaction between the faults is very weak and therefore the minimal supercells were used for the DFT calculations. The smallest cell for fault (a) containing one fault corresponds to a 90 atom monoclinic supercell. For faults (b), (c), (d), and (e) orthorhombic supercells of 100, 80, 80, and 160 atoms were used.

<table>
<caption>Table I. Lattice parameters of sapphire, including the rhombohedral lattice constant $a$, angle between lattice vectors $\alpha$, and unit cell volume $V_0$.</caption>
<tbody>
<tr>
<td>
</td>
<th>
$a$
</th>
<th>
$\cos\alpha$
</th>
<th>
$V_0$
</th>
</tr>
<tr>
<td>
LDA
</td>
<td>
5.10Å
</td>
<td>
0.568
</td>
<td>
83.49 Å³
</td>
</tr>
<tr>
<td>
GGA
</td>
<td>
5.16
</td>
<td>
0.569
</td>
<td>
86.81
</td>
</tr>
<tr>
<td>
Literature$^{\mathrm{a}}$
</td>
<td>
5.13
</td>
<td>
0.569
</td>
<td>
84.89
</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$Reference 27.

Using these minimal unit cells, the fault structure at $T$ =0 was then examined using the density functional theory (DFT) based electronic structure total energy techniques embedded in the Vienna Ab-initio Simulation Package (VASP).$^{24,25}$ The SFE was calculated using both the generalized gradient approximation (GGA) and the local density approximation (LDA) to density functional theory using the projector augmented wave method (PAW). The energy cutoff was chosen to be 37 Ry. Structures were relaxed under constant pressure until the forces on the ions were less than 0.01 eV/Å. For fault (e), Brillouin-zone integrations employed a $2×2×2$ $k$-point mesh. For the other faults, a $3×3×3$ $k$-point mesh was used. This choice of parameters yielded a solution converged to within $10^{-5}$ eV per cell.

Limited computational resources prevented the calculation of phonon spectra using $ab$ $initio$ methods. As a result, in order to study the temperature dependence of the SFE, shell-model calculations were again used. The free energy was optimized within the quasiharmonic approximation$^{19}$ at 1800 K.

## IV. BULK PROPERTIES

In order to verify the applicability of the computational methods to sapphire, properties of the bulk material were calculated within the GGA and the LDA, including the lattice constants and the elastic constants. Lattice parameters for the rhombohedral unit cell are presented in Table I. The conventional choice for the relation between the coordinate axes and the crystallographic axes is taken.$^{26}$ The results of the present calculations are compared to recent literature values in Table II.

## V. RESULTS AND DISCUSSION

Table III displays the computed SFEs obtained using both $ab$ $initio$ and empirical potential techniques. The same energetic trends are obeyed by calculations using LDA and GGA.

These computational values may be compared to experimental observations of dipole dissociation in the literature.

For faults observed on $\{11\overline{2}0\}$, WB-TEM studies$^{3}$ have yielded stacking fault energies of 0.10–0.15 J/m² for deformation at 1450 °C. In Ref. 2, the dissociation energy was found to be 0.32 J/m² by measurement of dissociation widths with HREM. Studies with GaAs have found the difference in precision between these two techniques is small,$^{28}$ suggesting that different processing conditions may lead to a substantial difference in SFE. Over a similar range of processing temperatures, the faults on $\{1\overline{1}00\}$ were measured$^{3,29}$ to be 0.16–0.4 J/m². (A more complete review of experimentally measured SFE may be found in Ref. 3.) Thus the predictions of both DFT methods appear to be in reasonable agreement with the experimental values.

It is not possible to compare directly the energetic ordering of the calculated fault energies to experimental values. However, it has been observed$^{29}$ that faults on $\{11\overline{2}0\}$ can rotate to $\{1\overline{1}00\}$. This implies that faults on $\{11\overline{2}0\}$ are higher energy defects, in contrast to this study’s findings.

### A. Low-angle boundary structures

The calculated fault energies may be used to predict the structure of near-$\{11\overline{2}0\}$ low-angle tilt boundaries. Consider a symmetric boundary with misorientation $\theta$. Using anisotropic elasticity theory, it is possible to calculate the splitting of the extended dislocations. It is first necessary to neglect $c_{14}$, so the stress from an isolated $(1/3)[10\overline{1}0]$ dislocation can be represented analytically. This approximation is justified from the $ab$ $initio$ calculations. The $x$ axis is defined to be along $[11\overline{2}0]$ and the $z$ axis to be along [0001]. The origin is placed on the dislocation line. Following standard techniques,$^{30,31}$ it is possible to find the relevant components of the stress on the plane $x$=0,

$$
\sigma_{xx}=b_{x}\frac{c_{11}^{2}-c_{12}^{2}}{4c_{11}\pi y},\tag{3}
$$

$$
\sigma_{xy}=b_{y}\frac{c_{11}^{2}-c_{12}^{2}}{4c_{11}\pi y}.\tag{4}
$$

Here, $b_{x}$ and $b_{y}$ are the components of the Burgers vector. Using the Peach-Kohler equation, it is possible to find the interaction force between isolated $(1/3)[10\overline{1}0]$ and $(1/3)[01\overline{1}0]$ dislocations lying on the plane $x$=0 to be

<table>
<caption>Table II. Elastic constants of sapphire, measured in $10^{11}$ Pa.</caption>
<tbody>
<tr>
<td>
</td>
<th>
$c_{11}$
</th>
<th>
$c_{12}$
</th>
<th>
$c_{13}$
</th>
<th>
$c_{33}$
</th>
<th>
$c_{14}$
</th>
<th>
$c_{44}$
</th>
</tr>
<tr>
<td>
LDA
</td>
<td>
4.96
</td>
<td>
1.66
</td>
<td>
1.29
</td>
<td>
4.93
</td>
<td>
0.18
</td>
<td>
1.53
</td>
</tr>
<tr>
<td>
GGA
</td>
<td>
4.54
</td>
<td>
1.51
</td>
<td>
1.08
</td>
<td>
4.58
</td>
<td>
0.21
</td>
<td>
1.32
</td>
</tr>
<tr>
<td>
Literature$^{\mathrm{a}}$
</td>
<td>
4.975
</td>
<td>
1.627
</td>
<td>
1.155
</td>
<td>
5.033
</td>
<td>
0.225
</td>
<td>
1.474
</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$Reference 26.

![](./images/812275805139763201_3.jpg)

FIG. 3. Spacing of dislocations in near-{11$\overline{2}$0} low-angle symmetric tilt boundary as a function of stacking fault energy.

$$
f_{y}=\frac{b_{p}^{2}\left(c_{11}^{2}-c_{12}^{2}\right)}{8 \pi y c_{11}} \tag{5}
$$

$$
=\frac{b_{p}^{2} M}{y}, \tag{6}
$$

where $b_{p}$ is the length of the Burgers vector of the partial dislocation, $y$ is the spacing between the dislocations, and $M$ is a constant with units of pressure. Using Eq. (5), the force between two infinite arrays of dissimilar partials may be calculated by performing a summation. This force must be balanced with the SFE,

$$
\gamma_{\mathrm{sf}}=\frac{b_{p}(2 \theta) M}{\sqrt{3} \pi} \sum_{n=0}^{\infty}\left(\frac{1}{n+\alpha}-\frac{1}{n+1-\alpha}\right). \tag{7}
$$

The parameter $\alpha$ is taken to be the fraction of length of the boundary that is stacking fault, such that $d_{0}=\alpha d$, as shown in Fig. 1. By explicitly performing this summation, it is possible to invert this equation to find the equilibrium spacing:

$$
d_{0}=\alpha d=-\frac{d}{\pi} \operatorname{arccot}\left(\frac{\sqrt{3} \gamma_{\mathrm{sf}}}{b_{p} M(2 \theta)}\right) \tag{8}
$$

In the limit of isotropic elasticity theory, Ikuhara *et al.* found a similar expression$^{11}$ with $M=\mu / 4(1-\nu)$. Here, $\nu$ is the Poisson ratio and $\mu$ is the shear modulus. It is important that the analytic form of $\alpha$ implies that its range is restricted between 0 and $1 / 2$. This result differs from the results of the experimental studies, which have measured $\alpha>1 / 2$ at certain misorientations. $^{11}$ This result may be due to imprecision in the measuring technique or it may be due to nonequilibrium effects, such as dislocation climb upon cooling.

<table>
<caption>TABLE III. Computed stacking fault energies from shell-model and DFT in $\text{J}/\text{m}^{2}$.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">DFT</th>
<th colspan="2">Gale and Henson$^{\text{a}}$</th>
<th colspan="2">Minervini <i>et al.</i>$^{\text{b}}$</th>
</tr>
<tr>
<th>LDA</th>
<th>GGA</th>
<th>0 K</th>
<th>1800 K</th>
<th>0 K</th>
<th>1800 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fault (a)</td>
<td>0.42</td>
<td>0.35</td>
<td>0.65</td>
<td>0.52</td>
<td>0.69</td>
<td>0.58</td>
</tr>
<tr>
<td>Fault (b)</td>
<td>0.51</td>
<td>0.41</td>
<td>1.02</td>
<td>0.84</td>
<td>0.82</td>
<td>0.71</td>
</tr>
<tr>
<td>Fault (c)</td>
<td>0.56</td>
<td>0.46</td>
<td>0.76</td>
<td>0.63</td>
<td>0.89</td>
<td>0.76</td>
</tr>
<tr>
<td>Fault (d)</td>
<td>0.80</td>
<td>0.62</td>
<td>1.61</td>
<td>1.34</td>
<td>1.32</td>
<td>1.15</td>
</tr>
<tr>
<td>Fault (e)</td>
<td>0.61</td>
<td>0.50</td>
<td>1.18</td>
<td>0.59</td>
<td>0.85</td>
<td>0.72</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">$^{\text{a}}$Reference 22.</td>
</tr>
<tr>
<td colspan="7">$^{\text{b}}$Reference 23.</td>
</tr>
</tfoot>
</table>

<table>
<caption>TABLE IV. Calculated values of the ratio $R=\gamma_{\text{sf}}/M$.</caption>
<thead>
<tr>
<th></th>
<th>$R$</th>
</tr>
</thead>
<tbody>
<tr>
<td>LDA</td>
<td>48.0mm</td>
</tr>
<tr>
<td>GGA</td>
<td>43.6</td>
</tr>
<tr>
<td>Ikuhara <i>et al.</i>$^{\text{a}}$</td>
<td>40.8</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="2">$^{\text{a}}$Reference 11.</td>
</tr>
</tfoot>
</table>

The SFE calculated in previous sections may be used to compute the dislocation spacing in this limit. For these calculations, the elastic parameters $c_{11}$, and $c_{12}$ are taken from the bulk properties calculated previously. $b_{p}$ is taken to be 0.275 nm. As can be seen from Fig. 3, the spacing is not strongly dependent on the SFE. Since the LDA overestimates the elastic constants and the GGA underestimates them, the differences in the predicted spacing are minimized. The values of $M$ used to generate the plots are reported in Table IV and are compared to the value measured by Ikuhara *et al.* under isotropic elasticity theory. Both computational results are found to be fairly close to the experimental result.

### B. Stacking fault free energy

It has been suggested that the difference in measured SFE can be attributed to either temperature or impurity effects. $^{2}$ In this section, the effect of vibrational entropy on the measured stacking fault energy is considered using empirical potentials. The free energy minimization technique takes into account the effect of finite lattice expansion, but it ignores the anharmonic effects that tend to become more important at higher temperature. Typically, techniques such as molecular dynamics are necessary for treating temperatures greater than half of the melting temperature. Harding *et al.*$^{19}$ has suggested that in ionic materials the potentials are often deep enough that quasiharmonic free energy minimization techniques are applicable at higher homologous temperatures. In this spirit, this study has performed a free energy minimization calculation that estimates the vibrational contribution to SFE to be on the order of $-0.1 \text{ J}/\text{m}^{2}$ at 1800 K. This agrees with results of grain boundaries in NiO, as suggested earlier by Kenway. $^{19}$

However, it is important to note that the experimental measurement of the SFE also depends on the elastic constants. Experimentally, a softening of 20-30% has been observed for the elastic constants between room temperature and 2100 K.³² This is on the same order as the vibrational contribution to the SFE as calculated by empirical potentials. Since Eq. (8) finds that $\cot \pi\alpha \propto \gamma_{\text{sf}}/M$, our calculations predict that the observed spacing will be very weakly dependent on temperature.

This conclusion is consistent with the observations of Cadoz *et al*.⁵ It seems unlikely that the atypically high SFE in electron irradiated sapphire²⁰ can be attributed only to vibrational entropy. Other temperature-dependent effects may be responsible, for instance segregation of point defects to the fault. It has been suggested⁴ that differences in sample purity in nominally pure sapphire are responsible for variations in the measured SFE on the order of 20 mJ/m².

It is worth noting that up to now, only vibrational entropy has been considered. Structural entropy may also affect the energetics of the interstitial $\{1\overline{1}00\}$ fault, which has two structures that are nearly degenerate. At high temperature, it is possible that both phases will be present. However, a calculation of the equilibrium structure of this fault at nonzero temperature would be required and is beyond the scope of this study.

# VI. SUMMARY AND CONCLUSIONS

The SFE for faults on the $\{11\overline{2}0\}$ and $\{1\overline{1}00\}$ planes have been calculated through first principles calculations as well as empirical potentials. For faults on $\{11\overline{2}0\}$, the SFE was found to be 0.42 J/m² under the LDA and 0.35 J/m² under the GGA. This result was found to be consistent with the structure of near-$\{11\overline{2}0\}$ low-angle symmetric tilt boundaries. Four structures were considered for faults on $\{1\overline{1}00\}$. The contribution to the stacking fault energy from vibrational entropy is found to be small, on the order of 0.1 J/m². Vibrational entropy is expected to affect neither the stability of the lowest energy structure nor the measured dislocation spacing.

# ACKNOWLEDGMENTS

M.H.J. thanks the Department of Defense for funding through the NDSEG scholarship. D.C.C. acknowledges support from the Miller Institute for Basic Research in Science. This work was sponsored in part by the Director, Office of Science, Office of Basic Energy Science, Division of Materials Science and Engineering, of the U.S. Department of Energy under Contract No. DE-AC03-76SF00098. Computer resources provided in part by a grant from the National Energy Research Scientific Computing Center.

*Electronic address: mj2k@berkeley.edu
†Electronic address: dcchrzan@berkeley.edu
¹D. S. Phillips, T. E. Mitchell, and A. H. Heuer, Philos. Mag. A 45, 371 (1982).
²A. Nakamura, T. Yamamoto, and Y. Ikuhara, Acta Mater. 50, 101 (2002).
³K. P. D. Lagerlöf, T. E. Mitchell, A. H. Heuer, J. P. Rivière, J. Cadoz, J. Castaing, and D. Phillips, Acta Metall. 32, 97 (1984).
⁴J. B. Bilde-Sørensen, A. R. Thölen, D. J. Gooch, and G. W. Groves, Philos. Mag. 33, 877 (1976).
⁵D. S. Phillips and J. L. Cadoz, Philos. Mag. A 46, 583 (1982).
⁶B. J. Hockey, in *Fracture Mechanics of Ceramics*, edited by R. C. Bradt, A. G. Evans, D. P. H. Hasselman, and F. F. Lange (Plenum, 1989), Vol. 6, pp. 637–658.
⁷C. B. Carter, D. L. Kohlstedt, and S. L. Sass, J. Am. Ceram. Soc. 63, 623 (1980).
⁸Y. R. Shiue and D. S. Phillips, Philos. Mag. A 50, 677 (1984).
⁹Y. Ikuhara, T. Watanabe, T. Yamamoto, T. Saito, H. Yoshida, and T. Sakuma, MRS Symposia Proceedings No. 601 (Materials Research Society, Pittsburgh, 2001), p. 125.
¹⁰Y. Ikuhara, T. Watanabe, T. Yamamoto, T. Saito, H. Yoshida, and T. Sakuma, in *Proceedings of the 7th Japan-France Mat. Sci. Sem.* (2001).
¹¹Y. Ikuhara, H. Nishimura, A. Nakamura, K. Matsunaga, T. Yamamoto, and K. P. D. Lagerlöf, J. Am. Ceram. Soc. 86, 595 (2003).
¹²S. T. Taylor, Ph.D. thesis, University of California at Berkeley (2002).
¹³R. A. Marks, S. T. Taylor, E. Mammana, R. Gronsky, and A. M. Glaeser, Nat. Mater. 3, 682 (2004).
¹⁴M. L. Kronberg, Acta Metall. 5, 507 (1957).
¹⁵P. R. Kenway, Philos. Mag. B 68, 171 (1993).

¹⁶A. G. Marinopoulos and C. Elsasser, Philos. Mag. Lett. 81, 329 (2001).
¹⁷J. P. Hirth, Metall. Trans. 1, 2367 (1970).
¹⁸J. F. Wan, S. P. Chen, and Z. Y. Xu, Sci. China, Ser. E: Technol. Sci. 44, 345 (2001).
¹⁹J. H. Harding, S. C. Parker, and P. W. Tasker, in *Nonstoichiometric Compounds Surfaces, Grain Boundaries and Structural Defects*, edited by J. Nowotny and W. Weppner (1989), pp. 337–349.
²⁰D. G. Howitt and T. E. Mitchell, Philos. Mag. A 44, 229 (1981).
²¹J. D. Gale, J. Chem. Soc., Faraday Trans. 93, 629 (1997).
²²J. D. Gale and N. J. Henson, J. Chem. Soc., Faraday Trans. 90, 3175 (1994).
²³L. Minervini, M. O. Zacate, and R. W. Grimes, Solid State Ionics 116, 339 (1999).
²⁴G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).
²⁵G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).
²⁶J. R. Gladden, J. H. So, J. D. Maynard, P. W. Saxe, and Y. L. Page, Appl. Phys. Lett. 85, 392 (2004).
²⁷P. Villars and L. D. Calvert, *Pearson's Handbook of Crystallographic Data for Intermetallic Phases*, 2nd ed. (ASM International, 1991).
²⁸A. Christensen and E. A. Carter, Phys. Rev. B 62, 16968 (2000).
²⁹T. E. Mitchell, B. J. Pletka, D. S. Phillips, and A. H. Heuer, Philos. Mag. 33, 877 (1976).
³⁰J. P. Hirth and J. Lothe, *Theory of Dislocations* (Krieger, 1982).
³¹H. Kung, J. Hirth, S. R. Foltyn, P. N. Arendt, Q. X. Jia, and M. P. Maley, Philos. Mag. Lett. 81, 85 (2001).
³²E. S. Zouboulis and M. Grimsditch, J. Appl. Phys. 70, 772 (1991).