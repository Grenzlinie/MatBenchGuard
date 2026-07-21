# Phase diagram of ferromagnetic XY model with nematic coupling on a triangular lattice

K. Qi $^{a,b}$, M.H. Qin $^{a,*}$, X.T. Jia $^{c}$, J.-M. Liu $^{b,**}$

$^{a}$ Laboratory for Advanced Materials, South China Normal University, Guangzhou 510006, China
$^{b}$ Laboratory of Solid State Microstructures, Nanjing University, Nanjing 210093, China
$^{c}$ School of Physics and Chemistry, Henan Polytechnic University, Jiaozuo 454000, China

---

## ARTICLE INFO

**Article history:**
Received 11 December 2012
Available online 9 April 2013

**Keywords:**
XY model
Kosterlitz-Thouless transition
Monte Carlo simulation

---

## ABSTRACT

The phase diagram of a ferromagnetic XY model with a nematic coupling (coupling strength $x$) on a triangular lattice is studied by means of Monte Carlo simulation. The algebraic-magnetic order associated with Kosterlitz-Thouless (KT) transition is observed over the whole $x$ range. In the large $x$ region, the phase transition from the algebraic-magnetic order to the algebraic-nematic order occurs at $T_{l}$. In addition, this phase transition can be scaled with the two-dimensional Ising critical exponents, demonstrating that the present system belongs to the universality class of Ising transition at $T_{l}$.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The two dimensional (2D) XY model has been well investigated for several decades due to its application in magnetic systems with planar anisotropy, quantum liquids and superconductors. As early as in 1966, it was proved that the 2D XY model cannot sustain long-range order even with trivial thermal fluctuations [1]. Alternatively, the so-called algebraic-magnetic (aM) order with Kosterlitz-Thouless (KT) transition may ensue [2,3]. After that, lots of work about the XY model have been reported [4-18].

On the other hand, nontrivial orders such as chiral order and nematic order in magnets, are drawing more and more attentions due to their relevancy with real magnetic materials as well as the contribution to the development of statistical mechanics. For example, a phase with coexisting nematic and vector spin chirality orders has been observed in the antiferromagnetic XY model with a nematic (biquadratic) coupling on the triangular lattice [7]. Later on, the same phase is also reported in our earlier work where a frustrated XY model on the square lattice has been studied with the Monte Carlo method [8]. In fact, the ferromagnetic XY model with a nematic coupling on square lattice has been studied as early as in 1989 [5]. The variations of temperature and the nematic coupling strength lead to three phases: a high-temperature disordered phase and two low temperature phases, namely, aM phase and algebraic-nematic (aN) phase. At non-zero temperatures, spin waves destroy the long-range order of the ground state, leaving power-law decay of the spin correlations. The high-temperature phase is entered respectively via the transition associated with an integer vortex pair excitation in the aM phase and an half-integer vortex pairs one in the aN phase [9]. At the same time, it is stated that the phase transition from disordered phase to aN phase is driven by the domain wall in which the free energy is expected to decrease with increasing temperature.

In fact, the consideration of the nematic coupling terms is mostly due to the fact that they can be large for magnetic ions with large spin [19]. For example, it is identified that the nematic coupling and the ferromagnetic coupling between the nearest neighbors may play an important role in triangular lattice system $NiGa_{2}S_{4}$, as revealed most recently [20]. In this work, a ferromagnetic XY model with a nematic coupling (coupling strength $x$) on a triangular lattice is studied by means of Monte Carlo simulation. Besides its contribution to the development of statistical mechanics, the study may be helpful to understand the experimental phenomena observed in $NiGa_{2}S_{4}$. As far as we know, few works on such a system have been reported. It will be demonstrated that a general KT transition from the algebraically correlated phase to the paramagnetic phase occurs when temperature raises up to a critical value. For the region in which the nematic coupling is dominated, a transition from the aM phase to the aN phase occurs at the critical temperature $T_{l}$ which is much lower than $T_{KT}$. In addition, the transition at $T_{l}$ has the same universality of scaling as the two-dimensional (2D) Ising transition, which is similar to earlier report [5].

For a classical XY spin model on a triangular lattice, we consider the following Hamiltonian which includes the nematic coupling interaction:

$$
H=-J_{1} \sum_{\langle i,j\rangle} \cos(\theta_{ij})-J_{2} \sum_{\langle i,j\rangle} \cos(2\theta_{ij}), \tag{1}
$$

---

* Corresponding author. Tel.: +86 13632457166.
** Corresponding author.
E-mail addresses: qinmh@scnu.edu.cn (M.H. Qin),
liujm@nju.edu.cn (J.-M. Liu).

0304-8853/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.jmmm.2013.03.036

![](./images/813231457710374913_1.jpg)
![](./images/813231457710374913_2.jpg)

where $\theta_{ij}$ is the angle difference $\theta_i-\theta_j$ between the nearest neighbors [i,j]. $J_1$=$1-x$ is the strength of the ferromagnetic coupling, and $J_2$=$x$ is the nematic coupling strength. For definition of the energy parameters $J_1$ and $J_2$, the Boltzmann constant and the lattice constant are set to unity.

