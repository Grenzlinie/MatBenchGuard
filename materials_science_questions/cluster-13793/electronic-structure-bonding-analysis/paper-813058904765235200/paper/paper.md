# Attractive interaction between interstitial solutes and screw dislocations in bcc iron from first principles

B. Lüthi $^{a}$, L. Ventelon $^{a,*}$, D. Rodney $^{b}$, F. Willaime $^{c}$

$^{a}$ DEN-Service de Recherches de Métallurgie Physique, CEA, Université Paris-Saclay, F-91191 Gif-Sur-Yvette, France
$^{b}$ Institut Lumière Matière, CNRS-Université Claude Bernard Lyon 1, F-69622 Villeurbanne, France
$^{c}$ DEN-Département des Matériaux pour le Nucléaire, CEA, Université Paris-Saclay, F-91191 Gif-Sur-Yvette, France

---

## ARTICLE INFO

**Article history:**
Received 13 November 2017
Received in revised form 23 January 2018
Accepted 4 February 2018

**Keywords:**
DFT calculations
Dislocation-solute interaction
Bcc iron

---

## ABSTRACT

Plasticity in steels depends largely on how dislocations interact with solute atoms. We consider here typical interstitial solutes (B, C, N, O) in body-centered cubic (bcc) Fe and show using ab initio calculations that, systematically, when a row of interstitial solutes is in the vicinity of a $1/2\langle 111\rangle$ screw dislocation, the dislocation adopts a hard core, forming regular prisms of Fe atoms centered on the solute atoms. This low-energy configuration, previously known only for C atoms, induces attractive dislocation-solute interaction energies ranging from $-1.3$ to $-0.2$ eV, depending on the nature of the solutes and their separation distance along the dislocation line. This attractive reconstruction is explained by the larger Voronoi volume of the prismatic sites in the dislocation core compared to bulk octahedral sites. Moreover, an analysis of the local density of states gives a first insight into the chemical contribution responsible for the solute dependence of the interaction energy.

© 2018 Published by Elsevier B.V.

---

## 1. Introduction

An accurate description of elementary deformation mechanisms is essential to better apprehend plasticity in metals. In alloys, it is particularly important to determine how dislocations, responsible for plastic deformation, interact with solute atoms, if one wants to understand the strengthening effect of solutes [1]. Dislocation-solute interactions have been modeled in the region away from the dislocation core with elasticity theory and interatomic potentials [2-7] and more rarely, in the dislocation core region, using first principles calculations [8-16].

When the solutes are outside the core region, dislocation-solute interactions are dominated by elasticity and the dislocation core structure is hardly affected by the presence of solutes. However, when the solutes enter the core region, they may have a more pronounced effect. In particular, a study in Fe(C) based on Density Functional Theory (DFT) calculations has shown that carbon interstitial solutes can stabilize the hard core configuration of the $\langle 111\rangle$ screw dislocation [17], a configuration which is unstable in pure body-centered cubic (bcc) metals, where the dislocation adopts a symmetrical easy core configuration while all other core configurations - the asymmetrical core, the split core and the hard core - are unstable [18-26]. More recently, the same reconstruction was observed in non-magnetic bcc transition metals from group 6 (Mo and W) in presence of C atoms [27].

In the hard core configuration of the decorated dislocation line illustrated on the right side of Fig. 1, the carbon atoms are at the center of regular trigonal prisms formed by the iron atoms inside the three $\langle 111\rangle$ atomic columns of the dislocation core. Such prisms are similar to the unit building block of cementite, $Fe_3C$, as well as of hexagonal WC and MoC, the stoichiometric stable carbides of group 6 transition metals [27]. In iron, the interaction between carbon atoms and the screw dislocation is so attractive that the reconstruction occurs spontaneously upon relaxation for dislocation positions within a radius of about $3.5$ Å from a row of carbon atoms separated by one Burgers vector, $b$, as illustrated in Fig. 2.

Preliminary calculations, not presented here, show that the Peierls stress of the reconstructed core dragging along its solute atoms is higher than 10 GPa. This reconstructed core may thus play an important role in the plasticity of ferritic steels and it is important to investigate how general the core reconstruction is with other interstitial solutes in bcc iron.

To assess the generality of the core reconstruction observed in Fe(C) and analyze its origin, we performed DFT calculations in Fe in presence of interstitial solutes close to C in the periodic table: B, N and O. Nitrogen for instance is known to induce strain-ageing

* Corresponding author.
E-mail address: lisa.ventelon@cea.fr (L. Ventelon).

https://doi.org/10.1016/j.commatsci.2018.02.016
0927-0256/© 2018 Published by Elsevier B.V.

![](./images/813058904765235200_1.jpg)
![](./images/813058904765235200_2.jpg)
![](./images/813058904765235200_3.jpg)

![](./images/813058904765235200_4.jpg)

