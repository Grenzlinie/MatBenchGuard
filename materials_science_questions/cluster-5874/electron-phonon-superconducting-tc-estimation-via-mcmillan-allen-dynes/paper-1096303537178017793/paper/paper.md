# Thoughts about boosting superconductivity

Dirk van der Marel¹

¹ Department of Quantum Mater Physics, University of Geneva,
24 Quai Ernest-Ansermet, 1211 Geneva 4, Switzerland

This manuscript version is made available under the CC-BY-4.0 license https://creativecommons.org/licenses/by/4.0/

(Dated: February 7, 2025)

In a superconductor electrons form pairs despite the Coulomb repulsion as a result of an effective attractive interaction mediated by, for example phonons. In the present paper DeGennes' description of the dynamically screened Coulomb interaction is adopted for the effective interaction. This model is generalized by including the elastic response of the charge-compensating background and the BCS gap equation is solved for the resulting effective electron-electron interaction. It is demonstrated that the superconducting critical temperature becomes strongly enhanced when the material is tuned close to a structural instability.

## I. INTRODUCTION

Jan Zaanen took no interest in boring subjects. Our first conversation in the autumn of 1982 included superconductivity, the Kondo effect and general relativity. Jan and I had just started our Ph D studies with George Sawatzky and we were making mutual introductions in our shared office in the basement of the chemistry building at the University of Groningen. This conversation was the first one of countless scientific discussions and it kicked off a lasting friendship.

One of the major questions that has occupied the generation to which Jan and I belonged, was inspired by the discovery of high temperature superconductivity in the cuprates [1]. In BCS theory a pairing instability occurs at a critical temperature $T_c$ where $\lambda\chi_0'(T_c)=1$. Here $\lambda$ is an attractive pairing interaction, $\chi_0'(T)\sim\ln(\omega_0/k_BT)$ is the static bare pair susceptibility and $\omega_0$ is an appropriately weighted average energy of the phonons involved in the pairing interaction. The conventional approach has been to argue that in the cuprates bosonic degrees of freedom such as phonons, plasmons, spin-fluctuations, loop-currents or excitons mediate a strong attractive pairing interaction. In a series of papers with Jian-Huang She and others, Jan and his coauthors argued [2-5], that the bare pair susceptibility in the cuprates has properties qualitatively different from standard metals, causing $T_c$ to be very high even when the pairing interaction isn't stronger than in other superconducting materials. They started from the Ansatz that the bare pair susceptibility of the cuprates has an algebraic temperature dependence $\chi_0'(T)\sim1/T^\alpha$ and this, they reasoned, causes the pairing instability to occur at relatively high temperatures. This Ansatz was motivated by the results of Ref. [6] on the "Planckian" nature of the relaxation time observed in optical experiments resulting from an animated discussion on our way to a meeting in Poland.

The concept that, as a result of coupling to phonons [7] or other collective degrees of freedom such as spin fluctuations [8] or loop currents [9], electrons overcome the Coulomb barrier and form pairs, is inherently counterintuitive. The -to my taste- most intuitively appealing explanation of how this works, was given by DeGennes in his textbook on superconductivity [10] and was based on the "jellium model". It turned out that solving this model is not entirely trivial [11-13] and a number of questions remain, some of which I will discuss below.

## II. THE JELLIUM MODEL

The interaction process where two electrons are scattered from $|\boldsymbol{k},-\boldsymbol{k}\rangle$ to $|\boldsymbol{k}',-\boldsymbol{k}'\rangle$ can be described by considering the Coulomb interaction $V(q)$ and the screening thereof [10]:
$$
V^{\text{eff}}(q,\omega)=\frac{V(q)}{\epsilon(q,\omega)},\tag{1}
$$
where $q=|\boldsymbol{k}-\boldsymbol{k}'|$. In the jellium model the potential landscape of the charge-compensating background is flat, so that the energy-momentum relation is $\epsilon=\hbar^2k^2/2m_e$. The dielectric function of a system of free electrons in a compressible positively charged background is (see A )
$$
\epsilon(q,\omega)=1+\frac{k_0^2}{q^2}+\frac{\omega_0^2}{B_0\rho_m^{-1}q^2/(1+q^2s^2)-\omega^2}\tag{2}
$$
where $k_0=\sqrt{4k_F/(\pi a_0)}$ is the Thomas-Fermi wave vector, $\omega_0$ is the plasma frequency of the charge-compensating background, $b_0$ is it's bulk modulus, $\rho_m$ it's mass density and $s$ is the length scale below which $B_q$ vanishes. For our discussion it is useful to define reduced parameters for the bulk moduli of the charge-compensating background ($b_0$) and of the electrons ($b_F$)
$$
b_0=B_0\frac{k_F^2}{\rho_m\omega_0^2}\tag{3}
$$
$$
b_F=\frac{k_F^2}{k_0^2}=\frac{\pi k_Fa_0}{4},\tag{4}
$$
both of which are dimensionless constants.

