# New Group V Elemental Bilayers: A Tunable Structure Model with 4,6,8-atom Rings

Xiangru Kong, $^{1, *}$ Linyang Li, $^{2, \dagger}$ Ortwin Leenaerts, $^{2}$ Xiong-jun Liu, $^{1}$ and François M. Peeters $^{2}$

$^{1}$ International Center for Quantum Materials, School of Physics, Peking University, Beijing,
100871, China and Collaborative Innovation Center of Quantum Matter, Beijing 100871, China
$^{2}$ Department of Physics, University of Antwerp, Groenenborgerlaan 171, B-2020 Antwerp, Belgium

(Dated: June 18, 2021)

Two-dimensional (2D) group V elemental materials have attracted widespread attention due to their nonzero band gap while displaying high electron mobility. Using first-principles calculations, we propose a series of new elemental bilayers with group V elements (Bi, Sb, As). Our study reveals the dynamical stability of 4, 6, and 8-atom ring structures, demonstrating their possible coexistence in such bilayer systems. The proposed structures for Sb and As are large-gap semiconductors that are potentially interesting for applications in future nanodevices. The Bi structures have nontrivial topological properties with a large and direct nontrivial band gap. The nontrivial gap is shown to arise from a band inversion at the Brillouin zone center due to the strong intrinsic spin-orbit coupling (SOC) in Bi atoms. Moreover, we demonstrate the possibility to tune the properties of these materials by enhancing the ratio of 6-atom rings to 4 and 8-atom rings, which results in wider nontrivial band gaps and lower formation energies.

## I. INTRODUCTION

The story of 2D materials begins with the successful exfoliation of graphene from graphite. $^{1}$ 2D materials are usually defined as crystalline materials consisting of a single or few layers of atoms. The unusual physical properties, caused by dimensional restrictions, lead researchers to study these materials for possible use in applications and future nanodevices. $^{2}$ The search for other 2D materials besides graphene is an on-going field of research. In analogy to graphene, other group IV elements also form 2D hexagonal structures, such as silicene, $^{3-6}$ germanene, $^{7,8}$ and stanene, $^{9}$ and have been successfully synthesized on different substrates. Similar structures could also be observed for the 2D group V elemental structures. In theory, buckled hexagonal honeycomb bilayers of group V elements are also stable and favorable in energy. $^{10}$ For example, hexagonal Bi(111) bilayers $^{11-14}$ have been experimentally synthesized on $Bi_{2}Te_{3}$ and $Bi_{2}Se_{3}$ surfaces. $^{15-17}$ In this connection, the successful growth of single layer blue phosphorus has attracted widespread attention to the group V elemental bilayers due to their nonzero band gap and high electron mobility. $^{18}$ There have also been many suggestions for other 2D stable carbon allotropes, $^{19,20}$ such as phagraphene $^{21}$ and graphyne, $^{22,23}$ and some of them have been successfully created or can be found as defects in graphene. The physical properties of such crystalline materials mainly originate from the underlying symmetry of the crystal structure. Therefore, it is interesting to study 2D crystal structures with different symmetries. Recently, some theoretical works have studied 2D group V structures with 4-atom and 8-atom rings on a square lattice. $^{24,25}$ However, the formation energy of these bilayer structures is relatively high which makes it difficult to realize them in experiments. It is thus an interesting question how such materials can be made more stable.

One of the most intriguing properties of some 2D materials is their nontrivial band topology. 2D topological insulators with time-reversal (TR) symmetry, also known as quantum spin Hall (QSH) insulators, are a very important set of 2D materials. $^{26-29}$ Graphene was the first proposal for such a topological insulator, but its negligible nontrivial band gap makes it impossible to observe the QSH effect. $^{29,30}$ In experiment, the QSH effect has been observed in HgTe/CdTe and InAs/GaSb quantum wells, $^{31-33}$ but the small bulk gap arising from weak SOC makes the operating temperature very low and this limits its further applications. $^{34-38}$ To realize 2D topological insulators with a large band gap, most studies have focused on some heavy elements, such as Bi, which exhibit a strong SOC effect. The largest nontrivial bulk gap (1.08eV) is found in $Bi_{2}F_{2}$ bilayer. The huge SOC gap in this material originates from the Bi $p_{x}$ and $p_{y}$ orbitals. $^{39,40}$ But also hexagonal Bi(111) bilayers have been realized and their time-reversal symmetry-protected edge states have been observed. $^{15}$ However, their topological nature is still debated. The search for other Bi-based QSH insulators is therefore interesting.

