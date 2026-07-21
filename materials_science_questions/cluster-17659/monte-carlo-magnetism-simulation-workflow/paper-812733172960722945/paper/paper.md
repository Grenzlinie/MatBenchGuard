# Monte Carlo simulation of polymerization-induced phase separation

Yang-Ming Zhu
Liquid Crystal Institute, Kent State University, Kent, Ohio 44242
(Received 27 February 1996)

In a reactive-monomer-small-molecule composite system, the degree of polymerization increases as time proceeds, which results in a phase separation of these two components. Because during this process the system is generally kept at a constant temperature, this separation is termed polymerization-induced phase separation (PIPS). In this paper we first calculated the polymerization degree as a function of time based on a kinetic model for polymerization process [J. C. Lin and P. L. Taylor, Phys. Rev. E 49, 2476 (1994)]. We then analyzed PIPS within the framework of the free energy of Flory and Huggins. The critical temperature of this composite system is polymerization degree dependent, which is in turn also a function of time. The quench depth of the PIPS system decreases with time due to the increase of critical temperature. To simulate PIPS, we mapped this time-dependent quench scheme into a two-dimensional Ising model by gradually reducing the quench temperature while letting the quench depth change with time as that in the PIPS system. Our simulation results show that both reaction speed and temperature can influence the phase-separated domain size, which is in qualitative agreement with experimental observations. [S1063-651X(96)05008-8]

PACS number(s): 82.35.+t, 64.75.+g, 61.30.−v, 05.50.+q

## I. INTRODUCTION

Phase separation phenomena have been extensively studied in the past two decades from both experimental and theoretical points of view [1]. The phase separation takes place when a fluid system is quenched from the one-phase region into the two-phase coexisting region (i.e., the unstable region of its phase diagram). Domains of coexisting phases grow and coarsen in time, and in the later stages, all domain sizes are much larger than any microscopic length. This is known as thermal-quench-induced phase separation (TIPS). In recent years, phase separation in confined geometry [2], dynamic coupling between phase separation and surface wetting [3], and competition between chemical reaction and phase separation [4] are new and seminal topics.

Phase separation is not only of theoretical interest, but also important for applications. For example, phase separation in a polymer-liquid-crystal composite system has found application in flat panel liquid-crystal displays. Generally, there are two kinds of polymer-liquid-crystal mixture systems with application potential: polymer-dispersed liquid crystals and liquid-crystal dispersed polymers. As a typical preparation procedure, a reactive monomer and liquid crystals are mixed and rigorously stirred to form one homogeneous phase. The mixture is sealed between two plates. The polymerization process commences on mixing, driving the system into an unstable region. Phase separation then occurs. Because the whole system is kept at a constant temperature, this separation is termed polymerization-induced phase separation (PIPS).

Although a great deal is known about TIPS, relatively little work has been done on PIPS [5–9]. In this paper we simulate PIPS by the Monte Carlo method. We do not simulate how the monomers are chemically bonded to form oligomers and polymers and then separate from the liquid crystal when the average polymerization degree increases. Instead, we first analyze how a certain average of polymerization degree evolves with time and how the critical temperature for this composite system depends on the polymerization degree. The critical temperature as well as the quench depth therefore can be expressed as a function of time. On these bases, PIPS can be regarded as TIPS by an appropriate quench scheme, and it is also possible to understand PIPS by simulating the TIPS with a proper quench (i.e., a time-dependent quench). We believe this scheme may reflect some macroscopic properties of PIPS.

This paper is organized as follows. In Sec. II we discuss the kinetic process of polymerization. Specifically, the average of the reciprocal of the polymerization degree for bifunctional monomers is derived there. Then in Sec. III we analyze the phase separation process based on the free energy of Flory and Huggins. The evolution of the quench depth as a function of time is obtained there. The time-dependent quench depth is then introduced in a two-component two-dimensional Ising model in Sec. IV. The simulation results of our proposed approach are also illustrated and discussed in Sec. IV; they indicate that both the polymerization speed and temperature can control the phase-separated domain size. We finally conclude the whole paper in Sec. V.

## II. KINETIC PROCESS OF POLYMERIZATION

