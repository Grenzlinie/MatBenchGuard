PHYSICAL REVIEW A 85, 053611 (2012)

# Finite-temperature phase diagram of a spin-1 Bose gas

Yuki Kawaguchi, $^{1}$ Nguyen Thanh Phuc, $^{1}$ and P. Blair Blakie $^{2}$

$^{1}$ Department of Physics, University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-0033, Japan
$^{2}$ Jack Dodd Centre for Quantum Technology, Department of Physics, University of Otago, Dunedin, New Zealand

(Received 31 January 2012; published 10 May 2012)

We formulate a self-consistent Hartree-Fock theory for a spin-1 Bose gas at finite temperature and apply it to characterization of the phase diagram. We find that spin coherence between thermal atoms in different magnetic sublevels develops via coherent collisions with the condensed atoms, and is a crucial factor in determining the phase diagram. We develop analytical expressions to characterize the interaction- and temperature-dependent shifts of the phase boundaries.

DOI: 10.1103/PhysRevA.85.053611
PACS number(s): 03.75.Mn, 05.30.Jp, 03.75.Hh

## I. INTRODUCTION

A key feature of a system with spin internal degrees of freedom is that the atoms can condense into a range of phases, characterized by various spin order parameters, dependent upon the nature of the interactions and the external magnetic field (e.g., see Fig. 1). The seminal theory for the spin-1 Bose gas was developed in 1998 [2,3] and soon after realized in experiments [4,5]. Aspects of the equilibrium phase diagram were initially observed in Ref. [4], and more recently experiments have used external fields to investigate the dynamical properties of this system (e.g., see Refs. [6–9]), including quenches between phases [10,11].

Several theoretical treatments within mean-field approximations have considered the equilibrium properties of a condensed spin-1 Bose gas at finite temperature [12–16]. Natu and Mueller have predicted that, for sufficiently large spin-dependent interaction strength, pairing or spontaneous magnetization will occur at slightly higher temperature than the condensation transition [17]. In the two-dimensional (2D) regime, where condensation is expected to be suppressed, the finite-temperature phase diagram has recently been elucidated [18,19].

This paper investigates the finite-temperature phase diagram of the spin-1 Bose gas, including both linear and quadratic Zeeman effects, which were not fully considered in previous work [12–14,16]. Figure 1 shows the mean-field phase diagram at $T=0$ drawn in the parameter space of the linear $(p)$ and quadratic $(q)$ Zeeman energies [1,4]. We investigate how the phase boundaries in Fig. 1 change as the temperature increases, using a Hartree-Fock (HF) mean-field theory. Although HF theory is the simplest many-body theory, it forms an important building block for more advanced many-body theories, and for comparison to other types of calculations. A key feature of our theory is the inclusion of spin coherence between noncondensate (thermal atoms) in different magnetic sublevels. We find that when the condensate is in a state of spontaneously broken spin rotational symmetry (about the direction of the applied field), i.e., in the antiferromagnetic and broken-axisymmetry phases, the spin coherence between noncondensed atoms also develops via coherent collisions with the condensed atoms. Moreover, the noncondensate spin coherence has a large effect on the phase boundaries in the finite-temperature regime. We derive analytical relations between the shifts in the phase boundaries and noncondensate spin density or spin coherence, which agree well with the full numerical results. These analytical results furnish additional insight into how the thermal fluctuations influence the condensate order and directly show the importance of the noncondensate spin coherence.

Finally, we note that HF calculations are generally expected to provide a good qualitative description of the interacting system. Indeed, HF theory accurately describes a range of thermodynamic measurements made on the scalar three-dimensional Bose gas (e.g., see [20–22]). However, the spinor situation is much less clear. Our recent work [16] suggests that the spinor gas, in the regime of current experiments with $^{87}$Rb, is strongly interacting, in the sense that the corrections to the Bogoliubov theory are nonperturbative. There also remain a number of open questions about the explanation of current experiments (e.g., see [8,11]) and what role thermal fluctuations, dipole-dipole interactions, or nonequilibrium effects play. The work we present here provides an important step toward achieving a more complete understanding of thermal effects in the spinor Bose gas.

## II. BASIC FORMALISM

We consider a spin-1 Bose gas confined in an optical potential $U(\mathbf{r})$ and subject to a uniform magnetic field along $z$. The single-particle description of the atoms is provided by the Hamiltonian

$$
\left(h_{0}\right)_{i j}=\left[-\frac{\hbar^{2} \nabla^{2}}{2 M}+U(\mathbf{r})-p i+q i^{2}\right] \delta_{i j}, \quad(1)
$$

where $p$ and $q$ are the coefficients of the linear and quadratic Zeeman terms, respectively, the subscripts $i, j=-1,0,+1$, refer to the magnetic sublevels of the atoms, and $M$ is the atomic mass. The value of $q$ is tunable independently of $p$, using an off-resonant microwave field [23].

Introducing spinor field operators $\hat{\psi}_{i}(\mathbf{r})$, the cold-atom Hamiltonian, including interactions, is given

1050-2947/2012/85(5)/053611(11)
053611-1
©2012 American Physical Society

![](./images/813310757566414856_1.jpg)

FIG. 1. (Color online) The $T = 0$ phase diagram of a spin-1 Bose gas for cases where the spin-dependent interaction is (a) antiferromagnetic ($c_1 > 0$) and (b) ferromagnetic ($c_1 < 0$). The vertical and horizontal axes are the linear and quadratic Zeeman energies (see text) in units of $|c_1|n$, where $n$ is the total number density (which is identical to the condensate number density at $T = 0$). The phases shown are (FM) ferromagnetic, (P) polar, (AFM) antiferromagnetic, and (BA) broken-axisymmetry phases (see Sec. IV A and Refs. [1,4]). The rotational symmetry about the direction of the applied field is spontaneously broken in the AFM and BA phases.

$$
\begin{aligned}
\hat{\mathcal{H}}= & \int d \mathbf{r}\left\{\sum_{i, j}\left[\hat{\psi}_{i}^{\dagger}(\mathbf{r})\left(h_{0}\right)_{i j} \hat{\psi}_{j}(\mathbf{r})\right.\right. \\
& \left.+\frac{c_{0}}{2} \hat{\psi}_{i}^{\dagger}(\mathbf{r}) \hat{\psi}_{j}^{\dagger}(\mathbf{r}) \hat{\psi}_{j}(\mathbf{r}) \hat{\psi}_{i}(\mathbf{r})\right] \\
& \left.+\frac{c_{1}}{2} \sum_{\alpha, i, j, k, l}\left(f_{\alpha}\right)_{i j}\left(f_{\alpha}\right)_{k l} \hat{\psi}_{i}^{\dagger}(\mathbf{r}) \hat{\psi}_{k}^{\dagger}(\mathbf{r}) \hat{\psi}_{l}(\mathbf{r}) \hat{\psi}_{j}(\mathbf{r})\right\}, \quad(2)
\end{aligned}
$$

where $\alpha = x$, $y$, or $z$ specifies the spin components, with $f_{\alpha}$ being the $3 \times 3$ spin-1 matrices. The parameters $c_0$ and $c_1$ are referred to as the spin-independent and spin-dependent interaction parameters, respectively, and are given by $c_0 = 4\pi\hbar^2(a_0 + 2a_2)/3M$, $c_1 = 4\pi\hbar^2(a_2 - a_0)/3M$, with $a_S$ ($S = 0,2$) being the $s$-wave scattering length for the scattering channel of total spin $S$.

### III. HARTREE-FOCK THEORY
#### A. General inhomogeneous theory

The basic mean-field approach is to assume that when there is a condensate in the system the field operator can be decomposed as
$$
\hat{\psi}_{i}(\mathbf{r})=\phi_{i}(\mathbf{r})+\hat{\delta}_{i}(\mathbf{r}),\qquad(3)
$$
where $\phi_i(\mathbf{r})$ is a classical field describing the condensate and the fluctuation operator $\hat{\delta}_i(\mathbf{r})$ describes the noncondensate modes. The HF equations can be derived by using a variational approach to minimize the free energy (e.g., see Appendix A and Refs. [24,25]). Key to this approach is the factorization of the expectation value of the interaction terms into expressions involving products of first-order correlation functions:
$$
\left\langle\hat{\psi}_{i}^{\dagger}(\mathbf{r}) \hat{\psi}_{j}(\mathbf{r})\right\rangle=n_{i j}^{\mathrm{c}}(\mathbf{r})+n_{i j}^{\mathrm{nc}}(\mathbf{r}),\qquad(4)
$$
where we have introduced the notation $n_{i j}^{\mathrm{c}}(\mathbf{r}) \equiv \phi_{i}^{*}(\mathbf{r}) \phi_{j}(\mathbf{r})$ and $n_{i j}^{\mathrm{nc}}(\mathbf{r}) \equiv\left\langle\hat{\delta}_{i}^{\dagger}(\mathbf{r}) \hat{\delta}_{j}(\mathbf{r})\right\rangle$ for the condensate and noncondensate one-body density matrices, respectively. $^1$ We emphasize that in the presence of a condensate, $n_{i j}^{\mathrm{nc}}(\mathbf{r})$ may have nonzero off-diagonal elements, that is, may exhibit partial phase coherence between thermal atoms in different magnetic sublevels. Since the Hamiltonian (2) is invariant under a spin rotation about the $z$ axis, $n_{i j}^{\mathrm{nc}}(\mathbf{r})$ should be diagonal in the normal phase (without pairing or ferromagnetic order [17]) so that the system is invariant under spin rotations. In a condensed phase, however, if the condensate spontaneously breaks the rotational symmetry in spin space, the noncondensate is also distributed inhomogeneously in spin space due to coherent collisions between condensed and noncondensed atoms. Noncondensate spin coherence was experimentally observed in a two-component Bose gas [26].

