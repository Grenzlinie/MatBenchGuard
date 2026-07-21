![](./images/812464240232235008_1.jpg)

Fig. 1. Density of diffusing adatoms on a terrace of size $\ell$. The origin of the $x$-axis is chosen to be in the middle of the terrace.

an incorporation mechanism is crucial to achieve slope selection. However, one simplifying assumption of the model is an infinite Ehrlich-Schwoebel barrier.

In this article we will present in more detail the argument leading to slope selection and we will generalize our results using a continuous step dynamics model analogous to [4]. In Section 2 we will introduce our extension of the BCF theory and will discuss the relation to existing results (Sects. 2 and 3). Typical mound morphologies and the growth dynamics are compared in Section 4. Afterwards we will investigate the emergence of slope selection within the framework of this model (Sect. 5). We will show that the selected slope has a temperature-dependence which is solely determined by the Ehrlich-Schwoebel barrier. Hence, the determination of selected terrace widths in experiments would give direct insight into microscopic properties such as the Ehrlich-Schwoebel barrier. We confirm the predicted importance of the incorporation mechanism using a kinetic Monte-Carlo simulation of a solid-on-solid model in Section 6. Another effective downward current could be due to detachment from steps and subsequent desorption. We will show in Section 7 that slope selection cannot be achieved by these two processes alone. In Section 8 we will calculate the saturation profile in the limiting case of an infinite Ehrlich-Schwoebel barrier.

## 2 BCF theory

The model is based on the Burton-Cabrera-Frank model in $1+1$ dimensions. Within this framework the crystal surface is specified by the position and direction (upward or downward) of steps. However, the results can be applied to surfaces in $2+1$ dimensions if more or less straight and parallel steps are present. In this case the $1+1$ D height profile of the BCF theory represents a cross-section perpendicular to the step edges. Figure 1 shows the crystal surface from the point of view of the BCF-theory. It is a coarse grained view – the detailed positions of atoms are not important. However, the terraces of the height of one atomic monolayer (ML) can still be distinguished. The most fundamental assumption is that at each time $t$ the adatom concentration $\rho$ is a function of the step positions only. In other words, the diffusion of adatoms is considerably faster than the step velocity. Thus, the diffusion equation becomes

$$
\frac{\partial \rho}{\partial t}(x, t)=0=D \nabla^{2} \rho(x, t)+\frac{F}{a} \tag{1}
$$

where $D$ is the diffusion constant and $F/a$ is the flux density with $a$ denoting the lattice constant. Hence, $1/F$ is the time necessary in order to deposit one monolayer. Up to now, this equation was solved with special boundary conditions at $x=-\ell/2$ and $+\ell/2$ in the literature. Clearly, the boundary conditions are chosen depending on whether the terrace is a vicinal, a top, or a bottom terrace. In the following we will discuss the typical case of a vicinal terrace. The extension to top and bottom terraces is straightforward.

To include an incorporation mechanism it is necessary to extend the theory. We assume that there exists an incorporation radius such that all particles arriving close to a downward step within this radius immediately jump down the step edge. Moreover, this mechanism is assumed to be temperature independent since the adsorption energy of an arriving particle is much higher than typical diffusion barriers. Hence, one has to split the density of diffusing particles into two regions. The first region close to the upper edge where equation (1) holds, and the second one given by the incorporation radius close to the downward step where no particles arrive ($F=0$). To describe the motion of steps the flux of incorporated particles must be taken into account separately.

In the following we will discuss in detail the situation $\ell > R_{\rm inc}$ as sketched in Figure 1. For smaller terraces only one region exists and the calculations are much easier. Since our analytical calculations will show that $\ell > R_{\rm inc}$ is the generic case we concentrate on this situation.

The general one-dimensional solution of equation (1) is a parabola characterized by three parameters. In addition to the two diffusion equations, four boundary conditions are necessary to determine the adatom concentrations $\rho_1$ and $\rho_2$ (cf. Fig. 1):

