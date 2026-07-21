![](./images/812446899423412225_1.jpg)

# Effect of intra-atomic Coulomb repulsion on charge transfer in atom scattering on metal surfaces

B. Hellsing
Institute of Theoretical Physics, Chalmers University of Technology, S-412 96 Göteborg, Sweden

and

V.P. Zhdanov
Institute of Catalysis, Novosibirsk 630090, Russia

Received 2 January 1992; accepted for publication 21 April 1992

Charge transfer in atom scattering on metal surfaces is usually described employing the time-dependent Anderson model. In the framework of this model, the electron hopping matrix element is assumed independent of the intra-atomic Coulomb repulsion and the occupation numbers of the adatom orbital. In the present paper, the latter assumption is relaxed. The occupation number dependence of the hopping matrix element is shown to describe the possibility of the formation of neutral, positive and negative ions in a single approach. The connection between the exact quantum mechanical result and the phenomenological master equation approach is outlined. The latter is shown to be valid for typical atom velocities, $v=0.005-0.001$ au, and is most efficient for numerical calculations. Calculated results are used to analyze experimental data for the scattering of alkali atoms on metal surfaces.

## 1. Introduction

The study of charge transfer processes between atoms or molecules and a metal surface is of fundamental interest, both from a theoretical and practical point of view [1]. For energies up to 5-10 keV, charge transfer occurs via resonance tunneling or Auger recombination. In the present paper, we are concerned with the former process, i.e., resonance tunneling of electrons between an adsorbate orbital and the conduction band of a metal surface. This process is conventionally described in the framework of the time-dependent Anderson model [1]. The model Hamiltonian is given by

$$
H(t)=H_{0}(t)+V(t)+H_{1}(t), \tag{1}
$$

with

$$
H_{0}(t)=\sum_{k, \sigma} \epsilon_{k} c_{k, \sigma}^{\dagger} c_{k, \sigma}+\sum_{\sigma} \epsilon_{\mathrm{a}}(t) c_{\mathrm{a}, \sigma}^{\dagger} c_{\mathrm{a}, \sigma}, \tag{2}
$$

$$
V(t)=\sum_{k, \sigma}\left[V_{k}(t) c_{\mathrm{a}, \sigma}^{\dagger} c_{k, \sigma}+\text { H.C. }\right], \tag{3}
$$

$$
H_{1}(t)=U(t) n_{\mathrm{a}, \sigma} n_{\mathrm{a},-\sigma}, \tag{4}
$$

where $n_{\mathrm{a}, \sigma}=c_{\mathrm{a}, \sigma}^{\dagger} c_{\mathrm{a}, \sigma}$. The first and second terms in eq. (2) describe the solid and a single non-degenerate adsorbate level in a one-electron approximation. $V_{k}(t)$ in eq. (3) takes into account the mixing of the substrate orbitals and the adsorbate orbital. The $U$ term in eq. (4) originates from the mutual Coulomb repulsion between the two electrons in the adsorbate level. The parameters of the Hamiltonian are time-dependent owing to the motion of the adatom.

If one neglects the intra-atomic Coulomb interaction, the charge-exchange problem can be solved analytically in the wide-band limit [2,3]. This approach has been quite successful in explaining experimental data [1]. However, the one-electron picture has limitations as discussed by Brako et al. [1], and it is of interest to analyze how the two-electron term in eq. (4) will influence the charge transfer between the metal substrate and the adsorbate atom. This problem has been considered in refs. [4-7].

Grimley et al. [4] and Yoshimori et al. [5] have employed the Hartree-Fock approximation in order to take into account the intra-atomic Coulomb interaction. Kasai et al. [6] have investigated the problem by deriving an infinite set of equations for the destruction and creation operators which are, by means of an approximation, cut to a finite number. In ref. [7], Brako and Newns have developed an approach based on an expansion into states with small number of electron-hole pairs and on prohibition of double occupation of the adsorbate orbital, i.e., $U=\infty$.

Analyzing the effect of the finite intra-atomic Coulomb repulsion on the charge transfer process, all authors [4-6] assumed that the electron hopping matrix elements, $V_{k}$, are independent of occupation numbers of the adsorbate orbitals with spin index $\sigma$ and $-\sigma$, respectively. This assumption is customary in the theory of chemisorption [8], and is also employed to study vibrational relaxation of adsorbates due to excitation of electron-hole pairs [9]. In these cases, this approach is reasonable, as the distance between the adsorbate and the surface does not change significantly.

In a scattering experiment, charge transfer often occurs at distances far from the surface. In addition, formation of neutrals or charged particles may take place at different distances. In this case, the assumption that the matrix elements $V_{k}$ are spin independent, may be incorrect. The aim of the present study is to explore the effect of including a spin dependence of the hopping matrix elements in the Anderson model. In particular, we have investigated the influence on the charge transfer in atom scattering from metal surfaces.

### 2. Hopping matrix element and interaction

