# Cluster Structures and Stabilities from Solid-state Potentials
## Application to Silicon Clusters

Sidian Li,† Roy L. Johnston and John N. Murrell*
School of Chemistry and Molecular Sciences, University of Sussex, Falmer, Brighton BN1 9QJ, UK

An empirical potential-energy function comprising two- and three-body terms, whose parameters have been determined from the properties of solid silicon, is used to study the structures and energies of silicon micro-clusters. For small clusters, densely packed (non-diamond) structures are found which are in broad agreement with *ab initio* calculations. For larger clusters, optimisations starting from fragments of the cubic bulk solids indicate that close-packed structures are favoured initially and that diamond structures become relatively more stable only for clusters of well above 100 atoms.

In recent papers, $^{1–4}$ we have proposed a new potential-energy function for elemental solids and have shown that its parameters may be determined by fitting phonon and elastic constant data and the lattice energies and lattice constants of one or more crystalline phase. To date, the method has only been used to study cubic systems but our potential function should be generally applicable.

Our objective is to obtain potentials which are applicable to the study of surfaces, defects, amorphous solids, liquids and clusters, as well as to bulk crystalline solids. To achieve this our potentials must be valid over a wide range of coordination numbers and geometries and we have therefore reproduced the properties of as many crystal structures as possible. Thus, the silicon potential used in this paper has been fitted to phonon and elastic constant data of the most stable (diamond) structure and, in addition, to the cohesive energies and lattice spacings of the face-centred cubic (f.c.c.), body centred cubic (b.c.c.) and simple cubic (s.c.) structures as calculated by first-principles pseudopotential methods by Cohen and co-workers.⁵ These calculations have been shown to be very reliable when tested on experimentally known structures.⁶

In this paper we describe the application of our potential, derived for bulk silicon, to the study of the structures and stabilities of discrete silicon clusters ranging from the dimer to structures containing hundreds of atoms. There is a wealth of experimental mass-spectroscopic data available for gas-phase silicon clusters (detected as their cations or anions) and their reactivities have also been investigated.⁷,⁸ There is, as yet, no clear evidence for the existence of ‘magic numbers’ corresponding to exceptionally stable cluster nuclearities, as the intensities of the mass-spectral peaks seem to depend on the method of generation and ionisation of the clusters.⁷

We are certainly not the first to utilise an empirical potential, derived from crystalline solids to study microscopic systems, $^{9–19}$ but we believe that our function reproduces a more extensive data base than others that have been used. The full range of applicability of our functions have yet to be tested. We are currently investigating the $2 \times 1$ reconstruction of the $Si(100)$ surface²⁰ and can reproduce the surface dimerisation, though more subtle aspects of the restructuring such as the tilting and twisting of the surface dimers have yet to be studied. As clusters can have as many as one third of their atoms on the surface,²¹ one would expect cluster and surface structures to have common features. Indeed Kaxiras has recently suggested that the clusters $Si_{33}$ and $Si_{45}$, which he finds to be particularly stable, have surface structures which are similar to the $7 \times 7$ and $2 \times 1$ reconstructions of the bulk $Si(111)$ surface, respectively.²²

Potentials for small clusters should be electronic state specific. For example *ab initio* calculations on $C_{4}$ indicate that there are two low-lying structures which are very close in energy; a singlet planar rhombus and a triplet linear structure, though there is some disagreement as to which is actually the ground state.²³ Clearly the potentials required to reproduce these minima accurately on the singlet and triplet surfaces are quite different. However, potentials derived from crystalline solids (*e.g.* diamond) will not be electronic state specific as in the dissociation limit they will not satisfy the Wigner–Witmer electron correlation rules for breaking chemical bonds.²⁴ We would, however, expect such potentials to be applicable to clusters which are sufficiently large that there are several electronic states populated at the temperature at which the studies are made; certainly as the size of the cluster increases a potential deduced from bulk properties must become more valid. Another problem is that for small clusters highly symmetrical structures may give rise to electronic states which are unstable with respect to Jahn–Teller or pseudo-Jahn–Teller distortions and these distortions may not be reproduced by non-state-specific potentials. Again this should be less of a problem for large clusters where the electronic energy levels approach a continuum. Chelikowsky and Phillips have proposed that Jahn–Teller distortions in large clusters will be reduced by steric hindrance $^{18b}$ so that any distortions are likely to be restricted to the surface atoms.¹⁸ᵈ

Our potential is written as the sum of effective two-body and three-body terms, such that the total energy of a cluster is given by:²
$$
V = \sum_{i} \sum_{j>i} V_{ij}^{(2)} + \sum_{i} \sum_{j>i} \sum_{k>j} V_{ijk}^{(3)} \tag{1}
$$
with the two- and three-body components having the following analytical forms:
$$
V_{ij}^{(2)} = -D(1 + a_{2} \rho_{ij})\mathrm{exp}(-a_{2} \rho_{ij}) \tag{2}
$$
$$
V_{ijk}^{(3)} = DP(Q_{1}, Q_{2}, Q_{3})\mathrm{exp}(-a_{3} Q_{1}) \tag{3}
$$
where $P$ is a totally symmetric polynomial in the symmetry coordinates $Q_{i}$.²⁵
$$
\begin{pmatrix}
Q_{1} \\
Q_{2} \\
Q_{3}
\end{pmatrix}
=
\begin{pmatrix}
\sqrt{\frac{1}{3}} & \sqrt{\frac{1}{3}} & \sqrt{\frac{1}{3}} \\
0 & \sqrt{\frac{1}{2}} & -\sqrt{\frac{1}{2}} \\
\sqrt{\frac{2}{3}} & -\sqrt{\frac{1}{6}} & -\sqrt{\frac{1}{6}}
\end{pmatrix}
\begin{pmatrix}
\rho_{1} \\
\rho_{2} \\
\rho_{3}
\end{pmatrix} \tag{4}
$$

† Permanent address: Institute of Molecular Science, Shanxi University, Taiyuan, People's Republic of China and Yuncheng Community College, Yuncheng, People's Republic of China.

