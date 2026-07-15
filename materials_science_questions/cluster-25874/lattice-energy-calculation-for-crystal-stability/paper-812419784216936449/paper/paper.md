![](./images/812419784216936449_1.jpg)

Available online at www.sciencedirect.com

![](./images/812419784216936449_2.jpg)

Chemical Physics Letters 370 (2003) 218–226

![](./images/812419784216936449_3.jpg)

www.elsevier.com/locate/cplett

# Ab initio MO based lattice energy for molecular crystals: packing structure of electron donor-acceptor (EDA) complex $\mathrm{H}_{3} \mathrm{~N}-\mathrm{BF}_{3}$

Tohru Ikeda $^{\mathrm{a}}$, Kanade Nagayoshi $^{\mathrm{a}}$, Kazuo Kitaura $^{\mathrm{b}, *}$

${ }^{\mathrm{a}}$ College of Integrated Arts and Sciences, Osaka Prefecture University, Sakai, Osaka 599-8531, Japan
${ }^{\mathrm{b}}$ Research Institute for Computational Sciences, National Institute of Advanced Industrial Science and Technology,
1-1-1 Umezono, Tsukuba, Ibaraki 305-8568, Japan

Received 14 August 2002; in final form 24 December 2002

## Abstract

A computational procedure is proposed for calculating the lattice energy of molecular crystals using the ab initio MO method. Our method does not require any adjustable parameters and provides a general description for various molecular crystals including electron donor-acceptor (EDA) complexes. Using the method, the packing structure of $\mathrm{H}_{3} \mathrm{~N}-\mathrm{BF}_{3}$ crystal was optimized at the HF/3-21 + G level and the lattice energy was calculated at the MP2/6-311 + G* level. The calculation reproduced the experimental lattice constants with reasonable accuracy. Moreover, the structural feature of the $\mathrm{H}_{3} \mathrm{~N}-\mathrm{BF}_{3}$ crystal was discussed based on the molecular interactions in the crystal.

© 2003 Elsevier Science B.V. All rights reserved.

## 1. Introduction

The theoretical prediction of packing structures of molecular crystals is important for understanding, predicting, and controlling the properties of matter. Much effort, therefore, has been made so far. It still remains, however, to be an unsolved problem with serious obstacles for material science [1,2]. One of the problems to be solved is related to potential functions. The packing structure calculations of molecular crystals have been made using classical intermolecular potential functions such as atom-atom type potentials [3-9]. Although the potential functions require moderate computational costs, efforts and skills are necessary to generate them reliably. Moreover, it seems very difficult to get well-balanced description of intermolecular interactions for various relative configurations of molecules in crystals, especially for molecules with large anisotropy, many-body effects, and/or delocalization of electrons [10,11].

In this Letter, we propose a method to calculate the lattice energy using the ab initio MO method: the lattice energy is directly obtained from ab initio MO calculations. A similar method has been applied to the packing structure calculation of

*Corresponding author. Fax: +81-298-61-3171.
E-mail address: kazuo.kitaura@aist.go.jp (K. Kitaura).

0009-2614/03/$ - see front matter © 2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0009-2614(03)00081-2

acetylene crystal [12]. They assumed that the mo-
lecular interaction in the crystal is pairwise addi-
tive and the lattice energy was given as a sum of
pair interaction energy between molecules. The
pair energy was calculated using the ab initio MO
method at the HF level and the London's formula
for dispersion energy. We also employ a pair in-
teraction approximation but include many-body
polarization energy in the one-body term of the
lattice energy, which is important for polar mole-
cules, and evaluate the electron correlation energy
by the MP2 method.

Our method does not require any adjustable
parameters and is applicable to a variety of mole-
cules. The EDA complex, a target of our method, is
concerned with charge transfer interaction which is
a strong interaction with large anisotropy. Classi-
cal potential functions have serious difficulties de-
scribing such interaction appropriately. Therefore,
the computational predictions of packing structure
of EDA complexes have not been done as yet.
Hence, the EDA complex is an appropriate target
of the present method to demonstrate applicability
and validity.