The asymptotic behavior of the electron hopping matrix element at large adsorbate-surface distances, $z \gg 1$ (in atomic units, which will be used from now on), can be estimated by [10]
$$V^{2} \sim \exp (-2 \gamma z),\qquad(5)$$
where $\gamma=\sqrt{2|E|}$ with $E$ denoting the electron binding energy. In the Hartree-Fock approximation, the electron binding energy is defined by
$$\left|E_{\mathrm{a}, \sigma}\right|=\left|\epsilon_{\mathrm{a}}+U\left\langle n_{\mathrm{a},-\sigma}\right\rangle\right|,\qquad(6)$$
where $\langle n_{\mathrm{a},-\sigma}\rangle$ is the expectation value of the occupation number of the adsorbate orbital with spin $-\sigma$. Thus we have
$$V_{k, \sigma}^{2}(z)=V_{k}^{2}(0) \exp \left(-2 \gamma_{\sigma} z\right),\qquad(7)$$
where
$$\gamma_{\sigma}=\sqrt{2\left|\epsilon_{\mathrm{a}}+U\left\langle n_{\mathrm{a},-\sigma}\right\rangle\right|}.\qquad(8)$$

Eqs. (7) and (8), describe the effect of the occupation numbers of the adsorbate orbitals $\langle n_{\mathrm{a}, \sigma}\rangle$ and $\langle n_{\mathrm{a},-\sigma}\rangle$, on the hopping matrix elements. This effect originates from the spin dependence of the electron binding energies. There is another phenomenon which will introduce an additional dependence of the hopping matrix elements on the occupation numbers. This concerns the time dependence of the electron density in the surface region of the metal (delocalization of the image charge). A change in the surface electron density should in turn lead to a change in the hopping matrix elements. However, this effect is expected to be weak, compared to that described by eqs. (7) and (8). In the latter case the hopping matrix elements will simply be determined by the probability for tunneling through a rectangular barrier, when the Coulomb interactions with the core and the image electron can be neglected. The effect of these Coulomb interactions on the hopping matrix elements can be estimated, using the expansion approach proposed in ref. [11],
$$V_{k, \sigma}^{2}(z) \sim z^{\left(4 Q+1 / 2 \gamma_{\sigma}\right)-1} \exp \left(-2 \gamma_{\sigma} z\right),\qquad(9)$$

where $Q=Q_{0}-\langle n_{-\sigma}\rangle$, and $Q_{0}$ is the core charge.

For hydrogen and alkali atoms $Q_{0}=1$, and if in addition one neglects the $\langle n_{-\sigma}\rangle$ term (this corresponds to the one-electron approximation), eq. (8) yields the same result as that obtained in ref. [11] (see also the discussion in ref. [3]). In principle, the pre-exponential factor in eq. (9) is not negligible. However, in our calculation we set this this to unity for two reasons: (i) this factor is less important than the exponential one, and (ii) reliable calculations of the pre-exponential fac- tors $V_{k}^{2}(0)$ in eq. (7) are not available at present.

For the electron energies $E_{\mathrm{a}, \sigma}$ in eq. (6), we take into account the image interaction,
$$
\epsilon_{\mathrm{a}}=-I+\frac{1}{4\left(z+z_{0}\right)} \quad(10)
$$
and
$$
U=I-A-\frac{1}{2\left(z+z_{0}\right)}, \quad(11)
$$
where $I$ and $A$ are the free atom ionization potential and electron affinity, respectively, and $z_{0} \simeq 3$ au is a parameter that reduces the image interaction at small distances [4].

## 3. Equations of motion

If we want to include the intra-atomic Coulomb repulsion into the model, the time-dependent problem has no exact solution. However, if we employ the Hartree-Fock approximation, the equations of motion can be integrated by analogy with the case of $U=0$ or $U=\infty$ [1]. In particular, the time dependence of the occupation number of the adsorbate orbital with spin $\sigma$ is in the wide-band limit described by
$$
\begin{aligned}
\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle= & \left\langle n_{\mathrm{a}, \sigma}(-\infty)\right\rangle \exp \left[-2 \int_{-\infty}^{t} \Delta_{\sigma}\left(t^{\prime}\right) \mathrm{d} t^{\prime}\right] \\
& +\pi^{-1} \int_{-\infty}^{\infty} f(\epsilon, T) I(\epsilon, t) \mathrm{d} \epsilon, \quad(12)
\end{aligned}
$$
with
$$
\begin{aligned}
I(\epsilon, t)= & \left|\int_{-\infty}^{t} \sqrt{\Delta_{\sigma}\left(t^{\prime}\right)} \exp \left\{-\mathrm{i} \epsilon t^{\prime}\right.\right. \\
& \left.\left.-\int_{t^{\prime}}^{t}\left[\mathrm{i} E_{\mathrm{a}, \sigma}\left(t^{\prime \prime}\right)+\Delta_{\sigma}\left(t^{\prime \prime}\right)\right] \mathrm{d} t^{\prime \prime}\right\} \mathrm{d} t^{\prime}\right|^{2},
\end{aligned}
$$
where $f(\epsilon, T)=\left(1+\exp \left[\left(\epsilon-E_{\mathrm{F}}\right) / T\right]\right)^{-1}$ is the Fermi distribution function, and
$$
\Delta_{\sigma}(t)=\Delta_{0} \exp \left[-2 \gamma_{\sigma} z(t)\right]. \quad(14)
$$

