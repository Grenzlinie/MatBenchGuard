![](./images/812449260321636352_1.jpg)

Chemical Physics 282 (2002) 371–377

# Chemical Physics
www.elsevier.com/locate/chemphys

# Mediated electron exchange between an electrode and the tip of a scanning tunneling microscope – a stochastic approach

A.N. Kuznetsov $^{1}$, W. Schmickler $^{*}$

Abteilung Elektrochemie, University of Ulm, D-89069 Ulm, Germany

Received 15 March 2002

## Abstract
We consider electron exchange between a metal electrode and the tip of a scanning tunneling microscope via an adsorbed intermediate state. The exchange is supposed to occur through resonant tunneling while the system moves stochastically on the free energy surface. We have performed model calculations for various system parameters, and offer a new interpretation of experimental data. © 2002 Elsevier Science B.V. All rights reserved.

## 1. Introduction
The scanning tunneling microscope (STM), operated in an electrochemical environment, offers the possibility to investigate electroactive species adsorbed on the electrode surface. In principle, an electrolyte cell is better suited for performing electronic spectroscopy on such states than ultrahigh vacuum, because two potential differences can be varied independently: the tunneling bias between the electrode and the STM, and the potential drop between electrode and solution. However, in practice it has been difficult to realize this possibility, and to date the investigation of protoporphyrin films initiated by Tao [1,2] remains the most convincing STM study of an adsorbed redox system.

In fact, there has been more theoretical than experimental activity in this area. Essentially, two different mechanisms have been proposed for electron exchange between a metal electrode and an STM tip via an adsorbed electronic state: Schmickler and Widrig proposed resonant tunneling, either elastic [3] or inelastic [4], while Kuznetsov et al. [5] suggested *vibrationally coherent two-step electron transfer*. In the present work, we propose a third model, which contains what we believe to be the strong points of both theories: We take the resonant tunneling mechanism from the former work and combine it with stochastic dynamics, which plays a significant role in the latter. Our results provide new insight into the dynamics of electron transfer via and adsorbate, and offer an alternative interpretation of Tao’s results.

## 2. The model
The model Hamiltonian is the same as in the work by Schmickler [4]; it is presented below to make this paper self-contained. We consider an electroactive adsorbate on a metal electrode, which is imaged by

---
$^{*}$Corresponding author. Tel.: +49-731-502-5402; fax: +49-731-502-5409.
$^{1}$ On leave from the Frumkin Institute, Moscow.

0301-0104/02/$ - see front matter © 2002 Elsevier Science B.V. All rights reserved.
PII: S0301-0104(02)00763-2

the tip of an STM placed immediately above. We label the electronic states in the electrode and the tip by their quasi-momenta $k$ and $l$, and the active orbital on the adsorbate by $a$. As is common in the theory of electron-transfer reactions, we suppose that the Coulomb repulsion between the two spin states on the redox orbital is so large that only single occupancy needs to be considered, and the spin indices can be dropped since they only contribute an overall factor of two. Electron exchange via the adsorbate is coupled to a phonon bath representing the solvent and, possibly, inner-sphere modes. The resulting model Hamiltonian is [3,4]

$$
\begin{aligned}
H= & \sum_{k} \epsilon_{k} n_{k}+\sum_{l} \epsilon_{l} n_{l}+\epsilon_{\mathrm{a}} n_{a}+\sum_{k}\left[V_{k} c_{k}^{+} c_{a}\right. \\
& \left.+V_{k}^{*} c_{a}^{+} c_{k}\right]+\sum_{l}\left[V_{l} c_{l}^{+} c_{a}+V_{l}^{*} c_{a}^{+} c_{l}\right] \\
& +\frac{1}{2} \sum_{v} \hbar \omega_{v}\left(p_{v}^{2}+q_{v}^{2}\right)-n_{a}\left[\sum_{v} \hbar \omega_{v} g_{v} q_{v}\right].
\end{aligned}
$$

