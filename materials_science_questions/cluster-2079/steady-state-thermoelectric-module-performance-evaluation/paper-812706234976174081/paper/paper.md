# Heat-Recovery Solar Cell

Kenji Kamide, $^{1,}$* Toshimitsu Mochizuki, $^{1}$ Hidefumi Akiyama, $^{2,3}$ and Hidetaka Takato $^{1}$

$^{1}$ Renewable Energy Research Center, National Institute of Advanced Industrial Science and Technology (AIST), Koriyama, Fukushima 963-0298, Japan
$^{2}$ The Institute for Solid State Physics (ISSP), The University of Tokyo, Kashiwa, Chiba 277-8581, Japan
$^{3}$ Advanced Operando-Measurement Technology Open Innovation Laboratory (OPERANDO-OIL), Kashiwa, Chiba 277-8581, Japan

![](./images/812706234976174081_1.jpg)
(Received 14 September 2018; revised manuscript received 25 October 2019; published 2 December 2019)

Heat-recovery (HERC) solar cell—a concept of solar cells utilizing the heat for improving the power conversion efficiency—is presented. HERC solar cell, characterized by an absorber hotter than electrodes, recovers heat as electricity to have high conversion efficiency exceeding the detailed balance limit when carrier-energy filtering is employed. Being different from hot-carrier solar cells, HERC solar cell does not require fast carrier extraction within the thermalization time, which largely improves its feasibility (feasible even with Si). An increment in the conversion efficiency originates from thermoelectricity produced by the temperature difference. Requirements for materials of the filtering layers are also given based on a nonideal device simulation with the thermoelectric properties.

DOI: 10.1103/PhysRevApplied.12.064001

## I. INTRODUCTION

Improving power conversion efficiencies is a clear target of solar-cell researches, while the cost reduction and reliability improvement are always the practical requirements for promoting new technologies. Si solar cells have been the first choice of the solution to achieve high efficiency within the practical requirements. Recently at the research level [1], the power conversion efficiency of single-junction Si solar cell has almost reached the theoretical limit known as the Shockley-Queisser (SQ) limit [2–4]. This in turn means that a concept to surpass the SQ limit is necessary to achieve further developments. Multijunction solar cell [5,6] is an approach to overcome the SQ limit of single-junction solar cells. However, they have not been commercialized due to cost issues. Hot-carrier solar cells [7–10] and intermediate-band solar cells [11] are promising concepts to exceed the SQ limit, whereas the proofs of concepts have not yet been achieved so far. At the present moment, a practical concept feasible with Si is desired. In this Paper, we present a concept “heat-recovery (HERC) solar cell” [12] that can be realized also in Si-based solar cell not only in solar cells made of strongly absorbing direct-gap semiconductor materials.

It is known that a large amount of energy is being lost as heat in solar cells, which amounts to roughly 50% of the solar energy in Si solar cells. Therefore, there is considerable room to improve the efficiency if a part of the heat could be converted to electricity. Hot-carrier solar cell [7–10] is a concept to reduce the heat loss by extracting hot carriers at high temperature $T_{\text{carrier}}$ before they lose the energy by cooling down to the lattice temperature $T_{\text{ph}}$. Therefore, the concept utilizes a nonequilibrium condition, $T_{\text{carrier}} > T_{\text{ph}}$. Considering the typical thermalization time of hot carriers, roughly 1 ps [13–17], thickness of absorber must be less than hundreds of nanometers to realize the concept. However, with such an ultrathin absorber, sufficient absorption of light becomes difficult even with strongly absorbing materials and almost impossible in a weak absorber like Si. As explained below, HERC solar cell utilizes another nonequilibrium condition and allows for exceeding the SQ limit without requiring fast carrier extraction.

To simplify the discussion, here we consider transmission of sub-band-gap photons, radiative recombination, and carrier thermalization in the absorber and electrodes are the energy-loss channels present in our model. The absorber is thick enough to ensure perfect absorption of above-band-gap photons, which is the case for 100-$\mu$m-thick Si with light-trapping texture.

## II. CONCEPT

HERC solar cell consists of an absorber and two electrodes (electron and hole reservoirs) to which electrons and holes in the absorber are extracted separately [18–20], as shown in Fig. 1(a). These are common to any solar cell. On the other hand, HERC solar cell is distinguished from normal solar cells by the following

$^{*}$kenji.kamide@aist.go.jp

![](./images/812706234976174081_2.jpg)

FIG. 1. Schematic diagrams for HERC solar cell: (a) the basic structure and (b) a function of the energy-filtering layers.

two points: (i) carrier-energy filtering layers are placed between the absorber and electrodes in order to control the energies of passing carriers; (ii) lattice temperature of the absorber ($\equiv T_{\text{ph}}$) is higher than that of the electrodes and the ambient ($\equiv T_{c}$). Here we should mention that condition (ii) is different from the requirement for hot-carrier solar cells [7], i.e., $T_{\text{carrier}} > T_{\text{ph}} = T_{c}$. HERC solar cell works with $T_{\text{carrier}} = T_{\text{ph}} > T_{c}$, on the other hand.

The carrier-energy filtering layers in (i) are made of semiconductors with a band gap larger than that of the absorber ($\equiv E_{g}$, 1.12 eV for Si), which create potential barriers of height $E_{b}$ restricting the kinetic energies of carriers to pass to $E_{e(h)} > E_{b}$, as shown in Fig. 1(b). To maintain condition (ii) without an external heater, it is necessary to collect and store the heat originating from the sun light inside the absorber. Thus, the filtering layers are preferably made of materials with low thermal conductivities.

### III. FORMULATION

Our simulation is based on the nonequilibrium theory of solar cells [13]. The nonequilibrium theory describes the dynamics of the carriers in the absorber, the thermalization and extraction processes, by introducing two time scales $\tau_{\text{ph}}$ and $\tau_{\text{out}}$ into the theory [13]. It provides a set of rate equations to determine the distribution functions in the microscopic states of electrons and holes in the absorber.

Here we briefly summarize the nonequilibrium theory applied to HERC solar cell. Several assumptions have been made in the theory: we consider an ideal case with (a) perfect absorption of photons with $E > E_{g}$ [i.e., an optically thick absorber where the absorptivity can be approximated by a step function $\theta(E - E_{g})$ [13,18,21]], (b) perfect carrier selectivity for the contacts, (c) perfect antireflection of photons at the front surface, (d) perfect passivation by which surface recombination of the carriers can be negligible, and (e) thickness of the absorber is much smaller than the diffusion length of the carriers so that the carrier distribution functions can be regarded as homogeneous inside the absorber. The assumptions from (a) to (e) are used in the SQ theory as an ideal case. In addition, we assume that (f) all microscopic states of carriers with the same energy have an equal probability, independent of their momentum directions (i.e., dependent solely on the kinetic energy). Our formulation is simplified by the last assumption (f), which will not affect strongly the main results.

### A. Rate equations for carrier distribution functions in the absorber

Under the above assumptions, the nonequilibrium theory provides a set of rate equations to determine distribution functions in the microscopic states of electrons ($n_{E_{e}}^{e}$) and holes ($n_{E_{h}}^{h}$) in the absorber,

$$
\frac{d}{d t} n_{E_{e}}^{e}=R_{E_{e}}^{e, \text { sun }}-R_{E_{e}}^{e, \text { rad }}-R_{E_{e}}^{e, \text { out }}-R_{E_{e}}^{e, \text { phonon }}, \quad \text { (1) }
$$

$$
\frac{d}{d t} n_{E_{h}}^{h}=R_{E_{h}}^{h, \text { sun }}-R_{E_{h}}^{h, \text { rad }}-R_{E_{h}}^{h, \text { out }}-R_{E_{h}}^{h, \text { phonon }}. \quad \text { (2) }
$$

On the right hand side of Eqs. (1) and (2), the first term is the generation rate by sun-light absorption, the second term is the radiative-recombination loss rate, the third term is the carrier-extraction rate, and the last term is the carrier-thermalization rate by intraband carrier-phonon scatterings, which are given in functional forms of $n_{E_{e}}^{e}$ and $n_{E_{h}}^{h}$ in Ref. [13].

The expressions for generation and radiative loss rates depend on whether the absorber is made of direct-gap or indirect-gap semiconductors, i.e., whether the generation and recombination are accompanied by direct or indirect transitions. For indirect-gap semiconductors (e.g., in Si), we find

$$
\begin{aligned}
R_{E_{e}}^{e, \text { sun }} & =\int_{E_{g}+E_{e}}^{\infty} \frac{j^{\text {sun }}(E) \times \mathcal{D}_{h}\left(E-E_{g}-E_{e}\right) / w}{\int_{0}^{E-E_{g}} \mathcal{D}_{e}\left(E^{\prime}\right) \mathcal{D}_{h}\left(E-E_{g}-E^{\prime}\right) d E^{\prime}} d E \\
& =\int_{0}^{\infty} \frac{j^{\text {sun }}\left(E_{g}+E_{e}+E_{h}\right) \times \sqrt{E_{h}}}{\pi w d_{e}\left(E_{e}+E_{h}\right)^{2} / 8} d E_{h},
\end{aligned}
$$

$$
\begin{aligned}
R_{E_{h}}^{h, \text { sun }} & =\int_{E_{g}+E_{h}}^{\infty} \frac{j^{\text {sun }}(E) \times \mathcal{D}_{e}\left(E-E_{g}-E_{h}\right) / w}{\int_{0}^{E-E_{g}} \mathcal{D}_{e}\left(E^{\prime}\right) \mathcal{D}_{h}\left(E-E_{g}-E^{\prime}\right) d E^{\prime}} d E \\
& =\int_{0}^{\infty} \frac{j^{\text {sun }}\left(E_{g}+E_{e}+E_{h}\right) \times \sqrt{E_{e}}}{\pi w d_{h}\left(E_{e}+E_{h}\right)^{2} / 8} d E_{e},
\end{aligned}
$$

where $\mathcal{D}_{e}(E)(=d_{e}\sqrt{E})$ and $\mathcal{D}_{h}(E)(=d_{h}\sqrt{E})$ are the density of states (per unit volume) of conduction electrons and valence holes and $d_{e(h)}=(2 m_{e(h)}^{*})^{3 / 2}/(2 \pi^{2} \hbar^{3})$ under the effective mass approximation. $j^{\text{sun}}(E)$ is the solar spectrum for the photon number current (per unit area, per unit time, and per unit energy), approximated by blackbody radiation

at $T_{\text{sun}} = 6000$ K under the AM0 condition [18]

$$
j^{\text{sun}}(E) = \mathcal{C}\mathcal{R} \times \frac{c}{4} \left( \frac{R_S}{L_{\text{ES}}} \right)^2 \mathcal{D}_\gamma^0(E) \times f_{T_{\text{sun}}}^B(E), \quad (5)
$$

where $\mathcal{C}\mathcal{R}$ is the concentration ratio, $c$ is the speed of light, $R_S$ is the radius of the sun, $L_{\text{ES}}$ is the distance between the earth and the sun, $\mathcal{D}_\gamma^0(E) = (1/3\pi^2)(\hbar c)^{-3} \times 3E^2$ is the photonic density of states in a vacuum, and $f_{T_{\text{sun}}}^B(E) = [\exp(E/k_B T_{\text{sun}}) - 1]^{-1}$ is the Bose-Einstein distribution function at energy $E$ with a temperature $T_{\text{sun}}$ and chemical potential of zero. The radiative loss rates for indirect-gap semiconductors are

$$
\begin{aligned}
R_{E_e}^{e,\text{rad}} &= \frac{c}{2\pi^2 w} \left( \frac{1}{\hbar c} \right)^3 \\
& \quad \times \int_0^\infty \frac{(E_g + E_e + E_h)^2 \sqrt{E_h} \times n_{E_e}^e n_{E_h}^h}{(\pi/8) d_e (E_e + E_h)^2} dE_h, \quad (6)
\end{aligned}
$$

$$
\begin{aligned}
R_{E_h}^{h,\text{rad}} &= \frac{c}{2\pi^2 w} \left( \frac{1}{\hbar c} \right)^3 \\
& \quad \times \int_0^\infty \frac{(E_g + E_e + E_h)^2 \sqrt{E_e} \times n_{E_e}^e n_{E_h}^h}{(\pi/8) d_h (E_e + E_h)^2} dE_e. \quad (7)
\end{aligned}
$$

Terms responsible for the carrier extraction, $R_{E_e}^{e,\text{out}}$ and $R_{E_h}^{h,\text{out}}$, are given by

$$
R_{E_e}^{e,\text{out}} = \frac{\theta(E_e - E_b)}{\tau_{\text{out}}} \left[ n_{E_e}^e - f_{T_c}^F (E_g + E_e - \mu_c) \right], \quad (8)
$$

$$
R_{E_h}^{h,\text{out}} = \frac{\theta(E_h - E_b)}{\tau_{\text{out}}} \left\{ n_{E_h}^h - f_{T_c}^F [E_h - (-\mu_v)] \right\}, \quad (9)
$$

where $f_T^F(E) \equiv 1/\{\exp[E/(k_B T)] + 1\}$ is the Fermi distribution function, and the step function $\theta(x)$ describes the effect of carrier-energy filtering layers. The carrier-extraction time $\tau_{\text{out}}$ can be regarded as a time scale, which the photogenerated carriers spend inside the absorber until they are extracted to the contacts.

Carrier-thermalization terms due to the intraband carrier-phonon scattering are

$$
\begin{aligned}
& R_{E_{e(h)}}^{e(h),\text{phonon}} \\
& = \int_0^\infty W_{E_{e(h)}, E_{e(h)}-\epsilon}^- \Bigg\{ n_{E_{e(h)}}^{e(h)} \left( 1 - n_{E_{e(h)}-\epsilon}^{e(h)} \right) \\
& \quad \times \left[ 1 + f_{T_{\text{ph}}}^B (\epsilon) \right] - n_{E_{e(h)}-\epsilon}^{e(h)} \left( 1 - n_{E_{e(h)}}^{e(h)} \right) f_{T_{\text{ph}}}^B (\epsilon) \Bigg\} d\epsilon
\end{aligned}
$$

