PHYSICAL REVIEW B 101, 184504 (2020)

# $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs): Iron-based superconducting analog of the cuprates

Xinlei Zhao, $^1$ Fengjie Ma $\odot$, $^{1,*}$ Zhong-Yi Lu, $^2$ and Tao Xiang$^{3,4}$

$^1$The Center for Advanced Quantum Studies and Department of Physics, Beijing Normal University, Beijing 100875, China
$^2$Department of Physics, Renmin University of China, Beijing 100872, China
$^3$Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China
$^4$School of Physical Sciences, University of Chinese Academy of Sciences, Beijing 100049, China

![](./images/812641355263115265_1.jpg)
(Received 14 October 2019; revised manuscript received 24 January 2020; accepted 20 April 2020; published 6 May 2020)

It has long been a challenging task to find compounds with similar crystal and electronic structures as cuprate superconductors with low dimensionality and strong antiferromagnetic fluctuations. The parent compounds of cuprate superconductors are Mott insulators with strong in-plane antiferromagnetic exchange interactions between Cu moments. Here, we show, based on first-principles density functional calculations, that $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs) exhibit many of the physical properties common to the cuprate parent compounds: (1) The FeSe$_2$ layer in $A$FeSe$_2$ is similar in crystalline and electronic structures to the CuO$_2$ plane in cuprates, although Se atoms are not coplanar to the square Fe lattice; (2) they are antiferromagnetic insulators, but with relatively small charge excitation gaps; (3) their ground states are Néel antiferromagnetic ordered, similar as in cuprates; and (4) the antiferromagnetic exchange interactions between Fe moments are larger than in other iron-based superconducting materials, but comparable to those in cuprates. As cuprates, these compounds may become high-$T_c$ superconductors upon doping of charge carriers either by chemical substitution or intercalation or by liquid or solid gating.

DOI: 10.1103/PhysRevB.101.184504

## I. INTRODUCTION

The discovery of both copper oxide (cuprate) and iron-based (iron pnictide or iron chalcogenide) high-temperature superconductivity has spurred enormous interests in the investigation of high-$T_c$ pairing mechanisms, and in the exploration of new high-$T_c$ materials and their applications. Both cuprate and iron-based superconductors are quasi-two- dimensional materials with strong antiferromagnetic fluctuations. Superconductivity emerges by doping holes or electrons to the parent compounds of these materials [1,2]. The parent compounds of cuprate superconductors are antiferromagnetic Mott insulators [3–5]. On the contrary, the parent compounds of iron-based superconductors are mostly semimetals [2,6–9]. These compounds, except for FeSe, LiFeAs, and ThFeAsN, also exhibit collinear, bicollinear, or blocked-type antiferromagnetic orders [10–19].

Cuprate superconductors still hold the record for the highest critical temperature at ambient pressure. They consist of copper-oxygen (CuO$_2$) planes separated by charge reservoir layers. At each copper-oxygen layer, Cu atoms form a square lattice and O atoms are located at the coplanar decorated sites of the square lattice. The low-energy physics of cuprate superconductors is governed by the strongly hybridized Cu $3d_{x^2-y^2}$ and O $2p_x$ or $2p_y$ orbitals. This hybridization mediates a strong antiferromagnetic superexchange interaction between Cu$^{2+}$ spins, which plays a central role in the pairing mechanism of high-$T_c$ superconductivity. A rule of thumb is that the superconducting transition temperature is positively correlated with this antiferromagnetic interaction [20,21].

Iron-based superconductors, on the other hand, contain FeAs or FeSe layers. Fe atoms in each layer also form a square lattice, but As or Se atoms are located at the middle of each square either above or below the Fe layer. In these materials, besides the As or Se mediated antiferromagnetic interaction between the next-nearest-neighboring Fe ions [10], there is also a direct exchange interaction between the two nearest-neighboring Fe ions, which is often ferromagneticlike. The dominant antiferromagnetic coupling constants in these materials are about half of the corresponding values in cuprates [10,16,17,22–25]. It suggests that the antiferromagnetic fluctuation or correlation is relatively weaker in iron-based superconductors. Moreover, the competition between nearest- and next-nearest-neighboring magnetic interactions introduces frustration, which may also weaken the magnetic correlation.

