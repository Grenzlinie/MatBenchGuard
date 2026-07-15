PHYSICAL REVIEW B 82, 155103 (2010)

# First-principles calculation of the structure and dielectric properties of $\text{Bi}_2\text{Ti}_2\text{O}_7$

Charles H. Patterson
School of Physics, Trinity College Dublin, Dublin 2, Ireland
(Received 2 July 2010; published 4 October 2010)

The structure, vibrational modes, and phonon contribution to the dielectric function of the pyrochlore $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ were calculated using first-principles methods. Total-energy minimization calculations were performed for $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ in a unit cell containing 88 ions, which had the ideal, cubic pyrochlore structure as the initial configuration. No symmetry constraints were imposed during this relaxation. Subsequent symmetry analysis of the relaxed structure found $Pna2_1$ space-group symmetry in a 44 ion unit cell. This structure contains Bi ions with two types of eightfold coordination by O and $O'$ ions. Vibrational modes and the dielectric function were calculated for the $Fd\overline{3}m$, $Pna2_1$, and $P_1$ structures. The crystal structure obtained by total-energy minimization is compared to structural data from reverse Monte Carlo analysis of neutron total scattering data. The imaginary part of the dielectric function derived from vibrational mode calculations is compared to dielectric function data for several related pyrochlores. Phonons which make the largest contributions to the dielectric constant are identified and analyzed.

DOI: 10.1103/PhysRevB.82.155103
PACS number(s): 61.50.Ah, 63.20.dk, 63.50.Lm

## I. INTRODUCTION

The structure of the insulating pyrochlore $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ (BTi) has been studied by x-ray and neutron-scattering $^{1-3}$ and density-functional theory (DFT) methods. $^{4-7}$ The ideal pyrochlore structure belongs to the $Fd\overline{3}m$ space group and consists of interpenetrating $\text{Bi}_2\text{O}'$ and $\text{Ti}_2\text{O}_6$ polyhedral networks. Both experimental and theoretical studies of $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ (Refs. 2, 4, and 5) and other bismuth pyrochlores $^{5,8-14}$ indicate that the $\text{Bi}_2\text{O}'$ network is distorted compared to the network in the ideal pyrochlore structure. Similarities between the structure of the $\text{Bi}_2\text{O}'$ network in $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ and the $\text{SiO}_2$ network in $\beta$ cristobalite have been highlighted. $^{3}$ The $\text{OSiO}$ bond angle in $\beta$ cristobalite is around $145^\circ$. Displacements of the Bi ion from the $O'O'$ axis in $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ have been inferred from powder neutron-diffraction studies, $^{2}$ where it was shown that marked improvements in fits to data were obtained by allowing Bi ions to shift from the ideal pyrochlore positions by $0.43$ Å. Bi displacements in $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ were also obtained from a reverse Monte Carlo (RMC) analysis of neutron total scattering data by Shoemaker $et$ $al.^{3}$ The distribution of Bi displacements is peaked around $0.4$ Å, which corresponds to a $\text{O'BiO'}$ bond angle around $160^\circ$. The cause of the displacement of the O ions from the $\text{SiSi}$ axis in $\beta$ cristobalite is clearly the stereochemical arrangement of two $\text{SiO}$ bonds and two off-center O lone pairs. The cause of the Bi displacement in $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ has been discussed in terms of off-centering of the Bi $6s$ lone pair $^{4,5,7}$ or a soft polar phonon mode $^{6}$ but the cause of displacement is not as clear as in $\text{SiO}_2$. The ratio of ionic radii in $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$, $r_A/r_B=1.93$, $^{2}$ lies outside the usual stability range for pyrochlores ($1.46$-$1.78$) at atmospheric pressure $^{15}$ and so some lattice instability might be expected.

The average structure for $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$, however, is cubic with $Fd\overline{3}m$ symmetry. The only indication from Bragg reflections that some symmetry breaking exists is the observation of the (442) reflection, $^{2}$ which is forbidden in the ideal cubic pyrochlore structure. The relationship between the symmetry-lowered structure at short range and average cubic symmetry at long range is not addressed here. This problem has been considered in $\beta$ cristobalite in terms of rigid unit modes of $\text{SiO}_4$ tetrahedra and domain models. $^{16}$

Insulating bismuth pyrochlores such as $\text{Bi}_{1.5}\text{Zn}_{0.92}\text{Nb}_{1.5}\text{O}_{6.92}$ (BZN), $\text{Bi}_{3/2}\text{ZnTa}_{3/2}\text{O}_6\text{O}'$ (BZT) or $\text{Bi}_{3/2}\text{MgNb}_{3/2}\text{O}_6\text{O}'$ (BMN) have been found to have large, dielectric constants, $^{17,18}$ which make them interesting candidates for device applications which require high-$k$ dielectrics. A correlation between Bi displacement and magnitude of the dielectric constant has been postulated in these pyrochlores. $^{12}$ Calculation of dielectric functions and analysis of modes and sources of polarization is probably the best way to understand the peculiar dielectric properties of such materials. As part of this work an attempt was made to obtain the dielectric function of $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ using reflectance measurement techniques previously used for related bismuth pyrochlores. $^{18}$ However, $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ transforms to $\text{Bi}_2\text{Ti}_4\text{O}_{11}$ and $\text{Bi}_4\text{Ti}_3\text{O}_{12}$ at $650^\circ$ C (Ref. 2) and several attempts to synthesize a dense sintered sample for IR reflectivity measurements have proven unsuccessful. $^{19}$

In the following sections of the paper we report DFT calculations of the crystal structure of $\text{Bi}_2\text{Ti}_2\text{O}_6\text{O}'$ in which $Fd\overline{3}m$, $P_1$, and $Pna2_1$ space-group symmetry constraints were applied to atomic positions. Calculations were performed using a conjugate gradient energy minimization technique in the CRYSTAL code. $^{20}$ The electronic density of states and charge density for a group of bands corresponding to the Bi $6s$ lone pair are analyzed and compared to results of previous calculations. Vibrational mode frequencies and phonon oscillator strengths for the three crystal structures were calculated using the methods described in Refs. 21 and 22 and are summarized below. Vibrational modes and Born effective charge tensors are used to analyze the sources of electric polarization in polar vibrational modes and dielectric function spectra are compared to those for BZN, BZT, and BMN.

1098-0121/2010/82(15)/155103(10)
155103-1
©2010 The American Physical Society

![](./images/811715887093514241_1.jpg)

FIG. 1. (Color online) Ti and O′ polyhedra in the ideal $Fd\overline{3}m$ pyrochlore structure viewed along the [101] direction. Ti ions are shown as small blue spheres, Bi ions as medium sized green spheres, O ions as large red spheres and O′ ions as large brown spheres. (a) $TiO_{6}$ octahedra. (b) O′Bi₄ tetrahedra. All Bi, Ti, O, and O′ ions are equivalent by symmetry in the ideal structure.

## II. RESULTS AND DISCUSSION

### A. Crystal structure

In this section we report results of conjugate gradient energy minimization calculations on $Bi_{2}Ti_{2}O_{6}O'$. The Perdew-Wang²³ generalized gradient approximation (GGA) to DFT was used throughout, except where B3LYP (Ref. 24) hybrid density functional calculations were performed for the $Fd\overline{3}m$ structure. Further details of the calculations are given in the Appendix.