Fig. 1. Schematic representation of the core reconstruction of the screw dislocation in bcc Fe induced by the segregation of carbon solutes. Fe atoms are in gray, solutes in red. On the left: easy core with interstitial carbon atoms in solid solution; the octahedral cage is shown around one of the solutes, with two first nearest neighbors (in dark gray) and four second nearest neighbors (in light gray). On the right: reconstructed core in the hard configuration after segregation of carbon atoms with a separation of $1b$. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813058904765235200_5.jpg)

Fig. 2. Representation in the (1 1 1) plane of the initial configurations leading to a spontaneous reconstruction into a hard core structure decorated by carbon atoms. The red hashed downward triangle and the red circle represent the final configuration with the solute at the center of the dislocation in its hard core configuration. The green sphere is the initial octahedral-like position for the carbon atom and the colored upward triangles are the initial positions for the easy core dislocation. $E_i$ stands for the $i^{th}$ neighboring position to the initial carbon position. The gray triangle represents the only configuration where the reconstruction was not spontaneous, but the resulting configuration was of higher energy than the configuration centered on the hard core. Gray, black and white spheres are the iron atoms projected in the (1 1 1) plane. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

in iron [28]. Thereafter, we will refer to these systems using the notations Fe(X), where X = B, C, N or O.

### 2. Methodology

The DFT calculations were performed with VASP [29] using the Projector Augmented Wave (PAW) pseudopotential scheme [30,31] within the Perdew-Burke-Ernzerhof (PBE) Generalized Gra- dient Approximation (GGA). A pseudopotential without semicore electrons was used for Fe and pseudopotentials with 2s and 2p valence states were used for B, C, N and O. All calculations were spin-polarized and performed at constant supercell volume with a 0.2 eV Methfessel-Paxton broadening and a 400 eV kinetic- energy cutoff. Atomic positions were relaxed with a convergence criterion on forces of $10^{-2}$ eV/Å. For the dislocation calculations, a quadrupolar periodic array of dislocation dipoles was used as in several previous studies of screw dislocations in bcc metals [20,19,27]. As detailed below, two interstitials were introduced, one near each dislocation, forming two rows of solutes through the periodic boundary conditions. The length of the cell in the $\langle 1\ 1\ 1\rangle$ direction of the dislocation lines, was either $1b$ or $2b$, in order to vary the separation distance between solute atoms along the dislocation lines. We have checked that the distance between solute rows in the (1 1 1) plane is large enough to avoid cross inter- actions [27].

The cells contained 2 solute atoms and either 135 or 270 Fe atoms. $1\times 2\times 16$ and $1\times 2\times 8$ shifted $k$-point grids were used for solute-solute distances of $1b$ and $2b$ respectively. Bulk and interstitial solute calculations without dislocations were per- formed in a 250-atom simulation cell and a $4\times 4\times 4$ shifted $k$-point grid. $\text{Fe}_3\text{C}$ calculations were done using a 16-atom unit cell with a $10\times 8\times 12$ shifted $k$-point grid.

The dislocation dipole was initially relaxed in pure iron in the easy core configuration, i.e. the minimum-energy position in pure bcc metals. Two solute atoms were then introduced in octahedral- like interstitial positions, first nearest-neighbors to each disloca- tion core. This configuration is noted $E_1$ in Fig. 2 (and corresponds to the $O^{(1)}$ position in Ref. [17]). The system was then relaxed to determine whether a spontaneous reorganization occured.

The interaction energy per solute atom between the dislocation and the solute atoms, $E_{\text{int}}$ is defined as:
$$
E_{\text{int}}=E_{\text{d}}-E_{\infty},\tag{1}
$$
where $E_{\text{d}}$ is the energy when the solute is located near a dislocation core and $E_{\infty}$ is the energy when the solute is infinitely separated from the dislocation core. Thus, negative energies correspond to attractive interactions. $E_{\text{d}}$ and $E_{\infty}$ are computed as:
$$
E_{\text{d}}=\frac{1}{2}E_{\text{dislo+X}}+E_{\text{bulk}},\ E_{\infty}=\frac{1}{2}E_{\text{dislo}}+E_{\text{X}}.\tag{2}
$$

The factor $\frac{1}{2}$ comes from the presence of two solute atoms and two dislocations within the simulation cell. $E_{\text{dislo+X}}$ (respectively $E_{\text{dislo}}$) is the energy of a cell containing a dislocation dipole with (respectively without) solute atoms in the vicinity of the cores. In the reference configuration, the dislocations are in their easy core and therefore $E_{\text{dislo}}=E_{\text{easy}}$ is the energy of a cell with a dipole of easy-core dislocations of length $1b$ or $2b$ depending on the separa- tion between solutes. $E_{\text{X}}$ (respectively $E_{\text{bulk}}$) is the energy of a per- fect bcc cubic cell with (respectively without) a solute atom in its most stable position. The preferred position for C, N and O solutes in the bcc iron lattice is the octahedral position illustrated on the left side of Fig. 1, in agreement with previous studies [32-36] (Table 1). Note that in the case of boron solutes, the most stable position is substitutional, in agreement with other DFT calculations [37,36,38]. However, the solution energy in the octahedral intersti- tial position is only slightly larger (+0.17 eV). For the sake of a more direct comparison with other solutes, we will consider here that B is also interstitial in the vicinity of the dislocation.

