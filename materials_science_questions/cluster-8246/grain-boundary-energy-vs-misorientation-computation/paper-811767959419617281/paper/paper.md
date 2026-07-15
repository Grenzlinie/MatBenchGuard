# Modeling of Grain-Boundary Segregation Behavior in Aluminum Oxide

Junghyun Cho, $^{*}$ Jeffrey M. Rickman, $^{*}$ Helen M. Chan, $^{*}$ and Martin P. Harmer $^{*, * *}$

Materials Research Center and Department of Materials Science and Engineering,
Whitaker Laboratory, Lehigh University, Bethlehem, Pennsylvania 18015

It is believed that the segregation of oversized dopant ions to grain boundaries in $Al_{2}O_{3}$ hinders grain-boundary diffusion, thereby reducing the tensile creep rate in this system by $\sim 2-3$ orders of magnitude. In order to explain this improvement in creep behavior, it is helpful to characterize both the effective cation and interstitial volumes at grain boundaries, because the relative openness of some boundary structures suggests a great accommodation of oversized ions. In this study, the boundary volume is determined by a spatially local Voronoi construction, which highlights cation $(Al^{3+})$ substitutional sites as well as large interstitial voids. In particular, we examine the spatial distribution of free volume near grain boundaries and, in addition, the dependence of the driving force for segregation on misfit strain in doped $Al_{2}O_{3}$. We interpret our results in light of recent evidence that selective codoping can provide a more efficient means of filling available space near boundaries, thereby further enhancing creep resistance.

## I. Introduction
Given their relative mechanical stability and refractory nature, ceramic materials have been used extensively for high-temperature structural applications. However, because of the limited utility of monolithic ceramics in some extreme conditions, ceramic-matrix composites (CMCs) have received considerable attention in recent years. For example, under conditions in which high oxidation resistance at high temperatures is required, ceramic oxides, such as $Al_{2}O_{3}$, are possible candidates for both fiber and matrix materials. In this regime, the creep properties of $Al_{2}O_{3}$ limit its applicability. Given this constraint, it is of interest to identify a subset of $Al_{2}O_{3}$-based oxides having superior creep resistance. We note that significant progress toward this goal occurred when it was discovered that the tensile creep rate of $Al_{2}O_{3}$ decreased by $\sim 2-3$ orders of magnitude by the addition of $Y_{2}O_{3}$ or $La_{2}O_{3}^{1,2}$

While the exact mechanism for enhanced creep resistance in these promising doped oxides is not yet known, emerging evidence suggests that grain boundaries play a dominant role in this behavior. One such observation is that oversized cation dopants strongly segregate to grain boundaries. This segregation tendency was highlighted in the work of Li and Kingery $^{3}$ and, more recently, in secondary ion mass spectroscopy (SIMS) mapping $^{4}$ and dedicated scanning transmission electron microscopy (STEM) studies. $^{5}$ Unfortunately, the complexity of grain-boundary geometries, particularly in the presence of dopants, makes it difficult to connect boundary structure with boundary transport and, ultimately, diffusional creep. Consequently, the interaction between cation $(Al^{3+})$ grain-boundary diffusion, which is believed to control creep in this study, $^{1,6,7}$ and dopant segregants has not been clearly identified. One purpose of this work, therefore, is to characterize systematically and model grain-boundary structure in doped $Al_{2}O_{3}$ in order to connect boundary structure with the propensity for segregation. The long-term goal is to describe grain-boundary transport kinetics in the presence of dopants and, thereby, further elucidate the mechanisms for observed creep behavior.

Specifically, we focus here on the local free volume associated with grain boundaries in order to identify those regions that might accommodate (oversized) segregants. Thus, we use a local Voronoi construction consisting of space-filling polyhedra in the vicinity of grain boundaries under consideration to quantify this volume. For convenience, the grain boundaries selected here are special, coincidence-site lattice (CSL) boundaries with a common [0001] rotation axis, even though we expect to use the results to obtain generic information applicable to a broader spectrum of boundaries. The procedure for generating and relaxing these boundaries is summarized below.

The systematic analysis undertaken here is also useful in understanding certain experimental synergies associated with selective codoping. For example, it has been found that codoping $Al_{2}O_{3}$ with neodymium and zirconium enhances its creep resistance beyond that observed in $Al_{2}O_{3}$ systems singly doped with either ion. $^{8}$ This observation has led to the conjecture that, in some circumstances, a combination of large and small ions can fill the grain-boundary region more efficiently than can either ion individually, thereby greatly inhibiting diffusion and creep. In principle, then, the characterization of grain-boundary volume can suggest optimal doping strategies in $Al_{2}O_{3}$ that lead to improved creep resistance.

## II. Simulation Methodology
### (1) Energetics
Various combinations of interionic potentials are used to describe the energetics of both pure and doped oxides. In particular, the lattice energy, $U$, of an oxide containing $N$ ions is calculated with a pair potential having two contributions: a short-range combination of Born-Mayer and attractive van der Waals interactions and a long-range Coulombic interaction that together are given by

$$
U=\frac{1}{2} \sum_{i=1}^{N} \sum_{\substack{j=1 \\ j \neq i}}^{N}\left[V\left(r_{i j}\right)+\frac{z_{i} z_{j}}{r_{i j}}\right] \tag{1}
$$

