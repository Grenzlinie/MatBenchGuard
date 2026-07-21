![](./images/812409713714003968_1.jpg)

Available online at www.sciencedirect.com

![](./images/812409713714003968_2.jpg)

Surface Science 532-535 (2003) 898-904

![](./images/812409713714003968_3.jpg)

www.elsevier.com/locate/susc

# Adsorption and diffusion on nanoclusters of $C_{60}$ molecules

F. Baletto $^{a, *}$, J.P.K. Doye $^{b}$, R. Ferrando $^{a}$, C. Mottet $^{c}$

$^{a}$ INFM, Dipartimento di Fisica, Universita di Genova, via Dodecaneso 33, Genova I-16146, Italy
$^{b}$ Department of Chemistry, University of Cambridge, Lensfield Road, Cambridge, UK
$^{c}$ CRMC²/CNRS, Campus de Luminy, Marseille, France

## Abstract
The adsorption and the energy barriers for diffusion on clusters of $C_{60}$ molecules are studied by means of quenched molecular dynamics simulations. The interaction among the $C_{60}$ molecules is modeled by means of the Girifalco potential. Three different clusters structures are considered: a truncated octahedron of 38 molecules, an icosahedron of 55 molecules and a truncated decahedron of 75 molecules.

© 2003 Elsevier Science B.V. All rights reserved.

Keywords: Clusters; Molecular dynamics; Adsorption kinetics; Fullerenes; Diffusion and migration; Growth

## 1. Introduction
Nanoclusters can present peculiar structures, which can be qualitatively different from those obtained by cutting a bulk solid. Since that the constraint of translational invariance has not to be imposed on nanoclusters, structures presenting fivefold symmetries are possible [1]. Among these structures, the most common are icosahedra (Ih) and truncated decahedra (Dh) (see Fig. 1). These three structural motifs morphologies have different energetic properties. Atomic distances in Ih clusters are strongly distorted with respect to ideal bulk values, and this causes an internal strain, which is proportional to the cluster volume. On the other hand, Ih clusters have a quasi-spherical shape, and a close-packed surface. Because of that, Ih structures are energetically favourable when the surface/volume ratio is high, i.e. at small sizes. On the other hand, pieces of the bulk volume, like the truncated octahedron (TO), have no internal strain but do not optimize the surface energy, either because their shape is far from being spherical, or because they have large open facets. This indicates that TO become favourable at large sizes. Deca- hedral structures are in between: they have less internal strain than Ih, but a better surface energy than TO. The sequence of the most stable structures will thus be Ih at small sizes, Dh at intermediate sizes and TO at large sizes [2–4]. The crossover sizes between Ih and Dh, and between Dh and TO are in general material-dependent [4].

The case of clusters of $C_{60}$ molecules is very interesting from this point of view. The interaction potential between $C_{60}$ molecules is extremely sticky, being characterized by a very narrow well compared to the size of the $C_{60}$ molecule. Because of that, strained structures such as Ih are extremely unfavourable, and the crossover size between Ih and Dh takes places already at very small sizes,

* Corresponding author. Tel.: +39-10-3536214; fax: +39-10-311066.
E-mail address: baletto@fisica.unige.it (F. Baletto).

0039-6028/03/$ - see front matter © 2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0039-6028(03)00135-3

![](./images/812409713714003968_4.jpg)

Fig. 1. From top to bottom, top and side views of $TO_{38}$, $Ih_{55}$ and $Dh_{75}$. The $TO_{38}$ presents six square (1 0 0) facets, the $Ih_{55}$ is limited only by triangular (1 1 1) facets and the $Dh_{75}$ presents square (1 0 0) facets on its side, which are separated by reentrances exposing (1 1 1) facets. In the third column we show the adsorption sites on the (1 1 1) facets for the three clusters. On the $Dh_{75}$, neither sites A, C, E nor B, D sites are equivalent due to the presence of edges. Contrary to silver clusters, on $C_{60}$ clusters the sites along the edges are slightly less favourable.

such as $N=15$ [5], where $N$ is the number of molecules in the cluster. On the other hand, ex- periments [6,7] have shown that much larger Ih are produced, and that Dh and TO structures can be obtained after annealing at high temperatures. The production of large Ih has been interpreted by molecular dynamics simulations of cluster growth [8] as resulting from kinetic trapping effects. The cluster initially grows as a small, thus energetically favourable, icosahedron; adding further molecules the structure grows around this small icosahedron preserving the initial symmetry, because the full rearrangement of the icosahedron into a more stable structure is extremely difficult due to the stickiness of the potential. Moreover, even if small Dh are formed (around $N\sim 25$), a transforma- tion of these Dh into larger Ih takes place via the nucleation of islands on hcp sites, (a decahedron plus an hcp island is a part of a larger icosahedron) as happens in the case of silver clusters [13,14].

