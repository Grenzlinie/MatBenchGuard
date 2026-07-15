PHYSICAL REVIEW B 72, 104102 (2005)

# Critical behavior of an elastic Ising antiferromagnet at constant pressure

Xiaoliang Zhu, F. Tavazza, and D. P. Landau

Center for Simulational Physics, The University of Georgia, Athens, Georgia 30602, USA

B. Dünweg
Max Planck Institute for Polymer Research, Ackermannweg 10, D-55128, Mainz, Germany

(Received 16 June 2005; published 2 September 2005)

We perform Monte Carlo simulations of a model for a binary alloy exhibiting superstructure formation with two sublattices, in the constant-pressure semigrand canonical ensemble. This corresponds to an elastic antiferromagnetic Ising model, where spins sit on a distortable diamond net and the interaction is described by the Stillinger-Weber potential. We find a phase transition line separating the disordered from the ordered phase. The finite-size scaling analysis of the critical behavior shows no deviations from three-dimensional Ising behavior. This would be expected in the rigid limit of the model, while for the compressible case, as realized by our model, theory predicts a weak, first-order transition.

DOI: 10.1103/PhysRevB.72.104102
PACS number(s): 64.60.Cn, 05.10.Ln, 64.60.My, 81.30.Dz

## I. INTRODUCTION

The Ising model is among the most important and most intensely studied models of statistical physics. Its critical behavior is quite well understood, based on different approaches like renormalization group, $\epsilon$ expansion, series expansions, $^{1-4}$ and Monte Carlo (MC) simulations, $^{5,6}$ which have all provided quite accurate values for critical parameters. Although the model is formulated in a "magnetic" language, it is only rarely applicable to real magnetic systems. This is due to the scalar nature of the order parameter. Typical Ising-type transitions therefore include, for instance, the gas-liquid transition, and unmixing in liquids, where the composition corresponds to the magnetization, and the chemical potential difference to the magnetic field.

In a solid, important phase transitions with a scalar order parameter (and hence possible candidates for Ising-type behavior) are (i) the unmixing of a binary alloy (corresponding to ferromagnetic ordering), and (ii) the formation of a simple superstructure which is described by just two sublattices (corresponding to antiferromagnetic ordering). However, taking into account the elastic deformability of the lattice, i.e., the coupling of the compositional and translational degrees of freedom, the phase transitions need not necessarily remain Ising-type. Due to the long-range nature of the elastic interaction, fundamentally different kinds of behavior are possible, including first-order transitions, Fisher renormalization of the critical exponents, and mean-field behavior. This "zoo" arises from certain details (see below) playing an important role, such that various cases need to be distinguished. The main source of our current understanding of these phenomena is theoretical reasoning based on simple (usually field-theoretic) Hamiltonians. To our knowledge, it has not been attempted to attack these questions experimentally in a systematic fashion. This is understandable, since rather high resolution would be necessary; furthermore, some of the theoretically interesting situations are hard if not impossible to realize. Numerical simulations of these systems, $^{7-14}$ which are significantly more complicated than the "bare" Ising model, could only attain the necessary resolution within (roughly) the last decade. It is in this field where the present study attempts to make a contribution.

One of the present authors has recently $^{15}$ attempted a survey of the pertinent theoretical literature, in order to obtain an overview over the possible cases and various predictions. For a sketch of the underlying reasoning, and references to the original papers, see the Appendix. So far, the following aspects have been identified as being important for the critical behavior of elastic alloys: First, the *nature of the coupling* is crucial. Depending on the order parameter symmetry, the lowest-order coupling term can either be written as a product of order parameter and strain, or *square* of the order parameter and strain. The former case applies to unmixing, the latter to superstructure formation—in this case, a sign change of the order parameter just corresponds to an exchange of sublattices, which is a valid symmetry operation, and hence a linear term is prohibited. Second, the critical behavior is influenced by *macroscopic constraints, or the thermodynamic ensemble* (plus boundary conditions). Since it turns out that the macroscopic fluctuations (i.e., those at wave number $\vec{k}=0$) are crucial for the critical behavior, it makes a difference whether the ensemble permits these fluctuations or not. For example, the constant-pressure ensemble allows fluctuations of the overall volume, but the constant-volume ensemble does not. Similarly, a simulation of a binary alloy in the semigrand canonical ensemble allows $\vec{k}=0$ fluctuations of the composition (or magnetization, which is the order parameter in the case of unmixing), while they are suppressed in the canonical ensemble. The resulting nonequivalence of ensembles was first noticed by Vandeworp and Newman. $^{12}$ This is intimately related to the difference between coherent and incoherent phase coexistence as it is well known from metallurgy. $^{16,17}$ A coherent alloy is one characterized by a single crystal with well-defined neighbor shells. The condition of coherency, i.e., of absence of broken bonds, usually implies that the system is in a metastable state. Conversely, an incoherent alloy is one where bond breaking is permitted; this additional relaxation mechanism then allows the system to reach full equilibrium. Coherency usually implies the oc

1098-0121/2005/72(10)/104102(10)/$23.00
104102-1
©2005 The American Physical Society

currence of internal stresses, which are most pronounced near the interface of two components with different lattice spacings. Since the semigrand canonical ensemble avoids the explicit treatment of the interface, and the associated coherency stresses, such a simulation produces the incoherent phase diagram (or some approximation thereof). Conversely, data obtained in the canonical ensemble (with fixed composition) pertain to the situation with an interface, and with coherency stresses (note that the computational models explicitly forbid bond breaking). Therefore, this yields the coherent phase diagram. For these reasons we may not infer the coherent canonical phase diagram from semigrand canonical data. For a more detailed elaboration on that point, see Ref. 12. Finally, it is also believed that *elastic anisotropy* plays a role in the critical behavior of elastic alloys.

For an elastic lattice gas in the semigrand ensemble (i.e., the composition is always allowed to fluctuate), the following predictions arise from the picture outlined in the Appendix:

(1) A ferromagnet at constant pressure should exhibit a first-order coexistence line in the field-temperature plane. The line ends in a critical point with mean-field behavior. This has indeed been observed in the simulations of Refs. 9 and 10.

(2) For a ferromagnet at constant volume, the theoretical situation is not quite clear. For intermediate volumes which enforce an intermediate lattice spacing somewhere in between those of the two pure species, one expects that a mixed state is stabilized by elasticity. If one then assumes¹⁵ that this mixed state is just a coexistence of two macroscopic domains, with an interfacial free energy which does not contribute in the thermodynamic limit, one arrives at the prediction of two first-order lines ending in critical points. However, simulations¹⁴ have shown that this assumption is apparently incorrect: One rather finds a region in the phase diagram which is completely separated from the homogeneous phase by two merging first-order lines. Within this region, the structures are much more complicated than simple macroscopic domains. This is further corroborated by additional simulations¹⁸ which have carefully studied interface fluctuations in such a system: It turns out that capillary waves are completely suppressed, implying that the interfacial tension is indeed infinite.