In this work, we propose a new structure model with 4-atom, 6-atom, and 8-atom (4,6,8-atom) rings for the group V elements: Bi, Sb, and As. The formation energy of these proposed structures is lower than those of other reported 2D group V structures containing 4- and 8-atom rings. $^{24,25}$ We find that their phonon spectra contain no imaginary frequency modes, indicating their dynamical stability. In the case of Bi, the calculated band structure suggests nontrivial topological properties with a relative large nontrivial bulk gap of 0.123 eV, resulting from a band inversion at the $\Gamma$ point. The proposed Sb and As bilayers show large indirect band gaps with SOC, but these band gaps are trivial.

We demonstrate that the properties of the proposed structures can be tuned by the number of 6-atom rings. For Bi, we show that the formation energy can be decreased while retaining the topologically nontrivial properties. The nontrivial SOC band gap can reach 0.373 eV, which is larger than that of other reported allotropes of

Bi, except the hexagonal bilayer. $^{24,25,41}$

## II. COMPUTATIONAL METHODS

Our first-principles calculations are based on Density Functional Theory (DFT) with the projector augmented wave method as implemented in the Vienna $ab$ $initio$ simulation package (VASP). $^{42-44}$ The generalized gradient approximation (GGA) in the form proposed by Perdew, Burke and Ernzerhof (PBE) $^{45}$ was chosen as the electron exchange-correlation functional. The structure relaxation including the atomic positions and lattice vectors was performed by the conjugate gradient (CG) scheme until the maximum force on each atom was less than 0.01 eV/Å. The energy cutoff of the plane waves was set to 500 eV with an energy precision of $10^{-5}$ eV. The Brillouin zone (BZ) was sampled by using a $13\times7\times$ 1 $\Gamma$-centered Monkhorst-Pack grid. Phonon frequencies are calculated by the finite displacement method with the Phonopy code. $^{46}$

The $Z_{2}$ topological invariants were obtained by calculating the Wannier Charge Centers (WCCs) and tracking the largest gap in the spectrum of the WCCs, $^{47}$ which is equivalent to the computation of the Wilson loop. $^{48}$ The explicit numerical computations were done with the Z2Pack code $^{49}$ which combines the $ab$ $initio$ calculations with the Wannier90 code. $^{50}$ The surface state calculations are illustrated with an effective tight-binding Hamiltonian generated from the first-principles Wannier functions. The $s$ and $p$ orbitals of the Bi atoms from the first-principles wave functions are used as the initial trial orbitals. The iterative Greens function method $^{51}$ was used with the software package Wannier tools. $^{52}$

## III. RESULTS

### A. Structure and Stability

Due to the similarity of the proposed structures for the various investigated elements, we mainly focus on the structure model of Bi in this section. An example of such a structure is given in Fig. 1. Its lattice is rectangular, which is different from the hexagonal lattice of Bi(111) bilayers $^{11-14}$ and the square lattice of the recently proposed Bi bilayers consisting of 4,8-atom rings. $^{24,25}$ The space group of the proposed orthorhombic crystals is $Pccm$ (or $D_{2h}^{3}$). There is a two-fold rotation, mirror, and inversion symmetry in this structure. Along the $x$ direction, there are two kinds of arrangements of atomic rings. One is formed by the line along the center of 4(8)-atom rings while the other is along the center of the 6-atom rings, as indicated by the blue dashed line in Fig. 1(a). The two arrangements of atomic rings alternate along the $y$ direction and form a new type of Bi bilayer. Regarding the number of atomic rings, one 4-atom ring corresponds to one 8-atom ring and one 6-atom ring. Since the 4-atom rings always come in pairs with the 8-atom rings, our structure is denoted as a 4(8)-6 Bi bilayer in the following. As demonstrated below, such structures can be easily tuned by including more hexagons. A similar structure model can be applied to Sb and As.

![](./images/867753046724051212_1.jpg)

FIG. 1. (a) Top view of the 4(8)-6 Bi bilayer: the rectangle indicates the unit cell, the blue dashed lines are the 4(8)-center-connected and 6-center-connected lines, and the inset in the upper right corner depicts the Brillouin zone (BZ) with the time-reversal invariant momenta (TRIM). (b) Side view of the 4(8)-6 Bi bilayer. (c) Phonon spectra of 4(8)-6 Bi, Sb, and As bilayers.