$$
\begin{aligned}
& - \int_0^\infty W_{E_{e(h)}+\epsilon, E_{e(h)}}^+ \Bigg\{ n_{E_{e(h)}+\epsilon}^{e(h)} \left( 1 - n_{E_{e(h)}}^{e(h)} \right) \\
& \quad \times \left[ 1 + f_{T_{\text{ph}}}^B (\epsilon) \right] - n_{E_{e(h)}}^{e(h)} \left( 1 - n_{E_{e(h)}+\epsilon}^{e(h)} \right) f_{T_{\text{ph}}}^B (\epsilon) \Bigg\} d\epsilon,
\end{aligned}
$$

where $W_{E_{e(h)}, E_{e(h)}-\epsilon}^-$ and $W_{E_{e(h)}+\epsilon, E_{e(h)}}^+$ represent the transition rates per unit energy. Here we assume that deformation-induced LA phonon scattering dominates the carrier thermalization in Si. In this case, the transition rates are given by

$$
W_{E_{e(h)}, E_{e(h)}-\epsilon}^- = C_{\text{ph}}^{e(h)} \frac{\epsilon^2}{\sqrt{E_{e(h)}}} \times \theta \left( \epsilon_{\text{cut}}^{e(h),-} - \epsilon \right), \quad (11)
$$

$$
W_{E_{e(h)}+\epsilon, E_{e(h)}}^+ = C_{\text{ph}}^{e(h)} \frac{\epsilon^2}{\sqrt{E_{e(h)}}} \times \theta \left( \epsilon_{\text{cut}}^{e(h),+} - \epsilon \right), \quad (12)
$$

where $C_{\text{ph}}^{e(h)} \equiv \left( a_{\text{def},c(v)}^2 \sqrt{m_{e(h)}^*/2} \right)/4\pi \hbar^4 v_A^4 \rho_A$, $a_{\text{def},c(v)}$ the deformation potentials approximated at the bottom (top) of the conduction (valence) band, $v_A$ the phonon velocity, and $\rho_A$ the mass density of the absorber. The step function in the transition rates limits the integration range in Eq. (10) to $0 \leq \epsilon \leq \epsilon_{\text{cut}}^{e(h),\pm}$, whereas the high-energy cutoffs $\epsilon_{\text{cut}}^{e(h),\pm}$ are given by

$$
\begin{aligned}
\epsilon_{\text{cut}}^{e(h),-} \equiv & \min \bigg[ E_{e(h)}, \epsilon_{\text{cut}}^{\text{ph}}, \\
& \left. 2v_A \left( \sqrt{2m_{e(h)}^* E_{e(h)}} - m_{e(h)}^* v_A \right) \right], \quad (13)
\end{aligned}
$$

$$
\epsilon_{\text{cut}}^{e(h),+} \equiv \min \left[ \epsilon_{\text{cut}}^{\text{ph}}, 2v_A \left( \sqrt{2m_{e(h)}^* E_{e(h)}} + m_{e(h)}^* v_A \right) \right]. \ (14)
$$

The cutoffs originate from the momentum and energy conservation in the LA phonon scattering process, and therefore, depend on the Debye energy $\epsilon_{\text{cut}}^{\text{ph}}$ (approximately 50 meV for Si), effective mass and energy of carriers, and phonon velocity. Based on the result, the thermalization time $\tau_{\text{ph}}^{e(h)} [E_{e(h)}]$ estimated by

$$
\begin{aligned}
\frac{1}{\tau_{\text{ph}}^{e(h)} [E_{e(h)}]} &= C_{\text{ph}}^{e(h)} \Bigg( \int_0^{\epsilon_{\text{cut}}^{e(h),-}} \frac{\epsilon^2 \left[ 1 + f_{T_{\text{ph}}}^B (\epsilon) \right]}{\sqrt{E_{e(h)}}} d\epsilon \\
& \quad + \int_0^{\epsilon_{\text{cut}}^{e(h),+}} \frac{\epsilon^2 f_{T_{\text{ph}}}^B (\epsilon)}{\sqrt{E_{e(h)}}} d\epsilon \Bigg),
\end{aligned}
$$

ranges between subpico and picoseconds [13].

### B. Macroscopic currents for particle number and energy

Based on the microscopic rate equations, Eqs. (1) and (2), macroscopic current for particle numbers and

energy can be calculated by integrating the equations over all the microscopic states. The total particle numbers of electron and hole, $N_e$ and $N_h$, generated in the absorber per unit time per unit area (we assume a planer solar cell with a thickness $w$) are

$$
\begin{aligned}
\frac{d N_{e}}{d t} &=w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) \frac{d}{d t} n_{E_{e}}^{e} d E_{e} \\
&=w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(R_{E_{e}}^{e, \text { sun }}-R_{E_{e}}^{e, \text { rad }}-R_{E_{e}}^{e, \text { out }}\right) d E_{e} \\
&=0,
\end{aligned}
$$

$$
\begin{aligned}
\frac{d N_{h}}{d t} &=w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{h}\right) \frac{d}{d t} n_{E_{h}}^{h} d E_{h} \\
&=w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left(R_{E_{h}}^{h, \text { sun }}-R_{E_{h}}^{h, \text { rad }}-R_{E_{h}}^{h, \text { out }}\right) d E_{h} \\
&=0,
\end{aligned}
$$

in the steady state, where we use a fact that the intraband phonon scattering conserves the number of carriers in the band, i.e., $\int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) R_{E_{e}}^{e, \text { phonon }} d E_{e}=$ $\int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) R_{E_{h}}^{h, \text { phonon }} d E_{h}=0$. Since the terms, $R_{E_{e}}^{e, \text { sun }}, R_{E_{e}}^{e, \text { rad }}$, and $R_{E_{e}}^{e, \text { out }}$ represent the rates for generation, radiative recombination loss, and carrier extraction, respectively, the charge current density $I$ delivered to the electrodes (per unit area) is given by

$$
\begin{aligned}
I &=q w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) R_{E_{e}}^{e, \text { out }} d E_{e}, \\
&=q w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(R_{E_{e}}^{e, \text { sun }}-R_{E_{e}}^{e, \text { rad }}\right) d E_{e}, \\
&=q w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) R_{E_{h}}^{h, \text { out }} d E_{h}, \\
&=q w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left(R_{E_{h}}^{h, \text { sun }}-R_{E_{h}}^{h, \text { rad }}\right) d E_{h}.
\end{aligned}
$$

Here, we divided $I(\equiv I_{\text {out }}=I_{\text {sun }}-I_{\text {rad }})$ into each contributions defined by

$$
\begin{aligned}
I_{\text {out }} & \equiv q w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) R_{E_{e}}^{e, \text { out }} d E_{e}, \\
& =\frac{q w}{\tau_{\text {out }}} \int_{E_{b}}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left[n_{E_{e}}^{e}-f_{T_{c}}^{F}\left(E_{g}+E_{e}-\mu_{c}\right)\right] d E_{e},
\end{aligned}
$$

$$
\begin{aligned}
I_{\text {sun }} & \equiv q w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) R_{E_{e}}^{e, \text { sun }} d E_{e}, \\
& =q × \mathcal{C} \mathcal{R} \frac{c}{4 \pi^{2}} \frac{1}{(\hbar c)^{3}}\left(\frac{R_{S}}{L_{\mathrm{ES}}}\right)^{2} \int_{E_{g}}^{\infty} E^{2} f_{T_{\text {sun }}}^{B}(E) d E,
\end{aligned}
$$

$$
\begin{aligned}
I_{\mathrm{rad}} & \equiv q w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) R_{E_{e}}^{e, \mathrm{rad}} d E_{e}, \\
& =q × \frac{c}{2 \pi^{2}} \frac{1}{(\hbar c)^{3}} \int_{E_{g}}^{\infty} E^{2}\left\langle n^{e} n^{h}\right\rangle_{E-E_{g}} d E,
\end{aligned}
$$

where we neglected the band-filling effect $(n_{E_{e(h)}}^{e(h)} \ll 1)$ to obtain the last expression for $I_{\text {rad }}$ with

$$
\begin{aligned}
&\left\langle n^{e} n^{h}\right\rangle_{E-E_{g}} \\
& \equiv \frac{\int_{0}^{E-E_{g}} \mathcal{D}_{e}\left(E^{\prime}\right) \mathcal{D}_{h}\left(E-E_{g}-E^{\prime}\right) n_{E^{\prime}}^{e} n_{E-E_{g}-E^{\prime}}^{h} d E^{\prime}}{\int_{0}^{E-E_{g}} \mathcal{D}_{e}\left(E^{\prime}\right) \mathcal{D}_{h}\left(E-E_{g}-E^{\prime}\right) d E^{\prime}} .
\end{aligned}
$$

Further, we also divide the net current into extraction and injection terms, $I_{\text {out }}=I_{\text {out }}^{A \rightarrow C}-I_{\text {out }}^{C \rightarrow A}$ where

$$
I_{\text {out }}^{A \rightarrow C} \equiv \frac{q w}{\tau_{\text {out }}} \int_{E_{b}}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) n_{E_{e}}^{e} d E_{e},
$$

$$
I_{\text {out }}^{C \rightarrow A} \equiv \frac{q w}{\tau_{\text {out }}} \int_{E_{b}}^{\infty} \mathcal{D}_{e}\left(E_{e}\right) f_{T_{c}}^{F}\left(E_{g}+E_{e}-\mu_{c}\right) d E_{e}.
$$

Energy currents for all dissipation channels can be obtained in a similar manner by considering the total energy produced in the absorber per unit time and per unit area via electrons and holes,

$$
\begin{aligned}
\frac{d\left\langle H_{e}\right\rangle}{d t}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}\right)\left(R_{E_{e}}^{e, \text { sun }}-R_{E_{e}}^{e, \text { rad }}\right. \\
& \left.-R_{E_{e}}^{e, \text { out }}-R_{E_{e}}^{e, \text { phonon }}\right) d E_{e}=0,
\end{aligned}
$$

$$
\begin{aligned}
\frac{d\left\langle H_{h}\right\rangle}{d t}= & w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) E_{h}\left(R_{E_{h}}^{h, \text { sun }}-R_{E_{h}}^{h, \text { rad }}\right. \\
& \left.-R_{E_{h}}^{h, \text { out }}-R_{E_{h}}^{h, \text { phonon }}\right) d E_{h}=0,
\end{aligned}
$$

which are balanced in the steady state ($H_e$ and $H_h$ are the Hamiltonians for electrons and holes in the absorber). A part of solar energy $(\equiv P_{\text {sun }})$ absorbed in the absorber (per unit time per unit area) is

$$
\begin{aligned}
P_{\text {sun }}-P_{T}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}\right) R_{E_{e}}^{e, \text { sun }} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) E_{h} R_{E_{h}}^{h, \text { sun }} d E_{h} \\
= & \frac{\mathcal{C} \mathcal{R}}{4 \pi^{2}} \frac{c}{(\hbar c)^{3}}\left(\frac{R_{S}}{L_{\mathrm{ES}}}\right)^{2} \int_{E_{g}}^{\infty} E^{3} f_{T_{\text {sun }}}^{B}(E) d E,
\end{aligned}
$$


where $P_T$ is the transmitted fraction given by
$$
P_{T}=\frac{\mathcal{C} \mathcal{R}}{4 \pi^{2}} \frac{c}{(\hbar c)^{3}}\left(\frac{R_{S}}{L_{\mathrm{ES}}}\right)^{2} \int_{0}^{E_{g}} E^{3} f_{\text {sun }}^{B}(E) d E. \quad(28)
$$

The energy loss by radiative recombination (per unit time per unit area) is given by
$$
\begin{aligned}
P_{\mathrm{rad}}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}\right) R_{E_{e}}^{e, \mathrm{rad}} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) E_{h} R_{E_{h}}^{h, \mathrm{rad}} d E_{h} \\
= & \frac{c}{2 \pi^{2}} \frac{1}{(\hbar c)^{3}} \int_{E_{g}}^{\infty} E^{3}\left\langle n^{e} n^{h}\right\rangle_{E-E_{g}} d E.
\end{aligned}\quad(29)
$$

The net energy delivered to the electrodes (per unit time per unit area) is
$$
\begin{aligned}
P_{\text {out }}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}\right) R_{E_{e}}^{e, \text { out }} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right) E_{h} R_{E_{h}}^{h, \text { out }} d E_{h}.
\end{aligned}\quad(30)
$$

Since a part of $P_{\text {out }}$ is the power output by the solar cell,
$$
\begin{aligned}
P_{\text {work }}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(\mu_{c}\right) R_{E_{e}}^{e, \text { out }} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left(-\mu_{v}\right) R_{E_{h}}^{h, \text { out }} d E_{h} \\
= & \frac{\mu_{c}-\mu_{v}}{q} I_{\text {out }}=V I_{\text {out }},
\end{aligned}\quad(31)
$$
the rest represents the heat current delivered to the electrodes (per unit time per unit area):
$$
P_{Q_{\text {out }}} \equiv P_{\text {out }}-P_{\text {work }}, \quad(32)
$$

$$
\begin{aligned}
= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}-\mu_{c}\right) R_{E_{e}}^{e, \text { out }} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left[E_{h}-\left(-\mu_{v}\right)\right] R_{E_{h}}^{h, \text { out }} d E_{h}.
\end{aligned}\quad(33)
$$

$P_{Q_{\text {out }}}$ is further divided into two, which are exhausted in the electron and hole contacts: $P_{Q_{\text {out }}}=P_{Q_{\text {out }}}^{(e)}+P_{Q_{\text {out }}}^{(h)}$, where
$$
P_{Q_{\text {out }}}^{(e)}=w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}-\mu_{c}\right) R_{E_{e}}^{e, \text { out }} d E_{e}, \quad(34)
$$

