Modern Physics Letters B, Vol. 12, No. 27 (1998) 1125–1132
© World Scientific Publishing Company

# STABILITY AND SPIN DENSITY IN DOPED QUASI-ONE-DIMENSIONAL NON-CONJUGATED ORGANIC FERROMAGNETS

K. L. YAO

CCAST (World Laboratory), P.O. Box 8730, Beijing 100080, and Department of Physics, Huazhong University of Science and Technology, Wuhan 430074, People's Republic of China

M. ZHAO and Z. L. LIU

Department of Physics, Huazhong University of Science and Technology, Wuhan 430074, People's Republic of China

Received 21 October 1998

The effects of polarons on the stability of ferromagnetic state in doped quasi-one- dimensional non-conjugated organic ferromagnets are investigated. It is shown that spin density wave of doped main chain near the polaron appears amplitude distortion which changes the stability of the ferromagnetic state. If the spins of polarons along the main chain are contrary to those of side radicals' electrons, the stability of the ferromagnetic state will be strengthened. Under the opposite condition, the stability will be weakened.

PACS Number(s): 75.30.Ds, 71.20.Hk

## 1. Introduction

Organic ferromagnets have attracted more and more interest from both experi- mentalists and theorists, the search for the origin of ferromagnetism in organic ferromagnets has become a challenge. $^{1-4}$ Ovchinnikov and Spector $^{2}$ developed a simplified model to describe the ferromagnetic ordering in organic materials. The main chain consists of carbon atoms each with a $\pi$ -electron and R is a kind of side radicals containing an unpaired electron. Considering the itineracy of $\pi$ -electrons, the Hubbard electron-electron correlation, electron-phonon coupling and the anti- ferromagnetic spin correlation between $\pi$ -electrons and side radicals electrons, Fang et al. $^{5}$ obtained a ferromagnetic ground state, in which a parallel spin arrangement of the unpaired electrons at side free-radical can be gained and there exists an antiferromagnetic spin density wave along the main chain.

However, in their work, the system was treated as a pure chain. Researches in recent years showed that the physical properties of conjugated polymers change drastically upon addition of donors or acceptors. $^{6-10}$ This has been discussed by con sidering additional electrons or holes in the electronic structure of the undoped ma-

terial and has led to the concept of nonlinear solitonic excitations in these systems.¹¹
As they are simi low-dimensional materials, we need consider these impurities in the organic ferromagnetic system. The purpose of this paper is to investigate effects of additional electrons on doped organic ferromagnets, with help of self-consistent method. In this work, we make some simplifications. We consider such a case that during the doping process the electrons transfer from impurity ions to the main chain and become π-electrons. One chain of organic ferromagnet is doped with an additional electron. Because of the split of energy levels of π-electrons with different spins in ferromagnetic system, we will discuss the effects of injecting electrons with different spins on the ferromagnetic state of the system.

## 2. The Model Hamiltonian and Numerical Method

The Hamiltonian of the system is studied is given by:

$$
\begin{aligned}
H = & -\sum_{i,\sigma}[t_0 + \gamma(U_i - U_{i+1})](C_{i+1,\sigma}^+ C_{i,\sigma} + \text{H.c.}) + \frac{K}{2} \sum_{i}(U_i - U_{i+1})^2 \\
& + U \sum_{i} n_{i\alpha} n_{i\beta} + J_f \sum_{i} \delta_i S_{i\mathrm{R}} \cdot S_i,
\end{aligned}
\tag{1}
$$

where $t_0, \gamma$ and $K$ have the same conventional meanings as in the SSH model. $i$ labels the $i$th lattice site, $C_{i,\sigma}^+$ and $C_{i,\sigma}$ are the creation and the annihilation operator for a $\pi$-electron with spin $\sigma$ on the $i$th site. $\sigma = (\alpha, \beta)$ labels the direction of spin, where $\alpha$ and $\beta$ denote up-spin and down-spin respectively. $U$ is the Hubbard repulsion term and $n_{i\sigma} = c_{i\sigma}^+ c_{i\sigma}$. $J_f$ is the coupling constant between the spin $\mathbf{S}_i$ of $\pi$-electrons and the residual spin $\mathbf{S}_{i\mathrm{R}}$ of the R radical. Here $\delta_i$ defines the connections of the side radicals. We assume that the side radicals connect with the odd carbon atoms, then $\delta_l = 1$ for odd sites and $\delta_l = 0$ for even sites.

