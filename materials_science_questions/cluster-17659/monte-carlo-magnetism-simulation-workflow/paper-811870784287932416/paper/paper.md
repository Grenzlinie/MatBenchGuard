Modern Physics Letters B, Vol. 23, No. 4 (2009) 549–565
© World Scientific Publishing Company

![](./images/811870784287932416_1.jpg)

# SURFACE-DIRECTED SPINODAL DECOMPOSITION: LATTICE MODEL VERSUS GINZBURG–LANDAU THEORY

KURT BINDER

Institut für Physik, Johannes Gutenberg Universität Mainz,
Staudinger Weg 7, D-55099 Mainz, Germany
kurt.binder@uni-mainz.de

SUBIR K. DAS

Theoretical Sciences Unit,
Jawaharlal Nehru Centre for Advanced Scientific Research,
Jakkur, Bangalore 560064, India
das@jncasr.ac.in

JÜRGEN HORBACH

Institut für Materialphysik im Weltraum,
Deutsches Zentrum für Luft- und Raumfahrt (DLR), 51170 Köln, Germany
juergen.horbach@dlr.de

Received 6 February 2009

When a binary mixture is quenched into the unstable region of the phase diagram, phase separation starts by spontaneous growth of long-wavelength concentration fluctuations ("spinodal decomposition"). In the presence of surfaces, the latter provide nontrivial boundary conditions for this growth. These boundary conditions can be derived from lattice models by suitable continuum approximations. But the lattice models can also be simulated directly, and thus used to clarify the conditions under which the Ginzburg–Landau type theory is valid. This comparison shows that the latter is accurate only in the immediate vicinity of the bulk critical point, if thermal fluctuations can also be neglected (true for the late stages of phase separation). In contrast, a local kinetic molecular field theory can take full account of nonlinearities and of rapid concentration variations, and thus has a much wider validity. This enables the detailed study of phase separation processes in thin films of solid binary alloys. However, the extension to spin-odal decomposition in fluid binary systems (which can be simulated by brute force large scale molecular dynamics methods, of course) remains an unsolved challenge.

**Keywords**: Binary mixtures; phase separation; Kawasaki kinetic Ising model; computer simulation; wetting.

## 1. Introduction and Overview

"Spinodal decomposition"$^{1–10}$ is a mechanism describing the kinetics of phase separation in unstable binary mixtures. Figure 1 shows a schematic phase diagram of a binary mixture ($T$ being the temperature and $c$ the relative concentration of

![](./images/811870784287932416_2.jpg)

Fig. 1. Schematic phase diagram of a binary mixture in the temperature ($T$)-concentration ($c$) plane, illustrating a quenching experiment where at time $t = 0$ temperature is lowered from $T = T_0$ to a value underneath the spinodal curve (broken curve), leading to the growth of a wavepacket of unstable standing concentration waves. This is indicated by the concentration variation in the $x$-direction, focusing on the wavelength $\lambda_m$ with maximum growth rate for simplicity. For further explanations cf. text.

one of the components). In this temperature-concentration plane, there often occurs a miscibility gap, as drawn schematically in Fig. 1 (the full curve ending in the critical point at $T = T_c$ and $c = c_{\text{crit}}$). In a state point $(T,c)$ that falls at $T < T_c$ underneath this coexistence curve, thermal equilibrium is described by a phase coexistence, and two (macroscopic) domains with concentrations given according to the two branches $c_{\text{coex}}^{(1)}, c_{\text{coex}}^{(2)}$ of the coexistence curve coexist. The relative amounts of these two phases are given by the lever rule.

Spinodal decomposition now occurs if we consider a "quenching experiment": At time $t = 0$, we bring a system that was in equilibrium for all times $t < 0$ at a temperature $T_0$ in a single homogeneous phase with concentration $\bar{c}$, to the considered state point in the miscibility gap. The basic ideas of the resulting phase transformation process have already been proposed about 50 years ago,$^{1,11}$ but nevertheless many aspects are still not yet well understood even today.$^{10}$ Thus, we summarize here a few key features only.

A central idea$^{1,11}$ that nevertheless is still of doubtful value$^{2,5,10,12-14}$ postulates the existence of a "spinodal curve" (broken curves in Fig. 1) that separates metastable from unstable (homogeneous) states underneath the coexistence curve. Underneath the spinodal curve, homogeneous initial states are unstable against

long wavelength concentration fluctuations, whose amplitudes spontaneously grow with time (and exponentially fast¹). The wavelengths in the unstable wave packet must exceed a critical wavelength $\lambda_c$, and the initial growth rate is maximal at $\lambda_m = \sqrt{2}\lambda_c$.¹ This predicted behavior is also qualitatively indicated in Fig. 1. Basically, this Cahn–Hilliard theory is only a linear stability analysis of concentration fluctuations, completely ignoring all nonlinear effects, and it predicts that $\lambda_c \to \infty$ when one approaches the spinodal curve. Related singular behavior is predicted when one approaches the spinodal curve from the metastable side.¹¹ However, for systems with short range forces, the neglect of nonlinear effects on the scale $\lambda_c$ is not self-consistent, as a Ginzburg-type criterion shows.¹³,¹⁴ The concept of a spinodal curve then is ill-defined, and the singularities associated with it are mean-field artefacts.¹²⁻¹⁴ Experiments and simulations (as reviewed in Ref. 5) show that the exponential growth of fluctuations with time is a mean-field artefact as well, apart from the very early stages of symmetrical polymer mixtures with very large molecular weights¹⁵ (for which mean-field theory is valid¹³,¹⁴).