where $z$ is the ionic charge, $r_{ij}$ the separation between ions $i$ and $j$, and $V(r_{ij})$ the short-range interaction

$$
V\left(r_{i j}\right)=A_{i j} \exp \left(-\frac{r_{i j}}{\rho}\right)-\frac{C}{r_{i j}^{6}} \tag{2}
$$

The empirical parameters $A$, $\rho$, and $C$ are determined from fits to perfect crystal data, such as the lattice parameter, elastic constants, and cohesive energy.

---
R. Raj—contributing editor

Manuscript No. 189878. Received September 11, 1998; approved July 12, 1999.
Supported by the U.S. Air Force Office of Scientific Research under Contract No. F49620-98-1-0117. (Monitored by Dr. A. Pechenik.)
Presented at the 100th Annual Meeting of the American Ceramic Society, Cincinnati, OH, May 4, 1998 (Computational Modeling of Materials and Processing Symposium, Paper No. SV-014-98).
*Member, American Ceramic Society.
**Fellow, American Ceramic Society.

<table>
<caption>Table I. Empirically Fitted Potential Parameters and Shell Constants for $\alpha$-Al₂O₃ and M₂O₃ Systems†</caption>
<thead>
<tr>
<th>Parameter</th>
<th>α-Al₂O₃</th>
<th>Fe₂O₃</th>
<th>Yb₂O₃</th>
<th>Eu₂O₃</th>
<th>La₂O₃</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A(+/-)$ (eV)</td>
<td>1460.3</td>
<td>3219.335</td>
<td>991.029</td>
<td>847.868</td>
<td>5436.827</td>
</tr>
<tr>
<td>ρ(+/−) (Å)</td>
<td>0.29912</td>
<td>0.2641</td>
<td>0.3515</td>
<td>0.3791</td>
<td>0.2939</td>
</tr>
<tr>
<td>$C(+/-)$ (eV · Å⁶)</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>$A(-/-)$ (eV)</td>
<td>22764.3</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ρ(−/−) (Å)</td>
<td>0.1490</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$C(-/-)$ (eV · Å⁶)</td>
<td>27.879</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$Y_{+}$ (|ẽ|)</td>
<td>1.3830</td>
<td>1.971</td>
<td>−0.278</td>
<td>−0.991</td>
<td>5.149</td>
</tr>
<tr>
<td>$k_{+}$ (eV · Å⁻²)</td>
<td>92.488</td>
<td>179.58</td>
<td>308.91</td>
<td>304.92</td>
<td>173.90</td>
</tr>
<tr>
<td>$Y_{-}$ (|ẽ|)</td>
<td>−2.8106</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$k_{-}$ (eV · Å⁻²)</td>
<td>103.07</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">†$Y$ = shell charge, $k$ = spring constant. In all cases, cation–cation potential is taken to be purely Coulombic (taken from Catlow et al.⁹ and Bush et al.²⁹).</td>
</tr>
</tfoot>
</table>

In this study, the potential parameters by Catlow et al.⁹ are used, as summarized in Table I, wherein only oxygen–oxygen and (repulsive) oxygen–aluminum interactions are considered, and where cutoff radii of 8.0 Å are imposed for both interactions. We note, however, that the long-range, Coulombic potential requires special treatment. Because this interaction falls off rather slowly in space, one can not establish arbitrary cutoff radii, because the summations indicated in Eq. (1) are only conditionally convergent.¹⁰ This problem is remedied, as usual, by using a three-dimensional Ewald summation¹¹,¹² to obtain the relevant contribution to the cohesive energy and associated Madelung constant. We also note the additional complication that a space-charge layer can form near extended defects.¹³,¹⁴ This effect is not considered explicitly below, because the focus of this study is isovalent cation impurities.

Because defect interactions in ionic crystals depend strongly on the electrical polarization of the lattice, the description above is incomplete, because it does not incorporate the dielectric response of the material. For this purpose, the shell model, used by Dick and Overhauser¹⁵ in their treatment of the dielectric properties of alkali halides, is implemented here. In this idealized model, an ion, $i$, is composed of both core and shell pieces that are connected by an elastic spring contributing an additional quadratic interaction potential

$$
V_{sc}^{i} = \frac{1}{2} k_{i} (r_{si} - r_{ci})^{2} \tag{3}
$$

where $k_{i}$ is a spring constant associated with ion, $i$, and $r_{si}$ and $r_{ci}$ the ionic shell and core positions, respectively. The corresponding shell charges and spring constant are again obtained from the dielectric properties of bulk crystals,⁹ as summarized in Table I. While the core and shell positions are taken to coincide initially, the final equilibrium configuration in a defect region often consists of many core–shell displacements, given its lower symmetry relative to the bulk environment, if the associated polarization energy is compensated by decreases in energy elsewhere.

