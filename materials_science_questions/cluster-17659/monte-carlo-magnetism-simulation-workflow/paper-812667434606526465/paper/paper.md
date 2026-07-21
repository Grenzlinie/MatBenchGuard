# Monte Carlo simulation of adiabatic cooling and nuclear magnetism

P.- A. Lindgård
Physics Department, Risø National Laboratory, DK-4000 Roskilde, Denmark

H. E. Viertiö
Low Temperature Laboratory, Helsinki University of Technology, SF-02150 Espoo, Finland

O. G. Mouritsen
Department of Structural Properties of Materials, The Technical University of Denmark, DK-2800 Lyngby, Denmark

(Received 7 March 1988)

A two-dimensional classical spin model of nuclear antiferromagnetism is studied by Monte Carlo computer simulation techniques as well as by mean-field calculations. The model includes nearest-neighbor dipolar and exchange interactions and a single-ion term. The phase boundary of the antiferromagnetic phase in the external-field-temperature plane exhibits sections of both first- and second-order transitions separated by a tricritical point. Particular attention is paid to the isentropes of the phase diagram, which correspond to the thermodynamic paths of constant entropy followed in experimental studies of nuclear magnetism using adiabatic demagnetization methods. It is found that, although fluctuations reduce the transition temperatures by 40%, the isentropes are reduced by less than 10% relative to those calculated by mean-field theory. The dynamics of the ordering process following constant-temperature or constant-magnetic-field quenches into the antiferromagnetic phase is found at late times to obey the classical Allen-Cahn growth law. The qualitative features of isentropic quenches and the nonequilibrium ordering phenomena during controlled heating treatments at constant rate are discussed in relation to recent experimental observations from neutron scattering experiments on nuclear antiferromagnetism in Cu.

## I. INTRODUCTION

Extremely low temperatures can be reached by adiabatic cooling of a nuclear magnetic system. In the case of $Cu,^{1}$ temperatures near $30 \mathrm{nK}\ (1 \mathrm{nK}=10^{-9} \mathrm{K})$ have been obtained. Both by static susceptibility measurements, $^{1}$ and very recently also by neutron scattering experiments, $^{2}$ the nuclear moments in Cu have been found to order antiferromagnetically at around 60 nK, with an intriguing phase diagram as a function of magnetic field $H$ and entropy $S$.

The nuclear magnetic systems are much purer with respect to the interactions than the usual electronic magnets. Thus, the Hamiltonian parameters can be calculated accurately from first principles $^{3}$ and there are, for example, no magnetoelastic effects. From a thermodynamic point of view, knowledge about phase transitions, magnetic order and phase diagrams are usually available only in terms of the variables $(H,T)$ for a system in equilibrium at a constant temperature $T$, set by a heat bath. For the nuclear magnet the spin system is an isolated system, not in contact with a heat bath, and it is better characterized by its entropy. In order to appreciate the ideal model systems of nuclear magnetism it is, therefore, important to understand the similarities and differences for a system described isothermally in the $(H,T)$ plane and adiabatically in the $(H,S)$ plane. It is the purpose of this paper to elucidate this question.

In the adiabatic cooling process, the nuclear spin system in the paramagnetic phase is almost fully polarized by the application of a large magnetic field $H$ at a temperature $T$, thus the corresponding entropy $S=S_{0}$ is small. When the spin-lattice relaxation time $\tau_{\mathrm{sl}}$ is much longer than the spin-spin relaxation time $\tau_{\mathrm{ss}}$ there is no heat exchange $d Q$ between the nuclear spin system and the lattice on the time scale of interest, which is of the order $\tau_{\mathrm{ss}}$. Therefore, the entropy is constant since

$$
d S=d Q / T=0. \tag{1}
$$

Hence, when the field is removed adiabatically the system lowers its temperature $T(S_{0})$, while conserving the entropy. It is of considerable interest to understand how the spontaneous antiferromagnetic (AFM) order evolves from the field-induced, ferromagnetically aligned state. We wish to determine the temperature $T(S_{0})$ reached at $H=0$ for a given entropy $S_{0}$, as well as the ordering dynamics and domain pattern formation of the formed AFM structure. Previously the relation between temperature and entropy has relied on mean-field theory $^{1}$ which neglects correlation effects. It is important to understand their influence on $T(S_{0})$, in particular for Cu which has large fluctuations because its spin system is essentially a frustrated nearest-neighbor (NN) antiferromagnet with a fcc lattice.

In order to study the effects of correlations and fluctuations as well as the question of domain formation in nonequilibrium, we have applied Monte Carlo computer simulation techniques to a simple two-dimensional (2D) spin model, for which fluctuation effects are particularly large.