The DFT calculations of the solute-dislocation interaction energy for solute separation distances of $1b$ (denoted $E_{\text{int}}(1b)$) and $2b$ (denoted $E_{\text{int}}(2b)$) along the dislocation line allow us to extract the first-neighbor interaction energy between solute atoms along the dislocation line, $V_{\text{XX}}$. As will be seen below, the interac- tion between solutes is mainly limited to first neighbors along $\langle 1\ 1\ 1\rangle$. In this case, $V_{\text{XX}}$ can be expressed as:
$$
V_{\text{XX}}=E_{\text{int}}(1b)-E_{\text{int}}(2b)+\Delta E_{\text{hard-easy}},\tag{3}
$$

Table 1
Solution energy differences (in eV) between tetrahedral and octahedral solute positions ($\Delta E_{t-o}$) and substitutional and octahedral solute positions ($\Delta E_{s-o}$) in a bcc iron lattice, calculated within DFT-GGA using the VASP code. In Ref. [36] 128-atom cubic cells were used taking into account the elastic correction [39].

<table>
<thead>
<tr>
<th>
</th>
<th>
</th>
<th>
B
</th>
<th>
C
</th>
<th>
N
</th>
<th>
O
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">
This work
</td>
<td>$\Delta E_{t-o}$</td>
<td>0.67</td>
<td>0.86</td>
<td>0.72</td>
<td>0.50</td>
</tr>
<tr>
<td>$\Delta E_{s-o}$</td>
<td>–0.17</td>
<td>2.27</td>
<td>2.90</td>
<td>1.52</td>
</tr>
<tr>
<td rowspan="2">
Ref. [36]
</td>
<td>$\Delta E_{t-o}$</td>
<td>0.67</td>
<td>0.87</td>
<td>0.73</td>
<td>0.52</td>
</tr>
<tr>
<td>$\Delta E_{s-o}$</td>
<td>–0.10</td>
<td>2.33</td>
<td>2.97</td>
<td>1.59</td>
</tr>
</tbody>
</table>

with $\Delta E_{\text{hard--easy}}$, the cost to transform a dislocation segment of length $1b$ from an easy to a hard core. The contribution $\Delta E_{\text{hard--easy}}$ in Eq. (3) comes from the fact that $V_{\text{XX}}$ is defined with the hard core configuration as reference, while the dislocation-solute interaction energy is calculated with respect to the easy core. The DFT value obtained for $\Delta E_{\text{hard--easy}}$ in Fe is $40\,\text{meV}/b$, in good agreement with previous DFT calculations performed with the PWSCF code [19]. Using the definitions in Eq. (2), $V_{\text{XX}}$ can be equivalently written as:

$$
V_{\text{XX}} = \frac{1}{2}\left(E_{\text{dislo+X}}(1b) + E_{\text{hard}}(1b) - E_{\text{dislo+X}}(2b)\right), \tag{4}
$$

where $E_{\text{hard}}(1b)$ is the energy of a cell with a dipole of hard-core dislocations of length $1b$.

In the following, $V_{\text{XX}}$ will be compared to the interaction energy between solute atoms in bulk octahedral sites separated by either $1b$ or $2b$ along the $\langle 1\,1\,1\rangle$ direction. These interaction energies, denoted $V_{\text{XX}}^{\text{bulk}}(d_{\text{XX}})$ with $d_{\text{XX}}=1b$ or $2b$, are calculated as:

$$
V_{\text{XX}}^{\text{bulk}}(d_{\text{XX}}) = E_{2\text{X}}(d_{\text{XX}}) + E_{\text{bulk}} - 2E_{\text{X}}, \tag{5}
$$

where $E_{2\text{X}}(d_{\text{XX}})$ is the energy of a perfect bcc cubic cell containing two solute atoms in octahedral positions separated by a distance $d_{\text{XX}}$ along $(1\,1\,1)$. From Eqs. (3) and (5), a negative value for $V_{\text{XX}}$ and $V_{\text{XX}}^{\text{bulk}}(d_{\text{XX}})$ means an attraction between the solute atoms.

## 3. Results and discussion

### 3.1. Core reconstruction and interaction energies