$\mathrm{H}_{3} \mathrm{N}-\mathrm{BF}_{3}$ complex is known as an increvalent
complex. For a series of such complexes with
the $\mathrm{B}-\mathrm{N}$ dative bond, it has been reported that the
$\mathrm{B}-\mathrm{N}$ bond length is shorter in the crystal than in the
gas phase [13,14]. We performed the optimization
of the packing structure and examined the $\mathrm{B}-\mathrm{N}$
bond shrinking in the crystal. We also performed an
analysis of the intermolecular interactions to un-
derstand the packing structure of the crystal.

## 2. Method

The lattice energy $E_{\text {latt }}$ is given as a sum of one-
body energy $e_{I}$ and two-body energy $e_{I J}$

$$
E_{\text {latt }}=\sum_{I}\left(e_{I}+\frac{1}{2} \sum_{J \neq I} e_{I J}\right),
\tag{1}
$$

where $I$ runs over all molecules within an 'asym-
metric unit' in which the molecule is regarded as an
unit object for symmetry operations associated
with the space group symmetry of the crystal,
and $J$ runs over all the others generated by the
symmetry operations. We will describe a proce-
dure to calculate $e_{I}$ and $e_{I J}$ by the ab initio MO
method.

First, we describe the computational procedure
for the one-body energy $e_{I}$ which is the energy of
molecule $I$ in the crystal and consists of the de-
formation energy $e_{I}^{\text {def }}$ and the polarization energy
$e_{I}^{\text {pol }}$,

$$
e_{I}=e_{I}^{\text {def }}+e_{I}^{\text {pol }}.
\tag{2}
$$

$e_{I}^{\text {def }}$ is the change in energy accompanied by the
deformation of molecule from its gas phase ge-
ometry and is easily obtained from ab initio MO
calculations. $e_{I}^{\text {pol }}$ is the deformation energy of the
electron distribution under the electrostatic po-
tential due to the surrounding molecules in the
crystal. This energy is calculated as follows:

$$
\begin{aligned}
e_{I}^{\mathrm{pol}} & =\left\langle\Psi_{I}\left|\hat{H}_{I}\left\{q_{a}\right\}\right| \Psi_{I}\right\rangle-\left\langle\Psi_{I}^{0}\left|\hat{H}_{I}\left\{q_{a}^{0}\right\}\right| \Psi_{I}^{0}\right\rangle \\
& =E_{I}-\left\langle\Psi_{I}^{0}\left|\hat{H}_{I}\left\{q_{a}^{0}\right\}\right| \Psi_{I}^{0}\right\rangle,
\end{aligned}
\tag{3}
$$

where $\Psi_{I}^{0}$ is the wavefunction of the isolated
molecule at the geometry deformed in the crystal
and is obtained from the following equation:

$$
\hat{H}_{I}^{0} \Psi_{I}^{0}=E_{I}^{0} \Psi_{I}^{0},
\tag{4}
$$

where $\hat{H}_{I}^{0}$ is the total Hamiltonian of the isolated
molecule. $\Psi_{I}$ is the wavefunction of molecule de-
formed by the environmental electrostatic poten-
tial and is obtained from the following equation:

$$
\hat{H}_{I}\left\{q_{a}\right\} \Psi_{I}=E_{I} \Psi_{I},
\tag{5}
$$

where $\hat{H}_{I}\left\{q_{a}\right\}$ is the Hamiltonian with the elec-
trostatic potential from the surrounding molecules
in the crystal,

$$
\hat{H}_{I}\left\{q_{a}\right\}=\hat{H}_{I}^{0}+\sum_{i \in I}^{N_{I}} \sum_{J \neq I} \sum_{a \in J} \frac{q_{a}}{r_{i a}},
\tag{6}
$$

where $N_{I}$ refers to the number of electrons in
the molecule $I$ and $r_{i a}$ is the separation between the
electron $i$ in the molecule $I$ and the nucleus $a$ in the
molecule $J$. In the Hamiltonian, the electrostatic
potential is approximated by using the fractional
point charge $q_{a}$: $q_{a}$ is the atomic net charge and is
calculated from the Mulliken population. $q_{a}^{0}$ in the
second term of Eq. (3) denotes the net charge of
the isolated molecule. Eq. (5) is solved repeatedly