The optimized structure parameters for the 4(8)-6 bilayers of Bi, Sb, and As are listed in Table I. Due to the similarity of these 4(8)-6 bilayers, we focus on the Bi bilayer first. The lattice constant $a$ ($b$) in the $x$ ($y$) direction of Bi is 7.918 Å (13.050 Å). Although the lattice of the 4(8)-6 bilayer has different symmetry than the hexagonal and square Bi bilayers, the local arrangement of the neighboring atoms is similar. $^{11-14,24,25}$ One Bi atom forms a bond with three other Bi atoms that are all above or below than the position of the Bi atom in the $z$ direction. However, while there is only one kind of Bi atoms (one Wyckoff Position) in the hexagonal and square Bi bilayers, there are two kinds of Bi atoms (two Wyckoff Positions) in the 4(8)-6 structure, as illustrated in Fig. 1(b). Corresponding to these two kinds of Bi atoms, denoted as Bi(1) and Bi(2) in the following, there are two buckling heights, $h_{1}=1.579$ Å and $h_{2}=2.014$ Å. The buckling heights of the hexagonal (1.737 Å) and square (1.757 Å) Bi bilayer are in between the two heights of the 4(8)-6 Bi bilayer. The Bi atoms in the 4(8)-6 bilayer are connected by four different bonds (see Fig. 1(a)) of which the lengths are shown in Table I. The length $d_{1}$ of the bond shared by the 6-atom and 8-atom rings is about 3.046 Å which is practically the same as the bond

<table>
<caption>TABLE I. The optimized structure parameters of 4(8)-6 Bi, Sb and As bilayers. $a$ ($b$) is the lattice constant in the $x$ ($y$) direction; $h_1$ and $h_2$ is the buckling height as shown in Fig. 4(b); $d_{1,2,3,4}$ denotes the different bond lengths shown in Fig. 4(a). $\Delta$E is the formation energy defined by Eq. (1).</caption>
<thead>
  <tr>
    <th>elements</th>
    <th>$a$ (Å)</th>
    <th>$b$ (Å)</th>
    <th>$h_1$ (Å)</th>
    <th>$h_2$ (Å)</th>
    <th>$d_1$ (Å)</th>
    <th>$d_2$ (Å)</th>
    <th>$d_3$ (Å)</th>
    <th>$d_4$ (Å)</th>
    <th>$\Delta$E (meV/atom)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Bi</td>
    <td>7.918</td>
    <td>13.050</td>
    <td>1.579</td>
    <td>2.014</td>
    <td>3.046</td>
    <td>3.055</td>
    <td>3.079</td>
    <td>3.043</td>
    <td>52.8</td>
  </tr>
  <tr>
    <td>Sb</td>
    <td>7.529</td>
    <td>12.402</td>
    <td>1.505</td>
    <td>1.897</td>
    <td>2.893</td>
    <td>2.901</td>
    <td>2.919</td>
    <td>2.892</td>
    <td>58.1</td>
  </tr>
  <tr>
    <td>As</td>
    <td>6.581</td>
    <td>10.904</td>
    <td>1.290</td>
    <td>1.563</td>
    <td>2.510</td>
    <td>2.516</td>
    <td>2.531</td>
    <td>2.509</td>
    <td>71.9</td>
  </tr>
</tbody>
</table>

length in the buckled hexagonal Bi bilayer (3.046 Å).$^{11-14}$ The length $d_2$ of the bond shared by 4-atom and 6-atom rings is about 3.055 Å which is slightly larger than $d_1$. The bond length $d_3$ shared by the 4-atom and 8-atom rings is about 3.079 Å which is larger than the reported bond length (3.059 Å) shared by the 4-atom and 8-atom rings in square Bi bilayer.$^{24}$ The bond length $d_4$ shared by the 8-atom and 8-atom rings is about 3.043 Å which is nearly the same as the reported bond length (3.044 Å) shared by the 8-atom and 8-atom rings in square Bi bilayer.$^{24}$ We can therefore conclude that the proposed structure is formed by an only slightly distorted combination of the square and hexagonal bilayer structures. Similar results are obtained for the 4(8)-6 Sb and As bilayers, although the structure parameters of Sb and As are smaller than that of 4(8)-6 Bi bilayer (see table I). This is in accordance with the general expectation that the lighter the atoms are, the smaller the structure parameters become.

Next, let us focus on the stability of the 4(8)-6 bilayers. To this end, we define the formation energy with respect to the hexagonal bilayer as follows:

$$
\Delta E=(E_{total}-N_{atom}\times\mu_{atom})/N_{atom}, \tag{1}
$$

where $E_{total}$ is the total energy of the 4(8)-6 bilayer, $N_{atom}$ is the total number of atoms in the crystal structure and $\mu_{atom}$ is the energy per atom calculated for the hexagonal honeycomb structure. Starting from Bi, $\Delta E$ increases with decreasing atomic number. The formation energy for Bi (52.8 meV/atom) is the smallest, while $\Delta E$ for Sb and especially As becomes somewhat larger. For comparison, the formation energy of a 4(8)-6 P bilayer was also calculated, and it was found to be even larger (76.8 meV/atom). Furthermore, the phonon spectrum of the P bilayer exhibits imaginary frequency modes, indicating its dynamical instability. Therefore, we will not consider the 4(8)-6 P bilayer in this work. For Bi, the formation energy of the 4(8)-6 Bi bilayer (52.8 meV/atom) is significantly smaller than that of a square Bi bilayer (80.6 meV/atom).$^{24}$ A similar behavior can be observed in 2D C allotropes, where the formation energy decreases with increasing number of C hexagons. In our case, the 4(8)-6 bilayers should be more stable than the reported square bilayers due to the larger number of hexagons.$^{24,25}$ To investigate the dynamical stability of the 4(8)-6 bilayers, their phonon spectrum along the high symmetry lines in the BZ is calculated from first principles using a supercell approximation (see Fig. 4(c)). It can be seen that the 4(8)-6 bilayers of Bi, Sb, and As are all dynamically stable, because no imaginary frequency modes are observed in their phonon spectrum.

