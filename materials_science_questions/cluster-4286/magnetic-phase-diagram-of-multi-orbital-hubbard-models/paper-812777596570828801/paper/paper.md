PHYSICAL REVIEW B 99, 205106 (2019)

# Coexistent spin-triplet superconducting and ferromagnetic phases induced by Hund's rule coupling and electronic correlations: Effect of the applied magnetic field

M. Fidrysiak, $^{1, *}$ D. Goc-Jagło, $^{1, \dagger}$ E. Kądzielawa-Major, $^{1, \ddagger}$ P. Kubiczek, $^{2, \S}$ and J. Spałek $^{1, \|}$

$^{1}$ Marian Smoluchowski Institute of Physics, Jagiellonian University, ul. Łojasiewicza 11, 30-348 Kraków, Poland
$^{2}$ I. Institut für Theoretische Physik, Universität Hamburg, Jungiusstraße 9, D-20355 Hamburg, Germany

![](./images/812777596570828801_1.jpg)
(Received 21 February 2019; published 6 May 2019)

The recently proposed local-correlation-driven pairing mechanism, describing ferromagnetic phases (FM1 and FM2) coexisting with spin-triplet superconductivity (SC) within a single orbitally degenerate Anderson lattice model, is extended to the situation with an applied Zeeman field. The model provides and rationalizes in a semiquantitative manner the principal features of the phase diagram observed for $UGe_2$ in the field absence [cf., Phys. Rev. B 97, 224519 (2018)]. As spin-dependent effects play a crucial role for both the ferromagnetic and SC states, the role of the Zeeman field is to single out different stable spin-triplet SC phases. This analysis should thus be helpful in testing the proposed real-space pairing mechanism, which may be regarded as complementary to spin-fluctuation theory suitable for $^3$He. Specifically, we demonstrate that the presence of the two distinct phases, FM1 and FM2, and the associated field-driven metamagnetic transition between them, induces a respective metasuperconducting phase transformation. At the end, we discuss briefly how the spin fluctuations might be incorporated as a next step in the renormalized quasiparticle picture considered herein.

DOI: 10.1103/PhysRevB.99.205106

## I. INTRODUCTION

The discovery of spin-triplet superconductivity (SC) inside ferromagnetic (FM) phases of uranium compounds $UGe_2$ [1–4], URhGe [5], UCoGe [6], and UIr [7] is directly related to the question of a pairing mechanism and the order-parameter symmetry under such circumstances. Due to substantial correlations in the $f$-electron sector, the situation here differs from that for superfluid $^3$He, where a normal (paramagnetic) Landau-Fermi liquid is unstable against the formation of a pure spin-triplet paired state induced by quantum spin fluctuations below the (FM) Stoner instability [8–10]. The uranium compounds may be regarded as those among the first solid-state systems with clear spin-triplet pairing, as the strong effective molecular field acting on spin degrees of freedom in the FM phase, at least for $UGe_2$, rules out any spin-singlet SC. Therefore, it is important to see if different phases $(A, A_1, A_2$, and $B)$ may still appear in an applied magnetic field, in direct correspondence with those observed in $^3$He. Yet, the SC states in the present situation are intertwined with two FM states, FM1 and FM2 [11], so we would like to single out the different coexisting phases. In brief, the pairing mechanism and order-parameter symmetry for uranium superconductors have yet to be determined in joint theoretical and experimental efforts. Here we explicitly identify the possible SC states within the FM and paramagnetic (PM) phases, and we estimate their gap relative magnitudes.