at the HF level of theory for the asymmetric unit molecules until the Mulliken populations of all molecules within the cut-off length become self- consistent. From this calculations, many-body polarization interactions which are the major many-body effects for polar molecules [15] are taken into consideration.

Second, we describe the computational proce- dure for the two-body energy $e_{I J}$, which is simply called 'pair energy' hereafter. $e_{I J}$ is the intermolecular interaction energy between the molecules $I$ and $J$ in the crystal and is calculated as follows:
$$
e_{I J}=\left\{E_{I J}^{0}-\left(E_{I}^{0}+E_{J}^{0}\right)\right\}-\left(e_{I}^{\mathrm{pol}(J)}+e_{J}^{\mathrm{pol}(I)}\right), \quad(7)
$$
where the first term is the usual intermolecular interaction energy in gas phase ($E_{I J}^{0}$ is the energy corresponding to $E_{I}^{0}$ in Eq. (4), where the $I J$ pair is regarded as a supermolecule) and the second term corrects the energy of the pair interaction in the molecular assembly. The first term of Eq. (7) includes the polarization energy of each molecule due to the electrostatic potential of the partner molecule in the pair [16]. Since the polarization energy of a molecule in the crystal is included into the one-body terms, the polarization energy involved in the first terms should be subtracted to avoid double counting. The polarization energy of molecule $I$ in the molecular pair $I J$ $e_{I}^{\mathrm{pol}}(J)$ is estimated as follows:
$$
\begin{aligned}
e_{I}^{\mathrm{pol}(J)}= & \left\langle\Psi_{I}^{(J)}\left|\hat{H}_{I}^{(J)}\left\{q_{a}\right\}\right| \Psi_{I}^{(J)}\right\rangle \\
& -\left\langle\Psi_{I}^{0}\left|\hat{H}_{I}^{(J)}\left\{q_{a}^{0}\right\}\right| \Psi_{I}^{0}\right\rangle \\
= & E_{I}^{(J)}-\left\langle\Psi_{I}^{0}\left|\hat{H}_{I}^{(J)}\left\{q_{a}^{0}\right\}\right| \Psi_{I}^{0}\right\rangle,
\end{aligned}\qquad(8)
$$
where
$$
\hat{H}_{I}^{(J)}\left\{q_{a}\right\} \Psi_{I}^{(J)}=E_{I}^{(J)} \Psi_{I}^{(J)}, \quad(9)
$$

$$
\hat{H}_{I}^{(J)}\left\{q_{a}\right\}=\hat{H}_{I}^{0}+\sum_{i \in I}^{N_{I}} \sum_{a \in J} \frac{q_{a}}{r_{i a}}. \quad(10)
$$

The present method is regarded as a simplified version of the pair interaction MO method or the fragment MO method [20,21], which was proposed for calculating large molecular clusters and large molecules. The fragment MO method is based on a pair approximation and gives the total energies of systems with many molecules as a sum of one- body energies and two-body interaction energies, which is fitted to the lattice energy expression of the total energy of crystals. However, it is not easy to apply the fragment MO method to lattice energy calculations; the pair interaction energy under the electrostatic potential from surrounding molecules is time-consuming to calculate in case of crystals, since the number of surrounding molecules becomes very large. Therefore we made some approximations to the fragment MO method: the pair interaction energy is calculated without electrostatic potential from surrounding molecules and the polarization energy of molecules is calculated using the fractional point charges of surrounding molecules.

The electron correlation effect was estimated by the second order Møller-Plesset perturbation theory (MP2). At the MP2 level, the one-body energy is evaluated by the same equation as the HF theory (Eq. (3)) and the two-body energy is calculated by the following equation instead of Eq. (7),
$$
\begin{aligned}
e_{I J}=\left\{E_{I J}^{\mathrm{MP}}-\left(E_{I}^{\mathrm{MP}}+E_{J}^{\mathrm{MP}}\right)\right\}-\left(e_{I}^{\mathrm{pol}(J)}+e_{J}^{\mathrm{pol}(I)}\right). \\
(11)
\end{aligned}
$$

