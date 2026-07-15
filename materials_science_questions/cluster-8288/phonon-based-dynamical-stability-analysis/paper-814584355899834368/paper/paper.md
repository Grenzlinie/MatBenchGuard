# Strong influence of off-site symmetry positions of hydrogen atoms in $\mathrm{ScH}_{3}$ hcp phases

T. Pakornchote $^{\mathrm{a},\mathrm{b}}$, T. Bovornratanaraks $^{\mathrm{a},\mathrm{b},*}$, S. Vannarat $^{\mathrm{c}}$, U. Pinsook $^{\mathrm{a},\mathrm{b}}$

$^{\mathrm{a}}$ Department of Physics, Faculty of Science, Chulalongkorn University, Bangkok, Thailand
$^{\mathrm{b}}$ ThEP, Commission on Higher Education, 328 Si-Ayutthaya Road, 10400 Bangkok, Thailand
$^{\mathrm{c}}$ Large-Scale Simulation Research Laboratory, Thailand National Electronics and Computer Technology Center, Pathumthani, Thailand

---

## ARTICLE INFO

**Article history:**
Received 29 July 2015
Accepted 23 October 2015
Available online 4 November 2015

**Keywords:**
A: Metal hydride
E: Density functional theory
C: Symmetry breaking
D: Hydrogen storage

---

## ABSTRACT

We investigate the wave-like arrangements of $\mathrm{H}$ atoms around metal plane $(\mathrm{H}_{\mathrm{m}})$ in the $\mathrm{ScH}_{3}$ hcp phase by using the *ab-initio* method. We found that only $P6_{3}/mmc$, $P\overline{3}c1$, $P6_{3}cm$ and $P6_{3}$ phases are energetically favorable. The wave-like arrangement allows the off-site symmetry positions of the $\mathrm{H}$ atoms, and leads to substantial changes in the pair distribution between $\mathrm{Sc}$ and $\mathrm{H}$ atoms which are associating with the changes in the electronic structure in such a way that the total energy is lowering. The symmetry breaking from $P6_{3}mmc$ is also responsible for the band gap opening. In the $P6_{3}$ structure, the calculated band gap is 0.823 eV and 1.223 eV using GGA and sX-LDA functionals, respectively. This band gap can be compared with 1.7 eV derived from the optical measurement and 1.55 eV from the HSE06 calculation. Thus, the broken symmetry structures can be viewed as Peierls distortion of the $P6_{3}/mmc$ structure. Furthermore, we found that only the $P6_{3}$ structure is dynamically stable, unlike $\mathrm{YH}_{3}$ where the $P6_{3}cm$ structure is also stable. The stability of $P6_{3}$ comes from sufficiently strong interactions between two neighboring $\mathrm{H}$ atoms at their off-site symmetry positions, i.e. near the metal plane and near the tetragonal site. The $P6_{3}$ phonon density of states is in good agreement with the data from the neutron experiment.

© 2015 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Rare-earth metal hydride $(\mathrm{REH}_{x})$ compounds have been found to be a switchable metal-insulator material under variation of the $\mathrm{H}$ content. The electronic property changes from a metal in dihydrides to an insulator in trihydrides, and the corresponding structure changes from the fcc to the hcp phase [1-3]. Under high pressure, the stoichiometry ratio of $\mathrm{REH}_{x}$ increases up to $x{=}3$, and the crystal structure transforms as the following typical sequences; $\mathrm{hcp}\rightarrow\mathrm{intermediate}\rightarrow\mathrm{fcc}\rightarrow\mathrm{hcp}\rightarrow Cmcm$ [4-16]. The second appearance of the hcp phase at higher pressure is different from the first appearance at lower pressure by the arrangement of $\mathrm{H}$ atoms.

There were several investigations on the arrangements of the $\mathrm{H}$ atoms in the $\mathrm{YH}_{3}$ hcp phase (the first appearance at lower pressure), and their influence on the electronic and dynamical properties [17-26]. The structure of the $\mathrm{YH}_{3}$ hcp phase was suggested to be similar to the $\mathrm{HoD}_{3}$ structure [27], which has six yttrium atoms in the unit cell, thus its Brillouin zone is one-third of the $P6_{3}/mmc$ hcp unit cell with $30^{\circ}$ (anti)clockwise rotation about the $c$-axis. The K point folds up three times into the $\varGamma$ point. Its $\mathrm{H}$ atoms can be categorized into two groups, i.e. the $\mathrm{H}$ atom near a tetrahedral site $(\mathrm{H}_{\mathrm{t}})$ and the $\mathrm{H}$ atom around a metal plane $(\mathrm{H}_{\mathrm{m}})$. The on-site symmetry position of the tetrahedral site is located at the center of a tetrahedron with one $\mathrm{Sc}$ atom at each corner. Thus $\mathrm{H}_{\mathrm{t}}$ is surrounded by four $\mathrm{Sc}$ atoms. On the other hand, the $\mathrm{H}_{\mathrm{m}}$ atom is surrounded by three $\mathrm{Sc}$ atoms. There are three possible positions for each $\mathrm{H}_{\mathrm{m}}$ atom, i.e. above, under or on the metal plane. The position on the metal plane is the on-site symmetry position, whereas the other two positions are the off-site symmetry positions. According to these different $\mathrm{H}$ atoms arrangements, the symmetry can vary from 24 operations in the $P6_{3}/mmc$ phase (where all the $\mathrm{H}_{\mathrm{m}}$ atoms are at their on-site symmetry positions) to, for example, 12 operations in the $P\overline{3}c1$ phase. Gelderen et al. proposed that the $P6_{3}cm$ and $P6_{3}$ phases are more energetically favorable and dynamically stable than the $P\overline{3}c1$ phase which has the phonon softening modes around the $\varGamma$ point [24,25]. Furthermore, the phonon DOS from the neutron powder diffraction (NPD) experiment [26] was in good agreement with the average phonon DOS of $P6_{3}$ and $P6_{3}cm$. They also suggested that $P\overline{3}c1$ could be the mean structure of the $\mathrm{YH}_{3}$ hcp phase.