<table><caption>Table 1 Parameters defining the silicon potential used in this study</caption>
<tbody><tr><td>$a_{2}$</td><td>6.50</td><td>$c_{0}$</td><td>3.598</td><td>$c_{4}$</td><td>$-5.570$</td><td>$c_{8}$</td><td>$-111.809$</td></tr>
<tr><td>$a_{3}$</td><td>6.50</td><td>$c_{1}$</td><td>$-11.609$</td><td>$c_{5}$</td><td>79.210</td><td>$c_{9}$</td><td>9.705</td></tr>
<tr><td>$D$/eV</td><td>2.918</td><td>$c_{2}$</td><td>13.486</td><td>$c_{6}$</td><td>$-6.458$</td><td>$c_{10}$</td><td>38.297</td></tr>
<tr><td>$r_{e}$/Å</td><td>2.389</td><td>$c_{3}$</td><td>$-18.174$</td><td>$c_{7}$</td><td>23.383</td><td></td><td></td></tr>
</tbody></table>

and

$$
\rho_{i j}=\left(r_{i j}-r_{e}\right) / r_{e} \quad (5)
$$

The silicon potential used in the work described here is based on a quartic polynomial:

$$
\begin{aligned}
P\left(Q_{1}, Q_{2}, Q_{3}\right) & =c_{0}+c_{1} Q_{1}+c_{2} Q_{1}^{2}+c_{3}\left(Q_{2}^{2}+Q_{3}^{2}\right) \\
& +c_{4} Q_{1}^{3}+c_{5} Q_{1}\left(Q_{2}^{2}+Q_{3}^{2}\right) \\
& +c_{6}\left(Q_{3}^{3}-3 Q_{3} Q_{2}^{2}\right) \\
& +c_{7} Q_{1}^{4}+c_{8} Q_{1}^{2}\left(Q_{2}^{2}+Q_{3}^{2}\right) \\
& +c_{9}\left(Q_{2}^{2}+Q_{3}^{2}\right)^{2}+c_{10} Q_{1}\left(Q_{3}^{3}-3 Q_{3} Q_{2}^{2}\right) \quad (6)
\end{aligned}
$$

and the complete set of parameters for this potential are given in Table 1.

Finding the optimum geometry of a cluster $X_{n}$ is, except for small $n$, a non-trivial task, owing to the high dimensionality of the problem. Various strategies have been reported in the literature for this minimisation; among the most common are the molecular dynamics (MD) and Monte Carlo (MC) approaches, usually involving simulated annealing and quenching steps. $^{26}$ For our calculations we have adopted the following strategy: (a) For small clusters $(n<8)$ we use a numerical minimisation routine (NAG library routine E04JAF) $^{27}$ which starts from a randomly generated structure and finds local minima by treating the $3 n$ Cartesian coordinates as independent variables. This was found to be a fast and reliable procedure. An MC-based routine was found to give the same structures. (b) For larger clusters we first generated benchmarks for finite 'shell' structures generated from the bulk cubic solids (diamond, s.c., b.c.c. and f.c.c.) and also for icosahedral structures, with the radius of each concentric shell around a central atom being independently optimised. For example, a cluster of 47 atoms can be generated from the diamond structure and consists of concentric shells of 4, 12, 12, 6 and 12 atoms around the central atom, the whole cluster (which may be written $1: 4: 12: 12: 6: 12$ ) possessing $O_{\mathrm{h}}$ symmetry. The optimised shell structure is obtained by varying the radii of these five shells. (c) Many of the radially optimised shell structures generated by approach (b) were used as initial structures for a full optimisation of all atomic coordinates using the same program as in (a). In some cases (vide infra) the shell structure was retained, while in others it was lost, though often only the outer shells were split into two or more sub-shells. We have made a thorough study of clusters up to $n=20$ and a partial study of selected larger clusters.

### Small Si Clusters $(Si_{2}-Si_{8})$

The binding energies (per atom) and geometries calculated, using our bulk Si potential, for silicon clusters with up to eight atoms are given in Table 2 and some of the structures are shown in Fig. 1. For the smaller clusters, several of the higher symmetry structures are presented as benchmarks, together with an indication of whether they correspond to global (stable) or local (metastable) minima on the potential-energy hypersurface, or whether they are not minima at all (unstable).

Before commenting on these results, it is worth reiterating that our potential is not electronic state specific so we do not

