# FIRST-ORDER TRANSITIONS IN PERCOLATION MODELS*

Fulvio PERUGGI

GNSM and CISM, Dipartimento di Fisica dell'Università di Napoli,
Mostra d'Oltremare, pad. 19, 80125 Napoli, Italy

Received 2 May 1986

We describe the analytic solution of a Potts-correlated-site/random-bond percolation model which exhibits a first-order percolative transition at the Potts critical point. The subject is discussed in connection with the droplet theory in lattice spin models.

The relevance of percolation models in a very large number of physical contexts is extensively discussed in many review articles $^{1-4}$ ). In very general terms, any percolation model is characterized by the spatial distribution of multi-state elementary objects, and the definition of "connectivity" between them. A cluster is a maximal aggregate of connected objects: the features of the model are usually studied by looking for (a) the existence of percolation point(s) where infinite clusters appear in the system, and (b) the behaviour of percolative functions describing relevant properties of the clusters. In random percolation models the appearance of infinite clusters, and the behaviour of the percolative functions like the thermal functions in a second-order phase transition, are due to purely "geometric" effects. Switching-on proper interactions, one can study the percolative behaviour in the largest scenario of cooperative phenomena. In such a context, phase transitions are sometimes described in terms of the so-called "droplet picture". In the droplet model of Fisher $^{5}$ ) one postulates that the free energy of a system can be expressed in terms of non-interacting droplets, and assumes that the asymptotic form of the expected number of droplets of given size, and the behaviour of their surface tension, are such that the droplets diverge at the critical point with prescribed exponents. In the droplet picture of a given model one adjusts the previous parameters in such a way that the droplets diverge at the critical point with the same exponents as the thermal functions of the system. Also the decay of a

* Supported by MPI and CNR.

0378-4371/87/$03.50 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

metastable phase into the stable one is described in terms of droplets and their growth or shrinkage in the context of classical nucleation theory (for a review about this topic see ref. 6). However, neither the droplet picture nor classical nucleation theory gives explicit prescriptions to identify the aggregates which play the role of the droplets in a given system.

A successful attempt to unify the percolation and droplet pictures for spin models on lattices was done recently $^{7-10}$ ). To be concrete about the related problems, let us consider the Ising-correlated-site percolation model on a lattice, where two nearest-neighbour sites are "connected" if they are in the same spin state, and one focuses on one species of clusters (e.g. those of up spins). Rigorous results $^{11-14}$ ), series expansions techniques $^{15}$ ), and Monte Carlo simulations $^{16}$ ) showed that at zero external field the Ising critical point and the percolation point are located, respectively, at temperatures $\theta_{c}, \theta_{p}$ such that $\theta_{c}<\theta_{p}$ in three or more dimensions (see e.g. fig. 1a, b), and $\theta_{c}=\theta_{p}$ in two dimensions. In the last case, however, the mean size and the connectedness length ( $\equiv$ mean diameter) of finite clusters diverge with critical exponents $\gamma_{p}$, $\nu_{p}$, respectively, greater than $\gamma, \nu$, i.e. those which characterize the susceptibili ty and the correlation length. Thus it was recognized that clusters of correlated- site percolation are too large to be the droplets. The following minimal requirements should be satisfied for an acceptable identification of clusters and droplets. (i) The system must split into single-site droplets (clusters) in the infinite-temperature limit, since no correlations are present; (ii) one must find $\gamma=\gamma_{p}$ and $\nu=\nu_{p}$ at $\theta_{c}=\theta_{p}$, i.e. good divergence at the right temperature; (iii) only one droplet (cluster) must be present at zero temperature, since the system is completely correlated. To satisfy properties (i)-(iii) one can intro- duce correlated-site/random-bond percolation models, where also the bonds are allowed to take up two states ("active" and "passive") which do not affect, and are not affected by, spin state distributions. In such models one says that two nearest-neighbour sites are connected if they are in the same spin state and the bond between them is active. Note that the active bond probability $p_{b}$ must be 0 because of property (i) and 1 because of property (iii). In other terms no constant $p_{b}$ is able to satisfy contemporaneously the requirements (i)-(iii) (see fig. 1b, c), and one needs a general recipe to establish the functional dependence of $p_{b}$ by the temperature. In the case of ferromagnetic interactions* such a relation was found explicitly for the Ising model $^{7}$ ) (see its effects in fig. 1d) and the Potts model $^{8}$ ) by means of lattice-independent proofs, and was successfully verified on two-dimensional lattices with the Migdal-Kadanoff renormalization group.