Recently, we have proposed that pairing in $UGe_2$ emerges due to the combined effect of FM exchange interaction (Hund's-rule coupling) combined with interelectronic correlations [12]. Reference [12] is regarded as Part I of our analysis of $UGe_2$ properties (hereinafter to as I). The spin-paired $A_1$ state proved to be the dominant phase there with the pair spins opposite to those of average spin polarization, a natural feature appearing in the half-metallic phase [13]. Remarkably, within the approach, the $A_1$-type SC emerges in a discontinuous manner at the metamagnetic transition between the two distinct FM phases (FM2 $\to$ FM1), as is evidenced in the recent specific-heat measurements [14]. Finally, SC practically disappears at the boundary of the PM phase, which requires invoking a strongly anisotropic and pressure-dependent form of spin-fluctuation spectrum to explain the character of the SC state in terms of pairing by long-wavelength FM excitations [15]. Within our combined correlation- and exchange-driven pairing scheme, all the above features are explained in a unified manner, as both the ferromagnetism and pairing are directly connected and driven by the real-space correlations of the same origin. The changes of applied pressure are theoretically mimicked by us by varying the hybridization magnitude between the almost localized U $5f$ electrons and conduction bands, and regarded as the primary factor inducing the observed evolution [16–19].

Studies of the ground-state properties as a function of pressure alone are, however, insufficient to confirm fully the relevance of real-space correlation-driven pairing. This is due to the availability of extensive experimental data covering SC and magnetic properties of $UGe_2$ in the three-dimensional parameter space spanned by pressure, temperature, and applied magnetic field [11]. In particular, any proposed pairing mechanism should be minimally tested against the sequence of magnetic-field-induced simultaneous metamagnetic and

$^*$maciej.fidrysiak@uj.edu.pl
$^\dagger$danuta.goc-jaglo@uj.edu.pl
$^\ddagger$ewa.kadzielawa@doctoral.uj.edu.pl
$^\S$patryk.kubiczek@physik.uni-hamburg.de
$^\|$jozef.spalek@uj.edu.pl

2469-9950/2019/99(20)/205106(13)
205106-1
©2019 American Physical Society

induced metasuperconducting transitions along the first-order line on the field-pressure plane. In this paper, we carry out this program and investigate possible spatially homogeneous phases in the Zeeman magnetic field. The resultant phase diagram agrees well with available data close to the pressure-induced magnetic transitions. We also provide a model band structure in the correlated state, as well as other characteristics, such as the $f$-level filling. The latter parameter points toward the almost localized nature of two out of three $\mathrm{U}^{3+}$ $5f$ electrons and one itinerant, originating from the orbital-selective $5f^{3} \rightarrow 5f^{2}$ ($\mathrm{U}^{3+} \rightarrow \mathrm{U}^{4+}$) valence transition suggested by us. The $f$-state filling is close to an integer, hence the term almost localized f electrons. As a reference point, we provide the ground-state results within a more general variational scheme [20] in zero applied magnetic field and discuss its subsequent simplification (cf. Appendix A). At the end, we outline possible extensions of our approach to incorporate both the full Gutzwiller-type projection (cf. Appendix A) and inclusion of the long-wavelength quantum spin fluctuations (cf. Appendix B).

## II. MODEL AND METHOD
We start from the four-orbital degenerate Anderson lattice model, formulated in the real-space language, which takes the form
$$
\begin{aligned}
\mathcal{H}-\mu \hat{N}_{e}= & \sum_{i j l \sigma} t_{i j} \hat{c}_{i \sigma}^{(l) \dagger} \hat{c}_{j \sigma}^{(l)}+V \sum_{i l \sigma}\left(\hat{f}_{i \sigma}^{(l) \dagger} \hat{c}_{i \sigma}^{(l)}+\text { H.c. }\right) \\
& +\epsilon^{f} \sum_{i l} \hat{n}_{i}^{f(l)}+U \sum_{i l} \hat{n}_{i \uparrow}^{f(l)} \hat{n}_{i \downarrow}^{f(l)} \\
& +U^{\prime} \sum_{i} \hat{n}_{i}^{f(1)} \hat{n}_{i}^{f(2)} \\
& -2 J \sum_{i}\left(\hat{\mathbf{S}}_{i}^{f(1)} \cdot \hat{\mathbf{S}}_{i}^{f(2)}+\frac{1}{4} \hat{n}_{i}^{f(1)} \hat{n}_{i}^{f(2)}\right)-\mu \hat{N}_{e}, \\
& (1)
\end{aligned}
$$
where $\mu$ is the chemical potential for the $N_{e}$-electron $N$-site system, and $\hat{f}_{i \sigma}^{(l) \dagger}\left(\hat{f}_{i \sigma}^{(l)}\right)$ is the creation (annihilation) operator of the $f$ electron on an orbital with $l=1,2$ on site $i$ and spin $\sigma=\uparrow, \downarrow$, hybridized with two species of conduction electrons characterized by the corresponding operators $\hat{c}_{i \sigma}^{(l) \dagger}$ and $\hat{c}_{i \sigma}^{(l)}$. Additionally, $\hat{n}_{i \sigma}^{f(l)} \equiv \hat{f}_{i \sigma}^{(l) \dagger} \hat{f}_{i \sigma}^{(l)}$ is the particle number operator for $f$ electrons in the original local state $|i l \sigma\rangle$, and $\hat{\mathbf{S}}_{i}^{f(l)} \equiv\left(\hat{S}_{i}^{f(l)+}, \hat{S}_{i}^{f(l)-}, \hat{S}_{i}^{f(l) z}\right)$ denotes the spin operator of the $f$ electron on orbital $|i l\rangle$. In this minimal model, the first term represents $c$-electron hopping, the second an intra-atomic hybridization between the subsystems of $f$ and $c$ states, and the third is the starting bare atomic $f$-level energy relative to the center of the conduction band. The next two terms express, respectively, the intraorbital and interorbital Coulomb interactions (both of intra-atomic nature), whereas the third represents ferromagnetic (Hund's-rule) exchange interaction between $f$ electrons. This model has been used by us before to explain the magnetic properties, including classical and quantum criticalities, as well as zero-field SC properties of $\mathrm{UGe}_{2}$ [12,17,19,20]. Here we extend this approach with a detailed analysis of coexisting magnetic and SC properties in an applied Zeeman magnetic field, and we determine the phase boundaries between them. Note that in an applied field, two terms should be added to Eq. (1): $-g_{f} \mu_{0} \mu_{B} H \sum_{i} S_{i}^{z}$ and $-g_{c} \mu_{0} \mu_{B} H \sum_{i} s_{i}^{z}$ for $f$ and $c$ electrons, respectively, where $g_{f}$ and $g_{c}$ are gyromagnetic factors, $\mu_{0}$ denotes material permeability, and $s_{i}^{z}$ is the $z$ th spin component for the $c$ electron. Hereafter, for simplicity, we take $g_{f}=g_{c} \equiv g$ and introduce reduced field $h \equiv g \mu_{0} \mu_{B} H / 2$. Moreover, we include only nearest- and next-nearest-neighbor hoppings $t<0$ and $t^{\prime}=$ $0.25|t|$, respectively, and set $U^{\prime}=U-2 J$. The total electron filling is taken as $n^{\text {tot }}=3.25$. Such a choice yields, at zero field, the sequence of magnetic and SC states that match the experimental phase diagram of $\mathrm{UGe}_{2}$ [12].

The model (1) is solved within the statistically consistent Gutzwiller approximation (SGA) [12,17,19,20], which, at zero temperature, is equivalent to an approximate (see below) minimization of the ground-state-energy functional of the form
$$
E_{G} \equiv \frac{\left\langle\Psi_{G}|\mathcal{H}| \Psi_{G}\right\rangle}{\left\langle\Psi_{G} | \Psi_{G}\right\rangle} \equiv \frac{\left\langle\Psi_{0}\left|\hat{P}_{G} \mathcal{H} \hat{P}_{G}\right| \Psi_{0}\right\rangle}{\left\langle\Psi_{0}\left|\hat{P}_{G}^{2}\right| \Psi_{0}\right\rangle},
\qquad(2)
$$
where the correlated wave function is taken in the form
$$
\left|\Psi_{G}\right\rangle \equiv \hat{P}_{G}\left|\Psi_{0}\right\rangle \equiv \prod_{i \alpha} \hat{P}_{G i \alpha}\left|\Psi_{0}\right\rangle.
\qquad(3)
$$
$\left|\Psi_{0}\right\rangle$ represents an uncorrelated state, and $\hat{P}_{G i \alpha}$ are operators acting locally on orbitals $\alpha \in\left\{f^{(1)}, f^{(2)}, c^{(1)}, c^{(2)}\right\}$ at site $i$, introduced to account for local correlations. We adopt a diagonal correlator form $\hat{P}_{G i \alpha} \equiv \lambda_{0_{i \alpha}}\left|0_{i \alpha}\right\rangle\left\langle 0_{i \alpha}\right|+\lambda_{\uparrow_{i \alpha}}\left|\uparrow_{i \alpha}\right\rangle\left\langle\uparrow_{i \alpha}\right|+$ $\lambda_{\downarrow i \alpha}\left|\downarrow_{i \alpha}\right\rangle\left\langle\downarrow_{i \alpha}\right|+\lambda_{\uparrow \downarrow_{i \alpha}}\left|\uparrow \downarrow_{i \alpha}\right\rangle\left\langle\uparrow \downarrow_{i \alpha}\right|$, where the $\lambda$-coefficients serve as variational weights of local many-particle states. Note that $\hat{P}_{G i \alpha}$ can be generalized to incorporate intraorbital $s$-wave superconducting correlations [21]. In our case, however, dominant pairing takes place between distinct $5 f$ orbitals, thus we retain the diagonal correlator structure. Moreover, we assume that $\hat{P}_{G i \alpha}$ respects lattice translational invariance, and we omit the position index, $i$.

Computation of the expectation values, defined by Eq. (2), is a complex many-body problem and may be carried out for finite systems by variational Monte Carlo methods (see, e.g., [22]) or in thermodynamic limit by suitable diagrammatic expansion [23–25]. Within the latter framework, eliminating Hartree bubbles improves substantially series convergence and is achieved by imposing an additional constraint [23,26] $\hat{P}_{G i \alpha}^{2} \equiv 1+x^{(\alpha)} \hat{d}_{\mathrm{HF}}^{(\alpha)}$, with $\hat{d}_{\mathrm{HF}}^{(\alpha)}=\left(\hat{n}_{i \uparrow}^{(\alpha)}-n_{i \uparrow}^{(\alpha)}\right)\left(\hat{n}_{i \downarrow}^{(\alpha)}-n_{i \downarrow}^{(\alpha)}\right)$, so that only one variational parameter $\left(x^{(\alpha)}\right)$ prevails per orbital. We used the compact notation $n_{i \sigma}^{(\alpha)} \equiv\left\langle\hat{n}_{i \sigma}^{(\alpha)}\right\rangle_{0} \equiv\left\langle\Psi_{0}\left|\hat{n}_{i \sigma}^{(\alpha)}\right| \Psi_{0}\right\rangle$. In the above formulation, already the leading diagrammatic contribution tends to capture essential features of correlated lattice models, and, to reduce computational cost, we discard higher-order terms (the SGA approximation). Moreover, since the correlations are most prominent in the $f$-electron sector, we take $x^{\left(f^{(1)}\right)}=x^{\left(f^{(2)}\right)} \equiv x$ and $x^{\left(c^{(1)}\right)}=x^{\left(c^{(2)}\right)}=0$. In the following, we skip the orbital indices for the $\lambda$-coefficients as they refer now exclusively to two equivalent $f$ orbitals. For a more complete discussion of the methodological aspects, see Appendix A.

One feature of the approach should be underlined at this point. Namely, the average in Eq. (2) involves an uncorrelated

wave function (in the form of a Slater determinant in either direct [27] or reciprocal [25] space). Therefore, by application of the Wick theorem, the nontrivial averages may be expressed in terms of $n_{i \sigma}^{(\alpha)}$, $\langle\hat{S}_{i}^{z f(\alpha)}\rangle_{0}$, $\langle\hat{c}_{i \sigma}^{(l) \dagger} \hat{c}_{j \sigma}^{(l)}\rangle_{0}$, etc. When executing this procedure, the projection part $\prod_{\alpha, l \neq i, j} \hat{P}_{G l \alpha}$, acting on the sites that differ from the two-state term in the starting Hamiltonian and generating higher-loop graphs, can be neglected. In effect, we obtain the renormalized energy functional

$$
\begin{aligned}
E_{G}= & \sum_{i j l \sigma} t_{i j}\left\langle\hat{c}_{i \sigma}^{(l) \dagger} \hat{c}_{j \sigma}^{(l)}\right\rangle_{0}+V \sum_{i l \sigma} q_{\sigma}\left(\left\langle\hat{f}_{i \sigma}^{(l) \dagger} \hat{c}_{i \sigma}^{(l)}\right\rangle_{0}+\text { c.c. }\right) \\
& +\sum_{i \sigma}\left[U^{\prime} g_{1 \sigma}+\left(U^{\prime}-J\right) g_{2 \sigma}\right]\left|\left\langle\hat{f}_{i \sigma}^{(1)} \hat{f}_{i \sigma}^{(2)}\right\rangle_{0}\right|^{2} \\
& -\sum_{i} 2 J\left\langle\hat{S}_{i}^{z f(1)}\right\rangle_{0}\left\langle\hat{S}_{i}^{z f(2)}\right\rangle_{0} \\
& +\sum_{i}\left(U^{\prime}-\frac{J}{2}\right)\left\langle\hat{n}_{i}^{f(1)}\right\rangle_{0}\left\langle\hat{n}_{i}^{f(2)}\right\rangle_{0} \\
& +\sum_{i l \sigma}\left(\epsilon^{f}-h \sigma\right)\left\langle\hat{n}_{i \sigma}^{f(l)}\right\rangle_{0}+U \sum_{i l} \lambda_{\uparrow \downarrow}^{2}\left\langle\hat{n}_{i \uparrow}^{f(l)}\right\rangle_{0}\left\langle\hat{n}_{i \downarrow}^{f(l)}\right\rangle_{0} \\
& -h \sum_{i l \sigma} \sigma\left\langle\hat{n}_{i \sigma}^{c(l)}\right\rangle_{0},
\end{aligned}
$$

where the renormalization factors
$$
g_{1 \sigma} \equiv 2\left(\lambda_{\uparrow \downarrow}^{2}-\lambda_{\bar{\sigma}}^{2}\right)\left(\lambda_{\sigma}^{2}+\left(\lambda_{\uparrow \downarrow}^{2}-\lambda_{\sigma}^{2}\right) n_{\bar{\sigma}}^{f(l)}\right) n_{\bar{\sigma}}^{f(l)},
$$

$$
g_{2 \sigma} \equiv\left(\lambda_{\uparrow \downarrow}^{2}-\lambda_{\bar{\sigma}}^{2}\right)^{2}\left(n_{\bar{\sigma}}^{f(l)}\right)^{2}+\left(\lambda_{\sigma}^{2}+\left(\lambda_{\uparrow \downarrow}^{2}-\lambda_{\sigma}^{2}\right) n_{\bar{\sigma}}^{f(l)}\right)^{2},
$$

and
$$
q_{\sigma} \equiv \lambda_{0} \lambda_{\sigma}+\left(\lambda_{\uparrow \downarrow} \lambda_{\bar{\sigma}}-\lambda_{0} \lambda_{\sigma}\right) n_{\bar{\sigma}}^{f(l)} \quad(5)
$$

appear in response to local electronic correlations $(\bar{\sigma} \equiv-\sigma)$ [12].

This renormalized Hamiltonian of the single-quasiparticle type with pairing should thus be diagonalized first, before the ground-state energy (2) in the correlated state is evaluated explicitly. Equivalently, optimization of $E_{G}$ over wave function $|\Psi_{0}\rangle$ yields an effective nonlinear Schrödinger equation $\mathcal{H}_{\text {eff }}|\Psi_{0}\rangle=E|\Psi_{0}\rangle$ with the following effective Hamiltonian:
$$
\mathcal{H}_{\mathrm{eff}}=\sum_{\mathbf{k}, \sigma} \Psi_{\mathbf{k} \sigma}^{\dagger}\left(\begin{array}{cccc}
\epsilon_{\mathbf{k} \sigma} & 0 & q_{\sigma} V & 0 \\
0 & -\epsilon_{\mathbf{k} \sigma} & 0 & -q_{\sigma} V \\
q_{\sigma} V & 0 & \epsilon_{\sigma}^{f} & \Delta_{\sigma \sigma}^{f f} \\
0 & -q_{\sigma} V & \Delta_{\sigma \sigma}^{f f} & -\epsilon_{\sigma}^{f}
\end{array}\right) \Psi_{\mathbf{k} \sigma}+E_{0},
$$

which is expressed now in terms of Nambu spinor $\Psi_{\mathbf{k} \sigma}^{\dagger} \equiv$ $(\hat{c}_{\mathbf{k} \sigma}^{(1) \dagger}, \hat{c}_{-\mathbf{k} \sigma}^{(2)}, \hat{f}_{\mathbf{k} \sigma}^{(1) \dagger}, \hat{f}_{-\mathbf{k} \sigma}^{(2)})$ and leads to the expectation value (2). Here
$$
\begin{aligned}
\epsilon_{\mathbf{k} \sigma}= & 2 t\left[\cos \left(k_{x}\right)+\cos \left(k_{y}\right)\right] \\
& +4 t^{\prime} \cos \left(k_{x}\right) \cos \left(k_{y}\right)-\mu-h \sigma
\end{aligned}
$$

is the Zeeman-split tight-binding dispersion relation for bare conduction electrons,
$$
\begin{aligned}
\epsilon_{\sigma}^{f} \equiv & \frac{\partial E_{G}}{\partial n_{i \sigma}^{f(1)}}=\epsilon^{f}+U \lambda_{\uparrow \downarrow}^{2} n_{i \bar{\sigma}}^{f(1)}+\left(U^{\prime}-J\right) n_{i \sigma}^{f(2)}+U^{\prime} n_{i \bar{\sigma}}^{f(2)} \\
& +\left(\frac{\partial q_{\bar{\sigma}}}{\partial n_{i \sigma}^{f(1)}} V \sum_{l}\left\langle\hat{f}_{i \bar{\sigma}}^{(l) \dagger} \hat{c}_{i \bar{\sigma}}^{(l)}\right\rangle_{0}+\text { c.c. }\right) \\
& +\left(\frac{\partial g_{1 \bar{\sigma}}}{\partial n_{i \sigma}^{f(1)}} U^{\prime}+\frac{\partial g_{2 \bar{\sigma}}}{\partial n_{i \sigma}^{f(1)}}\left(U^{\prime}-J\right)\right)\left|\left\langle\hat{f}_{i \bar{\sigma}}^{(1)} \hat{f}_{i \bar{\sigma}}^{(2)}\right\rangle_{0}\right|^{2} \\
& -\mu-h \sigma
\end{aligned}
$$

determines the position of the renormalized $f$-electron level, and $E_{0}$ is the energy shift (that does not influence expectation values but contributes to the ground-state energy). The effective gap parameter $\Delta_{\sigma \sigma}^{f f}$, and the effective SC coupling constant $\mathcal{V}_{\sigma}$ (to be addressed below), are defined by the relation
$$
\begin{aligned}
\Delta_{\sigma \sigma}^{f f} & \equiv \mathcal{V}_{\sigma}\left\langle\hat{f}_{i \sigma}^{(1)} \hat{f}_{i \sigma}^{(2)}\right\rangle_{0} \equiv \frac{\partial E_{G}}{\partial\left\langle\hat{f}_{i \sigma}^{(1) \dagger} \hat{f}_{i \sigma}^{(2) \dagger}\right\rangle_{0}} \\
& =-\left[g_{1 \sigma} U^{\prime}+g_{2 \sigma}\left(U^{\prime}-J\right)\right]\left\langle\hat{f}_{i \sigma}^{(1)} \hat{f}_{i \sigma}^{(2)}\right\rangle_{0}.
\end{aligned}
$$

The resultant integral Schrödinger-type equation is solved numerically in the loop with minimization of the energy functional [Eq. (4)] over the correlator parameter $x$. To avoid finite-size effects that become severe for weak SC order, considered here, we performed the calculations directly in the thermodynamic limit using adaptive integration. Note that the effective pairing potential $\mathcal{V}_{\sigma}$ can be attractive even in the regime where its Hartree-Fock (unrenormalized) correspondent $\mathcal{V}_{\sigma}^{\mathrm{HF}}=U-3 J$ is already repulsive [12]. In that case, the pairing is induced by nontrivial correlation effects.

A methodological remark is in place at this point. The above scheme employs correlator $\hat{P}_{G}$ that acts separately on each orbital. In a multiband system, such as the one considered here, one could expect that the correlator should allow for more general many-body states involving multiple orbitals at once. Such an extension makes it difficult to achieve numerical accuracy required to study SC order emerging on the scale of the order of 1 K in uranium materials. We have, nonetheless, performed such an extended analysis [20] for zero field and a limited range of model parameters, with the results very close to those obtained from the above simplified scheme. The discussion of those formal issues is deferred to Appendix A.

## III. RESULTS AND DISCUSSION

### A. Zero-field results as a reference point

The SC pairing discussed here is of local interorbital nature, i.e., of odd parity in the orbital and even in the spin indices, as was proposed before [20,28]. In Fig. 1(a) we draw schematically the sequence of phases obtained in zero applied field. The three SC states are labeled in a similar manner to those for the case of superfluid ${ }^{3} \mathrm{He}$, with $A_{1}$ being fully spin-polarized ( $\downarrow \downarrow$ Cooper pairs only), and $A_{2}$ phase is that with unequal order parameter amplitudes $\uparrow \uparrow$ and $\downarrow \downarrow$, which finally equalize in the PM state and result in $A$-type SC. Formally, the

![](./images/812777596570828801_2.jpg)

FIG. 1. (a) Sequence of ferromagnetic (FM2, FM1) and nonmagnetic (PM) phases, coexisting with superconducting $(A_{2}, A_{1}, A)$ states, as a function of increasing hybridization magnitude (emulating pressure change [19]) for zero external magnetic field. (b) The same as in (a), but for fixed hybridization and varying pressure, with the most prominent FM1 $+A_{1}$ phase taken as the starting point. The boundaries mark transition points in both the magnetic and superconducting sectors.

above SC states are characterized by nonvanishing anomalous amplitudes detailed in Table I. The coexistent phase FM1 + $A_{1}$ is the most prominent; $A_{2}$ and $A$ states play only a very minor, if not negligible, role in the field absence. We emulate changing external pressure by the corresponding change in hybridization magnitude (for a detailed discussion of this particular point, see Part I and Ref. [19]). As shown below, the role of the field is to enhance the presence of the $A_{2}$ phase.

For the sake of completeness, in Table II we provide selected numerical values of the effective SC gap parameters for $H=0$ in the $A_{1}, A_{2}$, and $A$ phases. They are defined as partial derivatives of the variational functional with respect to anomalous amplitudes [cf. Eqs. (9), (A17), and (A18)] and physically determine the spectrum of projected quasiparticle excitations [25]. As the SC transition sequence $A_{2} \to A_{1} \to A$ takes place simultaneously with that corresponding to discontinuous magnetic transitions (FM2 $\to$ FM1 $\to$ PM), they are also discontinuous, but the former discontinuities are probably too weak to be detected experimentally (note that the maximal value of the SC transition temperature does not exceed 1 K in all uranium systems) [1-7]. However, we obtain a clear sign of metasuperconducting transition accompanying the corresponding metamagnetic jumps. This issue is discussed below.

## B. Discontinuous phase transition in an applied magnetic field

In Fig. 1(b) we have drawn schematically the sequence of phases appearing with the increasing applied field, starting

<table>
<caption>TABLE I. Detailed structure of the anomalous local $f$-$f$ amplitudes for various coexistent magnetic and superconducting phases, appearing for the four-orbital periodic Anderson model (1).</caption>
<thead>
  <tr>
    <th>Phase</th>
    <th>Anomalous $f$-$f$ amplitudes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>PM $+A$</td>
    <td>$\langle \hat{f}_{i\downarrow}^{(1)\dagger} \hat{f}_{i\downarrow}^{(2)\dagger} \rangle_0 = \langle \hat{f}_{i\uparrow}^{(1)\dagger} \hat{f}_{i\uparrow}^{(2)\dagger} \rangle_0 > 0$</td>
  </tr>
  <tr>
    <td>FM1 $+A_{1}$</td>
    <td>$\langle \hat{f}_{i\downarrow}^{(1)\dagger} \hat{f}_{i\downarrow}^{(2)\dagger} \rangle_0 > 0$, $\langle \hat{f}_{i\uparrow}^{(1)\dagger} \hat{f}_{i\uparrow}^{(2)\dagger} \rangle_0 = 0$</td>
  </tr>
  <tr>
    <td>FM2 $+A_{2}$</td>
    <td>$\langle \hat{f}_{i\downarrow}^{(1)\dagger} \hat{f}_{i\downarrow}^{(2)\dagger} \rangle_0 > 0$ $\langle \hat{f}_{i\uparrow}^{(1)\dagger} \hat{f}_{i\uparrow}^{(2)\dagger} \rangle_0 > 0$</td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE II. Superconducting gap components as a function of hybridization $|V|$ for $U=4|t|$ and $J=1.6|t|$. Estimated numerical accuracy $\delta \Delta_{\sigma \sigma}^{f f}/|t|$ is also provided in the last column.</caption>
<thead>
  <tr>
    <th>$V/t$</th>
    <th>$100 \times \Delta_{\uparrow \uparrow}^{f f}/|t|$</th>
    <th>$100 \times \Delta_{\downarrow \downarrow}^{f f}/|t|$</th>
    <th>$100 \times \delta \Delta_{\sigma \sigma}^{f f}/|t|$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1.166667</td>
    <td>0.0000000</td>
    <td>0.0000000</td>
    <td>0.0000011</td>
  </tr>
  <tr>
    <td>1.3000000</td>
    <td>0.0038378</td>
    <td>0.0000000</td>
    <td>0.0000012</td>
  </tr>
  <tr>
    <td>1.3333333</td>
    <td>0.0225363</td>
    <td>0.0000000</td>
    <td>0.0000012</td>
  </tr>
  <tr>
    <td>1.4000000</td>
    <td>0.5660415</td>
    <td>0.0001295</td>
    <td>0.0000013</td>
  </tr>
  <tr>
    <td>1.4500000</td>
    <td>5.8775861</td>
    <td>0.0000000</td>
    <td>0.0000014</td>
  </tr>
  <tr>
    <td>1.5000000</td>
    <td>5.1822010</td>
    <td>0.0000000</td>
    <td>0.0000014</td>
  </tr>
  <tr>
    <td>1.5500000</td>
    <td>4.5934998</td>
    <td>0.0000000</td>
    <td>0.0000013</td>
  </tr>
  <tr>
    <td>1.6000000</td>
    <td>4.0906100</td>
    <td>0.0000000</td>
    <td>0.0000013</td>
  </tr>
  <tr>
    <td>2.0000000</td>
    <td>1.8155386</td>
    <td>0.0000000</td>
    <td>0.0000012</td>
  </tr>
  <tr>
    <td>2.5000000</td>
    <td>0.7775326</td>
    <td>0.0000000</td>
    <td>0.0000011</td>
  </tr>
  <tr>
    <td>3.0000000</td>
    <td>0.3706006</td>
    <td>0.0000000</td>
    <td>0.0000011</td>
  </tr>
  <tr>
    <td>3.5000000</td>
    <td>0.1909743</td>
    <td>0.0000000</td>
    <td>0.0000010</td>
  </tr>
  <tr>
    <td>4.0000000</td>
    <td>0.1049818</td>
    <td>0.0000000</td>
    <td>0.0000010</td>
  </tr>
  <tr>
    <td>4.1500000</td>
    <td>0.0887245</td>
    <td>0.0000000</td>
    <td>0.0000010</td>
  </tr>
  <tr>
    <td>4.1000000</td>
    <td>0.9525063</td>
    <td>0.9525063</td>
    <td>0.0000011</td>
  </tr>
  <tr>
    <td>4.2000000</td>
    <td>0.8016905</td>
    <td>0.8016935</td>
    <td>0.0000011</td>
  </tr>
  <tr>
    <td>4.2500000</td>
    <td>0.7355641</td>
    <td>0.7355662</td>
    <td>0.0000010</td>
  </tr>
  <tr>
    <td>4.4000000</td>
    <td>0.5685009</td>
    <td>0.5685018</td>
    <td>0.0000010</td>
  </tr>
  <tr>
    <td>5.0000000</td>
    <td>0.2062559</td>
    <td>0.2062561</td>
    <td>0.0000010</td>
  </tr>
</tbody>
</table>

from the most prominent FM1 $+A_{1}$. The high-field phase is always pure high-moment FM2. To illustrate the situation quantitatively, we have plotted in Figs. 2(a)-2(c) the total magnetic moment $m^{\text{tot}} \equiv m^f + m^c$ [cf. panel (a)], $\Delta_{\downarrow \downarrow}^{f f}$ [panel (b)], and $\Delta_{\uparrow \uparrow}^{f f}$ [panel (c)] SC amplitudes. All the transitions are of discontinuous metamagnetic/metasuperconducting character. The paired states disappear gradually as the magnetic moment increases in the FM2 phase. In that final state, both the diagonal pairing correlation $\langle \hat{f}_{i\sigma}^{(1)\dagger} \hat{f}_{i\sigma}^{(2)\dagger} \rangle_0$ and spin fluctuations are suppressed by the magnetic-field-enforced moment saturation. In Fig. 2 we show a representative situation near the FM2-FM1 boundary. Note that the considered discontinuous transitions may be easier to detect with the help of magnetic methods rather than by specific-heat measurements.

The character of the transitions as a function of applied field for a fixed value of hybridization is provided in Fig. 3. In Fig. 3(a) the components of the total moment are displayed. Note that the negative (Kondo-like) $c$-electron magnetic moment is practically field-independent. In Fig. 3(b) a pronounced $A_{1} \to A_{2}$ SC transition region is emphasized. Insets to Figs. 3(a) and 3(b) are to visualize clearly the discontinuities. This behavior may be compared with the measurements of the upper critical field $H_{c2}$ as a function of temperature close to the field-induced metamagnetic FM1 $\to$ FM2 transition point (cf. Fig. 10 of Ref. [4]). Specifically, for 13.5 kbar a sharp drop of SC transition temperature is observed experimentally above $\mu_0 H_x \approx 2$ T, in qualitative agreement with the theoretical result depicted in panel (b). Also, the SC state is detected unambiguously on both sides of the transition as is predicted by the local-correlation pairing scenario elaborated here. In Fig. 3(c) we plot the spin-dependent effective coupling constants $\mathcal{V}_\sigma$ (cf. I), defined by the relation $\Delta_{\sigma \sigma}^{f f} \equiv \mathcal{V}_\sigma \langle \hat{f}_{i\sigma}^{(1)} \hat{f}_{i\sigma}^{(2)} \rangle_0$ [cf. Eq. (9)]. Note that

![](./images/812777596570828801_3.jpg)

FIG. 2. (a) Total magnetization, $m^{\text{tot}} = m^f + m^c$ (a) and superconducting gap components [(b) and (c)] vs hybridization magnitude. Solid lines correspond to field value $h/|t| = 0.002$, the dashed lines represent the $h = 0$ situation [12]. The microscopic parameters are $U/|t| = 3.5$, $J/|t| = 1.1$, $T = 0$ K, $t'/|t| = 0.25$, $\epsilon^f/|t| = -4$, $n^{\text{tot}} \equiv n^f + n^c = 3.25$, and the field $h = 0.002|t|$, which corresponds to $\mu_0 H = 6.9$ T for the nearest-neighbor hopping $|t| = 0.2$ eV.

the pairing potential (effective coupling constant) is only moderately spin-dependent in an applied field, whereas the spin components of the gap behave in a very different manner. Such an asymmetry of the results for $\sigma = \uparrow, \downarrow$ components of $\Delta_{\sigma\sigma}^{ff}$ can be easily understood as, e.g., in the FM1 phase the spin-majority subband is full and the system becomes half-metallic, which implies $\Delta_{\uparrow\uparrow}^{ff} \equiv 0$. Finally, in panel (d) we plot the factors $q_\sigma$ that renormalize the $f$-$c$ hybridization magnitude [cf. Eqs. (6) and (5)]. These coefficients turn out to be of the order of unity, hence the major effect of correlations is to renormalize the pairing coupling constant rather than the single-particle dynamics.

To complete the picture, we have plotted in Figs. 4(a) and 4(b) the overall $f$-level occupancy ($n^f$) and that of the $c$ band ($n^c$); the details of $n^f$ evolution are shown in panel (b). The $f$-orbital occupancy is very close to unity, showing that those electrons have an almost localized nature.

![](./images/812777596570828801_4.jpg)

FIG. 3. Selected properties in an applied magnetic field at zero temperature. (a) Moments: $m^{\text{tot}}$, total (black line); $m^f$, $f$-electron component (blue); $m^c$, $c$-electron component (red). (b) Spin-triplet $f$-$f$ superconducting gap components: $\Delta_{\uparrow\uparrow}^{ff}$, purple; $\Delta_{\downarrow\downarrow}^{ff}$, green. (c) Spin-dependent pairing potential $\mathcal{V}_\sigma$. (d) Renormalization factors $q_\sigma$ [cf. Eq. (5)]. Phase transition from $\text{FM1} + A_1$ to $\text{FM2} + A_2$ takes place at $h_x/|t| = 0.001468$, which corresponds to magnetic field $\mu_0 H_x \approx 5.1$ T for $|t| = 0.2$ eV. The results are obtained for the following set of parameters: $U/|t| = 3.5$, $J/|t| = 1.1$, $T = 0$ K, $V/t = 1.26$, $t'/|t| = 0.25$, $\epsilon^f/|t| = -4$, $n^{\text{tot}} = 3.25$. Insets in (a) and (b) detail the discontinuous nature of the transitions. The pairing coupling constant is only weakly spin-dependent, whereas the gaps are due to the strong spin dependence of the electronic structure (see the text).

Moreover, approximately one additional electron (per U) is effectively transferred to the conduction band (strictly speaking $n^c \approx 1.25$). This conclusion confirms again our conjecture

![](./images/812777596570828801_5.jpg)

FIG. 4. Occupancies $n^f$ and $n^c$ as a function of applied magnetic field for the same parameters as those adopted in Fig. 3. The $f$-orbital occupancy is almost equal to unity showing an almost localized nature of those electrons even in the presence of a sizable hybridization.

reached before [12] that in the case of $\text{U}^{3+}$ each ion effectively turns into $\text{U}^{4+}$ with two nearly localized electrons and an itinerant electron created at the same time. Also, the Hund's-rule and intraorbital Coulomb-interaction contributions to the total energy depend relatively strongly on the value of the applied field, as demonstrated in Fig. 5. This feature supports further the strongly correlated nature of the system, in which various contributions balance out (partially compensate) each other in such a manner that a much smaller Zeeman contribution plays the role of a tip of balance between the localized and itinerant states of $f$-electrons [28]. Such a circumstance is characteristic of a Hund metal, as elaborated in I. Additionally, the SC in the relevant uranium systems emerges at low temperatures, typically below 1 K [1-7]. The related discontinuous transformations in the field involve even more subtle free-energy changes, as shown explicitly in Fig. 6 for the situation with FM1 $+A_1 \to$ FM2 $+A_2$ phase transformation. The corresponding total-energy change is of the order $10^{-5}|t|$, which for $|t| \sim 0.2$ eV is below the scale of 0.1 K. Nevertheless, the accuracy of our numerical results is well below these values (cf. Fig. 6 of Part I [12]).

![](./images/812777596570828801_6.jpg)

FIG. 5. Relative contributions of the renormalized Hund's-rule coupling and direct intraorbital Coulomb interactions to the ground-state energy for the value of hybridization $V/t=1.26$, i.e., at the threshold of FM2 $\to$ FM1 transition, where the $A_1$ SC phase appears in an abrupt manner. The model parameters coincide with those adopted in Fig. 3.

![](./images/812777596570828801_7.jpg)

FIG. 6. The ground-state energies of the two phases marked (a) with the phase-transformation point marked by the vertical dashed line. The difference of energies of the two phases (b) is of the order of 0.1 K. Note also that the transition is discontinuous as the two lines in (a) have at $h_x$ slightly different slopes.

Finally, in Fig. 7 we plot the boundary line between the FM1 $+A_1$ and FM2 $+A_2$ phases in the $H$-$|V|$ plane. It has a linear character in this narrow range of $V/t$ encompassing the FM2-FM1 discontinuous metamagnetic transition at $H=0$ as a starting point. This borderline may serve as an important feature and, in particular, help to single out the relevant SC

![](./images/812777596570828801_8.jpg)

FIG. 7. Calculated $f$-$c$ hybridization dependence of the characteristic transition field $\mu_0 H_x$ in the vicinity of the FM2-FM1 metamagnetic instability for $H=0$. The weak discontinuity may be detected by the magnetic susceptibility measurements across the boundary for fixed pressure ($V/t$ ratio).

205106-6

![](./images/812777596570828801_9.jpg)

FIG. 8. Renormalized band structure for $h/|t|=0.002$ and $V/t=1.26$ in the FM2 $+A_{2}$ phase (set of other parameters: $U/|t|=$ 3.5, $J/|t|=1.1$, $T=0$ K, $n^{\text{tot}}=3.25$, $t'/|t|=0.25$, $\epsilon^{f}/|t|=-4$). The eigenenergies are represented by dotted lines. The partial spectral-weight contributions from $f$-electrons [(a) and (b)] are marked in blue, whereas those for $c$-electrons [(c) and (d)] are in red. Color intensity represents the spectral-weight magnitude. In panel (e) the spin-resolved density of states is presented.

phases with symmetry of the order parameter $(A_{1}\to A_{2})$
changing in a discontinuous manner.

In summary, the observed SC discontinuities in an applied
magnetic field are relatively small. However, with the help
of sensitive magnetic measurements of ac susceptibility, they
should be detectable. Also, the appearance of the second
component of the SC gap at the $A_{1}\to A_{2}$ transition may
become observable in the pair tunneling spectroscopy. These
rather simple remarks require, however, a more quantitative
substantiation.

### C. Electronic structure

FM and SC phase transitions have a substantial impact
on the electronic (renormalized-band) structure. Particularly
interesting is the situation near the boundary between FM2 +
$A_{2}$ and FM1 $+A_{1}$ states. To elucidate the changes on both
sides of the transition, in Figs. 8 and 9 we have plotted
an exemplary structure along the high-symmetry lines just
below $(V/t=1.26)$ and just above that value $(V/t=1.262)$
for $h=2\times 10^{-3}|t|$. The slightly different magnitudes of $V$

![](./images/812777596570828801_10.jpg)

FIG. 9. (a)-(d) Band structure for $h/|t|=0.002$ and slightly larger hybridization $V/t=1.262$ in the FM1 $+A_{1}$ phase (the remaining parameters are the same as in Fig. 8). Eigenenergies are represented by dotted lines, partial contributions from $f$-electrons are marked in blue, whereas those from $c$-electrons are in red. Color intensity represents the spectral weight. (e) Orbital- and spin-resolved density of states.

have been selected to visualize the situation on both sides of the discontinuous FM1 $\rightarrow$ FM2 transition. The spin subbands with the dominant $f$ character are marked in blue. The spin splitting is induced mainly by Hund's rule and on-site repulsion $U$ (the effects of applied field and pairing are of minor importance). Remarkably, the $c$ electrons (marked in red in the lower panel) exhibit also a comparable spin splitting. This effect is caused by the circumstances in which the $c$ electrons are hybridized with their $f$-electron partners and, therefore, the Hund's rule interaction is transferred from the $f$- to the $c$-system. Note that the occupancy of each of the $f$ orbitals is $n^f/2=1\pm\delta$, with $\delta\ll1$ [cf. Fig. 4(b)], where the small portion $\delta$ comes from the upper spin subband, which crosses the Fermi level (zero-energy level) near the $\Gamma$ point. This is explicitly visualized on the density of states (right panel), where the $f\downarrow$ subband barely touches the Fermi energy and the majority-spin subband is practically filled. To a good accuracy, the system is thus a half metal with the predominant spin-minority carriers at the Fermi level. This is the reason why the $A_2$ phase is stable then and with the amplitudes $\Delta_{\downarrow\downarrow}\gg\Delta_{\uparrow\uparrow}$. The situation turns into an extreme case, with only $\Delta_{\downarrow\downarrow}\neq0$ in the FM1+$A_1$ phase. The latter result rationalizes nicely the related observation in the $H=0$ situation [12]. Note, however, that the exact half-metallic behavior, obtained in the present model, might be obscured in the real material by other bands that are weakly coupled to the considered $f$-$c$ subsystem.

## IV. OUTLOOK

### A. Effect of spin fluctuations (tentative)

Our present approach, based on the first nontrivial order (SGA) of treating the interelectronic correlations on a local scale, cannot explain enhanced residual linear specific heat appearing at temperatures well below $T_c$ in UGe$_2$ [14], as well as the strong effective mass enhancement at the FM1 $\rightarrow$ FM2 transition there [11,29]. Additionally, NQR relaxation with an anomalous temperature dependence is observed at the FM to PM transition at low temperature [30]. All these features may be explained qualitatively in terms of FM spin fluctuations starting from our renormalized mean-field picture. Whereas overall features of a transition from nonunitary to unitary SC are well reproduced by our phase diagram (also for UTe$_2$; cf. Ref. [31]), the long-wavelength fluctuations should be included, particularly for low-moment bearing systems UCoGe and UIr.

A general way to extend our work is as follows. We start from the effective Hamiltonian (1), but with renormalized microscopic parameters $U\lambda_{\uparrow\downarrow}^2$ and $Jg_{2\sigma}$ [cf. Eq. (4)], and we proceed with the Hubbard-Stratonovich transformation, as outlined in Appendix B for the case of a FM state. To incorporate fluctuations of the SC order parameter, one should include also the bilinear representation of the spin part $\sim Jg_{2\sigma}$, derived in Ref. [32]. However, a quantitative implementation of this program is quite cumbersome, as it requires computation of renormalized coupling constants at each stage of the analysis, before and after including the fluctuations in each order. Nonetheless, we believe that such a solution is possible to tackle, as the renormalized coupling parameters are reduced in the process already at the level of SGA. It is tempting to suggest that the effective picture should be not far away from that based on a $1/N$ expansion with effective parameters $U$ and $J$ (cf. Appendix B) calculated self-consistently within the SGA [33].

### B. Summary

In the preceding paper [12], referred to here as Part I, we have constructed a fairly complete zero-magnetic-field phase diagram composed of spin-triplet paired states coexisting with the ferromagnetic FM1 and FM2 phases. The $A_2$ and $A$ SC states appear in the field absence only with very small amplitudes. In the present work, we have shown that the applied magnetic field allows for fine-tuning of those phases and is likely to make them observable. In this manner, one can detect the states analogous to those seen clearly only for the superfluid $^3$He [9]. However, in contrast to $^3$He, here the pairing is of $s$-wave character, i.e., with an intra-atomic spin-triplet and the orbital singlet to make the wave function of the local pairs antisymmetric. It should be emphasized that this picture is applied here for moderately correlated systems, in which the pairing is induced by Hund's rule combined with direct short-range Coulomb interaction. In the strong-correlation limit, this type of pairing would have intersite (real-space) character with either spin-triplet or spin-singlet nature, depending on the band filling [34,35].

The principal result of this and the preceding [12] work is to describe, within a single (orbitally degenerate) Anderson lattice model, coexistent FM and spin-triplet SC phases within a consistent picture. In this way, we extend the well-established approaches to correlated normal and magnetic systems [28] to include the SC states coexisting with them and within a single mechanism. It must be emphasized that such a renormalized mean-field theory may also be generalized to a more involved systematic form of diagrammatic expansion, DE-GWF [36,37]. However, such an approach becomes quite involved in the multiorbital situation, particularly with multiple coexisting phases [27,38]. Inclusion of higher-order correlations introduces then an additional admixture of intersite correlations to the present local pairing. This should be an objective of a separate study.

At the end, we should mention that the present model neglects spin-orbit coupling and magnetocrystalline anisotropy in the uranium compounds addressed above [39,40]. From the fact that the overall phase diagram and the coexistent phases are reproduced correctly, we draw the conclusion that the orbital moment may be frozen (we consider only spin-aligned phases) and that the anisotropic character of the system is enforced naturally by the presence of the long-range FM order along the easy axis. Obviously, this may not be that simple if we would like to discuss the situation in the field by changing its orientation.

## ACKNOWLEDGMENT

This work was supported by Grant OPUS No. UMO-2018/29/B/ST3/02646 from Narodowe Centrum Nauki (NCN).

## APPENDIX A: STATISTICALLY CONSISTENT GUTZWILLER APPROXIMATION (SGA): SIMPLIFIED VERSUS FULL FORMS

In the preceding paper [12] (cf. Appendix A therein) we have discussed in detail the SGA approximation. Here we provide a more formal background. First, the multiband trial function for the ground state is selected in the form

$$
\left|\Psi_{G}\right\rangle=\prod_{i} \hat{P}_{i}\left|\Psi_{0}\right\rangle, \tag{A1}
$$

where $|\Psi_{0}\rangle$ is an antisymmetrized product (Slater determinant) of single-particle wave functions, in general describing a noncorrelated broken symmetry state, for which Wick's theorem holds. Operator $\hat{P}_{i}$ is the so-called Gutzwiller correlator that changes the weights of various many-body configurations in the variational wave function $|\Psi_{G}\rangle$. The general form of $\hat{P}_{i}$ is

$$
\hat{P}_{i}=\sum_{I I^{\prime}} \lambda_{i I I^{\prime}}|I, i\rangle\left\langle I^{\prime}, i\right|, \tag{A2}
$$

where the states $\{|I, i\rangle\}_{I}$ span the local Fock space of the correlated orbitals at site $i$ and the variational variables $\lambda_{i I I^{\prime}}$ form a matrix, here taken in the real-valued and symmetric form. Those correlated local spin-orbital states can be represented as

$$
|I, i\rangle=\prod_{\alpha \in I}^{<} \hat{f}_{i \alpha}^{\dagger}|0, i\rangle, \tag{A3}
$$

where $\alpha=(l, \sigma)$ labels combined spin-orbital indices, and the symbol "<" indicates a specified selected ascending order of the creation operators. Likewise,

$$
\left\langle I^{\prime}, i\right|=\prod_{\alpha \in I^{\prime}}^{>}\left\langle 0, i\right| \hat{f}_{i \alpha} \tag{A4}
$$

contains the annihilation operators in descending order so that

$$
|I, i\rangle\left\langle I^{\prime}, i\right|=\prod_{\alpha \in I}^{<} \hat{f}_{i \alpha}^{\dagger} \prod_{\beta \in I^{\prime}}^{>} \hat{f}_{i \beta} \prod_{\gamma \notin I \cup I^{\prime}}\left(1-\hat{n}_{i \gamma}^{f}\right). \tag{A5}
$$

The basic task is to compute the ground-state energy. For that purpose, one needs to evaluate the averages of the form

$$
\left\langle\Psi_{G}\left|\hat{O}_{i}\right| \Psi_{G}\right\rangle=\frac{\left\langle\Psi_{0}\left|\left(\prod_{j} \hat{P}_{j}\right) \hat{O}_{i}\left(\prod_{j} \hat{P}_{j}\right)\right| \Psi_{0}\right\rangle}{\left\langle\Psi_{0}\left|\left(\prod_{j} \hat{P}_{j}\right)\left(\prod_{j} \hat{P}_{j}\right)\right| \Psi_{0}\right\rangle}. \tag{A6}
$$

The products of local correlators can now be rearranged by using the fact that $\hat{P}_{i}$ and $\hat{P}_{j}$ commute for $i \neq j$. In effect,

$$
\left\langle\hat{O}_{i}\right\rangle=\frac{\left\langle\left(\prod_{j \neq i} \hat{P}_{j}^{2}\right) \hat{P}_{i} \hat{O}_{i} \hat{P}_{i}\right\rangle_{0}}{\left\langle\prod_{j} \hat{P}_{j}^{2}\right\rangle_{0}}, \tag{A7}
$$

where the averages with the subscript "0" are taken in the uncorrelated state, so that when the Wick theorem is applied to the averages in the uncorrelated $\langle\cdots\rangle_{0}$ representation, we obtain

$$
\begin{aligned}
\left\langle\prod_{j} \hat{P}_{j}^{2}\right\rangle_{0}\left\langle\hat{O}_{i}\right\rangle= & \left\langle\prod_{j \neq i} \hat{P}_{j}^{2}\right\rangle_{0}\left\langle\hat{P}_{i} \hat{O}_{i} \hat{P}_{i}\right\rangle_{0} \\
& +\sum_{\substack{\text { all pairs } \\
\text { of n.n. } \\
\text { contractions }}}\left\langle\overbrace{\prod_{j \neq i} \hat{P}_{j}^{2}}^{]}\right\rangle_{0}\left\langle\hat{P}_{i} \hat{O}_{i} \hat{P}_{i}\right\rangle_{0}+\cdots, \tag{A8}
\end{aligned}
$$

where the symbol

$$
\sum_{\substack{\text { all pairs } \\
\text { of n.n. } \\
\text { contractions }}}\langle\overbrace{\hat{\mathcal{A}}}^{]}\rangle_{0}\langle\overbrace{\hat{\mathcal{B}}}^{]}\rangle_{0} \tag{A9}
$$