(3) An antiferromagnet, since it couples quadratically to the strain, should correspond precisely to what is known as the "compressible Ising model" in the literature. In the case of constant pressure, a (very weak) first-order phase transition is predicted. A Monte Carlo study of the 2D compressible Ising antiferromagnet also found the transition is weakly first order and possibly second order when the coupling increased.¹⁹

(4) In the constant-volume case, the prediction is rather a second-order phase transition with Fisher-renormalized critical exponents. A recent MC simulation, however, found Ising-type critical behavior.²⁰

The present study is an attempt to test the prediction of case 3 by simulations. For this purpose, we slightly modify the model of Ref. 10 and introduce a nearest-neighbor interaction which favors antiferromagnetic ordering. This is then simulated at constant zero pressure. The details of the model and the simulation technique are outlined in Sec. II. Section III then presents the results on the phase diagram, and on the critical behavior, obtained via a standard finite-size scaling analysis. Within the resolution of our data, it was impossible to detect any deviation from standard Ising criticality. In Sec. IV we attempt to assess the influence of the elastic degrees of freedom, i.e., to determine how far the model deviates from a rigid Ising model. Finally, Sec. V concludes with a brief discussion.

## II. BACKGROUND

### A. Model and method

In order to make contact with previous simulation results of an analogous ferromagnetic system,¹⁰ we just modify this model slightly. Reference 10 had attempted to provide a semirealistic description of the unmixing of the semiconductor alloy Si-Ge. As an interaction potential, the Stillinger-Weber (SW) potential,²¹ suitably generalized to the binary case, was chosen. Other potentials for such systems have been proposed as well,²²⁻²⁴ but we view the SW potential as a good compromise between computational simplicity and realistic description of the system's properties. The only change compared to Ref. 10 is a modification of the nearest-neighbor interaction such that unlike neighbor pairs are favored. It should be noted that this choice of parameters implies that the present study makes no attempt to study some particular semiconductor alloy in a realistic fashion.

For reasons of computational efficiency, the particles are located on the nodes of a diamond network with fluctuating bonds but fixed topology. Although the nodes can move stochastically, the four nearest neighbors and the 12 next-nearest neighbors of a given node are known at the very beginning, and this information is used throughout the simulation. Each node has four degrees of freedom: The first one is a pseudospin variable $S_i$, which is either $+1$ or $-1$, corresponding to the two species of the alloy. The other three are the node's spatial coordinates, $\vec{r}_i$.

The diamond lattice can be decomposed into two interpenetrating fcc sublattices. In the totally ordered antiferromagnetic phase, the spins of the two sublattices are oppositely aligned. A further decomposition of the diamond lattice into eight simple cubic (SC) sublattices is useful for computational purposes; no two nodes within the same SC sublattice interact with each other.

The Hamiltonian consists of four parts
$$
\mathcal{H}=\mathcal{H}_{1}+\mathcal{H}_{1}^{+}+\mathcal{H}_{2}+\mathcal{H}_{3}, \tag{1}
$$
where $\mathcal{H}_{1}$ and $\mathcal{H}_{1}^{+}$ are the uniform magnetic field energy and staggered magnetic field energy, respectively
$$
\mathcal{H}_{1}=-h \sum_{j} S_{j}, \tag{2}
$$
$$
\mathcal{H}_{1}^{+}=-h^{+} \sum_{j} S_{j}^{+}. \tag{3}
$$
The staggered spin $S_{j}^{+}$ is defined as

$$
S_{j}^{+}=
\begin{cases}
S_{j} & \text{if } S_{j} \text{ is in fcc sublattice a} \\
-S_{j} & \text{if } S_{j} \text{ is in fcc sublattice b}.
\end{cases}
$$

The staggered magnetization $M^{+}$, also called the order parameter, is the summation of all $S_{j}^{+}$
$$
M^{+}=\sum_{j} S_{j}^{+}. \tag{4}
$$

The two-body part $\mathcal{H}_{2}$ can be written as
$$
\mathcal{H}_{2}=\sum_{\langle i,j\rangle} \epsilon(S_{i},S_{j})F_{2}[r_{ij}/\sigma(S_{i},S_{j})], \tag{5}
$$
and the three-body part is
$$
\begin{aligned}
\mathcal{H}_{3}=& \sum_{\langle i,j,k\rangle} \left[\epsilon(S_{i},S_{j})\epsilon(S_{j},S_{k})\right]^{1/2}\mathcal{L}(S_{i},S_{j},S_{k}) \\
& \times F_{3}[r_{ij}/\sigma(S_{i},S_{j}),r_{jk}/\sigma(S_{j},S_{k})]\left(\cos \theta_{ijk}+\frac{1}{3}\right)^{2}. \tag{6}
\end{aligned}
$$

The two-body part $\mathcal{H}_{2}$ and three-body part $\mathcal{H}_{3}$ together give the SW potential energy. For a detailed description of the involved functions and the chosen set of parameters, see Ref. 10. The only change is that we decrease $\epsilon(+1,-1)$, the covalent binding energy between unlike species, from the original value $-2.0427$ eV to $-2.3427$ eV to make the system antiferromagnetic. The choice of this new value is arbitrary as long as it is lower than the corresponding energies for like species, $\epsilon(+1,+1)=-2.17$ eV and $\epsilon(-1,-1)=-1.93$ eV.

Our MC simulation is performed as follows. For spin $S_{j}$ at position $\vec{r}_{j}$, we generate a new spin $S_{j}'$ at a slightly altered position $\vec{r}_{j}'$, and then use the Metropolis rejection method to accept or reject this attempt. The maximum displacement in a step is 0.005 times the length of unit cell in each of the $x$, $y$, and $z$ directions. After sweeping over the entire system, we keep the pressure constant and allow volume fluctuations by attempting to rescale the system to slightly different linear sizes $\Lambda_{x}'$, $\Lambda_{y}'$, $\Lambda_{z}'$ from the current ones: $x'$ $=x\Lambda_{x}'/\Lambda_{x}$, $y'=y\Lambda_{y}'/\Lambda_{y}$, $z'=z\Lambda_{z}'/\Lambda_{z}$. The acceptance or rejection of this attempt is determined by the Metropolis rejection method using the effective Hamiltonian, $\mathcal{H}_{eff}=\mathcal{H}$ $-Nk_{B}T\ln(\Lambda_{x}\Lambda_{y}\Lambda_{z})$, where $N$ is the number of nodes. A Tausworthe (shift-register) generator$^{25}$ is used to generate random numbers, and the magic numbers are $p=1279$, $q=1063$. All floating point quantities are double precision. The code is parallelized so that it runs on multiple processors with different random number sequences simultaneously. The multiple random number sequences diversify the data and improve the data quality used for histogram reweighting. Our system sizes are up to $L=24$, or $N=8L^{3}=110\ 592$. The number of spins is $N=8L^{3}$ because each diamond unit cell has 8 spins. All simulation runs are over $10^{7}$ Monte Carlo steps (MCS, sweeps through the entire lattice).

### B. Finite-size scaling analysis