The gradual crossover from (nonlinear) spinodal decomposition to nucleation¹² is still a problem that is not yet understood in detail, and will not be considered further in this brief review. We rather focus on the late stages of the phase separation process, where rather large domains of both phases (which have concentrations very close to $c_{\text{coex}}^{(1)}, c_{\text{coex}}^{(2)}$) can be identified, and we consider the kinetics of coarsening of these structures.²⁻¹⁰ In these late stages one expects a power law for the growth of the characteristic length scale $\ell(t)$ of the concentration inhomogeneities,
$$
q_m(t) \propto [\ell(t)]^{-1} \propto t^{-a}, \tag{1}
$$
and in scattering experiments the inverse of this length scale shows up³,⁸ as a peak (at wave number $q_m(t)$) in the structure factor $S(q,t)$. Such a power law was first proposed by Lifshitz and Slyozov¹⁶ for solid binary mixtures, on the basis of a diffusive mechanism of coarsening,
$$
a = 1/3, \tag{2}
$$
while different mechanisms (and different exponents) occur for fluid binary mixtures.¹⁷⁻²³ A key feature of both solid and liquid binary mixtures is the scaling of the structure factor during the late stages,
$$
S(q,t) = [\ell(t)]^d \tilde{S}[q\ell(t)], \quad t \to \infty, \quad q \to 0, \quad q\ell(t) \text{ finite}, \tag{3}
$$
where $d$ is the dimensionality and $\tilde{S}$ is the scaling function. While a real wealth of data on $\tilde{S}$ exists (e.g. Ref. 8), the theoretical understanding of $\tilde{S}$ (e.g. also its dependence on the volume fraction $\phi$ of the minority phase) is still incomplete. However, it is believed⁴ that statistical thermal fluctuations in the final state to which the quench leads are irrelevant, as far as late stage coarsening is concerned. Therefore, a popular description for spinodal decomposition of bulk solid binary mixtures is just "model B",²⁴ i.e. the nonlinear time-dependent Ginzburg–Landau (TDGL)

equation with conserved order parameter (here, conserved concentration), $^{6,10}$ also known as Cahn–Hilliard equation.

In the last two decades, much of the interest in this problem has been shifted to try to understand phase separation of binary mixtures confined to thin films. $^{22,23,25–50}$ Then the question of how one can describe the surface effects on phase separation in such a thin film arises. $^{22,23,27,46–51}$ Experimen-tally$^{25,26,29–33,36,39,40,43–45}$ one finds that an initially homogeneously mixed system, at volume fraction of 50% everywhere, develops a damped concentration wave pattern: the concentration of the species that likes to be at the surface increases, while the concentration of the other species decreases, but develops a maximum at some distance away from the surface, where the concentration of the species that was attracted to the surface has a minimum. Typically, there are several such oscillations of the local concentrations as a function of the distance $z$ from the surface; but the amplitude of these oscillations decreases with increasing $z$. This phenomenon is termed "surface-directed spinodal decomposition". $^{25–27}$ The wavelength of these oscillations $\lambda(t)$ is found to increase with time, sometimes a power law $\ell(t) \propto t^{1/3}$ does work$^{36}$ (even for fluid binary polymer mixtures), but often a faster growth is observed. The interpretation of these phenomena is still somewhat controversial, and many questions remain to be understood.

Of course, phase separation in experimentally prepared thin films is difficult to interpret for a variety of reasons: normally the top and bottom surface of a thin film are not equivalent to each other, and the wetting conditions$^{52–55}$ at these surfaces are not quantitatively characterized (also the substrate roughness or other defects may play a role). $^{56}$ In fluid binary mixtures, there is often a pronounced dynamic asymmetry between both constituents$^{8,57}$ which complicates the phase separation kinetics. Due to all these complications, computational modeling of idealized systems is very useful, since thin films with walls without imperfections are readily considered, all interaction parameters can be chosen at will and hence also the wetting properties of the walls can easily be characterized, and information on the formation of inhomogeneous structures is readily available in arbitrary detail, with perfect "resolution" not only in the $z$-direction perpendicular to the walls, but also laterally. In contrast, many experimental techniques (e.g. Ref. 58) have only limited resolution in the $z$-direction and average over the lateral direction completely.

In this brief review, we shall hence not discuss the experiments further, but focus on the insight that has been gained in the simplest case of phase separation in thin solid binary films, disregarding also elastic misfit. $^{6}$ Since most solid binary alloys are crystalline, the natural starting point is a perfect lattice with a free surface against an inert wall (Sec. 2). We shall formulate a molecular field theory for the spin-exchange kinetic Ising model ("Kawasaki model"$^{59}$) for the fully inhomogeneous, out of equilibrium case$^{51}$ (Sec. 3), and use this approach both to justify the appropriate boundary conditions$^{51}$ for the Ginzburg–Landau approach$^{27,34}$ (Sec. 4) and consider also the direct numerical solution of this set of coupled nonlinear

equations$^{60}$ (Sec. 5). In Sec. 6, we discuss the extent to which the Ginzburg-Landau approach approximates the lattice-based discrete molecular field theory very close to the critical points, while Sec. 7 summarizes a few conclusions.

### 2. Lattice Model
We assume a simple cubic lattice where each lattice site is taken by either an A-atom or a B-atom, and for simplicity, only nearest neighbor pairwise interactions are assumed: $\varphi_{\text{AA}}, \varphi_{\text{BB}}$, and $\varphi_{\text{BB}}$ (Fig. 2). It is rather natural to assume that the interactions in the lattice plane $n=1$ adjacent to the surface ($\varphi_{\text{AA}}^{\text{s}}, \varphi_{\text{AB}}^{\text{s}}$ and $\varphi_{\text{BB}}^{\text{s}}$, respectively) may differ from the bulk, and that the inert wall provides a potential on the atoms, which may again be different for A- and B-atoms ($v_{\text{A}}$ or $v_{\text{B}}$, respectively). In an attempt to formulate the simplest possible generic model, this potential is also assumed to have strictly short range (although it is known that long range surface potentials in many instances are rather common$^{52-54}$ and are known to have important physical effects on the wetting behavior$^{52-54}$).

![](./images/811870784287932416_3.jpg)

Fig. 2. Schematic description of the lattice model of a binary (A, B) mixture adjacent to a wall (shaded) perpendicular to the $z$-direction. The coordinate in the planes $n=1,2,3,\dots$ parallel to the wall (at $n=0$) is denoted as $\boldsymbol{\rho}$. Pairwise nearest neighbor interactions in the bulk are denoted as $\varphi_{\text{AA}}, \varphi_{\text{AB}}$, and $\varphi_{\text{BB}}$, and as $\varphi_{\text{AB}}^{\text{s}}, \varphi_{\text{AB}}^{\text{s}}$, and $\varphi_{\text{BB}}^{\text{s}}$ if both atoms lie in the plane adjacent to the surface ($n=1$), respectively. On these atoms also binding potentials $v_{\text{A}}, v_{\text{B}}$ act.

Of course, it is a straightforward exercise to transform this model from the local concentration variables $c_i$ at lattice site $i$ to the Ising spin representation ($c_i=1$, if lattice site is taken by an A-atom may correspond to the spin variable $S_i=-1$, $c_i=0$ if lattice site $i$ is taken by a B-atom corresponds to $S_i=+1$). Then the model is described by the Ising Hamiltonian with surface magnetic field $^{60}$