Here, $n$ denotes a number operator, $c^{+}$and $c$ are creation and annihilation operators. The first two terms represent the electronic states on the electrode and the tip, the third is for the adsorbate orbital. Electron exchange between the electrode and the adsorbate, and between the latter and the tip are effected by the forth and fifth terms, respectively. The modes of the phonon bath are labeled by $v$; $p_{v}$ and $q_{v}$ are the corresponding dimensionless momenta and coordinates. Finally, the $g_{v}$ are the coupling constants for the electron-phonon interaction. The total energy of reorganization is $\lambda=\sum_{v} \hbar \omega_{v} g_{v}^{2} / 2$.

The interaction of the adsorbate orbital with the two metals can be characterized by

$$
\begin{aligned}
& \Delta_{1}=\pi \sum_{k}\left|V_{k}\right|^{2} \delta\left(\omega-\epsilon_{k}\right), \\
& \Delta_{2}=\pi \sum_{l}\left|V_{l}\right|^{2} \delta\left(\omega-\epsilon_{l}\right).
\end{aligned}
$$

We employ the so-called wide band approximation [6], in which $\Delta_{1}$ and $\Delta_{2}$ are taken as constant. This is a good approximation when these quantities are much smaller than the electronic bands in the two metals, which is generally the case for electron transfer at metal electrodes.

In this work we are interested in the adiabatic limit, in which the electronic transitions are fast compared to the motion of the bath. The latter is treated as a classical system and represented by a single classical coordinate $q$, which we normalize such that $q=0$ corresponds to the equilibrium configuration for the oxidized state, and $q=1$ to that of the reduced state. The Green's functions for the electronic subsystems are easily calculated as a function of the solvent coordinate $q$ and are given in Appendix A.

In the adiabatic limit, for each value of $q$, there is a constant flux of electrons from one metal to the other, resulting in a an average occupation $\left\langle n_{a}\right\rangle$ of the adsorbate orbital, which is given by (see Appendix B):

$$
\begin{aligned}
\left\langle n_{a}\right\rangle= & \frac{1}{\pi} \int_{-\infty}^{E_{\mathrm{F}}^{\mathrm{el}}} \frac{\Delta_{1}}{(\omega-\tilde{\epsilon}(q))^{2}+\Delta^{2}} \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-\infty}^{E_{\mathrm{F}}^{\mathrm{tip}}} \frac{\Delta_{2}}{(\omega-\tilde{\epsilon}(q))^{2}+\Delta^{2}} \mathrm{~d} \omega,
\end{aligned}
$$

where $\Delta=\Delta_{1}+\Delta_{2}$ is the total energy broadening of the adsorbate orbital, and $\tilde{\epsilon}(q)=\epsilon_{\mathrm{a}}-2 \lambda q$ is the electronic energy of the adsorbate level as a function of the solvent coordinate. $E_{\mathrm{F}}^{\mathrm{el}}$ is the Fermi level of the electrode, and $E_{\mathrm{F}}^{\text {tip }}$ that of the tip. The rate of electrons passing from the electrode to the tip is then [4]

$$
k(q)=\frac{1}{\pi \hbar} \int_{E_{\mathrm{F}}^{\text {tip }}}^{E_{\mathrm{F}}^{\mathrm{el}}} \frac{\Delta_{1} \Delta_{2}}{(\omega-\tilde{\epsilon}(q))^{2}+\Delta^{2}} \mathrm{~d} \omega.
$$

The above equations completely define the adiabatic potential-energy surface, on which the system moves, and the rate of electron exchange at each position. Since the redox system interacts with two metals, the potential-energy surfaces differ from those encountered in normal electrochemical electron transfer. Therefore, we show a few examples. For this purpose, it is convenient to introduce the overpotential $\eta$ with respect to the electrode through

$$
\epsilon_{\mathrm{a}}-E_{\mathrm{F}}^{\mathrm{el}}=\lambda-e_{0} \eta
$$

and the tunneling bias through $V_{\mathrm{b}}=E_{\mathrm{F}}^{\mathrm{el}}-E_{\mathrm{F}}^{\text {tip }}$. We note that Eq. (5) is valid in the ideal situation in which the redox level is not affected by the bias or by double-layer effects. In a real experimental system, corrections may have to be applied. Fig. 1