According to Fisher's finite-size scaling theory, $^{26,27}$ the critical behavior of an infinite system may be extracted from that of finite systems by examining the size dependence of the singular part of the free-energy density. The free energy of a system of linear dimension $L$ is described by the scaling ansatz
$$
F(L,T,h)=L^{-(2-\alpha)/\nu}\mathcal{F}^{0}(tL^{1/\nu},hL^{(\gamma+\beta)/\nu}), \tag{7}
$$
where $t=(T-T_{c})/T_{c}$ ($T_{c}$ is the infinite-lattice critical temperature) and $h$ is the staggered magnetic field. The critical exponents $\alpha$, $\beta$, $\gamma$, and $\nu$ are all the appropriate values for the infinite system. Based on this scaling ansatz, we may obtain the following scaling form in zero field $h=0$:
$$
m^{+}=L^{-\beta/\nu}\tilde{m}(x_{t}), \tag{8}
$$
where $x_{t}=tL^{1/\nu}$ is the temperature scaling variable, and $m^{+}$ $=(1/8L^{3})M^{+}$ is the staggered magnetization per spin.

The specific heat capacity $C$ is calculated from the fluctuation of internal energy $E$
$$
C=\frac{1}{8L^{3}}\frac{1}{T^{2}}(\langle E^{2}\rangle-\langle E\rangle^{2}), \tag{9}
$$
where we use a unit system in which the Boltzmann constant is unity. Furthermore, the staggered finite-lattice susceptibility is obtained from the fluctuation relation
$$
\chi^{+}=\frac{8L^{3}}{T}(\langle |m^{+2}|\rangle-\langle |m^{+}|\rangle^{2}), \tag{10}
$$
while the Binder cumulant$^{28}$ is given by
$$
U_{4}=1-\frac{\langle m^{+4}\rangle}{3\langle m^{+2}\rangle^{2}}. \tag{11}
$$

Then, we also have the following scaling forms:
$$
C(T)=L^{\alpha/\nu}\tilde{C}(x_{t}), \tag{12}
$$

$$
\chi^{+}(T)=L^{\gamma/\nu}\tilde{\chi}(x_{t}), \tag{13}
$$

$$
U_{4}(T)=\tilde{U}(x_{t}). \tag{14}
$$

The finite-lattice (or effective) critical temperature $T_{c}(L)$ is defined to be where the scaling function reaches a maximum, or, in the case of the cumulant, has maximum slope. If the effective critical coupling $K_{c}(L)$ is defined to be the reciprocal of the effective critical temperature, $K_{c}(L)=1/T_{c}(L)$, then the following scaling form holds:
$$
K_{c}(L)=K_{c}+\lambda L^{-1/\nu}(1+bL^{-\omega}), \tag{15}
$$
where $K_{c}$ is the critical coupling of the infinite lattice, and $\omega$ is the correction-to-scaling exponent.

Binder$^{28}$ showed that the maximum slope of the cumulant $U_{4}$ at $K_{c}$ varies with system size like $L^{1/\nu}$. Taking into account a correction term, the size dependence becomes
$$
\left.\frac{dU_{4}}{dK}\right|_{max}=aL^{1/\nu}(1+bL^{-\omega}). \tag{16}
$$

The logarithmic derivative of any power of the staggered magnetization

$$
\frac{\partial}{\partial K} \ln \left\langle m^{+n}\right\rangle=\frac{1}{\left\langle m^{+n}\right\rangle} \frac{\partial}{\partial K}\left\langle m^{+n}\right\rangle=-\left[\frac{\left\langle m^{+n} E\right\rangle}{\left\langle m^{+n}\right\rangle}-\langle E\rangle\right],
\tag{17}
$$

has the same scaling properties as the cumulant slope. This provides us with additional estimates for $\nu$ and $K_{c}(L)$.

### C. Histogram reweighting method

The histogram reweighting technique $^{29}$ proposed by Ferrenberg and Swendsen has proved to be very effective. It yields excellent results in the neighborhood of the point where a sufficient MC simulation is performed. We rewrite the Hamiltonian of the system as follows:
$$
\mathcal{H}=-h M-h^{+} M^{+}+W,
\tag{18}
$$
where $W$ is the SW potential energy, $W=\mathcal{H}_{2}+\mathcal{H}_{3}$. A MC simulation of length $N$ performed at temperature $T_{0}$, uniform magnetic field $h_{0}$, and staggered magnetic field $h_{0}^{+}$generates $N$ configurations with a distribution frequency proportional to the Boltzmann weight, $\exp \left[-K_{0} \mathcal{H}\right]$, where $K_{0}=1 / T_{0}$. If we fix $h=0$ and $h^{+}=0$, and reweight over temperature, then the expectation value of an operator $A$ at $K=1 / T$ is given by
$$
\langle A\rangle_{K}=\frac{1}{Z} \sum_{j}^{N} A\left(W_{j}\right) \exp \left[-\left(K-K_{0}\right) W_{j}\right],
$$
where
$$
Z=\sum_{j}^{N} \exp \left[-\left(K-K_{0}\right) W_{j}\right].
$$

In histogram reweighting, it is necessary to check the histogram distribution. The reweighted mean internal energy should not be too far away from the center (or the maximum value) of the histogram. Otherwise, systematic errors will prevail. In practice, we require that
$$
H(\text { reweighted mean internal energy }) \geqslant 0.22 H_{\max },
$$
where $H$ is the histogram value, and $H_{\max }$ is the maximum histogram value. This guarantees that the reweighted mean internal energy is within 2 standard deviations from the center of the histogram.

## III. RESULTS

### A. Phase diagram

The field dependence and temperature dependence of specific heat and staggered susceptibility are shown in Fig. 1. These properties reach maxima at slightly different points. The staggered susceptibility exhibits smaller fluctuations and diverges with the system size much faster than the specific heat, which makes it an ideal indicator for critical points.

We determine the critical points along the phase boundary by locating the points where the staggered susceptibility reaches a maximum. In the plane $T-h$ (temperature-field, where $h$ is the uniform magnetic field thermodynamically conjugated to the concentration) we find a single phase boundary separating a disordered state from an ordered antiferromagnetic state, as shown in Fig. 2(a). The phase diagram is approximately (actually, within error bars) symmetric around the maximum. This is a nontrivial aspect, since it is not dictated by an obvious symmetry of the Hamiltonian (in contrast to symmetry with respect to the staggered field; note also that the symmetry axis is *not* located at $h=0$ ). The corresponding phase diagram in the temperature-concentration plane, which exhibits a similar symmetry, is shown in Fig. 2(b). An interesting feature of this is that the temperature-concentration curve turns slightly inward at low temperature. We believe this low-temperature behavior is

![](./images/812138459878653953_1.jpg)

FIG. 1. The field- and temperature-dependence of specific heat and susceptibility. The left two plots [(a) and (b)] show the temperature dependence at fixed field. The right two [(c) and (d)] show the field dependence at fixed temperature. Two systems of different sizes are used to show the finite size effects.

![](./images/812138459878653953_2.jpg)

FIG. 2. (a) shows the phase diagram in magnetic field-temperature space, and (b) in concentration-temperature space. The system size is $6 \times 6 \times 6$. Each simulation length is $10^{6}$ MCS. The error bars are smaller than the sizes of data symbols.