The model, which includes nearest-neighbor dipole and isotropic exchange forces between classical spins and a fourth-order, single-ion anisotropy term, leads to AFM order described by a two-dimensional order parameter. Hence, there are four degenerate types of ordered domains. The order-parameter degeneracy is discrete. The phase diagram as a function of field exhibits both first-order transitions and second-order (continuous) tran- sitions separated by a tricritical point. It thus allows an investigation of constant entropy lines (isentropes) cross- ing both first-order as well as second-order phase lines.

The experimentally studied nuclear spin system of Cu is governed by the dipole-dipole interaction and a dom- inant (NN) isotropic Ruderman-Kittel (RK) interaction. $^{3}$ Since the spin is $I=\frac{3}{2}$ there is no fourth-order anisotropy. Consequently, the mean-field AFM ground state is continuously degenerate with respect to linear combinations of ordering wave vectors and polarization directions of the spins. $^{4}$ Thus, an infinite number of different domains is possible. Yet, quantum fluctuations reduce the degeneracy to that allowed by the crystal symmetry, $^{5}$ i.e., typically 4 or 8 types of domains. In our classical model the problem is simplified by the anisotropy term and we study the competition of only four types of domains. The long-range nature of the dipolar and RK interactions manifests itself in particular at long wave- length $(k=0)$ and is not important for the antiferromagnetic order. For the classical spin system the entropy tends to minus infinity for $T=0$, whereas for the quantum system the entropy vanishes. Despite these differences we expect that a number of qualitative features of the model will be useful as a guide for the un- derstanding of Cu.

The paper is organized as follows. We will first discuss the calculated equilibrium properties and compare the results of the Monte Carlo simulations with mean-field theory. In particular, we calculate the isentropes in equi- librium. Subsequently the dynamics of the transition is studied using quenches both in constant field and temper- ature. We also attempt to simulate a constant-entropy quench by guiding the system along an isentrope. Finally, the effect of heating the ordered spin system at a con- stant heat exchange rate is simulated.

## II. THE MODEL

Let us consider a two-dimensional square array of size $N=L^{2}$ of classical spins interacting via the following Hamiltonian:
$$
\begin{aligned}
\mathcal{H}= & J \sum_{i j}\left[\mathbf{S}_{i} \cdot \mathbf{S}_{j}-2\left(\mathbf{S}_{i} \cdot \hat{\mathbf{r}}_{i j}\right)\left(\mathbf{S}_{j} \cdot \hat{\mathbf{r}}_{i j}\right)\right] \\
& -P \sum_{i}\left(S_{i x}^{4}+S_{i y}^{4}\right)-H \sum_{i} S_{i z},
\end{aligned}\tag{2}
$$
where $\hat{\mathbf{r}}_{i j}$ is a unit vector connecting nearest neighbors. The interaction $J$ in combination with the anisotropy $P(=2 J)$ favors at low temperature an antiferromagnetic order of aligned spin chains in either the $x$ or $y$ direction, forming four possible domains (see Fig. 1). The relative magnitudes of the exchange and dipolar interactions have been chosen so that the interaction strengths along and between the chains are equal. At high fields $H$ there is a transition to an $x, y$ paramagnetic state polarized along $z$, perpendicular to the plane. For $P \to 0$, the model belongs to the class of isotropic $X Y$ models in two dimensions for which it is known that there is no true long-range order. $^{6}$ The limit $P \to 0$ in two dimensions will therefore not be appropriate for a simulation of Cu. This limit must be studied using a three-dimensional model. The advantage of using the two-dimensional system is that it is easy to visualize the domain distributions and that one can study much larger systems than practicably possible in three di- mensions. Furthermore, the fluctuation effects are large, but limited when $P$ is finite.

![](./images/812667434606526465_1.jpg)

FIG. 1. The four possible antiferromagnetic domains in the ordered phase at $H=0$.

## III. STATIC PROPERTIES

The equilibrium properties of the model are calculated by the mean-field theory and by Monte Carlo computer simulation using Glauber dynamics. $^{7}$ In most runs the spins are visited sequentially and the statistics generated ranges up to 3000 Monte Carlo steps per site (MCS). Several different system sizes, $N=20^{2}, N=64^{2}$, and $N=200^{2}$, are considered in order to evaluate finite-size effects. The thermal properties (per spin) calculated directly include the magnetic enthalpy $E$, the components of the AFM order parameter, i.e., the staggered magnetization $M_{\perp}$, the induced ferromagnetic magnetization $M_{z}$, the specific heat $C_{H}$, and the ferromagnetic susceptibility $\chi_{0}^{zz}$, viz.
$$
\begin{aligned}
E & =\langle\mathcal{H}\rangle / N, \\
M_{\perp} & =\sum_{i}\left\langle e^{i \mathbf{k} \cdot \hat{\mathbf{r}}_{i j}} S_{i x}\right\rangle / N, \\
M_{z} & =\sum_{i} S_{i z} / N, \\
C_{H} & =\left(\left\langle\mathcal{H}^{2}\right\rangle-\langle\mathcal{H}\rangle^{2}\right) /\left(N k_{B} T^{2}\right), \\
\chi_{0}^{z z} & =\left[\left\langle\sum_{i} S_{i z}\right\rangle^{2}-\left\langle\sum_{i} S_{i z}\right\rangle^{2}\right] /\left(N k_{B} T\right).
\end{aligned}\tag{3}
$$