The generalized Gross-Pitaevskii equation (GPE) for the condensate is (see Appendix A)
$$
\mu \phi_{i}(\mathbf{r})=\sum_{j} L_{i j} \phi_{j}(\mathbf{r}),\qquad(5)
$$
where
$$
\begin{aligned}
L_{i j}= & \left(h_{0}\right)_{i j}+c_{0}\left(n^{\mathrm{c}}+n^{\mathrm{nc}}\right) \delta_{i j}+c_{0} n_{j i}^{\mathrm{nc}} \\
& +c_{1} \sum_{\alpha}\left[\left(F_{\alpha}^{\mathrm{c}}+F_{\alpha}^{\mathrm{nc}}\right)\left(f_{\alpha}\right)_{i j}+\sum_{k, l}\left(f_{\alpha}\right)_{i k}\left(f_{\alpha}\right)_{l j} n_{l k}^{\mathrm{nc}}\right]
\end{aligned}
\qquad(6)
$$
is the Gross-Pitaevskii matrix operator, and
$$
n^{\mathrm{c}}(\mathbf{r})=\sum_{i} n_{i i}^{\mathrm{c}}(\mathbf{r}),\qquad(7)
$$
$$
F_{\alpha}^{\mathrm{c}}(\mathbf{r})=\sum_{i, j}\left(f_{\alpha}\right)_{i j} n_{i j}^{\mathrm{c}}(\mathbf{r}),\qquad(8)
$$
$$
n^{\mathrm{nc}}(\mathbf{r})=\sum_{i} n_{i i}^{\mathrm{nc}}(\mathbf{r}),\qquad(9)
$$
$$
F_{\alpha}^{\mathrm{nc}}(\mathbf{r})=\sum_{i, j}\left(f_{\alpha}\right)_{i j} n_{i j}^{\mathrm{nc}}(\mathbf{r})\qquad(10)
$$
are the number and spin densities associated with the condensed and noncondensed atoms.

The HF grand-canonical Hamiltonian for the noncondensate is given by (see Appendix A)
$$
K_{\mathrm{HF}}=\int d \mathbf{r} \sum_{i, j} \hat{\delta}_{i}^{\dagger} A_{i j}(\mathbf{r}) \hat{\delta}_{j},\qquad(11)
$$
where
$$
A_{i j}=L_{i j}-\mu \delta_{i j}+c_{0} n_{j i}^{\mathrm{c}}+c_{1} \sum_{k, l}\left(f_{\alpha}\right)_{i k}\left(f_{\alpha}\right)_{l j} n_{l k}^{\mathrm{c}},\quad(12)
$$
i.e., differing from the condensate operator $L_{i j}$ by the inclusion of the exchange interactions with the condensate.

$^1$The full one-body density matrix also retains off-diagonal position arguments; however, these are not needed to formulate HF theory for a gas with contact interactions. In this work we will use the term off-diagonal in reference to the spin indices.

By finding the eigenvalues $(\epsilon_{\lambda})$ and eigenvectors $[u_{j}^{(\lambda)}(\mathbf{r})]$ of $A_{ij}$, i.e.,
$$
\epsilon_{\lambda} u_{i}^{(\lambda)}(\mathbf{r})=\sum_{j} A_{i j}(\mathbf{r}) u_{j}^{(\lambda)}(\mathbf{r}),\qquad(13)
$$
normalized so that
$$
\sum_{i} \int d \mathbf{r} u_{i}^{(\nu) *}(\mathbf{r}) u_{i}^{(\lambda)}(\mathbf{r})=\delta_{\nu \lambda},\qquad(14)
$$
the noncondensate density matrix is given by
$$
n_{i j}^{\mathrm{nc}}(\mathbf{r})=\sum_{\lambda} u_{i}^{(\lambda) *}(\mathbf{r}) u_{j}^{(\lambda)}(\mathbf{r}) \bar{n}_{\lambda},\qquad(15)
$$
where $\bar{n}_{\lambda}=1 /[\exp (\beta \epsilon_{\lambda})-1]$ is the Bose-Einstein distribution function with $\beta=1 /(k_{B} T)$.

### B. Specialization to the uniform system
For the purpose of studying the finite-temperature phase diagram we now discuss the specialization of the HF formalism to a uniform system. In this case $U(\mathbf{r}) \to 0$ and the mean fields $(n_{i j}^{c}$ and $n_{i j}^{nc})$ are spatially independent. The condensate occurs in the zero-momentum spatial mode, and the generalized GPE (5) reduces to the nonlinear algebraic equation
$$
\mu \phi_{i}=\sum_{j} \mathcal{L}_{i j} \phi_{j},\qquad(16)
$$
where
$$
\begin{aligned}
\mathcal{L}_{i j}= & \left(-p i+q i^{2}\right) \delta_{i j}+c_{0}\left[\left(n^{\mathrm{c}}+n^{\mathrm{nc}}\right) \delta_{i j}+n_{j i}^{\mathrm{nc}}\right] \\
& +c_{1} \sum_{\alpha}\left[\left(F_{\alpha}^{\mathrm{c}}+F_{\alpha}^{\mathrm{nc}}\right)\left(f_{\alpha}\right)_{i j}+\sum_{k, l}\left(f_{\alpha}\right)_{i k}\left(f_{\alpha}\right)_{l j} n_{l k}^{\mathrm{nc}}\right].
\end{aligned}
\qquad(17)
$$

The excited modes have plane-wave spatial dependence:
$$
u_{j}^{(\lambda)}(\mathbf{r})=\bar{u}_{j}^{(\nu)} e^{i \mathbf{k} \cdot \mathbf{r}},\qquad(18)
$$
where $\bar{u}_{j}^{(\nu)}$ is a constant spinor (and is independent of $\mathbf{k}$) and we have adopted the notation $\lambda \to \{\nu, \mathbf{k}\}$, with $\mathbf{k}$ a wave vector and $\nu$ an index to distinguish between modes.

The HF Hamiltonian takes the form
$$
A_{i j}=-\frac{\hbar^{2} \nabla^{2}}{2 M}+\mathcal{A}_{i j},\qquad(19)
$$
where
$$
\mathcal{A}_{i j}=\mathcal{L}_{i j}-\mu \delta_{i j}+c_{0} n_{j i}^{\mathrm{c}}+c_{1} \sum_{\alpha, k, l}\left(f_{\alpha}\right)_{i k}\left(f_{\alpha}\right)_{l j} n_{l k}^{\mathrm{c}} \quad(20)
$$
is a constant matrix. Notably the spatial and spin parts in Eq. (19) are decoupled and can be treated separately [allowing us to use the excited mode of the form given in Eq. (18)]. Diagonalizing $\mathcal{A}_{i j}$, we obtain the three eigenvectors $\bar{u}_{j}^{(\nu)}$ with respective eigenvalues $\kappa_{\nu}$, and hence the excitation spectrum is given by
$$
\epsilon_{\nu \mathbf{k}}=\frac{\hbar^{2} k^{2}}{2 M}+\kappa_{\nu}.\qquad(21)
$$

To evaluate the noncondensate one-body density matrix we set $\sum_{\lambda} \to(2 \pi)^{-3} \sum_{\nu} \int d \mathbf{k}$ in Eq. (15) and obtain
$$
n_{i j}^{\mathrm{nc}}=\sum_{\nu=1}^{3} \bar{u}_{i}^{(\nu) *} \bar{u}_{j}^{(\nu)} \frac{\mathrm{Li}_{3 / 2}\left(e^{-\beta \kappa_{\nu}}\right)}{\lambda_{\mathrm{dB}}^{3}},\qquad(22)
$$
where $\lambda_{\mathrm{dB}}=h / \sqrt{2 \pi M k_{\mathrm{B}} T}$ is the thermal de Broglie wave length and $\mathrm{Li}_{\sigma}(z) \equiv \sum_{t=1}^{\infty} z^{t} / t^{\sigma}$ is the polylogarithm. We note that for the thermal cloud to saturate, and hence condensation to occur, at least one of the eigenvalues $\kappa_{\nu}$ must approach zero at the condensation temperature.

## IV. RESULTS
The effect of the thermal cloud on the condensate is, in gen- eral, quite complicated and requires the full self-consistent cal- culation. We numerically solve the coupled Gross-Pitaevskii and HF equations self-consistently in the temperature range of $T=(0-0.5) T_{0}$, where $T_{0}$ is the condensation temperature of an ideal scalar gas with the same total number density. Because there are three internal states, the condensation temperature of an ideal spin-1 gas at $p=q=0$ is reduced to $T_{c}^{\text {spinor }}=(1 / 3)^{2 / 3} T_{0} \simeq 0.48 T_{0}$. For $^{87} Rb$ and $^{23} Na$ gases (in the $F=1$ hyperfine multiplet) the spin-dependent interaction is small relative to the spin-independent interaction $(c_{0} \sim$  $10^{2}|c_{1}|)$ ; however, for generality we explore larger values of up to $c_{1} / c_{0}= \pm 0.5$ , which might be realizable with new species of atoms, or using magnetic or optical manipulation of interatomic interactions.