$$
\mathcal{H}=-J \sum_{\langle i, j\rangle \in \text { bulk }} S_{i} S_{j}-J_{\mathrm{s}} \sum_{\langle i, j\rangle \in S_{1}, S_{2}} S_{i} S_{j}-H \sum_{i} S_{i}-H_{1} \sum_{i \in S_{1}} S_{i}-H_{1} \sum_{i \in S_{2}} S_{i}. \quad (4)
$$

Here we have assumed that the system is a thin film containing $D+1$ lattice planes perpendicular to the $z$-direction, and then a second wall at $n=D+2$ acts equivalent to the first one. The "exchange constants" $J, J_{s}$ in Eq. (4) then become $^{34}$

$$
J=\varphi_{\mathrm{AB}} / 2-\left(\varphi_{\mathrm{AA}}+\varphi_{\mathrm{BB}}\right) / 4, \quad J_{\mathrm{s}}=\varphi_{\mathrm{AB}}^{\mathrm{s}} / 2-\left(\varphi_{\mathrm{AA}}^{\mathrm{s}}+\varphi_{\mathrm{BB}}^{\mathrm{s}}\right) / 4, \quad (5)
$$

the bulk "magnetic field" $H$ involves also the chemical potentials $\mu_{\mathrm{A}}, \mu_{\mathrm{B}}$ of both species,

$$
H=\left(\mu_{\mathrm{B}}-\mu_{\mathrm{A}}\right) / 2+(1 / 2) \sum_{j(\neq i)}\left(\varphi_{\mathrm{AA}}-\varphi_{\mathrm{BB}}\right), \quad (6)
$$

while for sites $i$ from the first or last layer we have an additional "surface magnetic field" $H_1$,

$$
\begin{aligned}
H+H_{1}= & \left(\mu_{\mathrm{B}}-\mu_{\mathrm{A}}+v_{\mathrm{B}}-v_{\mathrm{A}}\right) \\
& +\frac{1}{2}\left\{\sum_{j(\neq i) \in 1 \text { st layer }}\left(\varphi_{\mathrm{AA}}^{\mathrm{s}}-\varphi_{\mathrm{BB}}^{\mathrm{s}}\right)+\sum_{j(\neq i) \in 2 \text { nd layer }}\left(\varphi_{\mathrm{AA}}-\varphi_{\mathrm{BB}}\right)\right\}.
\end{aligned}
$$

Note that a nonzero surface magnetic field $H_{1}$ arises even when $v_{\mathrm{B}}=v_{\mathrm{A}}=0$ and interactions are unchanged near the surfaces $\varphi_{\mathrm{AA}}^{\mathrm{s}}=\varphi_{\mathrm{AA}}$ and $\varphi_{\mathrm{BB}}^{\mathrm{s}}=\varphi_{\mathrm{BB}}$, as long as $\varphi_{\mathrm{AA}} \neq \varphi_{\mathrm{BB}}$: this is a consequence of the "missing neighbors" of sites in the first layer.

We now associate dynamics to the model by assuming a direct exchange mechanism, assuming the Glauber $^{61}$ transition probability to obtain the Kawasaki $^{59}$ spin exchange kinetic Ising model (where two randomly chosen nearest neighbor spins are exchanged for a trial move)

$$
W\left(S_{i} \rightarrow S_{j}, S_{j} \rightarrow S_{i}\right)=\left(1 / 2 \tau_{s}\right)\left[1-\tanh \left(\delta \mathcal{H} / 2 k_{B} T\right)\right], \quad (8)
$$

where $\delta \mathcal{H}$ is the energy change associated with the spin exchange, and $\tau_{s}$ sets the time scale.

Of course, it is well-known that the direct exchange of atoms is not a realistic description of the dynamics in real solid mixtures where concentration variations relax via vacancy-mediated diffusion. $^{62}$ In fact, a model similar to Fig. 2, without walls but allowing for a small concentration $c_{v}$ of vacant sites $V$ (the so-called ABV$\operatorname{model}^{63}$ ) has been introduced, but it has been found $^{7,64,65}$ that in typical cases the

resulting time evolution of this model is very similar to the time evolution resulting from the direct exchange model, resulting from Eq. (8).

One straightforward approach to study the model defined by Eqs. (4)-(8) would be Monte Carlo simulation. $^{66,67}$ In fact, studies of spinodal decomposition in the bulk with Monte Carlo methods have been done already a long time ago. $^{68,69}$ Since the structure factor $S(\mathbf{q}, t)$ is a quantity that exhibits "lack of selfaveraging", $^{66}$ however, one needs to repeat the simulation of the quenching experiment many times, using different pseudo-random number sequences, in order to obtain good statistics. Since one also wishes to simulate large lattices (such that finite size effects $^{66,67}$ do not invalidate the observation of the length scale $\ell(t)$ at late times, where $\ell(t)$ is much larger than the lattice spacing) over long times (initially the growth is even slower than the prediction according to Eqs. (1) and $(2)^{17,18}$ ), significant computational resources are needed for such studies, however. Thus, it has taken a large effort $^{69,70}$ to settle the controversy of whether the Lifshitz-Slyozov $^{16}$ law, Eq. (2), actually holds.

Since there are compelling theoretical arguments $^{4}$ that in the late stages of spin odal decomposition thermal fluctuations are irrelevant, the Monte Carlo method (which spends a lot of effort precisely to the faithful simulation of such thermal fluctuations $^{66,67}$ ) is widely considered as an "overkill" of the problem, and so it has become common practice to rather study it by numerical simulation of the nonlinear Ginzburg-Landau (GL) equation with conserved order parameter. $^{5,6,9,10,71}$ In fact, the patterns of (coarse-grained) configurations of the system in the bulk, obtained in this manner, look strikingly similar $^{71}$ to corresponding Monte Carlo work $^{69}$ (although in the GL treatment randomness only enters via the random initial condition of the time evolution).

As a consequence, the studies of surface effects on spinodal decomposition have avoided the use of Monte Carlo methods, but have mostly used GL approaches $^{26,46}$ and recently also a treatment based on the nonlinear inhomogeneous molecular field method $^{51}$ has been given. $^{50}$ Since this method can also be used $^{51}$ to derive boundary conditions for the GL approach, we turn to this local molecular field theory for the Kawasaki $^{59}$ spin exchange model next.

### 3. A Molecular Field Theory for the Kawasaki Model with Walls
We now recall (Fig. 2) that the index $i$ of a lattice site must distinguish the layer index $n$ of the plane parallel to the walls as well as the coordinate $\boldsymbol{\rho}$ in these planes, to define local averages in equilibrium (which are time-independent) and out of equilibrium (which are time-dependent) as follow,