$$
P_{Q_{\text {out }}}^{(h)}=w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left[E_{h}-\left(-\mu_{v}\right)\right] R_{E_{h}}^{h, \text { out }} d E_{h}. \quad(35)
$$

Heat current delivered into the absorber (per unit time per unit area) is
$$
\begin{aligned}
P_{Q_{\text {in }}}= & w \int_{0}^{\infty} \mathcal{D}_{e}\left(E_{e}\right)\left(E_{g}+E_{e}\right) R_{E_{e}}^{e, \text { phonon }} d E_{e} \\
& +w \int_{0}^{\infty} \mathcal{D}_{h}\left(E_{h}\right)\left(E_{h}\right) R_{E_{h}}^{h, \text { phonon }} d E_{h}.
\end{aligned}\quad(36)
$$

Alternatively, it can be evaluated by using the conservation law of total energy current,
$$
P_{Q_{\text {in }}}=P_{\text {sun }}-P_{T}-P_{\text {rad }}-P_{\text {out }}, \quad(37)
$$
where $P_{\text {out }}=P_{\text {work }}+P_{Q_{\text {out }}}$ from Eq. (32).

### C. Local equilibrium approximation

In this Paper, we assume that the carriers in the absorber are fully relaxed to be in thermal equilibrium with the lattice at the temperature $T_{\mathrm{ph}}$. This approximation is valid when time scales for all other dynamics (i.e., generation, radiation, and extraction in our model) are much slower than the thermalization time [13], whose time scale, $\tau_{\mathrm{ph}}$ given in Eq. (15), is typically of the order of pico or sub-picosecond [13–17]. The carrier-extraction time $\tau_{\text {out }}$ is a time scale, which the photogenerated carriers spend inside the absorber until they are extracted to the contacts. It cannot be less than a minimal time required for carriers traveling inside the absorber to reach the contact, $\tau_{\mathrm{dev}}^{c}$, which is roughly estimated as $10^{-9} \mathrm{~s}$ for an absorber with $100 \mu \mathrm{m}$ thickness (given the maximal velocity of carriers is approximately equal to $10^{5} \mathrm{~m} / \mathrm{s}$ ). Therefore, in the whole range of realistic parameter, $\tau_{\text {out }}$ is at least 3 orders larger than $\tau_{\mathrm{ph}}$, and the local equilibrium approximation should be valid.

Within the approximation, the distribution function of electrons and holes in the absorber is given by
$$
\begin{array}{r}
n_{E_{e}}^{e} \approx f_{T_{\mathrm{ph}}}^{F}\left(E_{g}+E_{e}-\mu_{c}^{\text {cell }}\right) \approx e^{-\left(E_{g}+E_{e}-\mu_{c}^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)}, \\
(38)
\end{array}
$$

$$
n_{E_{h}}^{h} \approx f_{T_{\mathrm{ph}}}^{F}\left[E_{h}-\left(-\mu_{v}^{\text {cell }}\right)\right] \approx e^{-\left(E_{h}+\mu_{v}^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)}, \quad(39)
$$
with yet unknown chemical potentials, $\mu_{c}^{\text {cell }}$ and $-\mu_{v}^{\text {cell }}$. By using Eqs. (38) and (39), we find $\left\langle n^{e} n^{h}\right\rangle_{E-E_{g}}$ in Eq. (22) is given by
$$
\left\langle n^{e} n^{h}\right\rangle_{E-E_{g}} \approx e^{-\left(E-q V^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)}, \quad(40)
$$
with $q V^{\text {cell }} \equiv \mu_{c}^{\text {cell }}-\mu_{v}^{\text {cell }}$, which yields an approximation for the radiative current loss in Eq. (21),
$$
\begin{aligned}
& I_{\mathrm{rad}}\left(T_{\mathrm{ph}}, V^{\text {cell }}\right) \\
& \quad \approx q \frac{c}{2 \pi^{2}} \frac{1}{(\hbar c)^{3}} \int_{E_{g}}^{\infty} E^{2} e^{-\left(E-q V^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)} d E.
\end{aligned}\quad(41)
$$
064001-5

In the same way, the energy loss due to the radiative recombination in Eq. (29) is given by
$$
\begin{aligned}
& P_{\mathrm{rad}}\left(T_{\mathrm{ph}}, V^{\text {cell }}\right) \\
& \quad \approx \frac{c}{2 \pi^{2}} \frac{1}{(\hbar c)^{3}} \int_{E_{g}}^{\infty} E^{3} e^{-\left(E-q V^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)} d E.
\end{aligned} \quad(42)
$$

Eqs. (41) and (42) are consistent with the generalized Planck radiation law for the charge current and energy current in the case of a perfect absorber with the temperature $T_{\mathrm{ph}}$ and Fermi-level separation $q V^{\text {cell }}$ [21].

The charge and energy current delivered to the electrodes are obtained similarly. Assuming the charge neutrality in the absorber for simplicity, which sets $\mu_{c(v)}^{c, \text { cell }}=$ $\left[E_{g}+k_{B} T_{\mathrm{ph}} \ln \left(d_{h} / d_{e}\right) \pm q V^{\text {cell }}\right] / 2$ and $\mu_{c(v)}=\left[E_{g}+k_{B} T_{c}\right.$ $\left.\ln \left(d_{h} / d_{e}\right) \pm q V\right] / 2$, we finally obtain
$$
\begin{aligned}
I_{\text {out }} \approx & \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left[\left(k_{B} T_{\mathrm{ph}}\right)^{3 / 2} e^{-\left[\left(E_{g}-q V^{\text {cell }}\right) / 2 k_{B} T_{\mathrm{ph}}\right]}\right. \\
& \times F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{\mathrm{ph}}}\right)-\left(k_{B} T_{c}\right)^{3 / 2} e^{-\left[\left(E_{g}-q V\right) / 2 k_{B} T_{c}\right]} \\
& \left.\times F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{c}}\right)\right],
\end{aligned}
$$

$$
\begin{aligned}
I_{\text {out }}^{A \rightarrow C} \approx & \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left(k_{B} T_{\mathrm{ph}}\right)^{3 / 2} e^{-\left[\left(E_{g}-q V^{\text {cell }}\right) / 2 k_{B} T_{\mathrm{ph}}\right]} \\
& \times F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{\mathrm{ph}}}\right),
\end{aligned}
$$

$$
I_{\text {out }}^{C \rightarrow A} \approx \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left(k_{B} T_{c}\right)^{3 / 2} e^{-\left[\left(E_{g}-q V\right) / 2 k_{B} T_{c}\right]} F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{c}}\right),
$$