The parameter $\Delta_{0}$ in the latter equation is defined by
$$
\Delta_{0}=\pi \sum_{k} V_{k}^{2}(0) \delta\left(E_{\mathrm{F}}-\epsilon_{k}\right). \quad(15)
$$

The quantities $E_{\mathrm{a}, \sigma}$ and $\Delta_{\sigma}$ are dependent on $\langle n_{\mathrm{a},-\sigma}(t)\rangle$ (see eqs. (6) and (14)). Thus, the occupation numbers $\langle n_{\mathrm{a}, \sigma}(t)\rangle$ and $\langle n_{\mathrm{a},-\sigma}(t)\rangle$ are interdependent and the equations for these variables must be solved self-consistently. Unfortunately, this procedure is rather difficult and tedious, and in practical calculations it is reasonable to start with the semi-classical master equations [1,12]
$$
\frac{\mathrm{d}\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle}{\mathrm{d} t}=2 \Delta_{\sigma}\left[N_{\mathrm{a}, \sigma}(z(t))-\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle\right]
$$
and
$$
\begin{aligned}
& \frac{\mathrm{d}\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle}{\mathrm{d} t} \\
& \quad=2 \Delta_{-\sigma}\left[N_{\mathrm{a},-\sigma}(z(t))-\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle\right], \quad(17)
\end{aligned}
$$
where $N_{\mathrm{a}, \sigma}(z(t))$ is the equilibrium occupation number at a distance $z(t)$.

To complete the specification of general equations, we should also note that the expectation values for producing positive, neutral and negative particles are, respectively,
$$
P_{+}(t)=\left[1-\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle\right]\left[1-\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle\right], \quad(18)
$$
$$
\begin{aligned}
P_{0}(t)= & \left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle\left[1-\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle\right] \\
& +\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle\left[1-\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle\right]
\end{aligned}
$$

and
$$
P_{-}(t)=\left\langle n_{\mathrm{a}, \sigma}(t)\right\rangle\left\langle n_{\mathrm{a},-\sigma}(t)\right\rangle. \tag{20}
$$

Finally, it is reasonable to discuss briefly the applicability of the semi-classical master equations. For this purpose, we differentiate eq. (12) with respect to time (omitting the spin index $\sigma$)
$$
\begin{aligned}
\frac{\mathrm{d}\left\langle n_{\mathrm{a}}(t)\right\rangle}{\mathrm{d} t}= & -2 \Delta\left\langle n_{\mathrm{a}}(t)\right\rangle \\
& +\pi^{-1} \int_{-\infty}^{\infty} f(\epsilon, T) J(\epsilon, t) \mathrm{d} \epsilon, \quad(21)
\end{aligned}
$$
where
$$
\begin{aligned}
J(\epsilon, t)= & 2 \sqrt{\Delta(t)} \int_{-\infty}^{t} \sqrt{\Delta\left(t^{\prime}\right)} \exp \left[-\int_{t^{\prime}}^{t} \Delta\left(t^{\prime \prime}\right) \mathrm{d} t^{\prime \prime}\right] \\
& \times \cos \left[\epsilon\left(t^{\prime}-t\right)+\int_{t^{\prime}}^{t} E_{\mathrm{a}}\left(t^{\prime \prime}\right) \mathrm{d} t^{\prime \prime}\right] \mathrm{d} t^{\prime}.
\end{aligned}
$$

Assuming that $\Delta$ and $E_{\mathrm{a}}$ in eq. (22) are time-independent, one can easily integrate eq. (22) and show that in this limit eq. (21) is equivalent to eq. (16). The time scale characterizing the convergence of the integral in eq. (22) is $\delta t \simeq 1 / \Delta$. The assumption that both $\Delta$ and $E_{\mathrm{a}}$ are constant over the interval $\delta t$ is correct if $|\delta \Delta|<\Delta$ and $\left|\delta E_{\mathrm{a}}\right|$ $<\Delta$, which is equivalent to
$$
v<\Delta / 2 \gamma \tag{23}
$$
and
$$
v<2 \Delta^{2} /\left|\frac{\mathrm{d} E_{\mathrm{a}}}{\mathrm{d} z}\right|, \tag{24}
$$
where $v$ is the velocity of the particle.

The condition $v=\Delta\left(z^{*}\right) / 2 \gamma$ defines the so-called "freezing distance" $z^{*}[1,12]$. As a rule, the charge transfer takes place at distances $z \leq$ $z^{*}$, where condition (23) is fulfilled. We have verified that in our calculations (scattering of alkali atoms) presented below, the second condition given by eq. (24) is also fulfilled. Thus, we do not expect any serious difference between the results obtained by the quantum mechanical or the semi-classical approaches. This expectation is in agreement with the results of analytical and numerical studies of $\mathrm{H}^{-}$formation in scattering on W [12,13]. According to refs. [12,13], the one-electron semi-classical master equation reproduces very accurately the corresponding quantum mechanical results in the velocity regime $v=$ $0.01-0.1$ au $(1$ au $=2.9 \times 10^{8} \mathrm{~cm} / \mathrm{s})$.