To obtain the effective interaction in dimensionless form we multiply $V^{\text{eff}}(q,\omega)$ with the density of states at the Fermi level

$$
N(0)=\frac{m_{e} k_{F}}{2 \pi^{2} \hbar^{2}} . \tag{5}
$$

The effective interaction in the s-wave channel is then given by

$$
v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s}(\omega)=\frac{1}{2} \int_{0}^{\pi} N(0) V^{\text{eff}}(q, \omega) \sin \theta d \theta, \tag{6}
$$

where $\theta$ is the angle between $\boldsymbol{k}$ and $\boldsymbol{k}^{\prime}$. The result of this integral in closed form is

$$
v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s}(\omega)=v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s, 1}(\omega)+v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s, 2}(\omega) \tag{7}
$$

$$
v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s, 1}(\omega)=\frac{1}{8 \kappa}\left[\sqrt{g}-\frac{h}{\sqrt{g}}\right] \ln \left|\frac{\left(e+\kappa_{+}\right)\left(e+\kappa_{-}\right)-g-2 \kappa \sqrt{g}}{\left(e+\kappa_{+}\right)\left(e+\kappa_{-}\right)-g+2 \kappa \sqrt{g}}\right| \quad (g>0) \tag{8}
$$

$$
v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s, 1}(\omega)=\frac{1}{4 \kappa}\left[\sqrt{-g}+\frac{h}{\sqrt{-g}}\right] \arctan \left[\frac{2 \kappa \sqrt{-g}}{\left(e+\kappa_{+}\right)\left(e+\kappa_{-}\right)-g}\right] \quad (g<0) \tag{9}
$$

$$
v_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{s, 2}(\omega)=\frac{1}{16 \beta_{F} \kappa} \ln \left|\frac{\left(e+\kappa_{+}\right)^{2}-g}{\left(e+\kappa_{-}\right)^{2}-g}\right|, \tag{10}
$$

where

$$
\begin{aligned}
& \kappa=\frac{k k^{\prime}}{k_{F}^{2}} ; \quad \kappa_{ \pm}=\frac{\left(k \pm k^{\prime}\right)^{2}}{2 k_{F}^{2}} ; \quad e=e_{1}+e_{2} ; \quad e_{1}=\frac{1-\beta_{F} z^{2} / \zeta_{0}^{2}}{4 \beta_{0}} ; \quad e_{2}=\frac{1}{4 \beta_{F}} ; \\
& g=e^{2}+\frac{z^{2} / \zeta_{0}^{2}}{4 \beta_{0}} ; \quad h=e_{1}^{2}-e_{2}^{2} ; \quad \zeta_{0}^{2}=\frac{b_{0} z_{0}^{2}}{b_{0}-b_{F} k_{F}^{2} s^{2} z^{2} / z_{0}^{2}} ; \quad z_{0}^{2}=\frac{4 m_{e}}{3 m_{N}} ; \quad z=\frac{\hbar \omega}{\epsilon_{F}} ; \\
& \beta_{F}=b_{F} \frac{b_{0}+k_{F}^{2} s^{2}\left(1-b_{F} z^{2} / z_{0}^{2}\right)}{b_{0}-b_{F} k_{F}^{2} s^{2} z^{2} / z_{0}^{2}} ; \quad \beta_{0}=\left[b_{0}-b_{F} k_{F}^{2} s^{2} z^{2} / z_{0}^{2}\right] \times\left[1+k_{F}^{2} s^{2} b_{0}^{-1}\left(1-b_{F} z^{2} / z_{0}^{2}\right)\right]. \tag{11}
\end{aligned}
$$

This function is displayed in Fig. 1 for mass number 7, density $n=4.6 \cdot 10^{22} \mathrm{~cm}^{-3}$ and a selection of values of $b_{0}$ and $s$. For $\omega \rightarrow \infty$ the interaction converges to the Thomas-Fermi screened Coulomb repulsion. The interaction has an explicit dependence on momentum and frequency, which is handled in different ways depending on the formalism:

1. If one solves the BCS gap equation [14] with the Bardeen-Pines approach [7], the $\omega$ dependence is treated as the on-shell interaction, $\hbar \omega=\epsilon_{\boldsymbol{k}}-\epsilon_{\boldsymbol{k}^{\prime}}$.