We use the mean-field approximation to divide $n_{i\sigma}$ and $S_{i\mathrm{R}}^z$ as follows⁵:

$$
n_{i\sigma} = \langle n_{i\sigma} \rangle + \Delta n_{i\sigma}, \quad S_{i\mathrm{R}}^z = \langle S_{i\mathrm{R}}^z \rangle + \Delta S_{i\mathrm{R}}^z.
\tag{2}
$$

Here $\langle \cdots \rangle = \langle G | \cdots | G \rangle$ is the average with respect to the ground state $|G\rangle$, $\Delta n_{i\sigma}$ and $\Delta S_{i\mathrm{R}}^z$ are fluctuations from the average values.

In order to minimize the total energy in our self-consistent calculation, it is convenient to cast all quantities into dimensionless forms as:

$$
h = \frac{H}{t_0}, \quad u = \frac{U}{t_0}, \quad j_f = \frac{J_f}{t_0}, \quad \lambda = \frac{2\gamma^2}{\pi t_0 K}, \quad y_i = (-1)^i \frac{Y}{t_0} (U_i - U_{i+1}). \quad (3)
$$

Then using the self-consistent iterative method, we can obtain the eigenenergies $\varepsilon_\mu^\sigma$, the expansion coefficient $Z_{\mu,i}^\sigma$ and the optimized geometry $y_i$ from the following

self-consistent equations:

$$
\begin{aligned}
& -\left[1+(-1)^{i} y_{i}\right] Z_{\mu, i+1}^{\alpha}-\left[1+(-1)^{i-1} y_{i-1}\right] Z_{\mu, i-1}^{\alpha}+\left[u \sum_{\substack{\mu^{\prime} \\
(\mathrm{occ})}} Z_{\mu^{\prime}, i}^{\beta^{*}} Z_{\mu^{\prime}, i}^{\beta}+\frac{j_{f} \delta_{i}\left\langle S_{i \mathrm{R}}^{z}\right\rangle}{2}\right] \\
& \quad \times Z_{\mu, i}^{\alpha}=\varepsilon_{\mu}^{\alpha} Z_{\mu, i}^{\alpha},
\end{aligned}
$$

$$
\begin{aligned}
& -\left[1+(-1)^{i} y_{i}\right] Z_{\mu, i+1}^{\beta}-\left[1+(-1)^{i-1} y_{i-1}\right] Z_{\mu, i-1}^{\beta}+\left[u \sum_{\substack{\mu^{\prime} \\
(\mathrm{occ})}} Z_{\mu^{\prime}, i}^{\alpha^{*}} Z_{\mu^{\prime}, i}^{\alpha}-\frac{j_{f} \delta_{i}\left\langle S_{i \mathrm{R}}^{z}\right\rangle}{2}\right] \\
& \quad \times Z_{\mu, i}^{\beta}=\varepsilon_{\mu}^{\beta} Z_{\mu, i}^{\beta},
\end{aligned}
$$

$$
y_{i}=\pi \lambda(-1)^{i}\left[\sum_{\substack{\mu, \sigma \\
(\mathrm{occ})}} Z_{\mu^{\prime}, i}^{\sigma^{*}} Z_{\mu^{\prime}, i+1}^{\sigma}-\frac{1}{N} \sum_{i} \sum_{\substack{\mu, \sigma \\
(\mathrm{occ})}} Z_{\mu^{\prime}, i}^{\sigma^{*}} Z_{\mu^{\prime}, i+1}^{\sigma}\right].
$$

Here, periodic boundary conditions are used, and (occ) means those states occupied by electrons. New values of the dimerization order parameter $y_{i}$ are calculated by minimizing the total energy $E(y_{i})$ of the system with respect to $y_{i}$

$$
\begin{aligned}
E\left(y_{i}\right)= & -\sum_{\substack{i, \sigma \\
(\mathrm{occ})}}\left\{\left[1+(-1)^{i} y_{i}\right] \sum_{\substack{\mu \\
(\mathrm{occ})}} Z_{\mu, i+1}^{\sigma^{*}} Z_{\mu, i}^{\sigma}+Z_{\mu, i}^{\sigma^{*}} Z_{\mu, i+1}^{\sigma}\right\}+\frac{1}{\lambda \pi} \sum_{i} y_{i}^{2} \\
& +u \sum_{i} \sum_{\substack{\mu \\
(\mathrm{occ})}} \sum_{\substack{\mu^{\prime} \\
(\mathrm{occ})}}\left|Z_{\mu, i}^{\alpha}\right|^{2}\left|Z_{\mu^{\prime}, i}^{\beta}\right|^{2}+\sum_{i} \sum_{\substack{\mu \\
(\mathrm{occ})}} \frac{j_{f} \delta_{i}\left\langle S_{i \mathrm{R}}^{z}\right\rangle}{2}\left[\left|Z_{\mu, i}^{\alpha}\right|^{2}-\left|Z_{\mu, i}^{\beta}\right|^{2}\right].
\end{aligned}
$$

