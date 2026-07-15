EPJ manuscript No.
(will be inserted by the editor)

# Structure and Fragmentation in Colloidal Artificial Molecules and Nuclei

C.J. Olson Reichhardt, C. Reichhardt and A.R. Bishop

Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545

the date of receipt and acceptance should be inserted later

**Abstract.** Motivated by recent experiments on colloidal systems with competing attractive and repulsive interactions, we simulate a two-dimensional system of colloids with competing interactions that can undergo fragmentation. In the absence of any other confining potential, the colloids can form stable clusters depending on the strength of the short range attractive term. By suddenly changing the strength of one of the interaction terms we find a rich variety of fragmentation behavior which is affected by the existence of "magic" cluster numbers. Such soft matter systems can be used to construct artificial nuclei.

**PACS.** 82.70.Dd Colloids – 45.70.Qj Pattern formation – 05.70.Ln Nonequilibrium and irreversible thermodynamics

The issue of pattern stability has attracted considerable interest in a wide range of different areas. A commonly encountered mechanism for pattern formation is the competition between short-range attraction and long-range repulsion, which occurs in many systems including magnetic films, Langmuir monolayers, diblock copolymers [1], water-oil mixtures [2], and two-dimensional electron systems [3]. Similar types of pattern formation are expected to occur in dense nuclear matter, where they have been termed "pasta" phases. These phases may occur under conditions of stellar collapse [4] or in the crust of a neutron star [5]. Models of classically interacting particles with competing attractive and repulsive interactions have been used to study a variety of topics in nuclear matter. For example, if two nuclei collide, they temporarily form a high density state which then expands rapidly and can fracture in a complex manner [6]. Nuclear fragmentation processes in both two-dimensional [7] and three-dimensional [8] geometries cause the nucleus to be decomposed into clusters of all sizes through mechanisms ranging from evaporation to multifragmentation.

Models of small numbers of interacting particles, outside the thermodynamic limit, can be useful in understanding the structure and stability of naturally occurring clusters such as nuclei. Repulsively interacting particles can be forced to form clusters by confining the particles in a trap potential. A wide variety of systems exhibit this type of behavior, including electrons in quantum dots [9] or on the surface of liquid helium [10], vortices in superfluids [11], colloidal particles in circular traps [12], confined ferromagnetic particles [13], and charged dust particles in plasma traps [14]. The resulting structures have been studied extensively for a range of interaction types and trap types [15], and the details are sensitive to the nature of the trapping potential.

There has recently been growing activity in studying colloidal systems with competing long range repulsive and short attractive interactions, where various types of clusters are observed to form [16,17,18,19,20]. For instance, clusters and "artificial atoms" were created in an experimental system of rotating disks with no confining potential [21]. Other current experiments use combinations of entropic attractive forces with additional repulsive interactions to form clusters and study their decay [22], and long-range repulsion between colloids has been achieved in nonpolar solvents [23] and water-oil emulsions [24]. Analogies have been made between colloidal clusters and nuclear matter, leading to proposals for mimicking nuclear matter phenomena with a colloidal system [20]. Although there have been several colloidal studies of equilibrium cluster shapes that have identified magic numbers, to our knowledge the fragmentation of colloidal clusters has not been considered previously.

Here, we form clusters out of colloids that have a competing short-range attraction and a long-range Coulomb repulsion. We identify the stability line as a function of the strength of the short-range attraction for clusters of different sizes. When the attraction falls above this line, clusters exist in the absence of a confining potential. We then study different mechanisms for destabilizing the clusters, including thermal excitation and a sudden quench of the attractive term to a lower value. The latter process is inspired by the sudden expansion of an energized nucleus. The microscopic details of the decays can be accessed directly through our simulations. We find numerous decay modes depending on the cluster size and the quench depth. This system can serve as a model for understanding the

![](./images/867760075417059966_1.jpg)

Fig. 1. Structure of stable clusters for N=(a) 5, (b) 6, (c) 7, (d) 8, (e) 9, (f) 10, (g) 11, (h) 12, (i) 13, (j) 14, (k) 15, (l) 16, (m) 17, (n) 18, (o) 19, (p) 20, (q) 22, (r) 24, (s) 26, (t) 30.

complex interactions between charged fragments in a cluster that is breaking apart.