$$
\begin{aligned}
P_{\text {out }} \approx & \frac{E_{g}}{q} I_{\text {out }}+\frac{2 w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left[\left(k_{B} T_{\mathrm{ph}}\right)^{5 / 2} e^{-\left[\left(E_{g}-q V^{\text {cell }}\right) / 2 k_{B} T_{\mathrm{ph}}\right]}\right. \\
& \times F_{3 / 2}\left(\frac{E_{b}}{k_{B} T_{\mathrm{ph}}}\right)-\left(k_{B} T_{c}\right)^{5 / 2} e^{-\left[\left(E_{g}-q V\right) / 2 k_{B} T_{c}\right]} \\
& \left.\times F_{3 / 2}\left(\frac{E_{b}}{k_{B} T_{c}}\right)\right],
\end{aligned}
$$

where $F_{\lambda}(x) \equiv \int_{\max (x, 0)}^{\infty} z^{\lambda} e^{-z} d z$. We also find the approximate expressions for $P_{Q_{\text {out }}}\left(\equiv P_{\text {out }}-V I_{\text {out }}\right)$ and $P_{Q_{\text {in }}}$ by using the above results and Eq. (37).

## IV. DEVICE SIMULATION

Device simulation is performed for an ideal HERC solar cell with a 100-$\mu$m-thick Si absorber under solar irradiation at 1-sun AM0 condition, whereas the solar spectrum is approximated by the 6000-K blackbody radiation. Under the condition, the SQ limit $(\equiv \eta_{\mathrm{SQ}})$ is $29.5 \%$ in a conventional planer solar cell at $T_{\mathrm{ph}}=T_{c}=300 \mathrm{~K}$.

The current-voltage $(I-V)$ characteristics of an ideal HERC solar cell, are obtained by solving simultaneously,
$$
I=I_{\text {out }}\left(T_{\mathrm{ph}}, V^{\text {cell }}, T_{c}, V\right),\quad (47)
$$

$$
I=I_{\text {sun }}-I_{\text {rad }}\left(T_{\mathrm{ph}}, V^{\text {cell }}\right),\quad (48)
$$

with $I_{\text {out }}\left(T_{\mathrm{ph}}, V^{\text {cell }}, T_{c}, V\right)$ given in Eq. (43) and $I_{\text {rad }}\left(T_{\mathrm{ph}}\right.$, $V^{\text {cell }}$ ) given in Eq. (41). Equations (47) and (48) relate the Fermi-level separation in the absorber, $V^{\text {cell }}\left[\equiv\left(\mu_{c}^{\text {cell }}-\right.\right.$ $\left.\left.\mu_{v}^{\text {cell }}\right) / q\right]$, with the output voltage, $V\left[\equiv\left(\mu_{c}-\mu_{v}\right) / q\right]$.

The $I$-$V$ curves are shown in Fig. 2 for different values of $E_{b}$ with $T_{\mathrm{ph}}=450 \mathrm{~K}$ and $\tau_{\text {out }}=10^{-9} \mathrm{~s}$. At first we check the validity of the local equilibrium approximation. As shown in Fig. 2, we compared $I$-$V$ curves obtained by the local equilibrium approximation (solid lines) and the full solution to the rate equations [Eqs. (1) and (2)] in the nonequilibrium theory (filled circles), where the carrier-thermalization times for electrons and holes are assumed to range between pico and subpicoseconds by setting the deformation potentials, $a_{\mathrm{def}, c}=a_{\mathrm{def}, v}=10 \mathrm{eV}$ in $R_{E_{e(h)}}^{e(h), \text { phonon }}$ in Eq. (10). For $\tau_{\text {out }}=10^{-9} \mathrm{~s}$, the results obtained by both theories agree well (Fig. 2) for all ranges of the parameters input. We further confirm that the local equilibrium approximation becomes more accurate for the larger extraction time (not shown).

For $E_{b}<0.6$, the open-circuit voltage $V_{\mathrm{OC}}$ increases with $E_{b}$ while the short-circuit current $I_{\mathrm{SC}}$ does not

![](./images/812706234976174081_3.jpg)

FIG. 2. $I$-$V$ curves for different values of the barrier height $E_{b}(=0,0.2,0.4,0.6,0.7 \mathrm{eV})$, obtained by the local equilibrium approximation (solid curves) and the full solution of the rate equations [Eqs. (1) and (2)] in the nonequilibrium theory (filled circles), for $\tau_{\text {out }}=10^{-9} \mathrm{~s}$. Simulations are performed for 100$\mu$m Si under irradiation of 6000-K blackbody spectrum (AM0) at 1-sun condition with $T_{c}=300 \mathrm{~K}$.

![](./images/812706234976174081_4.jpg)

FIG. 3. (a) Two-dimensional contour plot of the power conversion efficiency in $(E_b, V)$ plane are shown for $(\tau_{\text{out}}, T_{\text{ph}}) = (10^{-9}\ \text{s}, 450\ \text{K})$. Unstable parameter regions where the heat supply is depleted, $P_{Q_{\text{in}}} + P_T < 0$ and $P_{Q_{\text{in}}} < 0$, are superposed in the figure. (b) Max power conversion efficiency $\eta_{\text{max}}$ is plotted as a function of $\tau_{\text{out}}$ for $T_{\text{ph}} = 450\ \text{K}$ with and without an IR absorber (red squares and blue triangles, respectively), and for $T_{\text{ph}} = 300\ \text{K}$ (black circles). Simulations were performed for $100\ \mu\text{m}$ Si under irradiation of 6000 K blackbody spectrum (AM0) at 1 sun condition with $T_c = 300\ \text{K}$.

decrease significantly. On the other hand for $E_b \geq 0.6$, $I_{\text{SC}}$ significantly decreases with $E_b$ while $V_{\text{OC}}$ continuously increases (the critical value $E_b^c$ of $E_b$, above which $I_{\text{SC}}$ decreases, depends on $\tau_{\text{out}}$, $T_{\text{ph}}$, $I_{\text{sun}}$, and $w$; see Appendix A). From the results, the output power $I \times V$ seems to be maximized for $0.4\ \text{eV} < E_b < 0.7\ \text{eV}$. Correspondingly, as shown in Fig. 3(a), the contour plot of the power conversion efficiency $\eta (\equiv I \times V/P_{\text{sun}} \times 100)$ has a maximum, $43.0\%$ at $E_b \sim 0.55\ \text{eV}$.

As mentioned above, HERC solar cell utilizes a nonequilbirium condition, $T_{\text{ph}} > T_c$, which must be maintained in the operating device. For the stability of the operation, positive heat current into the absorber's crystal must be present in the steady state. Condition for the stability can be taken into account in the simulation, since the heat-current density per unit area, $P_{Q_{\text{in}}}$, is already given in the previous section. If the device has an IR absorber as shown in Fig. 1(a), the transmitted sub-band-gap photons can be absorbed at the rear side. It supplies heat current into the absorber, which maximally amounts to the whole transmitted energy current $P_T(> 0)$. In this way, $P_{Q_{\text{in}}} + P_T > 0$ is required to realize condition (ii) in HERC solar cell with an IR absorber. Without an IR absorber on the rear side [as being different from Fig. 1(a)], the requirement becomes higher, $P_{Q_{\text{in}}} > 0$. These are the minimum requirements for the stable operation at $T_{\text{ph}} > T_c$ no matter how much the heat leak is reduced.

The red shaded area surrounded by the dashed line in Fig. 3(a) shows a parameter regime with $P_{Q_{\text{in}}} + P_T < 0$, where the heat supply is insufficient and the HERC solar cell does not work steadily even with an IR absorber. Fortunately, the maximum point with $\eta = 43.0\%$ is outside this unstable regime. On the other hand, the maximum point belongs to an unstable regime without an IR absorber, i.e., where $P_{Q_{\text{in}}} < 0$ (in an area surrounded by the two blue curves). Therefore, HERC solar cell without an IR absorber has at most, $30.9\%$ efficiency at $E_b \sim 0.35\ \text{eV}$, outside the unstable regime. Parameter dependence of $P_{Q_{\text{in}}}$ is discussed in detail in Appendix B.

In Fig. 3(b), $\eta_{\text{max}}$ determined in this way are shown as a function of $\tau_{\text{out}}$ at $T_{\text{ph}} = 450\ \text{K}$ with and without an IR absorber, and at $T_{\text{ph}} = 300\ \text{K}$. At $T_{\text{ph}} = 450\ \text{K}$, $\eta_{\text{max}}$ increases logarithmically with decreasing $\tau_{\text{out}}$ for $\tau_{\text{out}} < 10^{-4}$ until it reaches the maximum where the curve has a kink, $\tau_{\text{out}} = \tau_{\text{out}}^{\text{kink}} [=10^{-7}\ \text{s}$ without an IR absorber, $10^{-10}\ \text{s}$ with an IR absorber (not shown)]. Appearance of the kinks shows that depletion of heat supply reduces $\eta_{\text{max}}$ for $\tau_{\text{out}} < \tau_{\text{out}}^{\text{kink}}$. To summarize the results at $T_{\text{ph}} = 450\ \text{K}$, $\eta_{\text{max}}\ (=43.0\%)$ is limited by $\tau_{\text{out}} \geq \tau_{\text{dev}}^c$ with an IR absorber, whereas it is limited by short heat supply having a maximum $(=38.9\%)$ at $\tau_{\text{out}} = \tau_{\text{out}}^{\text{kink}}$ without an IR absorber. In normal solar cell with $T_{\text{ph}} = T_c = 300\ \text{K}$, $\eta_{\text{max}}$ is limited by the detailed balance limit, $\eta_{\text{SQ}}\ (=29.5\%)$. For very slow extraction $[\tau_{\text{out}} > 10^{-3}\ \text{s}$ in Fig. 3(b) [13]], radiative recombination dominates the current loss and $\eta_{\text{max}}$ decreases strongly in all cases.

In Fig. 4, we show the limiting efficiency of HERC solar cells, which is obtained by optimizing $\eta_{\text{max}}$ for $V$, $E_b$, and $\tau_{\text{out}}(> \tau_{\text{dev}}^c)$, as a function of $T_{\text{ph}}$ (see Appendix C for details of the optimal parameters). For both with and without an IR absorber (upper two curves in Fig. 4), $\eta_{\text{max}}$ increases with $T_{\text{ph}}$ and largely exceeds the $\eta_{\text{SQ}}$. A departure between the two curves, found at $T_{\text{ph}} > 350\ \text{K}$, indicates that depletion of heat supply starts to play in a device without an IR absorber. The slope, roughly $1\%$ per $10\ \text{K}$ in the linear regime for both, is notably large, indicating the impact of heat recovery. This positive temperature dependence is a remarkable feature of HERC solar cell, which is opposite to a normal solar cell with $T_{\text{ph}} = T_c$ having a negative temperature characteristics, i.e., $\eta_{\text{max}}$ decreases with increasing $T_{\text{ph}}$ (the bottom dotted curve in Fig. 4). In a device without the energy filtering but with a temperature difference $T_{\text{ph}} > T_c$, $\eta_{\text{max}}$ does not decrease with the temperature (two dashed curves, middle in Fig. 4).


![](./images/812706234976174081_5.jpg)

FIG. 4. Theoretical limit on the conversion efficiency $\eta_{\text{max}}$ in HERC solar cells (solid curves) with (squares) and without (triangles) an IR absorber, plotted for $300\ \text{K} \leq T_{\text{ph}} \leq 450\ \text{K}$ and $T_{c} = 300\ \text{K}$. For comparison, we also show $\eta_{\text{max}}$ for HERC solar cells without energy filtering ($E_{b} = 0$, dashed) at $T_{\text{ph}} > T_{c}(= 300\ \text{K})$ with (open squares) and without (open triangles) an IR absorber, and $\eta_{\text{max}}$ for a normal solar cell with $T_{c} = T_{\text{ph}}$ (dotted).

How can these positive temperature characteristics of HERC solar cell be understood? Since it is obvious from Fig. 3(a) that the increase in $\eta_{\text{max}}$ mainly comes from the increase in $V_{\text{OC}}$, let us ask why $V_{\text{OC}}$ increases with $T_{\text{ph}}$ in HERC solar cell. We would like to note here that the $V_{\text{OC}}$-$E_{b}$ curve [thick black line in Fig. 3(a)] does not depend on $\tau_{\text{out}}$, since $\tau_{\text{out}}$ enters Eq. (47) only through a factor $1/\tau_{\text{out}}$ in $I_{\text{out}}$, and the open-circuit condition $I_{\text{out}} = 0$ is independent of $\tau_{\text{out}}(> 0)$. By expanding Eqs. (47) and (48) with respect to a small change $dT$ in the absorber's temperature ($T_{\text{ph}} = T + dT$ and $T_{c} = T$), $dV_{\text{OC}} \equiv V_{\text{OC}} - V_{\text{OC}}^{0}$ and $dV_{\text{OC}}^{\text{cell}} \equiv V_{\text{OC}}^{\text{cell}} - V_{\text{OC}}^{0}$ (deviations from the values at $T_{\text{ph}} = T_{c} = T = 300\ \text{K}$), we find

$$
0 = \frac{\partial I_{\text{out}}}{\partial V_{\text{OC}}^{\text{cell}}} \frac{dV_{\text{OC}}^{\text{cell}}}{dT} + \frac{\partial I_{\text{out}}}{\partial V_{\text{OC}}} \frac{dV_{\text{OC}}}{dT} + \frac{\partial I_{\text{out}}}{\partial T_{\text{ph}}}, \tag{49}
$$

$$
0 = \frac{\partial I_{\text{rad}}}{\partial V_{\text{OC}}^{\text{cell}}} \frac{dV_{\text{OC}}^{\text{cell}}}{dT} + \frac{\partial I_{\text{rad}}}{\partial T_{\text{ph}}}, \tag{50}
$$

where the partial derivatives of $I_{\text{out}}$ and $I_{\text{rad}}$ are evaluated under the open-circuit condition at $T_{\text{ph}} = T_{c} = T$. Note here that $V_{\text{OC}}$ and $V_{\text{OC}}^{\text{cell}}$ enter $I_{\text{out}}$ in Eq. (47) through the chemical potentials, $\mu_{c}$ and $\mu_{c}^{\text{cell}}$, in the Fermi-Dirac distribution. A straightforward calculation yields the following results:

$$
\frac{dV_{\text{OC}}^{\text{cell}}}{dT} = -\frac{E_{g} - qV_{\text{OC}}^{0}}{qT}, \tag{51}
$$

$$
\frac{d(V_{\text{OC}} - V_{\text{OC}}^{\text{cell}})}{dT} = \frac{E_{g} - qV_{\text{OC}}^{0} + 2E_{b}}{qT}, \tag{52}
$$

where small corrections of order $k_{B}/q$ are neglected in the right-hand side (see Appendix D for details). Summing up the two equations, we finally have

$$
\frac{dV_{\text{OC}}}{dT} = \frac{2E_{b}}{qT}. \tag{53}
$$

Equation (53) explains the results found in Fig. 4; a positive slope for HERC solar cell with energy filtering $E_{b} > 0$, and almost zero slope without the energy filtering $E_{b} = 0$. Moreover, Eq. (51) is a well-known expression for the negative temperature coefficient, due to the internal voltage drop, in normal solar cells (with $T_{\text{ph}} = T_{c} = T + dT$ and $V_{\text{OC}} = V_{\text{OC}}^{\text{cell}}$. See, e.g., Sec. 7.6 of Ref. [18]).

The positive temperature coefficient in Eq. (53), clearly originates from the difference in the output and internal voltages in Eq. (52). This term represents thermoelectric voltage produced at the energy-filtering layers, as shown below. Given that $E_{c}'$ and $E_{v}'$ are the conduction- and valence-band offsets of the energy-filtering layers, respectively, at electron- and hole-contact sides, Eq. (52) can be written as

$$
\frac{d(V_{\text{OC}} - V_{\text{OC}}^{\text{cell}})}{dT} = \frac{E_{c}' - \mu_{c}}{qT} + \frac{\mu_{v} - E_{v}'}{qT}. \tag{54}
$$

According to Mott's formula [22], the right-hand side in Eq. (54) is equal to a sum of the Seebeck coefficients for electrons and holes in the energy-filtering layers (agrees upto the leading order within the same approximation level). The thermoelectric effect is large enough to cancel and even exceed the negative effect of the internal voltage drop in Eq. (51) for $E_{b} > 0$. In Appendix E, the positive temperature coefficient in Eq. (53) is shown to be a general feature of HERC solar cells, which cannot be lost even when other temperature-dependent degradation factors are present (e.g., nonradiative recombinations and band-gap reduction).

Finally in Fig. 5, we plot $\eta_{\text{max}}$ of HERC solar cell with an absorber with different band gaps at different temperatures, $T_{\text{ph}} = 350, 400$, and $450\ \text{K}$. We find that the positive temperature dependence of $\eta_{\text{max}}$ is a general feature found for any absorber materials. For comparison, $\eta_{\text{max}}$ for hot-carrier solar cells is also shown for the same set of carrier temperatures, $T_{\text{carrier}} = 350, 400, 450\ \text{K}$ (dashed curves in Fig. 5) under the same illumination condition (1 sun, AM0). In spite of large differences in the mechanisms and in the range of the parameter ($\tau_{\text{out}} > \tau_{\text{ph}}$ or $\tau_{\text{out}} \ll \tau_{\text{ph}}$), the HERC solar cell and hot-carrier solar cell exhibit similar results for this temperature range. More surprisingly, HERC solar cell without fast-carrier extraction gives higher efficiency than hot-carrier solar cell with fast carrier extraction in some cases (e.g., in Si and CdTe at 450 K).

![](./images/812706234976174081_6.jpg)

FIG. 5. Theoretical limiting efficiency of HERC solar cell (with an IR absorber) with various absorber materials: Ge, CuInSe₂, Si, GaAs, and CdTe, respectively, with the thicknesses, 100, 2, 100, 2, 2 μm, the band gaps, 0.67, 1.04, 1.12, 1.42, 1.56 eV, the effective mass parameters (DOS value), $m_e^*/m_0 = 0.88, 0.09, 1.08, 0.067, 0.09$ for electrons, and $m_h^*/m_0 = 0.29, 0.73, 0.55, 0.47, 0.64$ for holes [18,23–25]. Simulations are performed for $T_{\text{ph}} = 350, 400, 450$ K and $T_c = 300$ K under 1 sun, AM0 condition with 6000-K blackbody spectrum. The SQ limit for normal solar cell [2] (solid curve), and max efficiencies of hot-carrier solar cells [7] with the same carrier temperatures, $T_{\text{carrier}} = 350, 400, 450$ K (dashed curves), are also shown for comparison. Calculation for a hot-carrier solar cell is performed based on the method presented in the original paper [7] with the same excitation condition.

## V. SIMULATION FOR A NONIDEAL DEVICE: EFFECTS OF THERMOELECTRIC PROPERTIES OF ENERGY-FILTERING LAYERS

In the preceding section, we show a device simulation for an ideal HERC solar cell where the increment in the conversion efficiency is found to originate from thermoelectricity produced by the temperature gradient in the energy-filtering layers (the Seebeck effect). In the ideal case, other factors, which could degrade the device performance, are completely neglected (as being similar to the studies for the conversion-efficiency limits of other types of solar cells including hot-carrier solar cells [2,7]). On the other hand, degradation factors, especially those inherent to the energy-filtering layers, need to be considered in a simulation for a real device. In this section, we present a simulation for a nonideal device by taking into account two factors related to the thermoelectric properties of the energy-filtering layers; one is finite electrical resistivity of the energy-filtering layers, $\rho(=1/\sigma>0)$, which causes an ohmic voltage drop ($\equiv dV_{\text{ohmic}}$), and another is finite thermal conductivity of the energy-filtering layers ($\equiv \kappa$), which is naively assumed small enough to provide a given temperature difference in the simulation for an ideal device.

Here, we consider a device shown in Fig. 6(a). The light acceptance surface of the absorber is $S_a$. The energy-filtering layers, having a cross-section area of $S_c$ and a length $L_c$, are made of semiconductors with a electrical resistivity $\rho$ (electrical conductivity $\sigma = 1/\rho$) and a thermal conductivity $\kappa$. As given in the previous section, semiconductor materials of the energy-filtering layers have the conduction- and valence-band offsets, $E_c'$ and $E_v'$, respectively, for the electron- and hole-contact sides. These offsets provide potential barriers of a height $E_b(>0)$ for carriers to be extracted to the electrodes.

![](./images/812706234976174081_7.jpg)

FIG. 6. Nonideal device simulation: (a) a schematic drawing of the device (with an IR absorber, electrodes are omitted in the figure for simplicity). (b) Maximum efficiency of HERC solar cell (with an IR absorber) plotted as a function of $T_{\text{ph}}$ for different values for thermoelectric parameters of the energy filtering layers, $\kappa/\sigma = 0, 10^{\boldsymbol{\cdot}-4.5}, 10^{\boldsymbol{\cdot}-4.0}, 10^{\boldsymbol{\cdot}-3.5}, 10^{\boldsymbol{\cdot}-3.0}, 10^{\boldsymbol{\cdot}-2.7}$, and $10^{\boldsymbol{\cdot}-2.5}$ V²/K. Simulations are performed based on the nonideal device model with a 100-μm Si absorber, illumination of 1 sun of 6000-K blackbody spectrum (AM0), and $T_c = 300$ K.

In this model, the voltage drop is given by

$$
d V_{\text{ohmic}}=2 ×\left(I S_{a}\right) ×\left(\rho \frac{L_{c}}{S_{c}}\right)=2 × I × \frac{l_{\text{eff}}}{\sigma}, \quad (55)
$$

where an effective length $l_{\text{eff}}$ of an energy-filtering layer is defined by $l_{\text{eff}} \equiv L_c S_a/S_c$. The factor 2 in Eq. (55) accounts for the voltage drop both at the electron- and hole-contact sides. An inclusion of the ohmic loss at the energy-filtering layers replaces $V$ with $V + dV_{\text{ohmic}}$ in Eq. (47), i.e.,

$$
I=I_{\text{out}}(T_{\text{ph}}, V^{\text{cell}}, T_{c}, V+d V_{\text{ohmic}}). \quad (56)
$$


Heat-current density flowing into an energy-filtering layer is
$$
j_{Q}=\left[P_{\text {sun }}-P_{\mathrm{rad}}\left(T_{\mathrm{ph}}, V^{\text {cell }}\right)-V^{\text {cell }} I\right] \frac{S_{a}}{2 S_{c}},\qquad(57)
$$
for a device with an IR absorber in Fig. 6(a). Using the expression, the temperature difference $T_{\mathrm{ph}}-T_{c}(=j_{Q} L_{c} / \kappa)$ is given by
$$
T_{\mathrm{ph}}-T_{c}=\frac{l_{\mathrm{eff}}}{2 \kappa}\left[P_{\mathrm{sun}}-P_{\mathrm{rad}}\left(T_{\mathrm{ph}}, V^{\mathrm{cell}}\right)-V^{\mathrm{cell}} I\right].\qquad(58)
$$

By solving simultaneously Eqs. (48), (56), and (58), $I$, $V^{\text{cell}}$, and $T_{\text{ph}}$ are given as a function of $V$ and $l_{\text{eff}}$ or, alternatively, $I$, $V^{\text{cell}}$, and $l_{\text{eff}}$ are given as a function of $V$ and $T_{\text{ph}}$.

The maximum efficiency $\eta_{\text{max}}$, determined in the same manner as presented in the previous section (i.e., the stability condition $P_{Q_{\text{in}}}+P_{T}>0$ is also considered), is shown in Fig. 6(b). In the figure, $\eta_{\text{max}}$ is plotted as a function of $T_{\text{ph}}$ for different values of $\kappa/\sigma$ (the same results are obtained for different sets of $\kappa$ and $\sigma$ with a given $\kappa/\sigma$). As expected, the efficiency decreases with increasing $\kappa$ and $\rho(=1/\sigma)$. The slope of the curves decreases with increasing $\kappa/\sigma$, and the sign of the slope changes at $\kappa/\sigma \sim 10^{-3.0}$ V$^{2}$/K from positive ($\kappa/\sigma < 10^{-3.0}$) to negative ($\kappa/\sigma > 10^{-3.0}$). Similar results to the ideal limit at $\kappa/\sigma=0$ (the dashed curve, same as a red curve in Fig. 4) can be found for $\kappa/\sigma < 10^{-4.0}$ V$^{2}$/K.

The numerical results can be explained as follows. Recalling that the temperature difference $dT(\equiv T_{\text{ph}}-T_{c})$ and the voltage drop $dV_{\text{ohmic}}$ are both linear in $l_{\text{eff}}$ [Eqs. (55) and (58)], we expand Eqs. (48) and (56) to the first order in $l_{\text{eff}}$ and obtain
$$
\begin{aligned}
\frac{d V}{d T} & =\frac{d V^{\text {cell }}}{d T}+\frac{d V-d V^{\text {cell }}}{d T}, \\
& \approx-\frac{E_{g}-q V^{\text {cell }}}{q T}+\frac{E_{g}+2 E_{b}-q V^{\text {cell }}}{q T}-\frac{d V_{\text {ohmic }}}{d T}, \\
& =\frac{2 E_{b}}{q T}-\frac{4 \kappa}{\sigma} \times \frac{I}{P_{\text {sun }}-P_{\text {rad }}\left(T_{\text {ph }}, V^{\text {cell }}\right)-V^{\text {cell }} I},
\end{aligned}\qquad(59)
$$
where we assume $T_{\text{ph}}=T_{c}=T$ and $V^{\text{cell}}=V$ at $l_{\text{eff}}=0$. We use Eqs. (55) and (58) for $dV_{\text{ohmic}}$ and $dT$ to obtain the final expression. The first and second terms in the right-hand side of the second equation correspond to an internal voltage drop in the absorber and a sum of the Seebeck coefficients of the energy-filtering layers [see Eq. (54)], respectively. Therefore, it is necessary for achieving positive temperature characteristics, $dV/dT>0$, that a thermoelectric gain of the voltage exceeds a sum of the voltage loss in the absorber and the ohmic loss in the filtering layers (in the presence of the photogenerated current $I \sim I_{\text{sun}}$).

From Eq. (59), the requirement for $dV/dT>0$, is roughly estimated as
$$
\frac{\kappa}{\sigma}<\frac{E_{b}}{q} × 3.0 × 10^{-3} \quad\left(\mathrm{V}^{2} / \mathrm{K}\right),\qquad(60)
$$
where we have inserted parameters obtained at the max power condition for $T_{\text{ph}}=T_{c}=300$ K ($I \approx I_{\text{sun}}$, $V^{\text{cell}}I \approx 0.3P_{\text{sun}}$, $P_{\text{rad}} \approx 0$) and $P_{\text{sun}}/I_{\text{sun}}=2.55$ V for a Si absorber ($E_{g}=1.12$ eV). Using the optimal barrier heights found in the ideal case ($\kappa/\sigma=0$), $E_{b}=0.39$, 0.47, and 0.55 eV at $T_{\text{ph}}=350$, 400, and 450 K, the upper bound in the condition, Eq. (60), is estimated to be $1.2 × 10^{-3}$, $1.4 × 10^{-3}$, and $1.6 × 10^{-3}$ V$^{2}$/K, respectively. This estimation reasonably explains the numerical result shown in Fig. 6(b). HERC solar cell based on a Si absorber can have a positive temperature characteristics if the energy-filtering layers are made of semiconductors with high electric conductivity and low thermal conductivity, which satisfies $\kappa/\sigma < 10^{-3.0}$ V$^{2}$/K. Moreover, the ideal limit of the efficiency is obtained for $\kappa/\sigma \ll 10^{-3.0}$ V$^{2}$/K, where the ohmic loss can be negligible.

Finally in this section, we discuss the feasibility of the condition. The most known thermoelectric material, $\text{Bi}_{2}\text{Te}_{3}$, has high electric conductivity $\sigma \approx 10^{5}$ S/m and low thermal conductivity of $\kappa \approx 1.4$ W/mK [26]. This gives a value, $\kappa/\sigma \approx 1.4 × 10^{-5.0}$ V$^{2}$/K, by which the ideal limit could be reached. However, $\text{Bi}_{2}\text{Te}_{3}$ is a narrow-gap semiconductor with a band gap approximately equal to 0.14 eV, and therefore cannot be used as the energy-filtering layers of HERC solar cell. A variety of perovskite materials, including organic-inorganic hybrids, are reported to have low thermal conductivity less than 1 W/mK and the band offsets can be varied with the atomic composition [27,28]. Organic-inorganic hybrid perovskites, however, seem to have lower electric conductivities than those of all-inorganic perovskites. Recent experiments showed that an all-inorganic material, $\text{CsSnI}_{3}$ [28], could satisfy all the requirements: its band gap 1.3 eV larger than that of Si, low thermal conductivity $\kappa=0.6$ W/mK, and high electric conductivity $\sigma=3 × 10^{4}$ S/m at room temperature, yielding $\kappa/\sigma \approx 2.0 × 10^{-5.0}$ V$^{2}$/K. At this point, we should notice that these parameters will be altered when the materials are used in a HERC solar cell under operation where the photogenerated electrons and holes are separated in the absorber and continuously injected to the energy-filtering layers. Therefore, the thermoelectric parameters should be discussed in a case under photodoping of the majority carriers, and hence the electrical conductivity will be improved. Introducing a phononic nanostructure [29,30] to these materials may also help reduce the thermal conductivity. Further experimental studies will be necessary to determine materials appropriate for the energy-filtering layers.

064001-10

## VI. CONCLUSIONS

We present a concept of HERC solar cell, and show that there is room to improve the conversion efficiency of Si solar cells beyond the SQ limit. The positive temperature characteristics originate from the thermoelectric effect produced at the energy-filtering layers. Storing the heat effectively inside the absorber to have large $T_{\mathrm{ph}} / T_{c}(>1)$ plays a crucial role (e.g., by using low-thermal-conductivity materials for the energy-filtering layers and by introducing phononic nanostructures [29,30]).

## ACKNOWLEDGMENTS

Authors acknowledge Tatsuro Yuge, Makoto Yamaguchi, Katsuhiko Shirasawa, Tetsuo Fukuda, Katsuhito Tanahashi, Tomihisa Tachibana, Takuya Matsui, and Yasuhiko Takeda for discussion. This work was supported by JSPS KAKENHI Grant No. JP19K04523.

## APPENDIX A: CRITICAL HEIGHT OF THE POTENTIAL BARRIER OF FILTERING LAYERS: $E_{b}^{c}$

As shown in the main text, the short-circuit current $I_{\mathrm{SC}}$ at $V=0$ is reduced for high potential barrier $E_{b}>E_{b}^{c}$. Here we give an analytic estimate of the critical height $E_{b}^{c}$.

In the following analysis, we assume $E_{b} \gg k_{B} T_{\mathrm{ph}}$ and $I=I_{\mathrm{out}}^{A \rightarrow C}-I_{\mathrm{out}}^{C \rightarrow A} \approx I_{\mathrm{out}}^{A \rightarrow C}$ with $I_{\mathrm{out}}^{A \rightarrow C} \gg I_{\mathrm{out}}^{C \rightarrow A}$ at $V=0$. Under the assumption, the equation for the short-circuit current is

$$
I_{\mathrm{SC}}=I_{\mathrm{sun}}-I_{\mathrm{rad}}=I_{\mathrm{out}}^{A \rightarrow C}. \tag{A1}
$$

From Eq. (41), the radiation loss is written as $I_{\mathrm{rad}}=A Y^{2}$ with $Y \equiv e^{q V^{\text {cell }} /\left(2 k_{B} T_{\mathrm{ph}}\right)}$ and

$$
\begin{aligned}
A & \equiv q \frac{c}{2 \pi^{2}} \frac{1}{(\hbar c)^{3}} \int_{E_{g}}^{\infty} E^{2} e^{-E /\left(k_{B} T_{\mathrm{ph}}\right)} d E=I_{\mathrm{rad}}\left(T_{\mathrm{ph}}, 0\right) \\
& \approx q \frac{c}{2 \pi^{2}} \frac{E_{g}^{2}}{(\hbar c)^{3}} \times e^{-E_{g} /\left(k_{B} T_{\mathrm{ph}}\right)}. \tag{A2}
\end{aligned}
$$

From Eq. (44), the extracted current is written as $I_{\mathrm{out}}^{A \rightarrow C}=B Y$ with

$$
\begin{aligned}
B & \equiv \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left(k_{B} T_{\mathrm{ph}}\right)^{3 / 2} e^{-\left(E_{g} / 2 k_{B} T_{\mathrm{ph}}\right)} F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{\mathrm{ph}}}\right), \\
& \approx \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left(k_{B} T_{\mathrm{ph}}\right) \sqrt{E_{b}} \times e^{-\left(E_{g}+2 E_{b}\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)}. \tag{A3}
\end{aligned}
$$

