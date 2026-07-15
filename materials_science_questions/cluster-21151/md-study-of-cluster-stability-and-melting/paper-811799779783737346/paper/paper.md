# Reentrant Morphology Transition in the Growth of Free Silver Nanoclusters

F. Baletto, $^{1}$ C. Mottet, $^{2}$ and R. Ferrando $^{1, *}$

$^{1}$INFM and CFSBT/CNR, Dipartimento di Fisica dell'Università di Genova, via Dodecaneso 33, 16146 Genova, Italy
$^{2}$CRMC2/CNRS, Campus de Luminy, Case 913, 13288 Marseille Cedex 9, France
(Received 7 February 2000)

The growth of free silver nanoclusters is studied by molecular dynamics simulations, from a small seed up to sizes $N \simeq 150$. It is shown that the final outcome of the growth process depends crucially on the growth conditions (deposition flux $\phi$ and temperature $T$). A reentrant morphology transition is obtained: at intermediate values of $T$ and $\phi$ a "decahedral window" is found; the window is surrounded by regimes where icosahedra are preferentially grown.

PACS numbers: 61.46.+w

The study of the growth properties of small (tens through hundreds of atoms) metal particles is of great importance for the applications, for example, in the fields of the controlled growth of nanostructures [1] and of catalysis [2]. Much experimental and theoretical effort has been devoted to the determination of the most favorable structures depending on the cluster size $N$. Small noble-metal clusters can present "noncrystallographic" structures, such as icosahedra (Ih) and decahedra (Dh) [3]. Both Ih and Dh are characterized by fivefold symmetry axes (six and one axes for Ih and Dh, respectively). For small Au clusters [4], it has been demonstrated that the truncated Marks decahedra [5] $[(m, n, p) m$-Dh, where $(m, n, p)$ are integers describing the truncation [4,5]; some $m$-Dh structures are represented in Fig. 1)] are favorable structures, together with a set of amorphous structures [6], in the range 50-250 atoms, and that icosahedra (Ih) are melting-precursor structures. On the other hand, experiments [7] of Ag and Cu cluster growth in inert gas aggregation (IGA) sources [8] have shown the existence of both Dh and Ih structures in a size range corresponding to cluster diameters of about 2 nm; the relative abundances of Ih and Dh structures strongly depend on the experimental conditions [7].

A crucial issue in the building of these nanostructures is the understanding of how the growth conditions, as opposed to purely thermodynamical factors (as energetics and a study of most stable structures at a given size by some algorithm), can determine the final atomic arrangement of the cluster; the importance of the growth conditions has been argued from the experimental observations of metal clusters of icosahedral or decahedral structures (see, for example, [5,7]) at such large sizes that only crystallographic structures (fcc structures for noble metals) were expected to exist there.

In this Letter, we study the growth of Ag nanoclusters in the $N$ range from a few atoms to about 150 atoms by molecular dynamics (MD) simulations on realistic time scales, in order to understand how the growth conditions influence the building up of cluster structures from a microscopic point of view. In our simulations we show that (a) in wide ranges of $(T, \phi)$, we obtain always Ih structures around the magic number 55 (see Fig. 1), and Dh structures around 75, in agreement with the predictions of Michaelian *et al.* [9], who performed the structural optimizations at these magic numbers; (b) at larger sizes, we find the main result of our Letter: we demonstrate that the resulting morphology depends crucially on growth conditions. Around $N = 150$, where two competing magic structures are present (the 146 $(3,2,2) m$-Dh and the 147 Ih, see Fig. 1), Ih are grown preferentially at low and high $T$, and Dh at intermediate $T$: a reentrant morphology transition takes place. The name "reentrant" is chosen in analogy with the reentrant layer-by-layer transition found in the epitaxial growth of Pt/Pt(111) [10], where a 3D-growth window [at intermediate $(T, \phi)$] is surrounded by layer-by-layer regimes.

![](./images/811799779783737346_1.jpg)

FIG. 1. Optimized structures at magic numbers.

Our simulations are thus able to reproduce both Ih and Dh structures in the 2 nm size range, in agreement with the experiments [7]. The results contained in the following demonstrate explicitly the importance of kinetic factors and show their interplay with thermodynamics.