For $\mathrm{ScH}_{3}$, the NPD experiment showed that the $\mathrm{Sc}$ atoms also form a hcp structure [28]. The $P6_{3}/mmc$ structure was used to fit the

---

*Corresponding author at: Department of Physics, Faculty of Science, Chulalongkorn University, Bangkok, Thailand.
E-mail address: thiti.b@chula.ac.th (T. Bovornratanaraks).

http://dx.doi.org/10.1016/j.ssc.2015.10.012
0038-1098/© 2015 Elsevier Ltd. All rights reserved.

![](./images/814584355899834368_1.jpg)

NPD data but the experimental evidence pointed out that the arrangement of the H atoms is more complicated. Antonov et al. found that the $H_m$ atoms must distribute around the metal planes, i.e. occupy some off-site symmetry positions. They also suggested that the structure of the $ScH_3$ hcp phase would be similar to that of $YH_3$. Moreover, the $ScH_3$ hcp phase found to be a semiconductor, the same as $YH_3$, with the band gap of approximately 1.7 eV at ambient pressure by extrapolating from the optical experiment data [29].

In this work, we examined all possible arrangements of the $H_m$ atoms in the $ScH_3$ hcp phase in a sufficiently large supercell with six Sc atoms, and their influence on the energy and dynamical properties. Our finding confirms that the broken symmetry structures cause the band gap opening, and result in the energy reduction. This can be viewed as Peierls distortion of $P6_3/mmc$. Furthermore, we investigated the dynamical stability of the hcp phase. We found that the strong interaction between off-site symmetry positions of $H_t$ and $H_m$ play a crucial role in the stability of the hcp phase.

This paper is organized as follows; the calculation method is explained in Section 2. The symmetry breaking structures are described in Section 3 as well as their energetical comparison. The relation between the structural and electronic properties is discussed in Section 4. Their dynamical stability are discussed and compared with the recent experimental data [28] in Section 5.

## 2. Method
We use CASTEP code based on the density functional theory (DFT) using the plane-wave method to study the properties of the $ScH_3$ hcp phases [30-33]. The Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional [34] is chosen to calculate the energy and the physical properties such as geometry and phonons. The ultrasoft pseudopotential based on Vanderbilt theory [35] is chosen for the Sc atom with $3d^1 3s^2 3p^6 2s^2$ electronic configuration. A sufficiently large supercell with six Sc atoms is chosen in order to accommodate most of the hcp phases found in $YH_3$. A larger supercell is beyond our scope. The lattice parameters and the atomic positions are relaxed to their optimum structure using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) method [36]. For the accuracy of the calculation, the convergence test is performed, so that the variation of energy is less than 1.6 meV. The optimum parameters are as follows; the energy cutoff ($E_c$) is 600 eV, and the spacing between k-mesh grid using Monkhorst-Pack scheme [37,38] is $\approx 0.02e^{-1}$. The supercell of 192 atoms (48 Sc atoms) is used for the phonon calculation with the finite displacement method [39]. We scope ourselves to the GGA regime. However, the bandgap accuracy can be improved by explicitly including the screened exchange (sX) interaction [40]. The sX gives partial correction to the electron self-energy, and hence improves the excited states. We apply sX-LDA, as implemented in CASTEP [41] with the norm-conserving pseudopotential [42], to the band gap calculation in limited cases. The improvement of the band gap result is shown in Section 4.

## 3. Broken symmetry structures
$ScH_3$ with the $HoD_3$ type structure is considered as a starting point. The Sc atoms arrange in the hcp lattice. However, the exact symmetry must be determined from the arrangement of the $H_m$ atoms. There are three possible sites for each $H_m$ atom, i.e. on, under and above the metal plane. As there are six $H_m$ atoms in this unit cell, there can be as many as 729 possible arrangements. These arrangements can be viewed as a wave-like array in [110] direction. By geometrical consideration and also the periodic boundary conditions, they can be reduced to only nine distinguishable arrangements. Then these nine structures are optimized at 0 GPa. We found that only 4 structures, i.e. $P6_3/mmc$, $P\overline{3}c1$, $P6_3cm$ and $P6_3$ as illustrated in Fig. 1, are energetically stable.

The circles in Fig. 1 represent the positions of the $H_m$ atoms on the (110) plane of the unit cell. The empty circles are the on-site symmetry positions, and the filled circles are the off-site symmetry positions. The exact coordinates in reduced units are also indicated. In Fig. 1, (a) is the $P6_3/mmc$ phase of which all the $H_m$ atoms are at the on-site symmetry positions, and (b)-(d) are the wave-like arrangement of $H_m$ and can be identified as $P\overline{3}c1$, $P6_3cm$ and $P6_3$ phases, respectively. Among these four structures, the $P$

<table><caption>Table 1 The atomic position of the $P\overline{3}c1$, $P6_3cm$ and $P6_3$ phases.</caption>
<thead>
<tr>
<th>atom</th>
<th>fractional coordinate</th>
<th>$P\overline{3}c1$</th>
<th>$P6_3cm$</th>
<th>$P6_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sc</td>
<td></td>
<td>6f</td>
<td>6c</td>
<td>6c</td>
</tr>
<tr>
<td></td>
<td>x</td>
<td>0.664</td>
<td>0.670</td>
<td>0.672</td>
</tr>
<tr>
<td></td>
<td>y</td>
<td></td>
<td></td>
<td>0.006</td>
</tr>
<tr>
<td></td>
<td>z</td>
<td></td>
<td>0.250</td>
<td>0.250</td>
</tr>
<tr>
<td>$H_t$</td>
<td></td>
<td>12g</td>
<td>6c</td>
<td>6c</td>
</tr>
<tr>
<td></td>
<td>x</td>
<td>0.351</td>
<td>0.303</td>
<td>0.374</td>
</tr>
<tr>
<td></td>
<td>y</td>
<td>0.028</td>
<td></td>
<td>0.030</td>
</tr>
<tr>
<td></td>
<td>z</td>
<td>0.091</td>
<td>0.091</td>
<td>0.089</td>
</tr>
<tr>
<td>$H_t$</td>
<td></td>
<td></td>
<td>6c</td>
<td>6c</td>
</tr>
<tr>
<td></td>
<td>x</td>
<td></td>
<td>−0.355</td>
<td>0.308</td>
</tr>
<tr>
<td></td>
<td>y</td>
<td></td>
<td></td>
<td>0.007</td>
</tr>
<tr>
<td></td>
<td>z</td>
<td></td>
<td>−0.091</td>
<td>0.410</td>
</tr>
<tr>
<td>$H_m$</td>
<td></td>
<td>2a</td>
<td>2a</td>
<td>2a</td>
</tr>
<tr>
<td></td>
<td>z</td>
<td></td>
<td>0.312</td>
<td>0.188</td>
</tr>
<tr>
<td>$H_m$</td>
<td></td>
<td>4d</td>
<td>4b</td>
<td>2b</td>
</tr>
<tr>
<td></td>
<td>z</td>
<td>0.193</td>
<td>0.210</td>
<td>0.263, −0.188</td>
</tr>
</tbody>
</table>