$$
m_{n}(\boldsymbol{\rho})=\left\langle S_{i}\right\rangle_{T}, \quad m_{n}(\boldsymbol{\rho}, t)=\left\langle S_{i}(t)\right\rangle_{T}. \tag{9}
$$

In molecular field theory, all quantities of interest can be expressed in terms of such single-site averages. For completeness, we recall the description of equilibrium for the considered thin film geometry. The free energy can then be written in terms of

layer energies $E_n$ and layer entropies $S_n$,

$$
F = \sum_{n=1}^{D+1} (E_n - TS_n) \tag{10}
$$

where $\sum_n E_n$ is found by replacing $S_i$ by $m_n(\boldsymbol{\rho})$ in the Hamiltonian, and $S_n$ is just written in terms of the familiar "entropy of mixing" terms of the alloy,

$$
S_n/k_B T = \sum_{\boldsymbol{\rho}} \left\{ \frac{1 + m_n(\boldsymbol{\rho})}{2} \ln \left[ \frac{1 + m_n(\boldsymbol{\rho})}{2} \right] + \frac{1 - m_n(\boldsymbol{\rho})}{2} \ln \left[ \frac{1 - m_n(\boldsymbol{\rho})}{2} \right] \right\}. \tag{11}
$$

From $(\partial F/\partial m_n(\boldsymbol{\rho}))_{T,H,H_1} = 0$, one then obtains the standard inhomogeneous molecular field equations in equilibrium, e.g.

$$
m_1(\boldsymbol{\rho}) = \tanh \frac{H_1^{\text{eff}}(\boldsymbol{\rho})}{k_B T}, \tag{12}
$$

with

$$
H_1^{\text{eff}}(\boldsymbol{\rho}) = J m_2(\boldsymbol{\rho}) + J_{\text{s}} \sum_{\Delta \boldsymbol{\rho}} m_1(\boldsymbol{\rho} + \Delta \boldsymbol{\rho}) + H_1 + H \tag{13}
$$

being the effective field acting on a spin at site $\boldsymbol{\rho}$ in the first layer ($\Delta \boldsymbol{\rho}$ being a vector connecting site $i$ with one of its 4 nearest neighbors in a layer).

This approach can be extended to the molecular field theory for the Kawasaki spin exchange kinetic Ising model, $^{59}$ using the transition probability, $^{51,73}$ Eq. (8), to derive a set of coupled kinetic equations for the local magnetization $^{50,51} m_n(\boldsymbol{\rho},t)$; e.g.

$$
\begin{aligned}
2 \tau_{s} \frac{d}{d t} m_{1}(\boldsymbol{\rho}, t) =& -5 m_{1}(\boldsymbol{\rho}, t)+m_{2}(\boldsymbol{\rho}, t)+\sum_{\Delta \boldsymbol{\rho}} m_{1}(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}, t) \\
&+\left[1-m_{1}(\boldsymbol{\rho}, t) m_{2}(\boldsymbol{\rho}, t)\right] \tanh \frac{J}{k_{B} T}\left[m_{2}(\boldsymbol{\rho}, t)+H_{1} / J\right. \\
&\left.+\frac{J_{s}}{J} \sum_{\Delta \boldsymbol{\rho}} m_{1}(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}, t)-m_{3}(\boldsymbol{\rho}, t)-m_{1}(\boldsymbol{\rho}, t)-\sum_{\Delta \boldsymbol{\rho}} m_{2}(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}, t)\right] \\
&+\sum_{\Delta \boldsymbol{\rho}}\left[1-m_{1}(\boldsymbol{\rho}, t) m_{1}(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}, t)\right] \tanh \frac{J}{k_{B} T}\left[m_{2}(\boldsymbol{\rho}, t)\right. \\
&+\frac{J_{s}}{J} \sum_{\Delta \boldsymbol{\rho}^{\prime}} m_{1}\left(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}^{\prime}, t\right)-m_{2}(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}, t) \\
&\left.-\frac{J_{s}}{J} \sum_{\Delta \boldsymbol{\rho}^{\prime}} m_{1}\left(\boldsymbol{\rho}+\Delta \boldsymbol{\rho}^{\prime}+\Delta \boldsymbol{\rho}, t\right)\right].
\end{aligned} \tag{14}
$$

Note that the factors with square brackets in front of the tanh functions come from terms related to the fact that no change of the configuration results, when a pair of parallel spins is exchanged. $^{51}$ The argument of the tanh functions can be interpreted

as the difference between the local effective fields $H_{1}^{\text{eff}}(\boldsymbol{\rho}, t)$ and the field acting on the site with which the exchange takes place.

While in thermal equilibrium only the equations for $m_{1}(\boldsymbol{\rho})$ and $m_{D+1}(\boldsymbol{\rho})$ differ from the standard bulk equation $\{m_{n}(\boldsymbol{\rho}) = \tanh \frac{J}{k_{B}T}[m_{n+1}(\boldsymbol{\rho}) + m_{n-1}(\boldsymbol{\rho}) + \sum_{\Delta \boldsymbol{\rho}} m_{n}(\boldsymbol{\rho} + \Delta \boldsymbol{\rho}) + H/J],\ n = 2,3,\ldots,D\}$, here the bulk-like equation applies only for the layers $n = 3,\ldots,D - 1$, while both layers $n = 1,\ n = 2$ and $n = D$ and $D + 1$ yield different equations. $^{50,51}$ This is simply understood by the fact that spins in layers $n = 2$ and $n = D$ can be exchanged with spins in layers $n = 1$ and $D + 1$, respectively, and thus get affected by the different effective fields $H_{1}^{\text{eff}}(\boldsymbol{\rho}, t)$ and $H_{D+1}^{\text{eff}}(\boldsymbol{\rho}, t)$ in these layers. Since the resulting set of equations is rather clumsy and can be found in the literature (Refs. 50 and 51), it is not repeated here.

We note that this spirit $^{72}$ of deriving a set of coupled nonlinear local equations on the lattice from the master equation within molecular field theory, for the description of spinodal decomposition, has been extensively exploited by Martin et al. $^{73-75}$ and by Vaks et al. $^{7,76,77}$ Also the extension to the interplay between spinodal decomposition and ordering in alloys has been extensively considered. $^{7,79}$ However, these interesting studies are outside of the focus of the present brief review.

## 4. Boundary Conditions for the Time-Dependent Ginzburg-Landau Theory

