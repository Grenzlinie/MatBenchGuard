![](./images/812111916347424769_1.jpg)

Available online at www.sciencedirect.com

![](./images/812111916347424769_2.jpg)

Physica E 33 (2006) 182–190

![](./images/812111916347424769_3.jpg)

www.elsevier.com/locate/physe

# Molecular-dynamics study of possible packing sequence of medium size gold clusters: $\mathrm{Au}_{2}-\mathrm{Au}_{43}$

Mustafa Böyükata*

Department of Physics, Erciyes University, 66100 Yozgat, Turkey

Received 16 October 2005; accepted 1 February 2006
Available online 29 March 2006

## Abstract

Growing pattern, structural stability, energetics and magic sizes of gold clusters, $\mathrm{Au}_{n}$ ($n=2-43$), have been investigated by using molecular-dynamics simulations. Starting from the dimer configuration, following rearrangement collision of the system in fusion process, and absorbing its energy step by step up to 0 K, possible stable structures of the clusters have been identified via an empirical model potential energy function. It has been found that gold clusters prefer to form three-dimensional compact structures and five-fold symmetry appears on the spherical medium clusters. This approach serves an efficient alternative to the growing path determination and the global optimization techniques.

© 2006 Elsevier B.V. All rights reserved.

PACS: 36.40.–c; 36.40.Qv; 61.46.+w; 02.70.Ns

Keywords: Gold clusters; Empirical potentials; Molecular dynamics

## 1. Introduction

Atomic clusters are aggregates of nanoscale particles that intermediate state of matter between atoms/molecules and bulk. They also exhibit a range of unusual physical and chemical properties such as structural, electronic and thermodynamic. Due to their broad applications toward biology, catalysis, and nanotechnology, the researches on clusters have shown a rapid development in both experimental and theoretical investigations over the last two decades [1–3]. In this area the changes of cluster properties as a function of size, such as evolution from small to large clusters, is one of the most interesting issues. Studies on the geometric and electronic structures are essential to understand the various properties. Unfortunately, the determination of equilibrium structures and of the atomic arrangements in transition metal (TM) clusters still remains a challenging task for the theoretician to answer the question of how the atoms are packed together in clusters.

Moreover, any experimental investigation and production of isolated microclusters are extremely difficult. For understanding the experimental observations computational studies provide helpful atomistic level simulations using empirical model potential energy functions (PEF) to investigate cluster properties.

For small clusters the first aim is usually to determine the lowest-energy minimum on the PEF using global optimization tools. For example, genetic algorithms (GA) have been applied to calculate the lowest energy for a specified PEF [4,5]. Other methods such as basin hopping (BH) [6–8] have shown to be accurate and widely used for the determination of the global minimum using various empirical PEFs for describing $\mathrm{Si}_{n}$ clusters [9]. As an alternative search method minima hopping (MH) has been suggested for complex molecular systems [10]. Similarly, simulated annealing (SA) has been also employed to investigate closed-shell systems [11]. Other strategies can be also proposed and analyzed in order to be a complementary tool for determining as efficient as possible global minima of hypersurfaces with especial attention to cluster formation even though several approximations are efficient for

---
*Tel.: +90 354 242 10 21/121; fax: +90 354 242 10 22.
E-mail address: boyukata@erciyes.edu.tr.

1386-9477/$ - see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.physe.2006.02.002

calculating minimum energy structures [12]. There are several proposed empirical PEFs in literature for various systems [13] which would predict cluster properties.

Gold microclusters are interesting and important in the physics and chemistry of TMs and their alloys because of the practical applications in nanocrystals and compounds [14–16]. There exist experimental works [17–19] and quantum mechanical calculations [20–22] for gold micro- clusters. Several empirical PEF [23–26] and empirical potential parametric calculations [27] were also reported for some model gold clusters. Using an empirical PEF the melting properties of gold particles were studied [28]. Additionally, structural properties of gold nanocrystalline clusters [29–31] and structural fluctuation of $Au_{55}$ and $Au_{147}$ clusters [32] have been studied. Recently, the groundstate geometrical structures of small gold clusters (up to 30 atoms) with their melting dynamics and isomer distributions of microstructers were also studied by using Monte Carlo (MC) and molecular-dynamics (MD) simulations [33].