## B. Electronic Band Structure

![](./images/867753046724051212_2.jpg)

FIG. 2. (a), (c) and (e) are the band structures of 4(8)-6 Bi, Sb, and As bilayers without SOC; (b), (d) and (f) are the band structures with SOC. The band gaps are given in the figure.

As mentioned in the introduction, 2D materials often have interesting electronic properties. The electronic band structure of the investigated 4(8)-6 bilayers is shown in Fig. 2. The left figures ((a), (c), and (e)) were calculated without SOC and the right ones ((b), (d), and (f)) were calculated with SOC. Let us consider the 4(8)-6 Bi bilayer first. It has a direct band gap of 0.570 eV at the $\Gamma$ point without SOC, which is similar to the hexagonal and square Bi bilayer.$^{13,24,25}$ With inclusion of SOC, the

4(8)-6 Bi bilayer retains its direct band gap, contrary to the case of hexagonal and square Bi bilayers which get an indirect band gap with SOC. The value of the direct band gap becomes 0.123 eV, which is smaller than that of the hexagonal and square Bi bilayer.

On the other hand, the Sb/As 4(8)-6 bilayers have indirect band gaps with and without SOC. This is similar to the hexagonal Sb/As bilayers, but different from the square ones which have a direct band gap both with and without SOC. The 4(8)-6 Sb bilayer has a large indirect SOC band gap of 1.011 eV, which is slightly smaller than the direct band gap (1.13eV) of the square Sb bilayer.²⁵ The 4(8)-6 As bilayer has the largest indirect SOC band gap (1.454 eV) of the three structures, but it is still smaller than the direct gap of the square As bilayer (1.71 eV).²⁵ Although, 4(8)-6 Bi, Sb, and As bilayers have substantially different band gaps, the regular pattern that the gap values increase with decreasing atomic number is similar to the hexagonal/square group V bilayers.

### C. Topological Properties

Since the electronic band gaps with SOC of hexagonal and square Bi bilayers have been shown to be nontrivial,¹³,²⁴,²⁵ we investigate the topological properties of the 4(8)-6 Bi bilayers here. Note that structures containing Bi atoms are often reported to be topologically nontrivial due to the strong intrinsic SOC of Bi. To investigate the topological properties of the 4(8)-6 Bi bilayer, we calculated the $Z_2$ topological invariant by tracking the largest gap in the spectrum of the WCCs. In addition to the Wilson like methods, we also calculated the $Z_2$ invariants by parity analysis because the 4(8)-6 Bi bilayer has inversion symmetry. Following Fu et al.,⁵³ the $Z_2$ topological invariant ($v$) in systems with time-reversal symmetry and inversion symmetry can be obtained by:

$$
(-1)^{v}=\prod_{i=1}^{4} \delta\left(K_{i}\right), \delta\left(K_{i}\right)=\prod_{m=1}^{N} \xi_{2 m}^{i}, \tag{2}
$$

with $K_i$ the TRIMs, $\xi = \pm 1$ the parity eigenvalue of the wave function, $\delta(K_i)$ the product of the parity eigenvalues at the TRIM, and $N$ the total number of degenerate occupied bands. In our case $K_i$ is Γ, X, Y, or M. The $Z_2$ topological invariant of the 4(8)-6 bilayer equals 1, which proves its nontrivial nature. We list the results of the parity eigenvalues in Table II. It is seen that only the Bi bilayers have a nontrivial topological invariant ($v=1$), with the only difference in parity eigenvalues between 4(8)-6 Bi and Sb or As bilayers at the Γ point. The parity eigenvalue of -1 at the Γ point of the 4(8)-6 Bi bilayer suggests that there is a band inversion at this TRIM (see below). Similar to the hexagonal and square bilayers, only the Bi bilayer has a topologically nontrivial band gap, while Sb and As bilayers have trivial gaps.¹³,²⁵