The second origin choice for the $Fd\overline{3}m$ unit cell was used. Bi ions are located at the (0.5, 0.5, 0.5) site, Ti ions at the origin, O ions at (0.375, 0.375, 0.375), and the O′ ion at (x, 0.125, 0.125). The energy minimized value of x is 0.325019. The lattice parameter for the energy minimized $Fd\overline{3}m$ unit cell was 10.376 Å. This value may be compared to the value from x-ray diffraction, 10.379 Å.² In the ideal pyrochlore structure (Fig. 1 and Table I), each Bi ion has two O′ nearest neighbors at 2.25 Å and six O neighbors at 2.58 Å. The Bi ion sits at the center of a puckered ring containing the O ions and the O′ ions cap the Bi ions above and below the ring. Bi ions have approximately cubic coordination polyhedra containing six O and two O′ ions in the energy minimized $P_{1}$ and $Pna2_{1}$ structures.

The $P_{1}$ structure was generated by relaxing positions of all 88 ions in the $Fd\overline{3}m$ conventional unit cell. It was analyzed using the ISOTROPY program²⁵ and found to have approximately $Pna2_{1}$ symmetry and a primitive unit cell containing 44 ions. A further energy minimization calculation was performed using these coordinates as the initial configuration in a 44 ion unit cell with $Pna2_{1}$ symmetry constraints. The $Fd\overline{3}m$ lattice parameter (10.376 Å) was used for the $P_{1}$ cell and a lattice parameter of 10.371 Å was used for the $Pna2_{1}$ cell. The $Pna2_{1}$ space group belongs to the series of maximal isomorphic subgroups of $Fd\overline{3}m$. The relationship between the 88 ion conventional cell of the $Fd\overline{3}m$ structure and the 44 ion primitive cell of the $Pna2_{1}$ structure is illustrated in Fig. 2, which shows both cells along the [010] direction.

The coordination polyhedra and bond lengths of the $Fd\overline{3}m$ and $Pna2_{1}$ structures in Figs. 1 and 3 and Table I show the changes which result from structure relaxation. There is one type of Bi and one type of Ti in the $Fd\overline{3}m$ structure and there are two Bi and two Ti types in the $P_{1}$ and $Pna2_{1}$ structures. Obviously the absence of symmetry constraints on the 16 Bi ions in the $P_{1}$ unit cell permits up to 16 distinct Bi types. However, bond length distributions for Bi ions in this structure clearly split into two classes where there are minor differences in bond length within a class, which are typically less than 0.005 Å. In the $Pna2_{1}$ structure, symmetry constraints allow two types of Bi and two types of Ti. Both types of Bi [labeled Bi(1) and Bi(2)] have similar mean bond lengths in $P_{1}$ and $Pna2_{1}$ (ranging only from 2.52 to 2.54 Å), although the distribution of bond lengths is somewhat different in the two types of Bi (Table I). The approximately cubic coordination of the two types of Bi ion is shown in Fig. 3. There are two types of Ti in the $P_{1}$ and $Pna2_{1}$ structures with very similar mean TiO bond lengths (Table I). Unique fractional coordinates for the energy minimized $Pna2_{1}$ structure are given in Table II.

As mentioned above, structure determination of $Bi_{2}Ti_{2}O_{6}O'$ by RMC analysis³ shows displacement of Bi ions off the O′O′ axis by around 0.4 Å, resulting in a O′BiO′ bond angle of around 160°. When Bi is displaced from its ideal position at the center of the puckered ring, it can move toward one of the O ions in the ring or between a pair of ions in the ring. The former site is the 96g Wyckoff position of the $Fd\overline{3}m$ space group and the latter is the 96h position. Shoemaker et al.³ find a preference for occupation of the 96h site but the ratio of frequencies of occupation of either site is just 5:4. They find an approximately sinusoidal distribution of frequencies for the Bi displacement angle, $\theta$, with six maxima in the range $0<\theta\leq360^{\circ}$, corresponding to the 96h site and minima corresponding to the 96g site. $BiO_{6}O_{2}'$ polyhedra for Bi(1) and Bi(2) ions in the relaxed $Pna2_{1}$ structure are shown in Fig. 4. Bi(1) ions are displaced away from the O′O′ axis toward two O ions resulting in BiO bond distances of 2.30 and 2.31 Å while Bi(2) ions are displaced toward one O ion and the BiO bond distance is 2.28 Å. Bi(1) therefore occupies a site similar to the 96h position and Bi(2) occupies a site similar to the 96g position in the ideal pyrochlore structure. The magnitude of the displacement of Bi(1) from the O′O′ axis is 0.41 Å compared to 0.20 Å for the displacement of Bi(2) from the O′O′ axis. The model obtained from RMC analysis³ found the Bi displacement to be distributed around 0.4 Å; however, the distribution is skewed and has extra weight below 0.4 Å which may be due to a second type of Bi ion with a smaller displacement. There is a preference for the 96h site in the RMC model by 5:4 whereas there are equal numbers of Bi ions in 96h and 96g sites in the relaxed $P_{1}$ and $Pna2_{1}$ structures.

Changes in the Bi₂O′ network between the $Fd\overline{3}m$ structure and the $P_{1}$ or $Pna2_{1}$ structures can best be understood by looking at O′Bi₄ tetrahedra. In both $P_{1}$ and $Pna2_{1}$ structures, there is a single type of O′Bi₄ tetrahedron containing two Bi(1) and two Bi(2) ions. BiBi distances in these tetrahedra are given in Table I. The BiBi distance in the $Fd\overline{3}m$ structure is 3.67 Å and the dispersion of BiBi distances in