$6_3/mmc$ structure is the highest symmetry structure with 24 symmetry operations, whereas $P\overline{3}c1$, $P6_3cm$ and $P6_3$ have lower symmetry, i.e. 12, 12, and 6 symmetry operations, respectively. The $P\overline{3}c1$ structure breaks mirror symmetry of $P6_3/mmc$, the $P6_3cm$ structure breaks inversion symmetry, whereas $P6_3$ breaks mirror, inversion and glide symmetries. We shall call these lower symmetry structures as broken symmetry structures from now on. Their optimized lattice parameters are shown in Table 1. Despite of its highest symmetry, the $P6_3/mmc$ energy is more than 0.14 eV higher than those of the broken symmetry structures. For the broken symmetry structures, the energy of $P6_3cm$ is 0.95 meV lower than that of $P\overline{3}c1$. This difference is within our window of the convergence error of 1.6 meV. Thus, $P6_3cm$ and $P\overline{3}c1$ are considered to be equal in terms of energy, i.e. they have a chance to co-exist, similar to the $YH_3$ case. For simplicity, we choose $P\overline{3}c1$ for discussing the structural comparison. The lowest energy structure is the $P6_3$ phase, where the energy is 8.13 meV lower than the $P\overline{3}c1$ phase. At this stage, the $P6_3$ phase is the strongest candidate for the hcp phase of $ScH_3$. This conclusion has recently been proposed also by Ye et al. [16] using a structure searching method.

Next, the atomic distribution is considered in order to examine the nature of bondings. To set up a reference, we draw a graphical representation of an Sc atom surrounding by eleven nearest H atoms, composed of three $H_m$ atoms and eight $H_t$ atoms, as shown in Fig. 2(a). According to Table 2, upon the symmetry breaking process, the Sc and H atoms are significantly redistributed. The graphical representation in Fig. 2(a) helps us keep track of the equivalent H sites in the different structures. The nearest $Sc-H_m$ distance is 1.939 Å in $P6_3/mmc$, and split into 1.954 and 1.958 Å in $P\overline{3}c1$ and split into 1.953, 1.965 and 1.972 Å in $P6_3$, compared with the experimental data of 1.961 Å [28]. The tendency is that the $Sc-H_m$ distances are extended a little along the symmetry breaking process. Furthermore, the electronic population analysis also shows increasing overlap population of $Sc-H_m$ from 0.17 in $P6_3/mmc$, to 0.18–0.19 in $P\overline{3}c1$, and to 0.18–0.20 in $P6_3$.

In accordance with the $H_m$ arrangements, the $H_t$ atoms are found to displace from the ideal tetrahedral sites to the off-site symmetry positions as well. The $H_t$ atoms in $P6_3/mmc$ phase move to the off-site symmetry positions along the $c$-axis, as shown by the red arrow direction in Fig. 2(b), whereas in other phases they move to the off-site symmetry positions in a specific direction depended on the phase, as shown arbitrarily by the blue arrow direction in Fig. 2(b). The detail of the $H_t$ displacements varies from phase to phase. However, we focus only on the $Sc-H_t$ distances. The nearest $Sc-H_t$ distance is 2.088 Å in $P6_3/mmc$, and becomes 2.089 Å in $P\overline{3}c1$ and split into 2.082 and 2.086 Å in $P6_3$. This $Sc-H_t$ distance remains almost intact upon symmetry breaking. However, the most intriguing feature is the second nearest $Sc-H_t$ distance of the $P6_3/mmc$ structure. In $P6_3/mmc$, it is 2.165 Å, then split into 2.074, 2.137 and 2.293 Å in $P\overline{3}c1$, and split into 2.047, 2.055, 2.101, 2.145, 2.331 and 2.379 Å in $P6_3$. It is readily seen that the second shell of $Sc-H_t$ in $P6_3/mmc$ is greatly redistributed along the symmetry breaking process. The distribution of the $H_t$ atoms around the Sc atoms causes the variations of the overlap population of $Sc-H_t$ as well. The electronic population analysis shows that the overlap population of $Sc-H_t$ increases from 0.18 at the bond distance of 2.165 Å in $P6_3/mmc$ to 0.24 at the bond distance of 2.047 Å in $P6_3$. This quantity greatly affects the band structure as shall be discussed in Section 4. The experiment reported the $Sc-H_t$ distances at 2.069 and 2.185 Å [28].

![](./images/814584355899834368_2.jpg)

Fig. 2. (Color online) (a) Bonding between Sc (large circle) with eight $H_t$ and three $H_m$ neighbor atoms. (b) Four Sc atoms form a tetrahedron around a $H_t$ atom at the on-site (small solid circle) and the off-site positions (small dash circle). A red (blue) arrow points a direction of the off-site position in the vertical direction (an arbitrary direction). The distances are not to scale.