<table>
<caption>TABLE II. The parity eigenvalues at the four TRIMs (Γ, X, Y, M) and the $Z_2$ topological invariants ($v$) of the 4(8)-6 Bi, Sb, and As bilayers.</caption>
<thead>
  <tr>
    <th>element</th>
    <th>Γ</th>
    <th>X</th>
    <th>Y</th>
    <th>M</th>
    <th>$v$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Bi</td>
    <td>-1</td>
    <td>1</td>
    <td>-1</td>
    <td>-1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Sb</td>
    <td>1</td>
    <td>1</td>
    <td>-1</td>
    <td>-1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>As</td>
    <td>1</td>
    <td>1</td>
    <td>-1</td>
    <td>-1</td>
    <td>0</td>
  </tr>
</tbody>
</table>

![](./images/867753046724051212_3.jpg)

FIG. 3. The orbital-projected band structures of the 4(8)-6 Bi bilayer: (a) without SOC and (b) with SOC. The symbol size indicates the contribution weight: larger dot means higher contribution while smaller one indicates lower contribution. $\pm$ indicates an even or odd parity eigenvalue. Green: $p_{x,y}$ ($p_x$ and $p_y$) orbitals; red: $p_z$ orbitals.

To find the origin of the topologically nontrivial nature of the 4(8)-6 Bi bilayer, we investigate the band inversion by the orbital-projected band structures as shown in Fig. 3. We can see that SOC plays an important role in the inversion of the states with $p_{x,y}$ and $p_z$-orbital character: without SOC at the Γ point, the $p_{x,y}$ orbitals contribute the most to the highest occupied band and the $p_z$ orbitals contribute the most to the lowest unoccupied band, but the situation is reversed when including SOC. This is also confirmed by the reversal of parity eigenvalues between the highest occupied band and the lowest unoccupied band at the Γ point. Note that the observed

![](./images/867753046724051212_4.jpg)

FIG. 4. The edge states of 4(8)-6 Bi bilayer: (a) without SOC; and (b) with SOC.

![](./images/867753046724051212_5.jpg)

FIG. 5. The tunable structures: (a) 4(8)-6-6; (b) 4(8)-6-6-6; (c) 4(8)-6-6-6-6 Bi bilayers. The blue dashed lines are the 4(8)-center-connected and 6-center-connected lines.

band inversion found here is similar to the case of hexagonal and square Bi bilayers whose band inversion also occurs between the $p_{x,y}$ and $p_z$ orbitals. $^{13,24,25}$ The band inversion indicates that there must be a gap closing with corresponding formation of a Dirac cone when continuously turning on the SOC. $^{24,54}$

Besides the nonzero $Z_2$ topological invariant and the observed band inversion, the existence of gapless edge states is another prominent feature of QSH insulators. According to the bulk-edge correspondence in topological insulators, a nontrivial topological invariant ($v=1$) indicates the presence of topologically protected edge states at the edges of the material. The calculated edge states of the 4(8)-6 Bi bilayer are shown in Fig. 4. In Fig. 4(a), it is seen that there are edge states in the band gap without SOC, but these edge states do not bridge the band gap which indicates that they are trivial. However, including SOC, there are two oppositely propagating gapless edge states appearing in the bulk gap that connect the conduction and valence bands and which cross at the TRIM (X point) as shown in Fig. 4(b).

### D. Structural Tunability

As we discussed above, the formation energy decreases with increasing number of 6-atom rings in the system. In this section we investigate how the properties of the 4(8)-6 Bi bilayer can be tuned by changing the number of hexagons. This is done in a systematic way by increasing the number of 6-connected-lines which connect the centers of 6-atom rings in the $x$ direction. Taking Bi as an example, we show three such structures in Fig. 5. As indicated by the blue dashed lines, the number of 6-connected-lines is 2, 3, and 4 in these structures and they are correspondingly named 4(8)-6-6, 4(8)-6-6-6 and 4(8)-6-6-6-6. The calculated structure parameters of the three structures are shown in Table III. Due to the similar structure along the $x$ direction compared to 4(8)-6, the lattice constants of the expanded structures in the $x$ direction are similar (7.919 Å, 7.778 Å, 7.708 Å, and 7.661 Å) and are in between those of the square and hexagonal structure. We can easily understand this: the larger the number of the 6-atom rings becomes, the closer to the hexagonal Bi bilayer the expanded structure gets. There is now a larger variety of different Bi atoms, corresponding to various buckling heights, so we compare the averaged buckling heights. These are 1.724 Å, 1.735 Å, 1.734 Å, and 1.734 Å, respectively. Note that these averaged buckling heights are larger than the buckling height of $1.71 \AA$ as found in the hexagonal Bi bilayer $^{14,55}$ and smaller than $1.76 \AA$ in the square Bi bilayer. $^{24,25}$

![](./images/867753046724051212_6.jpg)

FIG. 6. The energy per atom of 4(8)-6, 4(8)-6-6, 4(8)-6-6-6, 4(8)-6-6-6-6 Bi bilayers.