During the past decades, great efforts have been made to find superconducting materials similar in structure to cuprates but without copper. A typical example is Sr$_2$RuO$_4$, which is a bulk superconductor below roughly 2 K [26]. Superconducting coherence peaks were also observed in the tunneling spectrum of surface electron-doped Sr$_2$IrO$_4$ [27], although zero resistance has not been observed. Sr$_2$IrO$_4$ shows many similarities with cuprates, but its antiferromagnetic correlation is dominated by the spin-orbit coupling, which is also smaller than the superexchange interaction in cuprates [28–30]. Recently, superconducting condensation was observed in hole-doped infinite-layer nickelate, Nd$_{0.8}$Sr$_{0.2}$NiO$_2$, below 9–15 K [31]. NdNiO$_2$ is isostructural to the infinite-layer parent

*fengjie.ma@bnu.edu.cn

2469-9950/2020/101(18)/184504(6)
184504-1
©2020 American Physical Society

![](./images/812641355263115265_2.jpg)

FIG. 1. (a) Tetragonal unit cell of $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs) with $I\overline{4}m2$ symmetry (space group No. 119). (b) Schematic top view of the FeSe$_2$ layer. $J_1$, $J_2$, and $J_3$ are the magnetic coupling constants between the first-, second-, and third-nearest-neighboring Fe moments, respectively. $a$, $b$, and $c$ are the principal axes of the crystal. $a'$ and $b'$ are the axes along the diagonal directions in the square Fe lattice.

cuprates. However, it lacks a strong covalent character between Ni and ligand O atoms, which would imply that spin fluctuations are absent or considerably diminished in these nickelate materials. Indeed, antiferromagnetic long-range order is not observed in NdNiO$_2$ [31,32].

In this paper, we show, based on first-principles density functional calculations, that ternary iron selenides $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs) with $I\overline{4}m2$ symmetry (space group No. 119) are ideal compounds similar in structure to the parent compounds of cuprate superconductors. Specifically, these compounds have tetragonal FeSe$_2$ layers, similar in structure to the CuO$_2$ planes of cuprates except that the Se atoms are located alternately above and below the square Fe lattice, as shown in Fig. 1. More importantly, $A$FeSe$_2$ have also similar electronic properties to cuprates. First, there exist strong antiferromagnetic superexchange interactions between Fe magnetic moments, about $115\ \text{meV}/S^2$ ($S$ is the value of the effective spin of the Fe ion), which are comparable to the corresponding values in cuprates [24,25]. Second, as cuprates, $A$FeSe$_2$ are Néel antiferromagnetic insulators. But the charge excitation gaps are about one to two orders of magnitude smaller than in cuprates. These similarities suggest that $A$FeSe$_2$ have a strong chance to become high-$T_c$ superconductors upon hole or electron doping.

## II. COMPUTATIONAL DETAILS

$A$FeSe$_2$ have a number of stable structures, which include the structures with space groups of $I\overline{4}m2$ [33,34] and $C2/m$ [35] for TlFeSe$_2$, $C2/c$ for KFeSe$_2$ and RbFeSe$_2$ [36], and $C2/m$ for CsFeSe$_2$ [37]. Among these structures, only $I\overline{4}m2$ contains the quasi-two-dimensional FeSe$_2$ layers studied in this paper. Compounds with $C2/c$ or $C2/m$ structures are quasi-one-dimensional materials [35–39].

In our calculations, the plane-wave basis method and QUANTUM ESPRESSO software package were used [40]. The ultrasoft pseudopotentials with the generalized gradient approximation (GGA) of the Perdew-Burke-Ernzerhof formula for the exchange-correlation potentials were adopted [41,42].

<table>
<caption>Table I. Optimized lattice constants (in units of Å) of $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs) in the Néel antiferromagnetic ground state. The magnetic unit cell is doubled in comparison with the crystal unit cell, and the principal axes change to $a'$ and $b'$.</caption>
<thead>
<tr>
<th>$A$FeSe$_2$</th>
<th>$a'$</th>
<th>$b'$</th>
<th>$c$</th>
</tr>
</thead>
<tbody>
<tr>
<td>TlFeSe$_2$</td>
<td>5.473</td>
<td>5.451</td>
<td>13.424</td>
</tr>
<tr>
<td>KFeSe$_2$</td>
<td>5.536</td>
<td>5.529</td>
<td>13.205</td>
</tr>
<tr>
<td>RbFeSe$_2$</td>
<td>5.601</td>
<td>5.596</td>
<td>13.715</td>
</tr>
<tr>
<td>CsFeSe$_2$</td>
<td>5.662</td>
<td>5.658</td>
<td>14.350</td>
</tr>
</tbody>
</table>