The stability of the $E_1$ octahedral position near a dislocation (see Fig. 2) was investigated for solutes X = B, C, N and O in Fe and for two X-X distances along the $\langle 1\,1\,1\rangle$ direction, $d_{\text{XX}}=1b$ and $2b$. A spontaneous reconstruction of the dislocation core towards the hard core was evidenced for every solute and for both solute separation distances. As in Fe(C), the solute atoms are at the center of regular trigonal prisms of iron atoms. One exception is Fe(N) with $d_{\text{NN}}=1b$, where the dislocation core stays in the easy configuration and moves away from the nitrogen atom. The energy of this configuration is however higher than the reconstructed configuration obtained by introducing directly the N solute atoms into the dislocation hard core. In other words, in this case the reconstruction towards the hard core is energetically favorable but not spontaneous.

For each Fe(X) system, the interaction energies between the dislocation and the solutes were calculated for $d_{\text{XX}}=1b$ and $2b$. Fig. 3 shows that the interaction is always attractive and strong, varying from about $-1.3\,\text{eV}$ to $-0.2\,\text{eV}$ for $d_{\text{XX}}=1b$ and from $-1.2\,\text{eV}$ to $-0.6\,\text{eV}$ for $d_{\text{XX}}=2b$. A decrease, in absolute value, of the interaction energy from boron to carbon and carbon to nitrogen and an increase from nitrogen to oxygen is evidenced for both $1b$ and $2b$ distances. Based on these results, the X-X interaction energies along the dislocation line, $V_{\text{XX}}$, were computed using Eq. (3). For comparison, the X-X interaction energies in bulk, $V_{\text{XX}}^{\text{bulk}}(1b)$ and $V_{\text{XX}}^{\text{bulk}}(2b)$ were also calculated from Eq. (5) and are in agreement with Ref. [40]. In bulk, for a distance of $1b$ between the two solutes along $(1\,1\,1)$, the N-N and C-C interactions are strongly repulsive (resp. $+0.22\,\text{eV}$ and $+0.32\,\text{eV}$), while the B-B and O-O interactions are weakly attractive (resp. $-0.02\,\text{eV}$ and $-0.08\,\text{eV}$) (see Fig. 4). Upon increasing the distance between solutes to $2b$ in the bulk, the interaction energies fall to zero in all cases (see Fig. 4), justifying to consider in Eq. (3) only a first nearest neighbor interaction between solutes along the dislocation line. The interaction between solute atoms is remarkably similar between bulk and dislocation sites. One exception is O, with a strongly repulsive interaction along the dislocation line $(+0.24\,\text{eV})$ compared to a weak attraction in bulk, but the latter is known to be atypical [40]. For the other systems, the interaction is weakly attractive in Fe(B) and strongly repulsive in Fe(N) and Fe(C), both in bulk and in the dislocation core.

![](./images/813058904765235200_6.jpg)

Fig. 3. Dislocation-solute interaction energy ($E_{\text{int}}$ in Eq. (1)) calculated for distances along $\langle 1\,1\,1\rangle$ of $1b$ and $2b$. The different colors represent different references for the solute atom: red is for the octahedral position and blue for the substitutional position (only in the case of B as it is the most stable position in bulk). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

### 3.2. Voronoi volumes and lattice distortion

As noted in Ref. [17], the local environment around a solute atom in a prismatic site, namely, the number of neighbors (six) and interatomic distances, is comparable to that in the bulk octahedral site, although we should note that while in the prismatic site, all six neighbors are equidistant, the octahedral site in the bcc lattice is distorted with two first nearest neighbors (1NN) and four second nearest neighbors (2NN), as illustrated in Fig. 1. It is therefore not surprising that these two sites have similar solute energies. However, we have seen in Fig. 3 that the prismatic site is systematically more favorable.

As a first step to explain the higher stability of the prismatic site, we compared the Voronoi volumes for all solute atoms, before and after relaxation, for both the octahedral and prismatic sites. Since the interaction between solutes is negligible for $d_{\text{XX}}=2b$, in the following we will compare the isolated bulk octahedral site and the prism configuration with one solute every $2b$ (denoted below $2b$ prism), considering this configuration also as isolated. The results reported in Table 2 show that the unrelaxed volume is about 15% larger for the prismatic site, which already goes in the direction of favoring this site, since as a general rule, interstitial solutes prefer larger insertion sites. After relaxation, the Voronoi volume of the prismatic site is still larger than the octahedral site,

![](./images/813058904765235200_7.jpg)

Fig. 4. Interaction energy between solute atoms along the $\langle 1\,1\,1\rangle$ direction when they are introduced in their octahedral sites in bulk Fe and inside the dislocation hard core.