Having evaluated the energy for a given perfect or defect configuration, the equilibrium, ground-state energy is found using the conjugate-gradient technique, wherein forces are calculated at each step in the relaxation.¹⁶ In many cases, we compare these energies with those obtained by zero-temperature Monte Carlo (MC) simulation. These experiments are performed by using a rectangular or rhombic supercell of dimension $1 \times 1 \times n$, where $n$ is variable, with periodic boundary conditions imposed in three directions (see Table II). As a result, in the case of extended defects, such as surfaces and grain boundaries, a spatially periodic superlattice is constructed, and $n$ is adjusted until extended defect–defect interactions have been substantially reduced or eliminated, sometimes using extrapolation. Grain-boundary superlattices have been investigated by others using a similar methodology.¹⁷ The height, $z$, of the simulation cell is also variable, permitting us to adjust the stress component, $\sigma_{zz}$. Finally, we are also able to add an excess volume fraction, $\delta$, near an interface by incorporating a gap and then minimizing the total energy with respect to the distance between two crystals. Given the time-consuming nature of the atomic relaxation procedure, gap optimization is performed, in practice, in the unrelaxed state.

### (2) Grain-Boundary Geometry

While grain boundaries can be characterized by various geometric parameters,¹⁸ it is convenient here to classify boundary geometry in terms of a CSL model. The fundamental quantity in this description is the multiplicity, $\Sigma$, defined as the volume ratio of the CSL unit cell to that of the original unit cell. For our purposes, Grimmer et al.¹⁹ have tabulated all coincidence orientations with multiplicities $\Sigma \leq 36$ for rhombohedral lattices with axial ratios, $c/a$, for corundum-type structures (i.e., $2.696 < c/a < 2.765$). Among these interfaces, we have selected six basal-plane grain boundaries, namely $\Sigma 3$, 7, 13, 19, 21, and 31, which are constructed here via rotation around the [0001] axis. From related geometric considerations, one can show that common rotations (in which the same relative orientation of two halves of a bicrystal can be described also by a rotation around the three-fold axis by an angle $\theta$ so that $3^{1/2} \tan \theta/2$ is rational)¹⁹ result in the coincidence of a fraction $1/\Sigma$ of translation vectors in rhombohedral lattices. We note here that electron backscattered Kikuchi diffraction results for experimentally hot-pressed polycrystalline Al₂O₃ samples reveal the presence of both $\Sigma 3$ and $\Sigma 13$ boundaries, albeit in rather limited proportions.²⁰

For the purpose of illustration, Fig. 1 shows the ionic positions associated with a $\Sigma 13$ boundary, while also highlighting the associated CSL unit cell, and Table II summarizes the salient features of the CSL boundaries used in this study. Finally, we note that, during relaxation to equilibrium, the translations parallel to the boundary plane (i.e., $x$- and $y$-directions) are fixed,¹⁷ and we do not consider explicitly the role of point defects in the possible stabilization of some grain boundaries.²¹

### (3) Voronoi Polyhedra

As discussed above, we wish to examine quantitatively the volume associated with grain-boundary regions in the oxides under consideration.²²,²³ Our approach has been to partition space in a slab of prescribed thickness near a (relaxed) boundary using a

<table>
<caption>Table II. Selected CSLs around the [0001] Axis and the Associated $1 \times 1 \times n$ Simulation Cells Used in This Study</caption>
<thead>
<tr>
<th>$\Sigma$</th>
<th>$\theta$ (degrees)</th>
<th>$n$</th>
<th>Number of ions in the simulation cell</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>60.00</td>
<td>4</td>
<td>1920</td>
</tr>
<tr>
<td>7</td>
<td>38.21</td>
<td>4</td>
<td>2520</td>
</tr>
<tr>
<td>13</td>
<td>27.80</td>
<td>4</td>
<td>3120</td>
</tr>
<tr>
<td>19</td>
<td>46.83</td>
<td>2</td>
<td>2280</td>
</tr>
<tr>
<td>21</td>
<td>21.79</td>
<td>4</td>
<td>3360</td>
</tr>
<tr>
<td>31</td>
<td>17.90</td>
<td>4</td>
<td>7440</td>
</tr>
</tbody>
</table>

![](./images/811767959419617281_1.jpg)

Fig. 1. Rotation of two crystals by 27.80° to build a Σ13 boundary. This is viewed along the [0001] axis, and the coincidence sites and the corresponding unit cells are indicated. ((○) or (●) = oxygen; (◎) = coincidence site.)

Voronoi construction.²⁴·²⁵ In particular, two measures of interfacial volume are determined: the spatial distribution of cation volume and the distribution of void volume, by associating each element of space with either a cation or a void, respectively. In the cation case, a Voronoi polyhedron is constructed from the envelope of planes that bisect each line, which connects the cation to a neighboring anion. Thus, in a bulk environment, each cation is octahedrally coordinated and associated with a cubic Voronoi cell (Fig. 2). Interstices are characterized by a similar procedure. For convenience, in both cases, the average "radius" (the average distance from a cation site to six neighboring faces) of the Voronoi cell is used as a measure of cell size given that the determination of cell volume is rather tedious for general polyhedra.

While this approach is quite useful in that it provides data on the distribution and frequency of possible segregation sites, it is worth noting two limitations. First, this subdivision of space is complicated by ambiguities in identifying void locations in a defect region, by the polarizability of ions in low-symmetry positions and by relatively large ionic relaxations in some cases. Second, it is essentially a geometric description of an interfacial region that does not incorporate explicitly local charge considerations. Nevertheless, as is seen below, the Voronoi construction is quite informative.

### (4) Isovalent Doping of α-Al₂O₃