Using the expressions with $C \equiv I_{\text {sun }}$, the current equation gives a quadratic equation

$$
A Y^{2}+B Y-C=0, \tag{A4}
$$

which determines an unknown variable $V^{\text {cell }}$. Since $Y>0$ from the definition, the positive solution is found to be

$$
Y=\frac{\sqrt{B^{2}+4 A C}-B}{2 A}. \tag{A5}
$$

By inserting the result for $Y$, the short-circuit current is found to be

$$
I_{\mathrm{SC}}=I_{\mathrm{out}}=B Y=B \frac{\sqrt{B^{2}+4 A C}-B}{2 A}, \tag{A6}
$$

and the short-circuit current normalized by the photogenerated current is

$$
\begin{aligned}
\frac{I_{\mathrm{SC}}}{I_{\text {sun }}} & =\frac{\sqrt{1+4\left(A C / B^{2}\right)}-1}{2\left(A C / B^{2}\right)}=\frac{\sqrt{1+4 x^{2}}-1}{2 x^{2}} \\
& = \begin{cases}1 & (x \ll 1) \\
1 / x & (x \gg 1),\end{cases} \tag{A7}
\end{aligned}
$$

with $x \equiv \sqrt{A C / B^{2}}$. Therefore, the condition for the short-circuit current to be decreased strongly due to the high potential barrier is $x \equiv \sqrt{A C / B^{2}} \gg 1$. Since the condition can be written as $\sqrt{A C / B^{2}}=\sqrt{\left(C \times A Y^{2}\right) /(B Y)^{2}}=$ $\sqrt{I_{\text {sun }} I_{\text {rad }} /\left(I_{\text {out }}^{A \rightarrow C}\right)^{2}} \gg 1$, the critical height of the potential barrier $E_{b}^{c}$ can be determined at the crossover value $(x \approx 1)$ as given by