![](./images/812138459878653953_3.jpg)

FIG. 3. The order parameter distributions at the critical temperature. Also shown for comparison is the rigid 3D Ising universal distribution (solid line) according to Ref. 6. The distributions have been scaled to unit variance. Here, $\sigma_m$ is the standard deviation of the staggered magnetization $m^+$. Error bars are smaller than the symbol sizes except for $L=18$, where they are smaller than twice the symbol sizes.

real, because it occurs consistently in different runs, and the difference (0.0039) to the concentration at $T=0.1$ exceeds the standard deviation (0.0014). We have, however, not carefully investigated this interesting phenomenon.

### B. Critical behavior
In what follows, we will present data which show that, within the resolution of our simulation, the phase transformation can be perfectly described by a second-order transition with the critical exponents of the three-dimensional Ising universality class. A first, rather direct indication comes from the order parameter distribution at the critical point (we will describe below how we locate it accurately). In Fig. 3, all distributions for different system sizes collapse to the universal 3D Ising distribution function.

The estimation of critical parameters was then done as follows: First, we extracted $\nu$ by considering the scaling behavior of certain thermodynamic derivatives, including the derivative of the cumulant $U_4$, and the logarithmic derivatives of $|m^+|$, $|m^+|^2$, as in Ref. 5. We plot these properties as a function of lattice size on a log-log scale in Fig. 4.

The estimates for $1/\nu$ from the nonlinear least-square fits are given in Table I. Combining these three estimates, we get $1/\nu$=$1.60{\pm}0.01$. This agrees with the value $(1.594{\pm}0.004)$ reported for the rigid case$^5$ within 1 standard deviation. Therefore, our estimate for $\nu$ is $0.625{\pm}0.004$. The size of the error bars comes primarily from the statistical errors in our simulation. Since this is an elastic Ising model, i.e., spin positions are continuous variables, we cannot utilize the same ultrafast multispin coding algorithm as in Ref. 5; therefore, we cannot handle very large systems such as $L=96$. With relatively modest lattice sizes, we expect a noticeable correction term denoted by $\omega$. However, we find $\omega$ is extremely volatile, ranging from 0.6 to 4.5. This volatility also comes from the statistical errors in our data, which submerge the correction terms.

We find that the elasticity has a strong effect on the critical transition temperature. In the absence of elasticity, the model becomes a rigid Ising model on a diamond lattice, whose transition temperature is known to be $T_c^{diamond}$=$2.704\ 04|J|$.$^{30}$ With $|J|=|2\epsilon(+1,-1)-\epsilon(+1,+1)-\epsilon(-1,-1)|/4$, the transition would be $k_BT_c$=$0.14\ 635$ eV, less than half of the transition temperature found in our simulation. We fitted the data to Eq. (15) by fixing $1/\nu$=$1.60$, $\omega$=$1.0$, and varying $K_c$, $\lambda$, and $b$. The choice $\omega$=$1.0$ is not necessarily optimal, but it works very well. In fact, previous works$^5$ have suggested $\omega$=$1.0$. The results are shown in Fig. 5 and Table II. Almost all data agree with the fitted data within 1 standard deviation, and all agree within 2 standard deviations. The average of these values is $3.204\ 44{\pm}0.000\ 19$. This corresponds to the critical temperature $k_BT_c$=$0.312\ 067{\pm}0.000\ 018$ eV. Our error bars are bigger than those in the rigid case due to the added complexity.

![](./images/812138459878653953_4.jpg)

FIG. 4. Log-log plot of the maximum slopes of various thermodynamic quantities used to determine $\nu$. The straight lines show the nonlinear least-square fit of Eq. (16). All data points agree within 1 standard deviation.

The Binder cumulant $U_4$ scales with the linear system size $L$ as Eq. (14). At the critical temperature $T_c$, the $U_4(T)$ curves of all lattice sizes should have the same value $\tilde{U}(0)$, which would be a crossing point of all curves in Fig. 6. The crossing value is one of the universal properties, which determines the university class to which the model belongs. Due to finite lattice size effects, the curves do not cross exactly at the same point, but have their crossing points change systematically for small systems. For large systems, no systematic variation is visible. By averaging the crossing points for $L$ $\geqslant 10$, we find that this crossing value is $0.472{\pm}0.002$. This is the same as that in the universality class of the rigid three-dimensional Ising model.

TABLE I. Estimates for $1/\nu$ obtained by finite size scaling of the maximum slopes of the cumulant and the logarithmic derivatives of $|m^+|^2$ and $|m^+|$.

<table>
<thead>
<tr>
<th>
</th>
<th>
$1/\nu$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$U_4$
</td>
<td>
$1.597{\pm}0.016$
</td>
</tr>
<tr>
<td>
$\ln|m^+|$
</td>
<td>
$1.607{\pm}0.006$
</td>
</tr>
<tr>
<td>
$\ln|m^+|^2$
</td>
<td>
$1.603{\pm}0.015$
</td>
</tr>
</tbody>
</table>

![](./images/812138459878653953_5.jpg)

FIG. 5. Size dependence of the finite-lattice critical temperature estimated from various properties. Data are shown with standard deviations. The solid lines are nonlinear least-square fits to Eq. (15).

We also estimate $\beta/\nu=0.5034\pm0.0035$ by scaling $|m^+|$ at $K_c$. The estimate for the exponent $\beta$ is then $\beta=0.315\pm0.004$, which is close to the consensus Monte Carlo rigid Ising result, $0.3263\pm0.0006$. $^{5,6}$ The exponent $\gamma/\nu$ is determined by the scaling behavior of the finite-lattice susceptibility defined in Eq. (10). The estimate is $\gamma/\nu=2.027\pm0.0045$, and the estimate for $\gamma$ is $\gamma=1.27\pm0.01$, which is also close to the rigid Ising result, $\gamma=1.242\pm0.007$. $^{5,6}$

All of the above analyses yield consistent results, i.e., the critical behavior is simple Ising-type.

## IV. ELASTICITY IN THE MODEL

We have seen that the critical transition temperature is quite different from that of the rigid model, but the phase transition still appears to belong to the universality class of rigid Ising model. Is this because the model is still too rigid to see the asymptotic behavior? To answer this question, we will assess the elasticity in our model in this section. However, this is a rather vague issue. The theory does not tell us how much elasticity is sufficient to see the deviation from Ising behavior. We have tried a number of approaches to assess the elasticity in the model, but these have so far not been able to produce a clear picture. Here, we will only show the bond length distribution as an assessment of elasticity. In Fig. 7, the bond length distributions are quite broad, with the half-height-width being about 20% of the mean value, which means our model is indeed very elastic. Figure 7 also shows the uniformity of elasticity in the system, because the bond length distribution of all sites and that of a single site agree very well and almost overlap with each other. Nonetheless, untangling the interplay between magnetic and elastic degrees of freedom remains a challenge.