* The criticality of systems characterized by antiferromagnetic interactions, which will not be considered here, is better described by $\mathscr{A} \mathscr{B}$-percolation models and the associated $\mathscr{A} \mathscr{B}$-droplets (see refs. 9, 10).

Let $\nu_i=1,2,\dots,q$ be spin variables associated to the sites of a lattice of dimensionality $d$, and consider the Potts Hamiltonian

$$
-\beta \mathscr{H}=K \sum_{\langle i j\rangle} \delta_{\nu_{i} \nu_{j}}+H \sum_{i} \delta_{\nu_{i}},\tag{1}
$$

where the first sum runs over the bonds of the lattice, and Krönecker delta functions are used. In such a system the previous cluster characterization is unchanged, but one has a polychromatic percolation model since $q$ distinct species (≡ colours) of clusters appear*. Coniglio and Peruggi$^8$) showed that for

![](./images/812447804382248960_1.jpg)

* Formal definitions of the characteristic functions of polychromatic correlated-site/random-bond percolation models on general lattices can be found in ref. 17.

![](./images/812447804382248960_2.jpg)

Fig. 1. Thermal functions (a) and percolative functions (b, c, d) for the zero-field Ising model on a Bethe lattice of coordination number $\sigma+1=3$. The free energy and the mean number of finite clusters are represented by solid lines; the order parameter and the percolation probability are represented by broken lines; the susceptibility and the mean size of finite clusters are represented by dotted lines. The values of the critical temperature $\theta_{\mathrm{c}}$ and the percolative temperature $\theta_{\mathrm{p}}$ are marked. The active bond concentration is $p_{\mathrm{b}}=1$ in (b), $p_{\mathrm{b}}=0.8$ in (c), $p_{\mathrm{b}}=1-\theta$ in (d).

every $d$ and $q$ the droplets are identified by the choice

$$
p_{\mathrm{b}}=1-\mathrm{e}^{-K} \equiv 1-\theta . \tag{2}
$$

Note that this relation automatically satisfies properties (i) and (iii), so that one has to verify only property (ii). To do this for $d \geqslant 3$ we consider

polychromatic Potts-correlated-site/random-bond percolation models on a Bethe lattice of coordination number $\sigma+1$. The main features of such a choice are the following. First, the system belongs to a class of models for which a method of solution already exists $^{17}$ ), and it is known that exact results on Bethe lattices are good approximations for high-dimensional lattices. Second, in the above-mentioned approach, bond properties and site properties split: the former are treated explicitly, so that the involved Hamiltonian formulation of the model (s-state Potts spins diluted by $q$-state Potts spins, see ref. 8) required by renormalization group techniques need not be considered; the latter give no problem, since the exact solution of the Potts model (1) is well-known $^{18,19}$ ).

In the following, without loss of generality, we will focus on "black" clusters made of spin state 1 in the "white" background formed by all other colours. Furthermore, since we are mainly interested in the zero-field properties of the system, we will consider it in the $H \rightarrow 0^{+}$limit, which, among the $q$ ordered phases that appear below the critical temperature

$$
\theta_{\mathrm{c}}=\left[(q-1)^{(\sigma-1) /(\sigma+1)}-1\right] /(q-2),
$$