In this paper, the computational investigation results are presented improving the basic understanding of the growing phenomena of isolated medium size gold clusters containing up to 43 atoms. MD simulations have been performed using a recently developed empirical PEF for gold [25,34]. The main aim here is to further understand the structural implications of this PEF by identifying the characteristic structural motifs associated with the stable minima of gold clusters. To predict their structural and energetic properties rearrangement collision approaches [12,35,36] in fusion regime has been applied to characterize the growing structures. A possible geometrical packing sequence was particularly studied for $Au_{2}-Au_{43}$ sizes.

## 2. Computational background

Classical MD method was applied for investigating the structures of gold cluster through the $Au+Au_{n-1}$ ($n \leqslant 43$) collision. It is possible to calculate the total interaction energy of $N$-particle system from the sum of suitable effective-pair interactions [25]. The used effective-pair PEF is in the form [25]

$$
V(r)=D_{21} \frac{A_{1}}{r^{\lambda_{1}}} \mathrm{e}^{-\alpha_{1} r^{2}}+D_{22} \frac{A_{2}}{r^{\lambda_{2}}} \mathrm{e}^{-\alpha_{2} r^{2}} \tag{1}
$$

with the parameters $A_{1}=345.923364$, $A_{2}=-38.9245908$, $\lambda_{1}=1.04289230$, $\lambda_{2}=1.05974062$, $\alpha_{1}=0.750775065$, $\alpha_{2}=$ $0.229377368$, $D_{21}=0.888911352$, and $D_{22}=0.254280292$ for gold. In these parameters, the energy is in eV and the distance is in Å. The effective-pair potential with $D_{21}=$ $D_{22}=1.0$ represents the dimer potential. The present empirical PEF for the gold element satisfies the bulk cohesive energy, and the bulk stability condition (for details see Ref. [25]). Via this PEF the classical Hamilton's equations were solved to follow the particles motion. For a many-particle system long trajectories are needed to estimate thermodynamic properties of the microcanonical ensemble using MD with any accuracy. These simulations can associate real time scales with finite nonergodic trajectories restricted to well-defined regions at the configuration space. The Runge–Kutta of fifth and sixth order algorithm is used as the numerical integration with the improvement of step size changing order which provides an efficient strategy. In the trajectory integration Cartesian coordinates are used for time dependent positions and moments of the particles. The accuracy of the phase space coordinates and the conservation of energy are considered in step size control of the micro canonical simulations. All trajectories were checked to produce energy conservations of the order of $10^{-10}$ during the integration.

At the beginning of the atom-cluster collision, the initial potential energy of the system is equal to the target $Au_{n-1}$ cluster energy. It is changing by the motion of the projectile atom towards the target. Therefore, the potential gets the new energy value depending on the final configuration of the new structure. While this building-up procedure the colliding atom was sent from a relatively large distance, asymptotic region in which the interaction energy with target is zero. Formation of the new cluster is related with the translation energy of the new projectile atom. To avoid the fragmentation and scattering, all collisions are realized with low energies to keep particles together in fusion regime. The initial kinetic energies, i.e. from the collision energy of the projectile atom, are distributed amongst the kinetic energies of all particles in the system after the interaction starts. Moreover, the initial center of mass motion was kept constant during the interaction and the collision occurs around the center of mass of the system. There might be many local minima on the PEF of a many- particle system. When the colliding atom, for example, hits the target cluster on any open sites it can easily construct a new structure. Collision sites on the target cluster are also effective for these regimes. The orientation space of the target clusters is randomly represented by Euler angles [37]. Upon relaxation, the cluster rearranged substantially. This process is repeated for five different orientation of initial configuration. The most stable one is determined through following each trajectory set by checking the potential energy of the system at 100 steps up to end of the two million steps. The newly generated configuration that has the energy nearest the minima in each trajectory set is kept and after 10 000 relaxation steps it is minimized by removing kinetic energy (up to 0 K) for finding the corresponding structure. This means that, totally, 10 million points are searched in the phase space to find the most stable geometry of each cluster. After determining the new cluster, it is used for new collision and these processes is repeated for finding new larger cluster. As in a similar way of our previous work [36], the methodology was applied to investigate the structures and the possible growing mechanism for these particular gold clusters up to 43.