The model we consider is initially a composite system of monomers and liquid crystal with molecular concentration $p$ and $1-p$, respectively. As time goes on, monomers chemically bond to form oligomers and then polymers. While the monomers may be multifunctional, which is a simple case for theoretical treatment, in practical cases, the monomers may be bifunctional [10]. In the final stage, the mixture system is actually a composition of liquid crystal and polymers with various degrees of polymerization.

Let us discuss the kinetics of the polymerization process. The central quantity of interest is the distribution function $P(N,t)$, defined as the probability that at time $t$, any site is occupied by a monomer forming part of a polymer with a

polymerization degree $N$. Lin and Taylor [7] argued that the master equation for $P(N,t)$ is

$$
\begin{aligned}
\frac{d P(N, t)}{d t}= & \frac{k N}{2} \sum_{m+n=N} A(m) P(m, t) A(n) P(n, t) \\
& -k N A(N) P(N, t) \sum_{m=1}^{+\infty} A(m) P(m, t), \quad(1)
\end{aligned}
$$

where $k$ is the temperature-dependent reaction rate constant and $A(m)$ is a function of $m$ depending upon the functionality of the monomer. For example, for a bifunctional monomer, $A(m)=2 / m$ [11]. The first term on the right side of Eq. (1) represents the rate at which an $N$-mer is formed by the reaction of an $m$-mer and an $n$-mer $(m+n=N)$ and the second term represents the rate of removal of $N$-mer by reaction with other polymers of all possible sizes. Lin and Taylor discussed only the multifunctional polymerization process [7]. For bifunctional monomers, Eq. (1) reads

$$
\begin{aligned}
\frac{d P(N, t)}{d t}= & 2 k N \sum_{m+n=N} \frac{P(m, t) P(n, t)}{m n} \\
& -4 k P(N, t) \sum_{m=1}^{+\infty} \frac{P(m, t)}{m}.
\end{aligned}
$$

Equation (2) is more difficult to solve; however, we can still get some information about the bifunctional polymerization process.

Introducing a reduced time $\tau=k p t$ and a normalized distribution function $Q(N, \tau)=P(N, \tau) / p$, and letting $Q(N, \tau) /$ $N=R(N, \tau)$, we have from Eq. (2)

$$
\begin{aligned}
\frac{d R(N, \tau)}{d \tau}= & 2 \sum_{m+n=N} R(m, \tau) R(n, \tau) \\
& -4 R(N, \tau) \sum_{m=1}^{+\infty} R(m, \tau) .
\end{aligned}
$$

Summarizing the above equation with respect to $N$, one gets

$$
\frac{d}{d \tau}\left(\sum_{m=1}^{+\infty} R(m, \tau)\right)=-2\left(\sum_{m=1}^{+\infty} R(m, \tau)\right)^{2} .
$$

The boundary condition is, at $\tau=0, \sum_{m=1}^{+\infty} R(m, \tau)=1$. This is related to the fact that before polymerization commences, the degree of polymerization is 1 . Integrating this differential equation, we have $\sum_{m=1}^{+\infty} R(m, \tau)=1 /(1+2 \tau)$. Considering $\langle 1 / N\rangle=\sum_{m=1}^{+\infty} Q(N, \tau) / N$, we finally arrive at [12,13]

$$
\left\langle\frac{1}{N}\right\rangle=\frac{1}{1+2 \tau} .
$$

### III. CRITICAL TEMPERATURE FOR PHASE SEPARATION

Flory and Huggins proposed a mean field expression for the free energy of a polymeric system [9], which was combined with the theory of spindoal decomposition of Cahn and Hilliard [14] by Kim and Palffy-Muhoray [6] and later by Lin and Taylor [7] to discuss PIPS in a polymer-liquidcrystal composite system. Here, we also employ this free energy formalism to discuss PIPS.

Phase separation is driven by the free energy and the corresponding time scale is governed by diffusion, while the polymerization proceeds at a rate governed by the kinetics of the chemical reaction. However, if the rate for diffusion is much smaller than that for reaction, then phase separation can be considered as determined by the local free energy [7]. In the Flory-Huggins mean field model of a solution of $N$-mer, the free energy $f$ per molecule is

$$
F(p)=\frac{f(p)}{k_{B} T}=\frac{p}{N} \ln p+(1-p) \ln (1-p)+\chi p(1-p),
$$