After the full convergence test, the kinetic energy cutoff for wave functions and charge density were chosen to be 960 and 7720 eV, respectively. The Marzari-Vanderbilt broadening technique [43] was used. For the density of states calculations, a mesh of $28 \times 28 \times 28$ $k$ points and the tetrahedra method were used. All of the lattice parameters were optimized until the force on each atom was smaller than $0.001\ \text{eV}/\mathring{\text{A}}$ and the total pressure was smaller than 0.1 kbar. Parameter-free $ab$ initio calculations with the recently developed strongly constrained and appropriately normed (SCAN) meta-GGA exchange-correlation functional [44], which has been demonstrated to be able to give an accurate treatment of the antiferromagnetic ground state and estimate of exchange coupling in La$_2$CuO$_4$ without invoking any free parameters such as the Hubbard $U$ [45], were also performed for crossing check, especially the gap value and coupling strength.

## III. RESULTS AND DISCUSSIONS

Similar to the parent compounds of cuprate superconductors, we find that $A$FeSe$_2$ ($A$ = Tl, K, Rb, or Cs) are Néel antiferromagnetic insulators. The insulating gaps are about 22, 22, 56, and 98 meV for TlFeSe$_2$, KFeSe$_2$, RbFeSe$_2$, and CsFeSe$_2$, respectively. The gap value becomes slightly larger, e.g., $\sim 100\ \text{meV}$ for TlFeSe$_2$, using the more advanced SCAN meta-GGA scheme [44]. These gap values are about one to two orders of magnitude smaller than in cuprates. (The spin-orbit coupling effect has also been checked, which does not affect the results listed.) The ordering moment of each Fe ion is $\sim 3.6\mu_B$. Table I shows the optimized lattice constants for $A$FeSe$_2$ in the Néel antiferromagnetic state. Since the unit cell is doubled due to the antiferromagnetic long-range order, the corresponding principal axes change from $a$ and $b$ to $a'$ and $b'$, namely, along the two diagonal directions of the square Fe lattice. After dividing $a'$ and $b'$ by a factor of $\sqrt{2}$, we find that the calculated lattice constants agree very well with the experimental data for TlFeSe$_2$ [33,34]. There is a weak magnetic coupling between different Fe layers. This leads to a Peierls-like distortion [46] which lifts the degeneracy between the $a'$- and $b'$-axis lattice constants. The lattice constant becomes slightly larger in the direction ($a'$ axis) along which the interlayer spins are antiparallel aligned, than the direction ($b'$ axis) along which the interlayer spins are parallel aligned. However, the difference between $a'$ and $b'$ is very small, which is difficult to be detected experimentally.

Figure 2(a) shows the electronic band structure of TlFeSe$_2$ in the Néel antiferromagnetic ground state. There is an indirect energy gap $\sim 22\ \text{meV}$ from $\Gamma$ to $E/D$ between the valence

![](./images/812641355263115265_3.jpg)

FIG. 2. Electronic structure of TlFeSe₂ in the Néel antiferromagnetic state. (a) Band structure; the Fermi energy (the top of valence band) is set to zero. (b), (c) Charge and spin density distributions along one of the Fe-Se-Fe directions in an FeSe₂ layer, respectively. The charge and spin density distributions along the other Fe-Se-Fe direction are similar, except that Se atoms are located above the Fe-Fe layer. In (b), yellow and pink colors represent the contributions from Se and Fe atoms, respectively. The isosurface is 0.05 $e/$bohr³. In (c), blue and pink colors represent different spin polarizations. The isosurface is 0.0045 $e/$bohr³.

![](./images/812641355263115265_4.jpg)

FIG. 3. (a) Total and orbital-resolved partial density of states of up-spin electrons, and (b) projected density of states of Fe $3d$ orbitals in the Néel antiferromagnetic state for TlFeSe₂.

and conduction bands. From the result of orbital-resolved partial density of states, as shown in Fig. 3(a), we find that the bands around the Fermi level contribute mainly by Fe $3d$ and Se $4p$ electrons. More specifically, the conduction band is predominantly contributed by Fe $3d$ orbitals, while the valence band is contributed mainly by Se $4p$ orbitals. Tl layers serve as a charge reservoir in the compound.