## 3. Results and discussions

### 3.1. Geometries

The simulation procedure of rearrangement collision has been applied for optimizing the possible stable structures of gold clusters up to 43 atoms. The found lowest-energy structures are presented in Figs. 1–6. These results are in agreement with previously reported geometries of LJ clusters [38] and other relevant studies which will be discussed. The microstructures smaller than $\mathrm{Au}_{13}$ are displayed in Fig. 1. The well-known primitive geometries for 2-, 3- and 4-atom clusters are small enough to allow possible minima to be constructed directly. A regular tetrahedron is the most stable geometry of $\mathrm{Au}_{4}$ within $T_{\mathrm{d}}$ symmetry. Its bond length and binding energy values have been calculated as $2.93\,\mathrm{\mathring{A}}$ and $0.15\,\mathrm{eV/atom}$, respectively. A trigonal, an octahedron and a pentagonal bipyramids are predicted as ground state structures for $\mathrm{Au}_{5}$, $\mathrm{Au}_{6}$ and $\mathrm{Au}_{7}$ clusters with $0.55$, $0.63$ and $0.70\,\mathrm{eV/atom}$ binding energies, respectively. One of the previous studies [34], Erkoç has generated the microclusters, $n=3$–13, by adding an atom and annealing procedure. For each size he reported a unique structure. In spite of the same potential, in that study, the geometries for $\mathrm{Au}_{6}$ and $\mathrm{Au}_{7}$ clusters are different than here. In that study the determined geometries are growing from the stable structure of $\mathrm{Au}_{5}$. However, the structures, found here, for both sizes are more stable than those isomers. Within a good agreement with the results for $\mathrm{Au}_{8}$, the ground-state structure is an additional atom to the pentagonal bipyramid form ($D_{5\mathrm{h}}$ symmetry) of $\mathrm{Au}_{7}$ cluster. In this building-up procedure from $\mathrm{Au}_{9}$ to $\mathrm{Au}_{12}$ clusters the ground states geometries are in a growing pattern based on icosahedrons packing through filling the triangular open sites of 7-atom gold structure as shown in Fig. 1. In the present analysis, the second pentagonal ring is firstly observed in $\mathrm{Au}_{12}$ which is based on variant of the icosahedral structure. The obtained putative stable structure for the cluster $\mathrm{Au}_{13}$ is in spherical icosahedron form. Five-fold ring is a common backbone leading to nearly perfect icosahedrons form of 13-atom cluster. However, in Ref. [34] the obtained geometries for $\mathrm{Au}_{9}$–$\mathrm{Au}_{12}$ are different than these findings while the same spherical structure for 13-atoms. Most of the clusters, in general, might have various local minima corresponding to the absolute minimum energy of the PES of a many-particle system.

![](./images/812111916347424769_4.jpg)

Fig. 1. Equilibrium structures of gold microclusters for $n=2$–13.

![](./images/812111916347424769_5.jpg)

Fig. 2. Equilibrium structures of gold microclusters for $n=14$–19.

In addition to these microclusters, in this work, medium size small clusters have been also simulated and the stable structures are presented in Figs. 2–5. For microstructures consisting of a few atoms, it is easy to get a new structure by binding over a favorable open site. However, the new geometry for larger clusters may go in different local isomers of the new configuration due to their dislocated structures and high symmetries. The considerable adsorption regions are atop, bridge and hollow sites on cluster surfaces. From rearrangement structures it takes long computational time to obtain the stable geometry of the clusters unless the colliding atom hits the target at any suitable sites. Therefore the target position was randomly

![](./images/812111916347424769_6.jpg)

Fig. 3. Equilibrium structures of gold microclusters for $n=20$-$25$.

![](./images/812111916347424769_7.jpg)

Fig. 4. Equilibrium structures of gold microclusters for $n=26$-$31$.