selects the one where the concentration $p_{1}$ of the spin state 1 is greater than those of the other spin states. We remark that the transition at $\theta_{\mathrm{c}}$ is of second-order for $q=2$, and of first-order for $q>2$. For the solution of the present percolation problem we need, as functions of the temperature, the values of $p_{1}$ and those of $p_{11}$, i.e. the conditional probability that a site is in the spin state 1, given that a specified adjacent site is in the spin state 1. These probabilities, as well as the thermal functions of interest (i.e. the free energy $\beta \mathscr{F}$, the order parameter $m \equiv\left(q p_{1}-1\right) /(q-1)$, the susceptibility $\chi=\partial p_{1} / \partial H$, and the pair correlation $\mathscr{G}_{i j}$ ) are calculated as shown in refs. 18, 19. The percolative functions (i.e. the mean number of finite clusters $N$, the percolation probability $P$, the mean size of finite clusters $S$, and the pair connectedness $P_{i j}$ ) are given by $^{17}$ )

$$
\begin{aligned}
& N=p_{1} Q^{\sigma+1}-\frac{\sigma+1}{2} p_{1} p_{\mathrm{b}} p_{11} Q^{2 \sigma}, \\
& P=1-Q^{\sigma+1}, \\
& S=\frac{1+p_{\mathrm{b}} p_{11} Q^{\sigma-1}}{1-\sigma p_{\mathrm{b}} p_{11} Q^{\sigma-1}}, \\
& P_{i j}=p_{1}\left(p_{\mathrm{b}} p_{11}\right)^{l} Q^{(l-1)(\sigma-1)+2 \sigma},
\end{aligned}
$$

where $l$ is the number of bonds between the sites $i$ and $j$, and the percolation

threshold is characterized by

$$\sigma p_{\mathrm{b}} p_{11}=1.\tag{5}$$

The term $Q$ is equal to 1 below and at the threshold, and is the solution $0\leqslant Q<1$ of the equation

$$Q=1-p_{\mathrm{b}} p_{11}+p_{\mathrm{b}} p_{11} Q^{\sigma}\tag{6}$$

otherwise. All the previously mentioned extensive thermal and percolative functions are calculated per site of the lattice.

As one expects, relation (5) implies that infinite black clusters do not exist when the active bond concentration is lower than the random-bond percolation threshold $p_{\mathrm{bc}}=1 / \sigma$, no matter how the spin states are distributed. The correlations in such a distribution are taken into account by the factor $p_{11}$. From the results of refs. 18,19 it follows that $p_{11}$ is a decreasing function of $\theta$ which in the ordered phase goes from the value 1 at $\theta=0$ (perfectly ordered spins) to the value $[1+(q-2) \theta_{\mathrm{c}}] /[1+(q-1) \theta_{\mathrm{c}}]$ at $\theta_{\mathrm{c}}$, and in the disordered phase goes from the value $1 /[1+(q-1) \theta_{\mathrm{c}}]$ at $\theta_{\mathrm{c}}$ to the value $1 / q$ at $\theta=1$ (randomly distributed spins). This behaviour implies that the relation $\sigma p_{\mathrm{b}} p_{11}>$ $1\left(\sigma p_{\mathrm{b}} p_{11}<1\right)$ is satisfied in the ordered (disordered) phase for every active bond concentration such that $1-\theta_{\mathrm{c}}<p_{\mathrm{b}} \leqslant 1\left(0 \leqslant p_{\mathrm{b}}<1-\theta_{\mathrm{c}}\right)$. For $q>2$ these inequalities hold for $p_{\mathrm{b}}=1-\theta_{\mathrm{c}}$, too; while for $q=2$ and $p_{\mathrm{b}}=1-\theta_{\mathrm{c}}$ relation (5) is satisfied at $\theta_{\mathrm{c}}$. Thus we deduce that the droplet dilution (2) sets $\theta_{\mathrm{p}}=\theta_{\mathrm{c}}$ for every $q \geqslant 2$. The percolative transition is second-order for $q=2$; this character is completely deleted for $q>2$, where we have a first-order transition with a jump of the percolation probability from 0 to a finite value, and no divergence of the mean cluster size. The above-mentioned property (ii) is always satisfied, with mean-field exponents for $q=2$.