The distribution of spin density $\delta n_{i}$ and charge density $\left\langle n_{i}\right\rangle$ of $\pi$-electrons and unpaired electron at side radicals can be obtained self-consistently as:

$$
\left\langle n_{i}\right\rangle=\left\langle n_{i}^{\alpha}\right\rangle+\left\langle n_{i}^{\beta}\right\rangle=\sum_{\substack{\mu, \sigma \\
(\mathrm{occ})}} Z_{\mu, i}^{\sigma} Z_{\mu, i}^{\sigma^{*}},
$$

$$
\delta n_{i}=\frac{1}{2}\left(\left\langle n_{i}^{\alpha}\right\rangle-\left\langle n_{i}^{\beta}\right\rangle\right)=\frac{1}{2}\left(\sum_{i} \sum_{\substack{\mu \\
(\mathrm{occ})}}\left|Z_{\mu, i}^{\alpha}\right|^{2}-\left|Z_{\mu, i}^{\beta}\right|^{2}\right).
$$

The starting geometry in the iterative optimization process is usually the one with zero dimerization and $\langle n_i^\alpha \rangle = \langle n_i^\beta \rangle = 1/2$. The stability of the optimized geometry is always tested by using another starting configuration and performing the optimization once again.

## 3. Results and Discussion
In the following calculation, we will consider a chain$^5$ of an organic ferromagnet that contains 80 carbons along the main chain and 40 side radicals. Additionally, we consider a case where the chain is doped with one donor electron: injecting one electron into the neutral main chain. $S=(1/2,-1/2)$ labels the spin of the donor electron. From Eqs. (4)-(6), we know that the eigenvalue equation is unsymmetrical about spin owing to the Hubbard electron-electron repulsion and the antiferromagnetic correlation between $\pi$-electrons and unpaired electrons at the side radicals. So in this system, the spin degeneracy has been lifted, and we must solve the system with the different spin donor electron. In numerical studies, there are two the parameters $\lambda$ and $u$. Since the main chain of this network is the same as that of polyacetylene, we can estimate the parameters with parameters of polyacetylene as $\lambda=0.0\sim0.3$ and $u=0.0\sim4.0.^{11}$ Here we assume $t_0=2.5$ eV, $\lambda=0.25$ and $u=0.8$.

First, we discuss effects of donor electrons on the stability of the ferromagnetic state of the system. Fang *et al.* found that when $j_j\neq0.0$, the total energy of the ground state system monotonously decreases with the increasing of $\langle S_{i\mathrm{R}}^z \rangle$ and reaches the lowest when $\langle S_{i\mathrm{R}}^z \rangle=\pm1/2$ (see Fig. 1(a)). So if $j_j\neq0.0$, the ground state is a ferromagnetic state. These results are based on a neutral chain. We find that the ferromagnetic state of doping system differs from that of neutral system. Figures 1(b) and 1(c) respectively show the total energy of doping system versus $\langle S_{i\mathrm{R}}^z \rangle$ under conditions of $S=-1/2$ and $S=1/2$. From Fig. 1(b), we can see that curves of doping system is similar to that of ground state system, only the former changes more quickly than the latter. So this doping system is also a ferromagnetic state and steadier than the ground state system. From Fig. 1(c), we can see that when $j_f$ is bigger, the change trend of curves is similar to that in Figs. 1(a) and 1(b). So this doping system must also be a ferromagnetic state system though its stability is weaker than that of the others. But when $j_f$ is smaller, the change trend is not monotonous and the doping system is no longer a ferromagnetic state.

Then, why are there the differences between the ground state system and the doping system? When the organic ferromagnet gains a donor electron, like doped polyacetylene, a polaron is excited along the main chain. It is the polaron that leads to these changes of ferromagnetic state of system. We suppose the system is ferromagnetic state ($\langle S_{i\mathrm{R}}^z \rangle=1/2$), the SDW of pure system distributes along the main chain equally. But under the influence of the polaron, SDW of doped main chain near the polaron appears amplitude distortion. Because the exchange interaction between the unpaired electrons at side free-radicals is realized through