TABLE II. Estimates for $K_c$ obtained by finite size scaling of locations of the maximum slopes (except $\chi^+$, where the maximum value is used) of various thermodynamic derivatives.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$K_c$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$U_4$</td>
      <td>3.204 50$\pm$0.000 64</td>
    </tr>
    <tr>
      <td>$\ln|m^+|^2$</td>
      <td>3.204 11$\pm$0.000 36</td>
    </tr>
    <tr>
      <td>$\ln|m^+|$</td>
      <td>3.204 54$\pm$0.000 30</td>
    </tr>
    <tr>
      <td>$\chi^+$</td>
      <td>3.204 53$\pm$0.000 32</td>
    </tr>
    <tr>
      <td>$|m|$</td>
      <td>3.204 52$\pm$0.000 50</td>
    </tr>
  </tbody>
</table>

![](./images/812138459878653953_6.jpg)

FIG. 6. The Binder cumulant crossing. The curves alternate in solid and dashed lines for clarity. They are smooth because the data points are reweighted from histograms, and can reach any resolution. Lattice sizes are shown on both ends of each curve.

## V. CONCLUSION

We have investigated the phase diagram and critical behavior of an elastic antiferromagnetic Ising model with SW potential. The simulations were performed at constant pres-

![](./images/812138459878653953_7.jpg)

FIG. 7. The bond length distribution (a)-(c) are normalized together so that their integrated areas reflect their relative concentrations. Plot (d) is the distribution of all bonds, which is the sum of (a), (b), and (c). Plot (e) shows the bond length distribution of a single site over time.

sure in a semigrand-canonical ensemble. The phase transition is found to be second order everywhere, which disagrees with the theory. The reason might be that the theory is overly simplified, or our lattice sizes are not large enough. Note that it is expected that deviations from rigid behavior should be much harder to detect than in the ferromagnetic case, where the coupling between order parameter and elastic strain is linear in the former, i.e., intrinsically much stronger than in the present case, where it is quadratic in the order parameter. By examining the critical exponents and the crossing point of the Binder cumulant, we find that the transition appears to belong to the universality class of the rigid, three-dimensional Ising model, but the possibility of a very slow crossover toward a first-order transition cannot be completely ruled out. If this happens, however, the lattice sizes that will be required to see this behavior will be far larger than those that are accessible using current computers and algorithms. We then have the intriguing situation in which either the theory is somehow incomplete, or much more challenging simulations are needed.

## ACKNOWLEDGMENTS

We would like to thank L. Cannavacciuolo for helpful discussions. Some of the calculations were performed at TACC (Texas Advanced Computing Center). This research was supported in part by NSF Grant No. DMR-0341874.

## APPENDIX: THEORETICAL BACKGROUND: PHASE TRANSITIONS IN ELASTIC ALLOYS FORMING A SIMPLE SUPERSTRUCTURE

It is easy to see that the Hamiltonian can be cast in the form

$$
\begin{aligned}
\mathcal{H}= & \sum_{i \neq j} J_{i j}\left(\left\{\vec{r}_{l}\right\}\right) S_{i} S_{j}+\sum_{i-j-k} J_{i j k}\left(\left\{\vec{r}_{l}\right\}\right) S_{i} S_{j} S_{k} \\
& -\sum_{i} H_{i}\left(\left\{\vec{r}_{l}\right\}\right) S_{i}+\mathcal{H}_{0}\left(\left\{\vec{r}_{l}\right\}\right).
\end{aligned}\qquad(A1)
$$

We now assume that the interaction constants are chosen such that the low-temperature phase of the system is an ordered superstructure which can be described by a simple decomposition into two sublattices, $a$ and $b$. We define sublattice magnetizations $m_{a}$ and $m_{b}$ via $m_{a}=(2 / N) \sum_{i \in a} S_{i}$ and $m_{b}=(2 / N) \sum_{i \in b} S_{i}$, as well as the total magnetization $m=(1 / 2)\left(m_{a}+m_{b}\right)$, and the antiferromagnetic order parameter, $\phi=(1 / 2)\left(m_{a}-m_{b}\right)$. Here, $N$ denotes the total number of lattice sites. If the elastic degrees of freedom were absent (i.e., if all $J \mathrm{~s}$ were just constants which do not depend on the atom coordinates), then the system would exhibit a second-order phase transition whose critical behavior falls into the universality class of the three-dimensional Ising model (note that the order parameter is one-dimensional).

For the elastic distortions, we choose the ground state of $\mathcal{H}_{0}$ as a reference state. Except for trivial translations and rotations of the overall system, this specifies both the atomic positions $\vec{r}_{i}^{(0)}$ and the size and shape of the overall system uniquely. The displacement $\vec{u}_{i}$ of the $i$ th atom, $\vec{u}_{i}=\vec{r}_{i}-\vec{r}_{i}^{(0)}$, can then be thought of as being composed of two contributions: First, the atom is displaced by a certain amount $\vec{u}_{i}^{(0)}$ but the system is kept macroscopically fixed; second, the overall system is subjected to a macroscopic strain described by a strain tensor $\overleftrightarrow{E}$ (which we assume to be symmetric, in order to eliminate trivial rotations)

$$
\vec{r}_{i}=(\overleftrightarrow{1}+\overleftrightarrow{E})\left(\vec{r}_{i}^{(0)}+\vec{u}_{i}^{(0)}\right),\qquad(A2)
$$

or

$$
\vec{u}_{i}=\vec{u}_{i}^{(0)}+\overleftrightarrow{E} \vec{r}_{i}^{(0)} ;\qquad(A3)
$$

in the second equation, we have linearized with respect to $\vec{u}_{i}^{(0)}$ and $\overleftrightarrow{E}$, assuming that the elastic distortions are small. In the disordered state, and in the vicinity of the phase transition, this is a reasonable assumption, since most of the local (atomic) distortions will cancel out (and this holds even if we confine ourselves to one sublattice only).

In order to demonstrate that a first-order phase transition is expected, we now switch to a field-theoretic description. In essence, the discussion is nothing but an abbreviated outline of the seminal paper by Larkin and Pikin. $^{31,32}$ It should be noted that the same result has also been obtained by other authors, $^{33-40}$ using slightly different formulations and/or theoretical approaches (in particular, the renormalization group).

First, we view the displacement as a continuous vector field $\vec{u}(\vec{r})$

$$
\vec{u}(\vec{r})=\overleftrightarrow{E} \vec{r}+\vec{u}_{0}(\vec{r}),\qquad(A4)
$$

and for the second part, for which the periodic boundary conditions apply, we write the Fourier expansion

$$
\vec{u}(\vec{r})=\overleftrightarrow{E} \vec{r}+\sum_{\vec{k} \neq 0} \sum_{\lambda} \tilde{u}_{\lambda}(\vec{k}) \vec{\epsilon}_{\lambda}(\vec{k}) \exp (i \vec{k} \cdot \vec{r}).\qquad(A5)
$$

Here, $\vec{k} \neq 0$ are the reciprocal lattice vectors of the undistorted system, while $\lambda=0,1,2$ is a polarization index: $\vec{\epsilon}_{\lambda}$ are orthogonal unit vectors $\left(\vec{\epsilon}_{\lambda} \cdot \vec{\epsilon}_{\mu}=\delta_{\mu \nu}\right)$, with $\vec{\epsilon}_{0} \equiv \hat{k}$ (unit vector in $\vec{k}$ direction) denoting the longitudinal polarization.