On the basis of these quantities the phase diagram is constructed using standard principles. $^{7}$ By choosing units such that $J=k_{B}=1$ and $S=1$ all quantities on the plots are dimensionless for simplicity. In the AFM ordered phase, equilibrium is obtained by starting at $H=0$ from a single-domain configuration at a given $T$ and subsequently increasing $H$ in steps up to a high field $H_{0}$. The system

is equilibrated after each step.

Figure 2 shows the calculated staggered magnetization $M_{\perp}$ and the induced magnetization $M_{z}$ as a function of $T$ and $H$ for two different system sizes. Despite the finite-size rounding effects it is clear that the phase transition is of first order at low temperatures. The first-order jump in $M_{z}$ at $T=0$ and $M_{z}(0, H)$ are calculated exactly, yielding some exact borders on the phase diagram. The first-order transition manifests itself as a clear change in slope $d E / d H$ of $E$ versus $H$ at constant $T$. Similarly, the jump $\Delta M_{\perp}$ in $M_{\perp}$ in Fig. 2 is well resolved, whereas it is difficult to follow the corresponding jump in $M_{z}$. On Fig. 3 is shown the temperature variation of $d E / d H$ and $\Delta M_{\perp}$, which consistently idicates that the transition becomes of second-order at the tricritical point $T^{*}$ $\simeq 0.5 J / k_{B}$.

In order to calculate the entropy we use the fundamental thermodynamic relation between the induced magnetization $M_{z}$ and the Gibbs free energy $F$ per spin: $M_{z}=-\partial F / \partial H$. At high fields the free energy $F\left(T, H_{0}\right)$ can be calculated very accurately using mean-field theory.

![](./images/812667434606526465_2.jpg)

FIG. 2. The staggered magnetization $M_{\perp}$ and the induced ferromagnetic component $M_{z}$ obtained by Monte Carlo simulation for two systems $(\bullet) N=20^{2}$ and $(\bigcirc) N=64^{2}$. Some finite-size rounding effects are evident, but also a clear indication of a first-order transition. An exact calculation yields $M_{z}(H)$ at $T=0$.

![](./images/812667434606526465_3.jpg)

FIG. 3. The first-order transition and the tricritical point $T^{*}$ is determined from the change at the phase boundary in the slope $d E / d H$ of the magnetic enthalpy $E=\langle H\rangle$ and the jump in the staggered magnetization $\Delta M_{\perp}=M_{\perp}(\mathrm{AFM})-M_{\perp}(\mathrm{PARA})$.

By numerical integration one can then derive the free energy at a lower field $H$

$$
F(T, H)=F\left(T, H_{0}\right)-\int_{H_{0}}^{H} M_{z}\left(T, H^{\prime}\right) d H^{\prime}. \tag{4}
$$

We have used $H_{0}=30 J$, which for all relevant temperatures gives a magnetization $M_{z}\left(T, H_{0}\right)$ deviating less than $5 \%$ from the saturation value 1. The entropy at a given temperature can then be calculated from the relation $F=E-T S$, which gives

$$
S=\frac{1}{T}\left\lfloor E(T, H)-F\left(T, H_{0}\right)+\int_{H_{0}}^{H} M_{z}\left(T, H^{\prime}\right) d H^{\prime}\right\rfloor. \tag{5}
$$

The magnetic enthalpy $E=\langle\mathcal{H}\rangle / N$ and the induced magnetization $M_{z}$ (see Fig. 2) are calculated by the Monte Carlo method for a grid of $(T, H)$ points for fields up to $H=H_{0}=30 J$. The entropy at constant field as a function of temperature is then found by interpolation. The result is shown on Fig. 4. The interpolation allows more information to be extracted from the data than indicated by the points $(\bigcirc)$. At $H=8 J$ there is an indication of a very small jump in the entropy corresponding to only a very small latent heat at this first-order transition. We return to this feature below. For completeness we also show on Fig. 5 the uniform susceptibility along the field, $\chi_{0}^{z z}$, calculated partly directly and partly from the data on Fig. 2. It is evident that the nature of the transition is not easily obtainable from $\chi_{0}^{z z}$, and also that the AFM transition in low fields is only very weakly visible. These conclusions, which are consequences of the fact that $\chi_{0}^{z z}$ is not the ordering susceptibility, are expected to be true also for the real $\mathrm{Cu}$ system.