2. If one solves the Eliashberg equations [15], the dependence on $\omega$ is transformed to Matsubara frequencies which are on the imaginary frequency axis. The singularities seen in Fig. 1 are absent for the imaginary axis, which has certain practical advantages for numerical coding. After solving the gap-function for the Matsubara frequencies one can in principle reconstruct the gap-function along the real axis, which is however a challenging numerical procedure.

3. If one solves the McMillan equation [16], one usually starts from the electron-phonon coupling function $\alpha^{2} F(\omega)$ which is nowadays typically obtained from a frozen-phonon band structure calculation. Formally the electronphonon coupling function and the pairing interaction are connected by Kramers-Kronig relations, i.e. $v(\omega)=$ $\mu-2 \int_{0}^{\infty} \frac{\nu \alpha^{2} F(\nu)}{\nu^{2}-\omega^{2}} d \nu$, [17] where $\mu$ is the the Thomas-Fermi screened Coulomb repulsion. In the MacMillan approach the phonon-mediated interaction $\lambda$ is calculated from integrating $\alpha^{2} F(\omega) / \omega$.

In section IV we will solve the BCS gap equation, i.e. item 1 of the list above. Before doing so we open a parenthesis to briefly discuss a frequently used approximation which we will not use in section IV. This approximation rests on the argument that the most important contribution to the pairing interaction originates from the Fermi surface area. The Coulomb interaction can then be represented by a single parameter $\mu$, corresponding to $k=k^{\prime}=k_{F}$

$$
\mu=\frac{1}{8 b_{F}} \ln \left(1+4 b_{F}\right). \tag{12}
$$

Continuing the discussion of the case $k=k^{\prime}=k_{F}$, the static $(\omega=0)$ interaction is

$$
v^{s}(0)=\frac{1}{8 b_{F}} \frac{b_{0}}{k_{F}^{2} s^{2}+b_{0}} \ln \left|1+\frac{4 b_{F}\left(k_{F}^{2} s^{2}+b_{0}\right)}{b_{F}+b_{0}}\right|, \tag{13}
$$

which combines the phonon-mediated attraction and the Coulomb repulsion. Correspondingly, the parameter characterizing the phonon-mediated attraction is

$$
\lambda=\mu-v^{s}(0). \tag{14}
$$

![](./images/1096303537178017793_1.jpg)

Figure 1. Interaction potential in the s-wave channel, Eq. 7, as a function of $\hbar\omega$ in the case of lithium for four representative values of the reduced bulkmodulus of the charge-compensating background, $b_0$, and of $(k_F s)^2$. For this $r_s$ value the reduced bulk modulus of the electrons is $b_F=\pi k_F a_0/4=0.461$. The curves displayed here are for $k=k'=k_F$. The Fermi energy is $\epsilon_F=4.7$ eV and the plasma energy of the charge-compensating background is $\hbar\omega_0=70$ meV.

![](./images/1096303537178017793_2.jpg)

Figure 2. Gapfunction at $T=0$ in the case of lithium for three different values of the reduced bulk modulus $b_0$ and $(k_F s)^2=0.23b_F$. For this $r_s$ value the reduced bulk modulus of the electrons is $b_F=0.461$.

We see right away that for $b_0=0$ we have $\lambda=\mu$, for $b_0>0$ we obtain $\lambda<\mu$ and for $b_0<0$ it follows that $\lambda>\mu$. Fig. 1 illustrates these three cases. At this point we close the parenthesis about the $k=k'=k_F$ approximation. In section IV we solve the BCS gap equation with the substitution $\hbar\omega=\epsilon_{\boldsymbol{k}}-\epsilon_{\boldsymbol{k}'}$ and the full $k$ and $k'$ dependence of the interaction.

## III. STABILITY CONSIDERATIONS

The sound dispersion of a metal is obtained from the condition $\epsilon(q,\omega)=0$. Taking the limit $q\rightarrow0$, we obtain the sound velocity:

$$
c=\frac{\omega}{q}=\frac{\omega_0}{k_F}\sqrt{b_F+b_0}. \tag{15}
$$

Correspondingly, the overall reduced bulk modulus of the charge-compensating background and the electrons together is

$$
b_{tot}=b_F+b_0. \tag{16}
$$

For $b_0 > -b_F$ the overall compressibility is positive. While this is a necessary condition for stability of the system, it is not a sufficient one. A stricter requirement is, that $\text{Re}\epsilon(q,0)$ should *not* be in the range $\{0;1\}$ [18]. Consequently, from the expression for the dielectric function, Eq. 2, for the present model the stability condition is

$$
b_0>-\min(k_F^2s^2,b_F) \tag{17}
$$

We furthermore notice that $1/\epsilon(q,0)$ diverges for $q=q_c$ where

$$
q_c=k_F\sqrt{\frac{-b_F-b_0}{k_F^2s^2+b_0}}. \tag{18}
$$

