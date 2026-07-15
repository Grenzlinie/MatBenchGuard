# Structural, electronic properties and stability of the $(1 \times 1)$ PbTiO₃ $(1\ 1\ 1)$ polar surfaces by first-principles calculations

Qing Pang $^{a}$, Jian-Min Zhang $^{a,*}$, Ke-Wei Xu $^{b}$, Vincent Ji $^{c}$

$^{a}$ College of Physics and Information Technology, Shaanxi Normal University, Xian 710062, Shaanxi, PR China
$^{b}$ State Key Laboratory for Mechanical Behavior of Materials, Xian Jiaotong University, Xian 710049, Shaanxi, PR China
$^{c}$ ICMMO/LEMHE UMR CNRS 8182, Université Paris-Sud 11, 91405 Orsay Cedex, France

---

## ARTICLE INFO

**Article history:**
Received 26 August 2008
Received in revised form 10 May 2009
Accepted 18 May 2009
Available online 22 May 2009

**Keywords:**
PbTiO₃ surface
Relaxation
Electronic structure
Stability
First-principles

---

## ABSTRACT

Under GGA, the structural, electronic properties and stabilities of four different $(1 \times 1)$ terminations of cubic PbTiO₃ $(1\ 1\ 1)$ surface, the directly cleaved $(1\ 1\ 1)$-Ti and $(1\ 1\ 1)$-PbO₃ terminations and the constructed $(1\ 1\ 1)$-TiO and $(1\ 1\ 1)$-PbO₂ ones, have been systematically studied by using projector-augmented wave method implemented in VASP. For $(1\ 1\ 1)$-Ti and $(1\ 1\ 1)$-PbO₃ terminations, Ti–O bonds between the outermost two layers are enhanced after relaxation, while those between the second and the third layers are weakened. In addition, a contraction of O–O distance in surface PbO₃ layer is also found for $(1\ 1\ 1)$-PbO₃ termination. Moreover, electronic structures of both $(1\ 1\ 1)$-Ti and $(1\ 1\ 1)$-PbO₂ terminations are significantly influenced by structure relaxations, and the effects of the surface on the DOS are dominantly on the Ti layers, especially the CB. For a constructed $(1\ 1\ 1)$-TiO termination, the relaxation results show both Ti–O bonds between the outermost two layers and those between the second PbO₃ layer and the third Ti layers are enhanced. For a constructed $(1\ 1\ 1)$-PbO₂ termination, Ti–O bonds between the outermost two layers are also enhanced as in the $(1\ 1\ 1)$-TiO termination, however, inequivalent Ti–O bonds between the second layer Ti atom and the third layer O atoms are found, with two bonds expanding and the other one contracting. Results of electronic structure calculations show these two constructed terminations are all insulating and changes of DOS originate dominantly from modifications of surface compositions. Furthermore, it is found that for all four different $(1\ 1\ 1)$ terminations, the movements of the cation and/or anion on the outermost layer along the surface normal direction after relaxation all result in a reduction of the space electric field. In O and Pb external environments, it is predicted that $(1\ 1\ 1)$-PbO₂ termination is the most stable one in O- and Pb-rich environments, however, the $(1\ 1\ 1)$-Ti termination is stable one in O- and Pb-poor conditions. The $(1\ 1\ 1)$-TiO termination also shows a stability domain in moderate O and Pb environments.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

ABO₃ perovskite thin films are intensively investigated due to their importance for many technological applications, including photo-catalysis, high temperature oxygen sensors, substrates for epitaxial growth of high-$T_{c}$ superconducting thin films, non-volatile memory cells, electro-optical materials, dielectric materials and piezoelectrical devices [1–7]. Lead titanate (PbTiO₃) is one of the simplest and most important members in ABO₃ perovskite family possessing of a high Curie temperature of $493\ ^{\circ}\text{C}$ and a high spontaneous polarization of $75\ \mu\text{C/cm}^{2}$ [8]. Due to large electro-optic coefficient and high photorefractive sensitivity, it can be used as an optical sensor [9]. In addition, it is a good starting point for understanding ferroelectricity and other properties because of the simplest structures and a clearly established single phase transition at $T_{c} \approx 763\ \text{K}$ from a paraelectric cubic phase (Pm3m) to a ferroelectric tetragonal phase (P4mm) [10]. Similar as other perovskite compounds, its ferroelectricity also arises from a delicate balance between short-range forces favoring the undistorted cubic paraelectric structure on the one hand, and long-range Coulomb interactions favoring a ferroelectric distortion on the other hand [6,7]. Extensive investigations on its electronic structure indicate that Pb–O and Ti–O covalent bonding weaken the short-range repulsions and give rise to the ferroelectric distortion [11,12]. Furthermore, the cubic PbTiO₃ is subject to several competing structural instabilities, which can give rich phase diagrams with structures ranging from polar ferroelectric to non-polar antiferrodistortive (AFD), and such structural instabilities and the associated properties can be increased or suppressed by the presence of a surface [1,13,14].

Different from the bulk, the thin films materials have relatively larger surface and interface thus investigating how the structure

---

* Corresponding author. Tel.: +86 29 85308456.
E-mail address: jianm_zhang@yahoo.com (J.-M. Zhang).

0169-4332/$ – see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.apsusc.2009.05.032