<table>
<caption>TABLE I. BiO, BiO′, and TiO bond lengths, BiBi distances and mean bond lengths in angstrom from DFT energy minimization.</caption>
<tbody>
<tr>
<td colspan="2">
$Fd\overline{3}m$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="2">
BiO
</td>
<td colspan="6">
2.58 (6)
</td>
</tr>
<tr>
<td colspan="2">
BiO′
</td>
<td colspan="6">
2.25 (2)
</td>
</tr>
<tr>
<td colspan="2">
TiO
</td>
<td colspan="6">
1.99 (6)
</td>
</tr>
<tr>
<td colspan="2">
BiBi
</td>
<td colspan="6">
3.67 (6)
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="2">
$P_1$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(1)O
</td>
<td>
2.30
</td>
<td>
2.33
</td>
<td>
2.52
</td>
<td>
2.53
</td>
<td>
2.94
</td>
<td>
3.05
</td>
</tr>
<tr>
<td>
Bi(2)O
</td>
<td>
2.28
</td>
<td>
2.41
</td>
<td>
2.44
</td>
<td>
2.75
</td>
<td>
2.77
</td>
<td>
2.98
</td>
</tr>
<tr>
<td>
Bi(1)O′
</td>
<td>
2.25
</td>
<td>
2.28
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(2)O′
</td>
<td>
2.26
</td>
<td>
2.27
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Ti(1)O
</td>
<td>
1.90
</td>
<td>
1.92
</td>
<td>
1.97
</td>
<td>
1.97
</td>
<td>
2.08
</td>
<td>
2.09
</td>
</tr>
<tr>
<td>
Ti(2)O
</td>
<td>
1.95
</td>
<td>
1.95
</td>
<td>
1.96
</td>
<td>
1.99
</td>
<td>
2.00
</td>
<td>
2.02
</td>
</tr>
<tr>
<td>
Bi(1)Bi(1)
</td>
<td>
3.72
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(1)Bi(2)
</td>
<td>
3.60
</td>
<td>
3.64
</td>
<td>
3.77
</td>
<td>
3.79
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(2)Bi(2)
</td>
<td>
3.67
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="2">
$Pna2_1$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(1)O
</td>
<td>
2.30
</td>
<td>
2.31
</td>
<td>
2.46
</td>
<td>
2.59
</td>
<td>
2.95
</td>
<td>
3.13
</td>
</tr>
<tr>
<td>
Bi(2)O
</td>
<td>
2.28
</td>
<td>
2.36
</td>
<td>
2.46
</td>
<td>
2.74
</td>
<td>
2.86
</td>
<td>
2.97
</td>
</tr>
<tr>
<td>
Bi(1)O′
</td>
<td>
2.26
</td>
<td>
2.29
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(2)O′
</td>
<td>
2.25
</td>
<td>
2.27
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Ti(1)O
</td>
<td>
1.91
</td>
<td>
1.92
</td>
<td>
1.95
</td>
<td>
1.98
</td>
<td>
2.05
</td>
<td>
2.12
</td>
</tr>
<tr>
<td>
Ti(2)O
</td>
<td>
1.94
</td>
<td>
1.95
</td>
<td>
1.96
</td>
<td>
1.99
</td>
<td>
2.00
</td>
<td>
2.03
</td>
</tr>
<tr>
<td>
Bi(1)Bi(1)
</td>
<td>
3.73
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(1)Bi(2)
</td>
<td>
3.59
</td>
<td>
3.61
</td>
<td>
3.78
</td>
<td>
3.85
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Bi(2)Bi(2)
</td>
<td>
3.67
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$Fd\overline{3}m$
</td>
<td>
$P_1$
</td>
<td>
$Pna2_1$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(1)O$\rangle$
</td>
<td>
2.58
</td>
<td>
2.52
</td>
<td>
2.54
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(2)O$\rangle$
</td>
<td>
2.58
</td>
<td>
2.53
</td>
<td>
2.52
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(1)O′$\rangle$
</td>
<td>
2.25
</td>
<td>
2.26
</td>
<td>
2.28
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(2)O′$\rangle$
</td>
<td>
2.25
</td>
<td>
2.27
</td>
<td>
2.26
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Ti(1)O$\rangle$
</td>
<td>
1.99
</td>
<td>
1.99
</td>
<td>
1.99
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Ti(2)O$\rangle$
</td>
<td>
1.99
</td>
<td>
1.98
</td>
<td>
1.98
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(1)Bi(1)$\rangle$
</td>
<td>
3.67
</td>
<td>
3.72
</td>
<td>
3.73
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(1)Bi(2)$\rangle$
</td>
<td>
3.67
</td>
<td>
3.70
</td>
<td>
3.71
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\langle$Bi(2)Bi(2)$\rangle$
</td>
<td>
3.67
</td>
<td>
3.67
</td>
<td>
3.67
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

the $P_1$ and $Pna2_1$ structures is 3.59–3.85 Å. The view of the O′Bi₄ tetrahedra in Fig. 3(d) along the [100] direction shows strong buckling of Bi rows along [001] similar to that found in RMC data.³ The view of the $Fd\overline{3}m$ and $Pna2_1$ O′Bi₄ tetrahedra along the [010] axis in Fig. 5 shows how the O′Bi₄ tetrahedra pack in alternating rows in (010) planes in the $Pna2_1$ structure.

### B. Electronic structure

The electronic structure of Bi₂Ti₂O₆O′ from DFT calculations has been reported previously⁴,⁵,⁷ and so only a brief description of the electronic structure is given here. In common with previous work on Bi₂Ti₂O₆O′,⁴,⁵ we find a group of bands at the bottom of the valence band which has mainly Bi 6s character. The valence band for the $Pna2_1$ structure consists of a group of bands extending from the valence band maximum down to −5.4 eV and a group of 8 bands extending from −8.2 to −9.7 eV. The density of states for these bands (Fig. 6) shows that the partial density of states from the former group of bands contains contributions from all types of atoms in the unit cell while the latter 8 bands consist mainly of Bi states.

![](./images/811715887093514241_2.jpg)

FIG. 2. Outline and registry of the 88 ion $Fd\overline{3}m$ conventional unit cell and 44 ion $Pna2_1$ primitive unit cell.

Since accommodation of an off-center Bi lone pair has been postulated as the cause of symmetry breaking in the ideal pyrochlore structure in $Bi_2Ti_2O_6O',^{4,5,7}$ the electron density corresponding to these bands was calculated to determine whether or not the lone pair was atom centered. The charge density for the states in the bands which range in energy from $-8.2$ to $-9.7$ eV is shown in Fig. 7. Previous analyses $^{4,5,7}$ of the lone pair in $Bi_2Ti_2O_6O'$ used the electron localization function for the lone pair density rather than the density itself. There is no significant off-centering of the lone

![](./images/811715887093514241_3.jpg)

FIG. 3. (Color online) Bi, Ti, and $O'$ polyhedra in the $Pna2_1$ structure. Large spheres O (red) and $O'$ (brown) ions, medium spheres Bi(1) (dark green) and Bi(2) (light green) ions, small blue spheres Ti ions. (a) Bi(1) polyhedra viewed along the [001] direction. (b) Bi(2) polyhedra viewed along the [100] direction, (c) Ti octahedra viewed along the [100] direction, (d) $O'$ tetrahedra viewed along the [100] direction. Ti(1) octahedra in (c) are in the center of the $BiO'$ diamond network. Ti(2) octahedra form rows between the Ti(1) octahedra.

<table>
<caption>TABLE II. Fractional coordinates for unique ions in the $Pna2_1$ structure for $Bi_2Ti_2O_6O'$ determined from DFT energy minimization. Lattice constants are 7.33340 and 10.37100 Å.</caption>
<tr><td>Bi(1)</td><td>0.46821</td><td>0.02436</td><td>0.01883</td></tr>
<tr><td>Bi(2)</td><td>0.22034</td><td>0.23870</td><td>0.71964</td></tr>
<tr><td>Ti(1)</td><td>0.49128</td><td>0.49330</td><td>0.99697</td></tr>
<tr><td>Ti(2)</td><td>0.25941</td><td>0.76040</td><td>0.75377</td></tr>
<tr><td>O(1)</td><td>0.30771</td><td>0.62654</td><td>0.55680</td></tr>
<tr><td>O(2)</td><td>0.79348</td><td>0.11688</td><td>0.06149</td></tr>
<tr><td>O(3)</td><td>0.71201</td><td>0.62190</td><td>0.95715</td></tr>
<tr><td>O(4)</td><td>0.17647</td><td>0.13538</td><td>0.44955</td></tr>
<tr><td>O(5)</td><td>0.51184</td><td>0.81992</td><td>0.74272</td></tr>
<tr><td>O(6)</td><td>0.99726</td><td>0.92673</td><td>0.25312</td></tr>
<tr><td>O'</td><td>0.52092</td><td>0.87681</td><td>0.24008</td></tr>
</table>