represents all the nonzero pair contractions selected for a given broken-symmetry state. A detailed procedure is quite cumbersome and will not be detailed here [20,36,37].

Under the so-called Gutzwiller conditions [20,36,37]

$$
\left\langle\hat{P}_{i}^{2}\right\rangle_{0}=1, \tag{A10}
$$

$$
\left\langle\hat{P}_{i}^{2} \hat{f}_{i \alpha}^{\dagger} \hat{f}_{i \beta}\right\rangle_{0}=\left\langle\hat{f}_{i \alpha}^{\dagger} \hat{f}_{i \beta}\right\rangle_{0}, \tag{A11}
$$

and for large site-coordination number, a straightforward general formula for the expectation values of local operators is obtained,

$$
\left\langle\Psi_{G}\left|\hat{O}_{i}\right| \Psi_{G}\right\rangle=\left\langle\hat{P}_{i} \hat{O}_{i} \hat{P}_{i}\right\rangle_{0}, \tag{A12}
$$

which can be used to evaluate $\langle\Psi_{G}|\mathcal{H}| \Psi_{G}\rangle$ (note that all the $f$-dependent terms are local).

In effect, we obtain Landau-type functional $L$, which, at $T=0$, is composed of $\langle\mathcal{H}\rangle_{G}$ and incorporates the condition for the chemical potential, the enforced normalization $\langle\Psi_{G}|\Psi_{G}\rangle=1$, as well as the requirement of having the same number of particles in the initial $(|\Psi_{0}\rangle)$ and correlated $(|\Psi_{G}\rangle)$ states (before and after the projection with $\hat{P}_{G}$), namely

