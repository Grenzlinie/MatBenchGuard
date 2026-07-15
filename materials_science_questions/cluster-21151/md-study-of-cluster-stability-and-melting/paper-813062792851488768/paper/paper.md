# MOLECULAR DYNAMICS STUDY OF THE FORMATION OF ARGON CLUSTERS IN THE COMPRESSED GAS

E.E. POLYMEROPOULOS and J. BRICKMANN

Institut für Physikalische Chemie, Technische Hochschule Darmstadt, Petersenstrasse 20, D-6100 Darmstadt, Federal Republic of Germany

Received 5 July 1982

The formation of clusters (nucleation) in compressed argon gas is studied with the molecular dynamics simulation technique using two-body Lennard-Jones and three-body Axilrod-Teller potentials. The three-body interactions become increasingly important with decreasing temperature for cluster stability and cluster size distributions

## 1. Introduction

The formation of microclusters of atoms and molecules has found increasing interest among theoretical [1-12] and experimental [13-17] investigators. The problems involved can be directly related to many fields of chemistry and physics, such as nucleation, catalysis, interface phenomena, etc. Most recent theoretical and numerical studies have dealt with cluster formation in the liquid or solid state but little has been done with regard to the gas phase [2-5]. The reasons for this may partly be attributed to the fact that in the gas phase the frequency of dynamic cluster formation is small, and their lifetime (stability) very short, thus making very time-consuming calculations necessary in numerical simulations. However, the problem of obtaining a microcluster distribution in the gas phase is of great interest, especially in view of recent experiments [14-17] in which cluster distributions of sizes 2-100 atoms have been obtained in molecular-beam expansions.

In this letter we report on molecular dynamics simulations of cluster formation of argon atoms in the gas phase. Two different model approaches are studied: In model A only spherical two-body interactions described by a Lennard-Jones (12,6) potential are considered. In model B additional three-body interactions of Axilrod-Teller type are introduced. Cluster size distributions and lifetimes of the different clusters are calculated from quasi-equilibrium simulations in both cases at two temperatures.

## 2. Method of calculation

The molecular dynamics technique is well suited to simulating macroscopic properties of matter from microscopic interactions [18]. Since clusters of atoms form the bridge between microscopic and macroscopic particles, this method should also give reasonable results for the nucleation process from a microscopic point of view. We have chosen a system which was experimentally studied by Michels et al. [19] ($\rho = 93.04$ g/ℓ, $P = 49.95$ atm, $T = 273$ K). The simulation was performed with 108 argon atoms in a cubic box of length 4.254 nm with periodic boundary conditions for the particle motion.

The interaction of the argon atoms is either via a Lennard-Jones (LJ) potential (two-body interaction, model A)
$$V_{\mathrm{LJ}}=4 \epsilon\left[\left(\sigma / r_{i j}\right)^{12}-\left(\sigma / r_{i j}\right)^{6}\right],$$
where $\sigma = 3.405$ Å and $\epsilon = 119.4$ K, or via a combination of a LJ and a three-body Axilrod-Teller (AT) potential $V_{\text{AT}}$ (model B), with
$$V_{\mathrm{AT}}=\nu\left(1+\cos \theta_{1} \cos \theta_{2} \cos \theta_{3}\right) /\left(r_{i j} r_{i k} r_{j k}\right)^{3},$$
where $\nu = 73.2 × 10^{84}$ erg cm$^{9}$, $r_{ij}, r_{ik}, r_{jk}$ and $\theta_{1}, \theta_{2}, \theta_{3}$ the sides and interior angles of a triangle formed by three particles. It is well known [20] that the AT potential is repulsive for acute triangles and attractive for obtuse triangles and that the AT potential is of shorter range than the LJ potential.

We have performed calculations over 30000 integra- tion steps, each step being $20 \times 10^{-16} ~s$ The definition of a cluster is similar to that of Stillinger [21], i.e. a cluster is defined as such an aggregate in which each atom is not further away than a radius $R_{cl}=2.00 \sigma$ from at least one other atom in the aggregate. This means that our clusters could assume any possible geometry. The value of $2.00 \sigma$ corresponds to a relatively small value of the energy in the potential energy curve of argon but lies well within the attractive branch of thepotential. We have experimented with values of $R_{cl}$  ranging from $1.60 \sigma$ to $2.10 \sigma$ and have found that the density of small clusters up to 10 atoms is relatively in- sensitive to $R_{cl}$ . As expected, larger clusters are identi fied as one increases $R_{cl}$ .