Unlike the model studied in Ref. [7], our model does not contain any chiral orders due to the lack of the frustration ingredient. In the large $J_2/J_1$ region where the nematic interaction is much stronger than the ferromagnetic one, the spins between the nearest neighbors prefer either parallel or antiparallel with each other at the equal probabilities at low temperature, forming the possible nematic order, same as the earlier report [5].

![](./images/813231457710374913_3.jpg)

Fig. 1. Calculated phase diagram for the model in Eq. (1). The high-temperature paramagnetic phase is denoted by PM, the phases with algebraic correlations in magnetic and nematic order by aM and aN respectively. The statistical errors of all the symbols are given in the $T$ direction.

The Monte Carlo simulation is performed on a 2D $L \times L$ ($L$=18, 27, 36, 45, 54, and 72) triangular lattice with period boundary conditions using the standard Metropolis algorithm [21]. The initial spin configuration at high temperature ($T$) is totally disordered. Typically, the initial $3 \times 10^5$ Monte Carlo steps are discarded for the equilibrium consideration and another $2 \times 10^5$ Monte Carlo steps are retained for statistic averaging of the simulation.

The phase diagram in the $x$–$T$ plane for the model stated in Eq. (1) is shown in Fig. 1. The two curves mark the boundaries between three different phases, which are the aM phase, aN phase and paramagnetic (PM) phase. An integer vortex-mediated KT transition marking the PM–aM boundary splits into a half-integer vortex-mediated KT transition which marks the PM–aN boundary, plus a transition which separates the aM order from the aN order. It is noticed that in the most cases the critical temperatures of the KT transition and Ising transition are relatively higher than the corresponding ones [5]. This phenomenon can be easily understood from the point that for the systems with the same ferromagnetic coupling, one with higher coordination number shows the higher critical temperature. It is noted that for triangular system one spin interacts with six nearest neighbors rather than four for square system. So, the algebraically correlated order in triangular system is so robust and its destruction needs relatively high temperature.

![](./images/813231457710374913_4.jpg)

Fig. 2. Helicity modulus Y according to Eq. (2) for various sizes $L$ (a) at $x$=0.4 and (c) $x$=0.9. The straight line is $(2/\pi)(\sqrt{3}/2)(1+3x)T$. The crossing temperatures of this line and Y for each $L^{-1}$ are shown in (b) for $x$=0.4 and (d) $x$=0.9 with the extrapolation to $L^{-1}$=0.

The determination of $T_{\text{KT}}$ is made with the helicity modulus $Y$, also called the spin-wave stiffness [22,23]. Under this circumstance, $Y$ can be defined by

$$
\begin{aligned}
Y= & \frac{J_{1}}{2 L^{2}}\left\langle\sum_{[i, j]} \cos \theta_{i j}\right\rangle+\frac{2 J_{2}}{L^{2}}\left\langle\sum_{[i, j]} \cos 2 \theta_{i j}\right\rangle \\
& -\frac{1}{T L^{2}}\left\langle\left(J_{1} \sum_{[i, j]} x_{i j} \sin \theta_{i j}+2 J_{2} \sum_{[i, j]} x_{i j} \sin 2 \theta_{i j}\right)^{2}\right\rangle
\end{aligned}
$$

![](./images/813231457710374913_5.jpg)

Fig. 3. Specific heat $C$ as a function of $T$ for $L=36$ at (a) $x=0.4$, (b) $x=0.73$ and (c) $x=0.9$.

Here $x_{i j}=x_{i}-x_{j}$ is the separation of two coordinate sites. For a given lattice size $L$, the critical temperature $T_{\text{KT}}$ can be determined by the crossing of $Y(T)$ with the straight line $(2 / \pi)(\sqrt{3} / 2)\left(J_{1}+4 J_{2}\right)$ $T=(2 / \pi)(\sqrt{3} / 2)(1+3 x) T$. The helicity modulus for $L=18-72$ at $x=0.4$ and 0.9 are shown in Fig. 2(a) and (c), and the corresponding crossing points are shown in Fig. 2(b) and (d) respectively. The extrapolations to $L \rightarrow \infty$ using the polynomial fits yield the estimated values of $T_{\text{KT}}$ which is $1.254(5)$ for $x=0.4$ and $1.379(5)$ for $x=0.9$. This method is effective in giving a good estimate of $T_{\text{KT}}$ and a more sophisticated method taking into account the logarithmic correction gives a similar result [24].

The critical temperature of the transition from the aM phase to the aN phase can be easily estimated from the low-temperature specific-heat peak, as stated in our earlier work [8]. Specific heat $C$ as a function of $T$ at $x=0.4, x=0.73$ and $x=0.9$ for $L=36$ are plotted in Fig. 3. It is indicated that the one single peak at small $x$ separates to two independent peaks which gradually detach from each other with the increasing of $x$. In the low $x$ region $(x<0.65)$, no transition from the aM phase to the aN phase occurs, leaving the single peak in the $C-T$ curves, as shown in Fig. 3(a). On the other hand, the low-temperature sharp peaks at $0.96(2)$ for $x=0.73$ and $0.36(2)$ for $x=0.9$ clearly mark the nematic phase transitions, as shown in Fig. 3(b) and (c).