where $\chi=\left[\varepsilon_{m l}-\left(\varepsilon_{m m}+\varepsilon_{l l}\right) / 2\right] / k_{B} T$ reflects the molecular interaction and is generally positive ( $\varepsilon_{m l}, \varepsilon_{m m}, \varepsilon_{l l}$ are intermolecular interactions between monomer and liquid crystal, monomer and monomer, and liquid crystal and liquid crystal, respectively), $k_{B}$ is Boltzmann's constant, and $T$ is temperature.

The polymer-liquid-crystal system is unstable when $F^{\prime \prime}(p)<0$. We have the spinodal line given by

$$
F^{\prime \prime}(p)=\frac{1}{N p}+\frac{1}{(1-p)}-2 \chi=0 .
$$

If we take

$$
a=\left(2 \varepsilon_{m l}-\varepsilon_{m m}-\varepsilon_{l l}\right) / k_{B},
$$

then Eq. (7) changes to

$$
\frac{1}{N p}+\frac{1}{1-p}-\frac{a}{T}=0,
$$

i.e., for fixed $1 / N$, spinodal decomposition takes place at temperature

$$
T=\frac{a}{1 / N p+1 /(1-p)} .
$$

We see that at a high temperature, spinodal decomposition takes place when $1 / N$ is small. We show in Fig. 1(a) the spinodal curves in the temperature and concentration space for various $1 / N$, where the temperature is in units of $a$. For each $1 / N$, the extremum point gives the critical temperature $\left(T_{c}\right)$ and critical concentration $\left(p_{c}\right)$ :

$$
p_{c}=\frac{1}{1+1 / \sqrt{1 / N}},
$$

$$
T_{c}=\frac{a}{(1+\sqrt{1 / N})^{2}} .
$$

They can also be obtained directly from $F^{\prime \prime \prime}(p)=0$. In Fig. 1(b) we plot the critical temperature (in units of $a$ ) as well as the spinodal temperature (also in units of $a$ ) for different polymer concentration as functions of $1 / N$, where one can find that the critical temperature is actually the envelope of the spinodal temperatures at various polymer concentrations. As we stated above, after monomers react with each other to

![](./images/812733172960722945_1.jpg)

FIG. 1. (a) Spinodal lines in the temperature and concentration parameter space at various polymerization degrees. From top to bottom, $1/N$=0.001, 0.01, 0.1, and 1, respectively. The temperature is in units of $a$. For the definition of $a$, please refer to the text. (b) Spinodal temperatures (solid lines) and critical temperature (dotted line) as a function of the inverse of polymerization degree ($1/N$). For the spinodal temperatures, from top to bottom, the polymer concentrations are 0.3, 0.5, and 0.7, respectively. The temperature is also in units of $a$. The critical temperature is the envelope of the spinodal temperature at various polymer concentrations.

form oligomers and polymers, the mixture is a composition of liquid crystal and polymer with various degrees of polymerization $N$. $1/N$ in Eqs. (10)–(12) can be approximated by the average of the inverse of polymerization degrees given by Eq. (5).

Suppose the liquid-crystal–polymer composite system is kept at temperature $T_q$. From Eqs. (10) and (5), one can obtain the induction time [6]

$$
\tau_{0}=\frac{T_{q}-a p(1-p)}{2 p\left[a(1-p)-T_{q}\right]}. \tag{13}
$$

Using Eqs. (5) and (12), we get the time-dependent quench depth

$$
\frac{T_{q}}{T_{c}}=\frac{T_{q}}{a}\left[1+\sqrt{1 /(1+2 \tau)}\right]^{2}, \tag{14}
$$

which will be extensively used in the next section.

## IV. SIMULATION RESULTS AND DISCUSSION

We note that PIPS is similar to TIPS if one takes a proper quench scheme. At the beginning, the system is in a homogeneous phase. As the polymerization process goes on, the system is expelled into an unstable region and the quench depth is gradually decreased due to the advancement of the critical temperature $T_c$. The kinetics of phase separation in polymer mixtures and small molecule mixtures is similar in many respects and the kinetics is mainly determined by the quench scheme [1]. In this sense, PIPS can be considered as TIPS [15]. However, the thermal quench depth is time dependent.