Namely, the electron correlation effect is assumed to be pairwise additive, since the many-body correlation energy is small for polar molecules [15], while $e_{I}$ is calculated at the MP2 level to include the change in the correlation energy of molecules.

The computational procedure at the HF level is summarized as follows:
(1) Generate all molecules within cut-off length by the symmetry operations associated with the space group on the asymmetric unit molecules.
(2) Calculate initial density matrices and net atomic charges of symmetrically unique molecules in the unit cell and copy their net atomic charges to the corresponding atoms of the symmetrically equivalent molecules.
(3) Solve HF equations of symmetrically unique molecules in the unit cell with electrostatic potentials from surrounding molecules (Eq. (11)). Check the convergence on the density matrices of the molecules. If they are not converged, go back to step 2.

(4) Calculate the energies of the isolated molecules which are used to evaluate the polarization energies (Eq. (3)).

(5) Solve HF equations of the dimers composed of an asymmetric unit molecule and a molecule within the cut-off length. Only the calculations on the symmetrically unique molecular pairs are sufficient. Then, calculate the polarization energy of monomers in the dimers (Eq. (8)) to obtain pair energies (Eq. (7)).

(6) Calculate the lattice energy (Eq. (1)) using the polarization energy (Eq. (3)) and the pair energies (Eq. (7)).

Now, we summarize the advantages of our method. First, the method provides the general-purpose description of the molecular interactions. The important factors such as anisotropy of interactions and many-body polarization effects are described appropriately, as well as quantum mechanical short-range interactions (exchange repulsion and charge transfer interaction). Second, the method does not require any adjustable parameters and is free from the problems associated with empirical potential functions such as arbitrariness and artificiality of the parameters. The method, therefore, is expected to be applicable to a wide variety of molecular crystals and the method was applied to several van der Waals crystals (ethylene and benzene) and hydrogen bonded crystals (hydrogen chloride and methanol). The calculated lattice constants and the lattice energies were in reasonable agreement with experiments [17].

Although our method is of practical use, a drawback is that the calculations require much computational time. It may be easy to reduce the elapsed time by using parallel processing, since the pair energies are calculated independently. So far as the methods based on the first-principles calculation are concerned, the crystal orbital method has been proposed [22–25]. This method, however, requires enormous computational time and practical calculations of equilibrium structures have been limited to one-dimensional crystals such as polymers with periodic symmetry [26].

A similar computational procedure to ours for calculating lattice energy using the ab initio MO method has been proposed by Nyburg and Faerman [12]. They calculated the two-body term of the lattice energy at the HF level with an empirical estimation of the dispersion energy, assuming that the molecular interaction in the crystal is fully pairwise additive. In this work, we improved their method on the following two points: the many-body polarization effect is taken into consideration and the electron correlation energy is evaluated by the MP2 method.

### 3. Computational details

We performed lattice energy calculations on the $\mathrm{H}_{3} \mathrm{N}-\mathrm{BF}_{3}$ crystal using the procedure described above. In the calculations, $\mathrm{BF}_{3}$ and $\mathrm{NH}_{3}$ molecules were adopted as the component molecules of the 'asymmetric unit'. $\mathrm{NH}_{3}$ and $\mathrm{BF}_{3}$ molecules were treated as rigid-bodies with $\mathrm{C}_{3 \mathrm{v}}$ symmetry: $r(\mathrm{B}-\mathrm{F})=1.3742 \AA$ and $\angle \mathrm{F}-\mathrm{B}-\mathrm{F}=110.995^{\circ}$ for $\mathrm{BF}_{3}$, and $r(\mathrm{N}-\mathrm{H})=1.0188 \AA$ and $\angle \mathrm{H}-\mathrm{N}-\mathrm{H}=$ $108.548^{\circ}$ for $\mathrm{NH}_{3}$. These geometrical parameters of the molecules were taken from the X-ray structure [18] and the equivalent bond lengths and angles were averaged. According to the experiment, the number of complexes in the unit cell was assumed to be 8 and the $Pbca$ space group symmetry was assumed [18]. In the calculation of the lattice energy (Eq. (1)), the molecules within the cut-off length of $20 \AA$ were considered. The number of molecules $\left(\mathrm{NH}_{3}\right.$ and $\left.\mathrm{BF}_{3}\right)$ within the cut-off length was 898. An error in energy brought by this cut-off was about 0.05 kcal/mol, which was estimated by directly summing up the Coulomb interaction energy up to the cut-off length of $80 \AA$.