In addition, the distribution among H atoms is also very interesting. The $H_t-H_t$ distance is as close as 1.927 Å in $P6_3/mmc$. Upon symmetry breaking, it is extended significantly to 1.963 Å in $P\overline{3}c1$ and to 1.988 Å in $P6_3$. The experiment reported the $H_t-H_t$ distances at 1.983 Å [28]. Another special feature is the $H_t-H_m$ distance which is 2.165 Å in $P6_3/mmc$. Upon symmetry breaking, the distance of some $H_t-H_m$ pairs is shrinking a little to 2.143 Å in $P\overline{3}c1$, but shrinking significantly to 2.088 Å in $P6_3$. The experiment reported that the nearest $H_t-H_m$ distance is 2.09 Å [28]. We found that the H–H distribution plays an important role in the dynamical stability as shall be discussed in Section 5.

Segal et al. [43] discussed that smaller overlap population tends to be more of the ionic bonding. In ionic crystals, such as NaF and NaCl, the overlap population is about 0.18–0.20, the same order as in Sc–H, but the bulk modulus of $ScH_3$ is double [10]. In addition, Mullikan charge analysis shows that the Sc charge is around +0.95 whereas the H charge varies between −0.31 and −0.35. This indicates certain degree of ionic bondings in $ScH_3$ as well. Upon symmetry breaking, the charge of the off-site symmetry $H_m$ atom appears to be a little less negative, while the charge of its three surrounding Sc atoms appear to be a little less positive. For the off-site symmetry $H_t$ atom, the charge remains intact, but the overlap populations among the four surrounding Sc atoms are redistributed. The charge distribution will slightly affect the Madelung energy.

<table>
<caption>Table 2
The distance, d, and the overlap population of orbitals between various neighboring atoms.</caption>
<thead>
<tr>
<th>Neigh-
boring
type</th>
<th colspan="2">P6₃/mmc</th>
<th colspan="2">P$\overline{3}$c1</th>
<th colspan="2">P6₃cm</th>
<th colspan="2">P6₃</th>
</tr>
<tr>
<th></th>
<th>d (Å)</th>
<th>Overlap population</th>
<th>d (Å)</th>
<th>Overlap population</th>
<th>d (Å)</th>
<th>Overlap population</th>
<th>d (Å)</th>
<th>Overlap population</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sc–Hₘ</td>
<td>1.939</td>
<td>0.17</td>
<td>1.954</td>
<td>0.18</td>
<td>1.953</td>
<td>0.20</td>
<td>1.953</td>
<td>0.18</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>1.958</td>
<td>0.19</td>
<td>1.961</td>
<td>0.19</td>
<td>1.965</td>
<td>0.20</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>1.972</td>
<td>0.20</td>
</tr>
<tr>
<td>Sc–Hₜ</td>
<td>2.088</td>
<td>0.12</td>
<td>2.089</td>
<td>0.13</td>
<td>2.088</td>
<td>0.13</td>
<td>2.082</td>
<td>0.13</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2.090</td>
<td>0.13</td>
<td>2.086</td>
<td>0.13</td>
<td></td>
</tr>
<tr>
<td>2.165</td>
<td>0.18</td>
<td>2.293</td>
<td>0.13</td>
<td>2.216</td>
<td>0.16</td>
<td>2.047</td>
<td>0.24</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2.101</td>
<td>0.21</td>
</tr>
<tr>
<td></td>
<td></td>
<td>2.074</td>
<td>0.22</td>
<td>2.084</td>
<td>0.22</td>
<td>2.145</td>
<td>0.18</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2.379</td>
<td>0.11</td>
</tr>
<tr>
<td></td>
<td></td>
<td>2.137</td>
<td>0.20</td>
<td></td>
<td></td>
<td>0.22</td>
<td>2.331</td>
<td>0.11</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0.10</td>
<td>2.055</td>
<td>0.23</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2.341</td>
</tr>
<tr>
<td>Hₜ–Hₜ</td>
<td>1.927</td>
<td>–0.05</td>
<td>1.963</td>
<td>–0.05</td>
<td>1.967</td>
<td>–0.05</td>
<td>1.988</td>
<td>–0.05</td>
</tr>
<tr>
<td>Hₜ–Hₘ</td>
<td>2.165</td>
<td>–0.03</td>
<td>2.143</td>
<td>–0.04</td>
<td>2.144</td>
<td>–0.04</td>
<td>2.088</td>
<td>–0.04</td>
</tr>
<tr>
<td>Sc–Sc</td>
<td>3.358</td>
<td>0.09</td>
<td>3.334</td>
<td>0.11</td>
<td>3.318</td>
<td>0.11</td>
<td>3.320</td>
<td>0.11</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3.338</td>
<td>0.11</td>
<td></td>
<td>0.11</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3.413</td>
<td>0.11</td>
<td></td>
</tr>
</tbody>
</table>

## 4. Electronic properties

To analyze the effects of the H arrangements on the electronic properties, the band structures of $P6_3/mmc$ and $P\overline{3}c1$ are compared in Fig. 3(a), and of $P\overline{3}c1$ and $P6_3$ phases are compared in Fig. 3(b). In particular, we consider the band structure in a range of a few eV around the Fermi energy ($E_F$) only. In this range, the band structure of $P6_3cm$ is quite similar to that of $P\overline{3}c1$. The partial DOS is also evaluated, as shown in Fig. 4. The partial DOS and the characteristic of the band structure help us identify the nature of bands and bondings.

Let us start with the $P6_3/mmc$ structure which is the highest symmetry among the others. In order to make a compatible comparison, the $P6_3/mmc$ phase is calculated by using the HoD₃-type structure, and placing all the $H_m$ atoms on metal plane, i.e. at the on-site symmetry position. Thus, the Brillouin zone has the same size as the other broken symmetry structures. The partial DOS (Fig. 4(a)) shows that the valance band is dominated by the interactions between Sc and H. By adopting the notations of Wang and Chou [18], they indicated that $\Gamma_1^-$ (Sc-$d_{yz}$), $\Gamma_2^+$ (Sc-$d_{xz}$), $\Gamma_2^-$ (Hₜ-s), and $\Gamma_4^-$ (Hₘ-s and Hₜ-s) bands are close to $E_F$, as shown in Fig. 3(a).

