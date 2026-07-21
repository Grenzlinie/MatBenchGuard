# Steplike magnetization of spin chains in a triangular lattice: Monte Carlo simulations
X. Y. Yao, S. Dong, and J.-M. Liu*

Laboratory of Solid State Microstructures, Nanjing University, Nanjing 210093, China
International Center for Materials Physics, Chinese Academy of Sciences, Shenyang, China

(Received 19 March 2006; revised manuscript received 10 May 2006; published 29 June 2006)

A two-dimensional Ising-like model for a triangular spin-chain lattice, where each spin-chain is treated as a rigid giant spin, is proposed to investigate the magnetization of a triangular spin-chain lattice by Monte Carlo simulation. The simulations show the steplike evolution of the magnetization at low temperature against an external magnetic field, namely two steps above 10 K and four steps below 10 K, in quantitative agreement with experiments on a ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$ compound. It is argued that the interchain interaction and magnetic inhomogeneity of the lattice are two important ingredients to induce the intriguing steplike feature of the magnetization below 10 K.

DOI: 10.1103/PhysRevB.73.212415
PACS number(s): 75.30.Kz, 75.60.-d, 75.40.Mg

It is known that dimensionality reduction and geometrical frustration can result in fascinating physical phenomena in strongly correlated electron and spin systems. Typical examples are those compounds with well-aligned one-dimensional (1D) spin chains along the same direction, and the cross section forms a triangular lattice. They offer peculiar property and continue to attract interest. One example is ${\text{CsCoX}}_{3}$, where X is Cl or Br and both intrachain and interchain interactions are antiferromagnetic (AFM) (Ref. 1). The partially disordered antiferromagnetic (PDA) state was first observed in these compounds and a ferrimagnetic state is attained below the transition temperature.

Recently, another family of 1D spin-chain compounds with the general formula ${A}_{3}^{\prime}{\text{ABO}}_{6}$ (where $A^{\prime}$ is Ca or Sr, $A$ and $B$ are transition metal elements) have attracted attention. $^{2,3}$ They have a rhombohedral structure consisting of parallel 1D ${\text{ABO}}_{6}$ chains along the hexagonal $c$ axis, separated by $A^{\prime 2+}$ ions. $^{4}$ These chains are built by alternating and facesharing ${\text{AO}}_{6}$ trigonal prisms and ${\text{BO}}_{6}$ octahedra. Each chain is surrounded by six equally spaced chains, forming a triangular lattice in the $ab$ plane. Generally, the interchain distance is about double of the intrachain $A$-$B$ distance. Among these, ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$, as the only compound in which both $A$ and $B$ sites are occupied by the same metallic element, has been intensively studied due to its complex magnetic behaviors. $^{4-12}$ In contrast to ${\text{CsCoX}}_{3}$ (Ref. 1), the intrachain coupling in ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$ is ferromagnetic (FM) along the $c$ axis, while the interchain coupling (much weaker) in the $ab$ plane is AFM (Ref. 5). Experimental $^{6,7,12}$ and theoretical $^{13}$ investigations confirmed the strong Ising-like anisotropy of the chains. The fascinating feature observed in ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$ is a steplike magnetization $(M)$ as a function of the external magnetic field $(h)$ applied along the chains. $^{6,8,11}$ However, beside the ${M}_{0}/3$ step (where ${M}_{0}$ is the saturated $M$) observable in other materials, $^{3}$ the three substeps observed at the lower temperature $T^{6,8,11}$ were reported only for ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$, while its origin is still a matter of debate.

Theoretically, effort was made to explain those peculiar effects using different models. $^{14-16}$ Recently Kudasov $^{15}$ develop a two-dimensional (2D) Ising model to investigate the steplike magnetization by an analytical method, regarding a spin-chain as a large rigid spin and assuming a quench at $T=0$. In that paper, the fourth approximation qualitatively reproduces the four equidistant steps of the $M(h)$ curve as observed in experiments. In our work, as an approach to the 1D spin-chain magnets, we improve this 2D Ising-like model to study the multistep magnetic behaviors of a triangular lattice by Monte Carlo simulation. Our simulation results quantitatively give the variation of the $M(h)$ curve over whole $T$ range, well consistent with the experiments on ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$. And the heights of steps are demonstrated to be correlative with the inhomogeneity of the system.