A more complete picture of the propensity for grain-boundary segregation incorporates the elastic deformation that attends the introduction of impurities in the boundary region. Such deformations are particularly relevant here, because experimental evidence indicates that oversized isovalent ions, such as yttrium and lanthanum, strongly segregate to grain boundaries, suggesting that the main driving force for segregation is size mismatch (despite reports that yttrium can behave as a donor).²⁶·²⁷ The strain energy associated with this mismatch has been given in the continuum limit by Eshelby and is proportional to the square of the misfit strain, as given by the square of the difference, $\Delta r$, between dopant and host ion radii.²⁸ In fact, for a related elastically isotropic system, one can write

$$
U_{s}=\frac{6 \pi r^{3}(\Delta r / r)^{2} B}{(1+3 B / 4 G)} \tag{4}
$$

where $B$ is the bulk modulus of the solute ion and $G$ the shear modulus of the matrix.

In this study, we consider the interchange of a generic trivalent cation, M, with an aluminum cation. This substitution, which can be performed conveniently in a simulation, might arise in practice, for example, from the reaction

$$
\frac{1}{2} \mathrm{M}_{2} \mathrm{O}_{3}+\mathrm{Al}_{\mathrm{Al}}^{\times}=\mathrm{M}_{\mathrm{Al}}^{\times}+\frac{1}{2} \mathrm{Al}_{2} \mathrm{O}_{3} \tag{5}
$$

The short-range interaction between dopant and oxygen ions is incorporated in the simulation by using empirical potential parameters obtained by Bush *et al.* for a series of metal oxides, as

![](./images/811767959419617281_2.jpg)

Fig. 2. (a) Octahedral environment of oxygen anions for an aluminum cation in bulk. (b) Corresponding Voronoi cell is a cube.

summarized in Table I. $^{29}$ Various dopants, ranging in size from iron (0.64 Å) to lanthanum (1.06 Å), are used here. Now, the Langmuir-McLean theory predicts that that

$$
C_{\mathrm{gb}} \approx C_{1} \exp \left(-\frac{\Delta H}{k T}\right) \tag{6}
$$

where $C_{\mathrm{gb}}$ is the occupation fraction (impurity/host ions) at the grain boundary, $C_{1}$ the bulk fraction, and $\Delta H$ the segregation enthalpy of interaction between the solute ion and the boundary. $^{30}$ We note that, in writing Eq. (6), we have used a dilute solution approximation and also neglected entropic contributions to the free energy. With this definition, then, a negative $\Delta H$ implies segregation. Thus, if the strain energy is the main driving force for segregation, $\Delta H$ is essentially proportional to

$$
-\Delta H=k T \ln \left(\frac{C_{\mathrm{gb}}}{C_{1}}\right) \propto\left(\frac{\Delta r}{r}\right)^{2} \tag{7}
$$

In the following section, the validity of this relation is assessed via an identification of favorable boundary sites that most relieve the strain energy. For this purpose, segregation enthalpy is calculated and related to boundary geometry.

### III. Results and Discussion

We summarize here the energetic and geometric information obtained from simulation. As indicated above, relaxed, equilibrium structures are obtained primarily via conjugate-gradient energy minimization, and these results are compared, in some cases, with those calculated via the zero-temperature MC method in order to validate the methodology. The data obtained from these two complementary relaxation schemes are presented in Table III for a bulk system, a basal free surface, and an (oxygen-terminated) basal twin boundary. It is worth pointing out that our results for the energies of the perfect crystal, the basal free surface, and point-defect formation energies (such as the Schottky quintet, Frenkel anion, and Frenkel cation) agree very well with previous simulation studies that have used this potential. $^{9,31}$

For the CSL boundaries considered in this study, grain-boundary excess energies (per unit area) are calculated and shown in Fig. 3 as a function of misorientation angle. As is evident from

<table>
<caption>Table III. Energetic Comparison between Two Energy Minimization Procedures</caption>
<thead>
  <tr>
    <th></th>
    <th>Monte Carlo method</th>
    <th>Conjugate-gradient method</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Perfect lattice (eV/formula unit)</td>
    <td>−160.62</td>
    <td>−160.62</td>
  </tr>
  <tr>
    <td>(0001) Free surface (960 ions) (J/m²)</td>
    <td>2.93</td>
    <td>2.92</td>
  </tr>
  <tr>
    <td>(0001) Twin boundary (960 ions) (J/m²)†</td>
    <td>3.89</td>
    <td>3.86</td>
  </tr>
</tbody>
</table>

†Based on oxygen-terminated twin boundary; twin boundary energy was 3.10 J/m² when it was extrapolated to an infinite system to avoid interactions between the two twins.

Fig. 3, the boundary energies lie in the range of $\sim$2.8–3.2 J/m², with the $\Sigma 3$ basal twin boundary having the lowest energy in this series of CSLs. It should be noted that the energy of this $\Sigma 3$

![](./images/811767959419617281_3.jpg)

Fig. 3. Grain-boundary energy versus misorientation angle for selected CSLs around the [0001] axis. Twin boundary forms at a misorientation of 60°. ((□) indicates grain-boundary energy with an incorporated gap between two half crystals.)

![](./images/811767959419617281_4.jpg)

Fig. 4. Relaxed structures from (a) Σ3 (twin) and (b) Σ13 boundary. Location of boundaries is indicated by a bold line. Number shows the oxygen stacking sequence, and arrow indicates the [0001] direction. ((⊗) = oxygen; (●) = aluminum.)