We model Ag by many-body potentials as developed by Rosato, Guillopé, and Legrand [11] (RGL). The form and the parameters of the potentials for noble metals can be found in Ref. [12]. These potentials are developed on the basis of the second-moment ap- proximation to the tight-binding model, and can be considered as a kind of embedded atom potential [13]. RGL potentials have been successfully tested in many simulations of surface diffusion on noble and transition metals [12].

In our simulations, we start from a small seed of seven atoms arranged as a pentagonal bipyramid. We have veri- fied that this structure is the most stable at seven atoms (in agreement with the calculations in Ref. [14]; on the other hand, the geometry of other isomers of Ag₇ and of smaller clusters is not correctly reproduced by our poten- tials). However, the starting arrangement is not important for the development of the simulation, because all cluster atoms are free to move and, at small sizes, they can rear- range in a short time. Atoms are deposited one by one on the cluster, at time intervals of length $\tau = 1/\phi$, by putting the atom on a randomly chosen point on a large sphere cen- tered around the cluster center of mass, and directing the atom velocity towards the cluster. The initial velocity of the deposited adatom is chosen as the average velocity at 1500 K, corresponding to a typical evaporation tempera- ture of Ag in an IGA source [7]. As time intervals $\tau$ we have considered 2.1, 7, and 21 ns. These deposition in- tervals are close to those in IGA experiments; at an Ag pressure of 3 mbar, the average interval between impacts on a 55 Ih is of the order of one atom each 50–100 ns. The total simulation time for $\tau = 21$ ns is about $3\ \mu$s, and a complete growth simulation takes five days of CPU time on a last-generation workstation. In between two subse- quent depositions, the cluster is thermalized [15] at a given temperature $T$, by means of an Andersen thermostat [16], whose stochastic collision frequency is chosen in order to obtain an efficient thermalization without perturbing the diffusive properties of the cluster atoms (see [17] for a de- tailed discussion). $T$ is chosen in the range 350–600 K, following the available estimates of cluster temperatures in IGA experiments [7], which indicate values within the above range.

In the following, we describe the results of our simu- lations, first at small sizes and then around 150 atoms. We have performed a systematic analysis of local atomic structure by the common neighbor analysis [18], on sev- eral thousands of snapshots for each simulation. A com- plete description of the analysis will be reported elsewhere. Typical simulation results can be well summarized by Fig. 2, where snapshots from simulations at different tem- peratures but at the same flux are reported.

![](./images/811799779783737346_2.jpg)

FIG. 2. Snapshots of cluster growth at $\tau = 1/\phi = 7$ ns from three simulations at three different temperatures: 400 K (top row), 500 K (middle row), 600 K (bottom row). In each row, the five snapshots are taken at sizes of 55, 75, 105, 135 and 147 atoms from left to right. At 147 atoms, Ih structures are obtained in the simulations at 400 and 600 K, and a Dh at 500 K. At 55 atoms, we obtain an Ih at 400 and 500 K (the structure at 600 K is fluctuating fast); at 75 atoms, we obtain a Dh at 400 and 500 K and a melted structure at 600 K.

Results at small sizes.—Apart from the small perfect structures around $N = 10$, the first magic structure which is encountered during growth is the 55 Ih (see Fig. 1). This structure is favored from the energetic point of view (as shown in Ref. [9], with this respect, Ag is different from Au [4]), as can be seen in Fig. 3, and it is obtained in all 45 simulations we have performed up to 550 K. Slightly below 600 K the 55 Ih melts, and it can appear sometimes in the simulations at 600 K in the fluctuation among dif- ferent structures. In the simulations, structures which are very close to a perfect 55 Ih are always obtained, often without defects, and with a maximum of one couple of diffusing defects (a vacancy plus an adatom). Also the 75 (2,2,2)$m$-Dh is a favored structure [9], and we have estimated its melting temperature to be around 550 K. In the simulations, 75 (2,2,2)$m$-Dh are always grown at any of the three fluxes up to 500 K. However, at the lowest tem- peratures, Dh structures with asymmetries and/or defects are grown. In the $N$ range between 55 and 75, we have first Ih structures (the 55 Ih plus adatom islands) and then a transition to incomplete Dh structures above 65 atoms, where the latter are the best from the energetic point of view.

