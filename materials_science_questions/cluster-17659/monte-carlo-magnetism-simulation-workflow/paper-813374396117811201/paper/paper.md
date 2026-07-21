# Loop algorithm for classical antiferromagnetic Heisenberg models with biquadratic interactions

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2011 J. Phys.: Conf. Ser. 320 012009

(http://iopscience.iop.org/1742-6596/320/1/012009)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 46.161.62.5
This content was downloaded on 29/06/2016 at 06:37

Please note that terms and conditions apply.

# Loop algorithm for classical antiferromagnetic Heisenberg models with biquadratic interactions

Hiroshi Shinaoka $^{1,2}$, Yusuke Tomita $^{1}$ and Yukitoshi Motome $^{3}$

$^{1}$Institute for Solid State Physics, University of Tokyo, Kashiwanoha, Kashiwa, Chiba, 277-8581, Japan
$^{2}$Present address: Nanosystem Research Institute, AIST, Tsukuba 305-8568, Japan
$^{3}$Department of Applied Physics, University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-8656, Japan

E-mail: h.shinaoka@aist.go.jp

**Abstract.** Monte Carlo simulation using the standard single-spin flip algorithm often fails to sample over the entire configuration space at low temperatures for frustrated spin systems. A typical example is a class of spin-ice type Ising models. In this case, the difficulty can be avoided by introducing a global-flip algorithm, the loop algorithm. Similar difficulty is encountered in $O(3)$ Heisenberg models in the presence of biquadratic interaction. The loop algorithm, however, is not straightforwardly applied to this case, since the system does not have a priori spin-anisotropy axis for constructing the loops. We propose an extension of the loop algorithm to the bilinear-biquadratic models. The efficiency is tested for three different ways to flip spins on a loop in Monte Carlo simulation. We show that the most efficient method depends on the strength of the biquadratic interaction.

## 1. Introduction

Monte Carlo (MC) simulation is a powerful tool for investigating thermodynamic properties of classical spin models [1]. The standard single-spin flip algorithm is widely used because it is simple and applicable to systems with any type of interactions. However, it is well known that it suffers from slow relaxation in many cases. For example, the single-spin-flip dynamics exhibits critical slowing down near a continuous transition temperature where the correlation length diverges. Such difficulty is avoided by using a nonlocal, global update, such as the Swendsen-Wang cluster algorithm for Ising systems [2] or its Wolff's extension to Heisenberg systems [3]. These cluster algorithms accelerate the relaxation by flipping many spins at once, i.e., updating the spin configuration drastically.

Besides the critical slowing down, the single-spin flip algorithm often suffers from dynamical freezing at low temperature $(T)$ when the ground state has macroscopic degeneracy under the influence of geometrical frustration. A typical example is an antiferromagnetic Ising model on a pyrochlore lattice. The pyrochlore lattice is a three-dimensional frustrated structure given by a corner-sharing network of tetrahedra, as shown in Fig. 1(a). When the antiferromagnetic exchange interaction is limited to nearest-neighbor sites, no long-range ordering occurs down to zero $T$ and the ground state has macroscopic degeneracy [4]. The degenerate manifold is identified by a collection of local constraints enforcing two spins pointing up and two spins pointing down in every tetrahedron, as exemplified in Fig. 1(a). This 'two-up two-down'

constraint is called the ice rule because of an analogy to the constraint on positions of protons in hexagonal ice [5, 6]. Similar situation was recently discovered in the so-called spin-ice systems, in which the Ising-like spins point along the local ⟨111⟩ axes and interact with each other by ferromagnetic exchange interaction and dipole interaction [7, 8]. Because the degenerate 'ice-rule' configurations are separated by large energy barriers of the order of the dominant interaction scale $J$, the single-spin flip does not work at low $T \ll J$. The difficulty is avoided by introducing a global flip called the loop flip, in which one reverses all Ising spins on a specific closed loop passing through tetrahedra [9, 10, 11, 12, 13]; the loop is chosen so that the spins are up and down (inward and outward in the spin-ice problem) alternatively along the loop [see the hexagon in Fig. 1(a) as an example]. This loop flip enables to transform an ice-rule state to another ice-rule state bypassing the energy barriers.

The difficulty remains even when the Ising discreteness is relaxed and spins can fluctuate, as long as the ground-state manifold retains a multivalley structure with large energy barriers. Such situation is seen in variants of pyrochlore antiferromagnets, such as classical Heisenberg models in the presence of the single-ion easy-axis anisotropy [14, 15] and the biquadratic interaction [16]. In contrast to the Ising case, however, it is nontrivial how to define the loop with alternating spins. Moreover, the loop flip procedure is not unique in the Heisenberg spin case because of the continuous degrees of freedom. Recently, the authors extended the loop algorithm to the Heisenberg spin systems with single-ion anisotropy by defining 'colors' of spins as black and white, which is a natural generalization of up and down in the antiferromagnetic Ising case, in terms of the projection of spins on the anisotropy axis [15]. We tested different ways to flip spins on a formed loop and showed that the efficiency strongly depends on the method. In the models with the biquadratic interaction, however, because of the $O(3)$ spin rotational symmetry, we have no explicit anisotropy axis to project spins on. Therefore, an extension of the loop algorithm to this class of models is not straightforward.

In this paper, we develop an extension of the loop algorithm to classical antiferromagnetic Heisenberg spin systems with biquadratic interaction in which the spin-ice type manifold emerges at low $T$. We propose a way to define the projection axis for constructing loops and test three different ways to flip a formed loop. We apply the algorithm to a nearest-neighbor bilinear- biquadratic model, and compare the efficiency of the three methods. Interested readers are referred to Ref. [17] for further application of the present algorithm to a bond-disordered bilinear- biquadratic model.

## 2. Extension of the loop algorithm to bilinear-biquadratic spin systems
### 2.1. Model
In this section, we extend the loop algorithm to classical antiferromagnetic Heisenberg models with biquadratic interactions. We start with a Hamiltonian of a simple form:

$$
\mathcal{H}=\sum_{\langle i, j\rangle}\left\{J\left(\vec{S}_{i} \cdot \vec{S}_{j}\right)-b\left(\vec{S}_{i} \cdot \vec{S}_{j}\right)^{2}\right\},
\tag{1}
$$

where $\vec{S}_{i}$ denotes a classical Heisenberg spin at site $i$ on the pyrochlore lattice [Fig. 1(a)] (we take $|\vec{S}_{i}|=1$) and $b$ is the coupling constant of the biquadratic interaction. Here we consider $b>0$ which favors collinear spin configurations. We note that such 'ferro'-type biquadratic interaction originates in the spin-lattice coupling as well as quantum and thermal fluctuations. We consider the antiferromagnetic exchange interaction $J>0$, and take the energy unit as $J=1$. The sum runs over the nearest-neighbor bonds of the pyrochlore lattice. The following algorithm is applicable to more general spin-ice type models on other frustrated lattices with farther-neighbor or bond-dependent interactions, and site-dependent anisotropy.

![](./images/813374396117811201_1.jpg)

**Figure 1.** (a) The pyrochlore lattice composed of a three-dimensional network of corner-sharing tetrahedra. A 16-site cubic unit cell is shown. Spins are denoted by solid arrows. The broken arrow $\vec{Q}$ shows a common axis selected by $b$ in the nematic phase. Black (filled) circles represent spins in the direction of $\vec{Q}$, while white (open) circles represent spins in the opposite direction. The spin configuration is an example of the spin-ice type states in which the 'two-up two-down' local constraint is satisfied in every tetrahedron. The hexagon with a bold dashed line denotes one of the shortest loops on which a flip of all spins (black and white) transforms the ice-rule state to another ice-rule state. (b) Three different ways to flip black and white: (1) *flip xyz*, (2) *flip parallel*, and (3) *rotate*. See the text for details.

When $b=0$, the model given by Eq. (1) exhibits no long-range ordering down to $T=0$, and the ground state is given by a collection of local constraints that enforces the sum of $\vec{S}_i$ to be zero in every tetrahedron. Consequently, the ground-state manifold has continuous macroscopic degeneracy [18, 19, 20]. For $b>0$, the present model exhibits a weak first-order transition at $T_c \sim b$ to a nematic state in which spins spontaneously select a common axis $\vec{Q}$ without selecting their directions on it [16]. Hence, the ground state for $b>0$ is identified by a collection of spin-ice type local constraints: in every tetrahedron, two out of four spins are aligned parallel to each other and the other two are antiparallel to them — 'two-up two-down' configuration [see Fig. 1(a)]. The ground-state manifold develops a multivalley structure whose minima correspond to different spin-ice-type configurations separated by large energy barriers of the order of $b$ and $J$.

### 2.2. Algorithm
In the previous paper, the authors developed an extension of the loop algorithm to be applicable to a family of classical Heisenberg antiferromagnets with single-ion anisotropy, in which the single-spin flip algorithm suffers from slow relaxation due to the formation of the spin-ice type manifold [15]. In the extended loop algorithm, (i) we first project all the spins onto the anisotropy axis to assign black and white colors, (ii) next, construct a loop of alternating black and white, and (iii) flip all the spins on the loop. For the present bilinear-biquadratic model, a similar difficulty from slow relaxation is anticipated because the low-$T$ state develops the spin-ice type degeneracy as mentioned above. However, it is not straightforward to apply the extended loop algorithm since the present model retains $O(3)$ spin rotational symmetry and does not have any explicit anisotropy axis to project the spins on. It is necessary to deduce the common axis $\vec{Q}$ selected by $b$ for each MC sample.

Here, we propose the following procedure to define the projection axis. We first pick up a set of $N_{\mathrm{T}}$ tetrahedra $\{\mathcal{T}_m\}$ ($m=1,\cdots,N_{\mathrm{T}}$) randomly from the whole system. Starting from an

initial guess $\vec{\alpha}_0$ [we take $\vec{\alpha}_0=(0,0,1)$], the normalized projection axis $\vec{\alpha}$ is obtained iteratively by

$$
\vec{\alpha}_{n+1} \propto \sum_{i \in\left\{\mathcal{T}_{m}\right\}} \operatorname{sign}\left(\vec{S}_{i} \cdot \vec{\alpha}_{n}\right) \vec{S}_{i}. \tag{2}
$$

Here the sum is taken over all spins belonging to the selected tetrahedra $\{\mathcal{T}_{m}\}$, and $n$ (= $0,1,\cdots,n_{\text{max}}-1$) is the index of the iteration. For larger $N_{\text{T}}$ and $n_{\text{max}}$, the resultant $\vec{\alpha}=\vec{\alpha}_{n_{\text{max}}}$ gives a better approximation of $\vec{Q}$. In practice, we take $N_{\text{T}}=24$ and $n_{\text{max}}=6$ in the following calculations for the system size with $N_{\text{s}}=16 \times 8^{3}$ spins. We confirm that the loop flip is efficiently performed for these conditions, as demonstrated below. Once $\vec{\alpha}$ is defined in this way, the step (ii) and (iii) are done in the same way as in Ref. [15]. It should be noted that, to ensure the detailed balance, loops must be constructed avoiding the tetrahedra included in $\{\mathcal{T}_{m}\}$ as well as defect tetrahedra in which the ice rule is violated. Otherwise, the loop flip becomes irreversible because the flip changes $\vec{\alpha}$.

In the extended loop algorithm, the loop flip procedure to reverse all colors on a loop is not unique because spins can thermally fluctuate [15]. To choose an efficient method, careful consideration on the energy change is necessary. In Ref. [15], the authors tested two different ways: (1) *flip xyz* and (2) *flip parallel*. In *flip xyz*, all three Cartesian components of $\vec{S}_{i}$ are reversed as $\vec{S}_{i} \rightarrow-\vec{S}_{i}$, while in *flip parallel*, only parallel components $\vec{S}_{i \|}$ are reversed as $\vec{S}_{i} \rightarrow \vec{S}_{i}-2(\vec{S}_{i} \cdot \vec{\alpha}) \vec{\alpha}$ [see Fig. 1(b)]. The previous study revealed that, in the case of the single-ion anisotropy, only the acceptance rate for *flip parallel* can become one (rejection free) in the limit of $T \rightarrow 0$; the acceptance rate for *flip xyz* converges to a finite value less than unity as $T \rightarrow 0$ because of the effect of thermal fluctuations on the transverse component of spins [15]. In addition to these two updates, in this paper, we introduce another way to reverse colors, i.e., (3) *rotate*. In *rotate*, one translates every spin to the neighboring site on the loop simultaneously in the direction in which the loop was formed [see Fig. 1(b)]. In the next section, we try the three different methods and demonstrate that the most efficient method depends on the model parameter $b$.

## 3. Benchmark
In this section, we apply the extended loop algorithm to the model given by Eq. (1). We demonstrate the efficiency of loop flips in MC simulations and compare the efficiency of the three methods. In the following, we show the MC results for the systems size with $N_{\text{s}}=16 \times 8^{3}$ spins under periodic boundary conditions. To retain the ergodicity, we use the loop flip together with the single-spin flip. One MC step consists of single-spin flips, followed by loop flips with either *flip xyz*, *flip parallel*, or *rotate*. In the single-spin flips, we randomly choose a new spin state on the unit sphere for each spin following a procedure proposed by Marsaglia [21].

At low $T$ compared to $b$ and $J$, spin configurations are enforced to satisfy the 'two-up two-down' ice rule, and the acceptance rate of the single-spin flip, $P_{\text{single}}$, is suppressed. This is demonstrated in Fig. 2. On the other hand, the probability that a closed loop is successfully formed, $P_{\text{loop}}$, steeply increases below the nematic transition temperature $T_{\text{c}} \sim b$, indicating that almost all tetrahedra start to follow the ice rule below $T_{\text{c}}$. [For $b>J$, the ice rule is weakly violated in the range of $T \gtrsim J$ even below $T_{\text{c}}$, but gradually satisfied for $T \lesssim J$, as exemplified in Fig. 2(d).] The acceptance rate of flips of a formed loop also increases below $T_{\text{c}}$ and remains finite as $T \rightarrow 0$; here, $P_{xyz}$, $P_{\text{parallel}}$, and $P_{\text{rotate}}$ are the rate for *flip xyz*, *flip parallel*, and *rotate*, respectively. The total acceptance rate of the loop flip is given by the product as $P_{\text{loop}} \times P_{xyz}$, $P_{\text{loop}} \times P_{\text{parallel}}$, and $P_{\text{rotate}} \times P_{\text{parallel}}$ for each method. Hence the acceptance rate of the loop flip sharply increases at $T<T_{\text{c}}$, compensating the decrease of $P_{\text{single}}$. These $T$ dependences are qualitatively the same for the wide range of $b$, as shown in Fig. 2.

![](./images/813374396117811201_2.jpg)

Figure 2. Temperature dependences of the acceptance rates of the single-spin flip ($P_{\rm single}$), the probability of formation of closed loops ($P_{\rm loop}$), the acceptance rates of flip of a formed loop by flip xyz ($P_{xyz}$), flip parallel ($P_{\rm parallel}$), and rotate ($P_{\rm rotate}$). The data are calculated at (a) $b=0.05$, (b) 0.2, (c) 0.6, and (d) 1.5. The vertical broken lines denote the nematic transition temperature $T_{\rm c}$ estimated by the peak position in the specific heat (not shown).

![](./images/813374396117811201_3.jpg)

Figure 3. $b$ dependence of $P_{\rm parallel}$, $P_{xyz}$, $P_{\rm rotate}$, and $P_{\rm single}$ at $T=0.02$.

As demonstrated in the previous study for the models with single-ion anisotropy [15], the efficiency of the loop flip at low $T$ depends on the method. Furthermore, in the present case with the biquadratic interaction $b$, the efficiency at low $T$ strongly depends on $b$. The result is presented in Fig. 3. For small $b<0.1$, flip parallel is most efficient, while it is taken over by rotate in the intermediate range of $0.1<b<0.5$, and finally by flip xyz for $b>0.5$.

The difference of the efficiency is understood by the following consideration on the energy change by the flips. Considering a given state at a finite $T$ well below $T_{\rm c}$, its energy measured from the ground-state energy is given by $E=E_J+E_b$, where $E_J$ and $E_b$ are the energies corresponding to the first and second terms in Eq. (1), respectively. Both $E_J$ and $E_b$ are of the order of $T$ at low $T$. The three loop flips change the two contributions in different ways. The flip xyz changes $E_J$ by a certain fraction $\Delta E_J$ but conserves $E_b$. Meanwhile, flip parallel and rotate change both of $E_J$ and $E_b$ by $\Delta E_J$ and $\Delta E_b$, respectively. First we consider the large $b$ limit, where $E\simeq E_b\propto T$ and $E_J/E_b\propto b^{-1}$. For flip xyz in which $\Delta E_b=0$, we obtain $\Delta E/T=\Delta E_J/T\propto b^{-1}\to0$ as $b\to\infty$. Since the acceptance rate is given by $\exp(-\Delta E/T)$, this consideration gives $\lim_{b\to+\infty}P_{xyz}\to1$, that is, flip xyz becomes rejection free as $b\to+\infty$.

This is consistent with the behavior in Fig. 3. On the contrary, flip parallel and rotate cannot become rejection free for $b \to \infty$ because they change $E_b$ by $O(T)$; $P_{\text{parallel}}$ and $P_{\text{rotate}}$ converge to finite values less than unity at $b \to \infty$, respectively. Note that rotate does not change a half of the nearest-neighbor bond energies. This may account for why $P_{\text{rotate}} > P_{\text{parallel}}$ at $b \to +\infty$.

For smaller $b$, spins deviate from the common axis $\vec{Q}$ with larger angle. Considering that $\vec{Q}$ is set by $E_b \sim T$ and $E_b$ is proportional to $b\theta^2$ ($\theta$ is a typical deviation angle), we obtain $\theta = O(\sqrt{T/b})$ for $b \ll J$ [22]. Since flip parallel changes $E_J$ and $E_b$ by $O(J\theta^4)$ and $O(b\theta^2)$, respectively [15], we obtain $\Delta E/T = \Delta E_b/T = O(1)$ at low $T \ll T_c$ for flip parallel. This indicates that $P_{\text{parallel}}$ does not vanish even at $b \to 0$ in the nematic phase. Meanwhile, the other two methods change the energy as $\Delta E/T = \Delta E_J/T = O(J\theta^2/T) = O(J/b)$ at low $T$ and $b \ll J$ [15]. This suggests that their acceptance rates vanish as $b \to 0$ in contrast to flip parallel. Therefore, flip parallel becomes most efficient at $b \to 0$. These considerations are consistent with the numerical results shown in Fig. 3. In the intermediate regime, i.e, $0.1 < b < 0.5$, rotate is superior to the other two, presumably because of a remnant of the advantage of rotate over flip parallel at $b \to \infty$.

### 4. Summary
In this paper, we have extended the loop algorithm to the classical antiferromagnetic Heisenberg spin models with biquadratic interaction which have spin-ice type ground-state degeneracy. The efficiency of the extended loop algorithm has been demonstrated in Monte Carlo simulations. We have examined three different ways of loop flips, flip xyz, flip parallel, and rotate, and compared their efficiency. We have shown that the most efficient method depends on the strength of the biquadratic interaction $b$. This $b$ dependence has been explained by considering effects of thermal fluctuations on the energy changes by the loop flips.

This work was supported by Grant-in-Aids (No. 19052008), Global COE Program "the Physical Sciences Frontier", and HPCI Strategic Program, from MEXT, Japan.

### References
[1] Landau D P and Binder K 2000 *A guide to Monte Carlo simulation in statistical physics* (Cambridge: Cambridge Univ. Press)
[2] Swendsen R H and Wang J S 1987 *Phys. Rev. Lett.* **58** 86-88
[3] Wolff U 1989 *Phys. Rev. Lett.* **62** 361-364
[4] Anderson P W 1956 *Phys. Rev.* **102** 1008-1013
[5] Bernal J D and Fowlers R H 1933 *J. Chem. Phys.* **1** 515-548
[6] Pauling L 1935 *J. Am. Chem. Soc.* **57** 2680
[7] Harris M J, Bramwell S T, McMorrow D F, Zeiske T and Godfrey K W 1997 *Phys. Rev. Lett.* **79** 2554-2557
[8] Ramirez A P, Hayashi A, Cava R J, Siddharthan R and Shastry B S 1999 *Nature* **399** 333-335
[9] Rahman A and Stillinger F H 1972 *J. Chem. Phys.* **57** 4009
[10] Yanagawa A and Nagle J F 1979 *Chem. Phys.* **43** 329
[11] Barkema G T and Newman M E J 1998 *Phys. Rev. E* **57** 1155-1166
[12] Melko R G, den Hertog B C and Gingras M J P 2001 *Phys. Rev. Lett.* **87** 067203
[13] Melko R G and Gingras M J P 2004 *J. Phys.: Condens. Matter* **16** R1277
[14] Champion J D M, Bramwell S T, Holdsworth P C W and Harris M J 2002 *Europhys. Lett.* **57** 93
[15] Shinaoka H and Motome Y 2010 *Phys. Rev. B* **82** 134420
[16] Shannon N, Penc K and Motome Y 2010 *Phys. Rev. B* **81** 184409
[17] Shinaoka H, Tomita Y and Motome Y 2011 *Phys. Rev. Lett.* **107** 047204
[18] Reimers J N 1992 *Phys. Rev. B* **45** 7287-7294
[19] Moessner R and Chalker J T 1998 *Phys. Rev. Lett.* **80** 2929-2932
[20] Moessner R and Chalker J T 1998 *Phys. Rev. B* **58** 12049-12062
[21] Marsaglia G 1972 *The Annals of Mathematical Statistics* **43** 645-646
[22] In the case of the single-ion anisotropy considered in Ref. [15], we assumed that $\theta \propto T$. It should be corrected as $\theta = O(\sqrt{T/D_1})$ ($D_1$ is the anisotropy). This, however, does not alter the arguments in the previous study.