![](./images/811767959419617281_5.jpg)

Fig. 5. Same structure as in Fig. 4 focusing on three boundary planes (O-Al-O), as viewed along the [0001] axis: (a) Σ3 boundary voids characterized by the trigonal prisms of A (large) and B (small); (b) Σ13 boundary.

![](./images/811767959419617281_6.jpg)
![](./images/811767959419617281_7.jpg)

Fig. 6. Voronoi cell characterization of a boundary plane, as compared to bulk environment: (a) Σ3, substitutional; (b) Σ3, interstitial; (c) Σ13, substitutional; (d) Σ13, interstitial. (T = tetrahedral site, O = octahedral site, d = Voronoi cell radius, $d_b$ = Voronoi cell radius for the bulk sites.)

boundary is lower than that of the corresponding oxygen-terminated basal twin (see Table III), and that, more generally, all of these boundary energies are each less than twice the calculated (0001) surface energy, indicating stability against spontaneous grain-boundary separation.

We note here, as mentioned above, that in-plane (i.e., $x$ and $y$) boundary translations have not been considered in this study. While such translations can facilitate grain-boundary relaxation in some cases, they are not easily incorporated in the superlattice model, given the two interfaces created per cell. Further, it is often difficult to determine, $a$ $priori$, the optimal displacement vectors associated with relaxation. An alternative to this description is the Mott–Littleton approach, wherein the crystal is divided into region I, surrounding an interface, and an outer region II, modeled as a dielectric continuum.⁹ The drawback of this approach is, however, that the usual Ewald summation technique must be modified to account for the loss of periodicity in one direction. Thus, we have adopted the view that the superlattice model is adequate for the segregation studies reviewed here, because, although grain-boundary translation can affect the detailed locations of potential segregation sites, the overall distribution of excess grain-boundary volume is likely to be less sensitive to such translations. The incorporation of grain-boundary sliding into segregation studies is a subject for future work.

Figure 4 shows the corresponding relaxed grain-boundary structures, based for simplicity only on ionic core positions, for both the Σ3 and Σ13 boundaries. In the former case, the grain-boundary region remains relatively coordinated, with the requisite mirror symmetry across the boundary. By contrast, the latter (Σ13) boundary region is more disordered, exhibiting a rumpled structure in the oxygen layers ($\Delta z \approx 1$ Å at plane 1) near the boundary plane. Given this difference in the degree of disorder, these two boundaries serve as prototypes in the discussion below.

Note, however, from Fig. 4(b) that the terminating boundary plane is not easily located, unlike that for the Σ3 boundary. Indeed, one might imagine alternative starting configurations, such as, for example, the one obtained by placing the boundary plane between two aluminum layers (i.e., splitting two aluminum layers between oxygen layers). In fact, the relaxation of this configuration yields a different boundary structure with a correspondingly (slightly) higher energy ($\sim 1\%$). This result implies that there can be various metastable local energy minima corresponding to different initial structures. Such minima can, in fact, be artifacts of the simplified potential used here that neglect short-range, cation–cation interactions (see Table I). In any case, we focus on the structure presented in Fig. 4(b), while hoping to identify a global minimum with simulated annealing in future work.

![](./images/811767959419617281_8.jpg)

Fig. 7. Excess parameter, $\delta d$, a measure of excess volume of large boundary substitutional sites as a function of $i$th aluminum layer (which increases upon moving away from the boundary). $\Sigma 3$ shows narrow distribution and so approaches the bulk value more quickly.

A somewhat more detailed description of the boundary structure is possible, in some cases, upon viewing several planes along the [0001] axis (Fig. 5). For example, one can view the $\Sigma 3$ boundary interstices in terms of two types of trigonal prisms (located at sites A and B), which have a relative radii of $d/d_{\mathrm{b}}=1.03$ and 0.986 , respectively, where $d$ is the average radius of the trigonal prisms and $d_{\mathrm{b}}$ the radius of bulk octahedral interstitial sites (Fig. 5(a)). However, the disorder associated with the $\Sigma 13$ boundary precludes this simple analysis and leads to several types of interstices of varying size (Fig. 5(b)).

Based solely on geometrical arguments, it is expected that areas of larger interfacial volume can serve as potential sites for dopant segregation. Thus, in order to identify the most likely candidate sites, we compiled a frequency histogram of Voronoi volumes for the $\Sigma 3$ and $\Sigma 13$ boundaries. As is evident in the histogram for substitutional sites (Fig. 6(a)), the $\Sigma 3$ boundary has broken the degenerate, bulk unimodal size distribution into an essentially bimodal distribution of sites with widely disparate sizes. The situation for interstitial sites (Fig. 6(b)) is rather similar, yet complicated by the fact that there are now both octahedral and more numerous tetrahedral bulk sites. It is found that one-fourth of the boundary interstices are larger than these bulk sites. In the case of the $\Sigma 13$ boundary, several potential substitutional sites, many larger than the corresponding bulk sites, are available for segregation in addition to some interstitial sites (see Figs. 6(c) and (d)).