As revealed experimentally, in ${\text{Ca}}_{3}{\text{Co}}_{2}{\text{O}}_{6}$ the 1D spin chains align along the $c$ axis and form a triangle lattice in the $ab$ plane. Because the intrachain FM interaction is much stronger than the interchain AFM coupling, when the temperature decreases, each ferromagnetic chain would behave like a magnetic moment, namely a rigid giant spin. Therefore, the resultant magnetic structure should have two-dimensional character, which has been evidenced by several previous investigations. $^{7,8,15}$ As an approximation, the 3D issue is reduced into a 2D triangular lattice composed of giant chain spins. It should be mentioned that the chain spins only have two equivalent projections along the chain direction due to the strong Ising-like anisotropy. Between the two nearest-neighboring spin chains only the AFM coupling is considered. In addition, considering the inhomogeneity of the system, a random exchange term ${\Delta}_{m,n}$ is taken into account. The Hamiltonian can be written as follows

$$
H = \sum_{\lbrack m,n\rbrack} (J + \Delta_{m,n})S_{m}^{e}S_{n}^{e} - h\mu_{B}g\sum_{m}S_{m}^{e}, \tag{1}
$$

$$
\Delta_{m,n} = span \cdot J \cdot RAM_{m,n}, \tag{2}
$$

where $J>0$ is the AFM interchain coupling, $S_{m}^{e}$ is the effective spin moment of a spin-chain with the value $\pm S^{e}$, $g$ is the Lande factor, and $\mu_{B}$ is Bohr magneton; $\lbrack m,n\rbrack$ denotes the summation over all the nearest-neighbor pairs; $RAM_{m,n}$ is the random number in $\lbrack-1,1\rbrack$, and $span$ represents the magnitude of random exchange term. As a rigid giant spin, $S^{e}$ should be much more than the spin moment of a magnetic ion in the chain. On the other hand, the ion spin interaction along the chain is not long ranged, so $S^{e}$ should be finite. For

<table><caption>Table I. System parameters chosen for the simulation.</caption>
<tbody>
<tr>
<td>Parameter</td>
<td>Value</td>
<td>Parameter</td>
<td>Value</td>
</tr>
<tr>
<td>$k_B$ (J/K)</td>
<td>$1.3807×10^{-23}$</td>
<td>$J$ (J)</td>
<td>$3.592×10^{-25}$</td>
</tr>
<tr>
<td>$\mu_B$ (J/T)</td>
<td>$9.274×10^{-24}$</td>
<td>$S^e$</td>
<td>32</td>
</tr>
<tr>
<td>$g$</td>
<td>2</td>
<td>$span$</td>
<td>0.15</td>
</tr>
</tbody>
</table>

different materials, $S^e$ and $J$ have different values. However, the real values of the two parameters are not available from experiments and a reasonable choice of them is judged from a quantitative comparison between the simulated results and the experimental data. The values of these parameters for the simulation are shown in Table I.

The simulation starts from an $L×L$ ($L=100$) Ising triangular lattice with periodic boundary conditions. The procedure of the simulation is described as follows. At a given $T$, the simulation starts from $h=0$ with a random spin configuration. The standard Metropolis algorithm is employed to reach the equilibrium, and then magnetization is evaluated. Afterward $h$ is raised and the simulation is performed on the state obtained before to reach a new equilibrium. This process is repeated until high field. Therefore the simulation results obtained are for equilibrium state. The final results are obtained by averaging ten independent data sets with different seeds for a random number generation.

