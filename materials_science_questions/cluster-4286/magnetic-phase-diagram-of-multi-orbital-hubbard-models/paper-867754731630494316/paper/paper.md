# Correlation Effects on Antiferromagnetism in Fe Pnictides

Katsunori KUBO¹ and Peter THALMEIER²

¹Advanced Science Research Center, Japan Atomic Energy Agency, Tokai, Ibaraki 319-1195
²Max Planck Institute for Chemical Physics of Solids, 01187 Dresden, Germany

To investigate correlation effects on antiferromagnetic order in Fe pnictides, we apply a variational Monte Carlo method to a two-orbital model. We obtain a small ordered moment consistent with experimental observations even for a Coulomb interaction comparable to the band width. Studies of estimation of the Coulomb interaction for Fe pnictides suggest values comparable to or slightly smaller than the band width, and much larger ordered moments have been obtained by the Hartree-Fock approximation for such a large Coulomb interaction. Thus, the correlation effect is important for Fe pnictides at least quantitatively.

KEYWORDS: iron pnictides, variational Monte Carlo method, magnetic order

The discovery of superconductivity in ${\rm LaFeAsO_{1-x}F_x}$ with a high transition temperature $T_c=26\ {\rm K}^{1)}$ has stimulated extensive and intensive studies on Fe pnictides. Superconductivity takes place around the magnetic phase boundaries¹⁻⁵) as in high-$T_c$ cuprates. Such a similarity suggests that magnetism is playing an important role in the emergence of superconductivity, and it is highly desirable to unveil the microscopic origin of magnetism characteristic to Fe pnictides.

To unveil the magnetism in Fe pnictides, the present authors applied Hartree-Fock approximation⁶) to a two-orbital model.⁷) The results are summarized as follows. The antiferromagnetic order with ordering vector $(\pi,0)$, in the unfolded Brillouin zone with one Fe ion per unit cell, is stabilized by the nesting between hole and electron pockets. This antiferromagnetic state inevitably accompanies ferro-orbital order, since the ordering with $(\pi,0)$ breaks the equivalence of $x$ and $y$ directions, and as a result, the occupancies of $d_{zx}$ and $d_{yz}$ orbitals become different. Under such ferro-orbital order, the lattice should be distorted from a tetragonal to orthorhombic structure through an electron-lattice interaction. Even in the antiferromagnetic state, a band gap does not open at some points in the Brillouin zone due to multiorbital nature of the bands. Therefore the system remains metallic in the ordered state. These results are consistent with experimental observations of magnetic order with $(\pi,0)$, lattice distortion, and metallic conductivity.

However, in our previous Hartree-Fock result, the ordered moment is large in contradiction with experimental observations,⁵,⁸⁻¹⁴) if we take a large Coulomb interaction comparable to the band width. Studies of estimation of the Coulomb interaction for Fe pnictides suggest values comparable to¹⁵) or slightly smaller than¹⁶) the band width. For such large values of Coulomb interactions correlation effects beyond the Hartree-Fock approximation may be important. In particular, correlation effects are expected to reduce the magnitude of the ordered moment. Indeed, importance of the correlation effects is discussed for a three-orbital model by using a Gutzwiller approximation.¹⁷)

In this paper, we investigate correlation effects on magnetism by applying a variational Monte Carlo (VMC) method to the two-orbital model. While the VMC method has been applied to a five-orbital model with a partially-projected Gutzwiller wavefunction,¹⁸) only Fermi-surface distortion and superconductivity are discussed there. In the VMC method, we consider a Gutzwiller-projected wavefunction as a variational wavefunction. We show that this wavefunction contains substantial correlation effects beyond the Hartree-Fock approximation while this wavefunction is simple enough for numerical calculation.