Around $E_F$, the dispersions of $\Gamma_1^-$ and $\Gamma_2^+$ are degenerate. Along $\Gamma$-A and $K$-$\Gamma$-M directions, some parts of these two bands are below $E_F$, and forming electron pockets around the $\Gamma$ point. At the A point, they raise up to around 0.8 eV above $E_F$ and cross with the $\Gamma_2^-$ and $\Gamma_4^-$ bands. Most of the $\Gamma_2^-$ and $\Gamma_4^-$ bands are below $E_F$, except around the $\Gamma$ and A points in which the bands raise above $E_F$, and form hole pockets. The electron and hole pocket manifest themselves as a density peak in the DOS at $E_F$, as seen in Fig. 4(a). The $\Gamma_1^-$ and $\Gamma_2^+$ bands also cross with the $\Gamma_2^-$ and $\Gamma_4^-$ bands at some points along the $K$-$\Gamma$ and $\Gamma$-M directions. From the band structure, it seems that these four bands are only weakly interacting in $P6_3/mmc$, and it is obvious that there is no band gap in this structure. Thus, the $P6_3/mmc$ structure is a metal. This is in contrast with the optical band gap from the experiment [29] which indicates that ScH₃ is a semiconductor with an extrapolating band gap of 1.7 eV at ambient pressure.

For the $P\overline{3}c1$ and $P6_3cm$ phases, their band structures close to $E_F$ are very similar. However, we shall see later in Section 5 that their phonons are quite different. The band structure is also similar to that of the $P\overline{3}c1$ phase of YH₃ from a previous LDA study [20]. As discussed in the previous section, the wave-like arrangement allows the $H_m$ atoms to occupy the off-site symmetry positions and causes the corresponding rearrangement of the $H_t$ atoms. The $H_t$ atoms in the $P\overline{3}c1$ and $P6_3cm$ phases occupy the off-site symmetry positions as well. The $P\overline{3}c1$ structure breaks mirror symmetry of $P6_3/mmc$, whereas the $P6_3cm$ structure breaks inversion symmetry. Some of the Sc–Hₜ and Sc–Hₘ overlap populations are promoted, as seen in Table 1, so that their bondings in these broken symmetry structures are stronger than in $P6_3/mmc$. These are consistent with the strong interaction between $\Gamma_1^-$ and $\Gamma_4^-$, i.e. the strong interaction among Sc-$d_{yz}$, Hₘ-s and Hₜ-s. These states are mixed together and open a large gap of about 2.7 eV at the $\Gamma$ point (see Fig. 3(a)). The partial DOS show that the density peak of Sc, $H_t$ and $H_m$ just below $E_F$ in $P6_3/mmc$ (see Fig. 4(a)) moves to lower energy in $P\overline{3}c1$ and $P6_3cm$, as seen in Fig. 4(b) and (c), respectively. The total energy of $P\overline{3}c1$ and $P6_3cm$ are lowering. The electron and hole pockets are partly removed, i.e. the magnitude of the density peak at $E_F$ is smaller than that of $P6_3/mmc$. Another contribution of the electron and hole pocket comes from the $\Gamma_2^-$ and $\Gamma_2^+$ bands which are only weakly interacting in $P\overline{3}c1$ and $P6_3cm$, and open a much smaller gap of about 0.013 eV. This gap also defines the band gap of these phases. The dispersions of the $\Gamma_2^-$ and $\Gamma_2^+$ interacting bands form cone-like states, as seen in graphene, at approximately half way between $K$ and $\Gamma$, and between $\Gamma$ and $M$. However, these are removed in the sX-LDA calculation where the d band positions are even higher. We found that the sX-LDA band gaps are 0.158 eV and 0.234 eV in $P\overline{3}c1$ and $P6_3cm$, respectively.

For $P6_3$, the general features of the band structure around $E_F$ are similar to those of $P\overline{3}c1$ and $P6_3cm$, see the comparison in Fig. 3(b). However, as seen in Table 1, some Sc–Hₜ pairs are getting closer in $P6_3$ than in $P\overline{3}c1$ and $P6_3cm$. The arrangement of $H_m$ in $P6_3$ is now breaking the glide symmetry of $P\overline{3}c1$ and $P6_3cm$. Furthermore, the overlap population of some of Sc–Hₜ pairs are significantly increased relative to those of the higher symmetry structures. This is because the glide symmetry breaking promotes the strong interaction between the $\Gamma_2^-$ and $\Gamma_2^+$ bands. In the other words, Sc-$d_{xz}$ and Hₜ-s are now strongly interacting. Consequently, the $\Gamma_2^-$ and $\Gamma_2^+$ interacting bands open an energy gap of about 1.7 eV at the $\Gamma$ point. From Fig. 4(d), it can be readily seen that the hole pocket is now completely removed, and the electron pocket due to Sc and $H_t$ interaction moves into lower energy, compared with other phases in Fig. 4(a)–(c). Therefore, the $E_F$ and the valence band maximum of $P6_3$ are about 50 meV and 0.5 eV, respectively,

![](./images/814584355899834368_3.jpg)

Fig. 3. (Color online) Comparison of the band structures between (a) $P6_3/mmc$ (black lines) and $P\overline{3}c1$ (red dashed lines) phases and (b) $P\overline{3}c1$ and $P6_3$ (blue line) phases, and (c) $P6_3$ with GGA (blue lines) and with sX-LDA (dotted lines) functionals. The $E_F$ is specified by horizontal dashed lines, but for (c) the $E_F$ is set at 0 eV.

lower than those of $P\overline{3}c1$ and $P6_3cm$. This makes the $P6_3$ structure the lowest energy structure among the others. The band gap is now widened to 0.823 eV. The sX-LDA calculation gives the band gap of 1.223 eV. The most improvement from sX-LDA is the position of the d bands of Sc, as seen in Fig. 3(c). Kume et al. [29] measured the optical gap of $ScH_3$ under high pressure, and gave an extrapolation value of the band gap to be 1.7 eV at 0 GPa. A recent work on HSE06 calculation also gave the band gap of 1.55 eV [16].
The electronic stability due to the structural changes and their associated symmetry breaking can be viewed as Peierls distortion in three dimensions.