<table>
<caption>Table 2 Unrelaxed and relaxed Voronoi volumes (in $\AA^3$) for the isolated solute in octahedral position in the bulk and for the solute in the prism configuration for $d_{xx}=2b$.</caption>
<tbody>
<tr>
<td>
</td>
<td>
</td>
<td>
B
</td>
<td>
C
</td>
<td>
N
</td>
<td>
O
</td>
</tr>
<tr>
<td>
Octa.
</td>
<td>
Unrelaxed
</td>
<td>
</td>
<td>
</td>
<td>
5.67
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
Relaxed
</td>
<td>
7.33
</td>
<td>
6.89
</td>
<td>
6.82
</td>
<td>
7.29
</td>
</tr>
<tr>
<td>
Prism
</td>
<td>
Unrelaxed
</td>
<td>
</td>
<td>
</td>
<td>
6.58
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
Relaxed
</td>
<td>
7.56
</td>
<td>
7.25
</td>
<td>
7.21
</td>
<td>
7.63
</td>
</tr>
</tbody>
</table>

but only by approximately 5%, depending on the solute. This suggests that, after relaxation, the matrix is more deformed around an octahedral than a prismatic site. We therefore expect that a larger strain energy is stored in the lattice for the octahedral site, which reinforces the stability of the prismatic site. Following Ref. [40], we calculated a lattice distortion energy, defined as the energy difference between two systems without solutes. The reference energy corresponds to the relaxed system without solute, i.e. in the present case either the perfect crystal or the relaxed hard core configuration (although unstable, this configuration can be relaxed by constraining the three atomic columns in the core to remain at the same altitude). The energy of the distorted system is obtained by inserting the solute, relaxing the system, removing the solute and calculating the energy without further relaxation. As reported in Table 3, we find that, as anticipated, the lattice distortion energies are much larger for the octahedral site.

The solute-dislocation interaction energy, $E_{\text{int}}$ in Eq. (1), can be estimated by adding the lattice distortion energy difference and the energy difference between the hard and easy cores over a distance of $2b$, i.e. 0.08 eV. The resulting estimates are compared in Table 3 to the DFT values for $d_{xx}=2b$ shown in Fig. 3. This comparison shows that the lattice distortion energy accounts for a large part of the solute-dislocation interaction energy. With the exception of Fe(B), we even find a quantitative agreement within 0.2 eV.

The lattice distortion energy can be analyzed in more details by looking at the amplitude of atomic displacements. As expected, the shortest bonds, i.e. the bonds with the two nearest neighbors of the octahedral site, have the largest displacements. These atoms relax in order to create an environment around the interstitial solute more isotopic than the original octahedral environment in pure iron. A large contribution to the lattice distortion energy of the octahedral site is therefore due to the fact that the first nearest neighbors do not form a perfect octahedron.

In brief, our analysis suggests that the high stability of the prismatic site compared to the octahedral site is mainly due to a geometrical effect: the prismatic site has 6 equidistant nearest neighbors and a larger Voronoi volume, therefore inducing less strain in the matrix.

### 3.3. Magnetism and electronic structure

In order to further explore how the Fe lattice is distorted upon solute insertion, we calculated the Voronoi volumes and local magnetic moments on the nearest neighbors of the solute atoms, for a solute inserted in a bulk octahedral site and in a prismatic dislocation core site for $d_{xx}=1b$ and $2b$. The results, displayed in Fig. 5, show that B, C, and N yield very similar values for both quantities for a given type of Fe site. On the other hand, O solutes induce larger Voronoi volumes and local magnetic moments. Fig. 5 shows that for every type of site octahedral 1NN, octahedral 2NN, 1b prism and 2b prism there is a clear correlation between Voronoi volume and magnetic moment, consistent with the so-called magnetovolume effect [40-44]. In other words, the local magnetic moment acts as a probe for local volume changes. We also note that, for a given type of Fe site, the Voronoi volume change due to solute insertion varies significantly from B to O whereas these

<table>
<caption>Table 3 Lattice distortion energies (in eV) for the octahedral and prismatic configurations with a solute separation distance of $2b$. $\Delta$(P-O) is the lattice distortion energy difference between the prismatic and octahedral sites. An estimate of the solute-dislocation interaction energy, $\Delta$(P-O) $+ 2\Delta E_{\text{hard-easy}}$, (see text for details) is compared to the direct DFT calculation for $d_{xx}=2b$ as plotted in Fig. 3 and reported in the last line of the table.</caption>
<tbody>
<tr>
<td>
</td>
<td>
B
</td>
<td>
C
</td>
<td>
N
</td>
<td>
O
</td>
</tr>
<tr>
<td>
Octa. position
</td>
<td>
1.41
</td>
<td>
1.08
</td>
<td>
1.03
</td>
<td>
1.36
</td>
</tr>
<tr>
<td>
Prism (2b)
</td>
<td>
0.50
</td>
<td>
0.22
</td>
<td>
0.21
</td>
<td>
0.50
</td>
</tr>
<tr>
<td>
$\Delta$(P-O) $+ 2\Delta E_{\text{hard-easy}}$
</td>
<td>
$-$0.83
</td>
<td>
$-$0.78
</td>
<td>
$-$0.74
</td>
<td>
$-$0.78
</td>
</tr>
<tr>
<td>
Interaction energy
</td>
<td>
$-$1.20
</td>
<td>
$-$0.75
</td>
<td>
$-$0.56
</td>
<td>
$-$0.72
</td>
</tr>
</tbody>
</table>