shows a few potential-energy curves for zero overpotential and for various values of the interaction constants $\Delta_1$ and $\Delta_2$, which in this plot were taken as equal. Due to the interaction with the tip, the potential energy does not have a maximum at $q=1/2$, but it continues to rise till $\tilde{\epsilon}(q)$ has passed below the Fermi level of the tip. This effect is most easily understood for small interactions $\Delta_1$ and $\Delta_2$: In the absence of the tip, the potential-energy curve would have a cusp at $q=1/2$, where the occupation probability $\langle n_a\rangle$ would jump from zero to unity. In the presence of the tip the occupation probability is given by Eq. (3); in the limit of small $\Delta$ the integrands are proportional to $\delta(\omega-\lambda(1-2q))$ at zero overpotential. With the parameters of Figs. 1 and 2, $\langle n_a\rangle$ reaches a plateau of $1/2$ at $q=1/2$, and then jumps to $\langle n_a\rangle=1$ at $q=(1+e_0V_b/\lambda)/2$, which here takes the value of $1/2+1/6$. The potential energy continues to rise in the region where $\langle n_a\rangle$ has a plateau, since the solvent approaches the configuration appropriate for a filled orbital, while the occupancy stays constant. For larger interactions $\Delta_1$ and $\Delta_2$ the plateau in the occupancy is smeared out (see Fig. 2), and the potential-energy curves are more rounded.

For large interactions, the minimum near $q=1$ is higher than that at $q=0$, since the occupancy $\langle n_a(q=1)\rangle$ is not yet unity. So the equilibrium is disturbed by the presence of the tip.

![](./images/812449260321636352_2.jpg)

Fig. 1. Potential-energy curves at zero overpotential. System parameters: $\lambda=0.6$ eV; $V_b=0.2$ V. Full curve: $\Delta_1=\Delta_2=0.05$ eV; short dashes: $\Delta_1=\Delta_2=0.01$ eV; long dashes: $\Delta_1=\Delta_2=0.001$ eV.

![](./images/812449260321636352_3.jpg)

Fig. 2. Occupation probability $\langle n_a\rangle$ and transfer rate $k(q)$ as a function of the solvent coordinate $q$. Full curve: $\Delta_1=\Delta_2=0.05$ eV; long dashes: $\Delta_1=\Delta_2=0.01$ eV; short dashes: $\Delta_1=\Delta_2=0.001$ eV.

Application of an overpotential shifts the energy difference between the reduced and the oxidized states. The effect on the potential-energy curves is similar to that observed in the absence of the tip, but the actual shape of the curve is changed in the region near the maximum (see Fig. 3).

### 3. Stochastic molecular dynamics

In our model the system moves stochastically on the adiabatic potential-energy surface. In order

![](./images/812449260321636352_4.jpg)

Fig. 3. Potential-energy curves for various overpotentials. System parameters: $\lambda=0.6$ eV; $V_b=0.2$ V. $\Delta_1=\Delta_2=0.01$ eV. Full curve: $\eta=0$; dotted curve: $\eta=-0.1$ V; dashed curve: $\eta=0.1$ V.

to introduce stochastic motion we have imple- mented the collision model proposed by Kast et al. [7]. We have used this method before in an inves- tigation of adiabatic electron-transfer reactions [8]; we briefly review the main points. The system is coupled to a heat bath consisting of particles with a mass $m_{2}$. At each time step $\delta t$ of the simulation the system collides with a particle from the bath, whose velocity obeys the Maxwell-Boltzmann distribution. The implementation in terms of a generalized Verlet algorithm is given in the original paper, where the long-time behavior of the system is also examined. The coupling between the system and the bath is characterized by two quantities: by the mass ratio $m=m_{2} / m_{1}$ of the mass of the bath particles to the mass of the system, and by the time step $\delta t$, which is also the interval between subse quent collisions. As discussed by Kast et al., these parameters have to be chosen with some care if the system is to obey Boltzmann statistics with the desired temperature. Generally speaking, this method works well for small to intermediate fric- tion; details are given in the original paper. In our simulations, we chose the internal unit of time such that the period of the harmonic oscillator was $T=2 \pi / \omega=2 \pi$, and performed runs for $\delta t=0.01$ and for $m=0.01$, unless noted otherwise. With these values the system obeys Boltzmann statistics, and the kinetic temperature is practically equal to that of the bath [7].