## 5. Dynamical properties

As we have seen from Sections 3 and 4, the $P6_3$ structure is the most energetically favorable, compared with the other three local

![](./images/814584355899834368_4.jpg)

Fig. 4. (Color online) Partial DOS of (a) $P6_3/mmc$ phase, (b) $P\overline{3}c1$ phase, (c) $P6_3cm$ phase and (d) $P6_3$ phase. The contribution from Sc, $H_t$ and $H_m$ atoms are presented by blue line, red line and green line, respectively. The grey area is from the $d$ orbital of the Sc atom. The solid line and dotted line are the $s$ orbital and the $p$ orbital, respectively.

minimum structures. We need to examine further into their dynamical properties. By using the finite displacement method with a supercell of 192 atoms (48 Sc atoms), we calculate the phonon dispersion (Fig. 5), and the phonon density of states of the $P6_3/mmc$ (Fig. 6), $P\overline{3}c1$ (Fig. 7(d)), $P6_3cm$ (Fig. 7(c)) and $P6_3$ (Fig. 7(a)) structures. The phonon density of states is compared with the inelastic neutron scattering (INS) experiment of $ScH_{2.9}$ at 10 K (Fig. 7(c)) by Antonov et al. [28].

From the calculated phonon dispersion in Fig. 5, the dispersion of the $P6_3/mmc$, $P\overline{3}c1$, and $P6_3cm$ structures exhibit some imaginary modes around the $\Gamma$ point. Thus, we conclude that only the $P6_3$ structure is dynamically stable. The other structures are unstable. This is in contrast with $YH_3$ where the $P6_3cm$ structure is also dynamically stable [24,25]. Our finding could rule out the co-exist phases and the average structure over the co-existing structures, unless the imaginary modes might be stabilized by anharmonic effects at finite temperature.

We examine the phonon density of states in more detail by evaluating the partial phonon DOS, labelled by blue (Sc), green ($H_m$) and red ($H_t$) lines in Figs. 6 and 7. It helps us identify which type of atoms play a major role in a given mode. The phonon DOS of the $P6_3/mmc$, $P\overline{3}c1$, $P6_3cm$ and $P6_3$ structures share some common features. They can be divided into six frequency regions:

(1) The Sc region where the vibrations of the Sc atoms dominate. The phonon frequencies of this region are between 0 and 42 meV in all phases. The partial DOS shows some coupling between Sc and H but the vibrations of H are very small in this region. The experimental data [28] shows the peaks between 0 and 45 meV as well, as shown in Fig. 7(b). Due to different responses to neutrons between Sc and H, this part of DOS can be easily assigned to the vibration of the Sc atoms.

![](./images/814584355899834368_5.jpg)

Fig. 5. (Color online) The phonon dispersion of acoustic modes and optical modes of Sc atoms are presented as follows: (a) $P6_3/mmc$, (b) $P\overline{3}c1$, (c) $P6_3cm$ and (d) $P6_3$.

![](./images/814584355899834368_6.jpg)

Fig. 6. (Color online) Partial phonon DOS of the $P6_3/mmc$ phase is presented. The solid lines are the contribution from the Sc atom (blue line), $H_t$ atom (red line) and $H_m$ atom (green line). The total phonon DOS are presented by dashed lines. Vertical arrows denote $c$-polarization, horizontal arrows denote $ab$-polarization and crossed lines denote $abc$-polarization. The polarizations are taken from the modes at $\Gamma$ point only.

(2) The $ab$-$H_t$ region where the vibrations with the $ab$-polarization of the $H_t$ atoms dominate. From geometry, the $H_t$ atom is surrounding by four nearest Sc atoms which form a tetrahedron cage. The on-site symmetry $H_t$ atom is located at the center of the tetrahedron. In $P6_3/mmc$, $H_t$ occupies a slightly off-site symmetry position, as shown in Fig. 2(b). The force constants on $H_t$ are moderate, and the frequencies of the $ab$-polarization are between 75 and 125 meV in $P6_3/mmc$. The phonon DOS has very high density around 115 meV. In the broken symmetry structure, $H_t$ occupies another off-site symmetry position, which displaces further from the center of the tetrahedron. This displacement is depending on the structure. The corresponding vibration modes become more complex. Some of the $H_t$ modes are coupled to the $H_m$ modes, and the frequencies shift to lower frequencies in $P\overline{3}c1$, $P6_3cm$ and $P6_3$. Some modes become complicated vibrations with $abc$-polarizations, and the frequencies shift to higher frequencies. The ab-$H_t$ region is confined in the range between 40 and 110 meV. It seems that the high density peak around 115 meV in $P6_3/mmc$ dissociates itself into these two groups, i.e. the $H_t$-$H_m$ coupling (lower frequencies) and the $abc$-polarization (higher frequencies) regions, in the broken symmetry structures.

![](./images/814584355899834368_7.jpg)

Fig. 7. (Color online) Partial phonon DOS of (a) $P6_3$ phase, (b) the dynamical structure factor $S(Q,\omega)$ from INS experiment, (c) $P6_3cm$ phase and (d) $P\overline{3}c1$ phase. The meanings of lines and the arrows are the same as in Fig. 6.

(3) The $c$-$H_t$ region where the vibrations with the $c$-polarization of the $H_t$ atoms dominate. The $c$-polarization of the $H_t$ modes in the tetrahedron cage show strong interaction, and the frequencies are between 125 and 165 meV in $P6_3/mmc$. Under symmetry breaking process, the $H_t$ atoms experience even stronger interaction, and the

frequencies shift to the range between 140 and 170 meV in the broken symmetry structures.

(4) The $ab$-$\text{H}_\text{m}$ region where the vibrations with the $ab$-polarization of the $\text{H}_\text{m}$ atoms dominate. From geometry, the $\text{H}_\text{m}$ atom is surrounding by three nearest Sc atoms which form an equilateral triangle. The on-site symmetry $\text{H}_\text{m}$ atom is located on the plane at the center of the triangle. The interaction on $\text{H}_\text{m}$ on the plane is very strong and hence the frequencies of the $ab$-polarization are highest, i.e. between 175 and 190 meV in $P6_3/mmc$. The off-site symmetry is located above/below this plane. The force constants are weakening a little, and hence the frequencies of the $ab$-polarization are a little softening to between 170 and 185 meV in $P\overline{3}c1$, $P6_3cm$ and $P6_3$.