To construct the line of phase transitions, $T_{N}(H)$, we have used primarily the data on Fig. 2, supplemented by the calculated $C_{H}$. The result is shown in Fig. 6. The first-order line obtained by analyzing $d E / d H$ is indicated by a dashed curve. The second-order line is indicated by the solid curve. The thin lines indicate the calculated isentropes obtained by interpolation of $S(T, H)$ data cal-

![](./images/812667434606526465_4.jpg)

FIG. 4. The entropy $S$ vs temperature at different values of the field. The transition is of first order at $H=8 J$ and shows a small discontinuity corresponding to a small latent heat. The arrows indicate the transition temperatures.

![](./images/812667434606526465_5.jpg)

FIG. 5. The uniform susceptibility along the field $\chi_{0}^{zz}$. The arrows indicate the transition temperature. One notices that neither the temperature nor the order of the transition is well determined by $\chi_{0}^{zz}$.

culated equidistantly at $k_{B} T / J=0.1,0.2, \ldots, 1.1$.

By inspection of Fig. 6 we notice an interesting property of the model. By the adiabatic removal of the field, i.e., by following an isentrope, one reaches the lowest temperature at or above the phase boundary, and the temperature increases again in the ordered phase. The physical reason for this phenomenon is the anisotropy term $P$ in Eq. (2). This term contributes little to the enthalpy in the ferromagnetically polarized state, polarized along the $z$ direction, but it contributes significantly with the onset of the AFM order in the $X Y$ plane. At high temperatures the effect sets in already before reaching the phase boundary, clearly showing the influence of the onset of AFM short-range order. We also notice that the isentropes pass the second-order phase boundary with no noticeable change in slope within the available accuracy. At the first-order phase boundary, small discontinuities in the isentropes are observed indicating that a small latent heat is accompanying this transition. It is interesting that our model, for example, at $k_{B} T / J=0.1$ shows that the entropy is actually higher in the AFM ordered phase than in the paramagnetic phase at the transition point, which is counterintuitive.

For comparison we show on Fig. 7 the phase diagram and the isentropes calculated for the model, Eq. (2), by means of the mean-field theory. We notice that the results of Figs. 6 and 7 are nearly identical at low temperatures, $k_{B} T<0.3 J$. In particular, the isentropes show a similar discontinuity towards lower $T$ in the ordered phase. The reason is here more clear. It is simply a consequence of the fact that the first-order boundary initially increases with temperature, clearly visible in Fig. 7, but also noticeable in Fig. 6. At the point where the boundary is horizontal (independent of $T$ ) there is no discontinuity in the entropy and no latent heat at the first-order transition. This phenomenon has previously also been found in other models. It follows from the Clausius-Clapeyron equation for the slope of the phase boundary $H=H(T)$, which can be written

$$
\left.\frac{d H(T)}{d T}\right|_{T_{N}(H)}=-\frac{S(\mathrm{AFM})-S(\mathrm{PARA})}{M_{z}(\mathrm{AFM})-M_{z}(\mathrm{PARA})}. \quad \text { (6) }
$$

At higher $T$ in Fig. 6 there is a small latent heat and a small discontinuity in the isentropes towards higher temperatures in the ordered phase. This corresponds to a lower entropy in the ordered phase at constant $T$, which is intuitively more obvious. The discontinuity vanishes as the tricritical point is approached.

By analytic expansion of the mean-field (MF) free energy the tricritical point is found to be $k_{B} T_{\mathrm{MF}}^{*} \cong 0.3 J$, which is lower than $k_{B} T^{*} \cong 0.5 J$ found by the Monte Carlo simulation, Fig. 3. The fluctuations, therefore, enhance the first-order nature of the transition. On the other hand, the ordering temperature at $H=0$ is strongly reduced by fluctuation effects, $T_{N}^{\mathrm{MF}}(H=0)=1.5 J / k_{B}$,

![](./images/812667434606526465_6.jpg)

FIG. 6. The phase diagram obtained by Monte Carlo simulation on systems of size $N=64^{2}$. The isentropes are calculated by integrating $M_{z}(H)$ from high fields. One notices small discontinuities at the first-order boundary, but no change at the second-order boundary. Short-range order effects persist far above the phase boundary giving rise to the bending of the isentropes at high $T$.

whereas $T_{N}^{\mathrm{MC}}(H=0)=0.95 \mathrm{~J} / k_{B}$. Judged with respect to the phase boundaries the isentropes behave strikingly different in the mean-field theory and the Monte Carlo simulation. The mean-field isentropes show an increasing temperature dependence right at the phase boundary, with a sharp kink at the second-order phase line. In the Monte Carlo simulation the increasing temperature dependence occurs at approximately the same $(T, H)$ location, but now well above the phase boundary at high $T$. This shows that the short-range order effects set in approximately where the mean-field theory predicts the onset of long-range order. In the Monte Carlo simulation we do not see any sharp change in the isentropes when crossing the second-order lines, with the present $(T, H)$ grid. It is concluded that the isentropes on an absolute $(T, H)$ scale are quite accurately calculated by means of the mean-field theory, except very close to the true phase boundary. The phase boundary is, however, significantly renormalized in temperature. We expect this conclusion to be applicable also for $\mathrm{Cu}$, where $T_{N}$ is reduced by fluctuations to $0.25 T_{N}^{\mathrm{MF}} .^{3}$