and electronic properties are affected by the surface or interface is of primary importance. As a result of the rapidly increasing use of thin film in devices and their progressive miniaturization, the effects of surfaces on structural phase transitions and functional properties have become an issue of significant practical as well as fundamental interest. Motivated by these, though many first-principles calculations have been carried out to investigate the atomic structures and electronic properties of $ABO_3$-type perovskite surfaces, and the results are in good agreement with available experimental observations [15-24], the properties of the polar orientation surface are much less known. Due to potentially interesting applications of polar perovskite surfaces, such as their high surface reactivity for epitaxial growth metal-ceramic functional materials, the enhanced understanding of these surfaces is necessary. In this paper, we present first-principles calculations on the polar (1 1 1) surfaces of cubic $PbTiO_3$ with both unrestructured and restructured terminations. To our knowledge, no theoretical research is reported about this direction. It is expected that this systematic calculation is of high interest in relation to understanding the structure and electronic properties as well as surface thermodynamic stability of $PbTiO_3$ polar surfaces, and we hope our results will give a clue for the application of preparing various surfaces.

The paper is organized as follows. In the second section, the calculation methods and the four different structure models of $PbTiO_3$ (1 1 1) surface are described in detail. Our calculation results of surface atomic geometries, the electronic structures (such as band structures, the density of states and the charge density distribution), as well as a discussion about surface dangling bonds and the surface charge, are in Section 3. The surface thermodynamic stability of $PbTiO_3$ (1 1 1) surface is discussed in Section 4. The conclusions are given in the last section.

## 2. Method and structure models

The calculations were carried out using the Vienna ab initio simulation package (VASP) based on density functional theory with projector-augmented wave (PAW) pseudopotential method [25-28]. The exchange and correlation energy was treated via the generalized gradient approximation (GGA) using the Perdew-Burke-Ernzerhof formulation [29]. A conjugate-gradient algorithm was used to relax the ions into their groundstates, and the energies and the forces on each ion were converged within $1.0 \times 10^{-6}$ eV/atom and 0.02 eV/Å respectively. The Kohn-Sham orbitals were expanded by a plane wave basis set and an energy cutoff of 400 eV was used throughout. Pb 6s and 6p, Ti 3d and 4s, and O 2s and 2p orbitals were regarded as valence orbitals, thus 26 electrons were adopted as valence electrons in one bulk unit cell. The surfaces were described in the framework of the slab model and an $11 \times 11 \times 1$ grid in the Brillouin zone as proposed by Monkhorst and Pack [30] was used for the slab structure. A Gaussian broadening of 0.05 eV was chosen and all values were obtained at 0 K.

Before starting the surface calculation, an $11 \times 11 \times 11$ grid was adopted for optimization of the bulk phase calculation, and the obtained lattice constant of 3.968 Å is in good agreement with experimental value of 3.97 Å. This theoretical lattice constant is used in following surface calculations.

Different from the (1 0 0) cleavage of cubic $PbTiO_3$, which naturally gives non-polar PbO and $TiO_2$ terminations, a cleavage of $PbTiO_3$ to create (1 1 1) surfaces leads to the formation of polar surfaces, that means the stacking of the crystal along the [1 1 1] direction consists of alternating planes of Ti and $PbO_3$ units (shown in Fig. 1) having formal charges of +4 and -4 respectively, assuming $O^{2-}$, $Ti^{4+}$, and $Pb^{2+}$ constituents. Such a sequence of atomic layers of Ti and $PbO_3$ stoichiometry gives rise to a monotonic raised microscopic electric field, which has to be compensated through either an anomalous filling of the surface electronic states or a modification of the surface composition. The former method indicates crucial variations of the electronic structure of the surfaces that should be detected by experiments, while the latter will lead to non-stoichiometric terminations. Therefore, in this paper, special attention is paid to two main classes of terminations with odd number of (1 1 1) planes: the stoichiometric (1 1 1)-Ti and (1 1 1)-$PbO_3$ terminations on one hand, and the constructed non-stoichiometric (1 1 1)-TiO and (1 1 1)-$PbO_2$ ones on the other hand.

The side views of the four different $(1 \times 1)$ slab models of the $PbTiO_3$ (1 1 1) surface are shown in Fig. 2, (a) (1 1 1)-Ti termination with thirteen atomic layers, (b) (1 1 1)-$PbO_3$ termination with thirteen atomic layers, (c) (1 1 1)-TiO termination with nine atomic layers and (d) (1 1 1)-$PbO_2$ termination with nine atomic layers. Each slab is separated by a vacuum region of 12 Å. During the surface structure optimization, all atoms were fully relaxed.

## 3. Atomic and electronic structures

### 3.1. (1 1 1)-Ti and (1 1 1)-$PbO_3$ terminations

In bulk $PbTiO_3$, the Ti atom is in the center of an octahedron constructed by six O atoms nearby, while the O atom is bound by two Ti neighbors. However, when a cleavage perpendicular to [1 1 1] direction happens to create the (1 1 1) surfaces, three out of six Ti-O bonds are broken. In a (1 1 1)-Ti termination, the surface Ti

![](./images/811850816104169472_1.jpg)

Fig. 1. Schematic configuration of the stacking sequence of $PbTiO_3$ (1 1 1) layers.

![](./images/811850816104169472_2.jpg)

