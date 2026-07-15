# Monte Carlo simulation of electron emission induced by swift highly charged ions: beyond the linear response approximation

M. Beuve $^{1,2,3}$, M. Caron $^{1, \mathrm{a}}$, P.D. Fainstein $^{3}$, M. Galassi $^{2}$, B. Gervais $^{1}$, R.D. Rivarola $^{2}$, and H. Rothard $^{1, \mathrm{~b}}$

$^{1}$ Centre Interdisciplinaire de Recherche Ions Lasers, CEA-CNRS-ISMRA, rue Claude Bloch, BP 5133,
14070 Caen Cedex 05, France
$^{2}$ Instituto de Física Rosario, CONICET-UNR, av. Pellegrini 250, 2000 Rosario, Argentina
$^{3}$ Centro Atómico Bariloche, Comisión Nacional de Energía Atómica, av. E. Bustillo 9500, 8400 Bariloche, Argentina

Received 2 January 2002 / Received in final form 26 April 2002
Published online 8 October 2002 - © EDP Sciences, Società Italiana di Fisica, Springer-Verlag 2002

**Abstract.** Numerical simulations of ion induced electron emission from solids mostly use the first order Born approximation within the dielectric formalism to describe valence electron excitation. As a result, the yield of emitted electrons is found to scale with the square of the projectile charge $Q_P$ in contrast to experimental findings obtained with carbon targets [1]. Since similar deviations from $Q_P^2$ scaling were observed for the electronic stopping power, at least a part of this deviation must be related to primary ion-electron interaction, for which an alternative description needs to be developed. We thus present here a distorted wave approach for the modelling of primary interaction, which can be expected to give better results in view of its success in describing ion-atom collisions at large impact velocity. Keeping the same description of the electron transport through the target, we show that both the electron yield and the stopping power ratios (with respect to the same quantities for $\mathrm{C}^{6+}$), as a function of the projectile charge, are better reproduced by this alternative approach. We show that low energy electron excitation is responsible for the deviation from the $Q_P^2$ scaling. We also analyse the effect of the transport on the primary electrons. This distorted wave approach successfully explains the shape of the ratio of energy differential spectra for two different $Q_P$ obtained in earlier experiment for Al and C. Furthermore, we predict a different behaviour of the forward and backward electron emission with respect to $Q_P$ in qualitative agreement with experimental results.

**PACS.** 79.20.Ap Theory of impact phenomena; numerical simulation - 34.50.Bw Energy loss
and stopping power - 34.50.Dy Interactions of atoms and molecules with surfaces; photon and electron
emission; neutralization of ions

## 1 Introduction
Since the pioneering work of Bohr [2] and Lindhard [3], ion penetration in solids received a lot of interest. The case of swift heavy ions covers a wide area of physical processes. It ranges from projectile transport through solids [4] with particular signature of solid state effects on projectile pop-ulation to target modifications like defect creation [5] or target particle ejection into the vacuum [6]. Among all of these phenomena, electron emission plays a central role since it reflects the projectile energy loss via electronic ex-citation and is therefore a precursor for all effects taking place at larger time scale.

The case of swift light ions impinging on metals re-ceived a particular interest both experimentally [7] and theoretically as a prototype which exhibits most of the key features of electron emission [8,9]. From these studies, we learn that electron emission is a rather complex phe-nomenon, which can be regarded as a two step process. The first step, often called primary ionisation, consists in the population of target excited electronic states induced by the projectile. It takes place at very short times and is obviously intimately related to projectile energy loss. The second step consists in the transport of the electrons in ex-cited states of the target and their emission into vacuum. During the course of their transport, the primaries can generate secondary electrons in a cascade process increas-ing the total number of excited electrons [10]. A direct con-sequence of the transport is that a lot of details about the primary ion-solid interaction are lost. In some cases, this interaction can be traced back (e.g. for the convoy, Auger or binary encounter electron peaks), while the dominant low-energy electron contribution is strongly modified. The whole process has been modelled by Monte Carlo simula-tion and can be regarded as a numerical resolution of a master phase space equation governing the electron emis-sion process [11,12].

$^{\mathrm{a}}$ Now at: Philips Automotive Lighting-BCA Chartres, 20 rue Rabuan de Coudray, BP 319, 28006 Chartres Cedex, France.
$^{\mathrm{b}}$ e-mail: rothard@ganil.fr

Studies with swift heavy ions are scarce. Indeed, the complexity of the phenomena increases since heavy ions can induce large perturbations in the target. The few proposed models seem not consistent with recent experimental data obtained with highly charged ions [1,13,14]. In particular: (i) the backward yield $(\gamma_{B})$ over stopping power (Se) ratio $\Lambda$ depends on the projectile charge $Q_{P}$ [1]; (ii) the forward over backward yield ratio $\gamma_{F} / \gamma_{B}$ increases with the projectile charge [14]; (iii) the ratio of two spectra recorded at the same velocity $v_{P}$ for different $Q_{P}$ shows that the high energy part follows more or less a $Q_{P}^{2}$ law while the low energy part somewhat saturates [15,16]; and (iv) this ratio exhibits a puzzling step-like feature at the Auger threshold of the core electrons [15-17]. All of this experimental facts deserve to be considered in a unified theoretical approach. It is the aim of this paper to investigate theoretically the behaviour of electron emission when the projectile charge increases from 1 to 39 at a fixed projectile velocity $v_{P}=19$ a.u. (an energy corresponding to9.2 MeV/u). For this system, a complete set of experimental data exists [1].

Our strategy can be summarised as follows. We shall concentrate on primary electron production and show that the standard perturbation theory, known as linear response theory, cannot reproduce the projectile charge dependence of the backward emission yield ratio obtained by comparison with the $C^{6+}$ case. A similar breakdown of this theory to reproduce the stopping power ratio is a clear evidence that it does not accurately describe the primary excitation. Furthermore, a phenomenological approach recently successfully correlated the evolutions of both electron yield and stopping power with the charge of the projectile [1]. We therefore investigate here an alternative modelling of the primary process, which allows to account for high charge effects. For both models, linear and alternative, we use the same description of the transport to clearly point out the differences in modelling of the primary process. Our description of the transport is briefly presented in Section 2 without going into the very details of the model since our aim is to focus on primary effects. The modelling of primary excitation is presented in Section 3. In particular Section 3.1 recalls the important features of linear response theory and Section 3.2 presents our alternative method to account for high charge. Section 4 presents our results and provides a complete comparison of both models with each other and with available experimental data. We finally give some concluding remarks in Section 5. While not otherwise stated, the ion energy is 9.2 MeV/u, the target is an amorphous carbon foil and atomic units are used.