In the two-orbital model, we consider a square lattice of Fe ions with $d_{zx}$ and $d_{yz}$ orbitals.⁷,¹⁹) The model Hamiltonian is given by
$$
\begin{aligned}
H =& \sum_{\boldsymbol{k},\tau,\tau',\sigma} \epsilon_{\boldsymbol{k}\tau\tau'} c_{\boldsymbol{k}\tau\sigma}^{\dagger} c_{\boldsymbol{k}\tau'\sigma} + U \sum_{i,\tau} n_{i\tau\uparrow} n_{i\tau\downarrow} \\
&+ U' \sum_{i} n_{ix} n_{iy} + J \sum_{i,\sigma,\sigma'} c_{ix\sigma}^{\dagger} c_{iy\sigma'}^{\dagger} c_{ix\sigma'} c_{iy\sigma} \\
&+ J' \sum_{i,\tau\neq\tau'} c_{i\tau\uparrow}^{\dagger} c_{i\tau\downarrow}^{\dagger} c_{i\tau'\downarrow} c_{i\tau'\uparrow},
\end{aligned} \quad (1)
$$
where $c_{i\tau\sigma}$ is the annihilation operator of the electron at site $i$ with orbital $\tau$ and spin $\sigma$ ($=\uparrow$ or $\downarrow$) and $c_{\boldsymbol{k}\tau\sigma}$ is the Fourier transform of $c_{i\tau\sigma}$. The orbital indices $\tau=x$ and $y$ represent $d_{zx}$ and $d_{yz}$ orbitals, respectively. The number operators are defined by $n_{i\tau\sigma}=c_{i\tau\sigma}^{\dagger} c_{i\tau\sigma}$ and $n_{i\tau}=\sum_{\sigma} n_{i\tau\sigma}$. The coupling constants $U$, $U'$, $J$, and $J'$ denote the intraorbital Coulomb, interorbital Coulomb, exchange, and pair-hopping interactions, respectively. The relations $U=U'+J+J'$ and $J=J'$ hold for the $t_{2g}$ orbitals,²⁰) and we use them. We use the hopping parameters proposed by Raghu et al.⁷) and the coefficients in the kinetic energy terms are given by $\epsilon_{\boldsymbol{k}xx}=-2t_1\cos k_x-2t_2\cos k_y-4t_3\cos k_x\cos k_y$, $\epsilon_{\boldsymbol{k}yy}=-2t_2\cos k_x-2t_1\cos k_y-4t_3\cos k_x\cos k_y$, and $\epsilon_{\boldsymbol{k}xy}=\epsilon_{\boldsymbol{k}yx}=-4t_4\sin k_x\sin k_y$, where $t_1=-t$, $t_2=1.3t$, $t_3=t_4=-0.85t$, and we have set the lattice constant unity. The band width is $W=12t$.

We consider the variational wave function given by
$$
|\Psi\rangle=P_{\rm G}|\Phi\rangle=\prod_{i\gamma}[1-(1-g_{\gamma})|i\gamma\rangle\langle i\gamma|]|\Phi\rangle, \quad (2)
$$
where $P_{\rm G}$ is the Gutzwiller projection operator for onsite density correlation.²¹⁻²⁴) $|i\gamma\rangle\langle i\gamma|$ denotes projection onto the