pair density, leading us to conclude that this is not the primary driving force in Bi displacement from the $O'O'$ axis. The band structure for the bands which are mainly composed of Bi $6s$ orbitals consist of four dispersive and four nondispersive bands, for which the density of states shows a sharp peak plus a broad distribution between $-9.7$ and $-8.2$ eV. Dispersion of the bands in the broad distribution is only possible if there is significant covalent interaction between Bi and $O'$ ions. It is possible that interaction between Bi and $O'$ ions drives the distortion, if increased interaction between these ions via Bi ion displacement is energetically favorable.

### C. Vibrational spectrum

Vibrational modes at the $\Gamma$ point of the Brillouin zone were calculated using the frozen phonon method available in CRYSTAL. $^{20,21}$ The phonon contribution to the dielectric function was calculated using Born charges derived from changes induced in Wannier orbitals by atomic displacements along phonon normal coordinates. $^{20,22}$ The methods used are briefly outlined below. It is well known that the polarization in systems with periodic boundary conditions is ill defined. However, changes in polarization due to atomic displacements can be calculated using localized Wannier orbitals. The change in the net dipole moment of Wannier orbitals associated with the zeroth unit cell, $\partial\mu_i$, which is created by an atomic displacement, $\partial u_{\alpha j}$, at the $\alpha^{\text{th}}$ nucleus, defines the atomic Born charge tensors, $Z_{\alpha,ij}^*$,

![](./images/811715887093514241_4.jpg)

FIG. 4. (Color online) $BiO_6O_2'$ polyhedra for Bi(1) in the $96h$ site (left) and Bi(2) in the $96g$ site (right) viewed along the $O'O'$ axis in the $Pna2_1$ structure. Bond lengths are given in angstrom. O ions (red), $O'$ ions (brown), Bi ions (green).

![](./images/811715887093514241_5.jpg)

FIG. 5. (Color online) BiBi distances in angstrom in O'Bi₄ tetrahedra in the ideal pyrochlore $Fd\overline{3}m$ and $P_{1}$ structures viewed along the [010] direction. (Left panel) BiBi distances in O'Bi₄ tetrahedra in the ideal cubic pyrochlore structure are all the same. (Right panel) Bi(1) ions (dark green), Bi(2) ions (light green).

$$
Z_{\alpha, i j}^{*}=\frac{\partial \mu_{i}}{\partial u_{\alpha j}}.\tag{1}
$$

The transformation from atomic, Cartesian coordinates, $u_{\alpha,i}$ to phonon normal coordinates, $Q_{p}$ is,

$$
Q_{p}=\sum_{\alpha, i} \frac{t_{p, \alpha i}}{\sqrt{M_{\alpha}}} u_{\alpha i},\tag{2}
$$

where $p$ labels the vibrational mode, $t_{p,\alpha i}$ contains components of the $p$th phonon eigenvector and $M_{\alpha}$ is the mass of the $\alpha$th atom. Born charge tensors in the normal ($Z$) and atomic, Cartesian ($Z^{*}$) coordinate systems are related by,

![](./images/811715887093514241_6.jpg)

FIG. 6. Atom-projected valence band densities of states for Bi₂Ti₂O₆O' in the $Pna2_{1}$ structure.

![](./images/811715887093514241_7.jpg)

FIG. 7. Charge density in the $Pna2_{1}$ structure associated with a group of 8 bands attributed to Bi 6s lone pairs. (Left panel) Charge density in a (100) plane containing Bi(1) ions. (Right panel) Charge density in a (100) plane containing Bi(2) ions.

$$
Z_{p, i}=\sum_{\alpha, j} \frac{t_{p, \alpha j} Z_{\alpha, i j}^{*}}{\sqrt{M_{\alpha}}}.\tag{3}
$$

The phonon contribution to the long wavelength dielectric function is given in terms of Born charge tensors in the normal coordinate basis and phonon frequencies,

$$
\epsilon_{i j}(\omega)=\frac{4 \pi}{\Omega} \sum_{p} \frac{Z_{p, i} Z_{p, j}}{\omega_{p}^{2}-\omega^{2}-i \omega \gamma_{p}}.\tag{4}
$$

$\Omega$ is the unit-cell volume and $\omega_{p}$ and $\gamma_{p}$ are the frequency and phenomenological damping parameter of the $p$th mode.

The polarization sources which contribute to the dielectric function when a vibrational mode is excited are visualized below by plotting a vector, $z_{p,i\alpha}$, on each atom in the unit cell whose magnitude and direction are proportional to

$$
z_{p, i \alpha}=\sum_{j} \frac{t_{p, \alpha j} Z_{\alpha, i j}^{*}}{\sqrt{M_{\alpha}}}.\tag{5}
$$

This vector corresponds to the cell dipole moment associated with the $p$th vibrational mode, split into its atomic components.

Mode frequencies and the imaginary part of the dielectric function were calculated for the $Fd\overline{3}m$, $P_{1}$, and $Pna2_{1}$ structures described in Sec. II A using a DFT-GGA hamiltonian.²³ Mode frequencies and the imaginary part of the dielectric function were also calculated for Bi₂Ti₂O₆O' in the ideal pyrochlore structure using a B3LYP hamiltonian.²⁴ Mode frequencies for Bi₂Ti₂O₆O' in the ideal pyrochlore structure from a DFT-GGA calculation have been reported previously.⁶ In the absence of dielectric function measurements for Bi₂Ti₂O₆O', we compare the imaginary part of the dielectric function, $\epsilon_{2}$, from Eq. (4), for BTi to spectra for BMN, BZT, and BZN. The latter spectra were generated using a fit to reflectance spectra.¹⁸ The oscillator model used in that work was,

$$
\epsilon(\omega)=\sum_{p} \frac{\Delta \epsilon_{p} \omega_{p}^{2}}{\omega_{p}^{2}-\omega^{2}-i \omega \gamma_{p}}+\epsilon_{\infty},\tag{6}
$$

where $\omega_{p}$, $\gamma_{p}$, and $\Delta \epsilon_{p}$ denote the mode frequency, damping coefficient, and oscillator strength for the $p$th phonon mode, respectively. Fitted damping coefficients lie in the range

<table>
<caption>TABLE III. IR active ($F_{1u}$) mode frequencies in cm⁻¹ for Bi₂Ti₂O₆O′ in the $Fd\overline{3}m$ ideal pyrochlore structure.</caption>
<thead>
  <tr>
    <th>GGAᵃ</th>
    <th>GGAᵇ</th>
    <th>Hybrid DFTᶜ</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>98$i$</td>
    <td>142$i$</td>
    <td>71$i$</td>
  </tr>
  <tr>
    <td>81</td>
    <td>62</td>
    <td></td>
  </tr>
  <tr>
    <td>112</td>
    <td>86</td>
    <td>107</td>
  </tr>
  <tr>
    <td>229</td>
    <td>213</td>
    <td>222</td>
  </tr>
  <tr>
    <td>262</td>
    <td>317</td>
    <td>283</td>
  </tr>
  <tr>
    <td>352</td>
    <td>327</td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>378</td>
  </tr>
  <tr>
    <td>464</td>
    <td>435</td>
    <td>502</td>
  </tr>
</tbody>
</table>

ᵃFennie <i>et al.</i> Ref. 6.
ᵇThis work, GGA calculation.
ᶜThis work, hybrid DFT calculation.