We performed Monte Carlo simulation of the PIPS by a proper thermal quench scheme on two-dimensional square lattices of size 200×200. At the beginning, each lattice was initialized at a temperature $T=\infty$ with a molecule randomly chosen to be $A$ or $B$. Here $A$ and $B$ are different kinds of molecules: e.g., $A$ is monomer and $B$ is liquid crystal. The concentration of $A$ is 0.5, which is the critical concentration of this model. Although in a real polymer-dispersed liquid-crystal system the polymer concentration is generally larger than 0.5, and in a liquid-crystal-dispersed polymer case, the polymer concentration is around 0.05, here the symmetric quenching still captures the main properties of a real system. Nearest-neighbor molecules interact with energy $-J$ ($J$) if the molecules are of the same (different) kinds ($J$ is positive). Since our simulations were performed on a two-dimensional square lattice, we can use Onsager’s solution of the Ising model [16] to find the critical temperature $T_c$, which turns out to be $k_BT_c=0.567J$. The configuration of the system was updated according to the standard Metropolis Monte Carlo scheme [17]. One Monte Carlo step (MCS) includes an attempted exchange of every nearest-neighbor molecule via Kawasaki dynamics [17], i.e., the acceptance probability

$$
P_{\text{exch}}=\frac{\exp \left(-\Delta E / k_{B} T_{q}\right)}{1+\exp \left(-\Delta E / k_{B} T_{q}\right)},
$$

where $\Delta E=E_{\text{final}}-E_{\text{initial}}$, the difference between the energies of the system before and after the exchange. The quench depth was changed according to Eq. (14). In a real PIPS process, the temperature is kept constant. As the polymerization process goes on, the interactions between monomer and monomer and between monomer and liquid crystal are also changed, which induces the increment of the critical temperature. Here, in our simulation, the critical temperature is constant, however, we change the quench temperature to keep the quench depth the same as in the PIPS system, intending to mimic the interaction change in this system. There is a time constant associated with Kawasaki dynamics that sets the physical time scale. We took this constant equal to 1 in our simulation (i.e., $t=1$ MCS). The simulation was performed under various conditions: different reaction rates and different temperatures.

To test the validity of our program codes, we first conducted the simulations with constant quench depth. We kept the quench depth at 1.0, 0.9, 0.8, 0.7, 0.6, and 0.5. One probe

![](./images/812733172960722945_2.jpg)

FIG. 2. First moment $k_1$ (a) and first zero crossing (b) as a function of MCS for different simulation with constant quench depth.

in phase separation experiments is the dynamic structure factor $S(\mathbf{k},t)$, defined as the Fourier transform of the pair correlation function $G(\mathbf{r},t)$:

$$
G(\mathbf{r},t)=\frac{1}{M} \sum_{\mathbf{r}_{i}}\left\langle\left[c\left(\mathbf{r}_{i}, t\right)-c_{0}\right]\left[c\left(\mathbf{r}_{i}+\mathbf{r}\right)-c_{0}\right]\right\rangle,
$$

$$
S(\mathbf{k},t)=\sum_{\mathbf{r}} \exp(j\mathbf{k}\cdot\mathbf{r})G(\mathbf{r},t).
$$

Here $c_0$ is the average concentration which remains constant during the evolution, $\mathbf{r}$ and $\mathbf{r}_i$ run over the $M$ lattice sites. The angle brackets $\langle\,\rangle$ denote the ensemble average which is realized in the simulations by making several independent runs. To improve the accuracy and the presentation of data, $S(\mathbf{k},t)$ is further smoothed by averaging over all wave vectors with magnitude between $k$ and $k+\delta k$, known as spherical averaging [1]. In ordinary phase separation, the characteristic wave vector moves to smaller values following a quench to the unstable region. Experiments typically will measure the peak position $k_m$ as a function of time following a quench. Here we calculate an equivalent quantity, the first moment of structure factor $S$, $k_1$ [1,4(a)]:

$$
k_{1}(t)=\frac{\sum_{k} k(t) S(k, t)}{\sum_{k} S(k, t)}.
$$

$k_1(t)$ can be calculated more accurately than the peak position. We calculated $k_1$ as a function of MCS for each quench depth. The results are given in Fig. 2(a). From Fig. 2(a) one can see that $k_1$ does not behave well when the quench depth is larger than 0.7: In some regions, the curves for different quench depth are mixed up. However, a double logarithmic plot shows that at larger MCS's, the slope for each curve tends to $-\frac{1}{4}$, indicating the validity of our simulations [1].