state $\gamma$ at site $i$ and $g_\gamma$ is the variational parameter controlling the probability of state $\gamma$. There are sixteen states at each site in the present two-orbital model. The Hartree-Fock type wave function $|\Phi\rangle$, which describes a charge, spin, orbital, and spin-orbital coupled ordered state, is given by
$$
|\Phi\rangle=\prod_{k a \tau \sigma} b_{\boldsymbol{k} \tau \sigma}^{(a) \dagger}|0\rangle,\tag{3}
$$
where $a$ is a band index and $|0\rangle$ is the vacuum. The quasiparticles occupy $N_\sigma$ states for each spin $\sigma$ from the lowest quasiparticle energy state, where $N_\sigma$ is the number of electrons with spin $\sigma$. Here we consider a half-filled case, and we set $N_\uparrow=N_\downarrow=N$, where $N$ is the number of the lattice sites. The quasiparticle states are obtained by diagonalizing the following $4 \times 4$ matrix:
$$
\begin{aligned}
& \left(\begin{array}{cccc}
\epsilon_{\boldsymbol{k} x x} & \epsilon_{\boldsymbol{k} x y} & 0 & 0 \\
\epsilon_{\boldsymbol{k} y x} & \epsilon_{\boldsymbol{k} y y} & 0 & 0 \\
0 & 0 & \epsilon_{\boldsymbol{k}+\boldsymbol{Q} x x} & \epsilon_{\boldsymbol{k}+\boldsymbol{Q} x y} \\
0 & 0 & \epsilon_{\boldsymbol{k}+\boldsymbol{Q} y x} & \epsilon_{\boldsymbol{k}+\boldsymbol{Q} y y}
\end{array}\right) \\
& -\left(\begin{array}{cccc}
\Delta_{x \sigma} & 0 & \Delta_{x \sigma \boldsymbol{Q}} & 0 \\
0 & \Delta_{y \sigma} & 0 & \Delta_{y \sigma \boldsymbol{Q}} \\
\Delta_{x \sigma \boldsymbol{Q}} & 0 & \Delta_{x \sigma} & 0 \\
0 & \Delta_{y \sigma \boldsymbol{Q}} & 0 & \Delta_{y \sigma}
\end{array}\right),
\end{aligned}\tag{4}
$$
where $\boldsymbol{Q}=(\pi, 0)$ is the ordering vector. The quasiparticle gap in the ordered state is given by
$$
\Delta_{\tau \sigma}=\Delta_{\mathrm{o}}\left(\delta_{\tau x}-\delta_{\tau y}\right)+\Delta_{\mathrm{so}}\left(\delta_{\sigma \uparrow}-\delta_{\sigma \downarrow}\right)\left(\delta_{\tau x}-\delta_{\tau y}\right),\tag{5}
$$
$$
\begin{aligned}
\Delta_{\tau \sigma \boldsymbol{Q}}= & \Delta_{\mathrm{c} \boldsymbol{Q}}+\Delta_{\mathrm{s} \boldsymbol{Q}}\left(\delta_{\sigma \uparrow}-\delta_{\sigma \downarrow}\right)+\Delta_{\mathrm{o} \boldsymbol{Q}}\left(\delta_{\tau x}-\delta_{\tau y}\right) \\
& +\Delta_{\mathrm{so} \boldsymbol{Q}}\left(\delta_{\sigma \uparrow}-\delta_{\sigma \downarrow}\right)\left(\delta_{\tau x}-\delta_{\tau y}\right),
\end{aligned}\tag{6}
$$
where $\Delta_{\mathrm{o}}$ and $\Delta_{\mathrm{so}}$ denote the gaps for uniform orbital and spin-orbital ordered states, respectively. $\Delta_{\mathrm{c} Q}, \Delta_{\mathrm{s} Q}, \Delta_{\mathrm{o} Q}$, and $\Delta_{\mathrm{so} Q}$ denote the gaps for antiferro-ordered states of charge, spin, orbital, and spin-orbital, respectively. We also take them as variational parameters.

For this variational wavefunction, we evaluate energy by the Monte Carlo method, and optimize variational parameters to find the state which has the lowest energy. We set all $\Delta_{\tau \sigma}$ and $\Delta_{\tau \sigma Q}$ zero to evaluate energy of the paramagnetic state, that is, we optimize only Gutzwiller parameters $g_\gamma$. For the antiferromagnetic state, we also vary $\Delta_{\mathrm{o}}, \Delta_{\mathrm{s} Q}$, and $\Delta_{\mathrm{so} Q}$. We also evaluated energy by varying all $\Delta_{\tau \sigma}$ and $\Delta_{\tau \sigma Q}$ for some values of $U$, but we could not find a solution which has lower energy than the antiferromagnetic state. The calculations are done for an $8 \times 8$ lattice with an antiperiodic boundary condition for both directions.

Figure 1 shows energy as functions of $U$ obtained with the Hartree-Fock approximation $^{6)}$ and the present VMC method. The energy is lowered by the correlation effects beyond the Hartree-Fock approximation.