The optimization of the packing structure of the crystal was performed at the HF/3-21G and HF/3-21 + G level using a numerical differentiation of the lattice energy (Eq. (1)) with respect to geometrical parameters. The optimized parameters were the lattice constants ($a$, $b$, and $c$), the fractional coordinates ($x$, $y$, and $z$) of the origin of the molecular coordinate system of $\mathrm{NH}_{3}$, the intermolecular distance between $\mathrm{NH}_{3}$ and $\mathrm{BF}_{3}$, and the orientation of $\mathrm{NH}_{3}$ and $\mathrm{BF}_{3}$. The lattice energy was recalculated at the $\mathrm{MP2/6-311+G^{*}}$ level at the HF/3-21 + G optimized structure. In this lattice energy calculation, the $\mathrm{H}_{3} \mathrm{N}-\mathrm{BF}_{3}$ complex was

treated as an asymmetric unit molecule, in order to compare the calculated lattice energy with the corresponding experiment.

All calculations were performed with our original program which is based on the GAUSSIAN 94 program package [27] for ab initio MO calculations.

## 4. Results and discussion

The optimized lattice constants are shown in Table 1. The lattice constants ($a$, $b$, and $c$) obtained with the 3-21G basis set were in poor agreement with the experiment: the parameter $b$ was significantly underestimated. On the other hand, the 3-21 + G basis set reproduced the experimental results reasonably, though the lattice constants were underestimated by 1.6–3.0%. Due to unbalanced underestimation, $a$ is slightly shorter than $b$, which is not in accord with the experimentally observed order, $b < a < c$. The experimentally observed difference between $a$ and $b$ is only 0.11 Å and such precision is difficult to be achieved by the calculations of packing structures of molecular crystals at present. It is satisfactory to reproduce experimental lattice constants within several percent errors.

It is known, in the series of related increvalent complexes with the B–N dative bond, that the B–N bond shrinks in the crystals [13]. The observed B–N bond length, $r(\text{B–N}) = 1.60$ Å, in the $\text{H}_3\text{N–BF}_3$ crystal is 0.07 Å shorter than that in gas phase [18,28]. The HF/3-21 + G calculation gave the B–N bond length of 1.51 Å which was 0.13 Å shorter than the optimized length of the free complex at the same level of theory. Thus, our calculation reproduced the same tendency as the experiment, though the calculated B–N length was somewhat short and the bond shrinking was overestimated. Since the B–N bond shrinking in the crystal was not observed when the polarization interaction was not included in the calculations, it is said that the B–N bond shrinking is caused by the polarization interaction. This also suggests that the present method with the 3-21 + G basis set overestimates the polarization interaction and results in the overestimate of the bond shrinking.

The calculated complex with the shorter B–N length than the real one was consistent with the underestimated lattice constants described above. Thus, our method gave a reasonable packing structure of the EDA crystal, though a better wavefunction may be needed for a quantitative description of the crystal.

The calculated lattice energy is shown in Table 2. Both the HF/3-21 + G and the MP2/6-311 + G* calculations gave the similar lattice energies: –33.0 and –30.8 kcal/mol, respectively. There are no available experimental data to be directly compared with the calculated lattice energy. However, the experimental heat of sublimation ($\text{H}_3\text{N–BF}_3$ (s) $\rightarrow \text{NH}_3(\text{g}) + \text{BF}_3(\text{g})$) has been reported to be 42 kcal/mol [19], and the dissociation energy of $\text{H}_3\text{N–BF}_3$ was estimated to be 23.0 kcal/mol from MP2/TZ2P calculations [28]. By using this disso-