## 2 Monte Carlo simulation of electron transport
### 2.1 Master phase space equation
We shall work in the framework of statistical physics and we consider the phase space coordinates as stochastic variables described by a density probability function. The dynamical evolution of this probability function is generally given by the Liouville equation of the whole system [18]. Following a large number of authors in this field [8,9,19], we rather describe our system with the help of a phenomenological master equation, which we can derive under the following assumptions considering the electron emission as a two-step process. In a first step, the interaction between the projectile ion and the target liberates electrons above the Fermi energy of the target and in a second step, the excited electrons diffuse in a potential representing the solid. During their diffusion the excited electrons can ionise other target electrons giving rise to a cascade reaction. In most of the previous models [9,10,20], the interaction of the electrons with the surface barrier of the target is considered as a third step. In our case, this interaction is already taken into account by considering that the electrons move in the target potential [11,12]. We will consider the target as an inexhaustible source of electrons, i.e. we will neglect all the modifications of the electronic system due to the excitation of electrons and thus we consider that the projectile and the cascading electrons collide with a target in its ground state. This approximation is expected to be valid as long as the probability of the interaction between two excited electrons is small during transport. We assume that the transport of the electrons results from a series of stochastic collisions, and that it can be described classically on a mesoscopic scale (i.e. its position $r$ and its momentum $p$ are simultaneously well defined), whereas the collisions follow quantum mechanical rules. The collisions of the cascading electrons take place inside the target, which is delimited by a macroscopic potential $V_{0}(r)$. This potential represents the attractive background potential of the solid experienced by a test-electron. In our model we define $V_{0}(r)$ as the average potential of the solid in its ground state. It is therefore uniform inside the solid with $V_{0}(r)=V_{0}$. It vanishes outside the solid, i.e. $\lim _{r \to+\infty} V_{0}(r)=0$. Our only assumption about the shape of $V_{0}(r)$ is that it vanishes smoothly on a microscopic scale. In such a case the transmission through the surface barrier is well reproduced by a classical calculation [12].

Since the projectile ions considered in this work are heavy $(Z_{P}>6)$ and fast $(v_{P}>v_{1 s}$ , with $v_{1 s}$ the target $1 s$ orbital velocity), they can be assumed to propagate along an unperturbed straight line with a constant velocity $v_{P}$ . Moreover, we will neglect any projectile charge changing from target electron capture and projectile electron loss. This is a reasonable assumption for the projectiles considered in this work for which the incident charge is chosen as close as possible to the equilibrium charge $Q_{P}$ , which is itself very close to the atomic number $Z_{P}$ [1]. Therefore, the phase space distribution function may be integrated over the projectile coordinates and the projectile appears only as a source term in the following master equation:

$$
\begin{aligned}
\frac{\partial f}{\partial t}+\mathbf{p} \cdot \nabla_{\mathbf{r}} f-\nabla_{\mathbf{r}} & V_{0} \nabla_{\mathbf{p}} f= \\
& -k(\mathbf{p}) f+\int \mathrm{d} \mathbf{p}^{\prime} K\left(\mathbf{p}, \mathbf{p}^{\prime}\right) f\left(\mathbf{p}^{\prime}\right)+S(\mathbf{p}, t) \quad(1)
\end{aligned}
$$