![](./images/812384727498489858_1.jpg)

Fig. 1. The total energy of the system (a) without the donor electron versus $\langle S_{i\mathrm{R}}^{z}\rangle$ with different $j_{f}$; (b) with a donor electron $(S=-1/2)$ versus $\langle S_{i\mathrm{R}}^{z}\rangle$ with different $j_{f}$; (c) with a donor electron $(S=1/2)$ versus $\langle S_{i\mathrm{R}}^{z}\rangle$ with different $j_{f}$.

![](./images/812384727498489858_2.jpg)

![](./images/812384727498489858_3.jpg)

Fig. 2. The polaron along main chain with different $j_f$. Curves $\alpha$, $\beta$ and $\gamma$ correspond to $j_f = 0.2$,
0.3, 0.5, respectively.

SDW, then the distortion of SDW will change the exchange interaction and the ferromagnetic state of the system.

In the last section, we will discuss effects of $j_f$, the exchange between $\pi$-electrons and the unpaired electrons at side free-radicals, on the polaron and the stability of doped ferromagnetic system. We find that the depth and width of the polaron hardly change with different $j_f$ (see Fig. 2), but the energy levels of polaron change. $\Delta E_1$, the energy level difference between polarons with opposite spins, increases with the increasing of $j_f$. We can describe the stability of doped ferromagnetic system with the energy difference $\Delta E_2$ of ferromagnetic state $(\langle S_{iR}^z\rangle=1/2)$ and non-ferromagnetic state $(\langle S_{iR}^z\rangle=0)$ of the system. Here we use $\Delta E_2^\beta$ and $\Delta E_2^\alpha$ to represent this kind of energy difference of doped system: $S=-1/2$ and $S=1/2$ respectively. Figure 3 shows that they both increase with the increasing of $j_f$. So the stability of ferromagnetic system strengthens with the increasing $j_f$. In addition, the calculatio shows that when $j_f$ is a constant, $\Delta E_2^\beta-\Delta E_2^\alpha=\Delta E_1$.

![](./images/812384727498489858_4.jpg)

Fig. 3. The energy difference of ferromagnetic state and non-ferromagnetic state of the doped system versus $j_f$. Curves $\alpha,\beta$ correspond to $S=-1/2$ and $S=1/2$, respectively.

In the above calculations, the system is supposed to be the ferromagnetic state with $\langle S_{iR}^z\rangle=1/2$. If the system is the ferromagnetic state with $\langle S_{iR}^z\rangle=-1/2$, the result will be similar but the effects of two kinds of spins donor electron is reversed.

In summary, the polarons with different spins have opposite effects on the stability of the organic ferromagnetic system: If the spins of polarons along the main

chain are contrary to those of side radicals' electrons, the stability of the ferromag- netic state will be strengthened. Under the opposite condition, the stability will be weakened. In addition, the stability of doped ferromagnetic system increases with the increasing of $j_{f}$.

Acknowledgment

This work is supported by the National Natural Science Foundation of China under the grant No. 19777101 and 19774023.

References

1. H. Iwamura, T. Sugawara, K. Itoh and T. Takui, *Mol. Cryst. Liq. Cryst.* **125**, 379 (1985).
2. M. Takahashi *et al.*, *Phys. Rev. Lett.* **67**, 746 (1991).
3. K. Nasu, *Phys. Rev.* **B33**, 330 (1986).
4. A. A. Ovchinnikov and V. N. Spector, *Synth. Met.* **27**, B615 (1988).
5. Z. Fang, Z. L. Liu and K. L. Yao, *Phys. Rev.* **B49**, 3916 (1994).
6. G. W. Bryant and A. J. Glick, *Phys. Rev.* **B26**, 5855 (1982).
7. E. M. Conwell and S. Jeyadev, *Phys. Rev. Lett.* **61**, 361 (1988).
8. E. M. Conwell, H. A. Mizes and S. Jeyadev, *Phys. Rev.* **B40**, 1630 (1989).
9. R. J. Cohen and A. J. Glick, *Phys. Rev.* **B42**, 7659 (1990).
10. J. Voit, *Phys. Rev. Lett.* **64**, 323 (1990).
11. A. J. Heeger, S. Kivelson, J. R. Schrieffer and W. P. Su, *Rev. Mod. Phys.* **60**, 781 (1988).