Instead of $\mathcal{H}_{0}$, we now consider the Hamiltonian of linear elasticity theory $^{41}$ (as discussed, we assume weak distortions)

$$
\mathcal{H}_{e l}=\int d^{d} \vec{r}\left(\frac{K}{2} e_{\alpha \alpha} e_{\beta \beta}+\mu \bar{e}_{\alpha \beta} \bar{e}_{\alpha \beta}\right).\qquad(A6)
$$

Here the integration runs over the volume of the (undistorted) system. $K>0$ and $\mu>0$ are bulk and shear modulus, respectively (for simplicity, the cubic anisotropy of the crystal is ignored), while $e_{\alpha \beta}$ is the strain tensor

$$
e_{\alpha \beta}=\frac{1}{2}\left(\frac{\partial u_{\alpha}}{\partial r_{\beta}}+\frac{\partial u_{\beta}}{\partial r_{\alpha}}\right),\qquad(A7)
$$

and $\bar{e}_{\alpha \beta}$ its traceless part

$$
\bar{e}_{\alpha \beta}=e_{\alpha \beta}-\frac{1}{d} \delta_{\alpha \beta} e_{\gamma \gamma}. \tag{A8}
$$

In these equations, $\alpha$ and $\beta$ denote Cartesian indices (for which we assume the Einstein summation convention), and $d$ is the spatial dimension. For the macroscopic strain $\vec{E}$ we introduce a similar decomposition into the trace $(E_{\alpha \alpha} \equiv E_{0})$ and traceless part $\bar{E}_{\alpha \beta}$. It is now straightforward to express $\mathcal{H}_{e l}$ in terms of the phonon modes $\tilde{u}_{\lambda}(\vec{k})$ and the macroscopic strain. Denoting the system volume with $V$, one finds

$$
\begin{aligned}
\frac{\mathcal{H}_{e l}}{V}= & \frac{K}{2} E_{0}^{2}+\mu \bar{E}_{\alpha \beta} \bar{E}_{\alpha \beta}+\frac{1}{2}\left[K+\left(2-\frac{2}{d}\right) \mu\right] \sum_{\vec{k}} k^{2}\left|\tilde{u}_{0}(\vec{k})\right|^{2} \\
& +\frac{\mu}{2} \sum_{\vec{k}} \sum_{\lambda=1}^{d-1} k^{2}\left|\tilde{u}_{\lambda}(\vec{k})\right|^{2}.
\end{aligned} \tag{A9}
$$

The most important feature is the fact that the long-wavelength longitudinal modes have a stiffness which is larger than that of the macroscopic distortion. This results in a singularity of the effective spin-spin interaction at $\vec{k}=0$, and it is this peculiarity which governs the critical behavior.

Furthermore, we consider the system at frozen-in atomic positions $\vec{r}_{i}=\vec{r}_{i}^{(0)}$. This is a standard antiferromagnetic Ising model, for which we can write the field-theoretic Landau- Ginzburg-Wilson Hamiltonian

$$
\mathcal{H}_{L G W}=\int d^{d} \vec{r}\left\{\frac{R}{2}(\nabla \phi)^{2}+\frac{r}{2} \phi^{2}+\frac{u}{4!} \phi^{4}\right\}. \tag{A10}
$$

Here, $\phi$ is the order parameter. It should be noted that the Hamiltonian must be strictly of even order in $\phi$, since the transformation $\phi \rightarrow-\phi$ just corresponds to an exchange (or relabeling) of sublattices, with respect to which it is of course invariant. Geometrically, this is facilitated by a trans- lation of the crystal such that the sublattices are mapped onto each other. Using the Fourier expansion

$$
\phi(\vec{r})=\sum_{\vec{k}} \tilde{\phi}(\vec{k}) \exp (i \vec{k} \cdot \vec{r})=\phi_{0}+\sum_{\vec{k} \neq 0} \tilde{\phi}(\vec{k}) \exp (i \vec{k} \cdot \vec{r}),
\tag{A11}
$$

the Hamiltonian can be written as

$$
\begin{aligned}
\frac{\mathcal{H}_{L G W}}{V}= & \frac{R}{2} \sum_{\vec{k}} k^{2}|\tilde{\phi}(\vec{k})|^{2}+\frac{r}{2} \sum_{\vec{k}}|\tilde{\phi}(\vec{k})|^{2} \\
& +\frac{u}{4!} \sum_{\vec{k}_{1} \vec{k}_{2} \vec{k}_{3}} \tilde{\phi}\left(\vec{k}_{1}\right) \tilde{\phi}\left(\vec{k}_{2}\right) \tilde{\phi}\left(\vec{k}_{3}\right) \tilde{\phi}\left(-\vec{k}_{1}-\vec{k}_{2}-\vec{k}_{3}\right).
\end{aligned}
\tag{A12}
$$

Finally, we study a coupling term between the order parameter and the phonons. Noting that it is not the displacement field but rather the strain that describes the distortions on a local scale, we seek an interaction term of lowest order in the latter (weak distortions). Furthermore, the coupling should also be of lowest order in the order parameter (weak deviations from the disordered phase), and be compatible with the symmetries of the system. This leads directly to

$$
\mathcal{H}_{c}=g \int d^{d} \vec{r} \phi(\vec{r})^{2} e_{\alpha \alpha}(\vec{r}), \tag{A13}
$$

for the following reasons: The lowest order in $\phi$ must be quadratic, since the coupling must also obey the fundamental symmetry $\phi \rightarrow-\phi$. For the strain, the lowest order is linear. Considering the invariance with respect to rotations (point symmetry of the crystal), one first notices that $\phi$ behaves as a scalar field. As the overall coupling must be a scalar, it must have the form $\phi^{2} g_{\alpha \beta} e_{\alpha \beta}$, where $g_{\alpha \beta}$ is a constant second-rank tensor (a property of the undistorted disordered crystal). However, in the cubic system the only invariant tensors are multiples of the unit tensor. Note that the sign of $g$ is not specified. Next, we introduce the variable $\psi(\vec{r})$ $=\phi(\vec{r})^{2}$, plus the corresponding Fourier expansion ( $\psi_{0}$ denoting the $\vec{k}=0$ component of $\psi$ ). In Fourier space we then have

$$
\frac{\mathcal{H}_{c}}{V}=g \phi_{0} E_{0}+i g \sum_{\vec{k} \neq 0} k \tilde{\psi}(\vec{k})^{\star} \tilde{u}_{0}(\vec{k}). \tag{A14}
$$

The further development is somewhat technical but rather straightforward. Since the phonon modes $\tilde{u}_{\lambda}(\vec{k})$ are Gaussian degrees of freedom, they can be integrated out exactly (with different behavior for longitudinal and transversal modes). This results in an effective Hamiltonian depending only on the order parameter and the macroscopic strain. The treatment of the latter depends on the ensemble: In our case, we do not allow macroscopic shear (hence, we can set $\bar{E}_{\alpha \beta}=0$ ), but volume fluctuations (which correspond to $E_{0}$, a variable which can hence be integrated out). One thus obtains for our case