It is relevant to recall the well-known formula of the Landau-Zener type [1],
$$
\left\langle n_{\mathrm{a}}(\infty)\right\rangle=\exp \left[-\Delta\left(z_{\mathrm{c}}\right) / \gamma v\right], \tag{25}
$$
where $z_{\mathrm{c}}$ is the crossing point $\left(E_{\mathrm{a}}=E_{\mathrm{F}}\right)$. Eq. (25) can be derived from the quantum mechanical result in eq. (12). If the stationary phase approximation is applied on the expression in eq. (22), the stationary phase region in time is given by $\delta t \simeq \sqrt{\pi /\left|\mathrm{d} E_{\mathrm{a}} / \mathrm{d} t\right|}$ [12]. In this case, the requirement that $|\delta \Delta|<\Delta$ and $\left|\delta E_{\mathrm{a}}\right|<\Delta$ holds over the interval $\delta t$ yields the following conditions
$$
v<\left|\frac{\mathrm{d} E_{\mathrm{a}}}{\mathrm{d} z}\right| / 4 \gamma^{2} \tag{26}
$$
and
$$
v>4 \Delta^{2} /\left|\frac{\mathrm{d} E_{\mathrm{a}}}{\mathrm{d} z}\right|. \tag{27}
$$

If we then integrate eq. (22), eq. (21) yields the master equation in eq. (16) with the equilibrium occupation numbers $N_{\mathrm{a}}$ replaced by the Fermi distribution function, $f\left(E_{\mathrm{a}}, T\right)$. In the low temperature limit, $T \rightarrow 0$, this master equation is easily solved and eq. (25) is the result. Note that the conditions of eqs. (24) and (27) are opposite. In reality, the condition (27) is often violated in experiments. For the velocities in the regime $v=$ $0.01-0.1$ au, condition (27) requires an unrealistic rapid change of the adsorbate energy level $E_{\mathrm{a}}(z)$ with distance to the surface. Thus, the semi-classical equations, eqs. (16) and (17), are more appropriate compared to eq. (25), in order to explain typical experimental data.

## 4. Results of calculations

In this section, we present results of simulations demonstrating the consequences of the dependence of the hopping matrix elements on the occupation numbers. To reveal this effect, it is instructive to perform the calculations for three different expressions of the parameter $\gamma$. The

first expression, $\gamma_{\sigma}$, is defined by eq. (8). The second, $\gamma_{0}$, by assuming $\langle n_{\mathrm{a},-\sigma}\rangle=0$ in eq. (8), i.e.,
$$
\gamma_{0}=\sqrt{2\left|\epsilon_{\mathrm{a}}\right|}. \quad(28)
$$

The third one, $\gamma_{1}$, is defined by putting $\langle n_{\mathrm{a},-\sigma}\rangle=$ 1 in eq. (8), i.e.,
$$
\gamma_{1}=\sqrt{2\left|\epsilon_{\mathrm{a}}+U\right|}. \quad(29)
$$

The parameter $\gamma=\gamma_{0}$ is expected to be an appropriate approximation when describing formation of positive ions, as we then assume that the probability is low for the second electron (with spin $-\sigma$) to be found on the scattered atom. On the other hand, $\gamma=\gamma_{1}$ is more appropriate when simulating formation of negative ions, as the state with spin $-\sigma$ is assumed to be completely occupied in this case.

When $\gamma_{\sigma}$ is replaced by the approximation $\gamma_{0}$ $(\gamma_{1})$ in our simulations, we do not assume $\langle n_{\mathrm{a},-\sigma}\rangle$ $=0\left(\langle n_{\mathrm{a},-\sigma}\rangle=1\right)$ in the equations used to calculate the equilibrium occupation numbers, i.e., we solve the two-electron problem in all cases.

In the literature, the charge transfer is often described in the framework of the one-electron approximation. For example, formation of positive ions is calculated assuming $\langle n_{\mathrm{a},-\sigma}\rangle=0$, not only in eq. (8), but also in the equation for $N_{\mathrm{a}, \sigma}$ (this one-electron approach corresponds to $U=$ $\infty$). On the other hand, formation of negative ions is often simulated by assuming $\langle n_{\mathrm{a},-\sigma}\rangle=1$ in the equation for $N_{\mathrm{a}, \sigma}$. Our two-electron approach with $\gamma=\gamma_{0}$ and $\gamma=\gamma_{1}$ yields the results which are close to the corresponding one-electron results.