The previous argument is illustrated in fig. 1 for the case $q=2$, i.e. the Ising model and the associated percolation model. Note that the percolative func- tions are affected by the thermal transition and exhibit cusps at the critical temperature $\theta_{\mathrm{c}}$ (fig. $1 \mathrm{~b}, \mathrm{c}$ ). For $p_{\mathrm{b}}=1$ the conditions for percolation are so favourable that infinite clusters are present at any temperature for every coordination number*. The percolation threshold can be seen only for $\sigma=2$ : it is located at infinite temperature, where one recovers the random-site percola- tion problem (fig. 1b). The percolative temperature decreases when bond dilution is introduced (fig. 1c); in particular, with the droplet dilution (2) we

* The case $\sigma=1$, i.e. the linear chain, is excluded from our considerations because we are interested only in $d=\infty$ lattices.

find $\theta_{\mathrm{p}}=(\sigma-1) /(\sigma+1)=\theta_{\mathrm{c}}$ (fig. 1d). The characteristic functions of the $q=3$ Potts model and the associated percolation model are shown in fig. 2 for a Bethe lattice with $\sigma=5$, which simulates the cubic lattice. Now the thermal transition occurring at $\theta_{\mathrm{c}}$ is first-order and causes discontinuities of the percolative functions. For $p_{\mathrm{b}}=1$ the present system always percolates (fig. $2 \mathrm{~b}$ ), so that the usual second-order-like transition of percolation appears only for small enough $p_{\mathrm{b}}$ (fig. $2 \mathrm{c}$ ). The effects of the droplet dilution are shown in fig. $2 \mathrm{~d}$ : note that all the percolative functions are discontinuous at $\theta_{\mathrm{p}}=\theta_{\mathrm{c}}$, while, among the thermal functions, only the order parameter exhibits a jump. We emphasize that the plots of fig. $2 \mathrm{~b}$ are not general: there are values of $\sigma>1$

![](./images/812447804382248960_3.jpg)

![](./images/812447804382248960_4.jpg)

Fig. 2. Thermal functions (a) and percolative functions (b, c, d) for the zero-field $q=3$ Potts model on a Bethe lattice with $\sigma=5$. The same code as in fig. 1 is used. The active bond concentration is $p_{\mathrm{b}}=1$ in (b), $p_{\mathrm{b}}=0.5$ in (c), $p_{\mathrm{b}}=1-\theta$ in (d). Note that, when the percolative temperature is found in the disordered phase, it is given by $\theta_{\mathrm{p}}=(\sigma p_{\mathrm{b}}-1)/(q-1)$: $\theta_{\mathrm{p}}>1$ means that the system always percolates, as in (a).

and $q>2$ such that the percolative temperature for $p_{\mathrm{b}}=1$ can be found in the range $\theta_{\mathrm{c}} \leqslant \theta_{\mathrm{p}}<1$. In all these cases the dilution (2) leads to graphs similar to those shown in fig. 2d. Evidence of the previous droplet behaviour was already found on two-dimensional lattices $^{8)}$, although the first-order thermal and percolative transitions were not detected explicitly, due to the limitations of the Migdal-Kadanoff renormalization procedure used in such a case.

Up to now we have studied the droplet picture of the Potts model: to establish connections with classical nucleation theory we consider the meta- stable phases of the system. It is known $^{18.19}$ ) that for $q>2$ around the critical temperature (3) there are a supercooled disordered phase and a superheated ordered phase bounded respectively by spinodal temperatures $\theta_{1}<\theta_{c}$ and $\theta_{2}>\theta_{c}$ . At these points the metastable phase is characterized by divergence of the susceptibility and abrupt jump of the order parameter to the value which pertains to the stable phase. One expects that the droplet dilution (2) will give a corresponding divergence of the mean cluster size. At the temperature $\theta_{1}=(\sigma-1) /(\sigma+q-1)$ this indeed is true for every $\sigma>1$ and $q>2$ : an example is shown in fig. $3 a, b$ . On the other hand, in the metastable phase at $\theta_{2}$ one finds always $\sigma p_{b} p_{11}>1$ when $p_{b}$ is given by (2), i.e. the system is well above the threshold and the mean size of finite clusters does not diverge at that