Finally, the Voronoi analysis is extended to layers near each boundary. In Fig. 7, the excess volume available is plotted as a function of $i$th aluminum layer from the boundary (0 is at the boundary) near the $\Sigma 3$ and $\Sigma 13$ grain boundaries. One measure of this excess volume is the excess parameter, $\delta d$, characterized by

$$
\delta d=\frac{1}{N} \sum_{i=1}^{N}\left(d_{i}-d_{\mathrm{b}}\right) \times \Theta\left(d_{i}-d_{\mathrm{b}}\right)
\tag{8}
$$

where $N$ is total number of sites, $d_{i}\left(d_{\mathrm{b}}\right)$ the average radius of site $i$ (a bulk site), and $\Theta\left(d_{i}-d_{\mathrm{b}}\right)$ a step function. From Fig. 7, it is concluded that, because of the more-localized excess volume associated with the $\Sigma 3$ boundary, segregation is likely to occur near this boundary (within $\sim 2.0 \AA$ ), whereas, in the case of the $\Sigma 13$ boundary, a segregant concentration profile likely extends over several layers. Electron microscopy studies have reported essentially no segregation of yttrium to the basal twin boundary, whereas they have detected segregation to other boundaries. $^{32}$

The relevance of the relative excess radius, $\left(d-d_{\mathrm{b}}\right) / d_{\mathrm{b}}$, in this segregation study can be seen by examining Fig. 8, which shows the simulation result of unrelaxed substitutional energy (relative to bulk) of europium in the $\Sigma 13$ boundary as a function of $\left(d-d_{\mathrm{b}}\right) / d_{\mathrm{b}}$ for sites of various sizes. Europium is an intermediate-sized lanthanide ion having a radius of $0.95 \AA$. The substitutional energy shows a roughly linear relationship with the relative excess radius, indicating the larger volume can more easily accommodate oversized ions. Further, those sites with zero excess radius have nearly zero corresponding excess energies, implying that such sites are essentially bulklike and that the size of the local Voronoi cell is the best indicator of the propensity for segregation. A more complete description must, of course, incorporate ionic relaxation.

![](./images/811767959419617281_9.jpg)

Fig. 8. Unrelaxed substitutional energy of europium in $\Sigma 13$ boundary as a function of boundary space, showing linear relationship. $(E_{\Sigma 13}=$ unrelaxed substitutional energy at $\Sigma 13, E_{\mathrm{b}}=$ unrelaxed substitutional energy in the bulk.)

Having characterized the volume in boundary regions, we next determine zero-temperature (substitutional) segregation enthalpies, $\Delta H$, for relaxed boundary and bulk sites. Such information can, in principle, be used in an equilibrium statistical mechanical calculation of a segregation profile, although our aim here is only to identify likely segregation sites based on volume and complementary energetic considerations. For this purpose, our results are perhaps best illustrated in the case of the $\Sigma 13$ boundary.

The segregation enthalpy, $\Delta H$, is displayed in Fig. 9 for four dopants (iron, ytterbium, europium, and lanthanum) of varying size as a function of $(\Delta r)^{2}$ for three types of boundary substitutional sites. These sites, labeled 1,2, and 3 and ordered based on size, have relative radii, $d/d_{\mathrm{b}}$, of 1.067,1.018, and 0.9813, respectively. For type 1 sites, the observed linear relationship suggests that the main driving force for segregation is indeed size mismatch. As the site volume decreases, segregation enthalpy also expectedly increases and is positive for type 3 sites, which are smaller than their bulk counterparts. Similar trends exist for substitutional sites near the boundary. In summary, these results not only indicate which subset of sites are preferred for segregation but also suggest that (1) site exhaustion can lead to a saturation of segregation behavior and that (2) selective codoping schemes can be used to enhance segregation, particularly in the case of the $\Sigma 13$ boundary with its multiplicity of potential sites. The possibility of segregation saturation is consistent with the observation of similar segregation profiles in systems with relatively large ionic impurities, such as yttrium- and lanthanum-doped $\mathrm{Al}_{2} \mathrm{O}_{3},{ }^{5}$ while the advantages of codoping are discussed above in relation to the neodymium-zirconium codoped $\mathrm{Al}_{2} \mathrm{O}_{3}$ system. $^{8}$

It is of interest to explore the implications of these results for transport processes in ceramic oxides. In particular, it has been shown in preliminary work that the presence of segregating ions near grain boundaries can alter (possibly fast) diffusive paths in interfacial regions. $^{20,33}$ We are, in fact, now in the process of correlating these diffusion studies with investigations of the kinetics of creep. Therefore, to the extent that grain-boundary diffusion controls the long-time mechanical response of the material, as exemplified by its creep rate, the propensity for segregation

![](./images/811767959419617281_10.jpg)
![](./images/811767959419617281_11.jpg)

Fig. 9. (a) Segregation enthalpy, $\Delta H$, versus square of the difference in radii for four different dopant ions at three different sites in the same boundary plane of $\Sigma 13$. (b) Three different sites representing largest $(d/d_{b}=1.067)$, intermediate (1.018), and smallest (0.9813), as shown in this histogram.

likely governs this response. From this perspective, one can envision scenarios in which a relatively small impurity concentra- tion at the boundary can substantially improve creep resistance by blocking or modifying a few, critical diffusive pathways. Such synergies in yttrium- and lanthanum-doped $Al_{2}O_{3}$ are described in the Introduction.