We simulate $N$ interacting colloids in a system with open boundary conditions. No confining force is applied to the colloids, which either remain in a cluster due to the colloid-colloid interactions when placed in a stable configuration, or scatter under Coulomb repulsion when placed in an unstable configuration. The overdamped equation of motion for colloid $i$ is $\eta d\mathbf{r}_i/dt = \mathbf{f}_i = \sum_{j\neq i}^N \mathbf{f}_{ij} + \mathbf{f}^T$, where $\eta$ is a phenomenological damping term. The colloid-colloid interaction $\mathbf{f}_{ij} = -\nabla U(r_{ij})\hat{\mathbf{r}}_{ij}$ for colloids separated by $\mathbf{r}_{ij} = \mathbf{r}_i - \mathbf{r}_j$ consists of a long-range Coulomb repulsion and a short-range exponential attraction:

$$
U(r)=1 / r-B \exp (-\kappa r). \tag{1}
$$

At small and large $r$ the repulsive Coulomb term dominates. The attractive interaction can be varied using the inverse screening length $\kappa$ and the parameter $B$. Here we fix $\kappa=1$. As we will demonstrate, clusters are stabilized above a critical value $B_c$ which is a function of $N$. The temperature is modeled as Langevin random kicks with the properties $\langle f^T(t)\rangle=0$ and $\langle f^T(t) f^T(t')\rangle=2 \eta k_B T \delta(t-t')$. To initialize the system, we set $B \geq B_c$ and allow the colloid positions to relax into a stationary state in the absence of temperature.

Due to the attractive component of the colloid-colloid interaction, stable clusters of colloids form even in the absence of a confining potential. We illustrate the stable clusters obtained for representative values of $N$ ranging from $N=5$ to $N=30$ in Fig. 1. In general, the colloids tend to form a small portion of a triangular lattice whenever possible, not unlike the hypothetical triangular structure assumed in the nuclear lattice model [25]. Since the underlying substrate is flat, geometrically necessary dislocations do not arise. Certain configurations which are the most lattice-like are also the most stable. These "magic" clusters include $N=7$, 12, and 19. Note that the magic cluster $N=12$ forms a nonhexagonal segment of a triangular lattice, so that it is highly stable even though it does not meet the proposed magic cluster criterion of $N=1+3 p(p-1)$ for integer $p$ [26]. The strong tendency toward triangular ordering is in contrast to systems of confined repulsively interacting particles, which tend to form ringlike structures instead. The smaller clusters shown in Fig. 1 resemble structures obtained in the cluster phase of either a periodic system [27] or one confined to a trap [28]. In these systems, interactions with neighboring clusters alter the shapes of larger clusters and can distort the triangular ordering. Thus, the configurations we observe here for larger unconfined clumps differ from those found in confined or periodic systems.

![](./images/867760075417059966_2.jpg)

Fig. 2. (a) Dots: Critical value $B_c$ for stable cluster formation versus cluster size N. Dotted line: Fit to $B_c=4.2+0.5 \ln (N)$. (b) $d B_c / d N$ for the same data. Negative values of $d B_c / d N$ indicate clusters that are more stable than neighboring cluster sizes.

To measure the stability of the configurations at different values of $N$, we perform a series of simulations in which $B$ is initially set to a value which gives a stable configuration, and is then abruptly lowered to a new value. We can identify when $B<B_c$ by observing the cluster break into two or more pieces. In Fig. 2(a) we plot $B_c$ versus $N$ through $N=80$. Configurations with $B \geq B_c$ are stable, while those with $B<B_c$ break apart. We find that $B_c$ increases approximately logarithmically with $N$, but that there are noticeable fluctuations which are particularly pronounced for small $N$. This is more easily seen in a plot of $d B_c / d N$, shown in Fig. 2(b). Magic clusters appear as pronounced dips in $d B_c / d N$. This general behavior is similar to that observed in artificial atoms, where a confining potential is present [29].

The structure of our clusters is predominantly triangular, but we can define the equivalent of outer and inner shells of colloids in the clusters. Unlike systems of particles confined in traps, our shells are not circular. The evolution of the shell structure is shown in Fig. 3(a), where the number of colloids $N_{shell}$ in each of the first four shells is plotted as a function of cluster size $N$. The second shell first appears at $N=7$, while the third shell arises for $N \geq 18$ and the fourth shell for $N \geq 29$. There is some tendency for the shells to favor an occupancy of $N_{shell}=6$, as seen by the presence of a step in $N_{shell}$ at $N_{shell}=6$ in Fig. 3(a) for all three of the shells. These results resemble

