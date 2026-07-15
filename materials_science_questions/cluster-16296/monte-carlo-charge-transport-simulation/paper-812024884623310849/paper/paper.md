# Introducing energy broadening in semiclassical Monte Carlo simulations

Giulio Ferrari · A. Asenov · M. Nedjalkov · C. Jacoboni

Published online: 24 January 2007
© Springer Science + Business Media, LLC 2007

**Abstract** Combining an insight on the quantum transport given by the Wigner function formalism and the classical perturbation theory, an algorithm has been developed that allows the introduction of collisional broadening in semiclassical electron transport Monte Carlo (MC) simulations. In the proposed algorithm, electron energy and momentum are treated as independent variables; the laws of energy and momentum conservation are fulfilled at each scattering event, but the relationship between energy and momentum is not given by the traditional expression, since Bloch states are not eigenstates of the total Hamiltonian. The results obtained for a simple model semiconductor demonstrate that the non-physical instabilities observed in previous attempts to introduce collisional broadening in semiclassical MC simulations have been removed. The algorithm is suitable for application in MC simulations of realistic device models.

**Keywords** Monte Carlo simulation · Collisional broadening · Quantum corrections

---

G. Ferrari (⊗) · A. Asenov
Device Modelling Group, Dept. Electronics & Electrical Engineering, University of Glasgow, G12 8LT Glasgow, United Kingdom.
e-mail: g.ferrari@elec.gla.ac.uk

M. Nedjalkov
AMADEA Group, Inst. for Microelectronics, TU Wien, Gußhausstr. 27–29/E360, 1040 Wien, Austria.

C. Jacoboni
National Research Center S3, INFM-CNR and Dipartimento di Fisica Università di Modena e Reggio Emilia, Via Campi 213/A, I-41100 Modena, Italy.

---

## 1 Introduction

The scaling of electronic devices, the implementation of new materials and the realisation of new structures is forcing the modelling community to take into account the quantum mechanical behaviour of the systems under investigation [1–3]. The quest for development of a fully quantum mechanical formalism, able to describe rigorously the phonon-electron interaction and at the same time applicable to simulations of real devices, is still open [4–7]. Therefore, semiclassical MC simulation is still the most appropriate and efficient, from a computational point of view, tool to study high-field transport in 3D systems which can take into account the full band structure and can include all the relevant scattering mechanisms [8]. However, the reliability of MC simulations based on the Fermi golden rule, was brought into question at the point when the simulated system required very high phonon scattering rates [9]: The main issue of concern was the need to consider the effect of collisional broadening (CB). Since then, several attempts have been made to introduce corrections to the traditional MC codes in order to take into account this effect [10–12]. In the heart of these approaches is the violation of energy conservation between two electron states connected through a phonon process: The possible transitions were of the following type:

$$
E_{j a}=E_{j b} \pm \hbar \omega_{p h}+\delta E_{j}, \tag{1}
$$

where $E_{j b}$ and $E_{j a}$ are the energies of the electron before and after the $j$-th scattering event, $\hbar \omega_{p h}$ is the energy of the phonon involved in the process, and $\delta E_{j}$ is a stochastically sampled deviation from the energy conservation, which is usually chosen from a Lorentzian distribution [11]. In the papers mentioned above where this technique has been implemented, the results have always shown non-physical

![](./images/812024884623310849_1.jpg)

instabilities due to the accumulation of the CB contributions through a sequence of scattering events. This highlights the need for a more rigorous analysis of the quantum dynamics of the scattering process, that leads to the removal of the observed energy instability. Moreover, the dependence of the width of CB on the time $\Delta t$ available for each scattering event to be completed is determined by the uncertainty principle and is of the order of:

$$
\sigma_{E j}=\frac{\hbar}{t_{j}-t_{(j-1)}}. \tag{2}
$$

Taking into account the above considerations, an exploratory CB algorithm has been implemented in a simple bulk MC code and its effects have been studied in detail. Initial satisfactory results have been obtained, and improvements are already in progress.