Figure 2 shows the ground state energy as a function of $U$ measured from that of the paramagnetic state. The transition from the paramagnetic state to the antiferromagnetic state occurs at $U \gtrsim 7 t$. If the energy difference is proportional to $U^2$ around the transition it is of second order, and if the energy difference is proportional to $U$ the transition is first order. However, it is difficult to distinguish a second order transition from a weak first order transition as is obtained by the Hartree-Fock approximation $^{6)}$ from the present results due to numerical accuracy.

![](./images/867754731630494316_1.jpg)

Fig. 1. (Color online) Energy $E$ as functions of the Coulomb interaction with $J=0.1 U$ obtained with the Hartree-Fock approximation $^{6)}$ and the VMC method.

![](./images/867754731630494316_2.jpg)

Fig. 2. (Color online) Energy $E_{\mathrm{AF}}$ of the antiferromagnetic ground state measured from energy $E_{\text {para }}$ of the paramagnetic state as a function of $U$ with $J=0.1 U$.

Figure 3 shows the ordered magnetic moment $m_{\mathrm{s} Q}$ evaluated for the optimized wavefunction. $m_{\mathrm{s} Q}$ is defined as
$$
m_{\mathrm{s} \boldsymbol{Q}}=\frac{1}{N} \sum_{i \tau} \mathrm{e}^{\mathrm{i} \boldsymbol{Q} \cdot \boldsymbol{r}_{i}}\left\langle n_{i \tau \uparrow}-n_{i \tau \downarrow}\right\rangle,\tag{7}
$$
where $\boldsymbol{r}_{i}$ denotes the position of site $i$ and $\langle\cdots\rangle$ represents the expectation value. To check the finite size effect of the model, we also show the results for a $10 \times 10$ lattice. The finite size effect on $m_{\mathrm{s} Q}$ is weak in particular for the large $m_{\mathrm{s} Q}$ region. In the result of the Hartree-Fock approximation, there is a small but finite jump in $m_{\mathrm{s} Q},{ }^{6)}$ while it is invisible in the scale of Fig. 3. For the results of the VMC, as in the energy difference, it is difficult to determine whether the transition is first order or second order. If it is a first order transition, the jump in the magnetic moment at the transition is very small. The ordered moment is not large for $U \lesssim 9 t$. By comparing the results by the Hartree-Fock approximation and the present

![](./images/867754731630494316_3.jpg)

Fig. 3. (Color online) Ordered moment $m_{s Q}$ in the antiferromagnetic ground state as functions of $U$ with $J=0.1 U$ obtained with the Hartree-Fock approximation⁶) and the VMC method. Note that if a fully polarized state is realized, it has $m_{s Q}=2$.

VMC results, we conclude that the correlation effect strongly reduces the value of the ordered moment and such an effect is important for Fe pnictides.

Around $U=9.6 t$, we find another phase transition within the antiferromagnetic phase. This phase transition is of first order and it is probably a metal to insulator transition, since the energy gain by the kinetic energy is reduced at $U \gtrsim 9.6 t$ (not shown).

We have also searched for a ferro-orbital ordered state without antiferromagnetic order, that is, the gap parameters are set zero except for $\Delta_{\mathrm{o}}$, but we could not find such a state as a ground state. In the antiferromagnetic state, the order parameter $m_{\mathrm{o}}=(1 / N) \sum_{i \sigma}\left\langle n_{i x \sigma}-n_{i y \sigma}\right\rangle$ for the ferro-orbital order becomes also finite due to symmetry lowering. However, the values are too small and we cannot determine $m_{\mathrm{o}}$ confidently due to our numerical accuracy.

To summarize, we have applied the variational Monte Carlo method to a two-orbital model to investigate correlation effects. Then, we have found that the ordered moment in the antiferromagnetic state is strongly suppressed by the correlation effect. Thus, to obtain a small ordered moment as in experimental observations, for $U \lesssim W$, we should take correlation effect into account properly.