Fig. 2. Side views of the four different slab models of the $PbTiO_3$ (1 1 1) surface: (a) (1 1 1)-Ti termination, (b) (1 1 1)-$PbO_3$ termination, (c) (1 1 1)-TiO termination and (d) (1 1 1)-$PbO_2$ termination. The (1 1 1) surface is at the top of the figure.

atom misses three of its six O neighbors with respect to that in the bulk, and correspondingly, in a (1 1 1)-$PbO_3$ termination, the surface O atom is only bound by a single Ti atom below.

The relaxations of (1 1 1)-Ti and (1 1 1)-$PbO_3$ terminations have been calculated, and the results show that metallic atoms Ti and Pb in the slab only move along the direction of surface normal, however, relaxations of O atoms are complicated, not only along the surface normal but also in $PbO_3$ plane of the slab. A spontaneous breaking of original symmetry takes place, by which the Ti-O bonds between the outermost two layers are reinforced and those between the second and the third layers are weakened. In addition, the O-O bonds in the surface $PbO_3$ layer of (1 1 1)-$PbO_3$ termination are also reinforced. Relaxation effects propagate into the slab and modify the structure and energy of inner layers, especially for (1 1 1)-$PbO_3$ slab. In the (1 1 1)-Ti slab, the Ti-O bond of the outermost two layers is contracted by about 9.14% and that between the second and the third layers is expanded by about 2.17%. In the (1 1 1)-$PbO_3$ slab, the contraction and the expansion values are 2.26% and 1.84% respectively.

The atomic displacements along the direction of surface normal for the two terminations are listed in Table 1 together with results of interlayer relaxations. We can see that in (1 1 1)-Ti slab, Ti atoms on the outermost layer move 0.253 Å inward in the slab, which leads to a large contraction of interlayer distance between the outermost two layers ($\Delta d_{12}=-29.66\%$). On the second $PbO_3$ layer, the inward displacement 0.249 Å of Pb atom and outward displacement 0.199 Å of O atom together result in a very large rumpling of 0.448 Å. In addition, although a large rumpling of 0.356 Å is also found between the Pb and O atoms in the fourth $PbO_3$ layer, it is decreased in the deeper $PbO_3$ layers. Moreover, a damped relaxation behavior is found in Ti layers, that is, the displacement value of Ti atom becomes smaller as penetrating into the slab. Finally, we can clearly see that the interlayer relaxation between the sixth $PbO_3$ layer and the central Ti layer is only $-0.13\%$ thus can be negligible. In (1 1 1)-$PbO_3$ slab, very large contraction of interlayer distance between the outermost two layers ($\Delta d_{12}=-18.85\%$) is also found, which is dominantly resulted from the relaxation of the second layer Ti atoms, because Pb and O atoms on the outermost layer all move inward with relative smaller values. In addition, very small interlayer relaxations $\Delta d_{23}=+0.09\%$ and $\Delta d_{45}=-0.38\%$ are found, however, that between the third $PbO_3$ and fourth Ti layers is very large ($\Delta d_{34}=+12.52\%$), even in deeper layers (for instance, it also remains an expansion of 1.91% between the sixth Ti layer and the central $PbO_3$ layer). Moreover, the displacements of the Ti atoms do not show a damped behavior as those in (1 1 1)-Ti termination. Compared with the small rumpling 0.08 Å of the outermost $PbO_3$ layer, rumplings of both the third and the fifth $PbO_3$ layers are much larger, with values 0.703 Å and 0.238 Å respectively, which is also different from the decreased rumpling behavior found in (1 1 1)-Ti termination.

Table 1
The atomic displacement along surface normal and the interlayer relaxation ($\Delta d_{ij}$) for (1 1 1)-Ti and (1 1 1)-$PbO_3$ terminations. The mean positions of the $PbO_3$ layers are calculated by averaging the normal coordinates of the corresponding atoms. Minus (-) indicates inward direction in the slab or contraction of interlayer distance, while plus (+) indicates outward direction in the slab or expansion of interlayer distance.

<table>
<thead>
<tr>
<th colspan="3">Ti-termination</th>
<th colspan="3">$PbO_3$-termination</th>
</tr>
<tr>
<th>Layer</th>
<th>Atomic displacements (Å)</th>
<th>$\Delta d_{ij}$</th>
<th>Layer</th>
<th>Atomic displacements (Å)</th>
<th>$\Delta d_{ij}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ti</td>
<td>Ti (-0.253)</td>
<td>−29.66%</td>
<td>$PbO_3$</td>
<td>Pb (-0.063) $O_3$ (-0.071)</td>
<td>−18.85%</td>
</tr>
<tr>
<td>$PbO_3$</td>
<td>Pb (-0.249) $O_3$ (+0.199)</td>
<td>+1.55%</td>
<td>Ti</td>
<td>Ti (+0.147)</td>
<td>+0.09%</td>
</tr>
<tr>
<td>Ti</td>
<td>Ti (+0.069)</td>
<td>+1.47%</td>
<td>$PbO_3$</td>
<td>Pb (+0.673) $O_3$ (-0.030)</td>
<td>+12.52%</td>
</tr>
<tr>
<td>$PbO_3$</td>
<td>Pb (-0.215) $O_3$ (+0.141)</td>
<td>+2.21%</td>
<td>Ti</td>
<td>Ti (+0.003)</td>
<td>−0.38%</td>
</tr>
<tr>
<td>Ti</td>
<td>Ti (+0.027)</td>
<td>+2.46%</td>
<td>$PbO_3$</td>
<td>Pb (+0.185) $O_3$ (-0.053)</td>
<td>−1.29%</td>
</tr>
<tr>
<td>$PbO_3$</td>
<td>Pb (-0.111) $O_3$ (+0.035)</td>
<td>−0.13%</td>
<td>Ti</td>
<td>Ti (+0.022)</td>
<td>+1.91%</td>
</tr>
<tr>
<td>Ti</td>
<td>No displacement</td>
<td></td>
<td>$PbO_3$</td>
<td>No displacement</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/811850816104169472_3.jpg)