For $Ca_3Co_2O_6$, the intrachain FM ordering of Co ions forms at $\sim$40 K. We start our simulation from 40 to 2 K. For the convenience of discussion, the $T$ range is divided into two subranges: intermediate $T$ range (40 K$\sim$10 K) and low $T$ range (10 K$\sim$2 K). The simulated $M(h)$ curves in the intermediate $T$ range are presented in Fig. 1(a), revealing two clear steps at 10 K. When $h$ increases from zero, $M$ rapidly reaches the first plateau, and then switches to $M_0$ above $h_c{\approx}3.6$ T. $M{\sim}M_0/3$ on the first plateau, resulting from the ferrimagnetic ordering of the spin chains due to the AFM interaction between the chains. The spin configuration is snapshot in Fig. 2(a) at 10 K as $h=1.8$ T on the first plateau, where the black and gray-white solid circles represent spin up and spin down, respectively, with the spin up along the direction of $h$. This configuration shows a regular ferrimagnetic structure, namely two kinds of spin chains are observed: among the three spin chains in the hexagonal unit cell, one takes spin down and is surrounded by six chains of spin up, and the other two chains are spin up with half neighbors spin up and half spin down. In other words, one of the three spin chains takes the spin down, while the other two take the spin up, leading to $M{\sim}M_0/3$. As $T$ is raised, the steps are progressively washed out due to the thermal activation. Above $T$=35 K, the $M_0/3$ plateau disappears completely and the $M$-$h$ relation is linear.

![](./images/812072202634526722_1.jpg)

FIG. 1. (Color online) $M(h)$ curves in (a) the intermediate $T$ range, and (b) the low $T$ range.

![](./images/812072202634526722_2.jpg)

FIG. 2. 40$\times$40 spin snapshots of the triangular lattice for (a) $T$=10 K, $h=1.8$ T; (b) $T$=2 K, $h=0.6$ T; (c) $T$=2 K, $h=1.8$ T, and (d) $T$=2 K, $h=3.0$ T.

Figure 1(b) demonstrates the simulated $M(h)$ curves in the low $T$ range, showing that besides the jump to $M_0$ above $h_c{\approx}3.6$ T, three magnetization substeps appear gradually with decreasing $T$. For the curve at 2 K, below $h_c{\approx}3.6$ T one observes three substeps maintaining in regular intervals of 1.2 T, namely $h_{S1}{\approx}1.2$ T and $h_{S2}{\approx}2.4$ T. The partial spin snapshots at $h$=0.6, 1.8, and 3.0 T, respectively on the three substeps at $T$=2 K, are shown in Figs. 2(b)–2(d). Different spin configurations correspond to the three substeps. On the first substep, shown in Fig. 2(b), the spin configuration consists of ferrimagnetically ordered regions as shown in Fig. 2(a) and chain-to-chain FM stripes either spin down or spin up. We denote this state as A. The spin configuration on the second substep is shown in Fig. 2(c), revealing the aggregation of the ferrimagnetically ordered regions into large regions. However, many irregular small FM regions appear too. This state is signified as B. Figure 2(d) presents the spin configuration on the third substep. The small irregular regions mentioned above connect with each other, forming spin-up FM stripes, while the majority of whole area retains the ferrimagnetic ordering. We mark this state with C.

For $Ca_3Co_2O_6$, the measured $M(h)$ curves indeed show a steplike shape. $^{6,8,11}$ At $T{\sim}10$ K, with increasing $h$, the $M(h)$ curve first presents a $M_0/3$ plateau, then jumps to $M_0$ above $h_c{\approx}3.6$ T. The ferrimagnetic spin configuration on the $M_0/3$ plateau was revealed by neutron powder diffraction.$^{5}$ As $T$ falls below 10 K, three substeps at $h_{S1}{\approx}1.2$ T and $h_{S2}{\approx}2.4$ T below $h_c{\approx}3.6$ T were observed. Our simulations

![](./images/812072202634526722_3.jpg)

FIG. 3. Simulated magnetic phase diagram. P, Fi, Fo, and DIS, are for paramagnetic, ferrimagnetic, ferromagnetic, and disordered magnetic states, respectively. A, B, and C represent the three states presented in the text.