1) Y. Kamihara, T. Watanabe, M. Hirano, and H. Hosono: J. Am. Chem. Soc. 130 (2008) 3296.
2) M. Rotter, M. Pangerl, M. Tegel, and D. Johrendt: Angew. Chem., Int. Ed. 47 (2008) 7949.
3) H. Kotegawa, H. Sugawara, and H. Tou: J. Phys. Soc. Jpn. 78 (2008) 013709.
4) J.-H. Chu, J. G. Analytis, C. Kucharczyk, and I. R. Fisher: Phys. Rev. B 79 (2009) 014506.
5) H. Luetkens, H.-H. Klauss, M. Kraken, F. J. Litterst, T. Dellmann, R. Klingeler, C. Hess, R. Khasanov, A. Amato, C. Baines, M. Kosmala, O. J. Schumann, M. Braden, J. Hamann-Borrero, N. Leps, A. Kondrat, G. Behr, J. Werner, and B. Büchner: Nat. Mater. 8 (2009) 305.
6) K. Kubo and P. Thalmeier: J. Phys. Soc. Jpn. 78 (2009) 083704.
7) S. Raghu, X.-L. Qi, C.-X. Liu, D. J. Scalapino, and S.-C. Zhang: Phys. Rev. B 77 (2008) 220503(R).
8) C. de la Cruz, Q. Huang, J. W. Lynn, J. Li, W. Ratcliff II, J. L. Zarestky, H. A. Mook, G. F. Chen, J. L. Luo, N. L. Wang, and P. Dai: Nature 453 (2008) 899.
9) J. Zhao, W. Ratcliff II, J. W. Lynn, G. F. Chen, J. L. Luo, N. L. Wang, J. Hu, and P. Dai: Phys. Rev. B 78 (2008) 140504(R).
10) Q. Huang, Y. Qiu, W. Bao, M. A. Green, J. W. Lynn, Y. C. Gasparovic, T. Wu, G. Wu, and X. H. Chen: Phys. Rev. Lett. 101 (2008) 257003.
11) K. Kaneko, A. Hoser, N. Caroca-Canales, A. Jesche, C. Krellner, O. Stockert, and C. Geibel: Phys. Rev. B 78 (2008) 212502.
12) M. Rotter, M. Tegel, D. Johrendt, I. Schellenberg, W. Hermes, and R. Pötgen: Phys. Rev. B 78 (2008) 020503(R).
13) S. Kitao, Y. Kobayashi, S. Higashitaniguchi, M. Saito, Y. Kamihara, M. Hirano, T. Mitsui, H. Hosono, and M. Seto: J. Phys. Soc. Jpn. 77 (2008) 103706.
14) H.-H. Klauss, H. Luetkens, R. Klingeler, C. Hess, F. J. Litterst, M. Kraken, M. M. Korshunov, I. Eremin, S.-L. Drechsler, R. Khasanov, A. Amato, J. Hamann-Borrero, N. Leps, A. Kondrat, G. Behr, J. Werner, and B. Büchner: Phys. Rev. Lett. 101 (2008) 077005.
15) V. I. Anisimov, Dm. M. Korotin, M. A. Korotin, A. V. Kozhevnikov, J. Kuneš, A. O. Shorikov, S. L. Skornyakov, and S. V. Streltsov: J. Phys.: Condens. Matter 21 (2009) 075602.
16) K. Nakamura, R. Arita, and M. Imada: J. Phys. Soc. Jpn. 77 (2008) 093711.
17) S. Zhou and Z. Wang: Phys. Rev. Lett. 105 (2010) 096401.
18) F. Yang, H. Zhai, F. Wang, and D.-H. Lee: arXiv:1007.2643.
19) M. Dagh ofer, A. Moreo, J. A. Riera, E. Arrigoni, D. J. Scalapino, and E. Dagotto: Phys. Rev. Lett. 101 (2008) 237004.
20) H. Tang, M. Plihal, and D. L. Mills: J. Magn. Magn. Mater. 187 (1998) 23.
21) T. Okabe: J. Phys. Soc. Jpn. 66 (1997) 2129.
22) J. Bünemann, W. Weber, and F. Gebhard: Phys. Rev. B 57 (1998) 6896.
23) K. Kobayashi and H. Yokoyama: Physica C 445-448 (2006) 162.
24) K. Kubo: Phys. Rev. B 79 (2009) 020407(R).