The square root is real for $b_0\in\{-b_F;-k_F^2s^2\}$, implying that in this parameter range the system is unstable with respect to a charge density wave (CDW) of wave vector $q_c$. To evaluate the superconducting properties in this range requires knowledge about the amplitude of the CDW in equilibrium and of its impact on the electrondispersion, which is outside the limitations of the present model.

## IV. SUPERCONDUCTIVITY

The BCS gap equation for s-wave pairing, using the corresponding definition of the interaction, Eq. 6, is

$$
\begin{aligned}
\Delta(\epsilon) & =-\int_0^\infty \frac{v_{k,k'}^s(\omega)\Delta(\epsilon')}{2\sqrt{(\epsilon'-\mu_F)^2+\left|\Delta(\epsilon')\right|^2}} \times \\
& \times\tanh\left(\frac{\sqrt{(\epsilon'-\mu_F)^2+\left|\Delta(\epsilon')\right|^2}}{2k_BT}\right)\sqrt{\frac{\epsilon'}{\epsilon_F}}d\epsilon',
\end{aligned} \tag{19}
$$

where $\hbar\omega=\epsilon-\epsilon'$ and $\mu_F$ is the chemical potential. The density of states is $N(\epsilon)=N(0)\sqrt{\epsilon/\epsilon_F}$, but note that the

![](./images/1096303537178017793_3.jpg)

Figure 3. Phase diagram in the case of lithium for 3 dif- ferent values of $(k_{F} s)^{2}$. The horizontal axis is the reduced bulk modulus of the charge-compensating background, Eq.3. Middle panel $(k_{F}^{2} s^{2}=0.23)$ : In principle the curve extends to $b_{0}=-0.23$ , but for $-b_{0} \lesssim 0.23$ the numerical output of the gap equation becomes inaccurate.

factor $N(0)$ has been absorbed in the definition of the interaction, Eq. 6. Since in the present study $k_{B} T_{c} \ll \epsilon_{F}$ , it follows that $\mu_{F} \cong \epsilon_{F}$ . A consequence of Eq. 19 is, that $\Delta(\epsilon)$ can be chosen real. For display purposes we adopt the convention that $\Delta(0)$ is real and positive. As illustrated in Fig. 1, if $b_{0}=0$ , the effective interaction has a negative sign for energies well below $\hbar \omega_{0}$ . On the other hand, $v^{s}(0)=0$ , i.e. the static interaction is zero. Given this state of affairs one may wonder if the ground state is superconducting. This question was addressed for the case of hydrogen, also using the jellium model, by Ginzburg and Kirzhnits [11], by Kirzhnits [12] and in a recent paper of the present author and Berthod [13]. The answer was that, in fact, the ground state is superconducting. While the original estimates were in the range of a few $100 ~K[11,12]$ , we found relatively low values of $T_{c}$ with this model [13]: The density dependence of $T_{c}$ is dome shaped with the maximum, $T_{c}=30 ~K$ , at $r_{s}=3.5$ . Although this is far below the original estimates $[11,12]$ , still the message of principle remains that, despite the fact that $v^{s}(0)=0$ , there is a non-trivial superconducting solution. Cohen and Anderson [19] argued that the static dielectric function cannot be negative. Consequently $v^{s}(0) \geq 0$ , which is equivalent to the condition $\lambda \leq \mu$ . They simplified the interaction potential to $V(k, k')=\lambda-\mu$ for energies below $\omega_{0}, V(k, k')=-\mu$ for energies above $\omega_{0}$ and obtained

$$
k_{B} T_{c}=\frac{2 e^{\gamma}}{\pi} \omega_{0} \exp \left(-\frac{1}{\lambda-\mu^{*}}\right) \tag{20}
$$

where $\mu^{*}=\mu /[1+\mu \ln (\epsilon_{F} / \omega_{0})]$ is the screened Coulomb pseudopotential. With the aforementioned constraint that the static dielectric function cannot be negative, the additional constraint that $\mu<1 / 2$ , and taking realistic values for the Fermi energy and the phonon plasma frequency $(\epsilon_{F} \sim 7 eV, \omega_{0} \sim 0.1 eV)$ they concluded that $T_{c}$ has a maximum of about $10 ~K$ . However, as discussed in the previous section, Dolgov, Khirzhnits and Maksi- mov [18] have demonstrated that negative values of the static dielectric function are possible, but values in the range $\{0 ; 1\}$ cannot occur for a stable system.

We now turn to the case of lithium. The cell volume of solid lithium is $V_{0}=21.6 \AA^{3}$ [20]. Consequently the conduction-electron density is $n=4.6 \cdot 10^{22} ~cm^{-3}$ and the Wigner-Seitz radius is $r_{s}=3.27$ . Correspondingly $k_{F}=1.1 \cdot 10^{8} ~cm^{-1}, \epsilon_{F}=4.7 eV$ and $\hbar \omega_{0}=70 meV$ . In Fig. 2 the gap function is shown for 3 representative cases corresponding to the interaction potential displayed in Fig. 1, $b_{0}$ positive, zero and negative. We see that the effect of positive $b_{0}$ is to suppress the superconducting order. In contrast, a negative $b_{0}$ enhances $T_{c}$ . Regarding positive $b_{0}$ it is of interest to point out that in this case the interaction (blue curve in Fig. 1) is entirely repulsive for all energies. Indeed, as illustrated by Eq. 20, even in this case a superconducting solution can be obtained,provided that $\lambda>\mu^{*}$ [21]. In this case the gap $\Delta(\omega)$  changes sign exactly where the Coulomb interaction be- comes repulsive as illustrated in Fig. 2 of Ref [22] and Fig. 2 of the present paper.

In Ref. [13], it was shown that $T_{c}^{*}=0.925 \sqrt{\varepsilon_{F} E_{c}} / k_{B}$  where $E_{c}$ is the condensation energy calculated at $T=0$ , coincides with the critical temperature following from the jump in the specific heat, providing an efficient method for obtaining the critical temperature. In Fig. 3 the criti- cal temperature calculated from the condensation energy is displayed as a function of $b_{0}$ . Pointing to the left is the direction of positive $b_{0}$ where the critical temperature decreases below $1 mK$ . Experimentally, the critical temperature has been determined as $T_{c}=0.4 mK$ [23].In view of these findings it seems plausible that the low $T_{c}$  values in the alkali metals are caused by none-negligible elasticity of the charge-compensating background. Point- ing to the right is the direction of negative $b_{0}$ , illustrat ing that tuning the system toward an elastic instability is a promising strategy for boosting $T_{c}$ . Note that the acoustic phonons soften in this limit. Using theoretical models different from the one employed here, Bergmann and Rainer [24], Maksimov and Savrasov [25] and Jiang et al. [26] have also concluded that phonon softening should typically be accompanied by an increase of $T_{c}$ .

While we have seen that a negative $b_{0}$ is beneficial for superconductivity, the elastic response in this model is given by $b_{0}+b_{F}$ . If a negative value of $b_{0}+b_{F}$ were to occur, the material would collapse. For this reason candidates for this type of boosting of superconductivity have to be materials in proximity to a lattice instability,i.e. with $b_{0}<0$ while still being in a thermodynamically stable state with $b_{0}+b_{F}>0$ . It is tempting to look for a relation to the observed $T_{c}$ enhancement of lithium up to $20 ~K$ for pressures in the range of 20 to 70 GPa [27, 28]. However, at high densities the overlap of core electrons becomes an important factor and contrary

to intuition the electronic structure of lithium becomes less free-electron like [29], atoms form pairs and above 80 GPa the material is even semiconducting [30]. The high pressure phases of lithium are therefore not captured by the model here considered. That said, in a realistic de- scription of the system taking into account the lattice structure, instabilities can occur similar in nature as the one that we discussed above. For the same reason the dielectric function could become negative when the sys- tem is tuned close to such an instability, and once again the static interaction would be attractive with the effect of boosting $T_{c}$. In that sense, the structural instabilities that are known to occur in lithium under pressure [31], may play a similar role as in the model discussed above.

## V. OUTLOOK

While we saw that the BCS gap equations can be solved relatively easily for the jellium model, the model itself contains a number of approximations: (i) The Thomas- Fermi approximation was used to describe the screening of the Coulomb interaction. (ii) The frequency depen- dence of the interaction was treated by substituting the energy difference of the interacting electrons. As was shown by DeGennes [10] this is equivalent to treating the electron-phonon coupling in second order perturba- tion theory. (iii) The BCS variational wavefunction was assumed. (iv) The potential of the positively charged nu- clei was replaced with a constant value. Removing some or all of these approximations would allow for more re- alistic modeling of the superconducting properties. This may require a radically different approach such as the holographic method [32] of which Jan was a great am- bassador. In certain parameter ranges the static suscep- tibility diverges for wave vector $q_{c}$, while the interaction in the s-wave channel of the undistorted system is at- tractive. Within the limitations of the model used here these aspects could not be addressed more deeply, but I believe that they deserve further attention. Jan Zaanen proposed, together with Jian-Huang She, that high $T_{c}$ su perconductivity can be obtained by using a material for which the pair susceptibility has an algebraic tempera- ture dependence. The main finding of the present paper is that tuning the system close to a lattice instability boosts the pairing interaction. Combining these two el- ements, algebraic pair susceptibility and proximity to a lattice instability, looks like a promising strategy for the realization of superconductivity at room temperature.

## VI. CONCLUSIONS

We have explored DeGenne's intuitive "jellium" descrip- tion of the effective interaction, which treats the Coulomb repulsion and the phonon-mediated interaction in one fell swoop. One additional element -not considered by DeGennes- was included, namely the elastic response of the charge-compensating background. When leaving out this elastic response, the interaction potential vanishes in the static limit. Nevertheless, the BCS gap equation has a solution with a non-zero $T_{c}$. If a positive elastic re sponse is added (causing the sound velocity to increase), the interaction potential in the static limit is repulsive. Even in this case $T_{c}$ can be non-zero. If a negative elas tic response is introduced (causing the sound velocity to decrease), the interaction potential in the static limit is attractive and qualitatively similar to the standard BCS scenario for pairing. This has the effect of boosting the critical temperature.

## VII. ACKNOWLEDGEMENTS

I am grateful to Erik van Heumen, Christophe Berthod, Louk Rademaker, Frank Marsiglio and Alessio Zaccone for inspiring discussions and comments. This paper is dedicated to the memory of Jan Zaanen who has been an inexhaustible source of original perspectives.

### Appendix A: Linear response of electrons and a compressible charge-compensating background

The dielectric function is defined as the linear response of the charge of the material to a test charge $\rho_{ext}$. The charge of the material has in the present case two contri- butions: electrons and the massive charge-compensating background. We use the mean-field approximation for the dielectric function, so that it becomes the sum of two independent contributions from the electrons and the charge-compensating background

$$
\epsilon(q, \omega)=1-4 \pi \chi_{e}^{(0)}-4 \pi \chi_{0}^{(0)} \tag{A1}
$$

For the electronic susceptibility we adopt the Thomas- Fermi approximation

$$
4 \pi \chi_{e}^{(0)}=-\frac{k_{0}^{2}}{q^{2}} \tag{A2}
$$

The charge-compensating background is characterized by the following properties

- Mass density $\rho_{m}$, charge density $\rho_{c}$ with the ra tio $\rho_{c} / \rho_{m}$ fixed by the charge/mass ratio of the matter constituting the charge-compensating back- ground, and the corresponding fluctuations of den- sity $\delta \rho_{m, e}(r, t)$ and current $\delta j_{m, c}(r, t)$ satisfying the continuity relation $\nabla \cdot \delta \boldsymbol{j}_{m, c}=-\partial \delta \rho_{m, c} / \partial t$.
- the bulk modulus $B_{q}$, which may depend on the wave vector $q$ of the density fluctuation.

$\delta E$ is the electric field generated by the test charge and the resulting fluctuation of the charge-compensating background respectively, i.e.

$$
\nabla \cdot \delta \boldsymbol{E}=4 \pi\left(\delta \rho_{e x t}+\rho_{c}\right) \tag{A3}
$$

The fluctuations of mass and charge contained inside an infinitesimal volume element $\Omega$ are $M = \Omega \delta \rho_m = \Omega(\rho_m/\rho_c)\delta \rho_c$ and $Q = \Omega \delta \rho_c$. The fluctuation of the mass-flow represented by this volume element is $\Omega \delta \boldsymbol{j}_m = \Omega(\rho_m/\rho_c)\delta \boldsymbol{j}_c$. The restoring force due to the density fluctuation is $\delta \boldsymbol{F} = -\Omega B_q(\nabla \delta \rho_m/\rho_m) = -\Omega B_q(\nabla \delta \rho_c/\rho_c)$. The acceleration of the mass $M$ is given by Newton's law

$$
M \frac{d}{dt} \delta \boldsymbol{v} = Q \delta \boldsymbol{E} + \delta \boldsymbol{F} \tag{A4}
$$

so that

$$
\frac{\rho_m}{\rho_c} \frac{d}{dt} \delta \boldsymbol{j}_c = \rho_c \delta \boldsymbol{E} - B_q \frac{\nabla \delta \rho_c}{\rho_c}. \tag{A5}
$$

Taking the divergence of both sides and using the continuity relation we obtain in the limit of small motion

$$
-\frac{\partial^2}{\partial t^2} \delta \rho_c = \frac{4 \pi \rho_c^2}{\rho_m} (\delta \rho_{ext} + \delta \rho_c) - B_q \nabla \cdot \nabla \delta \rho_c \tag{A6}
$$

We substitute $\delta \rho_{m,c}(\boldsymbol{r}, t) = \delta \rho_{m,c} e^{i(\boldsymbol{q} \cdot \boldsymbol{r} - \omega t)}$ and obtain

$$
\omega^2 \delta \rho_c = \omega_0^2 (\delta \rho_{ext} + \delta \rho_c) + B_q q^2 \delta \rho_c \tag{A7}
$$

where

$$
\omega_0^2 = \frac{4 \pi \rho_c^2}{\rho_m}. \tag{A8}
$$

We thus arrive at the contribution to the susceptibility of the massive charge-compensating background

$$
4 \pi \chi_0^{(0)} = \frac{\delta \rho_c}{\delta \rho_c + \delta \rho_{ext}} = \frac{\omega_0^2}{\omega^2 - B_q \rho_m^{-1} q^2} \tag{A9}
$$

We adopt the following model for the bulkmodulus

$$
B_q = \frac{B_0}{1 + q^2 s^2} \tag{A10}
$$

where $b_0 \rho_m^{-1}$ is usually positive, but negative values are possible. One may wonder why a $q$-dependence is introduced. It would in fact be unreasonable to assume that the elastic properties would remain the same at all length scales. The only important requirement for the present discussion is, that $B_q$ converges to zero as $1/q^2$, the details of the $q$ dependence don't matter. Substituting Eqs. A2 and A9 in Eq. 2 results in

$$
\epsilon(q, \omega) = 1 + \frac{k_0^2}{q^2} + \frac{\omega_0^2}{B_0 \rho_m^{-1} q^2/(1 + q^2 s^2) - \omega^2} \tag{A11}
$$

## DATA AND CODE AVAILABILITY

- The theoretical data generated in this study are available in Ref. [33]. These will be preserved for 10 years. All other data that support the plots within this paper and other findings of this study are available from the author upon reasonable request.
- The custom computer codes used to generate the results reported in this paper are available in Ref. [33].
- Any additional information required to reanalyze the data reported in this paper is available from the author upon request.

## DECLARATION OF INTERESTS

The author declares no competing interests.

[1] J. G. Bednorz, K. A. Muller, Possible high $T_c$ superconductivity in the Ba-La-Cu-O system, Z. Phys. B: Condens. Matter 64 (1986) 189-193. doi:10.1007/bf01303701.
[2] J.-H. She, J. Zaanen, BCS superconductivity in quantum critical metals, Phys. Rev. B 80 (2009) 184518. doi:10.1103/PhysRevB.80.184518.
[3] J.-H. She, B. J. Overbosch, Y.-W. Sun, Y. Liu, K. E. Schalm, J. A. Mydosh, J. Zaanen, Observing the origin of superconductivity in quantum critical metals, Phys. Rev. B 84 (2011) 144527. doi:10.1103/PhysRevB.84.144527.
[4] S.-X. Yang, H. Fotso, S.-Q. Su, D. Galanakis, E. Khatami, J.-H. She, J. Moreno, J. Zaanen, M. Jarrell, Proximity of the Superconducting Dome and the Quantum Critical Point in the Two-Dimensional Hubbard Model, Phys. Rev. Lett. 106 (2011) 047004. doi:10.1103/PhysRevLett.106.047004.
[5] J.-H. She, J. Zaanen, Superconductivity and fermionic quantum criticality, Physica C: Superconductivity 493 (2013) 34-35, new3SC-9. doi:https://doi.org/10.1016/j.physc.2013.03.014.
[6] D. van der Marel, H. J. A. Molegraaf, J. Zaanen, Z. Nussinov, F. Carbone, A. Damascelli, H. Eisaki, M. Greven, P. H. Kes, M. Li, Quantum critical behaviour in a high-$T_c$ superconductor, Nature 425 (2003) 271. doi:10.1038/nature01978.
[7] J. Bardeen, D. Pines, Electron-Phonon Interaction in Metals, Phys. Rev. 99 (1955) 1140. doi:10.1103/PhysRev.99.1140.
[8] D. J. Scalapino, E. Loh, J. E. Hirsch, $d$-wave pairing near a spin-density-wave instability, Phys. Rev. B 34 (1986) 8190-8192. doi:10.1103/PhysRevB.34.8190.

[9] C. M. Varma, Pseudogap in cuprates in the loop-current ordered state, Journal of Physics: Condensed Matter 26 (2014) 505701. doi:10.1088/0953-8984/26/50/505701.

[10] P. G. De Gennes, Superconductivity of Metals and Alloys, Benjamin, New York, Amsterdam, 1966.

[11] V. L. Ginzburg, D. A. Kirzhnits, Superconductivity in White Dwarfs and Pulsars, Nature 220 (1968) 148. doi:10.1038/220148b0.

[12] D. A. Kirzhnits, Superconductivity in Systems with Arbitrary Interaction Sign, ZhETF Pis. Red. 9 (1969) 360.

[13] D. van der Marel, C. Berthod, Superconductivity in metallic hydrogen, Newton 1 (2025) 100002. doi:10.1016/j.newton.2024.100002.

[14] J. Bardeen, L. N. Cooper, J. R. Schrieffer, Theory of Superconductivity, Phys. Rev. 108 (1957) 1175. doi:10.1103/PhysRev.108.1175.

[15] G. M. Eliashberg, Interactions between electrons and lattice vibrations in a superconductor, Sov. Phys. JETP 11.

[16] W. L. McMillan, Transition Temperature of Strong-Coupled Superconductors, Phys. Rev. 167 (1968) 331. doi:10.1103/PhysRev.167.331.

[17] F. Marsiglio, Eliashberg theory: A short review, Annals of Physics 417 (2020) 168102, eliashberg theory at 60: Strong-coupling superconductivity and beyond. doi:https://doi.org/10.1016/j.aop.2020.168102.

[18] O. V. Dolgov, D. A. Kirzhnits, E. Maksimov, On an admissible sign of the static dielectric function of matter, Reviews of Modern Physics 53 (1981) 81. doi:10.1103/RevModPhys.53.81.

[19] M. L. Cohen, P. W. Anderson, Comments on the Maximum Superconducting Transition Temperature, AIP Conf. Proc. 4 (1972) 17. doi:10.1063/1.2946185.

[20] M. Hanfland, I. Loa, K. Syassen, U. Schwarz, K. Takemura, Equation of state of lithium to 21 GPa, Solid State Communications 112 (1999) 123. doi:10.1016/S0038-1098(99)00322-1.

[21] P. Coleman, Introduction to Many-Body Physics, Cambridge University Press, Cambridge. UK. Cambridge, 2015.

[22] P. Morel, P. W. Anderson, Calculation of the Superconducting State Parameters with Retarded Electron-Phonon Interaction, Phys. Rev. 125 (1962) 1263. doi:10.1103/PhysRev.125.1263.

[23] J. Tuoriniemi, K. Juntunen-Nurmilaukas, J. Uusvuori, E. Pentti, A. Salmela, A. Sebedash, Superconductivity in lithium below 0.4 millikelvin at ambient pressure, Nature 447 (2007) 187. doi:10.1038/nature05820.

[24] G. Bergmann, D. Rainer, The sensitivity of the transition temperature to changes in $\alpha^{2}F(\omega)$, Z. Phys. 263 (1973) 59-68. doi:10.1007/BF02351862.

[25] E. Maksimov, D. Savrasov, Lattice stability and superconductivity of the metallic hydrogen at high pressure, Solid State Communications 119 (2001) 569-572. doi:https://doi.org/10.1016/S0038-1098(01)00301-5.

[26] C. Jiang, E. Beneduce, M. Baggioli, C. Setty, A. Zaccone, Possible enhancement of the superconducting $T_{c}$ due to sharp Kohn-like soft phonon anomalies, Journal of Physics: Condensed Matter 35 (2023) 164003. doi:10.1088/1361-648X/acbd0a.

[27] K. Shimizu, H. Ishikawa, D. Takao, T. Yagi, K. Amaya, Superconductivity in compressed lithium at 20 K, Nature 419 (2002) 597. doi:doi.org/10.1038/nature01098.

[28] S. Deemyad, J. Schilling, Superconducting Phase Diagram of Li Metal in Nearly Hydrostatic Pressures up to 67 GPa, Phys. Rev. Letters 91 (2003) 167001. doi:10.1103/PhysRevLett.91.167001.

[29] J. B. Neaton, N. W. Ashcroft, Pairing in dense lithium, Nature 400 (1999) 141. doi:10.1038/22067.

[30] S. Matsuoka, K. Shimizu, Direct observation of a pressure-induced metal-to-semiconductor transition in lithium, Nature 458 (2018) 186. doi:10.1038/nature07827.

[31] M. Marqués, M. I. McMahon, E. Gregoryanz, M. Hanfland, C. L. Guillaume, C. J. Pickard, G. J. Ackland, R. J. Nelmes, Crystal Structures of Dense Lithium: A Metal-Semiconductor-Metal Transition, Phys. Rev. Lett. 106 (2011) 095502. doi:10.1103/PhysRevLett.106.095502.

[32] J. Zaanen, Y.-W. Sun, Y. Liu, K. Schalm, Holographic duality in condensed matter physics, Cambridge University Press, 2015.

[33] D. van der Marel, Open Data to "Thoughts about boosting superconductivity", Yareta doi:DOI:10.26037/yareta:t4bzvpegabdw5fmyih6faakhba.