$$
\sqrt{I_{\mathrm{sun}} I_{\mathrm{rad}}}=I_{\mathrm{out}}^{A \rightarrow C}\left(E_{b}^{c}\right). \tag{A8}
$$

$E_{b}^{c}$ evaluated from this condition perfectly explains the numerical results [e.g., Eq. (A8) gives $E_{b}^{c}=0.658 \mathrm{eV}$ for Fig. 3(a) in the main text]. Using Eqs. (A2) and (A3) and introducing the normalized parameter $z_{c} \equiv E_{b}^{c} /\left(k_{B} T_{\mathrm{ph}}\right)$, the condition is explicitly given by

$$
z_{c}=a+\frac{1}{2} \ln z_{c}, \tag{A9}
$$

with a parameter

$$
\begin{aligned}
a= & \frac{1}{2} \ln \left[\frac{w^{2} d_{e} d_{h}\left(k_{B} T_{\mathrm{ph}}\right)^{3}\left(2 \pi^{2}\right)(\hbar c)^{3}}{\tau_{\text {out }}^{2} \times\left(I_{\text {sun }} / q\right) \times c E_{g}^{2}}\right] \\
= & \ln \frac{1}{\tau_{\text {out }}}+\frac{3}{2} \ln \left(k_{B} T_{\mathrm{ph}}\right)-\ln \frac{I_{\text {sun }}}{q}+\ln w \\
& +\frac{1}{2} \ln \left[\frac{2 \pi^{2}(\hbar c)^{3} d_{e} d_{h}}{c E_{g}^{2}}\right], \tag{A10}
\end{aligned}
$$

where $a$ should be much larger than unity to have $z_{c}=$ $E_{b}^{c} /\left(k_{B} T_{\mathrm{ph}}\right) \gg 1$. Equation (A9) can be solved for $a \gg 1$

by successive iterations as
$$
\begin{aligned}
z_{c} & =a+\frac{1}{2} \ln \left(z_{c}\right)=a+\frac{1}{2} \ln \left[a+\frac{1}{2} \ln \left(z_{c}\right)\right] \\
& =a+\frac{1}{2} \ln \left\{a+\frac{1}{2} \ln \left[a+\frac{1}{2} \ln \left(z_{c}\right)\right]\right\}=\cdots, \quad(\mathrm{A} 11)
\end{aligned}
$$
and the iteration stopped at the first level,
$$
z_{c}=a+\frac{1}{2} \ln a, \quad \text { (A12) }
$$
already shows a good agreement with the exact value in our simulation. In this way, the critical height of the potential barrier can be estimated by
$$
E_{b}^{c}=k_{B} T_{\mathrm{ph}} z_{c}=k_{B} T_{\mathrm{ph}} \times\left(a+\frac{1}{2} \ln a\right). \quad \text { (A13) }
$$

Since $z_{c}$ increases monotonically with $a$ for $a>1$, we can draw the following conclusions for the parameter dependency from Eqs. (A10) and (A13):

(a) $E_{b}^{c}$ increases as $\tau_{\text {out }}$ decreases;
(b) $E_{b}^{c}$ increases as $T_{\mathrm{ph}}$ increases [whereas the linear dependency dominates in Eq. (A13)];
(c) $E_{b}^{c}$ decreases as $I_{\text {sun }}$ (hence the concentration ratio $C R$ ) increases;
(d) $E_{b}^{c}$ decreases as $w$ decreases.

## APPENDIX B: PARAMETER DEPENDENCE OF THE HEAT CURRENT $P_{Q \text { in }}$

Here we show an analysis to find parameter dependence of the heat current, $P_{Q \text { in }}$. Using the conservation law for the total energy current, Eq. (37), the parameter dependence of $P_{Q \text { in }}\left[=P_{\text {sun }}-P_{T}-\left(P_{\text {rad }}+P_{\text {out }}\right)\right]$ comes from $P_{\text {rad }}+P_{\text {out }}$. From Eqs. (43)-(46), $P_{\text {out }}$ is given by
$$
\begin{aligned}
P_{\text {out }}= & \frac{E_{g}}{q} I_{\text {out }}+\frac{2 k_{B} T_{\text {ph }}}{q} \frac{F_{3 / 2}\left(\frac{E_{b}}{k_{B} T_{\text {ph }}}\right)}{F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{\text {ph }}}\right)} I_{\text {out }}^{A \rightarrow C} \\
& -\frac{2 k_{B} T_{c}}{q} \frac{F_{3 / 2}\left(\frac{E_{b}}{k_{B} T_{c}}\right)}{F_{1 / 2}\left(\frac{E_{b}}{k_{B} T_{c}}\right)} I_{\text {out }}^{C \rightarrow A}, \\
= & {\left[\frac{E_{g}}{q}+\frac{2 k_{B} T_{\text {ph }}}{q} G\left(\frac{E_{b}}{k_{B} T_{\text {ph }}}\right)\right] I_{\text {out }} } \\
& +\frac{2 k_{B}}{q}\left[T_{\text {ph }} G\left(\frac{E_{b}}{k_{B} T_{\text {ph }}}\right)-T_{c} G\left(\frac{E_{b}}{k_{B} T_{c}}\right)\right] I_{\text {out }}^{C \rightarrow A},
\end{aligned}
$$
where we introduce
$$
G(x) \equiv \frac{F_{3 / 2}(x)}{F_{1 / 2}(x)}= \begin{cases}3 / 2 & (x \ll 1) \\ x+1 & (x \gg 1)\end{cases}
$$
by which the asymptotic form of $P_{\text {out }}$ is found to be
$$
P_{\text {out }}= \begin{cases}\left(E_{g}+3 k_{B} T_{\mathrm{ph}}\right) \times\left(I_{\mathrm{out}} / q\right)+3 k_{B}\left(T_{\mathrm{ph}}-T_{c}\right) \times\left(I_{\mathrm{out}}^{C \rightarrow A} / q\right). & \left(\frac{E_{b}}{k_{B} T_{c}}, \frac{E_{b}}{k_{B} T_{\mathrm{ph}}} \ll 1\right) \\ \left(E_{g}+2 E_{b}+2 k_{B} T_{\mathrm{ph}}\right) \times\left(I_{\mathrm{out}} / q\right)+2 k_{B}\left(T_{\mathrm{ph}}-T_{c}\right) \times\left(I_{\mathrm{out}}^{C \rightarrow A} / q\right). & \left(\frac{E_{b}}{k_{B} T_{c}}, \frac{E_{b}}{k_{B} T_{\mathrm{ph}}} \gg 1\right).\end{cases}
$$

In a similar manner, from Eqs. (29) and (21), the radiation energy current $P_{\text {rad }}$ can be written as
$$
P_{\text {rad }} \approx\left(E_{g}+k_{B} T_{\text {ph }}\right) \times\left(I_{\text {rad }} / q\right). \quad \text { (B4) }
$$

For voltage fairly below the open-circuit voltage $\left(V<V_{\mathrm{OC}}\right)$, we have asymptotic forms of the currents: $I_{\text {out }} \rightarrow I_{\text {sun }}$ and $I_{\text {rad }} \rightarrow 0$ for $E_{b}<E_{b}^{c}$, and $I_{\text {out }} \rightarrow 0, I_{\text {out }}^{C \rightarrow A} \rightarrow 0$ and $I_{\text {rad }} \rightarrow I_{\text {sun }}$ for $E_{b}>E_{b}^{c}$. Therefore, we have
$$
P_{\text {rad }}+P_{\text {out }}= \begin{cases}\left(E_{g}+3 k_{B} T_{\text {ph }}\right) \times\left(I_{\text {sun }} / q\right)+3 k_{B}\left(T_{\text {ph }}-T_{c}\right) \times\left(I_{\text {out }}^{C \rightarrow A} / q\right), & \left(E_{b} \ll k_{B} T_{c}\right) \\ \left(E_{g}+2 E_{b}+2 k_{B} T_{\text {ph }}\right) \times\left(I_{\text {sun }} / q\right)+2 k_{B}\left(T_{\text {ph }}-T_{c}\right) \times\left(I_{\text {out }}^{C \rightarrow A} / q\right), & \left(k_{B} T_{\text {ph }} \ll E_{b}<E_{b}^{c}\right) \\ \left(E_{g}+k_{B} T_{\text {ph }}\right) \times\left(I_{\text {sun }} / q\right), & \left(E_{b}>E_{b}^{c}\right)\end{cases}
$$
by which the temperature dependence is given by
$$
\frac{d\left(P_{\mathrm{rad}}+P_{\mathrm{out}}\right)}{d T_{\mathrm{ph}}}=-\frac{d P_{Q \mathrm{in}}}{d T_{\mathrm{ph}}}= \begin{cases}3 k_{B}\left(I_{\mathrm{sun}} / q+I_{\mathrm{out}}^{C \rightarrow A} / q\right)>0, & \left(E_{b} \ll k_{B} T_{c}\right) \\ 2 k_{B}\left(I_{\mathrm{sun}} / q+I_{\mathrm{out}}^{C \rightarrow A} / q\right)>0, & \left(k_{B} T_{\mathrm{ph}} \ll E_{b}<E_{b}^{c}\right) \\ k_{B} I_{\mathrm{sun}} / q>0, & \left(E_{b}>E_{b}^{c}\right)\end{cases}
$$


and the $\tau_{\text{out}}$ dependency is given by

$$
\frac{d\left(P_{\mathrm{rad}}+P_{\text {out }}\right)}{d \tau_{\text {out }}}=-\frac{d P_{Q_{\text {in }}}}{d \tau_{\text {out }}}= \begin{cases}-\frac{1}{\tau_{\text {out }}} \times 3 k_{B}\left(T_{\mathrm{ph}}-T_{c}\right) I_{\text {out }}^{C \rightarrow A} / q<0. & \left(E_{b} \ll k_{B} T_{c}\right) \\ -\frac{1}{\tau_{\text {out }}} \times 2 k_{B} \tau_{\text {out }}\left(T_{\mathrm{ph}}-T_{c}\right) I_{\text {out }}^{C \rightarrow A} / q<0. & \left(k_{B} T_{\mathrm{ph}} \ll E_{b}<E_{b}^{c}\right) \\ 0. & \left(E_{b}>E_{b}^{c}\right).\end{cases}
\tag{B7}
$$

These results support the claim that $P_{Q_{\text {in }}}$ decreases monotonically with increasing $T_{\mathrm{ph}}$ and decreases with decreasing $\tau_{\text {out }}$.
As for the $E_{b}$ dependency, it is given by

$$
\frac{d\left(P_{\mathrm{rad}}+P_{\text {out }}\right)}{d E_{b}}=-\frac{d P_{Q_{\text {in }}}}{d E_{b}}= \begin{cases}0. & \left(E_{b} \ll k_{B} T_{c}\right) \\ \frac{2}{q}\left[I_{\mathrm{sun}}-\left(\frac{T_{\mathrm{ph}}}{T_{c}}-1\right) I_{\text {out }}^{C \rightarrow A}\right]. & \left(k_{B} T_{\mathrm{ph}} \ll E_{b}<E_{b}^{c}\right) \\ 0. & \left(E_{b}>E_{b}^{c}\right).\end{cases}
\tag{B8}
$$

Since $(T_{\mathrm{ph}}/T_{c}-1)I_{\text{out}}^{C\rightarrow A}\propto(T_{\mathrm{ph}}/T_{c}-1)\sqrt{E_{b}}e^{-E_{b}/(k_{B}T_{\mathrm{ph}})}e^{qV/(2k_{B}T_{\mathrm{ph}})}/\tau_{\text{out}}$ for $k_{B}T_{\mathrm{ph}}\ll E_{b}<E_{b}^{c}$, $d(P_{\mathrm{rad}}+P_{\text{out}})/dE_{b}$ can be negative when $(T_{\mathrm{ph}}/T_{c}-1)I_{\text{out}}^{C\rightarrow A}>I_{\text{sun}}$ for large $T_{\mathrm{ph}}$, large $V$, and small $\tau_{\text{out}}$. In such a case, we find a nonmonotonic dependence on $E_{b}$,

$$
\frac{d\left(P_{\mathrm{rad}}+P_{\text {out }}\right)}{d E_{b}}=-\frac{d P_{Q_{\text {in }}}}{d E_{b}} \approx \begin{cases}-\frac{2}{q}\left(\frac{T_{\mathrm{ph}}}{T_{c}}-1\right) I_{\text {out }}^{C \rightarrow A}<0, & \left(E_{b}<E_{b}^{*}\right) \\ \frac{2}{q} I_{\text {sun }}>0, & \left(E_{b}^{*}\right.<E_{b}<E_{b}^{c}) \\ \left(E_{g}+2 E_{b}^{*}+2 k_{B} T_{\mathrm{ph}}\right) / q \times\left(d I_{\mathrm{out}} / d E_{b}\right)<0, & \left(E_{b} \approx E_{b}^{c}\right) \\ 0, & \left(E_{b}>E_{b}^{c}\right)\end{cases}
\tag{B9}
$$

where the crossover value, $E_{b}=E_{b}^{*}$, is given by

$$
\begin{aligned}
I_{\text {sun }}= & \left(\frac{T_{\mathrm{ph}}}{T_{c}}-1\right) I_{\text {out }}^{C \rightarrow A}\left(E_{b}=E_{b}^{*}\right), \\
= & \left(\frac{T_{\mathrm{ph}}}{T_{c}}-1\right) \frac{q w \sqrt{d_{e} d_{h}}}{\tau_{\text {out }}}\left(k_{B} T_{c}\right) e^{-\left[\left(E_{g}-q V\right) / 2 k_{B} T_{c}\right]} \\
& \times \sqrt{E_{b}^{*}} e^{-E_{b}^{*} /\left(k_{B} T_{c}\right)}.
\end{aligned}
\tag{B10}
$$