![](./images/812667434606526465_7.jpg)

FIG. 7. The phase diagram calculated by the mean-field theory including directly calculated isentropes. A comparison with Fig. 6 shows that the phase boundary is much reduced by fluctuations, whereas the isentropes remain quite accurately described by the mean-field theory for $T \leq T_{N}^{\mathrm{MF}}(H=0)$.

## IV. DYNAMICS OF THE ORDERING PROCESS

The ordering of the individual spin in its local magnetic field is a very fast process on the experimental time scale. Conversely, the dynamics of the nonequilibrium domain-boundary network, which is formed during the global ordering process, is much slower. When the system is taken across the phase boundary in Fig. 6 into the antiferromagnetic phase, domains of all four thermodynamically equivalent types of order in Fig. 1 are nucleated simultaneously. At late times, the ordered domains cover the whole system and they start competing. The consequences of this competition is domain growth and it may be described via the dynamics of the random network of boundaries which separate the domains. It is the interfacial energy associated with the curvature of the domain boundaries which provides the driving force for the growth. $^{8}$

There is currently a strong experimental and theoretical interest in characterizing possible universal aspects of domain-growth kinetics. $^{9}$ Of particular interest is to study the dependence on the ordering degeneracy, $p$, and the nature of the conservation laws. The adiabatic ordering process provides in this context an interesting situation which has not been studied before. The antiferromagnetic order of our model has $p=4$ and the ordering process in the experimental system is subject to the unusual law of entropy conservation. We are unable, in a computer simulation of the models of the type studied here, to rigorously enforce a constant-entropy law. Therefore, we have simulated a quasiconstant-entropy annealing process by guiding the system through a series of nonequilibrium states close to an equilibrium isentrope. Furthermore, we have performed constant-temperature and constant-field quenches without any conservation laws imposed.

Firstly, we describe the results of constant-temperature and constant-field quenches for systems with $N=64^{2}$. Both types of quenches have been performed to two different points within the ordered phase $(T_{1}, H_{1})=(0.7 J / k_{B}, 0)$ and $(T_{2}, H_{2})=(0.4 J / k_{B}, 4 J)$. The constant-field quenches are started from equilibrium configurations typical for initial temperatures $k_{B} T_{i} / J=1.5$. The constant-temperature quenches are started from $H_{i}=11.0 \mathrm{~J}$. The quenches are carried out by suddenly assigning the new values of the independent thermodynamic variables, and the growth process is then

monitored on a time scale of MCS using standard techniques. $^{7}$ For convenience, we focus on the time dependent inverse excess energy
$$\Delta E^{-1}(t)=[E(t)-E(T, H)]^{-1} \sim R(t) \sim t^{n},\qquad(7)$$
which scales as the average linear domain size, $R(t)$ as discussed by Sadiq and Binder. $^{10} E(t)$ is the nonequilibrium energy at time $t$ and $E(T, H)$ is the equilibrium energy at the point towards which the quench is directed. $\Delta E(t)$ is a measure of the total nonequilibrium internal energy associated with the entire domain-boundary network. It is convenient to use $\Delta E^{-1}(t)$ as a measure of linear scale since it is a self-averaging quantity $^{11}$ which is easy to obtain with good statistical accuracy. We have in Eq. (7) anticipated that at late times the domains will grow according to a simple power law. $^{9}$ The data forΔE(t) for both types of quench are obtained as an ensemble average over ten independent quenches realized using different initial configurations and different random number sequences.

In Fig. 8 we show the results for $\Delta E^{-1}(t)$ for the different quenches. It is seen that all sets of data are consistent with a power law at late times and that the exponent is the same in all cases, independent of field and temperature and independent of whether the quench is performed in field or temperature. The arrows indicate where finite-size effects start to be important $[R(t) \simeq 0.4 L].^{11}$ Data obtained for the $N=200^{2}$ system confirm this power law and finite-size effects set in only at a later time. The value of the exponent, $n \simeq 0.50$, is consistent with the classical value predicted theoretically by Lifshitz $^{12}$ and by Allen and Cahn $^{8}$ for systems with non conserved order parameter. This result is furthermore in accordance with recent finite-temperature quench studies of a general class of two-dimensional anisotropic $X Y$ models $^{13}$ to which the present model belongs. This class of models is characterized by its capacity of supporting "soft" domain walls, however, at finite temperatures give rise to the same kinetic growth exponent as hard-wall Ising and Potts models. Our results thus give further testimony to the universal classification ofdomain-growth kinetics. $^{14}$ 

