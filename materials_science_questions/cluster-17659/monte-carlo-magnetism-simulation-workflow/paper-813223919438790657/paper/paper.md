# Critical phase of a magnetic hard hexagon model on a triangular lattice

Yasushi Honda and Tsuyoshi Horiguchi

Department of Computer and Mathematical Sciences, Graduate School of Information Sciences, Tohoku University, Sendai 980-77, Japan
(Received 15 July 1996)

We introduce a magnetic hard hexagon model with two-body restrictions for configurations of hard hexagons and investigate its critical behavior by using Monte Carlo simulations and a finite size scaling method for discrete values of activity. It turns out that the restrictions bring about a critical phase which the usual hard hexagon model does not have. An upper and a lower critical value of the discrete activity for the critical phase of the proposed model are estimated as 4 and 6, respectively. [S1063-651X(97)04601-1]

PACS number(s): 64.60.-i, 75.10.-b

## I. INTRODUCTION

Critical behavior of the hard hexagon model on a triangular lattice is well known through its exact solution by using the corner transfer matrix [1]. Below a critical value of the activity $z\sim 11$, the system is in the disordered phase. Therefore, a correlation function between hard hexagons decays exponentially there [2]. Above the critical value of the activity, the hexagons on the lattice condense and make an ordered configuration. The degeneracy of the ordered configuration is triplefold and the universality class of the critical point is the same as that of the three-state Potts model [1,3]. The fact that the hexagons are hard means that there is a restriction between the nearest-neighbor sites, such that any two hexagons cannot occupy two neighboring sites simultaneously on the triangular lattice. This property of the hard hexagon model can be regarded as the nearest-neighbor exclusion. Adding to the nearest-neighbor exclusion, a next-nearest-neighbor exclusion causes fourfold degeneracy in the ground state. Todo and Suzuki [4] claimed that the hard hexagon model with the next-nearest-neighbor exclusion belongs to the same universality class as that of the four-state Potts model by means of the numerical study by using the phenomenological renormalization group method and the conformal invariance.

Recently, it was found that an antiferromagnetic spin-$S$ Ising model on the triangular lattice has a relation with the hard hexagon model with many restrictions for configurations of hexagons [6]. The phase transition as a function of $S$ in the ground state of the spin-$S$ Ising model was studied by using a mapping from the ground state degeneracy of the system at zero temperature to a partition function of a spin-1/2 system at a pseudotemperature [5,6]; the mapped system is called a $\Delta$ model. The original $S=1/2$ Ising model was exactly solved and it is well known that the system is critical with $\eta=1/2$ at zero temperature [7,8]. Nagai *et al.* [9] showed that the critical index $\eta$ decreases from 1/2 for $S=1/2$ when the spin $S$ increases from $S=1/2$. It has been clarified that $\eta$ becomes zero at $S=7/2$ discontinuously [6]. This behavior of $\eta$ suggests an appearance of a partial long-range order for the system with $S\geqslant7/2$; it was shown explicitly for $S=\infty$ [10]. We remind the reader that the $\Delta$ model is the hard hexagon model with many kinds of restrictions [6]. In contrast with the usual hard hexagon model which does not have any extra restrictions but only the nearest-neighbor repulsion, the $\Delta$ model is critical for $1/2\leqslant S\leqslant3$ [6].

The purpose of the present paper is to introduce a hard hexagon model; we call it a magnetic hard hexagon model. The magnetic hard hexagon model with up to the third-nearest-neighbor repulsions is investigated by Monte Carlo simulations and a finite size scaling for evaluation of $\eta$. We find that the hard hexagon model has an ordered phase, a critical phase, and the disordered phase. We discuss a relation of the hard hexagon model with the spin-$S$ Ising model on the antiferromagnetic triangular lattice.

In Sec. II, we introduce the magnetic hard hexagon model with exclusions up to the third-nearest-neighbor sites with relation to the spin-$S$ Ising model on the triangular lattice. In Sec. III, we show our results about a phase diagram of our model and discuss these results. Concluding remarks are given in Sec. IV.