![](./images/813058904765235200_8.jpg)

Fig. 5. Variation of the magnetic moment of iron atoms as a function of their Voronoi volume for first- and second-nearest neighbors (1NN and 2NN) of the solute in bulk octahedral site, and in the prismatic sites of the dislocation core for solutes separated by $1b$ and $2b$. The moments for bulk, easy and hard cores are shown for comparison. The lines are guides for the eyes.

![](./images/813058904765235200_9.jpg)

Fig. 6. Total projected local density of states with boron solute atoms. The upper part of the graph compares the octahedral configuration to pure bcc iron and the middle part compares the prism configuration with $d_{xx}=2b$ and $1b$ and the dislocation in pure bcc iron in its easy configuration. For the octahedral configuration, the total local density of states for the iron atoms is averaged over the six nearest neighbors.

two solutes have similar solute Voronoi volumes. This result shows that the lattice relaxation close to the solute deviates from linear elasticity and that bonding between Fe atoms is itself affected by the nature of the solute. This can be seen as a consequence of the very different nature of the Fe-X bonds, which varies from covalent with B to ionic with O [40].

Finally, as a first step towards analyzing the chemical origin of the similarities and discrepancies observed in the interaction energies, we calculated the local density of states (LDOS) on the solutes and on their nearest neighbors, for the octahedral and trigonal prismatic sites (see Figs. 6-9). Concerning the comparison between the octahedral and prismatic $2b$ configurations, we note that: (i) for all solutes, the changes in the Fe LDOS are less pronounced when going from the easy core to the prism than from bulk to octahedral, consistent with a smaller lattice distortion energy; (ii) the hybridization between the solute p states and the metal states is stronger for the prismatic than the octahedral site. This is in particular the case for X = N (Fig. 8) where the p-state peak (around -7 eV) in the $2b$-prism configuration is much broader than in the octahedral site and extends to slightly higher energies, closer to the metal band LDOS. But further analysis is required to provide more quantitative insights into the link between the LDOS and the chemical contribution to the solute-dislocation interaction energies. It is also interesting to note the formation of X-X bonds when going from $2b$- to the $1b$-prism, as seen from the formation of s and p bands in the LDOS, suggesting a significant chemical contribution to the X-X interaction energy. In the case of C, a strong similarity

![](./images/813058904765235200_10.jpg)

Fig. 7. Same as Fig. 6 for X = C. The local density of states of cementite is also shown for comparison at the bottom. The average is made over the six iron atoms forming one prism.

![](./images/813058904765235200_11.jpg)

Fig. 8. Same as Fig. 6 for X = N.

![](./images/813058904765235200_12.jpg)

Fig. 9. Same as Fig. 6 for X = O.

is evidenced in the electronic structures of the $2b$-prism configuration and cementite (Fig. 7).

## 4. Summary and conclusions

In this paper the interaction between $1/2\langle111\rangle$ screw dislocations and interstitial solute atoms was investigated for different solutes (B, C, N and O) in $\alpha$-Fe. Our DFT calculations show that solute atoms stabilize the hard core configuration with the solutes

placed at the center of regular trigonal prisms formed by the metal atoms of the three $\langle 1\ 1\ 1 \rangle$ atomic columns of the hard core. The solute-dislocation interaction energy is strongly attractive in all cases, ranging from $-1.2$ eV to $-0.6$ eV when the solutes are separated by a distance of $2b$ for which they can be considered as non-interacting. The larger Voronoi volume of the trigonal prismatic site compared to the bulk octahedral site is proposed to be the main driving force for this strong attraction. A large part of this energy, about $-0.85$ eV, is attributed to the lattice distortion energy, and in particular to the relaxation of the two first nearest neighbors in the octahedral site. Chemical contributions, responsible for the solute dependence of the interaction energy, are suggested from the analysis of the local density of states. The nearest-neighbor solute-solute interaction along the dislocation is repulsive for C, N and O, and it vanishes for B, but in all cases the solute-dislocation interaction remains strongly attractive for a fully decorated dislocation line. As shown in the case of C in Ref. [17], a strong segregation of all solutes at the dislocation core is therefore expected at thermal equilibrium.

## Data availability

The raw data required to reproduce these findings cannot be shared at this time as the data also forms part of an ongoing study. The processed data required to reproduce these findings cannot be shared at this time as the data also forms part of an ongoing study.

## Acknowledgments