### A. Identification of phases
For the system we consider here of a spin-1 Bose gas subject to a magnetic field, a variety of phases arise and are well characterized for the $T=0$ case (see Fig. 1). These phases are identified according to the properties of the condensate order parameter $(\phi_{1}, \phi_{0}, \phi_{-1})$ . Here, we briefly summarize the defining characteristics of each phase and discuss how we identify these phases in our HF calculations (for more details on the definition and properties of these phases, see Ref. [1]).

Ferromagnetic (FM) phase. The condensate order param- eter is of the form $(\sqrt{n^{c}}, 0,0)$ for $p>0$ . In this phase the condensate is fully magnetized along the direction of the applied field, i.e.,
$$
F_{\perp}^{\mathrm{c}}=0 \quad \text { and } \quad F_{z}^{\mathrm{c}} / n^{\mathrm{c}}=1,\qquad(23)
$$
where $F_{\perp}^{c}=[(F_{x}^{c})^{2}+(F_{y}^{c})^{2}]^{1 / 2}$ is the transverse spin density.

Antiferromagnetic (AFM) phase. The condensate order parameter is of the form $(\sqrt{n_{1,1}^{c}}, 0, \sqrt{n_{-1,-1}^{c}})$ . In this phase the condensate is partially magnetized along the direction of the applied field, i.e.,
$$
F_{\perp}^{\mathrm{c}}=0 \quad \text { and } \quad 0<F_{z}^{\mathrm{c}} / n^{\mathrm{c}}<1.\qquad(24)
$$

Polar $(P)$ phase. The condensate order parameter is of the form $(0, \sqrt{n^{c}}, 0)$ . In this phase the condensate is unmagnetized, i.e.,
$$
F_{\perp}^{\mathrm{c}}=0 \quad \text { and } \quad F_{z}^{\mathrm{c}} / n^{\mathrm{c}}=0.\qquad(25)
$$

Broken-axisymmetry (BA) phase. The condensate order parameter is of the form $(\sqrt{n_{1,1}^{c}}, \sqrt{n_{0,0}^{c}}, \sqrt{n_{-1,-1}^{c}})$ (see Ap pendix $C 1$ and Ref. [1] for more details). In this phase

![](./images/813310757566414856_2.jpg)

FIG. 2. (Color) Results of the HF calculation for antiferromagnetic interactions with $c_1/c_0=0.05$. (a) Temperature dependence of the phase diagram in $(q,p)$ space, where the FM-P and AFM-P phase boundaries are independent of temperature. The region of the AFM phase shrinks as the temperature increases. The longitudinal magnetization per atom of (b) the condensate and (c) the noncondensate at $T/T_0=0.1$. The transverse magnetizations are always zero for both condensed and noncondensed atoms.

the condensate is partially magnetized but tilts against the direction of the applied field, i.e.,
$$
F_\perp^\mathrm{c}>0.\tag{26}
$$

We use the conditions (23)–(26) to identify the phase of any self-consistent solution we obtain to the HF equations. Obtaining precise equality is not possible in finite-precision numerical calculations, and in practice we identify each phase when the appropriate equality (or inequality) is satisfied to one part in $10^4$ (e.g., we identify the ferromagnetic phase by requiring $F_z^\mathrm{c}/n^\mathrm{c}\geqslant0.9999$).

### B. Antiferromagnetic interactions

#### 1. Numerical results

The results for $c_1/c_0=0.05$ are summarized in Fig. 2. Figure 2(a) shows the temperature dependence of the $q$-$p$ phase diagram. The region of the P phase is unchanged, whereas the AFM–FM phase boundary moves downward as the temperature increases. Figures 2(b) and 2(c) are plots of the longitudinal magnetizations of condensate and noncondensate, respectively, at $T/T_0=0.1$. When the condensate is in the P phase, the noncondensate is magnetized in the $z$ direction due to the linear Zeeman effect. On the other hand, when the condensate is magnetized in the $z$ direction (i.e., in the FM and AFM phases), the noncondensate is magnetized antiparallel to the condensate. This is because the condensate mainly occupies the lowest Zeeman sublevel ($i=1$) in these phases, and therefore the residual noncondensate atoms prefer to populate the other spin states. This can be understood as follows: The noncondensed atoms in spin states different from the condensate interact with the condensate only via the direct (Hartree) term; in contrast, it is of higher energetic cost for noncondensate atoms to occupy the same spin state as the condensate because both the direct (Hartree) and exchange (Fock) terms contribute.

### 2. AFM-FM phase boundary

Here, we focus on the temperature dependence of the linear Zeeman energy $p_\mathrm{b}$ that specifies the AFM-FM phase boundary. The order parameter for the AFM phase is given by
$$
\begin{pmatrix}\phi_1\\phi_0\\phi_{-1}\end{pmatrix}=\begin{pmatrix}\sqrt{n_{1,1}^\mathrm{c}}\\0\\\sqrt{n_{-1,-1}^\mathrm{c}}\end{pmatrix},\tag{27}
$$
where we can choose $\phi_{\pm1}$ as positive real numbers without loss of generality, because the phases of $\phi_{\pm1}$ can be removed by a gauge transformation and a spin rotation about the $z$ axis. In other words, both the gauge transformation and spin rotation symmetries are spontaneously broken in the AFM phase. Since $n_{ij}^\mathrm{c}$ has the off-diagonal elements $n_{1,-1}^\mathrm{c}=n_{-1,1}^\mathrm{c}=\sqrt{n_{1,1}^\mathrm{c}n_{-1,-1}^\mathrm{c}}$, $n_{ij}^\mathrm{nc}$, in general, has the off-diagonal components
$$
\boldsymbol{n}^\mathrm{nc}=\begin{pmatrix}n_{1,1}^\mathrm{nc}&0&(n_{-1,1}^\mathrm{nc})^*\\0&n_{0,0}^\mathrm{nc}&0\\n_{-1,1}^\mathrm{nc}&0&n_{-1,-1}^\mathrm{nc}\end{pmatrix}.\tag{28}
$$

The generalized GPE (16) for the AFM phase reduces to
$$
\begin{pmatrix}-\tilde{p}-\tilde{\mu}&C_-n_{-1,1}^\mathrm{nc}\\C_-(n_{-1,1}^\mathrm{nc})^*&\tilde{p}-\tilde{\mu}\end{pmatrix}\begin{pmatrix}\phi_1\\phi_{-1}\end{pmatrix}=0,\tag{29}
$$
where
$$
\tilde{\mu}=\mu-\left(q+c_0n+c_1n_{0,0}^\mathrm{nc}+C_+\frac{n_{1,1}^\mathrm{nc}+n_{-1,-1}^\mathrm{nc}}{2}\right),\quad(30)
$$
$$
\tilde{p}=p-c_1F_z^\mathrm{c}-\frac{c_0+3c_1}{2}F_z^\mathrm{nc},\tag{31}
$$
$$
C_\pm=c_0\pm c_1,\tag{32}
$$
with $n=n^\mathrm{c}+n^\mathrm{nc}$. At $T=0$, Eq. (29) has an AFM solution ($\phi_{\pm1}\neq0$) when $\tilde{p}=0$, that is, $p=c_1F_z^\mathrm{c}$. From the fact that $F_z^\mathrm{c}=n^\mathrm{c}$ at the AFM-FM phase boundary, $p_\mathrm{b}$ at $T=0$ is given by
$$
\frac{p_\mathrm{b}}{c_1n}=1.\tag{33}
$$

At $T\neq0$, the condition that Eq. (29) has a nontrivial solution determines $\tilde{\mu}$. Substituting $\tilde{\mu}$ and the solution of $(\phi_1,\phi_{-1})$ into the HF equations and solving self-consistently, we obtain the following relation among $p$, $F_z^\mathrm{c}$, and $F_z^\mathrm{nc}$ in the

AFM phase:
$$
\begin{aligned}
p= & \frac{3 C_{+}-2 C_{-}}{4} F_{z}^{\mathrm{c}}+\frac{4 C_{+}-3 C_{-}}{4} F_{z}^{\mathrm{nc}} \\
& -\frac{1}{2} \sqrt{\left(\frac{C_{+} F_{z}^{\mathrm{c}}-C_{-} F_{z}^{\mathrm{nc}}}{2}\right)^{2}+C_{-}^{2} F_{z}^{\mathrm{c}} F_{z}^{\mathrm{nc}}}. \quad(34)
\end{aligned}
$$

The detailed derivation of Eq. (34) is given in Appendix B. Using the fact that $F_{z}^{\mathrm{c}}=n^{\mathrm{c}}$ at the AFM-FM phase boundary, and expanding Eq. (34) in terms of $F_{z}^{\mathrm{nc}} / n^{\mathrm{c}}$, the phase boundary is approximated as
$$
\frac{p_{\mathrm{b}}}{c_{1} n} \cong \frac{n^{\mathrm{c}}}{n}+\frac{3 c_{0}+c_{1}}{c_{0}+c_{1}} \frac{F_{z}^{\mathrm{nc}}}{n}. \quad(35)
$$