## II. MAGNETIC HARD HEXAGON MODEL WITH RESTRICTIONS

Let us introduce a magnetic hard hexagon model which is related to a representation of the ground state degeneracy for the spin-$S$ Ising model on an antiferromagnetic triangular lattice (ATL). The "occupation number" of magnetic hard hexagons is denoted by $\zeta_i$ at a site $i$ on the triangular lattice $\Lambda$; $\zeta_i$ takes on $\{-1,0,+1\}$. If the site $i$ is occupied by an "up magnetic hard hexagon" or by a "down magnetic hard hexagon," then we assign them $\zeta_i=+1$ and $-1$, respectively. If the site $i$ is empty, then we set $\zeta_i=0$.

The ground partition function of the system is written as
$$
\begin{aligned}
Z_{\text{RMHH}}= & \sum_{\{\zeta_i\}} z^{\sum_{i=1}^N\left|\zeta_i\right|} \prod_{\langle i,j\rangle}\left(1-\left|\zeta_i\right|\left|\zeta_j\right|\right) \\
& \times \prod_{\langle i,k\rangle'} \frac{1}{2}\left(1+\zeta_i \zeta_k\right) \prod_{\langle i,l\rangle''} \frac{1}{2}\left(1-\zeta_i \zeta_l\right),
\end{aligned}\quad (1)
$$
where $N=|\Lambda|$, and the products with $\langle i,j\rangle$, $\langle i,k\rangle'$, and $\langle i,l\rangle''$ are taken over the nearest-neighbor pairs of sites, the next-nearest-neighbor pairs of sites, and third-nearest-neighbor pairs of sites, respectively. We explain below a

![](./images/813223919438790657_1.jpg)

FIG. 1. Set of sites, $C_{1}(i)$ and $C_{2}(i)$, encircling the site $i$. These appear in Eq. (5) for evaluation of the occupation number $k_{i}\{\sigma_{I}\}$ of a hexagon.

relation of $Z_{\text{RMHH}}$ with the ground state degeneracy of the spin-$S$ Ising model on the ATL. In this relation, the activity denoted by $z$ is equal to $2S$.

The Hamiltonian of the spin-$S$ Ising model on the ATL is written as
$$
\mathcal{H}\{S\}=J \sum_{\langle i, j\rangle} S_{i} S_{j}, \tag{2}
$$
where $J\ (>0)$ is the interaction constant between nearestneighbor sites denoted by $\langle i, j\rangle$ and $S_{i}$ is a spin variable which takes a value on $\{-S,-S+1, \ldots, S-1, S\}$. It has been shown that the ground state degeneracy of this system is equivalent to a partition function of a spin-1/2 Ising model as follows [5,6]:
$$
Z=\sum_{\left\{\sigma_{l} \mid E\left\{\sigma_{l}\right\} / L^{2}=-J / 4\right\}} \exp \left\{\ln (2 S) K\left\{\sigma_{I}\right\}\right\}, \tag{3}
$$
where the summation for spin configurations $\{\sigma_{I}\}$ is taken over the ground-state configurations of the spin-1/2 Ising model on the ATL with $\sigma_{I} \in\{-1 / 2,+1 / 2\}$: the energy of the system, $E\{\sigma_{I}\} / L^{2}$, has to be $-J / 4$. We recall that this is the partition function of the $\Delta$ model [5]. The linear size of the system is denoted by $L$. $K\{\sigma_{I}\}$ denotes the total number of free spins and is expressed as follows:
$$
K\left\{\sigma_{I}\right\}=\sum_{i \in \Lambda} k_{i}\left\{\sigma_{I}\right\}, \tag{4}
$$

$$
k_{i}\left\{\sigma_{I}\right\} \equiv \prod_{j \in C_{1}(i)}\left(\frac{1}{2}+2 \sigma_{i} \sigma_{j}\right) \prod_{j \in C_{2}(i)}\left(\frac{1}{2}-2 \sigma_{i} \sigma_{j}\right), \quad(5)
$$
where in Eq. (4) the summation is over the set of sites in the lattice $\Lambda$ and in Eq. (5) $C_{1}(i)$ and $C_{2}(i)$ are sets of sites, each of them composed of three sites encircling the site $i=(x, y)$ as shown in Fig. 1. When right bonds shown by thick lines are arranged in such a way given in Fig. 2, the value of the function $k_{i}\{\sigma_{I}\}$ becomes 1; this means that a hexagon occupies the site $i=(x, y)$. In this situation, the site $(x+1, y)$ cannot be occupied by another hexagon, because the value of $\sigma_{(x, y)} \sigma_{(x+1, y)}$ on the bond $(x, y)-(x+1, y)$ is $-1 / 4$ and hence the value of $k_{(x+1, y)}\{\sigma_{I}\}$ is 0. One cannot put another hexagon on the site $(x, y-1)$ because the value $\sigma_{(x, y)} \sigma_{(x, y-1)}$ is $+1 / 4$. For the same reasons as those for the sites $(x+1, y)$ and $(x, y-1)$ explained above, all of the sites encircling the site $i=(x, y)$ cannot be occupied by another hexagon when the site $i$ is occupied by a hexagon. Therefore, we can regard $k_{i}\{\sigma_{I}\}$ as an occupation number of the hard hexagon.

![](./images/813223919438790657_2.jpg)

FIG. 2. Restriction between two hexagons on the nearestneighbor sites. Thick solid lines encircling the site $i=(x, y)$ mean right bonds which give $k_{i}\{\sigma_{I}\}=1$ corresponding to an occupation of this site by a hexagon. One cannot put another hexagon, for example, on $(x+1, y)$ or $(x, y-1)$ obviously.

In the partition function written in Eq. (3), the summation is taken over the ground state spin configurations. If we regard the function $k_{i}\{\sigma_{I}\}$ of the spin configuration $\{\sigma_{I}\}$ as a variable $k_{i}$, the partition function is rewritten as a summation over configurations of hard hexagons $\{k_{i}\}$ as follows:
$$
\begin{aligned}
Z= & \sum_{\left\{k_{i}\right\}} \exp \left\{\ln (2 S) \sum_{i \in \Lambda} k_{i}\right\} \sum_{\left\{\sigma_{I}\right\}} \delta\left(E\left\{\sigma_{I}\right\} / L^{2}+J / 4\right) \\
& × \prod_{i \in \Lambda} \delta\left(k_{i}-k_{i}\left\{\sigma_{I}\right\}\right), \tag{6}
\end{aligned}
$$
where we define a function $\delta(x)$ as
$$
\delta(x) \equiv \begin{cases}1 & (x=0) \\ 0 & (x \neq 0).\end{cases} \tag{7}
$$

The restriction for occupations of the nearest-neighbor sites, namely the nearest-neighbor exclusion, is included in the expression $\prod_{i \in \Lambda} \delta(k_{i}-k_{i}\{\sigma_{I}\})$ in Eq. (6). One can write it explicitly as follows:
$$
\begin{aligned}
Z= & \sum_{\left\{k_{i}\right\}} \exp \left\{\ln (2 S) \sum_{i \in \Lambda} k_{i}\right\} \prod_{\langle i, j\rangle}\left(1-k_{i} k_{j}\right) \\
& × \sum_{\left\{\sigma_{I}\right\}} \delta\left(E\left\{\sigma_{I}\right\} / L^{2}+J / 4\right) \prod_{i \in \Lambda} \delta\left(k_{i}-k_{i}\left\{\sigma_{I}\right\}\right). \quad(8)
\end{aligned}
$$

Comparing this form with the usual hard hexagon model with only the nearest-neighbor exclusion [1], one notices that $2S$ plays a role of activity. When the partition function is expressed in terms of the occupation number of the hard hexagons, we can see that there are many other restrictions

![](./images/813223919438790657_3.jpg)

FIG. 3. Restriction between two magnetic hard hexagons on the next-nearest-neighbor sites. A magnetic hard hexagon $\zeta_{i}=+1$ occupies the site $i=(x, y)$, and therefore a magnetic hard hexagon $\zeta_{i^{\prime}}=+1$ can occupy the site $i^{\prime}=(x+1, y-1)$, but $\zeta_{i^{\prime}}=-1$ cannot.

for configurations of hard hexagons than that for the nearest-neighbor sites. In order to embody some of these restrictions, we introduce a magnetic hard hexagon in the following.

Let us define the "occupation number" of the magnetic hard hexagon $\zeta_{i}\{\sigma_{l}\}$ as follows:
$$
\begin{aligned}
\zeta_{i}\left\{\sigma_{l}\right\} & \equiv 2 \sigma_{i} \prod_{j \in C_{1}(i)}\left(\frac{1}{2}+2 \sigma_{i} \sigma_{j}\right) \prod_{j \in C_{2}(i)}\left(\frac{1}{2}-2 \sigma_{i} \sigma_{j}\right) \\
& =2 \sigma_{i} k_{i}\left\{\sigma_{l}\right\}.
\end{aligned}\qquad(9)
$$

By introducing the function $\zeta_{i}\{\sigma_{l}\}$, one can distinguish two types of hard hexagons; one of them is given by $\sigma_{i}=+1 / 2$ and the other by $\sigma_{i}=-1 / 2$. They correspond to $\zeta_{i}=+1$ and $\zeta_{i}=-1$, respectively; we call them an up magnetic hard hexagon for $\zeta_{i}=+1$ and a down magnetic hard hexagon for $\zeta_{i}=-1$. Regarding the occupation number of the magnetic hard hexagon as a variable similar to that in the usual hard hexagon, the partition function (8) can be rewritten by a sum over configurations of magnetic hard hexagons $\{\zeta_{i}\}$ as follows:
$$
\begin{aligned}
Z= & \sum_{\left\{\zeta_{i}\right\}} \exp \left\{\ln (2 S) \sum_{i \in \Lambda}\left|\zeta_{i}\right| \prod_{\langle i, j\rangle}\left(1-\left|\zeta_{i}\right|\left|\zeta_{j}\right|\right)\right. \\
& \left.\times \sum_{\left\{\sigma_{l}\right\}} \delta\left(E\left\{\sigma_{l}\right\} / L^{2}+J / 4\right) \prod_{i \in \Lambda} \delta\left(\zeta_{i}-\zeta_{i}\left\{\sigma_{l}\right\}\right).\right.
\end{aligned}\qquad(10)
$$

In this description, the factor $\prod_{i \in \Lambda} \delta(\zeta_{i}-\zeta_{i}\{\sigma_{l}\})$ gives extra exclusion conditions as for configurations of magnetic hard hexagons other than the nearest-neighbor exclusion. Namely, the magnetic hard hexagons have in general next-nearest-neighbor exclusion, third-nearest-neighbor exclusion, and so on, in addition to the nearest-neighbor exclusion.

Let us assume that a site $i=(x, y)$ is occupied by an up magnetic hard hexagon with $\zeta_{(x, y)}=+1$ as shown in Fig. 3. Since two sites $(x+1, y)$ and $(x, y-1)$ at the boundary between two hexagons located at $(x, y)$ and $(x+1, y-1)$ are connected by a right bond with $\sigma_{(x+1, y)}=-1 / 2$ and $\sigma_{(x, y-1)}=+1 / 2$, an up magnetic hard hexagon with $\zeta_{(x+1, y-1)}=+1$ on the site at $(x+1, y-1)$ can exist with that with $\zeta_{(x, y)}=1$. However, following the definition of the magnetic hard hexagon defined by Eq. (9), the site at $(x+1, y-1)$ cannot be occupied by a down magnetic hard hexagon with $\zeta_{(x+1, y-1)}=-1$. The other five next-nearest-neighbor sites of $(x, y)$ are in a similar situation. Thus we realize that there is a restriction between two magnetic hard hexagons on the next-nearest-neighbor sites.

![](./images/813223919438790657_4.jpg)

FIG. 4. Restriction between two magnetic hexagons on third-nearest-neighbor sites.

We notice that there is another restriction due to the definition of magnetic hard hexagon as explained in Fig. 4. Assume that a site at $(x, y)$ is occupied by an up magnetic hard hexagon. When we put a magnetic hard hexagon at the site(x+2,y), for example, this magnetic hard hexagon is in contact with the magnetic hard hexagon at $(x, y)$ on the site $(x+1, y)$. Since $\zeta_{(x, y)}=+1$, the value of spin at $(x+1, y)$ is $-1 / 2$. When the magnetic hard hexagon at $(x+2, y)$ has $\zeta_{(x+2, y)}=1$, the bond between sites $(x+1, y)$ and $(x+2, y)$ is not satisfied and hence the magnetic hard hexagons at the site $(x, y)$ and $(x+2, y)$ are not compatible. On the other hand, the magnetic hard hexagon with $\zeta_{(x+2, y)}=-1$ is compatible with that with $\zeta_{(x, y)}=+1$. Other third-nearest-neighbor sites are in the same situation as that of the site(x+2,y). Thus we have the restriction that a magnetic hard hexagon located at the third-nearest-neighbor sites, $l$, of an occupied site $i, \zeta_{i}$, has to have the reverse sign of that of $\zeta_{i} ; \zeta_{l}=-sgn(\zeta_{i})$.

We have explained three kinds of restrictions for configurations of magnetic hard hexagons. Although they originally stem from a definition of the magnetic hexagon as a function of spin configurations defined in Eq. (9), we can write them explicitly in terms of $\{\zeta_{i}\}$ as follows:
$$
R\left\{\zeta_{l}\right\} \equiv \prod_{\langle i, j\rangle}\left(1-\left|\zeta_{i}\right|\left|\zeta_{j}\right|\right) \prod_{\langle i, k\rangle}{ }^{\prime} \frac{1}{2}\left(1+\zeta_{i} \zeta_{k}\right) \prod_{\langle i, l\rangle}{ }^{\prime \prime} \frac{1}{2}\left(1-\zeta_{i} \zeta_{l}\right),
\qquad(11)
$$
where $\langle i, k\rangle^{\prime}$ and $\langle i, l\rangle^{\prime \prime}$ mean the next-nearest-neighbor and the third-nearest-neighbor pairs, respectively. In the $\Delta$ model for which its partition function is given by Eq. (10), there are many other restrictions than those two-body exclusions mentioned above. It is expected that those two-body exclusions give an important effect for a large value of the activity and hence the magnetic hard hexagons condense and make an ordered phase for large values of activity; the large value of the activity corresponds to a large value of the spin.

We now propose a magnetic hard hexagon model which has only three kinds of two-body exclusions and we investigate a critical behavior of the magnetic hard hexagon model; the partition function of the model is described as follows:

$$
Z_{\mathrm{RMHH}}=\sum_{\left\{\zeta_{l}\right\}} \exp \left\{\ln (2 S) \sum_{i \in \Lambda}\left|\zeta_{i}\right|\right\} R\left\{\zeta_{l}\right\}, \quad(12)
$$

where $R\{\zeta_{l}\}$ is the restriction defined in Eq. (11); this is equivalent to that given by Eq. (1). Although the usual hard hexagon model with only the nearest-neighbor exclusion was solved exactly, it seems difficult to obtain an exact solution for the present model. We therefore carry out Monte Carlo (MC) simulations for the model.

## III. RESULTS FROM MONTE CARLO SIMULATION AND DISCUSSIONS

We perform MC simulations at a finite temperature given by $T=1 / \ln (2 S)$ with a unit of the Boltzmann constant $k_{B}=1$. We used the Metropolis dynamics to update configurations of the magnetic hard hexagon in the MC simulations. A finite size scaling method [6,9-12] is used to estimate a critical index $\eta$ which describes a decay of correlation functions between hexagons separated by a long distance. The index $\eta$ is determined from

$$
A_{z} \equiv \frac{1}{L^{2}}\left\langle\left(\sum_{i \in A} \zeta_{i}\right)^{2}+\left(\sum_{j \in B} \zeta_{j}\right)^{2}+\left(\sum_{k \in C} \zeta_{k}\right)^{2}\right\rangle \propto L^{2-\eta},
$$

where $A$, $B$, and $C$ mean three kinds of sublattice of the triangular lattice. We need two finite lattices at least to obtain the index $\eta$ from this relation as follows:

$$
\eta\left(L_{i+1}\right)=2-\frac{\ln \left\{A_{z}\left(L_{i+1}\right) / A_{z}\left(L_{i}\right)\right\}}{\ln \left(L_{i+1} / L_{i}\right)}.
$$

In the present study, we set $L_{1}, L_{2}, \ldots, L_{6}$ equal to 24,36 , 48, 60, 90, 120, respectively, in this order. This method is based on the assumption that a system is in a critical phase. If the system is in the disordered phase, $\eta$ estimated by this method would appear to be 2. This value does not mean that the system is in a critical phase with the index $\eta=2$ but in the disordered phase. On the other hand, if the system is in an ordered phase, it should be zero.

In the present MC simulations, we used more than $10^{5}$ MC step per site for each system size. Figure 5 shows results of size dependences of critical index $\eta$ for $z=1,2,3$, and 3.5. We observed that $\eta$ approaches 2 in the thermodynamic limit for these values of activity. These results mean that the systems with these values of activity are in the disordered phase. For a small value of the activity, the density of magnetic hard hexagons is low and hence there are many lattice sites unoccupied by a magnetic hard hexagon.

![](./images/813223919438790657_5.jpg)

FIG. 5. Size dependences of critical index $\eta$ for $z=1,2$, and 3 . The values of $\eta$ become 2 in the thermodynamic limit. This means that the system is in the disordered phase.

In Figs. 6 and 7, size dependences of the critical index $\eta$ are shown for $z=4,5,5.5,6,6.5$, and 7. For $z_{c 1} \leqslant z \leqslant z_{c 2}$, the values of $\eta$ take finite values in the thermodynamic limit where $3.5<z_{c 1} \leqslant 4$ and $6 \leqslant z_{c 2}<6.5$. Since the values of $\eta$ are obviously less than 2 and actually less than $1 / 2$, the systems with these values of activity are in a critical phase. In contrast to the case with $z<z_{c 1}$, two-body restrictions considered in our model play a role of providing a critical phase for $z_{c 1} \leqslant z \leqslant z_{c 2}$. For $z=6.5$ and 7 , we found that the value of $\eta$ becomes zero in the thermodynamic limit. These results suggest an appearance of ordered phase at $z=z_{c 2}$. From the relation of the present model with the spin $S$ Ising model on the ATL, we have $z=2 S$ and hence $S_{c 1}=2$ and $S_{c 2}=3$. Note that the discrete value of activity, namely, the value of spin where $\eta$ becomes zero is very close to that in the original spin system; $S_{c 2}=3$ [6]. This agreement, we think, is due to a dominant role of the two-body restrictions in the region of large activity, which gives high density of magnetic hard hexagons.

In Fig. 8, we show a comparison of phase diagrams for the usual hard hexagon model, the magnetic hard hexagon model with two-body restrictions, and the spin- $S$ Ising model on the ATL. The usual hard hexagon model with only the nearest-neighbor exclusion has two phases, that is, the disordered phase and the ordered phase. There is no critical phase in the usual hard hexagon model. On the other hand, the spin- $S$ Ising model on the ATL, which is equivalent to a magnetic hard hexagon model with many restrictions, has the critical phase and the ordered phase. There is no disordered

![](./images/813223919438790657_6.jpg)

FIG. 6. Size dependences of critical index $\eta$ for $z=4,5$, and 5.5. The values of $\eta$ apparently become finite less than $1 / 2$ in the thermodynamic limit. These results mean the systems with $z=4,5$, and 5.5 are in a critical phase.

![](./images/813223919438790657_7.jpg)

FIG. 7. Size dependences of critical index $\eta$ for $z=6$, 6.5, and 7. For $z=6$, the value of $\eta$ becomes finite in the thermodynamic limit. On the other hand, for $z=6.5,7$ the value of $\eta$ becomes zero, which corresponds to an ordered phase.

phase in the original spin-$S$ Ising model. Our model investi- gated in the present paper has three phases, that is, the dis- ordered phase, the critical phase, and the ordered phase. The ground state degeneracy is sixfold. Hence we expect that our model belongs to the same universality class as that of the six-state clock model.

## IV. CONCLUSIONS

We have proposed a magnetic hard hexagon model with two-body exclusions. We have shown a relation of the model and the spin-$S$ Ising model on the antiferromagnetic triangu- lar lattice. The phase diagram of the model has been inves- tigated by evaluating the critical exponent $\eta$ by means of Monte Carlo simulations. It turned out that the model has three phases, that is to say, the disordered phase for $z<z_{c 1}$, the critical phase for $z_{c 1} \leqslant z \leqslant z_{c 2}$, and the ordered phase for $z>z_{c 2}$, where $3.5<z_{c 1} \leqslant 4$ and $6 \leqslant z_{c 2}<6.5$. We notice that an upper critical value $S_{c 2}$ for the critical phase in the model is the same as the critical value of spin in the original spin-$S$ Ising model.

![](./images/813223919438790657_8.jpg)

FIG. 8. (a) Phase diagram of the usual hard hexagon model with only the nearest-neighbor exclusion. There is no critical phase. (b) Phase diagram of our model investigated in the present paper. There appear a critical phase between the disordered phase and the or- dered phase. (c) Phase diagram of the spin-$S$ Ising model on the ATL. There is no disordered phase.

Although the two-body restrictions considered in our model are not enough when they are compared to those in- cluded in the original spin-$S$ system, namely the $\Delta$ model, we saw they are enough to provide a critical phase, which does not exist in the usual hard hexagon model. We esti- mated in the present paper only the index $\eta$ to clarify the phase diagram of our model. Calculations of the other criti- cal indices and estimations of more definite values of $z_{c 1}$ and $z_{c 2}$ are left as a future problem to understand the critical property of our model.

## ACKNOWLEDGMENTS

We would like to thank Dr. A. Lipowski for valuable discussions. This work was partly supported by the Com- puter Center, Tohoku University.

[1] R. J. Baxter, *Exactly Solved Models in Statistical Mechanics* (Academic Press, London, 1989).
[2] R. J. Baxter and P. A. Pearce, J. Phys. A **15**, 897 (1982).
[3] S. Alexander, Phys. Lett. A **54**, 353 (1975).
[4] X. Todo and M. Suzuki, in *Coherent Approaches to Fluctua- tions*, edited by M. Suzuki and N. Kawashima (World Scien- tific, Singapore, 1996).
[5] A. Lipowski, T. Horiguchi, and D. Lipowska, Phys. Rev. Lett. **74**, 3888 (1995).
[6] Y. Honda, A. Lipowski, and T. Horiguchi, Phys. Rev. B **52**, 13 429 (1995).
[7] G. H. Wannier, Phys. Rev. **79**, 357 (1950); R. M. F. Houtap- pel, Physica **16**, 425 (1950); K. Husimi and I. Syoji, Prog. Theor. Phys. **5**, 177 (1950); **5**, 341 (1950).
[8] J. Stephenson, J. Math. Phys. **5**, 1009 (1964).
[9] O. Nagai, S. Miyashita, and T. Horiguchi, Phys. Rev. B **47**, 202 (1993).
[10] T. Horiguchi, O. Nagai, and S. Miyashita, J. Phys. Soc. Jpn. **60**, 1513 (1991).
[11] S. Miyashita, H. Nishimori, A. Kuroda, and M. Suzuki, Prog. Theor. Phys. **60**, 1669 (1978).
[12] K. Binder, in *Finite Size Scaling and Numerical Simulation of Statistical Systems*, edited by V. Privman (World Scientific, Singapore, 1990).