<table>
<caption>TABLE III. The optimized structure parameters of 4(8)-6-6, 4(8)-6-6-6, and 4(8)-6-6-6-6 Bi bilayers. $a$ ($b$) is the lattice constant in the $x$ ($y$) direction; $h$ is the averaged buckling height.</caption>
<thead>
<tr>
<th>structures</th>
<th>$a$ (Å)</th>
<th>$b$ (Å)</th>
<th>$h$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>4(8)-6-6</td>
<td>7.778</td>
<td>17.493</td>
<td>1.735</td>
</tr>
<tr>
<td>4(8)-6-6-6</td>
<td>7.708</td>
<td>21.834</td>
<td>1.734</td>
</tr>
<tr>
<td>4(8)-6-6-6-6</td>
<td>7.661</td>
<td>26.188</td>
<td>1.734</td>
</tr>
</tbody>
</table>

We also calculated the energy per atom in all these structures and compare them to the hexagonal and square Bi bilayers which have been studied before. $^{14,24,25,55}$ As shown in Fig. 6, the hexagonal Bi bilayer has the lowest energy which implies it is the most

![](./images/867753046724051212_7.jpg)

FIG. 7. (a), (c), and (e) are the band structures of the 4(8)-6-6, 4(8)-6-6-6, and 4(8)-6-6-6-6 Bi bilayers without SOC; (b), (d), and (f) are the band structures with SOC. The band gaps are marked in the figure.

![](./images/867753046724051212_8.jpg)

FIG. 8. The nontrivial edge states of the structures: (a) 4(8)-6-6, (b)4(8)-6-6-6, and (c) 4(8)-6-6-6-6 Bi bilayers.

stable of all these structures. On the other hand, the square Bi bilayer has the largest energy of all. The energy per atom of the new proposed structures varies monotonously between these two limiting structures and converges to the energy of the hexagonal bilayer as more hexagons are included.

The electronic band structures of the 4(8)-6-6, 4(8)-6-6-6, 4(8)-6-6-6-6 Bi bilayers are shown in Fig. 7. As shown in Fig. 7 (a), (c) and (e), the direct band gaps calculated without SOC of the three structures are 0.490 eV, 0.540 eV and 0.545 eV, which is smaller than that of 4(8)-6 Bi bilayer. After inclusion of SOC, as shown in Fig. 7 (b), (d) and (f), the band gaps of the three structures are 0.351 eV, 0.309 eV and 0.373 eV. Note that the band gaps become indirect in contrast to the direct band gap of the 4(8)-6 Bi bilayer. Compared with the hexagonal/square Bi bilayer, $^{13,24,25}$, only the 4(8)-6 Bi bilayer with SOC has a direct gap. Calculations of the $Z_2$ topological invariant show that all the new structures are topological insulators induced by SOC. Moreover, the indirect nontrivial SOC gap becomes larger upon inclu- sion of more Bi hexagons and approaches the gap of the hexagonal Bi bilayer. $^{24,25,41}$ The nontrivial edge states of 4(8)-6-6, 4(8)-6-6-6, 4(8)-6-6-6-6 Bi bilayers are shown in Fig. 8. The topological edge states of the three structures appear to be very similar.

In general, we can conclude that as the number of the 6-atom rings increases, the energy, electronic structure, and nontrivial band gap approach those of the hexago- nal Bi bilayer. At the same time, the lines of 4-atom and 8-atom rings can be regarded as line defects in the hexagonal Bi bilayer. By introducing such line defects, it is possible to tune the properties of the hexagonal Bi bilayer.

## IV. CONCLUSIONS

Using first-principles calculations, we propose a new stable 4(8)-6 model for the group V elements (Bi, Sb, As), which enrich the family of 2D materials. Their forma- tion energy compares favorably to square bilayers while our phonon calculations confirm their dynamical stabil- ity. The trivial (Sb, As) and nontrivial (Bi) band gap make the group V 4(8)-6 structures promising candidates for applications in future nanodevices. The nontrivial topological phase of the Bi 4(8)-6 structure was demon- strated by the calculations of $Z_2$ topological invariant, band inversion and the edge states. Interestingly, the Bi 4(8)-6 structure has a direct band gap in contrast to the previously studied square and hexagonal Bi bilayers. Moreover, the 4(8)-6 model allows for property tuning by changing the ratio of hexagons in the structure. In the case of Bi, we investigated 3 such models, namely 4(8)-6-6, 4(8)-6-6-6, and 4(8)-6-6-6-6, and found that they are all topological insulators. As the number of the hexagons increases, the energy, electronic structure, and nontrivial band gap approach those of the hexagonal Bi bilayer. In the dilute limit, the lines of 4-atom and 8-atom rings can be regarded as line defects in the hexagonal Bi bilayer that can be used to tune the properties of the hexagonal Bi bilayer.

## ACKNOWLEDGMENTS