Fig. 3. Calculated electronic band structures along high symmetric points in Brillouin zone. (a) Unrelaxed (1 1 1)-Ti termination, (b) relaxed (1 1 1)-Ti termination, (c) unrelaxed (1 1 1)-PbO₃ termination, and (d) relaxed (1 1 1)-PbO₃ termination. The Fermi level is set to zero with dashed lines for all cases. [G(0,0,0); F(0,0.5,0); Q(0,0.5,0.5); Z(0, 0, 0.5); B(0.5, 0, 0)].

The calculated band structures along high symmetric points in Brillouin zone are shown in Fig. 3 for (a) unrelaxed and (b) relaxed (1 1 1)-Ti terminations, and (c) unrelaxed and (d) relaxed (1 1 1)-PbO₃ terminations. Comparing the band structures of both unrelaxed and relaxed of each termination, we know that a broadening in band gap and thus an increasing in insulating property are observed for both (1 1 1)-Ti and (1 1 1)-PbO₃ terminations after relaxation. However, for (1 1 1)-Ti termination it is resulted from a downward shift of the valence band (VB), on the contrary, for (1 1 1)-PbO₃ termination it is due to an upward shift of the conduction band (CB). Therefore, electronic structures of both terminations are significantly influenced by the structure relaxations.

In order to distinguish the surface states and analyze the surface electronic structure in detail, we plot the densities of states (DOS) of each layer for the relaxed (1 1 1)-Ti and (1 1 1)-PbO₃ terminations in Fig. 4(a) and (b) respectively, and the seventh layer is the central layer that can be regarded as in the bulk. From Fig. 4(a), we can see that, in (1 1 1)-Ti slab the DOS curve of the first Ti layer shows noticeable differences with respect to that of the central Ti layer, with an enhancement at high energy region of VB on the one hand and a decrement at high energy region of CB on the other hand. For the third, the fifth and the central seventh Ti layers, the obvious modifications take place only in the CB, that is the DOS of the high energy region increases while that of the low energy part decreases, successively. However, a similar DOS curve is obtained for the second, the fourth and the sixth Ti layers. From Fig. 4(b), we can see that, in (1 1 1)-PbO₃ slab the DOS in the low energy region of the VB on the first PbO₃ layer is lower than that on the other three PbO₃ layers. In addition, the DOS at top of the VB is slightly higher in the first and the third PbO₃ layers. Compared with the fourth and the sixth Ti layers, the second Ti layer has a lower DOS at the low energy region of the VB and a narrower and lower DOS peak of CB. Comparing Fig. 4(a) and (b), we know that for both (1 1 1)-Ti and (1 1 1)-PbO₃ terminations, the effects of the surface on the DOS are dominant on the Ti layers, especially the CB.

### 3.2. (1 1 1)-TiO and (1 1 1)-PbO₂ terminations

In order to reduce the surface formal charge, the (1 1 1)-TiO and (1 1 1)-PbO₂ terminations are constructed. The former can be obtained from (1 1 1)-Ti termination by adsorbing an additional O atom on top site of the surface Ti atom so that a new Ti-O bond is formed. The latter can be derived from (1 1 1)-PbO₃ termination by removing an O atom away from the surface PbO₃ layer, as a result, one more Ti-O bond is broken and a stronger breaking of the original symmetry thus happens which may give rise to a complicated relaxation phenomenon.

The relaxation results of (1 1 1)-TiO termination also show that metallic atoms only move along the direction of surface normal as those in the two stoichiometric terminations considered above. However, in (1 1 1)-PbO₂ slab, two types of metallic atoms Ti and Pb move not only along surface normal, but also in Ti and PbO₃ planes respectively. Moreover, in (1 1 1)-TiO slab, the Ti-O bond of 1.685 Å between the first layer Ti and the adatom O is much shorter and stronger than that of 1.984 Å in the bulk. Three equivalent Ti-O bonds between the first layer Ti atom and the second layer O atoms contract by about 3.53%, and those between the second layer O atoms and the third layer Ti atom also contract by a relative large value of 5.29%. In (1 1 1)-PbO₂ slab, the remaining two Ti-O bonds

![](./images/811850816104169472_4.jpg)

Fig. 4. DOS decomposed into each layer for (a) (1 1 1)-Ti and (b) (1 1 1)-PbO₃ terminations. Individual states are broadened with the width of 0.05 eV and Fermi level is set to zero with dashed line.

between the outermost two layers atoms are reinforced, with contraction value of 7.93%. Moreover, due to a complex movement of the third layer O atoms (see next paragraph), inequivalent Ti–O bonds between the second layer Ti atom and the third layer O atoms are found, that is, two bonds expand by about 7.77% and the other one contracts by about 8.10%.