We also calculated the autocorrelation function of the separated pattern, and then computed the average in all directions of $\mathbf{r}$ with $|\mathbf{r}|$=const. The first zero crossing (FZC) in the averaged one-dimensional autocorrelation function was used as another probe for the phase-separated domain size. Again we illustrate the results in Fig. 2(b). We see that FZC has a better behavior as compared to $k_1$. A double logarithmic plot also gives a slope of $\frac{1}{4}$ at larger MCS values. So, in the following, we use both $k_1$ and FZC as probes of phase-separated domain size.

![](./images/812733172960722945_3.jpg)

FIG. 3. Examples of 200×200 lattice configurations after PIPS is triggered. (a) MCS=2000, $k$=0.1, $T_q$=0.4$a$, (b) MCS=2000, $k$=0.01, $T_q$=0.4$a$, (c) MCS=20 000, $k$=0.01, $T_q$=0.4$a$, and (d) MCS=20000, $k$=0.01, $T_q$=0.3$a$. Molecules of liquid crystal (monomer) are shown as black (white). Note for (a), (c), and (d), $1+2kp\times$(MCS)=201, while for (b) it is 101.

### A. Influence of polymerization speed

We studied the influence of polymerization speed $k$ on the phase-separated domain size, which is very critical for the application of polymer-dispersed liquid crystals. Figure 3 shows some configurations generated by simulation. Molecules of liquid crystal (monomer) are shown as black (white). For Figs. 3(a) and 3(b), MCS=2000, $T_q$=0.4$a$ (clearly, for this selected temperature, the monomer-liquid-crystal composite system will not separate at the beginning), but $k$=0.1 and 0.01, respectively. One can see that the do-

![](./images/812733172960722945_4.jpg)

FIG. 4. (a) First moment $k_1$ as a function of MCS for different reaction speed $k$. $T_q$=0.4$a$. The changes of quench depth with MCS are shown in the inset. (b) First zero crossing of the autocorrelation function of the separated pattern as a function of MCS. (c) Polymerization speed $k$-dependent $k_1$ and first zero crossing when $1+2kp\times$(MCS)$=201$.

![](./images/812733172960722945_5.jpg)

FIG. 5. (a) First moment $k_1$ as a function of MCS for different $T_q$. $k$=0.01. The changes of quench depth with MCS are shown in the inset. (b) First zero crossing of the autocorrelation function of the separated pattern as a function of MCS. (c) $T_q$-dependent $k_1$ and first zero crossing when $1+2kp\times$(MCS)$=201$.

main size for Fig. 3(a) is smaller than that for Fig. 3(b), also see Figs. 4(a) and 4(b). Experimental results show that when the chemical reaction is increased, the domain size of the phase-separated pattern is depressed [18]. This simulation seems to support the real observation. As a matter of fact, as the polymerization goes on, a gelation transition occurs at a later stage, where the polymers form a network while the polymerization degree tends to infinite. Apparently our present model cannot take this transition into account. More recent theories by Sciortino *et al.* [19], Glotzer *et al.* [4(a)], and Chen and Chen [20] seem useful. In our model, in order

to mimic this gelation, we just stop the simulation at a par- ticular MCS so that $1 + 2kp \times (\text{MCS})$ remains constant (i.e., we let the polymerization degree become an arbitrarily larger constant when gelation occurs). A similar idea was used to generate a porous medium [21]. Taking this ‘‘gelation’’ into consideration, we know that phase separation stops at an early time when $k$ is large and vice versa. Thus one should not compare the domain size at the same MCS, but at the same $1 + 2kp \times (\text{MCS})$ (i.e., the same polymerization de- gree). Here we assume the maximum polymerization degree is 201. Figure 3(c) shows another pattern when MCS =20 000. Other parameters are identical to those for Fig. 3(b). We note that the polymers involved in Figs. 3(a) and 3(c) have the same polymerization degree. One can see that the domain size of Fig. 3(c) is much larger than that of Fig. 3(a), also see Fig. 4.