Let us now consider scattering of $\mathrm{Na}$ atoms from metal surfaces, e.g., from W. In this case $I=5.14 \mathrm{eV}$ and $A=0.55 \mathrm{eV}$. The work function of the clean surface is $\phi=5.2 \mathrm{eV}$. Thus, at infinite separation the level $\epsilon_{\mathrm{a}}$ is found slightly above the Fermi level, and in the quasi-adiabatic regime, the $\mathrm{Na}^{+}$ions should be the dominant species in the scattering. However, if the substrate work function is reduced considerably (e.g., due to alkali deposition on the surface), $\mathrm{Na}^{-}$ions may be formed with finite probability. The transition from the formation of positive ions to the formation of negative ions, with decreasing work function, is most interesting. In this case the occupation numbers $\langle n_{\mathrm{a}, \sigma}\rangle$ and $\langle n_{\mathrm{a},-\sigma}\rangle$ are not too low and the effect of these numbers on the matrix elements $V_{k, \sigma}$ may be significant (see eqs. (7) and (8)).

Employing eqs. (16)-(20), with $\Delta_{0}=5 \mathrm{eV}$ in eq. (14), we have calculated, in the wide-band limit, the asymptotic probability $(t \rightarrow+\infty)$ for formation of negative, neutral and positive ions, considering the neutral state as the initial state $(t \rightarrow-\infty)$. Note that for the velocities we will consider, the scattered atom loses almost all memory of the initial state, i.e, the final state is formed primarily on the outgoing trajectory (see figs. 2 and 3). Thus the results will essentially be independent of whether the incident particle is an ion $+/-$ or a neutral. We use the trajectory approximation, defined by
$$
z(t)=\left\{\begin{array}{rl}
-v t & \text { if } t<0, \\
v t & \text { if } t>0.
\end{array} \quad\right. \text { (30) }
$$

The atomic velocity is assumed to be in the range $v=0.01-0.1$ au. For the $\mathrm{Na}$ atom these velocities correspond to kinetic energies $50 \mathrm{eV}-5 \mathrm{keV}$. In this case the trajectory approximation is reasonable and the conditions of eqs. (23) and (24) are usually fulfilled. Note also that at these velocities the scattered atom loses almost all memory of the initial state, i.e., the final state is formed primarily on the outgoing trajectory.

Fig. 1 shows the adiabatic $(v=0)$ two-electron Hartree-Fock energies $E_{\mathrm{a}, \sigma}$ (see eq. (12)) and the adiabatic energies $\epsilon_{\mathrm{a}}$ and $\epsilon_{\mathrm{a}}+U$ (the latter energies correspond to the one-electron picture with $\langle n_{\mathrm{a},-\sigma}\rangle=0$ and 1, respectively) as a function of distance from the turning point of the $\mathrm{Na}$ atom trajectory for $\phi=4 \mathrm{eV}$. The two-electron energies are seen to be considerably different compared to the one-electron energies at $z \leq 5$ au. Thus, the one-electron approximation with energies $\epsilon_{\mathrm{a}}$ or $\epsilon_{\mathrm{a}}+U$ yields the correct asymptotic occupation numbers only provided that the final state of the scattered atom is formed at distances $z \geq 5$ au.

Figs. 2 and 3 exhibit the typical distance dependence of the occupation numbers for the velocity $v=0.01$ and 0.1 au. In the former case (fig.

![](./images/812446899423412225_2.jpg)

Fig. 1. Adiabatic Hartree-Fock energies $E_{\mathrm{a}, \sigma}=\epsilon_{\mathrm{a}}+U\left\langle n_{\mathrm{a},-\sigma}\right\rangle$ (solid lines) and energies $\epsilon_{\mathrm{a}}$ and $\epsilon_{\mathrm{a}}+U$ (lower and upper dashed lines) as a function of adsorbate-surface distance $z$ for Na, $U$ is given by eq. (11) with $I=5.14$ eV and $A=0.55$ eV. The metal work function is $\phi=4$ eV and $\Delta_{0}=5$ eV (see eq. (14)).

![](./images/812446899423412225_3.jpg)

Fig. 2. Occupation numbers $n_{\mathrm{a}, \sigma}$ and $n_{\mathrm{a},-\sigma}$ (solid lines) as a function of adsorbate-surface distance $z$ from the turning point of the Na atom trajectory for a velocity $v=0.01$ au and with a work function $\phi=4$ eV. The dashed lines show the equilibrium occupation numbers $N_{\mathrm{a}, \sigma}$ and $N_{\mathrm{a},-\sigma}$.

![](./images/812446899423412225_4.jpg)

Fig. 3. The same as in fig. 2 for $v=0.1$ au.

2 with $v=0.01$ au), the occupation numbers are very close to the equilibrium values in the region $z<3.5$ au, while the non-adiabatic effects take place at $z>3.5$ au. For the higher velocity, $v=0.1$ au, the non-adiabatic effects are rather strong even near the surface. It is clear that in this case equilibrium is even not obtained at the turning point (see the lower part of fig. 3). This means that the final asymptotic occupancies will depend on the initial asymptotic occupancies. However, $v=0.1$ au $(=2.9 \times 10^{7} \mathrm{~cm} / \mathrm{s})$ exceeds the typical experimental velocities we will consider.

Figs. 4 and 5 show the work function dependence of the probabilities for formation of $\mathrm{Na}^{+}$, $\mathrm{Na}$ and $\mathrm{Na}^{-}$for the velocities $v=0.1$ and 0.01 au, respectively. The width of the transition regions, in terms of $\phi$, for different charge states are seen to increase with increasing velocity. As expected, the results obtained with $\gamma_{\sigma}$ (eq. (8)) and $\gamma_{0}$ (eq. (28)) are almost the same, considering the formation of positive ions. On the other hand, employing the parameter $\gamma_{0}$ for the description of formation of negative ions leads to a considerable overestimation of the probability $P_{-}$in the region $1.5<\phi<4.5$ eV. This effect is more pronounced for $v=0.01$ au (fig. 5). For the results

obtained with $\gamma_{\sigma}$ and $\gamma_{1}$ (eq. (29)), the agreement is good when comparing the probabilities of formation of negative ions, while the probabilities for the formation of positive ions are underestimated.

The calculated probability $P_{+}$, obtained with the use of $\gamma_{\sigma}$ and $\gamma_{0}$, shows that with the latter choice, $P_{+}$ is underestimated. This is essentially a non-adiabatic effect. Comparing the results displayed in the upper panels of figs. 4 and 5, this discrepancy will increase with the velocity. The main reason is that $\gamma_{0} \leq \gamma_{\sigma}$ or $\Delta_{0} \geq \Delta_{\sigma}$, which means that $\gamma_{0}$ refers to the short tunneling time. If we consider the particle having a finite velocity on the outgoing trajectory, the initially $(t=-\infty)$ occupied level crosses the Fermi level trying to regain its electron. The choice $\gamma_{\sigma}$, referring to the long tunneling time, will then yield the great-

![](./images/812446899423412225_5.jpg)

Fig. 4. Probabilities of formation of $\mathrm{Na}^{-}, \mathrm{Na}$ and $\mathrm{Na}^{+}$versus work function. The atomic velocity is $v=0.01$ au. The results obtained with $\gamma=\gamma_{\sigma}$ (solid lines) and $\gamma=\gamma_{0}$ (dashed lines) are compared in the upper panel. The bottom panel shows the corresponding comparison for $\gamma=\gamma_{\sigma}$ (solid lines) and $\gamma=\gamma_{1}$ (dashed lines).

![](./images/812446899423412225_6.jpg)

Fig. 5. The same as in fig. 4 for $v=0.1$ au.

est survival probability for the positive ionic state. The greater the velocity, the less time for the system to equilibrate and the larger the difference between the results for $P_{+}$. In the limit when the work function approaches the asymptotic ionization potential, i.e., the crossing takes place at large particle surface distances $(\gamma_{0}=\gamma_{\sigma})$, $P_{+}$ is independent of the choice $\gamma_{0}$ or $\gamma_{\sigma}$, which is shown in the upper panels of figs. 4 and 5.

Fig. 6 displays a comparison between the results obtained with a one-electron and a two-electron master equation approach. This figure demonstrates that if the parameters in the oneelectron model are chosen correctly (i.e., $\gamma_{0}$ for the production of positive ions and $\gamma_{1}$ for negative ions), the results of this model are in good agreement with the ones from a two-electron approach.

In fig. 7 we compare experimental data on the formation probability of $\mathrm{K}^{+}$, when scattering potassium atoms on a $\mathrm{Cu}(110)$ surface partially covered by cesium [19], with calculated results. The values of the parameters $\Delta_{0}=5$ eV and

![](./images/812446899423412225_7.jpg)

Fig. 6. Probabilities of formation of $Na^{-}$ and $Na^{+}$ versus work function. The atomic velocity is $v=0.01$ au. Solid lines show the results obtained in the framework of the two-electron approach with $\gamma_{\sigma}$. The probability of formation of $Na^{-}$ (dashed line) has been calculated employing the one-electron approximation with $\gamma_{1}$ and $E_{\mathrm{a}}=\epsilon_{\mathrm{a}}+U$. The probability of formation of $Na^{+}$ (dashed line) has been obtained within the one-electron approximation with $\gamma_{0}$ and $E_{\mathrm{a}}=\epsilon_{\mathrm{a}}$.

![](./images/812446899423412225_8.jpg)

Fig. 7. Formation probability of $K^{+}$ in potassium scattering on a Cu(110) surface, partially covered by cesium, i.e., versus work function. The velocity of the incoming potassium atom is $v=0.0055$ au. Experimental data [19] (diamonds) are compared with results from calculations adopting, the two-electron approximation with $\gamma=\gamma_{\sigma}$ (solid line), the one-electron approximation with $\gamma=\gamma_{1}$ and $E_{\mathrm{a}}=\epsilon_{\mathrm{a}}$ (dashed line) and eq. (25) with $E_{\mathrm{a}}=\epsilon_{\mathrm{a}}$ (dashed-dotted line). The ionization potential and electron affinity for potassium are $I=4.3$ eV and $A=0.8$ eV, respectively.

![](./images/812446899423412225_9.jpg)

Fig. 8. Formation probability of $Na^{+}$ in sodium scattering on a W(110) surface, partially covered by sodium. Experimental data from ref. [15] (diamonds) and calculations with $\gamma=\gamma_{\sigma}$ for $v=0.01$ au and $\Delta_{0}=5$ eV (solid line) and $\Delta_{0}=20$ eV (dashed line).

$z_{0}=3$ au, were the same as in the case of Na. The comparison shows that the theoretical approaches employed, predict a too rapid increase in the scattered positive ion fraction with increasing work function. The agreement between our calculated results and the experimental data is improved compared to the results obtained with the simple expression in eq. (25). The expression in eq. (25) (with $E_{\mathrm{a}}=\epsilon_{\mathrm{a}}$ and the same $\Delta_{0}$ as in ref. [17]) predicts a considerably more rapid increase of the formation probability of $K^{+}$ with increasing work function. With our smaller value of $\Delta_{0}=5$ eV, we derive the same shape of the curve, but shifted 0.5 eV towards smaller $\phi$ values. Obviously, the theoretical model is lacking some ingredients, in particular for low cesium coverages (large work function). We will comment on this further below.

Formation of $Na^{+}$, Na and $Na^{-}$ during scattering on a tungsten surface was experimentally studied by Overbosch et al. [15,16]. The experimental data for $Na^{+}$ [15], shown in fig. 8, agrees reasonably with the results of our calculations. In this comparison, we also show that the calculations depends only weakly on the value of the parameter $\Delta_{0}$. When $\Delta_{0}=5$ eV is replaced by $\Delta_{0}=20$ eV, only a slight shift of $P^{+}$ versus $\phi$ is observed.

![](./images/812446899423412225_10.jpg)

Fig. 9. Formation probability of $Li^{+}$ in lithium atom scattering on a W(110) surface, partly covered by cesium. Experimental data from ref. [17] (diamonds) and calculated results with $\gamma=\gamma_{\sigma}$ and $v=0.0083$ au (solid line). The ionization potential and electron affinity for potassium are $I=5.4$ eV and $A=0.6$ eV, respectively.

The formation probabilities of $Na^{-}$, measured for $v \simeq 0.01$ au and $\phi=2-3$ eV, are rather small, e.g., $P^{-} \simeq 0.04$ and 0.025 for $\phi=2$ and 2.5 eV, respectively [16]. According to our calculations (fig. 4), the corresponding values are almost the same, $P^{-} \simeq 0.03$ and 0.018, if we use $\gamma_{\sigma}$ or $\gamma_{1}$. On the other hand, if we employ $\gamma_{0}$, we have $P^{-} \simeq$ 0.16 and 0.08, i.e., the theory of overestimates the formation probabilities of $Na^{-}$ (see fig. 4).

Scattering of Li atoms on a W(110) surface was studied by Geerlings et al. [17,18]. The results for the measured formation probability of $Li^{+}$ ions versus work function is shown in fig. 9. In our calculation, we chose $\Delta_{0}=5$ eV and $z_{0}=3$ au. The experimental data shows an almost linear dependence of the ion production versus work function. The interpretation is that the adsorbed cesium ions acts as independent neutralization centers [17].

Finally, we want to make some general comments on the comparison between our calculated results and the experimental data. In general the positive ion production versus work function still decreases too rapid compared to experiment. Analyzing the data in comparison with results from calculations based on a one-electron approach which yields the result given by eq. (25), Geerlings et al. [17] and Kimmel et al. [20] claim that the discrepancy is due to local electrostatic effects. The electrostatic field is set up by the adsorbed alkali atoms. For higher coverages the overlayer introduces a nonlocal adsorbate-induced work function, while for smaller coverages the adsorbed alkali atoms essentially acts as independent dipoles [17,20]. Consequently, the electrostatic effects should be most pronounced where the positive ion production starts to decrease (see figs. 7-9). It is obvious that when comparing our calculated results with experiments, it is in this region the discrepancy is largest. For smaller values of the work function, corresponding to higher coverages of adsorbed alkali atoms, the agreement is reasonable. Including the local electrostatic effects in a one-electron model calculation, both Geerlings et al. [17] and Kimmel et al. [20] obtained a considerable improved agreement with experiment.

## 5. Conclusions

In this paper we have proposed a scheme how to calculate the final charge state probabilities of a single adsorbate orbital scattered on a metal surface. Within the two-electron Hartree-Fock approximation, the fractions of ionic products + or - and neutrals are determined simultaneously. The basic ingredients that allow for the determination is an improved treatment of the electron hopping matrix element which in general is shown to depend on both the intra-atomic Coulomb repulsion and the spin occupation numbers. In the one-electron approximation, only a single fraction can be considered. In this case the occupancy of one of the spin states is assumed to be either one or zero, corresponding to the formation of negative or positive ions, respectively.

We also show that the conditions for applying the usual semi-classical master equations, eqs. (16) and (17), are in fact opposite compared to the well-known conditions for using the exponential formula (eq. (25)), which is often applied to fit experimental data. It is important to note that

in the velocity range of interest [$v = 0.01$-$0.1$ au $(2 \times 10^6$-$2 \times 10^7$ cm/s)], the semi-classical ap- proach is more appropriate. The alternative mas- ter equations, where the equilibrium occupancy in eqs. (16) and (17) is replaced by the Fermi distribution function, yields the exponential for- mula in eq. (25) at $T=0$ and is valid when conditions (26) and (27) are fulfilled. For the velocities of interest, the latter conditions corre- sponds to the case when the adsorbate energy level varies extremely rapid with respect to the distance to the surface. In general this is not the case.

Finally, we relate our model calculations to experiments. For alkali atoms scattered on met- als, the experimental data for the positive ion production demonstrates a considerable discrep- ancy with what is obtained from the simple theo- retical expression, eq. (25) (see fig. 7). The com- parison with experiment is improved with our two-electron approach. However, we believe that the local electrostatic effects, caused by the ad- sorbed alkali atoms (used to vary the work func- tion), are important to include in the modeling, as pointed out by Geerlings et al. [17] and Kim- mel et al. [20].

### Acknowledgements

The authors would like to thank Bengt Kasemo for valuable discussions and most valuable sug- gestions. We acknowledge support from the Swedish Natural Science Research Council (NFR). One of us (V.P.Zh.) also thanks the Royal Swedish Academy of Science for supporting his visit to Chalmers University of Technology.

### References

[1] R. Brako and D.M. Newns, Rep. Prog. Phys. 52 (1989) 655;
A.T. Amos, K.W. Sulston and S.G. Davison, Adv. Chem. Phys. 76 (1989) 335;
J. Los and J.J.C. Geerlings, Phys. Rep. 190 (1990) 133.

[2] A. Blandin, A. Nourtier and D.W. Hone, J. Phys. (Paris) 37 (1976) 369.

[3] R. Brako and D.M. Newns, Surf. Sci. 108 (1981) 253.

[4] T.B. Grimley, V.C. Jyothi Bhasu and K.L. Sebastian, Surf. Sci. 124 (1983) 305.

[5] A. Yoshimori, H. Kawai and K. Makoshi, J. Phys. Soc. Jpn. 53 (1984) 2441; Prog. Theor. Phys. Suppl. 80 (1984) 203; in: Dynamical Processes and Ordering on Solid Surfaces, Eds. A. Yoshimori and M. Tsukada (Springer, Berlin, 1985) p. 74.

[6] H. Kasai and A. Okiji, Surf. Sci. 183 (1987) 147;
H. Nakanishi, H. Kasai and A. Okiji, Surf. Sci. 197 (1988) 515.

[7] R. Brako and D.M. Newns, Solid State Commun. 55 (1985) 633.

[8] D.M. Newns, Phys. Rev. 178 (1969) 1123;
T.L. Einstein, J.A. Hertz and J.R. Schrieffer, in: Theory of Chemisorption, Ed. J.R. Smith (Springer, Berlin, 1980) p. 183.

[9] B.N.J. Persson and M. Persson, Solid State Commun. 77 (1980) 175;
H. Ueba, J. Chem. Phys. 77 (1982) 3759;
A.I. Volokitin, O.M. Braun and V.M. Yakovlev. Surf. Sci. 172 (1986) 31;
V.P. Zhdanov, Elementary Physicochemical Processes on Solid Surfaces (Plenum, New York, 1991).

[10] R.F. Khairutdinov, K.I. Zamaraev and V.P. Zhdanov, in: Electron Tunneling in Chemistry, Comprehensive Chem- ical Kinetics, Vol. 30, Ed. R.G. Compton (Elsevier, Am- sterdam, 1989).

[11] T.P. Grozdanov and R.K. Janev, Phys. Lett. A 65 (1978) 396.

[12] J.J.C. Geerlings, J. Los, J.P. Gauyacq and N.M. Temme, Surf. Sci. 172 (1986) 257.

[13] R. Rasser, J.N.M. Wunnik and J. Los, Surf. Sci. 118 (1982) 697.

[14] D.C. Langreth and P. Nordlander, Phys. Rev. B 43 (1991) 2541.

[15] E.G. Overbosch and J. Los, Surf. Sci. 108 (1981) 99.

[16] E.G. Overbosch and J. Los, Surf. Sci. 108 (1981) 117.

[17] J.J.C. Geerlings, L.F.Tz. Kwakman and J. Los, Surf. Sci. 184 (1987) 305.

[18] J.J.C. Geerlings, R. Rodnik, J. Los and J.P. Gauyacq, Surf. Sci. 186 (1987) 15.

[19] G.A. Kimmel, D.M. Goodstein and B.H. Cooper, J. Vac. Sci. Technol. A 7 (1989) 2186.

[20] G.A. Kimmel, D.M. Goodstein, Z.H. Levine and B.H. Cooper, Phys. Rev. B 43 (1991) 9403.