$$
\rho_{1}(-\ell / 2)=0 \tag{2}
$$

$$
\rho_{1}(\ell / 2-R_{\mathrm{inc}})=\rho_{2}(\ell / 2-R_{\mathrm{inc}}) \tag{3}
$$

$$
\rho_{1}^{\prime}(\ell / 2-R_{\mathrm{inc}})=\rho_{2}^{\prime}(\ell / 2-R_{\mathrm{inc}}) \tag{4}
$$

$$
-D \rho_{2}^{\prime}(\ell / 2)=\frac{D}{\ell_{1}} \rho_{2}(\ell / 2). \tag{5}
$$

Condition (2) is for the special case of perfectly absorbing step edges. (3) and (4) are necessary to obtain a smooth density between regions 1 and 2. The left hand side of (5) is the particle current at the step edge. On the right hand side this is reformulated using the number of jump attempts $D\rho_2(\ell/2)$ multiplied by the probability of overcoming the Ehrlich-Schwoebel barrier $E_{\rm S}$. This probability is expressed as the inverse of a typical length $\ell_1$

$$
\frac{1}{\ell_{1}}=\frac{1}{a} \exp \left(-\frac{E_{\mathrm{S}}}{k_{\mathrm{B}} T}\right) \tag{6}
$$

where $a$ stands for the lattice constant.

![](./images/812464240232235008_2.jpg)

Fig. 2. Arrangement of steps around the bottom terrace of width $\ell$ between two mounds.

The resulting density distribution has the form indicated in Figure 1: a parabola in the upper region and linear close to the downward step. The detailed expressions of $\rho_1$ and $\rho_2$ are not of much interest since the evolution of the crystal is determined by the currents at the edges. In the following we will call $u(\ell)$ the upward current, i.e.

$$
\begin{aligned}
u(\ell) & =-D \rho_{1}^{\prime}(-\ell / 2) \\
& =-\frac{F}{2 a\left(\ell+\ell_{1}\right)}\left(\ell^{2}+2 \ell \ell_{1}-2 R_{\mathrm{inc}} \ell_{1}-{R_{\mathrm{inc}}}^{2}\right). \quad(7)
\end{aligned}
$$

The downward current due to diffusion (the contribution of the incorporation mechanism is not included) becomes

$$
\begin{aligned}
d(\ell) & =-D \rho_{2}^{\prime}(+\ell / 2) \\
& =\frac{F}{2 a\left(\ell+\ell_{1}\right)}\left(\ell-R_{\mathrm{inc}}\right)^{2}.
\end{aligned}
$$

Note, that these results are very similar to the corresponding equations (2.2) and (2.3) of reference [4] where no incorporation was considered. Setting $R_{\text {inc }}=0$ we regain their results.

The absence of a dependence on $D$ reflects the ansatz of a quasi-stationary distribution. All arriving particles are compensated by the loss of particles at the borders and hence the currents are proportional to $F$. The density itself is proportional to the ratio $F/D$ which again is intuitively clear.

## 3 Closure of bottom terraces

In the following, we will reinvestigate the discussion of [4] concerning the closure of a bottom terrace (cf. Fig. 2). In the limiting case of an infinite Ehrlich-Schwoebel barrier the dynamics of the steps become very simple. We denote by $x(t)$ the position of the right step which of course will depend on the time $t$. The origin is chosen to be in the middle of the bottom terrace. Due to the infinite Ehrlich-Schwoebel barrier the movement of the right and the left step are symmetric. The evolution is then described by $\dot{x}(t)=-F x(t)-F R_{\text {inc }}$. The first term corresponds to the particles which do fall on the bottom terrace and diffuse to the right. The second term is the contribution of particles which are incorporated from the step above (which is valid as long as the bottom terrace is more than a distance $R_{\text {inc }}$ away from a top terrace). As a result $x(t)$ evolves as

$$
x(t)=\left(x_{0}+R_{\mathrm{inc}}\right) \exp (-F t)-R_{\mathrm{inc}}. \quad(9)
$$