Table 2 gives atomic displacements along direction of the surface normal and interlayer relaxations of the two constructed terminations. It is noted that in (1 1 1)-TiO slab, the displacement of the surface layer Ti atom is 0.162 Å inward, however, that of the third layer Ti atom is 0.157 Å outward. Although a large relaxation of interlayer distance between the outermost two layers ($\Delta d_{12}=-9.56\%$) is found, stronger ones ($\Delta d_{23}=-18.39\%$ and $\Delta d_{34}=+15.32\%$) are also found for the interlayer distances beneath. In addition, rumplings of the second and the fourth layer PbO₃ are 0.277 Å and 0.160 Å respectively, and interlayer distance between the central Ti layer and its adjacent PbO₃ layer contracts by about 1.57%. In (1 1 1)-PbO₂ slab, a rumpling about 0.152 Å in the first PbO₂ layer and an inward displacement of the second layer Ti atom are found. More complicated rumpling phenomenon appears in the third PbO₃ layer: two O atoms move outward, while the other one moves inward, thus this PbO₃ layer is split into two O-sublayers and one central Pb-sublayer, and large interlayer relaxations ($\Delta d_{23}=+7.44\%$ and $\Delta d_{34}=+3.25\%$) around this PbO₃ layer are obtained. In addition, we can see very small displacement of Ti atom on the fourth Ti layer and a negligible expansion of interlayer distance between the fourth Ti and the central PbO₃ layers.

Comparing Tables 1 and 2, it is found that for all four different (1 1 1) terminations, the movements of the cation and/or anion on the outermost layer along the surface normal direction after relaxation all result in a reduction of the space electric field. For the (1 1 1)-Ti termination, the space electric field is dominantly from a positive formal charge of +4 contributed by first layer Ti atom. Due

Table 2
Same as Table 1 but for the (1 1 1)-TiO and (1 1 1)-PbO₂ terminations with nine layers.

<table>
<tbody>
<tr>
<td colspan="3">TiO-termination</td>
<td colspan="3">PbO₂-termination</td>
</tr>
<tr>
<td>Layer</td>
<td>Atomic displacements (Å)</td>
<td>$\Delta d_{ij}$</td>
<td>Layer</td>
<td>Atomic displacements (Å)</td>
<td>$\Delta d_{ij}$</td>
</tr>
<tr>
<td>TiO</td>
<td>Ti (−0.162)</td>
<td>−9.56%</td>
<td>PbO₂</td>
<td>Pb (+0.038) O₂ (−0.114)</td>
<td>−1.59%</td>
</tr>
<tr>
<td>PbO₃</td>
<td>Pb (−0.261) O₃ (+0.016)</td>
<td>−18.39%</td>
<td>Ti</td>
<td>Ti (−0.045)</td>
<td>+7.44%</td>
</tr>
<tr>
<td>Ti</td>
<td>Ti (+0.157)</td>
<td>+15.32%</td>
<td>PbO₃</td>
<td>Pb (+0.047) O₂ (+0.175) O₁ (−0.236)</td>
<td>+3.25%</td>
</tr>
<tr>
<td>PbO₃</td>
<td>Pb (−0.138) O₃ (+0.022)</td>
<td>−1.57%</td>
<td>Ti</td>
<td>Ti (+0.003)</td>
<td>+0.27%</td>
</tr>
<tr>
<td>Ti</td>
<td>No displacement</td>
<td></td>
<td>PbO₃</td>
<td>No displacement</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/811850816104169472_5.jpg)

Fig. 5. Same as Fig. 4, but for (a) the (1 1 1)-TiO and (b) the (1 1 1)-PbO₂ terminations.

to the inward displacement of the outermost layer Ti atom, the space electric field of positive charge is decreased. For (1 1 1)-PbO₃ termination, the space electric field is dominantly from a negative formal charge of -4 contributed by one Pb atom and three O atoms together. Although the inward displacement of Pb atom on the first layer reduces the space electric field of positive charge, the outward displacements of the three O atoms are much larger which leads to a stronger reduction in the space electric field of negative charge, thus the space electric field is also decreased. For (1 1 1)-TiO termination, due to adsorbing an O atom, the initio formal charge of +4 firstly reduced to +2, thus the space electric field are dominantly from a positive formal charge of +2, and then the inward displacement of first layer Ti atom continuously reduces the space electric field of positive charge. For (1 1 1)-PbO₂ terminations, the removal of an outermost layer O atom firstly reduces the formal charge from -4 to -2, thus the space electric field is dominant from a negative formal charge of -2, and then the reduction of the space electric field of positive charge by the outward displacement of first layer Pb atom and that of the space electric field of negative charge by inward displacement of the same layer O atoms together result in a reduction of the total space electronic field.

The results of electronic structure calculation for the two constructed terminations show that they are all insulating. The densities of states of each layer for the relaxed (1 1 1)-TiO and (1 1 1)-PbO₂ terminations are given in Fig. 5(a) and (b) respec- tively, and the fifth layer is the central one that can be regarded as in the bulk. From Fig. 5(a), we can see that in (1 1 1)-TiO slab, compared with the similar DOS of the third and central fifth Ti layers, the DOS of the first TiO layer decreases at low energy region of both VB and CB except two sharp peaks appear at -14.5 eV and at top of the VB which are contributed by the adatom O. In addition, a similar DOS curve is obtained for the second and fourth PbO₃ layers. From Fig. 5(b), we can see that in (1 1 1)-PbO₂ slab, compared with the similar DOS of the third and central fifth PbO₃ layers, the DOS of the first PbO₂ layer decreases at low energy region of both VB and CB except one narrow and spiky peak appears at about -16 eV. Compared with the fourth Ti layers, the second Ti layer has a lower DOS at the low energy region of the VB and a narrower and lower DOS peak of CB. We can conclude that, for both (1 1 1)-TiO and (1 1 1)-PbO₂ terminations, although very weak electron redistributions are found, changes of DOS originate dominantly from modifications of the surface layer compositions.