In Fig. 4(a), we show a snapshot of the nematic order at $T=0.4$ for $x=0.95$. The spins become generally parallel or antiparallel with each other, forming the so-called nematic order. At last, the critical exponent of the nematic transition is estimated with the dependence of the specific heat peak upon the absolute value of the difference between the critical temperature and its neighbor ones, i.e., $C_{\text{peak}} \propto|T_{c}-T|^{-\alpha}$. In Fig. 4(b), we plot the specific heats under different temperatures around $C_{\text{peak}}$ for $L=36$ at $x=0.9$. The linear fit gives $\alpha \approx 0.02$ which is almost same as that of 2D Ising model, i.e., $\alpha=0$. Taking into account the simulation errors, it is reasonable to argue that the universality class of this phase transition is that of 2D Ising transition as reported in earlier works [5,7].

To sum up, the phase diagram of ferromagnetic $XY$ model with nematic coupling $(x)$ on a triangular lattice is studied in details with Monte Carlo method. The phase diagram exhibits three phases including the algebraic-magnetic phase, the algebraic-nematic phase and the paramagnetic phase. In the large region of $x(x \geq 0.65)$, an Ising transition from the aM phase to aN phase is observed in addition to the usual KT transition. This work is a complementary one to the study of 2D $XY$ models, and may be helpful to understand the experimental phenomena observed in $\mathrm{NiGa}_{2} \mathrm{~S}_{4}$.

![](./images/813231457710374913_6.jpg)

Fig. 4. (a) A snapshot of the nematic order at $T=0.4$ at $x=0.95$. (b) A scaling plot of specific heats under different $T$ around critical temperature for lattice size $L=36$ at $x=0.9$.

### Acknowledgment

This work was supported by the Natural Science Foundation of China (11204091, 11274094, and 11234005), the National Key Projects for Basic Research of China (2009CB623303), China Postdoctoral Science Foundation funded project (2012T50684 and 20100480768), and the Priority Academic Program Development of Jiangsu Higher Education Institutions, China.

### References

[1] N.D. Mermin, H. Wagner, Physical Review Letters 17 (1966) 1133.
[2] J.M. Kosterlitz, D.J. Thouless, Journal of Physics C 6 (1973) 1181.
[3] D.P. Landau, Journal of Applied Physics 73 (1993) 6091.
[4] J.M. Kosterlitz, Journal of Physics C 7 (1974) 1046.
[5] D.B. Carpenter, J.T. Chalker, Journal of Physics: Condensed Matter 1 (1989) 4907.
[6] J. Villain, Journal of Physics C: Solid State Physics 10 (1977) 1717.
[7] J.H. Park, S. Onoda, N. Nagaosa, J.H. Han, Physical Review Letters 101 (2008) 167202.
[8] M.H. Qin, X. Chen, J.-M. Liu, Physical Review B 80 (2009) 224415.

[9] D.H. Lee, G. Grinstein, Physical Review Letters 55 (1985) 541.
[10] J. Tobochnik, G.V. Chester, Physical Review B 20 (1979) 3761.
[11] S. Teitel, C. Jayaprakash, Physical Review B 27 (1983) 598.
[12] J. Lee, E. Granato, J.M. Kosterlitz, Physical Review B 44 (1991) 4819.
[13] J. Villain, Journal of Physics C 10 (1977) 4793.
[14] S. Lee, K.C. Lee, Physical Review B 49 (1994) 15184.
[15] R. Gupta, J. DeLapp, G.G. Batrouni, G.C. Fox, C.F. Baillie, J. Apostolakis, Physical Review Letters 61 (1988) 1996.
[16] E. Granato, J.M. Kosterlitz, J. Lee, M.P. Nightingale, Physical Review Letters 66 (1991) 1090.
[17] P. Olsson, Physical Review Letters 75 (1995) 2758.
[18] S. Miyashita, H. Nishimori, A. Kuroda, M. Suzuki, Progress of Theoretical Physics 60 (1978) 1669.
[19] L.X. Hayden, T.A. Kaplan, S.D. Mahanti, Physical Review Letters 105 (2010) 047203.
[20] E.M. Stoudenmire, S. Trebst, L. Balents, Physical Review B 79 (2009) 214436.
[21] D.P. Landau, K. Binder, A Guide to Monte Carlo Simulations in Statistical Physics, Cambridge University Press, Cambridge, England, 2005.
[22] M.E. Fisher, M.N. Barber, D. Jasnow, Physical Review 0A 8 (1973) 1111.
[23] D.H. Lee, J.D. Joannopoulos, J.W. Negele, D.P. Landau, Physical Review B 33 (1986) 450.
[24] P. Minnhagen, B.J. Kim, S. Bernhardsson, G. Cristofano, Physical Review B 76 (2007) 224403.