As long as $R_{\text {inc }}>0$ there exists a closure time

$$
t_{\mathrm{c}}=\frac{1}{F} \ln \left(\frac{x_{0}+R_{\mathrm{inc}}}{R_{\mathrm{inc}}}\right). \quad(10)
$$

Without an incorporation mechanism $\left(R_{\text {inc }}=0\right)$ the bottom terrace will never be closed. This is the reason why Elkinani and Villain called their model the Zeno-model to remind the Greek philosopher and his paradox. Even though the situation is changed if the discrete structure of the terraces is considered $^{1}$ they showed that this trend still holds which gives rise to the formation of deep cracks. Likewise they found that even finite values of the Ehrlich-Schwoebel barrier do not change this growth scenario which has been investigated in more detail in [28]. Once mounds are built up they remain forever with a fixed lateral size. Our discussion of this limiting case shows that the inclusion of an incorporation mechanism changes the growth in a fundamental manner.

## 4 Growth dynamics

To set up the basic ideas of the behaviour during crystal growth we show two typical surface profiles according to the numerical integration of the step system. In Figure 3 we compare the resulting structure of the Zeno model [4] without an incorporation mechanism and with the inclusion of such a mechanism.

The simulations were carried out on on a system of $485 a$ width with parameters corresponding to the model of Section 6 (the temperature used is $T=550 \mathrm{~K}$ ):

$$
\begin{gathered}
D=10^{12} \exp \left(-\frac{0.9 \mathrm{eV}}{k_{\mathrm{B}} T}\right) \frac{a^{2}}{\mathrm{~s}} \approx 5664 \frac{a^{2}}{\mathrm{~s}} \\
\ell_{1}=\exp \left(+\frac{0.1 \mathrm{eV}}{k_{\mathrm{B}} T}\right) a \approx 8.2 a \\
R_{\mathrm{inc}}=1 a \\
F=1 \mathrm{ML} \mathrm{s}^{-1}.
\end{gathered}
$$

As in [4] the Ehrlich-Schwoebel barrier has been suppressed for bottom terraces of one lattice constant width. Without an additional incorporation mechanism the appearance of trenches is unavoidable in accordance to [28]. The incorporation mechanism gives rise to a well-defined slope which does not change with time. Another fundamental difference is the coarsening behaviour. Without an incorporation mechanism the trenches are stable and the number of mounds remains constant. The additional incorporation mechanism leads to a coarsening behaviour.

In lattice models as well as for continuum equations the coarsening is driven by fluctuations [29,26] and in $1+1$ dimensions the corresponding exponent is $1 / 3$. This is in accordance to Ostwald-ripening which has been predicted from the similarities of the relevant continuum

1 The currents can be translated into probabilities of placing a particle at the step edge. Hence, a bottom terrace of width one always has a nonvanishing probability to be filled.

![](./images/812464240232235008_3.jpg)

Fig. 4. We compare the morphology of the surfaces without (left) and with (right) an incorporation mechanism. Note that the two grey-scales are different. The heights in the left picture range from 1208 to 1326 whereas the right surface only spans a height difference of 12 from minimum to maximum. The contour lines are drawn for the same surface at an earlier stage where only 300 ML have been deposited. Without incorporation the mounds (towers) are nearly unchanged despite the deposition of 1000 ML.

Here, we concentrate on a particular set of parameters even though other parameter sets were used as well. We choose $\nu_0 = 10^{12}\ \mathrm{s}^{-1}$, $E_\mathrm{B} = 0.9\ \mathrm{eV}$, $E_\mathrm{N} = 0.25\ \mathrm{eV}$, and $E_\mathrm{S} = 0.1\ \mathrm{eV}$. This model was already investigated in [31] and reproduces some kinetic features of CdTe(001). The deposition of particles occurs with a rate $F$. The incorporation is simulated as follows: after a deposition site is chosen the particle is allowed to relax immediately to a lower neighbouring site if such a site is available. Only the four nearest neighbour sites are checked, hence $R_\mathrm{inc}=1a$.