We then turn to our attempt to perform a quasi-isentropic quench. We chose to study one isentrope $S=-3.0 k_{B}$ crossing a first-order transition line and one isentrope $S=-1.4 k_{B}$ crossing a second-order transition line. The quench is simulated by guiding the system along the path by successively assigning corresponding values of $T$ and $H$ in the direction towards the ordered phase. The quench along $S=-3.0 k_{B}$ was performed in13 steps starting from $(T, H)=(0.35 J / k_{B}, 14.1 J)$ down to $(0.35 J / k_{B}, 0)$ . For the quench along $S=-1.4 k_{B}$ tensteps were used starting from $(T, H)=(0.8 J / k_{B}, 9.5 J)$  down to $(T, H)=(0.8 J / k_{B}, 0)$ . The steps were equidistant in $H$ . At each step the system was allowed to equilibrate for 300 MCS. In principle, this procedure does not strictly follow the isentrope since the system is never allowed to come to equilibrium. However, by choosing appropriate equilibration times at each step along the path we expect that the degree of local ordering obtained at each point reflects faithfully the entropy at that point, except for the entropy $\Delta S$ associated with the domain boundaries. This can be approximated by $\Delta S=\Delta E / T$ , where AE is the excess energy of the system relative to that in thermal equilibrium. In the studied constant entropy quenches we found that $\Delta S$ is quite small $\Delta S<0.1 S$ compared with the total entropy $S$ . Hence, we are following the isentrope very closely, but are at the same time allowing for a nonequilibrium domain distribution. The annealing of this distribution is slow on the time scale chosen for the isentropic quench. By comparing the final domain distribution and morphology after an accumulated number of $13 \times 300$ or $10 \times 300$ MCS with that ob

![](./images/812667434606526465_8.jpg)

FIG. 8. The time dependence of the excess magnetic enthalpy, $\Delta E(t)$ , after a rapid quench is indicative of the characteristic domain growth behavior. At the bottom are shown quenches in field and temperature across the second-order boundary to $(T, H)=(0.7 J / k_{B}, 0)$ and at the top similar quenches across the first-order boundary to(T,H)=(0.4J/kg,4J). Quenches in both field and temperature behave similarly and are consistent with the classical domain growth law, Eq. (7), with $n=\frac{1}{2}$ . The solid lines are guides tothe eye with slope $n=\frac{1}{2}$ through the data points at $t=100$  MCS. The arrows indicate the time at which the domains have grown to a size where finite-size effects set in. The data are averaged over ten different runs. The "error bars" indicate the maximum deviation of the various runs.

tained by similar either constant-field or constant- temperature step-by-step quenches to the same point, $(T,H)=(0.35J/k_{B},0)$ or $(0.8J/k_{B},0)$, we find no significant differences. This seems to indicate that quasi- isentropic annealing does not lead to any peculiarities re- garding the domain structure of the antiferromagnetic phase.

## V. SIMULATION OF THE EFFECT OF HEATING
A nuclear spin system, with a low spin temperature $T$ relative to the lattice temperature $T_{L}$, is on a time scale longer than $\tau_{ss}$ heating at an approximately constant heat exchange rate. Furthermore, in a neutron scattering ex- periment the interaction with the neutrons will contrib- ute to a constant influx of heat into the spin system. It is therefore very relevant for the experimental situation to illustrate the effects of heating at a constant rate by means of a computer simulation. A system in equilibri- um at a temperature $T(S)$ increases its entropy $S$ by the amount $dS=dQ/T(S)$ when heated by a heat pulse $dQ$. The new equilibrium temperature is then $T(S+dS)$. Since the temperature is not a linear function of entropy, as can be seen on Fig. 4, the spin temperature does not in- crease linearly with time when the system is heated at a constant rate. In particular, at a first-order transition, with a discontinuous jump in entropy, the temperature remains constant for a while during the influx of the la- tent heat. In general, the increase in temperature $\Delta T$ in a time interval $\Delta t$ is
$$\Delta T=T(S+\Delta S)-T(S), \tag{8}$$
where the entropy decrease is obtained from the relation
$$\int_{S}^{S+\Delta S} T\left(S^{\prime}\right) d S^{\prime}=\int_{0}^{\Delta t}\left\lfloor\frac{d Q}{d t}\right\rfloor d t. \tag{9}$$

Heating with a constant heat exchange rate $dQ/dt$ corre- sponds to increasing the temperature such that the area under the $T(S)$ curve increases at constant rate.