<table><caption>Table 2 Optimised structures, bond lengths and binding energies calculated for silicon clusters with 2-8 atoms</caption>
<thead>
<tr>
<th>cluster</th>
<th>structure</th>
<th>symmetry</th>
<th>bond lengths/Å</th>
<th>binding energy per atom/eV</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Si_{2}$</td>
<td>dimer</td>
<td>$D_{\infty h}$</td>
<td>2.39</td>
<td>1.46</td>
</tr>
<tr>
<td>$Si_{3}$</td>
<td>isosceles triangle</td>
<td>$C_{2v}$</td>
<td>$2.46,3.26,\theta =83.3^{\circ }$</td>
<td>$1.97(g)^{a}$</td>
</tr>
<tr>
<td></td>
<td>linear</td>
<td>$D_{\infty h}$</td>
<td>2.45</td>
<td>$1.77(l)^{a}$</td>
</tr>
<tr>
<td rowspan="3">$Si_{4}$</td>
<td>equilateral triangle</td>
<td>$D_{3h}$</td>
<td>2.69</td>
<td>1.94 (l)</td>
</tr>
<tr>
<td>square</td>
<td>$D_{4h}$</td>
<td>2.47</td>
<td>2.67 (g)</td>
</tr>
<tr>
<td>tetrahedron</td>
<td>$T_{d}$</td>
<td>2.77</td>
<td>2.47 (l)</td>
</tr>
<tr>
<td>$Si_{5}$</td>
<td>I</td>
<td>$D_{3h}$</td>
<td>$r_{12}=2.57$<br>$r_{22'}=3.32,r_{11'}=3.41$</td>
<td>3.01 (g)</td>
</tr>
<tr>
<td rowspan="3">$Si_{6}$</td>
<td>pentagon</td>
<td>$D_{5h}$</td>
<td>2.40</td>
<td>$2.68(n)^{a}$</td>
</tr>
<tr>
<td>II</td>
<td>$D_{2d}$</td>
<td>$r_{12}=2.52,r_{22'}=2.62$<br>$r_{12'}=3.37,r_{22'}=3.49$</td>
<td>3.25 (g)</td>
</tr>
<tr>
<td>III</td>
<td>$C_{2v}$</td>
<td>$r_{11'}=2.55,r_{12}=2.52$<br>$r_{22'}=2.45$</td>
<td>2.98 (l)</td>
</tr>
<tr>
<td rowspan="4">$Si_{7}$</td>
<td>octahedron</td>
<td>$O_{h}$</td>
<td>2.78</td>
<td>3.03 (n)</td>
</tr>
<tr>
<td>hexagon</td>
<td>$D_{6h}$</td>
<td>2.43</td>
<td>2.59 (n)</td>
</tr>
<tr>
<td>IV</td>
<td>$C_{2v}$</td>
<td>$r_{12}=2.66,r_{13}=2.57$<br>$r_{24}=2.58,r_{34}=2.52$<br>$r_{22'}=3.38,r_{23}=3.36$</td>
<td>3.38 (g)</td>
</tr>
<tr>
<td>V</td>
<td>$C_{2}$</td>
<td>$r_{13}=2.48,r_{22'}=2.54$<br>$r_{23}=2.54,r_{24}=2.48$<br>$r_{34'}=2.52$</td>
<td>3.32 (l)</td>
</tr>
<tr>
<td rowspan="3">$Si_{8}$</td>
<td>cube</td>
<td>$O_{h}$</td>
<td>2.51</td>
<td>3.59 (g)</td>
</tr>
<tr>
<td>VI</td>
<td>$C_{1}$</td>
<td>$r_{12}=2.62,r_{13}=2.71$<br>$r_{14}=2.56,r_{15}=2.65$<br>$r_{26}=2.57,r_{27}=2.54$<br>$r_{36}=2.65,r_{37}=2.62$<br>$r_{46}=2.50,r_{57}=2.57$<br>$r_{38}=2.56,r_{58}=2.50$</td>
<td>3.49 (l)</td>
</tr>
<tr>
<td>VII</td>
<td>$C_{2}$</td>
<td>$r_{11'}=2.52,r_{12}=2.49$<br>$r_{14}=2.49,r_{14}=3.38$<br>$r_{23}=2.55,r_{34}=2.48$</td>
<td>3.46 (l)</td>
</tr>
</tbody>
</table>

$^{a}g=$ global minimum; $l=$ local minimum; $n=$ non-minimum.

![](./images/812358289089101824_1.jpg)

Fig. 1 Structures of some of the silicon clusters listed in Table 2

expect to find a close correspondence between our results and the geometries and energies of particular electronic states. However, the results for this group of small clusters are important for seeing how the larger clusters are built up.

The two-body term in our potential (which has $D=2.92$ eV, $r_{\mathrm{e}}=2.39$ Å) is a little weaker than that for the $^{3} \Sigma_{\mathrm{g}}^{-}$ ground state of $\mathrm{Si}_{2}(D=3.24$ eV, $r_{\mathrm{e}}=2.25$ Å),$^{28}$ however, the degeneracy-weighted average of the dissociation energies of all of the states arising from the ground electronic configu- ration of $\mathrm{Si}_{2}(\pi_{\mathrm{u}}^{2})$ is $2.86$ eV and the average bond length is $2.29$ Å,$^{29}$ values which are closer to our parameters.

In the following discussion of clusters $\mathrm{Si}_{3}-\mathrm{S}_{8}$ we have com- pared our results with the best available $ab$ initio calculations of Raghavachari and co-workers, $^{30}$ which are at the HF/6- $31G^{*}$ level. Accurate calculations on small silicon clusters, which agree essentially with those of Raghavachari, have also been performed by Pacchioni and Koutecky $^{31}$ and Messmer and co-workers. $^{32}$ Further calculations on silicon clusters are listed in ref. 7 and 8. These calculations all predict structures for low-nuclearity clusters (up to 10 atoms) which are more close-packed than bulk diamond; this reduces the number of dangling bonds arising from the high proportion of surface atoms.

Using our silicon potential, we find $\mathrm{Si}_{3}$ to have a $C_{2\mathrm{v}}$ struc- ture, with the bond lengths and bond angle being slightly larger than predicted by the $ab$ initio calculations $(r_{\mathrm{e}}=2.17$ Å, $\theta=78^{\circ}).^{30}$ The stability is a little lower than the calcu- lations and experiments suggest (2.5 eV per atom). $^{7}$ Our potential predicts a metastable $D_{3\mathrm{h}}$ minimum $0.03$ eV per atom above the global minimum and the $ab$ initio calcu- lations identify this as the geometry of the lowest triplet state of $\mathrm{Si}_{3}$, with a binding energy only $0.01$ eV per atom less than that of the singlet $(C_{2\mathrm{v}})$ state. Our energy difference between the bent $(C_{2\mathrm{v}})$ and linear $(D_{\infty\mathrm{h}})$ structures is quite close to the $ab$ initio value of $0.14$ eV per atom, although our finding that the linear structure is at a very shallow minimum is not sup- ported by Raghavachari's calculations.

We find the most stable $\mathrm{Si}_{4}$ structure to be a square $(D_{4\mathrm{h}})$ whereas the $ab$ initio calculations give a rhombic $(D_{2\mathrm{h}})$ ground state, with the $D_{4\mathrm{h}}$ geometry not being a minimum on either the singlet or triplet surfaces, owing to strong pseudo- Jahn-Teller distortions of both the singlet and triplet squares. We find tetrahedral $\mathrm{Si}_{4}$ to be metastable, in agreement with the $ab$ initio calculations.

The only minimum we have found on the $\mathrm{Si}_{5}$ surface has $D_{3\mathrm{h}}$ symmetry (I) and this is also found by $ab$ initio calcu- lations. It is misleading to refer to this structure as a trigonal bipyramid as there is a significant compression along the three-fold axis (ax-ax $=3.41$ Å) and the equatorial bonds are consequently quite long (eq-eq $=3.32$ Å $cf.$ ax-eq $=2.47$ Å) which is confirmed by the $ab$ initio calculations. The $ab$ initio geometry (ax-eq $=2.34$ Å, eq-eq $=3.26$ Å, ax-ax $=2.78$ Å; binding energy $=3.30$ eV per atom) is in good agreement with that reported here, though our calculations underesti- mate the axial compression; in fact all of our calculated bond lengths are slightly too long. Interestingly, the $ab$ initio calcu- lations also find $^{30a}$ a metastable triplet state arising from an uncompressed trigonal bipyramidal geometry (ax-eq $=2.40$ Å, eq-eq $=2.48$ Å, ax-ax $=3.86$ Å; binding energy $=3.12$ eV per atom).

The important structural feature of the $\mathrm{Si}_{5}$ cluster (I) is the occurrence of four-atom faces with local 'butterfly' $(D_{2\mathrm{d}})$ geometries. This feature is maintained for $\mathrm{Si}_{6}$, by bridging one of the faces of $\mathrm{Si}_{5}$ to give a structure with overall $D_{2\mathrm{d}}$ symmetry (II). The best $ab$ initio structure is very similar to our minimum, but has lower symmetry $(C_{2\mathrm{v}})$ owing to the formation of two bonds (eq-eq in the parent $\mathrm{Si}_{5}$ cluster) which yields an edge-bridged trigonal-bipyramidal structure. Extended Hückel calculations on our structure indicate an $\mathrm{e}^{2}$ ground configuration in the $D_{2\mathrm{d}}$ geometry which would be unstable to a pseudo-Jahn-Teller distortion towards the $ab$ initio $C_{2\mathrm{v}}$ structure. Our $D_{2\mathrm{d}}$ structure is close in energy to the $ab$ initio $C_{2\mathrm{v}}$ structure. We have also found a local minimum corresponding to an approximately planar struc- ture (III) with $C_{2\mathrm{v}}$ symmetry comprising two fused four- membered rings.

Adding a further face-capping atom to the $D_{2\mathrm{d}}$ $\mathrm{Si}_{6}$ cluster leads, with our potential to a $\mathrm{Si}_{7}$ structure (IV) which has $C_{2\mathrm{v}}$ symmetry. This cluster has one atom which is four-connected, but the four bonds are not tetrahedrally oriented. $Ab$ initio calculations on a number of $\mathrm{Si}_{7}$ structures found the pentag- onal bipyramid to be most stable, a rather surprising result as the axial atoms have five short bonds $(2.47$ Å) to the equato- rial atoms and there is also a short $(2.58$ Å) axial-axial dis- tance, though the overlap populations do not indicate significant bonding along this axis. $^{30}$ We have also found a local minimum with $C_{2}$ symmetry (V) which is formed by bridging two of the atoms of structure III, together with a

![](./images/812358289089101824_2.jpg)

Fig. 2 Generation of the $C_2$ symmetry $Si_8$ cluster (VII) from the cube. The distortion (indicated by arrows) results in the formation of a bond across one diagonal (indicated by the dotted line) and the breaking of two bonds (marked x)

folding of the $Si_6$ fragment. Our structures do not appear to have been examined by $ab$ initio methods.

Our most stable $Si_8$ structure is the cube, but we found two metastable structures, one of which (VI) has no symmetry elements and is formed from the global $Si_7$ minimum (IV) by bridging across one of the four-membered faces. The second local minimum that we found has $C_2$ symmetry (VII) and is related to the cube by forming a bond across one of the diagonals of a square face and breaking two bonds, as shown in Fig. 2. Neither of these structures have been examined by $ab$ initio calculations; the high symmetry ones may of course be unstable to Jahn-Teller or pseudo-Jahn-Teller distortions. The best $ab$ initio structure for $Si_8$ is a bicapped (on opposite faces) octahedron with $C_{2h}$ symmetry (owing to a Jahn-Teller distortion away from $D_{3d}$ symmetry).$^{30}$

The most important generalisation that can be drawn from our results for small Si clusters is that there is a preponder- ance of four-atom rings. Fig. 3 shows how some of the global and local minima that we have found can be built up from square $Si_4$ by successively adding two-coordinate bridging atoms. These structures are more compact than microcrystal- line fragments of the diamond lattice in which one sees exclu- sively six-membered rings. As mentioned above, the formation of more closely packed structures presumably occurs so as to minimise the number of surface dangling bonds. As the cluster size increases, however, larger ringsshould become more prevalent. Even for $Si_7$ (V) and $Si_8$ (VII) we see metastable structures containing five-membered rings. Our calculations do not predict any magic number clusters in the region $Si_2$-$Si_8$, a result which is in agreement with the $ab$ initio work of Raghavachari. $^{30}$

## Radially Optimised Shell Structures
Fig. 4 shows the binding energies per atom of $Si_n$ shell clusters $(n<100)$ derived from the cubic solids. The structures were relaxed by allowing the radii of the shells to vary inde- pendently as described above. We also have results for larger diamond shell structures. The largest we have considered has357 atoms (19 shells) and a binding energy per atom of 4.63 eV, which is still short of the bulk Si (diamond) cohesive energy of 4.72 per atom. $^{33}$ However, even for the 19-shell diamond cluster $ca$. one third of the atoms are surface atoms(i.e. they have unsaturated valencies; dangling bonds) which easily accounts for the energy loss.

From Fig. 4 it can be seen that the s.c. and b.c.c. fragments stand out as being particularly stable; less so the f.c.c. frag-

![](./images/812358289089101824_3.jpg)

Fig. 4 Binding energy per atom as a function of the number of atoms for radially optimised silicon shell clusters derived from the diamond (d), s.c. (s), b.c.c. (b) and f.c.c. (f) solids. The bulk values are indicated by the arrows at the right

![](./images/812358289089101824_4.jpg)

Fig. 3 Illustration of the stepwise generation of $Si_5$-$Si_8$ structures, consisting exclusively of four-membered rings, from square $Si_4$ by adding two-coordinate bridging atoms (indicated by shading)

mens although $Si_{43}$ has a higher binding energy per atom than the diamond cluster of comparable size. Semiempirical (SINDO1) calculations by Kupka and Jug found some f.c.c., h.c.p. and icosahedral structures to be more stable thandiamond structures in the range 13-35 atoms. $^{21}$ Above 35 atoms, diamond shell structures were found to be more stable than h.c.p., but still less stable than f.c.c. This finding is con- sistent with our work, which predicts that the diamond struc- tures become more stable than the close-packed ones at nuclearities well above 100.

As shown in Fig. 4, we find a general upward trend in binding energy for all the cubic structures, which is to be expected since the average number of dangling bonds (unsaturated valencies) per atom decreases as the ratio of surface to bulk atoms decreases. Kupka and Jug's calcu- lations, while showing a steady rise in binding energy for the diamond clusters, predict a decrease in binding energy for f.c.c. and h.c.p. shell clusters. $^{21}$ We think that this result is unphysical as it implies that the f.c.c. and h.c.p. binding ener- gies would not converge to the bulk values for infinite nuclearities. Kupka and Jug state that the binding energy of f.c.c. $Si_{43}$ (3.66 eV per atom; $c f$ . our value of 3.80 ) is anomalously low, but it is more likely that their values for $Si_{13}$ (4.37 eV per atom) and $Si_{19}$ (4.24 eV per atom) are too high.

Superimposed on the general increase in binding energy with cluster nuclearity, shown in Fig. 4, there are a number of peaks of stability corresponding to magic number clusters. The most prominent of these is the three-shell 27-atom s.c. cluster with a binding energy of 4.14 eV per atom; the most stable shell structure up to 55 atoms. This cluster will be dis- cussed in greater detail below.

Calculations were also performed on shell clusters pos- sessing icosahedral symmetry, with 13, 43 and 55 atoms. The icosahedral and f.c.c. structures, with the same nuclearity, have approximately the same energy. For $Si_{13}$ the centred icosahedron and the f.c.c. centred cuboctahedron are almost isoenergetic while for $Si_{43}$ the f.c.c. structure is favoured by0.03 eV per atom and for $Si_{55}$ the icosahedral structure is favoured by 0.02 eV per atom. Kupka and Jug found the centred icosahedron to be a true minimum on the $Si_{13}$ poten tial surface and the f.c.c. structure to be a first-order saddle point which is 0.58 eV per atom less stable, $^{21}$ a much greater energy difference than we obtain. The h.c.p. $Si_{13}$ structure (acentred anti-cuboctahedron, which we have not investigated) is calculated to be 0.06 eV per atom less stable than f.c.c.

For certain cluster nuclearities it is possible to construct complete shell clusters based on two or more bulk structures. In these cases, examples of which occur at n = 19 and 27, it is informative to see which is the energetically favoured struc- ture. For n = 27 we find that, starting from radially expanded shell geometries, the radially optimised structures based on the s.c. and b.c.c. solids are identical, because the first shell of8 atoms in the b.c.c. structure (1:8:6:12) passes through the second and third shells to give the s.c. 1:6:12:8 shell structure. This is also observed for n = 19, where the s.c. cluster (with shell structure 1:6:12) relaxes to the f.c.c. ord- ering 1:12:6. Starting from clusters which are not so expanded, however, introduces an activation barrier to shellinterchange and the partially relaxed s.c. cluster with 19 atoms is found to have a binding energy of 3.57 eV per atom, compared with the f.c.c. value of 3.72 eV per atom.

The stabilities of complete shell structures have implica- tions for incomplete shell clusters also. Consider, for example,taking a stable filled-shell structure such as the s.c. $Si_{27}$  cluster and adding successive atoms to the surface. If thebinding energies of the additional atoms are zero (at worst) then the energies per atom for larger n are $4.12 \times(27 / n)$ . For n = 29, for example, this gives a binding energy of 3.84 eV per atom, which is still greater than the energy of the diamond structure for n = 29 (3.61 eV per atom), so it is clear that the less stable filled-shell structures will relax to incomplete-shell geometries if the structure is fully optimised.

Table 3 lists the optimised shell radius expansion factors for filled-shell structures with up to 55 atoms. These expan- sion factors are calculated as the ratio of the shell radius in the cluster to that in the bulk. The bulk radii have been cal- culated using the following relative nearest-neighbour dis- tances: $r($ s.c. $)=1.12 r(d) ; r($ b.c.c. $)=1.21 r(d) ; r($ f.c.c. $)=1.26 r(d)$ ,which were calculated previously from our potential. $^{4}$

It is informative to consider what happens to the shell radii of the f.c.c. structures going from the 13-atom (one shell) to the 19-atom (two shells), 43-atom (three shells) and 55-atom(four shells) clusters. From Table 3 it is apparent that adding a shell to $Si_{13}$ leads to an expansion of the inner shell from0.96 to 0.99 times the bulk f.c.c. radius, while the contraction of the second shell is quite substantial. This was also found by Kupka and Jug, and attributed by them to bonding between the first and second shells resulting in the inner shell being drawn out. $^{21}$ Adding a third shell causes the first shell to expand slightly (to 1.01 times the bulk value), but results ina large increase in the second shell radius (from 0.92 to 1.03 times the bulk value). This is to be expected since the third

<table>
<caption>Table 3 Optimised radii of shell clusters (with up to 55 atoms) derived from the cubic solids<sup>a</sup></caption>
<thead>
<tr>
<th>no. atoms</th>
<th>no. shells</th>
<th>structure</th>
<th>a(i)</th>
<th>binding energy per atom/eV</th>
</tr>
</thead>
<tbody>
<tr>
<td>5</td>
<td>1</td>
<td>d 1:4</td>
<td>1.04</td>
<td>1.96</td>
</tr>
<tr>
<td>7</td>
<td>1</td>
<td>s.c. 1:7</td>
<td>0.95</td>
<td>2.22</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>b.c.c. 1:8</td>
<td>0.94</td>
<td>2.55</td>
</tr>
<tr>
<td>13</td>
<td>1</td>
<td>f.c.c. 1:12</td>
<td>0.96</td>
<td>3.40</td>
</tr>
<tr>
<td>15</td>
<td>2</td>
<td>b.c.c. 1:8:6</td>
<td>1.01, 0.91</td>
<td>3.77</td>
</tr>
<tr>
<td>17</td>
<td>2</td>
<td>d 1:4:12</td>
<td>1.02, 1.01</td>
<td>2.50</td>
</tr>
<tr>
<td>19</td>
<td>2</td>
<td>f.c.c. 1:12:6</td>
<td>0.99, 0.92</td>
<td>3.72</td>
</tr>
<tr>
<td>19</td>
<td>2</td>
<td>s.c. 1:6:12</td>
<td>1.01, 0.95</td>
<td>3.57</td>
</tr>
<tr>
<td>27</td>
<td>3</td>
<td>s.c. 1:6:12:8</td>
<td>0.99, 0.98, 0.96</td>
<td>4.14</td>
</tr>
<tr>
<td>27</td>
<td>3</td>
<td>b.c.c. 1:8:6:12</td>
<td>1.04, 0.97, 0.94</td>
<td>3.68</td>
</tr>
<tr>
<td>29</td>
<td>3</td>
<td>d 1:4:12:12</td>
<td>0.98, 1.01, 1.00</td>
<td>3.61</td>
</tr>
<tr>
<td>33</td>
<td>4</td>
<td>s.c. 1:6:12:8:6</td>
<td>1.00, 1.00, 0.95, 0.96</td>
<td>3.82</td>
</tr>
<tr>
<td>35</td>
<td>4</td>
<td>d 1:4:12:12:6</td>
<td>0.98, 1.01, 1.01, 1.01</td>
<td>3.77</td>
</tr>
<tr>
<td>43</td>
<td>3</td>
<td>f.c.c. 1:12:6:24</td>
<td>1.01, 1.03, 0.96</td>
<td>3.80</td>
</tr>
<tr>
<td>47</td>
<td>5</td>
<td>d 1:4:12:12:6:12</td>
<td>0.95, 0.98, 1.03, 1.00, 0.98</td>
<td>3.51</td>
</tr>
<tr>
<td>51</td>
<td>4</td>
<td>b.c.c. 1:8:6:12:24</td>
<td>1.02, 0.99, 1.01, 0.96</td>
<td>3.96</td>
</tr>
<tr>
<td>55</td>
<td>4</td>
<td>f.c.c. 1:12:6:24:12</td>
<td>0.99, 0.99, 0.98, 0.96</td>
<td>3.87</td>
</tr>
</tbody>
</table>

<sup>a</sup> a(i) is the ratio of the ith shell radius in the cluster to that in the infinite solid. The nearest neighbour distances in the s.c., b.c.c. and f.c.c. infinite lattices are factors of 1.12, 1.21 and 1.26 greater than diamond (d), respectively.

shell contains 24 atoms and should have substantial bonding to the second shell atoms. On going to the four shell 55-atom cluster we see that the inner two shells are now very close (0.99) to the bulk values, though they are still slightly more expanded (relative to the bulk) than the third (0.98) and fourth (0.96) shells.

Another interesting structure is the 15-atom b.c.c. cluster which shows a marked contraction of the outer shell of six atoms such that the second shell radius is only 0.91 times the bulk value, with the inner shell of 8 atoms having almost the same radius (1.01) as the bulk. This distortion producing a cluster which is almost spherical ($r_2/r_1 = 1.04$ compared with $2/\sqrt{3} = 1.15$ for bulk b.c.c.). Similarly the very stable 27-atom s.c. cluster has a cubic structure with 9 atoms per face, as shown in Fig. 5, but the $a(i)$ values decrease with increasing shell number ($i$) so that the cluster becomes slightly more spherical. The great stability of this three shell cluster (binding energy = 4.14 eV per atom) compared with the two shell $Si_{19}$ (3.57 eV per atom) and four shell $Si_{33}$ (3.82 eV per atom) s.c. clusters is associated with the fact that the 8 third shell atoms are added to high (three) coordinate sites at the corners of the cube and they increase the coordination number of the 12 second shell atoms from 2 to 4. Thus the 27-atom cluster has a binding energy which is quite close to that calculated for the bulk (4.58 eV per atom). Addition of the fourth shell, however, adds 6 atoms which lie above the faces of the cube in one-coordinate sites and they only increase the coordination number of the first shell from 5 to 6.

In summary, although the b.c.c. and f.c.c. lattices are the least stable of the cubic structures that we have considered for silicon, $^{3,4}$ radial relaxation results in the finite b.c.c. and f.c.c. shell clusters becoming more stable relative to diamond clusters of comparable size. This relaxation also results in the b.c.c. and f.c.c. shell clusters with five-shells or more having greater binding energies than the corresponding bulk solids, which is not observed for diamond or s.c. shell clusters in the region studied. The s.c. bulk structure is already quite close in energy to diamond and, even unrelaxed, the small s.c. shell clusters are more stable than diamond structures of compar- able size. This finding is consistent with the above mentioned predominance of four-membered rings in small clusters, since the s.c. shell structures are all characterised by large numbers of square rings.

# Fully Optimised Structures up to $Si_{20}$

We have examined the full optimisation of all clusters up to $Si_{20}$ starting from initial geometries which either correspond to completely or partially filled shell structures derived from the cubic solids, or are generated randomly. In all cases the shell structures relax further, though the final structure may differ depending on the starting point. For $Si_{10}$, for example, the diamond, b.c.c. and f.c.c. precursors all relax to the same structure which has 16 bonds and a binding energy of 3.74 eV per atom, while starting from a 10 atom s.c. fragment leads to a 14-bond structure with a binding energy of 3.50 eV per atom. There is no guarantee that we have found the global minima for these clusters $^{34}$ but extensive searches from ran domly initiated structures have not produced lower energies. The $3n - 6$ dimensional hypersurface has many minima, some of which are geometrically equivalent, but many others will be distinct and the minimisation routine that we use can find only the nearest local minimum to the starting point by a steepest descent method. Because the uncertainty of finding the true minimum increases with $n$, we have not yet made a comprehensive search above $n = 20$, although some of the complete shell structures have been examined.

Fig. 6 shows the binding energy per atom as a function of $n$ for the fully optimised structures. For the smaller clusters there is a considerable increase in stability on relaxing the constraint of shell structure and consequently there is a steady rise from $n = 2$ to 8 but thereafter the slope decreases considerably. The value for $n = 9$ is slightly lower than for $n = 8$, though the total binding energy continues to rise at a rate of $ca.$ 4 eV per atom added. The most important point to note is that the approach to the asymptotic (bulk diamond structure) limit of 4.72 eV per atom is very slow, as in clusters of up to 20 atoms, there are considerably more surface than bulk atoms. There is no sign of magic numbers (corresponding to clusters with substantially higher binding energies than their neighbours) in the series so far.

![](./images/812358289089101824_5.jpg)

Fig. 5 The unrelaxed cubic s.c. shell cluster $Si_{27}$. The six first-shell atoms (1) define an octahedron, the twelve second-shell atoms (2) define a cuboctahedron, and the eight third-shell atoms (3) define a cube. Relaxation results in non-planar cube faces and shell radii which are closer than for the ideal cube

# Summary of Previously Published Potentials

In recent years there have been many studies of silicon clusters using empirical potentials derived from bulk properties. $^{7,9-19}$ We here refer specifically only to two recent studies, by Chelikowsky, Phillips and co-workers $^{18}$ and by Bolding and Andersen. $^{19}$

Bolding and Andersen have used a modified Tersoff potential $^{11}$ (where many-body effects are included via an environment-dependent two-body term) in which the bonding in small clusters is divided into $\pi$ and $\sigma$ components. $^{19}$ The structures that they obtain as the global

![](./images/812358289089101824_6.jpg)

Fig. 6 Binding energy per atom as a function of the number of atoms for fully optimised clusters $Si_{2}-Si_{20}$

J. GHEM. SOC. FARADAY TRANS., 1992, VOL. 88

minima of $Si_{4}, Si_{7}$ and $Si_{9}$ are in good agreement with those obtained from $a b$ initio calculations. $^{30}$ For $Si_{3}, Si_{5}, Si_{8}$ and Si1o, however, the Bolding and Andersen global minima cor- respond to local minima on the $a b$ initio surface. For $Si_{6}$ the predicted structure is an octahedron, which is close in energy and geometry to the $a b$ initio $C_{2 v}$ structure, into which it can be converted by a Jahn-Teller distortion. Bolding and Ander- sen have also investigated the potentials of Stillinger and Weber, $^{9}$ Biswas and Hamann $^{10}$ and Tersoff. $^{11}$ In agreement with previous MD studies by Feuston et al. $^{15}$ they found that the simple Stillinger-Weber potential yields clusters which are too open (for instance the most stable $Si_{5}$ structure is the planar pentagon) which is presumably due to the bias which the Stillinger-Weber three-body term has for tetrahedral angles. $^{9}$ Similar results were obtained with the Biswas Hamann potential $^{10}$ which has a qualitatively similar three body term. Finally, Bolding and Andersen found that amongst several Tersoff potentials, $^{11}$ the one that gives the best agreement with the $a b$ initio calculations (and their own potentials) gives the poorest fit to the properties of bulk silicon. It has also been found that Tersoff's potential gives clusters which are more stable than the bulk, $^{17}$ which is clearly unphysical. $^{22 c}$ It should be noted that both the Stillinger-Weber and Biswas-Hamann potentials give good fits to the properties of diamond silicon, but fail badly for clusters.

Chelikowsky, Phillips and co-workers derived a seven- parameter potential for silicon $^{18}$ which reproduces theenergy-volume curves calculated by Cohen and co-workers $^{5}$  rather than phonon dispersion curves. With the addition of four 'backbonding' parameters, designed to reduce surface forces, they have obtained reasonable agreement with the ab initio results for $Si_{2}-Si_{10}$ (though $Si_{4}$ is predicted to be tetra hedral and $Si_{6}$ octahedral). They also predict an icosahedral growth pattern for clusters $Si_{n}$ with $10<n<20$ with magic number stabilities for icosahedral $Si_{13}$ and fused bi icosahedral $Si_{19}$ . For $20<n<30$ some elements of this pen tagonal growth sequence are retained. The problem with the Chelikowsky-Phillips potential is that the agreement with ab initio geometries can be obtained only by introducing the backbonding parameters which would have to go to zero in the bulk solid and presumably also in very large clusters. Whilst the authors claim that this enables the study of metal- lic (close-packed) and covalent (diamond-like) clusters as a function of a single parameter (one of their four backbonding parameters), it is difficult to see how this parameter should be defined in systems, such as liquid or amorphous silicon, where different types of bonding coexist.

Chelikowsky has also noted that for low cluster nuclearities f.c.c. fragments have greater binding energies than diamond fragments and estimates the crossover as occurring between 40 and 50 atoms, although since his structures are not fully optimised he says the crossover point may lie between 20 and 100 atoms. $^{18 c}$ Note, however that the nuclearities investigated do not all correspond to complete shell structures as in our study.

Finally, we would like to mention recent applications of density functional techniques to the study of the structures, energies and reactivities of silicon clusters. Tomanek and Sch- luter have performed combined tight-binding density func- tional calculations on silicon clusters up to $Si_{14} \cdot^{35}$ Their results are in good agreement with the $a b$ initio work of Ragh avachari and co-workers. $^{30}$ They find a gradual increase in binding energy with nuclearity, converging to the bulk value very slowly, as in our calculations, and estimate the close- packed-diamond crossover to occur somewhere in the range100 <n<1000. The model of Tomanek and Schluter has been criticised, however, on the grounds that it overestimatesthe stabilities of highly coordinated structures by too large a margin (several eV per atom). $^{22 c, 36}$ 

Ballone et al. have used the MD-density functional method of Car and Parinello $^{37}$ to study clusters with up to 10 atoms. $^{38}$ The minima obtained generally agree with the $a b$  initio calculations. $Si_{10}$ is an interesting case. Raghavachari's ab initio calculations originally predicted a tetracapped octa- hedral geometry $^{30 a}$ but Ballone et al. found the tetracapped trigonal prism to be slightly more stable (with a binding energy less than 0.01 eV per atom higher than that of thetetracapped octahedron). $^{38}$ Upon reinvestigating the problem, Raghavachari and Rohlfing found that the two structures do in fact lie very close in energy and that the rela- tive stability of the two isomers depends on the extent towhich electron correlation is included. $^{30 b}$ 

Recently, Andreoni and Pastore have explored the trans- ferrability of classical (bulk-derived) potentials to silicon microclusters, $^{39}$ by comparing the results of computer simulations using the Car-Parrinello method $^{37}$ and the Tersoff $^{11}$  and (early) Chelikowsky-Phillips $^{18 a, b}$ potentials. They point out that the empirical potentials give the 'wrong' structures for $Si_{4}$ (where they predict a tetrahedral geometry) and for $Si_{8}-Si_{10}$ . Chelikowsky et al. subsequently improved their fitby increasing the back-bonding parameter. $^{18 d}$ 

In conclusion, our potential, derived from bulk properties, with no additional parameters specific to clusters, performs at least as well as any of the empirical potentials mentioned above. We are currently studying the optimum structures of larger clusters $(n>20)$ in more detail and we hope also to obtain additional information on how our potential performs for surfaces and defects. We see no evidence at the present time to support the pessimistic view of Biswas and Hamann that a potential which simultaneously fits data from small clusters and solids should, necessarily, include $N$ -body terms with $N>3.^{10 a}$ 

S.L. is grateful for financial suport from the PRC. R.L.J. would like to thank the Royal Society for the award of a University Research Fellowship.

### References
1 J. N. Murrell and R. E. Mottram, Mol. Phys., 1990, 69, 571.
2 J. N. Murrell and J. A. Rodriguez-Ruiz, Mol. Phys., 1990, 71,823.
3 A. R. Al-Derzi, R. L. Johnston, J. N. Murrell and J. A. Rodriguez-Ruiz, Mol. Phys., 1991, 73, 265.
4 B. R. Eggen, R. L. Johnston, S. Li and J. N. Murrell, Mol. Phys., in the press.
5 M. T. Yin and M. L. Cohen, Phys. Rev. B, 1982, 26, 5668; K. J. Chang and M. L. Cohen, Phys. Rev. B, 1985, 31, 7819.
6 M. L. Cohen, Philos. Trans. R. Soc. London A, 1991, 334, 501.
7 M. L. Mandich, W. D. Reents Jr. and V. E. Bondybey, in *Atomic and Molecular Clusters, Studies in Physical and Theoretical Chemistry*, ed. E. R. Bernstein, Elsevier, Amsterdam, 1990, vol.68, ch. 2, p. 69.
8 D. M. P. Mingos, T. Slee and Z. Lin, Chem. Rev., 1990, 90, 383.
9 F. Stillinger and T. Weber, Phys. Rev. B, 1985, 31, 5262.
10 (a) R. Biswas and D. R. Hamann, Phys. Rev. Lett., 1985, 55,2001; (b) R. Biswas and D. R. Hamann, Phys. Rev. B, 1987, 36,6434.
11 J. Tersoff, Phys. Rev. Lett., 1986, 56, 632; P. C. Kelires and J. Tersoff, Phys. Rev. Lett., 1988, 61, 562.
12 E. Blaisten-Barojas and D. Levesque, Phys. Rev. B, 1986, 34,3910.
13 B. W. Dodson, Phys. Rev. B, 1987, 35, 2795.
14 M. I. Baskes, Phys. Rev. Lett., 1987, 59, 2666.
15 B. P. Feuston, R. K. Kalia and P. Vashishta, Phys. Rev. B, 1988,37,6297.
16 A. D. Mistriotis, N. Flytzanis and S. C. Farantos, Phys. Rev. B,1989,39,1212.
17 J. L. Chen and C. S. Wang, Bull. Am. Phys. Soc., 1989, 34, 409.

18 (a) J. R. Chelikowsky, J. C. Phillips, M. Kamal and M. Strauss, Phys. Rev. Lett., 1989, 62, 292; J. R. Chelikowsky and J. C. Phil- lips, Phys. Rev. Lett., 1989, 63, 1653; (b) J. R. Chelikowsky and J. C. Phillips, Phys. Rev. B, 1990, 41, 5735; (c) J. R. Chelikowsky in Atomistic Simulation of Materials: Beyond Pair Potentials, ed. V. Vitek and D. J. Srolovitz, Plenum, New York, 1989, p. 67; (d) J. R. Chelikowsky, K. M. Glassford and J. C. Phillips, Phys. Rev. B, 1991, 44, 1538.

19 B. C. Bolding and H. C. Andersen, Phys. Rev. B, 1990, 41, 10568.

20 G. A. Somorjai, Chemistry in Two Dimensions: Surfaces, Cornell University Press, Ithaca, New York, 1981, p. 148.

21 H. Kupka and K. Jug, Chem. Phys., 1989, 130, 23.

22 (a) E. Kaxiras, Chem. Phys. Lett., 1989, 163, 323; E. Kaxiras, Phys. Rev. Lett., 1990, 64, 551. See also the discussions in: (b) B. L. Swift, D. A. Jelski, D. E. Higgs, T. T. Rantala and T. F. George, Phys. Rev. Lett., 1991, 66, 2686; (c) E. Kaxiras, Phys. Rev. Lett., 1991, 66, 2687.

23 W. Weltner Jr. and R. J. Van Zee, Chem. Rev., 1989, 89, 1713.

24 E. P. Wigner and E. E. Witmer, Z. Phys., 1928, 51, 859.

25 J. N. Murrell, S. Carter, S. C. Farantos, P. Huxley and A. J. C. Varandas, Molecular Potential Energy Functions, Wiley, New York, 1984, p. 40.

26 E. Blaisten-Barojas in Elemental and Molecular Clusters, Springer Series in Materials Science, ed. G. Benedek, T. P. Martin and G. Pacchioni, Springer, Berlin, vol. 6, p. 106.

27 Nag Fortran Mini Manual, Mark 9, Numerical Algorithms Group, Oxford, 1981.

28 K. P. Huber and G. Herzberg, Constants of Diatomic Molecules, Van Nostrand Reinhold, New York, 1979.

29 H. Dohmann, P. J. Bruna, S. D. Peyerimhoff and R. J. Buenker, Mol. Phys., 1984, 51, 1109.

30 (a) K. Raghavachari, J. Chem. Phys., 1986, 84, 5672; (b) K. Ragh- avachari and C. M. Rohlfing, J. Chem. Phys., 1988, 89, 2219; (c) K. Raghavachari and C. M. Rohlfing, Chem. Phys. Lett., 1988, 143, 428.

31 G. Pacchioni and J. Koutecky, J. Chem. Phys., 1986, 84, 3301.

32 C. H. Patterson and R. P. Messmer, Phys. Rev. B, 1990, 42, 7530; R. P. Messmer, W.-X. Tang and H.-X. Wang, Phys. Rev. B, 1990, 42, 9241.

33 CRC Handbook of Chemistry and Physics, CRC Press, Boca Raton, Florida, 64th edn., 1984, D-83.

34 R. O. Jones and O. Gunnarsson, Rev. Mod. Phys., 1989, 61, 689.

35 D. Tomanek and M. A. Schluter, Phys. Rev. Lett., 1986, 56, 1055; D. Tomanek and M. A. Schluter, Phys. Rev. B, 1987, 36, 1208.

36 F. S. Khan and J. Q. Broughton, Phys. Rev. B, 1991, 43, 11754.

37 R. Car and M. Parrinello, Phys. Rev. Lett., 1985, 55, 2471.

38 P. Ballone, W. Andreoni, R. Car and M. Parrinello, Phys. Rev. Lett., 1988, 60, 271.

39 W. Andreoni and G. Pastore, Phys. Rev. B, 1990, 41, 10243.

Paper 1/06359F; Received 19th December, 1991