This work is supported by the MOST (Grant No. 2016YFA0301604), NSFC (No. 11574008), Thousand- Young-Talent Program of China, and Fonds Wetenschap- pelijk Onderzoek (FWO-Vl). The computational re- sources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government department EWI.

$^{*}$ kongxru@pku.edu.cn
$^{\dagger}$ linyang.li@uantwerpen.be

$^{1}$ K. S. Novoselov, A. K. Geim, S. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Science **306**, 666 (2004).

$^{2}$ S. J. Kim, K. Choi, B. Lee, Y. Kim, and B. H. Hong, Annu. Rev. Mater. Res. **45**, 63 (2015).

$^{3}$ B. Feng, Z. Ding, S. Meng, Y. Yao, X. He, P. Cheng, L. Chen, and K. Wu, Nano Lett. **12**, 3507 (2012).

$^{4}$ P. Vogt, P. De Padova, C. Quaresima, J. Avila, E. Frantzeskakis, M. C. Asensio, A. Resta, B. Ealet, and G. Le Lay, Phys. Rev. Lett. **108**, 155501 (2012).

$^{5}$ D. Chiappe, C. Grazianetti, G. Tallarida, M. Fanciulli, and A. Molle, Adv. Mater. **24**, 5088 (2012), 0811.4412.

$^{6}$ D. Chiappe, E. Scalise, E. Cinquanta, C. Grazianetti, B. Van Den Broek, M. Fanciulli, M. Houssa, and A. Molle, Adv. Mater. **26**, 2096 (2014).

$^{7}$ E. Bianco, S. Butler, S. Jiang, O. D. Restrepo, W. Windl, and J. E. Goldberger, ACS Nano **7**, 4414 (2013).

$^{8}$ M. Derivaz, D. Dentel, R. Stephan, M.-C. Hanf, A. Mehdaoui, P. Sonnet, and C. Pirri, Nano Lett. **15**, 2510 (2015).

$^{9}$ F.-f. Zhu, W.-j. Chen, Y. Xu, C.-l. Gao, D.-d. Guan, C.-h. Liu, D. Qian, S.-C. Zhang, and J.-f. Jia, Nat. Mater. **14**, 1020 (2015).

$^{10}$ S. Zhang, Z. Yan, Y. Li, Z. Chen, and H. Zeng, Angew. Chem. Int. Edit. **54**, 3112 (2015).

$^{11}$ A. Takayama, T. Sato, S. Souma, T. Oguchi, and T. Taka- hashi, Phys. Rev. Lett. **114**, 66402 (2015).

$^{12}$ I. K. Drozdov, A. Alexandradinata, S. Jeon, S. Nadj-Perge, H. Ji, R. J. Cava, B. Andrei Bernevig, and A. Yazdani, Nat. Phys. **10**, 664 (2014).

$^{13}$ X. Li, H. Liu, H. Jiang, F. Wang, and J. Feng, Phys. Rev. B **90**, 165412 (2014).

$^{14}$ Z. Liu, C.-X. Liu, Y.-S. Wu, W.-H. Duan, F. Liu, and J. Wu, Phys. Rev. Lett. **107**, 136805 (2011).

$^{15}$ F. Yang, L. Miao, Z. F. Wang, M.-Y. Yao, F. Zhu, Y. R. Song, M.-X. Wang, J.-P. Xu, A. V. Fedorov, Z. Sun, G. B. Zhang, C. Liu, F. Liu, D. Qian, C. L. Gao, and J.-F. Jia, Phys. Rev. Lett. **109**, 16801 (2012).

$^{16}$ T. Hirahara, G. Bihlmayer, Y. Sakamoto, M. Yamada, H. Miyazaki, S.-i. Kimura, S. Blügel, and S. Hasegawa, Phys. Rev. Lett. **107**, 166801 (2011).

$^{17}$ T. Hirahara, N. Fukui, T. Shirasawa, M. Yamada, M. Ai- tani, H. Miyazaki, M. Matsunami, S. Kimura, T. Taka- hashi, S. Hasegawa, and K. Kobayashi, Phys. Rev. Lett. **109**, 227401 (2012).

$^{18}$ J. L. Zhang, S. Zhao, C. Han, Z. Wang, S. Zhong, S. Sun, R. Guo, X. Zhou, C. D. Gu, K. D. Yuan, Z. Li, and W. Chen, Nano Lett. **16**, 4903 (2016).

$^{19}$ S. H. Zhang, J. Zhou, Q. Wang, X. S. Chen, Y. Kawazoe, and P. Jena, Proc. Nat. Acad. Sci. USA **112**, 2372 (2015).

$^{20}$ Y. Liu, G. Wang, Q. Huang, L. Guo, and X. Chen, Phys. Rev. Lett. **108**, 225505 (2012).