In cuprates, six oxygen atoms surrounding a Cu atom form an octahedra. The crystal field generated by this octahedra splits Cu $3d$ orbitals into a threefold degenerate $t_{2g}$ level, containing $(3d_{xy}, 3d_{xz}, 3d_{yz})$ orbitals, and a twofold degenerate $e_{g}$ level, containing $(3d_{x^2-y^2}, 3d_{z^2})$ orbitals. If the octahedra is elongated along the $c$ axis by the Jahn-Teller effect, the $e_{g}$ orbital is further separated into two levels, which lifts the Cu $3d_{x^2-y^2}$ orbital to the top of the valence bands. $Cu^{2+}$ carries an effective $S=1/2$ magnetic moment because this $3d_{x^2-y^2}$ orbital is just half filled. Moreover, there is a strong hybridization between Cu $3d_{x^2-y^2}$ and O $2p_x$ or $2p_y$ orbitals. Upon hole doping, this hybridization, together with the strong on-site Coulomb repulsion, tends to bound a Cu spin with an O hole, forming a Zhang-Rice spin singlet state [47].

In $A$FeSe₂, each Fe is surrounded by four Se atoms. These four Se atoms impose a tetrahedral crystal field on Fe, which reverses the energetic order of $t_{2g}$ and $e_{g}$ orbitals. In this case, $t_{2g}$ has a higher energy than $e_{g}$. However, the crystal-field splitting imposed on Fe by Se atoms is relatively small in comparison with the Hund's coupling. As a result, in the ground state, as shown in Fig. 3(b), the five Fe up-spin orbitals are almost completely filled while the five Fe down-spin orbitals are all partially occupied. Thus each Fe ion possesses a large magnetic moment.

Figures 2(b) and 2(c) show respectively the charge and spin density distributions around Fe and Se atoms for TlFeSe₂. Similar charge and spin distributions have also been found in other $A$FeSe₂ compounds. As expected, the magnetic moment is concentrated mainly around each Fe ion. The large overlap between the electronic cloud of Fe and that of Se suggests that there is a strong hybridization between Se $4p$ and Fe $3d$ orbitals along the direction connecting Fe and Se atoms. On the other hand, the direct wave-function overlap between two neighboring Fe is negligibly small. This is different than in other Fe-based superconducting materials [10,11,17,48]. This suggests that, similar as in cuprate superconductors, the magnetic coupling between Fe spins results predominantly from the Se-bridged superexchange interaction [10], and the direct magnetic coupling between two Fe moments is negligible.

To quantify the magnetic interactions, we model the low-energy state by an extended Heisenberg model with the first-, second-, and third-nearest-neighboring interactions [10,22],

$$
H = \sum_{ij} \big(J_1\delta_{\langle i,j\rangle_1} + J_2\delta_{\langle i,j\rangle_2} + J_3\delta_{\langle i,j\rangle_3}\big)\vec{S}_i \cdot \vec{S}_j, \tag{1}
$$

where $\langle i, j\rangle_n$ ($n=1,2,3$) means that $j$ is one of the $n$th-nearest neighbors of $i$.

Assuming that the energy differences between different magnetic states result purely from the magnetic exchange

<table>
<caption>TABLE II. Magnetic coupling constants (in units of meV/S²) of $A$FeSe₂ ($A$ = Tl, K, Rb, or Cs).</caption>
<tbody><tr>
<td>$A$FeSe₂</td>
<td>$J_1$</td>
<td>$J_2$</td>
<td>$J_3$</td>
</tr>
<tr>
<td>TlFeSe₂</td>
<td>115.01</td>
<td>9.29</td>
<td>10.92</td>
</tr>
<tr>
<td>KFeSe₂</td>
<td>115.00</td>
<td>6.04</td>
<td>9.29</td>
</tr>
<tr>
<td>RbFeSe₂</td>
<td>115.75</td>
<td>7.62</td>
<td>15.96</td>
</tr>
<tr>
<td>CsFeSe₂</td>
<td>115.62</td>
<td>8.62</td>
<td>14.79</td>
</tr>
</tbody>
</table>