where $f(\mathbf{r}, \mathbf{p}, t)$ is the number of excited electrons at the phase space coordinate $\mathbf{x}=(\mathbf{r}, \mathbf{p})$ at time $t$. Here, $k(\mathbf{p})$ is the probability per unit of time that an electron at $\mathbf{p}$ changes its linear momentum due to collisions, $K(\mathbf{p}, \mathbf{p}')$ is the probability per unit of time that an electron with momentum $\mathbf{p}'$ produces an electron with momentum $\mathbf{p}$ either by its own deflection and energy loss or by inducing secondary electrons. $S(\mathbf{p}, t)$ denotes the number of electrons liberated per unit of time with a momentum $\mathbf{p}$ at time $t$, due to the interaction between the projectile and the target. The left-hand side contains the drift term and, in particular, the electron interaction with the surface. The above equation holds for the entire phase space and the collision kernels $k(\mathbf{p})$ and $K(\mathbf{p}, \mathbf{p}')$ vanish outside the solid.

From the distribution function $f(\mathbf{r}, \mathbf{p}, t)$, we obtain:
$$
\frac{\mathrm{d}^{3} \gamma}{\mathrm{d} p^{3}}=\lim _{t \rightarrow+\infty} \int_{\text {out }} \mathrm{d} \mathbf{r} f(\mathbf{r}, \mathbf{p}, t)
\tag{2}
$$
where $\mathrm{d}^{3} \gamma / \mathrm{d} p^{3}$ is the triply differential yield (with respect to the three momentum components) and the integration runs over the exterior of the target slab under consideration. Doubly differential, singly differential and total yields are then obtained by successive integration. This expression is the outgoing flux of electrons and it can be reduced either to the backward or to the forward outgoing flux to get the forward and backward yields, respectively. A schematic representation of the interaction geometry is depicted in Figure 1a. The mathematical transformation that relates the solution of equation (1) to the source term $S$ is linear. The linearity comes from our hypothesis of a small perturbation, which allows one to separate transport and source terms. Hence, any scaling laws about $S$ apply as well on the electron yields.

The master equation may be handled in several ways. A well-suited choice is a Monte Carlo (MC) simulation [10,11,21], which does not require any further assumptions and gives the solution of the above 7-dimensional linear master equation, in the limit of infinite sampling [12]. In the simulation, the particles are followed from the entrance of the ion in the solid until the electrons leave the solid or until their energy becomes so small that they cannot exit the solid potential anymore (i.e. a negative energy with respect to vacuum level). The interaction times, or the equivalent electronic mean free paths, are sampled using a Poisson law according to our model, for which: (i) the stochastic forces deriving from the collision kernels $k(\mathbf{p})$ and $K(\mathbf{p}, \mathbf{p}')$ depend on the electron momentum, but do not depend on the position of the electron inside the target and (ii) the excited electrons evolve in an uniform potential inside the target and therefore do not experience any acceleration which could change their mean free paths [12].

We consider a target of amorphous carbon with an atomic density of 0.0148 a.u. $(2 \mathrm{~g} / \mathrm{cm}^{3})$. Energies are given with respect to the vacuum. The position of the Fermi level is obtained from the work function of graphite taken at 0.173 a.u. (4.7 eV) below the vacuum level [22]. The potential inside the target is taken to be $V_{0}=-0.700$ a.u. (19 eV), and gives an overall agreement between experiment and theory [11]. Our modelling of the solid is depicted schematically in Figure 1b.

![](./images/812391120037216256_1.jpg)

### 2.2 Electron kernels

We shall present in this section the kernels we use in our calculations, for which physical justifications were discussed elsewhere [9-12,20,23]. These kernels are known to give satisfactory results for electron transport above a few keV and they are commonly used for secondary electron emission studies [9-12,20,23]. We first assume that our kernel is separable into three parts, corresponding to: (i) elastic collisions with target atoms, (ii) inelastic collisions with $1 s$ core electrons of the carbon atoms and (iii) inelastic collisions with the valence band electrons.

For the elastic collisions we calculate the corresponding kernel $K_{\mathrm{el}}$ from an effective potential constructed from the electronic density of a carbon atom [11,24] and a suitable exchange potential [25]. It takes into account the presence of the nearest neighbours and is spherically averaged for the sake of simplicity [11]. Since we are interested in low-energy as well as high-energy electrons, we used the phase shift analysis [26] to generate the values of $K_{\mathrm{el}}(q)$, where $q$ is the momentum exchange in an elastic collision. The corresponding interaction does not give rise to any electron multiplication.

The interaction with the target core electrons is treated like an electron-atom interaction. The solid state effect accounted for is the excitation threshold $S_K =$ 10.44 a.u. (284 eV) that corresponds to the solid excitation threshold rather than to the atom ionisation threshold. For electron transport, $1s$-electron excitation does not need to be described with high precision and thus, we shall adopt a simple formulation of $K_{1s}$ deduced from Gryzinski's formulae for atom ionisation cross-section [27]. We also account for the Auger process, which represents 99.7% of the electron-hole recombination process for the $1s$-shell of carbon. Both, the "filling hole" electron and the Auger electron initial energies are uniformly sampled between the bottom and the top of the valence band, and the Auger electron velocity distribution is considered to be isotropic. Finally, the net result of the interaction with $1s$-electrons is to add two more electrons to the cascade.

For the transport process, the interaction with the valence band electrons of the target largely dominates the interaction with the core electrons, due mainly to two reasons. First, it is easier to ionise a valence electron, for which the binding energy is of the order of 0.5 a.u. (13.6 eV), than a core electron for which the binding energy is of around 10 a.u. Second, even at the earliest time of its development, the cascade is mostly constituted of low energy electrons (lower than 50 eV) for which it is energetically impossible to ionise $1s$ electrons. For a solid target, the electron interaction with valence electrons differs from electron-atom collisions because of collective effects such as plasmon excitation [8,28]. Therefore, to describe this interaction we use the dielectric response theory, which takes into account the collective effects. We shall give more details about this process in Section 3.1. Since we assume that electron-hole recombination in valence band does not give rise to appreciable changes in the cascading process (we do not include them in our simulation), each interaction with the valence electrons increases by one the number of cascading electrons. It is important to note that the absolute magnitude of the electron yield is sensitive to the choice of the dielectric response function. The results presented in this paper were all obtained with the response function as given by Ashley [29]. We have checked that using another choice for the response function leaves unchanged the ratios presented in Section 4.

## 3 Source terms
From now on, we shall assume that $S(\mathbf{p}, t)$ is constant in time. The generalisation to a time dependent source term is straightforward. As for the electron kernels, it is customary to split the source term $S(\mathbf{p})$ into a valence contribution $S_{\text{val}}(\mathbf{p})$ and the inner-shell contributions. In the case of carbon, the inner shells reduces to the $1s$ shell, so that we have:
$$
S(\mathbf{p})=S_{\text{val}}(\mathbf{p})+S_{1s}(\mathbf{p}), \tag{3}
$$
where $S_{1s}(\mathbf{p})$ stands for the $1s$ contribution. We will compare two approximations for $S_{\text{val}}$, namely the Linear Response Theory (LRT) and the Continuum Distorted (CDW) Wave Eikonal Initial State (EIS) approximation, denoted by $S_{\text{val}}^{\text{LRT}}$ and $S_{\text{val}}^{\text{CDW}}$, respectively. In the following we will use the CDW-EIS formalism presented below for $1s$ interaction, except when otherwise stated. The model which combines the linear response theory with the CDW-EIS formalism for $1s$ interaction will be referred to as the "dielectric model".

### 3.1 Linear response theory for valence electrons
The valence electrons of a solid sample can be regarded as an electron gas [8-10,28]. Its interaction with an external charge has been studied by numerous authors [30-32] and can be characterised by a response function of the target electrons in the limit of the first-order Born approximation. The response function, which is an intrinsic property of the material, determines the characteristic energy and momentum loss spectra of the projectile, or in an equivalent way the momentum and energy gain for the valence electrons. In particular, it accounts for collective effects and their characteristic features observed in energy loss spectra [30]. However, it gives a priori no information how such an energy and momentum gain, being essentially a collective effect, could generate single electron excitations as it is assumed in most theories about secondary electrons emission [8-10,22,28]. Following Ritchie [33], we will assume that the excitation of the medium generates a transient wake potential, which can be decomposed into a sum of elementary excitations with well-defined momentum and frequency. Each elementary excitation is then a sum, over all the target electrons, of mono-electronic operators and each of these mono-electronic operators introduces mono-electronic transitions that can be assimilated to a statistical set of single electron-hole pair excitations in the medium [28,33].

To be consistent, the whole time evolution of the target electrons should be followed, but this would lead to very complicated calculations. For the sake of simplicity, we shall therefore assume that the wake field is applied to a material in its ground state. In other words, each target electron is regarded as a test charge, which feels both the external unscreened field of the incident particle and the screening field corresponding to the polarisation of the surrounding target atoms. We also assume that the final electronic state can be approximated by a plane wave to make the calculation easier. Then, for a bare ion of charge $Q_P$ and velocity $v_P$, the following expressions are obtained [11,12,33]:
$$
K(q, \omega)=\frac{2 Q_{P}^{2}}{\pi v_{P} q} \operatorname{Im}\left[-\varepsilon^{-1}(q, \omega)\right] \tag{4}
$$

$$
\begin{aligned}
S_{q, \omega}(\mathbf{k})= & 2 \pi\left|V_{q, \omega}\right|^{2} \int \mathrm{d} \omega_{i} \rho_{S}\left(\omega_{\mathbf{k}}\right) \rho_{S}\left(\omega_{i}\right) \\
& \times \chi_{\omega_{i}}(\mathbf{k}-\mathbf{q}) \delta\left(\omega_{i}-\omega_{\mathbf{k}}+\omega\right)
\end{aligned} \tag{5}
$$

$$
\int \mathrm{d}^{3} \mathbf{k} S_{q, \omega}(\mathbf{k})=K(q, \omega) \tag{6}
$$

where $q$ and $\omega$ are the momentum and energy loss respectively, $\mathbf{k}$ and $\omega_{\mathbf{k}}$ are the momentum and energy of the ejected electron respectively, and $\omega_i$ its energy before the collision. $V_{q,\omega}$ is the screened Coulomb potential describing the interaction between the projectile and the target electron, which is proportional to $Q_P^2$. Within our approximation, all the information is provided by the response function $\varepsilon^{-1}(q,\omega)$ (which is adjusted to experimental results), the energy density of state $\rho_S$ and the initial density of state in momentum space $\chi_{\omega_i}$ (which is defined as the momentum distribution averaged over all the electronic states of energy $\omega_i$). Further, we assume that $\chi_{\omega_i}$ can also be adjusted to experimental results [11,12]. The connection with equation (3) is simply obtained by:

$$
S_{\text{val}}^{\text{LRT}}(\mathbf{k}) = \int \mathrm{d}\omega \int \mathrm{d}q S_{q,\omega}(\mathbf{k}). \tag{7}
$$

We emphasize that the expression (5) for the source term is strictly proportional to $Q_P^2$ via $V_{q,\omega}$. For our purpose, this is the main result of linear response approach.

### 3.2 CDW-EIS approximation for core and valence electrons
The ideal "ansatz" for the source term would be to develop a full non-linear response theory for a solid. If this is not possible, the entire solid may be represented by a reduced size cluster, large enough to keep track of condensed matter effects. Although such kind of calculations are now available for some simple cases [34-36], it seems to be a very cumbersome task to perform explicitly the calculation for the large-velocity projectile considered in this work (and hence large velocity ejected electrons). On the other hand, ion-atom collision theories are well developed in this velocity regime and we shall model the solid with the help of an *effective-atom* as it is described in the following. Indeed, large deviations from $Q_P^2$-scaling have been observed for ionisation in ion-atom collisions at large impact velocity [37], in particular for helium targets [38]. This so-called *saturation effect* has been also observed for excitation in a velocity regime close to 19 a.u. [39]. The deviation from the $Q_P^2$-scaling is attributed to a *two-centre effect* [40], which is a signature that the electron is ejected in the combined fields of the projectile and target. For relatively large projectile charge $Q_P$, such that the ratio $Q_P/v_P$ no longer is small compared to unity, this behaviour is quite well reproduced by the CDW-EIS (Continuum Distorted Wave-Eikonal Initial State) theoretical approximation [41]. Our proposal is to search if the *two-centre effect*, which takes place in ion-atom collisions, is also present in ion-solid collisions. In the latter case, we shall call this *saturation effect* a *non-linear effect*, to stress that our approach goes beyond the linear theory based on the dielectric formalism. Moreover, one of the characteristic features of the *two-centre effect*, namely the convoy electron emission at $0^\circ$, has been also observed for ion-solid interactions [42].

In our case, the ratio $Q_P/v_P$ varies from a value of $2 \times 10^{-3}$ for a proton (weak perturbation) up to a value of 2 for $\text{Mo}^{39+}$ (strong perturbation) at 9.2 MeV/u. Like the linear response theory presented above, the CDW-EIS approximation is a perturbation theory, but where the full incoming ion potential is no longer taken as the perturbation [40]. In fact, the perturbation is taken in the kinetic energy, and the asymptotic Coulombic tail of the ion potential is directly included in the representation of the initial electron state, by choosing a multiplicative distortion of the initial bound wave function which corresponds to an eikonal approximation (Eikonal Initial State: EIS) of the electron-projectile continuum. This EIS distortion allows to obtain a normalised initial distorted wave function, in contrast to the case of using a more complete electron-projectile Coulomb continuum factor [43]. The target electrons are treated independently according to the frozen core approximation [41]. It is worth noting here that we account for multiple process [44] within the independent electron approximation. In particular, the calculated cross-sections correspond to the *total number* of electrons ejected from a target atom per unit of incident flux. It fully accounts for multiple ionisation and is therefore identical to the net ionisation cross-section [37,45].

In our CDW-EIS calculations the undistorted initial bound state is described by a multiple-zeta Rothaan Hartree Fock wave function for carbon [24]. We accounted also for solid state effects by considering a $sp^2$ hybridised initial state [46]. We included one $\pi$ and three $\sigma$ states with an energy corresponding to the band median energy ($-0.291$ a.u. and $-0.585$ a.u., respectively). The resulting absolute total yield and stopping power for protons and $\text{Mo}^{39+}$ do not present any significant improvement with regard to the non-hybridised model of an isolated atom for which we have two $2s$ and two $2p$ electrons with energy $-0.740$ a.u. and $-0.310$ a.u., respectively. In both cases, the total average energies are very close ($-0.512$ a.u. for hybridised model and $-0.525$ a.u. for the other one). We conclude that hybridisation plays a secondary role in our case. The final state is obtained as the double product of a plane wave and two continuum factors (Continuum Distorted Wave State: CDW), one centred at the target and corresponding to an effective potential $Z_T^*/x$, and another centred at the bare projectile and corresponding to a potential $Q_P/s$ ($\mathbf{x}$ and $\mathbf{s}$ being the electron-target nucleus and electron-projectile position vectors, respectively). We used for $Z_T^*$ the definition proposed by Belkic *et al.* [47], where $Z_i^* = \sqrt{(-2u_i n_i^2)}$ for a given $i$-level, with binding energy $u_i$ and principal quantum number $n_i$. For the $2s$ and $2p$ levels, we have $Z_{2s}^* = 2.44$ and $Z_{2p}^* = 1.57$, respectively. We have verified that this choice of effective charges gives the best representation of the stopping power. The effective atom model is schematically depicted in Figure 1b.

With respect to the linear response theory, the CDW-EIS calculation, which neglects solid state collective effects in the primary collision, is no longer proportional to $Q_P^2$. It might be therefore able to reproduce the experimental observation, as it does for ion-He collisions. An explicit calculation of collective effects beyond the first Born perturbation theory is still lacking and it would be very

cumbersome. Moreover the influence of this primary col-
lective effects on electron emission (in particular on an
integrated quantities such as the total yield) is difficult
to estimate precisely, because the transport completely
swamps out the fine detail of the primary ion-target in-
teraction. We emphasize that plasmon excitation is still
present in transport, and collective effects are therefore
accounted for in their main contribution to electron emis-
sion.

The cross-section for liberating an electron with mo-
mentum $\mathbf{k}$ has to be calculated in a consistent way with
the electron transport description [12]. For an isotropic
medium, and considering that the electron energy must
be the same in the solid and in the atom, the number of
electron emitted per unit of time becomes:

$$
\begin{aligned}
S_{\text {val }}^{\mathrm{CDW}}(\mathbf{k}) & =v_{P} \rho_{\mathrm{AT}} \sum_{i=2 s, 2 p} \frac{\partial^{3} \sigma_{i}}{\partial k^{3}} \\
& =v_{P} \rho_{\mathrm{AT}} \sum_{i=2 s, 2 p} \frac{\partial^{3} \sigma_{i}}{\partial k^{\prime 3}} \sqrt{1+2 \frac{V_{0}-U_{S}}{k^{2}}},
\end{aligned}
\tag{8}
$$

with

$$
\frac{\mathbf{k}^{2}}{2}+V_{0}=\frac{\mathbf{k}^{\prime 2}}{2}+U_{S}
\tag{9}
$$

where $\mathbf{k}$ is the momentum of the electron inside the solid
and $\mathbf{k}'$ the momentum of the electron leaving the atom.
$\rho_{\mathrm{AT}}$ is the atomic density of the solid. $V_{0}$ is the uniform
background potential of the solid as defined in Section 2.1.
$U_{S}$ is an arbitrary potential energy in which the effective
atom is placed to mimic the solid. $U_{S}$ belongs necessarily
to $[V_{0}, 0]$. For low density solids with large average inter-
atomic spacing such as amorphous carbon $U_{S} \sim 0$. By
changing $U_{S}$, we have tested that the variation of the yield
with respect to $Q_{P}$ is not sensitive to the fine details of
the atomic model embedding in the solid. In the following,
we refer the model that includes a CDW-EIS formalism
for both the valence and the $1s$ levels to as the "effective
atom model".

## 4 Results and discussions

### 4.1 Effective atom model qualification

Before investigating the effects of increasing the projectile
charge $Q_{P}$, it is necessary to qualify the effective atom
model with respect to the dielectric model, which has
been widely used to model electron emission, and which
is known to give good results for weak perturbation when
compared to experiment [7-11,48]. Therefore we compare
in Figure 2 two energy differential spectra of primary elec-
trons ejected in backward direction for a 9.2 MeV proton
and for foil thickness of $4.0\ \mathrm{\mu g/cm^{2}}$. These spectra include
only the valence electron contribution. They were calcu-
lated with the dielectric formalism and with the effective
atom model in the energy range from $-10$ to $50$ eV, where
differences between both models are expected to signifi-
cant. The energy is referenced with respect to the vacuum
level. Comparing both theoretical models, we first remark
that no primary electron is produced under the vacuum
level when the atomic approximation is used. This be-
haviour is due to our neglect of the excitation mechanism
and to the energy definition equation (8) that we used in
the atomic model to calculate the source term. Second,
we notice the structure around 10 eV for the dielectric
formalism. This energy corresponds approximately to the
middle of the valence band ($\sim 15$ eV) shifted by the aver-
age plasmon energy ($\sim 25$ eV). It characterises the damp-
ing of plasmons and hence does not appear in the atomic
approach where no collective effects are included. Finally,
for a similar stopping power (see Tab. 1 for $\mathrm{H^{+}}$), the en-
ergy distribution is different for the atomic model and
the dielectric formalism because of the collective excita-
tions, which suppress low energy transfer to the benefits
of higher energy transfer in the energy range 0 to 50 eV.

![](./images/812391120037216256_2.jpg)

Fig. 2. Backward energy differential source term (primary electron spectrum) for a 9.2 MeV/u proton. Only the valence electron contribution is included.

![](./images/812391120037216256_3.jpg)

Fig. 3. Backward energy differential yield (emitted electron spectrum) for a 9.2 MeV/u proton. The differential yield includes both valence and $1s$ electron contributions. The $1s$ electron contribution including Auger electrons is shown sepa- rately.

**Table 1.** Absolute electron yields and stopping powers for experiment, atomic model and dielectric model. Tabulated stopping power values were taken from references [50,51] for protons. $^{a}$ The experimental yield for $\text{H}^{+}$ is extrapolated from experimental results at various lower energies [54,55] by scaling with the stopping power. $^{b}$ The experimental yield for $\text{S}^{16+}$ is extrapolated from experimental results at 8.7 MeV/u by scaling with the stopping power.

<table>
  <thead>
    <tr>
      <th>Ion</th>
      <th colspan="3">$\gamma_{B}$</th>
      <th colspan="3">$\mathrm{d}E/\mathrm{d}x$ (keV/nm)</th>
    </tr>
    <tr>
      <th></th>
      <th>Exp.</th>
      <th>Atomic</th>
      <th>Diel.</th>
      <th>Tab.</th>
      <th>Atomic</th>
      <th>Diel.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{H}^{+}$</td>
      <td>$0.12^{a}$</td>
      <td>$8.14 \times 10^{-2}$</td>
      <td>$8.34 \times 10^{-2}$</td>
      <td>$8.66 \times 10^{-3}$</td>
      <td>$8.53 \times 10^{-3}$</td>
      <td>$8.13 \times 10^{-3}$</td>
    </tr>
    <tr>
      <td>$\text{C}^{6+}$</td>
      <td>$3.6$</td>
      <td>$2.83$</td>
      <td>$3.00$</td>
      <td>$3.07 \times 10^{-1}$</td>
      <td>$3.07 \times 10^{-1}$</td>
      <td>$2.94 \times 10^{-1}$</td>
    </tr>
    <tr>
      <td>$\text{S}^{16+}$</td>
      <td>$24.6^{b}$</td>
      <td>-</td>
      <td>-</td>
      <td>$1.94$</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>$\text{Ca}^{20+}$</td>
      <td>$32.1$</td>
      <td>$28.3$</td>
      <td>$31.8$</td>
      <td>$2.88$</td>
      <td>$3.23$</td>
      <td>$3.18$</td>
    </tr>
    <tr>
      <td>$\text{Ni}^{27+}$</td>
      <td>$45.0$</td>
      <td>$49.5$</td>
      <td>$57.0$</td>
      <td>$5.13$</td>
      <td>$5.71$</td>
      <td>$5.72$</td>
    </tr>
    <tr>
      <td>$\text{Mo}^{39+}$</td>
      <td>$82.3$</td>
      <td>$96.3$</td>
      <td>$117$</td>
      <td>$9.91$</td>
      <td>$11.33$</td>
      <td>$11.66$</td>
    </tr>
  </tbody>
</table>

In Figure 3, energy differential yields of backward emitted electrons for 9.2 MeV protons are presented for the atomic model and the dielectric formalism. The calculation was also performed for $4.0\ \mu\text{g/cm}^{2}$ foil thickness and includes both the valence and the $1s$ shell contributions. In contrast with the corresponding primary spectra shown in Figure 2, the curves are similar both in shape and in intensity. This result illustrates how much the electron transport and the potential barrier of the foil modify the primary spectra. In particular, the structure around 10 eV in the primary spectrum obtained with the dielectric model and due to collective effects is strongly modified, and the low energy peak in the primary spectrum obtained for atomic formalism is almost suppressed because the very low energy electron have a very low chance to escape the foil. The similarity of the curves in Figure 3 shows that the atomic model works quite well (as well as the dielectric model for $\text{H}^{+}$) in describing the details electron emission.

### 4.2 Total yield and stopping power

The experimental results for electron yields were obtained at the medium energy facility at GANIL for a set of isotachic ions ($v_{P}=19$ a.u.). The experiment was performed under ultra high vacuum (UHV) conditions with $200\ \mu\text{g/cm}^{2}$ thick amorphous carbon targets on copper backing. They were sputter cleaned with a $500\ \text{eV}\ \text{Ar}^{+}$ ion beam. The experimental apparatus and procedure were described previously [1,46]. The error bars for the absolute total yields are of the order of 10%. The stopping power values were obtained from several compilations of experimental values [50–52]. The agreement between the different compilations is excellent in this energy range. The relative error bars provided by the authors are within 5% [50] or less for protons [51,52]. These data are strictly valid for projectiles at charge equilibrium, *i.e.* when the projectile charge state distribution becomes stationary [53], while in our calculations we simply consider a bare ion with the corresponding average charge. Nevertheless, the incoming projectile charge is very close to the equilibrium charge state and the stopping power deviation is found to be less than 2% for $\text{Mo}^{39+}$ ions for which the equilibrium charge state is estimated to be 39.2 [1,53]. The absolute experimental and theoretical results are summarised in Table 1.

The experimental $\gamma_{B}$-value for $\text{H}^{+}$ is extrapolated from data at 1 MeV [54] and data at 6.2 MeV [55] by means of a linear scaling with the stopping power, which has been shown to be valid for protons in this energy range [48].

For the whole range of charge presented here, the experimental and theoretical values are comparable in magnitude. For protons, for which perturbative theories are expected to give better results, the atomic model gives results comparable with the dielectric formalism. For both theories, Se underestimate the tabulated value by 5% or less, and $\gamma_{B}$ underestimates its experimental counterpart by a factor 1.5 approximately. This difference is quite likely due to the description of low energy electron transport based on perturbation theory that underestimates the electron mean free path. The agreement between tabulated and calculated stopping power confirms this interpretation.

In order to see the variation with the projectile charge $Q_{P}$ better, and since the data for protons were obtained indirectly from separate experiments, we define the normalised yield $R_{\gamma}$ with respect to the $\text{C}^{6+}$ projectile:
$$
R_{\gamma}(Q_{P}) = \frac{6^{2}\gamma_{B}(\text{X}^{Q_{P}+})}{Q_{P}^{2}\gamma_{B}(\text{C}^{6+})} \,. \tag{10}
$$

In the same way, we define the normalised stopping power $R_{\mathrm{d}E/\mathrm{d}x}$ as:
$$
R_{\mathrm{d}E/\mathrm{d}x}(Q_{P}) = \frac{6^{2}\mathrm{d}E/\mathrm{d}x(\text{X}^{Q_{P}+})}{Q_{P}^{2}\mathrm{d}E/\mathrm{d}x(\text{C}^{6+})} \,. \tag{11}
$$

$R_{\gamma}$ and $R_{\mathrm{d}E/\mathrm{d}x}$ are presented in Figures 4 and 5 respectively, for experiment and for both of the theoretical models. The slight decrease obtained with the dielectric formalism in Figures 4 and 5 comes from the use of CDW-EIS cross-sections describing the interaction of the projectile with the target $1s$-electrons. The atomic model reproduces both $R_{\gamma}$ and $R_{\mathrm{d}E/\mathrm{d}x}$ in a better agreement with experiments than the dielectric model does. It is interesting to note that, either experimentally or theoretically, the decrease of $R_{\gamma}$ is more pronounced than the decrease of $R_{\mathrm{d}E/\mathrm{d}x}$. This shows that the electron transport magnifies the saturation effect already observed for the primary interaction *via* the stopping power. This is consistent with the fact that low energy electron production

![](./images/812391120037216256_4.jpg)

Fig. 4. Experimental and theoretical results for the normalized backward yields $R_\gamma$ versus the projectile charge $Q_P$ (see Tab. 1). For the dielectric model the $1s$ ionisation was calculated with CDW-EIS theory.

![](./images/812391120037216256_5.jpg)

Fig. 5. Tabulated and calculated normalized electronic stopping power $R_{Se}$ versus the projectile charge $Q_P$ (see Tab. 1).

saturates much more than the high energy electron production, as we shall see in the next section. Indeed, in calculating
$$
\frac{\mathrm{d} E}{\mathrm{~d} x}=v_{P}^{-1} \int \mathrm{d} \omega \frac{\mathrm{d} S}{\mathrm{~d} \omega} \omega,
$$
where $v_{P}^{-1} \mathrm{d} S / \mathrm{d} \omega$ is the differential energy loss spectrum per unit length with respect to energy loss, both backward and forward contributions are included and more emphasis is put on the high energy side of the spectrum, while the simulation shows that this high energy part contributes less to the backward yield.

In spite of the improvement brought by the atomic modelling of primary interaction, a systematic overestimation of the experimental ratios remains. It increases with the projectile charge, up to $23 \%$ for $R_{\gamma}(39+)$ and up to $11 \%$ for $R_{\mathrm{d} E / \mathrm{d} x}(39+)$. Since the quantitative variation of the stopping power ratio with respect to the charge is not completely reproduced, we can conclude that the modelling of the source term could be improved further. We emphasize that a better electron transport calculation for the cascade generation would not affect the stopping power variation and hence cannot explain this difference. A clue for understanding where this difference comes from, can be obtained by the following consideration. Since CDW-EIS theory reproduces accurately the experimental data for light target atoms such as He [41], and since for carbon the $1 s$ level contribution to $\gamma_{B}$ amounts to $25 \%$ for protons (including Auger electrons and their cascades) it is conceivable that the $1 s$ ionisation is overestimated by CDW-EIS theory for large projectile charge. Recent measurements of Auger electron spectra [17] giving access to $1 s$ ionisation probability for carbon foils are in favour of this interpretation.

### 4.3 Forward/backward differential energy spectra

From energy differential spectra we can obtain more information about the observed reduction effect with respect to $Q_{P}^{2}$ scaling. In particular, we will show in this section that this effect takes place on the low energy side of the spectrum for backward and forward-emitted electrons.

In order to point out the asymmetry between backward and forward-emitted low energy electrons, we calculated energy differential spectra with a $4.0 \mu \mathrm{g} / \mathrm{cm}^{2}$ thick foil. For such a thickness and at $9.2 \mathrm{MeV} / \mathrm{u}$, the cascades of low energy electrons are almost fully developed, but the fast electron cascades have hardly influenced the forward spectrum yet [48]. Figure 6 presents the normalised energy differential source ratio for molybdenum $(Q_{P}=39)$:
$$
S_{s p B, s p F}(39, E)=\frac{1}{39^{2}} \frac{\frac{\mathrm{d} S_{B, F}}{\mathrm{~d} E}(39+)}{\frac{\mathrm{d} S_{B, F}}{\mathrm{~d} E}(1+)}
\tag{12}
$$
for backward and forward-ejected electrons obtained with the atomic model. $S_{s p B}$ and $S_{s p F}$ are represented by dashed lines in Figure 6. Both curves include the valence and $1 s$ contribution to the source, and they correspond to what would be typically observed for collisions with atoms. The thin dotted line stands for any theory scaling as $Q_{P}^{2}$ and does not exhibit any characteristic feature. In contrast, we can observe several features characterising the normalised source ratio for CDW-EIS modelling. The most significant of them is the strong asymmetry between backward and forward direction due to the very strong perturbation induced by the $\mathrm{Mo}^{39+}$ projectile. The normalised backward source term $S_{s p B}$ is about two times lower than its forward counterpart $S_{s p F}$. This difference is even larger on the high-energy side where $S_{s p B}$ decreases down to 0.3. This difference in magnitude between $S_{s p F}$ and $S_{s p B}$ illustrates nicely the "forward focusing effect" [14], that is, when $Q_{P}$ increases, $S_{s p B}$ decreases more than $S_{s p F}$.

![](./images/812391120037216256_6.jpg)

Fig. 6. For molybdenum ($Q_P=39$): calculated ratio of the energy differential source $S_{spF}(Q_P)$ and $S_{spB}(Q_P)$ (dashed lines); calculated ratio of the energy differential yield $R_{spF}(Q_P)$ and $R_{spB}(Q_P)$ (solid lines); calculated ratio of spectrum obtained from a $Q_P^2$ scaling (thin dotted line). Forward and backward contributions to the spectra are separated. Normalised calculated ratio of the $1s$ inverse mean free path (point $a$).

We can distinguish 4 different energy regions in which several features appear due to the enhancement of $Q_P$. (i) Above 280 eV, the saturation does not affect seriously the fast electron emission in the forward direction and $S_{spF} \approx 1$. A closer inspection shows that the respective forward contribution at 280 eV of the $1s$ and valence levels are $3.6 \times 10^{-3}$:$1.9 \times 10^{-2}$ for proton and 4.2:31.3 for $Mo^{39+}$. At 500 eV the respective contributions are: $2.2 \times 10^{-3}$:$1.0 \times 10^{-2}$ for proton and 2.9:15.1 for $Mo^{39+}$. Therefore, in this region, $S_{spF}$ is dominated by electrons ejected from valence band, for which the cross-section scales approximately as $Q_P^2$. In contrast, $S_{spB}$ decreases above 280 eV. The reason is the increasing $1s$ contribution to $S_{spB}$ together with the stronger saturation of the $1s$ electron ejection cross-section with respect to the valence cross-section. (ii) We observe a strong dip around 260 eV in the forward direction and a shallow maximum in the backward direction. The half-width of this features is equal to the energy width of the valence band (20 eV). The minimum of the dip in forward direction and the maximum of the bump in the backward direction reach almost the same value because, at this energy, the spectrum is dominated by the isotropic KVV Auger electron emission. Since the fluorescence yield of the carbon $1s$ level is extremely small, the KVV Auger electron production cross-section is almost equal to the $1s$ ionisation cross-section. Therefore in this region, the source ratio is approximately equal to the normalised total $1s$ inverse mean free path ratio (see point $a$ in Fig. 6). Aside of this narrow Auger energy area, the spectrum is dominated by the valence contribution. Since the valence electron ejection cross-section in forward direction does not saturate in this region, $S_{spF}$ is higher, and consequently the Auger peak corresponds to a dip in the forward source ratio. At the opposite, the valence electron ejection cross-section in backward direction saturates slightly more than the total $1s$ cross-section, and consequently the Auger peak corresponds to a shallow peak in the backward source ratio. (iii) In the region between 20 and 240 eV, $S_{spF}$ reaches values larger than 1. This means that the projectile focuses the electron in the forward direction with an efficiency that increases with the projectile charge as observed experimentally [14]. Hence, this part of the source energy spectrum behaves in an opposite way than a saturation effect. (iv) Finally, between 0 and 20 eV, we observe a strong reduction of the low-energy electron emission in both forward and backward directions. This relative reduction plays an important role since it occurs in an energy range where the contribution to the emitted spectrum is large.

In order to observe the contribution of the transport process, we have also plotted in Figure 6 the normalised emitted-electron spectra $R_{spB,spF}$ defined in the same way:

$$
R_{spB,spF}(39,E) = \frac{1}{39^2} \frac{\frac{\mathrm{d}\gamma_{B,F}}{\mathrm{d}E}(39+)}{\frac{\mathrm{d}\gamma_{B,F}}{\mathrm{d}E}(1+)} . \tag{13}
$$

$R_{spB}$ and $R_{spF}$ are represented by continuous lines in Figure 6. The jitter is due to MC statistics. We observe that the transport tends to attenuate the asymmetry between backward and forward direction. The general behaviour is to enhance $R_{spB}$ and to lower $R_{spF}$ by mixing the contribution of $S_{spF}$ and $S_{spB}$ to produce either $R_{spF}$ or $R_{spB}$. In contrast to the source ratios $S_{spF}$ and $S_{spB}$, $R_{spF}$ and $R_{spB}$ are parallel to each other above 50 eV.

Considering the 4 energy regions defined above, we can analyse the significance of transport with respect to the projectile charge variation. (i) Above 280 eV, $R_{spF}$ is almost identical to $S_{spF}$. This is because $R_{spF}$ results from the cascades of primary electron emitted in the forward direction, which are therefore included in $S_{spF}$ at higher energy, where almost no saturation is observed. In contrast, $R_{spB}$ is much higher than $S_{spB}$, revealing the large contribution of forward primary electron included in $S_{spF}$ to the backward emission, mainly because of backscattering of these forward primary electron. (ii) The forward Auger dip and backward Auger bump are both transformed into a step-like feature between 260 and 280 eV. There is some track of the forward dip in $R_{spF}$, but the bump in $R_{spB}$ has been transformed into a step. This is, again, because of the large contribution of the forward primary emission to backward emission. (iii) Between 20 and 260 eV, $R_{spF}$ is lower than in the region above 280 eV. The same holds true for $R_{spB}$. The explanation comes from the transport of the Auger electrons that contribute significantly in this energy range, and which spread the Auger dip in $S_{spF}$ toward lower energy. A detailed analysis of the Auger contribution to the step-like feature is shown in Figure 7. We present, here, a calculation with the full primary spectrum (Auger on) and a calculation in which the Auger electrons were not included (Auger off).

![](./images/812391120037216256_7.jpg)

Fig. 7. Same as Figure 6 for a calculation including all primaries (Auger on) and a calculation without the Auger primaries (Auger off).

This figure shows clearly that the primary Auger electron is responsible for the step-like feature in $R_{spF}$ and $R_{spB}$. The step-like shape of $R_{spB}$ around the Auger energy is qualitatively in excellent agreement with the observations made independently for aluminium, copper and gold [15] and more recently for carbon [17]. This effect discussed previously in the literature in terms of track potential [16] effect is nothing but the different behaviour of the total $1s$ ionisation probability and of the energy differential ionisation probability with respect to the projectile charge $Q_{P}$, as discussed for the source term. (iv) Finally, below 20 eV, $R_{spF}$ and $R_{spB}$ have kept the behaviour of $S_{spF}$ and $S_{spB}$, i.e. they increase when the the energy increase in qualitative agreement with experiment [16,17]. This energy region contributes significantly to the saturation effect observed for $\gamma_{B}$ in Figure 4.

The asymmetry in the evolution of $R_{spB}$ and $R_{spF}$ with respect to the projectile charge, as reported in Figure 6, is large enough to be observed experimentally. We suggest performing an experimental determination of both $R_{spB}$ and $R_{spF}$ around the Auger energy, for swift projectiles and very thin targets to avoid transport effects as much as possible. Such an experimental measurement would bring one more argument in favour or against the existence of a two-centre effect in solids.

## 5 Conclusion

We studied the dependence of electron emission on projectile charge $Q_{P}$ for swift ions at a fixed velocity $v_{P} =$ 19 a.u. We reminded that the linear response modelisation of the projectile target interaction fails to reproduce both the backward yield $\gamma_{B}$ and stopping power variations with $Q_{P}$. We then modelled this interaction with the help of an atomic model within the CDW-EIS formalism, which reproduces the $Q_{P}$ saturation effect observed in ion-atom collision. This latter model can reproduce to some extent the energy levels of the solid and it gives better results concerning various aspects of the electron emission. The fine details (such as the hybridisation) play a little role in changing the absolute yield $\gamma_{B}$ and stopping power values, but the variations with $Q_{P}$ are rather insensitive to it.

The main result of our study is that the relative variation of both the yield and the stopping power with the projectile charge $Q_{P}$ is much better reproduced with our effective atom model within CDW-EIS formalism than within the linear response theory. Let us note that both theories agree with each other for proton yield and they reproduce equally well the stopping power for protons. The analysis of energy differential source shows a large forward-backward asymmetry of the source term, due to the larger charge of the projectile. The transport reduces significantly this asymmetry, even for target as thin as $4\ \mu\text{g/cm}^2$, but it is still clearly observable. Our calculations allow a qualitative analysis of the experimental results obtained for several materials by various authors. Indeed, an attractive point of this model is to describe, *within a unique approach*, not only the yield evolution with $Q_{P}$ but also more refined quantities such as the $Q_{P}$-dependence of the energy differential spectra ratio. For backward electron emission, the shape of the energy differential spectra ratio around a core excitation threshold is due to the difference in the saturation between the Auger yield, which follow the total core excitation mean free path, and the differential yield around this excitation threshold, which follows the energy differential valence mean free path. Finally, a measurement of the forward and backward energy differential spectra would allow performing a sensitive test of our atomic modelisation.

Refining the comparison of our theory and experimental data, some differences still exist between the theoretical $\gamma_{B}$ dependence in $Q_{P}$ and its experimental counterpart. Since the same observation is done for the stopping power, it remains a primary effect that is not accounted for by our model. Such a primary effect could be due to a specific solid state effect such as the dynamical screening, which is not included in our atomic modelisation. Alternatively, the calculated saturation of the $1s$ ionisation cross-section could be too weak for solid carbon as indicated by preliminary experimental results. Because of the transport, this difference would be somewhat magnified, and it could be responsible for the observed difference between calculation and experiment.

In conclusion, we presented a novel numerical description of ion induced electron emission from solids, based on an atomic description of the ionisation process that allows to go beyond the linear response approximation. This theoretical approach allowed, for the first time, to understand the shape of the differential energy spectra ratio for two projectile different charge at the same velocity. The comparison with experimental yields shows that this approach allows a better description than linear models based on linear response theory.

This research was supported in part by the cooperation program SCyT (Argentina) – ECOS-sud (France), grant No. A98E02. We acknowledge the region Basse-Normandie for its financial support of the Ph.D. thesis of M. Beuve and M. Caron. We also acknowledge G. Cremer and F. Fremont for fruitful discussions about the Auger effect.

# References

1. M. Beuve, M. Caron, B. Gervais, H. Rothard, Phys. Rev. B **62**, 8818 (2000)
2. N. Bohr, Mat. Fys. Med. Dan. Vid. Selsk. **18**, 1 (1948)
3. J. Lindhard, Mat. Fys. Med. Dan. Vid. Selsk. **28**, 1 (1954)
4. J. Burgdörfer, in *The Physics of Electronic and Atomic collisions*, edited by A. Dalgarno *et al.*, AIP Conf. Proc. **205**, 476 (1989)
5. Materials under irradiation, A. Dunlop, F. Rullier- Albenque, C. Jaouen, C. Templier, J. Davenas, Trans-Tech publications, 1993
6. *Fundamental Processes in Sputtering of Atoms and Molecules*, edited by P. Sigmund, K. Dan. Vid. Selsk. Mat. Fys. Medd. **43**, 1-675 (1993); G. Betz, K. Wien, Int. J. Mass Spectrom. Ion Process. **140**, 1 (1994)
7. *Particle induced electron emission I*, edited by G. Höhler, E.A. Niekisch, Springer Tracts of Modern Physics **122** (Springer Verlag, Berlin, 1991); *Particle induced electron emission II*, edited by G. Höhler, E.A. Niekisch, Springer Tracts of Modern Physics **123** (Springer Verlag, Berlin, 1991)
8. M. Rösler, W. Brauer, Phys. Stat. Sol. (b) **148**, 213 (1988)
9. A. Dubus, J.C. Dehaes, J.P. Ganachaud, A. Hafni, M. Cailler, Phys. Rev. B **47**, 11056 (1993); J.C. Dehaes, A. Dubus, Nucl. Instrum. Meth. B **78**, 255 (1993)
10. J.P. Ganachaud, M. Cailler, Surf. Sci. **83**, 488 (1979)
11. B. Gervais, M. Beuve, M. Caron, H. Rothard, in prepara- tion
12. M. Beuve, thèse de l'université de Caen, 1999
13. G. Schwietz, G. Xiao, Nucl. Instrum. Meth. B **107**, 113 (1996)
14. H. Rothard, M. Jung, M. Caron, J.P. Grandin, B. Gervais, A. Billebaud, A. Clouvas, R. Wünsch, Phys. Rev. A **57**, 3660 (1998)
15. A. Koyama, A. Ishikawa, Y. Sasa, O. Benka, M. Uda, Nucl. Instrum. Meth. B **33**, 341 (1988)
16. A. Koyama, O. Benka, Y. Sasa, M. Uda, Phys. Rev. B **34**, 8150 (1986); A. Koyama, O. Benka, Y. Sasa, M. Uda, Nucl. Instrum. Meth. B **13**, 637 (1986)
17. M. Caron, H. Rothard, M. Beuve, B. Gervais, Phys. Scripta **T80**, 331 (1999); M. Caron, thèse de l'université de Caen, unpublished, 2000
18. L.E. Reichl, *A Modern Course of Statistical Physics* (John Wiley and Sons, New York, 1998)
19. J. Devooght, A. Dubus, J.C. Dehaes, Phys. Rev. B **36**, 5093 (1987); J. Devooght, A. Dubus, J.C. Dehaes, Phys. Rev. B **36**, 5110 (1987)
20. M. Rösler, W. Brauer, Phys. Stat. Sol. (b) **104**, 161 (1981); M. Rösler, W. Brauer, Phys. Stat. Sol. (b) **104**, 575 (1981)
21. J. Burgdörfer, J. Gibbons, Phys. Rev. A **42**, 1206 (1990)
22. R.F. Willis, B. Fitton, G.S. Painter, Phys. Rev. B **9**, 1926 (1974)
23. S. Lencinas, J. Burgdörfer, J. Kemmler, O. Heil, K. Kroneberger, N. Keller, H. Rothard, K.O. Groeneveld, Phys. Rev. A **41**, 1435 (1990)
24. E. Clementi, C. Roetti, At. Data Nucl. Data Tab. **14**, 177 (1974)
25. M.E. Riley, D.G. Truhlar, J. Chem. Phys. **63**, 2182 (1975)
26. C.J. Joachain, *Quantum Collision Theory*, 3rd edn. (North Holland, 1983)
27. M. Gryzinski, Phys. Rev. **138**, A305 (1965), Phys. Rev. **138**, A322 (1965), Phys. Rev. **138**, A36 (1965)

28. M.S. Chung, T.E. Everhart, Phys. Rev. B **15**, 4699 (1977)
29. J.C. Ashley, J.J. Cowan, R.H. Ritchie, V.E. Anderson, J. Hoelzl, Thin Sol. Films **60**, 361 (1979)
30. P. Nozières, D. Pines, Phys. Rev. **113**, 1254 (1959)
31. J.C. Ashley, C.J. Tung, R.H. Ritchie, IEEE Trans. Nucl. Sci. **NS22**, 2533 (1975)
32. P.M. Echenique, R.H. Ritchie, F. Flores, Sol. State Phys. **43**, 231 (1990)
33. R.H. Ritchie, A. Howie, P.M. Echenique, G.J. Basbas, T.L. Ferrell, J.C. Ashley, Scann. Microsc. Supp. 4, 45 (1990); R.H. Ritchie, R.N. Hamm, J.E. Turner, H.A. Wright, J.C. Ashley, G.J. Basbas, Nucl. Tracks Radiat. Meas. **16**, 141 (1989)
34. M. Gross, C. Guet, Phys. Rev. A **54**, R2547 (1996)
35. J.M. Pitarke, R.H. Ritchie, P.M. Echenique, Phys. Rev. B **52**, 13883 (1995)
36. C.A. Ullrich, P.G. Reinhard, E. Suraud, Phys. Rev. A **57**, 1938 (1997)
37. A. Cassimi, J.P. Grandin, L.H. Zhang, A. Gosselin, D. Hennecart, X. Husson, D. Lecler, A. Lepoutre, I. Lesteven- Vaisse, Rad. Eff. Def. Sol. **126**, 21 (1993)
38. J.H. McGuire, A. Müller, B. Schuch, W. Groh, E. Salzborn, Phys. Rev. A **35**, 2479 (1987)
39. X.Y. Xu, E.C. Montenegro, R. Anholt, K. Danzmann, W.E. Meyerhof, A.S. Schlachter, B.S. Rude, R.J. McDonald, Phys. Rev. A **38**, 1848 (1988)
40. P.D. Fainstein, V.H. Ponce, R.D. Rivarola, J. Phys. B **24**, 3091 (1991)
41. P.D. Fainstein, V.H. Ponce, R.D. Rivarola, J. Phys. B **21**, 287 (1988)
42. C.O. Reinhold, J. Burgdörfer, J. Kemmler, Phys. Rev. A **45**, R2655 (1992) and reference therein
43. D.S.F. Crothers, J.F. McCann, J. Phys. B **16**, 3229 (1983)
44. D. Vernhet, J.P. Rozet, K. Wohrer, L. Adoui, C. Stéphan, A. Cassimi, J.M. Ramillon, Nucl. Instrum. Meth. B **107**, 71 (1996)
45. I. Ben Itzhak, T.J. Gray, J.C. Legg, J.H. McGuire, Phys. Rev. A **37**, 3685 (1988)
46. C. Cohen-Tanoudji, B. Diu, F. Laloë, *Mécanique Quan- tique* (Herman, Paris, 1988)
47. D. Belkic, R. Gayet, A. Salin, Phys. Rep. **56**, 279 (1979)
48. M. Beuve, M. Caron, B. Gervais, H. Rothard, A. Clouvas, C. Potiriadis, Eur. Phys. J. D **15**, 293 (2001)
49. M. Caron, H. Rothard, M. Jung, V. Mouton, D. Lelièvre, M. Beuve, B. Gervais, Nucl. Instrum. Meth. B **146**, 126 (1998)
50. F. Hubert, R. Bimbot, H. Gauvin, At. Data Nucl. Data Tab. **46**, 1 (1990); R. Bimbot, C. Cabot, D. Gardes, H. Gauvin, R. Hingmann, I. Orliange, L. de Reilhac, Nucl. Instrum. Meth. **44**, 1 (1989); R. Bimbot, C. Cabot, D. Gardes, H. Gauvin, R. Hingmann, I. Orliange, L. de Reilhac, K. Subotic, Nucl. Instrum. Meth. **44**, 19 (1989)
51. N. Sakamoto, N. Ogawa, N. Shiomi-Tsuda, Nucl. Instrum. Meth. B **115**, 84 (1996); ICRU Rep. **49**, 1 (1993)
52. H.H. Andersen, J.F. Ziegler, *Stopping powers and ranges in all elements* (Pergamon Press, Elmsford, 1977)
53. J.P. Rozet, C. Stéphan, D. Vernhet, Nucl. Instrum. Meth. B **107**, 67 (1996)
54. D. Hasselkamp, A. Scharmann, Phys. Stat. Sol. (a) **79**, K197 (1983)
55. A. Koyama, T. Shikata, H. Sakairi, Jap. J. Appl. Phys. **20**, 65 (1981)