As has been mentioned above, it is widely believed that the late stages of spinodal decomposition in the bulk can be well described by considering the solutions of the TDGL theory with conserved order parameter $^{4-6,10,71}$ ("model B" $^{24}$ without statistical noise term). This equation is ($\tau$ is a scaled time, and $\mathbf{r}$ is a spatial coordinate in three-dimensional continuous space) written as

$$
\frac{\partial}{\partial \tau} \Psi(\mathbf{r}, \tau)=-\nabla \cdot \mathbf{J}(\mathbf{r}, \tau)=\nabla \cdot\left[\nabla\left(\delta \mathcal{F}_{b} / \delta \Psi\right)\right], \tag{15}
$$

where $\mathbf{J}(\mathbf{r}, \tau)$ plays the role of a current, and the free energy functional $\mathcal{F}_{b}\{\Psi(\mathbf{r})\}$ in scaled form becomes

$$
\mathcal{F}_{b}\{\Psi(\mathbf{r})\}=\int d \mathbf{r}\left\{-\Psi(\mathbf{r})^{2} / 2+\Psi(\mathbf{r})^{4} / 4+[\nabla \Psi(\mathbf{r})]^{2} / 4\right\}, \tag{16}
$$

so that Eq. (15) leads to

$$
\frac{\partial \Psi(\mathbf{r}, \tau)}{\partial \tau}=-\nabla^{2}\left[\Psi(\mathbf{r}, \tau)-\Psi(\mathbf{r}, \tau)^{3}+\frac{1}{2} \nabla^{2} \Psi(\mathbf{r}, \tau)\right]. \tag{17}
$$

It is tempting to use a related approach also for spinodal decomposition in a system with a surface, where $\mathbf{r}=(\boldsymbol{\rho}, z) \xi_{b}$, $z$ now denoting the distance in continuous space and $\xi_{b}$ is the bulk correlation length. For this purpose, we rewrite Eq. (17) redefining the rescaled order parameter field $\Psi(\mathbf{r}, \tau)=m_{b} \Phi(\boldsymbol{\rho}, z, t)$ where

$m_b(=\sqrt{3}(1-T/T_{cb})^{1/2})$ is the bulk magnetization of the Ising model of Sec. 3 near the bulk critical temperature $T_{cb}$ in the molecular field approximation,

$$
\begin{aligned}
2 \tau_{s} \frac{\partial \Phi(\boldsymbol{\rho}, z, t)}{\partial t}=&-\nabla^{2}\left\{\left(T_{c b} / T-1\right) \Phi(\boldsymbol{\rho}, z, t)\right. \\
&\left.-\frac{1}{3} \Phi(\boldsymbol{\rho}, z, t)^{3}+\frac{J}{T} \nabla^{2}(\Phi(\boldsymbol{\rho}, z, t))\right\}, \quad 0<z<D.
\end{aligned} \quad(18)
$$

We note that the bulk correlation length in molecular field theory is, as is well known, given by ($a$ is the lattice spacing of the Ising model, which henceforth we set equal to unity)

$$
\xi_{b}^{2}=a^{2}\left\{k_{B} T /\left[J\left(1-m_{b}^{2}\right)\right]-k_{B} T_{c b} / J\right\} \approx a^{2} /\left[12\left(1-T / T_{c b}\right)\right], \quad(19)
$$

where the last approximation holds only for $T$ close to $T_{cb}(=6J/k_B)$. Equation (18) can also be directly derived from a continuum approximation to the bulk counterpart of the set of discrete kinetic equations considered in Sec. 3 [e.g. Eq. (14)]. However, for this partial differential equation, which obviously contains terms of order $\nabla^{4}\Phi$, two boundary conditions for $z=0$ and $z=D$ are needed to guarantee a sensible solution. The formulation of these boundary conditions for model $B$ is a nontrivial problem. $^{27,34,48-51,80}$ From rather general symmetry arguments one can deduce the possible form of these boundary conditions $^{79}$ from a generalization of Eq. (16) that contains boundary terms, without recourse to any microscopic lattice model. However, the numerical treatment of the resulting boundary conditions re- quires great care because of a delta function appearing at the boundary, for short range surface forces. $^{49}$ Since here we are interested in a comparison with the lattice model of Sec. 3 anyway, we emphasize the original approach $^{51}$ where boundary conditions were also derived by a continuum approximation from the set of discrete equations for $m_n(\boldsymbol{\rho},t)$ considered in Sec. 3.

This can be done by suitable expansion of differences in terms of differentials, $^{51,73}$

$$
\begin{aligned}
m_{n \pm 1}(\boldsymbol{\rho}, t)=& m_{n}(\boldsymbol{\rho}, t) \pm \frac{\partial m_{n}(\boldsymbol{\rho}, t)}{\partial n}+\frac{1}{2} \frac{\partial^{2} m_{n}(\boldsymbol{\rho}, t)}{\partial n^{2}} \\
& \pm \frac{1}{6} \frac{\partial^{3} m_{n}(\boldsymbol{\rho}, t)}{\partial n^{3}}+\frac{1}{24} \frac{\partial^{4} m_{n}(\boldsymbol{\rho}, t)}{\partial n^{4}},
\end{aligned} \quad(20)
$$

and $m_n(\boldsymbol{\rho}+\Delta\boldsymbol{\rho},t)=m_n(\boldsymbol{\rho},t)+(\Delta\boldsymbol{\rho}\cdot\nabla_{\parallel})m_n(\boldsymbol{\rho},t)+$ (higher order terms not written here, see Ref. 51). Straightforward but tedious algebra yields $\{\Phi(\boldsymbol{\rho},z,t)\equiv m_n(\boldsymbol{\rho},t)$, $z=(n-1)a\}$

$$
\begin{aligned}
2 \tau_{s} \frac{\partial}{\partial t} \Phi(\boldsymbol{\rho}, z=0, t)=& \frac{H_{1}}{T}+\frac{J}{T}\left(4 \frac{J_{s}}{J}-5\right) \Phi(\boldsymbol{\rho}, z=0, t) \\
&+\left.\frac{J}{T} \frac{\partial \Phi(\boldsymbol{\rho}, z, t)}{\partial z}\right|_{z=0},
\end{aligned} \quad(21)
$$

which comes from Eq. (11) and only the terms of leading order as $T \to T_{cb}$ have been retained, and a second equation which results from the equation for $^{51}$

$2 \tau_{s} d m_{2}(\boldsymbol{\rho}, t) / d t$. It has been argued $^{27,34}$ that one may replace this second equation by the more compact condition that the flux of order parameter in the $z$-direction vanishes,