The two simulations shown in Figure 4 are carried out on a $300\times300$ lattice at 560 K and started on a singular (flat) surface.

In Figure 4 the resulting surfaces with and without the inclusion of the incorporation mechanism are shown. Without an incorporation mechanism no slope selection occurs. Clearly, without incorporation the configuration of the towers remains unchanged whereas the inclusion leads to coarsening. The number of mounds diminishes with time. Accordingly, the surface width $w$ grows like $w\propto t^\beta$ with an exponent $\beta\approx1/3$ [32]. Without an incorporation mechanism no coarsening can be identified. The towers grow independently of each other and therefore, the surface width grows as in the case of random deposition like $w\propto t^{1/2}$ which is confirmed by the simulated data (not shown). We want to mention that it seems that at higher temperatures the attachment/detachment kinetics of atoms at step edges yields a coarsening effect (data not shown). However, still no slope selection has been observed.

At first glance our findings contradict previous results obtained with a very similar model. Šmilauer and Vvedensky obtained a formation of mounds with slope selection irrespective of the inclusion or exclusion of an incorporation mechanism [14]. However, they implemented the Ehrlich-Schwoebel barrier in a different way. Rather than to hinder the jump over a step edge they impede the jump towards a step edge. Their motivation for this implementation was to allow the adatoms to leave a small line of particles of width one which has been tested as a cause for reentrant layer-by-layer growth [23,30]. In our simulations the same goal is achieved by suppressing the Ehrlich-Schwoebel barrier in such a situation. However, in their simulations particles arriving directly at a step edge have a probability of $1/4$ to jump down the edge, $1/4$ to jump away from the edge and $1/2$ to jump along the step edge. Effectively this leads to an incorporation radius of length $1/2$.

Other simulations of SOS-models used bcc(001) [15,24] in order to study the growth of typical metals. In these simulations the SOS-restriction is implemented in such a way that an adatom must be supported by the four underlying atoms. Hence, the downward funneling process is directly implemented. Again, as a result slope selection is achieved, which has already been discussed in great detail in [25].

## 7 Detachment and desorption

One might assume that other mechanisms could lead to a zero in the slope dependent current. In the following we will carry out an analogous calculation with an adatom-detachment rate from steps and inclusion of desorption [33]. Both processes are likely to generate an effective downward current which can compensate for the Ehrlich-Schwoebel effect. Even though it is difficult to relate a stable slope to the surface diffusion current in the framework of continuum equations if desorption is included, one can still calculate attachment/detachment currents at the step edges in the framework of the BCF theory. Therefore, the determination of the selected slope using $J(\ell)$ is possible despite the missing volume conservation. To investigate whether the aforementioned processes are sufficient to obtain slope selection (and to simplify notation) we exclude the incorporation mechanism. Thus, the distinction of the two regions on a terrace is not necessary.

The desorption of diffusing adatoms is easily incorporated including a term $-\rho(x)/\tau$ in the diffusion equation (1) [33]. In order to include detachment from steps we have to replace boundary condition (2) by

$$
-D\rho'(-\ell/2)=\gamma-\frac{D}{a}\rho(-\ell/2)\tag{14}
$$

where $\gamma$ stands for the detachment rate from steps. Accordingly, the boundary condition at the downward step has to be corrected and reads now

$$
-D\rho'(\ell/2)=\frac{D}{\ell_1}\rho(\ell/2)-\gamma\frac{a}{\ell_1}\cdot\tag{15}
$$

The overall slope dependent current becomes

$$
J(\ell)=\frac{(\Delta-1)(\ell_1-a)\left(\frac{a\gamma}{\tau}-DF\right)}{(\ell_1+a)\sqrt{\frac{D}{\tau}}(\Delta+1)+\frac{a\ell_1}{\tau}(\Delta-1)+D(\Delta-1)}\tag{16}
$$