![](./images/867760075417059966_3.jpg)

measurements in dusty plasma systems [14]. We expect the shell structure shown here to be generally applicable to the type of colloid-colloid interaction we have assumed, and not to be parameter dependent.

We next consider how to destabilize our cluster structures so that they fragment. First we study thermal destabilization. Here, we fix $B$ at a stable value $B \geq B_{c}$, and simulate the system for a fixed number of time steps at each value of $T$, increasing $T$ until the thermal fluctuations break the cluster apart. We perform a series of runs at each value of $B$ to obtain an average melting temperature $T_{m}$ as a function of $B$. The results for five different cluster sizes are shown in Fig. 3(b). In each case, $T_{m}$ increases with $B$ since the attractive energy of the cluster is increasing. The rate of increase steepens as $N$ increases. The destabilization is triggered by the escape of at least one of the particles from the cluster, and can thus be regarded as a first passage process that becomes more likely as $T$ increases. In our overdamped system, it is difficult for a single particle to accumulate enough energy to escape the cluster at low temperatures, unlike the evaporation process that can occur in a massive system. This tends to stabilize the clusters at low temperatures.

The structures can also be destabilized by starting from a configuration with $B > B_{c}$, and then suddenly lowering $B$ to a value $B^{*} < B_{c}$. This type of process could occur after two nuclei collide and form a highly compressed but unstable structure, which subsequently fragments. In a colloidal system, sudden adjustments to the form of the interaction potential might be achieved through magnetic interactions, as was considered for purely repulsive particles in Ref. [30], or through electric interactions, as in Ref. [31]. We begin with configurations prepared slightly above $B_{c}$ and perform a series of quenches at small but finite $T$ to different values of $B^{*}$. We measure 20 quenches for each value of $B^{*}$ in order to accumulate statistics on the resulting fragment configurations. The clusters break into smaller clusters which are stable at $B^{*}$. As $B_{c} - B^{*}$ increases, the number of fragment clusters increases and the average size of a fragment cluster drops.

Different clusters show different types of decay modes. We notate these modes using $(j_{1}^{n_{j_{1}}}, j_{2}^{n_{j_{2}}}, ...j_{m}^{n_{j_{m}}})$, where $j_{i}$ is the number of colloids in clusters of type $i$, $n_{j_{i}}$ is the number of clusters of type $i$, and there are $m$ different cluster types. We also measure the average multiplicity of the decay at a given value of $B$, $\langle M(B)\rangle = \langle\sum_{i=1}^{m} n_{j_{m}}(B)\rangle$. We illustrate the probability $P$ of each decay mode for $N = 5$ as a function of $B^{*}$ in Fig. 4(a). Here we observe all six possible decay modes, and find two dominant decay modes: a breakup into one 1-particle cluster and two 2-particle clusters, denoted $(1^{1},2^{2})$, or complete disintegration into five 1-particle clusters, denoted $(1^{5})$. For the magic cluster $N = 7$ (not shown), we find only a single decay mode of complete disintegration, $(1^{7})$, unless $B^{*}$ is extremely close to $B_{c}$. The $N = 7$ state has such strong symmetry that the particles are not able to form subclumps as they break away from the main clump. Fig. 4(b) shows the decay modes for the magic cluster $N = 12$, illustrated in Fig. 5(a). The two dominant decay modes are both symmetric: a breakup into three 1-particle clusters and three 3-particle clusters $(1^{3},3^{3})$, illustrated in Fig. 5(b), and complete disintegration, $(1^{12})$, shown in Fig. 5(c). At $B^{*}$ values falling in the transition region between these two regimes for the case of a cluster held at finite temperature, numerous decay modes occur with no single mode dominating. In the case of an asymmetric, nonmagic cluster such as $N = 15$, plotted in Fig. 4(c), a series of decay modes appears. Images of representative decays are shown in Fig. 5(d-f). For $B^{*}$ close to $B_{c}$, the cluster breaks into two large asymmetric pieces, such as $(6^{1},9^{1})$ shown in Fig. 5(d). As $B^{*}$ is lowered, smaller pieces begin to appear, as in the case of $(2^{1},6^{1},7^{1})$ in Fig. 5(e). For $B^{*}$