The interaction with the bath exerts a certain 'friction' on the redox system. As a measure for the friction we use the coefficient

$$
\gamma=\frac{2 m}{(1+m) \delta t} \quad(6)
$$

In the limit where both $m$ and $\delta t$ tend to zero at constant $\gamma$, a free particle obeys the Langevin equation with $\gamma$ as friction coefficient [7]. Our simulations with $m=0.01$ correspond to low friction with $\gamma=1.98$. A few simulations were performed with a higher friction coefficient; as expected, they show a lower current, but the de- pendencies on the other system parameters remain unchanged, so they will not be discussed further.

The simulations were started with the system at the bottom of one of the two minima on the po- tential-energy curve; generally we took the abso- lute minimum, but if the simulation runs for a sufficiently long time the starting point does not influence the results. Due to the thermal fluctua- tions induced by the bath the system moves stochastically on the potential-energy curve; si- multaneously with the motion we evaluated the rate of electron exchange. In the course of its trajectory the system sometimes crosses the barrier between the two valleys. The simulations were continued until it had crossed the barrier a preset number of times; in the results displayed below the system has typically crossed the barrier several thousand times, and the average current was cal- culated.

## 4. Results of the simulations

As mentioned above two potentials, the over- potential and the tunneling bias, can be varied independently. Fig. 4 shows the current obtained for a small overpotential and increasing bias, and several values of the energy of reorganization $\lambda$. The results are easily understood within the Geri- scher picture [9] (see Fig. 5). Electron tunneling can only occur in the energy gap between the two Fermi levels. The center of the reduced density of states lies at an energy $\lambda$ below the Fermi level of the electrode. With increasing bias the Fermi level of the tip is pushed lower, and tunneling can occur

![](./images/812449260321636352_5.jpg)

Fig. 4. Current as a function of the tunneling bias $V_{b}$. System parameters: $\Delta_{1}=\Delta_{2}=0.01 eV ; \eta=0.01 ~V$ . (O) $\lambda=0.2 eV$ ;( $\square$ ) $\lambda=0.4 eV$ ; (x) $\lambda=0.6 eV$ . The current has been normal ized such that the maximum current is unity.

![](./images/812449260321636352_6.jpg)

Fig. 5. Gerischer picture of electron transfer applied to the present situation.

through a wider range of reduced states, and hence the current increases. When the bias is much larger than the reorganization energy, the current be- comes constant. The smaller $\lambda$, the steeper the initial rise of the current, and the sooner it be- comes constant. For large bias the current shows small fluctuations. These are caused by the defor- mation of the potential-energy curves by the bias; in terms of the Gerischer picture this means that the distributions are distorted by the bias.

The application of an overpotential $\eta$ shifts the two minima of the potential curve with respect to each other. The system spends most of the time in the deeper well, and the rate of electron transfer therefore depends critically on the energy of acti- vation needed to reach the transition region from the lower well. If the bias is small compared to the energy of reorganization, as in Fig. 3, this energy of activation is lowest for an overpotential close to zero. Indeed, it is easy to see that for a very small bias the current reaches its maximum exactly at $\eta=0$. Both the height of the maximum and rate of decrease of the current from this value are deter- mined by the energy of reorganization: The lower $\lambda$, the higher is the maximum current, and the faster is the decrease on both sides (see Fig. 6). Only the latter effect can be seen in the figure be- cause the current has been normalized.

It is of interest to compare our model with the experimental data of Tao mentioned in Section 1

![](./images/812449260321636352_7.jpg)

Fig. 6. Current as a function of the overpotential $\eta$. System parameters: $\Delta_{1}=\Delta_{2}=0.01$ eV; $V_{b}=0.1$ V. (●) $\lambda=0.2$ eV; (□) $\lambda=0.4$ eV; $(\times)\lambda=0.6$ eV. The currents have been normalized such that the maximum current is unity.

[1]. We have therefore performed calculations with parameters meant to represent the experimental situation: a strong coupling $\Delta_{1}=0.01$ V to the electrode, weak coupling $\Delta_{2}=0.001$ eV to the tip, and a small bias of $V_{b}=0.05$ V. The experimental data fit quite well to a reorganization energy of the order of $\lambda=0.4-0.6$ eV, which is close to the value suggested by Tao himself (see Fig. 7). However, in our model the current is determined both by $\lambda$ and by the change in occupation be- tween oxidized and reduced states effected by the overpotential.