### 3.3. Dangling bond and surface charge
An isolated dangling bond appeared on the surface can introduce a gap state with a very small dispersion. This has been reported in many papers [31-33]. However, when more than one dangling bonds are close to each other, the original localized gap states may disappear, splitting into bonding states (around the top of valence band) and anti-bonding states (around the bottom of the conduction band), due to the interaction between these dangling bonds. Such new bonding states or anti-bonding states are even inside into the valence band or conduction band. In our calculations, because of the periodical boundary condition, the dangling bonds from the O or Ti of the selected $(1 \times 1)$ supercell for cubic PbTiO₃ (1 1 1) surfaces can interact with each other in this $(1 \times 1)$ surpercell and even with the dangling bonds in the adjacent surpercells, the original gap state of each dangling bond is thus transformed into the bonding state and anti-bonding state. Therefore, there are no states in the gap from the O and Ti dangling bonds. The disappearance of the dangling bonds in the band gap has been obtained in many other similar surface calculations [17,34,35].

To investigate the electronic density distribution of PbTiO₃ (1 1 1) surfaces, we plot the charge density contours of different slab models in Fig. 6. Different from the bulk charge distribution, we can see that due to the charge redistribution of the surface atoms, a charge accumulation appears at the outermost layer for each type of (1 1 1) surface.

### 4. Surface stability
It is known that surface is an open system which can exchange atoms with the surroundings. Therefore, investigating which

![](./images/811850816104169472_6.jpg)

Fig. 6. Charge density contours of relaxed $PbTiO_{3}(\begin{array}{lll}1 & 1 & 1\end{array})$ surfaces in $(2 \overline{1} \overline{1})$ plane: (a) (1 111 )-Ti termination containing surface Ti atom; (b) (1 111 )-PbO₃ termination containing two surface O atoms; (c) (1 111 )-TiO termination containing surface Ti atom and O adatom; (d) (1 111 )-PbO₂ termination containing surface O and Pb atoms. The corresponding positions of the containing atoms are referred to Fig. 2.

termination is more stable under specific experimental environment is very significant, for instance, in oxygen and lead external environments. In order to solve the problem, we have calculated the surface grand potential, which implies a contact with matter reservoirs, for the four terminations with the equation [36,37]:

$$
\Omega(\mathrm{i})=\frac{1}{2 S}\left[E_{\text {slab }}^{\text {rel }}(\mathrm{i})+P V-T S-n_{\mathrm{Pb}} \mu_{\mathrm{Pb}}-n_{\mathrm{Ti}} \mu_{\mathrm{Ti}}-n_{\mathrm{O}} \mu_{\mathrm{O}}\right],\qquad(1)
$$

where $\Omega(\mathrm{i})$ and $E_{\text {slab }}^{\text {rel }}(\mathrm{i})$ (i = Ti, PbO₃, TiO or PbO₂) are the surface grand potential per unit area and the slab energy after relaxation of i termination respectively. The $\mu_{\mathrm{Pb}}$, $\mu_{\mathrm{Ti}}$ and $\mu_{\mathrm{O}}$ are the chemical potentials of the Pb, Ti and O atomic species, and $n_{\mathrm{Pb}}$, $n_{\mathrm{Ti}}$ and $n_{\mathrm{O}}$ are the number of Pb, Ti and O atoms in the slab respectively. For typical pressure $P$ and temperature $T$, the $PV$ and $-TS$ terms can be neglected with respect to the other contributions. Since PbTiO₃ is a ternary oxide, the chemical potential $\mu_{\mathrm{PbTiO}_{3}}$ of the cubic phase is defined as a sum of three terms,
$$
\mu_{\mathrm{PbTiO}_{3}}=\mu_{\mathrm{Pb}}+\mu_{\mathrm{Ti}}+3 \mu_{\mathrm{O}}.\qquad(2)
$$

As long as the surface is in equilibrium with the bulk PbTiO₃, we have $\mu_{\mathrm{PbTiO}_{3}}=E_{\text {bulk }}$ ($E_{\text {bulk }}$ is the bulk energy per formula unit of cubic PbTiO₃), and can eliminate the $\mu_{\mathrm{Ti}}$ variable in the surface grand potential by substituting Eq. (2) into Eq. (1),
$$
\Omega(\mathrm{i})=\frac{1}{2 S}\left[E_{\text {slab }}^{\text {rel }}(i)-n_{\mathrm{Ti}} E_{\text {bulk }}-\mu_{\mathrm{O}}\left(n_{\mathrm{O}}-3 n_{\mathrm{Ti}}\right)-\mu_{\mathrm{Pb}}\left(n_{\mathrm{Pb}}-n_{\mathrm{Ti}}\right)\right]. \quad(3)
$$