## 2 Electron-phonon scattering

The first problem to be solved when including CB in the electron-phonon processes is the preservation of the long term energy conservation. A number of observations lead to the conclusion that both energy and momentum conservation laws are satisfied at each scattering event:
1.  The overall energy in transport is conserved because the Hamiltonian for the total system of the electron(s) and phonons is time independent. This means that the electron-phonon scattering is an inelastic, phase-breaking process only with respect to the electron or phonon system alone, while it is an elastic and coherent process for the coupled system.
2.  In an electron-phonon interaction the crystal-momentum conservation, in a homogeneous system, is guaranteed by the matrix elements.
3.  An electron can be scattered to a state with an energy not given by the simple balance between the energy before scattering and the energy of the involved phonon. This is due to the fact that the final state, considered in transition, is an eigenstate of the unperturbed Hamiltonian, which is not a state of well defined energy of the electron system interacting with the phonons.

Therefore we may assume that the energy is conserved at each scattering event. In fact, in the two-time Wigner-function approach a frequency contribution is transferred to/from the electron at each scattering process, equal to the frequency of the phonon [6]. However, we have to abandon the simple relation:

$$
E=\frac{p^{2}}{2 m}, \tag{3}
$$

because, in the case of collisions, several values of the energy $E$ are possible for each value of the momentum $p$ (see the results in Fig. 3 for an example). The energy exchanged at each scattering event is determined by the phonon frequency $\omega_{p h}$, and the momentum exchanged is determined by the phonon wave-vector $q$. But, the final electron energy and electron momentum are not necessarily related by (3).

Our derivation of the distribution of possible final states is based on the perturbation theory. The traditional derivation of the Fermi golden rule is interrupted before the limit for $\Delta t \to \infty$, when the probability of transition for time unit from an initial state of energy $\omega_{i}$ to a final state of energy $\omega_{f}$ through the emission or absorption of a phonon of energy $\omega_{p h}$ is proportional to:

$$
\left|a_{f i}\right|^{2} \propto \frac{\sin ^{2}\left(\frac{\omega_{f}-\omega_{i} \pm \omega_{p h}}{2} \Delta t\right)}{\left(\frac{\omega_{f}-\omega_{i} \pm \omega_{p h}}{2} \Delta t\right)^{2}}. \tag{4}
$$

From the above formula it is observable that the distribution of energies of the possible final states is broadened and the broadening depends on the time interval $\Delta t$ after the preparation of the initial state $i$. Figure 1 illustrates the function from Eq. (4). Figure 1(a) shows the probability distribution of the final states for an absorption of a phonon $\omega_{p h}$ after a time $\Delta t$ from the moment when the electron state with an energy of $E_{i}$ was prepared; Fig. 1(b) illustrates the probability distribution of the final states for an emission of a phonon. In this particular case, thanks to the fact that final states not accessible classically have now a non-zero probability to be occupied, a process not classically possible can indeed occur. The width of the distributions depends on the interval $\Delta t$.

## 3 CB-MC algorithm

The MC algorithm that we are proposing follows the scheme of the traditional semiclassical MC simulations [8], but it deals with the electron energy $E$ and momentum $p$ as independent variables.

**Initial state.** The semiclassical simulation starts at time $t=t_{0}$; the initial momentum $p_{0}$ is generated according to the thermal distribution and the initial energy $E_{0}$ is determined by (3).

**First flight.** The duration $t_{1}$ of the first flight is determined in a traditional way, according to the scattering probabilities, including self-scattering. The value of the momentum at the end of the first flight $p_{1 b}$ (where b stands for "before" the scattering event) is determined classically: If an electric field $F$ is acting on the system, the variation is is:

$$
\Delta p_{(t 1-t 0)}=e F\left(t_{1}-t_{0}\right) \tag{5}
$$

![](./images/812024884623310849_2.jpg)