$$
\begin{aligned}
L \equiv & \langle\hat{H}\rangle_{G}-\mu \sum_{i}\left(\sum_{\alpha}\left\langle\hat{n}_{i \alpha}^{f}\right\rangle+\sum_{\beta}\left\langle\hat{n}_{i \beta}^{c}\right\rangle-n^{\mathrm{tot}}\right) \\
& +\sum_{i} \eta_{i}\left(\left\langle\hat{P}_{i}^{2}\right\rangle_{0}-1\right) \\
& +\sum_{i \alpha \beta} \eta_{i \alpha \beta}\left(\left\langle\hat{P}_{i}^{2} \hat{f}_{i \alpha}^{\dagger} \hat{f}_{i \beta}\right\rangle_{0}-\left\langle\hat{f}_{i \alpha}^{\dagger} \hat{f}_{i \beta}\right\rangle_{0}\right). \tag{A13}
\end{aligned}
$$

The functional $L$ needs to be optimized with respect to all $\lambda$ and $\eta$ parameters, representing additional constraints [20] in the SGA approximation, as well as $\mu$ and $|\Psi_{0}\rangle$. Minimization with respect to $|\Psi_{0}\rangle$ leads to an effective (renormalized) quasiparticle Hamiltonian in an applied magnetic field $h$, which, in the component Nambu representation [cf. Eq. (6)], can be recast to the following form:

$$
\mathcal{H}_{\mathrm{eff}}=\sum_{\mathbf{k} \sigma} \Psi_{\mathbf{k} \sigma}^{\dagger}\left(\begin{array}{cccc}
\epsilon_{\mathbf{k} \sigma} & 0 & \tilde{V}_{\sigma} & \tilde{\Delta}_{f c \sigma} \\
0 & -\epsilon_{\mathbf{k} \sigma} & \tilde{\Delta}_{f c \sigma} & -\tilde{V}_{\sigma} \\
\tilde{V}_{\sigma} & \tilde{\Delta}_{f c \sigma} & \tilde{\epsilon}_{f \sigma} & \tilde{\Delta}_{f \sigma} \\
\tilde{\Delta}_{f c \sigma} & -\tilde{V}_{\sigma} & \tilde{\Delta}_{f \sigma} & -\tilde{\epsilon}_{f \sigma}
\end{array}\right) \Psi_{\mathbf{k} \sigma}+E_{0}, \tag{A14}
$$

with the renormalized parameters defined as

$$
\tilde{\epsilon}_{f \sigma} \equiv \frac{1}{2} \frac{\partial L}{\partial n_{f \sigma}^{0}}, \tag{A15}
$$

$$
\tilde{V}_{\sigma} \equiv \frac{1}{4} \frac{\partial L}{\partial v_{\sigma}^{0}}, \tag{A16}
$$