(5) The $c$-$\text{H}_\text{m}$ region where the vibrations with the $c$-polarization of the $\text{H}_\text{m}$ atoms dominate. From Section 3, the $c$-axis displacements of the $\text{H}_\text{m}$ atoms along the [110] direction, and all equivalent $\Gamma$-$M$ directions, are corresponding to the structural changes. We found also that some of the $c$-polarization of the $\text{H}_\text{m}$ modes in $P6_3/mmc$ are unstable in $\Gamma$-$K$ and $\Gamma$-$M$ directions, see Fig. 5(a). This is because the interaction between Sc and $\text{H}_\text{m}$ is very weak along the $c$-axis. Furthermore, the displacement of $\text{H}_\text{m}$ along the $c$-axis would lead to a lower energy structure. Thus some components of the force constants may not be well-defined. The phonon DOS is very low in this region between 50 and 70 meV in $P6_3/mmc$. There are some couplings to $\text{H}_\text{t}$ as well but the density is very low. The unstable modes can be stabilized by the stronger couplings among Sc, $\text{H}_\text{m}$ and $\text{H}_\text{t}$, as seen in the $P\overline{3}c1$, $P6_3cm$ and $P6_3$ structures. The magnitude of the phonon DOS increases. However, it is only $P6_3$ that is fully stabilized.

(6) The $\text{H}_\text{m}$-$\text{H}_\text{t}$ region where the coupling vibrations of the Sc, $\text{H}_\text{m}$ and $\text{H}_\text{t}$ atoms dominate. The $\text{H}_\text{m}$-$\text{H}_\text{t}$ region is very narrow in $P6_3/mmc$, i.e. between 50 and 70 meV. However, during the symmetry breaking process, some of the $\text{H}_\text{m}$-$\text{H}_\text{t}$ pairs are getting closer and exhibit stronger interaction, as discussed in Section 3. Thus the $\text{H}_\text{m}$-$\text{H}_\text{t}$ region shifts to higher frequencies and expands to a wider range between 40 and 110 meV in $P\overline{3}c1$, 50 and 105 meV in $P6_3cm$, and 50 and 110 meV in $P6_3$. In $P6_3$, there are five main peaks at 59, 69, 84, 96, 102 meV, compared with the experimental main peaks at 52, 62, 71, 81, 98 and 107 meV, respectively [28]. The coupled vibrations in $\text{ScH}_3$ are very crucial to the stability of the hcp phase, and the interactions are just sufficient enough to stabilize $P6_3$ only. Unlike $\text{YH}_3$, where several phases are dynamically stable, thus the stable phase in $\text{YH}_3$ can come from a mixture of the co-exist phases. This mixture will not happen in $\text{ScH}_3$ as the other hcp phases are dynamically unstable and will be quickly transformed into $P6_3$.

As discussed above, the calculated peak positions of $P6_3$ phase are generally in good agreement and most comparable with the experimental data [28]. Nevertheless, there is a possibility that the unusually large vibrations of the H atoms at finite temperature and the contribution of anharmonicity need to be taken into account in order to provide more accurate frequencies. Furthermore, the experiment reported with the stoichiometry ratio of $x=2.9(0)$ for $\text{ScH}_x$. The H defects would also lead to some changes in the normal modes of the system as well. However, these are beyond the scope of the present work.

## 6. Conclusion

We have used the DFT calculation to study the wave-like arrangements of the H atoms around the metal plane ($\text{H}_\text{m}$) in the $\text{ScH}_3$. We found that only the $P6_3/mmc$, $P\overline{3}c1$, $P6_3cm$ and $P6_3$ phases are energetically favorable, but only $P6_3$ is dynamically stable. The wave-like arrangement allows the off-site symmetry positions of the H atoms, and leads to substantial changes in the pair distribution between Sc and $\text{H}_\text{m}$, and Sc and $\text{H}_\text{t}$, which we have investigated in more detail. There are symmetry breakings along the process. Consequently, the corresponding electronic structure changes in such a way that the total energy is lowering. The symmetry breaking is also responsible for the band gap opening. This mechanism can be viewed as Peierls distortion in 3D. In the $P6_3$ structure, the calculated bandgap is 0.823 eV and 1.223 eV using GGA and sX-LDA functionals, respectively. This band gap can be compared with 1.7 eV derived from the optical measurement and 1.55 eV from the HSE06 calculation [16]. We examined further into the dynamical stability. We found that the stability of $P6_3$ comes from sufficiently strong interactions between two neighboring $\text{H}_\text{t}$ and $\text{H}_\text{m}$ atoms. In $P\overline{3}c1$ and $P6_3cm$, these couplings between $\text{H}_\text{t}$ and $\text{H}_\text{m}$ are also strong, but not enough to stabilize the phase. This should rule out the co-exist phases or the average structure over the other hcp phases in $\text{ScH}_3$. The calculated phonon density of states of $P6_3$ is in good agreement with the data from the neutron experiment [28]. Some correction could be added due to the large dynamics of H at finite temperature as seen in the Debye-Waller factor in the experiment.

## Acknowledgements

We are very grateful to acknowledge K. Kotmool for very useful information and discussion. This project has been partially supported by National Research Council of Thailand (NRCT) and National Research University Project, Office of Higher Education Commission (WCU-58-013-FW). T.B. acknowledges Thailand Research Fund (TRF) Contract number RSA5580014. Computing facilities have been partially provided by the Ratchadaphiseksomphot Endowment Fund of Chulalongkorn University (RES560530180-AM) and the Special Task Force for Activating Research (STAR) through the Energy Materials Physics Research Group.

## References

[1] J.N. Huiberts, R. Griessen, J.H Rector, R.J Wijngaarden, J.P Dekker, D.G. de Groot, N.J Koeman, Nature 380 (1996) 231-234.

