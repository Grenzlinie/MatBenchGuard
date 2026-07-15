# Relaxation in DLA with surface tension

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1990 J. Phys. A: Math. Gen. 23 3271

(http://iopscience.iop.org/0305-4470/23/14/024)

View [the table of contents for this issue](the table of contents for this issue), or go to the [journal homepage](journal homepage) for more

Download details:

IP Address: 139.184.14.159
This content was downloaded on 15/08/2015 at 23:27

Please note that [terms and conditions apply](terms and conditions apply).

J. Phys. A: Math. Gen. 23 (1990) 3271-3278. Printed in the UK

# Relaxation in DLA with surface tension

M A Novotny†, R Tao‡ and D P Landau§

† Supercomputer Computations Research Institute B-186, Florida State University, Tallahassee, Florida 32306-4052, USA
‡ Department of Physics, Southern Illinois University, Carbondale, Illinois 62901, USA
§ Center for Simulational Physics and Department of Physics, University of Georgia, Athens, Georgia 30602, USA

Received 5 March 1990

Abstract. We have carried out a Monte Carlo simulation on DLA clusters, grown with the inclusion of varying amounts of surface tension, which are allowed to relax, or equilibrate, through single particle hops to states of lower energy. We find that the DLA cluster rapidly breaks up into a number of disconnected, smaller clusters but that the fractal dimension of the system is essentially unchanged. In contrast, the energy of the system relaxes to a much lower value via multi-exponential processes with quite different time constants. These results model experiments involving the injection of air into epoxy.

## 1. Introduction

During the past few years there has been tremendous interest in understanding growth with a great emphasis upon irreversible processes [1]. One of the the most important models which has been studied extensively is the DLA (diffusion-limited aggregation) model which was introduced by Witten and Sander [2]. In this model a particle executes a random walk until it strikes a particle on the aggregate (which starts with a single seed particle), where it sticks to the aggregate at the point of contact. A new walker is then released from infinity, and the process repeats itself. The aggregate which is grown by this process is not compact but has a tenuous appearance and is fractal. Although the bonds which hold the particles together may be considered to have a certain energy, the geometry of the problem is the sole determining factor. Many particles are connected to only one or two near neighbours and from the point of view of energetics and statistical mechanics are in a non-equilibrium state. This process, and a wide range of variations of DLA growth, have been used as a starting point for understanding different types of aggregate formation [1]. Surface tension has been included in DLA simulations both by varying the probability that a particle sticks to the aggregate [3,4] and by incorporating interactions between the random walker and the particles on the aggregate [5]. In order to 'smooth' the aggregates, in some simulations the particles have been allowed a one-time hopping to nearby positions of lower energy after they first make contact with the cluster [3-5]. These variations of the DLA model have been shown to be relevant to fluid-fluid displacement in a porous media, since both problems reduce to the Laplace equation with similar boundary conditions [3-8]. This one-time particle hopping allows the cluster to relax, thus lowering its energy, but it does not change the fractal nature of the cluster [5]. In this paper we explicitly study the effect of hopping on DLA clusters which are no

0305-4470/90/143271 + 08$03.50 © 1990 IOP Publishing Ltd

longer growing. Our results will be discussed in terms of the implication which they have for simulation studies as well as for experiments which have been carried out for air injected into epoxy. This work is related to previous studies of DLA models which allow disaggregation processes [9,10], and to recent equilibrium models for solidification and growth [11]. However, in our model we separate the problem into two disjoint parts; i.e. we first grow the DLA aggregate (with or without surface tension), and then we allow this aggregate to approach thermal equilibrium.

## 2. Method

DLA clusters were generated using standard techniques with the added feature that surface tension was included by introducing a curvature-dependent interaction between the random walker and particles on the aggregate [5]. In this way clusters of up to $5 \times 10^{4}$ particles were grown on a square lattice. One cluster was chosen for each size and value of surface tension and then allowed to 'relax' in the following way: a site on the perimeter of the cluster is randomly chosen and allowed to attempt to move to another site within a predefined radius of its original position. If the energy of the particle is lower in the new site than in the old site the particle 'hops' to this new site; if the energy is the same in the new and the old site the particle 'hops' with 50% probability; otherwise it remains in its original position. This process continues for a predetermined number of 'trial hops', or Monte Carlo steps (MCS). This type of Monte Carlo procedure is often referred to as using zero-temperature Kawasaki dynamics. In our simulations, we have used an attractive energy associated with nearest-neighbour sites on the square lattice. The equilibration process acts on a lattice gas model which has nearest-neighbour attractive interactions. Starting from the non-equilibrium state of the fractal, the system is allowed to relax towards equilibrium via the zero- temperature Kawasaki dynamics described above. Various properties of the system are computed at regular intervals and the information is stored. This process is then repeated using a different sequence of random numbers and the values are then averaged over the different relaxation sequences. In all phases of the simulation a Tausworthe random number generator was used.

## 3. Results

We found that visual inspection of the system at various times during the simulation was useful. In figure 1 we show the initial DLA cluster plus two different relaxed clusters (with different 'hopping radii') for a cluster grown without surface tension and for one grown with surface tension. The relaxed clusters bear a strong resemblance to the patterns which are formed when air is injected into epoxy in a two dimensional random porous medium which is then allowed to harden. The initial stages of injection are described in [12]. However, here we are interested in phenomena at later times when the epoxy has hardened and the fingers of air are found to have evolved into bubbles [13]. The changes which occur as a result of relaxation are by no means instantaneous and, as seen in figure 2, the energy relaxes in a multistep process in which there is a pronounced, rapid short-time exponential decay followed by much slower exponential decays to its final value. The initial decay seems to be roughly independent of the hopping radius used, but the amplitude associated with at least the long-time decay

![](./images/811975233052344321_1.jpg)

Figure 1. Two different DLA aggregates are shown, with a surface tension of zero (a) and with a surface tension of 0.1 (d), grown as described in [5]. The aggregates in (a) and (d) were then allowed to relax toward equilibrium using $10^6$ MCS as described in the text. Pictures (b) and (e) correspond respectively to the equilibrated aggregates (a) and (d) with nearest and next-nearest neighbour hopping (hopping to the 8 nearest lattice plaquettes, or hopping with a radius of $\sqrt{2}$). Pictures (c) and (f) correspond respectively to the equilibrated aggregates (a) and (d) with hopping to the nearest 36 lattice plaquettes (a hopping radius of $\sqrt{10}$). All aggregates contain $5 \times 10^3$ particles, and are shown plotted with the same scale (the lattice size is about $125 \times 125$).

![](./images/811975233052344321_2.jpg)

Figure 2. The relaxation of the energy is shown as a function of the time in units of Mcs/particle. Four different hopping radii are shown, the numbers correspond to the number of lattice plaquettes that a particle is allowed to hop to. The curves are averages over 100 different random number sequences for an aggregate of $10^4$ particles grown with zero surface tension.

decreases rapidly as the hopping radius is decreased. The time constant for the long-time decay appears to be similar for different hopping radii, but we cannot exclude the possibility that it actually varies slightly.

We have also examined the dependence of the final, relaxed energy on the size of the initial cluster. The results, shown in figure 3, indicate that even for an initial DLA cluster composed of 2500 particles, the final energy is dominated by the statistics rather than by the finite number of particles. Several other DLA clusters of 2500 particles were grown and the initial energies of these clusters were found to vary by 1-2% and, when relaxed, the system energies were correlated with the initial energies. We therefore do not expect any significant difference in our results to appear if we were to repeat this calculation using initial clusters which were larger by only a modest amount compared with the largest ones considered here, and substantially larger clusters would require prohibitive amounts of computer time.

We have also examined the time dependence of the total number of clusters in the system, see figure 4. The number of clusters increases with a much faster timescale than that appropriate for the energy decay. A novel feature is that the number of clusters overshoots its final value, as demonstrated in the insert in figure 4. We also calculated the effective fractal dimension of the aggregates as a function of equilibration time. The effective fractal dimension, $D_{\mathrm{f}}^{\text {eff }}$, is defined by $N \propto r^{D_{\mathrm{f}}^{\text {eff }}}$, with $N$ the number of particles within a distance $r$ from the centre of mass of the system. As illustrated in figure 5, the fractal dimension changes very little with equilibration. In fact, for different aggregates or for different random number sequences used to equilibrate the same aggregate, the slight changes either increased or decreased $D_{\mathrm{f}}^{\text {eff }}$. Thus, although some of the properties of the cluster do change during the equilibration process, the fractal dimension apparently does not care about the details within a very broad range

![](./images/811975233052344321_3.jpg)

Figure 3. The energy of the equilibrated aggregates is shown as a function of $1/N$, with $N$ the number of particles in the aggregate. The number of different sequences of random numbers averaged over for each aggregate size is: ($N$, number); (1000, 1000); (2500, 100), (10 000, 100), (50 000, 1). In each case the values are shown for a single initial aggregate, but a different aggregate for each of the four points. The values are for nearest-neighbour hopping and zero surface tension.

![](./images/811975233052344321_4.jpg)

Figure 4. The number of clusters is shown as a function of the time in MCS/particle. This is for an initial aggregate grown with zero surface tension, with hopping to nearest and next-nearest neighbours. Note in particular the rapid rise initially from a single cluster to a large number of clusters, and then a slow relaxation to a lower number of clusters. The insert is an expansion of the first five MCS/particle showing the initial rise and relaxation.

![](./images/811975233052344321_5.jpg)

Figure 5. The effective fractal dimension $D_{\mathrm{f}}^{\text {eff }}$ as a function of MCS/particle is shown for a cluster of $10^{3}$ particles with hopping to nearest neighbours. This graph is an average over $10^{2}$ random number sequences. Note the greatly expanded scale for $D_{\mathrm{f}}^{\text {eff }}$.

![](./images/811975233052344321_6.jpg)

Figure 6. The energy of equilibrated aggregates which were grown with different surface tensions is shown as a function of the allowed hopping radius. All points are for aggregates of $5 \times 10^{4}$ particles after equilibration for $5 \times 10^{3} \mathrm{MCS} /$ particle. A single initial aggregate was used for all points for a given surface tension. Only one equilibration was used on the aggregate. The full lines are only a guide for the eye. The broken line is the energy of a circular compact cluster of $5 \times 10^{4}$ particles.

![](./images/811975233052344321_7.jpg)

Figure 7. The number of clusters in equilibrated aggregates which were grown with different surface tensions is shown as a function of the allowed hopping radius. All points are for aggregates of $5\times10^{4}$ particles after equilibration for $5\times10^{3}$ MCS/particle. A single initial aggregate was used for all points for a given surface tension. Only one equilibration was used on the aggregate. The lines are only a guide for the eye.

of parameters. Of course, if the hopping radius is made sufficiently large (comparable with the size of the cluster) and we allow the system to relax for a sufficient period of time it will eventually become compact.

Many of the properties of the fully relaxed clusters do depend fairly substantially on the value of the hopping radius used. For example, the energy of the relaxed cluster decreased by as much as 50% with respect to the unrelaxed cluster as the hopping radius was increased. The variation of the final energy with hopping radius is shown in figure 6. Notice that the final energy is quite close to the value which we would expect for a compact cluster with a free surface even though the fractal dimension is unchanged from its original DLA value. In figure 7 we show the dependence of the average cluster size on the hopping radius. As long as the hopping radius is larger than the average finger thickness [5], the aggregate quickly breaks into a large number of clusters. The number of clusters increases slightly as the hopping radius increases.

### 4. Conclusions

Our study has revealed substantial changes in the internal energy of DLA clusters which are allowed to equilibrate, but for the values of the parameters considered here the fractal dimension of the system does not change. This means that relaxation techniques which have been used in the past to study DLA clusters do not themselves introduce a modification of the fractal properties of the system. DLA is an example of a non-equilibrium system, and our simulations show that different quantities behave quite differently as partial equilibrium is achieved.

When a less viscous fluid is injected into a more viscous fluid in a porous media, fingering related to that seen in DLA simulations [3-8] is observed [11]. However, there are always some relaxation effects which will attempt to change the injected fluid from having a fractal pattern to the equilibrium structure of a compact droplet (at least this is the situation if the injected fluid does not wet the porous medium). Our simulation demonstrates that these relaxation effects do not cause a substantial change in the fractal dimension, and hence can safely be ignored in the analysis of experimental data. The effects of surface tension are to increase the width of the aggregate fingers. We predict that effects of equilibration with surface tension will be to increase the typical size of the droplets formed during equilibration.

## Acknowledgments

The authors wish to thank the IBM Bergen Scientific Centre for its hospitality during a portion of the time when this work was carried out. We are indebted to J Feder, T Jøssang, K Kaski, P Meakin and K Måløy for helpful comments and discussion. This research was supported in part by NSF grant DMR-8715740, and by the Florida State University Supercomputer Computations Research Institute which is partially funded by the US Department of Energy through Contract DE-FC05-85ER25000.

## References

[1] Family F and Landau D P (eds) 1984 *Kinetics of Aggregation and Gelation* (Amsterdam: North-Holland)
Stanley H E and Ostroskey N (eds) 1986 *On Growth and Form, Fractal and Non-fractal Patterns in Physics* (Boston: Martinus Nijhoff)

[2] Witten T A and Sander L M 1981 *Phys. Rev. Lett.* **47** 1400-3

[3] Kadanoff L P 1985 *J. Stat. Phys.* **39** 267-83

[4] Vicsek T 1984 *Phys. Rev. Lett.* **53** 2281-4
Vicsek T 1985 *Phys. Rev. A* **32** 2084-9

[5] Tao R, Novotny M A and Kaski K 1988 *Phys. Rev. A* **38** 1019-26

[6] Paterson L 1984 *Phys. Rev. Lett.* **52** 1621-4

[7] Bensimon D, Kadanoff L P, Liang S, Shraiman B and Tang C 1986 *Rev. Mod. Phys.* **58** 977-99

[8] Meakin P, Family F and Vicsek T 1987 *J. Coll. Interface Sci.* **117** 394-9

[9] Botet R and Jullien R 1985 *Phys. Rev. Lett.* **55** 1943-6

[10] Kolb M 1986 *J. Phys. A: Math. Gen.* **19** L263-8

[11] Sørensen E S, Fogedby H C and Mouritsen O G 1988 *Phys. Rev. Lett.* **61** 2770-3

[12] Måløy K J, Feder J and Jøssang T 1985 *Phys. Rev. Lett.* **55** 2688-91

[13] Måløy K J, Feder J and Jøssang T (unpublished)