![](./images/867760075417059966_4.jpg)

![](./images/867760075417059966_5.jpg)

Fig. 5. Images of decay. (a) $N=12$, initial configuration. (b) $N=12$, $B^*=5$, $(1^3,3^3)$. (c) $N=12$, $B^*=4.75$, $(1^{12})$. (d) $N=15$, $B^*=5.5$, $(6^1,9^1)$. (e) $N=15$, $B^*=5.35$, $(2^1,6^1,7^1)$. (f) $N=15$, $B^*=5.1$, $(1^4,2^4,3^1)$. (g) $N=19$, $B^*=5.55$, $(1^3,2^3,3^2,4^1)$. (h) $N=24$, $B^*=5.7$, $(1^2,10^1,12^1)$. (i) $N=26$, $B^*=5.6$, $(1^3,2^1,3^1,9^2)$.

considerably below $B_c$, the cluster disintegrates into many small pieces, as illustrated in Fig. 5(f) for $(1^4,2^4,3^1)$. Similar patterns occur for larger clusters. In Fig. 5(g), the magic cluster $N=19$ undergoes a nearly symmetric decay around a single central particle into the configuration $(1^3,2^3,3^2,4^1)$. A decay into two large pieces combined with two small fragments is shown in Fig. 5(h) for $N=24$. The relatively symmetric but elongated $N=26$ cluster is illustrated breaking into two symmetric large fragments with $N=9$ along with a handful of smaller fragments in Fig. 5(i).

The average multiplicity of the decay $\langle M\rangle$, or the average number of fragments into which the cluster breaks, increases as $B^*$ decreases. This is shown in Fig. 4(d) for $N=5,12$, and 15. The presence of two dominant decay modes for $N=5$ and 12 appears as steps in $\langle M\rangle$ as a function of $B^*$. The asymmetric cluster $N=15$ has a much more complex structure of decay modes, with none of the modes strongly dominant. This produces a smoother increase of $\langle M\rangle$ with decreasing $B^*$. The clusters reach the point of complete disintegration into individual fragments $(\langle M\rangle=N)$ at $B^*=4.78$ for $N=5$, $B^*=4.76$ for $N=12$, and $B^*=4.62$ for $N=15$.

In conclusion, motivated by recent experiments in colloidal systems with competing interactions, we study a system that can form stable clusters in the absence of any confining potential. We have shown that some cluster sizes are magic, and correspond to a defect-free segment of a triangular lattice. The strength of the short-range attractive term required to stabilize the clusters increases logarithmically with the cluster size. Clusters can be melted by increasing the temperature, or destabilized by suddenly quenching the attractive portion of the interaction to a lower value. We find a variety of decay modes in the latter case, with a structure that depends on the symmetry of the original cluster. These results suggest that colloidal systems of self-confined clusters where the interactions can be controlled may offer insights into the effects of interactions between charged fragments during decay processes such as multifragmentation for a larger class of systems including molecular clusters and nuclei.

We thank W.K. Kegel for useful comments and bringing to our attention some of the recent experimental work on colloidal systems with competing interactions. This work was supported by the U.S. Department of Energy under Contract No. W-7405-ENG-36.

## References