$$
\frac{\mathcal{H}_{e f f}}{V}=\frac{\mathcal{H}_{L G W}}{V}-\frac{1}{2} \frac{g^{2}}{K} \psi_{0}^{2}-\frac{1}{2} \frac{g^{2}}{K+(2-2 / d) \mu} \sum_{\vec{k} \neq 0}|\tilde{\psi}(\vec{k})|^{2}.
\tag{A15}
$$

At this point, it is useful to introduce the constant

$$
J=\frac{g^{2}}{2}\left(\frac{1}{K}-\frac{1}{K+(2-2 / d) \mu}\right)>0, \tag{A16}
$$

such that we can write

$$
\frac{\mathcal{H}_{e f f}}{V}=\frac{\mathcal{H}_{L G W}}{V}-J \psi_{0}^{2}-\frac{1}{2} \frac{g^{2}}{K+(2-2 / d) \mu} \sum_{\vec{k}}|\tilde{\psi}(\vec{k})|^{2},
\tag{A17}
$$

where in the second term now all Fourier modes contribute. However, since

$$
V \sum_{\vec{k}}|\tilde{\psi}(\vec{k})|^{2}=\int d^{d} \vec{r} \psi(\vec{r})^{2}=\int d^{d} \vec{r} \phi(\vec{r})^{4}, \tag{A18}
$$

and we assume rather weak coupling, the second term can be absorbed into a redefinition of the fourth-order coupling constant $u$ of $\mathcal{H}_{L G W}$. Furthermore

$$
\psi_{0}=\frac{1}{V} \int d^{d} \vec{r} \psi(\vec{r})=\frac{1}{V} \int d^{d} \vec{r} \phi(\vec{r})^{2}=\sum_{\vec{k}}|\tilde{\phi}(\vec{k})|^{2},
$$

(A19)

such that the final effective Hamiltonian reads

$$
\frac{\mathcal{H}_{e f f}}{V}=\frac{\mathcal{H}_{L G W}}{V}-J\left(\sum_{\vec{k}}|\tilde{\phi}(\vec{k})|^{2}\right)^{2}.
$$

(A20)

The remaining fourth-order term is treated via a Hubbard-
Stratonovich transformation: With $\beta=1 / T$, we can write the
partition function (apart from irrelevant prefactors) as

$$
\begin{aligned}
Z & =\int \mathcal{D} \phi \exp \left\{-\beta \mathcal{H}_{L G W}(r)+\beta J V\left(\sum_{\vec{k}}|\tilde{\phi}(\vec{k})|^{2}\right)^{2}\right\} \\
& \sim \int_{-\infty}^{\infty} d x \int \mathcal{D} \phi \exp \left\{-\beta \mathcal{H}_{L G W}(r)-\frac{x^{2}}{4 \beta J V}-x \sum_{\vec{k}}|\tilde{\phi}(\vec{k})|^{2}\right\} \\
& =\int_{-\infty}^{\infty} d x \int \mathcal{D} \phi \exp \left\{-\beta \mathcal{H}_{L G W}\left(r+\frac{2}{\beta V} x\right)-\frac{x^{2}}{4 \beta J V}\right\} \\
& =\int_{-\infty}^{\infty} d x \exp \left\{-\beta V f\left(r+\frac{2}{\beta V} x\right)-\frac{x^{2}}{4 \beta V J}\right\} \\
& \sim \int_{-\infty}^{\infty} d y \exp \left\{-\beta V f(y)-\frac{\beta V}{16 J}(y-r)^{2}\right\}.
\end{aligned}
$$

(A21)

In these equations, we have (i) emphasized the dependence of $\mathcal{H}_{L G W}$ on the second-order coefficient $r$; (ii) made use of the fact that the term quadratic in $\tilde{\phi}$ can be combined with the second-order term of $\mathcal{H}_{L G W}$; (iii) integrated over the order parameter field—$f(r)$ denotes the (known) free-energy per unit volume of the rigid Ising model described by $\mathcal{H}_{L G W}(r)$—and (iv) introduced a variable transformation. Since the remaining integral is just one-dimensional, it is, in the thermodynamic limit $V \rightarrow \infty$, rigorously correct to replace the integration by just maximizing the argument of the expo-
nential

$$
f(y)+\frac{1}{16 J}(y-r)^{2} \stackrel{!}{=} \operatorname{Min},
$$

(A22)

or

$$
\frac{d f}{d y}=\frac{1}{8 J}(r-y).
$$

(A23)

The critical point of the rigid Ising model occurs at some value $y=r_{c}$, in the vicinity of which the free energy has the leading-order form

$$
f(y)= \begin{cases}-A_{+}\left|y-r_{c}\right|^{2-\alpha}, & y>r_{c} \\ -A_{-}\left|y-r_{c}\right|^{2-\alpha}, & y<r_{c} .\end{cases}
$$

(A24)

Here, $A_{+}>0, A_{-}>0$ are critical amplitudes. Nothing that $\alpha$ $>0$ in the three-dimensional Ising universality class, one thus finds that the graphical solutions of Eq. (A23) look ge- nerically as plotted in Fig. 8 (where, however, the "clarity" of the behavior is exaggerated—in order to make the devia-

![](./images/812138459878653953_8.jpg)

FIG. 8. Graphical solution of Eq. (A23). The numbers at the figure axes are arbitrary. Note also that the value of the exponent $\alpha$ was increased to $\alpha=0.4$ for better visibility of the plot.

tion of $d f / d y$ from a straight line clearly visible, we had to increase the value of $\alpha$ substantially). The system is driven through the transition by varying the parameter $r$, which cor- responds to shifting the straight line up and down. One clearly sees typical first-order behavior, where the system jumps from one stable solution to another one. Furthermore, one notes that upon increasing the coupling between compo- sitional and translational degrees of freedom, $J$ increases and the straight line becomes flatter. Correspondingly, the first- order jump increases, too. In the limit of vanishing coupling, one obtains an infinite slope, and only one solution, corre- sponding to the second-order phase transition of the rigid model.

A few final remarks are in order. First, it should be no- ticed that the present approach can easily be applied to other cases. In the constant-volume ensemble, one has to take into account that the variable $E_{0}$ is not to be integrated over but rather is a constant. This leads to an effective Hamiltonian of just the same form as Eq. (A20), however with a negative coupling $J$. Analytically continuing Eq. (A23) yields a simi- lar plot, just with the slope of the straight line reversed. One sees that in this case only one solution occurs (second-order transition). Furthermore, in the vicinity of the critical point this yields a nonlinear relationship between the "external" temperature $r$ and the "intrinsic" temperature $y$ correspond- ing to the rigid model, $|y-r_{c}|^{1-\alpha} \propto|r-r_{c}|$-in other words, one expects Fisher-renormalized critical exponents. $^{42}$