couplings between Fe local moments, the coupling constants $J_1$, $J_2$, and $J_3$ [Fig. 1(b)] can be determined by evaluating the energies of ferromagnetic, Néel antiferromagnetic, collinear antiferromagnetic, and bicollinear antiferromagnetic ordered states at each FeSe₂ layer. The results are shown in Table II. The dominant interaction is the nearest-neighboring Heisenberg interaction, i.e., the $J_1$ term. For all the four compounds we have studied, $J_1$ is found to be about 115 meV/S², comparable to the corresponding value in cuprates [24,25] and about two times larger than the values of other typical iron-based superconductors [10,22]. The value is independent of the methods adopted, e.g., it is about 112 meV/S² using the SCAN meta-GGA scheme [44]. $J_2$ is comparable to $J_3$. But both $J_2$ and $J_3$ are one order of magnitude smaller than $J_1$.

We have also calculated the electronic and phonon structures of $A$FeSe₂ in the nonmagnetic states. Without antiferromagnetic long-range order, these compounds become metallic. The total energy difference between the Néel AFM ground state and the nonmagnetic state is large, $\sim$0.713 eV/Fe. As shown in Figs. 4(b) and 4(c), there are four bands across the Fermi level. Among them, three are electron types whose Fermi-surface sheets are located at the corners of Brillouin zone, and one is a hole type with a surface around the high-symmetry $k$ point $\Sigma$. These four bands are quasi-two-dimensional-like. Their energy dispersions along the $c$ axis are small in comparison with the in-plane ones, similar as in cuprate superconducting materials. A scrutiny of the Fermi-surface structures indicates that there is no commensurate vector connecting the electron-type Fermi-surface sheets with the hole-type one, hence no Fermi-surface nesting.

We have also examined the lattice dynamic instability of TlFeSe₂ by calculating the phonon spectra in the nonmagnetic state using density functional perturbation theory [40]. Figure 4(a) shows the phonon energy dispersion and the corresponding density of states. There is no negative or imaginary phonon frequency along any high-symmetry direction. This indicates that the tetragonal TlFeSe₂ lattice is chemically stable, in agreement with the fact that this compound has been successfully synthesized in a laboratory [33,34].

The above discussion shows that $A$FeSe₂ share many common properties of the parent compounds of cuprate superconductors. First, the FeSe₂ layer is similar in structure to the CuO₂ plane in cuprates, although Se atoms are not coplanar to the square lattice of Fe atoms. Second, there is a strong Se $4p$ orbital mediated superexchange interaction between Fe magnetic moments, similar as in cuprates where the superexchange interaction between Cu spins mediated by O $2p$ orbitals plays a crucial role in the high-$T_c$ superconductivity. Moreover, the nearest-neighbor exchange coupling constant $J_1$ is larger than in other iron-based superconductors, but is of the same order as in cuprates. Third, the ground states of both $A$FeSe₂ and the parent compounds of cuprate superconductors are Néel antiferromagnetic ordered. These similarities suggest that $A$FeSe₂ are perfect candidates of high-$T_c$ superconducting parent compounds. Upon hole or electron doping, either by chemical substitutions or intercalations or by liquid or solid gating, they may become superconducting.

However, the antiferromagnetic insulating gaps of $A$FeSe₂ are about one to two orders of magnitude smaller than in cuprates, which implies that $A$FeSe₂ may be even more tunable than cuprate superconductors. Thus it is highly feasible to suppress the charge excitation gaps of $A$FeSe₂, for example, by chemical doping, pressure, or ion gating, and drive it into a superconducting phase.

In cuprates, it is believed that strong antiferromagnetic fluctuations play an important role in gluing electrons, and the superconducting gap has $d_{x^2-y^2}$-wave pairing symmetry. In doped $A$FeSe₂, it is likely that strong antiferromagnetic fluctuations would also serve as the main driving force of superconductivity. However, the superconducting gap in doped $A$FeSe₂ may not have a simple $d$ wave or other pairing symmetry, because nonmagnetic states of $A$FeSe₂ are multiband systems. The pairing symmetry is determined not just by the pairing interaction, but also by the Fermi-surface structures. It is the interplay of these two effects that determines the symmetry of the gap function and its sign structures on the Fermi surfaces [49]. In a multiband system, if the dominant interaction between two bands in the particle-particle channel is repulsive, then the gap functions of these two bands tend to take opposite signs. On the other hand, if the dominant interband interaction is attractive, then the gap functions of these two bands tend to take the same sign.

![](./images/812641355263115265_5.jpg)

FIG. 4. (a) Energy dispersion of phonons (left panel) and the corresponding density of states (right panel) for TlFeSe₂. (b) Electronic band structure and (c) the Fermi surface contours for TlFeSe₂ in the nonmagnetic state. The Fermi energy is set to zero.