The right-hand side of Eq. (35) goes to unity as $T \to 0$, being consistent with Eq. (33). The first term on the right-hand side of Eq. (35) describes the shift in the boundary due to the thermal depletion of the condensate, while the second term describes the interaction of the noncondensed component back on the condensate and acts to reduce the value of $p_{\mathrm{b}}$ since $F_{z}^{\mathrm{nc}}<0$ [see Fig. 2(c)].

This result can be understood in terms of two underlying effects that compete against each other:

(i) The noncondensate magnetization $F_{z}^{\mathrm{nc}}(<0)$ increases the effective linear Zeeman energy [see Eq. (31)], i.e., increases the energy difference between the $i=1$ and $-1$ components of the condensate [see Eq. (29)]. This causes $|\phi_{1}|$ to increase relative to $|\phi_{-1}|$, and thus tends to reduce the value of $p_{\mathrm{b}}$ at the phase boundary (where $\phi_{-1}=0$).

(ii) The noncondensate spin coherence plays a nontrivial role through exchange (Fock) collisions between condensate and noncondensate atoms of the type $(i, \mathbf{0})+(j, \mathbf{k}) \leftrightarrow(i, \mathbf{k})+$ $(j, \mathbf{0})$: Off-diagonal elements of $n_{i j}^{\text {nc }}$ contribute to enhancing the coupling between $\phi_{1}$ and $\phi_{-1}$ [see Eq. (29)], thus acting to make $|\phi_{1}|$ and $|\phi_{-1}|$ more similar, and hence supporting the AFM phase (i.e., this effect tends to increase $p_{\mathrm{b}}$).

To quantify the competition between these two effects we neglect the noncondensate spin coherence by explicitly setting $n_{-1,1}^{\text {nc }}=0$ in Eq. (28) and calculate $p_{\mathrm{b}}$. In such a case, Eq. (29) has an AFM solution when $\tilde{p}=0$, resulting in
$$
\frac{p_{\mathrm{b}}}{c_{1} n}=\frac{n^{\mathrm{c}}}{n}+\frac{c_{0}+3 c_{1}}{2 c_{1}} \frac{F_{z}^{\mathrm{nc}}}{n}. \quad(36)
$$

The larger prefactor of the last term demonstrates that when noncondensate spin coherence is neglected [i.e., only effect (i) contributes] the phase boundary $p_{\mathrm{b}}$ is more significantly reduced.

Figure 3 shows the temperature dependence of $p_{\mathrm{b}}$ for a particular choice of the quadratic Zeeman energy $(q=-3 c_{1} n)$ obtained by the full HF calculation (I) and the HF calculation with the off-diagonal elements of $n_{i j}^{\text {nc }}$ neglected (II), $^{2}$ which show good agreement with Eqs. (35) and (36), respectively. The deviations of the curves I and II from $p_{\mathrm{b}} /(c_{1} n)=n^{\mathrm{c}} / n$ are the effects of the thermal components $(F_{z}^{\mathrm{nc}} / n)$. Note that the value of $p_{\mathrm{b}}$ significantly decreases when we neglect the spin coherence of the noncondensate. We find that the temperature dependence of the condensate fraction $n^{\mathrm{c}} / n$ and the noncondensate magnetization $F_{z}^{\text {nc }}$ are almost the same for I and II, so the difference in the phase boundaries arises from the coefficients of $F_{z}^{\mathrm{nc}} / n$ in Eqs. (35) and (36). For the case of the full HF calculation [Eq. (35)], $p_{\mathrm{b}}$ is insensitive to the value of $c_{1}$ as long as $c_{1} / c_{0} \ll 1$. On the other hand, Eq. (36) is strongly dependent on $c_{1} / c_{0}$, in particular when $c_{1} / c_{0}$ is small. We have also numerically calculated $p_{\mathrm{b}}$ for the interaction parameters of $c_{1} / c_{0}=0.005$ and 0.5. The results agree with Eqs. (35) and (36).

![](./images/813310757566414856_3.jpg)

FIG. 3. (Color online) Temperature dependence of the AFM-FM phase boundary $p_{\mathrm{b}}$ at $q=-3 c_{1} n$ and $c_{1} / c_{0}=0.05$ obtained by (I) the full HF calculation and (II) the HF calculation but neglecting the off-diagonal elements of $n_{i j}^{\text {nc }}$, together with the curves indicating $n^{\mathrm{c}} / n$, Eq. (35), and Eq. (36).

## C. Ferromagnetic interactions

### 1. Numerical results

The numerical results for $c_{1} / c_{0}=-0.05$ are summarized in Fig. 4. Figure 4(a) shows the temperature dependence of the $q-p$ phase diagram. The region of the FM phase is unchanged, whereas the BA-P phase boundary moves to the left-hand side as the temperature increases. Figures 4(b) and 4(c) are plots of the longitudinal and transverse magnetizations of condensate atoms, respectively, at $T / T_{0}=0.1$, and Figs. 4(d) and 4(e) show the same quantities for the noncondensate. In Fig. 4(e), $F_{\perp}^{\text {nc }}<0$ means that the transverse magnetization of the noncondensate is antiparallel to that of the condensate. As in the case of the AFM and FM phases of Fig. 2, the noncondensate magnetization is roughly antiparallel to that of the condensate, except for the vicinity of the BA-P phase boundary where the condensate magnetization becomes small.

### 2. BA-P phase boundary

We investigate the temperature dependence of the BA-P phase boundary $q_{\mathrm{b}}$ at $p=0$. In the BA phase at $p=0$ the condensate magnetization is purely transverse and vanishes at $q=q_{\mathrm{b}}$. Note that the numerical result [Fig. 4(e)] shows that the noncondensed component is also magnetized in the transverse direction (see also Ref. [16]), indicating the existence of spin coherence in the noncondensate. This is because the spin rotational symmetry about the $z$ axis is broken in the HF

$^{2}$ Irrespective of whether off-diagonal parts of $n_{i j}^{\text {nc }}$ arise, we include only the diagonal parts when evaluating the self-consistent HF Hamiltonian [see Eq. (20)].

![](./images/813310757566414856_4.jpg)

FIG. 4. (Color online) Results of the HF calculation for ferromagnetic interactions with $c_1/c_0=-0.05$. (a) Temperature dependence of the phase diagram in $(q,p)$ space, where the FM-BA phase boundary is independent of temperature. The region of the BA phase shrinks as the temperature increases. The longitudinal and transverse magnetization per atom at $T/T_0=0.1$ for (b),(c) the condensate and (d),(e) the noncondensate. In (e), $F_{\perp}^{\text{nc}}<0$ means that the transverse magnetization of the noncondensate is antiparallel to that of the condensate.

Hamiltonian (11) due to the existence of the transversely magnetized condensate.

At $T=0$, the BA-P phase boundary is given by [1]
$$
\frac{q_{\mathrm{b}}}{\left|c_{1}\right| n}=2.
\tag{37}
$$

At finite temperature, by solving the Gross-Pitaevskii and HF equations self-consistently, we obtain the following relation for the BA-P boundary (see Appendix C 1 for the derivation):
$$
\frac{q_{\mathrm{b}}}{\left|c_{1}\right| n} \cong 2 \frac{n^{\mathrm{c}}}{n}-\frac{4\left(3 c_{0}-5\left|c_{1}\right|\right)}{c_{0}-\left|c_{1}\right|} \frac{d^{\mathrm{nc}}}{n},
\tag{38}
$$

![](./images/813310757566414856_5.jpg)

FIG. 5. (Color online) Temperature dependence of the BA-P phase boundary $q_{\mathrm{b}}$ at $p=0$ and $c_1/c_0=-0.05$ obtained by (I) the full HF calculation and (II) the HF calculation but neglecting the off-diagonal elements of $n_{ij}^{\text{nc}}$, together with the curves indicating $2n^{\text{c}}/n$, Eq. (38), and Eq. (40).

where
$$
d^{\mathrm{nc}}=\frac{1}{2}\left(n_{1,1}^{\mathrm{nc}}-n_{0,0}^{\mathrm{nc}}+n_{-1,1}^{\mathrm{nc}}\right).
\tag{39}
$$

As in the case of antiferromagnetic interactions, the noncondensate spin coherence has a significant effect on the location of the phase boundary. If we neglect the off-diagonal elements of $n_{ij}^{\text{nc}}$, the phase boundary is changed to
$$
\frac{q_{\mathrm{b}}}{\left|c_{1}\right| n}=2 \frac{n^{\mathrm{c}}}{n}-\frac{c_{0}+\left|c_{1}\right|}{\left|c_{1}\right|} \frac{d^{\mathrm{nc}}}{n},
\tag{40}
$$
where $d^{\mathrm{nc}}$ is defined in Eq. (39) but with $n_{1,-1}^{\text{nc}}=0$. The derivation of Eq. (40) is given in Appendix C 2.