Similarly, one can also treat the case of an elastic alloy with no tendency to superstructure formation, e.g., the Si- Ge system studied in Ref. 9. Here, there is no intrinsic sym- metry $\phi \rightarrow-\phi$, and hence the coupling term is linear in $\phi$. Using the same formalism as above, one can show (for the case of constant pressure) rather easily that the system ex- hibits a mean-field-like second-order transition at a tempera- ture above the critical point of $\mathcal{H}_{L G W}$. Another way to see this is to directly assume that the strain is the primary order parameter-because of bilinear coupling it should not matter if one considers the strain in response to a given order pa- rameter field, as done here, or vice versa. Therefore, the sys- tem can be directly identified with one case, the so-called

"type-zero" transition, of Cowley's classification scheme$^{43}$ of structural phase transitions in solids. For type zero, mean-field behavior is predicted. Related systems (with identical theoretical predictions) are hydrogen in metals, $^{44}$ and collapsing polymer networks. $^{45}$ In contrast to the present case, the predicted behavior was not difficult to observe in a simulation. $^{9}$

Another important point to discuss is the neglect of cubic anisotropy in the elastic Hamiltonian. This case has been treated in Refs. 38-40 with renormalization group methods. For constant pressure, the prediction remains first order, while for constant volume the predicted behavior is somewhat more complicated (we refer the reader to the original literature).

$^{1}$G. A. Baker, B. G. Nickel, and D. I. Meiron, Phys. Rev. B $\textbf{17}$, 1365 (1978).

$^{2}$E. Brezin, J.-C. LeGuillou, and J. Zinn-Justin, Phys. Lett. $\textbf{47A}$, 285 (1974).

$^{3}$J.-C. LeGuillou and J. Zinn-Justin, Phys. Rev. B $\textbf{21}$, 3976 (1980).

$^{4}$J.-H. Chen, M. E. Fisher, and B. G. Nickel, Phys. Rev. Lett. $\textbf{48}$, 630 (1982).

$^{5}$A. M. Ferrenberg and D. P. Landau, Phys. Rev. B $\textbf{44}$, 5081 (1991).

$^{6}$H. W. Blöte, E. Luijten, and J. R. Heringa, J. Phys. A $\textbf{28}$, 6289 (1995).

$^{7}$P. C. Kelires and J. Tersoff, Phys. Rev. Lett. $\textbf{63}$, 1164 (1989).

$^{8}$P. C. Weakliem and E. A. Carter, Phys. Rev. B $\textbf{45}$, 13458 (1992).

$^{9}$B. Dünweg and D. P. Landau, Phys. Rev. B $\textbf{48}$, 14182 (1993).

$^{10}$M. Laradji, D. P. Landau, and B. Dünweg, Phys. Rev. B $\textbf{51}$, 4894 (1995).

$^{11}$E. M. Vandeworp and K. E. Newman, Phys. Rev. B $\textbf{52}$, 4086 (1995).

$^{12}$E. M. Vandeworp and K. E. Newman, Phys. Rev. B $\textbf{55}$, 14222 (1997).

$^{13}$C. Tzoumanekas and P. C. Kelires, Phys. Rev. B $\textbf{66}$, 195209 (2002).

$^{14}$F. Tavazza, D. P. Landau, and J. Adler, Phys. Rev. B $\textbf{70}$, 184103 (2004).

$^{15}$B. Dünweg, *Computersimulationen zu Phasenübergängen und Kritischen Phänomenen*, Habilitationsschrift, Universät Mainz, Germany (2000).

$^{16}$R. D. Doherty, in *Physical Metallurgy*, edited by R. W. Cahn and P. Haasen (Elsevier, Amsterdam, 1983), p. 933.

$^{17}$P. Fratzi, O. Penrose, and J. L. Lebowitz, J. Stat. Phys. $\textbf{95}$, 1429 (1999).

$^{18}$B. J. Schulz, B. Dünweg, K. Binder, and M. Müller, Phys. Rev. Lett. (to be published).

$^{19}$L. Gu, B. Chakraborty, P. L. Garrido, M. Phani, and J. L. Leb- owitz, Phys. Rev. B $\textbf{53}$, 11985 (1996).

$^{20}$L. Cannavacciuolo and D. P. Landau, Phys. Rev. B $\textbf{71}$, 134104 (2005).

$^{21}$F. H. Stillinger and T. A. Weber, Phys. Rev. B $\textbf{31}$, 5262 (1985).

$^{22}$J. G. Kirkwood, J. Chem. Phys. $\textbf{7}$, 506 (1939).

$^{23}$P. N. Keating, Phys. Rev. $\textbf{145}$, 637 (1966).

$^{24}$J. Tersoff, Phys. Rev. Lett. $\textbf{56}$, 632 (1986).

$^{25}$R. C. Tausworthe, Math. Comput. $\textbf{19}$, 201 (1965).

$^{26}$M. N. Barber, in *Phase Transitions and Critical Phenomena*, edited by C. Domb and J. L. Lebowitz (Academic, New York, 1983), Vol. 8.

$^{27}$M. E. Fisher and M. N. Barber, Phys. Rev. Lett. $\textbf{28}$, 1516 (1972).

$^{28}$K. Binder, Z. Phys. B: Condens. Matter $\textbf{43}$, 119 (1981).

$^{29}$A. M. Ferrenberg and R. H. Swendsen, Phys. Rev. Lett. $\textbf{61}$, 2635 (1988).

$^{30}$M. E. Fisher, Rep. Prog. Phys. $\textbf{30}$, 615 (1967).

$^{31}$A. I. Larkin and S. A. Pikin, Sov. Phys. JETP $\textbf{29}$, 891 (1969).

$^{32}$S. A. Pikin, Physica A $\textbf{194}$, 352 (1993).

$^{33}$J. Oitmaa and M. N. Barber, J. Phys. C $\textbf{8}$, 3653 (1975).

$^{34}$J. Sak, Phys. Rev. B $\textbf{10}$, 3957 (1974).

$^{35}$J. Bruno and J. Sak, Phys. Rev. B $\textbf{22}$, 3302 (1980).

$^{36}$J. Bruno and J. Sak, Phys. Rev. B $\textbf{22}$, 3319 (1980).

$^{37}$F. J. Wegner, J. Phys. C $\textbf{7}$, 2109 (1974).

$^{38}$D. J. Bergman and B. I. Halperin, Phys. Rev. B $\textbf{13}$, 2145 (1976).

$^{39}$M. de Moura, T. C. Lubensky, Y. Imry, and A. Aharony, Phys. Rev. B $\textbf{13}$, 2176 (1976).

$^{40}$T. Nattermann, J. Phys. A $\textbf{10}$, 1757 (1977).

$^{41}$L. D. Landau and I. M. Lifshitz, *Theory of Elasticity* (Butterworth-Heinemann, Oxford, 2002).

$^{42}$M. E. Fisher, Phys. Rev. $\textbf{176}$, 257 (1968).

$^{43}$R. A. Cowley, Phys. Rev. B $\textbf{13}$, 4877 (1976).

$^{44}$H. Wagner and H. Horner, Adv. Phys. $\textbf{23}$, 587 (1974).

$^{45}$L. Golubovic and T. C. Lubensky, Phys. Rev. Lett. $\textbf{63}$, 1082 (1989).