$$
\left.\frac{\partial}{\partial z}\left\{\left(\frac{T_{c b}}{T}-1\right) \Phi(\boldsymbol{\rho}, z, t)-\frac{1}{3}[\Phi(\boldsymbol{\rho}, z, t)]^{3}+\frac{J}{T} \frac{\partial^{2}}{\partial z^{2}}[\Phi(\boldsymbol{\rho}, z, t)]\right\}\right|_{z=0}=0. \quad(22)
$$

Note that the order parameter in the surface layer is not conserved (Eq. 20), of course, because order parameter can be transported from the bulk to the surface of the thin film; but Eq. (18) ensures that the total order parameter in the thin film is conserved.

From this derivation it is evident that the resulting set of equations, Eqs. (18), (20) and (21) are valid only if $\xi_{b} \gg a=1$. Only then are concentration variations small on the scale of a lattice spacing. When one deals with critical phenomena, one does want to consider the limit $\xi_{b} \rightarrow \infty$, and then a treatment based on the Ginzburg-Landau free energy functional (plus fluctuations, requiring then a renor- malization group approach $^{6,24,80}$ ) is perfectly justified. For spinodal decomposition, however, we are not $a$ priori interested in the critical region - but using time depen dent Ginzburg-Landau (TDGL) theory does require that $\xi_{b} \gg a$! In fact, choosing $\xi_{b}=2 a$ only already requires us to use $T=5.875 J / k_{B}$, i.e. $T / T_{c b} \approx 0.98$. This also requires the use of not too thin films (because of the shift of $T_{c}(D)$ with film thick ness, which in mean-field theory is $T_{c b}-T_{c}(D) \propto D^{-2}$, see Ref. 50 and references therein), because if the quench does not lead into the two-phase region of the thin film no lateral phase separation would take place. $^{35,38,47}$

## 5. Numerical Solution of the Set of Nonlinear Equations for the Local Order Parameters on the Lattice

The problem that the standard approach to surface-directed spinodal decomposi- tion is justified in a strict sense only for $T$ very close to $T_{c b}$ is immediately avoided if one solves directly the set of nonlinear kinetic equations for $m_{n}(\boldsymbol{\rho}, t)$ on the lattice, such as those considered in Sec. 3 (e.g. Eq. (14)). Using films of thickness $D=9$, 19 and 29 (i.e. containing 10, 20 or 30 lattice planes) and lateral linear dimen- sions $L=128$, these equations have been solved, choosing as an initial condition $m_{n}(\boldsymbol{\rho}, t)$ from a uniform random distribution between -1 and +1 , with the total magnetization in the film zero. Figure 3 shows results for a quench to $T=4 J / k_{B}$ $(T / T_{c b}=2 / 3)$, where $\xi_{b} \approx 0.33 a$. One can clearly recognize that rapid concen- tration variations occur, and are well resolved by the present technique. Wave-like concentration variations across the film build up during rather early stages, but the first minimum adjacent to the walls moves towards the center of the film, until the minima finally merge, and the laterally averaged profile reveals a stratified struc- ture. Note that the field $H_{1}=J$ used in this calculation corresponds to a situation where the semi-infinite Ising system would be in a state of complete wetting. $^{82}$ However, one should not conclude from Fig. 3(a) that the system at any time is

![](./images/811870784287932416_4.jpg)

Fig. 3. (a) Layerwise order parameter $\Psi_{\text{av}}(n)$ plotted versus layer index $n$ for four different times for the choice $D=29$, $L=128$, $H_1=J$, $J_s=J$, $k_B=4J$, obtained by averaging over runs from five independent initial configurations. The continuous lines are cubic interpolations of the original data, used as guides to the eye. (b) Cross-sectional snapshot pictures of the same systems as in (a), displaying the magnetization configuration in a plane parallel to the walls at $n=15$. (c) Same as (b), but in $xz$-plane for $y=L/2$. The time unit $\tau_s$ has been set to unity. From Das et al.$^{50}$

laterally homogeneous: snapshot pictures of the plane $z=D/2$ (Fig. 3(b)) reveal at early times $(t=50)$ the characteristic pattern of spinodal decomposition, similar to studies of bulk two-dimensional spinodal decomposition.$^{5,69,70}$ The snapshot pictures taken across the thin film (Fig. 3(c)) reveal that in the early stages $(t\leq50)$ bulk-like three-dimensional spinodal decomposition occurs inside of the film, while at the walls a precursor of a wetting layer forms. When the length scale $\ell(t)$ of the concentration inhomogeneities (cf. Eq. (1)) becomes comparable to the film thickness $D$, a crossover to two-dimensional spinodal decomposition occurs. Since the

thickness of the surface enrichment layers has grown, the center of the thin film is now depleted from the species that is attracted to the wall, and so the snapshot at $t = 10000$ is typical for off-critical spinodal decomposition. For $t = 2000$, however, at $z = D/2$ there is a local maximum of $\Psi_{\text{av}}(n)$, cf. Fig. 3(a), and then the roles of majority and minority phases have reversed.

This interplay of growing surface enrichment layers and lateral phase separation has been pointed out already in studies using the TDGL approach. $^{46,47}$ For small $D$ such as $D = 9$, however, the crossover to the asymptotic power law (Eqs. (1) and (2)) already occurs for times of the order $t \approx 10^3$, and $S(k,t)$ (orienting the wavevector $\mathbf{k}$ parallel to the walls, of course) has the shape that is characteristic for two-dimensional spinodal decomposition $^{50}$ (i.e. for $k \approx 2k_m(t)$ a flat shoulder is seen before, for $k > 4k_m(t)$, the Porod law $^{83}$ $S(k,t) \propto k^{-d+1} = k^{-3}$, sets in).

## 6. Comparison Between the Lattice Approach and TDGL Theory

When one compares TDGL results for the temperature $T/T_{cb} = 2/3$ chosen for the example of the previous section with the lattice treatment, one discovers $^{50}$ severe discrepancies, as expected, due to the smallness of the correlation length. In the present section, we discuss a comparison in the critical region, at $k_BT/J = 5.875$ where $\xi_b/a = 2$. While the snapshot pictures $^{50}$ produced from the lattice treatment (Sec. 4) and the TDGL approach already look indistinguishable, one can still identify small systematic discrepancies when one compares the averaged concentration profiles (Fig. 4). It turns out that for smaller $D$ these differences are even more pronounced. Here the discrete mesh sizes of the TDGL approach were adjusted to the lattice constant, rather than to $\xi_b,^{26,34}$ so the numerical effort of both methods