Figure 5 shows the temperature dependence of $q_{\mathrm{b}}$ at $p=0$ obtained by the full HF calculation (I) and the HF calculation with the off-diagonal elements of $n_{ij}^{\text{nc}}$ neglected (II), which show good agreement with Eqs. (38) and (40), respectively. The deviations of the curves I and II from $q_{\mathrm{b}}/(\left|c_1\right|n)=2n^{\mathrm{c}}/n$ are the effects of the noncondensate $(d^{\mathrm{nc}}/n)$. As in the case of Fig. $3$, $q_{\mathrm{b}}$ is greatly suppressed when we neglect the coherence of the noncondensate. The difference also comes from the coefficients of $d^{\mathrm{nc}}/n$ in Eqs. (38) and (40): Eq. (38) is insensitive to the value of $c_1$ as long as $|c_1|/c_0\ll1$; while Eq. (40) is strongly dependent on $c_1/c_0$, in particular when $|c_1|/c_0$ is small. We have also numerically calculated $q_{\mathrm{b}}$ for the interaction parameters of $c_1/c_0=-0.005$ and $-0.5$. The results agree with Eqs. (38) and (40).

The interpretation of the above results is similar to the case of antiferromagnetic interactions. In Eq. (39) the main contribution to $d^{\mathrm{nc}}$ comes from the population difference between $i=1$ and 0 components, $n_{1,1}^{\mathrm{nc}}-n_{0,0}^{\mathrm{nc}}(=n_{-1,-1}^{\mathrm{nc}}-n_{0,0}^{\mathrm{nc}}$ for $p=0)$, which induces an energy difference between condensed atoms in the $i=0$ and $\pm1$ components via the exchange (Fock) terms [the last terms in the first and second lines of Eq. (17)]. Hence, $d^{\mathrm{nc}}$ contributes to increasing $|\phi_0|$ relative to $|\phi_{\pm1}|$, and thus tends to reduce the value of $q_{\mathrm{b}}$. On the other hand, the off-diagonal elements of $n_{ij}^{\text{nc}}$, in particular $n_{\pm1,0}^{\text{nc}}$ and $n_{0,\pm1}^{\text{nc}}$, compete against this by coupling condensate atoms in $i=0$ and $\pm1$ states [see Eq. (17)], which acts to balance the condensate population in these states and strengthen the BA phase (i.e., this effect tends to increase $q_{\mathrm{b}}$).


## V. CONCLUSIONS AND OUTLOOK

In this work we have formulated a self-consistent HF theory to characterize the phase diagram of a spin-1 Bose gas at finite temperature. Numerical results, presented over a wide parameter regime, show that certain phase boundaries change appreciably with temperature. We have developed analytical results that accurately describe these shifts in phase boundaries as a function of the interaction parameters and the properties of the noncondensate.

Our treatment includes spin coherence for the noncondensate component of the system, which naturally develops via coherent collisions with the condensate. Our calculations show that the noncondensate spin coherence is crucial to stabilizing the AFM and BA phases, in which the spin rotational symmetry is spontaneously broken. Indeed, neglect of spin coherence in the thermal cloud leads to significant shifts in the locations of the phase boundaries from the full HF calculations.

The effect of the thermal fluctuations on the condensate order is a key prediction that could be explored in experiments. Early measurements made by Miesner and co-workers [4] mapped out parts of the phase diagram using a $^{23}$Na condensate (with antiferromagnetic interactions). In that work the temperature of the system was estimated to be about 100 nK, sufficiently hot that thermal effects should be relevant; however, the authors measured the P-AFM phase boundary which we predict to be temperature insensitive [see Fig. 2(a)]. Aided by improvements in techniques for measuring spinor gas properties (e.g., see Refs. [7,27]), it should be feasible to precisely determine the finite-temperature phase diagram in experiments and compare to our predictions.

It would also be interesting to experimentally investigate the role of the noncondensate spin coherence. Our results show that a large change in the phase boundary occurs when the noncondensate coherence is removed (see Figs. 3 and 5). Given the large difference in the decoherence times for the condensate and noncondensate spin coherence [27], it may be possible to use external fields to reduce (or remove) the spin coherence of the noncondensate, yet leave that of the condensate intact. In the vicinity of the phase boundary this could allow the condensate to exist in a metastable state which would transition to a new phase as the noncondensate spin coherence is eventually reestablished.

On the theoretical front many challenges and opportunities exist for extending our understanding of spinor gases beyond the HF approximation. A natural extension is to develop a quasiparticle-based mean-field theory such as the HF-Bogoliubov-Popov formalism [12,16]. In Ref. [16] we applied this theory to compute the BA-P phase boundary as a function of temperature for $p=0$ and the parameters of $^{87}$Rb. The predictions of Ref. [16] are quantitatively similar to the HF results we present here, with the notable exception of the $T \to 0$ limit where we have found that the quantum depletion (excluded in the HF theory) acts to increase $q_{\text{b}}$ to a value greater than $2|c_{1}|n^{\text{c}}$. An alternative direction is the use of classical field techniques [28], which, within their regime of validity, will provide a dynamical description of the finite-temperature spinor system, and have already seen some initial applications to quasi-two-dimensional spinor gases [29]. Another avenue for consideration is the inclusion of dipole-dipole interactions between atoms into the finite-temperature description (e.g., see [30]). These long-range interactions have been predicted to give rise to interesting new features in the ground-state phase diagram [31], and are thought to be important for explaining some of the observations in the $^{87}$Rb spinor gas [8].

## ACKNOWLEDGMENTS

Y.K. and N.T.P. were supported by KAKENHI (Grants No. 22340114, No. 22740265, and No. 22103005), a Global COE Program "Physical Sciences Frontier," and the Photon Frontier Network Program from MEXT of Japan, and by JSPS and FRST under the Japan-New Zealand Research Cooperative Program. P.B.B. was supported by Marsden Contract No. UOO0924 and FRST IIOF Contract No. UOOX0915.

## APPENDIX A: HARTREE-FOCK THEORY AND THERMODYNAMIC PARAMETERS

The HF theory can be derived by assuming that the many-body density matrix is given by

$$
D_{0}=\frac{1}{Z_{0}} e^{-\beta \hat{K}_{\mathrm{HF}}}, \tag{A1}
$$

where $Z_{0}=\operatorname{Tr}\{e^{-\beta \hat{K}_{\mathrm{HF}}}\}$ and $\hat{K}_{\mathrm{HF}}=\int d\mathbf{r}\sum_{i,j}\hat{\delta}_{i}^{\dagger}A_{ij}\hat{\delta}_{j}$ is the assumed single-particle form for the HF Hamiltonian. The variational principle applied to determine $\hat{K}_{\mathrm{HF}}$ (or, equivalently, $A_{ij}$) is that $D_{0}$ makes the thermodynamic potential $\Phi(D)$ stationary, where

$$
\Phi(D)=\operatorname{Tr}\{k_{\mathrm{B}}T D\ln D+D\hat{\mathcal{H}}-\mu D\hat{N}\}, \tag{A2}
$$

with $\hat{N}$ being the number operator. This procedure gives the form of the Gross-Pitaevskii and HF equations used in this paper [i.e., Eqs. (5), (11), and (12)].

In terms of the self-consistent solution of the HF equations thermodynamic parameters can be evaluated. The HF energy is given by

$$
\begin{aligned}
E_{\mathrm{HF}}&=\operatorname{Tr}\{D_{0}\hat{\mathcal{H}}\} \tag{A3} \\
&=\int d\mathbf{r}\Bigg\{\sum_{j}\Bigg[\phi_{j}^{*}(h_{0})_{jj}\phi_{j}+\sum_{\lambda}\bar{n}_{\lambda}u_{j}^{\lambda *}(h_{0})_{jj}u_{j}^{\lambda}\Bigg] \\
&\quad+\frac{c_{0}}{2}\bigg[(n^{\text{c}}+n^{\text{nc}})^{2}+\sum_{ij}n_{ij}^{\text{nc}}(2n_{ji}^{\text{c}}+n_{ji}^{\text{nc}})\bigg] \\
&\quad+\sum_{\alpha}\frac{c_{1}}{2}\bigg[\bigg(F_{\alpha}^{\text{c}}+F_{\alpha}^{\text{nc}}\bigg)^{2} \\
&\quad+\sum_{ijkl}(f_{\alpha})_{ij}(f_{\alpha})_{kl}n_{kj}^{\text{nc}}(2n_{il}^{\text{c}}+n_{il}^{\text{nc}})\bigg]\Bigg\}, \tag{A4}
\end{aligned}
$$

and by evaluating Eq. (A2), using the self-consistently determined HF density matrix, the free energy of the HF solution

(Φ_HF) can be determined. Equivalently, it can be evaluated as
$$
\Phi_{\mathrm{HF}}=E_{\mathrm{HF}}-\mu N-T S_{\mathrm{HF}},\qquad(\mathrm{A}5)
$$
where the entropy is
$$
S_{\mathrm{HF}}=-k_{B} \sum_{\lambda}\left[\bar{n}_{\lambda} \ln \bar{n}_{\lambda}-\left(1+\bar{n}_{\lambda}\right) \ln \left(1+\bar{n}_{\lambda}\right)\right].\qquad(\mathrm{A}6)
$$

## APPENDIX B: DERIVATION OF EQ. (35)

In this and the following appendixes, we use boldface quantities to represent matrix quantities for notational efficiency, for example, $n_{ij}^c \to \boldsymbol{n}^c$, $n_{ij}^{\text{nc}} \to \boldsymbol{n}^{\text{nc}}$, and $\delta_{ij} \to \mathbf{1}$. We also introduce $d^c \equiv n_{1,-1}^c = n_{-1,1}^c$, $d^{\text{nc}} \equiv n_{-1,1}^{\text{nc}}$, $n_i^c \equiv n_{ii}^c$, and $n_i^{\text{nc}} \equiv n_{ii}^{\text{nc}}$.