changed. In this work, the ground state structures for Au₁₄-Au₁₉ clusters follow icosahedric growth pattern based on the geometry of Au₁₃ as shown in Fig. 2. For Au₁₉, the found geometry is the double icosahedrons structure ($D_{5h}$) which is another well-known magic size. The clusters possess the tendency to form trigonal pseudo- spherical polyhedra. As cluster size increases further, it becomes increasingly difficult to visualize the growth pattern. Even though the structural evolution of clusters in this region is more complicated, it is possible to analyze the cluster formation mechanism by investigating their preference for growing pattern. From Au₂₀ up to Au₃₄ clusters atoms prefer to fill favorable hollow sites (the most favorable adsorption site) on the equatorial region of the double icosahedrons form of Au₁₉. As shown in Fig. 3, Au₂₀ is growing up by adding an atom to the most open hollow sites on the equatorial part of Au₁₉ and filling another hollow site brings out Au₂₁ geometry. In a similar way up to Au₂₅ the clusters prefer to grow from the low coordination and more reactive sites on the equatorial region. A similar behavior was also observed in other studies for gold clusters in Refs. [39,40].

Fig. 4 illustrates the determined structures for Au₂₆-Au₃₁ sizes. Au₂₆ has an interesting view of crossed shape of 19-atom geometry as presented at the beginning of the figure. These structures are often based on the double icosahedrons geometry with the additional atoms attached to various positions on 19-atom cluster. As we reported a similar growing pattern for iron clusters [36] increasing the number of atoms on the surface of the cluster leads to some structural distortions of the basic building elements. It is observed here that the new optimized structure grows from hollow site of the previous smaller cluster. All configura- tions led to the migration of the colliding atom from the

![](./images/812111916347424769_8.jpg)

Fig. 5. Equilibrium structures of gold microclusters for $n=32-37$.

![](./images/812111916347424769_9.jpg)

Fig. 6. Equilibrium structures of gold microclusters for $n=38-43$.

on-top or bridge sites to hollow. The adsorbating atoms were generally introduced onto low coordination gold atoms due to their reactivity. As the consequence of this pattern (Fig. 5), filling the hollow and more reactive sites, all low coordination points on the equatorial region of $\mathrm{Au}_{19}$ are covered one by one by the addition of atoms and finally a closed shell structure of $\mathrm{Au}_{34}$ is formed with three new 5-atom rings. The structural evolution of $\mathrm{Au}_{35}$ cluster in this formation pattern is demonstrated in the form of placing atom on more reactive hollow site of $\mathrm{Au}_{34}$ geometry. As a result, the new larger sizes will continue to evaluate by filling the surface of 34-atom cluster, such as the growing pattern of $\mathrm{Au}_{36}$ and $\mathrm{Au}_{37}$. The smaller sizes of the determined global minima have centered icosahedral morphologies. While increasing the size, any of the octahedral, decahedral and icosahedral morphologies has also been observed for the predicted global minima. As shown in Fig. 6, for further large sizes up to $\mathrm{Au}_{43}$, increase in the number of atoms leads to more reactive favorable hallow sites on the surface of clusters. Therefore, it becomes more complicated to determine the most stable structures.

### 3.2. Energetics and magic sizes

The calculated total energy values $(E_{\text{tot}})$ for $\mathrm{Au}_{2}-\mathrm{Au}_{44}$ clusters are given in Table 1. The binding energies (the average interaction energy per atom in the cluster) versus the cluster size (the number of atoms in the cluster) are plotted for the putative stable structures in Fig. 7a. As the cluster size increases the average binding energy per atom decreases, which is an exponential like decaying. This general decaying trend with respect to the cluster size is a common behavior almost for all metal clusters [41]. A central issue in cluster physics is to identify particularly stable sizes. A detailed structural picture and the non-monotonic variation in the properties of clusters can be obtained by locating the global minimum as a function of size. This can then give information about the provided abundances of particularly stable clusters [42]. Figs. 7b and