## IV. CONCLUSION

In summary, we have provided strong theoretical arguments, based on first-principles density functional calculations, to show that doped ternary iron selenides, $AFeSe_2$, are good candidates for high-$T_c$ superconductors. These cuprate analogs of Fe-based superconductors, if successfully synthesized, would serve as a unique platform to bridge the gap between cuprate and Fe-based superconductors, and to understand the pairing mechanism in both materials, leading to a unified theory of high-$T_c$ superconductivity.

## ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China under Grants No. 11674027 and No. 11888101, and the National Key Research and Development Project of China under Grant No. 2017YFA0302901.

[1] J. G. Bednorz and K. A. Müller, *Z. Phys. B* **64**, 189 (1986).
[2] Y. Kamihara, T. Watanabe, M. Hirano, and H. Hosono, *J. Am. Chem. Soc.* **130**, 3296 (2008).
[3] D. Vaknin, S. K. Sinha, D. E. Moncton, D. C. Johnston, J. M. Newsam, C. R. Safinya, and H. E. King, *Phys. Rev. Lett.* **58**, 2802 (1987).
[4] J. M. Tranquada, D. E. Cox, W. Kunnmann, H. Moudden, G. Shirane, M. Suenaga, P. Zolliker, D. Vaknin, S. K. Sinha, M. S. Alvarez, A. J. Jacobson, and D. C. Johnston, *Phys. Rev. Lett.* **60**, 156 (1988).
[5] P. A. Lee, N. Nagaosa, and X.-G. Wen, *Rev. Mod. Phys.* **78**, 17 (2006).
[6] M. Rotter, M. Tegel, and D. Johrendt, *Phys. Rev. Lett.* **101**, 107006 (2008).
[7] X. C. Wang, Q. Q. Liu, Y. X. Lv, W. B. Gao, L. X. Yang, R. C. Yu, F. Y. Li, and C. Q. Jin, *Solid State Commun.* **148**, 538 (2008).
[8] F.-C. Hsu, J.-Y. Luo, K.-W. Yeh, T.-K. Chen, T.-W. Huang, P. M. Wu, Y.-C. Lee, Y.-L. Huang, Y.-Y. Chu, D.-C. Yan, and M.-K. Wu, *Proc. Natl. Acad. Sci. USA* **105**, 14262 (2008).
[9] J. Guo, S. Jin, G. Wang, S. Wang, K. Zhu, T. Zhou, M. He, and X. Chen, *Phys. Rev. B* **82**, 180520(R) (2010).
[10] F. Ma, Z.-Y. Lu, and T. Xiang, *Phys. Rev. B* **78**, 224517 (2008).
[11] F. Ma, W. Ji, J. Hu, Z.-Y. Lu, and T. Xiang, *Phys. Rev. Lett.* **102**, 177003 (2009).
[12] C. de la Cruz, Q. Huang, J. W. Lynn, J. Li, W. Ratcliff II, J. L. Zarestky, H. A. Mook, G. F. Chen, J. L. Luo, N. L. Wang, and P. Dai, *Nature (London)* **453**, 899 (2008).
[13] S. Li, C. de la Cruz, Q. Huang, Y. Chen, J. W. Lynn, J. Hu, Y.-L. Huang, F.-C. Hsu, K.-W. Yeh, M.-K. Wu, and P. Dai, *Phys. Rev. B* **79**, 054503 (2009).
[14] X.-W. Yan, M. Gao, Z.-Y. Lu, and T. Xiang, *Phys. Rev. B* **83**, 233205 (2011).
[15] C. Cao and J. Dai, *Phys. Rev. Lett.* **107**, 056401 (2011).
[16] X. W. Yan, M. Gao, Z. Y. Lu, and T. Xiang, *Phys. Rev. Lett.* **106**, 087005 (2011).
[17] Z.-Y. Lu, F. Ma, and T. Xiang, *J. Phys. Chem. Solids* **72**, 319 (2011).
[18] J. H. Tapp, Z. Tang, B. Lv, K. Sasmal, B. Lorenz, P. C. W. Chu, and A. M. Guloy, *Phys. Rev. B* **78**, 060505(R) (2008).
[19] T. Shiroka, T. Shang, C. Wang, G.-H. Cao, I. Eremin, H.-R. Ott, and J. Mesot, *Nat. Commun.* **8**, 156 (2017).
[20] D. Muñoz, F. Illas, and I. de P. R. Moreira, *Phys. Rev. Lett.* **84**, 1579 (2000).
[21] X. Wan, T. A. Maier, and S. Y. Savrasov, *Phys. Rev. B* **79**, 155114 (2009).
[22] F. Ma, Z.-Y. Lu, and T. Xiang, *Front. Phys. China* **5**, 150 (2010).
[23] X.-W. Yan, M. Gao, Z.-Y. Lu, and T. Xiang, *Phys. Rev. B* **84**, 054502 (2011).
[24] M. R. Norman and C. Pépin, *Rep. Prog. Phys.* **66**, 1547 (2003).
[25] D. Reznik, P. Bourges, H. F. Fong, L. P. Regnault, J. Bossy, C. Vettier, D. L. Milius, I. A. Aksay, and B. Keimer, *Phys. Rev. B* **53**, R14741 (1996).
[26] Y. Maeno, H. Hashimoto, K. Yoshida, S. Nishizaki, T. Fujita, J. G. Bednorz, and F. Lichtenberg, *Nature (London)* **372**, 532 (1994).
[27] Y. J. Yan, M. Q. Ren, H. C. Xu, B. P. Xie, R. Tao, H. Y. Choi, N. Lee, Y. J. Choi, T. Zhang, and D. L. Feng, *Phys. Rev. X* **5**, 041018 (2015).
[28] J. Kim, D. Casa, M. H. Upton, T. Gog, Y.-J. Kim, J. F. Mitchell, M. van Veenendaal, M. Daghofer, J. van den Brink, G. Khaliullin, and B. J. Kim, *Phys. Rev. Lett.* **108**, 177003 (2012).
[29] B. H. Kim, G. Khaliullin, and B. I. Min, *Phys. Rev. Lett.* **109**, 167205 (2012).
[30] F. Wang and T. Senthil, *Phys. Rev. Lett.* **106**, 136402 (2011).
[31] D. Li, K. Lee, B. Y. Wang, M. Osada, S. Crossley, H. R. Lee, Y. Cui, Y. Hikita, and H. Y. Hwang, *Nature (London)* **572**, 624 (2019).
[32] M. A. Hayward and M. J. Rosseinsky, *Solid State Sci.* **5**, 839 (2003).
[33] A. Kutoglu, *Naturwissenschaften* **61**, 125 (1974).
[34] G. D. Guseinov, F. M. Seidov, S. N. Dzhuraev, and E. M. Kerimova, *Inorg. Mater. (USSR)* **27**, 377 (1991) [Izv. Akad. Nauk SSSR, Neorg. Mater. **27**, 467 (1991)].
[35] K. Klepp and H. Boller, *Monatsh. Chem.* **110**, 1045 (1979).
[36] W. Bronger, A. Kyas, and P. Müller, *J. Solid State Chem.* **70**, 262 (1987).
[37] P. Stüble and C. Röhr, *Z. Anorg. Allg. Chem.* **643**, 1462 (2017).
[38] Z. Seidov, H.-A. Krug von Nidda, J. Hemberger, A. Loidl, G. Sultanov, E. Kerimova, and A. Panfilov, *Phys. Rev. B* **65**, 014433 (2001).
[39] E. B. Asgerov, N. T. Dang, A. I. Beskrovnyy, A. I. Madadzada, D. I. Ismayilov, R. N. Mehdiyeva, S. H. Jabarov, and E. M. Karimova, *Semiconductors* **49**, 879 (2015).
[40] P. Giannozzi *et al.*, *J. Phys.: Condens. Matter* **21**, 395502 (2009).
[41] D. Vanderbilt, *Phys. Rev. B* **41**, 7892 (1990).
[42] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).
184504-5

[43] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Phys. Rev. Lett. 82, 3296 (1999).

[44] J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. 115, 036402 (2015).

[45] C. Lane, J. W. Furness, I. G. Buda, Y. Zhang, R. S. Markiewicz, B. Barbiellini, J. Sun, and A. Bansil, Phys. Rev. B 98, 125140 (2018).

[46] M. Hase, I. Terasaki, and K. Uchinokura, Phys. Rev. Lett. 70, 3651 (1993).

[47] F. C. Zhang and T. M. Rice, Phys. Rev. B 37, 3759 (1988).

[48] T. Yildirim, Phys. Rev. Lett. 102, 037003 (2009).

[49] J. M. Wheatley and T. Xiang, Solid State Commun. 88, 593 (1993).