Results around $N = 150$.—At these sizes, the results display a richer phenomenology, as can be seen in Table I. This happens because of the existence of two competing magic structures in the same size range: the 146 (3,2,2)$m$-Dh and the 147 Ih. The latter is more favorable from the energetic point of view (see Fig. 3); we have also verified that a 146 Ih obtained from the perfect 147 Ih by cutting one vertex has a slightly lower energy than the perfect 146 (3,2,2)$m$-Dh. However, our results show that there is a wide $(T,\phi)$ range (centered

![](./images/811799779783737346_3.jpg)

FIG. 3. $\Delta$ [Eq. (1)] as a function of the cluster size $N$ for some structures corresponding to magic numbers. The squares correspond to Ih structures, and the circles to $m$-Dh structures. The full circles are not-centered $m$-Dh with six atoms along the symmetry axis, whereas the open circles are centered $m$-Dh, with five atoms along the symmetry axis. The lines are only guides to the eyes.

around 500 K at the fluxes of our simulations) where only $m$-Dh are obtained in practice. These structures must be due to kinetic factors (see the discussion below). We obtain usually almost perfect $m$-Dh. At low $T$, Ih are preferentially grown; however, at the lowest temperature and with fast fluxes, we often obtain hybrid structures with many defects. At high temperatures Ih are again more likely to grow: at 600 K we have obtained always almost perfect Ih. Therefore, the morphology transition reenters at high temperatures for clusters of size $N \simeq 150$.

Just to give a schematic picture of the results with reference to the structures in Fig. 1, we can say that during a low-$T$ simulation, we recover a sequence of the kind $(A) \to (B) \to (C) \to (F)$, while at intermediate $T$ a sequence of the kind $(A) \to (B) \to (D) \to (E)$ is reproduced. At high $T$, we recover melted structures up to $N \simeq 135$ and finally we reproduce always structure $(F)$.

The reentrant morphology transition can be understood in the following scenario, with the help of Fig. 3, where the quantity $\Delta$ [4], defined as

$$
\Delta=\frac{E_{N}-\varepsilon_{B} N}{N^{2 / 3}} \tag{1}
$$

($E_N$ is the optimized energy of a cluster of size $N$ and $\varepsilon_B$ is the cohesive energy per atom in bulk Ag), is plotted for the magic structures.

Let us consider, for example, the case of $\tau=7$ ns (third column in Table I) and examine first the low-$T$ (350-400 K) case. At these temperatures, the 55 Ih and the 75 (2,2,2)$m$-Dh are formed, with fewer and fewer defects as $T$ increases. Both the 55 Ih and the 75 (2,2,2)$m$-Dh are centered structures with five atoms along each symmetry axis. Now we add further atoms to the 75 (2,2,2)$m$-Dh. Some of these atoms diffuse towards sites on the side of the Dh, where they tend to complete the structure of the 100 (3,1,2)$m$-Dh (see Fig. 1). In fact, also the 100 (3,1,2)$m$-Dh is a centered structure with five atoms along its axis, and can be obtained from the 75 (2,2,2)$m$-Dh by addition of atoms in the truncations. Around $N=100$ the most favorable structure is the 101 (2,3,2)$m$-Dh (see Fig. 3). This $m$-Dh is not centered, with six atoms along its axis. At low $T$ the growing cluster is not able to optimize its energy, and the cluster remains trapped along the line connecting the 75 (2,2,2) and the 100 (3,1,2)$m$-Dh, which are quite similar structures. When the 100 (3,1,2)$m$-Dh is practically completed, the addition of more atoms causes the nucleation of islands on the facets, and starts the formation of an external icosahedral shell (see the third snapshot in the top row of Fig. 2). Then the incomplete icosahedral structure keeps on growing and the Ih symmetry propagates to the center of the cluster. At the end a 147 Ih (a centered structure with seven atoms along each symmetry axis) is grown. At intermediate temperatures (from 450 to 550 K) the situation is different (see Fig. 2). In fact, around $N=100$, the cluster is able to optimize its energy, and to perform a transition to the best structures [those related to the 101 (2,3,2)$m$-Dh, see the third snapshot in the middle row of Fig. 2]. Adding further atoms, the truncation is completed, and the 146 (3,2,2)$m$-Dh is formed (the latter is a not-centered structure with six atoms along its axis, and it can be obtained from the 101 (2,3,2)$m$-Dh by adding atoms to the truncations). The completion of the 146 (3,2,2)$m$-Dh is achieved even if, above $N \simeq 130$, Ih