This work was performed using GENCI-CINES computer center under Grant No. 2015-096821, and the Partnership for Advanced Computing in Europe (PRACE) for awarding access to the SODIFE project to the Curie resources, based in France at the TGCC center. The authors acknowledge support from the ANR project DeGAS (ANR-16-CE08-0008). D.R. acknowledges support from LABEX iMUST (ANR-10-LABX-0064) of Université de Lyon (programme Investissements d'Avenir, ANR-11-IDEX-0007). This work has been carried out within the framework of the EUROfusion Consortium and has received funding from the Euratom research and training programme 2014-2018 under Grant Agreement No. 633053. The views and opinions expressed herein do not reflect those of the European Commission. Dr. C. Barouh, Dr. C.-C. Fu, Dr. E. Clouet and Dr. P. Olsson are acknowledged for fruitful discussions.

## References

[1] A.H. Cottrell, B.A. Bilby, Dislocation theory of yielding and strain ageing of iron, Proc. Phys. Soc. A 62 (1949) 49.

[2] D.L. Olmsted, L.G.J. Hector, W.A. Curtin, R.J. Clifton, Atomistic simulations of dislocation mobility in Al, Ni and Al/Mg alloys, Model. Simul. Mater. Sci. Eng. 13 (2005) 371.

[3] K. Tapasa, Y.N. Osetsky, D.J. Bacon, Computer simulation of interaction of an edge dislocation with a carbon interstitial in $\alpha$-iron and effects on glide, Acta Mater. 55 (2007) 93.

[4] E. Clouet, S. Garruchet, H. Nguyen, M. Perez, C.S. Becquart, Dislocation interaction with C in $\alpha$-Fe: a comparison between atomic simulations and elasticity theory, Acta Mater. 56 (2008) 3450.

[5] A. Ishii, J. Li, S. Ogata, Conjugate channeling effect in dislocation core diffusion: carbon transport in dislocated bcc iron, Plos One 8 (2013) e60586.

[6] K. Chockalingam, R. Janisch, A. Hartmaier, Coupled atomistic-continuum study of the effects of C atoms at $\alpha$-Fe dislocation cores, Model. Simul. Mater. Sci. Eng. 22 (2014) 075007.

[7] R.G.A. Veiga, H. Goldenstein, M. Perez, C.S. Becquart, Monte Carlo and molecular dynamics simulations of screw dislocation locking by Cottrell atmospheres in low carbon Fe-C alloys, Scripta Mater. 108 (2015) 19.

[8] D.R. Trinkle, C. Woodward, The chemistry of deformation: how solutes soften pure metals, Science 310 (2005) 1665.

[9] N.I. Medvedeva, Y.N. Gornostyrev, A.J. Freeman, Solid solution softening and hardening in the group-V and group-VI bcc transition metals alloys: first principles calculations and atomistic modeling, Phys. B 76 (2007) 212104.

[10] L. Romaner, C. Ambrosch-Draxl, R. Pippan, Effect of rhenium on the dislocation core structure in tungsten, Phys. Rev. Lett. 104 (2010) 195503.

[11] Y. Zhao, G. Lu, QM/MM study of dislocation-hydrogen/helium interactions in $\alpha$-Fe, Model. Simul. Mater. Sci. Eng. 19 (2011) 065004.

[12] H. Li, S. Wurster, C. Motz, L. Romaner, C. Ambrosch-Draxl, R. Pippan, Dislocation-core symmetry and slip planes in tungsten alloys: ab initio calculations and microcantilever bending experiments, Acta Mater. 60 (2012) 748.

[13] M. Itakura, H. Kaburaki, M. Yamaguchi, T. Okita, The effect of hydrogen atoms on the screw dislocation mobility in bcc iron: a first-principles study, Acta Mater. 61 (2013) 6857.

[14] G.D. Samolyuk, Y.N. Osetsky, R.E. Stoller, The influence of transition metal solutes on the dislocation core structure and values of the Peierls stress and barrier in tungsten, J. Phys.: Condens. Matter 25 (2013) 025403.

[15] L. Romaner, V.I. Razumovskiy, R. Pippan, Core polarity of screw dislocations in Fe-Co alloys, Philos. Mag. Lett. 94 (2014) 334.

[16] D. Rodney, L. Ventelon, E. Clouet, L. Pizzagalli, F. Willaime, Ab initio modeling of dislocation core properties in metals and semi-conductors, Acta. Mater. 124 (2017) 633.

[17] L. Ventelon, B. Lüthi, E. Clouet, L. Proville, B. Legrand, D. Rodney, F. Willaime, Dislocation core reconstruction induced by carbon segregation in bcc iron, Phys. Rev. B 91 (2015) 220102(R).

[18] L. Ventelon, F. Willaime, Core structure and Peierls potential of screw dislocations in $\alpha$-Fe from first principles: cluster versus dipole approaches, J. Comput.-Aided Mater. Des. 14 (2007) 85.

[19] L. Dezerald, L. Ventelon, E. Clouet, C. Denoual, D. Rodney, F. Willaime, Ab initio modeling of the two-dimensional energy landscape of screw dislocations in bcc transition metals, Phys. Rev. B 89 (2014) 024104.

[20] L. Ventelon, F. Willaime, E. Clouet, D. Rodney, Ab initio investigation of the Peierls potential of screw dislocations in bcc Fe and W, Acta Mater. 61 (2013) 3973.

[21] C.R. Weinberger, G.J. Tucker, S.M. Foiles, Peierls potential of screw dislocations in bcc transition metals: predictions from density functional theory, Phys. Rev. B 87 (2013) 054114.

[22] M. Itakura, H. Kaburaki, M. Yamaguchi, First-principles study on the mobility of screw dislocations in bcc iron, Acta Mater. 60 (2012) 3698.

[23] E. Clouet, L. Ventelon, F. Willaime, Dislocation core energies and core fields from first principles, Phys. Rev. Lett. 102 (2009) 055502.

[24] C. Domain, G. Monnet, Simulation of screw dislocation motion in iron by molecular dynamics simulations, Phys. Rev. Lett. 95 (2005) 215506.

[25] C. Woodward, S.I. Rao, Ab-initio simulation of isolated screw dislocations in bcc Mo and Ta, Philos. Mag. A 81 (2001) 1305.

[26] S. Ismail-Beigi, T.A. Arias, Ab initio study of screw dislocations in Mo and Ta: a new picture of plasticity in bcc transition metals, Phys. Rev. Lett. 84 (2000) 1499.

[27] B. Lüthi, L. Ventelon, C. Elsässer, D. Rodney, F. Willaime, First principles investigation of carbon-screw dislocation interactions in body-centered cubic metals, Model. Simul. Mater. Sci. Eng. 25 (2017) 084001.

[28] J.D. Baird, The effects of strain-ageing due to interstitial solutes on the mechanical properties of metals, Metall. Rev. 16 (1971) 1.

[29] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169.

[30] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953.

[31] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758.

[32] D.E. Jiang, E.A. Carter, Carbon dissolution and diffusion in ferrite and austenite from first principles, Phys. Rev. B 67 (2003) 214103.

[33] C.-C. Fu, E. Meslin, A. Barbu, F. Willaime, V. Oison, Effect of C on vacancy migration in $\alpha$-iron, Solid State Phenom. 139 (2008) 157.

[34] A. Claisse, P. Olsson, First-principles calculations of (Y, Ti, O) cluster formation in body centred cubic iron-chromium, Nucl. Instr. Meth. Phys. Res. B 303 (2013) 18.

[35] M.H. Wu, X.H. Liu, J.F. Gu, Z.H. Jin, First-principles simulations of iron with nitrogen: from surface adsorption to bulk diffusion, Model. Simul. Mater. Sci. Eng. 21 (2013) 045004.

[36] M. Souissi, Y. Chen, M.H.F. Sluiter, H. Numakura, Ab initio characterization of B, C, N and O in bcc iron: solution and migration energies and elastic strain fields, Comput. Mater. Sci. 124 (2016) 249.

[37] A.F. Bialon, T. Hammerschmidt, R. Drautz, Ab initio study of boron in $\alpha$-iron: migration barriers and interaction with point defects, Phys. Rev. B 87 (2013) 104109.

[38] S.S. Baik, B.I. Min, S.K. Kwon, Y.M. Koo, Boron solution and distribution in $\alpha$-Fe: application to boron steel, Phys. Rev. B 81 (2010) 144101.

[39] C. Varvenne, F. Bruneval, M.-C. Marinica, E. Clouet, Point defect modeling in materials: coupling ab initio and elasticity approaches, Phys. Rev. B 88 (2013) 134102.

[40] C. Barouh, T. Schuler, C.-C. Fu, M. Nastar, Interaction between vacancies and interstitial solutes (C, N and O) in $\alpha$-Fe: from electronic structure to thermodynamics, Phys. Rev. B 90 (2014) 054112.

[41] I. Turek, J. Hafner, Magnetism of amorphous iron: from ferromagnetism to antiferromagnetism and spin-glass behavior, Phys. Rev. B 46 (1992) 247.

[42] P.-W. Ma, W.C. Liu, C.H. Woo, S.L. Dudarev, Large-scale molecular dynamics simulation of magnetic properties of amorphous iron under pressure, J. Appl. Phys. 101 (2007) 073908.

[43] L. Zhang, C.-C. Fu, G.-H. Lu, Energetic landscape and diffusion of He in $\alpha$-Fe grain boundaries from first principles, Phys. Rev. B 87 (2013) 134107.

[44] L. Zhang, M. Šob, Z. Wu, Y. Zhang, G.-H. Lu, Characterization of iron ferromagnetism by the local atomic volume: from three-dimensional structures to isolated atoms, J. Phys.: Condens. Matter 26 (2014) 086002.