[2] J.N. Huiberts, J.H. Rector, R.J. Wijngaarden, S. Jetten, D.G. de Groot, B. Dam, N.J Koeman, R. Griessen, B. Bjorvarsson, S. Olafsson, Y.S. Cho, J. Alloys Compd. 239 (1996) 158-171.

[3] R. Griessen, J.N. Huiberts, M. Kremers, A.T.M. van Gogh, N.J. Koeman, J.P. Dekker, P.H.L. Notten, J Alloys Compd. 253-254 (1997) 44-50.

[4] T. Palasyuk, M. Tkacz, Solid State Commun. 130 (2004) 219-221.

[5] T. Palasyuk, M. Tkacz, Solid State Commun. 133 (2005) 477-480.

[6] T. Palasyuk, M. Tkacz, Solid State Commun. 133 (2005) 481-486.

[7] T. Palasyuk, M. Tkacz, Solid State Commun. 141 (2007) 302-305.

[8] T. Palasyuk, M. Tkacz, Solid State Commun. 141 (2007) 354-358.

[9] A. Machida, A. Ohmura, T. Watanuki, T. Ikeda, K. Aoki, S. Nakano, K. Takemura, Solid State Commun. 138 (2006) 436-440.

[10] A. Ohmura, A. Machida, T. Watanuki, K. Aoki, S. Nakano, K. Takemura, J. Alloys Compd. 446 (2007) 598.

[11] Y. Yao, D.D. Klug, Phys. Rev. B 81 (2010) 140104.

[12] Y. Li, Y. Ma, Solid State Commun. 151 (2011) 388-391.

[13] B. Kong, L. Zhang, X.R. Chen, T.X. Zeng, L.C. Cai, Physica B 407 (2012) 2050-2057.

[14] B. Kong, Z.W. Zhou, D.L. Chen, R.F. Ling-Hu, Chin. Phys. B 5 (2013) 057102.

[15] T. Pakornchote, U. Pinsook, T. Bovornratanaraks, J. Phys. Condens. Matter 26 (2014) 025405.

[16] X. Ye, R. Hoffmann, N.W. Ashcroft, J. Phys. Chem. C 119 (2015) 5614-5625.

[17] T.J. Udovic, Q. Huang, J.J. Rush, J. Phys. Chem. Solids 57 (1995) 423-435.

[18] Y. Wang, M.Y. Chou, Phys. Rev. B 51 (1995) 7500.

[19] R. Eder, H.F. Pen, G.A. Sawatzky, Phys. Rev. B 56 (1997) 10115.

[20] P.J. Kelly, J.P. Dekker, R. Stumpf, Phys. Rev. Lett. 78 (1997) 1315.

[21] K.K. Ng, F.C. Zhang, V.I. Anisimov, T.M. Rice, Phys. Rev. B 59 (1999) 5398.

[22] P. van Gelderen, P.A. Bobbert, P.J. Kelly, G. Brocks, Phys. Rev. Lett. 85 (2000) 2989.

[23] P. van Gelderen, P.A. Bobbert, P.J. Kelly, G. Brocks, R. Tolboom, Phys. Rev. B 66 (2002) 075104.

[24] P. van Gelderen, P.J. Kelly, G. Brocks, Phys. Rev. B 63 (2001) 100301.

[25] P. van Gelderen, P.J. Kelly, G. Brocks, Phys. Rev. B 68 (2003) 094302.

[26] V.K. Fedotov, V.E. Antonov, I.O. Bashkin, T. Hansen, I. Natkaniec, J. Phys. Condens. Matter 18 (2006) 1593-1599.

[27] T.J. Udovic, Q. Huang, J.J. Rush, in: N.N. Nickel, W.B. Jackson, R.C. Bowman, R.G. Leisure (Eds.), Hydrogen in Semiconductors and Metals, Symposia Proceedings No. 513, MRS, Pittsburgh, 1998, 1999, p. 197.

[28] V.E. Antonov, I.O. Bashkin, V.K. Fedotov, S.S. Khasanov, A.I. Kolesnikov, T. Hansen, A.S. Ivanov, I. Natkaniec, Phys. Rev. B 73 (2006) 054107.

[29] T. Kume, H. Ohura, T. Takeichi, A. Ohmura, A. Machida, T. Watanuki, K. Aoki, S. Sasaki, H. Shimizu, K. Takemura, Phys. Rev. B 84 (2011) 064132.

[30] S.J. Clark, M.D. Segall, C.J. Pickard, P.J. Hasnip, M.I.J. Probert, K. Refson, M.C. Payne, Z. Kristall. 220 (2005) 567-570.

[31] P. Hohenberg, W. Kohn, Phys. Rev. 136 (1964) B864.

[32] W. Kohn, L.J. Sham, Phys. Rev. 140 (1965) A1133.

[33] M.C. Payne, M.P. Teter, D.C. Allan, T.A. Arias, J.D. Joannopoulos, Rev. Mod. Phys. 64 (1992) 1045-1097.

[34] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[35] D. Vanderbilt, Phys. Rev. B 41 (1990) 7892-7895.

[36] B.G. Pfrommer, M. Cote, S.G. Louie, M.L. Cohen, J. Comput. Phys. 131 (1997) 233-240.

[37] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188-5192.

[38] J.D. Pack, H.J. Monkhorst, Phys. Rev. B 16 (1977) 1748-1749.

[39] W. Frank, C. Elsässer, M. Fähnle, Phys. Rev. Lett. 74 (1995) 1791-1794.

[40] A. Seidl, A. Görling, P. Vogl, J.A. Majewski, M. Levy, Phys. Rev. B 53 (1996) 3764-3774.

[41] S.J. Clark, J. Robertson, Phys. Rev. B 82 (2010) 085208.

[42] D.R. Hamann, M. Schlüter, C. Chiang, Phys. Rev. Lett 43 (1979) 1494-1497.

[43] M.D. Segall, R. Shah, C.J. Pickard, M.C. Payne, Phys. Rev. B 54 (1996) 16317-16320.