In order to understand the microscopic mecha- nisms leading to kinetic trapping phenomena, the study of the adsorption of molecules on clusters surfaces and of the barriers of the elementary diffusion mechanisms is extremely important. We calculate an energetic map for the adsorption of molecules above it, and then the barriers for the most important diffusion processes. We consider three different clusters structures: a TO of 38 molecules, an Ih of 55 molecules and a truncated Dh of 75 molecules ($TO_{38}$, $Ih_{55}$ and $Dh_{75}$ respec- tively). According to global-energy optimizations with different interaction potentials [5], the $TO_{38}$ and the $Dh_{75}$ are lowest-energy structures at their sizes, while the $Ih_{55}$ is not. In spite of that, the growth simulations [8] have shown that the $Ih_{55}$ is always obtained, while the $TO_{38}$ is never found, and the $Dh_{75}$ is very rare.

The paper is structured as follows. In Section 2 we describe the model and the method; in Section

3 we show the results and Section 4 contains the conclusions.

## 2. Model and method

The interaction between $C_{60}$ molecules is modelled by the Girifalco [9] potential, which is a pair potential obtained assuming a spherical shape for the molecule and an uniform distribution of Lennard-Jones centers on its surface. In this framework, the total energy reads

$$
\begin{aligned}
E= & -\alpha \sum_{i<j}\left[\frac{1}{s_{i j}\left(s_{i j}-1\right)^{3}}+\frac{1}{s_{i j}\left(s_{i j}+1\right)^{3}}-\frac{2}{s_{i j}^{4}}\right] \\
& +\beta \sum_{i<j}\left[\frac{1}{s_{i j}\left(s_{i j}-1\right)^{9}}+\frac{1}{s_{i j}\left(s_{i j}+1\right)^{9}}-\frac{2}{s_{i j}^{10}}\right],
\end{aligned}
$$

where $s_{i j}=r_{i j} / 2 a$, with $r_{i j}$ separation between the centres of molecules $i$ and $j$ of radius $a$. The constants $\alpha$ and $\beta$ are given by $\alpha=3600 A / 768 a^{6}$ and $\beta=3600 B / 368640 a^{12}$, with $A$ and $B$ coefficients of the attractive and repulsive terms in the Lennard-Jones carbon-carbon potential. The use of more sophisticated potentials [10] has not given qualitative differences in the growth simulations [8]. In Fig. 2 we compare the Girifalco potential with a Lennard-Jones potential with the same equilibrium distance and the same well depth, and a Lennard-Jones potential with the RGL potential for silver. It is clear that the Girifalco potential has a much narrower well than the others, while the silver potential is the softest.

The adsorption energetics of $C_{60}$ molecules on the cluster surface have been calculated by quenched molecular dynamics, while the energy barriers have been obtained by the nudged elastic band (NEB) method [11]. Some technical considerations are necessary before using the NEB method with the Girifalco potential: in fact, the stickiness of the potential and the presence of an infinite repulsive part at non-zero distance imply that the convergence depends strongly on the choice of the initial images to be relaxed. These initial images must be already quite close to the mimimum-energy path, otherwise the convergence is not obtained. A trick to facilitate the convergence is to start the NEB with a mild elastic constant, which allows an easier displacement of the images. The images obtained after relaxation with a mild elastic constant are then used as starting images for running the NEB with a stiffer elastic constant, which insures a better positioning along the minimum-energy path.

## 3. Results

### 3.1. Adsorption energies

A truncated octahedron (TO) is obtained by cutting off the apices of an octahedron with a square

![](./images/812409713714003968_5.jpg)

Fig. 2. Left panel: comparison of the RGL potential for a silver dimer (—) with a Lennard-Jones potential with same equilibrium position and same well depth $(\cdots)$ . Right panel: comparison of the Girifalco potential (—) for $C_{60}$ molecules with a Lennard-Jones potential with same equilibrium position and same well depth $(\cdots)$ . It is evident that the Girifalco potential has a much narrower well (i.e. it is the stickiest), while the silver potential is the softest.