Table 1
Calculated lattice constants and B–N bond length for $\text{H}_3\text{N–BF}_3$ crystal$^{\text{a}}$

| | Expt$^{\text{b}}$ | HF/3-21G | HF/3-21 + G |
| --- | --- | --- | --- |
| $a$ (Å) | 8.22 | 8.03 (–0.19) | 7.97 (–0.25) |
| $b$ (Å) | 8.11 | 7.54 (–0.57) | 7.98 (–0.13) |
| $c$ (Å) | 9.31 | 9.04 (–0.27) | 9.14 (–0.17) |
| $r(\text{B–N})$ (Å) | 1.60 | 1.56 (–0.05) | 1.51 (–0.09) |

$^{\text{a}}$The differences from the experimental values are given in parentheses.
$^{\text{b}}$Ref. [17].

<table>
<caption>Table 2<br>Calculated lattice energy and pair energies of $\text{H}_3\text{N–BF}_3$ crystal$^{\text{a}}$</caption>
<thead>
<tr>
<th></th>
<th>HF/3-21 + G</th>
<th>MP2/6-311+G*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lattice energy</td>
<td>–33.0</td>
<td>–30.8</td>
</tr>
<tr>
<td>Polarization energy</td>
<td>–3.3</td>
<td>–3.7</td>
</tr>
<tr>
<td>Deformation energy</td>
<td>4.5</td>
<td>3.8</td>
</tr>
<tr>
<td>Pair energy$^{\text{b}}$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>(1)–(2)</td>
<td>–17.8</td>
<td>–16.0</td>
</tr>
<tr>
<td>(1)–(3)</td>
<td>–8.4</td>
<td>–7.3</td>
</tr>
<tr>
<td>(1)–(4)</td>
<td>–4.3</td>
<td>–4.3</td>
</tr>
<tr>
<td>(1)–(5)</td>
<td>–4.2</td>
<td>–3.9</td>
</tr>
<tr>
<td>(1)–(6)</td>
<td>–6.3</td>
<td>–5.2</td>
</tr>
<tr>
<td>(1)–(7)</td>
<td>–4.8</td>
<td>–3.9</td>
</tr>
<tr>
<td>(1)–(8)</td>
<td>–0.7</td>
<td>–0.9</td>
</tr>
</tbody>
</table>

$^{\text{a}}$All energies are given in kcal/mol. A negative value shows stabilization.
$^{\text{b}}$Pair energy $e_{IJ}$ is calculated by Eq. (7) or Eq. (11). See Fig. 1 for the indices of complex pairs.

ciation energy and the lattice energy calculated at the MP2/6-311+G* level, the heat of sublimation without the correction of the zero-point energy (ZPE) is obtained to be 53.8 kcal/mol which is 11.8 kcal/mol larger than the experimental value. Al- though the evaluation of ZPE of solids is beyond this work, the calculated energy is reduced to some extent by the ZPE correction. The discrepancy, however, seems too large to be compensated by the ZPE correction. In the experiment, the $H_{3}N-BF_{3}$ complex was assumed to be completely dissociated in gas phase. However, this complex has only re- cently been detected in gas phase [29]. If a few complexes existed in gas phase, the measurement might underestimate the heat of sublimation. Thus, it is very difficult to estimate the accuracy of the calculated lattice energy at present. The quantitative comparison between the experimental and the theoretical values should be made in future work.

In Table 2, the pair energies $e_{IJ}$ calculated by Eq. (7) and (11), for the main complex pairs in the crystal are shown. The index of $H_{3}N-BF_{3}$ complex defined in Fig. 1 is used to specify the pair of the complex. From the comparison of the results from the two computational levels, one notices that the HF/3-21+G energies are close to the MP2/6-311+G* energies for all pairs. This indicates that the calculation at the HF/3-21+G level rea- sonably describes the interaction energies of the dimers in this crystal.