To simulate the experimental situation we first quench the system rapidly to the ordered state at a given $(T_{0},H_{0})$ and then let the system attempt to find the equilibrium state at the temperature $T_{0}$ during a time interval $\Delta t_{eq}$ by performing a number of Monte Carlo steps. After this time interval, global equilibrium is usually not attained. We then start heating the system at a constant rate by as- signing a higher temperature after every elapse of a time interval $\Delta t$. For simulating a fast heating rate we use $\Delta t=200$ MCS with $\Delta t_{eq}=200$ MCS and for a slow rate we use $\Delta t=300$ MCS with $\Delta t_{eq}=1800$ MCS. In the fast process the time intervals are not sufficient for the system to reach equilibrium. In the slow process the system is closer to local equilibrium at all times. Figure 9 shows the results of the simulated heating process at constant rate for $H_{0}=0$ and $H_{0}=8J$, crossing the second- and first-order boundaries, respectively. At the top is shown the nonlinear increase in temperature, obtained from Fig.4, corresponding to the same constant heat rate, the bold step indicates the transition temperature.

Let us now follow the development of the magnetic or- der by calculating the magnetic structure factor $S(\mathbf{k})$, which can be measured by neutron scattering. In Fig. 9 we show the intensity $I=\int S(\mathbf{k}) d \mathbf{k}$ and suitable powers, $s_{1}^{-1}$ and $s_{2}^{-1/2}$, of the moments $s_{n}=\int S(\mathbf{k})|k|^{n} d \mathbf{k}/I$. These powers, which are related to the width of $S(\mathbf{k})$, have dimensions of length and measure the average size of the ordered domains. The results from crossing the second-order line for $H=0$ are shown to the left. At the bottom is shown the slow heating process. The width $s_{1}^{-1}$ is almost constant up to $T_{N}$ and then increases when the long-range order is replaced by short-range order. The intensity decreases towards $T_{N}$ following the de- crease of the order parameter $M_{\perp}$. In the first process, shown above, the long-range order is not fully developed at $t=0$ and the width now clearly decreases with $T$ in- creasing towards $T_{N}$ showing that the domains are grow- ing more rapidly at higher temperature. The long-range order (intensity) is initially much smaller than in the pre- vious, slow case and increases with increasing tempera- ture because the domains grow, in spite of the decreasing average magnetization. A similar effect is in fact seen ex- perimentally in the neutron scattering experiments forCu. $^{2}$

The results of the same heating simulation across a

![](./images/812667434606526465_9.jpg)

FIG. 9. Results of simulation of heating at constant rate across a second-order line $(H=0)$ (left), and a first-order line $(H=8J)$ (right). The temperature increase as a function of time t in units of Monte Carlo steps per site is calculated from the en- tropy, Fig. 4. (○) indicates the intensity of the structure factor, and $(\square)$ and $(\nabla)$ indicate the powers $s_{1}^{-1}$ and $s_{2}^{-1/2}$ of the two first moments of the structure factor, respectively. In the fast heating process the system is allowed to equilibrate after the quench only for a short time interval $\Delta t_{eq}=200$ MCS, it is then heated by a heat pulse at every $\Delta t=200$ MCS. In the slow pro cess $\Delta t_{eq}=1800$ MCS and the heat pulse is induced at every $\Delta t=300$ MCS. The data are averaged over x and y domains and are for the fast runs further averaged over two different runs. The slow run represents a single, but reproducible and typical event.

first-order boundary at $H_{0}=8J$ are shown to the right. The effects are quite similar and there is no dramatic difference between the second- and first-order transition. This is, of course, due to the very small latent heat displayed by our model. There may be a weak qualitative difference in the fact that the peak intensity is somewhat higher at the first-order transition temperature, indicating the sharp drop in the staggered magnetization (see Fig. 2). The conclusion is, however, that the heating measurements may not be reliable for determining the nature of the transition. The above results are rather specific for the model studied since $T(S)$ is not universal. In cases with larger latent heat we thus expect a more drastic difference between the heating through the first-order and second-order transitions.

## VI. DISCUSSION

Using a simple two-dimensional dipole model system we have studied a number of questions of relevance for the understanding of nuclear magnetism and adiabatic demagnetization, for example, in Cu. Although the real system, Cu, is much more complicated we expect the following features found in the model to be general applicability. The mean-field phase diagram is strongly renormalized in temperature., i.e., $T_{N} \ll T_{N}^{\mathrm{MF}}$, but the isentropes calculated by means of mean-field theory are much less renormalized for $T \leq T_{N}^{\mathrm{MF}}$. The reason is that the entropy depends on the energy fluctuations which are mainly influenced only by the short-range nature of the magnetic ordering and, therefore, insensitive to the long-range order being replaced by short-range order. Details in the isentropes will, of course, be influenced by the true phase transition boundary since the heat capacity $C_{H}=dS/dT$ is weakly divergent.