30–100 cm⁻¹, leading to fairly broad peaks in $\epsilon_{2}$ spectra.¹⁸ Damping coefficients of 40 cm⁻¹, were used for dielectric functions obtained from CRYSTAL calculations.

Factor group analysis of the normal modes at the $\Gamma$ point of the $Fd\overline{3}m$ pyrochlore structure yields

$$
\begin{aligned}
\Gamma= & 8 F_{1 u}(I R)+4 F_{2 u}+2 F_{1 g}+4 F_{2 g}(R)+3 E_{u}+E_{g}(R)+3 A_{2 u} \\
& +A_{g}(R),
\end{aligned}
\tag{7}
$$

including three translational modes which belong to the $F_{1u}$ representation. Only the $F_{1u}$ modes are IR active while $F_{2g}$, $E_{g}$, and $A_{g}$ modes are Raman active. Frequencies from DFT-GGA and B3LYP calculations on the ideal pyrochlore structure are given in Tables III and IV.

We find modes with negative eigenvalues belonging to $F_{1u}$, $F_{2u}$, and $E_{u}$ representations for our GGA and hybrid DFT calculations. Since these eigenvalues equal the square of vibrational frequencies, a negative eigenvalue corresponds to an imaginary frequency and an unstable lattice. The earlier calculation of these vibrational frequencies⁶ also reported unstable $F_{1u}$ and $E_{u}$ modes; no $F_{2u}$ modes frequencies were reported. $F_{1u}$ mode frequencies from the three calculations on Bi₂Ti₂O₆O′ in the $Fd\overline{3}m$ structure are compared in Table III. The imaginary part of the dielectric function calculated using Eq. (4), where parameters were obtained from CRYSTAL calculations, is shown in Fig. 8. The modes at 62 and 317 cm⁻¹ dominate the spectrum; modes at other frequencies are barely visible in the spectrum.