<table><caption>Table 1 The calculated total energy values ($E_{\text{tot}}$) for $\text{Au}_n$ ($n=2$–44) clusters</caption>
<thead>
<tr>
<th>$n$</th>
<th>$E_{\text{tot}}$ (eV)</th>
<th>$n$</th>
<th>$E_{\text{tot}}$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>$-0.30485$</td>
<td>24</td>
<td>$-27.49300$</td>
</tr>
<tr>
<td>3</td>
<td>$-0.91455$</td>
<td>25</td>
<td>$-28.84086$</td>
</tr>
<tr>
<td>4</td>
<td>$-1.82908$</td>
<td>26</td>
<td>$-30.50368$</td>
</tr>
<tr>
<td>5</td>
<td>$-2.75472$</td>
<td>27</td>
<td>$-31.68834$</td>
</tr>
<tr>
<td>6</td>
<td>$-3.80116$</td>
<td>28</td>
<td>$-33.01304$</td>
</tr>
<tr>
<td>7</td>
<td>$-4.92834$</td>
<td>29</td>
<td>$-34.63892$</td>
</tr>
<tr>
<td>8</td>
<td>$-5.87104$</td>
<td>30</td>
<td>$-35.82830$</td>
</tr>
<tr>
<td>9</td>
<td>$-7.11028$</td>
<td>31</td>
<td>$-37.14164$</td>
</tr>
<tr>
<td>10</td>
<td>$-8.33834$</td>
<td>32</td>
<td>$-38.45583$</td>
</tr>
<tr>
<td>11</td>
<td>$-9.56294$</td>
<td>33</td>
<td>$-39.96552$</td>
</tr>
<tr>
<td>12</td>
<td>$-11.04486$</td>
<td>34</td>
<td>$-41.43849$</td>
</tr>
<tr>
<td>13</td>
<td>$-12.87841$</td>
<td>35</td>
<td>$-42.64175$</td>
</tr>
<tr>
<td>14</td>
<td>$-13.83486$</td>
<td>36</td>
<td>$-43.95120$</td>
</tr>
<tr>
<td>15</td>
<td>$-15.08184$</td>
<td>37</td>
<td>$-45.53733$</td>
</tr>
<tr>
<td>16</td>
<td>$-16.31843$</td>
<td>38</td>
<td>$-46.93205$</td>
</tr>
<tr>
<td>17</td>
<td>$-17.54577$</td>
<td>39</td>
<td>$-48.29073$</td>
</tr>
<tr>
<td>18</td>
<td>$-18.99694$</td>
<td>40</td>
<td>$-49.96025$</td>
</tr>
<tr>
<td>19</td>
<td>$-20.76827$</td>
<td>41</td>
<td>$-51.42916$</td>
</tr>
<tr>
<td>20</td>
<td>$-21.97855$</td>
<td>42</td>
<td>$-52.73162$</td>
</tr>
<tr>
<td>21</td>
<td>$-23.19181$</td>
<td>43</td>
<td>$-54.63580$</td>
</tr>
<tr>
<td>22</td>
<td>$-24.59053$</td>
<td>44</td>
<td>$-55.82702$</td>
</tr>
<tr>
<td>23</td>
<td>$-26.30390$</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

c show the first energy difference and the second finite difference (the stability function) of the total energy of the determined clusters

$$
\Delta_{1} E=E_{n+1}-E_{n}, \tag{2}
$$

$$
\Delta_{2} E=E_{n+1}+E_{n-1}-2 E_{n}, \tag{3}
$$

as a function of the number of atoms, respectively. The peaks shown in Fig. 7c correspond to the most stable structures (magic clusters) and the minima show the most unstable sizes. The following magic numbers are observed: 7, 13, 19, 23, 26, 29, 34, 37, 40, 43. The corresponding sizes for the least stable clusters are: 8, 12, 14, 18, 22, 25, 28, 30, 32, 36, 39, 42. In Ref. [43], the corresponding peaks in the stability function appear at $n=13,19,23,26,29,32,34,43$ for LJ clusters and all of them emerge in our results. It is clearly understood that further calculations and alternative analysis with more accurate methods may be helpful to identify magic clusters.

![](./images/812111916347424769_10.jpg)

Fig. 7. (a) Binding energies; (b) first and (c) second finite difference of the total energies for the stable clusters up to $\text{Au}_{43}$.

### 3.3. Structure analysis

In previous section, it was seen that there are some particular sizes having energetically magic characteristics. In order to obtain further general information on the size dependence of the structural growing and to confirm this magic behavior, distributions of the atoms in the determined stable geometries have been investigated (Fig. 8). Firstly, we will study the radial distributions of the atoms, which are displayed in Fig. 8a. The radial distribution is the distance of each atom to the center of mass of an $\text{Au}_n$ cluster, as follows:

$$
r_{i}=\left|R_{i}-R_{0}\right|,
$$

$$
R_{0}=\frac{1}{n} \sum_{i=1}^{n} R_{i}, \tag{4}
$$

where $R_i$ is the position of the $i$th atom. Subsequently, all these distances are shown as a function of the cluster size,

![](./images/812111916347424769_11.jpg)

Fig. 8. (a) Radial distributions; (b) pair distances of atoms and (c) second finite differences of mean values for the radial and pair distributions for the stable clusters up to Au₄₃.

in the upper panel of Fig. 8. One of the aspects in the resulting diagram of this analysis is the increasing radius of the clusters with increasing size. For the largest distance to the origin (assumed as radius of the cluster) increases continuously with the increasing number of atoms. Some irregularities occur and in those cases the cluster radius decreases slightly by adding an atom e.g., the radius of Au₈ is larger than those of its larger neighbors up to $n=13$. The maxima in the largest distances correspond to the more reactive sizes. Au₁₄, for example, has more reactive sites due to the low coordination of the system. Especially in the trends of the radius of the clusters (largest distances) have lower values identifying obviously for determined magic sizes. In most cases, this decrease is consistent with a reorganization of the system and an increase of the number of symmetry elements. In Ref. [44] Joswig and Springborg has noticed similar aspects from the same analysis for aluminum clusters. Another aspect is that the increasing number of atoms per cluster leads various different distances. It means that these clusters have lower symmetries than those with only a few different distances to the origin [44]. Moreover, it is possible to identify more atomic shells from this radial distribution. The second shell of atoms is established already from Au₁₃ but for the smallest systems the inner shell contains just a single atom which is placed very close to the center of the cluster. The microclusters up to 13-atom cluster grow via pushing an atom to the center. Au₄ and Au₆ have similar behavior because they are in regular tetrahedron octahedron structures, respectively. That is, all atoms are in the same distance from the center. The largest empty space is in the 6-atom microcluster. Especially for magic sizes the number of atoms of the inner shell can be easily observed due to their higher symmetric structures. For example, Au₁₉ and Au₂₆ have mainly four distances. After Au₁₅ the deviation of the central atom has dominantly increased up to Au₂₆. It reaches the biggest value in this medium size region. Au₂₆ is a turning point for central atom because the growing structure in this point has half-filled equatorial sites of the Au₁₉ cluster. Even though the closest and the largest distances have absolutely different properties, the mean displacements from center of mass of the clusters are, as expected, in slightly increasing due to the close packing phenomena.

In Fig. 8b mean, minimum and maximum values of the pair displacement distributions of the consisting atoms are demonstrated for Au₂-Au₄₄ clusters as a function of number of atoms. Maximum, minimum and mean pair distances of atoms are the same, $2.93\,\text{\AA}$, for 4-atom cluster due to its regular pyramidal geometry. The minimum pair distances decrease slightly while the mean pair distance increases with the increasing number of atoms because the increase in the number of atoms leads to close packing of the system. When it reaches up to 44-atom the mean and minimum values become 5.91 and $2.64\,\text{\AA}$, respectively. On the other hand, the maximum pair distances have different trends in different size ranges. Structurally, different reorientations cause sudden increases and fluctuations in the maximum pair distances. For example, up to Au₈ all structures are in different orientations. From Au₈ to Au₁₃ the icosahedrons packing based growing pattern based on pentagonal bipyramid structure of Au₇ results in decrease for maximum pair distances. An addition of an atom to the triangular open sites of Au₁₃ again leads a new increase in the maximum pair distance suddenly for Au₁₄. Up to Au₁₉ the growing pattern is based on 13-atom geometry. The distance between two polar atoms of 19-atom cluster is the

source of the rapid increase in the maximum pair distance from $Au_{18}$ to $Au_{19}$. From $Au_{19}$ up to $Au_{26}$ one observes a slightly decrease in the maximum pair distances. For the particular case of $Au_{26}$ there is an interesting symmetry-like structure, crossing shape of the two 19-atom clusters. After passing $Au_{26}$ structure there is a rapid increase in the maximum pair distance due to new nonsymmetric form of $Au_{27}$. There are slightly fluctuations in regions 27-34 and relatively rapid increase up to 39. Final decrease is observed at $Au_{41}$ and again a new increase occurs for further sizes. Generally, any typical changes are determined around the magic sizes.