We start from Eq. (29). From the condition that Eq. (29) has a nontrivial solution, $\tilde{\mu}$ is obtained as
$$
\tilde{\mu}= \pm \sqrt{\tilde{p}^{2}+C_{-}^{2}\left|d^{\mathrm{nc}}\right|^{2}}.\qquad(\mathrm{B}1)
$$

Choosing the lower chemical potential, the order parameter is given by
$$
\phi_{1}=\sqrt{\frac{n^{\mathrm{c}}}{2}\left(1+\frac{\tilde{p}}{\lambda}\right)},\qquad(\mathrm{B}2a)
$$

$$
\phi_{-1}=-e^{-i \theta} \sqrt{\frac{n^{\mathrm{c}}}{2}\left(1-\frac{\tilde{p}}{\lambda}\right)},\qquad(\mathrm{B}2b)
$$
where
$$
\lambda=\sqrt{\tilde{p}^{2}+C_{-}^{2}\left|d^{\mathrm{nc}}\right|^{2}},\qquad(\mathrm{B}3)
$$

$$
\theta=\arg \left(d^{\mathrm{nc}}\right).\qquad(\mathrm{B}4)
$$

Since we have chosen $\phi_{\pm 1}$ to be positive real numbers, $d^{\text{nc}}$ is a negative number ($\theta=\pi$). From Eq. (B2), we obtain the relation between the condensate spin density and $d^{\text{nc}}$:
$$
\frac{d^{c}}{F_{z}^{c}}=\frac{\phi_{1} \phi_{-1}}{\left|\phi_{1}\right|^{2}-\left|\phi_{-1}\right|^{2}}=-\frac{C_{-} d^{\mathrm{nc}}}{2 \tilde{p}}.\qquad(\mathrm{B}5)
$$

Next, by substituting Eqs. (27) and (28) into Eq. (20), we obtain
$$
\mathcal{A}=\left(-\mu+c_{0} n\right) \mathbf{1}+\left(\begin{array}{ccc}
-p+c_{1} F_{z}+q & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & p-c_{1} F_{z}+q
\end{array}\right)+\left(\begin{array}{ccc}
C_{+} n_{1}+c_{1} n_{0} & 0 & C_{-} d \\
0 & c_{0} n_{0}+c_{1}\left(n_{1}+n_{-1}\right) & 0 \\
C_{-} d & 0 & C_{+} n_{-1}+c_{1} n_{0}
\end{array}\right),
$$
(B6)

where $n_i = n_i^c + n_i^{\text{nc}}$, $F_z = F_z^c + F_z^{\text{nc}}$, and $d = d^c + d^{\text{nc}}$. The eigenvalue for the $i=0$ component is immediately obtained as
$$
\kappa_{0}=c_{0} n+c_{0} n_{0}+c_{1}\left(n_{1}+n_{-1}\right)-\mu.\qquad(\mathrm{B}7)
$$

For the $i=\pm 1$ components, we need to diagonalize the following $2 \times 2$ matrix:
$$
\begin{aligned}
\tilde{\mathcal{A}}= & {\left[-\tilde{\mu}+c_{1} n_{0}^{\mathrm{c}}+\frac{C_{+}}{2}\left(n_{1}^{\mathrm{c}}+n_{-1}^{\mathrm{c}}\right)\right] \mathbf{1} } \\
& +\left(\begin{array}{cc}
-\tilde{p}+C_{+} F_{z}^{\mathrm{c}} / 2 & C_{-} d \\
C_{-} d & \tilde{p}-C_{+} F_{z}^{\mathrm{c}} / 2
\end{array}\right).
\end{aligned}\qquad(\mathrm{B}8)
$$

This matrix is almost the same as Eq. (29), and the eigenvalues and eigenvectors are given by
$$
\kappa_{ \pm}=-\tilde{\mu}+c_{1} n_{0}^{\mathrm{c}}+\frac{C_{+}}{2}\left(n_{1}^{\mathrm{c}}+n_{-1}^{\mathrm{c}}\right) \pm \lambda^{\prime},\qquad(\mathrm{B}9)
$$

$$
\left(\begin{array}{c}
\bar{u}_{1}^{( \pm)} \\
\bar{u}_{-1}^{( \pm)}
\end{array}\right)=\frac{1}{\sqrt{2 \lambda^{\prime}}}\left(\begin{array}{c}
\sqrt{\lambda^{\prime} \mp\left(\tilde{p}-C_{+} F_{z}^{\mathrm{c}} / 2\right)} \\
\pm \operatorname{sgn}(d) \sqrt{\lambda^{\prime} \pm\left(\tilde{p}-C_{+} F_{z}^{\mathrm{c}} / 2\right)}
\end{array}\right),\quad(\mathrm{B}10)
$$
where
$$
\lambda^{\prime} \equiv \sqrt{\left(\tilde{p}-C_{+} F_{z}^{\mathrm{c}} / 2\right)^{2}+C_{-}^{2} d^{2}}.\qquad(\mathrm{B}11)
$$

Since $n_{\pm 1}^{\text{nc}}$ and $d^{\text{nc}}$ are self-consistently determined so as to satisfy Eq. (22), we obtain the relation between $F_z^{\text{nc}}$
and $d^{\text{nc}}$:
$$
\begin{aligned}
\frac{d^{\mathrm{nc}}}{F_{z}^{\mathrm{nc}}} & =\frac{\sum_{v= \pm} \bar{u}_{-1}^{(v) *} \bar{u}_{1}^{(v)} \mathrm{Li}_{3 / 2}\left(e^{-\beta \kappa_{v}}\right)}{\sum_{v= \pm}\left[\bar{u}_{1}^{(v) *} \bar{u}_{1}^{(v)}-\bar{u}_{-1}^{(v) *} \bar{u}_{-1}^{(v)}\right] \mathrm{Li}_{3 / 2}\left(e^{-\beta \kappa_{v}}\right)} \\
& =-\frac{C_{-} d}{2 \tilde{p}-C_{+} F_{z}^{\mathrm{c}}}.
\end{aligned}\qquad(\mathrm{B}12)
$$

Equations (B5) and (B12) are rewritten as a linear equation of $d^c$ and $d^{\text{nc}}$:
$$
\left(\begin{array}{cc}
2 \tilde{p} & C_{-} F_{z}^{\mathrm{c}} \\
C_{-} F_{z}^{\mathrm{nc}} & 2 \tilde{p}-C_{+} F_{z}^{\mathrm{c}}+C_{-} F_{z}^{\mathrm{nc}}
\end{array}\right)\left(\begin{array}{l}
d^{c} \\
d^{\mathrm{nc}}
\end{array}\right)=0.\qquad(\mathrm{B}13)
$$

In order for $d^c$ and $d^{\text{nc}}$ to have a nontrivial solution, $\tilde{p}$, $F_z^c$, and $F_z^{\text{nc}}$ have to satisfy
$$
2 \tilde{p}\left(2 \tilde{p}-C_{+} F_{z}^{\mathrm{c}}+C_{-} F_{z}^{\mathrm{nc}}\right)-C_{-}^{2} F_{z}^{\mathrm{c}} F_{z}^{\mathrm{nc}}=0.\qquad(\mathrm{B}14)
$$

Solving Eq. (B14) in terms of $p$, we obtain Eq. (34), where we have chosen the sign in front of the square-root term so that Eq. (34) continuously goes to the solution at $T=0$.

## APPENDIX C: DERIVATION OF EQS. (38) and (40)

In the BA phase at $p=0$ the condensate is magnetized in the transverse direction. Without loss of generality, we can choose the direction of the magnetization in the $x$ direction, i.e., the magnetic field is applied in the $z$ direction and

spontaneous magnetization arises in the $x$ direction. We then move to the frame of reference which is rotated around the $y$ axis by $\pi/2$. In this frame of reference, the magnetic field is applied in the $-x$ direction and the magnetization arises in the $z$ direction. In this appendix all results are given in this frame of reference unless specified otherwise. The magnetic sublevel $i$ in the rotated frame corresponds to the eigenvalue of $f_x$ in the laboratory frame.

### 1. Full HF calculation
The matrices $\mathcal{L}$ and $\mathcal{A}$ in the rotated frame are given by
$$
\begin{aligned}
\mathcal{L}= & q f_{x}^{2}+c_{0}\left[n \mathbf{1}+\left(\boldsymbol{n}^{\mathrm{nc}}\right)^{\mathrm{T}}\right] \\
& +c_{1} \sum_{\alpha}\left[F_{\alpha} f_{\alpha}+f_{\alpha}\left(\boldsymbol{n}^{\mathrm{nc}}\right)^{\mathrm{T}} f_{\alpha}\right],
\end{aligned} \qquad (C1)
$$

$$
\mathcal{A}=\mathcal{L}-\mu \mathbf{1}+c_{0}\left(\boldsymbol{n}^{\mathrm{nc}}\right)^{\mathrm{T}}+c_{1} \sum_{\alpha} f_{\alpha}\left(\boldsymbol{n}^{\mathrm{c}}\right)^{\mathrm{T}} f_{\alpha}. \qquad (C2)
$$