Fig. 1 Plot of the function (4)
for a phonon of energy
$\hbar\omega_{ph}=450K$. (a): In the case
of absorption of the phonon at a
time $\Delta t=0.15ps$ after the
preparation of the initial state
$E_i=250K$; (b): In the case of
emission of the phonon at a time
$\Delta t=0.05ps$ after the
preparation of the initial state:
this process is classically
impossible, while quantistically
the broadened distribution of
possible final states extends to
states with positive unperturbed
energies, allowing this process

![](./images/812024884623310849_3.jpg)

First scattering. At the time $t_1$ a scattering event occurs.
Before each scattering event the space position can be calcu-
lated using a classical formula:

$$
z(t_1)=z(t_0)+\frac{p_1}{m}(t_1-t_0)+\frac{1}{2}\frac{eF}{m}(t_1-t_0)^2. \tag{6}
$$

Knowing the position of electrons allows a relatively sim-
ple implementation of this algorithm in a device simulation,
where the spatial configuration of the system is fundamental.
The energy of the electron is calculated as:

$$
E_{1b}=E(t_0)+\left(\frac{p^2(t_1)-p^2(t_0)}{2m}\right). \tag{7}
$$

At the scattering time $t_1$, the type of scattering is determined
using the probabilities $P(E_{1b})$. Here we use the electron en-
ergy for the probability instead of the energy linked to the
density of final states through $p^2/2m$ as a first approximation
and it is justified by the fact that the integral of the function
(4) is equal to 1 at all times: This means that the proba-
bility of scattering for time unit to states different from the
state fulfilling the energy conservation becomes non-zero,

![](./images/812024884623310849_4.jpg)

reducing the probability of scattering to the energy-conserving state. For simplicity, in this first attempt the threshold processes that have a negative conserving energy (as the one described in Fig. 1(b)) have not been considered. In future works, these processes will be included by evaluating the scattering probabilities using a convolution of the function (4) with the density of states, giving rise to negative values of the energy in the distributions.

If a self scattering is chosen, then the flight continues. If another type of scattering is chosen, the new values for the electron energy and momentum are determined as follows:

$$
E_{1 a}=E_{1 b} \pm \hbar \omega_{p h} ; \tag{8}
$$

$$
\delta E_{1}=(r-0.5) \sigma_{E_{1}} ; \quad 0<r<1 \tag{9}
$$

$$
\frac{p_{1 a}^{2}}{2 m}=E_{1 b} \pm \hbar \omega_{p h}+\delta E_{1}. \tag{10}
$$

The sign $\pm$ corresponds to an absorption or emission process. The new value of $p_{1 a}$ is calculated starting from the value of the electron energy $E_{1 b}$. In this way the broadening due to the duration of the new flight is taken into account, but, at the same time, there is no accumulation of CB. After calculating $p_{1 a}$ according to the type of scattering mechanism, then the $q$ of the phonon is determined.

Successive history. During the successive flights the momentum varies classically, with a velocity determined by $p$. Under the action of an electric field $F$, the energy varies as described by (7). The position at the end of the flights is calculated following Eq. (6). The successive scattering processes are treated as the first one. It is fundamental to note once more that there is no memory of the energy broadening taken in the previous scattering events: The energy spreading given by Eq. (2) is calculated according to the time interval $(t_{j}-t_{j-1})$ and the new momentum is given by the electron energy modified by this broadening.

## 4 Results
In order to perform an initial analysis of the effect of CB and of the reliability of the algorithm, we have chosen a model semiconductor system. The system simulated is bulk silicon $(m^{*}=.32)$, with a single spherical parabolic band; the electrons are subject to momentum randomising scattering through the absorption and emission of monoenergetic phonons $(\omega_{p h}=450 K)$; the initial electron energy is $300 K$ and the electrons are accelerated in uniform electric field. A single carrier is followed through a series of free flights and scattering events, until enough statistics are collected, so that the results are independent of the initial conditions.