The cluster identification procedure does not give any information about the lifetimes and stabilities of the aggregates. Short-lived encounter complexes cannot be distinguished from quasi-stable complexes consider- ing only the actual local arrangement at a given time. Therefore, we have imposed an additional criterion in identifying quasi-stable clusters. We call a cluster "quasi- stable" if the set of contributing atoms fulfils the cri- terion given above at least for a time interval of a fullperiod of oscillation of two argon atoms in an $Ar_{2}$  cluster under our experimental conditions

This ensures that we are counting real clusters in our distribution, and excludes short-lived complexes. The frequency for one oscillation for an internuclear separa- tion of $206 \sigma$ as calculated by means of the action angle variable technique is $0.73 \times 10^{12} ~s^{-1}$ . This period corresponds to $\approx 500$ integration steps.

At the beginning of each calculation the particles were placed on the lattice points of a fcc lattice, and were given a random velocity distribution. After an in- itial phase of thermalization (randomization of position and momenta) the system was adiabatically brought to the desired temperature by scaling the particle velocities. Subsequently, it was allowed to stabilize for a few hun- dred steps at the chosen temperature, and then the par- ticle coordinates were averaged every 100 integration steps over a time period of 30000 integration steps. The averaged coordinates were stored and were later used to determine the clusters being formed. Clusters that were built during the last 500 steps of the calculation were not considered to avoid misinformation concerning life- times of individual clusters. For the same reason care was taken to ensure that all clusters included in our dis- tributions had a complete life cycle within the 30000 steps of the calculation.

## 3. Results and discussion
Distributions of cluster density versus cluster size were obtained at temperatures of 273 and 150 K for systems whose particles interacted either with a LJ po- tential (model A) or a combination of a LJ and an AT potential (model B). We have computed two types of distributions. Firstly, distributions in which all clusters that appear during the simulation were counted regard- less of whether clusters composed of the same atoms appeared more than once at different times of the sim- ulation. Secondly, we have counted clusters that are made up of the same atoms only once, thus obtaining a distribution of all unique (different) clusters formed during the simulation. By dividing the number of clusters of each size of the first distribution by the correspond- ing number of the second distribution we obtain a mea- sure for the stability and average lifetime of the various cluster sizes.

In fig. 1 are shown the cluster distributions at 273(top) and 150 K (bottom) for all clusters that appear during the simulation regardless of whether the same cluster appears more than once at different times of the simulation. We have plotted cluster density versus cluster size. The density of clusters built only under the in- fluence of a LJ potential (model A: dark columns) is shown side-by-side with the density of clusters built under the influence of a combination of LJ and AT potentials (model B; light columns). A comparison of the cluster distributions at 273 and 150 K shows that at lower temperatures larger clusters are built than at higher temperatures, as expected. It is also obvious that the formation of these larger clusters at lower tempera- tures is favoured by the inclusion of three-body interac- tions (model B). Smaller clusters of sizes up to six argon atoms also appear with a larger rate at 150 K under the influence of two- and three-body interactions. There seems to be no definite pattern for the fomation of clusters of intermediate size at 150 K, and nothing defi- nite can be said about the influence of the interaction potential at 273 K. The reason for this observation at higher temperatures is certainly due to the fact that most clusters have a very short lifetime at 273 K and are de- stroyed by collisions with their neighbours. As the tem-

![](./images/813062792851488768_1.jpg)

Fig. 1. Cluster density versus size distribution at 273 (top) and 150 K (bottom) All cluster configurations being formed during the calculation are counted regardless of whether clusters made up of the same atoms appear more than once at different times. Dark columns represent clusters being built under the influence of a LJ potential (model A), and light columns represent clusters being built under the influence of a LJ plus AT potential (model B).

![](./images/813062792851488768_2.jpg)

Fig. 2. Cluster density versus cluster size distribution (bottom) and average cluster lifetimes (top) at 273 K. Cluster configurations being formed with the same atoms at different times are counted only once. Lifetimes are obtained by dividing the cluster density for each cluster size in fig. 1 by the corresponding cluster density in fig 2. Average cluster lifetimes equal to or less than one period of oscillation of an $Ar_2$ cluster (5.0 ps) are not shown in the figure. Dark and light columns represent clusters as in fig. 1.

![](./images/813062792851488768_3.jpg)

Fig. 3. Cluster density versus cluster size distribution (bottom) and cluster lifetimes as described in fig. 2 but at 150 K.

perature is lowered collisions become less frequent, and as a result, clusters have longer lifetimes.