According to Eq. (3), one can deduce the range of the accessible values of $\Omega(\mathrm{i})$ for each termination if the minimum and maximum values of the O and Pb chemical potentials are known. Introducing the variations of the chemical potential with reference phases ($\Delta \mu_{\mathrm{O}}=\mu_{\mathrm{O}}-E_{\mathrm{O}_{2}}^{\mathrm{mol}} / 2$ and $\Delta \mu_{\mathrm{Pb}}=\mu_{\mathrm{Pb}}-E_{\mathrm{Pb}}^{\text {Bulk }}$), we can obtain

![](./images/811850816104169472_7.jpg)

Fig. 7. Stability diagram of $PbTiO_{3}(\begin{array}{lll}1 & 1 & 1\end{array})$ surfaces. The most stable termination is represented in the left panel as a function of the excess O and Pb chemical potentials $\Delta \mu_{\mathrm{O}}$ (horizontal) and $\Delta \mu_{\mathrm{Pb}}$ (vertical). In the right panel, the surface grand potentials are represented as a function of $\Delta \mu_{\mathrm{O}}$ (for a particular value of the Pb chemical potential $\Delta \mu_{\mathrm{Pb}}=0$ eV).

from Eq. (3) the followings:

$$
\Omega(\mathrm{i})=\phi(\mathrm{i})-\frac{1}{2 S}\left[\Delta \mu_{\mathrm{O}}\left(n_{\mathrm{O}}-3 n_{\mathrm{Ti}}\right)-\Delta \mu_{\mathrm{Pb}}\left(n_{\mathrm{Pb}}-n_{\mathrm{Ti}}\right)\right], \tag{4}
$$

$$
\begin{aligned}
\phi(\mathrm{i}) & =\frac{1}{2 S}\left[E_{\text {slab }}^{\text {rel }}(\mathrm{i})-n_{\mathrm{Ti}} E_{\text {bulk }}-\frac{1}{2} E_{\mathrm{O}_{2}}^{\text {mol }}\left(n_{\mathrm{O}}-3 n_{\mathrm{Ti}}\right)\right. \\
& \left.-E_{\mathrm{Pb}}^{\text {bulk }}\left(n_{\mathrm{Pb}}-n_{\mathrm{Ti}}\right)\right],
\end{aligned} \tag{5}
$$

$\phi(\mathrm{i})$ expresses the stability of the surface with respect to bulk $\mathrm{PbTiO}_{3}$, molecular oxygen, and metallic lead, while $(n_{\mathrm{O}}-3 n_{\mathrm{Ti}})$ represents the excess (if positive) or the deficiency (if negative) in the number of oxygen atoms of the terminations.

We plot the stability diagram of $\mathrm{PbTiO}_{3}\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ surfaces in $\mathrm{O}$ and $\mathrm{Pb}$ external environments and the surface grand potential $\Omega(\mathrm{i})$ as a function of $\Delta \mu_{\mathrm{O}}$ for a particular value of the $\mathrm{Pb}$ chemical potential $\Delta \mu_{\mathrm{Pb}}=0 \mathrm{eV}$ in left panel and right panel of Fig. 7. Small values of $\Delta \mu_{\mathrm{O}}$ and $\Delta \mu_{\mathrm{Pb}}$ correspond to O-poor and Pb-poor conditions, while large ones are associated with high oxygen and high lead conditions respectively. In the left panel, we can see that only three out of four possible terminations, $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2},\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{TiO}$, and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{Ti}$ terminations can be formed. The $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2}$ termination is stable in O- and Pb-rich environments, however, the $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti termination is stable in O- and Pb-poor conditions. In addition, the constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-TiO termination also shows a relative small stability domain in moderate O and Pb conditions. In the right panel, we can see that in the accessible values of $\Delta \mu_{\mathrm{O}}$, the $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2},\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{TiO}$, and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti terminations are all likely to be observed. Moreover, the $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2}$ termination is the dominant among the three terminations in the range of accessible values of $\Delta \mu_{\mathrm{O}}$. In experiments, by controlling the oxygen pressure in the vacuum chamber, different terminations of $\mathrm{PbTiO}_{3}\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ surfaces should be obtained.

## 5. Conclusions

Under GGA, the structural and electronic properties of four $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ surfaces of cubic $\mathrm{PbTiO}_{3}$, directly cleaved $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{3}$ terminations and constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-TiO and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ $\mathrm{PbO}_{2}$ terminations, have been studied by using projector augmented wave method implemented in VASP. The surface stabilities in $\mathrm{O}$ and $\mathrm{Pb}$ external environments are also considered in detail for the four different $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ terminations. Following conclusions are obtained:

(1) For two stoichiometric $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{3}$ terminations, Ti-O bonds between outermost two layers contract, while those between the second and the third layers expand. The $\mathrm{O}-\mathrm{O}$ distances of surface $\mathrm{PbO}_{3}$ layer of $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{3}$ termination also contract. In addition, the effects of atomic relaxations on electronic structure are significant. Moreover, from the DOS curves of both terminations, we know that the effects of the surface on the DOS are dominantly on the Ti layers, especially the CB.

(2) For the constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-TiO termination, Ti-O bonds between the outermost two layers and those between the second $\mathrm{PbO}_{3}$ layer and the third Ti layer all contract. For the constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2}$ termination, Ti-O bonds between the outermost two layers contract, however, inequivalent Ti-O bonds between the second layer Ti atom and the third layer $\mathrm{O}$ atoms are found, that is, two bonds expand and the other one contracts. In addition, the two constructed terminations are all insulating and changes of DOS originate dominantly from modifications of the surface compositions.