$$
\tilde{\Delta}_{f \sigma} \equiv \frac{1}{2} \frac{\partial L}{\partial A_{f \sigma}^{0}}, \tag{A17}
$$

$$
\tilde{\Delta}_{f c \sigma} \equiv \frac{1}{4} \frac{\partial L}{\partial A_{f c \sigma}^{0}}, \tag{A18}
$$

and $\epsilon_{\mathbf{k} \sigma}$ is given by Eq. (7). The bare parameters read

$$
n_{f \sigma}^{0} \equiv\left\langle\hat{f}_{i l \sigma}^{\dagger} \hat{f}_{i l \sigma}\right\rangle_{0}, \tag{A19}
$$

$$
n_{c \sigma}^{0} \equiv\left\langle\hat{c}_{i l \sigma}^{\dagger} \hat{c}_{i l \sigma}\right\rangle_{0}, \tag{A20}
$$

$$
v_{\sigma}^{0} \equiv\left\langle\hat{f}_{i l \sigma}^{\dagger} \hat{c}_{i l \sigma}\right\rangle_{0}, \tag{A21}
$$

$$
A_{f \sigma}^{0} \equiv\left\langle\hat{f}_{i 1 \sigma}^{\dagger} \hat{f}_{i 2 \sigma}^{\dagger}\right\rangle_{0}, \tag{A22}
$$

$$
A_{f c \sigma}^{0} \equiv\left\langle\hat{f}_{i 1 \sigma}^{\dagger} \hat{c}_{i 2 \sigma}^{\dagger}\right\rangle_{0}=\left\langle\hat{c}_{i 1 \sigma}^{\dagger} \hat{f}_{i 2 \sigma}^{\dagger}\right\rangle_{0}. \tag{A23}
$$

Note that the averages (A19)–(A23) define the uncorrelated broken-symmetry state, whereas Eqs. (A15)–(A18) define the physical state. Also, the Hamiltonian (A14) is self-consistent in which the quantities defining the physical state are $\mu$, $\tilde{\Delta}_{f \sigma}$, $\tilde{\Delta}_{f c \sigma}$, $\tilde{V}_{\sigma}$, $\tilde{\epsilon}_{f \sigma}$, and the band dispersion relation of $\epsilon_{\mathbf{k} \sigma}$ for bare $c$ electrons. They are determined from a system of five self-consistent equations. Note also that in the effective Hamiltonian (6) the anomalous averages $\tilde{\Delta}_{f c \sigma}$ are set to zero, which means that the direct hybrid ($c$-$f$) pairing is regarded as negligible. This is not the case for the singlet-paired systems [18,41,42].

In Figs. 10(a)–10(d) we display the selected properties of the SC state on the basis of the full solution of the self-consistent equations obtained with the help of Hamiltonian (A14), for the three selected values of the Hund’s rule exchange integral $J$. Namely, in (a) we display the total magnetic moment $m^{\text{tot}}$. Panel (b) shows the dominant (spin-down) pairing amplitude in $\text{FM1} + A_1$ and $\text{PM} + A$ phases. In panel (c) we draw the ground-state energy, whereas in (d) we plot the condensation energy (the energy difference between the SC state and that corresponding to the appropriate pure FM phase). All these characteristics are quantitatively similar to those obtained earlier within the simplified picture with $\Delta_{f c \sigma} \equiv 0$. From that we draw the conclusion that the hybrid pairing component has a negligible effect on SC. Also, the component $\Delta_{0}$ of the pairing amplitude of $f$-electrons (i.e., the one with zero $z$ spin-component of the pair) is suppressed in this system with relatively large $U$. Hence, the simplified solution detailed in Appendix A of Ref. [12] represents, to a good accuracy, the full solution. The same type of picture is used throughout the present paper for the case of nonzero applied field.

