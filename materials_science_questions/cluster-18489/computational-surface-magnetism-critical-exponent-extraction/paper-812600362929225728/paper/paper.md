![](./images/812600362929225728_1.jpg)

Computational Materials Science 10 (1998) 283-286

# Monte Carlo simulations of magnetic properties in multilayers

L. Veiller, D. Ledue*, J. Teillet

GMP Magnétisme et Applications, UMR 6634 CNRS-Université de Rouen, 76821 Mont-Saint-Aignan Cedex, France

## Abstract
A Monte Carlo method has been used to simulate Heisenberg multilayer systems $(L × L × 4 P)$ consisting of alternating $P$ ferromagnetic layers A and B with antiferromagnetic interface coupling $J_{AB}$. Finite-size effects on the specific heat and magnetisation thermal variation for two kinds of boundary conditions at the top and bottom planes are investigated. In particular, our Monte Carlo data evidence that the specific heat exhibits two peaks and a single phase transition occurs at the temperature which corresponds to the location of the high temperature peak (as $L \to \infty$). Copyright © 1998 Elsevier Science B.V.

Keywords: Heisenberg model; Monte Carlo simulation; Magnetic multilayers

## 1. Introduction
In recent years, some bilayer systems made up of alternating layers of transition metal (TM) and rare earth (RE) atoms have been extensively studied for reasons of scientific interest and technological applications [1,2]. In particular, Tb/Fe ferrimagnetic multilayers with small layer thicknesses which exhibit large perpendicular magnetic anisotropy have potential application as magneto-optical recording media [3,4]. However, most of the theoretical works related to magnetic multilayers are restricted to simple Ising or Heisenberg systems consisting of identical spin ions and very few numerical or analytical studies dealing with RE/TM magnetic properties have been published. For example, mean-field and effective- field theories have been used to study magnetic properties of RE/TM multilayers [2,5,6], but very few Monte Carlo studies deal with RE/TM multilayer systems.

In this article we examine, by Monte Carlo simulations, the temperature dependence of the specific heat and magnetisation of a magnetic multilayer system consisting of two alternating ferromagnetic materials (A and B) with different bulk properties. Finite-size effects in the case of two kinds of boundary conditions have been investigated.

## 2. Model and formulation
We consider a multilayer system in which $P$ ferromagnetic layers of materials A and B alternate. For reason of simplicity, we restrict our study to simple cubic structure. Each layer is made up of four atomic planes which are $L × L$ in cross section. Then, the total number of atoms is $N = 4 × P × L^2$.

* Corresponding author. Tel.: +33.(0)2.35.14.68.77; fax:+33.(0)2.35.14.66.52; e-mail: denis.ledue@univ-rouen.fr

0927-0256/98/$19.00 Copyright © 1998 Elsevier Science B.V. All rights reserved
PII S0927-0256(97)00122-5

The Hamiltonian for this system is given by

$$
H = -\sum_{\langle i,j \rangle} J_{ij}S_iS_j,
$$

where $S_i$ is a classical Heisenberg spin and the sum is taken over nearest-neighbour pairs of spins. $J_{ij}$ denotes nearest-neighbour exchange interaction and is assumed to be $J_{\text{AA}}(J_{\text{BB}})$ between A (B) atoms and $J_{\text{AB}}$ between different atoms at the interfaces. The exchange parameters are defined in temperature units.

In order to relate our results to real systems, such as RE/TM multilayers, we make the assumption that A and B atoms are transition metal (iron) and rare earth (terbium) like atoms, respectively. Then, the magnetic moments for A and B atoms are related to the spin momentum $S_{\text{A}}$ and the total angular momentum $J_{\text{B}}$, respectively, by

$$
\boldsymbol{m}_{\text{A}} = -g_{\text{A}}\mu_{\text{B}}S_{\text{A}},
$$

$$
\boldsymbol{m}_{\text{B}} = -g_{\text{B}}\mu_{\text{B}}J_{\text{B}} = \frac{-g_{\text{B}}}{g_{\text{B}}-1}\mu_{\text{B}}S_{\text{B}},
$$