Since the matrix elements of $f_{x}^{2}$ are given by
$$
f_{x}^{2}=\left(\begin{array}{ccc}
1 / 2 & 0 & 1 / 2 \\
0 & 1 & 0 \\
1 / 2 & 0 & 1 / 2
\end{array}\right), \qquad (C3)
$$
we can assume that $i=0$ and $i=\pm 1$ components are decoupled:
$$
\boldsymbol{n}^{\mathrm{c}}=\left(\begin{array}{ccc}
n_{1}^{\mathrm{c}} & 0 & d^{\mathrm{c}} \\
0 & 0 & 0 \\
d^{\mathrm{c}} & 0 & n_{-1}^{\mathrm{c}}
\end{array}\right), \quad \boldsymbol{n}^{\mathrm{nc}}=\left(\begin{array}{ccc}
n_{1}^{\mathrm{nc}} & 0 & \left(d^{\mathrm{nc}}\right)^{*} \\
0 & n_{0}^{\mathrm{nc}} & 0 \\
d^{\mathrm{nc}} & 0 & n_{-1}^{\mathrm{nc}}
\end{array}\right). \quad (\mathrm{C} 4)
$$

The order parameter for the BA phase in the laboratory frame is given by $\sqrt{n^{\mathrm{c}} / 2}(a, \sqrt{2} b, a)^{\mathrm{T}}\left(a, b \in \mathbb{R}, a^{2}+b^{2}=1,0 \leqslant a \leqslant\right.$ $1 / \sqrt{2}$) [1], which is transformed in the rotated frame as $\sqrt{n^{\mathrm{c}} / 2}(a+b, 0, a-b)^{\mathrm{T}}$. It follows that $d^{\mathrm{c}}$ is always negative in the BA phase because $0 \leqslant a \leqslant 1 / \sqrt{2} \leqslant b \leqslant 1$. When the system is in the polar phase $(a=0, b=1)$, we have $d^{\mathrm{c}}=-n^{\mathrm{c}} / 2$.

From Eq. (C1), the $i=\pm 1$ components should satisfy
$$
\left(\begin{array}{cc}
\tilde{p}-\tilde{\mu} & q / 2+C_{-} d^{\mathrm{nc}} \\
q / 2+C_{-}\left(d^{\mathrm{nc}}\right)^{*} & -\tilde{p}-\tilde{\mu}
\end{array}\right)\left(\begin{array}{l}
\phi_{1} \\
\phi_{-1}
\end{array}\right)=0, \quad (\mathrm{C} 5)
$$
where
$$
\tilde{\mu}=\mu-\left(q / 2+c_{0} n+c_{1} n_{0}^{\mathrm{nc}}+C_{+} \frac{n_{1}^{\mathrm{nc}}+n_{-1}^{\mathrm{nc}}}{2}\right), \quad (\mathrm{C} 6)
$$

$$
\tilde{p}=c_{1} F_{z}^{\mathrm{c}}+\frac{c_{0}+3 c_{1}}{2} F_{z}^{\mathrm{nc}}, \qquad (C7)
$$
and $C_{ \pm}$are defined in Eqs. (32). From the condition that Eq. (C5) has a nontrivial solution, $\tilde{\mu}$ is determined as
$$
\tilde{\mu}= \pm \sqrt{\tilde{p}^{2}+\left|\frac{q}{2}+C_{-} d^{\mathrm{nc}}\right|^{2}}. \qquad (C8)
$$

Choosing the lower chemical potential, the order parameter is given by
$$
\phi_{1}=\sqrt{\frac{n^{\mathrm{c}}}{2}\left(1-\frac{\tilde{p}}{\lambda}\right)}, \qquad (C9a)
$$

$$
\phi_{-1}=-e^{-i \theta} \sqrt{\frac{n^{\mathrm{c}}}{2}\left(1+\frac{\tilde{p}}{\lambda}\right)}, \qquad (C9b)
$$
where
$$
\lambda \equiv \sqrt{\tilde{p}^{2}+\left(\frac{q}{2}+C_{-} d^{\mathrm{nc}}\right)^{2}}, \qquad (C10)
$$

$$
\theta \equiv \arg \left(\frac{q}{2}+C_{-} d^{\mathrm{nc}}\right). \qquad (C11)
$$

Since $\phi_{-1}$ is assumed to be a negative real number, $\theta$ has to be zero, that is, $d^{\mathrm{nc}}$ is real and satisfies $q / 2+C_{-} d^{\mathrm{nc}}>0$. From Eq. (C9), we obtain the relation between $F_{z}^{\mathrm{c}}$ and $d^{\mathrm{c}}$:
$$
\frac{d^{\mathrm{c}}}{F_{z}^{\mathrm{c}}}=\frac{q / 2+C_{-} d^{\mathrm{nc}}}{\left(C_{+}-C_{-}\right) F_{z}^{\mathrm{c}}+\left(2 C_{+}-C_{-}\right) F_{z}^{\mathrm{nc}}}. \qquad (C12)
$$

Next, we consider the equation for the noncondensate part. The matrix $\mathcal{A}$ is given by
$$
\mathcal{A}=\left(-\mu+c_{0} n\right) \mathbf{1}+\left(\begin{array}{ccc}
c_{1} F_{z}+q / 2 & 0 & q / 2 \\
0 & q & 0 \\
q / 2 & 0 & -c_{1} F_{z}+q / 2
\end{array}\right)+\left(\begin{array}{ccc}
C_{+} n_{1}+c_{1} n_{0} & 0 & C_{-} d \\
0 & c_{0} n_{0}+c_{1}\left(n_{1}+n_{-1}\right) & 0 \\
C_{-} d & 0 & C_{+} n_{-1}+c_{1} n_{0}
\end{array}\right).
$$
(C13)

For the $i=\pm 1$ components, we need to diagonalize the $2 \times 2$ matrix:
$$
\tilde{\mathcal{A}}=\left(-\tilde{\mu}+c_{1} n_{0}^{\mathrm{c}}+C_{+} \frac{n_{1}^{\mathrm{c}}+n_{-1}^{\mathrm{c}}}{2}\right) \mathbf{1}+\left(\begin{array}{cc}
\tilde{p}+C_{+} F_{z}^{\mathrm{c}} / 2 & q / 2+C_{-} d \\
q / 2+C_{-} d & -\tilde{p}-C_{+} F_{z}^{\mathrm{c}} / 2
\end{array}\right). \qquad (C14)
$$

The eigenvalues and eigenvectors of $\tilde{\mathcal{A}}$ are given by
$$
\kappa_{ \pm}=-\tilde{\mu}+c_{1} n_{0}^{\mathrm{c}}+C_{+} \frac{n_{1}^{\mathrm{c}}+n_{-1}^{\mathrm{c}}}{2} \pm \lambda^{\prime}, \qquad (C15)
$$

$$
\left(\begin{array}{c}
\tilde{u}_{1}^{( \pm)} \\
\tilde{u}_{-1}^{( \pm)}
\end{array}\right)=\frac{1}{\sqrt{2 \lambda^{\prime}}}\left(\begin{array}{c}
\sqrt{\lambda^{\prime} \pm\left(\tilde{p}+C_{+} F_{z}^{\mathrm{c}} / 2\right)} \\
\pm e^{-i \theta^{\prime}} \sqrt{\lambda^{\prime} \mp\left(\tilde{p}+C_{+} F_{z}^{\mathrm{c}} / 2\right)}
\end{array}\right), \quad (\mathrm{C} 16)
$$
where
$$
\lambda^{\prime} \equiv \sqrt{\left(\tilde{p}+C_{+} \frac{F_{z}^{\mathrm{c}}}{2}\right)^{2}+\left(\frac{q}{2}+C_{-} d\right)^{2}}, \qquad (C17)
$$

$$
\theta^{\prime} \equiv \arg \left(\frac{q}{2}+C_{-} d\right). \qquad (C18)
$$

Since $n_{\pm 1}^{\text{nc}}$ and $d^{\text{nc}}$ are self-consistently determined so as to satisfy Eq. (C22), we obtain the relation between $F_{z}^{\text{nc}}$ and $d^{\text{nc}}$ as
$$
\begin{aligned}
\frac{d^{\text{nc}}}{F_{z}^{\text{nc}}} & =\frac{\sum_{v= \pm} \bar{u}_{-1}^{(v) *} \bar{u}_{1}^{(v)} \operatorname{Li}_{3 / 2}\left(e^{-\beta \kappa_{v}}\right)}{\sum_{v= \pm}\left[\bar{u}_{1}^{(v) *} \bar{u}_{1}^{(v)}-\bar{u}_{-1}^{(v) *} \bar{u}_{-1}^{(v)}\right] \operatorname{Li}_{3 / 2}\left(e^{-\beta \kappa_{v}}\right)} \\
& =\frac{q / 2-C_{-} d}{\left(2 C_{+}-C_{-}\right) F_{z}}. \quad \text { (C19) }
\end{aligned}
$$