The significance of three-body interactions can also be seen in figs. 2 and 3 where we have plotted the den- sity distributions of unique clusters (clusters made up of the same atoms being counted only once) versus cluster size (bottom), and the average lifetime of the various clusters (top) as obtained by dividing the dis- tribution of all possible clusters (fig. 1) by the corre- sponding distribution of unique clusters at 273 (fig. 2) and 150 K (fig. 3) Thus, clusters formed at 150 K have in general a longer average lifetime. In addition, from a comparison of the lifetimes at the two temperatures we can say that the inclusion of three-body interactions in the potential (model B) gives most clusters a longer life- time, and consequently, greater stability than in the case of model A.

The reason for the greater stability of a cluster under the influence of three-body interactions must be sought in the geometry of the clusters as well as in the opera- tional definition of clusters we have used. Our defini- tion, in contrast, for example, to a definition that con- siders the local density of atoms in the unit cell, allows all possible geometries. This, of course, favours the for- mation of long linear structures that are stable if three- body interactions are included in the potential. It is well known [22,23] that the inclusion of triple-dipole interactions gives the correct fcc packing for rare-gas crystals. Our results indicate that such a stabilizing ef- fect already occurs in the gas phase, showing the signifi- cace of three-body interactions in the formation of rare- gas clusters.

The investigations described above show that the molecular dynamics simulation technique is well suited for studying nucleation of inert atoms in the gas phase. In particular, the influence of different interaction po- tentials can be analyzed. Further calculations, which are in progress, may shed light on the behaviour of gas clusters in expanding beams which are presently experi- mentally studied by various groups.

### Acknowledgement
One of the authors (EEP) would like to thank Mr. W. Fischer for many helpful discussions and suggestions. This research was supported by the Deutsche Forschungs- gemeinschaft, Bonn, and the Fonds der Chemischen Industcrie, Frankfurt/Main.

### References
[1] J.K. Lee, J.A. Barker and F.F. Abraham, J. Chem. Phys. 58 (1973) 3166.

[2] D.J. McGinty, J. Chem. Phys. 55 (1971) 580, 58 (1973)4733.
[3] H.W. Harrison, W.C. Schieve and J.S. Turner, J. Chem. Phys. 56 (1972) 710.
[4] W.C. Schueve and H.W. Harrison, J. Chem. Phys. 61 (1974)700.
[5] M. Synek, W.C. Schieve and H.W. Harrison, J. Chem. Phys.67 (1977) 2916.
[6] C.L. Briant and J.J. Burton, J. Chem. Phys. 63 (1975)2045.
[7] M. Rao, B.J. Berne and M.H. Kalos, J. Chem. Phys. 68(1978) 1325.
[8] M.R. Hoare, Advan. Chem. Phys. 40 (1979) 49.
[9] T.M. Cooper and R.B. Birge, J. Chem. Phys. 74 (1981)5669.
10] J.W. Brady, J.D. Doll and D.L. Thompson in Intermo- lecular Forces, Proceedings of the 14th Jerusalem Sympo- sium on Quantum Chemistry and Quantum Biology, ed. B. Pullman (Reidel, Dordrecht, 1981) p. 213.
11] R.D. Etters, R. Danilowicz and J. Kaelberer, J. Chem. Phys. 67 (1977) 4145.
12] R.D. Etters and R. Danilowicz, J. Chem. Phys. 71 (1979)4767.

[13] P.M. Dehmer and S.T. Pratt, J. Chem. Phys. 76 (1982)843.
[14] O. Echt, K. Sattler, and E. Recknagel, Phys. Rev. Letters47 (1981) 1121.
[15] O. Echt, E. Recknagel and K. Sattler, Proceedings of the8th International Symposium on Molecular Beams, Cannes(1981) p.144.
[16] O. Echt, E. Recknagel adn K. Sattler, Europhysics Con- ference Abstracts, Vol 5A (1981) p. 420.
[17] O. Echt, A. Reyes-Flotte, M. Knapp, K. Sattler and E. Recknagel, Ber. Bunsenges. Physik Chem., to be published.
[18] P. Lykos, ed , Computer Modelling of Matter, ACS Sym- posium Series 86 (1978).
[19] A. Michels, H. Wyker and H.K. Wyker, Physica 15 (1949)627.
[20] J.M. Haile, in Computer Modelling of Matter, ed. P. Lykos, ACS Symposium Series 86 (1978) p. 172.
[21] F. Stillunger, J. Chem. Phys. 38 (1963) 1486.
[22] L. Jansen and E. Lombardi, Discussions Faraday Soc. 40(1965)78.
[23] T. Halicioglu and P I. White, Surface Sci. 106 (1981) 45.