![](./images/811870784287932416_5.jpg)

Fig. 4. Comparison of the layerwise average order parameter profile across the film for three times ($t = 50$, 500 and 10000, respectively) according to the lattice model (open symbols) and the TDGL theory (full symbols), for $D = 29$, $k_BT/J = 5.875$, and $H_1/J = 1$. From Das et al. $^{50}$

is comparable. Since we found that one can work in the lattice approach with a relatively large time increment $(\delta t=0.1)^{50}$ and still keep a reasonable accuracy, it is clear that the lattice approach is to be preferred when one wants to maintain the relation to a microscopic model, such as the Ising model with boundary fields (Eqs. (4)-(8)) in the present case. On the other hand, the approach of Sec. 4 takes much less computer resources than a Monte Carlo simulation of that model would take (at the same level of accuracy).

## 7. Conclusions

In this paper, the state of the art of the theory of surface effects on spinodal decomposition was reviewed, with an emphasis on the Kawasaki spin exchange kinetic Ising model in the presence of free surfaces at which (in magnetic language) surface fields act. Even for this simple model, the complicated interplay between the formation of (precursors of) wetting layers and lateral phase separation parallel to the walls is not fully understood.

We have emphasized a recent approach where this lattice model is solved numerically in the framework of a local molecular field theory in terms of the inhomogeneous magnetization distribution $m_{n}(\boldsymbol{\rho}, t)$ in the thin film. This approach is much faster than Monte Carlo simulation. The latter approach, however, would be preferable when one is interested in the precise description of very early stages (where thermal fluctuations matter) and in the region near the actual critical point of the model (which occurs at $k_{B} T / J \approx 4.51$ ). $^{67}$ Note also that our lattice molecular field approach cannot describe any nucleation phenomena correctly, since thermal fluctuations are neglected, and hence would fail in the bulk near the spinodal curve (Fig. 1) and also near the walls when heterogeneous nucleation should occur (which is the case in the incomplete wetting region near first-order wetting transitions $^{52-55}$ ). Nevertheless this approach has advantages in comparison with the TDGL theory, which has been found to become quantitatively equivalent to the lattice molecular field theory only extremely close to the bulk molecular field critical temperature. We also note that a generalization of the lattice approach to more realistic lattice models of alloys $^{73-78}$ is conceivable. However, derivation of a theory for surface effects on spinodal decomposition in fluid binary mixtures (so far accessible only by Molecular Dynamics methods $^{22,23,83}$ ) remains a challenge: already the counterpart to the simple molecular field theory in equilibrium for inhomogeneous Ising systems with walls (Eqs. (10)-(13)) requires for off-lattice fluids the use of the density functional approach. $^{84}$ Extension of this approach to fluid mixtures far from equilibrium is an unsolved challenge.

## Acknowledgments

This paper owes a lot to joint research with Prof. Harry L. Frisch (see Ref. 51) who passed away in 2007. We dedicate this paper to his memory. Stimulating interactions with Prof. S. Puri are acknowledged. We are grateful to the Deutsche Forschungsgemeinschaft (DFG) for support under grant No TR6/A5.

### References

1.  J. W. Cahn, *Acta Metall.* **9** (1961) 795.
2.  J. D. Gunton, M. San Miguel and P. S. Salni, *Phase Transitions and Critical Phenomena*, Vol. 8, eds. C. Domb and J. L. Lebowitz (Academic Press, London, 1983), p. 267.
3.  S. Komura and H. Furukawa (eds.), *Dynamics of Ordering Processes in Condensed Matter* (Plenum Press, New York, 1988).
4.  A. J. Bray, *Adv. Phys.* **43** (1994) 357.
5.  K. Binder and P. Fratzl, *Phase Transformations in Materials*, ed. G. Kostorz (Wiley-VCH, Weinheim, 2001), p. 409.
6.  A. Onuki, *Phase Transition Dynamics* (Cambridge University Press, Cambridge, 2002).
7.  V. G. Vaks, *Phys. Rep.* **391** (2004) 157.
8.  T. Hashimoto, *J. Polym. Sci., Part B: Polym. Phys.* **42** (2004) 3027.
9.  S. Dattagupta and S. Puri, *Dissipative Phenomena in Condensed Matter: Some Applications* (Springer, Berlin, 2004).
10. S. Puri and V. Wadhavran (eds.), *Kinetics of Phase Transitions* (CRC Press, Boca Raton, 2009).
11. J. W. Cahn and J. E. Hilliard, *J. Chem. Phys.* **31** (1959) 688.
12. K. Binder and D. Stauffer, *Adv. Phys.* **25** (1976) 343.
13. K. Binder, *Phys. Rev. A* **29** (1984) 341.
14. K. Binder, *Rep. Prog. Phys.* **50** (1987) 783.
15. F. S. Bates and P. Wiltzius, *J. Chem. Phys.* **91** (1989) 3258.
16. I. M. Lifshitz and V. V. Slyozov, *J. Phys. Chem. Solids* **19** (1961) 35.
17. K. Binder and D. Stauffer, *Phys. Rev. Lett.* **33** (1974) 1006.
18. K. Binder, *Phys. Rev. B* **15** (1977) 4425.
19. E. Siggia, *Phys. Rev. A* **20** (1979) 595.
20. M. San Miguel, M. Grant and J.D. Gunton, *Phys. Rev. A* **31** (1985) 1001.
21. H. Furukawa, *Phys. Rev. A* **31** (1985) 1103.
22. S. K. Das, S. Puri, J. Horbach and K. Binder, *Phys. Rev. Lett.* **96** (2006) 016107.
23. S. K. Das, S. Puri, J. Horbach and K. Binder, *Phys. Rev. E* **73** (2006) 031604.
24. P. C. Hohenberg and B. I. Halperin, *Rev. Mod. Phys.* **49** (1977) 435.
25. R. A. L. Jones, L. J. Norton, E. J. Kramer, F. S. Bates and P. Wiltzius, *Phys. Rev. Lett.* **66** (1991) 1326.
26. P. Wiltzius and A. Cumming, *Phys. Rev. Lett.* **66** (1991) 3000.
27. S. Puri and K. Binder, *Phys. Rev. A* **46** (1992) R4487.
28. G. Brown and A. Chakrabarti, *Phys. Rev. A* **46** (1992) 4829.
29. H. Tanaka, *Phys. Rev. Lett.* **70** (1993) 53.
30. H. Tanaka, *Europhys. Lett.* **24** (1993) 665.
31. B. Q. Shi, C. Hamson and A. Cumming, *Phys. Rev. Lett.* **70** (1993) 206.
32. G. Krausch, C. A. Dai, E. J. Kramer and F. S. Bates, *Phys. Rev. Lett.* **71** (1993) 3669.
33. G. Krausch, C. A. Dai, E. J. Kramer and F. S. Bates, *Macromolecules* **27** (1994) 6768.
34. S. Puri and K. Binder, *Phys. Rev. E* **49** (1994) 5359.
35. S. Puri and K. Binder, *J. Stat. Phys.* **77** (1994) 145.
36. G. Krausch, *Mater. Sci. Eng.* **R14** (1995) 1.
37. S. Puri and H. L. Frisch, *J. Phys.: Condens. Matter* **9** (1997) 2109.
38. K. Binder, *J. Nonequilibrium Thermodyn.* **23** (1998) 1.
39. M. Geoghegan, H. Ermer, G. Jüngst, G. Krausch and R. Breen, *Phys. Rev. E* **62** (2000) 940.