In Fig. 8c the second finite difference of the distributions of optimized structures for $Au_{3}-Au_{43}$ are presented for average values of radial and pair distributions as a function of cluster size. Structural reorientations of $Au_{4}$ and $Au_{6}$ lead peaks in the values of the second finite differences. $Au_{13}$ has peak due to the effect of its spherical structures. In all cases, for similar stability functions of maximum and minimum displacements, this cluster has the same char- acteristic. As shown in the graph for all energetically magic-like sizes up to 43 peaks are also visualized except $Au_{19}$, $Au_{32}$ and $Au_{43}$. These peaks for 23, 26, 29 and 34 are related with the structures of these clusters and their close packing sequences. They describe the reactive sites filled structures and these results are in good agreement with our previous results for iron clusters [36].

To investigate the growth mechanism in more detail, the density coefficients for number of atoms per volume of the clusters were also calculated which is defined as follows. For each cluster

$$
\sigma(n)=\frac{n}{r_{n}^{3}} \tag{5}
$$

is the proportionality values of the cluster density. In the equation, $n$ is the number of atoms and $r_{n}$ is the radius of the cluster corresponding to the largest value of the radial distributions in Fig. 8a. Figs. 9a and b illustrate the density coefficients and their stability functions. There are big fluctuations in microcluster region. It means they are reoriented through the changing of all the atom positions. This fluctuation is smaller for medium size clusters because for larger clusters the orientation of the new clusters after rearrangement collision occurs on the surface atoms of the clusters. Inner structures of these clusters generally keep their previous geometries. The minima in the stability functions visualize the relatively more close packing sizes such as 4, 6, 13, 23, 26, 29 and 34.

### 4. Conclusions

In this paper, rearrangement collision procedure has been performed to find likely global minima for the free $Au_{n}$ clusters in the size range of $n=2-44$ whose interac tions are described by a pair potential. Using MD and energy minimization techniques it has been found out that gold clusters prefer to form three-dimensional compact structures and five-fold symmetry appears on the spherical clusters.

![](./images/812111916347424769_12.jpg)

Fig. 9. (a) Density coefficients and (b) their stability values.

As a result, the PEF can be used for qualitative structural analysis of medium size clusters such as for determinations of growing pattern and magic sizes. The rearrangement collision approach, as an alternative proce- dure, is more efficient for the investigation of possible growing pattern of the stable structures of atomic clusters. The procedure can easily be applied to the other cluster systems with different interatomic PEFs. In addition the selected structural analysis in this work (radial, pair and density coefficient distributions) can be efficiently used and generalized for further studies and for other material clusters.

### Acknowledgments

This work was supported by Research Fund of Erciyes University.

### References

[1] H. Haberland (Ed.), Clusters of Atoms and Molecules, Springer, Berlin, 1994.

[2] W.A. de Heer, Rev. Mod. Phys. 65 (1993) 612.

[3] Y. Gao, X.C. Zeng, J. Am. Chem. Soc. 127 (2005) 3698.

[4] G. Rossi, R. Ferrando, A. Rapallo, A. Fortunelli, B.C. Curley, L.D. Lloyd, R.L. Johnston, J. Chem. Phys. 122 (2005) 194309.

[5] B. Hartke, Struct. Bonding 110 (2004) 33.

[6] D. Wales, J. Doye, J. Phys. Chem. A 101 (1997) 5111.

[7] A. Sebetci, Z.B. Güvenç, Model. Simul. Mater. Sci. Eng. 13 (2005) 683.

[8] J. Doye, D. Wales, M. Miller, J. Chem. Phys. 109 (1998) 8143.

[9] S. Yoo, X. Zeng, J. Chem. Phys. 119 (2003) 1442.

[10] S. Goedecker, J. Chem. Phys. 120 (2004) 9911.

[11] M.D. de Andrade, K.C. Mundim, L.A.C. Malbouisson, Int. J. Quantum Chem. 103 (2005) 493.