(3) It is found that for all four different $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ terminations, the movements of the cation and/or anion on the outermost layer along the surface normal direction after relaxation all result in a reduction of the space electric field. Due to the interaction between the surface Ti and O dangling bonds, we found no localized states in the middle part of the gap, but only bonding states and anti-bonding states at the edge of the band gap.

(4) In the four terminations of $\mathrm{PbTiO}_{3}\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ surface, the constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2}$ termination is the most stable one in O- and Pb-rich environments, however, the stoichiometric $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti termination is the most stable one in O- and Pb-poor conditions. The $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-TiO termination also shows a small stability domain in moderate $\mathrm{O}$ and $\mathrm{Pb}$ environments. Moreover, in the range of accessible values of $\Delta \mu_{\mathrm{O}}$, the $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2},\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$ $\mathrm{TiO}$, and $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)$-Ti terminations are all likely to be observed, especially for the constructed $\left(\begin{array}{lll}1 & 1 & 1\end{array}\right)-\mathrm{PbO}_{2}$ termination.

## Acknowledgement

The authors would like to acknowledge the State Key Development for Basic Research of China (Grant No. 2004CB619302) for providing financial support for this research.

## References

[1] M.E. Lines, A.M. Glass, Principles and Applications of Ferroelectrics and Related Materials, Clarendon, Oxford, 1977.

[2] V.E. Henrik, P.A. Cox, The Surface of Science of Metal Oxides, Cambridge University Press, New York, 1994.

[3] J.F. Scott, Ferroelectric Memories, Springer, Berlin, 2000.

[4] C. Noguera, Physics and Chemistry at Oxide Surface, Cambridge University Press, New York, 1996.

[5] C. Noguera, J. Phys. Condens. Matter 12 (2000) R367.

[6] R.E. Cohen, H. Krakauer, Phys. Rev. B 42 (1990) 6416.

[7] R.E. Cohen, Nature (Lond.) 358 (1992) 136.

[8] H. Fujishita, S. Hoshino, J. Phys. Soc. Jpn. 53 (1983) 226.

[9] J.F. Scott, C.A. Paz de Araujo, Science 246 (1986) 1404.

[10] R.J. Nelmes, W.F. Kuhs, Solid State Commun. 54 (1985) 721.

[11] A. Garcia, D. Vanderbilt, Phys. Rev. B 54 (1996) 3871.

[12] U.V. Waghmare, K.M. Rabe, Phys. Rev. B 55 (1997) 6161.

[13] W. Zhong, D. Vanderbilt, Phys. Rev. Lett. 74 (1995) 2587.

[14] A. Munkholm, S.K. Streiffer, M.V. Ramana Murty, J.A. Eastman, C. Thompson, O. Auciello, L. Thompson, J.F. Moore, G.B. Stephenson, Phys. Rev. Lett 88 (2002) 016101.

[15] E. Heifets, R.I. Eglitis, E.A. Kotomin, J. Maier, G. Borstel, Phys. Rev. B 64 (2001) 235417.

[16] E. Heifets, W.A. Goddard, E.A. Kotomin, R.I. Eglitis, G. Borstel, Phys. Rev. B 69 (2004) 035408.

[17] Y.X. Wang, M. Arai, T. Sasaki, C.L. Wang, Phys. Rev. B 73 (2006) 035411.

[18] J.M. Zhang, J. Cui, K.W. Xu, V. Ji, Z.Y. Man, Phys. Rev. B 76 (2007) 115426.

[19] J. Cui, J.M. Zhang, K.W. Xu, V. Ji, Z.Y. Man, Surf. Coat. Technol. 202 (2008) 3284.

[20] R.I. Eglitis, G. Borstel, E. Heifets, S. Piskunov, E. Kotomin, J. Electroceram. 16 (2006) 289.

[21] A. Asthagiri, D.S. Sholl, J. Chem. Phys. 116 (2002) 9914.

[22] A. Asthagiri, D.S. Sholl, Surf. Sci. 581 (2005) 66.

[23] A. Asthagiri, C. Niederberger, A.J. Francis, L.M. Poter, P.A. Salvador, D.S. Sholl, Surf. Sci. 537 (2003) 134.

[24] S.M. Hosseini, T. Movlarooy, A. Kompany, Physica B 391 (2007) 316.

[25] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558.

[26] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1994) 8245.

[27] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.

[28] G. Kresse, D. Joubert, Phys. Rev. 59 (1999) 1758.

[29] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[30] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5118.

[31] R.G. Henning, P.A. Fedders, A.E. Carlsson, Phys. Rev. B 66 (2002) 195213.

[32] R. Kagimura, R.W. Nunes, H. Chacham, Phys. Rev. Lett. 98 (2007) 026801.

[33] H. Raza, Phys. Rev. B 76 (2007) 045308.

[34] E. Heifets, R.I. Eglitis, E.A. Kotomin, J. Maier, G. Borstel, Surf. Sci. 513 (2002) 211.

[35] A. Pojani, F. Finocchi, C. Noguera, Appl. Surf. Sci. 142 (1999) 177.

[36] A. Pojani, F. Finocchi, C. Noguera, Surf. Sci. 442 (1999) 179.

[37] X.G. Wang, A. Chaka, M. Scheffler, Phys. Rev. Lett. 84 (2000) 3650.