In Fig. 3(a) in the main text, the heat depletion occurs for a device without an IR absorber when $P_{Q_{\text{in}}}<0$ in a parameter region surrounded by the solid blue curves. In the figure, for a given bias voltage in $0.25\ \text{V}<V<0.8\ \text{V}$, the heat depletion is found in two separated regions, i.e., $E_{b}<\mathcal{O}(E_{b}^{*})$ and $E_{b}^{**}<E_{b}<E_{b}^{c}$, where $E_{b}^{**}$ is estimated by

$$
P_{\text {sun }}-P_{T}=\left(E_{g}+2 E_{b}^{* *}+2 k_{B} T_{\mathrm{ph}}\right) \times\left(I_{\mathrm{sun}} / q\right), \quad (\mathrm{B} 11)
$$

which gives $E_{b}^{**}=0.404$ eV for Fig. 3(a) ($T_{\mathrm{ph}}=450$ K, $E_{g}=1.12$ eV, 1-sun blackbody sun at 6000 K). In this way, the nonmonotonic shape of the boundary [$P_{Q_{\text{in}}}=0$ in Fig. 3(a)] can be understood as the result of nonmonotonic $E_{b}$ dependency of $P_{Q_{\text{in}}}$ in Eq. (B9).

## APPENDIX C: NUMERICAL DATA FOR OPTIMAL PARAMETERS AT $\eta=\eta_{\text{max}}$

In Fig. 7, we show the numerical data for $\eta_{\text{max}}$ in a wide range of $T_{\mathrm{ph}}$ [300 K $\leq T_{\mathrm{ph}} \leq 2000$ K, Fig. 7(a)], and the optimal values for $\tau_{\text{out}}$ [Fig. 7(b)], $E_{b}$ [Fig. 7(c)], $V$, and $V^{\text{cell}}$ [Fig. 7(d)] at $\eta=\eta_{\text{max}}$ for a device with and without an IR absorber. As mentioned in the main text, the optimal $\tau_{\text{out}}$ increases with increasing $T_{\mathrm{ph}}$ [Fig. 7(b)], which gradually decreases optimal $E_{b}$ and $V$ [Figs. 7(c) and 7(d)] at high temperature where the max efficiency is limited by the heat supply (notice that $E_{b}^{c}$ decreases with increasing $\tau_{\text{out}}$ as shown in Appendix A). As a characteristic of HERC solar cell, as seen in Fig. 7 (d), the bias voltage can exceed $E_{g}$, which should of course be less than $E_{g}+2E_{b}$. The internal voltage (i.e., Fermi-level separation inside the absorber) decreases with increasing $T_{\mathrm{ph}}$, as shown in Fig. 7(d) (dashed lines). The negative and positive temperature dependencies of $V^{\text{cell}}$ and $V$ (in the linear regime) are consistent with those of $V_{\text{OC}}^{\text{cell}}$ and $V_{\text{OC}}$ as given in Eqs. (D10) and (D11).

![](./images/812706234976174081_8.jpg)

## APPENDIX D: TEMPERATURE DEPENDENCE OF THE OPEN-CIRCUIT VOLTAGES: $dV_{OC}/dT$ and $dV_{OC}^{cell}/dT$

Temperature dependence of the open-circuit voltages in the linear regime [Eqs. (51)-(53) in the main text] is easily obtained by setting, $T_c = T$, $T_{\rm ph} = T + dT$, $V = V_{\rm OC}^0 + dV_{\rm OC}$, and $V^{\rm cell} = V_{\rm OC}^{0} + dV_{\rm OC}^{\rm cell}$ and expanding the equations for the current under the open-circuit condition ($I=0$) to the first order in the small differences,

$$
0 = I_{\rm sun} - I_{\rm rad}(T_{\rm ph}, V^{\rm cell}) = -\frac{\partial I_{\rm rad}}{\partial T_{\rm ph}}dT - \frac{\partial I_{\rm rad}}{\partial V^{\rm cell}} dV_{\rm OC}^{\rm cell}, \tag{D1}
$$

$$
\begin{aligned}
0 = & I_{\rm out}(T_{\rm ph}, V^{\rm cell}, T_c, V) = \frac{\partial I_{\rm out}}{\partial T_{\rm ph}}dT + \frac{\partial I_{\rm out}}{\partial V^{\rm cell}} dV_{\rm OC}^{\rm cell} \\
& + \frac{\partial I_{\rm out}}{\partial V}dV_{\rm OC},
\end{aligned} \tag{D2}
$$

where all the derivatives are evaluated at $T_{\rm ph} = T_c = T$ and $V^{\rm cell} = V = V_{\rm OC}^0$ defined by $I_{\rm sun} - I_{\rm rad}(T, V_{\rm OC}^0) = I_{\rm out}(T, V_{\rm OC}^0, T, V_{\rm OC}^0) = 0$. From Eqs. (D1) and (D2), we have

$$
\frac{dV_{\rm OC}^{\rm cell}}{dT} = -\left( \frac{\partial I_{\rm rad}}{\partial T_{\rm ph}} \bigg/ \frac{\partial I_{\rm rad}}{\partial V^{\rm cell}} \right), \tag{D3}
$$

$$
\frac{dV_{\rm OC}}{dT} = -\left( \frac{\partial I_{\rm out}}{\partial T_{\rm ph}} \bigg/ \frac{\partial I_{\rm out}}{\partial V} \right) - \left( \frac{\partial I_{\rm out}}{\partial V^{\rm cell}} \bigg/ \frac{\partial I_{\rm out}}{\partial V} \right)\left( \frac{dV_{\rm OC}^{\rm cell}}{dT} \right). \tag{D4}
$$

As for the derivatives of $I_{\rm rad}$, we find from Eq. (41),

$$
\begin{aligned}
\frac{\partial I_{\rm rad}}{\partial T_{\rm ph}} = & q \times \frac{c}{2\pi^2} \frac{1}{(\hbar c)^3} \int_{E_g}^{\infty} \left( \frac{E - qV^{\rm cell}}{k_B T_{\rm ph}^2} \right) \\
& \times E^2 e^{-(E - qV^{\rm cell})/(k_B T_{\rm ph})} dE \approx \frac{E_g - qV^{\rm cell}}{k_B T_{\rm ph}^2} I_{\rm rad},
\end{aligned} \tag{D5}
$$

$$
\begin{aligned}
\frac{\partial I_{\rm rad}}{\partial V^{\rm cell}} = & q \times \frac{c}{2\pi^2} \frac{1}{(\hbar c)^3} \int_{E_g}^{\infty} \left( \frac{q}{k_B T_{\rm ph}} \right) \\
& \times E^2 e^{-(E - qV^{\rm cell})/(k_B T_{\rm ph})} dE = \frac{q}{k_B T_{\rm ph}} I_{\rm rad}. \tag{D6}
\end{aligned}
$$

For the derivatives of $I_{\rm out}$, we find from Eqs. (43)-(45),

$$
\frac{\partial I_{\rm out}}{\partial T_{\rm ph}} = \frac{\partial I_{\rm out}^{A \to C}}{\partial T_{\rm ph}} \approx \left( \frac{E_g - qV^{\rm cell} + 2E_b}{2k_B T_{\rm ph}^2} \right) I_{\rm out}^{A \to C}, \tag{D7}
$$

$$
\frac{\partial I_{\rm out}}{\partial V^{\rm cell}} = \frac{\partial I_{\rm out}^{A \to C}}{\partial V^{\rm cell}} = \frac{q}{2k_B T_{\rm ph}} I_{\rm out}^{A \to C}, \tag{D8}
$$

$$
\frac{\partial I_{\rm out}}{\partial V} = -\frac{\partial I_{\rm out}^{C \to A}}{\partial V} = -\frac{q}{2k_B T_c} I_{\rm out}^{C \to A} = -\frac{q}{2k_B T_c} I_{\rm out}^{A \to C}, \tag{D9}
$$

for $E_b \gg k_B T$, where we use a relation $I_{\rm out}^{C \to A} = I_{\rm out}^{A \to C}$ satisfied at the open-circuit condition. Inserting the above results for the derivatives with $T_{\rm ph} = T_c = T$ and $V^{\rm cell} = V = V_{\rm OC}^0$ into Eqs. (D3) and (D4), we finally have

$$
\frac{dV_{\rm OC}^{\rm cell}}{dT} \approx -\frac{E_g - qV_{\rm OC}^0}{qT}, \tag{D10}
$$

$$
\frac{d V_{\mathrm{OC}}}{d T} \approx \frac{E_{g}-q V_{\mathrm{OC}}^{0}+2 E_{b}}{q T}+\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=\frac{2 E_{b}}{q T}. \quad (\mathrm{D} 11)
$$

For conventional solar cells under an equilibrium condition $(T_c = T_{\rm ph})$, the negative temperature dependence is reproduced by performing a similar analysis with $T_c = T + dT$, $T_{\rm ph} = T + dT$, $V = V_{\rm OC}^0 + dV_{\rm OC}$, and $V^{\rm cell} = V_{\rm OC}^0 + dV_{\rm OC}^{\rm cell}$. In this case, the current equations under the open-circuit condition are

$$
\begin{aligned}
0=I_{\mathrm{sun}}-I_{\mathrm{rad}}\left(T_{\mathrm{ph}}, V^{\mathrm{cell}}\right)=-\frac{\partial I_{\mathrm{rad}}}{\partial T_{\mathrm{ph}}} d T-\frac{\partial I_{\mathrm{rad}}}{\partial V^{\mathrm{cell}}} d V_{\mathrm{OC}}^{\mathrm{cell}}, & \\
(\mathrm{D} 12) &
\end{aligned}
$$

$$
\begin{aligned}
0= & I_{\mathrm{out}}\left(T_{\mathrm{ph}}, V^{\mathrm{cell}}, T_{c}, V\right)=\frac{\partial I_{\mathrm{out}}}{\partial T_{\mathrm{ph}}} d T+\frac{\partial I_{\mathrm{out}}}{\partial V^{\mathrm{cell}}} d V_{\mathrm{OC}}^{\mathrm{cell}} \\
& +\frac{\partial I_{\mathrm{out}}}{\partial T_{c}} d T+\frac{\partial I_{\mathrm{out}}}{\partial V} d V_{\mathrm{OC}}, \quad (\mathrm{D} 13)
\end{aligned}
$$

Therefore, Eqs. (D3) and (D4) for HERC solar cell $(T_c \neq T_{\rm ph})$ are modified to

$$
\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=-\left(\frac{\partial I_{\mathrm{rad}}}{\partial T_{\mathrm{ph}}} \bigg/ \frac{\partial I_{\mathrm{rad}}}{\partial V^{\text {cell }}}\right), \quad (\mathrm{D} 14)
$$

$$
\begin{aligned}
\frac{d V_{\mathrm{OC}}}{d T}= & -\left(\frac{\partial I_{\mathrm{out}}}{\partial T_{\mathrm{ph}}}+\frac{\partial I_{\mathrm{out}}}{\partial T_{c}}\right) \bigg/\left(\frac{\partial I_{\mathrm{out}}}{\partial V}\right) \\
& -\left(\frac{\partial I_{\mathrm{out}}}{\partial V^{\text {cell }}} \bigg/ \frac{\partial I_{\mathrm{out}}}{\partial V}\right)\left(\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}\right), \quad (\mathrm{D} 15)
\end{aligned}
$$

in normal solar cells. The unknown derivative appeared in this case is

$$
\frac{\partial I_{\mathrm{out}}}{\partial T_{c}}=-\frac{\partial I_{\mathrm{out}}^{C \rightarrow A}}{\partial T_{c}} \approx-\left(\frac{E_{g}-q V+2 E_{b}}{2 k_{B} T_{c}^{2}}\right) I_{\mathrm{out}}^{C \rightarrow A}, (\mathrm{D} 16)
$$

which cancels with $\partial I_{\rm out}/\partial T_{\rm ph}$ in Eq. (D15). In this way, we find

$$
\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=\frac{d V_{\mathrm{OC}}}{d T} \approx-\frac{E_{g}-q V_{\mathrm{OC}}^{0}}{q T}, \quad (\mathrm{D} 17)
$$

for normal solar cells without the temperature difference.

## APPENDIX E: GENERALITY OF “$dV_{\rm OC}/dT=2E_b/(qT)$”

In the previous section, the temperature characteristics of the $V_{\rm OC}$ are shown to be given by Eq. (D11), in a simple case where the current loss is solely due to the radiative recombination ($I = I_{\rm sun} - I_{\rm rad}$). Here we consider the following factors that have strong temperature dependence and might alter the result in Eq. (D11):

(a) Nonradiative recombination can induce dominant loss with a strong dependence on the absorber’s temperature.

(b) Band-gap reduction due to an increase in the absorber’s temperature: $dE_g/dT_{\rm ph} \equiv -\alpha_g$ ($-0.28$ meV/K in Si [31]).

The nonradiative recombination can be included in the analysis by replacing $I_{\rm rad}$ with $I_{\rm loss}(=I_{\rm rad}+I_{\rm nr})$ in Eq. (D1). Normally in most cases, dominant mechanisms for nonradiative recombination in the absorber is due to the recombination mediated by trapping impurtiy states in the bulk [Shockley-Read-Hall (SRH) recombination [32]] or by surface states (surface recombination) whose energies are positioned deep inside the forbidden gap. According to Refs. [18] and [32], the recombination rate for these processes are given by