It is difficult to judge whether the classical domain-growth behavior found for the simple model is representative for Cu, which in the mean-field theory has an infinite number of domains. It is, in fact, a question whether true long-range order can actually be reached in Cu. In quenches we have found that the domain-wall entropy is small and, therefore, the thermodynamic force driving the system towards equilibrium is small. Hence, we expect that the time scale needed to reach a one-domain equilibrium state in a system like Cu to be much longer than the spin-spin relaxation time $\tau_{ss}$. If this time scale approaches $\tau_{sl}$ this system will heat up before it can reach equilibrium. A study of the time dependence of the intensity and the width of the scattering factor $S(\mathbf{k})$ may shed light on this question. The qualitative behavior found in the heating simulations indicates an initial domain growth during heating in the ordered phase causing even an increase of the intensity. This phenomenon is of a simple physical origin and can, therefore, also be expected to occur in a system like Cu.

The constraint of constant entropy imposed on the ordering process in nuclear spin systems opens up for some new aspects of nucleation, growth and annealing processes which are fundamentally different from those usually encountered in materials science. Specifically, when the magnetic system is crossing the phase boundary along an isentrope, the early-time nucleation of the ordered antiferromagnetic phase and the subsequent growth of the ordered domains need not lead to an homogeneous equilibrium single-domain structure. Rather, it is likely to lead to a heterogeneous multidomain structure, where the entropy of the domain walls and the domain-wall network topology is compensated by a degree of antiferromagnetic ordering within the domains which is higher than in the corresponding single-domain structure with the same total entropy. The multidomain structure is also an equilibrium state of the system with the same free energy and entropy as the single-domain structure, but with a different temperature. It will not anneal in time as long as there is no heat exchange with the environment. This may provide an additional source for the experimental observation in Cu (Ref. 2) of a low scattering intensity immediately after the adiabatic demagnetization and then a rise in intensity as time lapses and thermal energy can be exchanged with the environment.

Finally, we wish to remark that the simple model studied in this paper has by itself an interesting phase diagram with both first-order and continuous transitions. The first-order transition is at low-temperature endothermic and the first-order phase boundary has a maximum at $T\neq 0$ at a point where there is no latent heat associated with the transition.

## ACKNOWLEDGMENTS

It is a pleasure to thank K. Binder for a stimulating conversation and B. Andresen for useful discussions on annealing. We also thank O. U. Lounasmaa and A. J. Oja for comments. H.E.V. is grateful for the warm hospitality of Riso National Laboratory. The work of O.G.M. is supported by the Danish Natural Science Research Council under Grant No. 5.21.99.72, and the work of H.E.V. by the Academy of Finland.

$^{1}$M. T. Huiku, T. A. Jyrkkiö, J. M. Kyynäräinen, M. T. Loponen, O. V. Lounasmaa, and A. S. Oja, J. Low. Temp. Phys. 62, 433 (1986); A. S. Oja, Phys. Scr. T19, 462 (1987).
$^{2}$T. A. Jyrkkiö, M. T. Huiko, O. V. Lounasmaa, K. Siemensmeyer, K. Kakurai, M. Steiner, K. N. Clausen, and J. K. Kjems, Phys. Rev. Lett. 60, 2418 (1988).
$^{3}$P.-A. Lindgård, X-W. Wang and B. N. Harmon, J. Magn. Magn. Mater. 54-57, 1052 (1986); M. A. Ruderman and C. Kittel, Phys. Rev. 96, 99 (1954).
$^{4}$P. Kumar, J. Kurkijärvi, and A. S. Oja, Phys. Rev. B 31, 3194 (1985).
$^{5}$P.-A. Lindgård, Phys. Rev. Lett. 61, 629 (1988); H. E. Viertiö and A. S. Oja, Phys. Rev. 36, 3805 (1987).
$^{6}$J. V. José, L. P. Kanaoff, S. Kirkpatrick, and D. F. Nelson, Phys. Rev. B 16, 1217 (1977).
$^{7}$O. G. Mouritsen, *Computer Studies of Phase Transitions and Critical Phenomena* (Springer, Heidelberg, 1984).
$^{8}$S. A. Allen and J. W. Cahn, Acta Metall. 27, 1085 (1979).

$^9$J. D. Gunton, in *Time-Dependent Effects in Disordered Materi- als*, edited by R. Pynn (Plenum, New York, 1987).

$^{10}$A. Sadiq and K. Binder, J. Stat. Phys. **35**, 517 (1984).

$^{11}$A. Milchev, K. Binder, and D. W. Heermann, Z. Phys. B **63**, 521 (1986).

$^{12}$I. M. Lifshitz, Zh. Eksp. Teor. Fiz. **42**, 1354 (1962) [Sov. Phys.—JETP **15**, 939 (1962)].

$^{13}$O. G. Mouritsen and E. Praestgaard, Phys. Rev. B **38**, 2703 (1988).

$^{14}$H. C. Fogedby and O. G. Mouritsen, Phys. Rev. B **37**, 5962 (1988).