<table>
<caption>TABLE I. Simulation results at 147 atoms for different temperatures $T$ and fluxes $\phi=1/\tau$ ($\tau$ is the interval between subsequent depositions). For each couple $(T,\phi)$ three independent simulations were made. At the lowest $T$ we often obtain structures which are hybrids composed by both Ih-like and Dh-like parts.</caption>
<thead>
  <tr>
    <th>$T$ (K)</th>
    <th>$\tau=2.1$ ns</th>
    <th>$\tau=7.0$ ns</th>
    <th>$\tau=21.0$ ns</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>350</td>
    <td>3 hybrid</td>
    <td>2 Ih + 1 hybrid</td>
    <td>1 Ih + 1 Dh + 1 hybrid</td>
  </tr>
  <tr>
    <td>400</td>
    <td>2 Ih + 1 Dh</td>
    <td>2 Ih + 1 hybrid</td>
    <td>1 Ih + 2 Dh</td>
  </tr>
  <tr>
    <td>450</td>
    <td>2 Ih + 1 Dh</td>
    <td>3 Dh</td>
    <td>3 Dh</td>
  </tr>
  <tr>
    <td>500</td>
    <td>3 Dh</td>
    <td>3 Dh</td>
    <td>3 Dh</td>
  </tr>
  <tr>
    <td>550</td>
    <td>1 Ih + 2 Dh</td>
    <td>3 Dh</td>
    <td>2 Ih + 1 Dh</td>
  </tr>
  <tr>
    <td>600</td>
    <td>3 Ih</td>
    <td>3 Ih</td>
    <td>3 Ih</td>
  </tr>
</tbody>
</table>

structures (those leading to the 147 Ih) are energetically more favorable. However, at intermediate temperatures, the growing structure remains trapped in a not-centered Dh structure. If $T$ is raised further (up to about 600 K, see Fig. 2), the growing cluster becomes able to optimize its energy above $N \simeq 130$ and to complete the transition to the 147 Ih.

At slower fluxes (for example, $\tau=21 \mathrm{~ns}$) the morphology transitions are displaced: $146(3,2,2) m$-Dh are already obtained at 400 K and some 147 Ih appear already around 550 K.

Our structure optimizations show that the $146(3,2,2) m$ -Dh is not the best structure at that size. Therefore, we expect it to be a metastable cluster evolving at long times towards the minimum-energy structure (an Ih with one atom less; truncating a vertex of the 147 Ih or even putting one vacancy at the center, a better structure than the 146 Dh is obtained [19]). However, these times can be very long, in such a way that the $146(3,2,2) m$-Dh could be observed in experiments. We have taken a 146 $(3,2,2) m$-Dh perfect structure and we have let it evolve at different temperatures. At 650 K the structure disorders fast, on the scale of 4 ns; at 600 K the structure stays stable on times of the order of 80 ns and then transforms into an Ih; finally, at 550 K the structure is stable for more than $3 \mu \mathrm{s}$, i.e., at least 30 times more than at 600 K. From these results, one would expect that a $146(3,2,2) m$-Dh at 450 K be stable on the scale of several milliseconds. Finally, we have checked that the 147 Ih, as obtained in the simulations at 600 K, is a stable structure, and it does not fluctuate to different isomers on the experimental growth time scales. We have let a 147 Ih evolve freely for $10 \mu \mathrm{s}$ (a time which is more than 2 orders of magnitude longer than the interval between depositions in experiments) at 600 K, and the 147 Ih has retained its shape during the whole time. This has to be compared to the much shorter lifetime (some tens of ns) of the Dh structure at 600 K. In fact, the latter has a higher energy with respect to the Ih by more than 0.4 eV. This check on the stability of the 147 Ih (whose melting occurs in the range 650-670 K in our model) completes the demonstration that a real reentrant transition is found.