Now, let us look at the pair interactions be- tween the complexes together with their geome- tries. The important geometrical parameters of the representative complex pairs are shown in Fig. 2. There is a prominently stable complex pair, the (1)-(2) pair (Table 2 and Fig. 2). This dimer is considerably stabilized by an anti-parallel dipole- dipole interaction in addition to two $N-H\cdots F$ hydrogen bonds. The second most stable (1)-(3) pair is stabilized through a bifurcated hydrogen bonding between a fluorine atom of one complex and two hydrogen atoms of another complex, and the less stable (1)-(4) pair is stabilized by a $N-H\cdots F$ hydrogen bond between the $H_{3}N-BF_{3}$ complexes.

The stable complex pairs form the complex tetramer which consists of complexes (1)-(4). The sum of the pair energies between the complex (1) and other three complexes in the tetramer

![](./images/812419784216936449_4.jpg)

Fig. 1. The indices of the $H_{3}N-BF_{3}$ complexes in the crystal. The left-hand and the right-hand figures are at $a=0$ and $a=1/2$, respectively. The complex (1) is the 'asymmetric unit'. The complex (1) is drawn with broken lines in the right-hand figure for making clear the relative positions of complexes.

![](./images/812419784216936449_5.jpg)

Fig. 2. Some representative complex pairs in the $\text{H}_3\text{N-BF}_3$ crystal: (a) the (1)-(2) pair (top view), (b) the (1)-(2) pair (side view), (c) the (1)-(3) pair, and (d) the (1)-(4) pair. The length and angle are in $\bullet$ and degrees, respectively.

becomes $-27.6$ kcal/mol at the MP2/6-311+G* level (Table 2). This energy accounts for a large part of the lattice energy. The (3)-(4) pair is equivalent to the (1)-(2) pair and their interaction energies are the same. In this tetramer, the anti-parallel complex dimer (APCD) (1)-(2) bridges two complexes in another anti-parallel dimer (3)-(4) through the (1)-(3) and (1)-(4) interactions. In this manner, the tight anti-parallel dimer is further stabilized through these bridging interactions. This tetramer is regarded as a building block of the crystal.

From the pair energy analysis, a 'basic structure' with $C_i$ symmetry was extracted (Fig. 3). The features of the packing structure can be well understood on the basis of this structure. The basic structure consists of the four anti-parallel complex dimers: APCD1 to APCD4 framed in Fig. 3. APCD1 bridges the two complexes in APCD2 to make APCD1-APCD2 connection. The same connections are also seen in APCD2-APCD3, APCD3-APCD4, and APCD4-APCD1. The bridged APCDs extend in two dimensions to form a layer. Within this layer, the relative configuration of the neighboring APCDs is restricted around the center of symmetry by the cyclic connection in the basic structure. Furthermore, there is a glide plane at $a=1/4$ in this crystal and the layers are stacked along the $a$-axis. In this stacking structure, the (1)-(5), the (1)-(6), and the (1)-(7) complex pairs, which were not discussed in detail, can be regarded as the interface between the two adjacent layers from the viewpoint of the pair interaction.

In conclusion, the $\text{H}_3\text{N-BF}_3$ crystal is constructed as a hierarchical structure with five levels: the molecules ($\text{NH}_3$ or $\text{BF}_3$), the $\text{H}_3\text{N-BF}_3$ complex, APCD, the two-dimensional layer with the bridged APCDs, and the stacked layers (whole crystal).

![](./images/812419784216936449_6.jpg)

Fig. 3. 'Basic structure' of the $\text{H}_3\text{N-BF}_3$ crystal with $C_i$ symmetry. The framed parts represent the anti-parallel $\text{H}_3\text{N-BF}_3$ complex dimers (APCDs). The broken lines show hydrogen bonds. The circle on the $c$-axis represents a center of symmetry in the crystal.

## 5. Summary