![](./images/812449260321636352_8.jpg)

Fig. 7. Current as a function of the overpotential. System pa- rameters: $\Delta_{1}=0.01$ V, $\Delta_{2}=0.001$ V, $V_{b}=0.05$ V. Full line: $\lambda=0.6$ eV; dashed line: $\lambda=0.4$ eV; dotted line: $\lambda=0.2$ eV. The points are the experimental values from Tao [1].

## 5. Conclusions

In this work we have considered the case in the interaction of the adsorbed electroactive species both with the tip and the metal is so strong that the adiabatic limit holds. The electron transfer is thought to occur through resonant tunneling, while the system moves on a potential-energy surface determined by the electronic interactions, the tunneling bias, the overpotential, and the sol- vent reorganization. Our model is compatible to the only experimental data that exists, and offer a reinterpretation of these data.

There are several effects which we have not considered: nonadiabaticity for the tip-reactant interactions and the reorganization of quantum modes are the most important ones. They will be left for future work.

## Acknowledgements

W.S. acknowledges financial support by the Volkswagenstiftung with gratitude; A.M.K. would like to thank the Humboldt Foundation for a senior award.

## Appendix A

### A.1. The electronic Green's function

In the adiabatic limit the classical modes, with effective coordinate $q$, can be treated as an external parameter; so we can focus an the Green's function of the adsorbate with $q$-dependent energy $\tilde{\epsilon}$. We split the electronic Hamiltonian into two parts:

$$
H_{0}=\tilde{\epsilon} n_{a}+\sum_{k} \epsilon_{k} n_{k}+\sum_{l} \epsilon_{l} n_{l}, \tag{A.1}
$$

$$
\begin{aligned}
H_{T}= & \sum_{k}\left[V_{k} c_{k}^{+} c_{a}+V_{k}^{*} c_{a}^{+} c_{k}\right] \\
& +\sum_{l}\left[V_{l} c_{l}^{+} c_{a}+V_{l}^{*} c_{a}^{+} c_{l}\right]. \tag{A.2}
\end{aligned}
$$

Starting from the operator identity:

$$
G=G_{0}+G H_{T} G_{0} \tag{A.3}
$$

for the associated Green's functions, we calculate the following relations between the matrix elements:

$$
\left\langle a\left|G^{+}(z)\right| k\right\rangle=\frac{V_{k}^{*}}{z-\epsilon_{k}+\mathrm{i} \delta}\left\langle a\left|G^{+}(z)\right| a\right\rangle, \tag{A.4}
$$

$$
\left\langle a\left|G^{+}(z)\right| l\right\rangle=\frac{V_{k}^{*}}{z-\epsilon_{l}+\mathrm{i} \delta}\left\langle a\left|G^{+}(z)\right| a\right\rangle, \tag{A.5}
$$

$$
\begin{aligned}
& \left\langle a\left|G^{+}(z)\right| a\right\rangle=\frac{1}{z-\tilde{\epsilon}+\mathrm{i} \delta} \\
& \quad \times\left\{1+\sum_{k} V_{k}\left\langle a\left|G^{+}(z)\right| k\right\rangle+\sum_{l} V_{l}\left\langle a\left|G^{+}(z)\right| l\right\rangle\right\}. \tag{A.6}
\end{aligned}
$$

This system of equation can be solved; we obtain:

$$
\left\langle a\left|G^{+}(z)\right| a\right\rangle=\frac{1}{z-\tilde{\epsilon}+\mathrm{i} \Delta}, \tag{A.7}
$$

$$
\left\langle a\left|G^{+}(z)\right| k\right\rangle=\frac{V_{k}^{*}}{\left(z-\epsilon_{k}+\mathrm{i} \delta\right)(\tilde{\epsilon}+\mathrm{i} \Delta)}, \tag{A.8}
$$

$$
\left\langle a\left|G^{+}(z)\right| l\right\rangle=\frac{V_{l}^{*}}{\left(z-\epsilon_{l}+i \delta\right)(\tilde{\epsilon}+\mathrm{i} \Delta)}, \tag{A.9}
$$