1. M. Seul, D. Andelman, Science 267, 476 (1995)
2. W.M. Gelbart, A. Ben Shaul, J. Phys. Chem. 100, 13169 (1996)
3. A.A. Koulakov, M.M. Fogler, B.I. Shklovskii, Phys. Rev. Lett. 76, 499 (1996); M.M. Fogler, A.A. Koulakov, B.I. Shklovskii, Phys. Rev. B 54, 1853 (1996); E. Fradkin, S.A. Kivelson, Phys. Rev. B 59, 8065 (1999); J. Schmalian, P.G. Wolynes, Phys. Rev. Lett. 85, 836 (2000)
4. D.G. Ravenhall, C.J. Pethick, J.R. Wilson, Phys. Rev. Lett. 50, 2066 (1983)
5. G. Watanabe, K. Sato, K. Yasuoka, T. Ebisuzaki, Phys. Rev. C 66, 012801(R) (2002); ibid. 69, 055805 (2004); G. Watanabe, T. Maruyama, K. Sato, K. Yasuoka, T. Ebisuzaki, Phys. Rev. Lett. 94, 031101 (2005)
6. D.H.E. Gross, Nucl. Phys. A 553, 175C (1993)
7. A. Strachan, C.O. Dorso, Phys. Rev. C 55, 775 (1997)
8. R.J. Lenk, V.R. Pandharipande, Phys. Rev. C 34, 177 (1986)
9. M.A. Reed, W.P. Kirk, Nanostructure Physics and Fabrication (Academic Press, Boston, 1989)
10. P. Leiderer, W. Ebner, V.B. Shilkin, Surf. Sci. 113, 105 (1987)
11. Y. Kondo, J.S. Korhonen, M. Krusius, V.V. Dmitriev, E.V. Thuneberg, G.E. Volovik, Phys. Rev. Lett. 68, 3331 (1992)
12. R. Bubeck, C. Bechinger, S. Neser, P. Leiderer, Phys. Rev. Lett. 82, 3364 (1999); Q.-H. Wei, C. Bechinger, D. Rudhardt, P. Leiderer, Phys. Rev. Lett. 81, 2606 (1998)
13. M. Golosovsky, Y. Saado, D. Davidov, Phys. Rev. E 65, 061405 (2002)
14. W.-T. Juan, Z.-H. Huang, J.-W. Hsu, Y.-J. Lai, L. I, Phys. Rev. E 58, R6947 (1998)
15. V.M. Bedanov, F.M. Peeters, Phys. Rev. B 49, 2667 (1994); V.A. Schweigert, F.M. Peeters, Phys. Rev. B 51, 7700 (1995); A.A. Koulakov, B.I. Shklovskii, Phys. Rev. B

57, 2352 (1998); M. Kong, B. Partoens, F.M. Peeters,
Phys. Rev. E 65, 046602 (2002)

16. J. Groenewold, W.K. Kegel, J. Phys. Chem. B 105, 11702
(2001)

17. A. Stradner, H. Sedgwick, F. Cardinaux, W.C.K. Poon,
S.U. Egelhaaf, P. Schurtenberger, Nature 432, 492 (2004)

18. S. Mossa, F. Sciortino, P. Tartaglia, E. Zaccarelli, Lang-
muir 20, 10756 (2004); F. Sciortino, S. Mossa, E. Zac-
carelli, P. Tartaglia, Phys. Rev. Lett. 93, 055701 (2004);
F. Sciortino, P. Tartaglia, E. Zaccarelli, J. Phys. Chem. B
109, 21942 (2005)

19. D. Pini, A. Parola, L. Reatto, J. Phys.: Condens. Matter
18, S2305 (2006); A. Imperio, L. Reatto, J. Chem. Phys.
124, 164712 (2006)

20. J. Groenewold, W.K. Kegel, J. Phys.: Condens. Matter 16,
S4877 (2004)

21. B.A. Grzyboswki, H.A. Stone, G.M. Whitesides, Nature
405, 1033 (2000); B.A. Grzybowski, X. Jiang, H.A. Stone,
G.M. Whitesides, Phys. Rev. E 64, 011603 (2001)

22. D.G. Grier, private communication.

23. M.F. Hsu, E.R. Dufresne, D.A. Weitz, Langmuir 21, 4881
(2005)

24. M.E. Leunissen, A. van Blaaderen,
A.D. Hollingsworth, M. Sullivan, P. Chaikin,
http://meetings.aps.org/Meeting/MAR06/Event/39085.

25. W. Bauer, D.R. Dean, U. Mosel, U. Post,
Phys. Lett. 150B, 53 (1985)

26. M. Saint Jean, C. Even, C. Guthmann, Europhys. Lett.
55, 45 (2001)

27. C.J. Olson Reichhardt, C. Reichhardt, I. Martin,
A.R. Bishop, Physica D 193, 303 (2004)

28. K. Nelissen, B. Partoens, F.M. Peeters, Phys. Rev. E 71,
066204 (2005)

29. J.J. Thomson, Philos. Mag. 7, 237 (1904); B. Partoens,
F.M. Peeters, J. Phys.: Condens. Matter 9, 5383 (1997)

30. K. Zahn, J.M. Mendez, G. Maret, Phys. Rev. Lett. 79, 175
(1997)

31. A. Yethiraj, A. van Blaaderen, Nature 421, 513 (2003)