basis (see the top row of Fig. 1). In particular, the TO₃₈ has eight square (1 0 0) facets and eight hexagonal (1 1 1) facets. On each (1 0 0) facet there is a single adsorption site, whereas on each (1 1 1) facet six adsorption sites are present, three on fcc and three on hcp stacking. Adsorption is clearly more favourable on (1 0 0) facets (see Table 1), since the adsorbed molecules have four nearest-neighbour molecules there, compared to the coordination three on the (1 1 1) facets. On the latter facets, fcc and hcp sites differ in energy by less than a hundredth of an eV.

An icosahedron (Ih) consists of 20 distorted tetrahedra sharing a common vertex. The Ih₅₅ presents 20 equivalent distorted (1 1 1) facets. On each facet there are four adsorption sites, three with anti-Mackay stacking (which corresponds to the hcp stacking) and a single central site on Mackay (i.e. fcc) stacking. Even if the fcc site is slightly better (by less than 0.03 eV, see Table 1), the possibility of accommodating three molecules on hcp sites favours the growth of an anti-Mackay overlayer on the Ih₅₅, as seen in experiments [7].

The Dh₇₅ is a truncated Marks decahedron [12] with 10 (1 1 1) facets (five for each cap), five square (1 0 0) facets and five reentrances exposing again (1 1 1) facets. Adsorption is more favourable either in the truncations or on the (1 0 0) facets, where the admolecule has coordination four. There is a slight preference for the truncations. However, since the (1 1 1) facets on the caps contain a much larger number of adsorption sites, the key processes concerning the growth on this cluster involve the adsorption on these facets [13]. Each (1 1 1) facet presents seven stable adsorption sites. Three of them are on decahedral (i.e. fcc) stacking, and four of them are of icosahedral (i.e. hcp) stacking. The difference in adsorption energies among these sites are within 0.03 eV, the central fcc site being the best one. However, the possibility of accommodating a larger number of molecules on icosahedral sites, favours the formation of islands on this stacking. This is the starting point of the kinetic solid–solid transformation of the Dh into a larger Ih, by a mechanism analogous to the one which takes place in the growth of silver clusters [13,14].

### 3.2. Energy barriers

On the TO₃₈, admolecules can move over a single (1 1 1) facet, jumping between fcc and hcp sites (intrafacet diffusion), or between adjacent facets of different symmetry (interfacet diffusion). Intrafacet diffusion is characterized a barrier of 0.19 eV (see Table 2). This is lower than the breaking of a single nearest-neighbour bond: the cohesive energy per molecule of solid C₆₀ is of 1.74 eV, and the breaking of a single bond would amount a sixth part of it, i.e. to 0.29 eV. This is a general phenomenon related to diffusion on (1 1 1)

Table 1
Adsorption energies on the TO₃₈, the Ih₅₅ and the Dh₇₅

<table>
<thead>
<tr>
<th>Cluster</th>
<th>Facet and site</th>
<th>Energy</th>
</tr>
</thead>
<tbody>
<tr>
<td>TO₃₈</td>
<td>(1 0 0)</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) fcc (sites B)</td>
<td>0.26</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) hcp (sites A)</td>
<td>0.26</td>
</tr>
<tr>
<td>Ih₅₅</td>
<td>(1 1 1) fcc (sites B)</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) hcp (sites A)</td>
<td>0.02</td>
</tr>
<tr>
<td>Dh₇₅</td>
<td>Truncation</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>(1 0 0)</td>
<td>0.02</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) fcc (sites D)</td>
<td>0.25</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) fcc (sites B)</td>
<td>0.27</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) hcp (sites E)</td>
<td>0.28</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) hcp (sites C)</td>
<td>0.26</td>
</tr>
<tr>
<td></td>
<td>(1 1 1) hcp (sites A)</td>
<td>0.27</td>
</tr>
</tbody>
</table>

All values are in eV. For each structure, the zero level of the adsorption energy is set at energy of the most favourable site.
The letters which label the sites are shown in Fig. 1.

Table 2
Energy barriers for the most important diffusion processes for admolecules on the clusters surfaces

<table>
<thead>
<tr>
<th>Cluster</th>
<th>Process</th>
<th>Barrier</th>
</tr>
</thead>
<tbody>
<tr>
<td>TO₃₈</td>
<td>j(1 1 1)</td>
<td>0.18</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/(1 1 1)</td>
<td>0.31</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/(1 0 0)</td>
<td>0.37</td>
</tr>
<tr>
<td>Ih₅₅</td>
<td>j(1 1 1)</td>
<td>0.12</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/(1 1 1)</td>
<td>0.27</td>
</tr>
<tr>
<td></td>
<td>ex(1 1 1)/(1 1 1)</td>
<td>0.54</td>
</tr>
<tr>
<td>Dh₇₅</td>
<td>j(1 1 1)</td>
<td>0.18</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/(1 1 1)</td>
<td>0.29</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/(1 0 0)</td>
<td>0.33</td>
</tr>
<tr>
<td></td>
<td>j(1 1 1)/R</td>
<td>0.30</td>
</tr>
<tr>
<td></td>
<td>ex(1 1 1)/(1 1 1)</td>
<td>1.40(1.50)</td>
</tr>
</tbody>
</table>