where we have used relations of the form

$$
\begin{aligned}
\sum_{k} \frac{\left|V_{k}\right|^{2}}{z-\epsilon_{k}+\mathrm{i} \delta}= & \operatorname{Pr} \sum_{k} \frac{\left|V_{k}\right|^{2}}{z-\epsilon_{k}} \\
& -\mathrm{i} \pi \sum_{k}\left|V_{k}\right|^{2} \delta\left(z-\epsilon_{k}\right)=-\mathrm{i} \Delta_{1}, \tag{A.10}
\end{aligned}
$$

Pr denotes the principal value. In the last step the wide-band approximation was employed.

## Appendix B

### B.1. Occupation in the adiabatic limit

From the Green's function we calculate the matrix elements for transitions to the adsorbed state:

$$
\begin{aligned}
\langle a|\exp -\mathrm{i} H t| a\rangle & =\frac{\mathrm{i}}{2 \pi} \int \mathrm{d} \omega \mathrm{e}^{-\mathrm{i} \omega t}\left\langle a\left|G^{+}(z)\right| a\right\rangle, \quad \text { (B.1) } \\
& =\frac{\mathrm{i}}{2 \pi} \int \mathrm{d} \omega \frac{\mathrm{e}^{-\mathrm{i} \omega t}}{\omega-\tilde{\epsilon}+\mathrm{i} \Delta}, \quad \text { (B.2) } \\
& =\mathrm{e}^{-\mathrm{i} t(\tilde{\epsilon}-\mathrm{i} \Delta)} \rightarrow 0 \text { for } t \rightarrow \infty, \quad \text { (B.3) }
\end{aligned}
$$

$$
\begin{aligned}
\langle a|\exp -\mathrm{i} H t| k\rangle & =\frac{\mathrm{i}}{2 \pi} \int \mathrm{d} \omega \mathrm{e}^{-\mathrm{i} \omega t} \frac{V_{k}^{*}}{\left(z-e_{k}+\mathrm{i} \delta\right)(z-\tilde{\epsilon}+\mathrm{i} \Delta)}, & & (\mathrm{B} .4) \\
& =\frac{V_{k}^{*} \mathrm{e}^{-\mathrm{i} t \epsilon_{k}}}{\epsilon_{k}-\tilde{\epsilon}+\mathrm{i} \Delta} \quad \text { for } t \rightarrow \infty & & (\mathrm{B} .5)
\end{aligned}
$$

and similarly

$$
\langle a|\exp -\mathrm{i} H t| l\rangle=\frac{V_{l}^{*} \mathrm{e}^{-\mathrm{i} t \epsilon_{l}}}{\epsilon_{l}-\tilde{\epsilon}+\mathrm{i} \Delta} \quad \text { for } t \rightarrow \infty . \quad \text { (B.6) }
$$

Eq. (3) is then obtained by noting that the states below the Fermi levels of the electrode and the tip are occupied.

## References

[1] N. Tao, Phys. Rev. Lett. 76 (1996) 4066.
[2] W. Han, E.N. Durantini, T.A. Moore, A.L. Moore, D. Gust, P. Rez, G. Leatherman, G.R. Sealey, N.J. Tao, S.M. Lindsay, J. Phys. Chem 101 (1997) 10719.
[3] W.Schmickler, C. Widrig, J. Electroanal. Chem. 336 (1992) 213.
[4] W. Schmickler, Surf. Sci. 295 (1993) 43.
[5] A.M. Kuznetsov, J. Ulstrup, J. Phys. Chem. A 104 (2000) 11531; Probe Microsc. 2 (2001) 187.
[6] R. Brako, D.M. Newns, Rep. Prog. Phys. 2 (1989) 655.
[7] S.M. Kast, K. Nicklas, H.J. Bär, J. Brickmann, J. Chem. Phys. 100 (1994) 566; J. Chem. Phys. 104 (1996) 3732.
[8] A.N. Kuznetsov, W. Schmickler, Chem. Phys. Lett. 327 (2000) 314.
[9] H. Gerischer, Z. Phys. Chem. NF 26 (1969) 21.