$$
\begin{aligned}
R_{\mathrm{SRH}} & =n_{\mathrm{imp}} v \sigma_{\mathrm{imp}} n_{i} \frac{\exp \left[\left(\mu_{c}^{\mathrm{cell}}-\mu_{v}^{\mathrm{cell}}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right]-1}{\exp \left[\left(\mu_{c}^{\mathrm{cell}}-E_{\mathrm{imp}}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right]+\exp \left[\left(E_{\mathrm{imp}}-\mu_{v}^{\mathrm{cell}}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right]+2}, \\
& =n_{\mathrm{imp}} v \sigma_{\mathrm{imp}} n_{i} \frac{\exp \left[\left(q V^{\mathrm{cell}}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right]-1}{\exp \left[\left(q V^{\mathrm{cell}}-\bar{E}_{\mathrm{imp}}\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)\right]+\exp \left[\left(q V^{\mathrm{cell}}+\bar{E}_{\mathrm{imp}}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right]+2}, \\
& \approx n_{\mathrm{imp}} v \sigma_{\mathrm{imp}} n_{i} \exp \left[\left(q V^{\mathrm{cell}}-\left|\bar{E}_{\mathrm{imp}}\right|\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)\right], \quad (\mathrm{E} 1)
\end{aligned}
$$

where $v$ and $n_i$ are the thermal velocity and the intrinsic density of the carriers, and $\sigma_{\rm imp}$, $n_{\rm imp}$, and $E_{\rm imp}$ are the scattering cross section, number density, and energy level of the impurity. The energy level of the impurity measured from the center of the Fermi levels is defined by $\bar{E}_{\rm imp} \equiv E_{\rm imp} - (\mu_c^{\rm cell} + \mu_v^{\rm cell})/2$. Surface recombination is also

given by the similar expression whereas the surface states locate at the absorber's surfaces and form a continuum of the energy levels spread over the forbidden gap. How- ever, as found from the expression in Eq. (E1), and as discussed in Sec. 6.5 of Ref. [18], effect of SRH recombination mainly comes from the impurities with the energy level close to the center of the Fermi levels, i.e., $\bar{E}_{imp} \approx 0$. This applies both to the recombi nation in the bulk or at the surface. By taking the major contribution from the impurity states with $\bar{E}_{imp} \approx 0$, we can approximate the nonradiative recombination rate is $R_{SRH} \approx n_{imp} v \sigma_{imp} n_{i} \exp [(q V^{cell}) /(2 k_{B} T_{ph})]$. Noticing $n_{i} \propto$  $e^{-E_{g} /(2 k_{B} T_{ph})}$ , the current loss from the nonradiative recom bination by the bulk and surface recombination (SRH mechanism) is given by

$$
I_{\mathrm{nr}} \propto \exp \left[-\left(E_{g}-q V^{\text {cell }}\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)\right]. \tag{E2}
$$

In this way, the total current loss $I_{rad}+I_{nr}$ is given by

$$
\begin{aligned}
I_{\mathrm{loss}} \approx & I_{\mathrm{rad}}+I_{\mathrm{nr}}=C_{\mathrm{rad}} \exp \left[-\left(E_{g}-q V^{\text {cell }}\right) /\left(k_{B} T_{\mathrm{ph}}\right)\right] \\
& +C_{\mathrm{nr}} \exp \left[-\left(E_{g}-q V^{\text {cell }}\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)\right], \tag{E3}
\end{aligned}
$$

where $C_{rad}$ and $C_{nr}$ depend on temperature only weakly and can be regarded as constants in the discussion presented here. Equation (E3) is consistent with the two-diode model for $p$ - $n$ junciton solar cell [18]. Exponential functions in $I_{loss }$ have a universal form $\{\exp [-(E_{g}-q V^{cell}) /(2 k_{B} T_{ph})]\}^{k}$ with $k=1$ and 2, which comes essentially from powers of the carrier densities. Considering this, the current loss due to the higher-order scattering processes seems to be given in the same form with $k>2$ (e.g., $k=3$ for Auger recombination). This observation indicates that the total current loss can be expressed in a more general form,

$$
I_{\text {loss }}=\sum_{k=1}^{\infty} C_{k} \exp \left[-k\left(E_{g}-q V^{\text {cell }}\right) /\left(2 k_{B} T_{\mathrm{ph}}\right)\right], \tag{E4}
$$

where the strong dependency on $T_{ph}$ and $V^{cell }$ comes only from the exponential functions. Using Eq. (E4) and replac- ing $I_{rad}$ with $I_{loss}$ in Eq. (D1), we find exactly the same result for $d V_{OC}^{cell} / d T$ ,

$$
\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=-\left(\frac{\partial I_{\text {loss }}}{\partial T_{\mathrm{ph}}} / \frac{\partial I_{\text {loss }}}{\partial V^{\text {cell }}}\right)=-\frac{E_{g}-q V_{\mathrm{OC}}^{0}}{q T}, \tag{E5}
$$

while Eq. (D11) for $d V_{OC} / d T$ also remains unchanged. Therefore, the temperature characteristics of the open- circuit voltages in HERC solar cells, given in Eq. (D10)[=Eq. (E5)] and Eq. (D11), are general results applicable even when the current loss is dominated by nonradiative recombinations.

Another factor that should be considered is the tem- perature dependence of the band gap: $d E_{g} / d T=-\alpha_{g}$ . An inclusion of this effect changes the temperature derivatives of $I_{loss }$ and $I_{out }$ in Eqs. (E5) and (D4) as

$$
\frac{\partial I_{\text {loss }}}{\partial T_{\mathrm{ph}}}=\left.\frac{\partial I_{\text {loss }}}{\partial T_{\mathrm{ph}}}\right|_{E_{g}=\text { fixed }}+\frac{d E_{g}}{d T_{\mathrm{ph}}} × \frac{\partial I_{\text {loss }}}{\partial E_{g}}, \tag{E6}
$$

$$
\frac{\partial I_{\text {out }}}{\partial T_{\mathrm{ph}}}=\left.\frac{\partial I_{\text {out }}}{\partial T_{\mathrm{ph}}}\right|_{E_{g}=\text { fixed }}+\frac{d E_{g}}{d T_{\mathrm{ph}}} × \frac{\partial I_{\text {out }}}{\partial E_{g}}. \tag{E7}
$$

Applying this change, we find

$$
\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=-\frac{E_{g}-q V_{\mathrm{OC}}^{0}+\alpha_{g} T}{q T}, \tag{E8}
$$

$$
\frac{d V_{\mathrm{OC}}}{d T}=\left(\frac{E_{g}-q V_{\mathrm{OC}}^{0}+\alpha_{g} T}{q T}+\frac{2 E_{b}}{q T}\right)+\frac{d V_{\mathrm{OC}}^{\text {cell }}}{d T}=\frac{2 E_{b}}{q T}. \tag{E9}
$$

Equation (E8) clearly shows that the internal voltage $V_{OC}^{cell }$  decreases more strongly due to the band-gap reduction with increasing $T_{ph}$ . However, the strong degradation effect is perfectly canceled in the output bias voltage $V_{OC}$ with the increased thermoelectric voltage $d(V_{OC}-V_{OC}^{cell}) / d T$ , in a similar manner to the result for the case without the band-gap change $(\alpha_{g}=0)$ .

The above results strongly indicate that the positive tem- perature characteristics, generally given by $d V_{OC} / d T=$ 2Eb/(qT), is a general feature of HERC solar cells (uti- lizing the temperature difference), which cannot be lost easily even if other degradation factors are present. Of course, degradation factors reduce the value itself of $V_{OC}^{0}$ . However, the temperature derivative $d V_{OC} / d T$ remain unchanged as given by $2 E_{b} /(q T)>0$ .

[1] K. Yoshikawa, W. Yoshida, T. Irie, H. Kawasaki, K. Kon ishi, H. Ishibashi, T. Asatani, D. Adachi, M. Kanematsu, H. Uzu, and K. Yamamoto, Exceeding conversion efficiency of $26 \%$ by heterojunction interdigitated back contact solar cell with thin film Si technology, Sol. Energy Mater. Sol. Cells 173, 37 (2017).

[2] W. Shockley and H. J. Queisser, Detailed balance limit of efficiency of $p-n$ junction solar cells, J. Appl. Phys. 32, 510(1961).

[3] A. Richter, M. Hermle, and S. W. Glunz, Reassessment of the limiting efficiency for crystalline silicon solar cells, IEEE J. Photovoltaics 3, 1184 (2013).

[4] M. A. Green, Y. Hishikawa, W. Warta, E. D. Dunlop, D. H. Levi, J. Hohl-Ebinger, and A. W. Ho-Baillie, Solar cell efficiency tables (Version 50), Prog. Photovoltaics 25, 668(2017).

[5] E. D. Jackson, Solar energy convertor, U.S. Patent No. 2,949,498 (16 August 1960).

[6] A. De Vos, Detailed balance limit of the efficiency of tandem solar cells, J. Phys. D: Appl. Phys. 13, 839 (1980).

[7] R. T. Ross and A. J. Nozik, Efficiency of hot-carrier solar energy converters, J. Appl. Phys. 53, 3813 (1982).

[8] P. Würfel, Solar energy conversion with hot electrons from impact ionisation, Sol. Energy Mater. Sol. Cells 46, 43 (1997).

[9] Y. Takeda, T. Motohiro, D. König, P. Aliberti, Y. Feng, S. Shrestha, and G. Conibeer, Practical factors lowering conversion efficiency of hot carrier solar cells, Appl. Phys. Exp. 3, 104301 (2010).

[10] Y. Takeda, A. Ichiki, Y. Kusano, N. Sugimoto, and T. Motohiro, Resonant tunneling diodes as energy-selective contacts used in hot-carrier solar cells, J. Appl. Phys. 118, 124510 (2015).

[11] A. Luque and A. Martí, Increasing the Efficiency of Ideal Solar Cells by Photon Induced Transitions at Intermediate Levels, Phys. Rev. Lett. 78, 5014 (1997).

[12] K. Kamide, T. Mochizuki, H. Akiyama, and H. Takato, in 2018 IEEE 7th World Conference on Photovoltaic Energy Conversion (WCPEC) (A Joint Conference of 45th IEEE PVSC, 28th PVSEC & 34th EU PVSEC) (Waikoloa Village, HI, 2018), p. 1817.

[13] K. Kamide, T. Mochizuki, H. Akiyama, and H. Takato, Nonequilibrium Theory on the Conversion Efficiency Limit of Solar Cells Including Thermalization and Extraction of Carriers, Phys. Rev. Appl. 10, 044069 (2018).

[14] T. Suzuki and R. Shimano, Cooling dynamics of photoexcited carriers in Si studied using optical pump and terahertz probe spectroscopy, Phys. Rev. B 83, 085207 (2011).

[15] J. R. Goldman and J. A. Prybyla, Ultrafast Dynamics of Laser-Excited Electron Distributions in Silicon, Phys. Rev. Lett. 72, 1364 (1994).

[16] A. J. Sabbah and D. M. Riffe, Femtosecond pump-probe reflectivity study of silicon carrier dynamics, Phys. Rev. B 66, 165217 (2002).

[17] M. Green, Third Generation Photovoltaics: Advanced Solar Energy Conversion (Springer-Verlag, Berlin, Heidelberg, 2003).

[18] P. Würfel and U. Würfel, Physics of Solar Cells: From Basic Principles to Advanced Concepts (Wiley-VCH, Weinheim, 2016), 3rd ed.

[19] U. Würfel, A. Cuevas, and P. Würfel, Charge carrier separation in solar cells, IEEE J. Photovoltaics 5, 461 (2015).

[20] Electron-hole separation for the extraction is realized in various ways, e.g., by a formation of $p$-$n$ junction in the absorber or doped regions producing large contrasts in conductivities for the majority and minority carriers [18,19]. In Fig. 1(b), an infinitely high potential barrier perfectly blocks electrons (holes) from being extracted to or injected from the hole (electron) contact.

[21] P. Würfel, The chemical potential of radiation, J. Phys. C: Solid State Phys. 15, 3967 (1982).

[22] H. Fritzsche, A general expression for the thermoelectric power, Solid State Commun. 9, 1813 (1971).

[23] Le Si Dang, G. Neu, and R. Romestain, Optical detection of cyclotron resonance of electron and holes in CdTe, Solid State Commun. 44, 1187 (1982).

[24] S. M. Wasim, L. Essaleh, C. Rincoón, G. Marín, J. Galibert, and J. Leotin, Density of states effective mass of $n$-type CuInSe₂ from the temperature dependence of Hall coefficient in the activation regime, J. Phys. Chem. Solids 66, 1887 (2005).

[25] H. Neumann, H. Subotta, W. Kissinger, V. Riede, and G. Kuhn, Hole effective masses in CuInSe₂, Phys. Status Solidi B 108, 483 (1981).

[26] I. T. Witting, T. C. Chasapis, F. Ricci, M. Peters, N. A. Heinz, G. Hautier, and G. J. Snyder, The thermoelectric properties of bismuth telluride, Adv. Electron. Mater. 5, 1800904 (2019).

[27] C. Ge, M. Hu, P. Wu, Qi Tan, Z. Chen, Y. Wang, J. Shi, and J. Feng, Ultralow thermal conductivity and ultrahigh thermal expansion of single-crystal organic-inorganic hybrid perovskite CH₃NH₃PbX₃ (X = Cl, Br, I), J. Phys. Chem. C 122, 15973 (2018).

[28] W. Lee, H. Li, A. B. Wong, D. Zhang, M. Lai, Y. Yu, Q. Kong, E. Lin, J. J. Urban, J. C. Grossman, and P. Yang, Ultralow thermal conductivity in all-inorganic halide perovskites, PNAS 114, 8693 (2017).

[29] J.-K. Yu, S. Mitrovic, D. Tham, J. Varghese, and J. R. Heath, Reduction of thermal conductivity in phononic nanomesh structures, Nat. Nanotechnol. 5, 718 (2010).

[30] P. E. Hopkins, C. M. Reinke, M. F. Su, R. H. Olsson, E. A. Shaner, Z. C. Leseman, J. R. Serrano, L. M. Phinney, and I. El-Kady, Reduction in the thermal conductivity of single crystalline silicon by phononic crystal patterning, Nano Lett. 11, 107 (2011).

[31] P. Y. Yu and M. Cardona, Fundamentals of Semiconductors: Physics and Material Properties (Springer, New York, 2005), 3rd ed.

[32] W. Shockley and W. T. Read, Statistics of the recombinations of holes and electrons, Phys. Rev. 87, 835 (1952).