Equations (C12) and (C19) are rewritten as a linear equation for $F_{z}^{\mathrm{c}}$ and $F_{z}^{\mathrm{nc}}$ :
$$
\begin{aligned}
& \left(\begin{array}{cc}
2 c_{1} d^{c}-C_{-} d^{\mathrm{nc}}-q / 2 & \left(2 C_{+}-C_{-}\right) d^{\mathrm{c}} \\
-\left(2 C_{+}-C_{-}\right) d^{\mathrm{nc}} & C_{-} d^{c}-4 c_{1} d^{\mathrm{nc}}+q / 2
\end{array}\right) \\
& \quad \times\left(\begin{array}{c}
F_{z}^{\mathrm{c}} \\
F_{z}^{\mathrm{nc}}
\end{array}\right)=0. \quad \text { (C20) }
\end{aligned}
$$

From the condition that $F_{z}^{\mathrm{c}}$ and $F_{z}^{\mathrm{nc}}$ have a non-trivial solution, we obtain
$$
\begin{aligned}
q & \cong 2\left(C_{+}-C_{-}\right) d^{\mathrm{c}}\left(1+\frac{4 C_{+}-C_{-}}{C_{+}} \frac{d^{\mathrm{nc}}}{d^{\mathrm{c}}}\right) \quad(\mathrm{C} 21) \\
& =4 c_{1} d^{\mathrm{c}}\left(1+\frac{3 c_{0}+5 c_{1}}{c_{0}+c_{1}} \frac{d^{\mathrm{nc}}}{d^{\mathrm{c}}}\right), \quad \text { (C22) }
\end{aligned}
$$
where we have expanded $q$ to first order in the parameter $d^{\text{nc}} / d^{\text{c}}$. Since $d^{\mathrm{c}}=-n^{\mathrm{c}} / 2$ at the BA-P boundary, we obtain the boundary $q_{\mathrm{b}}$ as Eq. (38).

In the laboratory frame, $\boldsymbol{n}^{\text{nc}}$ is related to that in the rotated frame as
$$
\boldsymbol{n}^{\mathrm{nc}(\mathrm{lab})}=e^{-i f_{y} \pi / 2} \boldsymbol{n}^{\mathrm{nc}} e^{i f_{y} \pi / 2}, \quad (\mathrm{C} 23)
$$
from which $d^{\text{nc}}$ is rewritten in terms of $\boldsymbol{n}^{\text{nc}}$ in the laboratory frame as
$$
d^{\mathrm{nc}} \equiv n_{-1,1}^{\mathrm{nc}}=\frac{1}{2}\left(n_{1,1}^{\mathrm{nc}(\mathrm{lab})}+n_{-1,1}^{\mathrm{nc}(\mathrm{lab})}-n_{0,0}^{\mathrm{nc}(\mathrm{lab})}\right). \quad (\mathrm{C} 24)
$$

### 2. Neglecting the off-diagonal part

When we neglect the off-diagonal part of $\boldsymbol{n}^{\text{nc}}$ in the laboratory frame,
$$
\boldsymbol{n}^{\mathrm{nc}(\mathrm{lab})}=\left(\begin{array}{ccc}
n_{1}^{\mathrm{nc}(\mathrm{lab})} & 0 & 0 \\
0 & n_{0}^{\mathrm{nc}(\mathrm{lab})} & 0 \\
0 & 0 & n_{-1}^{\mathrm{nc}(\mathrm{lab})}
\end{array}\right), \quad (\mathrm{C} 25)
$$
the noncondensed component has no transverse magnetization, which means $F_{z}^{\text{nc}}=0$, i.e., $n_{1}^{\text{nc}}=n_{-1}^{\text{nc}}$, in the rotated frame. Hence, the calculation for the condensate part is the same as that for the full HF calculation if we impose $n_{1}^{\text{nc}}=n_{-1}^{\text{nc}}$. Equation (C12) then reduces to
$$
\frac{d^{\mathrm{c}}}{F_{z}^{\mathrm{c}}}=\frac{q / 2-C_{-} d^{\mathrm{nc}}}{\left(C_{+}-C_{-}\right) F_{z}^{\mathrm{c}}}, \quad (\mathrm{C} 26)
$$
from which we obtain Eq. (40).

[1] M. Ueda and Y. Kawaguchi, e-print arXiv:1001.2072.

[2] T.-L. Ho, Phys. Rev. Lett. 81, 742 (1998).

[3] T. Ohmi and K. Machida, J. Phys. Soc. Jpn 67, 1822 (1998).

[4] J. Stenger, S. Inouye, D. M. Stamper-Kurn, H.-J. Miesner, A. P. Chikkatur, and W. Ketterle, Nature (London) 396, 345 (1999).

[5] H.-J. Miesner, D. M. Stamper-Kurn, J. Stenger, S. Inouye, A. P. Chikkatur, and W. Ketterle, Phys. Rev. Lett. 82, 2228 (1999).

[6] M.-S. Chang, C. D. Hamley, M. D. Barrett, J. A. Sauer, K. M. Fortier, W. Zhang, L. You, and M. S. Chapman, Phys. Rev. Lett. 92, 140403 (2004); M.-S. Chang, Q. Qin, W. Zhang, L. You, and M. S. Chapman, Nat. Phys. 99, 111 (2005).

[7] A. T. Black, E. Gomez, L. D. Turner, S. Jung, and P. D. Lett, Phys. Rev. Lett. 99, 070403 (2007).

[8] M. Vengalattore, S. R. Leslie, J. Guzman, and D. M. Stamper-Kurn, Phys. Rev. Lett. 100, 170403 (2008); M. Vengalattore, J. Guzman, S. R. Leslie, F. Serwane, and D. M. Stamper-Kurn, Phys. Rev. A 81, 053612 (2010).

[9] Y. Liu, E. Gomez, S. E. Maxwell, L. D. Turner, E. Tiesinga, and P. D. Lett, Phys. Rev. Lett. 102, 225301 (2009).

[10] L. E. Sadler, J. M. Higbie, S. R. Leslie, M. Vengalattore, and D. M. Stamper-Kurn, Nature (London) 443, 312 (2006).

[11] Y. Liu, S. Jung, S. E. Maxwell, L. D. Turner, E. Tiesinga, and P. D. Lett, Phys. Rev. Lett. 102, 125301 (2009).

[12] T. Ioshima, T. Ohmi, and K. Machida, J. Phys. Soc. Jpn. 69, 3864 (2000).

[13] W.-J. Huang, S.-C. Gou, and Y.-C. Tsai, Phys. Rev. A 65, 063610 (2002).

[14] W. Zhang, S. Yi, and L. You, Phys. Rev. A 70, 043611 (2004).

[15] K. Kis-Szabó, P. Szépfalusy, and G. Szirmai, Phys. Lett. A 364, 362 (2007).

[16] N. T. Phuc, Y. Kawaguchi, and M. Ueda, Phys. Rev. A 84, 043645 (2011).

[17] S. S. Natu and E. J. Mueller, Phys. Rev. A 84, 053625 (2011).

[18] S. Mukerjee, C. Xu, and J. E. Moore, Phys. Rev. Lett. 97, 120406 (2006).

[19] A. J. A. James and A. Lamacraft, Phys. Rev. Lett. 106, 140402 (2011).

[20] F. Gerbier, J. H. Thywissen, S. Richard, M. Hugbart, P. Bouyer, and A. Aspect, Phys. Rev. Lett. 92, 030405 (2004).

[21] F. Gerbier, J. H. Thywissen, S. Richard, M. Hugbart, P. Bouyer, and A. Aspect, Phys. Rev. A 70, 013607 (2004).

[22] N. Tammuz, R. P. Smith, R. L. D. Campbell, S. Beattie, S. Moulder, J. Dalibard, and Z. Hadzibabic, Phys. Rev. Lett. 106, 230401 (2011).

[23] F. Gerbier, A. Widera, S. Fölling, O. Mandel, and I. Bloch, Phys. Rev. A 73, 041602 (2006).

[24] J. Blaizot and G. Ripka, *Quantum Theory of Finite Systems*, 1st ed. (MIT Press, Cambridge, MA, 1986).

[25] T. Bergeman, Phys. Rev. A 55, 3658 (1997).

[26] J. M. McGuirk, D. M. Harber, H. J. Lewandowski, and E. A. Cornell, Phys. Rev. Lett. 91, 150402 (2003); H. J. Lewandowski, J. M. McGuirk, D. M. Harber, and E. A. Cornell, ibid. 91, 240404 (2003).

[27] J. M. Higbie, L. E. Sadler, S. Inouye, A. P. Chikkatur, S. R. Leslie, K. L. Moore, V. Savalli, and D. M. Stamper-Kurn, Phys. Rev. Lett. 95, 050401 (2005).

[28] P. B. Blakie, A. S. Bradley, M. J. Davis, R. J. Ballagh, and C. W. Gardiner, *Adv. Phys.* **57**, 363 (2008).

[29] V. Pietilä, T. P. Simula, and M. Möttönen, *Phys. Rev. A* **81**, 033616 (2010); S.-W. Su, C.-H. Hsueh, I.-K. Liu, T.-L. Horng, Y.-C. Tsai, S.-C. Gou, and W. M. Liu, *ibid*. **84**, 023601 (2011).

[30] S. Ronen and J. L. Bohn, *Phys. Rev. A* **76**, 043607 (2007); R. N. Bisset, D. Baillie, and P. B. Blakie, *ibid*. **83**, 061602 (2011).

[31] Y. Kawaguchi, H. Saito, and M. Ueda, *Phys. Rev. Lett.* **97**, 130404 (2006).