Figure 2 compares the electron-energy distributions with and without CB for an electric field $F=10 kV / cm$. In the traditional MC simulation, the electron energy reproduces a heated Maxwell-Boltzmann distribution. The CB-MC simulation shows a distribution close to the one obtained via the Fermi golden rule. There is some increase in the high-energy tail of the distribution, but far less than that observed in previous works [10,11].

Figure 3 compares the dispersion relation between the electron energy and the modulus of the momentum $|\vec{p}|$ obtained from a traditional MC simulation, where the relation is a function expressed by (3), and from a CB-MC simulation, where the relation is broadened and a distribution of $E$ values corresponds to each value of the momentum $|\vec{p}|$, and vice versa.

Fig. 2 Comparison of the energy distributions between a traditional MC simulation and a CB-MC one. The applied field is $F=10 kV / cm$. The high-energy tail of the distribution increases but it does not show the runaway observed with the previous approaches

![](./images/812024884623310849_5.jpg)

![](./images/812024884623310849_6.jpg)

Fig. 3 Dispersion relation of the electron energy $E$ and the modulus of the momentum $|\vec{p}|$: A comparison between the result obtained for a traditional MC simulation, where $E=p^{2}/2m$, and a CB-MC simulation, where the relation is shown to be broadened. In the latter case, a distribution of possible values of $E$ corresponds to each value of the momentum $|\vec{p}|$ and vice versa. The applied field is $F=10kV/cm$

![](./images/812024884623310849_7.jpg)

Fig. 4 Average electron energy as a function of the applied field. The CB-MC average energy is consistently higher than the traditional MC one. No instability is found

The simulations have been carried out for a range of values of the applied field $F$. In Fig. 4 the average electron energy versus the applied field is shown: The average energy with CB included is consistently higher than the one obtained with traditional MC simulations, but the heating of the system is maintained under control.

## 5 Conclusions
An improved algorithm for the inclusion of CB in semiclas- sical MC simulations has been proposed. A basic theoretical analysis of the electron-phonon scattering from a quantum point of view has been outlined and a modification to the tra- ditional MC algorithm has been developed on the basis of the perturbation theory. This analysis justifies, as a first approx- imation, the choice of the scattering event with the energy- conserving electron energy. The same arguments show also the path for a successive and more accurate extension, in or- der to include threshold processes. Our algorithm allows for CB at each scattering event, depending on the time interval between two successive phonon interactions. At the same time, it prevents the accumulation of CB corrections that lead in the past to non-physical growth of the high-energy tail of electron distributions. The results obtained from a model semiconductor system show no artificial runaway in the electron energy distributions. All the carrier distributions obtained with CB-MC simulations exhibit some important deviations from those obtained with traditional MC.

Acknowledgments One of the authors (G.F.) would like to express his gratitude to Karol Kalna and Antonio Martinez for fecund discussions and valuable suggestions. This work has been partially supported by the U.S. Office of Naval Research (contract No. N00014-98-1-0777).

## References
1. Ancona, M.G. et al.: IEEE T. Electron Dev. 47, 2310 (2000)
2. Ferry, D.K. et al.: IDEM 00 Tech. Dig., 287 (2000)
3. Tsuchiya, H. et al.: J. Appl. Phys. 89, 4023 (2005)
4. Register, L.F.: Int. J. High Speed Electron. Syst. 9, 251(1998)
5. Datta, S.: Superlattices Microstruct. 28, 253 (2000)
6. Jacoboni, C. et al.: Rep. Prog. Phys. 67, 1033 (2004)
7. Iotti, R. et al.: Phys. Rev. B 72, 125347 (2005)
8. Jacoboni, C. et al.: Rev. Modern Phys. 55, 645 (1983)
9. Capasso, F. et al.: J. Appl. Phys. 53, 3324 (1982)
10. Chang, Y.-C. et al.: Appl. Phys. Lett. 42, 76 (1983)
11. Reggiani, L. et al.: Phys. Rev. B 36, 6602 (1987)
12. Špička, V. et al.: Phys. Rev. Lett. 73, 3439 (1994)

![](./images/812024884623310849_8.jpg)