All values are in eV.

facets. Indeed, neighbouring fcc and hcp sites are so close that, at the saddle point, there are two full nearest-neighbours bonds plus a non-negligible contributions coming from two molecules whose distance is between the first and the second neighbour distance. This phenomenon is however much less evident on $C_{60}$ surfaces than on metal surfaces. There, the diffusion barrier on (111) surfaces is a small fraction of the energy of a single bond [13,15]. This happens because metal poten- tials are much softer, and the contribution of further neighbours than the first ones is more im- portant. Interfacet diffusion from (111) to (100) facets takes place by a jump and implies again the breaking of a single bond. Because of that, the barrier is again of 0.27 eV (see Fig. 3). The reverse process is much more difficult, since two bonds have to be broken, and it is characterized by a barrier above 0.5 eV. Exchange processes are in general difficult, due again to the stickiness of the interaction potential which does not allow any relaxations of the edge molecules (see the discus- sion about the diffusion on the $Ih_{55}$ in the follow ing).

On the $Ih_{55}$, intrafacet diffusion has a smaller energy barrier than on the (111) facets of the $TO_{38}$ and of $Dh_{75}$: the distortion of the (111) facets implies a more important contribution coming from molecules whose distance is between the first and second neighbour ones. Interfacet diffusion is even more interesting, and can be used as a further example to show an evident difference between the behaviours of sticky and soft potentials. A system with a soft interatomic potential is silver. There, interfacet diffusion on the $Ih_{55}$ takes place prefer- entially by exchange. Indeed, the exchange barrier is very low (0.15 eV), compared to the jump barrier (0.32 eV). The low exchange barrier is due to

![](./images/812409713714003968_6.jpg)

Fig. 3. Initial, saddle point and final positions for some typical diffusion processes: the jump from a (111) to a (100) facet on a $TO_{38}$ (top row), the exchange between two adjacent (111) facets on a $Ih_{55}$ (middle row) and the jump from a (111) facet to the Marks reentrance on a $Dh_{75}$ (bottom row).

the easy relaxation of the edge atoms to allow the incorporation of the adatom. On the contrary, on C₆₀ clusters, the exchange barrier is much higher than the jump barrier, the latter corresponding again to the breaking of a single bond. For a sticky potential, incorporation (and therefore exchange) is always difficult, as you can see from the saddle point in Fig. 3.

On the Dh₇₅, the situation is analogous. Intrafacet diffusion on (1 1 1) facets has again has barriers of about 0.2 eV; interfacet diffusion takes place by jump, the exchange processes being unfavourable. For example, interfacet diffusion among adjacent (1 1 1) facets has a barrier of 0.28 eV by jump (breaking of a single bond), while the exchange is characterized by an extremely high barrier, of the order of 1.5 eV. Here, the incorporation into the edge between the facets is much more difficult than on the Ih₅₅ in fact, the edge is longer (four molecules instead of three), and one end is at the reentrance. The molecule at this end is very difficult to displace, and so does not allow the opening of the space which is needed to the incorporation process. This situation was already evident in the case of silver [13], where, however, the barrier for exchange was of 0.56 eV. Interfacet diffusion from (1 1 1) facets to the reentrance (0.30 eV, see Fig. 3) and to (1 0 0) facets (0.33 eV) is again characterized by a barrier corresponding to the breaking of a single bond, whereas the reverse processes are more difficult because two bonds must be broken.

We do not consider any exchange processes with vertex atoms because they are already unfavourable on silver clusters [13]; in these mechanisms several bonds are broken at the saddle point, and thus they should be very unlikely on C₆₀ clusters.

## 4. Discussion and conclusions