We have computed the structure factors and FZC under various conditions. Figure 4(a) shows $k_1$ as a function of MCS for $k=0.1$ and 0.01. The inset in Fig. 4(a) shows how the quench depth changes with time. FZC as a function of MCS is shown in Fig. 4(b). From these two plots, we can see FZC behaves similarly to $k_1$. To compare the domain size for various $k$, we calculated $k_1$ and FZC at the same $k \times (\text{MCS})$, here 200 (i.e., $N=201$). The result is shown in Fig. 4(c). When $k$ increases, the domain size decreases. Here, one should be more careful about the result in Fig. 4(c) be- cause we keep $k \times (\text{MCS})$ at an arbitrary number. Thus it cannot amount to the real situation and can only be used as a qualitative prediction of the relationship between the phase- separated domain size and the polymerization speed.

### B. Influence of temperature

We also performed the simulation at different temperature $T_q$. Here, the temperature is in units of $a$. However, when the temperature is raised, the chemical reaction speed $k$ is also increased, and larger $k$ results in a smaller phase- separated domain size. Let us first assume $k$ is invariant when temperature changes.

Also shown in Fig. 3 is the simulated pattern for a differ- ent temperature. For Fig. 3(d), $\text{MCS}=20$ 000, $k=0.01$, and $T_q=0.3a$, so $1 + 2kp \times (\text{MCS})=201$. Compared to Fig. 3(c), one can see the domain size of Fig. 3(d) is smaller. Quanti- tative evidence of this is shown in Fig. 5. In Fig. 5(a) we give the relation between $k_1$ and MCS for temperature $T_q=0.4a$ and $0.3a$. The inset is the quench depth evolution with MCS. We also calculated the FZC for each case [see Fig. 5(b)]. It is clear from Fig. 5(b) that higher temperature will increase the phase-separated domain size. We still com- puted FZC and $k_1$ as a function of $T_q$ while keeping the polymerization degree at 201. Figure 5(c) clearly shows the domain size increases with the increase of temperature.

As always observed, higher temperature results in a higher polymerization speed, $k_1$, which tends to reduce the phase-separated domain size. Thus the effects of temperature are complicated. Actually, there are two competing effects, enlarging or depressing the domain size. The real situation is determined by the dominant effect. Without the chemical information it is hard to say which one will prevail. That is also the reason both effects have been reported [18].

### V. CONCLUSION

We have obtained a formula to describe how the polymer- ization degree changes with time for a reactive-monomer- small-molecule composite system based on a kinetic model of polymerization. Within the framework of the free energy of Flory and Huggins, we have also calculated the quench depth as a function of time for the polymerization-induced phase separation system. We suggest PIPS can be simulated by TIPS with a proper quench scheme. Our simulation re- sults show that the phase-separated domain size, which is very important for the practical application of this system, can be controlled by reaction rate and temperature. High po- lymerization speed tends to depress the domain size, while high temperature can increase or decrease the domain size, depending on the influence of temperature on the chemical reaction speed. When temperature has little effect on the po- lymerization speed, high temperature tends to increase the domain size, otherwise it will decrease the domain size. These simulation results are qualitatively in agreement with experimental observations. Our simulation can be easily ex- tended to the three-dimensional case as well as off symmet- ric quenching cases. As one can see from Eq. (1), the poly- merization we discussed here is a condensation process. However, the presented idea is also applicable to a free radi- cal polymerization process [22], where the polymerization degree has a different time dependent behavior.

Finally, let us point out the limitation of our approach. Apparently, the final domain size in this liquid-crystal- polymer composite system must be related to the gelation phenomenon. In our model we cannot take this into account. Hopefully, our approach can be merged with recent theories [4(a),19,20] to include gelation phenomenon. Further study on the pinning effects in this system is in progress.

### ACKNOWLEDGMENTS

We thank Bill Fritz, E. Landry, P. L. Taylor, and D. K. Yang for critical reading of this manuscript.