In this Letter, we have reported the first (to our knowledge) MD simulation of cluster growth from a seed of a few atoms to two-nanometer sizes on realistic time scales, and studied the dependence of the cluster structures on the growth conditions. In fact, we have demonstrated that the resulting structure of nanometer Ag clusters depends on kinetic factors and can differ from the minimum- energy structure. At small sizes (less than 100 atoms), minimum-energy Ih and $m$-Dh structures are always recovered as the growth proceeds. On the other hand, at larger sizes, of about 150 atoms, different magic structures are in competition. In this case, the final outcome depends crucially on the growth conditions, and a reentrant morphology transition takes place: at a given deposition flux, Ih structures are obtained at low and high temperatures, while Marks truncated Dh structures are grown in the intermediate range. The latter $m$-Dh have higher energies than the icosahedra in this size range, and therefore they are metastable growth structures. However, they can be stable for such long times to allow the experimental detection. This agrees with the experimental observation [7] of both Ih and Dh Ag structures at diameters close to 2 nm.

We thank W. Harbich, B. Legrand, A.C. Levi, R. Monot, F. Montalenti, and G. Tréglia for useful discussions and critical reading of the manuscript. F. Baletto and R. Ferrando acknowledge financial support from the Ital- ian MURST under Project No. 9902112831. The CRMC2 is associated with the Universities of Aix-Marseille II and III.

*Corresponding author.
Email address: ferrando@fisica.unige.it

[1] P. Jensen, Rev. Mod. Phys. 71, 1695 (1999).
[2] C.R. Henry, Surf. Sci. Rep. 31, 231 (1998).
[3] T.P. Martin, Phys. Rep. 273, 199 (1996).
[4] C.L. Cleveland et al., Phys. Rev. Lett. 79, 1873 (1997); C.L. Cleveland, W.D. Luedtke, and U. Landman, Phys. Rev. Lett. 81, 2036 (1998).
[5] L.D. Marks, Rep. Prog. Phys. 57, 603 (1994).
[6] I.L. Garzon et al., Phys. Rev. Lett. 81, 1600 (1998); J.M. Soler et al., Phys. Rev. B 61, 5771 (2000).
[7] B.D. Hall, M. Flüeli, R. Monot, and J.-P. Borel, Phys. Rev. B 43, 3906 (1991); D. Reinhard, B.D. Hall, D. Ugarte, and R. Monot, Phys. Rev. B 55, 7868 (1997); D. Reinhard, B.D. Hall, P. Berthoud, S. Valkealahti, and R. Monot, Phys. Rev. Lett. 79, 1459 (1997).
[8] W. de Heer, Rev. Mod. Phys. 65, 611 (1993).
[9] K. Michaelian, N. Rendón, and I.L. Garzon, Phys. Rev. B 60, 2000 (1999).
[10] R. Kunkel, B. Poelsema, L.K. Verheij, and G. Comsa, Phys. Rev. Lett. 65, 733 (1990).
[11] M. Guillopé and B. Legrand, Surf. Sci. 215, 577 (1989); F. Cleri and V. Rosato, Phys. Rev. B 48, 22 (1993).
[12] F. Montalenti and R. Ferrando, Phys. Rev. B 59, 5881 (1999).
[13] B. Legrand and M. Guillopé, in Atomistic Simulation of Materials, edited by V. Vitek and D.J. Srolovitz (Plenum, New York, 1989), p. 361.
[14] V.B. Koutecký, L. Cespiva, P. Fantucci, and J. Koutecký, J. Chem. Phys. 98, 7981 (1993).
[15] S. Valkealahti and M. Manninen, Phys. Rev. B 57, 15533 (1998).
[16] D. Frenkel and B. Smit, Understanding Molecular Simulations (Academic Press, London, 1996).
[17] F. Baletto, C. Mottet, and R. Ferrando, Surf. Sci. 446, 31 (2000).
[18] D. Faken and H. Jónsson, Comput. Mater. Sci. 2, 279 (1994).
[19] C. Mottet, G. Tréglia, and B. Legrand, Surf. Sci. 383, L719 (1997).