Finally, the results of this study of $Al_{2}O_{3}$ grain boundaries correlate roughly with some experimental findings, namely that the largest substitutional sites represent $\sim 4 \%$ of the $\Sigma 13$ boundary sites, translating to the $5 \%-10 \%$ of dopant coverage found in both SIMS and STEM work. $^{4,5}$ It should be noted, however, that our simulations are clearly idealized in certain respects. For example, the present work was performed at $0 ~K$, where vacancy formation is not a factor; whereas, at higher temperatures, the presence of vacancies can alter detailed boundary structure $^{34}$ and presumably, therefore, detailed segregation profiles. Also, while general grain boundaries are clearly present in the experimental systems studied to date, we have confined our investigations to a subset of special boundaries given the constraints of spatial periodicity and system size. Thus, we have focused here only on two prototypical special boundaries on the basal plane. A more extensive study of other special boundaries, with a possible extrapolation to general bound- aries, is contemplated for future work.

## IV. Summary
In this study, the volumes associated with several special grain boundaries in $Al_{2}O_{3}$ were characterized by a spatially local Voronoi construction in order to identify potential sites for impurity segregation. In particular, both the $\Sigma 3$ (twin) and the $\Sigma 13$ basal boundaries were examined in some detail in order to determine the frequency and spatial distribution of these sites. In conjunction with this geometrical study, a complementary ener- getic analysis yielded site segregation enthalpies and shed some light on observed experimental behavior. The dependence of enthalpy on ionic radius was examined by simulating ionic size mismatch using a variety of isovalent dopants, and it was found that the strain energy associated with this mismatch contributed significantly to the driving force for segregation.

As indicated above, a better understanding of boundary segre- gation behavior in polycrystalline $Al_{2}O_{3}$ systems is key to describ ing the enhancement of time-dependent mechanical properties given that segregation is likely to alter boundary transport. Thus, future efforts are directed at linking segregation to transport properties at grain boundaries and at investigating boundary segregation in codoped $Al_{2}O_{3}$ by using computer simulation. In this way, one may be able to identify which dopants and which boundaries have the greatest impact on observed creep behavior.

## Acknowledgments:
The authors would like to thank Professor F. Lange and Dr. C. Wang for helpful discussions.

## References
$^{1}$ J. Cho, M. P. Harmer, H. M. Chan, J. M. Rickman, and A. M. Thompson, "Effect of Yttrium and Lanthanum on the Tensile Creep Behavior of Aluminum Oxide," J. Am. Ceram. Soc., 80 [4] 1013-17 (1997).
$^{2}$ J. D. French, J. Zhao, M. P. Harmer, H. M. Chan, and G. A. Miller, "Creep of Duplex Microstructures," J. Am. Ceram. Soc., 77 [11] 2857-65 (1994).
$^{3}$ C.-W. Li and W. D. Kingery, "Solute Segregation at Grain Boundaries in Polycrystalline $Al_{2}O_{3}$ "; pp. 368-78 in Advances in Ceramics, Vol. 10, Structure and Properties of $MgO$ and $Al_{2}O_{3}$ Ceramics. Edited by W. D. Kingery. American Ceramic Society, Columbus, OH, 1984.
$^{4}$ A. M. Thompson, K. K. Soni, H. M. Chan, M. P. Harmer, D. B. Williams, J. M. Chabala, and R. Levi-Setti, "Rare Earth Dopant Distributions in Creep-Resistant Al2O3," J. Am. Ceram. Soc., 80 [2] 373-76 (1997).
$^{5}$ J. Bruley, J. Cho, H. M. Chan, M. P. Harmer, and J. M. Rickman, "Scanning Transmission Electron Microscopy Analysis of Grain Boundaries of Creep-ResistantYttrium- and Lanthanum-Doped Alumina Microstructures," J. Am. Ceram. Soc., 82[10] 2865-70 (1999).
$^{6}$ R. M. Cannon and R. L. Coble, "Review of Diffusional Creep of $Al_{2}O_{3}$ "; pp61-100 in Deformation of Ceramic Materials, Proceedings of a Symposium on Plastic Deformation of Ceramic Materials (Pennsylvania State University, July 1974). Edited by R. C. Bradt and R. E. Tressler, Plenum, New York, 1975.
7A. H. Chokshi and G. L. Langdon, "Diffusion Creep in Ceramics: A Comparison with Metals"; pp. 1205-26 in Diffusion in Metals and Alloys DIMETA 88, Defect and Diffusion Forum, Vols. 66-69 (Balatonfüred, Hungary, September 1988). Edited by F. J. Kedves and D. L. Bake. Sci-Tech Publications, Brookfield, VT, 1990.
$^{8}$ Y.-Z. Li, C. Wang, H. M. Chan, J. M. Rickman, and M. P. Harmer, "Codoping of Alumina to Enhance Creep Resistance," J. Am. Ceram. Soc., 82 [6] 1497-504 (1999).
°C. R. W. Catlow, R. James, W. C. Mackrodt, and R. F. Stewart, "DefectEnergetics in $\alpha-Al_{2} O_{3}$ and Rutile $TiO_{2}$ ," Phys. Rev. B: Condens. Matter, 25 [2]1006-26 (1982)
10N. W. Ashcroft and N. D. Mermin, Solid State Physics. Holt, Rinehart, and Winston, New York, 1976.
"P. P. Ewald, "Die Berechnung Optischer und Elektrostatischer Gitterpotentiale," Ann. Phys. (Leipzig), 64, 253-87 (1921).
12M. P. Allen and D. J. Tildesley, Computer Simulation of Liquids; pp. 156-62. Oxford Press, Oxford, U.K., 1987.
13K. L. Kliewer and J. S. Koehler, "Space Charge in Ionic Crystals. I. General Approach with Application to NaCI," Phys. Rev. A, 140 [4A] 1226-39 (1965).
14D. M. Duffy and P. W. Tasker, "Space-Charge Regions around Dipolar Grain Boundaries," J. Appl. Phys., 56 [4] 971-77 (1984).
15B. G. Dick and A. W. Overhauser, "Theory of the Dielectric Constants of Alkali Halide Crystals," Phys. Rev., 112, 90-103 (1958).
16W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, Numerical Recipes in Fortran: The Art of Scientific Computing, 2nd ed.; pp. 413-18. Cambridge, New York, 1992.