[1] J. D. Gunton, M. S. Miguel, and P. S. Sahni, in *Phase Tran- sitions and Critical Phenomena*, edited by C. Domb and J. H. Lebowitz (Academic, London, 1983), Vol. 8.
[2] Z. Zhang and A. Chakrabarti, Phys. Rev. E **50**, R4290 (1994); M. Y. Liu, S. K. Sinha, J. M. Drake, X. I. Wu, P. Thiyagara- jan, and H. B. Stanley, Phys. Rev. Lett. **72**, 2207 (1994).
[3] H. Tanaka, Phys. Rev. Lett. **72**, 2581 (1994); **72**, 3690 (1994).
[4] (a) S. C. Glotzer, M. F. Gyure, F. Sciortino, A. Coniglio, and H. E. Stanley, Phys. Rev. Lett. **70**, 3275 (1993); Phys. Rev. E **49**, 247 (1994); (b) S. C. Glotzer, D. Stauffer, and N. Jan, Phys. Rev. Lett. **72**, 4109 (1994); (c) S. C. Glotzer, E. A. Di Marzio, and M. Muthukumar, ibid. **74**, 2034 (1995); (d) S. C. Glotzer and A. Coniglio, Phys. Rev. E **50**, 4241 (1994).
[5] G. W. Smith, Phys. Rev. Lett. **70**, 1981 (1993); G. W. Smith

and N. A. Vaz, Liq. Cryst. **3**, 543 (1988).

[6] J. Y. Kim, C. H. Cho, P. Palffy-Muhoray, M. Mustafa, and T. Kyu, Phys. Rev. Lett. **71**, 2232 (1993); J. Y. Kim and P. Palffy-Muhoray, Mol. Cryst. Liq. Cryst. **203**, 93 (1991).

[7] J. C. Lin and P. L. Taylor, Phys. Rev. E **49**, 2476 (1994); Mol. Cryst. Liq. Cryst. **237**, 25 (1993).

[8] J. C. Lin and P. L. Taylor, Phys. Rev. E **49**, 4258 (1994).

[9] F. J. Flory, J. Chem. Phys. **10**, 51 (1942); M. Huggins, J. Phys. Chem. **46**, 151 (1942).

[10] D. K. Yang, L. C. Chien, and J. W. Doane, Appl. Phys. Lett. **60**, 3102 (1992); G. P. Crawford, A. Scharkowski, Y. K. Fung, J. W. Doane, and S. Zumer, Phys. Rev. E **52**, R1273 (1995).

[11] For multifunctional polymerization, Lin and Taylor [7] let $A(m)=1$. But we prefer to set $A(m)$ a constant, otherwise the reaction speed of multifunctional polymerization is slower than that of a bifunctional one.

[12] Our result shows that when $\tau \ll 1$, $\langle 1/N \rangle=1-2\tau$; however, Lin and Taylor showed that when $\tau \lesssim 1$, $\langle 1/N \rangle=1-\tau/2$, meaning that the bifunctional polymerization is faster than multifunctional polymerization. As we have mentioned, we prefer to set $A(m)$ as a constant for a multifunctional case. In a lattice model, this constant is dimension related. For example, for the one-dimensional case, $A(m)=2$, and for the two-dimensional case, $A(m)=4$. Consequently, Lin and Taylor's result should be modified as $\langle 1/N \rangle=1-2\tau$ and $\langle 1/N \rangle=1-4\tau$ for one-dimensional and two-dimensional cases, respectively.

[13] A quite similar result $\langle N \rangle=1+2\tau$ can be obtained in a different way. L. C. Chien (unpublished).

[14] J. W. Cahn, J. Chem. Phys. **42**, 93 (1965); J. W. Cahn and J. E. Hilliard *ibid.* **29**, 258 (1958).

[15] In the later stage of PIPS, a second phase separation appears [6]. This second separation has already been reported in TIPS although the origin is still controversial. Understanding the physical origin for the second separation in TIPS should be informative to that in PIPS. See H. Tanaka, Phys. Rev. E **51**, 1313 (1995).

[16] H. E. Stanley, *Introduction to Phase Transitions and Critical Phenomena* (Oxford University Press, New York, 1971).

[17] *Applications of Monte Carlo Method in Statistical Physics*, edited by K. Binder (Springer-Verlag, Berlin, 1987).

[18] G. W. Smith, Mol. Cryst. Liq. Cryst. **241**, 77 (1994).

[19] F. Sciortino, R. Bansil, H. E. Stanley, and P. Alstrom, Phys. Rev. E **47**, 4615 (1993).

[20] W. J. Chen and S. H. Chen, Phys. Rev. E **52**, 5696 (1995).

[21] A. Chakrabarti, Phys. Rev. Lett. **69**, 1548 (1992); Z. Zhang and A. Chakrabarti, Phys. Rev. E **52**, 4991 (1995).

[22] A. M. North, *The Kinetics of Free Radical Polymerization* (Pergamon Press, 1966).