where we assume that Landé factors $g_{\text{A}}=2$ and $g_{\text{B}}=\frac{3}{2}$, $S_{\text{A}}=1$, $S_{\text{B}}=3$ and $J_B=6$. We have considered $J_{\text{AB}}<0$, $J_{\text{AA}}>0$ and $J_{\text{BB}}>0$. The exchange interactions $J_{\text{AA}}$ and $J_{\text{BB}}$ have been estimated by Monte Carlo simulations on pure monoatomic A and B systems, respectively, so that the maximum of the specific heat is located at $T_{\text{C}}^{\text{iron}} \approx 1044$ K and $T_{\text{C}}^{\text{terbium}} \approx 220$ K. We found $J_{\text{AA}} \approx 780$ K and $J_{\text{BB}} \approx 18$ K. As usually considered for Fe-Tb alloy systems, we have taken $J_{\text{BB}} < |J_{\text{AB}}| < J_{\text{AA}}$, here $J_{\text{AB}}=-200$ K.

Simulations were performed using the importance-sampling Monte Carlo procedure based on the standard Metropolis algorithm [7] and updating the spin configuration in visiting atomic site randomly. Our data were obtained by repeating the calculations at several temperatures. In our simulations, the temperature is slowly decreased. At each temperature, the first $2 \times 10^3$ Monte Carlo steps (MCS) were discarded for equilibration before averaging over the next $78 \times 10^3$ MCS. The thermodynamic quantities of interest at each temperature are the total energy, $E(T) = -\langle\sum_{\langle i,j \rangle} J_{ij}S_iS_j\rangle$, the specific heat calculated from the fluctuations of the internal energy,
$C(T)=(\langle E^2 \rangle - \langle E \rangle^2)/(NkT^2)$, and the magnetisation per atom

$$
\begin{aligned}
m(T) =& \frac{1}{N} \left[ \left\langle \left| \sum_i m_i^x \right| \right\rangle^2 + \left\langle \left| \sum_i m_i^y \right| \right\rangle^2 \right. \\
& \left. + \left\langle \left| \sum_i m_i^z \right| \right\rangle^2 \right],
\end{aligned}
$$

where $\langle \rangle$ is the average over the MCS, i.e. thermal average at temperature $T$.

Periodic boundary conditions have been applied in the plane of the layers while two kinds of boundary conditions have been used along the perpendicular direction at the top and bottom planes: free boundary conditions (FBC) with $P=4$ to take account of free surfaces in real systems and periodic boundary conditions (PBC) with $P=2$ for a bilayer system. For a given size $N$, each data point was averaged over three runs using different starting configurations and different random number sequences. In the work reported, $N$ has been assigned various values from 576 to 28 800 spins.

## 3. Numerical results and discussion

The first aim of this paper is to study the size effects with FBC at the top and bottom planes ($P=4$). The cross sections vary from $L=6$ to $L=24$.

Specific heat profiles versus temperature are shown in Fig. 1. The temperature dependence of the specific heat exhibits two peaks, at about 220 and 960 K ($\pm 20$ K), as previously seen for Ising models [6,8]. This could suggest that two phase transitions occur. Indeed, for $J_{\text{AB}}=0$ K, the multilayer system is decomposed into four independent layers so the net specific heat is the sum of the A and B independent layers: each peak occurs near to the temperature at which a maximum would occur for each independent layer ($220$ K $\leftrightarrow$ B layers, $960$ K $\leftrightarrow$ A layers) and the system undergoes two phase transitions. However, when $J_{\text{AB}} \neq 0$ K, the maximum for the high temperature peak ($C_{\text{max}}^1$) increases and this peak narrows as $L$ increases (Fig. 1). On the contrary, the

![](./images/812600362929225728_2.jpg)

Fig. 1. Temperature dependence of the specific heat with free boundary conditions $(P=4)$ for different values of $L$. For reason of clarity, only curves for $L=6$ and $L=24$ are drawn.

low temperature peak is roughly unchanged and thus reveals only an alteration of the short range order in B layers. Owing to these facts, the transition temperature $T_{\mathrm{C}}$ of the multilayer system can be determined from the location of the high temperature specific heat peak (as $L \rightarrow \infty$) and can be estimated to about 960 K in our system.