[12] I.A. Solov'yov, A.V. Solov'yov, W. Greiner, Int. J. Mod. Phys. E 13 (2004) 697.

[13] S. Erkoç, Phys. Rep. 278 (1997) 79.

[14] R.P. Andres, J.D. Bielefeld, J.I. Henderson, D.B. Janes, V.K. Kolagunda, C.P. Kubiak, W.J. Mahoney, R.F. Osifchin, Science 273 (1996) 1691.

[15] L.D. Marks, Rep. Prog. Phys. 57 (1994) 603.

[16] H. Hakkinen, B. Yoon, U. Landman, X. Li, H.J. Zhai, L.S. Wang, J. Phys. Chem. A 107 (2003) 6168.

[17] M.D. Morse, Chem. Rev. 86 (1986) 1049.

[18] J. Ho, K.M. Ervin, W.C. Lineberger, J. Chem. Phys. 93 (1990) 6987.

[19] C. Jaackschath, I. Rabin, W. Schuze, Z. Phys. D 22 (1992) 517.

[20] C.W. Bausclicher Jr., S.R. Langho, H. Partridge, J. Chem. Phys. 93 (1990) 8133.

[21] K.K. Das, K. Balasubramanian, Chem. Phys. Lett. 176 (1991) 571.

[22] D.W. Lias, K. Balasubramanian, J. Chem. Phys. 97 (1992) 2548.

[23] S. Erkoç, Phys. Stat. Sol. B 161 (1990) 211.

[24] S. Erkoç, Chem. Phys. Lett. 173 (1990) 57.

[25] S. Erkoç, Z. Phys. D 32 (1994) 257.

[26] J.Y. Fang, R.L. Johnston, J.N. Murrell, J. Chem. Soc. Faraday Trans. 89 (1993) 1659.

[27] J. Uppenbrink, D.J. Wales, J. Chem. Phys. 96 (1992) 8520.

[28] F. Ercolessi, W. Andreoni, E. Tosatti, Phys. Rev. Lett. 66 (1991) 911.

[29] C.L. Cleveland, U. Landman, T.G. Schaa, M.N. Shagullin, P.W. Stephens, R.L. Whetten, Phys. Rev. Lett. 79 (1997) 1873.

[30] C.L. Cleveland, W.D. Luedtke, U. Landman, Phys. Rev. Lett. 81 (1998) 2036.

[31] J.A. Ascencio, C. Gutierrez-Wing, M.E. Espinosa, M. Marin, S. Tehuacanero, C. Zorrilla, M. Jose-Yacaman, Surf. Sci. 396 (1998) 349.

[32] S. Sawada, S. Sugano, Z. Phys. D 24 (1992) 377.

[33] H. Arslan, M.H. Güven, New J. Phys. 7 (2005) 60.

[34] S. Erkoç, Physica E 8 (2000) 210.

[35] J. Rogan, R. Ramirez, A.H. Romero, M. Kiwi, Eur. Phys. J. D 28 (2004) 219.

[36] M. Böyükata, E. Borges, J.P. Braga, J.C. Belchior, J. Alloys Compd. 403 (2005) 349.

[37] R.M. Lynden-Bell, A.J. Stone, Mol. Sim. 3 (1989) 271.

[38] D.J. Wales, J.P.K. Doye, J. Phys. A 101 (1997) 5111.

[39] M. Mavrikakis, P. Stoltze, J.K. Nørskov, Catal. Lett. 64 (2000) 101.

[40] N.S. Phala, G. Klatt, E. van Steen, Chem. Phys. Lett. 395 (2004) 33.

[41] G. Scoles (Ed.), The Chemical Physics of Atomic and Molecular Clusters, North-Holland, Amsterdam, 1990.

[42] J. Schmelzer Jr., S.A. Brown, A. Wurl, M. Hyslop, R.J. Blaikie, Phy. Rev. Lett. 88 (2002) 226802.

[43] I.A. Solov'yov, W. Greiner, A. Koshelev, A. Shutovich, Phys. Rev. Lett. 90 (2003) 053401.

[44] J.-O. Joswig, M. Springborg, Phys. Rev. B 68 (2003) 085408.