<table>
<caption>TABLE IV. $Fd\overline{3}m$ Raman active ($R$) and silent ($S$) mode frequencies. Modes from GGA calculations in this work are given in the upper part of the table and corresponding mode frequencies from Fennie <i>et al.</i> (Ref. 6) are given in the lower part.</caption>
<thead>
  <tr>
    <th>$F_{2g}$ ($R$)</th>
    <th>$E_{g}$ ($R$)</th>
    <th>$A_{g}$ ($R$)</th>
    <th>$E_{u}$ ($S$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>262</td>
    <td>281</td>
    <td>537</td>
    <td>135$i$</td>
  </tr>
  <tr>
    <td>395</td>
    <td></td>
    <td></td>
    <td>100</td>
  </tr>
  <tr>
    <td>535</td>
    <td></td>
    <td></td>
    <td>394</td>
  </tr>
  <tr>
    <td>711</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>278</td>
    <td>369</td>
    <td>462</td>
    <td>100$i$</td>
  </tr>
  <tr>
    <td>414</td>
    <td></td>
    <td></td>
    <td>107</td>
  </tr>
  <tr>
    <td>462</td>
    <td></td>
    <td></td>
    <td>400</td>
  </tr>
  <tr>
    <td>535</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

![](./images/811715887093514241_8.jpg)

FIG. 8. Imaginary part of the dielectric function for BMN, BZT, BZN, and Bi₂Ti₂O₆O′. Spectra for BMN, BZT, and BZN were constructed from fitting parameters to experimental data in Ref. 18 at 50 K. Spectra for Bi₂Ti₂O₆O′ in the $Fd\overline{3}m$, $Pna2_{1}$, and $P_{1}$ structures obtained from first-principles calculations. Parameters fitted using experimental data were oscillator strength, natural frequency, and natural linewidth. Oscillator strengths and natural frequencies for Bi₂Ti₂O₆O′ were obtained from calculations and a natural linewidth of 40 cm⁻¹ was assumed for each mode.

The $Pna2_{1}$ group belongs to the set of groups with $C_{2v}$ point symmetry. Factor group analysis of the normal modes at the $\Gamma$ point of the $Pna2_{1}$ structure yields

$$
\begin{aligned}
\Gamma=33 A_{1}(I R, R)+33 A_{2}(R)+33 B_{1}(I R, R)+33 B_{2}(I R, R).
\end{aligned}
\tag{8}
$$

$A_{1}$, $B_{1}$, and $B_{2}$ modes have net dielectric polarizations parallel to the $c$, $b$, and $a$ axes of the unit cell, respectively. There is a marked difference in the distribution of IR mode intensities on going from the ideal $Fd\overline{3}m$ structure to the relaxed $Pna2_{1}$ or $P_{1}$ structures (Fig. 8). Since there are many more ions in the latter primitive unit cells (22 for $Fd\overline{3}m$, 44 for $Pna2_{1}$, and 88 for $P_{1}$) and the symmetry for the latter two structures is much reduced, we comment only on the modes which have significant intensity in the $Pna2_{1}$ structure $\epsilon_{2}$ spectrum. Strong interaction with IR radiation by the $F_{1u}$ mode at 62 cm⁻¹ in the $Fd\overline{3}m$ structure is replaced by interaction via $A_{1}$ modes at 54, 91, 122, and 131 cm⁻¹, $B_{1}$ modes at 40, 95, and 113 cm⁻¹ and a $B_{2}$ mode at 116 cm⁻¹ (Table V). The IR active mode at 317 cm⁻¹ in the $Fd\overline{3}m$ structure is

<table>
<caption>TABLE V. IR active mode frequencies in per centimeter, relative peak intensities in the $\epsilon_{2}$ spectrum, $I/I_{max}$, and mode contributions, $\epsilon_{p}$, to the dielectric constant for $Pna2_{1}$ $Bi_{2}Ti_{2}O_{6}O'$. Relative intensities are proportional to $Z_{p}^{2}/\omega_{p}$ and contributions to the dielectric constant are proportional to $Z_{p}^{2}/\omega_{p}^{2}$ (Eq. (4)). $A_{1}$, $B_{1}$, and $B_{2}$ modes couple to light with the electric vector parallel to the $c$, $b$, and $a$ axes, respectively.</caption>
<thead>
<tr>
<th colspan="3">$A_{1}$ $^{\mathrm{a}}$</th>
<th colspan="3">$B_{1}$ $^{\mathrm{a}}$</th>
<th colspan="3">$B_{2}$ $^{\mathrm{a}}$</th>
</tr>
<tr>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{I/I_{max}}$</th>
<th>$\boldsymbol{\epsilon_{p,cc}}$</th>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{I/I_{max}}$</th>
<th>$\boldsymbol{\epsilon_{p,bb}}$</th>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{I/I_{max}}$</th>
<th>$\boldsymbol{\epsilon_{p,aa}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$202i$</td>
<td></td>
<td></td>
<td>$40$</td>
<td>$0.48$</td>
<td>$96.7$</td>
<td>$116$</td>
<td>$1.00$</td>
<td>$69.4$</td>
</tr>
<tr>
<td>$54$</td>
<td>$0.15$</td>
<td>$23.4$</td>
<td>$95$</td>
<td>$0.21$</td>
<td>$18.0$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$91$</td>
<td>$0.38$</td>
<td>$33.7$</td>
<td>$113$</td>
<td>$0.88$</td>
<td>$62.9$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$122$</td>
<td>$0.17$</td>
<td>$11.5$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$131$</td>
<td>$0.12$</td>
<td>$7.6$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$286$</td>
<td>$0.21$</td>
<td>$5.7$</td>
<td>$281$</td>
<td>$0.34$</td>
<td>$9.8$</td>
<td>$267$</td>
<td>$0.11$</td>
<td>$3.4$</td>
</tr>
<tr>
<td>$336$</td>
<td>$0.13$</td>
<td>$3.2$</td>
<td></td>
<td></td>
<td></td>
<td>$285$</td>
<td>$0.13$</td>
<td>$3.6$</td>
</tr>
<tr>
<td>$356$</td>
<td>$0.10$</td>
<td>$2.2$</td>
<td></td>
<td></td>
<td></td>
<td>$334$</td>
<td>$0.12$</td>
<td>$2.9$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">$^{\mathrm{a}}$Only modes with relative intensities greater than 10% of the most intense mode are shown.</td>
</tr>
</tfoot>
</table>

replaced by $A_{1}$ modes at 286, 336, and $356\ \mathrm{cm}^{-1}$, a $B_{1}$ mode at $281\ \mathrm{cm}^{-1}$ and $B_{2}$ modes at 267, 285, and $334\ \mathrm{cm}^{-1}$. The highest mode frequencies in the $Pna2_{1}$ structure lie around $750\ \mathrm{cm}^{-1}$ $(741,\ 747,\ 755\ \mathrm{cm}^{-1})$ and may be observed in Raman spectroscopy.

There is one unstable $A_{1}$ mode in the $Pna2_{1}$ structure whereas there are eight unstable modes (including degeneracy factors) in the $Fd\overline{3}m$ structure. The $Fd\overline{3}m$ structure is definitely unstable whereas the $Pna2_{1}$ unstable mode may result from the inability of the energy minimization algorithm to find the absolute energy minimum in a complex structure such as this. Small rotations of polyhedra may have very flat potential energy surfaces close to the equilibrium structure, leading to convergence close to but not at, equilibrium.

The $\epsilon_{2}$ spectrum shown in Fig. 8 is calculated using Eq. (4) and includes contributions from all IR active modes. Thus we do not assume any specific polarization for the incident electric field in generating the spectra for the $P_{1}$ and $Pna2_{1}$ structures of $Bi_{2}Ti_{2}O_{6}O'$. Table V gives the predicted maximum intensity of each mode in the $\epsilon_{2}$ spectrum calculated using Eq. (4). The Lorentz oscillator form assumed for the frequency dependence of the dielectric function in Eq. (4) predicts a maximum value of $4\pi Z_{p}^{2}/\Omega\gamma_{p}\omega_{p}$ at $\omega_{p}$. Relative values of $Z_{p}^{2}/\omega_{p}$ are compared in Table V, where it is shown that the most intense peak in the $\epsilon_{2}$ spectrum is a $B_{1}$ mode at $116\ \mathrm{cm}^{-1}$. Equation (4) also predicts a dielectric constant value of $4\pi Z_{p}^{2}/\Omega\omega_{p}^{2}$. Contributions of modes which make significant contributions to the dielectric constant are also given in Table V. The phonon contribution to the diagonal elements of the dielectric tensor, when all modes are taken into account, is $\epsilon_{aa}=101.7$, $\epsilon_{bb}=198.3$, and $\epsilon_{cc}=102.9$. There is considerable anisotropy in the dielectric constant whereas the macroscopic $Fd\overline{3}m$ symmetry found for $Bi_{2}Ti_{2}O_{6}O'$ implies an isotropic dielectric constant tensor. Anisotropy in the dielectric constant tensor is, of course, allowed in the $Pna2_{1}$ space group, which has $C_{2v}$ point symmetry. The relationship between the long-range cubic symmetry in $Bi_{2}Ti_{2}O_{6}O'$ and breaking of this symmetry at short range, through Bi displacements and possibly other sources, was mentioned above. Restoration of a macroscopic cubic symmetry is expected to lead to restoration of cubic symmetry in the dielectric constant tensor also.

Table V shows that modes with vibrational frequencies below $120\ \mathrm{cm}^{-1}$ contribute the majority of the dielectric constant in each case. $A_{1}$ modes at 54 and $91\ \mathrm{cm}^{-1}$ make contributions of 23.4 and 33.7 to $\epsilon_{cc}$, the $B_{1}$ modes at 40, 95, and $113\ \mathrm{cm}^{-1}$ make contributions of 96.7, 18.0, and 62.9 to $\epsilon_{bb}$ and the $B_{2}$ mode at $116\ \mathrm{cm}^{-1}$ contributes 69.4 to $\epsilon_{aa}$. When we compare the dielectric function spectra for BMN, BZT, and BZN in Fig. 8 to spectra for $Bi_{2}Ti_{2}O_{6}O'$ in the $P_{1}$ or $Pna2_{1}$ structures, we find three modes between 40 and $200\ \mathrm{cm}^{-1}$ (BMN 42, 108, and $173\ \mathrm{cm}^{-1}$, BZT 50, 144 and $191\ \mathrm{cm}^{-1}$, BZN 42, 88 and $142\ \mathrm{cm}^{-1}$) which make large contributions to the dielectric constant for each material. $^{18}$ Parameters from Ref. 18 fitted to Eq. (6) predict dielectric

<table>
<caption>TABLE VI. IR active mode frequencies in $\mathrm{cm}^{-1}$ and mode contributions, $\epsilon_{p}$, to the dielectric constant for BMN, BZT. and BZN.</caption>
<thead>
<tr>
<th colspan="2">BMN</th>
<th colspan="2">BZT</th>
<th colspan="2">BZN</th>
</tr>
<tr>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{\epsilon_{p}}$</th>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{\epsilon_{p}}$</th>
<th>$\boldsymbol{\omega}$</th>
<th>$\boldsymbol{\epsilon_{p}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$42$</td>
<td>$21.6$</td>
<td>$50$</td>
<td>$16.1$</td>
<td>$42$</td>
<td>$48.8$</td>
</tr>
<tr>
<td>$108$</td>
<td>$18.5$</td>
<td>$144$</td>
<td>$14.8$</td>
<td>$88$</td>
<td>$12.8$</td>
</tr>
<tr>
<td>$173$</td>
<td>$16.0$</td>
<td>$191$</td>
<td>$9.2$</td>
<td>$142$</td>
<td>$18.9$</td>
</tr>
</tbody>
</table>

![](./images/811715887093514241_9.jpg)

FIG. 9. (Color online) Polarization associated with vibrational modes in $Pna2_1$ $Bi_2Ti_2O_6O'$ decomposed into dipole moments on atomic sites derived from Born charge tensors and phonon displacements. Left panel $B_1$ mode at $40\ \text{cm}^{-1}$. Center panel $B_2$ mode at $116\ \text{cm}^{-1}$. Right panel $B_1$ mode at $281\ \text{cm}^{-1}$.

constants of 68.9, 54.2, and 100.7 for BMN, BZT, and BZN, respectively. Contributions to the dielectric constant from these modes are given in Table VI.

Most of the modes listed in Table VI make contributions to the dielectric constant less than 20 while contributions for modes up to $200\ \text{cm}^{-1}$ listed in Table V range from 11.5 to 96.7. One mode in the fitted experimental data ($42\ \text{cm}^{-1}$ in BZN) has a significantly larger contribution (48.8). Hence it is clear that a small number of low frequency modes are responsible for the anomalously large dielectric constants in these materials.

In order to gain further insight into polarization sources in the $Pna2_1$ structure, Born charges in the normal mode basis split into atomic contributions as in Eq. (5), are shown in Fig. 9. The modes analyzed are the $B_1$ modes at 40 and $281\ \text{cm}^{-1}$ and the $B_2$ mode at $116\ \text{cm}^{-1}$. The first of these has the largest contribution of all to the dielectric function, the second is the main contributor to the peak in the $\epsilon_2$ spectrum around $280\ \text{cm}^{-1}$ and the third is the main contributor to the peak around $110\ \text{cm}^{-1}$.

Polarization sources in the $40\ \text{cm}^{-1}$ mode shown in the left panel in Fig. 9 show relatively large dipole moments on Bi(1) and Bi(2) sites. However, these moments make a relatively small contribution to the total cell moment because Bi(1) and Bi(2) contributions tend to cancel. Most of the polarization of this mode comes from a fairly uniform distribution of dipole moments on O ions. These are not seen in Fig. 9 as the arrows are smaller than the O ion sphere radii.

Polarization sources in the $B_2$ mode at $116\ \text{cm}^{-1}$ are shown in the center panel of Fig. 9. The majority of the cell dipole moment in this mode is associated with Ti(1) and Ti(2) ions. Dipole moments on Ti(1) sites are nearly aligned with the $a$ axis. Since $B_2$ modes have a net polarization along the $a$ axis only, Ti(1) sites make the greater contribution to the net cell dipole moment in this mode.

Polarization sources in the $B_1$ mode at $281\ \text{cm}^{-1}$ are shown in the right panel of Fig. 9. Cell dipole moments are mainly located on some O ions and all of the O$'$ ions. The net cell polarization is along the $b$ axis and dipole moments are mainly strongly aligned with this axis.

Figure 9 shows that while heavy ions such as Bi may have large amplitude displacements in low-frequency vibrational modes, they do not necessarily make the main contribution to the macroscopic polarization. The mode at $40\ \text{cm}^{-1}$ is a relatively low-frequency mode with most of the polarization associated with O and O$'$ ions.

TABLE VII. Atomic Bi, Ti and. O Born charges for $Bi_2Ti_2O_6O'$ in the $Pna2_1$ structure.

|          |          |
|----------|----------|
| Bi(1)    | 5.08     |
| Bi(2)    | 5.12     |
| Ti(1)    | 7.22     |
| Ti(2)    | 7.34     |
| O(1)     | $-$3.03  |
| O(2)     | $-$3.20  |
| O(3)     | $-$3.04  |
| O(4)     | $-$3.09  |
| O(5)     | $-$3.07  |
| O(6)     | $-$3.09  |
| O$'$     | $-$2.80  |

Born charges for $Bi_2Ti_2O_6O'$ are given in Table VII. Born charges are defined to be the trace of the Born charge tensor divided by three. Table VII shows Born charges for Bi ions greater than 5, for Ti ions greater than 7, O ion charges ranging from $-3.03$ to $-3.20$ and an O$'$ charge of $-2.80$.

### III. SUMMARY

The $Bi_2O'$ network in the ideal cubic pyrochlore structure can be viewed as a diamond lattice of O$'$ ions connected by Bi ions with well-defined O'Bi$_4$ tetrahedra. The ideal cubic pyrochlore structure contains rows of Bi ions along [101] and $[10\overline{1}]$ directions. When this structure is allowed to relax with no symmetry constraints ($P_1$) or $Pna2_1$ symmetry constraints, these rows are found to contain two distinct types of Bi ion, denoted here as Bi(1) and Bi(2). The rows are visible on the diagonal running from bottom left to top right in the top panel of Fig. 5 and Bi(1) rows with up-down buckling are shown in Fig. 3(d). Bi(1) rows contain Bi ions in a $96h$ Wyckoff position of the $Fd\overline{3}m$ unit cell with a large displacement of the Bi ion from the O'O' axis $(0.4\ \mathring{A})$ and the pattern of displacements of Bi(1) is similar to the pattern shown in Fig. 7b of Ref. 3. Bi(2) rows contain Bi ions in a $96g$ Wyckoff position with a smaller displacement of the Bi ion from the O'O' axis $(0.2\ \mathring{A})$.

The unit cells used for the structure relaxations in this work contained 44 or 88 ions for the $Pna2_1$ or $P_1$ structures and may be significantly smaller than any domain making up the macroscopic structure which has cubic symmetry on average.$^2$ Nevertheless, the pattern of displacements obtained from these cells is similar to that found from RMC data; it also resembles the structure found for $Bi_2Ti_2O_6O'$ in previous first-principles energy minimization calculations.$^5$

The electronic density of states for $Bi_2Ti_2O_6O'$ in this work is similar to that reported previously.$^{4-6}$ The charge density from bands, which are predominantly of Bi 6$s$ character, is calculated in a (100) plane which contains Bi(1) rows and is perpendicular to Bi(2) rows. Charge density about Bi ions is spherically symmetric, except along BiO' bond directions. It is suggested that buckling of Bi rows, which is largest in Bi(1) rows, is caused by covalent interac-

tions with O' ions rather than the need to accommodate an off-center Bi 6s lone pair, as has been suggested previously. $^{4,5,7}$

Vibrational modes were calculated for $Bi_{2}Ti_{2}O_{6}O'$ in the $F d \overline{3} m$, $P n a 2_{1}$, and $P_{1}$ structures. The imaginary part of the dielectric function was calculated using oscillator strengths obtained from Born charges in the phonon normal mode basis. The $F d \overline{3} m$ structure has three unstable vibrational modes belonging to the $F_{1 u}, F_{2 u}$, and $E_{u}$ irreducible representations. The $P n a 2_{1}$ structure has one unstable vibrational mode belonging to the $A_{1}$ irreducible representation.

Two out of seven $F_{1 u}$ IR active modes in the $\epsilon_{2}$ spectrum for the $F d \overline{3} m$ structure have the great majority of the oscillator strength. These modes occur at 62 and $317 ~cm^{-1}$ . $A_{1}$ modes at 91,286 and $336 ~cm^{-1}, B_{1}$ modes at $40,95,113$ , and $281 ~cm^{-1}$ and a $B_{2}$ mode at $116 ~cm^{-1}$ carry the majority of the oscillator strength in the $\epsilon_{2}$ spectrum of the $P n a 2_{1}$ structure. The $\epsilon_{2}$ spectra for the $P n a 2_{1}$ and $P_{1}$ structures closely resemble each other.

Oscillator strengths and mode frequencies from our calculations are compared to parameters obtained by fitting $\epsilon_{2}$ data from reflectivity measurements $^{18}$ on related pyrochlore structures such as $Bi_{1.5} Zn_{0.92} Nb_{1.5} O_{6.92}$ . Three or four phonons contribute the majority of the dielectric constant for $Bi_{2} Ti_{2} O_{6} O', \ Bi_{1.5} Zn_{0.92} Nb_{1.5} O_{6.92}, \ Bi_{3 / 2} MgNb_{3 / 2} O_{6} O'$ , or $Bi_{3 / 2} ZnTa_{3 / 2} O_{6} O'$ . These phonons lie between 40 and $140 ~cm^{-1}(Bi_{2} Ti_{2} O_{6} O^{\prime})$ or between 40 and $190 ~cm^{-1}$ for theother materials. $^{18}$

The anisotropic dielectric constant tensor obtained for $Bi_{2} Ti_{2} O_{6} O'$ has components $\epsilon_{a a}=101.7, \epsilon_{b b}=198.3$ , and $\epsilon_{c c}$ =102.9. These values may be compared to isotropic dielectric constants measured for related pyrochlores which lie in the range 52 to 106, including a high-frequency electronic contribution of around $5.^{18}$ The dielectric constant of Bi, Ti,O,O' is difficult to obtain by similar means since it decomposes at temperatures well below typical sintering temperatures for these materials. The value of the dielectricconstant obtained for $Bi_{2} Ti_{2} O_{6} O'$ is perhaps 50 to $100 \%$  larger than these values. Larger values for dielectric con- stants from first principles calculations may be expected since they tend to predict vibrational mode frequencies lowerthan experimental values, when a DFT hamiltonian is used; furthermore, sintered materials may have a lower density than that of the perfect bulk crystal and hence a lower dielectric constant. The anisotropic dielectric constant tensor for Bi, Ti,O,O' may be reconciled with its cubic, macroscopic symmetry by noting that experiment $^{2,3}$ finds the cubic sym metry to be broken at short length scales. The unit cells used for the work reported here are much smaller than expected domain sizes, which may give a macroscopic sample a macroscopic, cubic symmetry.

## ACKNOWLEDGMENTS
This work was supported by Science Foundation Ireland under Grant No. RFP/09/MTR2295. Computer time was pro- vided by the Trinity Centre for High Performance Computing which is supported by the Irish Higher Education Authority and Science Foundation Ireland. The author wishes to acknowledge helpful discussions with J. C. Nino, A. L. Hector, D. J. Arenas, and D. B. Tanner and to thank D. B. Tanner for suggesting this problem for study.

## APPENDIX: DETAILS OF CALCULATIONS
The basis sets and pseudopotentials used for these calculations were as follows: Bi the ECP78MWB quasirelativistic pseudopotential and corresponding $4 s 3 p 1 d / 2 s 2 p 1 d$ Gaussian orbital basis from the Stuttgart/Cologne group; $^{26} Ti$ the Hay-Wadt small core pseudopotential and a $6 s 6 p 5 d / 3 s 3 p 3 d$  basis originally used in conjunction with that pseudopotential to study titanates; $^{27} O$ the all-electron $14 s 6 p / 4 s 3 p$ basis originally used to study $NiO$ (Ref. 28) supplemented with a $d$  orbital with exponent of 0.5. Integration over the Brillouin zone was done using a $3 \times 3 \times 3$ Monkhorst-Pack net $^{29}$ for the $P_{1}$ and $P n a 2_{1}$ structures and a $6 \times 6 \times 6$ net for the $F d \overline{3} m$  unit cell. CRYSTAL code lattice sum tolerances of 7777 and14 were used. Figures 1, 3-5, and 9 were produced using theVESTA visualization package. $^{30}$

---

$^{1}$ I. Radosavljevic, J. S. O. Evans, and A. W. Sleight, J. Solid State Chem. 136, 63 (1998).
$^{2}$ A. L. Hector and S. B. Wiggin, J. Solid State Chem. 177, 139(2004).
$^{3}$ D. P. Shoemaker, R. Seshadri, A. L. Hector, A. Llobet, T. Proffen, and C. J. Fennie, Phys. Rev. B 81, 144113 (2010).
4R. Seshadri, Solid State Sci. 8, 259 (2006).
$^{5}$ B. B. Hinojosa, J. C. Nino, and A. Asthagiri, Phys. Rev. B 77,104123 (2008).
°C. J. Fennie, R. Seshadri, and K. M. Rabe, arXiv:0712.1846v1(unpublished).
7B. C. Melot, R. Tackett, J. O'Brien, A. L. Hector, G. Lawes, R. Seshadri, and A. P. Ramirez, Phys. Rev. B 79, 224111 (2009).
8M. Avdeev, M. K. Haas, J. D. Jorgensen, and R. J. Cava, J. Solid State Chem. 169, 24 (2002).
°I. Levin, T. G. Amos, J. C. Nino, T. A. Vanderah, C. A. Randall, and M. T. Lanagan, J. Solid State Chem. 168, 69 (2002).
101. R. Evans, J. A. K. Howard, and J. S. O. Evans, J. Mater. Chem.13, 2098 (2003).
"Q. Zhou, B. J. Kennedy, V. Ting, and R. L. Withers, J. Solid State Chem. 178, 1575 (2005).
12B. Melot, E. Rodriguez, T. Proffen, M. A. Hayward, and R. Seshadri, Mater. Res. Bull. 41, 961 (2006).
13S. J. Henderson, O. Shebanova, A. L. Hector, P. F. McMillan, and M. T. Weller, Chem. Mater. 19, 1712 (2007).
14E. E. Rodriguez, F. Poineau, A. llobet, K. Czerwinski, R. Seshadri, and A. K. Cheetham, Inorg. Chem. 47, 6281 (2008).
15M. A. Subramanian, G. Aravamudan, and G. V. Subba-Rao, Prog. Solid State Chem. 15, 55 (1983).
16E. R. Cope and M. T. Dove, J. Phys.: Condens. Matter 22,

155103-9

125401 (2010).

$^{17}$J. C. Nino, M. T. Langran, C. A. Randall, and S. Kamba, *Appl. Phys. Lett.* **81**, 4404 (2002).

$^{18}$M. Chen, D. B. Tanner, and J. C. Nino, *Phys. Rev. B* **72**, 054303 (2005).

$^{19}$J. C. Nino, D. B. Tanner, D. J. Arenas, and A. L. Hector (private communication).

$^{20}$R. Dovesi *et al.*, *CRYSTAL06 User's Manual* (University of Torino, Torino, 2007).

$^{21}$F. Pascale, C. Zicovich-Wilson, F. Lopez, B. Civalleri, R. Orlando, and R. Dovesi, *J. Comput. Chem.* **25**, 888 (2004).

$^{22}$C. Zicovich-Wilson, F. J. Torres, F. Pascale, L. Valenzano, R. Orlando, and R. Dovesi, *J. Comput. Chem.* **29**, 2268 (2008).

$^{23}$J. P. Perdew and Y. Wang, *Phys. Rev. B* **45**, 13244 (1992).

$^{24}$A. D. Becke, *J. Chem. Phys.* **98**, 5648 (1993).

$^{25}$D. M. Hatch and H. T. Stokes, *Phys. Rev. B* **65**, 014113 (2001).

$^{26}$W. Küchle, M. Dolg, H. Stoll, and H. Preuss, *Mol. Phys.* **74**, 1245 (1991).

$^{27}$S. Piskunov, E. Heifets, R. I. Eglitis, and G. Borstel, *Comput. Mater. Sci.* **29**, 165 (2004).

$^{28}$M. D. Towler, N. L. Allan, N. M. Harrison, V. R. Saunders, W. C. Mackrodt, and E. Aprà, *Phys. Rev. B* **50**, 5041 (1994).

$^{29}$H. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188 (1976).

$^{30}$K. Momma and F. Izumi, *J. Appl. Crystallogr.* **41**, 653 (2008).