We have proposed a computational procedure to calculate the lattice energy using the ab initio MO method. The method was applied to $\text{H}_3\text{N-BF}_3$ crystal which was never calculated with force fields. The calculated lattice constants and the packing structure were in reasonable agreement with the experiment, even though this system contains various kinds of molecular interactions such as dative bonds, hydrogen bonds and electrostatic interactions. For a better description of the crystals, however, a higher level of MO calculations than HF/3-21+G which was employed in the optimization of the packing structure in this work may be needed together with a scheme for correcting the basis set superposition error which may affect the packing structure to some extent.

## Acknowledgements

The work was supported in part by ACT-JST. The numerical calculations were partially carried out at the Computer Center of the Institute for Molecular Science.

## References

[1] J. Maddox, Nature 335 (1988) 201.
[2] A. Gavezzotti, Acc. Chem. Res. 27 (1994) 309.
[3] A.J. Pertsin, A.I. Kitaigorodsky, The Atom-Atom Potential Method: Applications to Organic Molecular Solids, Springer, New York, 1987.
[4] J. Pillardy, R.J. Wawak, Y.A. Arnautova, C. Czaplewski, H.A. Scheraga, J. Am. Chem. Soc. 122 (2000) 907.
[5] D. Gao, D.E. Williams, Acta Cryst. A 55 (1999) 621.
[6] I. Nobeli, S.L. Price, J. Phys. Chem. A 103 (1999) 6448.
[7] S.L. Price, J. Chem. Soc., Faraday Trans. 92 (1996) 2997.
[8] B.S. Potter, R.A. Palmer, R. Withnall, B.Z. Chowdhry, S.L. Price, J. Mol. Struct. 485 (1999) 349.
[9] D.C. Sorescu, D.L. Thompson, J. Phys. Chem. B 101 (1997) 3605.
[10] D.E. Williams, J.-M. Yan, Adv. Atomic Mol. Phys. 23 (1987) 87.
[11] A.D. Buckingham, P.W. Fowler, J.M. Hutson, Chem. Rev. 88 (1988) 963.
[12] S.C. Nyburg, C.H. Faerman, Mol. Phys. 67 (1989) 447.
[13] M.A. Dvorak, R.S. Ford, R.D. Suenram, F.J. Lovas, K.R. Leopold, J. Am. Chem. Soc. 114 (1992) 108.

[14] V. Jonas, G. Frenking, J. Chem. Soc., Chem. Commun. (1994) R1489.

[15] M.J. Rlrod, R.J. Saykally, Chem. Rev. 94 (1994) 1975.

[16] K. Kitaura, K. Morokuma, Int. J. Quantum Chem. 10 (1976) 325.

[17] To be published.

[18] J.L. Hoard, S. Geller, W.M. Cashin, Acta Cryst. 4 (1951) 396.

[19] J.L. Hoard, S. Geller, T.B. Owen, Acta Cryst. 4 (1951) 405.

[20] K. Kitaura, T. Sawai, T. Asada, T. Nakano, M. Uebayasi, Chem. Phys. Lett. 312 (1999) 319.

[21] K. Kitaura, E. Ikeo, T. Asada, T. Nakano, M. Uebayasi, Chem. Phys. Lett. 313 (1999) 701.

[22] H. Teramae, K. Takeda, J. Am. Chem. Soc. 111 (1989) 1281.

[23] H. Teramae, J. Chem. Phys. 85 (1986) 990.

[24] S. Hirata, S. Iwata, J. Chem. Phys. 108 (1998) 7901.

[25] S. Hirata, H. Torii, M. Tasumi, Phys. Rev. B 57 (1998) 11994.

[26] H. Teramae, J. Chem. Software 4 (1998) 73.

[27] M.J. Frisch et al., GAUSSIAN 94, Revision D.4, Gaussian Inc., Pittsburgh, PA, 1995.

[28] D. Fujiang, P.W. Fowler, A.C. Legon, J. Chem. Soc., Chem. Commun. (1995) 113.

[29] A.C. Legon, H.E. Warner, J. Chem. Soc., Chem. Commun. (1991) 1397.