In Fig. 2, we have plotted the thermal variation of the magnetisation per spin (only results for $L=6$ and $L=24$ are drawn). Below the transition, the magnetisation per spin tends to the expected limit value of $3.5 \mu_{\mathrm{B}}$ which corresponds to the ferromagnetic ground state. As expected, finite-size effects are responsible for a tail above the transition where spontaneous magnetisation should be zero. Moreover, these finite-size effects prevent us from observing magnetic compensation for small sizes $(L<16)$ while a compensation point can be seen for large enough sizes $(L \geq 16)$. In particular, this point is close to 500 K for the largest system $(L=24)$.

Secondly, we discuss the size effects in the case of PBC, at the top and bottom planes, on the specific heat and magnetisation $(P=2)$. The cross sections vary from $L=10$ to $L=60$.

The size effects on the two peaks are similar as for FBC, so the thermal variation of the specific heat for different values of $L$ is not shown. For comparison, we plot in Fig. 3 the thermal dependence of the specific heat for the two types of boundary conditions $(L=24)$. It can be seen that the location and the height of the high temperature peak seems to be independent of $P$ and the boundary conditions. On the other hand, with PBC, the low temperature peak is shifted to higher temperatures due to a more rapid ordering of the B sites. Indeed, the B spins of the top plane have a more reduced freedom in the PBC system than in the FBC system because of the presence of magnetically ordered A planes in the neighbouring when $T<T_{\mathrm{C}}$. This is also valid to explain that the compensation point exhibits a shift towards high temperatures $(T_{\mathrm{comp}} \sim 620 \mathrm{~K})$ for the system with PBC while $T_{\mathrm{comp}} \sim 500 \mathrm{~K}$ for the system with FBC (Fig. 4). With PBC, the magnetisation of the sublattice A is more rapidly compensated by the magnetisation of the B layer. It should be noted that PBC allow the magnetisation curve to be more regular and, therefore, the position of the compensation temperature to be determined more precisely (Fig. 4).

![](./images/812600362929225728_3.jpg)

Fig. 2. Temperature dependence of the magnetisation per atom with free boundary conditions $(P=4)$ for different values of $L$. The continuous arrow indicates the compensation point for $L=24$.

![](./images/812600362929225728_4.jpg)

Fig. 3. Comparison of the temperature dependence of the specific heat for $L=24$ with two kinds of boundary conditions applied along the perpendicular direction: open ($P=4$) or periodic ($P=2$).

In this paper, we have investigated the finite-size effects on the magnetisation and the specific heat for a Heisenberg multilayer system. Two kinds of boundary conditions have been applied along the perpendicular direction of the layers. Our results evidence that a single phase transition occurs in a Heisenberg multilayer with non-zero interface coupling and that the transition temperature is given by the location of the high temperature peak of the specific heat (as $L \to \infty$). The number of layers and the type of boundary conditions are ineffective on the location and the height of the high temperature peak. On the other hand, the effects of free surfaces are substantial concerning the low temperature peak and the determination of the compensation point. Then, it is more judicious to study magnetic properties of a bilayer with PBC and larger values of $L$ for which Monte Carlo data will be less disperse in order to estimate more accurately the transition temperature and the compensation point.

![](./images/812600362929225728_5.jpg)

Fig. 4. Comparison of the temperature dependence of the magnetisation per atom for $L=24$ with two kinds of boundary conditions applied along the perpendicular direction : open ($P=4$) or periodic ($P=2$). The arrow shows the location of the compensation point for the bilayer system with PBC.

## Acknowledgements
This study was supported in part by the Conseil Régional de Haute-Normandie.

## References
[1] S. Honda, T. Kimura and N. Nawate, J. Magn. Magn. Mater. 121 (1993) 144.
[2] S. Honda and M. Nawate, J. Magn. Magn. Mater. 136 (1994) 163.
[3] K. Yamauchi, K. Habu and N. Sato, J. Appl. Phys. 64 (1988) 5748.
[4] F. Richomme, J. Teillet, A. Fnidiki, P. Auric and Ph. Houdy, Phys. Rev. B 54 (1996) 416.
[5] T. Kaneyoshi and M. Jašcur, Physica A 203 (1994) 316.
[6] M. Jašcur and T. Kaneyoshi, J. Magn. Magn. Mater. 140-144 (1995) 488.
[7] N. Metropolis et al., J. Chem. Phys. 21 (1953) 1087.
[8] A.M. Ferrenberg and D.P. Landau, J. Appl. Phys. 70 (1991) 6215.