![](./images/812447804382248960_5.jpg)

![](./images/812447804382248960_6.jpg)

Fig. 3. The same system and code as in fig. 2 are considered. In (a, b) we show the values that the thermal and percolative functions assume in the metastable supercooled disordered phase which appears in the range $\theta_{1} \leqslant \theta<\theta_{c}$. In (c, d) we show the values that the thermal and percolative functions assume in the metastable superheated ordered phase which appears in the range $\theta_{c}<\theta \leqslant \theta_{2}$. The active bond concentration is $p_{b}=1-\theta$ both in (b) and (d). Note that the temperature scale, the susceptibility scale, and the mean cluster size scale are conveniently expanded/compressed.

point (see e.g. fig. 3c, d). To explain this failure of Coniglio and Peruggi's prescription we remark that there are reasons which suggest that the symmetry breakdown among the spin states invalidates their proof in the ordered phases. This point of view is also supported by the fact that in the Ising model one has distinct critical exponents for percolative and thermal functions when $\theta \to \theta_{c}^{-}$ (e.g. we find $\gamma^{\prime}=1$ and $\gamma_{p}^{\prime}=1 / 2)^{*}$.

* Note that only the $\theta \to \theta_{c}^{+}$ critical exponents are considered in our statement of property (ii).

In conclusion, we have solved and studied a polychromatic Potts-correlated-site/random-bond percolation model on Bethe lattices. The number of spin states and the density of active bonds in the system govern the percolative transition, which can be second-order-like or first-order-like. We have dis- cussed in detail the connection of this problem with droplet theory and classical nucleation theory. The present high-dimensional solution is the natural com- pletion of previous two-dimensional results, and gives a clear-cut picture of droplets' properties.

## References

1) J.W. Essam, in: Phase Transitions and Critical Phenomena, C. Domb and M.S. Green, eds. (Academic, New York, 1972) vol. 2.
2) D. Stauffer, Phys. Rep. 54 (1979) 1.
3) J.W. Essam, Rep. Prog. Phys. 43 (1980) 833.
4) Percolation structures and processes, in: Annals of the Israel Physical Society, G. Deutscher, R. Zallen and J. Adler, eds. (Adam Hilger, Bristol, 1983) vol. 5.
5) M.E. Fisher, Physics 3 (1967) 255.
6) J.D. Gunton, M. San Miguel and P.S. Sahni, in: Phase Transitions and Critical Phenomana, C. Domb and J.L. Lebowitz, eds. (Academic, New York, 1983) vol. 8.
7) A. Coniglio and W. Klein, J. Phys. A: Math. Gen. 12 (1980) 2775.
8) A. Coniglio and F. Peruggi, J. Phys. A: Math. Gen. 15 (1982) 1873.
9) A. Coniglio, F. di Liberto, G. Monroy and F. Peruggi, Phys. Lett. A 87 (1982) 189.
10) F. Peruggi, F. di Liberto and G. Monroy, Physica 123A (1984) 175.
11) A. Coniglio, J. Phys. A: Math. Gen. 8 (1975) 1773.
12) A. Coniglio, Phys. Rev. B 13 (1976) 2194.
13) A. Coniglio, C.R. Nappi, F. Peruggi and L. Russo, Commun. Math. Phys. 51 (1976) 315.
14) A. Coniglio, C.R. Nappi, F. Peruggi and L. Russo, J. Phys. A: Math. Gen. 10 (1977) 205.
15) M.F. Sikes and D.S. Gaunt, J. Phys. A: Math. Gen. 9 (1976) 2131.
16) H. Müller-Krumbhaar, Phys. Lett. A 50 (1974) 27.
17) F. Peruggi, J. Math. Phys. 25 (1984) 3303 and 3316.
18) F. Peruggi, F. di Liberto and G. Monroy, J. Phys. A: Math. Gen. 16 (1983) 811.
19) F. Peruggi, F. di Liberto and G. Monroy, Physica 141A (1987) 151, this volume.