$^{21}$ Z. Wang, X.-F. Zhou, X. Zhang, Q. Zhu, H. Dong, M. Zhao, and A. R. Oganov, Nano Lett. **15**, 6182 (2015).

$^{22}$ B. G. Kim and H. J. Choi, Phys. Rev. B **86**, 115435 (2012).

$^{23}$ A. Wang, L. Li, X. Wang, H. Bu, and M. Zhao, Diam. Relat. Mater. **41**, 65 (2014).

$^{24}$ L. Kou, X. Tan, Y. Ma, H. Tahini, L. Zhou, Z. Sun, D. Ai- jun, C. Chen, and S. C. Smith, 2D Mater. **2**, 45010 (2015).

$^{25}$ P. Li and W. Luo, Sci. Rep. **6**, 25423 (2016).

$^{26}$ X.-L. Qi and S.-C. Zhang, Rev. Mod. Phys. **83**, 1057 (2011).

$^{27}$ M. Z. Hasan and C. L. Kane, Rev. Mod. Phys. **82**, 3045 (2010).

$^{28}$ B. A. Bernevig and S.-C. Zhang, Phys. Rev. Lett. **96**, 106802 (2006).

$^{29}$ C. L. Kane and E. J. Mele, Phys. Rev. Lett. **95**, 226801 (2005).

$^{30}$ Y. Yao, F. Ye, X.-L. Qi, S.-C. Zhang, and Z. Fang, Phys. Rev. B **75**, 41401 (2007).

$^{31}$ B. A. Bernevig, T. L. Hughes, and S.-C. Zhang, Science **314**, 1757 (2006).

$^{32}$ I. Knez, R.-R. Du, and G. Sullivan, Phys. Rev. Lett. **107**, 136603 (2011).

$^{33}$ M. König, S. Wiedmann, C. Brüne, A. Roth, H. Buhmann, L. W. Molenkamp, X.-L. Qi, and S.-C. Zhang, Science **318**, 766 (2007).

$^{34}$ L. Li, X. Zhang, X. Chen, and M. Zhao, Nano Lett. **15**, 1296 (2015).

$^{35}$ X. Chen, L. Li, and M. Zhao, Phys. Chem. Chem. Phys. **17**, 16624 (2015).

$^{36}$ X. Chen, L. Li, and M. Zhao, RSC Adv. **5**, 72462 (2015).

$^{37}$ M. Zhao, X. Zhang, and L. Li, Sci. Rep. **5**, 16108 (2015).

$^{38}$ M. Zhao, X. Chen, L. Li, and X. Zhang, Sci. Rep. **5**, 8441 (2015).

$^{39}$ Z. Song, C.-C. Liu, J. Yang, J. Han, M. Ye, B. Fu, Y. Yang, Q. Niu, J. Lu, and Y. Yao, NPG Asia. Mater. **6**, e147 (2014).

$^{40}$ C.-C. Liu, S. Guan, Z. Song, S. A. Yang, J. Yang, and Y. Yao, Phys. Rev. B **90**, 85431 (2014).

$^{41}$ R.-w. Zhang, C.-w. Zhang, W.-x. Ji, P. Li, and P.-j. Wang, arXiv preprint arXiv:1607.03568 (2016).

$^{42}$ G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).

$^{43}$ G. Kresse and J. Hafner, Phys. Rev. B **48**, 13115 (1993).

$^{44}$ G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

$^{45}$ J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

$^{46}$ A. Togo and I. Tanaka, Scripta Mater. **108**, 1 (2015), 1506.08498.

$^{47}$ A. A. Soluyanov and D. Vanderbilt, Phys. Rev. B **83**, 235401 (2011).

$^{48}$ R. Yu, X. L. Qi, A. Bernevig, Z. Fang, and X. Dai, Phys. Rev. B **84**, 75119 (2011).

$^{49}$ D. Gresch, G. Autès, O. V. Yazyev, M. Troyer, D. Vander- bilt, B. A. Bernevig, and A. A. Soluyanov, arXiv preprint arXiv:1610.08983 (2016).

$^{50}$ A. A. Mostofi, J. R. Yates, G. Pizzi, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, Comput. Phys. Commun. **185**, 2309 (2014).

$^{51}$ M. P. L. Sancho, J. M. L. Sancho, J. M. L. Sancho, and J. Rubio, J. Phys. F **15**, 851 (1985).

$^{52}$ Q. S. Wu and S. N. Zhang, https://github.com/quanshengwu/wannier_tools.

$^{53}$ L. Fu and C. L. Kane, Phys. Rev. B **76**, 045302 (2007).

$^{54}$ L. Li, O. Leenaerts, X. Kong, X. Chen, M. Zhao, and F. M. Peeters, arXiv preprint arXiv:1609.06790 (2016).

$^{55}$ L. Chen, Z. F. Wang, and F. Liu, Phys. Rev. B **87**, 235420 (2013).