In this paper, we have studied the adsorption and the energy barriers for diffusion for C₆₀ molecules adsorbed on the surface of three different clusters of C₆₀ molecules. On all the clusters, adsorption energies can be rationalized by a simple nearest-neighbour counting. In fact, due to the stickiness of the potential, further neighbours only give weak contributions. Differences between fcc and hcp sites on (1 1 1) facets are always small, of a few hundredths of eV. However, both on the Ih₅₅ and on the Dh₇₅, there is a higher number of hcp than of fcc sites, and this favours the formation of an anti-Mackay overlayer on the icosahedron, and of islands on *icosahedral* stacking on the decahedron. The formation of an anti-Mackay overlayer on the Ih₅₅ is in full agreement with the experimental results [7], where peaks in the mass spectrum are found at 55, 58, 61, 64, … molecules, corresponding to the formation of islands of three molecules on hcp sites on different facets. On the other hand, the rather high interfacet diffusion barriers on the Ih₅₅ hinder the formation of a single large island, which would be formed with a high admolecule mobility. On the (1 1 1) facets of the Dh₇₅, the growth of islands in *icosahedral* stacking can be the initial stage for the formation of a larger icosahedron in the growth process, being thus another mechanism to build up large metastable Ih.

Our calculations concerning the energy barriers for diffusion show that, due to the stickiness of the potential, the counting of nearest-neighbour bonds gives a reliable indication of the value of all the barriers, with the partial exception of intrafacet diffusion on (1 1 1) facets. Here the barrier for diffusion between fcc and hcp sites is about 2/3 of the strength of a single bond. However, we remark that on the surfaces of metals (which present softer potentials), the barrier is usually a small fraction of a single-bond energy.

Interfacet diffusion can take place via jump processes between neighbouring facets and it is quite independent of the local morphology: the jump from a (1 1 1) to a Marks reentrance presents the same energy barrier of the jump between two adjacent (1 1 1) on a Ih and the jump from a (1 1 1) to a (1 0 0) on a TO. Moreover, these diffusion barriers are of the same order of the energy necessary to break a single bond. Exchange processes have always high barriers, even on small clusters such as TO₃₈ or Ih₅₅. This hinders interfacet mobility, since the typical low-barrier exchange processes (such as the chain [13,16]) which connect different facets on metal cluster surfaces, are very difficult on these particles. This suggests that

complicated rearrangements of the clusters, such as those needed for structural transformations, are extremely difficult, in full agreement with the outcome of the growth simulations [8]. The only one structural transformation which can take place is the transformation of a decahedron into an icosahedron which is favoured by two facts: first, islands are better place on hcp sites; second, the reentrance is the most stable adsorption site on a Dh, and this adsorption site is a candidate to become a new fivefold symmetry point.

## References

[1] T.P. Martin, Phys. Rep. 273 (1996) 199.

[2] C.L. Cleveland, U. Landman, J. Chem. Phys. 94 (1991) 7376.

[3] J. Uppenbrink, D.J. Wales, J. Chem. Phys. 98 (1993) 5720.

[4] F. Baletto, R. Ferrando, A. Fortunelli, F. Montalenti, C. Mottet, J. Chem. Phys. 116 (2002) 3856.

[5] J.P.K. Doye, D.J. Wales, W. Branz, F. Calvo, Phys. Rev. B 64 (2002) 235409.

[6] T.P. Martin, U. Näher, H. Schaber, U. Zimmermann, Phys. Rev. Lett. 70 (1993) 3079.

[7] W. Branz, N. Malinowski, H. Schaber, T.P. Martin, Chem. Phys. Lett. 328 (2000) 245;
W. Branz, N. Malinowski, A. Enders, T.P. Martin, Phys. Rev. B 66 (2002) 094107.

[8] F. Baletto, J.P.K. Doye, R. Ferrando, Phys. Rev. Lett. 88 (2002) 075503.

[9] L.A. Girifalco, J. Phys. Chem. 96 (1992) 858.

[10] J.M. Pacheco, J.P. Prates-Ramalho, Phys. Rev. Lett. 79 (1997) 3873.

[11] H. Jonsson, G. Mills, K.W. Jacobsen, Nudged elastic band for finding minimum energy paths of transitions, in: B.J. Berne, G. Ciccotti, D.F. Coker (Eds.), Classical and Quantum Dynamics in Condensed Phase Simulations, World Scientific, 1998.

[12] L.D. Marks, Rep. Prog. Phys. 57 (1994) 603.

[13] F. Baletto, R. Ferrando, Surf. Sci. 490 (2001) 361.

[14] F. Baletto, C. Mottet, R. Ferrando, Phys. Rev. B 63 (2001) 155408.

[15] R. Ferrando, G. Trèglia, Surf. Sci. 331–333 (1995) 920.

[16] F. Baletto, C. Mottet, R. Ferrando, Surf. Sci. 446 (2000) 31.