![](./images/812777596570828801_11.jpg)

FIG. 10. Exemplary phase diagram obtained with the multiorbital correlator in the $f$-electron sector. (a) The total magnetization $m$, (b) pairing amplitude $A_{f \downarrow}$, (c) ground-state energy $E_{G}$ per lattice site, and (d) SC condensation energy $\Delta E$, all as a function of hybridization for $n=3.2$, $\epsilon_{f}=-3|t|$, $U+J=5|t|$, square lattice density of $c$ states: $t<0$, $t'=0.25|t|$, and for three rations $J/U=$ 0.5, 0.45, 0.4. Note that $A_1$ phase is characterized by $A_{f \uparrow}=0$, whereas in $A$ phase we have $A_{f \uparrow}=A_{f \downarrow}$. The condensation energy for $J/U=0.4$ is so low that it is hardly visible on the scale. Note that despite seemingly discontinuous behavior, $\Delta E$ does not exhibit jumps across the joint metamagnetic and metasuperconducting transitions, but it varies extremely rapidly in the narrow parameter range. For the zero-field case, this has been detailed in Appendix D of Ref. [43].

## APPENDIX B: INCORPORATION OF QUANTUM SPIN FLUCTUATIONS IN AN ORBITALLY DEGENERATE SYSTEM: AN OUTLINE

The atomic part of the Hamiltonian (1) for $f$ electrons located on orbitals $l=1,2,\dots,d$, where $d$ is their degeneracy, can be rewritten in the form

$$
\begin{aligned}
\mathcal{H}_{I}=U \sum_{i l} \hat{n}_{i \downarrow}^{f(l)} \hat{n}_{i \uparrow}^{f(l)}+\frac{K}{2} \sum_{\substack{i l l^{\prime} \\
\sigma \sigma^{\prime}}} \hat{n}_{i \sigma}^{f(l)} \hat{n}_{i \sigma^{\prime}}^{f\left(l^{\prime}\right)}-J \sum_{i l l^{\prime}} \hat{\mathbf{S}}_{i}^{f(l)} \hat{\mathbf{S}}_{i}^{f\left(l^{\prime}\right)},
\end{aligned}
\tag{B1}
$$