reproduce these steps quantitatively. And it is shown in the spin snapshots from our simulation that the long-range ferri- magnetic correlation still exists below 10 K. This phenom- enon was evidenced by neutron diffraction too. $^{17}$ Therefore our model exhibits the intrinsic character of the structure. But the height of the second substep in the experiments is lower than our simulation result to some extent, which is due to the complexity of real material. The equidistance of the substeps is ascribed to the competition between the exchange interaction and magnetic field, as shown in Eq. (1). Starting from the view of the mean field, ignoring the random ex- change term $\Delta_{m, n}$ , for a spin $S_{m}^{e}$ the first item $J S_{m}^{e} \sum S_{n}^{e}$ repre sents the interaction energy and the second one $-h \mu_{B} g S_{m}^{e}$ is the magnetic field energy. These two energies compete with each other, namely $J \sum S_{n}^{e}$ vs $h \mu_{B} g$ . When one of the six nearest-neighboring spins flips, the change of $J \sum S_{n}^{e}$ is $2 J S^{e}$ . So $2 J S^{e}$ corresponds to the interval between two critical fields, which is estimated to be $h_{int }=2 J S^{e} /(g \mu_{B}) \approx 1.2 ~T$ . And the critical spin-flip fields $h_{S 1}=1 h_{int } \approx 1.2 ~T, h_{S 2}=2 h_{int }$ ≈2.4 T, h_c=3h_int≈3.6 T, resulting in the equidistant distri- bution of these critical spin-flip fields.

According to the magnetic behavior shown above, we then construct the phase diagram as shown in Fig. 3. Several domains can be distinguished, including the paramagnetic (P), ferrimagnetic (Fi), ferromagnetic (Fo) and disordered magnetic (DIS) states, which coincides well with the experiments. $^{7,8}$ In addition, the three states presented above are added to the phase diagram, marked with A, B, and C.

For the $M_{0} / 3$ plateau in the intermediate $T$ range, the ferrimagnetic scenario was confirmed in many experiments. But for the three substeps in the low $T$ range, the origin is still a matter of debate. Currently, three scenarios are pro- posed: (i) $h$ -induced transitions between different spin configurations; $^{8,15}$ (ii) quantum tunneling of the mag netization $^{12}$ ; and (iii) a combination of two relaxation pro cesses: $T$ -independent relaxation and thermally activated relaxation. $^{11}$ In our simulation, a chain is regarded as a rigid giant spin, and the spin fluctuation inside the chain is negli- gible and only the interchain interaction is considered. Even with this approximation, the complex magnetic behavior of Ca3Co2O6 can be reproduced quantitatively. So the inter- chain interaction plays an important role in determining the three substeps of magnetization below 10 K, even if this be- havior may be ascribed to a combination of several ingredi- ents.

![](./images/812072202634526722_4.jpg)

FIG. 4. (Color online) (a) 40×40 spin snapshot of the triangular lattice with span=0.05 for T=2 K and h=0.6 T. (b) M(h) curves for different span at T=2 K.

The substeps in the low $T$ range reflect the coexistence of several spin configurations, and the random exchange term in addition to $J$ enhances the inhomogeneity and consequently conduces to form different configurations. Figure 4(a) illus- trates the spin snapshot with span=0.05, corresponding to a small random exchange term, at T=2 and h=0.6 T. Compar- ing Fig. 4(a) with Fig. 2(b), besides the ferrimagnetic order- ing, regions of the other spin configurations in Fig. 2(b) oc- cupy a larger fraction than that shown in Fig. 4(a). On the other hand, as span arises from 0 to 0.5 at 2 K, the difference of $M$ between neighboring substeps increases but the borders of the substeps become more and more faint, as shown in Fig. 4(b). When span=0.5, corresponding to a large random exchange term, the three substeps are almost smeared out.The doping experiment on $Ca_{3} Co_{2} O_{6}$ shows similar results. $^{10}$  Therefore, it is argued that the inhomogeneity has an impor- tant effect on those substeps. Only when the inhomogeneity is in an appropriate range, the $M(h)$ curve in the low $T$ range shows a distinct steplike pattern.