$^{17}$J. D. Rittner, D. Udler, and D. N. Seidman, "Solute–Atom Segregation at Symmetric Twist and Tilt Boundaries in Binary Metallic Alloys on an Atom-Scale," *Interface Sci.*, **4**, 65–80 (1996).

$^{18}$A. P. Sutton and R. W. Balluffi, *Interfaces in Crystalline Materials*; pp. 3–68. Clarendon, Oxford, U.K., 1995.

$^{19}$H. Grimmer, R. Bonnet, S. Lartigue, and L. Priester, "Theoretical and Experimental Descriptions of Grain Boundaries in Rhombohedral $\alpha$-Al$_2$O$_3$," *Philos. Mag. A*, **61** [3] 493–509 (1990).

$^{20}$J. Cho, "Role of Rare-Earth Dopants on the Improved Creep Properties of Aluminum Oxide"; Ph.D. Thesis, Lehigh University, Bethlehem, PA, 1998.

$^{21}$D. Wolf, "Energy and Structure of (001) Coincidence-Site Twist Boundaries and the Free (001) Surface in MgO: Theoretical Study," *J. Am. Ceram. Soc.*, **67** [1] 1–13 (1984).

$^{22}$M. F. Ashby, F. Spaepen, and S. Williams, "The Structure of Grain Boundaries Described as a Packing of Polyhedra," *Acta Metall.*, **26**, 1647–63 (1978).

$^{23}$H. J. Frost, "A First Report on a Systematic Study of Tilt-Boundaries in Hard Sphere F.C.C. Crystals," *Scr. Metall.*, **14**, 1051–56 (1980).

$^{24}$J. L. Finney, "Random Packings and the Structure of Simple Liquids I. The Geometry of Random Close Packing," *Proc. R. Soc. London A*, **319**, 479–93 (1970).

$^{25}$D. Srolovitz, K. Maeda, S. Takeuchi, T. Egami, and V. Vitek, "Local Structure and Topology of a Model Amorphous Metal," *J. Phys. F: Met. Phys.*, **11**, 2209–19 (1981).

$^{26}$M. M. El-Aiat and F. A. Kröger, "Yttrium, an Isoelectric Donor in $\alpha$-Al$_2$O$_3$," *J. Am. Ceram. Soc.*, **65** [6] 280–83 (1982).

$^{27}$M. K. Loudjani, A. M. Huntz, and R. Cortès, "Influence of Yttrium on Microstructure and Point Defects in $\alpha$-Al$_2$O$_3$ in Relation to Oxidation," *J. Mater. Sci.*, **28**, 6466–73 (1993).

$^{28}$J. D. Eshelby, "The Continuum Theory of Lattice Defects," *Solid State Phys.*, **3**, 79 (1956).

$^{29}$T. S. Bush, J. D. Gale, C. R. A. Catlow, and P. D. Battle, "Self-Consistent Interatomic Potentials for the Simulation of Binary and Ternary Oxides," *J. Mater. Chem.*, **4** [6] 831–37 (1994).

$^{30}$D. McLean, *Grain Boundaries in Metals*, Clarendon, Oxford, U.K., 1957.

$^{31}$P. W. Tasker, "Surfaces of Magnesia and Alumina"; see Ref. 3, pp. 176–89.

$^{32}$M. A. Gülgün, V. Putlayev, and M. Rühle, "Effects of Yttrium Doping in $\alpha$-Alumina: I. Microstructure and Microchemistry," *J. Am. Ceram. Soc.*, **82** [7] 1849–56 (1999).

$^{33}$J. Cho, C. M. Wang, H. M. Chan, and J. M. Rickman, "Role of Segregating Ions on the Improved Creep Resistance of Aluminum Oxide," *Acta Mater.*, in press.

$^{34}$M. P. Harmer, H. M. Chan, J. M. Rickman, J. Cho, and C. M. Wang, "Grain Boundary Chemistry and Creep Resistance of Oxide Ceramics"; pp. 139–44 in *The Science of Engineering Ceramics II*. Edited by K. Niihara, T. Sekino, E. Yasuda, and T. Sasa. Trans Tech Publication Ltd., Aedermannsdorf, Switzerland, 1998. $\square$