40. H. Wang and R. J. Composto, *J. Chem. Phys.* **113** (2000) 10386.

41. S. Puri and K. Binder, *Phys. Rev. Lett.* **86** (2001) 1797.

42. S. Puri and K. Binder, *Phys. Rev. E* **66** (2002) 061602.

43. H. Tanaka, *J. Phys.: Condens. Matter* **13** (2002) 4637.

44. H. Jinnai, H. Kitagishi, K. Hamano, Y. Nishikawa and M. Takahashi, *Phys. Rev. E* **67** (2003) 021801.

45. M. Geoghegan and G. Krausch, *Prog. Polym. Sci.* **28** (2003) 261.

46. S. Puri, *J. Phys.: Condens. Matter* **17** (2005) R101.

47. S. K. Das, S. Puri, J. Horbach and K. Binder, *Phys. Rev. E* **72** (2005) 061603.

48. I. C. Henderson and N. Clarke, *Macromol. Theory Simul.* **14** (2005) 435.

49. J.-I. Fukuda, M. Yoneya and H. Yokoyama, *Phys. Rev. E* **73** (2006) 066706.

50. S. K. Das, J. Horbach and K. Binder, *Phys. Rev. E* (2009) in press.

51. K. Binder and H.L. Frisch, *Z. Phys. B: Condens. Matter* **84** (1991) 403.

52. P. G. de Gennes, *Rev. Mod. Phys.* **57** (1985) 827.

53. S. Dietrich, *Phase Transitions and Critical Phenomena*, Vol. 12, eds. C. Domb and J. L. Lebowitz (Academic Press, London, 1988), p. 1.

54. D. Bonn and D. Ross, *Rep. Prog. Phys.* **64** (2001) 1085.

55. K. Binder, D. P. Landau and M. Müller, *J. Stat. Phys.* **110** (2003) 1411.

56. G. Forgacs, R. Lipowsky and T. M. Nieuwenhuizen, *Phase Transitions and Critical Phenomena*, Vol. 14, eds. C. Domb and J. L. Lebowitz (Academic Press, London, 1991), Chap. 2.

57. H. Tanaka, *J. Phys.: Condens. Matter* **12** (2000) R207.

58. A. Budkovsky, *Adv. Polym. Sci.* **148** (1999) 1.

59. K. Kawasaki, *Phase Transitions and Critical Phenomena*, Vol. 2, eds. C. Domb and M. S. Green (Academic Press, London, 1972), Chap. 11.

60. S. K. Das, S. Puri, J. Horbach and K. Binder, *Phys. Rev. E* **73** (2006) 031604.

61. K. Binder and P.C. Hohenberg, *Phys. Rev. B* **6** (1972) 3461.

62. R. J. Glauber, *J. Math. Phys.* **4** (1963) 29.

63. C. P. Flynn, *Point Defects and Diffusion* (Clarendon Press, Oxford, 1972).

64. R. Kutner, K. W. Kehr and K. Binder, *Phys. Rev. B* **39** (1989) 4891.

65. K. Yaldram and K. Binder, *Acta Metall.* **39** (1991) 707.

66. K. Yaldram and K. Binder, *J. Stat. Phys.* **62** (1991) 161.

67. K. Binder and D. W. Heermann, *Monte Carlo Simulation in Statistical Physics. An Introduction*, 4th edn. (Springer, Berlin, 2002).

68. D. P. Landau and K. Binder, *A Guide to Monte Carlo Simulation in Statistical Physics*, 3rd edn. (Cambridge University Press, Cambridge, 2009).

69. J. Marro, A. B. Bortz, M. H. Kalos and J. L. Lebowitz, *Phys. Rev. B* **12** (1975) 2000.

70. J. G. Amar, F. E. Sullivan and R. D. Mountain, *Phys. Rev. B* **37** (1988) 196.

71. S. K. Das and S. Puri, *Phys. Rev. E* **65** (2002) 026141.

72. T. M. Rogers and R. C. Desai, *Phys. Rev. B* **39** (1989) 11965.

73. K. Binder, *Z. Phys.* **267** (1974) 313.

74. G. Martin, *Phys. Rev. B* **41** (1990) 2279.

75. F. Haider, P. Bellon and G. Martin, *Phys. Rev. B* **42** (1990) 8274.

76. G. Martin and P. Bellon, *Solid State Phys.* **50** (1997) 189.

77. K. D. Belashchenko, V. Yu. Dobretsov, I. R. Pankratov and G. Vaks, *J. Phys.: Condens. Matter* **11** (1999) 10593.

78. V. G. Vaks and I. R. Pankratov, *Zh. Eksp. Teor. Fiz.* **124** (2003) 114; *JETP* **97** (2003) 168.

79. V. Yu. Dobretsov, V. G. Vaks and G. Martin, *Phys. Rev. B* **54** (1996) 3227.

80. H. W. Diehl and H.-K. Janssen, *Phys. Rev. A* **45** (1992) 7140.

Surface-Directed Spinodal Decomposition 565

81. M. E. Fisher, *Rev. Mod. Phys.* **46** (1974) 587.

82. K. Binder and D. P. Landau, *Phys. Rev. B* **37** (1988) 1745.

83. G. Porod, *Kolloid Z.* **124** (1951) 83.

84. K. Bucior, L. Yelash and K. Binder, *Phys. Rev. E* **77** (2008) 015602.

85. D. Henderson (ed.), *Fundamentals of Inhomogeneous Fluids* (Marcel Dekker, New York, 1992).