In summary, an Ising-like model has been employed to investigate the spin-chain structure in a triangular lattice by Monte Carlo simulation. The results show the different step- like behaviors in the different temperature ranges, consistent with experimental observations on $Ca_{3} Co_{2} O_{6}$ . It is indicated that the interchain spin interaction and the inhomogeneity of the system are two important ingredients to influence the steplike feature in the low $T$ range. Although the spin-chain interactions in real materials are far more complicated, the magnetic property and microscopic spin configurations can be well explained by such a simple Ising model.

The authors thank the Natural Science Foundation of China (Grants Nos. 50332020, 10021001, 10474039) and National Key Projects for Basic Researches of China (Grants Nos. 2002CB613303, 2004CB619004).

*Corresponding author; email address: liujm@nju.edu.cn

¹M. F. Collins and O. A. Petrenko, Can. J. Phys. 75, 605 (1997).

²S. Rayaprol, K. Sengupta, and E. V. Sampathkumaran, Solid State Commun. 128, 79 (2003); V. Hardy, M. R. Lees, A. Maignan, S. Hébert, D. Flahaut, C. Martin, and D. M. Paul, J. Phys.: Con- dens. Matter 15, 5737 (2003).

³E. V. Sampathkumaran and A. Niazi, Phys. Rev. B 65, 180401(R) (2002).

⁴H. Fjellvag, E. Gulbrandsen, S. Aasland, A. Olsen, and B. C. Hauback, J. Solid State Chem. 124, 190 (1996).

⁵S. Aasland, H. Fjellvag, and B. Hauback, Solid State Commun. 101, 187 (1997).

⁶H. Kageyama, K. Yoshimura, K. Kosuge, M. Azuma, M. Takano, H. Mitamura, and T. Goto, J. Phys. Soc. Jpn. 66, 3996 (1997).

⁷H. Kageyama, K. Yoshimura, K. Kosuge, H. Mitamura, and T. Goto, J. Phys. Soc. Jpn. 66, 1607 (1997).

⁸A. Maignan, C. Michel, A. C. Masset, C. Martin, and B. Raveau, Eur. Phys. J. B 15, 657 (2000).

⁹B. Martínez, V. Laukhin, M. Hernando, J. Fontcuberta, M. Parras, and J. M. González-Calbet, Phys. Rev. B 64, 012417 (2001); B. Raquet, M. N. Baibich, J. M. Broto, H. Rakoto, S. Lambert, and A. Maignan, Phys. Rev. B 65, 104442 (2002); E. V. Sampath- kumaran, N. Fujiwara, S. Rayaprol, P. K. Madhu, and Y. Uwa- toko, Phys. Rev. B 70, 014437 (2004); O. A. Petrenko, J. Wool- dridge, M. R. Lees, P. Manuel, and V. Hardy, Eur. Phys. J. B 47, 79 (2005).

¹⁰D. Flahaut, A. Maignan, S. Hebert, C. Martin, R. Retoux, and V. Hardy, Phys. Rev. B 70, 094418 (2004).

¹¹V. Hardy, M. R. Lees, O. A. Petrenko, D. M. K. Paul, D. Flahaut, S. Hébert, and A. Maignan, Phys. Rev. B 70, 064424 (2004).

¹²A. Maignan, V. Hardy, S. Hebert, M. Drillon, M. R. Lees, O. Petrenko, D. M. K. Paul, and D. Khomskii, J. Mater. Chem. 14, 1231 (2004).

¹³H. Wu, M. W. Haverkort, Z. Hu, D. I. Khomskii, and L. H. Tjeng, Phys. Rev. Lett. 95, 186401 (2005).

¹⁴S. Miyashita, J. Phys. Soc. Jpn. 55, 3605 (1986).

¹⁵Y. B. Kudasov, Phys. Rev. Lett. 96, 027212 (2006).

¹⁶E. Kim, B. Kim, and S. J. Lee, Phys. Rev. E 68, 066127 (2003).

¹⁷H. Kageyama, K. Yoshimura, K. Kosuge, X. Xu, and S. Kawano, J. Phys. Soc. Jpn. 67, 357 (1998).