where $K=U'-J/2$ and the primed summation is performed over $l\neq l'$. Note that the interaction parameters $U$, $K$, and $J$ are taken as the same for each pair $(l,l')$ of orthogonalized orbitals. Therefore, we introduce next the global spin- and particle-number operators as
$$
\hat{\mathbf{S}}_{i}^{f} \equiv \sum_{l=1}^{d} \hat{\mathbf{S}}_{i}^{f(l)}, \quad \hat{n}_{i}^{f} \equiv \sum_{\sigma} \hat{n}_{i \sigma}^{f} \equiv \sum_{l \sigma} \hat{n}_{i \sigma}^{f(l)}. \tag{B2}
$$

By expressing the orbital-dependent operators in Eq. (B1) through their global correspondents [44], up to a constant, one obtains
$$
\mathcal{H}_{I}=\frac{1}{2} K \sum_{i}\left(\hat{n}_{i}^{f}\right)^{2}-J \sum_{i}\left(\hat{\mathbf{S}}_{i}^{f}\right)^{2}+I \sum_{i l} \hat{n}_{i \uparrow}^{f(l)} \hat{n}_{i \downarrow}^{f(l)} \tag{B3}
$$
with $I \equiv U-K-\frac{3}{2} J$. Assuming the standard relation for $d$ electrons $U'=U-2J$, we obtain $K=U-\frac{5}{2}J$, $I=J/2$. We thus have decomposed the intra-atomic interaction into the three parts: local charge, spin, and the Hubbard-type correlations, respectively. Now, noticing that the first two terms give a contribution of the order of $d^{2}$, whereas the third one $\sim d$, and disregarding charge fluctuations, we have, to a first approximation,
$$
\mathcal{H}_{I}=-\left(J+\frac{I}{3 d}\right) \sum_{i}\left(\hat{\mathbf{S}}_{i}^{f}\right)^{2}, \tag{B4}
$$
i.e., the total local spin fluctuations provide the leading contribution. In the FM state, one can take $\hat{\mathbf{S}}_{i}^{f}=\langle S_{i}^{f z}\rangle \hat{\mathbf{e}}_{z}+\hat{\mathbf{s}}_{i}$, where the static part of magnetization introduces a natural anisotropy axis for spin fluctuations expressed by $\hat{\mathbf{s}}_{i}=\hat{\mathbf{s}}_{i}(\tau)$, where $\tau$ is the imaginary time. To include the dynamic fluctuations, one utilizes the Hubbard-Stratonovich transformation
$$
\exp \left(\hat{a}^{2}\right)=\int_{-\infty}^{\infty} d x \exp \left(-\pi x^{2}-2 \hat{a} x \sqrt{\pi}\right) \tag{B5}
$$
for each spin-operator component $\hat{S}^{f \alpha}(\tau)$. By including also the single-particle part $\hat{\mathcal{H}}_{0}$, we obtain the following expression for the system density matrix:
$$
\begin{aligned}
\rho= & T e^{-\beta \hat{\mathcal{H}}_{0}} \prod_{i} \int \mathcal{D} \xi_{i}^{\alpha}(\tau) \exp \left(-\int_{0}^{1} d \tau\left(\xi_{i}^{\alpha}\right)^{2}\right. \\
& \left.-\int_{0}^{1} d \tau 2 i \sqrt{\pi \beta J} \xi_{i}^{\alpha}(\tau) A_{i}^{\alpha}(\tau)\right),
\end{aligned} \tag{B6}
$$
where $\mathcal{D}\xi_{i}^{\alpha}(\tau)$ denotes functional integration over each Gaussian random field $\xi_{i}^{\alpha}(\tau)$, $\beta \equiv (k_B T)^{-1}$, $\tau$ is in units of $\beta$, and $A_{i}^{\alpha}(\tau)\equiv \hat{S}_{i}^{f \alpha}(\tau)$. One can see that this form is of the same type as that for the Hubbard model with the explicitly rotationally invariant interaction term
$$
U \hat{n}_{i \uparrow} \hat{n}_{i \downarrow}=\frac{1}{4} U\left(\hat{n}_{i \uparrow}+\hat{n}_{i \downarrow}\right)^{2}-\frac{1}{3} U \hat{\mathbf{S}}_{i}^{2} \tag{B7}
$$
and fluctuating field $\hat{S}_{i}^{\alpha}(\tau)$ [45]. Therefore, the spin-fluctuation contribution can be calculated in the same manner as in the Hubbard model with the part $\langle S_{i}^{z}\rangle \neq 0$. However, in order to incorporate the fluctuations starting from the SGA (renormalized mean-field) solution, replacing the Hartree-Fock solution as a saddle-point approximation, our coupling constant must also be renormalized, $J \to J\lambda_J$, as contained when solving the self-consistent equation for $\langle S_{i}^{f z}\rangle_0$. Implementation of this program is quite involved, both analytically and numerically, so it should be analyzed in detail separately. In any case, the spin-fluctuation contribution will renormalize the SGA characteristics by not just an additive contribution. However, a further generalization of expression (B4) is required to include also the pairing fluctuations. This can be implemented in the following manner. We start from the binomial representation of the Hund's rule part, which, for the simplest spin $S=1$ case $(l=1,2)$, takes the form
$$
\hat{\mathbf{S}}_{i}^{f(l)} \hat{\mathbf{S}}_{i}^{f\left(l^{\prime}\right)}+\frac{3}{4} \hat{n}_{i}^{f(l)} \hat{n}_{i}^{f\left(l^{\prime}\right)}=\sum_{m=-1}^{1} \hat{A}_{i m}^{\dagger} \hat{A}_{i m}^{f}, \tag{B8}
$$
where the pairing amplitude components are defined as [32]
$$
\begin{aligned}
\hat{A}_{i 1}^{\dagger} & \equiv \hat{f}_{i \uparrow}^{(1) \dagger} \hat{f}_{i \uparrow}^{(2) \dagger}, \\
\hat{A}_{i 0}^{\dagger} & \equiv \frac{1}{\sqrt{2}}\left(\hat{f}_{i \uparrow}^{(1) \dagger} \hat{f}_{i \downarrow}^{(2) \dagger}+\hat{f}_{i \downarrow}^{(1) \dagger} \hat{f}_{i \uparrow}^{(2) \dagger}\right), \\
\hat{A}_{i-1}^{\dagger} & \equiv \hat{f}_{i \downarrow}^{(1) \dagger} \hat{f}_{i \downarrow}^{(2) \dagger}.
\end{aligned} \tag{B9}
$$

This bilinear form can be transformed to the corresponding representation (B6) and will involve additional fluctuating fields $\{\eta_{i}^{m}(\tau)\}$ $(m=-1,0,+1)$, which express three local components of the pairing $\Delta_{i m}^{f}$. In general, one can decompose the Hund's rule term into two components, diagonal (magnetic moment) and off-diagonal (pairing gap), according to the prescription provided in Ref. [46].

[1] S. S. Saxena, P. Agarwal, K. Ahilan, F. M. Grosche, R. K. W. Haselwimmer, M. J. Steiner, E. Pugh, I. R. Walker, S. R. Julian, P. Monthoux, G. G. Lonzarich, A. Huxley, I. Sheikin, D. Braithwaite, and J. Flouquet, Superconductivity on the border of itinerant-electron ferromagnetism in UGe₂, Nature (London) 406, 587 (2000).

[2] N. Tateiwa, T. C. Kobayashi, K. Hanazono, K. Amaya, Y. Haga, R. Settai, and Y. Onuki, Pressure-induced superconductivity in a ferromagnet UGe₂, J. Phys.: Condens. Matter 13, L17 (2001).

[3] C. Pfleiderer and A. D. Huxley, Pressure Dependence of the Magnetization in the Ferromagnetic Superconductor UGe₂, Phys. Rev. Lett. 89, 147005 (2002).

[4] A. Huxley, I. Sheikin, E. Ressouche, N. Kernavanois, D. Braithwaite, R. Calemczuk, and J. Flouquet, UGe₂: A ferromagnetic spin-triplet superconductor, Phys. Rev. B 63, 144519 (2001).

[5] D. Aoki, A. Huxley, E. Ressouche, D. Braithwaite, J. Flouquet, J.-P. Brison, E. Lhotel, and C. Paulsen, Coexistence of superconductivity and ferromagnetism in URhGe, Nature (London) 413, 613 (2001).

[6] N. T. Huy, A. Gasparini, D. E. de Nijs, Y. Huang, J. C. P. Klaasse, T. Gortenmulder, A. de Visser, A. Hamann, T. Görlach,

and H. v. Löhneysen, Superconductivity on the Border of Weak Itinerant Ferromagnetism in UCoGe, *Phys. Rev. Lett.* **99**, 067006 (2007).

[7] T. C. Kobayashi, S. Fukushima, H. Hidaka, H. Kotegawa, T. Akazawa, E. Yamamoto, Y. Haga, R. Settai, and Y. Onuki, Pressure-induced superconductivity in ferromagnet UIr without inversion symmetry, *Physica B* **378**, 355 (2006).

[8] P. W. Anderson and W. F. Brinkman, Theory of anisotropic superfluidity in $^3$He, in *Physics of Liquid and Solid Helium*, edited by K. H. Bennemann and J. B. Ketterson, Pt. II (Wiley, New York, 1978), pp. 177–286.

[9] D. Vollhardt and P. Wölfle, *The Superfluid Phases of Helium 3* (Taylor & Francis, London, 1990).

[10] M. M. Wysokiński and J. Spałek, Properties of an almost localized Fermi liquid in an applied magnetic field revisited: A statistically consistent Gutzwiller approach, *J. Phys.: Condens. Matter* **26**, 055601 (2014).

[11] D. Aoki, K. Ishida, and J. Flouquet, Review of U- based ferromagnetic superconductors: Comparison between UGe₂, URhGe, and UCoGe, *J. Phys. Soc. Jpn.* **88**, 022001 (2019).

[12] E. Kądzielawa-Major, M. Fidrysiak, P. Kubiczek, and J. Spałek, Spin-triplet paired phases inside a ferromagnet induced by Hund’s rule coupling and electronic correlations: Application to UGe₂, *Phys. Rev. B* **97**, 224519 (2018).

[13] A. Harada, S. Kawasaki, H. Mukuda, Y. Kitaoka, Y. Haga, E. Yamamoto, Y. Ōnuki, K. M. Itoh, E. E. Haller, and H. Harima, Experimental evidence for ferromagnetic spin-pairing superconductivity emerging in UGe₂: A $^{73}$Ge-nuclear-quadrupole-resonance study under pressure, *Phys. Rev. B* **75**, 140502(R) (2007).

[14] N. Tateiwa, T. C. Kobayashi, K. Amaya, Y. Haga, R. Settai, and Y. Ōnuki, Heat-capacity anomalies at $T_{\rm sc}$ and $T^*$ in the ferromagnetic superconductor UGe₂, *Phys. Rev. B* **69**, 180513(R) (2004).

[15] K. G. Sandeman, G. G. Lonzarich, and A. J. Schofield, Ferromagnetic Superconductivity Driven by Changing Fermi Surface Topology, *Phys. Rev. Lett.* **90**, 167005 (2003).

[16] M. M. Wysokiński, M. Abram, and J. Spałek, Ferromagnetism in UGe₂: A microscopic model, *Phys. Rev. B* **90**, 081114(R) (2014).

[17] M. M. Wysokiński, M. Abram, and J. Spałek, Criticalities in the itinerant ferromagnet UGe₂, *Phys. Rev. B* **91**, 081108(R) (2015).

[18] M. M. Wysokiński, J. Kaczmarczyk, and J. Spałek, Correlation-driven $d$-wave superconductivity in Anderson lattice model: Two gaps, *Phys. Rev. B* **94**, 024517 (2016).

[19] M. Abram, M. M. Wysokiński, and J. Spałek, Tricritical wings in UGe₂: A microscopic interpretation, *J. Magn. Magn. Mater.* **400**, 27 (2016).

[20] P. Kubiczek, Spin-triplet pairing in orbitally degenerate Anderson lattice model, MSc thesis, Jagiellonian University, Kraków, Poland, 2016.

[21] J. Kaczmarczyk, T. Schickling, and J. Bünemann, Evaluation techniques for Gutzwiller wave functions in finite dimensions, *Phys. Status Solidi B* **252**, 2059 (2015).

[22] A. Biborski, A. P. Kądzielawa, and J. Spałek, Atomization of correlated molecular-hydrogen chain: A fully microscopic variational Monte Carlo solution, *Phys. Rev. B* **98**, 085112 (2018).

[23] J. Bünemann, T. Schickling, and F. Gebhard, Variational study of Fermi surface deformations in Hubbard models, *Europhys. Lett.* **98**, 27006 (2012).

[24] J. Kaczmarczyk, J. Bünemann, and J. Spałek, High-temperature superconductivity in the two-dimensional $t$-$J$ model: Gutzwiller wavefunction solution, *New J. Phys.* **16**, 073018 (2014).

[25] M. Fidrysiak, M. Zegrodnik, and J. Spałek, Realistic estimates of superconducting properties for the cuprates: Reciprocal-space diagrammatic expansion combined with variational approach, *J. Phys.: Condens. Matter* **30**, 475602 (2018).

[26] F. Gebhard, Gutzwiller correlated wave functions in finite dimensions $d$: A systematic expansion in $1/d$, *Phys. Rev. B* **41**, 9452 (1990).

[27] M. Zegrodnik, J. Bünemann, and J. Spałek, Even-parity spin-triplet pairing by purely repulsive interactions for orbitally degenerate correlated fermions, *New J. Phys.* **16**, 033001 (2014).

[28] J. Spałek, A. Datta, and J. M. Honig, Discontinuous Metal-Insulator Transitions and Fermi-Liquid Behavior of Correlated Electrons, *Phys. Rev. Lett.* **59**, 728 (1987).

[29] T. Terashima, T. Matsumoto, C. Terakura, S. Uji, N. Kimura, M. Endo, T. Komatsubara, and H. Aoki, Evolution of Quasiparticle Properties in UGe₂ with Hydrostatic Pressure Studied via the De Haas–Van Alphen Effect, *Phys. Rev. Lett.* **87**, 166401 (2001).

[30] M. Manago, S. Kitagawa, K. Ishida, K. Deguchi, N. K. Sato, and T. Yamamura, Enhancement of superconductivity by pressure-induced critical ferromagnetic fluctuations in UCoGe, *Phys. Rev. B* **99**, 020506(R) (2019).

[31] S. Ran, C. Eckberg, Q.-P. Ding, Y. Furukawa, T. Metz, S. R. Saha, I-L. Liu, M. Zic, H. Kim, J. Paglione, and N. P. Butch, Spontaneously polarized half-gapped superconductivity, arXiv:1811.11808 .

[32] J. Spałek, Spin-triplet superconducting pairing due to local Hund’s rule and Dirac exchange, *Phys. Rev. B* **63**, 104513 (2001).

[33] Y. Takahashi, *Spin Fluctuation Theory of Itinerant Electron Magnetism* (Springer, Berlin, 2013).

[34] A. Klejnberg and J. Spałek, Hund’s rule coupling as the microscopic origin of the spin-triplet pairing in a correlated and degenerate band system, *J. Phys.: Condens. Matter* **11**, 6553 (1999).

[35] A. Klejnberg and J. Spałek, Metal-insulator transition, gap opening due to the combined orbital-spin ordering, and spin-triplet superconductivity, *Phys. Rev. B* **61**, 15542 (2000).

[36] J. Bünemann, W. Weber, and F. Gebhard, Multiband Gutzwiller wave functions for general on-site interactions, *Phys. Rev. B* **57**, 6896 (1998).

[37] J. Spałek and M. Zegrodnik, Spin-triplet paired state induced by Hund’s rule coupling and correlations: A fully statistically consistent Gutzwiller approach, *J. Phys.: Condens. Matter* **25**, 435601 (2013).

[38] M. Zegrodnik, J. Spałek, and J. Bünemann, Coexistence of spin-triplet superconductivity with magnetism within a single mechanism for orbitally degenerate correlated electrons: Statistically consistent Gutzwiller approximation, *New J. Phys.* **15**, 073050 (2013).

[39] A. B. Shick and W. E. Pickett, Magnetism, Spin-Orbit Coupling, and Superconducting Pairing in UGe₂, *Phys. Rev. Lett.* **86**, 300 (2001).

205106-12

[40] A. B. Shick, V. Janiš, V. Drchal, and W. E. Pickett, Spin and orbital magnetic state of UGe₂ under pressure, *Phys. Rev. B* **70**, 134506 (2004).

[41] J. Karbowski and J. Spałek, Interorbital pairing for heavy fermions and universal scaling of their basic characteristics, *Phys. Rev. B* **49**, 1454 (1994).

[42] O. Howczak, J. Kaczmarczyk, and J. Spałek, Pairing by Kondo interaction and magnetic phases in the Anderson-Kondo lattice model: Statistically consistent renormalized mean-field theory, *Phys. Status Solidi B* **250**, 609 (2013).

[43] E. Kądzielawa-Major, Exchange interactions, electronic states, and pairing of electrons in correlated and hybridized systems, Ph.D. thesis, Jagiellonian University, Kraków, Poland, 2018.

[44] A. Klejnberg and J. Spałek, Simple treatment of the metal-insulator transition: Effects of degeneracy, temperature, and applied magnetic field, *Phys. Rev. B* **57**, 12041 (1998).

[45] W. E. Evenson, J. R. Schrieffer, and S. Q. Wang, New approach to the theory of itinerant electron ferromagnets with local-moment characteristics, *J. Appl. Phys.* **41**, 1199 (1970).

[46] U. Lindner, A generalized Ginzburg-Landau functional for systems with correlation, *J. Phys.: Condens. Matter* **3**, 347 (1991).